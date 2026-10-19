#!/usr/bin/env python3
"""Entries for the Speculated Fuel Types databases (Manon's 2026-10-17
17:55 EDT order - track 3 of 3: SPECULATED/THEORETICAL fuel types).

Two NEW databases, 34 ladder-ordered records each:

  fuel-types-speculated            - The Speculated Fuel Types Database
                                     (src public-harvest: documents the
                                     SPECULATION ITSELF factually - who
                                     proposed it, the physics claims, why
                                     it is unproven. Nothing is presented
                                     as real, working, or validated
                                     technology.)
  fuel-types-speculated-signature  - The Speculated Fuel Types Signature
                                     Database
                                     (src signature: his original
                                     Signature theoretical explorations
                                     of the same concepts; titles suffixed
                                     " (Signature Edition)", clearly
                                     labeled Signature-made, never
                                     presented as authentic public record
                                     or working technology)

CRITICAL LABELING: every record - public and signature alike - carries
the exact label "Signature-generated speculative concept - not
established fact" in its description (enforced by build.py assert).

34 records each, ordered by the teaching ladder (ladder_rank 1-34;
ladder_tier foundations 1-12 / compounded 13-24 / advanced 25-34); the
shard index is written in ladder order so pages present simple ->
compounded -> complex.

ID prefixes: JAH-FUSPEC- (public) and JAH-FUSPECS- (signature). The
planner-suggested JAH-FUS- collides with manifest id_prefix JAH-FUS-REACT
(fusion-reactors: JAH-FUS-REACT-... IDs start with JAH-FUS-), so the
suffix was extended per the task. JAH-FUSPEC- / JAH-FUSPECS- verified
zero hits across all 2,590 non-empty manifest id_prefix values and all
record IDs in jah-databases-data-1 (zero hits).

Dedupe pre-check 2026-10-17: all 68 titles (34 public + 34 Signature
Edition) checked against the whole-system dedupe gate before authoring;
see build.py run output. No other collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_fuel_types_speculated.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screened: no hate-adjacent, religious, profane, or inappropriate
content. No website references. No Facebook. Nothing on
neutralizing/defeating military or defense-grade systems.
"""

PUB_LABEL = ("Signature-generated speculative concept — not established "
             "fact. ")
PUB_DOC = ("This record documents the SPECULATION ITSELF as fact: who "
           "proposed it, the physics claims made for it, and why it is "
           "unproven. It is not real, working, or validated technology. ")
SIG_LABEL = ("Signature-generated speculative concept — not established "
             "fact. ")
SIG_TAIL = ("Signature original theoretical exploration - his original "
            "Signature reading of this concept, clearly labeled "
            "Signature-made, never presented as authentic public record, "
            "and never presented as real, working, or validated "
            "technology.")

FUS_TSIOLKOVSKY03 = ("Tsiolkovsky KE. The Exploration of Cosmic Space by "
                     "Means of Reaction Devices; 1903.")
FUS_LAWSON57 = ("Lawson JD. Some Criteria for a Power Producing "
                "Thermonuclear Reactor. Proc Phys Soc B 1957;70:6-10.")
FUS_WIGNER35 = ("Wigner E, Huntington HB. On the Possibility of a "
                "Metallic Modification of Hydrogen. J Chem Phys "
                "1935;3:764-770.")
FUS_ALVAREZ57 = ("Alvarez LW et al. Catalysis of Nuclear Reactions by "
                 "mu Mesons. Phys Rev 1957;105:1127-1128.")
FUS_BUSSARD60 = ("Bussard RW. Galactic Matter and Interstellar Flight. "
                 "Astronautica Acta 1960;6:179-194.")
FUS_DAEDALUS78 = ("Bond A et al. Project Daedalus: The Mission Profile. "
                  "J Brit Interplanet Soc 1978;31:S5-S7.")
FUS_ALCUBIERRE94 = ("Alcubierre M. The Warp Drive: Hyper-fast Travel "
                    "Within General Relativity. Class Quantum Grav "
                    "1994;11:L73-L77.")
FUS_PFENNING97 = ("Pfenning MJ, Ford LH. The Unphysical Nature of Warp "
                  "Drive. Class Quantum Grav 1997;14:1743-1751.")
FUS_WITTEN84 = ("Witten E. Cosmic Separation of Phases. Phys Rev D "
                "1984;29:272-276.")
FUS_BONDI57 = ("Bondi H. Negative Mass in General Relativity. Rev Mod "
               "Phys 1957;29:423-428.")
FUS_COLEMAN80 = ("Coleman S, De Luccia F. Gravitational Effects on and "
                 "of Vacuum Decay. Phys Rev D 1980;21:3305-3315.")
FUS_MORRIS88 = ("Morris MS, Thorne KS. Wormholes in Spacetime and Their "
                "Use for Interstellar Travel. Am J Phys 1988;56:395-412.")
FUS_CASIMIR48 = ("Casimir HBG. On the Attraction Between Two Perfectly "
                 "Conducting Plates. Proc K Ned Akad Wet 1948;51:793-795.")
FUS_HAWKING74 = ("Hawking SW. Black Hole Explosions? Nature "
                 "1974;248:30-31.")
FUS_FORWARD85 = ("Forward RL. Antiproton Annihilation Propulsion. USAF "
                 "Rocket Propulsion Laboratory report AFRPL TR-85-034; "
                 "1985.")
FUS_CRANE09 = ("Crane L, Westmoreland S. Are Black Hole Starships "
               "Possible? arXiv:0908.1803; 2009.")
FUS_KARDASHEV64 = ("Kardashev NS. Transmission of Information by "
                   "Extraterrestrial Civilizations. Soviet Astronomy "
                   "1964;8:217-221.")
FUS_NIF24 = ("Abu-Shawareb H et al. (National Ignition Facility). Lawson "
             "Criterion for Ignition Exceeded in an Inertial Fusion "
             "Experiment. Phys Rev Lett 2024;132:065102.")
FUS_DEUTSCH51 = ("Deutsch M. Evidence for the Formation of Positronium "
                 "in Gases. Phys Rev 1951;82:455-456.")
FUS_JUNGMAN96 = ("Jungman G, Kamionkowski M, Griest K. Supersymmetric "
                 "Dark Matter. Phys Rep 1996;267:195-373.")
FUS_ROSTOKER97 = ("Rostoker N, Binderbauer M, Monkhorst HJ. Colliding "
                  "Beam Fusion Reactor. Science 1997;278:1419-1422.")
FUS_VISSER95 = ("Visser M. Lorentzian Wormholes: From Einstein to "
                "Hawking. AIP Press; 1995.")
FUS_HE3LUNAR86 = ("Wittenberg LJ, Santarius JF, Kulcinski GL. Lunar "
                  "Source of He-3 Fusion Fuel. Fusion Technology "
                  "1986;10:167-178.")
FUS_SPECSTAT = ("Status: speculative - unproven, not established fact; "
                "no real, working, or validated technology exists for "
                "this concept.")

