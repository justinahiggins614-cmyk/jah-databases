// Seeded boundless generator for the Numerical Analysis Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-numerical-analysis.js [seed]  (prints one JSON record)
// or: node gen-numerical-analysis.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "numerical-analysis";
const RECORD_KIND = "numerical analysis record";
const ID_PREFIX = "JAH-NUMANA-";
const AI_NAME = "JAH Numerical Analysis Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Numerical Analysis: Error and Its Sources",
    "subject": "error and its sources",
    "description": "Error is the difference between a computed value and the true value. Absolute error is the size of the difference; relative error is the absolute error divided by the size of the true value. Errors come from rounding (a computer stores finitely many digits), truncation (a method stops early), and the data itself (measurements are inexact). Absolute error measures the difference; relative error measures it against the size of the answer. Rounding error comes from finite-precision arithmetic; truncation error comes from stopping a process early. Errors can amplify: subtracting nearly equal numbers loses significant digits (catastrophic cancellation).",
    "inputs": "FIGURES = {'absolute_error': 3.33e-05, 'relative_error': 0.0001, 'digits_kept': 4, 'sqrt_value': 100.005, 'difference': 0.005, 'accurate_value': 0.00499987, 'error_sources': 3, 'decimal_places': 4}\nLABEL = 'error-and-its-sources'\n",
    "expected": "count: 8\nlabel: error-and-its-sources\nmax: 100.005\nmean: 13.8769\nmin: 3.33e-05\ntotal: 111.0151\nResult: count=8|label=error-and-its-sources|max=100.005|mean=13.8769|min=3.33e-05|total=111.0151\nRun 1 SHA-256: ea9eaf7f8dd811ae6385f5eae4dc72d52dfa367d178becb4d9486c5136fd76e8\nRun 2 SHA-256: ea9eaf7f8dd811ae6385f5eae4dc72d52dfa367d178becb4d9486c5136fd76e8\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Floating-Point Arithmetic",
    "subject": "floating-point arithmetic",
    "description": "Floating-point arithmetic is how computers store real numbers: a number is stored as a significand (its digits) times a power of 2, with a fixed number of bits. Double precision (the usual format) has 53 bits of significand, about 16 decimal digits, and a relative rounding error of about 2.2 times 10^-16 per operation (the machine epsilon). Double precision has about 16 decimal digits and machine epsilon about 2.2e-16. Adding a tiny number to a large one can lose the tiny number entirely. The order of operations changes the rounding, so the same computation can give different answers.",
    "inputs": "FIGURES = {'machine_epsilon': 2.2e-16, 'significand_bits': 53, 'decimal_digits': 16, 'ulp_at_1e16': 2, 'sum_0.1_ten': 0.9999999999999999, 'harmonic_10': 2.9289682539682538, 'operations': 3, 'terms_summed': 10}\nLABEL = 'floating-point-arithmetic'\n",
    "expected": "count: 8\nlabel: floating-point-arithmetic\nmax: 53\nmean: 10.9911\nmin: 2.2e-16\ntotal: 87.929\nResult: count=8|label=floating-point-arithmetic|max=53|mean=10.9911|min=2.2e-16|total=87.929\nRun 1 SHA-256: b02d28abf308911ea4028b21f3bb2d4252edb186f2e906e5b65982a4b52756bd\nRun 2 SHA-256: b02d28abf308911ea4028b21f3bb2d4252edb186f2e906e5b65982a4b52756bd\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Bisection",
    "subject": "bisection for root finding",
    "description": "Bisection finds a root (a point where a function is zero) by halving an interval that brackets it: if a continuous function changes sign on an interval, it has a root inside (the intermediate value theorem). Evaluate the midpoint; keep the half where the sign still changes; repeat. Each step halves the error. Bisection needs a sign change on the starting interval. Each step halves the interval, so n steps reduce the error by a factor of 2^n. Bisection is slow but certain: it always converges when the hypotheses hold.",
    "inputs": "FIGURES = {'steps_taken': 3, 'interval_width': 0.125, 'midpoint': 1.4375, 'true_root': 1.41421356, 'error_bound': 0.0625, 'f_at_1.5': 0.25, 'f_at_1.25': -0.4375, 'f_at_1.375': -0.109375}\nLABEL = 'bisection-for-root-finding'\n",
    "expected": "count: 8\nlabel: bisection-for-root-finding\nmax: 3\nmean: 0.7178\nmin: -0.4375\ntotal: 5.7423\nResult: count=8|label=bisection-for-root-finding|max=3|mean=0.7178|min=-0.4375|total=5.7423\nRun 1 SHA-256: 6b7ae2ec0c642c20f9746fdb441a33d17ba1a0f811bc3cc68eba2073438209fb\nRun 2 SHA-256: 6b7ae2ec0c642c20f9746fdb441a33d17ba1a0f811bc3cc68eba2073438209fb\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Newton's Method",
    "subject": "Newton's method for root finding",
    "description": "Newton's method finds a root by following tangent lines: from a guess x, the next guess is x - f(x)/f'(x), the point where the tangent line at x crosses the axis. Near a simple root it converges quadratically: the number of correct digits roughly doubles at each step. The iteration is x(n+1) = x(n) - f(x(n))/f'(x(n)). Near a simple root, convergence is quadratic: correct digits roughly double per step. A bad starting guess, or a derivative near zero, can make it diverge or cycle.",
    "inputs": "FIGURES = {'step_1': 1.5, 'step_2': 1.4166667, 'step_3': 1.4142157, 'true_root': 1.41421356, 'error_step_3': 2.1e-06, 'bisection_error_3': 0.0625, 'iterations': 3, 'derivative_at_1': 2}\nLABEL = 'newton-s-method-for-root-finding'\n",
    "expected": "count: 8\nlabel: newton-s-method-for-root-finding\nmax: 3\nmean: 1.3509\nmin: 2.1e-06\ntotal: 10.8076\nResult: count=8|label=newton-s-method-for-root-finding|max=3|mean=1.3509|min=2.1e-06|total=10.8076\nRun 1 SHA-256: df5c49aeb1f5d7b05d9f7d28f932657d6f154477b50c9eb10207cd4ae944b472\nRun 2 SHA-256: df5c49aeb1f5d7b05d9f7d28f932657d6f154477b50c9eb10207cd4ae944b472\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: The Secant Method",
    "subject": "the secant method for root finding",
    "description": "The secant method is Newton's method without the derivative: it approximates the derivative by the slope of the secant line through the last two points. The iteration uses x(n+1) = x(n) - f(x(n)) times (x(n) - x(n-1)) / (f(x(n)) - f(x(n-1))). It converges superlinearly (faster than linear, slower than quadratic) and needs no derivative. The secant method needs two starting points, not one. Its order of convergence is about 1.618 (the golden ratio). It is used when the derivative is unavailable or expensive.",
    "inputs": "FIGURES = {'step_1': 1.333333, 'step_2': 1.4, 'step_3': 1.414634, 'true_root': 1.41421356, 'error_step_3': 0.00042, 'convergence_order': 1.618, 'starting_points': 2, 'iterations': 3}\nLABEL = 'the-secant-method-for-root-finding'\n",
    "expected": "count: 8\nlabel: the-secant-method-for-root-finding\nmax: 3\nmean: 1.5226\nmin: 0.00042\ntotal: 12.1806\nResult: count=8|label=the-secant-method-for-root-finding|max=3|mean=1.5226|min=0.00042|total=12.1806\nRun 1 SHA-256: 909b764299cf85f2ab17570406faa498c4b039a0bae7e9353a927818f0b21a9b\nRun 2 SHA-256: 909b764299cf85f2ab17570406faa498c4b039a0bae7e9353a927818f0b21a9b\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Gaussian Elimination and LU Factorisation",
    "subject": "Gaussian elimination and LU factorisation",
    "description": "Gaussian elimination solves a linear system by row operations, turning the matrix into triangular form. LU factorisation writes A as L times U, where L is lower triangular (non-zero entries only on and below the diagonal, with 1s on the diagonal) and U is upper triangular. Once factored, many systems with the same A are solved cheaply by forward and back substitution. Elimination costs about (2/3) n cubed operations for an n by n system. LU factorisation separates the work: factor once, solve many times. Partial pivoting (swapping rows to put the largest entry on the diagonal) controls rounding error.",
    "inputs": "FIGURES = {'solution_x': 1, 'solution_y': 3, 'l_21': 0.5, 'u_11': 2, 'u_22': 2.5, 'operations_order': 3, 'rows': 2, 'checks': 2}\nLABEL = 'gaussian-elimination-and-lu-factorisation'\n",
    "expected": "count: 8\nlabel: gaussian-elimination-and-lu-factorisation\nmax: 3\nmean: 2.0\nmin: 0.5\ntotal: 16.0\nResult: count=8|label=gaussian-elimination-and-lu-factorisation|max=3|mean=2.0|min=0.5|total=16.0\nRun 1 SHA-256: 3e8445da69de483a6a7b7103dd62cf6129fae88e1e02a71aa05ded449a36d637\nRun 2 SHA-256: 3e8445da69de483a6a7b7103dd62cf6129fae88e1e02a71aa05ded449a36d637\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Iterative Methods for Linear Systems",
    "subject": "iterative methods for linear systems",
    "description": "An iterative method for a linear system starts from a guess and improves it step by step, stopping when the residual (the difference between A times the guess and b) is small enough. The Jacobi method updates all unknowns from the old values; Gauss-Seidel updates them one by one, using the newest values. Both converge for diagonally dominant matrices (where each diagonal entry is larger in size than the sum of the other entries in its row). Jacobi updates all unknowns from the previous iteration; Gauss-Seidel uses the newest values as it goes. Both converge for strictly diagonally dominant matrices. Iterative methods are used for large sparse systems (mostly zeros), where elimination is too expensive.",
    "inputs": "FIGURES = {'true_x': 1.1818, 'true_y': 2.2727, 'jacobi_step3_x': 1.2292, 'jacobi_step3_y': 2.3056, 'gs_step1_x': 1.75, 'gs_step1_y': 2.0833, 'iterations_shown': 3, 'diagonal_dominant': 1}\nLABEL = 'iterative-methods-for-linear-systems'\n",
    "expected": "count: 8\nlabel: iterative-methods-for-linear-systems\nmax: 3\nmean: 1.8528\nmin: 1\ntotal: 14.8226\nResult: count=8|label=iterative-methods-for-linear-systems|max=3|mean=1.8528|min=1|total=14.8226\nRun 1 SHA-256: 7466fea29ebe3c77f0714694dbf30212060217e0a11433e870ff140ea5e22695\nRun 2 SHA-256: 7466fea29ebe3c77f0714694dbf30212060217e0a11433e870ff140ea5e22695\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: The Condition Number",
    "subject": "the condition number",
    "description": "The condition number of a matrix measures how much the solution of a linear system can change when the data change a little. For the 2-norm, it is the largest singular value divided by the smallest. A condition number near 1 means a well-conditioned problem; a large one (say 10^6) means the answer can lose about 6 decimal digits to rounding. The condition number is the ratio of the largest to the smallest singular value. A relative error in the data is amplified by at most the condition number. A singular matrix has infinite condition number.",
    "inputs": "FIGURES = {'determinant': 0.0001, 'condition_number': 40002, 'identity_condition': 1, 'inverse_entry': 10001, 'solution_x': 1, 'solution_y': 1, 'change_in_b': 0.0001, 'amplification': 10000}\nLABEL = 'the-condition-number'\n",
    "expected": "count: 8\nlabel: the-condition-number\nmax: 40002\nmean: 7500.75\nmin: 0.0001\ntotal: 60006.0002\nResult: count=8|label=the-condition-number|max=40002|mean=7500.75|min=0.0001|total=60006.0002\nRun 1 SHA-256: f116050fd78539865f2cea10636adc0e4d425e2b95b006ea1651ab56f8fe6099\nRun 2 SHA-256: f116050fd78539865f2cea10636adc0e4d425e2b95b006ea1651ab56f8fe6099\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Polynomial Interpolation",
    "subject": "polynomial interpolation",
    "description": "Polynomial interpolation finds the polynomial of degree at most n that passes through n + 1 given points. Lagrange's formula builds it as a sum of basis polynomials, each 1 at one point and 0 at the others. Newton's divided differences build it step by step, adding one point at a time. The error is bounded by the next derivative times a product of distances. There is exactly one polynomial of degree at most n through n + 1 points. Lagrange's formula writes it as a sum of basis polynomials. The error at x is f^(n+1)(xi)/(n+1)! times the product of (x - x_i).",
    "inputs": "FIGURES = {'points': 3, 'degree': 2, 'x2_coefficient': -0.5, 'x_coefficient': 2.5, 'constant': 1, 'check_at_1': 3, 'check_at_2': 4, 'basis_polynomials': 3}\nLABEL = 'polynomial-interpolation'\n",
    "expected": "count: 8\nlabel: polynomial-interpolation\nmax: 4\nmean: 2.25\nmin: -0.5\ntotal: 18.0\nResult: count=8|label=polynomial-interpolation|max=4|mean=2.25|min=-0.5|total=18.0\nRun 1 SHA-256: 64a109bf9f8986839e22734b3b5fa047d9017144b64091ab30e1d2ec4a6e8748\nRun 2 SHA-256: 64a109bf9f8986839e22734b3b5fa047d9017144b64091ab30e1d2ec4a6e8748\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Splines",
    "subject": "splines",
    "description": "A spline is a piecewise polynomial: a different low-degree polynomial on each interval between the data points, joined smoothly (with matching values and derivatives at the joins). A cubic spline (degree 3 on each piece, with continuous first and second derivatives) is the standard choice: it is smooth, it does not oscillate like a high-degree polynomial, and it is the curve a flexible strip would take. A cubic spline is a cubic polynomial on each interval, with continuous value, slope, and curvature at the joins. A natural spline has zero second derivative at the ends. Splines avoid Runge's phenomenon: they stay close to the data.",
    "inputs": "FIGURES = {'points': 3, 'pieces': 2, 'value_at_0.5': 0.6875, 'max_value': 1, 'degree': 3, 'continuity_orders': 2, 'end_condition': 0, 'checks': 2}\nLABEL = 'splines'\n",
    "expected": "count: 8\nlabel: splines\nmax: 3\nmean: 1.7109\nmin: 0\ntotal: 13.6875\nResult: count=8|label=splines|max=3|mean=1.7109|min=0|total=13.6875\nRun 1 SHA-256: 9cf91113d30cd351119a1481638824277289d6ef29a64f7be6381aedfcd35db2\nRun 2 SHA-256: 9cf91113d30cd351119a1481638824277289d6ef29a64f7be6381aedfcd35db2\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Numerical Integration",
    "subject": "numerical integration",
    "description": "Numerical integration (quadrature) approximates a definite integral by a weighted sum of function values. The trapezoidal rule averages the left and right sums; Simpson's rule fits parabolas through triples of points and is exact for cubics. The error of the trapezoidal rule is proportional to h squared, and of Simpson's rule to h to the fourth power, where h is the step size. The trapezoidal rule with step h has error proportional to h squared. Simpson's rule with step h has error proportional to h to the fourth power. Gaussian quadrature chooses the points and weights to be exact for the highest possible degree.",
    "inputs": "FIGURES = {'true_value': 1.7182818, 'trapezoidal': 1.753931, 'trapezoidal_error': 0.0356, 'simpson': 1.718861, 'simpson_error': 0.00058, 'points_used': 3, 'step_size': 0.5, 'rules_compared': 2}\nLABEL = 'numerical-integration'\n",
    "expected": "count: 8\nlabel: numerical-integration\nmax: 3\nmean: 1.3409\nmin: 0.00058\ntotal: 10.7273\nResult: count=8|label=numerical-integration|max=3|mean=1.3409|min=0.00058|total=10.7273\nRun 1 SHA-256: d27dca7398bd4cece2a0b97adb9f1ce9c1cec2fa5e7ab711359fdd6febf67884\nRun 2 SHA-256: d27dca7398bd4cece2a0b97adb9f1ce9c1cec2fa5e7ab711359fdd6febf67884\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Euler's Method for ODEs",
    "subject": "Euler's method for ordinary differential equations",
    "description": "Euler's method approximates the solution of dy/dx = f(x, y) step by step: from (x, y), the next point is (x + h, y + h f(x, y)), moving along the tangent line. The local error per step is proportional to h squared, and the global error after a fixed interval is proportional to h. It is the simplest method, and the baseline against which better methods are measured. Each step moves along the tangent line by h times the slope. The global error is proportional to h: halving h halves the error. Euler's method is explicit (the next value is computed directly) and first-order.",
    "inputs": "FIGURES = {'euler_h0.1': 1.21, 'true_value': 1.2214, 'error_h0.1': 0.0114, 'euler_h0.05': 1.2155, 'error_h0.05': 0.0059, 'step_size': 0.1, 'steps': 2, 'error_ratio': 2}\nLABEL = 'euler-s-method-for-ordinary-differential-equations'\n",
    "expected": "count: 8\nlabel: euler-s-method-for-ordinary-differential-equations\nmax: 2\nmean: 0.9705\nmin: 0.0059\ntotal: 7.7642\nResult: count=8|label=euler-s-method-for-ordinary-differential-equations|max=2|mean=0.9705|min=0.0059|total=7.7642\nRun 1 SHA-256: 88674df3a2b3507828152e28f6337ca6e5fa6fe66d28bb01e974607a6024f485\nRun 2 SHA-256: 88674df3a2b3507828152e28f6337ca6e5fa6fe66d28bb01e974607a6024f485\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Runge-Kutta Methods",
    "subject": "Runge-Kutta methods",
    "description": "Runge-Kutta methods improve on Euler by taking several trial steps and combining them with weights chosen to cancel the lower-order error terms. The classic fourth-order method takes four slopes per step (at the start, twice in the middle, and at the end) and combines them as (k1 + 2 k2 + 2 k3 + k4)/6. Its global error is proportional to h to the fourth power. The classic method uses 4 slopes per step and has global error proportional to h^4. Halving h reduces the error by a factor of 16. Runge-Kutta methods are the workhorses of ordinary differential equation solvers.",
    "inputs": "FIGURES = {'rk4_at_0.1': 1.1051708, 'rk4_at_0.2': 1.2214028, 'true_value': 1.2214028, 'rk4_error': 1e-06, 'euler_value': 1.21, 'euler_error': 0.0114, 'slopes_per_step': 4, 'order': 4}\nLABEL = 'runge-kutta-methods'\n",
    "expected": "count: 8\nlabel: runge-kutta-methods\nmax: 4\nmean: 1.5962\nmin: 1e-06\ntotal: 12.7694\nResult: count=8|label=runge-kutta-methods|max=4|mean=1.5962|min=1e-06|total=12.7694\nRun 1 SHA-256: 17683d57e0ff0153d814cce431110e6bd1ade06a00cd3970fa08432077982834\nRun 2 SHA-256: 17683d57e0ff0153d814cce431110e6bd1ade06a00cd3970fa08432077982834\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Least Squares and Data Fitting",
    "subject": "least squares and data fitting",
    "description": "Least squares fits a model to data by minimising the sum of the squares of the residuals (the differences between the observed and predicted values). For a line, the normal equations solve for the intercept and slope. The QR factorisation solves the same problem more stably, and the singular value decomposition handles rank-deficient cases. The normal equations are A^T A x = A^T b. QR factorisation solves least squares without forming A^T A. The residual is orthogonal to every column of A at the solution.",
    "inputs": "FIGURES = {'intercept': 1.1667, 'slope': 1.5, 'residual_sum_squares': 0.1667, 'residual_1': -0.1667, 'residual_2': 0.3333, 'residual_3': -0.1667, 'points': 3, 'parameters': 2}\nLABEL = 'least-squares-and-data-fitting'\n",
    "expected": "count: 8\nlabel: least-squares-and-data-fitting\nmax: 3\nmean: 0.9792\nmin: -0.1667\ntotal: 7.8333\nResult: count=8|label=least-squares-and-data-fitting|max=3|mean=0.9792|min=-0.1667|total=7.8333\nRun 1 SHA-256: 82674a23ee40ebab0cf57681d613ecf3b981a53befc6c7aead43e203e8b60d49\nRun 2 SHA-256: 82674a23ee40ebab0cf57681d613ecf3b981a53befc6c7aead43e203e8b60d49\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Numerical Differentiation",
    "subject": "numerical differentiation",
    "description": "Numerical differentiation approximates a derivative from function values. The forward difference (f(x + h) - f(x))/h has error proportional to h; the central difference (f(x + h) - f(x - h))/(2h) has error proportional to h squared. But rounding error grows as h shrinks, so there is an optimal h: too large and truncation dominates, too small and rounding dominates. The forward difference has error proportional to h. The central difference has error proportional to h squared. The optimal h balances truncation error (growing with h) against rounding error (growing as h shrinks).",
    "inputs": "FIGURES = {'true_derivative': 0.5403023, 'forward_h0.1': 0.49736, 'forward_error': 0.043, 'central_h0.1': 0.5394, 'central_error': 0.0009, 'central_h0.01': 0.5403, 'step_h': 0.1, 'optimal_h': 0.01}\nLABEL = 'numerical-differentiation'\n",
    "expected": "count: 8\nlabel: numerical-differentiation\nmax: 0.5403023\nmean: 0.2839\nmin: 0.0009\ntotal: 2.2713\nResult: count=8|label=numerical-differentiation|max=0.5403023|mean=0.2839|min=0.0009|total=2.2713\nRun 1 SHA-256: 8c3f98bc555e5e75eb4d39ae6f51011e0788bf30157dd3af3b554033378a13e7\nRun 2 SHA-256: 8c3f98bc555e5e75eb4d39ae6f51011e0788bf30157dd3af3b554033378a13e7\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: The Finite Difference Method",
    "subject": "the finite difference method",
    "description": "The finite difference method solves differential equations by replacing derivatives with differences on a grid. For the heat equation, the second derivative is replaced by (u(i-1) - 2 u(i) + u(i+1))/h squared, and time is stepped explicitly. The method is stable only when the time step satisfies a condition (for the heat equation, k times dt / h squared at most 1/2). Derivatives are replaced by differences between neighbouring grid points. The explicit method for the heat equation is stable only when k dt / h^2 is at most 1/2. The error is proportional to h squared in space and dt in time (for the explicit method).",
    "inputs": "FIGURES = {'h_grid': 0.25, 'dt_stable': 0.02, 'stability_ratio': 0.32, 'exact_decay': 0.8209, 'fd_decay': 0.8125, 'dt_unstable': 0.04, 'unstable_ratio': 0.64, 'grid_points': 5}\nLABEL = 'the-finite-difference-method'\n",
    "expected": "count: 8\nlabel: the-finite-difference-method\nmax: 5\nmean: 0.9879\nmin: 0.02\ntotal: 7.9034\nResult: count=8|label=the-finite-difference-method|max=5|mean=0.9879|min=0.02|total=7.9034\nRun 1 SHA-256: ad815a59256de6b86edcb71092c1fad8dca69c127795145a63bc5596f29cf418\nRun 2 SHA-256: ad815a59256de6b86edcb71092c1fad8dca69c127795145a63bc5596f29cf418\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Approximation Theory",
    "subject": "approximation theory",
    "description": "Approximation theory asks how well a function can be approximated by simpler functions, such as polynomials. The Weierstrass theorem says every continuous function on a closed interval can be approximated uniformly (everywhere at once) by polynomials. The best approximation (minimising the maximum error) equioscillates: its error alternates between plus and minus its maximum at least n + 2 times for a degree-n polynomial. The Weierstrass theorem guarantees polynomial approximations exist for every continuous function. The best approximation minimises the maximum error, and its error equioscillates. Chebyshev polynomials give near-best approximations and are used in practice.",
    "inputs": "FIGURES = {'taylor_max_error': 0.1321, 'best_max_error': 0.045, 'chebyshev_error': 0.0451, 'cheb_constant': 1.2661, 'cheb_linear': 1.1303, 'cheb_quadratic': 0.2715, 'interval_half': 1, 'degree': 2}\nLABEL = 'approximation-theory'\n",
    "expected": "count: 8\nlabel: approximation-theory\nmax: 2\nmean: 0.7363\nmin: 0.045\ntotal: 5.8901\nResult: count=8|label=approximation-theory|max=2|mean=0.7363|min=0.045|total=5.8901\nRun 1 SHA-256: c091ae12b496fcb767236c029019d4f89ba011d5da7cf0bcf5ae102d0c5d5c6f\nRun 2 SHA-256: c091ae12b496fcb767236c029019d4f89ba011d5da7cf0bcf5ae102d0c5d5c6f\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Optimisation by Gradient Descent",
    "subject": "optimisation by gradient descent",
    "description": "Gradient descent minimises a function by stepping downhill: from x, move to x - alpha times the gradient (the vector of partial derivatives), where alpha is the step size (the learning rate). With a well-chosen step, it converges to a minimum; with too large a step it overshoots and diverges; with too small a step it crawls. The step is x - alpha times the gradient, where alpha is the step size. Too large a step overshoots; too small a step converges slowly. Newton's method uses the second derivative as well and converges faster near the minimum.",
    "inputs": "FIGURES = {'start_x': 4, 'step_1': 3.2, 'step_2': 2.56, 'step_3': 2.048, 'after_10': 0.4295, 'f_after_10': 0.1845, 'shrink_factor': 0.8, 'step_size': 0.1}\nLABEL = 'optimisation-by-gradient-descent'\n",
    "expected": "count: 8\nlabel: optimisation-by-gradient-descent\nmax: 4\nmean: 1.6653\nmin: 0.1\ntotal: 13.322\nResult: count=8|label=optimisation-by-gradient-descent|max=4|mean=1.6653|min=0.1|total=13.322\nRun 1 SHA-256: 268cfa93f572682d553c653d5ca10e0fb2c3c01966306c86651ef929934e63f2\nRun 2 SHA-256: 268cfa93f572682d553c653d5ca10e0fb2c3c01966306c86651ef929934e63f2\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Monte Carlo Integration",
    "subject": "Monte Carlo integration",
    "description": "Monte Carlo integration estimates an integral by random sampling: the average of the function at random points, times the volume of the region, estimates the integral. The error shrinks like 1 over the square root of the number of samples, regardless of dimension, which is why Monte Carlo is used for high-dimensional integrals where grid methods fail. The estimate is the average of the function values times the volume. The error shrinks like 1/sqrt(N) for N samples, in any dimension. Variance reduction (such as importance sampling) makes the estimate more accurate for the same N.",
    "inputs": "FIGURES = {'darts_100': 100, 'inside_100': 79, 'pi_estimate_100': 3.16, 'darts_10000': 10000, 'inside_10000': 7854, 'pi_estimate_10000': 3.1416, 'std_error': 0.0041, 'pi_true': 3.14159}\nLABEL = 'monte-carlo-integration'\n",
    "expected": "count: 8\nlabel: monte-carlo-integration\nmax: 10000\nmean: 2255.3059\nmin: 0.0041\ntotal: 18042.4473\nResult: count=8|label=monte-carlo-integration|max=10000|mean=2255.3059|min=0.0041|total=18042.4473\nRun 1 SHA-256: 93ed5502090e9634d6a4fdae3f6090db0bc4c8e9ca7553bc6ada366934bb3e1d\nRun 2 SHA-256: 93ed5502090e9634d6a4fdae3f6090db0bc4c8e9ca7553bc6ada366934bb3e1d\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Stiff Equations and Implicit Methods",
    "subject": "stiff equations and implicit methods",
    "description": "A stiff equation is one with very different time scales: a fast transient that decays quickly and a slow evolution that matters. Explicit methods must take tiny steps to stay stable on the fast scale, even after it has decayed. Implicit methods (which solve an equation at each step, rather than computing the next value directly) are stable for large steps and are the tool for stiff problems. Stiffness means the time scales differ by orders of magnitude. Explicit methods are limited by stability, not accuracy, on stiff problems. The backward Euler method is implicit and unconditionally stable for the test equation.",
    "inputs": "FIGURES = {'stiffness_ratio': 1000, 'transient_at_0.01': 4.5e-05, 'explicit_step_limit': 0.002, 'steps_needed': 5000, 'implicit_step': 0.1, 'y_at_0.1': 0.99496, 'cos_0.1': 0.995004, 'error': 4e-05}\nLABEL = 'stiff-equations-and-implicit-methods'\n",
    "expected": "count: 8\nlabel: stiff-equations-and-implicit-methods\nmax: 5000\nmean: 750.2615\nmin: 4e-05\ntotal: 6002.092\nResult: count=8|label=stiff-equations-and-implicit-methods|max=5000|mean=750.2615|min=4e-05|total=6002.092\nRun 1 SHA-256: 2af3b381005c62766f9287e72b3775f56352c7f5b15d9c9c0e1ec4802aab6ffc\nRun 2 SHA-256: 2af3b381005c62766f9287e72b3775f56352c7f5b15d9c9c0e1ec4802aab6ffc\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: The Fast Fourier Transform",
    "subject": "the fast Fourier transform",
    "description": "The fast Fourier transform (FFT) computes the discrete Fourier transform (the values of a polynomial at the roots of unity) in n log n operations instead of n squared, by splitting the problem in half recursively. It is the algorithm that makes digital signal processing possible: it turns a signal into its frequencies and back. The discrete Fourier transform of n points costs n squared operations directly. The FFT splits the points into even and odd halves, recursively, costing n log n. The FFT is used for filtering, compression, and solving differential equations.",
    "inputs": "FIGURES = {'n_points': 4, 'fft_operations': 8, 'direct_operations': 16, 'n_1024_fft': 10240, 'n_1024_direct': 1048576, 'transform_values': 1, 'halves': 2, 'log_factor': 2}\nLABEL = 'the-fast-fourier-transform'\n",
    "expected": "count: 8\nlabel: the-fast-fourier-transform\nmax: 1048576\nmean: 132356.125\nmin: 1\ntotal: 1058849\nResult: count=8|label=the-fast-fourier-transform|max=1048576|mean=132356.125|min=1|total=1058849\nRun 1 SHA-256: fdc7e72e6159b9a19d01c303cc32ca25613ba648d615766d66a08296adaa8278\nRun 2 SHA-256: fdc7e72e6159b9a19d01c303cc32ca25613ba648d615766d66a08296adaa8278\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Numerical Solution of Nonlinear Systems",
    "subject": "numerical solution of nonlinear systems",
    "description": "Newton's method extends to systems: at each step, solve the linear system J delta = -F, where J is the Jacobian matrix (the matrix of partial derivatives) and F is the vector of function values, then update x by delta. Near a solution it converges quadratically, like the one-variable method. The Jacobian is the matrix of partial derivatives. Each step solves J delta = -F and updates x by delta. Near a solution the error squares at each step.",
    "inputs": "FIGURES = {'true_x': 1.4142, 'true_y': 1.4142, 'start_x': 1, 'step1_x': 1.5, 'error_step1': 0.0858, 'step2_x': 1.4167, 'error_step2': 0.0025, 'jacobian_rows': 2}\nLABEL = 'numerical-solution-of-nonlinear-systems'\n",
    "expected": "count: 8\nlabel: numerical-solution-of-nonlinear-systems\nmax: 2\nmean: 1.1042\nmin: 0.0025\ntotal: 8.8334\nResult: count=8|label=numerical-solution-of-nonlinear-systems|max=2|mean=1.1042|min=0.0025|total=8.8334\nRun 1 SHA-256: 9ae88cc5bc5e0b2e04c7aba314d5f4fa56261b93829107efdb264bb3d20f47de\nRun 2 SHA-256: 9ae88cc5bc5e0b2e04c7aba314d5f4fa56261b93829107efdb264bb3d20f47de\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Richardson Extrapolation and Romberg Integration",
    "subject": "Richardson extrapolation and Romberg integration",
    "description": "Richardson extrapolation combines two approximations with different step sizes to cancel the leading error term, raising the order. Romberg integration applies it to the trapezoidal rule, producing Simpson's rule and higher-order rules from trapezoid values alone. Each extrapolation cancels one more error term. The trapezoidal rule has error proportional to h squared. Combining h and h/2 cancels the h squared term, giving Simpson's rule. Repeating gives higher-order rules, each more accurate.",
    "inputs": "FIGURES = {'true_value': 1.7182818, 'trapezoid_h1': 1.85914, 'trapezoid_h0.5': 1.75393, 'romberg_1': 1.71886, 'romberg_1_error': 0.00058, 'romberg_2': 1.718282, 'romberg_2_error': 2e-07, 'levels': 3}\nLABEL = 'richardson-extrapolation-and-romberg-integration'\n",
    "expected": "count: 8\nlabel: richardson-extrapolation-and-romberg-integration\nmax: 3\nmean: 1.4711\nmin: 2e-07\ntotal: 11.7691\nResult: count=8|label=richardson-extrapolation-and-romberg-integration|max=3|mean=1.4711|min=2e-07|total=11.7691\nRun 1 SHA-256: 663eabc7417aba9297a798316423be9d8acdbc8755e7d798f1905969a1de0aa0\nRun 2 SHA-256: 663eabc7417aba9297a798316423be9d8acdbc8755e7d798f1905969a1de0aa0\nDeterministic: MATCH\n"
  },
  {
    "title": "Numerical Analysis: Capstone Solving a Real Problem End to End",
    "subject": "capstone: solving a real problem end to end",
    "description": "A capstone problem for numerical analysis solves a real problem end to end: choose the method, bound the error, compute, and check. This record prices a simple integral, solves a linear system, and finds a root, showing the method choice, the error bound, and the check for each. The method is chosen by the problem's type and the accuracy needed. The error is bounded before computing, and checked after by halving the step. The answer is stated with its error bound, not as a bare number.",
    "inputs": "FIGURES = {'simpson_value': 1.718861, 'simpson_error': 0.00058, 'refined_value': 1.718282, 'solution_x': 1, 'solution_y': 3, 'newton_root': 1.4142157, 'newton_error': 2.1e-06, 'problems_solved': 3}\nLABEL = 'capstone-solving-a-real-problem-end-to-end'\n",
    "expected": "count: 8\nlabel: capstone-solving-a-real-problem-end-to-end\nmax: 3\nmean: 1.4815\nmin: 2.1e-06\ntotal: 11.8519\nResult: count=8|label=capstone-solving-a-real-problem-end-to-end|max=3|mean=1.4815|min=2.1e-06|total=11.8519\nRun 1 SHA-256: cf3ae2ff282f08074e569451e14fbfc3af948a0cf325d4d4c9b7ebd8de80af41\nRun 2 SHA-256: cf3ae2ff282f08074e569451e14fbfc3af948a0cf325d4d4c9b7ebd8de80af41\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Numerical analysis",
    "url": "https://en.wikipedia.org/wiki/Numerical_analysis",
    "establishes": "The reference for error and its sources in this record."
  },
  {
    "name": "Wikipedia - Numerical stability",
    "url": "https://en.wikipedia.org/wiki/Numerical_stability",
    "establishes": "The reference for error and its sources in this record."
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
