---
title: "본문 문서 디자인 강화 샘플"
type: sample
tags: [type/sample, topic/owen-graphite, topic/document-design]
created: 2026-05-06
updated: 2026-05-06
cssclasses:
  - ogd-report-mode
  - ogd-modern-tables
  - ogd-print-avoid-breaks
  - ogd-spacing-relaxed
---

# 본문 문서 디자인 강화 샘플

> [!summary] 핵심 요약
> 이 문서는 Owen Graphite의 본문 디자인을 강화할 때 확인해야 할 문단 리듬, 제목 계층, callout, 표와 캡션, 다이어그램, 코드 블록, 체크리스트를 한 흐름으로 배치한 샘플이다. 실제 개선 작업에서는 이 문서를 Reading View, Live Preview, PDF 출력에서 함께 확인한다.

Owen Graphite의 본문은 화려한 장식보다 문서의 구조가 먼저 읽히는 방향이 어울린다. 제목은 섹션의 시작점을 분명하게 만들고, 문단은 긴 한국어 문장을 읽어도 피로하지 않도록 충분한 행간을 유지한다.

표, callout, 코드, 다이어그램은 각각 독립된 장식 요소가 아니라 본문 흐름 안에서 같은 간격 체계로 이어져야 한다. 아래 샘플은 그 기준을 한 문서에서 점검하기 위한 기준 문서다.

## 1. 문단 리듬과 제목 계층

문단 리듬은 본문 디자인의 첫인상을 결정한다. 너무 촘촘하면 보고서가 압축된 메모처럼 보이고, 너무 넓으면 정보 밀도가 낮아져 위키 문서의 탐색성이 떨어진다. Owen Graphite에서는 기본 문단은 차분하게, 섹션 시작 전 여백은 조금 더 넓게 두는 방향이 적합하다.

두 번째 문단은 앞 문단과 자연스럽게 이어져야 한다. 문단 사이 여백은 제목 여백보다 작아야 하며, 표나 callout 다음에는 독자가 다시 본문으로 돌아올 수 있도록 약간의 호흡이 필요하다.

### 1.1 H3는 본문 안의 안내자

H3는 새 장을 여는 제목이라기보다 독자가 긴 섹션 안에서 위치를 잃지 않도록 돕는 안내자에 가깝다. 그래서 H2보다 가볍고, 본문과 너무 멀어지지 않아야 한다.

#### 1.1.1 H4는 보조 분기

H4 이하 제목은 강조보다 정렬감이 중요하다. 굵기와 크기를 과하게 키우기보다, 본문보다 조금 강한 밀도와 안정적인 여백으로 구분한다.

> 인용문은 본문보다 한 단계 낮은 목소리로 보이는 것이 좋다. 왼쪽 세로 장식에 의존하기보다, 배경과 테두리의 미묘한 차이로 보조 정보임을 표현한다.

### 1.2 아주 긴 제목이 들어왔을 때 줄바꿈과 하단 rule이 본문을 밀어내지 않는지 확인하는 스트레스 테스트

긴 제목은 실제 보고서에서 자주 나온다. 제목이 두 줄 이상으로 접힐 때 하단 rule, 번호, 접기 아이콘, 다음 문단의 첫 줄이 서로 겹치지 않아야 한다. 모바일 폭에서는 제목이 자연스럽게 줄바꿈되고, Reading View와 Live Preview의 줄 높이가 크게 달라지지 않는지도 확인한다.

#### 1.2.1 H4에서도 길이가 긴 보조 제목이 들어올 때 계층은 유지하되 본문보다 과하게 커지지 않는지 확인

보조 제목은 문서의 깊이를 보여주지만, 본문보다 더 큰 시각적 소음을 만들면 안 된다. 이 문단은 H4 아래에서 본문이 바로 따라올 때 위쪽 여백과 아래쪽 여백이 안정적인지 확인하기 위한 문장이다.

## 2. Callout은 정보 박스가 아니라 문서 구조다

Callout은 색상으로만 구분하면 문서 전체가 산만해진다. Owen Graphite에서는 기본 표면을 흰색/회색 frosted glass로 유지하고, 의미색은 얕은 rim, chip, icon, halo 수준에서만 드러나는 방향이 적합하다.

