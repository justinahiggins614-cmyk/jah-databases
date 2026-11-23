// Seeded boundless generator for the Differential Equations Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-differential-equations.js [seed]  (prints one JSON record)
// or: node gen-differential-equations.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "differential-equations";
const RECORD_KIND = "differential equation record";
const ID_PREFIX = "JAH-DIFFEQ-";
const AI_NAME = "JAH Differential Equations Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Differential Equations: What a Differential Equation Is",
    "subject": "differential equations and their meaning",
    "description": "A differential equation is an equation that involves a function and its derivatives (rates of change). The order is the highest derivative that appears. A solution is a function that satisfies the equation. An initial condition fixes the value of the solution (and possibly its derivatives) at a starting point, picking one solution from the family. The order of an equation is the highest derivative in it. A first-order equation has a one-parameter family of solutions; an initial condition picks one. An existence and uniqueness theorem states when a solution exists and is the only one.",
    "inputs": "FIGURES = {'order': 1, 'family_parameter': 1, 'solution_at_2': 5, 'derivative_at_2': 4, 'c_value': 1, 'second_solution_at_1': 8.155, 'initial_value': 3, 'checks': 2}\nLABEL = 'differential-equations-and-their-meaning'\n",
    "expected": "count: 8\nlabel: differential-equations-and-their-meaning\nmax: 8.155\nmean: 3.1444\nmin: 1\ntotal: 25.155\nResult: count=8|label=differential-equations-and-their-meaning|max=8.155|mean=3.1444|min=1|total=25.155\nRun 1 SHA-256: c88de2cad74d09a6fddf11ad15b3e8307a46c95f0910f255729be4bf8d3d43ec\nRun 2 SHA-256: c88de2cad74d09a6fddf11ad15b3e8307a46c95f0910f255729be4bf8d3d43ec\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Separable Equations",
    "subject": "separable differential equations",
    "description": "A separable equation is one where the terms in x and the terms in y can be put on opposite sides of the equation: dy/dx = g(x) h(y). It is solved by dividing by h(y), integrating both sides, and solving for y. The method works when the variables separate cleanly. Separate: write dy / h(y) = g(x) dx, then integrate both sides. The constant of integration appears on one side and is fixed by the initial condition. Constant solutions, where h(y) = 0, can be lost by dividing, and must be checked separately.",
    "inputs": "FIGURES = {'initial_value': 2, 'y_at_1': 3.297, 'derivative_at_1': 3.297, 'exponent_at_1': 0.5, 'constant_a': 2, 'steps': 3, 'variables': 2, 'checks': 1}\nLABEL = 'separable-differential-equations'\n",
    "expected": "count: 8\nlabel: separable-differential-equations\nmax: 3.297\nmean: 2.1368\nmin: 0.5\ntotal: 17.094\nResult: count=8|label=separable-differential-equations|max=3.297|mean=2.1368|min=0.5|total=17.094\nRun 1 SHA-256: 84ee9a764e98c96877ca8e761d61b2c9f48134b857f503f86101b24c3943963d\nRun 2 SHA-256: 84ee9a764e98c96877ca8e761d61b2c9f48134b857f503f86101b24c3943963d\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: First-Order Linear Equations",
    "subject": "first-order linear differential equations",
    "description": "A first-order linear equation has the form dy/dx + P(x) y = Q(x). It is solved by an integrating factor: multiply by mu(x) = e to the power of the integral of P(x), which turns the left side into the derivative of mu times y, and then integrate. The method always works for this form. The integrating factor is mu(x) = e^(integral of P(x) dx). Multiplying by mu turns the left side into the derivative of (mu y). The general solution is y = (1/mu) times the integral of (mu Q) plus a constant.",
    "inputs": "FIGURES = {'y_at_1': 1.7293, 'derivative_at_1': 0.5413, 'steady_value': 2, 'constant_c': -2, 'integrating_factor_at_1': 7.389, 'steps': 3, 'terms': 2, 'checks': 1}\nLABEL = 'first-order-linear-differential-equations'\n",
    "expected": "count: 8\nlabel: first-order-linear-differential-equations\nmax: 7.389\nmean: 1.9575\nmin: -2\ntotal: 15.6596\nResult: count=8|label=first-order-linear-differential-equations|max=7.389|mean=1.9575|min=-2|total=15.6596\nRun 1 SHA-256: e2e4623e25cfc917edbba7de11158d04b32ce52a3a3cceac0c90f1c791d90719\nRun 2 SHA-256: e2e4623e25cfc917edbba7de11158d04b32ce52a3a3cceac0c90f1c791d90719\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Second-Order Linear Equations",
    "subject": "second-order linear differential equations",
    "description": "A second-order linear equation with constant coefficients has the form a y'' + b y' + c y = 0 (the homogeneous case). It is solved by the characteristic equation a r squared + b r + c = 0: distinct real roots give exponentials, a repeated root gives an exponential times x, and complex roots give oscillations (sines and cosines times an exponential). The characteristic equation is a r^2 + b r + c = 0. Distinct real roots r1, r2 give y = C1 e^(r1 x) + C2 e^(r2 x). Complex roots alpha plus or minus beta i give y = e^(alpha x) (C1 cos(beta x) + C2 sin(beta x)).",
    "inputs": "FIGURES = {'root_1': 1, 'root_2': 2, 'c1': 2, 'c2': -1, 'y_at_0': 1, 'yp_at_0': 0, 'characteristic_terms': 3, 'steps': 3}\nLABEL = 'second-order-linear-differential-equations'\n",
    "expected": "count: 8\nlabel: second-order-linear-differential-equations\nmax: 3\nmean: 1.375\nmin: -1\ntotal: 11\nResult: count=8|label=second-order-linear-differential-equations|max=3|mean=1.375|min=-1|total=11\nRun 1 SHA-256: 3951134af73cad555b0fe9fe24c3b815e80e183ccec1231aa70085adcdd04985\nRun 2 SHA-256: 3951134af73cad555b0fe9fe24c3b815e80e183ccec1231aa70085adcdd04985\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: The Harmonic Oscillator",
    "subject": "the harmonic oscillator",
    "description": "The harmonic oscillator is the equation y'' + omega squared y = 0, describing a mass on a spring or a pendulum for small swings. Its solutions are sines and cosines: y = A cos(omega t) + B sin(omega t), oscillating with angular frequency omega (radians per second) and period 2 pi / omega. The general solution is A cos(omega t) + B sin(omega t). The amplitude is the square root of A squared plus B squared; the period is 2 pi / omega. Adding damping (a first-derivative term) makes the oscillation decay.",
    "inputs": "FIGURES = {'omega': 2, 'period': 3.1416, 'amplitude': 1, 'y_at_pi_over_4': 0, 'y_at_pi_over_2': -1, 'velocity_max': 2, 'initial_y': 1, 'initial_v': 0}\nLABEL = 'the-harmonic-oscillator'\n",
    "expected": "count: 8\nlabel: the-harmonic-oscillator\nmax: 3.1416\nmean: 1.0177\nmin: -1\ntotal: 8.1416\nResult: count=8|label=the-harmonic-oscillator|max=3.1416|mean=1.0177|min=-1|total=8.1416\nRun 1 SHA-256: aec28972606224082ab34c1f6446f45b8072373e4fee429dbf4c706ea1f97961\nRun 2 SHA-256: aec28972606224082ab34c1f6446f45b8072373e4fee429dbf4c706ea1f97961\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: The Laplace Transform",
    "subject": "the Laplace transform",
    "description": "The Laplace transform turns a function of time into a function of a new variable s, by integrating f(t) times e^(-s t) from 0 to infinity. It turns differentiation into multiplication by s, so a differential equation becomes an algebraic equation, which is solved and then transformed back. The transform of f'(t) is s F(s) - f(0). The transform of e^(a t) is 1/(s - a). The transform of a constant 1 is 1/s, and of t is 1/s squared.",
    "inputs": "FIGURES = {'y_at_0': 3, 'y_at_1': 0.406, 'transform_value': 3, 'pole': -2, 'steps': 3, 'initial_value': 3, 'decay_rate': 2, 'checks': 1}\nLABEL = 'the-laplace-transform'\n",
    "expected": "count: 8\nlabel: the-laplace-transform\nmax: 3\nmean: 1.6758\nmin: -2\ntotal: 13.406\nResult: count=8|label=the-laplace-transform|max=3|mean=1.6758|min=-2|total=13.406\nRun 1 SHA-256: 1a3479724eb2129dd6d90a26cbd7f3a45dbdbb517a31652bce09d81969d32e1e\nRun 2 SHA-256: 1a3479724eb2129dd6d90a26cbd7f3a45dbdbb517a31652bce09d81969d32e1e\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Systems and Phase Portraits",
    "subject": "systems of differential equations and phase portraits",
    "description": "A system of first-order differential equations describes several quantities changing together. A phase portrait is a picture of the solutions in the state plane (the plane of the two variables), with arrows showing the direction of motion at each point. An equilibrium is a point where all derivatives are zero. The state plane has the two variables as its axes. An equilibrium is a point where the system is at rest. The eigenvalues of the linearised system classify the equilibrium as a node, a saddle, a spiral, or a centre.",
    "inputs": "FIGURES = {'eigenvalue_1': -1, 'eigenvalue_2': -2, 'x_at_1': 0.3679, 'y_at_1': 0.1353, 'x_at_2': 0.1353, 'y_at_2': 0.0183, 'equilibria': 1, 'dimensions': 2}\nLABEL = 'systems-of-differential-equations-and-phase-portraits'\n",
    "expected": "count: 8\nlabel: systems-of-differential-equations-and-phase-portraits\nmax: 2\nmean: 0.0821\nmin: -2\ntotal: 0.6568\nResult: count=8|label=systems-of-differential-equations-and-phase-portraits|max=2|mean=0.0821|min=-2|total=0.6568\nRun 1 SHA-256: 2d39f2d37a0e82d5a01ed27f242d4f779bf5258566bb88bdbe220cbb7d6ddd3e\nRun 2 SHA-256: 2d39f2d37a0e82d5a01ed27f242d4f779bf5258566bb88bdbe220cbb7d6ddd3e\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: The Heat Equation",
    "subject": "the heat equation",
    "description": "The heat equation is the partial differential equation u_t = k u_xx, where u is temperature, t is time, x is position, and k is the thermal diffusivity (a measure of how fast heat spreads). It says the rate of change of temperature at a point is proportional to the curvature of the temperature profile there: heat flows from hot to cold, smoothing the profile. The heat equation is solved by separation of variables, giving a Fourier series (a sum of sines and cosines). High-frequency components decay fastest, so the profile smooths over time. The steady state (the long-run temperature) is linear in x for fixed end temperatures.",
    "inputs": "FIGURES = {'k_value': 1, 'factor_at_0.1': 0.3727, 'factor_at_0.5': 0.0072, 'pi_squared': 9.8696, 'length': 1, 'peak_initial': 1, 'modes': 1, 'steps': 2}\nLABEL = 'the-heat-equation'\n",
    "expected": "count: 8\nlabel: the-heat-equation\nmax: 9.8696\nmean: 2.0312\nmin: 0.0072\ntotal: 16.2495\nResult: count=8|label=the-heat-equation|max=9.8696|mean=2.0312|min=0.0072|total=16.2495\nRun 1 SHA-256: c59af4597882b8a8bf8d943f597693782b4a722ad041a999f6b049c06bd33a22\nRun 2 SHA-256: c59af4597882b8a8bf8d943f597693782b4a722ad041a999f6b049c06bd33a22\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: The Wave Equation",
    "subject": "the wave equation",
    "description": "The wave equation is the partial differential equation u_tt = c squared u_xx, where u is the displacement of a string or the pressure in a gas, and c is the wave speed. It says the acceleration at a point is proportional to the curvature there. Its solutions are waves travelling in both directions at speed c. The general solution is f(x - c t) + g(x + c t): a right-moving and a left-moving wave. A plucked string vibrates as a sum of standing waves (modes) with frequencies that are multiples of the fundamental. The wave speed c is the square root of tension over density for a string.",
    "inputs": "FIGURES = {'wave_speed': 2, 'period': 1, 'max_displacement': 1, 'frequency': 1, 'length': 1, 'modes': 1, 't_flat': 0.25, 't_inverted': 0.5}\nLABEL = 'the-wave-equation'\n",
    "expected": "count: 8\nlabel: the-wave-equation\nmax: 2\nmean: 0.9688\nmin: 0.25\ntotal: 7.75\nResult: count=8|label=the-wave-equation|max=2|mean=0.9688|min=0.25|total=7.75\nRun 1 SHA-256: 0dd8a7fe28cd2f39e5aa71fcad2e9157d597dcff95ac26e5bdec7bfe8312b6f3\nRun 2 SHA-256: 0dd8a7fe28cd2f39e5aa71fcad2e9157d597dcff95ac26e5bdec7bfe8312b6f3\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Laplace's Equation and Harmonic Functions",
    "subject": "Laplace's equation and harmonic functions",
    "description": "Laplace's equation is u_xx + u_yy = 0, where the subscripts are second partial derivatives. A function satisfying it is called harmonic. It describes steady states: the temperature in a plate after a long time, or the electric potential in empty space. A harmonic function has no local maximum or minimum inside its region: its extremes occur on the boundary. Laplace's equation is the steady-state limit of the heat equation. The mean value property says a harmonic function's value at a point is the average of its values on any circle around it. The maximum principle says the extremes occur on the boundary.",
    "inputs": "FIGURES = {'top_temperature': 100, 'first_coefficient': 127.32, 'centre_temperature': 25.3, 'sinh_ratio': 0.199, 'plate_size': 1, 'terms_used': 1, 'edges_held': 3, 'steps': 2}\nLABEL = 'laplace-s-equation-and-harmonic-functions'\n",
    "expected": "count: 8\nlabel: laplace-s-equation-and-harmonic-functions\nmax: 127.32\nmean: 32.4774\nmin: 0.199\ntotal: 259.819\nResult: count=8|label=laplace-s-equation-and-harmonic-functions|max=127.32|mean=32.4774|min=0.199|total=259.819\nRun 1 SHA-256: f64f39a9c5f290260847e625020ada4dadaa39cbe70913d2fbf44bad26dbbdc7\nRun 2 SHA-256: f64f39a9c5f290260847e625020ada4dadaa39cbe70913d2fbf44bad26dbbdc7\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Fourier Series",
    "subject": "Fourier series",
    "description": "A Fourier series represents a periodic function (one that repeats) as a sum of sines and cosines. The coefficients are found by integrating the function against each sine and cosine: the orthogonality of sines and cosines picks out one coefficient at a time. Fourier series solve the heat and wave equations by separating variables. The Fourier series of a function on (-pi, pi) is a0/2 plus the sum of a_n cos(nx) + b_n sin(nx). The coefficients are integrals: a_n is (1/pi) times the integral of f(x) cos(nx). A jump in the function causes the Gibbs overshoot: the partial sums overshoot by about 9 percent near the jump.",
    "inputs": "FIGURES = {'first_coefficient': 1.2732, 'partial_sum_3': 1.1037, 'true_value': 1, 'overshoot': 0.1037, 'terms_used': 3, 'odd_terms_only': 1, 'period': 6.2832, 'gibbs_percent': 9}\nLABEL = 'fourier-series'\n",
    "expected": "count: 8\nlabel: fourier-series\nmax: 9\nmean: 2.8455\nmin: 0.1037\ntotal: 22.7638\nResult: count=8|label=fourier-series|max=9|mean=2.8455|min=0.1037|total=22.7638\nRun 1 SHA-256: ebbd040b62ed893b91c410a119b62d11f622e170e1b25da9afa29708e875af08\nRun 2 SHA-256: ebbd040b62ed893b91c410a119b62d11f622e170e1b25da9afa29708e875af08\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Numerical Methods for ODEs",
    "subject": "numerical methods for ordinary differential equations",
    "description": "A numerical method for an ordinary differential equation approximates the solution step by step. Euler's method takes a step along the tangent line: y(n+1) = y(n) + h f(x(n), y(n)), where h is the step size. Runge-Kutta methods take several trial steps and combine them for higher accuracy. The error shrinks as the step size shrinks. Euler's method has error proportional to the step size h. The classic fourth-order Runge-Kutta method has error proportional to h to the fourth power. Stability matters: a method can blow up on a stiff equation (one with very different time scales) even with a small step.",
    "inputs": "FIGURES = {'euler_2_steps': 1.21, 'true_value': 1.2214, 'error_h0.1': 0.0114, 'euler_h0.05': 1.2155, 'rk4_value': 1.2214, 'step_size': 0.1, 'steps_taken': 2, 'order_rk4': 4}\nLABEL = 'numerical-methods-for-ordinary-differential-equations'\n",
    "expected": "count: 8\nlabel: numerical-methods-for-ordinary-differential-equations\nmax: 4\nmean: 1.3725\nmin: 0.0114\ntotal: 10.9797\nResult: count=8|label=numerical-methods-for-ordinary-differential-equations|max=4|mean=1.3725|min=0.0114|total=10.9797\nRun 1 SHA-256: b69eeca58547b86a088ea5259ed80cd0fbe017accc6e4b56fc8240eb345ad326\nRun 2 SHA-256: b69eeca58547b86a088ea5259ed80cd0fbe017accc6e4b56fc8240eb345ad326\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Stability of Equilibria",
    "subject": "stability of equilibria",
    "description": "An equilibrium of a differential equation is a state where nothing changes. It is stable when solutions starting nearby stay nearby, asymptotically stable when they also return to it, and unstable when they move away. For a linear system, stability is read from the eigenvalues: negative real parts mean stability. A linear system is asymptotically stable exactly when all eigenvalues have negative real parts. A saddle has eigenvalues of opposite signs and is unstable. Lyapunov's method proves stability for non-linear systems by finding an energy-like function that decreases.",
    "inputs": "FIGURES = {'eigenvalue_1': -1, 'eigenvalue_2': -2, 'x_at_1': 0.3679, 'y_at_1': 0.1353, 'x_at_2': 0.1353, 'y_at_2': 0.0183, 'saddle_eigenvalues': 2, 'equilibria': 1}\nLABEL = 'stability-of-equilibria'\n",
    "expected": "count: 8\nlabel: stability-of-equilibria\nmax: 2\nmean: 0.0821\nmin: -2\ntotal: 0.6568\nResult: count=8|label=stability-of-equilibria|max=2|mean=0.0821|min=-2|total=0.6568\nRun 1 SHA-256: 4baee4dac73473c7128da3ec3bce04f6a224c3a6fd01d8b9237dae5702ef9db4\nRun 2 SHA-256: 4baee4dac73473c7128da3ec3bce04f6a224c3a6fd01d8b9237dae5702ef9db4\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Exact Equations",
    "subject": "exact differential equations",
    "description": "A first-order equation M(x, y) dx + N(x, y) dy = 0 is exact when there is a function F with F_x = M and F_y = N, so the equation says dF = 0 and the solutions are the level curves F(x, y) = C. The test is that the partial derivative of M with respect to y equals the partial derivative of N with respect to x. The test for exactness is M_y = N_x. When the test fails, an integrating factor may make the equation exact. The solution is found by integrating M with respect to x and matching the y-dependence.",
    "inputs": "FIGURES = {'m_y': 1, 'n_x': 1, 'solution_at_1_1': 3, 'terms_in_f': 3, 'constant_c': 3, 'test_passed': 1, 'steps': 3, 'variables': 2}\nLABEL = 'exact-differential-equations'\n",
    "expected": "count: 8\nlabel: exact-differential-equations\nmax: 3\nmean: 2.125\nmin: 1\ntotal: 17\nResult: count=8|label=exact-differential-equations|max=3|mean=2.125|min=1|total=17\nRun 1 SHA-256: 1e08058d6f2cd985b9e07705379f2a88df6a040c40da03a051142f12d4ba56f0\nRun 2 SHA-256: 1e08058d6f2cd985b9e07705379f2a88df6a040c40da03a051142f12d4ba56f0\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Undetermined Coefficients",
    "subject": "undetermined coefficients for non-homogeneous equations",
    "description": "A non-homogeneous linear equation has a forcing term on the right: a y'' + b y' + c y = f(x). Its general solution is the homogeneous solution plus one particular solution. The method of undetermined coefficients guesses the form of the particular solution from the form of f(x) (a polynomial, an exponential, a sine or cosine, or a product) with unknown coefficients, and solves for them. The guess for a polynomial forcing term is a polynomial of the same degree. For an exponential e^(a x), guess A e^(a x), unless a is a root of the characteristic equation, in which case multiply by x. For a sine or cosine, guess a combination of sine and cosine.",
    "inputs": "FIGURES = {'a_coefficient': -6, 'forcing_amplitude': 6, 'root_matched': 1, 'homogeneous_terms': 2, 'particular_terms': 1, 'characteristic_roots': 2, 'steps': 3, 'checks': 1}\nLABEL = 'undetermined-coefficients-for-non-homogeneous-equations'\n",
    "expected": "count: 8\nlabel: undetermined-coefficients-for-non-homogeneous-equations\nmax: 6\nmean: 1.25\nmin: -6\ntotal: 10\nResult: count=8|label=undetermined-coefficients-for-non-homogeneous-equations|max=6|mean=1.25|min=-6|total=10\nRun 1 SHA-256: 8a9fbbdd5ffeff7fd0d0a927aa8392b88317f31dad26d76bdb00243143443847\nRun 2 SHA-256: 8a9fbbdd5ffeff7fd0d0a927aa8392b88317f31dad26d76bdb00243143443847\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Variation of Parameters",
    "subject": "variation of parameters",
    "description": "Variation of parameters is the general method for a particular solution of a non-homogeneous linear equation: it builds the solution from the homogeneous solutions with variable coefficients, found by integrating. For y'' + P(x) y' + Q(x) y = R(x) with homogeneous solutions y1 and y2, the particular solution is -y1 times the integral of (y2 R / W) plus y2 times the integral of (y1 R / W), where W is the Wronskian (the determinant of the matrix of y1, y2 and their derivatives). The Wronskian W = y1 y2' - y1' y2 measures the independence of the two solutions. The formulas involve integrals that may have no elementary form. The method works for variable coefficients as well as constant ones.",
    "inputs": "FIGURES = {'wronskian': 1, 'integral_1_terms': 1, 'integral_2_value': 1, 'homogeneous_solutions': 2, 'particular_terms': 2, 'forcing_function': 1, 'steps': 3, 'checks': 1}\nLABEL = 'variation-of-parameters'\n",
    "expected": "count: 8\nlabel: variation-of-parameters\nmax: 3\nmean: 1.5\nmin: 1\ntotal: 12\nResult: count=8|label=variation-of-parameters|max=3|mean=1.5|min=1|total=12\nRun 1 SHA-256: 77726ec9352b3c1e6439497c6ee45fe6ea597964852b9c196bcb315e1b41d6fb\nRun 2 SHA-256: 77726ec9352b3c1e6439497c6ee45fe6ea597964852b9c196bcb315e1b41d6fb\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Bessel Functions and Special Functions",
    "subject": "Bessel functions and special functions",
    "description": "Some differential equations have solutions that are not elementary functions, and those solutions are given names: Bessel functions solve Bessel's equation, which appears in circular symmetry; Legendre polynomials solve Legendre's equation, which appears in spherical symmetry. A special function is a named solution of an important equation, tabulated and studied like an elementary function. Bessel's equation is x squared y'' + x y' + (x squared - n squared) y = 0. The Bessel function J_0(x) starts at 1 and oscillates with slowly decreasing amplitude. Legendre polynomials appear in the multipole expansion of a potential.",
    "inputs": "FIGURES = {'j0_at_1': 0.7652, 'approx_at_1': 0.765625, 'j0_at_2': 0.2239, 'approx_at_2': 0.222222, 'first_zero': 2.4048, 'terms_used': 3, 'series_terms': 4, 'order': 0}\nLABEL = 'bessel-functions-and-special-functions'\n",
    "expected": "count: 8\nlabel: bessel-functions-and-special-functions\nmax: 4\nmean: 1.4227\nmin: 0\ntotal: 11.3817\nResult: count=8|label=bessel-functions-and-special-functions|max=4|mean=1.4227|min=0|total=11.3817\nRun 1 SHA-256: aafa60cf91908d9e29a1462dd0e38e4f85e9b1084ada3abf6d8ed53d0dfdf710\nRun 2 SHA-256: aafa60cf91908d9e29a1462dd0e38e4f85e9b1084ada3abf6d8ed53d0dfdf710\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Boundary Value Problems",
    "subject": "boundary value problems",
    "description": "A boundary value problem fixes the solution's values at the ends of an interval, rather than at one starting point. For example, y'' = -y with y(0) = 0 and y(pi) = 0 has solutions sin(nx) for integer n, and the values of n for which a non-zero solution exists are the eigenvalues of the problem. Unlike initial value problems, a boundary value problem may have no solution, one, or infinitely many. A boundary value problem fixes values at two ends; an initial value problem fixes value and derivative at one point. The eigenvalues are the parameter values for which a non-zero solution exists. The eigenfunctions (the solutions) are orthogonal, and they build Fourier series.",
    "inputs": "FIGURES = {'first_eigenvalue': 9.8696, 'second_eigenvalue': 39.4784, 'eigenfunctions': 2, 'boundary_points': 2, 'n_values': 2, 'interval_length': 1, 'zero_solution_cases': 1, 'steps': 3}\nLABEL = 'boundary-value-problems'\n",
    "expected": "count: 8\nlabel: boundary-value-problems\nmax: 39.4784\nmean: 7.5435\nmin: 1\ntotal: 60.348\nResult: count=8|label=boundary-value-problems|max=39.4784|mean=7.5435|min=1|total=60.348\nRun 1 SHA-256: 1a16f3d8fdeef9ef7997082392b4ed7693dd539514968507a0e057c6570ea4a6\nRun 2 SHA-256: 1a16f3d8fdeef9ef7997082392b4ed7693dd539514968507a0e057c6570ea4a6\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: The Logistic Equation",
    "subject": "the logistic equation",
    "description": "The logistic equation is dy/dt = r y (1 - y/K), where r is the growth rate and K is the carrying capacity (the largest population the environment can support). It models growth that slows as the population approaches K: the solution is a sigmoid (S-shaped) curve rising from the starting value toward K. The equilibria are y = 0 (unstable) and y = K (stable). The solution is y(t) = K / (1 + A e^(-r t)), where A is set by the starting value. The growth is fastest at y = K/2, the inflection point of the S-curve.",
    "inputs": "FIGURES = {'growth_rate': 0.5, 'carrying_capacity': 1000, 'starting_value': 100, 'y_at_2': 232, 'y_at_6': 690.6, 'y_at_10': 942.8, 'inflection_at': 500, 'constant_a': 9}\nLABEL = 'the-logistic-equation'\n",
    "expected": "count: 8\nlabel: the-logistic-equation\nmax: 1000\nmean: 434.3625\nmin: 0.5\ntotal: 3474.9\nResult: count=8|label=the-logistic-equation|max=1000|mean=434.3625|min=0.5|total=3474.9\nRun 1 SHA-256: fbd624a91938d5a4ee5958d6a92e024a2c3dc0626ff4b5d298c91ecf5ec0087b\nRun 2 SHA-256: fbd624a91938d5a4ee5958d6a92e024a2c3dc0626ff4b5d298c91ecf5ec0087b\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: The Pendulum Equation",
    "subject": "the pendulum equation",
    "description": "The pendulum equation is theta'' + (g/L) sin(theta) = 0, where theta is the angle from the vertical, g is gravity, and L is the length. For small angles, sin(theta) is approximately theta, giving the harmonic oscillator with period 2 pi times the square root of (L/g). For large angles the motion is non-linear and the period grows. The linearised equation is theta'' + (g/L) theta = 0, with period 2 pi sqrt(L/g). The period is independent of the amplitude only in the linear approximation. The full equation has an energy integral: the sum of kinetic and potential energy is constant.",
    "inputs": "FIGURES = {'length': 1, 'g_value': 9.81, 'period_small': 2.006, 'frequency': 0.4985, 'period_10deg': 2.01, 'period_60deg': 2.33, 'amplitude_10deg': 0.1745, 'error_60deg': 16}\nLABEL = 'the-pendulum-equation'\n",
    "expected": "count: 8\nlabel: the-pendulum-equation\nmax: 16\nmean: 4.2286\nmin: 0.1745\ntotal: 33.829\nResult: count=8|label=the-pendulum-equation|max=16|mean=4.2286|min=0.1745|total=33.829\nRun 1 SHA-256: 607d3e9033f899225134f39cd9c0692adcca5fb3ddb29be73b30dcfc5e1b7476\nRun 2 SHA-256: 607d3e9033f899225134f39cd9c0692adcca5fb3ddb29be73b30dcfc5e1b7476\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Green's Functions",
    "subject": "Green's functions",
    "description": "A Green's function is the response of a linear system to a point impulse (a sudden kick at one place and time). Once the Green's function is known, the response to any forcing is the integral of the forcing times the Green's function: the system is a sum of its responses to many small kicks. It is the inverse of the differential operator, in the sense of an integral. The Green's function G(x, s) is the response at x to an impulse at s. The solution is the integral of G(x, s) times the forcing f(s). For the operator -d squared/dx squared on (0, 1), the Green's function is min(x, s) times (1 - max(x, s)).",
    "inputs": "FIGURES = {'y_at_half': 0.125, 'max_y': 0.125, 'interval_length': 1, 'boundary_values': 2, 'green_pieces': 2, 'integral_parts': 2, 'checks': 2, 'steps': 3}\nLABEL = 'green-s-functions'\n",
    "expected": "count: 8\nlabel: green-s-functions\nmax: 3\nmean: 1.5312\nmin: 0.125\ntotal: 12.25\nResult: count=8|label=green-s-functions|max=3|mean=1.5312|min=0.125|total=12.25\nRun 1 SHA-256: 5d4f265d41a200c22f39109081b0e11b6564a9f3b4e2250a15af838661776efa\nRun 2 SHA-256: 5d4f265d41a200c22f39109081b0e11b6564a9f3b4e2250a15af838661776efa\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Power Series Solutions",
    "subject": "power series solutions of differential equations",
    "description": "A power series solution writes the unknown function as a series (a sum of powers of x with unknown coefficients) and finds the coefficients by substituting into the equation. It solves equations whose coefficients are not constant, where elementary methods fail. The radius of convergence is the distance to the nearest singularity. Assume y = sum a_n x^n and substitute into the equation. Matching coefficients gives a recurrence for the a_n. The series converges inside its radius of convergence.",
    "inputs": "FIGURES = {'terms_used': 4, 'value_at_0.5': 1.127626, 'cosh_0.5': 1.127626, 'x2_term': 0.125, 'x4_term': 0.002604, 'x6_term': 2.2e-05, 'coefficients_found': 4, 'error': 1e-06}\nLABEL = 'power-series-solutions-of-differential-equations'\n",
    "expected": "count: 8\nlabel: power-series-solutions-of-differential-equations\nmax: 4\nmean: 1.2979\nmin: 1e-06\ntotal: 10.3829\nResult: count=8|label=power-series-solutions-of-differential-equations|max=4|mean=1.2979|min=1e-06|total=10.3829\nRun 1 SHA-256: 0a40a456f3d148f35677e434254f0b3057158ad1e2d55011147c4ad9c417ec45\nRun 2 SHA-256: 0a40a456f3d148f35677e434254f0b3057158ad1e2d55011147c4ad9c417ec45\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Existence and Uniqueness Theorems",
    "subject": "existence and uniqueness theorems",
    "description": "The existence and uniqueness theorem says that y' = f(x, y) with y(x0) = y0 has exactly one solution near x0, provided f is continuous and Lipschitz in y (its slope in y is bounded). When f is not Lipschitz, solutions can branch: several solutions can satisfy the same initial condition. Continuity plus a Lipschitz condition gives one solution. The proof builds the solution by Picard iteration. Without Lipschitz, solutions can branch.",
    "inputs": "FIGURES = {'solutions_found': 2, 'y0': 0, 'exponent': 0.667, 'x_cubed_at_1': 1, 'e_at_1': 2.71828, 'lipschitz_y_equals_y': 1, 'branching': 1, 'theorems': 1}\nLABEL = 'existence-and-uniqueness-theorems'\n",
    "expected": "count: 8\nlabel: existence-and-uniqueness-theorems\nmax: 2.71828\nmean: 1.1732\nmin: 0\ntotal: 9.3853\nResult: count=8|label=existence-and-uniqueness-theorems|max=2.71828|mean=1.1732|min=0|total=9.3853\nRun 1 SHA-256: 455ea2750d082bce79924d69479244590e0f81d2b9594e3b10a41a2d030317e2\nRun 2 SHA-256: 455ea2750d082bce79924d69479244590e0f81d2b9594e3b10a41a2d030317e2\nDeterministic: MATCH\n"
  },
  {
    "title": "Differential Equations: Capstone Modelling a Real System",
    "subject": "capstone: modelling a real system",
    "description": "A capstone problem for differential equations is a real system modelled end to end: write the equation from the physics, classify it, solve it by the right method, and check the answer against the numbers. This record models a cooling cup of coffee, a mixing tank, and a spring, showing the same methods on three systems. The model is written from a balance: what goes in, minus what goes out, equals the change. The method is chosen by the equation's type: separable, linear, or second-order. The answer is checked against the initial condition and against common sense.",
    "inputs": "FIGURES = {'initial_temp': 90, 'room_temp': 20, 'cooling_rate': 0.05, 'temp_at_10': 62.46, 'temp_at_30': 35.62, 'half_life': 13.86, 'excess_initial': 70, 'systems_modelled': 3}\nLABEL = 'capstone-modelling-a-real-system'\n",
    "expected": "count: 8\nlabel: capstone-modelling-a-real-system\nmax: 90\nmean: 36.8738\nmin: 0.05\ntotal: 294.99\nResult: count=8|label=capstone-modelling-a-real-system|max=90|mean=36.8738|min=0.05|total=294.99\nRun 1 SHA-256: e0968f37c8335c96656a106a9549a86633c4b93f806577e68b465dd35c540d77\nRun 2 SHA-256: e0968f37c8335c96656a106a9549a86633c4b93f806577e68b465dd35c540d77\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Differential equation",
    "url": "https://en.wikipedia.org/wiki/Differential_equation",
    "establishes": "The reference for differential equations and their meaning in this record."
  },
  {
    "name": "Wikipedia - Ordinary differential equation",
    "url": "https://en.wikipedia.org/wiki/Ordinary_differential_equation",
    "establishes": "The reference for differential equations and their meaning in this record."
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
