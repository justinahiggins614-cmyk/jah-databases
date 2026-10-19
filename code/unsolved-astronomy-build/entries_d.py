#!/usr/bin/env python3
"""Entries 27-34 (ladder ranks 27-34, Advanced)."""

CIT_RIESS98 = ("Riess AG et al. Observational evidence from supernovae for an "
               "accelerating universe and a cosmological constant. Astron J; 1998.")
CIT_PERLMUTTER = ("Perlmutter S et al. Measurements of Omega and Lambda from 42 "
                  "high-redshift supernovae. Astrophys J; 1999.")
CIT_DESI = ("DESI Collaboration. DESI 2024 results: validation of cosmological "
            "parameters and evolving dark energy. JCAP; 2025.")
CIT_GUNN = ("Gunn JE, Peterson BA. On the density of neutral hydrogen in "
            "intergalactic space. Astrophys J; 1965.")
CIT_FAN = ("Fan X et al. Constraining the evolution of the ionizing background "
           "and the epoch of reionization with z~6 quasars. Astron J; 2006.")
CIT_PLANCK = ("Planck Collaboration. Planck 2018 results: VI. Cosmological "
              "parameters. Astron Astrophys; 2020.")
CIT_BOWMAN = ("Bowman JD et al. An absorption profile centred at 78 MHz in the "
              "sky-averaged spectrum. Nature; 2018.")
CIT_SINGH = ("Singh S et al. On the detection of a cosmic dawn signal in the "
             "SARAS 3 data. Nature Astron; 2022.")
CIT_CLOWES = ("Clowes RG et al. A structure in the early Universe at z~1.3 that "
              "exceeds the homogeneity scale of the R-W concordance cosmology. "
              "Mon Not R Astron Soc; 2013.")
CIT_YADAV = ("Yadav JK et al. Fractal dimension as a measure of the scale of "
             "homogeneity. Mon Not R Astron Soc; 2010.")
CIT_HAWKING = ("Hawking SW. Breakdown of predictability in gravitational "
               "collapse. Phys Rev D; 1976.")
CIT_ALMHEIRI = ("Almheiri A et al. The entropy of bulk quantum fields and the "
                "entanglement wedge of an evaporating black hole. JHEP; 2019.")
CIT_AMPS = ("Almheiri A, Marolf D, Polchinski J, Sully J. Black holes: "
            "complementarity or firewalls? JHEP; 2013.")
CIT_PENROSE = ("Penrose R. Gravitational collapse and space-time singularities. "
               "Phys Rev Lett; 1965.")
CIT_MATHUR = ("Mathur SD. The fuzzball proposal for black holes. Fortschr Phys; 2005.")
CIT_GUTH = ("Guth AH. Inflationary universe: a possible solution to the horizon "
            "and flatness problems. Phys Rev D; 1981.")
CIT_LINDE = ("Linde A. Eternally existing self-reproducing chaotic inflationary "
             "universe. Phys Lett B; 1986.")
CIT_CALDWELL = ("Caldwell RR, Kamionkowski M, Weinberg NN. Phantom energy: dark "
                "energy with w < -1 causes a cosmic doomsday. Phys Rev Lett; 2003.")

