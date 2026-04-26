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
  required = %w[theme.css manifest.json README.md CHANGELOG.md LICENSE snippets/zz-obsidian-gray-force-override-v2.css docs/fixtures/table-report.md docs/fixtures/table-preview.html docs/fixtures/live-preview-editing.md screenshots/light.png screenshots/dark.png screenshots/report.png screenshots/table-sample.png]
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
    "screenshots/report.png" => [512, 288],
    "screenshots/table-sample.png" => [1946, 1988]
  }
  png_sizes.each do |path, expected|
    data = File.binread(path, 24)
    fail_with("#{path} is not a PNG") unless data.start_with?("\x89PNG\r\n\x1A\n".b)
    width, height = data.byteslice(16, 8).unpack("NN")
    fail_with("#{path} expected #{expected.join('x')}, got #{width}x#{height}") unless [width, height] == expected
  end
  info("screenshot PNG dimensions match expected sizes")

  release_workflow = read(".github/workflows/release.yml")
  release_assets = %w[theme.css manifest.json README.md CHANGELOG.md LICENSE snippets/zz-obsidian-gray-force-override-v2.css]
  missing_assets = release_assets.reject { |asset| release_workflow.match?(/^\s{12}#{Regexp.escape(asset)}\s*$/) }
  fail_with("release workflow missing assets: #{missing_assets.join(', ')}") unless missing_assets.empty?
  info("release workflow includes README assets")

  css_sources = {
    "theme.css" => theme,
    "snippets/zz-obsidian-gray-force-override-v2.css" => read("snippets/zz-obsidian-gray-force-override-v2.css")
  }
  forbidden_live_preview_rules = {
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-line\s*\{[^}]*margin-(?:top|bottom)\s*:\s*(?:[1-9]|0\.[1-9]|[a-zA-Z_-])[^;}]*/m => "non-zero margin on CM6 .cm-line",
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-line\s*\{[^}]*line-height\s*:\s*(?:[0-9]|var\(|calc\(|normal\b)[^;}]+/m => "global line-height override on CM6 .cm-line",
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-content\s*\{[^}]*overflow-wrap\s*:\s*anywhere/m => "overflow-wrap:anywhere on CM6 .cm-content",
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+\.cm-content\s*\{[^}]*word-break\s*:\s*keep-all/m => "word-break:keep-all on CM6 .cm-content",
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-quote[^{}]*\{[^}]*background(?:-color)?\s*:\s*(?:#|rgb|hsl|var\(|linear-gradient)[^;}]+/m => "non-transparent Live Preview quote background",
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-quote[^{}]*\{[^}]*border(?:-left|-inline-start)?\s*:\s*(?:[1-9]|0\.[1-9]|[a-zA-Z_-])[^;}]*/m => "decorative Live Preview quote border",
    /(?:body\s+)?\.markdown-source-view\.mod-cm6\s+[^{}]*HyperMD-header-[3-6][^{}]*\{[^}]*z-index\s*:\s*(?:-?\d+|var\()[^;}]+/m => "stacking z-index on Live Preview H3-H6"
  }
  css_sources.each do |path, content|
    forbidden_live_preview_rules.each do |pattern, description|
      fail_with("#{path}: #{description}") if content.match?(pattern)
    end
  end
  info("Live Preview editability guards clean")

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
