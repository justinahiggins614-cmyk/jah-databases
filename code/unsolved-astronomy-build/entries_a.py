#!/usr/bin/env python3
"""Entries 1-9 (ladder ranks 1-9, Foundations) for the Unsolved Astronomy databases.

Every entry: key, name, group, ladder_rank, ladder_tier, problem, background,
why_it_matters, sig_pointer (public half), sig_solution (signature half, full
treatment opening with the exact honesty label), citations, demo_params.

Record schema used by build.py:
  id, t, g, name, title, description, problem, background, why_it_matters,
  signature_solution, src, ladder_rank, ladder_tier, citations, demo
"""

SIG_TAIL = ("Signature original - his original Signature solution method: every "
            "unsolved problem an open door, every proposed solution a labeled "
            "pathway with its confirm and refute conditions written down in "
            "advance, never presented as established science. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_MCKAY = ("McKay DS et al. Search for past life on Mars: possible relic "
             "biogenic activity in Martian meteorite ALH84001. Science; 1996.")
CIT_WEBSTER = ("Webster CR et al. Background levels of methane in Mars atmosphere "
               "show strong seasonal variations. Science; 2018.")
CIT_EHMAN = ("Ehman JR. The Big Ear Wow! signal. 30th anniversary report. "
             "Ohio State University Radio Observatory; 2007.")
CIT_PARIS = ("Paris A, Davies E. Hydrogen clouds from comets 266P/Christensen "
             "and P/2008 Y2 (Gibbs) are candidates for the source of the 1977 "
             "'Wow' signal. J Geophys Res Planets; 2017.")
CIT_MEECH = ("Meech KJ et al. A brief visit from a red and extremely elongated "
             "interstellar asteroid. Nature; 2017.")
CIT_MICHELE = ("Micheli M et al. Non-gravitational acceleration in the trajectory "
               "of 1I/2017 U1 ('Oumuamua). Nature; 2018.")
CIT_BATYGIN = ("Batygin K, Brown ME. Evidence for a distant giant planet in "
               "the solar system. Astron J; 2016.")
CIT_BROWN = ("Brown ME, Batygin K. The Planet Nine hypothesis. Phys Today; 2021.")
CIT_WITHBROE = ("Withbroe GL, Noyes RW. Mass and energy flow in the solar "
                "chromosphere and corona. Annu Rev Astron Astrophys; 1977.")
CIT_PARKER = ("Parker EN. Nanoflares and the solar X-ray corona. Astrophys J; 1988.")
CIT_GODFREY = ("Godfrey DA. A hexagonal feature around Saturn's north pole. "
               "Icarus; 1988.")
CIT_MORALES = ("Morales-Juberias R et al. Emergence of polar-jet polygons on "
               "giant planets. Astrophys J Lett; 2011.")
CIT_LORIMER = ("Lorimer DR et al. A bright millisecond radio burst of "
               "extragalactic origin. Science; 2007.")
CIT_MACQUART = ("Macquart JP et al. A census of baryons in the Universe from "
                "localized fast radio bursts. Nature; 2020.")
CIT_BOCHENEK = ("Bochenek CD et al. A fast radio burst associated with a "
                "Galactic magnetar. Nature; 2020.")
CIT_FERMI = ("Jones EM. Where is everybody? An account of Fermi's question. "
             "Los Alamos National Laboratory; 1985.")
CIT_HART = ("Hart MH. Explanation for the absence of extraterrestrials on "
            "Earth. Q J R Astron Soc; 1975.")
CIT_DRAKE = ("Drake FD. Project Ozma. Phys Today; 1961.")

