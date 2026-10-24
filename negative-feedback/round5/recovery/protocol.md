# Recovery rerun protocol — 2026-10-25

The final 2026-10-23 upload did not complete. Workspace maintenance removed unpushed files. The published checkpoint256f7e94225174aac36eeb0667a8f6a9741992a1 remains intact. This is a NEW rerun, not recovered original output bytes. Prior reported numerical observations are historical conversation records until rerun. No publication-complete claim is made from the interrupted tool call.

Before execution: C4/6,d=C,tau1,epsilon.01,omega=exp(-.9s),K1/4096,seeds7701/7702. Each seed uses a normalized Gaussian initialization or an explicitly generated .01 Gaussian perturbation of the balanced antipodal state. Fixed step2,cap20000; stop only after100 steps on a20-step checkpoint with96-node expected-field norm<1e-8 (64node during updates;96node endpoint). No settings changed after outcomes. Save all endpoints, metrics, intermediate snapshots and wall times.

Theorem prediction: every stable stationary geometry at K4096 has off-GramMSE<=.02474255(C4)or.02969105(C6), radius>=.68848907/.51606330. K1 bound is vacuous; exact coarse eigenvalues establish bad stable points. Runs are converged candidates, not all equilibrium enumeration. Independently calculate full product-sphere spectra at the preselected C6seed7701 coarse-initialized endpoints for both K; tolerance1e-6 for numerical rotation residuals. A trajectory cap or apparent bound violation is preserved and investigated, not silently tuned.

Training uses the published checkpoint oracle, with no external data or GPU. This is population flow, not sampled-index SGD. Previously executed sampled-index outputs after the checkpoint were lost; do not relabel these new population outputs as their recovery.
