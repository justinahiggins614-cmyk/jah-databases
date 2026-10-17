#!/usr/bin/env python3
"""Seed entries for the Relativity field build (field #1, taxonomy order).

Public database `relativity`: real, fact-checked relativity physics
(src public-harvest). Signature database `relativity-signature`: his original
Signature interpretation (src signature, titles suffixed " (Signature
Edition)", never presented as authentic public record).

Every record carries ladder_rank (1-10) + ladder_tier
(foundations/compounded/advanced); pages render in ladder order.

Never the words "bat belt". No website references. No Facebook.
"""

C = 299792458.0  # m/s, exact by SI definition

# Shared citation tails
CIT_STD = "Standard physics literature (peer-reviewed relativity textbooks and journals)."
CIT_E1905 = ("Einstein, A. (1905). 'On the Electrodynamics of Moving Bodies.' "
             "Annalen der Physik, 17, 891-921.")
CIT_E1915 = ("Einstein, A. (1915). 'The Field Equations of Gravitation.' "
             "Sitzungsberichte der Preussischen Akademie der Wissenschaften.")
CIT_E1916 = ("Einstein, A. (1916). 'The Foundation of the General Theory of Relativity.' "
             "Annalen der Physik, 49, 769-822.")
CIT_MM = ("Michelson, A. A., & Morley, E. W. (1887). 'On the Relative Motion of the "
          "Earth and the Luminiferous Ether.' American Journal of Science, 34, 333-345.")
SIG_TAIL = ("Signature editions are original Signature interpretations of the physics, "
            "written in the Signature system — clearly labeled Signature-made, never "
            "presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-relativity", "name": "What Is Relativity: Motion Is Always Relative",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Relativity is the branch of physics that describes how measurements of space and time "
  "depend on the observer's state of motion. Its founding insight is simple: there is no "
  "absolute rest frame in the universe — every measurement of speed, position, or time is "
  "made relative to some chosen reference frame. A passenger walking down the aisle of a "
  "smoothly moving train moves at walking speed relative to the train, but at train speed "
  "plus walking speed relative to the ground; both descriptions are correct in their own "
  "frame. Albert Einstein built special relativity (1905) on this idea plus the constancy "
  "of the speed of light, and general relativity (1915) by extending it to gravity and "
  "accelerated motion. At everyday speeds the relativistic corrections are immeasurably "
  "small, which is why Galilean relativity served physics well for three centuries — "
  "Einstein's theory contains Newton's as its low-speed limit."),
 "how_it_works": (
  "Relativity works by writing the laws of physics in a form that is valid in every "
  "inertial reference frame. Instead of treating space and time as separate absolutes, "
  "special relativity treats them as a single four-dimensional spacetime whose geometry "
  "all observers agree on. Transforming measurements from one frame to another is done "
  "with the Lorentz transformations, which reduce to the familiar Galilean rules when "
  "speeds are far below the speed of light. Because the correction factor differs from "
  "one by only about nine parts in a quadrillion at highway speeds, everyday engineering "
  "never notices it — but particle accelerators, atomic clocks, and GPS satellites must "
  "account for it or they fail."),
 "key_points": [
  "All motion is measured relative to a chosen reference frame; there is no absolute rest.",
  "Einstein's 1905 special relativity covers uniform motion; his 1915 general relativity covers gravity and acceleration.",
  "At everyday speeds, relativity agrees with Newtonian physics to better than one part in a trillion.",
  "Space and time are unified into a single four-dimensional spacetime.",
  "The theory is one of the most precisely tested in all of science."],
 "requirements": [
  "High-school algebra and comfort with the idea of coordinate systems.",
  "No calculus needed for the foundations tier; later tiers use it.",
  "A willingness to follow thought experiments carefully."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "galilean",
 "sig_lens": (
  "The Signature reading of relativity starts from a design principle: every instrument "
  "reads the universe from its own frame, so the Signature system treats the reference "
  "frame as part of the measurement itself. This database keeps that discipline — every "
  "record names its frame before it names its numbers."),
},
{
 "key": "principle-of-relativity", "name": "The Principle of Relativity",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "The principle of relativity states that the laws of physics are identical in every "
  "inertial reference frame — every laboratory moving at constant velocity. Galileo "
  "Galilei stated the first version around 1632: no mechanical experiment performed "
  "inside a smoothly sailing ship can reveal whether the ship is moving or at rest. "
  "Einstein's 1905 leap was to extend the principle from mechanics to all of physics, "
  "including electromagnetism: Maxwell's equations, which predict a fixed speed of "
  "light, must hold in every inertial frame. That single extension forced the "
  "abandonment of absolute time and produced time dilation, length contraction, and the "
  "relativity of simultaneity as unavoidable consequences. The principle remains the "
  "deepest symmetry in physics — modern particle physics is built by demanding that "
  "physical laws respect it."),
 "how_it_works": (
  "The principle works as a constraint on every candidate physical law: write the law "
  "in one inertial frame, transform to another frame moving at constant velocity, and "
  "the law must keep the same form. In Galilean relativity the transformation was x' = "
  "x − vt with time unchanged; Einstein showed the correct transformation is the "
  "Lorentz transformation, which mixes space and time. Any theory whose equations change "
  "form under this transformation contradicts the principle and is ruled out. This is "
  "why physicists test new theories against relativity first — the principle is a "
  "filter that candidate laws of nature must pass."),
 "key_points": [
  "Galileo (1632): mechanical experiments cannot detect uniform motion.",
  "Einstein (1905): ALL physical laws, including electromagnetism, are frame-independent.",
  "The principle forced the speed of light to be the same in every inertial frame.",
  "It acts as a symmetry filter: candidate laws must keep their form under Lorentz transformations.",
  "Modern field theory is constructed by enforcing this principle."],
 "requirements": [
  "Familiarity with the 'What Is Relativity' record.",
  "Basic understanding of what a physical law is (an equation relating measurable quantities)."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905,
  "Galilei, G. (1632). Dialogue Concerning the Two Chief World Systems.",
  CIT_STD],
 "demo_kind": "galilean",
 "sig_lens": (
  "The Signature take treats the principle of relativity as a design law for instruments: "
  "a Signature instrument must report the same physics from any uniform-motion platform, "
  "so every Signature design is validated in at least two frames before it ships."),
},
{
 "key": "two-postulates", "name": "The Two Postulates of Special Relativity",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Special relativity rests on exactly two postulates, published by Einstein in 1905. "
  "Postulate 1: the laws of physics are the same in all inertial frames (the principle "
  "of relativity). Postulate 2: the speed of light in vacuum is the same for all "
  "inertial observers, regardless of the motion of the source or the observer. The "
  "second postulate is the radical one — common sense says light from a moving source "
  "should travel faster, like a ball thrown from a moving train, but exhaustive "
  "experiments from Michelson-Morley (1887) onward show it does not. Everything strange "
  "about relativity — time dilation, length contraction, the relativity of simultaneity "
  "— follows logically from these two short statements plus the definition of an "
  "inertial frame. Their spareness is their power: two sentences generate the entire "
  "theory, and every prediction has survived a century of testing."),
 "how_it_works": (
  "The postulates work as axioms: assume both, then derive what moving observers must "
  "measure. If light speed is fixed at c for everyone, then a light beam bouncing "
  "between mirrors on a moving train must travel a longer zigzag path as seen from the "
  "ground — and since speed is distance over time, the ground observer must measure a "
  "longer time between ticks. That is time dilation, derived in five lines from the "
  "postulates. Length contraction and the relativity of simultaneity fall out the same "
  "way. The postulates cannot be proven from anything deeper within the theory; they "
  "are justified because everything derived from them matches experiment."),
 "key_points": [
  "Postulate 1: physics is identical in all inertial frames.",
  "Postulate 2: light speed in vacuum (c) is identical for all inertial observers.",
  "The Michelson-Morley experiment (1887) gave the first strong evidence for postulate 2.",
  "Time dilation, length contraction, and relative simultaneity are theorems, not extra assumptions.",
  "No experiment has ever falsified either postulate."],
 "requirements": [
  "The 'Principle of Relativity' and 'Inertial Reference Frames' records.",
  "Comfort with simple algebra (square roots appear in derivations)."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905, CIT_MM, CIT_STD],
 "demo_kind": "michelson",
 "sig_lens": (
  "The Signature framing admires the postulates as a specification: two lines of "
  "requirements that generate a whole physics. Signature designs copy that discipline — "
  "state the invariants first, derive everything else, never bolt on exceptions."),
},
{
 "key": "inertial-frames", "name": "Inertial Reference Frames",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "An inertial reference frame is a frame of reference in which an object at rest "
  "stays at rest and an object in motion keeps moving in a straight line at constant "
  "speed — Newton's first law holds exactly. A smoothly cruising airplane is very "
  "close to an inertial frame; a car rounding a corner is not, because passengers "
  "feel pushed sideways with no visible force acting on them. That phantom push is "
  "the signature of a non-inertial frame: in accelerating frames, fictitious forces "
  "(centrifugal, Coriolis) appear. Special relativity's postulates apply strictly to "
  "inertial frames, which is why the theory's name contains 'special' — it handles "
  "the special case of uniform motion. True inertial frames are an idealization, but "
  "any frame far from strong gravity and acceleration approximates one well enough "
  "for the theory's predictions to be tested to extraordinary precision."),
 "how_it_works": (
  "An inertial frame works as the clean laboratory of relativity: inside it, the "
  "laws of physics take their simplest form and clocks can be synchronized by light "
  "signals without ambiguity. To compare measurements between two inertial frames in "
  "relative motion, physicists apply the Lorentz transformation, which tells exactly "
  "how space and time coordinates mix. Non-inertial frames are handled by general "
  "relativity, which shows that acceleration is locally indistinguishable from "
  "gravity — the equivalence principle. In practice, laboratories, satellites, and "
  "particle beams are treated as inertial frames whenever their acceleration is "
  "negligible over the measurement time."),
 "key_points": [
  "Inertial frame: Newton's first law holds; no fictitious forces.",
  "Special relativity applies exactly to inertial frames — hence 'special'.",
  "Accelerating or rotating frames show centrifugal and Coriolis effects.",
  "General relativity extends physics to all frames via the equivalence principle.",
  "Real laboratories are approximately inertial when acceleration is negligible."],
 "requirements": [
  "The 'What Is Relativity' record.",
  "Newton's first law (an object in motion stays in motion)."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "galilean",
 "sig_lens": (
  "The Signature practice: name your frame before you trust your numbers. Every "
  "Signature measurement log records the frame's acceleration, because a reading taken "
  "in a turning frame is a different instrument than the same hardware standing still."),
},
{
 "key": "light-clock", "name": "The Light Clock Thought Experiment",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The light clock is Einstein's simplest thought experiment and the clearest route "
  "into time dilation. Picture two parallel mirrors with a pulse of light bouncing "
  "between them; each round trip is one 'tick'. At rest, the light travels straight "
  "up and down. Now watch the same clock glide past you at high speed: the light "
  "must chase the moving mirrors, tracing a zigzag path that is plainly longer than "
  "the straight up-and-down path. Because the speed of light is the same for every "
  "observer (postulate 2), the longer path must take a longer time — so you see the "
  "moving clock tick slower than an identical clock at rest beside you. The effect "
  "is not mechanical: it is time itself running slower for the moving system, and it "
  "applies to every clock — light clocks, atomic clocks, beating hearts, decaying "
  "particles — without exception."),
 "how_it_works": (
  "The light clock works by pure geometry. If the mirrors are distance L apart, a "
  "stationary observer measures the round-trip time T0 = 2L/c. For a clock moving at "
  "speed v, the light travels the hypotenuse of a right triangle: half-tick path "
  "length sqrt(L^2 + (vT/2)^2), giving T = 2·sqrt(L^2 + (vT/2)^2)/c, which solves to "
  "T = T0 / sqrt(1 − v^2/c^2). The denominator is the Lorentz factor gamma, so the "
  "moving clock's period is stretched by exactly gamma. Because the argument uses "
  "only the constancy of c and Euclidean geometry, it proves time dilation must "
  "affect all physical processes equally — any process that didn't slow down could "
  "be used to detect absolute motion, violating the principle of relativity."),
 "key_points": [
  "A light clock's tick is one round trip of a light pulse between two mirrors.",
  "A moving clock's light traces a longer zigzag path as seen by a stationary observer.",
  "Constant light speed forces the longer path to take longer: T = gamma * T0.",
  "The argument covers every clock, not just light clocks — time itself dilates.",
  "Real atomic clocks flown on airplanes (Hafele-Keating, 1971) confirm the effect."],
 "requirements": [
  "The 'Two Postulates' record.",
  "The Pythagorean theorem."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905,
  "Hafele, J. C., & Keating, R. E. (1972). 'Around-the-World Atomic Clocks.' Science, 177, 166-170.",
  CIT_STD],
 "demo_kind": "lightclock",
 "sig_lens": (
  "The Signature lesson of the light clock: the simplest possible instrument — two "
  "mirrors and a pulse — exposes the deepest fact about time. Signature design chases "
  "that economy: the cleanest apparatus that can still decide the question."),
},
{
 "key": "time-dilation", "name": "Time Dilation",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Time dilation is the measured slowing of time for a system moving relative to the "
  "observer: a moving clock ticks slower by the Lorentz factor gamma = "
  "1/sqrt(1 − v^2/c^2). At 87 percent of light speed, gamma is 2 and moving clocks "
  "run at half rate; at 99.5 percent, gamma is 10. The effect is symmetric — each of "
  "two inertial observers sees the other's clock running slow — because each is "
  "entitled to regard themselves as at rest. Nature provides a dramatic demonstration: "
  "muons created by cosmic rays high in the atmosphere live only 2.2 microseconds, "
  "far too short to reach the ground, yet they arrive in droves because at 99.8 "
  "percent of light speed their internal clocks run about 16 times slower as seen "
  "from Earth. GPS satellites, particle accelerators, and atomic-clock experiments "
  "all measure time dilation routinely; it is engineering fact, not philosophy."),
 "how_it_works": (
  "Time dilation works through the geometry of spacetime. Every observer measures "
  "'proper time' — the time read by a clock moving with the system — while a clock "
  "moving at speed v relative to the observer accumulates coordinate time stretched "
  "by gamma: delta-t = gamma * delta-tau. The symmetry between observers is real but "
  "not paradoxical: comparing clocks requires bringing them together, and that "
  "requires acceleration, which breaks the symmetry (the twin paradox). In particle "
  "accelerators, unstable particles live gamma times longer in the laboratory frame, "
  "letting physicists study them; in GPS, satellite clocks tick faster overall "
  "because gravitational time dilation outweighs the special-relativistic slowing."),
 "key_points": [
  "Moving clocks run slow by the Lorentz factor: delta-t = gamma * delta-tau.",
  "The effect is symmetric between inertial observers — each sees the other's clock slow.",
  "Muons from cosmic rays reach the ground only because of time dilation (gamma ~ 16).",
  "Measured directly by atomic clocks on aircraft and in particle accelerators.",
  "GPS must correct for it; uncorrected, positions would drift kilometers per day."],
 "requirements": [
  "The 'Light Clock' record.",
  "Ability to compute 1/sqrt(1 - x^2) on a calculator."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905,
  "Rossi, B., & Hall, D. B. (1941). 'Variation of the Rate of Decay of Mesotrons with Momentum.' Physical Review, 59, 223-228.",
  CIT_STD],
 "demo_kind": "timedil",
 "sig_lens": (
  "The Signature use of time dilation is practical: wherever the Signature system "
  "timestamps fast-moving data — satellite links, high-speed sensors — the timestamps "
  "are corrected to a common frame first, because raw clock readings from moving "
  "platforms are not comparable until relativity is accounted for."),
},
{
 "key": "lorentz-factor", "name": "The Lorentz Factor",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The Lorentz factor, written as the Greek letter gamma, is the single number that "
  "controls how strong relativistic effects are at a given speed: gamma = "
  "1/sqrt(1 − v^2/c^2), where v is the speed and c is the speed of light. At rest "
  "gamma is exactly 1; at half light speed it is about 1.15; at 90 percent it is "
  "2.29; at 99 percent it is 7.09; at 99.99 percent it is about 70.7. As v approaches "
  "c, gamma grows without bound — it diverges to infinity, which is the mathematical "
  "reason massive objects can never reach light speed: it would take infinite energy. "
  "Gamma multiplies moving time intervals (time dilation), divides moving lengths "
  "(length contraction), and multiplies mass-energy (relativistic energy). Memorizing "
  "its shape — flat near 1 for everyday speeds, exploding near c — is the fastest way "
  "to develop intuition for all of special relativity."),
 "how_it_works": (
  "The Lorentz factor works as the conversion ratio between a moving system's own "
  "measurements and a stationary observer's. It emerges whenever the constancy of c "
  "is combined with the Pythagorean theorem — in the light-clock derivation, gamma "
  "is the ratio of the zigzag hypotenuse to the vertical leg. Because it appears in "
  "time dilation, length contraction, the Lorentz transformations, relativistic "
  "momentum, and relativistic energy, computing gamma is the first step of nearly "
  "every special-relativity calculation. Physicists often work directly with beta = "
  "v/c and gamma instead of raw speeds, since all formulas simplify; 'gamma = 10' "
  "unambiguously means 99.5 percent of light speed."),
 "key_points": [
  "gamma = 1/sqrt(1 - v^2/c^2); gamma = 1 at rest, diverging to infinity as v approaches c.",
  "Landmark values: gamma=2 at 86.6% c; gamma=10 at 99.5% c; gamma=100 at 99.995% c.",
  "Divergence at c is why massive objects cannot reach light speed.",
  "Gamma scales time intervals (up), lengths (down), momentum and energy (up).",
  "Physicists quote speeds as (beta, gamma) pairs rather than raw velocities."],
 "requirements": [
  "The 'Time Dilation' record.",
  "Square roots and percentages."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "gamma",
 "sig_lens": (
  "The Signature habit: quote gamma, not just speed. A Signature spec sheet for any "
  "relativistic system lists beta and gamma up front, because gamma is the number "
  "that actually sizes the corrections."),
},
{
 "key": "length-contraction", "name": "Length Contraction",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Length contraction is the measured shortening of a moving object's length along "
  "its direction of motion: L = L0/gamma, where L0 is the object's length at rest "
  "(its proper length) and gamma is the Lorentz factor. A 100-meter spaceship "
  "passing at 87 percent of light speed measures only 50 meters long to a "
  "stationary observer; at 99.5 percent it is 10 meters. Only the dimension along "
  "the motion contracts — widths and heights are unaffected. Like time dilation, "
  "the effect is symmetric: each observer measures the other's rulers as shortened. "
  "It is not a mechanical squeezing; it is how space itself measures out for moving "
  "systems, and it is required to keep the speed of light constant for all "
  "observers. Direct mechanical measurement is impractical at attainable speeds, but "
  "the effect is confirmed indirectly — for example, in the electromagnetic fields "
  "of relativistic particle beams, which behave exactly as contracted charge "
  "distributions predict."),
 "how_it_works": (
  "Length contraction works because measuring a moving object's length requires "
  "marking both ends at the same time — and simultaneity is relative. An observer "
  "who considers herself at rest marks the front and back of the passing ship "
  "simultaneously in her frame; in the ship's frame those two markings happen at "
  "different times, while the ship has moved between them. Working through the "
  "Lorentz transformation, the distance between the simultaneous marks comes out "
  "shorter by exactly gamma. The contraction guarantees consistency: the crew "
  "measures the same relative speed using their own uncontracted rulers and the "
  "observer's dilated clocks, and both frames agree that light moves at c."),
 "key_points": [
  "Moving lengths shrink along the motion: L = L0 / gamma; transverse sizes unchanged.",
  "Symmetric between observers, like time dilation — not a physical compression.",
  "Arises because length measurement needs simultaneous endpoints, and simultaneity is relative.",
  "Required for consistency of relative speed measurements between frames.",
  "Confirmed indirectly in relativistic beam physics and collider design."],
 "requirements": [
  "The 'Lorentz Factor' and 'Simultaneity Is Relative' records.",
  "Understanding that measuring length needs both ends marked at once."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "lencontract",
 "sig_lens": (
  "The Signature moral of length contraction: never trust a measurement until you "
  "know how its endpoints were synchronized. Signature procedures timestamp both "
  "ends of any moving baseline in a single declared frame."),
},

