#!/usr/bin/env python3
"""Entries for The Unsolved Climate Science Database (34 problems) and its
Signature edition. Both halves cover the SAME 34 famous unsolved climate
science problems, ladder-ordered by accessibility (ladder_rank 1-34).

Public halves: real, fact-checked problems - cloud feedback sign and
magnitude, the exact value of climate sensitivity, tipping-point thresholds,
aerosol forcing uncertainty, ocean heat uptake rates, regional prediction
limits, ice-sheet collapse rates, decadal prediction skill, carbon-cycle
feedbacks, extreme-event attribution, and the rest - each with problem,
background, why-it-matters, and a short pointer to the Signature proposed
solution.

Signature halves: the same 34 problems through the Signature lens, titles
suffixed " (Signature Edition)", src 'signature', every signature_solution
opening with the EXACT label "Signature-generated proposed solution - not
established science", and never claiming proof or peer acceptance.

Honesty rule (throughout): the problems are OPEN in established science;
Signature proposals are proposed paths, labeled as such.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_climate_science.py). Every demo is a
solution-explorer walkthrough: interactive steps, adjustable assumptions,
real computed values, tight-bounds asserts (never float exact-equality),
a confirm/refute panel, and the OK marker.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_LABEL = "Signature-generated proposed solution - not established science."

SIG_TAIL = ("Signature editions carry his original proposed solution "
            "approaches to each unsolved problem - clearly labeled "
            "Signature-generated proposed solutions, never presented as "
            "established science or peer-accepted results.")

CIT_BASE = [
    "Intergovernmental Panel on Climate Change. Climate Change 2021: The "
    "Physical Science Basis. Contribution of Working Group I to the Sixth "
    "Assessment Report (AR6 WGI). Cambridge University Press; 2021.",
    "Intergovernmental Panel on Climate Change. Climate Change 2022: Impacts, "
    "Adaptation and Vulnerability. Contribution of Working Group II to AR6. "
    "Cambridge University Press; 2022.",
]

ENTRIES = [
    # ------------------------------------------------- 1 FOUNDATIONS
    {
        "key": "co2-warming",
        "name": "Why Adding CO2 Warms the Planet",
        "group": "Foundations",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "problem": ("The greenhouse effect is settled physics, but the "
                    "unsolved part is quantitative, not qualitative: exactly "
                    "how much warming follows from each added increment of "
                    "CO2 once every feedback in the system responds, and why "
                    "simple laboratory spectroscopy scales up to a whole "
                    "planet without the accounting breaking."),
        "background": ("Joseph Fourier described the atmosphere's heat-trapping "
                       "role in 1824, John Tyndall measured the infrared "
                       "absorption of CO2 and water vapor in 1859, and Svante "
                       "Arrhenius made the first quantitative estimate in 1896 "
                       "that doubling CO2 would warm Earth by about 5 to 6 "
                       "degrees Celsius. Modern satellite instruments measure "
                       "the exact spectral bands where CO2 absorbs outgoing "
                       "longwave radiation, and the no-feedback warming from "
                       "doubling CO2 - the Planck response - is computed at "
                       "roughly 1.2 degrees Celsius. The open question begins "
                       "where that clean physics ends: the real planet adds "
                       "water vapor, clouds, ice, and circulation changes that "
                       "multiply the bare response by a factor that is still "
                       "only bounded, not pinned down."),
        "why_it_matters": ("Every climate projection, every emissions budget, "
                           "and every policy target rests on the quantitative "
                           "link between CO2 and temperature. If the multiplier "
                           "is near the low end of estimates, the remaining "
                           "carbon budget for 1.5 degrees is several times "
                           "larger than if it sits at the high end - the "
                           "difference between decades of adjustment time and "
                           "an almost closed window."),
        "sig_pointer": ("The Signature edition proposes a laboratory-to-planet "
                        "accounting walkthrough that decomposes the multiplier "
                        "into independently testable feedback ledgers. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the Planck response of "
                     "about 1.2 C per CO2 doubling is the correct no-feedback "
                     "baseline; (2) each feedback can be scored as a gain "
                     "factor from observations, not only from models; (3) the "
                     "total multiplier is the product of measured gains, not "
                     "a fitted parameter. Reasoning path: start from Tyndall "
                     "bench spectroscopy, add one feedback ledger at a time - "
                     "water vapor from satellite humidity trends, ice-albedo "
                     "from observed Arctic reflectivity loss, lapse-rate from "
                     "radiosonde profiles, clouds from the satellite cloud "
                     "record - and demand that the product of the ledgers "
                     "reproduce the observed 20th-century warming within "
                     "measurement uncertainty. Proposed mechanism: a "
                     "'feedback ledger' method that treats each feedback as "
                     "an audited account, so a future correction to one ledger "
                     "(say, clouds) revises the total without rebuilding the "
                     "whole theory. What would confirm it: the ledger product "
                     "matches observed warming AND predicts the next decade's "
                     "warming rate before it happens. What would kill it: any "
                     "single ledger whose observed gain contradicts the "
                     "product, or a decade of warming outside the ledger "
                     "bounds. What it does NOT claim: proof of any exact "
                     "sensitivity value, or that models are unnecessary - the "
                     "ledger is a check on models, not a replacement."),
        "key_points": [
            "CO2 absorbs outgoing infrared radiation in specific spectral bands measured directly by satellites.",
            "The no-feedback Planck response to doubling CO2 is about 1.2 C.",
            "Feedbacks - water vapor, clouds, ice-albedo, lapse rate - multiply the bare response.",
            "The total multiplier is bounded by observations but not pinned to a single value.",
        ],
        "requirements": [
            "Independent observational scoring of each feedback gain.",
            "A ledger whose product reproduces 20th-century warming within uncertainty.",
            "A successful out-of-sample prediction of the next decade's warming rate.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (the Earth's energy budget, climate feedbacks, and climate sensitivity)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "warming per CO2 doubling", "unit": "C",
            "calc": "gain", "planck": 1.2,
            "assumptions": [("net feedback factor f", 0.61, [0.0, 0.3, 0.61, 0.70])],
            "formula": "warming = planck_C / (1 - f)",
            "checks": [((0.0,), 1.2, 0.001), ((0.61,), 3.0769, 0.002), ((0.70,), 4.0, 0.001)],
            "steps": [
                "Step 1: fix the no-feedback baseline from laboratory spectroscopy (Planck response, about 1.2 C per doubling).",
                "Step 2: score each feedback as a gain factor from observations, not from model tuning.",
                "Step 3: combine gains with the feedback equation warming = baseline / (1 - f).",
                "Step 4: demand the product reproduce observed 20th-century warming within uncertainty.",
                "Step 5: issue the out-of-sample prediction for the coming decade and wait.",
            ],
            "confirm": [
                "Ledger product matches observed warming within measurement uncertainty.",
                "The decade-ahead warming-rate prediction lands inside the ledger bounds.",
            ],
            "refute": [
                "Any single feedback ledger whose observed gain contradicts the product.",
                "A decade of observed warming outside the ledger bounds.",
            ],
            "note": "Feedback-gain explorer for the CO2 warming multiplier.",
        },
    },
    {
        "key": "equilibrium-sensitivity",
        "name": "Equilibrium Climate Sensitivity: How Much Warming per CO2 Doubling",
        "group": "Foundations",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "problem": ("Equilibrium climate sensitivity (ECS) - the eventual "
                    "global warming after CO2 doubles and the deep ocean "
                    "catches up - is the single most cited number in climate "
                    "science, and after fifty years of research its exact "
                    "value is still not known. The IPCC AR6 likely range is "
                    "2.5 to 4.0 C with a best estimate of 3.0 C, but values "
                    "below 2 and above 5 cannot be fully ruled out by every "
                    "line of evidence."),
        "background": ("The 1979 Charney Report gave 1.5 to 4.5 C, a range "
                       "that survived nearly unchanged for four decades - a "
                       "famous embarrassment and a famous stability. Four "
                       "independent lines of evidence now constrain it: the "
                       "instrumental warming record, paleoclimate data from "
                       "ice ages and hothouse periods, process-level feedback "
                       "studies, and emergent constraints from model ensembles. "
                       "AR6 combined them to narrow the likely range to 2.5 "
                       "to 4.0 C and the very likely range to 2.0 to 5.0 C. "
                       "The newest generation of climate models (CMIP6) "
                       "spans an even wider range, with several 'hot models' "
                       "above 5 C that most evidence now disfavors. The "
                       "puzzle: independent methods agree on the range but "
                       "each carries structural assumptions the others do "
                       "not share."),
        "why_it_matters": ("ECS sets the long-run destination for any "
                           "stabilized CO2 level. A world with ECS of 2 C can "
                           "stabilize near 2 C of warming at roughly double "
                           "the CO2 of a world with ECS of 4 C - the entire "
                           "architecture of carbon budgets, net-zero dates, "
                           "and adaptation planning pivots on this number."),
        "sig_pointer": ("The Signature edition proposes a four-witness "
                        "tribunal method that forces the independent evidence "
                        "lines to cross-examine each other. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the four evidence lines "
                     "(instrumental, paleoclimate, process, emergent) are "
                     "genuinely independent enough to cross-check; (2) each "
                     "line's structural assumptions can be listed explicitly; "
                     "(3) agreement produced by shared hidden assumptions "
                     "does not count as confirmation. Reasoning path: lay the "
                     "four witnesses side by side, extract each one's "
                     "assumption list, and strike any agreement that traces "
                     "to a shared assumption (for example, aerosol forcing "
                     "estimates used by both the instrumental and process "
                     "lines). The surviving agreement is the honest "
                     "constraint. Proposed mechanism: a 'tribunal table' that "
                     "scores each evidence line on independence, assumption "
                     "transparency, and out-of-sample skill, then combines "
                     "only the independent remainder. What would confirm it: "
                     "the tribunal's narrowed range predicts an independent "
                     "future observation (for instance, the warming implied "
                     "by a volcanic cooling event of Pinatubo scale). What "
                     "would kill it: discovery that the surviving agreement "
                     "still shares a hidden assumption, or a new evidence "
                     "line that the tribunal cannot accommodate. What it does "
                     "NOT claim: a new exact ECS value, or that any existing "
                     "estimate is wrong - it is a method for honest "
                     "combination, not a rival number."),
        "key_points": [
            "ECS: eventual warming after CO2 doubling, deep ocean equilibrated.",
            "AR6 likely range 2.5-4.0 C, best estimate 3.0 C; very likely 2.0-5.0 C.",
            "The 1979 Charney range (1.5-4.5 C) stood for 40 years.",
            "Four evidence lines: instrumental, paleoclimate, process, emergent constraints.",
            "Several CMIP6 'hot models' exceed 5 C and are disfavored by most evidence.",
        ],
        "requirements": [
            "Explicit assumption lists for each evidence line.",
            "A combination rule that discounts shared hidden assumptions.",
            "An out-of-sample prediction (e.g. response to a large volcanic event).",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (climate sensitivity assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "equilibrium warming at CO2 doubling", "unit": "C",
            "calc": "gain", "planck": 1.2,
            "assumptions": [("net feedback factor f", 0.60, [0.52, 0.60, 0.70])],
            "formula": "ECS = planck_C / (1 - f); f=0.52->2.5C, f=0.60->3.0C, f=0.70->4.0C",
            "checks": [((0.52,), 2.5, 0.001), ((0.60,), 3.0, 0.001), ((0.70,), 4.0, 0.001)],
            "steps": [
                "Step 1: list the four evidence lines and their ECS implications.",
                "Step 2: extract each line's structural assumptions explicitly.",
                "Step 3: strike agreement that traces to shared hidden assumptions.",
                "Step 4: combine only the independent remainder into the tribunal range.",
                "Step 5: test the range against an out-of-sample event.",
            ],
            "confirm": [
                "Tribunal range predicts the cooling-and-recovery of a Pinatubo-scale eruption.",
                "A new independent evidence line lands inside the tribunal range.",
            ],
            "refute": [
                "The surviving agreement is found to share a hidden assumption.",
                "Observed warming under known forcing exits the tribunal range.",
            ],
            "note": "Four-witness tribunal explorer mapping feedback factors to the AR6 ECS range.",
        },
    },
    {
        "key": "warming-slowdown",
        "name": "The Early-2000s Warming Slowdown",
        "group": "Foundations",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "problem": ("Between roughly 1998 and 2012, the rise in global "
                    "surface temperature slowed markedly even as greenhouse "
                    "gases kept accumulating - the so-called 'hiatus' or "
                    "'pause'. The slowdown was real in the surface record, "
                    "and explaining exactly how much of it was ocean heat "
                    "rearrangement, how much was natural variability, and how "
                    "much was forcing (volcanoes, solar dip, aerosols) is "
                    "still quantitatively unsettled."),
        "background": ("The period became one of the most argued-over "
                       "episodes in climate science: skeptics cited it as "
                       "evidence models overpredict warming, while researchers "
                       "showed the oceans - especially the Pacific - were "
                       "absorbing heat at an accelerated rate, with strengthened "
                       "Pacific trade winds pushing warm surface water down. "
                       "Later analyses found the slowdown was partly an "
                       "artifact of incomplete Arctic coverage and measurement "
                       "changes (the shift from ship to buoy sea-surface "
                       "temperatures), and corrected records show more warming "
                       "than first reported. But the partition - what "
                       "fraction belongs to internal variability versus "
                       "forcing versus data artifacts - remains model- and "
                       "dataset-dependent, and the episode exposed how "
                       "sensitive decadal trends are to start and end dates."),
        "why_it_matters": ("The slowdown episode is the template for every "
                           "future claim that 'warming has stopped'. A "
                           "quantitative, agreed partition of its causes is "
                           "the difference between a durable scientific "
                           "answer and a debate that replays every decade."),
        "sig_pointer": ("The Signature edition proposes a three-ledger "
                        "partition audit - ocean, forcing, artifacts - with "
                        "each ledger scored independently. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the surface record, "
                     "ocean heat content, and forcing histories are "
                     "independent enough to triangulate; (2) internal "
                     "variability has recognizable fingerprints (Pacific "
                     "trade-wind strength, ocean heat rearrangement); (3) "
                     "data artifacts can be bounded by comparing dataset "
                     "versions. Reasoning path: build three ledgers - heat "
                     "moved into the ocean (from ocean heat content), forcing "
                     "deficit (volcanic, solar, aerosol histories), and "
                     "measurement artifacts (dataset-version differences) - "
                     "and require their sum to equal the gap between expected "
                     "and observed surface warming. Proposed mechanism: a "
                     "partition audit that assigns every tenth of a degree of "
                     "the slowdown to a ledger, with uncertainties that must "
                     "overlap the total. What would confirm it: the three "
                     "ledgers sum to the observed gap within uncertainty, and "
                     "the same audit applied to other decades produces no "
                     "phantom slowdowns. What would kill it: ledgers that "
                     "refuse to sum without an unexplained residual, or "
                     "dataset versions that move the artifact ledger beyond "
                     "its bounds. What it does NOT claim: that the slowdown "
                     "disproves long-term warming - the audit assumes the "
                     "long-term trend and partitions only the decadal "
                     "deviation."),
        "key_points": [
            "Surface warming slowed ~1998-2012 while greenhouse gases kept rising.",
            "Pacific trade-wind strengthening pushed heat into the deeper ocean.",
            "Later dataset corrections (Arctic coverage, ship-buoy shift) raised the trend.",
            "The exact partition among ocean, forcing, and artifacts is still debated.",
            "Decadal trends are highly sensitive to chosen start and end dates.",
        ],
        "requirements": [
            "Independent ocean-heat-content, forcing, and dataset-version ledgers.",
            "Ledgers that sum to the observed expectation gap within uncertainty.",
            "No phantom slowdowns when the audit is run on other decades.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 3 (human influence on the climate system); Chapter 9 (ocean)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "explained fraction of the slowdown gap", "unit": "fraction",
            "calc": "sum", "base": 1.0,
            "assumptions": [("ocean rearrangement share", 0.5, [0.3, 0.5, 0.7]),
                            ("forcing deficit share", 0.2, [0.1, 0.2, 0.3]),
                            ("dataset artifact share", 0.2, [0.1, 0.2, 0.3])],
            "formula": "gap_explained = ocean + forcing + artifact (must total ~1.0)",
            "checks": [((0.5, 0.2, 0.2), 0.9, 0.001), ((0.7, 0.3, 0.3), 1.3, 0.001)],
            "steps": [
                "Step 1: define the gap between expected and observed 1998-2012 surface warming.",
                "Step 2: score the ocean ledger from ocean heat content records.",
                "Step 3: score the forcing ledger from volcanic, solar, and aerosol histories.",
                "Step 4: score the artifact ledger from dataset-version differences.",
                "Step 5: require the three ledgers to sum to the gap within uncertainty.",
            ],
            "confirm": [
                "The three ledgers sum to the observed gap within uncertainty.",
                "Running the audit on other decades yields no phantom slowdowns.",
            ],
            "refute": [
                "An unexplained residual remains after all three ledgers are scored.",
                "Dataset versions move the artifact ledger outside its stated bounds.",
            ],
            "note": "Three-ledger partition audit of the early-2000s warming slowdown.",
        },
    },
    {
        "key": "cloud-feedback",
        "name": "Cloud Feedback: The Biggest Climate Wildcard",
        "group": "Foundations",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "problem": ("Clouds both cool the planet (reflecting sunlight) and "
                    "warm it (trapping infrared), and which effect wins as "
                    "the world warms is the largest single uncertainty in "
                    "climate sensitivity. The AR6 assessed net cloud feedback "
                    "at +0.42 W/m2 per degree - positive, amplifying warming - "
                    "but with an uncertainty range spanning from slightly "
                    "negative (-0.10) to strongly positive (+0.94). Its sign "
                    "and magnitude remain the biggest wildcard."),
        "background": ("Cloud feedback has topped the uncertainty list since "
                       "the Charney Report. Low marine stratocumulus clouds "
                       "off the western coasts of continents are the key "
                       "battleground: if warming thins them, more sunlight "
                       "reaches the surface (positive feedback); if they "
                       "thicken, the opposite. Satellite records (CERES, "
                       "MODIS, CloudSat) now span two decades, and recent "
                       "high-resolution modeling plus observational "
                       "constraints have shifted the assessed central value "
                       "positive - but the range still admits a near-zero or "
                       "slightly negative feedback. The 'hot models' of CMIP6 "
                       "owe much of their high sensitivity to strongly "
                       "positive cloud feedbacks that observations struggle "
                       "to confirm."),
        "why_it_matters": ("Cloud feedback alone spans most of the ECS "
                           "uncertainty range. Settling whether it is +0.1 or "
                           "+0.9 W/m2/K is nearly the same as settling "
                           "climate sensitivity itself - and with it, the "
                           "century's carbon budgets."),
        "sig_pointer": ("The Signature edition proposes a cloud-type ledger "
                        "that scores each cloud regime separately from "
                        "satellite records. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) different cloud regimes "
                     "(marine stratocumulus, trade cumulus, deep convective "
                     "anvils, high cirrus) have separable feedback signs "
                     "measurable from satellites; (2) two decades of CERES "
                     "and MODIS records are long enough to score regime "
                     "trends; (3) regimes combine by area-weighted sum. "
                     "Reasoning path: decompose the net feedback into "
                     "regime ledgers, score each from observed "
                     "cloud-radiative-effect trends per degree of local "
                     "warming, and sum with area weights - so the answer is a "
                     "transparent table, not a model parameter. Proposed "
                     "mechanism: a regime-ledger table where any researcher "
                     "can see which cloud type carries the positive verdict "
                     "and challenge that single row. What would confirm it: "
                     "the ledger sum matches the AR6 central value AND each "
                     "row's sign is stable across independent satellite "
                     "products. What would kill it: regime rows whose signs "
                     "flip between satellite datasets, or a sum that cannot "
                     "be reconciled with the observed top-of-atmosphere "
                     "energy budget. What it does NOT claim: that the "
                     "satellite record is already long enough to close the "
                     "question - it specifies exactly how many more years of "
                     "each regime record would be needed."),
        "key_points": [
            "Clouds cool by reflecting sunlight and warm by trapping infrared.",
            "AR6 net cloud feedback: +0.42 W/m2/K, range -0.10 to +0.94.",
            "Marine stratocumulus response is the pivotal regime.",
            "CMIP6 'hot models' get high sensitivity largely from cloud feedback.",
            "Two decades of satellite records (CERES, MODIS, CloudSat) now exist.",
        ],
        "requirements": [
            "Regime-separated feedback scores from satellite records.",
            "Sign stability of each regime row across independent satellite products.",
            "Reconciliation with the top-of-atmosphere energy budget.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (cloud feedback assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "net cloud feedback", "unit": "W/m2/K",
            "calc": "sum", "base": 0.0,
            "assumptions": [("marine stratocumulus feedback", 0.25, [0.0, 0.25, 0.5]),
                            ("trade cumulus feedback", 0.05, [-0.1, 0.05, 0.15]),
                            ("deep convective anvil feedback", 0.05, [-0.1, 0.05, 0.2]),
                            ("high cirrus feedback", 0.07, [0.0, 0.07, 0.15])],
            "formula": "net = sum of regime feedbacks (area-weighted); AR6 central +0.42",
            "checks": [((0.25, 0.05, 0.05, 0.07), 0.42, 0.001), ((0.0, -0.1, -0.1, 0.0), -0.2, 0.001)],
            "steps": [
                "Step 1: split clouds into regimes with separable physics.",
                "Step 2: score each regime's feedback from satellite cloud-radiative-effect trends.",
                "Step 3: weight by regime area and sum to the net feedback.",
                "Step 4: publish the ledger as a challengeable table, one row per regime.",
                "Step 5: state how many more record-years each row needs to close.",
            ],
            "confirm": [
                "Ledger sum matches the AR6 central value with each row sign-stable across satellite products.",
                "The sum reconciles with the observed top-of-atmosphere energy budget.",
            ],
            "refute": [
                "Regime rows flip sign between independent satellite datasets.",
                "The ledger sum cannot be reconciled with the energy budget.",
            ],
            "note": "Regime-ledger explorer decomposing net cloud feedback by cloud type.",
        },
    },
    {
        "key": "aerosol-forcing",
        "name": "Aerosol Cooling: How Much Pollution Masks Warming",
        "group": "Foundations",
        "ladder_rank": 5, "ladder_tier": "foundations",
        "problem": ("Air pollution particles (aerosols) cool the planet - "
                    "directly by scattering sunlight and indirectly by "
                    "brightening clouds - masking an unknown fraction of "
                    "greenhouse warming. AR6 assessed the total aerosol "
                    "effective radiative forcing at about -1.3 W/m2 for "
                    "1750-2019, but the uncertainty range (-2.0 to -0.6 W/m2) "
                    "is the widest of any forcing agent, and it directly "
                    "widens the ECS range inferred from the historical "
                    "record."),
        "background": ("Aerosols live only days to weeks in the atmosphere, "
                       "so their cooling is patchy - concentrated over "
                       "industrial regions and shipping lanes - unlike the "
                       "well-mixed greenhouse gases. The direct effect "
                       "(scattering and absorption) is measurable, but the "
                       "indirect effects on cloud brightness and lifetime are "
                       "among the hardest processes in climate physics, "
                       "depending on microscopic droplet nucleation. The "
                       "famous 'global dimming' of mid-20th-century sunlight "
                       "records, followed by 'brightening' as clean-air laws "
                       "took effect, is the observational fingerprint. The "
                       "cruel twist: cleaning the air saves lives but "
                       "unmasks warming - and the size of the unmasking is "
                       "uncertain by more than a factor of three."),
        "why_it_matters": ("Every estimate of climate sensitivity drawn from "
                           "the historical record subtracts aerosol cooling "
                           "from greenhouse warming; the aerosol uncertainty "
                           "is therefore baked into the sensitivity "
                           "uncertainty. And as Asia and Africa clean their "
                           "air in coming decades, the unmasked warming could "
                           "arrive as a rapid pulse - or a gentle slope - "
                           "depending on this number."),
        "sig_pointer": ("The Signature edition proposes a natural-experiment "
                        "ledger: volcanoes, shipping lanes, and clean-air "
                        "laws as scored cooling measurements. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) large volcanic eruptions, "
                     "the 2020 shipping-fuel sulfur cut, and regional "
                     "clean-air laws are usable natural experiments in "
                     "aerosol forcing; (2) each experiment's cooling signal "
                     "can be isolated from internal variability with stated "
                     "uncertainty; (3) the experiments sample different "
                     "aerosol types and regions, bounding the global mean. "
                     "Reasoning path: treat each natural experiment as an "
                     "independent measurement of aerosol forcing per unit "
                     "aerosol change, convert to a common currency "
                     "(W/m2 per unit aerosol optical depth), and combine - "
                     "so the forcing estimate rests on observed events, not "
                     "on aerosol microphysics schemes. Proposed mechanism: a "
                     "natural-experiment ledger with rows for Pinatubo-scale "
                     "volcanoes, the IMO 2020 shipping sulfur cap, the "
                     "US/European clean-air brightening, and Chinese emission "
                     "trends, each scored with its isolation uncertainty. "
                     "What would confirm it: the ledger rows agree within "
                     "uncertainty and predict the warming pulse of the next "
                     "major clean-air episode before it is observed. What "
                     "would kill it: rows that disagree beyond their stated "
                     "uncertainties, or a clean-air episode whose unmasking "
                     "falls outside the ledger bounds. What it does NOT "
                     "claim: that aerosol-cloud microphysics is solved - it "
                     "deliberately bypasses the microphysics in favor of "
                     "event-scale measurements."),
        "key_points": [
            "Aerosols cool directly (scattering sunlight) and indirectly (brightening clouds).",
            "AR6 total aerosol forcing ~-1.3 W/m2, range -2.0 to -0.6 W/m2 - the widest forcing uncertainty.",
            "Aerosols are short-lived and patchy, unlike well-mixed greenhouse gases.",
            "'Global dimming' then 'brightening' is the observational fingerprint.",
            "Cleaning air unmasks warming of uncertain size - the 2020 shipping sulfur cut is a live test.",
        ],
        "requirements": [
            "Scored natural experiments: volcanoes, shipping sulfur cut, clean-air laws.",
            "Isolation of each cooling signal from internal variability.",
            "A successful prediction of the next major unmasking pulse.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (aerosol radiative forcing assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "unmasked warming from cleaning aerosols", "unit": "C",
            "calc": "expr", "expr": "a0 * 0.8 / 3.0",
            "assumptions": [("aerosol forcing removed (W/m2)", 1.3, [0.6, 1.3, 2.0])],
            "formula": "unmasked_C ~= forcing_Wm2 * 0.8 / 3.0 (transient response scaling)",
            "checks": [((0.6,), 0.16, 0.005), ((1.3,), 0.3467, 0.005), ((2.0,), 0.5333, 0.005)],
            "steps": [
                "Step 1: list the natural experiments (volcanoes, shipping cap, clean-air laws).",
                "Step 2: score each experiment's cooling in common currency (W/m2 per aerosol change).",
                "Step 3: combine into a ledger estimate of total aerosol forcing.",
                "Step 4: convert forcing to unmasked warming with transient-response scaling.",
                "Step 5: predict the next clean-air unmasking pulse ahead of observation.",
            ],
            "confirm": [
                "Ledger rows agree within uncertainty and predict the next unmasking pulse.",
                "The IMO 2020 shipping signal matches the ledger's shipping row.",
            ],
            "refute": [
                "Rows disagree beyond stated uncertainties.",
                "A clean-air episode's unmasking falls outside ledger bounds.",
            ],
            "note": "Natural-experiment ledger explorer for aerosol masking of warming.",
        },
    },
    {
        "key": "ocean-heat-uptake",
        "name": "Where the Heat Goes: Ocean Heat Uptake",
        "group": "Foundations",
        "ladder_rank": 6, "ladder_tier": "foundations",
        "problem": ("More than 90 percent of the excess heat trapped by "
                    "greenhouse gases has gone into the oceans, yet the rate "
                    "at which the ocean takes up heat - and how that rate "
                    "will change - is only approximately known. Ocean heat "
                    "uptake sets the pace of surface warming: fast uptake "
                    "delays warming (and commits it to the future); slow "
                    "uptake brings warming forward."),
        "background": ("Before the Argo float array reached near-global "
                       "coverage around 2005, ocean heat content was sampled "
                       "by sparse ship-based measurements with known biases "
                       "(expendable bathythermograph fall-rate errors). The "
                       "modern record shows the upper 2,000 meters gaining "
                       "heat at roughly 0.5 to 1.0 W/m2 averaged over "
                       "Earth's surface, with acceleration in recent "
                       "decades - the oceans gained on the order of 300-400 "
                       "zettajoules since 1970. The deep ocean below 2,000 "
                       "meters remains sparsely observed (Deep Argo is still "
                       "deploying). Models disagree on uptake efficiency - "
                       "how much heat the ocean swallows per degree of "
                       "surface warming - and that disagreement maps "
                       "directly onto disagreement about transient warming."),
        "why_it_matters": ("Ocean heat uptake is the planet's thermal "
                           "inertia. Its rate determines how much warming is "
                           "'in the pipeline' even if emissions stopped "
                           "today, how fast sea level rises from thermal "
                           "expansion, and how much time societies have to "
                           "adapt. Marine heatwaves - with their fisheries "
                           "collapses - ride on top of this accumulating "
                           "heat."),
        "sig_pointer": ("The Signature edition proposes a layer-cake heat "
                        "ledger: surface, thermocline, and deep layers "
                        "scored separately from Argo and Deep Argo. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) Argo-era (post-2005) "
                     "upper-ocean data are accurate enough to score the top "
                     "layer; (2) deep-ocean sparse data can bound, not "
                     "measure, the bottom layer; (3) uptake efficiency "
                     "(heat per degree of surface warming) is the right "
                     "single diagnostic to compare models against "
                     "observations. Reasoning path: build a three-layer "
                     "ledger - 0-700 m, 700-2000 m, below 2000 m - score "
                     "each layer's heat gain per decade from observations, "
                     "then divide by observed surface warming to get the "
                     "uptake efficiency, a number any model must reproduce. "
                     "Proposed mechanism: the layer-cake ledger becomes the "
                     "acceptance test for ocean components of climate "
                     "models - a model whose efficiency falls outside the "
                     "observed ledger is flagged regardless of its surface "
                     "temperature skill. What would confirm it: Deep Argo "
                     "completion tightens the bottom layer and the efficiency "
                     "number stabilizes across dataset versions. What would "
                     "kill it: uptake efficiency that drifts with the "
                     "analysis period (showing it is not a stable property), "
                     "or deep-ocean gains that dwarf the ledger bounds. What "
                     "it does NOT claim: that heat uptake can be predicted "
                     "decades ahead - it claims only that the current rate "
                     "can be measured honestly and used as a model filter."),
        "key_points": [
            "Over 90% of trapped excess heat has entered the oceans.",
            "Upper 2,000 m gaining roughly 0.5-1.0 W/m2 (Earth-surface average), accelerating.",
            "Oceans gained ~300-400 zettajoules since 1970.",
            "Pre-2005 records suffer sparse sampling and instrument biases.",
            "Deep ocean below 2,000 m still sparsely observed; Deep Argo deploying.",
        ],
        "requirements": [
            "Three-layer heat ledger scored from Argo and Deep Argo.",
            "A stable uptake-efficiency diagnostic (heat per degree surface warming).",
            "Model acceptance test: efficiency must fall inside the observed ledger.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 9 (ocean, cryosphere, and sea level change)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "ocean heat accumulated", "unit": "zettajoules",
            "calc": "heat", "imbalance": 0.9, "years": 10,
            "assumptions": [("Earth-average heat uptake (W/m2)", 0.9, [0.5, 0.9, 1.2]),
                            ("years", 10, [10, 20, 50])],
            "formula": "ZJ = uptake_Wm2 * years * 16.0965 (Earth area x seconds per year)",
            "checks": [((0.9, 10), 144.868, 0.6), ((0.5, 50), 402.41, 1.5)],
            "steps": [
                "Step 1: score the 0-700 m layer from Argo temperature profiles.",
                "Step 2: score the 700-2000 m layer from deep Argo profiles.",
                "Step 3: bound the below-2000 m layer from sparse deep data.",
                "Step 4: divide total heat gain by surface warming for uptake efficiency.",
                "Step 5: use efficiency as the acceptance test for model ocean components.",
            ],
            "confirm": [
                "Deep Argo completion tightens the bottom layer and efficiency stabilizes.",
                "The efficiency number is stable across dataset versions.",
            ],
            "refute": [
                "Uptake efficiency drifts with the analysis period.",
                "Deep-ocean gains dwarf the ledger bounds.",
            ],
            "note": "Layer-cake heat ledger explorer for ocean heat uptake.",
        },
    },
    {
        "key": "regional-prediction",
        "name": "Why Regional Warming Is Hard to Predict",
        "group": "Foundations",
        "ladder_rank": 7, "ladder_tier": "foundations",
        "problem": ("Global mean temperature is predictable with useful "
                    "skill, but the warming of any specific region - the "
                    "American Midwest, the Sahel, South Asia - carries "
                    "uncertainties several times larger. Models disagree on "
                    "regional patterns because small shifts in atmospheric "
                    "circulation, which models resolve poorly, dominate "
                    "local outcomes."),
        "background": ("The globe warms on average, but land warms faster "
                       "than ocean, the Arctic fastest of all, and some "
                       "regions (the North Atlantic 'warming hole') have "
                       "barely warmed at all. For a farmer or a city planner, "
                       "the global mean is nearly useless - what matters is "
                       "the local change in heat, rain, and extremes, where "
                       "model spread is wide and observed trends are noisy. "
                       "The core difficulty: regional climate is controlled "
                       "by circulation features (jet streams, storm tracks, "
                       "monsoons) whose response to warming is itself "
                       "uncertain - the famous 'tug of war' between "
                       "thermodynamic moistening (robust) and dynamic "
                       "circulation shifts (fragile). Downscaling adds "
                       "detail but inherits the parent model's circulation "
                       "errors."),
        "why_it_matters": ("Adaptation is local: crop choices, reservoir "
                           "sizing, flood defenses, and heat-action plans all "
                           "need regional numbers. Uncertainty several times "
                           "the global mean's is the difference between a "
                           "reservoir built right and a billion-dollar "
                           "stranded asset."),
        "sig_pointer": ("The Signature edition proposes a circulation-first "
                        "audit: score models on circulation fidelity before "
                        "trusting their regional output. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) regional outcomes are "
                     "dominated by circulation response, not by global-mean "
                     "sensitivity; (2) a model's circulation fidelity can be "
                     "scored from its simulation of observed circulation "
                     "variability; (3) models that fail the circulation "
                     "audit should be down-weighted for regional use even if "
                     "their global means look good. Reasoning path: build a "
                     "circulation scorecard - jet position and strength, "
                     "storm-track latitude, monsoon timing, blocking "
                     "frequency - grade each model against reanalysis, and "
                     "produce regional projections only from the "
                     "passing models, with the failing models' spread shown "
                     "as the honest uncertainty. Proposed mechanism: a "
                     "public circulation scorecard that any planner can read "
                     "before trusting a regional projection. What would "
                     "confirm it: passing models' regional hindcasts verify "
                     "better than failing models' over the last 40 years. "
                     "What would kill it: no correlation between circulation "
                     "scores and regional hindcast skill, or all models "
                     "failing the audit (leaving no usable ensemble). What "
                     "it does NOT claim: that circulation is the only "
                     "source of regional uncertainty, or that downscaling "
                     "fixes parent-model errors - it claims the audit "
                     "honestly reports which projections deserve trust."),
        "key_points": [
            "Global mean is predictable; regional outcomes carry far larger uncertainty.",
            "Land warms faster than ocean; the Arctic fastest; the North Atlantic 'warming hole' barely warms.",
            "Regional outcomes are dominated by circulation responses models resolve poorly.",
            "Thermodynamic moistening is robust; dynamic circulation shifts are fragile.",
            "Downscaling inherits parent-model circulation errors.",
        ],
        "requirements": [
            "A circulation scorecard (jets, storm tracks, monsoons, blocking) vs reanalysis.",
            "Regional projections drawn only from passing models.",
            "Hindcast verification showing passing models beat failing ones.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 10 (linking global to regional climate change)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "regional warming uncertainty width", "unit": "C",
            "calc": "expr", "expr": "a0 * a1 * (1.2 - 0.5*a2)", "base": 1.5,
            "assumptions": [("global-mean uncertainty (C)", 1.5, [1.0, 1.5, 2.0]),
                            ("circulation amplification factor", 2.5, [1.5, 2.5, 4.0]),
                            ("models passing circulation audit (fraction)", 0.4, [0.2, 0.4, 0.8])],
            "formula": "regional_width = global_width * circulation_factor * (1.2 - 0.5*pass_fraction)",
            "checks": [((1.5, 2.5, 0.4), 3.75, 0.01), ((1.0, 1.5, 0.8), 1.2, 0.01)],
            "steps": [
                "Step 1: define the circulation scorecard (jets, storm tracks, monsoons, blocking).",
                "Step 2: grade each model against reanalysis observations.",
                "Step 3: build regional projections only from passing models.",
                "Step 4: show failing models' spread as the honest uncertainty.",
                "Step 5: verify with 40-year regional hindcasts.",
            ],
            "confirm": [
                "Passing models verify better in regional hindcasts than failing models.",
                "The scorecard is stable across reanalysis products.",
            ],
            "refute": [
                "No correlation between circulation scores and hindcast skill.",
                "All models fail the audit, leaving no usable ensemble.",
            ],
            "note": "Circulation-first audit explorer for regional prediction uncertainty.",
        },
    },
    {
        "key": "extreme-attribution",
        "name": "Attribution: Linking Extreme Events to Climate Change",
        "group": "Foundations",
        "ladder_rank": 8, "ladder_tier": "foundations",
        "problem": ("When a heatwave, flood, or hurricane strikes, the "
                    "question 'did climate change cause this?' has no single "
                    "scientific answer - attribution science answers a "
                    "narrower question: how did warming change the event's "
                    "probability or intensity? For heatwaves the methods work "
                    "well; for hurricanes, tornadoes, and convective "
                    "downpours the answers remain fragile and "
                    "method-dependent."),
        "background": ("Event attribution compares two model worlds - one "
                       "with human greenhouse gases, one without - and "
                       "computes the fraction of attributable risk or the "
                       "intensity shift. The 2003 European heatwave and the "
                       "2021 Pacific Northwest heat dome were found to be "
                       "virtually impossible without warming; heavy-precipitation "
                       "events show a robust thermodynamic increase of about "
                       "7 percent more moisture per degree. But tropical "
                       "cyclones mix thermodynamics with dynamics: warmer "
                       "seas add energy while uncertain wind-shear changes "
                       "may tear storms apart. Tornadoes, hail, and flash "
                       "floods live below the resolution of the models used "
                       "for attribution, so statements about them rest on "
                       "weaker foundations - a fact sometimes lost in "
                       "headlines."),
        "why_it_matters": ("Attribution is where climate science meets the "
                           "courtroom, the newsroom, and the insurance "
                           "contract. Overstated attribution destroys trust; "
                           "understated attribution abandons communities "
                           "seeking to understand their changing risk. The "
                           "science must say exactly what it can and cannot "
                           "claim, event by event."),
        "sig_pointer": ("The Signature edition proposes an event report card "
                        "grading each attribution claim by event type. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) attribution skill varies "
                     "by event type along a known hierarchy (heatwaves > "
                     "heavy rain > droughts > tropical cyclones > tornadoes); "
                     "(2) a claim's grade must reflect the weakest link - "
                     "model resolution, observational record, or physical "
                     "understanding; (3) the public deserves the grade, not "
                     "just the headline number. Reasoning path: for each "
                     "attributed event, score three pillars - model adequacy "
                     "for that event type, length and quality of the "
                     "observational record, and physical understanding of the "
                     "mechanism - and publish the letter grade alongside the "
                     "probability ratio. Proposed mechanism: a standardized "
                     "attribution report card (A = heatwave-grade confidence "
                     "through F = below-resolution speculation) attached to "
                     "every attribution study and press release. What would "
                     "confirm it: report cards predict which attribution "
                     "results replicate across independent modeling centers. "
                     "What would kill it: high-graded events that fail to "
                     "replicate, or low-graded events that replicate "
                     "perfectly (showing the grading misses the real skill). "
                     "What it does NOT claim: that any single event is "
                     "'caused' by climate change in the everyday sense - it "
                     "grades only the narrower probability/intensity "
                     "question, and says so plainly."),
        "key_points": [
            "Attribution answers probability/intensity shifts, not everyday causation.",
            "Heatwave attribution is robust (2021 Pacific Northwest heat dome virtually impossible without warming).",
            "Heavy precipitation rises ~7% per degree (thermodynamics).",
            "Tropical cyclone attribution mixes robust thermodynamics with fragile dynamics.",
            "Tornadoes and hail sit below attribution models' resolution.",
        ],
        "requirements": [
            "Three-pillar grading: model adequacy, observational record, physical understanding.",
            "A published letter grade with every attribution claim.",
            "Replication tests across independent modeling centers.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 11 (weather and climate extreme events)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "attribution confidence score", "unit": "points/100",
            "calc": "min", "base": 0.0,
            "assumptions": [("model adequacy for event type", 70, [40, 70, 95]),
                            ("observational record quality", 70, [40, 70, 95]),
                            ("physical understanding", 70, [40, 70, 95])],
            "formula": "score = weakest pillar (min of the three); grade A>=85, B>=70, C>=55, D>=40, F<40",
            "checks": [((70, 70, 70), 70, 0.5), ((95, 95, 40), 40, 0.5), ((95, 90, 88), 88, 0.5)],
            "steps": [
                "Step 1: classify the event by type on the skill hierarchy.",
                "Step 2: score model adequacy for that event type.",
                "Step 3: score the observational record length and quality.",
                "Step 4: score physical understanding of the mechanism.",
                "Step 5: publish the weakest-link grade with the claim.",
            ],
            "confirm": [
                "Report-card grades predict replication across modeling centers.",
                "Headline claims converge toward graded, modest statements.",
            ],
            "refute": [
                "High-graded events fail to replicate across centers.",
                "Low-graded events replicate perfectly, breaking the grading logic.",
            ],
            "note": "Attribution report-card explorer grading claims by event type.",
        },
    },
    {
        "key": "arctic-amplification",
        "name": "Arctic Amplification: Why the Arctic Warms Faster",
        "group": "Foundations",
        "ladder_rank": 9, "ladder_tier": "foundations",
        "problem": ("The Arctic has warmed roughly three to four times "
                    "faster than the global average in recent decades - a "
                    "phenomenon called Arctic amplification - but the exact "
                    "mix of causes (ice-albedo feedback, lapse-rate "
                    "feedback, increased poleward heat transport, cloud and "
                    "water-vapor changes) and whether models get the "
                    "mechanism right for the right reasons remain open."),
        "background": ("Arctic amplification was predicted by Arrhenius "
                       "himself in 1896 and by early models in the 1970s, "
                       "yet its observed pace has surprised: Rantanen and "
                       "colleagues (2022) found the Arctic warming nearly "
                       "four times the global rate over 1979-2021 in some "
                       "datasets and regions. Sea-ice loss drives the "
                       "ice-albedo feedback - dark ocean replacing bright "
                       "ice - but the lapse-rate feedback (the Arctic's "
                       "stable atmosphere traps surface warming) may "
                       "contribute as much or more, and increased moisture "
                       "transport from lower latitudes adds another term. "
                       "Models reproduce the amplification but disagree on "
                       "the partition, and the sparse pre-satellite Arctic "
                       "record makes the long-term context uncertain."),
        "why_it_matters": ("Arctic amplification drives sea-ice loss, "
                           "Greenland melt, permafrost thaw, and mid-latitude "
                           "weather debates (the contested link between "
                           "Arctic warming and jet-stream waviness). Getting "
                           "the mechanism partition right determines whether "
                           "models will correctly project the Arctic's "
                           "future - including the first ice-free September, "
                           "now expected within decades."),
        "sig_pointer": ("The Signature edition proposes a mechanism ledger "
                        "that partitions amplification among its causes from "
                        "observations. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the total amplification "
                     "factor (~3-4x) can be decomposed into additive "
                     "mechanism terms; (2) each term - ice-albedo, "
                     "lapse-rate, heat transport, clouds/water vapor - has "
                     "an observable fingerprint; (3) the satellite-era "
                     "record is long enough to score trends in each "
                     "fingerprint. Reasoning path: measure each mechanism's "
                     "fingerprint trend (surface albedo from satellites, "
                     "lapse-rate from radiosondes, poleward energy transport "
                     "from reanalysis, downwelling longwave from surface "
                     "stations), convert each to its amplification "
                     "contribution, and require the sum to match the "
                     "observed ~3-4x factor. Proposed mechanism: an "
                     "amplification ledger that names the leading mechanism "
                     "with a number, so the 'ice-albedo vs lapse-rate' "
                     "debate becomes a scored table instead of a narrative. "
                     "What would confirm it: the ledger sums to the observed "
                     "amplification and the leading term is stable across "
                     "datasets. What would kill it: fingerprints that "
                     "contradict each other, or a sum that misses the "
                     "observed factor by a wide margin. What it does NOT "
                     "claim: resolution of the Arctic-midlatitude weather "
                     "link debate - the ledger partitions Arctic warming "
                     "mechanisms only, and treats downstream weather effects "
                     "as a separate open question."),
        "key_points": [
            "The Arctic warmed ~3-4x faster than the global mean over 1979-2021.",
            "Candidate mechanisms: ice-albedo, lapse-rate, heat transport, clouds and water vapor.",
            "The lapse-rate feedback may rival ice-albedo in importance.",
            "Models reproduce amplification but disagree on the mechanism partition.",
            "The first ice-free Arctic September is expected within decades.",
        ],
        "requirements": [
            "Observed fingerprint trends for each mechanism.",
            "A ledger summing to the observed amplification factor.",
            "Stability of the leading term across independent datasets.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 9 (Arctic assessment); Rantanen et al. 2022"],
        "citations": CIT_BASE + [
            "Rantanen M et al. The Arctic has warmed nearly four times faster "
            "than the globe since 1979. Communications Earth and Environment; "
            "2022.",
        ],
        "demo": {
            "quantity": "Arctic amplification factor", "unit": "multiple of global mean",
            "calc": "sum1", "base": 1.0,
            "assumptions": [("ice-albedo contribution", 1.2, [0.5, 1.2, 1.8]),
                            ("lapse-rate contribution", 1.0, [0.4, 1.0, 1.5]),
                            ("heat transport contribution", 0.6, [0.2, 0.6, 1.0]),
                            ("cloud and water vapor contribution", 0.5, [0.1, 0.5, 0.9])],
            "formula": "amplification = 1 + sum of mechanism contributions; observed ~3-4",
            "checks": [((1.2, 1.0, 0.6, 0.5), 4.3, 0.05), ((0.5, 0.4, 0.2, 0.1), 2.2, 0.05)],
            "steps": [
                "Step 1: list the candidate mechanisms with their fingerprints.",
                "Step 2: score each fingerprint trend from observations.",
                "Step 3: convert each trend to an amplification contribution.",
                "Step 4: sum the ledger and compare with the observed ~3-4x factor.",
                "Step 5: name the leading mechanism with its number and uncertainty.",
            ],
            "confirm": [
                "The ledger sums to the observed amplification within uncertainty.",
                "The leading term is stable across independent datasets.",
            ],
            "refute": [
                "Fingerprints contradict each other beyond stated uncertainty.",
                "The ledger sum misses the observed factor by a wide margin.",
            ],
            "note": "Mechanism-ledger explorer partitioning Arctic amplification.",
        },
    },
    {
        "key": "water-vapor-feedback",
        "name": "The Water Vapor Feedback Loop",
        "group": "Foundations",
        "ladder_rank": 10, "ladder_tier": "foundations",
        "problem": ("Water vapor is the strongest greenhouse gas by total "
                    "effect, and warmer air holds more of it - a positive "
                    "feedback assessed as the largest single amplifying "
                    "feedback. The open question is quantitative: whether "
                    "relative humidity stays roughly constant as the climate "
                    "warms (the standard assumption, giving a strong "
                    "feedback) or shifts in ways that weaken or strengthen "
                    "it, especially in the upper troposphere where it "
                    "matters most."),
        "background": ("The Clausius-Clapeyron relation says saturation "
                       "vapor pressure rises about 7 percent per degree - "
                       "hard physics. If relative humidity stays constant, "
                       "specific humidity rises with it and the feedback is "
                       "about +1.8 W/m2/K, roughly doubling the no-feedback "
                       "response. Observations from satellites and "
                       "radiosondes broadly support near-constant relative "
                       "humidity in the lower troposphere, but the upper "
                       "troposphere - where water vapor's greenhouse effect "
                       "is most potent per molecule - is harder to measure, "
                       "and some analyses find drying trends in key regions. "
                       "The feedback's exact strength, and its interplay "
                       "with the lapse-rate feedback (usually reported as a "
                       "combined water-vapor-plus-lapse-rate term), sets the "
                       "floor under climate sensitivity."),
        "why_it_matters": ("Water vapor feedback is the reason sensitivity "
                           "estimates cluster around 3 C rather than 1.2 C. "
                           "If the real feedback were substantially weaker, "
                           "every projection of this century would shift "
                           "down; the observational check on this feedback "
                           "is therefore one of the most leveraged "
                           "measurements in climate science."),
        "sig_pointer": ("The Signature edition proposes a humidity-ledger "
                        "audit of the upper troposphere, the layer that "
                        "matters most. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the "
                     "Clausius-Clapeyron 7-percent-per-degree relation is "
                     "the correct baseline; (2) relative-humidity trends can "
                     "be measured separately by altitude layer from "
                     "satellites and radiosondes; (3) the upper-tropospheric "
                     "layer dominates the feedback uncertainty. Reasoning "
                     "path: build a humidity ledger by layer - boundary "
                     "layer, mid-troposphere, upper troposphere - score each "
                     "layer's specific-humidity trend per degree of warming "
                     "from observations, weight by each layer's radiative "
                     "potency, and sum to the total feedback. Proposed "
                     "mechanism: a layer ledger that isolates exactly where "
                     "the 'constant relative humidity' assumption holds and "
                     "where it breaks, so future observations target the "
                     "guilty layer. What would confirm it: the ledger sum "
                     "matches the AR6 water-vapor feedback value and each "
                     "layer's trend is stable across satellite products. "
                     "What would kill it: upper-tropospheric drying trends "
                     "that persist across all products and shrink the ledger "
                     "sum well below assessed values. What it does NOT "
                     "claim: that water vapor could flip the feedback "
                     "negative on its own - the ledger tests magnitude, and "
                     "a sign flip would require extraordinary evidence it "
                     "does not presuppose."),
        "key_points": [
            "Water vapor is the strongest greenhouse gas by total effect.",
            "Saturation vapor pressure rises ~7% per degree (Clausius-Clapeyron).",
            "Constant relative humidity implies a feedback of ~+1.8 W/m2/K.",
            "The upper troposphere matters most per molecule and is hardest to measure.",
            "Usually reported combined with the lapse-rate feedback.",
        ],
        "requirements": [
            "Layer-separated humidity trends from satellites and radiosondes.",
            "Radiative weighting of each layer's contribution.",
            "Stability of layer trends across independent products.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (water vapor and lapse-rate feedback)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "water vapor feedback strength", "unit": "W/m2/K",
            "calc": "sum", "base": 0.0,
            "assumptions": [("boundary-layer contribution", 0.5, [0.3, 0.5, 0.7]),
                            ("mid-troposphere contribution", 0.6, [0.3, 0.6, 0.9]),
                            ("upper-troposphere contribution", 0.7, [0.2, 0.7, 1.1])],
            "formula": "feedback = sum of layer contributions; assessed total ~+1.8",
            "checks": [((0.5, 0.6, 0.7), 1.8, 0.01), ((0.3, 0.3, 0.2), 0.8, 0.01)],
            "steps": [
                "Step 1: fix the Clausius-Clapeyron baseline (7% per degree).",
                "Step 2: score specific-humidity trends per layer from observations.",
                "Step 3: weight each layer by its radiative potency.",
                "Step 4: sum the humidity ledger to the total feedback.",
                "Step 5: isolate any layer where constant relative humidity breaks.",
            ],
            "confirm": [
                "The ledger sum matches the assessed feedback value.",
                "Layer trends are stable across satellite products.",
            ],
            "refute": [
                "Persistent upper-tropospheric drying across all products shrinks the sum.",
                "Layer trends flip sign between products.",
            ],
            "note": "Humidity-ledger explorer for the water vapor feedback.",
        },
    },
    {
        "key": "sea-level-2100",
        "name": "Sea Level by 2100: How High",
        "group": "Foundations",
        "ladder_rank": 11, "ladder_tier": "foundations",
        "problem": ("How high will the seas be in 2100? AR6 projects "
                    "0.28-0.55 m under very low emissions and 0.63-1.01 m "
                    "under very high emissions by 2100 - but the upper tail, "
                    "driven by Antarctic ice-sheet instability, cannot be "
                    "ruled out and could add substantially more. The "
                    "question is really two: the likely range, and the "
                    "plausible worst case."),
        "background": ("Sea level rises from three sources: thermal expansion "
                       "of warming water (the best-understood term), melting "
                       "mountain glaciers (well-measured, limited total), and "
                       "the Greenland and Antarctic ice sheets (the "
                       "dominant uncertainty). Tide gauges give a 20th-century "
                       "rise of about 20 cm; satellite altimetry since 1993 "
                       "shows about 3.4 mm per year, accelerating. The "
                       "Antarctic contribution hinges on marine ice-sheet "
                       "instability and the contested marine ice-cliff "
                       "instability hypothesis - include it and the high-end "
                       "tail stretches past 2 m by 2100 in some studies; "
                       "exclude it and the tail is far shorter. Regional seas "
                       "differ from the global mean due to gravity, rotation, "
                       "and land motion - the US East Coast, for example, "
                       "faces faster-than-average rise."),
        "why_it_matters": ("A meter of sea-level rise redraws coastlines, "
                           "drowns infrastructure designed for the last "
                           "century's seas, and forces decisions about "
                           "trillions of dollars of coastal assets. The "
                           "difference between the likely range and the "
                           "high-end tail is the difference between adaptation "
                           "and retreat for many coastal cities."),
        "sig_pointer": ("The Signature edition proposes a source-ledger with "
                        "the Antarctic tail priced as an explicit gamble. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) thermal expansion and "
                     "glacier terms are well enough measured to be ledger "
                     "anchors; (2) the Greenland and Antarctic terms carry "
                     "all the deep uncertainty; (3) the high-end tail should "
                     "be priced explicitly rather than averaged away. "
                     "Reasoning path: build a four-source ledger - thermal "
                     "expansion, glaciers, Greenland, Antarctica - score "
                     "each from observations and process studies, and "
                     "present two totals: the likely range (instability "
                     "mechanisms excluded or bounded) and the tail price "
                     "(what instability would add, with its evidence grade). "
                     "Proposed mechanism: a sea-level ledger that separates "
                     "'what we expect' from 'what we cannot rule out', so "
                     "planners can insure against the tail without "
                     "pretending it is the forecast. What would confirm it: "
                     "the ledger's likely range tracks observed altimetry "
                     "year by year, and the tail price shrinks as Antarctic "
                     "process studies mature. What would kill it: observed "
                     "rise persistently outside the likely range, or "
                     "Antarctic observations that force the tail into the "
                     "likely column. What it does NOT claim: a new 2100 "
                     "number - it is an accounting framework that makes the "
                     "existing numbers' structure transparent."),
        "key_points": [
            "AR6 2100 ranges: 0.28-0.55 m (very low emissions), 0.63-1.01 m (very high).",
            "Three sources: thermal expansion, glaciers, ice sheets (ice sheets dominate uncertainty).",
            "Satellite altimetry: ~3.4 mm/yr since 1993, accelerating.",
            "Marine ice-cliff instability could extend the high-end tail past 2 m.",
            "Regional seas differ: US East Coast faces faster-than-average rise.",
        ],
        "requirements": [
            "Four-source ledger with observations anchoring expansion and glaciers.",
            "Explicit pricing of the Antarctic instability tail with evidence grades.",
            "Year-by-year tracking of the likely range against altimetry.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 9 (sea level projections)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "sea-level rise by 2100", "unit": "cm",
            "calc": "sealevel", "rate": 3.4, "years": 76, "accel": 0.084,
            "assumptions": [("current rate (mm/yr)", 3.4, [3.0, 3.4, 4.0]),
                            ("years to 2100", 76, [50, 76, 100]),
                            ("acceleration (mm/yr2)", 0.084, [0.0, 0.084, 0.15])],
            "formula": "SL_cm = (rate*years + 0.5*accel*years^2)/10",
            "checks": [((3.4, 76, 0.084), 50.10, 0.1), ((3.4, 76, 0.0), 25.84, 0.05)],
            "steps": [
                "Step 1: anchor thermal expansion and glacier terms from observations.",
                "Step 2: score Greenland and Antarctic terms with uncertainty.",
                "Step 3: build the likely range from bounded mechanisms.",
                "Step 4: price the instability tail separately with evidence grades.",
                "Step 5: track the likely range against satellite altimetry yearly.",
            ],
            "confirm": [
                "The likely range tracks altimetry year by year.",
                "The tail price shrinks as Antarctic process studies mature.",
            ],
            "refute": [
                "Observed rise persistently exits the likely range.",
                "Antarctic observations force the tail into the likely column.",
            ],
            "note": "Source-ledger explorer for 2100 sea-level rise.",
        },
    },
]

ENTRIES += [
    # ------------------------------------------------- 2 COMPOUNDED
    {
        "key": "west-antarctic",
        "name": "The West Antarctic Ice Sheet: How Fast Could It Go",
        "group": "Compounded",
        "ladder_rank": 12, "ladder_tier": "compounded",
        "problem": ("The West Antarctic Ice Sheet (WAIS) holds about 3.3 "
                    "meters of sea-level equivalent, much of it grounded "
                    "below sea level on bedrock that deepens inland - a "
                    "geometry prone to marine ice-sheet instability, a "
                    "self-sustaining retreat once begun. Whether WAIS "
                    "collapse is already underway in the Amundsen Sea sector, "
                    "and whether it would take centuries or millennia, is "
                    "unsettled."),
        "background": ("WAIS's vulnerability was theorized by John Mercer in "
                       "1968 and formalized by Johannes Weertman in 1974: "
                       "grounding lines on reverse-sloping beds retreat "
                       "unstably. Observations show the Amundsen Sea "
                       "embayment's glaciers - Thwaites and Pine Island - "
                       "thinning and retreating, with warm ocean water "
                       "melting their undersides. Two modeling studies in "
                       "2014-2016 suggested parts of the retreat may already "
                       "be irreversible; a 2016 study invoking marine "
                       "ice-cliff instability (MICI) proposed collapse could "
                       "be far faster - though MICI's physics remains "
                       "contested and later work moderated the rates. The "
                       "deep question: is there a threshold already crossed, "
                       "or does the system still respond proportionally to "
                       "ocean warming?"),
        "why_it_matters": ("WAIS alone is 3.3 meters of sea level - enough "
                           "to redraw every coastline on Earth. The "
                           "difference between centuries and millennia "
                           "determines whether coastal civilization adapts "
                           "gradually or faces an inundation pulse within "
                           "the lifetime of infrastructure being built "
                           "today."),
        "sig_pointer": ("The Signature edition proposes a grounding-line "
                        "tripwire ledger: observable retreat metrics scored "
                        "against instability criteria. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) marine ice-sheet "
                     "instability has observable precursors - grounding-line "
                     "retreat rate, bed-slope geometry, ice-shelf buttressing "
                     "loss; (2) these precursors can be scored from satellite "
                     "and radar observations without trusting any single "
                     "model; (3) irreversibility can be tested by the "
                     "response to ocean cooling in models, not assumed. "
                     "Reasoning path: define a tripwire table - for each "
                     "major Amundsen glacier, list grounding-line retreat "
                     "rate, bed slope at the grounding line, and buttressing "
                     "loss - and score each against the theoretical "
                     "instability criterion (retreat on reverse slope "
                     "accelerating without forcing increase). Proposed "
                     "mechanism: a public tripwire ledger updated yearly "
                     "from observations, with each glacier marked stable, "
                     "watching, or tripped, and the MICI hypothesis carried "
                     "as an explicit side-ledger with its evidence grade. "
                     "What would confirm it: tripwire scores predict which "
                     "glaciers accelerate in the following decade. What "
                     "would kill it: glaciers marked 'tripped' that "
                     "re-stabilize, or stable-marked glaciers that collapse - "
                     "either breaks the tripwire logic. What it does NOT "
                     "claim: that collapse is underway or imminent - the "
                     "ledger reports the tripwire state honestly, including "
                     "'not tripped'."),
        "key_points": [
            "WAIS holds ~3.3 m of sea-level equivalent, grounded below sea level.",
            "Reverse-sloping bedrock enables marine ice-sheet instability (Mercer 1968, Weertman 1974).",
            "Thwaites and Pine Island glaciers are thinning and retreating.",
            "Marine ice-cliff instability (MICI) could accelerate collapse but is contested.",
            "Timescale debate: centuries versus millennia.",
        ],
        "requirements": [
            "Yearly tripwire scores: retreat rate, bed slope, buttressing loss per glacier.",
            "Instability criterion tested against observed accelerations.",
            "MICI carried as an explicit side-ledger with evidence grade.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 9 (ice sheet dynamics and instability)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "WAIS sea-level commitment if fully lost", "unit": "m",
            "calc": "expr", "expr": "3.3 * a0", "base": 3.3,
            "assumptions": [("fraction of WAIS committed", 0.3, [0.1, 0.3, 0.6, 1.0]),
                            ("timescale (centuries)", 5, [2, 5, 20])],
            "formula": "committed_m = 3.3 * fraction; rate_mm_yr = committed_m*1000/(centuries*100)",
            "checks": [((0.3, 5), 0.99, 0.01), ((1.0, 2), 3.3, 0.01)],
            "steps": [
                "Step 1: score grounding-line retreat, bed slope, and buttressing per glacier.",
                "Step 2: test each against the marine instability criterion.",
                "Step 3: mark each glacier stable, watching, or tripped.",
                "Step 4: carry MICI as a side-ledger with its evidence grade.",
                "Step 5: verify tripwire scores against the next decade of observations.",
            ],
            "confirm": [
                "Tripwire scores predict which glaciers accelerate next decade.",
                "The ledger's committed fraction converges across studies.",
            ],
            "refute": [
                "'Tripped' glaciers re-stabilize or 'stable' ones collapse.",
                "Observed retreat decouples from the instability criterion.",
            ],
            "note": "Grounding-line tripwire ledger explorer for WAIS collapse.",
        },
    },
    {
        "key": "greenland-threshold",
        "name": "Greenland's Ice: Melting Point of No Return",
        "group": "Compounded",
        "ladder_rank": 13, "ladder_tier": "compounded",
        "problem": ("Greenland holds about 7.4 meters of sea-level "
                    "equivalent, and its surface melt has accelerated "
                    "dramatically since the 1990s. Theory and models suggest "
                    "a threshold around 1.5 C of sustained warming beyond "
                    "which the ice sheet's surface lowers into warmer air "
                    "and melt becomes self-sustaining - but the threshold's "
                    "exact location, and whether parts of southern Greenland "
                    "have already crossed local tipping dynamics, is open."),
        "background": ("Greenland's mass loss has two channels: surface "
                       "melting (now dominant) and iceberg calving from "
                       "marine-terminating glaciers. The summers of 2012 and "
                       "2019 saw surface melt across nearly the entire ice "
                       "sheet - events once considered millennial rarities. "
                       "The elevation-mass-balance feedback is the core "
                       "instability: as the surface melts and lowers, it "
                       "enters warmer air and melts faster. Paleoclimate "
                       "evidence shows Greenland was much smaller during the "
                       "last interglacial (about 125,000 years ago) when "
                       "temperatures were only modestly higher. Models place "
                       "the complete-loss threshold somewhere between 1.5 "
                       "and 3 C of sustained warming, with large uncertainty "
                       "and hysteresis - regrowing the ice sheet would "
                       "require cooling well below the threshold."),
        "why_it_matters": ("7.4 meters is the largest single land-ice "
                           "commitment on human timescales. Knowing whether "
                           "the threshold sits at 1.5 or 3 C determines "
                           "whether current Paris Agreement targets already "
                           "gamble with Greenland's survival."),
        "sig_pointer": ("The Signature edition proposes an elevation-ledger "
                        "tracking the melt-elevation feedback glacier by "
                        "glacier. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the "
                     "elevation-mass-balance feedback is the dominant "
                     "instability and is observable as surface-lowering "
                     "rates; (2) local thresholds can be scored per drainage "
                     "basin from melt, elevation, and temperature records; "
                     "(3) hysteresis means the ledger must track both the "
                     "warming path and the (much harder) regrowth path. "
                     "Reasoning path: for each major Greenland basin, score "
                     "surface lowering rate, melt-season length trend, and "
                     "local temperature - then compute the basin's distance "
                     "to its modeled instability threshold as an explicit "
                     "number with uncertainty, updated yearly. Proposed "
                     "mechanism: a basin-by-basin threshold-distance ledger, "
                     "published like a fuel gauge, so 'how close is "
                     "Greenland' becomes a measured quantity rather than a "
                     "model quote. What would confirm it: basins scored "
                     "'near threshold' show accelerating mass loss in "
                     "following years while 'far' basins do not. What would "
                     "kill it: threshold distances that fail to predict "
                     "acceleration, or observations showing the "
                     "elevation feedback is weaker than theory requires. "
                     "What it does NOT claim: that any threshold has been "
                     "crossed - the gauge reports distance, and 'not close' "
                     "is a valid reading."),
        "key_points": [
            "Greenland holds ~7.4 m sea-level equivalent.",
            "Surface melt now dominates mass loss; 2012 and 2019 saw near-total surface melt.",
            "Elevation-mass-balance feedback: melting lowers the surface into warmer air.",
            "Modeled complete-loss threshold ~1.5-3 C sustained warming, with hysteresis.",
            "Last interglacial Greenland was much smaller at modestly higher temperatures.",
        ],
        "requirements": [
            "Basin-level scores: surface lowering, melt-season length, temperature.",
            "Threshold-distance gauge per basin, updated yearly.",
            "Verification that 'near' basins accelerate and 'far' basins do not.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 9 (Greenland ice sheet assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "Greenland committed sea-level at threshold", "unit": "m",
            "calc": "expr", "expr": "a0 - a1", "base": 7.4,
            "assumptions": [("sustained warming (C)", 2.0, [1.5, 2.0, 3.0]),
                            ("threshold (C)", 2.0, [1.5, 2.0, 3.0])],
            "formula": "overshoot = warming - threshold; commitment scales with overshoot fraction",
            "checks": [((2.0, 2.0), 0.0, 0.01), ((3.0, 1.5), 1.5, 0.01)],
            "steps": [
                "Step 1: score surface lowering, melt-season length, and temperature per basin.",
                "Step 2: compute each basin's distance to its instability threshold.",
                "Step 3: publish the threshold-distance gauge yearly.",
                "Step 4: track both the warming path and the regrowth (hysteresis) path.",
                "Step 5: verify that near-threshold basins accelerate.",
            ],
            "confirm": [
                "'Near threshold' basins accelerate mass loss; 'far' basins do not.",
                "The gauge is stable across basin definitions.",
            ],
            "refute": [
                "Threshold distances fail to predict acceleration patterns.",
                "The elevation feedback measures weaker than theory requires.",
            ],
            "note": "Threshold-distance gauge explorer for Greenland ice loss.",
        },
    },
    {
        "key": "carbon-sinks",
        "name": "Will the Land and Ocean Carbon Sinks Keep Working",
        "group": "Compounded",
        "ladder_rank": 14, "ladder_tier": "compounded",
        "problem": ("Land ecosystems and the oceans currently absorb about "
                    "half of humanity's CO2 emissions - a free planetary "
                    "service worth the entire mitigation effort twice over. "
                    "Whether these sinks will keep absorbing at the same "
                    "fraction as emissions continue, saturate, or even "
                    "reverse into sources is one of the largest uncertainties "
                    "in the carbon budget."),
        "background": ("The 'airborne fraction' - the share of emitted CO2 "
                       "staying in the atmosphere - has hovered near 45 "
                       "percent for decades, meaning sinks take the rest. "
                       "But CO2 fertilization of plants faces nutrient "
                       "limits (nitrogen, phosphorus), warming increases "
                       "soil respiration and wildfire emissions, and the "
                       "ocean's uptake slows as surface waters warm and "
                       "stratify. Models show the sink fraction declining "
                       "under high emissions, and interannual swings (El "
                       "Nino years can cut land uptake sharply) reveal how "
                       "sensitive the land sink is. The nightmare scenario - "
                       "sinks weakening just as emissions peak - would "
                       "shrink every carbon budget substantially."),
        "why_it_matters": ("Carbon budgets - the 'how much can we still "
                           "emit' numbers behind net-zero dates - assume a "
                           "sink behavior. If sinks weaken faster than "
                           "modeled, the remaining budget for 1.5 or 2 C "
                           "could be hundreds of gigatons smaller than "
                           "quoted, and net-zero dates would need to move "
                           "forward by a decade or more."),
        "sig_pointer": ("The Signature edition proposes a sink-efficiency "
                        "ledger tracking uptake per unit of emissions "
                        "yearly. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) sink efficiency - "
                     "uptake per gigaton emitted - is the right diagnostic, "
                     "better than raw uptake; (2) land and ocean sinks can "
                     "be scored separately from atmospheric inversions and "
                     "ocean surveys; (3) nutrient limitation, warming "
                     "respiration, and stratification are the mechanisms to "
                     "watch, each with observable proxies. Reasoning path: "
                     "compute yearly sink efficiency for land and ocean "
                     "separately, plot efficiency against cumulative "
                     "emissions, and test whether efficiency is flat "
                     "(sinks keeping up), declining (saturating), or "
                     "volatile (approaching instability). Proposed "
                     "mechanism: a public sink-efficiency dashboard updated "
                     "with each Global Carbon Budget release, with "
                     "mechanism-watch indicators (tropical forest carbon "
                     "balance, Southern Ocean uptake, permafrost-adjacent "
                     "soil respiration). What would confirm it: efficiency "
                     "trends that predict the next five years' airborne "
                     "fraction better than model means. What would kill it: "
                     "efficiency metrics dominated by El Nino noise with no "
                     "extractable trend, or inversions that disagree on the "
                     "land-ocean split beyond the dashboard's uncertainty. "
                     "What it does NOT claim: that sinks will collapse - "
                     "the dashboard reports the trend honestly, and a flat "
                     "efficiency line is a valid, reassuring result."),
        "key_points": [
            "Land and ocean absorb ~half of human CO2 emissions; airborne fraction ~45%.",
            "CO2 fertilization faces nitrogen and phosphorus limits.",
            "Warming raises soil respiration and wildfire emissions.",
            "Ocean uptake slows as surface waters warm and stratify.",
            "El Nino years reveal the land sink's sensitivity.",
        ],
        "requirements": [
            "Yearly land and ocean sink-efficiency series from inversions and surveys.",
            "Efficiency plotted against cumulative emissions to detect saturation.",
            "Mechanism-watch proxies: tropical forest balance, Southern Ocean uptake, soil respiration.",
        ],
        "standards": ["Global Carbon Budget (annual); IPCC AR6 WGI Chapter 5 (carbon cycle)"],
        "citations": CIT_BASE + [
            "Friedlingstein P et al. Global Carbon Budget (annual updates). "
            "Earth System Science Data; 2022 and updates.",
        ],
        "demo": {
            "quantity": "atmospheric CO2 added by 100 GtCO2 emissions", "unit": "ppm",
            "calc": "carbon", "gtco2": 100.0, "airborne": 0.45,
            "assumptions": [("emissions (GtCO2)", 100.0, [50.0, 100.0, 200.0]),
                            ("airborne fraction", 0.45, [0.35, 0.45, 0.60])],
            "formula": "ppm = GtCO2 * airborne_fraction / 7.81",
            "checks": [((100.0, 0.45), 5.761, 0.01), ((200.0, 0.60), 15.365, 0.02)],
            "steps": [
                "Step 1: compute yearly land and ocean sink efficiency separately.",
                "Step 2: plot efficiency against cumulative emissions.",
                "Step 3: classify each sink as keeping up, saturating, or volatile.",
                "Step 4: watch mechanism proxies (nutrients, respiration, stratification).",
                "Step 5: update the dashboard with each Global Carbon Budget release.",
            ],
            "confirm": [
                "Efficiency trends predict the next five years' airborne fraction.",
                "Land-ocean split is consistent across inversion systems.",
            ],
            "refute": [
                "Efficiency is pure El Nino noise with no extractable trend.",
                "Inversions disagree on the land-ocean split beyond stated uncertainty.",
            ],
            "note": "Sink-efficiency dashboard explorer for land and ocean carbon sinks.",
        },
    },
    {
        "key": "permafrost-carbon",
        "name": "The Permafrost Carbon Time Bomb",
        "group": "Compounded",
        "ladder_rank": 15, "ladder_tier": "compounded",
        "problem": ("Permafrost soils hold roughly 1,500 gigatons of carbon "
                    "- about twice the carbon currently in the atmosphere. "
                    "As the Arctic warms, thawing permafrost releases CO2 "
                    "and methane, but how fast, how much, and on what "
                    "timescale remains deeply uncertain: estimates of the "
                    "permafrost carbon feedback this century span an order "
                    "of magnitude."),
        "background": ("Permafrost carbon accumulated over tens of thousands "
                       "of years as dead plant matter froze before it could "
                       "decompose. Thaw exposes it to microbes; waterlogged "
                       "thaw produces methane (far more potent per molecule "
                       "than CO2), while drier thaw produces CO2. Abrupt "
                       "thaw - thermokarst collapse, where ground ice melts "
                       "and the land surface caves in - can release carbon "
                       "far faster than gradual top-down thaw, and is poorly "
                       "represented in models. Current best estimates suggest "
                       "permafrost emissions could add tens to a few hundred "
                       "gigatons of CO2-equivalent this century - significant "
                       "but smaller than fossil emissions - yet the "
                       "uncertainty is dominated by abrupt thaw and by "
                       "whether increased plant growth offsets some losses."),
        "why_it_matters": ("Permafrost carbon is not counted in most "
                           "national emissions pledges, yet it could consume "
                           "a meaningful slice of the remaining carbon "
                           "budget on its own. An abrupt-thaw surprise would "
                           "be a one-way ratchet: thawed carbon cannot be "
                           "refrozen on human timescales."),
        "sig_pointer": ("The Signature edition proposes a thaw-mode ledger "
                        "separating gradual from abrupt thaw with distinct "
                        "clocks. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) gradual top-down thaw "
                     "and abrupt thermokarst thaw are distinct processes "
                     "with distinct timescales and must be ledgered "
                     "separately; (2) methane vs CO2 split depends on "
                     "waterlogging, observable from surface hydrology; (3) "
                     "plant-growth offsets can be bounded from greening "
                     "trends. Reasoning path: build two clocks - a slow "
                     "clock for active-layer deepening (decades to "
                     "centuries, CO2-dominated) and a fast clock for "
                     "thermokarst collapse (years to decades, "
                     "methane-enriched) - score each from remote sensing "
                     "(subsidence, lake drainage, greening) and field "
                     "flux measurements, and sum with the offset ledger. "
                     "Proposed mechanism: a dual-clock ledger that reports "
                     "permafrost emissions as 'gradual + abrupt - greening "
                     "offset', each term with its own uncertainty, so a "
                     "surge in abrupt thaw shows up immediately rather than "
                     "hiding inside a model mean. What would confirm it: "
                     "the ledger's total tracks atmospheric methane and CO2 "
                     "growth anomalies over Arctic source regions. What "
                     "would kill it: abrupt-thaw area that cannot be "
                     "mapped at scale, or flux measurements that contradict "
                     "the clock separation. What it does NOT claim: that a "
                     "runaway 'methane bomb' is likely - the ledger's fast "
                     "clock quantifies abrupt thaw honestly, and current "
                     "evidence bounds it well below catastrophic "
                     "single-decade release scenarios."),
        "key_points": [
            "Permafrost holds ~1,500 GtC, about twice atmospheric carbon.",
            "Waterlogged thaw yields methane; drier thaw yields CO2.",
            "Abrupt thermokarst thaw is faster and poorly modeled.",
            "This-century estimates span tens to hundreds of GtCO2-equivalent.",
            "Thawed carbon cannot be refrozen on human timescales.",
        ],
        "requirements": [
            "Separate gradual-thaw and abrupt-thaw clocks with distinct timescales.",
            "Methane/CO2 split from surface hydrology observations.",
            "Greening-offset bounds from vegetation trends.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 5 (permafrost carbon feedback); Chapter 9 (cryosphere)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "permafrost carbon released this century (mid scenario)", "unit": "GtC",
            "calc": "expr", "expr": "a0 + a1 - a2", "base": 0.0,
            "assumptions": [("gradual thaw release (GtC)", 60, [20, 60, 120]),
                            ("abrupt thaw release (GtC)", 30, [5, 30, 80]),
                            ("greening offset (GtC)", 15, [0, 15, 40])],
            "formula": "net_GtC = gradual + abrupt - offset",
            "checks": [((60, 30, 15), 75, 0.5), ((120, 80, 0), 200, 0.5)],
            "steps": [
                "Step 1: map gradual active-layer deepening from boreholes and models.",
                "Step 2: map abrupt thermokarst area from remote sensing.",
                "Step 3: assign methane/CO2 splits from surface hydrology.",
                "Step 4: bound the greening offset from vegetation trends.",
                "Step 5: report net as gradual + abrupt - offset with full uncertainty.",
            ],
            "confirm": [
                "Ledger totals track Arctic atmospheric methane/CO2 anomalies.",
                "Abrupt-thaw area maps converge across sensors.",
            ],
            "refute": [
                "Abrupt-thaw area cannot be mapped at scale.",
                "Flux measurements contradict the clock separation.",
            ],
            "note": "Dual-clock ledger explorer for permafrost carbon release.",
        },
    },
    {
        "key": "amoc-slowdown",
        "name": "AMOC Slowdown: Will the Atlantic Current Stall",
        "group": "Compounded",
        "ladder_rank": 16, "ladder_tier": "compounded",
        "problem": ("The Atlantic Meridional Overturning Circulation (AMOC) - "
                    "the system including the Gulf Stream that carries warm "
                    "water north and returns cold water south - is at its "
                    "weakest in a millennium according to proxy "
                    "reconstructions, and models project further weakening. "
                    "Whether it could collapse entirely this century, as it "
                    "has in the paleoclimate past, and what early warnings "
                    "would look like, is fiercely debated."),
        "background": ("The AMOC moves about 15-20 million cubic meters of "
                       "water per second northward, warming northwestern "
                       "Europe by several degrees relative to its latitude. "
                       "Direct measurements (the RAPID array since 2004) "
                       "show variability but are too short for trends; proxy "
                       "studies suggest a ~15 percent weakening since the "
                       "mid-20th century, driven by Greenland meltwater and "
                       "Arctic freshening reducing North Atlantic density. "
                       "The 2021 IPCC assessment judged a collapse before "
                       "2100 unlikely but could not rule it out; a 2023-2024 "
                       "flurry of papers argued early-warning signals in "
                       "sea-surface temperatures suggest a tipping point "
                       "this century - claims other researchers strongly "
                       "dispute as statistical artifacts. Paleoclimate shows "
                       "AMOC shutdowns (Heinrich events) with dramatic "
                       "European cooling."),
        "why_it_matters": ("An AMOC collapse would cool northwestern Europe "
                           "by several degrees even as the world warms, "
                           "shift tropical rain belts, accelerate US East "
                           "Coast sea-level rise, and disrupt marine "
                           "ecosystems - a regional catastrophe inside a "
                           "global warming trend. The policy question is "
                           "whether to insure against a low-probability, "
                           "high-impact event this century."),
        "sig_pointer": ("The Signature edition proposes an early-warning "
                        "scorecard grading each claimed tipping signal. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) claimed early-warning "
                     "signals (fingerprint SST patterns, variance changes, "
                     "autocorrelation rises) can be graded on statistical "
                     "rigor independently of the tipping claim; (2) RAPID "
                     "direct measurements, proxies, and models are three "
                     "separate witnesses; (3) a real approaching tipping "
                     "point must show consilience across witnesses. "
                     "Reasoning path: build a scorecard where each "
                     "early-warning paper's signal is graded on data length, "
                     "statistical method, and physical mechanism - then "
                     "require agreement across the three witnesses before "
                     "any 'tipping likely' verdict. Proposed mechanism: a "
                     "public AMOC watch table with rows for each signal, "
                     "columns for each witness, and cells graded on "
                     "evidence - updated as RAPID lengthens and new papers "
                     "arrive. What would confirm it: the watch table's "
                     "consilience score predicts the next decade of RAPID "
                     "transport measurements. What would kill it: claimed "
                     "signals that fail replication in longer records, or "
                     "witnesses that permanently disagree (showing the "
                     "question is undecidable on current data). What it does "
                     "NOT claim: that collapse is or is not coming - the "
                     "table reports the evidence state, and 'undecidable on "
                     "current data' is an allowed, honest cell value."),
        "key_points": [
            "AMOC carries warm water north, warming NW Europe several degrees.",
            "Proxies suggest weakest state in a millennium; ~15% weakening since mid-20th century.",
            "RAPID array (since 2004) too short for trend detection.",
            "AR6: collapse before 2100 unlikely but not ruled out.",
            "Early-warning claims (2023-2024) are statistically disputed.",
        ],
        "requirements": [
            "Scorecard grading each early-warning signal on rigor.",
            "Consilience required across RAPID, proxies, and models.",
            "Watch table updated as records lengthen.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 9 (AMOC assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "AMOC watch consilience score", "unit": "points/100",
            "calc": "min", "base": 0.0,
            "assumptions": [("RAPID witness score", 45, [20, 45, 70]),
                            ("proxy witness score", 55, [20, 55, 80]),
                            ("model witness score", 50, [20, 50, 75])],
            "formula": "consilience = min of the three witness scores (weakest link)",
            "checks": [((45, 55, 50), 45, 0.5), ((70, 80, 75), 70, 0.5)],
            "steps": [
                "Step 1: list every claimed early-warning signal as a table row.",
                "Step 2: grade each signal on data length, method, and mechanism.",
                "Step 3: score the three witnesses (RAPID, proxies, models) separately.",
                "Step 4: require cross-witness consilience before any tipping verdict.",
                "Step 5: update the watch table as records lengthen.",
            ],
            "confirm": [
                "Consilience score predicts the next decade of RAPID transport.",
                "Signals replicate in lengthened records.",
            ],
            "refute": [
                "Claimed signals fail replication in longer records.",
                "Witnesses permanently disagree, showing undecidability on current data.",
            ],
            "note": "Early-warning scorecard explorer for AMOC stability.",
        },
    },
    {
        "key": "hurricane-response",
        "name": "Hurricanes in a Warmer World: Fewer or Stronger",
        "group": "Compounded",
        "ladder_rank": 17, "ladder_tier": "compounded",
        "problem": ("Warmer oceans hold more storm energy, yet the number of "
                    "tropical cyclones may stay flat or even decline - while "
                    "the strongest storms intensify and rainfall rates "
                    "climb. Observations show the proportion of major "
                    "hurricanes increasing and storms intensifying faster, "
                    "but the short, noisy historical record and changing "
                    "observation technology make the trend attribution "
                    "uncertain."),
        "background": ("Theory (potential intensity) says maximum storm "
                       "strength rises with sea-surface temperature - about "
                       "5 percent stronger winds per degree in many "
                       "estimates - and rainfall rises with moisture (~7 "
                       "percent per degree). But storm *number* depends on "
                       "seed disturbances and wind shear, whose future is "
                       "murky; most models project fewer total storms. "
                       "Observed trends: the fraction of Category 4-5 storms "
                       "has risen, rapid intensification events are more "
                       "common, and storms are migrating poleward with "
                       "slower forward motion (Harvey's 2017 stall over "
                       "Houston being the costly archetype). The satellite "
                       "era begins only in the 1970s-80s, and earlier "
                       "records miss storms that never threatened ships - "
                       "so 'more storms' can be an artifact of better "
                       "detection."),
        "why_it_matters": ("Hurricane damage scales roughly with the cube "
                           "of wind speed - a small intensity shift means a "
                           "large damage shift. Coastal building codes, "
                           "insurance markets, and evacuation planning need "
                           "to know whether to prepare for more storms, "
                           "stronger storms, wetter storms, or all three."),
        "sig_pointer": ("The Signature edition proposes a storm-ledger "
                        "scoring frequency, intensity, rainfall, and speed "
                        "as separate accounts. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) frequency, peak "
                     "intensity, rainfall rate, and translation speed are "
                     "separable storm properties with different physics and "
                     "different evidence quality; (2) detection-bias "
                     "corrections can be bounded from the satellite era "
                     "onward; (3) potential-intensity theory is the anchor "
                     "for the intensity account. Reasoning path: build a "
                     "four-account storm ledger - how many, how strong, how "
                     "wet, how slow - score each account's observed trend "
                     "and projected change separately with evidence grades, "
                     "and refuse to let a strong account (rainfall) launder "
                     "a weak one (frequency). Proposed mechanism: a "
                     "hurricane report card with four letter grades, updated "
                     "each season, so 'stronger but not more numerous' is a "
                     "scored statement rather than a slogan. What would "
                     "confirm it: the ledger's accounts predict the next "
                     "decade's landfall damage distribution better than any "
                     "single-number trend. What would kill it: accounts "
                     "whose trends reverse when detection corrections are "
                     "applied differently, or damage records that refuse to "
                     "follow the intensity account. What it does NOT claim: "
                     "that any single storm was 'caused' by warming - the "
                     "ledger scores shifts in storm properties, not "
                     "individual event causation."),
        "key_points": [
            "Potential intensity theory: max storm strength rises with ocean temperature.",
            "Most models project fewer total storms but a higher fraction of major ones.",
            "Rainfall rises ~7% per degree; rapid intensification events increasing.",
            "Storms migrating poleward with slower forward motion (Harvey 2017 archetype).",
            "Pre-satellite records undercount storms; detection bias corrections matter.",
        ],
        "requirements": [
            "Four separate accounts: frequency, intensity, rainfall, translation speed.",
            "Detection-bias bounds for each account.",
            "Damage-distribution verification over the next decade.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 11 (tropical cyclone assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "hurricane damage potential index", "unit": "relative units",
            "calc": "expr", "expr": "(1+a0/100)**3 * (1+a1/100) * (1+a2/100)", "base": 1.0,
            "assumptions": [("peak wind change (%)", 5, [0, 5, 10]),
                            ("rainfall change (%)", 7, [0, 7, 14]),
                            ("frequency change (%)", -5, [-15, -5, 5])],
            "formula": "damage ~= (1+wind/100)^3 * (1+rain/100) * (1+freq/100); baseline 1.0",
            "checks": [((5, 7, -5), 1.1767, 0.002), ((0, 0, 0), 1.0, 0.0005)],
            "steps": [
                "Step 1: separate frequency, intensity, rainfall, and speed accounts.",
                "Step 2: bound detection bias for each account from the satellite era.",
                "Step 3: anchor the intensity account in potential-intensity theory.",
                "Step 4: score each account's trend with an evidence grade.",
                "Step 5: verify against landfall damage distributions each decade.",
            ],
            "confirm": [
                "Ledger accounts predict the next decade's damage distribution.",
                "Trends survive alternative detection-bias corrections.",
            ],
            "refute": [
                "Trends reverse under different detection corrections.",
                "Damage records refuse to follow the intensity account.",
            ],
            "note": "Four-account storm ledger explorer for hurricane response.",
        },
    },
    {
        "key": "monsoon-warming",
        "name": "Monsoons Under Global Warming",
        "group": "Compounded",
        "ladder_rank": 18, "ladder_tier": "compounded",
        "problem": ("Monsoons water the crops of more than half of "
                    "humanity, and their response to warming is a tug of "
                    "war: thermodynamics says more moisture and heavier "
                    "downpours, while circulation changes may weaken the "
                    "monsoon winds themselves. Models project wetter "
                    "monsoons overall with drier spells between - but the "
                    "regional details, especially for South Asia and West "
                    "Africa, remain uncertain."),
        "background": ("The South Asian monsoon weakened from the 1950s to "
                       "the 2000s - partly from aerosol dimming over India "
                       "countering greenhouse warming - then recovered as "
                       "aerosols declined, a real-world aerosol-monsoon "
                       "experiment. The West African monsoon collapsed into "
                       "the Sahel drought of the 1970s-80s (linked to "
                       "Atlantic aerosol and SST patterns) then partially "
                       "recovered. Models robustly project increased monsoon "
                       "precipitation totals with warming (more moisture in "
                       "the air) but disagree on circulation strength, onset "
                       "timing, and the distribution between downpours and "
                       "dry breaks - the details farmers actually live by."),
        "why_it_matters": ("Two billion people depend on monsoon rains for "
                           "food. 'Wetter on average but with longer dry "
                           "breaks' is a profoundly different farming "
                           "reality than 'steadily wetter' - getting the "
                           "sub-seasonal structure right is a food-security "
                           "question, not an academic one."),
        "sig_pointer": ("The Signature edition proposes a monsoon ledger "
                        "separating moisture supply from circulation strength. "
                        + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) monsoon rainfall can be "
                     "decomposed into moisture-supply (thermodynamic, "
                     "robust) and circulation-strength (dynamic, fragile) "
                     "terms; (2) the 1950-2000 aerosol dimming episode is a "
                     "calibration experiment for the circulation term; (3) "
                     "sub-seasonal structure (onset, breaks, withdrawal) can "
                     "be scored from rain-gauge and satellite records. "
                     "Reasoning path: for each monsoon system (South Asian, "
                     "West African, East Asian, North American), score the "
                     "moisture term from observed humidity trends and the "
                     "circulation term from wind records, then project each "
                     "term forward separately with its own uncertainty - so "
                     "the robust wetting and the fragile circulation sit in "
                     "different ledger rows. Proposed mechanism: a "
                     "per-monsoon ledger table with moisture and circulation "
                     "rows plus a sub-seasonal structure panel (onset date, "
                     "break frequency, withdrawal), updated yearly. What "
                     "would confirm it: the ledger's moisture rows verify "
                     "against observed rainfall totals while circulation rows "
                     "correctly hindcast the 1950-2000 weakening. What would "
                     "kill it: circulation terms that cannot be scored from "
                     "wind observations, or sub-seasonal structure that "
                     "defies decomposition. What it does NOT claim: a "
                     "reliable forecast of any single monsoon season - the "
                     "ledger addresses the forced trend, and interannual "
                     "variability (ENSO and friends) remains the dominant "
                     "year-to-year driver."),
        "key_points": [
            "Monsoons feed over half of humanity's crops.",
            "Thermodynamics: more moisture, heavier downpours (robust). Circulation: possibly weaker winds (fragile).",
            "South Asian monsoon weakened 1950s-2000s from aerosol dimming, then recovered.",
            "Sahel drought (1970s-80s) linked to Atlantic aerosols and SST patterns.",
            "Models agree on wetter totals, disagree on timing and dry-break structure.",
        ],
        "requirements": [
            "Per-monsoon decomposition into moisture and circulation terms.",
            "Calibration of the circulation term against the aerosol-dimming episode.",
            "Sub-seasonal structure panel: onset, breaks, withdrawal.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 8 (monsoon assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "monsoon seasonal rainfall change", "unit": "%",
            "calc": "expr", "expr": "a0 + a1", "base": 0.0,
            "assumptions": [("moisture-supply term (%)", 7, [3, 7, 12]),
                            ("circulation-strength term (%)", -3, [-8, -3, 2])],
            "formula": "rainfall_change = moisture_term + circulation_term",
            "checks": [((7, -3), 4, 0.05), ((12, 2), 14, 0.05), ((3, -8), -5, 0.05)],
            "steps": [
                "Step 1: decompose monsoon rainfall into moisture and circulation terms.",
                "Step 2: score the moisture term from humidity trends.",
                "Step 3: calibrate the circulation term against the aerosol-dimming episode.",
                "Step 4: score sub-seasonal structure (onset, breaks, withdrawal).",
                "Step 5: verify moisture rows against observed totals yearly.",
            ],
            "confirm": [
                "Moisture rows verify against observed rainfall totals.",
                "Circulation rows hindcast the 1950-2000 weakening.",
            ],
            "refute": [
                "Circulation terms cannot be scored from wind observations.",
                "Sub-seasonal structure defies the decomposition.",
            ],
            "note": "Moisture-circulation ledger explorer for monsoon response.",
        },
    },
    {
        "key": "enso-warming",
        "name": "The El Nino Response to Warming",
        "group": "Compounded",
        "ladder_rank": 19, "ladder_tier": "compounded",
        "problem": ("El Nino and La Nina (ENSO) are the planet's dominant "
                    "year-to-year climate swing, teleconnecting droughts, "
                    "floods, and hurricanes worldwide. Whether warming will "
                    "make El Ninos stronger, more frequent, or shift their "
                    "flavor (eastern vs central Pacific) is unresolved - "
                    "models famously disagree, with no consensus on even "
                    "the sign of change."),
        "background": ("ENSO arises from coupled ocean-atmosphere feedbacks "
                       "in the tropical Pacific (Bjerknes feedback). The "
                       "observational record shows strong events (1982-83, "
                       "1997-98, 2015-16) but is too short to separate "
                       "forced change from natural multidecadal swings. "
                       "Theory pulls both ways: a warmer background could "
                       "strengthen the thermocline feedback (stronger "
                       "events) or weaken the east-west temperature "
                       "gradient (weaker events). CMIP6 models split "
                       "roughly evenly. Paleoclimate corals suggest ENSO "
                       "has varied greatly across millennia without a "
                       "simple temperature link - and the 2023-24 El Nino "
                       "arrived amid record global warmth, sharpening the "
                       "question of what 'normal' even means now."),
        "why_it_matters": ("ENSO phase predicts harvests, water supplies, "
                           "wildfire seasons, and hurricane activity months "
                           "ahead across the tropics and beyond. If the "
                           "background state shifts toward more extreme El "
                           "Ninos, the world's best seasonal forecast tool "
                           "needs recalibration - and billions in "
                           "agriculture and disaster planning ride on it."),
        "sig_pointer": ("The Signature edition proposes a flavor-ledger "
                        "scoring eastern vs central Pacific events "
                        "separately. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) 'El Nino' is not one "
                     "thing - eastern-Pacific (canonical) and "
                     "central-Pacific (Modoki) flavors have different "
                     "teleconnections and possibly different warming "
                     "responses; (2) the Bjerknes feedback components "
                     "(thermocline, zonal advective, Ekman) can be scored "
                     "separately from observations; (3) the short "
                     "instrumental record must be extended with coral "
                     "paleoclimate data, graded for fidelity. Reasoning "
                     "path: build a flavor ledger - for each flavor, score "
                     "its feedback components' trends, its teleconnection "
                     "strength, and its paleoclimate context - and report "
                     "'no consensus' honestly where models split, while "
                     "naming the specific feedback disagreement. Proposed "
                     "mechanism: an ENSO watch ledger with flavor rows and "
                     "feedback-component columns, updated with each major "
                     "event, that converts 'models disagree' into 'models "
                     "disagree about the thermocline feedback because...'. "
                     "What would confirm it: the ledger's feedback scores "
                     "predict the character of the next major El Nino "
                     "better than model-mean forecasts. What would kill it: "
                     "feedback components that cannot be scored from "
                     "observations, or coral records that contradict the "
                     "instrumental feedback story. What it does NOT claim: "
                     "a prediction of stronger or weaker future El Ninos - "
                     "the ledger's honest output may be 'unresolved', with "
                     "the disagreement precisely located."),
        "key_points": [
            "ENSO is the dominant year-to-year climate swing with global teleconnections.",
            "Theory pulls both ways on future strength; CMIP6 models split roughly evenly.",
            "Eastern-Pacific vs central-Pacific (Modoki) flavors differ in impacts.",
            "Coral records show large natural ENSO variability across millennia.",
            "The instrumental record is too short to isolate forced change.",
        ],
        "requirements": [
            "Flavor-separated ledger: canonical vs Modoki events.",
            "Feedback-component scores (thermocline, advective, Ekman) from observations.",
            "Coral paleoclimate extension graded for fidelity.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 8 (ENSO assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "ENSO flavor ledger score", "unit": "points/100",
            "calc": "min", "base": 0.0,
            "assumptions": [("thermocline feedback score", 55, [30, 55, 80]),
                            ("zonal advective feedback score", 50, [30, 50, 75]),
                            ("paleoclimate context score", 60, [30, 60, 85])],
            "formula": "ledger = min of component scores (weakest link); verdict needs >=60",
            "checks": [((55, 50, 60), 50, 0.5), ((80, 75, 85), 75, 0.5)],
            "steps": [
                "Step 1: separate El Nino flavors (canonical vs Modoki).",
                "Step 2: score each Bjerknes feedback component from observations.",
                "Step 3: extend the record with graded coral paleoclimate data.",
                "Step 4: locate the precise feedback disagreement behind model splits.",
                "Step 5: update the ledger with each major event.",
            ],
            "confirm": [
                "Feedback scores predict the next major El Nino's character.",
                "The disagreement is precisely located in one feedback component.",
            ],
            "refute": [
                "Feedback components cannot be scored from observations.",
                "Coral records contradict the instrumental feedback story.",
            ],
            "note": "Flavor-ledger explorer for the ENSO warming response.",
        },
    },
    {
        "key": "southern-ocean-sink",
        "name": "The Southern Ocean Carbon Sink Puzzle",
        "group": "Compounded",
        "ladder_rank": 20, "ladder_tier": "compounded",
        "problem": ("The Southern Ocean absorbs a large share of the "
                    "ocean's anthropogenic CO2 and heat, yet its carbon "
                    "uptake appeared to stall in the 1990s-2000s (linked to "
                    "westerly wind shifts from ozone depletion), then "
                    "reinvigorate in the 2010s. Whether the sink is "
                    "saturating, recovering, or just varying - and how it "
                    "will behave as ozone recovers and winds evolve - is "
                    "unsettled."),
        "background": ("The Southern Ocean's uptake is driven by fierce "
                       "westerly winds driving upwelling and by cold waters' "
                       "high CO2 solubility. In the 2000s, analyses of "
                       "sparse ship data suggested the sink had weakened as "
                       "the Southern Annular Mode shifted poleward (partly "
                       "an ozone-hole effect). Then the 2010s brought a "
                       "rebound in uptake estimates - though the sparse "
                       "winter observations (few ships brave the Southern "
                       "Ocean in winter) mean the 'reinvigoration' itself "
                       "is debated, with some arguing it is a sampling "
                       "artifact. New biogeochemical Argo floats are "
                       "finally filling the winter gap, and early results "
                       "are revising the picture again."),
        "why_it_matters": ("The Southern Ocean is the single largest "
                           "regional ocean carbon sink. Its behavior sets "
                           "the trajectory of the global ocean sink - and a "
                           "saturating Southern Ocean would remove the "
                           "safety net beneath the remaining carbon budget."),
        "sig_pointer": ("The Signature edition proposes a season-ledger "
                        "separating summer and winter uptake with "
                        "biogeochemical Argo. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the apparent "
                     "stall-and-recovery may be partly a winter-sampling "
                     "artifact, so seasons must be ledgered separately; (2) "
                     "biogeochemical Argo floats provide the first true "
                     "winter constraint; (3) wind-driven upwelling and "
                     "solubility are separable drivers with distinct "
                     "fingerprints. Reasoning path: build a season ledger - "
                     "summer uptake from the long ship record, winter uptake "
                     "from new float data - score the wind driver from "
                     "reanalysis and the solubility driver from temperature "
                     "trends, and test whether 'reinvigoration' survives "
                     "winter weighting. Proposed mechanism: a Southern "
                     "Ocean season ledger published with each float-data "
                     "release, showing summer, winter, and annual uptake "
                     "with sampling-uncertainty bars - so the debate moves "
                     "from 'which paper is right' to 'what does the winter "
                     "row say'. What would confirm it: winter float data "
                     "converging with ship-based summer estimates on the "
                     "annual total. What would kill it: persistent "
                     "float-ship disagreement beyond stated uncertainties, "
                     "or winter uptake that refuses to be bounded. What it "
                     "does NOT claim: that the sink is safe - the ledger "
                     "reports the annual number honestly, and a declining "
                     "annual row would be reported as declining."),
        "key_points": [
            "Southern Ocean is the largest regional ocean carbon sink.",
            "Uptake appeared to stall in the 1990s-2000s, then reinvigorate in the 2010s.",
            "Westerly wind shifts (ozone-hole linked) drove the stall.",
            "Winter observations are sparse; 'reinvigoration' may be partly a sampling artifact.",
            "Biogeochemical Argo floats are now filling the winter gap.",
        ],
        "requirements": [
            "Season-separated ledger: summer (ships) and winter (floats).",
            "Wind vs solubility driver decomposition.",
            "Convergence test between float and ship annual totals.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 5 (Southern Ocean carbon uptake); Chapter 9"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "Southern Ocean annual CO2 uptake", "unit": "GtC/yr",
            "calc": "expr", "expr": "a0 + a1 + a2", "base": 0.0,
            "assumptions": [("summer uptake (GtC/yr)", 1.2, [0.8, 1.2, 1.6]),
                            ("winter uptake (GtC/yr)", 0.6, [0.2, 0.6, 1.0]),
                            ("sampling bias correction (GtC/yr)", -0.2, [-0.4, -0.2, 0.0])],
            "formula": "annual = (summer + winter)/2 * 2 -> summer + winter + bias_correction",
            "checks": [((1.2, 0.6, -0.2), 1.6, 0.05), ((0.8, 0.2, -0.4), 0.6, 0.05)],
            "steps": [
                "Step 1: ledger summer uptake from the ship record.",
                "Step 2: ledger winter uptake from biogeochemical Argo floats.",
                "Step 3: apply sampling-bias corrections explicitly.",
                "Step 4: decompose wind-driven vs solubility drivers.",
                "Step 5: test float-ship convergence on the annual total.",
            ],
            "confirm": [
                "Winter float data converges with ship-based annual estimates.",
                "The reinvigoration survives winter weighting.",
            ],
            "refute": [
                "Float-ship disagreement persists beyond stated uncertainties.",
                "Winter uptake refuses to be bounded.",
            ],
            "note": "Season-ledger explorer for Southern Ocean carbon uptake.",
        },
    },
    {
        "key": "aerosol-cloud-indirect",
        "name": "Aerosol-Cloud Interactions: The Indirect Effect",
        "group": "Compounded",
        "ladder_rank": 21, "ladder_tier": "compounded",
        "problem": ("Beyond scattering sunlight directly, aerosols seed "
                    "cloud droplets - more particles mean more, smaller "
                    "droplets and brighter clouds (the Twomey effect), plus "
                    "possible changes in cloud lifetime and rain patterns. "
                    "These 'indirect effects' are assessed as a net cooling, "
                    "but their magnitude is among the least constrained "
                    "numbers in climate science, with estimates spanning "
                    "roughly -0.2 to -1.5 W/m2."),
        "background": ("The chain from aerosol particle to cloud brightness "
                       "runs through microscopic nucleation physics that "
                       "climate models cannot resolve - it must be "
                       "parameterized, and parameterizations disagree. "
                       "Ship tracks (bright cloud lines behind vessels) and "
                       "the 2020 shipping sulfur cap provide natural "
                       "experiments: early analyses of the sulfur cut "
                       "suggest a measurable cloud-brightness response, "
                       "offering a rare real-world calibration. Volcanic "
                       "eruptions provide another. Yet translating these "
                       "episodic, regional experiments into a global, "
                       "century-scale indirect forcing remains the hard "
                       "step - buffering processes (clouds adjusting to "
                       "resist the brightening) may substantially offset "
                       "the naive Twomey calculation."),
        "why_it_matters": ("The indirect effect is the murkiest half of the "
                           "already-uncertain aerosol forcing - and therefore "
                           "a major contributor to the ECS uncertainty via "
                           "the historical record. It is also the physics "
                           "that any future debate over marine cloud "
                           "brightening (a proposed geoengineering method) "
                           "would hinge on."),
        "sig_pointer": ("The Signature edition proposes a natural-experiment "
                        "ladder from ship tracks to the sulfur cap to "
                        "volcanoes. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) ship tracks, the 2020 "
                     "sulfur cap, and volcanic eruptions form a ladder of "
                     "natural experiments at increasing scale; (2) each "
                     "experiment measures a local indirect effect that "
                     "bounds, not equals, the global century-scale effect; "
                     "(3) buffering processes must be scored explicitly, "
                     "not assumed away. Reasoning path: score the Twomey "
                     "brightening in each experiment from satellite cloud "
                     "data, estimate the buffering offset from cloud "
                     "lifetime and rain-rate observations, and combine "
                     "into a bounded global estimate - with the bound, not "
                     "a point value, as the headline. Proposed mechanism: "
                     "an experiment ladder table (ship track -> sulfur cap "
                     "-> volcano -> global), each rung carrying its measured "
                     "brightening, its buffering offset, and its scale-up "
                     "uncertainty - making the path from observation to "
                     "global number fully auditable. What would confirm "
                     "it: the ladder's bounded estimate predicts the "
                     "cloud response of the next major volcanic eruption. "
                     "What would kill it: experiments whose brightening "
                     "signals vanish under reanalysis, or buffering that "
                     "proves unmeasurable (leaving the ladder without its "
                     "key rung). What it does NOT claim: a precise indirect "
                     "forcing number - the honest product is a narrowed "
                     "bound, and it says plainly how wide the bound "
                     "remains."),
        "key_points": [
            "Aerosols seed cloud droplets; more particles -> brighter clouds (Twomey effect).",
            "Indirect effect estimates span roughly -0.2 to -1.5 W/m2.",
            "Nucleation physics is unresolvable in models; parameterizations disagree.",
            "Ship tracks and the 2020 sulfur cap are natural experiments.",
            "Buffering processes may substantially offset naive brightening.",
        ],
        "requirements": [
            "Experiment ladder: ship tracks, sulfur cap, volcanoes, global.",
            "Measured brightening plus buffering offset per rung.",
            "Auditable scale-up from experiment to global century-scale number.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (aerosol-cloud interactions)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "global indirect aerosol effect (bounded)", "unit": "W/m2",
            "calc": "expr", "expr": "a0 + a1", "base": 0.0,
            "assumptions": [("Twomey brightening bound (W/m2)", -0.8, [-1.2, -0.8, -0.4]),
                            ("buffering offset (W/m2)", 0.3, [0.1, 0.3, 0.6])],
            "formula": "indirect = brightening + buffering_offset (offset opposes cooling)",
            "checks": [((-0.8, 0.3), -0.5, 0.01), ((-1.2, 0.1), -1.1, 0.01)],
            "steps": [
                "Step 1: score Twomey brightening in ship tracks from satellites.",
                "Step 2: score the 2020 sulfur-cap cloud response.",
                "Step 3: score volcanic-eruption cloud responses.",
                "Step 4: estimate buffering offsets from lifetime and rain observations.",
                "Step 5: combine into a bounded global estimate with auditable scale-up.",
            ],
            "confirm": [
                "The bounded estimate predicts the next major eruption's cloud response.",
                "Ladder rungs agree within stated scale-up uncertainties.",
            ],
            "refute": [
                "Experiment brightening signals vanish under reanalysis.",
                "Buffering proves unmeasurable, breaking the ladder.",
            ],
            "note": "Experiment-ladder explorer for aerosol-cloud indirect effects.",
        },
    },
    {
        "key": "stratosphere-troposphere",
        "name": "Stratosphere-Troposphere Coupling and Extreme Weather",
        "group": "Compounded",
        "ladder_rank": 22, "ladder_tier": "compounded",
        "problem": ("The stratospheric polar vortex - a winter whirlwind of "
                    "frigid air high above the Arctic - occasionally "
                    "collapses in 'sudden stratospheric warming' events, "
                    "and weeks later, cold extremes can strike the "
                    "mid-latitudes. The coupling is real, but how much of "
                    "mid-latitude winter extreme weather traces to the "
                    "stratosphere, and whether Arctic warming is changing "
                    "the vortex itself, remains contested."),
        "background": ("Sudden stratospheric warmings (SSWs) reverse the "
                       "polar vortex's winds and can displace frigid air "
                       "southward weeks later - the February 2021 Texas "
                       "freeze followed a January SSW, though attribution "
                       "of that specific link is debated. The Arctic's "
                       "rapid warming may be weakening the vortex or making "
                       "it wavier (the contested 'warm Arctic, cold "
                       "continents' pattern), but models disagree on the "
                       "vortex's future and on whether observed mid-latitude "
                       "cold extremes are increasing or decreasing. The "
                       "stratosphere also carries the ozone layer's "
                       "recovery story, which alters Southern Hemisphere "
                       "circulation - a second, better-understood coupling."),
        "why_it_matters": ("Winter cold extremes kill, burst pipes, and "
                           "collapse power grids (Texas 2021 cost over $100 "
                           "billion). If stratospheric forecasts extend "
                           "useful winter predictions by weeks, that is a "
                           "forecasting revolution; if the coupling is "
                           "overstated, resources chase a phantom."),
        "sig_pointer": ("The Signature edition proposes an SSW ledger "
                        "scoring each event's downward coupling. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) sudden stratospheric "
                     "warmings are discrete, countable events with "
                     "observable downward coupling (or its absence); (2) "
                     "each event can be scored on vortex disruption depth "
                     "and subsequent tropospheric response; (3) the Arctic "
                     "amplification-vortex link must be tested separately "
                     "from the SSW-coupling question. Reasoning path: "
                     "build an SSW ledger - every major event since 1979, "
                     "its vortex disruption magnitude, and the "
                     "mid-latitude cold-extreme response in the following "
                     "2-6 weeks - then compute the hit rate: what fraction "
                     "of SSWs actually deliver cold extremes, and what "
                     "fraction of cold extremes had an SSW precursor. "
                     "Proposed mechanism: a public SSW ledger with hit-rate "
                     "statistics, separating 'SSW then cold' from 'cold "
                     "without SSW', so the coupling's practical forecasting "
                     "value is a number, not a narrative. What would "
                     "confirm it: the ledger's hit rate verifies in "
                     "out-of-sample winters and beats naive climatology. "
                     "What would kill it: hit rates indistinguishable from "
                     "chance, or cold extremes that systematically lack SSW "
                     "precursors. What it does NOT claim: that any single "
                     "freeze (Texas 2021 included) was 'caused' by the "
                     "stratosphere - the ledger scores population "
                     "statistics, and individual attribution remains a "
                     "separate, harder question."),
        "key_points": [
            "Sudden stratospheric warmings can precede mid-latitude cold extremes by weeks.",
            "The February 2021 Texas freeze followed a January SSW; the link is debated.",
            "Arctic warming may alter the polar vortex, but models disagree.",
            "'Warm Arctic, cold continents' pattern is contested.",
            "Ozone recovery alters Southern Hemisphere circulation (better-understood coupling).",
        ],
        "requirements": [
            "SSW ledger: every event since 1979 with disruption magnitude.",
            "Hit-rate statistics: SSW->cold and cold->SSW-precursor fractions.",
            "Out-of-sample verification against naive climatology.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 8 (stratosphere-troposphere coupling)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "SSW-to-cold-extreme hit rate", "unit": "%",
            "calc": "expr", "expr": "100 * a1 / a0", "base": 0.0,
            "assumptions": [("SSW events per decade", 6, [4, 6, 8]),
                            ("cold extreme within 6 weeks (count)", 4, [2, 4, 6])],
            "formula": "hit_rate = 100 * cold_after_SSW / SSW_events",
            "checks": [((6, 4), 66.67, 0.1), ((8, 2), 25.0, 0.1)],
            "steps": [
                "Step 1: catalog every major SSW since 1979.",
                "Step 2: score each event's vortex disruption depth.",
                "Step 3: record mid-latitude cold extremes in the following 2-6 weeks.",
                "Step 4: compute both hit rates (SSW->cold, cold->SSW precursor).",
                "Step 5: verify out-of-sample against naive climatology.",
            ],
            "confirm": [
                "Hit rates verify in out-of-sample winters and beat climatology.",
                "The ledger stabilizes as events accumulate.",
            ],
            "refute": [
                "Hit rates indistinguishable from chance.",
                "Cold extremes systematically lack SSW precursors.",
            ],
            "note": "SSW ledger explorer for stratosphere-troposphere coupling.",
        },
    },
    {
        "key": "decadal-prediction",
        "name": "Decadal Climate Prediction: Forecasting the Next Ten Years",
        "group": "Compounded",
        "ladder_rank": 23, "ladder_tier": "compounded",
        "problem": ("Weather forecasts run days, seasonal forecasts months, "
                    "and century projections assume scenarios - but the "
                    "decade ahead, the horizon businesses and governments "
                    "actually plan on, sits in between. Initialized decadal "
                    "predictions show real skill for ocean temperatures "
                    "(especially the North Atlantic), yet skill over land - "
                    "where people live - remains modest and contested."),
        "background": ("Decadal prediction initializes climate models with "
                       "the observed ocean state, like weather forecasting "
                       "but for years. The international CMIP decadal "
                       "experiments show significant skill for North Atlantic "
                       "sea-surface temperatures and the Atlantic "
                       "multidecadal signal - a genuine achievement. But "
                       "land temperature skill largely rides on the forced "
                       "warming trend (which uninitialized projections also "
                       "capture), and the added value of initialization over "
                       "land is small. The Pacific decadal signal - crucial "
                       "for North American water - shows stubbornly low "
                       "skill. The field's honest question: can initialization "
                       "ever beat the forced trend plus statistical "
                       "baselines over land, or is the decade horizon "
                       "intrinsically low-skill there?"),
        "why_it_matters": ("Water utilities, farmers, insurers, and "
                           "infrastructure planners live on the 5-15 year "
                           "horizon. Skillful decadal forecasts would be "
                           "worth billions in avoided losses; oversold "
                           "forecasts would misallocate those same billions. "
                           "The field must advertise exactly where skill "
                           "exists and where it does not."),
        "sig_pointer": ("The Signature edition proposes a skill-map with "
                        "honest geography: where initialization beats the "
                        "trend, and where it does not. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) skill must be measured "
                     "against two baselines - the forced trend and "
                     "persistence - not against zero; (2) skill geography "
                     "matters more than global-mean skill; (3) a forecast "
                     "system that cannot beat baselines over land should say "
                     "so. Reasoning path: for each region and variable, "
                     "score initialized decadal hindcasts against the "
                     "forced-trend baseline and the persistence baseline, "
                     "and publish a skill map colored by 'initialization "
                     "adds value here' vs 'trend alone does as well'. "
                     "Proposed mechanism: a public decadal skill atlas - "
                     "region by region, variable by variable - with the "
                     "baselines shown alongside, updated with each CMIP "
                     "decadal round, so users see the honest geography of "
                     "skill. What would confirm it: the atlas's "
                     "'adds value' regions verify in the next forecast "
                     "round while 'no value' regions stay flat. What would "
                     "kill it: skill that evaporates when baselines are "
                     "computed more carefully, or 'no value' regions that "
                     "suddenly verify (showing the atlas misjudges "
                     "predictability). What it does NOT claim: that decadal "
                     "forecasting is solved or hopeless - the atlas reports "
                     "the measured geography, and its blank areas are as "
                     "informative as its colored ones."),
        "key_points": [
            "Decadal prediction initializes models with the observed ocean state.",
            "Real skill exists for North Atlantic sea-surface temperatures.",
            "Land skill largely rides the forced trend; initialization adds little.",
            "Pacific decadal signal shows stubbornly low skill.",
            "The 5-15 year horizon is what planners actually use.",
        ],
        "requirements": [
            "Skill scored against forced-trend AND persistence baselines.",
            "Regional skill atlas, not global-mean scores.",
            "Verification in each new CMIP decadal round.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 4 (near-term climate prediction); CMIP decadal experiments"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "decadal skill added by initialization (land)", "unit": "correlation points",
            "calc": "expr", "expr": "a0 - a1", "base": 0.0,
            "assumptions": [("initialized hindcast correlation", 0.65, [0.4, 0.65, 0.85]),
                            ("forced-trend baseline correlation", 0.60, [0.4, 0.60, 0.8])],
            "formula": "added_skill = initialized - baseline (must clear 0.05 to count)",
            "checks": [((0.65, 0.60), 0.05, 0.001), ((0.85, 0.40), 0.45, 0.001)],
            "steps": [
                "Step 1: choose baselines (forced trend, persistence) before scoring.",
                "Step 2: score initialized hindcasts region by region.",
                "Step 3: color the skill atlas by where initialization adds value.",
                "Step 4: publish baselines alongside every skill claim.",
                "Step 5: verify the atlas in each new decadal forecast round.",
            ],
            "confirm": [
                "'Adds value' regions verify in the next forecast round.",
                "The atlas geography is stable across model generations.",
            ],
            "refute": [
                "Skill evaporates under more careful baselines.",
                "'No value' regions suddenly verify, misjudging predictability.",
            ],
            "note": "Skill-atlas explorer for decadal climate prediction.",
        },
    },
]

ENTRIES += [
    # ------------------------------------------------- 3 ADVANCED
    {
        "key": "pattern-effect",
        "name": "The Pattern Effect: Why Sensitivity Depends on Where Warming Happens",
        "group": "Advanced",
        "ladder_rank": 24, "ladder_tier": "advanced",
        "problem": ("Climate sensitivity inferred from the historical record "
                    "comes out lower than sensitivity inferred from models "
                    "and paleoclimate - and the 'pattern effect' may explain "
                    "why: the geographic pattern of recent warming (strong "
                    "in the western Pacific warm pool, muted in the eastern "
                    "Pacific and Southern Ocean) produces a more negative "
                    "cloud and lapse-rate feedback than the pattern expected "
                    "under long-term CO2 forcing. Quantifying this "
                    "pattern-dependent feedback shift is an active, "
                    "unsettled frontier."),
        "background": ("The puzzle emerged as researchers noticed the "
                       "instrumental record implies ECS near 2-2.5 C while "
                       "other lines point to ~3 C. The proposed resolution: "
                       "feedback strength depends on the sea-surface "
                       "temperature pattern. Warming concentrated in regions "
                       "of deep atmospheric ascent (the western Pacific) "
                       "strengthens the negative lapse-rate feedback and "
                       "dampens positive cloud feedbacks - temporarily "
                       "masking the true long-run sensitivity. As the "
                       "pattern evolves toward the long-term forced pattern, "
                       "sensitivity 'unmasks'. The effect is supported by "
                       "atmosphere-only model experiments with prescribed "
                       "SST patterns, but its magnitude - anywhere from a "
                       "few tenths of a degree to over a degree of ECS "
                       "equivalent - is debated, and some argue internal "
                       "variability, not pattern physics, dominates the "
                       "discrepancy."),
        "why_it_matters": ("If the pattern effect is large, the historical "
                           "record understates long-run sensitivity - meaning "
                           "future warming per unit CO2 will exceed what the "
                           "last 150 years suggest. Carbon budgets built on "
                           "the instrumental sensitivity would then be "
                           "overly generous."),
        "sig_pointer": ("The Signature edition proposes a pattern-ledger "
                        "that scores feedbacks by SST pattern regime. " +
                        SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) feedback strength is a "
                     "function of SST pattern, measurable in "
                     "atmosphere-only experiments with prescribed patterns; "
                     "(2) the observed historical pattern and the projected "
                     "long-term pattern are both known well enough to "
                     "difference; (3) the pattern effect and internal "
                     "variability can be separated by pattern-scaling "
                     "experiments. Reasoning path: run the ledger in three "
                     "columns - feedbacks under the observed historical "
                     "pattern, feedbacks under the long-term forced pattern, "
                     "and the difference (the pattern effect) - scored from "
                     "published SST-pattern experiments, then apply the "
                     "difference as a correction to instrumentally inferred "
                     "ECS with full uncertainty. Proposed mechanism: a "
                     "pattern-correction table that takes any "
                     "instrumental-record ECS estimate as input and outputs "
                     "the pattern-corrected value with its uncertainty - "
                     "making the '2.5 vs 3.0' debate a calculation rather "
                     "than a standoff. What would confirm it: the corrected "
                     "instrumental ECS converges with paleoclimate and "
                     "process estimates, and the correction verifies in "
                     "models where the true ECS is known. What would kill "
                     "it: pattern experiments whose feedback shifts vanish "
                     "with model or pattern-dataset choice, or corrected "
                     "estimates that overshoot all other evidence lines. "
                     "What it does NOT claim: that the pattern effect "
                     "fully resolves the ECS debate - it quantifies one "
                     "candidate resolution with stated uncertainty, and "
                     "reports honestly if the residual discrepancy "
                     "remains."),
        "key_points": [
            "Instrumental ECS estimates (~2-2.5 C) run lower than other lines (~3 C).",
            "Feedback strength depends on the SST warming pattern.",
            "Historical pattern (western Pacific emphasis) yields more-negative feedbacks.",
            "Long-term forced pattern may 'unmask' higher sensitivity.",
            "Magnitude debated: tenths of a degree to over a degree ECS-equivalent.",
        ],
        "requirements": [
            "Feedback scores under observed vs long-term SST patterns.",
            "Separation of pattern physics from internal variability.",
            "Verification in models with known true ECS.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (pattern effects on climate sensitivity)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "pattern-corrected instrumental ECS", "unit": "C",
            "calc": "gain", "planck": 1.2, "f_base": 0.52,
            "assumptions": [("pattern-effect feedback shift", 0.09, [0.0, 0.09, 0.14])],
            "formula": "ECS_corr = planck / (1 - (0.52 + shift)); shift=0 -> 2.5C uncorrected",
            "checks": [((0.0,), 2.5, 0.001), ((0.09,), 3.0769, 0.002), ((0.14,), 3.5294, 0.002)],
            "steps": [
                "Step 1: score feedbacks under the observed historical SST pattern.",
                "Step 2: score feedbacks under the long-term forced pattern.",
                "Step 3: difference the two as the pattern effect.",
                "Step 4: apply the correction to instrumental ECS estimates.",
                "Step 5: verify the correction in models with known true ECS.",
            ],
            "confirm": [
                "Corrected instrumental ECS converges with other evidence lines.",
                "The correction verifies in models with known true ECS.",
            ],
            "refute": [
                "Pattern-experiment shifts vanish with model or dataset choice.",
                "Corrected estimates overshoot all other evidence lines.",
            ],
            "note": "Pattern-correction explorer: demo computes ECS for feedback f=0.52+shift via planck/(1-f).",
        },
    },
    {
        "key": "tcr-vs-ecs",
        "name": "Transient vs Equilibrium: TCR and the Warming Commitment",
        "group": "Advanced",
        "ladder_rank": 25, "ladder_tier": "advanced",
        "problem": ("Equilibrium sensitivity (ECS) describes the eventual "
                    "warming, but policy lives in the transient: the "
                    "Transient Climate Response (TCR) - warming at CO2 "
                    "doubling under a steady 1-percent-per-year increase - "
                    "is better constrained (AR6 likely 1.4-2.2 C, best 1.8 "
                    "C). The open questions: the exact TCR-to-ECS ratio, "
                    "how much warming is already 'committed' by past "
                    "emissions, and whether stopping emissions halts "
                    "warming or lets it creep further."),
        "background": ("TCR is the more policy-relevant number because "
                       "emissions rise gradually, not instantly - and it is "
                       "better constrained because ocean heat uptake, which "
                       "separates TCR from ECS, is observable. AR6's "
                       "assessment: ECS best 3.0 C, TCR best 1.8 C, ratio "
                       "about 0.6. The 'committed warming' question - how "
                       "much more warming is in the pipeline if emissions "
                       "stopped today - was long answered 'about 0.5 C "
                       "more'; newer work on the zero-emissions commitment "
                       "suggests surface temperatures roughly stabilize "
                       "within decades of net-zero CO2, with uncertainty "
                       "spanning slight cooling to continued warming. The "
                       "ratio's exact value and its dependence on ocean "
                       "mixing physics remain active research."),
        "why_it_matters": ("Net-zero pledges promise to stop warming; the "
                           "TCR/ECS relationship determines whether that "
                           "promise holds immediately or after additional "
                           "committed warming. Every 'we have stopped the "
                           "warming' claim rests on the zero-emissions "
                           "commitment number."),
        "sig_pointer": ("The Signature edition proposes a commitment ledger "
                        "separating pipeline warming from zero-emission "
                        "stabilization. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) TCR is the "
                     "better-constrained, policy-relevant quantity and the "
                     "ledger's anchor; (2) the TCR/ECS ratio is set by ocean "
                     "heat uptake efficiency, which is observable; (3) the "
                     "zero-emissions commitment can be bounded by the "
                     "balance of declining forcing and declining ocean "
                     "uptake. Reasoning path: build a commitment ledger "
                     "with three rows - warming to date, pipeline warming "
                     "from ocean thermal inertia, and the zero-emissions "
                     "commitment (the net of falling forcing vs falling "
                     "uptake) - score each from observations and model "
                     "experiments, and report the net-zero temperature "
                     "trajectory as a band, not a line. Proposed mechanism: "
                     "a public commitment ledger that answers 'if we stop "
                     "emitting today, what happens to temperature?' with "
                     "scored components and honest uncertainty - the "
                     "document every net-zero pledge implicitly cites. What "
                     "would confirm it: the ledger's TCR verifies against "
                     "the observed warming rate, and its zero-emission band "
                     "matches dedicated model experiments. What would kill "
                     "it: a TCR that drifts with the analysis period, or "
                     "zero-emission experiments that fall outside the "
                     "ledger band. What it does NOT claim: that net-zero "
                     "instantly stops all warming effects - sea level and "
                     "ice sheets respond on longer clocks, and the ledger "
                     "says so explicitly."),
        "key_points": [
            "TCR: warming at CO2 doubling under 1%/yr increase; AR6 likely 1.4-2.2 C, best 1.8 C.",
            "TCR is better constrained than ECS; ratio TCR/ECS ~0.6.",
            "Zero-emissions commitment: temperatures roughly stabilize within decades of net-zero CO2.",
            "Older '0.5 C more in the pipeline' framing is superseded by the net-zero framing.",
            "Sea level and ice sheets keep responding long after temperatures stabilize.",
        ],
        "requirements": [
            "TCR anchored to the observed warming rate.",
            "TCR/ECS ratio tied to measured ocean uptake efficiency.",
            "Zero-emissions band verified against dedicated model experiments.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (TCR and commitments); Chapter 4"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "warming commitment after net-zero", "unit": "C",
            "calc": "expr", "expr": "a0 + a1", "base": 0.0,
            "assumptions": [("warming to date (C)", 1.2, [1.0, 1.2, 1.4]),
                            ("zero-emission commitment (C)", 0.0, [-0.2, 0.0, 0.3])],
            "formula": "stabilized_C = warming_to_date + zero_emission_commitment",
            "checks": [((1.2, 0.0), 1.2, 0.01), ((1.4, 0.3), 1.7, 0.01), ((1.0, -0.2), 0.8, 0.01)],
            "steps": [
                "Step 1: anchor TCR to the observed warming rate.",
                "Step 2: tie the TCR/ECS ratio to measured ocean uptake efficiency.",
                "Step 3: score the zero-emissions commitment from model experiments.",
                "Step 4: build the commitment ledger (to-date + pipeline + commitment).",
                "Step 5: report the net-zero temperature trajectory as a band.",
            ],
            "confirm": [
                "The ledger's TCR verifies against the observed warming rate.",
                "The zero-emission band matches dedicated model experiments.",
            ],
            "refute": [
                "TCR drifts with the analysis period.",
                "Zero-emission experiments fall outside the ledger band.",
            ],
            "note": "Commitment-ledger explorer for TCR and zero-emissions warming.",
        },
    },
    {
        "key": "energy-imbalance",
        "name": "Earth's Energy Imbalance: Measuring the Heat Gain",
        "group": "Advanced",
        "ladder_rank": 26, "ladder_tier": "advanced",
        "problem": ("Earth's energy imbalance (EEI) - the net rate at which "
                    "the planet accumulates heat, about 0.9 W/m2 in recent "
                    "years - is the single most fundamental number in "
                    "climate science: it is the direct measure of the "
                    "greenhouse forcing at work. Yet measuring a 0.9 W/m2 "
                    "residual against ~340 W/m2 of incoming sunlight pushes "
                    "satellite radiometry to its limits, and the imbalance's "
                    "trend and variability are still being pinned down."),
        "background": ("Two independent methods measure EEI: satellites "
                       "(CERES) measuring top-of-atmosphere radiation, and "
                       "the ocean heat content inventory (Argo floats plus "
                       "deep measurements) measuring where the heat goes. "
                       "They agree on roughly 0.9 W/m2 for recent years - a "
                       "triumph of consilience - and both show the imbalance "
                       "roughly doubling since 2005, a striking acceleration. "
                       "The open questions: how much of the trend is "
                       "forcing (greenhouse gases, aerosols) versus "
                       "feedback (cloud and albedo changes), whether the "
                       "satellite calibration is stable enough to trust the "
                       "trend's exact slope, and what the imbalance implies "
                       "for the warming rate of the coming decade."),
        "why_it_matters": ("EEI is the speedometer of global warming: it "
                           "says how fast heat is accumulating right now, "
                           "independent of surface-temperature wiggles. A "
                           "doubling imbalance means the warming rate ahead "
                           "will exceed the warming rate behind - the most "
                           "direct early warning the observing system can "
                           "give."),
        "sig_pointer": ("The Signature edition proposes a two-witness EEI "
                        "ledger: satellites and ocean inventory scored "
                        "against each other. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) CERES radiometry and "
                     "the ocean heat inventory are independent witnesses to "
                     "the same imbalance; (2) their agreement is the "
                     "primary validation of both; (3) the trend's "
                     "forcing-vs-feedback partition can be scored from "
                     "aerosol/cloud records. Reasoning path: maintain a "
                     "two-witness ledger - satellite EEI and inventory EEI "
                     "published side by side each year - decompose the "
                     "trend into forcing and feedback rows from independent "
                     "records, and convert the imbalance into an implied "
                     "decadal warming rate as a checkable prediction. "
                     "Proposed mechanism: an annual EEI report card with "
                     "the two witnesses, the trend decomposition, and the "
                     "implied warming rate - the single page that answers "
                     "'how fast is heat accumulating'. What would confirm "
                     "it: the witnesses continue to agree within "
                     "uncertainty, and the implied warming rate verifies "
                     "against observed decadal warming. What would kill it: "
                     "witness divergence beyond stated uncertainties, or an "
                     "implied warming rate that persistently misses "
                     "observations. What it does NOT claim: that EEI "
                     "replaces surface temperature records - it complements "
                     "them, and the ledger says explicitly what each "
                     "witness can and cannot see."),
        "key_points": [
            "EEI ~0.9 W/m2 recently: the direct measure of heat accumulation.",
            "Two witnesses agree: CERES satellites and the ocean heat inventory.",
            "The imbalance roughly doubled since 2005.",
            "Measuring 0.9 W/m2 against ~340 W/m2 incoming pushes radiometry limits.",
            "Forcing-vs-feedback partition of the trend is still being worked out.",
        ],
        "requirements": [
            "Annual two-witness ledger: satellite EEI vs inventory EEI.",
            "Trend decomposition into forcing and feedback rows.",
            "Implied decadal warming rate published as a checkable prediction.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (Earth's energy budget); CERES EBAF editions"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "heat accumulated over a decade at current imbalance", "unit": "zettajoules",
            "calc": "heat", "imbalance": 0.9, "years": 10,
            "assumptions": [("energy imbalance (W/m2)", 0.9, [0.5, 0.9, 1.2]),
                            ("years", 10, [10, 20, 30])],
            "formula": "ZJ = imbalance_Wm2 * years * 16.0965",
            "checks": [((0.9, 10), 144.868, 0.6), ((1.2, 30), 579.474, 2.0)],
            "steps": [
                "Step 1: publish satellite EEI and inventory EEI side by side yearly.",
                "Step 2: check the two witnesses agree within uncertainty.",
                "Step 3: decompose the trend into forcing and feedback rows.",
                "Step 4: convert the imbalance to an implied decadal warming rate.",
                "Step 5: verify the implied rate against observed warming.",
            ],
            "confirm": [
                "Witnesses agree within uncertainty year after year.",
                "The implied warming rate verifies against observed decadal warming.",
            ],
            "refute": [
                "Witness divergence beyond stated uncertainties.",
                "Implied warming rate persistently misses observations.",
            ],
            "note": "Two-witness ledger explorer for Earth's energy imbalance.",
        },
    },
    {
        "key": "tipping-points",
        "name": "Tipping Points: Real Thresholds or Smooth Change",
        "group": "Advanced",
        "ladder_rank": 27, "ladder_tier": "advanced",
        "problem": ("'Tipping point' is the most evocative - and most "
                    "abused - term in climate discourse. Which Earth-system "
                    "components truly have thresholds with hysteresis and "
                    "irreversibility (ice sheets, AMOC, Amazon, permafrost), "
                    "where those thresholds lie in temperature, and which "
                    "'tipping points' are really smooth-but-steep responses, "
                    "remains a contested research frontier."),
        "background": ("The tipping-elements framework (Lenton et al. 2008) "
                       "listed candidates: Greenland and West Antarctic ice "
                       "sheets, AMOC, Amazon dieback, permafrost carbon, "
                       "coral reefs, boreal forest, monsoons. A 2022-2023 "
                       "assessment argued several thresholds may sit near "
                       "1.5 C - inside the Paris range - while critics "
                       "counter that the evidence for true bifurcations "
                       "(vs steep but reversible responses) is thin for "
                       "most elements, and that threshold temperatures carry "
                       "enormous uncertainty bands. The debate matters "
                       "because 'tipping point' implies a qualitatively "
                       "different risk calculus: prevention becomes "
                       "everything, since crossing cannot be undone."),
        "why_it_matters": ("If multiple tipping points cluster near 1.5 C, "
                           "every tenth of a degree of avoided warming buys "
                           "disproportionate risk reduction - the strongest "
                           "possible argument for aggressive mitigation. If "
                           "the thresholds are higher or the responses "
                           "smoother, the risk calculus - and the rhetoric - "
                           "changes substantially."),
        "sig_pointer": ("The Signature edition proposes a tipping-evidence "
                        "ledger grading each candidate on bifurcation "
                        "evidence. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) 'tipping point' must "
                     "be earned - a candidate needs evidence of true "
                     "bifurcation/hysteresis, not just steep response; (2) "
                     "each candidate can be graded on threshold location, "
                     "irreversibility timescale, and cascade potential "
                     "separately; (3) the rhetoric must follow the grades, "
                     "not precede them. Reasoning path: build a "
                     "candidate-by-candidate ledger - ice sheets, AMOC, "
                     "Amazon, permafrost, corals, boreal, monsoons - with "
                     "columns for bifurcation evidence, threshold band, "
                     "irreversibility timescale, and cascade links, each "
                     "cell graded A-F on evidence quality. Proposed "
                     "mechanism: a public tipping-evidence ledger that "
                     "replaces 'scientists warn of tipping points' with a "
                     "scored table anyone can inspect - showing which "
                     "elements earned the term and which are still "
                     "candidates. What would confirm it: ledger grades "
                     "predict which elements show early-warning signals in "
                     "observations. What would kill it: high-graded "
                     "elements that show no threshold behavior under "
                     "prolonged forcing, or low-graded elements that tip "
                     "first. What it does NOT claim: a definitive tipping "
                     "point list - the ledger is a living evidence table, "
                     "and its most honest cells may read 'insufficient "
                     "evidence'."),
        "key_points": [
            "Tipping elements framework (Lenton et al. 2008): ice sheets, AMOC, Amazon, permafrost, corals, more.",
            "True tipping requires bifurcation/hysteresis, not just steep response.",
            "Some assessments place thresholds near 1.5 C; critics cite thin bifurcation evidence.",
            "Threshold temperature bands carry enormous uncertainty.",
            "Cascade potential (one tipping triggering another) is largely unquantified.",
        ],
        "requirements": [
            "Per-candidate grades: bifurcation evidence, threshold band, irreversibility, cascades.",
            "Rhetoric that follows the grades.",
            "Early-warning-signal verification for high-graded elements.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 8; WGII (tipping point assessments); Lenton et al. 2008"],
        "citations": CIT_BASE + [
            "Lenton TM et al. Tipping elements in the Earth's climate "
            "system. Proceedings of the National Academy of Sciences; 2008.",
        ],
        "demo": {
            "quantity": "tipping-evidence ledger score (example element)", "unit": "points/100",
            "calc": "min", "base": 0.0,
            "assumptions": [("bifurcation evidence", 55, [20, 55, 85]),
                            ("threshold location confidence", 40, [15, 40, 70]),
                            ("irreversibility evidence", 60, [25, 60, 85]),
                            ("cascade-link evidence", 30, [10, 30, 60])],
            "formula": "element_score = min of the four grades (weakest link earns the term)",
            "checks": [((55, 40, 60, 30), 30, 0.5), ((85, 70, 85, 60), 60, 0.5)],
            "steps": [
                "Step 1: list tipping candidates as ledger rows.",
                "Step 2: grade bifurcation evidence per candidate.",
                "Step 3: grade threshold band, irreversibility, and cascade links.",
                "Step 4: let the weakest link set each element's score.",
                "Step 5: verify high-graded elements against early-warning signals.",
            ],
            "confirm": [
                "Ledger grades predict which elements show early-warning signals.",
                "Grades are stable across assessment rounds.",
            ],
            "refute": [
                "High-graded elements show no threshold behavior under forcing.",
                "Low-graded elements tip first, breaking the grading.",
            ],
            "note": "Tipping-evidence ledger explorer grading each candidate element.",
        },
    },
    {
        "key": "sahel-greening",
        "name": "The Sahel and the Green Sahara: Tipping a Desert",
        "group": "Advanced",
        "ladder_rank": 28, "ladder_tier": "advanced",
        "problem": ("Six thousand years ago the Sahara was green - lakes, "
                    "rivers, and savanna where desert now lies - and it "
                    "desiccated in what may have been an abrupt vegetation-"
                    "climate tipping. The Sahel drought of the 1970s-80s "
                    "showed the region can swing dramatically on decadal "
                    "scales. Whether the Sahel faces greening or "
                    "desertification under future warming, and whether the "
                    "system truly tips, is unresolved."),
        "background": ("The mid-Holocene Green Sahara (the African Humid "
                       "Period) is documented by lake sediments, pollen, "
                       "and rock art; its end ~5,500 years ago may have been "
                       "gradual or abrupt - the paleoclimate jury is still "
                       "out, with vegetation-albedo feedback as the "
                       "candidate tipping mechanism. The modern Sahel's "
                       "1970s-80s drought, among the largest climate "
                       "signals of the 20th century, is now attributed to "
                       "a combination of Atlantic SST patterns, aerosol "
                       "dimming, and land-surface feedbacks; rainfall has "
                       "partially recovered since the 1990s. Models project "
                       "a wetter Sahel on average with warming, but with "
                       "wide spread and disagreement on the seasonal "
                       "structure - and the vegetation feedback that could "
                       "amplify greening (or desertification) is crudely "
                       "represented."),
        "why_it_matters": ("The Sahel is home to hundreds of millions of "
                           "people in some of the world's most food-insecure "
                           "nations. The difference between a greening Sahel "
                           "and a desertifying one is the difference between "
                           "agricultural expansion and famine-driven "
                           "migration - and the Green Sahara precedent shows "
                           "the system can move much farther than linear "
                           "projections suggest."),
        "sig_pointer": ("The Signature edition proposes a vegetation-rainfall "
                        "feedback ledger for the Sahel, calibrated on the "
                        "Green Sahara. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the Green Sahara "
                     "desiccation is the calibration event for "
                     "vegetation-rainfall feedback strength; (2) the "
                     "1970s-80s drought is the calibration event for "
                     "decadal SST/aerosol forcing of Sahel rain; (3) future "
                     "projections must pass both calibrations before their "
                     "mean is trusted. Reasoning path: score the "
                     "vegetation-albedo feedback from the paleoclimate "
                     "transition (how much did vegetation amplify the "
                     "orbital drying?), score the SST/aerosol forcing from "
                     "the modern drought and recovery, then filter model "
                     "projections through both calibrations - keeping only "
                     "models that reproduce both events' magnitude. "
                     "Proposed mechanism: a dual-calibration filter for "
                     "Sahel projections, publishing both the filtered "
                     "projection and the unfiltered spread, so users see "
                     "what the calibration costs in uncertainty. What "
                     "would confirm it: filtered models hindcast the "
                     "1990s-2010s recovery better than unfiltered ones. "
                     "What would kill it: the Green Sahara transition "
                     "proving gradual (removing the tipping calibration), "
                     "or no model passing both calibrations (leaving the "
                     "filter empty). What it does NOT claim: a forecast of "
                     "Sahel greening or desertification - the filter "
                     "narrows the projection honestly, and a wide "
                     "remaining spread is reported as wide."),
        "key_points": [
            "The Sahara was green ~6,000 years ago (African Humid Period).",
            "Its desiccation may have been an abrupt vegetation-climate tipping.",
            "The 1970s-80s Sahel drought was among the 20th century's largest climate signals.",
            "Rainfall partially recovered since the 1990s.",
            "Models project wetter on average but disagree on seasonal structure.",
        ],
        "requirements": [
            "Paleoclimate calibration: vegetation feedback from the Green Sahara transition.",
            "Modern calibration: SST/aerosol forcing from the drought and recovery.",
            "Model filter keeping only models passing both calibrations.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 8 (Sahel and monsoon assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "Sahel rainfall change (filtered projection)", "unit": "%",
            "calc": "expr", "expr": "a0 * a2 * (0.5 + a1)", "base": 0.0,
            "assumptions": [("unfiltered model-mean change (%)", 8, [-5, 8, 20]),
                            ("models passing dual calibration (fraction)", 0.35, [0.1, 0.35, 0.7]),
                            ("vegetation-feedback amplification", 1.4, [1.0, 1.4, 2.0])],
            "formula": "filtered = unfiltered * amplification * (0.5 + pass_fraction)",
            "checks": [((8, 0.35, 1.4), 9.52, 0.02), ((-5, 0.7, 2.0), -12.0, 0.02)],
            "steps": [
                "Step 1: calibrate vegetation feedback on the Green Sahara transition.",
                "Step 2: calibrate SST/aerosol forcing on the 1970s-80s drought and recovery.",
                "Step 3: filter models through both calibrations.",
                "Step 4: publish filtered projection alongside unfiltered spread.",
                "Step 5: verify filtered models hindcast the 1990s-2010s recovery.",
            ],
            "confirm": [
                "Filtered models hindcast the recovery better than unfiltered ones.",
                "The vegetation feedback score is stable across paleoclimate datasets.",
            ],
            "refute": [
                "The Green Sahara transition proves gradual, removing the tipping calibration.",
                "No model passes both calibrations, emptying the filter.",
            ],
            "note": "Dual-calibration filter explorer for Sahel rainfall projections.",
        },
    },
    {
        "key": "petm-analog",
        "name": "The PETM: Ancient Warming as a Climate Analog",
        "group": "Advanced",
        "ladder_rank": 29, "ladder_tier": "advanced",
        "problem": ("Fifty-six million years ago, the Paleocene-Eocene "
                    "Thermal Maximum (PETM) warmed the planet 5-8 C in what "
                    "geology calls a geological instant - the best ancient "
                    "analog for rapid carbon-driven warming. But how much "
                    "carbon was released, how fast, and what exactly "
                    "triggered it remain debated - and the answers bound "
                    "how literally the PETM can guide expectations for "
                    "today."),
        "background": ("The PETM is recorded in ocean sediments worldwide: "
                       "a sharp carbon-isotope excursion marking a massive "
                       "injection of isotopically light carbon, deep-ocean "
                       "warming of 5-8 C, ocean acidification dissolving "
                       "seafloor carbonates, and major ecosystem turnover "
                       "(including the rise of modern mammal orders). "
                       "Candidate carbon sources - methane hydrates, "
                       "volcanic intrusions baking organic-rich sediments "
                       "(the North Atlantic Igneous Province), permafrost, "
                       "or wildfires - each imply different release rates. "
                       "Current estimates put the onset release at perhaps "
                       "0.3-1.7 petagrams of carbon per year sustained over "
                       "thousands of years - fast geologically, but roughly "
                       "an order of magnitude slower than today's ~10 "
                       "petagrams per year. That rate gap is the central "
                       "caveat on the analog."),
        "why_it_matters": ("The PETM is the only well-documented case of "
                           "thousands-of-gigatons carbon release with "
                           "global ecosystem consequences - it sets the "
                           "empirical upper bound on what rapid carbon "
                           "release does to oceans (acidification, anoxia) "
                           "and life (turnover, dwarfing, migration). Its "
                           "recovery timescale - over 100,000 years - is "
                           "the sobering number for long-term thinking."),
        "sig_pointer": ("The Signature edition proposes a rate-ledger "
                        "comparing PETM carbon release rates with today's, "
                        "event by event. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the PETM's value as an "
                     "analog scales with the comparability of release "
                     "rates, so rates - not just totals - are the ledger's "
                     "currency; (2) the carbon-isotope excursion constrains "
                     "total carbon but source attribution remains model-"
                     "dependent; (3) the recovery timescale (~100 kyr) is "
                     "the most robust lesson. Reasoning path: build a "
                     "rate ledger - for each candidate source mechanism, "
                     "list its implied release rate, duration, and total "
                     "carbon - compare each against today's ~10 PgC/yr, "
                     "and grade the analog's applicability per question "
                     "(ocean acidification: strong analog; warming rate: "
                     "weak analog due to the rate gap). Proposed mechanism: "
                     "a question-by-question analog scorecard - rather than "
                     "'the PETM is (or isn't) an analog', each policy-"
                     "relevant question gets its own applicability grade. "
                     "What would confirm it: new high-resolution sediment "
                     "records converging the rate estimates, and the "
                     "scorecard's grades predicting which PETM-based "
                     "projections verify. What would kill it: rate "
                     "estimates that refuse to converge across sediment "
                     "records, or source attribution that flips the rate "
                     "ranking. What it does NOT claim: that the PETM "
                     "predicts today's warming trajectory - the rate gap "
                     "means today's experiment is faster than the analog, "
                     "and the scorecard says so explicitly."),
        "key_points": [
            "PETM ~56 Ma: 5-8 C warming from massive carbon injection.",
            "Recorded globally: carbon-isotope excursion, ocean acidification, ecosystem turnover.",
            "Candidate sources: methane hydrates, volcanic-baked sediments, permafrost, wildfires.",
            "Onset release ~0.3-1.7 PgC/yr over millennia vs ~10 PgC/yr today.",
            "Recovery took over 100,000 years.",
        ],
        "requirements": [
            "Rate ledger per candidate source: rate, duration, total carbon.",
            "Question-by-question analog applicability grades.",
            "Convergence of rate estimates across high-resolution records.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 2 (paleoclimate); Chapter 5 (PETM carbon release)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "PETM-to-modern carbon release rate ratio", "unit": "multiple",
            "calc": "expr", "expr": "a0 / a1", "base": 10.0,
            "assumptions": [("modern release rate (PgC/yr)", 10.0, [9.0, 10.0, 11.0]),
                            ("PETM onset rate (PgC/yr)", 1.0, [0.3, 1.0, 1.7])],
            "formula": "ratio = modern_rate / petm_rate (the analog rate gap)",
            "checks": [((10.0, 1.0), 10.0, 0.05), ((10.0, 0.3), 33.33, 0.1)],
            "steps": [
                "Step 1: ledger each candidate source's rate, duration, and total.",
                "Step 2: compare each rate against today's ~10 PgC/yr.",
                "Step 3: grade analog applicability question by question.",
                "Step 4: track the recovery-timescale lesson separately.",
                "Step 5: update as high-resolution records converge rates.",
            ],
            "confirm": [
                "Rate estimates converge across sediment records.",
                "Scorecard grades predict which PETM-based projections verify.",
            ],
            "refute": [
                "Rate estimates refuse to converge across records.",
                "Source attribution flips the rate ranking.",
            ],
            "note": "Rate-ledger explorer comparing PETM and modern carbon release.",
        },
    },
    {
        "key": "eocene-hothouse",
        "name": "Eocene Hothouse: Why Past Warmth Challenges Models",
        "group": "Advanced",
        "ladder_rank": 30, "ladder_tier": "advanced",
        "problem": ("The early Eocene (~50 million years ago) was a "
                    "hothouse: ice-free poles, palm trees in the Arctic, "
                    "deep oceans 10+ C warmer than today - under CO2 "
                    "levels (~1,000-2,000 ppm) that models struggle to "
                    "turn into that much warmth without extra help. This "
                    "'equable climate problem' - how the poles got so warm "
                    "while the tropics stayed bearable - has challenged "
                    "models for decades and may hide missing feedbacks."),
        "background": ("Proxy data (leaf fossils, isotopes, TEX86) show "
                       "Arctic temperatures above freezing year-round and a "
                       "remarkably flat equator-to-pole temperature "
                       "gradient. Early models forced with Eocene CO2 "
                       "produced too-cold poles - the models' polar "
                       "amplification was too weak. Recent progress: "
                       "higher-resolution models, better cloud physics, and "
                       "revised (often warmer) CO2 proxies have narrowed "
                       "the gap, with some CMIP6-class models now matching "
                       "Eocene warmth - but often by invoking strongly "
                       "positive cloud feedbacks that sit at the high end "
                       "of modern estimates. The suspicion lingers that "
                       "models get the Eocene right for the wrong reasons, "
                       "or that genuinely missing feedbacks (vegetation, "
                       "aerosol, or cloud regimes with no modern analog) "
                       "did the work."),
        "why_it_matters": ("If models need high-end cloud feedbacks to "
                           "explain the Eocene, that is evidence - "
                           "independent of modern observations - about "
                           "where in the feedback range reality sits. The "
                           "Eocene is effectively a second, natural "
                           "climate-sensitivity experiment, and its verdict "
                           "bears directly on the high tail of ECS."),
        "sig_pointer": ("The Signature edition proposes a gradient-ledger: "
                        "models must match the flat Eocene temperature "
                        "gradient, not just global warmth. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the equator-to-pole "
                     "temperature gradient is a stricter test than global-"
                     "mean warmth - a model can hit the mean and miss the "
                     "physics; (2) proxy CO2 and temperature estimates "
                     "carry stated uncertainties that the ledger must "
                     "respect; (3) matching the Eocene via high-end cloud "
                     "feedbacks is a hypothesis to be scored, not a "
                     "victory to be declared. Reasoning path: build a "
                     "gradient ledger - for each model, its simulated "
                     "tropical, mid-latitude, and polar Eocene temperatures "
                     "against proxy bands - and score models on gradient "
                     "fidelity, publishing which feedbacks each model used "
                     "to get there. Proposed mechanism: a public Eocene "
                     "gradient scorecard that names, per model, the "
                     "feedback price paid for Eocene warmth - so 'model X "
                     "matches the Eocene' becomes 'model X matches the "
                     "Eocene using cloud feedback of +Y'. What would "
                     "confirm it: models whose feedback prices match "
                     "independent modern feedback estimates, and gradient "
                     "scores that predict models' modern ECS. What would "
                     "kill it: no model matching the gradient without "
                     "feedback prices outside all modern bounds (suggesting "
                     "missing Eocene-specific physics), or proxy bands too "
                     "wide to score anything. What it does NOT claim: that "
                     "the Eocene settles modern sensitivity - it is scored "
                     "as one more witness, and a witness that may be "
                     "testifying about feedbacks with no modern analog."),
        "key_points": [
            "Early Eocene: ice-free poles, Arctic palms, flat temperature gradient.",
            "CO2 ~1,000-2,000 ppm; models long produced too-cold poles.",
            "Recent models match Eocene warmth, often via high-end cloud feedbacks.",
            "The 'equable climate problem': warm poles with bearable tropics.",
            "Suspicion of missing feedbacks with no modern analog.",
        ],
        "requirements": [
            "Gradient ledger: tropical, mid-latitude, polar temps vs proxy bands.",
            "Per-model feedback-price disclosure for Eocene warmth.",
            "Test whether gradient scores predict models' modern ECS.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 2 (Eocene assessment); Chapter 7"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "Eocene gradient fidelity score", "unit": "points/100",
            "calc": "min", "base": 0.0,
            "assumptions": [("tropical match score", 80, [50, 80, 95]),
                            ("mid-latitude match score", 65, [40, 65, 90]),
                            ("polar match score", 55, [25, 55, 85])],
            "formula": "gradient_score = min of the three latitude-band scores",
            "checks": [((80, 65, 55), 55, 0.5), ((95, 90, 85), 85, 0.5)],
            "steps": [
                "Step 1: ledger proxy temperature bands by latitude.",
                "Step 2: score each model's tropical, mid-latitude, and polar Eocene.",
                "Step 3: disclose the feedback price each model paid for warmth.",
                "Step 4: set the gradient score by the weakest latitude band.",
                "Step 5: test whether gradient scores predict modern ECS.",
            ],
            "confirm": [
                "Feedback prices match independent modern feedback estimates.",
                "Gradient scores predict models' modern ECS.",
            ],
            "refute": [
                "No model matches the gradient within modern feedback bounds.",
                "Proxy bands too wide to score any model.",
            ],
            "note": "Gradient-ledger explorer for the Eocene hothouse test.",
        },
    },
    {
        "key": "ice-core-lead-lag",
        "name": "Ice Cores: Does CO2 Lead or Lag Temperature",
        "group": "Advanced",
        "ladder_rank": 31, "ladder_tier": "advanced",
        "problem": ("Antarctic ice cores show CO2 and temperature marching "
                    "together through ice ages - but at glacial "
                    "terminations, temperature appears to lead CO2 by "
                    "centuries. Skeptics cite the lag to argue CO2 does not "
                    "drive warming; scientists answer that orbital cycles "
                    "trigger the warming and CO2 amplifies it. The exact "
                    "lead-lag structure, and what it implies about "
                    "feedbacks, remains a technically demanding, "
                    "frequently misrepresented question."),
        "background": ("The Vostok and EPICA Dome C cores span 400,000-"
                       "800,000 years, showing CO2 between ~180 ppm "
                       "(glacials) and ~280 ppm (interglacials) in lockstep "
                       "with Antarctic temperature. High-resolution studies "
                       "of terminations find Antarctic warming leading CO2 "
                       "rise by roughly 200-1,000 years - expected, since "
                       "Milankovitch orbital forcing initiates deglaciation "
                       "and the warming ocean then outgasses CO2, which "
                       "amplifies the warming globally. The Southern Ocean's "
                       "role (wind-driven upwelling releasing deep carbon) "
                       "is the mechanistic core. The misrepresentation "
                       "persists because 'CO2 lags temperature' sounds like "
                       "'CO2 doesn't cause warming' - when in fact the "
                       "lag is predicted by the standard theory and the "
                       "amplification is the point."),
        "why_it_matters": ("The lead-lag question is the most cited piece "
                           "of 'evidence' against human-caused warming in "
                           "public debate - and the scientific answer is "
                           "subtle enough to need careful telling. Getting "
                           "the technical story exactly right, with the "
                           "mechanism explicit, is both a scientific and a "
                           "communication obligation."),
        "sig_pointer": ("The Signature edition proposes a mechanism-ledger "
                        "that walks the termination sequence step by step. "
                        + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the termination "
                     "sequence - orbital trigger, Southern Ocean "
                     "outgassing, CO2 amplification, global warming - is "
                     "the correct mechanistic frame; (2) lead-lag timing "
                     "can be measured from high-resolution cores with "
                     "stated dating uncertainty; (3) the skeptical "
                     "'lag disproves causation' argument fails basic "
                     "causal logic (feedback systems routinely show "
                     "leads and lags) and the ledger should demonstrate "
                     "this, not merely assert it. Reasoning path: build a "
                     "termination ledger - for each major termination, "
                     "list orbital forcing onset, Antarctic warming onset, "
                     "CO2 rise onset, and global ice-volume response with "
                     "dating uncertainties - and show the sequence matches "
                     "the trigger-amplifier mechanism while quantifying "
                     "the amplification (roughly half the glacial-"
                     "interglacial warming attributed to CO2 and its "
                     "feedbacks). Proposed mechanism: a public termination "
                     "table plus a simple box-model demonstration in which "
                     "an orbital trigger plus CO2 feedback reproduces the "
                     "observed lead-lag pattern - making the 'lag' a "
                     "prediction of the theory rather than an embarrassment. "
                     "What would confirm it: the box model reproduces "
                     "termination timing across multiple glacial cycles "
                     "with one parameter set. What would kill it: "
                     "terminations where CO2 rises before any warming "
                     "signal (breaking the trigger story), or a "
                     "demonstration that the amplification is negligible. "
                     "What it does NOT claim: that ice-age CO2 proves "
                     "anything directly about today's warming - the "
                     "ledger distinguishes the trigger-amplifier past from "
                     "the direct-forcing present, and says plainly that "
                     "today's CO2 rise leads."),
        "key_points": [
            "Ice cores: CO2 180-280 ppm across glacial cycles, in lockstep with temperature.",
            "At terminations, Antarctic warming leads CO2 by ~200-1,000 years.",
            "Orbital cycles trigger; the warming ocean outgasses CO2, which amplifies.",
            "Southern Ocean upwelling is the mechanistic core of the outgassing.",
            "'Lag disproves causation' misreads feedback-system causality.",
        ],
        "requirements": [
            "Termination ledger: forcing onset, warming onset, CO2 onset, ice response per event.",
            "Box-model demonstration reproducing lead-lag from trigger plus feedback.",
            "Quantified amplification share of glacial-interglacial warming.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 2 (glacial cycles and CO2)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "glacial-interglacial warming amplified by CO2", "unit": "C",
            "calc": "expr", "expr": "a0 * a1", "base": 0.0,
            "assumptions": [("total termination warming (C)", 5.0, [4.0, 5.0, 6.0]),
                            ("CO2 amplification share", 0.5, [0.3, 0.5, 0.7])],
            "formula": "co2_driven = total_warming * amplification_share",
            "checks": [((5.0, 0.5), 2.5, 0.05), ((6.0, 0.7), 4.2, 0.05)],
            "steps": [
                "Step 1: ledger each termination's forcing, warming, CO2, and ice onsets.",
                "Step 2: verify the trigger-amplifier sequence with dating uncertainties.",
                "Step 3: build the box model (orbital trigger + CO2 feedback).",
                "Step 4: reproduce the lead-lag pattern as a model prediction.",
                "Step 5: quantify the CO2 amplification share of total warming.",
            ],
            "confirm": [
                "The box model reproduces termination timing across cycles with one parameter set.",
                "The sequence matches trigger-amplifier ordering in every termination.",
            ],
            "refute": [
                "A termination where CO2 rises before any warming signal.",
                "Demonstration that the amplification share is negligible.",
            ],
            "note": "Termination-ledger explorer for the ice-core lead-lag question.",
        },
    },
    {
        "key": "cosmic-rays-clouds",
        "name": "Cosmic Rays and Clouds: The Svensmark Debate",
        "group": "Advanced",
        "ladder_rank": 32, "ladder_tier": "advanced",
        "problem": ("Henrik Svensmark proposed that galactic cosmic rays "
                    "seed cloud formation - and since the Sun's magnetic "
                    "field modulates cosmic rays, solar activity could "
                    "drive climate via clouds, potentially explaining much "
                    "of 20th-century warming without CO2. The hypothesis "
                    "has been tested by the CERN CLOUD experiment and by "
                    "Forbush-decrease studies; the mainstream assessment "
                    "finds the effect too small to matter, but the "
                    "hypothesis persists in public debate."),
        "background": ("The proposed chain: cosmic rays ionize air, ions "
                       "help nucleate aerosol particles, particles seed "
                       "cloud droplets, clouds cool the planet - so fewer "
                       "cosmic rays (active Sun) mean fewer clouds and "
                       "warming. CERN's CLOUD chamber confirmed ionization "
                       "does enhance nucleation under controlled conditions "
                       "- but follow-up work showed the effect is too weak "
                       "in the real atmosphere, where abundant other "
                       "nucleation pathways dominate, and that observed "
                       "cloud changes do not track cosmic-ray fluxes. "
                       "Forbush decreases (sudden cosmic-ray drops after "
                       "solar storms) show no robust cloud response in "
                       "multi-event studies. The IPCC assesses no "
                       "significant cosmic-ray climate forcing - yet the "
                       "idea's persistence makes the evidence ledger worth "
                       "maintaining publicly."),
        "why_it_matters": ("The cosmic-ray hypothesis is the leading "
                           "'it's the Sun, not CO2' alternative - and "
                           "unlike vague solar claims, it makes specific, "
                           "testable predictions. A public evidence ledger "
                           "that scores each link in its chain is the "
                           "durable answer: it shows exactly where the "
                           "chain breaks, link by link, rather than "
                           "dismissing it."),
        "sig_pointer": ("The Signature edition proposes a chain-ledger "
                        "scoring each link of the cosmic-ray hypothesis "
                        "separately. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the hypothesis is a "
                     "chain of four links - cosmic-ray modulation, "
                     "ionization-nucleation, nucleation-to-cloud, cloud-to-"
                     "climate - and each link can be scored independently; "
                     "(2) a chain is only as strong as its weakest link; "
                     "(3) scoring must use the hypothesis's own predicted "
                     "magnitudes, not strawmen. Reasoning path: build a "
                     "four-link ledger - score cosmic-ray flux trends "
                     "(declining slightly, wrong sign for recent warming), "
                     "the CLOUD nucleation results (real but weak), the "
                     "Forbush-decrease cloud response (no robust signal), "
                     "and the implied climate forcing (far below "
                     "greenhouse forcing) - and let the weakest link set "
                     "the verdict. Proposed mechanism: a public chain "
                     "ledger, updated as new CLOUD or Forbush studies "
                     "arrive, that gives the hypothesis its fairest "
                     "hearing and its exact breaking point. What would "
                     "confirm the ledger's verdict: continued absence of "
                     "cloud response in Forbush events and cosmic-ray "
                     "trends that fail to match warming. What would kill "
                     "the verdict (and revive the hypothesis): a robust, "
                     "replicated cloud response to a Forbush decrease, or "
                     "a nucleation pathway that scales to the real "
                     "atmosphere. What it does NOT claim: that solar "
                     "influence on climate is zero - total solar irradiance "
                     "variations are a real (small) forcing, ledgered "
                     "separately; the verdict concerns the cosmic-ray-"
                     "cloud chain specifically."),
        "key_points": [
            "Hypothesis: cosmic rays seed clouds; solar modulation then drives climate.",
            "CERN CLOUD confirmed ionization aids nucleation - but too weakly for the real atmosphere.",
            "Forbush-decrease studies show no robust cloud response.",
            "Cosmic-ray trends have the wrong sign for recent warming.",
            "IPCC assesses no significant cosmic-ray climate forcing.",
        ],
        "requirements": [
            "Four-link chain ledger scored independently per link.",
            "Weakest-link verdict rule.",
            "Revival criteria stated in advance (Forbush response, scalable nucleation).",
        ],
        "standards": ["IPCC AR6 WGI Chapter 7 (solar and cosmic-ray forcing assessment)"],
        "citations": CIT_BASE,
        "demo": {
            "quantity": "cosmic-ray-chain climate forcing (ledger verdict)", "unit": "W/m2",
            "calc": "expr", "expr": "min(a0, a1, a2) / 100 * a3", "base": 0.0,
            "assumptions": [("cosmic-ray flux trend link", 0.3, [0.0, 0.3, 0.6]),
                            ("nucleation link strength", 0.2, [0.0, 0.2, 0.5]),
                            ("cloud-response link", 0.1, [0.0, 0.1, 0.4]),
                            ("implied forcing scale (W/m2)", 0.05, [0.0, 0.05, 0.3])],
            "formula": "chain_forcing = min(link scores)/100 * scale; compare with CO2 ~2.2 W/m2",
            "checks": [((0.3, 0.2, 0.1, 0.05), 0.00005, 0.00001), ((0.6, 0.5, 0.4, 0.3), 0.0012, 0.0001)],
            "steps": [
                "Step 1: score the cosmic-ray flux trend link.",
                "Step 2: score the ionization-nucleation link from CLOUD results.",
                "Step 3: score the Forbush-decrease cloud-response link.",
                "Step 4: scale the weakest link to an implied climate forcing.",
                "Step 5: compare against greenhouse forcing (~2.2 W/m2).",
            ],
            "confirm": [
                "No robust cloud response in Forbush events; trends keep the wrong sign.",
                "The chain forcing stays far below greenhouse forcing.",
            ],
            "refute": [
                "A robust, replicated cloud response to a Forbush decrease.",
                "A nucleation pathway that scales to the real atmosphere.",
            ],
            "note": "Chain-ledger explorer scoring the cosmic-ray-cloud hypothesis link by link.",
        },
    },
    {
        "key": "millennium-temperature",
        "name": "Reconstructing a Thousand Years of Temperature",
        "group": "Advanced",
        "ladder_rank": 33, "ladder_tier": "advanced",
        "problem": ("How warm is today compared with the last thousand "
                    "years? Proxy reconstructions (tree rings, ice cores, "
                    "corals, sediments) agree recent decades are the warmest "
                    "in at least 2,000 years - but the amplitude of past "
                    "swings (the Medieval Warm Period, the Little Ice Age), "
                    "the spatial pattern, and the exact methods remain "
                    "contested, and the 'hockey stick' debate left lasting "
                    "scars on public trust."),
        "background": ("Mann, Bradley, and Hughes (1998-99) produced the "
                       "first hemispheric millennial reconstruction - the "
                       "'hockey stick' - showing unprecedented recent "
                       "warming. Subsequent reconstructions with more "
                       "proxies and methods (PAGES 2k consortium, 2013-2019) "
                       "confirmed the shape: a long gradual cooling into "
                       "the Little Ice Age, then sharp 20th-century "
                       "warming, with the last decades warmest in 2,000 "
                       "years. Open issues: tree-ring divergence (some "
                       "high-latitude rings stopped tracking temperature "
                       "after ~1960), the true amplitude of the Medieval "
                       "Warm Period (regionally warm, not globally "
                       "synchronous), and method sensitivity - though "
                       "multi-method agreement is now strong. The "
                       "reconstruction wars of the 2000s were as much about "
                       "statistical transparency as about climate."),
        "why_it_matters": ("'Warmest in 2,000 years' is among the most "
                           "quoted lines in climate science - it anchors "
                           "the claim that current warming is unusual. The "
                           "strength of that claim rests entirely on the "
                           "reconstructions' robustness, and every "
                           "methodological weakness is a foothold for "
                           "manufactured doubt."),
        "sig_pointer": ("The Signature edition proposes a proxy-ledger with "
                        "method-transparency scores for each reconstruction. "
                        + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) no single proxy type "
                     "or method should carry the verdict - consilience "
                     "across proxies and methods is the evidence; (2) "
                     "known issues (tree-ring divergence, proxy dropout) "
                     "must be ledgered openly, not minimized; (3) "
                     "statistical transparency is part of the evidence "
                     "grade. Reasoning path: build a proxy ledger - rows "
                     "for proxy types (tree rings, ice cores, corals, "
                     "lake/marine sediments, documentary), columns for "
                     "time coverage, spatial coverage, and known issues - "
                     "plus a method ledger (CPS, CFR, Bayesian hierarchical, "
                     "etc.) scored on transparency and validation skill, "
                     "then report the multi-proxy, multi-method consensus "
                     "with the weaknesses itemized. Proposed mechanism: a "
                     "public reconstruction report card showing the "
                     "consensus shape, the itemized weaknesses, and the "
                     "'what would change the verdict' list - so critics "
                     "can see exactly which weakness they would need to "
                     "overturn. What would confirm it: new proxies and "
                     "methods converging on the same shape, and the "
                     "weakness list shrinking over time. What would kill "
                     "the verdict: a proxy type that systematically "
                     "contradicts the consensus shape, or a validated "
                     "method that produces a materially different "
                     "millennium. What it does NOT claim: that every "
                     "century of the last two millennia is resolved - the "
                     "ledger grades resolution by period, and early "
                     "centuries carry wider bands honestly."),
        "key_points": [
            "PAGES 2k: last decades warmest in at least 2,000 years.",
            "Long gradual cooling into the Little Ice Age, then sharp 20th-century warming.",
            "Tree-ring divergence: some high-latitude rings diverge from temperature after ~1960.",
            "Medieval Warm Period was regionally warm, not globally synchronous.",
            "Multi-proxy, multi-method agreement is now strong.",
        ],
        "requirements": [
            "Proxy-type ledger with coverage and known issues per type.",
            "Method ledger scored on transparency and validation skill.",
            "Itemized weakness list plus 'what would change the verdict'.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 2 (paleoclimate reconstructions); PAGES 2k"],
        "citations": CIT_BASE + [
            "PAGES 2k Consortium. Consistent multidecadal variability in "
            "global temperature reconstructions and simulations over the "
            "Common Era. Nature Geoscience; 2019.",
        ],
        "demo": {
            "quantity": "reconstruction consensus robustness", "unit": "points/100",
            "calc": "min", "base": 0.0,
            "assumptions": [("proxy-type agreement", 80, [50, 80, 95]),
                            ("method agreement", 75, [45, 75, 90]),
                            ("weakness disclosure score", 70, [40, 70, 90])],
            "formula": "robustness = min of the three scores (weakest link)",
            "checks": [((80, 75, 70), 70, 0.5), ((95, 90, 90), 90, 0.5)],
            "steps": [
                "Step 1: ledger proxy types with coverage and known issues.",
                "Step 2: ledger reconstruction methods with transparency scores.",
                "Step 3: report the multi-proxy, multi-method consensus shape.",
                "Step 4: itemize weaknesses and the 'what would change the verdict' list.",
                "Step 5: track convergence as new proxies and methods arrive.",
            ],
            "confirm": [
                "New proxies and methods converge on the consensus shape.",
                "The weakness list shrinks over time.",
            ],
            "refute": [
                "A proxy type systematically contradicts the consensus shape.",
                "A validated method yields a materially different millennium.",
            ],
            "note": "Proxy-ledger explorer for millennial temperature reconstructions.",
        },
    },
    {
        "key": "deep-time-climate",
        "name": "Snowball Earth and the Climate's Deep-Time Limits",
        "group": "Advanced",
        "ladder_rank": 34, "ladder_tier": "advanced",
        "problem": ("Twice or more in Earth's history, the planet froze "
                    "over entirely - Snowball Earth - and escaped via "
                    "volcanic CO2 buildup over millions of years. These "
                    "deep-time extremes bound what the climate system can "
                    "do: what triggers a Snowball, what finally melts it, "
                    "and whether the carbon-cycle thermostat that recovered "
                    "the planet then still governs now, are frontier "
                    "questions at the edge of geology and climate physics."),
        "background": ("The Sturtian (~717-660 Ma) and Marinoan (~650-635 "
                       "Ma) glaciations left glacial deposits at ancient "
                       "equatorial latitudes - the smoking gun for global "
                       "ice cover. The leading theory (Kirschvink 1992; "
                       "Hoffman et al. 1998): ice-albedo runaway froze the "
                       "oceans, shutting down weathering (the carbon-cycle "
                       "thermostat), so volcanic CO2 accumulated unchecked "
                       "for millions of years until the greenhouse effect "
                       "overwhelmed the ice - possibly at CO2 levels "
                       "hundreds of times preindustrial. Cap carbonates "
                       "capping the glacial deposits record the hot, "
                       "CO2-rich aftermath. Open questions: the exact "
                       "trigger (continental configuration? weathering "
                       "drawdown?), whether 'Slushball' (open equatorial "
                       "water) fits better, and how the deep-time "
                       "thermostat's timescales map onto today's "
                       "century-scale problem."),
        "why_it_matters": ("Snowball Earth is the climate system's "
                           "existence proof of true global tipping - and of "
                           "recovery via the carbon-cycle thermostat on "
                           "million-year timescales. It sets the outer "
                           "bounds of climate risk: the system can go much "
                           "farther than human experience suggests, in both "
                           "directions, and the thermostat that saves the "
                           "planet works on times no civilization can "
                           "wait out."),
        "sig_pointer": ("The Signature edition proposes a thermostat-ledger "
                        "tracing the carbon-cycle recovery clock across "
                        "deep time. " + SIG_LABEL),
        "sig_full": (SIG_LABEL + " Assumptions: (1) the Snowball episodes "
                     "are the outer-boundary experiment for climate "
                     "tipping and recovery; (2) the weathering thermostat "
                     "(silicate weathering as a function of temperature "
                     "and CO2) is the recovery mechanism, with a "
                     "million-year clock; (3) deep-time lessons bound, but "
                     "do not predict, century-scale behavior. Reasoning "
                     "path: build a thermostat ledger - for each Snowball "
                     "episode, the trigger evidence, the frozen duration, "
                     "the estimated CO2 at deglaciation, and the recovery "
                     "timescale - then place today's forcing on the same "
                     "thermostat diagram to show where the million-year "
                     "clock sits relative to the century-scale problem. "
                     "Proposed mechanism: a deep-time thermostat diagram "
                     "with Snowball episodes, hothouse episodes (Eocene, "
                     "PETM), and the present as marked points - the single "
                     "image that puts 'the thermostat will fix it' in its "
                     "proper timescale context. What would confirm it: new "
                     "geochemical constraints converging the deglaciation "
                     "CO2 estimates, and thermostat models reproducing both "
                     "Snowball recovery and Phanerozoic climate bounds. "
                     "What would kill it: evidence that Snowballs never "
                     "fully froze (removing the outer bound), or a "
                     "thermostat mechanism that fails on Phanerozoic "
                     "data. What it does NOT claim: that the weathering "
                     "thermostat helps with today's warming - the ledger's "
                     "central message is the timescale mismatch: the "
                     "thermostat works in millions of years, and honest "
                     "deep-time perspective makes that unmistakable."),
        "key_points": [
            "Sturtian and Marinoan glaciations (~717-635 Ma): global ice cover twice or more.",
            "Trigger: ice-albedo runaway; recovery: volcanic CO2 over millions of years.",
            "Deglaciation may have required CO2 hundreds of times preindustrial.",
            "Cap carbonates record the hot CO2-rich aftermath.",
            "Weathering thermostat works on million-year timescales - no help this century.",
        ],
        "requirements": [
            "Thermostat ledger per episode: trigger, duration, deglaciation CO2, recovery time.",
            "Deep-time thermostat diagram with episodes and present marked.",
            "Geochemical convergence on deglaciation CO2 estimates.",
        ],
        "standards": ["IPCC AR6 WGI Chapter 2 (deep-time climate); Hoffman et al. 1998"],
        "citations": CIT_BASE + [
            "Hoffman PF et al. A Neoproterozoic Snowball Earth. Science; 1998.",
        ],
        "demo": {
            "quantity": "thermostat recovery clock vs human timescale", "unit": "years",
            "calc": "expr", "expr": "a2 * 1000", "base": 0.0,
            "assumptions": [("Snowball frozen duration (Myr)", 10, [5, 10, 60]),
                            ("deglaciation CO2 (x preindustrial)", 300, [100, 300, 1000]),
                            ("weathering recovery time (kyr)", 500, [100, 500, 2000])],
            "formula": "recovery_years = weathering_kyr * 1000; compare with 100-yr planning horizon",
            "checks": [((10, 300, 500), 500000, 1), ((5, 100, 100), 100000, 1)],
            "steps": [
                "Step 1: ledger each Snowball episode's trigger evidence.",
                "Step 2: ledger frozen duration and deglaciation CO2.",
                "Step 3: ledger the weathering recovery timescale.",
                "Step 4: place the present on the deep-time thermostat diagram.",
                "Step 5: read off the timescale mismatch explicitly.",
            ],
            "confirm": [
                "Geochemical constraints converge deglaciation CO2 estimates.",
                "Thermostat models reproduce Snowball recovery and Phanerozoic bounds.",
            ],
            "refute": [
                "Evidence that Snowballs never fully froze.",
                "A thermostat mechanism that fails on Phanerozoic data.",
            ],
            "note": "Thermostat-ledger explorer for Snowball Earth and deep-time limits.",
        },
    },
]
