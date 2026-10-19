#!/usr/bin/env python3
"""Entries 18-26 (ladder ranks 18-26, Compounded/Advanced)."""

CIT_BEGELMAN = ("Begelman MC, Blandford RD, Rees MJ. Massive black hole binaries "
                "in active galactic nuclei. Nature; 1980.")
CIT_NANOGRAV = ("NANOGrav Collaboration. The NANOGrav 15-year data set: evidence "
                "for a gravitational-wave background. Astrophys J Lett; 2023.")
CIT_CEN = ("Cen R, Ostriker JP. Where are the baryons? Astrophys J; 1999.")
CIT_SHULL = ("Shull JM, Smith BD, Danforth CW. A perplexing census of the "
             "baryonic content of the Universe. Astrophys J; 2012.")
CIT_MACQUART = ("Macquart JP et al. A census of baryons in the Universe from "
                "localized fast radio bursts. Nature; 2020.")
CIT_KLYPIN = ("Klypin A et al. Where are the missing Galactic satellites? "
              "Astrophys J; 1999.")
CIT_BOYLAN = ("Boylan-Kolchin M, Bullock JS, Kaplinghat M. Too big to fail? "
              "Mon Not R Astron Soc; 2011.")
CIT_BULLOCK = ("Bullock JS, Boylan-Kolchin M. Small-scale challenges to the "
               "cold dark matter paradigm. Annu Rev Astron Astrophys; 2017.")
CIT_ZWICKY = ("Zwicky F. Die Rotverschiebung von extragalaktischen Nebeln. "
              "Helv Phys Acta; 1933.")
CIT_RUBIN = ("Rubin VC, Ford WK Jr. Rotation of the Andromeda nebula from a "
             "spectroscopic survey of emission regions. Astrophys J; 1970.")
CIT_LEE = ("Lee BW, Weinberg S. Cosmological lower bound on heavy-neutrino "
           "masses. Phys Rev Lett; 1977.")
CIT_PEC = ("Peccei RD, Quinn HR. CP conservation in the presence of "
           "pseudoparticles. Phys Rev Lett; 1977.")
CIT_PITROU = ("Pitrou C et al. Precision big bang nucleosynthesis with the "
              "PRIMAT code. Phys Rep; 2021.")
CIT_SPITE = ("Spite F, Spite M. Lithium abundance at the formation of the "
             "Galaxy. Astron Astrophys; 1982.")
CIT_VIELVA = ("Vielva P et al. Detection of non-Gaussianity in the WMAP 1-year "
              "data using spherical wavelets. Astrophys J; 2004.")
CIT_LAND = ("Land K, Magueijo J. The axis of evil. Phys Rev Lett; 2005.")
CIT_SZAPUDI = ("Szapudi I et al. Detection of a supervoid aligned with the cold "
               "spot of the cosmic microwave background. Mon Not R Astron Soc; 2015.")
CIT_RIESS = ("Riess AG et al. A comprehensive measurement of the local value of "
             "the Hubble constant. Astrophys J Lett; 2022.")
CIT_PLANCK = ("Planck Collaboration. Planck 2018 results: VI. Cosmological "
              "parameters. Astron Astrophys; 2020.")
CIT_NERONOV = ("Neronov A, Vovk I. Evidence for strong extragalactic magnetic "
               "fields from Fermi observations of TeV blazars. Science; 2010.")
CIT_DURRER = ("Durrer R, Neronov A. Cosmological magnetic fields: their "
              "generation, evolution and observation. Astron Astrophys Rev; 2013.")
CIT_SAKHAROV = ("Sakharov AD. Violation of CP invariance, C asymmetry, and "
                "baryon asymmetry of the universe. JETP Lett; 1967.")
CIT_FUKUGITA = ("Fukugita M, Yanagida T. Baryogenesis without grand unification. "
                "Phys Lett B; 1986.")