{
 "key": "simultaneity", "name": "Simultaneity Is Relative",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The relativity of simultaneity states that two events judged simultaneous in one "
  "inertial frame are generally not simultaneous in another frame moving relative to "
  "the first. Einstein's train thought experiment makes it vivid: lightning strikes "
  "both ends of a moving train, and an observer on the embankment midway between the "
  "strikes sees the flashes at the same instant — but a passenger at the train's "
  "midpoint is rushing toward the front flash and away from the rear one, so the "
  "front light reaches her first, and she judges the front strike earlier. Both "
  "judgments are correct within their frames; there is no frame-independent fact "
  "about which distant events are 'truly' simultaneous. This demolishes Newton's "
  "absolute time: without universal simultaneity there is no universal 'now' "
  "stretching across the universe. It is also the hidden engine behind length "
  "contraction, which depends on marking both ends of a moving object 'at the same "
  "time.'"),
 "how_it_works": (
  "Relative simultaneity works through the finite, frame-independent speed of light. "
  "Einstein defined simultaneity operationally: two distant events are simultaneous "
  "in a frame if light signals emitted at the events reach the frame's midpoint "
  "observer at the same instant. Apply that definition in a moving frame and the "
  "midpoint itself is moving relative to the embankment frame, so the light travel "
  "times differ. Quantitatively, two events separated by distance L along the motion "
  "that are simultaneous in the embankment frame differ in time by gamma·v·L/c² in "
  "the train frame. For a 100-meter train at 80 percent of light speed that is about "
  "445 nanoseconds — small, but real and measured in synchronized-clock experiments."),
 "key_points": [
  "Simultaneity is frame-dependent: no universal 'now' exists across space.",
  "Einstein's operational definition uses light signals reaching a midpoint observer.",
  "Time offset between frames: delta-t' = gamma * v * L / c^2 for separation L.",
  "This effect underlies length contraction and the Lorentz transformation's time term.",
  "Verified in experiments with synchronized atomic clocks in relative motion."],
 "requirements": [
  "The 'Two Postulates' record.",
  "Comfort with the train thought experiment."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "simultaneity",
 "sig_lens": (
  "The Signature consequence: a distributed Signature system has no universal 'now' "
  "either, so event ordering is always stamped per-frame. Signature logs never claim "
  "two distant events were simultaneous without naming the frame that judged them."),
},
{
 "key": "spacetime", "name": "Spacetime: The Four-Dimensional Continuum",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Spacetime is the four-dimensional continuum formed by treating the three "
  "dimensions of space and one dimension of time as a single unified geometry. "
  "Hermann Minkowski, Einstein's former teacher, introduced the idea in 1908: "
  "different observers slice spacetime into 'space' and 'time' differently — just "
  "as two people can slice a loaf at different angles — but the four-dimensional "
  "loaf itself is the same for everyone. Every event is a point in spacetime with "
  "coordinates (t, x, y, z); an object's history is a 'worldline' threading through "
  "it. The invariant all observers agree on is the spacetime interval, which plays "
  "the role distance plays in ordinary geometry. Special relativity is the physics "
  "of flat (Minkowski) spacetime; general relativity lets spacetime curve, and that "
  "curvature is gravity. Once spacetime is accepted, time dilation and length "
  "contraction stop looking like distortions and start looking like perspective — "
  "different frames simply view the same four-dimensional reality from different "
  "angles."),
 "how_it_works": (
  "Spacetime works as the arena in which physics happens. The Lorentz "
  "transformations are rotations in spacetime — they mix the t and x coordinates "
  "the way an ordinary rotation mixes x and y, except the 'rotation angle' is set "
  "by velocity and the geometry uses a minus sign on the time part. That minus sign "
  "creates the light cone structure: events inside your light cone can affect you, "
  "events outside cannot, and this causal structure is identical for all observers. "
  "Worldlines of massive objects always stay inside the light cone (slower than "
  "light); light itself travels exactly on it. General relativity generalizes the "
  "flat Minkowski metric to curved metrics, and free-falling objects follow "
  "geodesics — the straightest possible worldlines in curved spacetime."),
 "key_points": [
  "Spacetime unifies 3 space + 1 time dimensions; events are points (t, x, y, z).",
  "Minkowski (1908) reformulated special relativity as spacetime geometry.",
  "The spacetime interval is the frame-independent 'distance' all observers agree on.",
  "Light cones encode causality: only events inside the cone can influence each other.",
  "General relativity = curved spacetime; gravity is that curvature."],
 "requirements": [
  "The 'Simultaneity Is Relative' record.",
  "Basic comfort with 3D coordinates extended by one more axis."],
 "standards": ["SI units throughout", "metric signature (-,+,+,+)"],
 "citations": [CIT_E1905,
  "Minkowski, H. (1908). 'Space and Time.' Address to the 80th Assembly of German Natural Scientists.",
  CIT_STD],
 "demo_kind": "interval",
 "sig_lens": (
  "The Signature view: spacetime is the only honest map. A Signature system diagram "
  "plots events, not just objects — where and when together — because debugging a "
  "timing fault without the time axis is like navigating with half a map."),
},
# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "lorentz-transforms", "name": "The Lorentz Transformations",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "The Lorentz transformations are the exact equations that convert space and time "
  "coordinates between two inertial frames in relative motion: x' = gamma(x − vt) "
  "and t' = gamma(t − vx/c²), for a frame moving at speed v along the x-axis. "
  "Hendrik Lorentz discovered the mathematical form in 1904 while studying "
  "electromagnetism; Einstein in 1905 derived it from the two postulates and gave "
  "it physical meaning. The equations show space and time mixing: where you are "
  "affects when you judge events to happen, and vice versa. When v is tiny compared "
  "to c, gamma approaches 1 and the vx/c² term vanishes, and the transformations "
  "collapse back to Galileo's x' = x − vt, t' = t — which is why Newton never "
  "noticed the difference. Everything in special relativity — time dilation, "
  "length contraction, velocity addition, the Doppler shift — can be derived from "
  "these two lines, making them the working machinery of the theory."),
 "how_it_works": (
  "The transformations work by enforcing the two postulates mathematically. "
  "Demanding that a spherical light wave x² + y² + z² = c²t² look identical in "
  "both frames (postulate 2), plus linearity and the principle of relativity "
  "(postulate 1), forces the unique solution with gamma = 1/sqrt(1 − v²/c²). In "
  "practice, physicists transform events into the frame where a calculation is "
  "easiest — usually the rest frame of a particle — do the physics there, and "
  "transform back. The inverse transformation has the same form with v replaced by "
  "−v, guaranteeing the symmetry between frames. Applied twice, Lorentz "
  "transformations compose into another Lorentz transformation, which is why "
  "velocities add by the relativistic formula rather than by simple addition."),
 "key_points": [
  "x' = gamma(x - vt); t' = gamma(t - vx/c^2); y, z unchanged (motion along x).",
  "Derived by Einstein (1905) from the two postulates; Lorentz found the math in 1904.",
  "Reduce to Galilean transformations when v is much smaller than c.",
  "Inverse transform uses -v: full symmetry between frames.",
  "All of special relativity's effects derive from these equations."],
 "requirements": [
  "The 'Lorentz Factor' and 'Simultaneity Is Relative' records.",
  "Algebra with two variables."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [CIT_E1905,
  "Lorentz, H. A. (1904). 'Electromagnetic Phenomena in a System Moving with Any Velocity Smaller than that of Light.'",
  CIT_STD],
 "demo_kind": "lorentz",
 "sig_lens": (
  "The Signature use is literal: the Signature reference implementation of frame "
  "conversion is these two equations, tested by transforming an event out and back "
  "and demanding the original coordinates return exactly. A transform that cannot "
  "round-trip is not shipped."),
},
{
 "key": "velocity-addition", "name": "Relativistic Velocity Addition",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Relativistic velocity addition is the correct rule for combining speeds: if an "
  "object moves at speed u' in a frame that itself moves at speed v past you, you "
  "measure u = (u' + v)/(1 + u'v/c²) — not the simple sum u' + v. Fire a probe at "
  "half light speed from a ship moving at half light speed, and you measure 0.8c, "
  "not c. Fire photons (u' = c) from any moving source and the formula returns "
  "exactly c, as postulate 2 demands. At everyday speeds the denominator is "
  "essentially 1 and the rule reduces to ordinary addition, which is why no one "
  "noticed for centuries. The formula guarantees that no combination of "
  "slower-than-light speeds can ever reach or exceed c — the speed limit is "
  "built into the arithmetic itself, protecting causality in every frame."),
 "how_it_works": (
  "The formula works as a direct consequence of the Lorentz transformations. "
  "Velocity is dx/dt; transform both the displacement and the time interval with "
  "the Lorentz equations and divide, and the (1 + u'v/c²) denominator appears "
  "automatically from the t' = gamma(t − vx/c²) term — the relativity of "
  "simultaneity, doing its quiet work. Physicists use it constantly in collider "
  "physics: particles emerging from a collision at relativistic speeds in the "
  "center-of-mass frame must be transformed into the laboratory frame with this "
  "rule. It also resolves naive paradoxes, like why two headlights-on spaceships "
  "approaching each other at 0.75c each see the other approaching at 0.96c, not "
  "1.5c."),
 "key_points": [
  "u = (u' + v)/(1 + u'v/c^2): the exact combination rule for collinear speeds.",
  "0.5c + 0.5c = 0.8c; 0.9c + 0.9c = 0.9945c; c + anything = c.",
  "Reduces to ordinary addition when speeds are far below c.",
  "No combination of sublight speeds reaches c: causality is arithmetically protected.",
  "Essential in particle-collider data analysis."],
 "requirements": [
  "The 'Lorentz Transformations' record.",
  "Fraction arithmetic."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "veladd",
 "sig_lens": (
  "The Signature check on any speed-combining code: feed it c and demand c back. "
  "If a Signature navigation routine can produce a superluminal closing speed, the "
  "routine is wrong, not the universe — the formula above is the acceptance test."),
},
{
 "key": "mass-energy", "name": "Mass-Energy Equivalence (E = mc^2)",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Mass-energy equivalence is Einstein's 1905 discovery that mass is a form of "
  "energy: E = mc², where a mass m at rest embodies energy E, with c² as the "
  "conversion factor. Because c² is enormous (about 9×10^16 in SI units), tiny "
  "masses hold staggering energy — one kilogram equals about 9×10^16 joules, "
  "roughly the yield of a 21-megaton bomb, and one gram equals the energy of "
  "about 21 kilotons. The Sun shines by converting about 4.3 million tons of mass "
  "into energy every second through nuclear fusion. The full relation is E² = "
  "(pc)² + (mc²)², covering moving objects too; E = mc² is the rest-energy case. "
  "The equation is verified daily: particle masses are measured by the energy "
  "released when they are created or destroyed, and nuclear reactors and the Sun "
  "balance their books with it exactly."),
 "how_it_works": (
  "Mass-energy equivalence works because relativity unifies the conservation laws: "
  "what is conserved is total energy, and mass contributes mc² to the total. In "
  "nuclear fusion, the helium nucleus weighs slightly less than the hydrogen "
  "nuclei that formed it, and the missing mass appears as kinetic energy and "
  "radiation — the books balance only when mass is counted as energy. Einstein's "
  "original 1905 derivation considered a body emitting two light pulses in "
  "opposite directions and showed its mass must decrease by E/c². Modern particle "
  "physics inverts the relation constantly: colliders convert kinetic energy into "
  "new massive particles, manufacturing mass from pure motion."),
 "key_points": [
  "E = mc^2: rest mass m embodies energy E; c^2 (~9x10^16 J/kg) is the conversion.",
  "Full form E^2 = (pc)^2 + (mc^2)^2 includes momentum for moving bodies.",
  "The Sun converts ~4.3 million tons of mass to energy every second.",
  "Nuclear binding-energy differences are weighed as mass differences.",
  "Particle colliders routinely convert kinetic energy into new mass."],
 "requirements": [
  "The 'Lorentz Factor' record.",
  "Scientific notation (powers of ten)."],
 "standards": ["SI units throughout", "c = 299,792,458 m/s (exact, SI definition)"],
 "citations": [
  "Einstein, A. (1905). 'Does the Inertia of a Body Depend Upon Its Energy Content?' Annalen der Physik, 18, 639-641.",
  CIT_STD],
 "demo_kind": "emc2",
 "sig_lens": (
  "The Signature accounting rule: energy books must balance with mass on the "
  "ledger. Any Signature energy design — reactors, batteries, beams — converts "
  "between mass and energy with E = mc^2 as the exchange rate, and the design "
  "review checks the rate explicitly."),
},
{
 "key": "relativistic-momentum", "name": "Relativistic Momentum and Energy",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Relativistic momentum and energy generalize Newton's p = mv and kinetic energy "
  "to all speeds: momentum is p = gamma·m·v and total energy is E = gamma·m·c², "
  "with gamma the Lorentz factor. At low speeds gamma is nearly 1 and both reduce "
  "to the familiar Newtonian forms; near light speed, gamma grows without bound, "
  "so momentum and energy grow without bound too — pushing a particle ever closer "
  "to c takes ever more energy, diverging to infinity at c itself. The two are "
  "linked by the invariant E² − (pc)² = (mc²)², which every observer agrees on, "
  "just as all observers agree on the spacetime interval. Photons, with zero rest "
  "mass, carry momentum p = E/c — sunlight exerts real pressure, and solar sails "
  "are designed around it. These formulas are the daily working tools of "
  "accelerator physics: every collider's magnets and detectors are sized with "
  "them."),
 "how_it_works": (
  "The relativistic formulas work by preserving conservation laws in all frames. "
  "Newton's p = mv fails at high speeds because it is not conserved under Lorentz "
  "transformations; multiplying by gamma repairs it, giving a momentum four-vector "
  "(E/c, px, py, pz) that transforms cleanly between frames. Its squared length, "
  "E² − (pc)², is invariant and equals (mc²)² — the particle's rest energy squared — "
  "so measuring a particle's energy and momentum reveals its mass even when the "
  "particle is never at rest. Kinetic energy is the excess over rest energy: "
  "(gamma − 1)mc². In colliders, this is why doubling a beam's energy less than "
  "doubles its speed but keeps raising its momentum — the extra energy goes into "
  "gamma, not velocity."),
 "key_points": [
  "p = gamma*m*v; E = gamma*m*c^2; kinetic energy = (gamma - 1)*m*c^2.",
  "E^2 - (pc)^2 = (mc^2)^2 is invariant: all observers agree on it.",
  "Energy and momentum diverge as v approaches c: the light-speed barrier in action.",
  "Photons carry momentum p = E/c despite zero rest mass (radiation pressure).",
  "Collider magnets, beam energies, and detector calibrations all use these forms."],
 "requirements": [
  "The 'Mass-Energy Equivalence' record.",
  "Comfort with p = mv from Newtonian physics."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905,
  "Planck, M. (1906). 'The Principle of Relativity and the Fundamental Equations of Mechanics.'",
  CIT_STD],
 "demo_kind": "relmom",
 "sig_lens": (
  "The Signature sizing rule: never size a relativistic beamline with Newtonian "
  "momentum. Signature accelerator notes carry the invariant E^2 - (pc)^2 on every "
  "page, because that is the quantity every frame agrees on and therefore the "
  "only safe one to design against."),
},
{
 "key": "spacetime-interval", "name": "The Spacetime Interval and Causality",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "The spacetime interval is the frame-independent 'distance' between two events "
  "in spacetime: s² = −c²Δt² + Δx² + Δy² + Δz² (with the common −+++ sign "
  "convention). While different observers disagree on the time separation and the "
  "spatial separation individually, every observer computes the same s² — it is "
  "the invariant core of special relativity, the thing that survives all Lorentz "
  "transformations. Its sign classifies every pair of events: timelike (s² < 0) "
  "events can be causally connected, since something slower than light can travel "
  "between them; lightlike (s² = 0) events are connectable only by light; spacelike "
  "(s² > 0) events cannot influence each other at all, because influence would have "
  "to outrun light. This classification is absolute — all observers agree on which "
  "pairs can be cause and effect — so causality itself is protected by the "
  "geometry of spacetime, in every frame, with no exceptions."),
 "how_it_works": (
  "The interval works as relativity's universal yardstick. It is derived by "
  "demanding that the light-cone equation x² + y² + z² = c²t² keep its form under "
  "Lorentz transformations — the quantity s² is exactly what is preserved. "
  "Physicists use it to settle causal questions without transforming frames: "
  "compute s² once, and its sign answers whether event A could have influenced "
  "event B for every observer simultaneously. For timelike pairs, the interval "
  "gives the proper time between the events (tau = sqrt(−s²)/c) — the time a clock "
  "carried between them would read, the maximum aging any traveler between the "
  "events can achieve. That maximum-aging property is the resolution of the twin "
  "paradox."),
 "key_points": [
  "s^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2: identical for all inertial observers.",
  "Timelike (s^2<0): causal contact possible. Lightlike (s^2=0): light only. Spacelike (s^2>0): no contact possible.",
  "Causal classification is absolute — every frame agrees on it.",
  "Proper time between timelike events: tau = sqrt(-s^2)/c, the maximum possible aging.",
  "Settles cause-and-effect questions without any frame transformation."],
 "requirements": [
  "The 'Spacetime' record.",
  "Comfort with squared quantities and square roots."],
 "standards": ["SI units throughout", "metric signature (-,+,+,+)"],
 "citations": [CIT_E1905,
  "Minkowski, H. (1908). 'Space and Time.'",
  CIT_STD],
 "demo_kind": "interval",
 "sig_lens": (
  "The Signature causality audit: before any two Signature events are ordered as "
  "cause and effect, the interval between them is computed. Spacelike-separated "
  "events are never ordered — the log records them as unordered, because physics "
  "forbids the claim."),
},
{
 "key": "twin-paradox", "name": "The Twin Paradox",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The twin paradox is the famous scenario: one twin stays on Earth while the "
  "other rockets to a distant star at near light speed and returns, and the "
  "traveler comes home younger — having aged less than the stay-at-home twin. It "
  "looks paradoxical because time dilation is symmetric: shouldn't each twin see "
  "the other's clock running slow? The resolution is that the situations are not "
  "symmetric — the traveler must turn around, and turning around requires "
  "acceleration, which means the traveler does not stay in a single inertial "
  "frame. The Earth twin's worldline between departure and reunion is straight "
  "(maximal proper time); the traveler's is bent, and in spacetime geometry the "
  "straight path between two events has the longest proper time — the reverse of "
  "Euclidean intuition. Send a twin to a star 4 light-years away at 80 percent of "
  "light speed: Earth waits 10 years; the traveler ages only 6. The effect is "
  "real, measured with atomic clocks, and fully consistent — there is no paradox, "
  "only the geometry of spacetime."),
 "how_it_works": (
  "The paradox resolves through proper time along worldlines. Each twin's aging "
  "is the spacetime length of their worldline between the shared departure and "
  "reunion events. The stay-at-home twin's worldline is straight, accumulating "
  "the full coordinate time; the traveler's worldline has a kink at the turnaround, "
  "and each leg accumulates only 1/gamma of the Earth-frame leg time. With v = "
  "0.8c, gamma = 1.667, so each 5-year (Earth) leg ages the traveler 3 years — 6 "
  "years total against Earth's 10. During the outbound and inbound legs each twin "
  "does see the other's clock slow; the turnaround is when the traveler's notion "
  "of simultaneity swings violently, re-dating the Earth twin's clock forward. "
  "Atomic-clock experiments flying clocks around the world confirm the accounting "
  "exactly."),
 "key_points": [
  "Traveler ages less because their worldline between reunion events is bent, not straight.",
  "Straight worldlines maximize proper time — reversed from Euclidean intuition.",
  "Acceleration (the turnaround) breaks the symmetry between the twins.",
  "Example: 0.8c to a star 4 light-years out and back: 10 years Earth, 6 years traveler.",
  "Confirmed by flown atomic clocks; no genuine paradox remains."],
 "requirements": [
  "The 'Time Dilation' and 'Spacetime Interval' records.",
  "Accepting that acceleration is detectable without outside reference."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905,
  "Langevin, P. (1911). 'The Evolution of Space and Time.' Scientia, 10, 31-54.",
  "Hafele, J. C., & Keating, R. E. (1972). 'Around-the-World Atomic Clocks.' Science, 177, 166-170.",
  CIT_STD],
 "demo_kind": "twin",
 "sig_lens": (
  "The Signature moral: the longest path through spacetime is the straight one. "
  "Signature mission planning uses proper time, not coordinate time, to budget "
  "crew aging and clock drift — the worldline is the schedule, and bent worldlines "
  "cost time."),
},
{
 "key": "relativistic-doppler", "name": "The Relativistic Doppler Effect",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The relativistic Doppler effect is the shift in observed wavelength of light "
  "from a moving source: receding sources are redshifted (stretched to longer "
  "wavelengths), approaching sources are blueshifted. For motion along the line "
  "of sight, the observed-to-emitted wavelength ratio is sqrt((1+beta)/(1-beta)) "
  "for recession, with beta = v/c — at half light speed receding, light arrives "
  "at 1.73 times its emitted wavelength (redshift z = 0.73). Unlike sound, the "
  "relativistic formula needs no medium and includes time dilation: there is also "
  "a transverse Doppler shift for motion across the line of sight, a pure time "
  "dilation effect with no classical analogue, confirmed in 1938 by Ives and "
  "Stilwell. Cosmologists use redshift to measure the universe's expansion — "
  "distant galaxies show redshifts proportional to distance (Hubble's law) — and "
  "astronomers use Doppler shifts to weigh exoplanets, clock binary pulsars, and "
  "map galactic rotation."),
 "how_it_works": (
  "The effect works through the combination of classical wave spacing and time "
  "dilation. Successive wave crests are emitted farther apart when the source "
  "recedes (the classical part), and the source's own clock runs slow by gamma, "
  "stretching the emission interval further (the relativistic part); multiplying "
  "both gives the square-root formula. Because the derivation uses only the "
  "Lorentz transformation of the wave's phase, the shift is exact at all speeds "
  "with no medium required. The transverse effect — redshift for purely sideways "
  "motion, where the classical contribution is zero — isolates time dilation "
  "cleanly and was one of its first direct confirmations. In cosmology the same "
  "mathematics describes how expanding space stretches light during its journey, "
  "connecting observed redshift to the scale factor of the universe."),
 "key_points": [
  "Recession redshifts, approach blueshifts: ratio sqrt((1+beta)/(1-beta)) along line of sight.",
  "At 0.5c receding: wavelengths stretch 1.73x (z = 0.73).",
  "Transverse Doppler shift is pure time dilation — no classical analogue (Ives-Stilwell, 1938).",
  "Needs no medium, unlike sound; exact at all speeds.",
  "Foundation of Hubble's law, exoplanet detection, and precision pulsar timing."],
 "requirements": [
  "The 'Time Dilation' record.",
  "Wavelength vs. frequency relationship (longer wavelength = redder)."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905,
  "Ives, H. E., & Stilwell, G. R. (1938). 'An Experimental Study of the Rate of a Moving Atomic Clock.' Journal of the Optical Society of America, 28, 215-226.",
  CIT_STD],
 "demo_kind": "doppler",
 "sig_lens": (
  "The Signature application: every Signature spectral measurement is reduced to "
  "the emitter's rest frame with the square-root formula before any analysis. "
  "Raw observed wavelengths are instrument-frame artifacts; rest-frame wavelengths "
  "are the data."),
},
{
 "key": "proper-time-length", "name": "Proper Time and Proper Length",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Proper time and proper length are the measurements made in an object's own "
  "rest frame — the time read by a clock traveling with the object, and the "
  "length measured with rulers at rest relative to it. They are the 'true' "
  "personal quantities of the object: every other inertial frame measures "
  "dilated times (longer by gamma) and contracted lengths (shorter by gamma), "
  "but all frames agree on the proper values, which can be recovered from any "
  "frame via the invariants. Proper time is the spacetime length of a worldline: "
  "for a straight (inertial) worldline it is maximal between two events, which "
  "is why the stay-at-home twin ages most. For accelerated motion, proper time "
  "is the integral of sqrt(1 − v(t)²/c²)dt along the path — the clock hypothesis, "
  "verified to extreme precision, states that an ideal clock's rate depends only "
  "on its instantaneous speed, never on its acceleration. These are the "
  "quantities physicists actually compute with, because they are frame-free."),
 "how_it_works": (
  "Proper quantities work as the invariants everything else is computed from. "
  "Given any frame's measurements, proper time follows from the spacetime "
  "interval (tau = sqrt(−s²)/c for timelike separations) and proper length from "
  "the Lorentz contraction formula inverted (L0 = gamma·L). The clock hypothesis "
  "— that acceleration itself doesn't slow clocks, only speed does — lets "
  "physicists integrate proper time along arbitrary trajectories, which is how "
  "the twin paradox's turnaround is handled exactly. Particle physicists quote "
  "lifetimes as proper lifetimes (the muon's 2.2 microseconds) and compute "
  "laboratory lifetimes by multiplying by the particle's gamma. In general "
  "relativity the same idea generalizes: proper time is the integral of the "
  "metric along a worldline, the fundamental observable of the theory."),
 "key_points": [
  "Proper time: clock's own reading; proper length: ruler-at-rest measurement.",
  "All frames agree on proper quantities; they are recovered via invariants.",
  "Straight worldlines maximize proper time between two events.",
  "Clock hypothesis: ideal clocks care about speed only, not acceleration.",
  "Particle lifetimes are quoted as proper lifetimes, scaled by gamma in the lab."],
 "requirements": [
  "The 'Time Dilation', 'Length Contraction', and 'Spacetime Interval' records.",
  "Basic idea of integration (accumulating small pieces) — optional."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1905, CIT_STD],
 "demo_kind": "propertime",
 "sig_lens": (
  "The Signature standard: archive proper quantities, derive frame quantities. "
  "A Signature database stores each event's proper time and each object's proper "
  "length as canonical, because those are the numbers no frame dispute can move."),
},
{
 "key": "michelson-morley", "name": "The Michelson-Morley Experiment",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The Michelson-Morley experiment (1887) is the most famous null result in "
  "physics: it tried to detect Earth's motion through the hypothetical 'luminiferous "
  "ether' — the medium then believed to carry light — and found nothing. Albert "
  "Michelson and Edward Morley split a light beam, sent the halves along "
  "perpendicular arms, and recombined them; Earth's 30 km/s orbital motion "
  "should have made light travel measurably faster along one arm than the other, "
  "shifting the interference fringes by about 0.4 fringes as the apparatus "
  "rotated. The observed shift was less than a hundredth of that — consistent "
  "with zero. Repeated with ever-greater precision for 140 years, the null "
  "result stands: there is no ether wind, and light speed is isotropic for every "
  "observer. Einstein cited the result as key evidence for his second postulate, "
  "and modern versions using lasers and cryogenic resonators confirm isotropy to "
  "parts in 10^18."),
 "how_it_works": (
  "The experiment works as an exquisitely sensitive speedometer for light. The "
  "interferometer compares round-trip light travel times along two perpendicular "
  "paths; any difference in light speed along the arms shifts the interference "
  "fringe pattern. Classical ether theory predicted a shift proportional to "
  "v²/c² — small (one part in a hundred million for Earth's orbital speed) but "
  "well within the instrument's reach, since the 11-meter effective path length "
  "magnified it to nearly half a fringe. Rotating the whole apparatus through 90 "
  "degrees should have swapped the arms' roles and produced a clear signal. The "
  "absence of any shift killed the ether and, together with Maxwell's equations, "
  "left Einstein's postulate — light speed constant for all observers — as the "
  "only consistent explanation."),
 "key_points": [
  "1887: Michelson and Morley found no ether wind; fringe shift < 0.01 vs 0.4 expected.",
  "Expected shift: delta-N = (2L/lambda)(v^2/c^2) with L = 11 m, v = 30 km/s.",
  "The most famous null result in science — and one of the most replicated.",
  "Key experimental pillar of the light-speed postulate.",
  "Modern laser versions confirm isotropy to parts in 10^18."],
 "requirements": [
  "The 'Two Postulates' record.",
  "Basic idea of wave interference (optional)."],
 "standards": ["SI units throughout"],
 "citations": [CIT_MM, CIT_E1905,
  "Herrmann, S., et al. (2009). 'Rotating Optical Cavity Experiment Testing Lorentz Invariance.' Physical Review D, 80, 105011.",
  CIT_STD],
 "demo_kind": "michelson",
 "sig_lens": (
  "The Signature respect for null results: the experiment that finds nothing, "
  "cleanly, outranks the experiment that finds something messily. Signature test "
  "protocols require a stated expected signal size before the run — like the 0.4 "
  "fringes — so that a null result is a measurement, not a failure."),
},

