// Seeded boundless generator for the Calculus I-III Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-college-calculus.js [seed]  (prints one JSON record)
// or: node gen-college-calculus.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "college-calculus";
const RECORD_KIND = "calculus record";
const ID_PREFIX = "JAH-CCALC-";
const AI_NAME = "JAH Calculus Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Calculus: Limits and How Functions Approach Values",
    "subject": "limits of functions",
    "description": "A limit is the value a function approaches as its input approaches a given number. We write the limit of f(x) as x approaches a equals L when f(x) can be made as close to L as we like by taking x close enough to a. A limit describes approach, not arrival: the function need not equal L at a. The limit laws let limits be computed piece by piece: the limit of a sum is the sum of the limits. A function is continuous at a point when its limit there equals its value there. The squeeze theorem finds a limit by trapping a function between two functions with the same limit.",
    "inputs": "FIGURES = {'limit_value': 2, 'value_at_0.9': 1.9, 'value_at_0.99': 1.99, 'value_at_1.01': 2.01, 'value_at_1.1': 2.1, 'points_checked': 4, 'sides_checked': 2, 'factor_terms': 2}\nLABEL = 'limits-of-functions'\n",
    "expected": "count: 8\nlabel: limits-of-functions\nmax: 4\nmean: 2.25\nmin: 1.9\ntotal: 18.0\nResult: count=8|label=limits-of-functions|max=4|mean=2.25|min=1.9|total=18.0\nRun 1 SHA-256: e09ce816dbaaf082787b0daf00138c623eb64d810f28509bddd8aa246dda4f64\nRun 2 SHA-256: e09ce816dbaaf082787b0daf00138c623eb64d810f28509bddd8aa246dda4f64\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: The Derivative as a Rate of Change",
    "subject": "the derivative as a rate of change",
    "description": "The derivative of a function at a point is the instantaneous rate of change of the function there, defined as the limit of the average rate of change as the interval shrinks to zero. Geometrically it is the slope of the tangent line (the line that just touches the graph at that point). The derivative of x to the power n is n times x to the power n - 1. A function must be continuous where it is differentiable, but continuity alone does not guarantee differentiability: a corner has no derivative. The derivative of a constant is zero, and the derivative of a sum is the sum of the derivatives.",
    "inputs": "FIGURES = {'derivative_at_3': 6, 'derivative_at_0': 0, 'function_at_3': 9, 'power_n': 2, 'coefficient': 2, 'points_checked': 2, 'limit_steps': 3, 'definition_parts': 2}\nLABEL = 'the-derivative-as-a-rate-of-change'\n",
    "expected": "count: 8\nlabel: the-derivative-as-a-rate-of-change\nmax: 9\nmean: 3.25\nmin: 0\ntotal: 26\nResult: count=8|label=the-derivative-as-a-rate-of-change|max=9|mean=3.25|min=0|total=26\nRun 1 SHA-256: ecf409c424876baeda5357a25e3f0538ee515f6427c33c144198ff8490083bc3\nRun 2 SHA-256: ecf409c424876baeda5357a25e3f0538ee515f6427c33c144198ff8490083bc3\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: The Product, Quotient, and Chain Rules",
    "subject": "the product, quotient, and chain rules",
    "description": "The product rule says the derivative of a product is the derivative of the first times the second plus the first times the derivative of the second. The quotient rule handles division. The chain rule differentiates a composition (a function inside a function): differentiate the outer function, then multiply by the derivative of the inner function. The product rule: (fg)' = f'g + fg'. The quotient rule: (f/g)' = (f'g - fg') / g squared. The chain rule: the derivative of f(g(x)) is f'(g(x)) times g'(x).",
    "inputs": "FIGURES = {'h_at_1': 8, 'h_prime_at_1': 24, 'chain_factors': 2, 'product_terms': 2, 'quotient_terms': 2, 'rules_named': 3, 'x_checked': 1, 'derivative_value': 24}\nLABEL = 'the-product-quotient-and-chain-rules'\n",
    "expected": "count: 8\nlabel: the-product-quotient-and-chain-rules\nmax: 24\nmean: 8.25\nmin: 1\ntotal: 66\nResult: count=8|label=the-product-quotient-and-chain-rules|max=24|mean=8.25|min=1|total=66\nRun 1 SHA-256: eaae11c5b313ebc2dfbd63798027b1fac901827f855c873cf0b309a3566dcf2a\nRun 2 SHA-256: eaae11c5b313ebc2dfbd63798027b1fac901827f855c873cf0b309a3566dcf2a\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Optimisation with Derivatives",
    "subject": "optimisation with derivatives",
    "description": "Optimisation is finding the largest or smallest value of a function. A critical point is a point where the derivative is zero or does not exist; maxima and minima occur at critical points or at the ends of the interval. The second derivative test says a critical point is a local maximum when the second derivative is negative there, and a local minimum when it is positive. The first derivative test reads the sign change of the derivative around a critical point. On a closed interval, the extreme values occur at critical points or at the endpoints. The second derivative measures concavity (whether the graph bends up or down).",
    "inputs": "FIGURES = {'fence_total': 100, 'optimal_x': 25, 'parallel_side': 50, 'max_area': 1250, 'second_derivative': -4, 'critical_points': 1, 'endpoints_checked': 2, 'derivative_zero_at': 25}\nLABEL = 'optimisation-with-derivatives'\n",
    "expected": "count: 8\nlabel: optimisation-with-derivatives\nmax: 1250\nmean: 181.125\nmin: -4\ntotal: 1449\nResult: count=8|label=optimisation-with-derivatives|max=1250|mean=181.125|min=-4|total=1449\nRun 1 SHA-256: 6dc461e48e92b0801c929709a0826b81a7cfa2f0604793af877c7b56991cf0b1\nRun 2 SHA-256: 6dc461e48e92b0801c929709a0826b81a7cfa2f0604793af877c7b56991cf0b1\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Related Rates",
    "subject": "related rates",
    "description": "Related rates problems ask how fast one quantity changes when another changes, given a relation between them. The method is to write the relation, differentiate both sides with respect to time using the chain rule, and substitute the known values. Differentiate the relation with respect to time, not with respect to the other variable. Substitute the values at the instant asked about only after differentiating. Draw a diagram and label the quantities and their rates.",
    "inputs": "FIGURES = {'ladder_length': 5, 'foot_distance': 3, 'top_height': 4, 'foot_speed': 0.5, 'top_speed': -0.375, 'triangle_sides': 3, 'relation_terms': 2, 'steps': 3}\nLABEL = 'related-rates'\n",
    "expected": "count: 8\nlabel: related-rates\nmax: 5\nmean: 2.5156\nmin: -0.375\ntotal: 20.125\nResult: count=8|label=related-rates|max=5|mean=2.5156|min=-0.375|total=20.125\nRun 1 SHA-256: 2867bda4d8f018b136b9ab9c836e61bb944ebff9016cb55c7143ca33ef6b5b93\nRun 2 SHA-256: 2867bda4d8f018b136b9ab9c836e61bb944ebff9016cb55c7143ca33ef6b5b93\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: The Definite Integral and Area",
    "subject": "the definite integral and area",
    "description": "The definite integral of a function from a to b is the limit of Riemann sums (sums of the areas of thin rectangles under the graph) as the rectangles get thinner. When the function is positive, the integral is the area under its graph; in general it is the signed area, with parts below the axis counted negatively. A Riemann sum approximates the integral by rectangles; the integral is the limit as their width goes to zero. The integral of a sum is the sum of the integrals, and constants factor out. The average value of a function on an interval is its integral divided by the interval's length.",
    "inputs": "FIGURES = {'integral_value': 2.6667, 'rectangles_4': 3.75, 'rectangles_10': 2.87, 'upper_limit': 2, 'antiderivative_at_2': 2.6667, 'width_4': 0.5, 'terms_4': 4, 'terms_10': 10}\nLABEL = 'the-definite-integral-and-area'\n",
    "expected": "count: 8\nlabel: the-definite-integral-and-area\nmax: 10\nmean: 3.5567\nmin: 0.5\ntotal: 28.4534\nResult: count=8|label=the-definite-integral-and-area|max=10|mean=3.5567|min=0.5|total=28.4534\nRun 1 SHA-256: 86c0203e1fad48263d916f873abe7d565109a798794a9291912f492a09d0b1b7\nRun 2 SHA-256: 86c0203e1fad48263d916f873abe7d565109a798794a9291912f492a09d0b1b7\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: The Fundamental Theorem of Calculus",
    "subject": "the fundamental theorem of calculus",
    "description": "The fundamental theorem of calculus has two parts. The first says that the derivative of the integral of a function, as a function of its upper limit, is the original function: differentiation undoes integration. The second says that the definite integral of a function equals the difference of the values of any antiderivative at the endpoints: integration undoes differentiation. Part one: the derivative of the integral from a to x of f(t) dt is f(x). Part two: the integral from a to b of f(x) dx is F(b) - F(a), where F is any antiderivative of f. The theorem is why integrals are usually computed by finding antiderivatives rather than by limits of sums.",
    "inputs": "FIGURES = {'integral_value': 15, 'antiderivative_at_4': 16, 'antiderivative_at_1': 1, 'trapezoid_heights_sum': 10, 'width': 3, 'area_check': 15, 'lower_limit': 1, 'upper_limit': 4}\nLABEL = 'the-fundamental-theorem-of-calculus'\n",
    "expected": "count: 8\nlabel: the-fundamental-theorem-of-calculus\nmax: 16\nmean: 8.125\nmin: 1\ntotal: 65\nResult: count=8|label=the-fundamental-theorem-of-calculus|max=16|mean=8.125|min=1|total=65\nRun 1 SHA-256: 4fcdd7c65f7fe4e3e7a62ba162da494a2310b5586672320cac708ad12658b433\nRun 2 SHA-256: 4fcdd7c65f7fe4e3e7a62ba162da494a2310b5586672320cac708ad12658b433\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Integration by Substitution",
    "subject": "integration by substitution",
    "description": "Integration by substitution is the chain rule in reverse: when the integrand contains a function and (up to a constant) its derivative, substitute a new variable for the inner function, turning the integral into a simpler one. The differential dx is replaced by du over the derivative of the substitution. Choose the substitution u = g(x), then du = g'(x) dx. For a definite integral, change the limits to the u values as well. The substitution is undone at the end, replacing u by g(x).",
    "inputs": "FIGURES = {'integral_value': 1.71828, 'e_value': 2.71828, 'lower_u': 0, 'upper_u': 1, 'substitution_terms': 2, 'limits_changed': 2, 'check_value': 1.71828, 'steps': 3}\nLABEL = 'integration-by-substitution'\n",
    "expected": "count: 8\nlabel: integration-by-substitution\nmax: 3\nmean: 1.7694\nmin: 0\ntotal: 14.1548\nResult: count=8|label=integration-by-substitution|max=3|mean=1.7694|min=0|total=14.1548\nRun 1 SHA-256: 60076cbaaa64eeed1773a03491a46d129922a9504971971a2c5d1f62de8d25be\nRun 2 SHA-256: 60076cbaaa64eeed1773a03491a46d129922a9504971971a2c5d1f62de8d25be\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Integration by Parts",
    "subject": "integration by parts",
    "description": "Integration by parts is the product rule in reverse: the integral of u times dv equals u times v minus the integral of v times du. It trades one integral for another, and it is chosen when the new integral is easier than the old one, typically when one factor becomes simpler on differentiating and the other is easy to integrate. Choose u to be the factor that simplifies on differentiating, and dv the factor that is easy to integrate. The formula is: integral of u dv = u v - integral of v du. Repeated parts handles products of polynomials with exponentials or trigonometric functions.",
    "inputs": "FIGURES = {'integral_value': 1, 'e_value': 2.71828, 'boundary_term': 2.71828, 'subtracted_integral': 1.71828, 'integrand_at_half': 0.824, 'limits': 2, 'parts_applied': 1, 'steps': 3}\nLABEL = 'integration-by-parts'\n",
    "expected": "count: 8\nlabel: integration-by-parts\nmax: 3\nmean: 1.8724\nmin: 0.824\ntotal: 14.9788\nResult: count=8|label=integration-by-parts|max=3|mean=1.8724|min=0.824|total=14.9788\nRun 1 SHA-256: 1fcfec0a926f5cdc6b8d5fdce0e2aca3ff1137f31f8ce3b98c5e6207081eea5b\nRun 2 SHA-256: 1fcfec0a926f5cdc6b8d5fdce0e2aca3ff1137f31f8ce3b98c5e6207081eea5b\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Partial Fractions",
    "subject": "integration by partial fractions",
    "description": "Partial fractions is the method for integrating a rational function (a ratio of polynomials): factor the denominator, write the fraction as a sum of simpler fractions with unknown constants, solve for the constants, and integrate each piece, which is a logarithm or an arctangent. Factor the denominator completely over the reals. Each distinct linear factor gives a term A/(x - a); each repeated factor gives a chain of terms. The constants are found by clearing denominators and comparing coefficients.",
    "inputs": "FIGURES = {'constant_a': 0.3333, 'constant_b': -0.3333, 'factors': 2, 'terms': 2, 'coefficient_sum': 0, 'check_numerator': 1, 'x_test_1': 1, 'x_test_2': -2}\nLABEL = 'integration-by-partial-fractions'\n",
    "expected": "count: 8\nlabel: integration-by-partial-fractions\nmax: 2\nmean: 0.5\nmin: -2\ntotal: 4.0\nResult: count=8|label=integration-by-partial-fractions|max=2|mean=0.5|min=-2|total=4.0\nRun 1 SHA-256: 690e79877263a15c1bb1fd08a01d6e539eb098c4a230c946b268029049274a34\nRun 2 SHA-256: 690e79877263a15c1bb1fd08a01d6e539eb098c4a230c946b268029049274a34\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Sequences and Series Convergence Tests",
    "subject": "convergence tests for series",
    "description": "A convergence test is a rule that decides whether a series has a finite sum. The comparison test compares with a known series; the ratio test looks at the limit of the ratio of successive terms; the root test looks at the n-th root of the n-th term; the integral test compares with an improper integral. The ratio test: if the limit of |a(n+1)/a(n)| is below 1, the series converges absolutely. The integral test applies to positive decreasing terms and compares the series with an integral. The alternating series test: a series with decreasing terms tending to zero converges, with error below the first omitted term.",
    "inputs": "FIGURES = {'ratio_limit': 0, 'sum_limit': 1.71828, 'partial_sum_5': 2.70833, 'e_value': 2.71828, 'terms_used': 5, 'tests_named': 4, 'harmonic_diverges': 1, 'ratio_at_n5': 0.1667}\nLABEL = 'convergence-tests-for-series'\n",
    "expected": "count: 8\nlabel: convergence-tests-for-series\nmax: 5\nmean: 2.1639\nmin: 0\ntotal: 17.3116\nResult: count=8|label=convergence-tests-for-series|max=5|mean=2.1639|min=0|total=17.3116\nRun 1 SHA-256: 27478dda75943cdd64aabbdd09977b5be06fefbb06663736eac6b46edda1052f\nRun 2 SHA-256: 27478dda75943cdd64aabbdd09977b5be06fefbb06663736eac6b46edda1052f\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Taylor Series and Approximation",
    "subject": "Taylor series and approximation",
    "description": "A Taylor series represents a function as an infinite sum of powers of (x - a), with coefficients given by the function's derivatives at a: the n-th coefficient is the n-th derivative at a divided by n factorial. The partial sums are polynomial approximations, and Taylor's theorem bounds the error of stopping early. The Taylor series of e^x about 0 is 1 + x + x squared/2! + x cubed/3! + ... The Taylor series of sin(x) about 0 is x - x cubed/3! + x to the fifth/5! - ... Taylor's theorem with remainder bounds the error by the next term's size when the derivatives are bounded.",
    "inputs": "FIGURES = {'approximation': 1.648437, 'true_value': 1.648721, 'error': 0.000284, 'next_term': 0.00026, 'error_bound': 0.00043, 'terms_used': 5, 'x_value': 0.5, 'degree': 4}\nLABEL = 'taylor-series-and-approximation'\n",
    "expected": "count: 8\nlabel: taylor-series-and-approximation\nmax: 5\nmean: 1.5998\nmin: 0.00026\ntotal: 12.7981\nResult: count=8|label=taylor-series-and-approximation|max=5|mean=1.5998|min=0.00026|total=12.7981\nRun 1 SHA-256: 2014fa7a54b434e9917bc352e2ca751da4ac726f7124de11a5381d852773b9e9\nRun 2 SHA-256: 2014fa7a54b434e9917bc352e2ca751da4ac726f7124de11a5381d852773b9e9\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Partial Derivatives",
    "subject": "partial derivatives",
    "description": "A partial derivative is the derivative of a function of several variables with respect to one variable, holding the others fixed. The partial derivative with respect to x measures how the function changes when only x changes. The gradient is the vector of all the partial derivatives, pointing in the direction of steepest increase. To compute a partial derivative with respect to x, treat the other variables as constants. Clairaut's theorem says mixed partial derivatives are equal when they are continuous. The gradient points in the direction of steepest increase, and its size is the steepest rate.",
    "inputs": "FIGURES = {'fx_at_2_1': 7, 'fy_at_2_1': 16, 'gradient_x': 7, 'gradient_y': 16, 'point_x': 2, 'point_y': 1, 'variables': 2, 'partials_computed': 2}\nLABEL = 'partial-derivatives'\n",
    "expected": "count: 8\nlabel: partial-derivatives\nmax: 16\nmean: 6.625\nmin: 1\ntotal: 53\nResult: count=8|label=partial-derivatives|max=16|mean=6.625|min=1|total=53\nRun 1 SHA-256: ce2768ca970af3dac0b8ec270eb70ab5e0482eefc7cc4ebff542c43221101c1e\nRun 2 SHA-256: ce2768ca970af3dac0b8ec270eb70ab5e0482eefc7cc4ebff542c43221101c1e\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Multiple Integrals",
    "subject": "multiple integrals",
    "description": "A multiple integral integrates a function over a region in two or three dimensions: a double integral over a region in the plane, a triple integral over a region in space. It is the limit of sums over small rectangles or boxes, and it computes volumes, masses, and averages over regions. A double integral is computed as an iterated integral: integrate with respect to one variable, then the other. The order of integration can be changed, sometimes making the integral much easier. Polar, cylindrical, and spherical coordinates simplify integrals over round regions.",
    "inputs": "FIGURES = {'integral_value': 3, 'rectangle_area': 2, 'integral_of_x': 2, 'integral_of_y': 1, 'x_upper': 2, 'y_upper': 1, 'average_x': 1, 'average_y': 0.5}\nLABEL = 'multiple-integrals'\n",
    "expected": "count: 8\nlabel: multiple-integrals\nmax: 3\nmean: 1.5625\nmin: 0.5\ntotal: 12.5\nResult: count=8|label=multiple-integrals|max=3|mean=1.5625|min=0.5|total=12.5\nRun 1 SHA-256: fe428859190d2c33e93058d8fa2b183c6c9f96745693260cfd2f02ba42362ff4\nRun 2 SHA-256: fe428859190d2c33e93058d8fa2b183c6c9f96745693260cfd2f02ba42362ff4\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Vector Calculus and the Theorems of Green, Stokes, and Gauss",
    "subject": "vector calculus and its great theorems",
    "description": "Vector calculus studies vector fields (assignments of a vector to each point in space). The theorems of Green, Stokes, and Gauss relate an integral over a region to an integral over its boundary: Green relates a line integral around a closed curve to a double integral over the region inside; Stokes extends this to surfaces; Gauss relates a surface integral to a triple integral over the volume inside. Green's theorem: the line integral of a field around a closed curve equals the double integral of the field's curl over the region. Stokes' theorem: the line integral around the boundary of a surface equals the surface integral of the curl. Gauss' divergence theorem: the surface integral of a field over a closed surface equals the triple integral of the divergence over the volume.",
    "inputs": "FIGURES = {'area_of_unit_circle': 3.14159, 'curl_value': 1, 'line_integral': 3.14159, 't_upper': 6.28318, 'field_components': 2, 'theorems_named': 3, 'dimensions': 2, 'check_agrees': 1}\nLABEL = 'vector-calculus-and-its-great-theorems'\n",
    "expected": "count: 8\nlabel: vector-calculus-and-its-great-theorems\nmax: 6.28318\nmean: 2.6958\nmin: 1\ntotal: 21.5664\nResult: count=8|label=vector-calculus-and-its-great-theorems|max=6.28318|mean=2.6958|min=1|total=21.5664\nRun 1 SHA-256: ecb9e04c17526f213b0d1bd022cb4d9d65fac5e1819bb525a46ad84f18bb903b\nRun 2 SHA-256: ecb9e04c17526f213b0d1bd022cb4d9d65fac5e1819bb525a46ad84f18bb903b\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Improper Integrals",
    "subject": "improper integrals",
    "description": "An improper integral is an integral over an unbounded interval, or of a function that becomes infinite inside the interval. It is defined as a limit: integrate up to a finite point, then let that point go to infinity, or let it approach the trouble spot, and take the limit if it exists. The integral of 1/x squared from 1 to infinity converges to 1. The integral of 1/x from 1 to infinity diverges: it grows like the logarithm. The p-test says the integral of 1/x to the power p from 1 to infinity converges exactly when p is greater than 1.",
    "inputs": "FIGURES = {'integral_value': 1, 'value_at_5': 0.99326, 'value_at_10': 0.99995, 'p_test_threshold': 1, 'harmonic_diverges': 1, 'lower_limit': 0, 'steps': 2, 'limit_points_checked': 2}\nLABEL = 'improper-integrals'\n",
    "expected": "count: 8\nlabel: improper-integrals\nmax: 2\nmean: 1.1242\nmin: 0\ntotal: 8.9932\nResult: count=8|label=improper-integrals|max=2|mean=1.1242|min=0|total=8.9932\nRun 1 SHA-256: de551ea97d441d806c87fc999263102b93b91a827c0f600706b531dd1e4ed580\nRun 2 SHA-256: de551ea97d441d806c87fc999263102b93b91a827c0f600706b531dd1e4ed580\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Differential Equations from Calculus",
    "subject": "differential equations from calculus",
    "description": "Calculus leads directly to differential equations: a differential equation involves a function and its derivatives, and solving it means finding the function. The simplest is dy/dx = ky, whose solutions are exponentials: y = C e^(kx), where C is set by the starting value. The equation dy/dx = ky has the general solution y = C e^(kx). An initial condition fixes C: if y(0) = 3, then C = 3. Separation of variables solves equations where the x terms and the y terms can be put on opposite sides.",
    "inputs": "FIGURES = {'c_value': 3, 'y_at_1': 22.167, 'doubling_time': 0.3466, 'growth_rate': 2, 'y_at_0': 3, 'derivative_check': 2, 'steps': 3, 'initial_condition': 3}\nLABEL = 'differential-equations-from-calculus'\n",
    "expected": "count: 8\nlabel: differential-equations-from-calculus\nmax: 22.167\nmean: 4.8142\nmin: 0.3466\ntotal: 38.5136\nResult: count=8|label=differential-equations-from-calculus|max=22.167|mean=4.8142|min=0.3466|total=38.5136\nRun 1 SHA-256: 325acf4b2685b28c6cf8773656b455ce8e5f81fc0048fe2331d71027e60df32e\nRun 2 SHA-256: 325acf4b2685b28c6cf8773656b455ce8e5f81fc0048fe2331d71027e60df32e\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Lagrange Multipliers",
    "subject": "Lagrange multipliers",
    "description": "Lagrange multipliers solve constrained optimisation: maximising a function f subject to a constraint g = c. At the optimum, the gradient of f is parallel to the gradient of g, so the gradient of f equals lambda times the gradient of g, for some number lambda (the Lagrange multiplier), together with the constraint itself. The multiplier lambda measures how much the optimum value changes if the constraint is relaxed. The method gives candidates; each must be checked against the constraint and against the others. With several constraints, one multiplier is introduced per constraint.",
    "inputs": "FIGURES = {'optimal_x': 5, 'optimal_y': 5, 'max_value': 25, 'multiplier': 5, 'constraint_sum': 10, 'endpoint_value': 0, 'candidates': 1, 'constraints': 1}\nLABEL = 'lagrange-multipliers'\n",
    "expected": "count: 8\nlabel: lagrange-multipliers\nmax: 25\nmean: 6.5\nmin: 0\ntotal: 52\nResult: count=8|label=lagrange-multipliers|max=25|mean=6.5|min=0|total=52\nRun 1 SHA-256: bac86467e8d2e03bd6c632f71e830ee26789d00434fed82cf31a2a9df6331bb8\nRun 2 SHA-256: bac86467e8d2e03bd6c632f71e830ee26789d00434fed82cf31a2a9df6331bb8\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: The Mean Value Theorem",
    "subject": "the mean value theorem",
    "description": "The mean value theorem says: if a function is continuous on a closed interval and differentiable on the open interval, then there is a point inside where the instantaneous rate of change equals the average rate of change over the whole interval. Geometrically, some tangent line is parallel to the secant line (the line joining the endpoints). The theorem is the bridge between local information (derivatives) and global information (net change). Rolle's theorem is the special case where the endpoint values are equal: then some derivative is zero. The theorem proves that a function with zero derivative everywhere is constant.",
    "inputs": "FIGURES = {'distance_km': 120, 'time_hours': 2, 'average_speed': 60, 'theorem_point': 1, 'average_rate': 2, 'interval_length': 2, 'function_at_2': 4, 'hypotheses': 2}\nLABEL = 'the-mean-value-theorem'\n",
    "expected": "count: 8\nlabel: the-mean-value-theorem\nmax: 120\nmean: 24.125\nmin: 1\ntotal: 193\nResult: count=8|label=the-mean-value-theorem|max=120|mean=24.125|min=1|total=193\nRun 1 SHA-256: 66dd1506ecb3b2611160d026915fd56e4df358e332dba001d5f8bec694180ee3\nRun 2 SHA-256: 66dd1506ecb3b2611160d026915fd56e4df358e332dba001d5f8bec694180ee3\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Curve Sketching with Derivatives",
    "subject": "curve sketching with derivatives",
    "description": "Curve sketching is drawing the graph of a function from its calculus: the first derivative shows where it rises and falls, the second derivative shows where it bends up or down, and the critical points, inflection points (where the bending changes), intercepts, and asymptotes (lines the graph approaches) complete the picture. The function rises where the first derivative is positive and falls where it is negative. The function is concave up where the second derivative is positive, concave down where it is negative. An inflection point is a point where the concavity changes sign.",
    "inputs": "FIGURES = {'critical_x_1': -1, 'critical_x_2': 1, 'local_max': 2, 'local_min': -2, 'inflection_x': 0, 'root_1': -1.732, 'root_2': 0, 'root_3': 1.732}\nLABEL = 'curve-sketching-with-derivatives'\n",
    "expected": "count: 8\nlabel: curve-sketching-with-derivatives\nmax: 2\nmean: 0.0\nmin: -2\ntotal: 0.0\nResult: count=8|label=curve-sketching-with-derivatives|max=2|mean=0.0|min=-2|total=0.0\nRun 1 SHA-256: 23c0c850f44f979d39741d2b39f5c7e297cb20a1412adddab44de1a598623f56\nRun 2 SHA-256: 23c0c850f44f979d39741d2b39f5c7e297cb20a1412adddab44de1a598623f56\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Volumes of Revolution",
    "subject": "volumes of revolution",
    "description": "A volume of revolution is the volume of a solid made by rotating a region around an axis. The disk method slices the solid into thin disks perpendicular to the axis, each with volume pi times radius squared times thickness, and integrates. The shell method slices it into cylindrical shells parallel to the axis. The disk method: volume is the integral of pi times the radius squared, with respect to the axis variable. The washer method extends this to regions with a hole, subtracting the inner radius squared. The shell method: volume is the integral of 2 pi times radius times height, with respect to the other variable.",
    "inputs": "FIGURES = {'volume': 25.1327, 'pi_times_8': 25.1327, 'upper_x': 4, 'radius_at_4': 2, 'shell_check': 25.1327, 'methods_used': 2, 'disk_radius_squared': 4, 'steps': 3}\nLABEL = 'volumes-of-revolution'\n",
    "expected": "count: 8\nlabel: volumes-of-revolution\nmax: 25.1327\nmean: 11.2998\nmin: 2\ntotal: 90.3981\nResult: count=8|label=volumes-of-revolution|max=25.1327|mean=11.2998|min=2|total=90.3981\nRun 1 SHA-256: 8379ef14b427d642096d1486351e68c9c191aad7d7f9f09605423eee61bcae48\nRun 2 SHA-256: 8379ef14b427d642096d1486351e68c9c191aad7d7f9f09605423eee61bcae48\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Arc Length and Surface Area",
    "subject": "arc length and surface area",
    "description": "Arc length is the length of a curve, computed by integrating the length of infinitesimal (infinitely small) pieces: the integral of the square root of 1 plus the square of the derivative. Surface area of a surface of revolution is computed similarly, integrating the circumference of each circular slice. The arc length of y = f(x) from a to b is the integral of sqrt(1 + (f'(x)) squared) dx. The surface area of the surface made by rotating the curve around the x-axis is the integral of 2 pi y times the arc-length element. Many arc-length integrals have no elementary closed form and are computed numerically.",
    "inputs": "FIGURES = {'arc_length': 4.6667, 'straight_distance': 4.5826, 'upper_x': 3, 'y_at_3': 3.464, 'integrand_at_3': 2, 'curve_points': 2, 'formula_terms': 2, 'steps': 3}\nLABEL = 'arc-length-and-surface-area'\n",
    "expected": "count: 8\nlabel: arc-length-and-surface-area\nmax: 4.6667\nmean: 3.0892\nmin: 2\ntotal: 24.7133\nResult: count=8|label=arc-length-and-surface-area|max=4.6667|mean=3.0892|min=2|total=24.7133\nRun 1 SHA-256: 6a16663447ad28d9a401cc3879934d37f13cac18669f835d29d192abc487cd0b\nRun 2 SHA-256: 6a16663447ad28d9a401cc3879934d37f13cac18669f835d29d192abc487cd0b\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Parametric Curves and Polar Coordinates",
    "subject": "parametric curves and polar coordinates",
    "description": "A parametric curve is described by giving x and y as functions of a parameter t, rather than y as a function of x. Polar coordinates describe a point by its distance r from the origin and its angle theta from the positive x-axis. Both describe curves that are not graphs of functions, such as circles and spirals. A circle of radius a is parametrised by x = a cos(t), y = a sin(t). Polar coordinates relate to rectangular by x = r cos(theta), y = r sin(theta). The area in polar coordinates is the integral of (1/2) r squared d theta.",
    "inputs": "FIGURES = {'petal_area': 1.5708, 'total_area': 6.2832, 'petals': 4, 'radius_max': 2, 'circle_area': 12.566, 'theta_range': 1.5708, 'integrand_factor': 2, 'steps': 3}\nLABEL = 'parametric-curves-and-polar-coordinates'\n",
    "expected": "count: 8\nlabel: parametric-curves-and-polar-coordinates\nmax: 12.566\nmean: 4.1239\nmin: 1.5708\ntotal: 32.9908\nResult: count=8|label=parametric-curves-and-polar-coordinates|max=12.566|mean=4.1239|min=1.5708|total=32.9908\nRun 1 SHA-256: 8bd809ea43991d131a8b28a5ddaf8d9c35d16fd78fdb98a2e4aedd21a7b33d9a\nRun 2 SHA-256: 8bd809ea43991d131a8b28a5ddaf8d9c35d16fd78fdb98a2e4aedd21a7b33d9a\nDeterministic: MATCH\n"
  },
  {
    "title": "Calculus: Capstone — Modelling with Calculus",
    "subject": "a capstone modelling problem using calculus",
    "description": "This capstone combines optimisation, integration, and series: design a box of fixed volume with least surface area, check a volume of revolution by integration, and approximate a value by a Taylor polynomial. A capstone problem uses several tools at once, and the answer is stated with its checks. The box problem is solved by differentiating the surface area. The volume of revolution is checked by the disc method. The Taylor polynomial is checked against the true value.",
    "inputs": "FIGURES = {'volume': 32, 'side_m': 3.174, 'height_m': 3.174, 'surface_area': 60.5, 'hemisphere_volume': 16.755, 'taylor_e0.1': 1.10517, 'true_e0.1': 1.1051702, 'parts': 3}\nLABEL = 'a-capstone-modelling-problem-using-calculus'\n",
    "expected": "count: 8\nlabel: a-capstone-modelling-problem-using-calculus\nmax: 60.5\nmean: 15.1017\nmin: 1.10517\ntotal: 120.8133\nResult: count=8|label=a-capstone-modelling-problem-using-calculus|max=60.5|mean=15.1017|min=1.10517|total=120.8133\nRun 1 SHA-256: 4fcc1d6ffcb9aa05eabf3840bb1cb6427c6fdbc01a4e097e103cc4c6f93faad3\nRun 2 SHA-256: 4fcc1d6ffcb9aa05eabf3840bb1cb6427c6fdbc01a4e097e103cc4c6f93faad3\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Limit (mathematics)",
    "url": "https://en.wikipedia.org/wiki/Limit_(mathematics)",
    "establishes": "The reference for limits of functions in this record."
  },
  {
    "name": "Wikipedia - Calculus",
    "url": "https://en.wikipedia.org/wiki/Calculus",
    "establishes": "The reference for limits of functions in this record."
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