ENTRIES_C = [
    {
        "key": "final-parsec",
        "name": "The Final Parsec Problem",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("When galaxies merge, their central black holes should spiral "
                    "together and merge - but theory says the inspiral stalls about "
                    "a parsec apart. How do black hole binaries cross the final parsec?"),
        "background": (
            "Galaxy mergers are common, so binary supermassive black holes should be "
            "common too - and their mergers power the nanohertz gravitational-wave "
            "background. Dynamical friction brings the pair together efficiently down "
            "to about a parsec, where the binary ejects the nearby stars and empties "
            "its loss cone. Begelman, Blandford, and Rees pointed out in 1980 that "
            "with the stars gone, nothing extracts further orbital energy and the "
            "binary stalls. Proposed rescues include triaxial galaxy shapes that "
            "refill the loss cone, gas disks that drag the binary inward, and third "
            "black holes from subsequent mergers. In 2023 pulsar timing arrays "
            "including NANOGrav found evidence of the gravitational-wave background, "
            "suggesting binaries do merge - but the mechanism and timescale remain "
            "unmeasured."),
        "why_it_matters": (
            "Binary black hole mergers are the loudest gravitational-wave sources in "
            "the nanohertz band and the engines of the brightest quasars. If "
            "binaries stall, the universe should be full of stranded pairs - a "
            "testable prediction. The answer determines the merger rate that pulsar "
            "timing arrays and the future LISA mission will observe."),
        "sig_pointer": (
            "The Signature edition walks the timescale comparison: hardening rate, "
            "Hubble time, and which rescue mechanisms beat the clock."),
        "sig_solution": (
            "Assumptions: the loss-cone depletion calculation is correct for "
            "spherical galaxies and the NANOGrav signal is astrophysical. Reasoning: "
            "the problem is a race between the binary hardening timescale and the "
            "age of the universe, so each proposed rescue can be scored by whether "
            "it brings the merger time under a Hubble time for typical galaxy "
            "parameters. Proposed method: compute the stalling timescale for a grid "
            "of binary masses and mass ratios, then apply each rescue mechanism - "
            "triaxial loss-cone refilling, circumbinary gas-disk torques, triple "
            "interactions - with its published efficiency, and map which regions of "
            "parameter space merge in time. What would confirm a dominant mechanism: "
            "pulsar-timing measurements of the background spectrum matching that "
            "mechanism's predicted binary population. What would kill the stalling "
            "picture: direct imaging of a large population of parsec-scale binaries "
            "that have sat unmerged for billions of years. What this does NOT claim: "
            "it does not claim which mechanism wins, does not claim the NANOGrav "
            "signal is fully characterized, and does not claim gas disks are "
            "always present."),
        "citations": [CIT_BEGELMAN, CIT_NANOGRAV],
        "demo_params": {"m1_msun": 1.0e8, "m2_msun": 3.0e7, "separation_pc": 1.0},
    },
    {
        "key": "missing-baryons",
        "name": "The Missing Baryons",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("Big Bang nucleosynthesis and the cosmic microwave background "
                    "agree on how much ordinary matter the universe holds - but "
                    "censuses of stars and gas find only a fraction of it. Where is "
                    "the rest?"),
        "background": (
            "The cosmic baryon density is one of cosmology's best-measured numbers: "
            "about 4.9 percent of the universe's energy budget. Yet adding up stars, "
            "cold gas, and hot cluster gas accounts for only about half of it - and "
            "in individual galaxies like the Milky Way the shortfall is worse. In "
            "1999 Cen and Ostriker predicted the missing baryons hide as warm-hot "
            "intergalactic medium, million-degree filaments between galaxies too "
            "diffuse to glow. Searches in X-ray absorption and the Sunyaev-Zeldovich "
            "effect found pieces of it. Then in 2020 the Macquart relation - fast "
            "radio burst dispersion versus redshift - weighed all the electrons "
            "along the line of sight and found the baryons in the intergalactic "
            "medium, closing the cosmic census. The galactic-scale shortfall, the "
            "missing baryons around individual galaxies, remains open."),
        "why_it_matters": (
            "Baryons are the only matter we are made of - losing track of most of "
            "them was cosmology's bookkeeping embarrassment. The warm-hot medium "
            "also records the history of galactic winds and feedback: how galaxies "
            "breathe matter in and out. Completing the census tests whether our "
            "cosmic accounting is finally honest."),
        "sig_pointer": (
            "The Signature edition walks the baryon ledger: the cosmic density, the "
            "observed fractions, and the warm-hot reservoir that balances the books."),
        "sig_solution": (
            "Assumptions: the BBN and CMB baryon densities are correct and the "
            "Macquart-relation measurement is unbiased. Reasoning: the cosmic census "
            "is now essentially closed, so the remaining problem is the galactic "
            "halo scale - and it should be attacked as a mass-budget problem per "
            "galaxy mass bin. Proposed method: compute the expected baryon mass for "
            "halos from dwarf to cluster scale from the cosmic fraction, subtract "
            "the observed stars plus cold plus hot gas, and map the residual as a "
            "function of halo mass; then test whether feedback models eject exactly "
            "that residual in simulations. What would confirm the feedback picture: "
            "X-ray and ultraviolet absorption measurements finding the predicted "
            "warm-hot halo mass around galaxies of each mass. What would kill it: "
            "deep halo censuses finding the baryons were never missing - hidden in "
            "cold molecular gas or low-mass stars. What this does NOT claim: it "
            "does not claim the cosmic census is exact, does not claim feedback "
            "models are correct, and does not claim the Milky Way's own halo is "
            "measured."),
        "citations": [CIT_CEN, CIT_SHULL, CIT_MACQUART],
        "demo_params": {"omega_b": 0.049, "observed_fraction": 0.55},
    },
    {
        "key": "small-scale-crises",
        "name": "Dark Matter's Small-Scale Crises",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Cold dark matter predicts swarms of dwarf-galaxy satellites and "
                    "sharply peaked dark halos, but observations show fewer dwarfs "
                    "and flatter cores. Is the theory wrong, or is ordinary matter "
                    "to blame?"),
        "background": (
            "The cold dark matter model triumphs on cosmic scales, but three "
            "small-scale tensions emerged: the missing satellites problem (simulations "
            "predict far more dwarf satellites around the Milky Way than observed), "
            "the cusp-core problem (simulations predict steeply rising central "
            "densities while dwarf galaxies show flat cores), and too-big-to-fail "
            "(the most massive predicted subhalos are too dense to host any known "
            "dwarf). Two camps formed: one blames baryonic physics - supernova "
            "explosions blowing gas out and flattening cusps, ultraviolet background "
            "suppressing small galaxies - and the other modifies dark matter itself, "
            "with warm, self-interacting, or fuzzy dark matter. Modern "
            "hydrodynamical simulations with strong feedback reproduce many "
            "observations, but the debate is not settled."),
        "why_it_matters": (
            "These are the sharpest tests of the dark matter paradigm: if the "
            "tensions require new dark-matter physics, it would be the first "
            "observational handle on what dark matter is. If baryons explain "
            "everything, it validates our understanding of galaxy formation "
            "feedback. Either outcome is a major discovery."),
        "sig_pointer": (
            "The Signature edition walks the satellite-count comparison: predicted "
            "subhalos versus observed dwarfs, and the feedback energy budget that "
            "must flatten each cusp."),
        "sig_solution": (
            "Assumptions: the simulation predictions for dark-matter-only halos are "
            "correct and the Milky Way satellite census is substantially complete "
            "for the classical dwarfs. Reasoning: each crisis is a numbers mismatch "
            "that can be quantified - count the predicted subhalos, count the "
            "observed dwarfs, compute the feedback energy available per halo - so "
            "the baryonic explanation either balances the ledger or it does not. "
            "Proposed method: for each crisis, compute the quantitative gap (missing "
            "satellite count, cusp mass deficit, too-big-to-fail density excess) "
            "and compare against the maximum effect supernova feedback can produce "
            "given the observed stellar masses; where feedback falls short, test "
            "whether self-interacting dark matter with a specific cross-section "
            "closes the gap without breaking cluster-scale constraints. What would "
            "confirm the baryonic solution: ultra-faint dwarf discoveries completing "
            "the predicted count and measured cores matching feedback-only "
            "simulations. What would kill it: isolated field dwarfs with cores "
            "that no feedback budget can produce. What this does NOT claim: it "
            "does not claim feedback is sufficient, does not claim self-interacting "
            "dark matter exists, and does not claim the satellite census is complete."),
        "citations": [CIT_KLYPIN, CIT_BOYLAN, CIT_BULLOCK],
        "demo_params": {"predicted_subhalos": 500.0, "observed_dwarfs": 60.0},
    },
    {
        "key": "dark-matter-nature",
        "name": "The Nature of Dark Matter",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Something outweighs visible matter five to one and sculpts every "
                    "galaxy, yet no particle detector has caught it. What is dark "
                    "matter made of?"),
        "background": (
            "Fritz Zwicky found in 1933 that the Coma cluster moves too fast for its "
            "visible mass; Vera Rubin confirmed in the 1970s that spiral galaxies "
            "rotate too fast at their edges. Gravitational lensing and the cosmic "
            "microwave background agree: about 27 percent of the universe is dark "
            "matter. Candidates span 90 orders of magnitude in mass: WIMPs, weakly "
            "interacting massive particles whose predicted annihilation rate "
            "naturally gives the right cosmic abundance (the WIMP miracle); axions, "
            "ultralight particles from the Peccei-Quinn theory; sterile neutrinos; "
            "and primordial black holes. Decades of direct-detection experiments, "
            "including XENONnT, have found nothing, progressively squeezing the WIMP "
            "parameter space."),
        "why_it_matters": (
            "Dark matter is a quarter of the universe and we do not know what it "
            "is - the largest known unknown in physics. Its identity determines how "
            "galaxies formed, how structure grows, and whether new forces or "
            "particles await discovery. A detection would be a Nobel-level "
            "revolution; a confirmed non-detection of all candidates would be "
            "equally revolutionary."),
        "sig_pointer": (
            "The Signature edition walks the WIMP-miracle arithmetic: the annihilation "
            "cross-section that yields the observed abundance, and the exclusion "
            "plot that candidate models must survive."),
        "sig_solution": (
            "Assumptions: the cosmic dark matter density is 0.12 in units of h^2 "
            "and thermal freeze-out is the production mechanism for the WIMP "
            "benchmark. Reasoning: the thermal-relic calculation is one of the few "
            "places where a dark matter candidate makes a sharp numerical prediction "
            "- the required annihilation cross-section - so candidates can be "
            "admitted or rejected by arithmetic. Proposed method: compute the "
            "thermal-relic cross-section from the observed abundance, overlay the "
            "direct-detection exclusion curves and collider limits, and map the "
            "surviving parameter space for each candidate class (WIMP, axion, "
            "sterile neutrino, primordial black hole); then identify which upcoming "
            "experiment covers each surviving island. What would confirm a "
            "candidate: a direct-detection signal with the predicted annual "
            "modulation seen in two independent targets, or an axion haloscope "
            "signal confirmed at a second facility. What would kill the WIMP "
            "paradigm: exclusion of the full thermal-relic cross-section range with "
            "no signal. What this does NOT claim: it does not claim WIMPs exist, "
            "does not claim any candidate is favored, and does not claim detection "
            "is imminent."),
        "citations": [CIT_ZWICKY, CIT_RUBIN, CIT_LEE, CIT_PEC],
        "demo_params": {"omega_h2": 0.12, "sigma_v": 3.0e-26},
    },
    {
        "key": "lithium-problem",
        "name": "The Cosmic Lithium Problem",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Big Bang nucleosynthesis predicts three times more lithium-7 "
                    "than the oldest stars contain. Where did the lithium go?"),
        "background": (
            "Big Bang nucleosynthesis is one of cosmology's great triumphs: from "
            "one parameter, the baryon density, it predicts the primordial "
            "abundances of hydrogen, helium, and lithium. Hydrogen and helium match "
            "beautifully. But lithium-7 comes out about three times too high: "
            "theory says 4.7 parts per ten billion, while the Spite plateau - the "
            "constant lithium abundance in the oldest halo stars, measured since "
            "1982 - sits near 1.6. Proposed solutions split three ways: nuclear "
            "physics (an unmeasured resonance destroying beryllium-7, lithium's "
            "parent), stellar physics (lithium settling or burning inside the old "
            "stars themselves), or new physics in the early universe. Precision "
            "nuclear measurements have closed several loopholes without closing "
            "the gap."),
        "why_it_matters": (
            "BBN is the earliest testable epoch of the universe; a persistent "
            "factor-of-three failure means something is wrong in our picture of "
            "the first minutes. If the answer is stellar, it rewrites stellar "
            "evolution; if nuclear, it points to undiscovered resonances; if new "
            "physics, it could reveal decaying particles from the Big Bang itself."),
        "sig_pointer": (
            "The Signature edition walks the abundance ratio: predicted versus "
            "observed, and the depletion factor each solution class must supply."),
        "sig_solution": (
            "Assumptions: the Spite plateau value is the primordial abundance "
            "depleted by a uniform stellar factor, and the BBN prediction with "
            "the Planck baryon density is correct. Reasoning: the discrepancy is "
            "a single number - a factor of about three - so every proposed "
            "solution must quantitatively supply exactly that factor through a "
            "mechanism that leaves hydrogen and helium untouched. Proposed method: "
            "compute the required depletion factor from the observed ratio, then "
            "test each solution class - nuclear destruction channels, stellar "
            "diffusion and mixing models, decaying-particle scenarios - for "
            "whether it delivers that factor while preserving the successful "
            "deuterium and helium predictions. What would confirm the stellar "
            "solution: a measured trend of lithium with stellar parameters "
            "matching diffusion models across many halo stars. What would kill a "
            "nuclear solution: laboratory measurement of the relevant cross-"
            "sections at BBN energies showing no enhancement. What this does NOT "
            "claim: it does not claim the answer is stellar, does not claim new "
            "physics is needed, and does not claim the plateau is truly flat."),
        "citations": [CIT_PITROU, CIT_SPITE],
        "demo_params": {"li_predicted": 4.7e-10, "li_observed": 1.6e-10},
    },
    {
        "key": "cmb-anomalies",
        "name": "Anomalies in the Cosmic Microwave Background",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("The cosmic microwave background is almost perfectly uniform - "
                    "but it carries a Cold Spot, a preferred axis, and a lopsided "
                    "hemisphere that the standard model did not predict."),
        "background": (
            "The CMB's temperature fluctuations match the standard cosmological "
            "model exquisitely - except for a handful of large-scale oddities. The "
            "Cold Spot, found in 2004, is a 5-degree patch about 70 microkelvin "
            "colder than average. The 'axis of evil' aligns the quadrupole and "
            "octopole patterns along a preferred direction. One hemisphere of the "
            "sky has slightly stronger fluctuations than the other. Proposed "
            "explanations range from a giant supervoid (the integrated "
            "Sachs-Wolfe effect), to cosmic textures or bubble-universe collisions, "
            "to the sobering possibility that they are statistical flukes "
            "amplified by looking at the data after the fact - the look-elsewhere "
            "effect. Planck confirmed the anomalies are real features of the sky; "
            "whether they are real features of physics is undecided."),
        "why_it_matters": (
            "The CMB is our baby picture of the universe; unexplained features in "
            "it could be fingerprints of new physics - cosmic defects, a "
            "multiverse collision, or a breakdown of statistical isotropy. If they "
            "are flukes, understanding why protects cosmology from chasing phantoms. "
            "Either way, they test the foundations of the standard model."),
        "sig_pointer": (
            "The Signature edition walks the significance arithmetic: the Cold "
            "Spot's depth and size against Gaussian expectations, and the "
            "look-elsewhere correction."),
        "sig_solution": (
            "Assumptions: the Planck maps are free of foreground contamination at "
            "the relevant scales and the standard model's Gaussian prediction is "
            "the correct null hypothesis. Reasoning: anomaly claims live or die on "
            "proper statistics - the look-elsewhere effect must be priced in before "
            "any physical explanation is entertained. Proposed method: compute the "
            "naive significance of each anomaly, then apply the full look-elsewhere "
            "correction for the number of comparable tests the community has run, "
            "and rank the anomalies by corrected significance; only survivors above "
            "a pre-registered threshold earn physical modeling. What would confirm "
            "a physical origin: an independent dataset - such as large-scale "
            "structure or polarization - showing the same preferred direction or "
            "the supervoid with the required depth. What would kill the Cold Spot "
            "as physics: a corrected significance below 2 sigma, or a foreground "
            "systematic reproducing it. What this does NOT claim: it does not "
            "claim any anomaly is new physics, does not claim they are all flukes, "
            "and does not claim the supervoid explanation is ruled out."),
        "citations": [CIT_VIELVA, CIT_LAND, CIT_SZAPUDI],
        "demo_params": {"cold_spot_uk": -70.0, "spot_deg": 5.0, "cmb_rms_uk": 110.0},
    },
    {
        "key": "hubble-tension",
        "name": "The Hubble Tension",
        "group": "Advanced",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "problem": ("The universe's expansion rate measured from nearby stars is "
                    "about 73 km/s/Mpc; inferred from the early universe it is "
                    "about 67. The 5-sigma disagreement will not go away. Which "
                    "side is wrong - or is the model?"),
        "background": (
            "The SH0ES team, using Cepheid variable stars and supernovae as a "
            "distance ladder, finds 73.0 plus or minus 1.0 km/s/Mpc. The Planck "
            "satellite, fitting the standard cosmological model to the cosmic "
            "microwave background, infers 67.4 plus or minus 0.5. The gap has "
            "survived a decade of scrutiny: JWST re-observed the key Cepheids in "
            "2024 and confirmed the local calibration, while independent local "
            "methods - gravitational lensing time delays, megamasers, surface "
            "brightness fluctuations - mostly side with the higher value. Proposed "
            "solutions divide into early-universe fixes (extra radiation or early "
            "dark energy changing the sound horizon) and late-universe fixes "
            "(evolving dark energy), plus the possibility of an unrecognized "
            "systematic error."),
        "why_it_matters": (
            "The Hubble constant sets the age, size, and expansion history of the "
            "universe - it is cosmology's most fundamental number. A real "
            "tension means the standard model is missing an ingredient, possibly "
            "new physics in the first instants or a new component of the cosmos. "
            "Resolving it is the field's highest-profile open problem."),
        "sig_pointer": (
            "The Signature edition walks the tension arithmetic: the sigma "
            "calculation, the sound-horizon lever, and the early-versus-late "
            "solution scorecard."),
        "sig_solution": (
            "Assumptions: both measurements' quoted uncertainties are honest and "
            "the JWST Cepheid cross-check stands. Reasoning: the tension is a "
            "single number - about 5 sigma - and any proposed solution must move "
            "one side by that full amount without breaking the half-dozen other "
            "datasets each side fits. Proposed method: compute the tension "
            "significance from the published values, then for each proposed "
            "solution (early dark energy, extra relativistic species, evolving "
            "dark energy, local void) compute how far it shifts H0 and score it "
            "against the collateral damage to CMB, BAO, and supernova fits. What "
            "would confirm new physics: an early-universe modification that raises "
            "the CMB-inferred H0 to 73 while keeping all other fits intact. What "
            "would kill the crisis: a discovered systematic in the distance ladder "
            "or the CMB analysis that moves either side by 5 sigma. What this does "
            "NOT claim: it does not claim new physics is required, does not claim "
            "any proposed solution works, and does not claim the tension will "
            "survive the next generation of data."),
        "citations": [CIT_RIESS, CIT_PLANCK],
        "demo_params": {"h0_local": 73.0, "h0_local_err": 1.0, "h0_cmb": 67.4, "h0_cmb_err": 0.5},
    },
    {
        "key": "cosmic-magnetism",
        "name": "The Origin of Cosmic Magnetic Fields",
        "group": "Advanced",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("Magnetic fields thread every galaxy and galaxy cluster, and "
                    "even the voids between them may be magnetized. Where did the "
                    "universe's magnetism come from?"),
        "background": (
            "Galaxies host microgauss-strength fields coherent over thousands of "
            "light-years; clusters host similar fields over millions. The standard "
            "story is the galactic dynamo: a tiny seed field amplified by rotating, "
            "turbulent gas over billions of years. But dynamos need a seed, and "
            "observations of distant blazars suggest even intergalactic voids carry "
            "fields around 10^-16 gauss - far from any galaxy that could have "
            "seeded them. Candidate primordial origins include magnetic fields "
            "generated during inflation or at the electroweak phase transition. "
            "Whether the void fields are truly primordial or were expelled from "
            "galaxies by ancient outflows is actively debated."),
        "why_it_matters": (
            "Magnetic fields shape star formation, cosmic-ray propagation, and "
            "galaxy evolution - yet their ultimate origin is unknown. A primordial "
            "field would be a relic of the universe's first fractions of a second, "
            "a fossil of inflation or phase transitions. It would also affect how "
            "the first stars and galaxies assembled."),
        "sig_pointer": (
            "The Signature edition walks the dynamo arithmetic: seed strength, "
            "amplification factor, and the void-field measurement that challenges "
            "astrophysical origins."),
        "sig_solution": (
            "Assumptions: the blazar-derived lower bounds on void fields are "
            "correct and dynamo theory's amplification rates apply to young "
            "galaxies. Reasoning: the problem reduces to a seed budget - compute "
            "the weakest seed a dynamo can amplify to observed strengths in the "
            "available time, and check whether astrophysical batteries can supply "
            "it. Proposed method: compute the required seed field for galaxies at "
            "each redshift given dynamo growth rates, compare against the maximum "
            "seed from astrophysical processes (Biermann battery, stellar "
            "outflows), and identify the redshift or environment where "
            "astrophysical seeds fall short - that shortfall is the quantitative "
            "case for a primordial field. What would confirm a primordial origin: "
            "void fields measured well above any outflow-transport model with a "
            "spectrum matching inflationary predictions. What would kill it: a "
            "demonstrated transport mechanism carrying galactic fields into voids "
            "at the observed strengths. What this does NOT claim: it does not "
            "claim void fields are confirmed, does not claim dynamos are fully "
            "understood, and does not claim a specific primordial mechanism."),
        "citations": [CIT_NERONOV, CIT_DURRER],
        "demo_params": {"b_observed_g": 1.0e-6, "growth_efolds": 30.0, "b_void_g": 1.0e-16},
    },
    {
        "key": "antimatter-asymmetry",
        "name": "Why the Universe Contains Matter Instead of Nothing",
        "group": "Advanced",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("The Big Bang should have made equal matter and antimatter, "
                    "which would have annihilated completely. Instead, one extra "
                    "quark in ten billion survived - and built everything. Why?"),
        "background": (
            "The universe's baryon-to-photon ratio is measured at 6.1 parts per ten "
            "billion - the tiny excess of matter over antimatter. In 1967 Andrei "
            "Sakharov laid out the three required conditions for generating such an "
            "asymmetry: baryon-number violation, charge-parity violation, and "
            "departure from thermal equilibrium. The Standard Model contains all "
            "three in principle but in practice produces an asymmetry ten billion "
            "times too small. Leading proposals include leptogenesis - an asymmetry "
            "in neutrinos converted to baryons (Fukugita and Yanagida, 1986) - and "
            "electroweak baryogenesis during the universe's phase transition. "
            "Searches for antimatter galaxies and cosmic antihelium have found "
            "nothing definitive; the asymmetry is a fact awaiting its mechanism."),
        "why_it_matters": (
            "This is the reason anything exists at all. The mechanism behind the "
            "asymmetry is almost certainly physics beyond the Standard Model - "
            "its discovery would rank with the Higgs. It connects the smallest "
            "scales (neutrino masses, CP violation) to the largest fact about the "
            "cosmos: that there is something rather than nothing."),
        "sig_pointer": (
            "The Signature edition walks the asymmetry arithmetic: the measured "
            "eta, the Standard Model shortfall, and the Sakharov-condition "
            "checklist each candidate must pass."),
        "sig_solution": (
            "Assumptions: the measured baryon-to-photon ratio is primordial and "
            "no large antimatter regions exist. Reasoning: Sakharov's conditions "
            "turn the problem into a checklist - any proposed mechanism must "
            "quantitatively produce eta of 6.1e-10, and the Standard Model's "
            "ten-billion-fold shortfall is the number to beat. Proposed method: "
            "compute the predicted asymmetry for each candidate mechanism "
            "(leptogenesis with measured neutrino parameters, electroweak "
            "baryogenesis, Affleck-Dine) and score them on the three Sakharov "
            "conditions plus testability - which makes a prediction a current or "
            "planned experiment can check. What would confirm leptogenesis: "
            "measurement of CP violation in neutrino oscillations at the strength "
            "the mechanism requires, plus a seesaw-scale consistent with the "
            "asymmetry. What would kill a candidate: a parameter measurement "
            "(Higgs mass, neutrino mixing) that closes its viable window. What "
            "this does NOT claim: it does not claim leptogenesis is correct, does "
            "not claim the Standard Model cannot be extended to work, and does "
            "not claim the asymmetry was generated at any specific epoch."),
        "citations": [CIT_SAKHAROV, CIT_FUKUGITA],
        "demo_params": {"eta": 6.1e-10, "sm_shortfall": 1.0e10},
    },
]