{
 "key": "equivalence-principle", "name": "The Equivalence Principle",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "The equivalence principle is Einstein's bridge from special to general "
  "relativity: locally, the effects of gravity are indistinguishable from the "
  "effects of acceleration. Einstein called its 1907 realization his 'happiest "
  "thought' — a person falling from a roof feels weightless, exactly as if "
  "floating in deep space, while a person in a rocket accelerating at 1g in deep "
  "space feels pressed to the floor exactly as if standing on Earth. No local "
  "experiment can tell the two apart. The principle rests on a deep observed "
  "fact: inertial mass (resistance to acceleration) equals gravitational mass "
  "(response to gravity) to extraordinary precision — the MICROSCOPE satellite "
  "(2022) confirmed it to about one part in 10^15. From this single principle "
  "Einstein derived gravitational time dilation, the bending of light, and "
  "gravitational redshift years before he had the full field equations. It "
  "remains the conceptual core of general relativity: gravity is not a force "
  "but the shape of spacetime, and free fall is just coasting along it."),
 "how_it_works": (
  "The principle works by reinterpreting gravity geometrically. If a sealed "
  "laboratory cannot distinguish uniform gravity from uniform acceleration, then "
  "the 'gravitational force' felt standing on Earth is really the floor "
  "accelerating you upward through spacetime while your natural free-fall path "
  "would curve downward. Light must bend in an accelerating rocket (a horizontal "
  "beam appears to sag toward the floor), so by equivalence it must bend in a "
  "gravitational field too — a prediction confirmed in 1919. Clocks run slow in "
  "an accelerating frame (the rear clock lags), so they must run slow deep in a "
  "gravitational field — gravitational time dilation, confirmed by Pound-Rebka "
  "and by every GPS satellite. General relativity is what you get when you "
  "demand the equivalence principle hold at every point of a spacetime whose "
  "curvature can vary from place to place."),
 "key_points": [
  "Local indistinguishability of gravity and acceleration (Einstein's 'happiest thought,' 1907).",
  "Rests on inertial mass = gravitational mass, tested to ~1 part in 10^15 (MICROSCOPE, 2022).",
  "Predicts light bending, gravitational redshift, and gravitational time dilation.",
  "Implies gravity is spacetime geometry, not a force; free fall is inertial motion.",
  "The conceptual foundation of general relativity."],
 "requirements": [
  "The 'Inertial Reference Frames' record.",
  "Newton's gravity (F = GmM/r^2) for contrast."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1916,
  "Touboul, P., et al. (2022). 'MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle.' Physical Review Letters, 129, 121102.",
  CIT_STD],
 "demo_kind": "equiv",
 "sig_lens": (
  "The Signature design import: equivalence is a test protocol. Any Signature "
  "inertial sensor must read identically under 1g of gravity and 1g of thrust — "
  "if it can tell them apart, the sensor is miscalibrated, because physics says "
  "the distinction does not locally exist."),
},
{
 "key": "spacetime-curvature", "name": "Spacetime Curvature",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Spacetime curvature is general relativity's replacement for Newton's "
  "gravitational force: mass and energy warp the geometry of spacetime, and "
  "objects move along the straightest possible paths (geodesics) through that "
  "warped geometry. John Archibald Wheeler's summary is canonical: 'Spacetime "
  "tells matter how to move; matter tells spacetime how to curve.' Curvature "
  "shows up as the failure of Euclidean rules — on a positively curved surface "
  "like a sphere, a triangle's angles sum to more than 180 degrees (a triangle "
  "covering an eighth of a sphere has three right angles: 270 degrees total). "
  "Near Earth the curvature is gentle but real; near a black hole it is extreme "
  "enough to trap light. The curvature at each point is encoded in the Riemann "
  "curvature tensor, a mathematical object with 256 components (20 independent "
  "in four dimensions) that measures precisely how much initially parallel "
  "geodesics converge or diverge — the geometric meaning of tidal gravity."),
 "how_it_works": (
  "Curvature works through geodesic deviation: release two nearby freely falling "
  "particles, and in curved spacetime their separation changes — they drift "
  "together or apart — even though each feels no force. That relative "
  "acceleration is tidal gravity, and it is the directly measurable face of "
  "curvature (ocean tides are Earth's tidal field in action). Mathematically, "
  "the metric tensor g describes distances in spacetime at each point, and the "
  "Einstein field equations dictate how mass-energy determines the metric; the "
  "Riemann tensor is computed from the metric's second derivatives. A useful "
  "picture: the rubber-sheet analogy, where a bowling ball dents a sheet and "
  "marbles spiral in — imperfect (it needs gravity to pull the marbles down) "
  "but correct about the essential point that orbits are straight lines in a "
  "curved geometry, not circles held by a force."),
 "key_points": [
  "'Spacetime tells matter how to move; matter tells spacetime how to curve' (Wheeler).",
  "Curvature = failure of Euclidean geometry (e.g., spherical triangle angles sum > 180 deg).",
  "Measurable as geodesic deviation: nearby free-fall paths converge/diverge (tidal gravity).",
  "Encoded in the Riemann tensor (20 independent components in 4D spacetime).",
  "Orbits are geodesics — straightest paths in curved spacetime, not forced circles."],
 "requirements": [
  "The 'Equivalence Principle' and 'Spacetime' records.",
  "Willingness to think of geometry as flexible."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1916, CIT_STD],
 "demo_kind": "curvature",
 "sig_lens": (
  "The Signature modeling rule: simulate the geometry, not the force. Where a "
  "Signature system models gravity — orbital tools, drop-test rigs — it "
  "integrates geodesics through a metric rather than adding a force vector, "
  "because the geometric form stays correct where the force picture breaks."),
},
{
 "key": "einstein-field-equations", "name": "The Einstein Field Equations",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "The Einstein field equations are the master equations of general relativity, "
  "published by Einstein in November 1915: R_uv − ½Rg_uv + Λg_uv = (8πG/c⁴)T_uv. "
  "The left side describes the curvature of spacetime (the Ricci tensor R_uv, "
  "the Ricci scalar R, the metric g_uv, and the cosmological constant Λ); the "
  "right side describes the mass-energy content (the stress-energy tensor T_uv), "
  "with Newton's constant G and c⁴ setting the coupling strength. In words: the "
  "curvature of spacetime at each point is determined by the energy and momentum "
  "there. They are ten coupled nonlinear partial differential equations — "
  "famously difficult; exact solutions exist only for highly symmetric cases "
  "like the Schwarzschild (non-rotating mass) and Kerr (rotating mass) metrics. "
  "Yet they predict, with quantitative precision, the bending of starlight, the "
  "orbit of Mercury, gravitational time dilation, black holes, gravitational "
  "waves, and the expansion of the universe. Solving them numerically for "
  "colliding black holes took decades of supercomputer development and was "
  "vindicated by LIGO's detections."),
 "how_it_works": (
  "The equations work as a two-way law: pick a mass-energy distribution T_uv, "
  "and the equations constrain the spacetime metric g_uv; then matter and light "
  "move on geodesics of that metric. In the weak-field, slow-motion limit they "
  "reduce exactly to Newton's Poisson equation for gravity, which is why Newton "
  "worked for 250 years. Exact solutions are found by imposing symmetry: assume "
  "a static spherical mass and the equations yield the Schwarzschild metric, "
  "which predicts Mercury's 43-arcsecond-per-century perihelion shift and the "
  "1.75-arcsecond bending of starlight. For dynamic situations like merging "
  "black holes there is no exact solution, so physicists evolve the equations "
  "numerically on supercomputers — numerical relativity — and the resulting "
  "gravitational waveforms matched LIGO's signals template-for-template."),
 "key_points": [
  "R_uv - 1/2 R g_uv + Lambda g_uv = (8 pi G/c^4) T_uv: curvature = mass-energy content.",
  "Published November 1915; ten coupled nonlinear partial differential equations.",
  "Reduce to Newtonian gravity in the weak-field, slow-motion limit.",
  "Exact solutions: Schwarzschild (1916), Kerr (1963), FLRW cosmology.",
  "Numerical solutions predicted the black-hole-merger waveforms LIGO detected."],
 "requirements": [
  "The 'Spacetime Curvature' record.",
  "Tensor notation is helpful but the conceptual form suffices for this tier."],
 "standards": ["SI units throughout", "G = 6.67430e-11 m^3 kg^-1 s^-2"],
 "citations": [CIT_E1915, CIT_E1916,
  "Schwarzschild, K. (1916). 'On the Gravitational Field of a Mass Point According to Einstein's Theory.'",
  CIT_STD],
 "demo_kind": "perihelion",
 "sig_lens": (
  "The Signature stance on the field equations: they are the acceptance suite. "
  "Any Signature gravity model — however simplified for real-time use — must "
  "reproduce the Schwarzschild predictions (43 arcseconds, 1.75 arcseconds) to "
  "declared tolerance, or it is not a relativity model."),
},
# -------------------------------------------------------------------- ADVANCED
{
 "key": "gravitational-time-dilation", "name": "Gravitational Time Dilation",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Gravitational time dilation is the slowing of time deep in a gravitational "
  "field: a clock closer to a massive body ticks slower than an identical clock "
  "farther away, as measured by a distant observer. Near a non-rotating mass, "
  "the rate is d_tau = dt·sqrt(1 − rs/r), where rs = 2GM/c² is the Schwarzschild "
  "radius. The effect is tiny on Earth — a clock at sea level loses about 22 "
  "milliseconds per year relative to one far from Earth — but it is measurable: "
  "Pound and Rebka (1959) detected the corresponding gravitational redshift of "
  "gamma rays over just 22.5 meters of Harvard tower height. It dominates the "
  "relativistic corrections in GPS: satellite clocks, high above Earth's gravity "
  "well, run fast by about 45.9 microseconds per day from gravity, outweighing "
  "their 7.2-microsecond special-relativistic slowing for a net +38.6 "
  "microseconds per day. At a black hole's event horizon the factor reaches "
  "zero: to a distant observer, time stops at the horizon entirely."),
 "how_it_works": (
  "Gravitational time dilation works through the equivalence principle plus the "
  "geometry of the Schwarzschild metric. In an accelerating rocket, light "
  "signals sent from the rear to the front arrive redshifted because the front "
  "is receding during the light's travel; clocks at the rear must therefore be "
  "ticking slower as judged from the front. By equivalence, the same holds in "
  "gravity: deeper clocks tick slower. The Schwarzschild solution makes it "
  "quantitative — the metric's time component g_tt = −(1 − rs/r) directly gives "
  "the ticking rate of stationary clocks. GPS engineers apply it daily: each "
  "satellite's atomic clock is factory-offset so it ticks at the correct rate "
  "once in orbit, and receivers solve for position using light-travel times "
  "that assume the correction. Without it, navigation errors would grow about "
  "11 kilometers per day."),
 "key_points": [
  "Deeper in a gravity well, clocks tick slower: d_tau = dt*sqrt(1 - rs/r).",
  "Sea-level clock loses ~22 ms/year vs. a clock far from Earth.",
  "Pound-Rebka (1959) measured gravitational redshift over 22.5 m.",
  "GPS: +45.9 us/day (gravity) vs -7.2 us/day (motion) = net +38.6 us/day.",
  "At a black hole's event horizon, the factor hits zero: time 'stops' for distant observers."],
 "requirements": [
  "The 'Equivalence Principle' and 'Einstein Field Equations' records.",
  "Square roots; comfort with the Schwarzschild radius formula."],
 "standards": ["SI units throughout", "G = 6.67430e-11 m^3 kg^-1 s^-2"],
 "citations": [CIT_E1916,
  "Pound, R. V., & Rebka, G. A. (1960). 'Apparent Weight of Photons.' Physical Review Letters, 4, 337-341.",
  CIT_STD],
 "demo_kind": "grtimedil",
 "sig_lens": (
  "The Signature timing discipline: altitude is a clock correction. Any Signature "
  "system fusing timestamps from sensors at different heights applies the "
  "Schwarzschild factor before comparing them — a mountain-top sensor and a "
  "valley sensor are in different time zones of physics, not just geography."),
},
{
 "key": "geodesics", "name": "Geodesics: The Straightest Paths in Curved Spacetime",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A geodesic is the straightest possible path through curved spacetime — the "
  "trajectory of any object in free fall, feeling no force. On Earth's curved "
  "surface, geodesics are great circles: intercontinental flights follow them, "
  "which is why the shortest New York–London route arcs far north over the "
  "Atlantic rather than following a straight line on a flat map (the great-circle "
  "route is about 5,570 km; the flat-map 'straight' line is longer). In "
  "spacetime, planets orbit the Sun along geodesics of the Schwarzschild "
  "geometry — no gravitational force pulls them; they coast straight through "
  "curved spacetime and the curvature bends their paths into ellipses. Light "
  "follows null geodesics, which is why gravity bends starlight. The geodesic "
  "equation, d²x/dτ² + Γ(dx/dτ)(dx/dτ) = 0, uses the Christoffel symbols Γ "
  "computed from the metric; in flat spacetime the Γ terms vanish and geodesics "
  "are ordinary straight lines at constant velocity — Newton's first law, "
  "recovered."),
 "how_it_works": (
  "Geodesics work as the generalization of 'straight line' to curved geometry. "
  "They extremize the spacetime interval between two events — for massive "
  "objects, they maximize proper time, which is why free-falling objects are "
  "the true inertial observers of general relativity (standing on the ground, "
  "you are the one accelerating). Mission planners compute spacecraft "
  "trajectories as geodesics of the solar system's metric plus small thrust "
  "corrections; GPS satellites' orbits are geodesics of Earth's Schwarzschild "
  "field to the precision needed. The Christoffel symbols in the geodesic "
  "equation encode how the coordinate grid itself twists from point to point — "
  "they are the 'fictitious forces' of curved coordinates, vanishing in free-"
  "falling local frames exactly as the equivalence principle demands."),
 "key_points": [
  "Geodesics = straightest paths in curved spacetime = free-fall trajectories.",
  "On a sphere: great circles (why flights arc north on flat maps).",
  "Planetary orbits are spacetime geodesics — no force pulls the planets.",
  "Light follows null geodesics: gravity bends starlight.",
  "In flat spacetime the geodesic equation reduces to Newton's first law."],
 "requirements": [
  "The 'Spacetime Curvature' record.",
  "Great-circle idea from geography is enough intuition."],
 "standards": ["SI units throughout", "Earth radius 6,371 km"],
 "citations": [CIT_E1916, CIT_STD],
 "demo_kind": "geodesic",
 "sig_lens": (
  "The Signature navigation principle: plot the geodesic first, then budget "
  "thrust. A Signature trajectory plan starts from the free-fall path — the "
  "geometry's own answer — and treats every burn as a priced deviation from it, "
  "never the other way around."),
},

