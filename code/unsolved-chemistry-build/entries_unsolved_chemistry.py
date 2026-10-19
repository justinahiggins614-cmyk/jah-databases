#!/usr/bin/env python3
"""Entries for the Unsolved Chemistry databases (Manon 16:15 orders, batch 1).

34 famous unsolved chemistry problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex). Public half =
fact-checked problems; signature half = the same problems with the
Signature system's proposed solution approach, titles suffixed
" (Signature Edition)", src signature, clearly labeled Signature-made.

ID prefixes: JAH-USCH- (public) and JAH-USCHS- (signature), verified free
2026-10-17 in the manifest id_prefix values and across all shard index
files (zero hits).

Honesty rule (series canon): the signature_solution OPENS WITH THE EXACT
LABEL "Signature-generated proposed solution - not established science."
Never claim proof, never imply peer acceptance, never present speculation
as settled.

Citations are real publications/editions (books, reviews, landmark
papers). Never the words "bat belt" anywhere. No website references.
No Facebook.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature solution approach: "
            "every unsolved problem treated as a covenant of evidence, the "
            "solution path walked step by step with adjustable assumptions "
            "and a confirm-or-refute panel. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_ATKINS = ("Atkins P, de Paula J. Physical Chemistry. 11th ed. Oxford "
              "University Press; 2018.")
CIT_CLAYDEN = ("Clayden J, Greeves N, Warren S. Organic Chemistry. 2nd ed. "
               "Oxford University Press; 2012.")
CIT_HOUSECROFT = ("Housecroft CE, Sharpe AG. Inorganic Chemistry. 5th ed. "
                  "Pearson; 2018.")
CIT_BALL_WATER = ("Ball P. Water - A Biography. Weidenfeld and Nicolson; 1999.")
CIT_DEBENEDETTI = ("Debenedetti PG. Metastable Liquids: Concepts and "
                   "Principles. Princeton University Press; 1996.")
CIT_GALLO = ("Gallo P et al. Water: A Tale of Two Liquids. Chemical Reviews "
             "116, 7463-7500; 2016.")
CIT_JENG = ("Jeng M. The Mpemba effect: When can hot water freeze faster "
            "than cold? American Journal of Physics 74, 514-522; 2006.")
CIT_TURIN = ("Turin L. A spectroscopic mechanism for primary olfactory "
             "reception. Chemical Senses 21, 773-791; 1996.")
CIT_BLOCK = ("Block E et al. Implausibility of the vibrational theory of "
             "olfaction. Proceedings of the National Academy of Sciences "
             "112, E2766-E2774; 2015.")
CIT_ANFINSEN = ("Anfinsen CB. Principles that govern the folding of protein "
                "chains. Science 181, 223-230; 1973.")
CIT_DILL = ("Dill KA, MacCallum JL. The protein-folding problem, 50 years "
            "on. Science 338, 1042-1046; 2012.")
CIT_WOLFENDEN = ("Wolfenden R, Snider MJ. The depth of chemical time and the "
                 "power of enzymes as catalysts. Accounts of Chemical "
                 "Research 34, 938-945; 2001.")
CIT_CHANDLER = ("Chandler D. Interfaces and the driving force of hydrophobic "
                "assembly. Nature 437, 640-647; 2005.")
CIT_SOAI = ("Soai K, Shibata T, Morioka H, Choji K. Asymmetric autocatalysis "
            "and amplification of enantiomeric excess of a chiral molecule. "
            "Nature 378, 767-768; 1995.")
CIT_MILLER = ("Miller SL. A production of amino acids under possible "
              "primitive Earth conditions. Science 117, 528-529; 1953.")
CIT_SUTHERLAND = ("Sutherland JD. The origin of life - out of the blue. "
                  "Angewandte Chemie International Edition 55, 104-121; 2016.")
CIT_UMENA = ("Umena Y, Kawakami K, Shen JR, Kamiya N. Crystal structure of "
             "oxygen-evolving photosystem II at 1.9 angstrom resolution. "
             "Nature 473, 55-60; 2011.")
CIT_DEB_STILL = ("Debenedetti PG, Stillinger FH. Supercooled liquids and the "
                 "glass transition. Nature 410, 259-267; 2001.")
CIT_AGMON = ("Agmon N. The Grotthuss mechanism. Chemical Physics Letters "
             "244, 456-462; 1995.")
CIT_JUNGWIRTH = ("Jungwirth P, Tobias DJ. Specific ion effects at the "
                 "air/water interface. Chemical Reviews 106, 1259-1281; 2006.")
CIT_KASHCHIEV = ("Kashchiev D. Nucleation: Basic Theory with Applications. "
                 "Butterworth-Heinemann; 2000.")
CIT_WOLDE = ("ten Wolde PR, Frenkel D. Enhancement of protein crystal "
             "nucleation by critical density fluctuations. Science 277, "
             "1975-1978; 1997.")
CIT_MADDOX = ("Maddox J. Crystals from first principles. Nature 335, 201; "
              "1988.")
CIT_PELED = ("Peled E. The electrochemical behavior of alkali and alkaline "
             "earth metals in nonaqueous battery systems. Journal of the "
             "Electrochemical Society 126, 2047-2051; 1979.")
CIT_UHLIG = ("Uhlig HH, Revie RW. Corrosion and Corrosion Control. 4th ed. "
             "Wiley; 2008.")
CIT_BUCK = ("Buck RC et al. Perfluoroalkyl and polyfluoroalkyl substances in "
            "the environment: Terminology, classification, and origins. "
            "Integrated Environmental Assessment and Management 7, 513-541; "
            "2011.")
CIT_SMIL = ("Smil V. Enriching the Earth: Fritz Haber, Carl Bosch, and the "
            "Transformation of World Food Production. MIT Press; 2001.")
CIT_HOFFMAN = ("Hoffman BM, Lukoyanov D, Yang ZY, Dean DR, Seefeldt LC. "
               "Mechanism of nitrogen fixation by nitrogenase. Chemical "
               "Reviews 114, 4041-4062; 2014.")
CIT_LEWIS = ("Lewis NS, Nocera DG. Powering the planet: Chemical challenges "
             "in solar energy utilization. Proceedings of the National "
             "Academy of Sciences 103, 15729-15735; 2006.")
CIT_SCHLAPBACH = ("Schlapbach L, Zuettel A. Hydrogen-storage materials for "
                  "mobile applications. Nature 414, 353-358; 2001.")
CIT_SOMORJAI = ("Somorjai GA, Li Y. Introduction to Surface Chemistry and "
                "Catalysis. 2nd ed. Wiley; 2010.")
CIT_NORSKOV = ("Norskov JK et al. Towards the computational design of solid "
               "catalysts. Nature Chemistry 1, 37-46; 2009.")
CIT_BENEDICT = ("Benedict M, Pigford TH, Levi HW. Nuclear Chemical "
                "Engineering. McGraw-Hill; 1981.")
CIT_KAY = ("Kay ER, Leigh DA, Zerbetto F. Synthetic molecular motors and "
           "mechanical machines. Angewandte Chemie International Edition "
           "46, 72-191; 2007.")
CIT_COROPCEANU = ("Coropceanu V et al. Charge transport in organic "
                  "semiconductors. Chemical Reviews 107, 926-952; 2007.")
CIT_ADLEMAN = ("Adleman LM. Molecular computation of solutions to "
               "combinatorial problems. Science 266, 1021-1024; 1994.")
CIT_REYMOND = ("Reymond JL. The chemical space project. Accounts of Chemical "
               "Research 48, 722-730; 2015.")
CIT_CRAMER = ("Cramer CJ. Essentials of Computational Chemistry. 2nd ed. "
              "Wiley; 2004.")
CIT_TIELENS = ("Tielens AGGM. The Physics and Chemistry of the Interstellar "
               "Medium. Cambridge University Press; 2005.")
CIT_WIGNER = ("Wigner E, Huntington HB. On the possibility of a metallic "
              "modification of hydrogen. Journal of Chemical Physics 3, "
              "764-770; 1935.")
CIT_BEDNORZ = ("Bednorz JG, Mueller KA. Possible high Tc superconductivity "
               "in the Ba-La-Cu-O system. Zeitschrift fuer Physik B 64, "
               "189-193; 1986.")
CIT_JAIN = ("Jain A et al. Commentary: The Materials Project: A materials "
            "genome approach to accelerating materials innovation. APL "
            "Materials 1, 011002; 2013.")
CIT_PYYKKO = ("Pyykko P. Relativistic effects in structural chemistry. "
              "Chemical Reviews 88, 563-594; 1988.")
CIT_ROTHLISBERGER = ("Rothlisberger D et al. Kemp elimination catalysts by "
                     "computational enzyme design. Nature 453, 190-195; 2008.")

ENTRIES = [
    {
        "key": "mpemba",
        "name": "Why Does Hot Water Sometimes Freeze Faster Than Cold?",
        "group": "Approachable",
        "ladder_rank": 1,
        "ladder_tier": "approachable",
        "problem": (
            "The Mpemba effect: under some conditions, a container of hot "
            "water freezes before an otherwise identical container of cold "
            "water. This has been reported since Aristotle and named after "
            "Tanzanian schoolboy Erasto Mpemba, yet there is still no agreed "
            "mechanism. Many proposed explanations - evaporation, convection, "
            "supercooling, dissolved gases, container geometry - each explain "
            "some experiments and fail others. The deeper unsolved problem: "
            "what is the full, reproducible recipe of conditions that "
            "controls freezing order, and which physical factors dominate in "
            "each regime?"
        ),
        "background": (
            "Aristotle, Francis Bacon, and Descartes all noted that hot "
            "water can freeze first. The modern name comes from Erasto "
            "Mpemba, whose 1963 school experiment with ice cream mix led to a "
            "1969 paper with Denis Osborne. Since then, dozens of laboratory "
            "studies have confirmed the effect under specific conditions "
            "while others failed to reproduce it at all. Candidate "
            "mechanisms pile up: evaporation reduces the mass of the hot "
            "sample; convection stirs the hot sample while the cold sample "
            "stratifies; dissolved gases differ; hot water supercools less "
            "readily; frost on the freezer shelf melts and improves thermal "
            "contact; solutes concentrate differently. Mark Jeng's 2006 "
            "review showed that most experiments do not control enough "
            "variables to decide among them. Recent work suggests there is "
            "no single Mpemba effect - there are several distinct effects "
            "with different dominant causes, and the definition of 'freezes "
            "first' (first ice crystal vs fully solid) changes the winner."
        ),
        "why_it_matters": (
            "Freezing, crystallization, and heat transfer underpin food "
            "storage, cryopreservation of cells and organs, and materials "
            "processing. If we understood the competing mechanisms, we could "
            "design faster, more uniform freezing protocols and avoid "
            "surprises in industrial cooling. More fundamentally, it is a "
            "humbling case: a phenomenon a child can observe that still "
            "defeats a complete explanation."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the four-factor competition model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the Mpemba effect as a race between evaporation loss, "
            "convective mixing, supercooling depth, and thermal contact - "
            "and proposes the exact controlled experiment that would decide "
            "which factor wins in each regime."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the Mpemba effect not "
            "as one mechanism but as a competition of four measurable "
            "factors, and walks the elimination protocol explicitly.\n\n"
            "ASSUMPTIONS: (1) Two open-topped beakers, same volume, same "
            "freezer, differing only in initial temperature. (2) 'Freezes "
            "first' means the first appearance of ice crystals at the "
            "surface. (3) Ambient freezer air and shelf contact are "
            "characterized, not assumed identical. (4) Dissolved-gas content "
            "is measured, not ignored.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Evaporation ledger: hot "
            "water loses mass to evaporation before freezing begins; less "
            "mass means less heat to remove, so compute the evaporated "
            "fraction from vapor pressure curves. Step 2 - Convection check: "
            "a hot sample convects strongly while cooling, keeping it "
            "thermally uniform; a cold sample stratifies, so its surface "
            "reaches freezing temperature while its interior is still warm - "
            "compute the Biot-like mixing number for each. Step 3 - "
            "Supercooling depth: dissolved gases and prior heating history "
            "change nucleation sites; measure the supercooling each sample "
            "tolerates before the first crystal. Step 4 - Contact audit: "
            "melted frost under the hot beaker changes thermal contact; "
            "measure the contact conductance directly.\n\n"
            "PROPOSED MECHANISM: the freezing race is decided by whichever "
            "factor removes heat fastest in that setup; the demo walks a "
            "numerical four-factor model showing how changing one assumption "
            "flips the winner. There is no universal winner - the claim is "
            "that the effect is a family of regimes, each dominated by a "
            "different factor.\n\n"
            "WHAT WOULD CONFIRM IT: a published matrix experiment varying "
            "initial temperature, lid state (open/closed), gas content, and "
            "shelf insulation, where each regime's winner matches the "
            "four-factor prediction. WHAT WOULD KILL IT: finding a "
            "reproducible Mpemba case with all four factors measured and "
            "controlled that still shows hot freezing first against the "
            "model's prediction.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim hot water always "
            "freezes first (it does not), does not claim a single mechanism, "
            "and does not claim the model constants are universal - they "
            "must be measured per setup."
        ),
        "key_points": [
            "The Mpemba effect is real but fragile: it appears under specific conditions and vanishes under others, which is why decades of experiments disagree.",
            "At least five candidate mechanisms compete - evaporation, convection, supercooling, dissolved gases, thermal contact - and different experiments isolate different ones.",
            "The honest framing: there is likely no single Mpemba effect but a family of regime-dependent effects.",
            "A decisive experiment must control all four factors at once and measure, not assume, thermal contact and gas content.",
            "The Signature approach walks a four-factor competition model and proposes the exact elimination protocol.",
        ],
        "citations": [CIT_JENG, CIT_ATKINS],
    },
    {
        "key": "water_anomalies",
        "name": "Why Does Water Behave So Strangely?",
        "group": "Approachable",
        "ladder_rank": 2,
        "ladder_tier": "approachable",
        "problem": (
            "Water breaks the rules that govern nearly every other liquid. "
            "It expands when it freezes; its liquid is densest at 4 degrees "
            "Celsius; it has an enormous heat capacity, surface tension, and "
            "heat of vaporization; it becomes less viscous under pressure; "
            "its compressibility has a minimum. More than seventy such "
            "anomalies are catalogued. The unsolved problem: what single "
            "underlying structure of liquid water explains the whole family "
            "of anomalies at once, and is there a hidden liquid-liquid "
            "critical point deep in the supercooled region?"
        ),
        "background": (
            "For a century, water's anomalies were treated as a grab bag of "
            "oddities. The modern organizing idea, the two-liquid picture, "
            "proposes that liquid water is a fluctuating mixture of two "
            "local structures: a low-density, open, tetrahedral "
            "hydrogen-bond network and a high-density, collapsed, "
            "disordered arrangement. As temperature and pressure change, the "
            "balance shifts, and the anomalies emerge from the competition. "
            "This picture predicts a liquid-liquid critical point in deeply "
            "supercooled water - a second critical point where the two "
            "liquid forms become indistinguishable - which would explain why "
            "the anomalies grow stronger as water is cooled. The 2016 "
            "Chemical Reviews survey by Gallo and colleagues gathered the "
            "evidence for the tale of two liquids, but the critical point "
            "itself sits in 'no man's land', a temperature range where "
            "bulk water crystallizes faster than it can be studied. "
            "Computer simulations see it; experiments in confined water and "
            "in ultrafast X-ray probes see hints; a direct observation in "
            "bulk water remains out of reach."
        ),
        "why_it_matters": (
            "Water is the solvent of life, the coolant of power plants, the "
            "medium of the climate system. A unified theory of water's "
            "structure would sharpen every model of protein folding, "
            "solvation, weather, and ocean chemistry. The liquid-liquid "
            "hypothesis, if confirmed, would be the biggest conceptual "
            "advance in liquid physics in fifty years."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the two-state competition model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "treats the anomalies as the signature of two competing local "
            "water structures and proposes the specific X-ray and "
            "thermodynamic fingerprints that would prove or kill the "
            "liquid-liquid critical point."
        ),
        "sig_full": (
            LABEL + " The Signature approach adopts the two-liquid picture "
            "as the working hypothesis and derives testable fingerprints "
            "from it, step by step.\n\n"
            "ASSUMPTIONS: (1) Liquid water samples two local structural "
            "basins - open tetrahedral (low density) and collapsed "
            "disordered (high density) - with a free-energy difference that "
            "depends on temperature and pressure. (2) The anomalies are "
            "response functions (heat capacity, compressibility, expansivity) "
            "of the shifting population balance. (3) A liquid-liquid "
            "critical point exists in the supercooled region where the two "
            "populations merge.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Two-state mixture: write "
            "the liquid as a mixture with mole fraction x of the "
            "low-density form; every anomaly is the derivative of x with "
            "respect to temperature or pressure. Step 2 - Response peaks: "
            "show that the heat capacity maximum, the compressibility "
            "minimum, and the density maximum all fall out of one "
            "temperature-dependent x(T,P). Step 3 - Critical scaling: near "
            "the hypothesized critical point, fluctuations in x should grow "
            "with a specific power law - compute the predicted small-angle "
            "X-ray scattering intensity curve. Step 4 - Confinement bridge: "
            "predict how the anomalies shift in nanopores, where 'no man's "
            "land' can be entered without crystallization.\n\n"
            "PROPOSED MECHANISM: the 70+ anomalies are one phenomenon - the "
            "population balance of two local water structures swinging with "
            "temperature and pressure, ending at a liquid-liquid critical "
            "point.\n\n"
            "WHAT WOULD CONFIRM IT: observation of critical-like scattering "
            "divergence and Widom-line convergence in bulk or confined "
            "supercooled water matching the predicted exponents. WHAT WOULD "
            "KILL IT: a water model with no two-state structure that still "
            "reproduces all the anomalies, or scattering data in no man's "
            "land that flatly contradicts the predicted fluctuation growth.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the critical point "
            "has been observed (it has not), does not claim simulations "
            "prove reality, and does not claim the two-state picture is the "
            "only possible organizing principle."
        ),
        "key_points": [
            "Water has more than seventy documented anomalies - density maximum at 4 C, huge heat capacity, pressure-melting oddities - unmatched by any other common liquid.",
            "The leading organizing idea is the two-liquid picture: fluctuating open-tetrahedral and collapsed-disordered local structures.",
            "The picture predicts a liquid-liquid critical point in deeply supercooled water, hidden in a region where bulk water crystallizes too fast to study.",
            "Simulations and confined-water experiments support it; direct bulk observation is still missing.",
            "The Signature approach derives the response-function fingerprints and the exact scattering test that would settle it.",
        ],
        "citations": [CIT_GALLO, CIT_DEBENEDETTI, CIT_BALL_WATER],
    },
    {
        "key": "smell",
        "name": "What Is a Molecule Smell Made Of?",
        "group": "Approachable",
        "ladder_rank": 3,
        "ladder_tier": "approachable",
        "problem": (
            "Nobody fully knows how the nose converts a molecule's structure "
            "into the sensation of smell. The dominant theory says shape "
            "rules: receptors recognize molecular shape like locks and keys. "
            "The challenger, Luca Turin's vibration theory, says receptors "
            "also sense molecular vibrations via inelastic electron "
            "tunneling - predicting that replacing hydrogen with deuterium "
            "(same shape, different vibration) should change a smell. Some "
            "experiments support this; others, including a major 2015 study, "
            "find the effect implausible. The unsolved problem: what is the "
            "actual transduction mechanism at the olfactory receptor, and "
            "how much do vibrations contribute?"
        ),
        "background": (
            "Olfaction was long the least understood sense. The 1991 "
            "discovery of the olfactory receptor gene family showed the nose "
            "uses about 400 receptor types in humans, each binding many "
            "odorants. The shape theory - molecular shape and functional "
            "groups determine receptor binding - explains most structure-"
            "odor relationships. In 1996 Luca Turin proposed that receptors "
            "act as biological spectroscopes: an electron tunnels across the "
            "receptor only when the odorant's vibration matches the energy "
            "gap, making smell partly a matter of molecular vibration "
            "frequencies. The clean test is deuteration: deuterated and "
            "normal molecules have nearly identical shapes but different "
            "vibrational frequencies. Some studies reported humans and flies "
            "can distinguish them; a 2015 Proceedings of the National "
            "Academy of Sciences paper argued the physics makes the proposed "
            "mechanism implausible in real receptors. The field remains "
            "split, with evidence that both shape and vibration may play "
            "roles in different receptors."
        ),
        "why_it_matters": (
            "Smell drives flavor, memory, danger detection, and much of "
            "animal behavior; flavor and fragrance is a multi-billion "
            "industry built partly on trial and error. Cracking the "
            "transduction code would let chemists design scents rationally "
            "and build artificial noses that truly rival biology - for "
            "medical diagnosis by breath, explosives detection, and food "
            "safety."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the dual-channel receptor model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the receptor as using BOTH shape docking and a "
            "vibration-assisted tunneling check, and proposes the deuterated "
            "isotopomer experiment that would measure each channel's share."
        ),
        "sig_full": (
            LABEL + " The Signature approach refuses the shape-vs-vibration "
            "war and models the receptor as a two-stage device, deriving "
            "what each stage must contribute.\n\n"
            "ASSUMPTIONS: (1) An olfactory receptor has a binding pocket "
            "whose geometry sets which molecules dock (shape gate). (2) "
            "Signal transduction can be assisted by vibration-matched "
            "inelastic electron tunneling, as Turin proposed, but only "
            "where the receptor's donor-acceptor gap is tuned to it. "
            "(3) Deuteration changes vibrational frequencies by roughly the "
            "square root of 2 while leaving shape essentially unchanged.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Shape gate: compute "
            "docking - molecules that cannot fit the pocket cannot activate, "
            "regardless of vibration; this explains why shape theory works "
            "most of the time. Step 2 - Vibration audit: for a docked "
            "molecule, compute the H-to-D vibrational frequency shift (about "
            "1000 wavenumbers for C-H stretch) and ask whether it crosses "
            "the receptor's hypothesized tunneling gap. Step 3 - Dual "
            "prediction: the model predicts SOME receptor-odorant pairs "
            "show isotope effects (gap-tuned receptors) and others show "
            "none - reconciling the contradictory literature. Step 4 - "
            "Receptor-by-receptor map: propose screening a receptor panel "
            "against deuterated odorant libraries to classify each receptor "
            "as shape-only or shape-plus-vibration.\n\n"
            "PROPOSED MECHANISM: olfaction is a shape-gated, "
            "vibration-assisted process; the field's contradiction comes "
            "from averaging over receptors that differ in which channel "
            "dominates.\n\n"
            "WHAT WOULD CONFIRM IT: a receptor panel screen where a subset "
            "of receptors responds differently to deuterated vs normal "
            "odorants while the rest do not, matching the gap-tuning "
            "prediction. WHAT WOULD KILL IT: a complete receptor panel "
            "showing zero isotope effect anywhere, or a full shape-only "
            "model that predicts all observed odor responses.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim Turin is right in "
            "full, does not claim humans can smell deuterium differences in "
            "everyday odorants, and does not claim the tunneling physics is "
            "settled - it proposes the experiment that would settle each "
            "receptor's mechanism."
        ),
        "key_points": [
            "Two theories compete: shape-based lock-and-key docking versus vibration-sensing via electron tunneling.",
            "The decisive test is deuteration - same shape, different vibration - and the literature is genuinely split on the result.",
            "A 2015 study argued the tunneling physics is implausible in real receptors; other studies report measurable isotope effects.",
            "The contradiction may come from averaging over different receptors that use different mechanisms.",
            "The Signature approach proposes a receptor-by-receptor classification experiment to measure each channel's share.",
        ],
        "citations": [CIT_TURIN, CIT_BLOCK, CIT_CLAYDEN],
    },
    {
        "key": "protein_folding",
        "name": "How Do Proteins Fold Into Their Shapes?",
        "group": "Approachable",
        "ladder_rank": 4,
        "ladder_tier": "approachable",
        "problem": (
            "A protein chain can in principle adopt an astronomical number "
            "of shapes, yet in the cell it reliably folds into one working "
            "structure in milliseconds to seconds. This is Levinthal's "
            "paradox: a random search of all conformations would take longer "
            "than the age of the universe. Anfinsen showed the folded "
            "structure is encoded in the amino acid sequence, but the "
            "dynamical question - the actual pathways, the folding nucleus, "
            "why some proteins misfold into disease - remains unsolved in "
            "full. Structure prediction has leapt forward, yet the folding "
            "process itself, especially in the crowded cell, is still only "
            "partly understood."
        ),
        "background": (
            "In 1973 Christian Anfinsen showed that a denatured protein "
            "refolds spontaneously, proving the native structure is the "
            "thermodynamic minimum encoded by the sequence. Cyrus Levinthal "
            "pointed out the paradox: the chain cannot be searching "
            "randomly, so folding must follow biased pathways. The modern "
            "answer is the energy funnel: the energy landscape slopes "
            "toward the native state, guiding the chain downhill while "
            "local traps slow it. Dill and MacCallum's 2012 fifty-year "
            "review mapped how far the field had come - from lattice models "
            "to atomistic simulations to the stunning success of AI "
            "structure prediction. But prediction is not mechanism: the "
            "transient folding nucleus, the role of the ribosome and "
            "chaperones in the cell, and the misfolding routes behind "
            "Alzheimer's and prion diseases remain active frontiers. "
            "Intrinsically disordered proteins, which never settle into one "
            "shape, rewrote the one-sequence-one-structure rule entirely."
        ),
        "why_it_matters": (
            "Misfolded proteins cause Alzheimer's, Parkinson's, prion "
            "diseases, and many failures in biologic drugs. Understanding "
            "folding pathways - not just final structures - would let us "
            "predict which mutations cause misfolding, design proteins that "
            "fold reliably, and build drugs that rescue broken folders. It "
            "is the dynamical core beneath the whole protein revolution."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the funnel-plus-nucleus walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models folding as a biased funnel search seeded by a "
            "contact-order folding nucleus, and proposes the single-molecule "
            "experiment that would catch the nucleus forming."
        ),
        "sig_full": (
            LABEL + " The Signature approach takes the energy funnel as the "
            "framework and derives the folding nucleus as the testable "
            "core, step by step.\n\n"
            "ASSUMPTIONS: (1) The native state is the global free-energy "
            "minimum (Anfinsen). (2) The landscape is funnel-shaped but "
            "rugged: local traps exist. (3) A small set of native contacts - "
            "the folding nucleus - forms early and commits the chain; "
            "contact order (sequence separation of contacting residues) "
            "sets the folding speed.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Levinthal audit: count "
            "conformations for a short chain to show the paradox is real "
            "for random search, then show how even a weak energetic bias "
            "collapses the search time exponentially - the funnel's job. "
            "Step 2 - Nucleus identification: compute contact order and "
            "predict which residue pairs must meet first; these are the "
            "candidate nucleus. Step 3 - Trap census: enumerate the "
            "off-pathway traps and their escape times; the observed folding "
            "time is the nucleus commitment time plus trap delays. Step 4 - "
            "Cellular correction: add ribosome exit-tunnel and chaperone "
            "interactions as landscape tilts, predicting which proteins "
            "need chaperones from their trap census alone.\n\n"
            "PROPOSED MECHANISM: folding equals nucleus commitment on a "
            "biased funnel; misfolding equals commitment to a trap basin of "
            "comparable depth - disease mutations are trap-deepeners.\n\n"
            "WHAT WOULD CONFIRM IT: single-molecule FRET catching the "
            "predicted nucleus contacts forming before global collapse, "
            "with folding times matching the contact-order prediction "
            "across a protein family. WHAT WOULD KILL IT: proteins whose "
            "measured folding pathways show no early nucleus, or trap "
            "censuses that fail to predict chaperone dependence.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the funnel picture "
            "is complete (disordered proteins break it), does not claim "
            "prediction equals mechanism, and does not claim misfolding "
            "diseases are solved - it proposes the nucleus-catching "
            "experiment."
        ),
        "key_points": [
            "Levinthal's paradox: random search would outlast the universe, so folding must follow biased pathways down an energy funnel.",
            "Anfinsen proved the sequence encodes the native structure; the unsolved part is the dynamical pathway and the folding nucleus.",
            "Contact order - how far apart contacting residues sit in the sequence - predicts folding speed across many proteins.",
            "Misfolding diseases are trap basins: mutations that deepen off-pathway traps.",
            "The Signature approach walks the funnel-plus-nucleus model and proposes the single-molecule nucleus-catching test.",
        ],
        "citations": [CIT_ANFINSEN, CIT_DILL, CIT_CLAYDEN],
    },
    {
        "key": "enzyme_speed",
        "name": "Why Are Enzymes Such Spectacular Catalysts?",
        "group": "Approachable",
        "ladder_rank": 5,
        "ladder_tier": "approachable",
        "problem": (
            "Enzymes accelerate reactions by factors up to 10^21 - turning "
            "reactions that would take millions of years into millisecond "
            "events - yet after a century of study there is no consensus on "
            "exactly how. Linus Pauling's idea, that enzymes bind the "
            "transition state tighter than the substrate, is the "
            "textbook answer, but it does not explain everything: some "
            "enzymes show catalytic effects far beyond what binding energy "
            "alone accounts for. Competing explanations invoke electrostatic "
            "preorganization, quantum tunneling of hydrogen, protein "
            "dynamics gating the reaction, and near-attack conformers. The "
            "unsolved problem: the complete, quantitative accounting of an "
            "enzyme's rate enhancement, factor by factor."
        ),
        "background": (
            "Wolfenden and Snider's 2001 analysis quantified the staggering "
            "proficiencies of enzymes: rate enhancements of 10^10 to 10^21 "
            "over the uncatalyzed reactions. Pauling's 1948 transition-state "
            "stabilization idea became the foundation of enzymology and of "
            "catalytic antibody design. But puzzles accumulated. Kinetic "
            "isotope effects in some enzymes suggested hydrogen tunnels "
            "through the barrier rather than climbing it. Simulations by "
            "Warshel and others argued that the dominant effect is "
            "electrostatic preorganization - the enzyme's active site is "
            "already arranged to stabilize the transition state's charge "
            "distribution, while water must reorganize at great cost. Others "
            "argued protein motions - dynamics on microsecond to "
            "millisecond scales - gate the chemistry. The honest state of "
            "the field: each factor is proven in some enzyme, none is "
            "proven universal, and the full factor-by-factor ledger exists "
            "for only a handful of systems."
        ),
        "why_it_matters": (
            "A complete accounting of enzyme catalysis is the blueprint for "
            "designing artificial enzymes, better industrial biocatalysts, "
            "and drugs that inhibit pathogenic enzymes precisely. Every "
            "improvement in our understanding converts directly into "
            "cleaner chemical manufacturing - reactions run at room "
            "temperature in water instead of in toxic solvents at high "
            "heat."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the factor-by-factor ledger, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "builds the complete rate-enhancement ledger - transition-state "
            "binding, electrostatic preorganization, tunneling, dynamics - "
            "and proposes the isotope-effect experiment that assigns each "
            "factor its share."
        ),
        "sig_full": (
            LABEL + " The Signature approach builds the full "
            "factor-by-factor ledger of a 10^15-fold rate enhancement and "
            "derives the experiment that assigns each factor its share.\n\n"
            "ASSUMPTIONS: (1) The uncatalyzed reference reaction in water is "
            "the correct baseline (the Wolfenden proficiencies). (2) The "
            "enhancement factorizes, to first order, into separable "
            "contributions: transition-state binding, electrostatic "
            "preorganization, tunneling, and dynamical gating. (3) "
            "Temperature-dependent kinetic isotope effects separate "
            "tunneling from classical over-the-barrier contributions.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Ledger frame: write the "
            "observed 10^15 enhancement as a product of four factors and "
            "solve for each from independent measurements. Step 2 - "
            "Preorganization audit: compute the reorganization energy the "
            "enzyme avoids paying relative to water - Warshel's argument "
            "quantified. Step 3 - Tunneling check: use the "
            "temperature dependence of the kinetic isotope effect to bound "
            "the tunneling contribution; large, temperature-independent KIEs "
            "mean tunneling matters. Step 4 - Dynamics gate: compare "
            "catalytic rates in rigidified vs flexible enzyme variants to "
            "isolate the dynamical contribution.\n\n"
            "PROPOSED MECHANISM: the enhancement is a product of factors "
            "whose shares differ per enzyme - preorganization dominates "
            "most, tunneling dominates hydrogen-transfer specialists, "
            "dynamics gates conformationally complex cases.\n\n"
            "WHAT WOULD CONFIRM IT: a model enzyme where all four ledger "
            "entries are measured independently and their product matches "
            "the observed enhancement within an order of magnitude. WHAT "
            "WOULD KILL IT: an enzyme where the ledger's product misses the "
            "observed rate by many orders of magnitude with all factors "
            "measured, implying a missing catalytic principle.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim one universal "
            "mechanism (the field's evidence forbids it), does not claim "
            "factorization is exact, and does not claim we can yet design "
            "10^15-fold catalysts from the ledger alone."
        ),
        "key_points": [
            "Enzymes achieve rate enhancements up to 10^21 - the largest catalytic effects known in chemistry.",
            "Pauling's transition-state stabilization is the foundation but does not complete the accounting.",
            "Candidate extra factors: electrostatic preorganization, hydrogen tunneling, protein dynamics, near-attack conformers.",
            "The full factor-by-factor ledger exists for only a handful of enzymes.",
            "The Signature approach walks the ledger and proposes the isotope-effect experiment that assigns each factor its share.",
        ],
        "citations": [CIT_WOLFENDEN, CIT_CLAYDEN, CIT_ATKINS],
    },
    {
        "key": "hydrophobic",
        "name": "What Is the Hydrophobic Effect Really?",
        "group": "Approachable",
        "ladder_rank": 6,
        "ladder_tier": "approachable",
        "problem": (
            "Oil and water do not mix because water expels oily molecules - "
            "the hydrophobic effect drives protein folding, membrane "
            "formation, and micelles. Yet its molecular mechanism is still "
            "debated. For small oily solutes the effect is entropy-driven "
            "(water orders around them); for large oily surfaces it is "
            "enthalpy-driven (water's hydrogen bonds break). The crossover "
            "between these regimes, around one nanometer, is the famous "
            "length-scale puzzle. The unsolved problem: a single molecular "
            "theory that predicts, from first principles, the solvation "
            "thermodynamics of any oily solute at any size."
        ),
        "background": (
            "The classical picture, from Frank and Evans in 1945, said "
            "water forms ordered 'icebergs' around small hydrophobic "
            "solutes, costing entropy. For decades this entropy story ruled. "
            "Then experiments on large hydrophobic surfaces showed the "
            "opposite signature: the driving force was enthalpic, tied to "
            "broken hydrogen bonds and even dewetting - water pulling away "
            "from the surface. David Chandler's 2005 Nature review unified "
            "the picture: small solutes fit into water's hydrogen-bond "
            "network without breaking it (entropic cost), while large "
            "solutes force the network to reorganize or rupture (enthalpic "
            "cost), with the crossover near one nanometer. Lum, Chandler, "
            "and Weeks built this into a theory. But a fully predictive, "
            "first-principles account - one that takes any solute shape and "
            "returns its hydration free energy, enthalpy, and entropy - "
            "remains out of reach, and the fine details of water's "
            "restructuring at complex biomolecular surfaces are still being "
            "mapped."
        ),
        "why_it_matters": (
            "The hydrophobic effect is the main force that folds proteins, "
            "assembles cell membranes, and lets drugs bind their targets. A "
            "predictive theory would sharpen drug design (binding free "
            "energies), materials design (self-assembling structures), and "
            "our understanding of every membrane protein - the targets of "
            "most modern drugs."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the crossover walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models hydrophobic solvation as a length-scale crossover at "
            "one nanometer - entropic below, enthalpic above - and proposes "
            "the solute-size series experiment that maps the crossover "
            "exactly."
        ),
        "sig_full": (
            LABEL + " The Signature approach takes the Lum-Chandler-Weeks "
            "crossover picture and turns it into a predictive walkthrough "
            "with a decisive experiment.\n\n"
            "ASSUMPTIONS: (1) Water's hydrogen-bond network can accommodate "
            "solutes smaller than ~1 nm without breaking bonds (entropic "
            "regime). (2) Larger solutes force bond breaking or dewetting "
            "(enthalpic regime). (3) The hydration free energy, enthalpy, "
            "and entropy can be decomposed per unit of buried oily surface "
            "area in each regime.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Small-solute ledger: "
            "compute the entropy cost of ordering water around a methane-"
            "sized solute from the measured hydration thermodynamics. "
            "Step 2 - Large-surface ledger: compute the enthalpy cost of "
            "broken hydrogen bonds at an extended oily surface and the "
            "dewetting threshold. Step 3 - Crossover scan: walk a series of "
            "solutes from 0.3 to 3 nm, predicting where the entropy-driven "
            "signature flips to enthalpy-driven - the model says near 1 nm. "
            "Step 4 - Shape correction: extend from spheres to real "
            "biomolecular shapes by counting concave vs convex surface "
            "patches, since curvature sets the local regime.\n\n"
            "PROPOSED MECHANISM: hydrophobic solvation is one phenomenon "
            "with two thermodynamic faces, switching at the nanometer "
            "length scale where water's network can no longer wrap the "
            "solute intact.\n\n"
            "WHAT WOULD CONFIRM IT: calorimetry on a homologous solute "
            "series showing the entropy-to-enthalpy flip exactly at the "
            "predicted size, with curvature-corrected predictions matching "
            "protein-surface hydration data. WHAT WOULD KILL IT: a solute "
            "series with no clean crossover, or large-surface hydration "
            "that stays entropy-driven, contradicting the dewetting "
            "prediction.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the crossover is "
            "infinitely sharp (it is a smooth transition), does not claim "
            "first-principles prediction for arbitrary biomolecules yet, "
            "and does not claim the iceberg picture was simply wrong - it "
            "was the small-solute limit of the full theory."
        ),
        "key_points": [
            "The hydrophobic effect drives protein folding, membranes, and micelles - yet its mechanism is still debated.",
            "Small oily solutes: entropy-driven (water ordering). Large oily surfaces: enthalpy-driven (broken hydrogen bonds, dewetting).",
            "The crossover sits near one nanometer - the length-scale puzzle at the heart of the problem.",
            "Chandler's 2005 unification and Lum-Chandler-Weeks theory frame the modern picture, but full first-principles prediction is missing.",
            "The Signature approach walks the crossover and proposes the solute-size series that would map it exactly.",
        ],
        "citations": [CIT_CHANDLER, CIT_ATKINS, CIT_CLAYDEN],
    },
    {
        "key": "homochirality",
        "name": "Why Is All of Life Chemistry One-Handed?",
        "group": "Approachable",
        "ladder_rank": 7,
        "ladder_tier": "approachable",
        "problem": (
            "Life uses only left-handed amino acids and right-handed sugars - "
            "a property called homochirality - even though nonliving "
            "chemistry makes both mirror images equally. How did one hand "
            "win? Tiny initial imbalances could have been amplified by "
            "autocatalytic reactions, but where did the first imbalance "
            "come from - circularly polarized starlight, the weak nuclear "
            "force's parity violation, chiral mineral surfaces, or pure "
            "chance? The unsolved problem: the actual historical pathway "
            "from a racemic (50/50) prebiotic world to a single-handed "
            "biosphere."
        ),
        "background": (
            "Pasteur discovered molecular chirality in 1848 by separating "
            "left- and right-handed tartaric acid crystals by hand. The "
            "mystery of life's single handedness deepened as biochemistry "
            "showed it is universal: every organism uses L-amino acids and "
            "D-sugars. In 1953 Frank proposed the theoretical core - "
            "autocatalysis plus mutual antagonism can amplify a tiny "
            "enantiomeric excess into homochirality. In 1995 Soai and "
            "coworkers demonstrated it in the lab: an autocatalytic "
            "reaction that amplifies a minuscule chiral imbalance into near-"
            "complete single-handedness. Candidate seeds for the first "
            "imbalance include circularly polarized light from neutron "
            "stars, parity violation in the weak force (which makes "
            "left- and right-handed molecules differ in energy by a "
            "fantastically small amount), adsorption on chiral quartz or "
            "clay surfaces, and simple statistical fluctuation. Meteorites "
            "like Murchison carry small L-excesses in amino acids, hinting "
            "the seed may have come from space - but no chain from seed to "
            "biosphere is established."
        ),
        "why_it_matters": (
            "Homochirality is one of the deepest clues about life's origin - "
            "solving it constrains where and how life began, on Earth or "
            "elsewhere. It also matters practically: single-handed drugs "
            "are safer (the wrong hand of thalidomide caused tragedy), and "
            "understanding chiral amplification improves asymmetric "
            "synthesis, the backbone of modern pharmaceutical manufacturing."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the seed-plus-amplifier model, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models homochirality as a tiny physical seed (parity violation "
            "or polarized light) multiplied by Soai-type autocatalytic "
            "amplification, and proposes the measurement that would rank "
            "the candidate seeds."
        ),
        "sig_full": (
            LABEL + " The Signature approach separates the problem into two "
            "stages - seed and amplifier - and quantifies what each stage "
            "must deliver.\n\n"
            "ASSUMPTIONS: (1) Prebiotic chemistry began essentially racemic. "
            "(2) A Frank-type autocatalytic network (each hand catalyzes "
            "its own formation and suppresses the other) can amplify an "
            "initial excess. (3) The seed is a real physical asymmetry: "
            "weak-force parity violation, circularly polarized light, or "
            "chiral mineral surfaces.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Seed audit: compute the "
            "size of each candidate seed - parity violation gives "
            "energy differences around 10^-17 kT, polarized light can give "
            "percent-level excesses under ideal conditions, mineral "
            "surfaces give adsorption selectivities of a few percent. "
            "Step 2 - Amplifier math: run the Frank autocatalysis model to "
            "find the minimum seed each amplifier needs to reach "
            "homochirality before side reactions racemize the pool. Step 3 "
            "- Race condition: the amplifier must outrun racemization - "
            "compute the required rate margin for each seed candidate. "
            "Step 4 - Meteoritic check: compare the predicted surviving "
            "excess in carbonaceous meteorites with the measured L-excesses "
            "in Murchison amino acids.\n\n"
            "PROPOSED MECHANISM: a small physical seed (ranked by the audit) "
            "fed into an autocatalytic amplifier that outran racemization; "
            "homochirality is the frozen outcome of that race.\n\n"
            "WHAT WOULD CONFIRM IT: a laboratory prebiotic network "
            "demonstrating seed-to-homochirality with a measured seed, plus "
            "meteoritic excesses matching the predicted survivor pattern. "
            "WHAT WOULD KILL IT: proof that no plausible amplifier outruns "
            "racemization under prebiotic conditions, or a second genesis "
            "found using the opposite hand - which would point to chance "
            "rather than a universal seed.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim to know which seed "
            "won, does not claim the Soai reaction is prebiotic (it is a "
            "model, not a history), and does not claim homochirality was "
            "necessary for life rather than a frozen accident."
        ),
        "key_points": [
            "Life is homochiral - L-amino acids, D-sugars - while nonliving chemistry makes both hands equally.",
            "Frank (1953) showed autocatalysis can amplify a tiny imbalance; Soai (1995) demonstrated it in the lab.",
            "Candidate seeds: parity violation, circularly polarized starlight, chiral minerals, pure chance.",
            "Meteorites carry small L-excesses, hinting at an extraterrestrial seed - but the chain to the biosphere is unproven.",
            "The Signature approach splits seed from amplifier and computes which seeds could actually have won the race.",
        ],
        "citations": [CIT_SOAI, CIT_SUTHERLAND, CIT_CLAYDEN],
    },
    {
        "key": "abiogenesis",
        "name": "Where Did the Chemistry of Life Come From?",
        "group": "Approachable",
        "ladder_rank": 8,
        "ladder_tier": "approachable",
        "problem": (
            "How did nonliving chemistry become living chemistry? The "
            "Miller-Urey experiment showed amino acids form in simulated "
            "early-Earth conditions, and modern work builds nucleotides "
            "under plausible prebiotic conditions - but no experiment has "
            "produced a self-reproducing chemical system from nonliving "
            "starting materials. Competing scenarios (warm ponds, deep-sea "
            "vents, wet-dry cycling, delivery from space) each explain part "
            "of the chemistry and none closes the loop. The unsolved "
            "problem: a continuous, experimentally demonstrated pathway "
            "from simple molecules to a self-sustaining, evolving chemical "
            "system."
        ),
        "background": (
            "In 1953 Stanley Miller, working with Harold Urey, sparked a "
            "mixture of methane, ammonia, hydrogen, and water and produced "
            "amino acids - proof that life's building blocks form without "
            "life. The decades since have been a long march: the formose "
            "reaction makes sugars from formaldehyde; Sutherland's group "
            "showed activated nucleotides can form under plausibly "
            "prebiotic conditions; deep-sea vent chemistry offers natural "
            "proton gradients that resemble cellular energy systems; "
            "wet-dry cycling concentrates and polymerizes building blocks. "
            "Yet the gaps are famous: making building blocks is not making "
            "polymers; making polymers is not making replication; making "
            "replication is not making evolution. The RNA world hypothesis - "
            "that RNA was both genome and catalyst - organized the field "
            "but still lacks a demonstrated prebiotic route to "
            "self-replicating RNA. Each scenario has a strongest link and a "
            "weakest link, and the weakest links differ by scenario, which "
            "is why the debate persists."
        ),
        "why_it_matters": (
            "This is the question of our own origin - and the template for "
            "recognizing life elsewhere. A demonstrated pathway would tell "
            "us how common life should be in the universe and guide the "
            "search for biosignatures on exoplanets. Practically, prebiotic "
            "chemistry has already gifted us new synthetic methods and "
            "self-assembling materials."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the network-bootstrapping walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models abiogenesis as an autocatalytic reaction network that "
            "bootstraps itself during wet-dry cycling on mineral surfaces, "
            "and proposes the closure experiment that would demonstrate the "
            "loop closing."
        ),
        "sig_full": (
            LABEL + " The Signature approach frames abiogenesis as a "
            "network-closure problem and derives the experiment that would "
            "demonstrate closure.\n\n"
            "ASSUMPTIONS: (1) Building blocks (amino acids, nucleobases, "
            "sugars, phosphates) were available from Miller-type, vent, or "
            "meteoritic sources. (2) Wet-dry cycling on mineral surfaces "
            "concentrates reactants and drives polymerization. (3) A "
            "chemical network is 'alive' in the minimal sense when it is "
            "autocatalytic as a whole - every member is produced by "
            "reactions within the set - and capable of variation and "
            "selection.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Inventory: list the "
            "demonstrated prebiotic reactions (building-block syntheses) "
            "and their yields - the parts bin. Step 2 - Network assembly: "
            "connect the parts into a reaction graph and compute which "
            "subsets are collectively autocatalytic (reflexively "
            "autocatalytic sets, after Kauffman). Step 3 - Cycling drive: "
            "model wet-dry cycles as a ratchet that concentrates "
            "monomers and selects for longer polymers, computing the "
            "cycle count needed to reach catalytic closure. Step 4 - "
            "Closure experiment: propose the actual flask experiment - "
            "starting mixture, cycle protocol, mineral surface - with "
            "predicted milestones (first oligomers, first catalysis of "
            "network reactions, sustained replication).\n\n"
            "PROPOSED MECHANISM: life began as a collectively autocatalytic "
            "network bootstrapped by environmental cycling, not as a single "
            "miracle molecule; replication of the network preceded "
            "replication of any individual polymer.\n\n"
            "WHAT WOULD CONFIRM IT: a laboratory system that, from "
            "nonliving starting materials under cycling, develops a "
            "sustained autocatalytic network showing heritable variation. "
            "WHAT WOULD KILL IT: proof that no collectively autocatalytic "
            "set is reachable from the demonstrated parts bin, or that "
            "cycling destroys polymers faster than it builds them under all "
            "plausible conditions.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the RNA world is "
            "wrong, does not claim vents beat ponds (the network math is "
            "scenario-agnostic), and does not claim a flask experiment "
            "would prove Earth's history - only that the pathway is "
            "chemically possible."
        ),
        "key_points": [
            "Miller-Urey (1953) proved life's building blocks form without life; the gap from building blocks to self-reproduction is still open.",
            "Competing scenarios - warm ponds, deep-sea vents, wet-dry cycling, space delivery - each explain part of the chemistry.",
            "The RNA world organizes the field but lacks a demonstrated prebiotic route to self-replicating RNA.",
            "The Signature reframe: the target is network closure (a collectively autocatalytic set), not a single miracle molecule.",
            "The Signature approach proposes the closure experiment with predicted milestones from oligomers to sustained replication.",
        ],
        "citations": [CIT_MILLER, CIT_SUTHERLAND, CIT_CLAYDEN],
    },
    {
        "key": "photosystem",
        "name": "How Do Plants Split Water With Sunlight?",
        "group": "Approachable",
        "ladder_rank": 9,
        "ladder_tier": "approachable",
        "problem": (
            "Photosystem II splits water into oxygen, protons, and electrons "
            "using sunlight - the reaction that made Earth's oxygen "
            "atmosphere and powers nearly all life. Its catalytic heart, "
            "the Mn4CaO5 cluster, was imaged at atomic resolution in 2011, "
            "yet the exact sequence of proton and electron transfers, the "
            "precise O-O bond-forming step, and how the protein avoids "
            "wasteful back-reactions remain debated. The unsolved problem: "
            "the complete, step-by-step mechanism of biological water "
            "oxidation at the atomic level."
        ),
        "background": (
            "Oxygenic photosynthesis evolved over two billion years ago and "
            "transformed the planet. The water-oxidizing complex cycles "
            "through five states (S0 through S4, the Kok cycle), "
            "accumulating four oxidizing equivalents from four photons "
            "before releasing one O2 molecule. The 1.9-angstrom crystal "
            "structure of 2011 revealed the Mn4CaO5 cluster's distorted-"
            "chair geometry and its water channels. Since then, X-ray "
            "free-electron lasers have caught the cluster in action, "
            "showing manganese oxidation states shifting through the cycle. "
            "But the crux - how the O-O bond actually forms in the S4 "
            "state, whether by oxyl radical coupling or nucleophilic attack "
            "of water, and how protons are shuttled out through specific "
            "channels without short-circuiting - is still contested. "
            "Multiple computational models fit parts of the data; no single "
            "mechanism satisfies all spectroscopic, kinetic, and structural "
            "constraints at once."
        ),
        "why_it_matters": (
            "Artificial photosynthesis - splitting water with sunlight to "
            "make hydrogen fuel - is the clean-energy dream, and nature's "
            "catalyst is the existence proof and the blueprint. Every "
            "mechanistic detail we extract guides the design of cheap, "
            "earth-abundant water-oxidation catalysts. Understanding the "
            "proton channels also illuminates how biology moves protons "
            "generally, from respiration to ATP synthesis."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the redox-leveling walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the Mn4CaO5 cluster as a redox-leveling machine that "
            "keeps each oxidation step affordable via coupled proton loss, "
            "and proposes the spectroscopic fingerprint that would identify "
            "the O-O bond-forming intermediate."
        ),
        "sig_full": (
            LABEL + " The Signature approach walks the Kok cycle as a "
            "redox-leveling machine and derives the fingerprint of the "
            "decisive intermediate.\n\n"
            "ASSUMPTIONS: (1) The S-state cycle accumulates four holes on "
            "the Mn4CaO5 cluster before O2 release. (2) Each oxidation is "
            "proton-coupled: losing a proton with each electron keeps the "
            "redox potentials level (no step becomes impossibly uphill). "
            "(3) The O-O bond forms in the transient S4 state by one of "
            "two routes: oxyl-oxo coupling or water nucleophilic attack.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Potential ladder: "
            "compute the redox potential of each S-state transition with "
            "and without coupled proton loss, showing that uncoupled "
            "oxidation would stall the cycle. Step 2 - Proton audit: trace "
            "the proposed proton-exit channels and count the protons "
            "released per transition against measurements. Step 3 - O-O "
            "decision: compute the predicted Mn oxidation-state pattern "
            "and O-O vibrational frequency for each bond-forming route. "
            "Step 4 - Fingerprint: predict the exact spectroscopic "
            "signature (X-ray emission, vibrational) of the S4 "
            "intermediate under each route.\n\n"
            "PROPOSED MECHANISM: the cluster is a charge-leveling device - "
            "proton-coupled electron transfer keeps every step within the "
            "photon's energy budget, and the protein's channels enforce "
            "the proton bookkeeping that prevents back-reaction.\n\n"
            "WHAT WOULD CONFIRM IT: time-resolved X-ray spectroscopy "
            "catching the S4 intermediate with the predicted oxidation "
            "pattern and O-O frequency. WHAT WOULD KILL IT: an S4 "
            "fingerprint matching neither route's prediction, or a "
            "demonstrated water-oxidation cycle that skips proton coupling "
            "without stalling.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the O-O mechanism "
            "is settled (it is the contested core), does not claim the "
            "computational models are converged, and does not claim an "
            "artificial mimic will match the enzyme's efficiency - only "
            "that the leveling principle is the design rule to copy."
        ),
        "key_points": [
            "Photosystem II's Mn4CaO5 cluster splits water using four photons per O2 - the reaction behind Earth's oxygen atmosphere.",
            "The 1.9-angstrom structure (2011) and X-ray laser movies revealed the machinery, but the O-O bond-forming step is still contested.",
            "Two candidate routes: oxyl radical coupling versus nucleophilic attack of water.",
            "Proton-coupled electron transfer keeps each oxidation step affordable - the redox-leveling principle.",
            "The Signature approach derives the S4 intermediate's spectroscopic fingerprint that would decide the mechanism.",
        ],
        "citations": [CIT_UMENA, CIT_LEWIS, CIT_HOUSECROFT],
    },
    {
        "key": "glass",
        "name": "What Is a Glass: Liquid or Solid?",
        "group": "Approachable",
        "ladder_rank": 10,
        "ladder_tier": "approachable",
        "problem": (
            "Cool a liquid fast enough and it never crystallizes - it "
            "becomes a glass, like window glass or amber. The viscosity "
            "rises by fourteen orders of magnitude over a small temperature "
            "range, yet no sharp phase transition is visible and the "
            "structure looks like a liquid's. Is the glass transition a "
            "true thermodynamic phase transition hidden below the "
            "experimental glass temperature, or purely a kinetic freezing of "
            "motion? After decades, the field is split between competing "
            "theories, and the nature of the glass transition remains one "
            "of the deepest unsolved problems in condensed matter."
        ),
        "background": (
            "When a liquid is supercooled, its viscosity climbs "
            "super-exponentially - far faster than the simple Arrhenius law "
            "predicts - until molecular motion effectively stops at the "
            "glass transition temperature. Debenedetti and Stillinger's "
            "2001 review framed the central mystery: the structure barely "
            "changes while the dynamics slow by factors of 10^14. "
            "Competing theories abound. Adam-Gibbs ties the slowdown to a "
            "vanishing configurational entropy, implying a true "
            "thermodynamic transition (the Kauzmann paradox) lurking below. "
            "Random first-order transition theory predicts a growing "
            "cooperativity length - regions of molecules that must move "
            "together. Dynamic facilitation says there is no thermodynamics "
            "at all, only kinetic constraints propagating through space. "
            "Experiments keep finding dynamic heterogeneity - fast and slow "
            "patches coexisting - which every theory claims as support. No "
            "experiment has yet reached the predicted hidden transition, "
            "because the system falls out of equilibrium first."
        ),
        "why_it_matters": (
            "Glasses are everywhere: windows, optical fibers, phone "
            "screens, metallic glasses, amorphous pharmaceuticals, and the "
            "vitrified states used to preserve cells and vaccines. A true "
            "theory of the glass transition would let us design "
            "ultra-stable glasses, predict drug shelf life, and control "
            "amorphous materials rationally instead of by recipe."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the cooperativity walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the glass transition as a growing cooperativity length "
            "with a hidden thermodynamic transition below, and proposes "
            "the ultrastable-glass experiment that would reach it."
        ),
        "sig_full": (
            LABEL + " The Signature approach takes the growing-"
            "cooperativity picture as the working model and derives the "
            "experiment that could reach the hidden transition.\n\n"
            "ASSUMPTIONS: (1) As a liquid supercools, molecular motion "
            "requires increasingly large cooperatively rearranging regions; "
            "the region size (cooperativity length) grows as temperature "
            "falls. (2) The viscosity follows the Vogel-Fulcher-Tammann "
            "law, diverging at a finite temperature below the laboratory "
            "glass transition. (3) Vapor-deposited ultrastable glasses "
            "access states far below the ordinary glass transition, "
            "approaching the hypothesized hidden transition.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Slowdown audit: fit "
            "viscosity data to both Arrhenius (no transition) and VFT "
            "(hidden transition) forms and quantify how strongly the data "
            "prefer super-Arrhenius behavior. Step 2 - Length census: "
            "extract the cooperativity length from dynamic heterogeneity "
            "measurements (multi-point susceptibilities) and check whether "
            "it grows as the theories predict. Step 3 - Entropy check: "
            "compute the configurational entropy from calorimetry and test "
            "the Adam-Gibbs correlation between entropy and relaxation "
            "time. Step 4 - Ultrastable probe: predict the calorimetric "
            "signature an ultrastable glass should show if a true "
            "transition lies beneath.\n\n"
            "PROPOSED MECHANISM: the glass transition is the kinetic "
            "shadow of a genuine thermodynamic transition (random first-"
            "order type) that experiments cannot quite reach because the "
            "system falls out of equilibrium first.\n\n"
            "WHAT WOULD CONFIRM IT: an ultrastable glass or aged glass "
            "showing the predicted thermodynamic signature (a sharp "
            "entropy or heat-capacity feature) at the extrapolated "
            "transition temperature. WHAT WOULD KILL IT: cooperativity "
            "lengths that saturate instead of growing, or a system that "
            "reaches the predicted transition temperature in equilibrium "
            "with no thermodynamic feature.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the hidden "
            "transition is proven (it is not), does not claim dynamic "
            "facilitation is ruled out, and does not claim all glass-"
            "formers behave identically - strong and fragile liquids "
            "differ, and the model must handle both."
        ),
        "key_points": [
            "A supercooled liquid's viscosity rises 10^14-fold with almost no structural change - the central mystery of the glass transition.",
            "Competing theories: hidden thermodynamic transition (Adam-Gibbs, random first-order) versus pure kinetic freezing (dynamic facilitation).",
            "Dynamic heterogeneity - coexisting fast and slow regions - is observed but claimed by every theory.",
            "Ultrastable vapor-deposited glasses may let experiments approach the hypothesized hidden transition.",
            "The Signature approach walks the cooperativity audit and proposes the ultrastable-glass test.",
        ],
        "citations": [CIT_DEB_STILL, CIT_DEBENEDETTI, CIT_ATKINS],
    },
    {
        "key": "proton_hop",
        "name": "How Do Protons Hop Through Water?",
        "group": "Approachable",
        "ladder_rank": 11,
        "ladder_tier": "approachable",
        "problem": (
            "Protons move through water far faster than other ions - about "
            "five times faster than sodium - by the Grotthuss mechanism: "
            "instead of swimming, the proton hops from water molecule to "
            "water molecule along hydrogen bonds. But the fine details are "
            "still debated: does the excess proton live mostly as an Eigen "
            "cation (H9O4+, proton locked on one water) or a Zundel cation "
            "(H5O2+, proton shared between two)? How do the surrounding "
            "waters reorganize to let the hop happen? The unsolved problem: "
            "the complete molecular movie of proton transport in water."
        ),
        "background": (
            "In 1806 Theodor von Grotthuss proposed that water conducts "
            "electricity by chains of molecules passing something along - "
            "a stunning guess made before molecules were understood. The "
            "modern picture: an excess proton in water forms fleeting "
            "structures - the Eigen cation, with the proton localized on a "
            "central hydronium solvated by three waters, and the Zundel "
            "cation, with the proton shared between two waters. "
            "Spectroscopy and simulation suggest the proton interconverts "
            "between these forms as surrounding waters rearrange, and the "
            "hop itself is gated by this reorganization: the proton can "
            "only move when the second solvation shell is correctly "
            "aligned. Agmon's 1995 review organized the mechanism, and "
            "ultrafast spectroscopy has since clocked the interconversion "
            "at sub-picosecond timescales. Yet the exact sequence - which "
            "water moves first, how far the structural diffusion extends, "
            "how the picture changes at interfaces and in confinement - "
            "remains contested, with simulations and experiments still "
            "negotiating."
        ),
        "why_it_matters": (
            "Proton transport is the currency of bioenergetics: respiration "
            "and photosynthesis pump protons, and ATP synthase spends the "
            "gradient. Fuel cells live or die by proton conduction through "
            "their membranes. A complete molecular movie would guide better "
            "fuel-cell membranes, better understanding of acid-base "
            "chemistry in confinement, and the design of protonic devices."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the gated-hop walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models proton transport as Zundel-Eigen interconversion gated "
            "by second-shell reorganization, and proposes the isotope-"
            "labeled spectroscopy test that would film each hop's "
            "choreography."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the proton as a "
            "structural defect whose motion is gated by the water network, "
            "and derives the choreography test.\n\n"
            "ASSUMPTIONS: (1) The excess proton exists as interconverting "
            "Eigen (localized) and Zundel (shared) forms. (2) A hop "
            "requires pre-organization of the second solvation shell - the "
            "network must align before the proton can move. (3) The "
            "observed mobility is the product of hop frequency and "
            "successful-hop probability (many attempts abort).\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Speciation census: "
            "from spectroscopy, estimate the Eigen-Zundel population ratio "
            "and the interconversion rate. Step 2 - Gating audit: compute "
            "how the hop rate depends on second-shell order parameters "
            "from simulation trajectories - the gate's signature. Step 3 "
            "- Abort count: count attempted vs completed hops to get the "
            "success probability; the model predicts most attempts fail "
            "because the gate was not ready. Step 4 - Isotope probe: "
            "predict how deuteration changes each step's rate (heavier "
            "deuterons hop slower and gate differently), giving a "
            "multi-point fingerprint.\n\n"
            "PROPOSED MECHANISM: proton mobility equals rapid "
            "Eigen-Zundel interconversion times a network-gating factor; "
            "the water does the work, the proton rides the reorganization.\n\n"
            "WHAT WOULD CONFIRM IT: 2D infrared spectroscopy on "
            "isotope-labeled water resolving the predicted sequence - "
            "shell reorganization, then interconversion, then hop - with "
            "the predicted abort ratio. WHAT WOULD KILL IT: a hop "
            "sequence that proceeds without prior shell reorganization, "
            "or mobility that does not factor into interconversion and "
            "gating components as predicted.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the Eigen-Zundel "
            "assignment is final (the field still argues), does not claim "
            "simulations are reality, and does not claim the bulk picture "
            "transfers unchanged to interfaces or confinement - those are "
            "separate records."
        ),
        "key_points": [
            "Protons move through water ~5x faster than other ions by hopping along hydrogen bonds - the Grotthuss mechanism (1806).",
            "The excess proton interconverts between Eigen (localized) and Zundel (shared) forms on sub-picosecond timescales.",
            "The hop is gated: surrounding waters must reorganize before the proton can move, and most attempts abort.",
            "The exact choreography - which water moves first, how far the defect spreads - is still contested.",
            "The Signature approach factors mobility into interconversion and gating and proposes the isotope-labeled film test.",
        ],
        "citations": [CIT_AGMON, CIT_ATKINS, CIT_BALL_WATER],
    },
    {
        "key": "water_surface",
        "name": "What Happens at the Surface of Water?",
        "group": "Approachable",
        "ladder_rank": 12,
        "ladder_tier": "approachable",
        "problem": (
            "The surface of water is not just bulk water cut off - "
            "molecules there orient, ions distribute unevenly, and the "
            "surface carries an electric charge whose sign is still "
            "argued about. Experiments suggest the air-water interface is "
            "negatively charged (hydroxide enriched), while some "
            "simulations find hydronium prefers the surface. This "
            "contradiction sits at the heart of atmospheric chemistry, "
            "electrochemistry, and biology's membrane interfaces. The "
            "unsolved problem: the true molecular structure and charge "
            "distribution of water's interfaces."
        ),
        "background": (
            "For a century, textbooks taught that ions are repelled from "
            "the air-water interface - the classic Onsager-Samaras image "
            "charge argument. Then simulations in the early 2000s showed "
            "large polarizable ions like iodide actually prefer the "
            "surface, and experiments confirmed it: the Hofmeister series, "
            "long a mystery of protein chemistry, is partly an interface "
            "story. Jungwirth and Tobias's 2006 review organized the new "
            "picture of specific ion effects at interfaces. But water's own "
            "ions remain contested: surface-sensitive spectroscopy and "
            "electrokinetic measurements point to hydroxide enrichment "
            "(negative surface), while several simulations put hydronium at "
            "the surface instead. The disagreement matters because the "
            "surface charge controls how droplets nucleate in clouds, how "
            "aerosols react in the atmosphere, and how proteins meet "
            "membranes. Different techniques probe different depths and "
            "different definitions of 'surface', which is why the "
            "contradiction has survived this long."
        ),
        "why_it_matters": (
            "Cloud droplets form on aerosol surfaces - their chemistry "
            "sets climate-relevant properties. Every electrochemical cell "
            "operates at a water interface; every cell membrane is one. "
            "Settling the surface's structure and charge would sharpen "
            "atmospheric models, battery design, and our picture of "
            "biological interfaces."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the depth-resolved walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "resolves the hydronium-hydroxide contradiction as a "
            "depth-resolution problem - different techniques average over "
            "different layers - and proposes the layered measurement that "
            "would map the true profile."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the surface-charge "
            "contradiction as a measurement-depth problem and derives the "
            "layered profile each technique should see.\n\n"
            "ASSUMPTIONS: (1) The interface is several molecular layers "
            "thick, with orientation, density, and ion concentration each "
            "varying with depth. (2) Different techniques weight different "
            "depths: electrokinetics senses the shear plane, sum-frequency "
            "spectroscopy senses the topmost oriented layer, simulations "
            "report the full profile. (3) Hydronium and hydroxide have "
            "genuinely different depth preferences.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Profile hypothesis: "
            "propose a layered model - hydronium enriched in the topmost "
            "layer, hydroxide enriched just beneath, net charge depending "
            "on where you cut. Step 2 - Technique audit: compute what each "
            "major technique (zeta potential, SFG spectroscopy, X-ray "
            "reflectivity, simulation) should report given the layered "
            "profile - showing the 'contradiction' is expected. Step 3 - "
            "Ion series: extend to the Hofmeister ions, predicting each "
            "ion's depth preference from polarizability and size. Step 4 "
            "- Decisive layering: propose depth-resolved spectroscopy "
            "with isotopic labeling to measure the hydronium and "
            "hydroxide profiles separately.\n\n"
            "PROPOSED MECHANISM: there is no single surface charge - the "
            "interface is a stratified charge structure, and each "
            "experiment has been correctly reporting its own layer.\n\n"
            "WHAT WOULD CONFIRM IT: depth-resolved measurements showing "
            "the predicted hydronium-top/hydroxide-subsurface stratification, "
            "with each classical technique's result recovered as the "
            "appropriate depth average. WHAT WOULD KILL IT: a technique-"
            "independent profile showing uniform ion distribution, or "
            "layered measurements contradicting the predicted "
            "stratification order.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim simulations are "
            "wrong or experiments are wrong (both may be right about "
            "different layers), does not claim the profile is universal "
            "across all interfaces, and does not claim atmospheric "
            "implications are settled - those follow after the profile "
            "does."
        ),
        "key_points": [
            "Water's surface has its own molecular structure, ion preferences, and charge - distinct from the bulk.",
            "Experiments suggest a negative surface (hydroxide enriched); some simulations favor hydronium - a genuine contradiction.",
            "The resolution may be depth: different techniques average over different molecular layers.",
            "Specific ion effects (Hofmeister series) are partly an interface story, confirmed for large polarizable ions.",
            "The Signature approach models a stratified charge profile and proposes the layered measurement to map it.",
        ],
        "citations": [CIT_JUNGWIRTH, CIT_ATKINS, CIT_BALL_WATER],
    },
    {
        "key": "nucleation",
        "name": "How Do Crystals Begin?",
        "group": "Deep",
        "ladder_rank": 13,
        "ladder_tier": "deep",
        "problem": (
            "Before a crystal exists, a tiny cluster of molecules must "
            "decide to become one - the nucleation event. Classical "
            "nucleation theory pictures a single step: a crystalline "
            "cluster grows past a critical size. But experiments keep "
            "catching a two-step route: first a dense disordered droplet, "
            "then crystal order appearing inside it. Which route dominates, "
            "under what conditions, and what the true free-energy landscape "
            "looks like, is still unsettled. The unsolved problem: the "
            "real molecular pathway of crystal nucleation."
        ),
        "background": (
            "Classical nucleation theory, built by Gibbs, Volmer, and "
            "others, treats nucleation as a tug-of-war: bulk free energy "
            "favors the new phase while surface tension opposes it, giving "
            "a critical nucleus size and a rate. It works beautifully in "
            "some systems and fails by orders of magnitude in others. In "
            "1997 ten Wolde and Frenkel showed that near a metastable "
            "fluid-fluid critical point, protein crystallization is "
            "dramatically enhanced by density fluctuations - a hint that "
            "nucleation is a two-variable story (density and order), not "
            "one. Since then, two-step nucleation - dense liquid droplet "
            "first, crystal inside it second - has been observed in "
            "proteins, colloids, calcium carbonate, and organic molecules. "
            "Yet classical one-step nucleation is also observed, and the "
            "field cannot yet predict which pathway a given system will "
            "take. Kashchiev's 2000 treatise remains the theoretical "
            "bedrock, but the two-step phenomenology still lacks a "
            "predictive theory of comparable power."
        ),
        "why_it_matters": (
            "Crystallization is how we make pharmaceuticals (most drugs "
            "are crystals), semiconductors, and countless materials - and "
            "how kidney stones and ice form where they should not. "
            "Controlling which polymorph nucleates, and when, is worth "
            "billions in drug manufacturing alone. A predictive nucleation "
            "theory would turn crystallization from an art into an "
            "engineering discipline."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the two-pathway walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models nucleation as a competition between one-step and "
            "two-step pathways on a two-dimensional (density, order) "
            "landscape, and proposes the fluctuation-spectroscopy test "
            "that predicts which path a system takes."
        ),
        "sig_full": (
            LABEL + " The Signature approach puts nucleation on a "
            "two-dimensional landscape and derives the pathway-selection "
            "rule.\n\n"
            "ASSUMPTIONS: (1) Nucleation is described by two order "
            "parameters: local density and local crystalline order. (2) "
            "The free-energy surface over this plane has a saddle for the "
            "classical path and a valley-through-dense-liquid for the "
            "two-step path. (3) Which saddle is lower depends on "
            "supersaturation and on how close the system is to any hidden "
            "fluid-fluid critical point.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Landscape sketch: "
            "compute the classical barrier from surface tension and "
            "driving force (the Gibbs baseline). Step 2 - Dense-liquid "
            "valley: estimate the barrier for forming a dense disordered "
            "droplet, then for ordering within it - the two-step total. "
            "Step 3 - Pathway race: the observed route is the lower "
            "barrier; derive the selection rule as a function of "
            "supersaturation and critical-point proximity. Step 4 - "
            "Fluctuation fingerprint: predict the pre-nucleation "
            "fluctuation spectrum each pathway imprints (density "
            "fluctuations spike before order in two-step).\n\n"
            "PROPOSED MECHANISM: nucleation is a pathway competition on "
            "the density-order plane; two-step wins whenever a dense-"
            "liquid valley undercuts the classical saddle, especially "
            "near hidden critical points.\n\n"
            "WHAT WOULD CONFIRM IT: light-scattering or X-ray "
            "measurements catching density fluctuations rising before any "
            "crystalline order in a system the rule predicts is two-step, "
            "and the reverse order where it predicts classical. WHAT "
            "WOULD KILL IT: systems that nucleate with no detectable "
            "pathway dependence on critical-point proximity, or a "
            "single-pathway theory that predicts all observed rates.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim classical theory "
            "is dead (it wins in many systems), does not claim the "
            "two-dimensional landscape is exact, and does not claim "
            "polymorph selection is solved - that is a harder problem "
            "built on top of this one."
        ),
        "key_points": [
            "Crystal nucleation may proceed in one step (classical) or two (dense droplet first, crystal inside) - experiments see both.",
            "Classical nucleation theory predicts some rates well and misses others by orders of magnitude.",
            "The 1997 ten Wolde-Frenkel result showed density fluctuations near a hidden critical point can massively enhance nucleation.",
            "No theory yet predicts which pathway a given system will take.",
            "The Signature approach derives a pathway-selection rule on the density-order plane and the fluctuation test for it.",
        ],
        "citations": [CIT_WOLDE, CIT_KASHCHIEV, CIT_ATKINS],
    },
    {
        "key": "csp",
        "name": "Can We Predict Which Crystals a Molecule Will Form?",
        "group": "Deep",
        "ladder_rank": 14,
        "ladder_tier": "deep",
        "problem": (
            "Given only a molecule's structure, can we predict how it will "
            "pack into a crystal? In 1988 Nature editor John Maddox called "
            "this a scandal: it remained impossible to predict crystal "
            "structures from first principles. Crystal structure prediction "
            "(CSP) has since become a real computational discipline - "
            "blind tests show it can find the right structure among "
            "thousands of candidates - but polymorphism (same molecule, "
            "many crystal forms) still surprises the pharmaceutical "
            "industry, and the energy differences between forms are often "
            "smaller than the errors in our best calculations. The unsolved "
            "problem: reliable, routine prediction of all accessible "
            "crystal forms and their relative stability."
        ),
        "background": (
            "Maddox's 1988 editorial 'Crystals from first principles' "
            "declared it 'impossible to predict the structure of even the "
            "simplest crystalline solids from a knowledge of their chemical "
            "composition.' The statement became a rallying cry. Modern CSP "
            "works by generating thousands of candidate packings and "
            "ranking them by computed lattice energy - and in the "
            "Cambridge blind tests, the best methods now routinely place "
            "the experimental structure at or near the top. But the "
            "victories hide the difficulty: polymorph energy differences "
            "are often 1-2 kJ/mol, at the edge of density-functional "
            "accuracy; temperature and entropy (not just lattice energy) "
            "decide real stability; and industry keeps discovering new "
            "polymorphs of old drugs - the famous ritonavir case, where a "
            "new crystal form appeared and shut down manufacturing, "
            "remains the cautionary tale. CSP can now usually find the "
            "known forms; guaranteeing it has found ALL the forms is still "
            "beyond reach."
        ),
        "why_it_matters": (
            "A drug's crystal form controls its solubility, bioavailability, "
            "and patent life - a surprise polymorph can kill a product. The "
            "same holds for pigments, explosives, and organic electronics. "
            "Reliable CSP would let chemists screen solid forms on a "
            "computer before making them, saving years and fortunes, and "
            "would complete the loop from molecule to material."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the energy-landscape walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the polymorph landscape as a dense thicket of nearly "
            "degenerate minima and proposes the completeness test - a "
            "search protocol with a provable 'no more forms' criterion."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats CSP as a completeness "
            "problem and derives a stopping criterion for the search.\n\n"
            "ASSUMPTIONS: (1) Candidate packings are generated by "
            "symmetry-constrained random search plus evolutionary "
            "refinement. (2) Ranking uses dispersion-corrected "
            "density-functional energies plus harmonic free-energy "
            "corrections. (3) The search is complete when new candidates "
            "stop appearing in the low-energy window, measured by a "
            "coverage statistic.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Energy scale audit: "
            "compare typical polymorph energy gaps (1-2 kJ/mol) against "
            "method errors, showing why ranking is the hard part. Step 2 "
            "- Landscape density: estimate how the number of distinct "
            "minima grows with molecular flexibility - the search "
            "difficulty. Step 3 - Coverage statistic: define the "
            "discovery rate of new low-energy forms per thousand "
            "candidates; completeness is claimed when the rate falls "
            "below a threshold calibrated on systems with known full "
            "polymorph sets. Step 4 - Temperature promotion: re-rank the "
            "complete low-energy set by free energy at real "
            "temperatures, predicting the observable polymorphs.\n\n"
            "PROPOSED MECHANISM: the polymorph landscape is a dense "
            "thicket of nearly degenerate minima; reliable prediction "
            "equals complete search plus honest error bars on ranking.\n\n"
            "WHAT WOULD CONFIRM IT: blind-test molecules where the "
            "protocol's 'complete' set contains every experimentally "
            "found polymorph and no experiment later finds a missing "
            "stable form. WHAT WOULD KILL IT: a molecule where the "
            "coverage statistic declares completeness yet a new "
            "polymorph is later discovered in the searched energy "
            "window.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim current DFT "
            "accuracy is sufficient (it is the limiting factor), does "
            "not claim kinetics (which form nucleates first) is solved, "
            "and does not claim the protocol is cheap - only that "
            "completeness can be made measurable."
        ),
        "key_points": [
            "Maddox's 1988 'scandal': crystal structures could not be predicted from composition - a challenge the field took up.",
            "Modern CSP ranks thousands of candidate packings; blind tests show it usually finds known forms.",
            "Polymorph energy gaps (1-2 kJ/mol) sit at the edge of our best computational accuracy.",
            "The ritonavir case - a surprise polymorph halting drug production - shows what is at stake.",
            "The Signature approach makes search completeness measurable with a coverage stopping criterion.",
        ],
        "citations": [CIT_MADDOX, CIT_CLAYDEN, CIT_CRAMER],
    },
    {
        "key": "sei",
        "name": "What Is Happening Inside a Battery as It Charges?",
        "group": "Deep",
        "ladder_rank": 15,
        "ladder_tier": "deep",
        "problem": (
            "Every lithium-ion battery survives because of a film a few "
            "nanometers thick: the solid-electrolyte interphase (SEI), "
            "formed when electrolyte decomposes on the anode during the "
            "first charge. It must conduct lithium ions while blocking "
            "electrons - and nobody fully understands its structure, "
            "composition, or growth mechanism. It keeps growing slowly, "
            "consuming lithium and killing capacity; it behaves "
            "differently on graphite, silicon, and lithium metal; and "
            "lithium dendrites can pierce it and short the cell. The "
            "unsolved problem: the complete chemistry and physics of the "
            "SEI - what it is, how it grows, and how to engineer it."
        ),
        "background": (
            "Emanuel Peled identified the SEI in 1979 as the passivating "
            "layer that makes lithium batteries possible at all: without "
            "it, the electrolyte would reduce continuously on the anode. "
            "The SEI is a mosaic of inorganic crystals (lithium fluoride, "
            "lithium carbonate, lithium oxide) embedded in an organic "
            "polymer matrix - but the exact mosaic varies with electrolyte, "
            "additives, temperature, and cycling history, and it is "
            "notoriously hard to observe: it is nanometers thick, "
            "air-sensitive, and buried inside a sealed cell. Cryo-electron "
            "microscopy has recently imaged it at atomic resolution, "
            "revealing surprising order in what was assumed amorphous. "
            "Yet the growth law (why it never fully stops), the ion "
            "transport mechanism through the mosaic, and the link between "
            "SEI chemistry and dendrite penetration remain contested. "
            "Silicon anodes, which swell 300% on charging, crack the SEI "
            "repeatedly - the central obstacle to high-capacity anodes."
        ),
        "why_it_matters": (
            "Batteries are the bottleneck of the energy transition - "
            "electric vehicles, grid storage, portable electronics all "
            "wait on longer-lived, safer, cheaper cells. The SEI controls "
            "cycle life, safety, and fast-charging ability. Engineering it "
            "deliberately, instead of by additive trial and error, could "
            "unlock silicon anodes and lithium-metal batteries, roughly "
            "doubling energy density."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the mosaic-growth walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the SEI as a self-limiting mosaic whose growth law is "
            "set by electron tunneling through the film, and proposes the "
            "thickness-vs-time measurement that would prove or kill the "
            "tunneling limit."
        ),
        "sig_full": (
            LABEL + " The Signature approach models SEI growth as "
            "electron-tunneling-limited and derives the growth law test.\n\n"
            "ASSUMPTIONS: (1) The SEI grows by electrolyte reduction at "
            "the film surface, requiring electrons to cross the existing "
            "film. (2) Electron transport through the mosaic falls "
            "exponentially with thickness (tunneling or hopping). (3) "
            "Mechanical cracking (silicon swelling, lithium plating "
            "stress) resets local thickness to zero, restarting growth.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Growth law: with "
            "tunneling-limited electrons, film thickness grows as the "
            "logarithm of time - derive the log law and its prefactor "
            "from the tunneling decay length. Step 2 - Capacity ledger: "
            "convert the growth law into lithium consumed per cycle - "
            "the capacity-fade prediction. Step 3 - Mosaic transport: "
            "model lithium-ion conduction through grain boundaries of "
            "the inorganic mosaic vs the organic matrix, predicting "
            "which phase carries the current. Step 4 - Crack audit: add "
            "mechanical fracture events; each crack is a fresh growth "
            "site, explaining why silicon anodes fade fast.\n\n"
            "PROPOSED MECHANISM: the SEI is a tunneling-limited "
            "self-passivating mosaic; it never fully stops because "
            "tunneling never reaches zero and cracks keep resetting it.\n\n"
            "WHAT WOULD CONFIRM IT: thickness-vs-time measurements "
            "following the predicted logarithmic law with the "
            "tunneling-derived prefactor, and capacity fade matching "
            "the lithium-consumption ledger across electrolytes. WHAT "
            "WOULD KILL IT: growth that continues linearly long after "
            "the tunneling limit should have choked it, or an SEI that "
            "stops growing entirely despite ongoing cycling.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the mosaic "
            "composition is universal (it varies), does not claim "
            "dendrite penetration is solved, and does not claim "
            "artificial SEIs are designed yet - only the growth-law "
            "framework for designing them."
        ),
        "key_points": [
            "The SEI - a nanometer film from electrolyte decomposition - is what makes lithium-ion batteries possible, and its chemistry is still murky.",
            "It is a mosaic of inorganic crystals in an organic matrix, varying with every electrolyte and additive.",
            "It grows logarithmically (maybe), consuming lithium and fading capacity; silicon's 300% swelling cracks it repeatedly.",
            "Cryo-electron microscopy recently revealed unexpected atomic order in the film.",
            "The Signature approach derives the tunneling-limited growth law and the thickness-vs-time test.",
        ],
        "citations": [CIT_PELED, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "corrosion",
        "name": "How Does Rust Really Eat Metal?",
        "group": "Deep",
        "ladder_rank": 16,
        "ladder_tier": "deep",
        "problem": (
            "Corrosion costs the world trillions - roughly 3-4% of global "
            "GDP - yet predicting when and where a specific structure will "
            "corrode remains unreliable. The electrochemistry is textbook "
            "material: anodic dissolution here, cathodic reduction there. "
            "But real corrosion is localized and multiscale: pits initiate "
            "at invisible defects, cracks grow by stress-corrosion "
            "coupling, protective films break down stochastically, and "
            "microstructure decides everything. The unsolved problem: a "
            "predictive, multiscale theory linking atomic-scale film "
            "breakdown to engineering-scale failure."
        ),
        "background": (
            "Uhlig and Revie's classic text codified corrosion science: "
            "mixed-potential theory (the Evans diagram) predicts uniform "
            "corrosion rates beautifully. The trouble is that engineering "
            "failures are rarely uniform - they are pits, crevices, "
            "stress-corrosion cracks, and galvanic couples, all localized "
            "phenomena. Pitting initiates at sulfide inclusions or grain "
            "boundaries through film-breakdown events that are "
            "statistical in nature; once a pit starts, its chemistry "
            "acidifies and autocatalyzes. Stress-corrosion cracking couples "
            "mechanics and chemistry at a crack tip in ways still modeled "
            "semi-empirically. Modern tools - scanning electrochemical "
            "microscopy, atom-probe tomography of passive films - are "
            "finally resolving the initiation sites, but no model yet spans "
            "from a single chloride ion attacking a nanometer film to a "
            "bridge cable failing decades later."
        ),
        "why_it_matters": (
            "Corrosion destroys infrastructure, grounds aircraft, leaks "
            "pipelines, and limits the lifetime of every metal technology "
            "including implants and nuclear waste containers. A predictive "
            "multiscale theory would let engineers design for a specified "
            "lifetime instead of overbuilding by guesswork - saving "
            "trillions and preventing catastrophic failures."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the defect-to-failure walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models corrosion as a cascade - stochastic film breakdown at "
            "defects, autocatalytic pit chemistry, mechanics-coupled crack "
            "growth - and proposes the inclusion-mapping test that would "
            "predict pitting sites before they pit."
        ),
        "sig_full": (
            LABEL + " The Signature approach builds corrosion as a "
            "three-stage cascade and derives the pre-failure prediction "
            "test.\n\n"
            "ASSUMPTIONS: (1) Passive films are protective except at "
            "microstructural defects (inclusions, grain boundaries), where "
            "breakdown is a stochastic event with a measurable rate. (2) "
            "Once initiated, pit chemistry acidifies and autocatalyzes "
            "(the pit sustains itself). (3) Crack growth couples the pit "
            "chemistry to mechanical stress intensity at the tip.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Defect census: map "
            "inclusion size, spacing, and composition on a steel surface "
            "and compute each defect's film-breakdown probability per "
            "unit time in chloride solution. Step 2 - Initiation race: "
            "the first pit appears at the weakest defect - predict the "
            "time-to-first-pit distribution from the census. Step 3 - "
            "Autocatalysis check: model the pit's internal acidification "
            "and show the feedback that makes pits stable once started. "
            "Step 4 - Crack coupling: where stress is present, convert "
            "pit depth to stress intensity and predict the "
            "pit-to-crack transition.\n\n"
            "PROPOSED MECHANISM: corrosion failure is a cascade - "
            "defect statistics set initiation, autocatalytic chemistry "
            "sets pit stability, mechanics sets the final failure; each "
            "stage is predictable from the previous stage's output.\n\n"
            "WHAT WOULD CONFIRM IT: inclusion-mapped coupons whose "
            "measured time-to-first-pit and pit locations match the "
            "census prediction, and pit-to-crack transitions at the "
            "predicted stress intensities. WHAT WOULD KILL IT: pits "
            "initiating with no correlation to the mapped defect "
            "population, or initiation times that defy the statistical "
            "census.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim uniform corrosion "
            "needs this machinery (Evans diagrams already work there), "
            "does not claim all alloys follow the same defect statistics, "
            "and does not claim lifetime prediction is solved - only "
            "that the cascade makes it testable stage by stage."
        ),
        "key_points": [
            "Corrosion costs ~3-4% of global GDP, yet localized corrosion (pitting, cracking) resists prediction.",
            "Uniform corrosion is well described by mixed-potential theory; failures are almost never uniform.",
            "Pits initiate stochastically at microstructural defects, then autocatalyze through internal acidification.",
            "Stress-corrosion cracking couples pit chemistry to fracture mechanics at the crack tip.",
            "The Signature approach builds the defect-to-failure cascade and the inclusion-mapping prediction test.",
        ],
        "citations": [CIT_UHLIG, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "pfas",
        "name": "How Do We Destroy Forever Chemicals?",
        "group": "Deep",
        "ladder_rank": 17,
        "ladder_tier": "deep",
        "problem": (
            "Per- and polyfluoroalkyl substances (PFAS) - the 'forever "
            "chemicals' in nonstick coatings, firefighting foams, and "
            "countless products - now contaminate water supplies worldwide. "
            "The carbon-fluorine bond is among the strongest in chemistry, "
            "which is why PFAS survive heat, acids, and microbes for "
            "decades. Destroying them requires breaking those bonds "
            "completely: partial destruction just makes shorter PFAS that "
            "are still harmful. The unsolved problem: a cheap, scalable, "
            "complete mineralization method - turning PFAS fully into "
            "fluoride, carbon dioxide, and water - that works in real "
            "contaminated water, not just clean lab solutions."
        ),
        "background": (
            "PFAS were prized precisely for their indestructibility; that "
            "property became the crisis. Buck and colleagues' 2011 review "
            "catalogued the sprawling family - thousands of compounds - "
            "and their global spread. The C-F bond (around 485 kJ/mol) "
            "resists biological and most chemical attack; conventional "
            "water treatment does not touch them. Destruction methods "
            "exist in the lab: electrochemical oxidation, sonochemical "
            "pyrolysis, supercritical water oxidation, UV/sulfite "
            "reductive systems, and high-temperature incineration. Each "
            "has a catch: energy cost, incomplete defluorination (leaving "
            "shorter-chain PFAS), sensitivity to water matrix (real water "
            "has competing organics and salts), or the risk of forming "
            "other harmful byproducts. Recent work on low-temperature "
            "mineralization in polar aprotic solvents showed complete "
            "defluorination is chemically possible under mild conditions - "
            "but scaling any method to treat millions of liters of "
            "contaminated groundwater economically remains unsolved."
        ),
        "why_it_matters": (
            "PFAS exposure is linked to immune, thyroid, liver, and "
            "developmental effects, and contamination is effectively "
            "irreversible by natural processes. Communities near "
            "manufacturing sites and military bases live with it now. A "
            "scalable destruction technology is the difference between "
            "managing a permanent pollutant and actually eliminating it."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the bond-by-bond walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models PFAS destruction as a sequential defluorination ladder "
            "and proposes the fluorine-balance test that certifies complete "
            "mineralization in real water matrices."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats PFAS destruction as "
            "a bond-by-bond ledger and derives the certification test for "
            "completeness.\n\n"
            "ASSUMPTIONS: (1) Destruction proceeds by sequential C-F bond "
            "cleavage; each step has its own activation barrier, and "
            "partial sequences yield shorter PFAS. (2) Complete "
            "mineralization means every fluorine atom ends as fluoride "
            "ion - the fluorine mass balance must close. (3) Real water "
            "matrix (dissolved organics, chloride, carbonate) competes for "
            "the reactive species.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Bond ladder: list the "
            "C-F bond strengths along a representative PFAS (e.g., PFOA) "
            "and compute the energy each destruction method delivers per "
            "bond - the thermodynamic feasibility screen. Step 2 - "
            "Intermediate trap audit: identify the stable partial "
            "products each method can stall at, and their toxicity "
            "relative to the parent. Step 3 - Matrix penalty: estimate "
            "how competing scavengers in real water dilute the reactive "
            "species, scaling lab rates to field rates. Step 4 - "
            "Fluorine balance: the certification - measure total "
            "organofluorine in, fluoride out; mineralization is complete "
            "only when the balance closes with no missing organofluorine.\n\n"
            "PROPOSED MECHANISM: scalable destruction equals a method "
            "whose per-bond energy clears the whole ladder faster than "
            "intermediates escape, in the presence of matrix scavengers; "
            "the fluorine balance is the non-negotiable proof.\n\n"
            "WHAT WOULD CONFIRM IT: a pilot-scale system treating real "
            "contaminated groundwater with closed fluorine balance, "
            "energy cost per liter published, and no detectable "
            "organofluorine residuals. WHAT WOULD KILL IT: a method that "
            "closes the balance in clean water but systematically stalls "
            "at short-chain intermediates in real matrices.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim any current method "
            "is deployable at scale (none fully is), does not claim "
            "fluoride product is harmless at all concentrations, and does "
            "not claim destruction solves the source problem - stopping "
            "production matters as much as cleanup."
        ),
        "key_points": [
            "PFAS 'forever chemicals' resist destruction because the C-F bond (~485 kJ/mol) is among chemistry's strongest.",
            "Partial destruction is dangerous: it yields shorter-chain PFAS that remain harmful.",
            "Lab methods exist (electrochemical, sonochemical, supercritical water, UV/sulfite) but each has scaling catches.",
            "Complete mineralization must be certified by closing the fluorine mass balance - fluoride out equals organofluorine in.",
            "The Signature approach walks the bond-by-bond ladder and proposes the fluorine-balance certification test.",
        ],
        "citations": [CIT_BUCK, CIT_ATKINS, CIT_CLAYDEN],
    },
    {
        "key": "n2_fixation",
        "name": "How Do We Pull Nitrogen From the Air at Room Temperature?",
        "group": "Deep",
        "ladder_rank": 18,
        "ladder_tier": "deep",
        "problem": (
            "The air is 78% nitrogen, but the N-N triple bond (941 kJ/mol) "
            "makes it nearly inert. Humanity fixes nitrogen with the "
            "Haber-Bosch process - 400-500 C, 200 atmospheres, 1-2% of "
            "world energy - while soil bacteria do it at room temperature "
            "with the nitrogenase enzyme. The enzyme's mechanism, after "
            "decades of study, is still not fully mapped: the exact site "
            "of N2 binding on the FeMo cofactor and the sequence of "
            "hydrogenation steps remain debated. The unsolved problem has "
            "two faces: the complete nitrogenase mechanism, and a "
            "human-made catalyst that fixes nitrogen under mild conditions."
        ),
        "background": (
            "Smil's history documents how Haber-Bosch 'enriched the Earth': "
            "it feeds roughly half of humanity but devours fossil energy "
            "and emits CO2. Nature's alternative, nitrogenase, works at "
            "ambient temperature and pressure using the FeMo cofactor - a "
            "cluster of iron, molybdenum, sulfur, and carbon. Hoffman's "
            "2014 review synthesized decades of spectroscopy into the "
            "current mechanistic picture: N2 binds to the cofactor after "
            "accumulation of reducing equivalents, then is hydrogenated "
            "stepwise. But the precise binding site, the order of proton "
            "and electron delivery, and how the enzyme suppresses the "
            "competing hydrogen-evolution reaction are still contested. On "
            "the synthetic side, molecular catalysts that reduce N2 under "
            "mild conditions exist (Schrock, Nishibayashi systems) but "
            "with turnover numbers far from practical; electrochemical "
            "nitrogen reduction is plagued by hydrogen evolution winning "
            "the race. The gap between the enzyme and our best mimics "
            "measures exactly what we do not understand."
        ),
        "why_it_matters": (
            "Fertilizer from Haber-Bosch feeds billions but costs "
            "enormous energy and emissions. A mild-condition nitrogen "
            "fixation catalyst - especially an electrochemical one driven "
            "by renewable electricity - would decarbonize fertilizer, "
            "enable distributed production for small farms, and open new "
            "routes to nitrogen-containing chemicals without fossil heat."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the hydrogenation-ladder walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models nitrogenase as a proton-electron bookkeeping machine "
            "that outruns hydrogen evolution, and proposes the intermediate-"
            "trapping experiment that would map the full N2 reduction "
            "sequence."
        ),
        "sig_full": (
            LABEL + " The Signature approach audits nitrogenase's "
            "proton-electron bookkeeping and derives the selectivity rule "
            "a synthetic catalyst must satisfy.\n\n"
            "ASSUMPTIONS: (1) N2 binds to the FeMo cofactor only after "
            "the cluster accumulates multiple reducing equivalents (the "
            "Janus intermediate concept). (2) Reduction proceeds by "
            "alternating proton/electron delivery along either a distal "
            "or alternating hydrogenation path. (3) Hydrogen evolution is "
            "the ever-present competing reaction that any working system "
            "must suppress.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Energy ledger: write "
            "the full N2-to-2NH3 free-energy ladder and the H2-evolution "
            "ladder side by side; the catalyst must keep every N2 step "
            "below the H2 steps. Step 2 - Binding audit: compare the "
            "predicted N2 binding geometries on the cofactor and their "
            "spectroscopic signatures. Step 3 - Pathway race: compute the "
            "barriers for distal vs alternating hydrogenation and for H2 "
            "loss at each stage - the selectivity map. Step 4 - Mimic "
            "spec: translate the winning features (accumulation before "
            "binding, proton-gated electron delivery, H2 suppression) "
            "into design rules for a synthetic system.\n\n"
            "PROPOSED MECHANISM: nitrogenase wins by accumulating "
            "reducing power BEFORE binding N2, then delivering protons "
            "and electrons in a gated sequence that never gives hydrogen "
            "evolution an open lane.\n\n"
            "WHAT WOULD CONFIRM IT: trapping and spectroscopically "
            "identifying the predicted N2-bound and partially hydrogenated "
            "intermediates in the enzyme's cycle, with kinetics matching "
            "the ledger. WHAT WOULD KILL IT: an intermediate sequence "
            "that contradicts the accumulation-before-binding order, or a "
            "synthetic system that fixes N2 efficiently while violating "
            "the proposed design rules.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the mechanism is "
            "known (the binding site is still debated), does not claim a "
            "practical synthetic catalyst exists, and does not claim "
            "electrochemical NRR's selectivity problem is solved - only "
            "the ledger any solution must satisfy."
        ),
        "key_points": [
            "Haber-Bosch feeds half of humanity at 400-500 C and 200 atm; nitrogenase does it at room temperature - the gap is the mystery.",
            "The FeMo cofactor's N2 binding site and hydrogenation sequence remain debated after decades of spectroscopy.",
            "Hydrogen evolution is the constant competitor that any nitrogen-reduction system must outrun.",
            "Synthetic N2-reduction catalysts exist but with turnovers far from practical.",
            "The Signature approach writes the competing energy ledgers and derives the selectivity rules a working mimic must satisfy.",
        ],
        "citations": [CIT_HOFFMAN, CIT_SMIL, CIT_HOUSECROFT],
    },
    {
        "key": "co2_fuel",
        "name": "How Do We Turn Carbon Dioxide Back Into Fuel?",
        "group": "Deep",
        "ladder_rank": 19,
        "ladder_tier": "deep",
        "problem": (
            "Reducing CO2 to fuels with renewable electricity would close "
            "the carbon loop: burn fuel, recapture the CO2, remake the "
            "fuel. But CO2 is a stubborn molecule, and its reduction "
            "competes with hydrogen evolution at nearly every catalyst. "
            "Copper is the only metal that makes significant amounts of "
            "multi-carbon products (ethylene, ethanol), yet its selectivity "
            "is poor and its active sites under reaction conditions are "
            "still debated - the surface restructures as it works. The "
            "unsolved problem: a catalyst that reduces CO2 selectively, "
            "efficiently, and durably to a chosen fuel product."
        ),
        "background": (
            "Lewis and Nocera's 2006 'Powering the planet' framed solar "
            "fuels as the central chemical challenge of energy. "
            "Electrochemical CO2 reduction has since become a major field: "
            "gold and silver make CO selectively, tin makes formate, but "
            "only copper makes C2+ products - the valuable fuels - and it "
            "makes a messy mixture of them. The selectivity problem is "
            "mechanistic: the branching between products is decided by "
            "adsorbed intermediates (*CO, *CHO, *OCCO) whose binding "
            "energies scale together (the scaling relations), making it "
            "hard to favor one path without favoring others. Operando "
            "spectroscopy keeps showing that copper's surface under "
            "reaction conditions is not the pristine crystal of the "
            "textbook - it reconstructs, oxidizes partially, and hosts "
            "grain boundaries that may be the true active sites. "
            "Scaling-relation-breaking catalyst designs (tandem, alloy, "
            "molecular) are the field's great hope, but none has yet "
            "delivered a durable, selective, efficient device."
        ),
        "why_it_matters": (
            "Aviation, shipping, and heavy industry cannot easily run on "
            "batteries - they need dense chemical fuels. CO2-to-fuels "
            "closes the loop without new fossil carbon, turning waste "
            "into feedstock. Selective, durable catalysts are the missing "
            "piece between renewable electricity and carbon-neutral "
            "liquid fuels."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the intermediate-branching walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models product selectivity as a branching ratio set by "
            "intermediate binding energies, and proposes the tandem-"
            "catalyst design that breaks the scaling relations binding "
            "copper's selectivity."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats selectivity as a "
            "branching problem on the intermediate energy landscape and "
            "derives the scaling-breaking design.\n\n"
            "ASSUMPTIONS: (1) Product distribution is set by the relative "
            "binding energies of key intermediates (*CO, *CHO, *OCCO) on "
            "the active sites. (2) On pure metals these binding energies "
            "scale together, locking in copper's messy mixture. (3) The "
            "true active site under operation is a restructured surface "
            "(grain boundaries, partial oxidation), not the pristine "
            "crystal.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Branching map: write "
            "the reaction network from CO2 to each product and identify "
            "the selectivity-determining intermediate at each fork. Step "
            "2 - Scaling audit: show how *CO vs *CHO binding scales on "
            "pure metals, proving why single metals cannot isolate one "
            "product. Step 3 - Break the scaling: design a tandem site - "
            "one component makes CO, a neighboring different site "
            "couples CO - so the two key bindings are tuned "
            "independently. Step 4 - Operando check: predict the "
            "spectroscopic signature of the working tandem site vs the "
            "restructured-copper site.\n\n"
            "PROPOSED MECHANISM: selectivity equals independent control "
            "of the branching intermediates' binding energies; tandem "
            "sites achieve what no single metal can because they break "
            "the scaling relations.\n\n"
            "WHAT WOULD CONFIRM IT: a tandem catalyst showing single-"
            "product selectivity (>80% faradaic efficiency to one C2+ "
            "product) sustained over hundreds of hours, with operando "
            "spectroscopy confirming the designed dual-site mechanism. "
            "WHAT WOULD KILL IT: a single-metal catalyst achieving the "
            "same selectivity (scaling was not the binding constraint), "
            "or tandem systems that always degrade to copper-like "
            "mixtures.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim such a catalyst "
            "exists yet, does not claim copper's active site is settled, "
            "and does not claim device-level economics work - only the "
            "mechanistic design rule."
        ),
        "key_points": [
            "CO2 reduction to fuels would close the carbon loop, but hydrogen evolution competes at every catalyst.",
            "Only copper makes multi-carbon products, as a messy mixture - its working surface restructures and its true active sites are debated.",
            "Scaling relations lock intermediate binding energies together on pure metals, capping selectivity.",
            "Tandem and alloy designs aim to break the scaling relations; none has yet delivered a durable selective device.",
            "The Signature approach maps the branching intermediates and derives the tandem design rule.",
        ],
        "citations": [CIT_LEWIS, CIT_SOMORJAI, CIT_ATKINS],
    },
    {
        "key": "hydrogen_storage",
        "name": "How Do We Store Hydrogen Safely and Densely?",
        "group": "Deep",
        "ladder_rank": 20,
        "ladder_tier": "deep",
        "problem": (
            "Hydrogen is the lightest element and the most diffuse fuel: a "
            "kilogram holds great energy, but a liter of hydrogen gas at "
            "ambient conditions holds almost none. Storing it densely "
            "enough for vehicles means compressing to 700 atmospheres, "
            "liquefying at -253 C, or packing it into a solid material - "
            "and each route has a fundamental catch. Solid-state storage "
            "(metal hydrides, complex hydrides, adsorbents) trades "
            "capacity against the temperature needed to release the "
            "hydrogen: materials that hold a lot will not let go without "
            "strong heating. The unsolved problem: a storage material with "
            "high gravimetric AND volumetric density that loads and "
            "unloads near ambient conditions, reversibly, thousands of "
            "times."
        ),
        "background": (
            "Schlapbach and Zuettel's 2001 Nature review set the targets "
            "that still govern the field: a practical store needs roughly "
            "5-7 weight percent hydrogen and fast, reversible cycling near "
            "room temperature. The fundamental tension is thermodynamic: "
            "strong binding gives high capacity but requires high "
            "temperature to release; weak binding (physisorption in porous "
            "materials) works only when cold. Metal hydrides like LaNi5 "
            "cycle beautifully but are heavy; magnesium hydride holds 7.6 "
            "wt% but needs ~300 C; complex hydrides (alanates, borohydrides) "
            "hold even more but suffer poor reversibility; metal-organic "
            "frameworks adsorb impressively at 77 K and disappoint at room "
            "temperature. Nanoconfinement, catalysts, and destabilized "
            "hydride mixtures have chipped at the trade-off without "
            "breaking it. After decades, no solid-state material meets all "
            "targets simultaneously - which is why hydrogen vehicles still "
            "use 700-bar carbon-fiber tanks."
        ),
        "why_it_matters": (
            "Hydrogen is the leading candidate for decarbonizing "
            "steel, chemicals, heavy transport, and seasonal energy "
            "storage - all sectors batteries cannot reach. Storage is the "
            "bottleneck: solve it and hydrogen becomes a practical "
            "everywhere-fuel; leave it unsolved and hydrogen stays "
            "confined to niches with expensive tanks."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the binding-energy walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models storage as a thermodynamic window - binding must sit "
            "between 27 and 33 kJ/mol - and proposes the destabilized-"
            "mixture design that tunes real materials into the window."
        ),
        "sig_full": (
            LABEL + " The Signature approach reduces hydrogen storage to "
            "a thermodynamic window and derives the tuning strategy.\n\n"
            "ASSUMPTIONS: (1) Reversible near-ambient storage requires the "
            "hydrogen binding enthalpy to sit in a window around 27-33 "
            "kJ/mol H2: weaker will not hold it, stronger will not release "
            "it. (2) Gravimetric and volumetric density, kinetics, and "
            "cycle life are constraints on top of the window, not "
            "substitutes for it. (3) Destabilization - mixing two "
            "hydrides so their reaction products are stabilized - can "
            "shift effective thermodynamics into the window.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Window derivation: "
            "from the van't Hoff relation, compute the enthalpy range "
            "giving 1-10 bar equilibrium pressure at room temperature - "
            "the non-negotiable window. Step 2 - Material audit: place "
            "the known families (intermetallics, MgH2, alanates, "
            "borohydrides, MOFs) on the enthalpy-vs-capacity map and "
            "show each family's miss. Step 3 - Destabilization design: "
            "for an over-stable hydride, propose a reaction partner "
            "that stabilizes the dehydrogenated state, computing the "
            "shifted effective enthalpy. Step 4 - Kinetic gate: check "
            "that the tuned system also passes a kinetic screen - "
            "catalysts or nanoconfinement to keep rates practical.\n\n"
            "PROPOSED MECHANISM: practical storage equals a material "
            "tuned into the 27-33 kJ/mol window with kinetics unlocked; "
            "destabilized mixtures are the systematic route because "
            "single compounds rarely land in the window by luck.\n\n"
            "WHAT WOULD CONFIRM IT: a destabilized mixture demonstrating "
            ">5 wt% reversible capacity, 1-10 bar plateau at room "
            "temperature, and >1000 cycles with a published pressure-"
            "composition isotherm. WHAT WOULD KILL IT: a material "
            "meeting all targets far outside the window (the window "
            "theory is wrong), or proof that destabilization always "
            "wrecks reversibility.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim such a material "
            "exists, does not claim thermodynamics is the only barrier "
            "(kinetics and heat management are real), and does not claim "
            "700-bar tanks are obsolete - only the design map for "
            "replacing them."
        ),
        "key_points": [
            "Hydrogen's energy per kilogram is superb; per liter at ambient conditions it is nearly nothing - storage is the bottleneck.",
            "The thermodynamic trap: strong binding holds hydrogen but will not release it; weak binding works only when cold.",
            "Reversible near-ambient storage needs binding enthalpies in a narrow window around 27-33 kJ/mol.",
            "No solid-state material yet meets capacity, window, kinetics, and cycle-life targets simultaneously.",
            "The Signature approach derives the window from the van't Hoff relation and proposes destabilized-mixture tuning.",
        ],
        "citations": [CIT_SCHLAPBACH, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "active_sites",
        "name": "How Do Catalysts Really Work on Surfaces?",
        "group": "Deep",
        "ladder_rank": 21,
        "ladder_tier": "deep",
        "problem": (
            "Heterogeneous catalysts - solids that speed reactions of "
            "gases and liquids on their surfaces - make most of the "
            "world's chemicals. Yet for many industrial catalysts we "
            "still do not know the true active site: the surface under "
            "reaction conditions reconstructs, oxidizes, covers itself in "
            "intermediates, and the sites that actually do the chemistry "
            "may be rare defects, step edges, or dynamic ensembles that "
            "exist only while working. The unsolved problem: identifying "
            "the working active site, counting it, and watching it "
            "operate - for real catalysts under real conditions."
        ),
        "background": (
            "The Sabatier principle (1912) gave the field its compass: "
            "the best catalyst binds intermediates neither too weakly nor "
            "too strongly - the volcano plot, with activity peaking at "
            "intermediate binding. Somorjai's surface science showed that "
            "crystal face, steps, and kinks change activity dramatically. "
            "But the 'pressure gap' and 'materials gap' haunted the field "
            "for decades: pristine single crystals in ultrahigh vacuum "
            "are not industrial catalysts in hot, high-pressure gas. "
            "Modern operando spectroscopy - watching catalysts while they "
            "work - keeps revealing that surfaces restructure: copper "
            "oxidizes partially during CO2 reduction, platinum surfaces "
            "roughen during CO oxidation, and 'single-atom' catalysts may "
            "agglomerate or, conversely, nanoparticles may disperse into "
            "atoms under reaction conditions. Counting active sites "
            "(turnover frequency's denominator) remains one of the "
            "field's embarrassments: reported rates often cannot be "
            "compared because nobody knows how many sites were working."
        ),
        "why_it_matters": (
            "Catalysts enable fertilizer, fuels, plastics, and pollution "
            "control - catalysis touches the majority of manufactured "
            "goods. Knowing the true active site lets us make more of it "
            "and less of the inert bulk: less platinum in fuel cells, less "
            "rhodium in converters, cheaper catalysts for green chemistry. "
            "It converts catalyst development from screening thousands of "
            "formulations to designing the site directly."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the site-counting walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the working surface as a dynamic ensemble and proposes "
            "the poison-titration-plus-operando protocol that identifies "
            "and counts the true active sites."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the active site as a "
            "working-state property and derives the protocol to find and "
            "count it.\n\n"
            "ASSUMPTIONS: (1) The working surface differs from the "
            "as-prepared surface: adsorbates, partial oxidation, and "
            "restructuring create the true sites. (2) Only a fraction of "
            "surface atoms are active; the rest are spectators. (3) A "
            "site's identity is proven by correlating its spectroscopic "
            "signature with activity across conditions.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Volcano baseline: "
            "compute the Sabatier volcano for the reaction to know what "
            "binding strength the ideal site needs. Step 2 - Candidate "
            "census: enumerate candidate sites (terraces, steps, kinks, "
            "defects, single atoms, interfaces) and their predicted "
            "binding energies. Step 3 - Operando correlation: track each "
            "candidate's spectroscopic signature while varying conditions "
            "and correlate signature intensity with measured rate - the "
            "true site's signal moves with the rate. Step 4 - Poison "
            "titration: selectively poison candidate sites and count how "
            "many poison molecules kill the rate - the active-site count.\n\n"
            "PROPOSED MECHANISM: the active site is the surface "
            "configuration whose population tracks the reaction rate "
            "under operando conditions; everything else is spectator; the "
            "poison titration counts it.\n\n"
            "WHAT WOULD CONFIRM IT: a catalyst where operando "
            "spectroscopy plus poison titration converge on one site "
            "type, and synthesizing more of that site (by faceting, "
            "defect engineering) raises the rate proportionally. WHAT "
            "WOULD KILL IT: rates that track no single site's "
            "population, or poison titrations that kill the rate without "
            "a matching site - implying delocalized or collective "
            "activity.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim every catalyst "
            "has one site type (ensembles are real), does not claim "
            "operando techniques see everything, and does not claim the "
            "pressure gap is closed - only the protocol for closing it "
            "site by site."
        ),
        "key_points": [
            "Industrial catalysts work, but their true active sites under reaction conditions are often unknown - surfaces restructure as they work.",
            "The Sabatier volcano principle sets the target binding strength; the question is which surface atoms achieve it.",
            "Operando spectroscopy keeps revealing working surfaces different from textbook crystals.",
            "Counting active sites remains an embarrassment: rates often cannot be compared across studies.",
            "The Signature approach proposes the operando-correlation plus poison-titration protocol to identify and count true sites.",
        ],
        "citations": [CIT_SOMORJAI, CIT_NORSKOV, CIT_ATKINS],
    },
    {
        "key": "catalyst_design",
        "name": "How Do We Design a Catalyst From Scratch?",
        "group": "Deep",
        "ladder_rank": 22,
        "ladder_tier": "deep",
        "problem": (
            "Catalyst discovery is still largely Edisonian: make hundreds "
            "of formulations, test them, keep the winner. Computational "
            "catalyst design promises the opposite - specify the reaction, "
            "compute the ideal active site, then synthesize it. The "
            "descriptor approach (Norskov and colleagues) made this real "
            "for some reactions: one number, like an adsorption energy, "
            "predicts activity across metals. But extending it to complex "
            "reactions, to oxides and single atoms, to selectivity (not "
            "just activity), and to stability under reaction conditions "
            "remains unsolved. The unsolved problem: a general, reliable "
            "computational design loop from reaction to working catalyst."
        ),
        "background": (
            "Norskov's 2009 Nature Chemistry paper, 'Towards the "
            "computational design of solid catalysts,' crystallized the "
            "descriptor paradigm: because intermediate binding energies "
            "scale together, a single descriptor (e.g., *OH binding for "
            "oxygen reduction) predicts where a material sits on the "
            "volcano - and which undiscovered materials should sit at the "
            "top. Successes followed: new ammonia-synthesis and "
            "oxygen-reduction catalysts were computationally proposed and "
            "experimentally confirmed. But the paradigm strains at "
            "complexity: multi-step reactions need multiple descriptors; "
            "selectivity (which product) is harder than activity (how "
            "fast); oxides, carbides, and single-atom sites obey different "
            "scaling; and a computationally perfect site is worthless if "
            "it sinters, poisons, or reconstructs in the reactor. Machine "
            "learning now accelerates the screening, but ML models inherit "
            "the training data's limits - they interpolate brilliantly "
            "and extrapolate dangerously. The design loop exists in "
            "prototype; as a general engineering discipline it does not "
            "yet exist."
        ),
        "why_it_matters": (
            "Every green-chemistry dream - CO2 to fuels, nitrogen to "
            "fertilizer at mild conditions, plastic waste back to monomer - "
            "is a catalyst design problem. A reliable design loop would "
            "compress decades of trial-and-error into computation, "
            "deliver the catalysts the energy transition needs, and cut "
            "the precious-metal content of existing processes."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the descriptor-funnel walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models catalyst design as a four-gate funnel - activity, "
            "selectivity, stability, synthesizability - and proposes the "
            "closed-loop protocol where every computational prediction "
            "earns its keep experimentally."
        ),
        "sig_full": (
            LABEL + " The Signature approach builds catalyst design as a "
            "four-gate funnel and derives the closed-loop protocol.\n\n"
            "ASSUMPTIONS: (1) A descriptor (or small descriptor set) "
            "predicts activity via scaling relations for the reaction "
            "class. (2) Selectivity, stability, and synthesizability are "
            "separate gates - passing activity does not imply passing "
            "the rest. (3) Computational predictions must be tested in "
            "closed loop; untested predictions do not count as designs.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Activity gate: "
            "compute the descriptor volcano and list the materials at "
            "its top - the activity shortlist. Step 2 - Selectivity "
            "gate: for the shortlist, compute the branching barriers to "
            "unwanted products; discard materials that are fast but "
            "indiscriminate. Step 3 - Stability gate: compute "
            "segregation, oxidation, and sintering tendencies under "
            "reaction conditions; discard beautiful sites that will not "
            "survive. Step 4 - Synthesizability and loop closure: rank "
            "survivors by synthetic accessibility, make the top three, "
            "test under realistic conditions, and feed the results back "
            "to correct the descriptors.\n\n"
            "PROPOSED MECHANISM: reliable design equals the four-gate "
            "funnel run in closed loop; most 'designed' catalysts fail "
            "because they were only pushed through gate one.\n\n"
            "WHAT WOULD CONFIRM IT: a catalyst that passes all four "
            "gates computationally and then works as predicted in the "
            "reactor - with the loop's corrections measurably improving "
            "the next design round. WHAT WOULD KILL IT: systematic "
            "failure at gate three (stability) despite passing gates "
            "one and two - implying the working-state problem defeats "
            "descriptor design in general.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim descriptors work "
            "for all reactions (they do not), does not claim ML "
            "extrapolation is trustworthy, and does not claim the loop "
            "is fast or cheap - only that it is the honest structure of "
            "a design discipline."
        ),
        "key_points": [
            "Catalyst discovery is still mostly trial and error; computational design promises the reverse.",
            "The descriptor paradigm (Norskov) predicts activity from a single binding energy via scaling relations - with real successes.",
            "It strains at selectivity, at oxides and single atoms, and at stability under reaction conditions.",
            "Machine learning accelerates screening but extrapolates dangerously beyond its training data.",
            "The Signature approach builds the four-gate funnel (activity, selectivity, stability, synthesizability) run in closed loop.",
        ],
        "citations": [CIT_NORSKOV, CIT_SOMORJAI, CIT_CRAMER],
    },
    {
        "key": "isotope",
        "name": "How Do We Separate Isotopes Cheaply?",
        "group": "Deep",
        "ladder_rank": 23,
        "ladder_tier": "deep",
        "problem": (
            "Isotopes of an element are chemically nearly identical - "
            "separating them means exploiting tiny differences in mass, "
            "diffusion, or spectra. The world needs separated isotopes: "
            "enriched uranium and lithium for energy, deuterium for "
            "reactors and science, medical isotopes for diagnosis and "
            "therapy, stable isotopes for tracers. Yet separation remains "
            "expensive and energy-hungry: gaseous diffusion and "
            "centrifuges for uranium, the Girdler sulfide process for "
            "heavy water. The unsolved problem: a general, cheap, "
            "low-energy isotope separation method that works beyond the "
            "few isotopes with established industrial processes."
        ),
        "background": (
            "Benedict's Nuclear Chemical Engineering codified the "
            "separation science: the key number is the single-stage "
            "separation factor, usually barely above 1 (1.004 for "
            "gaseous diffusion of uranium), so thousands of stages in "
            "cascade are needed. Centrifuges improved the factor to ~1.3 "
            "per stage but remain capital-intensive precision machines. "
            "Laser isotope separation (AVLIS/MLIS) promised single-step "
            "selectivity by tuning lasers to one isotope's spectral "
            "lines - demonstrated for uranium and lithium, never fully "
            "commercialized. Chemical exchange methods exploit tiny "
            "equilibrium isotope effects. Each success is bespoke: the "
            "method that enriches lithium does not enrich carbon. No "
            "universal low-energy separator exists, and for many "
            "isotopes (including medically valuable ones) supply depends "
            "on aging reactors and fragile supply chains rather than on "
            "a clean separation technology."
        ),
        "why_it_matters": (
            "Medical isotopes diagnose and treat cancer; enriched lithium "
            "and deuterium serve fusion and fission; stable-isotope "
            "tracers map metabolism and climate. Cheap separation would "
            "secure medical supply chains, enable new reactor designs, "
            "and open isotope-enabled science now priced out of reach. "
            "It is also a nonproliferation-relevant technology, which is "
            "partly why progress is slow and guarded."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the cascade walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models separation cost as a cascade of small factors and "
            "proposes the selectivity-vs-throughput screen that would "
            "identify a genuinely general low-energy method."
        ),
        "sig_full": (
            LABEL + " The Signature approach reduces isotope separation "
            "to cascade economics and derives the screen for a general "
            "method.\n\n"
            "ASSUMPTIONS: (1) Any method is characterized by its "
            "single-stage separation factor alpha and its throughput per "
            "unit energy. (2) Total cost scales with the number of "
            "stages (set by alpha) times the per-stage energy. (3) A "
            "'general' method must work for elements across the periodic "
            "table, not one bespoke case.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Cascade math: from "
            "alpha, compute the stages needed for a target enrichment "
            "(e.g., natural to 90%) - showing why alpha=1.004 needs "
            "thousands of stages and alpha=1.3 needs tens. Step 2 - "
            "Method audit: place diffusion, centrifuge, laser, chemical "
            "exchange, and emerging methods (membranes, quantum sieving) "
            "on the alpha-vs-energy map. Step 3 - Generality test: "
            "score each method on how many elements it can address - "
            "the bespoke penalty. Step 4 - Screen spec: define the "
            "target zone (alpha, energy, generality) a new method must "
            "hit to displace incumbents, and the experiment that "
            "measures it.\n\n"
            "PROPOSED MECHANISM: separation cost is cascade economics; "
            "the winning general method is the one that maximizes "
            "alpha-per-joule across many elements - likely a "
            "spectral or quantum-sieving method, not a mechanical one.\n\n"
            "WHAT WOULD CONFIRM IT: a new method demonstrating "
            "alpha > 1.5 at low energy on three chemically unrelated "
            "elements, with a published cost-per-separative-work-unit "
            "below centrifuge. WHAT WOULD KILL IT: proof that "
            "thermodynamics caps practical alpha-per-joule near "
            "current methods for all approaches - i.e., the bespoke "
            "era is permanent.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim laser "
            "separation will commercialize (history counsels caution), "
            "does not claim any specific emerging method wins, and "
            "does not ignore the nonproliferation dimension - a "
            "general cheap separator has security implications that "
            "constrain deployment."
        ),
        "key_points": [
            "Isotopes are chemically nearly identical; separation exploits tiny mass, diffusion, or spectral differences.",
            "Single-stage separation factors are barely above 1, so thousands of cascade stages are needed - the cost driver.",
            "Each industrial success is bespoke: uranium centrifuges, heavy-water exchange; no general method exists.",
            "Laser isotope separation promised single-step selectivity but never fully commercialized.",
            "The Signature approach maps methods on alpha-vs-energy and defines the target zone a general method must hit.",
        ],
        "citations": [CIT_BENEDICT, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "molecular_machines",
        "name": "How Do Molecular Machines Move on Purpose?",
        "group": "Frontier",
        "ladder_rank": 24,
        "ladder_tier": "frontier",
        "problem": (
            "Living cells run on molecular machines - kinesin walks along "
            "microtubules carrying cargo, ATP synthase spins like a "
            "turbine. Synthetic chemists now build molecular motors, "
            "shuttles, and rotaxanes. But at the molecular scale there is "
            "no inertia and Brownian motion batters everything: how does "
            "directed motion emerge from random thermal kicks? The "
            "unsolved problem: the general design principles that convert "
            "random fluctuations into useful directed work at the "
            "nanoscale - and how close synthetic machines can come to "
            "biological efficiency."
        ),
        "background": (
            "At the nanoscale, water feels like molasses and thermal noise "
            "dominates - Feynman's famous observation that 'there's plenty "
            "of room at the bottom' came with the warning that the rules "
            "are different there. Biology solved it: kinesin takes 8-nm "
            "steps along microtubules, one ATP per step, with remarkable "
            "efficiency; ATP synthase rotates at ~100 revolutions per "
            "second. The 2016 Nobel Prize recognized Sauvage, Stoddart, "
            "and Feringa for synthetic molecular machines - catenanes, "
            "rotaxanes, and light-driven rotary motors. Kay, Leigh, and "
            "Zerbetto's 2007 review mapped the mechanisms: Brownian "
            "ratchets, where asymmetric energy landscapes rectify random "
            "motion, and power strokes, where a chemical step drives a "
            "conformational change. Yet the efficiency gap between "
            "biological and synthetic machines remains large, and the "
            "general theory of how to design a ratchet for a given task - "
            "how much asymmetry, how fast the switching, how to beat "
            "thermal noise - is still being written."
        ),
        "why_it_matters": (
            "Molecular machines are the hypothetical assemblers of "
            "nanotechnology: drug-delivery vehicles that walk to tumors, "
            "pumps that desalinate water molecule by molecule, materials "
            "that repair themselves. The design principles are also the "
            "key to understanding every motor protein in the cell - and "
            "their failures in disease."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the ratchet walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models directed motion as a flashing Brownian ratchet and "
            "derives the asymmetry-switching recipe that maximizes "
            "efficiency against thermal noise."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the molecular machine "
            "as a flashing ratchet and derives the efficiency recipe.\n\n"
            "ASSUMPTIONS: (1) At the nanoscale, motion is overdamped: no "
            "inertia, only thermal kicks and the energy landscape. (2) "
            "Directed motion requires breaking symmetry - an asymmetric "
            "landscape plus energy input (chemical or light) that flashes "
            "it on and off. (3) Efficiency is useful work out divided by "
            "free energy in per cycle.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Ratchet sketch: model "
            "a particle on a sawtooth potential that flashes between on "
            "and off; compute the net drift from asymmetric diffusion - "
            "the rectification mechanism. Step 2 - Switching audit: vary "
            "the flash rate; too slow wastes time, too fast outruns "
            "diffusion - find the optimal rate. Step 3 - Load test: add "
            "an opposing force (cargo) and compute the stall force and "
            "the efficiency vs load curve. Step 4 - Biology benchmark: "
            "place kinesin and Feringa's motor on the same efficiency "
            "map and identify what the synthetic motor lacks (gating, "
            "tight coupling).\n\n"
            "PROPOSED MECHANISM: directed nanoscale motion equals an "
            "asymmetric landscape flashed at the diffusion-matched rate; "
            "efficiency is lost wherever the machine slips (futile "
            "cycles) or fights its own symmetry.\n\n"
            "WHAT WOULD CONFIRM IT: a synthetic motor whose measured "
            "efficiency-vs-flash-rate curve matches the predicted "
            "optimum, and a redesigned motor closing half the gap to "
            "kinesin by the recipe. WHAT WOULD KILL IT: motors whose "
            "performance is insensitive to landscape asymmetry - "
            "implying a different principle dominates.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the ratchet "
            "picture covers all biological motors (power strokes are "
            "real too), does not claim synthetic motors will match "
            "biology soon, and does not claim a universal assembler is "
            "near - only the design map."
        ),
        "key_points": [
            "At the nanoscale there is no inertia - thermal kicks dominate, so directed motion must be rectified from randomness.",
            "Biology's machines (kinesin, ATP synthase) are far more efficient than synthetic ones; the gap measures our ignorance.",
            "Two mechanisms: Brownian ratchets (rectified diffusion) and power strokes (driven conformational change).",
            "The 2016 Nobel Prize recognized synthetic molecular machines; the design theory is still being written.",
            "The Signature approach derives the flashing-ratchet efficiency recipe and the biology benchmark.",
        ],
        "citations": [CIT_KAY, CIT_ATKINS, CIT_CLAYDEN],
    },
    {
        "key": "organic_charge",
        "name": "How Does Charge Move Through Plastic Electronics?",
        "group": "Frontier",
        "ladder_rank": 25,
        "ladder_tier": "frontier",
        "problem": (
            "Organic semiconductors - carbon-based plastics that conduct - "
            "enable flexible displays, printed solar cells, and wearable "
            "sensors. But how charge actually moves through them is "
            "debated: like a wave in a crystal band, or like a frog "
            "hopping between localized sites? The measured mobilities "
            "fall in the awkward middle, decreasing with temperature in "
            "some materials (band-like) and increasing in others "
            "(hopping-like). The unsolved problem: the true charge-"
            "transport mechanism in organic semiconductors, and how to "
            "design molecules for high mobility."
        ),
        "background": (
            "In silicon, charge moves as delocalized waves in bands - the "
            "textbook picture. In disordered organics, the early picture "
            "was hopping: charges localized on molecules, jumping with "
            "thermal help (Marcus theory). Then ultrapure organic crystals "
            "(rubrene, pentacene) showed mobilities above 10 cm^2/Vs that "
            "DECREASE with heating - the band-transport signature - in "
            "materials with no business behaving like silicon. Coropceanu "
            "and colleagues' 2007 review framed the paradox: neither pure "
            "band nor pure hopping fits. The emerging picture is "
            "transient localization: thermal molecular motions constantly "
            "scramble the electronic couplings, so a charge surfs a "
            "flickering landscape - delocalized over a few molecules at "
            "any instant, hopping in effect over time. But turning this "
            "into quantitative mobility predictions for new molecules, "
            "and disentangling the roles of static disorder vs dynamic "
            "disorder, remains unfinished."
        ),
        "why_it_matters": (
            "Printed, flexible, biocompatible electronics - solar cells "
            "you print like newspaper, sensors woven into clothing, "
            "medical patches - all depend on organic semiconductors. "
            "Higher mobility means faster transistors and more efficient "
            "solar cells. A predictive transport theory would let chemists "
            "design high-mobility molecules instead of screening them."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the flickering-landscape walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models transport as transient localization on a thermally "
            "flickering coupling landscape, and proposes the temperature-"
            "and disorder-dependence test that separates the mechanisms."
        ),
        "sig_full": (
            LABEL + " The Signature approach models the charge as surfing "
            "a flickering landscape and derives the mechanism-separating "
            "test.\n\n"
            "ASSUMPTIONS: (1) Electronic couplings between molecules "
            "fluctuate on the timescale of molecular vibrations "
            "(dynamic disorder). (2) Static disorder (impurities, grain "
            "boundaries) adds a frozen component. (3) The charge is "
            "transiently delocalized over a coherence length set by the "
            "ratio of coupling to disorder.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Limit audit: compute "
            "the mobility predicted by pure band theory and pure Marcus "
            "hopping for a model crystal - showing the measured values "
            "fall between. Step 2 - Flicker model: simulate a charge on "
            "a lattice with time-fluctuating couplings; extract the "
            "effective mobility and its temperature dependence. Step 3 - "
            "Disorder split: predict how mobility vs temperature differs "
            "when static disorder dominates (activated, hopping-like) vs "
            "dynamic disorder (band-like decrease). Step 4 - Molecular "
            "design rule: derive what molecular features maximize the "
            "coherence length - rigid backbones, strong pi-stacking, "
            "low-frequency vibrations suppressed.\n\n"
            "PROPOSED MECHANISM: organic charge transport is transient "
            "localization - delocalized over a flickering few molecules, "
            "hopping in the long-time average; the band-vs-hop debate "
            "dissolves into a coherence-length question.\n\n"
            "WHAT WOULD CONFIRM IT: a material series where measured "
            "mobility-temperature curves and coherence lengths (from "
            "spectroscopy) match the flicker-model predictions, and a "
            "molecule designed by the rule achieving record mobility. "
            "WHAT WOULD KILL IT: high-mobility organics with no "
            "detectable dynamic disorder, or mobilities that follow pure "
            "Marcus hopping with no band-like regime.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the debate is "
            "over (it is not), does not claim quantitative prediction "
            "for arbitrary molecules yet, and does not claim static "
            "disorder is negligible - in real devices it often dominates."
        ),
        "key_points": [
            "Organic semiconductors enable flexible electronics, but their charge-transport mechanism is genuinely debated.",
            "Ultrapure organic crystals show band-like signatures (mobility falling with temperature) that hopping theory cannot explain.",
            "The emerging picture: transient localization - charges surf a thermally flickering coupling landscape.",
            "Static disorder vs dynamic disorder must be disentangled to predict real-device mobilities.",
            "The Signature approach derives the coherence-length design rule for high-mobility molecules.",
        ],
        "citations": [CIT_COROPCEANU, CIT_ATKINS, CIT_CRAMER],
    },
    {
        "key": "molecular_computing",
        "name": "Can We Compute With Molecules?",
        "group": "Frontier",
        "ladder_rank": 26,
        "ladder_tier": "frontier",
        "problem": (
            "In 1994 Leonard Adleman solved a small combinatorial problem "
            "using DNA in a test tube - molecular computation was born. "
            "Since then: DNA logic gates, molecular neural networks, "
            "chemical reaction networks that compute. But can molecules "
            "ever compete with silicon, or is molecular computing "
            "destined for niches? The fundamental limits - speed (diffusion "
            "is slow), error rates, energy per operation (Landauer limit), "
            "and I/O - are still being mapped. The unsolved problem: the "
            "true computational power and limits of chemical systems, and "
            "where molecules genuinely beat transistors."
        ),
        "background": (
            "Adleman's 1994 Science paper used DNA hybridization to solve "
            "a 7-city traveling salesman instance: massive parallelism "
            "(10^14 molecules at once) compensating for slow individual "
            "operations. The field grew: DNA strand-displacement circuits "
            "implement logic gates and neural networks; the Belousov-"
            "Zhabotinsky reaction computes image processing; researchers "
            "have built chemical oscillators, memories, and pattern "
            "recognizers. But the sober accounting (advanced by "
            "theorists of chemical computation) shows the catches: "
            "diffusion-limited operations run at hertz, not gigahertz; "
            "error rates compound without the error correction silicon "
            "takes for granted; reading the answer out (sequencing, "
            "spectroscopy) is slow and costly. The Landauer limit sets "
            "the minimum energy per irreversible bit operation - molecules "
            "operate closer to it than transistors, but slowness may "
            "erase the advantage. The field's honest frontier: finding "
            "the problems where massive parallelism plus chemical "
            "embodiment wins despite the speed penalty."
        ),
        "why_it_matters": (
            "If molecules can compute where silicon cannot go - inside "
            "the body (smart therapeutics that sense and decide), in "
            "environments hostile to electronics, or at the ultimate "
            "energy-efficiency limit - it opens a new computing paradigm. "
            "Even short of that, chemical computation illuminates how "
            "cells themselves compute: gene regulation is a molecular "
            "program running now."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the limits walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "audits molecular computation against the Landauer limit, "
            "diffusion speed, and error rates, and proposes the niche-"
            "finding protocol that identifies where molecules genuinely "
            "beat silicon."
        ),
        "sig_full": (
            LABEL + " The Signature approach audits molecular computation "
            "against physical limits and derives the niche-finding "
            "protocol.\n\n"
            "ASSUMPTIONS: (1) Elementary molecular operations are "
            "diffusion- or reaction-limited (~ms to s timescales). (2) "
            "Energy per operation has a Landauer floor (kT ln 2) that "
            "molecules approach more closely than transistors. (3) "
            "Errors compound exponentially with circuit depth unless "
            "corrected; molecular error correction is expensive.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Speed audit: compare "
            "operation rates (molecular Hz vs silicon GHz) and count how "
            "much parallelism is needed to break even on throughput. "
            "Step 2 - Energy audit: compute energy per operation for a "
            "DNA gate vs a transistor gate relative to the Landauer "
            "limit - the efficiency edge. Step 3 - Error budget: for a "
            "circuit of depth d with per-gate error e, compute the "
            "success probability; derive the maximum viable depth. Step "
            "4 - Niche map: score application domains (in-vivo sensing, "
            "combinatorial search, pattern recognition in chemical "
            "space) on parallelism-need vs speed-need vs I/O cost.\n\n"
            "PROPOSED MECHANISM: molecular computing wins only where "
            "massive parallelism and chemical embodiment outweigh slow "
            "serial speed - the niche map, not a silicon replacement, "
            "is the honest target.\n\n"
            "WHAT WOULD CONFIRM IT: a molecular system solving a real "
            "problem (e.g., in-vivo disease-marker classification) "
            "faster, cheaper, or more robustly than the silicon "
            "alternative, as the niche map predicts. WHAT WOULD KILL "
            "IT: proof that error correction overhead always erases "
            "the parallelism advantage at any useful circuit depth.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim molecules will "
            "replace silicon (they will not for general computing), "
            "does not claim the Landauer limit is reachable in "
            "practice, and does not claim current DNA circuits scale - "
            "only the audit framework for finding where they win."
        ),
        "key_points": [
            "Adleman's 1994 DNA computation launched the field: massive molecular parallelism vs slow individual operations.",
            "DNA circuits now implement logic gates and neural networks; chemical systems compute patterns and memories.",
            "The catches: hertz-scale speeds, compounding errors, costly readout - silicon runs at gigahertz.",
            "Molecules operate closer to the Landauer energy limit than transistors - a genuine efficiency edge.",
            "The Signature approach audits speed, energy, and errors to map the niches where molecules genuinely win.",
        ],
        "citations": [CIT_ADLEMAN, CIT_ATKINS, CIT_CRAMER],
    },
    {
        "key": "chemical_space",
        "name": "How Many Stable Molecules Are Possible?",
        "group": "Frontier",
        "ladder_rank": 27,
        "ladder_tier": "frontier",
        "problem": (
            "How many different stable molecules could exist? Estimates "
            "range from 10^23 to 10^180 for drug-like molecules alone - "
            "numbers so large that humanity has made only about 10^8 "
            "compounds, a negligible fraction. But these are guesses: "
            "counting 'possible molecules' requires defining stability, "
            "synthesizability, and the element set, and no rigorous "
            "enumeration exists. The unsolved problem: the true size and "
            "structure of chemical space - and how to navigate a space so "
            "vast that exhaustive search is not just impractical but "
            "meaningless."
        ),
        "background": (
            "The question goes back to Cayley (1875), who counted alkane "
            "isomers and watched the numbers explode combinatorially. "
            "Modern estimates: Bohacek, McMartin, and Guida (1996) put "
            "drug-like molecules at 10^63; others argue 10^23 to 10^60 "
            "depending on constraints. Reymond's chemical space project "
            "has systematically enumerated subsets - like all molecules up "
            "to 17 atoms of C, N, O, S, halogens (GDB-17: 166 billion "
            "structures) - proving the space is both vast and navigable "
            "in slices. But enumeration is not understanding: the space "
            "has structure - activity islands, scaffold hierarchies, "
            "synthetic accessibility gradients - that we are only "
            "beginning to map. Machine learning now explores it by "
            "generating candidates, but generative models sample "
            "unevenly and cannot certify what they have missed. The "
            "deep question is not the number but the geography: what "
            "fraction is stable, what fraction synthesizable, and where "
            "are the useful continents?"
        ),
        "why_it_matters": (
            "Every new drug, material, and catalyst is a point in "
            "chemical space we have not visited. Mapping the space's "
            "structure turns drug discovery from lottery into exploration "
            "strategy: knowing where the useful continents lie, and which "
            "regions are barren, focuses synthesis where it pays. It is "
            "the master map beneath all of molecular design."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the enumeration walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models chemical space as a combinatorial explosion with "
            "stability and synthesizability filters, and proposes the "
            "coverage metric that certifies how much of a region has "
            "actually been explored."
        ),
        "sig_full": (
            LABEL + " The Signature approach builds chemical space as "
            "filtered combinatorics and derives the exploration-coverage "
            "metric.\n\n"
            "ASSUMPTIONS: (1) The raw space is the combinatorial set of "
            "atom-connectivity graphs under valence rules. (2) Filters "
            "apply in sequence: thermodynamic stability, kinetic "
            "persistence, synthetic accessibility - each cutting orders "
            "of magnitude. (3) Usefulness (bioactivity, function) is a "
            "further sparse filter, clustered in 'continents'.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Raw count: "
            "combinatorially enumerate small-molecule graphs to show "
            "the explosion (Cayley's alkane growth as the seed "
            "demonstration). Step 2 - Filter cascade: apply stability "
            "and synthesizability estimates, computing the surviving "
            "fraction at each filter - the honest size estimate. Step 3 "
            "- Geography: cluster a large enumerated library (GDB-style) "
            "by scaffold to reveal the continent structure and the "
            "empty oceans. Step 4 - Coverage metric: for any explored "
            "region, compute the fraction of scaffold-space covered - "
            "the certificate of how much remains.\n\n"
            "PROPOSED MECHANISM: chemical space is a vast filtered "
            "combinatorial set with clustered useful continents; "
            "exploration strategy should maximize scaffold-coverage, "
            "not compound counts.\n\n"
            "WHAT WOULD CONFIRM IT: generative exploration guided by "
            "the coverage metric discovering useful molecules in "
            "previously empty scaffold regions at a higher hit rate "
            "than random screening. WHAT WOULD KILL IT: useful "
            "molecules turning out uniformly distributed (no "
            "continents), or the filters proving so aggressive that "
            "the accessible space is small.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim an exact total "
            "number (the filters are estimates), does not claim "
            "generative models explore evenly, and does not claim "
            "synthesizability is predictable in general - only the "
            "framework for measuring exploration."
        ),
        "key_points": [
            "Estimates of possible drug-like molecules range from 10^23 to 10^180; humanity has made ~10^8 - a negligible fraction.",
            "Cayley (1875) started the counting with alkane isomers; Reymond's GDB-17 enumerated 166 billion small molecules.",
            "The deep question is geography, not the number: where are the useful continents, and what is barren?",
            "Stability and synthesizability filters cut the raw combinatorial space by orders of magnitude.",
            "The Signature approach derives the scaffold-coverage metric that certifies how much of a region is explored.",
        ],
        "citations": [CIT_REYMOND, CIT_CLAYDEN, CIT_CRAMER],
    },
    {
        "key": "open_shell",
        "name": "How Do We Model Molecules With Unpaired Electrons?",
        "group": "Frontier",
        "ladder_rank": 28,
        "ladder_tier": "frontier",
        "problem": (
            "Many of chemistry's most important species - transition-"
            "metal catalysts, metalloenzyme active sites, bond-breaking "
            "transition states, magnetic molecules - have unpaired "
            "electrons and near-degenerate electronic states. Standard "
            "density functional theory (DFT), the workhorse of "
            "computational chemistry, often fails badly for them: it "
            "uses a single electronic configuration where nature needs "
            "many (multireference character). The accurate methods "
            "(CASSCF and its children) scale exponentially and choke on "
            "realistic system sizes. The unsolved problem: a practical, "
            "accurate electronic-structure method for strongly correlated "
            "(multireference) molecules at realistic sizes."
        ),
        "background": (
            "DFT's triumph is the story of modern computational "
            "chemistry: good accuracy at manageable cost for most organic "
            "molecules. But its single-determinant foundation cracks for "
            "open-shell transition metals, bond dissociation, and "
            "excited states - exactly the chemistry of catalysis. The "
            "gold standard, complete-active-space SCF (CASSCF), treats "
            "the multireference problem correctly but its cost grows "
            "exponentially with the active space; a dozen orbitals is "
            "heroic, while a metalloenzyme needs dozens. Cramer's "
            "textbook codified the dilemma. Recent hope comes from "
            "density-matrix renormalization group (DMRG), selected "
            "configuration interaction, and machine-learned wavefunctions "
            "(neural-network quantum states), each pushing the boundary - "
            "but none yet delivers black-box reliability: the user must "
            "still choose the active space wisely, and choosing wrongly "
            "gives confidently wrong answers. For the working chemist, "
            "multireference systems remain the place where computation "
            "is most needed and least trustworthy."
        ),
        "why_it_matters": (
            "Catalyst design, metalloenzyme mechanisms, photochemistry, "
            "and molecular magnetism all run through multireference "
            "electronic structure. A black-box accurate method would "
            "unlock computational design for exactly the reactions that "
            "matter most - nitrogen fixation, water oxidation, C-H "
            "activation - where DFT's errors are largest."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the correlation walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the multireference problem as an active-space "
            "selection problem and proposes the diagnostic-plus-"
            "convergence protocol that certifies a calculation is "
            "trustworthy."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats multireference "
            "calculation as a certification problem and derives the "
            "trust protocol.\n\n"
            "ASSUMPTIONS: (1) Multireference character is measurable: "
            "diagnostics (fractional occupation numbers, spin "
            "contamination, single-reference diagnostics like T1) flag "
            "it. (2) Accuracy requires the active space to include all "
            "strongly correlated orbitals - missing one corrupts the "
            "answer. (3) Converging a property with growing active space "
            "(or with DMRG bond dimension) is the empirical certificate "
            "of correctness.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Diagnostic triage: "
            "compute the multireference diagnostics for a test set "
            "(bond dissociation, transition-metal complexes) and sort "
            "systems by correlation strength. Step 2 - Active-space "
            "audit: show how computed spin-state gaps change as the "
            "active space grows - the non-converged answers scatter, "
            "the converged ones agree. Step 3 - Method shootout: "
            "compare DFT, CASSCF, DMRG, and selected-CI on the same "
            "systems, mapping each method's trustworthy domain. Step 4 "
            "- Certification protocol: the proposed workflow - "
            "diagnose, converge active space, cross-check two methods - "
            "with pass/fail criteria.\n\n"
            "PROPOSED MECHANISM: trustworthy multireference computation "
            "equals diagnostics plus demonstrated convergence; the "
            "field's wrong answers come from skipping one of the two.\n\n"
            "WHAT WOULD CONFIRM IT: blind predictions of spin-state "
            "gaps and reaction barriers for new transition-metal "
            "systems where the protocol's certified answers match "
            "experiment and uncertified ones scatter. WHAT WOULD KILL "
            "IT: systems where the full protocol converges yet "
            "disagrees with experiment - implying missing physics, not "
            "missing correlation.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim a new method "
            "(the protocol organizes existing ones), does not claim "
            "black-box status is achieved, and does not claim DMRG or "
            "neural wavefunctions have won - only the certification "
            "discipline that makes any of them trustworthy."
        ),
        "key_points": [
            "DFT, the workhorse of computational chemistry, fails for strongly correlated (multireference) systems - catalysts, metalloenzymes, bond breaking.",
            "The accurate methods (CASSCF) scale exponentially; a dozen active orbitals is heroic, enzymes need dozens.",
            "Active-space selection is the crux: choose wrongly and the answer is confidently wrong.",
            "New methods (DMRG, selected CI, neural wavefunctions) push the boundary but are not black-box yet.",
            "The Signature approach derives the diagnose-converge-crosscheck certification protocol.",
        ],
        "citations": [CIT_CRAMER, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "interstellar",
        "name": "What Is the Chemistry of Interstellar Space?",
        "group": "Frontier",
        "ladder_rank": 29,
        "ladder_tier": "frontier",
        "problem": (
            "Space is a chemistry lab: over 300 molecules have been "
            "identified in interstellar clouds, from simple diatomics to "
            "fullerenes and chiral propylene oxide. Yet huge spectral "
            "features remain unassigned - the diffuse interstellar bands "
            "(hundreds of absorption lines with no agreed carrier) and the "
            "unidentified infrared emission bands. At 10 Kelvin and near-"
            "vacuum, chemistry runs on ion-molecule reactions, grain-"
            "surface catalysis, and UV processing - regimes barely "
            "reproducible on Earth. The unsolved problem: the complete "
            "inventory and reaction networks of interstellar chemistry, "
            "including the carriers of the century-old unidentified bands."
        ),
        "background": (
            "Tielens' treatise systematized the field: molecular clouds "
            "are cold, dark, and diffuse, yet they manufacture surprising "
            "complexity. Gas-phase ion-molecule reactions (fast even at "
            "10 K, no activation barrier) build chains; dust grains act "
            "as catalytic surfaces where atoms meet and as deep freezers "
            "where ices accumulate; UV and cosmic rays process the ices "
            "into organics. The detections keep coming - benzonitrile, "
            "cyanocyclopentadiene, fullerenes C60/C70 - each a triumph of "
            "lab spectroscopy matched to telescope data. But the diffuse "
            "interstellar bands, first seen in 1922, resisted assignment "
            "for a century (a few were recently attributed to C60+); the "
            "unidentified infrared bands are widely attributed to "
            "polycyclic aromatic hydrocarbons (PAHs) yet no single PAH "
            "has been definitively matched. And the path from "
            "interstellar organics to life's molecules - the astrochemistry-"
            "prebiotic bridge - is mapped only in outline."
        ),
        "why_it_matters": (
            "Interstellar chemistry is the starting inventory for planet "
            "formation: the organics in comets and meteorites seeded "
            "early Earth. Identifying the band carriers closes a "
            "century-old spectroscopic mystery and calibrates our models "
            "of galactic chemical evolution. The grain-surface chemistry "
            "also teaches catalysis in the most extreme conditions "
            "imaginable."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the network walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models interstellar chemistry as coupled gas-grain networks "
            "and proposes the band-carrier identification protocol that "
            "would assign the remaining diffuse interstellar bands."
        ),
        "sig_full": (
            LABEL + " The Signature approach builds the interstellar "
            "network as coupled gas-grain chemistry and derives the "
            "carrier-identification protocol.\n\n"
            "ASSUMPTIONS: (1) At 10 K, gas-phase chemistry is dominated "
            "by barrierless ion-molecule reactions; neutral-neutral "
            "reactions with barriers are frozen out. (2) Grain surfaces "
            "catalyze atom-addition reactions (H, C, N, O) and store "
            "the products as ices. (3) A band carrier is identified only "
            "by laboratory spectroscopy matching astronomical spectra "
            "in position, profile, and relative intensity.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Network skeleton: "
            "write the ion-molecule reaction network for a dark cloud "
            "and compute steady-state abundances - the baseline "
            "inventory. Step 2 - Grain audit: add surface reactions and "
            "ice processing; show which molecules REQUIRE grains "
            "(their gas-phase routes are too slow). Step 3 - Carrier "
            "shortlist: for the unidentified bands, generate candidate "
            "carriers (PAH variants, fullerenes, carbon chains) and "
            "compute their predicted spectra. Step 4 - Identification "
            "protocol: the lab-measurement campaign - gas-phase "
            "spectroscopy of each candidate under interstellar-like "
            "conditions, matched against telescope data with "
            "statistical scoring.\n\n"
            "PROPOSED MECHANISM: interstellar complexity equals "
            "barrierless gas-phase ion chemistry PLUS grain-surface "
            "catalysis PLUS energetic ice processing; the unidentified "
            "bands are large carbonaceous molecules whose lab spectra "
            "have not yet been measured in the right conditions.\n\n"
            "WHAT WOULD CONFIRM IT: laboratory gas-phase spectra of a "
            "candidate (e.g., a specific PAH ion) matching multiple "
            "diffuse bands in position and profile, as C60+ did for a "
            "few. WHAT WOULD KILL IT: exhaustive candidate spectroscopy "
            "with no matches - implying the carriers are something "
            "entirely unconsidered (e.g., grain-surface species).\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the PAH "
            "hypothesis is proven (it is the leading attribution, not a "
            "proof), does not claim the prebiotic bridge is mapped, and "
            "does not claim models reproduce all observed abundances - "
            "only the network-plus-protocol framework."
        ),
        "key_points": [
            "Over 300 molecules are known in interstellar space, built at 10 K by ion-molecule reactions and grain-surface catalysis.",
            "The diffuse interstellar bands (seen since 1922) and unidentified infrared bands still lack agreed carriers.",
            "A few DIBs were recently assigned to C60+ - proof the century-old mystery is crackable.",
            "PAHs are the leading attribution for the infrared bands, but no single PAH is definitively matched.",
            "The Signature approach derives the lab-spectroscopy identification protocol for the remaining bands.",
        ],
        "citations": [CIT_TIELENS, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "metallic_hydrogen",
        "name": "What Is Metallic Hydrogen, and Can It Survive at Room Temperature?",
        "group": "Frontier",
        "ladder_rank": 30,
        "ladder_tier": "frontier",
        "problem": (
            "In 1935 Wigner and Huntington predicted that squeezing "
            "hydrogen hard enough would turn it into a metal - a lattice "
            "of protons in a sea of electrons, possibly a room-"
            "temperature superconductor and a revolutionary rocket fuel. "
            "Ninety years later, metallic hydrogen remains one of "
            "physics and chemistry's great chases: diamond-anvil claims "
            "are announced and contested, the required pressures (~400-"
            "500 GPa) push instruments to their limits, and whether the "
            "metallic phase could be metastable at ambient pressure - "
            "recoverable, usable - is unknown. The unsolved problem: "
            "definitive creation, characterization, and recovery of "
            "metallic hydrogen."
        ),
        "background": (
            "Wigner and Huntington's 1935 paper calculated that at ~25 "
            "GPa hydrogen should metalize - an underestimate, but the "
            "idea stuck: hydrogen, the simplest element, should become "
            "an alkali-like metal under pressure. Modern calculations put "
            "metalization near 400-500 GPa, pressures found only in "
            "giant-planet interiors (metallic hydrogen likely fills "
            "Jupiter). The experimental chase has produced drama: "
            "multiple claims of observation, retractions, and fierce "
            "debate over whether reflective samples in diamond anvils "
            "are hydrogen or artifacts (alumina from the gasket, "
            "stressed diamond). Theory adds the tantalizing possibility "
            "that metallic hydrogen, once formed, might remain "
            "metastable when pressure is released - calculations "
            "disagree. If recoverable and superconducting near room "
            "temperature (as some theories predict, given hydrogen's "
            "light mass and high phonon frequencies), it would transform "
            "energy transmission and propulsion - which is why each "
            "claim makes headlines and each refutation stings."
        ),
        "why_it_matters": (
            "A room-temperature superconductor would revolutionize power "
            "grids, maglev, and medical imaging; metallic hydrogen is "
            "theorized to be one. As a propellant, metastable metallic "
            "hydrogen's recombination energy dwarfs chemical fuels. And "
            "Jupiter's interior is made of the stuff - understanding it "
            "is planetary science too."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the compression walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models metalization as band-gap closure under compression "
            "and proposes the multi-probe certification protocol that a "
            "metallic-hydrogen claim must pass."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats metallic-hydrogen "
            "claims as a certification problem and derives the "
            "multi-probe protocol.\n\n"
            "ASSUMPTIONS: (1) Metalization occurs when compression "
            "closes hydrogen's band gap (~400-500 GPa per modern "
            "theory). (2) A genuine claim must show metallic "
            "reflectivity AND the sample must be proven to be hydrogen "
            "(not gasket or diamond artifacts). (3) Metastability at "
            "ambient pressure requires a kinetic barrier to "
            "recombination - calculable in principle.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Gap audit: compute "
            "the band gap vs pressure from the Wigner-Huntington "
            "reasoning updated with modern equations of state - the "
            "pressure target. Step 2 - Artifact census: list every "
            "known false-positive (alumina reflectance, stressed-"
            "diamond Raman shifts, hydrogen diffusion into gaskets) "
            "and its diagnostic. Step 3 - Certification protocol: the "
            "claim must pass reflectivity + Raman (proving hydrogen "
            "present) + conductivity + pressure calibration by an "
            "independent standard, all on the same sample. Step 4 - "
            "Metastability test: compute the predicted barrier to "
            "recombination on decompression; design the controlled "
            "release experiment.\n\n"
            "PROPOSED MECHANISM: metallic hydrogen is real at "
            "sufficient pressure (Jupiter proves the phase exists); "
            "the scientific problem is certification of laboratory "
            "samples and the open question of ambient metastability.\n\n"
            "WHAT WOULD CONFIRM IT: a sample passing the full "
            "multi-probe protocol, reproduced by an independent lab, "
            "with measured superconducting transition if present. WHAT "
            "WOULD KILL IT: a proof that the barrier to recombination "
            "vanishes at low pressure (no metastability possible), or "
            "all claims failing the artifact census.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim metallic "
            "hydrogen has been definitively made (claims are "
            "contested), does not claim room-temperature "
            "superconductivity is established, and does not claim "
            "metastability - only the protocol that would settle each."
        ),
        "key_points": [
            "Wigner and Huntington (1935) predicted hydrogen becomes a metal under extreme pressure - possibly a room-temperature superconductor.",
            "Laboratory claims at 400-500 GPa are announced and contested; artifacts (gasket, diamond) mimic the signal.",
            "Whether metallic hydrogen could survive decompression (metastability) is theoretically disputed.",
            "Jupiter's interior is likely metallic hydrogen - the phase exists in nature.",
            "The Signature approach derives the multi-probe certification protocol every claim must pass.",
        ],
        "citations": [CIT_WIGNER, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "htsc",
        "name": "What Makes High-Temperature Superconductors Superconduct?",
        "group": "Frontier",
        "ladder_rank": 31,
        "ladder_tier": "frontier",
        "problem": (
            "In 1986 Bednorz and Mueller found superconductivity at 35 K "
            "in a copper oxide - shattering the old limits and launching "
            "a revolution. Cuprates now superconduct above liquid-"
            "nitrogen temperatures; iron-based and hydride "
            "superconductors followed. Yet nearly forty years later, "
            "there is no agreed mechanism for cuprate superconductivity: "
            "conventional phonon pairing cannot explain it, and "
            "competing theories (spin fluctuations, resonating valence "
            "bonds, stripes, quantum criticality) each explain part of "
            "the phenomenology. The unsolved problem: the pairing glue "
            "in high-temperature superconductors."
        ),
        "background": (
            "Before 1986, theory said superconductivity above ~30 K was "
            "unlikely; Bednorz and Mueller's La-Ba-Cu-O at 35 K broke "
            "the rule within months, and YBCO at 93 K followed within a "
            "year. The cuprate phase diagram became the most studied "
            "image in condensed matter: antiferromagnetic insulator at "
            "zero doping, superconducting dome at intermediate doping, "
            "strange metal above. The pseudogap region - a partial "
            "energy gap opening well above the superconducting "
            "transition - is itself a major unsolved sub-problem. "
            "Anderson's resonating-valence-bond proposal, spin-"
            "fluctuation theories, stripe and charge-order pictures, "
            "and quantum-critical scenarios all capture aspects: "
            "magnetism is clearly involved, but whether spin "
            "fluctuations ARE the pairing glue or fellow travelers "
            "remains contested. Hydride superconductors (H3S at 203 K, "
            "LaH10 at 250 K under megabar pressures) are more "
            "conventional - phonon-mediated - which sharpens the "
            "question: what is different about the cuprates?"
        ),
        "why_it_matters": (
            "Room-temperature, ambient-pressure superconductivity would "
            "transform civilization: lossless power grids, compact fusion "
            "magnets, maglev everywhere, ultra-efficient electronics. "
            "Every proposed mechanism is also a design hint - knowing "
            "the glue tells us what to synthesize next. The hydrides "
            "show high Tc is possible; the cuprates suggest it might be "
            "possible without megabar pressures."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the pairing-glue walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the cuprate phase diagram as magnetism and "
            "superconductivity competing for the same electrons, and "
            "proposes the glue-fingerprint experiment that would identify "
            "the pairing boson."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats the pairing glue as "
            "an identification problem and derives the fingerprint test.\n\n"
            "ASSUMPTIONS: (1) Cuprate superconductivity is d-wave "
            "pairing emerging from doping an antiferromagnetic Mott "
            "insulator. (2) The pairing boson leaves fingerprints: its "
            "energy scale appears in tunneling spectra, its symmetry in "
            "the gap structure, its doping dependence in the Tc dome. "
            "(3) The pseudogap is either a competitor or a precursor - "
            "the glue test must distinguish these.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Dome audit: map Tc "
            "vs doping and extract the energy scales (pseudogap, spin "
            "resonance, superconducting gap) - the phenomenology ledger. "
            "Step 2 - Glue candidates: for spin fluctuations, RVB, and "
            "charge-order scenarios, compute the predicted tunneling "
            "spectrum and gap symmetry. Step 3 - Fingerprint match: "
            "identify which measurements discriminate the candidates "
            "(e.g., the neutron spin resonance's relation to the gap). "
            "Step 4 - Design hint: from the winning glue, derive what "
            "chemical tuning (layer spacing, apical oxygen, disorder) "
            "should raise Tc.\n\n"
            "PROPOSED MECHANISM: the glue is magnetic in origin - spin "
            "fluctuations pairing electrons in the d-wave channel, with "
            "charge order as competitor; the dome is the sweet spot "
            "where magnetism is strong enough to pair but not so strong "
            "as to localize.\n\n"
            "WHAT WOULD CONFIRM IT: a doping- and material-series where "
            "the spin-fluctuation spectrum quantitatively predicts Tc "
            "and the gap structure across the dome, with the pseudogap "
            "resolved as precursor pairing. WHAT WOULD KILL IT: a "
            "cuprate family where Tc is high but spin fluctuations are "
            "absent, or a competing theory predicting the dome shape "
            "better.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the mechanism is "
            "settled (it is the most contested problem in the field), "
            "does not claim the pseudogap is understood, and does not "
            "claim a room-temperature recipe - only the fingerprint "
            "test and the design hints it would unlock."
        ),
        "key_points": [
            "Bednorz and Mueller (1986) shattered the Tc ceiling; cuprates superconduct above liquid-nitrogen temperature.",
            "Nearly 40 years later, the pairing mechanism is still contested: spin fluctuations, RVB, stripes, quantum criticality.",
            "The pseudogap - a partial gap opening above Tc - is itself a major unsolved sub-problem.",
            "Hydride superconductors (250 K at megabar pressures) are conventional; the cuprates' ambient-pressure mystery is sharper.",
            "The Signature approach derives the glue-fingerprint test from the phase-diagram ledger.",
        ],
        "citations": [CIT_BEDNORZ, CIT_ATKINS, CIT_HOUSECROFT],
    },
    {
        "key": "inverse_design",
        "name": "How Do We Design Materials Backwards From Properties?",
        "group": "Frontier",
        "ladder_rank": 32,
        "ladder_tier": "frontier",
        "problem": (
            "The traditional materials pipeline goes composition to "
            "structure to property: make it, then measure what you got. "
            "Inverse design flips it: specify the desired property (a "
            "band gap, a catalytic activity, a thermal conductivity) and "
            "compute which material has it. The Materials Project and "
            "similar databases now hold millions of computed compounds, "
            "and machine learning proposes new ones - but the loop "
            "rarely closes: predicted materials fail to synthesize, "
            "computed properties miss real-world behavior, and the "
            "search space dwarfs the databases. The unsolved problem: a "
            "reliable inverse-design loop from property specification to "
            "synthesized, working material."
        ),
        "background": (
            "Jain and colleagues' 2013 Materials Project paper launched "
            "the materials-genome era: high-throughput density-functional "
            "calculations covering tens of thousands of compounds, open "
            "to all. The paradigm works in showcase cases - new battery "
            "cathodes, thermoelectrics, and catalysts proposed "
            "computationally and confirmed experimentally. But the "
            "failure modes are systematic: DFT formation energies have "
            "errors that can invert stability rankings; synthesizability "
            "is not computed (a predicted compound may be unmakable); "
            "real properties (defects, grain boundaries, temperature) "
            "differ from ideal-crystal calculations; and generative ML "
            "models propose structures outside their training "
            "distribution with unreliable property predictions. The "
            "field's dirty secret: the hit rate from prediction to "
            "working material is low, and negative results go "
            "unpublished, so the true reliability is unknown."
        ),
        "why_it_matters": (
            "Batteries, solar cells, catalysts, superconductors, "
            "thermoelectrics - every energy and electronics technology "
            "waits on better materials. A reliable inverse-design loop "
            "would compress the 20-year materials-development cycle to "
            "years, letting us design the exact material each "
            "application needs instead of adapting applications to "
            "available materials."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the design-loop walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models inverse design as a five-gate loop - property, "
            "stability, synthesizability, realizability, validation - and "
            "proposes the published hit-rate protocol that would certify "
            "a design pipeline as genuinely reliable."
        ),
        "sig_full": (
            LABEL + " The Signature approach builds inverse design as a "
            "five-gate loop and derives the reliability certification.\n\n"
            "ASSUMPTIONS: (1) A target property can be computed with "
            "known error bars for candidate structures. (2) "
            "Thermodynamic stability, synthesizability, and real-world "
            "realizability (defects, temperature) are separate gates "
            "with their own models. (3) A pipeline's reliability is "
            "measured by its published hit rate: predictions made vs "
            "materials working as predicted.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Property gate: "
            "screen candidates by computed target property with "
            "uncertainty quantification - the shortlist. Step 2 - "
            "Stability gate: rank by energy above the convex hull with "
            "honest DFT error bars; discard the thermodynamically "
            "hopeless. Step 3 - Synthesizability gate: score by "
            "learned synthesizability models and precursor "
            "availability; discard the unmakable. Step 4 - "
            "Realizability gate: estimate defect and temperature "
            "effects on the target property. Step 5 - Validation "
            "ledger: synthesize the survivors, publish hits AND "
            "misses, and update every gate's model.\n\n"
            "PROPOSED MECHANISM: reliable inverse design equals the "
            "five-gate loop with a published hit-rate ledger; pipelines "
            "fail by skipping gates (usually synthesizability) and by "
            "hiding misses.\n\n"
            "WHAT WOULD CONFIRM IT: a pipeline publishing a hit rate "
            "above 50% (predicted materials working as predicted) over "
            "dozens of attempts, with misses analyzed and fed back. "
            "WHAT WOULD KILL IT: hit rates stuck near zero despite all "
            "gates - implying the computed-property to real-material "
            "mapping is fundamentally unreliable.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim current "
            "pipelines are reliable (hit rates are low and "
            "underreported), does not claim DFT errors are solved, and "
            "does not claim synthesizability is predictable in general "
            "- only the loop structure and the honesty ledger."
        ),
        "key_points": [
            "Inverse design flips the pipeline: specify the property, compute the material - instead of make-then-measure.",
            "The Materials Project (2013) launched the materials-genome era with millions of computed compounds.",
            "Systematic failure modes: DFT error bars invert rankings, synthesizability is not computed, real materials differ from ideal crystals.",
            "Published hit rates are low and misses go unpublished - true reliability is unknown.",
            "The Signature approach builds the five-gate loop and the published hit-rate certification.",
        ],
        "citations": [CIT_JAIN, CIT_CRAMER, CIT_HOUSECROFT],
    },
    {
        "key": "superheavy",
        "name": "Why Do Heavy Elements Break the Periodic Table Patterns?",
        "group": "Frontier",
        "ladder_rank": 33,
        "ladder_tier": "frontier",
        "problem": (
            "The periodic table predicts chemical behavior from position - "
            "but for the heaviest elements, relativity rewrites the "
            "rules. In superheavy atoms, inner electrons move at a "
            "large fraction of light speed, gaining mass, contracting "
            "orbitals, and reshuffling the valence shells that control "
            "chemistry. Gold is golden and mercury is liquid because of "
            "relativity; for elements past 100, the effects are so "
            "strong that an element may not behave like its group at "
            "all - copernicium might be a volatile liquid-metal gas, "
            "oganesson might be a reactive solid, not a noble gas. The "
            "unsolved problem: predicting and verifying the chemistry "
            "of superheavy elements, atom by atom."
        ),
        "background": (
            "Pyykko's 1988 Chemical Reviews article, 'Relativistic "
            "effects in structural chemistry,' showed relativity is not "
            "a small correction: the 6s contraction makes gold's color, "
            "mercury's liquidity, and lead-acid battery voltages what "
            "they are. For superheavy elements (Z > 103), made atom-by-"
            "atom in accelerators with half-lives of seconds or "
            "milliseconds, the effects dominate: spin-orbit splitting "
            "can exceed shell gaps, scrambling the Aufbau order. "
            "Chemistry must be done one atom at a time - gas-phase "
            "chromatography catching single atoms, measuring adsorption "
            "enthalpies from a handful of decay events. Copernicium "
            "(Z=112) behaves more volatile than mercury, contrary to "
            "naive group trends; flerovium (114) shows unexpected "
            "inertness; oganesson (118) is predicted to be no noble gas "
            "at all. Each new element is an experimentum crucis for "
            "relativistic quantum chemistry - and the calculations are "
            "so demanding that predictions often precede measurements "
            "by decades."
        ),
        "why_it_matters": (
            "Superheavy chemistry tests quantum mechanics in its most "
            "extreme regime - where relativity and electron correlation "
            "collide. It probes the predicted 'island of stability' of "
            "long-lived nuclei and completes our understanding of the "
            "periodic system's limits. The relativistic methods honed "
            "here also improve everyday chemistry of heavy elements: "
            "catalysts, batteries, and nuclear materials."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the relativistic walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models superheavy chemistry as relativistic orbital "
            "reshuffling and proposes the single-atom adsorption test "
            "that would verify each element's predicted personality."
        ),
        "sig_full": (
            LABEL + " The Signature approach treats superheavy chemistry "
            "as orbital reshuffling under relativity and derives the "
            "single-atom verification test.\n\n"
            "ASSUMPTIONS: (1) Inner-shell electrons at high Z reach "
            "relativistic speeds; the mass increase contracts s and p1/2 "
            "orbitals and expands d and f orbitals indirectly. (2) "
            "Spin-orbit splitting can reorder valence shells, changing "
            "the chemically active configuration. (3) Single-atom "
            "gas-phase adsorption enthalpies are the measurable proxy "
            "for volatility/reactivity.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Contraction audit: "
            "compute the relativistic 7s contraction for Z=112-118 and "
            "show how it stabilizes the closed shell (the inertness "
            "mechanism). Step 2 - Reordering map: for each superheavy "
            "element, derive the predicted valence configuration and "
            "the group-trend violation it implies. Step 3 - Adsorption "
            "prediction: convert the predicted atomic properties into "
            "a measurable adsorption enthalpy on gold or quartz "
            "surfaces. Step 4 - Atom-at-a-time statistics: design the "
            "experiment - how many decay events are needed to "
            "distinguish the predicted enthalpy from the group-trend "
            "expectation.\n\n"
            "PROPOSED MECHANISM: superheavy chemistry equals the "
            "periodic table re-sorted by relativity; each element's "
            "'personality' is its relativistically reshuffled valence "
            "shell, testable one atom at a time.\n\n"
            "WHAT WOULD CONFIRM IT: single-atom thermochromatography "
            "measuring adsorption enthalpies that match the "
            "relativistic predictions (and violate naive group trends) "
            "for multiple elements. WHAT WOULD KILL IT: elements that "
            "follow naive group trends despite large predicted "
            "relativistic effects - implying the calculations "
            "overestimate reality.\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim long-lived "
            "superheavies exist (the island of stability is unreached), "
            "does not claim bulk chemistry is possible (it is not, at "
            "atom-at-a-time scales), and does not claim the "
            "calculations are easy - only the prediction-to-measurement "
            "chain."
        ),
        "key_points": [
            "Relativity reshuffles superheavy atoms' valence shells - elements may not behave like their periodic-table group at all.",
            "Pyykko (1988) showed relativity is no small correction: gold's color and mercury's liquidity are relativistic effects.",
            "Superheavy elements are made atom-by-atom with second-scale half-lives; chemistry is single-atom thermochromatography.",
            "Copernicium is unexpectedly volatile; oganesson may be no noble gas - predictions awaiting decisive tests.",
            "The Signature approach derives each element's predicted personality and the atom-count needed to verify it.",
        ],
        "citations": [CIT_PYYKKO, CIT_HOUSECROFT, CIT_ATKINS],
    },
    {
        "key": "de_novo_enzyme",
        "name": "Can We Create Artificial Enzymes as Good as Natures?",
        "group": "Frontier",
        "ladder_rank": 34,
        "ladder_tier": "frontier",
        "problem": (
            "If we understood enzyme catalysis completely, we could "
            "design new enzymes from scratch - for reactions nature "
            "never evolved, like breaking down plastics or capturing "
            "CO2. Computational enzyme design has produced real "
            "catalysts: the 2008 Kemp-elimination designs proved the "
            "principle. But designed enzymes are typically millions of "
            "times worse than natural ones - their rate enhancements "
            "are modest, and closing the gap has required rounds of "
            "directed evolution. The unsolved problem: designing, "
            "purely computationally, an enzyme that rivals natural "
            "catalytic proficiency - and understanding what the "
            "designs are still missing."
        ),
        "background": (
            "Rothlisberger and colleagues' 2008 Nature paper was the "
            "landmark: computationally designed protein scaffolds "
            "catalyzing the Kemp elimination, a reaction with no natural "
            "enzyme. The designs worked - proof of principle - but with "
            "rate enhancements around 10^5, versus natural enzymes' "
            "10^15 or more. The field's response was revealing: "
            "directed evolution (mutating and selecting the designs in "
            "the lab) improved them by orders of magnitude, showing "
            "the designs were good starting points but missing "
            "something. What? The leading hypotheses: designs capture "
            "transition-state binding but miss electrostatic "
            "preorganization; they are too rigid, missing the dynamical "
            "motions natural enzymes use; their active sites are "
            "over-solvated or misaligned by fractions of an angstrom "
            "that matter enormously. Each design-evolution cycle teaches "
            "the field what to compute next - but a purely "
            "computational design matching natural proficiency has not "
            "yet been achieved."
        ),
        "why_it_matters": (
            "Designer enzymes for non-natural reactions would "
            "revolutionize manufacturing: plastic-degrading enzymes for "
            "waste, CO2-capturing enzymes for climate, new synthetic "
            "routes for medicines - all running at room temperature in "
            "water. The gap between designed and natural enzymes "
            "measures exactly what we still do not understand about "
            "catalysis itself."
        ),
        "sig_pointer": (
            LABEL + " The Signature half of this database (this title, "
            "Signature Edition) carries the full step-by-step treatment: "
            "assumptions, the gap-closing walkthrough, and the "
            "confirm-or-refute panel. In one line: the Signature approach "
            "models the design gap as missing preorganization plus "
            "missing dynamics, and proposes the head-to-head design "
            "competition that would prove the gap closed."
        ),
        "sig_full": (
            LABEL + " The Signature approach audits the design gap "
            "factor by factor and derives the competition that would "
            "prove it closed.\n\n"
            "ASSUMPTIONS: (1) Natural proficiency (~10^15) factorizes "
            "into transition-state binding, electrostatic "
            "preorganization, tunneling, and dynamics (per the enzyme-"
            "speed record in this database). (2) Current computational "
            "designs capture mainly the first factor. (3) A designed "
            "enzyme 'rivals nature' when its proficiency is within two "
            "orders of magnitude of natural enzymes for comparable "
            "reactions.\n\n"
            "REASONING PATH, STEP BY STEP: Step 1 - Gap ledger: place "
            "the best pure-computation designs and natural enzymes on "
            "the proficiency scale; quantify the gap (typically 10^8 "
            "to 10^10). Step 2 - Missing-factor audit: for a designed "
            "enzyme, compute its electrostatic preorganization vs a "
            "natural enzyme's - the hypothesized missing millions. "
            "Step 3 - Dynamics prescription: specify what the design "
            "protocol must add - flexible-backbone sampling, "
            "electric-field optimization, second-shell design. Step 4 "
            "- Competition spec: the head-to-head test - a blind "
            "reaction target, pure-computation designs only, "
            "proficiency measured by independent labs.\n\n"
            "PROPOSED MECHANISM: the design gap is missing "
            "preorganization plus missing dynamics; closing it requires "
            "designing the electric field and the motions, not just the "
            "shape of the active site.\n\n"
            "WHAT WOULD CONFIRM IT: a purely computational design "
            "achieving within 100x of natural proficiency on a "
            "non-natural reaction, reproduced independently. WHAT WOULD "
            "KILL IT: proof that the missing factors are "
            "computationally intractable in principle (e.g., dynamics "
            "contributions that cannot be predicted from structure).\n\n"
            "WHAT IT DOES NOT CLAIM: it does not claim the gap is "
            "closed (it is not), does not claim directed evolution is "
            "unnecessary (it currently is necessary), and does not "
            "claim any specific protocol will work - only the audit "
            "that shows what must be added and the competition that "
            "would prove it."
        ),
        "key_points": [
            "Computational enzyme design works in principle (2008 Kemp elimination) but designs lag natural enzymes by ~10^8-10^10 in proficiency.",
            "Directed evolution closes much of the gap in the lab - proving the designs are good starting points missing something.",
            "Leading hypotheses for the missing factors: electrostatic preorganization and protein dynamics.",
            "Designer enzymes for plastic breakdown or CO2 capture await the gap closing.",
            "The Signature approach audits the gap factor by factor and proposes the blind design competition.",
        ],
        "citations": [CIT_ROTHLISBERGER, CIT_WOLFENDEN, CIT_CLAYDEN],
    },
]