> [!note] 기준 정보
> `note`와 `info`는 본문 흐름을 보조하는 가장 중립적인 정보 박스다. 제목은 짧게, 본문은 두세 문장 안에서 끝내는 것이 읽기 좋다.

> [!tip] 작성 팁
> 실무 문서에서는 callout을 모든 문단에 적용하지 않는다. 요약, 판단, 위험, 실행 항목처럼 독자가 빠르게 찾아야 하는 정보에만 사용한다.

> [!warning] 출력 전 확인
> PDF 출력이 필요한 문서에서는 callout이 페이지 하단에서 잘리지 않는지 확인한다. 긴 callout은 두 개의 짧은 callout으로 나누는 편이 안정적이다.

> [!success] 완료 기준
> callout의 역할이 제목만 보고도 구분되고, 본문으로 돌아왔을 때 문서 흐름이 끊기지 않으면 성공이다.

> [!risk] 긴 callout 스트레스 테스트
> 긴 callout은 PDF 출력에서 중간 분할 위험이 높고, Live Preview에서는 접기 아이콘과 본문 줄 간격이 어긋날 수 있다. 이 샘플은 두 문단 이상으로 이어지는 callout이 표면, 테두리, 제목, 본문 간격을 안정적으로 유지하는지 확인하기 위한 것이다.
>
> 두 번째 문단에서는 실제 보고서의 위험 설명처럼 문장이 길어지는 상황을 가정한다. 의미색은 강조를 돕는 수준에 머물러야 하며, callout 전체가 강한 색 면으로 보이면 Owen Graphite의 차분한 문서 톤과 맞지 않는다.

## 3. 표와 캡션

표는 Owen Graphite의 핵심 사용처다. 표 자체의 선과 배경만 다듬는 것보다, 표 앞뒤 문맥과 캡션을 함께 정리해야 문서 품질이 올라간다.

<p class="table-caption">표 1. 문서 구성 요소별 디자인 역할</p>

| 구성 요소 | 역할 | 강화 방향 | 점검 기준 |
| --- | --- | --- | --- |
| 제목 | 구조 안내 | H2/H3/H4 위계 차등화 | 긴 문서에서 위치가 바로 읽히는가 |
| 문단 | 읽기 흐름 | 행간과 문단 간격 정리 | 한국어 장문이 답답하지 않은가 |
| Callout | 의미 구분 | 얕은 rim과 chip 중심 | 색이 과하지 않은가 |
| 표 | 비교와 판단 | caption과 주변 여백 정리 | 본문과 자연스럽게 이어지는가 |

표 바로 뒤 문단은 표를 다시 해석하는 문장이어야 한다. 표 안에 모든 설명을 밀어 넣으면 행 높이가 커지고 PDF 출력에서 분할 위험이 커진다.

### 3.1 비교표 샘플

<table class="wide-table comparison-table print-fit-table">
  <thead>
    <tr>
      <th>패턴</th>
      <th>장점</th>
      <th>위험</th>
      <th>권장 사용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>문단 중심</td>
      <td>서사가 자연스럽고 원문 Markdown이 읽기 쉽다.</td>
      <td>핵심 판단이 묻힐 수 있다.</td>
      <td>배경 설명, 분석 서술</td>
    </tr>
    <tr>
      <td>표 중심</td>
      <td>비교와 상태 파악이 빠르다.</td>
      <td>긴 문장을 넣으면 폭이 무너진다.</td>
      <td>기능 비교, 위험도, 현황판</td>
    </tr>
    <tr>
      <td>Callout 중심</td>
      <td>요약과 판단을 빠르게 찾을 수 있다.</td>
      <td>남용하면 본문 계층이 약해진다.</td>
      <td>핵심 결론, 주의, 실행 항목</td>
    </tr>
  </tbody>
</table>

<p class="table-caption">표 2. 본문 패턴별 사용 기준</p>

### 3.2 긴 셀과 줄바꿈 샘플

긴 식별자, 정책명, 설명 문장이 표 안에 들어오면 셀 높이가 커지고 모바일 폭에서 레이아웃이 흔들릴 수 있다. 아래 표는 `wrap-table`과 `print-fit-table`을 함께 확인하기 위한 스트레스 샘플이다.

