# Shared nonlinear encoder check

Status: implementation and pre-execution checks. The primary experiment is uniform SSL warmup followed by uniform/frozen/adaptive sampling forks. A predeclared unlabeled PCA initialization control tests whether the square result depends on initially factorized geometry.

The main possible falsifier is that ordinary SSL warmup already learns a tetrahedral four-state arrangement, which can remain stable under filtering. In that event the earlier square result cannot support a blanket claim about pretrained encoders.

See protocol.md for the fixed design and criteria. Code and results will be linked here after execution. No representation training labels or image-performance claims are used.
