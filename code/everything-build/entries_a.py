#!/usr/bin/env python3
"""PHASE D — Everything databases, entries part A: mathematics, physics,
chemistry, biology, computer science. Each entry:
(key, group, title, desc, points, requirements, standards, citations, demo_kind, src)
Public records are fact-checked established knowledge (src public-harvest);
Signature records are original Signature designs (src signature).
"""

ENTRIES_A = [
# ============================== MATHEMATICS ==============================
("number-systems", "Foundations",
 "Number Systems: From Natural Numbers to Complex Numbers",
 "The number systems build in stages, each solving equations the previous stage could not. "
 "Natural numbers count; integers add zero and negatives so x + 5 = 3 has a solution; rational numbers "
 "as ratios solve 2x = 1; real numbers complete the line so x^2 = 2 lands somewhere; complex numbers "
 "close algebra itself so x^2 = -1 is solvable. The complex plane unites algebra with geometry — "
 "multiplication becomes rotation and scaling — and the fundamental theorem of algebra guarantees every "
 "polynomial equation has its full set of roots among the complex numbers.",
 ["Naturals, integers, rationals, reals, complex numbers: each extends the last",
  "Each extension solves previously unsolvable equations",
  "The complex plane: multiplication as rotation and scaling",
  "Fundamental theorem of algebra: n roots for every degree-n polynomial",
  "Real uses: signal processing, electrical engineering, quantum mechanics"],
 "A reader comfortable with basic arithmetic; sketching a coordinate plane helps for complex numbers.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (number theory and analysis textbooks).",
 "math", "public-harvest"),
("algebraic-structures", "Algebra",
 "Algebraic Structures: Groups, Rings, and Fields",
 "A group is a set with one operation satisfying four rules: closure, associativity, an identity element, "
 "and inverses — the integers under addition are the classic example. A ring adds a second operation, "
 "multiplication, that distributes over the first, as the integers do under addition and multiplication. "
 "A field goes further and demands multiplicative inverses for every nonzero element, which the rational "
 "and real numbers provide. These abstractions let a single proof serve everywhere the axioms hold: "
 "solving equations, the symmetries of molecules, error-correcting codes, and the arithmetic of cryptography.",
 ["Groups: one operation with identity and inverses",
  "Rings: two operations with distributivity",
  "Fields: every nonzero element has a multiplicative inverse",
  "One proof serves every structure satisfying the axioms",
  "Applications: symmetry in physics, cryptography, coding theory"],
 "Familiarity with sets and basic equation solving.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (abstract algebra textbooks).",
 "math", "public-harvest"),
("euclidean-geometry", "Geometry",
 "Euclidean Geometry: Axioms, Proof, and Construction",
 "Euclid's Elements organized geometry around five postulates — including the famous parallel postulate — "
 "and derived hundreds of theorems by pure deduction from them. Straightedge-and-compass constructions make "
 "the axioms physical: bisecting angles, erecting perpendiculars, inscribing regular polygons. The parallel "
 "postulate's independence, settled in the 19th century, opened non-Euclidean geometries that later became "
 "the language of general relativity. Proof — a chain where each step is justified by axioms or earlier "
 "results — remains mathematics' gold standard of certainty.",
 ["Five postulates as the foundation of classical geometry",
  "Straightedge-and-compass constructions realize the axioms",
  "The parallel postulate: independent, not provable from the rest",
  "Non-Euclidean geometry grew from questioning the fifth postulate",
  "Proof as a justified chain of deductions"],
 "Basic plane geometry vocabulary: point, line, angle, triangle.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (Euclid's Elements; geometry textbooks).",
 "math", "public-harvest"),
("differential-calculus", "Calculus & Analysis",
 "Differential Calculus: Limits, Derivatives, and Change",
 "The derivative measures instantaneous rate of change: the slope of the tangent line, found as the limit "
 "of secant slopes as the interval shrinks to zero. Newton and Leibniz built the machinery independently in "
 "the 17th century; the limit concept, rigorized in the 19th, put it on firm ground. The power, product, "
 "quotient, and chain rules turn messy rates into routine computation. Optimization, related rates, and curve "
 "sketching all flow from asking where a function rises, falls, or turns — the derivative's sign and zeros "
 "answer all three.",
 ["Derivative as instantaneous rate of change and tangent slope",
  "Limits made rigorous in the 19th century",
  "Power, product, quotient, and chain rules",
  "Optimization via critical points and sign analysis",
  "Models velocity, growth, and marginal change across science"],
 "Algebra fluency and comfort with functions and graphs.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (calculus and analysis textbooks).",
 "math", "public-harvest"),
("integral-calculus", "Calculus & Analysis",
 "Integral Calculus: Accumulation and the Fundamental Theorem",
 "The definite integral accumulates a quantity: area under a curve, distance traveled from a velocity "
 "function, total output from a production rate. Riemann's formulation as the limit of approximating sums "
 "made the idea precise. The fundamental theorem of calculus binds differentiation and integration as inverse "
 "operations — differentiate an accumulation function and you recover the rate. Substitution and integration "
 "by parts extend the toolkit, and improper integrals handle infinite domains and unbounded functions that "
 "appear throughout physics and probability.",
 ["Definite integral as the limit of approximating sums",
  "Accumulation: area, distance, totals from rates",
  "Fundamental theorem: differentiation and integration are inverses",
  "Substitution and integration by parts",
  "Improper integrals for infinite domains"],
 "Differential calculus: limits and the derivative.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (calculus and analysis textbooks).",
 "math", "public-harvest"),
("probability-theory", "Probability & Statistics",
 "Probability Theory: Axioms, Random Variables, and Distributions",
 "Kolmogorov's 1933 axioms define probability as a measure assigning numbers between 0 and 1 to events, with "
 "the whole sample space measuring exactly 1. Random variables map outcomes to numbers; their distributions "
 "model uncertainty across science — binomial for counts of successes, normal for bell-shaped error, Poisson "
 "for rare events in time or space. Expected value and variance summarize center and spread, while the law of "
 "large numbers and the central limit theorem explain why averages settle down and why the normal curve "
 "appears in so many unrelated measurements.",
 ["Kolmogorov's three axioms as the foundation",
  "Random variables map outcomes to numbers",
  "Binomial, normal, and Poisson distributions",
  "Expected value and variance summarize distributions",
  "Law of large numbers and central limit theorem"],
 "Basic algebra and comfort with functions.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (probability textbooks).",
 "math", "public-harvest"),
("statistical-inference", "Probability & Statistics",
 "Statistical Inference: Estimation and Hypothesis Testing",
 "Inference reasons from samples to populations. Point estimators like the sample mean target population "
 "parameters; confidence intervals quantify the uncertainty around those estimates. Hypothesis testing frames "
 "a null claim, computes how surprising the data would be if the claim held — the p-value — and rejects the "
 "claim when the surprise is too great to be chance. Power, significance level, and effect size together "
 "determine whether a study can actually detect what it seeks, and disciplined inference guards against "
 "mistaking random noise for genuine discovery.",
 ["Point estimation targets population parameters from samples",
  "Confidence intervals quantify estimation uncertainty",
  "Hypothesis tests weigh evidence against a null claim",
  "P-values measure surprise under the null, not truth of the claim",
  "Power and effect size decide what a study can detect"],
 "Probability basics: random variables and distributions.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard statistics literature (inference textbooks).",
 "math", "public-harvest"),
("number-theory", "Number Theory",
 "Number Theory: Primes, Divisibility, and Congruences",
 "Number theory studies the integers' hidden order. Euclid proved there are infinitely many primes, and the "
 "fundamental theorem of arithmetic gives every integer a unique prime factorization. Congruences — arithmetic "
 "modulo n — turn divisibility questions into algebra and underpin modern cryptography: RSA encryption rests "
 "on how hard it is to factor large products of two primes. Diophantine equations, perfect numbers, and the "
 "distribution of primes connect elementary questions to problems that resisted solution for centuries.",
 ["Euclid's proof of infinitely many primes",
  "Unique prime factorization of every integer",
  "Congruences: arithmetic modulo n",
  "RSA cryptography rests on factoring difficulty",
  "Elementary questions leading to deep unsolved problems"],
 "Comfort with integers, factors, and basic proofs.",
 ["ISO 80000-2 (mathematical signs and symbols)"],
 "Standard mathematics literature (number theory textbooks).",
 "math", "public-harvest"),
("sig-coordinate-unification", "Signature Mathematics",
 "Signature Coordinate Unification",
 "A Signature original design that treats every coordinate system — Cartesian, polar, cylindrical, spherical, "
 "and discrete lattice frames — as views of one unified addressing scheme. Instead of converting between "
 "systems with ad-hoc formulas, the design defines a single canonical Signature coordinate record from which "
 "each classical view is derived deterministically. Transformations become lossless round-trips, and mixed "
 "geometry problems (a polar sensor feeding a Cartesian map) resolve in the canonical frame without "
 "accumulated conversion error. Built in the Signature system as an original mathematical instrument.",
 ["One canonical Signature coordinate record underlies all classical systems",
  "Cartesian, polar, cylindrical, spherical derived deterministically",
  "Lossless round-trip transformations between views",
  "Mixed-frame problems resolve in the canonical frame",
  "Deterministic: same input, same canonical record, every run"],
 "Familiarity with at least one coordinate system.",
 ["Signature system conventions; ISO 80000-2 notation"],
 "Original Signature design; classical facts per standard mathematics literature.",
 "math", "signature"),
("sig-prime-lattice", "Signature Mathematics",
 "Signature Prime Lattice Mapping",
 "A Signature original instrument that lays the integers on a geometric lattice and reads prime structure "
 "as visible pattern: multiples form straight rays, primes are the points no ray reaches except through 1 "
 "and themselves, and prime gaps appear as measurable voids. The design pairs the lattice with deterministic "
 "Signature sieving so the map for any range is reproducible exactly. It is a working instrument for exploring "
 "multiplicative structure geometrically — a Signature treatment of number theory's oldest objects, built to "
 "be computed with, not just admired.",
 ["Integers laid on a geometric lattice as the working surface",
  "Multiples as rays; primes as points no ray reaches",
  "Prime gaps readable as measurable voids",
  "Deterministic Signature sieving: reproducible maps",
  "A computable instrument for multiplicative structure"],
 "Number theory basics: primes and divisibility.",
 ["Signature system conventions; ISO 80000-2 notation"],
 "Original Signature design; classical facts per standard mathematics literature.",
 "math", "signature"),
("sig-geometric-construction", "Signature Mathematics",
 "Signature Geometric Construction Engine",
 "A Signature original engine that performs classical straightedge-and-compass constructions as exact "
 "deterministic algorithms: every construction is a program whose steps are provably the Euclidean ones, "
 "with coordinates carried exactly rather than rounded. Angle bisection, perpendiculars, inscribed polygons, "
 "and Apollonian tangencies all execute as verified routines. The engine also flags the classical "
 "impossibilities — trisecting an arbitrary angle, doubling the cube — and explains which axiom boundary "
 "each one crosses. A Signature treatment of constructive geometry as runnable proof.",
 ["Classical constructions as exact deterministic algorithms",
  "Coordinates carried exactly, never rounded mid-construction",
  "Verified routines: bisection, perpendiculars, inscribed polygons",
  "Classical impossibilities detected and explained",
  "Construction as runnable proof"],
 "Euclidean geometry basics.",
 ["Signature system conventions; ISO 80000-2 notation"],
 "Original Signature design; classical facts per standard mathematics literature.",
 "math", "signature"),
("sig-equation-workability", "Signature Mathematics",
 "Signature Equation Workability Framework",
 "A Signature original framework that treats an equation as a machine with a workability verdict: given "
 "variables, domains, and constraints, it determines whether the equation is solvable, approximately solvable, "
 "or structurally unsound — and says exactly which term breaks it. Drawing on the Signature geometry treatment "
 "of known equations, it rewrites alike structures into universal forms so one verified solution pattern serves "
 "a whole family. The flagship pattern applies Signature geometry to the vector cross product, A x B = AB sin(theta), "
 "as the canonical example of an equation made universally workable.",
 ["Equations judged as machines: solvable, approximate, or unsound",
  "Fault isolation: the framework names the breaking term",
  "Alike structures rewritten into universal verified forms",
  "Flagship: vector cross product A x B = AB sin(theta) in Signature geometry",
  "One verified pattern serves a whole equation family"],
 "Algebra fluency; vectors helpful.",
 ["Signature system conventions; ISO 80000-2 notation"],
 "Original Signature design; classical facts per standard mathematics literature.",
 "math", "signature"),
# ============================== PHYSICS ==============================
("newton-laws", "Classical Mechanics",
 "Classical Mechanics: Newton's Laws of Motion",
 "Newton's three laws govern everyday motion. The first: objects keep their velocity unless a net force acts — "
 "inertia. The second: F = ma, force equals mass times acceleration, the workhorse equation of classical "
 "physics. The third: every action has an equal and opposite reaction. Together with universal gravitation, "
 "these laws predict projectile arcs, planetary orbits, and machine behavior with precision that held unchallenged "
 "for two centuries, and they remain the correct engineering description of the macroscopic slow-moving world.",
 ["First law: inertia — velocity persists without net force",
  "Second law: F = ma, the workhorse of classical physics",
  "Third law: equal and opposite reactions",
  "Universal gravitation extends the laws to orbits",
  "Correct engineering description of the macroscopic world"],
 "Basic algebra and the concept of a vector.",
 ["ISO 80000-3 (space and time); SI units"],
 "Standard physics literature (classical mechanics textbooks).",
 "physics", "public-harvest"),
("maxwell-equations", "Electromagnetism",
 "Electromagnetism: Maxwell's Equations",
 "Four equations unify electricity and magnetism: electric charges produce electric fields; no magnetic "
 "monopoles exist; changing magnetic fields induce electric fields; and electric currents plus changing "
 "electric fields produce magnetic fields. Maxwell saw that the equations predict waves traveling at the "
 "speed of light — light itself is an electromagnetic wave. Radio, optics, motors, and generators all follow "
 "from these four statements, making them the most technologically productive equations in physics.",
 ["Electric charges source electric fields",
  "Changing magnetic fields induce electric fields (Faraday)",
  "Currents and changing electric fields source magnetic fields",
  "The equations predict light-speed electromagnetic waves",
  "Foundation of radio, optics, motors, and power systems"],
 "Vector basics and the idea of a field.",
 ["ISO 80000-6 (electromagnetism); SI units"],
 "Standard physics literature (electromagnetism textbooks).",
 "physics", "public-harvest"),
("thermodynamics-laws", "Thermodynamics",
 "Thermodynamics: The Laws of Energy",
 "The zeroth law defines temperature through thermal equilibrium. The first law is energy conservation: energy "
 "is neither created nor destroyed, only converted — heat and work are its transfer modes. The second law "
 "states that entropy, the measure of disorder, never decreases in an isolated system, which is why heat flows "
 "hot to cold and perpetual motion machines are impossible. The third law sets absolute zero as unreachable. "
 "Engines, refrigerators, and the fate of the universe all answer to these four laws.",
 ["Zeroth law: temperature defined by equilibrium",
  "First law: energy is conserved; heat and work convert",
  "Second law: entropy never decreases in isolation",
  "Third law: absolute zero is unreachable",
  "Rules out perpetual motion; governs engines and refrigerators"],
 "Algebra and basic mechanics concepts.",
 ["ISO 80000-5 (thermodynamics); SI units"],
 "Standard physics literature (thermodynamics textbooks).",
 "physics", "public-harvest"),
("special-relativity", "Relativity",
 "Special Relativity: Space, Time, and E=mc^2",
 "Einstein's 1905 theory starts from two postulates: the laws of physics are identical in all inertial frames, "
 "and the speed of light is the same for every observer. The consequences overturn common sense: moving clocks "
 "run slow, moving objects contract, and simultaneity depends on the observer. Mass and energy are two forms of "
 "the same thing, related by E = mc^2. Particle accelerators confirm the predictions daily — fast particles live "
 "longer and weigh more exactly as the theory demands.",
 ["Two postulates: relativity principle and constant light speed",
  "Time dilation: moving clocks run slow",
  "Length contraction at near-light speeds",
  "E = mc^2: mass-energy equivalence",
  "Confirmed daily in particle accelerators"],
 "Algebra; comfort with thought experiments.",
 ["ISO 80000-3 (space and time); SI units"],
 "Standard physics literature (relativity textbooks).",
 "physics", "public-harvest"),
("quantum-mechanics", "Quantum Physics",
 "Quantum Mechanics: Wave Functions and Uncertainty",
 "Quantum mechanics describes nature at atomic scales, where particles behave as waves of probability. The wave "
 "function encodes everything knowable about a system; its squared magnitude gives the probability of finding "
 "the particle at each location. Heisenberg's uncertainty principle sets a fundamental limit: position and "
 "momentum cannot both be known exactly. Superposition, entanglement, and quantized energy levels follow from "
 "the same mathematics — and transistors, lasers, and MRI machines follow from those.",
 ["Wave function encodes probabilities, not certainties",
  "Uncertainty principle: position-momentum trade-off",
  "Quantized energy levels in atoms",
  "Superposition and entanglement",
  "Foundation of transistors, lasers, and MRI"],
 "Basic algebra and probability intuition.",
 ["ISO 80000-10 (atomic and nuclear physics); SI units"],
 "Standard physics literature (quantum mechanics textbooks).",
 "physics", "public-harvest"),
("fluid-dynamics", "Fluids & Waves",
 "Fluid Dynamics: Flow, Pressure, and Viscosity",
 "Fluid dynamics studies liquids and gases in motion. Bernoulli's principle links speed and pressure: faster "
 "flow means lower pressure, the effect behind airplane lift and curveballs. Viscosity measures a fluid's "
 "resistance to flow — honey versus water. The Navier-Stokes equations govern it all, and their turbulence "
 "solutions remain one of mathematics' great unsolved problems. Weather prediction, pipeline design, and "
 "aerodynamics all run on fluid dynamics.",
 ["Bernoulli's principle: speed and pressure trade off",
  "Viscosity as resistance to flow",
  "Laminar versus turbulent flow regimes",
  "Navier-Stokes equations govern all fluid motion",
  "Applications: flight, weather, pipelines, blood flow"],
 "Calculus basics helpful; algebra required.",
 ["ISO 80000-4 (mechanics); SI units"],
 "Standard physics literature (fluid mechanics textbooks).",
 "physics", "public-harvest"),
("wave-physics", "Fluids & Waves",
 "Wave Physics: Oscillation, Interference, and Resonance",
 "A wave carries energy without carrying matter: water waves move energy while water mostly bobs in place. "
 "Frequency, wavelength, and speed obey v = f times lambda. When waves meet, they interfere — crests add, "
 "troughs cancel — producing standing waves in instruments and noise-cancelling headphones alike. Resonance "
 "occurs when a system is driven at its natural frequency, amplifying the response enormously, from playground "
 "swings to bridge-destroying winds to tuned radio circuits.",
 ["Waves transport energy, not matter",
  "v = f times wavelength relates the three wave quantities",
  "Interference: constructive addition, destructive cancellation",
  "Standing waves from confined interference",
  "Resonance amplifies response at natural frequencies"],
 "Algebra and basic trigonometry.",
 ["ISO 80000-7 (light and radiation); SI units"],
 "Standard physics literature (waves and oscillations textbooks).",
 "physics", "public-harvest"),
("standard-model", "Modern Physics",
 "Particle Physics: The Standard Model",
 "The Standard Model catalogs nature's building blocks: six quarks and six leptons make up matter, while "
 "force-carrying bosons — photons, gluons, W and Z — mediate the electromagnetic, strong, and weak forces. "
 "The Higgs boson, confirmed in 2012, explains how particles acquire mass. The model predicts experimental "
 "results to extraordinary precision, yet it is incomplete: it omits gravity, dark matter, and dark energy, "
 "which together dominate the universe's content.",
 ["Matter particles: six quarks and six leptons",
  "Force carriers: photon, gluon, W, Z bosons",
  "Higgs boson explains the origin of mass",
  "Extraordinarily precise experimental predictions",
  "Incomplete: no gravity, dark matter, or dark energy"],
 "Basic quantum and relativity concepts helpful.",
 ["ISO 80000-10 (atomic and nuclear physics); SI units"],
 "Standard physics literature (particle physics references).",
 "physics", "public-harvest"),
("sig-motion-geometry", "Signature Physics",
 "Signature Motion Geometry",
 "A Signature original treatment that describes motion as pure geometry: trajectories become curves in a "
 "Signature configuration space where velocity is the tangent and acceleration the curvature. Projectile arcs, "
 "orbits, and pendulum swings are read as geometric facts rather than computed step by step — the path's shape "
 "carries the physics. The design keeps Newton's laws intact while giving every motion a canonical Signature "
 "geometric record that is deterministic and reproducible. A Signature treatment of mechanics as geometry first, "
 "arithmetic second.",
 ["Motion as curves in Signature configuration space",
  "Velocity as tangent, acceleration as curvature",
  "Trajectories read as geometric facts",
  "Newton's laws preserved in geometric form",
  "Canonical deterministic motion records"],
 "Classical mechanics basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard physics literature.",
 "physics", "signature"),
("sig-field-harmonics", "Signature Physics",
 "Signature Field Harmonics",
 "A Signature original design that treats electric, magnetic, and gravitational fields as harmonic structures "
 "on a shared Signature lattice: field lines become harmonic flows, and sources become the lattice points where "
 "harmony breaks. Maxwell's equations are preserved as the local rules of the lattice, while the global picture "
 "shows field energy as measurable harmonic content. The design gives field problems a geometric working surface "
 "where superposition is literal addition of harmonics — a Signature treatment of field theory.",
 ["Fields as harmonic structures on a Signature lattice",
  "Field lines as harmonic flows; sources as break points",
  "Maxwell's equations as local lattice rules",
  "Field energy readable as harmonic content",
  "Superposition as literal harmonic addition"],
 "Electromagnetism basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard physics literature.",
 "physics", "signature"),
("sig-energy-accounting", "Signature Physics",
 "Signature Energy Accounting",
 "A Signature original framework that tracks energy through any system as strict double-entry bookkeeping: every "
 "joule is debited from one form and credited to another, and the books must balance exactly. Kinetic, "
 "potential, thermal, chemical, and radiative accounts are kept separately, with conversion rules as the "
 "transfer postings. Losses are never 'lost' — they are posted to the thermal account. The design makes the "
 "first law of thermodynamics an auditable ledger, catching modeling errors as imbalances.",
 ["Energy tracked as double-entry bookkeeping",
  "Separate accounts: kinetic, potential, thermal, chemical, radiative",
  "Conversions as transfer postings between accounts",
  "No 'lost' energy: everything posts somewhere",
  "Imbalances flag modeling errors automatically"],
 "Thermodynamics basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard physics literature.",
 "physics", "signature"),
("sig-scale-bridging", "Signature Physics",
 "Signature Scale Bridging: Quantum to Classical",
 "A Signature original design that treats the quantum-to-classical transition as a continuous Signature scale "
 "rather than a mysterious jump: as action grows large compared to Planck's constant, quantum records converge "
 "deterministically onto classical trajectories in the design's bridging frame. Wave functions, uncertainty "
 "bounds, and classical paths are kept as three views of one Signature record, so a problem can be entered at "
 "any scale and read at any other. A Signature treatment of the correspondence principle as working machinery.",
 ["Quantum-to-classical as a continuous Signature scale",
  "Large action limit recovers classical trajectories",
  "Wave, uncertainty, and path views of one record",
  "Problems entered at any scale, read at any other",
  "Correspondence principle as working machinery"],
 "Quantum mechanics and classical mechanics basics.",
 ["Signature system conventions; SI units"],
 "Original Signature design; classical facts per standard physics literature.",
 "physics", "signature"),
# ============================== CHEMISTRY ==============================
("atomic-structure", "General Chemistry",
 "Atomic Structure and the Periodic Table",
 "Atoms consist of a dense nucleus of protons and neutrons surrounded by electrons in quantized shells. The "
 "proton count — the atomic number — defines the element. Mendeleev's periodic table arranges elements by "
 "atomic number so that columns share chemical behavior, because elements in a column have the same outer "
 "electron configuration. Trends across the table — electronegativity, atomic radius, ionization energy — "
 "follow from how tightly the nucleus holds its outer electrons, and they predict how elements will react "
 "before a single experiment is run.",
 ["Nucleus of protons and neutrons; electrons in shells",
  "Atomic number defines the element",
  "Periodic table groups elements by recurring behavior",
  "Trends: electronegativity, radius, ionization energy",
  "Outer electrons determine chemical reactivity"],
 "Basic algebra; comfort with abstract models.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (general chemistry textbooks).",
 "chem", "public-harvest"),
("chemical-bonding", "General Chemistry",
 "Chemical Bonding: Ionic, Covalent, and Metallic",
 "Atoms bond to reach stable electron configurations. Ionic bonds transfer electrons — sodium gives one to "
 "chlorine, forming Na+ and Cl- held by electrostatic attraction in table salt. Covalent bonds share electrons, "
 "as the two hydrogens and oxygen do in water, with polarity arising when sharing is unequal. Metallic bonds "
 "pool electrons across a lattice of positive ions, giving metals their conductivity and malleability. Bond "
 "type predicts melting point, solubility, and conductivity: the structure of matter follows from how electrons "
 "are shared.",
 ["Ionic bonds: electron transfer and electrostatic attraction",
  "Covalent bonds: electron sharing, polar or nonpolar",
  "Metallic bonds: pooled electrons across ion lattices",
  "Bond type predicts physical properties",
  "Octet rule as the organizing tendency"],
 "Atomic structure basics.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (general chemistry textbooks).",
 "chem", "public-harvest"),
("stoichiometry", "General Chemistry",
 "Stoichiometry: Balancing Reactions and the Mole",
 "The mole — 6.022 x 10^23 particles — lets chemists count atoms by weighing them. A balanced chemical equation "
 "conserves every atom: coefficients are chosen so each element appears equally on both sides, as 2H2 + O2 -> "
 "2H2O shows. Stoichiometry converts between grams, moles, and molecules through molar mass, and identifies the "
 "limiting reactant that caps how much product a reaction can make. Percent yield then measures how close the "
 "real reaction came to the theoretical ideal.",
 ["The mole: 6.022 x 10^23 particles as a counting unit",
  "Balanced equations conserve every atom",
  "Molar mass converts grams to moles",
  "Limiting reactant caps the product",
  "Percent yield measures real versus theoretical"],
 "Basic algebra and atomic masses.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (general chemistry textbooks).",
 "chem", "public-harvest"),
("acids-bases", "General Chemistry",
 "Acids, Bases, and the pH Scale",
 "Acids donate protons (H+), bases accept them — the Bronsted-Lowry definition that organizes acid-base "
 "chemistry. The pH scale compresses hydrogen-ion concentration into 0 to 14: each unit is a tenfold change, "
 "so pH 3 is ten times more acidic than pH 4. Neutralization pairs an acid with a base to make water and a "
 "salt. Buffers — weak acid/base pairs — resist pH change and keep blood at 7.4 and ecosystems stable. "
 "Titration measures unknown concentrations by careful neutralization.",
 ["Bronsted-Lowry: acids donate protons, bases accept",
  "pH 0-14; each unit is a tenfold concentration change",
  "Neutralization makes water plus a salt",
  "Buffers resist pH change in blood and nature",
  "Titration determines unknown concentrations"],
 "Basic algebra and logarithms intuition.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (general chemistry textbooks).",
 "chem", "public-harvest"),
("organic-chemistry", "Organic Chemistry",
 "Organic Chemistry: Hydrocarbons and Functional Groups",
 "Organic chemistry is the chemistry of carbon, whose four bonds build chains, rings, and the scaffolds of "
 "life. Hydrocarbons — alkanes, alkenes, alkynes — are the fuel family, from methane to the polymers in "
 "plastics. Functional groups are the reactive neighborhoods: alcohols (-OH), carboxylic acids (-COOH), amines "
 "(-NH2), each with characteristic reactions. Isomers share a formula but differ in structure, sometimes with "
 "dramatically different properties. Reaction mechanisms trace electron flow step by step, turning memorization "
 "into logic.",
 ["Carbon's four bonds build chains, rings, scaffolds",
  "Hydrocarbons: alkanes, alkenes, alkynes",
  "Functional groups define characteristic reactivity",
  "Isomers: same formula, different structure and properties",
  "Mechanisms trace electron flow as logic"],
 "Chemical bonding basics.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (organic chemistry textbooks).",
 "chem", "public-harvest"),
("chemical-kinetics", "Physical Chemistry",
 "Chemical Kinetics: Rates and Mechanisms",
 "Kinetics asks how fast reactions go, not just whether they can. Rate laws relate reaction speed to reactant "
 "concentrations, with orders determined experimentally — the balanced equation does not reveal them. "
 "Temperature speeds reactions per the Arrhenius relationship: more molecules clear the activation-energy "
 "barrier. Catalysts provide alternate pathways with lower barriers and emerge unchanged. Reaction mechanisms — "
 "the elementary steps — must sum to the overall equation and match the observed rate law.",
 ["Rate laws from experiment, not from the balanced equation",
  "Reaction orders describe concentration dependence",
  "Arrhenius: temperature and the activation barrier",
  "Catalysts lower barriers without being consumed",
  "Mechanisms must match the observed rate law"],
 "Algebra; basic calculus intuition helpful.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (physical chemistry textbooks).",
 "chem", "public-harvest"),
("chemical-equilibrium", "Physical Chemistry",
 "Chemical Equilibrium: Le Chatelier's Principle",
 "Many reactions are reversible, and equilibrium is the point where forward and reverse rates match — "
 "concentrations steady, reactions still running. The equilibrium constant K quantifies the balance point from "
 "concentrations. Le Chatelier's principle predicts the response to disturbance: add reactant and the system "
 "shifts toward products; raise temperature and it shifts to absorb the heat. Industrial processes like ammonia "
 "synthesis tune pressure and temperature to push equilibrium where economics wants it.",
 ["Equilibrium: forward and reverse rates equal",
  "Equilibrium constant K quantifies the balance",
  "Le Chatelier: systems oppose imposed changes",
  "Concentration, pressure, temperature as control knobs",
  "Industrial tuning: the Haber ammonia process"],
 "Stoichiometry basics.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (physical chemistry textbooks).",
 "chem", "public-harvest"),
("biochemistry", "Biochemistry",
 "Biochemistry: Proteins, Enzymes, and Metabolism",
 "Biochemistry is chemistry inside living things. Proteins — chains of amino acids folded into precise shapes — "
 "do the work: enzymes catalyze reactions, cutting activation barriers by orders of magnitude, each specific to "
 "its substrate like a lock to a key. Metabolism is the managed burn of fuel: glycolysis and the citric acid "
 "cycle extract energy from glucose, storing it as ATP, the cell's energy currency. DNA stores the instructions; "
 "proteins execute them. Denaturation — unfolding by heat or pH — destroys function by destroying shape.",
 ["Proteins: amino-acid chains folded into working shapes",
  "Enzymes as specific catalysts lowering activation barriers",
  "Metabolism extracts energy as ATP",
  "DNA stores instructions; proteins execute them",
  "Shape determines function; denaturation destroys both"],
 "Organic chemistry basics helpful.",
 ["IUPAC nomenclature; SI units"],
 "Standard chemistry literature (biochemistry textbooks).",
 "chem", "public-harvest"),
("sig-molecular-geometry", "Signature Chemistry",
 "Signature Molecular Geometry Engine",
 "A Signature original engine that builds molecules as exact geometric records: every atom placed by bond "
 "lengths and angles from VSEPR theory, every structure deterministic and reproducible. Rotations, reflections, "
 "and conformational searches execute as verified geometric operations rather than approximate simulations. "
 "The engine flags steric clashes geometrically and reports symmetry groups exactly. A Signature treatment of "
 "molecular structure as computable geometry — the shape of matter as a deterministic record.",
 ["Molecules as exact deterministic geometric records",
  "VSEPR-based placement: bond lengths and angles",
  "Conformations as verified geometric operations",
  "Steric clashes and symmetry detected exactly",
  "Structure as computable geometry"],
 "Chemical bonding basics.",
 ["Signature system conventions; IUPAC nomenclature"],
 "Original Signature design; classical facts per standard chemistry literature.",
 "chem", "signature"),
("sig-reaction-pathway", "Signature Chemistry",
 "Signature Reaction Pathway Mapper",
 "A Signature original instrument that maps a reaction as a pathway through Signature configuration space: "
 "reactants, transition states, and products as waypoints, with the activation barrier as measurable terrain. "
 "Balanced equations become verified routes; competing pathways are compared by barrier height and computed "
 "exactly. Catalysts appear as alternate low passes through the same terrain. The design keeps thermodynamics "
 "and kinetics intact while making every reaction a navigable, deterministic map.",
 ["Reactions as pathways through configuration space",
  "Transition states as measurable terrain features",
  "Competing pathways compared by barrier height",
  "Catalysts as alternate low passes",
  "Deterministic, navigable reaction maps"],
 "Kinetics and equilibrium basics.",
 ["Signature system conventions; IUPAC nomenclature"],
 "Original Signature design; classical facts per standard chemistry literature.",
 "chem", "signature"),
("sig-element-lattice", "Signature Chemistry",
 "Signature Element Lattice",
 "A Signature original reorganization of the periodic table as a true geometric lattice: elements positioned "
 "so that periodic trends — electronegativity, radius, ionization energy — become literal distances and slopes. "
 "Groups and periods are lattice directions; anomalous elements stand out as geometric outliers inviting "
 "investigation. The design preserves every established periodic fact while giving the table a computable "
 "surface where trend predictions are read as geometry. A Signature treatment of periodicity as spatial order.",
 ["Periodic table reorganized as a geometric lattice",
  "Trends as distances and slopes, not memorized lists",
  "Groups and periods as lattice directions",
  "Anomalous elements visible as geometric outliers",
  "Trend prediction by reading the geometry"],
 "Periodic table basics.",
 ["Signature system conventions; IUPAC nomenclature"],
 "Original Signature design; classical facts per standard chemistry literature.",
 "chem", "signature"),
("sig-solution-dynamics", "Signature Chemistry",
 "Signature Solution Dynamics",
 "A Signature original framework for solution chemistry as exact accounting: every dissolution tracked as "
 "solute and solvent records with concentration, activity, and equilibrium state carried deterministically. "
 "Acid-base titrations become navigable curves with the equivalence point computed, not estimated; buffer "
 "systems are modeled as self-correcting records with measurable capacity. Precipitation, solubility products, "
 "and colligative properties all execute as verified computations. A Signature treatment of solutions as "
 "auditable quantitative records.",
 ["Solutions as exact deterministic accounting records",
  "Titration curves with computed equivalence points",
  "Buffers as self-correcting records with capacity",
  "Solubility and colligative properties as verified computation",
  "Every ion accounted: nothing approximate in the books"],
 "Acids, bases, and stoichiometry basics.",
 ["Signature system conventions; IUPAC nomenclature"],
 "Original Signature design; classical facts per standard chemistry literature.",
 "chem", "signature"),
# ============================== BIOLOGY ==============================
("cell-biology", "Cell Biology",
 "Cell Biology: Structure of the Cell",
 "The cell is life's fundamental unit. Prokaryotic cells — bacteria and archaea — lack a nucleus; eukaryotic "
 "cells compartmentalize work in membrane-bound organelles. The nucleus holds DNA; mitochondria generate ATP "
 "through respiration; chloroplasts run photosynthesis in plants; ribosomes build proteins; the endoplasmic "
 "reticulum and Golgi apparatus process and ship them. The cell membrane's selective permeability controls what "
 "enters and leaves. Cell theory — all living things are made of cells, and all cells come from preexisting "
 "cells — is biology's founding statement.",
 ["Cell theory: life's unit; cells from preexisting cells",
  "Prokaryotic versus eukaryotic organization",
  "Organelles: nucleus, mitochondria, chloroplasts, ribosomes, ER, Golgi",
  "Membranes control selective transport",
  "Structure matched to function at every scale"],
 "Basic chemistry concepts helpful.",
 ["Standard biological nomenclature"],
 "Standard biology literature (cell biology textbooks).",
 "bio", "public-harvest"),
("genetics", "Genetics",
 "Genetics: From Mendel to DNA",
 "Mendel's pea-plant experiments revealed inheritance's rules: discrete factors (genes), dominance, and "
 "independent assortment. A century later the factors proved to be DNA — a double helix of four bases whose "
 "sequence encodes proteins via the triplet code. Meiosis shuffles parental chromosomes, generating the "
 "variation selection acts upon. Mutations — copying errors, radiation damage — are variation's raw material. "
 "From pedigree charts to genome sequencing, genetics reads the instruction set of life.",
 ["Mendel's laws: segregation and independent assortment",
  "DNA double helix and the triplet code",
  "Meiosis generates variation through shuffling",
  "Mutations as the raw material of variation",
  "Genotype to phenotype through protein expression"],
 "Cell biology basics.",
 ["Standard biological nomenclature"],
 "Standard biology literature (genetics textbooks).",
 "bio", "public-harvest"),
("evolution", "Evolution & Ecology",
 "Evolution: Natural Selection",
 "Darwin and Wallace saw that heritable variation plus differential survival changes populations over "
 "generations: natural selection. The fossil record, comparative anatomy, embryology, and now DNA sequencing "
 "converge on common descent — all life related through branching lineages. Mutations supply variation; "
 "selection, drift, and gene flow shape its fate. Speciation splits lineages when populations diverge beyond "
 "interbreeding. Antibiotic resistance in bacteria is natural selection observed in real time.",
 ["Natural selection: heritable variation plus differential survival",
  "Common descent supported by fossils, anatomy, DNA",
  "Mutation, selection, drift, gene flow as the forces",
  "Speciation through population divergence",
  "Antibiotic resistance as observed evolution"],
 "Genetics basics.",
 ["Standard biological nomenclature"],
 "Standard biology literature (evolutionary biology textbooks).",
 "bio", "public-harvest"),
("ecology", "Evolution & Ecology",
 "Ecology: Ecosystems and Energy Flow",
 "Ecology studies organisms in relationship with each other and their environment. Energy enters through "
 "producers — plants and algae capturing sunlight — and flows through consumers and decomposers, losing most "
 "at each trophic level as heat: the 10-percent rule of thumb. Food webs map who eats whom; nutrient cycles "
 "track carbon, nitrogen, and water through living and nonliving reservoirs. Population dynamics — exponential "
 "growth checked by carrying capacity — and succession, the orderly colonization of disturbed land, describe "
 "change over time.",
 ["Producers, consumers, decomposers in energy flow",
  "Trophic levels lose most energy as heat",
  "Food webs and nutrient cycles",
  "Population growth versus carrying capacity",
  "Succession: orderly recolonization after disturbance"],
 "Basic biology concepts.",
 ["Standard biological nomenclature"],
 "Standard biology literature (ecology textbooks).",
 "bio", "public-harvest"),
("human-anatomy", "Human Biology",
 "Human Anatomy: The Organ Systems",
 "Human anatomy maps the body's eleven organ systems. The skeletal system frames and protects; muscular tissue "
 "moves it; the nervous system commands via brain, spinal cord, and nerves; the cardiovascular system delivers "
 "oxygen and nutrients through heart and vessels; respiratory exchanges gases; digestive breaks down food; "
 "urinary filters waste; endocrine signals with hormones; lymphatic and immune defend; integumentary — skin — "
 "barriers the outside; reproductive continues the species. Each system's structure serves its function, and "
 "all eleven operate as one integrated organism.",
 ["Eleven organ systems working as one",
  "Skeletal, muscular, nervous: structure, movement, command",
  "Cardiovascular and respiratory: delivery and gas exchange",
  "Digestive, urinary, endocrine: processing, filtering, signaling",
  "Immune, integumentary, reproductive: defense, barrier, continuity"],
 "Basic biology vocabulary.",
 ["Terminologia Anatomica (international anatomical terminology)"],
 "Standard biology literature (anatomy references).",
 "bio", "public-harvest"),
("human-physiology", "Human Biology",
 "Human Physiology: Homeostasis",
 "Physiology is anatomy in action, and homeostasis — the maintenance of stable internal conditions — is its "
 "central theme. Negative feedback loops correct deviations: rising blood glucose triggers insulin, which "
 "lowers it; falling body temperature triggers shivering, which raises it. The heart adjusts rate and stroke "
 "volume to meet demand; kidneys tune blood volume and pH; lungs match breathing to CO2. Positive feedback "
 "amplifies instead — childbirth contractions, blood clotting — and is used sparingly, where escalation is "
 "the point.",
 ["Homeostasis: stable internal conditions",
  "Negative feedback corrects deviations",
  "Blood glucose, temperature, pH as regulated variables",
  "Heart, kidneys, lungs as the correcting effectors",
  "Positive feedback amplifies where escalation serves"],
 "Human anatomy basics.",
 ["Standard biological nomenclature"],
 "Standard biology literature (physiology textbooks).",
 "bio", "public-harvest"),
("microbiology", "Microbiology",
 "Microbiology: Bacteria, Viruses, and Fungi",
 "Microbiology studies life too small to see. Bacteria — single-celled prokaryotes — include decomposers, "
 "nitrogen fixers, gut symbionts, and pathogens; antibiotics target their distinctive machinery. Viruses are "
 "not cells at all: protein-coated genetic parcels that hijack host cells to replicate, from influenza to "
 "bacteriophages. Fungi digest externally and absorb, recycling the world's dead matter; a few cause disease. "
 "The germ theory — microorganisms cause many diseases — underlies sanitation, vaccination, and antisepsis, "
 "which together saved more lives than any other medical advance.",
 ["Bacteria: prokaryotes; symbionts, decomposers, pathogens",
  "Viruses: non-cellular genetic parcels needing hosts",
  "Fungi: external digesters and great recyclers",
  "Germ theory underlies sanitation and vaccination",
  "Antibiotics target bacterial machinery specifically"],
 "Cell biology basics.",
 ["Standard biological nomenclature"],
 "Standard biology literature (microbiology textbooks).",
 "bio", "public-harvest"),
("botany", "Botany",
 "Botany: Photosynthesis and Plant Structure",
 "Plants power the living world through photosynthesis: chlorophyll captures light to convert carbon dioxide "
 "and water into glucose and oxygen. Roots absorb water and minerals; xylem lifts them upward; leaves exchange "
 "gases through stomata while phloem distributes sugars. Flowers, fruits, and seeds are the reproductive "
 "solution of angiosperms, co-evolved with pollinators. Tropisms — growth toward light, against gravity — and "
 "hormones like auxin coordinate the plant without a nervous system.",
 ["Photosynthesis: light + CO2 + water -> glucose + oxygen",
  "Roots, xylem, leaves, phloem as transport systems",
  "Stomata regulate gas exchange and water loss",
  "Flowers, fruits, seeds: the angiosperm reproductive plan",
  "Tropisms and hormones coordinate growth"],
 "Cell biology basics.",
 ["International Code of Nomenclature for plants"],
 "Standard biology literature (botany textbooks).",
 "bio", "public-harvest"),
("sig-genome-pattern", "Signature Biology",
 "Signature Genome Pattern Engine",
 "A Signature original instrument that reads genetic sequences as geometric patterns on a Signature lattice: "
 "repeats become periodic structures, coding regions show as organized domains, and regulatory motifs appear as "
 "recurring geometric signatures. GC content, k-mer spectra, and repeat maps are computed deterministically "
 "over the lattice, giving every sequence a canonical Signature pattern record. The engine works on synthetic "
 "sample sequences for demonstration and is built to accept real reference data through proper channels. A "
 "Signature treatment of sequence analysis as pattern geometry.",
 ["Sequences read as geometric patterns on a Signature lattice",
  "Repeats, coding domains, motifs as pattern features",
  "GC content and k-mer spectra computed deterministically",
  "Canonical reproducible pattern records",
  "Demonstrated on synthetic sample sequences"],
 "Genetics basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard biology literature.",
 "bio", "signature"),
("sig-ecosystem-sim", "Signature Biology",
 "Signature Ecosystem Simulator",
 "A Signature original simulator that models ecosystems as deterministic Signature networks: species as nodes "
 "with population records, feeding relationships as energy-flow edges, carrying capacities as node limits. "
 "Predator-prey cycles, succession stages, and disturbance recovery all execute as reproducible runs from "
 "stated starting conditions — same inputs, same trajectory, every time. The design keeps real ecological "
 "principles (trophic loss, logistic growth, competitive exclusion) as the network's governing rules while "
 "making the whole system inspectable and replayable.",
 ["Ecosystems as deterministic species networks",
  "Energy-flow edges with trophic loss built in",
  "Logistic growth and carrying capacity per node",
  "Reproducible runs: same inputs, same trajectory",
  "Succession and disturbance as network dynamics"],
 "Ecology basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard biology literature.",
 "bio", "signature"),
("sig-cell-geometry", "Signature Biology",
 "Signature Cell Geometry",
 "A Signature original treatment that models the cell as exact geometry: organelles as bounded volumes with "
 "measured proportions, membranes as selective surfaces with transport rules, the cytoskeleton as a structural "
 "lattice. Diffusion, osmosis, and active transport become geometric flow problems with deterministic solutions. "
 "Cell division is choreographed as a verified geometric sequence — the mitotic spindle as a real construction. "
 "A Signature treatment of cell biology where structure is computable and every process has a geometric reading.",
 ["Organelles as bounded volumes with measured proportions",
  "Membranes as selective surfaces with transport rules",
  "Diffusion and osmosis as geometric flow problems",
  "Mitosis as a verified geometric sequence",
  "Structure computable; processes geometrically readable"],
 "Cell biology basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard biology literature.",
 "bio", "signature"),
("sig-biosequence-harmonizer", "Signature Biology",
 "Signature Bio-Sequence Harmonizer",
 "A Signature original instrument that aligns biological sequences by harmonic pattern matching on the Signature "
 "lattice: related sequences resonate at shared motifs while unrelated ones stay geometrically distant. "
 "Alignment scores, conserved regions, and phylogenetic distances are computed as deterministic harmonic "
 "measures rather than heuristic guesses. Demonstrated on synthetic sample sequences; built to accept real "
 "reference data through proper channels. A Signature treatment of comparative genomics as resonance geometry.",
 ["Sequence alignment as harmonic pattern matching",
  "Conserved regions as shared resonances",
  "Phylogenetic distance as deterministic harmonic measure",
  "Reproducible alignments, not heuristic guesses",
  "Demonstrated on synthetic sample sequences"],
 "Genetics basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard biology literature.",
 "bio", "signature"),
# ============================== COMPUTER SCIENCE ==============================
("data-structures", "Foundations",
 "Data Structures: Arrays, Linked Lists, Trees, Graphs",
 "Data structures organize data for efficient access. Arrays give constant-time indexing into contiguous "
 "memory; linked lists trade that for cheap insertion via pointer chains. Trees — especially balanced binary "
 "search trees — keep ordered data searchable in logarithmic time. Graphs model arbitrary relationships: "
 "social networks, road maps, the web itself. Hash tables pair keys to values in near-constant time on "
 "average. Choosing the right structure is the first and most consequential decision in program design, "
 "because no algorithm outruns a bad layout.",
 ["Arrays: constant-time index into contiguous memory",
  "Linked lists: cheap insertion via pointer chains",
  "Balanced trees: logarithmic search, insert, delete",
  "Graphs model arbitrary relationships",
  "Hash tables: near-constant-time key lookup"],
 "Basic programming concepts.",
 ["Standard CS terminology"],
 "Standard computer science literature (data structures textbooks).",
 "cs", "public-harvest"),
("algorithms-sorting", "Algorithms",
 "Algorithms: Sorting and Searching",
 "Sorting and searching are the canonical algorithm problems. Bubble and insertion sort are simple but "
 "quadratic; merge sort and quicksort achieve n log n through divide and conquer; counting sort goes linear "
 "when keys are bounded. Binary search finds items in sorted arrays in logarithmic time by halving the search "
 "space each step. Correctness proofs and complexity analysis separate algorithms that merely work from ones "
 "that scale — the difference between a demo and a system serving millions.",
 ["Quadratic sorts: simple, slow at scale",
  "Merge sort and quicksort: n log n via divide and conquer",
  "Binary search: logarithmic lookup in sorted data",
  "Correctness proofs guarantee the output",
  "Complexity analysis predicts scaling behavior"],
 "Data structures basics.",
 ["Standard CS terminology"],
 "Standard computer science literature (algorithms textbooks).",
 "cs", "public-harvest"),
("complexity", "Theory",
 "Computational Complexity: Big-O Notation",
 "Big-O notation classifies algorithms by growth: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) "
 "linearithmic, O(n^2) quadratic, O(2^n) exponential. It describes the worst case as input grows, ignoring "
 "constant factors to reveal the shape of scaling. P is the class of problems solvable in polynomial time; NP "
 "the class verifiable in polynomial time; whether P equals NP is the deepest open question in computer "
 "science, with a million-dollar prize. Complexity tells you before you code whether an approach can survive "
 "real input sizes.",
 ["Big-O classifies growth, ignoring constant factors",
  "From O(1) to O(2^n): the hierarchy of scaling",
  "Worst-case analysis as the standard lens",
  "P versus NP: solvable versus verifiable in polynomial time",
  "Complexity predicts survival at real input sizes"],
 "Algorithms basics.",
 ["Standard CS terminology"],
 "Standard computer science literature (complexity references).",
 "cs", "public-harvest"),
("operating-systems", "Systems",
 "Operating Systems: Processes, Memory, Files",
 "The operating system manages hardware on behalf of programs. Processes are running programs with isolated "
 "memory spaces, scheduled onto CPUs by the kernel; threads share a process's memory for parallel work. "
 "Virtual memory gives each process the illusion of vast private RAM, paging to disk as needed. The file "
 "system organizes persistent storage into named hierarchies with permissions. System calls are the controlled "
 "gates between user programs and kernel power — every read, write, and network packet passes through them.",
 ["Processes: isolated running programs scheduled by the kernel",
  "Threads share memory for parallel work",
  "Virtual memory: the illusion of vast private RAM",
  "File systems organize persistent named storage",
  "System calls gate all kernel access"],
 "Basic programming and hardware intuition.",
 ["POSIX concepts; standard CS terminology"],
 "Standard computer science literature (operating systems textbooks).",
 "cs", "public-harvest"),
("computer-networks", "Systems",
 "Computer Networks: Packets and Protocols",
 "The internet moves data as packets — small addressed chunks routed independently and reassembled at the "
 "destination. The layered model separates concerns: physical links, IP addressing and routing, TCP's reliable "
 "ordered streams, and application protocols like HTTP and DNS on top. DNS translates human names to numeric "
 "addresses; TLS encrypts the conversation. Congestion control probes for available bandwidth without "
 "overwhelming the network. Every video call and page load is this stack working invisibly, billions of times "
 "per second.",
 ["Packets: independently routed, reassembled at destination",
  "Layered model: physical, IP, TCP, application",
  "DNS maps names to addresses; TLS encrypts",
  "TCP provides reliable ordered byte streams",
  "Congestion control shares bandwidth fairly"],
 "Basic computing concepts.",
 ["IETF RFC standards; standard CS terminology"],
 "Standard computer science literature (networking textbooks).",
 "cs", "public-harvest"),
("databases-relational", "Systems",
 "Databases: The Relational Model and SQL",
 "The relational model organizes data into tables — relations — of rows and columns, with keys identifying "
 "rows and foreign keys linking tables. SQL queries this structure declaratively: you state what you want, "
 "the engine plans how. Normalization removes redundancy by splitting tables along functional dependencies. "
 "ACID transactions — atomic, consistent, isolated, durable — guarantee that concurrent users never see a "
 "half-written world. Indexes trade write speed and space for fast lookups, the fundamental database bargain.",
 ["Tables, keys, and foreign-key relationships",
  "SQL: declarative queries, engine-planned execution",
  "Normalization removes redundancy",
  "ACID transactions for concurrent correctness",
  "Indexes trade space for lookup speed"],
 "Basic data concepts.",
 ["SQL standard (ISO/IEC 9075)"],
 "Standard computer science literature (database textbooks).",
 "cs", "public-harvest"),
("programming-languages", "Foundations",
 "Programming Languages: Paradigms and Types",
 "Programming paradigms are philosophies of structuring computation: imperative (step-by-step state changes), "
 "functional (pure functions, immutable data), object-oriented (encapsulated state with behavior), and logic "
 "programming (declare relations, let the engine search). Type systems classify values — static types checked "
 "before running, dynamic types checked as you go — catching whole classes of errors early. Compilers translate "
 "to machine code ahead of time; interpreters execute on the fly. The paradigm shapes how you think; the best "
 "engineers borrow from all of them.",
 ["Imperative, functional, object-oriented, logic paradigms",
  "Static versus dynamic type checking",
  "Compilers translate ahead of time; interpreters on the fly",
  "Type systems catch error classes early",
  "Paradigms shape problem-solving thought"],
 "Experience with at least one programming language.",
 ["Standard CS terminology"],
 "Standard computer science literature (programming language texts).",
 "cs", "public-harvest"),
("cryptography", "Security",
 "Cryptography: Keys, Hashes, and Public-Key Systems",
 "Cryptography protects information mathematically. Symmetric ciphers use one shared secret key for speed; "
 "public-key systems use matched key pairs so anyone can encrypt but only the holder decrypts — RSA and "
 "elliptic curves are the workhorses. Hash functions fingerprint data irreversibly, underpinning password "
 "storage and integrity checks. Digital signatures prove authorship and detect tampering. Key exchange "
 "protocols like Diffie-Hellman let strangers agree on secrets over public channels — the trick that makes "
 "secure web browsing possible.",
 ["Symmetric ciphers: one shared key, high speed",
  "Public-key systems: encrypt with public, decrypt with private",
  "Hash functions fingerprint data irreversibly",
  "Digital signatures prove authorship",
  "Diffie-Hellman: strangers agree on secrets publicly"],
 "Basic algebra and modular arithmetic intuition.",
 ["NIST cryptographic standards"],
 "Standard computer science literature (cryptography textbooks).",
 "cs", "public-harvest"),
("sig-deterministic-compute", "Signature Computer Science",
 "Signature Deterministic Computation Engine",
 "A Signature original engine that executes computations with total determinism: same program, same inputs, "
 "same outputs — bit for bit, every run, on any machine. Nondeterminism is quarantined at declared boundaries "
 "(randomness from seeded generators, I/O at explicit gates) so the core is always reproducible. Every "
 "execution produces a verifiable trace: each step justified, each state transition checkable. A Signature "
 "treatment of computation where reproducibility is the foundation, not a feature.",
 ["Bit-for-bit reproducible execution on any machine",
  "Nondeterminism quarantined at declared boundaries",
  "Seeded randomness: reproducible 'random' streams",
  "Verifiable execution traces, step by step",
  "Reproducibility as foundation, not feature"],
 "Programming basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard CS literature.",
 "cs", "signature"),
("sig-data-geometry", "Signature Computer Science",
 "Signature Data Geometry",
 "A Signature original design that gives every dataset a geometric form: records as points in a Signature "
 "space, relationships as distances, clusters as visible neighborhoods. Queries become geometric operations — "
 "nearest neighbors, range selections, boundary crossings — executed deterministically on the lattice. Schema "
 "changes are geometric transformations with verifiable invariants. A Signature treatment of data "
 "organization where the shape of the data is as queryable as its contents.",
 ["Datasets as geometric forms in Signature space",
  "Records as points; relationships as distances",
  "Queries as geometric operations",
  "Schema changes as verifiable transformations",
  "Shape of data queryable alongside contents"],
 "Data structures basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard CS literature.",
 "cs", "signature"),
("sig-algorithm-workability", "Signature Computer Science",
 "Signature Algorithm Workability Proofs",
 "A Signature original framework that certifies algorithms with workability proofs: not just 'correct' but "
 "proven workable — termination guaranteed, complexity bounded, edge cases enumerated and handled. Each proof "
 "is a checkable record: preconditions, invariants, termination argument, complexity bound. Sorting, searching, "
 "and graph algorithms ship with their proofs attached, so reusing an algorithm means inheriting its "
 "guarantees. A Signature treatment of algorithms where every routine carries its own certificate of "
 "workability.",
 ["Workability proofs: correct, terminating, bounded",
  "Preconditions, invariants, termination arguments as records",
  "Edge cases enumerated, not discovered in production",
  "Proofs travel with the algorithm as certificates",
  "Reuse inherits guarantees"],
 "Algorithms basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard CS literature.",
 "cs", "signature"),
("sig-secure-channel", "Signature Computer Science",
 "Signature Secure Channel Constructor",
 "A Signature original design for building secure communication channels from first principles: key exchange, "
 "authentication, and encrypted transport composed as verified stages, each with its security property stated "
 "and checked. The construction uses only well-established primitives (never novel ciphers) arranged in a "
 "deterministic, auditable pipeline. Every channel carries a manifest of its guarantees — confidentiality, "
 "integrity, authenticity — so users know exactly what is proven. A Signature treatment of applied "
 "cryptography as certified construction.",
 ["Channels built from verified stages",
  "Established primitives only; never novel ciphers",
  "Security properties stated and checked per stage",
  "Channel manifest lists proven guarantees",
  "Deterministic, auditable construction pipeline"],
 "Cryptography basics.",
 ["Signature system conventions; NIST primitives"],
 "Original Signature design; classical facts per standard CS literature.",
 "cs", "signature"),
]
