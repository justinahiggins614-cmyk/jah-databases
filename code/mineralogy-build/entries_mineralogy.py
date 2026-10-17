#!/usr/bin/env python3
"""Seed entries for the Mineralogy field build (field #8, taxonomy order).

Verified 2026-10-17: NO database covers mineralogy as a science. Manifest
slug hit 'rocks-minerals' is a 52-record specimen catalog (rock overviews,
FAQs, applications) with no crystal systems, classification science,
optical mineralogy, or X-ray crystallography; 'geology' (10,000 records) is
the broad geology database with mineral content but no dedicated mineralogy
science coverage. So this build creates two NEW databases:

  mineralogy              — The Mineralogy Database (public-harvest: real,
                            fact-checked mineralogy — crystal systems and
                            symmetry, Dana/Strunz classification, physical
                            properties (hardness, cleavage, luster, streak,
                            color, specific gravity), optical mineralogy,
                            X-ray crystallography, formation environments,
                            rock-forming vs ore minerals, gemstones,
                            identification methods)
  mineralogy-signature    — The Mineralogy Signature Database (his original
                            Signature interpretation; src signature, titles
                            suffixed " (Signature Edition)", never presented
                            as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation constants (standard mineralogy literature)
CIT_DANA = ("Dana, J. D. (1837). 'A System of Mineralogy'. Durrie and Peck, "
            "New Haven.")
CIT_KLEIN = ("Klein, C. & Dutrow, B. (2007). 'Manual of Mineral Science', "
             "23rd ed. John Wiley & Sons.")
CIT_NESSE = ("Nesse, W. D. (2012). 'Introduction to Optical Mineralogy', "
             "4th ed. Oxford University Press.")
CIT_BRAGG = ("Bragg, W. H. & Bragg, W. L. (1913). 'The reflection of X-rays "
             "by crystals.' Proceedings of the Royal Society A 88: 428-438.")
CIT_BOWEN = ("Bowen, N. L. (1928). 'The Evolution of the Igneous Rocks'. "
             "Princeton University Press.")
CIT_PAULING = ("Pauling, L. (1929). 'The principles determining the structure "
               "of complex ionic crystals.' Journal of the American Chemical "
               "Society 51: 1010-1026.")
CIT_GOLDSCHMIDT = ("Goldschmidt, V. M. (1937). 'The principles of distribution "
                   "of chemical elements in minerals and rocks.' Journal of "
                   "the Chemical Society: 655-673.")
CIT_MOHS = ("Mohs, F. (1812). 'Versuch einer Elementar-Methode zur "
            "naturhistorischen Bestimmung und Erkennung der Fossilien'. "
            "Camesina, Vienna.")
CIT_STRUNZ = ("Strunz, H. & Nickel, E. H. (2001). 'Strunz Mineralogical "
              "Tables', 9th ed. Schweizerbart.")
CIT_DEER = ("Deer, W. A., Howie, R. A. & Zussman, J. (1963-). "
            "'Rock-Forming Minerals'. Geological Society of London.")
CIT_PUTNIS = ("Putnis, A. (1992). 'Introduction to Mineral Sciences'. "
              "Cambridge University Press.")
CIT_GIA = ("Standard gemological literature (gemstone properties, cutting "
           "grades, and treatment disclosure conventions).")
CIT_IMA = ("International Mineralogical Association — Commission on New "
           "Minerals, Nomenclature and Classification (CNMNC).")
CIT_STD = ("Standard mineralogy literature (peer-reviewed textbooks and "
           "journals).")
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "mineralogy, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-mineralogy", "name": "What Is Mineralogy: The Science of Earth's Crystalline Materials",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Mineralogy is the science of minerals — the naturally occurring crystalline "
  "solids that make up rocks, soils, ores, and gemstones. A mineral has five "
  "strict tests: it is naturally occurring, inorganic, solid, has a definite "
  "chemical composition, and possesses an ordered internal atomic structure. "
  "About 6,000 mineral species have been approved by the International "
  "Mineralogical Association, yet just a few dozen — quartz, feldspar, mica, "
  "olivine, pyroxene, amphibole, calcite — build nearly all of Earth's crust. "
  "Mineralogy studies how minerals form, how their atoms pack into crystal "
  "structures, and how composition and structure control every physical "
  "property from hardness to color. It underpins geology, mining, materials "
  "science, and gemology: every mine, every gemstone, every ceramic, and "
  "every microchip traces back to minerals understood by this science."),
 "how_it_works": (
  "Mineralogy works by connecting three levels of a mineral: its chemistry "
  "(which atoms and in what ratios), its crystal structure (how those atoms "
  "are ordered in space), and its physical properties (what you can measure "
  "with your hands, eyes, and instruments). A mineralogist reads the structure "
  "from X-ray diffraction, measures composition with analytical instruments, "
  "and tests properties like hardness, cleavage, density, and optical behavior "
  "to identify the mineral and explain how it formed. Because the same chemistry "
  "in a different structure makes a different mineral — diamond and graphite are "
  "both pure carbon — the internal arrangement matters as much as the formula. "
  "Modern mineralogy maps formation environments onto these properties, so a "
  "handful of tests on an unknown crystal reveals where it grew and what it is."),
 "key_points": [
  "Mineralogy: the science of naturally occurring crystalline solids — the building blocks of rocks, ores, and gemstones",
  "Five strict tests: naturally occurring, inorganic, solid, definite composition, ordered atomic structure",
  "About 6,000 approved mineral species, but a few dozen rock-forming minerals build nearly all of Earth's crust",
  "Diamond and graphite are both pure carbon — structure matters as much as chemistry",
  "Connects chemistry, crystal structure, and physical properties into one explanation",
  "Underpins mining, materials science, gemology, and ceramics",
 ],
 "requirements": [
  "Curiosity about how crystals and rocks are put together",
  "A hand lens and a few mineral specimens to practice recognizing",
  "Willingness to learn basic chemistry (atoms, formulas, bonds)",
  "A notebook for recording observations of hardness, color, and shape",
 ],
 "standards": [
  "Mineral definition per the five IMA-accepted criteria",
  "Species counts per the International Mineralogical Association approved list",
 ],
 "citations": [CIT_KLEIN, CIT_DANA],
 "sig_lens": (
  "Signature edition: mineralogy reframed as the engineering of ordered "
  "matter — every mineral read as a solved packing problem, with his "
  "original framework for predicting properties from structure alone."),
 "demo_kind": "mineral_count",
},
{
 "key": "five-criteria", "name": "The Five Tests: What Counts as a Mineral",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Not every solid is a mineral. A substance must pass five tests: (1) "
  "naturally occurring — formed by natural processes, not synthesized; "
  "(2) inorganic — not made by organisms (coal and pearls fail here); "
  "(3) solid — liquids like mercury and petroleum fail; (4) definite "
  "chemical composition — expressible as a formula, even when some atoms "
  "substitute for each other within limits; (5) ordered internal structure — "
  "atoms arranged in a repeating crystalline lattice, which is why volcanic "
  "glass (obsidian) is a mineraloid, not a mineral. These tests are "
  "definitional, not casual: opal, formed in nature with variable water "
  "content and no long-range order, is classed as a mineraloid. Water ice "
  "passes all five — it is a genuine mineral when it occurs naturally. The "
  "criteria exist so the 6,000 mineral species are a well-defined set, not "
  "an endless list of every rock-like substance."),
 "how_it_works": (
  "Applying the five tests works like a decision checklist run in order. "
  "First ask whether the substance formed naturally — a lab-grown crystal "
  "with the exact structure of quartz is not a mineral specimen, it is a "
  "synthetic. Then check it is inorganic and solid, ruling out biological "
  "products and liquids. Then determine composition: a formula must be "
  "statable, though solid-solution series (like olivine, Mg2SiO4 to Fe2SiO4) "
  "are allowed compositional ranges, not fixed points. Finally confirm "
  "crystallinity: X-ray diffraction must show a repeating lattice, not a "
  "random glass. Failing any single test demotes the substance to mineraloid, "
  "synthetic, or non-mineral — each with its own correct category."),
 "key_points": [
  "Five tests, all required: naturally occurring, inorganic, solid, definite composition, ordered structure",
  "Coal, pearls, and amber fail the inorganic test; mercury fails the solid test",
  "Obsidian and opal fail the ordered-structure test — they are mineraloids, not minerals",
  "Natural water ice passes all five tests and is a genuine mineral",
  "Solid-solution series allow compositional ranges within a stated formula",
  "Lab-grown crystals identical to natural ones are synthetics, not minerals",
 ],
 "requirements": [
  "A list of candidate substances to test (quartz, opal, coal, ice, steel, glass)",
  "Basic chemistry knowledge: elements, compounds, formulas",
  "Understanding that 'definite composition' allows defined substitution ranges",
  "Access to the mineral definition as published in standard textbooks",
 ],
 "standards": [
  "The five IMA-accepted mineral criteria per standard mineralogy texts",
  "Mineraloid classification per Klein & Dutrow conventions",
 ],
 "citations": [CIT_KLEIN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: the five tests rewritten as his original pass/fail "
  "decision engine — a deterministic classifier that sorts any substance "
  "into mineral, mineraloid, synthetic, or non-mineral in five checks."),
 "demo_kind": "five_tests",
},
{
 "key": "crystal-systems", "name": "Crystal Systems: The Seven Symmetry Systems of Mineralogy",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Every crystal belongs to one of seven crystal systems, defined by the "
  "lengths and angles of its unit-cell axes: cubic (a=b=c, all angles 90°), "
  "tetragonal (a=b≠c, all 90°), orthorhombic (a≠b≠c, all 90°), hexagonal "
  "(a=b≠c, two angles 90° and one 120°), trigonal (a=b=c, all angles equal "
  "but not 90°), monoclinic (a≠b≠c, two angles 90°), and triclinic "
  "(a≠b≠c, no angles 90°). The system is determined by symmetry, not by "
  "which faces grew best: a distorted cube of galena is still cubic because "
  "its internal symmetry is cubic. Higher symmetry means fewer independent "
  "measurements are needed — a cubic mineral's refractive index is single "
  "and its thermal expansion identical in all directions, while a triclinic "
  "mineral needs full directional characterization. Learning the seven "
  "systems is learning the coordinate language of all crystallography."),
 "how_it_works": (
  "Assigning a crystal system works by finding its symmetry elements — "
  "mirror planes, rotation axes, centers of symmetry — and matching them to "
  "one of the seven groups those elements can form. Measure or observe the "
  "unit cell: if all three axes are equal and mutually perpendicular, the "
  "system is cubic; relaxing those equalities step by step walks down through "
  "tetragonal, orthorhombic, monoclinic, to triclinic, with hexagonal and "
  "trigonal as the special sixfold/threefold branches. The external crystal "
  "shape hints at the system — hexagonal prisms of quartz, cubic forms of "
  "pyrite — but poor growth can hide it, so X-ray measurement of the lattice "
  "gives the final answer. Once the system is known, every directional "
  "property of the mineral is constrained by its symmetry rules."),
 "key_points": [
  "Seven crystal systems defined by unit-cell axis lengths and interaxial angles",
  "Cubic is highest symmetry (a=b=c, all 90°); triclinic is lowest (all unequal, none 90°)",
  "The system is set by internal symmetry, not by how well faces developed",
  "Higher symmetry means fewer independent property measurements are needed",
  "Quartz: hexagonal/trigonal; pyrite and galena: cubic; feldspar: triclinic/monoclinic",
  "X-ray lattice measurement settles ambiguous cases the eye cannot",
 ],
 "requirements": [
  "Wooden or paper crystal models (or 3D prints) of the seven systems",
  "A protractor and ruler for measuring model faces and axes",
  "Familiarity with the three lattice parameters a, b, c and angles alpha, beta, gamma",
  "Reference table of the seven systems' defining equalities",
 ],
 "standards": [
  "Crystallographic conventions for axis notation (a, b, c; alpha, beta, gamma)",
  "System definitions per standard crystallography texts (Klein & Dutrow)",
 ],
 "citations": [CIT_KLEIN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: the seven systems presented as his original symmetry "
  "compression scheme — each system a rule for how much measurement work a "
  "crystal demands, from cubic's single number to triclinic's full tensor."),
 "demo_kind": "crystal_systems",
},
{
 "key": "mineral-habit", "name": "Mineral Habit: The Shapes Crystals Take",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Habit is the characteristic external shape a mineral typically grows in — "
  "prismatic columns of tourmaline, bladed fans of kyanite, cubic grains of "
  "galena, fibrous masses of asbestos-form serpentine, botryoidal (grape-like) "
  "masses of malachite, and dendritic (branching) patterns of native copper. "
  "Habit reflects growth conditions: fast-growing faces disappear, leaving "
  "the slow-growing faces to define the final form, so the same mineral can "
  "show different habits in different environments — quartz grows as stubby "
  "prisms in veins and as fine druzy coatings in cavities. Habit is a "
  "field-identification workhorse because it is visible at a glance, but it "
  "is never proof alone: massive (shapeless) specimens of any mineral show no "
  "habit at all. Standard habit terms — acicular, bladed, columnar, equant, "
  "fibrous, foliated, granular, massive, platy, prismatic, tabular — form the "
  "shared vocabulary collectors and geologists use to describe specimens."),
 "how_it_works": (
  "Habit develops through differential growth rates on crystal faces. Each "
  "face of a growing crystal advances at a rate set by its atomic attachment "
  "energy, the solution's supersaturation, temperature, and impurities; the "
  "fastest faces grow themselves out of existence, and the surviving slow "
  "faces enclose the final shape. Impurities can poison specific faces — "
  "trace elements flatten quartz into tabular crystals in some deposits. "
  "Space constraints matter too: crystals growing freely in a cavity develop "
  "euhedral (well-formed) habits, while those crowded by neighbors grow "
  "anhedral (shapeless) masses. To use habit for identification, compare the "
  "specimen's dominant form against the mineral's documented habits, then "
  "confirm with a second property like hardness or cleavage, since "
  "environment-driven habit variation can mislead."),
 "key_points": [
  "Habit: the characteristic external growth shape (prismatic, bladed, fibrous, botryoidal, dendritic, cubic...)",
  "Fast-growing faces disappear; slow-growing faces define the final form",
  "Same mineral, different environments can produce different habits",
  "Euhedral crystals grow freely; anhedral masses grow crowded",
  "Standard habit terms form the shared descriptive vocabulary of the field",
  "Habit identifies at a glance but always needs a confirming second test",
 ],
 "requirements": [
  "A set of specimens or photographs showing contrasting habits",
  "Hand lens (10x) to see face development on small crystals",
  "A habit-term reference card for consistent descriptions",
  "Awareness that massive specimens show no diagnostic habit",
 ],
 "standards": [
  "Habit terminology per standard mineralogy references (Klein & Dutrow)",
  "Euhedral/subhedral/anhedral grain-shape conventions",
 ],
 "citations": [CIT_KLEIN, CIT_DANA],
 "sig_lens": (
  "Signature edition: habit decoded as his original growth-rate signature — "
  "a visual readout of which faces grew fastest, turning every crystal into "
  "a frozen record of its own formation conditions."),
 "demo_kind": "habit_lookup",
},
{
 "key": "mohs-hardness", "name": "The Mohs Hardness Scale: Scratch Testing",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The Mohs scale ranks ten reference minerals by scratch resistance, from "
  "talc (1) through gypsum (2), calcite (3), fluorite (4), apatite (5), "
  "orthoclase (6), quartz (7), topaz (8), corundum (9), to diamond (10). "
  "Each mineral scratches all those below it and is scratched by all above — "
  "a purely ordinal scale, so the hardness gap between 9 and 10 dwarfs the "
  "gap between 1 and 2. In the field, everyday tools substitute for the "
  "reference minerals: a fingernail is about 2.5, a copper coin about 3, a "
  "steel nail or knife blade about 5.5, window glass about 5.5, and a steel "
  "file about 6.5. Hardness reflects bond strength and structure — diamond's "
  "three-dimensional covalent network tops the scale, while graphite, pure "
  "carbon with weak interlayer bonds, sits near 1. The test is directional "
  "in some minerals: kyanite is 5 along its length but 7 across it."),
 "how_it_works": (
  "A scratch test works by dragging a harder point across a fresh mineral "
  "surface and checking whether a groove forms. Test both directions: try "
  "to scratch the unknown with the reference, then the reference with the "
  "unknown, because a true scratch cuts a groove while a rubbed-off powder "
  "trail wipes away. Work on a fresh surface or an inconspicuous spot, use "
  "firm steady pressure, and confirm with a hand lens — a real scratch has "
  "sharp edges and displaced material. Bracket the hardness: if a steel nail "
  "(5.5) scratches the mineral but a glass plate (5.5) does not, the mineral "
  "sits near 5.5 and finer references narrow it further. Report the result "
  "as a range (e.g., 6–6.5) rather than a false single number, and note any "
  "direction dependence, since hardness is a vector property in anisotropic "
  "minerals."),
 "key_points": [
  "Ten reference minerals, talc (1) to diamond (10); each scratches all below it",
  "Ordinal scale only — the 9-to-10 gap is enormous, the 1-to-2 gap is small",
  "Field substitutes: fingernail 2.5, copper 3, steel 5.5, glass 5.5, file 6.5",
  "A true scratch grooves the surface; a powder trail wipes off",
  "Hardness reflects bond strength and structure — diamond vs graphite",
  "Kyanite is direction-dependent: 5 one way, 7 the other",
 ],
 "requirements": [
  "A Mohs kit or field substitutes (nail, coin, glass plate, file)",
  "Fresh mineral surfaces and a 10x hand lens to verify grooves",
  "Practice distinguishing a true scratch from a powder streak",
  "The ten-mineral reference list committed to memory",
 ],
 "standards": [
  "Mohs scale reference minerals per Mohs (1812) and modern standard lists",
  "Ordinal-scale reporting conventions (report ranges, note anisotropy)",
 ],
 "citations": [CIT_MOHS, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: hardness treated as his original bond-strength "
  "readout — a scratch test becomes a one-motion probe of the crystal's "
  "internal bonding network, ranked against the ten reference anchors."),
 "demo_kind": "mohs_bracket",
},
{
 "key": "cleavage-fracture", "name": "Cleavage, Fracture, and Parting: How Minerals Break",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Cleavage is the tendency of a mineral to break along flat planes of "
  "atomic weakness, and it is one of the most diagnostic physical "
  "properties. Mica splits into paper-thin sheets along one perfect plane "
  "because its layers are weakly bonded; halite and galena break into "
  "cubes along three planes at right angles; calcite rhombs split along "
  "three planes that are not at right angles. Cleavage is described by the "
  "number of directions and their quality — perfect, good, distinct, poor — "
  "and the angles between them: feldspar's two planes meet at nearly 90°, "
  "pyroxene's at about 90°, amphibole's at 56° and 124°. When no weak planes "
  "exist, minerals fracture instead: quartz shows conchoidal (curved, "
  "shell-like) fracture, the same break that let flint knappers shape "
  "arrowheads. Parting looks like cleavage but is caused by twinning or "
  "exsolution lamellae, not by the structure itself."),
 "how_it_works": (
  "Cleavage works because crystal structures are anisotropic: bonds are "
  "strong in some directions and weak in others, and the mineral parts "
  "where the bonds are weakest. To observe it, strike or press the specimen "
  "and examine the fresh surfaces — cleavage planes are flat, often "
  "reflective, and repeat at consistent angles, while fracture surfaces "
  "curve or splinter irregularly. Count the directions by rotating the "
  "specimen: one plane gives sheets (mica), two give prisms (feldspar, "
  "pyroxene, amphibole), three give cubes or rhombs (halite, galena, "
  "calcite), four give octahedral fragments (fluorite), six give "
  "rhombohedra (sphalerite). Measure the interplanar angles with a "
  "protractor or goniometer — the 56°/124° amphibole angle versus the 90° "
  "pyroxene angle is the classic field distinction between the two dark "
  "mineral groups."),
 "key_points": [
  "Cleavage: breakage along structural planes of weakness — flat, repeating, reflective",
  "Described by number of directions, quality (perfect to poor), and angles between planes",
  "Mica: 1 perfect; feldspar: 2 at ~90°; halite/galena: 3 at 90°; calcite: 3 not at 90°; fluorite: 4",
  "Amphibole 56°/124° vs pyroxene ~90° is the classic cleavage-angle distinction",
  "Fracture (quartz: conchoidal) happens where no weak planes exist",
  "Parting mimics cleavage but comes from twinning, not structure",
 ],
 "requirements": [
  "Specimens with contrasting cleavage (mica, halite, calcite, feldspar, quartz)",
  "A protractor or contact goniometer for measuring plane angles",
  "A hand lens to check whether a break is flat (cleavage) or curved (fracture)",
  "Gentle tools — cleavage is best seen on fresh breaks, not hammered rubble",
 ],
 "standards": [
  "Cleavage notation: number of directions + quality + angles (standard references)",
  "Conchoidal/uneven/splintery/hackly fracture terminology",
 ],
 "citations": [CIT_KLEIN, CIT_DEER],
 "sig_lens": (
  "Signature edition: breakage read as his original structural X-ray — "
  "every cleavage plane a direct map of where the crystal's bonds are "
  "weakest, turning a hammer tap into structural data."),
 "demo_kind": "cleavage_angles",
},
{
 "key": "luster-streak", "name": "Luster and Streak: How Minerals Handle Light",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Luster describes how light reflects from a mineral's surface, and the "
  "first split is metallic versus non-metallic. Metallic luster — the "
  "opaque shine of pyrite, galena, or native copper — comes from free "
  "electrons and usually means an ore mineral; submetallic is the duller "
  "in-between. Non-metallic lusters have a vocabulary of their own: "
  "vitreous (glassy, like quartz), pearly (like mica sheets), silky (fibrous "
  "minerals), resinous (like sphalerite), waxy, greasy, adamantine (the "
  "fiery brilliance of diamond), and dull or earthy (like kaolinite). Streak "
  "is the color of the mineral's powder, tested by rubbing on unglazed "
  "porcelain: hematite's streak is unmistakable reddish-brown even when the "
  "specimen looks steel-gray, and pyrite's greenish-black streak separates "
  "it from gold's golden-yellow streak — the classic fool's-gold test. "
  "Streak beats surface color for identification because powder color is "
  "far more consistent than the impurities that tint whole crystals."),
 "how_it_works": (
  "Luster is judged by eye on a fresh surface in good light: hold the "
  "specimen so light rakes across it and classify the reflection as "
  "metallic (mirror-like, opaque) or one of the non-metallic types. Note "
  "that weathering dulls luster — always test the freshest face. The streak "
  "test works by crushing the mineral to powder, which averages out the "
  "surface impurities and oxidation films that mislead color judgments. "
  "Drag the specimen firmly across an unglazed porcelain streak plate and "
  "read the powder color; minerals harder than the plate (about 7) will not "
  "leave a streak and instead scratch the plate — itself a useful hardness "
  "clue. Record both: luster narrows the field (metallic vs non-metallic is "
  "the biggest single split in hand-sample identification), and streak "
  "confirms among the look-alikes."),
 "key_points": [
  "Luster: metallic vs non-metallic is the first and biggest visual split",
  "Non-metallic vocabulary: vitreous, pearly, silky, resinous, waxy, greasy, adamantine, dull",
  "Metallic luster (free electrons) usually signals an ore mineral",
  "Streak: powder color on porcelain — more reliable than surface color",
  "Hematite: red-brown streak; pyrite: greenish-black; gold: golden-yellow",
  "Minerals harder than ~7 scratch the plate instead of streaking",
 ],
 "requirements": [
  "An unglazed porcelain streak plate",
  "Good lighting and fresh mineral surfaces for luster judgment",
  "A luster-term reference list for consistent descriptions",
  "Caution: test streak on an inconspicuous spot of display specimens",
 ],
 "standards": [
  "Luster terminology per standard mineralogy references",
  "Streak-plate method (unglazed porcelain, ~hardness 7)",
 ],
 "citations": [CIT_KLEIN, CIT_DANA],
 "sig_lens": (
  "Signature edition: luster and streak as his original two-channel "
  "optical assay — surface reflection classifies the bonding, powder "
  "color bypasses the impurities, together a two-second field instrument."),
 "demo_kind": "luster_streak",
},
{
 "key": "mineral-color", "name": "Color in Minerals: Causes and Traps",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Color is the most obvious mineral property and the least trustworthy. "
  "Idiochromatic minerals are colored by an essential element — malachite "
  "is always green because copper is in its formula, azurite always blue. "
  "Allochromatic minerals are colored by trace impurities: pure quartz is "
  "colorless, but iron traces make amethyst purple, and irradiation plus "
  "aluminum makes smoky quartz brown. Pseudochromatic colors come from "
  "physical effects, not chemistry at all — the play of color in opal and "
  "labradorite is light diffracting through microscopic structures. Some "
  "minerals are reliable: sulfur is always yellow, cinnabar always red. But "
  "quartz alone spans colorless, white, gray, purple, yellow, brown, pink, "
  "and black, and fluorite can be nearly any color. The rule is simple: use "
  "color as a hint, never as proof — confirm every color-based guess with "
  "streak, hardness, or cleavage."),
 "how_it_works": (
  "Mineral color works through light absorption by electrons. In "
  "idiochromatic minerals, a major element's electron transitions absorb "
  "specific wavelengths — copper's d-electrons in malachite absorb red, "
  "leaving green reflected. In allochromatic minerals, trace transition "
  "metals or color centers (electron defects from radiation) do the "
  "absorbing: parts-per-million iron colors amethyst, and the color "
  "vanishes if the impurity is absent, which is why one quartz crystal can "
  "be purple and its neighbor colorless. Pseudochromatic effects need no "
  "absorber — interference and diffraction in thin layers or spheres "
  "split white light into spectral colors. To use color safely, ask which "
  "mechanism fits: consistent color across all specimens suggests "
  "idiochromatic (reliable); color varying wildly within one species "
  "suggests allochromatic or pseudochromatic (unreliable alone)."),
 "key_points": [
  "Color is the most obvious and least trustworthy identification property",
  "Idiochromatic: essential element colors it (malachite green, azurite blue) — reliable",
  "Allochromatic: trace impurities color it (amethyst, smoky quartz) — variable",
  "Pseudochromatic: light effects, not chemistry (opal, labradorite play of color)",
  "Quartz spans nearly every color; fluorite nearly any color — never identify by color alone",
  "Rule: color hints, streak/hardness/cleavage confirm",
 ],
 "requirements": [
  "Specimens showing color variation within one species (quartz, fluorite, calcite)",
  "A streak plate to see past surface color",
  "Basic understanding of light absorption by electrons",
  "Discipline to treat every color ID as provisional until confirmed",
 ],
 "standards": [
  "Idiochromatic/allochromatic/pseudochromatic classification (standard texts)",
  "Color-description conventions (hue, tone, consistency across specimens)",
 ],
 "citations": [CIT_KLEIN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: color decoded as his original three-mechanism "
  "sorter — essential-element, trace-impurity, or light-effect — each "
  "mechanism carrying a different trust rating for identification."),
 "demo_kind": "color_mechanism",
},
{
 "key": "specific-gravity", "name": "Specific Gravity: Weighing Minerals in Water",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Specific gravity (SG) is a mineral's density relative to water — a "
  "number with no units that says how many times heavier than an equal "
  "volume of water the mineral is. Most rock-forming minerals sit between "
  "2.5 and 3.5: quartz is 2.65, feldspar about 2.6, calcite 2.71. Metallic "
  "ore minerals run much higher — galena 7.5, native gold 19.3 — so heft "
  "alone can separate an ore from a look-alike rock mineral. SG reflects "
  "atomic weight and packing efficiency: dense atoms in tight structures "
  "give high values, which is why barite (BaSO4, SG 4.5) feels "
  "surprisingly heavy for a non-metallic mineral. The classic measurement "
  "uses Archimedes' principle — weigh the specimen in air, weigh it "
  "suspended in water, and divide: SG equals the air weight divided by "
  "the weight lost in water. No fancy instrument needed, just a balance, "
  "a beaker, and a thread."),
 "how_it_works": (
  "The water-weighing method works because a submerged object loses exactly "
  "the weight of the water it displaces. Weigh the clean, dry specimen in "
  "air (W_air), then hang it from the balance on a fine thread, submerge it "
  "fully in water without touching the beaker, and record the submerged "
  "weight (W_water). The loss W_air − W_water equals the weight of the "
  "displaced water, whose volume equals the specimen's volume — so "
  "SG = W_air / (W_air − W_water), with water's density taken as 1 g/cm³. "
  "Porous or cracked specimens trap air and read low; coat them in a thin "
  "wax layer (subtracting the wax's known contribution) or use a pycnometer "
  "for powders. For quick field estimates, simply heft two similar-sized "
  "specimens — the human hand reliably detects the quartz-to-galena "
  "difference after minimal practice."),
 "key_points": [
  "Specific gravity: density relative to water, unitless — quartz 2.65, galena 7.5, gold 19.3",
  "SG = weight in air divided by weight lost in water (Archimedes' principle)",
  "Reflects atomic weight plus packing efficiency",
  "Heft alone separates ore minerals from rock-mineral look-alikes",
  "Porous specimens read low — wax-coat or use a pycnometer",
  "Field shortcut: heft similar-sized specimens against a known reference",
 ],
 "requirements": [
  "A balance reading to 0.01 g, a beaker of water, and fine thread",
  "Clean, non-porous specimens (or wax for porous ones)",
  "Room-temperature water; record temperature for precise work",
  "A reference specimen of known SG for hand-heft calibration",
 ],
 "standards": [
  "SG definition: density relative to water at 4 °C",
  "Archimedes-method procedure per standard mineralogy lab manuals",
 ],
 "citations": [CIT_KLEIN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: specific gravity as his original mass-fingerprint — "
  "a balance, a beaker, and a thread become a composition probe, since "
  "density encodes atomic weight and packing in one number."),
 "demo_kind": "specific_gravity",
},
{
 "key": "dana-classification", "name": "The Dana Classification: Eight Chemical Classes",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The Dana system, originating with James Dwight Dana's 1837 System of "
  "Mineralogy, organizes minerals by chemistry into eight classes: native "
  "elements (gold, diamond, sulfur), sulfides (pyrite, galena), halides "
  "(halite, fluorite), oxides (hematite, corundum), carbonates (calcite, "
  "dolomite), nitrates, borates (borax), sulfates (gypsum, barite), "
  "phosphates (apatite), and silicates (quartz, feldspar, mica) — with "
  "silicates alone holding roughly 90 percent of Earth's crust. Each class "
  "is subdivided by structure and composition into finer groups, and every "
  "mineral gets a Dana number encoding its position (quartz is 75.1.3.1). "
  "Dana's chemistry-first ordering mirrors how minerals actually behave: "
  "members of a class share bonding types, typical properties, and "
  "formation environments. It remains the standard English-language "
  "reference framework, updated through successive editions for nearly two "
  "centuries."),
 "how_it_works": (
  "Classifying by Dana works by identifying the dominant anionic group in "
  "the formula. Read the formula and find the characteristic unit: no anion "
  "at all means native elements; S²⁻ means sulfides; Cl⁻ or F⁻ means "
  "halides; O²⁻ alone means oxides; (CO3)²⁻ means carbonates; (SO4)²⁻ "
  "sulfates; (PO4)³⁻ phosphates; (BO3)³⁻ or (B4O5(OH)4)²⁻ borates; and "
  "Si-O groupings mean silicates. Within the class, sort by cation and "
  "structure: the sulfide class splits into metal:sulfur ratio groups, the "
  "silicate class into the six structural families. The Dana number then "
  "pins the mineral's exact address — class, type, group, species — so any "
  "mineralogist worldwide can locate it in the system. When a formula fits "
  "no existing slot cleanly (complex sulfosalts, for example), the "
  "structural subdivisions decide the placement."),
 "key_points": [
  "Eight chemical classes from native elements to silicates, Dana 1837 onward",
  "Silicates alone form roughly 90% of Earth's crust",
  "Classification key: identify the dominant anionic group in the formula",
  "Dana numbers (e.g., quartz 75.1.3.1) encode class, type, group, species",
  "Class members share bonding types, properties, and formation environments",
  "The standard English-language reference framework for two centuries",
 ],
 "requirements": [
  "Ability to read chemical formulas and spot anionic groups",
  "A Dana class reference table with example minerals",
  "Familiarity with the six silicate structural families (they dominate the system)",
  "A current Dana reference for number lookups",
 ],
 "standards": [
  "Dana class definitions per the System of Mineralogy tradition",
  "Dana numbering: class.type.group.species hierarchy",
 ],
 "citations": [CIT_DANA, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: Dana's eight classes as his original chemical "
  "address system — every mineral filed by its anionic group, with the "
  "Dana number as a precise four-level locator."),
 "demo_kind": "dana_classify",
},
{
 "key": "strunz-classification", "name": "The Nickel-Strunz Classification: Structure-First Classes",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The Nickel-Strunz system (9th edition, Strunz & Nickel 2001) classifies "
  "minerals by crystal structure first and chemistry second, complementing "
  "Dana's chemistry-first approach. Its ten classes run: 1 elements, "
  "2 sulfides and sulfosalts, 3 halides, 4 oxides, 5 carbonates and "
  "nitrates, 6 borates, 7 sulfates/chromates/molybdates/tungstates, "
  "8 phosphates/arsenates/vanadates, 9 silicates, 10 organic compounds — "
  "with silicates subdivided by their tetrahedral linkage (neso-, soro-, "
  "cyclo-, ino-, phyllo-, tecto-). Every mineral gets a Strunz code like "
  "9.DA.05 for a specific structural slot, and the system is the working "
  "standard of the International Mineralogical Association's database. "
  "Because structure controls properties more directly than chemistry "
  "alone — the same composition in two structures can behave completely "
  "differently — the Strunz ordering is often the more predictive one for "
  "materials behavior. Serious mineral databases carry both Dana and "
  "Strunz codes for every species."),
 "how_it_works": (
  "Classifying by Nickel-Strunz works by determining the structural family "
  "before the chemistry. Identify the class from the dominant structural "
  "unit: isolated SiO4 tetrahedra mean nesosilicates (9.A), single chains "
  "mean inosilicates (9.D), sheets mean phyllosilicates (9.E), frameworks "
  "mean tectosilicates (9.F). Then subdivide by cation size, hydration, and "
  "additional anions to reach the exact code. The two-letter subdivision "
  "plus number (9.DA.05) places the mineral among its structural siblings "
  "regardless of which elements occupy the sites — so minerals that behave "
  "alike sit together even when their formulas differ. In practice, "
  "mineralogists look up the Strunz code after X-ray or optical work has "
  "revealed the structure, then use the code to find related species and "
  "predict unmeasured properties from structural analogs."),
 "key_points": [
  "Structure-first classification: ten classes, Strunz & Nickel 9th ed. (2001)",
  "Silicates subdivided by tetrahedral linkage (neso through tecto)",
  "Strunz codes (e.g., 9.DA.05) pin the exact structural slot",
  "The IMA database's working standard; complements Dana's chemistry-first order",
  "Structure predicts behavior — same chemistry in two structures behaves differently",
  "Serious databases carry both Dana and Strunz codes per species",
 ],
 "requirements": [
  "Structural data (from X-ray or reliable references) — chemistry alone is not enough",
  "The ten-class Strunz table with silicate subdivision codes",
  "Understanding of tetrahedral linkage terminology",
  "Access to the IMA mineral list for code verification",
 ],
 "standards": [
  "Nickel-Strunz 9th edition class and subdivision codes",
  "IMA-CNMNC usage as the database working standard",
 ],
 "citations": [CIT_STRUNZ, CIT_IMA],
 "sig_lens": (
  "Signature edition: Strunz as his original structure-first index — "
  "minerals filed by how their atoms link, so behaviorally similar "
  "species sit together no matter which elements they contain."),
 "demo_kind": "strunz_classify",
},
{
 "key": "reading-formulas", "name": "Reading Mineral Formulas: From Symbols to Composition",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A mineral formula is a compressed description of its chemistry: quartz "
  "SiO2 (one silicon, two oxygens), calcite CaCO3, halite NaCl, pyrite FeS2. "
  "Parentheses group units that substitute — olivine (Mg,Fe)2SiO4 means "
  "magnesium and iron share the same sites in any ratio, and the endmembers "
  "forsterite Mg2SiO4 and fayalite Fe2SiO4 name the pure extremes. Water of "
  "crystallization gets a dot: gypsum CaSO4·2H2O. Hydroxyl (OH) and fluorine "
  "commonly swap in micas and amphiboles, written (OH,F). Charges must "
  "balance: the cation charges sum to cancel the anion charges, which is "
  "why formulas are checkable arithmetic, not just labels. Reading fluency "
  "turns every formula into predictions — heavy cations mean high specific "
  "gravity, transition metals mean color, and (CO3) means the acid test "
  "will fizz."),
 "how_it_works": (
  "Reading a formula works left to right through its groups. Split off the "
  "anionic group first — (SiO4), (CO3), (SO4) — since it sets the Dana "
  "class. Expand parentheses: (Mg,Fe)2SiO4 means two cation sites each "
  "fillable by Mg or Fe, giving the full range from Mg2SiO4 to Fe2SiO4. "
  "Check charge balance by summing oxidation states — Ca²⁺ with (CO3)²⁻ "
  "balances to neutral, confirming CaCO3. Convert to weight percent by "
  "dividing each element's atomic-weight contribution by the formula weight; "
  "this is how assays are computed and how ore grades are stated. Watch the "
  "special notations: the dot in hydrates, (OH,F) for coupled substitution, "
  "and square brackets for complex anions. With fluency, a formula like "
  "Cu2CO3(OH)2 immediately reads as a copper carbonate hydroxide — "
  "malachite, green, effervesces in acid."),
 "key_points": [
  "Formulas compress chemistry: quartz SiO2, calcite CaCO3, pyrite FeS2",
  "Parentheses mark substitution: (Mg,Fe)2SiO4 spans forsterite to fayalite",
  "Dot marks water of crystallization: gypsum CaSO4·2H2O",
  "(OH,F) marks common anion swaps in micas and amphiboles",
  "Charges must balance — formulas are checkable arithmetic",
  "Fluency turns formulas into predictions: weight, color, acid response",
 ],
 "requirements": [
  "Periodic table with atomic weights and common oxidation states",
  "Practice expanding 20+ real mineral formulas by hand",
  "A calculator for formula-weight and weight-percent conversions",
  "Reference list of common anionic groups and their charges",
 ],
 "standards": [
  "IMA-approved formula notation conventions",
  "Charge-balance and endmember nomenclature rules",
 ],
 "citations": [CIT_KLEIN, CIT_IMA],
 "sig_lens": (
  "Signature edition: formulas as his original compressed chemistry — a "
  "parsing engine that expands every parenthesis, balances every charge, "
  "and converts symbols straight into weight percent and predictions."),
 "demo_kind": "formula_weight",
},

# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "point-groups", "name": "Symmetry Elements and the 32 Point Groups",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Crystal symmetry is described by symmetry elements — mirror planes (m), "
  "rotation axes (2, 3, 4, 6-fold), inversion centers (i), and rotoinversion "
  "axes — and the 32 unique combinations of these elements are the point "
  "groups. Every mineral's external symmetry belongs to exactly one point "
  "group, and each point group belongs to one crystal system: cubic holds "
  "five point groups, hexagonal seven, and so on down to triclinic's two. "
  "The point group dictates which physical properties can be directional: "
  "a center of symmetry forbids piezoelectricity, which is why quartz "
  "(point group 32, no center) is piezoelectric and halite (m3m, centered) "
  "is not. Hermann-Mauguin symbols like 4/mmm or -43m encode the elements "
  "compactly. Learning the 32 groups is learning the complete catalog of "
  "ways a crystal can be symmetric — the grammar behind the seven systems."),
 "how_it_works": (
  "Determining a point group works by inventorying the symmetry elements "
  "visible in the crystal's faces. Find the highest-order rotation axis "
  "first — a 4-fold axis immediately restricts the candidates to the "
  "tetragonal groups. Then check for mirror planes perpendicular and "
  "parallel to that axis, and for a center of symmetry (test: does every "
  "face have a parallel opposite face?). Match the collected elements "
  "against the 32-group table to name the group. The payoff is predictive: "
  "the point group tells you which tensor properties are allowed — "
  "piezoelectricity needs a non-centrosymmetric group, optical activity "
  "needs an enantiomorphic one, and the number of independent elastic "
  "constants drops as symmetry rises. X-ray diffraction confirms the "
  "assignment when faces are poorly developed, via systematic absences and "
  "Laue symmetry."),
 "key_points": [
  "32 point groups: every unique combination of mirror planes, rotation axes, inversion centers",
  "Each point group belongs to one crystal system (cubic 5 groups ... triclinic 2)",
  "Center of symmetry forbids piezoelectricity — quartz yes, halite no",
  "Hermann-Mauguin symbols (4/mmm, -43m) encode the elements compactly",
  "Point group predicts which directional properties are physically allowed",
  "X-ray Laue symmetry confirms the group when crystal faces are poor",
 ],
 "requirements": [
  "Crystal models marked with their symmetry elements",
  "The 32-group table with Hermann-Mauguin symbols",
  "Understanding of tensors at an intuitive level (direction-dependent properties)",
  "Stereographic projection basics for plotting symmetry",
 ],
 "standards": [
  "Hermann-Mauguin notation per the International Tables for Crystallography",
  "32 point group definitions (crystallographic restriction: 1,2,3,4,6-fold only)",
 ],
 "citations": [CIT_KLEIN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: the 32 groups as his original symmetry grammar — a "
  "complete inventory of how crystals can be symmetric, each group a rule "
  "book for which physical effects the crystal is allowed to show."),
 "demo_kind": "point_group_lookup",
},
{
 "key": "bravais-lattices", "name": "Crystal Lattices: The 14 Bravais Lattices",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "A crystal lattice is the infinite repeating pattern of points on which "
  "atoms sit, and Auguste Bravais proved in 1850 that only 14 distinct "
  "lattices exist in three dimensions. They arise from the seven crystal "
  "systems combined with four centering types: primitive (P, points only at "
  "corners), body-centered (I, plus a point at the cell center), face-centered "
  "(F, plus points at face centers), and base-centered (C, plus points on one "
  "pair of faces). Not every combination is unique — a face-centered "
  "tetragonal lattice is really a smaller body-centered one — leaving exactly "
  "14. The lattice plus the motif (which atoms sit at each point) fully "
  "defines a crystal structure: diamond is a face-centered cubic lattice "
  "with a two-atom motif. X-ray diffraction reads the lattice directly "
  "from the diffraction pattern's geometry, making Bravais lattices the "
  "bridge between measured spots and atomic arrangements."),
 "how_it_works": (
  "Identifying the Bravais lattice works from the diffraction pattern or "
  "from measured cell parameters. Index the diffraction spots to find the "
  "unit cell, then look for systematic absences — missing spots that reveal "
  "centering: body-centering kills spots where h+k+l is odd, face-centering "
  "kills spots with mixed even/odd indices. Match the cell shape to a "
  "crystal system and the absences to a centering type, and the pair names "
  "the lattice (e.g., orthorhombic F). The conventional cell is chosen for "
  "maximum symmetry display, not minimum volume, which is why some centered "
  "cells contain multiple lattice points. Once the lattice is known, "
  "placing the motif atoms at the lattice points — using fractional "
  "coordinates from structure solution — completes the full crystal "
  "structure description."),
 "key_points": [
  "Exactly 14 distinct lattices: 7 systems × 4 centerings, minus redundancies",
  "Centering types: primitive P, body-centered I, face-centered F, base-centered C",
  "Lattice + motif (atoms per point) fully defines a crystal structure",
  "Diamond: face-centered cubic lattice with a two-atom motif",
  "Systematic absences in diffraction reveal the centering type",
  "Bravais (1850): the complete catalog, proven, never extended",
 ],
 "requirements": [
  "Unit-cell models showing the four centering types",
  "Indexing practice: assigning hkl to diffraction spots",
  "Systematic-absence tables for P, I, F, C centerings",
  "Fractional-coordinate convention for placing motif atoms",
 ],
 "standards": [
  "Bravais lattice definitions per the International Tables for Crystallography",
  "Conventional-cell choice rules (maximum symmetry display)",
 ],
 "citations": [CIT_KLEIN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: the 14 lattices as his original proof of finiteness — "
  "only fourteen ways to repeat in 3D, and every crystal ever found fits "
  "one, a closed catalog no new discovery can escape."),
 "demo_kind": "bravais_lookup",
},
{
 "key": "silicate-structures", "name": "Silicate Structures: The Six Tetrahedral Families",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Silicate minerals are built from SiO4 tetrahedra — a silicon atom "
  "gripped by four oxygens — and the six families differ only in how those "
  "tetrahedra link: nesosilicates (isolated tetrahedra, olivine; Si:O = "
  "1:4), sorosilicates (paired, epidote; 2:7), cyclosilicates (rings, "
  "beryl and tourmaline; 1:3), inosilicates (single chains, pyroxene; 1:3 — "
  "and double chains, amphibole; 4:11), phyllosilicates (sheets, mica and "
  "clay; 2:5), and tectosilicates (full frameworks, quartz and feldspar; "
  "1:2). The linkage controls everything: sheet silicates cleave into "
  "flakes (mica), chain silicates into prisms (pyroxene, amphibole), and "
  "framework silicates have no dominant cleavage (quartz fractures). "
  "Aluminum freely substitutes for silicon in the tetrahedra, and the "
  "charge deficit is balanced by cations like K⁺, Na⁺, and Ca²⁺ sitting "
  "between the linked units — the chemical engine behind the feldspar and "
  "clay families."),
 "how_it_works": (
  "Classifying a silicate works by counting shared oxygens per tetrahedron. "
  "Each shared oxygen counts half toward each tetrahedron, so isolated "
  "tetrahedra give SiO4 (1:4), pairs give Si2O7 (2:7), rings and single "
  "chains give SiO3 (1:3), double chains give Si4O11 (4:11), sheets give "
  "Si2O5 (2:5), and frameworks give SiO2 (1:2). Read the formula's Si:O "
  "ratio to place an unknown: a 1:3 ratio means rings or single chains, and "
  "cleavage then decides between them (rings cleave poorly, chains give "
  "prismatic cleavage). Aluminum substitution is tracked by charge: each "
  "Al³⁺ replacing Si⁴⁺ needs one extra +1 cation nearby, which is why "
  "potassium feldspar KAlSi3O8 and albite NaAlSi3O8 carry exactly the "
  "alkalis their aluminum demands. The linkage also predicts weathering: "
  "framework silicates resist, sheet silicates hydrate into clays."),
 "key_points": [
  "Six families from one building block: the SiO4 tetrahedron",
  "Linkage sets the Si:O ratio: 1:4 isolated → 1:2 framework",
  "Linkage controls cleavage: sheets flake, chains prism, frameworks fracture",
  "Al substitutes for Si; alkalis balance the charge (feldspars, micas)",
  "Cyclosilicates (beryl, tourmaline) host the great gemstones",
  "Weathering resistance follows linkage: frameworks last, sheets hydrate to clay",
 ],
 "requirements": [
  "Tetrahedron models (or drawings) for each of the six linkages",
  "Si:O ratio table for quick formula-to-family placement",
  "Specimens: olivine, epidote, beryl, pyroxene, mica, quartz",
  "Charge-balance practice with Al-for-Si substitution",
 ],
 "standards": [
  "Silicate family definitions (neso/soro/cyclo/ino/phyllo/tecto)",
  "Si:O ratio conventions per structural linkage",
 ],
 "citations": [CIT_KLEIN, CIT_DEER],
 "sig_lens": (
  "Signature edition: the six families as his original linkage code — one "
  "tetrahedron, six ways to share oxygens, and the sharing pattern "
  "predicts cleavage, weathering, and gemstone potential outright."),
 "demo_kind": "silicate_ratio",
},
{
 "key": "rock-forming", "name": "Rock-Forming Minerals: The Minerals That Build Continents",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Fewer than thirty minerals make up the vast bulk of Earth's crust, and "
  "about a dozen do most of the work: quartz, the feldspars (orthoclase, "
  "albite, anorthite), micas (muscovite, biotite), amphiboles (hornblende), "
  "pyroxenes (augite), olivine, calcite, dolomite, and the clay minerals. "
  "Feldspar alone is roughly 60 percent of the crust by weight; quartz and "
  "feldspar together dominate every granite and sandstone. These minerals "
  "are rock-forming because they crystallize abundantly from common magmas, "
  "survive weathering in large volumes, or precipitate in bulk from water — "
  "not because they are rare or exotic. Identifying rocks in the field is "
  "mostly identifying their rock-forming minerals: light minerals (quartz, "
  "feldspar) versus dark (olivine, pyroxene, amphibole, biotite) set the "
  "color index that classifies igneous rocks. Every geology student learns "
  "these minerals first because every rock description is written in their "
  "names."),
 "how_it_works": (
  "Working with rock-forming minerals means estimating their proportions. "
  "In hand sample, compare light versus dark minerals by area: a granite "
  "with 30% quartz, 60% feldspar, and 10% dark minerals plots in the "
  "granite field of the QAP classification triangle. In thin section, point-"
  "counting — tallying which mineral sits under the crosshair at hundreds "
  "of points — gives modal percentages accurate to a few percent. "
  "Identification leans on the diagnostic handful: quartz (glassy, no "
  "cleavage, hardness 7), orthoclase (two cleavages at 90°, often pink), "
  "plagioclase (striated twins), muscovite (colorless sheets), biotite "
  "(dark sheets), hornblende (dark, 56°/124° cleavage), augite (dark, 90° "
  "cleavage), olivine (olive-green, granular, no cleavage). Weathering "
  "transforms the assemblage predictably — feldspar to clay, olivine to "
  "serpentine — so alteration products also identify the original rock."),
 "key_points": [
  "About a dozen minerals build nearly all of Earth's crust; feldspar alone ~60%",
  "Rock-forming status comes from abundance, not rarity or beauty",
  "Light vs dark mineral ratio (color index) classifies igneous rocks",
  "Field ID uses the diagnostic handful: quartz, feldspars, micas, amphibole, pyroxene, olivine",
  "QAP triangle plots quartz-alkali feldspar-plagioclase proportions",
  "Weathering products (clay, serpentine) identify the original minerals",
 ],
 "requirements": [
  "A study set of the ~12 key rock-forming minerals",
  "Hand lens and streak plate for the diagnostic tests",
  "The QAP classification triangle for igneous naming",
  "Practice estimating percentages by eye against reference charts",
 ],
 "standards": [
  "QAP modal classification (IUGS) for plutonic rocks",
  "Color-index conventions for igneous classification",
 ],
 "citations": [CIT_DEER, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: the crust reduced to his original dozen — a minimal "
  "working set of minerals whose proportions name every rock, with the "
  "QAP triangle as the naming machine."),
 "demo_kind": "qap_classify",
},
{
 "key": "ore-minerals", "name": "Ore Minerals: Where Metals Come From",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Ore minerals are the economically workable sources of metals: galena "
  "(PbS) for lead, sphalerite (ZnS) for zinc, chalcopyrite (CuFeS2) for "
  "copper, hematite (Fe2O3) and magnetite (Fe3O4) for iron, bauxite "
  "(gibbsite/boehmite) for aluminum, cassiterite (SnO2) for tin, and native "
  "gold and platinum-group minerals for precious metals. Most are sulfides "
  "and oxides with metallic luster and high specific gravity — properties "
  "that made them findable long before chemistry existed. An ore is an "
  "economic concept, not just a mineralogical one: a rock is ore only if "
  "the metal can be extracted at a profit, so grade (metal percentage), "
  "tonnage, and processing cost decide. A 1% copper deposit can be ore at "
  "today's prices and waste rock at yesterday's. Ore minerals form where "
  "geological processes concentrate dispersed metals a thousandfold — "
  "hydrothermal veins, magmatic sulfide layers, sedimentary precipitates, "
  "and weathering-enriched zones."),
 "how_it_works": (
  "Evaluating an ore mineral deposit works through grade-tonnage arithmetic. "
  "Assay the rock to get the metal grade (percent or grams per tonne), "
  "multiply by the tonnage of the mineralized body to get contained metal, "
  "then subtract mining, crushing, and refining costs at current metal "
  "prices to find the cutoff grade — material above it is ore, below it is "
  "waste. Mineralogy decides the processing: sulfide ores float in froth-"
  "flotation circuits and roast or smelt; oxide ores leach in acid or "
  "cyanide; the grain size of the ore mineral sets how finely the rock must "
  "be ground to liberate it. Exploration reads the mineralogy outward — "
  "alteration halos of chlorite, sericite, and clay around a vein system "
  "point toward the center, and gossans (rusty oxidized caps) mark sulfide "
  "bodies below. Every step, from discovery to the smelter, is applied "
  "mineralogy."),
 "key_points": [
  "Ore minerals: galena→lead, sphalerite→zinc, chalcopyrite→copper, hematite/magnetite→iron",
  "Mostly sulfides and oxides with metallic luster and high SG",
  "Ore is economic: grade × tonnage × price − costs decides, not mineralogy alone",
  "1% copper can be ore today and waste tomorrow — price sets the cutoff",
  "Mineralogy chooses the processing: flotation, smelting, leaching",
  "Alteration halos and gossans are the mineralogical pathfinders to buried ore",
 ],
 "requirements": [
  "Ore-mineral specimen set (galena, sphalerite, chalcopyrite, hematite, magnetite)",
  "Assay concepts: grade, grams per tonne, cutoff grade",
  "Basic economics: commodity prices and processing costs",
  "Understanding that 'ore' is a moving economic target",
 ],
 "standards": [
  "Ore/reserve reporting conventions (grade, tonnage, cutoff)",
  "Mineral-processing selection by ore mineralogy (flotation, leach, smelt)",
 ],
 "citations": [CIT_KLEIN, CIT_STD],
 "sig_lens": (
  "Signature edition: ore as his original concentration equation — "
  "geological processes multiply dispersed metals a thousandfold, and "
  "grade-times-tonnage-minus-cost decides what counts as treasure."),
 "demo_kind": "ore_grade",
},
{
 "key": "igneous-formation", "name": "Igneous Crystallization: Bowen's Reaction Series",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Bowen's reaction series (1928) orders the crystallization of minerals "
  "from a cooling magma: the discontinuous branch runs olivine → pyroxene "
  "→ amphibole → biotite, the continuous branch runs calcium-rich "
  "plagioclase → sodium-rich plagioclase, and both converge on orthoclase, "
  "muscovite, and finally quartz. Early minerals are magnesium- and "
  "iron-rich and crystallize hot; late minerals are silica- and alkali-rich "
  "and crystallize cool. As early crystals settle out (fractional "
  "crystallization), the remaining melt grows more silicic — the mechanism "
  "that differentiates one basaltic magma into gabbro, diorite, and "
  "granite. The series also runs backward as a weathering guide: minerals "
  "that crystallize first weather first, which is why olivine alters to "
  "serpentine while quartz endures as sand. Bowen derived it from "
  "laboratory melts, and a century of petrology has confirmed it as the "
  "master sequence of igneous mineralogy."),
 "how_it_works": (
  "Applying the series works by reading a rock's minerals as a cooling "
  "history. List the minerals present and place each on the series: olivine "
  "plus calcic plagioclase means early, hot crystallization (a gabbro or "
  "basalt); quartz plus orthoclase plus sodic plagioclase means late, cool "
  "crystallization (a granite or rhyolite). Check reaction relationships — "
  "olivine rimmed by pyroxene records the discontinuous reaction where "
  "early olivine reacted with the melt to make pyroxene. Use the series to "
  "predict the missing: a rock with amphibole but no pyroxene crystallized "
  "past the pyroxene stage. For weathering, reverse it: the first minerals "
  "to crystallize are the least stable at Earth's surface, so an olivine "
  "basalt weathers far faster than a quartz granite. The series is a "
  "sequence, not a law — water content and pressure shift positions — but "
  "as a first-order predictor it rarely misleads."),
 "key_points": [
  "Discontinuous branch: olivine → pyroxene → amphibole → biotite (hot to cool)",
  "Continuous branch: Ca-plagioclase → Na-plagioclase",
  "Both branches converge: orthoclase → muscovite → quartz (last to crystallize)",
  "Fractional crystallization differentiates basaltic magma toward granite",
  "Reversed, the series predicts weathering order: olivine first, quartz last",
  "Reaction rims (olivine cored by pyroxene) record the series in action",
 ],
 "requirements": [
  "Bowen's reaction series diagram (discontinuous + continuous branches)",
  "Specimens spanning gabbro/basalt to granite/rhyolite",
  "Thin-section or hand-lens practice spotting reaction rims",
  "Understanding that water and pressure shift the sequence",
 ],
 "standards": [
  "Bowen's reaction series (Bowen 1928) as the igneous crystallization reference",
  "IUGS rock naming tied to the mineral assemblages the series predicts",
 ],
 "citations": [CIT_BOWEN, CIT_DEER],
 "sig_lens": (
  "Signature edition: Bowen's series as his original cooling clock — one "
  "magma, one sequence, readable forward as crystallization history and "
  "backward as weathering destiny."),
 "demo_kind": "bowen_order",
},
{
 "key": "sedimentary-metamorphic", "name": "Sedimentary and Metamorphic Mineral Formation",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Sedimentary minerals form at Earth's surface: evaporites (halite, gypsum) "
  "precipitate as water evaporates, carbonates (calcite, dolomite, aragonite) "
  "grow in warm seas and from shells, and clays form as feldspars weather. "
  "Metamorphic minerals form when heat and pressure rebuild rocks without "
  "melting them: shale becomes slate, then schist (garnet, staurolite, "
  "kyanite appear in sequence), then gneiss (sillimanite). Index minerals "
  "mark the grade — chlorite at low grade, garnet at medium, sillimanite at "
  "high — so a metamorphic rock's minerals are a thermometer and barometer "
  "combined. The classic Barrovian sequence (chlorite → biotite → garnet → "
  "staurolite → kyanite → sillimanite) maps increasing temperature across "
  "entire mountain belts. Together these environments make the minerals "
  "that igneous processes cannot: the salts, the cements, and the "
  "high-pressure assemblages of deep crust."),
 "how_it_works": (
  "Reading sedimentary formation works by evaporation and precipitation "
  "chemistry: as seawater evaporates, minerals drop out in solubility order — "
  "calcite first, then gypsum, then halite, then potassium salts — so a "
  "layered evaporite deposit records a drying sea. Metamorphic reading "
  "works by index minerals and facies: identify the highest-grade index "
  "mineral present (kyanite outranks garnet, sillimanite outranks kyanite) "
  "to bracket the temperature, and use pressure-sensitive pairs — kyanite "
  "versus andalusite versus sillimanite are the same composition Al2SiO5 "
  "in three structures stable at different pressures — to bracket depth. "
  "Plot the assemblage on a petrogenetic grid: the mineral combination "
  "chlorite+muscovite+quartz pins greenschist facies, while "
  "garnet+clinopyroxene+quartz pins eclogite facies. Each assemblage is an "
  "equilibrium answer to its pressure-temperature conditions."),
 "key_points": [
  "Evaporites precipitate in solubility order: calcite → gypsum → halite → K-salts",
  "Metamorphic index minerals mark grade: chlorite (low) → garnet → kyanite → sillimanite (high)",
  "Barrovian sequence maps temperature across mountain belts",
  "Al2SiO5 polymorphs (kyanite/andalusite/sillimanite) are pressure indicators",
  "Metamorphic facies (greenschist, amphibolite, eclogite) name P-T assemblages",
  "Each assemblage is the equilibrium answer to its conditions",
 ],
 "requirements": [
  "Evaporite and carbonate specimens (halite, gypsum, calcite, dolomite)",
  "Metamorphic grade series specimens (slate → schist → gneiss)",
  "Barrovian index-mineral chart and a petrogenetic grid",
  "Ability to spot index minerals (garnet, staurolite, kyanite) in hand sample",
 ],
 "standards": [
  "Metamorphic facies definitions (Eskola) and Barrovian zones",
  "Evaporite precipitation sequence per experimental solubility data",
 ],
 "citations": [CIT_DEER, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: sedimentary and metamorphic minerals as his original "
  "P-T recorder — every assemblage a solved equilibrium, every index "
  "mineral a tick mark on Earth's buried thermometer."),
 "demo_kind": "metamorphic_grade",
},
{
 "key": "hydrothermal-pegmatite", "name": "Hydrothermal Veins and Pegmatites",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Hydrothermal veins form when hot water — heated by magma or deep "
  "circulation — dissolves metals and silica, rises through fractures, and "
  "drops its load as it cools: quartz veins laced with gold, calcite veins, "
  "and the great sulfide veins carrying galena, sphalerite, and "
  "chalcopyrite. Temperature zones the deposition: high-temperature "
  "minerals (cassiterite, wolframite) near the heat source, "
  "lower-temperature ones (stibnite, cinnabar) farther out. Pegmatites are "
  "the extreme end-member — the last water-rich dregs of a granite magma, "
  "crystallizing into giant crystals: meter-long spodumene, gem tourmaline "
  "and beryl, and the lithium, cesium, and tantalum minerals the modern "
  "battery and electronics industries mine. A single pegmatite can zone "
  "from a feldspar-quartz border through a mica-rich wall into a quartz "
  "core, concentrating rare elements a hundredfold over the parent granite."),
 "how_it_works": (
  "Prospecting hydrothermal systems works by following the temperature "
  "gradient. Map the vein minerals outward from the heat source: "
  "high-temperature assemblages (quartz + cassiterite + wolframite) mark "
  "the hot core, grading to intermediate (galena + sphalerite + "
  "chalcopyrite) and distal low-temperature suites (stibnite, cinnabar, "
  "barite). Fluid-inclusion thermometry — measuring the homogenization "
  "temperature of microscopic trapped fluids — gives the actual deposition "
  "temperature. For pegmatites, read the internal zoning: the border zone "
  "crystallized first against the wall rock, the wall zone next, and the "
  "quartz core last, with rare-element minerals (spodumene, beryl, "
  "tourmaline, columbite-tantalite) concentrated in the intermediate zones. "
  "Sample systematically across the zones, because the economic minerals "
  "hide in specific shells of the zoned body, not everywhere."),
 "key_points": [
  "Hydrothermal veins: hot fluids cool in fractures, depositing quartz, gold, sulfides",
  "Deposition zones by temperature: cassiterite/wolframite (hot) → galena/sphalerite → stibnite/cinnabar (cool)",
  "Pegmatites: water-rich final granite melts with giant crystals",
  "Pegmatites concentrate Li, Cs, Ta — the battery/electronics metals",
  "Internal zoning (border → wall → intermediate → core) locates the economic minerals",
  "Fluid inclusions give actual deposition temperatures",
 ],
 "requirements": [
  "Vein specimens showing quartz-sulfide and zoned mineralization",
  "A temperature-zonation chart for hydrothermal minerals",
  "Pegmatite zone diagram (border/wall/intermediate/core)",
  "Hand lens for spotting rare-element minerals in pegmatite zones",
 ],
 "standards": [
  "Hydrothermal temperature-zonation conventions",
  "Pegmatite internal-structure nomenclature (Cameron et al. tradition)",
 ],
 "citations": [CIT_KLEIN, CIT_STD],
 "sig_lens": (
  "Signature edition: veins and pegmatites as his original concentration "
  "machines — hot fluids and final melts distilling dispersed elements "
  "into zoned, minable shells."),
 "demo_kind": "vein_zoning",
},
{
 "key": "polarizing-microscope", "name": "Optical Mineralogy: The Polarizing Microscope",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The polarizing (petrographic) microscope is mineralogy's central "
  "instrument: it shines polarized light through a 30-micron thin section "
  "of rock and reveals each mineral's optical fingerprint. Two polarizing "
  "filters — polarizer below, analyzer above — plus a rotating stage and "
  "compensator plates let the mineralogist measure refractive indices, "
  "birefringence, extinction angles, and interference figures. In "
  "plane-polarized light you read color, pleochroism, habit, cleavage, and "
  "relief; with the analyzer in (crossed polars) you read birefringence "
  "colors, extinction behavior, and twinning. A quartz grain shows low "
  "gray-white interference colors and undulose extinction; plagioclase "
  "shows polysynthetic twinning stripes; olivine blazes with high-order "
  "colors. Generations of geologists have identified every common mineral "
  "this way, and the skills transfer directly to quality control in "
  "ceramics, cement, and materials labs."),
 "how_it_works": (
  "Working the microscope follows a fixed routine. Start in plane-polarized "
  "light: note the mineral's color and whether it changes on stage rotation "
  "(pleochroism), its relief against neighbors (high relief = high refractive "
  "index), its shape and cleavage traces. Insert the analyzer for crossed "
  "polars: read the interference color and match it to the Michel-Lévy chart "
  "to get retardation, rotate to extinction and measure the extinction angle "
  "against cleavage or twin planes (diagnostic for feldspars and pyroxenes). "
  "Insert the Bertrand lens to view the interference figure — uniaxial "
  "minerals (quartz, calcite) show a centered cross, biaxial minerals "
  "(feldspar, mica) show curved isogyres — and count how the figure opens "
  "to estimate the optic angle 2V. Each observation eliminates candidates "
  "until one mineral fits all the optics."),
 "key_points": [
  "Polarizing microscope: the central instrument of optical mineralogy",
  "Plane-polarized light: color, pleochroism, relief, habit, cleavage",
  "Crossed polars: interference colors, extinction angles, twinning",
  "Interference figures distinguish uniaxial (cross) from biaxial (curved isogyres) minerals",
  "30-micron thin sections are the standard preparation",
  "Fixed routine: PPL observations → crossed-polars → interference figure",
 ],
 "requirements": [
  "Access to a polarizing microscope with rotating stage and Bertrand lens",
  "Thin sections of common rocks (granite, basalt, schist)",
  "Michel-Lévy interference color chart",
  "Practice time: optical ID is a trained skill, not a lookup",
 ],
 "standards": [
  "Standard 30-micron thin-section thickness",
  "Michel-Lévy chart retardation conventions",
 ],
 "citations": [CIT_NESSE, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: the polarizing microscope as his original "
  "light-interrogation engine — a fixed routine that squeezes a mineral's "
  "full optical fingerprint out of polarized light and a thin slice."),
 "demo_kind": "microscope_routine",
},
{
 "key": "refractive-index", "name": "Refractive Index and Birefringence",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Refractive index (n) measures how much a mineral slows light: diamond's "
  "2.42 bends light so strongly it sparkles, quartz's 1.55 is modest, and "
  "fluorite's 1.43 is low. Relief in thin section is refractive index made "
  "visible — a high-index mineral like garnet (1.72–1.89) stands out boldly "
  "against mounting medium (1.54), while quartz nearly vanishes. "
  "Birefringence is the difference between a mineral's highest and lowest "
  "indices: calcite's extreme 0.172 splits images visibly (the famous double "
  "refraction of Iceland spar), quartz's mild 0.009 gives first-order gray "
  "interference colors, and cubic minerals like garnet have zero "
  "birefringence — one index in all directions. Measuring n by the Becke "
  "line method or by immersion oils identifies minerals precisely: olivine "
  "(1.65–1.69) versus quartz (1.54–1.55) is unmistakable in matched oils."),
 "how_it_works": (
  "The Becke line method measures refractive index without instruments "
  "beyond the microscope. Mount the grain in an oil of known n, focus "
  "slightly above the grain boundary, and watch the bright Becke line: it "
  "moves into the higher-index medium as you raise focus. If the line moves "
  "into the grain, the grain's n exceeds the oil's — switch to a higher oil "
  "and repeat until the line disappears, meaning the indices match. For "
  "birefringence, measure the highest and lowest indices the same way "
  "(rotating the stage for anisotropic grains) and subtract: δ = n_high − "
  "n_low. Retardation then follows as thickness × birefringence, linking "
  "this measurement directly to the interference colors on the Michel-Lévy "
  "chart. Immersion sets with 0.002-spaced oils give laboratory precision; "
  "relief estimation gives field-grade answers in seconds."),
 "key_points": [
  "Refractive index: light-slowing power — diamond 2.42, quartz 1.55, fluorite 1.43",
  "Relief in thin section is refractive index made visible",
  "Birefringence δ = n_high − n_low: calcite 0.172 (extreme), quartz 0.009 (mild), garnet 0",
  "Becke line method: match the grain against calibrated immersion oils",
  "Retardation = thickness × birefringence — links to interference colors",
  "Cubic minerals are isotropic: single index, zero birefringence",
 ],
 "requirements": [
  "Calibrated immersion oil set (or a few key oils around 1.54)",
  "Polarizing microscope for Becke line observation",
  "Grain mounts of unknowns plus reference minerals",
  "Patience: matching to 0.002 takes careful focus work",
 ],
 "standards": [
  "Refractive index reported at sodium D wavelength unless noted",
  "Becke line and immersion-oil conventions (Emmons standard)",
 ],
 "citations": [CIT_NESSE, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: refractive index as his original light-speed "
  "fingerprint — one number per vibration direction, measured by watching "
  "a bright line choose sides at a grain boundary."),
 "demo_kind": "becke_line",
},
{
 "key": "pleochroism-interference", "name": "Pleochroism and Interference Colors",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Pleochroism is color change on rotation in plane-polarized light: "
  "biotite shifts from pale tan to deep brown, hornblende from yellow-green "
  "to blue-green, tourmaline from colorless to saturated color. It happens "
  "because anisotropic minerals absorb different wavelengths along different "
  "vibration directions — one mineral, two or three directional colors. "
  "Interference colors appear under crossed polars: the mineral splits light "
  "into two rays traveling at different speeds, and their recombination "
  "cancels some wavelengths, painting the grain in Newton's scale colors — "
  "first-order gray, white, yellow, red; second-order blues and greens; "
  "third-order pinks. The Michel-Lévy chart maps color to retardation in "
  "nanometers: retardation equals thickness times birefringence, so a "
  "30-micron quartz grain (δ=0.009) shows ~270 nm — first-order gray-white. "
  "Reading these colors is quantitative optics done by eye."),
 "how_it_works": (
  "Testing pleochroism works in plane-polarized light: center the grain, "
  "rotate the stage through 90°, and watch for color change — two colors "
  "means dichroic (uniaxial), three means trichroic (biaxial), none means "
  "isotropic or non-pleochroic. Record the colors at the extremes; the "
  "pleochroic formula (e.g., X=pale yellow, Z=blue-green for hornblende) is "
  "diagnostic. For interference colors, insert the analyzer, find the "
  "grain's maximum color at 45° to extinction, and match it on the "
  "Michel-Lévy chart: read retardation in nanometers off the color, divide "
  "by the known 30-micron thickness to get birefringence. Insert a "
  "first-order-red compensator to determine sign and to resolve "
  "high-order whites: if the color climbs the chart with the compensator "
  "in, retardation adds. Anomalous colors (Berlin blue, anomalous brown) "
  "flag dispersion quirks worth noting."),
 "key_points": [
  "Pleochroism: directional color change in PPL — biotite, hornblende, tourmaline",
  "Dichroic (2 colors) = uniaxial; trichroic (3) = biaxial",
  "Interference colors under crossed polars follow Newton's scale orders",
  "Michel-Lévy chart converts color → retardation (nm)",
  "Retardation = thickness × birefringence: quartz at 30µm ≈ 270 nm (first-order gray-white)",
  "Compensator plates determine sign and resolve high-order colors",
 ],
 "requirements": [
  "Polarizing microscope with rotating stage and compensator slot",
  "Michel-Lévy chart (printed or digital)",
  "First-order-red (gypsum) compensator plate",
  "Thin sections with pleochroic minerals (biotite schist, hornblende gabbro)",
 ],
 "standards": [
  "Pleochroic formula notation (X/Y/Z colors)",
  "Michel-Lévy retardation scale in nanometers",
 ],
 "citations": [CIT_NESSE, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: pleochroism and interference as his original "
  "directional-color readout — rotate the stage and the mineral reports "
  "its vibration directions in color, quantified on the Michel-Lévy scale."),
 "demo_kind": "retardation_calc",
},
{
 "key": "gemstones", "name": "Gemstones: Properties, Cutting, and Value",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "A gemstone is a mineral (occasionally a mineraloid like opal or an "
  "organic like pearl and amber) valued for beauty, durability, and rarity. "
  "Durability is hardness plus toughness: diamond (10) is hardest but "
  "cleaves, while jade (6.5–7) is far tougher. The great species — diamond, "
  "corundum (ruby, sapphire), beryl (emerald, aquamarine), chrysoberyl "
  "(alexandrite), spinel, topaz, tourmaline, garnet, peridot (olivine), "
  "zircon — each combine a crystal structure that takes a polish with "
  "optical properties that return light. Cutting is applied optics: facet "
  "angles are computed from the refractive index so light entering the "
  "crown reflects internally and exits back to the eye — diamond's 2.42 "
  "index demands different angles than quartz's 1.54. Value follows the "
  "four Cs for diamond (carat, color, clarity, cut) and analogous quality "
  "factors for colored stones, with origin and treatment disclosure "
  "governing the trade."),
 "how_it_works": (
  "Evaluating a gemstone works through the quality factors in order. Weigh "
  "it: one carat is exactly 0.2 grams. Grade color by hue, tone, and "
  "saturation against master stones — for colored gems, vivid saturation "
  "commands the premium. Map clarity under 10x: note inclusions' type, "
  "size, and position, since a feather at the girdle threatens durability. "
  "Assess cut by proportions and symmetry: table percentage, crown and "
  "pavilion angles matched to the species' refractive index, polish quality. "
  "Then verify identity and treatment: refractive index and specific gravity "
  "separate natural from synthetic and simulant; magnification reveals "
  "treatment fingerprints like heated-sapphire silk or fracture-filled "
  "clarity enhancement. Document everything, because undisclosed treatment "
  "is the trade's cardinal offense and detection is the gemologist's core "
  "skill."),
 "key_points": [
  "Gemstone = beauty + durability (hardness and toughness) + rarity",
  "Great species: diamond, corundum, beryl, chrysoberyl, spinel, topaz, tourmaline, garnet",
  "Facet angles derive from refractive index — cutting is applied optics",
  "Carat = 0.2 g exactly; the four Cs grade diamonds",
  "RI and SG separate natural, synthetic, and simulant",
  "Treatment disclosure is mandatory; detection is the core gemological skill",
 ],
 "requirements": [
  "10x loupe, refractometer, and specific-gravity setup for basic gem testing",
  "Master color stones or calibrated color references",
  "Knowledge of common treatments and their detection fingerprints",
  "Ethics: disclose everything, assume nothing",
 ],
 "standards": [
  "Carat defined as exactly 0.2 g (metric carat, 1907)",
  "Four-Cs grading and treatment-disclosure trade conventions",
 ],
 "citations": [CIT_GIA, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: gemstones as his original beauty-engineering — "
  "crystal structure plus optics plus rarity, with cutting angles computed "
  "from refractive index and value graded on disclosed quality."),
 "demo_kind": "gem_carat",
},
{
 "key": "hand-sample-id", "name": "Hand-Sample Identification: The Field Workflow",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Hand-sample identification is the systematic field workflow that names an "
  "unknown mineral with simple tools: observe luster first (metallic vs "
  "non-metallic splits the possibilities in half), test hardness with the "
  "Mohs kit, check cleavage and fracture, read the streak, estimate "
  "specific gravity by heft, and note color, habit, and any special traits "
  "(magnetism, taste, fluorescence, acid fizz). Each test eliminates "
  "candidates: metallic luster plus high heft plus cubic cleavage points to "
  "galena; vitreous luster, hardness 7, no cleavage, conchoidal fracture "
  "points to quartz. Dichotomous keys and flow charts formalize the order, "
  "but experienced mineralogists run the sequence from memory. The workflow "
  "ends with confirmation — two independent properties agreeing — never "
  "with a single-test guess. Done well, it identifies the common minerals "
  "in under a minute and flags the genuinely unknown for lab work."),
 "how_it_works": (
  "The workflow runs as an elimination funnel. Step one, luster: metallic "
  "sends you to the ore-mineral branch (then SG and streak decide), "
  "non-metallic to the rock-mineral branch. Step two, hardness: bracket "
  "with nail (5.5) and glass (5.5) — harder-than-steel versus "
  "softer-than-fingernail halves the field again. Step three, cleavage: "
  "count directions and measure angles (mica's one perfect, feldspar's two "
  "at 90°, calcite's three not at 90°). Step four, streak and special "
  "tests: hematite's red-brown streak, magnetite's magnetism, calcite's "
  "acid fizz, halite's salty taste. Record every result before naming — "
  "the written record catches the step where a guess jumped ahead of "
  "evidence. When two properties disagree, trust the more diagnostic one "
  "(cleavage over color, streak over luster on weathered specimens) and "
  "re-test the other."),
 "key_points": [
  "Elimination funnel: luster → hardness → cleavage → streak → special tests",
  "Metallic vs non-metallic luster halves the possibilities instantly",
  "Two independent agreeing properties confirm; one test never names a mineral",
  "Trust hierarchy: cleavage and streak beat color and weathered luster",
  "Special tests: magnetite (magnetic), calcite (acid fizz), halite (taste)",
  "Record every result — the log catches jumped-to conclusions",
 ],
 "requirements": [
  "Field kit: Mohs tools, streak plate, hand lens, dilute HCl, magnet",
  "A dichotomous key or flowchart for the local mineral suite",
  "Practice set of 20+ labeled specimens to calibrate judgment",
  "Notebook discipline: write results before naming",
 ],
 "standards": [
  "Standard hand-sample test sequence (luster/hardness/cleavage/streak/SG)",
  "Confirmation rule: two independent diagnostic properties minimum",
 ],
 "citations": [CIT_KLEIN, CIT_DANA],
 "sig_lens": (
  "Signature edition: field ID as his original elimination engine — a "
  "five-step funnel that halves the possibilities at every test and "
  "refuses to name a mineral on a single guess."),
 "demo_kind": "id_funnel",
},

# ------------------------------------------------------------------ ADVANCED
{
 "key": "bragg-law", "name": "X-Ray Diffraction: Bragg's Law and the Unit Cell",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "X-ray diffraction reads crystal structure directly from geometry. When "
  "X-rays of wavelength λ strike lattice planes spaced d apart, constructive "
  "interference occurs exactly when Bragg's law holds: nλ = 2d·sinθ, where θ "
  "is the angle between the ray and the planes and n is the diffraction "
  "order. Each set of planes (hkl) diffracts at its own angle, so the "
  "pattern of spots or powder rings encodes the plane spacings, and the "
  "spacings encode the unit-cell dimensions. A powder diffractometer "
  "sweeps θ and records intensity versus angle; matching the peak positions "
  "against reference patterns identifies the mineral — the basis of the "
  "Powder Diffraction File used in labs worldwide. Bragg's 1913 insight "
  "turned crystals into their own spectrometers: from a list of angles, the "
  "unit cell (a, b, c, α, β, γ) can be computed, and no two minerals share "
  "exactly the same cell. It remains the definitive mineral identification "
  "method when optics and chemistry are ambiguous."),
 "how_it_works": (
  "Running a powder identification works in four steps. Mount the ground "
  "powder, scan 2θ, and read each peak's angle; convert with Bragg's law, "
  "d = λ/(2·sinθ), using the tube's wavelength (copper Kα: 1.5406 Å). Index "
  "the pattern: assign (hkl) to peaks and refine the cell parameters by "
  "least squares until calculated angles match observed ones. Then search-"
  "match: compare the d-spacing/intensity list against the reference "
  "database, scoring on the strongest lines — the Hanawalt method uses the "
  "three strongest peaks as the lookup key. Confirm with chemistry or "
  "optics if the match is close but not exact, since solid solution shifts "
  "peaks systematically. Modern instruments do all of this in software, but "
  "the mineralogist still checks the fit: a mis-indexed pattern is a "
  "misidentified mineral."),
 "key_points": [
  "Bragg's law nλ = 2d·sinθ: each plane set (hkl) diffracts at its own angle",
  "Peak positions encode plane spacings; spacings encode the unit cell",
  "Powder patterns identify minerals by search-matching reference files",
  "Copper Kα wavelength 1.5406 Å is the workhorse radiation",
  "No two minerals share exactly the same unit cell — definitive identification",
  "Solid solution shifts peaks systematically; chemistry confirms close matches",
 ],
 "requirements": [
  "Powder diffractometer access (or a service lab)",
  "Finely ground, representative powder mount",
  "Reference pattern database for search-matching",
  "Bragg's-law fluency: converting 2θ to d-spacing by hand",
 ],
 "standards": [
  "Bragg's law (Bragg & Bragg 1913) as the diffraction foundation",
  "Powder Diffraction File search-match conventions (Hanawalt three-strongest-lines)",
 ],
 "citations": [CIT_BRAGG, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: Bragg's law as his original crystal spectrometer — "
  "the crystal diffracts its own structure into angles, and one equation "
  "converts angles back into the unit cell."),
 "demo_kind": "bragg_calc",
},
{
 "key": "structure-determination", "name": "Crystal Structure Determination",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Structure determination goes beyond the unit cell to find where every "
  "atom sits: the fractional coordinates (x, y, z) of each site. Peak "
  "positions give the lattice, but peak intensities encode the atom "
  "positions through the structure factor — the summed scattering of all "
  "atoms with their phase shifts. The phase problem (intensities record "
  "amplitudes, not phases) is solved by Patterson methods, direct methods, "
  "or charge flipping, and the resulting electron-density map is fitted "
  "with atoms until calculated and observed intensities agree (the "
  "R-factor, good structures refine below 5%). Pauling's rules then sanity-"
  "check the result: cations sit in coordination polyhedra sized to their "
  "radius ratio, and shared polyhedral edges obey electrostatic valence "
  "sums. A solved structure explains the mineral completely — its cleavage "
  "(weak planes in the structure), its optics (directional bonding), its "
  "stability — which is why structure solution is mineralogy's highest "
  "analytical art."),
 "how_it_works": (
  "Solving a structure follows the standard pipeline. Collect single-"
  "crystal diffraction data — thousands of measured intensities with their "
  "(hkl) indices. Solve the phase problem with direct methods to get a "
  "first electron-density map, locate the heaviest atoms (they dominate "
  "scattering), then find lighter atoms in difference maps. Refine by least "
  "squares: adjust coordinates and thermal parameters to minimize the "
  "difference between observed and calculated structure factors, watching "
  "the R-factor fall. Validate with Pauling's rules — check radius ratios "
  "predict the observed coordination (0.225–0.414 for tetrahedral, "
  "0.414–0.732 for octahedral), verify bond-valence sums match oxidation "
  "states, and confirm no impossible short contacts. Deposit the final "
  "coordinates: a solved structure is permanent, checkable data."),
 "key_points": [
  "Positions give the lattice; intensities give the atom positions via the structure factor",
  "Phase problem solved by direct methods, Patterson, or charge flipping",
  "R-factor below ~5% marks a good refinement",
  "Pauling's rules validate: radius ratios set coordination, bond valences sum correctly",
  "A solved structure explains cleavage, optics, and stability from first principles",
  "Structure solution is mineralogy's highest analytical art",
 ],
 "requirements": [
  "Single-crystal diffractometer and structure-solution software",
  "A suitable crystal (0.1–0.3 mm, untwinned, undamaged)",
  "Pauling's rules and bond-valence tables for validation",
  "Crystallographic training: space groups and refinement practice",
 ],
 "standards": [
  "Structure-factor formalism and R-factor reporting conventions",
  "Pauling's rules (1929) for structural validation",
 ],
 "citations": [CIT_PAULING, CIT_BRAGG],
 "sig_lens": (
  "Signature edition: structure solution as his original atomic "
  "cartography — phases recovered from intensities, atoms placed in "
  "electron density, Pauling's rules as the independent audit."),
 "demo_kind": "structure_factor",
},
{
 "key": "solid-solution", "name": "Solid Solution and Polymorphism",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Solid solution lets one mineral span a compositional range: olivine "
  "runs continuously from forsterite (Mg2SiO4) to fayalite (Fe2SiO4) as Mg "
  "and Fe swap freely on the same sites, and plagioclase runs from albite "
  "(NaAlSi3O8) to anorthite (CaAl2Si2O8) by coupled NaSi↔CaAl substitution. "
  "Complete series need similar ionic size and charge; where the mismatch "
  "is too great, a solvus (miscibility gap) opens — alkali feldspars "
  "unmix into perthite intergrowths on cooling. Polymorphism is the mirror "
  "phenomenon: identical composition, different structures — diamond and "
  "graphite (C), quartz/tridymite/cristobalite (SiO2), calcite/aragonite "
  "(CaCO3), and the Al2SiO5 trio (kyanite/andalusite/sillimanite). "
  "Polymorphs interconvert at specific pressures and temperatures, making "
  "them geological thermometers and barometers. Together, solid solution "
  "and polymorphism explain why mineral chemistry is ranges, not points, "
  "and why structure determines which composition can exist where."),
 "how_it_works": (
  "Analyzing a solid solution works by locating the composition between "
  "endmembers. Measure the composition (electron microprobe), express it "
  "as endmember percentages — Fo80Fa20 for an olivine with 80% forsterite — "
  "and interpolate properties: unit-cell edges, refractive indices, and "
  "density vary nearly linearly with composition (Vegard's law), so a "
  "measured cell edge reads out the composition without chemistry. Check "
  "for exsolution: perthitic feldspar or pyroxene lamellae under the "
  "microscope reveal a solvus crossed on cooling, and the lamellae "
  "compositions bracket the original homogeneous composition. For "
  "polymorphs, identify the structure by X-ray (composition is identical, "
  "so chemistry cannot help), then place the P-T conditions on the phase "
  "diagram: finding coesite (high-pressure SiO2) in a rock proves "
  "ultrahigh-pressure metamorphism. Compositional ranges and structural "
  "alternatives together map the conditions of formation."),
 "key_points": [
  "Solid solution: one structure, continuous composition range (olivine Fo–Fa, plagioclase Ab–An)",
  "Complete series need matched ionic size and charge; mismatch opens a solvus",
  "Perthite intergrowths record unmixing on cooling",
  "Polymorphism: same composition, different structures (diamond/graphite, calcite/aragonite)",
  "Polymorphs are P-T indicators: coesite proves ultrahigh pressure",
  "Vegard's law: cell edges and optics interpolate linearly between endmembers",
 ],
 "requirements": [
  "Electron microprobe or equivalent for quantitative composition",
  "Endmember-interpolation tables (Vegard's-law curves)",
  "X-ray diffraction to distinguish polymorphs (chemistry cannot)",
  "Phase diagrams for the relevant P-T stability fields",
 ],
 "standards": [
  "Endmember nomenclature (Fo/Fa, Ab/An conventions)",
  "Vegard's-law interpolation practice",
 ],
 "citations": [CIT_DEER, CIT_PAULING],
 "sig_lens": (
  "Signature edition: solid solution and polymorphism as his original "
  "composition-structure duality — chemistry slides along ranges while "
  "structure jumps between alternatives, each encoding formation "
  "conditions."),
 "demo_kind": "solid_solution",
},
{
 "key": "mineral-thermodynamics", "name": "Thermodynamics of Mineral Stability",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Thermodynamics decides which minerals exist at given conditions: the "
  "stable assemblage is the one with the lowest Gibbs free energy, "
  "G = H − TS. Every mineral reaction — kyanite converting to sillimanite "
  "with heating, calcite plus quartz reacting to wollastonite plus CO2 — "
  "has a free-energy change ΔG that goes negative exactly where the "
  "reaction runs forward. The Clapeyron equation, dP/dT = ΔS/ΔV, gives the "
  "slope of every reaction boundary on a phase diagram from measurable "
  "entropy and volume changes. Metastability explains the exceptions: "
  "diamond persists at the surface for billions of years because the "
  "graphite conversion is kinetically blocked, not because diamond is "
  "stable there. Geothermobarometry inverts the logic — measuring mineral "
  "compositions (like garnet-biotite Fe-Mg exchange) to compute the "
  "temperature and pressure where the rock equilibrated. Thermodynamics "
  "turns mineral assemblages into quantitative Earth history."),
 "how_it_works": (
  "Computing stability works from thermodynamic data tables. For a reaction, "
  "sum the formation free energies of products minus reactants to get ΔG "
  "at the conditions of interest; negative ΔG means the products are "
  "stable. Add temperature and pressure dependence: ΔG(T,P) = ΔH − TΔS + "
  "PΔV (for solids, approximately), and solve for the P-T curve where ΔG "
  "= 0 — that curve is the reaction boundary. For geothermobarometry, use "
  "calibrated exchange reactions: the Fe-Mg distribution between garnet "
  "and biotite shifts predictably with temperature, so measuring both "
  "minerals' compositions with the microprobe yields the equilibration "
  "temperature, while net-transfer reactions involving volume changes yield "
  "pressure. Always check for equilibrium first — zoned or reacted grains "
  "record changing conditions, and only touching, unzoned rims give the "
  "final P-T point."),
 "key_points": [
  "Stable assemblage = lowest Gibbs free energy: G = H − TS",
  "Clapeyron equation dP/dT = ΔS/ΔV gives every reaction boundary's slope",
  "Diamond at the surface is metastable — kinetically blocked, not stable",
  "Garnet-biotite Fe-Mg exchange is the classic geothermometer",
  "Only equilibrated, touching, unzoned rims give valid P-T points",
  "Thermodynamics converts assemblages into quantitative Earth history",
 ],
 "requirements": [
  "Thermodynamic data tables (formation H, S, V per mineral)",
  "Electron microprobe compositions for thermobarometry",
  "Calibrated geothermometer/barometer formulations",
  "Equilibrium assessment: check zoning and reaction textures first",
 ],
 "standards": [
  "Gibbs-energy minimization as the stability criterion",
  "Standard-state conventions for mineral thermodynamic data",
 ],
 "citations": [CIT_PUTNIS, CIT_DEER],
 "sig_lens": (
  "Signature edition: mineral stability as his original energy "
  "accounting — every assemblage the lowest-free-energy answer to its "
  "conditions, every reaction boundary computable from entropy and "
  "volume."),
 "demo_kind": "gibbs_stability",
},
{
 "key": "phase-diagrams", "name": "Phase Diagrams: Reading Mineral Stability Fields",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Phase diagrams map which minerals are stable at which conditions. "
  "P-T diagrams show reaction boundaries as curves — the Al2SiO5 diagram "
  "with its kyanite/andalusite/sillimanite triple point is mineralogy's "
  "most famous. T-X (temperature-composition) diagrams show melting and "
  "crystallization paths: the albite-anorthite loop traces how plagioclase "
  "composition evolves as magma cools, and eutectic diagrams show the "
  "lowest-melting mixture of two components. The lever rule reads any "
  "two-phase field quantitatively: the proportions of the two phases are "
  "the opposite segment lengths on the tie line. The phase rule, "
  "F = C − P + 2, counts the degrees of freedom — at the Al2SiO5 triple "
  "point (one component, three phases) there are zero: that P-T point is "
  "fixed in nature. Reading these diagrams is reading the operating manual "
  "of mineral formation."),
 "how_it_works": (
  "Reading a T-X diagram works by following the cooling path. Start at the "
  "bulk composition on the top axis, drop vertically as temperature falls "
  "until hitting the liquidus — the first crystal composition is read off "
  "the solidus at that temperature. Continue cooling: at each temperature, "
  "draw the horizontal tie line between liquidus and solidus, read the "
  "liquid and solid compositions at its ends, and apply the lever rule — "
  "fraction of solid equals the liquid-side segment over the whole tie "
  "line. On P-T diagrams, plot the observed assemblage and read the "
  "bracketed conditions: kyanite + quartz + muscovite sits in kyanite's "
  "field, pinning moderate pressure. Use the phase rule as a check: if you "
  "count more phases than components + 2 allow at your conditions, "
  "something is not in equilibrium — look for reaction textures or "
  "zoning that explain the excess."),
 "key_points": [
  "P-T diagrams: reaction boundaries as curves; the Al2SiO5 triple point is the icon",
  "T-X diagrams trace crystallization paths (albite-anorthite loop)",
  "Lever rule: phase proportions are opposite tie-line segment lengths",
  "Phase rule F = C − P + 2 counts degrees of freedom",
  "Triple point has zero freedom — that P-T point is fixed in nature",
  "Excess phases over the rule's allowance mean disequilibrium — investigate",
 ],
 "requirements": [
  "Key phase diagrams: Al2SiO5 P-T, Ab-An T-X, eutectic systems",
  "Lever-rule practice on two-phase fields",
  "Phase-rule fluency for equilibrium checking",
  "Petrogenetic grids for multi-reaction assemblages",
 ],
 "standards": [
  "Phase-rule formulation (Gibbs) and variance conventions",
  "Lever-rule and tie-line reading conventions",
 ],
 "citations": [CIT_BOWEN, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: phase diagrams as his original stability maps — "
  "every boundary a computed curve, every field a mineral's territory, "
  "the lever rule a quantitative reader for any point inside."),
 "demo_kind": "lever_rule",
},
{
 "key": "substitution-rules", "name": "Ionic Substitution: Goldschmidt's Rules",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Goldschmidt's rules (1937) predict which ions substitute for each other "
  "in crystal structures: (1) ions of similar radius (within ~15%) "
  "substitute readily — Mg²⁺ (0.72 Å) and Fe²⁺ (0.78 Å) swap freely in "
  "olivine; (2) ions of similar charge substitute more easily, and charge "
  "differences demand coupled substitution — Na⁺+Si⁴⁺ ↔ Ca²⁺+Al³⁺ keeps "
  "plagioclase neutral across the whole series; (3) the smaller, "
  "higher-charged ion enters the crystal preferentially at high "
  "temperature. These rules explain trace-element partitioning: nickel "
  "follows magnesium into olivine, depleting the melt; incompatible "
  "elements (large, highly charged — Zr, rare earths) are rejected by "
  "early crystals and concentrate in late melts and pegmatites. The rules "
  "are why ore deposits exist where they do and why the rare earths travel "
  "together. Every substitution also perturbs the structure measurably — "
  "cell edges shift, refractive indices move — so the rules run backward "
  "too, letting measured properties estimate hidden compositions."),
 "how_it_works": (
  "Applying the rules works as a three-check filter for any proposed "
  "substitution. Check radii first: look up the ionic radii for the "
  "coordination number in question and compute the percentage difference — "
  "under 15% passes freely, 15–30% passes partially at high temperature, "
  "over 30% is essentially blocked. Check charge second: equal charges "
  "substitute directly; unequal charges need a coupled partner elsewhere in "
  "the structure (write the coupled equation and verify neutrality). Check "
  "temperature preference third: at magmatic temperatures the crystal takes "
  "the smaller, higher-charged ion, fractionating the pair between solid "
  "and melt. Use the outcome to predict partitioning — compatible elements "
  "(Ni, Cr, Co) enter early minerals, incompatibles (Rb, Zr, REE) enrich "
  "the residual melt — and to sanity-check microprobe analyses: a reported "
  "substitution violating all three rules is probably an analytical error."),
 "key_points": [
  "Rule 1: similar radii (within ~15%) substitute readily — Mg/Fe in olivine",
  "Rule 2: similar charges substitute directly; differences need coupled substitution",
  "Rule 3: smaller, higher-charged ions enter crystals preferentially when hot",
  "Compatible elements (Ni, Cr) enter early minerals; incompatibles (Zr, REE) enrich late melts",
  "Coupled substitution NaSi↔CaAl carries plagioclase across its whole series",
  "Violations of all three rules flag probable analytical errors",
 ],
 "requirements": [
  "Ionic radius tables by coordination number (Shannon radii)",
  "Charge-balance practice with coupled substitutions",
  "Partition-coefficient concepts for trace-element work",
  "Microprobe data to test predictions against",
 ],
 "standards": [
  "Goldschmidt's rules (1937) as the substitution framework",
  "Shannon ionic radii as the reference dataset",
 ],
 "citations": [CIT_GOLDSCHMIDT, CIT_PAULING],
 "sig_lens": (
  "Signature edition: Goldschmidt's rules as his original substitution "
  "filter — three checks on radius, charge, and temperature that predict "
  "which ions go where and expose bad analyses."),
 "demo_kind": "goldschmidt_check",
},
{
 "key": "gem-treatments", "name": "Gemstone Treatments and Synthetics Detection",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Most gemstones on the market are treated: heating deepens sapphire blue "
  "and reddens ruby, irradiation plus heating makes blue topaz from "
  "colorless, fracture filling hides emerald's cracks with oil or resin, "
  "and diffusion adds a thin color skin to sapphire. Synthetics — "
  "flame-fusion corundum and spinel, hydrothermal quartz and emerald, flux-"
  "grown ruby and alexandrite, CVD and HPHT diamond — are real gem "
  "material grown in labs, distinct from simulants (glass, cubic zirconia) "
  "that merely imitate. Detection is applied mineralogy: curved growth "
  "striae betray flame-fusion synthetics, chevron patterns mark hydrothermal "
  "growth, breadcrumb inclusions flag flux material, and phosphorescence "
  "under UV can expose HPHT diamond. The trade rule is absolute: any "
  "treatment affecting value must be disclosed, and undisclosed treatment "
  "is fraud. The gemologist's instruments — microscope, spectroscope, "
  "refractometer, UV lamp — exist largely to answer one question: is this "
  "stone what it claims to be?"),
 "how_it_works": (
  "Detection follows an evidence ladder from cheap to conclusive. Start "
  "with the loupe and microscope: map inclusions — natural stones show "
  "mineral crystals, healed fractures, and silk; synthetics show curved "
  "striae, nail-head spicules, breadcrumb flux residue, or suspicious "
  "cleanliness. Check spectra: a handheld spectroscope reveals treatment "
  "fingerprints like the 450 nm band of heated sapphire or irradiation "
  "lines in diamond. Test fluorescence and phosphorescence under long- and "
  "short-wave UV — many synthetics and treatments glow distinctively. "
  "Measure properties against natural ranges: flux ruby can show slightly "
  "different SG and RI. For the hard cases, send to a major lab: "
  "photoluminescence, FTIR, and trace-element chemistry (LA-ICP-MS) "
  "resolve origin and treatment where optics cannot. Document the full "
  "evidence chain, because a detection report must convince a skeptical "
  "buyer, not just the examiner."),
 "key_points": [
  "Common treatments: heating (sapphire/ruby), irradiation (topaz), fracture filling (emerald), diffusion",
  "Synthetics are real material, lab-grown; simulants merely imitate",
  "Curved striae = flame fusion; chevrons = hydrothermal; breadcrumbs = flux",
  "Spectroscope, UV fluorescence, and microscopy form the detection ladder",
  "Advanced labs use FTIR, photoluminescence, and trace-element chemistry",
  "Disclosure rule is absolute: undisclosed treatment is fraud",
 ],
 "requirements": [
  "Gemological microscope, spectroscope, UV lamp, refractometer",
  "Reference sets of known natural, treated, and synthetic stones",
  "Inclusion-photograph atlases for pattern matching",
  "Access to a major lab for conclusive hard cases",
 ],
 "standards": [
  "Treatment-disclosure conventions of the gem trade",
  "Detection-report evidence standards (document the full chain)",
 ],
 "citations": [CIT_GIA, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: detection as his original authenticity ladder — "
  "inclusions first, spectra second, lab chemistry last, each rung "
  "raising the cost of faking it."),
 "demo_kind": "treatment_detect",
},
{
 "key": "ima-registry", "name": "The IMA and the Master List of Minerals",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The International Mineralogical Association's Commission on New "
  "Minerals, Nomenclature and Classification (CNMNC) is the gatekeeper of "
  "mineral species: nothing is an official mineral until the commission "
  "approves it. The master list holds about 6,000 valid species, each with "
  "an approved name, formula, type locality, and crystallographic data — "
  "plus lists of discredited names, synonyms, and grandfathered species "
  "(minerals described before the commission existed in 1959, accepted "
  "without modern review). Naming rules are strict: names honor people, "
  "places, or properties, must not duplicate existing names, and follow "
  "suffix conventions for series (-(Ce), -(La) for rare-earth dominance). "
  "The commission also prunes: inadequately described species are "
  "discredited, and redefinitions split or merge species as new data "
  "arrive. Every database, museum catalog, and textbook ultimately answers "
  "to this list — it is the single source of truth for what counts as a "
  "mineral species."),
 "how_it_works": (
  "Using the registry works by lookup and by proposal. To verify a "
  "mineral's status, search the master list for the name: check it is "
  "marked valid (not discredited, not a synonym), read the approved "
  "formula and type locality, and note any redefinition history. To "
  "propose a new species, assemble the full dossier — quantitative "
  "chemistry, X-ray structure or powder pattern, optical and physical "
  "properties, type specimen deposited in a museum — and submit to the "
  "CNMNC, which assigns reviewers and votes; approval typically takes "
  "months. Name the species per the rules: check the proposed name "
  "against the full list for collisions, apply the correct suffixes for "
  "dominant cations or anions, and avoid commercial or frivolous names. "
  "Track grandfathered species with extra care — some pre-1959 names "
  "cover what modern work would split into several species."),
 "key_points": [
  "CNMNC approval is what makes a mineral species official — ~6,000 valid species",
  "Master list carries approved names, formulas, type localities, crystallographic data",
  "Discredited names and synonyms are tracked, not silently dropped",
  "Naming rules: no duplicates, suffix conventions (-(Ce), -(La)), no frivolous names",
  "Grandfathered pre-1959 species accepted without modern review — handle with care",
  "New-species proposals need full chemistry, structure, properties, and a museum type specimen",
 ],
 "requirements": [
  "Access to the IMA master mineral list",
  "Understanding of CNMNC proposal and voting procedures",
  "Naming-rule reference for suffix conventions",
  "Museum-deposition arrangements for type material",
 ],
 "standards": [
  "CNMNC nomenclature rules and approval procedures",
  "Type-specimen deposition requirements",
 ],
 "citations": [CIT_IMA, CIT_STRUNZ],
 "sig_lens": (
  "Signature edition: the IMA list as his original single source of "
  "truth — one gatekeeper, one master list, and a voting procedure that "
  "turns a discovery into an official species."),
 "demo_kind": "ima_checklist",
},
{
 "key": "new-mineral", "name": "Describing a New Mineral: From Discovery to Approval",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Describing a new mineral is mineralogy's full pipeline in one project: "
  "prove the phase is new, characterize it completely, and win CNMNC "
  "approval. It starts with an anomaly — an X-ray pattern that matches "
  "nothing, a microprobe analysis that fits no formula — and proceeds "
  "through quantitative chemistry (electron microprobe for majors, "
  "structure-based methods for light elements), single-crystal or powder "
  "X-ray diffraction for the structure, and measurement of every physical "
  "property: hardness, density, optics, cleavage, color, streak, luster. "
  "The description must demonstrate the mineral is distinct — not a "
  "variety, not a mixture, not a known species with odd chemistry — and "
  "deposit type material in a recognized museum. About a hundred new "
  "species are approved each year, many found by re-examining old museum "
  "specimens with new instruments. A complete description is permanent "
  "science: the type specimen anchors the name forever."),
 "how_it_works": (
  "The description workflow runs as a validation checklist. First, rule "
  "out the known: search-match the powder pattern and compare the analysis "
  "against every similar species — most 'new' minerals die here as "
  "varieties or mixtures. Second, establish homogeneity: backscattered-"
  "electron imaging must show a single phase, not intergrowths. Third, get "
  "quantitative chemistry with proper standards and full element coverage, "
  "including water and light elements by structure or spectroscopy. Fourth, "
  "solve or refine the crystal structure — a new structure proves novelty "
  "by itself. Fifth, measure the physical and optical properties on the "
  "same material. Sixth, write the description paper with the proposed "
  "name, etymology, type locality, and repository, and submit to the "
  "CNMNC. Respond to reviewers, revise, and on approval the mineral joins "
  "the master list — roughly a year from anomaly to acceptance."),
 "key_points": [
  "Pipeline: anomaly → rule out known → prove homogeneity → chemistry → structure → properties → CNMNC",
  "Most candidates fail early as varieties, mixtures, or misidentified known species",
  "New crystal structure proves novelty by itself",
  "Type specimen must be deposited in a recognized museum",
  "~100 new species approved per year; many found in old museum drawers",
  "A complete description is permanent science — the type anchors the name forever",
 ],
 "requirements": [
  "Electron microprobe, X-ray diffractometer, and optical lab access",
  "Backscattered-electron imaging for homogeneity proof",
  "A recognized museum willing to curate type material",
  "Patience: anomaly to approval typically takes about a year",
 ],
 "standards": [
  "CNMNC new-mineral proposal requirements (chemistry, structure, properties, deposition)",
  "Type-specimen curation standards",
 ],
 "citations": [CIT_IMA, CIT_KLEIN],
 "sig_lens": (
  "Signature edition: new-mineral description as his original novelty "
  "proof — a validation pipeline that kills most candidates early and "
  "turns the survivors into permanent, anchored science."),
 "demo_kind": "newmineral_checklist",
},
{
 "key": "environmental-mineralogy", "name": "Environmental Mineralogy: Acid Drainage and Remediation",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Environmental mineralogy applies mineral reactions to pollution: the "
  "centerpiece is acid mine drainage, where exposed pyrite oxidizes — "
  "2FeS2 + 7O2 + 2H2O → 2Fe²⁺ + 4SO4²⁻ + 4H⁺ — generating sulfuric acid "
  "that leaches heavy metals from surrounding rock. Iron-oxidizing bacteria "
  "accelerate the reaction up to a millionfold, turning a slow weathering "
  "process into an environmental catastrophe measured in decades. "
  "Remediation is mineralogy in reverse: limestone drains neutralize acid "
  "(CaCO3 + 2H⁺ → Ca²⁺ + H2O + CO2), constructed wetlands precipitate iron "
  "as ochre, and phosphate amendments lock lead into stable pyromorphite. "
  "The same mineral reactions govern nuclear waste storage (bentonite clay "
  "barriers), CO2 sequestration (mineral carbonation of olivine and "
  "basalt), and asbestos hazard assessment. Predicting decades of "
  "geochemistry from mineral kinetics is the field's core skill — and its "
  "hardest problem."),
 "how_it_works": (
  "Assessing acid drainage works by acid-base accounting. Measure the "
  "sulfide content (acid potential: each percent sulfide-sulfur generates "
  "about 31 tonnes of CaCO3-equivalent acid per thousand tonnes of rock) "
  "and the carbonate content (neutralization potential by titration), then "
  "subtract: net positive means the rock will turn acidic. Kinetic tests — "
  "humidity cells leaching samples for months — refine the static number "
  "with real reaction rates, since armoring and bacterial catalysis shift "
  "outcomes. Design remediation from the mineralogy: size limestone drains "
  "from the acid load, choose wetlands where iron dominates, and add "
  "phosphate where lead is the risk (pyromorphite is among the most stable "
  "lead minerals known). Monitor with the same tools — water chemistry "
  "tracks which minerals are dissolving or precipitating — and adjust, "
  "because a remediation system is a managed mineral-reaction reactor."),
 "key_points": [
  "Pyrite oxidation generates sulfuric acid: 2FeS2 + 7O2 + 2H2O → acid + sulfate + iron",
  "Iron-oxidizing bacteria accelerate the reaction up to a millionfold",
  "Acid-base accounting: sulfide acid potential minus carbonate neutralization potential",
  "Limestone drains neutralize acid; wetlands precipitate iron; phosphate locks lead as pyromorphite",
  "Same mineral kinetics govern nuclear waste barriers and CO2 mineralization",
  "Remediation systems are managed mineral-reaction reactors — monitor and adjust",
 ],
 "requirements": [
  "Acid-base accounting lab procedure (sulfur analysis, neutralization titration)",
  "Humidity-cell kinetic test capability for critical sites",
  "Water-chemistry monitoring (pH, metals, sulfate)",
  "Geochemical modeling software or hand-calculation fluency",
 ],
 "standards": [
  "Acid-base accounting conventions (CaCO3-equivalent tonnes per thousand tonnes)",
  "Kinetic-test (humidity cell) standard procedures",
 ],
 "citations": [CIT_STD, CIT_PUTNIS],
 "sig_lens": (
  "Signature edition: environmental mineralogy as his original reaction "
  "ledger — every sulfide a potential acid source, every carbonate a "
  "neutralization credit, remediation as managed mineral accounting."),
 "demo_kind": "acid_base_accounting",
},
{
 "key": "systematic-collection", "name": "Building a Systematic Mineral Collection",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A systematic collection is a physical mineral database: specimens "
  "organized by the Dana or Strunz system, each with a catalog number, "
  "locality, acquisition record, and label — the private equivalent of a "
  "museum's scientific collection. Building one teaches mineralogy faster "
  "than any textbook because every specimen is handled, tested, and filed "
  "by its real properties. Start with the rock-forming dozen and the "
  "common ore minerals, add one representative per Dana class, then fill "
  "structural families (a nesosilicate, a sorosilicate, a cyclosilicate...) "
  "and classic localities. Curate ruthlessly: a small collection of "
  "labeled, localized, representative specimens beats a large one of "
  "pretty unknowns. Document everything — an unlabeled specimen loses most "
  "of its scientific value the day its locality is forgotten. Photograph, "
  "number, and store by system, and the collection becomes a teaching "
  "ladder you can hold: foundations in the first drawer, advanced species "
  "in the last."),
 "how_it_works": (
  "Building systematically works drawer by drawer. Assign every specimen a "
  "permanent catalog number on acquisition and log it immediately: number, "
  "species, variety, locality (as specific as possible), source, date, "
  "price or trade, and notes on tests performed. Organize by classification "
  "(Dana class order is the traditional choice), leaving growth space in "
  "each section. Verify each identification with at least two properties "
  "before labeling — a mislabeled collection teaches errors. Set "
  "acquisition priorities from a want list keyed to the system: fill class "
  "gaps first, upgrade quality second, chase rarities last. Maintain the "
  "collection physically: stable temperature and humidity, pyrite and "
  "specimens prone to 'pyrite disease' isolated and monitored, labels in "
  "archival materials. Review annually: re-identify doubtful pieces, "
  "update names to current IMA nomenclature, and deaccession duplicates "
  "to fund the gaps."),
 "key_points": [
  "A systematic collection is a physical mineral database organized by Dana or Strunz",
  "Every specimen: catalog number, locality, acquisition record, label",
  "Acquisition order: rock-forming dozen → one per class → structural families → localities",
  "Verify every ID with two properties before labeling",
  "An unlabeled specimen loses most scientific value when its locality is forgotten",
  "Annual review: re-identify, update to current IMA names, fill gaps",
 ],
 "requirements": [
  "Catalog system (numbered labels, logbook or database)",
  "Storage: drawers or boxes organized by classification, stable environment",
  "Basic ID kit (hand lens, hardness tools, streak plate) for verification",
  "Acquisition discipline: fill system gaps before chasing rarities",
 ],
 "standards": [
  "Museum cataloging conventions (number, locality, source, date)",
  "IMA nomenclature kept current across the collection",
 ],
 "citations": [CIT_DANA, CIT_IMA],
 "sig_lens": (
  "Signature edition: the systematic collection as his original physical "
  "database — drawers ordered by the classification system, every "
  "specimen a verified, localized record in a teaching ladder you can "
  "hold."),
 "demo_kind": "collection_audit",
},
]
