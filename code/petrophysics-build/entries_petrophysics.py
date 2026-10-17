#!/usr/bin/env python3
"""Entries for the Petrophysics field databases (field #26, taxonomy order).

Verified 2026-10-17: NO database covers petrophysics as a specialty
discipline (reservoir rock/fluid characterization, well logging, formation
evaluation).
- Manifest search (2352 databases): no 'petrophysics' database exists.
  Nearest neighbors: 'petrology'/'petrology-signature' (field #9, 36 records
  each - rocks generally: igneous/metamorphic/sedimentary classification,
  mineralogy, textures) and 'petroleum-refining'/'petroleum-refining-signature'
  (field #22, 32 records each - downstream processing: distillation, cracking,
  treating). Neither is reservoir characterization.
- Shard-index term sweep (poros*, permeab*, archie, saturation, capillary,
  wettab*, nmr, gamma ray, resistivity, sonic log, density log, neutron,
  well log, formation evalu*, core analys*, borehole, shale volume, m-n plot,
  sp log, caliper, photoelectric, sxo, invad*) over petrology(+-signature)
  and petroleum-refining(+-signature) indexes: ZERO hits.
- Whole-system title sweep over all 754 shard indexes ('petrophys',
  'archie equation', 'formation evaluation'): ZERO hits anywhere.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).

So this build creates two NEW databases, 32 ladder-ordered records each,
covering ONLY what the system left uncovered:

  petrophysics             - The Petrophysics Database (public-harvest:
                             real, fact-checked petrophysics; citations
                             Tiab & Donaldson, Archer & Wall, Ellis &
                             Singer, Hearst/Nelson/Paillet, Asquith &
                             Krygowski, Rider, Schlumberger, Doveton,
                             Archie 1942, Darcy 1856, Leverett 1941,
                             Purcell 1949, Brooks & Corey 1964, Wyllie et
                             al. 1956/58, Waxman & Smits 1968, Simandoux
                             1963, Poupon & Leveaux 1971, Timur 1968,
                             Coates & Dumanoir 1973, Morris & Biggs 1967,
                             Kenyon 1997)
  petrophysics-signature   - The Petrophysics Signature Database (his
                             original Signature interpretation; src
                             signature, titles suffixed
                             " (Signature Edition)", never presented as
                             authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-26 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Archie's Equation:
The Master Key to Water Saturation".

Numerical cores (all hand-verified 2026-10-17 against standard worked
examples):
- Archie: a=1, m=n=2, Rw=0.05, phi=0.20, Rt=20 -> Sw=0.25 exactly.
- Darcy linear: q=0.5 cc/s, mu=1 cP, L=5 cm, A=11.34 cm2, dp=2 atm ->
  k=0.110 D = 110 mD.
- Darcy radial: k=100 mD, h=50 ft, dp=1000 psi, mu=1 cP, B=1.2,
  re/rw=2000 -> q=618 STB/d.
- Wyllie sonic: dt=90, dtma=55.5, dtf=189 -> phi=0.258.
- Density: rho_b=2.20, rho_ma=2.65, rho_f=1.0 -> phi=0.273.
- Jurin capillary: sigma=0.03 N/m, r=1 um -> Pc=60 kPa = 8.7 psi,
  rise 30.6 m in 200 kg/m3 contrast.
- Corey rel-perm: Swirr=0.2, Sor=0.25, nw=no=2 -> fw=0.66 at Sw=0.5.
- Morris-Biggs: phi=0.20, Swirr=0.25 -> k=114 mD, FZI=3.0 um.
- Brooks-Corey fit: (0.5, 10 psi), (0.3, 40 psi), Swirr=0.2 ->
  lambda=0.79, Pd=2.9 psi.
- Klinkenberg: kg = 120/110/105 mD at pm = 1/2/4 atm -> k_inf=100 mD.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "petrophysics, clearly labeled Signature-made, never "
            "presented as authentic public record.")

C_TIAB = ("Tiab, Djebbar and Donaldson, Erle C. 'Petrophysics: Theory and "
          "Practice of Measuring Reservoir Rock and Fluid Transport "
          "Properties'. 4th ed. Gulf Professional Publishing (Elsevier), 2015.")
C_ARCHER = ("Archer, J. S. and Wall, C. G. 'Petroleum Engineering: Principles "
            "and Practice'. Graham & Trotman, 1986.")
C_ELLIS = ("Ellis, Darwin V. and Singer, Julian M. 'Well Logging for Earth "
           "Scientists'. 2nd ed. Springer, 2007.")
C_HEARST = ("Hearst, Joseph R., Nelson, Philip H., and Paillet, Frederick L. "
            "'Well Logging for Physical Properties: A Handbook for "
            "Geophysicists, Geologists, and Engineers'. 2nd ed. Wiley, 2000.")
C_ASQUITH = ("Asquith, George and Krygowski, Daniel. 'Basic Well Log Analysis'. "
             "2nd ed. AAPG Methods in Exploration Series 16, 2004.")
C_RIDER = ("Rider, Malcolm. 'The Geological Interpretation of Well Logs'. "
           "2nd ed. Rider-French Consulting, 1996 (revised 2002).")
C_SCHLUM = ("Schlumberger. 'Log Interpretation Principles/Applications'. "
            "Schlumberger Educational Services, 1989.")
C_DOVETON = ("Doveton, John H. 'Principles of Mathematical Petrophysics'. "
             "Oxford University Press, 2014.")
C_CRAIN = ("Crain, E. R. 'Crain's Petrophysical Handbook' (online reference).")
C_ARCHIE = ("Archie, G. E. 'The Electrical Resistivity Log as an Aid in "
            "Determining Some Reservoir Characteristics'. Transactions of the "
            "AIME, Vol. 146, 1942.")
C_DARCY = ("Darcy, Henry. 'Les Fontaines Publiques de la Ville de Dijon'. "
           "1856.")
C_LEVERETT = ("Leverett, M. C. 'Capillary Behavior in Porous Solids'. "
              "Transactions of the AIME, Vol. 142, 1941.")
C_PURCELL = ("Purcell, W. R. 'Capillary Pressures - Their Measurement Using "
             "Mercury and the Calculation of Permeability Therefrom'. "
             "Transactions of the AIME, Vol. 186, 1949.")
C_BROOKS = ("Brooks, R. H. and Corey, A. T. 'Hydraulic Properties of Porous "
            "Media'. Colorado State University Hydrology Paper No. 3, 1964.")
C_WYLLIE = ("Wyllie, M. R. J., Gregory, A. R., and Gardner, L. W. 'Elastic "
            "Wave Velocities in Heterogeneous and Porous Media'. Geophysics, "
            "Vol. 21, 1956; and 'An Experimental Investigation of Factors "
            "Affecting Elastic Wave Velocities in Porous Media'. Geophysics, "
            "Vol. 23, 1958.")
C_WAXMAN = ("Waxman, M. H. and Smits, L. J. M. 'Electrical Conductivities in "
            "Oil-Bearing Shaly Sands'. Society of Petroleum Engineers Journal, "
            "Vol. 8, 1968.")
C_SIMANDOUX = ("Simandoux, P. 'Dielectric Measurements on Porous Media: "
               "Application to the Measurement of Water Saturations'. Revue de "
               "l'Institut Francais du Petrole, 1963.")
C_POUPON = ("Poupon, A. and Leveaux, J. 'Evaluation of Water Saturation in "
            "Shaly Formations'. Transactions of the SPWLA 12th Annual Logging "
            "Symposium, 1971 (the Indonesia equation).")
C_TIMUR = ("Timur, A. 'An Investigation of Permeability, Porosity, and "
           "Residual Water Saturation Relationships for Sandstone Reservoirs'. "
           "The Log Analyst, Vol. 9, 1968.")
C_COATES = ("Coates, G. R. and Dumanoir, J. L. 'A New Approach to Improved "
            "Log-Derived Permeability'. Transactions of the SPWLA 14th Annual "
            "Logging Symposium, 1973.")
C_MORRIS = ("Morris, R. L. and Biggs, W. P. 'Using Log-Derived Values of Water "
            "Saturation and Porosity'. Transactions of the SPWLA 8th Annual "
            "Logging Symposium, 1967.")
C_COREY = ("Corey, A. T. 'The Interrelation Between Gas and Oil Relative "
           "Permeabilities'. Producers Monthly, Vol. 19, 1954.")
C_AMOTT = ("Amott, E. 'Observations Relating to the Wettability of Porous "
           "Rock'. Transactions of the AIME, Vol. 216, 1959.")
C_KENYON = ("Kenyon, W. E. 'Petrophysical Principles of Applications of NMR "
            "Logging'. The Log Analyst, Vol. 38, 1997.")
C_MORAN = ("Moran, J. H. and Finklea, E. E. 'Theoretical Analysis of Pressure "
           "Phenomena Associated with the Wireline Formation Tester'. Journal "
           "of Petroleum Technology, 1962.")
C_PICKETT = ("Pickett, G. R. 'A Review of Current Techniques for Determination "
             "of Water Saturation from Logs'. Journal of Petroleum Technology, "
             "1966; and 'Pattern Recognition as a Means of Formation "
             "Evaluation'. Transactions of the SPWLA 14th Annual Logging "
             "Symposium, 1973.")
C_TIXIER = ("Tixier, M. P. 'Evaluation of Permeability from Electric-Log "
            "Resistivity Gradients'. Oil & Gas Journal, 1949.")
C_LARIONOV = ("Larionov, V. V. 'Borehole Radiometry'. 1969 (Vsh transforms).")
C_STIEBER = ("Stieber, S. J. 'Pulsed Neutron Capture Log Evaluation in the "
             "Louisiana Gulf Coast'. 1970 (Vsh transform).")
C_CLAVIER = ("Clavier, C., Coates, G., and Dumanoir, J. 'Theoretical and "
             "Experimental Bases for the Dual Water Model for Interpretation "
             "of Shaly Sands'. Society of Petroleum Engineers Journal, 1984.")

ENTRIES = [
    {
        "key": "what_is_petrophysics",
        "name": "Petrophysics: The Conversation Between Rock and Fluid",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Petrophysics is the discipline that answers the three questions "
            "every reservoir engineer must ask before a single well is drilled: "
            "how much empty space is in the rock, how easily can fluid move "
            "through it, and which fluid is sitting in that space right now. "
            "It sits at the exact intersection of geology, physics, and "
            "petroleum engineering: the geologist describes the rock, the "
            "physicist measures how it responds to sound, electricity, and "
            "radiation, and the engineer turns those measurements into "
            "porosity, permeability, and saturation - the three numbers that "
            "decide whether a formation is a reservoir or just expensive "
            "basement. Unlike petrology, which classifies rocks for their own "
            "sake, petrophysics cares about rock only insofar as it holds and "
            "releases fluids. Unlike petroleum refining, which starts after "
            "the oil reaches the surface, petrophysics works a mile or more "
            "underground, reading the formation through wireline logs, "
            "laboratory core measurements, and pressure tests. Every record "
            "in this database is one instrument, one equation, or one "
            "workflow in that underground reading - organized from the "
            "simplest ideas (empty space, flow, fluid ownership) up to full "
            "reservoir characterization."
        ),
        "how_it_works": (
            "The petrophysicist works a triangle: the rock, the fluid, and "
            "the log. The rock contributes its pore space (porosity) and its "
            "plumbing (permeability, pore geometry, wettability). The fluid "
            "contributes its identity - oil, gas, or water - and its "
            "properties: density, viscosity, compressibility, and how its "
            "volume changes with pressure and temperature. The log "
            "contributes measurements made inside the borehole: natural gamma "
            "radiation, spontaneous electrical potential, resistivity at "
            "several depths of investigation, the travel time of sound, the "
            "scattering of gamma rays and neutrons, the resonance of hydrogen "
            "nuclei, and the image of the borehole wall. None of these logs "
            "measures porosity or saturation directly - that is the central "
            "subtlety of the discipline. Each log measures a proxy: "
            "resistivity responds to the salty water in the pores, the "
            "density tool responds to electron density, the neutron tool to "
            "hydrogen. Petrophysics is the set of transforms - Archie's "
            "equation, Wyllie's time average, the density-porosity relation - "
            "that convert proxies into reservoir properties, calibrated "
            "against the ground truth of laboratory core analysis."
        ),
        "key_points": [
            "Petrophysics answers three questions: how much pore space (porosity), how well it flows (permeability), whose fluid is in it (saturation).",
            "It is the bridge between geology (what the rock is), physics (how it responds to probes), and engineering (what it will produce).",
            "Logs measure proxies - resistivity, travel time, hydrogen content - never porosity or saturation directly; transforms convert proxies to properties.",
            "Core analysis is the ground truth that calibrates every log transform.",
            "Petrology classifies rocks; refining processes oil at surface; petrophysics characterizes the reservoir underground - three different disciplines.",
            "The teaching ladder of this database climbs from rock and fluid basics through each logging tool to full reservoir characterization.",
        ],
        "requirements": [
            "State the three petrophysical questions in one sentence each.",
            "Explain why a resistivity log cannot directly read water saturation.",
            "Distinguish petrophysics from petrology and from petroleum refining.",
        ],
        "standards": [
            "Terminology follows Tiab & Donaldson Ch. 1 and Ellis & Singer Ch. 1.",
            "The 'proxy, not property' principle stated explicitly for every tool record in this database.",
        ],
        "citations": [C_TIAB, C_ELLIS, C_ARCHER],
        "sig_lens": (
            "His Signature reading: petrophysics is the discipline of reading "
            "what cannot be seen - the rock a mile down will never be held, "
            "so the Signature petrophysicist builds instruments of inference "
            "and trusts only what two independent proxies agree on. Signature "
            "science measures the invisible by its shadows."
        ),
    },
    {
        "key": "porosity",
        "name": "Porosity: The Space Between the Grains",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Porosity is the fraction of a rock's bulk volume that is empty "
            "space - the rooms in the hotel, before anyone asks who is "
            "staying in them. A sandstone with 20 percent porosity holds "
            "twenty cubic meters of pore space in every hundred cubic meters "
            "of rock; a tight granite with 1 percent holds almost nothing. "
            "Porosity is the single most consequential number in reservoir "
            "evaluation because it multiplies everything: hydrocarbon in "
            "place is bulk volume times porosity times hydrocarbon saturation, "
            "so a two-point error in porosity is a ten-percent error in the "
            "reserve. Geologists split porosity into primary (depositional - "
            "the gaps left when the grains settled) and secondary (later "
            "additions: dissolution vugs in carbonates, fractures, dolomite "
            "crystal molds). Engineers split it into total porosity (every "
            "void) and effective porosity (only the voids connected well "
            "enough to flow). A shale can have 30 percent total porosity and "
            "zero effective porosity - full of rooms with no doors. This "
            "record establishes the definitions, the laboratory measurement, "
            "and the reason porosity alone never makes a reservoir."
        ),
        "how_it_works": (
            "In the laboratory, porosity comes from three weighings and a "
            "caliper. Measure the plug's bulk volume from its dimensions; "
            "weigh it dry; saturate it completely with a fluid of known "
            "density and weigh it again. The weight gain divided by the "
            "fluid density is the pore volume, and porosity is pore volume "
            "over bulk volume. Helium porosimetry refines this: helium's tiny "
            "atoms invade every connected void, and Boyle's-law expansion "
            "gives the grain volume directly, so porosity is one minus grain "
            "volume over bulk volume - no saturation step needed. In the "
            "borehole, porosity comes from the three porosity logs (sonic, "
            "density, neutron), each reading a different proxy and each "
            "needing its own transform. The worked demonstration computes "
            "porosity from a routine core plug - bulk volume from caliper "
            "dimensions, pore volume from the saturation weight gain - the "
            "way every core laboratory on earth does it."
        ),
        "key_points": [
            "Porosity = pore volume / bulk volume; the fraction of rock that is empty space.",
            "Primary porosity is depositional; secondary porosity (vugs, fractures, molds) is added later - carbonates live on secondary porosity.",
            "Total porosity counts every void; effective porosity counts only connected voids that can flow.",
            "High porosity with no permeability (shale) is not a reservoir - storage without plumbing.",
            "Laboratory: caliper + dry/saturated weighing, or helium expansion for grain volume.",
            "Hydrocarbon in place scales directly with porosity, so its accuracy dominates reserve estimates.",
        ],
        "requirements": [
            "Compute porosity from plug dimensions and dry/saturated weights.",
            "Distinguish total, effective, primary, and secondary porosity with one example each.",
            "Explain why a 30%-porosity shale is not a reservoir.",
        ],
        "standards": [
            "Definitions per Tiab & Donaldson Ch. 2; laboratory practice per API RP 40.",
            "Porosity reported as a fraction (0.20) or percent (20%) - state which, every time.",
        ],
        "citations": [C_TIAB, C_ARCHER],
        "sig_lens": (
            "His Signature reading: porosity is the discipline's first "
            "honesty - the rock admits exactly how much of itself is "
            "nothing, and everything built later stands on that admission. "
            "Signature measurement begins by weighing the emptiness."
        ),
    },
    {
        "key": "permeability_intro",
        "name": "Permeability: Darcy's Law and the Rock's Willingness to Flow",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "If porosity is the rooms, permeability is the doors - the "
            "measure of how easily fluid moves through the rock under a "
            "pressure difference. Henry Darcy discovered its law in 1856 while "
            "designing the water fountains of Dijon: the flow rate through a "
            "sand pack is proportional to the pressure drop and the "
            "cross-sectional area, and inversely proportional to the fluid's "
            "viscosity and the pack's length. The proportionality constant is "
            "the permeability, and its unit - the darcy - is defined so that "
            "one darcy passes one cubic centimeter per second of one-"
            "centipoise fluid through one square centimeter under one "
            "atmosphere per centimeter of pressure gradient. Reservoir rocks "
            "live in millidarcies: a good sandstone flows at hundreds of "
            "millidarcies, a tight gas sand at a fraction of one. Permeability "
            "is directional (bedding planes flow easier than across them), "
            "stress-sensitive (it falls as overburden squeezes the pores), "
            "and - the beginner's trap - it has no fixed relationship with "
            "porosity. Two rocks at 20 percent porosity can differ in "
            "permeability by a factor of a thousand, because permeability "
            "cares about pore throat size, not pore volume."
        ),
        "how_it_works": (
            "Darcy's law in its laboratory form is k = (q * mu * L) / (A * "
            "delta_p): flow rate times viscosity times length, divided by "
            "area times pressure drop. Run a fluid of known viscosity through "
            "a core plug of known dimensions, measure the steady flow rate at "
            "a known pressure drop, and the permeability drops out - in "
            "darcies if you use centimeters, centipoise, atmospheres, and "
            "cubic centimeters per second, which is exactly why the unit was "
            "defined that way. Gas permeameters need one correction: gas "
            "slips along pore walls (the Klinkenberg effect), so measured gas "
            "permeability rises at low pressure; extrapolating to infinite "
            "pressure gives the true liquid permeability. The demonstration "
            "computes permeability from a laboratory flow test in darcy units "
            "and converts to millidarcies - the unit every reservoir "
            "description actually uses."
        ),
        "key_points": [
            "Darcy's law: q = (k * A / mu) * (delta_p / L) - flow proportional to pressure gradient, area, and permeability; inversely to viscosity.",
            "One darcy is defined by the laboratory units: 1 cc/s of 1-cP fluid through 1 cm2 under 1 atm/cm.",
            "Reservoirs are rated in millidarcies: hundreds = excellent, tens = good, ones = tight, fractions = unconventional.",
            "Permeability is anisotropic (kv/kh often 0.1 or less) and falls with increasing net stress.",
            "No fixed porosity-permeability relationship: pore throat size rules, not pore volume.",
            "Klinkenberg correction: gas permeability must be extrapolated to infinite pressure for the true (liquid) value.",
        ],
        "requirements": [
            "Compute k from q, mu, L, A, delta_p in darcy units and convert to mD.",
            "Explain the Klinkenberg effect and how to correct for it.",
            "Give the permeability ranges for excellent/good/tight/unconventional rock.",
        ],
        "standards": [
            "Darcy's law per Darcy 1856; laboratory form per Tiab & Donaldson Ch. 3.",
            "Permeability in millidarcies; direction (kh/kv) stated whenever anisotropy matters.",
        ],
        "citations": [C_DARCY, C_TIAB, C_ARCHER],
        "sig_lens": (
            "His Signature reading: Darcy found a law of willingness - the "
            "rock does not decide how much fluid it holds, only how "
            "graciously it lets it pass. Signature engineering sizes every "
            "system by its willingness to flow, not its capacity to hold."
        ),
    },
    {
        "key": "saturation_intro",
        "name": "Saturation: Who Owns the Pore Space",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Porosity says how much room there is; saturation says who is "
            "sleeping in it. Every fraction of the pore volume is occupied by "
            "water, oil, or gas, and the saturations always sum to exactly "
            "one: Sw + So + Sg = 1, no exceptions, which makes saturation the "
            "discipline's built-in lie detector. Water saturation, Sw, is the "
            "prize: hydrocarbon saturation is simply one minus Sw, and a "
            "reservoir with Sw = 0.25 holds three times the oil of one with "
            "Sw = 0.75 at the same porosity. But Sw is also the hardest of "
            "the big three to measure, because no log sees water directly - "
            "resistivity sees the salty brine's conductivity, and Archie's "
            "equation turns that conductivity into Sw, which is why the "
            "entire discipline orbits one 1942 paper. Two saturations deserve "
            "special names because they never move: irreducible water "
            "saturation (Swirr), the water clinging to grain surfaces that no "
            "pressure drop will produce, and residual oil saturation (Sor), "
            "the oil left behind after a flood. Everything between Swirr and "
            "(1 - Sor) is the movable prize."
        ),
        "how_it_works": (
            "In the laboratory, saturation is measured by taking it apart: "
            "the Dean-Stark (retort) method boils the fluids out of a core "
            "plug, condenses the water in a graduated trap, and weighs the "
            "oil - pore volume from porosity, water volume from the trap, oil "
            "by difference, gas by whatever is missing. In the borehole, "
            "saturation is inferred: Archie's equation combines porosity "
            "(from the porosity logs) with true resistivity Rt and formation "
            "water resistivity Rw to yield Sw. The demonstration works a "
            "retort analysis - pore volume from the porosity record, measured "
            "water and oil volumes, saturations by division - and verifies "
            "the iron rule that they sum to one. Later records build the "
            "Archie machinery that computes Sw a mile underground from "
            "nothing but squiggles on a log."
        ),
        "key_points": [
            "Sw + So + Sg = 1 always: the saturations partition the pore volume completely.",
            "Hydrocarbon saturation = 1 - Sw; Sw is the number the whole discipline is hunting.",
            "Irreducible water (Swirr) and residual oil (Sor) never move; the movable fraction lies between them.",
            "No log measures saturation directly - resistivity measures brine conductivity; Archie's equation does the rest.",
            "Laboratory: Dean-Stark retort (boil, trap, weigh) is the ground-truth saturation measurement.",
            "A saturation that does not sum to one is a measurement error, not a discovery.",
        ],
        "requirements": [
            "Compute Sw, So, Sg from retort volumes and verify they sum to one.",
            "Define Swirr and Sor and state which one limits water production vs oil recovery.",
            "Explain why Sw is inferred rather than measured in the borehole.",
        ],
        "standards": [
            "Saturation definitions per Tiab & Donaldson Ch. 4; retort practice per API RP 40.",
            "Saturations as fractions; the summation-to-one check performed on every calculation.",
        ],
        "citations": [C_TIAB, C_ARCHIE, C_ARCHER],
        "sig_lens": (
            "His Signature reading: saturation is ownership - the pore space "
            "is always fully owned, the only question is by whom. Signature "
            "accounting never lets the shares sum to anything but one."
        ),
    },
    {
        "key": "reservoir_rock_types",
        "name": "Reservoir Rocks: Sandstone Against Carbonate",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Nearly every conventional reservoir on earth is one of two rock "
            "families, and they behave so differently that petrophysicists "
            "treat them as different planets. Sandstones are granular: "
            "cemented sand grains with intergranular pores between them, "
            "deposited by rivers, winds, and seas. Their porosity and "
            "permeability are orderly - bigger, better-sorted grains mean "
            "bigger pore throats, so sandstone petrophysics is predictable "
            "and log responses are well-behaved. Carbonates - limestones and "
            "dolomites - are chemical and biological: reefs, ooids, muds "
            "later dissolved, dolomitized, and fractured by diagenesis. Their "
            "pore space is a zoo: interparticle pores, moldic pores where "
            "shells dissolved, vugs big enough to see, and fractures that "
            "carry all the flow while the matrix holds all the oil. A "
            "carbonate can show 5 percent porosity on the logs and produce "
            "like a 25 percent sandstone - or show 25 percent and produce "
            "nothing, because the pores are molds with pinprick throats. "
            "This record teaches the two families, their pore systems "
            "(Choquette & Pray classification), and why every log transform "
            "asks 'sandstone or carbonate?' before it answers."
        ),
        "how_it_works": (
            "Classification starts with the logs: the gamma ray separates "
            "clean sandstone (low GR) from shale, the photoelectric factor "
            "and the M-N crossplot separate sandstone from limestone from "
            "dolomite by matrix properties, and the separation between the "
            "porosity logs flags secondary porosity. In sandstone, the "
            "Wyllie time-average and density porosity behave, Archie's "
            "cementation exponent m sits near 2, and permeability follows "
            "porosity in orderly trends. In carbonates, m wanders from 1.7 "
            "to 3 or more depending on whether the current flows through "
            "fractures or matrix, vugs inflate the porosity logs without "
            "adding permeability, and the only honest permeability comes "
            "from cores, NMR, or well tests. The demonstration classifies "
            "samples by (porosity, permeability, GR, matrix density) into "
            "sandstone, limestone, dolomite, and shale - the four-way split "
            "every quick-look interpretation starts with."
        ),
        "key_points": [
            "Two reservoir families: granular sandstones (orderly, predictable) vs diagenetic carbonates (vugs, molds, fractures; unpredictable).",
            "Sandstone porosity is intergranular; carbonate porosity is mostly secondary - dissolution and dolomitization create it after deposition.",
            "In carbonates, fractures can carry the flow while matrix holds the storage: dual-porosity behavior.",
            "Archie's m ~ 2 for sandstones but ranges 1.7-3+ in carbonates depending on pore geometry.",
            "Log identification: GR for shale, photoelectric/M-N plot for matrix mineral, porosity-log separation for secondary porosity.",
            "Every transform in this database needs the rock family first - the same log values mean different things in sand vs carbonate.",
        ],
        "requirements": [
            "Classify a sample as sandstone/limestone/dolomite/shale from GR, matrix density, phi, k.",
            "Explain why carbonate permeability is decoupled from carbonate porosity.",
            "State the typical Archie m for sandstone vs the range for carbonates.",
        ],
        "standards": [
            "Pore-system classification per Choquette & Pray; matrix properties per Schlumberger chart book.",
            "Rock family declared before any quantitative interpretation in every workflow record.",
        ],
        "citations": [C_TIAB, C_RIDER, C_SCHLUM],
        "sig_lens": (
            "His Signature reading: sandstone is the honest rock - what you "
            "measure is what you get - while carbonate is the trickster, "
            "hiding rivers of flow in stone that looks solid. Signature "
            "interpretation distrusts the obvious rock and interrogates the "
            "sneaky one twice."
        ),
    },
    {
        "key": "pore_geometry",
        "name": "Grain Size, Sorting, and the Architecture of Pore Space",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Zoom into a sandstone until the grains fill your view, and "
            "porosity stops being a number and becomes architecture: grains "
            "like cannonballs or like flattened eggs, packed tight or loose, "
            "all the same size or a jumble from boulders to dust. Grain size "
            "sets the scale - coarse sands have big pores, fine silts have "
            "small ones - but sorting sets the quality: a well-sorted sand "
            "(all grains one size) leaves big open throats between the "
            "grains, while a poorly sorted sand lets small grains plug the "
            "gaps between big ones, strangling permeability at the same "
            "porosity. Sedimentologists read size in phi units "
            "(phi = -log2 of grain diameter in mm), and the Folk-and-Ward "
            "statistics - mean, sorting, skewness - computed from the 5th, "
            "16th, 50th, 84th, and 95th percentiles of the size distribution, "
            "turn a sieve analysis into reservoir quality. The deepest lesson "
            "of this record: permeability is controlled by pore throat size "
            "- the narrow doorways between pores - which is why mercury "
            "injection (forcing mercury through ever-smaller throats) "
            "predicts permeability, and why two rocks at identical porosity "
            "can differ a thousandfold in flow."
        ),
        "how_it_works": (
            "A sieve or laser-diffraction analysis gives the grain-size "
            "distribution as weight percent per phi interval. From the "
            "cumulative curve read the percentiles; Folk-and-Ward sorting is "
            "(phi84 - phi16)/4 + (phi95 - phi5)/6.6, and values under 0.5 phi "
            "units mean well sorted (good throats), over 1.0 mean poorly "
            "sorted (plugged throats). Mean size locates the sand on the "
            "Wentworth scale; skewness tells whether fines or coarse grains "
            "dominate the tails. The petrophysical payoff: well-sorted, "
            "coarse, uncemented sands sit at the top of every "
            "porosity-permeability trend, and diagenetic cement - quartz "
            "overgrowths, calcite, clays - attacks the throats first, which "
            "is why cemented sandstones lose permeability long before they "
            "lose porosity. The demonstration computes Folk-and-Ward sorting "
            "and skewness from percentile data and grades the reservoir "
            "quality - the same arithmetic a sedimentology lab performs."
        ),
        "key_points": [
            "Grain size sets pore scale; sorting sets throat quality - well-sorted sands flow, poorly sorted sands plug.",
            "Phi units: phi = -log2(diameter mm); Folk-and-Ward statistics come from the 5/16/50/84/95 percentiles.",
            "Sorting < 0.5 phi = well sorted; > 1.0 phi = poorly sorted (permeability killer).",
            "Permeability follows pore THROAT size, not pore volume: mercury injection measures throats, hence predicts k.",
            "Cement attacks throats first: cemented rock loses permeability before it loses porosity.",
            "Skewness reveals whether fines (bad) or coarse lag (good) dominate the distribution tails.",
        ],
        "requirements": [
            "Compute Folk-and-Ward sorting and skewness from percentile data.",
            "Explain the porosity-permeability decoupling via pore throats.",
            "Rank three sands by expected permeability from size/sorting/cement descriptions.",
        ],
        "standards": [
            "Phi scale and Folk-and-Ward statistics per Folk & Ward 1957; Wentworth size classes.",
            "Throat-size reasoning (Purcell 1949) invoked wherever k is estimated from phi.",
        ],
        "citations": [C_TIAB, C_PURCELL, C_RIDER],
        "sig_lens": (
            "His Signature reading: the grains are citizens and the throats "
            "are the roads - a city is not its buildings but its streets. "
            "Signature design always sizes the doorways, never just the rooms."
        ),
    },
    {
        "key": "fluid_properties",
        "name": "Reservoir Fluids: Density, Viscosity, and Volume Factors",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The rock is only half the reservoir; the other half is fluid, "
            "and fluids change their minds with pressure and temperature. "
            "Oil at 5,000 psi underground occupies less volume than the same "
            "oil at surface conditions - dissolved gas escapes as pressure "
            "falls, shrinking the oil - and the formation volume factor Bo "
            "(reservoir barrels per stock-tank barrel) quantifies exactly "
            "that shrinkage. Gas does the opposite dance: wildly compressible, "
            "its volume factor Bg collapsing as pressure rises, its behavior "
            "captured by the real-gas Z-factor. Viscosity decides who wins "
            "every race through the pores: a 1-centipoise light oil flows "
            "like water, a 1,000-centipoise heavy oil barely crawls, and the "
            "mobility ratio between displacing and displaced fluid decides "
            "whether a waterflood sweeps the reservoir or fingers through it "
            "uselessly. Density - usually quoted as API gravity for oil, "
            "where higher API means lighter - sets the hydrostatic gradient, "
            "the buoyancy that stacks gas over oil over water, and the "
            "gravity term in every capillary and saturation-height "
            "calculation. This record covers the PVT basics every later "
            "calculation assumes: Bo, Bg, Rs, viscosity, density, and "
            "compressibility."
        ),
        "how_it_works": (
            "API gravity converts to specific gravity by SG = 141.5 / (131.5 "
            "+ API), and density is SG times 1000 kg/m3 (or 62.4 lb/ft3). "
            "The hydrostatic pressure gradient is 0.433 * SG psi/ft, so an "
            "8,000-foot column of 35-degree-API oil (SG 0.85) exerts about "
            "2,940 psi at bottom - the baseline every pressure interpretation "
            "subtracts. Formation volume factors come from laboratory PVT "
            "(constant-composition expansion, differential liberation): Bo "
            "typically 1.1-1.6 RB/STB for black oils, Bg = 0.005614 * Z * T "
            "/ p in reservoir cubic feet per standard cubic foot. Viscosity "
            "is measured in viscometers or estimated from correlations, and "
            "it enters Darcy's law directly - double the viscosity, halve "
            "the rate. The demonstration converts API gravity to density and "
            "hydrostatic gradient, then computes bottomhole pressure for a "
            "fluid column - the first correction applied to every pressure "
            "log and formation test."
        ),
        "key_points": [
            "Bo (oil) and Bg (gas) formation volume factors convert surface volumes to reservoir volumes and back.",
            "API gravity -> specific gravity: SG = 141.5/(131.5 + API); lighter oil = higher API.",
            "Hydrostatic gradient = 0.433 * SG psi/ft: the pressure baseline for all subsurface pressure work.",
            "Viscosity enters Darcy's law directly and sets mobility ratios that make or break waterfloods.",
            "Gas needs the Z-factor (real gas deviation); oil needs solution gas ratio Rs - both from PVT labs.",
            "Buoyancy (density differences) stacks gas/oil/water and drives the saturation-height function.",
        ],
        "requirements": [
            "Convert API gravity to density and hydrostatic gradient; compute column pressure.",
            "Explain Bo and Bg physically: why oil shrinks and gas expands toward surface.",
            "State how viscosity affects flow rate and flood efficiency.",
        ],
        "standards": [
            "PVT definitions per Tiab & Donaldson Ch. 5; API gravity per API standards.",
            "Volume factors dimensionless ratios (RB/STB); gradients in psi/ft with SG stated.",
        ],
        "citations": [C_TIAB, C_ARCHER],
        "sig_lens": (
            "His Signature reading: fluids are shapeshifters - the same oil "
            "is a different substance at every depth, and only the volume "
            "factors tell the truth across the journey. Signature accounting "
            "always converts to common conditions before comparing."
        ),
    },
]

ENTRIES += [
    {
        "key": "darcy_full",
        "name": "Darcy's Law in Full: Linear Flow, Radial Flow, and Units That Matter",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The laboratory form of Darcy's law is only the beginning. In a "
            "reservoir, fluid does not march down a straight core plug - it "
            "converges radially toward the wellbore, accelerating as the "
            "flow area shrinks, which is why well productivity is governed by "
            "the radial form: q = 0.00708 * k * h * (pe - pwf) / (mu * B * "
            "ln(re/rw)) in oilfield units, giving stock-tank barrels per day "
            "directly. The logarithm is the whole story of well testing: "
            "most of the pressure drop happens in the first few feet around "
            "the well, so skin damage (a thin zone of reduced permeability "
            "from drilling mud) can halve production while being invisible "
            "ten feet out. Engineers also meet Darcy's law in its "
            "differential form - velocity equals minus permeability over "
            "viscosity times the pressure gradient - which is the momentum "
            "equation inside every reservoir simulator. And because oilfield "
            "units are a historical attic (millidarcies, centipoise, feet, "
            "psi, barrels), the unit conversion constants (0.001127 for "
            "linear flow, 0.00708 for radial) are not trivia but the working "
            "language: this record teaches both forms, the constants, and "
            "the habit of checking units before trusting any rate."
        ),
        "how_it_works": (
            "Start from the differential form v = -(k/mu) * dp/dx and "
            "integrate over the geometry. For linear flow through constant "
            "area, integration gives q = 0.001127 * k * A * delta_p / (mu * "
            "B * L) with q in STB/day, k in mD, A in ft2, delta_p in psi, mu "
            "in cP, L in ft. For radial flow toward a well, the area shrinks "
            "as 2*pi*r*h, and integrating from the wellbore radius rw to the "
            "drainage radius re gives the logarithmic form with ln(re/rw) in "
            "the denominator - typically around 7 to 8, meaning the "
            "near-wellbore region dominates. The demonstration computes a "
            "well rate from the radial equation for a 100-mD, 50-foot pay "
            "zone under 1,000 psi of drawdown - about 618 STB/day - and shows "
            "how halving the permeability or doubling the viscosity halves "
            "the rate, while doubling the drainage radius barely moves the "
            "logarithm. That insensitivity to re is why drainage area is the "
            "least important variable in the equation and skin is the most "
            "feared."
        ),
        "key_points": [
            "Linear Darcy (lab): q = 0.001127*k*A*dp/(mu*B*L); radial Darcy (well): q = 0.00708*k*h*(pe-pwf)/(mu*B*ln(re/rw)).",
            "The logarithm ln(re/rw) ~ 7-8: most pressure drop is near-wellbore, so skin damage dominates productivity.",
            "Oilfield constants are unit conversions, not physics: 0.001127 (linear) and 0.00708 (radial) for STB/day.",
            "Differential form v = -(k/mu)*grad(p) is the momentum equation inside every reservoir simulator.",
            "Doubling drainage radius barely changes rate (log); halving permeability halves it (linear).",
            "Always carry B (formation volume factor): reservoir barrels are not stock-tank barrels.",
        ],
        "requirements": [
            "Compute a well rate from the radial Darcy equation in oilfield units.",
            "Explain physically why skin near the wellbore hurts more than damage far away.",
            "Convert a linear-flow lab result to field rate units without error.",
        ],
        "standards": [
            "Radial and linear forms per Tiab & Donaldson Ch. 6; oilfield units with constants stated.",
            "Skin discussed qualitatively here; quantitative well-test analysis belongs to pressure-transient records.",
        ],
        "citations": [C_DARCY, C_TIAB, C_ARCHER],
        "sig_lens": (
            "His Signature reading: the logarithm is nature's mercy and "
            "nature's warning - the far reservoir barely matters, the "
            "inches around the well decide everything. Signature work always "
            "finds the logarithm in the problem: the place where small "
            "changes rule."
        ),
    },
    {
        "key": "archie",
        "name": "Archie's Equation: The Master Key to Water Saturation",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "In 1942, Gus Archie of Shell published the empirical relation "
            "that still unlocks every resistivity log on earth. He found "
            "that a rock fully saturated with brine of resistivity Rw has "
            "resistivity Ro = F * Rw, where the formation factor F depends "
            "only on the pore geometry: F = a / phi^m, with the cementation "
            "exponent m near 2 for sandstones. Then he found that replacing "
            "some brine with non-conductive oil raises the resistivity by "
            "exactly the factor Sw^-n: Rt = Ro * Sw^-n, with the saturation "
            "exponent n also near 2. Inverted, Sw = (a * Rw / (phi^m * "
            "Rt))^(1/n) - water saturation from three logs (porosity, deep "
            "resistivity, and Rw from a water zone or the SP log) plus two "
            "exponents from core. The equation's power is its minimalism: it "
            "assumes the rock matrix conducts nothing and all current rides "
            "the brine, which is gloriously true for clean sandstones and "
            "gloriously false for shaly sands and carbonates - the failures "
            "being so instructive that they spawned Waxman-Smits, Simandoux, "
            "and the Indonesia equation (each with its own record). Archie's "
            "equation is the discipline's master key because every "
            "interpretation either uses it or explains why it cannot."
        ),
        "how_it_works": (
            "The workflow runs in three steps. First, find Rw: the "
            "resistivity of the formation brine, from a nearby water-bearing "
            "zone (where Sw = 1 so Rw = Ro * phi^m / a), from the SP log, or "
            "from a produced water sample catalog. Second, get porosity from "
            "the porosity logs and deep resistivity Rt from the laterolog or "
            "induction tool. Third, apply Sw = (a * Rw / (phi^m * Rt))^(1/n) "
            "with a = 1 (or 0.62/0.81 in the Humble/Phillips variants), m "
            "and n from core electrical measurements (default 2 and 2 when "
            "core is absent - the petrophysicist's original sin, confessed "
            "everywhere). The demonstration is the canonical textbook "
            "example: Rw = 0.05 ohm-m, phi = 0.20, Rt = 20 ohm-m, a = m = n "
            "as above - and Sw comes out exactly 0.25, a clean oil reservoir "
            "with 75 percent hydrocarbon saturation. Every later record "
            "either feeds this equation or corrects it."
        ),
        "key_points": [
            "Formation factor F = Ro/Rw = a/phi^m: pore geometry's fingerprint on electrical conduction.",
            "Resistivity index I = Rt/Ro = Sw^-n: replacing brine with oil raises resistivity predictably.",
            "Inverted: Sw = (a*Rw/(phi^m*Rt))^(1/n) - the most-used equation in formation evaluation.",
            "Defaults a=1, m=n=2 are for clean sandstones; carbonates and shaly sands need measured exponents.",
            "Rw must come from a water zone, the SP log, or samples - it is the equation's most fragile input.",
            "Every shaly-sand model (Waxman-Smits, Simandoux, Indonesia) is Archie plus a clay-conductivity correction.",
        ],
        "requirements": [
            "Compute Sw from Rw, phi, Rt with given a, m, n (the canonical 0.25 example).",
            "Derive F from a water zone and explain what m measures physically.",
            "State exactly which assumption fails in shaly sands.",
        ],
        "standards": [
            "Archie's relations per Archie 1942; Humble/Phillips parameter variants noted.",
            "Resistivity in ohm-m; temperature corrections to formation temperature applied before use.",
        ],
        "citations": [C_ARCHIE, C_TIAB, C_ASQUITH],
        "sig_lens": (
            "His Signature reading: Archie found that the rock confesses "
            "through its resistance - the current can only travel where the "
            "water is, so resistance maps the water. Signature inference "
            "works the same way: find what only the truth can carry, and "
            "measure how well it carries."
        ),
    },
    {
        "key": "resistivity_log",
        "name": "Resistivity Logging: Reading Water from Electricity",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Resistivity logs are the eyes of the hunt for hydrocarbons, "
            "because oil and gas are electrical insulators while formation "
            "brine - salty water - conducts. A clean water sand reads a few "
            "ohm-meters; the same sand full of oil reads tens or hundreds. "
            "But the borehole complicates everything: drilling mud invades "
            "the formation, flushing the near-wellbore with mud filtrate, so "
            "a single resistivity reading is meaningless without knowing how "
            "deep it looks. Modern tools therefore read three or more depths "
            "of investigation simultaneously: the shallow (flushed zone, "
            "Rxo), the medium, and the deep (uninvaded zone, Rt). The "
            "separation between them tells the invasion story - and the "
            "movable-hydrocarbon story: if the flushed zone (swept by mud "
            "filtrate) still shows high resistivity, hydrocarbons were there "
            "to be flushed, and the difference between flushed-zone "
            "saturation Sxo and true Sw is the movable oil. Two tool "
            "families dominate: induction tools (no electrodes, work in "
            "non-conductive oil-based mud, read conductivity) and laterologs "
            " (focused electrode currents, work in salty mud, read "
            "resistivity directly, with azimuthal versions imaging the "
            "borehole wall)."
        ),
        "how_it_works": (
            "The induction tool transmits an alternating magnetic field that "
            "induces eddy currents in the formation; the received signal is "
            "proportional to formation conductivity (the reciprocal of "
            "resistivity), with software focusing synthesizing multiple "
            "depths of investigation from one array. The laterolog injects "
            "current from electrodes and uses guard electrodes to focus it "
            "into a thin sheet, measuring resistivity with excellent thin-"
            "bed resolution. Interpretation reads the three curves like a "
            "story: deep Rt goes into Archie's equation for Sw; shallow Rxo "
            "goes into the flushed-zone Archie for Sxo (using mud-filtrate "
            "resistivity Rmf instead of Rw); and movable hydrocarbon is "
            "Sxo - Sw - the oil the filtrate could push, hence the oil a "
            "waterflood could move. The demonstration computes Sxo from Rxo "
            "and Rmf, Sw from Rt and Rw, and the movable fraction - the "
            "number that separates a residual stain from a producible "
            "reservoir."
        ),
        "key_points": [
            "Hydrocarbons insulate; brine conducts: resistivity contrast is the primary hydrocarbon indicator.",
            "Three depths of investigation (shallow/medium/deep) unravel mud-filtrate invasion: Rxo (flushed) vs Rt (uninvaded).",
            "Induction tools (conductivity, oil-based mud) vs laterologs (resistivity, water-based mud, thin beds).",
            "Flushed-zone Archie with Rmf gives Sxo; movable hydrocarbon = Sxo - Sw.",
            "High Rxo with separation from Rt means movable hydrocarbons were flushed - the producibility test.",
            "No separation (all curves together) means no invasion: either impermeable rock or matched salinities.",
        ],
        "requirements": [
            "Compute Sw from Rt/Rw and Sxo from Rxo/Rmf, then the movable fraction.",
            "Explain why three resistivities are needed instead of one.",
            "Choose induction vs laterolog for a given mud type and bed thickness.",
        ],
        "standards": [
            "Tool physics per Ellis & Singer Ch. 4-6 and Hearst et al. Ch. 5-7.",
            "Resistivity in ohm-m at formation temperature; invasion profile sketched before quantification.",
        ],
        "citations": [C_ELLIS, C_HEARST, C_ASQUITH],
        "sig_lens": (
            "His Signature reading: the tool reads at three depths because "
            "the truth has layers - the flushed skin may lie while the deep "
            "formation tells the truth. Signature measurement always probes "
            "at multiple depths and trusts the deepest consistent reading."
        ),
    },
    {
        "key": "sp_log",
        "name": "The SP Log: The Spontaneous Potential",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The spontaneous potential log is the oldest electrical log - "
            "run since the 1930s - and it works with no transmitter at all: "
            "it simply records the natural voltage between an electrode in "
            "the borehole and a reference at surface. That voltage exists "
            "because salty formation water and fresher mud filtrate meet at "
            "the permeable bed, and sodium and chloride ions diffuse across "
            "the boundary at different speeds, separating charge like a "
            "natural battery (the liquid-junction potential), reinforced by "
            "the shale membrane potential where clays act as ion-selective "
            "membranes. The result on the log is unmistakable: the SP "
            "deflects left (negative) opposite permeable beds and stays flat "
            "opposite shales, making it the classic permeability indicator "
            "and shale discriminator. But its quantitative crown is "
            "determining Rw: the static SP (the deflection in a thick clean "
            "bed) satisfies SSP = -K * log10(Rmf/Rw), so with mud-filtrate "
            "resistivity known, Rw - Archie's most fragile input - drops out "
            "of one of the cheapest logs ever run. The SP needs conductive "
            "mud, a salinity contrast, and permeable beds; in oil-based mud "
            "or fresh-mud/salty-formation reversals it goes quiet or flips, "
            "and the interpreter must know why."
        ),
        "how_it_works": (
            "Read the static SP deflection in millivolts opposite a thick, "
            "clean, permeable bed - that is SSP, the full electrochemical "
            "potential. Compute K = 61 + 0.133 * T where T is formation "
            "temperature in Fahrenheit (the Nernst temperature dependence). "
            "Then Rw = Rmf / 10^(-SSP/K): with SSP = -87.6 mV at 200 F and "
            "Rmf = 0.5 ohm-m, Rw = 0.05 ohm-m - the canonical value used in "
            "the Archie demonstration. Corrections apply for thin beds "
            "(deflection not fully developed), shaly beds (suppressed "
            "potential), and temperature (Rmf measured at surface must be "
            "corrected to formation temperature via the Arps formula). The "
            "demonstration computes SSP from K and the resistivity ratio, "
            "then inverts a measured SP deflection back to Rw - the full "
            "round trip the working petrophysicist performs."
        ),
        "key_points": [
            "SP is a natural battery: liquid-junction + shale-membrane potentials from salinity contrast at permeable beds.",
            "Deflects opposite permeable beds, flat opposite shales: the classic permeability/shale indicator.",
            "SSP = -K*log10(Rmf/Rw) with K = 61 + 0.133*T(F): the quantitative path to Rw.",
            "Needs water-based mud and a salinity contrast; dead in oil-based mud, reversed when mud is saltier than formation water.",
            "Thin beds and shaly beds suppress the deflection: corrections required before computing Rw.",
            "Rmf must be temperature-corrected (Arps formula) from surface measurement to formation temperature.",
        ],
        "requirements": [
            "Compute K at formation temperature and invert SSP to Rw.",
            "Explain the two electrochemical components and why shale reads flat.",
            "List three conditions that kill or reverse the SP and how to recognize each.",
        ],
        "standards": [
            "SP theory per Ellis & Singer Ch. 3; Rw-from-SP workflow per Schlumberger chart book (SP-4).",
            "SP in millivolts; polarity convention stated (negative deflection = permeable).",
        ],
        "citations": [C_ELLIS, C_SCHLUM, C_ASQUITH],
        "sig_lens": (
            "His Signature reading: the SP is the formation speaking without "
            "being asked - no transmitter, no signal sent, just the voltage "
            "of two waters meeting. Signature listening starts with the "
            "channels that need no power."
        ),
    },
    {
        "key": "gamma_ray",
        "name": "The Gamma Ray Log: The Shale Detector",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Shales are naturally radioactive - their clays carry potassium-40 "
            "and adsorb uranium and thorium - while clean sandstones and "
            "carbonates are nearly silent. The gamma ray log simply counts "
            "that natural radiation, and the result is the discipline's "
            "universal shale detector: high GR means shale, low GR means "
            "clean reservoir rock, in almost every sedimentary basin on "
            "earth. It works in cased hole, in oil-based mud, through every "
            "mud type - which is why it is the correlation workhorse, the "
            "curve every depth-match starts from. Quantitatively, the GR "
            "index IGR = (GR - GRmin)/(GRmax - GRmin) scales to shale volume "
            "Vsh through transforms that account for the nonlinear "
            "radioactivity-concentration relation: linear (young "
            "unconsolidated), Larionov's exponentials (0.33*(2^(2*IGR)-1) "
            "for older rocks, 0.083*(2^(3.7*IGR)-1) for Tertiary), Stieber, "
            "and Clavier. Spectral gamma ray tools go further, splitting the "
            "signal into potassium, uranium, and thorium - because a uranium "
            "spike in an otherwise clean sand means fractures or organic "
            "richness, not shale, and only the spectral log knows the "
            "difference."
        ),
        "how_it_works": (
            "Pick GRmin in the cleanest sand (or carbonate) and GRmax in the "
            "thickest shale on the log - these anchors are the whole "
            "calibration, and picking them badly is the classic GR error. "
            "Compute IGR, then Vsh: the linear transform is the pessimistic "
            "ceiling (overstates shale), Larionov-older-rocks the standard "
            "for consolidated formations, Larionov-Tertiary for young Gulf-"
            "Coast-type sediments, Stieber sitting between. For the textbook "
            "example GR = 75 API with anchors 20 and 120: IGR = 0.55, linear "
            "Vsh = 0.55, Larionov-older = 0.38, Stieber = 0.29, Larionov-"
            "Tertiary = 0.26 - a spread that shows why transform choice is a "
            "real decision with reserve consequences. Vsh then corrects "
            "porosity (density/neutron shale corrections) and gates the "
            "shaly-sand saturation models. The demonstration computes all "
            "four transforms for one GR reading and ranks them - the daily "
            "judgment call of the working interpreter."
        ),
        "key_points": [
            "GR counts natural radioactivity: shales hot (K/U/Th in clays), clean sands and carbonates quiet.",
            "Works through casing and any mud: the universal correlation and depth-match curve.",
            "IGR = (GR-GRmin)/(GRmax-GRmin); anchors picked in cleanest sand and thickest shale - the critical judgment.",
            "Vsh transforms: linear (max), Larionov older/Tertiary, Stieber - choice changes reserves.",
            "Spectral GR (K/U/Th split) distinguishes true shale from uranium-rich fractures or organic matter.",
            "Vsh feeds porosity shale-corrections and selects the shaly-sand saturation model.",
        ],
        "requirements": [
            "Compute IGR and Vsh by linear, Larionov (both), and Stieber transforms for given anchors.",
            "Explain why a uranium spike can fake a shale and how spectral GR exposes it.",
            "Describe how a bad GRmax pick propagates into reserves.",
        ],
        "standards": [
            "GR in API units; transforms per Larionov 1969, Stieber 1970, Clavier et al. 1977.",
            "Anchor selection documented on the log; transform choice justified by consolidation age.",
        ],
        "citations": [C_ELLIS, C_ASQUITH, C_LARIONOV, C_STIEBER],
        "sig_lens": (
            "His Signature reading: the shale announces itself - it cannot "
            "help glowing - while the reservoir rock stays quiet. Signature "
            "detection looks for what cannot hide its nature, and measures "
            "the quiet things by subtraction."
        ),
    },
    {
        "key": "sonic_log",
        "name": "The Sonic Log: Timing Sound Through Rock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The sonic log fires a pulse of sound across the borehole wall "
            "and times its arrival: the slower the sound, the more pore "
            "space it crossed. Wyllie, Gregory, and Gardner's 1956 time-"
            "average equation - delta_t = phi * delta_tf + (1 - phi) * "
            "delta_tma - treats the rock as sound traveling partly through "
            "fluid and partly through matrix, and inverted it gives porosity "
            "directly: phi_s = (delta_t - delta_tma)/(delta_tf - delta_tma), "
            "with matrix travel times 55.5 us/ft for sandstone, 47.5 for "
            "limestone, 43.5 for dolomite, and fluid time 189 us/ft. It was "
            "the first porosity log and remains the only one that also hears "
            "mechanics: the full-waveform sonic reads compressional, shear, "
            "and Stoneley waves, yielding Poisson's ratio, shear modulus, "
            "and Young's modulus - the elastic properties that feed "
            "fracturing design and sand-production prediction. The sonic's "
            "weaknesses are famous: it reads too high in unconsolidated "
            "sands (needs the compaction correction), it misses vuggy "
            "porosity (sound skips around vugs), and gas makes it read "
            "chaotically (cycle skipping). The Raymer-Hunt-Gardner transform "
            "fixes the high-porosity nonlinearity where Wyllie overshoots."
        ),
        "how_it_works": (
            "Read interval transit time delta_t in microseconds per foot. "
            "Select matrix time for the known lithology (55.5 sandstone "
            "default when unknown) and fluid time 189 for liquid-filled "
            "pores. Apply Wyllie: phi = (90 - 55.5)/(189 - 55.5) = 0.258 for "
            "the textbook delta_t = 90 - or Raymer-Hunt-Gardner phi = "
            "(5/8)*(delta_t - delta_tma)/delta_t = 0.240 for better behavior "
            "in high porosity. In unconsolidated sands multiply by the "
            "compaction factor (often ~1/1.3, calibrated to core); in gas "
            "zones distrust cycle-skipped readings and lean on density-"
            "neutron. Shear-wave velocity from the dipole sonic gives "
            "dynamic elastic moduli: mu = rho * Vs^2, and Poisson's ratio "
            "from Vp/Vs - the geomechanical half of the log that drilling "
            "and completions engineers live on. The demonstration computes "
            "both Wyllie and Raymer-Hunt-Gardner porosities for one transit "
            "time and shows the compaction correction."
        ),
        "key_points": [
            "Wyllie time-average: phi_s = (dt - dtma)/(dtf - dtma); matrix times 55.5/47.5/43.5 us/ft (ss/ls/dolo), fluid 189.",
            "First porosity log; the only porosity tool that also measures elastic moduli (Vp, Vs -> Poisson, shear modulus).",
            "Unconsolidated sands need the compaction correction (Wyllie reads high).",
            "Misses vuggy/secondary porosity (sound bypasses vugs); gas causes cycle skipping - distrust sonic in gas.",
            "Raymer-Hunt-Gardner corrects Wyllie's high-porosity overshoot.",
            "Dipole shear data feeds frac design, wellbore stability, and sanding prediction.",
        ],
        "requirements": [
            "Compute Wyllie and RHG porosity from a transit time; apply a compaction correction.",
            "Explain why sonic misses vugs and misreads gas, with the physical reason each time.",
            "Derive shear modulus and Poisson's ratio from Vp, Vs, and density.",
        ],
        "standards": [
            "Transit time in us/ft; transforms per Wyllie et al. 1956/1958 and Raymer-Hunt-Gardner 1980.",
            "Matrix time matched to lithology from the M-N/crossplot record; gas zones flagged.",
        ],
        "citations": [C_WYLLIE, C_ELLIS, C_HEARST],
        "sig_lens": (
            "His Signature reading: sound is the honest messenger - it "
            "cannot help arriving late through empty space, and its delay "
            "is the porosity confessing. Signature measurement trusts the "
            "messengers that cannot lie about their journey."
        ),
    },
    {
        "key": "density_log",
        "name": "The Density Log: Porosity from Compton Scattering",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The density tool carries a gamma-ray source and counts how many "
            "gamma rays scatter back: Compton scattering is proportional to "
            "electron density, which for most rocks is proportional to bulk "
            "density, which gives porosity by the simplest relation in "
            "petrophysics: phi_d = (rho_ma - rho_b)/(rho_ma - rho_f). With "
            "matrix density 2.65 g/cc for sandstone and fluid density 1.0, "
            "a bulk density reading of 2.20 means 27.3 percent porosity - "
            "one subtraction and one division, the most robust porosity in "
            "the business. The tool rides on a pad pressed against the "
            "borehole wall (shallowest investigation of the porosity tools, "
            "inches deep), so it also reports a density correction curve "
            "(DRHO) that diagnoses bad pad contact and mudcake: high DRHO "
            "means distrust the reading. The photoelectric factor (PEF), "
            "measured by the same tool from low-energy gamma absorption, is "
            "a lithology fingerprint - 1.81 for sandstone, 5.08 for limestone, "
            "3.14 for dolomite, 3.42 for anhydrite - nearly independent of "
            "porosity and fluid. Gas is the density log's famous tell: gas "
            "density near 0.2 g/cc makes the tool read anomalously LOW bulk "
            "density, hence anomalously HIGH porosity - the 'gas effect' "
            "that, paired with the neutron log's opposite response, makes "
            "the classic crossover gas indicator."
        ),
        "how_it_works": (
            "Read bulk density rho_b and the DRHO correction; if DRHO "
            "exceeds about 0.2 g/cc, find better pad contact or a better "
            "hole. Select matrix density for the lithology (2.65 "
            "sandstone, 2.71 limestone, 2.87 dolomite - from the PEF or "
            "crossplot) and fluid density (1.0 for filtrate/mud, 1.1 for "
            "salt mud, ~0.2 for gas). Compute phi_d = (2.65 - 2.20)/(2.65 - "
            "1.0) = 0.273 for the textbook case. In gas zones the same "
            "reading with rho_f = 0.2 gives phi = 0.184 - the fluid-density "
            "assumption swings the answer by nine porosity units, which is "
            "why gas-zone density porosity is always paired with neutron. "
            "Shale correction: subtract Vsh * phi_sh (shale porosity from "
            "an adjacent shale reading). The demonstration computes clean "
            "and gas-case density porosity plus the shale correction - the "
            "three density calculations in every interpretation."
        ),
        "key_points": [
            "phi_d = (rho_ma - rho_f)/(rho_ma - rho_f): the simplest, most robust porosity transform.",
            "Compton scattering -> electron density -> bulk density; pad tool, shallowest porosity investigation.",
            "DRHO correction curve diagnoses pad contact: high DRHO = distrust the reading.",
            "PEF lithology fingerprint: 1.81 ss / 5.08 ls / 3.14 dolo / 3.42 anhydrite - porosity-independent.",
            "Gas effect: low gas density -> anomalously high density porosity; pair with neutron for the crossover.",
            "Matrix density must match lithology; fluid density assumption swings gas-zone answers by ~9 p.u.",
        ],
        "requirements": [
            "Compute density porosity for liquid and gas fluid assumptions; explain the 9-p.u. swing.",
            "Use PEF to identify matrix and select rho_ma.",
            "Apply the shale correction to density porosity.",
        ],
        "standards": [
            "Density in g/cc; matrix/fluid densities stated with every computation.",
            "DRHO quality check performed before any quantitative use (per Schlumberger chart book).",
        ],
        "citations": [C_ELLIS, C_HEARST, C_ASQUITH],
        "sig_lens": (
            "His Signature reading: the density tool weighs the rock without "
            "a scale - it counts scattered light and infers mass. Signature "
            "instruments measure the unmeasurable by a proxy chained to "
            "physics, then print the chain for inspection."
        ),
    },
    {
        "key": "neutron_log",
        "name": "The Neutron Log: The Hydrogen Hunter",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The neutron tool bombards the formation with fast neutrons and "
            "counts how many come back slow: hydrogen - one proton, nearly "
            "the neutron's own mass - is by far the best moderator, so the "
            "tool is essentially a hydrogen counter. Since pore fluids "
            "(water, oil) are hydrogen-rich and rock matrix is not, the "
            "hydrogen index reads porosity - calibrated in limestone porosity "
            "units, the industry standard. But hydrogen is not porosity: "
            "shales carry bound water in their clays (high apparent "
            "porosity), gas carries little hydrogen per unit volume (low "
            "apparent porosity - the famous 'gas effect' that makes neutron "
            "porosity plunge in gas zones), and the tool reads deepest of "
            "the porosity trio. The magic is the pairing: in a liquid-filled "
            "clean formation, density and neutron porosities agree; in gas, "
            "density porosity soars while neutron porosity collapses, and "
            "the two curves cross over on the log - the crossover that has "
            "discovered more gas than any other single indicator. In shales, "
            "both read high together (no crossover), which is how the "
            "interpreter tells shale from gas. Modern pulsed-neutron tools "
            "additionally measure sigma (capture cross-section) for "
            "saturation behind casing - the cased-hole Sw measurement."
        ),
        "how_it_works": (
            "Read apparent neutron porosity in limestone units. In clean "
            "liquid formations it approximates true porosity after a small "
            "lithology correction (sandstone reads ~4 p.u. high on the "
            "limestone scale). Combine with density porosity by the root-"
            "mean-square: phi_xplot = sqrt((phi_d^2 + phi_n^2)/2) - the "
            "standard gas-corrected porosity, because the gas errors are "
            "opposite and roughly cancel. Diagnose by separation: phi_n far "
            "below phi_d with crossover = gas; both high together = shale "
            "(check GR); agreement = clean liquid formation. Excavation "
            "effect: the standard charts already correct for it. The "
            "demonstration computes the combined neutron-density porosity "
            "for a liquid case (0.27, 0.30 -> 0.285) and flags a gas case "
            "by the crossover separation - the two neutron calculations "
            "that matter."
        ),
        "key_points": [
            "Neutron tool = hydrogen counter: fast neutrons thermalized best by hydrogen; reads porosity via hydrogen index.",
            "Calibrated in limestone porosity units; lithology corrections needed for sandstone/dolomite.",
            "Gas effect: low hydrogen density -> neutron porosity collapses in gas (opposite of density's response).",
            "Neutron-density crossover (phi_n << phi_d) is the classic gas indicator; both-high-together means shale.",
            "Shale bound water inflates neutron porosity: correct with Vsh or use the pair diagnostically.",
            "Pulsed-neutron sigma logs measure Sw behind casing - the cased-hole saturation tool.",
        ],
        "requirements": [
            "Compute combined neutron-density porosity and explain the error cancellation in gas.",
            "Distinguish gas crossover from shale response on a log pair.",
            "Explain why neutron porosity is a hydrogen measurement, not a porosity measurement.",
        ],
        "standards": [
            "Neutron porosity in limestone p.u.; lithology corrections per chart book before combination.",
            "Gas diagnosis requires the density pair - never from neutron alone.",
        ],
        "citations": [C_ELLIS, C_HEARST, C_ASQUITH],
        "sig_lens": (
            "His Signature reading: the neutron tool hunts one atom - "
            "hydrogen - and finds water, oil, and gas by its absence or "
            "presence. Signature sensing picks the single atom that matters "
            "and ignores the mountain around it."
        ),
    },
]

ENTRIES += [
    {
        "key": "capillary_intro",
        "name": "Capillary Pressure: The Curved Interface Between Fluids",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Where oil meets water inside a pore, the interface curves - and "
            "a curved interface sustains a pressure difference. That "
            "difference is capillary pressure: Pc = P_nonwetting - P_wetting, "
            "always the non-wetting fluid pushing harder. It is the reason "
            "water rises in a thin glass tube against gravity (Jurin's law: "
            "Pc = 2 * sigma * cos(theta) / r), the reason a reservoir has a "
            "transition zone instead of a sharp oil-water contact, and the "
            "reason small pores stay water-filled while big pores produce "
            "oil. The numbers are humbling: in a one-micron throat with an "
            "oil-water interfacial tension of 30 dynes/cm, Pc is 60 kPa "
            "(8.7 psi) - enough to hold a 30-meter oil column against "
            "buoyancy in a 200 kg/m3 density contrast. Shrink the throat to "
            "0.1 micron and the same interface holds 300 meters: this is why "
            "tight rock has transition zones hundreds of feet tall while "
            "good sand has a sharp contact. Capillary pressure is also the "
            "bridge between the pore scale and the log scale: the drainage "
            "capillary curve measured on a core plug, scaled by the Leverett "
            "J-function, predicts water saturation at every height above the "
            "free-water level - the saturation-height function that fills "
            "reservoir models."
        ),
        "how_it_works": (
            "Jurin's law gives the pore-scale magnitude: Pc = 2 * sigma * "
            "cos(theta) / r. With sigma = 0.03 N/m (oil-water), theta = 0 "
            "(strongly water-wet), r = 1e-6 m: Pc = 60,000 Pa. Convert to a "
            "fluid column: h = Pc / ((rho_w - rho_o) * g) = 60,000 / (200 * "
            "9.81) = 30.6 m - the height of oil column one micron throat can "
            "support. At reservoir scale, equilibrium demands Pc = (rho_w - "
            "rho_hc) * g * h at every height h above the free-water level "
            "(where Pc = 0 by definition), so measuring the Pc-vs-saturation "
            "drainage curve in the lab and inverting it gives Sw at every "
            "elevation: high above the contact the big pores have drained "
            "and Sw approaches Swirr; near the contact Pc is small, only the "
            "biggest throats hold oil, and Sw is high. The demonstration "
            "computes Jurin Pc for two throat sizes and the supportable oil "
            "columns - the pore-to-reservoir scaling in one calculation."
        ),
        "key_points": [
            "Pc = P_nonwetting - P_wetting; curved interfaces sustain pressure differences (Jurin: 2*sigma*cos(theta)/r).",
            "1-micron throat, oil-water: Pc = 8.7 psi, supports 30 m of oil column - the pore scale rules the reservoir scale.",
            "Smaller throats = taller transition zones: tight rock has 100s of feet of transition; good sand has a sharp contact.",
            "At height h above the free-water level: Pc = (rho_w - rho_hc)*g*h - equilibrium ties capillary pressure to elevation.",
            "The lab drainage Pc curve, inverted through this equilibrium, gives Sw at every depth: the saturation-height function.",
            "Pc is always defined non-wetting minus wetting: sign errors here corrupt every saturation-height model.",
        ],
        "requirements": [
            "Compute Jurin Pc for given sigma, theta, r and convert to supportable hydrocarbon column.",
            "Explain why transition-zone height varies inversely with throat size.",
            "State the Pc=0 reference (free-water level) and the equilibrium relation.",
        ],
        "standards": [
            "Pc in psi or Pa with the reference stated; interfacial tension in dynes/cm with fluids named.",
            "Wettability assumption (theta) declared - Pc scales directly with cos(theta).",
        ],
        "citations": [C_TIAB, C_LEVERETT, C_ARCHER],
        "sig_lens": (
            "His Signature reading: the curved interface is a negotiation - "
            "two fluids agreeing on a pressure difference across a membrane "
            "of surface tension. Signature physics reads every boundary as "
            "a negotiation and asks what each side paid."
        ),
    },
    {
        "key": "wettability",
        "name": "Wettability: The Contact Angle That Rules Recovery",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Wettability answers one question: when oil and water share a "
            "pore, which one clings to the rock? In a water-wet rock the "
            "water coats every grain and the oil sits in the pore centers, "
            "free to flow; in an oil-wet rock the oil coats the grains and "
            "water fingers through the centers, leaving oil films that never "
            "produce. The contact angle measured through the water tells the "
            "story: near 0 degrees is strongly water-wet, near 180 is "
            "strongly oil-wet, and the vast middle is mixed- or "
            "intermediate-wet - which, paradoxically, often gives the best "
            "oil recovery, because neither fluid is trapped as a coating. "
            "Wettability quietly controls almost everything downstream: "
            "capillary pressure sign and magnitude (cos theta), relative "
            "permeability curve shapes, residual oil saturation, the "
            "success of waterflooding, and even Archie's saturation exponent "
            "n. And it is fragile: drilling mud filtrate, asphaltene "
            "deposition, and laboratory cleaning can all flip it, which is "
            "why special core analysis labs guard native wettability like a "
            "crime scene. Measured by contact angle (a droplet on a mineral "
            "plate), the Amott test (spontaneous vs forced imbibition "
            "volumes), or the USBM method (work areas under capillary "
            "curves), wettability is the reservoir property most often "
            "assumed and least often measured."
        ),
        "how_it_works": (
            "The Amott-Harvey index is the working measure: imbibe water "
            "spontaneously into an oil-saturated plug and record the "
            "produced oil Vosp; then force-flood and record Vot - the water "
            "index Iw = Vosp/Vot. Repeat with oil displacing water for Io. "
            "The index Iw - Io runs from +1 (strongly water-wet) through 0 "
            "(neutral) to -1 (strongly oil-wet). A plug with Iw = 0.8, Io = "
            "0.1 scores +0.7: water-wet, water imbibes eagerly, oil does "
            "not. The consequences propagate: water-wet relative permeability "
            "shows water mobility rising only at high Sw (water is the "
            "coating, last to flow) and residual oil trapped as center-pore "
            "blobs; oil-wet shows early water breakthrough and high Sor as "
            "films. The demonstration computes the Amott-Harvey index from "
            "imbibition volumes and classifies the rock - the two-minute "
            "version of the laboratory's most guarded measurement."
        ),
        "key_points": [
            "Wettability = which fluid coats the grains: water-wet (oil flows free), oil-wet (oil trapped as films), mixed-wet (often best recovery).",
            "Contact angle through water: ~0 deg water-wet, ~180 deg oil-wet; cos(theta) scales capillary pressure.",
            "Amott-Harvey index = Iw - Io: +1 water-wet, 0 neutral, -1 oil-wet.",
            "Controls rel-perm shapes, Sor, waterflood efficiency, and Archie's n - assumed constantly, measured rarely.",
            "Fragile: mud filtrate, asphaltenes, and lab cleaning can flip it; native-state cores are precious.",
            "USBM method uses capillary-curve work areas; contact angle uses a droplet on a plate.",
        ],
        "requirements": [
            "Compute the Amott-Harvey index from spontaneous/forced imbibition volumes and classify wettability.",
            "Explain why mixed-wet rock often recovers more oil than strongly water-wet rock.",
            "Trace wettability's effect on one downstream property (rel-perm, Sor, or Pc).",
        ],
        "standards": [
            "Amott-Harvey index dimensionless on [-1, +1]; contact angles in degrees through the water phase.",
            "Wettability state (native/restored/cleaned) reported with every SCAL measurement.",
        ],
        "citations": [C_TIAB, C_AMOTT, C_ARCHER],
        "sig_lens": (
            "His Signature reading: wettability is loyalty - the rock "
            "chooses which fluid it loves, and the beloved fluid stays "
            "while the other is free to leave. Signature systems ask what "
            "every surface is loyal to before predicting any flow."
        ),
    },
    {
        "key": "relative_perm",
        "name": "Relative Permeability: Two Fluids Sharing One Rock",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Absolute permeability describes one fluid filling every pore; "
            "reservoirs never oblige. When oil and water share the rock, "
            "each interferes with the other, and each flows as if the rock "
            "had a smaller permeability: the effective permeability. "
            "Relative permeability is the ratio - krw = kw/k, kro = ko/k - "
            "dimensionless curves from 0 to 1 plotted against water "
            "saturation, and they are the single most important input to "
            "every reservoir simulator and waterflood design. Their shape "
            "tells the production story: at Swirr only oil flows (krw = 0); "
            "as water saturation rises, kro falls and krw climbs; past the "
            "crossover, water dominates; at (1 - Sor) oil stops entirely. "
            "The Corey correlations capture the shapes with exponents: krw "
            "= krw0 * Swn^nw, kro = kro0 * (1 - Swn)^no, where Swn is "
            "normalized saturation. The fractional flow of water, fw = 1 / "
            "(1 + (kro * muw)/(krw * muo)), then predicts what comes out of "
            "the well: the Buckley-Leverett theory turns these curves into "
            "the water-breakthrough time and the flood's ultimate recovery. "
            "Measured in the laboratory by steady-state (two pumps, fixed "
            "ratio) or unsteady-state (flood and history-match) methods, "
            "relative permeability is expensive, wettability-sensitive, and "
            "irreplaceable."
        ),
        "how_it_works": (
            "Normalize saturation: Swn = (Sw - Swirr)/(1 - Swirr - Sor). "
            "Apply Corey with laboratory-fitted endpoints and exponents - "
            "the textbook water-wet set: Swirr = 0.20, Sor = 0.25, krw0 = "
            "0.30, kro0 = 0.90, nw = no = 2. At Sw = 0.50: Swn = 0.545, krw "
            "= 0.089, kro = 0.186. Then fractional flow with muw = 0.5 cP, "
            "muo = 2.0 cP: fw = 1/(1 + (0.186*0.5)/(0.089*2.0)) = 0.66 - "
            "two-thirds of the produced fluid is water even though the rock "
            "is only half water-saturated, because water's lower viscosity "
            "makes it more mobile. Sweep Sw from Swirr to (1 - Sor) and the "
            "full curves emerge: kro dying at 0.75, krw born at 0.20. The "
            "demonstration builds both Corey curves and the fractional flow "
            "curve - the complete two-phase flow description from five "
            "laboratory numbers."
        ),
        "key_points": [
            "Relative permeability kr = k_effective/k_absolute: each fluid's share of the flow capacity, 0 to 1 vs Sw.",
            "Endpoints: krw=0 at Swirr (only oil flows); kro=0 at 1-Sor (only water flows); crossover Sw marks the flow regime flip.",
            "Corey: krw = krw0*Swn^nw, kro = kro0*(1-Swn)^no - five lab numbers describe two-phase flow.",
            "Fractional flow fw = 1/(1+(kro*muw)/(krw*muo)): predicts produced water cut; viscosity ratio matters as much as kr.",
            "Curve shapes are wettability fingerprints: water-wet delays water mobility; oil-wet invites early breakthrough.",
            "Buckley-Leverett turns fw(Sw) into breakthrough time and recovery: the waterflood design equation.",
        ],
        "requirements": [
            "Build Corey krw/kro curves from endpoints and exponents; compute fw at a given Sw.",
            "Explain why fw can exceed Sw dramatically (viscosity ratio).",
            "Distinguish steady-state vs unsteady-state laboratory measurement.",
        ],
        "standards": [
            "kr dimensionless vs Sw fraction; endpoints and exponents reported with the curves, never assumed silently.",
            "Wettability state of the test declared - rel-perm without wettability context is decoration.",
        ],
        "citations": [C_TIAB, C_COREY, C_ARCHER],
        "sig_lens": (
            "His Signature reading: two fluids in one rock is a treaty - "
            "each concedes flow paths to the other, and the treaty terms "
            "are written in the curve shapes. Signature sharing problems "
            "are always solved by finding each party's relative permeability."
        ),
    },
    {
        "key": "vsh",
        "name": "Shale Volume: Correcting Logs for Clay",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "No reservoir rock is perfectly clean: dispersed clays coat "
            "grains, laminated shales stripe the sand, and structural shale "
            "replaces sand entirely. All of it is shale volume, Vsh - the "
            "fraction of the rock that is clay - and it poisons every "
            "measurement: shale's bound water inflates neutron porosity, "
            "its conductivity depresses resistivity (faking low Sw in "
            "Archie), its radioactivity is the GR signal itself, and its "
            "softness drags down the sonic. The petrophysicist's response is "
            "correction, not despair: porosity gets the shale correction "
            "(phi_corrected = phi_log - Vsh * phi_sh, with phi_sh read in an "
            "adjacent shale), resistivity gets the shaly-sand saturation "
            "models (Simandoux, Waxman-Smits, Indonesia - each its own "
            "record), and net-pay cutoffs reject rock above Vsh ~ 0.4 as "
            "non-reservoir. Vsh itself comes primarily from the gamma ray "
            "transforms (the dedicated GR record), secondarily from SP "
            "suppression or neutron-density separation, and the interpreter "
            "takes the minimum of the indicators - the classic 'minimum Vsh' "
            "rule - because every method overestimates in its own way. "
            "Getting Vsh right is unglamorous and decisive: a 0.1 error in "
            "Vsh propagates into porosity, saturation, permeability, and "
            "net pay - the entire reserve estimate."
        ),
        "how_it_works": (
            "Take Vsh from the GR transforms (Larionov-older = 0.38 in the "
            "textbook example). Read shale porosity phi_sh = 0.05 in the "
            "adjacent shale from the density log. Correct the density "
            "porosity: phi_dc = 0.273 - 0.38*0.05 = 0.254 - nearly two "
            "porosity units recovered from the shale's inflation. The same "
            "Vsh gates the saturation model choice: below ~0.1 use Archie; "
            "0.1-0.4 use a shaly-sand model; above 0.4 the rock is shale, "
            "not reservoir, and no saturation is computed. For laminated "
            "shales the Thomas-Stieber model goes further, correcting for "
            "the geometry of the laminations rather than just the volume. "
            "The demonstration applies the density shale correction and the "
            "model-selection gate - the two Vsh calculations that run in "
            "every interpretation."
        ),
        "key_points": [
            "Vsh = clay fraction: poisons porosity (bound water), resistivity (conductivity), sonic (softness).",
            "Density shale correction: phi_corrected = phi_d - Vsh*phi_sh, with phi_sh from an adjacent shale.",
            "Minimum-Vsh rule: take the smallest of GR/SP/neutron-density indicators - each overestimates differently.",
            "Vsh gates the saturation model: <0.1 Archie, 0.1-0.4 shaly-sand models, >0.4 not reservoir.",
            "Dispersed vs laminated vs structural shale need different corrections (Thomas-Stieber for laminations).",
            "A 0.1 Vsh error propagates into phi, Sw, k, and net pay - the whole reserve.",
        ],
        "requirements": [
            "Apply the density shale correction given Vsh and adjacent-shale porosity.",
            "State the model-selection gate thresholds and the reasoning behind each.",
            "Explain the minimum-Vsh rule and why each indicator overestimates.",
        ],
        "standards": [
            "Vsh as a fraction; phi_sh measured in adjacent shale on the same log, not assumed.",
            "Shale geometry (dispersed/laminated/structural) identified before choosing the correction model.",
        ],
        "citations": [C_ASQUITH, C_TIAB, C_CRAIN],
        "sig_lens": (
            "His Signature reading: shale is the impurity that must be "
            "weighed before the pure can be known - the correction is an "
            "act of honesty, subtracting what was never reservoir. Signature "
            "measurement always assays the impurity first."
        ),
    },
    {
        "key": "quicklook",
        "name": "Quick-Look Interpretation: Formation Evaluation in Five Minutes",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Before the computers, before the probabilistic inversions, the "
            "petrophysicist does the quick look: five minutes with the "
            "log, a pencil, and the discipline's greatest hits, answering "
            "'is this worth my week?' The choreography is fixed. One: "
            "lithology and shale - GR for Vsh, PEF/crossplot for matrix. "
            "Two: porosity - density and neutron, shale-corrected, "
            "combined by root-mean-square, gas flagged by crossover. Three: "
            "Rw - from the SP in a clean water zone or a known aquifer. "
            "Four: resistivity - deep Rt for Sw via Archie (or a shaly-sand "
            "model if Vsh demands it), Rxo/Rt separation for movable "
            "hydrocarbons. Five: the verdict - cutoffs (phi, Vsh, Sw) "
            "applied, pay flagged, hydrocarbon pore volume estimated. The "
            "quick look is deliberately approximate: its job is triage, not "
            "booking reserves. But its discipline is the discipline - every "
            "shortcut it takes (default m=n=2, Larionov Vsh, Wyllie or "
            "density porosity) is a conscious IOU, written down, to be "
            "repaid by the full interpretation. This record is the capstone "
            "of the compounded tier because it uses every tool record that "
            "came before it in one continuous workflow."
        ),
        "how_it_works": (
            "The worked zone: GR = 60 API (anchors 20/120) -> IGR = 0.40 -> "
            "Larionov-older Vsh = 0.245. Density rho_b = 2.25 -> phi_d = "
            "0.242, shale-corrected to 0.230. Sonic dt = 80 -> phi_s = 0.184; "
            "average porosity 0.207. SP = -70 mV at 200 F (K = 87.6), Rmf = "
            "0.5 -> Rw = 0.079. Deep Rt = 25 ohm-m -> Archie Sw = 0.27 with "
            "m = n = 2. Cutoffs: phi 0.207 > 0.10 pass, Vsh 0.245 < 0.40 "
            "pass, Sw 0.27 < 0.60 pass - PAY, with hydrocarbon pore volume "
            "phi*(1-Sw) = 0.151 per unit bulk volume. Every number carries "
            "its IOU: m=n=2 assumed (repay with core), Vsh transform chosen "
            "(repay with XRD), no gas check done (repay with the "
            "neutron-density pair). The demonstration runs this exact chain "
            "- the five-minute interpretation, computed."
        ),
        "key_points": [
            "Quick-look order: lithology/Vsh -> porosity -> Rw -> resistivity/Sw -> cutoffs/verdict.",
            "Five minutes, pencil, greatest hits: triage, not reserve booking - every shortcut is a documented IOU.",
            "Worked example: Vsh 0.245, phi 0.207, Rw 0.079, Sw 0.27 -> PAY by all three cutoffs.",
            "Uses every compounded-tier record: GR, density, sonic, SP, resistivity, Archie, Vsh, cutoffs.",
            "Default m=n=2 and chosen Vsh transform are the standard IOUs, repaid by core and full interpretation.",
            "The verdict is binary (pay/no-pay) but the IOU list is the real product of the quick look.",
        ],
        "requirements": [
            "Run the full quick-look chain on given log readings and render a pay/no-pay verdict.",
            "List the IOUs in a quick look and what repays each.",
            "Explain why the order (Vsh before phi before Sw) is not arbitrary.",
        ],
        "standards": [
            "Quick-look results labeled preliminary; cutoffs stated explicitly (phi/Vsh/Sw).",
            "Every defaulted parameter flagged as an IOU per the discipline's honesty standard.",
        ],
        "citations": [C_ASQUITH, C_RIDER, C_CRAIN],
        "sig_lens": (
            "His Signature reading: the quick look is triage medicine - "
            "decide in five minutes whether the patient deserves the week, "
            "and write down every assumption so the week can check them. "
            "Signature speed never skips the ledger of debts."
        ),
    },
    {
        "key": "crossplots",
        "name": "Crossplots: The M-N, Pickett, and Hingle Plots",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A log curve shows one measurement against depth; a crossplot "
            "shows two measurements against each other, and the patterns "
            "that emerge identify minerals, porosity, and saturation more "
            "surely than any single curve. The M-N plot is the lithology "
            "detective: M = (dtf - dt)/(rho_b - rho_f) * 0.01 and N = "
            "(phiNf - phiN)/(rho_b - rho_f) combine sonic, density, and "
            "neutron into coordinates where sandstone (0.81, 0.64), "
            "limestone (0.83, 0.59), and dolomite (0.78, 0.49) sit at fixed "
            "points - plot the zone, see which mineral point it lands on, "
            "read porosity off the diagonal lines. The Pickett plot is "
            "Archie's equation drawn: log(Rt) vs log(phi) is a straight "
            "line of slope -m at constant Sw, so water zones define the "
            "100%-Sw line (intercept = a*Rw) and hydrocarbon zones plot "
            "above it - Sw read by interpolation between the lines, m read "
            "from the slope, Rw from the intercept, all without a single "
            "assumed parameter. The Hingle plot (resistivity vs transit "
            "time on special scales) does the same linearization for the "
            "sonic. Crossplots are where the interpreter stops assuming "
            "and starts measuring: m, Rw, and lithology come out of the "
            "data instead of going in."
        ),
        "how_it_works": (
            "M-N example: dt = 60 us/ft, rho_b = 2.50 g/cc, phiN = 0.10 -> "
            "M = (189-60)/(2.50-1.0)*0.01 = 0.86, N = (1.0-0.10)/(2.50-1.0) "
            "= 0.60. Distances to the mineral points: limestone (0.83, "
            "0.59) at 0.032, sandstone (0.81, 0.64) at 0.064, dolomite "
            "(0.78, 0.49) at 0.136 - the zone is limestone, and the "
            "diagonal porosity lines read ~10 p.u. Pickett construction: "
            "plot water-zone points (Sw=1) on log-log axes; the best-fit "
            "line's slope is -m and its phi=1 intercept is a*Rw; draw "
            "parallel Sw lines (each factor of Sw^-n upward); drop the pay "
            "zone's (phi, Rt) point and read Sw between the lines. The "
            "demonstration computes the M-N coordinates, identifies the "
            "mineral by nearest point, and verifies the Pickett slope-to-m "
            "relation on synthetic water-zone data."
        ),
        "key_points": [
            "Crossplots trade depth for pattern: two measurements against each other reveal what one curve cannot.",
            "M-N plot: (M, N) from sonic/density/neutron; mineral points fixed - nearest point identifies lithology, diagonals give porosity.",
            "Pickett plot: log(Rt) vs log(phi); slope = -m, intercept = a*Rw, Sw by interpolation - Archie without assumed parameters.",
            "Hingle plot: same linearization using sonic transit time instead of porosity.",
            "Water zones must be present to anchor the Pickett line - no water leg, no calibration.",
            "Crossplots convert assumed inputs (m, Rw, lithology) into measured outputs.",
        ],
        "requirements": [
            "Compute M-N coordinates and identify the mineral by nearest fixed point.",
            "Explain how a Pickett plot yields m, Rw, and Sw from the same graph.",
            "State what data a Pickett plot requires to be calibratable.",
        ],
        "standards": [
            "Mineral M-N points per Schlumberger chart book; Pickett construction per Pickett 1966/1973.",
            "Lithology from crossplot confirmed by PEF before use in transforms.",
        ],
        "citations": [C_PICKETT, C_SCHLUM, C_DOVETON],
        "sig_lens": (
            "His Signature reading: the crossplot is the discipline's "
            "honesty device - instead of feeding assumptions in, it lets "
            "the data confess the parameters. Signature analysis always "
            "builds one plot where the inputs become outputs."
        ),
    },
    {
        "key": "routine_core",
        "name": "Routine Core Analysis: Measuring the Rock Directly",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Every log transform in this database is a confession that the "
            "interpreter is not holding the rock - routine core analysis is "
            "what happens when they are. Plugs drilled from whole core go "
            "through the standard battery: dimensions and weights for bulk "
            "volume and porosity (helium expansion for grain volume, "
            "saturation weighing for pore volume), gas permeability with the "
            "Klinkenberg correction to liquid-equivalent, Dean-Stark retort "
            "for saturations, and sieve or laser analysis for grain size. "
            "The laboratory's first product is calibration: core porosity "
            "corrects the log porosity transforms (that density matrix "
            "density of 2.65 is a guess until core confirms it), core "
            "permeability anchors the log-derived permeability correlations, "
            "and the core's own Archie measurements (F vs phi, I vs Sw) "
            "supply the m and n the quick look merely assumed. The second "
            "product is ground truth for the poro-perm relationship of that "
            "specific reservoir - the trend that turns a porosity map into "
            "a flow map. Core is expensive, sparse (inches sampled from "
            "miles), and altered by the journey to surface (stress relief "
            "opens microfractures, mud invades, gas escapes) - so the "
            "petrophysicist treats it as the honored but imperfect witness, "
            "corrected for overburden stress and depth-shifted to the logs "
            "before any comparison."
        ),
        "how_it_works": (
            "The plug battery, worked: a 3-inch plug (L = 7.62 cm, D = 3.81 "
            "cm) has bulk volume 86.87 cc; dry weight 195.0 g and saturated "
            "weight 208.3 g give pore volume 13.3 cc and porosity 0.153; "
            "grain density 195/(86.87-13.3) = 2.65 g/cc confirms clean "
            "quartz. Gas permeability at three mean pressures (120, 110, "
            "105 mD at 1, 2, 4 atm) extrapolates linearly against 1/pm to "
            "k_inf = 100 mD - the Klinkenberg correction removing gas slip. "
            "Depth-shift the plug to the log by matching core gamma to log "
            "gamma; stress-correct permeability to reservoir net stress "
            "(typically a 20-50% reduction from ambient lab conditions); "
            "then crossplot core phi vs log phi and fit the correction. "
            "The demonstration runs the full plug battery - porosity, grain "
            "density check, and Klinkenberg extrapolation - the three "
            "numbers every core report opens with."
        ),
        "key_points": [
            "Routine core = the plug battery: porosity, Klinkenberg permeability, retort saturations, grain size.",
            "First product: calibration - core phi corrects log transforms; core electrical tests supply Archie's m and n.",
            "Second product: the reservoir's own poro-perm trend, turning porosity maps into flow maps.",
            "Klinkenberg: plot kg vs 1/pm, extrapolate to infinite pressure for liquid-equivalent k.",
            "Core is altered (stress relief, invasion, gas escape): stress-correct and depth-shift before comparing to logs.",
            "Sparse and expensive: inches sampled from miles - core calibrates the continuous log, never replaces it.",
        ],
        "requirements": [
            "Compute plug porosity and grain density; use grain density as a lithology check.",
            "Perform the Klinkenberg extrapolation from three gas-perm measurements.",
            "Explain stress correction and depth-shifting and why each is mandatory.",
        ],
        "standards": [
            "Laboratory practice per API RP 40; Klinkenberg correction standard on all gas perms.",
            "Core-log comparison only after depth-shift (core gamma) and stress correction.",
        ],
        "citations": [C_TIAB, C_ARCHER, C_DOVETON],
        "sig_lens": (
            "His Signature reading: the core is the witness brought into "
            "the courtroom - honored, cross-examined (stress, invasion, "
            "shifting), and believed only where its story holds. Signature "
            "evidence always names its witness's wounds."
        ),
    },
    {
        "key": "shaly_sand",
        "name": "Shaly Sands: Waxman-Smits, Simandoux, and the Indonesia Equation",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Archie's equation assumes the rock matrix conducts nothing - "
            "and clay shatters that assumption. Clay minerals carry bound "
            "water loaded with exchangeable cations, and that bound water "
            "conducts electricity, adding a parallel conductive path the "
            "clean-sand Archie never budgeted. The symptom is unmistakable: "
            "Archie computed in a shaly sand overestimates water saturation "
            "(the extra conductivity fakes extra water), potentially "
            "condemning a pay zone that is actually hydrocarbon-bearing. "
            "Three corrections dominate practice. Simandoux (1963) adds the "
            "shale conductivity as a parallel term: 1/Rt = "
            "(phi^m*Sw^n)/(a*Rw*(1-Vsh)) + Vsh*Sw/Rsh - simple, needs only "
            "Vsh and shale resistivity. Waxman-Smits (1968) models the "
            "physics: the clay's cation exchange capacity per unit pore "
            "volume (Qv) adds (B*Qv) to the brine conductivity in a "
            "rigorous electrochemical equation - the most correct, needing "
            "laboratory CEC data. The Indonesia equation of Poupon and "
            "Leveaux (1971) is the empirical workhorse of Southeast Asia: "
            "1/sqrt(Rt) = (Vsh^(1-Vsh/2)/sqrt(Rsh) + "
            "phi^(m/2)/sqrt(a*Rw)) * Sw^(n/2) - no CEC needed, robust where "
            "it was tuned. Choosing among them is the shaly-sand art: "
            "Simandoux for quick work, Waxman-Smits where CEC exists, "
            "Indonesia where the rocks resemble its home basin."
        ),
        "how_it_works": (
            "The textbook comparison: phi = 0.25, Rt = 8 ohm-m, Rw = 0.05, "
            "Vsh = 0.30, Rsh = 4, a = 1, m = n = 2. Clean Archie gives Sw = "
            "0.316 - but the shale is conducting, so this is pessimistic. "
            "Simandoux: 1/8 = (0.0625*Sw^2)/(0.05*0.70) + 0.30*Sw/4, i.e. "
            "1.786*Sw^2 + 0.075*Sw - 0.125 = 0, yielding Sw = 0.244 - seven "
            "saturation units less water, which at 25 percent porosity is "
            "nearly two extra hydrocarbon-filled porosity units of pay. "
            "Waxman-Smits would refine this with measured Qv (typically "
            "lowering Sw further toward the truth in dispersed-clay sands), "
            "and the Indonesia equation gives its own answer tuned to its "
            "basin. The demonstration solves the Simandoux quadratic and "
            "shows the Archie-vs-corrected gap - the pay that clay was "
            "hiding."
        ),
        "key_points": [
            "Clay's bound water conducts: Archie in shaly sand overestimates Sw, hiding pay.",
            "Simandoux: parallel shale conductivity term; needs Vsh and Rsh - the quick correction.",
            "Waxman-Smits: cation exchange capacity Qv in a rigorous electrochemical model - needs lab CEC.",
            "Indonesia equation: empirical, CEC-free, tuned to SE Asian shaly sands - the regional workhorse.",
            "Worked gap: Archie Sw 0.316 vs Simandoux 0.244 - seven saturation units of hidden hydrocarbon.",
            "Model choice is the art: Simandoux (fast), Waxman-Smits (correct, needs CEC), Indonesia (basin-tuned).",
        ],
        "requirements": [
            "Solve the Simandoux equation for Sw and compare against clean Archie.",
            "Explain physically why clay conductivity fakes water saturation.",
            "Choose the right shaly-sand model for three data-availability scenarios.",
        ],
        "standards": [
            "Shaly-sand models per Simandoux 1963, Waxman & Smits 1968, Poupon & Leveaux 1971.",
            "Vsh and Rsh (or Qv/CEC) stated; clean-Archie comparison shown to quantify the correction.",
        ],
        "citations": [C_SIMANDOUX, C_WAXMAN, C_POUPON, C_CLAVIER],
        "sig_lens": (
            "His Signature reading: the clay is a second citizen the census "
            "forgot - it conducts, it counts, and every honest equation "
            "must give it its term. Signature models never let an "
            "unmodeled conductor vote in secret."
        ),
    },
]

ENTRIES += [
    {
        "key": "scal",
        "name": "Special Core Analysis: The Expensive Truth",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Routine core analysis measures the rock's static properties; "
            "special core analysis (SCAL) measures its behavior - how fluids "
            "move, trap, and fight inside the pores under reservoir "
            "conditions. The SCAL battery is the most expensive laboratory "
            "work in petrophysics because it is slow (a single capillary "
            "pressure curve can take weeks), delicate (wettability must be "
            "preserved or restored at reservoir temperature with live "
            "fluids), and irreplaceable: capillary pressure curves "
            "(drainage and imbibition, by porous plate, centrifuge, or "
            "mercury injection), relative permeability (steady- and "
            "unsteady-state oil-water and gas-oil), wettability (Amott and "
            "USBM at conditions), and electrical properties (m, n, Qv/CEC at "
            "reservoir stress and temperature). The porous-plate method is "
            "the gold standard for capillary pressure - a water-wet ceramic "
            "plate passes water but not oil below its entry pressure, so "
            "stepping the oil pressure and waiting for equilibrium maps "
            "Pc vs Sw point by patient point. The centrifuge is the fast "
            "alternative - spinning the plug creates a Pc gradient along "
            "its length, trading speed for the Hassler-Brunner inversion "
            "mathematics. Mercury injection is the fastest and most "
            "destructive: mercury, the ultimate non-wetting fluid, invades "
            "ever-smaller throats as pressure rises to 60,000 psi, mapping "
            "the throat-size distribution that predicts permeability - but "
            "the plug can never be used for anything else afterward. SCAL "
            "data feeds the reservoir simulator directly: Pc curves become "
            "saturation-height functions, rel-perm becomes the flow "
            "equations, and the whole field development plan quietly rests "
            "on a few plugs measured with obsessive care."
        ),
        "how_it_works": (
            "A drainage capillary curve is fitted with the Brooks-Corey "
            "model: Pc = Pd * Se^(-1/lambda), where Se = (Sw - Swirr)/(1 - "
            "Swirr) is effective saturation, Pd the displacement (entry) "
            "pressure, and lambda the pore-size-distribution index. Two "
            "laboratory points determine both: (Sw = 0.50, Pc = 10 psi) and "
            "(Sw = 0.30, Pc = 40 psi) with Swirr = 0.20 give Se = 0.375 and "
            "0.125; ln(40/10) = -(1/lambda)*ln(0.125/0.375), so lambda = "
            "0.79; then Pd = 10 * 0.375^(1/0.79) = 2.9 psi. Lambda near 1 "
            "means uniform throats (good sorting); lambda near 0.3 means a "
            "wide throat distribution (poor sorting, high Swirr). Pd is the "
            "largest throat's entry pressure - the minimum buoyancy needed "
            "to start oil invasion. The demonstration performs this exact "
            "two-point Brooks-Corey fit - the reduction of weeks of porous-"
            "plate patience to two reservoir parameters."
        ),
        "key_points": [
            "SCAL measures behavior (Pc, rel-perm, wettability, electrical) at reservoir conditions - slow, delicate, irreplaceable.",
            "Porous plate: gold standard, weeks per curve; centrifuge: fast, needs inversion math; mercury: fastest, destroys the plug.",
            "Brooks-Corey: Pc = Pd*Se^(-1/lambda); Pd = entry pressure of the largest throat, lambda = throat-size uniformity.",
            "Lambda ~1: well-sorted, uniform throats; lambda ~0.3: wide distribution, poor sorting, high Swirr.",
            "SCAL feeds the simulator directly: Pc curves -> saturation-height functions; rel-perm -> flow equations.",
            "Native wettability must be preserved: wrong wettability makes every SCAL number a different rock's answer.",
        ],
        "requirements": [
            "Fit Brooks-Corey Pd and lambda from two Pc-Sw points; interpret lambda geologically.",
            "Compare porous-plate, centrifuge, and mercury methods on speed, accuracy, and sample fate.",
            "Explain why SCAL at ambient conditions with cleaned plugs can mislead.",
        ],
        "standards": [
            "SCAL practice per API RP 40; Brooks-Corey per Brooks & Corey 1964.",
            "Wettability state, stress, temperature, and fluids reported with every SCAL dataset.",
        ],
        "citations": [C_BROOKS, C_TIAB, C_PURCELL],
        "sig_lens": (
            "His Signature reading: SCAL is patience as an instrument - "
            "weeks of waiting for a pressure step to equilibrate, because "
            "the rock's truth cannot be hurried. Signature laboratories "
            "budget time the way others budget money."
        ),
    },
    {
        "key": "pc_curves",
        "name": "Capillary Pressure Curves: Drainage, Imbibition, and the Leverett J-Function",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A capillary pressure curve is the rock's autobiography of fluid "
            "invasion: drainage (non-wetting fluid displacing wetting - oil "
            "migrating into a water-filled reservoir) follows one path, "
            "imbibition (wetting fluid displacing non-wetting - waterflooding "
            "oil out) follows another, and the hysteresis loop between them "
            "is the trapping story - the oil left behind as disconnected "
            "blobs is residual oil saturation, read straight off the "
            "imbibition endpoint. But a laboratory curve is measured on one "
            "plug with one fluid pair, and the reservoir needs Sw at every "
            "height in every rock type: the Leverett J-function is the "
            "scaling law that makes one curve serve all. J(Sw) = (Pc / "
            "(sigma * cos(theta))) * sqrt(k/phi) is dimensionless - "
            "capillary pressure normalized by interfacial forces and pore "
            "geometry - and rocks of similar pore structure share one "
            "J-curve regardless of their absolute permeability. Measure J "
            "vs Sw once on representative plugs, then at any reservoir "
            "location compute Pc from J, k, and phi, set it equal to the "
            "buoyancy (rho_w - rho_hc)*g*h, and read Sw at that height. "
            "Laboratory fluid pairs also need conversion: a mercury-air "
            "curve (sigma = 480 dynes/cm, theta = 140 deg) converts to "
            "reservoir oil-water (sigma = 30, theta = 30 deg) by the ratio "
            "of (sigma*cos(theta)) - typically shrinking lab pressures by "
            "an order of magnitude, because mercury's surface tension is "
            "brutal compared to oil-water's."
        ),
        "how_it_works": (
            "The conversions, worked: a mercury-air Pc of 100 psi becomes "
            "reservoir oil-water Pc = 100 * (30*cos(30 deg))/(480*|cos(140 "
            "deg)|) = 100 * 25.98/367.68 = 7.07 psi - the lab's harsh "
            "numbers tamed to reservoir gentleness. The J-function example: "
            "Pc = 5 psi, sigma = 30 dynes/cm, theta = 0, k = 100 mD, phi = "
            "0.20 -> J = (5/30)*sqrt(100/0.20) = 3.73, dimensionless and "
            "portable to any plug sharing the pore structure. In the "
            "saturation-height workflow the direction reverses: from the "
            "J-curve at the zone's Swirr, compute Pc = J*sigma*cos(theta)*"
            "sqrt(phi/k), equate to buoyancy for height h, and march down "
            "the curve - each J value is a depth, each depth a saturation. "
            "The demonstration performs the mercury-to-reservoir conversion "
            "and one J-function evaluation - the two scalings every "
            "capillary dataset passes through."
        ),
        "key_points": [
            "Drainage vs imbibition hysteresis: the loop's imbibition endpoint is residual oil saturation - trapping made visible.",
            "Leverett J(Sw) = (Pc/(sigma*cos(theta)))*sqrt(k/phi): dimensionless, shared by rocks of similar pore structure.",
            "J-function workflow: lab curve -> J -> reservoir Pc at any (k, phi) -> buoyancy -> Sw at every height.",
            "Fluid-pair conversion by (sigma*cos(theta)) ratio: mercury-air 100 psi ~= oil-water 7 psi.",
            "One representative J-curve serves a whole rock type: the SCAL-to-model multiplier.",
            "Hysteresis means the saturation history matters: drainage Sw and imbibition Sw at the same Pc differ.",
        ],
        "requirements": [
            "Convert a mercury-air Pc curve to reservoir oil-water conditions.",
            "Compute J from Pc, sigma, theta, k, phi and explain its dimensionless portability.",
            "Read Sor from an imbibition curve endpoint and explain the trapping mechanism.",
        ],
        "standards": [
            "J-function per Leverett 1941; fluid-pair conversions with sigma/theta of both pairs stated.",
            "Drainage vs imbibition labeled on every curve; hysteresis never averaged away.",
        ],
        "citations": [C_LEVERETT, C_PURCELL, C_TIAB],
        "sig_lens": (
            "His Signature reading: the J-function is the discovery that "
            "different rocks tell the same story at different volumes - "
            "normalize away the size and the truth is one curve. Signature "
            "scaling always looks for the dimensionless story underneath."
        ),
    },
    {
        "key": "nmr",
        "name": "NMR Logging: T2 Distributions and the Bound-Fluid Cutoff",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Nuclear magnetic resonance logging is the only log that sees "
            "pore SIZE, not just pore volume. Hydrogen nuclei in the pore "
            "fluids are aligned by a permanent magnet, tipped by a radio-"
            "frequency pulse, and their signal decays as the nuclei relax - "
            "and the relaxation time T2 is proportional to pore size, "
            "because fluid molecules near grain surfaces relax fast (short "
            "T2, small pores, bound water) while molecules in pore centers "
            "relax slowly (long T2, large pores, free fluid). The T2 "
            "distribution is therefore a pore-size distribution measured a "
            "mile underground: the area under the whole curve is total "
            "porosity (lithology-independent - no matrix assumption, the "
            "NMR's superpower), the area below the T2 cutoff (33 ms in "
            "sandstones, 92 ms in carbonates) is bound-fluid volume BVI, "
            "and the area above is free-fluid volume FFI - movable fluid "
            "identified without Archie, without Rw, without resistivity. "
            "The Timur-Coates equation turns the ratio into permeability: k "
            "= (phi/10)^4 * (FFI/BVI)^2 with phi in percent - because the "
            "free-to-bound ratio measures exactly what permeability needs: "
            "how much of the pore space is big connected pores versus small "
            "clinging ones. NMR also sees viscosity (heavy oil relaxes "
            "fast, faking bound fluid - the interpreter's trap) and, in "
            "advanced modes, separates oil from water by diffusion contrast."
        ),
        "how_it_works": (
            "The worked example: a T2 distribution with 40% of its area "
            "below 33 ms and 60% above, total NMR porosity 0.25. BVI = 0.10, "
            "FFI = 0.15 - ten porosity units of bound water, fifteen of "
            "movable fluid, no Archie required. Timur-Coates permeability: "
            "k = (25/10)^4 * (0.15/0.10)^2 = 39.06 * 2.25 = 87.9 mD - a "
            "permeability from pore-size proportions, independent of any "
            "poro-perm trend. The log-mean T2 (the distribution's "
            "geometric mean) tracks mean pore size and correlates with "
            "capillary pressure: short T2lm means high Pc, tall transition "
            "zones. Quality checks: the total NMR porosity must roughly "
            "match density-neutron porosity (if not, suspect gas or heavy "
            "oil), and the wait time must be long enough to polarize the "
            "slowest fluids (long T2 needs long waits - rushed logging "
            "loses the big pores). The demonstration computes BVI/FFI "
            "split, Timur-Coates k, and the T2lm - the three NMR numbers "
            "that matter."
        ),
        "key_points": [
            "T2 relaxation time proportional to pore size: short T2 = small pores/bound fluid, long T2 = big pores/free fluid.",
            "T2 distribution = underground pore-size distribution; total area = lithology-independent porosity (no matrix assumption).",
            "T2 cutoff (33 ms sandstone, 92 ms carbonate) splits BVI (bound) from FFI (free/movable) - producibility without Archie.",
            "Timur-Coates: k = (phi%/10)^4 * (FFI/BVI)^2 - permeability from pore-size proportions.",
            "Heavy oil relaxes fast and fakes bound fluid; gas needs wait-time care - know the fluid before trusting the split.",
            "T2lm (log mean) tracks mean pore size and predicts capillary behavior.",
        ],
        "requirements": [
            "Split a T2 distribution into BVI/FFI at the cutoff and compute Timur-Coates permeability.",
            "Explain why NMR porosity needs no matrix assumption while density porosity does.",
            "Diagnose heavy-oil and gas effects on the T2 distribution.",
        ],
        "standards": [
            "T2 in ms; cutoff stated per lithology (33/92 ms); NMR porosity compared against density-neutron as a quality check.",
            "Wait time adequate for the longest T2 present (per Kenyon 1997).",
        ],
        "citations": [C_KENYON, C_TIMUR, C_COATES, C_ELLIS],
        "sig_lens": (
            "His Signature reading: NMR listens to the hydrogen atoms "
            "confess how much room they have to dance - the small rooms "
            "hush them quickly, the grand halls let them ring. Signature "
            "sensing measures freedom by how long the signal sings."
        ),
    },
    {
        "key": "borehole_imaging",
        "name": "Borehole Imaging: Photographing the Formation Wall",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Every log in this database averages over feet of formation; "
            "borehole imaging shows the wall itself. Microresistivity "
            "imagers press pads of button electrodes against the borehole "
            "and map conductivity contrasts at sub-inch resolution; "
            "acoustic imagers scan with ultrasound and map hardness and "
            "borehole shape. The result is a 360-degree unrolled photograph "
            "of the rock: bedding planes appear as sinusoids (a plane "
            "cutting a cylinder unrolls to a sine wave), fractures as dark "
            "continuous sinusoids (conductive, open) or bright ones "
            "(resistive, cemented), vugs as dark spots, and breakouts - "
            "where stress has spalled the wall - as dark vertical bands "
            "marking the minimum horizontal stress direction. Dip and "
            "azimuth come from the sinusoid: dip = arctan(sinusoid height / "
            "borehole diameter), azimuth from the trough's position on the "
            "unrolled image. In carbonates, where fractures carry the flow, "
            "the imager is the reservoir description: fracture density, "
            "aperture, and orientation feed the discrete fracture network "
            "that the simulator flows. In clastics it maps sedimentary "
            "structures - cross-bedding azimuths for paleocurrent, slumps, "
            "and the thin beds the conventional logs averaged away."
        ),
        "how_it_works": (
            "The worked measurement: a bedding sinusoid with peak-to-trough "
            "height 0.60 m in a 0.20 m diameter borehole gives dip = "
            "arctan(0.60/0.20) = arctan(3.0) = 71.6 degrees - a steeply "
            "dipping bed, with azimuth read from where the trough sits on "
            "the 0-360 degree unrolled image (trough at 180 deg means dip "
            "azimuth 180, i.e., dipping south). Fractures are picked the "
            "same way: a dark (conductive) sinusoid crossing the full image "
            "is an open fracture, its aperture estimated from the "
            "conductivity anomaly; a bright sinusoid is calcite-cemented "
            "and hydraulically dead. Breakout analysis: two dark vertical "
            "bands 180 degrees apart mark wall failure at the azimuth of "
            "minimum horizontal stress - the geomechanical compass for "
            "orienting horizontal wells and predicting sanding. The "
            "demonstration computes dip from sinusoid geometry and "
            "classifies sinusoids as bedding, open fracture, or cemented "
            "fracture - the imager's three daily judgments."
        ),
        "key_points": [
            "Imagers unroll the borehole wall at sub-inch resolution: microresistivity (conductivity) or acoustic (hardness/shape).",
            "Planes become sinusoids: dip = arctan(height/diameter), azimuth from trough position.",
            "Dark continuous sinusoids = open (conductive) fractures; bright = cemented (dead); spots = vugs.",
            "In carbonates the imager IS the reservoir description: fracture density/aperture/orientation -> flow network.",
            "Breakouts (dark vertical bands) mark minimum horizontal stress azimuth - the geomechanical compass.",
            "Sees the thin beds and sedimentary structures conventional logs average away.",
        ],
        "requirements": [
            "Compute dip and dip azimuth from a sinusoid's height and trough position.",
            "Distinguish open fractures, cemented fractures, bedding, and breakouts on an image.",
            "Explain why imagers matter most in carbonates and what they feed (fracture network).",
        ],
        "standards": [
            "Dips in degrees with azimuth; image orientation (magnetic vs true north) stated.",
            "Fracture picks classified conductive/resistive with aperture estimates where quantified.",
        ],
        "citations": [C_RIDER, C_HEARST, C_ELLIS],
        "sig_lens": (
            "His Signature reading: the imager stops averaging and looks - "
            "after a database of proxies, here is a photograph. Signature "
            "wisdom knows when to stop inferring and simply open its eyes."
        ),
    },
    {
        "key": "formation_testing",
        "name": "Formation Testing: Pressure Points and Permeability from Drawdown",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The wireline formation tester presses a probe against the "
            "borehole wall, seals a tiny interval with a packer, and either "
            "withdraws a small fluid sample (drawdown) or lets the formation "
            "flow into a chamber - then watches the pressure recover. From "
            "that humble operation come three treasures. One: formation "
            "pressure at the probe depth, accurate to a few psi - string "
            "enough points together and the pressure-vs-depth gradient "
            "reveals fluid contacts (gradient breaks where oil meets water) "
            "and compartmentalization (offset gradients = sealed fault "
            "blocks). Two: permeability from the drawdown and buildup "
            "transient - spherical flow into the probe gives k = (q*mu)/"
            "(4*pi*r_p*delta_p), and the mobility k/mu grades the rock's "
            "flow quality foot by foot. Three: actual fluid samples - the "
            "only direct hydrocarbon evidence short of production, "
            "analyzed for composition, GOR, and contamination. Modern "
            "pump-out testers add downhole fluid analysis: optical "
            "spectrometry identifying oil vs water vs gas in real time, so "
            "the sample is captured only when clean. The tester's "
            "limitation is its shallow investigation - inches to feet - so "
            "its pressure is the near-wellbore truth, and supercharging "
            "(mud overbalance inflating the reading) must be diagnosed and "
            "corrected."
        ),
        "how_it_works": (
            "The worked drawdown: withdraw q = 1e-6 m3/s of 1-cP fluid "
            "through a 1-cm-radius probe, measuring delta_p = 100 kPa of "
            "drawdown. Spherical-flow permeability k = q*mu/(4*pi*r_p*"
            "delta_p) = 1e-9/(4*pi*0.01*1e5) = 7.96e-14 m2 = 0.081 mD - a "
            "tight zone, with mobility k/mu = 81 mD/cP. The pressure survey "
            "is the bigger prize: plot ten such points vs depth; a straight "
            "line of slope 0.433*SG psi/ft is one fluid column, a slope "
            "break is a contact, and a parallel-offset line is a "
            "compartment at different pressure. Drawdown mobility profiles "
            "(k/mu vs depth) flag the barriers: a zero-mobility streak is a "
            "seal, confirmed by the pressure offset across it. The "
            "demonstration computes spherical-flow permeability and "
            "mobility from a drawdown test - the tester's core calculation."
        ),
        "key_points": [
            "Formation tester: probe + packer + drawdown/buildup -> pressure, permeability, fluid samples at each depth.",
            "Pressure-vs-depth gradients reveal fluid contacts (slope breaks) and compartments (offset lines).",
            "Spherical-flow k from drawdown; mobility k/mu profiles flag seals and barriers foot by foot.",
            "Downhole fluid analysis (optical spectrometry) captures samples only when clean - contamination managed live.",
            "Shallow investigation (inches-feet): the near-wellbore truth; supercharging from mud overbalance must be corrected.",
            "The only direct fluid evidence short of production: samples analyzed for composition and GOR.",
        ],
        "requirements": [
            "Compute spherical-flow permeability and mobility from drawdown data.",
            "Read fluid contacts and compartmentalization from a pressure-vs-depth plot.",
            "Explain supercharging and how to diagnose it.",
        ],
        "standards": [
            "Pressures at formation conditions; gradients in psi/ft with fluid SG inferred.",
            "Contamination fraction reported with every sample; supercharging check standard.",
        ],
        "citations": [C_MORAN, C_TIAB, C_HEARST],
        "sig_lens": (
            "His Signature reading: the tester knocks on the rock's door "
            "and listens to how hard it is to draw breath - pressure is "
            "the reservoir's pulse, and a finger on the pulse at ten depths "
            "maps the whole body. Signature diagnosis always takes the "
            "pulse in many places."
        ),
    },
    {
        "key": "saturation_height",
        "name": "Saturation-Height Functions: Mapping the Transition Zone",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A reservoir is not oil-down-to-a-line: above the free-water "
            "level (where capillary pressure is zero) there is a transition "
            "zone where water saturation falls gradually from 100 percent "
            "to irreducible, and the zone's height is the capillary story "
            "told at reservoir scale. The saturation-height function is "
            "that story quantified: Sw as a function of height above the "
            "free-water level, built from laboratory capillary pressure "
            "curves through the equilibrium relation Pc = (rho_w - "
            "rho_hc)*g*h. At each height, buoyancy sets Pc; the drainage Pc "
            "curve (or its Brooks-Corey fit, or its J-function scaling) "
            "inverts Pc to Sw. In good rock (big throats, low Pd) the "
            "transition is a sharp step - ten feet from water to Swirr. In "
            "tight rock (small throats, high Pd) it sprawls for hundreds of "
            "feet, and wells drilled 'high' on structure can still produce "
            "mostly water. Reservoir models are initialized with these "
            "functions: every grid cell gets Sw from its elevation and its "
            "rock type's curve, so the model's oil-in-place honors both the "
            "capillary physics and the log-measured saturations. The "
            "function also quality-controls the logs: where log Sw and "
            "saturation-height Sw disagree, something is wrong - usually "
            "the Rw, the contact pick, or the rock typing."
        ),
        "how_it_works": (
            "Build it from the Brooks-Corey fit of the SCAL record (Pd = "
            "2.9 psi = 20,000 Pa, lambda = 0.79, Swirr = 0.20) with an "
            "oil-water density contrast of 200 kg/m3. At Sw = 0.50: Se = "
            "0.375, Pc = 20,000 * 0.375^(-1/0.79) = 68,960 Pa, so h = "
            "68,960/(200*9.81) = 35.1 m above the free-water level. Near "
            "irreducible (Sw = 0.25, Se = 0.0625): Pc = 668,600 Pa, h = "
            "341 m - the transition zone sprawls because the small throats "
            "demand enormous capillary pressure to drain. Plot Sw vs h and "
            "the field's vertical saturation profile emerges: sharp in "
            "good rock, smeared in tight rock. Initialize the model by "
            "evaluating this function at each cell's height; then compare "
            "against log Sw at the wells - agreement validates Rw, contact, "
            "and rock type in one check. The demonstration computes the "
            "two heights above - the transition zone's bottom and top."
        ),
        "key_points": [
            "Saturation-height function: Sw vs height above free-water level, from lab Pc curves via Pc = (rho_w - rho_hc)*g*h.",
            "Good rock: sharp transition (feet); tight rock: sprawling transition (hundreds of feet) - throat size rules.",
            "Initializes reservoir models: every cell's Sw from its elevation and rock-type curve - physics-honoring oil in place.",
            "Quality-controls the logs: log-Sw vs function-Sw disagreement indicts Rw, the contact pick, or rock typing.",
            "Free-water level (Pc=0) is the reference; perched and tilted contacts complicate the ideal picture.",
            "Built per rock type: one function per J-curve family, applied where that rock type lives.",
        ],
        "requirements": [
            "Compute Sw at given heights above FWL from a Brooks-Corey Pc fit.",
            "Explain why transition-zone height varies with rock quality.",
            "Use a saturation-height mismatch to diagnose which input is wrong.",
        ],
        "standards": [
            "Heights referenced to the free-water level; density contrast and Pc curve source stated.",
            "One function per rock type; model initialization documented per cell.",
        ],
        "citations": [C_LEVERETT, C_BROOKS, C_TIAB],
        "sig_lens": (
            "His Signature reading: the transition zone is the shoreline "
            "of the underground sea - not a line but a beach, wide where "
            "the sand is fine. Signature maps always draw the beach, never "
            "just the waterline."
        ),
    },
    {
        "key": "perm_from_logs",
        "name": "Permeability from Logs: Morris-Biggs, Coates, and the Flow-Zone Indicator",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "No log measures permeability directly - the discipline's "
            "lasting frustration - so permeability from logs is always a "
            "correlation, and the honest interpreter treats every value as "
            "a calibrated estimate wearing its error bars. Three families "
            "dominate. Empirical poro-perm transforms (Timur 1968 and its "
            "kin) fit core k against core phi and Swirr: Morris & Biggs "
            "(1967) gave the enduring form k = (100*phi^2.25/Swirr)^2 with "
            "phi as a fraction - at phi = 0.20, Swirr = 0.25 this yields "
            "114 mD, a credible sandstone. NMR-derived permeability "
            "(Timur-Coates, the NMR record) replaces Swirr with the "
            "FFI/BVI ratio - the pore-size argument made directly. And the "
            "hydraulic flow-unit approach (Amaefule's flow-zone indicator) "
            "reorganizes the Kozeny-Carman equation: RQI = 0.0314*sqrt(k/"
            "phi) is the reservoir quality index in microns, phi_z = "
            "phi/(1-phi) the normalized porosity, and FZI = RQI/phi_z is "
            "constant within a hydraulic unit - so rocks group by FZI, "
            "each group gets its own poro-perm trend, and the scatter that "
            "defeated single-trend correlations collapses. Tixier (1949) "
            "even coaxed permeability from resistivity gradients. The "
            "workflow is always: calibrate to core in the cored wells, "
            "apply by rock type in the uncored wells, and never show a "
            "log-derived permeability without its calibration crossplot."
        ),
        "how_it_works": (
            "Morris-Biggs, worked: phi = 0.20, Swirr = 0.25 (from NMR or "
            "core) -> k = (100 * 0.20^2.25 / 0.25)^2 = (10.67)^2 = 113.9 "
            "mD. Flow-zone indicator on the same rock: RQI = 0.0314 * "
            "sqrt(113.9/0.20) = 0.749 microns; phi_z = 0.20/0.80 = 0.25; "
            "FZI = 0.749/0.25 = 3.0 microns - this rock's hydraulic "
            "fingerprint. In practice: compute FZI at every core plug, "
            "histogram it, cluster into hydraulic units (each a distinct "
            "FZI band), fit a k-vs-phi trend per unit, then assign units "
            "in uncored wells from logs (GR, density-neutron separation, "
            "NMR T2lm) and apply the unit's trend. A single global trend "
            "through mixed rock types is the classic error - it honors no "
            "rock and predicts none. The demonstration computes "
            "Morris-Biggs k and the FZI fingerprint - the estimate and its "
            "rock-typing passport."
        ),
        "key_points": [
            "No log measures k directly: every log permeability is a calibrated correlation with honest error bars.",
            "Morris-Biggs: k = (100*phi^2.25/Swirr)^2 - the enduring empirical workhorse (114 mD at phi 0.20, Swirr 0.25).",
            "Timur-Coates (NMR): k from FFI/BVI - the pore-size argument made directly (see NMR record).",
            "Flow-zone indicator: FZI = RQI/phi_z constant per hydraulic unit - group rocks by FZI, fit trends per unit.",
            "Calibrate to core in cored wells; apply by rock type in uncored wells; show the calibration crossplot always.",
            "Single global poro-perm trends through mixed rock types honor no rock - unit-based trends are the fix.",
        ],
        "requirements": [
            "Compute Morris-Biggs permeability and the FZI fingerprint from phi, Swirr, k.",
            "Explain the hydraulic-unit workflow: cluster, fit per unit, apply by unit.",
            "State why log-derived k must always carry its calibration.",
        ],
        "standards": [
            "Log-k labeled estimated with method named; calibration crossplot (core vs log) required.",
            "FZI in microns; hydraulic units defined by FZI bands with geological meaning.",
        ],
        "citations": [C_MORRIS, C_TIMUR, C_COATES, C_TIXIER],
        "sig_lens": (
            "His Signature reading: permeability from logs is the "
            "discipline admitting what it cannot see and estimating anyway "
            "- but honestly, with the calibration on display. Signature "
            "estimation always shows its receipt."
        ),
    },
    {
        "key": "net_pay",
        "name": "Net Pay and Cutoffs: Deciding What Counts as Reservoir",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A thousand feet of logged interval is not a thousand feet of "
            "reservoir: net pay is the thickness that actually counts - "
            "porous enough, clean enough, hydrocarbon-filled enough to "
            "produce - and cutoffs are the three gates it must pass. The "
            "industry-standard gates: porosity above ~0.08-0.10 (below "
            "this the rock cannot flow economically), shale volume below "
            "~0.40 (above this it is shale, not reservoir), and water "
            "saturation below ~0.50-0.60 (above this it produces water, not "
            "oil). Apply them foot by foot: each depth sample passes or "
            "fails, consecutive passes sum to net pay, and the pay's average "
            "porosity and saturation give hydrocarbon pore volume HCPV = "
            "sum(h * phi * (1 - Sw)) - the volumetrics numerator that, "
            "times area and divided by Bo, becomes oil in place. Cutoffs "
            "are economic judgments wearing geological clothes: a high oil "
            "price lowers the Sw cutoff, a tight-rock play lowers the "
            "permeability cutoff, and every cutoff choice moves reserves. "
            "Net-to-gross (net pay over gross interval) then describes the "
            "reservoir's architecture: 0.9 is a blanket sand, 0.2 is "
            "stringers in shale. This record is the discipline's bottom "
            "line - everything measured upstream converges on the pay flag."
        ),
        "how_it_works": (
            "The worked interval: five 10-foot zones with (phi, Vsh, Sw) = "
            "(0.22, 0.10, 0.25), (0.18, 0.20, 0.35), (0.06, 0.15, 0.30), "
            "(0.20, 0.50, 0.30), (0.16, 0.25, 0.70). Cutoffs phi >= 0.08, "
            "Vsh <= 0.40, Sw <= 0.60. Zone 1 passes all three; zone 2 "
            "passes; zone 3 fails porosity; zone 4 fails Vsh; zone 5 fails "
            "Sw. Net pay = 20 ft of 50 (net-to-gross 0.40). Pay-averaged "
            "phi = 0.20, pay Sw = 0.30, HCPV = 10*0.22*0.75 + 10*0.18*0.65 "
            "= 1.65 + 1.17 = 2.82 ft of pure hydrocarbon column - the "
            "number volumetrics multiplies by area. Sensitivity: relaxing "
            "the Sw cutoff to 0.75 would admit zone 5 (+10 ft pay, but "
            "water-prone); tightening phi to 0.15 keeps the same pay here "
            "but bites in marginal rock. The demonstration runs this exact "
            "screening - the pay decision, computed."
        ),
        "key_points": [
            "Net pay = thickness passing all three cutoffs: phi (usually >= 0.08-0.10), Vsh (<= ~0.40), Sw (<= ~0.50-0.60).",
            "Applied foot by foot; consecutive passes sum to pay; pay averages give HCPV = sum(h*phi*(1-Sw)).",
            "Cutoffs are economic judgments in geological dress: prices and play type move them, and they move reserves.",
            "Net-to-gross describes architecture: 0.9 blanket sand vs 0.2 stringers in shale.",
            "HCPV times area over Bo is oil in place: net pay is the volumetrics bottleneck.",
            "Every upstream measurement converges here: the pay flag is the discipline's bottom line.",
        ],
        "requirements": [
            "Screen zones against cutoffs, sum net pay, compute net-to-gross and HCPV.",
            "Explain how changing each cutoff moves reserves and who decides the values.",
            "Trace one pay-foot's data lineage back through phi, Vsh, and Sw records.",
        ],
        "standards": [
            "Cutoff values stated explicitly with every net-pay map; sensitivity to cutoff choice shown.",
            "Pay computed on depth-matched, shale-corrected, quality-checked inputs only.",
        ],
        "citations": [C_ASQUITH, C_CRAIN, C_ARCHER],
        "sig_lens": (
            "His Signature reading: cutoffs are the moment judgment enters "
            "measurement - three gates, and the rock either passes or does "
            "not. Signature decisions name their gates out loud, so the "
            "judgment can be audited later."
        ),
    },
    {
        "key": "interpretation_workflows",
        "name": "Petrophysical Interpretation Workflows: Deterministic Against Probabilistic",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "All the instruments and equations of this database converge on "
            "one question: how does the working petrophysicist actually "
            "combine them into an answer - and how honest is the answer "
            "about its own uncertainty? The deterministic workflow is the "
            "classic chain: pick GR anchors, compute Vsh, correct porosity, "
            "derive Rw, apply Archie or a shaly-sand model, screen cutoffs - "
            "each step one number in, one number out, fast, transparent, "
            "and silently certain. Its weakness is exactly that silence: "
            "the Sw = 0.27 it reports used m = n = 2, and if m is really "
            "2.2 the truth is 0.31 - the deterministic answer never says "
            "so. The probabilistic workflow (exemplified by multi-mineral "
            "inversion solvers) treats every measurement as uncertain and "
            "every parameter as a distribution: it solves for mineral "
            "volumes, porosity, and saturations simultaneously, honoring "
            "all logs at once, and reports P10/P50/P90 - the answer with "
            "its doubt attached. The Monte Carlo check is the bridge: "
            "sample phi, Rt, m, n from their uncertainties through Archie's "
            "equation a few thousand times and watch Sw spread around the "
            "deterministic value - the five-minute uncertainty analysis "
            "that every deterministic interpretation deserves. The "
            "discipline's mature posture: deterministic for speed and "
            "insight, probabilistic for booking and risking, Monte Carlo "
            "to keep the deterministic honest."
        ),
        "how_it_works": (
            "The Monte Carlo honesty check, worked: Archie with Rw = 0.05, "
            "Rt = 20, m = n = 2, but phi drawn from N(0.20, 0.01) and Rt "
            "from N(20, 1) - realistic measurement scatter. Two thousand "
            "samples: the deterministic Sw = 0.25 sits at the distribution's "
            "center, P50 = 0.25, with P10 = 0.22 and P90 = 0.28 - the "
            "answer is 0.25 plus-or-minus three saturation units from "
            "measurement noise alone, before any parameter uncertainty. "
            "Add m uniform on [1.8, 2.2] and the spread doubles: the "
            "parameter you assumed dominates the error you ignored. The "
            "probabilistic solver generalizes this: instead of chaining "
            "single values, it inverts the full log suite for mineralogy, "
            "porosity, and fluids jointly, weighting each measurement by "
            "its precision. The demonstration runs the Monte Carlo - the "
            "deterministic answer, with its doubt attached."
        ),
        "key_points": [
            "Deterministic workflow: chained single-value steps (Vsh -> phi -> Rw -> Sw -> cutoffs) - fast, transparent, silently certain.",
            "Probabilistic workflow: joint inversion of all logs for minerals/porosity/fluids - reports P10/P50/P90, doubt attached.",
            "Monte Carlo through Archie: phi/Rt noise alone spreads Sw 0.22-0.28 around the 0.25 deterministic answer.",
            "Parameter uncertainty (m, n, Rw) typically dominates measurement noise - the assumed hurts more than the measured.",
            "Mature posture: deterministic for speed and insight, probabilistic for booking and risking, Monte Carlo to stay honest.",
            "The capstone record: every tool, transform, and correction in this database appears in one of the two workflows.",
        ],
        "requirements": [
            "Run a Monte Carlo Sw uncertainty from phi/Rt distributions and report P10/P50/P90.",
            "Contrast deterministic and probabilistic workflows on speed, transparency, and uncertainty handling.",
            "Identify which uncertainty source dominates a given interpretation.",
        ],
        "standards": [
            "Uncertainty reported with every booked number (P10/P50/P90 or equivalent); deterministic answers labeled as central estimates.",
            "Workflow choice (deterministic/probabilistic) documented with its justification.",
        ],
        "citations": [C_DOVETON, C_TIAB, C_CRAIN],
        "sig_lens": (
            "His Signature reading: the deterministic answer is a promise, "
            "the probabilistic answer is a promise with its doubts listed "
            "- and Signature engineering only books promises whose doubts "
            "are written down. Uncertainty is not the enemy of the answer; "
            "hidden uncertainty is."
        ),
    },
]
