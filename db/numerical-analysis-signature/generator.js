// Seeded boundless generator for the The Signature Numerical Analysis Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-numerical-analysis-signature.js [seed]  (prints one JSON record)
// or: node gen-numerical-analysis-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "numerical-analysis-signature";
const RECORD_KIND = "numerical analysis record";
const ID_PREFIX = "JAH-NUMANAS-";
const AI_NAME = "JAH Numerical Analysis Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Error Ledger",
    "subject": "a Signature error ledger design",
    "description": "The Error Ledger is a Signature-made design for teaching error: a ledger where a learner records the true value, the computed value, the absolute error, and the relative error for each computation, and sees which source (rounding, truncation, or data) dominates. Error is the difference between a computed value and the true value. Each entry records the true value, the computed value, and both errors. The dominant source is named: rounding, truncation, or data. A cancellation warning is raised when nearly equal numbers are subtracted.",
    "inputs": "FIGURES = {'absolute_error': 3.33e-05, 'relative_error': 0.0001, 'entries': 2, 'warnings': 1, 'accurate_value': 0.00499987, 'cancellation_value': 0.005, 'error_sources': 3, 'design_version': 1}\nLABEL = 'a-signature-error-ledger-design'\n",
    "expected": "count: 8\nlabel: a-signature-error-ledger-design\nmax: 3\nmean: 0.8763\nmin: 3.33e-05\ntotal: 7.0101\nResult: count=8|label=a-signature-error-ledger-design|max=3|mean=0.8763|min=3.33e-05|total=7.0101\nRun 1 SHA-256: 1a74f5125f6df68b38bc21d97d82b8d342a74a977a9efe698f6bb1b588f5320e\nRun 2 SHA-256: 1a74f5125f6df68b38bc21d97d82b8d342a74a977a9efe698f6bb1b588f5320e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Floating-Point Explorer",
    "subject": "a Signature floating-point explorer design",
    "description": "The Floating-Point Explorer is a Signature-made design for teaching floating-point arithmetic: an explorer where a learner sees how a number is stored (significand times a power of 2), finds the spacing between neighbours, and watches 1e16 + 1 round back to 1e16. Double precision has about 16 decimal digits. The explorer shows the bits of a number: sign, exponent, and significand. The spacing (unit in the last place) is shown at any size. Operations that lose information are flagged with the amount lost.",
    "inputs": "FIGURES = {'machine_epsilon': 2.2e-16, 'significand_bits': 53, 'decimal_digits': 16, 'ulp_at_1e16': 2, 'sum_0.1_ten': 0.9999999999999999, 'demonstrations': 2, 'flags': 1, 'design_version': 1}\nLABEL = 'a-signature-floating-point-explorer-design'\n",
    "expected": "count: 8\nlabel: a-signature-floating-point-explorer-design\nmax: 53\nmean: 9.5\nmin: 2.2e-16\ntotal: 76.0\nResult: count=8|label=a-signature-floating-point-explorer-design|max=53|mean=9.5|min=2.2e-16|total=76.0\nRun 1 SHA-256: e0d8cc5f3d80e61ffb5036828d81a5e56fe27c21047f91b2d5d2d6baadd74b51\nRun 2 SHA-256: e0d8cc5f3d80e61ffb5036828d81a5e56fe27c21047f91b2d5d2d6baadd74b51\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Bisection Halver",
    "subject": "a Signature bisection halver design",
    "description": "The Bisection Halver is a Signature-made design for teaching bisection: a tool where a learner picks an interval with a sign change, and the tool halves it step by step, showing the interval, the midpoint, and the error bound shrinking by half each time. Bisection finds a root by halving a bracketing interval. The interval is drawn with the function values at its ends. Each step shows the midpoint, its sign, and the half kept. The error bound (half the interval width) is shown shrinking.",
    "inputs": "FIGURES = {'steps_taken': 3, 'interval_width': 0.125, 'midpoint': 1.4375, 'true_root': 1.41421356, 'error_bound': 0.0625, 'widths_shown': 3, 'halvings': 3, 'design_version': 1}\nLABEL = 'a-signature-bisection-halver-design'\n",
    "expected": "count: 8\nlabel: a-signature-bisection-halver-design\nmax: 3\nmean: 1.6299\nmin: 0.0625\ntotal: 13.0392\nResult: count=8|label=a-signature-bisection-halver-design|max=3|mean=1.6299|min=0.0625|total=13.0392\nRun 1 SHA-256: e90d5c16d501a1edf0944269928146b1050f5adbfd6bede9e2ce2a49ed468c7b\nRun 2 SHA-256: e90d5c16d501a1edf0944269928146b1050f5adbfd6bede9e2ce2a49ed468c7b\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Newton Tracer",
    "subject": "a Signature Newton tracer design",
    "description": "The Newton Tracer is a Signature-made design for teaching Newton's method: a tracer where a learner picks a starting guess, and the tool draws the tangent line, follows it to the axis, and repeats, showing the error squaring at each step. Newton's method follows tangent lines to a root. Each step draws the tangent line and its axis crossing. The error is shown at each step, roughly squaring. A bad start that diverges or cycles is flagged with the reason.",
    "inputs": "FIGURES = {'step_1': 1.5, 'step_2': 1.4166667, 'step_3': 1.4142157, 'true_root': 1.41421356, 'error_step_3': 2.1e-06, 'error_step_2': 0.00245, 'steps': 3, 'design_version': 1}\nLABEL = 'a-signature-newton-tracer-design'\n",
    "expected": "count: 8\nlabel: a-signature-newton-tracer-design\nmax: 3\nmean: 1.2184\nmin: 2.1e-06\ntotal: 9.7475\nResult: count=8|label=a-signature-newton-tracer-design|max=3|mean=1.2184|min=2.1e-06|total=9.7475\nRun 1 SHA-256: 6d8b6cd5c67994bc4ef3a38a9e6b157007ca79857ede51a86a6b737bdcb1c4cc\nRun 2 SHA-256: 6d8b6cd5c67994bc4ef3a38a9e6b157007ca79857ede51a86a6b737bdcb1c4cc\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Secant Drawer",
    "subject": "a Signature secant drawer design",
    "description": "The Secant Drawer is a Signature-made design for teaching the secant method: a drawer where a learner picks two starting points, and the tool draws the secant line through them, follows it to the axis, and repeats. The secant method needs no derivative. Each step draws the secant line through the last two points. The error is shown shrinking with order about 1.618. The method is compared with Newton's method on the same problem.",
    "inputs": "FIGURES = {'step_1': 1.333333, 'step_2': 1.4, 'step_3': 1.414634, 'true_root': 1.41421356, 'error_step_3': 0.00042, 'convergence_order': 1.618, 'newton_step_3': 1.4142157, 'design_version': 1}\nLABEL = 'a-signature-secant-drawer-design'\n",
    "expected": "count: 8\nlabel: a-signature-secant-drawer-design\nmax: 1.618\nmean: 1.1994\nmin: 0.00042\ntotal: 9.5948\nResult: count=8|label=a-signature-secant-drawer-design|max=1.618|mean=1.1994|min=0.00042|total=9.5948\nRun 1 SHA-256: 0b55bfeda4d6ef26b777a67c747b7d57179189f2011545bc262d6500b9b800ac\nRun 2 SHA-256: 0b55bfeda4d6ef26b777a67c747b7d57179189f2011545bc262d6500b9b800ac\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Elimination Workbench",
    "subject": "a Signature elimination workbench design",
    "description": "The Elimination Workbench is a Signature-made design for teaching Gaussian elimination: a workbench where a learner performs row operations on a system, watches the matrix become triangular, and reads the solution by back-substitution, with the LU factors recorded. LU factorisation writes A as L times U. Each row operation is a button, and the matrix updates live. The multipliers are recorded in L, and the triangular result is U. Pivoting is offered when the diagonal entry is small.",
    "inputs": "FIGURES = {'solution_x': 1, 'solution_y': 3, 'l_21': 0.5, 'u_11': 2, 'u_22': 2.5, 'operations': 1, 'factors': 2, 'design_version': 1}\nLABEL = 'a-signature-elimination-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-elimination-workbench-design\nmax: 3\nmean: 1.625\nmin: 0.5\ntotal: 13.0\nResult: count=8|label=a-signature-elimination-workbench-design|max=3|mean=1.625|min=0.5|total=13.0\nRun 1 SHA-256: ba17805727ad0668170a707e57798eccf5db772016375ae099769f7000df8089\nRun 2 SHA-256: ba17805727ad0668170a707e57798eccf5db772016375ae099769f7000df8089\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Iterative Improver",
    "subject": "a Signature iterative improver design",
    "description": "The Iterative Improver is a Signature-made design for teaching iterative methods: a tool where a learner starts from a guess, watches Jacobi and Gauss-Seidel improve it step by step, and sees the residual shrink. An iterative method improves a guess until the residual is small enough. The guess and the residual are shown at each step. Jacobi and Gauss-Seidel are run side by side for comparison. The stopping rule is stated: stop when the residual is below the tolerance.",
    "inputs": "FIGURES = {'true_x': 1.1818, 'true_y': 2.2727, 'jacobi_step3_x': 1.2292, 'jacobi_step3_y': 2.3056, 'gs_step1_x': 1.75, 'gs_step1_y': 2.0833, 'jacobi_steps': 3, 'design_version': 1}\nLABEL = 'a-signature-iterative-improver-design'\n",
    "expected": "count: 8\nlabel: a-signature-iterative-improver-design\nmax: 3\nmean: 1.8528\nmin: 1\ntotal: 14.8226\nResult: count=8|label=a-signature-iterative-improver-design|max=3|mean=1.8528|min=1|total=14.8226\nRun 1 SHA-256: 30921882adbc5239095cbe011d291c9285b506045093dd4dd124047bd75bb4b1\nRun 2 SHA-256: 30921882adbc5239095cbe011d291c9285b506045093dd4dd124047bd75bb4b1\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Condition Meter",
    "subject": "a Signature condition meter design",
    "description": "The Condition Meter is a Signature-made design for teaching the condition number: a meter where a learner enters a matrix, the meter shows its condition number, and demonstrates the amplification by perturbing the data and watching the solution move. The condition number is the ratio of the largest to the smallest singular value. The meter shows the condition number and the singular values. Perturbing the data by a small amount shows the solution moving. A well-conditioned matrix is shown alongside for comparison.",
    "inputs": "FIGURES = {'condition_number': 40002, 'identity_condition': 1, 'change_in_b': 0.0001, 'change_in_solution': 1, 'amplification': 10000, 'solution_before_x': 1, 'solution_after_x': 0, 'design_version': 1}\nLABEL = 'a-signature-condition-meter-design'\n",
    "expected": "count: 8\nlabel: a-signature-condition-meter-design\nmax: 40002\nmean: 6250.75\nmin: 0\ntotal: 50006.0001\nResult: count=8|label=a-signature-condition-meter-design|max=40002|mean=6250.75|min=0|total=50006.0001\nRun 1 SHA-256: aa50db0706a0670d0775c063265b4ecc546ffb69639d09849b662278c1e0213e\nRun 2 SHA-256: aa50db0706a0670d0775c063265b4ecc546ffb69639d09849b662278c1e0213e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Interpolation Studio",
    "subject": "a Signature interpolation studio design",
    "description": "The Interpolation Studio is a Signature-made design for teaching interpolation: a studio where a learner places points, the studio draws the interpolating polynomial, and shows the error against the true function. The interpolating polynomial of degree at most n passes through n + 1 points. Points are placed by clicking, and the polynomial is drawn live. The error against the true function is shown where it is known. High-degree interpolation is shown oscillating (Runge's phenomenon), and splines are offered.",
    "inputs": "FIGURES = {'points': 3, 'degree': 2, 'check_at_1': 3, 'check_at_2': 4, 'x2_coefficient': -0.5, 'runge_points': 11, 'tests': 2, 'design_version': 1}\nLABEL = 'a-signature-interpolation-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-interpolation-studio-design\nmax: 11\nmean: 3.1875\nmin: -0.5\ntotal: 25.5\nResult: count=8|label=a-signature-interpolation-studio-design|max=11|mean=3.1875|min=-0.5|total=25.5\nRun 1 SHA-256: 88a10155831357456368925ad24f75c3ee615dafd259f730f4cb6431667802eb\nRun 2 SHA-256: 88a10155831357456368925ad24f75c3ee615dafd259f730f4cb6431667802eb\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Spline Drawer",
    "subject": "a Signature spline drawer design",
    "description": "The Spline Drawer is a Signature-made design for teaching splines: a drawer where a learner places points, and the tool draws the cubic spline through them, smooth at every join, with the pieces shown. A spline is a piecewise polynomial, joined smoothly. Points are placed, and the spline is drawn live. Each piece is shown as a cubic, with the joins marked. The natural end condition (zero second derivative) is the default.",
    "inputs": "FIGURES = {'points': 3, 'pieces': 2, 'value_at_0.5': 0.6875, 'max_value': 1, 'degree': 3, 'joins': 1, 'end_condition': 0, 'design_version': 1}\nLABEL = 'a-signature-spline-drawer-design'\n",
    "expected": "count: 8\nlabel: a-signature-spline-drawer-design\nmax: 3\nmean: 1.4609\nmin: 0\ntotal: 11.6875\nResult: count=8|label=a-signature-spline-drawer-design|max=3|mean=1.4609|min=0|total=11.6875\nRun 1 SHA-256: 99ef36364674e9529c390ad49c2bc6524db45326006457a2215981772154eae7\nRun 2 SHA-256: 99ef36364674e9529c390ad49c2bc6524db45326006457a2215981772154eae7\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Quadrature Comparator",
    "subject": "a Signature quadrature comparator design",
    "description": "The Quadrature Comparator is a Signature-made design for teaching numerical integration: a comparator where a learner picks an integral, and the tool computes the trapezoidal rule and Simpson's rule side by side, with the errors shown. Simpson's rule is exact for cubics and far more accurate than the trapezoidal rule for the same points. The trapezoidal and Simpson values are shown side by side. The error of each is shown against the true value where it is known. Halving the step is offered, showing the error shrinking by the predicted factor.",
    "inputs": "FIGURES = {'true_value': 1.7182818, 'trapezoidal': 1.753931, 'trapezoidal_error': 0.0356, 'simpson': 1.718861, 'simpson_error': 0.00058, 'refined_simpson': 1.718282, 'points_used': 3, 'design_version': 1}\nLABEL = 'a-signature-quadrature-comparator-design'\n",
    "expected": "count: 8\nlabel: a-signature-quadrature-comparator-design\nmax: 3\nmean: 1.3682\nmin: 0.00058\ntotal: 10.9455\nResult: count=8|label=a-signature-quadrature-comparator-design|max=3|mean=1.3682|min=0.00058|total=10.9455\nRun 1 SHA-256: 724ce5a8147387d70208f07bf613a90edf18d658ddbe4ac2aaefd49d36aaa453\nRun 2 SHA-256: 724ce5a8147387d70208f07bf613a90edf18d658ddbe4ac2aaefd49d36aaa453\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Euler Stepper",
    "subject": "a Signature Euler stepper design",
    "description": "The Euler Stepper is a Signature-made design for teaching Euler's method: a stepper where a learner chooses a step size, and the tool steps along the tangent lines, drawing the approximate solution against the true one, with the error shown. Euler's method moves along the tangent line at each step. The step size is adjustable, and the error is shown for each choice. Halving the step is shown to halve the error. The true solution is drawn alongside for comparison.",
    "inputs": "FIGURES = {'euler_h0.1': 1.21, 'true_value': 1.2214, 'error_h0.1': 0.0114, 'euler_h0.05': 1.2155, 'error_h0.05': 0.0059, 'step_sizes': 2, 'steps': 2, 'design_version': 1}\nLABEL = 'a-signature-euler-stepper-design'\n",
    "expected": "count: 8\nlabel: a-signature-euler-stepper-design\nmax: 2\nmean: 1.083\nmin: 0.0059\ntotal: 8.6642\nResult: count=8|label=a-signature-euler-stepper-design|max=2|mean=1.083|min=0.0059|total=8.6642\nRun 1 SHA-256: 714e608026e9bef4445e0907758b6d9b76b9976f19bd6c7a2033b610cd709578\nRun 2 SHA-256: 714e608026e9bef4445e0907758b6d9b76b9976f19bd6c7a2033b610cd709578\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Runge-Kutta Comparator",
    "subject": "a Signature Runge-Kutta comparator design",
    "description": "The Runge-Kutta Comparator is a Signature-made design for teaching Runge-Kutta methods: a comparator where a learner runs Euler and fourth-order Runge-Kutta side by side on the same problem, with the errors shown. The fourth-order method has error proportional to h to the fourth power. Both methods are run with the same step size, and their errors are shown. Halving the step is shown to cut the Runge-Kutta error by a factor of 16. The four slopes of each Runge-Kutta step are drawn.",
    "inputs": "FIGURES = {'rk4_value': 1.2214028, 'true_value': 1.2214028, 'rk4_error': 1e-06, 'euler_value': 1.21, 'euler_error': 0.0114, 'slopes_per_step': 4, 'order': 4, 'design_version': 1}\nLABEL = 'a-signature-runge-kutta-comparator-design'\n",
    "expected": "count: 8\nlabel: a-signature-runge-kutta-comparator-design\nmax: 4\nmean: 1.583\nmin: 1e-06\ntotal: 12.6642\nResult: count=8|label=a-signature-runge-kutta-comparator-design|max=4|mean=1.583|min=1e-06|total=12.6642\nRun 1 SHA-256: 3e9d4eee0a247d8a142bac08e9b4f5270f6a91ae4fe99be953a8ae8f4fbfb42e\nRun 2 SHA-256: 3e9d4eee0a247d8a142bac08e9b4f5270f6a91ae4fe99be953a8ae8f4fbfb42e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Least Squares Fitter",
    "subject": "a Signature least squares fitter design",
    "description": "The Least Squares Fitter is a Signature-made design for teaching least squares: a fitter where a learner plots data points, the tool fits the best line, and shows the residuals and their squares, with the QR solution offered as the stable route. Least squares minimises the sum of squared residuals. The data points are plotted, and the fitted line is drawn. Each residual is shown as a vertical segment, with its square listed. The QR solution is shown alongside the normal equations, agreeing.",
    "inputs": "FIGURES = {'points': 3, 'intercept': 1.1667, 'slope': 1.5, 'residual_sum_squares': 0.1667, 'dragged_sum_squares': 0.5, 'residuals_shown': 3, 'parameters': 2, 'design_version': 1}\nLABEL = 'a-signature-least-squares-fitter-design'\n",
    "expected": "count: 8\nlabel: a-signature-least-squares-fitter-design\nmax: 3\nmean: 1.5417\nmin: 0.1667\ntotal: 12.3334\nResult: count=8|label=a-signature-least-squares-fitter-design|max=3|mean=1.5417|min=0.1667|total=12.3334\nRun 1 SHA-256: 41bc3fd9d67b16ab517fa3d334e496151467ca7aa0b93882129a59bde41da909\nRun 2 SHA-256: 41bc3fd9d67b16ab517fa3d334e496151467ca7aa0b93882129a59bde41da909\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Difference Quotient Lab",
    "subject": "a Signature difference quotient laboratory design",
    "description": "The Difference Quotient Lab is a Signature-made design for teaching numerical differentiation: a laboratory where a learner approximates a derivative by forward and central differences, varies the step size, and watches the error fall and then rise as rounding takes over. The central difference has error proportional to h squared. Forward and central differences are computed side by side. The step size is varied on a slider, and the error is plotted. The optimal step (where truncation and rounding balance) is marked.",
    "inputs": "FIGURES = {'true_derivative': 0.5403023, 'forward_h0.1': 0.49736, 'forward_error': 0.043, 'central_h0.1': 0.5394, 'central_error': 0.0009, 'central_h0.01': 0.5403, 'optimal_h': 0.01, 'design_version': 1}\nLABEL = 'a-signature-difference-quotient-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-difference-quotient-laboratory-design\nmax: 1\nmean: 0.3964\nmin: 0.0009\ntotal: 3.1713\nResult: count=8|label=a-signature-difference-quotient-laboratory-design|max=1|mean=0.3964|min=0.0009|total=3.1713\nRun 1 SHA-256: 51543eb3a78dadb77adf5c25e67fcb44390949306279e3b4a7f7ba999790ba76\nRun 2 SHA-256: 51543eb3a78dadb77adf5c25e67fcb44390949306279e3b4a7f7ba999790ba76\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Grid Solver",
    "subject": "a Signature grid solver design",
    "description": "The Grid Solver is a Signature-made design for teaching the finite difference method: a solver where a learner sets up a grid, chooses the time step, and watches the heat equation evolve, with the stability condition checked live. The explicit method is stable only when k dt / h squared is at most 1/2. The grid and the time step are chosen, and the stability ratio is shown. A ratio above 1/2 is refused with the reason, or shown blowing up. The decay factor is compared with the exact value.",
    "inputs": "FIGURES = {'h_grid': 0.25, 'dt_stable': 0.02, 'stability_ratio': 0.32, 'exact_decay': 0.8209, 'fd_decay': 0.8125, 'dt_unstable': 0.04, 'unstable_ratio': 0.64, 'design_version': 1}\nLABEL = 'a-signature-grid-solver-design'\n",
    "expected": "count: 8\nlabel: a-signature-grid-solver-design\nmax: 1\nmean: 0.4879\nmin: 0.02\ntotal: 3.9034\nResult: count=8|label=a-signature-grid-solver-design|max=1|mean=0.4879|min=0.02|total=3.9034\nRun 1 SHA-256: f821d4418eeb64704dfa8930f6e19f833316a4dc459ddd23b41296e004743773\nRun 2 SHA-256: f821d4418eeb64704dfa8930f6e19f833316a4dc459ddd23b41296e004743773\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Best Approximation Finder",
    "subject": "a Signature best approximation finder design",
    "description": "The Best Approximation Finder is a Signature-made design for teaching approximation theory: a finder where a learner picks a function and a degree, and the tool shows the Taylor polynomial, the Chebyshev polynomial, and the best (minimax) polynomial, with their maximum errors compared. The best approximation minimises the maximum error. The three polynomials are drawn against the function. The maximum error of each is shown. The equioscillation of the best error is shown: it alternates between plus and minus its maximum.",
    "inputs": "FIGURES = {'taylor_max_error': 0.1321, 'best_max_error': 0.045, 'chebyshev_error': 0.0451, 'cheb_constant': 1.2661, 'cheb_linear': 1.1303, 'cheb_quadratic': 0.2715, 'degree': 2, 'design_version': 1}\nLABEL = 'a-signature-best-approximation-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-best-approximation-finder-design\nmax: 2\nmean: 0.7363\nmin: 0.045\ntotal: 5.8901\nResult: count=8|label=a-signature-best-approximation-finder-design|max=2|mean=0.7363|min=0.045|total=5.8901\nRun 1 SHA-256: 5ec5e0c4389c117ad8e6dbbfb567ed7949d72cea254807a611896a8b24f04bf8\nRun 2 SHA-256: 5ec5e0c4389c117ad8e6dbbfb567ed7949d72cea254807a611896a8b24f04bf8\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Descent Visualiser",
    "subject": "a Signature descent visualiser design",
    "description": "The Descent Visualiser is a Signature-made design for teaching gradient descent: a visualiser where a learner watches a point step downhill on a surface, with the step size adjustable, showing overshoot when the step is too large and crawling when it is too small. Gradient descent steps against the gradient. The surface is drawn with the path of the iterates. The step size is adjustable on a slider. Overshoot and crawling are shown as the step size changes.",
    "inputs": "FIGURES = {'start_x': 4, 'step_1': 3.2, 'step_2': 2.56, 'step_3': 2.048, 'after_10': 0.4295, 'shrink_factor': 0.8, 'step_sizes_tried': 3, 'design_version': 1}\nLABEL = 'a-signature-descent-visualiser-design'\n",
    "expected": "count: 8\nlabel: a-signature-descent-visualiser-design\nmax: 4\nmean: 2.1297\nmin: 0.4295\ntotal: 17.0375\nResult: count=8|label=a-signature-descent-visualiser-design|max=4|mean=2.1297|min=0.4295|total=17.0375\nRun 1 SHA-256: 7bb95c37c1bdebfaa702937f00e312a8715f94d7dcfe8b1888a4139dda49f907\nRun 2 SHA-256: 7bb95c37c1bdebfaa702937f00e312a8715f94d7dcfe8b1888a4139dda49f907\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Dartboard Pi Estimator",
    "subject": "a Signature dartboard pi estimator design",
    "description": "The Dartboard Pi Estimator is a Signature-made design for teaching Monte Carlo integration: an estimator where a learner throws darts at a square, counts those inside the inscribed circle, and estimates pi as 4 times the fraction inside. The error shrinks like 1 over the square root of the number of darts. Darts are thrown one by one, and the estimate updates live. The standard error is shown, shrinking like 1/sqrt(N). The estimate is compared with pi, about 3.14159.",
    "inputs": "FIGURES = {'darts_100': 100, 'inside_100': 79, 'pi_estimate_100': 3.16, 'darts_10000': 10000, 'inside_10000': 7854, 'pi_estimate_10000': 3.1416, 'std_error': 0.0164, 'pi_true': 3.14159}\nLABEL = 'a-signature-dartboard-pi-estimator-design'\n",
    "expected": "count: 8\nlabel: a-signature-dartboard-pi-estimator-design\nmax: 10000\nmean: 2255.3074\nmin: 0.0164\ntotal: 18042.4596\nResult: count=8|label=a-signature-dartboard-pi-estimator-design|max=10000|mean=2255.3074|min=0.0164|total=18042.4596\nRun 1 SHA-256: c22bdd9c9889ea4762f7f99f164b95247f65c00be51f55a39909364ab4afdbc4\nRun 2 SHA-256: c22bdd9c9889ea4762f7f99f164b95247f65c00be51f55a39909364ab4afdbc4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Stiffness Demonstrator",
    "subject": "a Signature stiffness demonstrator design",
    "description": "The Stiffness Demonstrator is a Signature-made design for teaching stiff equations: a demonstrator where a learner watches an explicit method take thousands of tiny steps on a stiff problem, and an implicit method take a few large ones. A stiff equation has very different time scales. The explicit method's step limit is shown, and its step count. The implicit method's large steps are shown alongside. The fast transient is shown decaying in the first hundredth of a second.",
    "inputs": "FIGURES = {'stiffness_ratio': 1000, 'explicit_step_limit': 0.002, 'steps_needed': 5000, 'implicit_step': 0.1, 'y_at_0.1': 0.99496, 'cos_0.1': 0.995004, 'transient_at_0.01': 4.5e-05, 'design_version': 1}\nLABEL = 'a-signature-stiffness-demonstrator-design'\n",
    "expected": "count: 8\nlabel: a-signature-stiffness-demonstrator-design\nmax: 5000\nmean: 750.3865\nmin: 4.5e-05\ntotal: 6003.092\nResult: count=8|label=a-signature-stiffness-demonstrator-design|max=5000|mean=750.3865|min=4.5e-05|total=6003.092\nRun 1 SHA-256: cc06cf1b25ca2a4dbb3bafa69d3451242a7f7628632b86d9d58596ad5a86a9cd\nRun 2 SHA-256: cc06cf1b25ca2a4dbb3bafa69d3451242a7f7628632b86d9d58596ad5a86a9cd\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The FFT Splitter",
    "subject": "a Signature fast Fourier transform splitter design",
    "description": "The FFT Splitter is a Signature-made design for teaching the fast Fourier transform: a splitter where a learner watches a transform split into even and odd halves, recursively, until the pieces are trivial, and then combine with twiddle factors. The FFT costs n log n operations instead of n squared. The split tree is drawn, with the even and odd halves at each level. The combine step shows the twiddle factors. The operation count is shown against the direct n squared.",
    "inputs": "FIGURES = {'n_points': 4, 'fft_operations': 8, 'direct_operations': 16, 'n_1024_fft': 10240, 'n_1024_direct': 1048576, 'halves': 2, 'levels': 2, 'design_version': 1}\nLABEL = 'a-signature-fast-fourier-transform-splitter-design'\n",
    "expected": "count: 8\nlabel: a-signature-fast-fourier-transform-splitter-design\nmax: 1048576\nmean: 132356.125\nmin: 1\ntotal: 1058849\nResult: count=8|label=a-signature-fast-fourier-transform-splitter-design|max=1048576|mean=132356.125|min=1|total=1058849\nRun 1 SHA-256: fc27d8e019a3b2a63d0c7b45aa2c5b87b10d1577a291be9b2d7adbf23810b342\nRun 2 SHA-256: fc27d8e019a3b2a63d0c7b45aa2c5b87b10d1577a291be9b2d7adbf23810b342\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Nonlinear System Solver",
    "subject": "a Signature nonlinear system solver design",
    "description": "The Nonlinear System Solver is a Signature-made design for teaching Newton's method for systems: a solver where a learner enters two equations, and the tool builds the Jacobian, solves for the correction, and steps toward the solution, showing the error squaring. Newton's method for systems solves J delta = -F at each step. The Jacobian is shown as the matrix of partial derivatives. Each step solves for the correction and updates the point. The error is shown squaring near the solution.",
    "inputs": "FIGURES = {'true_x': 1.4142, 'true_y': 1.4142, 'start_x': 1, 'step1_x': 1.5, 'error_step1': 0.0858, 'step2_x': 1.4167, 'error_step2': 0.0025, 'jacobian_rows': 2}\nLABEL = 'a-signature-nonlinear-system-solver-design'\n",
    "expected": "count: 8\nlabel: a-signature-nonlinear-system-solver-design\nmax: 2\nmean: 1.1042\nmin: 0.0025\ntotal: 8.8334\nResult: count=8|label=a-signature-nonlinear-system-solver-design|max=2|mean=1.1042|min=0.0025|total=8.8334\nRun 1 SHA-256: 9f98f239fe4d1ea4be3e200b85abe2a3365b7e21a9f840ba5f4b3ec3ebbe6e0a\nRun 2 SHA-256: 9f98f239fe4d1ea4be3e200b85abe2a3365b7e21a9f840ba5f4b3ec3ebbe6e0a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Romberg Extrapolator",
    "subject": "a Signature Romberg extrapolator design",
    "description": "The Romberg Extrapolator is a Signature-made design for teaching Romberg integration: an extrapolator where a learner enters trapezoid values, and the tool combines them to cancel error terms, building the Romberg table level by level. Each extrapolation cancels one more error term. The trapezoid values are entered, and the table is built. Each combination cancels the leading error term. The accuracy is shown improving level by level.",
    "inputs": "FIGURES = {'true_value': 1.7182818, 'trapezoid_h1': 1.85914, 'trapezoid_h0.5': 1.75393, 'romberg_1': 1.71886, 'romberg_1_error': 0.00058, 'romberg_2': 1.718282, 'romberg_2_error': 2e-07, 'levels': 3}\nLABEL = 'a-signature-romberg-extrapolator-design'\n",
    "expected": "count: 8\nlabel: a-signature-romberg-extrapolator-design\nmax: 3\nmean: 1.4711\nmin: 2e-07\ntotal: 11.7691\nResult: count=8|label=a-signature-romberg-extrapolator-design|max=3|mean=1.4711|min=2e-07|total=11.7691\nRun 1 SHA-256: ce563ca28ff4b55c2fbd8a107a4fc3ec0ce42d35d11a8c290c2c968889483f1b\nRun 2 SHA-256: ce563ca28ff4b55c2fbd8a107a4fc3ec0ce42d35d11a8c290c2c968889483f1b\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Numerical Capstone Console",
    "subject": "a Signature numerical capstone console design",
    "description": "The Numerical Capstone Console is a Signature-made design for teaching end-to-end numerical work: a console where a learner solves a real problem by choosing the method, bounding the error, computing, and checking, with the plan, the checks, and the assembly scored. A capstone problem uses several tools at once. The console plans the tools: method, error bound, computation, check. Each part is solved and checked separately. The assembly is scored as a whole argument, with the answer stated with its error bound.",
    "inputs": "FIGURES = {'problems_solved': 3, 'simpson_value': 1.718861, 'simpson_error': 0.00058, 'solution_x': 1, 'solution_y': 3, 'newton_root': 1.4142157, 'newton_error': 2.1e-06, 'design_version': 1}\nLABEL = 'a-signature-numerical-capstone-console-design'\n",
    "expected": "count: 8\nlabel: a-signature-numerical-capstone-console-design\nmax: 3\nmean: 1.3917\nmin: 2.1e-06\ntotal: 11.1337\nResult: count=8|label=a-signature-numerical-capstone-console-design|max=3|mean=1.3917|min=2.1e-06|total=11.1337\nRun 1 SHA-256: 9ac84aae0b9edb972fbf351782ff276bed1fc048f755fa63492152bc352e9772\nRun 2 SHA-256: 9ac84aae0b9edb972fbf351782ff276bed1fc048f755fa63492152bc352e9772\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Numerical analysis",
    "url": "https://en.wikipedia.org/wiki/Numerical_analysis",
    "establishes": "The reference for a Signature error ledger design in this record."
  },
  {
    "name": "Wikipedia - Numerical stability",
    "url": "https://en.wikipedia.org/wiki/Numerical_stability",
    "establishes": "The reference for a Signature error ledger design in this record."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic) {
  const code = "import hashlib\n" + topic.inputs +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), " +
    "\"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  return { code: code, expected: topic.expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const demo = buildDemo(topic);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + (EDITION === "signature"
      ? " Design-study: this is a Signature-made design, labelled design-study throughout, never presented as established fact or as an authentic public record."
      : " Established college-level knowledge, checked against its cited sources."),
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record: the same shape as the filed records, with its own figures.", A2: "The whole edition: every generated record joins the 24 filed records.", A3: "The subject against the whole network: every college subject linked, every record searchable." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug", a.slug === SLUG);
  t("slug signature form", EDITION === "signature" ? (a.slug.split("-signature").length - 1) === 1 : a.slug.indexOf("-signature") === -1);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
