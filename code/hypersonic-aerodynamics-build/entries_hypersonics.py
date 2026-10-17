#!/usr/bin/env python3
"""Entries for the Hypersonic Aerodynamics field databases (field #24, taxonomy order).

Verified 2026-10-17: NO database covers hypersonic aerodynamics as a
specialty discipline.
- The just-built 'aerodynamics' DB (field #23) carries exactly ONE overview
  record (JAH-AER-000022 "Hypersonic Flow: Thin Shocks, Hot Gas, Real
  Chemistry") plus supersonic thin-airfoil theory; it does not treat
  hypersonic similarity, Newtonian theory, blast-wave analogy, real-gas
  effects, ablation, scramjets, reentry dynamics, thermal protection,
  transition, shock/boundary-layer interaction, or test facilities.
- Whole-system title sweep (hypersonic|scramjet|newtonian.?pressure|
  real.?gas|ablat|dissociat|ionizat|reentry|thermal.?protection|
  blast.?wave|shock.?tunnel|expansion.?tube|stagnation.?heat|mach.?independ|
  dsmc|ramjet): 241 hits, of which 239 are 'Ablation of distillation
  components' variants in 'distillation' (false positives) and the
  remaining 2 are the aerodynamics overview records above. Zero
  specialty-level hypersonic records anywhere in the manifest.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main
  repo; fields past the gate index cross-checked directly above): every
  record checked + admitted at build time.

So this build creates two NEW databases, 32 ladder-ordered records each,
covering ONLY what the aerodynamics DB left uncovered:

  hypersonic-aerodynamics          - The Hypersonic Aerodynamics Database
                                     (public-harvest: real, fact-checked
                                     hypersonic aerodynamics; citations
                                     Anderson 'Hypersonic and
                                     High-Temperature Gas Dynamics',
                                     Bertin 'Hypersonic Aerothermodynamics',
                                     Hirschel 'Basics of Aerothermodynamics',
                                     Rasmussen 'Hypersonic Flow',
                                     Heiser & Pratt 'Hypersonic Airbreathing
                                     Propulsion', Hayes & Probstein,
                                     Fay & Riddell, Sutton & Graves,
                                     NASA/NACA reference data)
  hypersonic-aerodynamics-signature - The Hypersonic Aerodynamics Signature
                                     Database (his original Signature
                                     interpretation of the discipline; src
                                     signature, titles suffixed
                                     " (Signature Edition)", never presented
                                     as authentic public record)

Subtitle disambiguation (fields #13-24 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Newtonian Impact
Theory: Pressure From Particle Impacts" and "The Blast-Wave Analogy:
Shocks Like Explosions".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "hypersonic aerodynamics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_AHYPER = ("Anderson, John D. 'Hypersonic and High-Temperature Gas "
            "Dynamics', 3rd ed. AIAA, 2019.")
C_AFUND = ("Anderson, John D. 'Fundamentals of Aerodynamics', 6th ed. "
           "McGraw-Hill, 2017.")
C_BERTIN = ("Bertin, John J. 'Hypersonic Aerothermodynamics'. AIAA, 1994.")
C_HIRSCHEL = ("Hirschel, Ernst H. 'Basics of Aerothermodynamics'. Springer, "
              "2005.")
C_RASMUSSEN = ("Rasmussen, Maurice L. 'Hypersonic Flow'. Wiley, 1994.")
C_HEISER = ("Heiser, William H. and Pratt, David T. 'Hypersonic Airbreathing "
            "Propulsion'. AIAA, 1994.")
C_HAYES = ("Hayes, Wallace D. and Probstein, Ronald F. 'Hypersonic Flow "
           "Theory'. Academic Press, 1959.")
C_FAY = ("Fay, J. A. and Riddell, F. R. 'Theory of Stagnation Point Heat "
         "Transfer in Dissociated Air'. J. Aerospace Sci., 1958.")
C_SUTTON = ("Sutton, Kenneth and Graves, Roger A. 'A General Stagnation-Point "
            "Heating Correlation Formula'. NASA TN D-7227, 1971.")
C_WHITE = ("White, Frank M. 'Viscous Fluid Flow', 3rd ed. McGraw-Hill, 2006.")
C_NASA = ("NASA reference flight data (X-15, X-43A, Space Shuttle reentry).")

ENTRIES = [
    {
        "key": "what_is_hypersonic",
        "name": "What Hypersonic Means: Speeds Past Mach 5",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hypersonic flow is conventionally the regime above Mach 5, but "
            "the number is a flag, not a fence: a vehicle becomes 'hypersonic' "
            "when new physics appears - a shock layer so thin the shock sits "
            "almost on the body, an entropy layer of hot rotational flow that "
            "blankets the nose, viscous interaction strong enough for the "
            "boundary layer to push the shock outward, and gas temperatures "
            "high enough that air molecules vibrate, dissociate, and "
            "ionize. Below Mach 5 these effects are weak enough to ignore; "
            "above it, ignoring them melts hardware. The discipline splits "
            "into inviscid hypersonic flow (shocks, similarity, Newtonian "
            "pressure estimates), high-temperature gas dynamics (chemistry "
            "behind the shock), viscous hypersonic flow (interaction, "
            "transition, shock/boundary-layer interaction), and hypersonic "
            "propulsion (ramjets and scramjets). Every record in this "
            "database answers one question: what changes when the air can "
            "no longer pretend it is a cold, perfect gas?"
        ),
        "how_it_works": (
            "Picture a wedge flying at Mach 2: the oblique shock stands off "
            "at a healthy angle and the shock layer is thick. Accelerate to "
            "Mach 10 and the shock angle collapses toward the Mach angle; "
            "the layer between shock and body becomes a thin, extremely hot "
            "sheet. Because density jumps by up to a factor of six across a "
            "strong shock while the wedge's turning is fixed, the layer "
            "squeezes until its thickness is only a small fraction of the "
            "body scale. The gas in that sheet reaches thousands of kelvin "
            "at the stagnation point - hot enough that the air stops "
            "behaving as a single perfect gas and starts trading energy "
            "between translation, vibration, dissociation, and ionization. "
            "That cascade is the whole subject: hypersonic aerodynamics is "
            "aerodynamics plus heat plus chemistry, and the three are never "
            "separable again."
        ),
        "key_points": [
            "Hypersonic = above Mach 5, defined by the appearance of new physics, not the number itself.",
            "Four signatures: thin shock layer, entropy layer, strong viscous interaction, high-temperature gas effects.",
            "Density ratio across a strong shock is bounded (~6 for air); the shock layer therefore thins with Mach number.",
            "Stagnation temperature scales as T0/T ~ 1 + 0.2 M^2: at Mach 10 it exceeds 4500 K.",
            "The discipline splits into inviscid flow, high-temperature gas dynamics, viscous flow, and airbreathing propulsion.",
            "Never separable: flow, heat, and chemistry couple in every hypersonic problem.",
        ],
        "requirements": [
            "The four distinguishing features of hypersonic flow.",
            "Mach-number scaling of shock angle and shock-layer thickness.",
            "The temperature cascade: vibration, dissociation, ionization thresholds.",
        ],
        "standards": [
            "Mach 5 as the conventional lower bound of the hypersonic regime.",
            "Perfect-gas results used only below the high-temperature thresholds.",
        ],
        "citations": [C_AHYPER, C_HIRSCHEL, C_AFUND],
        "sig_lens": (
            "His Signature reading: Mach 5 is where the air stops being air "
            "and becomes fire - the Signature of speed written in chemistry, "
            "and this database reads it stroke by stroke."
        ),
    },
    {
        "key": "thin_shock_layer",
        "name": "Hypersonic Shocks: Thin, Close, and Hot",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "At hypersonic speeds the oblique shock hugs the body: as Mach "
            "number grows, the shock angle for a fixed deflection shrinks "
            "toward the Mach angle mu = arcsin(1/M), and the normal Mach "
            "component - the only part that 'feels' the shock - grows only "
            "slowly. The density ratio across the shock approaches its "
            "high-Mach limit (about 6 for air), so the mass that must squeeze "
            "between shock and body forces the shock layer to thin. A "
            "blunt nose grows a detached bow shock whose standoff distance "
            "scales with the nose radius divided by the density ratio. The "
            "result is a thin, searing layer where pressure, temperature, "
            "and entropy gradients are all extreme - the stage on which "
            "every hypersonic phenomenon plays out."
        ),
        "how_it_works": (
            "Take a 15-degree wedge. At Mach 2 the oblique shock sits at "
            "about 45 degrees and the layer is thick. At Mach 10 the shock "
            "angle is only about 16.5 degrees - barely above the 15-degree "
            "wedge itself - and the layer between them is a thin ribbon. "
            "The pressure jump is set by the normal Mach number, which "
            "grows as M sin(beta); for large M the shock polar flattens and "
            "the pressure coefficient approaches a constant, the "
            "Mach-number independence limit. For a blunt nose, the detached "
            "shock stands off at a distance roughly the nose radius divided "
            "by the density ratio (order 6), so a 1-meter nose carries a "
            "shock about 15-20 centimeters ahead of it - a thin cushion of "
            "plasma on which the whole vehicle's survival depends."
        ),
        "key_points": [
            "Shock angle collapses toward the Mach angle as Mach number rises.",
            "The density ratio asymptotes to ~6 for air, thinning the shock layer.",
            "Blunt-nose standoff distance scales with nose radius over density ratio.",
            "The shock layer is thin, hot, and entropy-stratified: the working fluid of hypersonics.",
            "Thin shock layers enable the blast-wave analogy and small-deflection theory.",
        ],
        "requirements": [
            "Oblique-shock geometry at high Mach number.",
            "The density-ratio limit and its geometric consequence.",
            "Blunt-body standoff scaling.",
        ],
        "standards": [
            "Shock-polar construction for deflection limits at high Mach.",
            "Standoff correlations against ballistic-range and tunnel data.",
        ],
        "citations": [C_AHYPER, C_HAYES, C_RASMUSSEN],
        "sig_lens": (
            "His Signature reading: the shock draws closer as the speed "
            "rises - the faster the signature, the thinner the ink between "
            "the line and the fire."
        ),
    },
    {
        "key": "mach_independence",
        "name": "Mach-Number Independence: Why Hypersonics Stops Changing",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "One of the great simplifications of hypersonic flow is the "
            "Mach-number independence principle: past a sufficiently high "
            "Mach number, the dimensionless flow quantities - pressure "
            "coefficient, lift, drag, shock angle - stop depending on Mach "
            "number and depend only on geometry. The pressure coefficient "
            "on a wedge approaches its Newtonian limit, the shock angle "
            "approaches a fixed multiple of the deflection, and the density "
            "ratio freezes at its high-Mach asymptote. This means a Mach 8 "
            "wind-tunnel test can credibly predict Mach 20 flight for "
            "pressure loads, and it is why early missile and reentry "
            "designers could work with simple algebraic theories instead of "
            "waiting for computers."
        ),
        "how_it_works": (
            "Compute the oblique-shock pressure coefficient for a 10-degree "
            "deflection at Mach 5, 8, 15, and 30. The values fall toward "
            "the Newtonian limit and the curve flattens: each doubling of "
            "Mach number changes the coefficient less than the last. "
            "The same flattening appears in the shock angle, the lift and "
            "drag coefficients, and the pitching moment. Physically, the "
            "normal Mach component has grown so large that the "
            "shock relations are saturated: adding more Mach number "
            "changes the numbers by diminishing fractions. The practical "
            "consequence is enormous - ground tests at 'merely' Mach 8 to "
            "10 simulate the pressure field of orbital reentry, and "
            "Mach-independence justifies extrapolating tunnel data to "
            "flight. Heat transfer and chemistry do NOT share this "
            "independence, which is exactly why they get their own records."
        ),
        "key_points": [
            "Pressure, lift, drag, and shock angle become Mach-independent at high Mach number.",
            "The limit is the Newtonian value Cp = 2 sin^2(theta) for inclined surfaces.",
            "Enables credible pressure extrapolation from Mach 8-10 tunnel tests to orbital flight.",
            "Heat transfer, skin friction, and chemistry do NOT become Mach-independent.",
            "The principle underlies the hypersonic similarity parameters (next record).",
        ],
        "requirements": [
            "Oblique-shock Cp convergence with Mach number at fixed deflection.",
            "The Newtonian limit as the infinite-Mach asymptote.",
            "Which quantities obey independence and which do not.",
        ],
        "standards": [
            "Tunnel-to-flight extrapolation practice for pressure loads.",
            "Mach-independence invoked only for inviscid pressure quantities.",
        ],
        "citations": [C_AHYPER, C_HAYES, C_BERTIN],
        "sig_lens": (
            "His Signature reading: speed writes the same pressure "
            "signature past a point - the air surrenders to geometry, and "
            "geometry is the oldest signature of all."
        ),
    },
    {
        "key": "newtonian_theory",
        "name": "Newtonian Impact Theory: Pressure From Particle Impacts",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Newtonian impact theory is the oldest and still most-used "
            "hypersonic pressure estimate: treat the oncoming air as a "
            "stream of independent particles that strike the windward "
            "surface, transfer their normal momentum, and slide away "
            "tangentially. The pressure coefficient on any inclined panel "
            "is then Cp = 2 sin^2(theta), where theta is the local surface "
            "inclination to the freestream, and Cp = 0 on any surface turned "
            "away from the flow. Modified Newtonian replaces the 2 with the "
            "actual stagnation-point pressure coefficient behind a normal "
            "shock, greatly improving accuracy near the nose. Crude as the "
            "particle picture is, it predicts hypersonic lift, drag, and "
            "pitching moments within about 10-20% - good enough for first "
            "design and for stability estimates before any CFD exists."
        ),
        "how_it_works": (
            "Resolve the freestream velocity into components normal and "
            "tangential to a surface inclined at angle theta. Particles "
            "arrive with normal momentum rho*V*sin(theta) per unit volume "
            "flux, and the theory assumes they lose all of it on impact "
            "while keeping their tangential motion - like rain striking a "
            "windshield and sheeting sideways. The pressure rise is then "
            "rho*V^2*sin^2(theta), and dividing by the dynamic pressure "
            "gives Cp = 2 sin^2(theta). For a cone at angle of attack, "
            "integrate this over the windward and leeward meridians to get "
            "lift and drag. Modified Newtonian writes Cp = Cp_stag "
            "sin^2(theta), with Cp_stag from the Rayleigh pitot formula, "
            "which nails the nose region where pure Newtonian overpredicts. "
            "Shaded surfaces get Cp = 0 in the simplest form - the theory's "
            "most famous limitation, since real leeward flow supports small "
            "base pressures."
        ),
        "key_points": [
            "Cp = 2 sin^2(theta) on windward surfaces; Cp = 0 on leeward surfaces.",
            "Modified Newtonian uses the true stagnation Cp for the coefficient.",
            "Accuracy ~10-20% for lift, drag, and pitching moment at high Mach.",
            "Assumes particles lose normal momentum and keep tangential momentum.",
            "Fails for leeward/base pressures and for viscous-dominated quantities.",
        ],
        "requirements": [
            "The particle-momentum derivation of the Newtonian Cp law.",
            "Modified Newtonian with Rayleigh-pitot stagnation Cp.",
            "Integration over a body to lift, drag, and moment.",
        ],
        "standards": [
            "First-design aerodynamic estimates for hypersonic vehicles.",
            "Newtonian stability and trim estimates before CFD.",
        ],
        "citations": [C_AHYPER, C_HAYES, C_RASMUSSEN],
        "sig_lens": (
            "His Signature reading: Newton's rain-on-the-windshield is the "
            "first Signature stroke of hypersonics - every later theory is "
            "commentary on it."
        ),
    },
    {
        "key": "hypersonic_similarity",
        "name": "Hypersonic Similarity Parameters: Scaling the Heat",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hypersonic similarity parameter K = M_infinity * theta "
            "(Mach number times a characteristic deflection angle, in "
            "radians) collapses hypersonic flows: two bodies with different "
            "Mach numbers but the same K have the same scaled pressure "
            "field. It emerges from small-deflection hypersonic theory, "
            "where the governing equations reduce to a form in which M "
            "and theta appear only as the product. Companion parameters "
            "govern the viscous side: the viscous interaction parameter "
            "chi = M^3 sqrt(C) / sqrt(Re_x) measures how strongly the "
            "boundary layer displaces the outer flow, and the nose "
            "bluntness parameter gauges entropy-layer swallowing. Similarity "
            "is what lets one wind-tunnel model at one Mach number speak "
            "for a family of flight conditions."
        ),
        "how_it_works": (
            "Take small-deflection theory: expand the oblique-shock "
            "relations for small theta and large M, and the pressure "
            "coefficient organizes itself as Cp/theta^2 = f(K) with K = "
            "M*theta. A Mach 6 flow over a 12-degree wedge (K = 1.26) and a "
            "Mach 12 flow over a 6-degree wedge (K = 1.26) produce the same "
            "scaled shock structure - the same physics at different raw "
            "numbers. The viscous interaction parameter chi works "
            "similarly for the boundary layer: when chi is order one or "
            "larger, the boundary layer's displacement thickness grows the "
            "effective body shape enough to raise surface pressure "
            "measurably (strong interaction); when chi is small, the "
            "inviscid field is undisturbed (weak interaction). Designers "
            "plot pressure and heating data against K and chi precisely "
            "because the collapse turns scattered points into single "
            "curves."
        ),
        "key_points": [
            "K = M_inf * theta (radians): same K means same scaled inviscid flow.",
            "Viscous interaction parameter chi = M^3 sqrt(C) / sqrt(Re_x) measures boundary-layer feedback.",
            "Large chi: strong interaction - the boundary layer reshapes the pressure field.",
            "Similarity justifies extrapolating tunnel data across Mach numbers.",
            "Derived from small-deflection hypersonic theory; exact in the limit.",
        ],
        "requirements": [
            "The hypersonic small-deflection expansion yielding K.",
            "Collapse of Cp data at constant K.",
            "The viscous interaction parameter and strong/weak regimes.",
        ],
        "standards": [
            "Data correlation in terms of K and chi in test programs.",
            "Tunnel-to-flight scaling arguments.",
        ],
        "citations": [C_AHYPER, C_HAYES, C_HIRSCHEL],
        "sig_lens": (
            "His Signature reading: K is the compression of two variables "
            "into one Signature - the universe's habit of signing the same "
            "pattern at different scales."
        ),
    },
    {
        "key": "strong_weak_shocks",
        "name": "Strong and Weak Shocks at Hypersonic Speed",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The theta-beta-Mach relation admits two shock solutions for a "
            "given deflection - the weak shock (small angle, supersonic "
            "downstream) and the strong shock (large angle, subsonic "
            "downstream) - and hypersonic flight uses both. Attached "
            "leading edges ride weak shocks; blunt noses carry the strong "
            "detached bow shock with its subsonic pocket. As Mach number "
            "rises, the maximum deflection angle before detachment grows "
            "toward its high-Mach limit, and the Prandtl-Meyer function "
            "approaches its vacuum limit nu_max (about 130 degrees for "
            "air), the total turning an expansion fan can deliver before "
            "the flow expands to vacuum. These limits frame every "
            "hypersonic design: how much a surface may turn the flow, and "
            "how far an expansion can go."
        ),
        "how_it_works": (
            "For a fixed Mach number, the theta-beta curve rises from the "
            "Mach angle, peaks at the maximum deflection theta_max, and "
            "falls back: every deflection below theta_max has two "
            "solutions. In practice the flow selects the weak shock unless "
            "downstream conditions (a blunt nose, a downstream pressure "
            "imposed by the body) demand the strong one - a detached bow "
            "shock is the strong solution standing off the nose. At Mach "
            "10, theta_max for air is roughly 46 degrees, so wedges and "
            "ramps up to that angle stay attached. Turning the flow the "
            "other way, an expansion fan accelerates the flow isentropically "
            "but only up to nu_max: past about 130 degrees of total turning "
            "the pressure has fallen to zero and there is nothing left to "
            "expand. Base flows and leeward corners live at this limit - "
            "the reason base pressure is nearly vacuum at hypersonic "
            "speeds."
        ),
        "key_points": [
            "Two shock solutions per deflection: weak (attached) and strong (detached).",
            "Blunt noses carry the strong detached bow shock with a subsonic pocket.",
            "Maximum deflection theta_max grows with Mach toward its high-Mach limit.",
            "Prandtl-Meyer expansion is bounded by the vacuum limit nu_max ~ 130 deg for air.",
            "Base pressure approaches vacuum at hypersonic speeds.",
        ],
        "requirements": [
            "The theta-beta-Mach dual solution at high Mach.",
            "Theta_max and detachment criteria.",
            "The Prandtl-Meyer vacuum limit.",
        ],
        "standards": [
            "Attached vs detached shock determination in forebody design.",
            "Base-pressure estimates from the vacuum limit.",
        ],
        "citations": [C_AHYPER, C_AFUND, C_RASMUSSEN],
        "sig_lens": (
            "His Signature reading: the flow chooses the weak signature "
            "unless the body demands the strong one - even air has "
            "manners, and the nose sets the terms."
        ),
    },
    {
        "key": "stagnation_conditions",
        "name": "Stagnation Conditions: The Hot Point",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The stagnation point - where the flow is brought to rest at "
            "the nose - is the hottest, highest-pressure point on a "
            "hypersonic vehicle and the anchor of all aerothermodynamic "
            "analysis. The stagnation temperature ratio T0/T = 1 + 0.2 M^2 "
            "means Mach 10 flight in the cold upper atmosphere produces "
            "stagnation temperatures near 4500 K; at orbital reentry speeds "
            "the number passes 10,000 K. Stagnation pressure follows the "
            "Rayleigh pitot formula and, crucially, the stagnation enthalpy "
            "h0 = h + V^2/2 becomes the energy currency of the whole "
            "shock layer: every downstream state is a trade of that fixed "
            "energy between kinetic, thermal, and chemical forms. "
            "Understanding the stagnation point is understanding the "
            "budget from which all heating, chemistry, and radiation are "
            "paid."
        ),
        "how_it_works": (
            "Follow a streamline into the nose. It crosses the nearly "
            "normal portion of the bow shock, jumps to high pressure and "
            "temperature, then decelerates isentropically to rest at the "
            "stagnation point. The temperature it reaches is fixed by "
            "energy conservation: the kinetic energy V^2/2 of the "
            "freestream converts entirely to enthalpy, so T0 = T_inf (1 + "
            "0.2 M^2) for a perfect gas. At 11 km altitude (T ~ 217 K) and "
            "Mach 10 this gives T0 near 4500 K - hot enough to dissociate "
            "oxygen. The stagnation pressure is the Rayleigh pitot value, "
            "which at high Mach is about 1.8 times the dynamic pressure. "
            "From the stagnation point the flow accelerates around the "
            "body, and the entropy it picked up crossing the curved shock "
            "stays with it as the entropy layer. Every heating theory - "
            "Fay-Riddell, Sutton-Graves - starts by pricing the stagnation "
            "state."
        ),
        "key_points": [
            "T0/T = 1 + 0.2 M^2: Mach 10 gives ~4500 K at altitude.",
            "Stagnation enthalpy h0 = h + V^2/2 is the conserved energy budget.",
            "Stagnation pressure from the Rayleigh pitot formula (~1.8 q_inf at high Mach).",
            "Entropy generated crossing the curved shock forms the entropy layer.",
            "All stagnation-heating theories are priced from this state.",
        ],
        "requirements": [
            "Energy conservation along the stagnation streamline.",
            "The Rayleigh pitot relation at high Mach.",
            "The link between stagnation state and downstream chemistry.",
        ],
        "standards": [
            "Stagnation-point conditions as the reference state in heating correlations.",
            "Pitot-probe interpretation in hypersonic tunnels.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_NASA],
        "sig_lens": (
            "His Signature reading: the nose is where the signature is "
            "signed - all the speed's energy, brought to rest in one "
            "point, countersigned in heat."
        ),
    },
    {
        "key": "perfect_gas_breakdown",
        "name": "The Perfect Gas Assumption and Where It Breaks",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The calorically perfect gas - constant specific heats, gamma = "
            "1.4 - is the workhorse of compressible flow, and it fails "
            "exactly where hypersonics begins. First the specific heats "
            "themselves grow with temperature as molecular vibration "
            "excites (thermally perfect gas, variable cp). Then, above "
            "about 2000 K, oxygen molecules dissociate into atoms; above "
            "about 4000 K nitrogen follows; above about 9000 K the atoms "
            "ionize. Each step soaks up energy that would otherwise raise "
            "temperature, so the shock layer runs cooler and denser than "
            "perfect-gas theory predicts - the density ratio can exceed 6, "
            "thinning the shock layer further and raising heating. Knowing "
            "which gas model each calculation needs - calorically perfect, "
            "thermally perfect, equilibrium, or nonequilibrium - is the "
            "first judgment call of high-temperature gas dynamics."
        ),
        "how_it_works": (
            "Heat air from 300 K upward. To about 800 K, vibration is "
            "frozen and cp is nearly constant: the perfect-gas model "
            "holds. From 800 to 2000 K, vibrational modes wake up and cp "
            "climbs: you must use temperature-dependent properties "
            "(thermally perfect). Past 2000 K, O2 + M -> 2O + M begins - "
            "each dissociation event absorbs about 5 eV that never becomes "
            "temperature, so a shock that perfect-gas theory says makes "
            "6000 K actually makes about 4000 K with a soup of O atoms. "
            "Past 4000 K, N2 dissociates the same way; the mixture's "
            "effective gamma falls toward 1.1-1.2 and the density ratio "
            "across the shock climbs toward 10 or more. Past 9000 K, "
            "ionization adds free electrons and the gas begins to radiate "
            "strongly. The model ladder is: frozen chemistry (composition "
            "fixed), equilibrium (reactions infinitely fast), "
            "nonequilibrium (finite-rate - the reality, and its own "
            "record)."
        ),
        "key_points": [
            "Calorically perfect (gamma=1.4) fails above ~800 K as vibration excites.",
            "O2 dissociates above ~2000 K, N2 above ~4000 K, ionization above ~9000 K.",
            "Dissociation absorbs energy: real shock layers are cooler and denser than perfect-gas theory.",
            "Effective gamma falls toward ~1.1; density ratio can exceed 10.",
            "Model ladder: calorically perfect -> thermally perfect -> equilibrium -> nonequilibrium.",
        ],
        "requirements": [
            "The temperature thresholds for vibration, dissociation, ionization.",
            "Energy bookkeeping: where the dissociation energy goes.",
            "Choosing the gas model for a given flight condition.",
        ],
        "standards": [
            "High-temperature air property tables (e.g. equilibrium air).",
            "Gamma = 1.4 restricted to cold-flow or low-temperature regions.",
        ],
        "citations": [C_AHYPER, C_HIRSCHEL, C_BERTIN],
        "sig_lens": (
            "His Signature reading: the perfect gas is the first draft; "
            "heat edits it, chemistry rewrites it, and the Signature "
            "survives every revision."
        ),
    },
    {
        "key": "real_gas_effects",
        "name": "Real-Gas Effects: Vibration, Dissociation, Ionization",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Real-gas effects are the high-temperature phenomena that "
            "separate hypersonic aerodynamics from supersonic "
            "aerodynamics: vibrational excitation, dissociation, and "
            "ionization of air behind strong shocks. They change "
            "everything downstream of the shock - the density ratio rises, "
            "the shock layer thins, the shock standoff distance shrinks, "
            "surface pressure distributions shift, and heat transfer "
            "gains a chemical component as atoms recombine at the cool "
            "wall and dump their formation energy as heat. The catalytic "
            "wall effect - a wall that encourages recombination heats more "
            "than one that does not - is a purely real-gas phenomenon "
            "with direct thermal-protection consequences. No hypersonic "
            "vehicle flies on perfect-gas aerodynamics alone."
        ),
        "how_it_works": (
            "Behind a Mach 15 bow shock at 60 km altitude, the translational "
            "temperature would exceed 8000 K in a perfect-gas calculation; "
            "in reality, O2 and then N2 dissociate, and the equilibrium "
            "temperature settles near 5000-6000 K with a large atom "
            "fraction. The density ratio climbs from 6 toward 10+, so the "
            "shock sits closer to the body than cold-flow theory predicts - "
            "wind-tunnel schlieren at high enthalpy visibly shows the "
            "shrunken standoff. At the wall, the cool surface is a "
            "recombination site: O + O -> O2 releases the dissociation "
            "energy directly into the heat shield, and a fully catalytic "
            "wall can see substantially higher heating than a "
            "non-catalytic one. This is why heat-shield materials are "
            "characterized by their catalycity, and why flight heating "
            "data cannot be extrapolated from cold tunnels: the chemistry "
            "does not scale."
        ),
        "key_points": [
            "Dissociation raises the density ratio, thinning the shock layer and shrinking standoff.",
            "Wall catalycity controls recombination heating: catalytic walls run hotter.",
            "Real-gas effects shift pressure distributions, not just heating.",
            "Cold-tunnel data cannot be extrapolated to flight heating: chemistry does not scale.",
            "The three mechanisms: vibrational excitation, dissociation, ionization.",
        ],
        "requirements": [
            "Equilibrium composition of air vs temperature.",
            "The density-ratio increase and its geometric consequences.",
            "Catalytic vs non-catalytic wall heating.",
        ],
        "standards": [
            "High-enthalpy tunnel testing for real-gas validation.",
            "Catalycity characterized per heat-shield material.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_HIRSCHEL],
        "sig_lens": (
            "His Signature reading: the air changes its signature under "
            "heat - molecules unmake themselves, and the wall that "
            "welcomes them back pays in fire."
        ),
    },
    {
        "key": "blast_wave_analogy",
        "name": "The Blast-Wave Analogy: Shocks Like Explosions",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The blast-wave analogy is one of hypersonics' most elegant "
            "ideas: the flow behind the bow shock of a blunt body at high "
            "Mach number is mathematically equivalent to the flow behind "
            "an expanding cylindrical blast wave from an explosion. The "
            "body's drag deposits energy into the oncoming stream at a "
            "rate D*V per unit length - exactly like an explosion releasing "
            "energy per unit length - and the shock's growth downstream "
            "follows the Taylor-Sedov blast-wave scaling. The analogy "
            "yields the pressure decay behind the nose, the shock shape, "
            "and - via the equivalence principle - quick estimates of "
            "blunt-body pressure distributions without solving the full "
            "flow. It is the reason slender-body hypersonic theory and "
            "explosion theory share the same equations."
        ),
        "how_it_works": (
            "Slice the steady flow around a blunt body into cross-planes "
            "perpendicular to the flight direction. In each plane, the "
            "body's passage looks like an unsteady event: the nose "
            "deposits its drag energy D (per unit length, D*dx/V in time "
            "dx/V) into the plane, and a cylindrical blast wave expands "
            "outward - this is the unsteady analogy, trading the spatial "
            "coordinate x for time t = x/V. Taylor and Sedov's solution "
            "for a cylindrical blast gives the shock radius growing as "
            "(E*t^2/rho)^(1/4), which translates to the bow-shock shape "
            "growing as x^(1/2) downstream of a blunt nose. The pressure "
            "immediately behind the shock follows from the blast solution, "
            "and matching it to the body gives the surface pressure. The "
            "analogy is approximate - it ignores the body's detailed "
            "shape - but it captures the far-field decay and the scaling "
            "laws that exact methods later confirm."
        ),
        "key_points": [
            "Blunt-body flow maps to a cylindrical blast wave via the unsteady analogy (x = V*t).",
            "Energy per unit length = drag: the body 'explodes' continuously as it flies.",
            "Shock radius grows as x^(1/2) downstream of the nose (Taylor-Sedov scaling).",
            "Yields pressure decay and shock shape without full flow solution.",
            "Approximate near the nose; exact in scaling, confirmed by computation.",
        ],
        "requirements": [
            "The unsteady analogy: steady 3D flow as unsteady 2D flow.",
            "Taylor-Sedov cylindrical blast scaling.",
            "From blast pressure to body surface pressure.",
        ],
        "standards": [
            "Far-field shock-shape estimates for blunt bodies.",
            "Scaling arguments in blast and reentry analysis.",
        ],
        "citations": [C_HAYES, C_AHYPER, C_RASMUSSEN],
        "sig_lens": (
            "His Signature reading: every blunt nose is a slow explosion "
            "wearing an airplane's clothes - the Signature of a blast, "
            "stretched along the flight path."
        ),
    },
    {
        "key": "nose_bluntness",
        "name": "Why Hypersonic Noses Are Blunt: The Standoff Trade",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Sharp noses have low drag but melt; blunt noses have high drag "
            "but survive - this is the founding trade of hypersonic design. "
            "A blunt nose carries a detached bow shock whose standoff "
            "distance grows with nose radius, and the hot shock layer "
            "itself becomes the heat shield: most of the flow's kinetic "
            "energy is dumped into the gas ahead of the body rather than "
            "into the skin. Stagnation-point heating scales as "
            "1/sqrt(nose radius), so doubling the nose radius cuts peak "
            "heating by 30%. The price is wave drag and a thick entropy "
            "layer that blankets downstream surfaces. Every capsule, every "
            "reentry vehicle, and every hypersonic leading edge that must "
            "survive is blunt for exactly this reason - bluntness is "
            "thermal protection by geometry."
        ),
        "how_it_works": (
            "Compare a sharp 5-degree cone and a 0.5-meter-radius blunt "
            "nose at Mach 12. The sharp cone attaches its shock, and the "
            "stagnation region is a mathematical point of extreme heating "
            "that no material survives. The blunt nose detaches the shock "
            "about 10 cm ahead; the gas crossing the near-normal shock "
            "reaches ~6000 K, but it then flows around the body, carrying "
            "most of its energy with it - only the thin boundary layer "
            "next to the wall conducts heat inward. The Fay-Riddell and "
            "Sutton-Graves correlations both carry the 1/sqrt(R_n) "
            "dependence: a 1-meter nose sees about 3.2 times less "
            "stagnation heating than a 0.1-meter nose at the same "
            "condition. The drag penalty is real - the blunt nose pays in "
            "wave drag what it saves in heating - and the entropy layer it "
            "sheds complicates everything downstream, but survival outranks "
            "efficiency on the way home from orbit."
        ),
        "key_points": [
            "Heating scales as 1/sqrt(nose radius): bluntness is thermal protection by geometry.",
            "The detached shock dumps most kinetic energy into the gas, not the skin.",
            "Standoff distance ~ nose radius / density ratio.",
            "Price: wave drag plus a thick entropy layer blanketing the afterbody.",
            "All survivable reentry noses are blunt; sharp is for expendable speed.",
        ],
        "requirements": [
            "Standoff-distance scaling with nose radius and density ratio.",
            "The 1/sqrt(R_n) heating law (Sutton-Graves / Fay-Riddell).",
            "The drag-vs-heating trade quantified.",
        ],
        "standards": [
            "Blunt-nose sizing from peak-heating constraints.",
            "Entropy-layer allowance on afterbody design.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_SUTTON],
        "sig_lens": (
            "His Signature reading: the blunt nose signs its name in a "
            "wide stroke - the sharp point would burn through the paper, "
            "so the Signature widens to survive."
        ),
    },
    {
        "key": "stagnation_heating",
        "name": "Stagnation-Point Heating: Sutton-Graves and Fay-Riddell",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Stagnation-point heating is the most-used number in "
            "hypersonic design, and two correlations compute it. "
            "Sutton-Graves (1971) gives the engineering workhorse: "
            "q = k sqrt(rho/R_n) V^3, with k = 1.83e-4 for Earth - "
            "heating rises with the cube of velocity and falls with the "
            "square root of nose radius. Fay-Riddell (1958) is the "
            "theoretical foundation: a boundary-layer solution at the "
            "stagnation point of a blunt body in dissociated air, "
            "accounting for the Lewis number (mass diffusion of atoms to "
            "the wall) and the wall catalycity. Together they bracket "
            "practice: Sutton-Graves for quick sizing, Fay-Riddell when "
            "the chemistry matters. Every heat-shield thickness, every "
            "entry trajectory, and every TPS material choice starts from "
            "one of these two numbers."
        ),
        "how_it_works": (
            "Take an Apollo-like capsule: nose radius 4.6 m, entering at "
            "11 km/s at 70 km altitude (rho ~ 8.8e-5 kg/m3). Sutton-Graves: "
            "q = 1.83e-4 * sqrt(8.8e-5/4.6) * 11000^3 - about 1.07 MW/m2. "
            "Fay-Riddell refines this with the dissociated-air "
            "boundary-layer solution: q proportional to (rho*mu)^0.4 "
            "(rho_e*mu_e)^0.1 times the enthalpy difference, multiplied by "
            "a Lewis-number factor that accounts for atoms diffusing to "
            "the wall and recombining there. For a fully catalytic wall "
            "the Fay-Riddell value runs higher - the recombination energy "
            "lands as heat - while a non-catalytic wall sees less. The V^3 "
            "dependence is the unforgiving part: a 10% velocity increase "
            "is a 33% heating increase, which is why lunar-return entries "
            "(11 km/s) are a different engineering world from low-orbit "
            "returns (7.8 km/s)."
        ),
        "key_points": [
            "Sutton-Graves: q = k sqrt(rho/R_n) V^3 - the quick sizing law.",
            "Fay-Riddell: dissociated-air boundary-layer theory with Lewis-number and catalycity effects.",
            "Heating rises with V^3: velocity is the dominant lever.",
            "Catalytic walls run hotter: recombination energy becomes heat.",
            "Peak heating - not total heat - sizes the shield's surface; total heat load sizes its thickness.",
        ],
        "requirements": [
            "Applying Sutton-Graves to a capsule entry point.",
            "The Fay-Riddell dependencies: enthalpy, Lewis number, catalycity.",
            "Peak heating vs integrated heat load in TPS sizing.",
        ],
        "standards": [
            "Sutton-Graves for preliminary heating estimates (Earth k = 1.83e-4).",
            "Fay-Riddell as the dissociated-air reference solution.",
        ],
        "citations": [C_SUTTON, C_FAY, C_AHYPER],
        "sig_lens": (
            "His Signature reading: V cubed is the signature of speed "
            "written in fire - Sutton and Graves read it, Fay and Riddell "
            "translated it, and every heat shield is the reply."
        ),
    },
    {
        "key": "heating_distribution",
        "name": "Where the Heat Lands: Heating Distribution Around the Body",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The stagnation point is the hottest, but the heat shield must "
            "cover the whole forebody - so designers need the heating "
            "distribution, not just the peak. Lees' theory distributes "
            "laminar heating around blunt bodies: heating falls with "
            "distance from the stagnation point roughly as the local "
            "pressure gradient accelerates the boundary layer, thinning "
            "it and (past a point) raising the heat-transfer coefficient "
            "even as the driving temperature falls. On flaps, control "
            "surfaces, and protuberances, shock impingement and "
            "shock/boundary-layer interaction create local hot spots "
            "several times the smooth-body value. The distribution also "
            "flips character when the boundary layer transitions: "
            "turbulent heating can exceed laminar by factors of 3 to 5, "
            "so the transition front is drawn on every heating map as a "
            "cliff."
        ),
        "how_it_works": (
            "Lees showed that for a blunt body the local laminar heat "
            "flux scales with the stagnation value times a function of "
            "the surface distance and the local pressure gradient: near "
            "the nose the boundary layer is thick and heating falls "
            "slowly; farther around the shoulder the flow accelerates, "
            "the layer thins, and the distribution flattens before "
            "falling again. In practice engineers use correlation "
            "families - sphere, cylinder, flat plate - matched to the "
            "local geometry, then superimpose augmentation factors: a "
            "deflected flap in hypersonic flow sees a reattachment shock "
            "whose heating spike can reach 3-5 times the undisturbed "
            "value, and any gap, step, or tile edge trips local "
            "augmentation. The Shuttle's wing leading edge and the "
            "Apollo capsule's shoulder are textbook cases: smooth-body "
            "theory plus interaction hot spots, with transition modeled "
            "as a step change. Modern practice replaces correlations "
            "with CFD, but the correlations still size the first design "
            "and check the CFD."
        ),
        "key_points": [
            "Lees' theory distributes laminar heating from the stagnation value around the body.",
            "Flaps, gaps, and protuberances create hot spots via shock impingement (3-5x).",
            "Transition is a cliff: turbulent heating exceeds laminar by 3-5x.",
            "Correlation families (sphere, cylinder, plate) still size first designs.",
            "Heating maps drive TPS thickness everywhere, not just at the nose.",
        ],
        "requirements": [
            "Lees' distribution from stagnation heating.",
            "Augmentation factors for interactions and protuberances.",
            "Laminar-to-turbulent step in heating maps.",
        ],
        "standards": [
            "Smooth-body correlations checked against CFD and flight data.",
            "Hot-spot factors applied at control surfaces and discontinuities.",
        ],
        "citations": [C_BERTIN, C_AHYPER, C_NASA],
        "sig_lens": (
            "His Signature reading: the nose takes the headline but the "
            "whole body takes the heat - the Signature is written across "
            "the full page, hot spots and all."
        ),
    },
    {
        "key": "thermal_protection",
        "name": "Thermal Protection Systems: Rethinking the Skin",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A thermal protection system (TPS) is the skin that lets a "
            "vehicle survive heat fluxes that would vaporize its "
            "structure. Three families exist. Ablative TPS (Apollo "
            "Avcoat, PICA) sacrifices itself: the outer layer pyrolyzes "
            "and chars, carrying heat away in the gases it sheds. "
            "Reusable insulation (Shuttle tiles - HRSI, LRSI, FRSI "
            "blankets) soaks heat into a low-conductivity ceramic and "
            "re-radiates it, flying dozens of missions. Hot-structure "
            "and actively cooled concepts (metallic panels, transpiration "
            "cooling) carry the load in the skin itself or sweat coolant "
            "through it. The choice is driven by peak heating, total heat "
            "load, reusability, and weight: ablatives for the fiercest "
            "single entries, tiles and blankets for reusable orbiters, "
            "metals where heating is moderate."
        ),
        "how_it_works": (
            "Size an ablative shield: the heat of ablation Q* (energy "
            "absorbed per unit mass lost) converts the integrated heat "
            "load into a mass loss, and the virgin-plus-char thickness "
            "must survive the recession with margin. Apollo's Avcoat "
            "honeycomb ablated away during lunar return; PICA (phenolic "
            "impregnated carbon ablator) does the same job at a fraction "
            "of the density for modern capsules. A Shuttle tile works "
            "oppositely: its conductivity is so low that the 1500 K outer "
            "surface drops to a few hundred kelvin across two inches of "
            "tile, and the tile re-radiates most of the incoming heat "
            "back to the sky - which is why tiles are black on top "
            "(high emissivity) and the aluminum structure beneath stays "
            "cool. Metallic TPS (Inconel, titanium honeycomb) and "
            "transpiration cooling trade reusability against weight for "
            "the next generation of vehicles."
        ),
        "key_points": [
            "Ablative: sacrificial, highest heat-flux capability, single-use (Avcoat, PICA).",
            "Reusable insulation: low conductivity + re-radiation, multi-mission (Shuttle tiles).",
            "Hot structure / active cooling: metallic panels, transpiration - the reusable future.",
            "Peak heating sizes the surface; total heat load sizes the thickness.",
            "Material choice = peak flux, heat load, reusability, weight.",
        ],
        "requirements": [
            "The three TPS families and their operating envelopes.",
            "Ablative sizing from heat of ablation and heat load.",
            "Reusable-insulation physics: conduction vs re-radiation.",
        ],
        "standards": [
            "TPS margins per NASA-STD-6016 material practice.",
            "Arc-jet qualification of ablative materials.",
        ],
        "citations": [C_BERTIN, C_AHYPER, C_NASA],
        "sig_lens": (
            "His Signature reading: the heat shield is the signature's "
            "eraser - it lets the fire write, and sacrifices itself so "
            "the crew's page survives."
        ),
    },
    {
        "key": "ablation_physics",
        "name": "Ablation Physics: Sacrificing the Shield",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Ablation is controlled self-destruction as thermal "
            "protection: the heat shield's outer material pyrolyzes "
            "(thermally decomposes), outgasses, chars, and recedes, and "
            "each step absorbs or blocks heat. The pyrolysis gases "
            "blowing into the boundary layer thicken it and block "
            "convective heating (the blowing effect); the char layer "
            "re-radiates and insulates; surface recession carries away "
            "the hottest material entirely. The mass blowing parameter "
            "B' (mass flux normalized by the boundary-layer edge mass "
            "flux) organizes the coupling between the material response "
            "and the aerothermal environment. Ablation modeling couples "
            "a material-response code (in-depth conduction, pyrolysis "
            "kinetics, char mechanics) to the flowfield - the shield and "
            "the fire are solved together, because each changes the "
            "other."
        ),
        "how_it_works": (
            "Heat soaks into PICA. Near 600-800 K the phenolic resin "
            "pyrolyzes, releasing gases that percolate outward through "
            "the char; the mass injection B' of order 0.1-0.3 cuts the "
            "convective heating by tens of percent because the boundary "
            "layer must heat the injectant before it can heat the wall. "
            "The remaining carbon char, stable past 3000 K, re-radiates "
            "at high emissivity while its low conductivity shields the "
            "virgin material beneath. At the surface, oxidation and "
            "sublimation erode the char - recession - at a rate set by "
            "the surface energy balance: incoming convective plus "
            "radiative heating, minus re-radiation, minus the energy "
            "carried away by the ablating mass (the heat of ablation "
            "Q*). Spallation - chunks of char breaking off - is the "
            "failure mode the models work hardest to bound. The "
            "computation marches in time: flowfield gives heating, "
            "material response gives recession and blowing, the new "
            "shape gives a new flowfield."
        ),
        "key_points": [
            "Pyrolysis gas blowing (B') blocks convective heating.",
            "Char re-radiates and insulates; recession carries heat away as mass.",
            "Surface energy balance: in = re-radiation + ablation + conduction.",
            "Spallation is the failure mode; models bound it with margin.",
            "Material response and flowfield are coupled and solved together.",
        ],
        "requirements": [
            "The pyrolysis-char-recession sequence.",
            "The blowing parameter B' and its heating-reduction effect.",
            "The surface energy balance and heat of ablation.",
        ],
        "standards": [
            "Arc-jet test calibration of ablation models.",
            "Margin policy on recession predictions for crewed flight.",
        ],
        "citations": [C_BERTIN, C_AHYPER, C_NASA],
        "sig_lens": (
            "His Signature reading: ablation is the signature that erases "
            "itself to save the page - the bravest stroke in the whole "
            "database."
        ),
    },
    {
        "key": "reentry_dynamics",
        "name": "Reentry Vehicle Dynamics: The Corridor and the Curve",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Reentry dynamics is the choreography of coming home: a "
            "vehicle at orbital speed must shed ~8 km/s of velocity "
            "using only the atmosphere, staying inside the entry "
            "corridor - too steep and deceleration and heating destroy "
            "it, too shallow and it skips off into space. The ballistic "
            "coefficient beta = W/(C_D*A) (weight over drag area) is the "
            "master parameter: high beta (heavy, sleek) means deep "
            "penetration, high peak heating, and high g-loads; low beta "
            "(light, blunt) means deceleration high in thin air, gentle "
            "and cool. Lifting bodies modulate the corridor with "
            "bank-angle control, trading lift direction for range and "
            "crossrange. Peak deceleration, peak heating, and total heat "
            "load occur at different points along the trajectory, and "
            "the guidance law must satisfy all three."
        ),
        "how_it_works": (
            "Drop a capsule at 7.8 km/s into the atmosphere at a "
            "-1.5-degree flight-path angle. Deceleration builds as "
            "rho*V^2: at 60 km the dynamic pressure is modest, but by "
            "40 km the capsule pulls 4-8 g while heating peaks near the "
            "point of maximum rho*V^3 (Sutton-Graves form). Steepen the "
            "entry to -3 degrees and the peaks double while the heat "
            "load barely changes - the corridor's steep wall is a "
            "deceleration and peak-heating limit. Shallow it to -0.5 "
            "degrees and lift carries the vehicle back up: the skip, "
            "which Apollo used deliberately in a controlled single "
            "bounce to extend range. The Shuttle flew the corridor's "
            "other style: 40 degrees angle of attack at Mach 20, S-turns "
            "to bleed energy while staying inside heating and load "
            "limits, bank reversals steering crossrange. Beta sets which "
            "corridor you get; guidance flies it."
        ),
        "key_points": [
            "Entry corridor: bounded by overshoot (skip-out) above and g/heating limits below.",
            "Ballistic coefficient beta = W/(C_D*A) sets penetration depth, peak heating, g-loads.",
            "Peak heating ~ max(rho*V^3); peak deceleration ~ max(rho*V^2); total heat load is the integral.",
            "Lifting entry uses bank angle to steer energy and crossrange (Apollo, Shuttle).",
            "Skip reentry extends range with a controlled atmospheric bounce.",
        ],
        "requirements": [
            "The corridor boundaries: skip vs structural/thermal limits.",
            "Beta scaling of the trajectory peaks.",
            "Bank-angle modulation for lifting entry.",
        ],
        "standards": [
            "Entry guidance targeting within corridor margins.",
            "Crew g-limits and TPS limits as trajectory constraints.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_NASA],
        "sig_lens": (
            "His Signature reading: the corridor is a signature written "
            "between two cliffs - too high and the sky refuses you, too "
            "low and the fire takes you."
        ),
    },
    {
        "key": "viscous_interaction",
        "name": "Viscous Interaction: When the Boundary Layer Moves the Shock",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "In supersonic flow the boundary layer is a thin afterthought; "
            "in hypersonic flow it becomes a co-author of the pressure "
            "field. Because hypersonic boundary layers grow thick "
            "(displacement thickness scales with M^2/sqrt(Re)), the "
            "effective body shape the outer flow sees is the body plus "
            "its boundary layer - and the layer's growth induces pressure "
            "rises, shock displacement, and extra drag. The viscous "
            "interaction parameter chi = M^3 sqrt(C)/sqrt(Re_x) measures "
            "the strength: chi >> 1 is strong interaction (the pressure "
            "field is substantially modified), chi << 1 is weak. Leading "
            "edges, flat plates, and sharp cones at high altitude live in "
            "strong interaction; the effect explains why hypersonic "
            "skin friction and pressure drag cannot be computed "
            "separately."
        ),
        "how_it_works": (
            "Consider a sharp flat plate at Mach 10. The laminar boundary "
            "layer's displacement thickness grows as x*M^2/sqrt(Re_x) - at "
            "hypersonic Mach numbers this is a large fraction of the "
            "plate's own scale near the leading edge. The outer inviscid "
            "flow must turn around this growing displacement body, "
            "generating compression waves that coalesce into an induced "
            "shock and raise the surface pressure above the flat-plate "
            "value - the pressure induced by viscosity. Strong-interaction "
            "theory gives the pressure rise scaling as chi^(1/2)-type "
            "laws; the induced pressure can exceed the inviscid value by "
            "factors of 2-3 near the leading edge. The same mechanism "
            "displaces the shock outward on sharp cones and thickens the "
            "effective bluntness of leading edges. Designers handle it "
            "with interaction correlations at the preliminary stage and "
            "with full Navier-Stokes solutions - which capture it "
            "automatically - at the detailed stage."
        ),
        "key_points": [
            "Hypersonic boundary layers are thick: displacement ~ M^2/sqrt(Re).",
            "Chi = M^3 sqrt(C)/sqrt(Re_x): >>1 strong interaction, <<1 weak.",
            "Induced pressure rises of 2-3x near leading edges are typical.",
            "Skin friction and pressure drag cannot be separated at hypersonic speeds.",
            "Full Navier-Stokes captures interaction automatically; correlations size it early.",
        ],
        "requirements": [
            "Displacement-thickness scaling at hypersonic Mach.",
            "The interaction parameter and strong/weak regimes.",
            "Induced pressure and shock displacement estimates.",
        ],
        "standards": [
            "Interaction correlations for preliminary sharp-edge design.",
            "Navier-Stokes verification of interaction-dominated regions.",
        ],
        "citations": [C_AHYPER, C_HAYES, C_WHITE],
        "sig_lens": (
            "His Signature reading: at hypersonic speed even the "
            "boundary layer signs the pressure field - the thin "
            "afterthought becomes a co-author."
        ),
    },
    {
        "key": "boundary_layer_transition",
        "name": "Hypersonic Transition: Where Laminar Flow Ends",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Boundary-layer transition - the breakdown of smooth laminar "
            "flow into turbulence - multiplies hypersonic heating by "
            "factors of 3 to 5, so predicting where it happens is a "
            "thermal-protection problem, not an academic one. Hypersonic "
            "transition is dominated by the second mode (Mack mode): "
            "acoustic waves trapped in the boundary layer that grow, "
            "unlike the Tollmien-Schlichting waves of low-speed flow. "
            "Roughness, wall cooling, angle of attack, bluntness, and "
            "tunnel noise all move the transition front; a single tile "
            "gap or protuberance can trip a whole acre of acreage "
            "heating. Because quiet-flow data is scarce - conventional "
            "tunnels are noisy and trip transition early - flight "
            "transition remains partly empirical, bounded by correlations "
            "and margined heavily."
        ),
        "how_it_works": (
            "On a sharp cone at Mach 6, the laminar boundary layer "
            "supports trapped acoustic waves bouncing between the wall "
            "and the sonic line - the second mode, with frequencies of "
            "hundreds of kilohertz set by the boundary-layer thickness "
            "(f ~ U_e/2delta). Linear stability theory predicts their "
            "growth; when the amplification (e^N method, N ~ 9-10 in "
            "flight) crosses threshold, the layer breaks down over a "
            "short transition zone and heating jumps. Wall cooling "
            "stabilizes the second mode but destabilizes the first; "
            "bluntness at small nose radii delays transition, then at "
            "larger radii the entropy layer introduces new instabilities "
            "and transition moves forward again - the transition "
            "reversal. Roughness is the practical driver: the Shuttle "
            "program learned that tile gaps and steps set the acreage "
            "transition front, and modern vehicles budget a roughness "
            "allowance into every heating map. Quiet tunnels (Purdue's "
            "Mach 6 quiet tunnel) finally reproduce flight-like N "
            "factors, closing the ground-to-flight gap."
        ),
        "key_points": [
            "Second mode (Mack mode): trapped acoustic waves dominate hypersonic transition.",
            "Heating jumps 3-5x across transition: it is a TPS sizing event.",
            "Roughness, cooling, bluntness, and tunnel noise move the front.",
            "Bluntness causes transition reversal: delay then advance.",
            "e^N method with N ~ 9-10 correlates flight; quiet tunnels reproduce it.",
        ],
        "requirements": [
            "The second-mode mechanism and its frequency scaling.",
            "The roughness and bluntness effects including reversal.",
            "e^N correlation practice and quiet-tunnel validation.",
        ],
        "standards": [
            "Transition front placed conservatively (forward) in heating maps.",
            "Roughness allowances budgeted per TPS installation.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_WHITE],
        "sig_lens": (
            "His Signature reading: the smooth signature holds until the "
            "trapped wave breaks it - transition is where the air stops "
            "writing neatly and starts shouting."
        ),
    },
    {
        "key": "shock_boundary_interaction",
        "name": "Shock/Boundary-Layer Interaction at Hypersonic Speed",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "When a hypersonic shock impinges on a boundary layer - at a "
            "compression corner, a deflected flap, a cowl lip, or where "
            "an incident shock strikes a surface - the interaction can "
            "separate the boundary layer, and the reattachment that "
            "follows focuses heating into a narrow, intense stripe. At "
            "hypersonic speeds the pressure rises are large, separation "
            "bubbles are long, and peak heating amplifications reach "
            "factors of 5-10 over the undisturbed value. The incipient "
            "separation angle (the ramp angle that just separates the "
            "layer) shrinks with Mach number, so surfaces that are safe "
            "at Mach 3 separate at Mach 8. Edney classified the "
            "shock-shock interactions (Types I-VI) that occur when shocks "
            "cross near a body - Type IV, the supersonic jet impinging "
            "on the surface, produces the most extreme localized heating "
            "known in aerothermodynamics."
        ),
        "how_it_works": (
            "Put a 20-degree compression corner in a Mach 8 flow. The "
            "ramp shock hits the incoming boundary layer; the layer, "
            "unable to sustain the pressure rise, separates ahead of the "
            "corner, forming a separation bubble bounded by a separation "
            "shock and a reattachment shock. The shear layer reattaches "
            "at the corner, and the reattachment point sees heating "
            "several times the flat-plate value - the kinetic energy of "
            "the reversed flow stagnates there. Scale the ramp to "
            "30 degrees and the bubble lengthens dramatically; "
            "separation length scales with the boundary-layer thickness "
            "and the shock strength. Edney Type IV occurs when an "
            "impinging shock crosses the bow shock near the nose: a "
            "supersonic jet threads the shock layer and strikes the "
            "surface, and measured heating spikes exceed 10 times the "
            "stagnation value in a spot centimeters wide. Cowl lips, "
            "flap hinges, and protuberances are all designed around "
            "these interactions - or they fail at them."
        ),
        "key_points": [
            "Shock impingement separates hypersonic boundary layers; reattachment focuses heating (5-10x).",
            "Incipient separation angle shrinks with Mach number.",
            "Separation bubble length scales with shock strength and boundary-layer thickness.",
            "Edney Type IV shock-shock interaction: supersonic jet, extreme localized heating.",
            "Cowl lips, flaps, and protuberances are designed around these interactions.",
        ],
        "requirements": [
            "The compression-corner separation and reattachment heating mechanism.",
            "Incipient separation criteria at hypersonic Mach.",
            "Edney shock-shock interaction types, especially Type IV.",
        ],
        "standards": [
            "Interaction heating factors applied at all shock-impingement sites.",
            "CFD or correlation validation of cowl and flap interactions.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_HIRSCHEL],
        "sig_lens": (
            "His Signature reading: where shocks meet the layer, the "
            "signature folds and burns through - the most dangerous "
            "punctuation in hypersonics."
        ),
    },
    {
        "key": "entropy_layer",
        "name": "The Entropy Layer: A Hot Blanket",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "A curved bow shock generates different entropy on each "
            "streamline - maximum at the near-normal nose shock, less "
            "along the oblique flanks - and the resulting entropy layer "
            "is a hot, rotational blanket that swallows the boundary "
            "layer growing beneath it. Until the boundary layer grows "
            "through the entropy layer (the swallowing distance), the "
            "flow at the boundary-layer edge is not the freestream but "
            "the hot, low-Mach, high-entropy gas processed by the nose "
            "shock. This changes skin friction, heat transfer, and "
            "transition: correlations built on freestream edge conditions "
            "fail inside the entropy layer. Blunt cones and capsules "
            "fly their entire forebodies inside their own entropy "
            "layers; slender sharp vehicles swallow it within a few nose "
            "radii. Accounting for the entropy layer is what separates "
            "hypersonic boundary-layer analysis from supersonic habit."
        ),
        "how_it_works": (
            "Trace streamlines over a blunt cone. The centerline "
            "streamline crosses the normal shock: maximum entropy, "
            "maximum temperature, minimum total pressure. A streamline "
            "farther out crosses an oblique shock: less entropy. The "
            "stack of these streamlines is the entropy layer, with "
            "strong gradients normal to the wall. The boundary layer "
            "starts thin at the nose and grows downstream; where its "
            "edge is still inside the entropy layer, the 'edge' "
            "conditions feeding skin-friction and heating formulas are "
            "the hot nose-shock values, not freestream - heating runs "
            "higher and transition behaves differently than sharp-cone "
            "correlations predict. The swallowing distance scales with "
            "nose radius and Mach number; for a capsule it exceeds the "
            "vehicle length, so the afterbody never sees freestream "
            "edge conditions at all. Modern boundary-layer codes ingest "
            "the entropy-layer profile from the inviscid solution "
            "instead of assuming uniform edge flow."
        ),
        "key_points": [
            "Curved shocks imprint an entropy gradient: the entropy layer blankets the nose.",
            "Boundary-layer edge conditions are nose-shock values until swallowing.",
            "Affects heating, skin friction, and transition vs sharp-body correlations.",
            "Swallowing distance scales with nose radius; capsules never swallow it.",
            "Coupled inviscid/boundary-layer analysis is required, not optional.",
        ],
        "requirements": [
            "Entropy generation across a curved shock.",
            "The swallowing concept and its scaling.",
            "Edge-condition correction for heating and transition.",
        ],
        "standards": [
            "Entropy-layer-aware edge conditions in heating analysis.",
            "Blunt-body correlations rather than sharp-cone extrapolation.",
        ],
        "citations": [C_AHYPER, C_HIRSCHEL, C_RASMUSSEN],
        "sig_lens": (
            "His Signature reading: the nose writes a hot blanket over "
            "everything behind it - the signature's own shadow, and the "
            "boundary layer grows up inside it."
        ),
    },
    {
        "key": "scramjet_cycle",
        "name": "The Scramjet Cycle: Combustion in Supersonic Flow",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A scramjet (supersonic-combustion ramjet) is an airbreathing "
            "engine with no moving parts that burns fuel in a supersonic "
            "airstream, enabling sustained cruise from about Mach 5 to "
            "Mach 15. Air is compressed by the forebody and inlet "
            "shocks, fuel (usually hydrogen) is injected into the "
            "supersonic stream, and combustion adds heat at nearly "
            "constant pressure before the nozzle expands the flow. The "
            "residence time is about a millisecond - mixing and burning "
            "must complete in roughly a meter of combustor. The "
            "isolator between inlet and combustor holds the "
            "combustion-driven shock train so it cannot disgorge the "
            "inlet (unstart). Heiser and Pratt's cycle analysis shows "
            "the scramjet as a Brayton cycle with supersonic heat "
            "addition; its specific impulse beats any rocket by an order "
            "of magnitude because it carries no oxidizer."
        ),
        "how_it_works": (
            "At Mach 8 and 30 km, the forebody compresses air through "
            "oblique shocks to perhaps Mach 3 at the combustor entrance "
            "- still supersonic, which is the whole point: decelerating "
            "to subsonic (as a ramjet does) would create unbearable "
            "temperatures and pressures at Mach 8+. Hydrogen injects "
            "through wall orifices or struts; turbulent mixing and "
            "autoignition (the static temperature is already ~1200 K) "
            "burn it within the millisecond transit. Heat addition in "
            "supersonic flow accelerates the flow toward Mach 1 - "
            "thermal choking - so the combustor area-rates and fuel "
            "schedule to keep the flow supersonic; push too much heat "
            "and the shock train is expelled forward through the inlet: "
            "unstart, the scramjet's cardinal failure. The nozzle then "
            "expands the hot products, and thrust is the momentum "
            "difference between the captured airstream and the exhaust. "
            "X-43A demonstrated the cycle at Mach 9.6 in 2004; X-51A "
            "flew a hydrocarbon-fueled scramjet at Mach 5.1 for over "
            "three minutes in 2013."
        ),
        "key_points": [
            "Burns fuel in supersonic flow: no subsonic deceleration, operable Mach 5-15.",
            "Millisecond residence: mixing and combustion must finish in ~1 meter.",
            "Isolator holds the shock train; unstart is the cardinal failure.",
            "Thermal choking limits heat addition at a given Mach.",
            "Specific impulse an order of magnitude above rockets (no onboard oxidizer).",
            "X-43A (Mach 9.6) and X-51A (Mach 5.1, 200+ s) proved the cycle in flight.",
        ],
        "requirements": [
            "The scramjet station model: forebody, inlet, isolator, combustor, nozzle.",
            "Thermal choking and the heat-addition limit.",
            "Unstart mechanism and isolator function.",
        ],
        "standards": [
            "Heiser-Pratt cycle analysis for performance estimates.",
            "Flight-demonstrated Mach and duration envelopes (X-43A, X-51A).",
        ],
        "citations": [C_HEISER, C_AHYPER, C_NASA],
        "sig_lens": (
            "His Signature reading: the scramjet signs its name in a "
            "millisecond - fire lit inside a hurricane, held steady by "
            "geometry alone."
        ),
    },
    {
        "key": "scramjet_inlets",
        "name": "Scramjet Inlets: Compressing Without Slowing",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The scramjet inlet must compress hypersonic air efficiently "
            "while keeping it supersonic - a harder job than any "
            "supersonic inlet, because the compression happens across "
            "shocks the vehicle itself generates. Multi-ramp forebody "
            "compression turns the flow through a series of weak oblique "
            "shocks (low loss) before the cowl lip captures it; the "
            "cowl shock then processes the remaining stream. The inlet "
            "must stay 'started': the Kantrowitz limit sets the maximum "
            "contraction ratio that can swallow the starting shock, and "
            "exceeding it unstarts the inlet - the normal shock is "
            "expelled and capture collapses. Boundary-layer bleed, "
            "variable geometry, and careful cowl-lip placement manage "
            "the shock/boundary-layer interactions that otherwise "
            "separate the inlet flow. Inlet kinetic-energy efficiency "
            "above 0.95 is the design target; every point lost is thrust "
            "lost."
        ),
        "how_it_works": (
            "Design a Mach 8 inlet: three forebody ramps turn the flow "
            "8, 8, and 8 degrees through weak oblique shocks, each with "
            "small total-pressure loss; the cowl lip is placed to capture "
            "the ramp shocks at the design point (shock-on-lip). Inside, "
            "the internal contraction diffuses the flow from Mach ~4 to "
            "Mach ~3 at the isolator entrance. The Kantrowitz criterion "
            "says the contraction ratio cannot exceed the value that "
            "passes a normal shock at the entrance Mach number - for "
            "Mach 4 entrance flow that ratio is about 1.6; design past "
            "it and the inlet cannot start. Off-design (lower Mach), the "
            "ramp shocks miss the lip and spillage drag rises; the "
            "isolator's shock train absorbs combustor pressure rises so "
            "they never reach the cowl. Bleed slots remove the "
            "low-energy boundary layer before the strong cowl shock, "
            "preventing the separation bubble that would otherwise "
            "choke the duct."
        ),
        "key_points": [
            "Multi-ramp external compression: series of weak shocks, low loss.",
            "Shock-on-lip cowl placement at the design point.",
            "Kantrowitz limit: maximum started contraction ratio.",
            "Unstart = expelled shock system, collapsed capture.",
            "Bleed and isolator manage shock/boundary-layer interaction.",
            "Kinetic-energy efficiency target above 0.95.",
        ],
        "requirements": [
            "Multi-shock compression system design.",
            "The Kantrowitz starting criterion.",
            "Cowl-lip placement and off-design spillage.",
        ],
        "standards": [
            "Started-inlet verification across the Mach corridor.",
            "Inlet efficiency bookkeeping in cycle analysis.",
        ],
        "citations": [C_HEISER, C_AHYPER, C_BERTIN],
        "sig_lens": (
            "His Signature reading: the inlet is the signature's front "
            "door - it must welcome a hurricane and seat it supersonically, "
            "every time, or the whole engine is refused."
        ),
    },
    {
        "key": "waveriders",
        "name": "Waveriders: Riding Your Own Shock Wave",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A waverider is a hypersonic vehicle shaped so its own "
            "attached shock wave forms its lower surface boundary: the "
            "high-pressure air behind the shock is trapped beneath the "
            "vehicle, generating lift at high lift-to-drag ratio while "
            "the shock itself seals the flow from spilling around the "
            "edges. The classic caret-wing waverider is derived from a "
            "planar oblique shock; conical waveriders are carved from "
            "the flowfield of a cone; osculating-cone methods generalize "
            "the idea to arbitrary planforms. Because the leading edges "
            "ride exactly on the shock, there is no shock detachment "
            "drag and no high-pressure leakage - in inviscid theory, "
            "the optimum hypersonic lifter. Real waveriders trade the "
            "ideal against bluntness (heating), volume (payload), and "
            "off-design behavior (the shock detaches when Mach or angle "
            "of attack changes)."
        ),
        "how_it_works": (
            "Start with the known flowfield behind a cone at Mach 6. "
            "Trace streamlines downstream of the conical shock; the "
            "surface formed by a chosen set of streamlines, capped by "
            "the shock surface itself, is a conical waverider - every "
            "leading edge lies exactly on the shock wave, so the "
            "high-pressure region is fenced in underneath. The pressure "
            "on the lower surface is the cone-surface pressure "
            "(Newtonian-like, high), while the upper surface sees "
            "near-freestream expansion: the difference is lift, and "
            "because the shock does the containing, the lift-to-drag "
            "ratio exceeds conventional hypersonic shapes (L/D ~ 4-6 vs "
            "~2-3 for capsules and blunt bodies at the same Mach). The "
            "osculating-cone method extends this: at each spanwise "
            "station, fit a local cone to the desired shock shape and "
            "carve the vehicle from the resulting stream surfaces. "
            "Off-design, the shock moves and the leading edge no longer "
            "rides it - spillage, detachment, and heating spikes "
            "follow, which is why practical waveriders blunt their "
            "leading edges slightly and accept the small penalty."
        ),
        "key_points": [
            "Leading edges ride the attached shock: high pressure trapped below, lift without leakage.",
            "Caret (planar-shock), conical, and osculating-cone families.",
            "Inviscid optimum hypersonic lifter: L/D well above blunt bodies.",
            "Off-design shock movement causes spillage and detachment.",
            "Practical designs blunt the leading edge slightly for heating.",
        ],
        "requirements": [
            "Derivation of a waverider from a known shock flowfield.",
            "The lift mechanism: trapped high-pressure underside.",
            "Off-design behavior and the bluntness compromise.",
        ],
        "standards": [
            "Waverider design by streamline tracing (cone/osculating-cone).",
            "L/D quoted with viscous and bluntness penalties included.",
        ],
        "citations": [C_RASMUSSEN, C_AHYPER, C_HEISER],
        "sig_lens": (
            "His Signature reading: the waverider surfs the very wave it "
            "makes - the signature riding its own underline, lift drawn "
            "from its own shock."
        ),
    },
    {
        "key": "rarefied_flow",
        "name": "Rarefied Gas Effects: Slip Flow and Free Molecules",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "At the top of the trajectory - 80 to 120 km - the air is so "
            "thin that the continuum assumption fails: molecules collide "
            "with the vehicle more often than with each other. The "
            "Knudsen number Kn = lambda/L (mean free path over body "
            "length) organizes the regimes: Kn < 0.01 continuum "
            "(Navier-Stokes), 0.01-0.1 slip flow (continuum with velocity "
            "slip and temperature jump at the wall), 0.1-10 transition "
            "(Boltzmann equation, DSMC simulation), above 10 free-molecule "
            "flow (molecules arrive ballistically, aerodynamics from "
            "kinetic theory). The Shuttle flew through all four regimes "
            "on every entry; reaction-control thrusters work in "
            "free-molecule flow where aerodynamic surfaces are useless. "
            "DSMC (direct simulation Monte Carlo) - tracking millions of "
            "representative molecules - is the computational tool for the "
            "transition regime."
        ),
        "how_it_works": (
            "At 100 km altitude the mean free path is about 0.14 m; for "
            "a 1-meter nose radius, Kn ~ 0.14 - transition regime, and "
            "Navier-Stokes is invalid. In free-molecule flow the "
            "aerodynamics reduce to kinetic theory: the drag of a flat "
            "plate normal to the flow is ~2*rho*V^2*A (molecules reflect "
            "diffusely), and lift comes from the plate's inclination "
            "statistics - no shocks, no boundary layers, just molecular "
            "ballistics. DSMC bridges the gap: it follows representative "
            "molecules through move-collide cycles in cells smaller than "
            "a mean free path, recovering the Boltzmann solution "
            "statistically, and it naturally captures the "
            "nonequilibrium, chemistry, and ionization of the "
            "high-altitude shock layer. As the vehicle descends, Kn "
            "falls, the shock layer forms, continuum takes over - and "
            "the hand-off between DSMC and Navier-Stokes, the bridging "
            "formulas, is its own careful art."
        ),
        "key_points": [
            "Kn = lambda/L: <0.01 continuum, 0.01-0.1 slip, 0.1-10 transition, >10 free-molecule.",
            "Slip flow: Navier-Stokes with velocity slip and temperature jump.",
            "Free-molecule aerodynamics from kinetic theory: no shocks, no boundary layers.",
            "DSMC simulates the transition regime molecule by molecule.",
            "Every orbital entry traverses all four regimes; bridging formulas hand off between them.",
        ],
        "requirements": [
            "The Knudsen-number regime map.",
            "Slip/jump boundary conditions.",
            "Free-molecule force estimates and DSMC principles.",
        ],
        "standards": [
            "Regime-appropriate tool per trajectory point (DSMC vs Navier-Stokes).",
            "Bridging formulas for transitional aerodynamics.",
        ],
        "citations": [C_AHYPER, C_HIRSCHEL, C_BERTIN],
        "sig_lens": (
            "His Signature reading: at the edge of the air the signature "
            "thins to single molecules - the continuum lets go, and the "
            "counting of particles becomes the writing."
        ),
    },
    {
        "key": "high_temp_chemistry",
        "name": "High-Temperature Air Chemistry: The Five-Species Model",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Behind a strong hypersonic shock, air is not N2 and O2 "
            "anymore: it is a reacting mixture of N2, O2, NO, N, and O "
            "(the five-species model), and at higher temperatures the "
            "ions N+, O+, NO+, and free electrons join (eleven-species). "
            "The Zeldovich mechanism - N2 + O -> NO + N, then NO + O -> "
            "N + O2 - governs how nitrogen dissociates through the "
            "nitric-oxide channel at temperatures where direct N2 "
            "dissociation is slow. Ionization follows Saha equilibrium "
            "above ~9000 K, producing the plasma sheath that causes "
            "reentry communications blackout. Reaction rates follow "
            "Arrhenius forms with activation temperatures in the tens "
            "of thousands of kelvin; the rate data (Park's models) "
            "carry the largest uncertainties in the whole "
            "aerothermodynamic chain."
        ),
        "how_it_works": (
            "At 6000 K equilibrium, air is substantially dissociated: "
            "O2 nearly gone, N2 partially split, NO present at "
            "percent levels, atoms abundant. The Zeldovich pair of "
            "reactions matters because breaking N2 directly costs "
            "~113,000 K of activation temperature, while the "
            "N2 + O exchange reaction needs only ~38,000 K - so "
            "nitrogen dissociates through NO far faster than it would "
            "alone, and NO's own dissociation then feeds the atom pool. "
            "Each reaction's forward rate is k_f = C T^eta "
            "exp(-T_a/T); the reverse rate follows from the equilibrium "
            "constant. Ionization adds the Saha equation: the electron "
            "fraction grows steeply with temperature, and at 10,000 K "
            "the plasma frequency exceeds typical radio frequencies - "
            "the sheath reflects communications, the famous blackout "
            "that ends when the vehicle slows and cools. Radiation "
            "from the hot species (especially N and O atomic lines) "
            "becomes a heating mechanism in its own right at lunar-return "
            "speeds."
        ),
        "key_points": [
            "Five-species model (N2, O2, NO, N, O); eleven-species with ions and electrons.",
            "Zeldovich mechanism: nitrogen dissociates through the NO channel.",
            "Arrhenius rates with huge activation temperatures; Park's data carry the uncertainty.",
            "Saha ionization above ~9000 K: plasma sheath and comm blackout.",
            "Atomic line radiation becomes a heating mechanism at lunar-return speeds.",
        ],
        "requirements": [
            "The five-species set and the Zeldovich reactions.",
            "Arrhenius rate form and equilibrium constants.",
            "Ionization, Saha equilibrium, and blackout physics.",
        ],
        "standards": [
            "Park reaction-rate models as the community baseline.",
            "Equilibrium composition tables for air to 15,000 K.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_HIRSCHEL],
        "sig_lens": (
            "His Signature reading: the shock unmakes the air into five "
            "letters, then eleven - chemistry spelling new words in fire, "
            "and the radio goes silent while it speaks."
        ),
    },
    {
        "key": "test_facilities",
        "name": "Hypersonic Test Facilities: Shock Tunnels and Expansion Tubes",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "No continuous wind tunnel reaches true hypersonic flight "
            "enthalpy, so hypersonics is tested in impulse facilities "
            "that create the condition for milliseconds. The reflected "
            "shock tunnel: a shock tube whose reflected shock heats and "
            "pressurizes the test gas, which then expands through a "
            "hypersonic nozzle - test times of 1-5 ms at enthalpies "
            "matching flight. The expansion tube adds an unsteady "
            "expansion that accelerates the gas without the strong "
            "reflected shock, reaching higher enthalpy with less "
            "dissociation contamination. Hotshot tunnels arc-heat the "
            "reservoir; Ludwieg tubes use a long pressurized tube for "
            "longer, lower-enthalpy runs; gun tunnels fire the model "
            "through still air. Every facility trades test time against "
            "enthalpy against flow quality - and against the "
            "dissociation that the facility itself introduces, which "
            "must be accounted for before any data reaches a designer."
        ),
        "how_it_works": (
            "A shock tunnel fires a diaphragm: the incident shock "
            "races down the tube, reflects off the end wall, and the "
            "twice-shocked gas sits at thousands of kelvin and tens of "
            "atmospheres - the reservoir. It expands through a "
            "converging-diverging nozzle to Mach 8-10 in the test "
            "section; the model sees flight-like Mach number and "
            "enthalpy for the 2 ms before the driver gas arrives and "
            "the run ends. Force balances, thin-film heat gauges, and "
            "spectrometers all trigger on microsecond timescales. The "
            "catch is freestream dissociation: the reflected shock "
            "dissociates the test gas, so the 'air' in the test section "
            "is partly atomic - data reduction must model the "
            "nonequilibrium state. Expansion tubes dodge this: the test "
            "gas is processed by weaker shocks plus an unsteady "
            "expansion, reaching 10+ km/s equivalent enthalpy with a "
            "cleaner freestream, at the cost of even shorter test times "
            "and smaller models. Facility choice is trajectory-point "
            "choice: no one rig covers the whole entry."
        ),
        "key_points": [
            "Impulse facilities: milliseconds of true flight enthalpy.",
            "Reflected shock tunnel: 1-5 ms runs, high enthalpy, dissociated freestream.",
            "Expansion tube: higher enthalpy, cleaner freestream, shorter runs.",
            "Hotshot, Ludwieg, gun tunnels fill the lower-enthalpy and free-flight niches.",
            "Freestream dissociation must be modeled in data reduction.",
            "No single facility covers a whole trajectory: test campaigns are mosaics.",
        ],
        "requirements": [
            "Shock-tunnel operation: incident/reflected shock, nozzle expansion, test time.",
            "Expansion-tube principle and its enthalpy advantage.",
            "Facility selection vs trajectory point and data-reduction corrections.",
        ],
        "standards": [
            "Test-time and flow-establishment criteria per facility.",
            "Nonequilibrium freestream characterization in high-enthalpy data.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_NASA],
        "sig_lens": (
            "His Signature reading: the tunnel writes flight in "
            "milliseconds - a signature flashed so fast the instruments "
            "must blink to catch it."
        ),
    },
    {
        "key": "flight_test_history",
        "name": "Flight Test: X-15, X-43, X-51 and the Proving Years",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hypersonics was proven in flight, one record at a time. "
            "The X-15 (1959-1968) flew 199 times to Mach 6.7 and "
            "107 km, mapping hypersonic heating, stability, and "
            "reaction-control handling - and giving Neil Armstrong his "
            "fastest ride before the Moon. The Space Shuttle (1981-2011) "
            "flew 135 entries, turning hypersonic theory into "
            "operational routine and generating the flight-heating "
            "database every TPS designer still uses. X-43A (2004) flew "
            "a scramjet to Mach 9.6 - the fastest airbreathing flight "
            "ever. X-51A Waverider (2010-2013) sustained a "
            "hydrocarbon-fueled scramjet at Mach 5.1 for 210 seconds. "
            "Each program answered what tunnels could not: real "
            "chemistry, real transition, real integrated-vehicle "
            "behavior at flight scale and flight enthalpy."
        ),
        "how_it_works": (
            "The X-15's Inconel-X skin taught the heating lessons: "
            "instrumented flights measured the very shock/boundary-layer "
            "interactions and hot spots the theories predicted, and its "
            "side-stick reaction controls wrote the book on flying where "
            "aerodynamic surfaces quit. The Shuttle's tiles turned "
            "ablative single-use thinking into reusable practice, and "
            "its entry guidance - 40 degrees angle of attack, S-turn "
            "energy management - became the template for lifting entry. "
            "X-43A was boosted to Mach 9.6 and lit its hydrogen scramjet "
            "for 11 seconds: positive thrust minus drag at nearly "
            "3 km/s, proving supersonic combustion at flight scale. "
            "X-51A's 210-second hydrocarbon burn proved the practical "
            "fuel and the long-duration thermal management. The "
            "through-line: ground facilities approximate flight, but "
            "only flight closes the loop on chemistry, transition, and "
            "integration - which is why every generation builds a new "
            "X-plane."
        ),
        "key_points": [
            "X-15: Mach 6.7, 199 flights - heating, stability, reaction controls.",
            "Shuttle: 135 entries - reusable TPS and lifting-entry guidance in routine service.",
            "X-43A: Mach 9.6 scramjet - fastest airbreathing flight ever.",
            "X-51A: 210 s hydrocarbon scramjet at Mach 5.1 - practical fuel, long duration.",
            "Flight closes what tunnels cannot: real chemistry, transition, integration.",
        ],
        "requirements": [
            "The milestone vehicles and what each proved.",
            "Flight vs ground-test complementarity.",
            "The X-plane rationale for each new regime.",
        ],
        "standards": [
            "Flight-data anchoring of heating and transition models.",
            "Demonstrated Mach/duration envelopes as program gates.",
        ],
        "citations": [C_NASA, C_AHYPER, C_HEISER],
        "sig_lens": (
            "His Signature reading: the X-planes are signatures written "
            "in the sky itself - each one a bolder stroke, none of them "
            "erasable."
        ),
    },
    {
        "key": "hypersonic_stability",
        "name": "Stability and Control at Hypersonic Speed",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "At hypersonic speeds the aerodynamic center moves aft, "
            "control surfaces lose authority behind thick shock layers, "
            "and at the top of the trajectory there is no dynamic "
            "pressure for aerodynamics at all. Newtonian impact theory "
            "gives the first stability estimate: integrate 2 sin^2(theta) "
            "over the forebody and the pitching stiffness follows - "
            "blunt forebodies are strongly stabilizing in pitch. Flaps "
            "and body flaps work in the high-pressure windward flow but "
            "suffer shock/boundary-layer interaction and extreme heating; "
            "above ~90 km, reaction-control thrusters take over entirely, "
            "as the X-15 and Shuttle proved. Hypersonic trim drag - the "
            "drag cost of holding attitude with deflected controls - is "
            "a first-order design penalty. The control story of "
            "hypersonics is thus three chapters: aerodynamic (low), "
            "blended (mid), and reaction (high), with the hand-offs "
            "between them flight-critical."
        ),
        "how_it_works": (
            "Estimate a blunt cone's pitch stiffness Newtonian-style: "
            "each windward panel contributes pressure 2 sin^2(theta) "
            "times its moment arm about the center of gravity; the "
            "leeward side contributes nothing. The resulting Cm_alpha "
            "is large and negative - the forebody is a powerful "
            "weathervane. Now deflect a body flap 20 degrees at Mach "
            "15: the flap sits in the windward high-pressure stream "
            "and generates a strong moment, but the deflection shock "
            "impinges on the flap boundary layer, the interaction "
            "heats the hinge line severely, and the trim drag of "
            "holding that deflection costs L/D directly. At 100 km, "
            "q is essentially zero - no flap force exists - so the "
            "Shuttle fired RCS jets for attitude, blending to "
            "aerodynamic control as dynamic pressure built through "
            "the entry. Modern vehicles schedule the same blend: "
            "RCS-only above the sensible atmosphere, blended through "
            "the hypersonic corridor, aero-only once q is sufficient."
        ),
        "key_points": [
            "Newtonian integration gives first pitch-stiffness estimates; blunt forebodies stabilize strongly.",
            "Control authority fades inside thick shock layers; heating punishes deflected surfaces.",
            "Trim drag is a first-order hypersonic design penalty.",
            "Three control regimes: aerodynamic, blended, reaction - with flight-critical hand-offs.",
            "X-15/Shuttle proved the RCS-to-aero blend on entry.",
        ],
        "requirements": [
            "Newtonian pitch-stiffness estimation.",
            "Hypersonic control-surface effectiveness and heating limits.",
            "The RCS/aero control blend schedule.",
        ],
        "standards": [
            "Trim-drag bookkeeping in hypersonic performance.",
            "Control hand-off criteria by dynamic pressure.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_NASA],
        "sig_lens": (
            "His Signature reading: the vehicle steers by fire, then by "
            "air, then by rockets - three hands signing the same "
            "trajectory, each taking over as the last one fades."
        ),
    },
    {
        "key": "nonequilibrium",
        "name": "Chemical Nonequilibrium: Damkohler and Relaxation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Behind a hypersonic shock the gas does not jump instantly "
            "to equilibrium: vibration, dissociation, and ionization "
            "each relax toward equilibrium over their own finite times, "
            "and the flow may cross the shock layer before they finish. "
            "The Damkohler number Da = (flow time)/(chemical time) "
            "decides the regime: Da >> 1 is equilibrium flow (chemistry "
            "infinitely fast), Da << 1 is frozen flow (composition "
            "locked), and Da ~ 1 is nonequilibrium - the reality across "
            "much of the trajectory. In nonequilibrium, a relaxation "
            "zone trails the shock: translational temperature spikes "
            "then falls as energy drains into vibration and "
            "dissociation, and the shock standoff distance, surface "
            "heating, and radiation all differ from both limits. "
            "Computing it requires finite-rate chemistry coupled to "
            "the flowfield - the most expensive and most uncertain "
            "aerothermodynamics there is."
        ),
        "how_it_works": (
            "Follow a fluid particle crossing a Mach 20 bow shock at "
            "70 km. Immediately behind the shock its translational "
            "temperature is ~15,000 K but its vibrational temperature "
            "is still the freestream 250 K and its composition is "
            "still N2/O2 - frozen. Over the vibrational relaxation "
            "time (microseconds), vibration equilibrates and the "
            "translational temperature falls; over the longer "
            "dissociation time, O2 then N2 break apart, soaking up "
            "more energy. The particle may reach the body before "
            "finishing - Da ~ 1 - so the shock layer contains the "
            "whole relaxation history as spatial structure: a thin "
            "frozen layer at the shock, then the relaxation zone, "
            "then near-equilibrium gas at the wall. The standoff "
            "distance for nonequilibrium sits between the frozen "
            "(large) and equilibrium (small) values. Landau-Teller "
            "formulas give vibrational relaxation times; Park's "
            "two-temperature model (T for translation-rotation, T_v "
            "for vibration) is the engineering compromise that makes "
            "the computation tractable."
        ),
        "key_points": [
            "Da = flow time / chemical time: >>1 equilibrium, <<1 frozen, ~1 nonequilibrium.",
            "Relaxation zone trails the shock: temperature overshoot then decay.",
            "Standoff, heating, and radiation differ from both limiting cases.",
            "Landau-Teller vibrational times; Park two-temperature model as the workhorse.",
            "Finite-rate coupled CFD is the most expensive aerothermodynamic analysis.",
        ],
        "requirements": [
            "The Damkohler number and the three regimes.",
            "Relaxation-zone structure behind the shock.",
            "Two-temperature modeling essentials.",
        ],
        "standards": [
            "Nonequilibrium analysis where Da ~ 1 (peak-heating trajectory points).",
            "Park model rate data with uncertainty margins.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_HIRSCHEL],
        "sig_lens": (
            "His Signature reading: the shock writes faster than the "
            "chemistry can read - the gas spends the whole shock layer "
            "catching up with its own signature."
        ),
    },
    {
        "key": "radiative_heating",
        "name": "Radiative Heating: The Glow of Return",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Above about 9-10 km/s entry speed, the shock layer glows "
            "so fiercely that radiation rivals convection as a heating "
            "mechanism: photons from the 10,000+ K plasma stream to the "
            "heat shield directly, unimpeded by the boundary layer. "
            "Atomic nitrogen and oxygen line radiation dominates, with "
            "molecular bands contributing; the radiative flux scales "
            "steeply with velocity (roughly V^8 in some correlations) "
            "and with the shock-layer thickness, so blunt bodies - "
            "thick shock layers - radiate more. Apollo's lunar return "
            "saw significant radiative heating; a Mars-return entry at "
            "12+ km/s would be radiation-dominated. Modeling it needs "
            "the nonequilibrium species concentrations (the radiators) "
            "plus a radiation transport solver (NEQAIR and its "
            "successors): the most physics-rich corner of "
            "aerothermodynamics, and the one with the widest "
            "uncertainty bands."
        ),
        "how_it_works": (
            "At 11 km/s the shock-layer temperature exceeds 10,000 K "
            "and the gas is partially ionized; excited N and O atoms "
            "decay and emit line radiation, while N2+ and molecular "
            "bands add continuum. The volumetric emission scales with "
            "the radiating species densities - themselves "
            "nonequilibrium quantities - integrated along the "
            "line of sight through the shock layer to the wall: a "
            "thicker (blunter) shock layer means a longer radiating "
            "column. Order of magnitude: Apollo saw radiative fluxes "
            "tens of percent of the convective peak; correlations like "
            "Tauber-Sutton give q_rad scaling brutally with velocity, "
            "so each additional km/s above 10 matters enormously. The "
            "wall sees it all - radiation crosses the boundary layer "
            "without attenuation - which is why radiative heating "
            "drives TPS material selection (high emissivity helps "
            "re-radiate it) and why uncertainty factors of 2-3x are "
            "still carried on lunar-return designs."
        ),
        "key_points": [
            "Radiation rivals convection above ~9-10 km/s entry speed.",
            "Atomic N and O line radiation dominates; molecular bands add more.",
            "Flux scales steeply with velocity and with shock-layer thickness (bluntness).",
            "Crosses the boundary layer unattenuated: the wall sees it all.",
            "NEQAIR-class transport + nonequilibrium chemistry; uncertainty bands are wide.",
        ],
        "requirements": [
            "The velocity threshold and scaling of radiative heating.",
            "Radiating species and their nonequilibrium concentrations.",
            "Radiation transport essentials and the Tauber-Sutton form.",
        ],
        "standards": [
            "Radiative heating included for entries above ~9 km/s.",
            "Uncertainty factors carried per agency practice on return missions.",
        ],
        "citations": [C_AHYPER, C_BERTIN, C_NASA],
        "sig_lens": (
            "His Signature reading: past ten kilometers a second the "
            "fire learns to throw its light ahead of itself - the "
            "signature arrives as a glow before the heat."
        ),
    },
    {
        "key": "integrated_design",
        "name": "Designing for Hypersonics: The Full Stack",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hypersonic vehicle design is integration or it is nothing: "
            "the forebody is the inlet, the airframe is the nozzle, the "
            "thermal protection is the structure's load path, and the "
            "trajectory is part of the vehicle. Turbine-based combined "
            "cycle (TBCC) and rocket-based combined cycle (RBCC) engines "
            "span the Mach 0-to-orbital gap no single engine can cover, "
            "handing off from turbine to ramjet to scramjet to rocket "
            "along the ascent. The design spiral runs "
            "aerodynamics-heating-propulsion-trajectory-structures in "
            "one loop because every discipline constrains the others: "
            "sharpen the nose for drag and heating kills it; blunt it "
            "for heating and the scramjet inlet starves. This capstone "
            "record assembles the full stack - regime map, heating "
            "budget, chemistry check, propulsion mode, control blend, "
            "and facility validation - into the single checklist every "
            "hypersonic program runs before it bends metal."
        ),
        "how_it_works": (
            "Lay out a Mach 8 cruise vehicle mission. The trajectory "
            "sets the dynamic-pressure corridor (q ~ 50-100 kPa "
            "typical); the regime map (Mach vs altitude) marks where "
            "real-gas effects, transition, and rarefaction each matter. "
            "Sutton-Graves prices stagnation heating at the hot "
            "trajectory points; Lees distributes it; interaction "
            "factors penalize the cowl lip and flaps; the TPS family "
            "is chosen by peak flux and heat load. The propulsion "
            "mode schedule - turbine to Mach 3, ramjet/scramjet to "
            "Mach 8 - sets inlet capture and nozzle expansion at each "
            "point, and the airframe forebody angles are literally the "
            "inlet ramps. Control blends RCS to aero through the "
            "ascent. Then validation: shock-tunnel heating at the "
            "peak point, expansion-tube chemistry at the hot point, "
            "quiet-tunnel transition, DSMC at the high-altitude "
            "point - the mosaic from the facilities record. Close the "
            "loop: weight from structures and TPS feeds back into "
            "trajectory and heating until the spiral converges."
        ),
        "key_points": [
            "Forebody = inlet, airframe = nozzle: propulsion and aerodynamics are one geometry.",
            "TBCC/RBCC combined cycles span Mach 0 to orbital; mode hand-offs are design drivers.",
            "The design spiral couples aero, heating, propulsion, trajectory, structures.",
            "Regime map + heating budget + chemistry + control blend + facility mosaic = the checklist.",
            "Every sharp-vs-blunt, reusable-vs-expendable choice is a full-stack trade.",
        ],
        "requirements": [
            "The integrated airframe-propulsion geometry.",
            "Combined-cycle mode scheduling.",
            "The full-stack validation mosaic across facilities.",
        ],
        "standards": [
            "Multidisciplinary design iteration practice (Heiser-Pratt + aerothermal).",
            "Flight-envelope clearance by combined ground-test evidence.",
        ],
        "citations": [C_HEISER, C_AHYPER, C_BERTIN],
        "sig_lens": (
            "His Signature reading: the hypersonic vehicle is one "
            "signature drawn across six disciplines - and this database "
            "is the pen."
        ),
    },
    {
        "key": "hypersonic_ld",
        "name": "Hypersonic Lift and Drag: The L/D Barrier",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The lift-to-drag ratio collapses as Mach number rises - "
            "from ~18 for an airliner to ~7 for a supersonic transport "
            "to ~4-6 for the best hypersonic waveriders and ~2 for "
            "blunt capsules - and this collapse, the L/D barrier, "
            "dictates what hypersonic vehicles can do. Wave drag grows "
            "with the square of thickness and deflection angles, skin "
            "friction stays high in hot turbulent boundary layers, and "
            "the Newtonian pressure field punishes any surface that "
            "turns the flow. Kuchemann's empirical relation ties maximum "
            "L/D to Mach number, and the barrier explains the vehicle "
            "zoo: capsules accept L/D ~ 0.3-2 and fall ballistically, "
            "lifting bodies reach ~2-3, waveriders push ~4-6 by "
            "trapping their own shock. Range, crossrange, and "
            "maneuverability all scale directly with hypersonic L/D, "
            "so every point of L/D is bought with bluntness trades, "
            "planform optimization, and viscous-drag reduction."
        ),
        "how_it_works": (
            "Break down hypersonic drag: wave drag from the shock "
            "system (Newtonian estimate: integrate 2 sin^2(theta) over "
            "windward area), skin-friction drag from the hot boundary "
            "layer (turbulent, high wall temperature), and base drag "
            "near vacuum. Lift comes almost entirely from windward "
            "pressure - the leeward side contributes little at "
            "hypersonic speed. The ratio L/D is therefore set by "
            "geometry: slender shapes with small deflection angles "
            "minimize wave drag but suffer heating and volume "
            "penalties; blunt shapes survive heating but their L/D "
            "collapses. Kuchemann's correlation, (L/D)_max ~ 4(M+3)/M "
            "in spirit, captures the decline and is still used for "
            "first estimates. A waverider at Mach 6 reaching L/D = 5 "
            "can glide ~5 times its altitude in range and bank for "
            "crossrange; a capsule at L/D = 0.5 falls nearly straight "
            "down. That arithmetic is why boost-glide vehicles chase "
            "every tenth of L/D."
        ),
        "key_points": [
            "L/D falls with Mach: ~18 subsonic, ~7 supersonic, ~4-6 best hypersonic, ~2 blunt.",
            "Wave drag (geometry) + hot skin friction + base drag = the hypersonic drag budget.",
            "Kuchemann's relation captures the (L/D)_max decline with Mach.",
            "Range and crossrange scale directly with hypersonic L/D.",
            "Vehicle classes sort by L/D: capsules, lifting bodies, waveriders.",
        ],
        "requirements": [
            "The hypersonic drag decomposition.",
            "Kuchemann's L/D correlation and its use.",
            "L/D consequences for range, crossrange, maneuver.",
        ],
        "standards": [
            "L/D quoted at the design Mach with viscous penalties included.",
            "Trimmed L/D (with control deflections) for performance claims.",
        ],
        "citations": [C_AHYPER, C_RASMUSSEN, C_HEISER],
        "sig_lens": (
            "His Signature reading: the faster the signature, the "
            "shorter the glide - L/D is the exchange rate between "
            "speed and reach, and hypersonics pays retail."
        ),
    },
    {
        "key": "boost_glide",
        "name": "Boost-Glide Vehicles: Falling With Style",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A boost-glide vehicle rides a rocket to near-orbital "
            "speed, then glides unpowered through the upper atmosphere "
            "at hypersonic Mach numbers, maneuvering with lift all the "
            "way down. Unlike a ballistic reentry vehicle, which falls "
            "on a predictable arc, the glider trades altitude for "
            "range, banks for crossrange, and arrives unpredictably - "
            "the trajectory is shaped in flight, not set at launch. "
            "The physics is pure hypersonics: L/D ~ 2-3 lifting-body "
            "glide at 30-80 km altitude, peak heating managed by "
            "bluntness and trajectory shaping, guidance by bank-angle "
            "modulation exactly as the Shuttle flew. Public programs - "
            "the US HTV-2 tests, the Army/Navy Common Hypersonic Glide "
            "Body - have demonstrated the regime and its difficulties: "
            "HTV-2's 2010 and 2011 flights both ended early when the "
            "vehicle departed controlled flight, teaching hard lessons "
            "about hypersonic controllability that every program since "
            "has absorbed."
        ),
        "how_it_works": (
            "Boost to ~6 km/s at ~100 km; tip over and enter the glide "
            "at high angle of attack. The vehicle now flies a "
            "quasi-equilibrium glide: lift supports a fraction of "
            "weight, drag bleeds speed, and the flight-path angle stays "
            "shallow because L/D of 2-3 at 50 km altitude balances the "
            "weight component. Bank the lift vector and the trajectory "
            "turns - crossrange of thousands of kilometers is available "
            "from the energy. Heating peaks in the mid-glide where "
            "rho*V^3 maximizes; the trajectory is shaped (higher, "
            "cooler vs lower, faster) against TPS limits. Guidance is "
            "bank-angle modulation inherited from Apollo and Shuttle: "
            "roll to steer lift up/down/left/right, holding the energy "
            "corridor. HTV-2's failures traced to greater-than-expected "
            "yaw and control-surface effectiveness loss in the "
            "high-Mach, high-altitude corner - the viscous interaction "
            "and real-gas effects this database covers, biting a real "
            "program. The lesson generalized: hypersonic controllability "
            "must be validated across the whole Mach-altitude map, not "
            "at points."
        ),
        "key_points": [
            "Boost to near-orbital speed, then unpowered hypersonic glide with maneuvering lift.",
            "Quasi-equilibrium glide at 30-80 km; bank-angle modulation steers range and crossrange.",
            "Heating peaks at max(rho*V^3); trajectory shaping trades heat vs speed.",
            "Guidance inherits Apollo/Shuttle bank-angle energy management.",
            "HTV-2 flights showed hypersonic controllability is the hard problem.",
        ],
        "requirements": [
            "The boost-glide trajectory: boost, glide, terminal phases.",
            "Quasi-equilibrium glide mechanics and bank steering.",
            "Controllability lessons from flight test.",
        ],
        "standards": [
            "Public flight-test record as the empirical anchor (HTV-2, C-HGB).",
            "Full-envelope controllability validation, not point checks.",
        ],
        "citations": [C_NASA, C_AHYPER, C_BERTIN],
        "sig_lens": (
            "His Signature reading: the boost-glider signs the longest "
            "signature in the sky - launched like a bullet, landed like "
            "a rumor."
        ),
    },
]
