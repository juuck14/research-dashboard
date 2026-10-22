# 세 연구 방향의 실제 사전 연구

시작일: 2026-10-22 KST. 기존 추천은 검증되지 않은 출발 가설이다.

## 연구 단위

- [부분 식별](../partial-identification/README.md): 허용 모형 및 변환을 고정한 뒤 동일 관측분포를 만드는 대안 잠재구조와 공통 부분구조를 찾는다.
- [Negative 피드백](../negative-feedback/README.md): positive law를 고정하고 full-support 독립·고정·적응 정책에서 population 선호와 갱신 효과를 분리한다.
- [Target 교정](../target-correction/README.md): 입력·초기 target에 정보가 있는 상태에서 frozen·갱신 teacher의 고정점 및 안정성을 비교한다.

## 증거와 판정 규칙

문헌의 결과, 직접 증명, 수치 확인, 미검증 추측을 구분한다. 검색 결과·초록만 확인한 논문으로 정리 범위를 추정하지 않는다. 실험 실행 전 각 주제 protocol.md에 설계·seed·판정 조건을 적고 이후 변경은 이유와 함께 남긴다. 합성 oracle와 실제 학습기를 구별하고 모집단·유한표본·최적화 차이를 섞지 않는다. 단일 사례로 일반 불가능성을 주장하지 않는다.

최종 판정은 진행 권고 / 수정 후 진행 / 기각 / 판정 보류 중 하나다. 진행 권고에는 핵심 명제의 실질적 지지와 논문 초안을 요구한다. 핵심 가설 자체가 미검증이면 보류로 표시한다. 독립 검토자가 직접 중복·논리·대안 설명을 공격한 기록을 review/에 보존한다.

## 실행 및 저장

환경은 CPU Python 3.12, NumPy/SciPy/Matplotlib/Pandas를 우선 사용한다. GPU나 대형 모델을 초기 증거의 전제로 삼지 않는다. 원문 PDF와 임시 데이터는 저장소에 올리지 않고 인용 URL·읽은 절·필요한 재현 코드와 작은 결과표/그림을 보존한다. 기존 최종보고 snapshot은 [여기](original-report-2026-10-21.md).

## 현황

2026-10-22 완료: 부분 식별 및 자기 target 교정은 현재 정식화 기각, negative는 normalized full-capacity feedback 경계로 수정 후 진행. 증명·exact population 계산·독립 검토·toy minibatch SGD를 수행했다. [최종 종합보고](final_report.md), [재현 안내](reproduction.md). 구체적 결과와 반론은 각 주제 및 review 디렉터리에 있다.