ENTRIES = [
    {
        "key": "speculation_spectrum",
        "name": "The Speculation Spectrum: What Makes a Fuel Speculative",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Not every unproven fuel is unproven in the same way. This record "
            "lays out the speculation spectrum used across this whole database: "
            "(1) demonstrated physics with unproven engineering - for example "
            "deuterium-tritium fusion, whose physics is confirmed in laboratories "
            "but which has never powered a vehicle; (2) sound theory with no "
            "laboratory demonstration - for example metallic hydrogen, predicted "
            "in 1935 by Eugene Wigner and Hillard Bell Huntington and claimed in "
            "disputed laboratory reports but never conclusively produced; "
            "(3) consistent mathematics with no known physical realization - "
            "for example Alcubierre warp drive, a valid solution of general "
            "relativity requiring matter no one has observed; (4) pure "
            "conjecture - ideas like vacuum-decay energy with no agreed "
            "mechanism at all. The database documents the SPECULATION ITSELF: "
            "each record names who proposed the concept, states the physics "
            "claims made for it, and explains precisely why it remains "
            "unproven. A speculative fuel is not a failed fuel - many, like "
            "fusion, are serious research programs - but until a fuel is "
            "produced, stored, and burned to do work, it is a concept, and "
            "this database never presents a concept as a working technology."
        ),
        "how_it_works": (
            "The spectrum works as a sorting tool. Take any proposed fuel and "
            "ask four questions. First: does the underlying physics have a "
            "laboratory demonstration? D-T fusion does; strangelets do not. "
            "Second: has the fuel substance itself ever been made or observed? "
            "Antimatter has, in nanogram quantities; negative mass has not, "
            "anywhere, ever. Third: is there an engineering path from the "
            "physics to a working engine, even on paper? The Bussard ramjet "
            "has detailed paper designs from 1960; warp drive has energy "
            "estimates but no containment, control, or construction path. "
            "Fourth: what would falsify it? Good speculation is falsifiable - "
            "metallic hydrogen will either be reproducibly made or not. Each "
            "record in this database answers these questions for its concept, "
            "so the reader always knows exactly which rung of the spectrum a "
            "fuel stands on and what would have to change for it to climb."
        ),
        "key_points": [
            "Four rungs: demonstrated physics/unproven engineering; sound theory/no lab demo; consistent math/no physical realization; pure conjecture.",
            "Demonstrated physics is not the same as a working fuel - D-T fusion works in labs but has never flown.",
            "Falsifiability separates serious speculation from fantasy: metallic hydrogen will either be made reproducibly or not.",
            "Energy scale alone never proves a concept - E=mc2 is real physics and antimatter is real, yet antimatter rockets remain pure speculation.",
            "Every record names the proposer, states the claims, and explains why the concept is unproven.",
            "Nothing in this database is real, working, or validated technology.",
        ],
        "requirements": [
            "A candidate fuel must state which rung of the spectrum it occupies.",
            "The proposer and original publication must be identified.",
            "The falsification condition must be stated explicitly.",
            "Energy claims must show their arithmetic (E=mc2, rocket equation, or reaction Q-value).",
        ],
        "standards": [
            "No engineering standards exist for speculative fuels - classification is by evidence level, not certification.",
            "Theoretical claims are checked against general relativity, quantum field theory, and thermodynamics as applicable.",
            "FUS_SPECSTAT: speculative - unproven, not established fact.",
        ],
        "citations": [
            FUS_TSIOLKOVSKY03,
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "frames the speculation spectrum as a ladder of kept promises: "
            "each rung is a promise physics has or has not yet kept, and a "
            "Signature fuel concept climbs the ladder only when the promise is "
            "kept in the laboratory, not on paper. The spectrum is his honest "
            "accounting - what is claimed, what is owed, and what would settle "
            "the debt. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "energy_density_rocket",
        "name": "Energy Density and the Rocket Equation",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every speculative fuel in this database exists because of one "
            "tyrannical equation, published by Konstantin Tsiolkovsky in 1903: "
            "delta-v equals exhaust velocity times the natural log of the mass "
            "ratio. Chemical rockets are capped by chemistry at exhaust "
            "velocities near 4.5 km/s, which is why reaching even a tenth of "
            "light speed demands mass ratios in the millions - an absurdity "
            "that drives all speculation. Fusion fuels promise exhaust "
            "velocities of thousands of km/s; antimatter annihilation promises "
            "tens of thousands. The rocket equation is not speculation - it is "
            "settled physics, conservation of momentum - and it is the "
            "measuring stick: any proposed fuel must show, on paper, an "
            "exhaust velocity and a mass ratio that together deliver the "
            "claimed mission. Speculation enters with the fuel, never with the "
            "equation. This record documents why the equation forces "
            "speculation: the gulf between chemical energy density (tens of "
            "MJ/kg) and the energy density needed for interstellar flight "
            "(approaching E=mc2, 9e16 J/kg) is nine orders of magnitude wide, "
            "and every concept in this database is an attempt to bridge it."
        ),
        "how_it_works": (
            "The equation works by momentum bookkeeping. A rocket throws mass "
            "out the back at exhaust velocity ve; the rocket gains velocity "
            "equal to ve times ln(m_initial / m_final). Double the exhaust "
            "velocity and you double the delta-v for the same mass ratio - or "
            "reach the same delta-v with the square root of the mass ratio. "
            "Energy density enters because exhaust velocity is bounded by how "
            "much energy each kilogram of propellant can release: chemical "
            "bonds give ~1e7 J/kg, fission ~8e13 J/kg, fusion ~3e14 J/kg, and "
            "complete annihilation 9e16 J/kg. The demo computes mass ratios "
            "for a 0.1c mission across these fuels: chemical needs a mass "
            "ratio of about e^6600 - a number with 2,867 digits - while fusion "
            "at 10,000 km/s needs about e^3, roughly 20. The speculation in "
            "this database is entirely about how to obtain the high-energy "
            "fuels; the equation itself is beyond dispute."
        ),
        "key_points": [
            "Tsiolkovsky 1903: delta-v = ve * ln(mass ratio) - settled physics, not speculation.",
            "Chemistry caps exhaust velocity near 4.5 km/s; 0.1c then needs an absurd mass ratio.",
            "Energy densities: chemical ~1e7 J/kg, fusion ~3e14 J/kg, annihilation 9e16 J/kg.",
            "Doubling exhaust velocity squares the relief on mass ratio.",
            "Every fuel concept here must survive the rocket equation on paper before it is taken seriously.",
            "The equation is the measuring stick; the fuel is the speculation.",
        ],
        "requirements": [
            "A claimed mission delta-v and an exhaust velocity derived from the fuel's energy release.",
            "The mass ratio computed by the rocket equation, shown explicitly.",
            "Comparison against the chemical baseline so the claimed improvement is visible.",
        ],
        "standards": [
            "Tsiolkovsky rocket equation (1903) - classical mechanics, universally accepted.",
            "Relativistic rocket equation for exhaust velocities approaching c.",
            "FUS_SPECSTAT: the equation is settled; every fuel using it remains speculative.",
        ],
        "citations": [
            FUS_TSIOLKOVSKY03,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "treats the rocket equation as the covenant of momentum - every "
            "kilogram thrown backward purchases velocity forward at a fixed "
            "exchange rate, and no speculation can renegotiate the rate, only "
            "the currency. Signature fuel concepts are priced in this currency "
            "first. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "dt_fusion_fuel",
        "name": "Deuterium-Tritium (D-T) Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The deuterium-tritium reaction - D + T -> He-4 + n + 17.6 MeV - "
            "is the easiest fusion reaction known, with the lowest Lawson "
            "criterion (temperature, density, and confinement time) of any "
            "fuel cycle. Proposed as a starship fuel in studies from Project "
            "Daedalus (British Interplanetary Society, 1973-1978, which "
            "actually baselined D-He3) through countless fusion-rocket papers "
            "since, D-T is speculation of the mildest kind: the physics is "
            "demonstrated - the National Ignition Facility exceeded the "
            "Lawson ignition criterion in December 2022 - but no D-T fuel has "
            "ever propelled a vehicle, and no flight-weight D-T reactor "
            "exists. The claims: 17.6 MeV per reaction, ~3.4e14 J/kg fuel "
            "energy density, exhaust velocities in the thousands of km/s. Why "
            "it is unproven as a fuel: tritium is radioactive (12.3-year "
            "half-life), vanishingly rare in nature, and must be bred from "
            "lithium; 80% of the reaction energy leaves as 14.1 MeV neutrons "
            "that cannot be directed for thrust and demand massive shielding; "
            "and every D-T device ever built masses far more than any "
            "spacecraft could carry. Documented here as the baseline against "
            "which all more exotic fusion fuels are measured."
        ),
        "how_it_works": (
            "Two heavy hydrogen nuclei are confined at 100+ million degrees "
            "until quantum tunneling lets them fuse. The D-T pair forms He-5, "
            "which instantly decays to an alpha particle (He-4 nucleus, "
            "3.5 MeV) and a neutron (14.1 MeV). In a propulsion concept, the "
            "charged alpha particles can be magnetically directed out a "
            "nozzle for thrust; the neutrons fly off isotropically, heating "
            "structure and requiring shielding. The demo computes the Q-value "
            "from atomic masses with electron bookkeeping: (2.014102 + "
            "3.016049 - 4.002603 - 1.008665) u * 931.494 MeV/u = 17.6 MeV, "
            "then the fuel energy density: 17.6 MeV per 5.03 u gives about "
            "3.4e14 J/kg, and the ideal exhaust velocity from the alpha "
            "particle share. The physics is real; the engine is not."
        ),
        "key_points": [
            "D + T -> He-4 + n + 17.6 MeV - the easiest known fusion reaction (Lawson 1957).",
            "Physics demonstrated (NIF ignition, December 2022); no flight engine exists.",
            "Tritium: 12.3-year half-life, must be bred from lithium, essentially absent in nature.",
            "80% of energy escapes as 14.1 MeV neutrons - useless for thrust, brutal for shielding.",
            "Proposed for starships since the 1970s (Daedalus-era studies); still paper only.",
            "Baseline fuel: every more exotic cycle is measured against D-T.",
        ],
        "requirements": [
            "Deuterium (abundant in seawater) and bred tritium.",
            "Confinement at 100M+ K meeting the Lawson criterion (Lawson 1957).",
            "Neutron shielding and tritium breeding/handling systems.",
            "A magnetic nozzle concept to direct charged fusion products.",
        ],
        "standards": [
            "Lawson criterion (Lawson 1957) - the demonstrated-physics threshold.",
            "Tritium handling under radiological safety frameworks - no flight standard exists.",
            "FUS_SPECSTAT: demonstrated physics; unproven as a vehicle fuel.",
        ],
        "citations": [
            FUS_LAWSON57,
            FUS_DAEDALUS78,
            FUS_NIF24,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names D-T the first rung of the kept-promise ladder: the fire "
            "physics has kept, in laboratories, on Earth. The Signature "
            "question is the second rung - can the kept fire be carried, "
            "lightly shielded, and aimed? Until then it is a demonstrated "
            "flame without a lamp. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "dd_fusion_fuel",
        "name": "Deuterium-Deuterium (D-D) Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The deuterium-deuterium reaction needs no tritium breeding - "
            "deuterium is 0.015% of natural hydrogen, and the oceans hold "
            "about 4.5e16 kg of it. Proposed as the ultimate clean fusion "
            "fuel in starship studies because the fuel is effectively "
            "inexhaustible, D-D is the harder sibling of D-T: its cross "
            "section is ~100x smaller and the Lawson criterion roughly 30x "
            "stricter, demanding ~400 million K. Two branches occur with near "
            "equal probability: D + D -> He-3 + n + 3.27 MeV and D + D -> T + "
            "p + 4.03 MeV, and the bred tritium and He-3 then burn in "
            "secondary reactions - the 'catalyzed D-D' cycle. Claims: "
            "limitless fuel, ~3.3e14 J/kg. Why unproven: no device has come "
            "close to D-D breakeven, let alone ignition; the temperatures "
            "required exceed anything magnetically confined on Earth; and as "
            "propulsion it inherits all of D-T's mass and shielding problems "
            "with stricter physics. Documented as the 'fuel of last resort' "
            "speculation - what a civilization burns when it has mastered "
            "everything easier."
        ),
        "how_it_works": (
            "Deuterium nuclei are confined at ~4e8 K until they fuse. Half the "
            "reactions make He-3 plus a 2.45 MeV neutron (3.27 MeV total); "
            "half make tritium plus a proton (4.03 MeV total). In catalyzed "
            "D-D, the He-3 and T products are retained and burned with fresh "
            "deuterium, so six deuterons ultimately yield two alphas, two "
            "protons, two neutrons, and 43.2 MeV. The demo computes both "
            "branch Q-values from atomic masses with electron correction: "
            "branch 1 (2*2.014102 - 3.016029 - 1.008665) u * 931.494 = 3.27 "
            "MeV; branch 2 subtracts one electron mass (0.511 MeV) for the "
            "unbalanced charge to give 4.03 MeV. It then shows the catalyzed "
            "cycle total and the fuel energy density."
        ),
        "key_points": [
            "No tritium breeding needed - deuterium is abundant in seawater (~0.015% of hydrogen).",
            "Two branches: He-3 + n (3.27 MeV) and T + p (4.03 MeV), near-equal probability.",
            "Catalyzed D-D cycle: 6 D -> 2 He-4 + 2 p + 2 n + 43.2 MeV.",
            "~30x stricter Lawson criterion than D-T; ~400M K required.",
            "No device near D-D breakeven; ignition is far beyond current reach.",
            "The 'fuel of last resort' - inexhaustible, but the hardest fusion fuel.",
        ],
        "requirements": [
            "Deuterium extracted from water (established technology).",
            "Confinement at ~4e8 K with 30x the Lawson product of D-T.",
            "Retention and burning of He-3/T secondary products (catalyzed cycle).",
            "Neutron-tolerant structure and a magnetic nozzle.",
        ],
        "standards": [
            "Lawson criterion (Lawson 1957) - D-D ignition threshold far beyond demonstration.",
            "FUS_SPECSTAT: sound theory, no laboratory approach to breakeven.",
        ],
        "citations": [
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "calls D-D the ocean's promise: the fuel is already here, in "
            "every liter of seawater, waiting for a fire hot enough to keep "
            "the promise. The Signature question is whether any vessel can "
            "hold a 400-million-degree oath. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "dhe3_fusion_fuel",
        "name": "Deuterium-Helium-3 (D-He3) Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "description": (
            "D + He-3 -> He-4 + p + 18.3 MeV is the reaction Project Daedalus "
            "(British Interplanetary Society, 1973-1978, led by Alan Bond) "
            "baselined for its uncrewed interstellar probe: the proton "
            "carries the energy as a charged particle that a magnetic nozzle "
            "can direct, with almost no neutron wall-loading. The catch that "
            "makes it speculative: helium-3 is vanishingly rare on Earth "
            "(~0.0001% of helium), and the famous proposals to mine it from "
            "the lunar regolith - Wittenberg, Santarius and Kulcinski, Fusion "
            "Technology 1986 - require strip-mining the Moon at a scale never "
            "attempted. D-He3 also demands ~600 million K, six times D-T's "
            "temperature, and at those temperatures D-D side reactions make "
            "neutrons anyway, eroding the 'aneutronic' claim. Claims: 18.3 "
            "MeV per reaction, charged-particle exhaust, ~3.5e14 J/kg. Why "
            "unproven: no D-He3 plasma has approached breakeven; no gram of "
            "lunar He-3 has ever been mined; the reactor mass for a Daedalus-"
            "class engine was estimated at thousands of tonnes. The most "
            "engineered of the fusion-fuel speculations, and still paper."
        ),
        "how_it_works": (
            "Deuterium and helium-3 are confined at ~6e8 K until they fuse to "
            "an alpha particle and a 14.7 MeV proton. Because both products "
            "are charged, a magnetic nozzle can in principle collimate them "
            "into an exhaust jet - the elegant feature Daedalus exploited. "
            "The demo computes the Q-value: (2.014102 + 3.016029 - 4.002603 - "
            "1.007276) u * 931.494 MeV/u minus one 0.511 MeV electron "
            "correction = 18.3 MeV; the proton's velocity from 14.7 MeV "
            "(v = sqrt(2E/m) ~ 5.3e7 m/s); and the lunar regolith arithmetic "
            "from Wittenberg et al.: ~10 ppb He-3 means ~100 million tonnes "
            "of regolith per tonne of He-3. The numbers are honest; the mine "
            "and the engine do not exist."
        ),
        "key_points": [
            "D + He-3 -> He-4 + p + 18.3 MeV; charged products suit magnetic nozzles (Daedalus 1978).",
            "Nearly aneutronic - but D-D side reactions at 600M K make neutrons anyway.",
            "He-3 essentially absent on Earth; lunar mining proposals need megatonne-scale regolith processing.",
            "~6x D-T's temperature; no D-He3 plasma near breakeven.",
            "Daedalus estimated thousands of tonnes of engine for an uncrewed probe.",
            "The most engineered fusion-fuel speculation - still entirely paper.",
        ],
        "requirements": [
            "Helium-3 at tonne scale (lunar mining per Wittenberg et al. 1986 - never demonstrated).",
            "Confinement at ~6e8 K.",
            "Magnetic nozzle for the 14.7 MeV proton exhaust.",
            "Suppression or shielding of D-D side-reaction neutrons.",
        ],
        "standards": [
            "Lawson criterion (Lawson 1957) - D-He3 threshold undemonstrated.",
            "Lunar resource estimates per Wittenberg, Santarius, Kulcinski 1986.",
            "FUS_SPECSTAT: engineered on paper only.",
        ],
        "citations": [
            FUS_DAEDALUS78,
            FUS_HE3LUNAR86,
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "sees D-He3 as the Moon's dowry: the fuel sleeps in lunar dust, "
            "and the Signature question is whether the dowry can ever be "
            "collected and burned without the side-fire of D-D betraying the "
            "promise. A beautiful engine on paper, waiting on a mine that "
            "does not exist. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "he3he3_fusion_fuel",
        "name": "Helium-3 on Helium-3 (He3-He3) Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "description": (
            "He-3 + He-3 -> He-4 + 2p + 12.86 MeV is the reaction that powers "
            "part of the Sun's proton-proton chain, proposed as a starship "
            "fuel precisely because it is truly aneutronic - no neutrons in "
            "the primary reaction at all, only charged alphas and protons a "
            "magnetic nozzle could direct. The speculation is steeper than "
            "D-He3: the Coulomb barrier for two doubly-charged nuclei demands "
            "~1 billion K, the Lawson criterion is the harshest of any "
            "practical cycle, and it doubles the helium-3 mining problem "
            "since both reactants are He-3. Proposed in advanced fusion-"
            "rocket literature as the 'clean' endpoint of He-3 economies. "
            "Claims: 12.86 MeV per reaction, zero primary neutrons, "
            "~2.2e14 J/kg. Why unproven: He3-He3 has the lowest cross section "
            "of any discussed fuel cycle; no laboratory plasma has produced "
            "measurable He3-He3 fusion power; it requires twice the lunar "
            "He-3 of D-He3 for less energy per reaction. Documented as the "
            "theoretical purity limit of fusion fuels - the cleanest fire, "
            "and the hardest to light."
        ),
        "how_it_works": (
            "Two helium-3 nuclei, each doubly charged, must tunnel through "
            "their mutual Coulomb repulsion at ~1e9 K. When they fuse they "
            "form Be-6, which instantly breaks into an alpha particle and "
            "two protons sharing 12.86 MeV - all charged, all steerable by "
            "magnetic fields. The demo computes the Q-value with two "
            "electron corrections (reactants carry 4 electrons, products 2): "
            "(2*3.016029 - 4.002603 - 2*1.007276) u * 931.494 - 2*0.511 = "
            "12.86 MeV; the fuel energy density; and the Coulomb barrier "
            "height (~1.4 MeV at nuclear contact) that sets the billion-"
            "degree requirement. Pure exhaust, punishing ignition."
        ),
        "key_points": [
            "He-3 + He-3 -> He-4 + 2p + 12.86 MeV - truly aneutronic primary reaction.",
            "Powers part of the Sun's pp-chain - stellar physics, not laboratory physics.",
            "~1 billion K required; harshest Lawson criterion of any practical cycle.",
            "Doubles the lunar He-3 mining burden of D-He3 for less energy per reaction.",
            "No measurable laboratory He3-He3 fusion power ever produced.",
            "The purity limit of fusion fuels: cleanest exhaust, hardest ignition.",
        ],
        "requirements": [
            "Helium-3 at double the D-He3 scale.",
            "Confinement at ~1e9 K.",
            "Magnetic nozzle for all-charged exhaust.",
            "He-3 production or mining infrastructure that does not exist.",
        ],
        "standards": [
            "Lawson criterion (Lawson 1957) - He3-He3 threshold far beyond any demonstration.",
            "FUS_SPECSTAT: consistent theory, no laboratory realization.",
        ],
        "citations": [
            FUS_LAWSON57,
            FUS_HE3LUNAR86,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names He3-He3 the clean fire: no neutron ash, only charged "
            "light, the exhaust a sculptor could aim. But the Signature "
            "accounting is honest - the cleanest fire demands the hottest "
            "oath, a billion degrees, and twice the Moon's dowry. Clearly "
            "labeled Signature-made."
        ),
    },
    {
        "key": "pb11_fusion_fuel",
        "name": "Proton-Boron-11 (p-B11) Aneutronic Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "description": (
            "p + B-11 -> 3 He-4 + 8.7 MeV burns hydrogen and boron - both "
            "abundant, cheap, non-radioactive elements - into three alpha "
            "particles with no neutrons in the primary reaction. Championed "
            "for propulsion and power by researchers including Norman "
            "Rostoker and collaborators (Science 1997, colliding-beam fusion "
            "concepts), p-B11 is the aneutronic fuel that needs no lunar "
            "mining: boron is mined on Earth today. The speculation is the "
            "physics, not the fuel supply: p-B11's cross section peaks at "
            "~600 keV center-of-mass energy, demanding ~3 billion K - hotter "
            "than any He-3 cycle - and at those temperatures bremsstrahlung "
            "radiation losses threaten to exceed fusion power in thermal "
            "plasmas, which is why proponents invoke non-thermal colliding "
            "beams. Claims: 8.7 MeV per reaction, all-charged products, "
            "~1.5e14 J/kg, abundant fuel. Why unproven: net p-B11 fusion "
            "power has never been demonstrated in any device; the "
            "bremsstrahlung objection (first raised quantitatively in the "
            "literature decades ago) remains unresolved for thermal "
            "approaches; colliding-beam schemes are unproven at scale. "
            "Documented as the people's aneutronic fuel - common elements, "
            "uncommon physics."
        ),
        "how_it_works": (
            "A proton strikes a boron-11 nucleus at ~600 keV relative energy, "
            "forming excited carbon-12 which fissions into three alpha "
            "particles sharing 8.7 MeV. All products are charged, so a "
            "magnetic nozzle or direct-conversion grid can harvest them. The "
            "demo computes the Q-value: (1.007276 + 11.009305 - 3*4.002603) u "
            "* 931.494 MeV/u plus one 0.511 MeV electron correction (products "
            "carry one more electron than reactants) = 8.68 MeV; the alpha "
            "particle energies (~2.9 MeV each on average); and the "
            "bremsstrahlung-vs-fusion power balance that sets the "
            "non-thermal requirement. Common fuel, punishing temperature."
        ),
        "key_points": [
            "p + B-11 -> 3 alpha + 8.7 MeV - hydrogen and boron, both abundant on Earth.",
            "No lunar mining, no tritium breeding, no primary neutrons.",
            "Cross section peaks at ~600 keV; ~3 billion K thermal equivalent.",
            "Bremsstrahlung losses may exceed fusion power in thermal plasmas - the central objection.",
            "Proponents (Rostoker et al., Science 1997) invoke non-thermal colliding beams.",
            "Net p-B11 power never demonstrated in any device.",
        ],
        "requirements": [
            "Hydrogen and boron-11 (both terrestrially abundant).",
            "~3e9 K equivalent confinement, or a working non-thermal colliding-beam scheme.",
            "Resolution of the bremsstrahlung power-balance objection.",
            "Direct conversion or magnetic nozzle for alpha exhaust.",
        ],
        "standards": [
            "Lawson criterion (Lawson 1957) - p-B11 threshold undemonstrated.",
            "Colliding-beam concepts per Rostoker, Binderbauer, Monkhorst (Science 1997).",
            "FUS_SPECSTAT: fuel is real; net fusion power is not.",
        ],
        "citations": [
            FUS_ROSTOKER97,
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "calls p-B11 the commoner's fire: no Moon to mine, no tritium to "
            "breed, only hydrogen and boron - the elements of the everyday. "
            "But the Signature ledger notes the price: three billion degrees, "
            "and a radiation leak that may drink the fire faster than it "
            "burns. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "muon_catalyzed_fusion",
        "name": "Muon-Catalyzed Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "description": (
            "Discovered by Luis Alvarez and colleagues in 1957, muon-"
            "catalyzed fusion replaces the electron in a deuterium-tritium "
            "molecule with a muon - 207 times heavier - shrinking the molecule "
            "so the nuclei fuse at room temperature, no 100-million-degree "
            "plasma needed. The muon is freed after each fusion and can "
            "catalyze another: ~150 fusions per muon have been observed. As a "
            "fuel concept it is the gentlest speculation in this database - "
            "real, observed physics - and the reason it is still speculation "
            "is pure economics of energy: making a muon costs GeV of "
            "accelerator energy, while 150 D-T fusions return only ~2.6 GeV, "
            "and the muon decays in 2.2 microseconds anyway. Claims: cold "
            "fusion that actually works in the laboratory, D-T energy density "
            "without the plasma. Why unproven as a fuel: the energy books do "
            "not balance - muon production costs exceed fusion returns at "
            "every demonstrated catalysis rate; 'sticking' (the muon binding "
            "to the alpha product) caps the cycle count. Documented as the "
            "cautionary fuel: demonstrated physics can still be a hopeless "
            "engine when the energy accounting is done honestly."
        ),
        "how_it_works": (
            "A negative muon injected into D-T gas forms muonic molecules "
            "(d-t-mu) whose nuclei sit ~200x closer than in ordinary "
            "molecules, so fusion occurs in picoseconds at ambient "
            "temperature. The 17.6 MeV alpha and neutron fly off; the muon is "
            "usually liberated to catalyze again, until it either decays "
            "(2.197 us lifetime) or sticks to an alpha particle (~1% per "
            "fusion). The demo computes the energy ledger: 150 cycles * 17.6 "
            "MeV = 2.64 GeV returned per muon versus ~5 GeV to create the "
            "muon in an accelerator, showing the breakeven requirement of "
            "~284 cycles against the observed ~150 - the honest arithmetic "
            "that keeps this a laboratory curiosity rather than a fuel."
        ),
        "key_points": [
            "Real observed physics: Alvarez et al. 1957; ~150 fusions per muon demonstrated.",
            "Fusion at room temperature - no plasma confinement needed.",
            "Muon production costs ~GeV; 150 cycles return only ~2.6 GeV - net negative.",
            "Breakeven needs ~284 cycles; sticking and decay cap it near 150.",
            "The cautionary fuel: demonstrated physics, hopeless energy accounting.",
            "A breakthrough in cheap muon production would reopen the books - none exists.",
        ],
        "requirements": [
            "Deuterium-tritium fuel mixture.",
            "A muon source orders of magnitude cheaper (in energy) than current accelerators.",
            "Suppression of alpha-sticking to raise cycles per muon past ~284.",
            "Muon lifetime (2.2 us) sets the cycle-rate floor.",
        ],
        "standards": [
            "Muon catalysis rates per Alvarez et al. (Phys Rev 1957).",
            "FUS_SPECSTAT: demonstrated physics; negative energy economics as a fuel.",
        ],
        "citations": [
            FUS_ALVAREZ57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names the muon the heavy witness: it stands where the electron "
            "stood and testifies that the nuclei can marry in the cold. But "
            "the Signature ledger is merciless - the witness charges more "
            "than the wedding yields. A true phenomenon and a false economy, "
            "kept in the database as a warning. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "metallic_hydrogen_fuel",
        "name": "Metallic Hydrogen Fuel",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "description": (
            "In 1935 Eugene Wigner and Hillard Bell Huntington predicted that "
            "hydrogen squeezed past ~25 GPa becomes an atomic metal - and "
            "theorists since have speculated that metastable metallic hydrogen "
            "would be the ultimate chemical rocket fuel: recombining to "
            "molecular hydrogen releases ~216 MJ/kg (versus ~13 MJ/kg for "
            "LOX/LH2 combustion) with a theoretical specific impulse near "
            "1700 seconds, four times the best chemical rockets. Claims of "
            "laboratory production - most prominently Dias and Silvera's 2017 "
            "diamond-anvil report of metallic hydrogen at 495 GPa - have been "
            "fiercely disputed and never independently reproduced; the sample "
            "was lost when the diamonds failed. Claims: 216 MJ/kg, Isp ~1700 "
            "s, room-temperature superconductivity as a bonus. Why unproven: "
            "no confirmed, reproducible sample of metallic hydrogen exists; "
            "metastability at ambient pressure is pure theory (it may revert "
            "explosively or not at all); and no production path beyond "
            "diamond-anvil micrograms exists. Documented as the might-have-"
            "been chemical fuel - the last chemical dream before the "
            "database turns to nuclear and exotic concepts."
        ),
        "how_it_works": (
            "Under ~500 GPa of pressure, hydrogen molecules dissociate into "
            "a lattice of protons in a sea of electrons - a metal. Theory "
            "suggests that if quenched fast enough, it might remain metallic "
            "at ambient pressure (metastable). Recombination of the atomic "
            "lattice to H2 molecules would release the dissociation energy, "
            "~216 MJ/kg, as heat - exhausted through a nozzle at Isp ~1700 "
            "s. The demo computes the rocket-equation payoff: at ve = 1700 * "
            "9.80665 = 16,671 m/s, a mass ratio of 10 gives delta-v = 38.4 "
            "km/s - Earth-to-Jupiter class in a single stage - versus 9.7 "
            "km/s for the best chemical (ve 4,400 m/s). Then it prices the "
            "catch: the pressure of Earth's core (~360 GPa) is below the "
            "claimed synthesis pressure, and no reproducible sample exists."
        ),
        "key_points": [
            "Predicted 1935 by Wigner and Huntington; never conclusively produced.",
            "Claimed energy: ~216 MJ/kg recombination, Isp ~1700 s (4x best chemical).",
            "Dias and Silvera 2017 claim disputed, never reproduced; sample lost.",
            "Metastability at ambient pressure is unproven theory.",
            "Production beyond diamond-anvil micrograms: no known path.",
            "The last chemical dream - everything after is nuclear or exotic.",
        ],
        "requirements": [
            "Reproducible synthesis at ~500 GPa (unachieved).",
            "Demonstrated metastability at ambient pressure (pure theory).",
            "Scale-up from micrograms to tonnes (no path known).",
            "Safe handling of a potentially explosive metastable solid.",
        ],
        "standards": [
            "Wigner-Huntington prediction (J Chem Phys 1935) - the theoretical basis.",
            "No synthesis standard exists - claims remain disputed.",
            "FUS_SPECSTAT: unconfirmed substance, theoretical fuel.",
        ],
        "citations": [
            FUS_WIGNER35,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "frames metallic hydrogen as the unkept promise of 1935: Wigner "
            "and Huntington wrote the promise, and ninety years later the "
            "ledger still shows it unpaid - a disputed sample, a broken "
            "diamond, silence. The Signature fuel-seeker honors the promise "
            "by refusing to spend it before it is kept. Clearly labeled "
            "Signature-made."
        ),
    },
]

