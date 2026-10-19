#!/usr/bin/env python3
"""Entries 10-17 (ladder ranks 10-17, Foundations/Compounded)."""

CIT_MAYOR = ("Mayor M, Queloz D. A Jupiter-mass companion to a solar-type star. "
             "Nature; 1995.")
CIT_LIN = ("Lin DNC, Papaloizou JCB. On the tidal interaction between protoplanets "
           "and the primordial solar nebula. Mon Not R Astron Soc; 1986.")
CIT_ALEXANDER = ("Alexander CMO et al. The provenances of asteroids, and their "
                 "contributions to the volatile inventories of the terrestrial "
                 "planets. Science; 2012.")
CIT_HARTLEY = ("Hartogh P et al. Ocean-like water in the Jupiter-family comet "
               "103P/Hartley 2. Nature; 2011.")
CIT_HARTMANN = ("Hartmann WK, Davis DR. Satellite-sized planetesimals and lunar "
                "origin. Icarus; 1975.")
CIT_CANUP = ("Canup RM. Forming a Moon with an Earth-like composition via a giant "
             "impact. Science; 2012.")
CIT_LOCK = ("Lock SJ, Stewart ST. The structure of terrestrial bodies: impact "
            "heating, corotation limits, and synestias. J Geophys Res Planets; 2017.")
CIT_JEWITT = ("Jewitt DC, Trujillo CA, Luu JX. Population and size distribution "
              "of small jovian Trojan asteroids. Astron J; 2000.")
CIT_ALLEN = ("Allen RL, Bernstein GM, Malhotra R. The edge of the solar system. "
              "Astrophys J Lett; 2001.")
CIT_AUGER = ("Pierre Auger Collaboration. Measurement of the energy spectrum of "
              "cosmic rays above 1e18 eV. Phys Rev Lett; 2008.")
CIT_GZK = ("Greisen K. End to the cosmic-ray spectrum? Phys Rev Lett; 1966.")
CIT_AMATERASU = ("Telescope Array Collaboration. An extremely energetic cosmic ray "
                 "observed by a surface detector array. Science; 2023.")
CIT_KLEBESAD = ("Klebesadel RW, Strong IB, Olson RA. Observations of gamma-ray "
                "bursts of cosmic origin. Astrophys J Lett; 1973.")
CIT_WOOSLEY = ("Woosley SE. Gamma-ray bursts from stellar mass accretion disks "
               "around black holes. Astrophys J; 1993.")
CIT_ABBOT = ("Abbott BP et al. Multi-messenger observations of a binary neutron "
             "star merger. Astrophys J Lett; 2017.")
CIT_ABEL = ("Abel T, Bryan GL, Norman ML. The formation of the first star in "
            "the Universe. Science; 2002.")
CIT_HIRANO = ("Hirano S et al. One hundred first stars. Astrophys J; 2014.")
CIT_BAÑADOS = ("Banados E et al. An 800-million-solar-mass black hole in a "
               "significantly neutral Universe at redshift 7.5. Nature; 2018.")
CIT_VOLONTERI = ("Volonteri M. The formation and evolution of massive black holes. "
                 "Science; 2012.")