ENTRIES_A = [
    {
        "key": "mars-life",
        "name": "Is There Life on Mars",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Is there life on Mars today, or was there life on Mars in the "
                    "past? Four decades of orbiters, landers, and rovers have found "
                    "water, organics, and seasonal methane, but no confirmed biosignature."),
        "background": (
            "Mars was once warmer and wetter: river valleys, lake beds, and the Jezero "
            "delta explored by the Perseverance rover record surface water billions of "
            "years ago. In 1976 the twin Viking landers ran life-detection experiments; "
            "the labeled-release experiment gave positive responses that were later "
            "attributed to reactive soil chemistry, including perchlorates discovered "
            "decades later. In 1996 a team announced possible fossil microbes in the "
            "Martian meteorite ALH84001, a claim most specialists now dispute but which "
            "revived the field of astrobiology. The Curiosity rover found organic "
            "molecules in ancient lake mudstones and detected seasonal methane swings "
            "in the atmosphere, and the Perseverance rover is caching samples for a "
            "future return to Earth. Today the honest state of the field is that Mars "
            "had habitable environments and still may have habitable niches underground, "
            "but no measurement yet requires biology to explain it."),
        "why_it_matters": (
            "A second, independent origin of life would rewrite biology: it would mean "
            "life is a cosmic commonplace rather than a one-off miracle. Even a negative "
            "answer, delivered with confidence, would sharpen the search for life on "
            "exoplanets by teaching us what a dead-but-habitable world looks like. "
            "The answer also decides how carefully human explorers must avoid "
            "contaminating, or being contaminated by, another biosphere."),
        "sig_pointer": (
            "The Signature edition of this record walks the full solution-explorer: a "
            "step-by-step proposed pathway for settling the Mars life question, with "
            "adjustable assumptions and written-down confirm and refute conditions."),
        "sig_solution": (
            "Assumptions: Martian life, if it exists, is most likely deep subsurface "
            "microbial life in briny aquifers, metabolizing without sunlight. Reasoning: "
            "surface conditions are sterilizing, but the deep subsurface offers liquid "
            "water films, chemical energy gradients, and shielding, so the search should "
            "be restructured as a subsurface energy-budget problem rather than a surface "
            "chemistry hunt. Proposed method: map subsurface water with radar and "
            "neutron spectroscopy, drill to the water table at multiple sites, and run "
            "three independent life tests on each sample - metabolic activity, "
            "molecular complexity patterns, and morphological structure - requiring all "
            "three before any claim. What would confirm it: the same sample passing all "
            "three independent tests with abiotic controls failing them. What would "
            "kill it: repeated deep-drilling campaigns finding organics and energy "
            "sources but zero correlated metabolic or structural signals. What this "
            "does NOT claim: it does not claim life is there, does not claim the "
            "methane is biological, and does not propose that any single instrument "
            "can settle the question alone."),
        "citations": [CIT_MCKAY, CIT_WEBSTER],
        "demo_params": {"fp_rates": [0.30, 0.20, 0.10]},
    },
    {
        "key": "wow-signal",
        "name": "The Wow! Signal",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("On August 15, 1977, the Big Ear radio telescope recorded a powerful "
                    "narrowband signal near the hydrogen line that lasted 72 seconds and "
                    "never repeated. What produced the Wow! signal?"),
        "background": (
            "The signal arrived at 1420 MHz, the famous hydrogen line that SETI pioneers "
            "Cocconi and Morrison had flagged as a natural interstellar hailing frequency "
            "in 1959. Volunteer astronomer Jerry Ehman circled the printout and wrote "
            "'Wow!' beside the intensity code 6EQUJ5, indicating a signal about 30 times "
            "stronger than background noise. Its rise-and-fall profile matched exactly "
            "what a fixed celestial source would look like drifting through the "
            "telescope beam. Decades of follow-up observations of the same sky region "
            "found nothing, and no natural explanation has been confirmed. In 2017 a "
            "proposal blamed hydrogen clouds around two comets that happened to be in "
            "the area, but follow-up analysis found the comet hypothesis could not "
            "reproduce the signal strength. It remains the most famous unexplained "
            "transient in radio astronomy."),
        "why_it_matters": (
            "A confirmed artificial origin would be the discovery of extraterrestrial "
            "intelligence - the single most consequential finding in science. A confirmed "
            "natural origin would still matter: it would reveal a new astrophysical "
            "phenomenon capable of mimicking an artificial beacon. Either way, the "
            "signal is a calibration point for every technosignature search that follows."),
        "sig_pointer": (
            "The Signature edition walks a proposed observational pathway for closing "
            "the Wow! case, with adjustable assumptions and explicit confirm and refute "
            "conditions, in the solution-explorer walkthrough."),
        "sig_solution": (
            "Assumptions: the 1977 printout is an accurate record of a real sky signal, "
            "not interference or a data artifact. Reasoning: a 30-sigma narrowband "
            "detection with the correct beam-drift profile is extraordinarily hard to "
            "produce by chance, so the case should be treated as an unsolved detection "
            "awaiting a decisive test rather than a curiosity. Proposed method: conduct "
            "a deep, long-dwell stare at both candidate sky positions with a modern "
            "array, recording full polarization and high spectral resolution, while "
            "simultaneously monitoring with an independent telescope hundreds of "
            "kilometers away to veto local interference. What would confirm an "
            "artificial origin: a repeat detection with the same drift profile, "
            "narrow bandwidth, and sidereal repeatability at both stations. What would "
            "kill it: a demonstrated natural source - such as a transient hydrogen "
            "maser event - reproducing the exact intensity profile, or a conclusive "
            "showing that 1970s interference could mimic the printout. What this does "
            "NOT claim: it does not claim the signal was aliens, does not claim comets "
            "are ruled out, and does not claim one more non-detection would settle "
            "anything."),
        "citations": [CIT_EHMAN, CIT_PARIS],
        "demo_params": {"snr_sigma": 30.0, "beam_seconds": 72.0},
    },
    {
        "key": "oumuamua",
        "name": "The Oumuamua Mystery",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("In 2017 the first known interstellar object, 1I/Oumuamua, swept "
                    "through the solar system - elongated, tumbling, reddish, accelerating "
                    "slightly without any visible outgassing. What was it?"),
        "background": (
            "Oumuamua was discovered by the Pan-STARRS survey in October 2017, already "
            "leaving the solar system on a hyperbolic trajectory that proved it came "
            "from another star. Its light curve swung by about 2.5 magnitudes, implying "
            "an extreme elongated shape, roughly ten times longer than wide if the "
            "variation came from shape alone. It showed a small non-gravitational "
            "acceleration pushing it away from the Sun, the classic signature of "
            "outgassing - yet no coma, no tail, and no dust were ever detected. Proposed "
            "explanations have ranged from a hydrogen iceberg to a nitrogen ice fragment "
            "chipped off an exo-Pluto, a fractal dust aggregate, and even an artificial "
            "light sail. The second interstellar visitor, 2I/Borisov in 2019, behaved "
            "like an ordinary comet, which only deepened the puzzle of why the first "
            "one did not."),
        "why_it_matters": (
            "Interstellar objects are physical samples of other planetary systems, "
            "delivered free of charge. Understanding Oumuamua would calibrate how "
            "planets eject debris and what the building blocks of alien worlds look "
            "like. If any interstellar object ever proved artificial, it would be the "
            "first direct evidence of extraterrestrial technology - so each one deserves "
            "a rigorous natural explanation first."),
        "sig_pointer": (
            "The Signature edition runs the full solution-explorer: the shape, spin, "
            "and acceleration numbers worked through step by step with adjustable "
            "assumptions and confirm/refute panels."),
        "sig_solution": (
            "Assumptions: the light curve and astrometry are correct, and the "
            "non-gravitational acceleration is real and Sun-directed. Reasoning: the "
            "puzzle is over-constrained - the object must be elongated, low-density or "
            "highly reflective, and able to accelerate without visible dust - so the "
            "honest approach is to compute which single material satisfies all "
            "constraints at once. Proposed method: build a constraint-satisfaction "
            "model combining the 10-to-1 shape ratio, the measured acceleration, and "
            "upper limits on dust and gas production, then score candidate compositions "
            "(water ice, nitrogen ice, hydrogen ice, porous aggregate) against all "
            "three simultaneously. What would confirm the leading natural model: a "
            "future interstellar object with the same acceleration-without-coma "
            "signature caught early enough for spectroscopy of its outgassing. What "
            "would kill it: a demonstrated laboratory or observational case that no "
            "known ice can produce the observed acceleration at the observed "
            "non-detection limits. What this does NOT claim: it does not claim "
            "Oumuamua was artificial, does not claim the nitrogen-ice model is proven, "
            "and does not claim the next interstellar visitor will look the same."),
        "citations": [CIT_MEECH, CIT_MICHELE],
        "demo_params": {"delta_mag": 2.5, "accel": 4.92e-6},
    },
    {
        "key": "planet-nine",
        "name": "Planet Nine",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("A half-dozen distant icy bodies beyond Neptune share oddly aligned "
                    "orbits. Is a hidden giant planet - Planet Nine - shepherding them, "
                    "or is the pattern an illusion?"),
        "background": (
            "In 2016 Konstantin Batygin and Mike Brown showed that the most distant "
            "Kuiper Belt objects cluster in their orbital orientations far more than "
            "chance would allow. Their proposed explanation was a planet of roughly 5 "
            "to 10 Earth masses orbiting 400 to 800 times farther from the Sun than "
            "Earth, on a tilted, elongated orbit taking some 10,000 years per circuit. "
            "No telescope has found it yet, and the search area spans much of the sky "
            "because the planet would be incredibly faint. Skeptics argue the clustering "
            "is an artifact of where surveys happened to look, and alternative "
            "explanations range from a massive debris disk to a primordial black hole. "
            "Deep surveys with the Subaru telescope continue the hunt, and the Vera "
            "Rubin Observatory is expected to either find the planet or rule out most "
            "of its allowed orbits."),
        "why_it_matters": (
            "A ninth planet would rewrite the architecture of our solar system and "
            "explain several long-standing oddities of the outer system. Finding it - "
            "or conclusively ruling it out - would also validate or retire the "
            "techniques astronomers use to infer unseen planets around other stars. "
            "The statistical debate itself is teaching the field how to avoid fooling "
            "itself with selection bias."),
        "sig_pointer": (
            "The Signature edition walks the orbital-numbers pathway: predicted mass, "
            "orbit, and brightness computed step by step, with confirm and refute "
            "conditions for the decade-long search."),
        "sig_solution": (
            "Assumptions: the orbital clustering of extreme trans-Neptunian objects is "
            "a real dynamical signal, not purely observational bias. Reasoning: if a "
            "shepherd exists, its mass and orbit are constrained by the same clustering "
            "it must explain, so the search box can be computed rather than guessed. "
            "Proposed method: run large ensembles of N-body simulations over the "
            "allowed mass-orbit grid, score each against the observed clustering "
            "strength, and publish the resulting probability map so every survey "
            "points at the highest-probability sky first. What would confirm it: "
            "direct imaging or a multi-year parallax track matching a bound orbit. "
            "What would kill it: the Rubin Observatory completing its census with no "
            "candidate and a bias-corrected analysis showing the clustering was a "
            "survey artifact. What this does NOT claim: it does not claim the planet "
            "exists, does not claim the simulations pick a unique orbit, and does not "
            "claim the black-hole alternative is ruled out."),
        "citations": [CIT_BATYGIN, CIT_BROWN],
        "demo_params": {"mass_earth": 6.0, "a_au": 460.0},
    },
    {
        "key": "corona-heating",
        "name": "Why the Solar Corona Is Millions of Degrees Hotter Than the Surface",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("The Sun's visible surface is about 5,800 K, but the wispy corona "
                    "above it burns at 1 to 3 million K. What heats the corona against "
                    "the flow of heat?"),
        "background": (
            "The puzzle dates to the 1940s, when Bengt Edlen identified coronal spectral "
            "lines as highly ionized iron - atoms stripped of many electrons, which "
            "requires million-degree temperatures. Heat should flow from hot to cold, "
            "so something must be dumping energy into the corona faster than it can "
            "radiate away. The energy budget is known: active regions need roughly "
            "10,000 watts per square meter, the quiet Sun a few hundred. The leading "
            "candidates are nanoflares - myriad tiny magnetic reconnection bursts "
            "proposed by Eugene Parker in 1988 - and the dissipation of Alfven waves "
            "traveling up along magnetic field lines. Modern observatories including "
            "the Parker Solar Probe, flying through the corona itself, and the Daniel "
            "K. Inouye Solar Telescope are now measuring the magnetic energy flows "
            "directly, but no single mechanism has been shown to carry the full budget."),
        "why_it_matters": (
            "Coronal heating drives the solar wind and space weather that batters "
            "satellites, power grids, and astronauts. Solving it would complete our "
            "understanding of how stars energize their atmospheres - and stellar "
            "coronae bathe every potentially habitable exoplanet in high-energy "
            "radiation. It is also a pure physics puzzle: magnetic energy converting "
            "to heat in a near-vacuum plasma."),
        "sig_pointer": (
            "The Signature edition runs the energy-budget walkthrough: required flux, "
            "wave flux, and nanoflare power compared step by step with adjustable "
            "assumptions and confirm/refute panels."),
        "sig_solution": (
            "Assumptions: the measured energy requirements are correct - about 10,000 "
            "W/m2 for active regions and a few hundred for quiet Sun - and the corona "
            "is heated in place rather than by conduction from below. Reasoning: the "
            "debate has stalled on qualitative arguments, so the way forward is a strict "
            "energy ledger: every proposed mechanism must show its measured flux meets "
            "or exceeds the requirement with no hand-waving. Proposed method: combine "
            "Parker Solar Probe in-situ wave measurements with DKIST magnetic field "
            "maps to build a complete input-output energy budget for a single active "
            "region, counting wave flux in, nanoflare burst statistics, and radiative "
            "losses out. What would confirm a mechanism: measured energy input matching "
            "the required flux within uncertainties across multiple regions and solar "
            "conditions. What would kill a candidate: a complete ledger showing its "
            "maximum possible flux falls an order of magnitude short. What this does "
            "NOT claim: it does not claim nanoflares or waves alone are the answer, "
            "does not claim the budget is closed, and does not claim laboratory plasma "
            "results transfer directly to the Sun."),
        "citations": [CIT_WITHBROE, CIT_PARKER],
        "demo_params": {"required_w_m2": 1.0e4, "rho": 1.0e-12, "v": 2.0e4, "v_alfven": 1.0e6},
    },
    {
        "key": "saturn-hexagon",
        "name": "Saturn's Hexagon",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("Saturn's north pole hosts a perfect six-sided jet stream wider "
                    "than Earth that has persisted for decades. What sculpts a hexagon "
                    "out of a gas giant's atmosphere?"),
        "background": (
            "Voyager first spotted the hexagon in 1981, and the Cassini orbiter watched "
            "it in detail from 2004 to 2017. The feature is a meandering eastward jet "
            "near 78 degrees north latitude, about 29,000 kilometers across, rotating "
            "with a period near 10 hours 39 minutes. Laboratory and computer models "
            "show that a fast jet on a rotating sphere can develop stationary "
            "large-scale waves - Rossby waves - and under the right speed profile the "
            "dominant wave settles at wavenumber six. Curiously, Saturn's south pole "
            "has a hurricane-like vortex but no polygon, and no other planet shows "
            "such a clean geometric storm. The hexagon's decades-long stability makes "
            "it a natural laboratory for the fluid dynamics of rotating atmospheres."),
        "why_it_matters": (
            "The hexagon is the cleanest example of self-organized geometry in a "
            "planetary atmosphere - order emerging from turbulence. Understanding it "
            "sharpens models of jet streams on Earth, where meandering Rossby waves "
            "steer weather systems, and on exoplanets, where we may one day map storm "
            "shapes directly. It is also a reminder that simple physics can paint "
            "startlingly precise patterns."),
        "sig_pointer": (
            "The Signature edition walks the wave-number calculation: jet speed, "
            "rotation rate, and the wavenumber-six resonance worked through with "
            "adjustable assumptions."),
        "sig_solution": (
            "Assumptions: the hexagon is a Rossby wave imprinted on a zonal jet, and "
            "the jet's speed profile measured by Cassini is representative. Reasoning: "
            "wavenumber six is not magic - it is the resonant mode where the jet's "
            "speed, the planet's rotation, and the wave's drift lock together, so the "
            "test is whether the numbers lock without fine-tuning. Proposed method: "
            "extract the jet speed profile from Cassini wind tracking, compute the "
            "stationary Rossby wavenumber as a function of latitude, and check that "
            "wavenumber six emerges as the stable mode at 78 degrees north while other "
            "latitudes and the south pole give different or no stable polygon. What "
            "would confirm it: the calculation predicting six at the north and no "
            "polygon at the south from the measured profiles alone. What would kill "
            "it: a profile that predicts wavenumber five or seven at the hexagon's "
            "latitude, or a decade of monitoring showing the shape drifting in ways "
            "the wave model forbids. What this does NOT claim: it does not claim the "
            "jet's energy source is known, does not claim to predict when the hexagon "
            "formed, and does not claim laboratory tanks capture the full physics."),
        "citations": [CIT_GODFREY, CIT_MORALES],
        "demo_params": {"jet_speed": 100.0, "lat_deg": 78.0, "r_saturn_km": 58232.0},
    },
    {
        "key": "fast-radio-bursts",
        "name": "What Produces Fast Radio Bursts",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("Fast radio bursts are millisecond flashes of radio light from "
                    "across the universe, some repeating, most seen once. What object "
                    "or process fires them?"),
        "background": (
            "The first FRB was found in 2007 in archival Parkes telescope data by "
            "Duncan Lorimer's team - a single millisecond burst brighter than anything "
            "in its patch of sky. Their dispersion, the smearing of the signal by "
            "intergalactic electrons, proved they come from cosmological distances, "
            "and the 2020 Macquart relation turned that smearing into a tool that "
            "located the universe's missing matter. Over a thousand are now known; a "
            "minority repeat, sometimes on clocklike cycles. In 2020 a Galactic "
            "magnetar, SGR 1935+2154, emitted an FRB-like burst, strongly implicating "
            "magnetars for at least some events. But no single mechanism explains the "
            "full population: the energies span orders of magnitude, some bursts show "
            "intricate time-frequency structure, and the one-off majority have never "
            "been seen to repeat."),
        "why_it_matters": (
            "FRBs are the most extreme radio transients known, releasing in a "
            "millisecond what the Sun emits in days. Identifying their engines would "
            "open a new window on neutron stars, magnetic fields, and possibly new "
            "physics. Already they serve as cosmic probes: each burst weighs the "
            "electrons along its line of sight, mapping matter across the universe."),
        "sig_pointer": (
            "The Signature edition walks the energetics: burst energy from fluence and "
            "distance, compared against magnetar budgets, with adjustable assumptions "
            "and confirm/refute panels."),
        "sig_solution": (
            "Assumptions: the dispersion distances are correct and the emission is at "
            "most mildly beamed. Reasoning: the population splits naturally - "
            "repeaters with structure versus one-off cannon shots - so the productive "
            "question is which engine powers each class, judged by energy budgets "
            "that must balance. Proposed method: for every well-localized burst, "
            "compute the isotropic-equivalent energy from fluence and distance, then "
            "test each engine class (young magnetar flares, magnetar giant flares, "
            "compact-object mergers, exotic models) against three filters: total "
            "energy available, repetition duty cycle, and host-galaxy environment. "
            "What would confirm a magnetar origin for a class: a repeater caught "
            "simultaneously in radio and X-rays with the X-ray energy exceeding the "
            "radio, matching magnetar flare ratios. What would kill it: a one-off "
            "burst localized to an old elliptical galaxy with energy far beyond any "
            "magnetar budget and no young stellar population. What this does NOT "
            "claim: it does not claim all FRBs share one engine, does not claim "
            "magnetars are proven for repeaters, and does not claim beaming is "
            "negligible."),
        "citations": [CIT_LORIMER, CIT_MACQUART, CIT_BOCHENEK],
        "demo_params": {"fluence_jy_ms": 1.0, "z": 0.193, "bandwidth_mhz": 400.0},
    },
    {
        "key": "fermi-paradox",
        "name": "The Fermi Paradox: Where Is Everybody",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("The galaxy is old enough for civilizations to have colonized it "
                    "many times over, yet we see no one. Where is everybody?"),
        "background": (
            "Enrico Fermi reportedly posed the question over lunch in 1950: if "
            "intelligent life is common, the galaxy should be crawling with evidence "
            "of it. The Drake equation, formulated by Frank Drake in 1961, breaks the "
            "question into factors - star formation, habitable planets, life, "
            "intelligence, longevity - most of which were guesses at the time. Since "
            "then, exoplanet surveys have found over 5,000 worlds and shown that "
            "roughly one in five Sun-like stars hosts an Earth-size planet in its "
            "habitable zone. SETI searches, including Breakthrough Listen, have "
            "scanned millions of stars and nearby galaxies for technosignatures and "
            "found nothing conclusive. Proposed resolutions range from the Rare Earth "
            "hypothesis to the Great Filter, the zoo hypothesis, and the sobering "
            "possibility that technological civilizations are simply short-lived."),
        "why_it_matters": (
            "The paradox is a mirror: our answer reveals our assumptions about life, "
            "intelligence, and survival. If the Great Filter lies ahead of us, "
            "humanity faces an existential warning; if behind us, we may be rare and "
            "precious. Practically, it sets the strategy for every SETI search and "
            "every biosignature mission - where to look and what counts as evidence."),
        "sig_pointer": (
            "The Signature edition runs the numbers walkthrough: the Drake equation "
            "with adjustable factors, search completeness, and the longevity term "
            "isolated as the decisive unknown."),
        "sig_solution": (
            "Assumptions: the exoplanet statistics are correct - habitable-zone rocky "
            "planets are common - and our searches have covered only a tiny fraction "
            "of the parameter space. Reasoning: the paradox dissolves into a single "
            "term - the average lifetime of a technological civilization - because "
            "every other Drake factor is now measured or bounded except longevity. "
            "Proposed method: compute the expected number of detectable civilizations "
            "as a function of the longevity term alone, holding the now-measured "
            "factors fixed, and compare against the actual completeness of radio and "
            "optical SETI searches to show which longevities are already ruled out and "
            "which remain open. What would confirm the short-lived hypothesis: "
            "statistical evidence that technological civilizations self-limit on "
            "thousand-year timescales, or a confirmed technosignature proving "
            "longevity is possible. What would kill it: a deep all-sky survey at "
            "Breakthrough Listen sensitivity finding zero candidates, which would push "
            "the bound toward rarity rather than brevity. What this does NOT claim: "
            "it does not claim aliens exist, does not claim the Great Filter is real, "
            "and does not claim our searches have been remotely complete."),
        "citations": [CIT_FERMI, CIT_HART, CIT_DRAKE],
        "demo_params": {"r_star": 1.5, "fp": 0.9, "ne": 0.4, "fl": 0.5, "fi": 0.2, "fc": 0.2},
    },
    {
        "key": "exoplanet-biosignatures",
        "name": "How to Recognize Life on Another World",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("Telescopes can now sniff exoplanet atmospheres, but which gases - "
                    "or combinations - would actually prove biology rather than "
                    "chemistry?"),
        "background": (
            "James Lovelock argued in the 1960s that life reveals itself through "
            "atmospheric disequilibrium: oxygen and methane coexist on Earth only "
            "because biology constantly replenishes both. Modern spectroscopy with "
            "JWST is beginning to measure molecules like water, carbon dioxide, and "
            "methane in exoplanet atmospheres. In 2025 a team reported possible "
            "dimethyl sulfide on the ocean world K2-18b, a molecule made by marine "
            "life on Earth - a claim immediately challenged as statistically weak and "
            "open to abiotic explanations. The field has learned hard lessons: "
            "oxygen can build up abiotically on planets around flare stars through "
            "water photolysis, and methane can pour out of volcanic rock. No single "
            "gas is a smoking gun; the community is converging on context - the "
            "planet, the star, and the combination of gases together."),
        "why_it_matters": (
            "This is the operational core of the search for life: without agreed "
            "biosignature criteria, every detection claim becomes an unresolvable "
            "argument. Getting it right means the difference between announcing life "
            "prematurely and missing it entirely. The standards built now will govern "
            "the flagship life-finding missions of the coming decades."),
        "sig_pointer": (
            "The Signature edition walks the detection arithmetic: signal strength, "
            "transits required, and the disequilibrium test, with adjustable "
            "assumptions and confirm/refute panels."),
        "sig_solution": (
            "Assumptions: transmission spectroscopy will remain the workhorse method, "
            "and stellar contamination can be modeled but never perfectly removed. "
            "Reasoning: the field keeps relitigating single-gas claims, so the fix is "
            "a published decision ladder - a gas pair plus planetary context plus a "
            "required statistical threshold - agreed before the next claim, not after. "
            "Proposed method: define a three-rung biosignature standard - (1) a "
            "thermodynamic disequilibrium pair such as oxygen plus methane, (2) a "
            "planetary context ruling out the known abiotic routes for that pair, and "
            "(3) independent confirmation by a second instrument or method - and "
            "compute for representative targets how many transits each rung costs. "
            "What would confirm a detection: a target clearing all three rungs with "
            "the abiotic null models quantitatively excluded. What would kill a "
            "candidate: any single abiotic pathway reproducing the observed spectrum "
            "within the measurement uncertainties. What this does NOT claim: it does "
            "not claim K2-18b shows life, does not claim oxygen is useless as a "
            "biosignature, and does not claim the ladder replaces detailed modeling."),
        "citations": [("Seager S. Exoplanet biosignatures: understanding oxygen as "
                       "a biosignature. Proc Natl Acad Sci; 2014."),
                      ("Meadows VS et al. Exoplanet biosignatures: understanding "
                       "oxygen as a biosignature. Astrobiology; 2018.")],
        "demo_params": {"snr_per_transit": 1.2, "required_snr": 5.0},
    },
]
