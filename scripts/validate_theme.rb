#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"
require "open3"

ROOT = File.expand_path("..", __dir__)
TARGET = ENV.fetch("OWEN_GRAPHITE_TARGET", "/Users/owen/work/Obsidian/.obsidian/themes/Owen Graphite")
CI_MODE = ARGV.include?("--ci")

def fail_with(message)
  warn "ERROR: #{message}"
  exit 1
end

def info(message)
  puts "OK: #{message}"
end

def read(path)
  File.read(File.join(ROOT, path))
end

Dir.chdir(ROOT) do
  required = %w[theme.css manifest.json README.md CHANGELOG.md LICENSE screenshots/light.png screenshots/dark.png screenshots/report.png]
  missing = required.reject { |path| File.file?(path) && File.size(path).positive? }
  fail_with("missing required files: #{missing.join(', ')}") unless missing.empty?
  info("required files present")

  manifest = JSON.parse(read("manifest.json"))
  version = manifest.fetch("version")
  fail_with("manifest version must be semver, got #{version}") unless version.match?(/\A\d+\.\d+\.\d+\z/)
  fail_with("manifest name mismatch") unless manifest["name"] == "Owen Graphite"
  info("manifest.json version=#{version}")

  changelog = read("CHANGELOG.md")
  readme = read("README.md")
  theme = read("theme.css")
  fail_with("CHANGELOG missing #{version} header") unless changelog.include?("## [#{version}]")
  fail_with("README missing #{version} version") unless readme.include?("`#{version}`") || readme.include?("v#{version}")
  fail_with("theme.css missing v#{version} marker") unless theme.include?("v#{version}")
  info("version markers aligned")

  legacy_version = ["1", "7", "6"].join(".")
  legacy_pattern = /v?#{Regexp.escape(legacy_version)}/
  stale_hits = []
  Dir.glob("**/*", File::FNM_DOTMATCH).each do |path|
    next if File.directory?(path)
    next if path.start_with?(".git/")
    next if path == ".DS_Store"

    begin
      content = File.binread(path)
      stale_hits << path if content.valid_encoding? && content.match?(legacy_pattern)
    rescue ArgumentError
      next
    end
  end
  fail_with("stale legacy marker found in: #{stale_hits.join(', ')}") unless stale_hits.empty?
  info("no stale legacy markers")

  setting_ids = theme.scan(/^\s*id:\s*([a-zA-Z0-9_-]+)/).flatten
  option_count = setting_ids.reject { |id| id == "owen-graphite-document" }.uniq.size
  fail_with("expected 26 Style Settings options, got #{option_count}") unless option_count == 26
  fail_with("README missing 26 options text") unless readme.include?("26개 옵션") && readme.include?("26%20options")
  info("Style Settings option count=#{option_count}")

  png_sizes = {
    "screenshots/light.png" => [512, 288],
    "screenshots/dark.png" => [512, 288],
    "screenshots/report.png" => [512, 288]
  }
  png_sizes.each do |path, expected|
    data = File.binread(path, 24)
    fail_with("#{path} is not a PNG") unless data.start_with?("\x89PNG\r\n\x1A\n".b)
    width, height = data.byteslice(16, 8).unpack("NN")
    fail_with("#{path} expected #{expected.join('x')}, got #{width}x#{height}") unless [width, height] == expected
  end
  info("screenshots are 512x288 PNGs")

  diff_check, diff_err, diff_status = Open3.capture3("git", "diff", "--check")
  fail_with("git diff --check failed:\n#{diff_check}#{diff_err}") unless diff_status.success?
  info("git diff --check clean")

  if !CI_MODE && Dir.exist?(TARGET)
    diff_out, diff_err, diff_status = Open3.capture3(
      "diff", "-qr", "--exclude=.git", "--exclude=.DS_Store", ROOT, TARGET
    )
    fail_with("target vault theme differs:\n#{diff_out}#{diff_err}") unless diff_status.success?
    info("target vault theme is synchronized")
  else
    info("target vault sync check skipped")
  end
end
