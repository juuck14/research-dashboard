# 직접 실행 결과

## Base unconstrained model
- Exact population flow1,080 설정/초기값 반복, 확인540. 모두 이론적 deadline 내 amplitude.1에 도달.
- Finite-difference gradient max error3.92194e−11.
- Hitting time은 sampling exposure로 약100배 달라질 수 있으나 frozen/adaptive 차이는 작았다.
- 결과: 이 모형의 permanent-omission 가설은 반박.

## N1 normalized additive mode
-672 설정, eps{.01,.1,.5},kappa{-8,-4,-2,-1,-.5,0,2},offset±1e−3/±1e−5,seed101/211,policy4.
- Curvature analytic–FD max error1.11769e−10.
- eps.1,kappa−2: frozen+.1879519276, adaptive−.2186626593. Same initial theta=.7864159047의 t200 amplitude adaptive3.0e−10/frozeninitial.70555/frozencenter.70711/uniform.70711.
- Finite time에 정확한 정보소실이라고 주장하지 않는다.

## N2 multiple negatives
- K{1,2,4,8,16}×eps3×kappa7=105 exact multinomial 조건.
- Probabilitysum maxerror3.55271e−15, analytic–FD4.52812e−10.
- eps.1,kappa−2의 factor-balance signflip 전부 유지. K16 frozen+1.11835605/adaptive−.80668974.

## Importance control
-90 조건, exact expectation에서 uniform correction field equality maxerror1.38778e−15.
- 따라서 same-uniform-objective optimization failure가 아니다.

## 독립 검산
- review/negative-feedback/: d3/d4 full-sphere mode 및 flow, K2/4 full tangent, no-selfnegative 검산.
- review/three-factor-extension/: root의 별도3-factor fullsphere numeric extension.

각 수치는 동일한 원자료의 test set 반복이 아니라 작은 모집단의 결정론적 수치 분석이다. config/seed/tolerance와 실행 코드는 해당 Python 파일 및 protocol.md에 있다.