ENTRIES_B = [
    {
        "key": "hot-jupiters",
        "name": "Hot Jupiters: Giants in Scorching Orbits",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("Giant planets orbit some stars in just days, closer than Mercury "
                    "is to the Sun - yet gas giants should only form far out where it "
                    "is cold. How did hot Jupiters get there?"),
        "background": (
            "The first exoplanet around a Sun-like star, 51 Pegasi b, announced by "
            "Michel Mayor and Didier Queloz in 1995, was a Jupiter-mass world on a "
            "4.2-day orbit - a configuration theorists had considered impossible, "
            "winning the pair the 2019 Nobel Prize. Core-accretion theory says giant "
            "planets need solid cores that grow beyond the ice line, several AU out. "
            "The leading fix is migration: the planet formed far out and spiraled "
            "inward through gravitational interaction with the gas disk, or was flung "
            "inward by gravitational scattering and then circularized by tides. "
            "Evidence is mixed: some hot Jupiters orbit neatly aligned with their "
            "star's spin, favoring gentle disk migration, while others are wildly "
            "misaligned, favoring violent scattering. A minority view holds that "
            "some formed roughly where they are."),
        "why_it_matters": (
            "Hot Jupiters were the first exoplanets ever found and remain the easiest "
            "to study - their atmospheres are the training ground for all exoplanet "
            "characterization. Their migration history determines whether planetary "
            "systems like ours are the norm or a lucky calm outcome. Understanding "
            "migration is essential for predicting where Earth-like planets survive."),
        "sig_pointer": (
            "The Signature edition walks the migration arithmetic: orbital period from "
            "Kepler's law, tidal circularization timescales, and the alignment test "
            "that separates the migration channels."),
        "sig_solution": (
            "Assumptions: 51 Pegasi b's measured mass and 4.2-day period are correct, "
            "and core accretion beyond the ice line is the formation mechanism. "
            "Reasoning: the migration channels make different predictions about "
            "spin-orbit alignment and companion planets, so the case can be settled "
            "statistically rather than per-planet. Proposed method: compile the "
            "aligned-versus-misaligned fraction across a large hot-Jupiter sample, "
            "compute the tidal realignment timescale for each system, and test "
            "whether the misaligned survivors are exactly those whose stars cannot "
            "tidally realign them - the smoking gun of violent scattering. What would "
            "confirm disk migration as dominant: a sample where aligned systems "
            "outnumber the tidal-realignment prediction. What would kill a channel: "
            "finding that misaligned systems have realignment times far shorter than "
            "their ages, meaning the misalignment must be primordial. What this does "
            "NOT claim: it does not claim all hot Jupiters migrated the same way, "
            "does not claim in-situ formation is ruled out, and does not claim "
            "migration theory is complete."),
        "citations": [CIT_MAYOR, CIT_LIN],
        "demo_params": {"a_au": 0.0527, "m_star_msun": 1.06},
    },
    {
        "key": "earth-water",
        "name": "Where Did Earth's Water Come From",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("Earth formed inside the snow line where water should have been "
                    "scarce, yet it has oceans. Did our water arrive on asteroids and "
                    "comets, or was it here all along?"),
        "background": (
            "The inner solar system was too hot for water ice to condense when the "
            "planets formed, so Earth's oceans are a delivery puzzle. The detective "
            "tool is the deuterium-to-hydrogen ratio: Earth's ocean water matches "
            "carbonaceous chondrite asteroids closely, while most comets measured so "
            "far are enriched in heavy hydrogen - except the Jupiter-family comet "
            "103P/Hartley 2, which matches Earth's oceans. Dynamical models show "
            "Jupiter's migration could have scattered water-rich asteroids inward, "
            "and recent work suggests the deep mantle holds several oceans' worth of "
            "water in minerals like ringwoodite, pointing to an endogenous "
            "contribution. The current consensus favors asteroids as the main source "
            "with a possible cometary minority, but the exact recipe is unsettled."),
        "why_it_matters": (
            "Water delivery decides whether rocky planets routinely end up habitable "
            "or whether Earth won a cosmic lottery. The answer calibrates how "
            "common ocean worlds should be around other stars. It also bears on "
            "Earth's own deep history: mantle water affects plate tectonics, "
            "volcanism, and the long-term climate."),
        "sig_pointer": (
            "The Signature edition walks the isotope arithmetic: D/H mixing fractions "
            "for asteroid versus comet sources, computed against the ocean standard."),
        "sig_solution": (
            "Assumptions: the measured D/H ratios of ocean water, carbonaceous "
            "chondrites, and comets are representative of their reservoirs. "
            "Reasoning: isotopes do not lie about provenance - Earth's water must be "
            "a mixture whose D/H is the weighted average of its sources, so the "
            "mixing fractions are a solvable algebra problem. Proposed method: solve "
            "the two-source mixing equation for the asteroidal versus cometary "
            "fractions using the best current D/H values, then propagate the "
            "measurement uncertainties to show the allowed range, and fold in the "
            "mantle-water reservoir as a third source. What would confirm asteroid "
            "dominance: returned samples from carbonaceous asteroids matching ocean "
            "D/H within tight bounds across multiple bodies. What would kill the "
            "comet-minority view: a population survey showing most Jupiter-family "
            "comets share Earth's D/H, not just Hartley 2. What this does NOT claim: "
            "it does not claim comets contributed nothing, does not claim the mantle "
            "reservoir is quantified, and does not claim D/H alone closes the case."),
        "citations": [CIT_ALEXANDER, CIT_HARTLEY],
        "demo_params": {"dh_earth": 1.56e-4, "dh_asteroid": 1.50e-4, "dh_comet": 3.10e-4},
    },
    {
        "key": "moon-formation",
        "name": "Exactly How the Moon Formed",
        "group": "Compounded",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "problem": ("The giant-impact theory says a Mars-size body struck the early "
                    "Earth, but the Moon is isotopically almost identical to Earth - "
                    "too identical for a random impactor. What really happened?"),
        "background": (
            "The giant-impact hypothesis, developed by Hartmann and Davis and by "
            "Cameron and Ward in the 1970s, explains the Moon's small iron core and "
            "the Earth-Moon system's angular momentum. But high-precision measurements "
            "show the Moon's oxygen, titanium, and tungsten isotopes match Earth's to "
            "extraordinary precision - surprising if half the Moon came from an "
            "impactor with a different composition. Proposed fixes include a "
            "fast-spinning early Earth flinging off mantle material, an impactor made "
            "of the same stuff as Earth, thorough mixing in the aftermath, and the "
            "synestia model - a vaporized, donut-shaped Earth-Moon structure in "
            "which the Moon condensed from well-mixed material. Each variant "
            "reproduces some observables and strains against others."),
        "why_it_matters": (
            "The Moon stabilizes Earth's tilt and drives tides that may have helped "
            "life; its formation is inseparable from Earth's early habitability. The "
            "isotope crisis is also a stress test for planet-formation models "
            "everywhere: if we cannot explain our own Moon's composition, our models "
            "of rocky exoplanets rest on shaky ground."),
        "sig_pointer": (
            "The Signature edition walks the angular-momentum and isotope ledgers: "
            "what each impact variant must balance, with confirm and refute panels."),
        "sig_solution": (
            "Assumptions: the isotopic measurements are correct and the present "
            "Earth-Moon angular momentum is the post-impact value minus tidal "
            "evolution. Reasoning: the problem is a ledger with two columns - "
            "isotopes and angular momentum - and every model must balance both, so "
            "the honest test is quantitative scoring, not narrative preference. "
            "Proposed method: build a scoring matrix for the leading variants "
            "(canonical impact, fast-spinning Earth, equal-composition impactor, "
            "synestia), computing for each the predicted isotopic offset and the "
            "required initial angular momentum, and rank them by total deviation "
            "from the measured values. What would confirm a variant: a simulation "
            "that simultaneously matches the isotopic identity and the angular "
            "momentum with no tuned parameters. What would kill the canonical model "
            "for good: a confirmed isotopic difference in a refractory element that "
            "no mixing scenario can erase. What this does NOT claim: it does not "
            "claim any variant is proven, does not claim the impactor's composition "
            "is known, and does not claim simulations have converged."),
        "citations": [CIT_HARTMANN, CIT_CANUP, CIT_LOCK],
        "demo_params": {"L_earth_moon": 3.41e34, "L_spin_earth": 5.86e33},
    },
    {
        "key": "kuiper-cliff",
        "name": "The Kuiper Cliff",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("The Kuiper Belt - the solar system's icy debris disk - ends "
                    "abruptly around 48 AU for no obvious reason. What truncated it?"),
        "background": (
            "Beyond Neptune lies the Kuiper Belt, source of short-period comets and "
            "home of Pluto. Surveys show its density of objects falls off a cliff "
            "near 48 AU, well inside the range where the Sun's gravity still holds "
            "sway. A smooth protoplanetary disk should have continued outward, and "
            "telescopes are sensitive enough to have seen objects beyond the edge if "
            "they were there. Proposed explanations include a close stellar encounter "
            "in the Sun's birth cluster stripping the outer disk, Neptune's migration "
            "sculpting the edge, or a yet-unseen planet truncating the distribution. "
            "The cliff's sharpness is the clue: whatever did it acted decisively."),
        "why_it_matters": (
            "The cliff is a fossil of the solar system's violent youth - its cause "
            "dates the events that shaped the outer planets. It also calibrates "
            "debris-disk models used to interpret the dusty rings seen around other "
            "stars. If a stellar encounter did it, our Sun was born in a crowded "
            "cluster whose siblings may still be identifiable."),
        "sig_pointer": (
            "The Signature edition walks the density-drop arithmetic: observed counts "
            "versus a smooth-disk extrapolation, and the encounter energy needed to "
            "cut the edge."),
        "sig_solution": (
            "Assumptions: survey completeness is well characterized out to 60 AU, so "
            "the missing objects are really missing. Reasoning: a smooth disk "
            "extrapolated outward predicts a definite number of detections beyond 48 "
            "AU, so the shortfall is a number that candidate mechanisms must "
            "reproduce. Proposed method: compute the expected beyond-cliff detections "
            "from the measured size distribution, then test each truncation "
            "mechanism - stellar encounter, Neptune migration resonance sweeping, "
            "unseen planet - for whether it reproduces both the cliff location and "
            "its sharpness. What would confirm the stellar-encounter model: "
            "identifying solar siblings whose trajectories converge on a close pass "
            "at the right epoch. What would kill it: a deep survey finding a smooth "
            "continuation of small objects beyond the cliff, showing the edge is a "
            "size-sorting effect. What this does NOT claim: it does not claim the "
            "encounter happened, does not claim Neptune is innocent, and does not "
            "claim the size distribution is fully measured."),
        "citations": [CIT_JEWITT, CIT_ALLEN],
        "demo_params": {"observed_beyond": 0.0, "expected_beyond": 14.0, "cliff_au": 48.0},
    },
    {
        "key": "uhecr",
        "name": "What Accelerates Ultra-High-Energy Cosmic Rays",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Particles arrive from space carrying 10 million times the energy "
                    "of the Large Hadron Collider's best shots. No known object should "
                    "be able to accelerate them - yet they arrive."),
        "background": (
            "Cosmic rays were discovered in 1912, but the ultra-high-energy tail - "
            "above 10^19 electron volts - remains mysterious. In 1966 Greisen, "
            "Zatsepin, and Kuzmin predicted that such particles cannot travel far: "
            "they collide with cosmic microwave background photons and lose energy, "
            "so their sources must lie within about 50 megaparsecs. The Pierre Auger "
            "Observatory and the Telescope Array have mapped thousands of these "
            "events and confirmed the predicted cutoff, yet no definitive source "
            "class has emerged. Hints point at active galactic nuclei and starburst "
            "galaxies, but the sky distribution is frustratingly blurry - partly "
            "because magnetic fields bend the particles' paths, and partly because "
            "their composition (protons versus heavier nuclei) is still debated. In "
            "2023 the Telescope Array caught the 244-EeV Amaterasu particle from an "
            "apparently empty region of sky."),
        "why_it_matters": (
            "These particles are nature's own supercolliders, reaching energies no "
            "human machine will ever touch. Their accelerators must be the most "
            "extreme engines in the universe - finding them would reveal new physics "
            "of magnetic acceleration. They also probe intergalactic magnetic fields "
            "and the composition of matter at the highest energies."),
        "sig_pointer": (
            "The Signature edition walks the GZK horizon calculation: interaction "
            "length, energy loss, and the source-distance budget that every "
            "candidate accelerator must satisfy."),
        "sig_solution": (
            "Assumptions: the GZK energy-loss physics is correct and the measured "
            "energy scale is accurate to within the experiments' systematics. "
            "Reasoning: the horizon argument turns the whole problem into a distance "
            "budget - any proposed source beyond about 50 Mpc for protons is "
            "automatically disqualified, which radically shortens the suspect list. "
            "Proposed method: compute the GZK horizon for protons and for iron "
            "nuclei separately, catalog every candidate accelerator class inside "
            "each horizon, and score them by whether their power output can supply "
            "the observed flux - a Hillas-criterion audit of the local universe. "
            "What would confirm a source class: arrival directions correlating with "
            "that class above chance after correcting for magnetic deflection, with "
            "the composition matching. What would kill the nearby-source requirement: "
            "a confirmed heavy-nuclei composition at the highest energies, which "
            "shrinks horizons further and deepens the mystery. What this does NOT "
            "claim: it does not claim AGN are the sources, does not claim the "
            "Amaterasu particle's origin is known, and does not claim magnetic "
            "deflection is modeled correctly."),
        "citations": [CIT_AUGER, CIT_GZK, CIT_AMATERASU],
        "demo_params": {"e_eV": 1.0e20, "horizon_mpc": 50.0},
    },
    {
        "key": "grb-engine",
        "name": "The Central Engines of Gamma-Ray Bursts",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Gamma-ray bursts are the brightest explosions since the Big "
                    "Bang, but what powers them - a newborn black hole or a "
                    "super-magnetic neutron star?"),
        "background": (
            "Discovered by Vela satellites in 1967 and declassified in 1973, GRBs "
            "were shown by the BATSE instrument to come from all over the sky - "
            "proving a cosmological origin. Long bursts (over 2 seconds) are now "
            "tied to the deaths of massive stars, the collapsar model, clinched when "
            "GRB 980425 arrived with supernova 1998bw. Short bursts were tied to "
            "neutron-star mergers by the 2017 gravitational-wave event GW170817 and "
            "its GRB 170817A. But the central engine - the compact object and disk "
            "that actually launches the relativistic jet - remains hidden: both a "
            "newborn black hole swallowing an accretion disk and a millisecond "
            "magnetar can fit many observations. The jet-launching mechanism and how "
            "the jet converts its energy to gamma rays are still debated."),
        "why_it_matters": (
            "GRBs are beacons from the early universe, probes of star formation "
            "across cosmic time, and the birth cries of black holes. Their engines "
            "are the most extreme laboratories for magnetic fields, relativity, and "
            "particle acceleration. Settling the engine question would unify our "
            "picture of stellar death."),
        "sig_pointer": (
            "The Signature edition walks the energy ledger: isotropic energy, beaming "
            "correction, and the true energy budget each engine must supply."),
        "sig_solution": (
            "Assumptions: the measured redshifts and fluences are correct, and jet "
            "breaks in afterglows give reliable opening angles. Reasoning: the "
            "isotropic energies look impossibly large until the beaming correction "
            "is applied - the true budget is what the engine must supply, and the "
            "two engine candidates have different maximum budgets. Proposed method: "
            "for a sample of bursts with measured jet breaks, compute the "
            "beaming-corrected true energy and compare against the maximum extractable "
            "energy of a magnetar (its rotational energy, about 10^52 erg) versus a "
            "black hole plus disk; bursts exceeding the magnetar ceiling require a "
            "black hole. What would confirm the black-hole engine for a burst: "
            "energy exceeding the magnetar ceiling plus a late-time X-ray plateau "
            "inconsistent with magnetar spin-down. What would kill the magnetar "
            "model broadly: a population analysis showing most bursts exceed its "
            "budget. What this does NOT claim: it does not claim every burst uses "
            "the same engine, does not claim jet physics is understood, and does "
            "not claim the beaming angles are precise."),
        "citations": [CIT_KLEBESAD, CIT_WOOSLEY, CIT_ABBOT],
        "demo_params": {"e_iso_erg": 8.8e54, "theta_jet_deg": 5.0},
    },
    {
        "key": "first-stars",
        "name": "The First Stars",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("The first stars formed from pristine hydrogen and helium with no "
                    "heavy elements to cool the gas. Were they monsters hundreds of "
                    "times the Sun's mass - and can we ever see one?"),
        "background": (
            "In the early universe there were no metals - astronomers' term for "
            "elements heavier than helium - so collapsing gas could only cool via "
            "molecular hydrogen, an inefficient coolant. Simulations by Abel, Bryan, "
            "and Norman in 2002 suggested the first star-forming clouds were massive "
            "and hot, producing stars of 100 solar masses or more that lived fast "
            "and died as spectacular supernovae, seeding the universe with the first "
            "metals. Later simulations with more physics found fragmentation could "
            "produce smaller stars too, perhaps tens of solar masses. No Population "
            "III star has ever been observed - the most metal-poor stars known still "
            "contain traces of earlier enrichment. JWST is hunting their supernovae "
            "and their distinctive helium emission lines."),
        "why_it_matters": (
            "The first stars ended the cosmic dark ages, forged the first heavy "
            "elements, and lit up the universe. Every atom in our bodies was shaped "
            "by their legacy. Their masses determine how quickly the universe was "
            "enriched and reionized - the initial conditions for everything that "
            "followed."),
        "sig_pointer": (
            "The Signature edition walks the Jeans-mass calculation: cloud "
            "temperature, cooling physics, and the characteristic mass that falls "
            "out, with adjustable assumptions."),
        "sig_solution": (
            "Assumptions: molecular hydrogen was the only coolant and the "
            "simulation-derived cloud temperatures near 200 K are representative. "
            "Reasoning: the characteristic stellar mass follows from the Jeans "
            "mass at the point where the cloud becomes opaque to its own cooling "
            "radiation - a calculation that can be done on paper and checked "
            "against simulations. Proposed method: compute the Jeans mass for "
            "primordial gas at the H2 cooling floor as a function of density, "
            "identify the fragmentation scale, and compare the predicted mass "
            "range against the nucleosynthetic signatures in the most metal-poor "
            "stars - which record the yields of the supernovae that preceded them. "
            "What would confirm the massive-star picture: metal-poor stars showing "
            "abundance patterns matching pair-instability supernova yields of "
            "150-solar-mass progenitors. What would kill it: JWST finding that the "
            "first galaxies' light requires only ordinary-mass stars, or metal-poor "
            "stars matching low-mass supernova yields. What this does NOT claim: it "
            "does not claim the mass function is known, does not claim fragmentation "
            "is settled, and does not claim any observed star is Population III."),
        "citations": [CIT_ABEL, CIT_HIRANO],
        "demo_params": {"T_K": 200.0, "n_cm3": 1.0e4},
    },
    {
        "key": "smbh-seeds",
        "name": "How Billion-Solar-Mass Black Holes Formed So Early",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Quasars shining less than a billion years after the Big Bang "
                    "are powered by black holes of up to ten billion solar masses. "
                    "How did they grow so big so fast?"),
        "background": (
            "The quasar ULAS J1342+0928, at redshift 7.5, hosts an 800-million-solar-mass "
            "black hole when the universe was under 700 million years old; even more "
            "massive examples are known. A black hole feeding at the Eddington limit "
            "doubles on the Salpeter timescale of about 45 million years, so growing "
            "from a stellar-mass seed of 100 Suns to a billion Suns takes roughly 16 "
            "e-foldings - about 725 million years of uninterrupted maximum feeding, "
            "leaving essentially no margin. Proposed solutions include heavy seeds: "
            "direct-collapse black holes of 10,000 to 100,000 solar masses forming "
            "from pristine gas clouds, runaway mergers in dense star clusters, and "
            "episodes of super-Eddington accretion. JWST keeps finding surprisingly "
            "massive black holes in small early galaxies, sharpening the problem."),
        "why_it_matters": (
            "Supermassive black holes co-evolve with galaxies - their masses track "
            "their host galaxies' properties for reasons still debated. If heavy "
            "seeds were common, black holes may have come first and galaxies grown "
            "around them, inverting the standard story. The answer rewrites the "
            "first chapter of galaxy formation."),
        "sig_pointer": (
            "The Signature edition walks the growth-time arithmetic: doublings "
            "needed, Salpeter time, and the margin against the age of the universe "
            "at redshift 7."),
        "sig_solution": (
            "Assumptions: the quasar black-hole masses from emission-line estimates "
            "are correct within a factor of a few, and the Eddington limit applies "
            "on average. Reasoning: the problem is a race against the clock that can "
            "be quantified exactly - count the doublings, multiply by the Salpeter "
            "time, compare with the age of the universe at the observed redshift. "
            "Proposed method: compute the minimum seed mass required for each "
            "high-redshift quasar under strict Eddington-limited growth, then test "
            "whether any astrophysical seed channel (direct collapse, cluster "
            "runaway) can supply that minimum; where it cannot, quantify the "
            "super-Eddington duty cycle required. What would confirm heavy seeds: "
            "JWST or gravitational-wave detection of an intermediate-mass black hole "
            "population at high redshift with no stellar-seed pathway. What would "
            "kill the crisis framing: revised mass estimates shrinking the "
            "high-redshift monsters by an order of magnitude. What this does NOT "
            "claim: it does not claim direct-collapse black holes exist, does not "
            "claim super-Eddington accretion is sustained, and does not claim the "
            "mass estimates are unbiased."),
        "citations": [CIT_BAÑADOS, CIT_VOLONTERI],
        "demo_params": {"seed_msun": 100.0, "final_msun": 1.0e9, "t_universe_myr": 700.0},
    },
]