<table class="wide-table comparison-table wrap-table print-fit-table">
  <thead>
    <tr>
      <th>항목</th>
      <th>긴 설명</th>
      <th>식별자</th>
      <th>확인 포인트</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>보고서 섹션</td>
      <td>PDF 출력 전 마지막 검토 단계에서 본문 문단, callout, 표, Mermaid, 이미지 캡션이 같은 간격 체계로 이어지는지 확인한다.</td>
      <td><code>ogd-document-body-rhythm-balanced-report-reading-check</code></td>
      <td>긴 코드 토큰이 셀 밖으로 밀려나지 않는가</td>
    </tr>
    <tr>
      <td>위키 노트</td>
      <td>짧은 항목을 빠르게 스캔하는 문서에서도 제목과 표가 과하게 벌어지지 않고, 리스트가 본문 폭 안에서 자연스럽게 중첩되는지 확인한다.</td>
      <td><code>owen-graphite-wiki-note-compact-navigation-context</code></td>
      <td>문장 줄바꿈과 행 높이가 안정적인가</td>
    </tr>
  </tbody>
</table>

<p class="table-caption">표 3. 긴 표 셀과 코드 토큰 줄바꿈 점검</p>

## 4. 이미지와 다이어그램 캡션

이미지나 Mermaid 다이어그램은 본문보다 먼저 시선을 끌기 때문에 주변 여백과 캡션이 중요하다. 캡션은 작고 차분해야 하며, 이미지와는 가깝게, 다음 문단과는 조금 멀게 배치되는 것이 좋다.

![](../../screenshots/readme/v2.22.31-liquid-glass-overview.svg)

<p class="figure-caption">그림 1. README liquid glass overview 이미지 임베드</p>

```mermaid
flowchart LR
  A[초안 작성] --> B[본문 리듬 정리]
  B --> C[표와 callout 배치]
  C --> D[Reading View 점검]
  D --> E[PDF 출력 확인]
```

<p class="figure-caption">그림 2. 본문 문서 디자인 점검 흐름</p>

다이어그램 뒤 문단은 그림에서 말하지 않은 해석을 제공해야 한다. 단순히 그림 내용을 반복하기보다, 다음 단계에서 무엇을 확인할지 안내하는 문장이 좋다.

## 5. 코드 블록과 인라인 코드

기술 문서에서는 코드 블록이 문서 분위기를 크게 바꾼다. Owen Graphite의 코드 블록은 IDE처럼 강한 색을 쓰기보다, graphite 표면 위에 읽기 쉬운 대비를 제공하는 방향이 적합하다.

```css
.markdown-preview-view p {
  line-height: 1.78;
  margin-block: 0.72em;
}

.markdown-preview-view h2 {
  margin-block-start: 2.2em;
}
```

```ts
type DocumentSurface = "reading" | "live-preview" | "pdf";

interface BodyDesignCheck {
  surface: DocumentSurface;
  headingRhythm: "stable" | "too-tight" | "too-loose";
  calloutTone: "neutral-glass" | "too-colorful";
  captionFlow: "clear" | "missing" | "overlapping";
}

const checks: BodyDesignCheck[] = [
  {
    surface: "reading",
    headingRhythm: "stable",
    calloutTone: "neutral-glass",
    captionFlow: "clear",
  },
  {
    surface: "live-preview",
    headingRhythm: "stable",
    calloutTone: "neutral-glass",
    captionFlow: "clear",
  },
];

const needsFollowUp = checks.some((check) =>
  check.headingRhythm !== "stable" ||
  check.calloutTone !== "neutral-glass" ||
  check.captionFlow !== "clear"
);
```

인라인 코드인 `ogd-spacing-relaxed`, `comparison-table`, `print-fit-table`은 본문 안에서 튀지 않아야 한다. 배경은 충분히 구분되되, 문장 리듬을 끊을 만큼 진하면 안 된다.

## 6. 체크리스트와 실행 항목

체크리스트는 문서 마지막에서 실행 상태를 정리할 때 가장 자주 쓰인다. 완료 상태는 취소선만으로 처리하기보다 색상, 투명도, 체크박스 표면이 함께 정돈되면 더 읽기 쉽다.

