#!/usr/bin/env python3
"""Entries for the Aerodynamics field databases (field #23, taxonomy order).

Verified 2026-10-17: NO database covers aerodynamics as an engineering
discipline.
- Manifest-wide regex search (aerofoil|airfoil|aerodynamic|mach.?number|
  shock.?wave|boundary.?layer|wind.?tunnel|navier|compressible|
  supersonic|hypersonic|drag.?polar|ground.?effect|aeroelastic|
  circulation|kutta|prandtl|area.?rule): the only hits are 'flight' (The
  Signature Flight School Database) and 'aviation' (JAH Aviation Database),
  both pilot-level with zero discipline coverage (aviation's generator has
  one incidental 'supersonic' mention; no airfoil theory, compressible flow,
  shock relations, boundary-layer theory, or stability/control treatment),
  plus wind-energy career DBs and 'aerospace-databases' (a database-of-
  databases index). Zero discipline-level aerodynamics records anywhere in
  the manifest.
- Fields #11-22 shard indexes (volcanology, climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics,
  econometrics, psychometrics, turbomachinery, electromagnetics,
  petroleum-refining): direct whole-shard title scans for
  aerofoil|airfoil|aerodynamic|mach.?number|shock.?wave|boundary.?layer|
  wind.?tunnel|navier|compressible|supersonic|hypersonic|drag.?polar|
  ground.?effect|aeroelastic = zero hits.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo;
  fields past the index cross-checked directly above): every record checked
  + admitted at build time.

So this build creates two NEW databases, 32 ladder-ordered records each:

  aerodynamics               - The Aerodynamics Database
                               (public-harvest: real, fact-checked
                               aerodynamics; citations Anderson,
                               Kuethe & Chow, Bertin & Cummings,
                               Abbott & Von Doenhoff, White,
                               Schlichting & Gersten, Shapiro,
                               Houghton & Carpenter, Raymer,
                               McCormick, NACA reports)
  aerodynamics-signature     - The Aerodynamics Signature Database
                               (his original Signature interpretation of
                               the discipline; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

Subtitle disambiguation (fields #13-23 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Continuity and
Bernoulli: Why Speed Changes Pressure" and "The Area Rule: Sculpting Wave
Drag Away".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "aerodynamics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_ANDERSON_FUND = ("Anderson, John D. 'Fundamentals of Aerodynamics', "
                   "6th ed. McGraw-Hill, 2017.")
C_ANDERSON_FLIGHT = ("Anderson, John D. 'Introduction to Flight', "
                     "8th ed. McGraw-Hill, 2016.")
C_KUETHE = ("Kuethe, Arnold M. and Chow, Chuen-Yen. 'Foundations of "
            "Aerodynamics', 5th ed. Wiley, 1998.")
C_BERTIN = ("Bertin, John J. and Cummings, Russell M. 'Aerodynamics for "
            "Engineers', 6th ed. Pearson, 2014.")
C_ABBOTT = ("Abbott, Ira H. and Von Doenhoff, Albert E. 'Theory of Wing "
            "Sections'. Dover, 1959.")
C_WHITE = ("White, Frank M. 'Viscous Fluid Flow', 3rd ed. McGraw-Hill, 2006.")
C_SCHLICHTING = ("Schlichting, Hermann and Gersten, Klaus. "
                 "'Boundary-Layer Theory', 9th ed. Springer, 2017.")
C_SHAPIRO = ("Shapiro, Ascher H. 'The Dynamics and Thermodynamics of "
             "Compressible Fluid Flow'. Ronald Press, 1953.")
C_HOUGHTON = ("Houghton, E. L. and Carpenter, P. W. 'Aerodynamics for "
              "Engineering Students', 7th ed. Butterworth-Heinemann, 2017.")
C_RAYMER = ("Raymer, Daniel P. 'Aircraft Design: A Conceptual Approach', "
            "6th ed. AIAA, 2018.")
C_MCCORMICK = ("McCormick, Barnes W. 'Aerodynamics, Aeronautics, and Flight "
               "Mechanics', 2nd ed. Wiley, 1995.")
C_NACA = ("NACA Report 824, 'Summary of Airfoil Data', 1945.")

ENTRIES = [
    {
        "key": "what_is_aerodynamics",
        "name": "What Aerodynamics Is: The Study of Air in Motion",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Aerodynamics is the branch of fluid mechanics that studies how air "
            "moves around solid bodies and how that motion produces forces. "
            "Every flying machine - from a paper dart to a supersonic "
            "airliner - is a negotiation with air: the air pushes back on the "
            "body (lift, drag, moments) and the body redirects the air. The "
            "discipline splits into incompressible aerodynamics (slow flight, "
            "where density barely changes) and compressible aerodynamics "
            "(fast flight, where density changes dominate and shock waves "
            "appear). It also splits into external aerodynamics (flow around "
            "aircraft, cars, buildings) and internal aerodynamics (flow inside "
            "ducts, inlets, and engines). Everything in this database is one "
            "answer to one question: what does the air do when something "
            "moves through it?"
        ),
        "how_it_works": (
            "Air is a continuous fluid: countless molecules act like a smooth "
            "medium. When a body moves through air (equivalently, air flows "
            "past a stationary body), the air must split, speed up, slow down, "
            "and rejoin. Where it speeds up, pressure falls; where it slows, "
            "pressure rises (Bernoulli's principle). Pressure acts on every "
            "square inch of the surface, and skin friction drags along it. "
            "Integrating pressure and shear over the whole surface gives the "
            "aerodynamic forces: lift perpendicular to the flow, drag along "
            "it, and the moments about the axes. Change the speed, the angle, "
            "or the shape, and the whole pressure map - and the forces - "
            "change with it."
        ),
        "key_points": [
            "Aerodynamics = fluid mechanics of air moving relative to a solid body.",
            "Two big divisions: incompressible (slow) vs compressible (fast) flow.",
            "External aerodynamics: around aircraft, cars, buildings; internal: inside ducts and engines.",
            "All forces come from two surface effects: pressure distribution and skin friction.",
            "Lift acts perpendicular to the flight direction; drag acts along it.",
            "Reference frames are equivalent: moving body through still air = air streaming past a fixed body.",
        ],
        "requirements": [
            "A working grasp of air as a continuous fluid medium.",
            "Speed, pressure, density, and temperature as the state variables of flow.",
            "Force as the sum of pressure and shear acting over a surface.",
        ],
        "standards": [
            "Standard atmosphere (ISA) properties for sea-level reference values.",
            "Conservation of mass, momentum, and energy as governing laws.",
        ],
        "citations": [C_ANDERSON_FUND, C_KUETHE, C_ANDERSON_FLIGHT],
        "sig_lens": (
            "His Signature reading: aerodynamics is the signature of motion "
            "written in air - every vehicle signs the sky with its pressure "
            "field, and reading that signature is the whole discipline."
        ),
    },
    {
        "key": "air_as_fluid",
        "name": "Air as a Fluid: Density, Pressure, and Viscosity",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Air behaves as a fluid - a substance that flows - and three "
            "properties govern everything it does: density (how much mass per "
            "cubic meter), pressure (how hard the molecules push), and "
            "viscosity (how strongly the fluid resists being sheared). Density "
            "sets the mass the wing must turn; pressure is the force the "
            "engineer's instruments read; viscosity creates the boundary "
            "layer, skin-friction drag, and flow separation. All three change "
            "with altitude: climb to 35,000 feet and the air is about one-"
            "fourth as dense as at sea level, so the airplane must fly faster "
            "to make the same lift. The International Standard Atmosphere "
            "(ISA) tabulates these changes so every designer uses the same "
            "reference sky."
        ),
        "how_it_works": (
            "Air follows the ideal gas law: pressure = density x R x "
            "temperature, with R = 287 J/(kg-K) for air. Temperature falls "
            "about 1.98 C per 1,000 feet up to 36,089 feet (the tropopause), "
            "then stays constant; pressure falls roughly exponentially "
            "because each layer supports the weight of the air above it. "
            "Viscosity rises slightly with temperature (Sutherland's formula) "
            "but matters mainly in the thin boundary layer near surfaces. "
            "Engineers compute aerodynamic forces with density because "
            "dynamic pressure - one half times density times velocity squared "
            "- is the currency of lift and drag: halve the density, double "
            "the speed-squared to keep forces the same."
        ),
        "key_points": [
            "Density, pressure, viscosity, temperature fully describe the air's state.",
            "Ideal gas law links pressure, density, and temperature (R = 287 J/(kg-K)).",
            "Density at 35,000 ft is roughly one-quarter of sea-level density.",
            "Dynamic pressure q = 1/2 rho V^2 is the common scale of all aerodynamic forces.",
            "Viscosity is tiny but decisive: it creates skin friction and the boundary layer.",
            "The ISA gives one shared reference atmosphere for all designers.",
        ],
        "requirements": [
            "Algebra and the ideal gas law.",
            "Temperature lapse rate and exponential pressure decay with altitude.",
            "The concept of dynamic pressure as force scale.",
        ],
        "standards": [
            "ISA sea-level reference: 1.225 kg/m3, 101,325 Pa, 288.15 K.",
            "Sutherland's formula for viscosity vs temperature.",
        ],
        "citations": [C_ANDERSON_FUND, C_KUETHE, C_HOUGHTON],
        "sig_lens": (
            "His Signature reading: the atmosphere is a layered archive - "
            "every altitude shelves a thinner, colder edition of the same "
            "fluid, and the ISA is its card catalog."
        ),
    },
    {
        "key": "four_forces",
        "name": "The Four Forces: Lift, Weight, Thrust, and Drag",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every airplane answers to four forces. Lift pulls the airplane "
            "up, perpendicular to the flight path; weight pulls it down toward "
            "the Earth's center; thrust pushes it forward, made by engines; "
            "drag pulls it back, the price of moving through air. In straight, "
            "level, unaccelerated flight they balance in pairs: lift equals "
            "weight, thrust equals drag. Turn, climb, or accelerate and the "
            "balance breaks on purpose: extra lift banks the airplane into a "
            "turn, excess thrust over drag climbs it. Because lift and drag "
            "both scale with dynamic pressure and wing area, the whole "
            "performance of an airplane - stall speed, range, ceiling - flows "
            "from how these four forces are proportioned."
        ),
        "how_it_works": (
            "Lift and drag are the aerodynamic forces the airflow applies to "
            "the airplane; weight is gravity on its mass; thrust is the "
            "engine's push. Engineers write lift L = q x S x CL and drag "
            "D = q x S x CD, where q is dynamic pressure, S is wing area, and "
            "CL, CD are dimensionless coefficients set by shape and angle of "
            "attack. Steady level flight demands L = W and T = D. The power "
            "required to sustain flight is P = D x V; the minimum of that "
            "curve sets the maximum endurance speed, and the tangent from the "
            "origin sets the maximum range speed. Maneuvering multiplies the "
            "load factor n = L/W: a 60-degree banked turn needs n = 2, so the "
            "wing must make twice its weight in lift."
        ),
        "key_points": [
            "Steady level flight: lift = weight and thrust = drag.",
            "Lift and drag scale with dynamic pressure times wing area times a coefficient.",
            "Power required = drag x velocity; its minimum sets best endurance speed.",
            "Load factor n = L/W multiplies in maneuvers: 60-degree bank needs n = 2.",
            "Excess thrust over drag is what climbs and accelerates the airplane.",
            "Every performance chart is a portrait of the four-force balance.",
        ],
        "requirements": [
            "Newton's second law applied to the whole airplane.",
            "Dynamic pressure and the wing reference area.",
            "The load factor concept for maneuvering flight.",
        ],
        "standards": [
            "Steady-flight equilibrium conditions (sum of forces = 0).",
            "Power-required curve analysis for performance speeds.",
        ],
        "citations": [C_ANDERSON_FLIGHT, C_MCCORMICK, C_KUETHE],
        "sig_lens": (
            "His Signature reading: four forces, one contract - the wing "
            "signs its lift, the engine signs its thrust, and every flight "
            "is the Signature-system balance of those signatures."
        ),
    },
    {
        "key": "bernoulli_continuity",
        "name": "Continuity and Bernoulli: Why Speed Changes Pressure",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Two equations run slow-speed aerodynamics. Continuity says air "
            "cannot pile up: where a streamtube narrows, the flow speeds up "
            "so the same mass passes each second. Bernoulli's equation says "
            "that along a streamline in steady, incompressible, frictionless "
            "flow, static pressure plus dynamic pressure is constant: where "
            "the air speeds up, the pressure falls; where it slows, pressure "
            "rises. This is why a wing's curved upper surface shows low "
            "pressure (the air accelerates over it) and why a venturi meter "
            "can measure airspeed from a pressure reading. The two equations "
            "together explain lift at its most basic: geometry sets the "
            "speed field, the speed field sets the pressure field, and the "
            "pressure field pushes the wing."
        ),
        "how_it_works": (
            "Continuity for incompressible flow: area x velocity is constant "
            "along a streamtube (A1 x V1 = A2 x V2), because density cannot "
            "change. Bernoulli: p + 1/2 rho V^2 = constant along a "
            "streamline, from the momentum equation with no friction and no "
            "density change. Squeeze the tube to half its area and velocity "
            "doubles, dynamic pressure quadruples, and static pressure drops "
            "by three units of the original dynamic pressure. These relations "
            "hold only for incompressible (Mach below ~0.3), inviscid, steady "
            "flow - exactly why they are the entry point, not the whole "
            "story, of aerodynamics."
        ),
        "key_points": [
            "Continuity: mass flow is conserved; a narrower streamtube means faster flow.",
            "Bernoulli: p + 1/2 rho V^2 is constant along a streamline (incompressible, inviscid, steady).",
            "Faster flow = lower pressure; slower flow = higher pressure.",
            "Valid only below about Mach 0.3, where density is effectively constant.",
            "A venturi uses the pressure drop to measure velocity - the pitot-static system in reverse.",
            "The pressure field integrated over the wing is the physical origin of lift.",
        ],
        "requirements": [
            "The mass-conservation idea behind continuity.",
            "The momentum balance that yields Bernoulli's equation.",
            "The limits: incompressibility, steadiness, no friction.",
        ],
        "standards": [
            "Mach < 0.3 as the incompressible-flow criterion.",
            "Pitot-static pressure measurement practice.",
        ],
        "citations": [C_ANDERSON_FUND, C_HOUGHTON, C_KUETHE],
        "sig_lens": (
            "His Signature reading: Bernoulli is the first signature of "
            "flow - a trade written in pressure, where every unit of speed "
            "is bought with pressure and the ledger always balances."
        ),
    },
    {
        "key": "reynolds_number",
        "name": "The Reynolds Number: When Smooth Flow Turns Turbulent",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The Reynolds number, Re = rho x V x L / mu, is the most used "
            "dimensionless number in aerodynamics: it compares inertia "
            "(which wants to keep the flow going straight) to viscosity "
            "(which wants to calm it). Low Reynolds number means smooth, "
            "orderly laminar flow; high Reynolds number means chaotic "
            "turbulent flow with eddies and mixing. The same wing at the "
            "same speed behaves differently in water than in air because Re "
            "changes - this is why wind tunnels must match Reynolds number "
            "to match reality. Re decides where the boundary layer turns "
            "turbulent, how much skin-friction drag the surface feels, and "
            "whether the flow separates from a curving surface."
        ),
        "how_it_works": (
            "Pick a length L (a wing chord), compute rho x V x L / mu. On a "
            "flat plate the boundary layer turns turbulent around Re_x = 5 x "
            "10^5 to 3 x 10^6 depending on smoothness and disturbances. A "
            "small model airplane at 10 m/s with a 0.3 m chord flies at Re ~ "
            "2 x 10^5 (mostly laminar); an airliner wing at 250 m/s with a 6 m "
            "chord flies at Re ~ 10^8 (turbulent over nearly all of it). "
            "Turbulent boundary layers mix faster, so they resist separation "
            "better but pay more skin friction. Dynamic similarity - matching "
            "Re between model and full scale - is the founding rule of "
            "experimental aerodynamics."
        ),
        "key_points": [
            "Re = rho V L / mu compares inertial forces to viscous forces.",
            "Low Re = laminar, orderly; high Re = turbulent, chaotic.",
            "Transition on a flat plate occurs around Re ~ 5 x 10^5 (smooth conditions).",
            "Turbulent layers resist separation but carry more skin-friction drag.",
            "Matching Re is the rule that makes wind-tunnel tests represent full-scale flight.",
            "Scale effects - why models misbehave - are mostly Reynolds-number effects.",
        ],
        "requirements": [
            "Density, velocity, a characteristic length, and dynamic viscosity.",
            "The laminar vs turbulent distinction.",
            "Dynamic similarity between model and prototype.",
        ],
        "standards": [
            "Re_x ~ 5 x 10^5 as the smooth flat-plate transition reference.",
            "Wind-tunnel Reynolds-number reporting practice.",
        ],
        "citations": [C_WHITE, C_SCHLICHTING, C_ANDERSON_FUND],
        "sig_lens": (
            "His Signature reading: the Reynolds number is the border "
            "checkpoint of flow - laminar below the line, turbulent above, "
            "and every surface negotiates its own crossing."
        ),
    },
    {
        "key": "lift_explained",
        "name": "How Wings Make Lift: Airfoils, Angle of Attack, and Circulation",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A wing makes lift by turning the airflow downward. The wing's "
            "cross-section - the airfoil - meets the air at an angle of "
            "attack; the air accelerates over the curved upper surface, "
            "pressure falls there, and the resulting pressure difference "
            "between lower and upper surfaces pushes the wing up. "
            "Mathematically, the Kutta-Joukowski theorem ties lift per unit "
            "span to circulation: L' = rho x V x Gamma, where circulation is "
            "the net spin of the flow around the airfoil. The starting "
            "vortex left behind at takeoff balances the bound circulation on "
            "the wing - a beautiful conservation law. Net effect: the wing "
            "deflects a mass of air downward, and Newton's third law gives "
            "the airplane its upward push."
        ),
        "how_it_works": (
            "Increase the angle of attack and lift grows almost linearly - "
            "about 0.11 per degree (2 pi per radian) for a thin airfoil - "
            "until the stall angle around 15 degrees, where the flow "
            "separates and lift collapses. Circulation Gamma arises because "
            "the flow must leave the sharp trailing edge smoothly (the Kutta "
            "condition); the asymmetry this imposes speeds the upper flow and "
            "slows the lower flow. Integrating the pressure difference over "
            "the chord gives L' = rho x V x Gamma. Cambered airfoils make "
            "lift even at zero angle of attack; symmetric ones need positive "
            "angle. Downwash - the downward-turned wake - is lift's "
            "signature on the air."
        ),
        "key_points": [
            "Lift = the wing deflecting air downward; the reaction pushes the wing up.",
            "Kutta-Joukowski: lift per unit span L' = rho V Gamma (circulation).",
            "Lift grows ~0.11 per degree of angle of attack until stall near 15 degrees.",
            "Camber lets an airfoil lift at zero angle of attack.",
            "The Kutta condition at the sharp trailing edge is what creates the circulation.",
            "Downwash in the wake is the physical trace of lift.",
        ],
        "requirements": [
            "The angle-of-attack concept and the airfoil cross-section.",
            "Circulation as the net rotational tendency of the flow.",
            "Newton's third law applied to the deflected air mass.",
        ],
        "standards": [
            "Thin-airfoil lift slope 2 pi per radian (incompressible).",
            "Stall angle ~15 degrees for typical airfoils.",
        ],
        "citations": [C_ANDERSON_FUND, C_KUETHE, C_ABBOTT],
        "sig_lens": (
            "His Signature reading: circulation is the wing's signature "
            "motion - a loop of spin bound to the airfoil, written in the "
            "air and answered by lift."
        ),
    },
    {
        "key": "drag_decomposed",
        "name": "Drag, Decomposed: Friction, Pressure, and Induced Drag",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Drag is not one thing but three, and each is fought differently. "
            "Skin-friction drag is the air's viscosity gripping the surface "
            "in the boundary layer - polished, laminar surfaces minimize it. "
            "Form (pressure) drag is the pressure deficit in the separated "
            "wake behind a blunt body - streamlined shapes minimize it. "
            "Induced drag is the price of lift itself: the wing's tip "
            "vortices tilt the lift vector backward, creating a drag that "
            "grows with the square of lift and shrinks with wingspan. At "
            "low speed, induced drag dominates (takeoff, climb); at high "
            "speed, friction and form drag dominate (cruise). The drag polar "
            "- CD plotted against CL - is the airplane's cost curve for "
            "flying."
        ),
        "how_it_works": (
            "Total drag D = q x S x (CD_friction + CD_pressure + CD_induced). "
            "Skin friction follows flat-plate laws: laminar Cf ~ "
            "1.328/sqrt(Re), turbulent Cf ~ 0.074/Re^0.2. Form drag comes "
            "from the wake: a streamlined body keeps the flow attached and "
            "the wake thin. Induced drag CDi = CL^2 / (pi x AR x e), where AR "
            "is aspect ratio (span^2/area) and e is the span efficiency - "
            "doubling the span quarters the induced drag at the same lift. "
            "The classic U-shaped drag-vs-speed curve is induced drag falling "
            "as 1/V^2 while parasite drag (friction + form) rises as V^2."
        ),
        "key_points": [
            "Skin-friction drag: viscosity's grip, fought with smoothness and laminar flow.",
            "Form drag: the wake's pressure deficit, fought with streamlining.",
            "Induced drag: the cost of lift, CDi = CL^2/(pi AR e).",
            "Induced drag dominates slow flight; parasite drag dominates fast flight.",
            "High aspect ratio (long, slender wings) is the direct cure for induced drag.",
            "The drag polar plots the total cost of any lift the wing makes.",
        ],
        "requirements": [
            "The three-component decomposition of drag.",
            "Aspect ratio and span efficiency factor.",
            "The speed dependence of each component.",
        ],
        "standards": [
            "Flat-plate skin-friction correlations (laminar and turbulent).",
            "The parabolic drag polar CD = CD0 + CL^2/(pi AR e).",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_HOUGHTON],
        "sig_lens": (
            "His Signature reading: drag is the tax the air levies on "
            "motion - friction, pressure, and lift each file their own "
            "return, and the polar is the audit."
        ),
    },
    {
        "key": "boundary_layer",
        "name": "The Boundary Layer: Where Air Meets the Wing",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Right at a solid surface, air sticks: the no-slip condition "
            "forces velocity to zero at the wall. The thin region where "
            "velocity climbs from zero back to the free-stream value is the "
            "boundary layer - often millimeters thick on a wing, yet it "
            "decides skin-friction drag, heat transfer, and whether the flow "
            "separates. Ludwig Prandtl's 1904 boundary-layer concept let "
            "engineers split the flow into an outer inviscid region (handled "
            "by Bernoulli and potential theory) and a thin viscous inner "
            "region - the founding simplification of modern aerodynamics. "
            "Laminar boundary layers are thin and low-drag; turbulent ones "
            "are thicker, draggier, but far more resistant to separation."
        ),
        "how_it_works": (
            "On a flat plate the laminar layer grows as delta ~ 5x/sqrt(Re_x) "
            "(the Blasius solution), and its skin friction is Cf = "
            "1.328/sqrt(Re_x). An adverse pressure gradient - pressure "
            "rising in the flow direction, as on the aft part of a wing - "
            "slows the near-wall flow; when the wall shear hits zero, the "
            "layer separates, the wake balloons, and pressure drag surges. "
            "Turbulent layers mix high-momentum air down to the wall, which "
            "is why golf-ball dimples and vortex generators exist: a "
            "deliberately turbulent layer stays attached longer. Transition "
            "location, roughness, and suction all tune the layer's behavior."
        ),
        "key_points": [
            "No-slip condition: air velocity is zero exactly at the surface.",
            "The boundary layer is thin but controls drag, heating, and separation.",
            "Prandtl (1904): split the flow into inviscid outer and viscous inner regions.",
            "Laminar Blasius layer: delta ~ 5x/sqrt(Re_x), low friction.",
            "Adverse pressure gradients cause separation: wall shear falls to zero.",
            "Turbulent layers are draggier but resist separation; vortex generators exploit this.",
        ],
        "requirements": [
            "The no-slip condition and the velocity profile idea.",
            "Laminar vs turbulent structure.",
            "Pressure gradient effects on near-wall flow.",
        ],
        "standards": [
            "Blasius flat-plate solution as the laminar reference.",
            "Separation criterion: zero wall shear stress.",
        ],
        "citations": [C_SCHLICHTING, C_WHITE, C_ANDERSON_FUND],
        "sig_lens": (
            "His Signature reading: the boundary layer is the negotiation "
            "table between the wing and the air - every drag dollar is "
            "counted in its first millimeter."
        ),
    },
]

ENTRIES += [
    {
        "key": "airfoil_geometry",
        "name": "Airfoil Geometry: Camber, Thickness, and the Mean Line",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every airfoil is described by a small vocabulary: the chord "
            "line (nose to tail), the mean camber line (midway between upper "
            "and lower surfaces), camber (how far the mean line bows above "
            "the chord), and thickness (the maximum height of the section). "
            "Camber is the dial for lift at zero angle of attack: a 2% "
            "camber gives roughly +0.2 of lift coefficient with the wing "
            "level. Thickness is the dial for structure and stall: thick "
            "sections (12-15%) carry deep spars and stall gently, thin "
            "sections (6-9%) suit high speed. The NACA four-digit family "
            "encodes all of it in the name - NACA 2412 means 2% camber at "
            "40% chord, 12% thick - and the NACA 6-series added laminar-flow "
            "shaping. Choosing the section is the first design decision of "
            "any wing."
        ),
        "how_it_works": (
            "Thin-airfoil theory treats the section as its camber line with "
            "a vortex sheet; the lift slope stays near 2 pi per radian "
            "regardless of camber, while the zero-lift angle shifts by about "
            "-0.11 radians per unit of (camber/chord) slope measure. The "
            "quarter-chord point is special: for subsonic thin airfoils the "
            "aerodynamic center sits there, and the pitching moment about it "
            "is nearly constant with angle of attack. Thickness delays the "
            "pressure recovery on the aft upper surface, which sets the "
            "maximum lift and stall character. Modern design uses inverse "
            "methods - specify the desired pressure distribution, compute "
            "the shape that produces it - then verifies with wind tunnels "
            "and CFD."
        ),
        "key_points": [
            "Chord, camber, thickness, and mean line are the section vocabulary.",
            "Camber sets lift at zero angle of attack (~+0.1 CL per 1% camber).",
            "Thickness sets structural depth, drag, and stall gentleness.",
            "NACA 2412 = 2% camber at 40% chord, 12% thick.",
            "The aerodynamic center sits near the quarter-chord for thin subsonic sections.",
            "Inverse design starts from a target pressure distribution and solves for the shape.",
        ],
        "requirements": [
            "The airfoil cross-section and its reference lines.",
            "How camber shifts the lift curve without changing its slope.",
            "The quarter-chord aerodynamic center property.",
        ],
        "standards": [
            "NACA 4-digit and 6-series naming conventions.",
            "Thin-airfoil theory lift slope 2 pi per radian.",
        ],
        "citations": [C_ABBOTT, C_ANDERSON_FUND, C_NACA],
        "sig_lens": (
            "His Signature reading: the airfoil section is a signature in "
            "cross-section - camber is the flourish, thickness the stroke "
            "weight, and the NACA digits its catalog number."
        ),
    },
    {
        "key": "compressible_flow",
        "name": "Compressible Flow: The Mach Number and the Speed of Sound",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Above about Mach 0.3 the air can no longer be treated as "
            "incompressible: density changes become large enough to reshape "
            "the flow. The Mach number M = V/a - velocity divided by the "
            "local speed of sound - is the compass of this regime. The speed "
            "of sound itself, a = sqrt(gamma x R x T), depends only on "
            "temperature for a perfect gas: about 340 m/s at sea level, 295 "
            "m/s at 35,000 feet. Below Mach 1 disturbances outrun the "
            "aircraft and the flow adjusts smoothly; above Mach 1 the "
            "aircraft outruns its own pressure signals, disturbances pile up, "
            "and shock waves form. Transonic (0.8-1.2), supersonic (1.2-5), "
            "and hypersonic (above 5) each have their own physics and their "
            "own design rules."
        ),
        "how_it_works": (
            "Sound is a weak pressure wave; information about the approaching "
            "body travels at speed a. At M < 1 the flow 'knows' the body is "
            "coming and streamlines adjust upstream. At M > 1 no signal "
            "travels ahead, so the flow turns only across shock waves - "
            "near-discontinuities in pressure, density, and temperature. The "
            "area-velocity relation for isentropic flow, dA/A = (M^2 - 1) "
            "dV/V, is the master rule of nozzles and diffusers: subsonic "
            "flow speeds up in a converging duct, supersonic flow speeds up "
            "in a diverging duct. That single sign flip - (M^2 - 1) - is why "
            "rocket nozzles are convergent-divergent."
        ),
        "key_points": [
            "Mach number M = V/a; compressible effects matter above ~M 0.3.",
            "Speed of sound a = sqrt(gamma R T): ~340 m/s at sea level, ~295 m/s at 35,000 ft.",
            "Subsonic: signals outrun the body, flow adjusts smoothly upstream.",
            "Supersonic: no upstream signals; turns happen only across shocks.",
            "Regimes: transonic 0.8-1.2, supersonic 1.2-5, hypersonic above 5.",
            "The area-velocity relation flips sign at Mach 1 - the basis of C-D nozzles.",
        ],
        "requirements": [
            "The Mach number as the ratio of flow speed to signal speed.",
            "Temperature dependence of the speed of sound.",
            "The concept of upstream influence (or its absence).",
        ],
        "standards": [
            "Mach 0.3 as the incompressibility limit.",
            "Isentropic flow relations for gamma = 1.4.",
        ],
        "citations": [C_ANDERSON_FUND, C_SHAPIRO, C_KUETHE],
        "sig_lens": (
            "His Signature reading: Mach 1 is the signature line of speed - "
            "below it the air signs ahead, above it the aircraft signs "
            "first and the shock is the stamp."
        ),
    },
    {
        "key": "ground_effect",
        "name": "Ground Effect: Free Lift Near the Surface",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Fly within about one wingspan of the ground and the airplane "
            "gets more efficient: induced drag drops because the ground "
            "blocks the downwash and weakens the wingtip vortices. Pilots "
            "feel it as 'float' on landing - the airplane that was "
            "descending happily suddenly refuses to settle. Racing cars "
            "exploit the same physics in reverse with venturi underbodies. "
            "Ground effect is pure induced-drag physics: the ground acts "
            "like a mirror wing (the method of images), and the mirrored "
            "vortex system cancels part of the real one's downwash. The "
            "effect is strongest below half a wingspan and fades by about "
            "one wingspan of height."
        ),
        "how_it_works": (
            "Induced drag comes from downwash tilting the lift vector; the "
            "ground constrains the vertical velocity to zero at the surface, "
            "so downwash - and with it induced drag - falls. The reduction "
            "factor is roughly 1 - exp-based correlations give about a 20-40% "
            "induced-drag cut at a height of one-tenth the span. Total drag "
            "at constant lift therefore falls, the lift-to-drag ratio rises, "
            "and the airplane floats. The mirror-image model places an "
            "identical wing below the ground plane; the symmetry enforces "
            "zero normal velocity at the ground exactly as the real surface "
            "does. Takeoff benefits too: the airplane lifts off at a lower "
            "speed, though it must then climb out of ground effect on "
            "reduced excess power."
        ),
        "key_points": [
            "Within ~one wingspan of the ground, induced drag drops sharply.",
            "The ground blocks downwash; wingtip vortices weaken.",
            "Landing 'float' is ground effect refusing to let the airplane settle.",
            "Modeled by the method of images: a mirror wing beneath the surface.",
            "Strongest below half a wingspan; negligible above one wingspan.",
            "Takeoff lift-off speed falls, but climb-out must escape the effect.",
        ],
        "requirements": [
            "Induced drag's dependence on downwash.",
            "The mirror-image (method of images) concept.",
            "Height measured in fractions of wingspan.",
        ],
        "standards": [
            "Ground-effect correction factors for induced drag (Wieselsberger-type).",
            "Takeoff and landing performance accounting for ground effect.",
        ],
        "citations": [C_MCCORMICK, C_ANDERSON_FLIGHT, C_RAYMER],
        "sig_lens": (
            "His Signature reading: the ground co-signs the wing's "
            "signature - a mirror wing under the runway that pays part of "
            "the lift bill for free."
        ),
    },
    {
        "key": "airfoil_performance",
        "name": "Airfoil Performance: Lift Curves, Stall, and Drag Polars",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The lift curve - CL versus angle of attack - is the airfoil's "
            "report card: a straight line of slope about 0.11 per degree, "
            "then a peak at CLmax (typically 1.2-1.6 for plain sections), "
            "then the stall drop as the upper-surface flow separates. The "
            "drag polar - CD versus CL - shows the price: minimum drag near "
            "zero lift, rising steeply past CLmax. Together they set the "
            "stall speed (Vs = sqrt(2W/(rho S CLmax))), the best glide "
            "angle, and the maneuvering limits. The NACA cataloged thousands "
            "of sections in wind tunnels (NACA TR-824), and those curves - "
            "later extended by CFD - are still the working data of wing "
            "design. Every airplane's flight envelope is drawn from these "
            "two curves."
        ),
        "how_it_works": (
            "Raise the angle of attack: the suction peak on the upper "
            "surface deepens, the adverse pressure gradient steepens, and at "
            "the critical angle the boundary layer separates - first near "
            "the trailing edge, then forward. Lift peaks and falls; drag "
            "jumps because the wake balloons. The polar's bucket shape comes "
            "from CD = CD0 + CL^2/(pi AR e): parasite drag constant, "
            "induced drag quadratic in lift. Maximum L/D sits at the tangent "
            "from the origin to the polar - the best-glide and best-range "
            "point. Compressibility and Reynolds number shift the curves: "
            "higher Re delays stall and deepens the bucket."
        ),
        "key_points": [
            "Lift curve: linear ~0.11/deg, peaks at CLmax, then stalls.",
            "Stall = upper-surface separation at the critical angle (~15 deg).",
            "Drag polar CD vs CL: the cost curve of lift; max L/D at the tangent point.",
            "Stall speed Vs = sqrt(2W/(rho S CLmax)).",
            "NACA TR-824 cataloged the classic section data.",
            "Reynolds number and Mach number shift both curves.",
        ],
        "requirements": [
            "Reading CL-alpha and CD-CL plots.",
            "The separation mechanism behind stall.",
            "How CLmax converts to stall speed.",
        ],
        "standards": [
            "NACA airfoil data reporting (TR-824).",
            "Stall-speed and maneuvering-speed definitions.",
        ],
        "citations": [C_ABBOTT, C_NACA, C_ANDERSON_FUND],
        "sig_lens": (
            "His Signature reading: the lift curve is the airfoil's "
            "handwriting - rising steady, peaking, then the stall where the "
            "signature breaks off the page."
        ),
    },
    {
        "key": "induced_drag",
        "name": "Induced Drag and Aspect Ratio: The Cost of Making Lift",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Induced drag is the unavoidable tax on lift: a finite wing "
            "leaks high-pressure air around its tips, the tip vortices "
            "induce downwash, and the downwash tilts the lift vector "
            "backward. The result is a drag component that grows with the "
            "square of the lift coefficient and shrinks with aspect ratio: "
            "CDi = CL^2/(pi x AR x e). Gliders stretch to aspect ratios of "
            "30-40 to nearly erase it; airliners sit near 8-10 as a "
            "compromise with structure and gates; fighters accept 3-4 and "
            "pay in fuel. Prandtl's lifting-line theory (1918) showed the "
            "elliptical lift distribution minimizes induced drag, which is "
            "why the Spitfire's elliptical wing is more than pretty - and "
            "why winglets recover some of the tip loss by diffusing the "
            "vortex."
        ),
        "how_it_works": (
            "Model the wing as a bound vortex with trailing tip vortices. "
            "Each trailing vortex induces a downward velocity on the wing "
            "(Biot-Savart law); the local flow tilts by the induced angle "
            "alpha_i, and the lift - perpendicular to the local flow - tilts "
            "back by the same angle, producing Di = L x alpha_i. With an "
            "elliptical spanwise lift distribution the downwash is uniform "
            "and CDi reaches its minimum CL^2/(pi AR). The Oswald "
            "efficiency factor e (0.7-0.95) measures how close a real wing "
            "comes to the elliptical ideal. Winglets act as end plates that "
            "spread the tip vortex vertically, raising the effective aspect "
            "ratio without lengthening the span."
        ),
        "key_points": [
            "Induced drag = lift tilted backward by downwash from tip vortices.",
            "CDi = CL^2/(pi AR e): square with lift, inverse with aspect ratio.",
            "Elliptical lift distribution gives the minimum (Prandtl, 1918).",
            "Oswald factor e measures closeness to the elliptical ideal.",
            "Winglets raise effective aspect ratio by managing the tip vortex.",
            "Design trade: long wings save fuel but cost structure and gate space.",
        ],
        "requirements": [
            "The tip-vortex/downwash mechanism.",
            "Aspect ratio = span^2 / wing area.",
            "The quadratic dependence on lift coefficient.",
        ],
        "standards": [
            "Prandtl lifting-line theory as the reference model.",
            "Oswald efficiency reporting in drag polars.",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_KUETHE],
        "sig_lens": (
            "His Signature reading: induced drag is the wing paying "
            "postage on its own lift - the tip vortices are the receipt, "
            "and span is the discount."
        ),
    },
    {
        "key": "normal_shocks",
        "name": "Normal Shock Waves: Supersonic to Subsonic in One Jump",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A normal shock is the thinnest violent event in aerodynamics: "
            "across a few molecular mean free paths, supersonic flow "
            "decelerates to subsonic, pressure jumps, density jumps, "
            "temperature jumps - and total pressure (the useful energy) is "
            "irreversibly lost. The normal-shock relations give the exact "
            "ratios as functions of upstream Mach number for a perfect gas. "
            "At Mach 2 the static pressure ratio is 4.5, the density ratio "
            "approaches its limit of 6, and the temperature ratio is 1.69; "
            "total pressure recovery is 0.721, meaning over a quarter of "
            "the flow's useful energy is gone. Every supersonic inlet, every "
            "transonic wing shock, and every re-entry bow shock obeys these "
            "relations - they are the toll booths of high-speed flight."
        ),
        "how_it_works": (
            "Apply conservation of mass, momentum, and energy across the "
            "discontinuity plus the ideal gas law: four equations solve for "
            "the downstream state given upstream Mach M1 and gamma. The "
            "pressure ratio is p2/p1 = 1 + 2 gamma/(gamma+1) (M1^2 - 1); the "
            "density ratio asymptotes to (gamma+1)/(gamma-1) = 6 for air, "
            "so density cannot rise without bound; the temperature ratio "
            "follows from the gas law. Entropy must increase, so only "
            "compression shocks (M1 > 1 to M2 < 1) are physical - expansion "
            "shocks are forbidden. The total-pressure loss grows fast with "
            "M1, which is why supersonic inlets use multiple oblique shocks "
            "instead of one strong normal shock."
        ),
        "key_points": [
            "Across a normal shock: M drops below 1, p/rho/T jump, total pressure is lost.",
            "Density ratio cannot exceed (gamma+1)/(gamma-1) = 6 for air.",
            "At Mach 2: pressure ratio 4.5, total-pressure recovery 0.656.",
            "Only compression shocks exist; expansion shocks violate entropy.",
            "Total-pressure loss rises steeply with upstream Mach number.",
            "The relations govern inlets, transonic wing shocks, and bow shocks.",
        ],
        "requirements": [
            "Conservation laws applied across a discontinuity.",
            "The perfect-gas relations with gamma = 1.4.",
            "Total vs static pressure and the entropy condition.",
        ],
        "standards": [
            "Normal-shock tables (e.g., NACA 1135) as reference data.",
            "Total-pressure recovery as the inlet efficiency metric.",
        ],
        "citations": [C_ANDERSON_FUND, C_SHAPIRO, C_BERTIN],
        "sig_lens": (
            "His Signature reading: the normal shock is the air's "
            "signature stamp at supersonic speed - one thin line where the "
            "flow signs away a third of its energy."
        ),
    },
    {
        "key": "oblique_shocks",
        "name": "Oblique Shocks and Expansion Fans: Turning Supersonic Flow",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Supersonic flow cannot turn a corner smoothly - it turns across "
            "an oblique shock (for turning into the flow) or a Prandtl-Meyer "
            "expansion fan (for turning away). The oblique shock sits at an "
            "angle beta to the flow, set by the deflection angle theta and "
            "the Mach number through the theta-beta-Mach relation. Small "
            "deflections give weak shocks with small losses; beyond the "
            "maximum deflection angle the shock detaches and stands off as "
            "a bow shock. Expansion fans are isentropic - no loss at all - "
            "which is why supersonic nozzles and the aft ends of wings use "
            "them. Together, shocks and fans are the complete toolkit for "
            "routing supersonic air around any shape."
        ),
        "how_it_works": (
            "Resolve the upstream Mach into components normal and tangential "
            "to the shock: only the normal component M1n = M1 sin(beta) "
            "changes, obeying the normal-shock relations, while the "
            "tangential component passes through unchanged. The theta-beta-"
            "Mach equation tan(theta) = 2 cot(beta) (M1^2 sin^2(beta) - 1) / "
            "(M1^2 (gamma + cos(2 beta)) + 2) is solved for beta given "
            "theta and M1 (two solutions: weak and strong; nature picks the "
            "weak). For expansions, the Prandtl-Meyer function nu(M) gives "
            "the turning: theta = nu(M2) - nu(M1), with the fan spreading "
            "over the Mach angle mu = arcsin(1/M). Supersonic inlets stack "
            "2-3 oblique shocks to compress with far less loss than one "
            "normal shock."
        ),
        "key_points": [
            "Supersonic flow turns into itself across oblique shocks, away via expansion fans.",
            "Theta-beta-Mach relation sets the shock angle for a given deflection.",
            "Only the normal Mach component changes across the shock.",
            "Beyond max deflection the shock detaches into a bow shock.",
            "Prandtl-Meyer fans are isentropic: turning with zero loss.",
            "Multi-oblique-shock inlets beat single normal shocks on recovery.",
        ],
        "requirements": [
            "The deflection-angle / shock-angle geometry.",
            "Normal/tangential Mach decomposition.",
            "The weak-vs-strong shock selection.",
        ],
        "standards": [
            "Oblique-shock charts and tables (NACA 1135).",
            "Prandtl-Meyer function tabulations.",
        ],
        "citations": [C_ANDERSON_FUND, C_SHAPIRO, C_BERTIN],
        "sig_lens": (
            "His Signature reading: oblique shocks are angled signatures "
            "and expansion fans the air's smooth cursive - together they "
            "write every supersonic turn."
        ),
    },
    {
        "key": "prandtl_glauert",
        "name": "The Prandtl-Glauert Correction: Compressibility at Subsonic Speeds",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Even below Mach 1, compressibility quietly amplifies "
            "aerodynamic forces: as Mach number rises toward 1, pressure "
            "coefficients grow by the Prandtl-Glauert factor 1/sqrt(1 - M^2). "
            "At Mach 0.6 the amplification is 25%; at Mach 0.8 it is 67%. "
            "This is why airliners cruise near Mach 0.78-0.85 and no "
            "faster: the suction peaks on the wing go supersonic locally, "
            "shocks appear, and wave drag erupts. The Prandtl-Glauert rule "
            "applies to thin airfoils at small angles in the linear range; "
            "it also corrects the lift slope (2 pi becomes 2 pi/sqrt(1 - "
            "M^2)) and shifts the aerodynamic center slightly aft. It is "
            "the first and most used compressibility correction in "
            "subsonic design."
        ),
        "how_it_works": (
            "Linearized small-perturbation theory transforms the "
            "compressible potential equation into Laplace's equation by "
            "stretching one coordinate by sqrt(1 - M^2); the pressure "
            "coefficient then scales as Cp = Cp_incompressible / sqrt(1 - "
            "M^2). The correction diverges at M = 1, which correctly "
            "signals the theory's breakdown in the transonic zone. The "
            "critical Mach number - the free-stream Mach at which sonic "
            "flow first appears on the airfoil - follows from the minimum "
            "pressure coefficient: stronger suction peaks mean lower "
            "critical Mach. Supercritical airfoils flatten the upper "
            "surface to weaken the suction peak and push critical Mach "
            "toward 0.75-0.8."
        ),
        "key_points": [
            "Pressure coefficients grow by 1/sqrt(1 - M^2) as Mach rises.",
            "At M 0.8 the amplification is ~67%: the reason cruise stops near M 0.85.",
            "Lift slope becomes 2 pi/sqrt(1 - M^2).",
            "Critical Mach: first sonic point on the airfoil; set by the suction peak.",
            "Supercritical sections flatten the upper surface to delay the shock.",
            "The rule breaks down at transonic speeds - divergence at M = 1 is the warning.",
        ],
        "requirements": [
            "Linearized small-perturbation theory idea.",
            "The pressure coefficient and its incompressible reference.",
            "Critical Mach number and the drag-divergence boundary.",
        ],
        "standards": [
            "Prandtl-Glauert compressibility correction.",
            "Supercritical airfoil design practice.",
        ],
        "citations": [C_ANDERSON_FUND, C_KUETHE, C_BERTIN],
        "sig_lens": (
            "His Signature reading: compressibility is the air "
            "underlining its own signature - the closer to Mach 1, the "
            "bolder the stroke, until the transonic page tears."
        ),
    },
    {
        "key": "sweep_transonic",
        "name": "Sweep and the Transonic Problem: Delaying the Shock",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The transonic problem is simple to state and hard to solve: "
            "between Mach 0.8 and 1.2, patches of supersonic flow and shock "
            "waves appear on the wing, drag spikes (drag divergence), and "
            "shock-induced separation can buffet the airframe. Adolf "
            "Busemann's 1935 insight - sweep the wing and only the Mach "
            "component normal to the leading edge matters - gave the cure: "
            "a 30-degree swept wing at Mach 0.85 sees only Mach 0.74 normal "
            "to its leading edge, delaying shocks and divergence. Swept "
            "wings enabled the jet age; every airliner since the Boeing 707 "
            "wears the solution. The costs are real too: tip stall, "
            "Dutch-roll tendencies, and heavier structure - handled with "
            "twist, fences, and careful taper."
        ),
        "how_it_works": (
            "For an infinite swept wing, the flow decomposes into a normal "
            "component (which the airfoil feels) and a spanwise component "
            "(which it ignores): M_normal = M_infinity x cos(sweep). "
            "Compressibility effects - critical Mach, shock strength, wave "
            "drag - scale with M_normal. Sweeping 35 degrees at Mach 0.85 "
            "drops the effective Mach to 0.70, deep in the well-behaved "
            "subsonic zone. Drag divergence (the Mach where drag suddenly "
            "rises) moves from ~0.7 for straight wings to ~0.85+ for swept "
            "supercritical wings. The trade: sweep moves the tip toward "
            "stall first (spanwise boundary-layer drift), so designers add "
            "washout (twist), leading-edge devices, and sometimes fences."
        ),
        "key_points": [
            "Transonic drag divergence: sudden drag rise from wing shocks near M 0.7-0.85.",
            "Sweep rule: only M x cos(sweep) normal to the leading edge drives compressibility.",
            "30-35 degrees of sweep buys ~0.15 of cruise Mach.",
            "Supercritical airfoils + sweep = the modern airliner wing formula.",
            "Costs: tip-first stall, Dutch roll, structural weight.",
            "Washout, fences, and slats manage the swept wing's vices.",
        ],
        "requirements": [
            "Drag divergence and the transonic drag rise.",
            "The normal-Mach decomposition on a swept wing.",
            "Sweep's penalties and their fixes.",
        ],
        "standards": [
            "Drag-divergence Mach definition (dCD/dM = 0.1).",
            "Supercritical airfoil + sweep design practice.",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_RAYMER],
        "sig_lens": (
            "His Signature reading: sweep is the wing signing at an "
            "angle - the air reads only the normal component, and the "
            "shock arrives late to the appointment."
        ),
    },
    {
        "key": "stall_high_lift",
        "name": "Stall and High-Lift Devices: Flaps, Slats, and the Critical Angle",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "Stall is the wing's hard limit: past the critical angle of "
            "attack (~15 degrees), the upper-surface flow separates and "
            "lift collapses while drag explodes. Because stall speed rises "
            "with the square root of weight over CLmax, landing a heavy "
            "airplane slowly demands more maximum lift - and that is what "
            "high-lift devices deliver. Trailing-edge flaps (plain, split, "
            "slotted, Fowler) add camber and area, raising CLmax from ~1.5 "
            "to 2.5-3.0; leading-edge slats and slots re-energize the "
            "boundary layer, delaying separation to higher angles. A "
            "landing airliner is a shape-shifter: clean wing for cruise, "
            "fully dressed wing - slats out, triple-slotted Fowler flaps "
            "down - for a 130-knot touchdown."
        ),
        "how_it_works": (
            "Flaps increase effective camber, shifting the whole lift curve "
            "up; slotted and Fowler flaps also add chord area and blow the "
            "slot jet over the flap's upper surface to keep it attached. "
            "Slats open a slot at the leading edge that ducts high-energy "
            "air onto the upper surface, raising the stall angle by 5-10 "
            "degrees. Combined, CLmax roughly doubles: Vs drops by ~30%, "
            "so a 200-ton airliner lands near 140 knots instead of 200. The "
            "price is drag - flaps are also airbrakes, which is why "
            "approach is flown with partial flap and full flap only for "
            "the final descent. Stick-shakers and angle-of-attack vanes "
            "warn before the critical angle is reached."
        ),
        "key_points": [
            "Stall: separation past the critical angle; lift drops, drag spikes.",
            "Flaps add camber and area: CLmax 1.5 -> 2.5-3.0.",
            "Slats/slots feed energy to the boundary layer, delaying separation.",
            "High-lift cuts landing speed ~30% for a heavy airplane.",
            "Flaps are also drag devices: approach uses partial settings.",
            "Stall warning (shaker, AoA vane) guards the critical angle.",
        ],
        "requirements": [
            "The stall mechanism: separation from the critical angle.",
            "Flap types and what each adds (camber, area, slot flow).",
            "The Vs ~ 1/sqrt(CLmax) relationship.",
        ],
        "standards": [
            "Certification stall-speed definitions (Vs1g, Vsr).",
            "Takeoff/landing high-lift configuration practice.",
        ],
        "citations": [C_ANDERSON_FLIGHT, C_MCCORMICK, C_RAYMER],
        "sig_lens": (
            "His Signature reading: high-lift devices are the wing "
            "changing its signature for landing - camber deepened, slots "
            "opened, signing slow flight with a bolder hand."
        ),
    },
    {
        "key": "wind_shear_wake",
        "name": "Wind Shear and Wake Turbulence: Hazards in the Air",
        "group": "Compounded",
        "ladder_rank": 8,
        "ladder_tier": "compounded",
        "description": (
            "The air is not always cooperative. Wind shear - a sudden "
            "change of wind speed or direction with position - can rob an "
            "airplane of airspeed in seconds; a microburst's descending "
            "core and spreading outflow first lifts the airplane (headwind "
            "surge) then slams it (tailwind + downdraft), the classic "
            "takeoff/landing killer. Wake turbulence is the other hazard: "
            "the wingtip vortices of a heavy airplane persist for minutes, "
            "sinking and spreading, and a light airplane crossing one can "
            "be rolled past its control authority. Separation standards - "
            "miles and minutes behind heavies - are aerodynamics written "
            "into air-traffic law, and onboard reactive/predictive shear "
            "detection is aerodynamics wired into the cockpit."
        ),
        "how_it_works": (
            "A microburst outflow can change the headwind component by 40+ "
            "knots over a mile: energy analysis shows the airplane loses "
            "both airspeed (tailwind) and altitude (downdraft) faster than "
            "thrust and pitch can compensate - the escape maneuver is full "
            "thrust and target pitch, never chasing airspeed. Wake vortices "
            "descend ~300-500 ft/min initially and decay over 2-3 minutes; "
            "their core tangential speeds scale with weight/(span x speed), "
            "so a heavy at low speed (takeoff/landing) leaves the "
            "strongest wake. Vortex strength is circulation Gamma ~ "
            "L/(rho V b): the same lift at lower speed means a fiercer "
            "vortex. Controllers apply weight-class separation minima "
            "derived directly from these scalings."
        ),
        "key_points": [
            "Wind shear: rapid wind change; microbursts combine tailwind shift with downdraft.",
            "Microburst escape: max thrust, target pitch - never chase the airspeed needle.",
            "Wake vortices persist minutes, sink, and spread behind heavy aircraft.",
            "Vortex strength scales with weight/(span x speed): worst at takeoff/landing.",
            "Separation minima are aerodynamic scalings codified into ATC rules.",
            "Predictive (Doppler) and reactive shear systems guard the cockpit.",
        ],
        "requirements": [
            "How shear changes the airplane's energy state.",
            "Vortex persistence, sink rate, and decay.",
            "The circulation scaling of wake strength.",
        ],
        "standards": [
            "ICAO wake-turbulence separation categories.",
            "Wind-shear escape maneuver procedure.",
        ],
        "citations": [C_MCCORMICK, C_ANDERSON_FLIGHT, C_HOUGHTON],
        "sig_lens": (
            "His Signature reading: shear and wake are the sky's "
            "unsigned hazards - no wing signed them, every pilot reads "
            "them, and the separation rules are the ledger."
        ),
    },
]

ENTRIES += [
    {
        "key": "supersonic_airfoil",
        "name": "Supersonic Airfoil Theory: Thin Wings and Wave Drag",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "At supersonic speeds the elegant subsonic machinery is "
            "replaced by shock-expansion theory: every surface inclination "
            "to the flow produces either an oblique shock (into the flow) "
            "or a Prandtl-Meyer fan (away from it), and the pressure on "
            "each panel follows directly. Ackeret's linearized theory "
            "gives the famous results for a thin flat plate at small angle "
            "alpha: CL = 4 alpha / sqrt(M^2 - 1) and the wave-drag "
            "coefficient CD_wave = 4 alpha^2 / sqrt(M^2 - 1) plus thickness "
            "terms. Wave drag - drag from the shock system's pressure "
            "footprint - is new at supersonic speed and dominates the "
            "drag budget. The diamond airfoil (double wedge) is the "
            "textbook shape: shocks on the forward faces, expansions on "
            "the aft faces, and minimum wave drag for a given thickness "
            "when the maximum thickness sits at mid-chord."
        ),
        "how_it_works": (
            "Apply oblique-shock relations on windward-facing panels and "
            "Prandtl-Meyer on leeward-facing panels; integrate pressures "
            "over the section. Linearizing for small deflections yields "
            "Cp = 2 theta / sqrt(M^2 - 1) per panel (theta positive into "
            "the flow). For a symmetric diamond of thickness ratio tau at "
            "angle alpha, CL = 4 alpha/sqrt(M^2-1) and CD = 4 "
            "(alpha^2 + (tau/2)^2 x shape factor)/sqrt(M^2-1): lift "
            "depends on angle, wave drag on angle squared plus thickness "
            "squared. Because the denominator sqrt(M^2-1) grows with Mach, "
            "wave drag falls as Mach rises past the transonic peak - one "
            "reason cruise Mach 2 was the Concorde's sweet spot. Minimum-"
            "wave-drag thickness placement is mid-chord."
        ),
        "key_points": [
            "Supersonic pressures come from shock-expansion panel analysis.",
            "Ackeret: CL = 4 alpha/sqrt(M^2 - 1) for a thin flat plate.",
            "Wave drag ~ (alpha^2 + thickness^2)/sqrt(M^2 - 1): new drag, dominant at supersonic speed.",
            "Diamond (double-wedge) airfoil: the minimum-wave-drag textbook shape.",
            "Wave drag falls with rising Mach past the transonic peak.",
            "Thickness placement at mid-chord minimizes wave drag.",
        ],
        "requirements": [
            "Oblique-shock and Prandtl-Meyer panel pressures.",
            "The small-deflection linearization.",
            "Wave drag as distinct from friction and induced drag.",
        ],
        "standards": [
            "Ackeret linearized supersonic theory.",
            "Shock-expansion method for arbitrary 2D sections.",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_SHAPIRO],
        "sig_lens": (
            "His Signature reading: supersonic theory is aerodynamics "
            "signed in straight lines - every panel stamps its own shock "
            "or fan, and wave drag is the ink."
        ),
    },
    {
        "key": "area_rule",
        "name": "The Area Rule: Sculpting Wave Drag Away",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "In 1952 Richard Whitcomb discovered that near Mach 1, what "
            "matters is not the wing or the fuselage alone but the total "
            "cross-sectional area distribution of the whole airplane along "
            "its length: wave drag is minimized when that distribution is "
            "smooth, like a Sears-Haack body. A fat wing bulging from a "
            "constant fuselage creates an area spike - and a wave-drag "
            "spike. The fix is the 'Coke-bottle' fuselage: pinch the "
            "fuselage waist where the wing adds area, keeping the total "
            "curve smooth. The F-102, redesigned with area-ruling, went "
            "from subsonic embarrassment to Mach 1.2+; the Convair 990 and "
            "countless airliners wear subtler versions. It remains the "
            "single most cost-effective transonic drag fix ever found."
        ),
        "how_it_works": (
            "Whitcomb's transonic area rule: at Mach ~1 the flow sees the "
            "airplane as a body of revolution with the same longitudinal "
            "area distribution; wave drag follows from that equivalent "
            "body's shape. The Sears-Haack body gives the minimum wave drag "
            "for given length and volume. Designers plot total area vs "
            "station, then indent the fuselage (or add fairings) to remove "
            "bumps at the wing, tail, and engine stations. The supersonic "
            "area rule generalizes it with Mach-plane cuts at the Mach "
            "angle. Wind-tunnel drag-rise measurements confirmed cuts of "
            "25%+ in transonic wave drag on area-ruled designs - a "
            "breakthrough verified before a single line of CFD existed."
        ),
        "key_points": [
            "Near Mach 1, total cross-sectional area distribution sets wave drag.",
            "Smooth Sears-Haack-like area curve = minimum wave drag.",
            "Coke-bottle fuselage: pinch the waist where the wing adds area.",
            "F-102 redesign proved it: subsonic to Mach 1.2+.",
            "Supersonic area rule uses Mach-plane cuts at the Mach angle.",
            "The cheapest transonic drag reduction ever discovered.",
        ],
        "requirements": [
            "The equivalent-body-of-revolution concept.",
            "Reading a longitudinal area-distribution plot.",
            "Sears-Haack minimum-drag shape.",
        ],
        "standards": [
            "Whitcomb transonic area rule (NACA, 1952).",
            "Supersonic area-rule Mach-plane method.",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_RAYMER],
        "sig_lens": (
            "His Signature reading: the area rule is the whole "
            "airplane signing as one body - the wing, fuselage, and "
            "tail co-author a single smooth signature in area."
        ),
    },
    {
        "key": "hypersonic_flow",
        "name": "Hypersonic Flow: Thin Shocks, Hot Gas, Real Chemistry",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Above Mach 5 the air stops behaving like a perfect gas. "
            "Shock layers grow thin and hug the body; the shock heats the "
            "air to thousands of degrees, and oxygen and nitrogen molecules "
            "dissociate - chemistry joins aerodynamics. Newtonian impact "
            "theory (Cp = 2 sin^2(theta)) becomes a useful approximation: "
            "the flow hits the surface like particles and the pressure "
            "depends only on local inclination. Viscous interaction thickens "
            "the boundary layer until it merges with the shock; real-gas "
            "effects change the shock standoff distance; and at the "
            "stagnation point, heating - not drag - sizes the heat shield. "
            "Hypersonics is where aerodynamics, thermodynamics, and "
            "chemistry fuse into one discipline."
        ),
        "how_it_works": (
            "The stagnation temperature ratio T0/T = 1 + (gamma-1)/2 M^2 "
            "gives ~5800 K behind a Mach 10 normal shock in air - hot "
            "enough to dissociate O2 (above ~2000 K) and N2 (above ~4000 "
            "K), absorbing energy and lowering gamma toward 1.1-1.2. "
            "Density ratio climbs past the perfect-gas limit of 6, so the "
            "shock lies closer to the body (thin shock layer). Newtonian "
            "theory predicts pressure from surface angle alone, accurate "
            "within ~10-15% for blunt bodies. Stagnation-point heating "
            "scales roughly as sqrt(rho) V^3 / sqrt(nose radius) "
            "(Fay-Riddell form): blunt noses spread the heat, which is why "
            "re-entry capsules are blunt, not sharp."
        ),
        "key_points": [
            "Hypersonic = above Mach 5; thin shock layers, extreme heating.",
            "High temperatures dissociate air: chemistry changes gamma and shock position.",
            "Newtonian Cp = 2 sin^2(theta): pressure from surface angle alone.",
            "Viscous interaction: boundary layer merges with the shock layer.",
            "Stagnation heating scales ~ sqrt(rho) V^3 / sqrt(nose radius).",
            "Blunt bodies survive re-entry; sharp bodies melt.",
        ],
        "requirements": [
            "Stagnation temperature vs Mach number.",
            "Dissociation and the breakdown of the perfect-gas model.",
            "The heating-rate scaling laws.",
        ],
        "standards": [
            "Fay-Riddell stagnation-point heating correlation.",
            "Newtonian impact theory for pressure estimation.",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_SHAPIRO],
        "sig_lens": (
            "His Signature reading: hypersonics is the signature "
            "written in fire - the air itself changes chemistry to sign "
            "the vehicle's passage."
        ),
    },
    {
        "key": "aircraft_stability",
        "name": "Aircraft Stability: The Weathervane and the Neutral Point",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Stability is the airplane's willingness to return to its "
            "trimmed attitude after a disturbance - the weathervane "
            "effect. Longitudinal static stability requires the center of "
            "gravity ahead of the neutral point (the point where pitching "
            "moment is independent of angle of attack); the distance "
            "between them, as a fraction of chord, is the static margin "
            "(typically 5-15%). A gust pitches the nose up, angle of "
            "attack rises, and with the CG ahead of the neutral point the "
            "tail generates a restoring nose-down moment. Move the CG aft "
            "past the neutral point and the airplane becomes unstable - "
            "which modern fighters do deliberately, using fly-by-wire to "
            "gain agility. Lateral-directional stability adds dihedral "
            "effect (roll from sideslip), weathervane stability (yaw from "
            "sideslip), and the spiral/Dutch-roll modes."
        ),
        "how_it_works": (
            "Write the pitching-moment coefficient about the CG: Cm_CG = "
            "Cm_ac_wing + CL_wing (x_CG - x_ac)/c - tail terms. "
            "Differentiating with angle of attack, static stability needs "
            "dCm/dalpha < 0: a nose-up disturbance must create nose-down "
            "moment. The neutral point is where dCm/dalpha = 0; static "
            "margin = (x_NP - x_CG)/c. The horizontal tail, with its long "
            "moment arm, dominates: tail volume coefficient V_H = (S_t x "
            "l_t)/(S x c) ~ 0.5-1.0 sizes it. Dynamically, the short-period "
            "and phugoid modes describe the oscillation back to trim; "
            "damping comes from pitch rate derivatives. Relaxed stability "
            "(CG near/aft of NP) cuts trim drag and boosts maneuverability "
            "at the cost of requiring active control."
        ),
        "key_points": [
            "Static stability: CG ahead of the neutral point; static margin 5-15% chord.",
            "dCm/dalpha < 0 is the mathematical condition for pitch stability.",
            "The tail's moment arm dominates: tail volume coefficient sizes it.",
            "Dynamic modes: short period (fast, damped) and phugoid (slow exchange of speed/height).",
            "Relaxed/negative stability + fly-by-wire = fighter agility.",
            "Lateral: dihedral effect, weathervane yaw stability, spiral and Dutch-roll modes.",
        ],
        "requirements": [
            "Pitching moment about the CG and its slope with angle of attack.",
            "Neutral point and static margin definitions.",
            "The tail's role as the stabilizing surface.",
        ],
        "standards": [
            "Static-margin design range for conventional aircraft.",
            "Flying-qualities specifications (MIL-STD-1797).",
        ],
        "citations": [C_MCCORMICK, C_ANDERSON_FLIGHT, C_RAYMER],
        "sig_lens": (
            "His Signature reading: the neutral point is where the "
            "airplane signs its own balance sheet - CG ahead and the "
            "signature holds; CG aft and the pilot must co-sign every "
            "second."
        ),
    },
    {
        "key": "control_surfaces",
        "name": "Control Surfaces: Pitch, Roll, and Yaw Authority",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Control is stability's partner: the pilot (or computer) must "
            "be able to command the attitude the stability then holds. "
            "Elevators (or stabilators) pitch the nose by changing the "
            "tail's lift; ailerons roll by differential lift on the wings "
            "(spoilers assist or replace them on many airliners); the "
            "rudder yaws the nose via the vertical tail. Control power "
            "scales with surface area, deflection, and dynamic pressure - "
            "which is why controls feel mushy at low speed and razor-sharp "
            "at high speed, and why hinge moments (the aerodynamic torque "
            "the pilot or actuator must overcome) grow with V^2. Adverse "
            "yaw - the down-going aileron making more drag and yawing the "
            "nose the wrong way - is cured with differential ailerons, "
            "Frise ailerons, or rudder coordination."
        ),
        "how_it_works": (
            "Deflecting a trailing-edge surface changes the section's "
            "effective camber: +20 degrees of elevator adds roughly +0.02 "
            "x 20 of tail lift coefficient per radian-class scaling, and "
            "the tail's long arm converts that to pitching moment. "
            "Control effectiveness derivatives (C_l_delta_a for roll, "
            "C_m_delta_e for pitch, C_n_delta_r for yaw) quantify "
            "authority per degree. Hinge moment H = q x S_c x c_c x C_h "
            "sets actuator sizing; aerodynamic balance (horn, overhang, "
            "sealed gaps) trims C_h. At transonic speeds shock-induced "
            "separation can blank the elevator - the reason for all-moving "
            "stabilators on supersonic aircraft. Fly-by-wire blends the "
            "surfaces: flaperons, elevons, and ruddervators mix the three "
            "axes on tailless and V-tail designs."
        ),
        "key_points": [
            "Elevator/stabilator: pitch; aileron/spoiler: roll; rudder: yaw.",
            "Control power scales with q: mushy slow, sharp fast.",
            "Hinge moments grow with V^2 and size the actuators.",
            "Adverse yaw: down-aileron drag yaws the wrong way; fixed by differential/Frise/coordination.",
            "All-moving tails cure transonic elevator blanking.",
            "Fly-by-wire blends surfaces: elevons, flaperons, ruddervators.",
        ],
        "requirements": [
            "How deflection changes camber and local lift.",
            "Control derivatives per axis.",
            "Hinge moment and aerodynamic balance.",
        ],
        "standards": [
            "Control-power sizing for takeoff rotation and crosswind landing.",
            "Flying-qualities control-authority criteria.",
        ],
        "citations": [C_MCCORMICK, C_RAYMER, C_ANDERSON_FLIGHT],
        "sig_lens": (
            "His Signature reading: control surfaces are the pilot's "
            "pen - every deflection edits the pressure signature, and "
            "the airplane answers in pitch, roll, and yaw."
        ),
    },
    {
        "key": "boundary_layer_control",
        "name": "Boundary-Layer Control: Suction, Blowing, and Laminar Wings",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "If the boundary layer is where drag is born, controlling it "
            "is where drag is killed. Suction through slots or porous "
            "skins removes the slow near-wall fluid, thinning the layer "
            "and delaying both transition and separation - laminar-flow-"
            "control wings have demonstrated 50%+ skin-friction cuts in "
            "flight tests. Blowing (tangential or normal jets) re-"
            "energizes the layer to prevent separation on flaps and "
            "inlets. Vortex generators are the passive version: tiny "
            "vanes that stir high-momentum air down to the wall. The "
            "prize is the natural-laminar-flow wing: shaped so the "
            "pressure falls continuously to 60-70% chord, keeping the "
            "layer laminar with no suction at all - now flying on "
            "business jets and gliders."
        ),
        "how_it_works": (
            "The boundary layer's fate is set by its velocity profile: "
            "suction removes the low-momentum fluid, making the profile "
            "fuller and more resistant to separation and transition. The "
            "suction coefficient C_Q = (suction volume flow)/(V x S) ~ "
            "10^-4 to 10^-3 is enough to hold laminar flow to high "
            "Reynolds numbers. Blowing coefficient C_mu = (jet momentum "
            "flux)/(q x S) ~ 0.01-0.1 can keep flaps attached at extreme "
            "deflections (the blown-flap STOL trick). Vortex generators "
            "shed streamwise vortices that mix the layer at zero power "
            "cost but add their own small drag. Natural laminar flow "
            "needs favorable pressure gradients and smooth, waviness-free "
            "surfaces - insect contamination alone can trip it."
        ),
        "key_points": [
            "Suction thins the layer, delaying transition and separation.",
            "Blowing re-energizes the layer: the blown-flap STOL trick.",
            "Vortex generators: passive mixing, zero power, small drag cost.",
            "Natural laminar flow wings keep laminar to 60-70% chord by shaping alone.",
            "Flight tests show 50%+ friction-drag cuts with active laminar control.",
            "Surface quality is critical: roughness and insects trip laminar flow.",
        ],
        "requirements": [
            "The velocity-profile view of separation resistance.",
            "Suction and blowing coefficients.",
            "Favorable vs adverse pressure gradients.",
        ],
        "standards": [
            "Laminar-flow-control flight-test practice (NASA/industry).",
            "Surface waviness and roughness criteria for NLF.",
        ],
        "citations": [C_SCHLICHTING, C_WHITE, C_RAYMER],
        "sig_lens": (
            "His Signature reading: boundary-layer control is editing "
            "the signature at the source - suction erases the slow "
            "strokes, blowing inks the weak ones, and the laminar wing "
            "writes clean."
        ),
    },
    {
        "key": "helicopter_rotors",
        "name": "Helicopter Rotor Aerodynamics: Hover and Forward Flight",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A helicopter rotor is a rotating wing, and its aerodynamics "
            "blend everything in this database with rotation. In hover, "
            "momentum theory treats the rotor as an actuator disk: thrust "
            "T = 2 rho A v_i^2, so the induced velocity is v_i = sqrt(T / "
            "(2 rho A)) and ideal hover power is T x v_i. Disk loading "
            "(thrust per disk area) sets the downwash violence: a light "
            "helicopter sips power, a heavy-lift rotor blasts the ground. "
            "In forward flight the advancing blade sees V + omega R while "
            "the retreating blade sees V - omega R - dissymmetry of lift "
            "that flapping hinges, cyclic pitch, and lead-lag hinges were "
            "invented to survive. Blade-element theory then integrates "
            "section lift and drag around the azimuth to get real "
            "performance, and the retreating-blade stall plus advancing-"
            "blade compressibility draw the helicopter's speed limit."
        ),
        "how_it_works": (
            "Momentum theory: the disk accelerates a mass flow rho A "
            "(V + v_i) downward; thrust equals mass flow times the "
            "velocity change 2 v_i in hover. Power = T(V + v_i); the "
            "figure of merit FM = ideal power/actual power (~0.7-0.8) "
            "measures rotor efficiency. Blade-element theory slices each "
            "blade into airfoil sections, looks up CL/CD at the local "
            "angle and Mach, and integrates thrust and torque over radius "
            "and azimuth - with flapping angle beta responding to the "
            "lift dissymmetry so the rotor stays level. Ground effect in "
            "hover cuts induced power ~15-25% near the surface. The "
            "vortex-ring state (settling with power) - descending into "
            "one's own downwash - is the rotor's most dangerous "
            "aerodynamic trap."
        ),
        "key_points": [
            "Hover: actuator-disk momentum theory; v_i = sqrt(T/(2 rho A)).",
            "Disk loading sets downwash strength and hover power.",
            "Forward flight: advancing vs retreating blade lift dissymmetry.",
            "Flapping hinges + cyclic pitch keep the rotor disk level.",
            "Blade-element theory integrates section forces over the disk.",
            "Limits: retreating-blade stall, advancing-blade compressibility, vortex-ring state.",
        ],
        "requirements": [
            "Actuator-disk momentum theory.",
            "The advancing/retreating blade velocity field.",
            "Flapping and cyclic pitch as the dissymmetry cure.",
        ],
        "standards": [
            "Figure of merit as rotor hover-efficiency metric.",
            "Vortex-ring-state avoidance criteria.",
        ],
        "citations": [C_MCCORMICK, C_ANDERSON_FLIGHT, C_BERTIN],
        "sig_lens": (
            "His Signature reading: the rotor signs the air in circles "
            "- a spiral signature of downwash, and every blade writes "
            "its line once per revolution."
        ),
    },
    {
        "key": "wind_tunnel",
        "name": "Wind Tunnel Testing: Similitude, Blockage, and Corrections",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The wind tunnel is aerodynamics' laboratory: hold the model "
            "still, move the air, and measure the forces. The founding "
            "rule is dynamic similarity - match Mach number (for "
            "compressibility) and Reynolds number (for viscosity) and the "
            "model's flow reproduces full scale. Closed-circuit tunnels "
            "recirculate the air for efficiency; open-circuit tunnels are "
            "simpler. But walls interfere: blockage (the model + wake "
            "constricting the test section) speeds the flow, and wall "
            "upwash changes the effective angle of attack - so every "
            "tunnel applies blockage and wall corrections. Cryogenic "
            "tunnels chill nitrogen to raise density and hit full-scale "
            "Reynolds numbers on small models; pressurized tunnels do it "
            "with pressure. The tunnel remains the referee that CFD must "
            "satisfy."
        ),
        "how_it_works": (
            "Forces are measured on a sting or strut balance; pressures "
            "through taps and rakes; the flow field with PIV, tufts, and "
            "smoke. Solid blockage epsilon_sb ~ (model volume)/(test "
            "section volume) raises the effective dynamic pressure; wake "
            "blockage adds a drag-proportional term - the corrected q is "
            "q(1 + epsilon). Wall corrections adjust angle of attack and "
            "drag for the tunnel's constraint on the model's induced "
            "flowfield. Reynolds scaling: Re = rho V L/mu, so a 1/10-"
            "scale model needs 10x the density-velocity product - "
            "achieved by pressurization (up to ~10 atm) or cryogenics "
            "(nitrogen at ~100 K). Transonic tunnels use slotted or "
            "porous walls to let the flow breathe through Mach 1."
        ),
        "key_points": [
            "Dynamic similarity: match Mach and Reynolds numbers to match reality.",
            "Blockage corrections fix the walls' speedup of the flow.",
            "Wall corrections fix induced-angle and drag interference.",
            "Pressurized and cryogenic tunnels reach full-scale Reynolds numbers.",
            "Slotted/porous walls make transonic testing possible.",
            "Balances, taps, PIV: the measurement toolkit.",
        ],
        "requirements": [
            "Mach and Reynolds similarity rules.",
            "Solid and wake blockage concepts.",
            "How walls distort the model's flowfield.",
        ],
        "standards": [
            "Standard wind-tunnel correction methods (AGARD).",
            "Reynolds-number reporting for test data.",
        ],
        "citations": [C_BERTIN, C_HOUGHTON, C_ANDERSON_FUND],
        "sig_lens": (
            "His Signature reading: the wind tunnel is where the "
            "signature is rehearsed - a scaled sky, corrected walls, and "
            "the model's pressure field auditioning for flight."
        ),
    },
    {
        "key": "cfd",
        "name": "CFD: Solving the Navier-Stokes Equations on a Grid",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Computational fluid dynamics solves the governing equations "
            "of flow - the Navier-Stokes equations - on a discretized "
            "grid, turning aerodynamics into arithmetic. The workflow is "
            "universal: build the geometry, generate the mesh (fine near "
            "walls where the boundary layer lives, coarser outside), "
            "choose the physics (inviscid Euler, RANS with a turbulence "
            "model, or scale-resolving LES/DNS), set boundary conditions, "
            "iterate to convergence, and validate against tunnel data. "
            "RANS with models like Spalart-Allmaras or k-omega SST is the "
            "industry workhorse: cheap enough for full aircraft, accurate "
            "for attached flow. CFD designed the modern supercritical "
            "wing, optimizes inlets, and predicts store separation - but "
            "it is a model of turbulence, not turbulence itself, so "
            "validation remains mandatory."
        ),
        "how_it_works": (
            "The domain is split into cells; fluxes across faces are "
            "computed from the conserved variables (mass, momentum, "
            "energy). Explicit schemes must respect the CFL condition: "
            "dt < dx/(|V| + a), so information cannot skip a cell per "
            "step; implicit schemes relax this at higher cost per step. "
            "Near walls, the mesh must resolve the viscous sublayer "
            "(y+ ~ 1) or use wall functions. Turbulence models close the "
            "Reynolds-averaged equations by relating eddy viscosity to "
            "mean gradients - the closure problem, CFD's central "
            "approximation. Convergence is judged by residual drops (3-6 "
            "orders) plus flat force histories; grid-convergence studies "
            "(Richardson extrapolation) separate physics from numerics."
        ),
        "key_points": [
            "CFD discretizes Navier-Stokes on a mesh and iterates to a solution.",
            "RANS + turbulence model (SA, k-omega SST) is the industry standard.",
            "CFL condition limits the time step for explicit schemes.",
            "Near-wall resolution (y+ ~ 1) or wall functions handle the boundary layer.",
            "Turbulence closure is the central approximation; validation is mandatory.",
            "Grid-convergence studies separate real physics from numerical error.",
        ],
        "requirements": [
            "The Navier-Stokes equations as the governing laws.",
            "Meshing: resolution where gradients are steep.",
            "The turbulence-closure problem.",
        ],
        "standards": [
            "AIAA CFD verification and validation guidelines.",
            "y+ criteria for wall-resolved vs wall-modeled meshes.",
        ],
        "citations": [C_BERTIN, C_ANDERSON_FUND, C_WHITE],
        "sig_lens": (
            "His Signature reading: CFD is the signature computed "
            "before it is flown - millions of cells voting on the "
            "pressure field, with the tunnel holding the recount."
        ),
    },
    {
        "key": "aeroelasticity",
        "name": "Aeroelasticity: Flutter, Divergence, and Control Reversal",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Aeroelasticity is the three-way coupling of aerodynamic "
            "forces, structural elasticity, and inertia - what happens "
            "when the wing bends under the very loads it creates. "
            "Divergence is the static failure: above a critical dynamic "
            "pressure, twist increases the angle of attack faster than "
            "stiffness can resist, and the wing twists off. Flutter is "
            "the dynamic killer: bending and torsion modes couple through "
            "the unsteady aerodynamics into a self-feeding oscillation "
            "that can destroy a wing in seconds. Control reversal is the "
            "subtle one: the wing twists opposite the aileron command, "
            "and past the reversal speed the roll goes the wrong way. "
            "Every airplane is flutter-cleared by analysis and flight test "
            "to 15% beyond its dive speed - the V-g diagram's red line "
            "is an aeroelastic promise."
        ),
        "how_it_works": (
            "Model the wing section with plunge (bending) and pitch "
            "(torsion) degrees of freedom; unsteady aerodynamic forces "
            "(Theodorsen theory) couple them. Flutter occurs when the "
            "coupled system's damping goes negative at some speed - "
            "energy flows from the airstream into the structure each "
            "cycle. Divergence: q_div ~ (torsional stiffness)/(e x c x "
            "dCL/dalpha x S) - stiffen the wing or move the elastic axis "
            "forward to raise it. Swept wings couple bending into "
            "torsion (wash-in/wash-out), which is why forward-swept "
            "wings diverge so readily. Fixes: mass balance of control "
            "surfaces, stiffness tailoring (aeroelastic tailoring with "
            "composites), and flutter dampers. Flight flutter testing "
            "excites the structure with stick raps or shakers and tracks "
            "damping vs speed."
        ),
        "key_points": [
            "Divergence: static twist-off above a critical dynamic pressure.",
            "Flutter: self-feeding bending-torsion oscillation; can destroy a wing in seconds.",
            "Control reversal: wing twist cancels then reverses aileron authority.",
            "Sweep couples bending and torsion; forward sweep diverges easily.",
            "Cures: stiffness, mass balance, aeroelastic tailoring with composites.",
            "Flutter clearance: analysis plus flight test to 1.15x dive speed.",
        ],
        "requirements": [
            "The bending-torsion coupling mechanism.",
            "Unsteady aerodynamics feeding energy into the structure.",
            "Divergence vs flutter vs reversal distinctions.",
        ],
        "standards": [
            "Flutter clearance requirements (FAR 25.629).",
            "Ground vibration testing for modal data.",
        ],
        "citations": [C_BERTIN, C_RAYMER, C_HOUGHTON],
        "sig_lens": (
            "His Signature reading: aeroelasticity is the signature "
            "arguing with the paper - the wing rewriting its own shape "
            "under load until structure or flutter settles the debate."
        ),
    },
    {
        "key": "propulsion_integration",
        "name": "Propulsion Integration: Inlets, Nozzles, and Afterbodies",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "An engine never flies alone: the inlet must deliver air to "
            "the fan or compressor at the right Mach number, pressure, "
            "and uniformity, and the nozzle must expand the exhaust to "
            "produce thrust - while the airframe around them adds drag. "
            "Subsonic inlets are simple diffusers (area grows, flow slows, "
            "pressure recovers); supersonic inlets are shock systems - "
            "external-compression ramps, mixed-compression designs - that "
            "trade total-pressure recovery against complexity and drag. "
            "Nozzles mirror the logic: convergent for subsonic, convergent-"
            "divergent for supersonic, with variable geometry to match "
            "off-design conditions. Inlet distortion (non-uniform flow "
            "into the fan) can stall the compressor; unstart (a supersonic "
            "inlet spitting its shock system) was the SR-71's famous "
            "violent event. Integration drag - the airframe's penalty for "
            "carrying the propulsion system - is booked to the airplane, "
            "not the engine."
        ),
        "how_it_works": (
            "A subsonic diffuser recovers pressure via Bernoulli: slow "
            "the flow from flight Mach to ~0.4-0.5 at the fan face with "
            "minimal separation (diffusion angle ~5-7 degrees per side). "
            "A Mach 2 mixed-compression inlet uses 2-3 oblique shocks plus "
            "a terminal normal shock for ~0.92 total-pressure recovery vs "
            "~0.72 for a single normal shock. The nozzle expands the flow "
            "to ambient pressure for maximum thrust: underexpanded jets "
            "waste potential, overexpanded jets separate. Variable ramps, "
            "bleed doors, and translating cowls schedule the shock system "
            "across the Mach range. Afterbody drag - the base and boattail "
            "behind the nozzle - is minimized by area-ruling the aft "
            "fuselage around the installed engines."
        ),
        "key_points": [
            "Inlets deliver the right Mach, pressure, and uniformity to the engine.",
            "Subsonic inlets: diffusers; supersonic inlets: managed shock systems.",
            "Multi-shock inlets recover ~0.9 total pressure at Mach 2 vs 0.65 for one normal shock.",
            "Nozzles: convergent subsonic, C-D supersonic, variable geometry for off-design.",
            "Inlet distortion stalls compressors; unstart ejects the supersonic shock system.",
            "Integration drag is charged to the airframe, not the engine.",
        ],
        "requirements": [
            "Diffusion vs shock-compression for pressure recovery.",
            "Nozzle expansion to ambient pressure.",
            "Distortion and unstart as operability limits.",
        ],
        "standards": [
            "Inlet total-pressure recovery and distortion descriptors (ARP 1420).",
            "Nozzle performance bookkeeping (installed vs uninstalled thrust).",
        ],
        "citations": [C_BERTIN, C_SHAPIRO, C_RAYMER],
        "sig_lens": (
            "His Signature reading: propulsion integration is two "
            "signatures sharing one page - the airframe's pressure "
            "field and the engine's, negotiated at the inlet lip."
        ),
    },
    {
        "key": "sonic_boom",
        "name": "Sonic Boom: The N-Wave and Its Reach",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A supersonic airplane drags a cone of compressed air along "
            "its flight path - the Mach cone - and where that cone "
            "sweeps the ground, listeners hear a double thunderclap: the "
            "sonic boom. The pressure signature is the classic N-wave: a "
            "sharp bow-shock rise, a linear fall through the airplane's "
            "length, and a sharp tail-shock return to ambient. Overpressure "
            "is modest - 1-2 pounds per square foot for an airliner-class "
            "vehicle at altitude - but the startle and the rattle broke "
            "windows in the Oklahoma City tests of 1964 and got supersonic "
            "flight over land banned. Boom intensity scales with weight "
            "and inversely with altitude and length: long, light, high "
            "airplanes boom softly. Shaping the area distribution can "
            "round the N into a softer signature - the low-boom design "
            "goal revived by NASA's X-59."
        ),
        "how_it_works": (
            "Whitham's F-function theory propagates the airplane's "
            "equivalent-area distribution along Mach lines to the ground: "
            "nonlinear steepening merges the shocks into the bow/tail "
            "pair of the N-wave. Peak overpressure scales roughly as "
            "(weight/length)^(1/2) x (1/altitude)^(3/4) x Mach factor - "
            "the famous scaling that makes altitude the best boom "
            "reducer. The boom carpet is ~1 mile wide per 1,000 feet of "
            "altitude; maneuvers focus the boom (superboom) where ray "
            "tubes converge. Low-boom shaping tailors the area "
            "distribution so shocks stay spread as a shaped signature "
            "rather than coalescing - targeting perceived loudness "
            "(PLdB) near 75 instead of the Concorde's ~105."
        ),
        "key_points": [
            "The boom is the Mach cone's ground footprint: an N-wave double bang.",
            "Overpressure ~1-2 psf for airliner-class at cruise altitude.",
            "Scales with weight, inversely with altitude and length.",
            "The 1964 Oklahoma City tests led to the overland supersonic ban.",
            "Maneuvers focus booms into superbooms.",
            "Low-boom shaping (X-59) targets ~75 PLdB vs Concorde's ~105.",
        ],
        "requirements": [
            "The Mach cone and its ground intersection.",
            "The N-wave pressure signature shape.",
            "Overpressure scaling with weight, altitude, length.",
        ],
        "standards": [
            "FAA overland supersonic flight restrictions.",
            "Perceived loudness (PLdB) as the low-boom metric.",
        ],
        "citations": [C_ANDERSON_FUND, C_BERTIN, C_KUETHE],
        "sig_lens": (
            "His Signature reading: the boom is the supersonic "
            "signature heard, not seen - an N stamped across the sky "
            "that the ground cannot help but read."
        ),
    },
    {
        "key": "design_integration",
        "name": "Design Integration: The Lift-to-Drag Balance of the Whole Airplane",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Aerodynamics ends where it began - at the whole airplane. "
            "Every topic in this database is a line item in one ledger: "
            "the lift-to-drag ratio L/D, the airplane's aerodynamic "
            "efficiency. Range follows the Breguet equation: range ~ "
            "(V/c) x (L/D) x ln(W_initial/W_final) - speed over fuel "
            "consumption, times L/D, times the logarithm of the weight "
            "fraction burned. Gliders reach L/D of 50-60; airliners 17-20; "
            "supersonic transports ~7-8. The designer trades wing loading "
            "(small wings: fast, efficient cruise, hot landing) against "
            "aspect ratio (long wings: low induced drag, heavy structure), "
            "sweep against stall behavior, and every drag count against "
            "fuel. Aerodynamics does not design the airplane alone - but "
            "no airplane flies well that ignores its ledger."
        ),
        "how_it_works": (
            "Build the drag polar: parasite drag from wetted-area "
            "estimates (equivalent flat-plate area), induced drag from "
            "aspect ratio and Oswald factor, wave drag from Mach and "
            "area ruling, trim drag from stability. The polar's maximum "
            "L/D sets best range speed; the minimum-drag speed sets best "
            "endurance. Size the wing: wing loading W/S sets stall speed "
            "(Vs = sqrt(2(W/S)/(rho CLmax))) and cruise efficiency; "
            "aspect ratio sets the induced-drag floor. Iterate: weight "
            "estimates feed the polar, the polar feeds fuel burn, fuel "
            "feeds weight - the design spiral converges on the airplane. "
            "One drag count (CD = 0.0001) is worth roughly 1% of cruise "
            "fuel on an airliner: aerodynamics is measured in counts."
        ),
        "key_points": [
            "L/D is the airplane's aerodynamic efficiency: gliders 50+, airliners ~18, SSTs ~7.",
            "Breguet range equation: range ~ (V/c)(L/D) ln(W0/W1).",
            "The drag polar sums parasite, induced, wave, and trim drag.",
            "Wing loading sets stall speed; aspect ratio sets induced drag.",
            "The design spiral iterates weight, drag, and fuel to convergence.",
            "One drag count ~= 1% of airliner cruise fuel.",
        ],
        "requirements": [
            "The complete drag-polar buildup.",
            "Breguet range and endurance relationships.",
            "The weight-drag-fuel design spiral.",
        ],
        "standards": [
            "Drag-count bookkeeping in performance analysis.",
            "Conceptual design iteration practice (Raymer).",
        ],
        "citations": [C_RAYMER, C_ANDERSON_FLIGHT, C_MCCORMICK],
        "sig_lens": (
            "His Signature reading: the whole airplane is the final "
            "signature - every record in this database a stroke, the "
            "L/D the legibility, the Breguet range how far it carries."
        ),
    },
]
