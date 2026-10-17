#!/usr/bin/env python3
"""Entries for the Calculus field databases (field #16, taxonomy order).

Verified 2026-10-17: NO database covers calculus as a discipline.
- 'mathematics-public' / 'mathematics-signature' / 'everything-mathematics':
  survey-level topic cards ("Calculus: limits, derivatives, integrals" as one
  card among dozens of branches) - no teaching depth.
- 'mathematics-study': curriculum/qualification cards - not the discipline.
- 'equations' (48,300 records): solved equation records - not calculus.
- 'scientific-formulas': formula CARDS - bare formulas ("Chain Rule",
  "Product Rule", "Taylor Series", "Derivative (power rule)") as reference,
  with no teaching, no ladder, no how-it-works, no demos. Reference cards are
  not discipline coverage (task instruction: formula cards do NOT count).
- 'hard-equations', 'math-word-problems', 'math': equation records /
  puzzle-style content - not calculus teaching.
- Whole-system dedupe index: zero calculus-discipline titles exist.

So this build creates two NEW databases, 36 ladder-ordered records each:

  calculus             - The Calculus Database
                         (public-harvest: real, fact-checked calculus)
  calculus-signature   - The Calculus Signature Database
                         (his original Signature interpretation;
                         src signature, titles suffixed
                         " (Signature Edition)", never presented
                         as authentic public record)

Subtitle disambiguation (fields #13-16 pattern): where a bare formula card
exists in scientific-formulas, discipline titles carry teaching-focused
subtitles, e.g. "The Chain Rule: Differentiating Composite Functions" rather
than bare "Chain Rule".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "calculus, clearly labeled Signature-made, never presented as "
            "authentic public record.")

C_STEWART = ("Stewart, James. 'Calculus: Early Transcendentals', 9th ed. "
             "Cengage Learning, 2021.")
C_APOSTOL = ("Apostol, Tom M. 'Calculus, Vol. 1: One-Variable Calculus, with "
             "an Introduction to Linear Algebra', 2nd ed. Wiley, 1967.")
C_SPIVAK = ("Spivak, Michael. 'Calculus', 4th ed. Publish or Perish, 2008.")
C_STRANG = ("Strang, Gilbert. 'Calculus'. Wellesley-Cambridge Press, 1991.")

ENTRIES = [
    {
        "key": "what_is_calculus",
        "name": "What Calculus Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Calculus is the mathematics of change and accumulation. Where "
            "algebra studies fixed quantities, calculus studies quantities "
            "that move: how fast a rocket climbs, how a curve bends, how "
            "a volume fills, how a population grows. It is built on two "
            "inverse operations. Differentiation cuts change into "
            "infinitesimal pieces, measuring instantaneous rates - the slope "
            "of a curve at a single point, the speed of a car at a single "
            "instant. Integration reassembles the pieces, measuring totals - "
            "the area under a curve, the distance traveled from a speed "
            "record, the work done by a varying force. Both rest on the "
            "limit: the precise way of talking about what a function "
            "approaches as its input approaches some value. The discipline "
            "runs from functions and limits, through derivatives and their "
            "applications, to integrals and their applications, then on to "
            "infinite series, parametric and polar forms, multivariable "
            "calculus, vector calculus, differential equations, and the "
            "numerical methods that carry calculus onto computers."
        ),
        "how_it_works": (
            "Calculus works by trading the impossible for the approachable. "
            "An instantaneous rate of change - slope at one point - is "
            "impossible to measure directly, because a rate needs two "
            "points. So calculus computes the average rate over smaller and "
            "smaller intervals and takes the limit as the interval shrinks "
            "to zero. That limit is the derivative. An exact area under a "
            "wiggly curve is impossible to measure directly, because the "
            "curve is not made of rectangles. So calculus slices the region "
            "into thinner and thinner rectangles and takes the limit as "
            "their widths shrink to zero. That limit is the integral. The "
            "fundamental theorem of calculus then proves the two operations "
            "undo each other: differentiation and integration are inverses. "
            "Everything else in the subject is machinery built on these "
            "two ideas - rules that make derivatives and integrals "
            "computable, and theorems that carry them to new settings."
        ),
        "key_points": [
            "Calculus studies change (differentiation) and accumulation (integration) - the two halves of one subject.",
            "The limit is the foundation: a rigorous way to describe what a function approaches as its input approaches a value.",
            "Differentiation measures instantaneous rates of change: slope at a point, speed at an instant, growth at a moment.",
            "Integration measures totals: areas, volumes, distances, work - assembled from infinitesimal pieces.",
            "The fundamental theorem of calculus proves differentiation and integration undo each other - they are inverse operations.",
        ],
        "requirements": [
            "Solid algebra: factoring, rational expressions, function notation, solving equations.",
            "Fluency with graphs: reading slope, intercepts, and shape from a plotted curve.",
            "A willingness to think about the infinitely small and the infinitely many - the limit idea takes practice.",
        ],
        "standards": [
            "Function notation f(x), limit notation lim(x->a), and derivative notation dy/dx and f'(x) used consistently.",
            "All quantities carry units through rate and accumulation problems; answers state units explicitly.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: calculus reframed as his engine of becoming - every "
            "derivative a Signature readout of how fast the world is changing, every "
            "integral a Signature gathering of what change has made."
        ),
        "demo_kind": "calc_branches",
    },
    {
        "key": "functions_models",
        "name": "Functions and Mathematical Models",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A function is the basic machine of calculus: a rule that takes "
            "each input x and returns exactly one output f(x). Calculus is "
            "the study of how those outputs change as the inputs change, so "
            "everything starts with functions and their graphs. Linear "
            "functions model constant rates; quadratics model acceleration "
            "and projectile paths; exponentials model growth and decay; "
            "trigonometric functions model oscillation. A mathematical "
            "model is a function chosen to describe a real situation - "
            "population over time, temperature over a day, velocity over a "
            "trip. Choosing the model means choosing the function's family "
            "and fitting its parameters to data; testing the model means "
            "comparing the function's predictions to new measurements. "
            "Domain and range, increasing and decreasing behavior, symmetry, "
            "periodicity, and composition of functions are the working "
            "vocabulary: every derivative and integral you ever compute "
            "will be computed on functions described in these terms."
        ),
        "how_it_works": (
            "Modeling works in four steps. First, name the quantities: the "
            "independent variable (usually time or position) and the "
            "dependent quantity the model predicts. Second, choose a "
            "function family whose shape matches the data's shape - "
            "straight-line data wants a linear function, doubling data "
            "wants an exponential, repeating data wants a sine wave. Third, "
            "fit the parameters: find the slope and intercept, the growth "
            "constant, the amplitude and period that make the function pass "
            "through or near the measured points. Fourth, validate: feed "
            "new inputs to the function and compare its outputs to fresh "
            "measurements; where it misses, refine the family or the "
            "parameters. Composition - feeding one function's output into "
            "another function's input - lets simple pieces build realistic "
            "models, and it is exactly what the chain rule later "
            "differentiates."
        ),
        "key_points": [
            "A function assigns exactly one output to each input - the fundamental machine calculus operates on.",
            "Mathematical models are functions chosen to describe real situations; the family is chosen by shape, parameters by data.",
            "Linear, quadratic, exponential, logarithmic, and trigonometric functions are the core model families.",
            "Composition f(g(x)) chains functions together; it is the structure the chain rule handles.",
            "Domain, range, monotonicity, symmetry, and periodicity are the working vocabulary of every later topic.",
        ],
        "requirements": [
            "Function notation and evaluation: given f(x), compute f(3), f(x+h).",
            "Graphing skill: plot points, recognize families by shape.",
            "Basic data sense: given a small table of measurements, judge which family fits.",
        ],
        "standards": [
            "Function families named by standard names: linear, quadratic, exponential, logarithmic, sinusoidal.",
            "Model parameters reported with units matching the modeled quantities.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: every model a Signature lens - his way of fitting a "
            "function to the world's shape and reading what the shape predicts."
        ),
        "demo_kind": "calc_models",
    },
    {
        "key": "idea_of_limit",
        "name": "The Idea of the Limit",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The limit is the single idea on which all of calculus stands. "
            "To say the limit of f(x) as x approaches a equals L means the "
            "values of f(x) can be made as close to L as anyone demands by "
            "taking x close enough to a - without ever requiring x to "
            "equal a. The function need not even be defined at a. Consider "
            "(x^2 - 1)/(x - 1): at x = 1 the formula is 0/0 and undefined, "
            "but for x near 1 the values crowd around 2, so the limit is 2. "
            "This idea rescues two quantities that are otherwise "
            "impossible: the slope of a curve at one point (average slope "
            "over shrinking intervals) and the exact area under a curve "
            "(sums over shrinking rectangles). The rigorous epsilon-delta "
            "definition turns 'arbitrarily close' into precise logic: for "
            "every tolerance epsilon there is a distance delta that forces "
            "f(x) within epsilon of L. One-sided limits, infinite limits, "
            "and limits at infinity extend the same idea to edges and "
            "horizons."
        ),
        "how_it_works": (
            "Working with limits is a negotiation between closeness of "
            "input and closeness of output. Numerically, you pick x values "
            "closer and closer to a from both sides - 0.9, 0.99, 0.999, "
            "then 1.1, 1.01, 1.001 - and watch f(x) settle toward a number; "
            "if both sides agree, that number is the limit. Graphically, "
            "you trace the curve toward the vertical line x = a and read "
            "the height the curve approaches. Analytically, you simplify: "
            "factor and cancel, rationalize, or divide by the highest power "
            "for limits at infinity. The limit laws let you split limits "
            "of sums, products, and quotients into limits of pieces. When "
            "the two sides disagree - a jump, a blow-up, an oscillation - "
            "the limit does not exist, and that disagreement is itself "
            "information about the function's behavior."
        ),
        "key_points": [
            "A limit describes what f(x) approaches as x approaches a; the function need not be defined at a itself.",
            "Limits make the impossible computable: slope at a point and area under a curve are both limits.",
            "One-sided limits check agreement from left and right; disagreement means no (two-sided) limit.",
            "The epsilon-delta definition makes 'arbitrarily close' rigorous.",
            "Infinite limits and limits at infinity describe blow-ups and end behavior.",
        ],
        "requirements": [
            "Comfort with function evaluation at many nearby points (tables).",
            "Algebraic simplification: factoring, rationalizing, working with fractions.",
            "Graph-reading: tracing a curve toward a vertical line.",
        ],
        "standards": [
            "Limit notation written in full: lim(x->a) f(x) = L, with one-sided variants lim(x->a-) and lim(x->a+).",
            "Numerical tables show values approaching from both sides before a limit claim is made.",
        ],
        "citations": [C_APOSTOL, C_SPIVAK],
        "sig_lens": (
            "Signature edition: the limit as his Signature zoom - pressing the lens ever "
            "closer until the world's blur resolves into a number."
        ),
        "demo_kind": "calc_limit_idea",
    },
    {
        "key": "computing_limits",
        "name": "Computing Limits",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Once the idea of the limit is clear, the work is computing "
            "them reliably. Direct substitution handles continuous "
            "functions: evaluate at a and you are done. The interesting "
            "cases are the indeterminate forms - 0/0, infinity/infinity - "
            "where substitution fails and algebra must intervene. Factoring "
            "and canceling resolves rational functions at holes; "
            "multiplying by the conjugate resolves roots; dividing "
            "numerator and denominator by the highest power resolves limits "
            "at infinity, revealing horizontal asymptotes. The limit laws - "
            "the limit of a sum is the sum of the limits, and likewise for "
            "differences, products, quotients (denominator nonzero), and "
            "powers - let you break a hard limit into easy pieces, provided "
            "each piece's limit exists. The squeeze theorem handles "
            "functions trapped between two others with the same limit, "
            "proving for example that sin(x)/x approaches 1 as x approaches "
            "0. Special trigonometric limits and the definition of e as a "
            "limit complete the toolkit that every derivative computation "
            "quietly depends on."
        ),
        "how_it_works": (
            "Computing a limit follows a decision tree. First try direct "
            "substitution; if it yields a finite number, that is the "
            "answer. If it yields 0/0, simplify algebraically: factor the "
            "numerator and denominator and cancel the common factor causing "
            "the hole, rationalize a radical by multiplying with its "
            "conjugate, or expand and collect terms. If it yields a form "
            "involving infinity, compare growth rates: for rational "
            "functions at infinity, the highest-degree terms decide, "
            "giving 0, a ratio of leading coefficients, or unbounded "
            "growth. If the function is trapped - bounded oscillation "
            "times a vanishing factor, like x*sin(1/x) - apply the squeeze "
            "theorem with explicit upper and lower bounding functions. "
            "Throughout, the limit laws justify each step, and one-sided "
            "limits are checked wherever a denominator can change sign or "
            "a root can go imaginary."
        ),
        "key_points": [
            "Direct substitution first; indeterminate forms (0/0, infinity/infinity) signal that algebra is needed.",
            "Factor-and-cancel, conjugate multiplication, and divide-by-highest-power are the three core algebraic moves.",
            "The limit laws justify splitting limits of sums, products, quotients, and powers into pieces.",
            "The squeeze theorem proves limits of trapped functions, e.g. sin(x)/x -> 1 as x -> 0.",
            "Limits at infinity reveal end behavior and horizontal asymptotes via dominant-term comparison.",
        ],
        "requirements": [
            "Factoring polynomials, including difference of squares and sum/difference of cubes.",
            "Working with conjugates and rationalizing denominators.",
            "Comparing polynomial degrees to judge growth at infinity.",
        ],
        "standards": [
            "Each algebraic step preserves the limit: the simplified function must agree with the original near (not necessarily at) a.",
            "Indeterminate forms are named explicitly before resolution (0/0, inf/inf).",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: limit computation as his Signature untangling - algebra "
            "pulling the true value out from behind an indeterminate mask."
        ),
        "demo_kind": "calc_limit_compute",
    },
    {
        "key": "continuity",
        "name": "Continuity of Functions: The Unbroken Graph",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A function is continuous at a point when its graph can be "
            "drawn through that point without lifting the pen: the "
            "function is defined there, the limit exists there, and the "
            "two are equal. Continuity is what makes calculus on a "
            "function trustworthy - continuous functions can be "
            "differentiated and integrated on their intervals, and they "
            "cannot jump over intermediate values. Discontinuities come "
            "in three flavors: removable (a hole that could be filled), "
            "jump (left and right limits exist but disagree), and "
            "infinite (the function blows up, as at a vertical "
            "asymptote). The intermediate value theorem turns continuity "
            "into a root-finding tool: if a continuous function is "
            "negative at one point and positive at another, it must cross "
            "zero somewhere between - the guarantee behind the bisection "
            "method. The extreme value theorem guarantees that a "
            "continuous function on a closed interval attains a maximum "
            "and a minimum, which is what makes optimization problems "
            "solvable."
        ),
        "how_it_works": (
            "Testing continuity at a point is a three-item checklist. "
            "First, is f(a) defined - does the formula produce a value? "
            "Second, does the two-sided limit as x approaches a exist - "
            "do the left and right approaches agree? Third, are they "
            "equal - does the limit match the value? Any failure is a "
            "discontinuity, classified by which item failed and how. "
            "Piecewise functions are checked at every breakpoint; rational "
            "functions are continuous everywhere except where the "
            "denominator vanishes. The intermediate value theorem is then "
            "applied by evaluating the function at the interval ends and "
            "checking for a sign change; the extreme value theorem is "
            "invoked by confirming continuity on a closed interval before "
            "hunting for maxima and minima. Both theorems are "
            "existence guarantees: they promise the value is there, and "
            "numerical methods go find it."
        ),
        "key_points": [
            "Continuity at a point = defined there, limit exists there, and the two are equal.",
            "Three discontinuity types: removable (hole), jump (sides disagree), infinite (blow-up).",
            "The intermediate value theorem: a continuous function cannot skip values - sign changes guarantee zeros.",
            "The extreme value theorem: continuity on a closed interval guarantees a max and a min exist.",
            "Differentiability implies continuity, but continuity does not imply differentiability (corners, cusps).",
        ],
        "requirements": [
            "Limit computation from the previous record, including one-sided limits.",
            "Reading piecewise definitions and domain restrictions.",
            "Sign analysis: evaluating a function at interval endpoints.",
        ],
        "standards": [
            "The three-part continuity test is applied explicitly at each candidate point.",
            "Discontinuities are classified by type, not merely labeled 'discontinuous'.",
        ],
        "citations": [C_APOSTOL, C_SPIVAK],
        "sig_lens": (
            "Signature edition: continuity as his Signature unbroken line - the world's "
            "quantities flowing without teleporting from one value to another."
        ),
        "demo_kind": "calc_continuity",
    },
    {
        "key": "derivative_rate",
        "name": "The Derivative: Instantaneous Rate of Change",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The derivative is the central object of differential "
            "calculus: the instantaneous rate of change of a function. "
            "For a position function s(t), the derivative s'(t) is the "
            "velocity at that instant; for a cost function C(x), the "
            "derivative is the marginal cost of one more unit. "
            "Geometrically it is the slope of the tangent line - the "
            "line that just touches the curve at a point. It is defined "
            "as a limit: the average rate of change (f(x+h) - f(x))/h "
            "over shrinking intervals h, pushed to h = 0. Where the "
            "derivative is positive the function climbs; where negative "
            "it falls; where zero it momentarily levels - a stationary "
            "point. A function can fail to be differentiable at corners "
            "(absolute value at zero), cusps, vertical tangents, and "
            "discontinuities: no smooth tangent exists there. The "
            "derivative function f' records the rate at every point at "
            "once, and its own derivative f'' - the second derivative - "
            "records how the rate itself is changing."
        ),
        "how_it_works": (
            "The derivative is computed as the limit of the difference "
            "quotient. Start with the average rate of change between x "
            "and x + h: (f(x+h) - f(x))/h. Algebraically simplify the "
            "numerator - expand, cancel the f(x) terms, factor out h - "
            "then divide by h and let h approach 0. What survives the "
            "limit is the derivative. Numerically, the same idea runs "
            "in reverse: compute the quotient for h = 0.1, 0.01, 0.001 "
            "and watch it converge; central differences (f(x+h) - "
            "f(x-h))/(2h) converge faster. The sign of the result tells "
            "you direction of change; its magnitude tells you speed. "
            "Repeating the process on f' gives f'', the concavity and "
            "acceleration record. Where the algebra of the quotient "
            "blows up or the left and right limits disagree, the "
            "derivative does not exist and the graph shows a corner, "
            "cusp, or break."
        ),
        "key_points": [
            "The derivative f'(x) is the limit of (f(x+h)-f(x))/h as h -> 0: instantaneous rate of change.",
            "Geometrically it is the tangent line's slope; physically it is velocity, marginal cost, growth rate.",
            "Sign of f' tells direction (up/down/flat); magnitude tells speed of change.",
            "Corners, cusps, vertical tangents, and discontinuities are points of non-differentiability.",
            "The second derivative f'' measures how the rate itself changes: concavity and acceleration.",
        ],
        "requirements": [
            "The limit concept and algebraic simplification of quotients.",
            "Slope of a line and the point-slope form for tangent lines.",
            "Interpreting position/velocity language from basic physics.",
        ],
        "standards": [
            "The difference quotient is written out in full before the limit is taken.",
            "Tangent lines are reported as equations with the point of tangency stated.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: the derivative as his Signature speedometer - pinned to "
            "the world's dashboard, reading how fast everything is becoming."
        ),
        "demo_kind": "calc_deriv_def",
    },
    {
        "key": "diff_rules",
        "name": "Differentiation Rules: Power, Product, and Quotient",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Computing derivatives from the limit definition every time "
            "would be exhausting, so calculus provides rules that make "
            "differentiation mechanical. The power rule is the "
            "workhorse: the derivative of x^n is n*x^(n-1) - bring the "
            "exponent down, subtract one. The sum rule differentiates "
            "term by term; constant multiples pass through. The product "
            "rule handles f(x)*g(x): the derivative is f'*g + f*g' - "
            "differentiate each factor in turn while the other stands "
            "still. The quotient rule handles f(x)/g(x): (f'*g - f*g')/g^2 "
            "- low d-high minus high d-low, over low squared. Together "
            "these rules differentiate every polynomial and rational "
            "function, and they combine with the rules for exponentials "
            "(d/dx e^x = e^x), logarithms (d/dx ln x = 1/x), and "
            "trigonometric functions (d/dx sin x = cos x, d/dx cos x = "
            "-sin x, and the rest) to cover the standard library. The "
            "rules are proved once from the limit definition and then "
            "used forever; fluency with them is the price of admission "
            "to everything downstream."
        ),
        "how_it_works": (
            "Applying the rules is a decomposition task. First, identify "
            "the function's outermost structure: is it a sum of terms, "
            "a product of factors, a quotient, or a composition (which "
            "belongs to the chain rule)? For a sum, differentiate each "
            "term and add. For a monomial a*x^n, apply the power rule: "
            "a*n*x^(n-1). For a product, label the factors f and g, "
            "compute f' and g' separately, and assemble f'*g + f*g'. For "
            "a quotient, compute the same pieces and assemble (f'*g - "
            "f*g')/g^2, then simplify. Exponentials, logs, and trig "
            "functions are differentiated by their memorized formulas "
            "wherever they appear as pieces. The final step is always "
            "simplification: factor common terms, combine fractions, and "
            "check the result numerically against the difference "
            "quotient at a sample point - a fast sanity check that "
            "catches sign errors."
        ),
        "key_points": [
            "Power rule: d/dx x^n = n*x^(n-1); sums differentiate term by term; constants factor out.",
            "Product rule: (fg)' = f'g + fg' - differentiate each factor in turn.",
            "Quotient rule: (f/g)' = (f'g - fg')/g^2.",
            "Standard derivatives: e^x -> e^x, ln x -> 1/x, sin x -> cos x, cos x -> -sin x.",
            "Strategy: identify structure (sum/product/quotient), apply the matching rule, then simplify and verify numerically.",
        ],
        "requirements": [
            "The derivative definition and difference-quotient algebra.",
            "Exponent rules and fraction manipulation for simplification.",
            "Memorized derivatives of e^x, ln x, sin x, cos x.",
        ],
        "standards": [
            "Every rule application names the rule being used.",
            "Final derivatives are simplified and checked numerically at a sample point.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: the differentiation rules as his Signature shorthand - "
            "the long limit labor compressed into moves his hand can make at speed."
        ),
        "demo_kind": "calc_diff_rules",
    },
    {
        "key": "chain_rule",
        "name": "The Chain Rule: Differentiating Composite Functions",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Most real functions are compositions - functions inside "
            "functions: sin(x^2), e^(3x), sqrt(1 + x^2), (x^3 + 2x)^10. "
            "The chain rule differentiates them: the derivative of the "
            "outer function evaluated at the inner function, times the "
            "derivative of the inner function. In Leibniz form, if y "
            "depends on u and u depends on x, then dy/dx = (dy/du)(du/dx) "
            "- the rates multiply like fractions, which is both the "
            "mnemonic and the intuition: a small change in x produces a "
            "change in u, which produces a change in y, and the total "
            "effect is the product of the two conversion rates. For "
            "sin(x^2): outer derivative cos(u) at u = x^2, times inner "
            "derivative 2x, giving 2x*cos(x^2). The rule chains "
            "arbitrarily: for three nested functions the derivative is "
            "the product of three rates. Forgetting the inner "
            "derivative - writing just cos(x^2) - is the most common "
            "error in all of differential calculus, and the rule exists "
            "to make it impossible to forget."
        ),
        "how_it_works": (
            "Chain-rule differentiation is an inside-out unpacking. "
            "First, name the layers: identify the outer function and "
            "the inner expression, writing y = f(u) with u = g(x). For "
            "deeper nesting, name u1, u2, and so on. Second, "
            "differentiate the outer function with respect to its own "
            "variable, leaving the inner expression untouched - "
            "differentiate sin(u) to cos(u), not to cos(x^2) yet. Third, "
            "differentiate the inner function with respect to x. Fourth, "
            "multiply the pieces and substitute the inner expression "
            "back in. Fifth, simplify. The Leibniz form dy/dx = "
            "dy/du * du/dx guides each step and extends to related "
            "rates, parametric equations, and implicit differentiation - "
            "every later technique in this database is the chain rule "
            "wearing a different hat. A numerical check against the "
            "difference quotient confirms the algebra."
        ),
        "key_points": [
            "Chain rule: d/dx f(g(x)) = f'(g(x)) * g'(x) - outer derivative times inner derivative.",
            "Leibniz form dy/dx = (dy/du)(du/dx): rates multiply like fractions.",
            "Always differentiate the outer function first, leaving the inner expression intact, then multiply by the inner derivative.",
            "The rule chains: three nested functions give a product of three rates.",
            "The classic error is dropping the inner derivative; the rule's structure prevents it.",
        ],
        "requirements": [
            "Identifying function composition and naming inner/outer layers.",
            "The basic differentiation rules for the individual layers.",
            "Careful bookkeeping: tracking which variable each derivative is with respect to.",
        ],
        "standards": [
            "Inner and outer functions are named explicitly before differentiating.",
            "Results are verified numerically against the difference quotient.",
        ],
        "citations": [C_STEWART, C_SPIVAK],
        "sig_lens": (
            "Signature edition: the chain rule as his Signature relay - change passed "
            "from layer to layer, each runner multiplying the baton's speed."
        ),
        "demo_kind": "calc_chain",
    },
    {
        "key": "implicit_diff",
        "name": "Implicit Differentiation",
        "group": "Differentiation",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Many curves cannot be written as y = f(x): the circle "
            "x^2 + y^2 = 25, the folium, an ellipse tilted by rotation. "
            "These relations define y implicitly as a function of x, "
            "and implicit differentiation finds dy/dx without solving "
            "for y. The trick is to differentiate both sides with "
            "respect to x, treating y as a function of x and applying "
            "the chain rule wherever y appears: d/dx(y^2) becomes "
            "2y*dy/dx, not 2y. The result is an equation containing "
            "dy/dx, which you solve algebraically. For the circle: 2x "
            "+ 2y*dy/dx = 0, so dy/dx = -x/y - the slope at any point, "
            "read straight off the coordinates. The method also "
            "differentiates inverse functions: writing y = arcsin(x) as "
            "sin(y) = x and differentiating implicitly yields dy/dx = "
            "1/sqrt(1 - x^2). It is the chain rule applied to relations, "
            "and it opens every curve that algebra cannot isolate."
        ),
        "how_it_works": (
            "Implicit differentiation runs in four moves. First, "
            "differentiate every term of the equation with respect to x. "
            "Terms in x alone differentiate normally. Terms in y "
            "differentiate with the chain rule, tacking on dy/dx: y^3 "
            "becomes 3y^2*dy/dx, sin(y) becomes cos(y)*dy/dx, xy becomes "
            "y + x*dy/dx by the product rule. Second, collect all terms "
            "containing dy/dx on one side of the equation. Third, "
            "factor out dy/dx and divide to isolate it. Fourth, "
            "simplify - often the original relation lets you replace "
            "messy expressions, as when x^2 + y^2 = 25 simplifies "
            "slope formulas. The answer is typically a function of both "
            "x and y, which is fine: the slope at a point on the curve "
            "depends on where you stand on it. Higher derivatives come "
            "from differentiating the dy/dx expression again."
        ),
        "key_points": [
            "Differentiate both sides with respect to x, treating y as a function of x.",
            "Every y-term gets the chain rule: d/dx(y^n) = n*y^(n-1)*dy/dx.",
            "Collect dy/dx terms, factor, and solve for dy/dx algebraically.",
            "Result is usually in x and y - e.g. the circle gives dy/dx = -x/y.",
            "Also differentiates inverse functions: arcsin, arctan, and ln fall out of implicit relations.",
        ],
        "requirements": [
            "The chain rule, applied reflexively to y-terms.",
            "The product rule for mixed xy terms.",
            "Solving linear equations for a target variable.",
        ],
        "standards": [
            "Each y-term's chain-rule step is shown, not skipped.",
            "The final dy/dx is simplified using the original relation where possible.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: implicit differentiation as his Signature skeleton key - "
            "unlocking the slope of any curve, even the ones algebra cannot open."
        ),
        "demo_kind": "calc_implicit",
    },
    {
        "key": "higher_derivatives",
        "name": "Higher-Order Derivatives",
        "group": "Differentiation",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Differentiating a derivative gives the second derivative "
            "f'' - the rate of change of the rate of change. For a "
            "position function, f' is velocity and f'' is acceleration: "
            "the second derivative is literally how hard you are being "
            "pushed. Geometrically, f'' measures concavity: positive "
            "means the curve cups upward (tangent lines lie below), "
            "negative means it cups downward. Where f'' changes sign "
            "sits an inflection point - the curve switches its cup, "
            "like an S bending from one concavity to the other. Third "
            "and higher derivatives continue the story: the third "
            "derivative of position is jerk, the felt jolt when "
            "acceleration itself changes, and engineers limit jerk to "
            "keep rides comfortable. Leibniz notation d^2y/dx^2 makes "
            "the repeated operation visible, and Taylor series later "
            "will show that the whole sequence f, f', f'', ... at a "
            "point encodes the entire function."
        ),
        "how_it_works": (
            "Higher derivatives are computed by repeated differentiation: "
            "find f', simplify, differentiate again for f'', simplify, "
            "and continue. Simplification between rounds is essential - "
            "unsimplified expressions explode in size. Each derivative "
            "is then read for meaning: f' = 0 locates stationary "
            "points; f'' > 0 at a stationary point means a local "
            "minimum (the second derivative test); f'' < 0 means a "
            "local maximum. Inflection points are found by solving "
            "f'' = 0 and checking for a sign change on either side. In "
            "motion problems the chain reads position -> velocity -> "
            "acceleration -> jerk, each the derivative of the last. "
            "Numerically, second derivatives come from second "
            "differences of function values, the discrete echo of "
            "differentiating twice."
        ),
        "key_points": [
            "f'' is the derivative of f': acceleration for motion, concavity for graphs.",
            "Second derivative test: f' = 0 and f'' > 0 -> local minimum; f'' < 0 -> local maximum.",
            "Inflection points sit where f'' changes sign - the curve switches concavity.",
            "Third derivative of position is jerk; engineers bound it for comfort and safety.",
            "The full sequence f, f', f'', ... at a point will later encode the whole function (Taylor).",
        ],
        "requirements": [
            "Fluency with first derivatives and simplification between rounds.",
            "Reading sign charts: where an expression is positive, negative, or zero.",
            "Basic motion vocabulary: position, velocity, acceleration.",
        ],
        "standards": [
            "Expressions are simplified between differentiation rounds.",
            "Inflection claims require a sign change of f'', not just f'' = 0.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: higher derivatives as his Signature depth gauge - each "
            "round of differentiation reading one layer deeper into how change changes."
        ),
        "demo_kind": "calc_higher",
    },
    {
        "key": "related_rates",
        "name": "Related Rates",
        "group": "Applications of Derivatives",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "In the physical world, quantities change together: as a "
            "balloon inflates, its radius, surface area, and volume all "
            "grow, each at its own rate, all linked by geometry. "
            "Related-rates problems turn a known rate into an unknown "
            "one through the chain rule. A spherical balloon's volume V "
            "= (4/3)pi*r^3 links volume and radius; differentiating "
            "with respect to time gives dV/dt = 4*pi*r^2*dr/dt, an "
            "equation relating the two rates. Given dV/dt (air pumped "
            "in per second) and the current radius, solve for dr/dt - "
            "how fast the surface is expanding right now. The method "
            "handles ladders sliding down walls, shadows lengthening, "
            "cones filling, boats approaching: write the geometric "
            "relation, differentiate with respect to time (every "
            "time-varying quantity gets the chain rule), substitute the "
            "known values, solve. The picture is mandatory - related "
            "rates are geometry with a clock running."
        ),
        "how_it_works": (
            "Every related-rates problem follows the same script. "
            "First, draw and label: name every changing quantity "
            "(radius r, height h, distance x), mark which rates are "
            "known and which is wanted, and record the instant's "
            "numerical values separately. Second, write the equation "
            "relating the quantities - a volume formula, the "
            "Pythagorean theorem, similar triangles. Third, "
            "differentiate both sides with respect to time t, applying "
            "the chain rule to every time-dependent variable so each "
            "term sprouts its rate (dr/dt, dh/dt). Fourth, substitute "
            "the known numbers - never before differentiating, since "
            "constants vanish and you would lose the rate. Fifth, "
            "solve for the unknown rate and check units and sign: a "
            "negative dr/dt means shrinking, and the units must be "
            "quantity-per-time."
        ),
        "key_points": [
            "Related rates link changing quantities through a geometric or physical relation differentiated in time.",
            "The chain rule is the engine: every time-varying variable contributes its own rate factor.",
            "Substitute known values only AFTER differentiating - early substitution kills the rates.",
            "Draw the picture first; label known rates, unknown rates, and the instant's values.",
            "Check sign and units: negative means decreasing, units must be quantity per unit time.",
        ],
        "requirements": [
            "Implicit differentiation with respect to time.",
            "Geometry formulas: volumes, areas, similar triangles, Pythagoras.",
            "Careful variable bookkeeping: rates vs. values at an instant.",
        ],
        "standards": [
            "A labeled diagram accompanies the setup.",
            "Substitution of numerical values happens after differentiation, never before.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: related rates as his Signature clockwork - gears of "
            "geometry turning together, each rate driving the next."
        ),
        "demo_kind": "calc_related",
    },
    {
        "key": "optimization",
        "name": "Optimization",
        "group": "Applications of Derivatives",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Optimization is calculus doing what the world constantly "
            "demands: find the best. The biggest area for a fixed fence "
            "length, the cheapest can holding a fixed volume, the "
            "fastest path, the maximum profit. The method converts the "
            "situation into a single-variable function on a closed "
            "interval, then lets derivatives do the hunting. Critical "
            "points - where f' = 0 or f' is undefined - are the only "
            "places an interior extremum can hide; the extreme value "
            "theorem guarantees the global max and min exist on a "
            "closed interval, so evaluating f at the critical points "
            "and the endpoints and comparing values finds them. The "
            "classic box problem - cut squares from a sheet's corners "
            "and fold up the sides - yields a cubic whose critical "
            "points give the maximum volume. Every design tradeoff, "
            "from bridge cables to business margins, is this same "
            "pattern: model, differentiate, compare candidates."
        ),
        "how_it_works": (
            "Optimization follows a fixed pipeline. First, draw the "
            "situation and name the quantity to maximize or minimize "
            "and the constraint linking the variables. Second, use the "
            "constraint to eliminate all but one variable, producing a "
            "single-variable function f on an explicit interval - the "
            "interval's endpoints come from physical reality (lengths "
            "cannot be negative, the cut cannot exceed half the sheet). "
            "Third, differentiate and find all critical points in the "
            "interval. Fourth, evaluate f at every critical point and "
            "at both endpoints; the largest value is the global "
            "maximum, the smallest the global minimum. Fifth, translate "
            "back: the winning x-value gives the optimal dimensions, "
            "and f's value gives the optimal outcome. The first or "
            "second derivative test can classify critical points, but "
            "the endpoint comparison is what certifies globality."
        ),
        "key_points": [
            "Optimization = model as a single-variable function on a closed interval, then compare candidates.",
            "Critical points (f' = 0 or undefined) plus endpoints are the only candidates for global extrema.",
            "The extreme value theorem guarantees the max and min exist - comparison finds them.",
            "The constraint eliminates variables; the interval comes from physical reality.",
            "Always translate the winning x back into the situation's dimensions and optimal value.",
        ],
        "requirements": [
            "Differentiation rules and critical-point algebra.",
            "Translating word problems into equations with constraints.",
            "Interval reasoning: endpoints and feasibility.",
        ],
        "standards": [
            "The constraint equation and the single-variable objective are both written explicitly.",
            "Endpoints are evaluated - interior critical points alone do not certify a global extremum.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: optimization as his Signature best-finder - the derivative "
            "sniffing out the peak and the valley no guesswork could reach."
        ),
        "demo_kind": "calc_optimize",
    },
    {
        "key": "curve_sketching",
        "name": "Extrema, Concavity, and Curve Sketching",
        "group": "Applications of Derivatives",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Derivatives let you draw a function's graph from its "
            "formula alone, reading shape from algebra. The first "
            "derivative f' controls rise and fall: f' > 0 means "
            "increasing, f' < 0 means decreasing, and sign changes at "
            "critical points mark local maxima (down-crossing) and "
            "minima (up-crossing) by the first derivative test. The "
            "second derivative f'' controls concavity: f'' > 0 cups "
            "up, f'' < 0 cups down, and sign changes of f'' mark "
            "inflection points where the bending reverses. Asymptotes "
            "frame the drawing: vertical asymptotes where the "
            "function blows up, horizontal or slant asymptotes from "
            "limits at infinity. Assembled - domain, intercepts, "
            "symmetry, asymptotes, increasing/decreasing intervals, "
            "local extrema, concavity, inflection points - these "
            "produce an accurate sketch without plotting hundreds of "
            "points. It is the same analysis, automated, inside every "
            "graphing tool: the machine is just running this checklist."
        ),
        "how_it_works": (
            "Curve sketching runs a fixed checklist. Compute the "
            "domain (where the formula is defined) and the intercepts. "
            "Find vertical asymptotes by locating blow-ups and "
            "horizontal/slant asymptotes via limits at infinity. "
            "Differentiate: solve f' = 0 for critical points, then "
            "build a sign chart for f' on the intervals between them - "
            "the sign pattern gives increasing/decreasing intervals, "
            "and each sign change classifies a local max or min. "
            "Differentiate again: solve f'' = 0, build its sign chart "
            "for concavity intervals, and mark inflection points where "
            "the sign genuinely changes. Plot the intercepts, extrema, "
            "and inflection points, draw the asymptotes as guides, and "
            "connect with curves obeying the rise/fall and cup "
            "directions. Verify key features numerically - evaluate f "
            "at the critical points - before trusting the sketch."
        ),
        "key_points": [
            "f' sign chart gives increasing/decreasing intervals; sign changes at critical points classify local max/min.",
            "f'' sign chart gives concavity; sign changes of f'' mark inflection points.",
            "Asymptotes (vertical from blow-ups, horizontal/slant from limits at infinity) frame the graph.",
            "The full checklist: domain, intercepts, symmetry, asymptotes, monotonicity, extrema, concavity, inflection.",
            "Graphing software runs this same analysis - the checklist is the algorithm.",
        ],
        "requirements": [
            "Solving f' = 0 and f'' = 0; sign-chart analysis.",
            "Limits at infinity and vertical-asymptote detection.",
            "Plotting points and reading graph features.",
        ],
        "standards": [
            "Every claimed extremum or inflection point is justified by a sign change, not just a zero derivative.",
            "Asymptotes are derived from limits, not guessed from the formula.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: curve sketching as his Signature portraiture - the "
            "derivatives sitting for the painter until the function's face appears."
        ),
        "demo_kind": "calc_sketch",
    },
    {
        "key": "lhopital",
        "name": "L'Hôpital's Rule",
        "group": "Differentiation",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Some limits defeat algebra: sin(x)/x as x approaches 0, "
            "(e^x - 1)/x, ln(x)/(x - 1). Each is 0/0, yet each has a "
            "definite value. L'Hôpital's rule resolves them: when "
            "f(x)/g(x) gives 0/0 or infinity/infinity at a, the limit "
            "equals the limit of f'(x)/g'(x) - differentiate top and "
            "bottom separately (not the quotient rule) and try again. "
            "For sin(x)/x: derivatives give cos(x)/1, whose limit at 0 "
            "is 1. The rule can be applied repeatedly until the form "
            "resolves. Other indeterminate forms are converted first: "
            "0*infinity becomes a quotient by rewriting, infinity - "
            "infinity combines into one fraction, and 0^0, 1^infinity, "
            "infinity^0 are tamed by taking logarithms, which drag the "
            "exponent down into a product. The rule's condition is "
            "strict - it applies only to genuine 0/0 or "
            "infinity/infinity forms; applying it to anything else "
            "produces confident nonsense."
        ),
        "how_it_works": (
            "Using L'Hôpital's rule is a loop with a gate. First, "
            "verify the gate: direct substitution must give 0/0 or "
            "infinity/infinity - if not, the rule does not apply, "
            "stop. Second, differentiate the numerator and the "
            "denominator separately and form the new quotient. Third, "
            "take the limit of the new quotient; if it resolves to a "
            "number or a determinate infinity, that is the answer. If "
            "it is still 0/0 or infinity/infinity, repeat. For the "
            "other forms, convert first: rewrite f*g as f/(1/g) for "
            "0*infinity; combine differences over a common denominator "
            "for infinity - infinity; take ln of both sides for the "
            "exponential forms, turning them into 0*infinity, then "
            "convert again. Each conversion is justified by continuity "
            "of the logarithm and exponential. A final numerical check "
            "near the limit point confirms the symbolic result."
        ),
        "key_points": [
            "L'Hôpital's rule: 0/0 or inf/inf forms resolve via lim f'(x)/g'(x) - differentiate top and bottom separately.",
            "The gate is strict: verify the indeterminate form by substitution before differentiating.",
            "The rule may be applied repeatedly until the form resolves.",
            "Other forms convert first: 0*inf -> quotient; exponential forms -> take logarithms.",
            "Misapplication to non-indeterminate forms gives wrong answers - the gate check is the whole safety.",
        ],
        "requirements": [
            "Fluency with the differentiation rules for the pieces.",
            "Logarithm and exponential algebra for the conversion step.",
            "Recognizing the seven indeterminate forms on sight.",
        ],
        "standards": [
            "The indeterminate form is verified by substitution before the rule is invoked.",
            "Each differentiation round is shown; the final answer is checked numerically.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: L'Hôpital's rule as his Signature skeleton key for limits - "
            "differentiating the lock until the stuck 0/0 swings open."
        ),
        "demo_kind": "calc_lhopital",
    },
    {
        "key": "antiderivatives",
        "name": "Antiderivatives",
        "group": "Integration",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "An antiderivative of f is a function F whose derivative is "
            "f: differentiation run backward. If f(x) = 2x, then F(x) = "
            "x^2 is an antiderivative - but so is x^2 + 5, x^2 - 100, "
            "and x^2 + C for any constant C, because constants "
            "differentiate to zero. The general antiderivative is "
            "always a family F(x) + C, and recovering the right member "
            "needs one extra piece of data: an initial condition like "
            "F(0) = 3 that pins down C. Antiderivatives reverse every "
            "differentiation rule: the power rule runs backward as "
            "x^n -> x^(n+1)/(n+1), sums split term by term, and the "
            "standard functions reverse to their known forms (1/x -> "
            "ln|x|, cos x -> sin x, e^x -> e^x). In physics this is "
            "how motion is reconstructed: integrate acceleration to "
            "get velocity, integrate velocity to get position, with "
            "initial velocity and position fixing the constants. The "
            "indefinite integral notation ∫f(x)dx is the symbol for "
            "this whole family."
        ),
        "how_it_works": (
            "Finding antiderivatives is pattern-matching in reverse. "
            "First, ask what function differentiates to each term: a "
            "power x^n comes from x^(n+1)/(n+1) (for n != -1); e^x "
            "comes from e^x; 1/x comes from ln|x|; sin x comes from "
            "-cos x; cos x comes from sin x. Constant multiples carry "
            "through; sums split into separate reversals. Second, add "
            "+ C to the assembled result - the arbitrary constant is "
            "not decoration, it is the general solution. Third, verify "
            "by differentiating your answer: you must recover the "
            "original integrand exactly. Fourth, if an initial "
            "condition is given, substitute it to solve for C and "
            "write the particular antiderivative. When no rule "
            "reverses cleanly - x*e^x, sqrt(1 + x^2) - the integral "
            "needs the techniques of later records (substitution, "
            "parts, partial fractions) or may not exist in elementary "
            "form at all."
        ),
        "key_points": [
            "An antiderivative F satisfies F' = f; the general form is always F(x) + C.",
            "Initial conditions pin down C, selecting one member of the family.",
            "Rules run backward: x^n -> x^(n+1)/(n+1), e^x -> e^x, 1/x -> ln|x|, cos x -> sin x.",
            "Physics: integrate acceleration -> velocity -> position; initial data fixes the constants.",
            "Always verify by differentiating the answer - you must recover the integrand.",
        ],
        "requirements": [
            "The differentiation rules, run in reverse as recognition patterns.",
            "Solving for C from an initial condition.",
            "Comfort with the + C convention and what it means.",
        ],
        "standards": [
            "Every indefinite integral carries + C.",
            "Answers are verified by differentiation before being trusted.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: antiderivatives as his Signature rewind - running the "
            "film of change backward until the original motion reappears."
        ),
        "demo_kind": "calc_antideriv",
    },
    {
        "key": "riemann_integral",
        "name": "Riemann Sums and the Definite Integral",
        "group": "Integration",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The definite integral ∫[a,b] f(x)dx is the exact signed "
            "area between the curve and the x-axis - and it is defined "
            "as a limit of Riemann sums. Slice [a,b] into n "
            "subintervals, build a rectangle on each slice with height "
            "f at a sample point, add the areas. Left endpoints, right "
            "endpoints, and midpoints give different sums for finite "
            "n, but as n grows and the slice widths shrink to zero, "
            "all choices converge to the same number: the integral. "
            "Area above the axis counts positive, below counts "
            "negative, so the integral is net signed area - a "
            "velocity integral gives net displacement, while total "
            "distance needs the integral of |v|. The integral's "
            "properties mirror summation: integrals add over adjacent "
            "intervals, constants factor out, sums split, and "
            "comparison bounds integrals between rectangle estimates. "
            "This limit-of-sums is the definition everything else "
            "must agree with - the fundamental theorem will later "
            "provide the shortcut, but the Riemann sum is the meaning."
        ),
        "how_it_works": (
            "A Riemann sum is built in five steps. Choose n and the "
            "slice width Δx = (b - a)/n. Choose sample points: left "
            "endpoints x_i = a + i*Δx, right endpoints, or midpoints "
            "(midpoints converge fastest). Evaluate f at each sample "
            "point and multiply by Δx - that is one rectangle's "
            "signed area. Add all n rectangles. Then take the limit "
            "as n -> infinity: in practice, double n repeatedly and "
            "watch the sums settle. The three sample choices bracket "
            "the truth for monotone functions - left and right sums "
            "trap the integral from opposite sides - which gives "
            "rigorous error bounds for finite n. The definite "
            "integral's properties (additivity, linearity, comparison) "
            "are all proved by passing the corresponding sum "
            "properties through the limit."
        ),
        "key_points": [
            "The definite integral is the limit of Riemann sums as slice widths shrink to zero.",
            "Left, right, and midpoint sums differ for finite n but converge to the same integral.",
            "Signed area: above the axis positive, below negative; net displacement vs total distance.",
            "Properties: additivity over intervals, linearity, comparison bounds.",
            "The Riemann sum is the definition; the fundamental theorem is the shortcut that must agree with it.",
        ],
        "requirements": [
            "Summation notation and the idea of a limit of sums.",
            "Evaluating functions at arithmetic sequences of points.",
            "Reading area-above vs area-below from a graph.",
        ],
        "standards": [
            "Slice width, sample choice, and n are stated explicitly in every sum.",
            "Convergence is demonstrated by doubling n, not asserted from one value.",
        ],
        "citations": [C_APOSTOL, C_STEWART],
        "sig_lens": (
            "Signature edition: Riemann sums as his Signature mosaic - ten thousand tiny "
            "rectangles laid until the curve's true area shows through."
        ),
        "demo_kind": "calc_riemann",
    },
    {
        "key": "ftc",
        "name": "The Fundamental Theorem of Calculus",
        "group": "Integration",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The fundamental theorem of calculus is the hinge of the "
            "whole subject: it proves that differentiation and "
            "integration undo each other. Part 1: if F(x) is the "
            "accumulation function ∫[a,x] f(t)dt, then F'(x) = f(x) - "
            "the rate at which accumulated area grows is the "
            "function's height. Part 2: ∫[a,b] f(x)dx = F(b) - F(a) "
            "for any antiderivative F - definite integrals are "
            "computed by evaluating an antiderivative at the "
            "endpoints and subtracting, no Riemann sums required. "
            "This turns area problems into antiderivative problems: "
            "∫[0,1] x^2 dx = 1/3 - 0 = 1/3 in one line. It also "
            "explains why every differentiation rule has an "
            "integration counterpart and why the two halves of the "
            "course are one subject. Net change appears as the "
            "physical reading: the integral of a rate of change over "
            "an interval is the net change in the quantity - "
            "integrate velocity to get displacement, integrate "
            "marginal cost to get total cost change."
        ),
        "how_it_works": (
            "Using the theorem is a two-step evaluation. First, find "
            "an antiderivative F of the integrand - any one will do, "
            "the + C cancels in the subtraction. Second, compute F(b) "
            "- F(a): evaluate at the top limit, evaluate at the "
            "bottom limit, subtract. That is the entire computation; "
            "the Riemann sum machinery is bypassed. Part 1 is used "
            "when the integral itself has a variable limit: to "
            "differentiate ∫[a,x] f(t)dt, just write f(x); when the "
            "upper limit is a function u(x), the chain rule adds a "
            "factor: d/dx ∫[a,u(x)] f(t)dt = f(u(x))*u'(x). The net "
            "change reading guides setup: identify the rate, identify "
            "the interval, integrate, and interpret the number as "
            "total accumulated change. Every area, volume, and work "
            "computation in the records ahead runs through this "
            "theorem."
        ),
        "key_points": [
            "FTC Part 1: d/dx of the accumulation function ∫[a,x] f(t)dt is f(x).",
            "FTC Part 2: ∫[a,b] f(x)dx = F(b) - F(a) - antiderivatives evaluate definite integrals.",
            "Variable limits differentiate by Part 1; composed limits add the chain rule factor.",
            "Net change: the integral of a rate over an interval is the quantity's total change.",
            "The theorem is why differentiation and integration are one subject, not two.",
        ],
        "requirements": [
            "Antiderivative fluency - the theorem is useless without them.",
            "The chain rule for variable-limit differentiation.",
            "Reading 'rate' vs 'quantity' in applied setups.",
        ],
        "standards": [
            "The antiderivative used is stated before evaluation.",
            "F(b) - F(a) is shown as two evaluations and a subtraction, with the + C noted as canceling.",
        ],
        "citations": [C_APOSTOL, C_SPIVAK],
        "sig_lens": (
            "Signature edition: the fundamental theorem as his Signature handshake - the "
            "two halves of calculus recognizing each other as inverses."
        ),
        "demo_kind": "calc_ftc",
    },
    {
        "key": "substitution",
        "name": "Integration by Substitution",
        "group": "Integration Techniques",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Substitution is the chain rule run backward - the first "
            "and most-used integration technique. When an integrand "
            "contains a function and (up to a constant) its "
            "derivative, naming the inner function u collapses the "
            "integral into a simple one. For ∫2x*cos(x^2)dx, set u = "
            "x^2; then du = 2x dx, and the integral becomes ∫cos(u)du "
            "= sin(u) + C = sin(x^2) + C. The method handles "
            "compositions systematically: spot the inner function, "
            "compute its differential, check that the remaining "
            "factors match du up to a constant, rewrite everything "
            "in u, integrate, substitute back. Definite integrals "
            "can change the limits too: when x runs a -> b, u runs "
            "u(a) -> u(b), so no back-substitution is needed. Failed "
            "substitutions - where the derivative factor is missing - "
            "signal that parts, partial fractions, or trig methods "
            "are needed instead."
        ),
        "how_it_works": (
            "Substitution follows five moves. First, choose u: the "
            "inner function of a composition, the expression inside "
            "a root or a power, or the denominator of a quotient. "
            "Second, compute du = u'(x)dx formally. Third, rewrite "
            "the integral: express the remaining x-factors as a "
            "constant multiple of du and replace every x with u - if "
            "x's remain that cannot be absorbed, the substitution "
            "fails and you choose again. Fourth, integrate in u "
            "using the basic rules. Fifth, substitute back to x (or, "
            "for definite integrals, transform the limits at step "
            "three and skip the return trip). Verification is by "
            "differentiation with the chain rule: differentiating "
            "your answer must reproduce the original integrand, "
            "which closes the loop with the rule substitution "
            "reverses."
        ),
        "key_points": [
            "Substitution reverses the chain rule: set u to the inner function, rewrite in du.",
            "The derivative factor must be present (up to a constant) - its absence means the substitution fails.",
            "Definite integrals may transform the limits u(a) -> u(b) and skip back-substitution.",
            "Choose u as the inner composition, the radicand, or the denominator.",
            "Verify by differentiating the answer with the chain rule.",
        ],
        "requirements": [
            "The chain rule, recognized in reverse.",
            "Differential notation: computing du = u'(x)dx.",
            "Comfort abandoning a bad u-choice and trying another.",
        ],
        "standards": [
            "The u-choice and du computation are written explicitly.",
            "No x remains after rewriting; the back-substitution (or limit change) is shown.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: substitution as his Signature renaming trick - one clever "
            "alias turning a tangled integral into a familiar one."
        ),
        "demo_kind": "calc_substitution",
    },
    {
        "key": "int_by_parts",
        "name": "Integration by Parts: A Product Rule in Reverse",
        "group": "Integration Techniques",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Integration by parts reverses the product rule: ∫u dv = "
            "uv - ∫v du. It trades one integral for another, and the "
            "trade wins when the new integral is simpler than the "
            "old. The classic ∫x*e^x dx sets u = x, dv = e^x dx; then "
            "du = dx, v = e^x, and the formula gives x*e^x - ∫e^x dx "
            "= (x-1)e^x + C - the x that made the integrand hard "
            "differentiates away. Choosing u follows the LIATE "
            "priority - Logarithmic, Inverse trig, Algebraic, "
            "Trigonometric, Exponential: whichever factor appears "
            "first in that list becomes u, because it simplifies "
            "most when differentiated. Some integrals need parts "
            "twice (e^x*sin x cycles back to itself, letting you "
            "solve for the integral algebraically); some need parts "
            "plus substitution; definite integrals apply the formula "
            "with the uv term evaluated at both limits. Tabular "
            "integration streamlines repeated parts for products of "
            "polynomials with exponentials or trig."
        ),
        "how_it_works": (
            "Integration by parts runs as a deliberate trade. First, "
            "split the integrand into u and dv using LIATE priority: "
            "logs and inverse trig become u (they simplify when "
            "differentiated), exponentials and trig become dv (they "
            "survive integration unchanged). Second, compute du by "
            "differentiating u and v by integrating dv. Third, write "
            "uv - ∫v du and simplify. Fourth, evaluate the new "
            "integral - if it is simpler, integrate it; if it "
            "reproduces the original (the cyclic case), collect like "
            "terms and solve algebraically; if it needs another "
            "round, apply parts again, possibly via the tabular "
            "method. For definite integrals, the boundary term uv is "
            "evaluated F(b) - F(a) style at the limits. The method "
            "fails gracefully: a bad u/dv split makes the new "
            "integral worse, which is the signal to swap the choice."
        ),
        "key_points": [
            "Formula: ∫u dv = uv - ∫v du - trade the integral for a simpler one.",
            "LIATE priority picks u: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential.",
            "Differentiate u to simplify it; integrate dv to keep it manageable.",
            "Cyclic cases (e^x sin x) return the original integral - solve for it algebraically.",
            "Definite integrals evaluate the uv boundary term at both limits.",
        ],
        "requirements": [
            "The product rule, run in reverse as a recognition pattern.",
            "LIATE ordering memorized and applied to choose u vs dv.",
            "Algebraic equation-solving for the cyclic case.",
        ],
        "standards": [
            "The u/dv split is stated with its LIATE justification.",
            "The new integral is shown to be simpler (or the cyclic equation solved explicitly).",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: integration by parts as his Signature trade - swapping a "
            "hard integral for an easier one, like trading a heavy crate for a light box."
        ),
        "demo_kind": "calc_parts",
    },
    {
        "key": "trig_integrals",
        "name": "Trigonometric Integrals and Substitutions",
        "group": "Integration Techniques",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Powers and products of sines and cosines integrate through "
            "identities, not brute force. Odd powers peel off one "
            "factor for the substitution: ∫sin^3(x)dx becomes "
            "∫(1 - cos^2 x) sin x dx with u = cos x. Even powers use "
            "the half-angle identities sin^2 = (1 - cos 2x)/2 to lower "
            "the degree. Products sin(mx)cos(nx) split via "
            "product-to-sum formulas. When the integrand contains "
            "sqrt(a^2 - x^2), sqrt(a^2 + x^2), or sqrt(x^2 - a^2), "
            "trigonometric substitution removes the root: x = a*sin θ "
            "collapses sqrt(a^2 - x^2) to a*cos θ, x = a*tan θ "
            "collapses sqrt(a^2 + x^2) to a*sec θ, x = a*sec θ "
            "collapses sqrt(x^2 - a^2) to a*tan θ. After integrating "
            "in θ, a reference triangle converts back to x. These "
            "methods complete the elementary toolkit: with "
            "substitution, parts, partial fractions, and trig "
            "techniques, every rational function and most "
            "trigonometric forms become integrable."
        ),
        "how_it_works": (
            "Trigonometric integrals follow identity-first recipes. "
            "For sin^m*cos^n: if either power is odd, save one factor "
            "of that function for du and convert the rest with "
            "sin^2 + cos^2 = 1; if both are even, apply half-angle "
            "identities repeatedly until only first powers remain. "
            "For tan/sec integrals, use the derivative pairs "
            "(tan)' = sec^2 and (sec)' = sec tan to guide "
            "substitutions. For roots, match the form: a^2 - x^2 "
            "takes x = a sin θ, a^2 + x^2 takes x = a tan θ, x^2 - "
            "a^2 takes x = a sec θ; draw the reference triangle "
            "labeled with the substitution so every trig function of "
            "θ converts back to an x-expression. Integrate in θ, "
            "then read the triangle backward to return to x. "
            "Definite integrals may convert limits to θ-limits and "
            "never return. Each result is verified by differentiation."
        ),
        "key_points": [
            "Odd powers: peel one factor for du, convert the rest via sin^2 + cos^2 = 1.",
            "Even powers: half-angle identities lower the degree until first powers remain.",
            "Trig substitution kills roots: a^2-x^2 -> a sin θ; a^2+x^2 -> a tan θ; x^2-a^2 -> a sec θ.",
            "The reference triangle converts the θ-answer back to x.",
            "These complete the elementary toolkit alongside substitution, parts, and partial fractions.",
        ],
        "requirements": [
            "The Pythagorean, half-angle, and product-to-sum identities.",
            "Substitution mechanics from the previous record.",
            "Drawing and reading reference triangles.",
        ],
        "standards": [
            "The identity or substitution used is named before integration begins.",
            "Reference triangles are drawn for every trig substitution.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: trig integrals as his Signature wave-taming - identities "
            "calming wild oscillations into integrals that sit still."
        ),
        "demo_kind": "calc_trigint",
    },
    {
        "key": "partial_fractions",
        "name": "Partial Fractions",
        "group": "Integration Techniques",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Every proper rational function - polynomial over "
            "polynomial, numerator degree below denominator degree - "
            "can be integrated, because partial fractions split it "
            "into pieces with known antiderivatives. The method: "
            "factor the denominator completely, then write one "
            "fraction per factor - A/(x - r) for each distinct "
            "linear factor, a chain A/(x-r) + B/(x-r)^2 + ... for "
            "repeated ones, (Ax + B)/(quadratic) for irreducible "
            "quadratics - and solve for the constants by clearing "
            "denominators and matching coefficients. Each piece then "
            "integrates elementarily: A/(x - r) gives A*ln|x - r|, "
            "powers give power-rule terms, irreducible quadratics "
            "give arctangent (after completing the square). For "
            "example, 1/(x(x-1)) splits into -1/x + 1/(x-1), "
            "integrating to ln|x-1| - ln|x|. If the numerator's "
            "degree is not below the denominator's, polynomial long "
            "division comes first. This is the technique that proves "
            "rational functions are always integrable in elementary "
            "terms - a completeness result, not just a trick."
        ),
        "how_it_works": (
            "Partial fractions run as structured decomposition. "
            "First, ensure a proper fraction: divide if the "
            "numerator's degree reaches the denominator's. Second, "
            "factor the denominator into linear and irreducible "
            "quadratic factors over the reals. Third, write the "
            "template: each distinct linear factor (x - r) contributes "
            "A/(x - r); each repeated factor (x - r)^k contributes k "
            "terms with powers 1 through k; each irreducible "
            "quadratic contributes (Ax + B)/(quadratic). Fourth, "
            "clear denominators and solve for the constants - "
            "substituting the roots r makes most constants fall out "
            "immediately (the cover-up method), with coefficient "
            "matching for the rest. Fifth, integrate term by term: "
            "linear pieces give logarithms, repeated pieces give "
            "powers, quadratics give arctangents after completing "
            "the square. The decomposition is verified by recombining."
        ),
        "key_points": [
            "Partial fractions split any proper rational function into integrable elementary pieces.",
            "Template: distinct linear -> A/(x-r); repeated -> power chain; irreducible quadratic -> (Ax+B)/quad.",
            "Long division first if the fraction is improper.",
            "Pieces integrate to logarithms, powers, and arctangents (after completing the square).",
            "This proves rational functions are always elementarily integrable - a completeness result.",
        ],
        "requirements": [
            "Factoring polynomials, including quadratics and grouping.",
            "Solving linear systems for the undetermined constants.",
            "Completing the square for irreducible quadratics.",
        ],
        "standards": [
            "The denominator factorization is shown before the template is written.",
            "The decomposition is verified by recombining the pieces.",
        ],
        "citations": [C_APOSTOL, C_STEWART],
        "sig_lens": (
            "Signature edition: partial fractions as his Signature disassembly line - one "
            "complicated rational machine broken into parts, each with its own manual."
        ),
        "demo_kind": "calc_partfrac",
    },
    {
        "key": "improper_integrals",
        "name": "Improper Integrals",
        "group": "Integration",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Improper integrals extend integration past its original "
            "boundaries: infinite limits, or integrands that blow up "
            "inside the interval. ∫[1,∞] (1/x^2)dx asks for the area "
            "under a curve that never ends - and the answer is a "
            "finite 1, because the curve thins faster than the "
            "interval lengthens. The definition is always a limit: "
            "replace infinity with a variable bound b, integrate, "
            "then let b -> infinity; replace a blow-up point c with "
            "c + epsilon and let epsilon -> 0. If the limit exists "
            "the integral converges; if not, it diverges - "
            "∫[1,∞] (1/x)dx diverges, growing like ln b without "
            "bound. The comparison test decides hard cases: if 0 <= "
            "f <= g and ∫g converges, then ∫f converges too. The "
            "p-integral test classifies the power family: ∫[1,∞] "
            "x^(-p)dx converges exactly when p > 1. Improper "
            "integrals underlie probability (total probability 1 over "
            "an infinite tail), physics (work escaping to infinity), "
            "and the Laplace transform."
        ),
        "how_it_works": (
            "Every improper integral is evaluated as a limit of "
            "proper ones. For an infinite upper limit: write "
            "∫[a,b] f, compute the antiderivative evaluation F(b) - "
            "F(a), then take the limit as b -> infinity - using "
            "L'Hôpital where needed. For a blow-up at c inside "
            "[a,b]: split the integral at c and take one-sided "
            "limits from each side; both must converge "
            "independently. Convergence is then classified, not just "
            "computed: compare against the p-integral benchmark, or "
            "dominate the integrand by a known convergent function "
            "for the comparison test. The p-test is the workhorse: "
            "memorize that x^(-p) at infinity converges iff p > 1 "
            "and at zero (∫[0,1]) converges iff p < 1. Divergent "
            "results are reported as divergence, never as infinity "
            "masquerading as an answer."
        ),
        "key_points": [
            "Improper integrals are defined as limits of proper integrals: infinite bounds or interior blow-ups.",
            "∫[1,∞] x^(-p)dx converges iff p > 1; ∫[0,1] x^(-p)dx converges iff p < 1.",
            "The comparison test transfers convergence from a dominating known integral.",
            "A blow-up inside the interval splits the integral; both halves must converge.",
            "Infinite area can be finite (1/x^2) or genuinely infinite (1/x) - the limit decides.",
        ],
        "requirements": [
            "Antiderivative evaluation and limit computation, including L'Hôpital.",
            "Inequality reasoning for the comparison test.",
            "One-sided limits at points of discontinuity.",
        ],
        "standards": [
            "The limit definition is written out before evaluation - no direct 'plugging in' of infinity.",
            "Convergence vs divergence is stated as the conclusion, with the test cited.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: improper integrals as his Signature horizon-gazing - "
            "measuring areas that run past the edge of the map, and finding some of "
            "them finite."
        ),
        "demo_kind": "calc_improper",
    },
    {
        "key": "area_between",
        "name": "Area Between Curves",
        "group": "Applications of Integrals",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The definite integral finds more than area under one "
            "curve: it finds area trapped between two. If f(x) >= "
            "g(x) on [a,b], the region between them has area "
            "∫[a,b] (f - g)dx - slice vertically, each slice a "
            "rectangle of height (top - bottom), and integrate. For "
            "y = x and y = x^2 on [0,1], the line is on top, and "
            "the area is ∫(x - x^2)dx = 1/6. The method generalizes: "
            "find the intersection points (they become the limits), "
            "determine which curve is on top on each subinterval "
            "(split the integral wherever they cross), and integrate "
            "the difference. When curves are better described as "
            "functions of y - x = g(y) on the right, x = h(y) on the "
            "left - slice horizontally and integrate with respect to "
            "y: ∫(right - left)dy. Consumer surplus in economics, "
            "the area between supply and demand curves, is exactly "
            "this computation wearing business clothes."
        ),
        "how_it_works": (
            "Area between curves is a four-step assembly. First, "
            "find intersection points by solving f(x) = g(x); these "
            "are the integration limits - sketch to see the region. "
            "Second, test which function is on top between "
            "intersections (evaluate at a sample point); wherever "
            "the top changes, split into separate integrals. Third, "
            "integrate (top - bottom)dx over each piece - or, if "
            "the region is y-simple, rewrite as functions of y and "
            "integrate (right - left)dy. Fourth, add the pieces; "
            "area is always positive, so a negative result means "
            "top and bottom were swapped. The choice between dx and "
            "dy slicing is strategic: pick the slicing that avoids "
            "splitting the region into many pieces. Symmetry and "
            "known antiderivative forms keep the computation short."
        ),
        "key_points": [
            "Area between curves: ∫(top - bottom)dx over the interval where they enclose a region.",
            "Intersections become limits; split the integral wherever the top curve changes.",
            "Horizontal slicing ∫(right - left)dy suits regions described naturally as functions of y.",
            "Area is positive by definition - a negative answer signals a top/bottom swap.",
            "Applications: consumer/producer surplus, material cross-sections, enclosed regions generally.",
        ],
        "requirements": [
            "Solving f(x) = g(x) for intersection points.",
            "Definite integration via the fundamental theorem.",
            "Choosing dx vs dy slicing from the region's shape.",
        ],
        "standards": [
            "Intersections are computed, not eyeballed, and shown as the limits.",
            "The top/bottom (or right/left) determination is justified by a test point.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: area between curves as his Signature land survey - "
            "measuring the territory two functions enclose between them."
        ),
        "demo_kind": "calc_area",
    },
    {
        "key": "volumes",
        "name": "Volumes of Revolution: Disks, Washers, and Shells",
        "group": "Applications of Integrals",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Revolve a plane region around an axis and it sweeps out "
            "a solid; calculus computes its volume by slicing. The "
            "disk method: revolve y = f(x) around the x-axis and each "
            "vertical slice becomes a disk of radius f(x), volume "
            "pi*[f(x)]^2 dx - integrate to get V = ∫pi*f(x)^2 dx. "
            "Revolving the region between two curves gives washers: "
            "outer radius minus inner radius, V = ∫pi*(R^2 - r^2)dx. "
            "The shell method slices the other way: cylindrical "
            "shells of radius x, height f(x), thickness dx have "
            "volume 2*pi*x*f(x)dx - ideal when revolving around the "
            "y-axis or when the disk setup would need many pieces. "
            "The sphere's volume 4/3*pi*r^3 falls out of disks in one "
            "line, which is both a check on the method and a "
            "reminder that calculus reproduces the classical "
            "formulas. Choosing disks vs shells is the whole art: "
            "pick the slicing that keeps the radius and height "
            "expressible without splitting."
        ),
        "how_it_works": (
            "Volume problems are solved by choosing the slice. "
            "First, sketch the region and the axis of revolution. "
            "Second, decide: if slices perpendicular to the axis "
            "produce disks or washers with easily written radii, use "
            "disks/washers with V = ∫pi*(R^2 - r^2)dx (or dy); if "
            "slices parallel to the axis are cleaner - typically "
            "when revolving around a vertical axis a region described "
            "in x - use shells with V = ∫2*pi*(radius)(height)dx. "
            "Third, write radius and height as functions of the "
            "integration variable, being careful with shifts when "
            "the axis is not a coordinate axis (radius = distance "
            "from the slice to the axis). Fourth, integrate and "
            "simplify. Sanity checks: the sphere via disks must give "
            "4/3*pi*r^3; dimensions must work out to length^3."
        ),
        "key_points": [
            "Disk: V = ∫pi*[f(x)]^2 dx; washer: V = ∫pi*(R^2 - r^2)dx for regions between curves.",
            "Shell: V = ∫2*pi*(radius)(height)dx - slices parallel to the axis of revolution.",
            "Shifted axes change the radius formula: radius is distance from slice to axis.",
            "Choose the method whose radius/height stay expressible without splitting the region.",
            "The sphere's 4/3*pi*r^3 via disks is the canonical sanity check.",
        ],
        "requirements": [
            "Setting up definite integrals from geometric descriptions.",
            "Distance-from-axis reasoning for shifted axes.",
            "Integrating powers and polynomials fluently.",
        ],
        "standards": [
            "The slice choice (disk/washer/shell) is justified by the region's geometry.",
            "Radius and height are written as explicit functions before integrating.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: volumes of revolution as his Signature pottery wheel - "
            "a flat region spun into a solid, the integral measuring the clay."
        ),
        "demo_kind": "calc_volumes",
    },
    {
        "key": "arclength_work",
        "name": "Arc Length, Surface Area, and Work",
        "group": "Applications of Integrals",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Integrals measure more than area and volume. Arc length: "
            "the length of y = f(x) from a to b is ∫sqrt(1 + "
            "(f')^2)dx - each infinitesimal segment is a hypotenuse "
            "sqrt(dx^2 + dy^2), and the integral adds them. Revolve "
            "that curve around an axis and the surface area follows: "
            "2*pi*∫(radius)*sqrt(1 + (f')^2)dx, each band a thin "
            "frustum. Work: a variable force F(x) pushing along x "
            "from a to b does W = ∫F(x)dx - constant force gives the "
            "familiar force-times-distance, and the integral extends "
            "it to springs (F = kx, so W = (1/2)kx^2), gravity over "
            "distance, and pumps lifting fluid (weight density times "
            "volume times lift height, integrated layer by layer). "
            "Hydrostatic force on a dam is the same pattern: pressure "
            "grows with depth, so force = ∫(pressure at depth)*(strip "
            "width) d(depth). One template - integrate (density of "
            "the quantity)*(geometric slice) - measures length, "
            "area, work, force, and mass."
        ),
        "how_it_works": (
            "Each application follows the slice-and-integrate "
            "template with its own density. Arc length: compute "
            "f'(x), form sqrt(1 + (f')^2), integrate - the "
            "antiderivative is often hard, so recognize when the "
            "curve is a line or circle arc (known lengths) versus "
            "genuinely needing the integral. Surface area: multiply "
            "the arc-length density by 2*pi*(radius), where radius "
            "is the distance from the curve to the axis of "
            "revolution. Work: write the force as a function of "
            "position - for a spring F = kx measured from natural "
            "length; for pumping, each horizontal slice at depth h "
            "has weight (density * area * thickness) and must be "
            "lifted (surface height - h), so dW = weight * lift "
            "distance. Hydrostatic force: pressure = (weight "
            "density)*(depth), times strip area, integrated over "
            "depth. Units are checked at the end: length, area, "
            "and energy (force*distance) respectively."
        ),
        "key_points": [
            "Arc length: ∫sqrt(1 + (f')^2)dx - infinitesimal hypotenuses summed.",
            "Surface of revolution: 2*pi*∫(radius)*sqrt(1 + (f')^2)dx.",
            "Work by variable force: W = ∫F(x)dx; springs give (1/2)kx^2.",
            "Pumping work and hydrostatic force integrate (density)*(slice)*(distance or depth).",
            "One template - integrate a density over geometric slices - serves length, area, work, and force.",
        ],
        "requirements": [
            "The Pythagorean infinitesimal: ds^2 = dx^2 + dy^2.",
            "Force, weight density, and pressure relationships from basic physics.",
            "Setting up integrals from physical descriptions.",
        ],
        "standards": [
            "The slice, its density, and its geometric measure are each identified before integrating.",
            "Final units are stated and checked (length, area, energy).",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: arc length and work as his Signature tape measure and "
            "dynamometer - the integral sizing curves and weighing effort."
        ),
        "demo_kind": "calc_arclen",
    },
    {
        "key": "sequences",
        "name": "Sequences",
        "group": "Sequences and Series",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A sequence is an ordered list of numbers a_1, a_2, a_3, "
            "... - the discrete cousin of a function, defined on the "
            "integers instead of the reals. The question is always "
            "convergence: do the terms settle toward a limit, or do "
            "they wander forever? The sequence 1/n converges to 0; "
            "(-1)^n diverges by oscillation; n^2 diverges to "
            "infinity; (1 + 1/n)^n converges to e, the definition of "
            "one of mathematics' great constants. Because sequences "
            "are functions of n, limit laws and L'Hôpital (applied "
            "to the continuous version) carry over. Bounded monotone "
            "sequences always converge - an increasing sequence with "
            "a ceiling cannot escape to infinity, so it must settle "
            "- and this theorem proves convergence where no formula "
            "for the limit exists, as with recursively defined "
            "sequences like Newton's method iterates. Sequences are "
            "the atoms of series: a series converges exactly when "
            "its sequence of partial sums converges."
        ),
        "how_it_works": (
            "Analyzing a sequence means finding its long-term "
            "behavior. First, write several terms to see the "
            "pattern - growth, decay, oscillation, or chaos. "
            "Second, compute the limit as n -> infinity using the "
            "continuous analog: treat a_n as f(n), apply limit "
            "laws, divide by highest powers, or use L'Hôpital on "
            "f(x). If the limit exists and is finite, the sequence "
            "converges to it. Third, when no closed form exists "
            "(recursive definitions), test monotonicity and "
            "boundedness: prove by induction the sequence is "
            "increasing and bounded above (or decreasing and "
            "bounded below), then invoke the monotone convergence "
            "theorem. Fourth, for alternating sequences, check "
            "whether the magnitude shrinks to zero. Numerical "
            "experimentation - computing a_10, a_100, a_1000 - "
            "suggests the answer, but the proof is the limit "
            "computation or the monotonicity argument."
        ),
        "key_points": [
            "A sequence converges if its terms approach a finite limit as n -> infinity.",
            "(1 + 1/n)^n -> e: sequences define fundamental constants.",
            "Limit laws and L'Hôpital apply via the continuous analog f(n).",
            "Bounded monotone sequences always converge - the key existence theorem.",
            "Series convergence is defined through the sequence of partial sums.",
        ],
        "requirements": [
            "Limit computation, including L'Hôpital for n -> infinity forms.",
            "Induction for monotonicity and boundedness proofs.",
            "Reading long-term behavior from formulas and from computed terms.",
        ],
        "standards": [
            "Convergence claims include the limit value or cite the monotone convergence theorem.",
            "Recursive sequences are analyzed by monotonicity/boundedness, not by guessing.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: sequences as his Signature countdown - term after term "
            "marching toward a limit, or marching off the edge of the world."
        ),
        "demo_kind": "calc_sequences",
    },
    {
        "key": "series_tests",
        "name": "Series and the Convergence Tests",
        "group": "Sequences and Series",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "An infinite series Σa_n is the sum of infinitely many "
            "terms - and the miracle is that such sums can be "
            "finite. The series converges exactly when its partial "
            "sums S_N = a_1 + ... + a_N approach a limit. The "
            "geometric series Σr^n converges to 1/(1-r) for |r| < 1 "
            "and diverges otherwise - the model for all comparison. "
            "The p-series Σ1/n^p converges iff p > 1; the harmonic "
            "series Σ1/n (p = 1) diverges, though agonizingly "
            "slowly. Since most series cannot be summed in closed "
            "form, the convergence tests decide convergence without "
            "finding the sum: the divergence test (terms must -> 0), "
            "the integral test (compare with ∫f), comparison and "
            "limit comparison (benchmark against known series), the "
            "ratio test (factorials and exponentials), the root test "
            "(nth powers), and the alternating series test "
            "(decreasing magnitudes -> 0 guarantees convergence, "
            "with error bounded by the first omitted term). Choosing "
            "the right test is the skill; the tests are the "
            "instruments."
        ),
        "how_it_works": (
            "Testing a series is a diagnostic flowchart. First, "
            "check the divergence test: if a_n does not approach 0, "
            "the series diverges - done. Second, identify the "
            "family: geometric (ratio of successive terms constant), "
            "p-series (power of n in the denominator), telescoping "
            "(terms cancel in partial sums) - these have known "
            "verdicts. Third, for positive-term series, match the "
            "dominant behavior: factorials or exponentials suggest "
            "the ratio test; nth powers suggest the root test; a "
            "resemblance to 1/n^p suggests limit comparison with a "
            "p-series; a decreasing continuous analog suggests the "
            "integral test. Fourth, for alternating series, verify "
            "decreasing magnitudes tending to zero and invoke the "
            "alternating series test, with the remainder bounded by "
            "the first dropped term. The verdict is always "
            "convergence or divergence - the sum itself usually "
            "stays unknown, approximated by partial sums."
        ),
        "key_points": [
            "A series converges iff its partial sums converge; the sum is the limit of partial sums.",
            "Geometric Σr^n converges (|r|<1) to 1/(1-r); p-series Σ1/n^p converges iff p > 1.",
            "Divergence test first: if terms don't -> 0, divergence is immediate.",
            "Ratio test for factorials/exponentials; root test for nth powers; comparison for look-alikes.",
            "Alternating series with decreasing-to-zero magnitudes converge, with error bounded by the first omitted term.",
        ],
        "requirements": [
            "Sequence limits, especially factorial and exponential growth rates.",
            "Improper integrals for the integral test.",
            "Inequality reasoning for comparison tests.",
        ],
        "standards": [
            "The divergence test is checked before any other test.",
            "The chosen test's hypotheses are verified explicitly, not assumed.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: convergence tests as his Signature assay kit - each test "
            "a different acid revealing whether an infinite sum holds together."
        ),
        "demo_kind": "calc_series",
    },
    {
        "key": "taylor_maclaurin",
        "name": "Taylor and Maclaurin Series: Approximating Functions",
        "group": "Sequences and Series",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Taylor series represent functions as infinite "
            "polynomials: f(x) = Σ f^(n)(a)/n! * (x-a)^n. The "
            "coefficients are the derivatives at a single point, "
            "so the whole function - globally - is encoded in its "
            "local behavior. Centered at a = 0 the series is called "
            "a Maclaurin series: e^x = Σx^n/n!, sin x = x - x^3/3! "
            "+ x^5/5! - ..., cos x = 1 - x^2/2! + ..., each "
            "converging for all x. Truncating after N terms gives "
            "the Taylor polynomial, the best Nth-degree "
            "approximation near a, with Taylor's inequality bounding "
            "the error by M|x-a|^(N+1)/(N+1)!. This is how "
            "calculators compute sin and e^x: they evaluate "
            "polynomials, because polynomials need only addition "
            "and multiplication. Series can be differentiated and "
            "integrated term by term inside their interval of "
            "convergence, turning hard integrals like ∫e^(-x^2)dx "
            "into easy termwise integrations."
        ),
        "how_it_works": (
            "Building a Taylor series is mechanical: compute the "
            "derivatives f(a), f'(a), f''(a), ..., divide the nth by "
            "n!, and assemble Σ f^(n)(a)/n! (x-a)^n. Recognize the "
            "famous Maclaurin series on sight - e^x, sin x, cos x, "
            "1/(1-x), ln(1+x), arctan x - and derive new ones by "
            "substitution (e^(-x^2) from e^x with -x^2), "
            "differentiation, or integration of known series. For "
            "approximation, truncate: choose N so Taylor's "
            "inequality guarantees the needed accuracy, with M a "
            "bound on the (N+1)th derivative. Convergence of the "
            "full series is checked with the ratio test, which also "
            "reveals the radius. The remainder estimate is what "
            "makes Taylor polynomials trustworthy engineering tools "
            "rather than hopeful guesses."
        ),
        "key_points": [
            "Taylor series: f(x) = Σ f^(n)(a)/n! (x-a)^n - local derivatives encode the global function.",
            "Maclaurin series (a=0) for e^x, sin x, cos x converge everywhere; memorize them.",
            "Truncation gives Taylor polynomials; Taylor's inequality bounds the approximation error.",
            "New series come from substitution, termwise differentiation, and termwise integration of known ones.",
            "This is how hardware computes transcendental functions: polynomials need only + and *.",
        ],
        "requirements": [
            "Higher-order derivatives computed reliably.",
            "The ratio test for radius of convergence.",
            "Factorial manipulation and inequality bounding.",
        ],
        "standards": [
            "The center a is stated; remainder bounds accompany every numerical approximation.",
            "New series derived from known ones name the operation (substitution, differentiation, integration).",
        ],
        "citations": [C_STEWART, C_SPIVAK],
        "sig_lens": (
            "Signature edition: Taylor series as his Signature Rosetta Stone - the "
            "derivatives at one point translating into the whole function everywhere."
        ),
        "demo_kind": "calc_taylor",
    },
    {
        "key": "power_series",
        "name": "Power Series",
        "group": "Sequences and Series",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A power series Σc_n (x-a)^n is an infinite polynomial "
            "with a personality: it converges on an interval and "
            "diverges outside it. The ratio test finds the radius of "
            "convergence R - the distance from the center a within "
            "which the series converges absolutely. Inside "
            "(a-R, a+R) the series defines a genuine function, "
            "differentiable and integrable term by term; at the "
            "endpoints x = a ± R each endpoint must be tested "
            "individually, since behavior there varies series by "
            "series. The interval of convergence is the series' "
            "domain of legitimacy. Power series multiply, "
            "differentiate, and integrate like polynomials within "
            "that interval, which makes them the working medium for "
            "solving differential equations by series, evaluating "
            "impossible integrals, and defining new functions "
            "(Bessel functions, the error function erf, all begin "
            "life as power series). Taylor series are the special "
            "case where the coefficients come from a function's "
            "derivatives; power series are the general setting."
        ),
        "how_it_works": (
            "Analyzing a power series starts with the ratio test "
            "applied to |c_n (x-a)^n|: the limit L determines "
            "convergence where L < 1, which rearranges to |x - a| "
            "< R with R = 1/limsup|c_(n+1)/c_n|. Inside the open "
            "interval, convergence is absolute and termwise "
            "operations are legal. Then test the endpoints: "
            "substitute x = a + R and x = a - R and run the "
            "ordinary series tests (alternating, p-series, "
            "divergence) on the resulting numerical series. The "
            "collected verdicts give the interval of convergence - "
            "open, closed, half-open, a single point, or the whole "
            "line. Within it, differentiate or integrate term by "
            "term to generate related series; the radius is "
            "preserved (endpoints may change). Radius arithmetic - "
            "adding series keeps the smaller radius - governs "
            "combinations."
        ),
        "key_points": [
            "A power series converges absolutely inside its radius R and diverges outside it.",
            "The ratio test computes R; endpoints x = a ± R are tested individually with series tests.",
            "Inside the interval, termwise differentiation and integration are legal.",
            "The interval of convergence is the series' domain: open, closed, half-open, a point, or all reals.",
            "Taylor series are power series whose coefficients are f^(n)(a)/n!; power series are the general setting.",
        ],
        "requirements": [
            "The ratio test applied with |x - a| as a parameter.",
            "Endpoint analysis with alternating/p-series/divergence tests.",
            "Termwise operations justified by absolute convergence inside R.",
        ],
        "standards": [
            "R is computed by the ratio test; both endpoints are tested and reported.",
            "The interval is stated in interval notation with the endpoint verdicts.",
        ],
        "citations": [C_STEWART, C_APOSTOL],
        "sig_lens": (
            "Signature edition: power series as his Signature territory - a radius of "
            "convergence marking how far from home the infinite polynomial can be trusted."
        ),
        "demo_kind": "calc_powerseries",
    },
    {
        "key": "parametric_polar",
        "name": "Parametric Equations and Polar Calculus",
        "group": "Parametric and Polar",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Some curves are best described by a third variable: "
            "parametric equations x = x(t), y = y(t) trace a path as "
            "t varies - the trajectory of a projectile, a cycloid "
            "rolled by a wheel, any motion with a clock. The "
            "derivative dy/dx = (dy/dt)/(dx/dt) divides the rates, "
            "giving the tangent slope without eliminating t; the "
            "second derivative needs the quotient-style formula with "
            "respect to t. Arc length integrates sqrt((dx/dt)^2 + "
            "(dy/dt)^2)dt - the speed integrated over time is "
            "distance traveled. Polar coordinates (r, θ) describe "
            "curves by radius as a function of angle: cardioids, "
            "roses, spirals, all awkward in x-y. Area in polar "
            "coordinates is (1/2)∫r^2 dθ - each infinitesimal "
            "wedge is a sector of area (1/2)r^2 dθ. Converting "
            "between systems (x = r cos θ, y = r sin θ) lets each "
            "problem live in its natural coordinates."
        ),
        "how_it_works": (
            "Parametric differentiation treats t as the driver: "
            "compute dx/dt and dy/dt, then dy/dx is their ratio; "
            "where dx/dt = 0 (and dy/dt != 0) the tangent is "
            "vertical. The second derivative is d/dt(dy/dx) divided "
            "by dx/dt - differentiate the first derivative with "
            "respect to t, then divide again. Arc length integrates "
            "the speed sqrt((x')^2 + (y')^2) over the t-interval; "
            "surface area uses the same density with the polar or "
            "parametric radius. In polar, sketch r(θ) by sampling "
            "θ, find area with (1/2)∫r^2 dθ between the θ-values "
            "that trace the region exactly once, and find tangent "
            "slopes via dy/dx = (dr/dθ sin θ + r cos θ)/(dr/dθ cos "
            "θ - r sin θ). Intersections in polar need care: the "
            "same point has many (r, θ) names, so solve r_1 = ±r_2 "
            "and check the pole separately."
        ),
        "key_points": [
            "Parametric: dy/dx = (dy/dt)/(dx/dt); arc length integrates speed over t.",
            "Second parametric derivative: differentiate dy/dx in t, divide by dx/dt.",
            "Polar area: (1/2)∫r^2 dθ - infinitesimal sectors summed.",
            "Convert with x = r cos θ, y = r sin θ; work each problem in its natural coordinates.",
            "Polar intersections need ± and pole checks - one point has many coordinate names.",
        ],
        "requirements": [
            "The chain rule in the form dy/dx = (dy/dt)/(dx/dt).",
            "Polar graphing: cardioids, roses, spirals by θ-sampling.",
            "Sector area geometry for the (1/2)r^2 density.",
        ],
        "standards": [
            "The parameter or angle interval tracing the curve exactly once is identified.",
            "Vertical tangents (dx/dt = 0) are located, not glossed over.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: parametric and polar as his Signature alternative maps - "
            "the same territory charted by clock-time and by compass-sweep."
        ),
        "demo_kind": "calc_parampolar",
    },
    {
        "key": "partial_derivatives",
        "name": "Partial Derivatives and the Gradient",
        "group": "Multivariable Calculus",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Functions of several variables - f(x, y) for terrain "
            "height, temperature maps, cost depending on labor and "
            "materials - need derivatives that hold all but one "
            "variable fixed. The partial derivative ∂f/∂x "
            "differentiates with respect to x while treating y as a "
            "constant: for f = x^2*y + sin(xy), ∂f/∂x = 2xy + "
            "y*cos(xy). Geometrically each partial is the slope of "
            "the surface in one coordinate direction. The gradient "
            "∇f = (∂f/∂x, ∂f/∂y) assembles the partials into a "
            "vector that points in the direction of steepest ascent, "
            "with magnitude equal to that steepest slope - the "
            "compass every hill-climber follows. The directional "
            "derivative D_u f = ∇f · u gives the slope in any unit "
            "direction u. Clairaut's theorem says mixed partials "
            "agree (f_xy = f_yx) for smooth functions, so "
            "differentiation order does not matter. Tangent planes "
            "z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b) generalize "
            "tangent lines, and differentials dz = f_x dx + f_y dy "
            "generalize linear approximation."
        ),
        "how_it_works": (
            "Computing partials is single-variable differentiation "
            "with blinders: differentiate with respect to the "
            "target variable, treating every other variable as a "
            "constant number. For f = x^2*y + sin(xy): holding y "
            "fixed, x^2*y differentiates to 2xy and sin(xy) needs "
            "the chain rule to y*cos(xy). Then assemble the "
            "gradient vector and use it: steepest ascent direction "
            "is ∇f/|∇f|, steepest descent its negative, and the "
            "directional derivative in unit direction u is the dot "
            "product ∇f · u. Critical points solve the system f_x "
            "= 0, f_y = 0 simultaneously; the second-derivative "
            "test uses D = f_xx*f_yy - (f_xy)^2 at each critical "
            "point (D > 0 with f_xx > 0: min; f_xx < 0: max; D < 0: "
            "saddle). Tangent planes and linear approximations come "
            "straight from the first partials."
        ),
        "key_points": [
            "Partial derivatives differentiate in one variable while others are held constant.",
            "The gradient ∇f points in the steepest-ascent direction with the steepest slope as magnitude.",
            "Directional derivative D_u f = ∇f · u: slope in any direction.",
            "Clairaut's theorem: mixed partials f_xy = f_yx for smooth functions.",
            "Critical points solve f_x = f_y = 0; the D-test classifies minima, maxima, and saddles.",
        ],
        "requirements": [
            "Single-variable differentiation rules, applied with other variables frozen.",
            "Vector basics: dot product, unit vectors, magnitude.",
            "Solving systems of equations for critical points.",
        ],
        "standards": [
            "Each partial names the variable differentiated and the variables held fixed.",
            "Gradient computations include both direction and magnitude interpretations.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: the gradient as his Signature compass - planted on any "
            "terrain, its needle swinging to the steepest way up."
        ),
        "demo_kind": "calc_partial",
    },
    {
        "key": "multiple_integrals",
        "name": "Multiple Integrals",
        "group": "Multivariable Calculus",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Multiple integrals extend integration to several "
            "variables: the double integral ∬_R f(x,y)dA is the "
            "volume under the surface z = f(x,y) over the region R, "
            "and the triple integral ∭_E f dV accumulates over a "
            "solid. Fubini's theorem computes them as iterated "
            "integrals - integrate in x, then in y - turning a "
            "volume into two ordinary single integrals performed "
            "in sequence. The region's description sets the limits: "
            "a rectangle gives constant limits, while a general "
            "region gives variable limits (y from x^2 to x, then x "
            "from 0 to 1), and the order of integration can be "
            "swapped by re-describing the region. Polar coordinates "
            "simplify circular regions (dA = r dr dθ); cylindrical "
            "and spherical coordinates do the same for solids "
            "(dV = r dz dr dθ, dV = ρ^2 sin φ dρ dφ dθ). Beyond "
            "volume, multiple integrals compute mass (integrate "
            "density), center of mass, moments of inertia, and "
            "average value over a region - one machine, many "
            "physical readings."
        ),
        "how_it_works": (
            "Evaluating a multiple integral is region description "
            "followed by iteration. First, sketch R and decide the "
            "integration order: Type I regions (y between functions "
            "of x) integrate dy first with x-limits outside; Type "
            "II regions reverse it. Write the iterated integral "
            "with inner limits possibly depending on the outer "
            "variable. Second, evaluate inside-out: treat the outer "
            "variable as constant while integrating the inner one, "
            "then integrate the result. Third, consider coordinate "
            "changes: circular regions become rectangular in polar "
            "(x = r cos θ, y = r sin θ, dA = r dr dθ), spherical "
            "symmetry calls for spherical coordinates. Fourth, "
            "interpret: with f = 1 the integral is area or volume; "
            "with f = density it is mass; divided by area/volume it "
            "is the average value. Symmetry often kills terms: odd "
            "functions over symmetric regions integrate to zero."
        ),
        "key_points": [
            "Double integrals give volume under a surface; triple integrals accumulate over solids.",
            "Fubini's theorem: evaluate as iterated single integrals, inside out.",
            "Region description sets the limits; swapping order means re-describing the region.",
            "Polar/cylindrical/spherical coordinates simplify symmetric regions (with their Jacobian factors).",
            "With density as integrand: mass, center of mass, moments of inertia, average value.",
        ],
        "requirements": [
            "Single-variable definite integration, performed twice in sequence.",
            "Describing regions with inequalities and reading bounds from sketches.",
            "Polar, cylindrical, and spherical coordinate conversions.",
        ],
        "standards": [
            "The region is sketched and its Type (I/II) or coordinate choice justified.",
            "Jacobian factors (r, ρ^2 sin φ) are included explicitly in coordinate changes.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: multiple integrals as his Signature volume-filler - "
            "sweeping a region twice over until every drop of space is counted."
        ),
        "demo_kind": "calc_multiple",
    },
    {
        "key": "vector_line_surface",
        "name": "Vector Fields: Line and Surface Integrals",
        "group": "Vector Calculus",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A vector field assigns a vector to every point - wind "
            "velocity across a map, gravitational force through "
            "space, electric field around charges. Line integrals "
            "accumulate a field along a curve: ∫_C F · dr is the "
            "work done by the force field F along the path C, "
            "computed by parametrizing the curve and integrating "
            "F(r(t)) · r'(t) over t. Path independence is the "
            "great divide: for conservative (gradient) fields the "
            "work depends only on the endpoints, and closed-loop "
            "integrals vanish; otherwise the path matters. Surface "
            "integrals extend the idea to surfaces: ∬_S F · dS is "
            "the flux - the net flow of the field through the "
            "surface, positive outward. Parametrizing the surface "
            "gives the normal vector via the cross product of "
            "partial derivatives, and the flux integral measures "
            "what pours through: fluid flow, electric flux, heat "
            "flow. Orientation (which way is 'through') is part of "
            "the data."
        ),
        "how_it_works": (
            "Line integrals parametrize first: write the curve as "
            "r(t) for t in [a,b], compute r'(t), evaluate F along "
            "the curve as F(r(t)), and integrate the dot product "
            "F(r(t)) · r'(t). To test conservativeness, check the "
            "cross-partial condition (P_y = Q_x in the plane) and "
            "then find the potential function f with ∇f = F by "
            "integrating components; work becomes f(end) - "
            "f(start). Surface integrals parametrize the surface "
            "as r(u,v), compute the normal n = r_u × r_v "
            "(oriented as required), and integrate F(r(u,v)) · n "
            "over the parameter domain. For graphs z = g(x,y) the "
            "normal simplifies to (-g_x, -g_y, 1). Flux sign is "
            "checked against the stated orientation - outward for "
            "closed surfaces by convention."
        ),
        "key_points": [
            "Line integral ∫_C F · dr: work of a field along a curve, via parametrization.",
            "Conservative fields are gradients: work is path-independent, closed loops give zero.",
            "Surface integral ∬_S F · dS: flux, the net flow of a field through a surface.",
            "Parametrization supplies the tangent (curves) or normal (surfaces) for the dot product.",
            "Orientation is data: flux sign depends on the chosen normal direction.",
        ],
        "requirements": [
            "Parametrizing curves and surfaces.",
            "Dot and cross products, including the geometric meaning of the normal.",
            "Recognizing gradient fields and finding potential functions.",
        ],
        "standards": [
            "Parametrizations state their parameter intervals explicitly.",
            "Conservative-field claims are verified by the cross-partial test.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: line and surface integrals as his Signature flow-meters - "
            "measuring work along every path and flux through every skin."
        ),
        "demo_kind": "calc_vector",
    },
    {
        "key": "big_theorems",
        "name": "Green's, Stokes', and the Divergence Theorems",
        "group": "Vector Calculus",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The three great theorems of vector calculus are the "
            "fundamental theorem grown up: each equates an integral "
            "over a boundary with an integral over the interior. "
            "Green's theorem: the circulation ∮_C F · dr around a "
            "closed plane curve equals the double integral of the "
            "microscopic circulation (Q_x - P_y) over the enclosed "
            "region - the whirl inside adds up to the flow around "
            "the edge. Stokes' theorem lifts this to surfaces: "
            "circulation around the boundary curve equals the flux "
            "of curl F through the surface - it turns hard boundary "
            "integrals into easier surface integrals and vice versa. "
            "The divergence theorem: the outward flux ∯_S F · dS "
            "through a closed surface equals the triple integral of "
            "div F over the enclosed volume - what pours out equals "
            "the total sourced inside. Together with the gradient "
            "theorem (work = potential difference), they form a "
            "complete dictionary between boundaries and interiors, "
            "the machinery behind Maxwell's equations and fluid "
            "dynamics."
        ),
        "how_it_works": (
            "Applying each theorem is a choice of the easier side. "
            "Green's: given a closed curve integral ∮P dx + Q dy, "
            "compute Q_x - P_y and integrate over the enclosed "
            "region - or go the other way to compute a hard area "
            "integral from an easy boundary (area = (1/2)∮x dy - y "
            "dx). Stokes': parametrize the boundary curve or the "
            "surface, whichever integral is simpler; compute curl F "
            "and dot with the surface normal, checking the "
            "right-hand-rule orientation match between curve and "
            "surface. Divergence: for flux through a closed surface, "
            "compute div F = P_x + Q_y + R_z and integrate over the "
            "volume - one triple integral replacing a parametrized "
            "surface. Orientation is the perennial trap: Green's "
            "needs counterclockwise, Stokes' needs the "
            "right-hand rule, divergence needs outward normals. "
            "Each application states the orientation check."
        ),
        "key_points": [
            "Green's: circulation around a closed curve = double integral of (Q_x - P_y) over the region.",
            "Stokes': boundary circulation = flux of curl through the surface.",
            "Divergence: outward flux through a closed surface = triple integral of div F over the volume.",
            "Each theorem trades a boundary integral for an interior one (or reverse) - pick the easier side.",
            "Orientation rules: counterclockwise (Green), right-hand rule (Stokes), outward normal (divergence).",
        ],
        "requirements": [
            "Curl and divergence computation from a vector field.",
            "Line, surface, double, and triple integrals from earlier records.",
            "Orientation discipline: checking normal/curve direction every time.",
        ],
        "standards": [
            "The orientation check is stated explicitly for every application.",
            "Both sides of the theorem are identified before choosing which to evaluate.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: the great theorems as his Signature ledger - every boundary "
            "balanced against its interior, nothing created or destroyed in the accounting."
        ),
        "demo_kind": "calc_theorems",
    },
    {
        "key": "first_order_de",
        "name": "First-Order Differential Equations",
        "group": "Differential Equations",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A differential equation is an equation involving "
            "derivatives - the language of laws: Newton's cooling, "
            "population growth, RC circuits, all say how a quantity "
            "changes in terms of its current state. First-order "
            "equations involve only dy/dx. Separable equations split "
            "into g(y)dy = h(x)dx and integrate both sides: dy/dx = "
            "ky gives ln|y| = kx + C, the exponential growth law. "
            "Linear equations dy/dx + P(x)y = Q(x) are solved with "
            "the integrating factor μ = e^∫P dx, which collapses "
            "the left side into a single derivative d/dx(μy). "
            "Direction fields sketch the equation's behavior "
            "without solving: at each (x,y) draw a tick of slope "
            "f(x,y), and solution curves follow the ticks like "
            "iron filings around a magnet. Existence and "
            "uniqueness theory guarantees one solution curve "
            "through each well-behaved point. Applications run "
            "everywhere: mixing tanks, cooling bodies, logistic "
            "populations with carrying capacity, continuously "
            "compounded interest."
        ),
        "how_it_works": (
            "Solving first-order equations follows type "
            "recognition. Separable: algebraically separate the "
            "variables to opposite sides with their differentials, "
            "integrate both sides, solve for y, and apply the "
            "initial condition to fix C. Linear: write in standard "
            "form y' + P(x)y = Q(x), compute μ = e^∫P(x)dx, "
            "multiply through so the left becomes d/dx(μy), "
            "integrate both sides, divide by μ. Direction fields "
            "are drawn by evaluating f(x,y) on a grid and drawing "
            "short slope segments - solution curves are then "
            "sketched tangent to the field, and equilibrium "
            "solutions (where f = 0) appear as horizontal "
            "attractors or repellers. Every solution is verified "
            "by differentiating it and substituting back into the "
            "original equation with its initial condition."
        ),
        "key_points": [
            "Separable equations: split variables, integrate both sides - dy/dx = ky yields exponentials.",
            "Linear equations: integrating factor μ = e^∫P dx collapses the left side to d/dx(μy).",
            "Direction fields reveal solution behavior without solving; equilibria show as horizontal lines.",
            "Initial conditions select one curve from the family - existence and uniqueness guarantee it.",
            "Models: growth/decay, Newton's cooling, mixing, logistic populations, RC circuits.",
        ],
        "requirements": [
            "Integration fluency: both sides of a separated equation must be integrable.",
            "Recognizing separable vs linear form on sight.",
            "Reading slope fields and equilibrium behavior.",
        ],
        "standards": [
            "The equation type is identified before the solution method is chosen.",
            "Solutions are verified by substitution into the original equation and initial condition.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: first-order equations as his Signature weather vanes - "
            "each point of the plane holding a tiny arrow, the solution the wind's path."
        ),
        "demo_kind": "calc_de1",
    },
    {
        "key": "second_order_laplace_numeric",
        "name": "Second-Order Equations, Laplace Transforms, and Numerical Methods",
        "group": "Differential Equations",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Second-order equations - involving y'' - govern "
            "oscillation: springs, pendulums, circuits, buildings in "
            "wind. Constant-coefficient linear equations ay'' + "
            "by' + cy = 0 are solved via the characteristic "
            "equation ar^2 + br + c = 0: distinct real roots give "
            "exponentials, repeated roots gain a factor of t, "
            "complex roots give sines and cosines - damped, "
            "undamped, or growing according to the real part. The "
            "Laplace transform L{f}(s) = ∫[0,∞] e^(-st)f(t)dt "
            "converts differential equations into algebra: "
            "derivatives become multiplication by s (minus initial "
            "values), so the equation is solved for Y(s) and "
            "inverted back to y(t) - ideal for circuits and "
            "control systems with switching inputs. When no "
            "closed form exists, numerical methods take over: "
            "Euler's method steps along the direction field "
            "(y_{n+1} = y_n + h*f), improved by Heun and "
            "Runge-Kutta; Simpson's rule integrates with "
            "parabolic accuracy O(h^4). Analysis (series and "
            "transforms) and numerics together solve essentially "
            "every equation the world writes down."
        ),
        "how_it_works": (
            "Second-order constant-coefficient equations start "
            "with the characteristic equation: solve ar^2 + br + c "
            "= 0 and read the root pattern - real distinct, "
            "repeated, or complex - to write the homogeneous "
            "solution; undetermined coefficients or variation of "
            "parameters handle forcing terms. Laplace transforms "
            "attack from the other side: transform both sides "
            "(L{y'} = sY - y(0), L{y''} = s^2 Y - sy(0) - y'(0)), "
            "solve the resulting algebraic equation for Y(s), "
            "and invert via partial fractions and known transform "
            "pairs. Numerically, Euler's method marches y_{n+1} = "
            "y_n + h*f(x_n, y_n) with error O(h); halving h "
            "quarters the error of Heun's method (O(h^2)) and "
            "divides Runge-Kutta's by 16 (O(h^4)). Simpson's rule "
            "∫ ≈ (h/3)(f_0 + 4f_1 + 2f_2 + ...) integrates with "
            "O(h^4) accuracy. Method choice balances accuracy "
            "against step cost, verified against known exact "
            "solutions."
        ),
        "key_points": [
            "Characteristic equation ar^2+br+c=0 classifies: real roots -> exponentials; complex -> oscillation; repeated -> t factor.",
            "Laplace transform converts derivatives to algebra: solve for Y(s), invert via partial fractions.",
            "Euler's method steps along the direction field; Heun and Runge-Kutta refine the stepping.",
            "Simpson's rule integrates with O(h^4) accuracy via parabolic segments.",
            "Analysis (characteristic/Laplace) and numerics (Euler/Simpson) together cover nearly every equation.",
        ],
        "requirements": [
            "First-order methods and the partial-fractions technique for Laplace inversion.",
            "Complex roots and Euler's formula for the oscillatory case.",
            "Error-order thinking: how accuracy improves as step size shrinks.",
        ],
        "standards": [
            "Root patterns are classified explicitly before the solution form is written.",
            "Numerical results are verified against an exact solution where one exists.",
        ],
        "citations": [C_STEWART, C_STRANG],
        "sig_lens": (
            "Signature edition: second-order equations and numerics as his Signature "
            "oscillation lab - springs singing, transforms translating, and step-by-step "
            "marching when the formulas run out."
        ),
        "demo_kind": "calc_de2num",
    },
]

assert len(ENTRIES) == 36, "expected 36 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries must be in ladder order"
tiers = [e["ladder_tier"] for e in ENTRIES]
assert tiers == sorted(tiers, key=lambda t: {"foundations": 0, "compounded": 1, "advanced": 2}[t]), "tiers out of order"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier", "description",
              "how_it_works", "key_points", "requirements", "standards",
              "citations", "sig_lens", "demo_kind"):
        assert k in e, "missing %s" % k
    assert len(e["key_points"]) == 5 and len(e["requirements"]) == 3 and len(e["standards"]) == 2
    assert len(e["citations"]) == 2 and len(e["description"]) > 200