- [x] H2/H3/H4 제목 계층 확인
- [x] 본문 문단 간격과 표 뒤 여백 확인
- [x] callout 색상 과다 사용 여부 확인
- [ ] 이미지와 표 caption 패턴 CSS 적용
- [ ] Reading View, Live Preview, PDF 출력 비교

중첩 리스트는 위키 문서에서 자주 나온다. 들여쓰기 guide가 너무 강하면 본문이 복잡해 보이고, 너무 약하면 구조가 흐려진다.

- 문서 구조 점검
  - 제목 계층
    - H2는 섹션 시작점
    - H3는 본문 안의 안내자
  - 본문 흐름
    - 문단 간격
    - 표 뒤 해석 문단
- 출력 안정성 점검
  - PDF 분할 회피
  - 모바일 폭 줄바꿈
  - 다크 모드 대비

> [!todo] 다음 개선 단위
> 1차 구현은 문단 리듬과 제목 계층부터 시작한다. 그 다음 callout, 표/이미지 caption, 코드 블록, 체크리스트 순서로 적용하면 회귀 범위를 좁게 유지할 수 있다.

## 7. 다크 모드 확인 메모

다크 모드에서는 흰색 glass surface를 그대로 반전시키면 검은 카드처럼 보일 수 있다. Owen Graphite의 다크 모드는 pure black보다 slate glass와 낮은 contrast rim을 중심으로 유지하는 편이 안정적이다.

> [!note] 다크 모드 점검
> callout, inline code, caption, table header, task checkbox가 모두 같은 어두운 graphite 계열 안에서 읽혀야 한다. warning이나 success 같은 의미색도 배경 면 전체가 아니라 테두리와 icon chip에 얕게 남는 것이 좋다.

| 점검 대상 | 기대 상태 | 위험 신호 |
| --- | --- | --- |
| Caption | 낮은 채도의 slate text | 본문보다 더 강하게 보임 |
| Code block | graphite panel + 읽기 쉬운 대비 | pure black에 가까운 과한 대비 |
| Callout | 얕은 의미색 rim | warning/error가 강한 색 카드처럼 보임 |
| Checkbox | frost aqua focus가 얕게 보임 | 체크 표시가 흐리거나 너무 밝음 |

## 8. PDF 분할 스트레스 샘플

아래 callout은 의도적으로 길게 작성한 PDF 분할 점검용 블록이다. 출력 시 한 페이지 하단에서 제목만 남거나, 테두리와 그림자가 다음 페이지로 어색하게 넘어가지 않는지 확인한다.

> [!warning] 긴 PDF 분할 점검 블록
> PDF 출력에서 문서 요소가 페이지 하단에 걸리면 읽기 흐름이 쉽게 깨진다. 특히 callout, 표, 코드 블록, Mermaid 다이어그램은 내부 요소가 여러 줄로 구성되어 있어서 분할 회피 규칙이 실제로 잘 작동하는지 확인해야 한다.
>
> 이 문단은 두 번째 단락이다. 긴 설명이 들어가도 callout 내부 line-height가 안정적이어야 하며, title 영역과 content 영역의 간격이 지나치게 벌어지면 안 된다.
>
> 이 문단은 세 번째 단락이다. 다크 모드와 라이트 모드 모두에서 의미색이 얕은 테두리와 icon chip 수준으로 제한되는지, 본문 가독성이 충분한지 확인한다.

## 9. 출력 점검 메모

이 샘플 문서를 실제 개선 작업의 smoke sample로 사용할 때는 다음 순서로 확인한다.

1. Reading View에서 문단과 제목 간격이 안정적인지 본다.
2. Live Preview에서 표와 callout 높이가 과하게 팽창하지 않는지 확인한다.
3. PDF 출력에서 callout, 표, Mermaid가 중간 분할되지 않는지 확인한다.
4. 모바일 폭에서 제목, 표, 코드 블록이 본문 폭을 밀어내지 않는지 확인한다.
5. 다크 모드에서 caption, inline code, checklist, warning callout의 대비가 안정적인지 확인한다.

> [!conclusion] 결론
> Owen Graphite의 본문 디자인 강화는 새로운 장식을 추가하는 작업이 아니라, 문서의 읽기 리듬과 정보 위계를 더 분명하게 만드는 작업이다. 이 샘플은 그 방향을 실제 Markdown 문서로 검토하기 위한 기준점이다.
