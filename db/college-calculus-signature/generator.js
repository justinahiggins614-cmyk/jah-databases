// Seeded boundless generator for the The Signature Calculus I-III Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-college-calculus-signature.js [seed]  (prints one JSON record)
// or: node gen-college-calculus-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "college-calculus-signature";
const RECORD_KIND = "calculus record";
const ID_PREFIX = "JAH-CCALCS-";
const AI_NAME = "JAH Calculus Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Limit Microscope",
    "subject": "a Signature limit microscope design",
    "description": "The Limit Microscope is a Signature-made design for teaching limits: a microscope that zooms into a function's graph near a point, showing the values approaching the limit from both sides as the zoom deepens. A limit is the value a function approaches as its input approaches a given number. The microscope zooms in steps of 10, showing the function values at each scale. Left and right approaches are shown in different colours, and must agree. A jump or an oscillation is flagged when the two sides disagree or never settle.",
    "inputs": "FIGURES = {'zoom_levels': 3, 'values_checked': 6, 'limit_value': 2, 'value_at_0.1_left': 1.9, 'value_at_0.1_right': 2.1, 'value_at_0.001': 1.999, 'jump_flagged': 1, 'design_version': 1}\nLABEL = 'a-signature-limit-microscope-design'\n",
    "expected": "count: 8\nlabel: a-signature-limit-microscope-design\nmax: 6\nmean: 2.3749\nmin: 1\ntotal: 18.999\nResult: count=8|label=a-signature-limit-microscope-design|max=6|mean=2.3749|min=1|total=18.999\nRun 1 SHA-256: a43c37c4fcb69d2b1bfae31373909792f1ae782cb0a1aa63b08bdfaa58696b2c\nRun 2 SHA-256: a43c37c4fcb69d2b1bfae31373909792f1ae782cb0a1aa63b08bdfaa58696b2c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Tangent Line Tracer",
    "subject": "a Signature tangent line tracer design",
    "description": "The Tangent Line Tracer is a Signature-made design for teaching the derivative: a tool where a learner drags a secant line (a line through two points of the graph) until the two points merge, and watches the secant become the tangent line whose slope is the derivative. The derivative is the instantaneous rate of change. Dragging the second point toward the first shows the secant slope approaching the derivative. The tangent line is drawn at the merged point with its slope displayed. A corner is flagged: the secants from the left and the right approach different slopes.",
    "inputs": "FIGURES = {'secants_shown': 3, 'slope_at_2.1': 4.1, 'slope_at_2.01': 4.01, 'slope_at_2.001': 4.001, 'derivative_at_2': 4, 'derivative_at_0': 0, 'tangents_drawn': 1, 'design_version': 1}\nLABEL = 'a-signature-tangent-line-tracer-design'\n",
    "expected": "count: 8\nlabel: a-signature-tangent-line-tracer-design\nmax: 4.1\nmean: 2.6389\nmin: 0\ntotal: 21.111\nResult: count=8|label=a-signature-tangent-line-tracer-design|max=4.1|mean=2.6389|min=0|total=21.111\nRun 1 SHA-256: 30901c8d0c5b55ce51b57e178e975b93bf2dbb6033af8a910d49d2c193245535\nRun 2 SHA-256: 30901c8d0c5b55ce51b57e178e975b93bf2dbb6033af8a910d49d2c193245535\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Rule Machine",
    "subject": "a Signature differentiation rule machine design",
    "description": "The Rule Machine is a Signature-made design for teaching the product, quotient, and chain rules: a machine where a learner feeds in a function built from parts, and the machine shows which rule applies at each step and differentiates one step at a time. The product rule, quotient rule, and chain rule are the working tools of differentiation. The machine parses the function into its parts and names the outermost rule. Each step shows the rule used and the result, so the chain of steps is auditable. A wrong rule choice is corrected with the reason why it does not apply.",
    "inputs": "FIGURES = {'steps': 2, 'rules_used': 1, 'derivative_at_1': 24, 'numerical_check': 24, 'functions_differentiated': 1, 'corrections_offered': 1, 'rules_named': 3, 'design_version': 1}\nLABEL = 'a-signature-differentiation-rule-machine-design'\n",
    "expected": "count: 8\nlabel: a-signature-differentiation-rule-machine-design\nmax: 24\nmean: 7.125\nmin: 1\ntotal: 57\nResult: count=8|label=a-signature-differentiation-rule-machine-design|max=24|mean=7.125|min=1|total=57\nRun 1 SHA-256: c1533bbc1b6791ad0ea750fdbeb376980c2f531582419bf9ae43c23fe467f266\nRun 2 SHA-256: c1533bbc1b6791ad0ea750fdbeb376980c2f531582419bf9ae43c23fe467f266\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Optimisation Workbench",
    "subject": "a Signature optimisation workbench design",
    "description": "The Optimisation Workbench is a Signature-made design for teaching optimisation: a bench where a learner states a quantity to maximise or minimise and its constraints, and the bench draws the function, marks the critical points (where the derivative is zero or does not exist), and tests each candidate including the endpoints. A maximum or minimum occurs at a critical point or an endpoint. The bench draws the function and marks every critical point. Each candidate is tested by the first or second derivative test. Endpoints are always listed as candidates, so a boundary maximum is never missed.",
    "inputs": "FIGURES = {'perimeter': 40, 'optimal_side': 10, 'max_area': 100, 'critical_points': 1, 'endpoints': 2, 'second_derivative': -2, 'candidates_tested': 3, 'design_version': 1}\nLABEL = 'a-signature-optimisation-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-optimisation-workbench-design\nmax: 100\nmean: 19.375\nmin: -2\ntotal: 155\nResult: count=8|label=a-signature-optimisation-workbench-design|max=100|mean=19.375|min=-2|total=155\nRun 1 SHA-256: 1db94f8ff199fe490bfb9538c088b4c07bbc1ad9c89c03311b909692b5a30116\nRun 2 SHA-256: 1db94f8ff199fe490bfb9538c088b4c07bbc1ad9c89c03311b909692b5a30116\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Related Rates Simulator",
    "subject": "a Signature related rates simulator design",
    "description": "The Related Rates Simulator is a Signature-made design for teaching related rates: a simulation where a learner watches two quantities change together (a ladder sliding, a tank filling), sees the relation between them, and reads the linked rates at any instant. Related rates link the rates of two quantities through a relation between them. The simulation animates the situation and shows both quantities and both rates. The relation is displayed and differentiated step by step. The learner can pause at any instant and read the exact rates.",
    "inputs": "FIGURES = {'ladder': 5, 'pause_1_foot': 3, 'pause_1_top': 4, 'pause_1_rate': 0.375, 'pause_2_foot': 4, 'pause_2_top': 3, 'pause_2_rate': 0.6667, 'foot_speed': 0.5}\nLABEL = 'a-signature-related-rates-simulator-design'\n",
    "expected": "count: 8\nlabel: a-signature-related-rates-simulator-design\nmax: 5\nmean: 2.5677\nmin: 0.375\ntotal: 20.5417\nResult: count=8|label=a-signature-related-rates-simulator-design|max=5|mean=2.5677|min=0.375|total=20.5417\nRun 1 SHA-256: ef7027b9caa7f15aac440a598931eaa0c628711d53065bbb2b61015472972164\nRun 2 SHA-256: ef7027b9caa7f15aac440a598931eaa0c628711d53065bbb2b61015472972164\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Riemann Sum Builder",
    "subject": "a Signature Riemann sum builder design",
    "description": "The Riemann Sum Builder is a Signature-made design for teaching the definite integral: a tool where a learner chooses the number of rectangles under a graph, watches the sum approach the integral as the rectangles get thinner, and sees the error shrink. The definite integral is the limit of Riemann sums (sums of thin rectangle areas). The builder draws the rectangles and shows the sum for any chosen count. Left, right, and midpoint rules are offered and compared. The error is shown against the exact integral where it is known.",
    "inputs": "FIGURES = {'exact_integral': 2.6667, 'sum_4': 3.75, 'sum_10': 2.87, 'sum_100': 2.6867, 'error_4': 1.0833, 'error_10': 0.2033, 'error_100': 0.02, 'rules_offered': 3}\nLABEL = 'a-signature-riemann-sum-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-riemann-sum-builder-design\nmax: 3.75\nmean: 2.035\nmin: 0.02\ntotal: 16.28\nResult: count=8|label=a-signature-riemann-sum-builder-design|max=3.75|mean=2.035|min=0.02|total=16.28\nRun 1 SHA-256: 6034c26be0641fc5cfb28110ec0a03a7e27fe1e174be719783be05c4f0bbdd21\nRun 2 SHA-256: 6034c26be0641fc5cfb28110ec0a03a7e27fe1e174be719783be05c4f0bbdd21\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Antiderivative Finder",
    "subject": "a Signature antiderivative finder design",
    "description": "The Antiderivative Finder is a Signature-made design for teaching the fundamental theorem: a tool where a learner enters a function, the tool proposes an antiderivative, and the learner verifies it by differentiating, which is how the fundamental theorem turns integrals into evaluations. An antiderivative of f is a function whose derivative is f. The finder proposes an antiderivative from a table of standard forms. Verification is by differentiating the proposal and comparing with the original. The definite integral is then computed as the difference of endpoint values.",
    "inputs": "FIGURES = {'functions_tested': 2, 'verifications': 2, 'integral_1': 15, 'integral_2': 1, 'endpoint_values_1': 16, 'endpoint_values_2': 1, 'table_entries': 20, 'design_version': 1}\nLABEL = 'a-signature-antiderivative-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-antiderivative-finder-design\nmax: 20\nmean: 7.25\nmin: 1\ntotal: 58\nResult: count=8|label=a-signature-antiderivative-finder-design|max=20|mean=7.25|min=1|total=58\nRun 1 SHA-256: 7082c8cb0b1196e368e4161b6c1e6afd7b6799c266d4ce10f50bc978851dfde3\nRun 2 SHA-256: 7082c8cb0b1196e368e4161b6c1e6afd7b6799c266d4ce10f50bc978851dfde3\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Substitution Workbench",
    "subject": "a Signature substitution workbench design",
    "description": "The Substitution Workbench is a Signature-made design for teaching integration by substitution: a bench where a learner picks the inner function, watches the substitution rewrite the integral, and sees the limits change for a definite integral. Substitution is the chain rule in reverse. The bench highlights the inner function and its derivative in the integrand. Choosing the substitution rewrites the integral in the new variable. For a definite integral, the limits are changed and shown alongside.",
    "inputs": "FIGURES = {'integral_value': 1.71828, 'limits_changed': 2, 'substitutions': 1, 'steps': 3, 'lower_limit': 0, 'upper_limit': 1, 'e_value': 2.71828, 'design_version': 1}\nLABEL = 'a-signature-substitution-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-substitution-workbench-design\nmax: 3\nmean: 1.5546\nmin: 0\ntotal: 12.4366\nResult: count=8|label=a-signature-substitution-workbench-design|max=3|mean=1.5546|min=0|total=12.4366\nRun 1 SHA-256: e3792929632e0f3bd867c476baa825ff04551b4ec74ff8c0abcf28f32e6056ba\nRun 2 SHA-256: e3792929632e0f3bd867c476baa825ff04551b4ec74ff8c0abcf28f32e6056ba\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Parts Workbench",
    "subject": "a Signature integration by parts workbench design",
    "description": "The Parts Workbench is a Signature-made design for teaching integration by parts: a bench where a learner chooses which factor to differentiate and which to integrate, and the bench shows the trade and the resulting integral. Integration by parts is the product rule in reverse. The bench lists the two choices of u and dv and shows the resulting integral for each. A bad choice is flagged when the new integral is harder than the old one. Repeated parts is supported, with the original integral reappearing and being solved for.",
    "inputs": "FIGURES = {'integral_value': 1, 'choices_tried': 2, 'choices_flagged': 1, 'boundary_term': 2.71828, 'subtracted': 1.71828, 'parts_applied': 1, 'steps': 3, 'design_version': 1}\nLABEL = 'a-signature-integration-by-parts-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-integration-by-parts-workbench-design\nmax: 3\nmean: 1.6796\nmin: 1\ntotal: 13.4366\nResult: count=8|label=a-signature-integration-by-parts-workbench-design|max=3|mean=1.6796|min=1|total=13.4366\nRun 1 SHA-256: 6a3626e742c991d0826068bd4c25345795b7f953a250c2a68ab9698d62fec6d2\nRun 2 SHA-256: 6a3626e742c991d0826068bd4c25345795b7f953a250c2a68ab9698d62fec6d2\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Series Convergence Lab",
    "subject": "a Signature series convergence laboratory design",
    "description": "The Series Convergence Lab is a Signature-made design for teaching convergence tests: a laboratory where a learner enters a series, the lab applies the ratio, root, comparison, and integral tests in turn, and reports which test decides and which is inconclusive. A convergence test decides whether a series has a finite sum. The lab lists the terms, the ratio of successive terms, and the limit of that ratio. Each test reports converges, diverges, or inconclusive, with the reason. The partial sums are plotted so the behaviour can be seen.",
    "inputs": "FIGURES = {'ratio_limit': 0, 'partial_sum_5': 2.70833, 'e_value': 2.71828, 'tests_applied': 4, 'series_tested': 2, 'inconclusive_count': 1, 'terms_shown': 5, 'design_version': 1}\nLABEL = 'a-signature-series-convergence-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-series-convergence-laboratory-design\nmax: 5\nmean: 2.3033\nmin: 0\ntotal: 18.4266\nResult: count=8|label=a-signature-series-convergence-laboratory-design|max=5|mean=2.3033|min=0|total=18.4266\nRun 1 SHA-256: 66c282d4c57e475c796747a36454c86fff892d98d57a2e0bc212ad198021b775\nRun 2 SHA-256: 66c282d4c57e475c796747a36454c86fff892d98d57a2e0bc212ad198021b775\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Taylor Approximator",
    "subject": "a Signature Taylor approximator design",
    "description": "The Taylor Approximator is a Signature-made design for teaching Taylor series: a tool where a learner chooses a function and a degree, sees the polynomial approximation drawn against the function, and reads the error and its bound. A Taylor series represents a function as a sum of powers with coefficients from its derivatives. The tool draws the function and the approximating polynomial together. Increasing the degree shows the approximation improving near the centre. The error and the remainder bound are shown for the chosen point.",
    "inputs": "FIGURES = {'degree_4_value': 1.648437, 'true_value': 1.648721, 'error_4': 0.000284, 'bound_4': 0.00043, 'degree_6_value': 1.648721, 'degrees_tried': 2, 'x_value': 0.5, 'design_version': 1}\nLABEL = 'a-signature-taylor-approximator-design'\n",
    "expected": "count: 8\nlabel: a-signature-taylor-approximator-design\nmax: 2\nmean: 1.0558\nmin: 0.000284\ntotal: 8.4466\nResult: count=8|label=a-signature-taylor-approximator-design|max=2|mean=1.0558|min=0.000284|total=8.4466\nRun 1 SHA-256: 9ed43363d734cd57729b85c1e0c11a96be83fa2b045109a5d963bb9fae21597d\nRun 2 SHA-256: 9ed43363d734cd57729b85c1e0c11a96be83fa2b045109a5d963bb9fae21597d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Multivariable Explorer",
    "subject": "a Signature multivariable explorer design",
    "description": "The Multivariable Explorer is a Signature-made design for teaching functions of several variables: a 3D surface a learner can rotate, with a point whose partial derivatives are shown as the slopes along the two axis directions, and the gradient shown as an arrow pointing uphill. A partial derivative measures change in one variable while the others are held fixed. Rotating the surface shows its shape from any angle. At the chosen point, the two partial derivatives are shown as slopes along the axes. The gradient arrow points in the direction of steepest increase.",
    "inputs": "FIGURES = {'fx_at_1_2': 2, 'fy_at_1_2': 4, 'height_at_1_2': 5, 'gradient_length': 4.4721, 'fx_at_0_0': 0, 'fy_at_0_0': 0, 'points_shown': 2, 'design_version': 1}\nLABEL = 'a-signature-multivariable-explorer-design'\n",
    "expected": "count: 8\nlabel: a-signature-multivariable-explorer-design\nmax: 5\nmean: 2.309\nmin: 0\ntotal: 18.4721\nResult: count=8|label=a-signature-multivariable-explorer-design|max=5|mean=2.309|min=0|total=18.4721\nRun 1 SHA-256: de59ac207559007724a6499af8320cb94fe44d8c67f4ceb9159924254e7fba6f\nRun 2 SHA-256: de59ac207559007724a6499af8320cb94fe44d8c67f4ceb9159924254e7fba6f\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Volume Builder",
    "subject": "a Signature volume builder design",
    "description": "The Volume Builder is a Signature-made design for teaching multiple integrals: a tool where a learner defines a region, chooses the order of integration, and watches the iterated integral build the volume slice by slice. A double integral over a region is computed as an iterated integral. The region is drawn, and the learner chooses the order of integration. The inner integral is shown as a slice, and the outer integral stacks the slices. Changing the order redraws the slices and must give the same volume.",
    "inputs": "FIGURES = {'volume': 3, 'orders_tried': 2, 'rectangle_area': 2, 'inner_result_at_2': 2.5, 'integral_of_x': 2, 'integral_of_y': 1, 'slices_shown': 10, 'design_version': 1}\nLABEL = 'a-signature-volume-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-volume-builder-design\nmax: 10\nmean: 2.9375\nmin: 1\ntotal: 23.5\nResult: count=8|label=a-signature-volume-builder-design|max=10|mean=2.9375|min=1|total=23.5\nRun 1 SHA-256: bde55160c15042386a97d851fddcc7cb7d7481a58b60af9beb60e60ee1d6dfc9\nRun 2 SHA-256: bde55160c15042386a97d851fddcc7cb7d7481a58b60af9beb60e60ee1d6dfc9\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Vector Field Studio",
    "subject": "a Signature vector field studio design",
    "description": "The Vector Field Studio is a Signature-made design for teaching vector calculus: a studio where a learner draws a vector field, sees its arrows, and computes its line integral along a curve, with Green's theorem shown as the link between the boundary integral and the interior. A vector field assigns a vector to each point. The studio draws the field as arrows on a grid. A curve is drawn, and the line integral along it is computed and shown. Green's theorem is displayed: the boundary integral equals the interior integral of the curl.",
    "inputs": "FIGURES = {'line_integral': 3.14159, 'area': 3.14159, 'curl': 1, 'arrows_drawn': 25, 'curve_points': 100, 'theorems_shown': 3, 'fields_drawn': 1, 'design_version': 1}\nLABEL = 'a-signature-vector-field-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-vector-field-studio-design\nmax: 100\nmean: 17.1604\nmin: 1\ntotal: 137.2832\nResult: count=8|label=a-signature-vector-field-studio-design|max=100|mean=17.1604|min=1|total=137.2832\nRun 1 SHA-256: d20723007cf0a063b80a661cb844477d507363efc247c03225f9fda53ca8fa1e\nRun 2 SHA-256: d20723007cf0a063b80a661cb844477d507363efc247c03225f9fda53ca8fa1e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Improper Integral Tester",
    "subject": "a Signature improper integral tester design",
    "description": "The Improper Integral Tester is a Signature-made design for teaching improper integrals: a tool where a learner enters an integral over an infinite interval, watches the finite cut-off move outward, and sees the values approach the limit or grow without bound. An improper integral is defined as a limit. The tool integrates up to a cut-off b and shows the value as b grows. Convergent integrals settle; divergent ones keep growing, and the tool flags them. The p-test is shown alongside for integrals of 1/x to the power p.",
    "inputs": "FIGURES = {'value_at_1': 0.63212, 'value_at_5': 0.99326, 'value_at_10': 0.99995, 'limit_value': 1, 'divergent_at_e2': 2.30259, 'divergent_at_e4': 4.60517, 'cutoffs_shown': 3, 'design_version': 1}\nLABEL = 'a-signature-improper-integral-tester-design'\n",
    "expected": "count: 8\nlabel: a-signature-improper-integral-tester-design\nmax: 4.60517\nmean: 1.8166\nmin: 0.63212\ntotal: 14.5331\nResult: count=8|label=a-signature-improper-integral-tester-design|max=4.60517|mean=1.8166|min=0.63212|total=14.5331\nRun 1 SHA-256: f09e90f9ea2e58f83b03c695eafcef8d446f30f07b28a2e22ca558f8f8e2dff0\nRun 2 SHA-256: f09e90f9ea2e58f83b03c695eafcef8d446f30f07b28a2e22ca558f8f8e2dff0\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Growth Equation Lab",
    "subject": "a Signature growth equation laboratory design",
    "description": "The Growth Equation Lab is a Signature-made design for teaching the simplest differential equations: a laboratory where a learner sets a growth rate, watches the exponential solution grow, and changes the starting value to see the whole family of solutions. The equation dy/dx = ky has solutions y = C e^(kx). The lab draws the solution curve for the chosen rate and starting value. Changing the starting value shifts the curve and shows the family of solutions. The doubling time is computed and shown on the graph.",
    "inputs": "FIGURES = {'rate': 2, 'starting_value': 3, 'y_at_1': 22.167, 'doubling_time': 0.3466, 'second_start': 1, 'second_y_at_1': 7.389, 'runs': 2, 'design_version': 1}\nLABEL = 'a-signature-growth-equation-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-growth-equation-laboratory-design\nmax: 22.167\nmean: 4.8628\nmin: 0.3466\ntotal: 38.9026\nResult: count=8|label=a-signature-growth-equation-laboratory-design|max=22.167|mean=4.8628|min=0.3466|total=38.9026\nRun 1 SHA-256: b0af159dcceecc9f1ad6209ec6e080d11263013229ebffefb994843cc604a552\nRun 2 SHA-256: b0af159dcceecc9f1ad6209ec6e080d11263013229ebffefb994843cc604a552\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Constraint Optimiser",
    "subject": "a Signature constraint optimiser design",
    "description": "The Constraint Optimiser is a Signature-made design for teaching Lagrange multipliers: a tool where a learner states a function and a constraint, and the tool draws the level curves (curves where the function is constant) and the constraint curve, showing them tangent at the optimum. At the optimum, the gradients are parallel. The tool draws the level curves of the function and the constraint curve together. The optimum is marked where a level curve is tangent to the constraint. The multiplier is shown as the ratio of the gradients at that point.",
    "inputs": "FIGURES = {'optimal_x': 5, 'optimal_y': 5, 'max_value': 25, 'multiplier': 5, 'constraint_sum': 10, 'endpoint_value': 0, 'curves_drawn': 3, 'design_version': 1}\nLABEL = 'a-signature-constraint-optimiser-design'\n",
    "expected": "count: 8\nlabel: a-signature-constraint-optimiser-design\nmax: 25\nmean: 6.75\nmin: 0\ntotal: 54\nResult: count=8|label=a-signature-constraint-optimiser-design|max=25|mean=6.75|min=0|total=54\nRun 1 SHA-256: a9eb7cf57769819fc0334ae2e418a6d7eb500c8748a4606e0b98764995e1d1fe\nRun 2 SHA-256: a9eb7cf57769819fc0334ae2e418a6d7eb500c8748a4606e0b98764995e1d1fe\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Mean Value Demonstrator",
    "subject": "a Signature mean value demonstrator design",
    "description": "The Mean Value Demonstrator is a Signature-made design for teaching the mean value theorem: a tool where a learner draws a function on an interval, and the tool draws the secant line (the line joining the endpoints) and finds the point where the tangent is parallel to it. The theorem guarantees such a point exists. The tool draws the function, the secant line, and the average rate of change. It searches for the point where the tangent is parallel to the secant. The hypotheses are checked: continuity on the closed interval, differentiability inside.",
    "inputs": "FIGURES = {'average_rate': 2, 'theorem_point': 1, 'distance_km': 120, 'time_hours': 2, 'average_speed': 60, 'interval_length': 2, 'tests_run': 2, 'design_version': 1}\nLABEL = 'a-signature-mean-value-demonstrator-design'\n",
    "expected": "count: 8\nlabel: a-signature-mean-value-demonstrator-design\nmax: 120\nmean: 23.75\nmin: 1\ntotal: 190\nResult: count=8|label=a-signature-mean-value-demonstrator-design|max=120|mean=23.75|min=1|total=190\nRun 1 SHA-256: 7dcca8b9a6ca19cae49d34e7ba620519372b414b9cd682467fedc85b0680b007\nRun 2 SHA-256: 7dcca8b9a6ca19cae49d34e7ba620519372b414b9cd682467fedc85b0680b007\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Curve Sketcher",
    "subject": "a Signature curve sketcher design",
    "description": "The Curve Sketcher is a Signature-made design for teaching curve sketching: a tool where a learner enters a function and the tool computes the derivatives, marks the critical points and inflection points, and draws the graph with its rising, falling, and bending labelled. The first derivative shows rise and fall; the second shows bending. The tool computes the first and second derivatives and their zeros. Critical points are marked as maxima, minima, or neither; inflection points are marked where the bending changes. Intercepts and asymptotes are listed alongside the sketch.",
    "inputs": "FIGURES = {'critical_points': 2, 'local_max': 2, 'local_min': -2, 'inflection_points': 1, 'roots': 3, 'root_1': -1.732, 'root_3': 1.732, 'design_version': 1}\nLABEL = 'a-signature-curve-sketcher-design'\n",
    "expected": "count: 8\nlabel: a-signature-curve-sketcher-design\nmax: 3\nmean: 0.875\nmin: -2\ntotal: 7.0\nResult: count=8|label=a-signature-curve-sketcher-design|max=3|mean=0.875|min=-2|total=7.0\nRun 1 SHA-256: 8328dac379722e06fe010f801b1958b5037fc1c5e5c02b07eac04a5f79bc648e\nRun 2 SHA-256: 8328dac379722e06fe010f801b1958b5037fc1c5e5c02b07eac04a5f79bc648e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Solid of Revolution Builder",
    "subject": "a Signature solid of revolution builder design",
    "description": "The Solid of Revolution Builder is a Signature-made design for teaching volumes of revolution: a tool where a learner draws a region, chooses an axis, and watches the solid form by rotation, with the volume computed by disks or shells. Rotating a region around an axis makes a solid whose volume is an integral. The tool draws the region and the axis, then animates the rotation. The disk method is shown as slices perpendicular to the axis; the shell method as shells parallel to it. Both methods are computed and must agree.",
    "inputs": "FIGURES = {'volume': 25.1327, 'methods': 2, 'upper_x': 4, 'radius_at_4': 2, 'disk_integral': 25.1327, 'shell_integral': 25.1327, 'slices_shown': 20, 'design_version': 1}\nLABEL = 'a-signature-solid-of-revolution-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-solid-of-revolution-builder-design\nmax: 25.1327\nmean: 13.0498\nmin: 1\ntotal: 104.3981\nResult: count=8|label=a-signature-solid-of-revolution-builder-design|max=25.1327|mean=13.0498|min=1|total=104.3981\nRun 1 SHA-256: 87964f26ab2b606bef0472155cd2d6b03884e4de9f047c338e8ae038762db201\nRun 2 SHA-256: 87964f26ab2b606bef0472155cd2d6b03884e4de9f047c338e8ae038762db201\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Arc Length Measurer",
    "subject": "a Signature arc length measurer design",
    "description": "The Arc Length Measurer is a Signature-made design for teaching arc length: a tool where a learner draws a curve, the tool approximates it by short straight segments, and the segment count is raised until the length settles. Arc length is the integral of the square root of 1 plus the square of the derivative. The tool draws the curve with the approximating segments overlaid. Raising the segment count shows the total length settling toward the integral. The surface area of the surface of revolution is offered as a second measure.",
    "inputs": "FIGURES = {'length_3_segments': 4.55, 'length_10_segments': 4.66, 'length_100_segments': 4.6666, 'exact_length': 4.6667, 'straight_distance': 4.5826, 'segment_counts': 3, 'upper_x': 3, 'design_version': 1}\nLABEL = 'a-signature-arc-length-measurer-design'\n",
    "expected": "count: 8\nlabel: a-signature-arc-length-measurer-design\nmax: 4.6667\nmean: 3.7657\nmin: 1\ntotal: 30.1259\nResult: count=8|label=a-signature-arc-length-measurer-design|max=4.6667|mean=3.7657|min=1|total=30.1259\nRun 1 SHA-256: 7968440a535ab901114579e158c8bde57a74ebca142b47c4b42b8163b6ff6b71\nRun 2 SHA-256: 7968440a535ab901114579e158c8bde57a74ebca142b47c4b42b8163b6ff6b71\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Polar Rose Plotter",
    "subject": "a Signature polar rose plotter design",
    "description": "The Polar Rose Plotter is a Signature-made design for teaching polar coordinates: a tool where a learner enters r as a function of theta (the angle), watches the curve traced as theta grows, and reads the area by the polar area formula. Polar coordinates describe a point by its distance and angle from the origin. The plotter traces the curve as theta increases, so the drawing order is visible. Petals are counted and each petal's area is computed by the formula (1/2) r squared integrated. The rectangular form is shown alongside for comparison.",
    "inputs": "FIGURES = {'petals': 4, 'petal_area': 1.5708, 'total_area': 6.2832, 'radius_max': 2, 'maxima': 4, 'theta_range': 6.2832, 'curves_traced': 1, 'design_version': 1}\nLABEL = 'a-signature-polar-rose-plotter-design'\n",
    "expected": "count: 8\nlabel: a-signature-polar-rose-plotter-design\nmax: 6.2832\nmean: 3.2671\nmin: 1\ntotal: 26.1372\nResult: count=8|label=a-signature-polar-rose-plotter-design|max=6.2832|mean=3.2671|min=1|total=26.1372\nRun 1 SHA-256: 52146a8b23a3958756fa2f2af71e49ce3c52d1b13a3d8ab99f08be5cac73788d\nRun 2 SHA-256: 52146a8b23a3958756fa2f2af71e49ce3c52d1b13a3d8ab99f08be5cac73788d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Limit at Infinity Viewer",
    "subject": "a Signature limit at infinity viewer design",
    "description": "The Limit at Infinity Viewer is a Signature-made design for teaching limits at infinity: a viewer where a learner watches a ratio tend to its limit as x grows, and watches (1 + 1/n)^n tend to e. A limit at infinity is the value a function approaches as its input grows without bound. The function is graphed, and the limit is shown as a horizontal line. The values are shown approaching the limit as x grows. The sequence (1 + 1/n)^n is shown approaching e.",
    "inputs": "FIGURES = {'value_x1': 0.833, 'value_x10': 3.048, 'value_x1000': 3.002, 'limit': 3, 'n_terms': 100, 'approx_e': 2.7048, 'e_true': 2.71828, 'error': 0.0135}\nLABEL = 'a-signature-limit-at-infinity-viewer-design'\n",
    "expected": "count: 8\nlabel: a-signature-limit-at-infinity-viewer-design\nmax: 100\nmean: 14.4149\nmin: 0.0135\ntotal: 115.3196\nResult: count=8|label=a-signature-limit-at-infinity-viewer-design|max=100|mean=14.4149|min=0.0135|total=115.3196\nRun 1 SHA-256: c359bcc8bcf231823685310173f7c063f4633460879cf0c10222278d876e9dfb\nRun 2 SHA-256: c359bcc8bcf231823685310173f7c063f4633460879cf0c10222278d876e9dfb\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Calculus Capstone Board",
    "subject": "a Signature calculus capstone board design",
    "description": "The Calculus Capstone Board is a Signature-made design for teaching combined calculus problem solving: a board of challenges, each needing limits, derivatives, and integrals together, where a learner plans the tools, solves each part, and assembles the parts. A capstone problem uses several ideas at once. Each challenge names the tools it needs: limit, derivative, integral, or series. Each part is solved and checked separately, then assembled. The board scores the plan, the checks, and the assembly.",
    "inputs": "FIGURES = {'parts': 3, 'volume': 0.41888, 'intersections': 2, 'integral_value': 0.13333, 'pi_factor': 0.41888, 'lower_limit': 0, 'upper_limit': 1, 'design_version': 1}\nLABEL = 'a-signature-calculus-capstone-board-design'\n",
    "expected": "count: 8\nlabel: a-signature-calculus-capstone-board-design\nmax: 3\nmean: 0.9964\nmin: 0\ntotal: 7.9711\nResult: count=8|label=a-signature-calculus-capstone-board-design|max=3|mean=0.9964|min=0|total=7.9711\nRun 1 SHA-256: 8bf0bc66a6e4475e76d66c626072f38dd192b86983f80116cae9d8c27be76821\nRun 2 SHA-256: 8bf0bc66a6e4475e76d66c626072f38dd192b86983f80116cae9d8c27be76821\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Limit (mathematics)",
    "url": "https://en.wikipedia.org/wiki/Limit_(mathematics)",
    "establishes": "The reference for a Signature limit microscope design in this record."
  },
  {
    "name": "Wikipedia - Calculus",
    "url": "https://en.wikipedia.org/wiki/Calculus",
    "establishes": "The reference for a Signature limit microscope design in this record."
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
