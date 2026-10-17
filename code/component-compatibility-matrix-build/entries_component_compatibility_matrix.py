#!/usr/bin/env python3
"""Entries for the Component Compatibility Matrix databases (Build-210 #3,
top-20 priority).

Verified 2026-10-17 (Build-210 top-20 #3): RAW SWEEP over the full manifest
(2,388 databases) PLUS every shard index title in jah-databases-data-1:
zero 'component-compatibility*' slugs/names; zero 'component compatibility
matrix' title collisions. The one keyword near-hit, 'component-parts-catalog'
(JAH-CPTC-), is a parts CATALOG - it catalogs what each part is, its
properties and uses; it does not JUDGE pairings. This database is the
distinct capability the paste names: compatibility matrices that declare
whether parts, modules, materials, and interfaces WORK TOGETHER - interface
compatibility (voltage levels, logic families, protocols, connectors,
mechanical fit), material compatibility (galvanic, thermal, chemical),
module interoperability rules, and how to verify a pairing. The paste's rule
was applied by name/purpose/record schema/capabilities: judging pairings is
a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  component-compatibility-matrix           - The Component Compatibility
                                             Matrix Database (public-harvest:
                                             real, fact-checked compatibility
                                             engineering - every record a full
                                             compatibility-matrix entry with
                                             verdict rules, the numbers behind
                                             them, and verification
                                             procedures; standard references
                                             Horowitz and Hill The Art of
                                             Electronics 3rd ed 2015; JEDEC
                                             JESD8C LVCMOS; NXP UM10204 I2C;
                                             ISO 11898 CAN; IEEE 802.3
                                             Ethernet; IPC J-STD-001; IPC-2221;
                                             IPC-2152; IEC 60664-1; IEC
                                             61000-4-2; MIL-STD-889 galvanic;
                                             MIL-HDBK-217F; ISO 286 fits;
                                             IEC 60529 IP codes; JEDEC JESD79;
                                             ASME B1.1; ISO 898; Machinery's
                                             Handbook 31st ed 2020)
  component-compatibility-matrix-signature - The Component Compatibility
                                             Matrix Signature Database
                                             (his original Signature Handshake
                                             Method: every pairing a covenant,
                                             the matrix the ledger where
                                             handshakes are recorded,
                                             compatibility the honor kept
                                             between works; src signature,
                                             titles suffixed " (Signature
                                             Edition)", never presented as
                                             authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CPCM- (public) and JAH-CPCMS- (signature), verified free
in the manifest and in every shard index (zero hits; JAH-CPCT- belongs to the
Component and Parts Catalog database, a different capability entirely, so the
CPCM form was chosen to avoid substring confusion).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_component_compatibility_matrix.py). Every demo prints its
real computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Handshake Method: "
            "every pairing a covenant, the matrix the ledger where handshakes "
            "are recorded, and compatibility the honor kept between works. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_HOROWITZ = ("Horowitz P, Hill W. The Art of Electronics. 3rd ed. "
                "Cambridge University Press; 2015.")
CIT_MACHINERY = ("Oberg E, Jones FD, Horton HL, Ryffel HH. Machinery's "
                 "Handbook. 31st ed. Industrial Press; 2020.")
CIT_JESD8C = ("JEDEC JESD8C.01. Interface Standard for Nominal 3 V/3.3 V "
              "Supply Digital Integrated Circuits; 2007.")
CIT_UM10204 = ("NXP Semiconductors. UM10204. I2C-bus specification and user "
               "manual. Rev 7; 2021.")
CIT_ISO11898 = ("ISO 11898-1:2015. Road vehicles - Controller area network "
                "(CAN) - Data link layer and physical signalling.")
CIT_IEEE802 = ("IEEE Std 802.3-2022. IEEE Standard for Ethernet.")
CIT_JSTD001 = ("IPC J-STD-001H. Requirements for Soldered Electrical and "
               "Electronic Assemblies; 2021.")
CIT_IPC2221 = ("IPC-2221B. Generic Printed Board Design; 2023.")
CIT_IPC2152 = ("IPC-2152. Standard for Determining Current-Carrying "
               "Capability in Printed Board Design; 2009.")
CIT_IEC60664 = ("IEC 60664-1:2020. Insulation coordination for equipment "
                "within low-voltage supply systems.")
CIT_IEC61000 = ("IEC 61000-4-2:2008. Electromagnetic compatibility (EMC) - "
                "Testing and measurement techniques - Electrostatic discharge "
                "immunity test.")
CIT_MIL889 = ("MIL-STD-889D. Dissimilar Metals; 2016.")
CIT_MIL217 = ("MIL-HDBK-217F Notice 2. Reliability Prediction of Electronic "
              "Equipment; 1995.")
CIT_ISO286 = ("ISO 286-1:2010. Geometrical product specifications (GPS) - "
              "ISO code system for tolerances on linear sizes.")
CIT_IEC60529 = ("IEC 60529:2013. Degrees of protection provided by "
                "enclosures (IP Code).")
CIT_JESD79 = ("JEDEC JESD79-5A. DDR5 SDRAM; 2021.")
CIT_IEC60068 = ("IEC 60068-2-1:2007 / 60068-2-2:2007. Environmental testing - "
                "Cold and dry heat.")
CIT_ASMEB11 = ("ASME B1.1-2019. Unified Inch Screw Threads (UN, UNR, and UNJ "
               "Thread Forms).")
CIT_ISO898 = ("ISO 898-1:2013. Mechanical properties of fasteners made of "
              "carbon steel and alloy steel.")
CIT_JESD22 = ("JEDEC JESD22-A114F. Electrostatic Discharge (ESD) Sensitivity "
              "Testing, Human Body Model; 2016.")
CIT_MIL202 = ("MIL-STD-202H. Test Method Standard: Electronic and Electrical "
              "Component Parts; 2015.")

ENTRIES = [
    {
        "key": "what_is_compat",
        "name": "What Compatibility Means",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Compatibility is the answer to one question asked before two "
            "things are joined: will they work together, and for how long. "
            "It is not a property of a single part - no resistor is "
            "\"compatible\" by itself. Compatibility is a property of a "
            "PAIRING: this output driving that input, this bolt in that "
            "hole, this metal touching that metal, this protocol talking to "
            "that protocol. A pairing is judged on every dimension where the "
            "two parts touch: electrical (voltages, currents, impedances), "
            "mechanical (fit, fastening, vibration), logical (protocols, "
            "timing, software versions), thermal (heat made, heat removed), "
            "chemical (corrosion, contamination), and environmental "
            "(temperature, humidity, shock). The verdict for a pairing is "
            "always one of three: compatible (safe to join), incompatible "
            "(will fail or be damaged), or conditional (works only inside "
            "stated limits). This record frames the whole database: every "
            "later record is one shelf of the verdict book, teaching how to "
            "read a pairing, how to score it, and how to prove the verdict "
            "before the parts ever meet."
        ),
        "how_it_works": (
            "Judging a pairing works by reduction: the two datasheets are "
            "read as contracts, and each contract's promises are checked "
            "against the other's demands. Start with the absolute limits - "
            "if one side's output can exceed the other's survival rating, "
            "the pairing is dead on arrival. Then check the operating "
            "window: the driver's guaranteed output levels must land inside "
            "the receiver's guaranteed input window with margin left over. "
            "Then the physical layer: pins, pitch, package, and fastening "
            "must mate. Then the logical layer: both sides must speak the "
            "same protocol at the same speed with the same timing. Then the "
            "slow killers: dissimilar metals, thermal expansion, heat, "
            "humidity, and chemical exposure over the product's life. Each "
            "dimension gets its own verdict; the pairing's overall verdict "
            "is the WORST of the dimensions - one red cell fails the "
            "pairing. Document the verdict in the matrix so the next "
            "engineer never re-runs the analysis blind."
        ),
        "key_points": [
            "Compatibility is a property of a pairing, never of a single part: judge two datasheets against each other, not one datasheet alone.",
            "Every pairing is judged on electrical, mechanical, logical, thermal, chemical, and environmental dimensions - all six, every time.",
            "The only verdicts are compatible, incompatible, or conditional; conditional always names its limits.",
            "The pairing's overall verdict is the worst of its dimensions: one red cell fails the whole pairing.",
            "Verdicts go into a written matrix so they are decided once, by evidence, and reused forever.",
        ],
        "requirements": [
            "Both sides' datasheets or specification sheets, read as contracts with numbers, not marketing.",
            "The absolute maximum ratings of the weaker side, checked before any operating-window analysis.",
            "A stated service environment: temperature range, humidity, vibration, and life expectancy.",
            "A verdict format the team shares: green, yellow with stated limits, or red - never a shrug.",
            "A record of the verdict in the compatibility matrix so the decision outlives the decision-maker.",
        ],
        "standards": [
            "Pairing verdicts are evidence-based: stated ratings with test conditions from the manufacturer's datasheets, per MIL-STD-202 test methods for electronic parts.",
            "Mechanical mating follows Machinery's Handbook conventions for dimensions, threads, and fits (ISO 286).",
            "Environmental limits are stated per IEC 60068 environmental test conditions, not as single room-temperature numbers.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MACHINERY, CIT_IEC60068],
        "sig_lens": (
            "The Signature read: compatibility is the handshake between two "
            "works, and the matrix is the ledger where handshakes are "
            "recorded. Where public engineering files a datasheet, the "
            "Signature Handshake Method files a covenant: each side swears "
            "its limits, the pairing is judged on all six dimensions, and "
            "the ledger entry stands so no builder shakes the same hand "
            "twice in the dark."
        ),
    },
    {
        "key": "matrix_format",
        "name": "Reading and Writing a Compatibility Matrix",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A compatibility matrix is a table that answers pairing "
            "questions at a glance: rows are one side of the pairing, "
            "columns are the other side, and each cell holds the verdict. "
            "A well-built matrix cell holds four things: the verdict "
            "(compatible, conditional, or incompatible), the dimension that "
            "decides it, the numbers that prove it, and the date and "
            "evidence behind it. Colors carry the verdict - green, yellow, "
            "red - because an engineer scanning a hundred pairings needs the "
            "answer in the color before reading the footnote. Rows and "
            "columns are organized by family: logic families against logic "
            "families, metals against metals, protocols against protocols. "
            "Symmetric matrices (metal against metal) need only the upper "
            "triangle; directional matrices (driver against receiver) need "
            "the full rectangle, because driving is not the same as being "
            "driven. This record teaches the format the whole database "
            "uses: read the matrix first, and only open the datasheets when "
            "a cell says yellow."
        ),
        "how_it_works": (
            "Building a matrix works by filling cells from evidence, never "
            "from memory. Pick the two families to cross - say, five supply "
            "voltages against six logic families, or eight metals against "
            "eight metals. For each cell, run the pairing analysis: compare "
            "the governing numbers (voltage levels, potentials, expansion "
            "coefficients), decide the verdict, and write the one-line "
            "proof into the cell's note. Directional pairings are analyzed "
            "both ways: A driving B can be green while B driving A is red. "
            "Conditional cells carry their limits in the note (\"works with "
            "a series resistor below 10 MHz\"), and every cell carries a "
            "revision date because datasheets and standards get revised. "
            "Reading works in reverse: find your row, find your column, read "
            "the color; green means join, red means redesign, yellow means "
            "read the footnote and obey the limits exactly."
        ),
        "key_points": [
            "Rows are one side of the pairing, columns the other; each cell holds verdict, deciding dimension, proof numbers, and evidence date.",
            "Colors carry the verdict for scanning: green join, red redesign, yellow obey the footnote limits.",
            "Symmetric pairings (metal on metal) need only the upper triangle; directional pairings (driver on receiver) need the full rectangle.",
            "Conditional cells must state their limits in the cell note - a yellow without limits is a red waiting to happen.",
            "Every cell is dated: datasheets get revised, and a 2015 verdict on a revised part is a rumor, not evidence.",
        ],
        "requirements": [
            "A defined row family and column family - no matrix judges a pairing its axes cannot name.",
            "Cell-level evidence: the compared numbers from the two datasheets or standards, written into the note.",
            "A verdict vocabulary limited to three words: compatible, conditional, incompatible.",
            "Revision dates on every cell and a review cadence for the whole matrix.",
            "Symmetry declared up front: symmetric or directional, so readers know whether to trust the mirror cell.",
        ],
        "standards": [
            "Matrix cells cite the datasheet or standard section behind the verdict, with test conditions attached.",
            "Electrical verdicts follow JEDEC and IEC threshold conventions; mechanical verdicts follow ISO 286 fit practice.",
            "Corrosion cells follow MIL-STD-889 dissimilar-metals practice with the environment stated.",
        ],
        "citations": [CIT_JESD8C, CIT_ISO286, CIT_MIL889],
        "sig_lens": (
            "The Signature read: the matrix is the ledger of handshakes, "
            "and each cell is a sworn entry. The Signature Handshake "
            "Method demands the proof numbers beside every verdict, the "
            "date beside every proof, and the limits beside every yellow - "
            "because a covenant with no witnesses is just a wish, and the "
            "ledger is the witness."
        ),
    },
    {
        "key": "interface_dims",
        "name": "The Five Dimensions of a Pairing",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every pairing of engineered parts touches in five dimensions, "
            "and a pairing is only as compatible as its weakest one. The "
            "electrical dimension asks whether voltages, currents, and "
            "impedances agree - an output that swings 5 volts into an input "
            "rated for 3.3 volts is an electrical failure. The mechanical "
            "dimension asks whether the parts physically mate and stay "
            "mated: pin count, pitch, package, thread, fastening, and "
            "vibration survival. The logical dimension asks whether both "
            "sides speak the same language at the same speed: protocol, "
            "timing, addressing, and software version. The thermal "
            "dimension asks where the heat goes: one side's waste heat is "
            "the other side's ambient temperature. The chemical and "
            "environmental dimension asks what time does to the joint: "
            "corrosion, oxidation, creep, humidity, and chemical attack. "
            "Engineers fail pairings by checking one dimension and assuming "
            "the rest. This record teaches the five-dimension sweep: score "
            "each, and let the lowest score rule."
        ),
        "how_it_works": (
            "The five-dimension sweep works as a scorecard. Write the "
            "pairing at the top, then open one section per dimension. "
            "Electrical: list the driver's guaranteed outputs and the "
            "receiver's guaranteed inputs; check survival first, then "
            "operating windows, then current and power. Mechanical: check "
            "footprint, pitch, height, thread, torque, and retention under "
            "vibration. Logical: check protocol, speed, timing, addressing, "
            "and version compatibility. Thermal: add the driver stage's "
            "dissipation to the receiver's ambient and check the result "
            "against both temperature ratings. Chemical: check the material "
            "pair against the galvanic series and the service environment. "
            "Score each dimension 0 to 10, where 10 is margin-rich and 0 is "
            "a hard fail; a pairing ships only if every dimension scores 6 "
            "or better, because field failures always come from the "
            "dimension nobody scored."
        ),
        "key_points": [
            "The five dimensions are electrical, mechanical, logical, thermal, and chemical/environmental - all five, every pairing.",
            "Survival is checked before operation: absolute maximums first, operating windows second, in every dimension.",
            "Score each dimension 0-10; the pairing's score is the minimum of the five, never the average.",
            "A pairing ships only when every dimension scores 6 or better - field failures live in the unscored dimension.",
            "The scorecard is the evidence trail: numbers per dimension, verdict per pairing, filed in the matrix.",
        ],
        "requirements": [
            "A pairing definition naming both sides precisely: part numbers, revisions, and firmware versions where they matter.",
            "Per-dimension numbers from datasheets: thresholds, ratings, dimensions, timings, materials, temperature limits.",
            "A stated service environment and life: the pairing is judged for where it will live, not the lab bench.",
            "A minimum-score rule the team enforces, written down before the first scorecard, not after the first failure.",
            "The completed scorecard filed where the next engineer will find it: the compatibility matrix.",
        ],
        "standards": [
            "Electrical checks follow datasheet absolute-maximum and recommended-operating tables per MIL-STD-202 conventions.",
            "Mechanical checks follow ISO 286 fits and Machinery's Handbook thread and fastener practice.",
            "Environmental checks follow IEC 60068 conditions and IEC 60529 protection ratings.",
        ],
        "citations": [CIT_HOROWITZ, CIT_ISO286, CIT_IEC60529],
        "sig_lens": (
            "The Signature read: the five dimensions are the five fingers "
            "of the handshake - electrical, mechanical, logical, thermal, "
            "chemical. The Signature Handshake Method closes all five: a "
            "pairing that grips with four fingers and leaves one open is "
            "not a handshake, it is a dropped part, and the ledger records "
            "drops in red."
        ),
    },
    {
        "key": "voltage_levels",
        "name": "Voltage-Level Compatibility",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Voltage-level compatibility is the first electrical question "
            "in any pairing: can this output's voltages live inside that "
            "input's limits. Digital inputs read the world through two "
            "thresholds - VIL, the highest voltage still guaranteed to read "
            "as low, and VIH, the lowest voltage guaranteed to read as "
            "high. Outputs promise VOL, the highest voltage they will emit "
            "as low, and VOH, the lowest they will emit as high. A pairing "
            "works when the driver's VOL sits safely below the receiver's "
            "VIL and the driver's VOH sits safely above the receiver's VIH "
            "- the gaps are the noise margins, and margin is what keeps a "
            "working board working on a hot day with a noisy supply. The "
            "classic traps are the mixed-voltage pairings: a 5-volt output "
            "driving a 3.3-volt input whose absolute maximum is 3.6 volts "
            "will damage the input, and a 3.3-volt output driving a 5-volt "
            "CMOS input whose VIH is 3.5 volts will read as neither high "
            "nor low. This record teaches the four-number check and the "
            "three cures: level shifters, open-drain with pull-up, and "
            "choosing parts whose windows already overlap."
        ),
        "how_it_works": (
            "The check works by stacking four numbers. From the driver's "
            "datasheet take VOL maximum and VOH minimum. From the receiver's "
            "datasheet take VIL maximum and VIH minimum, plus the input's "
            "absolute maximum voltage. First the survival test: the "
            "driver's highest possible output - including overshoot - must "
            "stay below the receiver's absolute maximum. Then the logic "
            "tests: VOL max must be below VIL max (low margin), and VOH min "
            "must be above VIH min (high margin). Margins under 0.2 volts "
            "are yellow - they work on the bench and fail in the field. "
            "When a test fails, the cures are: a level-shifter IC (cleanest, "
            "costs a part), an open-drain output with a pull-up to the "
            "receiver's rail (free, but only if the driver is open-drain "
            "and the speed allows), or re-selecting the receiver for "
            "TTL-compatible thresholds (the 74HCT family exists for exactly "
            "this). Never use a series resistor as a level shifter - it "
            "forms a divider with the input's leakage and protection "
            "diodes, and the margin it gives is imaginary."
        ),
        "key_points": [
            "Four numbers decide it: driver VOL/VOH against receiver VIL/VIH, with the receiver's absolute maximum checked first.",
            "Noise margin is the gap between what the driver guarantees and what the receiver demands - margin under 0.2 V is a yellow cell.",
            "5 V into a 3.3 V input rated 3.6 V absolute maximum is damage, not a logic problem.",
            "3.3 V LVCMOS into 5 V 74HC (VIH 3.5 V) fails the high test; into 5 V 74HCT (VIH 2.0 V) it passes.",
            "Cures are level shifters, open-drain with pull-up to the receiver rail, or TTL-threshold receivers - never a series resistor.",
        ],
        "requirements": [
            "Driver datasheet: VOL maximum, VOH minimum, and whether the output is push-pull or open-drain.",
            "Receiver datasheet: VIL maximum, VIH minimum, and absolute maximum input voltage.",
            "A stated noise environment: the margin rule tightens on noisy boards and long cables.",
            "A chosen cure for every failed test, documented before layout, not discovered at bring-up.",
            "The verdict entered in the voltage-level matrix with the four numbers as evidence.",
        ],
        "standards": [
            "LVCMOS thresholds follow JEDEC JESD8C (VIH 0.7 x VDDQ, VIL 0.3 x VDDQ for 3.3 V logic).",
            "TTL-compatible thresholds follow the 74HCT convention: VIH 2.0 V, VIL 0.8 V.",
            "Absolute-maximum survival ratings are per the receiver datasheet, tested per MIL-STD-202 methods.",
        ],
        "citations": [CIT_HOROWITZ, CIT_JESD8C, CIT_MIL202],
        "sig_lens": (
            "The Signature read: voltage levels are the volume of the "
            "handshake - too loud and the ear is damaged, too soft and the "
            "words are lost. The Signature Handshake Method tunes every "
            "electrical greeting to land inside the listener's hearing: "
            "margins written down, survival checked first, and no resistor "
            "ever asked to do a translator's job."
        ),
    },
    {
        "key": "logic_families",
        "name": "Logic Families and Their Pairings",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Logic families are tribes of digital parts that share supply "
            "voltages, thresholds, and speed: 74LS and 74ALS (5 V TTL, "
            "legacy), 74HC and 74HCT (5 V CMOS, the workhorses), 74LVC and "
            "74LV (3.3 V and below, modern low-voltage), 74AC and 74ACT "
            "(5 V high-speed CMOS), and the 4000 series (wide-voltage CMOS, "
            "slow but nearly indestructible). Each family publishes its "
            "tribe rules: supply range, input thresholds, output drive, and "
            "speed. Pairings inside one family always work - that is what "
            "the family promise means. Pairings across families are the "
            "compatibility question, and the answers form the classic "
            "matrix every digital engineer learns: 74HCT drives anything "
            "5 V because its inputs are TTL-compatible; 74LVC accepts 5 V "
            "on its inputs (on 5-volt-tolerant parts) but its 3.3 V "
            "outputs cannot drive 74HC's 3.5 V VIH; 4000-series parts run "
            "on anything from 3 to 18 V but are too slow for fast buses. "
            "This record teaches the family table: who can drive whom, in "
            "which direction, and where the level shifter goes."
        ),
        "how_it_works": (
            "The family matrix is built from four numbers per family: "
            "supply range, VIH, VIL, VOH, VOL - five numbers, really - plus "
            "the input's absolute maximum. Each ordered pair of families "
            "gets the four-number voltage check in both directions, because "
            "A driving B and B driving A are different questions. "
            "74HC (5 V) driving 74HCT (5 V): green both ways - the "
            "thresholds nest. 74LVC (3.3 V) driving 74HCT (5 V, VIH 2.0 V): "
            "green - the 3.3 V VOH clears 2.0 V with margin. 74LVC driving "
            "74HC (5 V, VIH 3.5 V): red - a 3.3 V output cannot promise 3.5 "
            "V. 74HC (5 V) driving 74LVC (3.3 V): red on survival unless the "
            "LVC part is 5-volt-tolerant - 5 V exceeds the 3.6-4.6 V "
            "absolute maximum of most 3.3 V inputs. The matrix also notes "
            "speed: 4000-series driving 74AC is electrically fine and "
            "logically hopeless above a few megahertz. Families are "
            "checked at their real supply rails, because a 74HC at 3.3 V "
            "is a different tribe member than a 74HC at 5 V."
        ),
        "key_points": [
            "Inside one family, pairings always work; across families, every ordered pair gets its own verdict.",
            "74HCT is the universal receiver at 5 V: its TTL thresholds accept 3.3 V LVCMOS and 5 V CMOS alike.",
            "74LVC drives 74HCT but not 74HC; 5 V CMOS drives 74LVC only on 5-volt-tolerant inputs.",
            "Check both directions: driver-to-receiver and receiver-to-driver are different cells.",
            "Supply rail matters as much as family name: a 74HC at 3.3 V has different thresholds than at 5 V.",
        ],
        "requirements": [
            "The two families' supply rails as actually powered, not as the part number suggests.",
            "Each family's VIH, VIL, VOH, VOL, and input absolute maximum from the datasheet.",
            "A stated operating frequency: electrically-green pairings can still fail on speed.",
            "Level-shifter placement for every red cell the design still needs.",
            "The family matrix on the wall or in the file, dated and revisioned.",
        ],
        "standards": [
            "CMOS thresholds follow JEDEC JESD8C for 3.3 V parts and the 74HC/4000-series datasheet conventions at 5 V.",
            "TTL thresholds (VIH 2.0 V, VIL 0.8 V) follow the 74LS/74HCT convention documented in Horowitz and Hill.",
            "Input absolute maximums are per the receiving part's datasheet; tolerance of 5 V inputs is a per-part feature, never assumed.",
        ],
        "citations": [CIT_HOROWITZ, CIT_JESD8C],
        "sig_lens": (
            "The Signature read: logic families are dialects, and the "
            "matrix is the phrasebook. The Signature Handshake Method "
            "learns each tribe's thresholds the way a traveler learns "
            "greetings: 74HCT the universal hello at five volts, 74LVC the "
            "modern tongue that must not be shouted at, and every crossing "
            "logged in the ledger before the first board is built."
        ),
    },
    {
        "key": "current_power",
        "name": "Current and Power Delivery Compatibility",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Current compatibility asks whether the supply side can feed "
            "the load side without sagging, overheating, or tripping: a "
            "regulator rated 1 amp feeding a load that draws 1.2 amps is a "
            "pairing that works until the thermal protection discovers it. "
            "The check has three parts. First the average: the sum of every "
            "load's average current must sit below the source's continuous "
            "rating with margin - the 80 percent rule keeps regulators in "
            "their comfortable zone. Second the peaks: loads like motors, "
            "radios, and processors draw short bursts far above their "
            "average, and the source must ride through the peaks without its "
            "voltage collapsing below every load's minimum. Third the path: "
            "the wires, traces, and connectors between source and load must "
            "carry the current without excessive drop or heating, per "
            "IPC-2152 current-carrying guidance. This record teaches the "
            "budget table: list every load, sum the averages, check the "
            "peaks, size the path, and prove the supply pairing before the "
            "first power-on."
        ),
        "how_it_works": (
            "The budget works like bookkeeping. List every load with its "
            "average current, its peak current, and the peak's duration. "
            "Sum the averages and compare against the source's continuous "
            "rating: the design rule is total average at or below 80 "
            "percent of the rating, leaving headroom for heat and aging. "
            "Then check the peaks: the source's transient capability plus "
            "the bulk capacitance must hold the rail above the minimum "
            "operating voltage of every load through the longest peak - "
            "capacitor energy (one-half C V squared, spent between the "
            "nominal and minimum rail) is the usual bridge. Then the path: "
            "trace width from IPC-2152 for the RMS current, connector "
            "current rating per pin (derated for adjacent loaded pins), and "
            "wire gauge for the drop budget - a 5 percent drop on a 5-volt "
            "rail is 0.25 volts the loads never see. Protection must agree "
            "too: the fuse or current limit must sit above the worst "
            "legitimate peak and below the wire's damage current, or the "
            "protection becomes the failure."
        ),
        "key_points": [
            "Three checks: average current within 80 percent of the source rating, peaks ridden through without rail collapse, path sized for current and drop.",
            "Peak current, not average, kills rails: size bulk capacitance from the energy the peak needs, not the datasheet's typical load.",
            "Connectors and traces are part of the pairing: IPC-2152 for traces, per-pin ratings derated for neighbors.",
            "Protection must thread the needle: above the worst legitimate peak, below the wire's damage current.",
            "The budget table is the evidence: every load listed, every number sourced, margin visible.",
        ],
        "requirements": [
            "Every load's average current, peak current, and peak duration from its datasheet or measurement.",
            "The source's continuous rating, transient capability, and protection thresholds.",
            "The path ratings: trace geometry, connector per-pin current, wire gauge and length.",
            "Every load's minimum operating voltage, so the rail-collapse check has a floor.",
            "The completed budget table filed with the power architecture, dated.",
        ],
        "standards": [
            "Trace current capacity follows IPC-2152; general board design follows IPC-2221B.",
            "Connector current ratings are per the connector datasheet, derated per the manufacturer's guidance for fully loaded housings.",
            "Wire ampacity follows the applicable wire standard for the insulation temperature rating in the service environment.",
        ],
        "citations": [CIT_IPC2152, CIT_IPC2221, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: current is the food of the circuit, and "
            "the budget is the seating chart. The Signature Handshake "
            "Method feeds every load its honest share: averages within the "
            "eighty-percent covenant, peaks bridged by stored energy, and "
            "no wire asked to carry more than its rating swore it could."
        ),
    },
    {
        "key": "connector_fit",
        "name": "Connector Mechanical Fit and Mating",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Two connectors are compatible when they mate fully, stay "
            "mated, and pass every signal and amp they promise - which is "
            "a longer checklist than \"the pins line up.\" The mechanical "
            "check covers footprint and pitch (the plug must match the "
            "receptacle's pin spacing exactly - 2.54 mm plugs do not mate "
            "with 2.00 mm receptacles), mating height and polarization "
            "(keyed housings that refuse backwards insertion), retention "
            "(latches, screws, or friction that survive the service "
            "vibration), and durability (mating cycles: a 30-cycle "
            "consumer connector dies young in a daily-mated test jig). The "
            "electrical check covers current per pin, voltage rating "
            "(creepage and clearance per IEC 60664-1), and contact "
            "resistance. The classic failures are the near-miss: a header "
            "that seats 90 percent of the way and passes at the bench, a "
            "latch that holds in the lab and walks out in the truck, a "
            "power pin sharing a housing with signal pins and cooking its "
            "neighbors. This record teaches the mating checklist that "
            "turns \"it plugs in\" into a proven pairing."
        ),
        "how_it_works": (
            "The mating check works in layers. First identity: the plug "
            "series and the receptacle series must be the manufacturer's "
            "declared mates - same series, same pin count, same pitch, same "
            "keying. Second geometry: overall height when mated must clear "
            "the enclosure; polarization features must make wrong-way "
            "insertion impossible, not merely difficult. Third retention: "
            "the latch or screw force must exceed the service vibration and "
            "pull forces with margin, per the connector's datasheet. Fourth "
            "electrical: per-pin current at the service temperature "
            "(derated when all pins carry current), voltage rating with "
            "creepage for the pollution degree, contact resistance times "
            "current for the heat each pin adds. Fifth life: mating cycles "
            "must exceed the product's lifetime insertions by a factor of "
            "two or more. The proof is physical: mate the pair, measure "
            "insertion force, verify full seating with a witness mark, "
            "shake it, thermal-cycle it, and re-measure contact resistance "
            "- the numbers before and after are the compatibility evidence."
        ),
        "key_points": [
            "Identity first: declared mates by series, pin count, pitch, and keying - near-miss series are red cells.",
            "Polarization must make wrong-way mating impossible, not merely awkward.",
            "Current rating is per pin at temperature and derates when neighbors also carry current.",
            "Mating-cycle life must exceed lifetime insertions by 2x or more; test jigs eat connectors.",
            "Prove it physically: seat, mark, vibrate, thermal-cycle, re-measure contact resistance.",
        ],
        "requirements": [
            "Both connectors' series, pin count, pitch, and keying from the manufacturer datasheets.",
            "Service vibration, pull forces, and insertion count over the product's life.",
            "Per-pin current at the service temperature, voltage rating, and pollution degree for creepage.",
            "Enclosure clearances for the mated height, including tolerance stack-up.",
            "A mated-pair test record: insertion force, witness marks, vibration and thermal-cycle results.",
        ],
        "standards": [
            "Creepage and clearance follow IEC 60664-1 for the working voltage and pollution degree.",
            "Current ratings are per the connector datasheet at the stated temperature, derated per manufacturer guidance.",
            "Mating durability is per the connector's specified cycle life; test methods follow the manufacturer's qualification practice.",
        ],
        "citations": [CIT_IEC60664, CIT_IPC2221, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: a connector is a handshake made of metal, "
            "and the mating checklist is the etiquette. The Signature "
            "Handshake Method seats every plug fully, latches it against "
            "the road's shaking, and proves the grip with a witness mark - "
            "because a handshake that lets go in the truck was never a "
            "handshake."
        ),
    },
    {
        "key": "protocols",
        "name": "Protocol Compatibility: UART, SPI, I2C, CAN, USB, Ethernet",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Protocol compatibility asks whether two devices can hold a "
            "conversation: same language, same speed, same manners. The "
            "wired protocols each carry their own pairing rules. UART is "
            "the simplest - two wires, but both sides must agree on baud "
            "rate, data bits, parity, and stop bits, and their clocks must "
            "match within a few percent or framing errors appear. SPI is a "
            "four-wire master-driven bus: mode (clock polarity and phase, "
            "0-3), bit order, and maximum clock rate must agree, and every "
            "slave needs its own chip-select. I2C is a two-wire multi-master "
            "bus with 7-bit addressing: no two devices may share an "
            "address, pull-up resistors must suit the bus capacitance, and "
            "speeds must overlap. CAN is a rugged two-wire differential "
            "bus needing 120-ohm termination at both ends and matching bit "
            "rates. USB and Ethernet are point-to-point and networked "
            "standards where the pairing question moves to versions, "
            "speeds, power delivery, and cable quality. This record teaches "
            "the per-protocol handshake checklist."
        ),
        "how_it_works": (
            "Each protocol gets its own compatibility proof. UART: compute "
            "the baud-rate error of each side's clock against the nominal "
            "rate - both sides within 2 percent is the practical rule, and "
            "the frame format (8-N-1 and friends) must match exactly. SPI: "
            "confirm the mode number matches (CPOL/CPHA), the master's "
            "clock stays under the slave's maximum, and chip-select "
            "polarity is right. I2C: list every device address and prove "
            "uniqueness (watch the fixed-address sensors), size the "
            "pull-ups from the bus capacitance per UM10204 - too strong and "
            "devices cannot pull low, too weak and rise times fail at "
            "speed. CAN: verify both ends terminated at 120 ohms, bit "
            "rates identical, and transceivers rated for the bus voltage. "
            "USB: check version and speed overlap, power roles, and cable "
            "rating. Ethernet: check speed and duplex negotiation overlap "
            "and magnetics ratings. Mixed-protocol pairings (UART to USB) "
            "are red unless a bridge IC is in the design - protocols do not "
            "translate themselves."
        ),
        "key_points": [
            "UART: baud rates within 2 percent and identical frame format, or framing errors.",
            "SPI: mode number, bit order, max clock, and one chip-select per slave must all agree.",
            "I2C: unique 7-bit addresses for every device and pull-ups sized to the bus capacitance.",
            "CAN: 120-ohm termination at both ends and identical bit rates; USB/Ethernet: version, speed, power, and cable overlap.",
            "Different protocols never mate directly: a bridge IC is a design element, not an adapter cable.",
        ],
        "requirements": [
            "Each device's supported protocols, speeds, modes, and addresses from the datasheets.",
            "Clock accuracy figures for UART pairings: the baud-error math needs real oscillator tolerances.",
            "Bus capacitance and device count for I2C pull-up sizing.",
            "Cable and termination specifications for CAN, USB, and Ethernet pairings.",
            "A protocol handshake table in the design file: who talks to whom, how fast, in what mode.",
        ],
        "standards": [
            "I2C timing and pull-up sizing follow NXP UM10204.",
            "CAN physical layer follows ISO 11898-1 with 120-ohm termination.",
            "Ethernet follows IEEE 802.3; USB signaling and power follow the USB-IF specifications for the version in use.",
        ],
        "citations": [CIT_UM10204, CIT_ISO11898, CIT_IEEE802, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: protocols are languages, and the checklist "
            "is the interpreter's oath. The Signature Handshake Method "
            "lets no two devices speak until the baud rates agree, the "
            "addresses are unique, and the modes match - because a "
            "conversation where neither side is understood is not "
            "communication, it is noise with wires."
        ),
    },
    {
        "key": "impedance",
        "name": "Signal Integrity and Impedance Matching",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Above a few megahertz, a wire stops being a wire and becomes "
            "a transmission line, and pairings must respect impedance or "
            "pay in reflections. Every high-speed interface declares its "
            "characteristic impedance: 50 ohms single-ended for most RF and "
            "many digital links, 90 or 100 ohms differential for USB, "
            "Ethernet, and LVDS, 120 ohms for CAN. When a driver, cable, "
            "and receiver all share the same impedance, the signal's energy "
            "flows into the load; when they differ, part of the energy "
            "reflects back, and the reflection adds to later bits as noise, "
            "jitter, and eye closure. The mismatch is quantified by the "
            "reflection coefficient: the difference of the impedances over "
            "their sum. A 50-ohm driver into a 75-ohm load reflects 20 "
            "percent of the voltage - enough to corrupt fast edges. This "
            "record teaches the impedance check: know the three "
            "impedances, compute the reflection, and terminate the line "
            "where the standard says to."
        ),
        "how_it_works": (
            "The check works by naming three impedances: the driver's "
            "source impedance, the cable or trace impedance, and the "
            "receiver's load impedance. Compute the reflection coefficient "
            "at each junction: gamma equals (Zload minus Zsource) divided "
            "by (Zload plus Zsource). A gamma under 0.1 is green; 0.1 to "
            "0.2 is yellow - it works with margin eaten; above 0.2 is red "
            "for fast edges. The cures are termination: series termination "
            "at the source (resistor equals line impedance minus driver "
            "impedance), parallel termination at the load (resistor equals "
            "line impedance to the rail), or differential termination "
            "across the pair. Cable choice is part of the pairing: 50-ohm "
            "coax with a 75-ohm system is a red cell no termination "
            "resistor fully fixes. The proof is measured: a time-domain "
            "reflectometer or a clean eye diagram at the receiver is the "
            "evidence the matrix cell wants."
        ),
        "key_points": [
            "Name three impedances - source, line, load - and compute the reflection coefficient at each junction.",
            "Gamma under 0.1 is green, 0.1-0.2 yellow, above 0.2 red for fast edges.",
            "Standard impedances: 50 ohm single-ended, 90/100 ohm differential, 120 ohm CAN - match the standard, not the habit.",
            "Termination cures mismatch: series at source, parallel at load, across the pair for differential.",
            "Prove with measurement: TDR or an open eye diagram is the evidence behind the cell.",
        ],
        "requirements": [
            "The declared impedance of each side: driver, cable/trace, receiver, from datasheets or the standard.",
            "The signal's edge rate or highest frequency: slow signals forgive, fast edges do not.",
            "The termination scheme the standard mandates, placed where the standard says.",
            "Cable and connector impedance ratings matching the system impedance.",
            "A measured eye diagram or TDR trace for yellow cells before they ship.",
        ],
        "standards": [
            "Differential pair impedances follow the interface standard: 90 ohm USB, 100 ohm Ethernet/LVDS, 120 ohm CAN per ISO 11898.",
            "Board trace impedance targets follow IPC-2221B controlled-impedance design practice.",
            "Measurement practice follows the interface standard's compliance test methods.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IPC2221, CIT_ISO11898],
        "sig_lens": (
            "The Signature read: impedance is the firmness of the grip - "
            "too loose and the signal slips back, too tight and it "
            "bounces. The Signature Handshake Method matches every "
            "high-speed grip to the standard's measure and terminates what "
            "it cannot match, so the energy arrives whole and the ledger "
            "records a clean eye."
        ),
    },
    {
        "key": "tolerance_fit",
        "name": "Tolerance and Clearance for Mating Parts",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Mechanical compatibility lives or dies in the thousandths: a "
            "shaft and a bore are compatible only when their tolerances "
            "guarantee the intended fit. The ISO 286 system gives every "
            "mating pair a language: clearance fits (the shaft is always "
            "smaller - parts slide), transition fits (sometimes clearance, "
            "sometimes interference - parts tap together), and interference "
            "fits (the shaft is always larger - parts press or shrink "
            "together). A 20 mm H7/g6 pairing always clears; a 20 mm H7/p6 "
            "pairing always interferes; a 20 mm H7/k6 might do either. The "
            "compatibility question is whether the WORST-CASE combination "
            "- largest shaft with smallest hole, or the reverse - still "
            "gives the intended behavior, because manufacturing makes every "
            "size in the tolerance band, not the nominal. Tolerance stack-up "
            "extends the same thinking across chains of parts: five parts "
            "each within tolerance can still fail to assemble if the stack "
            "was never analyzed. This record teaches the fit check: compute "
            "the worst cases, name the fit, and prove the chain assembles."
        ),
        "how_it_works": (
            "The fit check works from the tolerance tables. For a shaft and "
            "bore, look up the fundamental deviations and tolerance grades: "
            "H7 bore means the hole runs from nominal to nominal plus 21 "
            "microns at 20 mm; a g6 shaft runs from 7 to 20 microns UNDER "
            "nominal. The worst-case maximum clearance is the largest hole "
            "minus the smallest shaft; the worst-case minimum clearance "
            "(or maximum interference) is the smallest hole minus the "
            "largest shaft. If the minimum clearance stays positive, the "
            "fit always clears - green. If the maximum interference stays "
            "positive, it always presses - green for press fits. If the "
            "band straddles zero, it is a transition fit: conditional, and "
            "the design must tolerate both outcomes. For chains, add the "
            "tolerances: worst-case stack is the arithmetic sum (pessimistic "
            "but safe), statistical stack is the root-sum-square (realistic "
            "for many parts). Never assume nominal: the factory ships the "
            "whole band."
        ),
        "key_points": [
            "Clearance, transition, and interference fits are decided by the worst-case combination, never the nominal sizes.",
            "H7/g6 always clears, H7/p6 always interferes, H7/k6 may do either - the letters are the verdict.",
            "Worst-case stack-up adds tolerances arithmetically; statistical stack-up uses root-sum-square for long chains.",
            "Transition fits are conditional cells: the design must survive both clearance and interference outcomes.",
            "The factory ships the whole tolerance band - a pairing proven only at nominal is unproven.",
        ],
        "requirements": [
            "Both parts' tolerance designations (ISO 286 code or explicit plus/minus limits) from the drawings.",
            "The intended fit behavior stated up front: must-clear, must-press, or may-do-either.",
            "The full tolerance chain for multi-part assemblies, not just the mating pair.",
            "Service temperature range: thermal expansion shifts fits, especially in mixed materials.",
            "The fit calculation filed with the drawing package, dated.",
        ],
        "standards": [
            "Fits follow ISO 286-1:2010; inch-unit practice follows Machinery's Handbook.",
            "Threads follow ASME B1.1-2019 (unified) or ISO metric thread standards with the class stated.",
            "Temperature effects on fits are computed from material expansion coefficients per Machinery's Handbook.",
        ],
        "citations": [CIT_ISO286, CIT_MACHINERY, CIT_ASMEB11],
        "sig_lens": (
            "The Signature read: tolerance is the honesty of the "
            "handshake's grip - the ledger records not the intended squeeze "
            "but the loosest and the tightest the factory can honestly "
            "deliver. The Signature Handshake Method proves the fit at both "
            "edges of the band, because a covenant signed at nominal and "
            "broken at the limits was never signed."
        ),
    },
    {
        "key": "datasheet_cross",
        "name": "Reading Two Datasheets Side by Side",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every compatibility verdict in this database is built the same "
            "way: two datasheets open side by side, and the numbers "
            "compared line by line. The skill is knowing which lines to "
            "compare and which footnotes change the meaning. The reading "
            "order never varies: absolute maximum ratings first (the "
            "survival walls), recommended operating conditions second (the "
            "room the part promises to work in), electrical or mechanical "
            "characteristics third (typical versus minimum/maximum - "
            "typicals are not guaranteed), graphs fourth (behavior between "
            "the table rows), mechanical drawings fifth, and ordering "
            "information last. The traps sit in the footnotes: a VOH "
            "guaranteed only at 4 mA of load, a current rating valid only "
            "at 25 C ambient, an input threshold that moves with the "
            "supply rail. This record teaches the two-datasheet drill: "
            "same table, two columns, footnotes read aloud, verdict "
            "written with the evidence attached."
        ),
        "how_it_works": (
            "The drill works as a comparison table. Draw the governing "
            "rows: supply range, input thresholds, output levels, current "
            "ratings, temperature range, package and pinout, timing, and "
            "absolute maximums. Fill the driver column from datasheet A "
            "and the receiver column from datasheet B, copying the "
            "footnote conditions into the cell (\"at 25 C\", \"sourcing 4 "
            "mA\", \"VCC = 5 V\"). Compare row by row with the conditions "
            "in view: a VOH of 4.4 V minimum at 4 mA load paired with a "
            "receiver drawing 8 mA is not the green it appears. Flag every "
            "row where the conditions differ - those rows need derating "
            "math or a test, not a glance. The verdict column gets one of "
            "the three words per row; the pairing verdict is the worst "
            "row. Two engineers running the same drill on the same pair "
            "should reach the same verdict - if they do not, the drill "
            "found an ambiguous footnote, which is itself a finding."
        ),
        "key_points": [
            "Reading order is fixed: absolute maximums, operating conditions, characteristics tables, graphs, mechanical, ordering.",
            "Typical values are not guaranteed; maximum ratings are survival limits, not operating limits.",
            "Every compared number carries its footnote condition - mismatched conditions are flagged, not averaged.",
            "Two engineers must reach the same verdict; disagreement means the footnote is ambiguous, which is a finding.",
            "The comparison table is the evidence: two columns, footnotes visible, verdict per row.",
        ],
        "requirements": [
            "Current-revision datasheets for both parts - a verdict on a superseded revision is a rumor.",
            "The full footnote text for every compared number, copied, not paraphrased.",
            "A stated operating point: supply, load, temperature, and speed the pairing will actually see.",
            "A comparison table template the team reuses, so drills are comparable across pairings.",
            "The completed table filed in the matrix cell's evidence.",
        ],
        "standards": [
            "Datasheet test conditions follow MIL-STD-202 conventions for electronic parts.",
            "Mechanical data follows the manufacturer's drawing with ISO 286 tolerance practice.",
            "Revision control: verdicts cite the datasheet revision and date.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MIL202, CIT_ISO286],
        "sig_lens": (
            "The Signature read: two datasheets side by side are two "
            "witnesses sworn under the same oath, and the drill is the "
            "cross-examination. The Signature Handshake Method reads the "
            "footnotes aloud, compares with conditions in view, and writes "
            "the verdict where both witnesses can see it - because "
            "handshakes witnessed are handshakes kept."
        ),
    },
    {
        "key": "material_basics",
        "name": "Material Compatibility Basics",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Materials meet in three ways that can each fail a pairing: "
            "they touch and corrode (galvanic action), they heat and pull "
            "apart (thermal expansion mismatch), and they sit in chemicals "
            "that attack one of them. The material compatibility check "
            "starts with identity: name the actual alloys, not the family - "
            "\"aluminum\" is not a material, 6061-T6 is, and 6061 against "
            "304 stainless behaves differently than 7075 against brass. "
            "Then the three questions. Galvanic: how far apart are the two "
            "metals on the galvanic series in the service environment, and "
            "is an electrolyte present. Thermal: how far apart are their "
            "expansion coefficients, and what temperature swing will the "
            "joint see. Chemical: what fluids, fumes, and UV will reach "
            "the joint over its life. Plastics get the same treatment: "
            "chemical resistance charts, UV stability, and creep under "
            "sustained load. This record teaches the material-pairing "
            "triage that decides which of the three deep records a pairing "
            "needs."
        ),
        "how_it_works": (
            "Triage works as three quick screens. Screen one, galvanic: "
            "find both metals on the galvanic series for the service "
            "environment (seawater, industrial air, rural air behave "
            "differently); a potential difference above about 0.25 V in "
            "seawater flags the pair for the galvanic record, and any "
            "pair with a small anode (a steel screw in a large aluminum "
            "plate) gets flagged regardless, because the small side "
            "corrodes fast. Screen two, thermal: take the difference in "
            "expansion coefficients times the temperature swing times the "
            "joint length - that is the relative motion the joint must "
            "absorb every cycle; rigid joints with large motion go to the "
            "thermal record. Screen three, chemical: check the wetted "
            "materials against the chemical resistance data for every "
            "fluid the service environment promises. A pair passing all "
            "three screens is green; any flag sends the pairing to the "
            "deep record for that mechanism, and the cell stays yellow "
            "until the deep analysis lands."
        ),
        "key_points": [
            "Name the alloy, not the family: 6061-T6 against 304 stainless is a different pairing than 7075 against brass.",
            "Three screens: galvanic potential gap, thermal expansion motion, chemical resistance - flag any, green only on all three.",
            "Small anodes are the killer: a steel screw in a big aluminum plate corrodes far faster than equal areas.",
            "Thermal motion is coefficient difference times temperature swing times length - compute it, do not feel it.",
            "Triage decides which deep record a pairing needs; the cell stays yellow until the deep analysis is filed.",
        ],
        "requirements": [
            "Actual alloy and temper designations for both materials, from the drawing or the mill cert.",
            "The service environment: electrolyte presence, temperature swing, fluids, UV, and life.",
            "Galvanic series data for that environment, not a generic table.",
            "Joint geometry: the length over which thermal motion accumulates and the anode/cathode area ratio.",
            "The triage result recorded: green, or flagged to which deep record.",
        ],
        "standards": [
            "Galvanic series data follows MIL-STD-889 for the stated environment.",
            "Expansion coefficients follow Machinery's Handbook material data.",
            "Chemical resistance follows the material manufacturer's published compatibility charts for the stated chemicals.",
        ],
        "citations": [CIT_MIL889, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: materials are the flesh of the handshake, "
            "and triage is the physician's glance. The Signature Handshake "
            "Method names every alloy honestly, screens all three "
            "afflictions, and never declares a material healthy on a "
            "glance - the deep examination follows every flag, and the "
            "ledger waits for its report."
        ),
    },
    {
        "key": "galvanic",
        "name": "Galvanic Corrosion Pairings",
        "group": "Compounded",
        "ladder_rank": 3,
        "ladder_tier": "compounded",
        "description": (
            "When two different metals touch in the presence of an "
            "electrolyte - salt spray, rain, condensation, even humid air - "
            "they form a battery, and the more active metal corrodes to "
            "protect the nobler one. This is galvanic corrosion, the "
            "slowest and most certain pairing failure in the database. The "
            "galvanic series ranks metals by their electrical potential: "
            "magnesium and zinc at the active end, aluminum and steel in "
            "the middle, copper and brass nobler, stainless steels and "
            "titanium and graphite at the noble end. The corrosion rate "
            "follows two rules: the bigger the potential difference, the "
            "harder the drive; and the smaller the anode's area relative to "
            "the cathode's, the faster it is eaten - a stainless screw in "
            "an aluminum panel is a classic red cell, while an aluminum "
            "rivet in a stainless panel is far gentler. This record "
            "teaches the galvanic matrix: which metal pairs are safe, "
            "which need isolation, and which are forbidden."
        ),
        "how_it_works": (
            "The analysis works from the galvanic series for the service "
            "environment. Look up both metals' potentials (in seawater: "
            "magnesium about -1.4 V, zinc -1.0 V, aluminum -0.6 to -0.75 "
            "V, steel -0.4 to -0.6 V, copper -0.1 to -0.2 V, 316 stainless "
            "near 0.0 V, titanium +0.1 V, graphite +0.3 V, all versus "
            "saturated calomel). Take the absolute difference: under 0.15 "
            "V is green in most environments; 0.15 to 0.25 V is yellow - "
            "acceptable in dry indoor service, risky outdoors; above 0.25 "
            "V in a wet environment is red without mitigation. Then apply "
            "the area rule: divide the cathode area by the anode area - "
            "ratios above 10:1 with a small anode escalate any yellow to "
            "red. The cures, in order of reliability: choose closer metals "
            "(the honest fix), isolate with non-conductive gaskets and "
            "sleeves (breaks the circuit), coat the CATHODE (coating the "
            "anode merely moves the attack to the pinholes), or accept "
            "and inspect on a schedule (documented, never silent)."
        ),
        "key_points": [
            "Potential difference drives it: under 0.15 V green, 0.15-0.25 V yellow, above 0.25 V in wet service red.",
            "Area ratio multiplies it: a small anode feeding a large cathode corrodes catastrophically fast.",
            "Stainless screws in aluminum panels are the classic red cell; the reverse pairing is far gentler.",
            "Cures in order: closer metals, isolation, coat the cathode - never rely on coating the anode alone.",
            "No electrolyte, no galvanic cell: sealed dry environments genuinely change the verdict.",
        ],
        "requirements": [
            "Both metals' positions on the galvanic series for the actual service environment.",
            "The anode-to-cathode area ratio for the real joint geometry.",
            "Whether an electrolyte can reach the joint: sealing changes the verdict honestly.",
            "The mitigation chosen and its maintenance: isolation inspected, coatings renewed.",
            "The galvanic cell of the matrix filled with the potential difference as evidence.",
        ],
        "standards": [
            "Galvanic series and dissimilar-metal practice follow MIL-STD-889D.",
            "Marine and outdoor severity follows the environment definitions in the applicable service standard.",
            "Coating and isolation practice follows the fastener and enclosure manufacturer's guidance.",
        ],
        "citations": [CIT_MIL889, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: galvanic corrosion is betrayal inside the "
            "handshake - one metal quietly sacrificing the other. The "
            "Signature Handshake Method refuses pairings that eat their "
            "partners: it measures the potential gap, weighs the areas, "
            "and either separates the metals with honor or chooses closer "
            "kin - because no covenant survives one side consuming the "
            "other."
        ),
    },
    {
        "key": "thermal_expansion",
        "name": "Thermal Expansion Compatibility",
        "group": "Compounded",
        "ladder_rank": 3,
        "ladder_tier": "compounded",
        "description": (
            "Everything grows when heated, but not at the same rate, and "
            "the difference is what breaks joints. Aluminum grows about 23 "
            "parts per million per degree Celsius, steel about 12, copper "
            "17, silicon 2.6, FR-4 circuit board 12 to 16 in-plane, and "
            "epoxy potting compounds 50 to 70. Bolt an aluminum housing to "
            "a steel bracket across a 100-degree swing and the aluminum "
            "tries to grow nearly twice as far as the steel - the bolts "
            "carry the disagreement as shear, cycle after cycle, until "
            "something yields or fatigues. The same physics attacks solder "
            "joints: a large ceramic package (low expansion) on an FR-4 "
            "board (higher expansion) walks its solder joints a few microns "
            "every thermal cycle, and microns times thousands of cycles is "
            "a cracked joint. This record teaches the expansion check: "
            "compute the relative motion, decide whether the joint can "
            "absorb it, and choose the cure - compliance, matching, or "
            "decoupling."
        ),
        "how_it_works": (
            "The check is arithmetic: relative motion equals the "
            "difference in expansion coefficients times the temperature "
            "swing times the constrained length. A 100 mm aluminum-to-steel "
            "joint across 100 C moves (23-12) ppm/C x 100 C x 100 mm = 0.11 "
            "mm - enough to matter for dowels and precision fits. Compare "
            "the motion against what the joint tolerates: slotted holes "
            "and Belleville washers absorb it, rigid dowels do not; "
            "compliant solder and underfill survive it, stiff large-area "
            "bonds crack. The cures: match coefficients (aluminum housing "
            "on aluminum bracket), add compliance (slots, flexible "
            "interposers, soft gaskets), decouple (one fixed mount, the "
            "rest floating), or shrink the constrained length (split long "
            "joints into segments). For electronics, the package-to-board "
            "mismatch sets the solder-joint fatigue life - large, stiff, "
            "low-expansion packages on high-expansion boards in wide "
            "temperature swings are the red cells of thermal cycling."
        ),
        "key_points": [
            "Relative motion = coefficient difference x temperature swing x constrained length - compute it for every rigid joint.",
            "Aluminum on steel across 100 C moves about 0.11 mm per 100 mm of joint: enough to shear dowels and fatigue bolts.",
            "Cures in order: match the coefficients, add compliance, decouple the mounts, shorten the constrained length.",
            "Solder-joint fatigue follows the package-to-board expansion mismatch times the temperature swing.",
            "Slotted holes and spring washers are compatibility devices, not sloppy design.",
        ],
        "requirements": [
            "Expansion coefficients for both materials from a trusted source, at the service temperatures.",
            "The real temperature swing: worst-case hot to worst-case cold, not room to \"warm\".",
            "The constrained length of the joint and what absorbs the motion.",
            "The joint type's motion tolerance: rigid, compliant, or decoupled, stated honestly.",
            "The motion calculation filed with the joint design.",
        ],
        "standards": [
            "Expansion coefficients follow Machinery's Handbook material data.",
            "Thermal cycling severity follows IEC 60068-2-1/2 conditions for the service environment.",
            "Solder-joint fatigue practice follows IPC-A-610 and the package manufacturer's thermal-cycle guidance.",
        ],
        "citations": [CIT_MACHINERY, CIT_IEC60068, CIT_JSTD001],
        "sig_lens": (
            "The Signature read: heat makes every material speak, and "
            "different materials speak at different speeds. The Signature "
            "Handshake Method listens to both: it computes the motion, "
            "gives the joint room to breathe, and never bolts two "
            "expansions together rigidly and calls it strength - true "
            "strength is the joint that moves together and holds."
        ),
    },
    {
        "key": "chemical_env",
        "name": "Chemical and Environmental Compatibility",
        "group": "Compounded",
        "ladder_rank": 3,
        "ladder_tier": "compounded",
        "description": (
            "The service environment is the third partner in every pairing, "
            "and it votes. Chemicals attack materials selectively: "
            "chlorides pit stainless steels, ammonia cracks brass, strong "
            "alkalis dissolve aluminum, solvents swell and crack many "
            "plastics, and UV embrittles polymers left in the sun. "
            "Enclosures carry IP ratings per IEC 60529 - IP65 keeps dust "
            "and jets out, IP67 survives immersion - but the rating is a "
            "pairing verdict between the enclosure, its gaskets, and the "
            "environment, and it dies the day a gasket takes a "
            "compression set or a cable gland is mis-sized. Humidity "
            "writes its own failures: condensation on cold surfaces, "
            "dendrite growth between fine-pitch conductors, corrosion under "
            "conformal coat at pinholes. This record teaches the "
            "environmental pairing check: list what the environment brings, "
            "check every exposed material against it, and prove the "
            "enclosure pairing keeps the rest out."
        ),
        "how_it_works": (
            "The check works as an exposure inventory. List everything the "
            "environment delivers over the product's life: fluids (which "
            "chemicals, what concentration, splash or immersion), gases "
            "and fumes, salt, dust, UV hours, temperature and humidity "
            "extremes, and pressure washing or hose-down if the site does "
            "that. Check each exposed material against chemical resistance "
            "data for those agents - the manufacturer's chart, not memory; "
            "\"stainless\" is not one material and \"chemical resistant\" "
            "is not one property. Check the enclosure rating against the "
            "exposure: IP65 for washdown, IP67 where immersion is "
            "possible, and verify the gaskets and glands are part of the "
            "rated assembly, because an IP67 box with an unrated cable "
            "gland is an IP20 box with ambitions. For humidity, check "
            "condensation risk (cold surfaces in warm humid air) and specify "
            "conformal coat or potting where dendrites or corrosion would "
            "otherwise grow. Re-check after any material substitution - the "
            "environment does not renegotiate."
        ),
        "key_points": [
            "Inventory the environment first: fluids, fumes, salt, dust, UV, humidity extremes, washdown - over the full life.",
            "Check each exposed material against published chemical resistance data for those exact agents.",
            "An enclosure rating is a pairing verdict: box plus gaskets plus glands, or the rating is fiction.",
            "Humidity failures are slow: condensation, dendrites, and under-coat corrosion need prevention, not reaction.",
            "Any material substitution re-opens the environmental check - the environment does not renegotiate.",
        ],
        "requirements": [
            "A written exposure inventory for the service environment and life.",
            "Chemical resistance data for every exposed material against every inventoried agent.",
            "The enclosure's IP rating with the gaskets and glands as part of the rated assembly.",
            "A condensation and humidity plan: coat, pot, seal, or ventilate - chosen, not hoped.",
            "The environmental verdict in the matrix, tied to the inventory revision.",
        ],
        "standards": [
            "Enclosure protection follows IEC 60529 IP codes, tested as the complete assembly.",
            "Chemical resistance follows the material manufacturer's published compatibility charts.",
            "Humidity and condensation severity follow IEC 60068 environmental test conditions.",
        ],
        "citations": [CIT_IEC60529, CIT_IEC60068, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: the environment is the silent third hand "
            "in every handshake, and it never signs the ledger - it simply "
            "acts. The Signature Handshake Method inventories the third "
            "hand honestly, armors every exposed material against it, and "
            "seals the enclosure as one rated assembly - because a "
            "handshake the weather can undo was never sealed."
        ),
    },
    {
        "key": "joining",
        "name": "Solder and Joining Compatibility",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Joining is where two parts become one, and the joint is a "
            "pairing with its own compatibility rules. Soldered joints "
            "pair the solder alloy, the component termination, and the "
            "board finish: SAC305 lead-free solder (melting around 217 to "
            "220 C) wets copper, tin, and nickel-gold finishes well, wets "
            "oxidized surfaces not at all, and dissolves silver-bearing "
            "terminations over time; the old tin-lead eutectic (183 C) is "
            "easier to work but restricted by regulation in most products. "
            "Mixing lead-free solder with leaded terminations makes "
            "unreliable joints; mixing leaded solder into a lead-free "
            "process contaminates the line. Beyond solder: welds pair base "
            "metals and filler by metallurgy (dissimilar welds crack), "
            "adhesives pair by surface energy (low-energy plastics like "
            "polypropylene need treatment or they peel), and press-fits "
            "pair by spring temper and hole tolerance. This record teaches "
            "the joint compatibility check: match the metallurgy, respect "
            "the process window, and never mix alloy families."
        ),
        "how_it_works": (
            "The solder check starts with the alloy family: lead-free "
            "process means SAC alloys throughout - paste, wire, and "
            "component terminations - because lead contamination above "
            "about 0.1 percent changes the joint metallurgy and its "
            "reliability. Check the reflow window: the paste's liquidus "
            "plus superheat must sit below every component's rated peak "
            "temperature and below the board's decomposition point, with "
            "margin for profiler error. Check the finishes: ENIG, "
            "immersion silver, OSP, and HASL each have their solderability "
            "windows and shelf lives - an expired OSP board solders like a "
            "rumor. For welds, check the filler-to-base metallurgy chart "
            "and the heat input against distortion and heat-affected-zone "
            "limits. For adhesives, check surface energy (above about 36 "
            "dynes/cm wets well), surface preparation, and cure "
            "temperature against the adherends' limits. The proof is "
            "destructive on samples: cross-section the joint, look at the "
            "intermetallic layer (thin and continuous is right; thick and "
            "jagged is a future failure), and pull-test to the standard."
        ),
        "key_points": [
            "Never mix solder alloy families: lead-free process means SAC throughout, paste to termination.",
            "The reflow window must clear the paste liquidus and stay under every component's peak rating with margin.",
            "Board finishes have solderability windows and shelf lives - expired OSP is a red cell.",
            "Welds pair by filler-to-base metallurgy; adhesives pair by surface energy and preparation.",
            "Prove joints destructively on samples: cross-section the intermetallic, pull-test to the standard.",
        ],
        "requirements": [
            "The solder alloy family declared for the whole process, and every termination's compatibility with it.",
            "The reflow or wave profile with the window math: liquidus plus superheat versus component peaks.",
            "Board finish type and age, component MSL ratings, and storage conditions.",
            "Filler and adhesive selections with their metallurgy or surface-energy justification.",
            "Sample cross-sections and pull tests filed as the joint evidence.",
        ],
        "standards": [
            "Soldered assembly acceptability follows IPC-A-610H; process requirements follow IPC J-STD-001H.",
            "Lead restrictions follow the applicable regulation (RoHS) for the market.",
            "Welding filler selection follows the applicable AWS filler/base-metal guidance.",
        ],
        "citations": [CIT_JSTD001, CIT_IPC2221],
        "sig_lens": (
            "The Signature read: a joint is a handshake that must never "
            "let go, so the Signature Handshake Method marries only true "
            "metallurgical kin. One alloy family through the whole "
            "process, finishes honored in their season, and every joint "
            "proven by the cross-section's testimony - because a bond "
            "that fails in the field was a promise made to the wrong "
            "metal."
        ),
    },
    {
        "key": "power_supply",
        "name": "Power Supply Interoperability",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Power supplies and their loads form the most consequential "
            "pairing in any system: every other pairing assumes the rails "
            "are honest. Interoperability covers the steady state (voltage "
            "accuracy, load regulation, ripple and noise), the dynamic "
            "state (transient response to load steps, startup sequencing, "
            "monotonic rise), and the fault state (overcurrent behavior - "
            "hiccup, foldback, or latch - and what each does to a system "
            "that must recover by itself). The classic failures are "
            "sequencing (a 3.3 V rail rising before the 1.8 V rail it "
            "references, latching the load), ripple (a switcher's 100 mV "
            "of noise into an ADC that resolves microvolts), and "
            "backfeeding (an unpowered module fed through its I/O "
            "protection diodes by a powered neighbor). Redundant and "
            "paralleled supplies add sharing and OR-ing rules: paralleled "
            "supplies without active sharing fight each other, and OR-ing "
            "diodes or controllers must handle the full fault current. "
            "This record teaches the supply-load handshake in all three "
            "states."
        ),
        "how_it_works": (
            "The handshake is proven in three states. Steady state: the "
            "supply's output tolerance band (setpoint plus load regulation "
            "plus temperature drift) must sit inside every load's input "
            "range, and the ripple-plus-noise peak must sit below the most "
            "sensitive load's PSRR-limited requirement - measure it at the "
            "load's pins, not the supply's terminals. Dynamic state: apply "
            "the worst load step and verify the rail stays inside every "
            "load's window through the transient; verify startup is "
            "monotonic and sequenced per the loads' requirements (core "
            "before I/O, or whatever the datasheets demand). Fault state: "
            "short the output and confirm the protection mode matches the "
            "system's recovery story - hiccup for self-recovery, latch "
            "where a human must intervene. For paralleled or redundant "
            "supplies, verify current sharing within the specified band "
            "and prove the OR-ing path carries a full single-supply fault "
            "without collapsing the bus. Backfeeding gets its own test: "
            "power each module alone and confirm no rail rises through "
            "another module's I/O."
        ),
        "key_points": [
            "Prove three states: steady (tolerance plus ripple at the load's pins), dynamic (load steps, sequencing, monotonic startup), fault (protection mode matches the recovery story).",
            "Sequencing is a pairing rule: rails must rise in the order the loads' datasheets demand.",
            "Ripple is measured at the most sensitive load's pins against its PSRR-limited need.",
            "Paralleled supplies need active sharing; redundant buses need OR-ing proven under a full single-supply fault.",
            "Test backfeeding explicitly: power each module alone and watch every rail.",
        ],
        "requirements": [
            "Every load's input voltage range, ripple sensitivity, sequencing needs, and startup current.",
            "The supply's tolerance band, transient response, sequencing capability, and protection mode.",
            "The worst load step the system can produce, characterized honestly.",
            "OR-ing and sharing designs with their fault-current ratings.",
            "Measured steady, dynamic, and fault records filed as the supply evidence.",
        ],
        "standards": [
            "Board-level power design follows IPC-2221B; current capacity follows IPC-2152.",
            "Sequencing and tolerance follow the load datasheets' power requirements sections.",
            "EMC implications of switchers follow IEC 61000-4 series practice.",
        ],
        "citations": [CIT_IPC2221, CIT_IPC2152, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: the supply is the host of the feast, and "
            "interoperability is the seating covenant - every load fed "
            "within its tolerance, in its proper order, through every "
            "storm of load steps. The Signature Handshake Method proves "
            "the host in all three states, for a table where no guest "
            "goes hungry and no dish arrives before its course is a table "
            "that holds."
        ),
    },
    {
        "key": "grounding",
        "name": "Grounding and Shielding Compatibility",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Ground is the reference every signal is measured against, so "
            "two modules are only compatible if they agree on what ground "
            "is. The disagreements are legendary: ground loops (two "
            "grounds at different potentials driving current through "
            "shields and signal returns), split grounds joined in the "
            "wrong place, shields grounded at both ends on long runs "
            "(inviting loop current) versus one end (inviting antenna "
            "behavior at high frequency), and \"ground\" pins that carry "
            "amps of return current and therefore are not ground at all. "
            "The pairing rules: signal return currents must have a "
            "low-impedance path home that does not share impedance with "
            "other signals' returns; shields terminate to chassis at the "
            "right points for the frequency of interest; and mixed-signal "
            "systems keep noisy digital returns out of quiet analog "
            "references. This record teaches the grounding handshake: one "
            "reference, honest returns, and shields terminated with "
            "intent."
        ),
        "how_it_works": (
            "The handshake starts by drawing the ground system as a "
            "circuit, not a symbol. Identify every ground connection "
            "between the modules: signal returns, shield terminations, "
            "chassis bonds, and power returns. Compute the shared "
            "impedance: return current times shared impedance is the noise "
            "voltage injected into every signal sharing that path - at "
            "high frequency the inductance dominates, so short wide "
            "returns beat long thin ones. Apply the loop test: is there a "
            "closed conductive loop through grounds and shields? If yes, "
            "compute the loop area and the magnetic environment - large "
            "loops in noisy environments are red. Shield termination "
            "follows the frequency rule: below about 1 MHz, single-point "
            "shield grounding avoids low-frequency loops; above it, the "
            "shield must bond at both ends (360-degree bonds, not "
            "pigtails) or it stops being a shield. Mixed-signal pairings "
            "get a star or partitioned return with one defined meeting "
            "point, placed where the datasheets or the system architect "
            "say. Prove it by measurement: ground potential difference "
            "between modules under load, and noise on the quietest signal "
            "with the noisiest aggressor running."
        ),
        "key_points": [
            "Draw grounds as a circuit: every return, shield, chassis bond, and power ground is a branch with impedance.",
            "Shared return impedance converts return current into noise voltage - keep noisy returns out of quiet references.",
            "Shield termination is frequency-dependent: single-point below ~1 MHz, 360-degree both-ends above it, never pigtails at RF.",
            "Closed ground loops are red until proven quiet: compute the loop area and the magnetic environment.",
            "Prove by measurement: ground potential difference under load and quiet-signal noise with aggressors running.",
        ],
        "requirements": [
            "A ground interconnection drawing showing every conductive path between the modules.",
            "Return current magnitudes and the shared impedances they cross.",
            "The frequency range of interest: it decides the shield termination rule.",
            "The mixed-signal partitioning plan with its single meeting point.",
            "Measured ground-difference and noise records as the grounding evidence.",
        ],
        "standards": [
            "Shielding and bonding practice follows IEC 61000 series EMC guidance.",
            "Safety grounding follows the applicable electrical safety standard for the product class.",
            "Measurement follows standard EMC test practice for conducted noise.",
        ],
        "citations": [CIT_IEC61000, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: ground is the common tongue beneath all "
            "signals, and the handshake fails when the two sides speak it "
            "at different potentials. The Signature Handshake Method gives "
            "every current an honest path home, terminates every shield "
            "with intent, and measures the silence it promises - for a "
            "reference that wavers is no reference, and a covenant needs "
            "firm ground."
        ),
    },
    {
        "key": "battery_chem",
        "name": "Battery Chemistry Pairings",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Batteries are pairings with chemistry as the contract: mix "
            "chemistries and the contract is void. The rules are absolute "
            "in series strings: every cell must be the same chemistry, "
            "same capacity, same age, and same state of charge, because "
            "the weakest cell limits the string and the strongest cell "
            "overcharges the weakest on every cycle - the mechanism behind "
            "most pack failures and fires. Lithium-ion (3.6-3.7 V nominal, "
            "4.2 V charge termination) never series-pairs with LiFePO4 "
            "(3.2 V nominal, 3.65 V termination) or NiMH (1.2 V nominal): "
            "the charger terminates at one chemistry's voltage and "
            "destroys the other. Even within one chemistry, old and new "
            "cells in series are a red cell - capacity mismatch walks the "
            "pack into overcharge within dozens of cycles. Chargers are "
            "pairings too: the charger's algorithm (CC/CV voltages, "
            "termination current, temperature cutoffs) must match the "
            "cell's datasheet exactly, and multi-cell packs need balancing "
            "- passive or active - or the series string diverges. This "
            "record teaches the battery pairing laws: one chemistry, "
            "matched cells, matched charger, balancing where series."
        ),
        "how_it_works": (
            "The check starts with chemistry identity: read the cell "
            "datasheet's nominal voltage, charge termination voltage, and "
            "charge algorithm. In a series string, verify all cells share "
            "the chemistry, the rated capacity (within a few percent), "
            "the manufacturer lot or date code, and the measured open-"
            "circuit voltage before assembly (within tens of millivolts) - "
            "any outlier is rejected, not \"balanced out.\" Verify the "
            "charger: its constant-current rate within the cell's rated "
            "maximum, its constant-voltage setpoint at the chemistry's "
            "termination voltage (4.20 V for standard Li-ion, 3.65 V for "
            "LiFePO4), and its termination and safety timers. For series "
            "packs, verify the BMS: per-cell voltage monitoring, balancing "
            "current adequate for the expected mismatch, and temperature "
            "cutoffs. Parallel strings get their own rule: only parallel "
            "cells at equal voltage (within about 0.1 V per cell at "
            "connection, or the inrush current welds things), and fused "
            "or protected per the pack design. The proof is a formation "
            "log: every cell's capacity and internal resistance recorded "
            "before assembly, and the pack cycled with per-cell voltages "
            "logged."
        ),
        "key_points": [
            "Series strings: one chemistry, matched capacity, matched age, matched state of charge - no exceptions.",
            "Mixed chemistries in series are red: the charger terminates at one voltage and destroys the other.",
            "Charger algorithm must match the cell datasheet: CC rate, CV setpoint, termination, temperature cutoffs.",
            "Series packs need per-cell monitoring and balancing; parallel connections need equal voltages at joining.",
            "Proof is a formation log: every cell's capacity and resistance recorded before assembly.",
        ],
        "requirements": [
            "Cell datasheets: chemistry, nominal and termination voltages, charge algorithm, temperature limits.",
            "Per-cell incoming data: open-circuit voltage, and capacity/IR for series packs.",
            "Charger specifications matched line-by-line to the cell requirements.",
            "BMS specifications: monitoring resolution, balancing current, protection thresholds.",
            "The formation and cycling log filed as the pack evidence.",
        ],
        "standards": [
            "Lithium cell safety follows the applicable transport and product safety standards for the market (UN 38.3 for transport).",
            "Charger and BMS behavior follows the cell manufacturer's application guidance.",
            "Pack construction follows good practice for fusing, spacing, and thermal containment.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: a battery pack is a choir, and the "
            "pairing law is that every voice sings the same chemistry in "
            "the same key. The Signature Handshake Method admits no "
            "mismatched singers: matched cells, a charger that knows the "
            "tune, and a balancer keeping every voice true - because one "
            "false note in a lithium choir is sung in fire."
        ),
    },
    {
        "key": "rf_modules",
        "name": "RF Module Interoperability",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Radio modules pair across the air, which makes their "
            "compatibility a meeting of regulations, frequencies, and "
            "protocols rather than wires. Two RF modules interoperate only "
            "when they share the band (a 915 MHz LoRa module never hears a "
            "2.4 GHz one), the modulation and protocol (LoRaWAN versus raw "
            "LoRa versus Zigbee are different languages on possibly the "
            "same band), the regulatory region's power and duty-cycle "
            "limits, and the antenna interface (50-ohm SMA, U.FL, or "
            "chip antenna - each with its mating and placement rules). "
            "Antenna pairing is its own discipline: a 2.4 GHz antenna on a "
            "915 MHz module is a red cell with a 10 dB penalty, and an "
            "antenna pressed against a metal enclosure or a battery is an "
            "antenna in name only. Coexistence is the advanced question: "
            "two radios in one product (Wi-Fi plus Bluetooth, or LTE plus "
            "GNSS) must be checked for desensitization - the transmitter "
            "of one deafening the receiver of the other. This record "
            "teaches the RF handshake: same band, same protocol, legal "
            "power, honest antenna, proven coexistence."
        ),
        "how_it_works": (
            "The handshake is checked in layers. Regulatory: the module's "
            "certification (FCC, CE/RED, and friends) must cover the region "
            "of sale with the intended antenna - swapping to a higher-gain "
            "antenna voids the certification math. Frequency and protocol: "
            "both ends on the same band running the same stack at "
            "compatible settings (spreading factor, bandwidth, network "
            "keys for LoRaWAN; PAN ID and channel for Zigbee). Link "
            "budget: transmitter power plus antenna gains minus path loss "
            "and fade margin must exceed the receiver's sensitivity at the "
            "required range - compute it, then measure it in the real "
            "environment. Antenna: 50-ohm interface matched, antenna tuned "
            "for the band, keep-out zones respected, ground plane adequate "
            "for the antenna type. Coexistence: with two radios active, "
            "measure each receiver's sensitivity while the other transmits "
            "at full power - desensitization beyond the budget is a red "
            "cell cured by filtering, separation, or time-division. The "
            "proof is radiated: conducted numbers lie about antennas, so "
            "the range test happens over the air in the real enclosure."
        ),
        "key_points": [
            "Same band, same protocol, same region's regulations - all three, or the radios never meet.",
            "Certification covers the module WITH its antenna: higher-gain swaps void the math.",
            "Link budget is computed then measured: TX power plus gains minus loss and fade must beat sensitivity.",
            "Antennas need their keep-out and ground plane; metal-adjacent antennas are antennas in name only.",
            "Two radios in one product get a coexistence test: measure sensitivity while the other transmits.",
        ],
        "requirements": [
            "Each module's band, protocol, settings, regulatory certifications, and region list.",
            "Antenna specifications: band tuning, gain, interface, keep-out, and ground-plane needs.",
            "The link budget calculation for the required range and environment.",
            "Coexistence measurements for multi-radio products.",
            "Over-the-air range proof in the real enclosure, filed as the RF evidence.",
        ],
        "standards": [
            "Radio emissions and certification follow the region's regulations (FCC Part 15, EU RED) for the certified configuration.",
            "Antenna interface impedance follows the 50-ohm convention unless the module specifies otherwise.",
            "Coexistence practice follows the module manufacturer's multi-radio guidance.",
        ],
        "citations": [CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: radios shake hands across the empty air, "
            "and the Signature Handshake Method makes the greeting "
            "honest - same band, same tongue, lawful power, and an "
            "antenna given room to speak. No radio is certified alone and "
            "no link is proven on paper: the ledger records the "
            "over-the-air proof, in the real enclosure, at the real "
            "range."
        ),
    },
    {
        "key": "firmware_api",
        "name": "Firmware and API Version Compatibility",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Hardware pairings have a software shadow: the firmware and "
            "API versions on the two sides must agree, or the wires carry "
            "correct signals that mean the wrong things. The discipline "
            "is versioning honesty. Semantic versioning (MAJOR.MINOR.PATCH) "
            "is the contract: patch versions fix bugs without changing "
            "behavior, minor versions add backward-compatible features, "
            "major versions may break - and a major-version mismatch "
            "across a pairing is a red cell until proven otherwise. The "
            "classic failures: a sensor whose register map moved between "
            "firmware revisions, a bootloader that refuses an application "
            "built for a newer API, a host driver that configures a "
            "peripheral the old way while the new firmware expects the "
            "new way, and the silent one - two sides that both \"support "
            "the protocol\" but implement different optional features. "
            "This record teaches the version handshake: declare, check, "
            "negotiate, and fail loudly on mismatch."
        ),
        "how_it_works": (
            "The handshake is a protocol in itself. At connection - "
            "power-up, enumeration, or session start - each side declares "
            "its identity and version: hardware revision, firmware "
            "version, protocol version, in machine-readable registers or "
            "descriptors. Each side checks the other's declaration "
            "against its compatibility table: exact match green, "
            "same-major green, different-major red unless a migration path "
            "is proven. Where the protocol allows, the sides negotiate "
            "down to the highest mutually supported version - USB, "
            "Bluetooth, and most network stacks do this natively; bare-"
            "metal UART links must implement it by hand. On mismatch, the "
            "system must fail LOUDLY: a clear error, a log entry, a red "
            "LED pattern - never silent misbehavior. The build system "
            "enforces the pairing too: firmware images carry version "
            "metadata, the bootloader verifies compatibility before "
            "jumping, and manufacturing flashes matched sets. Keep a "
            "compatibility matrix of firmware pairs exactly like the "
            "hardware one - because a hardware-green pairing with a "
            "firmware-red shadow is red."
        ),
        "key_points": [
            "Semantic versioning is the contract: patch safe, minor additive, major may break - major mismatch is red until proven.",
            "Every connection starts with version declaration: hardware rev, firmware ver, protocol ver, machine-readable.",
            "Negotiate to the highest mutual version where the protocol allows; implement it by hand where it does not.",
            "Mismatch must fail loudly: clear error and log, never silent misbehavior.",
            "The bootloader verifies compatibility before jumping; manufacturing flashes matched sets.",
        ],
        "requirements": [
            "Version declarations from both sides: hardware revision, firmware version, protocol version.",
            "A firmware compatibility matrix: which versions pair with which, dated.",
            "Negotiation or minimum-version logic in the connection code.",
            "Bootloader compatibility verification before application handoff.",
            "Manufacturing records proving matched-set flashing.",
        ],
        "standards": [
            "Versioning follows Semantic Versioning 2.0.0 conventions.",
            "Protocol negotiation follows the protocol's own versioning specification.",
            "Update and rollback behavior follows the product's safety requirements.",
        ],
        "citations": [CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: firmware is the memory of the handshake - "
            "the wires may grip while the minds disagree. The Signature "
            "Handshake Method makes every mind declare itself, checks the "
            "declarations against the ledger, and fails loudly rather "
            "than misunderstand quietly - for a handshake where each side "
            "remembers a different agreement is no agreement."
        ),
    },
    {
        "key": "memory_storage",
        "name": "Memory and Storage Interface Compatibility",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Memory pairings are unforgiving: the wrong DRAM generation or "
            "storage protocol simply does not work, and the failure gives "
            "no partial credit. DRAM generations are physically and "
            "electrically distinct - DDR3 runs at 1.5 V, DDR4 at 1.2 V, "
            "DDR5 at 1.1 V, with different pin counts, keying notches, and "
            "signaling - so a DDR4 module never fits a DDR5 slot, by "
            "design. Within a generation, the controller and the module "
            "must agree on speed grade, timing parameters, and capacity "
            "organization; the SPD EEPROM on the module is the declaration "
            "the BIOS reads to configure the controller. Storage has its "
            "own generations: SD cards (SDSC, SDHC, SDXC) with speed "
            "classes, eMMC generations with incompatible voltage and speed "
            "expectations, NVMe over PCIe with lane-count and generation "
            "negotiation. This record teaches the memory handshake: match "
            "the generation physically, the timing logically, and let the "
            "SPD and negotiation do their jobs."
        ),
        "how_it_works": (
            "The check starts at the slot: the module's generation, pin "
            "count, and keying notch must match the socket - this is "
            "mechanical enforcement of electrical truth, and forcing it is "
            "destruction, not compatibility. Then the electrical: supply "
            "voltage of the generation (1.5/1.2/1.1 V for DDR3/4/5), "
            "VTT and VREF where the standard requires them. Then the "
            "logical: the controller's supported speed grades and timing "
            "tables against the module's SPD data - the BIOS trains the "
            "interface at boot, and training failures are the symptom of "
            "a marginal pairing (wrong termination, too-long traces, "
            "mixed modules). For storage: the host's supported generations "
            "and speed modes against the card's declarations, bus width "
            "(1/4/8-bit) negotiated honestly, and voltage switching (1.8 V "
            "signaling for UHS modes) supported on both sides. Mixed "
            "modules in multi-slot systems: identical part numbers is the "
            "green rule; mixed speeds train down to the slowest only when "
            "the controller genuinely supports it. Prove with training "
            "logs and stress: memory test to the standard, storage "
            "throughput at the negotiated mode."
        ),
        "key_points": [
            "Generations are physically enforced: DDR3/4/5 differ in voltage, pins, and keying - never force a module.",
            "Within a generation, controller speed grades and timings must cover the module's SPD declarations.",
            "Training failures at boot are the symptom of a marginal pairing: termination, trace length, or mixed modules.",
            "Storage: host generations and speed modes must overlap the card's; 1.8 V signaling needs both-side support.",
            "Multi-slot rule: identical part numbers is green; mixed sets train down only where genuinely supported.",
        ],
        "requirements": [
            "Module and socket generation, pin count, keying, and voltage from the standards and datasheets.",
            "Controller-supported speed grades, timings, and capacities.",
            "SPD data for the actual modules in the build.",
            "Storage host and card generation/mode declarations.",
            "Training logs, memory stress results, and storage throughput at the negotiated mode.",
        ],
        "standards": [
            "DDR generations follow JEDEC JESD79 series (DDR5: JESD79-5A) for voltage, signaling, and SPD.",
            "SD interfaces follow the SD Association specifications for the card's class and speed mode.",
            "eMMC follows the JEDEC eMMC standard for the generation in use.",
        ],
        "citations": [CIT_JESD79, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: memory is the handshake's memory - the "
            "pairing that must remember perfectly or not at all. The "
            "Signature Handshake Method seats only true-generation kin, "
            "lets the SPD speak its declaration, trains the interface "
            "honestly at boot, and stress-tests the remembering - for a "
            "memory that misremembers is worse than no memory."
        ),
    },
    {
        "key": "display_camera",
        "name": "Display and Camera Interface Compatibility",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Displays and cameras pair over some of the fastest wires in "
            "a product, and their compatibility is a bandwidth contract. "
            "MIPI DSI (display) and CSI (camera) carry pixels over 1 to 4 "
            "differential lanes, each lane up to gigabits per second; the "
            "pairing must agree on lane count, per-lane rate, and the "
            "protocol version, and the total bandwidth must cover the "
            "resolution times the frame rate times the bits per pixel. A "
            "1080p60 stream at 24 bits needs about 3 Gbps before blanking "
            "overhead - a 2-lane interface cannot carry it no matter how "
            "the software wishes. Parallel RGB and LVDS are the older "
            "tongues with their own clock-and-format agreements; HDMI and "
            "DisplayPort negotiate via EDID and link training. Touch "
            "panels add a second pairing (I2C or SPI plus interrupt and "
            "reset) that must be wired and addressed correctly. This "
            "record teaches the pixel-pipe handshake: compute the "
            "bandwidth, match the lanes, agree the format, and prove it "
            "with a stable image."
        ),
        "how_it_works": (
            "The handshake is arithmetic first. Compute the required "
            "bandwidth: horizontal pixels times vertical lines times frame "
            "rate times bits per pixel, plus blanking overhead (roughly 20 "
            "percent for MIPI). Compare against the interface capacity: "
            "lane count times per-lane rate times the encoding efficiency. "
            "Required must sit below capacity with margin - a pipe at 99 "
            "percent is a yellow cell that flickers in the heat. Then the "
            "format agreement: color format (RGB888, YUV variants), lane "
            "count, and protocol version must match on both ends; the "
            "display's initialization sequence (the vendor's command list) "
            "must be sent exactly, because panels without their init "
            "sequence show nothing and the failure looks like a hardware "
            "fault. Then the physical: lane polarity and order per the "
            "schematic, impedance-controlled routing for the gigabit "
            "lanes, and the touch controller's I2C address, interrupt, "
            "and reset lines. Prove with the image: stable frames at the "
            "target resolution and rate, through temperature, with the "
            "touch reporting accurately."
        ),
        "key_points": [
            "Bandwidth is arithmetic: pixels x lines x fps x bits-per-pixel plus overhead must sit below lane-count x per-lane-rate with margin.",
            "A pipe at 99 percent capacity is a yellow cell: it flickers when hot.",
            "Format must agree exactly: color format, lane count, protocol version - plus the vendor init sequence, sent exactly.",
            "Gigabit lanes need impedance-controlled routing; lane order and polarity per the schematic.",
            "Touch is a second pairing: address, interrupt, reset - wired and proven separately.",
        ],
        "requirements": [
            "Target resolution, frame rate, and color format for the application.",
            "Interface lane count, per-lane rate, and protocol version on both ends.",
            "The panel's or sensor's initialization sequence from the vendor.",
            "Touch controller address, interrupt, and reset assignments.",
            "A stable-image proof: frames at target rate through temperature, touch accuracy logged.",
        ],
        "standards": [
            "MIPI DSI/CSI lane rates and protocol follow the MIPI Alliance specifications for the version in use.",
            "HDMI/DisplayPort negotiation follows the respective interface specifications including EDID and link training.",
            "High-speed routing follows IPC-2221B controlled-impedance practice.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IPC2221],
        "sig_lens": (
            "The Signature read: the pixel pipe is a handshake at a "
            "billion grips per second, and the Signature Handshake Method "
            "counts every one. Bandwidth computed honestly, lanes matched, "
            "formats agreed, init sequences honored exactly - and the "
            "proof is the image itself, stable through heat, for a "
            "handshake you can see is a handshake kept."
        ),
    },
    {
        "key": "sensors",
        "name": "Sensor Module Compatibility",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Sensor modules pair a sensing element with a digital "
            "interface, and their compatibility spans the electrical, the "
            "protocol, and the physical world the sensor actually "
            "measures. The electrical-protocol checks are familiar: "
            "supply voltage within the sensor's range, logic levels "
            "compatible, I2C address unique on the bus (the classic "
            "failure - two identical sensors with fixed addresses), SPI "
            "mode and max clock honored. The sensor-specific checks are "
            "where pairings fail: range (a plus-minus-2g accelerometer "
            "saturates on a vibrating motor mount), bandwidth and output "
            "data rate (sampling must exceed twice the fastest signal of "
            "interest), accuracy and calibration (factory trim versus the "
            "application's need), and the physical coupling - a "
            "temperature sensor measuring its own PCB's heat instead of "
            "the air, a pressure sensor plumbed to a dead leg, an IMU "
            "mounted on a flexing panel. This record teaches the sensor "
            "handshake: interface first, then range, rate, accuracy, and "
            "honest physical coupling."
        ),
        "how_it_works": (
            "The handshake runs in two passes. Pass one, the interface: "
            "supply rails, logic thresholds, bus address uniqueness "
            "(list every I2C address on the bus - fixed-address parts "
            "collide silently), SPI mode and clock, interrupt line "
            "polarity and voltage. Pass two, the measurement: define the "
            "measurand's real range in service and verify the sensor's "
            "full-scale covers it with margin (saturation is a red cell); "
            "verify the output data rate exceeds twice the fastest signal "
            "of interest per Nyquist, with the anti-alias filtering the "
            "datasheet requires; verify accuracy and drift against the "
            "application's error budget across temperature. Then the "
            "coupling audit: trace the physical path from the measured "
            "phenomenon to the sensing element and name every corrupting "
            "influence - self-heating, vibration, EMI, mounting stress. "
            "Prove with a known stimulus: apply a reference input and "
            "log the sensor's reading against it, through the temperature "
            "range, because a sensor that cannot be calibrated against a "
            "known truth is a rumor with a part number."
        ),
        "key_points": [
            "Two passes: interface compatibility first, measurement compatibility second - both must be green.",
            "I2C address collisions are silent: list every address on the bus before declaring the pairing.",
            "Range must cover the service measurand with margin; saturation is a red cell.",
            "Data rate must exceed twice the fastest signal of interest, with the datasheet's filtering.",
            "Audit the physical coupling: the sensor must measure the phenomenon, not its own mounting.",
        ],
        "requirements": [
            "Sensor datasheet: supply, thresholds, address options, SPI mode/clock, range, rate, accuracy, drift.",
            "The bus inventory: every device address, every chip-select.",
            "The application's measurand range, fastest signal, and error budget.",
            "The physical mounting design with corrupting influences named.",
            "A calibration log against a known stimulus, through temperature.",
        ],
        "standards": [
            "I2C addressing and timing follow NXP UM10204.",
            "Accuracy and drift are per the sensor datasheet's test conditions.",
            "Calibration follows the application's measurement quality requirements.",
        ],
        "citations": [CIT_UM10204, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: a sensor is a witness, and the handshake "
            "swears the witness in. The Signature Handshake Method checks "
            "the witness's credentials (interface), its eyesight (range "
            "and rate), and its honesty (coupling and calibration) - for "
            "a system that acts on false testimony was never given true "
            "evidence."
        ),
    },
    {
        "key": "motor_driver",
        "name": "Motor and Driver Compatibility",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Motors and drivers pair as an electromechanical unit: the "
            "driver's electronics must suit the motor's windings, and the "
            "motor's mechanics must suit the load. The electrical checks: "
            "the driver's supply range must cover the motor's rated "
            "voltage, its continuous current rating must cover the "
            "motor's rated current with margin, and its peak rating must "
            "survive the stall current - because every motor stalls "
            "someday, and stall current is typically five to ten times the "
            "rated current. The control checks: brushed DC needs an "
            "H-bridge with adequate PWM frequency; brushless DC needs the "
            "right commutation (sensored or sensorless) and pole count "
            "support; steppers need current-regulated chopping matched to "
            "the winding inductance. The thermal check: the driver's "
            "dissipation at the real duty cycle must stay within its "
            "thermal limits, and the motor's temperature rise under the "
            "real load must stay within its insulation class. This record "
            "teaches the motor-driver handshake: voltage, current, "
            "control, and heat - proven at stall, not just at cruise."
        ),
        "how_it_works": (
            "The handshake starts with the motor's datasheet: rated "
            "voltage, rated current, stall current, winding resistance "
            "and inductance, pole count, and insulation class. The "
            "driver must satisfy four inequalities: supply range covers "
            "rated voltage; continuous current rating exceeds rated "
            "current with at least 25 percent margin; peak rating exceeds "
            "stall current for the stall duration the protection allows; "
            "and the control method matches the motor type (H-bridge for "
            "brushed, six-step or FOC with the right pole count for "
            "brushless, chopper current regulation for steppers). Compute "
            "the driver's dissipation: conduction loss (current squared "
            "times on-resistance, times duty) plus switching loss at the "
            "PWM frequency - then the junction temperature via the "
            "thermal resistance, checked against the limit with margin. "
            "Verify protection behavior at stall: current limit or "
            "thermal shutdown must engage before anything smokes, and the "
            "system must define what happens next. Prove on the bench: "
            "run the real load profile, stall it deliberately, and log "
            "currents and temperatures - the pairing is proven at stall, "
            "because cruise never broke anything."
        ),
        "key_points": [
            "Four inequalities: supply covers voltage, continuous rating covers rated current +25%, peak covers stall, control matches motor type.",
            "Stall current is 5-10x rated: the driver must survive the stall the motor will someday see.",
            "Compute driver dissipation at the real duty cycle and check junction temperature with margin.",
            "Protection must engage before smoke: define the stall behavior, not just the cruise behavior.",
            "Prove at stall on the bench: log currents and temperatures under the real load profile.",
        ],
        "requirements": [
            "Motor datasheet: voltage, rated/stall current, winding R and L, pole count, insulation class.",
            "Driver datasheet: supply range, continuous/peak current, Rds(on), control modes, protection behavior.",
            "The real load profile: torque, speed, duty cycle, and stall scenarios.",
            "Thermal path data: Rth values and the actual heatsinking.",
            "Bench logs: currents and temperatures at cruise and at deliberate stall.",
        ],
        "standards": [
            "Motor ratings follow the manufacturer's datasheet test conditions.",
            "Driver thermal ratings follow the datasheet's Rth specifications with the application's cooling.",
            "Insulation classes follow standard motor practice (e.g., Class B 130 C, Class F 155 C).",
        ],
        "citations": [CIT_HOROWITZ, CIT_MACHINERY],
        "sig_lens": (
            "The Signature read: the motor is the muscle and the driver "
            "the nerve - the handshake joins strength to command. The "
            "Signature Handshake Method proves the nerve can bear the "
            "muscle's full fury at stall, keeps the heat within the "
            "covenant, and defines what mercy looks like when the load "
            "refuses to move - for power without protection is not "
            "strength, it is an accident waiting for a shaft."
        ),
    },
    {
        "key": "networks",
        "name": "Network Stack and Middleware Compatibility",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Above the wires, devices pair through network stacks and "
            "middleware, and the compatibility questions move up the "
            "layers. The physical and link layers must still agree "
            "(Ethernet speed and duplex, Wi-Fi band and security mode), "
            "but the new questions are addressing (static versus DHCP, "
            "and what happens when two devices claim one address), "
            "protocols (MQTT, CoAP, HTTP, Modbus/TCP - both ends must "
            "speak the same application tongue), data formats (JSON "
            "schemas, byte orders, units - a temperature in Fahrenheit "
            "read as Celsius is a pairing failure with no electrical "
            "symptom), and security (TLS versions, cipher suites, "
            "certificate chains - a device that only speaks TLS 1.0 is "
            "red against a server that requires 1.2). Time is a pairing "
            "too: devices that timestamp data need synchronized clocks "
            "(NTP or PTP), or the logs disagree about what happened "
            "first. This record teaches the stack handshake: layer by "
            "layer, with the data format and the clock in the contract."
        ),
        "how_it_works": (
            "The handshake walks the stack from the bottom. Physical/link: "
            "speed, duplex, band, and security mode overlap on both ends. "
            "Network: addressing plan - DHCP with reservations or static "
            "with a registry, duplicate-address detection enabled, and the "
            "subnet and gateway actually routing between the devices. "
            "Transport/application: the same protocol, with versions that "
            "overlap, and the broker or server both ends expect (an MQTT "
            "device with no reachable broker is a red cell). Data: a "
            "written schema - field names, types, units, byte order - "
            "versioned like firmware, because \"temperature\" without "
            "units is not data. Security: overlapping TLS versions and "
            "cipher suites, valid certificate chains with synchronized "
            "clocks (certificates fail on wrong time), and credential "
            "provisioning that survives manufacturing. Time: NTP or PTP "
            "configured and verified, with the accuracy the application "
            "needs. Prove end to end: send the real messages through the "
            "real network, verify the schema validates, the units are "
            "right, and the timestamps agree."
        ),
        "key_points": [
            "Walk the stack bottom-up: link, addressing, protocol, data schema, security, time - every layer gets a verdict.",
            "Data without units is not data: schema, types, units, and byte order are in the contract, versioned.",
            "TLS compatibility needs overlapping versions and ciphers - and clocks right, or certificates fail.",
            "Addressing is a pairing: DHCP reservations or a static registry, with duplicate detection on.",
            "Prove end to end with real messages: schema validates, units correct, timestamps agree.",
        ],
        "requirements": [
            "Both ends' supported link modes, protocols, versions, and security capabilities.",
            "The addressing plan: DHCP or static, registry, and duplicate detection.",
            "The written, versioned data schema with units and byte order.",
            "TLS versions, cipher suites, certificate chains, and time sync design.",
            "End-to-end message proof through the real network with schema validation.",
        ],
        "standards": [
            "Ethernet follows IEEE 802.3; Wi-Fi modes follow the IEEE 802.11 amendments in use.",
            "TLS versions and cipher suites follow current IETF practice; deprecated versions are red.",
            "Time sync follows NTP or IEEE 1588 PTP as the accuracy requires.",
        ],
        "citations": [CIT_IEEE802],
        "sig_lens": (
            "The Signature read: the network is a hall of many handshakes "
            "at once, and the Signature Handshake Method introduces every "
            "layer properly - link to link, address to address, schema to "
            "schema, clock to clock. No layer assumes the others: each is "
            "greeted, each is verified, and the ledger records the whole "
            "stack, for a conversation is only as honest as its least "
            "examined layer."
        ),
    },
    {
        "key": "emc",
        "name": "EMC Compatibility Between Modules",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Electromagnetic compatibility is the pairing of every module "
            "with every other module through the air and the wires: no "
            "module may emit enough noise to break another, and every "
            "module must survive the noise the system honestly produces. "
            "The two directions have names: emissions (what a module "
            "radiates and conducts) and immunity (what it tolerates). The "
            "pairing analysis pairs each module's emissions profile "
            "against every other module's immunity profile, across the "
            "frequency range the standards care about. The classic "
            "failures: a switch-mode supply's harmonics landing in a "
            "radio's receive band, a motor driver's fast edges coupling "
            "into an adjacent analog front end, ESD from a human finger "
            "resetting a processor through an unprotected connector "
            "(IEC 61000-4-2 tests 8 kV contact, 15 kV air for a reason). "
            "Mitigation is layered: quiet layout, filtering at the "
            "interfaces, shielding where needed, and ESD protection on "
            "every exposed pin. This record teaches the EMC handshake: "
            "budget the noise, harden the victims, and test the pair, "
            "not just the parts."
        ),
        "how_it_works": (
            "The handshake builds a noise budget. List every noise source "
            "with its spectrum: switchers (fundamental plus harmonics), "
            "clocks and their edges, motors and relays (broadband "
            "transients), radios (intentional, high power). List every "
            "victim with its sensitivity: radio receive thresholds, ADC "
            "resolution floors, digital input thresholds versus coupled "
            "noise. For each source-victim pair, estimate the coupling "
            "path - conducted through shared supplies and grounds, "
            "radiated through the air and apertures, crosstalk between "
            "adjacent wiring - and compute the margin between the coupled "
            "noise and the victim's tolerance. Negative margin is a red "
            "cell; small positive margin is yellow. Apply mitigation in "
            "cost order: separation and layout first (free), filtering at "
            "module interfaces second (ferrites, pi filters on supplies; "
            "common-mode chokes on data), shielding third (with 360-degree "
            "seams, because a shield with slots is a sieve), ESD "
            "protection on every user-touchable pin always. Prove by "
            "test: pre-compliance scans of emissions, immunity testing "
            "with the real aggressors running, and ESD gun testing on the "
            "finished enclosure - the pair is proven together, because "
            "parts that pass alone routinely fail together."
        ),
        "key_points": [
            "EMC is a pairing: every source's emissions against every victim's immunity, across the full frequency range.",
            "Budget the noise per source-victim pair with the coupling path named: conducted, radiated, or crosstalk.",
            "Mitigation in cost order: layout and separation, interface filtering, shielding with honest seams, ESD protection always.",
            "A shield with slots is a sieve: 360-degree bonds, no pigtails, apertures smaller than the wavelength of concern.",
            "Prove the pair together: pre-compliance scans, immunity with aggressors running, ESD on the finished box.",
        ],
        "requirements": [
            "Emissions profiles for every noise source: spectrum, levels, and duty.",
            "Immunity thresholds for every victim: what breaks it and at what level.",
            "The coupling-path analysis for each source-victim pair with margin computed.",
            "The mitigation design: layout rules, filters, shields, ESD devices - placed, not wished.",
            "Pre-compliance and immunity test records on the assembled system.",
        ],
        "standards": [
            "ESD immunity follows IEC 61000-4-2 (8 kV contact, 15 kV air for severe environments).",
            "Emissions and immunity limits follow the product's applicable EMC standard for its market and class.",
            "Filtering and shielding practice follows IEC 61000 series guidance.",
        ],
        "citations": [CIT_IEC61000, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: every module speaks, and some shout - "
            "the EMC handshake teaches the system manners. The Signature "
            "Handshake Method budgets every shout against every ear, "
            "quiets the loud with layout and filtering, armors the "
            "tender with shields and ESD guards, and tests the whole "
            "choir together - for politeness between modules is not "
            "optional, it is the covenant of coexistence."
        ),
    },
    {
        "key": "timing",
        "name": "Timing Closure Across Interfaces",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "At speed, a pairing is a race between the signal and the "
            "clock, and timing closure is the proof the signal always "
            "wins honestly. Every synchronous interface - SPI at tens of "
            "megahertz, parallel buses, DDR memory - demands that data be "
            "stable for a setup time before the clock edge and held for a "
            "hold time after it. The pairing analysis adds the delays: "
            "the driver's clock-to-output, the trace flight time, skew "
            "between data and clock traces, and the receiver's setup and "
            "hold requirements - and checks that the data eye stays open "
            "at the receiver across temperature and voltage. The classic "
            "failures: a faster clock shrinking the bit period below the "
            "sum of the delays, long traces adding flight time the budget "
            "never included, and clock-data skew from unmatched routing. "
            "Source-synchronous interfaces (clock traveling with data, as "
            "in SPI and DDR) ease the math but still demand skew control. "
            "This record teaches the timing handshake: budget every "
            "nanosecond, control the skew, and prove the eye is open."
        ),
        "how_it_works": (
            "The handshake is a budget table in time. For the interface's "
            "clock period, subtract every uncertainty: driver "
            "clock-to-output maximum, receiver setup time, clock jitter, "
            "power-supply-induced jitter, and a margin reserve (10 percent "
            "of the period is the honest minimum). What remains is the "
            "allowance for trace flight time and skew - divide by the "
            "propagation speed (about 150-180 ps per inch on FR-4) to get "
            "the length budget, then route data and clock with matched "
            "lengths inside a fraction of that budget. Hold time gets its "
            "own check with minimum delays: driver clock-to-output "
            "minimum plus trace minimum must exceed receiver hold plus "
            "skew - hold failures cannot be fixed by slowing the clock, "
            "only by adding delay or fixing skew. For source-synchronous "
            "links, budget the skew between clock and data against the "
            "receiver's setup/hold window directly. Prove with "
            "measurement: probe at the receiver's pins (not the driver's), "
            "capture the eye across temperature extremes, and confirm "
            "setup and hold margins - the timing report is the evidence "
            "the cell files."
        ),
        "key_points": [
            "Budget every nanosecond: driver delays, receiver setup/hold, jitter, and a 10-percent margin reserve come off the period first.",
            "Trace length budget is what remains divided by ~150-180 ps/inch; route clock and data matched inside it.",
            "Hold failures cannot be fixed by slowing the clock - only by delay or skew correction.",
            "Source-synchronous links budget clock-to-data skew directly against the receiver's window.",
            "Prove at the receiver's pins, across temperature: the eye diagram is the timing evidence.",
        ],
        "requirements": [
            "Driver clock-to-output (min/max), receiver setup/hold, and clock jitter specifications.",
            "Trace lengths, propagation speed for the stackup, and the skew budget.",
            "The timing budget table with every term named and margined.",
            "Routing constraints issued to layout: matched lengths, the skew limit.",
            "Measured eye diagrams at the receiver across temperature extremes.",
        ],
        "standards": [
            "Timing parameters follow the interface standard and the datasheets' test conditions.",
            "High-speed routing follows IPC-2221B controlled-impedance and skew practice.",
            "Measurement follows the interface standard's compliance methods.",
        ],
        "citations": [CIT_HOROWITZ, CIT_IPC2221, CIT_JESD79],
        "sig_lens": (
            "The Signature read: timing is the rhythm of the handshake - "
            "data must arrive neither early nor late, but exactly on the "
            "beat. The Signature Handshake Method counts every nanosecond "
            "as a covenant term, matches the dancers' steps in copper, "
            "and proves the rhythm at the receiver's own pins - for a "
            "handshake off the beat is a stumble, and stumbles at speed "
            "are failures."
        ),
    },
    {
        "key": "derating_pair",
        "name": "Derating and Reliability of Pairings",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A pairing that works at its ratings on day one can still be "
            "a red cell: ratings are survival limits, and long life "
            "demands derating - operating well inside them. The practice "
            "is old and quantitative: run capacitors at 60-70 percent of "
            "rated voltage, semiconductors with junction temperatures 25 "
            "degrees or more below their maximum, resistors at half their "
            "power rating, because stress accelerates every failure "
            "mechanism exponentially. Pairings multiply the question: two "
            "parts in series share one reliability - the pair's failure "
            "rate is the sum of the parts' rates, so a pairing is only as "
            "reliable as its weakest member, and redundancy math only "
            "helps where it truly exists. This record teaches the "
            "derating handshake: stress ratios for the pair, temperature "
            "honesty, and the reliability arithmetic that turns two "
            "datasheets into one lifetime promise."
        ),
        "how_it_works": (
            "The handshake computes stress ratios for the pairing's "
            "critical parts: applied voltage over rated voltage, applied "
            "power over rated power, operating junction temperature "
            "versus maximum. Each ratio gets a derating limit from the "
            "project's policy (typical: 0.6-0.7 for voltage on "
            "capacitors, 0.5 for resistor power, Tj at least 25 C below "
            "max for semiconductors) - ratios above the limit are yellow "
            "or red regardless of the datasheet's blessing. Temperature "
            "is computed, not assumed: ambient plus each part's "
            "dissipation times its thermal resistance, with the pairing's "
            "mutual heating included (a hot neighbor raises your "
            "ambient). Then the reliability arithmetic: for parts in "
            "series (all must work), failure rates add - pull base rates "
            "from MIL-HDBK-217F or the manufacturer's data, adjust for "
            "the derated stress and temperature, and sum. The pair's MTBF "
            "is the reciprocal of the summed rate. If the result misses "
            "the requirement, the levers are derating (cooler, gentler), "
            "better parts, or true redundancy - never optimism."
        ),
        "key_points": [
            "Derating is the price of long life: 60-70% voltage on capacitors, 50% power on resistors, Tj 25 C below max.",
            "Stress ratios above the project's derating limits are yellow or red even when the datasheet allows them.",
            "Temperature is computed with mutual heating: a hot neighbor raises your ambient.",
            "Series pairings add failure rates: the pair's MTBF is the reciprocal of the summed rate.",
            "Miss the MTBF target with derating, better parts, or true redundancy - never with optimism.",
        ],
        "requirements": [
            "The project's derating policy: the stress-ratio limits for each part family.",
            "Applied stresses for the pairing's critical parts: voltage, current, power, temperature.",
            "Thermal resistances and the mutual-heating analysis.",
            "Base failure rates and the derated, temperature-adjusted pair MTBF calculation.",
            "The reliability calculation filed with the derating evidence.",
        ],
        "standards": [
            "Reliability prediction follows MIL-HDBK-217F Notice 2 methods with stated quality and environment factors.",
            "Derating limits follow the project's policy, guided by industry derating practice.",
            "Temperature measurement follows standard thermal test practice.",
        ],
        "citations": [CIT_MIL217, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: derating is the honor margin - the "
            "Signature Handshake Method never spends a part's whole "
            "strength on an ordinary day. It runs cool, runs gentle, and "
            "counts the pair's lifetime honestly, adding failure rates "
            "where series demands it - for a covenant measured in years "
            "is kept in margins, not in maxima."
        ),
    },
    {
        "key": "substitution",
        "name": "Cross-Reference Substitution Matrices",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Every part eventually goes away - discontinued, "
            "unobtainable, or priced into absurdity - and the "
            "cross-reference matrix is the pre-computed answer to \"what "
            "can replace it.\" A substitution matrix crosses the "
            "approved parts (rows) against candidate substitutes "
            "(columns), and each cell holds the verdict: drop-in "
            "(identical fit, form, function - rare and precious), "
            "conditional (works with stated changes: a different pinout "
            "adapter, a firmware tweak, a derating note), or rejected "
            "(with the reason, so nobody re-auditions it). The analysis "
            "is the full pairing drill against the original's datasheet: "
            "every critical parameter of the original becomes a row in "
            "the comparison, and the substitute must meet or beat each "
            "one under the same conditions. The traps are the silent "
            "parameters: ESD ratings, latch-up immunity, startup "
            "behavior, and second-source parts whose \"equivalent\" "
            "differs in exactly the parameter your circuit leans on. "
            "This record teaches the substitution handshake: qualify "
            "before you need it, document the conditions, and re-verify "
            "on every lot change."
        ),
        "how_it_works": (
            "The matrix is built per critical part, before the shortage. "
            "Extract the original's critical parameters: the ones the "
            "circuit actually depends on, with their test conditions - "
            "not the whole datasheet, the load-bearing dozen. For each "
            "candidate substitute, fill the comparison column: parameter "
            "by parameter, with conditions in view. Drop-in requires "
            "every critical parameter met or beaten, same package and "
            "pinout, same or better ratings - and even drop-ins get a "
            "bench verification, because datasheets have errata. "
            "Conditional substitutes get their conditions written into "
            "the cell: \"requires R7 changed to 4.7k,\" \"firmware v2.3 "
            "or later,\" \"derate to 80% current.\" Rejected candidates "
            "get the killing parameter named, so the next engineer does "
            "not repeat the analysis. Maintain the matrix as a living "
            "document: re-verify on manufacturer PCNs (process change "
            "notices), on lot changes for critical parts, and on any "
            "datasheet revision - a substitute qualified in 2021 against "
            "a 2021 datasheet is not qualified against the 2025 "
            "revision until re-checked."
        ),
        "key_points": [
            "Build the substitution matrix before the shortage: rows are critical parameters, columns are candidates.",
            "Drop-in means every load-bearing parameter met or beaten, same package and pinout - and still bench-verified.",
            "Conditional cells carry their conditions in writing: resistor changes, firmware minima, derating notes.",
            "Rejected candidates get the killing parameter named so the analysis is never repeated blind.",
            "Re-verify on PCNs, lot changes, and datasheet revisions: a 2021 qualification is not a 2025 qualification.",
        ],
        "requirements": [
            "The original part's load-bearing parameters with test conditions - the dozen the circuit depends on.",
            "Candidate datasheets, current revisions, compared parameter by parameter.",
            "Written conditions for every conditional substitute.",
            "Bench verification records for drop-ins and conditionals alike.",
            "A living-document discipline: PCN watch, lot-change re-verification, revision tracking.",
        ],
        "standards": [
            "Comparison follows the datasheets' test conditions per MIL-STD-202 conventions.",
            "Acceptance follows IPC-A-610 for assemblies; process changes tracked per manufacturer PCN practice.",
            "Counterfeit avoidance follows SAE AS5553-style vigilance for substituted sources.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MIL202],
        "sig_lens": (
            "The Signature read: substitution is the understudy's "
            "audition, and the matrix is the casting ledger. The "
            "Signature Handshake Method auditions understudies before "
            "the star falls ill: every load-bearing parameter tested, "
            "conditions written into the role, rejections explained - "
            "for a production line is a stage that cannot go dark, and "
            "the show is kept by preparation, not by panic."
        ),
    },
    {
        "key": "system_integration",
        "name": "Full System Integration Matrices",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Pairwise matrices judge couples; the system integration "
            "matrix judges the whole family at once. A product with "
            "twenty modules has one hundred ninety pairings, and the "
            "failures hide in the interactions no pair analysis sees: "
            "three modules sharing one supply rail whose combined "
            "transients collapse it, two radios desensitizing each other "
            "only when a third module's processor wakes, a ground loop "
            "that closes only through the chassis neither module's "
            "drawing shows. The integration matrix crosses every module "
            "against every other module AND against the shared resources: "
            "power rails, ground system, thermal environment, enclosure, "
            "and the human operator. Each cell holds the pair verdict; "
            "the shared-resource rows hold the summed demands against "
            "the resource's capacity. This record teaches the integration "
            "handshake: assemble the pair verdicts, sum the shared loads, "
            "hunt the three-body interactions, and prove the system as a "
            "system."
        ),
        "how_it_works": (
            "The matrix is built bottom-up. First, every module pair gets "
            "its pairing verdict from the pair records - the integration "
            "matrix references them, never redoes them. Second, the shared "
            "resources get their rows: each power rail sums every "
            "module's average and peak current against the supply's "
            "ratings; the thermal row sums every module's dissipation "
            "against the enclosure's cooling; the ground row maps every "
            "return; the EMC row maps every aggressor against every "
            "victim. Third, the three-body hunt: for each shared "
            "resource, ask what happens at the worst combination - all "
            "radios transmitting while the motors stall and the processor "
            "turbos - because systems fail at the corners, not the "
            "averages. Fourth, the bring-up order: modules integrate in "
            "dependency order (power, then clocking, then comms, then "
            "application), and each stage is proven before the next "
            "joins. The proof is system-level: the full assembly run "
            "through its worst-case profile - thermal, vibration, EMC, "
            "and functional - with every module's telemetry logged, "
            "because the integration verdict belongs to the system, not "
            "to any pair."
        ),
        "key_points": [
            "Pair verdicts are referenced, not redone; shared resources get their own rows with summed demands versus capacity.",
            "Hunt three-body interactions: the worst combination of loads, radios, and thermals - systems fail at corners.",
            "Bring up in dependency order: power, clocking, comms, application - each stage proven before the next joins.",
            "The enclosure, the operator, and the environment are modules too: they get rows in the matrix.",
            "The integration verdict belongs to the system: full-assembly worst-case profiling with all telemetry logged.",
        ],
        "requirements": [
            "The complete module list with revisions and firmware versions.",
            "Every pair verdict from the pair records, referenced by cell.",
            "Shared-resource budgets: power, thermal, ground, EMC, mechanical, operator.",
            "The worst-combination analysis for each shared resource.",
            "System-level worst-case test records with full telemetry.",
        ],
        "standards": [
            "Power and thermal budgets follow IPC-2221B/IPC-2152 practice with measured validation.",
            "EMC follows the product's applicable standard, tested on the full assembly.",
            "Environmental testing follows IEC 60068 conditions for the service environment.",
        ],
        "citations": [CIT_IPC2221, CIT_IEC60068, CIT_IEC61000],
        "sig_lens": (
            "The Signature read: the system is the great handshake - "
            "every module greeting every other at once, and the "
            "integration matrix is the seating of the whole hall. The "
            "Signature Handshake Method seats the pairs, sums the shared "
            "tables, watches the corners where three guests collide, and "
            "proves the feast as one - for a system is not a pile of "
            "green cells, it is a single covenant kept together."
        ),
    },
    {
        "key": "verification",
        "name": "Compatibility Testing and Verification",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Analysis predicts; testing proves. Compatibility "
            "verification is the planned program of tests that turns "
            "matrix verdicts from engineering judgment into evidence: "
            "each yellow and green cell that matters gets a test, each "
            "test has pass criteria written before it runs, and the "
            "results go back into the matrix as the cell's proof. The "
            "test pyramid for pairings runs from the bench (multimeter "
            "and scope: levels, margins, timing at the pins) through the "
            "chamber (temperature, humidity, vibration: the service "
            "environment, accelerated honestly) to the system (full "
            "assembly through its worst-case profile). The disciplines "
            "that matter: test the pairing, not the parts (a part that "
            "passes alone and fails paired is the normal case, not the "
            "exception); test at the corners (hot, cold, low line, high "
            "line, worst load); and test the conditional cells hardest, "
            "because yellow is where the field failures live. This record "
            "teaches the verification handshake: plan the proof, run it "
            "at the corners, and file the results where the verdict "
            "lives."
        ),
        "how_it_works": (
            "The program starts from the matrix: every cell rated yellow "
            "or green-critical gets a verification row - the test method, "
            "the equipment, the pass criteria, and the corner conditions. "
            "Bench tests prove the electrical pairings: logic margins "
            "measured at temperature extremes, timing eyes at the "
            "receiver, power-rail transients under worst load steps, "
            "protocol exchanges with error injection. Chamber tests prove "
            "the environmental pairings: thermal cycling for expansion "
            "and solder fatigue, humidity for corrosion and dendrites, "
            "vibration for connectors and mounts - with the pairing "
            "powered and monitored, because unpowered survivors tell you "
            "nothing. System tests prove the integration: the full "
            "assembly through its mission profile while every interface "
            "is exercised and logged. Every test is run at corners, not "
            "nominals: hot plus low-line plus max load is one corner, "
            "cold plus high-line plus min load another. Failures feed "
            "back correctly: a failed verification demotes the cell to "
            "red and reopens the analysis - the matrix is never edited to "
            "match a wish. Sample sizes follow the risk: safety-critical "
            "pairings get statistical samples, not one golden unit."
        ),
        "key_points": [
            "Every yellow and green-critical cell gets a verification row: method, equipment, pass criteria, corners - written before running.",
            "Test the pairing, not the parts: paired failures of individually-passing parts are the normal case.",
            "Corners, not nominals: hot/low-line/max-load and cold/high-line/min-load are the honest test points.",
            "Conditional cells get the hardest tests: yellow is where field failures live.",
            "Failed verification demotes the cell to red and reopens the analysis - never edit the matrix to match a wish.",
        ],
        "requirements": [
            "The verification plan traced to matrix cells: every important verdict has its proof row.",
            "Pass criteria written before the test runs, with the corner conditions named.",
            "Bench, chamber, and system coverage per the pairing's risk.",
            "Sample sizes matched to risk: statistical samples for safety-critical pairings.",
            "Results filed in the matrix cells as the verdicts' evidence, failures included.",
        ],
        "standards": [
            "Electrical test methods follow the interface standards and MIL-STD-202 conventions.",
            "Environmental tests follow IEC 60068 conditions for the service environment.",
            "EMC verification follows IEC 61000 series practice on the assembly.",
        ],
        "citations": [CIT_MIL202, CIT_IEC60068, CIT_IEC61000],
        "sig_lens": (
            "The Signature read: verification is the handshake witnessed "
            "under oath - the Signature Handshake Method swears every "
            "important verdict in the chamber and at the corners, writes "
            "the pass criteria before the trial, and honors a failure as "
            "honestly as a pass. For a covenant proven only at nominal "
            "is a covenant unproven, and the ledger records evidence, "
            "not wishes."
        ),
    },
    {
        "key": "obsolescence",
        "name": "Lifecycle and Obsolescence in Pairings",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pairings age, and the matrix must age with them. Components "
            "go end-of-life on the manufacturer's schedule, not yours; "
            "datasheets get revised and parameters shift; firmware moves "
            "on while hardware stands still; and a pairing that was green "
            "in 2021 can be yellow in 2025 because one side's process "
            "changed under a PCN you never read. Lifecycle management "
            "treats the pairing as the unit of obsolescence: when either "
            "side of a green cell goes EOL, the cell goes yellow until a "
            "substitute is qualified, and the substitution matrix from "
            "the earlier record is the pre-computed escape route. The "
            "disciplines: monitor PCNs and EOL notices for every part in "
            "every critical pairing; design with second sources qualified "
            "from the start; prefer parts with long lifecycle commitments "
            "(industrial and automotive grades outlive consumer ones); and "
            "keep the matrix revisioned so a 2021 verdict is never "
            "mistaken for a current one. This record teaches the "
            "lifecycle handshake: watch both sides, keep escapes warm, "
            "and never let a verdict outlive its evidence."
        ),
        "how_it_works": (
            "The practice is a watch list and a rhythm. The watch list "
            "names every part in every critical pairing with its lifecycle "
            "status: active, mature, EOL-announced (with last-buy date), "
            "obsolete. PCN and EOL feeds are monitored - distributor "
            "alerts, manufacturer notifications - and every notice "
            "triggers a pairing review: does the change touch a "
            "load-bearing parameter, and does the cell stay green. The "
            "rhythm is the periodic re-verification: critical pairings "
            "re-checked against current datasheet revisions on a schedule "
            "(yearly is the honest default), with the matrix revision "
            "bumped and the evidence refreshed. Design rules reduce the "
            "pain: qualify second sources during development, not during "
            "the shortage; choose packages and interfaces with broad "
            "multi-vendor support; isolate single-source risk behind "
            "abstraction (a module boundary beats a part-number "
            "dependency). Last-buy math is part of the handshake: when "
            "EOL is announced, compute the lifetime need plus spares plus "
            "scrap, buy once, and store honestly - because the second "
            "shortage is always worse than the first."
        ),
        "key_points": [
            "The pairing is the unit of obsolescence: EOL on either side turns the cell yellow until a substitute qualifies.",
            "Monitor PCNs and EOL notices for every part in every critical pairing; every notice triggers a review.",
            "Re-verify critical pairings against current datasheet revisions yearly; bump the matrix revision.",
            "Qualify second sources during development; prefer long-lifecycle grades; isolate single-source risk at module boundaries.",
            "Last-buy math: lifetime need plus spares plus scrap, bought once and stored honestly.",
        ],
        "requirements": [
            "The watch list: every critical-pairing part with lifecycle status and last-buy dates.",
            "PCN/EOL monitoring with a named owner and a review trigger.",
            "The re-verification schedule and the matrix revision history.",
            "Qualified second sources for critical parts, proven before need.",
            "Last-buy calculations and storage records where EOL has struck.",
        ],
        "standards": [
            "PCN practice follows the manufacturer's notification standards (JEDEC JESD46 for semiconductor changes).",
            "Storage of last-buy inventory follows the parts' MSL and shelf-life requirements.",
            "Counterfeit avoidance for broker-sourced EOL parts follows SAE AS5553-style vigilance.",
        ],
        "citations": [CIT_JESD22, CIT_HOROWITZ],
        "sig_lens": (
            "The Signature read: time is the uninvited partner in every "
            "handshake, and the Signature Handshake Method watches it. "
            "It keeps the watch list, reads every notice, re-verifies on "
            "the rhythm, and keeps escapes warm - for a covenant that "
            "assumes the world stands still is a covenant with an expiry "
            "it never read."
        ),
    },
    {
        "key": "build_matrix",
        "name": "Building Your Own Compatibility Matrix",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The final record is the method itself: how to build a "
            "compatibility matrix for your own system, from blank page to "
            "living document. Start with the pairing inventory: list every "
            "part, module, material, and interface in the system, and cross "
            "the families that actually meet - not every theoretical pair, "
            "the real mating surfaces, the real connectors, the real "
            "protocols, the real shared resources. For each cell, run the "
            "pairing drill from the records of this database: the "
            "five-dimension sweep, the deep analyses where triage flags "
            "them, the verdict with its proof numbers and date. Publish "
            "the matrix where the team works - the wall, the wiki, the "
            "design file - in the three colors, with yellow cells carrying "
            "their limits and every cell carrying its evidence. Then keep "
            "it alive: new parts get cells before they get designed in, "
            "PCNs and EOLs trigger reviews, verifications file back into "
            "cells, and the revision history shows the matrix learning. A "
            "finished matrix is never finished - it is the system's memory "
            "of every handshake it has judged, and the next project's "
            "starting point."
        ),
        "how_it_works": (
            "Build it in five passes. Pass one, inventory: enumerate the "
            "system's parts, modules, materials, interfaces, and shared "
            "resources; define the row and column families from what "
            "actually mates. Pass two, triage: run the five-dimension "
            "sweep on each cell at survey depth - most cells go green or "
            "red in an hour; the yellows earn deep analysis. Pass three, "
            "depth: work the yellow cells with the deep records - "
            "galvanic, thermal, timing, EMC, derating - until each has a "
            "verdict with proof numbers. Pass four, publish: the matrix "
            "in three colors where the team cannot miss it, every yellow "
            "with its limits, every cell with its evidence and date, the "
            "revision at the top. Pass five, sustain: gate every new part "
            "introduction on its matrix cells, review on PCN/EOL/ "
            "datasheet revision, file verification results back, and audit "
            "the matrix yearly against the as-built system. The measure "
            "of the matrix is reuse: when the next project starts from "
            "your cells instead of from zero, the method has paid for "
            "itself - which is exactly how this database was built."
        ),
        "key_points": [
            "Five passes: inventory the real matings, triage with the five-dimension sweep, work the yellows deep, publish in three colors, sustain forever.",
            "Cross what actually mates: real surfaces, real connectors, real protocols - not theoretical pairs.",
            "Publish where the team cannot miss it: every yellow with limits, every cell with evidence and date.",
            "Gate new parts on their matrix cells: no cell, no design-in.",
            "The matrix is the system's memory: the next project starts from your cells, not from zero.",
        ],
        "requirements": [
            "The complete pairing inventory: parts, modules, materials, interfaces, shared resources.",
            "The five-dimension sweep applied to every cell at survey depth.",
            "Deep analyses filed for every yellow cell before publication.",
            "A published, revisioned, three-color matrix with evidence per cell.",
            "The sustainment discipline: gating, reviews, verification feedback, yearly audit.",
        ],
        "standards": [
            "Cell evidence follows the datasheet and standard citations of the deep records.",
            "Revision control follows the project's document control practice.",
            "Verification feedback follows the verification record's test program.",
        ],
        "citations": [CIT_HOROWITZ, CIT_MACHINERY, CIT_ISO286],
        "sig_lens": (
            "The Signature read: this record is the method handing you "
            "its own tools - the ledger teaching you to keep a ledger. "
            "The Signature Handshake Method ends where it began: every "
            "pairing a covenant, every verdict witnessed, every yellow "
            "honored with limits, and the whole memory of handshakes kept "
            "where the next builder will find it. Build the matrix, keep "
            "the matrix, and no handshake in your system will ever again "
            "be shaken in the dark."
        ),
    },
]
