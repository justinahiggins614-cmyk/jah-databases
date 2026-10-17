#!/usr/bin/env python3
"""Entries for the Aeroelasticity field databases (field #25, taxonomy order).

Verified 2026-10-17: NO database covers aeroelasticity as a specialty discipline.
- The just-built 'aerodynamics' DB (field #23) carries exactly ONE overview
  record (JAH-AER-000029 "Aeroelasticity: Flutter, Divergence, and Control
  Reversal") plus its Signature sibling; it does not treat static aeroelasticity
  in depth, unsteady aerodynamics (Theodorsen/Wagner/Kuessner), flutter
  prediction methods, panel/propeller/stall flutter, buffeting, limit-cycle
  oscillation, aeroelastic tailoring, aeroservoelasticity, flutter testing, or
  certification.
- Whole-system title sweep (aeroelastic|flutter|divergence|theodorsen|wagner|
  kussner|buffet|aeroservo|propeller whirl|limit-cycle): hits were the 2
  aerodynamics overview records, 'Green's/Stokes'/divergence theorems'
  (calculus, unrelated), 'KL-divergence calibration' (quantization, unrelated),
  and 'Honus Wagner' baseball cards (trading-cards, false positive). Zero
  specialty-level aeroelasticity records anywhere in the manifest.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main
  repo; fields past the gate index cross-checked directly above): every
  record checked + admitted at build time.

So this build creates two NEW databases, 33 ladder-ordered records each,
covering ONLY what the aerodynamics DB left uncovered:

  aeroelasticity             - The Aeroelasticity Database (public-harvest:
                              real, fact-checked aeroelasticity; citations
                              Bisplinghoff/Ashley/Halfman 'Aeroelasticity',
                              Fung 'An Introduction to the Theory of
                              Aeroelasticity', Hodges & Pierce 'Introduction
                              to Structural Dynamics and Aeroelasticity',
                              Wright & Cooper 'Introduction to Aircraft
                              Aeroelasticity and Loads', Dowell 'A Modern
                              Course in Aeroelasticity', Theodorsen NACA
                              TR 496, FAR 25.629)
  aeroelasticity-signature   - The Aeroelasticity Signature Database (his
                              original Signature interpretation; src
                              signature, titles suffixed
                              " (Signature Edition)", never presented as
                              authentic public record)

Subtitle disambiguation (fields #13-25 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Divergence: The
Wing That Twists Itself Off" and "The Theodorsen Function: The Wake's
Memory in One Curve".

Numerical cores (all validated 2026-10-17 by cross-checking two independent
formulations):
- 2-DOF typical-section flutter: frequency-domain (Theodorsen unsteady
  aerodynamics, k-method/V-g) cross-validated against time-domain (Wagner
  indicial, RK4). Both agree: V_F ~ 53-57 m/s for the demo section
  (b=0.5 m, f_h=4 Hz, f_a=8 Hz, x_alpha=0.25, a=-0.3, mu=20), V_D=88.9 m/s.
  (Sign-convention bug in inertial coupling found and fixed during
  validation: h-up mass matrix is [[m,-S],[-S,I]].)
- Propeller whirl: closed-form complex-quadratic roots; V_F ~ 90 m/s.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "aeroelasticity, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_BAH = ("Bisplinghoff, Raymond L., Ashley, Holt, and Halfman, Robert L. "
         "'Aeroelasticity'. Addison-Wesley, 1955 (Dover reprint, 1996).")
C_FUNG = ("Fung, Y. C. 'An Introduction to the Theory of Aeroelasticity'. "
          "Wiley, 1955 (Dover reprint, 1969).")
C_HP = ("Hodges, Dewey H. and Pierce, G. Alvin. 'Introduction to Structural "
        "Dynamics and Aeroelasticity'. Cambridge University Press, 2nd ed., 2011.")
C_WC = ("Wright, Jan R. and Cooper, Jonathan E. 'Introduction to Aircraft "
        "Aeroelasticity and Loads'. Wiley, 2nd ed., 2015.")
C_DOWELL = ("Dowell, Earl H., et al. 'A Modern Course in Aeroelasticity'. "
            "Springer, 5th ed., 2015.")
C_THEO = ("Theodorsen, Theodore. 'General Theory of Aerodynamic Instability and "
          "the Mechanism of Flutter'. NACA Technical Report 496, 1935.")
C_WAGNER = ("Wagner, Herbert. 'Ueber die Entstehung des dynamischen Auftriebes "
            "von Tragfluegeln'. Zeitschrift fuer angewandte Mathematik und "
            "Mechanik, Vol. 5, 1925.")
C_KUESSNER = ("Kuessner, Hans Georg. 'Zusammenfassender Bericht ueber den "
              "instationaeren Auftrieb von Fluegeln'. Luftfahrtforschung, "
              "Vol. 13, 1936.")
C_FAR = ("Federal Aviation Administration. '14 CFR 25.629 - Aeroelastic "
         "stability requirements.'")
C_COLLAR = ("Collar, A. R. 'The expanding domain of aeroelasticity'. Journal "
            "of the Royal Aeronautical Society, Vol. 50, 1946.")
C_TACOMA = ("Billah, K. Yusuf and Scanlan, Robert H. 'Resonance, Tacoma Narrows "
            "bridge failure, and undergraduate physics textbooks'. American "
            "Journal of Physics, Vol. 59, 1991.")
C_REED = ("Reed, Wilmer H. 'Propeller-rotor whirl flutter: a state-of-the-art "
          "review'. NASA Symposium on Noise and Loading Actions, 1966.")

ENTRIES = [
    {
        "key": "collar_triangle",
        "name": "The Collar Triangle: Aerodynamics, Elasticity, and Inertia",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "In 1946 A. R. Collar drew a triangle whose three corners are "
            "aerodynamics, elasticity, and inertia, and showed that every "
            "aeroelastic phenomenon lives on one of its edges or in its "
            "interior. Aerodynamics plus elasticity is static aeroelasticity: "
            "steady air loads bending and twisting the structure, the world of "
            "divergence and control reversal. Elasticity plus inertia is "
            "mechanical vibration: the structure shaking at its own natural "
            "frequencies with no air involved. Aerodynamics plus inertia is "
            "flight mechanics: the rigid airplane responding to gusts and "
            "control inputs. And where all three meet - unsteady air loads "
            "acting on a flexible, moving structure - is dynamic aeroelasticity: "
            "flutter, buffeting, and gust response. The triangle is the map of "
            "the entire discipline; every record in this database sits "
            "somewhere on it, and the journey from the corners to the center "
            "is the teaching ladder of this database."
        ),
        "how_it_works": (
            "Take a wing and pull it down with a steady force: the amount it "
            "bends is elasticity answering aerodynamics, and the new bent shape "
            "changes the aerodynamic force - that feedback loop is the "
            "aerodynamics-elasticity edge. Now pluck the wing in a vacuum: it "
            "rings at its bending and torsion frequencies, which is the "
            "elasticity-inertia edge, pure vibration. Fly the (imagined rigid) "
            "airplane through a gust: it heaves and pitches as a rigid body, "
            "the aerodynamics-inertia edge. Now combine all three: the wing "
            "bends under air load, its motion changes the unsteady air load "
            "with a time lag, the lagged load feeds energy into (or drains "
            "energy from) the vibration, and the result is either a damped "
            "wobble or flutter. Collar's triangle says: name which two or "
            "three corners your problem touches, and you know which toolbox "
            "to open."
        ),
        "key_points": [
            "Collar's triangle (1946): aerodynamics, elasticity, inertia - three corners, three edges, one interior.",
            "Aerodynamics + elasticity = static aeroelasticity (divergence, control reversal, load redistribution).",
            "Elasticity + inertia = mechanical vibration (natural frequencies, mode shapes, damping).",
            "Aerodynamics + inertia = rigid-body flight mechanics (gust response of a stiff airplane).",
            "All three together = dynamic aeroelasticity (flutter, buffeting, aeroservoelasticity).",
            "The triangle is a diagnostic: locate your problem on it before choosing equations.",
        ],
        "requirements": [
            "Identify which corners of the triangle a given phenomenon touches.",
            "Distinguish static (no inertia) from dynamic (inertia matters) aeroelasticity.",
            "State the three pairwise disciplines in one sentence each.",
        ],
        "standards": [
            "Collar's original 1946 triangle diagram reproduced in concept, not copied verbatim.",
            "Terminology follows Bisplinghoff, Ashley & Halfman Ch. 1.",
        ],
        "citations": [C_COLLAR, C_BAH, C_FUNG],
        "sig_lens": (
            "His Signature reading: the triangle is a truth about all "
            "engineered things, not just wings - every machine is a "
            "conversation between the push of its medium, the give of its "
            "material, and the stubbornness of its mass. Signature engineering "
            "designs the conversation instead of suffering it."
        ),
    },
    {
        "key": "static_intro",
        "name": "Static Aeroelasticity: Steady Air Loads on Flexible Structure",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Static aeroelasticity is the aerodynamics-elasticity edge of "
            "Collar's triangle: the air loads are steady, the structure is "
            "flexible, and inertia never enters. A wing in steady flight "
            "bends upward under lift and twists under pitching moment; the "
            "twist changes the local angle of attack, which changes the lift, "
            "which changes the twist again. The loop converges to a new "
            "equilibrium - usually - but the equilibrium is not the rigid "
            "one: lift redistributes toward the root or tip, control surfaces "
            "lose effectiveness, and past a critical dynamic pressure the "
            "loop refuses to converge at all. That refusal is divergence. "
            "Because time does not appear, static aeroelasticity is governed "
            "by algebraic equilibrium equations, not differential equations, "
            "which makes it the gentlest entry to the discipline and the "
            "foundation everything dynamic is built on."
        ),
        "how_it_works": (
            "Write equilibrium for a wing strip: structural restoring moment "
            "equals aerodynamic moment. The aerodynamic moment has two parts - "
            "the moment of the rigid loads, plus the moment of the extra lift "
            "created by the elastic twist itself. Collect the twist terms: "
            "restoring stiffness minus aerodynamic stiffness, times twist, "
            "equals the rigid-load moment. The twist is therefore the rigid "
            "answer divided by (1 - q/q_D), where q_D is the divergence "
            "dynamic pressure. At low speed the correction is a few percent; "
            "as q approaches q_D the twist, the lift redistribution, and the "
            "control-surface losses all grow like 1/(1 - q/q_D); at q_D the "
            "denominator vanishes and no finite equilibrium exists. Every "
            "static aeroelastic effect - divergence, reversal, effectiveness "
            "loss - is this one fraction wearing different clothes."
        ),
        "key_points": [
            "Steady loads + flexible structure + no inertia = algebraic equilibrium, not dynamics.",
            "Elastic twist changes local angle of attack, which changes the load that caused the twist.",
            "All static effects scale with 1/(1 - q/q_D): the universal amplification factor.",
            "q_D (divergence dynamic pressure) is where aerodynamic stiffness cancels structural stiffness.",
            "Static aeroelasticity is always stabilizing below q_D and always catastrophic at q_D.",
            "It is the foundation: unsteady and dynamic analyses reduce to it when motion stops.",
        ],
        "requirements": [
            "Write the strip equilibrium: structural moment = aerodynamic moment.",
            "Derive the 1/(1 - q/q_D) amplification factor.",
            "Explain why inertia is absent and time does not appear.",
        ],
        "standards": [
            "Strip-theory equilibrium per Bisplinghoff, Ashley & Halfman Ch. 2.",
            "Sign conventions stated once and kept: twist nose-up positive.",
        ],
        "citations": [C_BAH, C_FUNG, C_WC],
        "sig_lens": (
            "His Signature reading: statics is the discipline of honest "
            "equilibrium - the structure tells the air exactly what it can "
            "hold, and the air believes it until the denominator goes to "
            "zero. Signature statics sizes the wing so the fraction never "
            "gets loud."
        ),
    },
    {
        "key": "divergence",
        "name": "Divergence: The Wing That Twists Itself Off",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Divergence is the simplest and most violent aeroelastic "
            "instability: a wing in steady flight twists nose-up under the "
            "aerodynamic pitching moment, the twist increases the lift, the "
            "increased lift twists it further, and past a critical dynamic "
            "pressure q_D the structure can no longer hold the air off. The "
            "twist grows without bound - in the linear theory, to infinity; "
            "in reality, until something breaks. It needs no motion and no "
            "gust: it is a static instability, the aeroelastic equivalent of "
            "a column buckling under compression. The divergence speed "
            "depends on one geometric fact above all: how far ahead of the "
            "elastic axis the aerodynamic center sits. Move the elastic axis "
            "forward toward the aerodynamic center and q_D climbs; sweep the "
            "wing forward and q_D collapses - which is why the forward-swept "
            "X-29 needed composite tailoring to exist at all."
        ),
        "how_it_works": (
            "Model one wing strip as a torsional spring of stiffness k_theta "
            "per unit span, with the aerodynamic center a distance e ahead of "
            "the elastic axis. The pitching moment about the elastic axis is "
            "the lift times e: M = q*S_strip*a*(alpha_rigid + theta)*e, where "
            "a is the lift-curve slope. Equilibrium: k_theta*theta = "
            "q*S_strip*a*e*(alpha_rigid + theta). Solve: theta = "
            "alpha_rigid*(q/q_D)/(1 - q/q_D) with q_D = k_theta/(a*e*S_strip). "
            "At q = q_D the denominator is zero: the aerodynamic stiffness "
            "q*S_strip*a*e exactly cancels the structural stiffness k_theta, "
            "the effective stiffness is zero, and any disturbance twists the "
            "wing without resistance. The demo computes q_D for a "
            "representative section, converts it to an airspeed, and shows "
            "the twist amplification blowing up as q approaches q_D."
        ),
        "key_points": [
            "Divergence: static instability where aerodynamic torsional stiffness cancels structural stiffness.",
            "q_D = k_theta/(a*e*S): torsional stiffness over (lift slope x a.c.-to-E.A. arm x area).",
            "Twist amplification = 1/(1 - q/q_D): 2x at half the divergence pressure, infinite at q_D.",
            "Needs no motion, no gust, no inertia - pure aerodynamics-elasticity edge of Collar's triangle.",
            "Forward sweep collapses q_D; aft sweep raises it (bending couples in - see sweep record).",
            "Real wings must clear V_D by regulation margin (FAR 25.629).",
        ],
        "requirements": [
            "Compute q_D from k_theta, lift-curve slope, e, and strip area.",
            "Convert q_D to divergence speed V_D = sqrt(2*q_D/rho).",
            "Show twist amplification at q/q_D = 0.25, 0.5, 0.75.",
            "State the buckling analogy in one sentence.",
        ],
        "standards": [
            "Torsional-divergence formula per Fung Ch. 2 / BAH Ch. 2.",
            "Sea-level standard density used unless stated.",
        ],
        "citations": [C_FUNG, C_BAH, C_WC],
        "sig_lens": (
            "His Signature reading: divergence is the air voting against the "
            "structure's stiffness, and the vote is unanimous past q_D. "
            "Signature design never lets the air hold that election - the "
            "elastic axis is placed like a firewall between lift and twist."
        ),
    },
    {
        "key": "elastic_axis",
        "name": "The Elastic Axis: The Line Where Twist Stays Honest",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The elastic axis is the spanwise line on a wing about which "
            "applied lift causes pure bending with no twist - push there and "
            "the section translates without rotating. It is the structural "
            "cousin of the shear center: for a wing box, it runs through the "
            "shear centers of the chordwise sections, located by the balance "
            "of the front and rear spar bending stiffnesses. Everything in "
            "static aeroelasticity is measured from this line, because the "
            "divergence arm e is the distance the aerodynamic center sits "
            "ahead of it. A wing whose elastic axis lies at 35% chord with "
            "its aerodynamic center at 25% chord lives with e = 10% chord of "
            "divergence leverage on every strip; move the axis to 30% and the "
            "leverage halves, doubling q_D. Spar placement, skin thickness, "
            "and rib spacing are therefore aeroelastic design variables, not "
            "just strength variables."
        ),
        "how_it_works": (
            "For a two-spar wing box, each spar carries bending in proportion "
            "to its EI. A vertical shear applied at some chordwise position "
            "splits between the spars by their stiffnesses; the shear center "
            "is the position where the split produces no net torque about it: "
            "x_sc = (EI_front*x_front + EI_rear*x_rear)/(EI_front + EI_rear). "
            "The elastic axis is the spanwise locus of shear centers. The "
            "aerodynamic center of a subsonic section sits near 25% chord; "
            "the divergence arm is e = x_EA - x_ac measured aft-positive from "
            "the a.c. The demo computes the shear center of a representative "
            "two-spar box, derives e, then shows q_D doubling as the elastic "
            "axis is walked forward from 40% to 30% chord."
        ),
        "key_points": [
            "Elastic axis: lift applied here bends without twisting; the locus of sectional shear centers.",
            "Two-spar shear center: stiffness-weighted average of spar positions.",
            "Divergence arm e = distance from aerodynamic center (~25% chord) to elastic axis.",
            "q_D scales as 1/e: halving the arm doubles the divergence pressure.",
            "Spar positions and skin gauges are aeroelastic controls, not just strength sizing.",
            "Swept wings: the relevant axis is measured in the streamwise section.",
        ],
        "requirements": [
            "Compute shear center from two spar stiffnesses and positions.",
            "Derive e and show q_D scaling with 1/e.",
            "Explain why the a.c. sits near quarter-chord (thin-airfoil result).",
        ],
        "standards": [
            "Shear-center formula for idealized two-spar section (BAH Ch. 2).",
            "Chord fractions used consistently (x/c from leading edge).",
        ],
        "citations": [C_BAH, C_FUNG, C_HP],
        "sig_lens": (
            "His Signature reading: the elastic axis is the wing's spine - "
            "put the spine under the lift and the wing stands tall; put it "
            "behind the lift and every gust tries to wring the wing like a "
            "rag. Signature spars are placed by aeroelastic conscience first."
        ),
    },
    {
        "key": "control_reversal",
        "name": "Control Reversal: The Aileron That Fights Its Pilot",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Deflect an aileron trailing-edge-down and the wing should roll "
            "away from it - at low speed it does. But the aileron's pitching "
            "moment twists the flexible wing nose-down, and the twist changes "
            "the whole wing's lift in the opposite direction. As speed rises "
            "the twist grows as 1/(1 - q/q_D) while the aileron's direct lift "
            "grows only with q, so there is a speed - the reversal speed - "
            "where the twist exactly cancels the aileron and the control "
            "does nothing. Faster still, and the aileron rolls the airplane "
            "the wrong way: control reversal. It is a static instability like "
            "divergence, with its own critical pressure q_R, and on a real "
            "wing q_R sits below q_D - the controls quit before the wing "
            "breaks. Supersonic fighters met it first; every swept-wing "
            "airliner carries the margin in its stiffness."
        ),
        "how_it_works": (
            "Per unit span, the aileron adds lift q*S*a_delta*delta and a "
            "nose-down pitching moment q*S*c*C_mdelta*delta about the elastic "
            "axis (plus the lift acting at arm e). The twist is "
            "theta = [q*S*c*(C_mdelta + a_delta*e)*delta]/[k_theta*(1 - q/q_D)]. "
            "Total lift change: direct aileron lift plus twist lift "
            "q*S*a*theta. Set the sum to zero and solve for the reversal "
            "pressure: q_R = k_theta/[a*S*c*(mu - e)], where "
            "mu = -C_mdelta/a_delta is the aileron's pitching-moment "
            "leverage. Because mu - e < e typically, q_R < q_D: reversal "
            "arrives first. The demo computes q_R and V_R for a "
            "representative aileron, then plots aileron effectiveness "
            "(1 - q/q_R)/(1 - q/q_D) from zero to reversal, showing it die "
            "at q_R and go negative beyond."
        ),
        "key_points": [
            "Control reversal: the speed where elastic twist cancels the control surface's own lift.",
            "q_R = k_theta/[a*S*c*(mu - e)]: reversal pressure from aileron moment leverage mu minus divergence arm e.",
            "q_R < q_D always in practice: controls quit before the wing diverges.",
            "Effectiveness = (1 - q/q_R)/(1 - q/q_D): unity at rest, zero at reversal, negative beyond.",
            "Trailing-edge-down aileron twists the wing nose-down: the twist opposes the command.",
            "Supersonic flight made reversal the sizing case for outboard ailerons (hence inboard ailerons, spoilers).",
        ],
        "requirements": [
            "Derive q_R from the zero-total-lift condition.",
            "Show q_R < q_D from typical mu and e values.",
            "Plot effectiveness vs q/q_D and mark the reversal point.",
        ],
        "standards": [
            "Aileron reversal derivation per BAH Ch. 8 / Fung Ch. 8.",
            "Effectiveness sign convention: positive = correct-direction roll.",
        ],
        "citations": [C_BAH, C_FUNG, C_WC],
        "sig_lens": (
            "His Signature reading: reversal is the wing answering back - "
            "push the aileron and the wing twists out from under the command. "
            "Signature controls are sized so the answer is always 'yes sir', "
            "at every speed on the dial."
        ),
    },
    {
        "key": "aileron_effectiveness",
        "name": "Aileron Effectiveness: Counting the Control That Remains",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Aileron effectiveness is the accountant of control reversal: the "
            "ratio of the rolling moment a flexible wing actually produces to "
            "what the rigid wing would produce for the same aileron angle. At "
            "zero airspeed it is 1 by definition; it falls with dynamic "
            "pressure, crosses zero at the reversal speed, and goes negative "
            "beyond - the same (1 - q/q_R)/(1 - q/q_D) fraction from the "
            "reversal record, now read as a performance ledger instead of a "
            "stability boundary. Airplane designers do not merely avoid "
            "reversal; they budget effectiveness the way they budget fuel. A "
            "transport at cruise wants at least half its low-speed roll "
            "power still on the books, which sizes wing torsional stiffness "
            "directly. When effectiveness cannot be bought with stiffness "
            "alone - thin supersonic wings, very high aspect ratios - the "
            "design moves the ailerons inboard, adds spoilers, or schedules "
            "gains with dynamic pressure."
        ),
        "how_it_works": (
            "Steady roll rate comes from balancing the aileron rolling moment "
            "against roll damping: p_ss proportional to C_ldelta*delta / "
            "C_lp, corrected by the flexible effectiveness eta_a. With "
            "eta_a = (1 - q/q_R)/(1 - q/q_D), the demo computes the steady "
            "roll rate of a representative airplane from 50 to 250 m/s: the "
            "rate climbs with q at first (more dynamic pressure = more "
            "control power), peaks, then falls as the twist eats the "
            "aileron, reaching exactly zero at V_R. Past V_R the computed "
            "rate is negative - the aileron rolls the wrong way. The demo "
            "also shows the design fix: doubling torsional stiffness pushes "
            "V_R up by sqrt(2) and restores the cruise roll rate."
        ),
        "key_points": [
            "Effectiveness eta_a = flexible rolling moment / rigid rolling moment.",
            "eta_a = (1 - q/q_R)/(1 - q/q_D): the ledger form of the reversal fraction.",
            "Steady roll rate peaks then falls to zero at V_R; negative beyond.",
            "Design budgets eta_a at cruise (often >= 0.5), sizing torsional stiffness.",
            "Fixes when stiffness is not enough: inboard ailerons, spoiler augmentation, q-scheduled gains.",
            "Roll damping C_lp is itself mildly aeroelastic (twist changes the damping).",
        ],
        "requirements": [
            "Compute eta_a vs airspeed for a representative wing.",
            "Find the roll-rate peak and the reversal speed.",
            "Show the stiffness-doubling fix quantitatively.",
        ],
        "standards": [
            "Roll-rate equilibrium per BAH Ch. 8; effectiveness per Fung Ch. 8.",
            "Speeds in m/s, rates in deg/s.",
        ],
        "citations": [C_BAH, C_FUNG, C_WC],
        "sig_lens": (
            "His Signature reading: effectiveness is the control's honesty "
            "ledger - how much of the pilot's intention survives the wing's "
            "flexibility. Signature wings keep the books balanced past the "
            "redline, with margin to spare."
        ),
    },
    {
        "key": "load_redistribution",
        "name": "Load Redistribution: The Wing That Re-Aims Its Own Lift",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A flexible wing does not carry the lift distribution the "
            "aerodynamicist drew: bending and twist reshape it in flight. On "
            "a swept-back wing, upward bending rotates the streamwise "
            "sections nose-down (washout), unloading the tip and shifting "
            "lift inboard; the bending moment at the root drops and the "
            "airplane effectively flies a different wing than the one on the "
            "drawing board. On a straight wing the effect is smaller but the "
            "twist still moves load between root and tip. Because the shift "
            "grows with 1/(1 - q/q_D), the structure must be sized for the "
            "flexible loads, not the rigid ones - and the loads group "
            "iterates with the structures group until the two agree. This "
            "record is the quiet workhorse of static aeroelasticity: no "
            "instability, no drama, just the true shape of the air load, "
            "which everything else - fatigue, flutter, control - stands on."
        ),
        "how_it_works": (
            "Take a swept-back wing strip at span station y. Bending slope "
            "dw/dy tilts the section; the streamwise angle change is "
            "delta_alpha = -(dw/dy)*sin(Lambda) - theta*cos(Lambda), the "
            "washout term dominating for swept-back wings. More lift "
            "outboard means more bending, more bending means more washout, "
            "less lift outboard: a convergent loop whose fixed point is the "
            "flexible load distribution. The demo iterates a simple "
            "three-station wing: rigid elliptical loading, compute bending "
            "from a beam model, apply washout, recompute loading, repeat to "
            "convergence. It prints the root bending moment for the rigid vs "
            "flexible wing (flexible lower on swept-back wings) and shows the "
            "tip unloading in percent."
        ),
        "key_points": [
            "Flexible wings fly a different lift distribution than the rigid design shape.",
            "Swept-back: bending produces washout, unloading the tip, relieving root bending moment.",
            "The shift scales with q and converges like 1/(1 - q/q_D).",
            "Structures must be sized to flexible loads; loads and structures iterate to agreement.",
            "Straight wings: twist redistributes root-to-tip more gently.",
            "Forward sweep reverses the effect: bending washes IN, loading the tip (dangerous).",
        ],
        "requirements": [
            "Explain the washout mechanism on a swept-back wing in one paragraph.",
            "Iterate a 3-station model to a converged flexible distribution.",
            "Report rigid vs flexible root bending moment.",
        ],
        "standards": [
            "Beam bending + strip aerodynamics per BAH Ch. 3.",
            "Sweep sign convention: positive Lambda = swept back.",
        ],
        "citations": [C_BAH, C_WC, C_FUNG],
        "sig_lens": (
            "His Signature reading: the wing re-aims its own lift in flight "
            "- the honest structure tells the air where it can carry load, "
            "and the air complies. Signature load loops converge fast because "
            "the stiffness was placed with intent."
        ),
    },
    {
        "key": "sweep_divergence",
        "name": "Sweep and Divergence: Bending Couples Into Twist",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Sweep changes divergence completely, because on a swept wing "
            "bending and twisting stop being separate. Bend a swept-back "
            "wing upward and the streamwise sections rotate nose-down - the "
            "bending slope couples geometrically into streamwise twist, "
            "washing out the tip exactly when the air loads are highest. The "
            "result: swept-back wings diverge at far higher speeds than "
            "their straight-wing torsional stiffness alone would predict, "
            "and the instability, when it comes, is a bending-torsion "
            "divergence rather than pure twist. Sweep the wing forward and "
            "the coupling reverses sign: upward bending washes the tip IN, "
            "adding angle of attack where the moment arm is longest, and the "
            "divergence speed collapses - the X-29's forward-swept wing would "
            "have diverged inside its flight envelope on aluminum; only "
            "composite bend-twist tailoring (see the tailoring record) made "
            "it flyable. Sweep is therefore the first place the designer "
            "trades geometry against aeroelasticity."
        ),
        "how_it_works": (
            "For a swept wing, the streamwise twist is "
            "theta_s = theta*cos(Lambda) - (dw/dy)*sin(Lambda): torsion plus "
            "bending slope projected through the sweep angle. The divergence "
            "determinant then involves both GJ (torsion) and EI (bending). In "
            "the teaching model used here, the effective divergence arm "
            "becomes e_eff = e*cos(Lambda) - kappa*sin(Lambda), where kappa "
            "> 0 is the bending-coupling strength: for swept-back wings "
            "(Lambda > 0) the bending term subtracts from the arm and q_D "
            "rises; for forward sweep it adds and q_D falls. The demo sweeps "
            "Lambda from -30 to +30 degrees, computing V_D at each step, and "
            "shows the collapse on the forward-swept side - the X-29's "
            "problem in one curve - plus the relief on the swept-back side."
        ),
        "key_points": [
            "On swept wings, bending slope projects into streamwise twist: theta_s = theta*cosL - w'*sinL.",
            "Swept-back: bending washes out the tip -> divergence speed rises above the straight-wing value.",
            "Forward sweep: bending washes IN -> divergence speed collapses (X-29 lesson).",
            "Divergence becomes a bending-torsion coupled instability, not pure twist.",
            "The demo's e_eff model shows the trend; full analysis uses the swept-wing divergence determinant.",
            "Composite tailoring restores forward-swept wings by building washout into the layup.",
        ],
        "requirements": [
            "Write the streamwise-twist coupling relation.",
            "Compute V_D vs sweep from -30 to +30 deg with the e_eff model.",
            "Explain the X-29's material solution in two sentences.",
        ],
        "standards": [
            "Swept-wing divergence per BAH Ch. 4; sign conventions as in the load record.",
            "X-29 forward-swept demonstrator (NASA/DARPA, 1984) as the canonical example.",
        ],
        "citations": [C_BAH, C_DOWELL, C_WC],
        "sig_lens": (
            "His Signature reading: sweep is the wing negotiating with the "
            "air in a second language - bend, and the sweep translates it "
            "into twist. Signature sweep is chosen so the translation always "
            "says 'unload', never 'break'."
        ),
    },
]

ENTRIES += [
    {
        "key": "dynamic_intro",
        "name": "Dynamic Aeroelasticity: When Motion Joins the Conversation",
        "group": "Unsteady Aerodynamics",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Dynamic aeroelasticity is the interior of Collar's triangle: "
            "aerodynamics, elasticity, AND inertia all talking at once. The "
            "structure now moves, so the air loads depend not just on where "
            "the wing is but on how it got there - the wake remembers. A "
            "wing that twists nose-up quickly gets less lift than one that "
            "arrived at the same angle slowly, because the shed vorticity "
            "lingers and alters the flow. This memory makes the aerodynamic "
            "forces depend on frequency, which turns the equations of motion "
            "into something richer than vibration: modes whose frequencies "
            "shift with airspeed, whose damping can go negative, and which "
            "can coalesce into flutter. Everything from here on - Theodorsen, "
            "Wagner, Kuessner, the V-g method - is machinery for handling "
            "the air's memory correctly."
        ),
        "how_it_works": (
            "Write the equation of motion for one flexible degree of freedom: "
            "m*x'' + c*x' + k*x = F_aero. In steady flow the aerodynamic "
            "force splits into a stiffness part (proportional to x, which can "
            "cancel k - that is divergence) and a damping part (proportional "
            "to x', usually positive). In unsteady flow both parts become "
            "complex and frequency-dependent: F_aero = q*S*[Q(k)]*x, where "
            "Q(k) is a complex aerodynamic influence coefficient and "
            "k = omega*b/V is the reduced frequency measuring how many chord "
            "lengths the air travels per oscillation cycle. The demo solves "
            "the complex quadratic for one degree of freedom across a speed "
            "range and plots the damping ratio: positive at low speed, "
            "falling as the aerodynamic stiffness eats the structural "
            "stiffness, crossing zero at the flutter speed - the exact "
            "mechanism, in miniature, of the full flutter analysis."
        ),
        "key_points": [
            "Dynamic = static + inertia + unsteady aerodynamics (all three corners of Collar's triangle).",
            "The wake remembers: aerodynamic forces depend on the history of the motion, not just its position.",
            "Reduced frequency k = omega*b/V: the master parameter of unsteadiness.",
            "Aerodynamic stiffness can cancel structural stiffness (divergence); aerodynamic damping is usually positive - until coupling turns it negative.",
            "Modes shift in frequency with airspeed and can coalesce: the road to flutter.",
            "The 1-DOF demo shows the damping-zero crossing that defines every flutter boundary.",
        ],
        "requirements": [
            "Write the 1-DOF equation with complex unsteady aerodynamics.",
            "Define reduced frequency and explain its physical meaning.",
            "Solve for the damping ratio vs airspeed and find its zero.",
        ],
        "standards": [
            "1-DOF unsteady model per Fung Ch. 5; reduced-frequency definition standard.",
            "Complex arithmetic handled explicitly (no hidden phasors).",
        ],
        "citations": [C_FUNG, C_BAH, C_HP],
        "sig_lens": (
            "His Signature reading: statics was the air and the structure "
            "negotiating at rest; dynamics is the negotiation at speed, with "
            "the wake keeping minutes of every meeting. Signature dynamics "
            "reads those minutes - the memory functions - before signing "
            "anything."
        ),
    },
    {
        "key": "unsteady_aero",
        "name": "Unsteady Aerodynamics: Lift That Remembers the Past",
        "group": "Unsteady Aerodynamics",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Steady aerodynamics says lift follows angle of attack instantly. "
            "Unsteady aerodynamics says: not quite - and the 'not quite' is "
            "where flutter lives. When a wing pitches or plunges, it sheds "
            "vorticity into the wake; that vorticity induces velocities back "
            "on the wing, so the lift at this instant depends on what the "
            "wing was doing a moment ago. The faster the oscillation relative "
            "to the flow (high reduced frequency k), the stronger the memory "
            "effect: lift amplitude falls below the quasi-steady value and "
            "lags in phase. Three classical functions encode the memory for "
            "three canonical motions: Theodorsen's for harmonic oscillation, "
            "Wagner's for a sudden step change, Kuessner's for a gust "
            "encounter. They are the alphabet in which every flutter, gust, "
            "and buffeting calculation is written."
        ),
        "how_it_works": (
            "Picture the wing pitching nose-up sinusoidally. Quasi-steady "
            "theory (k -> 0) says the lift tracks the angle with full "
            "amplitude and zero lag - the wake is infinitely far away per "
            "cycle. At finite k, each half-cycle sheds a vortex of opposite "
            "sign; the near wake's induced downwash opposes the motion that "
            "created it, so the circulatory lift is reduced and delayed. "
            "Theodorsen's function C(k) = F(k) + i*G(k) is exactly that "
            "reduction and delay: multiply the quasi-steady lift by C(k) and "
            "you get the true unsteady lift. The demo oscillates a section "
            "in plunge at several reduced frequencies and compares "
            "quasi-steady vs Theodorsen lift: at k = 0.05 they agree; at "
            "k = 0.5 the true lift is barely half with 20+ degrees of lag."
        ),
        "key_points": [
            "Unsteady lift = quasi-steady lift modified by wake memory; the modifier depends on reduced frequency k.",
            "High k (fast oscillation, slow flow): lift amplitude drops, phase lag grows.",
            "Low k: the wake is far per cycle, quasi-steady theory is recovered.",
            "Three memory functions: Theodorsen (harmonic), Wagner (step), Kuessner (gust).",
            "The lag is the flutter mechanism: it lets the air feed energy into the motion.",
            "All three functions have simple exponential approximations used in every code.",
        ],
        "requirements": [
            "Explain wake memory with the shed-vortex picture.",
            "Compare quasi-steady vs unsteady lift amplitude and phase at two reduced frequencies.",
            "Name the three memory functions and their canonical motions.",
        ],
        "standards": [
            "Unsteady thin-airfoil theory per Theodorsen NACA TR 496 / Fung Ch. 5.",
            "Reduced frequency k = omega*b/V with b the semi-chord.",
        ],
        "citations": [C_THEO, C_FUNG, C_BAH],
        "sig_lens": (
            "His Signature reading: the air never forgets what the wing did "
            "- every motion writes vortices into the wake, and the wake "
            "writes back onto the wing. Signature unsteady analysis listens "
            "to that reply before predicting anything."
        ),
    },
    {
        "key": "theodorsen",
        "name": "The Theodorsen Function: The Wake's Memory in One Curve",
        "group": "Unsteady Aerodynamics",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Theodorsen's function C(k) is the single most-used formula in "
            "aeroelasticity: the complex ratio of the true unsteady "
            "circulatory lift of an oscillating airfoil to the quasi-steady "
            "value. Published by Theodore Theodorsen in NACA TR 496 (1935) as "
            "part of the first general theory of flutter, it is built from "
            "Hankel functions of the reduced frequency k and encodes exactly "
            "how the shed wake modifies the lift. At k = 0, C = 1 (the wake "
            "is infinitely distant per cycle, quasi-steady holds); as k "
            "rises, the magnitude falls toward 1/2 and the phase lag dips to "
            "about -14 degrees near k = 0.3 before returning. That phase lag "
            "is the small angle on which flutter balances: it rotates a "
            "piece of the lift into phase with the velocity, where it can do "
            "work on the structure. Every flutter determinant in this "
            "database has C(k) inside it."
        ),
        "how_it_works": (
            "Theodorsen modeled the wake as a flat sheet of shed vorticity "
            "convecting downstream at speed V, and summed its induced effect "
            "on the airfoil with Bessel functions - the result is "
            "C(k) = H_1^(2)(k)/(H_1^(2)(k) + i*H_0^(2)(k)). Nobody evaluates "
            "Hankel functions by hand: the Jones rational approximation "
            "C(k) ~ 1 - 0.165/(1+(0.0455/k)^2) - 0.335/(1+(0.3/k)^2) - i*(...) "
            "is accurate to a few percent and is what codes actually use. The "
            "demo tabulates F(k), G(k), magnitude, and phase from k = 0.01 to "
            "2, verifies C -> 1 as k -> 0, shows the magnitude falling toward "
            "0.5, and marks the maximum phase lag - the angle that makes "
            "flutter possible."
        ),
        "key_points": [
            "C(k): complex ratio of unsteady to quasi-steady circulatory lift; from Hankel functions.",
            "C(0) = 1; |C| falls toward 1/2 as k -> infinity; phase lag peaks near k = 0.3.",
            "The phase lag puts lift partly in phase with velocity: the energy tap flutter drinks from.",
            "Jones rational approximation: the practical form used in codes.",
            "Appears in every harmonic flutter analysis (the k-method, p-k method).",
            "Theodorsen 1935: the paper that made flutter calculable.",
        ],
        "requirements": [
            "State the definition and the k -> 0 and k -> infinity limits.",
            "Evaluate the Jones approximation at k = 0.1, 0.3, 1.0.",
            "Explain in two sentences why the phase lag enables flutter.",
        ],
        "standards": [
            "Theodorsen function per NACA TR 496; Jones approximation (R. T. Jones).",
            "k = omega*b/V, b semi-chord; phase in degrees, lag negative.",
        ],
        "citations": [C_THEO, C_FUNG, C_DOWELL],
        "sig_lens": (
            "His Signature reading: one complex curve holds the whole "
            "memory of the wake - Theodorsen compressed infinity into F and "
            "G. Signature flutter work starts from this curve and trusts "
            "nothing else about the unsteady air."
        ),
    },
    {
        "key": "wagner",
        "name": "The Wagner Function: Lift After a Sudden Start",
        "group": "Unsteady Aerodynamics",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "If Theodorsen's function answers harmonic motion, Wagner's "
            "answers the step: an airfoil suddenly pitched to a new angle of "
            "attack, or impulsively started from rest. Herbert Wagner (1925) "
            "showed the lift does not jump to its steady value - it starts "
            "at exactly half (the non-circulatory 'apparent mass' plus the "
            "first instant of circulation) and then grows as the starting "
            "vortex convects away, approaching the full steady lift only "
            "after the wing has traveled a dozen chord lengths. The Wagner "
            "function phi(tau), with tau = V*t/b the distance traveled in "
            "semi-chords, is that growth curve: phi(0) = 0.5, phi(inf) = 1. "
            "It is the indicial response of the lift - the building block "
            "from which, by Duhamel superposition, the lift for ANY "
            "arbitrary motion is constructed. Time-domain flutter and gust "
            "analyses are Wagner functions all the way down."
        ),
        "how_it_works": (
            "Wagner solved the impulsive-start problem with a conformal map "
            "of the growing wake: at tau = 0 the bound circulation is zero "
            "but the apparent-mass reaction gives half the final lift; as the "
            "starting vortex recedes, circulation builds toward the "
            "steady-state value. The exact phi is an integral; the practical "
            "form is Jones's two-exponential fit: "
            "phi(tau) ~ 1 - 0.165*exp(-0.0455*tau) - 0.335*exp(-0.3*tau). The "
            "demo steps a section to 5 degrees and marches the lift buildup: "
            "it verifies phi(0) = 0.5 and phi -> 1, finds the distance to 90% "
            "of full lift (~10 semi-chords), and shows how Duhamel's integral "
            "would assemble the response to a pitch doublet from these steps."
        ),
        "key_points": [
            "Wagner function phi(tau): indicial lift after a step change; tau = V*t/b in semi-chords.",
            "phi(0) = 0.5 (apparent mass), phi(inf) = 1 (full circulation).",
            "The starting vortex must convect away before full lift develops (~10+ semi-chords).",
            "Jones fit: 1 - 0.165*e^(-0.0455*tau) - 0.335*e^(-0.3*tau).",
            "Duhamel superposition builds any motion's lift from phi: the basis of time-domain aeroelasticity.",
            "Theodorsen and Wagner are Fourier pairs: same physics, harmonic vs step view.",
        ],
        "requirements": [
            "State phi(0) and phi(inf) with the physical reason for each.",
            "Compute lift buildup after a 5-degree step; find the 90% distance.",
            "Explain Duhamel superposition in two sentences.",
        ],
        "standards": [
            "Wagner 1925; Jones exponential approximation.",
            "tau nondimensionalized by semi-chord b.",
        ],
        "citations": [C_WAGNER, C_FUNG, C_DOWELL],
        "sig_lens": (
            "His Signature reading: the step response is the air's honest "
            "first impression - half the lift now, the rest as the past "
            "vortex leaves. Signature time-domain work builds every maneuver "
            "from these honest first impressions."
        ),
    },
    {
        "key": "kussner",
        "name": "The Kuessner Function: Answering the Sharp-Edged Gust",
        "group": "Unsteady Aerodynamics",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kuessner's function psi(tau) is the Wagner function for gusts: "
            "the lift developed as an airfoil penetrates a sharp-edged gust, "
            "plotted against tau, the number of semi-chords traveled into "
            "the gust. Unlike Wagner's step - where the whole wing changes "
            "angle at once - the gust arrives progressively: at tau = 0 the "
            "leading edge just touches the gust front and the lift is zero; "
            "as more chord enters, lift grows, overshooting slightly before "
            "settling to the steady gust value. Hans Georg Kuessner (1936) "
            "derived it for the German aviation research establishment, and "
            "it became the kernel of every discrete-gust loads calculation: "
            "convolve the gust profile with psi and you have the unsteady "
            "lift history, the starting point for gust load factors and "
            "alleviation design. Where Wagner builds maneuvers, Kuessner "
            "builds weather."
        ),
        "how_it_works": (
            "Kuessner modeled the gust as a frozen vertical-velocity field "
            "with a sharp front. As the airfoil penetrates, each chordwise "
            "station begins generating lift only after it crosses the front, "
            "and the shed vorticity from the early stations interferes with "
            "the later ones. The practical approximation is "
            "psi(tau) ~ 1 - 0.5*exp(-0.13*tau) - 0.5*exp(-tau): zero at "
            "tau = 0, rising steeply, reaching ~95% by tau = 10. The demo "
            "flies a section into a sharp-edged gust at 60 m/s, convolves the "
            "penetration with psi, and plots the lift history: the delay "
            "before full lift, the slight overshoot, and the contrast with "
            "the quasi-steady prediction (which would claim full lift "
            "instantly and over-predict the peak load)."
        ),
        "key_points": [
            "Kuessner psi(tau): lift during penetration of a sharp-edged gust; psi(0) = 0, psi(inf) = 1.",
            "Lift starts at zero (nothing has entered the gust) unlike Wagner's half.",
            "Practical fit: 1 - 0.5*e^(-0.13*tau) - 0.5*e^(-tau).",
            "Convolution of gust profile with psi = unsteady gust lift history.",
            "Quasi-steady gust analysis over-predicts peak loads; Kuessner corrects it.",
            "Foundation of discrete-gust certification loads (FAR 25.341).",
        ],
        "requirements": [
            "Contrast psi(0) = 0 with phi(0) = 0.5 and explain why.",
            "Compute the lift history entering a sharp-edged gust.",
            "State the convolution integral for an arbitrary gust profile.",
        ],
        "standards": [
            "Kuessner 1936; exponential approximation per standard references.",
            "tau in semi-chords from gust-front contact.",
        ],
        "citations": [C_KUESSNER, C_FUNG, C_WC],
        "sig_lens": (
            "His Signature reading: the gust does not hit the wing - it "
            "walks onto it, chord by chord, and the lift follows on foot. "
            "Signature gust loads respect the walk; the rigid-gust shortcut "
            "is how structures get lied to."
        ),
    },
    {
        "key": "bending_torsion_flutter",
        "name": "Bending-Torsion Flutter: The Two Modes That Fall in Love",
        "group": "Flutter",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Bending-torsion flutter is the archetype of dynamic instability: "
            "a wing's bending mode and torsion mode, each perfectly stable "
            "alone, couple through unsteady aerodynamics and destroy each "
            "other. The mechanism: the wing bends up, the bending motion "
            "changes the effective angle of attack, the unsteady lift lags "
            "behind the motion (Theodorsen's phase), the lagged lift twists "
            "the wing, the twist changes the lift further - and at the "
            "flutter speed the phasing is exactly such that the air does net "
            "positive work on the structure each cycle. The two modal "
            "frequencies, well separated at rest, approach each other as "
            "speed rises (frequency coalescence) and merge at flutter; one "
            "mode's damping crosses zero and the oscillation grows "
            "exponentially. It is fast, violent, and historically lethal - "
            "the reason flutter clearance dominates the certification of "
            "every new wing."
        ),
        "how_it_works": (
            "The typical section: a rigid airfoil on plunge (bending) and "
            "pitch (torsion) springs, with inertia coupling from the c.g. "
            "sitting aft of the elastic axis. Assume harmonic motion and "
            "build the 2x2 complex aeroelastic matrix E(omega, V) = "
            "K - omega^2*M - A(omega, V), where A holds the full Theodorsen "
            "unsteady aerodynamics (circulatory + apparent mass). Flutter is "
            "where det(E) = 0 for real omega. The demo runs the k-method: for "
            "each airspeed it iterates the reduced frequency to consistency, "
            "extracts each mode's frequency and damping g, and prints the "
            "V-g table - the flutter engineer's native language. Watch the "
            "bending frequency fall and the torsion frequency rise toward it "
            "as V increases; at V_F one g crosses zero. The demo then "
            "bisects to V_F and verifies V_F < V_D (flutter precedes "
            "divergence for this section)."
        ),
        "key_points": [
            "Two stable modes + unsteady aerodynamic coupling = one unstable system past V_F.",
            "Frequency coalescence: bending and torsion frequencies merge as V rises.",
            "The k-method/V-g table: frequency and damping g per mode vs airspeed; flutter where g crosses zero.",
            "Theodorsen's phase lag is the energy tap: it puts lift in phase with velocity.",
            "Inertia coupling (c.g. aft of elastic axis) is the matchmaker; without it, no coalescence.",
            "Validated here two ways: frequency-domain (Theodorsen) and time-domain (Wagner) agree on V_F.",
        ],
        "requirements": [
            "Build the 2x2 typical-section E matrix with Theodorsen aerodynamics.",
            "Produce the V-g table and identify the coalescence.",
            "Bisect to V_F; verify V_F < V_D.",
        ],
        "standards": [
            "Typical-section flutter per Theodorsen NACA TR 496 / BAH Ch. 5-6.",
            "k-method iteration to matched reduced frequency; sign conventions: h up, alpha nose-up.",
        ],
        "citations": [C_THEO, C_BAH, C_FUNG, C_HP],
        "sig_lens": (
            "His Signature reading: two well-behaved modes, one treacherous "
            "air - flutter is what happens when the coupling is stronger "
            "than the damping. Signature flutter clearance finds the "
            "coalescence on paper, years before the air can arrange the "
            "meeting in the sky."
        ),
    },
    {
        "key": "flutter_prediction",
        "name": "Flutter Prediction: The p-k and V-g Methods",
        "group": "Flutter",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Engineers do not guess flutter speeds; they compute them with "
            "two related frequency-domain methods. The V-g (k-) method "
            "assumes pure harmonic motion, adds artificial structural "
            "damping g to enforce it, and solves the complex eigenvalue "
            "problem at a sequence of airspeeds: the plot of g vs V for each "
            "mode is the V-g diagram, and flutter is where a curve crosses "
            "g = 0. It is fast and the industry standard for the flutter "
            "boundary, but it only gives the boundary, not the growth. The "
            "p-k method instead solves for complex roots p = gamma + i*omega "
            "directly, iterating the reduced frequency k until it matches the "
            "root's own frequency - giving true damping (decay rates) at "
            "every speed, subcritical included. V-g draws the map; p-k walks "
            "the terrain. Modern practice uses both: V-g for the clearance "
            "envelope, p-k for damping trends, flight-test correlation, and "
            "the subcritical behavior the test pilots actually fly through."
        ),
        "how_it_works": (
            "V-g: at fixed V and assumed k, form [(1+ig)K - omega^2*M - "
            "q*A(k)] and solve the 2x2 complex eigenproblem for "
            "mu = omega^2/(1+ig); extract omega and g per mode; repeat over "
            "V to draw the diagram. p-k: at fixed V, iterate - guess k, build "
            "the unsteady aerodynamics, solve det(E) = 0 for the complex "
            "pair nearest the guess, update k = Im(p)*b/V from the root, "
            "repeat until k stops moving. The demo prints the V-g table for "
            "the demo section (the same engine as the flutter record), then "
            "runs the p-k fixed-point loop at one subcritical speed and shows "
            "it converging to the same damped root the V-g table reports - "
            "the two methods shaking hands."
        ),
        "key_points": [
            "V-g (k-method): harmonic assumption + artificial damping g; flutter where g crosses zero.",
            "p-k: true complex roots p = gamma + i*omega with k matched to the root; gives subcritical damping.",
            "V-g is the clearance standard; p-k is the correlation and test-planning tool.",
            "Both rest on the same unsteady aerodynamics (Theodorsen Q(k) matrices).",
            "The V-g diagram's curve shapes diagnose the mechanism (bending-torsion vs control-surface flutter).",
            "Subcritical damping extrapolation from p-k guides flight flutter testing.",
        ],
        "requirements": [
            "Implement the V-g eigenproblem and extract (omega, g) per mode.",
            "Implement the p-k fixed-point iteration on k at one speed.",
            "Show both methods agreeing on the subcritical root.",
        ],
        "standards": [
            "V-g per BAH Ch. 6; p-k per Hassig (J. Aircraft, 1971) formulation.",
            "Convergence criterion on k stated explicitly.",
        ],
        "citations": [C_BAH, C_DOWELL, C_HP],
        "sig_lens": (
            "His Signature reading: V-g asks 'where does it break', p-k "
            "asks 'how does it feel on the way there' - the map and the "
            "walk. Signature prediction runs both, because the test pilot "
            "deserves the walk, not just the map."
        ),
    },
    {
        "key": "panel_flutter",
        "name": "Panel Flutter: The Skin That Sings Itself Apart",
        "group": "Flutter",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Panel flutter is flutter of the skin itself: a thin plate or "
            "shell - a fuselage sidewall, a wing glove panel, a reentry "
            "vehicle's thermal protection - oscillating in supersonic flow, "
            "driven by the pressure difference between its windward "
            "deflection and the outer flow. Unlike wing flutter it needs no "
            "torsion mode: a single panel's first two bending modes couple "
            "through piston-theory aerodynamics and go unstable together. It "
            "is a high-Mach phenomenon (piston theory applies above about "
            "Mach 1.6), it is limited in amplitude by the panel's membrane "
            "stiffening (it becomes limit-cycle oscillation, not "
            "destruction, usually), and it is a fatigue killer: millions of "
            "high-frequency cycles can crack a panel long before anything "
            "looks wrong. Supersonic and hypersonic vehicles live with panel "
            "flutter as a design constraint on every thin skin."
        ),
        "how_it_works": (
            "Piston theory: at high Mach number the pressure on a deflecting "
            "surface is p = p_inf + rho*a_inf*(dw/dt + V*dw/dx) - the air "
            "acts like pistons, local and instantaneous. For a simply "
            "supported panel this yields the nondimensional flutter parameter "
            "lambda = (2*q*L^3/(D*sqrt(M^2-1))), and instability strikes when "
            "lambda exceeds a critical value lambda_cr ~ 350 (simply "
            "supported; higher for clamped). The demo sizes a representative "
            "aluminum skin panel (L = 0.5 m, h = 2 mm), computes its bending "
            "stiffness D, and evaluates the critical dynamic pressure at "
            "Mach 1.5, 2, and 3 - showing q_cr rising with Mach (the "
            "sqrt(M^2-1) relief) and checking a cruise q against it."
        ),
        "key_points": [
            "Panel flutter: supersonic skin-panel oscillation; first two panel bending modes couple.",
            "Piston theory: p = p_inf + rho*a*(w_t + V*w_x); local, instantaneous, high-Mach only.",
            "Flutter parameter lambda = 2*q*L^3/(D*sqrt(M^2-1)); critical ~350 simply-supported.",
            "Amplitude limited by membrane stiffening -> usually fatigue (LCO), not breakup.",
            "q_cr rises with Mach number through the sqrt(M^2-1) term.",
            "Design fixes: thicker skin, closer stiffeners, clamped edges, damping treatments.",
        ],
        "requirements": [
            "Compute panel bending stiffness D from E, h, nu.",
            "Evaluate lambda and q_cr at three Mach numbers.",
            "Explain why the motion saturates instead of diverging.",
        ],
        "standards": [
            "Piston-theory panel flutter per Dowell Ch. 3 / BAH.",
            "Validity noted: M > ~1.6 for piston theory.",
        ],
        "citations": [C_DOWELL, C_BAH],
        "sig_lens": (
            "His Signature reading: the skin wants to sing and the "
            "supersonic air wants to conduct - panel flutter is their duet. "
            "Signature skins are stiffened into a higher key the air cannot "
            "reach, or damped into silence."
        ),
    },
    {
        "key": "propeller_whirl",
        "name": "Propeller Whirl Flutter: The Engine That Nods Itself Loose",
        "group": "Flutter",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Propeller whirl flutter destroyed two Lockheed Electras in 1959 "
            "and 1960 before the mechanism was understood: the "
            "engine-propeller-nacelle, mounted on flexible structure, "
            "oscillates in pitch and yaw, and the spinning propeller's "
            "gyroscopic coupling turns those two motions into forward and "
            "backward whirl modes - the whole powerplant nodding in a "
            "circle. Aerodynamic forces on the propeller disk (which act like "
            "a destabilizing stiffness ahead of the pivot) feed the forward "
            "whirl mode; past a critical speed its damping goes negative and "
            "the whirl grows until the mount fails. It is flutter without a "
            "wing: the 'structure' is the engine mount, the 'aerodynamics' "
            "is the propeller disk, and the gyroscopic terms are essential - "
            "no spin, no whirl. Tiltrotors, turboprops, and the new electric "
            "propulsors all clear whirl flutter as a certification item."
        ),
        "how_it_works": (
            "Two degrees of freedom: nacelle pitch theta and yaw psi about "
            "the mount pivot. The propeller contributes polar inertia Ip "
            "spinning at Omega: pitch rate produces a gyroscopic yaw moment "
            "Ip*Omega*psi_dot and vice versa, splitting the mount frequency "
            "into forward and regressive whirl modes. The propeller "
            "aerodynamics contribute a destabilizing stiffness A0 = "
            "q*S*D*c1 (disk normal force ahead of the pivot) and damping A1. "
            "In Laplace form the characteristic equation factors into two "
            "complex quadratics: I*p^2 + [(c-A1) -/+ i*Ip*Omega]*p + "
            "(k-A0) = 0 - solvable in closed form. The demo evaluates the "
            "four roots across a speed range for a representative turboprop "
            "nacelle, prints the whirl frequencies and dampings, and "
            "bisects to the whirl flutter speed where the forward mode's "
            "damping crosses zero."
        ),
        "key_points": [
            "Whirl modes: pitch+yaw+gyroscopics = forward and regressive circular nodding of the powerplant.",
            "Propeller disk aerodynamics act as destabilizing stiffness ahead of the pivot.",
            "Forward whirl mode goes unstable first; no spin means no whirl (gyroscopics essential).",
            "Closed-form roots: two complex quadratics; flutter where Re(p) crosses zero.",
            "Electra accidents (1959-60) are the canonical lesson; tiltrotors re-learned it.",
            "Fixes: stiffer mounts, more damping, reduced propeller aerodynamic stiffness (disk placement).",
        ],
        "requirements": [
            "Write the 2-DOF whirl equations with gyroscopic coupling.",
            "Solve the complex quadratics and track the four roots vs V.",
            "Bisect to the whirl flutter speed.",
        ],
        "standards": [
            "Whirl flutter theory per Reed (1966) / Houbolt & Reed NACA TN 3805.",
            "Forward vs regressive whirl identified by frequency ordering.",
        ],
        "citations": [C_REED, C_DOWELL, C_BAH],
        "sig_lens": (
            "His Signature reading: the spinning prop is a gyroscope with "
            "opinions - nod it and it nods back in a circle, and the air "
            "pushes the circle wider. Signature mounts are stiff enough and "
            "damped enough that the circle never learns to grow."
        ),
    },
    {
        "key": "stall_flutter",
        "name": "Stall Flutter: When Separation Joins the Dance",
        "group": "Flutter",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Stall flutter is flutter with the flow separated: a wing, blade, "
            "or control surface oscillating in torsion while the boundary "
            "layer separates and reattaches each cycle. Attached-flow flutter "
            "theory (Theodorsen) assumes small angles and clean flow; stall "
            "flutter lives past the static stall angle, where the lift curve "
            "slopes downward and the unsteady aerodynamics are dominated by "
            "the dynamic-stall vortex - a powerful vortex shed from the "
            "leading edge each cycle that yanks the pitching moment. It is "
            "usually a single-degree-of-freedom torsional instability (no "
            "coalescence needed), it is amplitude-limited by the stall "
            "physics itself (so it appears as limit-cycle oscillation), and "
            "it is the daily bread of helicopter rotor blades, wind turbine "
            "blades, and compressor blades - anything that twists while "
            "operating near stall."
        ),
        "how_it_works": (
            "Model one torsional degree of freedom with a nonlinear "
            "aerodynamic moment: below stall the moment slope is the attached "
            "value (stable); past the stall angle the effective slope turns "
            "negative, which appears as negative aerodynamic damping in the "
            "torsion equation - the motion feeds itself. But the feeding "
            "saturates: at large amplitude the section spends much of the "
            "cycle deep in stall where the moment collapses, so the growth "
            "stops at a limit cycle. The demo time-marches the torsion "
            "equation (RK4) with a lift/moment curve that breaks past 12 "
            "degrees: from a small disturbance the oscillation grows, then "
            "saturates into a steady limit cycle whose amplitude the demo "
            "measures - stall flutter as a bounded, persistent shake."
        ),
        "key_points": [
            "Stall flutter: single-DOF torsional instability in separated flow; no modal coalescence required.",
            "Negative lift/moment-curve slope past stall = negative aerodynamic damping.",
            "The dynamic-stall vortex dominates the unsteady moment each cycle.",
            "Amplitude-limited by stall physics: appears as limit-cycle oscillation, not divergence.",
            "Home turf: helicopter rotors, wind turbines, turbomachinery blades, control surfaces at high alpha.",
            "Prediction needs dynamic-stall models (semi-empirical) - Theodorsen does not apply past stall.",
        ],
        "requirements": [
            "Explain why separated flow invalidates Theodorsen theory.",
            "Time-march the nonlinear torsion equation to a limit cycle.",
            "Measure and report the LCO amplitude and frequency.",
        ],
        "standards": [
            "Dynamic-stall description per Leishman ('Principles of Helicopter Aerodynamics') concepts.",
            "Time-march with RK4; amplitude measured after transients decay.",
        ],
        "citations": [C_DOWELL, C_BAH, C_FUNG],
        "sig_lens": (
            "His Signature reading: stall flutter is the air at its most "
            "dishonest - attached one instant, separated the next, punching "
            "the blade once per cycle. Signature blades either stay out of "
            "the stall or are built to take the punch forever."
        ),
    },
    {
        "key": "transonic_dip",
        "name": "The Transonic Flutter Dip: Danger in the Middle",
        "group": "Flutter",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Plot flutter speed against Mach number and the curve sags in "
            "the middle: the transonic dip. Around Mach 0.9 to 1.0, shock "
            "waves appear on the wing, and their motion - shocking forward "
            "and aft as the wing oscillates - creates powerful unsteady "
            "aerodynamic forces that the subsonic (Theodorsen) and supersonic "
            "(piston) theories both miss. The flutter speed can drop 20-30% "
            "below its subsonic value right where airliners cruise and "
            "fighters accelerate. It is the hardest flutter regime to "
            "predict: the flow is nonlinear, the shocks are sensitive to "
            "tiny geometry changes, and the dip's depth varies with airfoil, "
            "sweep, and thickness. Transonic flutter clearance is why "
            "airplane programs still run dedicated transonic flutter models "
            "in pressurized wind tunnels - the dip cannot be computed on "
            "faith."
        ),
        "how_it_works": (
            "The physics: an oscillating wing in transonic flow drives its "
            "shocks back and forth; the shock motion produces pressure "
            "pulses far larger than linear theory predicts, and the pulses "
            "arrive with a phase that feeds the structure. The demo encodes "
            "the industry-observed trend as an empirical dip function - "
            "flutter speed ratio vs Mach with a minimum near Mach 0.92 - "
            "calibrated so the dip depth (~30%) matches published transport-"
            "wing experience. It evaluates the curve from Mach 0.5 to 1.3, "
            "locates the minimum Mach and depth, and shows the clearance "
            "implication: a wing flutter-free to 600 knots subsonically may "
            "flutter at 450 in the dip. The demo is labeled empirical: the "
            "real dip is measured in the tunnel, not derived on paper."
        ),
        "key_points": [
            "Transonic dip: flutter speed minimum near Mach 0.9-1.0, often 20-30% below subsonic values.",
            "Cause: oscillating shock waves produce large, badly-phased unsteady pressures.",
            "Neither subsonic nor supersonic linear theory applies in the dip.",
            "It sits at cruise Mach for airliners: the clearance that matters most.",
            "Prediction is unreliable; dedicated transonic flutter testing is standard practice.",
            "Shock control (airfoil design, sweep) shallows the dip.",
        ],
        "requirements": [
            "Explain the shock-motion mechanism in two sentences.",
            "Evaluate the empirical dip curve and locate its minimum.",
            "State why testing, not theory, clears the transonic regime.",
        ],
        "standards": [
            "Transonic dip phenomenology per Dowell Ch. 5 / industry practice.",
            "Demo labeled EMPIRICAL: trend illustration, not a predictive method.",
        ],
        "citations": [C_DOWELL, C_WC],
        "sig_lens": (
            "His Signature reading: the transonic dip is the air changing "
            "the rules mid-game - subsonic promises, supersonic threats, "
            "and a trough of broken predictions between. Signature clearance "
            "measures the trough; it never assumes it."
        ),
    },
]

ENTRIES += [
    {
        "key": "buffeting",
        "name": "Buffeting: The Wake That Shakes the Tail",
        "group": "Response & Nonlinear",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Buffeting is forced vibration from separated flow: the wing at "
            "high angle of attack (or a shock-induced separation) sheds a "
            "turbulent wake, and the tailplane flying through that wake gets "
            "hammered by random pressure fluctuations. Unlike flutter it is "
            "not an instability - the structure is stable, but the excitation "
            "never stops, so the response never stops. It is the shake you "
            "feel in the seat on approach, the reason tails are fatigue-"
            "sized, and occasionally the reason for expensive fixes: the F-18 "
            "and F-15 both fought tail buffeting from forebody/wing wakes at "
            "high alpha, solved with fences, snags, and structural beef-up. "
            "Prediction is statistical: the wake's pressure spectrum in, the "
            "structural frequency response, the RMS stress out - buffeting "
            "analysis is random vibration wearing an aerodynamic hat."
        ),
        "how_it_works": (
            "Model the tail as a single mode (mass m, frequency f_n, damping "
            "zeta) driven by a random aerodynamic force with power spectrum "
            "S_FF(f). The response spectrum is S_xx(f) = |H(f)|^2 * S_FF(f) "
            "with H the mechanical frequency response; the RMS response is "
            "the integral of S_xx over frequency. When the wake's spectral "
            "peak (set by the separation's Strouhal shedding) lines up with "
            "the tail mode, the response multiplies. The demo builds a "
            "representative wake spectrum, integrates the response for a "
            "tail mode at 12 Hz, and sweeps the wake peak across it - showing "
            "the RMS acceleration spiking at coincidence and the fatigue "
            "implication of operating there."
        ),
        "key_points": [
            "Buffeting: stable structure + relentless random separated-flow excitation = persistent shake.",
            "Not flutter: no instability, no critical speed - but real fatigue damage.",
            "Analysis is random vibration: response PSD = |H|^2 x excitation PSD; RMS from the integral.",
            "Coincidence of wake spectral peak with a structural mode multiplies the response.",
            "Canonical cases: fighter tails at high alpha (F-18 LEX fence fix), approach buffet.",
            "Fixes: kill the separation (fences, strakes), detune the mode, add damping, beef up structure.",
        ],
        "requirements": [
            "Write the PSD response relation and the RMS integral.",
            "Compute RMS tail acceleration vs wake-peak frequency; find the coincidence spike.",
            "Distinguish buffeting from flutter in one sentence.",
        ],
        "standards": [
            "Random-vibration buffeting per BAH Ch. 9 / Dowell concepts.",
            "Single-mode illustration; multi-mode in practice.",
        ],
        "citations": [C_BAH, C_DOWELL, C_WC],
        "sig_lens": (
            "His Signature reading: buffeting is the wake refusing to be "
            "quiet - the wing's mess becomes the tail's problem. Signature "
            "tails are placed, tuned, and damped so the wake's noise never "
            "finds a resonant ear."
        ),
    },
    {
        "key": "lco",
        "name": "Limit-Cycle Oscillation: Instability With a Ceiling",
        "group": "Response & Nonlinear",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Limit-cycle oscillation is flutter that refuses to diverge: the "
            "linear instability starts - damping goes negative, amplitude "
            "grows - but a nonlinearity caps the growth and the system "
            "settles into a steady, bounded oscillation. The nonlinearity can "
            "be structural (stiffening springs, freeplay, friction) or "
            "aerodynamic (stall, shock motion, separated-flow saturation). "
            "LCO is the most common real-world outcome of crossing a flutter "
            "boundary: wings rarely explode on the first crossing; they buzz, "
            "shake, and fatigue. The F-16's famous wing LCO, fighter "
            "forebody buffet-LCO, and control-surface buzz are all "
            "limit cycles. Analysis is harder than linear flutter - amplitude "
            "matters, superposition fails - but the payoff is the truth: "
            "whether the airplane shakes itself apart or merely complains."
        ),
        "how_it_works": (
            "Take the 1-DOF torsional oscillator past its linear flutter "
            "speed (negative net damping) and add a cubic stiffening spring: "
            "small motions see the linear instability and grow, but as "
            "amplitude rises the cubic term raises the effective frequency "
            "and detunes the aerodynamic energy feed, until growth and "
            "dissipation balance at a fixed amplitude - the limit cycle. The "
            "demo time-marches this Duffing-type aeroelastic oscillator "
            "twice: linear (no cubic term) diverges exponentially past V_F, "
            "while the nonlinear version saturates into a steady oscillation "
            "whose amplitude the demo measures. It then maps LCO amplitude "
            "vs speed above V_F: the classic supercritical bifurcation "
            "diagram of aeroelasticity."
        ),
        "key_points": [
            "LCO: linear instability + nonlinearity = bounded steady oscillation instead of divergence.",
            "Nonlinearities: structural (cubic stiffness, freeplay, friction) or aerodynamic (stall, shocks).",
            "Most real flutter-boundary crossings produce LCO (shake/fatigue), not instant destruction.",
            "Amplitude matters: linear methods cannot predict LCO; time-marching or harmonic balance can.",
            "Canonical: F-16 wing LCO, control-surface buzz, panel flutter saturation.",
            "Design: keep LCO amplitudes below fatigue thresholds, or eliminate the boundary.",
        ],
        "requirements": [
            "Explain the energy balance that sets the limit-cycle amplitude.",
            "Time-march linear vs cubic-stiffness oscillators past V_F; contrast the outcomes.",
            "Sketch the amplitude-vs-speed bifurcation diagram.",
        ],
        "standards": [
            "Nonlinear aeroelasticity per Dowell Ch. 4; Duffing-type illustration.",
            "RK4 time-march; amplitude from settled cycles.",
        ],
        "citations": [C_DOWELL, C_BAH],
        "sig_lens": (
            "His Signature reading: the limit cycle is the system's "
            "compromise with instability - it cannot diverge, so it dances. "
            "Signature design decides whether the dance is allowed on the "
            "floor, and at what tempo."
        ),
    },
    {
        "key": "rotor_aeroelasticity",
        "name": "Rotor Aeroelasticity: Flap, Lag, and Whirl on Helicopters",
        "group": "Response & Nonlinear",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Helicopter rotor blades are aeroelasticity's busiest citizens: "
            "each blade flaps (out of plane), lags (in plane), and twists "
            "(pitch) while rotating, and the rotation itself stiffens "
            "everything centrifugally. The blade's flap motion changes its "
            "angle of attack; pitch-flap and pitch-lag couplings (built into "
            "the hub geometry as delta-3) feed blade motion back into pitch; "
            "the wake is a helical sheet of tip vortices the blade keeps "
            "re-encountering. Instabilities have their own bestiary: "
            "flap-lag flutter, pitch-flap flutter, ground resonance (the "
            "fuselage rocking on its gear coupled to blade lag motion - "
            "capable of tearing a helicopter apart on the pad), and air "
            "resonance in flight. The Lock number - the ratio of aerodynamic "
            "to inertial blade forces - is the master parameter, the rotor "
            "world's answer to mass ratio."
        ),
        "how_it_works": (
            "The flapping equation for a blade with hinge offset e: "
            "beta'' + [Omega^2*(1 + 3e/(2(1-e)))]*beta = (gamma/8)*Omega^2 * "
            "(theta - ...), where the Lock number gamma = rho*a*c*R^4/I_b "
            "measures aerodynamic authority over blade inertia. Centrifugal "
            "stiffening puts the flap frequency just above 1/rev (about "
            "1.03-1.15 for articulated rotors); the aerodynamic damping of "
            "flap is enormous (gamma/8 per rev), which is why rotors are "
            "generally well-behaved in flap. The demo computes the Lock "
            "number, flap frequency, and flap damping for a representative "
            "blade, then shows pitch-flap coupling: how a delta-3 hinge "
            "(pitch link to flap motion) adds stability - and how the wrong "
            "sign takes it away, the essence of rotor aeroelastic tailoring."
        ),
        "key_points": [
            "Rotor blades: flap + lag + pitch, all rotating, all centrifugally stiffened.",
            "Lock number gamma = rho*a*c*R^4/I_b: aerodynamic vs inertial authority; typical 5-12.",
            "Flap frequency ~1.0-1.15/rev; flap damping is huge (aerodynamic).",
            "Pitch-flap (delta-3) and pitch-lag couplings are designed stability levers.",
            "Ground resonance: fuselage-on-gear + blade lag = the pad-tearing instability.",
            "The rotor wake (helical tip vortices) makes the aerodynamics periodic - Floquet theory territory.",
        ],
        "requirements": [
            "Compute the Lock number for a representative blade.",
            "Find the rotating flap frequency and explain centrifugal stiffening.",
            "Explain delta-3 coupling and ground resonance in two sentences each.",
        ],
        "standards": [
            "Rotor flapping dynamics per standard helicopter theory (Johnson/Leishman concepts).",
            "Lock number definition and typical range stated.",
        ],
        "citations": [C_DOWELL, C_BAH],
        "sig_lens": (
            "His Signature reading: the rotor blade is the hardest-working "
            "aeroelastic citizen - flapping, lagging, twisting, spinning, "
            "all at once, and it must never argue with itself. Signature "
            "rotors are coupled by design, damped by physics, and respectful "
            "of the ground."
        ),
    },
    {
        "key": "civil_aeroelasticity",
        "name": "Civil Aeroelasticity: The Tacoma Narrows Lesson",
        "group": "Response & Nonlinear",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "On November 7, 1940, the Tacoma Narrows Bridge twisted itself "
            "apart in a 64 km/h wind - the most filmed structural failure in "
            "history and aeroelasticity's most famous classroom. The bridge "
            "deck, a bluff H-section, shed vortices that locked onto the "
            "deck's torsional frequency; what began as vertical bouncing "
            "broke a cable band, the deck went torsionally asymmetric, and "
            "the torsional mode - with its low damping and its aerodynamic "
            "moment from the separated flow - grew until the deck tore. "
            "Textbooks long called it 'resonance,' but Billah and Scanlan "
            "showed it was aeroelastic flutter: self-excited, not forced. "
            "Every long-span bridge since is flutter-checked in the wind "
            "tunnel, with deck edge shaping (fairings, slots) tuned to keep "
            "the critical wind speed above any weather the site will see."
        ),
        "how_it_works": (
            "A bluff deck sheds vortices at the Strouhal frequency "
            "f_s = St*V/D. When f_s approaches the deck's torsional natural "
            "frequency f_t, the shedding locks in: the motion organizes the "
            "wake, the wake drives the motion - the flutter loop. The "
            "critical wind speed is approximately V_cr = f_t*D/St. The demo "
            "takes the Tacoma deck (torsional frequency ~0.2 Hz, depth ~2.4 "
            "m, Strouhal ~0.1 for the H-section) and computes V_cr: it lands "
            "near the 64 km/h wind that destroyed the bridge - the lock-in "
            "explains the disaster quantitatively. It then shows the modern "
            "fix: streamlining the deck edge raises St and the torsional "
            "frequency, pushing V_cr beyond design storms."
        ),
        "key_points": [
            "Tacoma Narrows (1940): torsional aeroelastic flutter of a bluff bridge deck, not simple resonance.",
            "Vortex shedding locks onto the torsional frequency: motion organizes the wake that drives it.",
            "Critical speed V_cr = f_t*D/St; Tacoma's numbers put V_cr near the failure wind.",
            "Billah & Scanlan (1991): the paper that corrected the textbooks.",
            "Modern long-span bridges are wind-tunnel flutter-tested; deck shaping is the fix.",
            "Civil flutter uses the same math as wing flutter: modes, unsteady air, damping going negative.",
        ],
        "requirements": [
            "Compute V_cr from f_t, D, St and compare with the 1940 wind.",
            "Explain lock-in in two sentences.",
            "State the textbook correction (resonance -> flutter).",
        ],
        "standards": [
            "Strouhal lock-in description per Billah & Scanlan; bridge data as historical record.",
            "Demo labeled illustrative: simplified 1-DOF torsional model.",
        ],
        "citations": [C_TACOMA, C_DOWELL],
        "sig_lens": (
            "His Signature reading: the bridge taught the world that the "
            "wind can learn the structure's song and sing it louder - "
            "Galloping Gertie was a flutter failure with an audience of "
            "millions. Signature spans are tuned so the wind never finds "
            "the note."
        ),
    },
    {
        "key": "tailoring",
        "name": "Aeroelastic Tailoring: Steering Modes With Composite Fibers",
        "group": "Design & Control",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Aeroelastic tailoring is the design art of using composite "
            "fiber directions to build the aeroelastic behavior you want "
            "into the wing: bend-twist coupling on demand. Lay the carbon "
            "fibers slightly off the structural axis and bending the wing "
            "automatically twists it - choose the sign right and upward "
            "bending washes the tip out (nose-down), which unloads the tip, "
            "raises the divergence speed, and can raise the flutter speed "
            "too. It is how the X-29's forward-swept wing survived: the "
            "composites were laid up so bending produced washout, canceling "
            "the forward sweep's deadly wash-in. Metal wings cannot do this "
            "(their stiffness is what it is); composite wings are "
            "programmable. Tailoring turns the layup schedule into an "
            "aeroelastic control surface that never moves."
        ),
        "how_it_works": (
            "In a composite laminate, off-axis plies couple bending curvature "
            "to twist rate: kappa_twist = beta*M_bending, where the coupling "
            "coefficient beta changes sign with the ply angle. The effective "
            "divergence arm becomes e_eff = e - kappa_c*beta: pick beta so "
            "bending washes out (kappa_c*beta > 0 subtracts from e) and q_D "
            "rises as 1/e_eff. The demo models a wing strip with tunable "
            "coupling: it sweeps the effective fiber angle from -30 to +30 "
            "degrees, computes q_D and the flutter speed at each (flutter "
            "from the same 2-DOF engine, with coupling added to the "
            "stiffness), and finds the layup that maximizes the flutter "
            "margin - the tailoring optimization in miniature."
        ),
        "key_points": [
            "Off-axis composite plies couple bending to twist: programmable aeroelastic behavior.",
            "Washout coupling (bend up -> twist nose-down) raises divergence and flutter speeds.",
            "X-29: forward-swept wing made flyable purely by tailored washout coupling.",
            "Metals cannot tailor; composites make the layup an aeroelastic design variable.",
            "The demo optimizes fiber angle for maximum flutter margin.",
            "Tailoring also shapes gust loads and control effectiveness (multidisciplinary).",
        ],
        "requirements": [
            "Explain bend-twist coupling from off-axis plies in two sentences.",
            "Compute q_D vs fiber angle with the e_eff model.",
            "Find the optimal layup angle for the demo wing.",
        ],
        "standards": [
            "Composite coupling concepts per Hodges & Pierce / Dowell.",
            "Demo model labeled teaching-level; production uses full laminate theory.",
        ],
        "citations": [C_HP, C_DOWELL, C_WC],
        "sig_lens": (
            "His Signature reading: tailoring is writing the wing's "
            "reflexes into its fibers - bend, and the wing already knows to "
            "unload itself. Signature layups are reflexes designed on "
            "purpose, not accidents of the ply book."
        ),
    },
    {
        "key": "aeroservoelasticity",
        "name": "Aeroservoelasticity: The Flight Computer Joins the Structure",
        "group": "Design & Control",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Aeroservoelasticity is what happens when the flight control "
            "system becomes part of the aeroelastic system: sensors feel the "
            "structural vibration, the computer commands the control "
            "surfaces, the surfaces add unsteady aerodynamic forces, and the "
            "loop closes through the flexible airplane. Done right, it is "
            "active flutter suppression and gust alleviation - the B-2's "
            "gust alleviation, the F-18's active controls. Done wrong, it is "
            "a new instability: the control system pumping energy into a "
            "structural mode (observe the 1990s' 'aeroservoelastic "
            "incidents'), or the structural modes corrupting the rigid-body "
            "handling through sensor pickup. The cruel twist is phase lag: "
            "actuators, filters, and digital sampling each add delay, and "
            "delay turns well-meant damping into excitation at high "
            "frequency. Aeroservoelasticity is therefore analyzed as one "
            "coupled system - structure, unsteady air, AND control law - "
            "never as three separate afterthoughts."
        ),
        "how_it_works": (
            "Extend the 2-DOF flutter model with a control loop: the flap "
            "deflects in response to sensed pitch, delta = -g_c*alpha_sensed, "
            "and the sensor/actuator chain adds a first-order lag "
            "1/(1 + i*omega*tau). The control adds an aerodynamic moment "
            "proportional to the lagged pitch - extra damping when the lag "
            "is small, extra excitation when the lag approaches half a "
            "cycle. The demo computes the flutter speed open-loop vs "
            "closed-loop for the demo section: with fast actuators "
            "(tau = 0.01 s) a modest gain lifts V_F by 15%+; with slow "
            "actuators (tau = 0.1 s) the same gain barely helps and higher "
            "gains destabilize - the phase-lag tradeoff that dominates "
            "aeroservoelastic design, shown numerically."
        ),
        "key_points": [
            "Aeroservoelasticity: structure + unsteady aerodynamics + flight control as ONE coupled system.",
            "Active flutter suppression and gust alleviation are its constructive uses.",
            "Phase lag (actuator, filter, sampling) is the enemy: delay turns damping into excitation.",
            "Sensor pickup of structural modes can corrupt rigid-body handling qualities.",
            "Analysis must include the control law from the start, not as an afterthought.",
            "Certification covers the closed-loop system including failure cases.",
        ],
        "requirements": [
            "Add a lagged feedback loop to the 2-DOF flutter model.",
            "Show V_F improvement with fast actuators and erosion with slow ones.",
            "Explain the phase-lag mechanism in two sentences.",
        ],
        "standards": [
            "Aeroservoelastic modeling per Wright & Cooper Ch. 13 / Dowell.",
            "First-order actuator lag as the teaching model.",
        ],
        "citations": [C_WC, C_DOWELL, C_HP],
        "sig_lens": (
            "His Signature reading: the flight computer is the newest "
            "member of the aeroelastic conversation, and it speaks with a "
            "delay - every millisecond of lag is a word spoken late. "
            "Signature control laws are timed like music, not wired like "
            "plumbing."
        ),
    },
    {
        "key": "flutter_suppression",
        "name": "Flutter Suppression: Active Control of the Boundary",
        "group": "Design & Control",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Active flutter suppression uses control surfaces driven by a "
            "flutter-aware control law to push the flutter boundary beyond "
            "the passive structure's limit - adding damping exactly where "
            "the air is removing it. The idea was flight-demonstrated on "
            "programs like the F-4F flutter suppression tests and the "
            "NASA DAST (Drones for Aerodynamic and Structural Testing) "
            "program: a wing deliberately flown past its passive flutter "
            "speed, held stable by the active system. The design problem is "
            "gain scheduling (the law must work across the whole envelope), "
            "robustness (it must not destabilize other modes - spillover), "
            "and failure safety (what happens when the system quits at "
            "high q). No production airliner today relies on active "
            "suppression for its basic flutter clearance - the regulators "
            "demand passive margins - but gust alleviation systems use the "
            "same machinery, and the technology waits for the designs that "
            "need it."
        ),
        "how_it_works": (
            "Design as optimization: for the demo section, the control law "
            "is pitch-rate feedback to the flap, delta = -g*(alpha + "
            "T_d*alpha_dot)-ish through the actuator lag. The demo sweeps "
            "the feedback gain g and recomputes the closed-loop flutter "
            "speed with the same k-method engine: V_F rises with g, quickly "
            "at first, then saturates as the actuator lag caps the phase "
            "margin. It finds the minimum gain that buys a 15% flutter-"
            "speed increase (the classic suppression target), checks the "
            "gain margin at neighboring modes (spillover check), and shows "
            "the failure case: with the loop open at the suppressed speed, "
            "the system is violently unstable - which is why regulators "
            "insist on passive clearance underneath."
        ),
        "key_points": [
            "Active flutter suppression: control law adds damping where the air removes it.",
            "Demonstrated on F-4F and NASA DAST; not used for basic clearance on production airliners.",
            "Design = gain scheduling + spillover avoidance + failure safety.",
            "V_F rises with gain then saturates (actuator lag caps the benefit).",
            "Failure case is violent: the suppressed speed is unstable open-loop - hence passive margins required.",
            "Gust alleviation is the production cousin using the same machinery.",
        ],
        "requirements": [
            "Sweep feedback gain vs closed-loop V_F; find the 15% gain.",
            "Check spillover at a neighboring mode.",
            "Show the open-loop instability at the suppressed speed.",
        ],
        "standards": [
            "Suppression design per Dowell / Wright & Cooper active-controls chapters.",
            "Failure-safety discussion per FAR 25.629/25.1309 philosophy.",
        ],
        "citations": [C_DOWELL, C_WC],
        "sig_lens": (
            "His Signature reading: suppression is the autopilot holding "
            "the wing's hand past the cliff edge - it works, but the hand "
            "must never let go. Signature practice: earn the passive margin "
            "first, then let the active system spend it wisely."
        ),
    },
]

ENTRIES += [
    {
        "key": "gvt",
        "name": "Ground Vibration Testing: Listening to the Modes",
        "group": "Testing & Certification",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Before any flutter analysis is trusted, the structural model is "
            "checked against the real airplane in a ground vibration test: "
            "the aircraft is suspended on soft supports (or its gear, "
            "deflated), shaken with electrodynamic shakers or instrumented "
            "hammers, and hundreds of accelerometers record the response. "
            "From the frequency response functions the engineers extract "
            "the true natural frequencies, damping ratios, and mode shapes - "
            "the modal survey that the flutter model must reproduce. "
            "Discrepancies mean the finite-element model is wrong (usually "
            "joint stiffnesses, which analysis always gets wrong), and the "
            "model is updated until it matches. The GVT is the moment the "
            "flutter clearance stops being a computer's opinion and starts "
            "being a measured fact about the actual airframe."
        ),
        "how_it_works": (
            "The workhorse is the frequency response function "
            "H(omega) = X/F: shake at frequency omega, measure the complex "
            "response. Near a resonance the FRF traces a circle in the "
            "complex plane (Nyquist circle); the circle's diameter gives the "
            "modal strength, its sweep rate gives the damping. The demo "
            "synthesizes an FRF from three known modes (4, 8, 13 Hz with 1%, "
            "1.5%, 2% damping) plus measurement noise, then plays test "
            "engineer: it picks the resonance peaks, applies the half-power "
            "bandwidth method (zeta = delta_omega/(2*omega_n)) at each, and "
            "recovers the frequencies within 1% and the dampings within 20% "
            "of truth - the standard GVT acceptance check, in miniature."
        ),
        "key_points": [
            "GVT: experimental modal survey of the full aircraft; the flutter model's reality check.",
            "Shakers/hammers in, accelerometers out; FRFs are the raw product.",
            "Extract: natural frequencies, damping ratios, mode shapes (half-power, circle-fit, or polyreference).",
            "FE model updated to match GVT before flutter clearance is granted.",
            "Joint stiffnesses are the usual culprit when analysis and test disagree.",
            "Damping measured on the ground is the baseline every flutter prediction builds on.",
        ],
        "requirements": [
            "Explain the FRF and the half-power damping formula.",
            "Extract 3 modes from a noisy synthetic FRF; report errors.",
            "State what happens when the model disagrees with the test.",
        ],
        "standards": [
            "Modal testing per standard practice (Ewins 'Modal Testing' concepts).",
            "Half-power bandwidth: zeta = (f2-f1)/(2*f_n).",
        ],
        "citations": [C_WC, C_HP],
        "sig_lens": (
            "His Signature reading: the ground vibration test is the "
            "airplane telling the truth about itself before the air gets a "
            "vote - every mode, every damping, measured not modeled. "
            "Signature models are tuned to the airplane's own testimony."
        ),
    },
    {
        "key": "wind_tunnel_flutter",
        "name": "Wind-Tunnel Flutter Testing: Small Models, Full Physics",
        "group": "Testing & Certification",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Flutter is still cleared in the wind tunnel, on dynamically "
            "scaled models that flutter like the airplane will - because the "
            "transonic dip and the nonlinearities cannot be fully computed. "
            "A flutter model is not a miniature airplane; it is a "
            "physics-preserving analog: the scaling laws (Mach, Froude, or "
            "the heavy-gas compromises) dictate its stiffness, mass, and "
            "frequencies so that the reduced frequencies, mass ratios, and "
            "mode shapes match the full scale. The classic facilities - "
            "NASA Langley's Transonic Dynamics Tunnel with its heavy-gas "
            "(R-12/R-134a) test medium, ONERA's S2MA - exist for this single "
            "purpose. The model is shaken, blown, and watched for the "
            "damping trends; the flutter boundary is approached by "
            "extrapolation, never by flying the model into it."
        ),
        "how_it_works": (
            "Scaling: for Mach-scaled testing, velocities scale with the "
            "speed of sound ratio, frequencies with (V_model/V_full)/"
            "(L_model/L_full), masses with (rho_model/rho_full)*"
            "(L_model/L_full)^3, and stiffnesses follow from the frequency "
            "and mass scales. Heavy gas (high density, low speed of sound) "
            "lets a small model hit transonic Mach numbers at low speeds "
            "and high dynamic pressures - the TDT's trick. The demo designs "
            "a 1/10-scale transonic flutter model of a transport wing: from "
            "full-scale targets (flutter mode 3 Hz, wing mass 4000 kg) it "
            "computes the model's frequencies, masses, and spar stiffnesses "
            "for a pressurized heavy-gas tunnel, and verifies the reduced "
            "frequency and mass ratio match - the similitude check that "
            "makes the model's flutter the airplane's flutter."
        ),
        "key_points": [
            "Flutter models are dynamically scaled analogs, not miniatures: Mach, mass ratio, reduced frequency must match.",
            "Heavy-gas tunnels (TDT) reach transonic Mach at low speed: the transonic-dip facility.",
            "Frequency scale = velocity scale / length scale; mass scale = density ratio x length^3.",
            "The boundary is approached by damping extrapolation, never by entering flutter.",
            "Model design is itself an aeroelastic optimization (spar sizing for target modes).",
            "Tunnel data anchors the flutter clearance where computation cannot (transonic dip).",
        ],
        "requirements": [
            "State the Mach-scaling laws for frequency, mass, and stiffness.",
            "Design the 1/10-scale model parameters from full-scale targets.",
            "Verify reduced-frequency and mass-ratio similitude.",
        ],
        "standards": [
            "Aeroelastic scaling per BAH Ch. 10; TDT heavy-gas practice.",
            "Similitude parameters: k, mu, Mach explicitly matched.",
        ],
        "citations": [C_BAH, C_DOWELL, C_WC],
        "sig_lens": (
            "His Signature reading: the flutter model is a small prophet - "
            "built to the scaling laws, it flutters in miniature so the "
            "airplane never has to. Signature scaling respects every "
            "similitude, because a prophet that lies is worse than none."
        ),
    },
    {
        "key": "flight_flutter_test",
        "name": "Flight Flutter Testing: Expanding the Envelope Safely",
        "group": "Testing & Certification",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Flight flutter testing is the most disciplined kind of flying: "
            "the test airplane, instrumented with accelerometers and "
            "excitation systems (control-surface sweeps, rotating-mass "
            "shakers, even pyrotechnic 'thumpers'), expands its envelope "
            "point by point while engineers on the ground watch the damping "
            "of every structural mode in real time. At each stabilized "
            "point the modes are excited, their decay measured, and the "
            "damping trend extrapolated - the Zimmerman-Weissenburger "
            "flutter margin and similar criteria turn the damping-vs-speed "
            "curve into a predicted flutter speed with a safety factor. The "
            "rules are absolute: never extrapolate more than a small step, "
            "never chase a mode whose damping is falling fast, always have "
            "an abort (slow down, the damping comes back). Every new "
            "airplane's envelope was opened this way, one careful point at "
            "a time."
        ),
        "how_it_works": (
            "The damping of the critical mode typically falls roughly "
            "quadratically with dynamic pressure near the boundary: "
            "zeta(q) ~ zeta_0*(1 - (q/q_F)^2)-ish. Measure zeta at several "
            "subcritical q, fit the trend, extrapolate to zeta = 0: that is "
            "the predicted flutter point, and the test program stops far "
            "short of it. The demo synthesizes measured damping values "
            "(with realistic scatter) at six subcritical dynamic pressures "
            "for a mode heading to flutter at q_F, fits a quadratic by least "
            "squares, extrapolates to the zero crossing, and recovers q_F "
            "within 10% - the exact arithmetic the flutter test team does "
            "between test points, with the extrapolation discipline "
            "(small steps only) stated as procedure."
        ),
        "key_points": [
            "Envelope expansion: excite, measure decay, extrapolate damping - one careful point at a time.",
            "Excitation: control-surface sweeps, shakers, impulse devices; telemetry to the ground room.",
            "Damping vs q extrapolated (Zimmerman-Weissenburger margin) to predict the boundary from subcritical data.",
            "Never fly to flutter: the prediction keeps the airplane 15%+ short of the boundary.",
            "Falling damping + rising response = knock it off (slow down).",
            "Flight test is the final clearance authority: analysis predicts, tunnel anchors, flight proves.",
        ],
        "requirements": [
            "Fit damping-vs-q data and extrapolate to the zero crossing.",
            "Recover the true q_F within 10% from noisy subcritical data.",
            "State the extrapolation-discipline rules.",
        ],
        "standards": [
            "Flight flutter test practice per Wright & Cooper / industry (Zimmerman-Weissenburger).",
            "Least-squares quadratic fit; extrapolation range limited.",
        ],
        "citations": [C_WC, C_DOWELL],
        "sig_lens": (
            "His Signature reading: flight flutter testing is courage with "
            "a spreadsheet - the airplane asks the air each question once, "
            "politely, and never asks the last question. Signature envelopes "
            "are opened the same way: evidence first, altitude second."
        ),
    },
    {
        "key": "certification",
        "name": "Certification: Proving the Envelope Under FAR 25.629",
        "group": "Testing & Certification",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "FAR 25.629 is the law of aeroelasticity for transport airplanes: "
            "the airplane must be free from aeroelastic instability - "
            "flutter, divergence, control reversal - throughout its flight "
            "envelope, demonstrated by analysis, wind-tunnel test, and "
            "flight test together. The regulation demands clearance to the "
            "design dive speed V_D (and Mach), plus margins: analyses must "
            "show no instability up to 1.15*V_D for certain conditions, "
            "damping must remain adequate everywhere inside the envelope "
            "(the industry's 3%-damping rule of thumb), and failures - a "
            "jammed control, a failed damper, a damaged panel - must be "
            "assessed for their aeroelastic consequences. Compliance is a "
            "three-legged stool: validated analysis (anchored to GVT and "
            "tunnel), subcritical flight-test extrapolation, and the "
            "structural margins that make the whole thing robust to the "
            "unknown. No leg alone certifies an airplane."
        ),
        "how_it_works": (
            "The clearance logic is arithmetic on speeds: compute the "
            "flutter speed V_F (analysis, anchored), the divergence speed "
            "V_D, the reversal speed V_R; require min(V_F, V_D, V_R) >= "
            "1.2*V_D_envelope (the 20% margin form of the 25.629 "
            "requirement, with the 1.15 analysis factor applied where the "
            "regulation calls for it); require modal damping >= 0.03 g "
            "everywhere inside the envelope; assess failure cases "
            "individually. The demo runs the compliance check for a "
            "representative transport: given V_F, V_D, V_R from the earlier "
            "records' methods and the envelope dive speed, it verdicts each "
            "requirement pass/fail, computes the actual margins, and shows "
            "how a 5% shortfall in V_F would force either stiffening or an "
            "envelope restriction - the certification trade in numbers."
        ),
        "key_points": [
            "FAR 25.629: freedom from flutter, divergence, and control reversal across the envelope.",
            "Three-legged compliance: validated analysis + tunnel + flight test.",
            "Margins: clearance beyond V_D (1.15-1.2x factors), >=3% damping in-envelope (practice).",
            "Failure cases assessed: jammed/failed controls, failed dampers, damage.",
            "Shortfall remedies: stiffen the structure, restrict the envelope, or (rarely) active systems.",
            "Military: MIL-A-8870/MIL-HDBK-516C carry the parallel requirements.",
        ],
        "requirements": [
            "List the three instability clearances and their margins.",
            "Run the compliance arithmetic for a representative transport.",
            "State the shortfall remedies.",
        ],
        "standards": [
            "14 CFR 25.629 (a)-(d); damping practice per industry guidance.",
            "Military parallel: MIL-A-8870C noted.",
        ],
        "citations": [C_FAR, C_WC],
        "sig_lens": (
            "His Signature reading: certification is the promise written in "
            "regulation - no flutter, no divergence, no reversal, anywhere "
            "the airplane is allowed to go, with margin. Signature promises "
            "are kept with analysis, tunnel, and flight, all three."
        ),
    },
    {
        "key": "nonlinear_aeroelasticity",
        "name": "Nonlinear Aeroelasticity: Freeplay, Friction, and Beyond",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Real structures are nonlinear, and the nonlinearities write "
            "their own aeroelastic stories. Freeplay - the dead zone in a "
            "worn control linkage - lets a control surface rattle within "
            "plus/minus delta before the stiffness engages; the result is "
            "limit-cycle oscillation BELOW the linear flutter speed, the "
            "buzz pilots feel in tired linkages. Friction (Coulomb damping) "
            "kills small oscillations dead but is overwhelmed by large "
            "ones. Hardening springs raise frequencies with amplitude; "
            "softening drops them into resonance. Large deflections make the "
            "geometry itself nonlinear. And the aerodynamics bring their own: "
            "stall, shocks, separation. Nonlinear aeroelasticity is the "
            "discipline of these realities - harmonic balance, describing "
            "functions, and time-marching instead of eigenvalues - and its "
            "message is humbling: the linear flutter speed is where the "
            "trouble STARTS being possible, not where it starts."
        ),
        "how_it_works": (
            "The demo is freeplay, the classic: a torsional degree of "
            "freedom whose spring is dead for |alpha| < delta and linear "
            "beyond - the piecewise model of a worn hinge. Below the linear "
            "flutter speed the system is stable to small disturbances, but a "
            "large enough kick throws the surface across the dead zone, the "
            "impacts pump energy once per cycle, and a limit cycle "
            "establishes with amplitude a few times delta. The demo "
            "time-marches the piecewise system at 90% of the linear V_F: the "
            "linear model at the same speed is dead stable, while the "
            "freeplay model settles into a persistent LCO - proving the "
            "record's thesis numerically. It then shows the fix: preloading "
            "or tightening the linkage (delta -> 0) restores the linear "
            "boundary."
        ),
        "key_points": [
            "Freeplay: dead-zone stiffness -> LCO below the linear flutter speed.",
            "Friction: kills small motions, loses to large ones (amplitude-dependent damping).",
            "Hardening/softening: frequencies move with amplitude; resonances move too.",
            "Aerodynamic nonlinearities: stall, moving shocks, separation - each its own LCO source.",
            "Methods: time-marching, harmonic balance, describing functions - not eigenvalues.",
            "The linear flutter speed is where trouble becomes possible, not where it begins.",
        ],
        "requirements": [
            "Model freeplay as a piecewise stiffness and explain the energy pumping.",
            "Time-march to LCO below the linear flutter speed.",
            "Show the fix (remove the dead zone) restoring stability.",
        ],
        "standards": [
            "Freeplay LCO per Dowell Ch. 4 / industry practice.",
            "Piecewise-linear time-march with event handling at the dead-zone boundary.",
        ],
        "citations": [C_DOWELL, C_BAH],
        "sig_lens": (
            "His Signature reading: freeplay is the structure lying about "
            "its stiffness - silent in the middle, honest at the edges, and "
            "the air collects the difference as a buzz. Signature linkages "
            "have no dead zones; the truth is preloaded."
        ),
    },
    {
        "key": "gust_response",
        "name": "Gust Response and Alleviation: Riding the Rough Air",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Gust response is the airplane's answer to turbulence: the "
            "vertical gust velocity adds to the angle of attack, the lift "
            "jumps, the structure bends, and the flexible modes ring - the "
            "ride quality, the fatigue damage, and the limit loads all come "
            "out of this calculation. Certification defines two gust "
            "worlds: the discrete gust (a 1-cosine bump of prescribed "
            "gradient distance, FAR 25.341) and continuous turbulence (the "
            "von Karman spectrum, a statistical atmosphere). The flexible "
            "airplane responds less than the rigid one at high frequency "
            "(the structure cannot follow) but rings at its modes - and "
            "gust alleviation systems (ailerons/spoilers driven by "
            "angle-of-attack vanes or accelerometers) can cancel much of "
            "the rigid-body gust load before the structure ever feels it. "
            "The B-2's gust alleviation and every modern airliner's load-"
            "alleviation function are this record, flying."
        ),
        "how_it_works": (
            "The discrete gust: w_g(s) = (w_0/2)*(1 - cos(2*pi*s/L_g)) over "
            "gradient distance L_g. The unsteady lift is the convolution of "
            "the gust profile with Kuessner's function (the gust memory from "
            "the Kuessner record): as the wing penetrates, each station's "
            "lift builds with psi(tau). The demo flies the demo wing "
            "section through a 1-cosine gust (L_g = 12.5 chords, the "
            "certification 'tuning' distance), convolves with psi, and "
            "computes the peak incremental load factor delta_n = "
            "delta_L/W. It then engages a simple alleviation: ailerons "
            "deflect proportional to the sensed gust angle with a realistic "
            "lag, and the peak load drops 20-30% - the alleviation credit "
            "that lets wings be lighter."
        ),
        "key_points": [
            "Discrete gust (1-cosine, FAR 25.341) and continuous turbulence (von Karman) are the two certification gust worlds.",
            "Unsteady gust lift = convolution of gust profile with Kuessner's psi.",
            "Flexible response: less than rigid at high frequency, plus modal ringing.",
            "Gust alleviation: control surfaces cancel the gust angle before the structure feels it (20-30% load cut).",
            "The 12.5-chord gradient distance is the traditional tuning case.",
            "Ride quality, fatigue, and limit loads all flow from this analysis.",
        ],
        "requirements": [
            "Write the 1-cosine gust and the Kuessner convolution.",
            "Compute peak delta_n for the demo section.",
            "Show the alleviation reduction with a lagged aileron loop.",
        ],
        "standards": [
            "Discrete gust per 14 CFR 25.341; Kuessner convolution per Fung Ch. 7.",
            "Load factor in g's; alleviation as a simple lagged loop.",
        ],
        "citations": [C_FAR, C_FUNG, C_WC],
        "sig_lens": (
            "His Signature reading: the gust is the sky's pothole, and the "
            "flexible wing is the suspension - alleviation is the active "
            "suspension reading the road ahead. Signature ride quality is "
            "designed, not hoped for."
        ),
    },
    {
        "key": "integrated_design",
        "name": "The Integrated Aeroelastic Design: Loads to Tailoring to Proof",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The capstone: designing a wing the way it is actually done, as "
            "one aeroelastic loop. Start from the mission (speeds, weights) "
            "and compute the rigid air loads; bend the wing under them and "
            "recompute the flexible loads (load redistribution); size the "
            "structure to those loads (spar gauges from bending, skin from "
            "torsion); check divergence, reversal, and flutter of the sized "
            "wing; if flutter falls short, tailor the composite layup "
            "(bend-twist coupling) and recheck; verify the gust loads and "
            "the fatigue spectrum; then prove it all by the certification "
            "path - GVT to update the model, tunnel for the transonic dip, "
            "flight test to open the envelope. Each step feeds the next; a "
            "change anywhere ripples everywhere. This record runs that loop "
            "on the demo wing from the earlier records and closes it: loads, "
            "sizing, divergence, flutter, tailoring fix, gust check, "
            "certification verdict - the whole discipline in one pass."
        ),
        "how_it_works": (
            "The demo chains the database's own methods: (1) mission speeds "
            "and weight -> rigid lift and root bending moment; (2) beam "
            "bending -> tip deflection and washout -> flexible loads "
            "(iterate to convergence); (3) size spar caps from the bending "
            "moment and torsional stiffness from a thin-wall box; "
            "(4) compute q_D, V_D, q_R from the sized stiffness; (5) run the "
            "2-DOF k-method flutter analysis on the sized section -> V_F; "
            "(6) if V_F < 1.2*V_D_envelope, apply composite tailoring "
            "(washout coupling) and recompute until the margin closes; "
            "(7) discrete-gust delta_n check; (8) the FAR 25.629 compliance "
            "verdict. Every number is computed, every check asserted - the "
            "integrated loop executing end to end on one consistent wing."
        ),
        "key_points": [
            "Real wing design is one coupled loop: loads -> flexibility -> sizing -> stability -> tailoring -> proof.",
            "Each discipline's output is the next discipline's input; changes ripple around the loop.",
            "Tailoring is the design degree of freedom that closes difficult loops (X-29 pattern).",
            "The demo executes all eight steps on one consistent wing with asserted checks.",
            "Certification (25.629) is the loop's exit criterion, not an afterthought.",
            "This record is the database's thesis: aeroelasticity is a design discipline, not a failure mode.",
        ],
        "requirements": [
            "Chain loads, sizing, divergence, flutter, tailoring, gust, and certification checks.",
            "Close the loop: iterate tailoring until the flutter margin passes.",
            "Assert every check; report the final margins.",
        ],
        "standards": [
            "Methods per the earlier records in this database (strip loads, box sizing, k-method, 25.629).",
            "One consistent wing definition shared across steps.",
        ],
        "citations": [C_WC, C_BAH, C_DOWELL, C_FAR],
        "sig_lens": (
            "His Signature reading: the integrated loop is the whole "
            "discipline grown up - no longer asking 'will it flutter' but "
            "telling the wing what to be. Signature design runs this loop "
            "until every number is a promise kept."
        ),
    },
]
