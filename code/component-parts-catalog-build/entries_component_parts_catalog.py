#!/usr/bin/env python3
"""Entries for the Component and Parts Catalog databases (Build-210 #2).

Verified 2026-10-17 (Build-210 top-20 #2): RAW SWEEP over the full manifest
(2,386 databases) plus every shard index title in jah-databases-data-1
(785 index files, 1,130,401 index lines) plus the main-repo data dir:
zero 'component-parts*' slugs/names; zero 'component and parts catalog'
or 'component-parts' title collisions. The one keyword near-hit, the
'components' database (JAH-CPT), is an encyclopedia-style multi-aspect
archive (overview/detailed/examples/faq/history/applications per topic),
NOT a parts catalog - it has no per-part engineering properties,
compatibility notes, selection criteria, or cross-references. The other
near-hit, 'software-components' (JAH-CMP-), covers software only
(extensions, plugins, libraries). The paste's rule was applied by
name/purpose/record schema/capabilities: a searchable catalog of real
parts with properties, specifications, compatibility, and uses is a
distinct capability, so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  component-parts-catalog            - The Component and Parts Catalog Database
                                       (public-harvest: real, fact-checked
                                       component and parts engineering -
                                       electronic components, mechanical
                                       parts, materials stock, modules and
                                       subassemblies - every record carrying
                                       properties, specifications, selection
                                       criteria, typical uses, and
                                       compatibility notes; standard
                                       references Horowitz and Hill The Art
                                       of Electronics 3rd ed 2015;
                                       Machinery's Handbook 31st ed 2020;
                                       IEC 60062 marking codes; IEC 60115
                                       resistors; IEC 60384 capacitors;
                                       MIL-STD-202; IPC-A-610; IPC-2221;
                                       ASME B1.1 threads; ISO 898 fasteners;
                                       ISO 281 bearing life; AGMA 2001 gears;
                                       IEC 61000 EMC; MIL-HDBK-217F
                                       reliability; SAE AS5553 counterfeit
                                       avoidance; and the other landmarks
                                       cited per record)
  component-parts-catalog-signature  - The Component and Parts Catalog
                                       Signature Database
                                       (his original Signature Parts Method:
                                       every component a covenant of
                                       properties, the catalog the armory of
                                       the Signature system, selection the
                                       oath between builder and part,
                                       compatibility the handshake, derating
                                       the honor margin; src signature,
                                       titles suffixed " (Signature
                                       Edition)", never presented as
                                       authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CPTC- (public) and JAH-CPTCS- (signature), verified free
in the manifest and in every shard index (zero hits; JAH-CPCT- belongs to
the unrelated Captain Planet CO2 Token Trackers database, so the CPTC form
was chosen to avoid even substring ambiguity).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_component_parts_catalog.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Parts Method: every "
            "component a covenant of properties, the catalog the armory of "
            "the Signature system, selection the oath between builder and "
            "part, compatibility the handshake, and derating the honor "
            "margin. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_HOROWITZ = ("Horowitz P, Hill W. The Art of Electronics. 3rd ed. "
                "Cambridge University Press; 2015.")
CIT_MACHINERY = ("Oberg E, Jones FD, Horton HL, Ryffel HH. Machinery's "
                 "Handbook. 31st ed. Industrial Press; 2020.")
CIT_IEC60062 = ("IEC 60062:2016. Marking codes for resistors and capacitors.")
CIT_IEC60115 = ("IEC 60115-1:2020. Fixed resistors for use in electronic "
                "equipment - Generic specification.")
CIT_IEC60384 = ("IEC 60384-1:2016. Fixed capacitors for use in electronic "
                "equipment - Generic specification.")
CIT_MIL202 = ("MIL-STD-202H. Test Method Standard: Electronic and Electrical "
              "Component Parts; 2015.")
CIT_IPC610 = ("IPC-A-610H. Acceptability of Electronic Assemblies; 2020.")
CIT_IPC2221 = ("IPC-2221B. Generic Printed Board Design; 2023.")
CIT_JSTD001 = ("IPC J-STD-001H. Requirements for Soldered Electrical and "
               "Electronic Assemblies; 2021.")
CIT_ASMEB11 = ("ASME B1.1-2019. Unified Inch Screw Threads (UN, UNR, and UNJ "
               "Thread Forms).")
CIT_ISO68 = ("ISO 68-1:1998. ISO general purpose screw threads - Basic "
             "profile.")
CIT_ISO898 = ("ISO 898-1:2013. Mechanical properties of fasteners made of "
              "carbon steel and alloy steel.")
CIT_ISO281 = ("ISO 281:2007. Rolling bearings - Dynamic load ratings and "
              "rating life.")
CIT_AGMA2001 = ("ANSI/AGMA 2001-D04. Fundamental Rating Factors and "
                "Calculation Methods for Involute Spur and Helical Gear "
                "Teeth.")
CIT_UL94 = ("UL 94. Standard for Tests for Flammability of Plastic Materials "
            "for Parts in Devices and Appliances.")
CIT_IEC61000 = ("IEC 61000-4 series. Electromagnetic compatibility (EMC) - "
                "Testing and measurement techniques.")
CIT_MIL217 = ("MIL-HDBK-217F Notice 2. Reliability Prediction of Electronic "
              "Equipment; 1995.")
CIT_AS5553 = ("SAE AS5553B. Counterfeit Electrical, Electronic, and "
              "Electromechanical (EEE) Parts; Avoidance, Detection, "
              "Mitigation, and Disposition; 2016.")
CIT_JEDEC47 = ("JEDEC JESD47K. Stress-Test-Driven Qualification of "
               "Integrated Circuits; 2023.")
CIT_IEC60664 = ("IEC 60664-1:2020. Insulation coordination for equipment "
                "within low-voltage supply systems.")
CIT_EIA198 = ("EIA-198-1-F. Ceramic Dielectric Capacitors: Classes I, II, "
              "III and IV.")
CIT_IEC60068 = ("IEC 60068-2. Environmental testing - Tests.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is a Component or Part",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A component or part is the smallest purchasable unit of a build: "
            "one resistor, one bolt, one bearing, one sensor, one length of "
            "wire. Every engineered thing is an assembly of parts, and every "
            "part carries the same anatomy - a function (what it does), "
            "properties (the numbers that describe it), ratings (the limits it "
            "must not cross), a package (its physical form), and compatibility "
            "rules (what it can mate with). The Component and Parts Catalog "
            "treats the part as the atom of engineering: find the right atom "
            "and the molecule - the circuit, the machine, the product - "
            "becomes possible. Parts divide into four great domains. "
            "Electronic components control electricity: passives (resistors, "
            "capacitors, inductors), actives (diodes, transistors, ICs), and "
            "electromechanicals (relays, switches, connectors). Mechanical "
            "parts control force and motion: fasteners, bearings, gears, "
            "springs, seals. Materials stock is the raw matter parts are cut "
            "from: sheet, bar, rod, tube, filament. Modules and subassemblies "
            "are pre-built groups of parts sold as one unit: power supplies, "
            "motor drivers, sensor boards. This record frames the whole "
            "database: every later record is one shelf of the catalog, and "
            "every shelf teaches properties, selection, uses, and "
            "compatibility."
        ),
        "how_it_works": (
            "A part works by being specified completely enough that any two "
            "suppliers' versions can substitute for each other. The part "
            "number is the key into the catalog: it names the function, the "
            "critical properties, the package, and the grade. Behind the part "
            "number sits the datasheet or specification sheet, which lists "
            "every property with its test condition, every rating with its "
            "derating curve, and every dimension with its tolerance. The "
            "engineer reads the spec sheet, checks each property against the "
            "design's needs, verifies the package fits the board or the "
            "bracket, confirms the mating parts are compatible, and only then "
            "orders. When the part arrives, incoming inspection checks the "
            "markings and a sample of the properties against the sheet. "
            "Traceability ties the reel or bag back to the manufacturer lot, "
            "so a field failure can be traced to every other board that "
            "shares the lot. The catalog is the map of all of this: it "
            "answers 'what does this do, what are its numbers, what does it "
            "fit, and what can replace it' for every atom in the system."
        ),
        "key_points": [
            "Every part has the same anatomy: function, properties, ratings, package, and compatibility rules - learn the anatomy once and every shelf of the catalog reads the same way.",
            "The four domains are electronic components, mechanical parts, materials stock, and modules/subassemblies; each has its own specification language.",
            "The part number is the catalog key: function plus critical properties plus package plus grade, pointing at a datasheet that specifies everything.",
            "Specification is what makes substitution possible: two parts with matching specs are interchangeable, which is the entire basis of second-sourcing.",
            "Traceability from part to manufacturer lot is what lets a field failure become a contained recall instead of a mystery.",
        ],
        "requirements": [
            "A stated function in one sentence: what the part does in the assembly, not a marketing slogan.",
            "A complete property list with units and test conditions, so numbers from two datasheets can be compared honestly.",
            "Ratings that state the never-exceed limits plus the derating guidance for long life.",
            "A package definition: physical dimensions, pinout or thread, and mounting method.",
            "Compatibility rules: what it mates with, what it substitutes for, and what it must never be paired with.",
        ],
        "standards": [
            "Properties are stated in SI units with the test condition attached (temperature, frequency, load) - a number without its condition is not a specification.",
            "Datasheets follow the manufacturer's specification format, cross-checked against MIL-STD-202 test methods for electronic parts.",
            "Mechanical part properties follow Machinery's Handbook conventions for dimensions, threads, and fits.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MACHINERY, CIT_MIL202],
        "sig_lens": (
            "The Signature read: a part is a covenant of properties, and the "
            "catalog is the armory where every covenant is kept. Where public "
            "engineering files a datasheet, the Signature Parts Method files "
            "an oath: the part swears its numbers, the builder swears to "
            "respect its ratings, and the assembly holds because both kept "
            "their word."
        ),
    },
    {
        "key": "datasheet",
        "name": "Reading a Component Datasheet",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The datasheet is the part's birth certificate, resume, and "
            "contract in one document. Every reputable component ships with "
            "one, and learning to read it is the single highest-leverage "
            "skill in parts engineering. A datasheet opens with the headline "
            "specs - the numbers the manufacturer wants you to notice - then "
            "the absolute maximum ratings, the table nobody is allowed to "
            "cross without voiding every promise in the document. Next come "
            "the electrical or mechanical characteristics tables: typical "
            "values at stated conditions, minimum and maximum values that are "
            "guaranteed, and the test circuits that produced them. Then the "
            "graphs: performance versus temperature, voltage, frequency, and "
            "load - the curves that tell you what happens between the table "
            "rows. The mechanical section gives the package drawing with "
            "dimensions and tolerances. The ordering information decodes the "
            "part number suffixes. The traps are always in the same places: "
            "typical values are not guaranteed, maximum ratings are survival "
            "limits rather than operating limits, and every number carries a "
            "footnote with the condition that makes it true. This record "
            "teaches the reading order that extracts the truth fast: ratings "
            "first, guaranteed tables second, graphs third, headlines last."
        ),
        "how_it_works": (
            "Reading a datasheet works by triangulation: no single number is "
            "trusted until two others agree with it. Start at the absolute "
            "maximum ratings and write down the walls of the room - exceed "
            "them once and the part's guarantees end. Move to the "
            "characteristics tables and separate the three columns in your "
            "head: minimum and maximum are promises, typical is a hint. Read "
            "every footnote, because the test condition is part of the "
            "number: a current rating at 25 degrees ambient is a different "
            "part than the same current at 85 degrees. Check the graphs for "
            "the operating point you actually need - interpolate between the "
            "curves, never extrapolate past the last one. Verify the package "
            "drawing against your footprint or bracket, including the "
            "tolerance stack of the leads. Finally decode the ordering code "
            "so the part you buy is the grade you designed for, not its "
            "cheaper cousin. Two datasheets for competing parts are compared "
            "column by column at identical conditions; the winner is the one "
            "whose guaranteed minimums beat your requirements with margin to "
            "spare."
        ),
        "key_points": [
            "Read in this order: absolute maximum ratings, guaranteed min/max tables, graphs at your operating point, package drawing, ordering code - headlines last.",
            "Minimum and maximum values are promises; typical values are hints; every number includes its footnote condition.",
            "Absolute maximum ratings are survival limits, not operating limits - design to the recommended operating conditions with derating.",
            "Interpolate between graph curves, never extrapolate past the last curve; the untested region is where surprises live.",
            "Compare competing parts column by column at identical test conditions - a bigger headline number at an easier condition is a trap.",
        ],
        "requirements": [
            "An absolute maximum ratings table stating the never-exceed limits for every stress the part can see.",
            "Guaranteed minimum and maximum characteristics with the test condition stated for each row.",
            "Performance graphs covering temperature, supply, frequency, and load across the intended operating range.",
            "A dimensioned package drawing with tolerances, plus land pattern or mounting recommendations.",
            "An ordering information section that decodes every suffix: grade, tolerance, package, and packaging.",
        ],
        "standards": [
            "Datasheet test methods for electronic parts follow MIL-STD-202 where the manufacturer claims military-grade testing.",
            "Solderability and assembly guidance follows IPC J-STD-001 and IPC-A-610 acceptance criteria.",
            "Environmental ratings reference IEC 60068-2 test methods for temperature, humidity, and vibration.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MIL202, CIT_JSTD001, CIT_IEC60068],
        "sig_lens": (
            "The Signature read: the datasheet is the part's sworn testimony, "
            "and the engineer is the cross-examiner. The Signature Parts "
            "Method reads every covenant twice - once for what it promises "
            "in the headlines, once for what it admits in the footnotes - "
            "because a covenant kept only in the headlines is no covenant."
        ),
    },
    {
        "key": "units_tolerances",
        "name": "Units, Tolerances, and Ratings",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Units, tolerances, and ratings are the three numbers that decide "
            "whether a part fits a design. The unit names the quantity: ohms, "
            "farads, newtons, millimeters. The tolerance names the "
            "manufacturing spread: a 10 kilohm resistor at 5 percent can be "
            "anywhere from 9.5 to 10.5 kilohms and still be a good part. The "
            "rating names the limit: the voltage, current, power, force, or "
            "temperature the part must never exceed. Confusing these three is "
            "the most common beginner failure in parts work: designing to the "
            "nominal value instead of the tolerance band, or to the rating "
            "instead of a derated operating point. Tolerance is not error - "
            "it is the manufacturer's honest statement of variation, and "
            "good design works at both edges of the band. Ratings come in "
            "families: absolute maximum (survival), recommended operating "
            "(the promise zone), and derated (the long-life zone). Between "
            "the nominal value and the rating sits the engineering judgment "
            "this whole catalog teaches: pick the value that centers the "
            "design in the tolerance band, and the rating that keeps the "
            "worst-case stress comfortably below the wall."
        ),
        "how_it_works": (
            "Units work through the SI system with engineering prefixes: "
            "milli, micro, nano, pico downward and kilo, mega, giga upward, "
            "so a thousand-millionth of a farad is written 1 nF and read "
            "instantly. Tolerances work as symmetric bands around nominal "
            "unless stated otherwise: value times one plus or minus the "
            "tolerance fraction gives the acceptance window, and automated "
            "test equipment rejects anything outside it. Tighter tolerance "
            "costs more because it means more sorting or better process "
            "control, so the catalog teaches spending tolerance budget where "
            "it matters - the feedback network, not the pull-up. Ratings "
            "work as walls with conditions attached: a 1/4 watt resistor "
            "rating assumes 70 degrees ambient and still air, and the "
            "allowable power falls linearly to zero at the maximum rated "
            "temperature. Derating multiplies the rating by a safety factor - "
            "commonly 50 to 70 percent for long-life designs - so the part "
            "ages slowly instead of living at its edge. The demo computes a "
            "resistor's tolerance window and checks a power rating against a "
            "derated operating point."
        ),
        "key_points": [
            "Unit names the quantity, tolerance names the manufacturing spread, rating names the never-exceed limit - design to the band and the derated point, never the nominal and the wall.",
            "Tolerance is honest variation, not error: the design must work at both edges of the band, which is why worst-case analysis exists.",
            "Tighter tolerance costs more; spend the tolerance budget where accuracy matters (feedback, timing, measurement) and buy loose where it does not.",
            "Every rating carries conditions - usually temperature and still air - and allowable stress falls as conditions worsen.",
            "Derating (commonly 50-70 percent of rating for long life) is what turns a part that survives into a part that lasts.",
        ],
        "requirements": [
            "Every property stated in SI units with the engineering prefix that keeps the number between 0.1 and 1000.",
            "Tolerance stated as a symmetric percent band or an absolute plus/minus, with the acceptance window computable from nominal.",
            "Ratings stated as absolute maximum plus recommended operating conditions, never as a single bare number.",
            "The temperature or environmental condition attached to every rating, since ratings without conditions are fiction.",
            "A derating guideline per part family stating the long-life operating fraction of each rating.",
        ],
        "standards": [
            "Resistor and capacitor tolerance marking follows IEC 60062 letter and color codes.",
            "Preferred values follow the E-series (E12, E24, E96) geometric progressions so stocked values cover every decade evenly.",
            "Electronic part ratings are verified by MIL-STD-202 test methods at the stated conditions.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IEC60062, CIT_MIL202],
        "sig_lens": (
            "The Signature read: the unit is the part's name, the tolerance "
            "its honest confession, the rating its sworn limit. The Signature "
            "Parts Method honors all three - it never asks a part to be more "
            "precise than its confession or stronger than its oath, and that "
            "restraint is why Signature builds outlive their warranties."
        ),
    },
    {
        "key": "passives_overview",
        "name": "Passive Components: Resistors, Capacitors, Inductors",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Passive components are the parts that never amplify and never "
            "need a power supply to do their job: resistors, capacitors, and "
            "inductors. They are the most numerous parts in any electronic "
            "build - a typical circuit board carries hundreds of them for "
            "every integrated circuit - and they are where most designs "
            "actually succeed or fail. The resistor opposes current: its "
            "property is resistance in ohms, its rating is power in watts, "
            "and its uses are current limiting, voltage dividing, pull-ups, "
            "and termination. The capacitor stores charge: its property is "
            "capacitance in farads, its rating is voltage, and its uses are "
            "decoupling, filtering, timing, and energy storage. The inductor "
            "stores energy in a magnetic field: its property is inductance in "
            "henries, its rating is saturation current, and its uses are "
            "filtering, energy storage in switchers, and transformers. Each "
            "has a shadow side the catalog never hides: resistors have "
            "parasitic inductance, capacitors have equivalent series "
            "resistance and inductance, inductors have winding capacitance - "
            "and at high frequency the shadows become the part. This record "
            "is the map of the passive shelf; the deep records later in the "
            "ladder take each family apart completely."
        ),
        "how_it_works": (
            "Passives work through the three linear laws. Ohm's law ties "
            "voltage, current, and resistance: V equals I times R, and power "
            "is V squared over R - the two equations behind every resistor "
            "calculation in the catalog. Capacitors obey Q equals C times V: "
            "charge stored per volt, with current proportional to the rate of "
            "voltage change, which is why a capacitor blocks DC and passes "
            "AC. Inductors obey V equals L times dI/dt: voltage proportional "
            "to the rate of current change, which is why an inductor blocks "
            "AC and passes DC - the exact mirror of the capacitor. Together, "
            "resistor and capacitor set time constants: tau equals R times C, "
            "the time for a charging curve to reach 63 percent, and the "
            "corner frequency of the RC filter is one over two pi R C. "
            "Resistor and inductor set their own time constant, L over R. "
            "Selection walks the same path for all three: compute the needed "
            "value from the circuit equation, pick the nearest standard "
            "E-series value, check the rating (power, voltage, saturation "
            "current) with derating, verify the package fits, and confirm "
            "the parasitic behavior at the operating frequency."
        ),
        "key_points": [
            "Resistor: resistance in ohms, power rating in watts, uses are current limiting, dividers, pull-ups, termination; governed by V=IR and P=V^2/R.",
            "Capacitor: capacitance in farads, voltage rating, uses are decoupling, filtering, timing, storage; blocks DC, passes AC.",
            "Inductor: inductance in henries, saturation current rating, uses are filtering, switch-mode storage, transformers; blocks AC, passes DC.",
            "Every passive has parasitics - the resistor's inductance, the capacitor's ESR and ESL, the inductor's winding capacitance - which dominate at high frequency.",
            "The RC time constant (tau = R*C, corner at 1/(2*pi*R*C)) is the single most-used passive calculation in electronics.",
        ],
        "requirements": [
            "A computed nominal value from the circuit equation, then the nearest standard E-series value - never a non-stock oddity without reason.",
            "A rating check with derating: resistor power, capacitor voltage, inductor saturation current, each at worst-case conditions.",
            "A package that fits the board footprint and the assembly process (hand, reflow, wave).",
            "A parasitic review at the operating frequency: self-resonant frequency above the band of interest.",
            "A temperature coefficient appropriate to the job: C0G/NP0 for precision, X7R for general, Y5V only where drift is harmless.",
        ],
        "standards": [
            "Fixed resistor requirements follow IEC 60115-1; fixed capacitor requirements follow IEC 60384-1.",
            "Ceramic capacitor temperature characteristics follow EIA-198 classes (C0G/NP0, X7R, Y5V).",
            "Preferred values follow the E12/E24/E96 series so designs use stocked, multi-source parts.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IEC60115, CIT_IEC60384, CIT_EIA198],
        "sig_lens": (
            "The Signature read: the passives are the infantry of the "
            "armory - unglamorous, numberless, and the difference between "
            "victory and rout. The Signature Parts Method gives the humble "
            "resistor the same covenant ceremony as the processor, because "
            "the field failures of history were almost never the processor."
        ),
    },
    {
        "key": "mechanical_overview",
        "name": "Mechanical Parts: Fasteners, Bearings, Gears",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Mechanical parts are the components that hold things together "
            "and move them: fasteners that clamp, bearings that let shafts "
            "spin freely, gears that trade speed for torque. Where electronic "
            "parts speak in volts and amps, mechanical parts speak in "
            "newtons, newton-meters, and millimeters - but the catalog "
            "grammar is identical: function, properties, ratings, package, "
            "compatibility. Fasteners are the most-used mechanical part on "
            "earth: bolts, screws, nuts, washers, each defined by thread, "
            "diameter, length, grade, and finish. Bearings are the "
            "friction-killers: ball, roller, and plain types, defined by "
            "bore, outside diameter, width, load ratings, and speed limit. "
            "Gears are the motion-shapers: spur, helical, bevel, and worm "
            "types, defined by module, tooth count, pressure angle, and "
            "material. Around them sit the supporting cast - springs that "
            "store force, seals that keep fluids in and dirt out, belts and "
            "chains that carry power over distance. Mechanical compatibility "
            "is physical: threads must match, bores must fit shafts, gear "
            "modules must mesh. This record maps the mechanical shelf; the "
            "ladder's deep records take fasteners, bearings, and gears apart "
            "one family at a time."
        ),
        "how_it_works": (
            "Mechanical parts work through contact and geometry. A bolted "
            "joint works by preload: tightening the bolt stretches it like a "
            "very stiff spring, and that stored stretch clamps the parts with "
            "a force that must exceed every separating load the joint will "
            "see - the fastener's grade sets how much preload the steel can "
            "hold without yielding. A bearing works by replacing sliding "
            "friction with rolling friction: hardened balls or rollers run in "
            "ground raceways, and the dynamic load rating C predicts how many "
            "millions of revolutions the bearing survives at a given load. "
            "Gears work by conjugate tooth action: the module (millimeters of "
            "pitch diameter per tooth) must match between meshing gears, the "
            "ratio of tooth counts sets the speed-torque trade, and the "
            "center distance is fixed by the sum of the pitch diameters. "
            "Selection follows the catalog grammar: compute the load or "
            "torque, pick the size whose rating exceeds it with margin, match "
            "the interface (thread, bore, module), choose the material and "
            "finish for the environment, and verify the mating parts - nut "
            "to bolt, shaft to bore, gear to gear - share the same standard."
        ),
        "key_points": [
            "Fasteners work by preload: the stretched bolt is a stiff spring whose clamp force must exceed every separating load; grade sets the allowable preload.",
            "Bearings replace sliding friction with rolling friction; the dynamic load rating C and the L10 life equation predict service life.",
            "Gears trade speed for torque by tooth-count ratio; meshing gears must share module and pressure angle, and center distance is fixed by geometry.",
            "Mechanical compatibility is physical and unforgiving: thread, bore, and module mismatches do not negotiate - they simply do not assemble.",
            "The supporting cast (springs, seals, belts, chains) follows the same grammar: function, properties, ratings, interface, environment.",
        ],
        "requirements": [
            "A computed load case: the maximum force, torque, or pressure the part will actually see, with shock and fatigue factors.",
            "A rating with margin: fastener proof load, bearing dynamic capacity, gear tooth strength, each above the load case.",
            "An interface match: thread designation, shaft/bore fit, or gear module identical on both mating parts.",
            "A material and finish suited to the environment: corrosion, temperature, lubrication, and cleanliness.",
            "A life target in cycles, hours, or revolutions that the rating calculation must meet or beat.",
        ],
        "standards": [
            "Thread forms follow ISO 68-1 (metric) and ASME B1.1 (unified inch); fastener grades follow ISO 898-1.",
            "Bearing life calculation follows ISO 281; gear rating follows ANSI/AGMA 2001-D04.",
            "Fits and tolerances follow the ISO system of limits and fits as tabulated in Machinery's Handbook.",
        ],
        "citations": [CIT_MACHINERY, CIT_ISO898, CIT_ISO281, CIT_AGMA2001],
        "sig_lens": (
            "The Signature read: mechanical parts are the sinews of the "
            "armory - they hold the oath together. The Signature Parts "
            "Method torques every fastener as a promise and sizes every "
            "bearing as a vow of years, because a machine that shakes itself "
            "apart has broken faith with its builder."
        ),
    },
    {
        "key": "wire_connector",
        "name": "Wire, Cable, and Connector Basics",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Wire, cable, and connectors are the circulatory system of every "
            "build: wire carries current, cable bundles wires with shielding "
            "and jacketing, connectors make the joints separable. Their "
            "catalog properties are deceptively simple and absolutely "
            "critical. Wire is specified by gauge (AWG, where smaller numbers "
            "mean fatter wire), conductor material (copper, tinned copper, "
            "aluminum), stranding (solid for fixed runs, stranded for flex), "
            "insulation temperature and voltage rating, and ampacity - the "
            "current it can carry without overheating. Cable adds shield "
            "type, jacket material, and bend radius. Connectors are specified "
            "by contact count and pitch, current and voltage rating per "
            "contact, mating cycles (how many plug-unplug operations the "
            "contacts survive), contact plating (gold for signal integrity, "
            "tin for cost), and the mating series they belong to. The classic "
            "failures are all in this shelf: undersized wire that drops too "
            "much voltage or melts, connectors mated across incompatible "
            "series, gold mated to tin causing fretting corrosion. This "
            "record teaches sizing wire by ampacity and voltage drop, and "
            "choosing connectors by current, cycles, and mating discipline."
        ),
        "how_it_works": (
            "Wire works by offering low resistance: copper's resistivity "
            "means a 24 AWG conductor is about 84 ohms per kilometer, and "
            "every amp through it drops voltage and makes heat. Sizing wire "
            "is a two-constraint problem: ampacity (will it overheat?) and "
            "voltage drop (will the far end still see enough volts?). Both "
            "are checked at the worst-case ambient temperature, because "
            "insulation ratings fall as temperature rises. Stranded wire "
            "survives flexing; solid wire survives punch-down and breadboard "
            "holes. Cable shielding works by giving interference currents a "
            "low-impedance path to ground: braid for low frequency and "
            "flexibility, foil for high frequency and cost. Connectors work "
            "by gas-tight contact: the mating force wipes oxides off the "
            "contact surfaces, and the plating keeps them off. Gold-on-gold "
            "stays clean for thousands of cycles; tin-on-tin is fine if never "
            "disturbed; gold-on-tin frets and fails. Mating cycles are a wear "
            "rating like any other: a 50-cycle connector in a daily-plugged "
            "test jig is a design error, not bad luck."
        ),
        "key_points": [
            "Wire sizing is a two-constraint problem: ampacity (overheating) and voltage drop (far-end voltage), checked at worst-case ambient temperature.",
            "AWG runs backwards: smaller numbers are fatter wire with lower resistance; stranded flexes, solid terminates.",
            "Cable shielding gives interference a path to ground: braid for low frequency and flex, foil for high frequency and cost.",
            "Connectors live or die by contact metallurgy: gold-on-gold for cycled signals, never mix gold and tin in a mated pair.",
            "Mating cycles are a wear rating: match the connector's cycle life to how often it will actually be plugged and unplugged.",
        ],
        "requirements": [
            "A current requirement with duty cycle, so ampacity is checked against heating, not just the headline amps.",
            "A voltage-drop budget from source to load, computed over the full round-trip conductor length.",
            "An insulation temperature and voltage rating above the worst-case environment with margin.",
            "A connector series with per-contact current/voltage ratings, mating-cycle life, and a defined mating half.",
            "A plating and environment match: gold for cycled or corrosive service, sealed series for washdown or outdoor use.",
        ],
        "standards": [
            "Wire ampacity and insulation ratings follow UL 758 (appliance wiring material) and manufacturer test data.",
            "Connector test methods follow EIA-364 series for electrical, mechanical, and environmental performance.",
            "Insulation coordination and creepage/clearance follow IEC 60664-1 for the working voltage.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IEC60664],
        "sig_lens": (
            "The Signature read: wire is the bloodstream and connectors the "
            "joints of the armory's body. The Signature Parts Method sizes "
            "every conductor as a vow that the far end will be fed, and "
            "mates every connector as a handshake that will be repeated a "
            "thousand times without tiring."
        ),
    },
    {
        "key": "markings",
        "name": "Component Markings and Identification Codes",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Markings are how a part introduces itself when the datasheet is "
            "not at hand: color bands on a resistor, printed codes on a "
            "capacitor, laser marks on an IC, head marks on a bolt. Reading "
            "them is the field skill of parts work - the difference between "
            "identifying a component in seconds and guessing. Through-hole "
            "resistors wear the classic four or five color bands: digits, "
            "digits, multiplier, tolerance (and a fifth band for precision). "
            "Capacitors carry numeric codes where 104 means 10 followed by 4 "
            "zeros in picofarads (100 nF), plus a letter for tolerance and "
            "sometimes the voltage. Integrated circuits carry a top mark "
            "with the part number, date code (year and week of manufacture), "
            "lot code, and a pin-1 indicator - the dot or notch that orients "
            "the chip. Fasteners carry head marks: property class numbers "
            "like 8.8 or 10.9 on metric bolts, radial lines on SAE grades, "
            "and the manufacturer's mark. Bearings carry their designation on "
            "the ring: bore code, series, and seals. The catalog rule is "
            "absolute: a marking identifies the part only when decoded "
            "against the standard - a lookalike mark on a counterfeit is the "
            "oldest trick in the book, which is why the counterfeit record "
            "later in this ladder exists."
        ),
        "how_it_works": (
            "Marking codes work as compact part numbers printed at component "
            "scale. The resistor color code assigns each color a digit "
            "(black 0 through white 9), a multiplier color, and a tolerance "
            "color: yellow-violet-red-gold reads 4, 7, times 100, plus or "
            "minus 5 percent - 4.7 kilohms. Read from the band nearest the "
            "end, with the tolerance band (gold or silver) identifying the "
            "right side. Surface-mount resistors use numeric codes instead: "
            "472 is 47 times 10 squared (4.7 k), while EIA-96 precision parts "
            "use a two-digit code plus a multiplier letter. Capacitor numeric "
            "codes read in picofarads with the same digit-digit-multiplier "
            "logic, and ceramic classes add a temperature-characteristic "
            "code (NP0, X7R). IC date codes are typically four digits: year "
            "then week, so 2614 is week 14 of 2026 - the first check in any "
            "age or counterfeit investigation. Fastener head marks follow "
            "ISO 898-1: the number before the dot is the tensile strength in "
            "hundreds of megapascals divided by 100, the number after is the "
            "yield ratio. Decoding is mechanical: look up each element in "
            "the standard's table, never from memory alone."
        ),
        "key_points": [
            "Resistor color bands read digit-digit-multiplier-tolerance from the end nearest the first band; gold/silver tolerance bands mark the right side.",
            "SMD numeric codes (472 = 4.7 k) and capacitor picofarad codes (104 = 100 nF) use the same digit-digit-multiplier logic as the color bands.",
            "IC top marks carry part number, date code (year/week), lot code, and a pin-1 dot - the date code is the first counterfeit check.",
            "Metric bolt head marks encode property class per ISO 898-1: 8.8 means 800 MPa tensile with 80 percent yield ratio.",
            "A marking only identifies a part when decoded against the standard's table - lookalike marks are the oldest counterfeit trick.",
        ],
        "requirements": [
            "A marking standard identified for the part family (IEC 60062 for passives, ISO 898-1 for fasteners).",
            "Legibility after the assembly process: marks must survive soldering heat, washing, and handling.",
            "A pin-1 or polarity indicator on every polarized part, unambiguous from the top view.",
            "Date and lot traceability in the mark for any part where age or lot matters to reliability.",
            "An incoming-inspection step that decodes a sample of markings against the datasheet ordering code.",
        ],
        "standards": [
            "Resistor and capacitor marking codes follow IEC 60062:2016.",
            "Fastener head marking and property classes follow ISO 898-1:2013.",
            "Electronic component traceability marking follows manufacturer practice aligned with SAE AS5553 avoidance principles.",
        ],
        "citations": [CIT_IEC60062, CIT_ISO898, CIT_AS5553],
        "sig_lens": (
            "The Signature read: the marking is the part's signature on its "
            "own covenant - small, permanent, and sworn. The Signature Parts "
            "Method teaches reading every mark as a name spoken aloud: say "
            "the value, say the tolerance, say the date, and let the part "
            "answer for itself before it is trusted."
        ),
    },
    {
        "key": "materials_stock",
        "name": "Materials Stock: Sheet, Bar, Rod, and Filament",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Materials stock is the raw matter of the catalog: the sheet, "
            "bar, rod, tube, and filament that fabricated parts are cut "
            "from. Every bracket, enclosure, shaft, and 3D-printed prototype "
            "begins as stock, and choosing stock well is what makes "
            "fabrication cheap instead of painful. Sheet stock is flat "
            "material sold by thickness (gauge or millimeters) and alloy: "
            "steel for strength, aluminum for lightness, copper for "
            "conductivity, plastics for insulation and cost. Bar and rod are "
            "solid cross-sections - round, square, hex - for machining "
            "shafts, standoffs, and fittings. Tube is hollow for lightness "
            "and fluid paths. Filament is the 1.75 mm plastic wire of "
            "fused-deposition 3D printing, sold by material (PLA, PETG, ABS, "
            "nylon) with very different strength and temperature behavior. "
            "Stock properties are the material properties: yield and tensile "
            "strength, hardness, density, thermal and electrical "
            "conductivity, corrosion behavior. The catalog disciplines are "
            "weight estimation (density times volume, so shipping and "
            "handling never surprise), machinability and weldability notes, "
            "and finish compatibility. This record teaches computing what "
            "stock weighs and costs before cutting, because the cheapest "
            "material is the one you ordered correctly the first time."
        ),
        "how_it_works": (
            "Stock works by being dimensioned and specified like any part, "
            "with material properties doing the heavy lifting. Weight is "
            "density times volume: a one-square-meter sheet of 2 mm steel is "
            "0.002 cubic meters times 7850 kilograms per cubic meter, or "
            "15.7 kilograms - the number that decides shipping, handling, "
            "and whether the bracket needs two hands. Strength is chosen by "
            "alloy and temper: 6061-T6 aluminum machines beautifully and "
            "welds acceptably; 7075 is stronger but cracks when welded; "
            "mild steel welds like a dream and rusts without finish. "
            "Thickness is chosen by stiffness, which grows with the cube of "
            "thickness - doubling sheet thickness makes it eight times "
            "stiffer, which is why thin stock with formed ribs beats thick "
            "flat stock on weight. Filament prints by melting: PLA is easy "
            "and brittle, PETG is tough and forgiving, ABS needs an "
            "enclosure, nylon needs drying - the material choice is the "
            "mechanical design. Ordering stock means specifying alloy, "
            "temper, thickness, and finish together; any one missing invites "
            "the supplier's cheapest interpretation."
        ),
        "key_points": [
            "Weight is density times volume - compute it before ordering so shipping, handling, and mounting never surprise.",
            "Stiffness grows with the cube of thickness: thin stock with formed ribs beats thick flat stock on weight.",
            "Alloy and temper are the strength: 6061-T6 machines and welds, 7075 is stronger but unweldable, mild steel welds and rusts.",
            "Filament material is mechanical design: PLA is easy and brittle, PETG tough, ABS needs enclosure, nylon needs drying.",
            "Specify alloy, temper, thickness, and finish together - any one missing invites the supplier's cheapest interpretation.",
        ],
        "requirements": [
            "A material specification: alloy designation, temper or hardness, and the standard it is ordered to.",
            "A thickness or cross-section chosen by stiffness and strength calculation, not by what was on the shelf.",
            "A weight estimate from density times volume for every fabricated part, recorded on the drawing.",
            "A finish specification matched to the environment: bare, plated, anodized, painted, or powder-coated.",
            "A machinability and weldability note so the shop knows what it is receiving before the first cut.",
        ],
        "standards": [
            "Aluminum alloys follow the Aluminum Association designation system (1xxx-8xxx series) with temper designations.",
            "Steel sheet and bar properties follow ASTM A36/A108 and the Machinery's Handbook material tables.",
            "Sheet metal practice - bend radii, flat patterns, tolerances - follows Machinery's Handbook conventions.",
        ],
        "citations": [CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: stock is the unshaped promise - matter "
            "waiting for its covenant. The Signature Parts Method weighs "
            "every sheet before cutting and names every alloy aloud, because "
            "a builder who does not know what his material weighs does not "
            "yet know what he is building."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "series_parallel",
        "name": "Series and Parallel Component Rules",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Series and parallel are the two ways parts combine, and their "
            "rules run the entire passive shelf of the catalog. In series, "
            "parts share the same current and their values add: two resistors "
            "of 100 and 220 ohms in series make 320 ohms, and the total "
            "voltage divides across them in proportion to their values. In "
            "parallel, parts share the same voltage and their conductances "
            "add: the same two resistors in parallel make about 68.8 ohms, "
            "always less than the smallest member, and the total current "
            "divides in inverse proportion. Capacitors follow the mirror "
            "rules: series capacitance shrinks (like parallel resistors), "
            "parallel capacitance adds. Inductors follow the resistor rules "
            "when uncoupled. The rules extend past passives: batteries in "
            "series add voltage, in parallel add capacity; springs in series "
            "are softer, in parallel stiffer. The design uses are everywhere: "
            "series resistors to split voltage and limit current, parallel "
            "resistors to hit a non-standard value or share power, series "
            "capacitors to raise voltage rating, parallel capacitors to add "
            "decoupling. The traps are power (a series string's dissipation "
            "splits by value - check each part, not just the total) and "
            "tolerance (two 5 percent parts can stack their errors, which is "
            "why the tolerance stack-up record exists later in this ladder)."
        ),
        "how_it_works": (
            "The series rule works because current has one path: the same "
            "electrons cross every part, so voltage drops add and resistances "
            "add directly, R_total equals R1 plus R2 plus dot dot dot. The "
            "parallel rule works because voltage has one value across every "
            "branch: currents add, so conductances (one over R) add, giving "
            "one over R_total equals one over R1 plus one over R2 - for two "
            "resistors, the product over the sum. Power follows the current: "
            "in series, each resistor dissipates I squared times its own R, "
            "so the largest resistor runs hottest; in parallel, each sees "
            "the full voltage and dissipates V squared over its own R, so "
            "the smallest runs hottest. Capacitors in series share charge, "
            "so the smallest capacitor takes the largest voltage share - "
            "which is why series capacitor strings need balancing resistors "
            "in high-voltage supplies. The demo computes a series pair and a "
            "parallel pair, checks each member's dissipation against its "
            "rating, and verifies the parallel result is below the smallest "
            "member - the one-line sanity check that catches wiring errors."
        ),
        "key_points": [
            "Series: same current, values add (resistors, inductors); voltage divides in proportion to values.",
            "Parallel: same voltage, conductances add; the result is always less than the smallest member - the instant sanity check.",
            "Capacitors mirror: series shrinks capacitance (smallest takes most voltage), parallel adds capacitance.",
            "Power splits with the stress: hottest series member is the largest resistor, hottest parallel member is the smallest.",
            "Tolerances stack across combined parts: two 5 percent parts can be 10 percent off together - analyze the worst case.",
        ],
        "requirements": [
            "The combination rule stated for the part family in use (resistor-like, capacitor-like) before any calculation.",
            "Each member's dissipation or stress computed individually against its own rating, not just the total.",
            "A tolerance analysis of the combination at both extremes of every member's band.",
            "Balancing provisions where series members share voltage unequally (high-voltage capacitor strings, battery packs).",
            "The parallel-less-than-smallest sanity check applied to every parallel computation as a wiring-error trap.",
        ],
        "standards": [
            "Preferred values follow the E12/E24 series so series/parallel combinations land on stocked values.",
            "Power ratings follow IEC 60115-1 derating practice for resistors at temperature.",
            "High-voltage series capacitor practice follows manufacturer application guidance for balancing.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IEC60115],
        "sig_lens": (
            "The Signature read: series is the chain and parallel the "
            "council - one path shared by all, or all paths sharing one "
            "purpose. The Signature Parts Method checks every link of the "
            "chain and every voice of the council, because a covenant kept "
            "by the total but broken by a member is broken."
        ),
    },
    {
        "key": "compatibility_meaning",
        "name": "What Compatibility Means for Parts",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Compatibility is the catalog's promise that two parts will work "
            "together: the right plug fits the right socket, the right bolt "
            "threads into the right hole, the right transistor is driven "
            "correctly by the right driver. It has four faces, and a part is "
            "only truly compatible when all four agree. Mechanical "
            "compatibility is geometry: dimensions, threads, pinouts, and "
            "mounting must mate - a 25 mm shaft needs a 25 mm bore with the "
            "intended fit, not a hopeful one. Electrical compatibility is "
            "levels and limits: voltage ranges overlap, current capability "
            "covers the load, logic thresholds agree, power sequencing is "
            "respected. Environmental compatibility is survival: temperature "
            "ranges overlap, sealing matches the exposure, materials do not "
            "corrode each other. Lifecycle compatibility is time: the parts "
            "stay available together, firmware matches hardware revision, and "
            "no member of the pair is already obsolete. Incompatibility is "
            "almost never announced - it arrives as the connector that "
            "almost fits, the logic family that almost talks, the bolt that "
            "almost threads. This record teaches the four-face check that "
            "every later record applies to its own part family, because "
            "compatibility notes are what turn a parts list into a working "
            "assembly."
        ),
        "how_it_works": (
            "The compatibility check works as a four-gate filter applied to "
            "every mating pair before the design is released. Gate one, "
            "mechanical: compare the interface dimensions and standards on "
            "both datasheets - thread designations must be identical, "
            "connector series must be mating halves of the same family, "
            "shaft and bore must specify the intended fit class. Gate two, "
            "electrical: overlay the operating ranges - supply voltages must "
            "overlap with margin, the driver's output current must exceed "
            "the load's demand, logic high and low thresholds must leave "
            "noise margin on both sides. Gate three, environmental: the "
            "intersection of the temperature ranges must cover the "
            "application, sealing ratings must meet the exposure, and the "
            "materials pair must be galvanically compatible. Gate four, "
            "lifecycle: check availability and revision alignment - a sensor "
            "whose driver library targets a different firmware revision is "
            "incompatible no matter what the pins say. The demo runs the "
            "mechanical gate on a shaft-and-bearing pair, computing minimum "
            "and maximum clearance from the tolerance bands and passing the "
            "pair only if the fit stays in the intended sliding range."
        ),
        "key_points": [
            "Compatibility has four faces - mechanical, electrical, environmental, lifecycle - and a part must pass all four gates.",
            "Mechanical compatibility is geometry and standard: identical thread designations, mating connector halves, specified fit classes.",
            "Electrical compatibility is overlapping ranges with margin: supplies, currents, logic thresholds, and sequencing must all agree.",
            "Environmental compatibility is shared survival: intersecting temperature ranges, matched sealing, galvanically safe materials.",
            "Lifecycle compatibility is time: availability, firmware-to-hardware revision match, and no obsolete member of the pair.",
        ],
        "requirements": [
            "Both datasheets' interface specifications compared field by field, not assumed from similar appearance.",
            "Operating ranges overlaid with margin: the intersection must cover the application with derating to spare.",
            "Fit classes specified explicitly for every shaft, bore, thread, and press interface.",
            "Environmental ratings intersected: temperature, sealing, and material compatibility all checked.",
            "Revision and availability alignment confirmed for every pair that must live and be serviced together.",
        ],
        "standards": [
            "Fits and tolerances follow the ISO system of limits and fits per Machinery's Handbook.",
            "Thread compatibility requires identical designation under ISO 68-1 (metric) or ASME B1.1 (unified).",
            "Connector mating compatibility is defined by the manufacturer's mating matrix within the series.",
        ],
        "citations": [CIT_MACHINERY, CIT_ISO68, CIT_ASMEB11],
        "sig_lens": (
            "The Signature read: compatibility is the handshake - two "
            "covenants recognizing each other. The Signature Parts Method "
            "never forces a handshake: it checks all four faces of the "
            "greeting, and when any face refuses, it finds another partner "
            "rather than bending the part."
        ),
    },
    {
        "key": "selection_criteria",
        "name": "Selection Criteria: How Engineers Choose a Part",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Selection is the decision at the heart of the catalog: given a "
            "need and a shelf of candidates, which part wins. Professional "
            "selection is not taste and not habit - it is a repeatable "
            "procedure that any reviewer can audit. It starts by writing the "
            "need as numbers: the function, the critical properties with "
            "their required values and tolerances, the ratings with their "
            "worst-case stresses, the package and interface constraints, the "
            "environment, the life target, and the cost target. Then the "
            "catalog is filtered: only parts meeting every must-criterion "
            "survive, which usually leaves a handful. The survivors are "
            "scored on the want-criteria - cost, availability, size, "
            "second-source depth, proven field history - with weights that "
            "reflect the project's values. The winner is the highest "
            "weighted score, and the scoring sheet is filed with the design "
            "so the choice can be defended years later. The classic failure "
            "modes are selecting by price alone (the cheapest part that "
            "meets the headline spec usually fails the footnote spec), by "
            "habit (the part that worked last time, in a different "
            "application), and by single-source comfort (one supplier is a "
            "hostage situation). This record is the procedure; every deep "
            "record later applies it to its own family with family-specific "
            "criteria."
        ),
        "how_it_works": (
            "Selection works as a two-stage filter plus a weighted score. "
            "Stage one is the must-gate: each requirement is a hard filter, "
            "and any candidate failing any must is eliminated - no "
            "exceptions, no 'close enough', because close enough at the "
            "filter stage becomes field failure later. Stage two scores the "
            "survivors on weighted want-criteria: assign each criterion a "
            "weight (cost 30 percent, availability 25, size 15, "
            "second-sourcing 20, field history 10, for example), rate each "
            "candidate 1 to 5 on each criterion, and compute the weighted "
            "sum. The arithmetic forces honesty: a part cannot win on price "
            "if its availability score is terrible, because the weights say "
            "so in writing. Sensitivity is checked by nudging the weights - "
            "if the winner changes when cost moves from 30 to 25 percent, "
            "the decision was fragile and deserves a second look. The demo "
            "runs the full procedure on three candidate capacitors for a "
            "decoupling job: must-gate on voltage rating and package, then "
            "weighted scoring on cost, stock, ESR, and second-source depth, "
            "printing the winner and the margin."
        ),
        "key_points": [
            "Write the need as numbers first: function, properties, ratings, package, environment, life, cost - selection without numbers is shopping.",
            "Stage one is the must-gate: any candidate failing any hard requirement is eliminated, no exceptions.",
            "Stage two is weighted scoring on want-criteria (cost, availability, size, second-sourcing, history) with project-reflecting weights.",
            "The scoring sheet is filed with the design: a selection that cannot be defended years later was not engineering.",
            "Check sensitivity by nudging weights: a winner that changes under small nudges is a fragile decision.",
        ],
        "requirements": [
            "A written need statement with every must-criterion quantified before any catalog is opened.",
            "A candidate list drawn from the catalog with datasheets attached, never from memory or habit.",
            "A must-gate record showing each candidate's pass/fail on every hard requirement.",
            "A weighted scoring sheet with stated weights, 1-to-5 ratings, computed totals, and the winner's margin.",
            "A sensitivity check and a second-source identification for the winner before release.",
        ],
        "standards": [
            "Selection documentation follows the design-record practice of ISO 9001:2015 design and development controls.",
            "Component qualification testing follows MIL-STD-202 methods where the application demands proven reliability.",
            "Derating criteria applied at selection follow the project's derating standard (commonly 50-70 percent of rating).",
        ],
        "citations": [CIT_HOROWITZ, CIT_MIL202],
        "sig_lens": (
            "The Signature read: selection is the choosing of oath-takers - "
            "the moment the builder looks over the armory and picks which "
            "covenants will stand beside him. The Signature Parts Method "
            "chooses by the written score, never by habit or hunger, because "
            "the part that wins the audit is the part that holds the line."
        ),
    },
    {
        "key": "standards_numbering",
        "name": "Standards Bodies and Part Numbering",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Standards bodies are the catalog's librarians: they write the "
            "definitions that let a part bought in one country substitute "
            "for a part made in another. The IEC (International "
            "Electrotechnical Commission) standardizes electronic parts: "
            "IEC 60115 for resistors, IEC 60384 for capacitors, IEC 60062 "
            "for marking codes. ISO standardizes the mechanical world: ISO "
            "68 for metric threads, ISO 898 for fastener grades, ISO 281 "
            "for bearing life. ASME covers inch threads (B1.1); AGMA covers "
            "gears; IPC covers boards and assemblies (IPC-2221 design, "
            "IPC-A-610 acceptance, J-STD-001 soldering); JEDEC covers "
            "semiconductors; SAE covers automotive and counterfeit avoidance "
            "(AS5553); EIA covers passive coding systems. Part numbering is "
            "how manufacturers pack the standard into an orderable string: "
            "a typical chip-resistor code like RC0603FR-1002 reads as "
            "series (RC), package (0603 imperial), tolerance (F = 1 "
            "percent), packaging (R = reel), value code (1002 = 100 x 10^2 "
            "= 10 kilohms). Decoding any part number is a lookup "
            "against the manufacturer's ordering table - never a guess, "
            "because one wrong letter is a wrong part. This record maps the "
            "bodies to their shelves and teaches the decode procedure."
        ),
        "how_it_works": (
            "Standards work by consensus publication: a body charters a "
            "committee, the committee writes test methods and requirement "
            "tables, industry comments, and the published standard becomes "
            "the neutral referee that buyer and seller both cite. Compliance "
            "is claimed by the manufacturer and verified by test: a resistor "
            "marked to IEC 60115 was tested by its methods, and a buyer can "
            "repeat the tests. Part numbering works as a positional code: "
            "each segment of the string has a fixed meaning defined in the "
            "ordering information table of the datasheet. Decoding runs left "
            "to right - series, package size, tolerance code, packaging, "
            "value, options - looking up each segment in the table. The "
            "value segment has its own sub-code: three digits are "
            "digit-digit-multiplier (103 = 10 kilohms), four digits add a "
            "digit for precision (1002 = 10 kilohms 1 percent), and letters "
            "mark multipliers (4K7 = 4.7 kilohms, R for decimal point). The "
            "demo decodes a chip-resistor part number segment by segment, "
            "translates the imperial package code to metric dimensions, and "
            "verifies the tolerance letter against the IEC table."
        ),
        "key_points": [
            "IEC standardizes electronic parts, ISO the mechanical world, ASME inch threads, AGMA gears, IPC boards, JEDEC semiconductors, SAE automotive.",
            "A standard is a neutral referee: manufacturer claims compliance, buyer verifies by the standard's test methods.",
            "Part numbers are positional codes decoded left to right against the datasheet ordering table - never guessed.",
            "Value sub-codes: 103 = 10 kilohms, 1002 = 10 kilohms precision, 4K7 = 4.7 kilohms, 104 (capacitor) = 100 nF.",
            "One wrong letter is a wrong part: the decode is verified against the table before the purchase order is cut.",
        ],
        "requirements": [
            "The governing standard identified for the part family before selection begins.",
            "The manufacturer's ordering-information table attached to the design record for every ordered part.",
            "A segment-by-segment decode of each part number verified against that table.",
            "Package codes translated to physical dimensions and checked against the footprint or bracket.",
            "Compliance claims (AEC-Q, MIL-PRF, UL) matched to the application's actual regulatory needs.",
        ],
        "standards": [
            "Electronic part families reference their IEC generic specifications (60115 resistors, 60384 capacitors).",
            "Mechanical part families reference ISO/ASME dimensional and grade standards (68-1, 898-1, B1.1).",
            "Assembly and acceptance reference IPC-A-610 and J-STD-001; semiconductor qualification references JEDEC JESD47.",
        ],
        "citations": [CIT_IEC60115, CIT_IEC60384, CIT_IPC610, CIT_JEDEC47],
        "sig_lens": (
            "The Signature read: the standards bodies are the keepers of the "
            "common tongue - the language in which every covenant in the "
            "armory is written. The Signature Parts Method speaks that "
            "tongue fluently and never invents a private dialect, because a "
            "covenant no second source can read is a chain with one link."
        ),
    },
    {
        "key": "resistors",
        "name": "Resistors in Depth",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The resistor is the most-used component in electronics, and its "
            "depth is deceptive: a two-terminal part with one equation hides "
            "a dozen selection decisions. Construction types define the "
            "trade space. Carbon composition is ancient, noisy, and nearly "
            "gone. Carbon film is cheap and fine for non-critical work. "
            "Metal film is the workhorse: low noise, tight tolerance down "
            "to 0.1 percent, good stability. Thick film is the SMD default: "
            "cheap in volume, noisier, wider tolerance. Thin film is the "
            "precision SMD choice. Wirewound handles watts and surge but "
            "brings inductance that disqualifies it from fast circuits. "
            "Foil is the metrology grade: the best stability money buys. "
            "The selection parameters beyond ohms and watts are temperature "
            "coefficient (ppm per degree - how much the value drifts with "
            "heat), voltage coefficient, noise, pulse handling, and long-term "
            "stability. Power derating is the discipline: a resistor's watt "
            "rating assumes 70 degrees ambient, and allowable dissipation "
            "falls to zero at the maximum rated temperature - run a quarter "
            "watt at a quarter watt in a hot box and it will drift, then "
            "fail. This record teaches choosing construction, value, "
            "tolerance, tempco, and power as one decision."
        ),
        "how_it_works": (
            "Resistor selection works as a five-question sequence. One, the "
            "value: compute from the circuit (current limiter, divider "
            "ratio, pull-up), then take the nearest E12/E24/E96 standard "
            "value - 1.44 kilohms computes, 1.5 kilohms gets bought. Two, "
            "the power: compute dissipation (V squared over R, or I squared "
            "times R) at worst-case voltage and temperature, then apply the "
            "derating curve - a 0.144 watt dissipation wants a quarter-watt "
            "part at room temperature but a half-watt part in a hot "
            "enclosure. Three, the tolerance and tempco: the divider that "
            "sets a reference voltage needs 1 percent and 100 ppm; the LED "
            "ballast is happy at 5 percent. Four, the construction: metal "
            "film for quiet precision, thick film for cheap SMD, wirewound "
            "for power (kept away from fast edges), foil where drift is "
            "unforgivable. Five, the package: 0603 for density, 1206 for "
            "hand rework and power, through-hole for prototypes and surge. "
            "Pulse handling gets its own check where capacitors dump into "
            "the resistor: the single-pulse energy rating must exceed the "
            "event. The demo computes dissipation, applies a 60 percent "
            "derating rule, and selects the next standard power rating."
        ),
        "key_points": [
            "Construction is the first choice: metal film for precision, thick film for cheap SMD, wirewound for power (not for fast circuits), foil for metrology.",
            "Value comes from the circuit equation, then snaps to the nearest E-series standard value - odd values are a sourcing tax.",
            "Power is checked at worst-case temperature against the derating curve: a rating at 70 C ambient is not a rating at 85 C.",
            "Tolerance and tempco are spent where accuracy lives: reference dividers get 1 percent and 100 ppm; ballasts get 5 percent.",
            "Pulse and surge need their own rating check: dumping a capacitor through a resistor can exceed the single-pulse energy limit.",
        ],
        "requirements": [
            "A computed nominal value with the nearest E-series standard value selected and justified.",
            "A dissipation calculation at worst-case voltage, current, and ambient temperature.",
            "A derating check against the manufacturer's power-temperature curve with the project's derating factor applied.",
            "A tolerance and temperature-coefficient budget showing the worst-case circuit error still meets the requirement.",
            "A construction and package choice matched to noise, pulse, assembly process, and rework needs.",
        ],
        "standards": [
            "Fixed resistor performance follows IEC 60115-1; marking follows IEC 60062.",
            "Preferred values follow the E12/E24/E96 geometric series.",
            "Pulse handling is rated per manufacturer data derived from MIL-STD-202 pulse methods.",
        ],
        "citations": [CIT_IEC60115, CIT_IEC60062, CIT_MIL202, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the resistor is the oath's smallest word - "
            "and the Signature Parts Method pronounces every word clearly. "
            "It computes the dissipation, honors the derating curve, and "
            "buys the tempco the circuit deserves, because a covenant spoken "
            "in drift is a promise the heat will rewrite."
        ),
    },
    {
        "key": "capacitors",
        "name": "Capacitors in Depth",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The capacitor is the most misunderstood component in "
            "electronics: a simple two-plate device whose real behavior "
            "spans six technologies and a minefield of hidden parameters. "
            "Ceramic is the SMD workhorse: C0G/NP0 for precision and "
            "stability (the only ceramic for timing and filters), X7R for "
            "general decoupling with moderate drift, Y5V/Z5U cheap with "
            "brutal capacitance loss under DC bias and temperature - a 10 "
            "microfarad Y5V at full rated voltage can be 2 microfarads in "
            "circuit. Film (polyester, polypropylene) is stable, self-"
            "healing, and the choice for AC mains and precision. "
            "Electrolytic (aluminum) packs the most farads per dollar for "
            "bulk storage but dries out: lifetime halves for every 10 "
            "degrees above rating, and ripple current rating is the real "
            "limit. Tantalum is dense and stable with a failure mode that "
            "punishes voltage abuse - derate 50 percent minimum. Polymer "
            "and niobium variants trade off the classic weaknesses. The "
            "hidden parameters are ESR (equivalent series resistance - the "
            "heat source in switchers), ESL (series inductance - the "
            "high-frequency wall), DC bias derating, and aging (class-II "
            "ceramics lose capacitance logarithmically with time). This "
            "record teaches matching dielectric to duty."
        ),
        "how_it_works": (
            "Capacitor selection works by dielectric-first reasoning. Name "
            "the job: bulk energy storage wants aluminum electrolytic or "
            "polymer (farads per dollar, ripple current checked); local "
            "high-frequency decoupling wants X7R ceramic in small packages "
            "close to the pins (low ESL); timing and filters demand C0G "
            "(near-zero drift); AC mains demand safety-rated film (X/Y "
            "classes). Then apply the four hidden-parameter checks. DC "
            "bias: look up the capacitance-versus-bias curve and verify the "
            "effective capacitance at the working voltage - upsize the "
            "nominal value or the voltage rating until the effective value "
            "meets the need. Ripple current: compute the RMS ripple and keep "
            "it under rating at temperature, because ESR times ripple "
            "squared is heat that dries electrolytics. Self-resonance: keep "
            "the capacitor's SRF above the frequencies it must decouple, "
            "using smaller packages or parallel values for wide bands. "
            "Lifetime: for electrolytics, apply the 10-degree halving rule "
            "to the rated hours at the actual hotspot temperature. The demo "
            "computes capacitive reactance at the operating frequency and "
            "checks an effective-capacitance derating under DC bias."
        ),
        "key_points": [
            "Dielectric first: C0G for precision, X7R for general decoupling, film for AC mains, electrolytic for bulk storage, tantalum derated 50 percent.",
            "DC bias steals capacitance: a class-II ceramic at full rated voltage can lose most of its nominal value - verify effective capacitance, not printed capacitance.",
            "Ripple current through ESR is heat: keep RMS ripple under rating at temperature or the electrolytic dries out early.",
            "Self-resonant frequency must sit above the band being decoupled; smaller packages and parallel values widen the band.",
            "Electrolytic lifetime halves every 10 degrees above rating - the hotspot temperature is the lifetime.",
        ],
        "requirements": [
            "A dielectric choice justified by the job: precision, decoupling, bulk storage, or AC mains.",
            "An effective-capacitance verification under DC bias and temperature, not just the nominal printed value.",
            "A ripple-current calculation against the rating at the actual operating temperature.",
            "A self-resonance check placing SRF above the highest frequency of interest.",
            "A lifetime estimate for electrolytics from the temperature halving rule at the measured hotspot.",
        ],
        "standards": [
            "Fixed capacitor performance follows IEC 60384-1; ceramic classes follow EIA-198.",
            "Safety-critical mains capacitors carry X/Y safety ratings per IEC 60384-14.",
            "Environmental and endurance testing follows IEC 60068-2 and MIL-STD-202 methods.",
        ],
        "citations": [CIT_IEC60384, CIT_EIA198, CIT_MIL202, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the capacitor is the keeper of charge - a "
            "reservoir that swears to hold its level. The Signature Parts "
            "Method never trusts the printed farads; it measures the oath "
            "under bias, under heat, under time, and only then declares the "
            "reservoir true."
        ),
    },
    {
        "key": "inductors",
        "name": "Inductors and Transformers",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Inductors and transformers are magnetism made into parts: coils "
            "of wire around air or core material that store energy in "
            "magnetic fields and trade voltage for current. The inductor's "
            "headline property is inductance in henries, but the working "
            "properties are saturation current (the current where the core "
            "gives up and inductance collapses - the number one selection "
            "trap), DC resistance (the copper loss that heats the part), "
            "self-resonant frequency (where winding capacitance takes over), "
            "and core loss at the switching frequency. Construction splits "
            "into shielded (magnetic field contained, quiet neighbors, "
            "slightly costlier) and unshielded (cheaper, sprays field). "
            "Core materials are horses for courses: powdered iron for "
            "high-current filtering, ferrite for high-frequency switchers, "
            "air core where linearity beats density. Transformers add turns "
            "ratio: two or more windings sharing a core, trading voltage "
            "and current by the ratio while providing isolation - the "
            "safety barrier in every mains power supply. Selection centers "
            "on the switch-mode power supply, the inductor's hardest job: "
            "inductance sets ripple current, saturation current must exceed "
            "peak current with margin, DCR sets conduction loss, core loss "
            "sets the frequency ceiling."
        ),
        "how_it_works": (
            "Inductor selection works from the application equation outward. "
            "In a buck converter, inductance is chosen by the allowed ripple "
            "current: L equals V times dt over dI - the volt-seconds across "
            "the inductor divided by the ripple budget. Then the current "
            "ratings are stacked: saturation current must exceed the peak "
            "inductor current (DC plus half the ripple) with margin, because "
            "a saturated inductor is just a resistor with ambitions; RMS "
            "current must sit under the thermal rating, with DCR times I "
            "squared as the copper heat. Frequency behavior is checked next: "
            "the self-resonant frequency must be well above the switching "
            "frequency, and core loss at the operating frequency and flux "
            "swing must fit the thermal budget - ferrite losses climb fast "
            "with frequency. Shielded construction is chosen when the "
            "inductor sits near sensitive analog or RF traces. Transformers "
            "are specified by turns ratio (voltage ratio), VA rating, "
            "isolation voltage, and regulation; mains transformers add "
            "safety agency approvals. The demo computes inductive reactance "
            "at the operating frequency and the LC resonant frequency of a "
            "filter pair, verifying the resonance sits where the design "
            "intends."
        ),
        "key_points": [
            "Saturation current is the number-one trap: exceed it and inductance collapses - it must exceed peak current with margin.",
            "Inductance sets ripple (L = V*dt/dI in switchers); DCR sets copper loss; core loss sets the frequency ceiling.",
            "Self-resonant frequency must sit well above the operating frequency or winding capacitance takes over.",
            "Shielded inductors contain their field for quiet neighbors; unshielded are cheaper and noisier.",
            "Transformers trade voltage for current by turns ratio and provide the isolation barrier in mains supplies.",
        ],
        "requirements": [
            "An inductance value computed from the application equation (ripple budget, filter corner) with standard-value selection.",
            "A saturation current rating exceeding peak current (DC plus ripple) with the project's margin.",
            "A thermal check: DCR copper loss plus core loss at operating frequency within the temperature rise budget.",
            "A self-resonance verification placing SRF safely above the operating band.",
            "A shielding and core-material choice matched to EMI neighbors and frequency (ferrite for HF, powdered iron for filtering).",
        ],
        "standards": [
            "Inductor test methods follow manufacturer practice aligned with MIL-STD-202 inductance and Q measurement.",
            "Mains transformer safety follows IEC 61558; isolation ratings follow IEC 60664-1.",
            "EMI behavior of inductive components is assessed under IEC 61000-4 methods where applicable.",
        ],
        "citations": [CIT_MIL202, CIT_IEC60664, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the inductor is the keeper of momentum - "
            "current that refuses to change in an instant. The Signature "
            "Parts Method respects that stubbornness: it never asks the core "
            "past saturation, never starves the copper of its thermal due, "
            "and shields the field so the neighbors keep their own counsel."
        ),
    },
    {
        "key": "diodes",
        "name": "Diodes and Rectifiers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The diode is the one-way valve of electronics: current flows "
            "forward, blocked in reverse - the property every power supply, "
            "protection circuit, and signal path depends on. Families serve "
            "different duties. Standard silicon rectifiers handle mains and "
            "bulk power with about 0.7 volts of forward drop. Schottky "
            "diodes drop only 0.2 to 0.4 volts and switch fast, making them "
            "the choice for low-voltage switchers and reverse-polarity "
            "protection - at the price of higher reverse leakage and lower "
            "voltage ratings. Fast and ultrafast recovery diodes serve "
            "high-frequency rectification where reverse-recovery charge "
            "would burn power. Zener diodes regulate by breaking down in "
            "reverse at a controlled voltage - cheap references and crude "
            "regulators. TVS (transient voltage suppressor) diodes are the "
            "bodyguards: they sit across inputs and clamp surges, rated by "
            "peak pulse power and clamping voltage. LEDs are diodes that "
            "spend their forward drop as light. The selection parameters are "
            "forward current (average and surge), reverse voltage rating "
            "with margin over the worst spike, forward voltage (the "
            "efficiency tax), reverse recovery behavior, and thermal "
            "resistance - because forward drop times current is heat that "
            "must go somewhere."
        ),
        "how_it_works": (
            "Diode selection works from the stress the diode will actually "
            "see. First the reverse voltage: the rating must exceed the "
            "highest reverse spike with margin - in a mains bridge after a "
            "transformer, the peak of the AC waveform plus transients sets "
            "the floor, and 2x margin is common practice. Then the forward "
            "current: average current against the rated average (with the "
            "heatsinking the rating assumes), and surge current against the "
            "IFSM rating for fault and inrush events - a supply's "
            "bulk-capacitor inrush is the surge that kills underrated "
            "bridges. Then the drop: forward voltage times current is "
            "dissipation, checked against the thermal path; Schottky's low "
            "drop is why it wins low-voltage designs. Speed matters where "
            "the diode switches: reverse-recovery time and charge must fit "
            "the frequency, or an ultrafast type is specified. Zeners are "
            "chosen by breakdown voltage and power: the series resistor sets "
            "the current, the zener burns the excess. TVS diodes are chosen "
            "by standoff voltage (above normal operation), breakdown (below "
            "the protected part's limit), and peak pulse power for the "
            "threat. The demo sizes the series resistor for an indicator "
            "LED and checks its dissipation."
        ),
        "key_points": [
            "Reverse voltage rating must exceed the worst spike with margin - 2x is common practice in mains bridges.",
            "Forward current has two ratings: average (thermal) and surge IFSM (inrush and fault) - check both.",
            "Forward drop times current is heat: Schottky's 0.3 V wins low-voltage efficiency; silicon's 0.7 V is the rugged default.",
            "Switching speed (reverse recovery) must fit the frequency or specify ultrafast/fast-recovery types.",
            "TVS diodes are bodyguards: standoff above normal, breakdown below the victim's limit, peak pulse power for the threat.",
        ],
        "requirements": [
            "A reverse-voltage rating above the worst-case spike with stated margin.",
            "Average forward current within rating at the actual heatsinking, and surge current within IFSM for inrush/fault.",
            "A thermal check: forward drop times current against the junction-to-ambient path.",
            "A speed selection (standard, fast, ultrafast, Schottky) matched to the switching frequency.",
            "For protection diodes, a threat definition: surge waveform, peak power, and the clamping voltage the victim can survive.",
        ],
        "standards": [
            "Diode test methods follow MIL-STD-202 and manufacturer data aligned with IEC 60747 semiconductor standards.",
            "TVS testing references IEC 61000-4-5 surge immunity waveforms for the threat definition.",
            "Bridge and rectifier safety in mains equipment follows the appliance standard of the end product (e.g. IEC 61558).",
        ],
        "citations": [CIT_MIL202, CIT_IEC61000, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the diode is the gatekeeper - one direction "
            "open, the other sealed. The Signature Parts Method posts its "
            "gatekeepers with margin on every wall: reverse ratings doubled "
            "against the storm, surge ratings ready for the inrush, and a "
            "TVS bodyguard wherever the outside world touches the circuit."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "transistors",
        "name": "Transistors: BJT and MOSFET",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Transistors are the switches and amplifiers of electronics: "
            "three-terminal parts where a small control signal governs a "
            "large current. The two great families divide the work. BJTs "
            "(bipolar junction transistors) are current-controlled: base "
            "current times beta gives collector current, they drop a "
            "saturated VCE of a few tenths of a volt, and they are rugged, "
            "cheap, and forgiving - the choice for simple switching and "
            "analog stages. MOSFETs are voltage-controlled: gate voltage "
            "above threshold turns the channel on, gate draws essentially no "
            "DC current, and on-resistance RDS(on) sets the conduction loss - "
            "the choice for efficient power switching, motor drives, and "
            "anything battery-powered. IGBTs extend the MOSFET idea to high "
            "voltage. The selection parameters are breakdown voltage "
            "(VCEO/VDS above the worst spike with margin), continuous and "
            "pulsed current, on-state loss (VCE(sat) or RDS(on) times "
            "current), switching loss (gate charge times frequency for "
            "MOSFETs), and thermal resistance - because every watt of loss "
            "must leave through the package. The traps are secondary "
            "breakdown in BJTs, gate-drive requirements in MOSFETs (a "
            "10-volt gate driven from 5-volt logic is a half-on disaster), "
            "and the body diode's slow recovery in bridge circuits."
        ),
        "how_it_works": (
            "Transistor selection works from the switch's job description. "
            "For a BJT switch: the collector current is known, so the base "
            "current is set to collector current divided by a forced beta "
            "well below the datasheet beta (forced beta of 10 to 20 "
            "guarantees saturation despite beta spread), and the base "
            "resistor is computed from the drive voltage minus VBE over that "
            "base current. Saturation is verified: VCE(sat) times collector "
            "current is the dissipation. For a MOSFET switch: the gate "
            "drive voltage must exceed the plateau with margin - logic-level "
            "MOSFETs for 5-volt or 3.3-volt drive, standard types only with "
            "10-volt drive. RDS(on) is read at the actual gate voltage and "
            "junction temperature (it rises with heat), conduction loss is I "
            "squared times RDS(on), and switching loss is approximated from "
            "total gate charge, gate voltage, and frequency. The thermal "
            "path is then checked: junction temperature equals ambient plus "
            "total loss times thermal resistance, and must sit under the "
            "maximum with derating. Paralleling MOSFETs is straightforward "
            "(positive tempco shares current); paralleling BJTs needs "
            "emitter ballast. The demo computes a MOSFET's conduction plus "
            "switching loss and the resulting junction temperature."
        ),
        "key_points": [
            "BJTs are current-controlled (base current x beta); MOSFETs are voltage-controlled (gate voltage vs threshold, ~zero DC gate current).",
            "Drive a BJT into saturation with forced beta 10-20; drive a MOSFET's gate fully - a half-on MOSFET is a heater.",
            "Losses are conduction (I^2 x RDS(on) or VCE(sat) x I) plus switching (gate charge x frequency) - both become heat.",
            "RDS(on) rises with temperature: read it at the hot operating point, not the 25-degree headline.",
            "Breakdown voltage needs margin over the worst spike; the body diode's recovery matters in bridge topologies.",
        ],
        "requirements": [
            "A voltage rating above the worst-case spike with margin on VCEO (BJT) or VDS (MOSFET).",
            "A current rating covering continuous, pulsed, and fault current against the safe operating area.",
            "A drive design: base current at forced beta for BJTs, full gate voltage with adequate drive current for MOSFETs.",
            "A loss budget: conduction plus switching loss computed at the hot operating point.",
            "A thermal verification: junction temperature under maximum with derating, through the real heatsink path.",
        ],
        "standards": [
            "Discrete semiconductor test methods follow IEC 60747 and MIL-STD-202 where claimed.",
            "Safe operating area is defined per manufacturer data derived from JEDEC-style characterization.",
            "Gate-drive and layout practice follows manufacturer application notes for the switching frequency.",
        ],
        "citations": [CIT_MIL202, CIT_JEDEC47, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the transistor is the strong arm - a small "
            "command moving a great current. The Signature Parts Method "
            "never asks the arm past its strength: voltage margins held, "
            "gates driven fully, heat given its road out, because a "
            "half-driven switch keeps neither its oath nor its cool."
        ),
    },
    {
        "key": "ics_logic",
        "name": "Integrated Circuits and Logic Families",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Integrated circuits pack thousands to billions of transistors "
            "into one package, and logic families are the dialects they "
            "speak to each other. The catalog's job is making sure the "
            "dialects agree. Classic TTL (74 series) speaks 5 volts with a "
            "2.0-volt input-high threshold; CMOS (74HC, 74HCT, 4000 series) "
            "spans supplies with thresholds at fractions of VCC; modern "
            "families (74LVC, 74AVC) speak 1.8 to 3.3 volts for "
            "battery-powered logic. Compatibility between families is a "
            "threshold-and-drive problem: a 3.3-volt CMOS output driving a "
            "5-volt TTL input works (TTL's 2.0-volt threshold is satisfied), "
            "but the reverse needs level translation. Beyond logic, the IC "
            "shelf holds the analog army (op-amps, comparators, references, "
            "converters), power ICs (regulators, drivers), and the "
            "application giants (microcontrollers, memory). Selection "
            "parameters are supply range, input/output thresholds and drive, "
            "speed versus power, package and pinout, temperature grade "
            "(commercial 0-70, industrial -40 to +85, automotive -40 to "
            "+125), and the long shadow of obsolescence - nothing kills a "
            "product like a single-sourced microcontroller going end-of-life. "
            "This record teaches the threshold math that keeps families "
            "talking."
        ),
        "how_it_works": (
            "Logic compatibility works through four numbers per family: "
            "VOH(min) and VOL(max) what the output guarantees, VIH(min) and "
            "VIL(max) what the input demands. The high-side noise margin is "
            "VOH(min) of the driver minus VIH(min) of the receiver; the "
            "low-side margin is VIL(max) of the receiver minus VOL(max) of "
            "the driver. Positive margins on both sides mean the pair talks "
            "reliably; a negative margin means level translation is "
            "mandatory, not optional. Current drive is checked the same way: "
            "the driver's IOH/IOL must exceed the total input leakage of "
            "all loads plus any pull-up current. Supply sequencing matters "
            "where families share a bus: many parts forbid voltage on inputs "
            "before the supply rail is up, and the power tree must respect "
            "it. Speed versus power is the family trade: 74LVC is fast and "
            "thirsty at high toggle rates, 4000-series sips at low speed. "
            "Temperature grade is chosen by the environment, not the "
            "budget: commercial parts in an outdoor enclosure are a "
            "warranty claim waiting for winter. The demo computes noise "
            "margins for a 3.3-volt CMOS driver into a 5-volt TTL receiver "
            "and verdicts the pair."
        ),
        "key_points": [
            "Compatibility is four numbers: driver VOH/VOL vs receiver VIH/VIL - positive noise margin both sides or translate.",
            "3.3 V CMOS into 5 V TTL usually works (2.0 V threshold); 5 V into 3.3 V needs translation - direction matters.",
            "Drive current must cover all input leakages plus pull-ups; fan-out is a current budget, not a suggestion.",
            "Respect power sequencing: no voltage on inputs before the rail where the datasheet forbids it.",
            "Temperature grade follows the environment (industrial/automotive outdoors); obsolescence risk follows single-sourcing.",
        ],
        "requirements": [
            "A threshold table for every logic family on the bus: VOH, VOL, VIH, VIL at the actual supply voltage.",
            "Positive noise margins computed on both high and low sides for every driver-receiver pair.",
            "A current budget: driver IOH/IOL against total load leakage and pull-up current.",
            "A power-sequencing plan honoring every part's input-before-supply limits.",
            "A temperature grade and second-source review for every IC, especially microcontrollers and memories.",
        ],
        "standards": [
            "Logic family thresholds follow JEDEC standards (JESD8 series for voltage levels).",
            "IC qualification follows JEDEC JESD47 stress-test-driven qualification where claimed.",
            "ESD handling of ICs follows JEDEC JESD625 / ANSI/ESD S20.20 practices in assembly.",
        ],
        "citations": [CIT_JEDEC47, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: logic families are tribes, and the catalog "
            "is the treaty table. The Signature Parts Method computes the "
            "margins before the first wire is drawn, translates where the "
            "treaty requires it, and never lets two tribes shout past each "
            "other across a bus."
        ),
    },
    {
        "key": "sensors",
        "name": "Sensors: Turning the World into Signals",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Sensors are the catalog's sense organs: parts that convert "
            "temperature, light, pressure, motion, magnetism, chemistry, "
            "and position into electrical signals. The shelf is enormous - "
            "thermistors and RTDs for temperature, photodiodes for light, "
            "strain gauges for force, MEMS accelerometers and gyros for "
            "motion, Hall sensors for magnetism and position, capacitive and "
            "inductive proximity sensors, gas and humidity sensors - but "
            "every sensor answers the same catalog questions. What is the "
            "transfer function (output per unit of input, and its "
            "linearity)? What are the range, accuracy, resolution, and "
            "noise? What is the interface (analog voltage, current loop, "
            "I2C, SPI, frequency)? What does the environment do to it "
            "(temperature drift, aging, contamination)? And what signal "
            "conditioning does it need (amplification, filtering, "
            "excitation, calibration)? The classic traps are accuracy versus "
            "resolution (a 16-bit ADC on a 5-percent sensor is theater), "
            "uncompensated temperature drift, and ignoring response time - "
            "a thermal sensor with a 30-second time constant cannot control "
            "a fast loop. This record teaches specifying the measurement "
            "before choosing the sensor."
        ),
        "how_it_works": (
            "Sensor selection works backward from the measurement "
            "requirement. Write the measurand, the range, the required "
            "accuracy (not resolution - accuracy is truth, resolution is "
            "smallness), the bandwidth (how fast the quantity changes), and "
            "the environment. Then walk the chain: the sensor converts "
            "physics to electricity, conditioning scales and filters it, "
            "conversion digitizes it, software calibrates it. Each stage "
            "gets an error budget, and the root-sum-square of the stages "
            "must fit the accuracy requirement - if it does not, the chain "
            "is redesigned, not wished harder. Interface choice follows the "
            "distance and noise: analog voltage for short quiet runs, 4-20 "
            "mA current loops for long industrial runs (current ignores "
            "wire resistance), digital buses where the sensor carries its "
            "own ADC. Calibration is planned, not hoped: one-point offset, "
            "two-point gain-and-offset, or full curve against a reference, "
            "with recalibration intervals for drifting technologies. The "
            "demo computes a thermistor divider's output at two "
            "temperatures using the beta model, showing the nonlinearity "
            "that calibration must absorb."
        ),
        "key_points": [
            "Specify the measurement first: range, accuracy (truth), resolution (smallness), bandwidth, environment - then choose the sensor.",
            "Budget error stage by stage (sensor, conditioning, conversion) with root-sum-square; redesign the chain if the budget does not fit.",
            "Interface follows distance and noise: analog for short/quiet, 4-20 mA loops for long industrial runs, digital buses for smart sensors.",
            "Temperature drift and response time are the classic traps: compensate the drift, and match the time constant to the loop.",
            "Calibration is planned: offset, gain-and-offset, or full-curve against a reference, with intervals for drifting sensors.",
        ],
        "requirements": [
            "A measurement requirement: measurand, range, accuracy, resolution, bandwidth, and environment in writing.",
            "A transfer function with linearity, hysteresis, and drift specifications from the datasheet.",
            "An end-to-end error budget across sensor, conditioning, and conversion that fits the accuracy requirement.",
            "An interface choice justified by distance, noise, and system architecture.",
            "A calibration plan: method, reference standard, and recalibration interval.",
        ],
        "standards": [
            "Sensor test methods follow manufacturer data aligned with IEC 60747 and MIL-STD-202 where claimed.",
            "Industrial transmitter interfaces follow the 4-20 mA practice of IEC 60381.",
            "Calibration traceability follows ISO/IEC 17025 through accredited laboratories.",
        ],
        "citations": [CIT_MIL202, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the sensor is the scout - the eyes the "
            "armory sends into the world. The Signature Parts Method writes "
            "the scout's orders precisely (range, truth, speed), budgets its "
            "errors honestly, and calibrates its reports, because decisions "
            "made on lying scouts are defeats."
        ),
    },
    {
        "key": "optoelectronics",
        "name": "Optoelectronics: LEDs, Displays, and Photodetectors",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Optoelectronics is light made into parts: emitters that turn "
            "electricity into photons, detectors that turn photons back "
            "into electricity, and the couplers and displays built from "
            "them. LEDs are current-driven devices with a forward voltage "
            "set by color physics - about 2 volts for red, 3-plus for blue "
            "and white - and brightness proportional to current; they need "
            "series current limiting or constant-current drive, never a raw "
            "voltage rail. High-power LEDs add thermal management as the "
            "primary design task: light output falls and lifetime collapses "
            "as junction temperature rises. Displays range from seven-"
            "segment indicators through character LCDs to TFT and OLED "
            "panels, chosen by readability, power, and interface. "
            "Photodetectors - photodiodes, phototransistors, photoresistors - "
            "receive: specified by responsivity, spectral response, dark "
            "current, and speed. Optocouplers pair an LED with a detector "
            "in one package to cross isolation barriers: control signals "
            "pass, fault voltages do not - the safety component in power "
            "supplies and industrial I/O. The traps are driving LEDs from "
            "voltage (thermal runaway), ignoring viewing angle and binning "
            "(brightness and color matching), and forgetting that detector "
            "dark current doubles roughly every 10 degrees."
        ),
        "how_it_works": (
            "LED circuit design works from current, not voltage. The series "
            "resistor is computed as supply voltage minus LED forward "
            "voltage, divided by the desired current - a 5-volt rail driving "
            "a 2-volt red LED at 20 mA wants 150 ohms - and the resistor's "
            "dissipation (current squared times resistance) is checked. For "
            "precision or varying supplies, constant-current drivers replace "
            "the resistor: they hold current steady as voltage and "
            "temperature move, which is why every serious lighting product "
            "uses them. Brightness matching across multiple LEDs requires "
            "binning (same brightness and color bin from the manufacturer) "
            "or individual trimming, because LED forward voltage and "
            "efficacy vary unit to unit. High-power LED design is thermal "
            "design: the thermal resistance from junction to ambient times "
            "the dissipated power sets the junction temperature, and the "
            "lumen-maintenance curves say how fast light fades at that "
            "temperature. Optocoupler selection checks current transfer "
            "ratio at the operating LED current and temperature (CTR "
            "degrades with age and heat - design at end-of-life CTR), "
            "isolation voltage for the barrier, and speed for the signal. "
            "The demo sizes an LED series resistor and verifies its power "
            "rating."
        ),
        "key_points": [
            "LEDs are current devices: series resistor is (Vs-Vf)/I, or constant-current drive for serious lighting - never a raw voltage rail.",
            "Forward voltage follows color physics (~2 V red, ~3.2 V white/blue); brightness follows current.",
            "High-power LED design is thermal design: junction temperature sets light output and lifetime.",
            "Brightness/color matching needs manufacturer binning or trimming - LEDs vary unit to unit.",
            "Optocouplers cross isolation barriers: design at end-of-life CTR, verify isolation voltage and speed.",
        ],
        "requirements": [
            "An LED drive method: computed series resistance with dissipation check, or constant-current drive specified.",
            "A color/brightness binning plan wherever multiple LEDs must match visually.",
            "A thermal design for power LEDs: junction temperature computed through the real thermal path.",
            "Photodetector specs covering responsivity, spectral match to the emitter, dark current, and speed.",
            "Optocoupler CTR verified at operating current, temperature, and end-of-life, with isolation voltage for the barrier.",
        ],
        "standards": [
            "LED performance and lifetime follow IES LM-80 test methods with TM-21 projections where claimed.",
            "Optocoupler isolation follows IEC 60664-1 insulation coordination and UL 1577 recognition.",
            "Photometric quantities follow CIE definitions; display readability follows manufacturer application data.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IEC60664],
        "sig_lens": (
            "The Signature read: optoelectronics are the signal fires - "
            "light carrying orders across the dark between circuits. The "
            "Signature Parts Method lights every fire with measured fuel "
            "(current, not hope), bins its flames to match, and guards the "
            "isolation wall, because a signal fire that gutters is a "
            "message that never arrives."
        ),
    },
    {
        "key": "fasteners",
        "name": "Fasteners and Thread Standards",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Fasteners are the most numerous mechanical parts in existence: "
            "bolts, screws, nuts, washers, pins, rivets, inserts - the "
            "clamping technology that holds the built world together. A "
            "fastener is specified by thread designation (M10 x 1.5 metric "
            "coarse, or 3/8-16 UNC inch), length, head style, drive type, "
            "property class or grade (8.8, 10.9 metric; Grade 5, Grade 8 "
            "SAE), material, and finish (zinc, hot-dip galvanized, "
            "stainless, black oxide). Property class is the strength "
            "covenant: 8.8 means 800 MPa tensile strength with 80 percent "
            "yield ratio; 10.9 is stronger and less forgiving. The joint "
            "works by preload - the bolt stretched to 70-odd percent of its "
            "proof load so the clamped parts never separate under working "
            "loads. Thread standards are compatibility law: metric coarse "
            "and fine (ISO), unified coarse and fine (UNC/UNF, ASME), and "
            "never the twain shall meet - an M10 nut does not thread onto a "
            "3/8 bolt no matter how persuasive the wrench. Washers spread "
            "load and protect surfaces; prevailing-torque nuts and thread-"
            "locking compounds resist vibration loosening. The traps are "
            "mixing thread systems, reusing torque-to-yield bolts, and "
            "galling stainless threads without lubricant."
        ),
        "how_it_works": (
            "Fastener selection works from the joint's load case. The "
            "separating force is computed - tension trying to pull the "
            "joint apart, shear trying to slide it, plus vibration and "
            "fatigue factors. The bolt size and grade are chosen so the "
            "proof load (proof stress times tensile stress area) exceeds "
            "the required preload with margin: an M10 x 1.5 property class "
            "8.8 bolt has 58.0 square millimeters of stress area and 580 "
            "MPa proof stress, giving about 33.6 kN of proof load. Preload "
            "is set to roughly 75 percent of proof for reusable joints, "
            "applied by torque - with the torque-tension scatter (plus or "
            "minus 25 percent with ordinary lubrication) acknowledged in "
            "critical joints by using angle control or direct tension "
            "indication. Thread engagement is checked: steel needs about "
            "one diameter of engagement, aluminum and cast iron need more. "
            "The finish is chosen for the environment: zinc for indoor, "
            "hot-dip or stainless for outdoor and corrosive service - with "
            "the galvanic series consulted wherever dissimilar metals meet. "
            "The demo computes proof load and working preload for an M10 "
            "8.8 joint."
        ),
        "key_points": [
            "Property class is the strength covenant: 8.8 = 800 MPa tensile, 80 percent yield ratio; read it off the head mark.",
            "Joints work by preload (~75 percent of proof load): the stretched bolt clamps harder than any working load separates.",
            "Thread systems never mix: metric (ISO) and unified inch (UNC/UNF) are incompatible by law of geometry.",
            "Torque has plus/minus 25 percent scatter: critical joints use angle control or tension indication, not torque alone.",
            "Finish follows environment (zinc indoor, stainless/galvanized outdoor) with the galvanic series consulted for mixed metals.",
        ],
        "requirements": [
            "A joint load case: separating force, shear, vibration, and fatigue factors in writing.",
            "A bolt size and property class whose proof load covers the required preload with margin.",
            "A tightening specification: torque value with lubricant stated, or angle/tension method for critical joints.",
            "A thread-engagement check: one diameter minimum in steel, more in soft materials.",
            "A material and finish selection matched to corrosion exposure and galvanic compatibility.",
        ],
        "standards": [
            "Metric thread form follows ISO 68-1; fastener grades and head marking follow ISO 898-1.",
            "Unified inch threads follow ASME B1.1; SAE grades follow SAE J429.",
            "Torque-tension practice follows Machinery's Handbook and VDI 2230 for critical joints.",
        ],
        "citations": [CIT_ISO68, CIT_ISO898, CIT_ASMEB11, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: the fastener is the oath made steel - "
            "preload the tension of the promise. The Signature Parts Method "
            "torques every bolt as a vow spoken once and kept for years: "
            "proof load computed, lubricant named, engagement verified, "
            "because a joint that loosens has broken its word."
        ),
    },
    {
        "key": "bearings",
        "name": "Bearings and Bushings",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Bearings are friction's defeat: parts that let shafts spin, "
            "slides glide, and loads roll instead of grind. Rolling-element "
            "bearings - ball, roller, needle - run hardened elements in "
            "ground raceways: deep-groove ball bearings take combined radial "
            "and moderate thrust loads and are the default choice; angular-"
            "contact bearings take heavy thrust in one direction; tapered "
            "rollers take heavy combined loads; needle rollers pack maximum "
            "capacity into minimum radial space. Plain bearings (bushings) "
            "are simpler: a low-friction sleeve - bronze, PTFE-lined, or "
            "oil-impregnated sintered bronze - where the shaft slides "
            "directly; cheaper, tolerant of dirt, and fine at low speed. "
            "Every bearing is specified by bore, outside diameter, and "
            "width; the dynamic load rating C (the load for one million "
            "revolutions of L10 life); the static rating C0; the speed "
            "limit; the seal/shield choice (open, shielded ZZ, sealed 2RS); "
            "and the clearance class. The L10 life equation - life in "
            "millions of revolutions equals (C/P) cubed for ball bearings - "
            "is the catalog's central bearing calculation. The traps are "
            "undersized bearings in shock loads, wrong fits (a loose shaft "
            "fit frets, a tight housing fit cracks the ring), and "
            "contamination - the number-one bearing killer, which is why "
            "seals are a life decision, not an accessory."
        ),
        "how_it_works": (
            "Bearing selection works from the load-life equation. The "
            "application's radial and thrust loads are combined into the "
            "equivalent dynamic load P using the bearing's X/Y factors; "
            "shock and vibration multiply it by an application factor. The "
            "required L10 life is set - 90 percent of a bearing population "
            "survives past L10 - in millions of revolutions from the "
            "operating hours and speed. The required dynamic capacity is "
            "then C_needed equals P times (L10)^(1/3) for ball bearings "
            "(1/3.33 exponent for rollers), and the catalog is searched for "
            "the smallest bearing whose C exceeds it - smallest, because "
            "oversized bearings cost money and run hotter. Fits are chosen "
            "by the fit tables: rotating inner ring gets an interference "
            "fit (k5/m5 shaft), stationary outer ring a transition fit; "
            "temperature and speed adjust the choice. Lubrication is "
            "specified: grease for simplicity (relubrication interval from "
            "the tables), oil for high speed and heat removal. Seals are "
            "chosen by contamination: open for clean instrument service, "
            "ZZ shields for dusty shops, 2RS seals for wet or dirty duty. "
            "The demo computes L10 life in revolutions and hours for a "
            "loaded deep-groove bearing."
        ),
        "key_points": [
            "L10 life = (C/P)^3 million revolutions (ball): size the bearing from required life, then pick the smallest C that covers it.",
            "Equivalent load P combines radial and thrust via X/Y factors, multiplied by the application's shock factor.",
            "Fits are specified, not guessed: interference on the rotating ring, transition on the stationary ring, per the fit tables.",
            "Contamination is the number-one killer: seal choice (open/ZZ/2RS) is a life decision matched to the environment.",
            "Grease for simplicity with relubrication intervals; oil for high speed and heat removal.",
        ],
        "requirements": [
            "A load case: radial and thrust loads with shock/vibration application factors.",
            "An L10 life target in revolutions from operating hours and speed, with the 90-percent-survival meaning understood.",
            "A dynamic capacity C exceeding P*(L10)^(1/p) with the correct exponent for ball vs roller.",
            "Shaft and housing fits selected from the tables for the rotation condition, temperature, and load.",
            "A lubrication and sealing specification matched to speed, temperature, and contamination.",
        ],
        "standards": [
            "Dynamic load ratings and L10 life follow ISO 281:2007.",
            "Boundary dimensions follow ISO 15; fits follow the ISO system per Machinery's Handbook.",
            "Bearing steel and heat treatment follow manufacturer practice traceable to ISO 683-17.",
        ],
        "citations": [CIT_ISO281, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: the bearing is the vow of years - a promise "
            "that the shaft will spin a hundred million times without "
            "complaint. The Signature Parts Method sizes that vow by the "
            "equation, fits it by the table, seals it against the world's "
            "dirt, and feeds it on schedule, because longevity is a covenant "
            "kept daily."
        ),
    },
    {
        "key": "gears",
        "name": "Gears, Belts, and Power Transmission",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Gears, belts, and chains are how rotation travels and "
            "transforms: trading speed for torque, changing direction, and "
            "synchronizing shafts. Spur gears are the straight-toothed "
            "default for parallel shafts; helical gears run quieter and "
            "smoother at the cost of thrust loads; bevel gears turn corners "
            "between intersecting shafts; worm gears give huge reductions "
            "in one stage with sliding contact (and lower efficiency). The "
            "module - millimeters of pitch diameter per tooth - is the "
            "compatibility law: meshing gears must share module and "
            "pressure angle, full stop. Tooth count sets ratio: a 20-tooth "
            "pinion driving a 60-tooth gear gives 3:1 reduction, tripling "
            "torque (minus efficiency). Belts trade precision for quiet and "
            "forgiveness: V-belts slip slightly and absorb shock, timing "
            "belts (toothed) synchronize without slip. Chains handle heavy "
            "loads over distance with positive drive. Selection parameters "
            "are transmitted power, input speed, ratio, center distance, "
            "backlash needs, noise limits, lubrication, and life. The traps "
            "are mismatched modules, undersized teeth in shock service, and "
            "forgetting that worm gears need bronze wheels and generous "
            "lubrication to survive their sliding."
        ),
        "how_it_works": (
            "Gear selection works from geometry outward. The ratio is set "
            "by the application's speed-torque trade: tooth counts are "
            "chosen (z1 pinion, z2 gear, ratio z2/z1), keeping the pinion "
            "above the minimum teeth for the pressure angle to avoid "
            "undercut (17 teeth for 20-degree full-depth). Pitch diameters "
            "are module times teeth: d equals m times z, so a module-2, "
            "20-tooth pinion is 40 mm; the mating 60-tooth gear is 120 mm; "
            "and the center distance is fixed at half the sum, 80 mm - the "
            "housing is machined to that number, not adjusted later. Tooth "
            "strength is checked by the AGMA bending and contact stress "
            "equations against the transmitted power with service factors "
            "for shock. Backlash is specified where positioning matters "
            "(too tight binds with heat, too loose rattles). Belts are "
            "sized by power rating tables with service factors, center "
            "distance setting the belt length; timing belts add tooth "
            "profile and pitch compatibility. Lubrication is specified: "
            "grease or oil bath for enclosed gears, dry or lightly oiled "
            "for open belts and chains. The demo computes pitch diameters, "
            "center distance, and output speed for a spur pair."
        ),
        "key_points": [
            "Module is compatibility law: meshing gears must share module and pressure angle - mismatches do not assemble.",
            "Ratio is tooth-count ratio (z2/z1): speed divides, torque multiplies (minus efficiency).",
            "Center distance is fixed by geometry ((d1+d2)/2): the housing is machined to it, not adjusted later.",
            "Tooth strength follows AGMA bending/contact equations with service factors for shock loads.",
            "Belts forgive (V-belts absorb shock, timing belts synchronize); chains haul heavy loads with positive drive.",
        ],
        "requirements": [
            "A power, speed, and ratio requirement with shock and duty service factors.",
            "A module and tooth-count selection with the pinion above undercut minimum and pitch diameters computed.",
            "An AGMA strength check: bending and contact stress under allowable with the service factor applied.",
            "A center distance and backlash specification that the housing and assembly can actually hold.",
            "A lubrication, sealing, and noise specification matched to the enclosure and environment.",
        ],
        "standards": [
            "Gear rating follows ANSI/AGMA 2001-D04 for spur and helical teeth.",
            "Gear geometry follows ISO 53 / DIN 867 basic rack profiles; inspection follows AGMA 2015.",
            "Belt drive selection follows manufacturer power-rating tables per ISO 5292 (V-belts) and ISO 5296 (timing).",
        ],
        "citations": [CIT_AGMA2001, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: gears are the translators - speed rendered "
            "into torque, torque into speed, by teeth that keep their sworn "
            "spacing. The Signature Parts Method cuts no tooth short of the "
            "AGMA reckoning and meshes no pair of mismatched module, "
            "because a translation must be faithful or it is a lie."
        ),
    },
    {
        "key": "relays",
        "name": "Relays, Contactors, and Switches",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Relays, contactors, and switches are the muscle between control "
            "signals and power: a small coil or finger moves contacts that "
            "carry the load. Manual switches (toggle, rocker, pushbutton) "
            "are specified by pole/throw configuration (SPST, SPDT, DPDT), "
            "current and voltage rating, and mechanical life in cycles. "
            "Relays add the coil: a few dozen milliamps at 5, 12, or 24 "
            "volts pulls in contacts rated for amps - the isolation between "
            "coil and contacts is the safety feature. Contactors are relays "
            "grown up for motor and industrial loads, with arc chutes and "
            "auxiliary contacts. Solid-state relays switch silently with no "
            "moving parts but drop voltage and make heat. The selection "
            "parameters are coil voltage and power, contact rating (AC "
            "versus DC - DC is far harsher because there is no zero-crossing "
            "to quench the arc, so derate DC to a fraction of the AC "
            "rating), inrush versus steady current (a cold lamp filament "
            "draws ten times running current), electrical life at the actual "
            "load, and the protection diode across DC coils (without it, "
            "the collapsing field spikes hundreds of volts into the "
            "driver). The traps are switching DC at AC ratings, forgetting "
            "coil suppression, and rating by steady current where inrush "
            "rules."
        ),
        "how_it_works": (
            "Relay selection works from the load's true nature. The steady "
            "current is measured or computed, then the inrush is estimated: "
            "resistive loads are honest, lamp and heater loads surge, motor "
            "loads draw locked-rotor current, capacitive loads slam the "
            "contacts with charging current. The contact rating is chosen "
            "against the worse of the two: AC ratings assume the arc "
            "quenches at zero-crossing, so a 10-amp AC contact is typically "
            "a 3-amp DC contact at the same voltage - the derating is "
            "non-negotiable. Electrical life curves (operations versus "
            "current) are read at the actual load current, because a relay "
            "rated 100,000 operations at 5 amps may manage 10,000 at 10 "
            "amps. The coil is matched to the control voltage with margin "
            "for brownout (must-operate voltage), and coil power is budgeted "
            "in the supply. Every DC coil gets its flyback diode (or "
            "suppressor) across it, cathode to positive, placed at the "
            "relay - the collapsing magnetic field's spike is what kills "
            "transistor drivers. Contactors add overload relays and are "
            "sized by utilization category (AC-3 for motors). The demo "
            "computes coil power and applies the AC-to-DC contact derating."
        ),
        "key_points": [
            "Contacts are rated AC and DC separately: DC has no zero-crossing to quench arcs - derate DC to a fraction of the AC rating.",
            "Size to the worse of steady current and inrush: lamps, motors, and capacitors all surge past their running current.",
            "Electrical life falls fast with current: read the operations-vs-current curve at the actual load, not the headline.",
            "Every DC coil gets a flyback diode at the relay: the collapsing field spikes hundreds of volts without one.",
            "Coil voltage must hold through brownout: verify must-operate voltage against the worst supply dip.",
        ],
        "requirements": [
            "A load characterization: steady current, inrush profile, AC or DC, voltage, and duty.",
            "A contact rating covering the inrush with the AC/DC derating applied and life verified on the curve.",
            "A coil specification: voltage, power, must-operate/must-release voltages against supply tolerance.",
            "Coil suppression (flyback diode or suppressor) on every DC coil, placed at the relay.",
            "A mechanical-life and electrical-life budget matched to the product's service expectations.",
        ],
        "standards": [
            "Relay testing follows IEC 61810 electromechanical elementary relays; contactors follow IEC 60947-4-1.",
            "Utilization categories (AC-3, DC-1, etc.) follow IEC 60947 for the load type.",
            "Safety isolation between coil and contacts follows IEC 60664-1 for the working voltage.",
        ],
        "citations": [CIT_IEC60664, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the relay is the champion - a small oath "
            "(the coil) commanding a great one (the contacts). The Signature "
            "Parts Method arms its champions honestly: inrush reckoned, DC "
            "derated, coils suppressed, because a champion sent against a "
            "surge unprepared does not fall nobly - he welds shut."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "derating",
        "name": "Derating and Design Margins",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Derating is the discipline of never asking a part for its full "
            "rated strength: operating it at a fraction of its limits so it "
            "ages slowly instead of living at its edge. A capacitor rated 50 "
            "volts run at 25 volts, a resistor rated a quarter watt run at "
            "a tenth, a transistor rated 150 degrees junction run at 110 - "
            "these margins are what separate a product that survives its "
            "warranty from one that merely survives its test bench. The "
            "physics is unforgiving: capacitor lifetime doubles for every "
            "10-degree drop and every derated volt; semiconductor failure "
            "rates climb exponentially with junction temperature; "
            "electromigration in ICs accelerates with current density and "
            "heat. Industry practice converges on derating factors: 50 "
            "percent voltage on capacitors (more for tantalum), 60 percent "
            "power on resistors, 70-80 percent of maximum junction "
            "temperature on semiconductors, applied at worst-case ambient, "
            "worst-case load, and end-of-life conditions simultaneously. "
            "Derating is documented per part family in the project's "
            "derating standard, and every design review checks the "
            "spreadsheet: each stressed part, its rating, its worst-case "
            "stress, its derating ratio. The trap is derating the headline "
            "while ignoring the footnote - a 50-volt capacitor derated to "
            "25 volts still fails if ripple current cooks it."
        ),
        "how_it_works": (
            "Derating works as a per-family rule applied at the worst-case "
            "corner. For each stressed part, the worst-case stress is "
            "computed: maximum rail voltage including tolerance and "
            "transients for capacitors, RMS and peak current for inductors "
            "and contacts, dissipation at maximum ambient for resistors and "
            "semiconductors, junction temperature through the real thermal "
            "path. The derating ratio is stress divided by rating, and it "
            "must sit under the family limit: 0.50 voltage for general "
            "capacitors, 0.60 power for film resistors, junction temperature "
            "under about 110-125 C for silicon. Where the ratio fails, the "
            "design changes - a higher-rated part, a bigger package, a "
            "heatsink, or a topology change - not the rule. The analysis is "
            "tabulated: one row per part, columns for rating, worst-case "
            "stress, ratio, and verdict, reviewed and signed. Temperature "
            "derating gets special care because every rating assumes a "
            "reference ambient: the resistor rated at 70 C ambient must be "
            "re-rated along its derating curve for the actual enclosure "
            "temperature. The demo applies the capacitor voltage-derating "
            "rule to select a rating for a 24-volt rail and checks a "
            "resistor's power derating."
        ),
        "key_points": [
            "Derating = operating at a fraction of rating: 50 percent voltage on capacitors, 60 percent power on resistors, junctions well under maximum.",
            "Apply at the worst-case corner simultaneously: max ambient, max load, end-of-life, all at once - not one at a time.",
            "Lifetime physics rewards margins: capacitor life doubles per 10-degree drop; semiconductor failures climb exponentially with heat.",
            "Derate against the real rating at the real temperature: re-rate along the derating curve for the actual enclosure.",
            "Tabulate one row per stressed part (rating, stress, ratio, verdict) and review it like the contract it is.",
        ],
        "requirements": [
            "A project derating standard naming the allowed stress fraction for every part family.",
            "Worst-case stress computations for every stressed part at the simultaneous worst corner.",
            "Derating ratios verified under the family limits, with design changes (not rule changes) where ratios fail.",
            "Temperature re-rating along manufacturer derating curves for the actual enclosure ambient.",
            "A signed derating table reviewed at each design gate, updated for every part change.",
        ],
        "standards": [
            "Derating practice follows manufacturer guidelines and the project's derating standard (commonly per ECSS-Q-ST-30-11 or NAVSO P-3641 heritage).",
            "Capacitor voltage and temperature derating follows IEC 60384 endurance and manufacturer curves.",
            "Semiconductor thermal derating follows JEDEC JESD51 thermal measurement standards.",
        ],
        "citations": [CIT_IEC60384, CIT_JEDEC47, CIT_MIL217],
        "sig_lens": (
            "The Signature read: derating is the honor margin - the strength "
            "a warrior holds in reserve. The Signature Parts Method never "
            "spends the last of a part's oath: it keeps half the voltage, "
            "a third of the heat, in reserve, because the battle is always "
            "hotter than the parade ground."
        ),
    },
    {
        "key": "tolerance_stackup",
        "name": "Tolerance Stack-Up Analysis",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Tolerance stack-up is the reckoning every assembly faces: each "
            "part is made within its tolerance band, and the assembly must "
            "work when every part sits at its worst allowable extreme "
            "simultaneously. A shaft at its maximum, a bore at its minimum, "
            "a bracket at its longest - the stack-up analysis proves the "
            "fit still works, or the design changes. Two methods divide the "
            "practice. Worst-case analysis adds every tolerance in the "
            "chain: if three dimensions are each plus-or-minus 0.1, the "
            "stack is plus-or-minus 0.3 - guaranteed, conservative, and "
            "sometimes impossibly tight. Statistical (RSS) analysis takes "
            "the root-sum-square: sqrt(0.1^2 + 0.1^2 + 0.1^2), about 0.173 - "
            "valid when variations are independent and centered, predicting "
            "the spread the factory will actually produce. The catalog's "
            "rule: worst-case where safety or interchangeability demands "
            "it, RSS where the process is controlled and the economics "
            "matter - and the choice written down, because the two answers "
            "differ and the factory builds to whichever was specified. The "
            "analysis covers gaps, interferences, alignments, and "
            "electrical stacks (resistor dividers, timing chains) alike."
        ),
        "how_it_works": (
            "Stack-up analysis works by chaining dimensions. The analyst "
            "draws the dimension loop: starting at one feature, walking "
            "through every part and interface to the feature being checked, "
            "recording each dimension with its plus/minus tolerance and its "
            "direction sign (dimensions that grow the gap are positive, "
            "those that shrink it negative). Worst-case sums the absolute "
            "tolerances: the gap's variation is the straight sum, and the "
            "design passes if the minimum gap stays positive (for "
            "clearance) or the maximum interference stays under the press "
            "limit. RSS takes the square root of the sum of squares: valid "
            "when each contributor is an independent, roughly normal "
            "process - which machined dimensions from capable processes "
            "are. Contributors are ranked by their squared share so the "
            "designer knows which tolerance to tighten: halving the biggest "
            "contributor beats shaving all of them. Electrical stacks use "
            "the same math: a divider's ratio error is the RSS of the "
            "resistor tolerances for statistical yield, worst-case for "
            "guaranteed limits. The demo computes worst-case and RSS stacks "
            "for a three-dimension chain and ranks the contributors."
        ),
        "key_points": [
            "Worst-case sums tolerances (guaranteed, conservative); RSS takes root-sum-square (realistic for controlled processes) - choose and document.",
            "Draw the dimension loop with direction signs: dimensions growing the gap are positive, shrinking it negative.",
            "Clearance passes if the minimum gap stays positive; interference passes if maximum press stays under the limit.",
            "Rank contributors by squared share: tighten the biggest contributor first - it dominates the stack.",
            "Electrical stacks obey the same math: divider ratio error from resistor tolerances, worst-case for guarantees, RSS for yield.",
        ],
        "requirements": [
            "A dimension loop drawing naming every contributor with its tolerance and direction sign.",
            "Both worst-case and RSS computations with the chosen method justified and documented.",
            "A pass/fail verdict on the critical gap or interference at the stack extremes.",
            "A contributor ranking identifying which tolerance drives the stack, with a tightening plan if it fails.",
            "The same analysis for electrical stacks (dividers, timing) wherever tolerance affects function.",
        ],
        "standards": [
            "Dimensioning and tolerancing follow ASME Y14.5; general tolerances follow ISO 2768.",
            "Statistical tolerancing follows the process-capability practice of ISO 22514 where RSS is claimed.",
            "Fit calculations follow the ISO system of limits and fits per Machinery's Handbook.",
        ],
        "citations": [CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: the stack-up is the muster - every part "
            "present at its worst and the formation still holding. The "
            "Signature Parts Method musters the whole chain at dawn: "
            "worst-case where honor demands certainty, RSS where the "
            "process has earned trust, and the verdict written before the "
            "first chip is cut."
        ),
    },
    {
        "key": "thermal",
        "name": "Thermal Management and Heat Sinks",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Thermal management is the art of giving heat somewhere to go: "
            "every watt a part dissipates must travel from its junction to "
            "the ambient air without cooking anything along the way. The "
            "catalog treats heat as a current and temperature as a voltage: "
            "thermal resistance in degrees per watt is the opposition, and "
            "junction temperature equals ambient plus power times the total "
            "thermal resistance of the path. The path is a chain - junction "
            "to case, case to heatsink (through thermal interface material), "
            "heatsink to air - and the chain's total resistance decides the "
            "temperature. Heat sinks are finned aluminum that multiply "
            "surface area: specified by thermal resistance at a given "
            "airflow, because still air and forced air are different "
            "universes. Interface materials (grease, pads, phase-change) "
            "fill the microscopic air gaps that would otherwise insulate. "
            "The design sequence is fixed: compute the dissipation, set the "
            "maximum junction temperature with derating, measure the worst "
            "ambient, subtract to get the allowed rise, divide by power to "
            "get the allowed thermal resistance, then choose the heatsink "
            "and interface that beat it. The traps are forgetting the "
            "interface resistance, rating heatsinks at the wrong airflow, "
            "and stacking hot parts so each breathes the other's exhaust."
        ),
        "how_it_works": (
            "Thermal design works through the resistance chain. The allowed "
            "temperature rise is the derated maximum junction temperature "
            "minus the worst-case ambient: a 150-degree silicon limit "
            "derated to 125, in a 50-degree enclosure, allows 75 degrees of "
            "rise. Dividing by the dissipation gives the thermal budget: "
            "2.5 watts means the total path must be under 30 degrees per "
            "watt. The chain is then allocated: junction-to-case from the "
            "datasheet (say 3 C/W), interface material (0.5-2 C/W depending "
            "on type and pressure), leaving the remainder for the heatsink "
            "itself. Heatsink selection reads the thermal-resistance-versus-"
            "airflow curves: a sink rated 12 C/W in still air may be 4 C/W "
            "at 200 linear feet per minute - the fan decision changes the "
            "answer. Orientation matters for natural convection (fins "
            "vertical), and the enclosure's own ventilation sets the local "
            "ambient the sink actually sees. Verification is by measurement: "
            "thermocouples on the case under worst-case load, because "
            "models are optimistic and heat is honest. The demo computes "
            "junction temperature through a three-link chain and the margin "
            "to the derated limit."
        ),
        "key_points": [
            "Heat is current, temperature is voltage: Tj = Tambient + P x Rth(total) through the junction-case-sink-air chain.",
            "Budget the rise: derated max junction minus worst ambient, divided by power, gives the allowed total thermal resistance.",
            "Heatsinks are rated at an airflow: still-air and forced-air numbers differ by multiples - match the rating to the reality.",
            "Interface material is a real resistor in the chain: grease, pads, and phase-change each have their C/W - never dry-mount power parts.",
            "Verify by measurement: thermocouples under worst-case load, because models are optimistic and heat is honest.",
        ],
        "requirements": [
            "A dissipation number for every hot part at worst-case load and ambient.",
            "A derated maximum junction temperature per the project's derating standard.",
            "A thermal-resistance budget allocated across junction-case, interface, and heatsink links.",
            "A heatsink selected from its resistance-vs-airflow curves at the actual airflow and orientation.",
            "A measurement verification: case temperatures under worst-case load confirming the model.",
        ],
        "standards": [
            "Semiconductor thermal measurement follows JEDEC JESD51 series standards.",
            "Thermal interface material performance follows ASTM D5470 test methods.",
            "Enclosure thermal practice follows manufacturer application guidance and IEC 60068-2 temperature testing.",
        ],
        "citations": [CIT_JEDEC47, CIT_IEC60068, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: heat is the exertion of the oath - every "
            "watt a part spends must be given honorable passage out. The "
            "Signature Parts Method builds the road before the march: "
            "resistance budgeted link by link, sinks chosen for the real "
            "wind, temperatures measured in the field, because a warrior "
            "overheated is a covenant broken by fire."
        ),
    },
    {
        "key": "emc",
        "name": "EMI and EMC Compatibility",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Electromagnetic compatibility is the discipline of parts that "
            "neither shout nor startle: the product must not emit "
            "interference that disturbs others (EMI), and must not be "
            "disturbed by the interference around it (EMS) - together, EMC. "
            "Every fast edge is a radio transmitter: a 1-nanosecond rise "
            "time rings with energy past 300 MHz, and the PCB traces, "
            "cables, and enclosures are the antennas. The catalog's EMC "
            "shelf holds the countermeasures as parts: ferrite beads and "
            "common-mode chokes that become resistors at RF, feedthrough and "
            "filter capacitors that shunt noise to ground, TVS and MOV "
            "devices that clamp surges, shielded connectors and gaskets "
            "that close the enclosure's seams, and common-mode chokes for "
            "cable-borne noise. Selection is frequency-first: identify the "
            "noise spectrum (switching frequency and its harmonics, clock "
            "edges), then choose countermeasures whose impedance peaks in "
            "that band - a ferrite bead rated at 100 MHz does little at 10 "
            "MHz. Layout is half the battle: short return paths, solid "
            "ground planes, filtered I/O at the enclosure wall. The traps "
            "are adding beads without checking their DC current rating "
            "(they saturate), and filtering the board while the cable "
            "radiates unfiltered past the enclosure."
        ),
        "how_it_works": (
            "EMC design works by containing noise at its source and blocking "
            "it at every exit. First the sources are tamed: switching "
            "edges are slowed to the minimum speed the timing allows (a "
            "series resistor at the driver is the cheapest filter ever "
            "made), decoupling capacitors sit at every power pin with low-"
            "inductance mounting, and clocks are spread-spectrum where the "
            "receiver tolerates it. Then the exits are filtered: every cable "
            "leaving the enclosure gets its treatment at the wall - "
            "common-mode chokes for data pairs, pi-filters for power, "
            "shield termination 360 degrees at the connector. Ferrite beads "
            "are selected by impedance-versus-frequency curves matched to "
            "the noise band, with DC bias and current derating checked "
            "(bead impedance collapses near saturation current). Filter "
            "capacitors are chosen by self-resonant frequency above the "
            "noise band. Susceptibility is designed in parallel: TVS diodes "
            "at every external interface, rated for the IEC 61000-4-5 surge "
            "and 61000-4-2 ESD threats, with clamping voltage under the "
            "protected part's limit. The demo computes an RC filter's "
            "cutoff and its attenuation at a harmonic frequency."
        ),
        "key_points": [
            "EMC is two-sided: limit emissions (EMI) and harden immunity (EMS) - a quiet product that resets in a storm still fails.",
            "Fast edges are transmitters: slow edges to the timing minimum, decouple every power pin, keep returns short.",
            "Filter at the enclosure wall: every cable gets chokes, pi-filters, or shield termination where it exits.",
            "Ferrite beads are selected by impedance-vs-frequency in the noise band, with current/saturation derating - not by headline ohms.",
            "TVS at every external interface, rated for the IEC surge/ESD threats with clamping under the victim's limit.",
        ],
        "requirements": [
            "A noise inventory: switching frequencies, edge rates, and clock harmonics identified as the threat spectrum.",
            "Source control: edge-rate limiting, decoupling, and grounding designed before filters are added.",
            "Exit filtering: every external cable and interface treated at the enclosure boundary.",
            "Countermeasure selection by frequency behavior (impedance curves, SRF) with current and temperature derating.",
            "Susceptibility protection: TVS/clamp devices at all external interfaces rated for the standard threats.",
        ],
        "standards": [
            "Emissions and immunity testing follow the IEC 61000-4 series (ESD, surge, EFT, conducted/radiated).",
            "Product emission limits follow CISPR 32 (multimedia) or the applicable product-family standard.",
            "Filter component safety (X/Y capacitors) follows IEC 60384-14.",
        ],
        "citations": [CIT_IEC61000, CIT_IEC60384],
        "sig_lens": (
            "The Signature read: EMC is discipline of voice - the armory "
            "neither shouts into others' camps nor startles at others' "
            "shouts. The Signature Parts Method quiets every edge, guards "
            "every gate, and filters every road out of the enclosure, "
            "because a covenant kept electrically is kept silently."
        ),
    },
    {
        "key": "reliability",
        "name": "Reliability, MTBF, and Failure Rates",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Reliability is the catalog's long view: not whether the part "
            "works today, but the probability it still works years from "
            "now. The language is failure rate (lambda): failures per hour, "
            "often quoted in FITs (failures per billion hours). MTBF - mean "
            "time between failures - is one over the failure rate: 100 FITs "
            "means an MTBF of 10 million hours. The bathtub curve frames "
            "the life: early failures (manufacturing defects, screened by "
            "burn-in), the long flat useful life (random failures, the "
            "exponential model), and wear-out (electrolytics drying, fans "
            "seizing, relay contacts eroding). Prediction handbooks like "
            "MIL-HDBK-217F estimate part failure rates from stress and "
            "temperature - useful for comparing design alternatives, "
            "dangerous as absolute truth. System reliability multiplies: "
            "three parts each 99.9 percent reliable in series give 99.7 "
            "percent - which is why redundancy (parallel reliability) is "
            "the tool for high-availability design. The traps are quoting "
            "MTBF as a lifetime (it is not - half the population fails "
            "before one MTBF in the exponential model), ignoring wear-out "
            "mechanisms the handbook does not model, and forgetting that "
            "the prediction assumes the derating the design may not have."
        ),
        "how_it_works": (
            "Reliability prediction works by summing part failure rates. "
            "Each part gets a lambda from the handbook model at its actual "
            "temperature and stress: a film capacitor at 40 C might be 2 "
            "FITs, a power MOSFET at high junction temperature hundreds. "
            "The assembly lambda is the sum (series model - any part fails, "
            "the function fails), and MTBF is one over the sum. Mission "
            "reliability for time t is exp(-lambda*t): the probability of "
            "zero failures in the mission. The prediction is then used "
            "comparatively: design A's 50,000-hour MTBF versus design B's "
            "120,000 hours tells you B is the better bet, even if neither "
            "number is gospel. Wear-out is handled separately from the "
            "handbook: electrolytic lifetime from the temperature rule, fan "
            "life from the bearing L10, relay life from the operations "
            "curve - each with a scheduled replacement or a redundancy "
            "plan. Redundancy math is multiplicative on unreliability: two "
            "parallel 99-percent units give 99.99 percent (1 minus 0.01 "
            "squared). The demo converts FITs to MTBF and computes series "
            "mission reliability for a three-part chain over one year."
        ),
        "key_points": [
            "Failure rate (FITs) inverts to MTBF: 100 FITs = 10 million hours - but MTBF is not a lifetime, it is the mean of an exponential.",
            "The bathtub curve: burn-in screens early failures, the flat middle is the prediction zone, wear-out needs its own plan.",
            "Handbook predictions (MIL-HDBK-217F) compare designs reliably and predict absolutes poorly - use them comparatively.",
            "Series reliability multiplies (three 99.9 percent parts = 99.7 percent); redundancy multiplies unreliability away.",
            "Wear-out mechanisms (electrolytics, fans, contacts) are scheduled or redunded, never hand-waved.",
        ],
        "requirements": [
            "A part-level failure-rate rollup at actual temperature and stress, with the handbook and version cited.",
            "An MTBF computed from the summed lambda and a mission reliability for the warranty period.",
            "A wear-out inventory: every mechanism with a life estimate and a replacement or redundancy plan.",
            "A derating verification, because handbook numbers assume stresses the design must actually hold.",
            "A comparative use of the prediction: design alternatives ranked, not absolute promises made.",
        ],
        "standards": [
            "Electronic reliability prediction follows MIL-HDBK-217F Notice 2 (with its known limitations documented).",
            "System reliability modeling follows IEC 61078 (reliability block diagrams) and IEC 61025 (fault trees).",
            "Accelerated life testing follows JEDEC JESD47 and IEC 60068-2 environmental methods.",
        ],
        "citations": [CIT_MIL217, CIT_JEDEC47, CIT_IEC60068],
        "sig_lens": (
            "The Signature read: reliability is the oath projected through "
            "time - the promise that the covenant holds not just today but "
            "in the tenth year. The Signature Parts Method counts the FITs, "
            "plans the wear-out, and redounds the critical, because a vow "
            "that cannot name its tenth year is a wish."
        ),
    },
    {
        "key": "counterfeit",
        "name": "Counterfeit Component Detection",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Counterfeit components are the catalog's enemy within: parts "
            "marked as something they are not - relabeled lower grades, "
            "pulled and resold used parts, empty packages, or outright "
            "fakes. They enter through brokers and gray-market buys, "
            "especially during shortages when the authorized channel is "
            "dry. The damage is real: a relabeled capacitor with half the "
            "voltage rating, a remarked IC that is a different die, a "
            "cleaned-and-reballed BGA with fractured joints waiting for "
            "thermal cycles. Detection is a layered discipline codified in "
            "SAE AS5553: visual inspection under magnification (marking "
            "quality, font, alignment, pin-1 marks, surface texture - "
            "resurfaced parts show sanding marks), dimensional and weight "
            "checks against the datasheet, X-ray for die and bond-wire "
            "consistency, decapsulation and die inspection for high-risk "
            "lots, XRF for lead finish and RoHS compliance, solderability "
            "testing, and full electrical test against the datasheet "
            "limits. The first line of defense is avoidance: buy from "
            "authorized distributors and the manufacturer, keep the chain "
            "of custody documented, and treat any broker buy as guilty "
            "until proven innocent with the full test battery."
        ),
        "how_it_works": (
            "Counterfeit detection works as an escalating test sequence "
            "matched to risk. Every incoming lot gets the paperwork check: "
            "certificates of conformance, date codes consistent with the "
            "part's production history, packaging and moisture-barrier "
            "integrity, and traceability back to the authorized chain. Then "
            "visual inspection under 10-40x magnification against a known-"
            "good sample: marking permanence (solvent rub test - remarked "
            "parts wipe), font and logo fidelity, surface homogeneity "
            "(blacktopping shows edges), lead finish and straightness. "
            "Dimensional and weight sampling follows: counterfeits often "
            "miss the datasheet by small but measurable amounts. "
            "High-risk lots escalate to X-ray (die size, bond wires, lead "
            "frame versus the known-good), acoustic microscopy for "
            "delamination, and decapsulation with die photography compared "
            "to the manufacturer's die. Electrical testing closes the loop: "
            "full datasheet parametric test, because a remarked lower grade "
            "fails the limits it never met. The demo runs the statistical "
            "gate: a sample's mean weight and marking-consistency score "
            "against the genuine population, flagging the lot when either "
            "drifts past the control limit."
        ),
        "key_points": [
            "Avoidance first: authorized distributors and documented chain of custody - broker buys are guilty until proven innocent.",
            "Visual inspection under magnification catches most fakes: marking quality, solvent-rub permanence, resurfacing texture, lead finish.",
            "Weight and dimensions are cheap, powerful screens: counterfeits measurably miss the datasheet.",
            "Escalate by risk: X-ray, acoustic microscopy, decapsulation with die comparison for high-risk lots.",
            "Close with electrical test: a remarked lower grade fails the datasheet limits it never met.",
        ],
        "requirements": [
            "A purchasing policy: authorized sources by default, documented chain of custody, risk assessment for any broker buy.",
            "An incoming-inspection plan scaled to risk: paperwork, visual, dimensional/weight for every lot; X-ray/decap where risk warrants.",
            "Known-good reference samples retained for visual, X-ray, and electrical comparison.",
            "A solvent-rub marking permanence test and a solderability check in the standard battery.",
            "A quarantine and reporting procedure: suspect lots segregated, the supplier notified, the incident recorded.",
        ],
        "standards": [
            "Counterfeit avoidance, detection, mitigation, and disposition follow SAE AS5553B.",
            "Test methods for inspection follow SAE AS6081 for distribution and IDEA-STD-1010 inspection criteria.",
            "Electrical testing follows the datasheet limits with MIL-STD-202 methods where claimed.",
        ],
        "citations": [CIT_AS5553, CIT_MIL202],
        "sig_lens": (
            "The Signature read: the counterfeit is the oath-breaker - a "
            "part wearing a covenant it never swore. The Signature Parts "
            "Method knows its true suppliers, inspects every stranger at "
            "the gate with glass and scale and solvent, and casts out the "
            "false-marked, because the armory admits no liars."
        ),
    },
    {
        "key": "obsolescence",
        "name": "Obsolescence Management and Last-Time Buys",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Obsolescence is the catalog's slow tide: manufacturers "
            "discontinue parts - the average electronic component lives "
            "a few years while industrial products must live for decades - "
            "and every discontinuation threatens the product it is designed "
            "into. Proactive obsolescence management starts at selection: "
            "prefer multi-sourced, standard, long-lived parts; check the "
            "product-change and end-of-life notification policies; avoid "
            "single-source custom silicon where a standard part serves. "
            "Monitoring is continuous: distributor lifecycle databases, "
            "manufacturer PCN/EOL alerts, and periodic BOM health scans "
            "flag parts going not-recommended or end-of-life. When the EOL "
            "notice arrives, the options are ranked: last-time buy (purchase "
            "the lifetime need now - quantity computed from the demand "
            "forecast plus spares plus buffer, stored under controlled "
            "conditions), approved alternate (qualify the drop-in second "
            "source), redesign (replace the function with a current part, "
            "the honest long-term answer), or aftermarket/emulation (for "
            "legacy systems where redesign is impossible). The traps are "
            "underbuying the last-time quantity (the forecast was "
            "optimistic), storing parts badly (moisture and solderability "
            "decay), and discovering the EOL notice in the inbox six months "
            "late."
        ),
        "how_it_works": (
            "Obsolescence management works as a lifecycle watch with a "
            "quantified response. Each BOM line carries a lifecycle status "
            "(active, mature, not-recommended, EOL) refreshed from "
            "distributor and manufacturer feeds; the BOM health score is "
            "the fraction of lines at risk, reviewed quarterly. When an "
            "EOL notice lands, the clock starts: the last-order date is "
            "fixed, and the last-time-buy quantity is computed as annual "
            "demand times remaining product years, plus spares demand, plus "
            "a buffer for forecast error and attrition - commonly 15-25 "
            "percent - rounded to the manufacturer's minimum and reel "
            "quantities. Storage is specified: moisture-sensitive parts in "
            "sealed dry-pack with humidity indicators, temperature-"
            "controlled, with solderability retest intervals. The alternate "
            "path runs in parallel: the candidate replacement is qualified "
            "by form-fit-function comparison plus delta testing of every "
            "differing parameter, because 'drop-in' is a claim to verify. "
            "Redesign is scoped as a project with its own selection "
            "discipline from this catalog's earlier records. The demo "
            "computes a last-time-buy quantity from a demand forecast with "
            "buffer and MOQ rounding."
        ),
        "key_points": [
            "Design against obsolescence at selection: multi-sourced, standard, long-lived parts; check EOL notification policies.",
            "Monitor continuously: lifecycle status per BOM line, refreshed from distributor/manufacturer feeds, reviewed quarterly.",
            "Last-time buy = annual demand x remaining years + spares + 15-25 percent buffer, rounded to MOQ/reel quantities.",
            "Store buys properly: dry-pack for moisture-sensitive parts, controlled temperature, solderability retest intervals.",
            "Qualify alternates by form-fit-function plus delta testing - 'drop-in' is a claim to verify, not a fact to assume.",
        ],
        "requirements": [
            "A lifecycle status on every BOM line, refreshed quarterly from distributor and manufacturer sources.",
            "A BOM health review cadence with an at-risk threshold that triggers action plans.",
            "A last-time-buy procedure: demand forecast, buffer policy, MOQ rounding, storage specification, ownership.",
            "An alternate-qualification procedure: form-fit-function comparison plus delta testing of differing parameters.",
            "A redesign trigger policy: when lifetime buys and alternates cannot cover the product's remaining life.",
        ],
        "standards": [
            "Obsolescence management follows IEC 62402:2019 (obsolescence management guidance).",
            "Moisture-sensitive part storage follows IPC/JEDEC J-STD-033 handling and dry-pack practice.",
            "Product change and discontinuation notices follow JEDEC JESD46 notification practice.",
        ],
        "citations": [CIT_JEDEC47],
        "sig_lens": (
            "The Signature read: obsolescence is the tide that outlasts "
            "every armory - parts retire while products must march on. The "
            "Signature Parts Method watches the tide tables, buys the last "
            "campaign's supply with a full buffer, stores it like treasure, "
            "and qualifies successors before the need is desperate, because "
            "a covenant should end by planning, never by surprise."
        ),
    },
    {
        "key": "sourcing_bom",
        "name": "Sourcing, the BOM, and the Supply Chain",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Sourcing is where the catalog meets money: turning the bill of "
            "materials into purchase orders at the right price, the right "
            "quantity, and the right time. The BOM (bill of materials) is "
            "the authoritative parts list: every line carries the part "
            "number, description, quantity per assembly, reference "
            "designators, approved manufacturer list, and lifecycle status. "
            "Cost rolls up from unit prices that depend brutally on "
            "quantity: a capacitor that costs 10 cents at 100 pieces costs "
            "a tenth of a cent at a million - price breaks, MOQs (minimum "
            "order quantities), and reel quantities shape the real cost. "
            "Lead time is the other currency: 8 weeks standard, 26 weeks in "
            "shortages, and the production schedule must cover it. Sourcing "
            "strategy balances authorized distributors (traceability, "
            "support, fair pricing), direct manufacturer buys (volume "
            "leverage), and brokers (last resort, with the counterfeit "
            "battery from this ladder's earlier record). The disciplines "
            "are costed BOMs updated with real quotes (not catalog "
            "list prices), lead-time tracking per line, alternate-source "
            "qualification before the shortage, and the economic order "
            "quantity trade between inventory carrying cost and price "
            "breaks. The trap is designing a BOM nobody can buy: perfect "
            "parts with 52-week lead times and single sources."
        ),
        "how_it_works": (
            "Sourcing works from the costed, lead-timed BOM. Each line's "
            "unit price is quoted at the planned build quantity with the "
            "price-break ladder recorded: the price at 1k, 10k, 100k pieces "
            "shows where the next break falls and whether the build "
            "quantity should move to meet it. MOQ and package multiples "
            "round every order up: a 4,000-piece need with a 5,000 MOQ on "
            "reels of 5,000 buys 5,000 - the excess is inventory, planned "
            "and costed. Extended cost per line is rounded quantity times "
            "unit price; the BOM total is the sum, and the target cost is "
            "the verdict the design must meet. Lead times are tracked per "
            "line with the longest pole identified: the build schedule "
            "starts from the longest lead item, not from wishful thinking. "
            "Alternates are qualified and dual-sourced for critical lines "
            "before shortages strike, because qualification takes weeks you "
            "will not have during an allocation. The demo rolls up a small "
            "BOM: MOQ rounding, extended costs, total cost, and the "
            "longest-lead line that paces the schedule."
        ),
        "key_points": [
            "The BOM is the authoritative parts list: part number, quantity, designators, approved manufacturers, lifecycle status - one source of truth.",
            "Unit price depends brutally on quantity: quote at the build volume, record the price-break ladder, consider moving quantity to the next break.",
            "MOQ and package multiples round orders up: the excess is planned inventory, costed and stored - not a surprise.",
            "The schedule starts from the longest lead-time line: identify the pacing part and order it first.",
            "Dual-source critical lines before shortages: qualification takes weeks you will not have during an allocation.",
        ],
        "requirements": [
            "A BOM with approved manufacturer lists and lifecycle status on every line, under revision control.",
            "Real quoted pricing at the build quantity with the price-break ladder recorded per line.",
            "MOQ and packaging rounding applied to every order quantity, with excess inventory planned.",
            "Lead times tracked per line with the pacing (longest-lead) part identified and ordered first.",
            "Qualified alternates for critical and single-source lines before they are needed.",
        ],
        "standards": [
            "BOM structure and revision control follow the configuration management practice of ISO 10007.",
            "Procurement quality follows ISO 9001:2015 purchasing controls and AS5553 for broker buys.",
            "Moisture and ESD handling through the chain follow J-STD-033 and ANSI/ESD S20.20.",
        ],
        "citations": [CIT_AS5553],
        "sig_lens": (
            "The Signature read: sourcing is the quartermaster's art - the "
            "armory provisioned before the campaign, at honest prices, on "
            "time. The Signature Parts Method costs every line truthfully, "
            "rounds every order deliberately, paces the schedule by the "
            "longest road, and never lets a single merchant hold the "
            "armory hostage."
        ),
    },
    {
        "key": "cross_reference",
        "name": "Cross-References and Substitution",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Cross-referencing is the catalog's answer to 'what can replace "
            "this part': the disciplined search for substitutes when the "
            "specified part is unavailable, too expensive, or obsolete. A "
            "true cross meets form, fit, and function: the package and "
            "pinout match (form), it assembles into the same footprint and "
            "mating interfaces (fit), and every critical parameter meets or "
            "beats the original under the actual operating conditions "
            "(function). The procedure is parametric: list the original's "
            "critical parameters with their required values, filter the "
            "catalog for candidates meeting all of them, then delta-test "
            "the differences - the parameters where the candidate is "
            "merely adequate rather than identical get bench verification. "
            "Manufacturer cross-reference tools are starting points, not "
            "verdicts: they match headline parameters and miss footnotes. "
            "The classic traps are the 'equivalent' with a worse "
            "temperature coefficient, the pin-compatible IC with different "
            "timing, the 'same' capacitor with half the ripple rating, and "
            "the mechanical substitute in a different material. Substitution "
            "without requalification is gambling; substitution with a "
            "written delta analysis is engineering. This record is the "
            "capstone of the catalog's compatibility theme: every part "
            "findable, every replacement provable."
        ),
        "how_it_works": (
            "Cross-referencing works as a scored parametric match. The "
            "original part's critical parameters are tabulated with the "
            "minimum acceptable value for each: capacitance and voltage "
            "rating, ESR limit, package, temperature range - whatever the "
            "design actually depends on, including the footnote parameters "
            "the original selection relied on. Candidates are filtered: any "
            "candidate failing any critical parameter is out, no matter "
            "how attractive the price. Survivors are scored on parameter "
            "margin - how far each critical value clears the requirement - "
            "with extra weight on the parameters the design stresses most. "
            "The top candidate then faces delta analysis: every parameter "
            "where it differs from the original is listed, each difference "
            "is judged (better, equivalent, or worse-but-acceptable with "
            "reason), and worse-but-acceptable differences get bench tests "
            "specified. Only after the delta analysis passes is the "
            "substitute approved and added to the BOM's approved "
            "manufacturer list - which is what makes the next shortage a "
            "purchasing event instead of an engineering crisis. The demo "
            "scores three candidate capacitors against a required parameter "
            "set and ranks them by weighted margin."
        ),
        "key_points": [
            "A true cross meets form (package/pinout), fit (footprint/interfaces), and function (every critical parameter at operating conditions).",
            "Tabulate the original's critical parameters including footnote dependencies - the selection's hidden assumptions are the cross's traps.",
            "Filter hard on criticals, then score survivors by parameter margin weighted toward the design's stressed parameters.",
            "Delta analysis judges every difference (better / equivalent / worse-but-acceptable) with bench tests for the last category.",
            "Approved substitutes join the BOM's manufacturer list: the next shortage becomes a purchasing event, not a crisis.",
        ],
        "requirements": [
            "A critical-parameter table for the original part with minimum acceptable values from the design's actual needs.",
            "A hard filter eliminating any candidate that fails any critical parameter.",
            "A weighted margin score ranking the survivors, with weights reflecting the design's stressed parameters.",
            "A written delta analysis of every differing parameter with bench-test evidence for worse-but-acceptable items.",
            "BOM update: the approved substitute added to the manufacturer list with the analysis filed.",
        ],
        "standards": [
            "Substitution control follows the configuration management practice of ISO 10007.",
            "Parametric verification follows the datasheet test conditions with MIL-STD-202 methods where claimed.",
            "Second-source qualification follows the project's component qualification procedure.",
        ],
        "citations": [CIT_MIL202],
        "sig_lens": (
            "The Signature read: the cross-reference is the succession - "
            "the proof that the covenant outlives any single swearer. The "
            "Signature Parts Method writes every part's requirements so "
            "completely that a worthy successor can be proven worthy, "
            "because an armory that dies with one supplier was never an "
            "armory."
        ),
    },
    {
        "key": "modules",
        "name": "Modules and Subassemblies: Build vs Buy",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Modules and subassemblies are the catalog's top shelf: "
            "pre-built groups of parts sold as one unit - power supply "
            "modules, motor driver boards, sensor assemblies, wireless "
            "modules, display assemblies, complete cable harnesses. They "
            "compress months of design, layout, compliance testing, and "
            "supply-chain work into a purchase order, and the build-vs-buy "
            "decision is among the highest-leverage calls in engineering. "
            "Buy wins when the module is a commodity (someone builds it "
            "better and cheaper at scale), when compliance is expensive (a "
            "pre-certified wireless module skips the six-figure radio "
            "certification), when time-to-market dominates, or when the "
            "function is outside the team's core competence. Build wins "
            "when the function is the product's differentiation, when "
            "volumes make the module's margin intolerable, when the form "
            "factor or environment is exotic, or when supply assurance "
            "demands owning the design. The catalog treats modules as "
            "parts with the same grammar: function, properties, ratings, "
            "package, compatibility - plus module-specific checks: "
            "certifications carried (FCC, CE, UL), firmware and driver "
            "support, the vendor's longevity, and the interface contract "
            "(pinout, protocol, timing) that your design depends on."
        ),
        "how_it_works": (
            "Build-vs-buy works as a total-cost comparison over the "
            "product's life. The buy side totals module unit price times "
            "lifetime volume, plus integration engineering, plus the risk "
            "premium of vendor dependence (second-source or redesign cost "
            "if the module goes EOL). The build side totals NRE "
            "(engineering hours, prototypes, compliance testing and "
            "certification - the number everyone underestimates), plus "
            "unit BOM cost times volume, plus sustaining engineering. The "
            "break-even volume is where the lines cross: below it, buy; "
            "above it, build - with the strategic factors (differentiation, "
            "supply assurance, core competence) able to overrule the math "
            "in writing. Module selection then follows the catalog "
            "grammar with module extras: certifications verified as carried "
            "by the module (a pre-certified radio still needs integration "
            "testing in your enclosure), the interface contract reviewed "
            "pin by pin, firmware support and update policy confirmed, and "
            "the vendor's financial health and EOL policy checked - because "
            "a module vendor's bankruptcy is your redesign. The demo "
            "computes the break-even volume between a $12 module and a "
            "$40k NRE plus $4 unit build."
        ),
        "key_points": [
            "Buy wins for commodities, expensive compliance (pre-certified radios), time-to-market, and non-core functions; build wins for differentiation, high volumes, exotic needs, and supply assurance.",
            "Total the lifetime cost both ways: buy = module x volume + integration + dependence risk; build = NRE + BOM x volume + sustaining.",
            "Break-even volume decides the math; strategic factors (differentiation, assurance) may overrule it - in writing.",
            "Modules get the full catalog grammar plus extras: carried certifications, firmware support, vendor longevity, interface contract.",
            "A pre-certified module still needs integration testing in your enclosure; the vendor's EOL policy is your redesign policy.",
        ],
        "requirements": [
            "A lifetime-volume estimate the whole comparison rests on, with sensitivity at half and double volume.",
            "A buy-side total: module price at volume, integration engineering, and quantified dependence risk.",
            "A build-side total: honest NRE (engineering, prototypes, compliance, certification), unit BOM, sustaining.",
            "A computed break-even volume with the strategic overrule, if any, documented.",
            "For bought modules: verified certifications, reviewed interface contract, confirmed firmware support, checked vendor health.",
        ],
        "standards": [
            "Module safety and EMC compliance follow the end product's applicable standards (certifications verified, not assumed).",
            "Radio modules follow FCC Part 15 / ETSI EN 300 328 modular-approval conditions for integration.",
            "Configuration control of bought modules follows ISO 10007; PCN/EOL monitoring per IEC 62402.",
        ],
        "citations": [CIT_IEC61000],
        "sig_lens": (
            "The Signature read: the module is the allied company - a whole "
            "formation marching under your banner. The Signature Parts "
            "Method counts the alliance's true cost, inspects its papers "
            "(certifications, firmware, longevity), and signs the treaty "
            "with eyes open, because allies are chosen, not inherited - "
            "and the armory's strength is measured in treaties kept."
        ),
    },
])
