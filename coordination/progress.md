# 종합 연구 이력

## 2026-10-22 시작

- 실행: 기존 보고서와 juuck14/research-dashboard의 README·root inventory를 확인했다. 기존 파일은 README 하나이며 기존 연구 디렉터리는 없다.
- 실행: 세 독립 담당에게 부분 식별 / negative 피드백 / 자기 target 교정의 원문 검증·정식화·분석·실험을 배정했다.
- 계획: 1차 결과를 GitHub에 저장한 뒤 다른 담당의 교차 비판과 추가 실행으로 검증한다.
- 판단: 기존 추천 순위와 서지정보는 증거로 채택하지 않는다. 각 주제는 원문 및 직접 결과로 다시 판정한다.
- 미해결: 세 방향 모두 아직 핵심 결과와 신규성 검증이 없다.

## 2026-10-22 중간 결과 1

- 직접 분석·실행: 부분 식별에서 동일 관측법칙의 Gaussian 회전 대안, 제한된 모형의 정확 각도집합, 표본 무관 하한을 확보했다. 41개 oracle 조건과 360 표본 반복을 실행했다. 독립 검토는 추가 400사례와 GL shear 반례를 실행했다.
- 교정: 관측 whitening은 소스 기준 covariance=I 가정을 정당화하지 않는다. 이 추가 가정을 명시하고 일반 GL/비선형 모형에서는 exact set가 아닌 feasible alternatives/lower bounds로 범위를 줄였다.
- 문헌 대조: Gaussian 평균 TC와 기존 AJD contrast가 정확히 같아 현재 간결한 독립 주제는 기각 쪽이다. 자세한 근거는 topic 및 review 디렉터리 원문 대조에 있다.
- 직접 분석·실행: negative의 unnormalized identity-positive exact population family에서는 full-support floor 아래 누락 factor 방향이 transverse repelling이며 유한 탈출 상한이 있다. 1080개 조건/초기값 계산에서 반례가 없었다. 이 숫자는 독립 실데이터 시험 수가 아니다.
- 새 가설·추가 실행 중: normalized family에서는 balanced representation의 matched-frozen sampling은 안정하지만 adaptive sampling은 불안정할 수 있다. 독립 full-tangent lookup 계산에서도 확인돼 additive parameterization만의 결과는 아니다. 여러 negatives와 선행 performative/self-paced learning 대조가 아직 필요하다.
- 직접 분석·실행: target correction의 선형 full-rank 시작에서 frozen/EMA가 다르게 수렴할 수 있지만 Tian–Chen–Ganguli2021 Lemma1에 정확히 환원된다. 유한시간 amplitude 감소를 정보소실로 부르는 해석을 제거했다. 별도 reviewer가 54 고정점과 유한지지 rank1 정보보존 반례를 실행했다.
- 다음: negative 추가 주장의 다중-negative 강건성과 신규성, 각 topic 최종 판정, 재현 파일 검사를 마친다. 현상 존재와 독립 논문의 가치가 다르다는 점을 판정에 반영한다.

## 2026-10-22 최종 분석과 반론 해결

- 판정: 부분 식별·target 교정은 현재의 간결한 독립 주제로서 기각. Negative는 unnormalized 원가설을 반박한 뒤 normalized full-capacity matched-frozen/adaptive stability로 수정 후 진행.
- 직접 증명: negative K1의 모든 tangent mode spectrum과 두 안정성 부등식을 도출. Independent critic은 d3/d4·K2/K4·self-negative 제외에서도 검산.
- 추가 원문 대조: performative prediction과 self-paced implicit loss의 일반 instability 설명을 강력한 경쟁선행으로 인정. 별도 novelty reviewer의 신중론을 삭제하지 않음.
- Root 실행: 세 요인 8상태 d4/d8 complete tangent54조건 및54확인. 충분 차원에서도 matched-frozen 안정/adaptive 불안정 유지.
- Root 실행: symmetric bit-flip positive 채널 eta=.001/.01/.05/.1에서도 full-rank channel·stability difference 확인. 이 실험은 exact population이며 실제 SGD의 positive는 identity라는 구분 유지.
- Root 실행: SGD30회(6 primary+4 confirmation seeds×3policies). 사전 기준5/6·3/4에 대해 실제6/6·4/4 통과. 고정 feature noise=.05의 Bayes factor accuracy를 사용했으며 MI 소실로 해석하지 않음.
- Independent audit: root positive-gradient432차분 최대오차1.24e−10, SGD 기대gradient 일치5.20e−17, Bayes 평가 sanity 통과.
- 재현 보강: 재학습 없이 평가할 수 있도록 30개 최종 작은 embedding을 저장. 코드 변경 뒤 동일 seed 재실행해 기존 결과 불변 여부 확인.
- 종합보고: final_report.md, 주제별 README/verdict 및 negative paper_draft.md에 확보한 결과·기각·미해결을 연결. 완료 후 최종 commit을 main에 push하고 원격 readback으로 보존 확인.
