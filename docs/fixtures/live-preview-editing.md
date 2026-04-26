# Owen Graphite Live Preview Editing Fixture

이 문서는 Live Preview 편집 hitbox 회귀 확인용 샘플입니다. Reading View 장식보다 Live Preview의 커서 배치와 클릭 편집성을 우선 확인합니다.

## 1. Heading 주변 문장

**헤더 위 문장**: 굵은 텍스트로 시작하는 일반 문장입니다. 이 줄 전체를 클릭했을 때 편집 커서가 정상적으로 들어와야 합니다.

#### 1.1 H4 heading click target

헤더 아래 일반 문장입니다. 제목의 아래 여백과 겹치지 않고 첫 번째 글자부터 마지막 글자까지 편집 가능해야 합니다.

## 2. Wrapped blockquote

#### 2.1 Blockquote after heading

> 조직 내 특정 사용자/그룹 간 Teams·SharePoint·OneDrive·Exchange 커뮤니케이션·공유를 **단방향 또는 양방향으로 제한**하는 긴 blockquote 문장입니다. 화면 폭을 줄였을 때 두 번째 시각 줄과 세 번째 시각 줄도 클릭 편집이 되어야 합니다.

다음 일반 문장도 blockquote 영역이나 제목 여백에 가려지지 않아야 합니다.

## 3. Callout editing and icons

> [!info] Info callout
> DSPM for AI 자체는 E5 Compliance에 포함되지만, Copilot/Agent 활동 데이터를 실제로 수집·분석하려면 라이선스 조건과 collection policy 조건을 함께 확인해야 합니다.
>
> - 분석 대상자가 Copilot for M365 라이선스를 보유해야 합니다.
> - 긴 bullet 문장이 줄바꿈되어도 두 번째 시각 줄을 클릭해 편집할 수 있어야 합니다.

> [!warning] Warning callout
> 위험/주의 callout은 의미 색을 유지하되 Live Preview 편집성에는 영향을 주지 않아야 합니다.

> [!success] Success callout
> 성공/완료 callout은 일반 텍스트와 리스트가 정상적으로 편집되어야 합니다.

## 4. Inline formatting mix

일반 문장 안의 **굵은 글자**, *기울임*, `inline-code`, [[Internal Link]], https://example.com/path/to/a/very/long/url/value 조합이 줄바꿈되어도 클릭 위치와 커서 위치가 크게 어긋나지 않아야 합니다.

## 5. Table adjacency

#### 5.1 Heading before table

| 항목 | 설명 | 상태 |
|---|---|---|
| Live Preview | 제목과 표 사이 클릭 영역 확인 | OK |
| Wrapped text | 표 뒤의 긴 문장과 heading 간격 확인 | OK |

표 아래 문장입니다. 표 widget과 다음 문장 사이에서 클릭 편집이 정상 동작해야 합니다.
