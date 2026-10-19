#!/usr/bin/env python3
"""Record content for the Unsolved Mechanical Engineering databases
(Manon 2026-10-17 16:15 orders, Unsolved Problems Solved series).

34 real, fact-checked unsolved mechanical engineering problems across
turbulence control, friction and wear prediction, metamaterial
manufacturing at scale, soft robotics control, and energy-harvesting
efficiency limits - ladder-ordered 1 (approachable) to 34 (advanced).

Every signature solution opens with the exact honesty label and never
claims proof or peer acceptance. Where the honest answer is "we do not
know," it says so and states what would be needed to know.

Standing exclusions honored: civilian problems only (nothing on
neutralizing or defeating military or defense-grade systems), no
religious talk, nothing hate-adjacent or profane, no website or
Facebook references.
"""

SIG_LABEL = ("Signature-generated proposed solution \u2014 not established "
             "science.")

SIG_TAIL = ("Signature edition: his original Signature Engineering Method - "
            "a proposed solution approach, honesty-labeled, clearly labeled "
            "Signature-made and never presented as established science or "
            "authentic public record.")

ENTRIES = [
    # ---------------------------------------------------------- approachable
    {
        "key": "bearing-life",
        "name": "Bearing Life Prediction Under Real Conditions",
        "group": "Friction and Wear",
        "ladder_rank": 1,
        "ladder_tier": "approachable",
        "problem": ("How to predict the real service life of a rolling-element "
                    "bearing under the messy conditions of actual machines. The "
                    "standard L10 life formula assumes clean oil, constant load, "
                    "and ideal geometry, yet real bearings see contamination, "
                    "varying loads, misalignment, and temperature swings that can "
                    "cut life by a factor of ten - or extend it - in ways no "
                    "standard predicts reliably."),
        "background": ("Rolling-element bearings fail mostly by rolling-contact "
                       "fatigue: subsurface cracks that grow into spalls. Arvid "
                       "Palmgren and Gustaf Lundberg published the statistical "
                       "theory behind the L10 rating life in 1947, and it became "
                       "ISO 281, the rating every bearing catalog still prints. "
                       "ISO 281 was later extended with life-modification factors "
                       "for lubrication, contamination, and load, but the factors "
                       "are calibrated on clean laboratory rigs. In the field, "
                       "studies repeatedly show most bearings are replaced for "
                       "reasons other than classical fatigue - contamination, "
                       "poor fits, electrical erosion from variable-frequency "
                       "drives - and vibration-based remaining-life estimates can "
                       "disagree by an order of magnitude. The gap between the "
                       "catalog number and the machine reality is the unsolved "
                       "part."),
        "why_it_matters": ("Bearings sit inside nearly every rotating machine on "
                           "earth, from wind turbines to dental drills. Guessing "
                           "life wrong means either catastrophic unplanned "
                           "failures or throwing away healthy bearings on fixed "
                           "schedules. A trustworthy real-condition life model "
                           "would cut maintenance cost and downtime across "
                           "industry."),
        "citations": [
            "Lundberg, G. and Palmgren, A. Dynamic Capacity of Rolling Bearings. "
            "Ingeniorsvetenskapsakademien, Handlingar No. 196, Stockholm; 1947.",
            "ISO 281:2007. Rolling bearings - Dynamic load ratings and rating life.",
            "Harris, T. A. and Kotzalas, M. N. Rolling Bearing Analysis, 5th ed. "
            "CRC Press; 2006.",
        ],
        "sig_pointer": ("The Signature approach treats catalog life as only the "
                        "starting bid and layers field-calibrated contamination, "
                        "load-spectrum, and temperature modifiers on top, "
                        "updated live from the machine own vibration record."),
        "sig": {
            "assumptions": ("Catalog L10 is a valid baseline for clean "
                            "steady conditions. Field life is dominated by a "
                            "small number of measurable modifiers - "
                            "contamination level, load spectrum, misalignment, "
                            "temperature - that multiply rather than add."),
            "reasoning": ("Instead of refining the fatigue integral further, "
                          "re-frame life as a running product of the baseline and "
                          "continuously updated modifiers. Each modifier is tied "
                          "to a sensor the machine already has or can cheaply "
                          "get: oil particle counts, motor current signature, "
                          "housing temperature."),
            "mechanism": ("A three-layer estimator: layer one computes L10 from "
                          "the load spectrum; layer two applies contamination "
                          "and lubrication modifiers from oil and temperature "
                          "data; layer three corrects with a vibration-trend "
                          "residual trained on that specific machine family. "
                          "The output is a life distribution, not a single "
                          "number, with the widest uncertainty where data is "
                          "thinnest."),
            "confirm": ("Instrumented field trials where the estimator median "
                        "life lands within a factor of two of observed "
                        "replacement life across at least three machine "
                        "families."),
            "kill": ("If the vibration-trend residual adds no predictive power "
                     "over the catalog modifiers on blind field data, the "
                     "third layer is wrong and the approach reduces to a "
                     "better-calibrated ISO 281."),
            "notclaim": ("This does not claim to predict individual bearing "
                         "failures or to replace inspection. It claims only a "
                         "better-calibrated statistical life, and we do not "
                         "yet know whether cheap field sensors carry enough "
                         "signal; a controlled contamination test program "
                         "would be needed to find out."),
        },
        "demo_spec": {
            "approach": ("Layer catalog L10 life with a load modifier and a "
                         "contamination modifier to get a field-realistic life "
                         "estimate."),
            "assume": [("L10_catalog_mrev", 90.0, "million rev"),
                       ("load_ratio", 1.2, "-"),
                       ("contam_factor", 0.4, "-"),
                       ("speed_rpm", 1500.0, "rpm")],
            "derived": [
                ("L10_adj_mrev", "L10_catalog_mrev / (load_ratio ** 3)"),
                ("L10_field_mrev", "L10_adj_mrev * contam_factor"),
                ("L10_field_hours", "L10_field_mrev * 1e6 / (speed_rpm * 60.0)"),
                ("life_cut_pct", "(1.0 - L10_field_mrev / L10_catalog_mrev) * 100.0"),
            ],
            "confirm": ("Field trials show median life within a factor of two "
                        "of the layered estimate across three machine families."),
            "refute": ("Blind field data shows the vibration residual adds no "
                       "predictive power over catalog modifiers."),
        },
    },
    {
        "key": "fouling",
        "name": "Heat-Exchanger Fouling Prediction",
        "group": "Energy Harvesting and Thermal",
        "ladder_rank": 2,
        "ladder_tier": "approachable",
        "problem": ("How to predict, before building, how fast a heat exchanger "
                    "will foul - the buildup of scale, biofilm, or deposits that "
                    "strangles heat transfer. Designers still add crude fouling "
                    "margins from 1950s tables, which means most exchangers are "
                    "oversized, over-pumped, and cleaned on guesswork schedules."),
        "background": ("Fouling adds a thermal resistance in series with the "
                       "clean heat-transfer coefficient, and the classic Kern "
                       "and Seaton model of 1959 described it as deposition "
                       "minus removal. That was nearly seventy years ago, and "
                       "design practice has barely moved: the TEMA fouling "
                       "resistances engineers still use date to mid-century "
                       "field surveys. Fouling is estimated to cost industry "
                       "billions per year in extra energy and cleaning, and in "
                       "crude-oil preheat trains a few tenths of a millimeter of "
                       "deposit can raise fuel use measurably. Laboratory "
                       "fouling rigs do not reproduce plant hydrodynamics, so "
                       "their rates rarely transfer, and the coupling between "
                       "chemistry, microbiology, and local shear remains "
                       "unmodeled in any general way."),
        "why_it_matters": ("Heat exchangers move a large fraction of the world "
                           "industrial heat. Predicting fouling would let plants "
                           "build smaller exchangers, clean them only when "
                           "needed, and stop burning extra fuel to push heat "
                           "through deposits - a direct energy and emissions win."),
        "citations": [
            "Kern, D. Q. and Seaton, R. E. A Theoretical Analysis of Thermal "
            "Surface Fouling. British Chemical Engineering, vol. 4; 1959.",
            "Bott, T. R. Fouling of Heat Exchangers. Elsevier; 1995.",
            "Muller-Steinhagen, H. (ed.) Heat Exchanger Fouling and Cleaning: "
            "Fundamentals and Applications. Engineering Conferences "
            "International; 2003.",
        ],
        "sig_pointer": ("The Signature approach treats fouling as a local "
                        "deposition-removal race driven by wall shear and "
                        "surface energy, and sizes cleaning from a fouling "
                        "number computed per tube pass instead of one "
                        "plant-wide margin."),
        "sig": {
            "assumptions": ("Deposition and removal can be separated at the "
                            "tube-pass scale. Wall shear stress is the "
                            "dominant mechanical control, and surface energy "
                            "the dominant chemical control."),
            "reasoning": ("The 1950s tables fail because they average over "
                          "the whole exchanger while fouling is local - the "
                          "hottest, slowest tubes foul first. Model the race "
                          "per pass, then integrate, and the plant margin "
                          "becomes a computed distribution instead of a "
                          "table lookup."),
            "mechanism": ("A per-pass fouling number combining local shear, "
                          "temperature, and surface-energy terms, calibrated "
                          "against a small library of fluid chemistries. "
                          "Cleaning is scheduled when the computed resistance "
                          "crosses an economic threshold - the point where "
                          "extra pumping and lost heat cost more than the "
                          "cleaning - rather than on a calendar."),
            "confirm": ("Pilot exchangers instrumented per pass where the "
                        "predicted fouling curve matches measured resistance "
                        "growth within 25 percent over a full operating "
                        "campaign."),
            "kill": ("If per-pass predictions scatter no better than the "
                     "TEMA table values on blind plant data, the local-race "
                     "model adds nothing and the problem stays empirical."),
            "notclaim": ("This does not claim a universal fouling law; "
                         "biofouling in particular couples to biology the "
                         "model does not resolve. We do not know the "
                         "calibration library is wide enough - that needs a "
                         "multi-fluid test campaign."),
        },
        "demo_spec": {
            "approach": ("Compute clean vs fouled heat transfer and the "
                         "economic cleaning threshold from a per-pass "
                         "fouling resistance."),
            "assume": [("U_clean", 1200.0, "W/m2K"),
                       ("R_foul", 0.0005, "m2K/W"),
                       ("area_m2", 50.0, "m2"),
                       ("dT_K", 40.0, "K")],
            "derived": [
                ("U_fouled", "1.0 / (1.0 / U_clean + R_foul)"),
                ("Q_clean_W", "U_clean * area_m2 * dT_K"),
                ("Q_fouled_W", "U_fouled * area_m2 * dT_K"),
                ("duty_loss_pct", "(1.0 - Q_fouled_W / Q_clean_W) * 100.0"),
            ],
            "confirm": ("Instrumented pilot exchangers match the predicted "
                        "resistance growth within 25 percent over a campaign."),
            "refute": ("Per-pass predictions scatter no better than the "
                       "mid-century TEMA table values on blind plant data."),
        },
    },
    {
        "key": "gear-fatigue",
        "name": "Gear Contact Fatigue Prediction",
        "group": "Friction and Wear",
        "ladder_rank": 3,
        "ladder_tier": "approachable",
        "problem": ("How to predict when a gear tooth flank will pit or spall "
                    "under real duty cycles. Hertz worked out the contact "
                    "stresses in 1881, and gear standards still rate teeth from "
                    "those stresses plus empirical factors - yet pitting "
                    "remains one of the most common gearbox failure modes, "
                    "and micropitting in wind-turbine gears keeps "
                    "surprising operators."),
        "background": ("Heinrich Hertz published the contact-mechanics solution "
                       "for elastic bodies in 1881-1882, giving the subsurface "
                       "shear stress field that drives contact fatigue. Gear "
                       "rating standards (AGMA 2001, ISO 6336) wrap the Hertz "
                       "stress in factors for load distribution, dynamics, "
                       "lubrication, and material. The weak link is "
                       "micropitting: surface-initiated micro-cracks, only "
                       "microns deep, driven by asperity interaction in the "
                       "mixed-lubrication regime. It was a minor curiosity "
                       "until wind-turbine gearboxes started failing from it in "
                       "the 2000s, and there is still no rating method that "
                       "predicts micropitting risk from first principles - "
                       "engineers rely on the FVA and AGMA micropitting tests, "
                       "which are comparative, not predictive."),
        "why_it_matters": ("Gearboxes transmit power in vehicles, wind "
                           "turbines, ships, and factories. Pitting failures "
                           "mean unplanned downtime and expensive replacements, "
                           "and over-conservative ratings mean heavier, "
                           "costlier gearboxes than needed."),
        "citations": [
            "Hertz, H. On the Contact of Elastic Solids. Journal fur die reine "
            "und angewandte Mathematik, vol. 92; 1881.",
            "ISO 6336:2019. Calculation of load capacity of spur and helical gears.",
            "Olver, A. V. The Mechanism of Roller Contact Fatigue. Proceedings "
            "of the Institution of Mechanical Engineers, Part J; 2005.",
        ],
        "sig_pointer": ("The Signature approach computes the asperity-level "
                        "stress history through the mesh and accumulates a "
                        "micropitting damage index per tooth, turning the "
                        "comparative test into a calibrated predictor."),
        "sig": {
            "assumptions": ("Hertzian macro-stress is correct at the tooth "
                            "scale. Micropitting is driven by the sliding "
                            "asperity stress history, which can be estimated "
                            "from measured roughness and film thickness."),
            "reasoning": ("Rating standards stop at the macro scale and hand "
                          "the micro scale to comparative tests. Bridge the "
                          "scales: run the measured surface profile through "
                          "the mesh kinematics, get the asperity stress "
                          "cycles, and accumulate damage the way S-N curves "
                          "accumulate macro fatigue."),
            "mechanism": ("A per-tooth micropitting index: slide-to-roll "
                          "ratio and lambda film ratio from operating "
                          "conditions feed an asperity stress solver, whose "
                          "output accumulates against a calibrated "
                          "micropitting S-N curve. The FVA test rig "
                          "calibrates the curve; field oil and temperature "
                          "data scale it."),
            "confirm": ("Gear pairs whose computed index ordering matches "
                        "observed micropitting onset order on back-to-back "
                        "test rigs, within one load stage."),
            "kill": ("If measured roughness profiles do not change the "
                     "predicted ranking versus the macro-only rating, the "
                     "asperity layer is decorative and the approach fails."),
            "notclaim": ("This does not claim to retire the standards or the "
                         "test rigs; it claims to extend them. We do not know "
                         "the calibrated curve transfers across steel grades "
                         "- that needs a cross-grade test matrix."),
        },
        "demo_spec": {
            "approach": ("Estimate Hertzian contact pressure at the pitch "
                         "point and the lambda film ratio that flags "
                         "micropitting risk."),
            "assume": [("load_N", 5000.0, "N"),
                       ("radius_m", 0.02, "m"),
                       ("width_m", 0.03, "m"),
                       ("E_GPa", 210.0, "GPa"),
                       ("roughness_um", 0.4, "um")],
            "derived": [
                ("p0_GPa", "(load_N * E_GPa * 1e9 / (3.14159265 * width_m * radius_m * 2.0)) ** 0.5 / 1e9"),
                ("film_um", "0.15 * (load_N / 5000.0) ** -0.1"),
                ("lambda_ratio", "film_um / roughness_um"),
                ("risk_flag", "1.0 if lambda_ratio < 1.0 else 0.0"),
            ],
            "confirm": ("Computed index ordering matches observed micropitting "
                        "onset order on test rigs within one load stage."),
            "refute": ("Asperity profiles do not change predicted ranking "
                       "versus the macro-only rating."),
        },
    },
    {
        "key": "bolt-loosening",
        "name": "Bolted-Joint Self-Loosening Prediction",
        "group": "Friction and Wear",
        "ladder_rank": 4,
        "ladder_tier": "approachable",
        "problem": ("How to predict whether a tightened bolt will shake itself "
                    "loose in service. The Junker test has shown since 1969 "
                    "that transverse vibration is the killer, yet engineers "
                    "still cannot compute, from the joint design and the "
                    "vibration spectrum, whether a given bolt will loosen - "
                    "so critical joints get over-designed or fail."),
        "background": ("Gerhard Junker published the landmark transverse-"
                       "vibration loosening tests in 1969, showing that small "
                       "side-to-side motion walks a nut off far faster than "
                       "axial vibration ever could. The mechanism is now "
                       "understood qualitatively: transverse slip at the "
                       "thread and bearing surfaces lets the helix angle do "
                       "its work, rotating the nut loose one micro-slip at a "
                       "time. NASA published fastener design guidance "
                       "(NASA-RP-1228) after fastener failures in the space "
                       "program, and the VDI 2230 guideline covers static "
                       "joint design thoroughly. But the dynamic question - "
                       "given this vibration spectrum, does this joint loosen "
                       "in a thousand hours or a million - has no accepted "
                       "predictive model; industry still answers it with "
                       "Junker-machine testing of physical prototypes."),
        "why_it_matters": ("Bolted joints hold together vehicles, aircraft, "
                           "bridges, and machinery. Unexpected loosening "
                           "causes failures ranging from rattling panels to "
                           "lost wheels and structural collapse, while the "
                           "testing workaround slows every development "
                           "program."),
        "citations": [
            "Junker, G. H. New Criteria for Self-Loosening of Fasteners Under "
            "Vibration. SAE Transactions, vol. 78; 1969.",
            "VDI 2230 Part 1. Systematic calculation of highly stressed bolted "
            "joints; 2015.",
            "NASA-RP-1228. Fastener Design Manual; 1990.",
        ],
        "sig_pointer": ("The Signature approach converts the vibration "
                        "spectrum into an accumulated transverse-slip budget "
                        "and compares it against a slip-capacity curve for "
                        "the thread pair, giving a loosen-or-not verdict per "
                        "joint."),
        "sig": {
            "assumptions": ("Junker mechanism is the dominant loosening path "
                            "for transverse-dominated vibration. Slip "
                            "accumulates linearly with cycle count below a "
                            "friction threshold and accelerates above it."),
            "reasoning": ("Testing persists because the load at the thread "
                          "is never computed from the spectrum - it is "
                          "measured on a rig. Compute it instead: resolve "
                          "the joint vibration into transverse thread slip "
                          "per cycle, accumulate against the friction "
                          "threshold, and the Junker test becomes a "
                          "calibration point rather than a requirement."),
            "mechanism": ("A slip-budget integrator: the input vibration "
                          "spectrum is converted to thread-surface relative "
                          "displacement per cycle via the joint stiffness "
                          "model; cycles above the critical slip amplitude "
                          "consume the budget, cycles below do not. A "
                          "friction-decay term accounts for fretting wear "
                          "lowering the threshold over time."),
            "confirm": ("Blind predictions of loosen-vs-hold on a matrix of "
                        "joint geometries matching Junker-machine outcomes "
                        "with 90 percent agreement."),
            "kill": ("If the friction-decay term dominates unpredictably - "
                     "real joints scatter wider than the budget predicts - "
                     "the model is no better than testing."),
            "notclaim": ("This does not cover axial-vibration loosening or "
                         "thermal-cycle loosening, which are different "
                         "mechanisms. We do not know the decay term "
                         "transfers across coatings; that needs a coating "
                         "test matrix."),
        },
        "demo_spec": {
            "approach": ("Convert transverse vibration amplitude to a "
                         "slip budget and compare against the friction "
                         "threshold."),
            "assume": [("transverse_um", 200.0, "um"),
                       ("pitch_mm", 1.5, "mm"),
                       ("mu_thread", 0.12, "-"),
                       ("cycles", 1e6, "-")],
            "derived": [
                ("slip_ratio", "transverse_um / (pitch_mm * 1000.0)"),
                ("crit_slip", "mu_thread * 0.5"),
                ("budget_used", "cycles * max(0.0, slip_ratio - crit_slip) * 1e-6"),
                ("loosen_flag", "1.0 if budget_used > 1.0 else 0.0"),
            ],
            "confirm": ("Blind predictions match Junker-machine outcomes "
                        "with 90 percent agreement."),
            "refute": ("Friction-decay scatter makes the budget no better "
                       "than physical testing."),
        },
    },
    {
        "key": "vibration-harvest",
        "name": "Vibration Energy Harvesting Efficiency Limits",
        "group": "Energy Harvesting and Thermal",
        "ladder_rank": 5,
        "ladder_tier": "approachable",
        "problem": ("How much electrical power can ultimately be squeezed from "
                    "ambient vibration, and what design reaches that limit. "
                    "Harvesters power wireless sensors today, but reported "
                    "efficiencies scatter wildly, there is no agreed "
                    "practical ceiling the way the Betz limit caps wind "
                    "turbines, and most devices harvest orders of magnitude "
                    "less than optimistic papers imply."),
        "background": ("Piezoelectricity was discovered by the Curie brothers "
                       "in 1880, and the modern vibration harvester - a "
                       "cantilever tuned to a host vibration - descends from "
                       "that physics plus the resonant-generator analysis of "
                       "Williams and Yates in 1996. The theoretical maximum "
                       "for a resonant harvester is well understood: it is "
                       "bounded by the proof mass, the vibration amplitude "
                       "and frequency, and the damping split between "
                       "mechanical loss and electrical extraction. The "
                       "unsolved part is practical: real vibrations are "
                       "broadband and time-varying while harvesters are "
                       "narrowband; frequency-tuning mechanisms consume part "
                       "of what they gain; and there is no standard figure of "
                       "merit, so the literature compares devices on "
                       "incompatible metrics. Designers cannot answer the "
                       "simple question: for this vibration record, what is "
                       "the most power any harvester could deliver."),
        "why_it_matters": ("Trillions of future wireless sensors need power "
                           "without batteries or wiring. A trustworthy "
                           "practical limit would tell engineers when "
                           "harvesting can work, stop over-promising, and "
                           "focus effort on the designs that approach the "
                           "ceiling."),
        "citations": [
            "Williams, C. B. and Yates, R. B. Analysis of a Micro-Electric "
            "Generator for Microsystems. Sensors and Actuators A, vol. 52; 1996.",
            "Roundy, S. et al. A Study of Low Level Vibrations as a Power "
            "Source for Wireless Sensor Nodes. Computer Communications, vol. 26; "
            "2003.",
            "Beeby, S. P. et al. Energy Harvesting Vibration Sources for "
            "Microsystems Applications. Measurement Science and Technology, "
            "vol. 17; 2006.",
        ],
        "sig_pointer": ("The Signature approach defines the harvestable "
                        "ceiling directly from the measured vibration record "
                        "- mass, stroke limit, and damping split - so any "
                        "device can be scored as a fraction of its own "
                        "personal best."),
        "sig": {
            "assumptions": ("The host vibration record is known or "
                            "measurable. The harvester proof mass and "
                            "allowable stroke are fixed by the package. "
                            "Maximum extraction occurs when electrical "
                            "damping matches mechanical damping."),
            "reasoning": ("The literature scatters because every paper "
                          "invents its own metric. Fix the metric first: for "
                          "a given vibration record and package, the ceiling "
                          "is a definite integral over the record - no "
                          "device can beat it, every device can be scored "
                          "against it. Then the design problem becomes "
                          "climbing toward a known summit."),
            "mechanism": ("A ceiling integral computed from the acceleration "
                          "power spectrum of the host, the proof mass, and "
                          "the stroke limit, with the damping-split optimum "
                          "solved per frequency band. Broadband hosts get a "
                          "multi-mode ceiling; the ratio of device output to "
                          "ceiling becomes the standard efficiency figure, "
                          "replacing the current incompatible metrics."),
            "confirm": ("Three independent device families score below 1.0 "
                        "on the metric with no violations, and the best "
                        "devices cluster at similar fractions of ceiling."),
            "kill": ("If real devices systematically beat the ceiling, the "
                     "integral missed an energy path and the metric is "
                     "wrong."),
            "notclaim": ("This does not invent a better harvester; it "
                         "invents the ruler. We do not know the ceiling is "
                         "tight - the gap between best devices and ceiling "
                         "may be physics or just immature design, and only "
                         "a device-optimization campaign can tell."),
        },
        "demo_spec": {
            "approach": ("Compute the resonant-harvester power ceiling from "
                         "proof mass, vibration level, and damping split."),
            "assume": [("mass_kg", 0.05, "kg"),
                       ("freq_hz", 60.0, "Hz"),
                       ("accel_g", 1.0, "g"),
                       ("Q_factor", 50.0, "-")],
            "derived": [
                ("accel_ms2", "accel_g * 9.81"),
                ("omega", "2.0 * 3.14159265 * freq_hz"),
                ("P_ceiling_mW", "0.5 * mass_kg * accel_ms2 ** 2 / omega * Q_factor * 1000.0"),
                ("P_per_g2_mW", "P_ceiling_mW / accel_g ** 2"),
            ],
            "confirm": ("Independent device families score below 1.0 with "
                        "no ceiling violations."),
            "refute": ("Real devices systematically beat the ceiling, "
                       "showing the integral missed an energy path."),
        },
    },
    {
        "key": "am-parts",
        "name": "Reliable 3D-Printed Load-Bearing Parts",
        "group": "Manufacturing and Metamaterials",
        "ladder_rank": 6,
        "ladder_tier": "approachable",
        "problem": ("How to guarantee that a metal 3D-printed part carrying "
                    "real loads will not fail from hidden defects. Additive "
                    "manufacturing can print shapes no other process can make, "
                    "but porosity, residual stress, and rough as-built "
                    "surfaces scatter fatigue life so widely that critical "
                    "parts still need expensive per-part inspection and "
                    "testing."),
        "background": ("ASTM Committee F42 on additive manufacturing was "
                       "formed in 2009 to standardize the young field, and "
                       "laser powder-bed fusion can now match wrought tensile "
                       "strength in many alloys. The trouble is defects: "
                       "lack-of-fusion pores, keyhole pores, and residual "
                       "stresses from rapid thermal cycling, all varying with "
                       "geometry, orientation, and even position on the build "
                       "plate. Fatigue cracks start at the worst defect, so "
                       "life is controlled by defect statistics, not average "
                       "properties - and defect statistics change with every "
                       "process tweak. Aerospace qualification still leans on "
                       "extensive testing plus hot isostatic pressing, and "
                       "there is no accepted computational path from "
                       "in-process sensor data to a certified fatigue life."),
        "why_it_matters": ("Printing load-bearing parts on demand would "
                           "transform spares, lightweight structures, and "
                           "remote repair. The certification bottleneck is "
                           "the main thing standing between the technology "
                           "and that future."),
        "citations": [
            "ASTM F42 Committee. Additive Manufacturing Technology Standards; "
            "2009 onward.",
            "DebRoy, T. et al. Additive Manufacturing of Metallic Components - "
            "Process, Structure and Properties. Progress in Materials Science, "
            "vol. 92; 2018.",
            "National Academies. Frontiers of Additive Manufacturing Research; "
            "2022.",
        ],
        "sig_pointer": ("The Signature approach converts in-process melt-pool "
                        "monitoring into a defect-size distribution per part "
                        "and runs fracture mechanics on the worst predicted "
                        "defect, giving a per-part fatigue-life certificate."),
        "sig": {
            "assumptions": ("Fatigue life of printed metal is controlled by "
                            "the largest defect, per Murakami-style fracture "
                            "mechanics. In-process sensors (melt-pool "
                            "imaging, acoustic) carry enough signal to bound "
                            "the defect distribution."),
            "reasoning": ("Certification stalls because properties are "
                          "treated as material constants with scatter. Treat "
                          "them instead as what they are - the output of a "
                          "defect population - and the scatter becomes "
                          "computable. The sensors already watch every layer; "
                          "use their record as the part individual birth "
                          "certificate."),
            "mechanism": ("A per-part digital defect map built from "
                          "in-process monitoring, converted to an extreme-"
                          "value defect size, then run through a short-crack "
                          "fatigue model for the service loads. Parts whose "
                          "predicted life clears the requirement with margin "
                          "ship; the rest get HIP or are scrapped - a "
                          "computational proof test for every part."),
            "confirm": ("Predicted life rankings match observed fatigue test "
                        "rankings on a blind build plate with rank "
                        "correlation above 0.8."),
            "kill": ("If in-process sensors cannot resolve the defects that "
                     "actually initiate cracks - the killer defects hide "
                     "below sensor resolution - the map is fiction and the "
                     "approach fails."),
            "notclaim": ("This does not replace material qualification or "
                         "claim sensor data sees everything. We do not know "
                         "the resolution floor is low enough; a "
                         "sensor-vs-sectioning study is needed first."),
        },
        "demo_spec": {
            "approach": ("Apply a defect knockdown to printed tensile "
                         "strength via a Murakami-style defect size term."),
            "assume": [("uts_wrought_MPa", 950.0, "MPa"),
                       ("porosity_pct", 0.4, "pct"),
                       ("defect_mm", 0.3, "mm")],
            "derived": [
                ("knockdown", "1.0 - porosity_pct / 100.0 * 8.0 - defect_mm * 0.15"),
                ("uts_effective_MPa", "uts_wrought_MPa * max(0.2, knockdown)"),
                ("strength_loss_pct", "(1.0 - uts_effective_MPa / uts_wrought_MPa) * 100.0"),
            ],
            "confirm": ("Predicted life rankings match blind fatigue tests "
                        "with rank correlation above 0.8."),
            "refute": ("Killer defects hide below in-process sensor "
                       "resolution, making the defect map fiction."),
        },
    },
    {
        "key": "nvh",
        "name": "Machine Noise and Vibration Prediction",
        "group": "Soft Robotics and Control",
        "ladder_rank": 7,
        "ladder_tier": "approachable",
        "problem": ("How to predict, on the drawing board, how loud a machine "
                    "will be and where its vibration will go. Noise and "
                    "vibration simulation still misses reality by enough that "
                    "vehicles, appliances, and industrial equipment go through "
                    "rounds of build-and-test quieting late in development."),
        "background": ("Statistical energy analysis (SEA), developed by Lyon "
                       "and others in the 1960s-70s, predicts high-frequency "
                       "vibration energy flow between subsystems, while finite "
                       "element methods handle low frequencies - leaving the "
                       "mid-frequency gap where neither works well, which is "
                       "exactly where human hearing is most sensitive. "
                       "Damping remains the least predictable input: material "
                       "damping data measured on coupons rarely matches built-"
                       "up structures with joints, and joint damping can "
                       "dominate the whole response. Industry compensates "
                       "with prototype testing and add-on damping treatments, "
                       "an expensive loop that repeats for every new design."),
        "why_it_matters": ("Noise regulations tighten worldwide, and vibration "
                           "drives fatigue failures. Predicting NVH before "
                           "tooling is cut would shorten development, cut "
                           "weight spent on quieting patches, and make "
                           "quieter products."),
        "citations": [
            "Lyon, R. H. Statistical Energy Analysis of Dynamical Systems. MIT "
            "Press; 1975.",
            "Cremer, L., Heckl, M. and Petersson, B. A. T. Structure-Borne "
            "Sound. Springer; 2005.",
            "Desmet, W. and Vandepitte, D. Mid-frequency vibro-acoustic "
            "modelling. KU Leuven course notes; 2002.",
        ],
        "sig_pointer": ("The Signature approach closes the mid-frequency gap "
                        "with a hybrid solver that blends deterministic modes "
                        "and statistical energy flow, calibrated by a "
                        "joint-damping library measured once per joint type."),
        "sig": {
            "assumptions": ("Low-frequency modes are predictable by FEM; "
                            "high-frequency energy flow by SEA. The gap is "
                            "bridgeable, and joint damping is reusable data - "
                            "the same bolted joint damps the same way in any "
                            "machine."),
            "reasoning": ("Every program re-measures what the last program "
                          "learned about joints, then guesses in the mid-"
                          "frequency band. Build the joint-damping library "
                          "once, blend the solvers across the gap with an "
                          "overlap region where both run, and the prediction "
                          "inherits the library accuracy."),
            "mechanism": ("A hybrid solver with a frequency overlap band: "
                          "FEM modes below, SEA above, and a wave-based "
                          "blending in between. Joint damping comes from a "
                          "shared library keyed by joint type, preload, and "
                          "surface finish - measured once, reused everywhere, "
                          "growing with each program."),
            "confirm": ("Blind predictions on two new machine designs land "
                        "within 3 dB of measured overall sound power."),
            "kill": ("If joint damping proves non-transferable - the same "
                     "joint damps differently in different assemblies beyond "
                     "usable tolerance - the library concept collapses."),
            "notclaim": ("This does not claim to model nonlinear rattles or "
                         "aeroacoustic sources; those stay empirical. We do "
                         "not know the library converges - it needs "
                         "multi-program contribution to find out."),
        },
        "demo_spec": {
            "approach": ("Compute natural frequency and vibration "
                         "transmissibility for a single-degree-of-freedom "
                         "isolator model."),
            "assume": [("mass_kg", 8.0, "kg"),
                       ("stiffness_Npm", 1.8e6, "N/m"),
                       ("excite_hz", 120.0, "Hz"),
                       ("damping_ratio", 0.05, "-")],
            "derived": [
                ("fn_hz", "(stiffness_Npm / mass_kg) ** 0.5 / (2.0 * 3.14159265)"),
                ("r_ratio", "excite_hz / fn_hz"),
                ("transmiss", "((1.0 + (2.0 * damping_ratio * r_ratio) ** 2) / ((1.0 - r_ratio ** 2) ** 2 + (2.0 * damping_ratio * r_ratio) ** 2)) ** 0.5"),
            ],
            "confirm": ("Blind predictions land within 3 dB of measured "
                        "sound power on new designs."),
            "refute": ("Joint damping proves non-transferable across "
                       "assemblies, collapsing the library concept."),
        },
    },
    {
        "key": "small-turbo",
        "name": "Small-Scale Pump and Turbine Efficiency",
        "group": "Energy Harvesting and Thermal",
        "ladder_rank": 8,
        "ladder_tier": "approachable",
        "problem": ("How to keep turbomachinery efficient as it shrinks. "
                    "Large turbines exceed 90 percent efficiency, but "
                    "centimeter-scale pumps, micro-turbines, and drone "
                    "propulsion lose efficiency fast - clearances, surface "
                    "roughness, and viscous effects that are negligible at "
                    "large scale dominate at small scale, and the scaling "
                    "laws are unreliable."),
        "background": ("Turbomachinery design rests on similarity laws and "
                       "specific speed correlations built from a century of "
                       "large-machine data. Shrink the machine and three "
                       "things break the correlations: relative tip "
                       "clearances grow because manufacturing tolerances do "
                       "not shrink proportionally; Reynolds numbers fall, "
                       "thickening boundary layers; and surface roughness "
                       "becomes a large fraction of blade passages. The "
                       "result is the well-known size effect - small "
                       "turbochargers, micro gas turbines, and medical pumps "
                       "all underperform their scaled predictions. Designers "
                       "compensate with empirical correction factors that "
                       "are proprietary, scattered, and often wrong outside "
                       "the machines they were fitted to."),
        "why_it_matters": ("Small turbomachines power drones, portable "
                           "power, medical devices, and distributed energy. "
                           "Reliable small-scale design would unlock "
                           "lighter aircraft propulsion and more efficient "
                           "distributed power."),
        "citations": [
            "Dixon, S. L. and Hall, C. A. Fluid Mechanics and Thermodynamics "
            "of Turbomachinery, 7th ed. Butterworth-Heinemann; 2013.",
            "Casey, M. V. The Effects of Reynolds Number on the Efficiency of "
            "Centrifugal Compressor Stages. ASME J. Engineering for Gas "
            "Turbines and Power; 1985.",
            "Epstein, A. H. Millimeter-Scale, Micro-Electro-Mechanical Systems "
            "Gas Turbine Engines. ASME J. Engineering for Gas Turbines and "
            "Power, vol. 126; 2004.",
        ],
        "sig_pointer": ("The Signature approach replaces the scattered "
                        "correction factors with a clearance-roughness-"
                        "Reynolds loss budget computed per blade row, so "
                        "small-scale efficiency becomes a sum of named "
                        "losses instead of a fudge factor."),
        "sig": {
            "assumptions": ("The size effect decomposes into separable "
                            "losses: tip-clearance leakage, roughness "
                            "penalty, and low-Reynolds profile loss. Each "
                            "is computable from geometry and operating "
                            "point."),
            "reasoning": ("Correction factors fail because they hide three "
                          "different physics in one number. Separate them, "
                          "compute each from first-order models tied to "
                          "measurable geometry, and the small-scale machine "
                          "gets the same honest loss accounting large "
                          "machines enjoy."),
            "mechanism": ("A per-row loss budget: clearance loss from the "
                          "measured clearance-to-blade-height ratio, "
                          "roughness loss from the roughness Reynolds "
                          "number, profile loss from a low-Re cascade "
                          "correlation. The budget is computed at the "
                          "design point and across the map, and the "
                          "dominant loss tells the designer exactly what to "
                          "fix."),
            "confirm": ("Blind efficiency predictions on three small "
                        "turbomachines land within 2 points of measured "
                        "efficiency."),
            "kill": ("If the losses prove non-separable - fixing clearance "
                     "changes the roughness sensitivity unpredictably - "
                     "the budget is accounting fiction."),
            "notclaim": ("This does not claim to beat the large-machine "
                         "efficiency; small machines face real physical "
                         "penalties. We do not know the cascade "
                         "correlation holds below Re 50,000 - low-Re rig "
                         "data is needed."),
        },
        "demo_spec": {
            "approach": ("Estimate tip speed and the clearance-loss penalty "
                         "for a small high-speed rotor."),
            "assume": [("diam_mm", 25.0, "mm"),
                       ("rpm", 120000.0, "rpm"),
                       ("clearance_um", 80.0, "um"),
                       ("blade_h_mm", 3.0, "mm")],
            "derived": [
                ("tip_speed_ms", "3.14159265 * diam_mm / 1000.0 * rpm / 60.0"),
                ("clear_ratio", "clearance_um / 1000.0 / blade_h_mm"),
                ("clear_loss_pts", "clear_ratio * 100.0 * 0.6"),
                ("eff_penalty_pts", "clear_loss_pts + 1.5"),
            ],
            "confirm": ("Blind predictions land within 2 efficiency points "
                        "on small turbomachines."),
            "refute": ("Losses prove non-separable; fixing clearance changes "
                       "roughness sensitivity unpredictably."),
        },
    },
    {
        "key": "cui",
        "name": "Corrosion Under Insulation",
        "group": "Manufacturing and Metamaterials",
        "ladder_rank": 9,
        "ladder_tier": "approachable",
        "problem": ("How to predict and find corrosion hiding under pipe and "
                    "vessel insulation. CUI is invisible by definition - "
                    "water wicks into insulation, corrodes the steel "
                    "beneath, and the first sign is often a leak or a "
                    "rupture. Inspection is strip-and-look, which is "
                    "expensive and itself damages the insulation."),
        "background": ("Corrosion under insulation has caused some of the "
                       "chemical industry most expensive failures, and the "
                       "NACE IMPACT study of 2016 put the global cost of "
                       "corrosion at about 2.5 trillion US dollars per year, "
                       "with CUI a notorious slice. The mechanism is "
                       "understood - wet insulation holds chlorides against "
                       "steel in the 60 to 150 C danger zone - but prediction "
                       "is not: local wetting depends on cladding damage, "
                       "weather, and insulation type in ways no model "
                       "captures. Inspection technology (pulsed eddy "
                       "current, neutron backscatter, guided-wave "
                       "ultrasound) can find it but is slow and costly, so "
                       "plants inspect on risk schedules that are largely "
                       "expert judgment."),
        "why_it_matters": ("CUI failures cause fires, toxic releases, and "
                           "shutdowns. Predicting where water goes and "
                           "corrosion grows would let plants inspect the "
                           "right 5 percent of piping instead of guessing."),
        "citations": [
            "NACE International. International Measures of Prevention, "
            "Application, and Economics of Corrosion Technologies (IMPACT); 2016.",
            "API RP 583. Corrosion Under Insulation and Fireproofing; 2014.",
            "Winnik, S. (ed.) Corrosion Under Insulation (CUI) Guidelines. "
            "Elsevier; 2016.",
        ],
        "sig_pointer": ("The Signature approach models water ingress paths "
                        "from cladding condition and weather exposure to "
                        "rank every pipe segment by wet-time, turning the "
                        "inspection schedule into a computed priority list."),
        "sig": {
            "assumptions": ("CUI rate is controlled by time-of-wetness at "
                            "the steel surface in the temperature danger "
                            "zone. Cladding damage and exposure geometry "
                            "determine wet-time and are surveyable."),
            "reasoning": ("Plants cannot inspect everything, so inspection "
                          "is already a ranking problem solved by gut feel. "
                          "Replace gut feel with a wet-time model: survey "
                          "cladding condition once, combine with local "
                          "weather and operating temperature, and every "
                          "segment gets a computed CUI priority."),
            "mechanism": ("A per-segment wet-time score from cladding "
                          "survey data, orientation, and climate records, "
                          "mapped through a temperature-window corrosion "
                          "rate to a wall-loss forecast. Inspection "
                          "resources go to the top of the ranked list; the "
                          "model updates as inspection results come back."),
            "confirm": ("Ranked lists where the top quintile contains most "
                        "of the significant CUI found in a full inspection "
                        "campaign, on two or more plants."),
            "kill": ("If cladding surveys do not predict wet-time - water "
                     "finds paths the survey misses - the ranking is no "
                     "better than expert judgment."),
            "notclaim": ("This does not see through insulation or replace "
                         "inspection tools. We do not know survey data is "
                         "enough; hidden damage modes may dominate, which "
                         "only paired survey-and-strip studies can reveal."),
        },
        "demo_spec": {
            "approach": ("Forecast wall loss from time-of-wetness and the "
                         "temperature-window corrosion rate."),
            "assume": [("wet_fraction", 0.35, "-"),
                       ("rate_mmpy", 0.25, "mm/yr"),
                       ("years", 10.0, "yr"),
                       ("temp_C", 120.0, "C")],
            "derived": [
                ("window_factor", "1.0 if 60.0 <= temp_C <= 150.0 else 0.3"),
                ("loss_mm", "rate_mmpy * years * wet_fraction * window_factor"),
                ("loss_pct_wall", "loss_mm / 8.0 * 100.0"),
            ],
            "confirm": ("Top-quintile ranked segments contain most "
                        "significant CUI found in full campaigns."),
            "refute": ("Cladding surveys do not predict wet-time; water "
                       "finds paths the survey misses."),
        },
    },
]
ENTRIES += [
    {
        "key": "friction-wear",
        "name": "Predicting Friction and Wear in Real Machines",
        "group": "Friction and Wear",
        "ladder_rank": 10,
        "ladder_tier": "approachable",
        "problem": ("How to predict the friction coefficient and wear rate of "
                    "a sliding contact from first principles. Engineers "
                    "still design with Amontons and Coulomb 300-year-old "
                    "friction laws plus handbook wear coefficients that can "
                    "scatter over orders of magnitude - the most basic "
                    "mechanical interaction remains essentially empirical."),
        "background": ("Amontons stated his friction laws in 1699 and Coulomb "
                       "refined them in 1785: friction is proportional to "
                       "normal load and independent of apparent contact area. "
                       "Bowden and Tabor showed in the 1940s-50s why - real "
                       "contact happens at tiny asperities that deform until "
                       "their area carries the load. Archard published his "
                       "wear law in 1953, relating wear volume to load, "
                       "sliding distance, and hardness. Yet the wear "
                       "coefficient in Archard law is a fitted number that "
                       "varies wildly with the tribosystem, the Stribeck "
                       "curve of 1902 still organizes lubrication regimes "
                       "better than any theory predicts them, and "
                       "first-principles friction prediction from surface "
                       "topography remains an unsolved multiscale problem."),
        "why_it_matters": ("Friction consumes an estimated fifth of the "
                           "world energy use through direct losses, and wear "
                           "limits the life of every sliding machine part. "
                           "Predictive tribology would cut energy waste and "
                           "let designers choose materials computationally "
                           "instead of by test matrices."),
        "citations": [
            "Bowden, F. P. and Tabor, D. The Friction and Lubrication of "
            "Solids. Oxford University Press; 1950.",
            "Archard, J. F. Contact and Rubbing of Flat Surfaces. Journal of "
            "Applied Physics, vol. 24; 1953.",
            "Holmberg, K. and Erdemir, A. Influence of Tribology on Global "
            "Energy Consumption. Friction, vol. 5; 2017.",
        ],
        "sig_pointer": ("The Signature approach computes friction and wear "
                        "from measured 3D surface topography run through a "
                        "multiscale asperity model, replacing the handbook "
                        "coefficient with a computed one per surface pair."),
        "sig": {
            "assumptions": ("Friction and mild wear emerge from asperity "
                            "deformation and adhesion at the real contact "
                            "spots. Measured 3D topography plus material "
                            "properties contain enough information to "
                            "compute the outcome."),
            "reasoning": ("Handbook coefficients scatter because they "
                          "average over unknown topographies. Measure the "
                          "topography, simulate the asperity population "
                          "under load, and the coefficient becomes a "
                          "property of the specific surface pair rather "
                          "than a tribal number."),
            "mechanism": ("A multiscale contact solver: the measured "
                          "surface goes through a boundary-element contact "
                          "model to get the real area and pressure "
                          "distribution; adhesion and plowing terms give "
                          "friction; a local Archard accumulation gives "
                          "wear. One calibration constant per material "
                          "pair replaces the coefficient tables."),
            "confirm": ("Blind predictions of friction coefficient within "
                        "20 percent and wear-rate ranking correct across a "
                        "matrix of surface finishes."),
            "kill": ("If third-body effects - transfer films, wear debris "
                     "- dominate from the first cycles, the clean-surface "
                     "computation cannot predict steady state and the "
                     "approach fails."),
            "notclaim": ("This does not claim to model severe wear, "
                         "scuffing, or lubricated contacts yet; those add "
                         "physics beyond dry asperity mechanics. We do not "
                         "know the calibration transfers across "
                         "environments - humidity alone may break it."),
        },
        "demo_spec": {
            "approach": ("Estimate friction energy loss and Archard wear "
                         "volume for a sliding contact."),
            "assume": [("mu", 0.12, "-"),
                       ("load_N", 2000.0, "N"),
                       ("speed_ms", 2.0, "m/s"),
                       ("hours", 8000.0, "h"),
                       ("wear_k", 1e-6, "-"),
                       ("hardness_Pa", 2e9, "Pa")],
            "derived": [
                ("slide_m", "speed_ms * hours * 3600.0"),
                ("energy_MJ", "mu * load_N * slide_m / 1e6"),
                ("wear_mm3", "wear_k * load_N * slide_m / hardness_Pa * 1e9"),
                ("power_W", "mu * load_N * speed_ms"),
            ],
            "confirm": ("Blind friction predictions within 20 percent and "
                        "correct wear ranking across finishes."),
            "refute": ("Third-body transfer films dominate from the first "
                       "cycles, breaking the clean-surface computation."),
        },
    },
    {
        "key": "cavitation",
        "name": "Cavitation Erosion Prediction",
        "group": "Turbulence and Fluids",
        "ladder_rank": 11,
        "ladder_tier": "approachable",
        "problem": ("How to predict where and how fast cavitation will chew "
                    "up a propeller, pump impeller, or turbine runner. "
                    "Cavitation - vapor bubbles collapsing violently near "
                    "surfaces - erodes metal at astonishing rates, yet "
                    "designers cannot compute erosion risk from the flow "
                    "field and still rely on model tests and past damage."),
        "background": ("Lord Rayleigh analyzed the collapse of a spherical "
                       "cavity in 1917, showing the collapse focuses energy "
                       "into microjets and shock waves with pressures far "
                       "above material strength. The cavitation number, "
                       "sigma, tells whether cavitation occurs, but erosion "
                       "is a different question: it depends on where "
                       "bubbles collapse, how many, and how the material "
                       "responds to millions of micro-impacts. Propeller and "
                       "pump designers use model tests and empirical "
                       "erosion-risk charts; CFD can predict vapor volume "
                       "but not which collapses damage the surface. The "
                       "link from computed flow to grams of metal lost per "
                       "thousand hours is missing."),
        "why_it_matters": ("Cavitation limits how hard pumps, propellers, "
                           "and turbines can be pushed and destroys "
                           "impellers worth fortunes. Predicting erosion "
                           "would let designers run closer to the limit and "
                           "schedule maintenance before damage, not after."),
        "citations": [
            "Rayleigh, Lord. On the Pressure Developed in a Liquid During the "
            "Collapse of a Spherical Cavity. Philosophical Magazine, vol. 34; 1917.",
            "Brennen, C. E. Cavitation and Bubble Dynamics. Oxford University "
            "Press; 1995.",
            "Franc, J.-P. and Michel, J.-M. Fundamentals of Cavitation. "
            "Springer; 2004.",
        ],
        "sig_pointer": ("The Signature approach tracks computed bubble "
                        "collapse events to the wall and accumulates a "
                        "micro-impact fatigue dose per surface cell, turning "
                        "vapor-volume CFD into an erosion forecast."),
        "sig": {
            "assumptions": ("Erosion is micro-impact fatigue from discrete "
                            "collapse events. CFD resolves the vapor field "
                            "well enough to locate collapses; material "
                            "response follows an impact-fatigue curve."),
            "reasoning": ("CFD answers where vapor is, not where metal "
                          "leaves. Bridge the gap at the event level: each "
                          "collapse near a wall is a micro-impact with an "
                          "energy; accumulate impacts against the material "
                          "fatigue response and erosion becomes a computed "
                          "dose."),
            "mechanism": ("A collapse-event tracker coupled to the flow "
                          "solver: vapor structures that collapse within a "
                          "standoff distance of the wall deposit their "
                          "estimated impact energy into wall cells. Each "
                          "cell accumulates a fatigue dose; cells crossing "
                          "the threshold are flagged as erosion sites with "
                          "a rate."),
            "confirm": ("Predicted erosion-site maps overlap observed "
                        "damage patterns on test impellers with most "
                        "damage inside flagged zones."),
            "kill": ("If collapse energy estimates scatter too widely - "
                     "the microjet physics at collapse is still poorly "
                     "resolved - the dose map is noise and the approach "
                     "fails."),
            "notclaim": ("This does not claim to predict incubation time "
                         "precisely; material defect scatter dominates "
                         "early damage. We do not know the impact-fatigue "
                         "curve transfers across alloys - that needs a "
                         "materials test program."),
        },
        "demo_spec": {
            "approach": ("Compute the cavitation number and a collapse-"
                         "pressure proxy for a high-speed flow."),
            "assume": [("p_local_Pa", 1800.0, "Pa"),
                       ("p_vapor_Pa", 2330.0, "Pa"),
                       ("rho", 998.0, "kg/m3"),
                       ("vel_ms", 18.0, "m/s")],
            "derived": [
                ("dyn_Pa", "0.5 * rho * vel_ms ** 2"),
                ("sigma", "(p_local_Pa - p_vapor_Pa) / dyn_Pa"),
                ("cav_flag", "1.0 if sigma < 0.0 else 0.0"),
                ("collapse_MPa", "dyn_Pa * 8.0 / 1e6"),
            ],
            "confirm": ("Predicted erosion maps overlap observed damage on "
                        "test impellers."),
            "refute": ("Collapse energy estimates scatter too widely for "
                       "a usable dose map."),
        },
    },
    {
        "key": "thermal-packaging",
        "name": "Thermal Packaging of Dense Electronics",
        "group": "Energy Harvesting and Thermal",
        "ladder_rank": 12,
        "ladder_tier": "approachable",
        "problem": ("How to get heat out of ever-denser electronics before "
                    "it cooks them. Power densities keep climbing while "
                    "junction temperature limits stay fixed, and thermal "
                    "design still leans on conservative margins and late "
                    "prototype testing because hotspot prediction in real "
                    "assemblies is unreliable."),
        "background": ("The heat equation is old and conduction solvers are "
                       "mature, but real electronic assemblies defeat them: "
                       "thermal interface materials with uncertain "
                       "contact resistance, anisotropic composites, "
                       "time-varying power maps from real workloads, and "
                       "conjugate convection that couples the board to the "
                       "room. Data-center chips now dissipate hundreds of "
                       "watts each, EV power modules cycle thermally thousands "
                       "of times, and LED and RF devices fail at hotspots "
                       "no board-level model predicted. Thermal design "
                       "margins eat performance - chips throttle below "
                       "their electrical capability because the thermal "
                       "path cannot be trusted."),
        "why_it_matters": ("Every watt of compute, every EV mile, and "
                           "every 5G base station is thermally limited. "
                           "Trustworthy thermal prediction would unlock "
                           "performance already paid for in silicon and cut "
                           "cooling energy."),
        "citations": [
            "Incropera, F. P. et al. Fundamentals of Heat and Mass Transfer, "
            "6th ed. Wiley; 2006.",
            "Lasance, C. J. M. and Poppe, A. (eds.) Thermal Management for "
            "LED Applications. Springer; 2014.",
            "Bar-Cohen, A. and Wang, P. Thermal Management of On-Chip Hot "
            "Spots. ASME J. Heat Transfer; 2012.",
        ],
        "sig_pointer": ("The Signature approach builds the thermal model "
                        "from measured interface resistances and real "
                        "workload power maps, then designs the cooling to "
                        "the computed hotspot field instead of a uniform "
                        "margin."),
        "sig": {
            "assumptions": ("Conduction paths are modelable; the missing "
                            "inputs are interface resistances and true "
                            "power maps, both measurable. Hotspots, not "
                            "averages, set the limit."),
            "reasoning": ("Models fail on inputs, not physics. Measure the "
                          "two inputs that matter - the actual thermal "
                          "resistance of each interface as built, and the "
                          "power map of the real workload - and the mature "
                          "solvers finally get honest boundary conditions."),
            "mechanism": ("A measured-input thermal twin: interface "
                          "resistances from production-line thermal testing, "
                          "power maps from workload profiling, assembled "
                          "into a compact model that runs in seconds. "
                          "Cooling design targets the computed hotspot "
                          "field; margins shrink to the measurement "
                          "uncertainty instead of a blanket factor."),
            "confirm": ("Predicted junction temperatures within 5 C of "
                        "measurement on instrumented boards across three "
                        "product families."),
            "kill": ("If interface resistance varies more unit-to-unit "
                     "than the design margin, per-unit measurement becomes "
                     "mandatory and the twin is uneconomical."),
            "notclaim": ("This does not claim to fix bad thermal "
                         "architecture; it reveals it honestly. We do not "
                         "know production-line thermal testing is cheap "
                         "enough - that needs a manufacturing pilot."),
        },
        "demo_spec": {
            "approach": ("Compute junction temperature and thermal margin "
                         "from power and thermal resistance."),
            "assume": [("power_W", 350.0, "W"),
                       ("Rth_KpW", 0.35, "K/W"),
                       ("Tamb_C", 35.0, "C"),
                       ("Tjmax_C", 105.0, "C")],
            "derived": [
                ("Tj_C", "Tamb_C + power_W * Rth_KpW"),
                ("margin_C", "Tjmax_C - Tj_C"),
                ("max_power_W", "(Tjmax_C - Tamb_C) / Rth_KpW"),
                ("derate_pct", "(1.0 - power_W / max_power_W) * 100.0"),
            ],
            "confirm": ("Predicted junction temperatures within 5 C of "
                        "measurement across product families."),
            "refute": ("Unit-to-unit interface variation exceeds the "
                       "design margin, making the twin uneconomical."),
        },
    },
    # ---------------------------------------------------------- compounded
    {
        "key": "turbulence-closure",
        "name": "The Turbulence Closure Problem",
        "group": "Turbulence and Fluids",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("How to close the averaged equations of turbulent flow. "
                    "Averaging the Navier-Stokes equations produces more "
                    "unknowns than equations - the Reynolds stresses - and "
                    "after a century there is still no exact closure. Every "
                    "engineering turbulence model, from mixing length to the "
                    "latest machine-learned closures, is an approximation "
                    "with known failure modes."),
        "background": ("Osborne Reynolds decomposed flow into mean and "
                       "fluctuation in 1895, creating the averaged equations "
                       "and the unclosed Reynolds stress tensor in one "
                       "stroke. Prandtl mixing-length theory (1925) gave "
                       "the first practical closure; the k-epsilon model of "
                       "Launder and Spalding (1974) became the workhorse of "
                       "industrial CFD. Yet every closure fails somewhere: "
                       "separation, swirl, curvature, transition - engineers "
                       "know which model to distrust for which flow, which "
                       "is another way of saying none is general. Direct "
                       "numerical simulation resolves everything but costs "
                       "too much for engineering Reynolds numbers, scaling "
                       "roughly with Re cubed. The closure problem is "
                       "sometimes called the last great unsolved problem of "
                       "classical physics."),
        "why_it_matters": ("Nearly every fluid device - aircraft, "
                           "turbomachines, combustors, pipelines, weather "
                           "models - is designed with averaged equations. A "
                           "general closure would make CFD predictive "
                           "instead of calibrated, transforming design "
                           "across industries."),
        "citations": [
            "Reynolds, O. On the Dynamical Theory of Incompressible Viscous "
            "Fluids. Philosophical Transactions of the Royal Society; 1895.",
            "Launder, B. E. and Spalding, D. B. The Numerical Computation of "
            "Turbulent Flows. Computer Methods in Applied Mechanics and "
            "Engineering, vol. 3; 1974.",
            "Pope, S. B. Turbulent Flows. Cambridge University Press; 2000.",
        ],
        "sig_pointer": ("The Signature approach does not chase a universal "
                        "formula; it builds a closure selector that reads "
                        "the local flow regime and blends model forms, with "
                        "a built-in honesty flag where no model is "
                        "trustworthy."),
        "sig": {
            "assumptions": ("No single algebraic closure is general. Local "
                            "flow regime - strain rate, rotation, wall "
                            "distance - determines which closure form "
                            "fails least. DNS databases are rich enough to "
                            "train the selector."),
            "reasoning": ("A century of searching for one closure suggests "
                          "the prize is elsewhere: in knowing which "
                          "approximation to use where, and admitting where "
                          "none works. A regime-aware blender turns the "
                          "zoo of models from a liability into a toolkit."),
            "mechanism": ("A regime classifier trained on DNS and "
                          "high-fidelity LES databases maps each cell to a "
                          "flow regime; a blending layer mixes the "
                          "best-performing closures per regime with smooth "
                          "transitions. Where the classifier confidence is "
                          "low, the solver flags the region as "
                          "untrustworthy instead of silently producing "
                          "numbers."),
            "confirm": ("Blind RANS predictions with the blender beat the "
                        "best single model on a held-out set of separated "
                        "and swirling flows by a clear margin."),
            "kill": ("If regime boundaries prove too fuzzy - real flows "
                     "sit between regimes and the blender just averages "
                     "errors - the selector adds nothing over a good "
                     "default model."),
            "notclaim": ("This does not claim an exact closure; the exact "
                         "closure may not exist in algebraic form. We do "
                         "not know the DNS database covers enough regimes "
                         "- exotic flows will still need new data."),
        },
        "demo_spec": {
            "approach": ("Estimate turbulent eddy viscosity from k and "
                         "epsilon and compare model spread across closures."),
            "assume": [("rho", 1.2, "kg/m3"),
                       ("k", 0.5, "m2/s2"),
                       ("epsilon", 0.8, "m2/s3"),
                       ("Cmu_std", 0.09, "-"),
                       ("Cmu_alt", 0.07, "-")],
            "derived": [
                ("mu_t_std", "rho * Cmu_std * k ** 2 / epsilon"),
                ("mu_t_alt", "rho * Cmu_alt * k ** 2 / epsilon"),
                ("spread_pct", "abs(mu_t_std - mu_t_alt) / mu_t_std * 100.0"),
                ("Re_t", "rho * k ** 2 / (1.8e-5 * epsilon)"),
            ],
            "confirm": ("Blended predictions beat the best single model on "
                        "held-out separated and swirling flows."),
            "refute": ("Regime boundaries prove too fuzzy; the blender "
                       "averages errors instead of selecting."),
        },
    },
    {
        "key": "transition",
        "name": "Predicting Laminar-to-Turbulent Transition",
        "group": "Turbulence and Fluids",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("How to predict where a smooth laminar flow breaks down "
                    "into turbulence. Transition location sets drag, heat "
                    "transfer, and separation behavior, yet prediction still "
                    "rests on the semi-empirical e-to-the-N method calibrated "
                    "in the 1950s, with the N factor chosen by experience."),
        "background": ("Reynolds 1883 pipe experiments revealed transition; "
                       "Tollmien (1929) and Schlichting computed the "
                       "instability waves that now bear their names, and "
                       "Schubauer and Skramstad confirmed them experimentally "
                       "in 1947. Smith and Gamberoni, and separately van "
                       "Ingen, turned linear stability into the e^N method "
                       "in 1956: integrate disturbance growth, transition "
                       "when amplification reaches e^N, with N around 9 for "
                       "quiet tunnels and lower for noisy ones. The method "
                       "works for smooth, low-disturbance flows and fails "
                       "for bypass transition, roughness, and most real "
                       "engineering environments - which is to say, it "
                       "fails where it is needed most."),
        "why_it_matters": ("Transition determines aircraft drag, turbine "
                           "blade heat load, and pipeline friction. Moving "
                           "transition prediction from calibrated art to "
                           "reliable computation would cut drag and cooling "
                           "costs across transport and energy."),
        "citations": [
            "Schlichting, H. and Gersten, K. Boundary-Layer Theory, 8th ed. "
            "Springer; 2000.",
            "Smith, A. M. O. and Gamberoni, N. Transition, Pressure Gradient "
            "and Stability Theory. Douglas Aircraft Report ES 26388; 1956.",
            "van Ingen, J. L. A Suggested Semi-Empirical Method for the "
            "Calculation of the Boundary Layer Transition Region. Delft "
            "Report VTH-74; 1956.",
        ],
        "sig_pointer": ("The Signature approach replaces the single N "
                        "factor with a disturbance-environment spectrum "
                        "measured or estimated per application, so the "
                        "amplification integral starts from the real "
                        "disturbance climate instead of a guessed number."),
        "sig": {
            "assumptions": ("Linear stability correctly computes growth "
                            "rates; the missing input is the initial "
                            "disturbance spectrum, which is measurable or "
                            "estimable per environment class."),
            "reasoning": ("The e^N method fine growth physics but guesses "
                          "the starting line. Measure or classify the "
                          "disturbance environment - tunnel turbulence "
                          "level, surface roughness spectrum, acoustic "
                          "field - and the same integral predicts "
                          "transition without a tuned N."),
            "mechanism": ("A disturbance-climate library keyed by "
                          "application class (quiet tunnel, flight, "
                          "turbomachinery, rough wall), each entry a "
                          "disturbance spectrum. The stability solver "
                          "integrates growth from the spectrum; transition "
                          "is declared where integrated energy crosses the "
                          "breakdown threshold calibrated once per "
                          "mechanism family."),
            "confirm": ("Blind transition-location predictions within 10 "
                        "percent of chord on test wings in two different "
                        "disturbance environments."),
            "kill": ("If bypass mechanisms dominate most engineering "
                     "flows, the linear-growth integral is irrelevant "
                     "there and the library only helps the easy cases."),
            "notclaim": ("This does not claim to predict bypass or "
                         "roughness-dominated transition from theory; "
                         "those stay empirical. We do not know the "
                         "environment classes are stable enough to reuse "
                         "- that needs cross-facility comparison."),
        },
        "demo_spec": {
            "approach": ("Compute e^N amplification and the implied "
                         "transition Reynolds number."),
            "assume": [("N_factor", 9.0, "-"),
                       ("Re_per_m", 1e7, "1/m"),
                       ("x_chord_m", 1.0, "m")],
            "derived": [
                ("amplification", "2.718281828 ** N_factor"),
                ("Re_x", "Re_per_m * x_chord_m"),
                ("N_from_Re", "9.0 * (Re_x / 3e6) ** 0.15"),
                ("transition_flag", "1.0 if N_from_Re >= N_factor else 0.0"),
            ],
            "confirm": ("Blind predictions within 10 percent of chord in "
                        "two disturbance environments."),
            "refute": ("Bypass mechanisms dominate most engineering flows, "
                       "making the linear integral irrelevant there."),
        },
    },
    {
        "key": "drag-reduction",
        "name": "Turbulence Drag Reduction in Pipes and Channels",
        "group": "Turbulence and Fluids",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("How to cut turbulent skin-friction drag far below what "
                    "passive tricks achieve. Riblets and polymer additives "
                    "save roughly 10 percent; the dream is 30 to 50 percent "
                    "on demand, reversibly, without contaminating the fluid "
                    "- and no method has delivered it reliably at scale."),
        "background": ("Toms discovered in 1948 that tiny polymer additions "
                       "slash turbulent drag, an effect still not fully "
                       "explained. Shark-skin riblets, studied intensely in "
                       "the 1980s, give about 10 percent drag reduction by "
                       "impeding near-wall vortices; 3M even sold riblet "
                       "film for aircraft. Superhydrophobic surfaces promise "
                       "more but lose their air layer under pressure and "
                       "fouling. Active methods - wall oscillation, blowing "
                       "and suction - show 30-plus percent in labs but the "
                       "actuation energy eats the savings at scale. The "
                       "near-wall turbulence cycle is well described since "
                       "the 1990s, yet turning that understanding into a "
                       "practical large-area drag cutter remains open."),
        "why_it_matters": ("Skin friction is most of the drag on ships, "
                           "pipelines, and long-haul aircraft. Even a few "
                           "percent cut means megatons of fuel; tens of "
                           "percent would reshape shipping and aviation "
                           "economics."),
        "citations": [
            "Toms, B. A. Some Observations on the Flow of Linear Polymer "
            "Solutions. Proc. 1st Int. Congress on Rheology; 1948.",
            "Walsh, M. J. Riblets as a Viscous Drag Reduction Technique. "
            "AIAA Journal, vol. 21; 1983.",
            "Gad-el-Hak, M. Flow Control: Passive, Active, and Reactive Flow "
            "Management. Cambridge University Press; 2000.",
        ],
        "sig_pointer": ("The Signature approach pairs a durable passive "
                        "texture that weakens the near-wall cycle with "
                        "low-energy active pulses timed to the turbulence "
                        "bursting frequency, spending actuation energy only "
                        "where the cycle is vulnerable."),
        "sig": {
            "assumptions": ("The near-wall bursting cycle is the drag "
                            "engine. Passive textures can detune it "
                            "durably; short active pulses at the bursting "
                            "frequency can disrupt it at low energy cost."),
            "reasoning": ("Passive methods plateau near 10 percent and "
                          "active methods drown in actuation cost because "
                          "they fight turbulence continuously. Fight it "
                          "only at its vulnerable moment - the burst - on "
                          "top of a texture that already weakens the "
                          "cycle, and the energy budget may finally close."),
            "mechanism": ("A hybrid wall: micro-texture tuned to the "
                          "viscous length scale plus sparse actuators "
                          "firing short pulses phased to detected burst "
                          "events. A controller learns the local bursting "
                          "statistics and fires only then; net drag "
                          "reduction is measured against total energy in, "
                          "actuation included."),
            "confirm": ("Sustained net drag reduction above 25 percent "
                        "including actuation energy, over thousand-hour "
                        "durability runs."),
            "kill": ("If burst detection requires sensor densities that "
                     "cannot survive real fouling, or texture durability "
                     "fails in months, the hybrid cannot leave the lab."),
            "notclaim": ("This does not claim to beat the fundamental "
                         "limits of wall turbulence control; it claims a "
                         "practical operating point. We do not know the "
                         "sensors survive - that is the experiment that "
                         "matters."),
        },
        "demo_spec": {
            "approach": ("Compute drag power for a hull section and the "
                         "fuel value of a drag-reduction percentage."),
            "assume": [("area_m2", 3000.0, "m2"),
                       ("Cd", 0.003, "-"),
                       ("vel_ms", 8.0, "m/s"),
                       ("rho", 1025.0, "kg/m3"),
                       ("reduction_pct", 25.0, "pct")],
            "derived": [
                ("drag_N", "0.5 * rho * vel_ms ** 2 * Cd * area_m2"),
                ("power_MW", "drag_N * vel_ms / 1e6"),
                ("saved_MW", "power_MW * reduction_pct / 100.0"),
                ("saved_MWh_day", "saved_MW * 24.0"),
            ],
            "confirm": ("Net 25 percent reduction including actuation "
                        "energy over thousand-hour runs."),
            "refute": ("Burst sensors cannot survive fouling or texture "
                       "durability fails in months."),
        },
    },
    {
        "key": "nano-contact",
        "name": "Real Contact Area at the Nanoscale",
        "group": "Friction and Wear",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("How much area really touches when two surfaces meet. "
                    "The real contact area is a tiny fraction of the "
                    "apparent area and controls friction, electrical and "
                    "thermal contact resistance, and sealing - yet at the "
                    "nanoscale, where single asperities rule, continuum "
                    "models break down and atomistic simulations cannot "
                    "reach engineering scales."),
        "background": ("Greenwood and Williamson 1966 gave the classic "
                       "statistical asperity model; Persson 2001 provided "
                       "the multiscale contact theory now widely used. At "
                       "the nanoscale, atomic force microscopy can measure "
                       "single-asperity contact, and molecular dynamics can "
                       "simulate it - but MD handles nanometers and "
                       "nanoseconds while engineering contacts span "
                       "millimeters and hours. The scale gap means nobody "
                       "can compute, from first principles, the real area "
                       "of a practical contact, and contact resistance "
                       "predictions in connectors, switches, and thermal "
                       "interfaces still rely on fitted parameters."),
        "why_it_matters": ("Real contact area governs friction, wear, "
                           "electrical contact reliability, thermal "
                           "interfaces, and seals. Computing it would "
                           "rationalize design across electronics, power "
                           "systems, and machinery."),
        "citations": [
            "Greenwood, J. A. and Williamson, J. B. P. Contact of Nominally "
            "Flat Surfaces. Proc. Royal Society A, vol. 295; 1966.",
            "Persson, B. N. J. Theory of Rubber Friction and Contact "
            "Mechanics. J. Chemical Physics, vol. 115; 2001.",
            "Carpick, R. W. and Salmeron, M. Scratching the Surface: "
            "Fundamental Investigations of Tribology with Atomic Force "
            "Microscopy. Chemical Reviews, vol. 97; 1997.",
        ],
        "sig_pointer": ("The Signature approach stitches atomistic "
                        "single-asperity laws into the Persson multiscale "
                        "framework, so the nanoscale physics corrects the "
                        "continuum prediction instead of replacing it."),
        "sig": {
            "assumptions": ("Persson multiscale theory is structurally "
                            "right at the micro scale. Single-asperity "
                            "atomistic results can be distilled into "
                            "correction laws that plug into it."),
            "reasoning": ("Neither scale alone suffices: atomistics "
                          "cannot reach millimeters, continuum cannot see "
                          "atoms. Stitch them where they overlap - use "
                          "atomistic simulations to correct the "
                          "smallest-scale branch of the multiscale tree, "
                          "and let the continuum framework carry it up."),
            "mechanism": ("A corrected multiscale contact solver: the "
                          "Persson magnification integral runs as usual, "
                          "but the finest decade uses an atomistically "
                          "calibrated asperity law (adhesion-aware, "
                          "size-dependent hardness). Output is real area, "
                          "pressure distribution, and contact resistance "
                          "from one measured topography."),
            "confirm": ("Predicted contact resistance and stiffness match "
                        "measurements on nano-engineered surfaces within "
                        "30 percent with no per-surface fitting."),
            "kill": ("If the atomistic correction depends sensitively on "
                     "surface chemistry that varies uncontrollably, the "
                     "stitch adds parameters instead of removing them."),
            "notclaim": ("This does not claim to simulate engineering "
                         "contacts atomistically; it claims a corrected "
                         "continuum. We do not know the correction is "
                         "chemistry-robust - that needs a chemistry "
                         "sweep."),
        },
        "demo_spec": {
            "approach": ("Hertz single-asperity contact radius and mean "
                         "pressure at the nanoscale."),
            "assume": [("load_uN", 100.0, "uN"),
                       ("radius_nm", 50.0, "nm"),
                       ("E_GPa", 150.0, "GPa")],
            "derived": [
                ("a_nm", "((3.0 * load_uN * 1e-6 * radius_nm * 1e-9) / (4.0 * E_GPa * 1e9)) ** (1.0/3.0) * 1e9"),
                ("area_nm2", "3.14159265 * a_nm ** 2"),
                ("p_mean_GPa", "load_uN * 1e-6 / (3.14159265 * (a_nm * 1e-9) ** 2) / 1e9"),
            ],
            "confirm": ("Resistance and stiffness match measurements "
                        "within 30 percent with no per-surface fitting."),
            "refute": ("Atomistic correction depends on uncontrollable "
                       "surface chemistry, adding parameters."),
        },
    },
    {
        "key": "galling",
        "name": "Adhesive Wear and Galling",
        "group": "Friction and Wear",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("How to predict when sliding metal surfaces will seize "
                    "by galling - adhesive wear so severe that material "
                    "transfers and the joint welds itself. Galling strikes "
                    "stainless fasteners, valves, and forming dies without "
                    "warning, and the standard defense is still material "
                    "selection charts plus anti-seize compounds."),
        "background": ("Adhesive wear theory goes back to Bowden and Tabor: "
                       "clean metal asperities cold-weld, then tear. "
                       "Galling is adhesive wear runaway - once transfer "
                       "starts, the transferred lumps plow deeper, and the "
                       "contact degrades catastrophically within strokes. "
                       "The galling threshold stress is measured by tests "
                       "like ASTM G98 (button-on-block) and G196 "
                       "(galling resistance), which rank materials but do "
                       "not predict whether a specific design at a specific "
                       "load will gall. Austenitic stainless steels are "
                       "notorious; nitrogen-strengthened grades and "
                       "special alloys resist better, for reasons still "
                       "debated at the dislocation level."),
        "why_it_matters": ("Galled threads seize assemblies, galled valves "
                           "stick, galled dies scrap parts. Predicting the "
                           "threshold would let engineers design stainless "
                           "systems with confidence instead of over-"
                           "specifying exotic alloys."),
        "citations": [
            "ASTM G98-17. Standard Test Method for Galling Resistance of "
            "Materials.",
            "ASTM G196-08. Standard Test Method for Galling Resistance of "
            "Material Couples.",
            "Bhansali, K. J. and Miller, A. E. The Role of Stacking Fault "
            "Energy on Galling. Wear, vol. 75; 1982.",
        ],
        "sig_pointer": ("The Signature approach computes a galling index "
                        "from contact pressure, sliding distance per "
                        "stroke, and a material transfer-resistance score, "
                        "giving a go/no-go threshold per design."),
        "sig": {
            "assumptions": ("Galling initiates when local adhesive junctions "
                            "grow faster than they are worn away - a race "
                            "set by pressure, sliding, and the material "
                            "pair transfer resistance."),
            "reasoning": ("Tests rank materials because they hold geometry "
                          "fixed and vary the pair. Designs vary geometry "
                          "and hold the pair fixed - the untested "
                          "direction. A threshold model that takes both "
                          "sides as inputs turns the test data into design "
                          "data."),
            "mechanism": ("A galling index: normalized contact pressure "
                          "times a sliding-severity term, divided by a "
                          "pair-specific transfer resistance calibrated "
                          "from G98/G196 data. Index above one predicts "
                          "galling initiation within the service stroke "
                          "count; the model also flags the pressure "
                          "peaks to redesign."),
            "confirm": ("Index correctly classifies gall/no-gall on a "
                        "blind set of fastener and valve geometries with "
                        "90 percent accuracy."),
            "kill": ("If transfer resistance proves geometry-dependent - "
                     "the same pair galls differently in different "
                     "contacts beyond pressure effects - the index cannot "
                     "transfer and the approach fails."),
            "notclaim": ("This does not claim to capture lubricant "
                         "breakdown or temperature excursions; those are "
                         "separate triggers. We do not know the pair "
                         "database is wide enough - exotic pairs need "
                         "testing."),
        },
        "demo_spec": {
            "approach": ("Compute a galling index from contact pressure "
                         "over threshold and sliding severity."),
            "assume": [("pressure_MPa", 450.0, "MPa"),
                       ("threshold_MPa", 380.0, "MPa"),
                       ("stroke_mm", 12.0, "mm"),
                       ("strokes", 5000.0, "-")],
            "derived": [
                ("pressure_ratio", "pressure_MPa / threshold_MPa"),
                ("slide_m", "stroke_mm / 1000.0 * strokes"),
                ("gall_index", "pressure_ratio * (1.0 + slide_m / 1000.0)"),
                ("gall_flag", "1.0 if gall_index > 1.0 else 0.0"),
            ],
            "confirm": ("Index classifies gall/no-gall on blind geometries "
                        "with 90 percent accuracy."),
            "refute": ("Transfer resistance proves geometry-dependent "
                       "beyond pressure effects."),
        },
    },
    {
        "key": "multiphase",
        "name": "Multiphase Flow Regime Prediction",
        "group": "Turbulence and Fluids",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("How to predict which flow pattern - bubbly, slug, "
                    "annular, stratified - a gas-liquid mixture will adopt "
                    "in a pipe. Flow regime sets pressure drop and heat "
                    "transfer, yet regime maps are still empirical charts "
                    "(Baker 1954, Taitel-Dukler 1976) that fail outside "
                    "their fitted conditions."),
        "background": ("Baker published his empirical flow-pattern map in "
                       "1954; Taitel and Dukler gave it a mechanistic "
                       "foundation in 1976 with stability criteria for "
                       "stratified flow. Since then the maps have been "
                       "extended, re-fitted, and argued over, but the core "
                       "problem persists: regime boundaries shift with "
                       "fluid properties, pipe diameter, inclination, and "
                       "heat transfer in ways the maps do not capture. "
                       "Slug flow in particular - liquid slugs hammering "
                       "through pipelines - causes vibration and damage, "
                       "and predicting the bubbly-to-slug transition for a "
                       "new fluid pair is still closer to art than science."),
        "why_it_matters": ("Oil and gas pipelines, chemical reactors, "
                           "nuclear cooling, and refrigeration all run "
                           "multiphase flows. Wrong-regime prediction means "
                           "wrong pressure drop, flow-induced vibration, "
                           "and sometimes ruptured lines."),
        "citations": [
            "Baker, O. Simultaneous Flow of Oil and Gas. Oil and Gas Journal, "
            "vol. 53; 1954.",
            "Taitel, Y. and Dukler, A. E. A Model for Predicting Flow Regime "
            "Transitions in Horizontal and Near Horizontal Gas-Liquid Flow. "
            "AIChE Journal, vol. 22; 1976.",
            "Brennen, C. E. Fundamentals of Multiphase Flow. Cambridge "
            "University Press; 2005.",
        ],
        "sig_pointer": ("The Signature approach predicts regime from a "
                        "stability analysis of the interface computed for "
                        "the actual fluids and geometry, replacing the "
                        "fitted map with a computed boundary."),
        "sig": {
            "assumptions": ("Regime boundaries are stability boundaries of "
                            "the interface - Kelvin-Helmholtz and "
                            "Rayleigh-Taylor type. Given fluid properties "
                            "and geometry, the dominant instability is "
                            "computable."),
            "reasoning": ("Empirical maps fail because they interpolate "
                          "between fitted points in a space with too many "
                          "dimensions. Compute the boundary instead: for "
                          "each candidate interface configuration, test "
                          "its stability to the relevant disturbances, "
                          "and the stable configuration is the regime."),
            "mechanism": ("A regime engine: given fluids, pipe, and flow "
                          "rates, it evaluates interface stability for "
                          "stratified, annular, and dispersed "
                          "configurations using one-dimensional stability "
                          "criteria with fluid-property inputs. The "
                          "winning configuration sets the closure laws "
                          "for pressure drop - no map lookup."),
            "confirm": ("Predicted regime boundaries match new fluid-pair "
                        "experiments within the measurement uncertainty of "
                        "the boundary, without refitting."),
            "kill": ("If three-dimensional and entrance effects dominate "
                     "real transitions, the 1D stability criteria miss the "
                     "boundary systematically and the engine is no better "
                     "than a map."),
            "notclaim": ("This does not claim to resolve slug dynamics in "
                         "detail; it claims the regime boundary. We do not "
                         "know the criteria cover microgravity or "
                         "supercritical fluids - those need dedicated "
                         "validation."),
        },
        "demo_spec": {
            "approach": ("Compute mixture velocity and Froude number as "
                         "regime indicators for horizontal flow."),
            "assume": [("v_gas_ms", 3.0, "m/s"),
                       ("v_liq_ms", 1.0, "m/s"),
                       ("gas_frac", 0.6, "-"),
                       ("diam_m", 0.1, "m")],
            "derived": [
                ("v_mix", "v_gas_ms * gas_frac + v_liq_ms * (1.0 - gas_frac)"),
                ("froude", "v_mix / (9.81 * diam_m) ** 0.5"),
                ("slip", "v_gas_ms / v_liq_ms"),
                ("slug_risk", "1.0 if 0.3 < gas_frac < 0.8 and froude < 3.0 else 0.0"),
            ],
            "confirm": ("Predicted boundaries match new fluid-pair "
                        "experiments without refitting."),
            "refute": ("3D and entrance effects dominate; 1D criteria miss "
                       "boundaries systematically."),
        },
    },
]
ENTRIES += [
    {
        "key": "flutter",
        "name": "Flutter and Aeroelastic Instability",
        "group": "Soft Robotics and Control",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("How to predict the exact speed where a wing, blade, or "
                    "bridge deck starts fluttering - self-feeding vibration "
                    "where aerodynamics pump energy into the structure. "
                    "Flutter destroyed the Tacoma Narrows Bridge in 1940 and "
                    "still sets the speed limits of aircraft, yet prediction "
                    "for real flexible structures in real flows remains "
                    "uncertain enough to demand expensive flight testing."),
        "background": ("Collar 1946 framed aeroelasticity as the triangle of "
                       "aerodynamic, elastic, and inertial forces. Classical "
                       "flutter analysis couples structural modes with "
                       "unsteady aerodynamics (Theodorsen 1935 for airfoils) "
                       "and finds the speed where damping goes negative. "
                       "The theory works beautifully for clean wings in "
                       "smooth flow; reality adds transonic shocks, "
                       "separated flow, structural nonlinearity, and free "
                       "play in control surfaces - the domain of "
                       "limit-cycle oscillation, where the structure "
                       "flutters at bounded amplitude instead of diverging. "
                       "Predicting limit-cycle amplitude for a real wing "
                       "with worn hinges is still beyond reliable "
                       "computation, so flutter clearance is proven in "
                       "flight test, cautiously and expensively."),
        "why_it_matters": ("Flutter sets the flight envelope of every "
                           "aircraft and the safety of long-span bridges "
                           "and wind-turbine blades. Better prediction "
                           "would cut flight-test risk and let designers "
                           "use lighter, more flexible structures."),
        "citations": [
            "Collar, A. R. The Expanding Domain of Aeroelasticity. J. Royal "
            "Aeronautical Society, vol. 50; 1946.",
            "Theodorsen, T. General Theory of Aerodynamic Instability and the "
            "Mechanism of Flutter. NACA Report 496; 1935.",
            "Dowell, E. H. et al. A Modern Course in Aeroelasticity, 5th ed. "
            "Springer; 2014.",
        ],
        "sig_pointer": ("The Signature approach computes the flutter "
                        "boundary as a probability distribution over "
                        "structural uncertainties, and predicts limit-cycle "
                        "amplitude from measured free play rather than "
                        "assuming ideal hinges."),
        "sig": {
            "assumptions": ("Classical unsteady aerodynamics is adequate "
                            "outside transonic separated regimes. The "
                            "dominant uncertainty is structural - mode "
                            "shapes, damping, free play - not aerodynamic."),
            "reasoning": ("Flutter analysis fails in practice because it "
                          "consumes nominal structural data while real "
                          "structures vary. Propagate the variation: run "
                          "the flutter solution over the measured "
                          "uncertainty distribution and the boundary "
                          "becomes a probability, which is what flight "
                          "test actually needs."),
            "mechanism": ("A probabilistic flutter solver: structural "
                          "modes and damping from ground-vibration test "
                          "statistics feed a Monte-Carlo flutter "
                          "solution, yielding a flutter-speed "
                          "distribution. Free-play measurements feed a "
                          "nonlinear limit-cycle solver for amplitude. "
                          "Clearance is granted on probability, not on a "
                          "single nominal number."),
            "confirm": ("Predicted flutter-speed distributions bracket "
                        "observed flight-test flutter onsets on two "
                        "aircraft configurations."),
            "kill": ("If aerodynamic uncertainty dominates - transonic "
                     "shock motion swamps structural scatter - the "
                     "probabilistic structure model adds little and the "
                     "approach fails where it matters."),
            "notclaim": ("This does not claim to replace flutter flight "
                         "testing; it claims to make it safer and "
                         "shorter. We do not know the uncertainty model "
                         "is complete - unmodeled nonlinearities may "
                         "dominate."),
        },
        "demo_spec": {
            "approach": ("Estimate reduced frequency and a flutter-margin "
                         "proxy from bending/torsion frequencies."),
            "assume": [("f_bend_hz", 8.0, "Hz"),
                       ("f_tors_hz", 12.0, "Hz"),
                       ("vel_ms", 90.0, "m/s"),
                       ("chord_m", 1.2, "m")],
            "derived": [
                ("omega", "2.0 * 3.14159265 * f_bend_hz"),
                ("k_reduced", "omega * chord_m / (2.0 * vel_ms)"),
                ("freq_ratio", "f_tors_hz / f_bend_hz"),
                ("margin_flag", "1.0 if freq_ratio > 1.2 and k_reduced < 0.5 else 0.0"),
            ],
            "confirm": ("Predicted distributions bracket observed "
                        "flight-test flutter onsets."),
            "refute": ("Aerodynamic uncertainty dominates; structural "
                       "probabilism adds little."),
        },
    },
    {
        "key": "thermoacoustic",
        "name": "Thermoacoustic Instability in Combustors",
        "group": "Soft Robotics and Control",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("How to predict and kill the screaming instabilities "
                    "that destroy gas-turbine and rocket combustors. When "
                    "heat release couples with acoustics, pressure "
                    "oscillations grow until hardware fails - the F-1 "
                    "engine program fought it for years - yet designers "
                    "still discover instabilities in testing, not on the "
                    "computer."),
        "background": ("Rayleigh stated the criterion in 1878: heat added "
                       "in phase with pressure oscillations drives them. "
                       "Rocket programs learned it painfully - the F-1 "
                       "combustion instability delayed Apollo, and the "
                       "space shuttle main engine fought pogo and "
                       "instability modes. Modern lean-premixed gas "
                       "turbines, built for low NOx, are especially prone: "
                       "the flame sits near the stability boundary by "
                       "design. Low-order network models with flame "
                       "transfer functions predict onset for simple "
                       "geometries, but real annular combustors with "
                       "azimuthal modes, staging, and transient operation "
                       "still surprise engineers in full-scale tests."),
        "why_it_matters": ("Thermoacoustic instability destroys combustors "
                           "worth millions and limits how clean and "
                           "efficient turbines and rockets can run. "
                           "Prediction would let designers build stable "
                           "low-emission combustors the first time."),
        "citations": [
            "Rayleigh, Lord. The Explanation of Certain Acoustical Phenomena. "
            "Nature, vol. 18; 1878.",
            "Lieuwen, T. C. and Yang, V. (eds.) Combustion Instabilities in "
            "Gas Turbine Engines. AIAA; 2005.",
            "Culick, F. E. C. Unsteady Motions in Combustion Chambers for "
            "Propulsion Systems. AGARDograph; 2006.",
        ],
        "sig_pointer": ("The Signature approach maps the combustor "
                        "stability as a landscape over operating "
                        "conditions from a calibrated low-order model, "
                        "and steers operation along stable valleys with "
                        "active fuel staging."),
        "sig": {
            "assumptions": ("The Rayleigh mechanism dominates; flame "
                            "response is capturable by a measured flame "
                            "transfer function. Operating-condition space "
                            "is mappable by a calibrated low-order model."),
            "reasoning": ("Instabilities are discovered in testing "
                          "because stability is evaluated at design "
                          "points, not mapped across the operating "
                          "envelope. Map the whole envelope with a "
                          "calibrated low-order model, find the stable "
                          "valleys, and operate in them - with active "
                          "staging as the steering wheel."),
            "mechanism": ("A stability landscape: the low-order network "
                          "model, calibrated by single-burner flame "
                          "transfer measurements, computes growth rates "
                          "over the full load-speed-fuel-split space. "
                          "Control logic keeps operation in stable "
                          "valleys and uses fast fuel staging to damp "
                          "excursions, with the landscape recomputed as "
                          "hardware ages."),
            "confirm": ("Landscape predicts the unstable operating zones "
                        "found in full-scale tests before the test runs, "
                        "on two combustor families."),
            "kill": ("If flame transfer functions do not transfer from "
                     "single-burner rigs to the annular engine - "
                     "multi-burner coupling dominates - the landscape is "
                     "drawn from the wrong map."),
            "notclaim": ("This does not claim to model the nonlinear "
                         "limit-cycle amplitude precisely; it claims the "
                         "stability boundary. We do not know the "
                         "landscape stays valid as hardware degrades - "
                         "recalibration strategy is unproven."),
        },
        "demo_spec": {
            "approach": ("Compute a Rayleigh-index proxy and growth-rate "
                         "estimate from pressure oscillation level."),
            "assume": [("p_bar_Pa", 20e5, "Pa"),
                       ("p_prime_pct", 5.0, "pct"),
                       ("freq_hz", 400.0, "Hz"),
                       ("damping_1ps", 50.0, "1/s")],
            "derived": [
                ("p_prime_Pa", "p_bar_Pa * p_prime_pct / 100.0"),
                ("rayleigh_W", "p_prime_Pa * freq_hz * 0.01"),
                ("growth_1ps", "rayleigh_W / p_bar_Pa * 1e6 - damping_1ps"),
                ("unstable_flag", "1.0 if growth_1ps > 0.0 else 0.0"),
            ],
            "confirm": ("Landscape predicts unstable zones found in "
                        "full-scale tests before they run."),
            "refute": ("Flame transfer functions do not transfer from rig "
                       "to annular engine."),
        },
    },
    {
        "key": "metamaterial-scale",
        "name": "Metamaterial Manufacturing at Scale",
        "group": "Manufacturing and Metamaterials",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("How to manufacture mechanical metamaterials - "
                    "structures with impossible-seeming properties from "
                    "their architecture - at the scale and cost of real "
                    "products. Lab samples show negative Poisson ratios, "
                    "programmable stiffness, and wave-guiding behavior, "
                    "but scaling from centimeter coupons to square meters "
                    "of affordable product has stalled."),
        "background": ("Veselago theorized negative-index media in 1968; "
                       "Pendry 2000 and Shelby et al. 2001 demonstrated "
                       "them for electromagnetics, and the mechanical "
                       "analogue followed: Lakes 1987 foams with negative "
                       "Poisson ratio, then the modern wave of "
                       "architected lattices, origami mechanisms, and "
                       "pentamode structures. The properties come from "
                       "geometry, so in principle any base material works "
                       "- but geometry at the needed precision over large "
                       "areas is the wall. Additive manufacturing prints "
                       "beautiful coupons slowly and expensively; "
                       "conventional processes cannot make the "
                       "architectures at all. The field has a library of "
                       "wonders and almost no products."),
        "why_it_matters": ("Scalable metamaterials would deliver "
                           "ultralight structures, perfect shock "
                           "absorbers, acoustic cloaks, and programmable "
                           "mechanical logic. Manufacturing is the gap "
                           "between the library and the world."),
        "citations": [
            "Lakes, R. S. Foam Structures with a Negative Poisson Ratio. "
            "Science, vol. 235; 1987.",
            "Fleck, N. A., Deshpande, V. S. and Ashby, M. F. Micro-"
            "Architectured Materials. Proc. Royal Society A, vol. 466; 2010.",
            "Schaedler, T. A. et al. Ultralight Metallic Microlattices. "
            "Science, vol. 334; 2011.",
        ],
        "sig_pointer": ("The Signature approach redesigns metamaterial "
                        "architectures for the process, not the printer - "
                        "self-assembling and sheet-folding geometries that "
                        "a factory can actually make by the square meter."),
        "sig": {
            "assumptions": ("Many metamaterial properties survive "
                            "geometric simplification; the exotic behavior "
                            "needs the right topology, not nanometer "
                            "precision. Sheet-based and self-assembling "
                            "processes can hit the needed tolerances."),
            "reasoning": ("The field designs for the printer and then "
                          "despairs at scale. Invert it: design for "
                          "stamping, folding, and self-assembly first, "
                          "then search the architected-property space "
                          "within what those processes can make. Lose "
                          "some performance, gain manufacturability - "
                          "that trade is how every material became a "
                          "product."),
            "mechanism": ("A process-first design loop: the architected "
                          "cell is parameterized for sheet folding or "
                          "self-assembly constraints; an optimizer "
                          "searches the constrained space for target "
                          "properties (stiffness, Poisson ratio, energy "
                          "absorption). Pilot lines use roll-forming and "
                          "programmed folding to produce panel-scale "
                          "demonstrators."),
            "confirm": ("Panel-scale demonstrators (square meter) holding "
                        "at least 70 percent of coupon properties at "
                        "one-tenth the coupon cost per area."),
            "kill": ("If the target properties fundamentally need "
                     "precision the cheap processes cannot hold, the "
                     "constrained search finds nothing worth making and "
                     "the approach fails."),
            "notclaim": ("This does not claim all metamaterials scale; "
                         "many will stay lab wonders. We do not know "
                         "which property families survive simplification "
                         "- the search itself is the experiment."),
        },
        "demo_spec": {
            "approach": ("Scale a metamaterial panel: unit count, build "
                         "time, and cost per area vs coupon."),
            "assume": [("unit_mm", 2.0, "mm"),
                       ("target_m2", 1.0, "m2"),
                       ("units_per_hour", 5000.0, "-"),
                       ("coupon_cost_per_m2", 4000.0, "USD/m2")],
            "derived": [
                ("units_needed", "target_m2 / (unit_mm / 1000.0) ** 2"),
                ("hours", "units_needed / units_per_hour"),
                ("target_cost_per_m2", "coupon_cost_per_m2 / 10.0"),
                ("units_per_m2", "units_needed / target_m2"),
            ],
            "confirm": ("Square-meter panels hold 70 percent of coupon "
                        "properties at one-tenth the cost."),
            "refute": ("Target properties need precision cheap processes "
                       "cannot hold; the search finds nothing."),
        },
    },
    {
        "key": "soft-robot-control",
        "name": "Soft Robot Control (Infinite Degrees of Freedom)",
        "group": "Soft Robotics and Control",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("How to control a robot made of squishy material with, "
                    "in principle, infinite degrees of freedom. Soft "
                    "robots promise safe, adaptable machines, but their "
                    "bodies deform continuously - no joints, no encoders - "
                    "so the control theory built for rigid robots does "
                    "not apply, and most soft robots still run on "
                    "hand-tuned open-loop gaits."),
        "background": ("Whitesides group 2011 pneumatic soft robots kicked "
                       "off the modern field: cheap, compliant, safe "
                       "around humans. The control problem is fundamental: "
                       "a soft arm is a continuum, and the standard "
                       "reduction - piecewise constant curvature (PCC) - "
                       "is a coarse approximation that breaks under load "
                       "and contact. Proprioception is hard because the "
                       "sensors must stretch with the body; embedded "
                       "flex sensors, liquid-metal strain gauges, and "
                       "optical fibers all drift and hysteresis. "
                       "Model-based control exists in labs using FEM and "
                       "reduced-order models, but real-time closed-loop "
                       "control of a soft manipulator doing useful work "
                       "remains rare."),
        "why_it_matters": ("Soft robots could work safely alongside "
                           "people, handle fragile objects, and go where "
                           "rigid robots cannot - surgery, disaster "
                           "response, food handling. Control is the "
                           "bottleneck between demos and tools."),
        "citations": [
            "Rus, D. and Tolley, M. T. Design, Fabrication and Control of "
            "Soft Robots. Nature, vol. 521; 2015.",
            "Webster, R. J. and Jones, B. A. Design and Kinematic Modeling "
            "of Constant Curvature Continuum Robots. Int. J. Robotics "
            "Research, vol. 29; 2010.",
            "Della Santina, C. et al. Model-Based Control of Soft Robots. "
            "IEEE Control Systems Magazine, vol. 43; 2023.",
        ],
        "sig_pointer": ("The Signature approach controls the soft body "
                        "through a learned low-dimensional latent model "
                        "that updates from embedded stretch sensors, "
                        "closing the loop in the latent space instead of "
                        "the infinite-dimensional body."),
        "sig": {
            "assumptions": ("The soft body useful motions live on a low-"
                            "dimensional manifold despite the continuum. "
                            "Embedded stretch sensors observe it "
                            "sufficiently for feedback."),
            "reasoning": ("Rigid-robot control failed here because it "
                          "demands a joint model the body does not have. "
                          "Learn the body own coordinates instead: find "
                          "the latent space the motions actually occupy, "
                          "identify its dynamics from data, and control "
                          "there - the infinite DOF become a handful."),
            "mechanism": ("A latent-dynamics controller: offline, motion-"
                          "capture and sensor data learn an encoder from "
                          "sensor readings to a low-dimensional state "
                          "plus its dynamics; online, an MPC controller "
                          "plans in the latent space at control rate, "
                          "mapping commands back to actuator pressures. "
                          "The model re-identifies periodically as the "
                          "material ages."),
            "confirm": ("Closed-loop trajectory tracking on a soft "
                        "manipulator under varying payloads with error "
                        "below 5 percent of reach, sustained over weeks."),
            "kill": ("If sensor drift and hysteresis make the latent "
                     "state unobservable in practice - the encoder "
                     "cannot be trusted week to week - the loop cannot "
                     "close and the approach fails."),
            "notclaim": ("This does not claim to model contact-rich "
                         "manipulation; contact stays an open problem. "
                         "We do not know the manifold stays stable as "
                         "elastomers fatigue - long-duration trials are "
                         "needed."),
        },
        "demo_spec": {
            "approach": ("Size the latent state and control compute for a "
                         "segmented soft arm."),
            "assume": [("segments", 6.0, "-"),
                       ("dof_per_seg", 3.0, "-"),
                       ("ctrl_hz", 100.0, "Hz"),
                       ("latent_dim", 8.0, "-")],
            "derived": [
                ("full_state_dim", "segments * dof_per_seg * 2.0"),
                ("compression", "full_state_dim / latent_dim"),
                ("updates_per_s", "ctrl_hz"),
                ("flops_per_update", "latent_dim ** 3 * 10.0"),
            ],
            "confirm": ("Closed-loop tracking below 5 percent of reach "
                        "error under varying payloads, sustained."),
            "refute": ("Sensor drift makes the latent state unobservable "
                       "week to week; the loop cannot close."),
        },
    },
    {
        "key": "microrobot-swim",
        "name": "Microrobot Swimming in Viscous Fluids",
        "group": "Soft Robotics and Control",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("How to make microscopic robots swim where viscosity "
                    "rules and inertia is irrelevant. At the microscale, "
                    "water feels like honey - Purcell scallop theorem "
                    "says reciprocal motions go nowhere - yet targeted "
                    "drug delivery and microsurgery need swimmers that "
                    "actually get somewhere."),
        "background": ("Purcell 1977 lecture on life at low Reynolds "
                       "number showed why microorganisms use rotating "
                       "helices and beating cilia instead of paddling: "
                       "reciprocal motion produces zero net displacement. "
                       "Artificial microswimmers followed: magnetic "
                       "helices (Ghosh and Fischer 2009), flexible "
                       "magnetic filaments, acoustic swimmers. They work "
                       "in labs, but real biological fluids are "
                       "non-Newtonian, crowded with cells, and full of "
                       "flows; swarm control is unsolved; and powering "
                       "them without tethers at depth in tissue remains "
                       "hard. The gap between a swimmer in water and a "
                       "swimmer in blood doing a job is the unsolved "
                       "part."),
        "why_it_matters": ("Microswimmers could deliver drugs to exact "
                           "cells, clear clots, and perform microsurgery "
                           "without incisions. Locomotion that works in "
                           "real biological fluids is the enabling step."),
        "citations": [
            "Purcell, E. M. Life at Low Reynolds Number. American J. Physics, "
            "vol. 45; 1977.",
            "Ghosh, A. and Fischer, P. Controlled Propulsion of Artificial "
            "Magnetic Nanostructured Propellers. Nano Letters, vol. 9; 2009.",
            "Nelson, B. J., Kaliakatsos, I. K. and Abbott, J. J. Microrobots "
            "for Minimally Invasive Medicine. Annual Review of Biomedical "
            "Engineering, vol. 12; 2010.",
        ],
        "sig_pointer": ("The Signature approach designs swimmers for the "
                        "actual fluid - non-Newtonian, crowded - using "
                        "gait optimization in simulated biological media, "
                        "and steers swarms with global fields plus local "
                        "gait switching."),
        "sig": {
            "assumptions": ("Useful gaits for biological fluids can be "
                            "found by optimization in rheologically "
                            "faithful simulations. Global magnetic or "
                            "acoustic fields can address swarms; local "
                            "gait switching gives individuality."),
            "reasoning": ("Lab swimmers are optimized for water, then "
                          "fail in blood - the design fluid is wrong. "
                          "Optimize in the real medium from the start, "
                          "using measured rheology of the target fluid, "
                          "and the scallop theorem is satisfied by "
                          "construction rather than hoped for."),
            "mechanism": ("A gait-optimization pipeline: the swimmer "
                          "geometry and actuation are optimized against a "
                          "non-Newtonian fluid model fitted to the target "
                          "biofluid. Swarms are driven by a global field "
                          "with per-swimmer gait modes switched by field "
                          "frequency - one broadcast signal, many "
                          "behaviors."),
            "confirm": ("Optimized swimmers out-swim water-optimized "
                        "designs by 3x in blood-analog fluid, and hold "
                        "formation under flow."),
            "kill": ("If biological variability swamps the optimization - "
                     "every patient fluid needs its own swimmer - the "
                     "pipeline cannot produce a general device."),
            "notclaim": ("This does not claim to solve powering at depth "
                         "or biocompatibility; those are separate walls. "
                         "We do not know the fluid models are faithful "
                         "enough - in-vivo validation is the real test."),
        },
        "demo_spec": {
            "approach": ("Compute Reynolds number and Stokes drag for a "
                         "microswimmer to confirm the viscous regime."),
            "assume": [("length_um", 20.0, "um"),
                       ("vel_ums", 50.0, "um/s"),
                       ("visc_Pas", 0.004, "Pa s"),
                       ("rho", 1060.0, "kg/m3")],
            "derived": [
                ("Re", "rho * vel_ums * 1e-6 * length_um * 1e-6 / visc_Pas"),
                ("radius_m", "length_um * 1e-6 / 4.0"),
                ("stokes_nN", "6.0 * 3.14159265 * visc_Pas * radius_m * vel_ums * 1e-6 * 1e9"),
                ("body_lengths_ps", "vel_ums / length_um"),
            ],
            "confirm": ("Optimized swimmers out-swim water designs 3x in "
                        "blood-analog fluid."),
            "refute": ("Patient-to-patient fluid variability swamps the "
                       "optimization; no general device emerges."),
        },
    },
    {
        "key": "topology-opt",
        "name": "Topology Optimization to Manufacturable Parts at Scale",
        "group": "Manufacturing and Metamaterials",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": ("How to turn topology-optimized designs - the "
                    "organic-looking, mathematically optimal structures - "
                    "into parts a factory can actually make affordably. "
                    "Optimizers produce shapes with enclosed voids, "
                    "unmachinable undercuts, and member sizes no process "
                    "holds; the human reinterpretation step is slow, "
                    "subjective, and loses the optimality."),
        "background": ("Bendsoe and Kikuchi 1988 homogenization method "
                       "founded modern topology optimization; the SIMP "
                       "method made it practical. Optimized designs "
                       "routinely cut weight 30 to 50 percent versus "
                       "conventional designs, and aerospace now flies "
                       "topology-optimized brackets. But the raw output "
                       "is a density field, not a part: it needs "
                       "interpretation into CAD, then manufacturability "
                       "fixes that can destroy the performance gain. "
                       "Manufacturing constraints (minimum member size, "
                       "draft angles, overhang limits for printing) can be "
                       "added to the optimizer, yet the constrained "
                       "optimum for real multi-process factories - "
                       "choosing the process as well as the shape - is "
                       "still an open problem."),
        "why_it_matters": ("Lightweight optimal structures save fuel and "
                           "material across transport and industry. "
                           "Closing the optimizer-to-factory gap would "
                           "put mathematically optimal parts into mass "
                           "production."),
        "citations": [
            "Bendsoe, M. P. and Kikuchi, N. Generating Optimal Topologies in "
            "Structural Design Using a Homogenization Method. Computer Methods "
            "in Applied Mechanics and Engineering, vol. 71; 1988.",
            "Bendsoe, M. P. and Sigmund, O. Topology Optimization: Theory, "
            "Methods, and Applications. Springer; 2003.",
            "Zhu, J.-H., Zhang, W.-H. and Xia, L. Topology Optimization in "
            "Aircraft and Aerospace Structures Design. Archives of "
            "Computational Methods in Engineering, vol. 23; 2016.",
        ],
        "sig_pointer": ("The Signature approach optimizes shape and "
                        "process choice together, with the factory "
                        "capability map inside the optimizer loop, so the "
                        "output is a process-specific part, not a density "
                        "field needing translation."),
        "sig": {
            "assumptions": ("Manufacturing constraints are expressible as "
                            "optimizer constraints without destroying "
                            "convergence. The factory capability map - "
                            "tolerances, processes, costs - is knowable."),
            "reasoning": ("The gap exists because optimization and "
                          "manufacturing speak different languages: "
                          "density fields vs process plans. Put the "
                          "factory inside the optimizer - its real "
                          "constraints and costs - and co-optimize shape "
                          "with process selection; the output needs no "
                          "translation because it was born in factory "
                          "language."),
            "mechanism": ("A co-optimization loop: the topology optimizer "
                          "carries manufacturing-constraint filters "
                          "(minimum length scale, overhang, draft) plus a "
                          "process-selection variable per region with "
                          "associated cost. The objective blends "
                          "compliance and manufactured cost; the result is "
                          "a part plus its process plan, ready for the "
                          "floor."),
            "confirm": ("Co-optimized parts manufactured as-specified "
                        "achieve within 10 percent of predicted stiffness "
                        "at the predicted cost, on two different "
                        "processes."),
            "kill": ("If the constraint set makes the optimization "
                     "intractable at real mesh sizes - or the optimum "
                     "keeps collapsing to trivial shapes - the joint "
                     "formulation is unusable."),
            "notclaim": ("This does not claim global optimality; "
                         "manufacturing-constrained optima are local by "
                         "nature. We do not know factories will share "
                         "honest capability maps - that is a business "
                         "problem as much as a technical one."),
        },
        "demo_spec": {
            "approach": ("Estimate optimization compute load and the "
                         "weight-saving value of the optimized part."),
            "assume": [("elements", 1e6, "-"),
                       ("iterations", 200.0, "-"),
                       ("sec_per_iter", 45.0, "s"),
                       ("weight_save_kg", 12.0, "kg"),
                       ("fuel_val_per_kg", 800.0, "USD/kg")],
            "derived": [
                ("opt_hours", "elements / 1e6 * iterations * sec_per_iter / 3600.0"),
                ("value_usd", "weight_save_kg * fuel_val_per_kg"),
                ("dof_millions", "elements * 3.0 / 1e6"),
            ],
            "confirm": ("As-specified parts hit predicted stiffness "
                        "within 10 percent at predicted cost."),
            "refute": ("Constraints make optimization intractable at real "
                       "mesh sizes or collapse to trivial shapes."),
        },
    },
]
ENTRIES += [
    # ------------------------------------------------------------ advanced
    {
        "key": "compliant-fatigue",
        "name": "Compliant Mechanism Fatigue",
        "group": "Manufacturing and Metamaterials",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("How to predict the fatigue life of compliant mechanisms "
                    "- machines that move by bending flexures instead of "
                    "sliding joints. They promise zero backlash and no wear, "
                    "but their thin flexures see large cyclic strains where "
                    "standard fatigue data does not apply, and life "
                    "prediction is still guesswork."),
        "background": ("Howell BYU work systematized compliant mechanisms "
                       "in the 1990s-2000s: the pseudo-rigid-body model "
                       "lets designers treat flexures as joints with "
                       "torsional springs. They are now everywhere in "
                       "precision instruments, MEMS, and aerospace "
                       "deployables. The fatigue problem is special: "
                       "flexures operate at high strain, often with mean "
                       "strain from preload, in materials from spring steel "
                       "to polymers to silicon - and the S-N data designers "
                       "have comes from polished rotating-beam specimens "
                       "at low strain, a different universe. Stress "
                       "concentrations at the flexure roots, surface finish "
                       "from etching or printing, and mean-strain effects "
                       "combine in ways no standard covers."),
        "why_it_matters": ("Compliant mechanisms enable precision stages, "
                           "medical devices, and deployable space "
                           "structures with no friction or wear. Reliable "
                           "fatigue life would let them replace bearings "
                           "and joints in long-life applications."),
        "citations": [
            "Howell, L. L. Compliant Mechanisms. Wiley; 2001.",
            "Howell, L. L., Magleby, S. P. and Olsen, B. M. (eds.) Handbook "
            "of Compliant Mechanisms. Wiley; 2013.",
            "Midha, A. et al. Pseudo-Rigid-Body Model for Compliant "
            "Mechanisms. ASME J. Mechanical Design; 1994-2001 series.",
        ],
        "sig_pointer": ("The Signature approach builds flexure-specific "
                        "fatigue curves from small-coupon tests at real "
                        "strains and finishes, then maps them onto the "
                        "flexure stress field for a per-hinge life "
                        "prediction."),
        "sig": {
            "assumptions": ("Flexure fatigue is controlled by local strain "
                            "at the root, surface finish, and mean strain - "
                            "all measurable. Small-coupon data at real "
                            "strains transfers to real flexures."),
            "reasoning": ("Standard S-N data fails because it describes "
                          "the wrong specimen. Test the right specimen: "
                          "small coupons at flexure-representative strain, "
                          "finish, and mean strain, then map the resulting "
                          "curves onto the computed strain field of the "
                          "actual hinge."),
            "mechanism": ("A flexure fatigue pipeline: parameterized "
                          "coupon tests build strain-life curves per "
                          "material-finish-mean-strain combination; the "
                          "pseudo-rigid-body plus FEA strain field of the "
                          "mechanism is evaluated against those curves "
                          "per hinge. The weakest hinge sets the "
                          "mechanism life, and the model flags which "
                          "hinge to redesign."),
            "confirm": ("Predicted weakest-hinge rankings match observed "
                        "failure locations on test mechanisms, with life "
                        "within a factor of three."),
            "kill": ("If size effects dominate - real flexures fail "
                     "differently than coupons at any practical coupon "
                     "scale - the transfer assumption breaks and the "
                     "pipeline is unreliable."),
            "notclaim": ("This does not claim to cover polymers with "
                         "strong rate dependence or silicon with "
                         "statistical fracture; those need their own "
                         "campaigns. We do not know the coupon matrix is "
                         "affordable - it may be too large to build."),
        },
        "demo_spec": {
            "approach": ("Basquin-style life estimate for a flexure at "
                         "high cyclic strain."),
            "assume": [("strain_pct", 2.5, "pct"),
                       ("E_GPa", 3.2, "GPa"),
                       ("sigma_f_MPa", 900.0, "MPa"),
                       ("b_exp", -0.09, "-")],
            "derived": [
                ("stress_MPa", "strain_pct / 100.0 * E_GPa * 1000.0"),
                ("life_cycles", "(stress_MPa / sigma_f_MPa) ** (1.0 / b_exp)"),
            ],
            "confirm": ("Predicted weakest-hinge rankings match observed "
                        "failures; life within a factor of three."),
            "refute": ("Size effects dominate; coupon data does not "
                       "transfer to real flexures."),
        },
    },
    {
        "key": "random-fatigue",
        "name": "Fatigue Life Under Random Loading",
        "group": "Friction and Wear",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("How to predict fatigue life under real random loads - "
                    "the gusty, bumpy, vibrating service histories actual "
                    "structures see. Miner 1945 linear damage rule is "
                    "still the industry standard despite being known "
                    "wrong: load sequence effects can change life by "
                    "factors, and nobody has a generally accepted "
                    "replacement."),
        "background": ("Wohler S-N curves (1860s) and Miner linear "
                       "accumulation (1945) built modern fatigue design; "
                       "Paris 1963 gave crack growth its law. But service "
                       "loads are random, and sequence matters: an "
                       "overload can retard a crack (plastic wake) or "
                       "accelerate damage, and Miner rule ignores both. "
                       "Rainflow counting (Endo 1974) extracts cycles from "
                       "random histories, yet the damage sum still "
                       "misses interactions. Spectral methods (Dirlik "
                       "1985) speed random-fatigue analysis for "
                       "narrow-band loads but inherit Miner linearity. "
                       "After eighty years, cumulative damage under "
                       "truly random loading has no validated general "
                       "theory."),
        "why_it_matters": ("Aircraft, wind turbines, vehicles, and "
                           "offshore structures all live under random "
                           "loads. A trustworthy accumulation rule would "
                           "cut both unexpected failures and the "
                           "over-design that guards against them."),
        "citations": [
            "Miner, M. A. Cumulative Damage in Fatigue. J. Applied Mechanics, "
            "vol. 12; 1945.",
            "Paris, P. C. and Erdogan, F. A Critical Analysis of Crack "
            "Propagation Laws. J. Basic Engineering, vol. 85; 1963.",
            "Dirlik, T. Application of Computers in Fatigue Analysis. PhD "
            "thesis, University of Warwick; 1985.",
        ],
        "sig_pointer": ("The Signature approach replaces the linear sum "
                        "with a stateful damage integrator that remembers "
                        "recent overloads, calibrated on random-load test "
                        "histories rather than constant-amplitude data."),
        "sig": {
            "assumptions": ("Sequence effects are carried by a small "
                            "state - crack-tip plastic zone size, residual "
                            "stress - that evolves with the load history. "
                            "Random-load test data can calibrate the "
                            "state evolution."),
            "reasoning": ("Miner rule fails because it has no memory; "
                          "real damage remembers overloads. Give the "
                          "accumulator a memory: a state variable updated "
                          "by each load excursion, modulating the damage "
                          "rate of subsequent cycles. Calibrate the memory "
                          "on random histories, not constant-amplitude "
                          "tests."),
            "mechanism": ("A stateful damage integrator: each rainflow-"
                          "counted cycle updates a crack-tip state "
                          "(plastic zone, closure level); the damage "
                          "increment of the next cycle depends on the "
                          "state. The state-evolution law is fitted to a "
                          "library of random-load coupon tests spanning "
                          "narrow-band to broad-band spectra."),
            "confirm": ("Life predictions within a factor of two on blind "
                        "random-load histories across three spectra, "
                        "where Miner rule scatters by a factor of five."),
            "kill": ("If the state cannot be identified from measurable "
                     "quantities - the memory lives in unmeasurable "
                     "microstructure - the integrator is curve-fitting "
                     "and will not transfer."),
            "notclaim": ("This does not claim to retire S-N data or "
                         "fracture mechanics; it claims a better "
                         "accumulator. We do not know the state law is "
                         "material-general - each alloy family may need "
                         "its own."),
        },
        "demo_spec": {
            "approach": ("Basquin life from RMS stress and a sequence-"
                         "effect knockdown on Miner sum."),
            "assume": [("rms_MPa", 180.0, "MPa"),
                       ("sigma_f_MPa", 1200.0, "MPa"),
                       ("b_exp", -0.09, "-"),
                       ("sequence_factor", 0.6, "-")],
            "derived": [
                ("life_const_amp", "(rms_MPa / sigma_f_MPa) ** (1.0 / b_exp)"),
                ("life_random", "life_const_amp * sequence_factor"),
                ("miner_sum_at_fail", "1.0 / sequence_factor"),
            ],
            "confirm": ("Blind random-load predictions within a factor of "
                        "two where Miner scatters by five."),
            "refute": ("The damage state is unmeasurable; the integrator "
                       "is curve-fitting that will not transfer."),
        },
    },
    {
        "key": "creep-fatigue",
        "name": "Creep-Fatigue Interaction at High Temperature",
        "group": "Friction and Wear",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("How to predict life when creep and fatigue attack "
                    "together at high temperature. Turbine blades, "
                    "boiler tubes, and nuclear components see cyclic "
                    "loads at temperatures where time-dependent creep "
                    "damage grows during every hold period - and the "
                    "interaction is worse than either alone, in ways no "
                    "standard predicts reliably."),
        "background": ("Creep (Norton law) and fatigue (S-N, Paris) each "
                       "have mature theories, but their interaction does "
                       "not: creep cavitation at grain boundaries "
                       "accelerates fatigue crack growth, and cyclic "
                       "plasticity accelerates creep. The ASME Boiler and "
                       "Pressure Vessel Code and similar standards handle "
                       "it with linear damage summation - the time-"
                       "fraction rule plus Miner rule - which is known to "
                       "be non-conservative in some regimes and wildly "
                       "conservative in others. Hold-time tests show life "
                       "dropping far faster than either rule predicts, "
                       "yet power plants and jet engines are lifed on "
                       "these rules today."),
        "why_it_matters": ("High-temperature components are the most "
                           "expensive parts of power and propulsion "
                           "systems. Honest creep-fatigue life would "
                           "extend service intervals safely and stop "
                           "scrapping good hardware early."),
        "citations": [
            "Holdsworth, S. R. Creep-Fatigue Interaction. Comprehensive "
            "Structural Integrity, vol. 5; 2003.",
            "ASME Boiler and Pressure Vessel Code, Section III, Division 5 "
            "(high temperature reactors).",
            "Pineau, A. and Antolovich, S. D. High Temperature Fatigue of "
            "Engineering Materials. ECF; 2009.",
        ],
        "sig_pointer": ("The Signature approach models the interaction "
                        "through a shared grain-boundary damage state fed "
                        "by both creep cavitation and fatigue cycling, "
                        "replacing the linear sum with coupled damage "
                        "evolution."),
        "sig": {
            "assumptions": ("Both mechanisms feed one grain-boundary "
                            "cavitation state; their coupling is through "
                            "that state, not a fudge factor. Hold-time "
                            "test data can calibrate the coupling."),
            "reasoning": ("Linear summation fails because the damages "
                          "interact physically at grain boundaries - "
                          "cavities nucleated by creep grow under fatigue "
                          "and vice versa. Model the shared state "
                          "directly: one cavitation variable, two "
                          "driving terms, and the interaction emerges "
                          "instead of being assumed."),
            "mechanism": ("A coupled damage model: grain-boundary "
                          "cavitation evolves by a creep-nucleation term "
                          "during holds and a fatigue-growth term during "
                          "cycling, each calibrated from pure-creep and "
                          "pure-fatigue tests, with one coupling "
                          "parameter fitted to hold-time tests. Life is "
                          "the cycles to a critical cavitation level."),
            "confirm": ("Blind hold-time life predictions within a factor "
                        "of two across temperatures and hold durations, "
                        "where linear summation errs by five or more."),
            "kill": ("If microstructural evolution (precipitate "
                     "coarsening, oxidation) dominates the interaction, "
                     "the single-state model misses the real coupling "
                     "and fails."),
            "notclaim": ("This does not claim to cover environmental "
                         "attack or thermal-mechanical phasing effects "
                         "fully; those add states. We do not know one "
                         "coupling parameter suffices across alloys - "
                         "that needs a multi-alloy campaign."),
        },
        "demo_spec": {
            "approach": ("Larson-Miller parameter and linear vs coupled "
                         "damage comparison for a hold cycle."),
            "assume": [("temp_C", 600.0, "C"),
                       ("hold_h", 2.0, "h"),
                       ("cycles", 5000.0, "-"),
                       ("creep_frac", 0.4, "-"),
                       ("fatigue_frac", 0.5, "-")],
            "derived": [
                ("T_K", "temp_C + 273.15"),
                ("LM_param", "T_K * (20.0 + math.log10(hold_h))"),
                ("linear_sum", "creep_frac + fatigue_frac"),
                ("coupled_sum", "creep_frac + fatigue_frac + 0.8 * creep_frac * fatigue_frac"),
            ],
            "confirm": ("Blind hold-time predictions within a factor of "
                        "two where linear summation errs by five."),
            "refute": ("Microstructural evolution dominates; the "
                       "single-state model misses the coupling."),
        },
    },
    {
        "key": "superlubricity",
        "name": "Superlubricity Beyond the Laboratory",
        "group": "Friction and Wear",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("How to get superlubricity - friction coefficients "
                    "near zero - out of the lab and into real machines. "
                    "Structural superlubricity in graphite and "
                    "diamond-like carbon shows friction can nearly "
                    "vanish, but only at micro-contacts, in vacuum or "
                    "dry nitrogen, for short times. Scaling it to "
                    "engineering contacts in air has failed for decades."),
        "background": ("Hirano and Shinjo predicted superlubricity in "
                       "1990 for incommensurate crystal lattices; "
                       "Dienwiebel et al. 2004 measured it in graphite "
                       "flakes with friction coefficients around 0.001. "
                       "The mechanism is understood: mismatched lattices "
                       "cancel lateral forces. The scaling wall is "
                       "brutal - real contacts have many asperities that "
                       "lock into registry, humidity and contaminants "
                       "destroy the effect, and wear debris changes the "
                       "interface. Macroscale demonstrations exist "
                       "(DLC films, graphene coatings) but are "
                       "temperamental; no superlubric contact survives "
                       "years of dirty service."),
        "why_it_matters": ("Near-zero friction would slash energy losses "
                           "in machinery and enable wear-free sliding "
                           "components. The lab effect is real; the "
                           "engineering version would be revolutionary."),
        "citations": [
            "Hirano, M. and Shinjo, K. Atomistic Locking and Friction. "
            "Physical Review B, vol. 41; 1990.",
            "Dienwiebel, M. et al. Superlubricity of Graphite. Physical "
            "Review Letters, vol. 92; 2004.",
            "Erdemir, A. and Martin, J.-M. (eds.) Superlubricity. Elsevier; "
            "2007.",
        ],
        "sig_pointer": ("The Signature approach engineers the interface "
                        "as a system - incommensurate coating plus a "
                        "debris-ejecting texture plus humidity shielding "
                        "- attacking all three scaling killers at once "
                        "instead of chasing the perfect lattice."),
        "sig": {
            "assumptions": ("The three scaling killers are multi-asperity "
                            "locking, contamination, and debris "
                            "accumulation. Each is addressable by design; "
                            "their combination is what has never been "
                            "tried as a system."),
            "reasoning": ("Decades of work optimized the lattice and "
                          "ignored the system around it. Real contacts "
                          "fail on contamination and debris, not "
                          "crystallography - so design the contact as a "
                          "system: coating for incommensurability, "
                          "texture to eject debris, sealing geometry to "
                          "exclude humidity."),
            "mechanism": ("A system contact: graphene or DLC-based "
                          "incommensurate coating on a micro-textured "
                          "surface whose texture channels debris out of "
                          "the contact, with labyrinth edge geometry "
                          "limiting humidity ingress. The three "
                          "subsystems are tested separately then as a "
                          "stack, with friction logged over long "
                          "durations in ambient air."),
            "confirm": ("Sustained friction below 0.01 for 10 million "
                        "cycles in ambient air on a centimeter-scale "
                        "contact."),
            "kill": ("If debris generation is intrinsic and "
                     "un-ejectable at the needed rates, or humidity "
                     "ingress cannot be sealed without killing the "
                     "effect, the system approach fails like the "
                     "lattice-only approach."),
            "notclaim": ("This does not claim a universal coating; "
                         "different load regimes may need different "
                         "stacks. We do not know the texture survives "
                         "its own wear - long tests are the only way to "
                         "know."),
        },
        "demo_spec": {
            "approach": ("Friction force and energy saved scaling from "
                         "lab superlubricity to a machine contact."),
            "assume": [("mu_lab", 0.001, "-"),
                       ("mu_target", 0.005, "-"),
                       ("mu_conv", 0.1, "-"),
                       ("load_N", 1000.0, "N"),
                       ("slide_m", 1e6, "m")],
            "derived": [
                ("F_target_N", "mu_target * load_N"),
                ("E_conv_MJ", "mu_conv * load_N * slide_m / 1e6"),
                ("E_target_MJ", "mu_target * load_N * slide_m / 1e6"),
                ("saved_MJ", "E_conv_MJ - E_target_MJ"),
                ("improvement_x", "mu_conv / mu_target"),
            ],
            "confirm": ("Friction below 0.01 for 10 million cycles in "
                        "ambient air at centimeter scale."),
            "refute": ("Debris proves un-ejectable or humidity unsealable "
                       "without killing the effect."),
        },
    },
    {
        "key": "active-turbulence",
        "name": "Real-Time Active Turbulence Control",
        "group": "Turbulence and Fluids",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("How to control turbulence in real time on a real "
                    "vehicle or pipeline. Lab demonstrations cut drag "
                    "with blowing, suction, and plasma actuators, but "
                    "they need dense sensors, fast computation, and "
                    "actuation energy that wipes out the gains - and "
                    "none has survived the jump to full scale."),
        "background": ("Active flow control grew from the 1990s "
                       "understanding of coherent structures: if you can "
                       "sense and cancel the near-wall streaks and "
                       "vortices, drag falls. Opposition control "
                       "(Choi et al. 1994) showed 25 percent drag "
                       "reduction in DNS with ideal sensing. Plasma "
                       "actuators (Corke et al. 2000s) promised no "
                       "moving parts. Yet every real attempt hits the "
                       "same wall: the sensing-actuation-computation "
                       "loop must run at kilohertz over square meters, "
                       "sensors foul, actuators are fragile, and the "
                       "net energy - saved minus spent - goes negative "
                       "outside the lab."),
        "why_it_matters": ("Real-time turbulence control is the path to "
                           "the 30-percent drag cuts passive methods "
                           "cannot reach. Cracking the loop economics "
                           "would transform aviation fuel burn and "
                           "pipeline pumping costs."),
        "citations": [
            "Choi, H., Moin, P. and Kim, J. Active Turbulence Control for "
            "Drag Reduction in Wall-Bounded Flows. J. Fluid Mechanics, vol. "
            "262; 1994.",
            "Gad-el-Hak, M. Flow Control: Passive, Active, and Reactive Flow "
            "Management. Cambridge University Press; 2000.",
            "Corke, T. C., Enloe, C. L. and Wilkinson, S. P. Dielectric "
            "Barrier Discharge Plasma Actuators. Annual Review of Fluid "
            "Mechanics, vol. 42; 2010.",
        ],
        "sig_pointer": ("The Signature approach closes the loop "
                        "statistically rather than deterministically - "
                        "actuating on burst statistics instead of "
                        "instantaneous fields - cutting the sensor and "
                        "compute burden by orders of magnitude."),
        "sig": {
            "assumptions": ("Drag is produced by intermittent burst "
                            "events; suppressing bursts suppresses drag. "
                            "Burst statistics are predictable from sparse "
                            "sensors; the full velocity field is not "
                            "needed."),
            "reasoning": ("Deterministic control demands the impossible: "
                          "full-field sensing at kilohertz. But drag "
                          "comes from bursts, and bursts are statistical "
                          "events with precursors. Control the "
                          "statistics - fire actuators when burst "
                          "probability spikes - and the loop needs a "
                          "handful of sensors, not a million."),
            "mechanism": ("A statistical controller: sparse wall sensors "
                          "feed a burst-probability estimator trained on "
                          "DNS and lab data; actuators fire short pulses "
                          "only when probability crosses threshold. The "
                          "controller optimizes net energy (drag saved "
                          "minus actuation spent) directly, and adapts "
                          "the threshold as fouling changes the sensor "
                          "response."),
            "confirm": ("Sustained net-positive drag reduction above 15 "
                        "percent on a meter-scale test article in a "
                        "realistic flow, sensors included in the energy "
                        "budget."),
            "kill": ("If burst precursors are not detectable with sparse "
                     "sensors in noisy real flows, the statistical loop "
                     "has nothing to trigger on and the approach fails."),
            "notclaim": ("This does not claim deterministic turbulence "
                         "cancellation; it claims statistical suppression. "
                         "We do not know the estimator transfers from "
                         "lab to flight Reynolds numbers - that is the "
                         "scaling experiment."),
        },
        "demo_spec": {
            "approach": ("Size the sensor-actuator loop: data rate, "
                         "latency budget, and net-energy check."),
            "assume": [("sensors", 200.0, "-"),
                       ("sample_hz", 2000.0, "Hz"),
                       ("latency_ms", 2.0, "ms"),
                       ("drag_save_pct", 15.0, "pct"),
                       ("act_power_W", 800.0, "W"),
                       ("flow_power_kW", 40.0, "kW")],
            "derived": [
                ("data_MBps", "sensors * sample_hz * 4.0 / 1e6"),
                ("saved_kW", "flow_power_kW * drag_save_pct / 100.0"),
                ("net_kW", "saved_kW - act_power_W / 1000.0"),
                ("net_positive", "1.0 if net_kW > 0.0 else 0.0"),
            ],
            "confirm": ("Net-positive 15 percent drag cut on a "
                        "meter-scale article in realistic flow."),
            "refute": ("Burst precursors undetectable with sparse sensors "
                       "in noisy real flows."),
        },
    },
    {
        "key": "scramjet",
        "name": "Sustained Scramjet Combustion",
        "group": "Turbulence and Fluids",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("How to keep a scramjet burning steadily across its "
                    "flight envelope. Supersonic combustion - fuel burning "
                    "in air moving faster than sound - works in "
                    "demonstrators (X-43A hit Mach 9.6 in 2004, X-51A "
                    "flew in 2010) but flameholding, thermal loads, and "
                    "the narrow operable range keep it experimental after "
                    "sixty years."),
        "background": ("The scramjet concept dates to the 1950s-60s "
                       "(Weber and MacKay); the physics is brutal: air "
                       "crosses the combustor in about a millisecond, so "
                       "fuel must mix and burn in that time at "
                       "temperatures and pressures that melt most "
                       "materials. Cavity flameholders, pioneered in the "
                       "1990s-2000s, anchor the flame in recirculation "
                       "zones. The X-43A 2004 flights proved the concept "
                       "at Mach 7 and 9.6; the X-51A Waverider sustained "
                       "combustion for over three minutes in 2010-2013. "
                       "Yet operability - starting, throttling, "
                       "transitioning across Mach numbers without "
                       "unstart (the inlet disgorging its shock system) "
                       "- remains unsolved, and no operational scramjet "
                       "vehicle exists."),
        "why_it_matters": ("Scramjets are the only air-breathing path to "
                           "sustained hypersonic flight, promising "
                           "two-hour intercontinental travel and cheap "
                           "responsive space access. Operability is the "
                           "wall between demonstrators and vehicles."),
        "citations": [
            "Heiser, W. H. and Pratt, D. T. Hypersonic Airbreathing "
            "Propulsion. AIAA Education Series; 1994.",
            "Curran, E. T. Scramjet Engines: The First Forty Years. J. "
            "Propulsion and Power, vol. 17; 2001.",
            "Urzay, J. Supersonic Combustion in Air-Breathing Propulsion "
            "Systems. Annual Review of Fluid Mechanics, vol. 50; 2018.",
        ],
        "sig_pointer": ("The Signature approach treats the combustor as a "
                        "dynamical system to be steered, using fast fuel "
                        "staging and variable geometry driven by a "
                        "real-time operability map, instead of a fixed "
                        "geometry hoping the flow cooperates."),
        "sig": {
            "assumptions": ("Unstart and blowout are preceded by "
                            "detectable precursors in wall pressure "
                            "signatures. Millisecond fuel staging and "
                            "modest geometry variation can steer the "
                            "combustor away from the boundary."),
            "reasoning": ("Fixed-geometry combustors fail because the "
                          "operable window moves with flight condition "
                          "faster than the design can follow. Make the "
                          "combustor steerable: map the operability "
                          "boundary in real time from pressure "
                          "signatures, and continuously stage fuel and "
                          "geometry to stay inside it."),
            "mechanism": ("An operability autopilot: wall-pressure sensor "
                          "arrays feed a precursor detector trained on "
                          "ground-test unstart/blowout data; the "
                          "controller modulates fuel staging and inlet "
                          "geometry to hold margin to the boundary. The "
                          "map updates in flight as the engine learns "
                          "its own characteristics."),
            "confirm": ("Sustained combustion across a Mach 4-to-7 "
                        "acceleration in ground test with no unstart, "
                        "controlled by the autopilot."),
            "kill": ("If precursors are not reliably detectable ahead of "
                     "unstart at flight scale - the event is too abrupt "
                     "- the autopilot cannot act in time and the "
                     "approach fails."),
            "notclaim": ("This does not claim to solve materials or "
                         "cooling; those remain hard walls. We do not "
                         "know ground-test precursors transfer to flight "
                         "- flight data is the missing piece."),
        },
        "demo_spec": {
            "approach": ("Residence-time vs chemical-time check "
                         "(Damkohler) for supersonic combustion."),
            "assume": [("combustor_m", 1.5, "m"),
                       ("vel_ms", 1500.0, "m/s"),
                       ("chem_ms", 0.3, "ms"),
                       ("fuel_air", 0.03, "-")],
            "derived": [
                ("res_ms", "combustor_m / vel_ms * 1000.0"),
                ("damkohler", "res_ms / chem_ms"),
                ("burn_ok", "1.0 if damkohler > 3.0 else 0.0"),
                ("thrust_kN", "fuel_air * 50.0 * 9.81 / 1000.0 * 1000.0"),
            ],
            "confirm": ("Autopilot sustains combustion Mach 4-to-7 in "
                        "ground test with no unstart."),
            "refute": ("Unstart precursors not detectable in time at "
                       "flight scale."),
        },
    },
]
ENTRIES += [
    {
        "key": "hypersonic-transition",
        "name": "Hypersonic Boundary-Layer Transition",
        "group": "Turbulence and Fluids",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("How to predict where the boundary layer trips to "
                    "turbulence on a hypersonic vehicle. Transition "
                    "multiplies surface heating several-fold - it sizes "
                    "the heat shield - yet hypersonic transition "
                    "prediction is far behind its subsonic cousin, with "
                    "second-mode instabilities, roughness, ablation, "
                    "and real-gas effects interacting unpredictably."),
        "background": ("Mack 1969-1984 stability theory identified the "
                       "acoustic second mode as the dominant hypersonic "
                       "instability, confirmed in quiet tunnels. But "
                       "flight is not a quiet tunnel: the HIFiRE and "
                       "BOLT flight experiments showed transition "
                       "behaving differently than ground tests predict, "
                       "with roughness, blowing from ablating heat "
                       "shields, and angle of attack all shifting it. "
                       "Vehicle designers bracket the uncertainty with "
                       "huge heating margins - heat shields sized for "
                       "transition far forward of where it may actually "
                       "occur - because under-predicting means losing "
                       "the vehicle. The gap between quiet-tunnel "
                       "physics and flight reality is the unsolved "
                       "problem."),
        "why_it_matters": ("Transition location sizes every hypersonic "
                           "heat shield and sets the feasibility of "
                           "reusable hypersonic vehicles. Cutting the "
                           "uncertainty would remove tons of shield mass "
                           "and unlock reliable hypersonic flight."),
        "citations": [
            "Mack, L. M. Boundary-Layer Linear Stability Theory. AGARD "
            "Report 709; 1984.",
            "Schneider, S. P. Hypersonic Laminar-Turbulent Transition on "
            "Circular Cones and Scramjet Forebodies. Progress in Aerospace "
            "Sciences, vol. 40; 2004.",
            "Wheaton, B. M. et al. BOLT Flight Experiment Overview. AIAA "
            "SciTech; 2021.",
        ],
        "sig_pointer": ("The Signature approach fuses quiet-tunnel "
                        "second-mode physics with flight-data "
                        "corrections for roughness, blowing, and "
                        "real-gas effects, producing a flight-anchored "
                        "transition forecast instead of a tunnel "
                        "extrapolation."),
        "sig": {
            "assumptions": ("Second-mode growth is the core mechanism on "
                            "smooth cold walls; flight effects - "
                            "roughness, blowing, chemistry - act as "
                            "modifiers on that core, calibratable from "
                            "flight experiments."),
            "reasoning": ("Tunnel-to-flight extrapolation fails because "
                          "each flight effect is treated as a separate "
                          "mystery. Treat them as modifiers on one core "
                          "mechanism: compute second-mode growth, then "
                          "apply roughness, blowing, and real-gas "
                          "corrections calibrated against the growing "
                          "flight database."),
            "mechanism": ("A flight-anchored transition solver: linear "
                          "and nonlinear stability for the second mode "
                          "on the vehicle geometry, corrected by "
                          "roughness-spectrum, blowing-rate, and "
                          "chemistry modifiers fitted to HIFiRE/BOLT-class "
                          "flight data. Output is a transition front "
                          "with uncertainty bands that shrink as flight "
                          "data accumulates."),
            "confirm": ("Predicted transition fronts bracket flight-"
                        "measured fronts on two new flight experiments "
                        "without retuning."),
            "kill": ("If flight transition proves dominated by "
                     "mechanisms outside the second-mode-plus-modifiers "
                     "picture - crossflow, transient growth from "
                     "unmodeled sources - the anchored solver misses "
                     "systematically."),
            "notclaim": ("This does not claim to retire heating margins "
                         "entirely; uncertainty bands remain honest. We "
                         "do not know the modifier set is complete - "
                         "each new flight may reveal a new one."),
        },
        "demo_spec": {
            "approach": ("Transition Reynolds estimate and heating "
                         "multiplier for a hypersonic forebody."),
            "assume": [("mach", 7.0, "-"),
                       ("Re_per_m", 1e7, "1/m"),
                       ("x_m", 2.0, "m"),
                       ("Re_tr_base", 5e6, "-")],
            "derived": [
                ("Re_x", "Re_per_m * x_m"),
                ("second_mode_boost", "1.0 + 0.15 * (mach - 5.0)"),
                ("Re_tr_eff", "Re_tr_base / second_mode_boost"),
                ("turb_flag", "1.0 if Re_x > Re_tr_eff else 0.0"),
                ("heat_mult", "4.0 if Re_x > Re_tr_eff else 1.0"),
            ],
            "confirm": ("Predicted fronts bracket flight measurements on "
                        "new experiments without retuning."),
            "refute": ("Flight transition dominated by mechanisms "
                       "outside the second-mode-plus-modifiers picture."),
        },
    },
    {
        "key": "navier-stokes",
        "name": "The Navier-Stokes Regularity Question",
        "group": "Turbulence and Fluids",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Do the Navier-Stokes equations - the foundation of "
                    "all fluid mechanics - always have smooth solutions, "
                    "or can they blow up? This is one of the seven "
                    "Clay Millennium Prize Problems, worth one million "
                    "dollars, and it asks whether the mathematics "
                    "describing every fluid flow is even self-consistent."),
        "background": ("Navier and Stokes wrote the equations in the "
                       "1820s-40s; Leray 1934 proved weak solutions "
                       "exist globally but may be non-unique or "
                       "singular. The Millennium formulation (Fefferman "
                       "2000) asks: in three dimensions, do smooth, "
                       "finite-energy initial conditions always evolve "
                       "smoothly forever? Partial results abound - "
                       "regularity under small data, conditional "
                       "regularity criteria (Beale-Kato-Majda 1984), "
                       "near-miss blowup scenarios in simplified models "
                       "(Tao 2016 averaged model blows up, but the real "
                       "equations resist). Engineers use the equations "
                       "daily without knowing whether their solutions "
                       "are mathematically guaranteed to exist."),
        "why_it_matters": ("Beyond the prize, regularity underpins trust "
                           "in every CFD simulation ever run. A blowup "
                           "proof would reveal deep structure in "
                           "turbulence; a regularity proof would certify "
                           "the mathematics of fluid mechanics."),
        "citations": [
            "Fefferman, C. L. Existence and Smoothness of the Navier-Stokes "
            "Equation. Clay Mathematics Institute Millennium description; 2000.",
            "Leray, J. Sur le mouvement d un liquide visqueux emplissant "
            "l espace. Acta Mathematica, vol. 63; 1934.",
            "Beale, J. T., Kato, T. and Majda, A. Remarks on the Breakdown "
            "of Smooth Solutions for the 3-D Euler Equations. Communications "
            "in Mathematical Physics, vol. 94; 1984.",
        ],
        "sig_pointer": ("The Signature approach does not claim the "
                        "prize; it proposes a computational search "
                        "strategy - hunting candidate near-singular "
                        "structures in extreme DNS and testing them "
                        "against the known conditional-regularity "
                        "criteria - to map where blowup would have to "
                        "hide."),
        "sig": {
            "assumptions": ("If finite-time blowup exists, its precursors "
                            "leave signatures - extreme vorticity "
                            "amplification with specific scaling - "
                            "visible in sufficiently extreme DNS before "
                            "resolution fails."),
            "reasoning": ("The prize resists analysis, but computation "
                          "can narrow the hunt: run DNS at the edge of "
                          "feasibility, extract the most extreme events, "
                          "and test each against Beale-Kato-Majda-type "
                          "criteria. Either a candidate emerges that "
                          "analysts can attack, or the extreme events "
                          "keep obeying the criteria - both are "
                          "progress."),
            "mechanism": ("A blowup-hunting pipeline: extreme-Reynolds "
                          "DNS with adaptive resolution focused on "
                          "peak-vorticity regions; automated extraction "
                          "of candidate singular structures; evaluation "
                          "against conditional-regularity criteria; the "
                          "strongest candidates published as targets for "
                          "analytical attack. Negative results - events "
                          "obeying the criteria - are published too, as "
                          "evidence constraining where blowup can hide."),
            "confirm": ("A reproducible candidate structure whose "
                        "scaling violates a conditional-regularity "
                        "criterion under mesh refinement - a concrete "
                        "target for the analysts."),
            "kill": ("If extreme events always resolve into "
                     "criteria-obeying structures no matter the "
                     "Reynolds number, the hunt yields only negative "
                     "results and the computational path stalls."),
            "notclaim": ("This does not claim progress toward the "
                         "Millennium Prize itself; it claims a better "
                         "map of the battlefield. We do not know the "
                         "resolution is enough - the true event may "
                         "hide below any feasible grid, and we say so "
                         "plainly."),
        },
        "demo_spec": {
            "approach": ("Kolmogorov scale and DNS resolution requirement "
                         "at extreme Reynolds number."),
            "assume": [("Re", 1e6, "-"),
                       ("L_m", 1.0, "m"),
                       ("U_ms", 1.0, "m/s"),
                       ("nu", 1e-6, "m2/s")],
            "derived": [
                ("epsilon", "U_ms ** 3 / L_m"),
                ("eta_m", "(nu ** 3 / epsilon) ** 0.25"),
                ("eta_over_L", "eta_m / L_m"),
                ("points_1d", "L_m / eta_m"),
                ("points_3d", "(L_m / eta_m) ** 3"),
            ],
            "confirm": ("A reproducible candidate singular structure "
                        "surviving mesh refinement - a target for "
                        "analysts."),
            "refute": ("Extreme events always resolve into "
                       "criteria-obeying structures; the hunt stalls."),
        },
    },
    {
        "key": "chaotic-mixing",
        "name": "Closed-Loop Control of Chaotic Mixing",
        "group": "Turbulence and Fluids",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("How to control chaotic advection - the stretching "
                    "and folding that mixes fluids - in real time. "
                    "Chaotic mixing blends without turbulence, promising "
                    "fast gentle mixing for chemicals and pharma, but "
                    "designing and controlling the chaotic flow field "
                    "outside simple geometries is unsolved."),
        "background": ("Aref 1984 showed that even simple time-periodic "
                       "flows produce chaotic particle paths - chaotic "
                       "advection - giving exponential stretching without "
                       "turbulence. Static mixers (Kenics 1960s) exploit "
                       "it passively. The control frontier is active: "
                       "modulating boundary motions or body forces to "
                       "maximize mixing rate, avoid dead zones, and adapt "
                       "to changing fluids. The mathematics - Lyapunov "
                       "exponents, Lagrangian coherent structures (Haller "
                       "2000s) - describes mixing well but inverts poorly: "
                       "given a target mixedness, the required actuation "
                       "is not computable for real vessels."),
        "why_it_matters": ("Fast gentle mixing matters for "
                           "pharmaceuticals, specialty chemicals, and food "
                           "- anywhere turbulence would damage the "
                           "product. Controlled chaotic mixing would cut "
                           "batch times and improve uniformity."),
        "citations": [
            "Aref, H. Stirring by Chaotic Advection. J. Fluid Mechanics, "
            "vol. 143; 1984.",
            "Ottino, J. M. The Kinematics of Mixing: Stretching, Chaos, and "
            "Transport. Cambridge University Press; 1989.",
            "Haller, G. Lagrangian Coherent Structures. Annual Review of "
            "Fluid Mechanics, vol. 47; 2015.",
        ],
        "sig_pointer": ("The Signature approach steers mixing by tracking "
                        "Lagrangian coherent structures in real time from "
                        "sparse sensors and actuating to stretch the "
                        "worst-mixed regions, closing the loop on "
                        "mixedness itself."),
        "sig": {
            "assumptions": ("Lagrangian coherent structures organize "
                            "mixing and are estimable from sparse "
                            "velocity sensing. Stretching the least-mixed "
                            "regions is the optimal control action."),
            "reasoning": ("Open-loop chaotic mixers work but cannot "
                          "adapt; the missing piece is feedback on "
                          "mixedness. Coherent structures reveal which "
                          "fluid parcels resist mixing - aim actuation "
                          "at those parcels and the controller chases "
                          "uniformity directly."),
            "mechanism": ("A mixedness-feedback controller: sparse "
                          "sensors reconstruct the velocity field; "
                          "finite-time Lyapunov exponents map the "
                          "poorly-stretched regions; actuators (modulated "
                          "impellers, pulsed jets) target those regions. "
                          "A concentration proxy from inline sensors "
                          "closes the outer loop on actual mixedness."),
            "confirm": ("Closed-loop batches reach target uniformity 2x "
                        "faster than the best open-loop protocol on a "
                        "pilot mixer."),
            "kill": ("If coherent structures cannot be estimated fast "
                     "enough from sparse sensors in real vessels - the "
                     "reconstruction lags the flow - the controller "
                     "acts on stale maps and fails."),
            "notclaim": ("This does not claim to beat the fundamental "
                         "stretching limits of the flow; it claims to "
                         "reach them faster. We do not know the sensor "
                         "density needed - that is the pilot experiment."),
        },
        "demo_spec": {
            "approach": ("Stretching from Lyapunov exponent and the "
                         "mixing-time estimate."),
            "assume": [("lyap_1ps", 0.8, "1/s"),
                       ("time_s", 10.0, "s"),
                       ("D_m2ps", 1e-9, "m2/s"),
                       ("L0_mm", 10.0, "mm")],
            "derived": [
                ("stretch", "2.718281828 ** (lyap_1ps * time_s)"),
                ("striae_um", "L0_mm * 1000.0 / stretch"),
                ("diff_time_s", "(striae_um * 1e-6) ** 2 / D_m2ps"),
                ("mixed_flag", "1.0 if diff_time_s < time_s else 0.0"),
            ],
            "confirm": ("Closed-loop batches reach uniformity 2x faster "
                        "than best open-loop on a pilot mixer."),
            "refute": ("Coherent structures not estimable fast enough "
                       "from sparse sensors; controller acts on stale "
                       "maps."),
        },
    },
    {
        "key": "tether",
        "name": "Megastructure Tether Mechanics (Space Elevator Cable)",
        "group": "Manufacturing and Metamaterials",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("How to build a cable strong and light enough for a "
                    "space elevator - the most demanding tensile structure "
                    "ever conceived. The ribbon must support its own "
                    "100,000-kilometer weight plus climbers, survive "
                    "micrometeorites and atomic oxygen, and be "
                    "manufacturable in one continuous piece. No material "
                    "in production qualifies."),
        "background": ("Tsiolkovsky imagined the tower in 1895; Artsutanov "
                       "1960 and Pearson 1975 gave the modern cable "
                       "concept, with Edwards NASA Institute study 2000-"
                       "2003 working out the engineering. The requirement "
                       "is specific strength around 50 GPa at density "
                       "near 1300 kg/m3 - carbon nanotubes in theory "
                       "reach it (measured strengths to 100 GPa on "
                       "defect-free tubes), but macroscopic nanotube "
                       "fibers manage a few GPa at best, and defects "
                       "dominate at length. The taper ratio - how much "
                       "thicker the cable is at geostationary altitude "
                       "than at the ground - explodes as strength falls "
                       "short. Meanwhile the dynamics (climber-induced "
                       "waves, debris strikes, electrodynamic forces) "
                       "are barely modeled."),
        "why_it_matters": ("A working elevator would cut orbital access "
                           "costs by orders of magnitude and open the "
                           "solar system. The cable is the single "
                           "tallest materials pole in the tent - every "
                           "other subsystem is engineering, this one is "
                           "still science."),
        "citations": [
            "Edwards, B. C. The Space Elevator. NASA Institute for Advanced "
            "Concepts Phase I/II reports; 2000-2003.",
            "Pearson, J. The Orbital Tower. Acta Astronautica, vol. 2; 1975.",
            "Pugno, N. M. On the Strength of the Carbon Nanotube-Based Space "
            "Elevator Cable. J. Physics: Condensed Matter, vol. 18; 2006.",
        ],
        "sig_pointer": ("The Signature approach attacks the defect "
                        "scaling directly - hierarchical flaw-tolerant "
                        "cable architecture plus in-space splicing - "
                        "treating the cable as a damage-tolerant "
                        "structure rather than a perfect fiber."),
        "sig": {
            "assumptions": ("Nanotube intrinsic strength is sufficient; "
                            "the gap is defect control at length. A "
                            "hierarchical, flaw-tolerant architecture "
                            "can approach intrinsic strength the way "
                            "biological materials do. In-space splicing "
                            "is feasible."),
            "reasoning": ("Chasing perfect kilometers-long nanotubes "
                          "has stalled for twenty years. Nature never "
                          "makes perfect fibers - it makes hierarchical "
                          "damage-tolerant ones (tendon, spider silk). "
                          "Build the cable the same way: bundles of "
                          "bundles with sacrificial load paths, so "
                          "defects cost strength gracefully instead of "
                          "catastrophically."),
            "mechanism": ("A hierarchical cable: nanotube yarns twisted "
                          "into strands, strands into ropes with "
                          "cross-linking that arrests single-yarn "
                          "failure; health monitoring via embedded "
                          "conductivity sensing locates damage; "
                          "climber-robots splice replacement segments "
                          "in space. The taper ratio is computed for "
                          "the achieved hierarchical strength, not the "
                          "intrinsic tube strength."),
            "confirm": ("Kilometer-scale hierarchical test cables "
                        "demonstrating 20 GPa specific-strength "
                        "retention with graceful (non-catastrophic) "
                        "failure modes."),
            "kill": ("If cross-linking cannot arrest failure - one "
                     "broken yarn unzips the hierarchy - the "
                     "architecture gains nothing over a monofilament "
                     "and the approach fails."),
            "notclaim": ("This does not claim the elevator is buildable "
                         "now; it claims a path that does not require "
                         "perfect nanotubes. We do not know in-space "
                         "splicing works at the needed reliability - "
                         "that is a program in itself, and we say so."),
        },
        "demo_spec": {
            "approach": ("Breaking length and taper ratio for candidate "
                         "tether materials."),
            "assume": [("sigma_GPa", 50.0, "GPa"),
                       ("rho", 1300.0, "kg/m3"),
                       ("L_km", 100000.0, "km"),
                       ("g0", 9.81, "m/s2")],
            "derived": [
                ("break_km", "sigma_GPa * 1e9 / (rho * g0) / 1000.0"),
                ("taper", "2.718281828 ** (rho * g0 * L_km * 1000.0 / (sigma_GPa * 1e9) * 0.5)"),
                ("ok_flag", "1.0 if break_km > 5000.0 else 0.0"),
            ],
            "confirm": ("Kilometer test cables hold 20 GPa with "
                        "graceful failure modes."),
            "refute": ("Cross-linking cannot arrest failure; one broken "
                       "yarn unzips the hierarchy."),
        },
    },
]
