// Seeded boundless generator for the The Signature Differential Equations Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-differential-equations-signature.js [seed]  (prints one JSON record)
// or: node gen-differential-equations-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "differential-equations-signature";
const RECORD_KIND = "differential equation record";
const ID_PREFIX = "JAH-DIFFEQS-";
const AI_NAME = "JAH Differential Equations Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Equation Classifier",
    "subject": "a Signature equation classifier design",
    "description": "The Equation Classifier is a Signature-made design for teaching differential equations: a tool where a learner enters an equation and the tool names its order, its type (ordinary or partial, linear or non-linear), and the method that fits it. Classification is the first step of solving. The classifier reports the order, the linearity, and the type. Each classification is linked to the method that solves it. An equation that fits no method is flagged for numerical solution.",
    "inputs": "FIGURES = {'equations_classified': 3, 'orders_found': 2, 'methods_named': 3, 'types_named': 3, 'linear_count': 3, 'partial_count': 1, 'ordinary_count': 2, 'design_version': 1}\nLABEL = 'a-signature-equation-classifier-design'\n",
    "expected": "count: 8\nlabel: a-signature-equation-classifier-design\nmax: 3\nmean: 2.25\nmin: 1\ntotal: 18\nResult: count=8|label=a-signature-equation-classifier-design|max=3|mean=2.25|min=1|total=18\nRun 1 SHA-256: a2e42d64a5dd28e80feaa41ea727612f05ec768cb7f749893dbce720cc576a24\nRun 2 SHA-256: a2e42d64a5dd28e80feaa41ea727612f05ec768cb7f749893dbce720cc576a24\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Direction Field Painter",
    "subject": "a Signature direction field painter design",
    "description": "The Direction Field Painter is a Signature-made design for teaching first-order equations: a painter that draws short line segments showing the slope of the solution at each point of the plane, so the solutions can be seen as curves following the segments. A direction field shows the slope dy/dx at every point. The painter draws the slope segments on a grid. A solution curve is drawn by following the segments from a starting point. Equilibria (where the slope is zero) are marked.",
    "inputs": "FIGURES = {'slopes_shown': 3, 'solution_points': 2, 'y_at_2': 3, 'y_at_minus2': 3, 'equilibria': 1, 'grid_points': 25, 'curves_drawn': 1, 'design_version': 1}\nLABEL = 'a-signature-direction-field-painter-design'\n",
    "expected": "count: 8\nlabel: a-signature-direction-field-painter-design\nmax: 25\nmean: 4.875\nmin: 1\ntotal: 39\nResult: count=8|label=a-signature-direction-field-painter-design|max=25|mean=4.875|min=1|total=39\nRun 1 SHA-256: bbf33ae8e52baafcffda9c531d5d7656b91023022189c414e4fb49ceb80dfe4e\nRun 2 SHA-256: bbf33ae8e52baafcffda9c531d5d7656b91023022189c414e4fb49ceb80dfe4e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Separation Workbench",
    "subject": "a Signature separation workbench design",
    "description": "The Separation Workbench is a Signature-made design for teaching separable equations: a bench where a learner moves the x terms to one side and the y terms to the other, integrates both sides, and solves for y. A separable equation splits into a function of x and a function of y. The bench shows the separation step, with the x terms and y terms on opposite sides. Each side is integrated separately, with the constant shown. The initial condition is applied at the end, fixing the constant.",
    "inputs": "FIGURES = {'separations': 1, 'integrals': 2, 'y_at_1': 3.297, 'initial_value': 2, 'constant_a': 2, 'steps': 3, 'variables': 2, 'design_version': 1}\nLABEL = 'a-signature-separation-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-separation-workbench-design\nmax: 3.297\nmean: 2.0371\nmin: 1\ntotal: 16.297\nResult: count=8|label=a-signature-separation-workbench-design|max=3.297|mean=2.0371|min=1|total=16.297\nRun 1 SHA-256: 0aecb4df2880b98d13d819b62fac2561fce34b1e72d56be9ce85ca80467c997c\nRun 2 SHA-256: 0aecb4df2880b98d13d819b62fac2561fce34b1e72d56be9ce85ca80467c997c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Integrating Factor Machine",
    "subject": "a Signature integrating factor machine design",
    "description": "The Integrating Factor Machine is a Signature-made design for teaching first-order linear equations: a machine where a learner enters P(x) and Q(x), the machine computes the integrating factor mu(x) = e to the power of the integral of P, multiplies through, and integrates. The integrating factor turns the left side into a single derivative. The machine computes the integrating factor from P(x). Multiplying through shows the left side as the derivative of (mu y). Integrating and dividing by mu gives the solution.",
    "inputs": "FIGURES = {'y_at_1': 1.7293, 'steady_value': 2, 'constant_c': -2, 'steps': 3, 'factor_at_1': 7.389, 'terms': 2, 'checks': 1, 'design_version': 1}\nLABEL = 'a-signature-integrating-factor-machine-design'\n",
    "expected": "count: 8\nlabel: a-signature-integrating-factor-machine-design\nmax: 7.389\nmean: 2.0148\nmin: -2\ntotal: 16.1183\nResult: count=8|label=a-signature-integrating-factor-machine-design|max=7.389|mean=2.0148|min=-2|total=16.1183\nRun 1 SHA-256: a15d618301a5f93edd241e7815fd6248c9412bf1132d578e976642585df25ded\nRun 2 SHA-256: a15d618301a5f93edd241e7815fd6248c9412bf1132d578e976642585df25ded\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Characteristic Root Finder",
    "subject": "a Signature characteristic root finder design",
    "description": "The Characteristic Root Finder is a Signature-made design for teaching second-order linear equations: a tool where a learner enters the coefficients, the tool solves the characteristic equation, and reports the root type (distinct real, repeated, or complex) and the form of the solution. The characteristic equation is a r squared + b r + c = 0. The tool solves the characteristic equation and classifies the roots. Each root type is linked to its solution form: exponentials, x times an exponential, or oscillations. The initial conditions are applied to fix the constants.",
    "inputs": "FIGURES = {'equations_solved': 2, 'root_types': 2, 'root_1': 1, 'root_2': 2, 'c1': 2, 'c2': -1, 'omega': 2, 'design_version': 1}\nLABEL = 'a-signature-characteristic-root-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-characteristic-root-finder-design\nmax: 2\nmean: 1.375\nmin: -1\ntotal: 11\nResult: count=8|label=a-signature-characteristic-root-finder-design|max=2|mean=1.375|min=-1|total=11\nRun 1 SHA-256: 32af70836ff28b0a48b3d5e09af8eddf1e64adec9fd6c2314acc3f17272428d3\nRun 2 SHA-256: 32af70836ff28b0a48b3d5e09af8eddf1e64adec9fd6c2314acc3f17272428d3\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Spring Simulator",
    "subject": "a Signature spring simulator design",
    "description": "The Spring Simulator is a Signature-made design for teaching the harmonic oscillator: a simulation of a mass on a spring where a learner sets the stiffness, the mass, and the starting position, and watches the mass oscillate, with the period and amplitude shown. The oscillator equation is y'' + omega squared y = 0. The simulator animates the mass and draws its position against time. The period is shown as 2 pi / omega, and the amplitude as the starting displacement. Damping is offered as an option, showing the oscillation decaying.",
    "inputs": "FIGURES = {'omega': 2, 'period': 3.1416, 'amplitude': 1, 'y_at_pi_over_4': 0, 'y_at_pi_over_2': -1, 'damping_half_life': 1.386, 'tests': 2, 'design_version': 1}\nLABEL = 'a-signature-spring-simulator-design'\n",
    "expected": "count: 8\nlabel: a-signature-spring-simulator-design\nmax: 3.1416\nmean: 1.1909\nmin: -1\ntotal: 9.5276\nResult: count=8|label=a-signature-spring-simulator-design|max=3.1416|mean=1.1909|min=-1|total=9.5276\nRun 1 SHA-256: 5062936539c091006c941667bb41f415c6119c2300772063ca15fde2f7081484\nRun 2 SHA-256: 5062936539c091006c941667bb41f415c6119c2300772063ca15fde2f7081484\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Laplace Transformer",
    "subject": "a Signature Laplace transformer design",
    "description": "The Laplace Transformer is a Signature-made design for teaching Laplace transforms: a tool where a learner enters a differential equation, the tool transforms it into algebra, solves for the transformed solution, and transforms back. The Laplace transform turns differentiation into multiplication by s. The tool shows the transform of each term, including the initial values. The algebraic equation is solved for the transformed solution. The inverse transform is looked up in a table and shown.",
    "inputs": "FIGURES = {'y_at_0': 3, 'y_at_1': 0.406, 'pole': -2, 'steps': 3, 'table_entries': 20, 'transforms_shown': 3, 'checks': 1, 'design_version': 1}\nLABEL = 'a-signature-laplace-transformer-design'\n",
    "expected": "count: 8\nlabel: a-signature-laplace-transformer-design\nmax: 20\nmean: 3.6757\nmin: -2\ntotal: 29.406\nResult: count=8|label=a-signature-laplace-transformer-design|max=20|mean=3.6757|min=-2|total=29.406\nRun 1 SHA-256: f800c50c6650f6568ddedfb11488400ba9dd13b2a61b569e3598a1bfd124c7c0\nRun 2 SHA-256: f800c50c6650f6568ddedfb11488400ba9dd13b2a61b569e3598a1bfd124c7c0\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Phase Portrait Studio",
    "subject": "a Signature phase portrait studio design",
    "description": "The Phase Portrait Studio is a Signature-made design for teaching systems of equations: a studio where a learner enters a system, sees the phase portrait (the picture of trajectories in the state plane), and classifies the equilibria from the eigenvalues. A phase portrait shows how solutions move. The studio draws the direction arrows and several trajectories. Equilibria are marked and classified as node, saddle, spiral, or centre. The eigenvalues are shown with the classification they imply.",
    "inputs": "FIGURES = {'eigenvalue_1': -1, 'eigenvalue_2': -2, 'x_at_1': 0.3679, 'y_at_1': 0.1353, 'systems_shown': 2, 'classifications': 2, 'trajectories_drawn': 5, 'design_version': 1}\nLABEL = 'a-signature-phase-portrait-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-phase-portrait-studio-design\nmax: 5\nmean: 0.9379\nmin: -2\ntotal: 7.5032\nResult: count=8|label=a-signature-phase-portrait-studio-design|max=5|mean=0.9379|min=-2|total=7.5032\nRun 1 SHA-256: 949a74b0ac693e69a909f9c8ef124b7ff6f47dd090374f57f35ba2e55e9bc96a\nRun 2 SHA-256: 949a74b0ac693e69a909f9c8ef124b7ff6f47dd090374f57f35ba2e55e9bc96a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Heat Spreader",
    "subject": "a Signature heat spreader design",
    "description": "The Heat Spreader is a Signature-made design for teaching the heat equation: a simulation of a rod where a learner sets the initial temperature profile and watches it smooth out over time, with the Fourier modes decaying at their own rates. The heat equation says temperature change is proportional to curvature. The rod is drawn with its temperature profile, animated over time. Each Fourier mode is shown with its decay rate. The steady state is shown as the long-run profile.",
    "inputs": "FIGURES = {'factor_at_0.1': 0.3727, 'factor_at_0.5': 0.0072, 'length': 1, 'modes_shown': 2, 'profiles': 2, 'times_shown': 2, 'peak_initial': 1, 'design_version': 1}\nLABEL = 'a-signature-heat-spreader-design'\n",
    "expected": "count: 8\nlabel: a-signature-heat-spreader-design\nmax: 2\nmean: 1.1725\nmin: 0.0072\ntotal: 9.3799\nResult: count=8|label=a-signature-heat-spreader-design|max=2|mean=1.1725|min=0.0072|total=9.3799\nRun 1 SHA-256: 0f204759ab30a1799f86d3a7f176679daead081e2361cd58f2246067232ee0dc\nRun 2 SHA-256: 0f204759ab30a1799f86d3a7f176679daead081e2361cd58f2246067232ee0dc\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Vibrating String Tank",
    "subject": "a Signature vibrating string tank design",
    "description": "The Vibrating String Tank is a Signature-made design for teaching the wave equation: a tank where a learner plucks a string and watches the wave travel, reflect, and form standing waves. The wave equation says acceleration is proportional to curvature, and its solutions are waves travelling at speed c. The tank animates the string's shape over time. Travelling waves are shown moving left and right at speed c. Standing waves are shown as modes with fixed nodes.",
    "inputs": "FIGURES = {'wave_speed': 2, 'period': 1, 'max_displacement': 1, 't_flat': 0.25, 't_inverted': 0.5, 'modes_shown': 2, 'length': 1, 'design_version': 1}\nLABEL = 'a-signature-vibrating-string-tank-design'\n",
    "expected": "count: 8\nlabel: a-signature-vibrating-string-tank-design\nmax: 2\nmean: 1.0938\nmin: 0.25\ntotal: 8.75\nResult: count=8|label=a-signature-vibrating-string-tank-design|max=2|mean=1.0938|min=0.25|total=8.75\nRun 1 SHA-256: dabcf4993a2dcf05a9719aa02946bcc411c5007814eb25bb5d575c3b7ea02925\nRun 2 SHA-256: dabcf4993a2dcf05a9719aa02946bcc411c5007814eb25bb5d575c3b7ea02925\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Potential Mapper",
    "subject": "a Signature potential mapper design",
    "description": "The Potential Mapper is a Signature-made design for teaching Laplace's equation: a mapper where a learner sets the boundary values on a square and watches the interior fill with the harmonic solution, with no interior maximum or minimum. Laplace's equation describes steady states. The boundary values are set on the four edges. The interior is computed by averaging neighbours, iterated until it settles. The maximum principle is shown: the extremes stay on the boundary.",
    "inputs": "FIGURES = {'top_temperature': 100, 'centre_temperature': 25.3, 'agreement': 0.1, 'edges_set': 4, 'iterations': 100, 'first_coefficient': 127.32, 'plate_size': 1, 'design_version': 1}\nLABEL = 'a-signature-potential-mapper-design'\n",
    "expected": "count: 8\nlabel: a-signature-potential-mapper-design\nmax: 127.32\nmean: 44.84\nmin: 0.1\ntotal: 358.72\nResult: count=8|label=a-signature-potential-mapper-design|max=127.32|mean=44.84|min=0.1|total=358.72\nRun 1 SHA-256: 291243c8f745a4ac19966d59dced5d930b2fd68c20195b2c735076dd458ba2ba\nRun 2 SHA-256: 291243c8f745a4ac19966d59dced5d930b2fd68c20195b2c735076dd458ba2ba\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Fourier Synthesiser",
    "subject": "a Signature Fourier synthesiser design",
    "description": "The Fourier Synthesiser is a Signature-made design for teaching Fourier series: a synthesiser where a learner adds sine waves one by one and watches the sum approach a square wave, with the Gibbs overshoot visible near the jump. A Fourier series represents a periodic function as a sum of sines and cosines. Each sine term is added with its coefficient, and the partial sum is drawn. The overshoot near the jump is shown and measured at about 9 percent. The coefficients are computed by the integral formula and displayed.",
    "inputs": "FIGURES = {'sum_1_term': 1.2732, 'sum_3_terms': 1.1037, 'sum_10_terms': 1.0633, 'true_value': 1, 'overshoot_percent': 9, 'terms_added': 10, 'coefficients_shown': 5, 'design_version': 1}\nLABEL = 'a-signature-fourier-synthesiser-design'\n",
    "expected": "count: 8\nlabel: a-signature-fourier-synthesiser-design\nmax: 10\nmean: 3.68\nmin: 1\ntotal: 29.4402\nResult: count=8|label=a-signature-fourier-synthesiser-design|max=10|mean=3.68|min=1|total=29.4402\nRun 1 SHA-256: f0107f26eed10245e92ce4ed1b5c8945d0c91e0d71bf35b2dbb491d58bbc76c3\nRun 2 SHA-256: f0107f26eed10245e92ce4ed1b5c8945d0c91e0d71bf35b2dbb491d58bbc76c3\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Stepper",
    "subject": "a Signature numerical stepper design",
    "description": "The Stepper is a Signature-made design for teaching numerical methods for differential equations: a tool where a learner chooses a method (Euler or Runge-Kutta) and a step size, and watches the approximate solution step forward alongside the true solution, with the error shown at each step. Euler's method steps along the tangent line. The stepper draws the true solution and the approximation together. The step size is adjustable, and the error is shown for each choice. Runge-Kutta is offered for comparison, showing its much smaller error.",
    "inputs": "FIGURES = {'euler_h0.1': 1.21, 'true_value': 1.2214, 'error_h0.1': 0.0114, 'euler_h0.05': 1.2155, 'error_h0.05': 0.0059, 'rk4_value': 1.2214, 'methods_offered': 2, 'design_version': 1}\nLABEL = 'a-signature-numerical-stepper-design'\n",
    "expected": "count: 8\nlabel: a-signature-numerical-stepper-design\nmax: 2\nmean: 0.9857\nmin: 0.0059\ntotal: 7.8856\nResult: count=8|label=a-signature-numerical-stepper-design|max=2|mean=0.9857|min=0.0059|total=7.8856\nRun 1 SHA-256: 2b65e652b8828be92eb7bc322f5e5e886d2f06e8265503119a8ac468843f2bc4\nRun 2 SHA-256: 2b65e652b8828be92eb7bc322f5e5e886d2f06e8265503119a8ac468843f2bc4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Stability Tester",
    "subject": "a Signature stability tester design",
    "description": "The Stability Tester is a Signature-made design for teaching stability: a tool where a learner enters a system, the tool computes the eigenvalues of the linearised system, and reports stable, asymptotically stable, or unstable, with the trajectories drawn. Stability is read from the eigenvalues. The tool linearises at the equilibrium and computes the eigenvalues. Negative real parts mean stability; a positive real part means instability. Trajectories are drawn to confirm the verdict.",
    "inputs": "FIGURES = {'eigenvalue_1': -1, 'eigenvalue_2': -2, 'x_at_1': 0.3679, 'y_at_1': 0.1353, 'systems_tested': 2, 'verdicts': 2, 'saddle_eigenvalues': 2, 'design_version': 1}\nLABEL = 'a-signature-stability-tester-design'\n",
    "expected": "count: 8\nlabel: a-signature-stability-tester-design\nmax: 2\nmean: 0.5629\nmin: -2\ntotal: 4.5032\nResult: count=8|label=a-signature-stability-tester-design|max=2|mean=0.5629|min=-2|total=4.5032\nRun 1 SHA-256: 37c2604089c0daca8724daeaa7d685cbd2eb821403144d582495d71e4e89966e\nRun 2 SHA-256: 37c2604089c0daca8724daeaa7d685cbd2eb821403144d582495d71e4e89966e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Exactness Checker",
    "subject": "a Signature exactness checker design",
    "description": "The Exactness Checker is a Signature-made design for teaching exact equations: a tool where a learner enters M and N, the tool tests whether M_y equals N_x, and if exact, builds the potential function F step by step. An exact equation says dF = 0, so its solutions are the level curves F = C. The tool computes the two partial derivatives and compares them. When exact, it integrates M in x and matches N to find the y-part. A non-exact equation is flagged, with an integrating factor suggested where one is simple.",
    "inputs": "FIGURES = {'m_y': 1, 'n_x': 1, 'solution_at_1_1': 3, 'tests': 2, 'exact_count': 1, 'potential_terms': 3, 'second_m_y': 1, 'second_n_x_at_1': 2}\nLABEL = 'a-signature-exactness-checker-design'\n",
    "expected": "count: 8\nlabel: a-signature-exactness-checker-design\nmax: 3\nmean: 1.75\nmin: 1\ntotal: 14\nResult: count=8|label=a-signature-exactness-checker-design|max=3|mean=1.75|min=1|total=14\nRun 1 SHA-256: 66dd68bbefbb80be4798e52a63e444b6b6acccfdeb9d91f6f3adcba36802762c\nRun 2 SHA-256: 66dd68bbefbb80be4798e52a63e444b6b6acccfdeb9d91f6f3adcba36802762c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Forcing Response Lab",
    "subject": "a Signature forcing response laboratory design",
    "description": "The Forcing Response Lab is a Signature-made design for teaching non-homogeneous equations: a laboratory where a learner sets a forcing term, the lab finds a particular solution by undetermined coefficients or variation of parameters, and shows the total solution as the homogeneous part plus the particular part. A forced equation has a forcing term on the right. The lab classifies the forcing term and chooses the method. The particular solution is shown with its coefficients solved. The total solution is drawn with the homogeneous part fading and the particular part persisting.",
    "inputs": "FIGURES = {'a_coefficient': -6, 'forcing_amplitude': 6, 'methods_used': 2, 'forcing_terms': 2, 'particular_solutions': 2, 'homogeneous_terms': 2, 'steps': 3, 'design_version': 1}\nLABEL = 'a-signature-forcing-response-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-forcing-response-laboratory-design\nmax: 6\nmean: 1.5\nmin: -6\ntotal: 12\nResult: count=8|label=a-signature-forcing-response-laboratory-design|max=6|mean=1.5|min=-6|total=12\nRun 1 SHA-256: 301a3eddcf5c64e699bcb7f32c6ed12b315734072b50132812764ade4ddabcbb\nRun 2 SHA-256: 301a3eddcf5c64e699bcb7f32c6ed12b315734072b50132812764ade4ddabcbb\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Special Function Table",
    "subject": "a Signature special function table design",
    "description": "The Special Function Table is a Signature-made design for teaching special functions: a table where a learner looks up Bessel functions and Legendre polynomials by their series, sees their graphs, and finds their zeros. A special function is a named solution of an important equation. Each function is shown with its defining equation, its series, and its graph. Zeros are listed, since they are the eigenvalues of circular and spherical problems. Values are computed by the series and checked against the table.",
    "inputs": "FIGURES = {'j0_at_1': 0.7652, 'approx_at_1': 0.765625, 'j0_at_2': 0.2239, 'approx_at_2': 0.222222, 'first_zero': 2.4048, 'terms_used': 3, 'functions_listed': 2, 'design_version': 1}\nLABEL = 'a-signature-special-function-table-design'\n",
    "expected": "count: 8\nlabel: a-signature-special-function-table-design\nmax: 3\nmean: 1.2977\nmin: 0.222222\ntotal: 10.3817\nResult: count=8|label=a-signature-special-function-table-design|max=3|mean=1.2977|min=0.222222|total=10.3817\nRun 1 SHA-256: a3d0b863ccae5237192d41c45590eb9b027c29d8df397b2df5c34e36a632b3d5\nRun 2 SHA-256: a3d0b863ccae5237192d41c45590eb9b027c29d8df397b2df5c34e36a632b3d5\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Boundary Value Solver",
    "subject": "a Signature boundary value solver design",
    "description": "The Boundary Value Solver is a Signature-made design for teaching boundary value problems: a solver where a learner sets the values at the two ends, the tool finds the eigenvalues for which a non-zero solution exists, and draws the eigenfunctions. A boundary value problem fixes values at the ends, not at one starting point. The solver takes the equation and the two boundary values. It reports the eigenvalues and draws the first eigenfunctions. A parameter that is not an eigenvalue is reported as giving only the zero solution.",
    "inputs": "FIGURES = {'first_eigenvalue': 9.8696, 'second_eigenvalue': 39.4784, 'eigenfunctions': 2, 'boundary_points': 2, 'non_eigenvalue': 5, 'interval_length': 1, 'modes_drawn': 2, 'design_version': 1}\nLABEL = 'a-signature-boundary-value-solver-design'\n",
    "expected": "count: 8\nlabel: a-signature-boundary-value-solver-design\nmax: 39.4784\nmean: 7.7935\nmin: 1\ntotal: 62.348\nResult: count=8|label=a-signature-boundary-value-solver-design|max=39.4784|mean=7.7935|min=1|total=62.348\nRun 1 SHA-256: 75059ede3585deab5140e8cc5fbc38a5be2e4800d5fcaaa4d8fb4c95f7df5286\nRun 2 SHA-256: 75059ede3585deab5140e8cc5fbc38a5be2e4800d5fcaaa4d8fb4c95f7df5286\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Growth Curve Lab",
    "subject": "a Signature growth curve laboratory design",
    "description": "The Growth Curve Lab is a Signature-made design for teaching the logistic equation: a laboratory where a learner sets the growth rate and the carrying capacity (the largest population the environment can support), and watches the S-shaped curve rise toward the capacity. The logistic equation is dy/dt = r y (1 - y/K). The lab draws the S-curve for the chosen rate and capacity. The inflection point at K/2 is marked, where growth is fastest. The equilibria 0 and K are shown, with 0 unstable and K stable.",
    "inputs": "FIGURES = {'growth_rate': 0.5, 'carrying_capacity': 1000, 'starting_value': 100, 'y_at_2': 232, 'y_at_6': 690.6, 'y_at_10': 942.8, 'inflection_at': 500, 'inflection_time': 4.39}\nLABEL = 'a-signature-growth-curve-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-growth-curve-laboratory-design\nmax: 1000\nmean: 433.7862\nmin: 0.5\ntotal: 3470.29\nResult: count=8|label=a-signature-growth-curve-laboratory-design|max=1000|mean=433.7862|min=0.5|total=3470.29\nRun 1 SHA-256: dbc91642685f56832d5646e21ed57188bc6f0ff618edc299e16a8ae6710f6909\nRun 2 SHA-256: dbc91642685f56832d5646e21ed57188bc6f0ff618edc299e16a8ae6710f6909\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pendulum Lab",
    "subject": "a Signature pendulum laboratory design",
    "description": "The Pendulum Lab is a Signature-made design for teaching the pendulum equation: a laboratory where a learner sets the length and the starting angle, watches the pendulum swing, and compares the true period with the small-angle approximation. The pendulum equation is theta'' + (g/L) sin(theta) = 0. The lab animates the swing and shows the period for the chosen amplitude. The small-angle period 2 pi sqrt(L/g) is shown alongside for comparison. The error of the approximation is shown as a percentage.",
    "inputs": "FIGURES = {'length': 1, 'g_value': 9.81, 'period_small': 2.006, 'period_10deg': 2.01, 'error_10deg': 0.2, 'period_60deg': 2.33, 'error_60deg': 16, 'amplitudes_tested': 2}\nLABEL = 'a-signature-pendulum-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-pendulum-laboratory-design\nmax: 16\nmean: 4.4195\nmin: 0.2\ntotal: 35.356\nResult: count=8|label=a-signature-pendulum-laboratory-design|max=16|mean=4.4195|min=0.2|total=35.356\nRun 1 SHA-256: 56c8e60b47248a7b7edb77877853ff4acfd35e27658bcd124cea99c7df98dba4\nRun 2 SHA-256: 56c8e60b47248a7b7edb77877853ff4acfd35e27658bcd124cea99c7df98dba4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Impulse Response Bench",
    "subject": "a Signature impulse response bench design",
    "description": "The Impulse Response Bench is a Signature-made design for teaching Green's functions: a bench where a learner applies a kick at one point of a system and watches the response spread, then builds the response to any forcing by adding up the kicks. A Green's function is the response to a point impulse. The bench applies an impulse at a chosen point and draws the response. The response to a distributed forcing is built by adding the impulse responses. The Green's function is displayed as a formula for the chosen operator.",
    "inputs": "FIGURES = {'y_at_half': 0.125, 'max_y': 0.125, 'interval_length': 1, 'green_pieces': 2, 'integral_parts': 2, 'boundary_values': 2, 'checks': 2, 'design_version': 1}\nLABEL = 'a-signature-impulse-response-bench-design'\n",
    "expected": "count: 8\nlabel: a-signature-impulse-response-bench-design\nmax: 2\nmean: 1.2812\nmin: 0.125\ntotal: 10.25\nResult: count=8|label=a-signature-impulse-response-bench-design|max=2|mean=1.2812|min=0.125|total=10.25\nRun 1 SHA-256: bb59f09da990e57be5104f1a8b19144f1c504090854ab71de50ac4562114435d\nRun 2 SHA-256: bb59f09da990e57be5104f1a8b19144f1c504090854ab71de50ac4562114435d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Modelling Studio",
    "subject": "a Signature modelling studio design",
    "description": "The Modelling Studio is a Signature-made design for teaching modelling with differential equations: a studio where a learner writes a balance (what goes in, minus what goes out, equals the change), the studio forms the equation, classifies it, solves it, and checks the answer. Modelling is turning a story into an equation. The studio guides the balance, the classification, the solution, and the check. Each step is scored, and a wrong step is corrected with the reason. The answer is stated with its units and its conditions.",
    "inputs": "FIGURES = {'initial_temp': 90, 'room_temp': 20, 'cooling_rate': 0.05, 'temp_at_10': 62.46, 'temp_at_30': 35.62, 'half_life': 13.86, 'steps_guided': 4, 'design_version': 1}\nLABEL = 'a-signature-modelling-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-modelling-studio-design\nmax: 90\nmean: 28.3738\nmin: 0.05\ntotal: 226.99\nResult: count=8|label=a-signature-modelling-studio-design|max=90|mean=28.3738|min=0.05|total=226.99\nRun 1 SHA-256: 9930413db8ef4c2706d66532d9ec837f3059a206cbd7bbbd0c0785d302d2dfe4\nRun 2 SHA-256: 9930413db8ef4c2706d66532d9ec837f3059a206cbd7bbbd0c0785d302d2dfe4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Power Series Expander",
    "subject": "a Signature power series expander design",
    "description": "The Power Series Expander is a Signature-made design for teaching power series solutions: an expander where a learner substitutes a series into a differential equation, and the tool matches coefficients, finds the recurrence, and shows the series converging to the function. A power series writes the unknown as a sum of powers with unknown coefficients. The series is substituted, and the coefficients are matched. The recurrence is shown, and the terms are listed. The partial sums are shown converging to the function.",
    "inputs": "FIGURES = {'terms_used': 4, 'value_at_0.5': 1.127626, 'cosh_0.5': 1.127626, 'x2_term': 0.125, 'x4_term': 0.002604, 'x6_term': 2.2e-05, 'coefficients_found': 4, 'error': 1e-06}\nLABEL = 'a-signature-power-series-expander-design'\n",
    "expected": "count: 8\nlabel: a-signature-power-series-expander-design\nmax: 4\nmean: 1.2979\nmin: 1e-06\ntotal: 10.3829\nResult: count=8|label=a-signature-power-series-expander-design|max=4|mean=1.2979|min=1e-06|total=10.3829\nRun 1 SHA-256: 69b0be01be6ad5d96be647f28263c47364a879141ed4531fd54e51a4a0adefe1\nRun 2 SHA-256: 69b0be01be6ad5d96be647f28263c47364a879141ed4531fd54e51a4a0adefe1\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Differential Equations Capstone Console",
    "subject": "a Signature differential equations capstone console design",
    "description": "The Differential Equations Capstone Console is a Signature-made design for teaching combined differential equations: a console where a learner models a system, classifies the equation, solves it, and checks it, with the plan, the checks, and the assembly scored. A capstone problem uses several tools at once. The console plans the tools: balance, classification, solution, check. Each part is solved and checked separately. The assembly is scored as a whole argument.",
    "inputs": "FIGURES = {'parts': 4, 'checks_passed': 4, 'temp_at_10': 62.46, 'temp_at_30': 35.62, 'half_life': 13.86, 'initial_temp': 90, 'cooling_rate': 0.05, 'design_version': 1}\nLABEL = 'a-signature-differential-equations-capstone-console-design'\n",
    "expected": "count: 8\nlabel: a-signature-differential-equations-capstone-console-design\nmax: 90\nmean: 26.3737\nmin: 0.05\ntotal: 210.99\nResult: count=8|label=a-signature-differential-equations-capstone-console-design|max=90|mean=26.3737|min=0.05|total=210.99\nRun 1 SHA-256: 89c29fd63583d71e437a69ad016ec085992c9e8afb0fe51fd51e474d69e46c08\nRun 2 SHA-256: 89c29fd63583d71e437a69ad016ec085992c9e8afb0fe51fd51e474d69e46c08\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Differential equation",
    "url": "https://en.wikipedia.org/wiki/Differential_equation",
    "establishes": "The reference for a Signature equation classifier design in this record."
  },
  {
    "name": "Wikipedia - Ordinary differential equation",
    "url": "https://en.wikipedia.org/wiki/Ordinary_differential_equation",
    "establishes": "The reference for a Signature equation classifier design in this record."
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