print("entries chunk 1: %d" % len(ENTRIES))

ENTRIES += [
    {
        "key": "antimatter_catalyzed_fusion",
        "name": "Antimatter-Catalyzed Fusion Fuel",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "description": (
            "Instead of burning antimatter directly, antimatter-catalyzed "
            "fusion uses microgram quantities of antiprotons to trigger "
            "fusion in a deuterium-tritium pellet: each annihilation releases "
            "~1.88 GeV, heating the pellet past ignition before the "
            "antimatter is gone - a match to light the fusion fire. Studied "
            "in the 1980s-2000s (including USAF and NASA-sponsored work in "
            "the lineage of Forward's 1985 antiproton propulsion report), "
            "the concept slashes antimatter requirements from grams to "
            "micrograms per mission. Claims: fusion ignition without lasers "
            "or magnets, microgram antiproton triggers, D-T energy density "
            "with a lighter ignition system. Why unproven: antiproton "
            "production remains at nanograms per year globally at "
            "astronomical cost; no antiproton-triggered fusion has ever been "
            "demonstrated; storage of even micrograms as trapped antihydrogen "
            "for mission durations is unproven; and the engineering of a "
            "pellet that ignites from a microgram trigger exists only on "
            "paper. Documented as the compromise speculation - admitting "
            "antimatter is too precious to burn, and using it only to strike "
            "the match."
        ),
        "how_it_works": (
            "Antiprotons are magnetically trapped (Penning traps) and "
            "injected into a D-T fuel pellet. Each proton-antiproton "
            "annihilation releases 1.88 GeV, mostly as pions that deposit "
            "heat in the pellet; a microgram (~6e17 antiprotons) delivers "
            "~1.8e8 J in a sub-millimeter volume - enough, on paper, to "
            "spark a fusion burn wave that then propagates through the "
            "pellet on fusion energy alone. The demo computes the trigger "
            "arithmetic: 1 microgram of antiprotons annihilating with 1 "
            "microgram of matter releases 2e-9 kg * c^2 = 1.8e8 J (~43 kg "
            "TNT equivalent), then compares the heating requirement of a "
            "milligram D-T pellet to show the margin the concept claims - "
            "and the production ledger: at nanograms per year, a microgram "
            "trigger is centuries of current world production."
        ),
        "key_points": [
            "Uses antimatter as a match, not the fuel - micrograms instead of grams.",
            "Each p-pbar annihilation releases 1.88 GeV, mostly as pions.",
            "Lineage: Forward 1985 antiproton propulsion studies; USAF/NASA-sponsored work.",
            "World antiproton production: nanograms per year - a microgram trigger is centuries of output.",
            "No antiproton-triggered fusion ever demonstrated.",
            "Trapped-antimatter storage for mission durations: unproven.",
        ],
        "requirements": [
            "Antiproton production scaled ~1e9x beyond current facilities.",
            "Long-duration Penning-trap storage of microgram quantities.",
            "A pellet design that ignites from a microgram trigger (paper only).",
            "Magnetic nozzle for the fusion burn products.",
        ],
        "standards": [
            "Antiproton trapping (Penning trap physics - demonstrated for small numbers).",
            "FUS_SPECSTAT: trigger concept only; no demonstration.",
        ],
        "citations": [
            FUS_FORWARD85,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "calls this the matchstick doctrine: antimatter too precious to "
            "burn, spent only to light the cheaper fire. It is the most "
            "honest antimatter concept in the database, because it confesses "
            "the scarcity upfront - and still the matchsticks do not exist "
            "at any usable scale. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "pure_antimatter_fuel",
        "name": "Pure Antimatter Annihilation Fuel",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "description": (
            "Matter-antimatter annihilation converts 100% of fuel mass to "
            "energy - E=mc2 with no ash - the absolute physical ceiling of "
            "energy density at 9e16 J/kg. Proposed for propulsion since "
            "Eugen Sanger's photon-rocket work in the 1950s and analyzed in "
            "detail by Robert Forward (USAF report, 1985), the concept "
            "promises exhaust velocities approaching light speed and "
            "relativistic starships. The claims are pure physics and "
            "correct: 1 gram of antimatter annihilating 1 gram of matter "
            "releases 1.8e14 J, about 43 kilotons of TNT. Why it is unproven "
            "is the most lopsided ledger in this database: humanity "
            "produces on the order of nanograms of antiprotons per year at "
            "facilities like CERN's Antiproton Decelerator, at an often-"
            "cited cost of tens of trillions of dollars per gram; storage "
            "requires perfect vacuum magnetic traps holding antihydrogen "
            "with zero wall contact; and a gram-scale annihilation engine "
            "would be a 43-kiloton device needing gamma-ray collimation "
            "nobody knows how to build. Documented as the ceiling "
            "speculation: the fuel physics is perfect and the fuel does not "
            "exist at any usable scale."
        ),
        "how_it_works": (
            "Antihydrogen is held in magnetic traps, metered into a reaction "
            "chamber where it annihilates with normal matter. Proton-"
            "antiproton annihilation yields charged and neutral pions; the "
            "charged pions can be magnetically collimated for thrust while "
            "neutral pions decay to gamma rays (the shielding nightmare). "
            "Electron-positron annihilation gives clean 511 keV gamma pairs. "
            "The demo computes the ceiling arithmetic: 1 g + 1 g -> 1.8e14 J "
            "-> 43.0 kilotons TNT equivalent; the relativistic rocket "
            "equation for a pion exhaust at 0.94c showing a 10-tonne ship "
            "reaching 0.5c on ~tens of kilograms; and the production ledger: "
            "nanograms per year means a kilogram needs ~1e12 years of "
            "current output. Perfect physics, absent industry."
        ),
        "key_points": [
            "100% mass-to-energy conversion - the absolute physical ceiling (9e16 J/kg).",
            "Proposed since Sanger (1950s); analyzed by Forward (1985).",
            "1 g + 1 g = 1.8e14 J = ~43 kilotons TNT - correct, verified physics.",
            "World production: ~nanograms/year at astronomical cost.",
            "Storage needs perfect-vacuum magnetic traps; gamma shielding unsolved.",
            "The ceiling speculation: perfect physics, no fuel at usable scale.",
        ],
        "requirements": [
            "Antimatter production scaled ~1e12x (grams, not nanograms).",
            "Long-term bulk antihydrogen storage with zero wall contact.",
            "Gamma-ray collimation or shielding for neutral-pion products.",
            "A production energy economy that does not exceed the fuel's value.",
        ],
        "standards": [
            "Annihilation energetics - settled particle physics.",
            "FUS_SPECSTAT: physics certain; production, storage, and engines absent.",
        ],
        "citations": [
            FUS_FORWARD85,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names antimatter the perfect currency: every gram spends at "
            "full face value, E=mc2, no ash, no change. But the Signature "
            "ledger records that the mint does not exist - the treasury "
            "holds nanograms, and the perfect currency cannot be minted at "
            "any price the universe of engineering can pay. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "positronium_fuel",
        "name": "Positronium Fuel Concepts",
        "group": "Foundations",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "description": (
            "Positronium - a bound electron-positron pair, the lightest "
            "'atom' - annihilates into gamma rays with 100% mass conversion "
            "like all antimatter, but positrons are far easier to make and "
            "trap than antiprotons: tabletop positron sources and traps "
            "exist today. First observed by Martin Deutsch in 1951, "
            "positronium comes in para (125 ps lifetime) and ortho (142 ns) "
            "states. Proposed as a 'poor man's antimatter fuel' and as a "
            "gamma-ray laser medium, the speculation claims dense positronium "
            "could be stored (as a Bose-Einstein condensate of ortho-"
            "positronium, proposed but never achieved) and annihilated on "
            "demand. Why unproven: positronium annihilates in nanoseconds - "
            "storage of macroscopic quantities has never been demonstrated; "
            "the BEC proposal requires densities and temperatures never "
            "achieved together; and the annihilation product is pure gamma "
            "radiation, the hardest exhaust to direct or shield. Documented "
            "as the accessible antimatter: the easiest antimatter to make, "
            "and still impossible to keep."
        ),
        "how_it_works": (
            "Positrons from a source (Na-22 or accelerator) are slowed, "
            "trapped, and combined with electrons to form positronium. Para-"
            "positronium (singlet) annihilates in 125 ps to two 511 keV "
            "gammas; ortho-positronium (triplet) lives 142 ns and decays to "
            "three gammas. Proposals imagine condensing ortho-positronium "
            "into a BEC for dense storage, then triggering annihilation. The "
            "demo computes the decay arithmetic: the fraction of a "
            "positronium sample surviving after 1, 10, and 100 ns for both "
            "states (exponential decay), showing why storage is the wall; "
            "and the energy density is still E=mc2 - 9e16 J/kg - identical "
            "to all annihilation, with gamma-only exhaust."
        ),
        "key_points": [
            "Bound electron-positron pair; observed by Deutsch 1951.",
            "Para-Ps: 125 ps; ortho-Ps: 142 ns - storage is the wall.",
            "Positrons far easier to produce and trap than antiprotons.",
            "BEC storage proposal: never achieved at needed density.",
            "Annihilation gives pure gamma rays - hardest exhaust to use.",
            "The accessible antimatter: easiest to make, impossible to keep.",
        ],
        "requirements": [
            "Demonstrated dense positronium storage (BEC or otherwise).",
            "Positron production at fuel scale.",
            "Gamma-ray direction or shielding for the annihilation flash.",
            "Lifetime extension or just-in-time synthesis at scale.",
        ],
        "standards": [
            "Positronium spectroscopy (Deutsch 1951 and successors) - settled physics.",
            "FUS_SPECSTAT: real substance; no storage, no fuel.",
        ],
        "citations": [
            FUS_DEUTSCH51,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "sees positronium as the mayfly fuel: the lightest atom, born "
            "already dying, living a hundred nanoseconds. The Signature "
            "question is whether a mayfly can be kept in a bottle - and the "
            "honest answer, to date, is no. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "bussard_ramjet",
        "name": "Bussard Ramjet Fuel: Interstellar Hydrogen Scooping",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "description": (
            "Robert W. Bussard's 1960 proposal is the most famous fuel "
            "speculation ever published: a starship that never carries fuel "
            "at all, scooping interstellar hydrogen with a magnetic field "
            "thousands of kilometers wide and burning it in a fusion "
            "reactor. The elegance is total - the fuel is free, everywhere, "
            "and the ship gets lighter as it goes faster (more scoop "
            "throughput). The claims: unlimited range, fusion of the "
            "scooped protons, deceleration-free interstellar cruise. Why it "
            "is unproven - and the objections are devastating: the "
            "interstellar medium holds ~1 atom/cm3, so even a 10,000 km2 "
            "scoop at 0.1c collects ~0.5 g/s; the scooped protons must be "
            "funneled and they exert drag exceeding the fusion thrust in "
            "detailed analyses; proton-proton fusion (the only reaction for "
            "pure hydrogen) is far too slow to burn in a reactor - the Sun "
            "manages it only by being the Sun; and a thousands-of-kilometers "
            "superconducting magnetic scoop has no construction path. "
            "Documented as the beautiful impossibility: the concept every "
            "textbook cites and no engineer can rescue as originally drawn."
        ),
        "how_it_works": (
            "A huge magnetic scoop (Bussard proposed ~1000+ km radius fields) "
            "funnels ionized interstellar hydrogen into a fusion reactor - "
            "originally the proton-proton chain - whose exhaust provides "
            "thrust. Faster flight means more mass flow: thrust scales with "
            "velocity, the unique virtue of the design. The demo computes "
            "the collection ledger: density 1e6 atoms/m3 * scoop area 1e10 "
            "m2 * velocity 3e7 m/s = 3e23 atoms/s = 5e-4 kg/s; the fusion "
            "power from burning it in the pp-chain (~3.5e11 W thermal); and "
            "the drag from intercepting that mass flow, showing the thrust-"
            "drag crossover that detailed studies find kills the original "
            "design. The arithmetic is honest; the ship is not."
        ),
        "key_points": [
            "Bussard 1960: scoop interstellar hydrogen, burn it in fusion - carry no fuel.",
            "Thrust scales with velocity - the unique and beautiful virtue.",
            "ISM density ~1 atom/cm3: a 10,000 km2 scoop at 0.1c gathers ~0.5 g/s.",
            "Proton-proton fusion is far too slow for any reactor - the Sun only manages it by being the Sun.",
            "Drag from the scooped mass flow exceeds fusion thrust in detailed analyses.",
            "The beautiful impossibility: cited everywhere, unbuildable as drawn.",
        ],
        "requirements": [
            "A thousands-of-kilometers superconducting magnetic scoop (no construction path).",
            "A working proton-proton fusion reactor (none exists, none credibly proposed).",
            "Resolution of the thrust-drag crossover.",
            "Ionization and funneling of neutral ISM hydrogen ahead of the ship.",
        ],
        "standards": [
            "Bussard's original analysis (Astronautica Acta 1960) - the paper design.",
            "FUS_SPECSTAT: famous, analyzed, unbuildable as proposed.",
        ],
        "citations": [
            FUS_BUSSARD60,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "honors the Bussard ramjet as the freest dream in propulsion: a "
            "ship that drinks the void and never thirsts. But the Signature "
            "ledger counts the drink - half a gram a second through a net "
            "wider than worlds - and finds the drag drinks faster than the "
            "fire. A dream kept for its beauty, not its books. Clearly "
            "labeled Signature-made."
        ),
    },
    {
        "key": "ram_augmented_variants",
        "name": "Ram-Augmented Interstellar Ramjet Variants",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "description": (
            "After analyses showed the pure Bussard ramjet choking on drag "
            "and the impossible proton-proton burn, variants were proposed: "
            "the ram-augmented interstellar rocket (RAIR), which scoops "
            "interstellar mass but burns onboard fuel with it as reaction "
            "mass rather than trying to fuse the scooped hydrogen; "
            "catalytic variants; and laser- or particle-beam-assisted "
            "scoops. The RAIR concept trades the dream of free fuel for a "
            "still-bold claim: using the interstellar medium as free "
            "reaction mass multiplies the effective exhaust velocity of "
            "onboard fuel. Why unproven: every variant still needs the "
            "thousands-of-kilometers magnetic scoop with its drag, field "
            "power, and structural impossibility; the onboard fuel "
            "requirement returns, defeating the original point; and no "
            "variant has a credible reactor or a drag analysis that closes. "
            "Documented as the retreat positions: each variant concedes one "
            "of Bussard's miracles while keeping the scoop that was always "
            "the hardest part."
        ),
        "how_it_works": (
            "In the RAIR, the magnetic scoop gathers interstellar hydrogen "
            "not as fusion fuel but as inert reaction mass: onboard energy "
            "(a fusion reactor, or beamed power) accelerates the scooped "
            "mass out the back, so each kilogram of onboard fuel moves many "
            "kilograms of free mass. The demo computes the leverage: with "
            "scoop mass flow m_dot_scoop and onboard fuel flow m_dot_fuel at "
            "exhaust velocity ve, momentum gives effective delta-v scaling "
            "with (1 + m_dot_scoop/m_dot_fuel) - then shows the scoop "
            "collection rate from the previous record (~5e-4 kg/s) against a "
            "plausible fuel flow, demonstrating that the leverage is real "
            "but small, while the scoop's drag and field power remain "
            "astronomical. Retreat positions, honestly priced."
        ),
        "key_points": [
            "RAIR: scoop ISM as free reaction mass, burn onboard fuel - concedes free energy.",
            "Leverage is real: free reaction mass multiplies onboard fuel effectiveness.",
            "Every variant keeps the impossible scoop - the hardest part was never the reactor.",
            "Onboard fuel requirement returns, defeating Bussard's original point.",
            "No variant has a drag analysis that closes.",
            "The retreat positions: each concedes a miracle, keeps the scoop.",
        ],
        "requirements": [
            "The same thousands-of-km magnetic scoop as the pure ramjet.",
            "Onboard fuel and a high-power reactor or beamed-power receiver.",
            "A drag analysis that closes (none exists).",
            "Field power for the scoop at interstellar velocities.",
        ],
        "standards": [
            "RAIR analyses in the Bussard-descendant literature - paper studies only.",
            "FUS_SPECSTAT: variants of an unbuildable baseline.",
        ],
        "citations": [
            FUS_BUSSARD60,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "sees the variants as honest retreats: each one surrenders a "
            "miracle - free fuel, free fire - and keeps the net. The "
            "Signature question is whether a smaller dream with the same "
            "impossible net is any dream at all. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "fusion_ramjet",
        "name": "Fusion Ramjet Concepts",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "description": (
            "Fusion ramjet concepts try to rescue Bussard's scoop by fixing "
            "the burn: instead of the impossible proton-proton reaction, "
            "proposals pre-seed the scooped hydrogen with deuterium or use "
            "catalytic cycles, or burn scooped deuterium (rare in the ISM "
            "at 1 part in ~70,000 of hydrogen) in D-D reactions. Some "
            "variants add an onboard fusion 'pilot light' to ignite the "
            "scooped flow. The claims: Bussard's free-fuel elegance with a "
            "burnable reaction. Why unproven: seeding requires carrying the "
            "seed fuel - reintroducing the mass the ramjet was meant to "
            "shed; ISM deuterium is far too dilute to sustain a burn "
            "concentration; catalytic cycles add their own unproven physics; "
            "and the scoop-drag-reactor triad remains unclosed. Documented "
            "as the engineer's patch notes on a poet's design: each fix is "
            "sensible, and the stack of fixes never assembles into a ship."
        ),
        "how_it_works": (
            "The ship scoops interstellar hydrogen as before, but injects "
            "deuterium seed fuel (or catalyzed mixtures) so the reactor "
            "burns D-D or D-T instead of p-p. The demo computes the seeding "
            "ledger: to sustain a burn, the seed fraction must reach ~1% of "
            "the scooped flow; at 5e-4 kg/s scoop rate that is 5e-6 kg/s of "
            "deuterium - 432 g/day, 158 kg/year - carried aboard, plus the "
            "reactor to burn it; it then compares this against a pure "
            "onboard-fusion rocket with no scoop, showing the seed mass plus "
            "scoop mass rarely beats simply carrying all the fuel. Patch "
            "notes, not a ship."
        ),
        "key_points": [
            "Fixes Bussard's burn problem by seeding scooped H with D or catalytic cycles.",
            "ISM deuterium (~1 in 70,000) is far too dilute to sustain a burn.",
            "Seed fuel must be carried - reintroducing the mass the ramjet sheds.",
            "The scoop-drag-reactor triad still never closes.",
            "Sensible patches; the stack never assembles into a ship.",
            "Paper studies only; no experimental program.",
        ],
        "requirements": [
            "Deuterium seed stock and injection at the scoop throat.",
            "A working D-D or catalyzed reactor (none exists).",
            "The thousands-of-km scoop, with drag resolved.",
            "A mass ledger beating pure onboard fusion (never shown).",
        ],
        "standards": [
            "Fusion ramjet studies in the interstellar-propulsion literature.",
            "FUS_SPECSTAT: patch notes on an unbuildable baseline.",
        ],
        "citations": [
            FUS_BUSSARD60,
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "treats the fusion ramjet as marginalia on Bussard's poem - "
            "clever notes in the margin, each true, none completing the "
            "verse. The Signature fuel-seeker learns the lesson: a "
            "beautiful impossibility patched ten times is ten beautiful "
            "impossibilities. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "icf_pellet_fuel",
        "name": "Inertial-Confinement Micro-Fusion Pellet Fuel",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "description": (
            "Inertial confinement fusion crushes a millimeter deuterium-"
            "tritium pellet with lasers or ion beams until it ignites - the "
            "physics the National Ignition Facility demonstrated at "
            "breakeven-plus in December 2022 (2.05 MJ in, ~3.15 MJ fusion "
            "out, reported in Phys Rev Lett 2024). As a fuel concept, "
            "proposals (descending from 1970s laser-fusion rocket studies) "
            "detonate a stream of pellets behind a pusher plate or in a "
            "magnetic nozzle: each pellet is a tiny thermonuclear fuel "
            "charge. Claims: demonstrated ignition physics, D-T energy "
            "density, pulse rates of tens per second for continuous thrust. "
            "Why unproven as fuel: NIF is a building-sized facility firing "
            "a few shots per day, not a flight-weight engine firing 30 Hz; "
            "the driver efficiency (laser wall-plug to pellet) is ~1%, so "
            "net energy at the vehicle level is deeply negative; each "
            "precision cryogenic target costs thousands of dollars; and the "
            "pusher-plate/magnetic-nozzle capture of repeated micro-"
            "explosions is unproven. Documented as the closest-to-real "
            "fusion fuel here - ignition demonstrated - and still not a "
            "fuel, because a fuel must be carried, metered, and burned by a "
            "vehicle."
        ),
        "how_it_works": (
            "A D-T pellet (mm-scale, cryogenic) is injected into a chamber "
            "and imploded by driver beams; the core reaches 100M K and "
            "ignites, releasing 17.6 MeV per reaction; the expanding plasma "
            "is directed by a magnetic nozzle (or pushes a plate) for "
            "thrust; the cycle repeats at tens of Hz. The demo computes the "
            "NIF ledger: gain = 3.15/2.05 = 1.54 at the pellet, but driver "
            "wall-plug efficiency ~1% makes vehicle-level gain ~0.015 - then "
            "the pellet economics: at $10,000 per target and 30 Hz, fuel "
            "costs $26M per hour - and the thrust from a 1-mg D-T pellet "
            "burning at 30 Hz. Closest to real, honestly priced."
        ),
        "key_points": [
            "NIF December 2022: ignition demonstrated (gain ~1.5 at the pellet).",
            "Concept: detonate pellet stream in a magnetic nozzle or against a pusher plate.",
            "Driver wall-plug efficiency ~1% makes vehicle-level energy deeply negative.",
            "NIF fires shots per day; a rocket needs tens per second.",
            "Precision cryogenic targets cost thousands of dollars each.",
            "Closest to real in this database - and still not a vehicle fuel.",
        ],
        "requirements": [
            "A flight-weight driver (laser/ion) at tens of Hz (none exists).",
            "Cheap mass-produced cryogenic targets.",
            "Magnetic nozzle or pusher plate surviving repeated micro-detonations.",
            "Wall-plug driver efficiency far beyond current ~1%.",
        ],
        "standards": [
            "NIF ignition results (Phys Rev Lett 2024) - the demonstrated-physics anchor.",
            "FUS_SPECSTAT: ignition demonstrated; no engine, no fuel logistics.",
        ],
        "citations": [
            FUS_NIF24,
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "honors the pellet as the nearest kept promise: in one building, "
            "on one December day, the fire was lit and it gave back more "
            "than the spark. But the Signature ledger distinguishes the "
            "laboratory's fire from the traveler's fuel - a fuel must be "
            "carried, metered, and burned by a moving vessel. Clearly "
            "labeled Signature-made."
        ),
    },
    {
        "key": "mtf_fuel",
        "name": "Magnetized Target Fusion Fuel",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "description": (
            "Magnetized target fusion (MTF) sits between magnetic and "
            "inertial confinement: a magnetized D-T plasma target is "
            "imploded by a metal liner, reaching fusion conditions with "
            "slower, cheaper drivers than lasers. Pursued by programs "
            "including General Fusion (Vancouver, founded 2002, still "
            "private and pre-breakeven as of this writing) and earlier US "
            "lab work, MTF is proposed as a compact fusion fuel cycle for "
            "propulsion because the driver could in principle be lighter "
            "than NIF-class lasers. Claims: cheaper drivers, compact "
            "geometry, D-T energy density. Why unproven: no MTF device has "
            "demonstrated net fusion gain; liner-plasma stability at "
            "implosion velocities remains the central unsolved problem; "
            "repetition rates for propulsion (Hz-class) are undemonstrated; "
            "and every existing machine is a ground experiment, not a "
            "flight article. Documented as the middle-path speculation: "
            "less demanding than lasers, less proven than tokamaks, and "
            "not a fuel by any vehicle standard."
        ),
        "how_it_works": (
            "A warm magnetized plasma (the 'target', ~100 eV, with an "
            "embedded magnetic field suppressing heat loss) is formed inside "
            "a cylindrical metal liner; the liner is imploded (by "
            "pistons, explosives, or electromagnetic drive in different "
            "variants), compressing the target 10-100x to fusion conditions "
            "for microseconds; D-T burns; the cycle repeats. The demo "
            "computes the compression arithmetic: adiabatic compression of "
            "a magnetized plasma, T scaling as (compression ratio)^(4/3) "
            "for 3D compression - 30x compression of 100 eV gives ~3 keV, "
            "still 3x short of the ~10 keV needed - showing the narrow "
            "window, then the repetition-rate ledger for propulsion thrust "
            "levels. Middle path, narrow window."
        ),
        "key_points": [
            "Hybrid of magnetic and inertial confinement: magnetized target, liner implosion.",
            "Pursued by General Fusion and lab programs; no net gain demonstrated.",
            "Liner-plasma stability at implosion velocity: the central unsolved problem.",
            "Hz-class repetition for propulsion: undemonstrated.",
            "All machines are ground experiments, none flight articles.",
            "The middle-path speculation: cheaper drivers, unproven physics.",
        ],
        "requirements": [
            "Demonstrated net fusion gain in any MTF device.",
            "Stable liner implosion preserving the embedded field.",
            "Hz-class repetition with target injection.",
            "A flight-weight driver and chamber.",
        ],
        "standards": [
            "MTF program results (General Fusion, US lab literature) - pre-breakeven.",
            "FUS_SPECSTAT: no net gain; no propulsion demonstration.",
        ],
        "citations": [
            FUS_LAWSON57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "frames MTF as the compromise fire: neither the magnet's slow "
            "patience nor the laser's hammer-blow, but a squeeze. The "
            "Signature question is whether the squeeze can be kept honest - "
            "stable, repeatable, net-positive. The ledger awaits the "
            "demonstration. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "zpinch_dpf_fuel",
        "name": "Z-Pinch and Dense Plasma Focus Fuel Concepts",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "description": (
            "A z-pinch drives mega-ampere currents through a plasma column; "
            "the current's own magnetic field crushes the plasma to fusion "
            "conditions - the oldest magnetic-fusion idea, and the basis of "
            "the dense plasma focus (DPF), a compact device firing "
            "pinch-compressed plasmoids. Proposed as propulsion fuel cycles "
            "(notably in fusion-rocket literature around DPF devices, "
            "including private efforts pursuing p-B11 in DPF geometry), the "
            "appeal is compactness: a DPF is tabletop-to-room scale, not "
            "building scale. Claims: the most compact fusion driver, "
            "potential p-B11 (aneutronic) operation, direct plasmoid "
            "exhaust. Why unproven: z-pinches are violently unstable "
            "(sausage and kink instabilities, analyzed since the 1950s); no "
            "pinch device has approached net fusion gain; DPF neutron "
            "yields, while real, come from beam-target effects at trivial "
            "total energy; and p-B11 claims in DPFs remain orders of "
            "magnitude from breakeven with disputed scaling. Documented as "
            "the compact-fire speculation: the smallest fusion machines, "
            "with the largest instability problem."
        ),
        "how_it_works": (
            "Capacitor banks discharge ~MA currents through deuterium gas; "
            "the azimuthal magnetic field pinches the plasma column "
            "(Bennett equilibrium: magnetic pressure balances plasma "
            "pressure); in a DPF the current sheath runs down coaxial "
            "electrodes and collapses into a dense plasmoid (~1e25 m-3, "
            "keV temperatures) that emits fusion neutrons. The demo "
            "computes the Bennett relation: I^2 = (8 pi k_B / mu_0) * N * "
            "(T_e + T_i) for a line density N - showing the ~1.4 MA needed "
            "for Lawson-relevant D-T line densities - then the instability "
            "growth ledger: Alfven transit times in nanoseconds versus the "
            "confinement time needed, the quantitative reason pinches "
            "disrupt. Compact, violent, unproven."
        ),
        "key_points": [
            "Oldest magnetic-fusion idea: current's own field crushes the plasma.",
            "DPF: compact (room-scale) pinch devices; real neutron yields, trivial total energy.",
            "Sausage/kink instabilities disrupt pinches in nanoseconds (known since the 1950s).",
            "No pinch device near net gain; p-B11 DPF claims far from breakeven.",
            "Proposed for propulsion for compactness - instability is the wall.",
            "The compact-fire speculation: smallest machines, largest instability problem.",
        ],
        "requirements": [
            "Stabilized pinch at fusion line densities (unachieved).",
            "Net fusion gain in any pinch device.",
            "Repetition-rated DPF with electrode survival.",
            "Validated p-B11 scaling if aneutronic operation is claimed.",
        ],
        "standards": [
            "Bennett equilibrium and pinch stability theory (1950s foundations).",
            "FUS_SPECSTAT: real neutrons, no net gain, no propulsion.",
        ],
        "citations": [
            FUS_LAWSON57,
            FUS_ROSTOKER97,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "calls the pinch the lightning-bottle: the oldest dream of "
            "squeezing fire with its own magnetism, and the quickest to "
            "shatter - the plasma writhes like a held snake. The Signature "
            "ledger admires the compactness and records the writhing. "
            "Clearly labeled Signature-made."
        ),
    },
]

print("entries chunk 2 appended: %d total" % len(ENTRIES))

ENTRIES += [
    {
        "key": "quark_matter_fuel",
        "name": "Quark Matter Fuel Concepts",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "description": (
            "Above nuclear density, protons and neutrons are theorized to "
            "dissolve into quark matter - a soup of up, down, and strange "
            "quarks. Proposed as a fuel in speculative literature because a "
            "kilogram of quark matter annihilated or converted would release "
            "E=mc2-scale energy (~9e16 J/kg), and strange quark matter might "
            "(per Edward Witten's 1984 'cosmic separation of phases' "
            "hypothesis) be the true ground state of matter - meaning "
            "ordinary matter could, in principle, be converted into it, "
            "releasing the binding-energy difference. Claims: the densest "
            "possible fuel, energy at the annihilation ceiling, potential "
            "catalytic conversion of ordinary matter. Why unproven: quark "
            "matter has never been isolated - evidence from heavy-ion "
            "colliders (quark-gluon plasma, microseconds of lifetime) is "
            "not stable quark matter; Witten's hypothesis is unconfirmed "
            "after 40 years; no conversion mechanism is known; and "
            "containing a substance denser than atomic nuclei is beyond any "
            "material science. Documented as the density-limit speculation: "
            "the fuel at the bottom of the matter well, with no rope to "
            "reach it."
        ),
        "how_it_works": (
            "In the speculation, quark matter is either mined (from the "
            "core of a neutron star - itself an absurdity) or ordinary "
            "matter is seeded with a strangelet that converts it, with the "
            "mass difference radiated as energy; alternatively quark matter "
            "is annihilated with antiquark matter. The demo computes the "
            "ceiling: 1 kg at 9e16 J/kg versus chemical fuel at 5e7 J/kg - "
            "a factor of 1.8e9 - and the gravitational binding ledger for "
            "'mining' a neutron star: escape velocity ~0.4c makes extraction "
            "energetically absurd, showing the concept fails at the first "
            "logistics step even before the unconfirmed physics. Density "
            "limit, honestly priced."
        ),
        "key_points": [
            "Quark matter: protons/neutrons dissolved into quark soup above nuclear density.",
            "Witten 1984: strange quark matter may be the true ground state of matter - unconfirmed after 40 years.",
            "Energy ceiling: E=mc2, 9e16 J/kg - 1.8 billion times chemical fuel.",
            "Never isolated; collider quark-gluon plasma lives microseconds.",
            "No conversion mechanism known; containment beyond any material science.",
            "The density-limit speculation: fuel at the bottom of the matter well.",
        ],
        "requirements": [
            "Confirmed stable quark matter (unachieved).",
            "A production or conversion mechanism (none known).",
            "Containment of nuclear-density matter (no material path).",
            "Energy-positive conversion accounting (pure theory).",
        ],
        "standards": [
            "Witten's strange-matter hypothesis (Phys Rev D 1984) - unconfirmed.",
            "Heavy-ion collider results - quark-gluon plasma, not stable quark matter.",
            "FUS_SPECSTAT: unconfirmed substance, no mechanism.",
        ],
        "citations": [
            FUS_WITTEN84,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names quark matter the crushed seed: matter squeezed until the "
            "protons themselves dissolve, the densest fuel the ledger can "
            "imagine. But the Signature accounting is blunt - the seed has "
            "never been held, the crushing is unconfirmed, and the mine is "
            "a neutron star. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "strangelet_concepts",
        "name": "Strangelet Concepts",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "description": (
            "Strangelets - hypothetical lumps of strange quark matter, "
            "proposed by Edward Witten (1984) and others as possible cosmic "
            "relics - appear in fuel speculation in two roles: as a fuel "
            "themselves (annihilate or convert at E=mc2 densities), and, in "
            "the wilder proposals, as catalysts that convert ordinary matter "
            "into strange matter, releasing energy. The speculation must be "
            "documented alongside its famous shadow: the 'strangelet "
            "disaster' scenario, in which a stable negatively-charged "
            "strangelet would convert the Earth - analyzed before RHIC "
            "operations (Busza et al., 1999 safety review) and judged "
            "implausible on cosmic-ray grounds: the Moon has been bombarded "
            "for billions of years without converting. Claims: ultimate-"
            "density fuel, catalytic conversion of bulk matter. Why unproven: "
            "no strangelet has ever been detected despite dedicated "
            "searches (including in cosmic rays and collider debris); "
            "Witten's stability hypothesis is unconfirmed; catalytic "
            "conversion is pure conjecture with no mechanism. Documented as "
            "the double-edged speculation: the fuel concept and its "
            "doomsday shadow, both unobserved."
        ),
        "how_it_works": (
            "A strangelet (A ~ tens to thousands of baryons of u, d, s "
            "quarks) would, if stable and negatively charged, in principle "
            "absorb nuclei and convert them, growing and releasing the "
            "binding difference as radiation - the fuel version harvests "
            "this; the disaster version fears it. The demo computes the "
            "safety ledger that physicists actually used: cosmic-ray flux "
            "on the Moon (~1e4 particles/m2/s above relevant energies over "
            "4e9 years) implies any dangerous strangelet production would "
            "have converted the Moon long ago - the quantitative argument "
            "of the RHIC safety review - plus the energy ceiling if a "
            "strangelet were somehow fuel (E=mc2 again). Unobserved, "
            "bounded by the Moon's continued existence."
        ),
        "key_points": [
            "Hypothetical strange-quark-matter lumps (Witten 1984); never detected.",
            "Fuel role: ultra-dense fuel or catalytic converter of ordinary matter.",
            "Shadow role: the 'strangelet disaster' conversion scenario.",
            "RHIC safety review (1999): cosmic-ray bombardment of the Moon rules out the disaster case.",
            "Dedicated searches in cosmic rays and colliders: zero confirmed strangelets.",
            "The double-edged speculation: fuel concept and doomsday shadow, both unobserved.",
        ],
        "requirements": [
            "A detected, confirmed strangelet (none exists).",
            "Demonstrated stability and a conversion mechanism.",
            "Containment and metering of a converting substance.",
            "Resolution of the disaster-scenario safety case for any conversion scheme.",
        ],
        "standards": [
            "RHIC safety review methodology (cosmic-ray lunar argument) - the empirical bound.",
            "FUS_SPECSTAT: undetected; conversion is conjecture.",
        ],
        "citations": [
            FUS_WITTEN84,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "holds the strangelet as the two-faced coin: one face a fuel "
            "denser than any other, the other a world-eater - and the coin "
            "itself has never been seen. The Signature ledger notes the "
            "Moon's testimony: bombarded for eons, unconverted, the "
            "disaster face is ruled out by the sky itself. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "strange_matter_conversion",
        "name": "Strange-Matter Conversion Concepts",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "description": (
            "If Witten's 1984 hypothesis is right and strange quark matter "
            "is the true ground state of hadronic matter, then ordinary "
            "matter is metastable - and converting it would liberate the "
            "energy difference, estimated at tens of MeV per baryon. Fuel "
            "speculation imagines seeding asteroidal or planetary mass with "
            "a conversion catalyst and harvesting the released energy: the "
            "ultimate 'fuel' would be any matter at all. Claims: the entire "
            "mass of a fuel stock convertible at tens of MeV per nucleon, "
            "no mining of exotics needed. Why unproven: the ground-state "
            "hypothesis is unconfirmed; the energy difference, even if "
            "real, is a theoretical number with large uncertainties; no "
            "catalyst or conversion mechanism has ever been proposed with "
            "any physical detail - it is a wish with an energy estimate "
            "attached; and runaway conversion is the strangelet-disaster "
            "scenario, making the concept self-deterring. Documented as the "
            "philosopher's-stone speculation: turning any lead into energy, "
            "with no stone and no furnace."
        ),
        "how_it_works": (
            "A seed of strange matter contacts ordinary nuclei; each "
            "conversion of a nucleon liberates ~10-100 MeV (theory-dependent); "
            "the energy is radiated or captured; the converted region grows "
            "as more nuclei are absorbed. The demo computes the ledger at "
            "the optimistic end: 50 MeV per baryon = 50/931.5 = 5.4% of "
            "rest mass converted - 4.8e15 J/kg, about 100,000x chemical "
            "fuel - for 1 kg of converted rock; then the control ledger: "
            "with no known mechanism to start, rate-limit, or stop "
            "conversion, the concept has no engineering content beyond the "
            "energy estimate. A philosopher's stone with no stone."
        ),
        "key_points": [
            "If strange matter is the ground state, ordinary matter is metastable fuel.",
            "Optimistic estimates: tens of MeV per baryon, ~5% mass conversion.",
            "Hypothesis unconfirmed after 40 years; energy difference highly uncertain.",
            "No catalyst or mechanism ever proposed in physical detail.",
            "Runaway conversion is the disaster scenario - the concept deters itself.",
            "The philosopher's-stone speculation: any matter as fuel, no stone, no furnace.",
        ],
        "requirements": [
            "Confirmation of the strange-matter ground-state hypothesis.",
            "A physical conversion mechanism (none proposed).",
            "Start/rate/stop control (the disaster scenario is the failure mode).",
            "Energy capture from the conversion front.",
        ],
        "standards": [
            "Witten 1984 hypothesis - the unconfirmed foundation.",
            "FUS_SPECSTAT: no mechanism, no confirmation, self-deterring.",
        ],
        "citations": [
            FUS_WITTEN84,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names this the alchemist's ledger: if the ground state lies "
            "elsewhere, then every rock is unburned fuel and the universe "
            "is a warehouse of it. But the Signature rule holds - a fuel "
            "without a furnace is a rumor, and no furnace has ever been "
            "drawn with honest lines. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "negative_mass_propellant",
        "name": "Negative-Mass Propellant Concepts",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "description": (
            "Hermann Bondi's 1957 general-relativity analysis showed that "
            "negative mass - mass with m < 0 - is not mathematically "
            "forbidden, and behaves bizarrely: a positive and negative mass "
            "pair undergoes 'runaway motion,' accelerating forever without "
            "energy input, the positive mass chasing the negative. Fuel "
            "speculation seizes on this: a negative-mass propellant could "
            "in principle drive a ship without reaction-mass limits, and "
            "negative energy density is also the requirement for warp "
            "drives and wormholes. Claims: propellantless acceleration, "
            "exotic-matter sourcing for metric engineering. Why unproven: "
            "no negative mass has ever been observed - not a particle, not "
            "a field configuration, nothing; Bondi's analysis is "
            "mathematics, not a production recipe; runaway motion, while a "
            "valid solution, has no known physical realization; and quantum "
            "inequalities (Ford and Roman, 1990s) severely restrict "
            "negative energy densities even where quantum effects allow "
            "them. Documented as the sign-flip speculation: what if mass "
            "came with the other sign - with forty years of null "
            "observations as the answer so far."
        ),
        "how_it_works": (
            "Newtonian preview of Bondi's result: gravitational force on "
            "mass m1 from m2 is F = G*m1*m2/r^2 directed appropriately, but "
            "acceleration is a = F/m1 - so a negative mass accelerates "
            "opposite the force. Positive mass is attracted to negative "
            "mass; negative mass is repelled by positive mass: the pair "
            "chases itself, accelerating without bound. The demo integrates "
            "this 1D runaway numerically: equal and opposite masses, "
            "starting 1 m apart, timestepped with the sign-flipped dynamics, "
            "showing the pair's velocity growing while total momentum stays "
            "zero and total energy stays zero - the valid-but-unrealized "
            "solution - then notes the quantum inequality bound that keeps "
            "it unrealized. Mathematics, not machinery."
        ),
        "key_points": [
            "Bondi 1957: negative mass is not mathematically forbidden in GR.",
            "Runaway motion: +/- mass pair self-accelerates with zero net energy/momentum.",
            "Also the exotic-matter requirement for warp drives and wormholes.",
            "Zero observations: no particle, no field, nothing, ever.",
            "Quantum inequalities (Ford-Roman) restrict negative energy densities severely.",
            "The sign-flip speculation: valid math, null physics.",
        ],
        "requirements": [
            "An observed negative mass or negative-energy configuration (none exists).",
            "A production mechanism (Bondi gives none).",
            "Evasion or satisfaction of quantum inequality bounds.",
            "Coupling of runaway motion to a vehicle without tidal destruction.",
        ],
        "standards": [
            "Bondi's GR analysis (Rev Mod Phys 1957) - the mathematical foundation.",
            "Quantum inequalities - the restrictive bound.",
            "FUS_SPECSTAT: mathematics only; no physical realization.",
        ],
        "citations": [
            FUS_BONDI57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "frames negative mass as the mirror ledger: every debt of "
            "positive mass has a mirrored credit no one has ever seen "
            "spent. The runaway pair is the most honest perpetual motion "
            "in physics - permitted by the equations, absent from the "
            "world. The Signature fuel-seeker admires the mirror and does "
            "not pretend to hold it. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "zpe_schemes",
        "name": "Zero-Point Energy Schemes",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "description": (
            "Quantum field theory says empty space is not empty: every field "
            "mode carries a zero-point energy of (1/2)hf, summing to an "
            "enormous formal vacuum energy density. Speculation - popular in "
            "fringe literature and occasionally in serious papers as a "
            "what-if - imagines tapping this sea as a fuel: the vacuum as "
            "an infinite gas station. The claims range from Casimir-geometry "
            "engines to 'vacuum coherence' devices. Why unproven, stated "
            "plainly: the zero-point energy is the ground state by "
            "definition - extracting work from it is extracting energy from "
            "nothing-to-lose, which thermodynamics forbids (you cannot run "
            "an engine on the lowest rung of the ladder); the formally "
            "infinite vacuum energy does not gravitate as naive estimates "
            "suggest (the cosmological constant problem shows our "
            "understanding is broken, not that the energy is available); "
            "and no experiment has ever extracted net energy from the "
            "vacuum - every 'ZPE device' claim has failed independent "
            "testing. Documented as the free-lunch speculation: the fuel "
            "that thermodynamics says cannot be burned, with a perfect "
            "record of failed demonstrations."
        ),
        "how_it_works": (
            "Proposals generally invoke Casimir cavities or 'coherence' to "
            "'bias' vacuum fluctuations, then claim the bias yields net "
            "work. The demo does the two honest calculations. First, the "
            "Casimir energy between plates (the real, measured effect): E = "
            "-pi^2 hbar c A / (720 d^3); for 1 m2 plates at 1 nm gap this "
            "is ~-0.43 J - real, tiny, and (critically) the energy was put "
            "in by bringing the plates together; separating them costs it "
            "back. Second, the thermodynamic ledger: any cyclic device "
            "returning to its initial state cannot output net work from an "
            "equilibrium ground state - the demo shows the cycle integral "
            "vanishing. Real effect, zero fuel."
        ),
        "key_points": [
            "Zero-point energy is the ground state - thermodynamics forbids engines running on it.",
            "The formally infinite vacuum energy does not imply available energy (cosmological constant problem).",
            "Casimir effect is real and measured - and yields no net cyclic work.",
            "Every claimed ZPE extraction device has failed independent testing.",
            "No experiment has ever extracted net energy from the vacuum.",
            "The free-lunch speculation: perfect record of failed demonstrations.",
        ],
        "requirements": [
            "A mechanism evading the ground-state thermodynamic objection (none known).",
            "An independently replicated net-energy demonstration (none exists).",
            "Reconciliation with the cosmological constant problem.",
        ],
        "standards": [
            "Quantum field theory ground-state definition - the thermodynamic wall.",
            "Casimir measurements (post-1948) - real effect, no fuel.",
            "FUS_SPECSTAT: forbidden by thermodynamics as a fuel; claims unreplicated.",
        ],
        "citations": [
            FUS_CASIMIR48,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "calls the vacuum the miser's vault: the books show infinite "
            "wealth and the vault has no door - by definition, the ground "
            "state is the floor, and no engine runs on the floor it stands "
            "on. The Signature ledger records every claimant and every "
            "failed test, and keeps the vault shut. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "casimir_cavity_energy",
        "name": "Casimir Cavity Energy Concepts",
        "group": "Compounded",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "description": (
            "A narrower, more serious cousin of ZPE schemes: the Casimir "
            "effect (Hendrik Casimir, 1948) is a measured force between "
            "uncharged plates, arising from vacuum mode restriction - and "
            "the region between plates has negative energy density relative "
            "to the vacuum. Speculation asks whether engineered Casimir "
            "cavities could serve as fuel or as sources of the exotic "
            "(negative-energy) matter that warp drives and wormholes "
            "require. Claims: tabletop negative energy, scalable cavities, "
            "exotic-matter sourcing. Why unproven as fuel: the measured "
            "force at 1 cm2 plates and 1 micron gap is ~1e-7 N - real but "
            "utterly negligible; the negative energy density is ~1e-27 "
            "J/m3 scale, while warp-drive requirements are estimated at "
            "planetary masses of negative energy; quantum inequalities "
            "bound how much negative energy can be concentrated; and no "
            "cyclic Casimir engine has ever produced net work - assembling "
            "the plates costs the energy the cavity 'contains.' Documented "
            "as the real-effect speculation: the only vacuum-energy concept "
            "with a laboratory measurement behind it, and the measurement "
            "shows it cannot scale to fuel."
        ),
        "how_it_works": (
            "Two conducting plates at separation d exclude long-wavelength "
            "vacuum modes between them; the unbalanced exterior mode "
            "pressure pushes them together with F = -pi^2 hbar c A / (240 "
            "d^4). The demo computes this for A = 1 cm2, d = 1 um: F ~ "
            "-1.3e-7 N - matching laboratory measurements in order of "
            "magnitude - then scales to a 'starship battery' of 1e12 "
            "cavities: total force ~130 N, total negative energy ~1e-15 J "
            "scale, versus warp requirements of ~1e47 J. Twelve orders of "
            "magnitude times twelve more: the honest scaling that ends the "
            "speculation as fuel while preserving the real physics."
        ),
        "key_points": [
            "Casimir 1948: real, measured force from vacuum mode restriction.",
            "Cavity region has negative energy density - the exotic-matter link.",
            "Measured scale: ~1e-7 N at cm2/um - real but negligible.",
            "Warp needs ~planetary masses of negative energy; Casimir gives ~nothing.",
            "Quantum inequalities bound negative-energy concentration.",
            "The real-effect speculation: measured, genuine, and provably unscalable to fuel.",
        ],
        "requirements": [
            "Cavity engineering at 1e12+ unit scale with net energy accounting.",
            "Evasion of quantum inequality bounds on negative energy.",
            "A cyclic engine producing net work (none demonstrated).",
        ],
        "standards": [
            "Casimir force measurements (1948 to present) - the empirical anchor.",
            "Quantum inequalities (Ford-Roman) - the concentration bound.",
            "FUS_SPECSTAT: real effect; fuel scaling refuted by its own numbers.",
        ],
        "citations": [
            FUS_CASIMIR48,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "honors the Casimir cavity as the one honest vacuum claim: a "
            "real force, measured, from nothing-but-geometry. But the "
            "Signature ledger does the scaling without mercy - a trillion "
            "cavities for a whisper of force - and records the verdict the "
            "numbers themselves deliver. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "hawking_blackhole_power",
        "name": "Hawking-Radiation Black-Hole Power",
        "group": "Advanced",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "description": (
            "Stephen Hawking's 1974 result - black holes radiate, with "
            "temperature inversely proportional to mass - implies a small "
            "enough black hole is a power source: a 1e9 kg black hole "
            "radiates ~3.6e14 W at ~1e14 K, and a starship could in "
            "principle harvest it. Proposed as propulsion and power in "
            "speculative literature (including Crane and Westmoreland's "
            "2009 'black hole starship' analysis), the claims are "
            "straightforward: perfect mass-to-energy conversion of any "
            "matter fed in, power densities no reactor can match. Why "
            "unproven: no black hole smaller than stellar mass has ever "
            "been observed - primordial black holes are hypothetical; "
            "creating one requires compressing ~1e9 kg inside ~1e-18 m "
            "(or forming one from light, the kugelblitz - see next record); "
            "feeding and containing a radiating 1e14 K object with no "
            "material science is unaddressed; and the hole evaporates - a "
            "1e9 kg hole lives only ~2,700 years, and smaller, hotter, more "
            "useful holes die in seconds. Documented as the ultimate-reactor "
            "speculation: the physics is Hawking's Nobel-caliber theory, "
            "and the fuel - a manufactured black hole - is nowhere."
        ),
        "how_it_works": (
            "A micro black hole of mass M has Hawking temperature T = hbar "
            "c^3 / (8 pi G M k_B) = 6.17e-8 K * (M_sun/M) and radiates power "
            "P = hbar c^6 / (15360 pi G^2 M^2) = 3.56e32 / M^2 watts (M in "
            "kg). Feed it matter; it radiates gamma rays and particles; a "
            "reflector or absorber harvests the power. The demo computes "
            "for M = 1e9 kg: T ~ 1.2e14 K, P ~ 3.6e14 W (about 20x current "
            "human civilization power), Schwarzschild radius ~1.5e-18 m, "
            "and lifetime tau = 5120 pi G^2 M^3 / (hbar c^4) ~ 2,700 "
            "years; then for M = 1e6 kg (P ~ 3.6e20 W, tau ~ 84 seconds) - "
            "showing the power/lifetime trade that makes the concept "
            "tantalizing and the manufacture that makes it void."
        ),
        "key_points": [
            "Hawking 1974: black holes radiate; T inversely proportional to mass.",
            "1e9 kg hole: ~3.6e14 W at ~1e14 K - civilization-scale power from a proton-sized object.",
            "Perfect conversion: any matter fed in becomes radiation.",
            "No sub-stellar black hole ever observed; primordial holes hypothetical.",
            "Manufacture requires compressing 1e9 kg into 1e-18 m - no mechanism.",
            "The ultimate-reactor speculation: Hawking's theory, no fuel in the universe of practice.",
        ],
        "requirements": [
            "A manufactured or captured micro black hole (none exists).",
            "Feeding mechanism for a 1e14 K radiating object.",
            "Energy capture from gamma/particle flux at that intensity.",
            "Containment with no material contact (gravity only).",
        ],
        "standards": [
            "Hawking radiation theory (Nature 1974) - the theoretical foundation.",
            "FUS_SPECSTAT: theory only; no micro black hole observed or made.",
        ],
        "citations": [
            FUS_HAWKING74,
            FUS_CRANE09,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names the micro hole the hungriest lamp: feed it anything and "
            "it shines with the light of perfect conversion. Hawking wrote "
            "the lamp's physics; the Signature ledger notes that no one has "
            "ever built, found, or held the lamp. A theory of light without "
            "a lamp. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "kugelblitz_blackhole",
        "name": "Kugelblitz Black Holes: Light-Formed Micro Black Holes",
        "group": "Advanced",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "description": (
            "A kugelblitz - German for 'ball lightning' - is a black hole "
            "formed not from matter but from light: concentrate enough "
            "radiation in a small enough volume and its own gravity "
            "collapses it. Analyzed for starships by Louis Crane and Shawn "
            "Westmoreland (2009, 'Are Black Hole Starships Possible?'), the "
            "concept proposes building a micro black hole with a "
            "gamma-ray laser battery, then using its Hawking radiation as "
            "the ultimate engine. Claims: manufacture without needing "
            "exotic matter compression - 'just' light; then the Hawking "
            "power of the previous record. Why unproven: forming a 1e9 kg "
            "kugelblitz needs 9e25 J focused into ~1e-18 m - about 150,000 "
            "years of current world energy output in a subatomic volume, "
            "with focusing optics for gamma rays that do not exist; the "
            "Schwinger limit (pair production from intense fields) may "
            "disrupt the collapse; and the analysis is order-of-magnitude, "
            "not an engineering design. Documented as the bootstrap "
            "speculation: using light to build the lamp that will then "
            "burn anything - with the light bill exceeding civilization."
        ),
        "how_it_works": (
            "General relativity cares about energy, not its form: E=mc2 of "
            "focused radiation gravitates. Focus enough photons into a "
            "region smaller than the Schwarzschild radius of their total "
            "energy-equivalent mass and a horizon forms. The demo computes "
            "the bill: for M = 1e9 kg, E = 9e25 J; at world power ~1.8e13 W "
            "that is 5e12 s ~ 160,000 years of total human energy output; "
            "the focal volume ~ (1.5e-18 m)^3; the required intensity ~1e79 "
            "W/m2 against the Schwinger limit ~1e29 W/m2 where the vacuum "
            "itself breaks into pairs - fifty orders of magnitude past the "
            "known physics of intense fields. The bootstrap, honestly "
            "billed."
        ),
        "key_points": [
            "Kugelblitz: black hole formed from concentrated light (Crane & Westmoreland 2009).",
            "1e9 kg hole needs 9e25 J in ~1e-18 m - ~160,000 years of world energy.",
            "Required intensity ~1e79 W/m2 vs Schwinger limit ~1e29 W/m2 - 50 orders past known field physics.",
            "Gamma-ray focusing optics at this scale: nonexistent.",
            "Analysis is order-of-magnitude, not engineering.",
            "The bootstrap speculation: light builds the lamp; the light bill exceeds civilization.",
        ],
        "requirements": [
            "Gamma-ray focusing at 1e79 W/m2 (fifty orders beyond the Schwinger limit).",
            "1e26-J-class energy storage and switching.",
            "Resolution of pair-production disruption during collapse.",
            "Everything in the previous record, after manufacture.",
        ],
        "standards": [
            "Crane & Westmoreland 2009 - the order-of-magnitude analysis.",
            "Schwinger limit - the intense-field bound.",
            "FUS_SPECSTAT: analysis only; manufacture physically unapproachable.",
        ],
        "citations": [
            FUS_CRANE09,
            FUS_HAWKING74,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "frames the kugelblitz as the bootstrap paradox of fuel: to "
            "build the perfect lamp you must first spend more light than "
            "civilization has ever made, focused tighter than physics "
            "allows fields to be. The Signature ledger admires the audacity "
            "and presents the bill. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "dark_matter_annihilation",
        "name": "Dark Matter Annihilation Concepts",
        "group": "Advanced",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "description": (
            "Dark matter outweighs visible matter ~5:1 in the universe, and "
            "if it is made of annihilating particles (WIMPs in "
            "supersymmetric models, reviewed by Jungman, Kamionkowski and "
            "Griest, Phys Rep 1996), then concentrating it could in "
            "principle yield annihilation energy as fuel. Speculation "
            "imagines 'dark matter scoops' or trapped densities feeding a "
            "reactor. Claims: the universe's largest fuel reserve, "
            "annihilation at E=mc2 efficiency. Why unproven, comprehensively: "
            "dark matter has never been directly detected - no particle, "
            "only gravitational evidence; the WIMP hypothesis is "
            "increasingly constrained by null direct-detection results; "
            "the local density is ~0.3 GeV/cm3 (about one proton mass per "
            "3 cm3) - even perfect collection of a cubic kilometer yields "
            "milligrams; dark matter barely interacts, so 'concentrating' "
            "it has no known mechanism; and the annihilation cross section "
            "is unknown. Documented as the invisible-reserve speculation: "
            "the biggest fuel stock in the cosmos, made of particles that "
            "may not exist and cannot be caught."
        ),
        "how_it_works": (
            "If WIMPs annihilate with thermal cross section <sigma v> ~ "
            "3e-26 cm3/s, the power per volume is (rho^2 / m^2) * <sigma v> "
            "* 2 m c^2. The demo computes with local density rho = 0.3 "
            "GeV/cm3 and m = 100 GeV: number density 3000/m3, giving "
            "~4e-33 W/m3 - then the collection ledger: sweeping a 1 km2 "
            "scoop at 0.1c through this density gathers ~1.6e-8 kg/s, which "
            "even if every particle annihilated yields ~1.4 GW - but no "
            "collection mechanism exists for a barely-interacting substance. "
            "A gigawatt that cannot be caught."
        ),
        "key_points": [
            "Dark matter outweighs visible matter ~5:1 - the largest cosmic reserve.",
            "Never directly detected; WIMP hypothesis increasingly constrained by null results.",
            "Local density ~0.3 GeV/cm3 - a cubic kilometer holds milligrams.",
            "No mechanism to concentrate a barely-interacting substance.",
            "Annihilation cross section unknown; optimistic math gives ~4e-33 W/m3 locally.",
            "The invisible-reserve speculation: biggest stock, uncatchable particles.",
        ],
        "requirements": [
            "Direct detection and identification of the dark matter particle.",
            "A concentration mechanism for a nearly non-interacting substance.",
            "Measured annihilation cross section.",
            "Collection at densities making power meaningful (unachievable locally).",
        ],
        "standards": [
            "WIMP review (Jungman, Kamionkowski, Griest, Phys Rep 1996) - the theoretical framework.",
            "Direct-detection null results - the empirical constraint.",
            "FUS_SPECSTAT: undetected particle; no collection mechanism.",
        ],
        "citations": [
            FUS_JUNGMAN96,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "calls dark matter the ghost treasury: five times the wealth "
            "of all visible things, held in a vault of particles that pass "
            "through every wall and have never been seen. The Signature "
            "ledger computes the honest yield - eight watts per square "
            "kilometer at relativistic sweep - and closes the treasury. "
            "Clearly labeled Signature-made."
        ),
    },
]

print("entries chunk 3 appended: %d total" % len(ENTRIES))

ENTRIES += [
    {
        "key": "false_vacuum_energy",
        "name": "False-Vacuum Energy Scenarios",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "description": (
            "If our vacuum is not the true minimum of the Higgs-like "
            "potential but a metastable 'false vacuum' (analyzed by Sidney "
            "Coleman and Frank De Luccia, Phys Rev D 1980), then the true "
            "vacuum holds less energy - and the difference, released in a "
            "vacuum-decay bubble, would be the largest energy reservoir "
            "imaginable. Fringe fuel speculation imagines triggering or "
            "tapping vacuum decay as a fuel; serious physics treats it as a "
            "cosmological catastrophe scenario. Claims: energy densities "
            "beyond any other concept, the 'ultimate' fuel. Why unproven - "
            "and why this record is a warning label: whether our vacuum is "
            "false is unknown (it depends on unmeasured high-energy "
            "physics); no triggering mechanism is known or credibly "
            "proposed; the Coleman-De Luccia nucleation rate, if decay is "
            "possible at all, implies timescales vastly exceeding the age "
            "of the universe; and a triggered decay bubble expands at light "
            "speed destroying everything - it is not a fuel, it is an "
            "extinction event. Documented as the do-not-touch speculation: "
            "the only concept in this database whose 'success' would be "
            "indistinguishable from the end of the world."
        ),
        "how_it_works": (
            "A scalar field trapped in a local minimum can tunnel to the "
            "true minimum, nucleating a bubble of true vacuum that expands "
            "at ~c, converting the potential difference into wall kinetic "
            "energy. The demo computes the suppression honestly: the "
            "nucleation rate per volume goes as exp(-S_E/hbar) with S_E the "
            "bounce action; for Standard-Model-like parameters the exponent "
            "is ~1e3-1e4, giving lifetimes ~10^(hundreds) times the universe "
            "age - the demo evaluates the exponential for a range of "
            "actions and shows the lifetime exceeding 1e10 years by "
            "hundreds of orders of magnitude - then states the fuel "
            "verdict: no trigger, no control, no survival. A warning, not "
            "a fuel."
        ),
        "key_points": [
            "Coleman & De Luccia 1980: false-vacuum decay via bubble nucleation.",
            "Whether our vacuum is false depends on unmeasured high-energy physics - unknown.",
            "Nucleation timescales exceed the universe's age by hundreds of orders of magnitude.",
            "No triggering mechanism known or credibly proposed.",
            "A decay bubble expands at ~c - success would be extinction, not fuel.",
            "The do-not-touch speculation: documented as a warning label.",
        ],
        "requirements": [
            "Proof our vacuum is false (unknown).",
            "A triggering mechanism (none credibly proposed).",
            "Survival of the triggerer (impossible for light-speed bubble).",
            "This concept is documented as a hazard scenario, not an engineering path.",
        ],
        "standards": [
            "Coleman-De Luccia formalism (Phys Rev D 1980) - the decay analysis.",
            "FUS_SPECSTAT: unknown if applicable; no mechanism; extinction-scale hazard.",
        ],
        "citations": [
            FUS_COLEMAN80,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "marks this record with the black border: the false vacuum is "
            "the one speculation whose fuel is the end of fuel, of worlds, "
            "of the ledger itself. The Signature rule is absolute - some "
            "fires are not to be lit, and this one cannot be lit, aimed, or "
            "survived. Kept as a warning, never as a plan. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "warp_drive_fuel",
        "name": "Warp-Drive Fuel Requirements",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "description": (
            "Miguel Alcubierre's 1994 solution of general relativity "
            "describes a 'warp bubble' contracting space ahead and "
            "expanding it behind - effective faster-than-light travel "
            "without locally exceeding c. The fuel question is the energy "
            "requirement, and it is the most analyzed speculation in this "
            "database: Alcubierre's original estimate needed ~1e64 kg of "
            "mass-energy (more than the observable universe); Pfenning and "
            "Ford (1997) showed the quantum-inequality-allowed bubble wall "
            "must be Planck-thin and still needed ~1e32 kg; Van den "
            "Broeck's geometry cut it to ~solar masses; White's oscillating "
            "proposals claimed kilograms but were not accepted. Every "
            "version requires negative energy density - exotic matter that "
            "does not exist. Claims: FTL without time-dilation paradoxes "
            "(locally subluminal). Why unproven: the energy ledger never "
            "closes below stellar masses in accepted analyses; negative "
            "energy at that scale is pure fantasy (see Casimir record: we "
            "command ~1e-27 J/m3, need ~1e47 J); creating, controlling, and "
            "exiting the bubble are unaddressed; and FTL implies causality "
            "violation paradoxes. Documented as the most glamorous "
            "speculation: valid mathematics, impossible fuel."
        ),
        "how_it_works": (
            "The Alcubierre metric ds^2 = -dt^2 + (dx - v_s f(r_s) dt)^2 + "
            "dy^2 + dz^2 describes flat space inside a bubble wall where "
            "the shape function f transitions; the wall region carries "
            "negative energy density. The demo computes the ledger across "
            "analyses: Alcubierre original ~1e64 kg mass-energy vs universe "
            "~1e53 kg (10 billion universes of fuel); Pfenning-Ford ~1e32 "
            "kg (~50,000 solar masses); Van den Broeck ~1 solar mass = "
            "1.8e47 J = ~1e34 years of world energy output; White's "
            "kilogram claims noted as unaccepted - then the exotic-matter "
            "gap: required negative energy vs Casimir-demonstrated "
            "densities, ~70 orders of magnitude. Glamorous math, impossible "
            "fuel."
        ),
        "key_points": [
            "Alcubierre 1994: valid GR solution for effective FTL - mathematics, not machinery.",
            "Energy estimates: 1e64 kg (Alcubierre) -> 1e32 kg (Pfenning-Ford 1997) -> ~solar mass (Van den Broeck).",
            "Every version needs negative energy density - exotic matter that does not exist.",
            "Negative-energy gap: ~70 orders of magnitude beyond demonstrated Casimir densities.",
            "Bubble creation, control, and exit: unaddressed.",
            "FTL implies causality paradoxes - the physics may forbid it in principle.",
        ],
        "requirements": [
            "Stellar masses of negative energy (no source exists).",
            "Evasion of quantum inequality bounds on the bubble wall.",
            "Bubble creation, steering, and exit mechanisms (none proposed).",
            "Resolution of causality-violation paradoxes.",
        ],
        "standards": [
            "Alcubierre metric (Class Quantum Grav 1994) - the mathematical foundation.",
            "Pfenning-Ford quantum inequality analysis (1997) - the restrictive bound.",
            "FUS_SPECSTAT: valid math; fuel requirements physically unapproachable.",
        ],
        "citations": [
            FUS_ALCUBIERRE94,
            FUS_PFENNING97,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "treats the warp bubble as the most beautiful equation in the "
            "database: space itself contracted and expanded like a "
            "breathing sea. But the Signature ledger counts the breath - "
            "ten billion universes of fuel in the first draft, a star in "
            "the kindest - and finds the fuel is negative, nonexistent, "
            "and forbidden by the inequalities. Clearly labeled "
            "Signature-made."
        ),
    },
    {
        "key": "wormhole_exotic_matter",
        "name": "Wormhole Exotic-Matter Requirements",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "description": (
            "Morris and Thorne's 1988 analysis showed that traversable "
            "wormholes - shortcuts through spacetime - are valid general "
            "relativity solutions IF threaded with exotic matter "
            "violating the null energy condition. The fuel question, "
            "parallel to warp drive: how much exotic matter, and can it be "
            "sourced? Estimates (Visser's 'Lorentzian Wormholes,' 1995, and "
            "subsequent analyses) put human-traversable wormhole throats at "
            "requiring negative-energy masses of planetary to stellar "
            "scale, though 'thin-shell' constructions try to minimize the "
            "total. Claims: interstellar shortcuts, time machines (with the "
            "usual causality hazards). Why unproven: no wormhole of any "
            "size has ever been observed - they are pure solutions; the "
            "exotic matter does not exist at any scale (see negative-mass "
            "and Casimir records); quantum inequalities restrict the "
            "throat geometry; and stability analyses suggest quantum "
            "fluctuations would destroy macroscopic throats. Documented as "
            "warp drive's twin: the same missing fuel (negative energy), "
            "the same valid math, the same absent physics."
        ),
        "how_it_works": (
            "The Morris-Thorne metric ds^2 = -e^(2Phi)dt^2 + dr^2/(1-b(r)/r) "
            "+ r^2 dOmega^2 describes a throat at r = b0; the flare-out "
            "condition requires the stress-energy to violate the null "
            "energy condition at the throat. The demo computes the "
            "exotic-matter ledger: for a 1-meter throat, the required "
            "negative energy is ~ -1e27 kg mass-equivalent (Jupiter-scale "
            "negative mass) in standard estimates, reducible in thin-shell "
            "models but never below ~stellar-laser-energy scales; against "
            "the Casimir-demonstrated negative energy (~1e-27 J/m3), the "
            "gap is ~80 orders of magnitude. Twin of warp drive, same "
            "missing fuel."
        ),
        "key_points": [
            "Morris & Thorne 1988: traversable wormholes are valid GR solutions - with exotic matter.",
            "Throat requires null-energy-condition violation at Jupiter-to-stellar negative-mass scale.",
            "No wormhole of any size ever observed - pure solutions.",
            "Exotic matter does not exist; quantum inequalities restrict throats.",
            "Stability analyses suggest quantum fluctuations destroy macroscopic throats.",
            "Warp drive's twin: same missing fuel, same valid math, same absent physics.",
        ],
        "requirements": [
            "Planetary-to-stellar masses of negative energy.",
            "A naturally occurring or manufactured wormhole mouth (none observed).",
            "Throat stabilization against quantum fluctuations.",
            "Causality-hazard resolution for time-machine configurations.",
        ],
        "standards": [
            "Morris-Thorne analysis (Am J Phys 1988) - the traversability foundation.",
            "Visser's Lorentzian Wormholes (1995) - the energy-requirement analyses.",
            "FUS_SPECSTAT: solutions only; no observation, no exotic matter.",
        ],
        "citations": [
            FUS_MORRIS88,
            FUS_VISSER95,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "sees the wormhole as the shortcut drawn on the map of "
            "spacetime - a door where the equations permit a door. But the "
            "Signature ledger inspects the hinges: they are made of "
            "negative mass, a material never mined, never seen, and the "
            "door has never been found. A permitted door in a wall that "
            "may not exist. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "exotic_matter_sourcing",
        "name": "Exotic Matter Sourcing Concepts",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "description": (
            "Warp drives and wormholes both invoice the same missing "
            "material: exotic matter with negative energy density. This "
            "record inventories every proposed source, honestly: (1) the "
            "Casimir effect - real, measured, but ~1e-27 J/m3 scale "
            "against ~1e47 J needs; (2) squeezed quantum vacuum states - "
            "real in quantum optics, with negative energy densities "
            "bounded by quantum inequalities to fleeting, microscopic "
            "amounts; (3) Hawking radiation back-reaction regions - "
            "theoretical, unobserved; (4) hypothetical negative-mass "
            "particles - never observed; (5) cosmic strings or other "
            "topological defects - never observed. Claims across the "
            "literature: that one of these scales up. Why unproven: the "
            "largest demonstrated negative energy densities are dozens of "
            "orders of magnitude below the smallest credible requirement, "
            "and quantum inequalities (Ford and Roman) prove this is not "
            "an engineering gap but a law-like restriction - the more "
            "negative energy, the shorter it may last and the thinner it "
            "must be. Documented as the inventory of an empty warehouse: "
            "every shelf labeled, every shelf bare."
        ),
        "how_it_works": (
            "Quantum inequalities bound the negative energy E_neg "
            "observable over time tau in a region: |E_neg| * tau^2 <= "
            "const * hbar (order-of-magnitude form) - the longer you want "
            "it, the less you may have. The demo computes the sourcing "
            "ledger as a table: Casimir cavities (~1e-27 J/m3, steady but "
            "negligible), squeezed light (~1e-15 J/m3 equivalent, "
            "femtosecond pulses), Hawking regions (theoretical), negative "
            "mass (unobserved), topological defects (unobserved) - each "
            "against a 1-meter wormhole throat requirement (~1e44 J), "
            "showing gaps of 40-80 orders of magnitude, then applies the "
            "inequality scaling to show the gap is law-like, not "
            "technological. An empty warehouse, inventoried."
        ),
        "key_points": [
            "Warp and wormhole concepts all invoice the same missing material: negative energy density.",
            "Candidate sources: Casimir (real, negligible), squeezed vacuum (real, fleeting), Hawking regions (theoretical), negative mass (unobserved), defects (unobserved).",
            "Gaps of 40-80 orders of magnitude between demonstrated and required.",
            "Quantum inequalities make the gap law-like, not technological.",
            "No scaling path exists for any candidate source.",
            "The inventory of an empty warehouse: every shelf labeled, every shelf bare.",
        ],
        "requirements": [
            "A negative-energy source scalable 40+ orders of magnitude (none).",
            "Evasion of quantum inequality bounds.",
            "Macroscopic, persistent negative energy densities.",
        ],
        "standards": [
            "Quantum inequalities (Ford-Roman) - the law-like restriction.",
            "Casimir and squeezed-state measurements - the empirical ceiling.",
            "FUS_SPECSTAT: no source at any relevant scale.",
        ],
        "citations": [
            FUS_CASIMIR48,
            FUS_BONDI57,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "walks the warehouse aisle by aisle - Casimir's shelf with its "
            "dust of real force, the squeezed-light shelf flickering for "
            "femtoseconds, and shelf after shelf of the unobserved - and "
            "records what the inequalities proclaim: the warehouse is not "
            "merely empty, it is zoned against ever being filled. Clearly "
            "labeled Signature-made."
        ),
    },
    {
        "key": "white_hole_concepts",
        "name": "White Hole Concepts",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "description": (
            "White holes - the time-reverse of black holes, regions that "
            "matter and light can only exit - are valid eternal-black-hole "
            "solutions in general relativity, occasionally proposed as "
            "fuel or power concepts (a white hole 'fountain' as an energy "
            "source) and as the far mouths of wormholes. Claims: an "
            "eternal outflow of energy, the exhaust side of interstellar "
            "shortcuts. Why unproven, decisively: no white hole has ever "
            "been observed - the universe contains black hole candidates "
            "but zero white hole candidates; formation is the wall - "
            "black holes form from collapse, but nothing is known that "
            "forms a white hole (the time-reverse of collapse is "
            "unphysical without exquisite fine-tuning); and stability "
            "analyses show white holes are violently unstable to even "
            "infinitesimal perturbations, decaying or collapsing on short "
            "timescales. Documented as the mirror speculation: the "
            "equations permit it, the universe declines to make it, and "
            "instability would unmake it if it tried."
        ),
        "how_it_works": (
            "The maximally extended Schwarzschild solution contains a white "
            "hole region (region IV of the Kruskal diagram), the time "
            "reverse of the black hole interior: geodesics can only emerge. "
            "The demo computes the formation ledger: gravitational collapse "
            "forms black holes because entropy and dynamics favor it; the "
            "time-reversed process - diffuse matter spontaneously assembling "
            "into an exploding white hole - requires initial conditions of "
            "measure zero, quantified via the absurdity of the reversed "
            "entropy gradient; then the instability ledger: perturbation "
            "growth rates (blue-shift instability at the past horizon) "
            "destroy the solution on light-crossing times. Permitted by "
            "the equations, declined by the universe."
        ),
        "key_points": [
            "White holes: time-reverse of black holes, valid GR solutions - zero observed.",
            "Proposed as energy fountains and wormhole far-mouths.",
            "Formation wall: collapse makes black holes; nothing makes white holes.",
            "Blue-shift instability destroys white holes on light-crossing times.",
            "The universe holds black hole candidates and zero white hole candidates.",
            "The mirror speculation: permitted by equations, declined by the universe.",
        ],
        "requirements": [
            "An observed white hole (none exists).",
            "A formation mechanism (none known).",
            "Stabilization against blue-shift instability.",
            "A coupling mechanism to harvest the 'fountain' (pure theory).",
        ],
        "standards": [
            "Kruskal extension of Schwarzschild - the mathematical home of white holes.",
            "Instability analyses - the physical veto.",
            "FUS_SPECSTAT: unobserved, unformable, unstable.",
        ],
        "citations": [
            FUS_HAWKING74,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "names the white hole the fountain that never was: the "
            "equations draw it pouring light forever, but the universe "
            "never built the fountain, and the blue-shift instability "
            "would shatter it in a light-crossing time if it tried. The "
            "Signature ledger files it under mirrors - beautiful, "
            "reversed, absent. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "cosmic_string_energy",
        "name": "Cosmic String Energy Concepts",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "description": (
            "Cosmic strings - hypothetical one-dimensional topological "
            "defects from early-universe phase transitions, with tensions "
            "up to ~1e21 kg/m at GUT scales - appear in fuel speculation "
            "because a loop of cosmic string contains staggering energy "
            "(a 1-km GUT loop masses ~1e24 kg), and oscillating loops "
            "radiate gravitationally. Proposals imagine capturing a loop "
            "as a fuel reserve or power source. Claims: the densest "
            "linear energy in physics, a capturable cosmic battery. Why "
            "unproven: no cosmic string has ever been observed - "
            "gravitational lensing and CMB searches (including Planck "
            "constraints) find nothing, bounding tensions well below GUT "
            "scale; a captured loop's dynamics (whipping at near-c, "
            "gravitational radiation, possible black-hole collapse) make "
            "'storage' meaningless; and cutting or tapping a string has no "
            "proposed mechanism - the speculation is 'find one, somehow "
            "use it.' Documented as the lost-treasure speculation: the "
            "map is theory, the treasure unobserved, and the chest, if "
            "found, could not be opened."
        ),
        "how_it_works": (
            "A cosmic string has mass per unit length mu ~ eta^2 (eta the "
            "symmetry-breaking scale); GUT strings give G mu/c^2 ~ 1e-6, "
            "mu ~ 1e21 kg/m. The demo computes the treasure ledger: a "
            "1-km loop at GUT tension masses 1e24 kg with E = 9e40 J - "
            "~1e27 years of world energy - then the capture ledger: loop "
            "oscillation at relativistic speeds, gravitational-wave power "
            "~100 G mu^2 c ~ 1e46 W for GUT loops (the loop radiates itself "
            "away), and the observational bound: Planck CMB limits push G "
            "mu/c^2 below ~1e-7, ruling out the richest strings. Treasure "
            "unobserved, chest unopenable."
        ),
        "key_points": [
            "Cosmic strings: hypothetical 1D defects, GUT tension ~1e21 kg/m - never observed.",
            "A 1-km GUT loop would hold ~9e40 J - the densest linear energy in physics.",
            "CMB (Planck) and lensing searches: nothing; tensions bounded below GUT scale.",
            "Loops whip at near-c and radiate away gravitationally - 'storage' is meaningless.",
            "No mechanism proposed to cut, tap, or capture a string.",
            "The lost-treasure speculation: theoretical map, unobserved treasure, unopenable chest.",
        ],
        "requirements": [
            "An observed cosmic string (none exists).",
            "A capture mechanism for a relativistic whipping loop.",
            "An energy-tapping mechanism (none proposed).",
            "Survival of the tap against gravitational-radiation losses.",
        ],
        "standards": [
            "Cosmic string theory (Kibble and successors) - the theoretical map.",
            "Planck CMB bounds - the observational veto on GUT-scale strings.",
            "FUS_SPECSTAT: unobserved; no tapping mechanism.",
        ],
        "citations": [
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "frames the cosmic string as the lost treasure of the early "
            "universe: a thread with the mass of worlds in every kilometer, "
            "if the thread exists. The Signature ledger sends out the "
            "search parties - lensing, CMB, gravitational waves - and "
            "they return empty-handed, with bounds where treasure was "
            "marked. Clearly labeled Signature-made."
        ),
    },
    {
        "key": "kardashev_fuel_ladder",
        "name": "The Kardashev Fuel Ladder",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "description": (
            "Nikolai Kardashev's 1964 scale - Type I commanding planetary "
            "power (~4e12 W in his original, ~1e16 W in popular usage), "
            "Type II stellar (~4e26 W), Type III galactic (~4e37 W) - is "
            "not a fuel but the ladder every fuel in this database climbs: "
            "each concept is placed by the power its fuel could command. "
            "Sagan's interpolation (K = (log10 P - 6)/10) puts humanity at "
            "~0.73. This capstone record maps the database onto the "
            "ladder: chemical fuels are sub-Type I; D-T fusion power at "
            "civilization scale approaches Type I; antimatter and black-"
            "hole power reach toward Type II; warp and vacuum-decay "
            "concepts gesture at Type III. Claims: a civilization's fuel "
            "is its rank. Why the mapping is speculative: no civilization "
            "above ~0.73 is known - the scale is an extrapolation, not an "
            "observation; each rung's fuel remains in this database's "
            "unproven column; and the scale says nothing about whether "
            "higher rungs are reachable in principle. Documented as the "
            "capstone: the ladder the whole database climbs, with every "
            "rung above the present marked 'unproven' - the honest summit "
            "of speculation."
        ),
        "how_it_works": (
            "Kardashev's scale is logarithmic: each type commands ~1e10-1e11 "
            "W more than the last. Sagan's formula K = (log10(P) - 6)/10 "
            "interpolates. The demo computes the ladder: world power "
            "~1.8e13 W -> K ~ 0.73; Type I (1e16 W) -> 1.0; a D-T "
            "civilization at 1e16 W; a 1e9 kg black-hole power plant at "
            "3.6e14 W -> K ~ 0.86; a star-eating Type II at 4e26 W -> 2.0; "
            "then places each database concept on the ladder with its "
            "speculative status - showing that every rung above 0.73 is "
            "fueled by concepts this database marks unproven. The honest "
            "summit: the ladder is real arithmetic, the upper rungs are "
            "speculation."
        ),
        "key_points": [
            "Kardashev 1964: Type I planetary, Type II stellar, Type III galactic power.",
            "Sagan interpolation: K = (log10 P - 6)/10; humanity ~0.73.",
            "Each database concept maps to a rung by its commanded power.",
            "No civilization above ~0.73 is known - the scale is extrapolation.",
            "Every rung above the present is fueled by unproven concepts.",
            "The capstone: the ladder the database climbs, honestly marked.",
        ],
        "requirements": [
            "Power accounting for each fuel at civilization scale.",
            "Sagan-interpolated rank for each concept.",
            "Acknowledgment that the scale is extrapolation, not observation.",
        ],
        "standards": [
            "Kardashev's original scale (Soviet Astronomy 1964).",
            "Sagan's interpolation formula.",
            "FUS_SPECSTAT: the ladder is arithmetic; the upper rungs are speculation.",
        ],
        "citations": [
            FUS_KARDASHEV64,
            FUS_SPECSTAT,
        ],
        "sig_lens": (
            "Signature original theoretical exploration. His Signature reading "
            "makes the Kardashev ladder the summit ledger: every fuel in "
            "this database is a rung, and the Signature hand marks each "
            "rung honestly - kept or unkept, demonstrated or dreamed. "
            "Humanity stands at 0.73, and every rung above is a promise "
            "the universe has not yet been seen to keep. The honest summit "
            "of speculation. Clearly labeled Signature-made."
        ),
    },
]

print("entries complete: %d" % len(ENTRIES))
assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == list(range(1, 35)), "ladder ranks must be 1-34 in order"
keys = [e["key"] for e in ENTRIES]
assert len(set(keys)) == 34, "duplicate keys"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier",
              "description", "how_it_works", "key_points", "requirements",
              "standards", "citations", "sig_lens"):
        assert k in e and e[k], "missing/empty %s in %s" % (k, e["key"])
    blob = (e["description"] + e["how_it_works"] + e["sig_lens"] +
            " ".join(e["key_points"])).lower()
    assert "facebook" not in blob
    assert "bat belt" not in blob
print("entries validated: 34 entries, ladder 1-34, all fields present")
