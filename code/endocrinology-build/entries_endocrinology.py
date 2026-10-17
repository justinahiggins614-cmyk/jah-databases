#!/usr/bin/env python3
"""Entries for the Endocrinology field databases (field #37, taxonomy order).

Verified 2026-10-17: NO database covers endocrinology as a clinical specialty
(hypothalamic-pituitary axes, thyroid, adrenal, pancreatic/diabetes,
calcium-PTH-vitamin D, reproductive endocrinology, neuroendocrinology,
endocrine tumors, hormone assays and dynamic testing).

Manifest search (2,374 databases): zero 'endocrinolog*' slugs/names; no
db/endocrinolog* dirs. Whole-system exact-title sweep over the dedupe gate:
zero collisions for all 34 planned titles x2 editions (68 variants).
Near-neighbors confirmed different disciplines: 'biochemistry' (molecular
mechanisms), 'physiology' (general body function), 'embryology' (has an
'endocrine development' organogenesis record only), 'diabetes' coverage is
fragmented across general health databases, no discipline coverage.
ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  endocrinology              - The Endocrinology Database
                               (public-harvest: real, fact-checked clinical
                               endocrinology; standard references Melmed et al.
                               'Williams Textbook of Endocrinology' 15th ed
                               2024; Gardner/Shoback 'Greenspan's Basic &
                               Clinical Endocrinology' 11th ed 2022; Jameson et
                               al. 'Harrison's Principles of Internal
                               Medicine' 21st ed 2022; ADA Standards of Care
                               in Diabetes 2024; ATA hyperthyroidism and
                               thyroid nodule guidelines)
  endocrinology-signature    - The Endocrinology Signature Database
                               (his original Signature interpretation of the
                               hormone system as the body's chemical command
                               network; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-ENR- (public) and JAH-ENS- (signature). JAH-END- was
unavailable (taken by an earlier database), so endocrinology takes JAH-ENR-
and the signature edition takes JAH-ENS-; both verified free in the manifest
and in every shard index.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of the "
            "endocrine system as the body's chemical command network: every axis "
            "a control loop, every gland a transmitter, every hormone a signed "
            "message with a destination, a dose, and a receipt. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Endocrinology: The Science of Hormones and Chemical Signaling",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Endocrinology is the clinical medical specialty that studies hormones - "
            "chemical messengers made in one place, carried by the blood, and read by "
            "distant target cells - and the diseases that follow when the messaging "
            "breaks. The word comes from the Greek endon (within), krino (to separate), "
            "and logos (study): the study of the internal secretions. A healthy adult "
            "runs on more than fifty hormones coordinating growth, metabolism, "
            "reproduction, fluid and salt balance, stress responses, and the "
            "day-night cycle. Endocrinologists diagnose and manage diabetes mellitus, "
            "thyroid disease, pituitary and adrenal disorders, calcium and bone "
            "disorders, reproductive hormone disorders, and hormone-secreting tumors. "
            "The discipline is distinct from biochemistry, which studies the molecules "
            "themselves, and from physiology, which studies how the whole body "
            "functions: endocrinology is the specialty of the signaling system and its "
            "clinical failures. This record frames the discipline and the ladder of "
            "records that follows."
        ),
        "how_it_works": (
            "Endocrinology works as a network of control loops. A gland releases a "
            "hormone into the bloodstream at concentrations measured in billionths to "
            "trillionths of a mole per liter. Target cells carry receptors that bind "
            "the hormone only when its concentration crosses the receptor's affinity "
            "threshold, so the message is read by binding arithmetic, not by volume. "
            "Almost every axis closes its loop with negative feedback: the end "
            "product tells the upstream controllers to stand down, the way a "
            "thermostat cuts the furnace when the room reaches temperature. The demo "
            "works the binding arithmetic that decides whether a message is heard: "
            "receptor occupancy as a function of hormone concentration, showing that "
            "doubling a hormone near its affinity constant nearly doubles the signal, "
            "while doubling it far above saturation barely moves it."
        ),
        "key_points": [
            "Endocrinology = the clinical specialty of hormones and their disorders: diabetes, thyroid, pituitary, adrenal, calcium, reproductive, and tumor disease.",
            "More than 50 human hormones coordinate growth, metabolism, reproduction, salt and water balance, stress, and circadian rhythm.",
            "Hormones act at nanomolar to picomolar concentrations; the message is read by receptor binding, not by amount.",
            "Negative feedback closes nearly every axis: the end product suppresses its own upstream controllers.",
            "Distinct from biochemistry (the molecules) and physiology (whole-body function): endocrinology is the signaling system plus its clinical failures.",
        ],
        "requirements": [
            "The gland-target-receptor vocabulary kept straight: secretion, circulation, binding, response.",
            "The feedback-loop picture: controller, messenger, target, and the return signal that closes the loop.",
            "Concentration literacy: nanomolar and picomolar scales, and why tiny doses carry full messages.",
        ],
        "standards": [
            "Hormone names and abbreviations follow standard clinical usage (TSH, T4, ACTH, cortisol, insulin).",
            "Concentration units stated explicitly (mIU/L, ng/dL, pg/mL, nmol/L) since the same hormone is reported in several.",
            "Disease framing is diagnostic and management-oriented, matching the clinical-specialty scope.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the endocrine system is the body's signed-message "
            "network. Every hormone is a dispatch with a sender gland, a destination "
            "tissue, a concentration-encoded instruction, and a feedback receipt that "
            "confirms delivery. Disease is what happens when a dispatch is forged "
            "(too much hormone), lost (too little), or ignored (resistance)."
        ),
    },
    {
        "key": "endocrine_system",
        "name": "The Endocrine System: Glands, Targets, and Feedback Loops",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The endocrine system is the body's slow, broadcast communication network: "
            "glands and hormone-secreting tissues that release messengers into the "
            "blood for delivery everywhere. The classic roster runs from the "
            "hypothalamus and pituitary at the top, through the thyroid, the four "
            "parathyroids, the two adrenals, and the pancreatic islets, to the "
            "gonads (testes and ovaries), the pineal gland, and scattered "
            "hormone-making tissues in the gut, kidneys, heart, fat, and placenta. "
            "Unlike the nervous system's point-to-point wiring, endocrine messages "
            "travel by circulation and arrive in minutes to hours, last for minutes "
            "to days, and act on any cell carrying the right receptor. The system's "
            "organizing principle is the axis: a chain of command from hypothalamus "
            "to pituitary to end gland to target tissue, usually with the final "
            "hormone feeding back to quiet the controllers. This record maps the "
            "network's stations and its loop architecture."
        ),
        "how_it_works": (
            "The system works in five classic hypothalamic-pituitary axes plus "
            "independent glands. The HPA axis (stress: CRH to ACTH to cortisol), the "
            "HPT axis (metabolism: TRH to TSH to thyroid hormone), the HPG axis "
            "(reproduction: GnRH to LH/FSH to sex steroids), the GH axis (growth), "
            "and the prolactin axis (lactation) all run the same three-level "
            "pattern. Independent stations - the parathyroids reading blood calcium "
            "directly, the pancreatic islets reading blood glucose, the adrenals' "
            "medulla answering the sympathetic nervous system - skip the pituitary "
            "and regulate themselves against the variable they control. The demo "
            "quantifies what makes feedback work: a disturbance that would drive a "
            "hormone tenfold in open loop is held near normal in closed loop, and "
            "the arithmetic shows the disturbance-rejection percentage that "
            "negative feedback buys."
        ),
        "key_points": [
            "The endocrine system is the slow broadcast network: blood-borne messages, minutes to days, read by receptor-bearing cells anywhere.",
            "Classic stations: hypothalamus, pituitary, thyroid, parathyroids, adrenals, pancreatic islets, gonads, pineal, plus gut, kidney, heart, fat, and placenta.",
            "Five classic hypothalamic-pituitary axes: HPA (stress), HPT (thyroid), HPG (reproduction), GH (growth), prolactin (lactation).",
            "Independent glands (parathyroids, islets) regulate themselves against the variable they control, no pituitary required.",
            "Negative feedback is the organizing loop: the end product suppresses its upstream controllers.",
        ],
        "requirements": [
            "The five classic axes named with their three levels: hypothalamic signal, pituitary signal, end-gland hormone.",
            "The contrast with neural signaling: broadcast vs wired, slow vs fast, sustained vs brief.",
            "A working picture of disturbance rejection: feedback as the mechanism that holds hormone levels near set point.",
        ],
        "standards": [
            "Axis abbreviations (HPA, HPT, HPG) used in their standard clinical senses.",
            "Gland anatomy described in standard orientation and approximate size.",
            "Feedback described as negative unless a positive-feedback exception (ovulatory LH surge, parturition) is named.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the endocrine system is a broadcast command network "
            "with two kinds of stations - relayed stations that take orders down a "
            "three-level chain of command, and autonomous stations that read their "
            "own sensors and regulate themselves. Feedback is the network's "
            "acknowledgment protocol: every command carries a receipt that tells the "
            "sender to stop transmitting."
        ),
    },
    {
        "key": "hormone_classes",
        "name": "Hormone Classes: Peptides, Steroids, and Amines",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every hormone belongs to one of three chemical families, and the family "
            "decides nearly everything about how the hormone travels, how long it "
            "lasts, and where its receptor sits. Peptide and protein hormones - "
            "insulin, glucagon, growth hormone, ACTH, TSH - are chains of amino "
            "acids, water-soluble, carried free in plasma, and read by receptors on "
            "the cell surface because they cannot cross the membrane. Steroid "
            "hormones - cortisol, aldosterone, testosterone, estradiol, progesterone, "
            "vitamin D - are built from cholesterol, fat-soluble, carried bound to "
            "plasma proteins, and read by receptors inside the cell, where they "
            "switch genes on and off. Amine hormones split the difference: the "
            "catecholamines (epinephrine, norepinephrine, dopamine) behave like "
            "peptides with surface receptors and seconds-long lives, while the "
            "thyroid hormones (T3, T4), though built from the amino acid tyrosine, "
            "behave like steroids with nuclear receptors and days-long lives. This "
            "record teaches the three families and the pharmacology that follows "
            "from each."
        ),
        "how_it_works": (
            "Chemistry dictates pharmacology. Water-soluble peptides circulate free "
            "and hit the bloodstream at full strength within minutes, but enzymes "
            "chew them up in minutes - insulin's half-life is about five minutes - "
            "so they must be secreted continuously or in pulses. Fat-soluble steroids "
            "ride on binding proteins (cortisol-binding globulin, sex-hormone-binding "
            "globulin, albumin), which act as circulating reservoirs: only the small "
            "free fraction is active, and the bound pool buffers every swing, "
            "stretching the effective lifetime to hours. Thyroid hormones push this "
            "to the extreme: thyroxine (T4) is more than 99.9 percent protein-bound "
            "with a seven-day half-life, which is why a missed thyroid pill barely "
            "registers and why thyroid levels change over weeks, not hours. The demo "
            "works the molecular-weight and dosing arithmetic that separates the "
            "families: insulin's international-unit-to-mass conversion and the "
            "thousand-fold half-life span from insulin to thyroxine."
        ),
        "key_points": [
            "Three hormone families: peptides/proteins (surface receptors, minutes-long lives), steroids (intracellular receptors, hours-long lives), amines (split behavior).",
            "Peptides circulate free and act fast but are cleared in minutes; they are secreted in pulses or continuously.",
            "Steroids ride binding proteins; only the free fraction is active, and the bound pool buffers swings.",
            "Thyroid hormones behave like steroids: nuclear receptors, heavy protein binding, days-long half-lives.",
            "Family predicts therapy: peptides are injected (digested if swallowed), steroids and thyroid hormone are pills.",
        ],
        "requirements": [
            "One flagship hormone per family with its receptor location: insulin (surface), cortisol (intracellular), epinephrine (surface), T4 (nuclear).",
            "The free-vs-bound distinction and why binding proteins are reservoirs, not waste.",
            "The half-life ladder from minutes (insulin, catecholamines) to days (T4) and its dosing consequences.",
        ],
        "standards": [
            "Molecular weights and half-lives given as standard textbook values with units.",
            "Insulin dosing uses international units with the standard mass conversion stated.",
            "Receptor classes named by standard pharmacology (GPCR, nuclear receptor, enzyme-linked).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the three hormone families are three message "
            "formats. Peptides are telegrams - fast, plain-text, read at the door "
            "and shredded after delivery. Steroids are sealed orders - slow, "
            "armored in binding-protein envelopes, opened inside the cell where "
            "they rewrite the standing instructions. Amines are the hybrids that "
            "borrow whichever format the mission needs."
        ),
    },
    {
        "key": "receptors",
        "name": "Hormone Receptors: How Target Cells Read the Signal",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A hormone is only a message; the receptor is the reader, and the cell "
            "that lacks the receptor never hears the broadcast. Receptors come in "
            "two great architectures. Cell-surface receptors - dominated by the "
            "G-protein-coupled receptor (GPCR) family that reads epinephrine, "
            "glucagon, TSH, LH, FSH, ACTH, and dozens more - bind the hormone "
            "outside and relay the signal inside through second messengers like "
            "cyclic AMP, inositol trisphosphate, and calcium. Intracellular "
            "receptors - the nuclear receptor family that reads cortisol, "
            "aldosterone, sex steroids, thyroid hormone, and vitamin D - bind the "
            "hormone inside the cell (or inside the nucleus) and act directly as "
            "gene switches, which is why steroid effects take hours to appear and "
            "hours to fade. The same hormone can carry different orders to different "
            "tissues because different tissues express different receptor subtypes: "
            "epinephrine speeds the heart through beta-1 receptors while constricting "
            "skin vessels through alpha-1 receptors. This record teaches the reader "
            "side of the conversation."
        ),
        "how_it_works": (
            "Surface-receptor signaling is an amplification cascade: one occupied "
            "GPCR activates several G-proteins, each activates an enzyme that makes "
            "many second-messenger molecules, each messenger activates a kinase "
            "that phosphorylates many targets - total gains of a million-fold are "
            "routine, which is why picomolar hormone concentrations move whole "
            "organs. Nuclear-receptor signaling skips the cascade: the "
            "hormone-receptor complex binds DNA response elements and changes gene "
            "transcription, trading speed for duration and precision. Binding "
            "itself follows the occupancy law: the fraction of occupied receptors "
            "equals hormone concentration divided by the sum of concentration and "
            "the dissociation constant, so a cell is half-activated exactly when "
            "the hormone reaches its Kd. The demo works the cascade gain "
            "arithmetic - one ligand, ten G-proteins, a hundred messengers each, a "
            "thousand targets each - and the occupancy curve that turns "
            "concentration into signal."
        ),
        "key_points": [
            "No receptor, no response: target specificity lives in receptor expression, not in hormone delivery.",
            "Surface receptors (mostly GPCRs) signal through second-messenger cascades with million-fold amplification in seconds to minutes.",
            "Nuclear receptors are gene switches: slow onset, long duration, direct transcriptional control.",
            "One hormone, many messages: receptor subtypes let epinephrine speed the heart and constrict skin vessels at once.",
            "Receptor occupancy follows the binding law: half-maximal signal at the dissociation constant.",
        ],
        "requirements": [
            "The two architectures contrasted: surface cascade vs nuclear gene switch, with onset times.",
            "The amplification arithmetic: why trace hormone concentrations produce organ-scale effects.",
            "The subtype principle: same ligand, different receptor, different - even opposite - tissue response.",
        ],
        "standards": [
            "Receptor families named by standard classification (GPCR, nuclear receptor, receptor tyrosine kinase).",
            "Second messengers named correctly (cAMP, IP3, DAG, calcium).",
            "Time scales stated: seconds-minutes for cascades, hours for transcriptional effects.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: receptors are the installed base of decoding "
            "hardware. The broadcast is public - every tissue sees every hormone - "
            "but only tissues carrying the right decoder ring execute the order. "
            "Drug design is largely the art of picking which decoder rings to "
            "trigger: beta-blockers jam the cardiac epinephrine reader while "
            "leaving the rest of the network untouched."
        ),
    },
    {
        "key": "hypothalamus",
        "name": "The Hypothalamus: The Endocrine Command Center of the Brain",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The hypothalamus is a walnut-sized region at the base of the brain "
            "where the nervous system and the endocrine system shake hands. It "
            "reads blood temperature, osmolarity, glucose, and circulating hormones, "
            "takes neural input about stress, emotion, light, and hunger, and "
            "answers by releasing six major regulatory signals into the short "
            "portal blood vessels that feed the anterior pituitary: TRH (thyroid "
            "axis), CRH (stress axis), GnRH (reproductive axis), GHRH (growth axis), "
            "somatostatin (the brake on growth hormone and more), and dopamine (the "
            "brake on prolactin). Magnocellular neurons in the supraoptic and "
            "paraventricular nuclei go further: their axons run all the way down "
            "the pituitary stalk and dump oxytocin and vasopressin directly from "
            "the posterior pituitary into the general circulation. Much of the "
            "hypothalamus speaks in pulses - GnRH pulses every 60 to 120 minutes "
            "are the metronome of reproduction - and continuous, non-pulsatile "
            "delivery of the same signal shuts the system down, a paradox that "
            "medicine exploits in therapy. This record maps the command center."
        ),
        "how_it_works": (
            "The hypothalamus works as a pattern generator, not just a switch. "
            "Its releasing hormones are secreted in discrete pulses whose "
            "frequency encodes the message: GnRH pulses every 90 minutes sustain "
            "normal LH and FSH secretion, faster pulsing favors LH, slower pulsing "
            "favors FSH, and constant GnRH desensitizes the pituitary completely - "
            "which is why long-acting GnRH agonists, after a brief flare, are used "
            "to suppress puberty, endometriosis, and prostate cancer. The portal "
            "circulation is the private wire: hypothalamic signals travel a few "
            "millimeters of portal blood to the anterior pituitary at high "
            "concentration instead of being diluted through the whole body. The "
            "demo works the pulse-timing arithmetic that governs the reproductive "
            "axis: pulses per day at normal, fast, and slow frequencies, showing "
            "how timing alone rewrites the hormonal message."
        ),
        "key_points": [
            "The hypothalamus links brain and glands: it senses blood and neural state and releases six major pituitary regulators.",
            "The six signals: TRH, CRH, GnRH, GHRH, somatostatin, and dopamine - four accelerators, two brakes.",
            "Oxytocin and vasopressin are made in the hypothalamus and released from the posterior pituitary.",
            "The message is encoded in pulse frequency: GnRH every 60-120 minutes; constant GnRH shuts the axis down.",
            "The portal circulation is a private wire delivering concentrated signals the short distance to the pituitary.",
        ],
        "requirements": [
            "The six hypothalamic regulators named with their target pituitary hormone and net effect.",
            "The pulse-frequency code and the desensitization paradox that makes continuous GnRH suppressive.",
            "The anatomical split: anterior pituitary driven by portal signals, posterior pituitary as a release terminal for hypothalamic axons.",
        ],
        "standards": [
            "Nuclei named by standard neuroanatomy (supraoptic, paraventricular, arcuate).",
            "Pulse intervals given as standard physiological ranges.",
            "Therapeutic corollary (GnRH agonist suppression) stated as the clinical use of the desensitization principle.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the hypothalamus is the network operations center. "
            "It fuses sensor telemetry (blood chemistry) with intelligence reports "
            "(stress, light, emotion) and issues timed command bursts down a "
            "private line. Its deepest trick is steganography by rhythm: the same "
            "molecule means different things at different pulse rates, and a "
            "steady tone - normally a sign of strength - is read as a shutdown "
            "order."
        ),
    },
    {
        "key": "pituitary",
        "name": "The Pituitary Gland: The Master Gland and Its Axes",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The pituitary gland is a pea-sized organ - about a centimeter across, "
            "half a gram to a gram - hanging beneath the hypothalamus in a bony "
            "pocket of the skull called the sella turcica. It is really two glands "
            "in one. The anterior pituitary (adenohypophysis) manufactures six "
            "major hormones: growth hormone (GH), prolactin, ACTH, TSH, LH, and "
            "FSH, each from its own cell tribe - somatotrophs are the largest "
            "tribe at roughly half the cells, then corticotrophs and lactotrophs, "
            "then gonadotrophs, with thyrotrophs the smallest contingent. The "
            "posterior pituitary (neurohypophysis) manufactures nothing; it is the "
            "release terminal for oxytocin and vasopressin made upstream in the "
            "hypothalamus. Because the pituitary drives the thyroid, adrenals, and "
            "gonads, its failures cascade: too little pituitary function "
            "(hypopituitarism) starves three downstream glands at once, and a "
            "pituitary tumor can flood the body with one hormone while crushing "
            "the rest. This record maps the master gland's divisions and its "
            "downstream commands."
        ),
        "how_it_works": (
            "The anterior pituitary works as a six-channel relay station. Each "
            "hypothalamic signal addresses one cell tribe: GHRH tells "
            "somatotrophs to release GH, TRH tells thyrotrophs to release TSH, CRH "
            "tells corticotrophs to release ACTH, GnRH tells gonadotrophs to "
            "release LH and FSH, while somatostatin brakes GH and dopamine brakes "
            "prolactin. Each pituitary hormone then drives its end gland - TSH the "
            "thyroid, ACTH the adrenal cortex, LH/FSH the gonads, GH the liver's "
            "IGF-1 production - and the end hormone feeds back on both pituitary "
            "and hypothalamus. The gland's cell census is itself diagnostic "
            "logic: because somatotrophs are half the anterior pituitary, a "
            "non-functioning tumor large enough to compress the gland typically "
            "knocks out GH first. The demo works the cell-tribe census arithmetic "
            "and the size facts that make the sella a crowded neighborhood where "
            "millimeters matter."
        ),
        "key_points": [
            "The pituitary is two glands: anterior (makes six hormones) and posterior (releases two made in the hypothalamus).",
            "Anterior hormones: GH, prolactin, ACTH, TSH, LH, FSH - each from its own cell tribe.",
            "Cell census: somatotrophs ~50%, lactotrophs ~20%, corticotrophs ~15%, gonadotrophs ~10%, thyrotrophs ~5%.",
            "The pituitary drives thyroid, adrenals, and gonads - so pituitary failure cascades downstream threefold.",
            "Size matters: a ~1 cm gland in a bony pocket means tumors compress neighbors fast.",
        ],
        "requirements": [
            "The six anterior hormones matched to their cell tribe and downstream target.",
            "The anterior/posterior split: manufactured vs released, portal-driven vs axon-delivered.",
            "The cascade logic: why hypopituitarism presents as combined thyroid, adrenal, and gonadal failure.",
        ],
        "standards": [
            "Dimensions and weight given as standard anatomical values (~1 cm, 0.5-0.9 g).",
            "Cell-type percentages given as standard textbook ranges summing to the whole gland.",
            "Sella turcica named as the bony housing; optic chiasm noted as the superior neighbor.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the pituitary is the repeater station that fans "
            "one hypothalamic command into six addressed channels. Its org chart "
            "is public - half the staff works the growth desk - so an attacker "
            "(tumor) or a blackout (apoplexy, surgery) has predictable "
            "casualties: the biggest departments fall first, and every downstream "
            "agency loses its orders at once."
        ),
    },
    {
        "key": "negative_feedback",
        "name": "Negative Feedback: The Thermostat Logic of Hormones",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Negative feedback is the control logic that keeps hormones near their "
            "set points: the end product of an axis suppresses the controllers that "
            "made it. Thyroid hormone quiets TSH; cortisol quiets ACTH; testosterone "
            "quiets LH; IGF-1 quiets GH. The relation is not gentle - it is "
            "logarithmic. In the thyroid axis, a twofold change in free T4 drives "
            "roughly a hundredfold change in TSH in the opposite direction, which "
            "is why TSH is the sensitive screening test for thyroid disease: the "
            "amplified signal moves first and moves far. Feedback operates at two "
            "levels, the pituitary (short loop) and the hypothalamus (long loop), "
            "and it explains the signature patterns of endocrine disease: primary "
            "gland failure shows a low end hormone with a high trophic hormone "
            "(the controllers shouting at a deaf gland), while pituitary failure "
            "shows both low (no one shouting at all). This record teaches the "
            "loop logic that organizes all of clinical endocrinology."
        ),
        "how_it_works": (
            "Feedback works as a closed control loop with a set point. When the end "
            "hormone drifts below set point, suppression lifts and the pituitary "
            "releases more trophic hormone, which drives the end gland harder; when "
            "the end hormone overshoots, suppression deepens and the drive backs "
            "off. The log-linear form used in thyroidology says the natural log of "
            "TSH falls in a straight line as free T4 rises - each small T4 "
            "increment buys a proportional TSH decrement, compounding into the "
            "hundredfold swings clinicians rely on. A discrete controller model "
            "captures the same idea: each cycle corrects a fixed fraction of the "
            "remaining error, so the system converges geometrically to set point "
            "without ever overshooting wildly. The demo runs both: the "
            "doubling-halving arithmetic of the TSH-T4 pair, and a step-by-step "
            "controller converging on its set point, proving the thermostat "
            "settles instead of oscillating."
        ),
        "key_points": [
            "Negative feedback: the end hormone suppresses its own upstream controllers at pituitary and hypothalamic levels.",
            "The TSH-T4 relation is log-linear: a 2x change in free T4 drives ~100x change in TSH - TSH is the amplifier.",
            "Primary gland failure: low end hormone + HIGH trophic hormone. Pituitary failure: both LOW.",
            "Feedback makes hormone levels disturbance-rejecting: closed-loop control holds the set point against perturbations.",
            "Reading any axis starts with the pair: the end hormone and its trophic driver, interpreted together.",
        ],
        "requirements": [
            "The log-linear TSH-T4 relationship and why TSH is the screening test.",
            "The two failure patterns (primary vs secondary/central) read from the hormone pair.",
            "A controller's-eye view: set point, error, correction fraction, convergence.",
        ],
        "standards": [
            "TSH reported in mIU/L, free T4 in ng/dL (with pmol/L equivalents where helpful).",
            "Primary vs secondary/central terminology used in the standard endocrine sense.",
            "The 100-fold TSH swing per T4 doubling stated as the classic teaching approximation.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jonklaas J, Bianco AC, Bauer AJ, et al. Guidelines for the treatment of hypothyroidism. Thyroid. 2014;24(12):1670-1751.",
        ],
        "sig_lens": (
            "Signature reading: negative feedback is the thermostat protocol, and "
            "the thyroid axis runs it with a logarithmic amplifier bolted on. The "
            "design lesson is instrumentation: do not watch the furnace (T4), "
            "watch the thermostat wire (TSH) - the control signal carries the "
            "failure news a hundred times louder than the output does."
        ),
    },
    {
        "key": "synthesis_secretion",
        "name": "Hormone Synthesis, Storage, and Secretion: From Gene to Bloodstream",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Hormones are manufactured goods, and each family runs its own factory "
            "line. Peptide hormones are built like any protein: gene to messenger "
            "RNA to a long precursor chain that is trimmed in stages. Insulin's "
            "line is the textbook example - preproinsulin (110 amino acids) loses "
            "its signal peptide to become proinsulin (86), which is cut into the "
            "two-chain insulin molecule (51 amino acids: A chain of 21, B chain of "
            "30, stapled by disulfide bonds) plus the C-peptide fragment (31), "
            "with the four leftover amino acids consumed as cleavage sites. "
            "Steroid hormones are built the other way: cholesterol is remodeled "
            "step by step through the steroidogenic pathway, and because steroids "
            "leak through membranes they cannot be stockpiled - they are made to "
            "order on demand. The thyroid is the great exception among glands: it "
            "warehouses two to three months of hormone supply inside colloid, "
            "which is why thyroid failure and thyroid treatment both move in slow "
            "motion. Secretion itself is usually pulsatile or circadian rather "
            "than steady - cortisol peaks near waking, growth hormone pulses in "
            "deep sleep. This record follows the hormone from gene to bloodstream."
        ),
        "how_it_works": (
            "Peptide synthesis works by precursor trimming: long inactive chains "
            "are cut at paired basic amino acids by prohormone convertases, so one "
            "precursor can yield several active products - pro-opiomelanocortin "
            "(POMC), for example, is cut into ACTH, MSH, and beta-endorphin in "
            "different tissues. Steroid synthesis works by enzymatic remodeling of "
            "cholesterol through pregnenolone: the same trunk pathway branches "
            "into mineralocorticoids, glucocorticoids, and sex steroids depending "
            "on which enzymes a zone or gland expresses, which is why a single "
            "enzyme block (as in congenital adrenal hyperplasia) backs up one "
            "branch and floods another. Storage strategy follows chemistry: "
            "peptides wait in secretory granules for a calcium-triggered release, "
            "steroids leave the cell as fast as they are made, and thyroid hormone "
            "sits iodinated on thyroglobulin in colloid until TSH calls for it. "
            "The demo works the proinsulin cleavage arithmetic - 86 precursor "
            "amino acids accounted for as insulin plus C-peptide plus cleavage "
            "sites - and the thyroid's hundred-day inventory that makes it the "
            "system's warehouse."
        ),
        "key_points": [
            "Peptides are built as long precursors and trimmed: preproinsulin 110 -> proinsulin 86 -> insulin 51 + C-peptide 31.",
            "Steroids are remodeled from cholesterol on demand; they cannot be stored because they diffuse through membranes.",
            "One precursor, many products: POMC is cut into ACTH, MSH, and endorphin depending on the tissue.",
            "The thyroid warehouses 2-3 months of hormone in colloid - the system's strategic reserve.",
            "Secretion is patterned, not steady: pulses (GH, GnRH, insulin) and circadian rhythms (cortisol) carry information.",
        ],
        "requirements": [
            "The insulin precursor chain with amino-acid counts that add up.",
            "The cholesterol-to-steroid trunk and why enzyme expression decides which steroid a tissue makes.",
            "The three storage strategies: granules (peptides), make-to-order (steroids), colloid warehouse (thyroid).",
        ],
        "standards": [
            "Amino-acid counts and precursor names follow standard biochemical nomenclature.",
            "Thyroid storage stated as the standard 2-3 month (up to ~100 day) teaching value.",
            "Enzyme and precursor names (POMC, prohormone convertases) spelled in standard form.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: hormone manufacturing is three different supply "
            "chains. Peptides are assembled on the protein line and kitted in "
            "stages. Steroids are just-in-time manufacturing - no warehouse, "
            "build to order, ship immediately. The thyroid runs the strategic "
            "petroleum reserve model: refine in bulk, store months of inventory, "
            "release on command. Each logistics model dictates the failure mode "
            "when the factory breaks."
        ),
    },
    {
        "key": "assays",
        "name": "Measuring Hormones: Immunoassays and the Lab Workup",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Endocrinology is a laboratory specialty as much as a bedside one: the "
            "diagnosis usually lives in the numbers. The workhorse is the "
            "immunoassay - antibodies engineered to grab one hormone out of blood "
            "and report how much they caught, in sandwich or competitive formats, "
            "now mostly read by chemiluminescent labels. Modern TSH assays detect "
            "down to hundredths of a unit, which is what makes the log-linear "
            "TSH-T4 relationship clinically usable. But every measurement needs "
            "interpretation machinery: reference ranges (usually the central 95 "
            "percent of a healthy population), the distinction between total and "
            "free hormone (only the free fraction of protein-bound hormones like "
            "T4, testosterone, and cortisol is active), and the test-performance "
            "arithmetic of sensitivity, specificity, and predictive value that "
            "decides what a positive result actually means at a given disease "
            "prevalence. A hormone level is never read alone: it is read with its "
            "trophic partner, its binding proteins, the time of day, the assay's "
            "limits, and the patient's medications. This record teaches the "
            "measurement layer the whole specialty stands on."
        ),
        "how_it_works": (
            "A sandwich immunoassay works like a molecular trap: a capture "
            "antibody fixed to a surface grabs the hormone, a second labeled "
            "antibody grabs a different spot on the same hormone, and the label's "
            "light output is proportional to hormone concentration - more hormone, "
            "more light. A competitive assay inverts the logic for small hormones: "
            "labeled hormone competes with the patient's hormone for limited "
            "antibody, so more patient hormone means less light. Interpretation "
            "works through Bayes: a test that is 99 percent sensitive and 98 "
            "percent specific still yields a positive predictive value of only "
            "about 72 percent when the disease prevalence is 5 percent, because "
            "most positives come from the large healthy pool. The demo runs that "
            "predictive-value arithmetic - the calculation that stops clinicians "
            "from over-reading a mildly abnormal result - and the reference-range "
            "logic that defines normal as the middle 95 percent."
        ),
        "key_points": [
            "Immunoassays are antibody traps: sandwich format (more hormone, more signal) or competitive format (more hormone, less signal).",
            "Reference ranges are the central 95% of healthy people - 5% of healthy results fall outside by definition.",
            "Only free hormone is active for protein-bound hormones; total levels mislead when binding proteins change.",
            "Test meaning depends on prevalence: sensitivity and specificity are not enough without predictive-value math.",
            "A hormone is read with its trophic partner, binding proteins, time of day, assay limits, and medications.",
        ],
        "requirements": [
            "The two assay formats and which hormone sizes suit each.",
            "The sensitivity/specificity/PPV calculation worked from a concrete prevalence.",
            "The total-vs-free distinction with the binding-protein examples (TBG, SHBG, CBG, albumin).",
        ],
        "standards": [
            "Assay generations described correctly (third-generation TSH sensitivity ~0.01 mIU/L).",
            "Reference-range definition stated as the standard 2.5th-97.5th percentile convention.",
            "Units carried through every calculation; predictive value reported as a percentage.",
        ],
        "citations": [
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the assay is the network's listening post, and "
            "every listening post has a noise floor and a false-alarm rate. The "
            "craft is signal intelligence: knowing the sensor's limits, correcting "
            "for camouflage (binding proteins), reading the intercept in context "
            "(time of day, drugs), and running the Bayesian arithmetic before "
            "declaring that a blip on the scope is an actual contact."
        ),
    },
    {
        "key": "half_lives",
        "name": "Hormone Half-Lives and Clearance: Timing the Message",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Every hormone carries an expiration date, and the range is enormous: "
            "catecholamines and parathyroid hormone vanish in minutes, insulin in "
            "about five minutes, cortisol in about an hour and a half, T3 in a "
            "day, and thyroxine (T4) in about seven days. The half-life decides "
            "the hormone's job description. Short-lived hormones are the rapid "
            "response team - epinephrine must hit and fade in seconds, insulin "
            "must track each meal - and they have to be secreted continuously or "
            "in pulses because the blood clears them almost as fast as they "
            "arrive. Long-lived hormones are the climate, not the weather: T4's "
            "week-long half-life smooths every daily swing into a steady "
            "background, which is why thyroid status is read in weeks and why "
            "starting or stopping thyroid hormone takes over a month to settle. "
            "Clearance is mostly liver and kidney work - deiodination and "
            "conjugation for thyroid and steroids, renal filtration for peptides - "
            "so liver and kidney failure rewrite the timing of the whole system. "
            "This record teaches the clock each hormone runs on."
        ),
        "how_it_works": (
            "Hormone disappearance follows first-order kinetics: each half-life "
            "removes half of what remains, so the fraction left after n "
            "half-lives is one over two to the n. Stop levothyroxine and after "
            "three T4 half-lives (21 days) one-eighth of the drug remains; stop "
            "an insulin drip and after six insulin half-lives (30 minutes) under "
            "two percent remains - which is why insulin infusions need no taper "
            "and thyroid pills need no rush. Steady state obeys the five-half-life "
            "rule: a new constant dose reaches about 97 percent of its final "
            "level after five half-lives, so levothyroxine needs five weeks before "
            "the TSH can be trusted, while a cortisol infusion steadies in a "
            "single shift. Binding proteins stretch apparent half-life by "
            "shielding hormone from clearance - T4's seven days are mostly "
            "thyroxine-binding globulin's doing. The demo runs the decay "
            "arithmetic for stopping each major hormone and the five-half-life "
            "rule that sets every recheck interval in the specialty."
        ),
        "key_points": [
            "Half-life sets the job: minutes (epinephrine, insulin, PTH) for rapid response, days (T4) for background climate.",
            "Disappearance is first-order: fraction remaining after n half-lives is (1/2)^n.",
            "Steady state takes ~5 half-lives: 5 weeks for levothyroxine, hours for cortisol, minutes for insulin.",
            "Binding proteins extend apparent half-life by shielding hormone from liver and kidney clearance.",
            "Liver and kidney disease prolong half-lives - clearance failure is a whole-system timing fault.",
        ],
        "requirements": [
            "The half-life ladder memorized in order: catecholamines ~2 min, PTH ~4 min, insulin ~5 min, GH ~20 min, cortisol ~90 min, T3 ~1 day, T4 ~7 days.",
            "The (1/2)^n decay calculation applied to stopping a drug or infusion.",
            "The five-half-life steady-state rule and what it implies for recheck timing.",
        ],
        "standards": [
            "Half-lives given as standard textbook values with units and the bound/free caveat for T4.",
            "Recheck intervals derived from the rule, not quoted as bare protocol.",
            "Clearance organs named per hormone class (liver deiodination/conjugation, renal peptide filtration).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: half-life is the message's time-to-live flag. "
            "The network runs two postal classes: express couriers (minutes) for "
            "orders that must not outlive the moment, and bulk freight (days) for "
            "standing instructions. Therapy is applied logistics - you cannot "
            "send a standing order by express courier, and you cannot recall "
            "bulk freight once it ships. Every dosing interval in endocrinology "
            "is just the TTL arithmetic made clinical."
        ),
    },
    {
        "key": "gh_axis",
        "name": "The Growth Hormone Axis: GH, IGF-1, and Growth Disorders",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The growth hormone axis is the body's construction schedule: the "
            "hypothalamus releases GHRH (go) and somatostatin (stop), the "
            "pituitary's somatotrophs release growth hormone in nightly pulses, "
            "and GH orders the liver to make IGF-1 (insulin-like growth factor 1), "
            "which does most of the actual growing at the growth plates. GH "
            "secretion peaks in deep sleep and in puberty - adolescents make "
            "roughly a milligram a day - and a healthy prepubertal child grows 5 "
            "to 6 centimeters a year, accelerating to 8 to 12 in the pubertal "
            "spurt. The axis fails in two classic directions. Too little GH in "
            "childhood (growth hormone deficiency) produces proportionate short "
            "stature with a slow growth velocity and delayed bone age, treatable "
            "with recombinant GH. Too much GH after the growth plates fuse "
            "(acromegaly, usually a pituitary adenoma) enlarges hands, feet, jaw, "
            "and organs instead of height, with a diagnostic failure of GH to "
            "suppress below 1 ng/mL during an oral glucose load. This record "
            "teaches the growth axis and its two signature disorders."
        ),
        "how_it_works": (
            "The axis works as a relay with a mediator: GH is the order, IGF-1 is "
            "the foreman that executes it at bone and tissue. Pulsatility is load "
            "bearing - most daily GH leaves in a few large nocturnal bursts tied "
            "to slow-wave sleep, which is why a single random GH level is nearly "
            "useless and diagnosis rests on IGF-1 (which integrates the pulses "
            "into a stable day-long average) plus stimulation or suppression "
            "testing. Feedback closes at two points: IGF-1 suppresses pituitary "
            "GH release, and GH itself feeds back on the hypothalamus. In "
            "childhood the open growth plates convert the signal to height; after "
            "epiphyseal fusion the same signal can only thicken bone and soft "
            "tissue, which is why the timing of excess decides between gigantism "
            "and acromegaly. The demo works the growth arithmetic that clinicians "
            "actually use: centimeters per year at each phase, total pubertal "
            "gain, and the suppression threshold that separates normal from "
            "acromegaly."
        ),
        "key_points": [
            "The axis: hypothalamic GHRH/somatostatin -> pituitary GH (nightly pulses) -> liver IGF-1 -> growth plates.",
            "GH peaks in deep sleep and puberty (~1 mg/day in adolescents); IGF-1 is the stable, measurable integrator.",
            "Growth velocity: 5-6 cm/yr prepubertal, 8-12 cm/yr in the pubertal spurt.",
            "GH deficiency in childhood: proportionate short stature, slow velocity, delayed bone age - treated with recombinant GH.",
            "GH excess after plate fusion (acromegaly): enlarged hands, feet, jaw, organs; GH fails to suppress below 1 ng/mL on glucose load.",
        ],
        "requirements": [
            "The three-level relay with the IGF-1 mediator role stated explicitly.",
            "Why random GH is useless and IGF-1 plus dynamic testing is diagnostic.",
            "The timing rule: excess before fusion makes giants, after fusion makes acromegaly.",
        ],
        "standards": [
            "GH in ng/mL (mcg/L), IGF-1 age- and sex-adjusted; suppression threshold 1 ng/mL per standard criteria.",
            "Growth velocities given as standard pediatric ranges in cm/yr.",
            "Acromegaly diagnosis framed per Endocrine Society guidance (IGF-1 plus OGTT suppression).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Katznelson L, Laws ER Jr, Melmed S, et al. Acromegaly: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2014;99(11):3933-3951.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the growth axis is a construction program with a "
            "foreman (IGF-1) and a build window (open growth plates). The "
            "schedule is transmitted in nightly bursts - the crew works the "
            "night shift - and the project manager audits output, not orders: "
            "IGF-1 is the progress report, growth velocity the earned-value "
            "curve. Miss the window and the same budget only buys renovations, "
            "never new floors."
        ),
    },
    {
        "key": "thyroid_axis",
        "name": "The Thyroid Axis: TSH, T3, T4, and Metabolic Rate",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The thyroid axis sets the body's metabolic thermostat. The "
            "hypothalamus releases TRH, the pituitary answers with TSH, and the "
            "butterfly-shaped thyroid gland in the neck manufactures two iodine-"
            "containing hormones: thyroxine (T4), the abundant prohormone secreted "
            "at roughly 100 micrograms a day, and triiodothyronine (T3), the "
            "potent active hormone produced at about 30 micrograms a day - some "
            "80 percent of it converted from T4 in peripheral tissues by "
            "deiodinase enzymes rather than secreted directly. T3, roughly four "
            "times as potent as T4, binds nuclear receptors in nearly every cell "
            "and sets the pace of oxygen consumption, heat production, heart "
            "rate, gut motility, and brain development. The gland's raw materials "
            "are dietary iodine and the protein thyroglobulin; its warehouse "
            "strategy (months of colloid storage) makes it the most "
            "slow-moving axis in the body. This record teaches the axis that "
            "governs metabolic rate."
        ),
        "how_it_works": (
            "The axis works as a prohormone economy. The thyroid ships mostly "
            "T4 - stable, long-lived, weakly active - and the tissues mint the "
            "active currency T3 on demand by removing one iodine atom, while a "
            "parallel pathway makes the inert reverse T3 as a pressure valve "
            "during illness and starvation. Deiodinases are the local "
            "money-changers: type 1 and 2 activate (T4 to T3), type 3 inactivates "
            "(T4 to reverse T3, T3 to T2). Both T4 and T3 feed back on the "
            "pituitary and hypothalamus to throttle TSH, and the pituitary reads "
            "intracellular T3 converted locally from T4 - which is why TSH "
            "reflects tissue thyroid status even when blood T3 looks odd. Iodine "
            "is the rate-limiting raw material: the gland traps it with the "
            "sodium-iodide symporter, oxidizes it onto thyroglobulin, and couples "
            "iodotyrosines into T4 (four iodines) and T3 (three). The demo works "
            "the daily production budget - T4 secreted, T3 split between direct "
            "secretion and peripheral conversion - and the potency-weighted total "
            "that shows why T4 dominates the circulating pool while T3 does the "
            "work."
        ),
        "key_points": [
            "The axis: TRH -> TSH -> thyroid; T4 (~100 mcg/day, prohormone) and T3 (~30 mcg/day, active hormone).",
            "~80% of daily T3 comes from peripheral conversion of T4, not from direct thyroid secretion.",
            "T3 is ~4x as potent as T4; reverse T3 is the inert pressure valve made during illness.",
            "Deiodinases are local converters: types 1/2 activate, type 3 inactivates.",
            "Raw materials: dietary iodine plus thyroglobulin; the gland stores months of supply in colloid.",
        ],
        "requirements": [
            "The prohormone economy: why the thyroid ships T4 and tissues mint T3 locally.",
            "The deiodinase map: which enzyme activates, which inactivates, and when reverse T3 rises.",
            "The feedback wiring: TSH reflects pituitary intracellular T3, the integrated tissue signal.",
        ],
        "standards": [
            "Daily production values given as standard textbook figures (T4 ~100 mcg, T3 ~30 mcg, 80% conversion).",
            "Potency ratio T3:T4 stated as the standard ~4:1 teaching value.",
            "Free T4 in ng/dL, free T3 in pg/mL, TSH in mIU/L; iodine chemistry (T4 = 4 iodines) stated.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Ross DS, Burch HB, Cooper DS, et al. 2016 American Thyroid Association guidelines for diagnosis and management of hyperthyroidism. Thyroid. 2016;26(10):1343-1421.",
        ],
        "sig_lens": (
            "Signature reading: the thyroid axis is a central bank running a "
            "two-currency system. It issues the reserve currency (T4) in bulk "
            "and lets every province mint the spending currency (T3) locally, "
            "with a demonetization shredder (type 3 deiodinase) for crises. The "
            "vault holds months of reserves, so bank runs are slow - and the "
            "auditor (TSH) watches the money supply with a logarithmic magnifier."
        ),
    },
    {
        "key": "thyroid_disorders",
        "name": "Hyperthyroidism and Hypothyroidism: When the Thyroid Axis Fails",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Thyroid disease is the commonest endocrine disorder physicians treat, "
            "and it fails in exactly two directions. Hypothyroidism - too little "
            "hormone - slows everything: fatigue, weight gain, cold intolerance, "
            "constipation, dry skin, slowed thinking, and a TSH that climbs as the "
            "pituitary shouts at a failing gland. Hashimoto thyroiditis, autoimmune "
            "destruction of the gland, causes most cases in iodine-sufficient "
            "countries; worldwide, iodine deficiency remains the leading cause. "
            "Treatment is levothyroxine at about 1.6 micrograms per kilogram per "
            "day, titrated to normalize TSH. Hyperthyroidism - too much hormone - "
            "accelerates everything: weight loss, heat intolerance, tremor, "
            "palpitations, anxiety, and a suppressed TSH near zero. Graves disease, "
            "autoimmune stimulation of the TSH receptor, causes most cases, with "
            "its signature eye disease and pretibial skin changes. Treatment is "
            "antithyroid drugs (methimazole), radioactive iodine ablation, or "
            "surgery. Subclinical variants - abnormal TSH with normal free T4 - "
            "are the early-warning stage in both directions. This record teaches "
            "the two failure modes and their management."
        ),
        "how_it_works": (
            "Diagnosis works by reading the pair. In primary hypothyroidism the "
            "free T4 is low and the TSH is high - the amplifier doing its job - "
            "and a TSH above 10 mIU/L with a low T4 is overt disease, while a TSH "
            "of 4.5 to 10 with a normal T4 is subclinical. In hyperthyroidism the "
            "TSH is suppressed, usually below 0.1, with high free T4 and T3; the "
            "cause is sorted by radioactive iodine uptake (high in Graves and "
            "toxic nodules, near-zero in thyroiditis where the gland is leaking "
            "rather than overproducing) and by TSH-receptor antibodies. "
            "Levothyroxine replacement works because T4's seven-day half-life "
            "forgives imperfect adherence and peripheral conversion supplies the "
            "T3; the dose is weight-based because distribution follows body mass, "
            "and the recheck comes no sooner than five half-lives - about six "
            "weeks - after any change. The demo works the weight-based dosing "
            "arithmetic for a 70-kilogram adult and the TSH thresholds that "
            "separate subclinical from overt disease in both directions."
        ),
        "key_points": [
            "Hypothyroidism: low T4 + high TSH; Hashimoto thyroiditis is the leading cause where iodine is sufficient.",
            "Hyperthyroidism: suppressed TSH + high T4/T3; Graves disease (TSH-receptor antibodies) is the leading cause.",
            "Subclinical disease: abnormal TSH with normal free T4 - the early-warning stage in both directions.",
            "Levothyroxine ~1.6 mcg/kg/day, rechecked no sooner than ~6 weeks after a dose change (five half-lives).",
            "Radioactive iodine uptake separates overproduction (high uptake) from destructive leaking (near-zero uptake).",
        ],
        "requirements": [
            "The paired reading: TSH plus free T4 interpreted together, never alone.",
            "The two leading causes (Hashimoto, Graves) with their antibody markers (anti-TPO, TRAb).",
            "The dosing and recheck logic derived from T4's half-life, not memorized as bare protocol.",
        ],
        "standards": [
            "TSH thresholds per standard guidance: subclinical 4.5-10 mIU/L, overt >10 with low T4; suppressed <0.1 in overt hyperthyroidism.",
            "Levothyroxine dosing per ATA hypothyroidism guidance (~1.6 mcg/kg/day).",
            "Methimazole named as first-line antithyroid drug; propylthiouracil reserved for first-trimester pregnancy per ATA.",
        ],
        "citations": [
            "Ross DS, Burch HB, Cooper DS, et al. 2016 American Thyroid Association guidelines for diagnosis and management of hyperthyroidism. Thyroid. 2016;26(10):1343-1421.",
            "Jonklaas J, Bianco AC, Bauer AJ, et al. Guidelines for the treatment of hypothyroidism. Thyroid. 2014;24(12):1670-1751.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
        ],
        "sig_lens": (
            "Signature reading: the thyroid fails like a power grid in exactly "
            "two ways - brownout (hypothyroidism) and surge (hyperthyroidism) - "
            "and the control room alarms are wired backwards from intuition: the "
            "thermostat wire (TSH) screams during the brownout and goes silent "
            "during the surge. Replacement therapy is grid engineering: inject "
            "exactly the missing megawatts (weight-based T4) and wait five "
            "time-constants before trusting the meters."
        ),
    },
    {
        "key": "adrenal_cortex",
        "name": "The Adrenal Cortex: Cortisol, Aldosterone, and the Stress Response",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The adrenal cortex is the outer rind of the small triangular gland "
            "sitting atop each kidney, and it manufactures the steroid hormones "
            "that manage stress, salt, and sex-hormone precursors. It is built in "
            "three concentric zones, each with its own product line: the outer "
            "zona glomerulosa makes aldosterone, the salt-retaining "
            "mineralocorticoid that tells the kidney to keep sodium and dump "
            "potassium; the middle zona fasciculata makes cortisol, the "
            "glucocorticoid that mobilizes glucose, suppresses inflammation and "
            "immunity, and carries the stress response; the inner zona reticularis "
            "makes DHEA and other adrenal androgens, the precursors that matter "
            "most before puberty and after menopause. A healthy adult makes about "
            "15 milligrams of cortisol a day (roughly 9 milligrams per square "
            "meter of body surface), released in a circadian rhythm that peaks "
            "near waking and bottoms near midnight, with extra pulses for meals, "
            "exercise, illness, and stress. This record teaches the cortex's "
            "three zones and the two great hormones they ship."
        ),
        "how_it_works": (
            "The cortex works as two separate control loops sharing one "
            "cholesterol supply. Cortisol runs on the HPA axis: hypothalamic CRH "
            "tells the pituitary to release ACTH, ACTH tells the fasciculata to "
            "make cortisol, and cortisol feeds back on both - plus a circadian "
            "clock in the brain gates the whole axis, which is why morning "
            "cortisol is four times midnight cortisol and why night-shift "
            "schedules scramble it. Aldosterone runs on a different loop: the "
            "kidney's renin-angiotensin system and blood potassium tell the "
            "glomerulosa what to make, with ACTH only a minor modulator - so "
            "adrenal failure from pituitary disease loses cortisol but keeps "
            "aldosterone, while primary adrenal failure loses both. Cortisol's "
            "job is permissive and mobilizing: it keeps blood pressure "
            "responsive to catecholamines, keeps glucose available between meals "
            "by opposing insulin, and damps the immune system - the effects "
            "medicine borrows whenever it prescribes steroids. The demo works "
            "the daily production arithmetic (body-surface scaling to the "
            "15-milligram day) and the circadian amplitude that makes timing part "
            "of every cortisol interpretation."
        ),
        "key_points": [
            "Three zones, three product lines: glomerulosa (aldosterone), fasciculata (cortisol), reticularis (adrenal androgens).",
            "Cortisol ~15 mg/day on a circadian rhythm: peaks near waking, nadirs near midnight (~4x amplitude).",
            "Cortisol runs on the HPA axis (ACTH-driven); aldosterone runs on renin-angiotensin and potassium, not ACTH.",
            "Pituitary failure loses cortisol but spares aldosterone; primary adrenal failure loses both.",
            "Cortisol mobilizes glucose, maintains vascular tone, and suppresses immunity - the stress-response toolkit.",
        ],
        "requirements": [
            "The zone-to-hormone map (G-F-R: salt, sugar, sex) with each zone's controller.",
            "The two-loop architecture and why secondary adrenal insufficiency spares aldosterone.",
            "The circadian rhythm and why a random cortisol needs a time stamp to mean anything.",
        ],
        "standards": [
            "Daily cortisol production given as ~8-10 mg/m2/day, ~15 mg/day for 1.73 m2 BSA.",
            "Cortisol in mcg/dL (nmol/L equivalents); aldosterone in ng/dL.",
            "Zone names and the G-F-R mnemonic in standard anatomical order (outer to inner).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Bornstein SR, Allolio B, Arlt W, et al. Diagnosis and treatment of primary adrenal insufficiency: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2024;109(3):e372-e378.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the adrenal cortex is a three-product refinery "
            "with two independent control rooms. The salt desk (aldosterone) "
            "takes orders from the kidney's volume sensors; the crisis desk "
            "(cortisol) takes orders from the brain's alarm system down the HPA "
            "wire. Shared feedstock, separate management - which is exactly why "
            "a headquarters blackout (pituitary failure) idles the crisis desk "
            "while the salt desk keeps shipping."
        ),
    },
    {
        "key": "adrenal_medulla",
        "name": "The Adrenal Medulla: Catecholamines and Fight-or-Flight",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The adrenal medulla is the gland's inner core, and it is really a "
            "sympathetic ganglion that learned to secrete into blood instead of "
            "across a synapse. Its chromaffin cells manufacture the "
            "catecholamines - about 80 percent epinephrine (adrenaline) and 20 "
            "percent norepinephrine - and dump them in a surge whenever the "
            "sympathetic nervous system fires: danger, exercise, hemorrhage, "
            "hypoglycemia, cold. Epinephrine is the broadcast version of the "
            "fight-or-flight order: it accelerates the heart, dilates the "
            "airways, mobilizes glucose from the liver, dilates muscle vessels, "
            "constricts skin and gut vessels, dilates the pupils, and shuts down "
            "digestion - the full emergency posture in one chemical. The response "
            "is measured in seconds because catecholamine half-lives are about "
            "two minutes; the surge is gone almost as fast as it came, which is "
            "why the medulla answers to nerves rather than to slow hormonal "
            "loops. Its tumor, the pheochromocytoma, turns the emergency "
            "broadcast into episodic storms of headache, palpitations, sweating, "
            "and severe hypertension. This record teaches the fast arm of the "
            "adrenal."
        ),
        "how_it_works": (
            "The medulla works as the hormonal loudspeaker of the sympathetic "
            "nervous system. Preganglionic sympathetic fibers release acetylcholine "
            "directly onto chromaffin cells, which respond by exocytosing "
            "catecholamine granules into the bloodstream - neural speed in, "
            "hormonal broadcast out. Epinephrine and norepinephrine then read "
            "different receptor subtypes across tissues: beta-1 speeds and "
            "strengthens the heartbeat, beta-2 opens airways and muscle vessels, "
            "alpha-1 constricts skin and visceral vessels, and the liver's "
            "beta-2 and alpha-1 receptors jointly order glycogen breakdown, "
            "which is why adrenaline both races the pulse and raises blood "
            "sugar. Clearance is by the enzymes COMT and MAO plus rapid tissue "
            "uptake, giving the two-minute half-life that makes the surge "
            "self-terminating. The demo works the hemodynamics of the surge: "
            "resting versus emergency cardiac output from heart rate times stroke "
            "volume, showing the threefold-plus jump one chemical delivers, and "
            "the 80:20 epinephrine-to-norepinephrine manufacturing split."
        ),
        "key_points": [
            "The medulla is a sympathetic ganglion turned endocrine: neural input in, hormonal broadcast out.",
            "Products: ~80% epinephrine, ~20% norepinephrine, released on sympathetic firing.",
            "Effects: faster stronger heartbeat, open airways, mobilized glucose, redistributed blood flow - the emergency posture.",
            "Half-life ~2 minutes: the surge is powerful and self-terminating by design.",
            "Pheochromocytoma: the tumor that fires the emergency broadcast at random - episodic headache, palpitations, sweating, hypertension.",
        ],
        "requirements": [
            "The neural-to-hormonal handoff: acetylcholine in, catecholamines out.",
            "The receptor-subtype map that lets one chemical give different orders to heart, vessels, airways, and liver.",
            "The two-minute half-life and why the medulla answers to nerves, not hormonal loops.",
        ],
        "standards": [
            "Epinephrine:norepinephrine ratio given as the standard ~80:20 medullary split.",
            "Catecholamines in pg/mL; metanephrines as the standard screening metabolites.",
            "Pheochromocytoma described with its classic episodic triad plus hypertension.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the medulla is the panic button wired straight "
            "to the alarm panel. No committees, no feedback loops, no "
            "warehousing - a nerve fires, the broadcast goes out, every "
            "receiver executes its pre-programmed emergency routine, and the "
            "message self-destructs in two minutes. It is the only endocrine "
            "station that answers to electricity instead of chemistry, because "
            "some orders cannot wait for the mail."
        ),
    },
    {
        "key": "cortisol_disorders",
        "name": "Cushing Syndrome and Adrenal Insufficiency: Cortisol Disorders",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Cortisol disorders are mirror images, and both are diagnosed by "
            "catching the axis misbehaving. Cushing syndrome is chronic cortisol "
            "excess - most often from prescribed steroids, and among endogenous "
            "causes most often from a pituitary ACTH-secreting adenoma (Cushing "
            "disease). The body keeps the receipts: central weight gain, a round "
            "plethoric face, a dorsocervical fat pad, purple striae, thin fragile "
            "skin, muscle weakness, hypertension, glucose intolerance, and bone "
            "loss. Screening asks whether the feedback loop is broken: the 1-milligram "
            "overnight dexamethasone suppression test (a normal axis suppresses "
            "morning cortisol below 1.8 mcg/dL; Cushing's does not), late-night "
            "salivary cortisol (the midnight nadir is lost), and 24-hour urinary "
            "free cortisol. Adrenal insufficiency is cortisol deficiency - primary "
            "(Addison disease: the adrenals themselves fail, so ACTH is high and "
            "aldosterone is lost too, with the signature hyperpigmentation from "
            "excess POMC) or secondary (pituitary ACTH failure, aldosterone "
            "spared, no hyperpigmentation). A morning cortisol below 3 mcg/dL "
            "with symptoms confirms it; above 18 rules it out; the cosyntropin "
            "stimulation test settles the middle, with a 60-minute cortisol of at "
            "least 18 mcg/dL (500 nmol/L) passing. Both extremes can kill: "
            "untreated Addisonian crisis and severe Cushing's are emergencies. "
            "This record teaches the two mirror disorders."
        ),
        "how_it_works": (
            "Cushing testing works by interrogating feedback. Dexamethasone is a "
            "synthetic glucocorticoid the cortisol assay does not see: give 1 "
            "milligram at night, and a healthy HPA axis reads it as excess and "
            "shuts down, so morning cortisol falls below 1.8 mcg/dL; an "
            "autonomous source - adrenal tumor, ectopic ACTH, or a pituitary "
            "adenoma deaf to feedback - keeps secreting regardless. Sorting the "
            "ACTH then localizes: high ACTH means the problem is upstream "
            "(pituitary vs ectopic, separated by high-dose dexamethasone "
            "suppression and petrosal sampling), low ACTH means an adrenal "
            "source. Insufficiency testing works the other direction: cosyntropin "
            "is synthetic ACTH, and a healthy adrenal answers with a cortisol "
            "peak of at least 18 mcg/dL - the unit conversion (1 mcg/dL = 27.6 "
            "nmol/L) puts the pass mark at essentially 500 nmol/L, the number "
            "every guideline quotes. The demo works that unit conversion and the "
            "suppression-test arithmetic: baseline versus post-dexamethasone "
            "cortisol as a suppression percentage, showing what passing and "
            "failing look like in numbers."
        ),
        "key_points": [
            "Cushing syndrome: chronic cortisol excess; screen with 1-mg dexamethasone suppression (<1.8 mcg/dL normal), late-night salivary cortisol, urinary free cortisol.",
            "Cushing disease = pituitary ACTH adenoma; ACTH level then separates pituitary, ectopic, and adrenal sources.",
            "Adrenal insufficiency: morning cortisol <3 mcg/dL confirms, >18 rules out; cosyntropin peak >=18 mcg/dL (500 nmol/L) passes.",
            "Primary (Addison): high ACTH + hyperpigmentation + aldosterone lost. Secondary: low ACTH, aldosterone spared, no pigmentation.",
            "Both extremes are emergencies: adrenal crisis needs immediate stress-dose hydrocortisone.",
        ],
        "requirements": [
            "The dexamethasone suppression logic: why a synthetic steroid the assay cannot see tests the feedback loop.",
            "The ACTH-based localization tree for Cushing and for insufficiency.",
            "The cortisol unit conversion (mcg/dL to nmol/L) and the 500 nmol/L pass mark.",
        ],
        "standards": [
            "Cutoffs per Endocrine Society guidance: DST <1.8 mcg/dL, cosyntropin peak >=18 mcg/dL (500 nmol/L).",
            "Cushing disease vs syndrome terminology used in the standard sense.",
            "Emergency management (stress-dose hydrocortisone 100 mg IV) stated per guideline.",
        ],
        "citations": [
            "Nieman LK, Biller BMK, Findling JW, et al. The diagnosis of Cushing's syndrome: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2008;93(5):1526-1540.",
            "Bornstein SR, Allolio B, Arlt W, et al. Diagnosis and treatment of primary adrenal insufficiency: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2024;109(3):e372-e378.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
        ],
        "sig_lens": (
            "Signature reading: cortisol disorders are what happens when the "
            "crisis desk goes rogue - either it never stops shipping (Cushing) "
            "or the warehouse is empty when the alarm sounds (insufficiency). "
            "Diagnosis is penetration testing: inject a fake all-clear "
            "(dexamethasone) and see whether the desk stands down; inject a fake "
            "alarm (cosyntropin) and see whether the warehouse answers. A "
            "control system that fails either test is compromised."
        ),
    },
    {
        "key": "glucose_control",
        "name": "Blood Glucose Control: Insulin, Glucagon, and the Pancreatic Islets",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Blood glucose is the most tightly defended variable in the body "
            "after blood pH, and the pancreatic islets of Langerhans are its "
            "control room. Beta cells read rising glucose and release insulin, "
            "which orders muscle and fat to take up glucose and tells the liver "
            "to stop making it; alpha cells read falling glucose and release "
            "glucagon, which orders the liver to break down glycogen and "
            "manufacture new glucose. The two hormones are antagonists sharing "
            "one bloodstream, and the insulin-to-glucagon ratio is the actual "
            "control signal: high after meals (store), low during fasting "
            "(mobilize). Supporting cast includes somatostatin from delta cells "
            "(the local brake), plus the gut incretins GLP-1 and GIP, which "
            "amplify meal-time insulin release - the reason oral glucose provokes "
            "more insulin than the same glucose given intravenously. Fasting "
            "glucose normally sits between 70 and 100 mg/dL; the system defends "
            "it with counterregulatory backup (epinephrine, cortisol, growth "
            "hormone) if insulin ever overshoots. This record teaches the "
            "glucose control loop that diabetes breaks."
        ),
        "how_it_works": (
            "The beta cell works as a glucose sensor wired to a secretion "
            "machine: glucose enters through GLUT transporters, metabolism "
            "raises the ATP-to-ADP ratio, ATP-sensitive potassium channels "
            "close, the membrane depolarizes, calcium floods in, and insulin "
            "granules fuse with the membrane - metabolism translated directly "
            "into secretion with no neural middleman. Insulin then works "
            "through receptor tyrosine kinases that move GLUT4 transporters to "
            "muscle and fat cell surfaces, opening the gates glucose cannot open "
            "alone. Quantitatively, insulin sensitivity is captured by HOMA-IR: "
            "fasting glucose (mmol/L) times fasting insulin (microU/mL) divided "
            "by 22.5, with values under about 2 considered normal - a fasting "
            "glucose of 5.5 and insulin of 10 gives 2.44, the borderline the "
            "demo computes. The incretin effect adds the feed-forward layer: gut "
            "hormones sense the meal before blood glucose rises and prime the "
            "beta cells, contributing roughly half of post-meal insulin. The "
            "demo works the HOMA-IR arithmetic and the fasting-versus-fed "
            "insulin-glucagon ratio logic."
        ),
        "key_points": [
            "Beta cells release insulin (store glucose); alpha cells release glucagon (mobilize glucose); the insulin:glucagon ratio is the control signal.",
            "The beta cell senses glucose metabolically: glucose -> ATP -> K-channel closure -> calcium -> insulin release.",
            "Incretins (GLP-1, GIP) amplify meal-time insulin - oral glucose provokes more insulin than IV glucose.",
            "Fasting glucose 70-100 mg/dL, defended by counterregulatory hormones (epinephrine, cortisol, GH) against lows.",
            "HOMA-IR = (fasting glucose x fasting insulin)/22.5 quantifies insulin resistance; ~<2 is normal.",
        ],
        "requirements": [
            "The beta-cell stimulus-secretion coupling chain in order.",
            "The insulin:glucagon ratio as the fed-vs-fasted switch.",
            "HOMA-IR computed from a concrete fasting pair with the normal cutoff.",
        ],
        "standards": [
            "Glucose in mg/dL (mmol/L equivalents); insulin in microU/mL; HOMA-IR per the standard Matthews formula.",
            "Incretin effect stated as the standard oral-vs-IV insulin comparison.",
            "Counterregulatory hierarchy named in standard order (glucagon, epinephrine first).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "American Diabetes Association. Standards of Care in Diabetes - 2024. Diabetes Care. 2024;47(Suppl.1):S1-S321.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: glucose control is a dual-dispatch inventory "
            "system. Insulin is the warehousing order (store the surplus), "
            "glucagon the release order (ship from reserves), and the ratio "
            "between them - not either one alone - is the actual instruction. "
            "The gut runs advance shipping notices (incretins) so the warehouse "
            "crew is staged before the delivery truck arrives."
        ),
    },
    {
        "key": "diabetes",
        "name": "Diabetes Mellitus Type 1 and Type 2: Insulin Failure and Resistance",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Diabetes mellitus - 'honey-sweet urine' - is the commonest endocrine "
            "disease on earth, defined by chronic high blood glucose and "
            "diagnosed by numbers: hemoglobin A1C of 6.5 percent or higher, "
            "fasting glucose 126 mg/dL or higher, two-hour glucose 200 or higher "
            "on an oral tolerance test, or a random glucose of 200 or higher with "
            "classic symptoms. Type 1 is autoimmune destruction of the beta "
            "cells - absolute insulin deficiency, usually presenting in youth "
            "with weight loss, thirst, and ketoacidosis, treated with lifelong "
            "insulin. Type 2 is insulin resistance plus progressive beta-cell "
            "failure - the far commoner form, tied to excess weight and "
            "inactivity, often silent for years, managed stepwise from lifestyle "
            "through metformin and newer agents (GLP-1 receptor agonists, "
            "SGLT2 inhibitors) to insulin when the beta cells tire. A1C "
            "translates to estimated average glucose by the formula eAG = 28.7 "
            "x A1C - 46.7, so an A1C of 7.0 percent means an average glucose near "
            "154 mg/dL. Chronic hyperglycemia damages vessels, nerves, kidneys, "
            "and eyes over years - which is why the disease is managed to the "
            "numbers, not to the symptoms. This record teaches the two types, "
            "their diagnosis, and their logic of treatment."
        ),
        "how_it_works": (
            "Type 1 works as an immune system error: autoantibodies (against GAD, "
            "IA-2, ZnT8, insulin itself) mark beta cells for destruction, insulin "
            "falls to zero, and without insulin's brake the liver pours out "
            "glucose while fat breaks down into ketoacids - diabetic ketoacidosis. "
            "Type 2 works as a two-hit process: tissues resist insulin's signal "
            "(receptor and post-receptor defects in muscle, liver, and fat), and "
            "beta cells initially compensate with hyperinsulinemia until they "
            "decompensate over years - which is why type 2 is progressive and "
            "why most patients eventually need more therapy. The eAG formula is a "
            "regression line through the A1C-glucose relationship: every 1 point "
            "of A1C is about 29 mg/dL of average glucose, so the distance from "
            "an A1C of 9 (eAG ~212) to the under-7 target (~154) is a concrete "
            "57 mg/dL of average glucose to erase. The demo works the eAG "
            "arithmetic across the diagnostic and target thresholds and the "
            "threshold table that turns four different tests into one diagnosis."
        ),
        "key_points": [
            "Diagnosis by numbers: A1C >=6.5%, fasting >=126 mg/dL, 2-hour >=200, or random >=200 with symptoms.",
            "Type 1: autoimmune beta-cell destruction, absolute insulin deficiency, lifelong insulin from diagnosis.",
            "Type 2: insulin resistance + progressive beta-cell failure; stepwise therapy as compensation fades.",
            "eAG = 28.7 x A1C - 46.7: A1C 7.0% ~ 154 mg/dL average glucose; each A1C point is ~29 mg/dL.",
            "Complications are vascular, neural, renal, and retinal - the disease is managed to the numbers to prevent them.",
        ],
        "requirements": [
            "The four diagnostic criteria with their exact thresholds.",
            "The two-hit model of type 2 vs the autoimmune model of type 1, with the antibody panel named.",
            "The eAG conversion worked at diagnosis, target, and a high value.",
        ],
        "standards": [
            "Diagnostic thresholds per ADA Standards of Care 2024.",
            "A1C in percent (NGSP), eAG in mg/dL per the ADAG regression.",
            "Autoantibodies named by standard abbreviations (GAD65, IA-2, ZnT8, IAA).",
        ],
        "citations": [
            "American Diabetes Association. Standards of Care in Diabetes - 2024. Diabetes Care. 2024;47(Suppl.1):S1-S321.",
            "Nathan DM, Kuenen J, Borg R, et al. Translating the A1C assay into estimated average glucose values. Diabetes Care. 2008;31(8):1473-1478.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
        ],
        "sig_lens": (
            "Signature reading: diabetes is inventory-system failure in two "
            "flavors. Type 1 is the warehouse crew walking out - no staff, no "
            "storage orders, the loading dock floods. Type 2 is the warehouse "
            "going deaf - the orders arrive but the forklifts ignore them, so "
            "management shouts louder (hyperinsulinemia) until the managers "
            "burn out too. The A1C is the quarterly audit: a three-month "
            "average that cannot be faked the morning of the inspection."
        ),
    },
    {
        "key": "calcium",
        "name": "Calcium Homeostasis: PTH, Vitamin D, and Calcitonin",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Blood calcium is defended within a narrow band - 8.5 to 10.5 mg/dL "
            "total - because nerves, muscle, and the heart misfire outside it, "
            "and the defense is a three-hormone system. Parathyroid hormone "
            "(PTH), from the four parathyroid glands, is the rapid responder: "
            "when ionized calcium falls, PTH rises within minutes, pulling "
            "calcium from bone, reclaiming it in the kidney, and activating "
            "vitamin D. Vitamin D (calcitriol, the active 1,25 form) is the "
            "slow contractor: made in skin from sunlight, hydroxylated in liver "
            "then kidney, it opens the gut's calcium absorption - without it, "
            "dietary calcium mostly passes through. Calcitonin, from the "
            "thyroid's C cells, opposes PTH weakly by quieting bone-resorbing "
            "osteoclasts; it matters more as a tumor marker for medullary "
            "thyroid cancer than as a calcium regulator. The classic disorders "
            "read straight off the loop: primary hyperparathyroidism (high "
            "calcium with inappropriately normal or high PTH, usually a single "
            "adenoma), hypoparathyroidism (low calcium with low PTH, usually "
            "after neck surgery), and vitamin D deficiency (low calcium with "
            "high PTH - secondary hyperparathyroidism - plus soft bones). "
            "Because half of blood calcium rides on albumin, every total calcium "
            "is corrected for albumin: corrected = measured + 0.8 x (4.0 - "
            "albumin). This record teaches the mineral loop."
        ),
        "how_it_works": (
            "The parathyroid works as a calcium sensor with a set point: its "
            "calcium-sensing receptors (the same receptor family that the drug "
            "cinacalcet tickles) suppress PTH release when ionized calcium is "
            "normal and release the brake within minutes when it falls. PTH then "
            "acts on three fronts at once - bone (osteoclasts liberate calcium "
            "within hours), kidney (distal tubule reclaims calcium, dumps "
            "phosphate), and kidney again (1-alpha-hydroxylase activates vitamin "
            "D, which then multiplies gut absorption over days). Phosphate is "
            "the shadow variable: PTH lowers it while raising calcium, so the "
            "calcium-phosphate pair points at the diagnosis - high calcium with "
            "low phosphate suggests PTH-driven disease. The albumin correction "
            "is linear bookkeeping: each 1 g/dL of albumin below 4.0 binds about "
            "0.8 mg/dL of calcium, so a measured 8.0 with an albumin of 3.0 is "
            "really 8.8 - still low, but less alarming than the raw number. The "
            "demo works the correction arithmetic and the PTH response timing "
            "that makes calcium the fastest mineral loop in the body."
        ),
        "key_points": [
            "PTH is the rapid calcium defender: bone release, kidney reclaim, vitamin D activation - all within minutes to hours.",
            "Vitamin D is the slow contractor: enables gut calcium absorption over days; deficiency causes secondary hyperparathyroidism.",
            "Calcitonin weakly opposes PTH; its clinical role is mainly as a medullary thyroid cancer marker.",
            "Read calcium with phosphate and PTH together: the trio localizes the lesion.",
            "Correct every total calcium for albumin: corrected = measured + 0.8 x (4.0 - albumin).",
        ],
        "requirements": [
            "The three-front PTH action (bone, kidney calcium, vitamin D activation) with time scales.",
            "The calcium-phosphate pair as a diagnostic compass.",
            "The albumin correction worked numerically, with the bound-vs-ionized rationale.",
        ],
        "standards": [
            "Calcium in mg/dL (mmol/L equivalents), PTH in pg/mL, 25-OH vitamin D in ng/mL (sufficiency >=30).",
            "Correction formula per standard clinical practice.",
            "Primary hyperparathyroidism, hypoparathyroidism, and vitamin D deficiency framed by their calcium-PTH-phosphate patterns.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: calcium is the treasury reserve - too precious "
            "to float, too dangerous to spike. PTH is the central bank's "
            "trading desk, intervening in minutes; vitamin D is the trade "
            "ministry, negotiating supply contracts over weeks. The books are "
            "kept in two columns (calcium and phosphate) because every "
            "treasury operation moves both, and the auditor reads the pair to "
            "catch which desk is cooking the books."
        ),
    },
    {
        "key": "male_repro",
        "name": "Male Reproductive Endocrinology: Testosterone and Spermatogenesis",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Male reproductive endocrinology is the HPG axis in its male "
            "configuration: hypothalamic GnRH pulses drive pituitary LH and FSH, "
            "LH tells the testicular Leydig cells to make testosterone (5 to 7 "
            "milligrams a day in a healthy man), and FSH plus intratesticular "
            "testosterone drive the Sertoli cells that nurse sperm production. "
            "Testosterone's portfolio is broad - libido, erections, muscle mass, "
            "bone density, red blood cell production, mood, and the maintenance "
            "of spermatogenesis itself - which is why hypogonadism presents as a "
            "constellation: low libido, erectile difficulty, fatigue, loss of "
            "muscle, anemia, and infertility. The feedback logic from the "
            "foundations records applies directly: primary testicular failure "
            "shows low testosterone with high LH and FSH, while pituitary "
            "failure shows all three low. Spermatogenesis is a 64-to-72-day "
            "pipeline producing on the order of a hundred million sperm a day, "
            "so any insult - illness, heat, drugs - shows up in the semen "
            "analysis two to three months later. This record teaches the male "
            "axis and its clinical reading."
        ),
        "how_it_works": (
            "The testis works as two factories under one roof. Leydig cells sit "
            "in the interstitial space and convert cholesterol to testosterone "
            "on LH orders; most of it binds SHBG and albumin in blood, leaving "
            "about 2 percent free and active, and some is aromatized to "
            "estradiol in fat and brain - men need a little estrogen too, for "
            "bone and libido. Sertoli cells line the seminiferous tubules and, "
            "on FSH plus high local testosterone, shepherd germ cells through "
            "the 64-day metamorphosis from spermatogonium to spermatozoon; they "
            "also secrete inhibin B, which feeds back specifically on FSH, "
            "giving the pituitary a separate report card on the sperm factory "
            "apart from the testosterone factory. Diagnosis reads the trio: "
            "morning total testosterone (the circadian peak) with LH and FSH, "
            "drawn fasting before 10 AM on two occasions. The demo works the "
            "pipeline arithmetic - daily output times the 64-day transit gives "
            "the in-flight inventory - and the feedback patterns that separate "
            "testicular from pituitary failure."
        ),
        "key_points": [
            "The male HPG axis: GnRH -> LH/FSH -> Leydig testosterone (5-7 mg/day) + Sertoli-cell spermatogenesis.",
            "Two factories: Leydig (testosterone, LH-driven) and Sertoli (sperm, FSH + testosterone-driven, reports via inhibin B).",
            "Only ~2% of testosterone is free and active; SHBG changes mislead total-testosterone readings.",
            "Primary failure: low testosterone + high LH/FSH. Pituitary failure: all low.",
            "Spermatogenesis takes 64-72 days: semen analysis reflects insults from 2-3 months earlier.",
        ],
        "requirements": [
            "The two-compartment testis model with each compartment's driver and feedback reporter.",
            "The free-vs-total testosterone distinction and the morning-draw rule.",
            "The pipeline-delay logic linking exposure timing to semen analysis results.",
        ],
        "standards": [
            "Testosterone in ng/dL (nmol/L equivalents); morning reference roughly 300-1000 ng/dL per standard ranges.",
            "Hypogonadism diagnosis per Endocrine Society guidance (symptoms plus two low morning totals).",
            "Semen parameters per WHO 6th edition thresholds (15 million/mL concentration).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Bhasin S, Brito JP, Cunningham GR, et al. Testosterone therapy in men with hypogonadism: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2018;103(5):1715-1744.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the testis is a dual-plant industrial site with "
            "separate management chains - the chemical plant (testosterone, "
            "reports to LH) and the assembly line (sperm, reports to FSH via "
            "inhibin). The 64-day conveyor means quality control always lags "
            "the incident by a quarter: today's defect report describes last "
            "season's working conditions."
        ),
    },
    {
        "key": "female_repro",
        "name": "Female Reproductive Endocrinology: Estrogen, Progesterone, and the Cycle",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Female reproductive endocrinology is the HPG axis running its most "
            "complex program: the 28-day menstrual cycle, a precisely timed "
            "sequence that matures an egg, prepares the uterus, and - uniquely "
            "in human endocrinology - flips negative feedback to positive "
            "feedback at ovulation. The follicular phase (about 14 days): FSH "
            "recruits ovarian follicles, the dominant follicle secretes rising "
            "estradiol (peaking at 200-400 pg/mL), which thickens the uterine "
            "lining. Ovulation (about day 14): sustained high estradiol switches "
            "the feedback sign, triggering the LH surge that ruptures the "
            "follicle. The luteal phase (about 14 days): the ruptured follicle "
            "becomes the corpus luteum, secreting progesterone that matures the "
            "lining for implantation; without pregnancy the corpus luteum dies, "
            "hormones fall, and menstruation follows. A luteal progesterone "
            "above 3 ng/mL confirms ovulation happened. The cycle's disorders - "
            "polycystic ovary syndrome, hypothalamic amenorrhea, premature "
            "ovarian insufficiency, menopause - are all failures of specific "
            "cycle steps. This record teaches the cycle as an endocrine program."
        ),
        "how_it_works": (
            "The cycle works as a state machine with four states and one sign "
            "flip. In the follicular state, estradiol exerts negative feedback, "
            "keeping FSH just high enough to grow one follicle while starving "
            "the rest - a selection tournament. When estradiol stays above "
            "about 200 pg/mL for roughly 50 hours, the feedback sign inverts: "
            "the pituitary, primed by GnRH pulse acceleration, releases the LH "
            "surge, a tenfold spike that completes meiosis and ruptures the "
            "follicle about 36 hours later. The luteal state is a timed "
            "self-destruct: the corpus luteum has a 14-day lifespan unless "
            "rescued by hCG from an implanting embryo, which is why the luteal "
            "phase is the metronome-constant part of the cycle and variation in "
            "cycle length comes almost entirely from the follicular phase. The "
            "fertile window is the six days ending on ovulation day - five days "
            "of sperm survival plus the egg's 24 hours. The demo works the "
            "cycle-day arithmetic: phase boundaries, the fertile window, and "
            "the progesterone threshold that proves ovulation occurred."
        ),
        "key_points": [
            "The 28-day program: follicular (~14 d) -> ovulation (~day 14) -> luteal (~14 d) -> menstruation.",
            "Ovulation is the positive-feedback exception: sustained high estradiol triggers the LH surge.",
            "The luteal phase is a fixed ~14 days; cycle-length variation lives in the follicular phase.",
            "Luteal progesterone >3 ng/mL confirms ovulation; estradiol peaks 200-400 pg/mL before the surge.",
            "The fertile window is the 6 days ending on ovulation day.",
        ],
        "requirements": [
            "The four states in order with each state's dominant hormone and job.",
            "The feedback sign flip: conditions, threshold, and the LH surge timing.",
            "The fertile-window and ovulation-confirmation arithmetic.",
        ],
        "standards": [
            "Estradiol in pg/mL, progesterone in ng/mL, LH/FSH in mIU/mL per standard reporting.",
            "Cycle day 1 defined as first day of menses per standard convention.",
            "Ovulation confirmation threshold (>3 ng/mL luteal progesterone) per standard practice.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the menstrual cycle is the most sophisticated "
            "program the HPG axis runs - a monthly build-and-test cycle with a "
            "selection tournament (one follicle wins), a sign-flipping trigger "
            "(the LH surge), and a two-week acceptance test (the luteal phase) "
            "that either ships the product (pregnancy rescues the corpus "
            "luteum) or scraps the build and restarts (menstruation)."
        ),
    },
    {
        "key": "posterior_pituitary",
        "name": "The Posterior Pituitary: Oxytocin, Vasopressin, and Water Balance",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The posterior pituitary releases two nine-amino-acid hormones that "
            "were manufactured upstream in the hypothalamus: oxytocin and "
            "vasopressin (antidiuretic hormone, ADH). Oxytocin drives uterine "
            "contraction in labor and milk ejection during nursing, and it "
            "modulates social bonding - the physiology behind its 'bonding "
            "hormone' nickname. Vasopressin is the body's water-conservation "
            "order: it tells the kidney's collecting ducts to insert aquaporin "
            "water channels and reclaim free water, concentrating the urine up "
            "to 1200 mOsm/kg when water is scarce. The vasopressin system is "
            "exquisitely sensitive - a 1 percent rise in blood osmolarity "
            "measurably raises ADH - because water balance cannot wait. Its "
            "failures are mirror images: central diabetes insipidus (too little "
            "ADH - massive dilute urine, unquenchable thirst, from pituitary "
            "damage) and SIADH (too much ADH - water retention diluting blood "
            "sodium, from lung disease, drugs, or tumors). This record teaches "
            "the release terminal and its two dispatches."
        ),
        "how_it_works": (
            "Vasopressin works as a proportional controller on water: "
            "hypothalamic osmoreceptors shrink as plasma osmolarity rises, "
            "firing the magnocellular neurons harder, and ADH release rises "
            "steeply - roughly a tenfold hormone increase across the "
            "physiological osmolarity range - while thirst provides the backup "
            "intake arm. In the kidney, ADH binds V2 receptors on collecting-"
            "duct cells, raising cAMP, which shuttles aquaporin-2 channels into "
            "the luminal membrane; water follows the medullary osmotic gradient "
            "out of the tubule, and urine concentrates. Remove ADH and the "
            "channels are withdrawn within minutes - urine output can exceed a "
            "liter an hour in diabetes insipidus. The diagnostic water-"
            "deprivation test exploits this: a healthy kidney concentrates "
            "urine above 800 mOsm/kg when deprived, a central-DI kidney cannot "
            "until given desmopressin (synthetic ADH), and a nephrogenic-DI "
            "kidney cannot even then. The demo works the controller gain - "
            "percent ADH rise per percent osmolarity rise - and the urine "
            "concentration thresholds that separate the diagnoses."
        ),
        "key_points": [
            "Posterior pituitary releases two hypothalamic hormones: oxytocin (labor, lactation, bonding) and vasopressin/ADH (water conservation).",
            "ADH is a proportional controller: ~1% osmolarity rise measurably raises ADH; urine can concentrate to 1200 mOsm/kg.",
            "Mechanism: V2 receptor -> cAMP -> aquaporin-2 insertion -> water reclaimed in the collecting duct.",
            "Too little ADH: central diabetes insipidus (huge dilute urine + thirst). Too much: SIADH (water retention, low sodium).",
            "Water-deprivation test: healthy concentrates >800 mOsm/kg; desmopressin response separates central from nephrogenic DI.",
        ],
        "requirements": [
            "The osmoreceptor-to-aquaporin chain in order with the second messenger named.",
            "The gain concept: why small osmolarity changes drive large ADH swings.",
            "The deprivation-test logic tree distinguishing central DI, nephrogenic DI, and primary polydipsia.",
        ],
        "standards": [
            "Osmolarity in mOsm/kg, serum sodium in mEq/L; normal serum osmolality 275-295.",
            "Urine concentration thresholds per standard DI workup.",
            "Desmopressin named as the synthetic ADH analogue used diagnostically and therapeutically.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: vasopressin is the water-rationing order, and "
            "its control loop is the tightest in the building - a one-percent "
            "deviation moves the needle, because dehydration compounds "
            "fatally. The kidney is a smart valve: ADH is the signal that "
            "screws it toward conservation, and the valve springs back to "
            "full flow the moment the signal stops. Oxytocin, meanwhile, is "
            "the dispatch that starts the two most physical processes in "
            "human life - birth and nursing."
        ),
    },
    {
        "key": "neuroendocrinology",
        "name": "Neuroendocrinology: The Brain as an Endocrine Organ",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Neuroendocrinology is the study of the brain's own hormone "
            "production - the neurons that double as endocrine cells and the "
            "feedback loops that close through neural tissue. Its flagship is "
            "the pineal gland's melatonin: synthesized from serotonin in "
            "darkness on orders relayed from the retina through the "
            "suprachiasmatic nucleus (the circadian master clock), melatonin "
            "rises around 9 PM (dim-light melatonin onset), peaks between 2 and "
            "4 AM, and falls before waking - the chemical signal of night that "
            "times sleep, seasonal reproduction in animals, and puberty's "
            "calendar in humans. The wider field covers the hypothalamic "
            "releasing hormones themselves, the endorphin and enkephalin opioid "
            "peptides made in brain and pituitary, leptin signaling through "
            "hypothalamic appetite circuits, and the stress circuitry where "
            "cortisol feeds back on the hippocampus and amygdala. "
            "Neuroendocrine tumors - from pituitary adenomas to gut carcinoids "
            "to small-cell lung cancers secreting ACTH or ADH - are the "
            "pathology where the brain-gut-lung hormone network goes rogue. "
            "This record teaches the brain's endocrine double life."
        ),
        "how_it_works": (
            "Melatonin synthesis works as a darkness-gated assembly line: light "
            "hitting retinal ganglion cells signals the suprachiasmatic nucleus, "
            "which during daylight actively suppresses the pineal via "
            "sympathetic nerves; at dusk the suppression lifts, norepinephrine "
            "drives pinealocytes, and serotonin is acetylated then methylated "
            "into melatonin - the whole pathway switched by the light-dark "
            "cycle rather than by blood chemistry. The circadian cortisol "
            "rhythm runs the complementary program: the clock gates HPA drive "
            "so cortisol peaks near 8 AM around 20 mcg/dL and troughs near "
            "midnight near 5 mcg/dL, a fourfold amplitude that the demo "
            "computes, which is why 'morning person' physiology is partly "
            "scheduled hormone delivery. Leptin closes the energy loop through "
            "the arcuate nucleus: fat mass sets leptin, leptin reports to "
            "hypothalamic POMC and AgRP neurons, and appetite adjusts - the "
            "long-term adipostat that dieting fights. The demo works the "
            "melatonin timing landmarks and the cortisol circadian amplitude "
            "that makes time-of-day a laboratory variable."
        ),
        "key_points": [
            "The brain makes hormones: hypothalamic releasing factors, pineal melatonin, endogenous opioids.",
            "Melatonin is the chemical signal of night: rises ~9 PM, peaks 2-4 AM, gated by light via the suprachiasmatic nucleus.",
            "Cortisol runs a circadian program: ~20 mcg/dL at 8 AM, ~5 mcg/dL at midnight - a 4x amplitude.",
            "Leptin reports fat mass to hypothalamic appetite circuits - the long-term adipostat.",
            "Neuroendocrine tumors (pituitary, carcinoid, small-cell lung) are ectopic hormone secretion from neural-crest-derived tissue.",
        ],
        "requirements": [
            "The light-to-melatonin pathway in order: retina -> SCN -> sympathetic -> pineal -> melatonin.",
            "The cortisol circadian curve with its amplitude and clinical consequence (timed blood draws).",
            "The leptin-hypothalamus appetite loop as the energy-balance sensor.",
        ],
        "standards": [
            "Melatonin timing landmarks per standard chronobiology (DLMO ~21:00, peak 02:00-04:00).",
            "Cortisol values in mcg/dL with the standard morning/evening reference split.",
            "Tumor types named by standard pathology (carcinoid, small-cell carcinoma).",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: neuroendocrinology is where the network's "
            "control plane and data plane merge - the same tissue that computes "
            "also secretes. Melatonin is the broadcast time signal, the "
            "chemical equivalent of a radio time station: every cell with a "
            "clock can synchronize to nightfall. Cortisol's circadian wave is "
            "the scheduled shift change, and leptin is the fuel gauge wired "
            "straight into the appetite throttle."
        ),
    },
    {
        "key": "endocrine_tumors",
        "name": "Endocrine Tumors: Adenomas, Pheochromocytoma, and MEN Syndromes",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Endocrine tumors are unusual: most are benign adenomas, yet even a "
            "benign hormone-secreting tumor can be lethal through its product, "
            "and a millimeter-scale pituitary adenoma can flood the body with "
            "ACTH or growth hormone. The cast: pituitary adenomas (prolactinomas "
            "the commonest, then GH and ACTH-secreting), parathyroid adenomas "
            "(the usual cause of primary hyperparathyroidism - one rogue gland "
            "out of four), adrenal adenomas (cortisol-secreting in Cushing "
            "syndrome, aldosterone-secreting in primary aldosteronism), "
            "pheochromocytomas (adrenal medulla catecholamine storms), thyroid "
            "cancers (covered in their own record), pancreatic neuroendocrine "
            "tumors (insulinomas causing fasting hypoglycemia, gastrinomas, "
            "VIPomas), and medullary thyroid cancer from the calcitonin-making "
            "C cells. The inherited syndromes tie them together: MEN1 (menin "
            "gene - parathyroid, pituitary, and pancreatic tumors; "
            "hyperparathyroidism strikes about 95 percent by age 50), MEN2 "
            "(RET gene - medullary thyroid cancer in about 90 percent plus "
            "pheochromocytoma and hyperparathyroidism), and von Hippel-Lindau. "
            "The classic '10 percent rule' for pheochromocytoma - 10 percent "
            "malignant, 10 percent bilateral, 10 percent extra-adrenal - "
            "remains the teaching shorthand. This record maps the tumor "
            "landscape and its genetics."
        ),
        "how_it_works": (
            "Endocrine tumor diagnosis works by catching the product, not the "
            "lump: an insulinoma is found because supervised fasting provokes "
            "hypoglycemia with inappropriately unsuppressed insulin; a "
            "pheochromocytoma because plasma metanephrines - the catecholamine "
            "metabolites that tumors leak continuously even between surges - are "
            "elevated; a gastrinoma because fasting gastrin is high with a low "
            "gastric pH. The genetics work as tumor-suppressor or oncogene "
            "logic: MEN1's menin is a suppressor (two hits required, hence the "
            "multiplicity of tumors), while RET in MEN2 is an activated "
            "oncogene (one hit suffices, hence the near-certain medullary "
            "thyroid cancer and the recommendation for prophylactic "
            "thyroidectomy in childhood for the highest-risk mutations). "
            "Penetrance arithmetic turns family history into action: with 95 "
            "percent penetrance of hyperparathyroidism in MEN1, screening "
            "calcium in carriers is not optional. The demo works the "
            "pheochromocytoma 10-percent-rule compound probability and the "
            "MEN1 penetrance expectation across a carrier cohort."
        ),
        "key_points": [
            "Most endocrine tumors are benign adenomas - but benign plus hormone-secreting can still be lethal.",
            "Diagnosis catches the product: metanephrines (pheo), fasting insulin (insulinoma), gastrin (gastrinoma).",
            "MEN1 (menin): parathyroid + pituitary + pancreatic tumors; ~95% develop hyperparathyroidism by 50.",
            "MEN2 (RET): medullary thyroid cancer ~90% penetrance; highest-risk mutations warrant childhood prophylactic thyroidectomy.",
            "The pheochromocytoma 10% rule: 10% malignant, 10% bilateral, 10% extra-adrenal.",
        ],
        "requirements": [
            "The product-first diagnostic logic with one concrete test per tumor type.",
            "The MEN1/MEN2 gene-to-tumor maps with penetrance figures.",
            "The suppressor-vs-oncogene distinction and why it changes surgical timing.",
        ],
        "standards": [
            "Gene names in standard form (MEN1/menin, RET); penetrance figures as standard teaching values.",
            "Biochemical tests named per guideline (plasma free metanephrines, 72-hour fast, secretin stimulation).",
            "Tumor nomenclature per WHO endocrine tumor classification.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Brandi ML, Gagel RF, Angeli A, et al. Guidelines for diagnosis and therapy of MEN type 1 and type 2. J Clin Endocrinol Metab. 2001;86(12):5658-5671.",
            "Wells SA Jr, Asa SL, Dralle H, et al. Revised American Thyroid Association guidelines for the management of medullary thyroid carcinoma. Thyroid. 2015;25(6):567-610.",
        ],
        "sig_lens": (
            "Signature reading: endocrine tumors are rogue transmitters - "
            "usually low-power (benign), always unauthorized, and dangerous "
            "because the network obeys any properly formatted message no "
            "matter who sends it. The inherited syndromes are compromised "
            "source code: MEN1 ships with a broken failsafe (tumor suppressor "
            "lost), MEN2 with a stuck accelerator (oncogene on). Counter-"
            "intelligence is biochemical: you find the rogue station by its "
            "transmissions, not by sweeping the terrain."
        ),
    },
    {
        "key": "pcos",
        "name": "Polycystic Ovary Syndrome: The Commonest Endocrine Disorder",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Polycystic ovary syndrome (PCOS) is the commonest endocrine disorder "
            "in reproductive-age women, affecting roughly 8 to 13 percent - in a "
            "thousand women, 80 to 130. Diagnosis uses the Rotterdam criteria: "
            "two of three features - irregular or absent ovulation, clinical or "
            "biochemical signs of excess androgen (hirsutism, acne, elevated "
            "testosterone), and polycystic-appearing ovaries on ultrasound - "
            "after excluding look-alikes (thyroid disease, hyperprolactinemia, "
            "congenital adrenal hyperplasia, androgen-secreting tumors). The "
            "engine underneath is insulin resistance driving the ovaries: high "
            "insulin amplifies LH-driven androgen production by theca cells and "
            "suppresses SHBG, raising free testosterone - which is why PCOS "
            "travels with weight gain, acanthosis nigricans, and a steep future "
            "risk of type 2 diabetes, and why weight loss and insulin-sensitizing "
            "therapy are first-line. Management is goal-directed: combined "
            "hormonal contraceptives regulate cycles and suppress androgens, "
            "metformin addresses the metabolic root, letrozole is first-line for "
            "ovulation induction when pregnancy is wanted, and anti-androgens "
            "treat hirsutism. This record teaches the commonest disorder in the "
            "specialty."
        ),
        "how_it_works": (
            "PCOS works as a vicious cycle with insulin at the hub. Insulin "
            "resistance raises circulating insulin; insulin acts on ovarian "
            "theca cells through their IGF-1 receptors to boost androgen "
            "synthesis and on the liver to suppress SHBG production, so free "
            "testosterone rises by two mechanisms at once. Excess androgen "
            "disrupts GnRH pulsatility toward rapid LH-favoring pulses, which "
            "further drives theca androgen production while FSH stays too low "
            "to mature follicles - follicles stall at the small antral stage, "
            "accumulating as the 'polycystic' ultrasound appearance, and "
            "ovulation fails. The Rotterdam two-of-three rule is combinatorial: "
            "three criteria taken two or three at a time yield exactly four "
            "phenotypes (all three, or each pair), which is why two women with "
            "'PCOS' can look quite different - one anovulatory with hirsutism "
            "and normal ovaries, another ovulatory with polycystic ovaries and "
            "hyperandrogenism. The demo works the phenotype combinatorics and "
            "the prevalence arithmetic that makes PCOS the highest-volume "
            "diagnosis in reproductive endocrinology."
        ),
        "key_points": [
            "PCOS affects 8-13% of reproductive-age women - the commonest endocrine disorder.",
            "Rotterdam criteria: 2 of 3 (anovulation, hyperandrogenism, polycystic ovaries) after excluding mimics.",
            "The engine is insulin resistance: high insulin drives ovarian androgens and suppresses SHBG, raising free testosterone.",
            "Four phenotypes exist: all three criteria, or each of the three possible pairs.",
            "Management is goal-directed: contraceptives for cycles/androgens, metformin for metabolism, letrozole for ovulation induction.",
        ],
        "requirements": [
            "The Rotterdam two-of-three rule with the exclusion list.",
            "The insulin-theca-SHBG mechanism stated as the unifying pathophysiology.",
            "The four-phenotype combinatorics and why presentation varies.",
        ],
        "standards": [
            "Prevalence 8-13% per the 2023 international evidence-based guideline (Teede et al.).",
            "Rotterdam criteria per ESHRE/ASRM consensus; letrozole first-line for ovulation induction per 2023 guideline.",
            "Androgen excess defined clinically (hirsutism, acne) or biochemically (elevated free testosterone).",
        ],
        "citations": [
            "Teede HJ, Tay CT, Laven JJE, et al. Recommendations from the 2023 international evidence-based guideline for the assessment and management of polycystic ovary syndrome. J Clin Endocrinol Metab. 2023;108(10):2447-2469.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: PCOS is a feedback network captured by a "
            "metabolic hijacker. Insulin - a signal from a different department "
            "(energy) - cross-talks into the reproductive control loop, "
            "retunes the pulse generator, and stalls the production line at "
            "the quality-control gate. Four phenotypes, one hijack: the "
            "combinatorics of the diagnostic rule map exactly onto which "
            "stations the intruder has reached."
        ),
    },
    {
        "key": "thyroid_nodules",
        "name": "Thyroid Nodules and Thyroid Cancer: Evaluation Basics",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Thyroid nodules are extraordinarily common - palpable in about 5 "
            "percent of women, visible on ultrasound in up to half of adults - "
            "and the clinical question is always the same: is it cancer, and "
            "does it make hormone? The workup runs in order: TSH first (a low "
            "TSH means the nodule may be autonomous - confirm with a "
            "radioactive iodine scan showing a 'hot' nodule, which is rarely "
            "malignant), then ultrasound risk stratification, then fine-needle "
            "aspiration biopsy for nodules meeting size and suspicion "
            "thresholds. Cytology is reported in the six Bethesda categories, "
            "each carrying a standard malignancy risk from about 2 percent "
            "(benign, category II) to about 97 percent (malignant, category "
            "VI), with the indeterminate middle (III, IV) triaged by molecular "
            "testing or diagnostic surgery. Differentiated thyroid cancer "
            "(papillary and follicular) is usually curable - surgery plus "
            "selective radioactive iodine, then lifelong TSH suppression with "
            "levothyroxine - while medullary cancer (C cells, calcitonin "
            "marker) and anaplastic cancer play by tougher rules. This record "
            "teaches the nodule workup that every clinician runs."
        ),
        "how_it_works": (
            "The workup works as a funnel that spends the expensive tests only "
            "on the suspicious minority. TSH stratifies function: suppressed TSH "
            "points to autonomy (scan it), normal or high TSH points to "
            "non-functioning tissue (ultrasound it). Ultrasound stratifies "
            "anatomy: solid hypoechoic nodules with irregular margins, "
            "microcalcifications, or taller-than-wide shape earn biopsy at "
            "smaller sizes; spongiform or purely cystic nodules are reassuring. "
            "Bethesda cytology then converts the microscope into a probability: "
            "with risks of roughly 10, 2, 15, 25, 70, and 97 percent across "
            "categories I through VI, the category is a number the surgeon can "
            "operate on - or watch. The demo works the funnel arithmetic: in a "
            "hundred biopsied Bethesda II nodules at 2 percent risk, the "
            "expected cancers are two - the calculation that justifies watching "
            "rather than operating on the benign majority."
        ),
        "key_points": [
            "Nodules are common (palpable ~5% of women, ultrasound-visible in up to half of adults); the questions are malignancy and function.",
            "Workup order: TSH -> ultrasound risk stratification -> fine-needle aspiration at thresholds.",
            "Hot nodules (low TSH, avid on scan) are rarely malignant; the cancer hunt focuses on non-functioning nodules.",
            "Bethesda I-VI cytology carries malignancy risks ~10/2/15/25/70/97% - the category is an actionable probability.",
            "Differentiated thyroid cancer is usually curable: surgery + selective radioiodine + TSH suppression.",
        ],
        "requirements": [
            "The funnel order and what each step rules in or out.",
            "The Bethesda six-category risk ladder with the actionable middle.",
            "The hot-vs-cold distinction and why function changes the workup.",
        ],
        "standards": [
            "Bethesda risks per the ATA differentiated thyroid cancer guidelines (Haugen et al. 2015).",
            "TSH in mIU/L; nodule size thresholds per ATA ultrasound patterns.",
            "Calcitonin as the medullary cancer marker per ATA medullary guidelines.",
        ],
        "citations": [
            "Haugen BR, Alexander EK, Bible KC, et al. 2015 American Thyroid Association management guidelines for adult patients with thyroid nodules and differentiated thyroid cancer. Thyroid. 2016;26(1):1-133.",
            "Wells SA Jr, Asa SL, Dralle H, et al. Revised American Thyroid Association guidelines for the management of medullary thyroid carcinoma. Thyroid. 2015;25(6):567-610.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
        ],
        "sig_lens": (
            "Signature reading: the nodule workup is a triage funnel engineered "
            "to protect the majority from the scalpel. Each stage is a cheaper, "
            "safer test that disqualifies the innocent - blood test, sound "
            "waves, needle - so that only the statistically guilty reach the "
            "operating room. Bethesda is the sentencing grid: six categories, "
            "each with a published recidivism rate, each with a proportionate "
            "response."
        ),
    },
    {
        "key": "pituitary_tumors",
        "name": "Pituitary Tumors and Hyperprolactinemia: Reading the Sella",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Pituitary adenomas are the commonest sellar masses, and they "
            "present through three mechanisms: what they secrete, what they "
            "crush, and what they fail to make. Prolactinomas are the commonest "
            "secretory type (about 40 percent of pituitary adenomas): excess "
            "prolactin suppresses GnRH, causing galactorrhea, amenorrhea, and "
            "infertility in women and low libido, erectile dysfunction, and "
            "infertility in men - hyperprolactinemia is one of the commonest "
            "treatable causes of infertility. GH-secreting adenomas cause "
            "acromegaly; ACTH-secreting adenomas cause Cushing disease. Size "
            "classifies: microadenomas under 10 millimeters, macroadenomas 10 "
            "and above - and size matters because the optic chiasm sits just "
            "above the sella, so a growing macroadenoma classically clips the "
            "outer visual fields (bitemporal hemianopia) as it presses upward. "
            "Large non-secreting tumors crush the normal gland into "
            "hypopituitarism, GH usually falling first. The therapeutic "
            "standout: prolactinomas usually melt under dopamine agonists "
            "(cabergoline normalizes prolactin in about 90 percent), often "
            "without surgery. This record teaches the sellar mass and its "
            "three presentation modes."
        ),
        "how_it_works": (
            "Hyperprolactinemia works through disinhibition logic: dopamine "
            "from the hypothalamus tonically brakes prolactin, so anything that "
            "interrupts the brake - a prolactinoma, a stalk-compressing tumor, "
            "or dopamine-blocking drugs like antipsychotics - raises prolactin. "
            "Prolactin then suppresses GnRH pulsatility, shutting down the "
            "reproductive axis - which is why the infertility of "
            "hyperprolactinemia reverses when prolactin normalizes. Sorting the "
            "cause uses the level: prolactin above about 100 ng/mL usually "
            "means a true prolactinoma, modest elevations suggest stalk effect "
            "or drugs, and every workup excludes pregnancy, hypothyroidism "
            "(high TRH drives prolactin), and renal failure first. Volume "
            "arithmetic makes the size classification concrete: a sphere's "
            "volume grows with the cube of its radius, so a 12-millimeter "
            "adenoma holds more than three times the tissue of an 8-millimeter "
            "one - the demo computes exactly that ratio, showing why a few "
            "millimeters toward the optic chiasm change the surgical urgency."
        ),
        "key_points": [
            "Pituitary adenomas present three ways: hypersecretion, compression (vision, headache), hypopituitarism.",
            "Prolactinoma is the commonest secretory adenoma (~40%); hyperprolactinemia suppresses GnRH and causes reversible infertility.",
            "Microadenoma <10 mm, macroadenoma >=10 mm; upward growth hits the optic chiasm -> bitemporal hemianopia.",
            "Cabergoline normalizes prolactin in ~90% of prolactinomas - medicine first, surgery second.",
            "Workup excludes pregnancy, hypothyroidism, drugs, and renal failure before blaming the pituitary.",
        ],
        "requirements": [
            "The three presentation modes with the anatomy behind each.",
            "The dopamine-brake logic and the differential of hyperprolactinemia.",
            "The volume-cubed size arithmetic and why millimeters matter near the chiasm.",
        ],
        "standards": [
            "Prolactin in ng/mL; normal <25 (women), <20 (men) per standard assays.",
            "Size cutoff 10 mm per standard radiology; bitemporal hemianopia as the classic field defect.",
            "Cabergoline efficacy per Endocrine Society hyperprolactinemia guidance.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Melmed S, Casanueva FF, Hoffman AR, et al. Diagnosis and treatment of hyperprolactinemia: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2011;96(2):273-288.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: the sella is a crowded server rack - one "
            "rack unit tall, six services running, the fiber trunk (optic "
            "chiasm) routed directly overhead. A rogue process (adenoma) "
            "either spams its own protocol (hypersecretion), hogs the rack "
            "and overheats its neighbors (compression), or crashes the other "
            "services (hypopituitarism). Prolactinomas are the rare rogue "
            "process with a remote kill switch: dopamine agonists shut them "
            "down without opening the rack."
        ),
    },
    {
        "key": "dynamic_testing",
        "name": "Dynamic Endocrine Testing: Stimulation and Suppression Tests",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Static hormone levels often cannot answer the question, because "
            "pulsatile secretion, binding proteins, and feedback compensation "
            "hide the defect. Dynamic testing provokes the system and watches "
            "the response - the endocrine equivalent of a stress test. "
            "Suppression tests ask whether a suspiciously autonomous gland can "
            "be shut down: the 1-milligram overnight dexamethasone test for "
            "Cushing syndrome (normal: morning cortisol below 1.8 mcg/dL), the "
            "oral glucose suppression test for acromegaly (normal: GH below 1 "
            "ng/mL). Stimulation tests ask whether a suspect gland can answer "
            "a call: cosyntropin (synthetic ACTH) for adrenal insufficiency "
            "(normal: cortisol peaks at or above 18 mcg/dL), the insulin "
            "tolerance test for GH and ACTH deficiency (hypoglycemia must be "
            "real - glucose below 40 mg/dL - to count as a stimulus), GnRH and "
            "TRH stimulation tests for pituitary reserve. Each test has a "
            "pass-fail line drawn from physiology, and each has rules that "
            "invalidate it - estrogen raises cortisol-binding globulin and "
            "fakes a cosyntropin pass on total cortisol, dexamethasone "
            "interferes with assays that cross-react. This record teaches the "
            "provocation repertoire."
        ),
        "how_it_works": (
            "Suppression testing works by injecting a fake 'all clear': "
            "dexamethasone tells the HPA axis that glucocorticoid is abundant, "
            "and a healthy axis stands down - morning cortisol falls from a "
            "typical 15 mcg/dL to about 1.2, a 92 percent suppression the demo "
            "computes; an autonomous source ignores the memo and keeps "
            "secreting. Stimulation testing works by injecting a fake alarm: "
            "cosyntropin orders the adrenal to produce at full capacity, and "
            "the peak cortisol measures the gland's maximum output - at least "
            "18 mcg/dL means the factory can meet a crisis. The insulin "
            "tolerance test is the most physiological provocation of all: real "
            "hypoglycemia is a whole-body emergency that should maximally drive "
            "both GH and ACTH, so a blunted response proves the axis cannot "
            "answer a genuine crisis - but the test is itself hazardous and is "
            "never done where a seizure or cardiac event would be "
            "catastrophic. The demo works the suppression-percentage "
            "arithmetic and the unit conversion behind the 18 mcg/dL pass mark."
        ),
        "key_points": [
            "Dynamic tests provoke the axis: suppression tests check for autonomy, stimulation tests check for reserve.",
            "Dexamethasone 1 mg overnight: normal suppresses cortisol below 1.8 mcg/dL; Cushing's does not suppress.",
            "Cosyntropin stimulation: normal peaks at or above 18 mcg/dL (500 nmol/L); below that is adrenal insufficiency.",
            "OGTT suppression of GH below 1 ng/mL excludes acromegaly; failure to suppress confirms it.",
            "Every test has invalidators: binding-protein changes, assay cross-reactivity, inadequate stimulus.",
        ],
        "requirements": [
            "The suppression-vs-stimulation logic with one flagship test of each.",
            "The pass-fail numbers with their unit conversions.",
            "The invalidator list: what makes each test lie.",
        ],
        "standards": [
            "Cutoffs per Endocrine Society guidance: DST <1.8 mcg/dL, cosyntropin peak >=18 mcg/dL, OGTT GH <1 ng/mL.",
            "ITT stimulus adequacy defined as glucose <40 mg/dL per standard protocol.",
            "Cortisol in mcg/dL with nmol/L equivalents; GH in ng/mL.",
        ],
        "citations": [
            "Nieman LK, Biller BMK, Findling JW, et al. The diagnosis of Cushing's syndrome: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2008;93(5):1526-1540.",
            "Bornstein SR, Allolio B, Arlt W, et al. Diagnosis and treatment of primary adrenal insufficiency: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2024;109(3):e372-e378.",
            "Katznelson L, Laws ER Jr, Melmed S, et al. Acromegaly: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2014;99(11):3933-3951.",
        ],
        "sig_lens": (
            "Signature reading: dynamic testing is red-team exercising for "
            "control systems. Suppression tests are phishing simulations - send "
            "a forged stand-down order and see which stations disobey "
            "(autonomy). Stimulation tests are fire drills - sound the alarm "
            "and measure who musters (reserve). A system that fails either "
            "exercise is not ready for the real incident, and the numbers "
            "draw the line between drill-ready and compromised."
        ),
    },
    {
        "key": "cah",
        "name": "Congenital Adrenal Hyperplasia: Inborn Errors of Steroidogenesis",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Congenital adrenal hyperplasia (CAH) is the inborn-error chapter of "
            "endocrinology: an enzyme block in the cortisol assembly line that "
            "backs up precursors and floods the androgen branch. The commonest "
            "form, 21-hydroxylase deficiency, strikes about 1 in 15,000 births "
            "in its classic form. Without 21-hydroxylase, the adrenal cannot "
            "finish cortisol or aldosterone; the pituitary, reading low "
            "cortisol, pours out ACTH; the hyperstimulated gland shunts the "
            "backed-up precursors into androgens. Girls are born with virilized "
            "genitalia, both sexes risk salt-wasting adrenal crisis in the "
            "newborn period (about three-quarters of classic cases lose salt), "
            "and untreated children grow fast then stop early as excess "
            "androgen fuses the growth plates. Newborn screening by 17-"
            "hydroxyprogesterone - the precursor piled up behind the block - "
            "catches it in the first days of life. Treatment is lifelong "
            "glucocorticoid (and mineralocorticoid for salt-wasters) "
            "replacement, dosed to suppress the ACTH drive without causing "
            "Cushingoid overtreatment - the narrow therapeutic corridor that "
            "defines the disease's management. This record teaches the enzyme-"
            "block logic."
        ),
        "how_it_works": (
            "The block works as a dam with a spillway. Cholesterol flows down "
            "the steroidogenic trunk toward cortisol; the 21-hydroxylase dam "
            "stops it one step short, so 17-hydroxyprogesterone - the last "
            "intermediate before the dam - accumulates to levels hundreds of "
            "times normal, which is why it is the screening marker. The "
            " backed-up flow spills sideways into the androgen branch "
            "(DHEA, androstenedione, testosterone), because those enzymes are "
            "unblocked and the ACTH drive keeps the whole factory running hot. "
            "Aldosterone synthesis also needs 21-hydroxylase, so severe blocks "
            "lose salt and water through the kidney - the salt-wasting crisis "
            "of vomiting, dehydration, hyponatremia, and hyperkalemia that "
            "kills untreated newborns. Treatment closes the loop externally: "
            "replacement hydrocortisone supplies the missing cortisol, which "
            "restores feedback, quiets ACTH, and thereby throttles the androgen "
            "spillway - the dose titrated against 17-OHP and androstenedione. "
            "The demo works the incidence arithmetic (cases expected per "
            "births screened) and the salt-wasting share of classic cases."
        ),
        "key_points": [
            "CAH = enzyme block in cortisol synthesis; 21-hydroxylase deficiency is ~1 in 15,000 classic births.",
            "The dam-and-spillway logic: blocked cortisol/aldosterone, backed-up 17-OHP, spilled androgens.",
            "17-hydroxyprogesterone is the newborn screening marker - the precursor piled behind the block.",
            "~75% of classic cases are salt-wasters: aldosterone lost too, risking newborn adrenal crisis.",
            "Treatment: lifelong gluco- (and mineralocorticoid) replacement titrated to suppress ACTH without overtreatment.",
        ],
        "requirements": [
            "The dam-and-spillway mechanism with the three consequences (cortisol down, aldosterone down, androgens up).",
            "Why 17-OHP is the screening marker and what salt-wasting means physiologically.",
            "The treatment corridor: replacement that restores feedback without causing Cushingoid excess.",
        ],
        "standards": [
            "Incidence 1:15,000 classic 21-hydroxylase deficiency per standard newborn-screening data.",
            "17-OHP in ng/dL; salt-wasting defined by aldosterone deficiency with hyponatremia/hyperkalemia.",
            "Genetics: autosomal recessive CYP21A2 mutations, stated in standard nomenclature.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Speiser PW, Arlt W, Auchus RJ, et al. Congenital adrenal hyperplasia due to steroid 21-hydroxylase deficiency: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2018;103(11):4043-4088.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: CAH is a single-point failure in a branched "
            "assembly line - one broken machine, and the whole factory "
            "re-routes. The dam floods the upstream inventory (17-OHP, the "
            "tell-tale stockpile), the spillway overproduces the side product "
            "(androgens), and the downstream customer (salt balance) goes "
            "unserved. Replacement therapy is outsourcing the broken step: "
            "import the finished good (cortisol) and the line rebalances "
            "itself through restored feedback."
        ),
    },
    {
        "key": "obesity",
        "name": "Obesity and Metabolic Syndrome: Hormones of Energy Balance",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Obesity is an endocrine disease of energy balance, and the "
            "hormones of appetite and storage are its cast. Leptin, made by "
            "fat itself in proportion to fat mass, reports energy stores to "
            "the hypothalamus; ghrelin from the empty stomach shouts hunger; "
            "insulin, beyond glucose control, is the master storage signal "
            "that locks fat in adipocytes; GLP-1 and PYY from the gut signal "
            "satiety after meals. In obesity the reporting breaks down: leptin "
            "is high but the brain is leptin-resistant, so the adipostat reads "
            "empty while the tank is full - the same resistance logic as type 2 "
            "diabetes, one tissue over. Metabolic syndrome is the clinical "
            "cluster that follows: any three of five - large waist, high "
            "triglycerides, low HDL, hypertension, and elevated fasting "
            "glucose - marking the insulin-resistant patient headed for "
            "diabetes and cardiovascular disease. The combinatorics are exact: "
            "five criteria taken three or more at a time give sixteen qualifying "
            "combinations. Treatment has been revolutionized by GLP-1 receptor "
            "agonists, which restore the satiety signal pharmacologically. This "
            "record teaches the hormonal economics of weight."
        ),
        "how_it_works": (
            "Energy balance works as a defended set point with asymmetric "
            "defenses: the body fights weight loss far harder than weight gain, "
            "because the leptin-hypothalamus loop evolved against famine, not "
            "feast. When fat mass falls, leptin falls, and the arcuate nucleus "
            "answers with increased AgRP hunger signaling and decreased POMC "
            "satiety signaling plus a drop in metabolic rate - the physiology "
            "behind dieting's rebound. GLP-1 agonists work by borrowing the "
            "gut's own satiety channel: they slow gastric emptying, act on "
            "hypothalamic and brainstem appetite circuits, and reduce the "
            "reward value of food, producing the 15 percent mean weight loss "
            "seen with semaglutide at 68 weeks in the STEP-1 trial. The "
            "metabolic syndrome definition is pure combinatorics - choose any 3, "
            "4, or 5 of the 5 criteria: 10 + 5 + 1 = 16 qualifying patterns, "
            "the demo's computation - which is why two patients with "
            "'metabolic syndrome' can share only a single criterion. The demo "
            "works the sixteen-pattern count and the trial weight-loss "
            "arithmetic for a 110-kilogram patient."
        ),
        "key_points": [
            "Obesity is hormonal: leptin (fat's report), ghrelin (hunger's shout), insulin (the storage lock), GLP-1/PYY (satiety).",
            "Leptin resistance mirrors insulin resistance: high signal, deaf receiver - the adipostat reads empty.",
            "The body defends against weight loss harder than gain: falling leptin raises hunger and lowers metabolic rate.",
            "Metabolic syndrome: any 3 of 5 criteria (waist, triglycerides, HDL, blood pressure, fasting glucose) = 16 qualifying patterns.",
            "GLP-1 agonists restore satiety pharmacologically: semaglutide ~15% mean weight loss at 68 weeks (STEP-1).",
        ],
        "requirements": [
            "The four appetite hormones with source, signal direction, and the resistance concept.",
            "The asymmetric defense logic and its evolutionary rationale.",
            "The metabolic-syndrome combinatorics and the GLP-1 trial arithmetic.",
        ],
        "standards": [
            "Metabolic syndrome criteria per ATP III (waist, TG >=150, HDL <40/50, BP >=130/85, fasting glucose >=100).",
            "STEP-1 semaglutide 2.4 mg results per Wilding et al., NEJM 2021.",
            "BMI in kg/m2; obesity defined as >=30 per standard classification.",
        ],
        "citations": [
            "Wilding JPH, Batterham RL, Calanna S, et al. Once-weekly semaglutide in adults with overweight or obesity. N Engl J Med. 2021;384:989-1002.",
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Grundy SM, Cleeman JI, Daniels SR, et al. Diagnosis and management of the metabolic syndrome: an AHA/NHLBI scientific statement. Circulation. 2005;112:2735-2752.",
        ],
        "sig_lens": (
            "Signature reading: body weight is a defended inventory level with "
            "a rigged control system - the reorder point ratchets up easily "
            "and down almost never, because the firmware was written during "
            "famines. Leptin is the warehouse inventory report; in obesity "
            "the report arrives but the purchasing office ignores it. GLP-1 "
            "drugs are an override code injected into the satiety channel: "
            "they do not fix the broken gauge, they transmit a convincing "
            "forgery of 'enough' that the brain accepts."
        ),
    },
    {
        "key": "hormone_therapy",
        "name": "Therapeutic Hormones: Replacement, Contraception, and Pharmacology",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hormones are among the oldest and most precise drugs in medicine, "
            "used in three great strategies: replace what is missing, suppress "
            "what is excessive, and borrow a hormone's signal for a new purpose. "
            "Replacement is the purest: levothyroxine for hypothyroidism, "
            "hydrocortisone for adrenal insufficiency, testosterone for "
            "hypogonadism, estradiol for menopause, GH for GH deficiency, "
            "desmopressin for diabetes insipidus, insulin for type 1 diabetes - "
            "each dosed to restore physiology, not to exceed it. Suppression "
            "exploits feedback: combined hormonal contraceptives (estrogen plus "
            "progestin) suppress GnRH, LH, and FSH so completely that ovulation "
            "never occurs - perfect-use failure under 1 percent per year "
            "(Pearl index ~0.3), typical use around 7 to 9 percent because "
            "people miss pills. Borrowing repurposes signals: GnRH agonists "
            "suppress puberty, endometriosis, and prostate cancer through the "
            "desensitization paradox; GLP-1 agonists borrow satiety for weight "
            "loss; bisphosphonates are not hormones but they answer the bone "
            "question hormones usually handle. Every hormonal therapy obeys the "
            "half-life and feedback rules from the foundations records - which "
            "is why stopping a combined contraceptive restores fertility "
            "within weeks while stopping depot medroxyprogesterone can take "
            "the better part of a year. This record teaches the therapeutic "
            "playbook."
        ),
        "how_it_works": (
            "Contraceptive steroids work by multi-level suppression: the "
            "progestin component thickens cervical mucus and thins the "
            "endometrium while both steroids suppress hypothalamic GnRH "
            "pulsatility, abolishing the mid-cycle LH surge - three independent "
            "contraceptive mechanisms in one pill, which is why perfect use is "
            "so effective and why missed pills degrade it. The Pearl index "
            "converts efficacy to arithmetic: pregnancies per 100 woman-years, "
            "so a typical-use rate of 7 means 70 pregnancies in a thousand "
            "woman-years - the demo's computation - versus 3 in perfect use. "
            "Replacement therapy works by the feedback math in reverse: give "
            "enough levothyroxine to bring TSH into range, enough "
            "hydrocortisone to keep the patient well without Cushingoid signs, "
            "enough testosterone to reach mid-normal morning levels - always "
            "titrated against the loop's own reporter. Menopausal hormone "
            "therapy adds the risk-benefit ledger: effective for vasomotor "
            "symptoms and bone protection, with clotting and breast-cancer "
            "risks that confine it to symptomatic women near menopause onset "
            "per current guidance. The demo works the Pearl-index arithmetic "
            "and the suppression logic that makes one pill three contraceptives."
        ),
        "key_points": [
            "Three strategies: replace the missing (levothyroxine, insulin, hydrocortisone), suppress the excessive (contraceptives, GnRH agonists), borrow the signal (GLP-1 for weight).",
            "Combined contraceptives work at three levels: GnRH/LH/FSH suppression, cervical mucus, endometrium.",
            "Pearl index = pregnancies per 100 woman-years: ~0.3 perfect use, ~7-9 typical use for combined pills.",
            "Replacement is titrated to the loop's reporter (TSH, morning testosterone) - restore, never exceed.",
            "Return of fertility follows the drug's half-life: weeks after pills, many months after depot injections.",
        ],
        "requirements": [
            "The three-strategy framework with two drug examples each.",
            "The triple mechanism of combined contraceptives and the Pearl-index arithmetic.",
            "The titration principle: dose to the feedback reporter, with the half-life determining reversibility timing.",
        ],
        "standards": [
            "Pearl index figures per standard contraceptive technology references.",
            "Menopausal therapy framing per NAMS/Endocrine Society guidance (symptom-driven, near onset).",
            "Drug names generic (levothyroxine, cabergoline, medroxyprogesterone) with standard dosing language.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Bhasin S, Brito JP, Cunningham GR, et al. Testosterone therapy in men with hypogonadism: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2018;103(5):1715-1744.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: hormonal pharmacology is applied control "
            "theory. Replacement is closing someone else's broken loop with "
            "your own hardware. Contraception is a denial-of-service attack on "
            "the ovulation trigger - flood the controller with forged "
            "all-clear signals until it stops issuing launch orders. And every "
            "depot formulation is a time-release capsule whose half-life is "
            "the fine print on reversibility."
        ),
    },
    {
        "key": "pediatric",
        "name": "Pediatric Endocrinology: Growth Failure and Precocious Puberty",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pediatric endocrinology reads the child's growth chart the way a "
            "cardiologist reads an ECG: the curve is the vital sign. A healthy "
            "child tracks along a percentile; crossing percentiles downward, or "
            "a growth velocity under 4 centimeters a year in mid-childhood, "
            "triggers the workup for growth failure - GH deficiency, "
            "hypothyroidism, celiac disease, Turner syndrome, chronic illness. "
            "Bone age (the left-hand X-ray read against the Greulich-Pyle atlas) "
            "tells whether the skeleton is younger than the calendar: delayed "
            "bone age with short stature suggests a treatable endocrine cause "
            "with growth potential remaining, while advanced bone age warns "
            "that the growth plates will fuse early. The mid-parental height "
            "formula sets the genetic target - for a boy, (father + mother + "
            "13)/2 centimeters; for a girl, (father + mother - 13)/2 - so a "
            "father of 175 and mother of 162 predict a son near 175 and a "
            "daughter near 162. At the other end, precocious puberty (breast "
            "or testicular development before age 8 in girls, 9 in boys) is "
            "usually central - the GnRH pulse generator switching on early - "
            "and GnRH agonists pause it by the desensitization paradox, "
            "preserving adult height. This record teaches the pediatric lens."
        ),
        "how_it_works": (
            "Growth assessment works as statistical process control: height "
            "plotted against age- and sex-matched reference curves (CDC/WHO), "
            "with the growth velocity - centimeters per year between two "
            "measurements at least six months apart - as the sensitive "
            "derivative that falls before the percentile does. A velocity "
            "below the 3rd percentile for age is the red flag that launches "
            "the endocrine workup: TSH and free T4 (hypothyroidism slows "
            "growth before anything else), IGF-1 and GH stimulation testing, "
            "karyotype in short girls (Turner), celiac screen. Bone age "
            "converts the skeleton into a second clock: a 10-year-old with a "
            "bone age of 7 has years of growth-plate runway left, while a bone "
            "age of 13 is nearly out of runway - and the predicted adult "
            "height comes from combining current height with bone-age "
            "tables. The mid-parental height formula is linear genetics "
            "bookkeeping: each parent contributes half the deviation from the "
            "population mean, shifted by the 13-centimeter average sex "
            "difference. The demo works the formula for a concrete parental "
            "pair and the velocity threshold that separates normal from "
            "concerning."
        ),
        "key_points": [
            "The growth chart is the vital sign: percentile tracking plus growth velocity (cm/yr) as the sensitive derivative.",
            "Velocity <4 cm/yr in mid-childhood (below ~3rd percentile) triggers the endocrine workup.",
            "Bone age (Greulich-Pyle hand X-ray) measures remaining growth-plate runway: delayed = potential, advanced = early fusion.",
            "Mid-parental height: boy (father+mother+13)/2, girl (father+mother-13)/2 - the genetic target.",
            "Precocious puberty (<8 girls, <9 boys) is usually central; GnRH agonists pause it and preserve adult height.",
        ],
        "requirements": [
            "The velocity concept: why two measurements six months apart beat a single percentile.",
            "The bone-age-as-second-clock logic and what delayed vs advanced means for management.",
            "The mid-parental height formula worked numerically.",
        ],
        "standards": [
            "Growth references per CDC/WHO charts; velocity cutoffs per standard pediatric endocrinology.",
            "Bone age per Greulich-Pyle atlas; precocious puberty age cutoffs per standard definitions.",
            "GH stimulation testing and Turner karyotype per standard workup guidance.",
        ],
        "citations": [
            "Melmed S, Auchus RJ, Goldfine AB, et al. Williams Textbook of Endocrinology. 15th ed. Elsevier; 2024.",
            "Gardner DG, Shoback D. Greenspan's Basic & Clinical Endocrinology. 11th ed. McGraw Hill; 2022.",
            "Jameson JL, Fauci AS, Kasper DL, et al. Harrison's Principles of Internal Medicine. 21st ed. McGraw Hill; 2022.",
        ],
        "sig_lens": (
            "Signature reading: pediatric endocrinology is project management "
            "for the human construction schedule. The growth chart is the "
            "earned-value curve, velocity its slope, bone age the independent "
            "auditor's clock, and mid-parental height the contracted "
            "deliverable. Falling behind schedule triggers the root-cause "
            "drill; running ahead of schedule (precocious puberty) gets the "
            "pause button (GnRH agonist) so the project finishes at full "
            "specification instead of topping out early."
        ),
    },
    {
        "key": "emergencies",
        "name": "Endocrine Emergencies: DKA, Thyroid Storm, and Adrenal Crisis",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Endocrine emergencies are what happens when a control loop fails "
            "open, and all three great ones are diagnosed by numbers and "
            "treated by protocol. Diabetic ketoacidosis (DKA): absolute or "
            "relative insulin deficiency lets glucose soar above 250 mg/dL "
            "while unopposed glucagon drives fat into ketoacids - arterial pH "
            "below 7.30, bicarbonate below 18, anion gap widened, the patient "
            "dehydrated, breathing deep and fruity. Treatment is fluids first "
            "(15-20 mL/kg in the first hour - over a liter for a 70-kilogram "
            "adult), then insulin to close the ketone tap, potassium "
            "replacement, and hunting the trigger (infection, missed insulin). "
            "Thyroid storm: decompensated hyperthyroidism with fever, "
            "tachycardia, agitation, and organ dysfunction, scored by the "
            "Burch-Wartofsky scale (45 or above highly suggestive) - treated "
            "with beta-blockade, antithyroid drugs, iodine (after the drugs), "
            "and steroids. Adrenal crisis: cortisol deficiency under stress - "
            "hypotension unresponsive to fluids, hyponatremia, hyperkalemia, "
            "hypoglycemia - treated with immediate hydrocortisone 100 mg IV "
            "and fluids; never wait for labs. Myxedema coma and hypercalcemic "
            "crisis round out the set. This record teaches the emergencies "
            "that punish hesitation."
        ),
        "how_it_works": (
            "DKA works as a double failure: without insulin, glucose cannot "
            "enter cells (so blood glucose climbs) and hormone-sensitive lipase "
            "runs unopposed (so free fatty acids flood the liver, which "
            "converts them to the ketoacids beta-hydroxybutyrate and "
            "acetoacetate). The ketoacids consume bicarbonate - hence the low "
            "pH and low HCO3 - and the osmotic diuresis from glycosuria "
            "dehydrates the patient, concentrating everything further. The "
            "anion gap quantifies the unmeasured ketoacid anions: sodium minus "
            "(chloride plus bicarbonate), normally 8-12, widened past 12 and "
            "often past 20 in DKA. Treatment order is physics before chemistry: "
            "restore circulating volume first (the 15-20 mL/kg bolus the demo "
            "computes for a 70-kilogram adult), because insulin cannot reach "
            "tissues through an empty vasculature and because fluids alone "
            "lower glucose by dilution and improved perfusion. Thyroid storm "
            "management exploits the synthesis pipeline in order: block the "
            "effect (beta-blocker), block new synthesis (thionamide), block "
            "release of stored hormone (iodine, given after the thionamide so "
            "it is not used as substrate), block conversion (steroid). The "
            "demo works the DKA fluid bolus, the anion-gap arithmetic, and "
            "the Burch-Wartofsky threshold."
        ),
        "key_points": [
            "DKA: glucose >250, pH <7.30, HCO3 <18, widened anion gap - double failure of glucose entry and fat breakdown.",
            "DKA treatment order: fluids (15-20 mL/kg first hour), then insulin, potassium, trigger hunt.",
            "Thyroid storm: Burch-Wartofsky >=45 highly suggestive; treat beta-blocker -> thionamide -> iodine -> steroid, in that order.",
            "Adrenal crisis: hypotension + hyponatremia + hyperkalemia under stress - give hydrocortisone 100 mg IV immediately, never wait for labs.",
            "Myxedema coma and hypercalcemic crisis complete the emergency set; all punish hesitation.",
        ],
        "requirements": [
            "The DKA double-failure mechanism with the anion-gap calculation.",
            "The treatment sequencing for DKA and thyroid storm with the rationale for each order.",
            "The adrenal-crisis rule: treat first, confirm later.",
        ],
        "standards": [
            "DKA criteria per ADA Standards of Care 2024; fluid resuscitation 15-20 mL/kg/h per guideline.",
            "Burch-Wartofsky scoring per standard thyroid storm assessment.",
            "Adrenal crisis hydrocortisone 100 mg IV per Endocrine Society guidance.",
        ],
        "citations": [
            "American Diabetes Association. Standards of Care in Diabetes - 2024. Diabetes Care. 2024;47(Suppl.1):S1-S321.",
            "Ross DS, Burch HB, Cooper DS, et al. 2016 American Thyroid Association guidelines for diagnosis and management of hyperthyroidism. Thyroid. 2016;26(10):1343-1421.",
            "Bornstein SR, Allolio B, Arlt W, et al. Diagnosis and treatment of primary adrenal insufficiency: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2024;109(3):e372-e378.",
        ],
        "sig_lens": (
            "Signature reading: endocrine emergencies are cascading failures "
            "in safety-critical control systems, and every one has a "
            "runbook. DKA is a dual loss-of-control with a strict "
            "power-restore sequence (fluids before insulin - restore the "
            "bus before restarting the servers). Thyroid storm is a thermal "
            "runaway with a four-step scram procedure in a non-negotiable "
            "order. Adrenal crisis is the auxiliary power failure: when the "
            "backup generator is dead and the load spikes, you do not "
            "diagnose - you start the portable generator (hydrocortisone) "
            "and ask questions after the lights are on."
        ),
    },
    {
        "key": "future",
        "name": "The Future of Endocrinology: GLP-1 Agonists and Hormone Medicine",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Endocrinology is living through its most consequential therapeutic "
            "revolution since insulin: the incretin era. GLP-1 receptor "
            "agonists - semaglutide, tirzepatide (a dual GLP-1/GIP agonist), "
            "and their successors - began as diabetes drugs and became the "
            "first medicines to produce surgical-scale weight loss "
            "pharmacologically: 14.9 percent mean loss at 68 weeks for "
            "semaglutide 2.4 mg (STEP-1), 20.9 percent at 72 weeks for "
            "tirzepatide 15 mg (SURMOUNT-1) - a 110-kilogram patient losing 23 "
            "kilograms to reach 87. The benefits now extend past weight: "
            "cardiovascular event reduction, sleep-apnea improvement, "
            "kidney protection signals, and early data in addiction and "
            "neurodegeneration - because GLP-1 receptors sit in brain, heart, "
            "and kidney as well as gut and pancreas. Around this flagship, the "
            "field is advancing on every front: closed-loop insulin pumps "
            "(artificial pancreas systems pairing continuous glucose monitors "
            "with control algorithms), once-weekly insulins, oral "
            "peptide-delivery technologies, precision dosing from "
            "pharmacogenomics, and teplizumab delaying type 1 diabetes onset "
            "by treating autoimmunity before the beta cells fall. The "
            "discipline that began by replacing missing hormones now reprograms "
            "the loops themselves. This record closes the ladder looking "
            "forward."
        ),
        "how_it_works": (
            "GLP-1 agonists work by sustained pharmacologic activation of a "
            "physiologic satiety channel: native GLP-1 lasts minutes, but "
            "acylated and engineered analogues last a week, providing continuous "
            "signaling to hypothalamic and brainstem appetite circuits, slowing "
            "gastric emptying, and amplifying glucose-dependent insulin release "
            "(glucose-dependent, so hypoglycemia risk stays low without "
            "background insulin). The trial arithmetic is stark: in SURMOUNT-1, "
            "tirzepatide 15 mg took a 110-kilogram adult to about 87 kilograms "
            "in 72 weeks - the demo computes exactly that - a result range "
            "previously owned by bariatric surgery. Closed-loop pumps work as "
            "literal control systems: a continuous glucose monitor feeds a "
            "proportional-integral-derivative-style algorithm every five "
            "minutes, and the pump adjusts basal insulin continuously, with "
            "hybrid systems still needing meal announcements - the negative-"
            "feedback records from this ladder's foundations, now running in "
            "silicon on the patient's hip. Teplizumab works upstream of all of "
            "it: an anti-CD3 antibody that calms the autoimmune attack, "
            "delaying stage-3 type 1 diabetes by a median of about two years "
            "in high-risk individuals. The demo works the incretin trial "
            "arithmetic and the feedback-loop parallel that ties the future "
            "back to the foundations."
        ),
        "key_points": [
            "The incretin era: GLP-1 agonists produce surgical-scale weight loss pharmacologically - 14.9% (semaglutide, STEP-1), 20.9% (tirzepatide, SURMOUNT-1).",
            "Benefits extend beyond weight: cardiovascular, sleep apnea, kidney, and early neuro/addiction signals.",
            "Closed-loop pumps are literal feedback controllers: CGM + algorithm + pump adjusting insulin every 5 minutes.",
            "Teplizumab delays type 1 diabetes onset ~2 years by treating autoimmunity before beta-cell failure.",
            "The field's arc: from replacing missing hormones to reprogramming the loops themselves.",
        ],
        "requirements": [
            "The GLP-1 mechanism (satiety circuits, gastric slowing, glucose-dependent insulin) and the two landmark trial numbers.",
            "The closed-loop system as an engineered negative-feedback loop, tied to the foundations records.",
            "Teplizumab as the upstream strategy: immune modulation before organ failure.",
        ],
        "standards": [
            "STEP-1 (Wilding et al., NEJM 2021) and SURMOUNT-1 (Jastreboff et al., NEJM 2022) cited with dose and duration.",
            "Teplizumab delay figure per the TrialNet study (Herold et al., NEJM 2019).",
            "Closed-loop terminology per ADA Standards of Care (automated insulin delivery).",
        ],
        "citations": [
            "Wilding JPH, Batterham RL, Calanna S, et al. Once-weekly semaglutide in adults with overweight or obesity. N Engl J Med. 2021;384:989-1002.",
            "Jastreboff AM, Aronne LJ, Ahmad NN, et al. Tirzepatide once weekly for the treatment of obesity. N Engl J Med. 2022;387:205-216.",
            "Herold KC, Bundy BN, Long SA, et al. An anti-CD3 antibody, teplizumab, in relatives at risk for type 1 diabetes. N Engl J Med. 2019;381:603-613.",
            "American Diabetes Association. Standards of Care in Diabetes - 2024. Diabetes Care. 2024;47(Suppl.1):S1-S321.",
        ],
        "sig_lens": (
            "Signature reading: the future of endocrinology is the graduation "
            "from spare parts to systems engineering. For a century the "
            "specialty replaced broken components; now it patches the control "
            "software itself - sustained satiety signals where the native "
            "channel is weak, silicon feedback loops where the biological one "
            "failed, immune reprogramming before the hardware is destroyed. "
            "The ladder that began with 'what is a hormone' ends here: the "
            "messages were never just chemistry. They were always code."
        ),
    },
]
