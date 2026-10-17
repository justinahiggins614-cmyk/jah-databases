#!/usr/bin/env python3
"""Entries for the Electromagnetics field databases (field #21, taxonomy order).

Verified 2026-10-17: NO database covers electromagnetics as a discipline.
- Manifest-wide regex search (maxwell|transmission.?line|antenna|waveguide|
  smith.?chart|s.?param|radar|magnetostat|electrostat|faraday|ampere|
  gauss.?law|poynting|polariz|friis|dipole|finite.?diff|fdtd|method.?of.?
  moments): zero discipline-level hits across all 2342 databases. The only
  'radar' hits are weather radar inside atmospheric-science/meteorology -
  instruments, not field theory. The existing 'electromagnetism' DB (JAH-EM-,
  10000 records) is purely EM-spectrum band records - whole-index title scan
  for transmission line/maxwell/waveguide/smith chart/s-parameter/magnetostat/
  electrostat/poynting/friis/dipole/antenna/finite-difference = zero hits.
  'electronics' (223) and 'electronics-public' (9) are circuit-level - zero
  hits. 'electrical-electronic-testing' (24) - zero hits.
- Fields #11-20 shard indexes (volcanology, climatology, atmospheric-science,
  hydrology, meteorology, calculus, combinatorics, econometrics,
  psychometrics, turbomachinery) direct whole-shard title scans for
  electromagnet|antenna|maxwell|transmission line|waveguide|smith chart|
  radar cross|friis|magnetostat|electrostat|s.param = zero hits.
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo
  rebuilt 2026-10-17 08:04 UTC, covering fields through #10; fields #11-20
  cross-checked directly above): every record checked + admitted at build
  time.

So this build creates two NEW databases, 37 ladder-ordered records each:

  electromagnetics             - The Electromagnetics Database
                                 (public-harvest: real, fact-checked
                                 electromagnetics; citations Griffiths,
                                 Jackson, Pozar, Balanis, Cheng, Ulaby,
                                 Ramo/Whinnery/Van Duzer, Kraus/Fleisch,
                                 Sadiku, Collin, Harrington, Taflove/Hagness,
                                 Jin, Paul, Skolnik, Orfanidis)
  electromagnetics-signature   - The Electromagnetics Signature Database
                                 (his original Signature interpretation of
                                 the discipline; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

Subtitle disambiguation (fields #13-21 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Maxwell's Equations:
Four Laws, One Universe" and "The Smith Chart: Reading the Circle".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "electromagnetics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_GRIFFITHS = ("Griffiths, David J. 'Introduction to Electrodynamics', 4th "
               "ed. Cambridge University Press, 2017.")
C_JACKSON = ("Jackson, John David. 'Classical Electrodynamics', 3rd ed. "
             "Wiley, 1998.")
C_POZAR = ("Pozar, David M. 'Microwave Engineering', 4th ed. Wiley, 2011.")
C_BALANIS_AEM = ("Balanis, Constantine A. 'Advanced Engineering "
                 "Electromagnetics', 2nd ed. Wiley, 2012.")
C_BALANIS_ANT = ("Balanis, Constantine A. 'Antenna Theory: Analysis and "
                 "Design', 4th ed. Wiley, 2016.")
C_CHENG = ("Cheng, David K. 'Field and Wave Electromagnetics', 2nd ed. "
           "Addison-Wesley, 1989.")
C_ULABY = ("Ulaby, Fawwaz T. and Ravaioli, Umberto. 'Fundamentals of Applied "
           "Electromagnetics', 7th ed. Pearson, 2015.")
C_RAMO = ("Ramo, Simon, Whinnery, John R., and Van Duzer, Theodore. 'Fields "
          "and Waves in Communication Electronics', 3rd ed. Wiley, 1994.")
C_KRAUS = ("Kraus, John D. and Fleisch, Daniel A. 'Electromagnetics with "
           "Applications', 5th ed. McGraw-Hill, 1999.")
C_SADIKU = ("Sadiku, Matthew N. O. 'Elements of Electromagnetics', 7th ed. "
            "Oxford University Press, 2018.")
C_COLLIN = ("Collin, Robert E. 'Foundations for Microwave Engineering', 2nd "
            "ed. Wiley, 2001.")
C_HARRINGTON = ("Harrington, Roger F. 'Time-Harmonic Electromagnetic "
                "Fields'. Wiley-IEEE Press, 2001 (orig. McGraw-Hill, 1961).")
C_TAFLOVE = ("Taflove, Allen and Hagness, Susan C. 'Computational "
             "Electrodynamics: The Finite-Difference Time-Domain Method', "
             "3rd ed. Artech House, 2005.")
C_JIN = ("Jin, Jian-Ming. 'The Finite Element Method in Electromagnetics', "
         "3rd ed. Wiley, 2014.")
C_PAUL = ("Paul, Clayton R. 'Introduction to Electromagnetic Compatibility', "
          "2nd ed. Wiley, 2006.")
C_SKOLNIK = ("Skolnik, Merrill I. 'Introduction to Radar Systems', 3rd ed. "
             "McGraw-Hill, 2008.")
C_ORFANIDIS = ("Orfanidis, Sophocles J. 'Electromagnetic Waves and Antennas'. "
               "Rutgers University, 2016.")

ENTRIES = [
    {
        "key": "what_is_electromagnetics",
        "name": "What Electromagnetics Is: The Science of Fields That Fill Space",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Electromagnetics is the study of electric and magnetic fields - "
            "the invisible infrastructure on which the modern world runs. "
            "Every radio broadcast, cell call, radar sweep, power grid, "
            "electric motor, MRI scan, and beam of sunlight is a sentence "
            "written in the language of Maxwell's equations. The discipline "
            "has three great territories. Statics: charges at rest make "
            "electric fields (electrostatics); steady currents make magnetic "
            "fields (magnetostatics) - the realm of capacitors, magnets, and "
            "DC machines. Dynamics: time-varying fields couple to each other "
            "and launch waves - the realm of radio, light, and optics. "
            "Guided and radiated systems: transmission lines, waveguides, "
            "antennas, radar, and high-frequency circuits - the realm where "
            "fields are engineered into devices. The ladder of this database "
            "climbs in that order: sources make fields, fields obey boundary "
            "rules, changing fields make waves, and waves are guided, "
            "radiated, and put to work."
        ),
        "how_it_works": (
            "Electric charge is the source. A charge at rest fills the space "
            "around it with an electric field E; a charge in motion - a "
            "current - adds a magnetic field B. The two fields are not "
            "separate citizens: a changing magnetic field induces an "
            "electric field (Faraday's law, the principle of every "
            "generator), and a changing electric field induces a magnetic "
            "field (the displacement-current term, Maxwell's own addition). "
            "Coupled together, the fields sustain each other and propagate "
            "as a wave at the speed of light - which is why light IS an "
            "electromagnetic wave. Engineers shape these fields with "
            "conductors (which force E perpendicular to their surface), "
            "dielectrics (which store electric energy), magnetic materials "
            "(which channel magnetic flux), and geometry - lines, guides, "
            "and antennas that tell waves where to go and where to leave."
        ),
        "key_points": [
            "Electromagnetics studies electric and magnetic fields; charge is the source of both, through rest (E) and motion (B).",
            "Time-varying E and B couple to each other - this coupling is what makes electromagnetic waves, including light, possible.",
            "The discipline divides into statics (capacitors, magnets), dynamics (waves, polarization, propagation), and engineered systems (lines, guides, antennas, radar).",
            "Maxwell's equations are the complete rulebook: four equations that predict everything from static attraction to fiber optics.",
            "Nearly every modern technology - communications, power, sensing, computing hardware - is applied electromagnetics.",
        ],
        "requirements": [
            "No prior background needed - this is the first rung of the ladder.",
            "Comfort with the idea that empty space can carry invisible fields.",
            "Basic arithmetic; the mathematics builds gently from here.",
        ],
        "standards": [
            "Terminology follows Griffiths: field, flux, source, boundary condition.",
            "SI units throughout: volts per meter for E, tesla for B, coulomb for charge.",
        ],
        "citations": [C_GRIFFITHS, C_ULABY, C_SADIKU],
        "sig_lens": (
            "Signature take: the field is the Signature medium - invisible, "
            "everywhere, and obedient to law. His Signature framing treats "
            "every charge as a broadcaster and every field as the message: "
            "electromagnetics is the study of how the universe talks to "
            "itself across empty space."
        ),
    },
    {
        "key": "coulomb_law",
        "name": "Coulomb's Law: The Force Between Charges, and the Birth of the Field",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Coulomb's law is the founding measurement of electromagnetics: "
            "the force between two point charges is proportional to the "
            "product of the charges and inversely proportional to the square "
            "of the distance between them, directed along the line joining "
            "them. In symbols, F = (1 / 4 pi epsilon_0) * q1 * q2 / r^2, "
            "where epsilon_0 = 8.854 x 10^-12 farads per meter is the "
            "permittivity of free space and the constant 1 / 4 pi epsilon_0 "
            "is about 9 x 10^9 newton-square-meters per square coulomb. Like "
            "charges repel, opposite charges attract, and the inverse-square "
            "form - shared with gravity - is what makes the mathematics of "
            "fields close so beautifully. Superposition extends the law to "
            "any charge distribution: the total force is the vector sum of "
            "the pairwise forces, and from that sum the entire edifice of "
            "electrostatics is built."
        ),
        "how_it_works": (
            "Place charge q1 at the origin and q2 at distance r. Each charge "
            "experiences a force along the line between them with magnitude "
            "k * |q1 q2| / r^2, repulsive if the signs match, attractive if "
            "they differ. Halve the distance and the force quadruples; "
            "double one charge and the force doubles. For continuous charge "
            "distributions the law becomes an integral: break the "
            "distribution into infinitesimal charges dq, apply Coulomb's law "
            "to each pair, and add the vectors. The electric field is then "
            "defined as force per unit test charge, E = F / q, so that "
            "Coulomb's law reads as a field law: a point charge q produces "
            "E = k q / r^2 directed radially outward. The field exists "
            "whether or not a second charge is there to feel it."
        ),
        "key_points": [
            "Coulomb's law: F = k q1 q2 / r^2 along the line joining the charges, with k = 1 / 4 pi epsilon_0 ~ 9 x 10^9 N m^2/C^2.",
            "Like charges repel, opposite charges attract; force scales with the product of charges and the inverse square of distance.",
            "Superposition: the force from many charges is the vector sum of the pairwise Coulomb forces.",
            "Dividing by a test charge turns the force law into a field law: E = k q / r^2 radially from a point charge.",
            "The inverse-square form is the deep reason Gauss's law and the 1/r potential take their simple forms.",
        ],
        "requirements": [
            "Arithmetic with scientific notation and squared distances.",
            "Vector intuition: forces have direction, and directions add as vectors.",
            "The 'what electromagnetics is' record, or equivalent orientation.",
        ],
        "standards": [
            "epsilon_0 = 8.854187817 x 10^-12 F/m (exact by SI definition of the ampere era; CODATA value used).",
            "Sign convention: repulsive force positive along the separation vector for like charges.",
        ],
        "citations": [C_GRIFFITHS, C_SADIKU, C_CHENG],
        "sig_lens": (
            "Signature take: Coulomb's law is the Signature handshake - "
            "every charge announces itself to every other charge across "
            "space, louder when near, whispering with distance. His framing "
            "treats the inverse square as nature's volume knob."
        ),
    },
    {
        "key": "efield_gauss",
        "name": "The Electric Field and Gauss's Law: Flux Through Closed Surfaces",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The electric field E is force per unit charge: place a tiny test "
            "charge anywhere in space and E tells you which way it gets "
            "pushed and how hard, in newtons per coulomb (equivalently volts "
            "per meter). Field lines visualize it: they begin on positive "
            "charge, end on negative charge, never cross, and crowd together "
            "where the field is strong. Gauss's law is the field's accounting "
            "rule: the total outward flux of E through ANY closed surface "
            "equals the charge enclosed divided by epsilon_0. In symbols, the "
            "surface integral of E dot dA over a closed surface = Q_enclosed "
            "/ epsilon_0. It is one of Maxwell's four equations, and for "
            "symmetric charge distributions - spheres, infinite lines, "
            "infinite planes - it hands you the field in one line of algebra "
            "instead of a page of integration."
        ),
        "how_it_works": (
            "Choose a closed 'Gaussian surface' that matches the symmetry of "
            "the charge. For a point charge q, take a sphere of radius r: E "
            "is radial and uniform over the sphere, so flux = E * 4 pi r^2 = "
            "q / epsilon_0, giving E = q / 4 pi epsilon_0 r^2 - Coulomb's law "
            "recovered. For an infinite line charge with linear density "
            "lambda, take a coaxial cylinder: flux = E * 2 pi r L = lambda L "
            "/ epsilon_0, so E = lambda / 2 pi epsilon_0 r, falling as 1/r "
            "rather than 1/r^2. For an infinite sheet with surface density "
            "sigma, a pillbox surface gives E = sigma / 2 epsilon_0, "
            "independent of distance - the field of a charged plane is "
            "uniform. The differential form, divergence of E = rho / "
            "epsilon_0, says the same thing locally: electric field lines "
            "diverge outward from positive charge density."
        ),
        "key_points": [
            "The electric field E is force per unit charge (N/C = V/m); field lines start on positive charge and end on negative charge.",
            "Gauss's law: outward flux of E through any closed surface = enclosed charge / epsilon_0.",
            "Symmetry turns Gauss's law into a one-line field solver: spheres give 1/r^2, lines give 1/r, sheets give constant fields.",
            "The differential form (div E = rho / epsilon_0) is Maxwell's first equation: charge density is the source of electric flux.",
            "Flux depends only on enclosed charge - charges outside the surface contribute zero net flux.",
        ],
        "requirements": [
            "Coulomb's law and the field concept from the previous records.",
            "Basic integral intuition: flux = field times area when uniform and perpendicular.",
            "Recognizing spherical, cylindrical, and planar symmetry.",
        ],
        "standards": [
            "Flux sign convention: outward normal is positive; enclosed positive charge gives positive net flux.",
            "Gaussian surface is a mathematical construction - it need not coincide with any physical object.",
        ],
        "citations": [C_GRIFFITHS, C_CHENG, C_ULABY],
        "sig_lens": (
            "Signature take: Gauss's law is the Signature audit - no matter "
            "what surface you draw, the books balance: flux out equals "
            "charge within. His framing treats every closed surface as a "
            "ledger that charge cannot cheat."
        ),
    },
    {
        "key": "potential_voltage",
        "name": "Electric Potential and Voltage: The Landscape Charges Slide Down",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Electric potential V is the electric field's 'height map': a "
            "scalar, measured in volts, defined so that moving a charge q "
            "through a potential difference costs or yields energy q times "
            "delta-V. Where the field E is a vector at every point, the "
            "potential is a single number at every point, and the field is "
            "its downhill slope: E = -gradient of V. A point charge q makes "
            "V = k q / r, a 1/r hill (or valley) in space. Equipotential "
            "surfaces - contours of constant V - always cut field lines at "
            "right angles, and conductors in electrostatic equilibrium are "
            "entire equipotential volumes: no field inside, all excess charge "
            "on the surface. Voltage is simply potential difference, and "
            "nearly every circuit concept - batteries, grounds, node "
            "voltages - is bookkeeping on this landscape."
        ),
        "how_it_works": (
            "Potential is defined by the line integral V(b) - V(a) = - "
            "integral of E dot dl from a to b: the work per unit charge done "
            "BY the field moving from a to b, with a sign flip. Because "
            "electrostatic fields are conservative (curl of E = 0), the "
            "integral is path-independent and V is well-defined. For a point "
            "charge, integrating E = k q / r^2 radially inward from infinity "
            "(where V = 0 by convention) gives V = k q / r. Potentials "
            "superpose as scalars - far easier than vector field addition - "
            "and the field is recovered by differentiation: E = -grad V, "
            "pointing downhill on the potential landscape. Poisson's "
            "equation, Laplacian of V = -rho / epsilon_0, turns charge "
            "distributions directly into potential maps, which is how most "
            "real electrostatic problems are actually solved."
        ),
        "key_points": [
            "Potential V is energy per unit charge (volts); E = -grad V, so the field points downhill on the potential landscape.",
            "A point charge makes V = k q / r; potentials add as scalars, which is far easier than adding field vectors.",
            "Voltage is potential difference; moving charge q through delta-V changes its energy by q delta-V.",
            "Equipotentials are perpendicular to field lines; conductors in equilibrium are equipotential volumes with no internal field.",
            "Poisson's equation (Laplacian V = -rho / epsilon_0) converts charge maps into potential maps.",
        ],
        "requirements": [
            "The electric field and Gauss's law records.",
            "Gradient intuition: the slope of a hill points downhill; E is the slope of V.",
            "Line-integral intuition: adding up field along a path.",
        ],
        "standards": [
            "Reference convention: V = 0 at infinity for localized charge distributions.",
            "Sign convention: positive work done BY the field lowers the potential energy qV.",
        ],
        "citations": [C_GRIFFITHS, C_SADIKU, C_KRAUS],
        "sig_lens": (
            "Signature take: potential is the Signature terrain - an "
            "invisible landscape draped over space, and every charge is a "
            "marble rolling on it. His framing treats voltage as altitude: "
            "circuits are just plumbing on this hillside."
        ),
    },
    {
        "key": "capacitance",
        "name": "Capacitance: Storing Electric Energy Between Plates",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A capacitor is two conductors held apart, and capacitance C is "
            "the measure of how much charge separation it takes to build a "
            "given voltage: C = Q / V, in farads. The parallel-plate "
            "capacitor - area A, separation d - has C = epsilon A / d, and it "
            "is the workhorse geometry: charge +Q on one plate and -Q on the "
            "other makes a nearly uniform field E = sigma / epsilon between "
            "them, storing energy W = (1/2) C V^2 = (1/2) Q V in the field "
            "itself. Capacitors are everywhere: power-supply filters that "
            "smooth rectified AC, timing elements with resistors, DC blocks "
            "that pass AC signals, energy reservoirs in camera flashes and "
            "defibrillators, and the memory cells of DRAM (one tiny capacitor "
            "per bit). Series and parallel combinations follow the "
            "mirror-image rules of resistors: series adds reciprocally, "
            "parallel adds directly."
        ),
        "how_it_works": (
            "Connect a battery across the plates: charge flows until the "
            "plates' voltage equals the battery's, with +Q facing -Q across "
            "the gap. The field between the plates is nearly uniform, "
            "E = V / d, and building it up required work - charging a "
            "capacitor from 0 to V against its own rising voltage integrates "
            "to (1/2) C V^2, energy now parked in the electric field "
            "occupying the gap. Insert a dielectric and the capacitance "
            "grows by the relative permittivity epsilon_r (2 to 10 for most "
            "solids, ~80 for water), because the material's molecules "
            "polarize and partially cancel the plates' field, letting more "
            "charge on for the same voltage. In AC circuits the capacitor's "
            "impedance is 1 / j omega C - an open circuit at DC, nearly a "
            "short at high frequency - which is why capacitors couple "
            "signals while blocking DC bias."
        ),
        "key_points": [
            "Capacitance C = Q / V (farads); parallel plates give C = epsilon A / d.",
            "Stored energy W = (1/2) C V^2 lives in the electric field between the plates, not in the metal.",
            "Dielectrics multiply capacitance by epsilon_r via molecular polarization.",
            "AC impedance 1 / j omega C: blocks DC, passes high frequencies - the basis of coupling and filtering.",
            "Series: 1/C adds; parallel: C adds - the mirror image of resistor rules.",
        ],
        "requirements": [
            "Electric field, potential, and voltage records.",
            "Algebra with area, distance, and the permittivity constant.",
            "Willingness to think of energy as stored in empty space between plates.",
        ],
        "standards": [
            "Capacitor schematic symbol: two parallel lines (one curved for polarized/electrolytic).",
            "Voltage rating and dielectric breakdown field are safety-critical specifications.",
        ],
        "citations": [C_ULABY, C_SADIKU, C_GRIFFITHS],
        "sig_lens": (
            "Signature take: the capacitor is the Signature reservoir - a "
            "still pond of electric pressure between two shores. His framing "
            "treats every capacitor as stored intent: charge held apart, "
            "waiting for permission to reunite."
        ),
    },
    {
        "key": "current_ohm",
        "name": "Electric Current and Ohm's Law: Charge in Motion",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Electric current is charge in motion: I = dQ / dt, in amperes, "
            "with the microscopic picture carried by current density J "
            "(amperes per square meter), the vector field of flowing charge. "
            "In conductors, J = sigma E - the local Ohm's law - where sigma "
            "is conductivity; the familiar V = I R is its integrated form "
            "for a uniform wire, with resistance R = L / sigma A. Drift "
            "velocities are humiliatingly slow (millimeters per second in "
            "copper at household currents) - the signal travels at near light "
            "speed because the FIELD propagates, not the electrons. Moving "
            "charge does work: P = V I = I^2 R = V^2 / R is the power turned "
            "into heat, the reason wires have current ratings and the reason "
            "power is transmitted at high voltage (same power, less current, "
            "far less I^2 R loss)."
        ),
        "how_it_works": (
            "Apply voltage across a conductor: the field E inside pushes the "
            "free electrons, which accelerate, collide with the lattice, and "
            "settle at a steady drift velocity v_d, giving J = n q v_d with "
            "n the free-electron density. Collisions randomize the motion and "
            "dump the gained energy as heat - that is resistance, "
            "microscopically. For ohmic materials sigma is constant, so J is "
            "proportional to E, and integrating over a wire of length L and "
            "cross-section A gives V = I L / sigma A, i.e. V = I R. "
            "Kirchhoff's current law (charge conservation at a node: what "
            "flows in flows out) plus Ohm's law is the complete engine of DC "
            "circuit analysis. In AC, resistance generalizes to impedance, "
            "but the power bookkeeping P = V I remains."
        ),
        "key_points": [
            "Current I = dQ/dt (amperes); current density J is the vector field of flowing charge, with J = sigma E locally.",
            "Ohm's law V = I R, with R = L / sigma A for a uniform wire; microscopically, resistance is electron-lattice collisions.",
            "Electrons drift at mm/s - signals travel near light speed because the field propagates.",
            "Power P = V I = I^2 R becomes heat; high-voltage transmission minimizes I^2 R loss.",
            "Kirchhoff's current law (charge conservation) plus Ohm's law solves DC circuits.",
        ],
        "requirements": [
            "Charge, field, and potential records.",
            "Basic algebra; unit comfort with volts, amps, ohms, watts.",
            "No calculus needed - the microscopic picture is descriptive.",
        ],
        "standards": [
            "Conventional current: defined as flow of positive charge, opposite the electron drift.",
            "Resistor color codes and power ratings follow IEC 60062 conventions.",
        ],
        "citations": [C_ULABY, C_SADIKU, C_KRAUS],
        "sig_lens": (
            "Signature take: current is the Signature river - charge flowing "
            "downhill through the copper canyon, slow as individuals, swift "
            "as a wave. His framing treats every circuit as a watershed: "
            "voltage is the elevation, current the flow."
        ),
    },
    {
        "key": "biot_savart_ampere",
        "name": "Magnetic Fields from Currents: Biot-Savart and Ampere's Law",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Moving charge makes magnetic fields: every current element I dl "
            "contributes dB = (mu_0 / 4 pi) I dl cross r-hat / r^2 - the "
            "Biot-Savart law - with field lines curling around the wire by "
            "the right-hand rule. Ampere's law is the magnetic twin of "
            "Gauss's law: the line integral of B dot dl around ANY closed "
            "loop equals mu_0 times the current threading the loop. For "
            "symmetric currents it is a one-line solver: an infinite straight "
            "wire gives B = mu_0 I / 2 pi r, circling the wire and falling as "
            "1/r; a solenoid's interior field is nearly uniform, B = mu_0 n "
            "I, the basis of electromagnets. The constant mu_0 = 4 pi x 10^-7 "
            "henries per meter sets the magnetic strength scale, and "
            "together with epsilon_0 it fixes the speed of light."
        ),
        "how_it_works": (
            "Point the thumb of the right hand along the current; the "
            "fingers curl in the direction of B. Biot-Savart integrates "
            "these contributions: for the infinite wire, the integral over "
            "all current elements yields B = mu_0 I / 2 pi r purely "
            "azimuthal - no radial or axial component. Ampere's law gets "
            "there faster: draw a circular Amperian loop of radius r around "
            "the wire, B is tangent and uniform on it, so B * 2 pi r = mu_0 "
            "I. Stack loops into a solenoid and the exterior fields cancel "
            "while interior fields add, giving the uniform B = mu_0 n I "
            "inside (n = turns per meter). The differential form, curl of B "
            "= mu_0 J (for steady currents), is Maxwell's magnetostatic "
            "equation: current density is the source of magnetic curl."
        ),
        "key_points": [
            "Biot-Savart: dB = (mu_0/4 pi) I dl x r-hat / r^2; field lines circle the current by the right-hand rule.",
            "Ampere's law: closed line integral of B dot dl = mu_0 x current through the loop.",
            "Infinite wire: B = mu_0 I / 2 pi r azimuthal; solenoid: B = mu_0 n I uniform inside.",
            "mu_0 = 4 pi x 10^-7 H/m; with epsilon_0 it determines the speed of light.",
            "Differential form curl B = mu_0 J is the magnetostatic Maxwell equation: currents source magnetic curl.",
        ],
        "requirements": [
            "Current and current-density concepts from the Ohm's law record.",
            "Cross-product intuition: perpendicular to both inputs, right-hand rule.",
            "Line-integral intuition: adding up field along a loop.",
        ],
        "standards": [
            "B in tesla; 1 T = 10,000 gauss (cgs unit still common in magnetics).",
            "Right-hand rule is the universal sign convention for current-to-field direction.",
        ],
        "citations": [C_GRIFFITHS, C_CHENG, C_SADIKU],
        "sig_lens": (
            "Signature take: the current is the Signature spindle - charge in "
            "motion spinning an invisible whirlpool around itself. His "
            "framing treats every wire as a tiny tornado factory, its "
            "strength tallied by Ampere's loop."
        ),
    },
    {
        "key": "lorentz_force",
        "name": "The Lorentz Force: How Fields Push Moving Charge",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The Lorentz force law, F = q(E + v cross B), is the bridge "
            "between fields and matter: it says exactly how electric and "
            "magnetic fields push a charge q moving at velocity v. The "
            "electric part qE pushes along the field and does work; the "
            "magnetic part q v cross B pushes perpendicular to BOTH the "
            "velocity and the field, so magnetic forces bend trajectories "
            "without ever doing work (no energy change, only direction "
            "change). A charge entering a uniform B field perpendicularly "
            "spirals in a circle of radius r = m v / q B - the cyclotron "
            "principle behind mass spectrometers and particle accelerators. "
            "The same law drives every electric motor (current-carrying "
            "conductors pushed sideways in a magnetic field) and every "
            "generator run in reverse, and crossed E and B fields make "
            "velocity selectors and the Hall effect."
        ),
        "how_it_works": (
            "Decompose the motion: E accelerates charge along itself, "
            "changing speed; B provides a centripetal-style sideways push "
            "proportional to the perpendicular velocity component. With E = "
            "0 and v perpendicular to uniform B, the magnetic force is "
            "always perpendicular to v with magnitude q v B, so the charge "
            "executes uniform circular motion: q v B = m v^2 / r gives r = "
            "m v / q B, and the orbital frequency omega = q B / m - the "
            "cyclotron frequency, independent of speed (nonrelativistically). "
            "In a motor, the 'moving charges' are conduction electrons in "
            "rotor windings; the Lorentz force on each length element is "
            "I L cross B, and the geometry turns those pushes into torque. "
            "In the Hall effect, the magnetic deflection piles charge on one "
            "side of a conductor until its electric field balances the "
            "magnetic push - the resulting Hall voltage measures B or "
            "carrier density."
        ),
        "key_points": [
            "Lorentz force F = q(E + v x B): electric part does work along E; magnetic part bends motion perpendicular to v and B, doing no work.",
            "Uniform B gives circular motion with radius r = m v / q B and cyclotron frequency omega = q B / m.",
            "Electric motors are Lorentz force on current-carrying conductors (F = I L x B) converted to torque.",
            "Crossed E and B fields select velocity (v = E/B passes undeflected) - the principle of mass spectrometers.",
            "The Hall effect converts magnetic deflection into a measurable voltage for sensing B or carrier density.",
        ],
        "requirements": [
            "Electric and magnetic field concepts; cross-product direction sense.",
            "Circular-motion basics: centripetal force m v^2 / r.",
            "Current as moving charge (the Ohm's law record).",
        ],
        "standards": [
            "Charge sign matters: electrons bend opposite to positive charges in the same B field.",
            "Motor/generator duality: the same geometry generates emf when moved or produces force when driven.",
        ],
        "citations": [C_GRIFFITHS, C_ULABY, C_KRAUS],
        "sig_lens": (
            "Signature take: the Lorentz force is the Signature steering "
            "law - the electric hand pushes forward, the magnetic hand "
            "steers sideways. His framing treats every motor as a choreography "
            "of these two hands on rivers of charge."
        ),
    },
    {
        "key": "magnetic_materials",
        "name": "Magnetic Materials: Domains, Hysteresis, and Permanent Magnets",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Most magnetism in matter comes from atomic-scale current loops - "
            "electron orbits and spins - whose alignment is described by the "
            "magnetization M; the total field is B = mu_0 (H + M), where H is "
            "the field from free currents alone. Ferromagnets (iron, nickel, "
            "cobalt, and their alloys) keep M aligned in microscopic domains, "
            "and an applied H marches the domain walls until the material "
            "saturates; removing H leaves remanent magnetization, and "
            "reversing H traces the famous hysteresis loop, whose area is "
            "energy lost as heat per cycle. Soft magnetic materials (narrow "
            "loop, low coercivity) are transformer and motor cores - they "
            "must re-magnetize 50/60 times a second cheaply. Hard materials "
            "(wide loop, high coercivity: alnico, ferrites, neodymium-iron-"
            "boron) are permanent magnets that resist demagnetization. "
            "Permeability mu = B/H (often thousands of mu_0 in soft iron) "
            "measures how eagerly a material channels magnetic flux."
        ),
        "how_it_works": (
            "Start with unmagnetized iron: domains point every which way, "
            "net M = 0. Apply H: favorably-oriented domains grow at the "
            "expense of others (domain-wall motion), then whole domains "
            "rotate into alignment - B climbs steeply, then saturates when "
            "every atomic moment points along H. Reduce H to zero: walls "
            "don't fully retreat (they snag on defects), leaving remanence "
            "B_r - this is how permanent magnets are born. Apply reverse H "
            "to coercivity H_c to erase the magnetization; drive H through a "
            "full cycle and the B-H curve encloses the hysteresis loop. Each "
            "traversal dissipates the loop's area as heat - the reason "
            "transformer cores use grain-oriented silicon steel with the "
            "narrowest affordable loop, and the reason high-frequency cores "
            "switch to ferrites (ceramic, low eddy-current loss)."
        ),
        "key_points": [
            "B = mu_0 (H + M): H from free currents, M from atomic alignment; permeability mu = B/H measures flux-channeling eagerness.",
            "Ferromagnetic domains align with applied H via wall motion then rotation, saturating at full alignment.",
            "Hysteresis loop: remanence B_r (memory at zero H), coercivity H_c (field needed to erase); loop area = energy lost per cycle.",
            "Soft magnets (narrow loop) for transformer/motor cores; hard magnets (wide loop: ferrite, NdFeB) for permanent magnets.",
            "Eddy currents in cores waste power as heat - laminated steel or ferrite cores suppress them.",
        ],
        "requirements": [
            "Magnetic field and Ampere's law concepts.",
            "Hysteresis intuition: systems with memory don't retrace their path.",
            "Energy-area connection: loop area has units of energy density.",
        ],
        "standards": [
            "B-H curves are measured per IEC 60404; core loss quoted in W/kg at specified B and frequency.",
            "Magnet grades (e.g. N52 NdFeB) specify remanence and maximum energy product.",
        ],
        "citations": [C_GRIFFITHS, C_CHENG, C_KRAUS],
        "sig_lens": (
            "Signature take: the ferromagnet is the Signature memory metal - "
            "domains like tiny compasses that remember where they were "
            "pointed. His framing treats hysteresis as the material's diary: "
            "every loop a page, its area the price of remembering."
        ),
    },
    {
        "key": "faraday_lenz",
        "name": "Faraday's Law and Lenz's Law: Electricity from Changing Magnetism",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Faraday's law: a changing magnetic flux through a loop induces "
            "an electromotive force around it, emf = -d Phi_B / dt, where "
            "Phi_B is the magnetic flux (B dot area). The minus sign is "
            "Lenz's law: the induced current flows in the direction that "
            "OPPOSES the change - nature resists. This is the operating "
            "principle of civilization's power supply: rotate a coil in a "
            "magnetic field (or rotate the field around the coil) and out "
            "comes alternating current; every generator, transformer "
            "(changing flux in the primary induces voltage in the "
            "secondary), induction stove, wireless charger, and guitar "
            "pickup is Faraday's law at work. The differential form, curl of "
            "E = -partial B / partial t, is Maxwell's third equation: a "
            "time-varying magnetic field IS a circulating electric field."
        ),
        "how_it_works": (
            "Thread a coil of N turns and area A with B(t) = B_0 sin(omega "
            "t): flux Phi = N A B_0 sin(omega t), and emf = -d Phi/dt = -N A "
            "B_0 omega cos(omega t) - sinusoidal voltage at the same "
            "frequency, amplitude growing with turns, area, field strength, "
            "and frequency. Drop a magnet through a copper tube and Lenz's "
            "law shows itself dramatically: the falling flux induces "
            "currents whose field repels the magnet, braking its fall "
            "(eddy-current braking, used in trains and roller coasters). In "
            "a transformer, the primary's AC magnetizes the core; the "
            "secondary sees d Phi/dt and develops V2 = V1 * N2/N1. Because "
            "the induced E field circles (non-conservative - no potential "
            "can describe it), Faraday's law is the first place the tidy "
            "electrostatic world breaks open into dynamics."
        ),
        "key_points": [
            "Faraday's law: emf = -d Phi_B / dt around any loop; Lenz's law (the minus sign) makes induced effects oppose the change.",
            "Generators, transformers, induction heating, wireless charging, and guitar pickups all run on Faraday's law.",
            "Induced emf scales with turns N, area A, field B_0, and frequency omega: emf amplitude = N A B_0 omega.",
            "Eddy-current braking (magnet falling through copper tube) is Lenz's law made visible.",
            "Differential form curl E = -dB/dt: changing B IS a circulating E field - the break from electrostatics into dynamics.",
        ],
        "requirements": [
            "Magnetic flux intuition: B times area, counting field lines through a loop.",
            "Time derivatives: faster change means larger induced emf.",
            "The Lorentz force record (motional emf is the same physics).",
        ],
        "standards": [
            "Transformer voltage ratio V2/V1 = N2/N1 (ideal); polarity dots mark winding sense.",
            "Faraday's law in integral form is the basis of IEC definitions of induced voltage.",
        ],
        "citations": [C_GRIFFITHS, C_ULABY, C_CHENG],
        "sig_lens": (
            "Signature take: Faraday's law is the Signature echo - a "
            "changing magnetic field shouts, and the electric field answers "
            "in a circle. His framing treats every generator as a "
            "conversation between motion and magnetism, with Lenz enforcing "
            "politeness: the answer always pushes back."
        ),
    },
    {
        "key": "inductance",
        "name": "Inductance: Storing Energy in Magnetic Fields",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Inductance L is the magnetic twin of capacitance: where a "
            "capacitor stores energy in an electric field, an inductor "
            "stores it in a magnetic field. Defined by flux linkage per "
            "current, L = N Phi / I, in henries; a long solenoid gives L = "
            "mu N^2 A / l, growing with the square of the turns. The stored "
            "energy is W = (1/2) L I^2, parked in the B field threading the "
            "coil. Inductors oppose CHANGES in current (V = L dI/dt - "
            "Faraday's law across the coil's own turns), which makes them "
            "the flywheel of circuits: chokes that block AC while passing "
            "DC, energy-storage elements in switching power supplies, tuning "
            "coils paired with capacitors in radios, and the field windings "
            "of motors and generators. Mutual inductance M between two coils "
            "is the coupling that makes transformers work."
        ),
        "how_it_works": (
            "Drive current I through N turns: each turn's flux Phi threads "
            "all N turns, so the total flux linkage is N Phi = L I. Change "
            "the current and Faraday's law induces V = -L dI/dt across the "
            "coil - the inductor fights the change, which is why current "
            "through an inductor cannot jump instantaneously. In an RL "
            "circuit the current rises toward V/R with time constant tau = "
            "L/R, the magnetic dual of the RC time constant. Energy "
            "accounting: pushing current from 0 to I against the "
            "back-emf integrates to (1/2) L I^2, now stored in the field "
            "occupying the coil's volume (energy density B^2 / 2 mu). Open a "
            "switch on an inductive circuit and the collapsing field drives "
            "whatever voltage it takes to keep current flowing - the "
            "inductive kick that sparks relay contacts and demands flyback "
            "diodes."
        ),
        "key_points": [
            "Inductance L = N Phi / I (henries); solenoid L = mu N^2 A / l - turns count twice.",
            "Stored energy W = (1/2) L I^2 lives in the magnetic field, dual to the capacitor's (1/2) C V^2.",
            "V = L dI/dt: inductors oppose current changes; current through an inductor cannot change instantaneously.",
            "RL time constant tau = L/R; AC impedance j omega L: passes DC, blocks high frequencies.",
            "Mutual inductance M couples coils - the transformer principle; unclamped switching causes inductive kickback.",
        ],
        "requirements": [
            "Faraday's law (induction is the mechanism).",
            "Magnetic flux and solenoid field from the Ampere record.",
            "Capacitance record for the duality framing.",
        ],
        "standards": [
            "Inductor schematic: coiled loops; dot convention marks mutual-inductance winding sense.",
            "Saturation current rating: beyond it the core saturates and inductance collapses.",
        ],
        "citations": [C_ULABY, C_GRIFFITHS, C_SADIKU],
        "sig_lens": (
            "Signature take: the inductor is the Signature flywheel - "
            "current as momentum, the magnetic field as the spinning mass "
            "that refuses to stop. His framing treats every coil as "
            "stubbornness wound in copper: try to change the current, and "
            "it pushes back."
        ),
    },
    {
        "key": "maxwell_equations",
        "name": "Maxwell's Equations: Four Laws, One Universe",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Maxwell's equations are the complete rulebook of classical "
            "electromagnetics - four equations that contain Coulomb's law, "
            "Ampere's law, Faraday's law, and the absence of magnetic "
            "monopoles, plus Maxwell's own stroke of genius, the "
            "displacement current. In differential form: div E = rho / "
            "epsilon_0 (charge sources electric flux); div B = 0 (no magnetic "
            "charge - field lines always close); curl E = -partial B / "
            "partial t (changing B makes circulating E); curl B = mu_0 J + "
            "mu_0 epsilon_0 partial E / partial t (currents AND changing E "
            "make circulating B). The integral forms say the same with flux "
            "through surfaces and circulation around loops. From these four "
            "lines follow: charge conservation, the wave equation, the speed "
            "of light c = 1 / sqrt(mu_0 epsilon_0), and every antenna, fiber, "
            "and chip ever built."
        ),
        "how_it_works": (
            "The equations split into two pairs. The divergence pair "
            "constrains the fields' sources at every instant: electric field "
            "lines begin/end on charge; magnetic field lines never begin or "
            "end. The curl pair constrains their dynamics: each equation "
            "says a changing field of one kind curls around as the other "
            "kind. Couple them - let E change, which makes B curl, which "
            "changes, which makes E curl - and the disturbance propagates "
            "instead of staying put: take the curl of the curl equations in "
            "empty space and each field obeys the wave equation with speed "
            "1 / sqrt(mu_0 epsilon_0), which evaluates to 299,792,458 m/s. "
            "Maxwell computed this from purely electrical measurements and "
            "recognized the number: light is an electromagnetic wave. "
            "Boundary conditions (the next rung) tell the equations how to "
            "behave at material interfaces, completing the system."
        ),
        "key_points": [
            "Four equations: Gauss (electric), Gauss (magnetic: div B = 0), Faraday, Ampere-Maxwell - in differential or integral form.",
            "Divergence equations name the sources: charge for E, nothing (no monopoles) for B.",
            "Curl equations couple the fields' time derivatives: changing B makes circulating E, changing E makes circulating B.",
            "The coupling predicts waves at c = 1 / sqrt(mu_0 epsilon_0) - Maxwell's identification of light.",
            "Charge conservation (div J = -partial rho / partial t) is built into the equations, not an extra assumption.",
        ],
        "requirements": [
            "All statics records (Gauss, Ampere, Faraday) - Maxwell's equations are their union plus one term.",
            "Divergence/curl intuition: sources/sinks vs circulation.",
            "Readiness for the single most concentrated statement in the database.",
        ],
        "standards": [
            "SI (rationalized MKSA) form used throughout; Gaussian-cgs variants appear in older texts like Jackson's early editions.",
            "Time-harmonic phasor form (curl E = -j omega B, etc.) is the engineering working form for sinusoidal steady state.",
        ],
        "citations": [C_GRIFFITHS, C_JACKSON, C_CHENG, C_BALANIS_AEM],
        "sig_lens": (
            "Signature take: Maxwell's equations are the Signature "
            "constitution - four articles governing every spark, signal, "
            "and sunbeam. His framing treats Maxwell's addition of the "
            "displacement current as the single most daring pencil stroke "
            "in physics: a term added for symmetry that turned out to be "
            "light."
        ),
    },
]

ENTRIES += [
    {
        "key": "displacement_current",
        "name": "Displacement Current: The Term That Makes Light Possible",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The displacement current is Maxwell's own addition to Ampere's "
            "law: the term mu_0 epsilon_0 partial E / partial t, which says "
            "a changing electric field acts as a source of magnetic field "
            "exactly as a conduction current does. Maxwell added it for "
            "consistency - without it, Ampere's law contradicts charge "
            "conservation whenever charge piles up, as on a charging "
            "capacitor's plates - and the payoff was enormous: the new term "
            "completes the E-B coupling symmetry, and the coupled equations "
            "immediately predict self-sustaining waves. Between a charging "
            "capacitor's plates there is no conduction current, yet the "
            "magnetic field circles as if there were, because the growing E "
            "field between the plates IS the current. Every radio wave ever "
            "transmitted crosses empty space on displacement current alone."
        ),
        "how_it_works": (
            "Charge a capacitor with current I: conduction current flows in "
            "the wires, but between the plates there is vacuum. Apply "
            "Ampere's law with a surface spanning the loop that passes "
            "between the plates: no conduction current pierces it, yet the "
            "loop integral of B is nonzero - paradox, until the displacement "
            "term is included. The charge Q on the plates grows as dQ/dt = "
            "I, the field E = Q / epsilon_0 A grows with it, and the "
            "displacement current I_d = epsilon_0 d Phi_E / dt = dQ/dt = I "
            "exactly equals the wire current - the 'current' continues "
            "through the gap as changing field. In a propagating wave the "
            "same term alternates with Faraday's: changing E makes B, "
            "changing B makes E, leapfrogging through space with no charges "
            "anywhere. The continuity equation div J + partial rho / "
            "partial t = 0 is satisfied only because this term exists."
        ),
        "key_points": [
            "Displacement current density J_d = epsilon_0 partial E / partial t; it sources magnetic field like conduction current.",
            "Between charging capacitor plates, I_d exactly equals the wire current - the paradox that forced Maxwell's addition.",
            "The term restores charge conservation to Ampere's law and completes the E-B coupling symmetry.",
            "In free-space waves, displacement current alone carries the 'current' - no charges needed.",
            "In materials the term generalizes with D: partial D / partial t includes polarization currents.",
        ],
        "requirements": [
            "Maxwell's equations record - this is the deep dive on the fourth term.",
            "Capacitor charging picture (charge piles on plates).",
            "Partial-derivative intuition: how fast the field changes in time.",
        ],
        "standards": [
            "In phasor form the displacement term becomes j omega D - a susceptance-like contribution.",
            "Displacement current is not charge motion; calling it 'current' is historical - it is changing flux.",
        ],
        "citations": [C_GRIFFITHS, C_JACKSON, C_BALANIS_AEM],
        "sig_lens": (
            "Signature take: displacement current is the Signature ghost "
            "current - no charges move, yet the magnetic field feels a "
            "current anyway. His framing treats it as Maxwell's wager that "
            "symmetry outranks intuition - and the wager paid off as light."
        ),
    },
    {
        "key": "boundary_conditions",
        "name": "Boundary Conditions: What Fields Do at Material Interfaces",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Maxwell's equations rule the interior of each material, but "
            "real problems are patchworks - air against glass, copper "
            "against dielectric - and boundary conditions are the laws at "
            "the seams. Four rules: the normal component of D jumps by the "
            "free surface charge (D2n - D1n = rho_s); the tangential "
            "component of E is continuous (E1t = E2t); the normal component "
            "of B is continuous (B1n = B2n); the tangential component of H "
            "jumps by the free surface current (H1t - H2t = J_s). At a "
            "perfect conductor, E_tangential must vanish (charges move "
            "instantly to kill it), so static E meets metal at right angles "
            "and time-varying fields reflect. These four seam-laws, applied "
            "at every interface, are what make reflection, refraction, "
            "waveguides, and shielding calculable."
        ),
        "how_it_works": (
            "Derive them with pillboxes and loops: shrink a Gaussian "
            "pillbox across the interface and only the normal flux through "
            "its faces survives, giving the D-normal rule; shrink an "
            "Amperian loop across the interface and only the tangential "
            "circulation along its long sides survives, giving the "
            "E-tangential and H-tangential rules. At a dielectric interface "
            "with no free charge or current: D normal continuous "
            "(epsilon_1 E1n = epsilon_2 E2n - the E-field bends away from the "
            "normal (toward the interface) entering the higher-permittivity "
            "medium), E tangential "
            "continuous, B normal continuous, H tangential continuous. At a "
            "perfect electric conductor: E_t = 0 and B_n = 0 just outside "
            "(any tangential E would drive infinite surface current), with "
            "surface charge rho_s = D_n and surface current J_s = n cross H "
            "appearing to satisfy the jumps. Every Fresnel coefficient, "
            "waveguide mode, and shielding calculation starts here."
        ),
        "key_points": [
            "Four seam-laws: D_n jumps by rho_s; E_t continuous; B_n continuous; H_t jumps by J_s.",
            "At a perfect conductor, tangential E and normal B vanish just outside; surface charge/current absorb the jumps.",
            "Dielectric interface: E_tangential continuous, D_normal continuous - fields refract at the seam.",
            "Derived by shrinking Gaussian pillboxes and Amperian loops across the interface.",
            "Boundary conditions turn Maxwell's equations into solvable problems at every material seam.",
        ],
        "requirements": [
            "Maxwell's equations in integral form (flux and circulation).",
            "D and H fields: D = epsilon E, B = mu H in linear media.",
            "The conductors record (why free charge moves to cancel internal fields).",
        ],
        "standards": [
            "Perfect electric conductor (PEC) is the idealization: infinite conductivity, zero internal field.",
            "Surface impedance boundary condition generalizes PEC for good (not perfect) conductors.",
        ],
        "citations": [C_GRIFFITHS, C_CHENG, C_BALANIS_AEM],
        "sig_lens": (
            "Signature take: boundary conditions are the Signature customs "
            "law - every field crossing a border must declare itself, and "
            "the normal and tangential components go through separate "
            "checkpoints. His framing treats each interface as a negotiation "
            "between two materials, refereed by Maxwell."
        ),
    },
    {
        "key": "wave_equation",
        "name": "The Wave Equation: How Maxwell's Equations Predict Light",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Take the curl of Faraday's law, substitute the Ampere-Maxwell "
            "law, and use the vector identity for curl of curl: in a "
            "charge-free, current-free region each field obeys Laplacian of "
            "E = mu epsilon partial^2 E / partial t^2 - the wave equation. "
            "Its solutions are disturbances that propagate without changing "
            "shape at speed v = 1 / sqrt(mu epsilon). In vacuum, mu_0 and "
            "epsilon_0 give v = 299,792,458 m/s - the measured speed of "
            "light, computed from purely electrical constants. This was "
            "Maxwell's thunderclap: light is an electromagnetic wave, and "
            "the entire spectrum from radio to gamma rays is the same "
            "phenomenon at different frequencies. In materials the speed "
            "drops to c / n, where n = sqrt(mu_r epsilon_r) is the refractive "
            "index - the reason glass bends light."
        ),
        "how_it_works": (
            "Start with curl E = -partial B / partial t. Take the curl of "
            "both sides: curl curl E = -partial (curl B) / partial t. In "
            "free space curl B = mu_0 epsilon_0 partial E / partial t, so "
            "the right side becomes -mu_0 epsilon_0 partial^2 E / partial "
            "t^2. The vector identity curl curl E = grad(div E) - Laplacian "
            "E, with div E = 0 in free space, leaves Laplacian E = mu_0 "
            "epsilon_0 partial^2 E / partial t^2. Try a plane wave E = E_0 "
            "cos(kz - omega t): the Laplacian gives -k^2 E, the time "
            "derivative gives -omega^2 E, so the equation demands k^2 = mu_0 "
            "epsilon_0 omega^2, i.e. omega / k = 1 / sqrt(mu_0 epsilon_0) = "
            "c. The wave number k = 2 pi / lambda and omega = 2 pi f give "
            "the universal c = lambda f. Any waveform - pulses, modulated "
            "carriers - is a superposition of such plane waves."
        ),
        "key_points": [
            "In source-free regions Maxwell's equations reduce to the wave equation for E and B separately.",
            "Wave speed v = 1 / sqrt(mu epsilon); in vacuum this equals the measured speed of light.",
            "Plane wave E_0 cos(kz - omega t) satisfies the equation exactly when omega / k = c.",
            "The relation c = lambda f ties every frequency to its wavelength across the whole EM spectrum.",
            "In materials v = c / n with n = sqrt(mu_r epsilon_r) - refraction and slow-wave effects follow.",
        ],
        "requirements": [
            "Maxwell's equations and the displacement-current record.",
            "Second-derivative intuition: curvature in space tied to acceleration in time.",
            "Wave intuition: a shape that moves without changing.",
        ],
        "standards": [
            "c = 299,792,458 m/s exactly (SI defining constant since 1983).",
            "Time-harmonic form: Helmholtz equation (Laplacian + k^2) E = 0 with k = omega sqrt(mu epsilon).",
        ],
        "citations": [C_GRIFFITHS, C_JACKSON, C_ULABY],
        "sig_lens": (
            "Signature take: the wave equation is the Signature drumhead - "
            "strike the electromagnetic field anywhere and the ripple "
            "travels at exactly c, no faster, no slower. His framing treats "
            "every light beam as Maxwell's equations humming a single note."
        ),
    },
    {
        "key": "plane_waves",
        "name": "Plane Waves in Free Space: E, H, and the Speed of Light",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The plane wave is the hydrogen atom of electromagnetics: the "
            "simplest exact wave solution, and the building block of all "
            "others. A uniform plane wave has E and H perpendicular to each "
            "other and both perpendicular to the direction of propagation - "
            "a purely transverse wave - with the fixed ratio E / H = eta_0 "
            "= sqrt(mu_0 / epsilon_0) ~ 377 ohms, the intrinsic impedance of "
            "free space. Write it as E = x-hat E_0 cos(omega t - k z), H = "
            "y-hat (E_0 / eta_0) cos(omega t - k z): the fields oscillate in "
            "step, in phase, carrying energy forward at c. Any real wave - "
            "spherical waves from antennas, guided waves in cables - can be "
            "decomposed into plane waves (Fourier optics, angular spectrum), "
            "so mastering this one solution unlocks the rest. The 377-ohm "
            "ratio also foreshadows transmission lines: wave impedances are "
            "the field-theory cousins of characteristic impedances."
        ),
        "how_it_works": (
            "Assume E = x-hat E_x(z, t), no charges or currents: the wave "
            "equation gives E_x = E_0 cos(omega t - k z) with k = omega / c. "
            "Faraday's law curl E = -partial B / partial t then forces a "
            "magnetic field: the only nonzero curl component is partial E_x "
            "/ partial z = k E_0 sin(omega t - k z), so partial B_y / "
            "partial t = -that, integrating to B_y = (k / omega) E_0 cos(...) "
            "= E_0 / c cos(...) - in phase with E. With H = B / mu_0, the "
            "ratio E_x / H_y = mu_0 c = sqrt(mu_0 / epsilon_0) = eta_0. "
            "Physically: the changing E makes B (displacement current), the "
            "changing B makes E (Faraday), and they march in lockstep - "
            "neither leads, neither lags. The triad (E, H, propagation "
            "direction) is right-handed: point fingers along E, curl toward "
            "H, thumb gives the power flow."
        ),
        "key_points": [
            "Uniform plane wave: E perpendicular to H perpendicular to propagation - purely transverse, right-handed triad.",
            "Fixed ratio E/H = eta_0 ~ 377 ohms, the intrinsic impedance of free space; E and H oscillate in phase.",
            "Fields: E = E_0 cos(omega t - k z), H = (E_0 / eta_0) cos(omega t - k z) for z-propagation.",
            "Every wave decomposes into plane waves (Fourier/angular-spectrum view) - this solution is the universal building block.",
            "Wave impedance eta foreshadows the transmission-line characteristic impedance Z_0.",
        ],
        "requirements": [
            "The wave-equation record.",
            "Cross-product handedness (E cross H points along propagation).",
            "Cosine-wave comfort: amplitude, phase, in-step oscillation.",
        ],
        "standards": [
            "eta_0 = 376.730313... ohms (from the exact c and defined mu_0 era constants).",
            "Phasor notation E(z) = x-hat E_0 e^{-j k z} is the engineering shorthand for time-harmonic plane waves.",
        ],
        "citations": [C_ULABY, C_CHENG, C_GRIFFITHS],
        "sig_lens": (
            "Signature take: the plane wave is the Signature march - E and "
            "H stepping in perfect time, 377 ohms apart, advancing at c. "
            "His framing treats it as the simplest possible agreement "
            "between the electric and magnetic fields: equal partners, "
            "neither leading."
        ),
    },
    {
        "key": "polarization",
        "name": "Polarization: The Shape Traced by the Electric Field",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Polarization describes the path the tip of the E-field vector "
            "traces in the plane perpendicular to propagation, watched at a "
            "fixed point as time passes. Three cases: linear (E oscillates "
            "along a fixed line - the components in x and y are in phase), "
            "circular (equal amplitudes, 90 degrees out of phase - the tip "
            "sweeps a circle, right- or left-handed), and elliptical (the "
            "general case: unequal amplitudes or arbitrary phase - the tip "
            "sweeps an ellipse). Sunlight is unpolarized (random), skylight "
            "is partially polarized (why polarized sunglasses cut glare), "
            "and engineers choose deliberately: FM radio uses circular "
            "polarization so car antennas work at any orientation; satellite "
            "links use circular to defeat Faraday rotation in the "
            "ionosphere; radar uses polarization diversity to distinguish "
            "targets. Polarizers, wave plates, and Brewster's angle are the "
            "optical hardware of this idea."
        ),
        "how_it_works": (
            "Write E = x-hat E_x0 cos(omega t) + y-hat E_y0 cos(omega t + "
            "delta). If delta = 0 or pi, the y-component is always a fixed "
            "multiple of the x-component: the tip moves on a straight line - "
            "linear polarization at angle arctan(E_y0 / E_x0). If E_x0 = "
            "E_y0 and delta = +/- pi/2, then E = E_0 (x-hat cos omega t -/+ "
            "y-hat sin omega t): the tip circles at angular frequency omega, "
            "right-handed for one sign, left-handed for the other (IEEE "
            "convention: thumb along propagation, fingers curl with E "
            "rotation as time advances). Anything else gives an ellipse "
            "with axial ratio E_major / E_minor. A linear wave is the sum of "
            "a right- and left-circular wave; quarter-wave plates convert "
            "between linear and circular by delaying one component 90 "
            "degrees. Antennas only fully receive the polarization they "
            "transmit - cross-polarized antennas lose nearly all the "
            "signal (polarization mismatch factor)."
        ),
        "key_points": [
            "Polarization = the E-tip's path: linear (in-phase components), circular (equal, 90 deg apart), elliptical (general).",
            "Circular handedness follows the IEEE convention; linear = sum of two opposite circular waves.",
            "Engineers choose: circular for mobile/satellite links (orientation-proof), dual-polarization for radar and capacity doubling.",
            "Polarized sunglasses and Brewster's angle exploit the same physics as antenna polarization.",
            "Polarization mismatch between antennas can cost the entire link - matched polarization is a link-budget line item.",
        ],
        "requirements": [
            "Plane-wave record (transverse E and H).",
            "Phase-difference intuition: two oscillations 90 degrees apart trace a circle.",
            "Right-hand rule for handedness.",
        ],
        "standards": [
            "IEEE Std 145: polarization handedness defined with thumb along propagation direction.",
            "Axial ratio (major/minor axis, in dB) quantifies circular-polarization purity.",
        ],
        "citations": [C_BALANIS_AEM, C_ULABY, C_ORFANIDIS],
        "sig_lens": (
            "Signature take: polarization is the Signature dance step - the "
            "electric field can march straight, waltz in circles, or swing "
            "in ellipses. His framing treats every antenna as a dance "
            "partner that must know the steps, or the signal never arrives."
        ),
    },
    {
        "key": "poynting_vector",
        "name": "The Poynting Vector: Where the Electromagnetic Energy Goes",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Poynting vector S = E cross H is the energy-flow meter of "
            "electromagnetics: watts per square meter, pointing in the "
            "direction power travels. For a plane wave it gives the "
            "familiar time-averaged intensity <S> = E_0^2 / 2 eta_0 - a 1 "
            "V/m field carries about 1.33 milliwatts per square meter. The "
            "Poynting theorem is the energy-conservation law of fields: the "
            "outward flux of S through a closed surface plus the rate of "
            "increase of stored field energy inside equals minus the power "
            "delivered to charges (J dot E) - the books always balance. "
            "Solar panels, radio link budgets, microwave-oven heating "
            "patterns, and antenna gain definitions all run on Poynting "
            "arithmetic: follow S and you follow the power."
        ),
        "how_it_works": (
            "Take the dot product of Faraday's law with H and of the "
            "Ampere-Maxwell law with E, subtract, and apply a vector "
            "identity: div(E cross H) + partial u / partial t = -J dot E, "
            "where u = (1/2)(epsilon E^2 + mu H^2) is the field energy "
            "density. Integrate over a volume: the surface integral of S "
            "dot dA (power leaving) plus d/dt of stored energy equals the "
            "power the fields do on charges inside. For the z-propagating "
            "plane wave, E cross H = z-hat E_0 H_0 cos^2(omega t - kz); "
            "time-averaging cos^2 to 1/2 gives <S> = z-hat E_0^2 / 2 eta_0. "
            "Integrate <S> over a receiving antenna's effective aperture and "
            "you get the received power - the Friis equation is Poynting "
            "accounting at a distance. Reactive power sloshes as the "
            "imaginary part of the complex Poynting vector in phasor form."
        ),
        "key_points": [
            "S = E x H (W/m^2) points along power flow; plane-wave average <S> = E_0^2 / 2 eta_0.",
            "Poynting theorem: power out through a surface + stored-energy growth = -power delivered to charges.",
            "Field energy density u = (1/2)(epsilon E^2 + mu H^2) splits evenly between E and H in a plane wave.",
            "Link budgets, solar irradiance, and antenna effective aperture are all Poynting arithmetic.",
            "Phasor form splits S into real (propagating) and imaginary (reactive, sloshing) power.",
        ],
        "requirements": [
            "Plane-wave record (E/H ratio, in-phase fields).",
            "Energy-density intuition from the capacitor/inductor records.",
            "Dot/cross product comfort.",
        ],
        "standards": [
            "Solar constant ~1361 W/m^2 is a Poynting flux measurement at Earth's orbit.",
            "Antenna gain is defined via radiated power density (Poynting flux) relative to isotropic.",
        ],
        "citations": [C_GRIFFITHS, C_BALANIS_AEM, C_ULABY],
        "sig_lens": (
            "Signature take: the Poynting vector is the Signature "
            "cash-flow statement - every watt the fields move is tracked, "
            "and the theorem is the audit. His framing treats energy "
            "bookkeeping as the discipline's conscience: nothing appears "
            "or vanishes, it only flows."
        ),
    },
    {
        "key": "lossy_media_skin",
        "name": "Waves in Lossy Media: Skin Depth and the Good Conductor",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "In a conductor, the wave equation gains a conductivity term and "
            "the propagation constant becomes complex, gamma = alpha + j "
            "beta: the wave still oscillates (beta) but now decays "
            "exponentially (alpha) as it penetrates. The skin depth delta = "
            "sqrt(2 / omega mu sigma) is the distance over which the field "
            "falls to 1/e (~37%) - in copper at 1 MHz it is about 66 "
            "micrometers; at 60 Hz it is about 8.5 millimeters. Consequences "
            "are everywhere: AC current crowds into a thin skin of every "
            "wire (raising AC resistance far above DC resistance), "
            "microwave currents live in the plating of waveguides, magnetic "
            "shielding works by absorption within a few skin depths, and "
            "induction heating dumps power exactly in the skin layer. A "
            "'good conductor' (sigma >> omega epsilon) has alpha ~ beta ~ "
            "1/delta; seawater and soil sit in between, which is why "
            "submarines use extremely low frequencies."
        ),
        "how_it_works": (
            "With conduction current J = sigma E, the Ampere-Maxwell law "
            "gives curl H = (sigma + j omega epsilon) E in phasor form - "
            "conductivity joins permittivity as a complex epsilon_c = "
            "epsilon - j sigma/omega. The Helmholtz equation then has "
            "k_c^2 = omega^2 mu epsilon_c, complex. For a good conductor "
            "the sigma term dominates: gamma = sqrt(j omega mu sigma) = "
            "(1 + j) sqrt(omega mu sigma / 2), so alpha = beta = "
            "sqrt(omega mu sigma / 2) = 1/delta. The wave E_0 e^{-z/delta} "
            "e^{-j z/delta} decays within a few dozen micrometers in copper "
            "at radio frequencies - fields essentially live on surfaces, "
            "which is why hollow waveguides and thin plating work. Power "
            "dissipated per volume is (1/2) sigma |E|^2: the decaying field "
            "deposits its energy as heat in the skin, the basis of induction "
            "furnaces. Loss tangent tan(delta) = sigma / omega epsilon "
            "classifies every material from lossless dielectric to good "
            "conductor."
        ),
        "key_points": [
            "Complex propagation constant gamma = alpha + j beta: oscillation plus exponential decay into conductors.",
            "Skin depth delta = sqrt(2 / omega mu sigma): 1/e penetration distance (~66 um in copper at 1 MHz).",
            "AC resistance exceeds DC resistance because current crowds into the skin - critical for power and RF design.",
            "Shielding by absorption: each skin depth attenuates ~8.7 dB; a few skin depths make an effective shield.",
            "Loss tangent sigma / omega epsilon classifies materials; seawater/soil force ELF/VLF for subsurface links.",
        ],
        "requirements": [
            "Wave equation and plane-wave records.",
            "Complex-number comfort: real part = decay, imaginary part = oscillation.",
            "Conductivity from the Ohm's law record.",
        ],
        "standards": [
            "Copper conductivity 5.8 x 10^7 S/m (annealed, 20 C) is the reference for skin-depth tables.",
            "Litz wire (many insulated strands) defeats skin effect below ~1 MHz; plating suffices above.",
        ],
        "citations": [C_ULABY, C_CHENG, C_BALANIS_AEM],
        "sig_lens": (
            "Signature take: skin depth is the Signature tide line - the "
            "wave is allowed only ankle-deep into good conductors. His "
            "framing treats every copper surface as a shoreline where "
            "fields break and spend themselves as heat."
        ),
    },
    {
        "key": "fresnel_reflection",
        "name": "Reflection and Transmission at a Boundary: The Fresnel Coefficients",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "When a wave meets an interface, boundary conditions split it: "
            "part reflects, part transmits, with amplitudes set by the "
            "Fresnel coefficients. At normal incidence the reflection "
            "coefficient is Gamma = (eta_2 - eta_1) / (eta_2 + eta_1), where "
            "eta is the wave impedance - for nonmagnetic dielectrics this "
            "is (n_1 - n_2)/(n_1 + n_2) in refractive indices. Air to glass "
            "(n = 1.5) reflects 4% of the power - the faint ghost in every "
            "window - while air to metal reflects essentially 100%. Power "
            "conservation demands R + T = 1 (reflectance plus transmittance), "
            "and at oblique incidence the coefficients split by polarization "
            "(TE vs TM), with TM reflection vanishing at Brewster's angle. "
            "Anti-reflection coatings, radomes, stealth shaping, and every "
            "impedance-matching network are Fresnel engineering: choose the "
            "interface so the reflected wave cancels."
        ),
        "how_it_works": (
            "Write incident, reflected, and transmitted plane waves at the "
            "z = 0 interface and enforce E_tangential and H_tangential "
            "continuity. At normal incidence: E_i + E_r = E_t and H_i - H_r "
            "= H_t (the reflected H flips because propagation reverses), "
            "with H = E / eta in each medium. Solving gives E_r / E_i = "
            "(eta_2 - eta_1)/(eta_2 + eta_1) = Gamma and E_t / E_i = 2 "
            "eta_2/(eta_2 + eta_1) = tau. Power ratios: R = |Gamma|^2, T = "
            "(eta_1/eta_2) |tau|^2, and R + T = 1 exactly. A quarter-wave "
            "coating of index sqrt(n_1 n_2) makes the two reflections (air-"
            "coating, coating-glass) equal and opposite - destructive "
            "interference erases the reflection at the design wavelength, "
            "the principle of camera-lens coatings and the microwave "
            "quarter-wave transformer. At oblique incidence, phase matching "
            "along the interface (k_x continuous) gives Snell's law as a "
            "byproduct."
        ),
        "key_points": [
            "Normal-incidence Gamma = (eta_2 - eta_1)/(eta_2 + eta_1) = (n_1 - n_2)/(n_1 + n_2); air-glass reflects 4% of power.",
            "Power conservation: R + T = 1 with R = |Gamma|^2; metal interfaces reflect ~100%.",
            "Oblique incidence splits TE/TM; TM reflection vanishes at Brewster's angle (polarized sunglasses physics).",
            "Quarter-wave layer of index sqrt(n_1 n_2) cancels reflection - the anti-reflection coating principle.",
            "The same Gamma formula reappears for transmission lines: (Z_L - Z_0)/(Z_L + Z_0).",
        ],
        "requirements": [
            "Boundary-conditions record (tangential E/H continuity).",
            "Plane waves and wave impedance eta.",
            "Power proportional to |E|^2.",
        ],
        "standards": [
            "Fresnel equations are the basis of thin-film optics design (ISO 10110 optical coating specs).",
            "Brewster's angle theta_B = arctan(n_2/n_1) for nonmagnetic media.",
        ],
        "citations": [C_ULABY, C_ORFANIDIS, C_GRIFFITHS],
        "sig_lens": (
            "Signature take: the Fresnel split is the Signature toll booth "
            "- every wave pays part of itself to cross a border, and the "
            "impedances set the tariff. His framing treats matching layers "
            "as diplomacy: arrange the interfaces and the wave passes free."
        ),
    },
    {
        "key": "snell_tir",
        "name": "Snell's Law and Total Internal Reflection: Bending Light on Purpose",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Snell's law, n_1 sin(theta_1) = n_2 sin(theta_2), governs the "
            "bending of waves crossing into a different medium - the reason "
            "a straw looks broken in water and lenses focus. It follows from "
            "phase continuity along the interface: the wave's oscillation "
            "along the seam must match on both sides. When going from dense "
            "to rare (n_1 > n_2), the transmitted angle grows faster than "
            "the incident angle, and past the critical angle theta_c = "
            "arcsin(n_2 / n_1) no transmitted wave can satisfy the math - "
            "all power reflects. This total internal reflection (TIR) is the "
            "principle of fiber optics: light trapped in a glass core by its "
            "own geometry, bouncing kilometers with negligible loss. Prisms, "
            "diamond brilliance, and the sparkling of waveguides' dielectric "
            "cousins all run on TIR."
        ),
        "how_it_works": (
            "Match phases at the interface: incident k_x = k_1 sin(theta_1) "
            "must equal transmitted k_x = k_2 sin(theta_2); with k = n "
            "omega / c the omegas cancel, leaving Snell's law. For n_1 > "
            "n_2, sin(theta_2) = (n_1/n_2) sin(theta_1) exceeds 1 when "
            "theta_1 > theta_c - no real transmitted angle exists, so the "
            "transmitted field becomes evanescent: it decays exponentially "
            "away from the surface (a near-field that carries no power "
            "away) while the reflected wave carries 100% of the power. An "
            "optical fiber exploits this with core index n_core slightly "
            "above cladding n_clad: rays steeper than the acceptance angle "
            "leak, rays within it are trapped - the numerical aperture NA = "
            "sqrt(n_core^2 - n_clad^2) quantifies the light-gathering cone. "
            "Frustrated TIR (bringing a second surface within the "
            "evanescent tail) is how fingerprint sensors and some "
            "touchscreens read contact."
        ),
        "key_points": [
            "Snell's law n_1 sin(theta_1) = n_2 sin(theta_2) from phase continuity along the interface.",
            "Critical angle theta_c = arcsin(n_2/n_1) (dense to rare); beyond it, total internal reflection - 100% reflected.",
            "TIR traps light in fiber cores: the basis of all fiber-optic communications.",
            "Beyond theta_c the transmitted field is evanescent - decaying, carrying no power away.",
            "Numerical aperture NA = sqrt(n_core^2 - n_clad^2) sets the fiber's acceptance cone.",
        ],
        "requirements": [
            "Fresnel record (the oblique-incidence context).",
            "Refractive index n = sqrt(mu_r epsilon_r) from the wave-equation record.",
            "Sine-function comfort; inverse sine for the critical angle.",
        ],
        "standards": [
            "Fiber NA typically 0.14-0.22 for telecom single-mode fiber (ITU-T G.652).",
            "Critical-angle prisms are calibrated optical components per ISO 10110.",
        ],
        "citations": [C_ULABY, C_ORFANIDIS, C_CHENG],
        "sig_lens": (
            "Signature take: total internal reflection is the Signature "
            "mirror with no silver - glass trapping light by geometry "
            "alone. His framing treats the fiber as a hallway of mirrors "
            "the light built itself, bouncing for kilometers."
        ),
    },
    {
        "key": "transmission_lines",
        "name": "Transmission Lines: When Wires Become Waveguides",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A transmission line is any structure that guides TEM waves "
            "along its length: coaxial cable, twisted pair, microstrip on a "
            "circuit board, parallel wires. The defining realization is that "
            "when the line is long compared to the wavelength (or the signal "
            "is fast compared to the transit time), voltage and current are "
            "WAVES - V(z,t) and I(z,t) propagating at v = 1 / sqrt(LC) - not "
            "instantaneous node values. A 100-meter coax delays a pulse "
            "about 500 ns; at gigabit rates that delay spans many bits, so "
            "reflections, ringing, and impedance matching dominate digital "
            "design. Every high-speed bus (USB, HDMI, PCIe, DDR memory), "
            "every antenna feed, and every RF front end is transmission-"
            "line engineering: the line has a characteristic impedance Z_0, "
            "and anything not equal to Z_0 sends part of the signal back."
        ),
        "how_it_works": (
            "Model the line as infinitesimal series inductance L dz and "
            "shunt capacitance C dz per unit length (plus small R, G for "
            "loss). A voltage step launched at the source charges each "
            "shunt capacitor through each series inductor in turn - the "
            "disturbance advances one section per sqrt(LC) seconds per "
            "meter, i.e. at v = 1/sqrt(LC). For typical coax (L ~ 250 nH/m, "
            "C ~ 100 pF/m) v = 2 x 10^8 m/s (0.66 c) and Z_0 = sqrt(L/C) = "
            "50 ohms. At the load, the wave meets impedance Z_L: continuity "
            "of V and I forces a reflected wave with Gamma = (Z_L - Z_0)/"
            "(Z_L + Z_0) - the Fresnel coefficient in circuit clothing. "
            "Matched (Z_L = Z_0): no reflection, all power delivered. Open "
            "(Z_L = infinity): Gamma = +1, voltage doubles at the end. "
            "Short (Z_L = 0): Gamma = -1, voltage cancels. Unterminated "
            "high-speed traces ring between these extremes - the reason "
            "every fast bus is length-matched and terminated."
        ),
        "key_points": [
            "Long lines carry voltage/current WAVES at v = 1/sqrt(LC), not instantaneous values; delay = length / v.",
            "Characteristic impedance Z_0 = sqrt(L/C) (lossless); 50 ohms is the RF standard, 75 for video/CATV.",
            "Load reflection Gamma = (Z_L - Z_0)/(Z_L + Z_0): matched = absorbed, open = +1, short = -1.",
            "Reflections cause ringing and inter-symbol interference - high-speed digital design is line design.",
            "Coax, twisted pair, microstrip, stripline, CPW: different geometries, same wave physics.",
        ],
        "requirements": [
            "Capacitance and inductance records (L and C per unit length).",
            "Fresnel reflection record - the same Gamma reappears.",
            "Wave intuition: finite propagation speed.",
        ],
        "standards": [
            "50-ohm (RF/microwave) and 75-ohm (video/broadcast) are the standard Z_0 values.",
            "Controlled-impedance PCB fabrication targets +/-10% Z_0 per IPC-2141A.",
        ],
        "citations": [C_POZAR, C_ULABY, C_RAMO],
        "sig_lens": (
            "Signature take: the transmission line is the Signature "
            "aqueduct - signals as water hammer, impedance as the channel "
            "width. His framing treats every mismatch as rapids: the wave "
            "hits, part splashes back, and the circuit rings like a struck "
            "pipe."
        ),
    },
]

ENTRIES += [
    {
        "key": "telegrapher_equations",
        "name": "The Telegrapher's Equations: The Transmission Line's Laws of Motion",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The telegrapher's equations are the transmission line's "
            "Maxwell's equations: two coupled first-order equations, "
            "partial V / partial z = -(R + j omega L) I and partial I / "
            "partial z = -(G + j omega C) V, relating voltage and current "
            "along the line to the per-unit-length resistance R, inductance "
            "L, conductance G, and capacitance C. Eliminating one variable "
            "gives the wave equation for the other, with propagation "
            "constant gamma = sqrt((R + j omega L)(G + j omega C)) = alpha + "
            "j beta and characteristic impedance Z_0 = sqrt((R + j omega L)/"
            "(G + j omega C)). In the lossless limit (R = G = 0): Z_0 = "
            "sqrt(L/C), purely real; beta = omega sqrt(LC); waves travel "
            "undiminished. The distortionless condition R/L = G/C makes "
            "alpha frequency-independent - Heaviside's insight that saved "
            "long telegraph lines. These equations are the daily working "
            "tool of signal-integrity and RF engineers."
        ),
        "how_it_works": (
            "Apply KVL around the series elements of a dz section: the "
            "voltage drop is (R + j omega L) I dz, giving the first "
            "equation. Apply KCL at the shunt node: the current lost is "
            "(G + j omega C) V dz, giving the second. Differentiate the "
            "first in z and substitute the second: partial^2 V / partial "
            "z^2 = (R + j omega L)(G + j omega C) V = gamma^2 V - the wave "
            "equation with complex gamma. Solutions are forward and "
            "backward waves, V(z) = V+ e^{-gamma z} + V- e^{+gamma z}, with "
            "I(z) = (V+ e^{-gamma z} - V- e^{+gamma z}) / Z_0. The general "
            "Z_0 is complex (lossy lines have reactive characteristic "
            "impedance), but for low-loss lines Z_0 ~ sqrt(L/C) and alpha ~ "
            "(R/2) sqrt(C/L) + (G/2) sqrt(L/C) nepers per meter. Input "
            "impedance of a length-l line, Z_in = Z_0 (Z_L + Z_0 tanh(gamma "
            "l))/(Z_0 + Z_L tanh(gamma l)), predicts everything from stub "
            "tuners to antenna feed behavior."
        ),
        "key_points": [
            "Telegrapher's pair: dV/dz = -(R+jwL)I, dI/dz = -(G+jwC)V - KVL/KCL on infinitesimal sections.",
            "gamma = sqrt((R+jwL)(G+jwC)) = alpha + j beta; Z_0 = sqrt((R+jwL)/(G+jwC)).",
            "Lossless: Z_0 = sqrt(L/C) real, beta = omega sqrt(LC), alpha = 0 - undiminished propagation.",
            "Distortionless condition R/L = G/C (Heaviside): frequency-independent attenuation and velocity.",
            "General solution: forward + backward waves; Z_in formula handles any length and load.",
        ],
        "requirements": [
            "Transmission-lines record (the physical picture).",
            "Phasor/complex-impedance comfort (j omega L, j omega C).",
            "Coupled-equation intuition: V drives I, I drives V.",
        ],
        "standards": [
            "Per-unit-length parameters extracted from 2D field solvers or measurement (IPC-TM-650).",
            "Nepers vs dB: alpha in Np/m x 8.686 = dB/m.",
        ],
        "citations": [C_POZAR, C_RAMO, C_COLLIN],
        "sig_lens": (
            "Signature take: the telegrapher's equations are the Signature "
            "ledger lines - every infinitesimal slice of wire must balance "
            "its voltage against its current. His framing treats the whole "
            "cable as a chain of tiny accountants, each passing the wave "
            "along with its books balanced."
        ),
    },
    {
        "key": "reflection_vswr_smith",
        "name": "Reflection, VSWR, and the Smith Chart: Reading the Circle",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The voltage reflection coefficient Gamma = (Z_L - Z_0)/(Z_L + "
            "Z_0) measures what fraction of a wave bounces off a load; its "
            "magnitude |Gamma| runs from 0 (matched, all power delivered) "
            "to 1 (open or short, all power reflected). The standing-wave "
            "ratio VSWR = (1 + |Gamma|)/(1 - |Gamma|) is what technicians "
            "actually measure: 1.0 is perfect, 2.0 means ~11% of power "
            "reflected, infinity means total reflection. The Smith chart is "
            "the ingenious graphical calculator that maps the entire "
            "impedance plane onto the |Gamma| <= 1 disk via z = (1 + Gamma)/"
            "(1 - Gamma): moving along a transmission line is just rotating "
            "around the chart's center, adding series/shunt elements is "
            "moving along constant-resistance/conductance circles. Invented "
            "by Phillip Smith in 1939, it remains the RF engineer's native "
            "language for matching networks, stability circles, and noise "
            "circles."
        ),
        "how_it_works": (
            "On a line, V(z) = V+(e^{-j beta z} + Gamma_L e^{+j beta z}): "
            "incident plus reflected waves interfere into a standing wave "
            "whose envelope swings between |V+|(1 + |Gamma|) and |V+|(1 - "
            "|Gamma|) - the ratio is the VSWR, measured with a slotted line "
            "or derived from return loss RL = -20 log|Gamma|. The Smith "
            "chart plots Gamma in the complex plane; since z = Z/Z_0 = (1 + "
            "Gamma)/(1 - Gamma) is a bilinear map, lines of constant "
            "resistance and reactance become circles - the chart's famous "
            "mesh. A load Z_L = 100 ohms on 50-ohm line: Gamma = 1/3, a "
            "point on the real axis at 0.333; VSWR = 2. Moving lambda/8 "
            "toward the generator rotates the point 90 degrees around the "
            "center (constant |Gamma| circle). Matching means navigating to "
            "the chart's center (Gamma = 0): series elements move along "
            "constant-resistance circles, shunt elements along constant-"
            "conductance circles - stub tuners and L-networks are chart "
            "journeys drawn before they are built."
        ),
        "key_points": [
            "Gamma = (Z_L - Z_0)/(Z_L + Z_0); |Gamma|: 0 = matched, 1 = total reflection (open/short).",
            "VSWR = (1+|Gamma|)/(1-|Gamma|): 1.0 perfect, 2.0 ~ 11% power reflected; return loss = -20 log|Gamma|.",
            "Smith chart maps all passive impedances onto the |Gamma| <= 1 disk via z = (1+Gamma)/(1-Gamma).",
            "Line length = rotation about chart center; series/shunt elements = moves along circle families.",
            "Matching-network design is navigation to chart center; stability and noise circles live on the same chart.",
        ],
        "requirements": [
            "Transmission-lines record (incident/reflected waves).",
            "Complex-number plane comfort: magnitude and angle.",
            "Power proportional to |V|^2.",
        ],
        "standards": [
            "VSWR 1.5:1 is a common acceptance threshold for antenna systems (~4% reflected power).",
            "Smith chart normalized impedance z = Z/Z_0; admittance chart is the 180-degree-rotated overlay.",
        ],
        "citations": [C_POZAR, C_COLLIN, C_ULABY],
        "sig_lens": (
            "Signature take: the Smith chart is the Signature compass - "
            "the entire infinite impedance plane folded into one disk, "
            "with matching as true north at the center. His framing treats "
            "every RF engineer as a navigator, and the chart never lies "
            "about where you stand."
        ),
    },
    {
        "key": "s_parameters",
        "name": "S-Parameters: The Language of High-Frequency Circuits",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "At high frequencies, open and short circuits - the test "
            "conditions of Z/Y/H parameters - cause oscillations and are "
            "nearly impossible to realize, so the industry speaks "
            "S-parameters: scattering parameters defined with all ports "
            "terminated in the reference impedance (usually 50 ohms). For a "
            "two-port, b_1 = S_11 a_1 + S_12 a_2 and b_2 = S_21 a_1 + S_22 "
            "a_2, where a are incident and b reflected power-waves: S_11 is "
            "input reflection, S_21 forward transmission (gain), S_12 "
            "reverse isolation, S_22 output reflection. |S_21|^2 is the "
            "transducer power gain; S_11 = 0 means a matched input. "
            "Measured by vector network analyzers, shipped in Touchstone "
            "files with every RF transistor and filter, S-parameters are "
            "the datasheet language of everything above ~100 MHz - "
            "amplifiers, mixers, filters, and antennas alike."
        ),
        "how_it_works": (
            "Terminate port 2 in Z_0 (so a_2 = 0) and drive port 1: S_11 = "
            "b_1/a_1 is the input reflection coefficient, S_21 = b_2/a_1 "
            "the forward transmission. Reverse the setup for S_22, S_12. "
            "Because ports see matched loads, the device operates in its "
            "normal environment - no oscillation, no exotic fixtures. With "
            "an arbitrary load Gamma_L on port 2, the input reflection "
            "becomes Gamma_in = S_11 + S_12 S_21 Gamma_L / (1 - S_22 "
            "Gamma_L) - the load 'pulls' the input through the reverse path "
            "(mismatch and stability analysis lives in this formula). "
            "Cascade two-ports by converting to T (transfer) parameters, "
            "multiply, convert back. Power gain definitions (transducer, "
            "available, operating) are all algebraic functions of the S "
            "matrix and source/load reflections; amplifier stability "
            "circles (Rollett K-factor) are drawn from S-parameters on - "
            "fittingly - the Smith chart."
        ),
        "key_points": [
            "S-parameters relate incident (a) to reflected (b) power waves with all ports terminated in Z_0 - measurable at RF.",
            "Two-port: S_11 input match, S_21 forward gain, S_12 reverse isolation, S_22 output match.",
            "|S_21|^2 = transducer power gain; S_11 = S_22 = 0 is the matched ideal.",
            "Loaded input: Gamma_in = S_11 + S_12 S_21 Gamma_L/(1 - S_22 Gamma_L) - the mismatch/stability workhorse.",
            "Touchstone (.sNp) files + vector network analyzers make S-parameters the industry's exchange format.",
        ],
        "requirements": [
            "Reflection coefficient and Smith-chart records.",
            "Matrix-times-vector comfort (2x2).",
            "Power-wave intuition: a/b carry sqrt(power) with phase.",
        ],
        "standards": [
            "Touchstone file format (IEEE 370 references) is the S-parameter exchange standard.",
            "Reference impedance defaults to 50 ohms; must be stated for any S-parameter set.",
        ],
        "citations": [C_POZAR, C_COLLIN, C_RAMO],
        "sig_lens": (
            "Signature take: S-parameters are the Signature interview - "
            "ask each port how it answers waves, with every other port "
            "politely terminated. His framing treats the VNA as a "
            "polygraph: the device cannot hide its reflections."
        ),
    },
    {
        "key": "impedance_matching",
        "name": "Impedance Matching: Quarter-Wave Transformers and Stubs",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Maximum power transfer demands matching: a source delivers its "
            "full available power only into a matched load, and any mismatch "
            "sends power back as reflection (VSWR, lost gain, possible "
            "oscillation in amplifiers). The quarter-wave transformer is the "
            "cleanest fix for real loads: a lambda/4 line of impedance Z_1 "
            "= sqrt(Z_0 Z_L) between a Z_0 line and Z_L load transforms "
            "perfectly at the design frequency - the two reflections (line-"
            "transformer, transformer-load) are equal and opposite, "
            "destructive interference erasing Gamma. For complex loads, "
            "single-stub tuners (a shunt open/short stub at a calculated "
            "position and length) and L-networks (two reactances) navigate "
            "the Smith chart to center. Multi-section transformers trade "
            "bandwidth for complexity (binomial/maximally-flat and "
            "Chebyshev responses); at low frequencies, transformer "
            "windings do the same job magnetically."
        ),
        "how_it_works": (
            "A line of length l and impedance Z_1 terminated in Z_L has "
            "input Z_in = Z_1 (Z_L + j Z_1 tan(beta l))/(Z_1 + j Z_L tan(beta "
            "l)). At l = lambda/4, beta l = pi/2, tan -> infinity, and Z_in "
            "= Z_1^2 / Z_L - the quarter-wave inverts impedance. Choose Z_1 "
            "= sqrt(Z_0 Z_L): then Z_in = Z_0, matched. Example: 100-ohm "
            "load on 50-ohm line needs a 70.7-ohm quarter-wave section - "
            "reflections of (70.7-50)/(70.7+50) and (100-70.7)/(100+70.7) "
            "cancel. The stub tuner generalizes: at distance d from the "
            "load, the line's admittance is Y_0 + jB; a shunt stub of "
            "susceptance -jB cancels the imaginary part, leaving a pure "
            "match. L-networks do it with lumped L and C at low RF. "
            "Bandwidth is the price: single-section matches are narrowband "
            "(~10-20%); tapered lines and multi-section designs widen it "
            "toward the Bode-Fano limit, which says perfect broadband "
            "matching of reactive loads is fundamentally impossible."
        ),
        "key_points": [
            "Matching = maximum power transfer + zero reflection; mismatch wastes power and risks instability.",
            "Quarter-wave transformer: Z_1 = sqrt(Z_0 Z_L), lambda/4 long - two equal-and-opposite reflections cancel.",
            "Stub tuners (shunt stub at computed position/length) and L-networks match complex loads via Smith-chart navigation.",
            "Multi-section (binomial/Chebyshev) transformers widen bandwidth; tapers approach the broadband ideal.",
            "Bode-Fano limit: reactive loads cannot be matched perfectly over infinite bandwidth - physics sets the ceiling.",
        ],
        "requirements": [
            "Smith-chart record (navigation to center).",
            "Reflection coefficient and Z_in formula.",
            "Resonance intuition: reactances cancel in pairs.",
        ],
        "standards": [
            "Return loss >= 10 dB (|Gamma| <= 0.316) is a typical matching acceptance criterion.",
            "Bode-Fano criterion bounds the achievable match-bandwidth product for RC/RL loads.",
        ],
        "citations": [C_POZAR, C_COLLIN, C_ULABY],
        "sig_lens": (
            "Signature take: matching is the Signature handshake done "
            "right - two impedances meeting as equals, no reflection, no "
            "wasted power. His framing treats the quarter-wave section as "
            "a diplomat: it translates between strangers until both sides "
            "agree."
        ),
    },
    {
        "key": "waveguides",
        "name": "Waveguides: Guiding Waves Between Metal Walls",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A waveguide is a hollow metal pipe that guides waves by "
            "bouncing them between its walls - no center conductor, no TEM "
            "mode, just TE (transverse electric) and TM (transverse "
            "magnetic) modes that fit the cross-section. The dominant TE_10 "
            "mode of rectangular guide (width a) propagates only above the "
            "cutoff frequency f_c = c / 2a; below cutoff the wave is "
            "evanescent and dies within centimeters. Standard bands (WR-90 "
            "for X-band 8.2-12.4 GHz, a = 22.86 mm, f_c = 6.56 GHz) size the "
            "guide so only TE_10 propagates - single-mode, dispersion-"
            "controlled. Waveguides carry kilowatts where coax would melt "
            "(radar transmitters, satellite uplinks, microwave ovens' "
            "feed), with far lower loss than coax at microwave frequencies. "
            "Guide wavelength lambda_g = lambda / sqrt(1 - (f_c/f)^2) "
            "exceeds the free-space wavelength - waves zigzag, so they "
            "travel farther per unit forward progress."
        ),
        "how_it_works": (
            "Separate variables in the Helmholtz equation inside the "
            "rectangle with PEC walls (E_tangential = 0): the transverse "
            "field must vanish at the walls, so it forms standing-wave "
            "patterns sin(m pi x / a) sin(n pi y / b) - the TE_mn/TM_mn "
            "modes. The separation constant gives the cutoff wavenumber "
            "k_c = sqrt((m pi/a)^2 + (n pi/b)^2); propagation requires k > "
            "k_c, i.e. f > f_c = k_c c / 2 pi. For TE_10: k_c = pi/a, f_c "
            "= c/2a. Above cutoff the propagation constant beta = sqrt(k^2 "
            "- k_c^2) is real and the wave travels; below cutoff it is "
            "imaginary and the field decays - the guide is a high-pass "
            "filter made of geometry. The wave impedance for TE modes is "
            "Z_TE = eta k / beta (frequency-dependent, unlike coax's flat "
            "Z_0), and dispersion (beta nonlinear in omega) spreads pulses "
            "- the price of hollow guiding. Slots, irises, and posts inside "
            "the guide make filters, couplers, and matching elements."
        ),
        "key_points": [
            "Hollow metal pipe guides TE/TM modes; no TEM possible without an inner conductor.",
            "Cutoff f_c = c/2a for TE_10 rectangular: propagate above, evanescent decay below - geometry as high-pass filter.",
            "Single-mode bands (WR-90: 8.2-12.4 GHz) size the guide so only the dominant mode fits.",
            "Guide wavelength lambda_g = lambda/sqrt(1-(f_c/f)^2) > lambda; wave impedance Z_TE = eta k/beta is dispersive.",
            "Kilowatt power handling and low loss at microwave frequencies: radar, satcom, industrial heating.",
        ],
        "requirements": [
            "Boundary-conditions record (PEC walls force E_tangential = 0).",
            "Wave-equation/Helmholtz record.",
            "Standing-wave intuition: fitting half-wavelengths between walls.",
        ],
        "standards": [
            "EIA WR-designations (WR-90, WR-28, ...) standardize waveguide sizes and bands.",
            "Waveguide flanges (UG, CPR) standardize connections per MIL-DTL-3922.",
        ],
        "citations": [C_POZAR, C_COLLIN, C_RAMO],
        "sig_lens": (
            "Signature take: the waveguide is the Signature hallway - "
            "waves bouncing wall to wall, allowed through only if they "
            "fit the architecture. His framing treats cutoff as the "
            "bouncer: too long a wavelength, and the door never opens."
        ),
    },
    {
        "key": "cavity_resonators",
        "name": "Cavity Resonators: Trapping Waves in a Box",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Close both ends of a waveguide and the traveling wave becomes "
            "a standing wave: a cavity resonator, the microwave analog of "
            "an organ pipe or a laser cavity. A rectangular box (a x b x d) "
            "resonates at f_lmn = (c/2) sqrt((l/a)^2 + (m/b)^2 + (n/d)^2) "
            "for TE/TM_lmn modes - discrete frequencies set purely by "
            "geometry. The quality factor Q = omega (stored energy)/(power "
            "lost) reaches 10^3-10^4 in copper cavities (walls lose to skin "
            "effect) and 10^9+ in superconducting niobium (particle "
            "accelerators, quantum-computing resonators). Cavities are "
            "frequency references (wavemeters), narrowband filters "
            "(multipole cavity filters in base stations), the resonant "
            "heart of magnetrons and klystrons, and the boxes that trap "
            "microwaves in every microwave oven (a crude, multi-mode "
            "cavity with a stirrer)."
        ),
        "how_it_works": (
            "Impose PEC walls on all six faces: each field component forms "
            "standing waves sin(l pi x/a) sin(m pi y/b) sin(n pi z/d) with "
            "integer mode numbers, and the Helmholtz equation demands (l "
            "pi/a)^2 + (m pi/b)^2 + (n pi/d)^2 = k^2 = (2 pi f/c)^2 - hence "
            "the discrete f_lmn spectrum. Energy sloshes between E and H "
            "at the resonant frequency, decaying with time constant "
            "proportional to Q; drive it at resonance and tiny inputs build "
            "huge fields (the microwave oven's 1 kW becomes intense "
            "standing-wave hot spots - the turntable averages them). "
            "Coupling in/out through small irises or probes samples the "
            "field without spoiling Q much; tuning screws perturb the "
            "volume and trim the frequency (Slater perturbation: metal "
            "intrusion where E dominates lowers f, where H dominates raises "
            "it). Cavity filters cascade coupled resonators for steep "
            "skirts; accelerator cavities phase-synchronize E fields to "
            "surf charged particles to near light speed."
        ),
        "key_points": [
            "Closed metal box: discrete resonances f_lmn = (c/2)sqrt((l/a)^2+(m/b)^2+(n/d)^2) set by geometry alone.",
            "Q = omega x stored energy / power loss: ~10^4 copper, 10^9+ superconducting - the selectivity figure of merit.",
            "Energy sloshes E-to-H at resonance; weak drive builds huge fields - ovens, accelerators, filters.",
            "Coupling via irises/probes; tuning screws perturb volume (Slater perturbation rule).",
            "Applications: wavemeters, cavity filters, magnetron/klystron resonators, accelerator and qubit cavities.",
        ],
        "requirements": [
            "Waveguides record (modes, cutoff, standing patterns).",
            "Resonance intuition: drive at the natural frequency, amplitude builds.",
            "Skin-depth record (wall loss sets copper-cavity Q).",
        ],
        "standards": [
            "Unloaded Q_0 vs loaded Q_L vs external Q_e: 1/Q_L = 1/Q_0 + 1/Q_e.",
            "Superconducting RF cavities (niobium, 2 K) per TESLA/ILC specifications reach Q_0 > 10^10.",
        ],
        "citations": [C_POZAR, C_COLLIN, C_HARRINGTON],
        "sig_lens": (
            "Signature take: the cavity is the Signature echo chamber - "
            "a wave trapped in a metal box, ringing at the pitch its "
            "geometry dictates. His framing treats Q as patience: how "
            "many oscillations the box remembers before forgetting."
        ),
    },
    {
        "key": "antennas_intro",
        "name": "Antennas: Turning Guided Waves into Free Space",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "An antenna is a transducer between guided waves and free-space "
            "waves: it launches the transmission line's confined fields "
            "into the world (transmit) and harvests passing waves back "
            "into a line (receive) - reciprocity guarantees the two "
            "directions share gain, pattern, and impedance. Key figures of "
            "merit: radiation pattern (angular power distribution), "
            "directivity/gain (peak intensity vs isotropic), efficiency "
            "(radiated vs accepted power), polarization (which E-field the "
            "antenna speaks), and input impedance (what the feed line sees "
            "- usually engineered to 50 ohms). The far field begins beyond "
            "~2D^2/lambda (D = largest dimension); inside that, the "
            "reactive near field stores sloshing energy. Dipoles, "
            "monopoles, loops, patches, horns, dishes, and arrays are one "
            "family: accelerated charge, shaped by geometry."
        ),
        "how_it_works": (
            "Feed RF current into a conductor: charges accelerate, and "
            "accelerated charge radiates (Larmor) - the antenna is "
            "controlled acceleration. The current distribution (roughly "
            "sinusoidal on thin wires) determines the far field via the "
            "retarded potential integral: each current element contributes "
            "a spherical wavelet, and their interference IS the pattern. "
            "Reciprocity (a Maxwell-equations theorem) proves transmit and "
            "receive patterns identical: the effective aperture A_e = "
            "lambda^2 G / 4 pi ties gain to capture area - a dish's gain "
            "comes from its physical area, a dipole's ~2.15 dBi from its "
            "~0.13 lambda^2 effective aperture. Impedance matching (the "
            "Smith-chart record) applies at the feedpoint: mismatch "
            "reflects transmitter power back. Bandwidth, size, and "
            "efficiency trade fundamentally (Chu-Wheeler limit): small "
            "antennas are narrowband or inefficient - physics, not poor "
            "design."
        ),
        "key_points": [
            "Antenna = guided-to-free-space transducer; reciprocity makes transmit and receive patterns identical.",
            "Figures of merit: pattern, directivity/gain, efficiency, polarization, 50-ohm-ish feed impedance.",
            "Far field beyond ~2D^2/lambda; reactive near field inside stores non-radiating energy.",
            "Effective aperture A_e = lambda^2 G / 4 pi: gain IS capture area - dishes earn gain by size.",
            "Chu-Wheeler limit: electrically small antennas trade bandwidth and efficiency fundamentally.",
        ],
        "requirements": [
            "Radiation-from-accelerated-charge concept (previewed in statics, formalized later).",
            "Transmission-line matching record (feedpoint VSWR).",
            "Poynting vector (radiated power density).",
        ],
        "standards": [
            "Gain in dBi (vs isotropic) or dBd (vs dipole; dBi = dBd + 2.15).",
            "IEEE Std 145 defines antenna terms: directivity, gain, polarization, effective aperture.",
        ],
        "citations": [C_BALANIS_ANT, C_KRAUS, C_ULABY],
        "sig_lens": (
            "Signature take: the antenna is the Signature mouth and ear - "
            "the place where confined signals learn to fly and passing "
            "waves learn to land. His framing treats reciprocity as "
            "fairness: every antenna hears exactly as well as it shouts."
        ),
    },
    {
        "key": "half_wave_dipole",
        "name": "The Half-Wave Dipole: The Reference Antenna",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The half-wave dipole - two quarter-wave arms, total length "
            "lambda/2, fed at the center - is the reference antenna against "
            "which others are measured (dBd = dB relative to dipole). Its "
            "current is approximately sinusoidal, zero at the tips and "
            "maximum at the feedpoint, and its far-field pattern is the "
            "classic doughnut: E(theta) proportional to cos((pi/2) cos "
            "theta)/sin theta, maximum broadside (theta = 90 deg), nulls "
            "along the wire axis. Directivity is 1.64 (2.15 dBi), the "
            "half-power beamwidth ~78 degrees, and the feedpoint impedance "
            "~73 + j42.5 ohms (resonant near 73 ohms when shortened "
            "slightly). Rabbit-ear TV antennas, FM dipoles, and the driven "
            "element of every Yagi-Uda are half-wave dipoles; its image in "
            "a ground plane makes the quarter-wave monopole (car antennas, "
            "with ~36.5 ohms and 5.15 dBi over perfect ground)."
        ),
        "how_it_works": (
            "At total length lambda/2 the wire is resonant: the sinusoidal "
            "standing-wave current I(z) = I_0 sin(k(l/2 - |z|)) fits with "
            "nodes at the open tips. The far field integrates each element's "
            "contribution with its phase delay: E_theta proportional to the "
            "integral, which evaluates to cos((pi/2) cos theta)/sin theta - "
            "unity at broadside, zero on axis (elements' radiation cancels "
            "along the wire). Integrating |E|^2 over the sphere gives total "
            "radiated power; dividing the peak intensity by the average "
            "gives directivity 1.64. The 73-ohm feedpoint resistance is the "
            "radiation resistance - the circuit-model fiction (P = (1/2) "
            "I_0^2 R_rad) representing power carried away by the wave. "
            "Shorten slightly below lambda/2 and the inductive reactance "
            "vanishes: the resonant dipole looks like ~70 ohms resistive, "
            "an easy match to 75-ohm coax - the reason TV twin-lead and "
            "dipoles paired historically."
        ),
        "key_points": [
            "Half-wave dipole: lambda/2 total, center-fed, sinusoidal current - the 0-dBd reference antenna.",
            "Doughnut pattern cos((pi/2)cos theta)/sin theta: max broadside, nulls on the wire axis.",
            "Directivity 1.64 (2.15 dBi); beamwidth ~78 deg; feedpoint ~73 ohms (resonant when slightly shortened).",
            "Radiation resistance (~73 ohms) is the circuit fiction for power carried away: P = (1/2) I_0^2 R_rad.",
            "Quarter-wave monopole over ground = half the dipole imaged: ~36.5 ohms, the car-antenna classic.",
        ],
        "requirements": [
            "Antennas-intro record (pattern, directivity, reciprocity).",
            "Standing-wave intuition (current nodes at open tips).",
            "Interference: phased contributions adding/canceling with angle.",
        ],
        "standards": [
            "dBd (gain vs dipole) vs dBi (vs isotropic): dBi = dBd + 2.15.",
            "73-ohm nominal feedpoint is the basis of 75-ohm TV/broadcast systems.",
        ],
        "citations": [C_BALANIS_ANT, C_KRAUS, C_ORFANIDIS],
        "sig_lens": (
            "Signature take: the dipole is the Signature tuning fork of "
            "the airwaves - a half-wavelength of wire humming its one "
            "note, doughnut of energy blooming around it. His framing "
            "treats it as the atom of antennas: everything else is "
            "molecules built from dipoles."
        ),
    },
    {
        "key": "antenna_arrays",
        "name": "Antenna Arrays: Steering Beams Without Moving",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "An antenna array combines N elements with controlled phases to "
            "shape the pattern by interference: the total pattern is the "
            "single-element pattern times the array factor AF = sin(N psi/2)"
            "/sin(psi/2), where psi = k d cos(theta) + beta combines the "
            "geometric phase (spacing d, angle theta) with the electrical "
            "phase shift beta between elements. Choose beta = -k d cos "
            "theta_0 and the beam points at theta_0 - electronic steering "
            "with no moving parts, the principle of phased-array radar, 5G "
            "massive MIMO, and radio astronomy. An N-element broadside array "
            "gains ~N times the element directivity (array gain) and narrows "
            "the beam ~1/N. Grating lobes (extra main beams) appear if "
            "spacing exceeds lambda/(1 + |cos theta_0|) - the sampling-"
            "theorem of arrays - so half-wave spacing is the safe classic."
        ),
        "how_it_works": (
            "In the far field the elements' contributions differ only by "
            "phase: element n at position n d along the axis contributes "
            "e^{j n (k d cos theta + beta)} relative to element 0. Summing "
            "the geometric series gives AF = sin(N psi/2)/sin(psi/2) e^{j(N-"
            "1)psi/2} - magnitude N when psi = 0 (all in phase: the main "
            "beam), zero when N psi/2 = +/- pi (first nulls), with sidelobes "
            "between. Steering: set beta = -k d cos theta_0 so psi = 0 at "
            "the desired angle - phase shifters or true-time-delay units "
            "implement beta per element. Uniform amplitude gives -13.3 dB "
            "first sidelobes; tapering amplitudes (binomial, Dolph-"
            "Chebyshev) trades beamwidth for sidelobe suppression - "
            "Chebyshev is optimal for a given sidelobe level. Grating lobes "
            "are the array's aliasing: spacings over ~lambda/2 let a second "
            "psi = 2 pi direction radiate fully - avoided by dense spacing "
            "or limited scan range."
        ),
        "key_points": [
            "Pattern = element pattern x array factor; AF = sin(N psi/2)/sin(psi/2), psi = k d cos theta + beta.",
            "Phase progression beta = -k d cos theta_0 steers the beam electronically - phased arrays, 5G MIMO.",
            "N elements give ~N x directivity and ~1/N beamwidth (broadside, uniform).",
            "Grating lobes (aliasing) when d > lambda/(1+|cos theta_0|); lambda/2 spacing is the safe classic.",
            "Amplitude tapering (Dolph-Chebyshev optimal) trades beamwidth for sidelobe control.",
        ],
        "requirements": [
            "Half-wave dipole record (element pattern concept).",
            "Phasor addition: N equal phasors with progressive phase.",
            "Geometric-series sum intuition.",
        ],
        "standards": [
            "Phased-array calibration per IEEE Std 1720 (near-field array characterization).",
            "5G NR massive-MIMO arrays implement the same array-factor math in silicon.",
        ],
        "citations": [C_BALANIS_ANT, C_KRAUS, C_ORFANIDIS],
        "sig_lens": (
            "Signature take: the array is the Signature choir - N voices "
            "singing with timed delays so their waves arrive as one "
            "thunderclap in exactly the chosen direction. His framing "
            "treats beam steering as conducting: the phase shifters are "
            "the baton, silence everywhere else."
        ),
    },
]

ENTRIES += [
    {
        "key": "friis_equation",
        "name": "The Friis Equation: Radio Link Arithmetic",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The Friis transmission equation is the accountant's version of "
            "a radio link: P_r = P_t G_t G_r (lambda / 4 pi R)^2 - received "
            "power equals transmitted power times both antenna gains times "
            "the free-space path factor. The (lambda/4 pi R)^2 term is the "
            "spreading loss: power density falls as 1/R^2 (Poynting flux "
            "over a growing sphere) while the receive antenna harvests its "
            "effective aperture A_e = lambda^2 G_r / 4 pi. In decibels it "
            "becomes link-budget addition: P_r(dBm) = P_t + G_t + G_r - "
            "20 log(4 pi R/lambda) - margins. Example: 1 W at 2.4 GHz over "
            "1 km with 10-dBi antennas each gives ~100 dB of free-space path "
            "loss, ~10 nW received - and Wi-Fi works because receivers hear "
            "nanowatts. Add polarization mismatch, feedline loss, fading "
            "margin, and noise floor (kTB), and the Friis equation sizes "
            "every wireless system from Bluetooth to deep-space links "
            "(Voyager's signal arrives at ~10^-16 W)."
        ),
        "how_it_works": (
            "Transmitter radiates P_t G_t as effective isotropic power; at "
            "range R the flux is P_t G_t / 4 pi R^2 (Poynting density on "
            "the sphere). The receive antenna captures flux times its "
            "effective aperture: P_r = (P_t G_t / 4 pi R^2) (lambda^2 G_r "
            "/ 4 pi) - the Friis equation, valid in the far field of both "
            "antennas with matched polarization and impedance. Take 10 log "
            "of both sides: path loss L_fs(dB) = 20 log(4 pi R/lambda) = 20 "
            "log f + 20 log R + 32.44 (f in MHz, R in km) - the '6 dB per "
            "octave, 6 dB per doubling of distance' rule. Real budgets add "
            "L_misc (cables, connectors), polarization loss, atmospheric "
            "absorption (notably ~60 GHz oxygen and rain fade above 10 "
            "GHz), multipath fading margin (10-20 dB for mobile), and "
            "compare P_r against receiver sensitivity (kTB x noise figure x "
            "required SNR) - positive margin means the link closes."
        ),
        "key_points": [
            "Friis: P_r = P_t G_t G_r (lambda/4 pi R)^2 - far-field, matched polarization/impedance.",
            "Free-space path loss 20 log(4 pi R/lambda): 6 dB per distance doubling, 6 dB per frequency octave.",
            "Receive aperture A_e = lambda^2 G/4 pi converts flux to captured power - gain IS area.",
            "Link budget in dB is addition: gains minus losses minus margins vs receiver sensitivity (kTB).",
            "Real links add cable loss, polarization mismatch, rain/atmospheric loss, and fading margin.",
        ],
        "requirements": [
            "Poynting vector (power flux) and antenna gain/aperture records.",
            "Decibel arithmetic: dB addition = multiplication.",
            "Inverse-square intuition.",
        ],
        "standards": [
            "EIRP = P_t G_t (dBm) is the regulated transmit metric (FCC/ETSI limits).",
            "Free-space path loss formula is the reference for ITU-R P.525 propagation models.",
        ],
        "citations": [C_BALANIS_ANT, C_ULABY, C_KRAUS],
        "sig_lens": (
            "Signature take: the Friis equation is the Signature toll "
            "ledger for every radio mile - distance taxes the signal at "
            "6 dB per doubling, and only gain and aperture pay it back. "
            "His framing treats link budgets as travel budgets: plan the "
            "losses, or the message never arrives."
        ),
    },
    {
        "key": "radiation_mechanism",
        "name": "Why Accelerated Charge Radiates: The Larmor Formula",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The deep reason antennas work: accelerated charge radiates. "
            "The Larmor formula gives the power: P = q^2 a^2 / 6 pi "
            "epsilon_0 c^3 - radiated power grows with the SQUARE of the "
            "acceleration. A charge moving at constant velocity carries its "
            "Coulomb field along undisturbed (no radiation); jerk it - "
            "wiggle it in an antenna, bend it in a synchrotron, stop it in "
            "an X-ray tube - and the field lines can't keep up: the kink "
            "propagates outward at c as a wave, carrying energy away "
            "forever. This single fact explains antennas (controlled "
            "oscillation), synchrotron light sources (relativistic bending), "
            "bremsstrahlung X-rays (deceleration), and why atoms are stable "
            "(quantum mechanics forbids the spiraling collapse classical "
            "physics predicts). The angular pattern favors broadside to the "
            "acceleration - no radiation along the acceleration axis."
        ),
        "how_it_works": (
            "Picture the charge's field lines: moving uniformly, they are "
            "the Coulomb pattern dragged along. Accelerate the charge "
            "briefly: the near field updates to the new velocity, but the "
            "far field still shows the old position - the transition region "
            "between them is a kink, and that kink IS the radiation field, "
            "falling as 1/r (not 1/r^2) so its Poynting flux survives to "
            "infinity. Formally, the Lienard-Wiechert potentials give E_rad "
            "proportional to the retarded acceleration cross the line of "
            "sight; integrating S = E x H / mu_0 over angles yields the "
            "Larmor power. The sin^2(theta) pattern (theta from the "
            "acceleration vector) means a linear antenna radiates broadside "
            "and nothing along its axis - the dipole doughnut, derived from "
            "first principles. Relativistically the formula gains gamma^6 "
            "factors: synchrotron power scales as energy^4 / radius^2, the "
            "reason electron synchrotrons are kilometers around."
        ),
        "key_points": [
            "Larmor: P = q^2 a^2 / 6 pi epsilon_0 c^3 - only ACCELERATED charge radiates; uniform motion is silent.",
            "The kink picture: field lines can't update faster than c; the transition kink propagates as the wave.",
            "Radiation pattern ~ sin^2(theta) about the acceleration axis - nulls along the axis (dipole doughnut origin).",
            "Antennas = controlled charge wiggling; X-ray tubes = controlled stopping; synchrotrons = controlled bending.",
            "Relativistic gamma^6 scaling makes synchrotron radiation dominant at high energies.",
        ],
        "requirements": [
            "Coulomb field picture (field lines of a charge).",
            "Finite-speed-of-light intuition (information takes r/c to arrive).",
            "Antenna records (this is their 'why').",
        ],
        "standards": [
            "Larmor formula is the nonrelativistic limit of the Lienard-Wiechert radiated power.",
            "Synchrotron radiation power scaling underpins light-source facility design (ESRF, APS).",
        ],
        "citations": [C_GRIFFITHS, C_JACKSON, C_BALANIS_ANT],
        "sig_lens": (
            "Signature take: radiation is the Signature scream - charge "
            "moving smoothly whispers only to its neighbors, but jerk it "
            "and the news outruns it at light speed. His framing treats "
            "every antenna as a controlled scream, shaped by geometry "
            "into a message."
        ),
    },
    {
        "key": "scattering_rcs",
        "name": "Scattering and Radar Cross Section: How Big You Look to Radar",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Radar cross section sigma answers: 'how big does this object "
            "look to radar?' Defined as sigma = limit 4 pi R^2 |E_s|^2 / "
            "|E_i|^2 (scattered vs incident field, far-field), in square "
            "meters (or dBsm), it is NOT the physical area: a corner "
            "reflector has sigma far larger than its size, a stealth "
            "aircraft far smaller. Three regimes: Rayleigh (object << "
            "lambda: sigma ~ 1/lambda^4 - why the sky is blue), Mie "
            "resonance (object ~ lambda: oscillatory), and optical (object "
            ">> lambda: sigma ~ projected area - a large metal sphere gives "
            "pi a^2). Stealth engineering shapes surfaces to scatter away "
            "from the radar (faceting), coats with radar-absorbent material "
            "(lossy media doing their job), and manages edge diffraction - "
            "reducing sigma by factors of 10^4-10^6. The radar equation, "
            "P_r = P_t G_t G_r lambda^2 sigma / (4 pi)^3 R^4, shows the "
            "brutal R^4 dependence: doubling range costs 12 dB."
        ),
        "how_it_works": (
            "An incident wave induces currents on the target (physical "
            "optics: J_s = 2 n cross H_i on lit surfaces); those currents "
            "re-radiate - the scattered field. In the optical limit the "
            "lit hemisphere of a conducting sphere carries the induced "
            "current and the backscattered power equals the intercepted "
            "power pi a^2 times the antenna-like gain of the curved surface "
            "- net sigma = pi a^2, the geometric area. A flat plate at "
            "normal incidence gives sigma = 4 pi A^2 / lambda^2 - enormous "
            "(a 1-m^2 plate at 3 GHz has sigma ~ 1,260 m^2), which is why "
            "stealth avoids flat normal surfaces: tilt the plate and the "
            "specular flash misses the radar. The radar equation chains two "
            "Friis hops: power density at target (P_t G_t / 4 pi R^2), "
            "intercepted sigma, re-radiated isotropically-ish, captured by "
            "A_e at the radar: P_r = P_t G_t G_r lambda^2 sigma / (4 pi)^3 "
            "R^4. Detection needs P_r above the noise floor - hence "
            "megawatt transmitters and huge apertures for long range."
        ),
        "key_points": [
            "RCS sigma = 4 pi R^2 |E_s|^2/|E_i|^2 (m^2, dBsm): electromagnetic size, not physical size.",
            "Regimes: Rayleigh (~1/lambda^4, tiny), Mie resonance (~lambda), optical (~projected area; sphere = pi a^2).",
            "Flat plate at normal incidence: sigma = 4 pi A^2/lambda^2 - huge; stealth tilts surfaces away.",
            "Radar equation: P_r = P_t G_t G_r lambda^2 sigma/(4 pi)^3 R^4 - the R^4 law (12 dB per range doubling).",
            "Stealth = shaping + absorbent materials + edge treatment; corner reflectors do the opposite deliberately.",
        ],
        "requirements": [
            "Friis equation (the radar equation is two Friis hops).",
            "Scattering intuition: induced currents re-radiate.",
            "Decibel comfort (dBsm = dB relative to 1 m^2).",
        ],
        "standards": [
            "RCS quoted in dBsm; calibration via spheres and corner reflectors of known sigma.",
            "IEEE Std 1502 guides RCS measurement practice.",
        ],
        "citations": [C_SKOLNIK, C_BALANIS_AEM, C_KRAUS],
        "sig_lens": (
            "Signature take: radar cross section is the Signature shadow "
            "puppet - the shape a radar sees need not match the shape "
            "that is there. His framing treats stealth as shadow-craft: "
            "sculpt the scattered wave and the giant becomes a bird."
        ),
    },
    {
        "key": "radar_fundamentals",
        "name": "Radar Fundamentals: Pulses, Echoes, and Doppler",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Radar (radio detection and ranging) fires electromagnetic "
            "pulses and listens for echoes: range from delay (R = c delta_t "
            "/ 2 - divide by two for the round trip), direction from the "
            "antenna's beam, and radial velocity from the Doppler shift "
            "(f_d = 2 v / lambda, positive for approaching targets). A 100-"
            "microsecond echo delay means 15 km; a 300 m/s jet at 10 GHz "
            "(lambda = 3 cm) shifts the echo 20 kHz. Pulsed radar trades "
            "range resolution (c tau / 2 for pulse width tau) against "
            "average power; pulse-Doppler radar separates moving targets "
            "from ground clutter by frequency; continuous-wave Doppler "
            "radar (police guns, door openers) measures speed with no "
            "pulsing at all. The maximum unambiguous range R_unamb = c / 2 "
            "PRF: echoes arriving after the next pulse transmit are "
            "misread as close - range-Doppler ambiguity is the central "
            "design tension of every radar."
        ),
        "how_it_works": (
            "Transmit a short pulse: the leading edge travels to the "
            "target and back; the receiver timestamps the echo. Range "
            "resolution: two targets merge if their echoes overlap, so "
            "delta_R = c tau / 2 - shorter pulses (or pulse compression: "
            "long coded pulses squeezed by matched filtering to the "
            "bandwidth limit c/2B) resolve finer. Doppler: each wave crest "
            "reflects off a target advanced by v T, compressing the echo "
            "wavelength; the frequency shift f_d = 2 v_r / lambda measures "
            "radial velocity to m/s precision - weather radar's tornado "
            "signatures are Doppler couplets. PRF sets the rhythm: high "
            "PRF sees fast Dopplers unambiguously but folds distant ranges "
            "(second-time-around echoes); low PRF sees far but folds fast "
            "velocities. Medium-PRF with multiple PRFs resolves both - the "
            "art of radar waveform design. Integration over N pulses "
            "improves SNR by ~N (coherent) or ~sqrt(N) (noncoherent)."
        ),
        "key_points": [
            "Range R = c delta_t / 2; Doppler f_d = 2 v_r / lambda gives radial velocity.",
            "Range resolution delta_R = c tau / 2 (pulse) or c/2B (pulse-compression bandwidth).",
            "Pulse-Doppler separates movers from clutter by frequency; CW Doppler measures speed directly.",
            "Unambiguous range R_unamb = c/2PRF; the range-Doppler ambiguity is the core design trade.",
            "Pulse compression (matched filtering) gets fine resolution without sacrificing average power.",
        ],
        "requirements": [
            "Scattering/RCS record (where echoes come from).",
            "Wave speed c and frequency-wavelength relation.",
            "Doppler intuition: approaching waves bunch up.",
        ],
        "standards": [
            "Radar bands lettered per IEEE Std 521 (L, S, C, X, Ku, K, Ka).",
            "ATC/weather radars operate under ITU-R and national spectrum allocations.",
        ],
        "citations": [C_SKOLNIK, C_BALANIS_ANT, C_ULABY],
        "sig_lens": (
            "Signature take: radar is the Signature echo-location - "
            "shouting into the dark and reading the returning whispers "
            "for distance and speed. His framing treats every pulse as "
            "a question and every echo as an answer, with Doppler as "
            "the tone of voice."
        ),
    },
    {
        "key": "emc_emi",
        "name": "EMI and EMC: When Fields Misbehave - Emissions and Immunity",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Electromagnetic compatibility (EMC) is the discipline of "
            "peaceful coexistence: every device must neither emit "
            "intolerable interference (EMI) nor succumb to the interference "
            "around it (immunity/susceptibility). Digital edges with "
            "sub-nanosecond rise times are accidental radio transmitters - "
            "a 1-ns edge has significant energy past 300 MHz - and cables "
            "are accidental antennas, so emissions testing (FCC Part 15, "
            "CISPR 22/32) measures radiated fields at 3-10 m against "
            "microvolt-per-meter limits. Coupling paths are the curriculum: "
            "conducted (shared power/ground impedance), radiated (field-to-"
            "cable/loop pickup), capacitive crosstalk, inductive crosstalk. "
            "The fixes are the EMC canon: solid ground planes, short return "
            "loops (small loop area = small emissions AND small pickup), "
            "filtering at enclosure boundaries, shielding with attention to "
            "seams and apertures (a slot radiates like its longest "
            "dimension), and spread-spectrum clocking."
        ),
        "how_it_works": (
            "Model the aggressor: a switching current loop of area A at "
            "frequency f radiates E proportional to f^2 A I / r - doubling "
            "the loop area or the edge rate quadruples emissions, which is "
            "why tight layout (signal over unbroken ground plane, minimal "
            "loop area) is the first defense. Shielding effectiveness SE = "
            "R + A + B (reflection + absorption + multiple-reflection "
            "terms): reflection dominates for electric fields at thin "
            "shields, absorption A = 8.686 t/delta dB dominates for magnetic "
            "fields in thick shields - 1 mm of copper at 1 MHz (delta ~ 66 "
            "um) absorbs ~130 dB. But apertures leak: a slot of length l "
            "radiates like a dipole below lambda/2 resonance, so enclosures "
            "use waveguide-below-cutoff honeycomb vents and conductive "
            "gaskets. Immunity testing (IEC 61000-4-x) fires ESD guns (8 kV "
            "contact), radiated fields (3-10 V/m), bursts, and surges at the "
            "device - it must keep working. Filter at the boundary: every "
            "cable penetrating a shield gets filtered where it crosses, or "
            "the shield is decorative."
        ),
        "key_points": [
            "EMC = low emissions + high immunity; EMI is the interference itself (conducted, radiated, crosstalk).",
            "Fast edges + loop area radiate: E ~ f^2 A I / r - tight layout with solid ground planes is the first fix.",
            "Shielding SE = reflection + absorption (8.686 t/delta dB) + re-reflection; apertures leak like slot antennas.",
            "Filter every cable at the shield boundary; gaskets and honeycomb vents preserve enclosure integrity.",
            "Compliance: FCC Part 15 / CISPR 32 emissions limits; IEC 61000-4-x immunity (ESD, radiated, burst, surge).",
        ],
        "requirements": [
            "Skin-depth record (absorption loss).",
            "Antenna records (loops and slots radiate - intentionally or not).",
            "Faraday's law (changing flux induces in victim loops).",
        ],
        "standards": [
            "FCC Part 15 Subpart B / CISPR 32: radiated emissions limits (e.g. 30-88 MHz at 3 m).",
            "IEC 61000-4-2 (ESD), -4-3 (radiated immunity), -4-4 (burst), -4-5 (surge).",
        ],
        "citations": [C_PAUL, C_BALANIS_AEM, C_POZAR],
        "sig_lens": (
            "Signature take: EMC is the Signature good-neighbor law - "
            "every circuit must keep its fields to itself and tolerate "
            "its neighbors'. His framing treats the ground plane as the "
            "village green: keep your loops small, your edges civil, and "
            "no one complains to the FCC."
        ),
    },
    {
        "key": "computational_em",
        "name": "Computational Electromagnetics: FDTD, FEM, and the Method of Moments",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Computational electromagnetics (CEM) solves Maxwell's equations "
            "on computers where closed forms fail - real antennas, "
            "packages, and scattering targets. Three families dominate. "
            "FDTD (finite-difference time-domain): Yee's staggered grid "
            "marches E and H forward in time with central differences - "
            "simple, broadband (one run = whole spectrum), but the grid "
            "must resolve lambda/10-20 and the Courant limit S = c delta_t "
            "/ delta_x <= 1/sqrt(D) caps the time step. FEM (finite element "
            "method): unstructured tetrahedral meshes with variational "
            "formulation - the king of complex geometry (connectors, "
            "packages, cavities), at the cost of large sparse matrix "
            "solves. MoM (method of moments): integral-equation "
            "formulation on surfaces only - ideal for antennas and "
            "scattering in open space (no absorbing boundary needed), "
            "dense matrices limiting size. Together with high-frequency "
            "asymptotics (physical/geometrical optics), they design every "
            "modern antenna, filter, and package."
        ),
        "how_it_works": (
            "FDTD: discretize curl E = -mu partial H / partial t and curl H "
            "= epsilon partial E / partial t on Yee's grid - E components on "
            "cell edges, H on face centers, offset half a step in space and "
            "time (leapfrog). Update: H^{n+1/2} from E^n, then E^{n+1} from "
            "H^{n+1/2} - each step is local arithmetic, trivially "
            "parallel. Stability demands the Courant number S <= 1/sqrt(3) "
            "in 3D: the numerical wave must not outrun the physical one. "
            "Absorbing boundaries (PML - perfectly matched layer) fake "
            "infinite space. FEM: expand the field in basis functions on "
            "tetrahedra, apply Galerkin's method to the wave equation's "
            "weak form, solve the sparse system - superb for curved metal "
            "and dielectrics. MoM: expand surface currents in basis "
            "functions, enforce the boundary condition (E_tangential = 0) "
            "at test points - the EFIE - solve the dense Z-matrix; "
            "fast-multipole (FMM) acceleration reaches millions of "
            "unknowns. Rule of thumb: FDTD for broadband/transient, FEM "
            "for complex closed geometry, MoM for open-region antennas and "
            "RCS."
        ),
        "key_points": [
            "FDTD: Yee staggered grid, leapfrog time marching; broadband in one run; Courant S = c dt/dx <= 1/sqrt(D).",
            "FEM: unstructured meshes + variational form; best for complex geometry; large sparse solves.",
            "MoM: surface integral equations (EFIE); best for open-region antennas/RCS; dense matrices (FMM accelerates).",
            "PML absorbing boundaries fake infinite space for FDTD/FEM; MoM needs none.",
            "Asymptotics (PO/GO/UTD) handle electrically huge targets where full-wave is unaffordable.",
        ],
        "requirements": [
            "Maxwell's equations in differential form (what gets discretized).",
            "Boundary conditions (what MoM enforces, what PML absorbs).",
            "Wave-equation record (the PDE being solved).",
        ],
        "standards": [
            "IEEE Std 1597.1/1597.2 validate CEM codes against canonical problems.",
            "Convergence studies (mesh refinement) are required practice - an unconverged result is not a result.",
        ],
        "citations": [C_TAFLOVE, C_JIN, C_HARRINGTON],
        "sig_lens": (
            "Signature take: computational electromagnetics is the "
            "Signature wind tunnel - when the equations won't yield to "
            "pencil, build the field a digital twin and watch it fly. "
            "His framing treats Yee's grid as graph paper for lightning: "
            "discretize boldly, but respect the Courant limit."
        ),
    },
]
