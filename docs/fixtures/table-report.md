# Owen Graphite Table Report Fixture

이 문서는 `v1.8.7` 테이블 출력 회귀 확인용 샘플입니다. Reading View, Live Preview, 모바일 폭, PDF Export에서 표 폭, 긴 셀, 숫자 정렬, 위험도 badge, 표 주석을 확인합니다.

## 1. Wide Comparison Table

<table class="wide-table print-fit-table comparison-table nowrap-code-table">
  <thead>
    <tr>
      <th>항목</th>
      <th>정책 설명</th>
      <th>장문 식별자</th>
      <th class="num">점수</th>
      <th>권장 조치</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Baseline</td>
      <td>기본 보안 기준을 만족하지만 일부 예외 정책이 존재합니다.</td>
      <td><code>sec-Restrict-Tenant-Access-Policy-prod-eastasia-2026-review</code></td>
      <td class="num">95.2%</td>
      <td>예외 정책 만료일을 명시하고 분기별 검토에 포함합니다.</td>
    </tr>
    <tr>
      <td>Conditional Access</td>
      <td>사용자·디바이스·위치 조건별 MFA 강제 정책이 분리되어 있습니다.</td>
      <td><code>ca-policy-high-risk-signin-global-exclusion-breakglass</code></td>
      <td class="num">88.7%</td>
      <td>Break-glass 계정 제외 사유를 별도 표로 추적합니다.</td>
    </tr>
  </tbody>
</table>

<p class="table-source">Internal review fixture, 2026 Q2.</p>

## 1-1. Scroll Token Table

<table class="wide-table scroll-table scroll-token-table">
  <thead>
    <tr>
      <th>유형</th>
      <th>식별자</th>
      <th>검토 메모</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tenant policy</td>
      <td><code>sec-Restrict-Tenant-Access-Policy-prod-eastasia-2026-review</code></td>
      <td>행 높이보다 식별자 스캔성이 중요할 때 사용합니다.</td>
    </tr>
    <tr>
      <td>Conditional Access</td>
      <td><code>ca-policy-high-risk-signin-global-exclusion-breakglass</code></td>
      <td>화면 검토에서는 ellipsis, PDF에서는 print-fit 조합을 확인합니다.</td>
    </tr>
  </tbody>
</table>

## 2. Risk Table

<table class="risk-table compact-table">
  <thead>
    <tr>
      <th>리스크</th>
      <th>영향</th>
      <th>완화책</th>
      <th>상태</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>예외 정책 누락</td>
      <td>PDF 보고서에서 정책 추적성이 낮아질 수 있음</td>
      <td>예외 목록을 표준 appendix로 분리</td>
      <td class="risk-high">High</td>
    </tr>
    <tr>
      <td>긴 URL 셀 overflow</td>
      <td>모바일과 A4 출력에서 표 폭이 밀릴 수 있음</td>
      <td><code>wrap-table</code> 적용</td>
      <td class="risk-medium">Medium</td>
    </tr>
    <tr>
      <td>숫자 컬럼 가독성</td>
      <td>점수 비교가 어려워질 수 있음</td>
      <td><code>numeric-table</code> 또는 <code>.num</code> 적용</td>
      <td class="risk-ok">OK</td>
    </tr>
  </tbody>
</table>

<p class="table-note">상태 셀은 <code>.risk-high</code>, <code>.risk-medium</code>, <code>.risk-low</code>, <code>.risk-ok</code> 클래스로 명시합니다.</p>

## 3. Numeric Table

<table class="numeric-table print-fit-table">
  <thead>
    <tr>
      <th>월</th>
      <th>요청</th>
      <th>완료</th>
      <th>성공률</th>
      <th>평균 처리일</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>2026-01</td><td>1,204</td><td>1,178</td><td>97.84%</td><td>2.4</td></tr>
    <tr><td>2026-02</td><td>982</td><td>951</td><td>96.84%</td><td>2.8</td></tr>
    <tr><td>2026-03</td><td>1,341</td><td>1,309</td><td>97.61%</td><td>2.1</td></tr>
  </tbody>
</table>

## 4. Matrix Table

<table class="matrix-table compact-table">
  <thead>
    <tr>
      <th>영향도 \ 가능성</th>
      <th>Low</th>
      <th>Medium</th>
      <th>High</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>High</td><td class="risk-medium">M</td><td class="risk-high">H</td><td class="risk-high">H</td></tr>
    <tr><td>Medium</td><td class="risk-low">L</td><td class="risk-medium">M</td><td class="risk-high">H</td></tr>
    <tr><td>Low</td><td class="risk-low">L</td><td class="risk-low">L</td><td class="risk-medium">M</td></tr>
  </tbody>
</table>