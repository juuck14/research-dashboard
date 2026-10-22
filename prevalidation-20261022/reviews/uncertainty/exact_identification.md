# Unknown scalar positive concentration does not imply non-identification

**상태: 직접 증명.** 주담당의 증명 아이디어를 별도로 검산했다. 수치적 fitting은 증명이 아니다. circle, homoscedastic von Mises emission, uniform latent, 알려진 mean map을 갖는 제한 모형이다. 일반 probabilistic neural encoder 전체를 식별했다는 정리가 아니다.

## 모형과 관측

Z는 circle의 uniform 분포다. X|Z는 concentration a>0의 von Mises이고 mean은 Z다. Z+|Z는 concentration b>0의 von Mises positive transition이며 X+|Z+도 같은 emission이다. 모두 conditional independent하게 생성한다. 관측 pair angle difference의 Fourier 계수는

`B_n(a,b) = [I_n(a)/I_0(a)]² [I_n(b)/I_0(b)], n≥1`.

이는 convolution theorem의 직접 대입이다. observation ambiguity a와 correspondence b의 구분이 target이며 a,b는 **양의 유한 scalar**다. a=0 또는 b=0이면 모든 비상수 coefficient가 0이므로 joint identification은 불가능하다.

## 명제

모든 `B_n(a,b)`가 정확히 주어지면 (a,b)는 위 범위에서 유일하다. 따라서 알려진 positive concentration을 unknown scalar로 바꾸는 것만으로 이 subclass가 비식별이라고 주장할 수 없다.

## 증명

`x=a²/4`, `y=b²/4`로 둔다. Bessel의 수렴하는 양의 series에서

`I_n(a)=(a/2)^n/n! × S_n(x)`,

`S_n(x)=sum_{k≥0} x^k/[k!(n+1)…(n+k)]`.

고정 x에 대해 k≥4 tail은 `sum_{k≥4}(x/n)^k/k! = O(n^-4)`로 지배된다. k=0,1,2,3을 전개하고 `log(1+u)`를 쓰면

`log S_n(x) = x/n − x/n² + (x−x²/2)/n³ + O(n^-4)`.

따라서 `D_n=log B_n+3log(n!)`는

`D_n = n log L + C + S/n − S/n² + (S−R/2)/n³ + O(n^-4)`,

`L=x sqrt(y)`, `C=−2log I0(a)−log I0(b)`, `S=2x+y`, `R=2x²+y²`.

관측 sequence에서 순차 극한으로 `log L=lim D_n/n`, `C=lim(D_n−nlog L)`, `S=lim n(D_n−nlog L−C)`, 마지막으로 `S−R/2=lim n³(D_n−nlog L−C−S/n+S/n²)`를 얻는다.

이 값들은 cubic polynomial

`p(u)=u³−Su²+[(S²−R)/2]u−L²=(u−x)²(u−y)`

를 유일하게 결정한다. x≠y이면 x는 유일한 double root이고 y는 simple root다. x=y이면 triple root 하나다. 두 경우 모두 x,y가 유일하므로 `a=2sqrt(x)`, `b=2sqrt(y)`가 유일하다. QED.

## 증명이 뜻하지 않는 것

- 모든 harmonics를 정확히 관측하는 모집단 식별성이다. 유한 표본에서 고차 harmonics는 아주 작을 수 있다.
- a=b에서 각 harmonic의 Jacobian이 rank1인 것과 global injection은 양립한다. 정규적인 inverse conditioning이나 root-n 추정을 보장하지 않는다.
- mean map·encoder family·heteroscedastic a(x)를 함께 학습하면 다른 문제다.
- PCL2023의 알려진-kernel posterior theorem을 부정하거나 확장한 일반 정리가 아니다. 그 정리의 uncertainty confounding 해석에 대한 제한적인 반례다.
- 직접 확인한 고전 문헌에서 이 정확한 triple-von-Mises concentration 정리를 찾지는 못했으나, 그 사실만으로 학술적 신규성을 주장하지 않는다.

## Root의 singular-path 계산에 대한 추가 증명 검토

**직접 증명.** `f_m(c)=log[I_m(c)/I0(c)]`라 두자. 임의 고정 c>0에서 경로 `a=c+t,b=c−2t`의 계수는

`B_m(t)=B_m(0)[1+3 f_m''(c)t²−f_m'''(c)t³+O(t⁴)]`.

양의 vM density들의 convolution은 compact circle에서 양의 하한을 갖고 parameter의 모든 유한차 미분이 연속이다. 따라서 density에 대해 uniform하게 `p_t=p0+t²A+t³B+O(t⁴)`로 전개할 수 있다. A,B가 0이 아니라는 사실은 수치 확인만 필요하지 않다. 위 Bessel series 전개는 c의 compact neighborhood에서 세 번까지 항별 미분 가능하며

`f_m''(c)=−m/c²−(log I0)''(c)+O(m^-1)`,

`f_m'''(c)=2m/c³−(log I0)'''(c)+O(m^-1)`.

그러므로 충분히 큰 m에서 각각 nonzero다. `B_m(0)>0`이므로 A,B의 Fourier coefficient도 각각 하나 이상 nonzero다. Fourier uniqueness에서 A,B는 영함수가 아니다.

양의 하한을 이용한 KL의 Taylor 전개는 모든 c>0에서

`KL(p_t || p0) = (t⁴/2) ∫ A²/p0 + O(t⁵)`,

`KL(p_t || p_{−t}) = 2t⁶ ∫ B²/p0 + O(t⁸)`

를 준다. 두 leading constant는 양수다. 이는 이 특정 두 simple-hypothesis 판별의 차수를 보장한다. estimator의 minimax upper bound, unknown nuisance를 profile한 full local experiment, 일반 neural encoder의 속도는 증명하지 않는다.

이 algebra는 새로운 singular-inference 일반론이 아니다. Rotnitzky–Cox–Bottai–Robins2000의 s=2 magnitude/sign 구분과 직접 대조해야 한다.