ENTRIES_D = [
    {
        "key": "dark-energy",
        "name": "The Nature of Dark Energy",
        "group": "Advanced",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("Something is accelerating the expansion of the universe, "
                    "making up 69 percent of everything - and the simplest "
                    "explanation is off by 10^120. What is dark energy?"),
        "background": (
            "In 1998 two supernova teams found that distant supernovae are dimmer "
            "than expected: the universe's expansion is speeding up, a discovery "
            "that won the 2011 Nobel Prize. The simplest explanation is Einstein's "
            "cosmological constant - the energy of empty space - but quantum field "
            "theory predicts a vacuum energy 10^120 times larger than observed, "
            "the worst prediction in physics. Alternatives include quintessence, a "
            "dynamical field evolving over time, and modified gravity theories that "
            "change the laws on cosmic scales. In 2024-2025 the DESI survey reported "
            "hints that dark energy may be evolving, with the equation-of-state "
            "parameter differing from the constant value - a result that, if "
            "confirmed, rules out the cosmological constant."),
        "why_it_matters": (
            "Dark energy decides the fate of the universe and is the biggest "
            "unsolved problem in physics by energy budget. Its identity - vacuum "
            "energy, new field, or modified gravity - determines whether our "
            "understanding of gravity and quantum theory needs a revolution. "
            "Every precision cosmology survey of the next decade is, at heart, a "
            "dark-energy experiment."),
        "sig_pointer": (
            "The Signature edition walks the budget arithmetic: the 69-percent "
            "share, the 10^120 vacuum discrepancy, and the evolving-dark-energy "
            "scorecard from DESI."),
        "sig_solution": (
            "Assumptions: the supernova, CMB, and BAO measurements are correct and "
            "the DESI hint of evolution is taken as a hint, not a detection. "
            "Reasoning: the problem splits cleanly - either the acceleration is a "
            "substance (constant or field) or gravity itself is modified - and "
            "each branch makes distinct predictions for how the expansion history "
            "and structure growth relate. Proposed method: compute the expansion "
            "history for three benchmark models (cosmological constant, "
            "evolving-field w0wa, modified gravity) and score each against the "
            "combined supernova plus BAO plus CMB dataset, tracking both the fit "
            "quality and the fine-tuning cost of each. What would confirm evolving "
            "dark energy: DESI's full survey plus independent supernova data "
            "converging on w different from -1 at high significance. What would "
            "kill the vacuum-energy interpretation: a laboratory or theoretical "
            "result fixing the vacuum energy at the naive quantum value with no "
            "cancellation mechanism. What this does NOT claim: it does not claim "
            "dark energy evolves, does not claim the cosmological constant is "
            "dead, and does not claim modified gravity is viable."),
        "citations": [CIT_RIESS98, CIT_PERLMUTTER, CIT_DESI],
        "demo_params": {"omega_lambda": 0.69, "vacuum_discrepancy": 1.0e120},
    },
    {
        "key": "reionization",
        "name": "What Lit the Universe Back Up",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("After the Big Bang the universe went dark and neutral; then "
                    "something reionized it. Which sources - galaxies, quasars, or "
                    "something exotic - burned off the cosmic fog?"),
        "background": (
            "Recombination, 380,000 years after the Big Bang, left the universe "
            "full of neutral hydrogen - opaque and dark. By redshift 6, quasar "
            "spectra show the intergalactic medium was ionized again, with the "
            "Gunn-Peterson trough marking the transition. The Planck satellite's "
            "measurement of the Thomson optical depth, 0.054, pins the midpoint of "
            "reionization near redshift 7.7. The suspects are the first generations "
            "of stars and galaxies leaking ultraviolet photons, with quasars as a "
            "possible minority contributor. JWST keeps finding surprisingly abundant "
            "bright galaxies at redshift 10 and beyond - more ionizing sources "
            "than expected - while 21-centimeter experiments try to map the neutral "
            "gas directly. The photon budget roughly balances, but the exact "
            "sources and timeline are still being filled in."),
        "why_it_matters": (
            "Reionization is the last global phase transition of the universe - "
            "the moment starlight first sculpted intergalactic space. Its sources "
            "are the first galaxies, the ancestors of everything. Mapping it "
            "tests our whole picture of early star formation and the escape of "
            "radiation into intergalactic space."),
        "sig_pointer": (
            "The Signature edition walks the photon budget: photons per baryon "
            "required, the optical-depth constraint, and the escape-fraction "
            "ledger for galaxies versus quasars."),
        "sig_solution": (
            "Assumptions: the Planck optical depth of 0.054 is correct and the "
            "Gunn-Peterson observations fix the end of reionization near redshift "
            "6. Reasoning: reionization is a photon-counting problem - each baryon "
            "needs of order a few ionizing photons after accounting for "
            "recombinations - so the candidate sources must demonstrably supply "
            "the budget. Proposed method: compute the required ionizing emissivity "
            "as a function of redshift from the optical depth, then integrate the "
            "observed galaxy luminosity functions (JWST) times the escape fraction "
            "plus the quasar contribution, and identify the redshift range where "
            "the budget fails to close. What would confirm galaxies as the "
            "dominant source: direct Lyman-continuum leakage measurements showing "
            "escape fractions that close the budget at redshift 7-8. What would "
            "kill the galaxy-only picture: a 21-centimeter measurement of the "
            "neutral fraction timeline incompatible with the galaxy emissivity. "
            "What this does NOT claim: it does not claim the budget is closed, "
            "does not claim quasars are negligible, and does not claim the escape "
            "fractions are measured."),
        "citations": [CIT_GUNN, CIT_FAN, CIT_PLANCK],
        "demo_params": {"tau": 0.054, "z_mid": 7.7, "photons_per_baryon": 3.0},
    },
    {
        "key": "dark-ages",
        "name": "The Cosmic Dark Ages",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("Between the fading of the Big Bang's glow and the ignition "
                    "of the first stars lies a 100-million-year gap no telescope "
                    "has seen into. What did the dark ages look like?"),
        "background": (
            "After recombination the universe was filled with cooling neutral "
            "hydrogen and no light sources - the dark ages, roughly redshifts 1100 "
            "down to 20. The only probe is the 21-centimeter line of neutral "
            "hydrogen, redshifted by cosmic expansion into the radio band: gas at "
            "redshift 20 appears near 68 MHz. In 2018 the EDGES experiment reported "
            "an absorption trough at 78 MHz twice as deep as standard cosmology "
            "allows - a possible signature of exotic cooling, perhaps by dark "
            "matter interactions. The SARAS 3 experiment in 2022 did not confirm "
            "the signal, and the field awaits the HERA array and lunar far-side "
            "radio observatories, shielded from Earth's interference. The dark "
            "ages remain the least observed epoch in cosmic history."),
        "why_it_matters": (
            "The dark ages contain the initial conditions for the first stars, "
            "galaxies, and black holes - the seeds of all structure. The "
            "21-centimeter signal is potentially the richest cosmological dataset "
            "in existence, with more independent modes than the CMB. An confirmed "
            "anomaly there would be direct evidence of new physics in the early "
            "universe."),
        "sig_pointer": (
            "The Signature edition walks the 21-centimeter arithmetic: redshift to "
            "frequency mapping, the expected absorption depth, and the EDGES "
            "excess quantified."),
        "sig_solution": (
            "Assumptions: the standard thermal history gives the baseline "
            "21-centimeter signal and the SARAS non-confirmation is taken "
            "seriously. Reasoning: the observable is a single global spectrum, so "
            "the analysis must be ruthless about systematics - the EDGES episode "
            "showed how easily foregrounds and instrument effects mimic a signal. "
            "Proposed method: compute the standard-model global 21-centimeter "
            "spectrum from the thermal history, quantify exactly how much extra "
            "cooling the EDGES depth would require, and list the independent "
            "experiments (HERA power spectrum, lunar far-side global signal) that "
            "must agree before any anomaly is accepted. What would confirm new "
            "physics: two independent instruments with different systematics "
            "measuring the same anomalous depth and timing. What would kill the "
            "EDGES claim: HERA's power spectrum matching standard predictions at "
            "the corresponding redshifts. What this does NOT claim: it does not "
            "claim EDGES saw dark matter, does not claim the dark ages are "
            "understood, and does not claim any planned instrument is guaranteed "
            "to succeed."),
        "citations": [CIT_BOWMAN, CIT_SINGH],
        "demo_params": {"z": 20.0, "edges_depth_mk": 500.0, "standard_depth_mk": 200.0},
    },
    {
        "key": "giant-structures",
        "name": "Structures Too Large for the Universe",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("Quasar groups and galaxy walls spanning billions of light-years "
                    "exceed the scale at which the universe should be smooth. Do "
                    "they break the cosmological principle?"),
        "background": (
            "The cosmological principle - that the universe is homogeneous and "
            "isotropic on large scales - underpins all of cosmology, with the "
            "homogeneity scale measured near 370 megaparsecs. Yet the Huge Large "
            "Quasar Group, found in 2013, stretches 1.24 gigaparsecs; the Giant "
            "Arc of galaxies spans 3.3 billion light-years; the Big Ring is 1.3 "
            "billion light-years across. Their discoverers argue they are too "
            "large and too unlikely to be chance alignments. Critics counter that "
            "the structures were found by algorithms tuned to find them, that "
            "their statistical significance is overstated, and that the "
            "cosmological principle only requires statistical homogeneity, which "
            "can accommodate rare large fluctuations."),
        "why_it_matters": (
            "The cosmological principle is the foundation assumption of the "
            "standard model - if it fails, the Friedmann equations describing the "
            "universe's expansion need rethinking. Even if the structures are "
            "compatible with the model, they probe the extreme tail of structure "
            "formation. The debate is really about how cosmology handles rare "
            "events and a posteriori statistics."),
        "sig_pointer": (
            "The Signature edition walks the scale comparison: structure sizes "
            "versus the homogeneity scale, and the chance-alignment probability "
            "that decides the case."),
        "sig_solution": (
            "Assumptions: the reported structure sizes are correct and the "
            "homogeneity scale of 370 Mpc from fractal-dimension analyses is the "
            "right benchmark. Reasoning: the dispute is statistical at its core - "
            "a structure three times the homogeneity scale is either a real "
            "challenge or an expected rare fluctuation, and the two can be "
            "distinguished only by blind, pre-registered searches. Proposed "
            "method: compute the expected number of such structures in the "
            "standard model from mock catalogs, run the same detection algorithm "
            "blind on mocks and data, and compare counts; a statistically "
            "significant excess in the data is the only result that challenges "
            "the principle. What would confirm a genuine violation: multiple "
            "independent structures above the homogeneity scale found by blind "
            "searches at a rate the mocks cannot reproduce. What would kill the "
            "claims: blind reanalysis showing the structures dissolve or appear "
            "in mocks just as often. What this does NOT claim: it does not claim "
            "the principle is broken, does not claim the structures are unreal, "
            "and does not claim the detection algorithms are unbiased."),
        "citations": [CIT_CLOWES, CIT_YADAV],
        "demo_params": {"huge_lqg_gpc": 1.24, "homogeneity_mpc": 370.0},
    },
    {
        "key": "bh-information",
        "name": "The Black Hole Information Paradox",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("Black holes evaporate by Hawking radiation - but the radiation "
                    "looks thermal and featureless. Where does the information "
                    "about what fell in go?"),
        "background": (
            "In 1976 Stephen Hawking argued that black hole evaporation destroys "
            "information, violating quantum mechanics' unitarity. Decades of "
            "proposals followed: black hole complementarity, which says the "
            "information is both inside and outside depending on the observer; "
            "firewalls, which sacrifice the smooth horizon; and remnants. In 2019 "
            "the island formula, derived from holographic quantum gravity "
            "calculations, reproduced the Page curve - the expected pattern of "
            "information return - for certain theoretical black holes, the first "
            "computation to do so. But the calculation works in simplified models "
            "with extra mathematical machinery, and it does not say how the "
            "information physically gets out of a real astrophysical black hole. "
            "The paradox has evolved rather than resolved."),
        "why_it_matters": (
            "The paradox is the sharpest clash between general relativity and "
            "quantum mechanics - the two pillars of modern physics. Its resolution "
            "will likely reveal how spacetime itself emerges from quantum "
            "information. It has already spawned the holographic principle and "
            "much of modern quantum gravity."),
        "sig_pointer": (
            "The Signature edition walks the paradox quantitatively: Bekenstein-"
            "Hawking entropy, the Page time, and what the island calculation "
            "does and does not establish."),
        "sig_solution": (
            "Assumptions: Hawking's semiclassical calculation is correct as an "
            "approximation and unitarity holds in quantum gravity. Reasoning: the "
            "paradox can be stated as a counting problem - the radiation carries "
            "too little entropy to encode the infalling matter until the Page "
            "time, after which it must - so any resolution must specify when and "
            "how the information starts coming out. Proposed method: compute the "
            "Page time and the Bekenstein-Hawking entropy for astrophysical black "
            "holes, then audit each proposed resolution (complementarity, "
            "firewalls, islands, fuzzballs) against three requirements: reproduce "
            "the Page curve, preserve a smooth horizon for infalling observers, "
            "and derive from a concrete microscopic model rather than an "
            "assumption. What would confirm a resolution: a microscopic model "
            "that meets all three requirements and makes a distinct prediction - "
            "such as gravitational-wave echoes - that is then observed. What "
            "would kill the island program's claim to solve the paradox: a proof "
            "that its derivation cannot be extended to realistic black holes "
            "formed by collapse. What this does NOT claim: it does not claim the "
            "paradox is solved, does not claim firewalls exist, and does not "
            "claim information is preserved - that is the assumption under test."),
        "citations": [CIT_HAWKING, CIT_ALMHEIRI, CIT_AMPS],
        "demo_params": {"m_msun": 10.0},
    },
    {
        "key": "singularities",
        "name": "What Happens at a Singularity",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("General relativity predicts its own breakdown: infinite "
                    "density at the center of every black hole. What actually "
                    "happens where the equations fail?"),
        "background": (
            "Penrose's 1965 singularity theorems, recognized with the 2020 Nobel "
            "Prize, proved that gravitational collapse under general relativity "
            "inevitably produces singularities - regions where curvature and "
            "density become infinite and the theory stops making sense. Physicists "
            "take this as a signpost, not a description: quantum gravity must take "
            "over at the Planck scale. Candidate pictures include loop quantum "
            "gravity's bounce, where collapse rebounds into a new expanding "
            "region; string theory's fuzzballs, where the black hole is a "
            "horizonless tangle of strings with no interior singularity; and "
            "scenarios where the singularity is resolved into a regular quantum "
            "core. No observation can currently probe these scales - the nearest "
            "singularity is 26,000 light-years away behind an event horizon."),
        "why_it_matters": (
            "Singularities are where our best theory of gravity confesses "
            "ignorance - the frontier where quantum gravity must live. Whatever "
            "replaces them determines whether black holes have interiors at all, "
            "whether information survives, and possibly how universes begin. It "
            "is the deepest unsolved problem in gravitational physics."),
        "sig_pointer": (
            "The Signature edition walks the scale ladder: Schwarzschild radius "
            "for real black holes down to the Planck length, locating exactly "
            "where known physics ends."),
        "sig_solution": (
            "Assumptions: the singularity theorems hold within classical general "
            "relativity and quantum effects become important at the Planck scale. "
            "Reasoning: the honest statement of the problem is a scale comparison "
            "- the singularity is where curvature reaches the Planck scale, some "
            "sixty orders of magnitude beyond any tested regime - so proposals "
            "must be judged on what they predict at accessible scales, not on "
            "their Planck-scale storytelling. Proposed method: compute the "
            "curvature scales for stellar and supermassive black holes, identify "
            "the radius where each quantum-gravity proposal modifies the classical "
            "picture, and extract each proposal's observable consequences - "
            "gravitational-wave echoes, horizon-scale structure imaged by the "
            "Event Horizon Telescope, or Hawking-spectrum modifications. What "
            "would confirm a specific picture: a repeatable horizon-scale "
            "observation, such as echoes in merger ringdowns, matching one "
            "proposal's quantitative prediction. What would kill a proposal: its "
            "predicted deviations being ruled out by EHT imaging or LIGO data at "
            "the relevant precision. What this does NOT claim: it does not claim "
            "any quantum-gravity theory is correct, does not claim singularities "
            "are physical, and does not claim the interior is observable even in "
            "principle."),
        "citations": [CIT_PENROSE, CIT_MATHUR],
        "demo_params": {"m_msun_sgra": 4.3e6},
    },
    {
        "key": "eternal-inflation",
        "name": "Eternal Inflation and the Multiverse",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("Inflation may never end globally, spawning infinite bubble "
                    "universes - but a theory predicting everything predicts "
                    "nothing. Can the multiverse ever be tested?"),
        "background": (
            "Alan Guth proposed cosmic inflation in 1981 to solve the horizon and "
            "flatness problems; Andrei Linde and others realized that in most "
            "models inflation is eternal - it keeps going somewhere forever, "
            "budding off bubble universes with different properties. Our universe "
            "would be one bubble among infinitely many. The idea is mathematically "
            "natural but scientifically treacherous: with infinite universes, every "
            "possible observation occurs somewhere, and computing the probability "
            "of what we see requires a measure - a way of counting infinities - "
            "that no one agrees on. Critics argue it is untestable metaphysics; "
            "defenders point to possible signatures like bubble-collision imprints "
            "in the CMB or specific predictions from string-theory landscapes."),
        "why_it_matters": (
            "The multiverse question decides what kind of explanation cosmology "
            "is allowed to give: if our universe's properties are environmental "
            "accidents, the search for unique fundamental explanations ends. It "
            "is also the battleground for what counts as science - whether "
            "testability can be indirect and statistical rather than direct."),
        "sig_pointer": (
            "The Signature edition walks the measure problem: why infinite "
            "bubbles break probability, the e-fold arithmetic, and the testability "
            "criteria a multiverse claim must meet."),
        "sig_solution": (
            "Assumptions: inflation occurred and lasted at least the 50-60 e-folds "
            "needed to solve the horizon problem. Reasoning: the scientific "
            "content of eternal inflation is not the bubbles, which are "
            "unobservable by construction, but the measure problem - without an "
            "agreed way to count infinite universes, no prediction can be "
            "extracted, so the program's status should be judged by its progress "
            "on the measure, not its popularity. Proposed method: compute the "
            "e-fold requirements and the bubble nucleation rates for "
            "representative potentials, then audit each proposed measure "
            "(proper time, scale factor, causal patch) for whether it yields "
            "well-defined, cutoff-independent predictions for observables like "
            "the cosmological constant. What would confirm a scientific "
            "multiverse: a measure-independent prediction - such as a specific "
            "bubble-collision signature - that is then observed. What would kill "
            "the program's scientific status: a proof that all measures either "
            "diverge or depend on arbitrary cutoffs for every observable. What "
            "this does NOT claim: it does not claim the multiverse exists, does "
            "not claim it is unscientific, and does not claim any measure is "
            "correct."),
        "citations": [CIT_GUTH, CIT_LINDE],
        "demo_params": {"efolds_needed": 60.0},
    },
    {
        "key": "fate-universe",
        "name": "The Fate of the Universe",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Will the universe expand forever into cold darkness, tear "
                    "itself apart, or collapse and bounce? The ending is written "
                    "in the dark energy we do not understand."),
        "background": (
            "With the universe spatially flat and dark energy dominant, the "
            "default forecast is heat death: eternal accelerating expansion, "
            "stars burning out over 10^100 years, black holes evaporating, and a "
            "final equilibrium of cold dilute radiation. But the ending hinges on "
            "dark energy's true nature. If its equation of state is even slightly "
            "below -1 (phantom energy), expansion accelerates without bound and "
            "the Big Rip tears apart galaxies, stars, planets, and finally atoms "
            "in finite time. If dark energy decays or reverses, the universe could "
            "recollapse - possibly into a Big Crunch or a bouncing cosmology. The "
            "DESI hints of evolving dark energy have reopened every scenario that "
            "a pure cosmological constant had closed."),
        "why_it_matters": (
            "It is the last question: the destiny of everything. The answer is "
            "entangled with the nature of dark energy, the deepest problem in "
            "physics. And practically, each fate implies a different ultimate "
            "limit on life, computation, and survival - the final boundary "
            "condition for every far-future plan."),
        "sig_pointer": (
            "The Signature edition walks the fate decision tree: the equation-of-"
            "state parameter as the switch between Freeze, Rip, and Crunch, with "
            "timescales computed for each."),
        "sig_solution": (
            "Assumptions: the universe is spatially flat and general relativity "
            "holds on cosmic scales into the far future. Reasoning: the fate is "
            "controlled almost entirely by one number, the dark-energy "
            "equation-of-state w - so the problem becomes computing the outcome "
            "as a function of w and identifying which observations pin w down. "
            "Proposed method: compute the expansion history and key timescales "
            "(heat-death milestones, Big Rip time for representative phantom "
            "values, recollapse conditions) as functions of w, then map the "
            "current and projected DESI-era constraints on w onto the fate "
            "diagram to show which endings remain live. What would confirm heat "
            "death: w converging to exactly -1 with no evolution across all "
            "probes. What would kill it: a definitive measurement of w below -1 "
            "or of time evolution, promoting the Rip or dynamical scenarios. "
            "What this does NOT claim: it does not claim any fate is known, does "
            "not claim phantom energy exists, and does not claim the far-future "
            "extrapolation is more than conditional forecasting."),
        "citations": [CIT_RIESS98, CIT_DESI, CIT_CALDWELL],
        "demo_params": {"w": -1.0, "omega_lambda": 0.69, "h0": 70.0},
    },
]
