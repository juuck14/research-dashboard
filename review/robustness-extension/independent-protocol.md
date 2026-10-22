# 독립 gradient 검산 규약

2026-10-22. Root의 robustness-extension 결과를 읽은 뒤 시행하는 사후 독립 코드 감사다. 새 효과 탐색이나 seed 선택을 하지 않는다.

- run_checks.py의 function definitions만 AST로 읽어 실행하며 학습 main은 다시 실행하지 않는다. norm, qfun, positive, exactfield, evaluate의 실제 구현을 그대로 로드한다.
- 독립 scalar population loss를 anchor/positive/negative 64쌍 합으로 구현한다. eta={0,.01,.1}, random unit embeddings seeds={77,2011,4027}, uniform / q(square) / q(current)를 각기 고정해 16개 ambient coordinate의 normalized retraction 중앙차분(h=1e-6)을 계산한다. root의 projected exactfield와 최대 오차1e-7 이내인지 확인한다. q(current)를 FD 중 재갱신하면 detached 검산이 아니므로 금지한다.
- eta channel eigenvalues를 {1,1-2eta,1-2eta,(1-2eta)^2}와 대조한다. identity-positive에서 root SGD expected counts gradient와 exactfield가 일치하는지 검사한다.
- 평가 함수는 equal-prior four-state isotropic Gaussian-mixture Bayes factor rule인지 식으로 검사하고 square 및 완전한 one-factor representation의 sanity 값을 실행한다. 실제 final vectors를 재평가한 것으로 오해하지 않는다.
- 결과에는 root source SHA256, 체크 수, 최대 오차와 해석 범위를 기록한다. 코드를 고치거나 기존 결과를 덮지 않는다.