{
 "key": "black-holes", "name": "Black Holes",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A black hole is a region of spacetime where gravity is so strong that nothing "
  "— not even light — can escape: the escape velocity exceeds c. It forms when a "
  "massive star's core collapses past the point where any known force can hold it "
  "up, crushing matter inside its Schwarzschild radius rs = 2GM/c² (about 3 km "
  "per solar mass; Earth's would be 9 mm). The boundary, the event horizon, is a "
  "one-way surface: cross it and all future worldlines point inward toward the "
  "singularity. Karl Schwarzschild found the first exact solution of the field "
  "equations describing one in 1916, months after Einstein published them. "
  "Skepticism lasted decades, but the evidence is now overwhelming: Cygnus X-1 "
  "(identified 1971) pours X-rays from gas spiraling into a stellar black hole; "
  "the Event Horizon Telescope imaged the shadows of M87* (2019) and our own "
  "galaxy's Sagittarius A* (2022); and LIGO hears stellar black holes merging "
  "across the universe. They are no longer theory — they are observed "
  "astrophysical objects, and general relativity predicts their properties "
  "exactly."),
 "how_it_works": (
  "A black hole works as pure curved spacetime: inside the horizon, spacetime is "
  "tilted so steeply that the future light cone points entirely inward — moving "
  "toward the singularity becomes as unavoidable as moving toward tomorrow. The "
  "no-hair theorem states that a settled black hole is described by just three "
  "numbers: mass, spin, and charge (the Kerr metric for rotating holes, found "
  "1963). Matter falling in forms a superheated accretion disk whose friction "
  "glows in X-rays — how we spot them. Hawking's 1974 quantum calculation showed "
  "black holes slowly evaporate by emitting thermal radiation, with temperature "
  "inversely proportional to mass; stellar black holes take vastly longer than "
  "the age of the universe to evaporate. Tidal forces near small black holes "
  "'spaghettify' infalling matter — stretched vertically, squeezed horizontally "
  "— while supermassive holes are gentle at the horizon."),
 "key_points": [
  "Escape velocity exceeds c inside the event horizon; rs = 2GM/c^2 (~3 km per solar mass).",
  "Schwarzschild (1916) found the first exact solution; Kerr (1963) added rotation.",
  "No-hair theorem: mass, spin, charge fully describe a settled black hole.",
  "Observed: Cygnus X-1 (1971), EHT images of M87* (2019) and Sgr A* (2022), LIGO mergers.",
  "Hawking radiation (1974): black holes slowly evaporate; stellar ones outlive the universe."],
 "requirements": [
  "The 'Einstein Field Equations' and 'Gravitational Time Dilation' records.",
  "Escape velocity concept from Newtonian physics."],
 "standards": ["SI units throughout", "G = 6.67430e-11 m^3 kg^-1 s^-2"],
 "citations": [CIT_E1915,
  "Schwarzschild, K. (1916). 'On the Gravitational Field of a Mass Point.'",
  "Kerr, R. P. (1963). 'Gravitational Field of a Spinning Mass.' Physical Review Letters, 11, 237-238.",
  "Event Horizon Telescope Collaboration (2019). 'First M87 Event Horizon Telescope Results.' The Astrophysical Journal Letters, 875, L1.",
  CIT_STD],
 "demo_kind": "schwarz",
 "sig_lens": (
  "The Signature treatment of black holes is as calibration endpoints: the most "
  "extreme predictions of the field equations, and the theory passes. A "
  "Signature physics archive keeps its hardest test cases front and center — if "
  "the model survives the horizon, it survives the laboratory."),
},
{
 "key": "gravitational-waves-gr", "name": "Gravitational Waves in General Relativity",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Gravitational waves are ripples in spacetime itself, propagating outward at "
  "the speed of light from accelerating masses — most powerfully from merging "
  "black holes and neutron stars. Einstein predicted them in 1916 from the "
  "linearized field equations; they stretch and squeeze space by a fractional "
  "amount called strain, roughly 10^-21 for detectable events — changing the "
  "Earth-Sun distance by less than an atomic diameter. For a century they were "
  "considered undetectable in practice, until LIGO's 4-kilometer laser "
  "interferometers measured the September 14, 2015 signal GW150914: two black "
  "holes of about 36 and 29 solar masses spiraling together 1.3 billion "
  "light-years away, converting 3 solar masses into pure gravitational-wave "
  "energy in a fifth of a second (announced February 2016). Dozens of mergers "
  "have been heard since, plus the 2017 neutron-star merger GW170817 seen in "
  "both gravitational waves and light. A new sense has opened: humanity now "
  "listens to the universe as well as looks at it."),
 "how_it_works": (
  "Gravitational waves work as propagating curvature. Accelerating a mass "
  "quadrupole — two masses orbiting — shakes the metric, and the disturbance "
  "radiates at c, carrying energy (the binary pulsar PSR B1913+16 was seen "
  "spiraling inward exactly as wave emission predicts, Nobel Prize 1993). "
  "LIGO detects them with Michelson interferometers: a passing wave stretches "
  "one 4-km arm while squeezing the other, shifting the interference pattern by "
  "less than a proton's width — measured via averaging and quantum-noise "
  "engineering. The signal's rising 'chirp' encodes the masses and distance; "
  "template banks of numerical-relativity waveforms are matched against the "
  "data. Pulsar timing arrays (NANOGrav, 2023) have now detected the "
  "nanohertz background hum of supermassive black-hole binaries, extending "
  "gravitational-wave astronomy to galaxy-scale wavelengths."),
 "key_points": [
  "Ripples in spacetime from accelerating masses; predicted by Einstein, 1916.",
  "Strain ~10^-21: a proton-width change over kilometers.",
  "GW150914 (2015): first direct detection; 36+29 solar-mass black holes, 1.3 billion light-years.",
  "Hulse-Taylor pulsar (1974) gave indirect proof; Nobel Prize 1993.",
  "LIGO/Virgo catalog dozens of mergers; pulsar timing arrays hear the nanohertz background."],
 "requirements": [
  "The 'Einstein Field Equations' and 'Black Holes' records.",
  "Interferometer idea from the Michelson-Morley record helps."],
 "standards": ["SI units throughout", "G = 6.67430e-11 m^3 kg^-1 s^-2"],
 "citations": [CIT_E1916,
  "Abbott, B. P., et al. (LIGO Scientific Collaboration) (2016). 'Observation of Gravitational Waves from a Binary Black Hole Merger.' Physical Review Letters, 116, 061102.",
  "Hulse, R. A., & Taylor, J. H. (1975). 'Discovery of a Pulsar in a Binary System.' The Astrophysical Journal, 195, L51-L53.",
  CIT_STD],
 "demo_kind": "gw",
 "sig_lens": (
  "The Signature lesson of LIGO: measure the 'impossible' anyway. A strain of "
  "10^-21 was declared undetectable for decades; the Signature build ethic takes "
  "the other side — specify the noise budget honestly, engineer to it, and let "
  "the universe surprise you."),
},
{
 "key": "expanding-universe", "name": "The Expanding Universe",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "The expanding universe is general relativity's prediction — confirmed by "
  "observation — that space itself is growing larger over time, carrying "
  "galaxies apart. Alexander Friedmann found expanding solutions of the field "
  "equations in 1922; Georges Lemaitre independently derived them in 1927; "
  "Edwin Hubble in 1929 observed that distant galaxies recede with speeds "
  "proportional to their distance (Hubble's law, v = H0·d). The expansion is "
  "not galaxies flying through space but space itself stretching — light from "
  "distant galaxies is cosmologically redshifted during its journey. Run the "
  "expansion backward and everything converges about 13.8 billion years ago: "
  "the Big Bang, corroborated by the cosmic microwave background (Penzias and "
  "Wilson, 1965) and the observed abundances of light elements. The current "
  "expansion rate, the Hubble constant, is about 70 km/s per megaparsec — and "
  "since 1998 we have known the expansion is accelerating, driven by dark "
  "energy."),
 "how_it_works": (
  "Cosmic expansion works through the Friedmann-Lemaitre-Robertson-Walker "
  "metric, the field equations' solution for a homogeneous, isotropic universe: "
  "distances scale with a cosmic scale factor a(t), and the Friedmann equations "
  "govern how a(t) evolves given the universe's matter, radiation, and dark "
  "energy content. Galaxies sit at fixed comoving coordinates while the scale "
  "factor grows between them — like raisins in rising bread dough. Redshift z "
  "measures how much the universe has expanded since the light left: a galaxy "
  "at z = 1 emitted its light when the universe was half its present size. The "
  "Hubble constant sets the current expansion rate; its precise value is under "
  "active dispute (the 'Hubble tension' between early- and late-universe "
  "measurements), one of cosmology's liveliest open problems."),
 "key_points": [
  "Space itself expands; galaxies are carried apart (Hubble's law: v = H0*d, 1929).",
  "Friedmann (1922) and Lemaitre (1927) found expanding solutions of the field equations.",
  "13.8-billion-year age from expansion + cosmic microwave background (1965) + element abundances.",
  "Cosmological redshift measures the scale factor at emission: z = 1 means half-size universe.",
  "Expansion is accelerating (1998): dark energy dominates the present cosmos."],
 "requirements": [
  "The 'Einstein Field Equations' and 'Relativistic Doppler Effect' records.",
  "Redshift z meaning: fractional wavelength stretch."],
 "standards": ["SI units throughout", "H0 ~ 70 km/s/Mpc"],
 "citations": [CIT_E1915,
  "Hubble, E. (1929). 'A Relation Between Distance and Radial Velocity Among Extra-Galactic Nebulae.' Proceedings of the National Academy of Sciences, 15, 168-173.",
  "Penzias, A. A., & Wilson, R. W. (1965). 'A Measurement of Excess Antenna Temperature at 4080 Mc/s.' The Astrophysical Journal, 142, 419-421.",
  CIT_STD],
 "demo_kind": "hubble",
 "sig_lens": (
  "The Signature cosmological habit: always ask what the scale factor was. A "
  "Signature archive of cosmic events indexes every entry by redshift as well as "
  "by date, because 'when' in an expanding universe is meaningless without "
  "'how big the universe was then.'"),
},
{
 "key": "frame-dragging", "name": "Frame Dragging (Lense-Thirring Effect)",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Frame dragging is general relativity's prediction that a rotating mass twists "
  "spacetime around with it, dragging nearby inertial frames into partial "
  "co-rotation — as if spacetime were a viscous fluid stirred by the spinning "
  "mass. Josef Lense and Hans Thirring derived it in 1918 from the weak-field "
  "field equations: a satellite orbiting a rotating planet has its orbital "
  "plane slowly precessed, and a gyroscope near the planet precesses in the "
  "rotation direction. The effect around Earth is minuscule — tens of "
  "milliarcseconds per year — but Gravity Probe B (2004-2005), with the most "
  "perfect gyroscopes ever flown, measured the frame-dragging drift at 37.2 ± "
  "7.2 milliarcseconds per year against the predicted 39.2, and the larger "
  "geodetic precession at 6,602 against 6,606 predicted. Near a rapidly "
  "spinning black hole, frame dragging is extreme: inside the ergosphere, "
  "spacetime rotates so fast that nothing can stand still — everything is "
  "forced to co-rotate, the mechanism behind the Penrose process for extracting "
  "a black hole's rotational energy."),
 "how_it_works": (
  "Frame dragging works because mass-energy currents, like electric currents, "
  "generate their field's magnetic-like component — 'gravitomagnetism.' The "
  "rotating Earth's angular momentum J appears in the off-diagonal terms of the "
  "spacetime metric, and test gyroscopes precess around the rotation axis. The "
  "nodal Lense-Thirring rate for a satellite is 2GJ/(c²a³); the gyroscope "
  "drift measured by Gravity Probe B is the related spin precession. The same "
  "mathematics in the strong field gives the Kerr metric's ergosphere, where "
  "the dragging is total: the time-translation symmetry itself rotates, so "
  "remaining stationary is impossible. Astrophysicists invoke frame dragging to "
  "explain the powerful jets from active galactic nuclei — magnetic fields "
  "anchored in the dragged spacetime fling plasma outward along the spin axis."),
 "key_points": [
  "Rotating masses drag spacetime: Lense-Thirring effect, derived 1918.",
  "Gravity Probe B measured 37.2 +/- 7.2 mas/yr vs 39.2 predicted; geodetic 6,602 vs 6,606.",
  "Gravitomagnetism: mass currents generate the magnetic-like part of gravity.",
  "Inside a Kerr black hole's ergosphere, co-rotation is compulsory.",
  "Implicated in powering relativistic jets from active galaxies."],
 "requirements": [
  "The 'Einstein Field Equations' and 'Black Holes' records.",
  "Angular momentum concept."],
 "standards": ["SI units throughout", "G = 6.67430e-11 m^3 kg^-1 s^-2"],
 "citations": [CIT_E1916,
  "Lense, J., & Thirring, H. (1918). 'On the Influence of the Proper Rotation of Central Bodies on the Motions of Planets and Moons.' Physikalische Zeitschrift, 19, 156-163.",
  "Everitt, C. W. F., et al. (Gravity Probe B) (2011). 'Gravity Probe B: Final Results.' Physical Review Letters, 106, 221101.",
  CIT_STD],
 "demo_kind": "framedrag",
 "sig_lens": (
  "The Signature precision moral from Gravity Probe B: the 'unmeasurable' was "
  "measured. Signature instrument specs therefore never dismiss a small signal "
  "as undetectable in principle — they quote the noise floor and the integration "
  "time, and let the budget decide."),
},
{
 "key": "gravitational-lensing", "name": "Gravitational Lensing",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Gravitational lensing is the bending of light by gravity acting as a lens: "
  "a massive foreground object warps spacetime so that light from a background "
  "source takes multiple curved paths around it, magnifying, distorting, or "
  "multiplying the source's image. Einstein predicted the Sun would deflect "
  "starlight by 1.75 arcseconds at its limb — confirmed by Eddington's 1919 "
  "eclipse expedition, the observation that made Einstein world-famous. Strong "
  "lensing by galaxies creates dramatic Einstein rings, arcs, and quadruple "
  "quasar images; weak lensing subtly shears millions of background galaxies, "
  "letting astronomers map dark matter, which bends light but emits none. "
  "Microlensing — brief brightening when an unseen object crosses a star's line "
  "of sight — has discovered exoplanets down to Earth mass. Lensing is now a "
  "precision tool: time delays between multiple images of one quasar measure "
  "the Hubble constant independently, and lensing magnification lets the James "
  "Webb Space Telescope see the universe's first galaxies."),
 "how_it_works": (
  "Lensing works because light follows null geodesics through curved spacetime. "
  "For a point mass, the deflection angle is alpha = 4GM/(c²b) for impact "
  "parameter b — twice the Newtonian prediction, because general relativity "
  "curves space as well as time, and the 1919 measurement distinguished the "
  "two. The lens equation relates source position, image positions, and the "
  "deflection; when source, lens, and observer align, images merge into an "
  "Einstein ring of angular radius theta_E = sqrt(4GM/c² · D_ls/(D_l·D_s)). "
  "Astronomers invert observed image distortions to weigh the lens — including "
  "its dark matter — since lensing responds to all mass-energy regardless of "
  "luminosity. Time-delay cosmography exploits that different image paths have "
  "different lengths and gravitational time dilation, so quasar flickers arrive "
  "days to months apart."),
 "key_points": [
  "Massive objects bend light: alpha = 4GM/(c^2 b); Sun's limb deflection 1.75 arcseconds.",
  "Eddington's 1919 eclipse test confirmed it and made Einstein famous.",
  "Strong lensing: rings, arcs, multiple quasar images. Weak lensing maps dark matter.",
  "Microlensing finds exoplanets, including Earth-mass worlds.",
  "Time-delay lensing independently measures the Hubble constant."],
 "requirements": [
  "The 'Einstein Field Equations' and 'Geodesics' records.",
  "Basic optics (focal length intuition) helps."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1916,
  "Dyson, F. W., Eddington, A. S., & Davidson, C. (1920). 'A Determination of the Deflection of Light by the Sun's Gravitational Field.' Philosophical Transactions of the Royal Society A, 220, 291-333.",
  CIT_STD],
 "demo_kind": "lensing",
 "sig_lens": (
  "The Signature optics lesson: gravity is a lens you cannot buy. Signature "
  "telescope planning treats massive foreground clusters as instruments — free "
  "apertures provided by spacetime — and schedules deep observations behind "
  "them, because the universe's own optics outperform any glass."),
},
{
 "key": "cosmological-constant", "name": "The Cosmological Constant and Dark Energy",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The cosmological constant, Lambda, is the term Einstein added to his field "
  "equations in 1917 to permit a static universe — then called his 'biggest "
  "blunder' after Hubble found expansion. The joke was on history: in 1998, "
  "two supernova teams found the expansion is accelerating, and the simplest "
  "explanation is a constant vacuum energy density — Lambda, reinstated. It "
  "now dominates the cosmic budget: about 69 percent of the universe's "
  "energy density is dark energy, 26 percent dark matter, 5 percent ordinary "
  "matter. Lambda corresponds to an energy density near 10^-9 joules per cubic "
  "meter — absurdly small by particle-physics standards, yet it rules the "
  "cosmos because there is so much vacuum. Its physical origin is the deepest "
  "unsolved problem in physics: quantum field theory predicts a vacuum energy "
  "10^120 times larger, the worst prediction in science. Whether Lambda is "
  "truly constant or an evolving 'quintessence' field is under active test by "
  "surveys like DESI and Euclid."),
 "how_it_works": (
  "The cosmological constant works as a uniform energy density of empty space "
  "with negative pressure (p = −rho·c²), and in general relativity negative "
  "pressure gravitates repulsively — driving accelerated expansion. In the "
  "Friedmann equations it appears as a term that grows in influence as matter "
  "dilutes: early on matter dominated and expansion decelerated; about 5 "
  "billion years ago Lambda took over and acceleration began. Type Ia "
  "supernovae serve as standard candles revealing the expansion history: "
  "distant supernovae are dimmer than a decelerating universe would allow, "
  "the smoking gun of acceleration (Riess, Perlmutter, Schmidt — Nobel 2011). "
  "The critical density rho_c = 3H0²/(8πG) sets the scale; Lambda's measured "
  "value is about 1.1×10^-52 per square meter. Its constancy is tested by "
  "checking whether the dark-energy equation of state w equals −1 across "
  "cosmic time."),
 "key_points": [
  "Lambda: Einstein's 1917 term, discarded, reinstated by the 1998 acceleration discovery.",
  "Cosmic budget: ~69% dark energy, ~26% dark matter, ~5% ordinary matter.",
  "Acts as vacuum energy with negative pressure, driving accelerated expansion.",
  "Supernova standard candles proved acceleration (Nobel Prize 2011).",
  "Origin unknown; quantum prediction misses by 10^120 — physics' worst prediction."],
 "requirements": [
  "The 'Einstein Field Equations' and 'Expanding Universe' records.",
  "Energy density concept (energy per volume)."],
 "standards": ["SI units throughout", "H0 ~ 70 km/s/Mpc"],
 "citations": [CIT_E1915,
  "Riess, A. G., et al. (1998). 'Observational Evidence from Supernovae for an Accelerating Universe.' The Astronomical Journal, 116, 1009-1038.",
  "Perlmutter, S., et al. (1999). 'Measurements of Omega and Lambda from 42 High-Redshift Supernovae.' The Astrophysical Journal, 517, 565-586.",
  CIT_STD],
 "demo_kind": "lambda",
 "sig_lens": (
  "The Signature humility clause: the dominant component of the universe is "
  "unexplained, and the archive says so plainly. Signature records never dress "
  "ignorance as knowledge — 'origin unknown, under active test' is a complete "
  "and honest entry."),
},
{
 "key": "tests-of-gr", "name": "Tests of General Relativity",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The tests of general relativity are the experiments that have checked "
  "Einstein's theory against nature for over a century — and it has passed "
  "every one. The classical trio: Mercury's perihelion precession (43 "
  "arcseconds per century unexplained by Newton, predicted exactly by GR), the "
  "bending of starlight (1.75 arcseconds at the Sun's limb, confirmed by "
  "Eddington in 1919), and gravitational redshift (Pound-Rebka, 1959). The "
  "modern battery is fiercer: the Shapiro time delay of radar past the Sun "
  "(1964), the Hulse-Taylor binary pulsar spiraling inward exactly as "
  "gravitational-wave emission demands (Nobel 1993), Gravity Probe B's "
  "gyroscope precessions (2011), gravitational lensing maps of dark matter, "
  "and LIGO's waveform-by-waveform match to numerical relativity. Alternative "
  "theories are constrained by the parameterized post-Newtonian framework, in "
  "which GR's parameters match observations to parts per hundred thousand. No "
  "test has falsified general relativity in the regimes probed — though its "
  "incompatibility with quantum mechanics at the Planck scale guarantees new "
  "physics awaits."),
 "how_it_works": (
  "Testing GR works by comparing precise predictions of the field equations "
  "against precision measurements, often parameterized so alternative theories "
  "can be scored on the same scale. The parametrized post-Newtonian (PPN) "
  "formalism assigns numbers like gamma (space curvature per unit mass, GR: 1) "
  "and beta (nonlinearity, GR: 1); the Cassini spacecraft's 2003 Shapiro-delay "
  "measurement pinned gamma to 1 within 2.3×10^-5. Binary pulsars test the "
  "strong field: their orbital decay matches GR's quadrupole formula to "
  "better than a tenth of a percent over decades. LIGO tests the dynamical "
  "strong field: each merger's chirp, merger, and ringdown match supercomputer "
  "solutions of the full nonlinear equations. The theory survives because it "
  "keeps predicting numbers correctly, in weak fields and strong, slow motion "
  "and dynamical — the most thoroughly vindicated theory of gravity ever "
  "devised."),
 "key_points": [
  "Classical tests: Mercury 43'/century, light bending 1.75', gravitational redshift.",
  "Shapiro delay (1964), Hulse-Taylor pulsar decay (Nobel 1993), Gravity Probe B (2011).",
  "PPN framework: GR's parameters match experiment to parts per 100,000.",
  "LIGO waveforms match numerical-relativity predictions template-for-template.",
  "No falsification in any probed regime; quantum gravity remains the open frontier."],
 "requirements": [
  "All preceding advanced records (this is the capstone).",
  "Familiarity with arcseconds as an angular unit."],
 "standards": ["SI units throughout"],
 "citations": [CIT_E1915, CIT_E1916,
  "Will, C. M. (2014). 'The Confrontation between General Relativity and Experiment.' Living Reviews in Relativity, 17, 4.",
  CIT_STD],
 "demo_kind": "deflection",
 "sig_lens": (
  "The Signature verification standard: a theory earns the archive's trust the "
  "way GR did — by surviving a century of hostile, quantitative testing. "
  "Signature engineering applies the same bar to its own models: predict "
  "numbers, publish tolerances, invite the experiment that could kill the "
  "model."),
},
{
 "key": "relativity-gps", "name": "Relativity and GPS: Everyday Proof",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The Global Positioning System is relativity made into everyday "
  "infrastructure: its atomic clocks must be corrected for both special and "
  "general relativity, or navigation fails within hours. GPS satellites orbit "
  "at about 20,200 km altitude moving at 3.9 km/s. Special relativity slows "
  "their clocks by 7.2 microseconds per day relative to the ground; general "
  "relativity — weaker gravity at altitude — speeds them by 45.9 microseconds "
  "per day. The net +38.6 microseconds per day, multiplied by light speed, is "
  "an 11.6-kilometer daily position error if ignored. Engineers handle it by "
  "factory-offsetting each satellite's clock frequency (10.23 MHz tuned to "
  "10.22999999543 MHz) so it ticks correctly in orbit, and receivers apply "
  "further relativistic corrections including Earth's eccentricity effects. "
  "The system also replays history's first macroscopic test daily: the "
  "Hafele-Keating experiment (1971) flew atomic clocks around the world and "
  "measured exactly the predicted east-west asymmetric aging. Every smartphone "
  "fix is a relativity experiment that passes, billions of times per day."),
 "how_it_works": (
  "GPS works by trilateration from timed signals: each satellite broadcasts "
  "its position and the exact transmission time from its atomic clock, and the "
  "receiver solves for its own position and clock error from four or more "
  "satellites' pseudoranges (distance = c × travel time). Because a microsecond "
  "of clock error is 300 meters of position error, the relativistic offsets "
  "are not subtle corrections but mission-critical ones — the satellite clocks "
  "are physically built to run slow on the ground so they run right in orbit. "
  "The receiver software additionally corrects for the Sagnac effect (Earth's "
  "rotation during signal travel) and the eccentricity of each satellite's "
  "orbit, which modulates both the velocity and gravitational terms. The "
  "resulting few-meter accuracy, delivered to billions of devices, is the "
  "largest-scale continuous experimental confirmation of relativity ever "
  "built."),
 "key_points": [
  "GPS satellites: SR -7.2 us/day, GR +45.9 us/day, net +38.6 us/day clock offset.",
  "Uncorrected, positions drift ~11.6 km per day.",
  "Satellite clocks are factory-offset (10.23 MHz -> 10.22999999543 MHz) to tick correctly in orbit.",
  "Hafele-Keating (1971): flown atomic clocks confirmed the predicted asymmetric aging.",
  "Every phone's location fix is a passing relativity experiment, billions of times daily."],
 "requirements": [
  "The 'Time Dilation' and 'Gravitational Time Dilation' records.",
  "Trilateration idea: distances from known points fix your position."],
 "standards": ["SI units throughout", "GPS altitude ~20,200 km", "orbital speed ~3.9 km/s"],
 "citations": [
  "Ashby, N. (2003). 'Relativity in the Global Positioning System.' Living Reviews in Relativity, 6, 1.",
  "Hafele, J. C., & Keating, R. E. (1972). 'Around-the-World Atomic Clocks.' Science, 177, 166-170.",
  CIT_STD],
 "demo_kind": "gps",
 "sig_lens": (
  "The Signature proof standard: a theory graduates from the archive to the "
  "infrastructure when billions of devices bet their navigation on it daily. "
  "Signature systems treat GPS the way physics does — not as an application of "
  "relativity but as its continuous, planet-scale experimental confirmation."),
},
]
