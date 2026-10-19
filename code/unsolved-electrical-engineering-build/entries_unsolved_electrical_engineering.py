#!/usr/bin/env python3
"""Entries for the Unsolved Electrical Engineering databases (Manon 2026-10-17
16:15 orders, Unsolved Problems Solved series).

Verified 2026-10-17: ID prefixes JAH-USEE- (public) and JAH-USEES-
(signature) have ZERO hits in data/manifest.json id_prefix values and zero
hits across every record ID in ~/workspace/jah-databases-data-1/data/.
Slugs unsolved-electrical-engineering / -signature have zero hits in the
manifest. All 34 titles plus 34 " (Signature Edition)" titles pass the
whole-system exact-title dedupe gate at build time.

Two NEW databases, 34 ladder-ordered records each:

  unsolved-electrical-engineering            - The Unsolved Electrical
                                              Engineering Database
                                              (public-harvest: real,
                                              fact-checked famous unsolved
                                              electrical-engineering
                                              problems - wireless power,
                                              grid stability, terahertz,
                                              beyond-silicon computing,
                                              quantum interconnects, and
                                              29 more - civilian only)
  unsolved-electrical-engineering-signature  - The Unsolved Electrical
                                              Engineering Signature
                                              Database
                                              (his original Signature
                                              Engineering Method: full
                                              Signature-generated proposed
                                              solutions, honesty-labeled)

Standing exclusion honored: nothing on neutralizing or defeating military
or defense-grade systems - every problem is civilian. No religious talk.
Nothing hate-adjacent, profane, or inappropriate. No website references.
No Facebook.
"""

SIG_LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Engineering Method "
            "applied to famous unsolved electrical engineering problems: "
            "proposed solution approaches with stated assumptions, a "
            "reasoning path, a proposed mechanism, confirm-or-kill evidence, "
            "and an explicit statement of what each approach does NOT claim. "
            "Labeled Signature-made, never presented as established science "
            "or authentic public record.")

ENTRIES = [
    # ---------------- APPROACHABLE (ladder 1-12) ----------------
    {
        "key": "wireless_power_distance",
        "name": "Efficient Long-Distance Wireless Power Transfer",
        "group": "Wireless & RF",
        "ladder_rank": 1,
        "ladder_tier": "approachable",
        "problem": ("How can useful amounts of electrical power be delivered "
                    "wirelessly across rooms, buildings, or kilometers with "
                    "efficiency high enough to matter, without unsafe field "
                    "strengths or prohibitive cost?"),
        "background": ("Nikola Tesla demonstrated the dream more than a "
                       "century ago at Wardenclyffe: power through the air "
                       "and ground, no wires. The physics never cooperated "
                       "at distance - radiated power falls with the square "
                       "of distance, and beaming it tightly demands large "
                       "apertures and precise tracking. Modern near-field "
                       "systems work well: the MIT group showed resonant "
                       "magnetic coupling lighting a 60-watt bulb across 2 "
                       "meters in 2007, and the Qi standard now charges "
                       "phones across millimeters. But crossing a room at "
                       "high efficiency, or beaming kilowatts across "
                       "kilometers, remains stuck: radiative schemes lose "
                       "most energy to spreading, regulatory exposure "
                       "limits cap field strength, and laser or microwave "
                       "beaming adds conversion losses at both ends. "
                       "Research continues in metamaterial lenses, "
                       "retro-directive beam steering, and resonant "
                       "relay chains, but no far-field system has reached "
                       "the efficiency and cost of a copper wire."),
        "why_it_matters": ("Solving it would erase the last cord: phones, "
                           "sensors, vehicles, and even aircraft charging "
                           "from the ambient environment, plus power "
                           "delivery to disaster zones and remote sites "
                           "without stringing wire. It is also the missing "
                           "enabler for space solar power and long-endurance "
                           "drones. The economic prize is the wiring layer "
                           "of civilization itself."),
        "sig_pointer": ("The Signature approach proposes resonant relay "
                        "lattice corridors - chains of passive tuned "
                        "repeaters that carry evanescent fields across a "
                        "room the way fiber carries light - shifting the "
                        "problem from radiation to guided near-field hops."),
        "signature_solution": ("Step 1 - assumption: the spreading-loss "
            "wall is fundamental for radiation, so stop radiating and "
            "instead guide the near field through space with a lattice of "
            "passive resonant repeaters, each a high-Q tuned coil whose "
            "evanescent tail overlaps the next, so energy hops "
            "repeater-to-repeater across a room with per-hop loss under 2 "
            "percent. Step 2 - reasoning path: coupled-mode theory shows a "
            "chain of N resonators can reach end-to-end efficiency near "
            "(1 - loss)^N if every link is impedance-matched and detuning "
            "is actively trimmed; the repeaters need no power of their own "
            "except tiny tuning electronics, so the corridor can be printed "
            "into walls, floors, or ceiling tiles at commodity cost. Step 3 "
            "- proposed mechanism: a software-defined lattice that "
            "discovers the best path around furniture and people, trims "
            "each repeater with varactor tuning against drift, and folds "
            "in foreign-object detection by watching for Q-factor dips - "
            "a living organism of passive copper and a little firmware. "
            "Step 4 - what would confirm it: a 5-meter corridor delivering "
            "100 watts at better than 80 percent end-to-end efficiency "
            "with field strengths under international exposure limits, "
            "audited by an independent lab. Step 5 - what would kill it: "
            "measured per-hop loss that refuses to drop below about 5 "
            "percent at commodity Q values, or tuning instability that "
            "collapses the chain when a human walks through it. What this "
            "does NOT claim: it does not repeal the inverse-square law, "
            "does not claim kilometer-scale transfer, and does not promise "
            "efficiency anywhere near a copper wire - it proposes making "
            "wireless good enough across a room to matter."),
        "citations": ["N. Tesla, Wardenclyffe experiments, 1901-1917",
                      "A. Kurs et al., Wireless power transfer via strongly "
                      "coupled magnetic resonances, Science 317, 2007",
                      "Wireless Power Consortium, Qi specification v1.3, 2021",
                      "IEEE Std C95.1-2019, RF exposure limits"],
    },
    {
        "key": "grid_100_renewables",
        "name": "Grid Stability with 100 Percent Renewables",
        "group": "Power Systems",
        "ladder_rank": 2,
        "ladder_tier": "approachable",
        "problem": ("How can an electric grid run stably on 100 percent "
                    "inverter-based renewable generation, with no spinning "
                    "synchronous machines to supply inertia and fault "
                    "current?"),
        "background": ("For a century the grid has been stabilized by the "
                       "rotating mass of synchronous generators: their "
                       "inertia resists frequency changes, and their "
                       "electromagnetics supply the fault current that "
                       "protective relays depend on. Solar and wind connect "
                       "through inverters that have no inherent inertia, "
                       "and at high penetration the old stability math "
                       "breaks down - phase-locked loops interact, weak "
                       "grids oscillate, and relays can mis-operate. The "
                       "2021 Texas freeze and South Australia's "
                       "system-black events showed how stability margins "
                       "thin as synchronous plant retires. Grid-forming "
                       "inverter research, synthetic inertia, and "
                       "synchronous condensers are partial answers; "
                       "several island grids now run hours at near-100 "
                       "percent inverter penetration, but no large "
                       "continental grid has done it, and the protection "
                       "and black-start questions are still open."),
        "why_it_matters": ("This is the control problem behind full "
                           "decarbonization of electricity: without it, "
                           "renewables hit a stability ceiling and fossil "
                           "plants must stay online as spinning insurance. "
                           "Solving it unlocks a zero-carbon grid that is "
                           "also cheaper to run, with batteries and "
                           "inverters providing services the old machines "
                           "never could."),
        "sig_pointer": ("The Signature approach proposes a "
                        "stability-as-a-service lattice: every inverter "
                        "runs grid-forming firmware that synthesizes "
                        "virtual inertia from a shared, time-stamped "
                        "stability state, so the grid behaves like one "
                        "giant virtual synchronous machine."),
        "signature_solution": ("Step 1 - assumption: the grid does not "
            "need real spinning mass, it needs the BEHAVIOR of spinning "
            "mass - a predictable voltage-behind-reactance response with "
            "bounded delay - and inverters can synthesize that behavior "
            "faster than any rotor if they agree on a common reference. "
            "Step 2 - reasoning path: grid-forming inverters already "
            "emulate virtual synchronous machines locally; the failure "
            "mode is disagreement between units during faults. A shared "
            "stability state broadcast over sub-millisecond time-stamped "
            "links (GPS-disciplined, with holdover oscillators for GPS "
            "outages) lets every inverter compute the same virtual rotor "
            "angle, turning a thousand independent controllers into one "
            "coherent machine. Step 3 - proposed mechanism: a three-layer "
            "stack - local grid-forming firmware with 100-microsecond "
            "response, a regional consensus layer exchanging rotor-state "
            "vectors at 10 kHz, and a supervisory layer that replays "
            "yesterday's disturbances in a digital twin each night to "
            "retune gains. Protection migrates to traveling-wave and "
            "differential schemes that do not need synchronous fault "
            "current, and black-start sequences are rehearsed in the twin "
            "before they are ever needed. Step 4 - what would confirm it: "
            "a hardware-in-the-loop demonstration of a 10-GW-equivalent "
            "synthetic system surviving the three canonical disturbances - "
            "a three-phase fault, a sudden 2-GW loss of infeed, and a "
            "GPS holdover event - with frequency nadir and recovery "
            "inside today's grid codes, witnessed by a transmission "
            "operator. Step 5 - what would kill it: measured consensus "
            "latency that cannot stay under the stability deadline across "
            "real utility networks, or an instability mode the digital "
            "twin fails to predict. What this does NOT claim: it does not "
            "claim inverters can create energy from nothing, does not "
            "remove the need for long-duration storage, and does not "
            "promise cheaper protection - it proposes making the "
            "inverter-only grid behave."),
        "citations": ["NERC, inverter-based resource performance guideline, "
                      "2023",
                      "Australian Energy Market Operator, system strength "
                      "framework, 2024",
                      "ERCOT winter storm Uri review, 2021",
                      "IEEE 2800-2022, interconnection of inverter-based "
                      "resources"],
    },
    {
        "key": "terahertz_room_temp",
        "name": "Terahertz Electronics That Work at Room Temperature",
        "group": "Devices & Materials",
        "ladder_rank": 3,
        "ladder_tier": "approachable",
        "problem": ("How can compact, efficient terahertz sources, "
                    "amplifiers, and detectors operate at room temperature, "
                    "closing the terahertz gap between electronics and "
                    "optics?"),
        "background": ("The terahertz band - roughly 0.1 to 10 THz - sits "
                       "between microwave electronics, which run out of "
                       "steam as transistors approach their speed limits, "
                       "and photonics, which struggle to make the tiny "
                       "photon energies efficiently. The result is the "
                       "terahertz gap: sources are either bulky "
                       "(quantum-cascade lasers needing cryogenic cooling "
                       "at the low end, vacuum tubes) or feeble "
                       "(frequency-multiplied diodes delivering "
                       "microwatts). Yet the band promises see-through "
                       "imaging, ultra-wideband short-range links, and "
                       "spectroscopy that fingerprints molecules. Two "
                       "decades of work on resonant-tunneling diodes, "
                       "plasma-wave transistors, and graphene devices "
                       "have produced impressive laboratory records but no "
                       "room-temperature watt-class source or sensitive "
                       "uncooled detector array that industry can buy."),
        "why_it_matters": ("Closing the gap unlocks non-ionizing security "
                           "and medical imaging, terabit short-range "
                           "wireless, and molecular sensing on a chip. The "
                           "terahertz band is the last large swath of "
                           "spectrum with no mature electronics - whoever "
                           "tames it at room temperature opens an entire "
                           "hardware industry."),
        "sig_pointer": ("The Signature approach proposes stacked "
                        "plasma-wave transistor arrays in which "
                        "two-dimensional electron gases oscillate in "
                        "synchronized cavities, pooling microwatts into "
                        "milliwatts at room temperature through "
                        "coherent combining."),
        "signature_solution": ("Step 1 - assumption: no single "
            "room-temperature device will ever deliver watts at 1 THz, so "
            "the winning architecture pools hundreds of weak oscillators "
            "coherently, the way phased arrays pool weak antennas. Step 2 "
            "- reasoning path: plasma-wave field-effect transistors in "
            "high-mobility materials already oscillate in the terahertz "
            "at room temperature via the Dyakonov-Shur instability, but "
            "each emits microwatts and they refuse to stay in phase. "
            "Injection-locking a two-dimensional array through a shared "
            "dielectric cavity forces phase coherence, and coherent "
            "combining makes output power grow as the square of the "
            "element count - 400 elements at 25 microwatts each become "
            "10 milliwatts in one beam. Step 3 - proposed mechanism: a "
            "silicon-interposer tile carrying a 20-by-20 array of "
            "plasma-wave transistors inside a micromachined cavity, with "
            "on-chip phase sensing trimming each gate bias 10,000 times "
            "per second to hold lock across temperature drift; tiles stack "
            "for higher power, and the same tile run in reverse is the "
            "detector. Step 4 - what would confirm it: a tile delivering "
            "1 milliwatt continuous at 1 THz at room temperature with "
            "phase noise clean enough for a communications link, measured "
            "on a calibrated power meter. Step 5 - what would kill it: "
            "phase-locking overhead that eats more power than the array "
            "emits, or thermal crosstalk that detunes neighbors faster "
            "than the trimming loop can follow. What this does NOT claim: "
            "it does not promise watts, does not claim to beat the "
            "fundamental Johnson noise limits of detection, and does not "
            "replace cryogenic quantum-cascade lasers where they already "
            "win - it proposes a room-temperature path to useful "
            "milliwatts."),
        "citations": ["M. Dyakonov and M. Shur, shallow water analogy to "
                      "plasma waves, 1993",
                      "M. Tonouchi, cutting-edge terahertz technology, "
                      "Nature Photonics 1, 2007",
                      "IRDS roadmap, beyond-CMOS and emerging devices, 2023",
                      "IEEE Transactions on Terahertz Science and "
                      "Technology, ongoing"],
    },
    {
        "key": "beyond_silicon_transistors",
        "name": "Beyond-Silicon Transistors at Silicon Scale",
        "group": "Computing Hardware",
        "ladder_rank": 4,
        "ladder_tier": "approachable",
        "problem": ("What replaces the silicon transistor when scaling "
                    "ends - a switch that industry can actually manufacture "
                    "by the trillion with silicon's cost, yield, and "
                    "reliability?"),
        "background": ("Moore's law carried computing for fifty years, but "
                       "silicon transistors now approach atomic limits: "
                       "gate lengths measured in dozens of atoms, leakage "
                       "currents that waste power, and fabs costing tens of "
                       "billions of dollars. Candidates abound - carbon "
                       "nanotube transistors (a full CNT computer ran at "
                       "Stanford in 2013), two-dimensional materials like "
                       "molybdenum disulfide, tunnel FETs that beat the "
                       "thermal voltage limit, and negative-capacitance "
                       "devices - yet none has survived the brutal "
                       "economics of the fab: defect densities, variability "
                       "across billions of devices, and integration with "
                       "the existing silicon tool chain. The industry "
                       "roadmap now bets on 3D stacking and chiplet "
                       "integration to extend silicon, but the fundamental "
                       "question - what is the next switch - is still open."),
        "why_it_matters": ("Computing's energy appetite is becoming a "
                           "civilizational constraint: datacenters already "
                           "consume percent-scale fractions of national "
                           "electricity. A better switch means either "
                           "faster machines or the same machines at a "
                           "tenth the power - the difference between AI "
                           "for everyone and AI only for those who can "
                           "afford the power bill."),
        "sig_pointer": ("The Signature approach proposes hybrid "
                        "silicon-backbone integration: keep the silicon "
                        "wafer and its trillion-device infrastructure, and "
                        "grow the beyond-silicon switch only where it wins "
                        "- in the top metal layers as a 3D-printed device "
                        "tier, letting economics, not ideology, decide the "
                        "mix."),
        "signature_solution": ("Step 1 - assumption: the next switch does "
            "not need to replace silicon everywhere, it needs to win "
            "somewhere cheap enough that fabs adopt it incrementally - "
            "history shows every successful device transition (bipolar to "
            "CMOS, planar to FinFET) was evolutionary in manufacturing. "
            "Step 2 - reasoning path: carbon nanotubes and 2D materials "
            "fail as full-wafer replacements because of defect density "
            "and placement, but as a back-end-of-line device tier they "
            "only need to work where placed, with silicon underneath "
            "handling memory, I/O, and repair routing around bad "
            "devices - exactly how bad blocks are managed in flash "
            "memory. Step 3 - proposed mechanism: a standard CMOS wafer "
            "grown normally, then a low-temperature (under 400 C) "
            "deposition of aligned nanotube or MoS2 films on top, "
            "patterned into logic and memory tiers connected by "
            "through-layer vias; a built-in self-test maps defects at "
            "wafer probe and the silicon base reroutes around them. "
            "Manufacturing risk is contained because the silicon flow "
            "never changes. Step 4 - what would confirm it: a foundry "
            "pilot line producing hybrid wafers at 90 percent functional "
            "yield with the top tier delivering 3x energy-delay "
            "improvement on a real benchmark, audited across 1,000 "
            "wafers. Step 5 - what would kill it: defect densities in "
            "the top tier that stay above 1 per million devices after "
            "three process generations, or via resistance that erases "
            "the energy advantage. What this does NOT claim: it does not "
            "claim nanotubes or 2D materials will ever beat silicon "
            "dollar-for-dollar as a standalone technology, and does not "
            "promise a return to historical Moore's-law cadence - it "
            "proposes an evolutionary on-ramp the industry can actually "
            "afford to walk."),
        "citations": ["G. Hills et al., modern microprocessor built from "
                      "complementary carbon nanotube transistors, Nature "
                      "572, 2019",
                      "IRDS, International Roadmap for Devices and Systems, "
                      "2023 edition",
                      "S. B. Desai et al., MoS2 transistors with 1-nm gate, "
                      "Science 354, 2016"],
    },
    {
        "key": "quantum_interconnects",
        "name": "Quantum Interconnects Between Processors",
        "group": "Quantum Electronics",
        "ladder_rank": 5,
        "ladder_tier": "approachable",
        "problem": ("How can separate quantum processors be linked so that "
                    "entanglement - the fragile resource quantum computers "
                    "run on - survives the trip between them?"),
        "background": ("A single quantum processor is limited by how many "
                       "qubits fit in one cryostat and how well they can "
                       "be controlled. The natural escape is modularity: "
                       "many small processors linked by quantum "
                       "interconnects, sharing entanglement the way "
                       "classical machines share data over a network. But "
                       "entanglement is destroyed by the slightest "
                       "interaction with the environment - a photon lost "
                       "in fiber, a phonon in a converter, thermal noise "
                       "in an amplifier. Transduction between microwave "
                       "qubits and optical photons (the only carrier that "
                       "travels well) remains at percent-level efficiency "
                       "in the lab, far from the 99 percent-plus a real "
                       "network needs. Quantum repeaters, entanglement "
                       "distillation, and error-corrected links are all "
                       "active research, but no one has yet entangled two "
                       "distant processors at useful rates."),
        "why_it_matters": ("Modular quantum computers are the only "
                           "credible path to million-qubit machines: no "
                           "single cryostat will ever hold that many "
                           "qubits with individual control lines. Quantum "
                           "interconnects are also the foundation of a "
                           "future quantum internet - unhackable "
                           "communication and networked quantum sensors. "
                           "Without them, quantum computing stays stuck "
                           "at the single-rack scale."),
        "sig_pointer": ("The Signature approach proposes entanglement "
                        "distillation factories at every network node: "
                        "accept terrible raw transduction efficiency, then "
                        "purify many noisy pairs into few excellent ones "
                        "with local error correction, trading rate for "
                        "fidelity the way classical networks trade "
                        "bandwidth for reliability."),
        "signature_solution": ("Step 1 - assumption: raw "
            "microwave-to-optical transduction will stay lossy for a "
            "decade, so the interconnect must be designed around "
            "terrible raw fidelity, not in hope of perfect hardware. "
            "Step 2 - reasoning path: entanglement distillation is "
            "provably able to convert many low-fidelity pairs into fewer "
            "high-fidelity pairs using only local operations and classical "
            "communication; combined with heralded entanglement (knowing "
            "exactly which attempts succeeded), a node can run a "
            "continuous purification pipeline. The math says 1,000 raw "
            "pairs at 60 percent fidelity distill to a handful above 99 "
            "percent - the rate is low, but the quality is what "
            "computation needs. Step 3 - proposed mechanism: each "
            "interconnect node carries a small dedicated distillation "
            "processor (a few dozen physical qubits whose only job is "
            "purification), fed by massively parallel low-efficiency "
            "transducers; a link-layer protocol heralds successes, "
            "schedules distillation rounds, and delivers certified "
            "high-fidelity pairs to the compute qubits on demand. Step 4 "
            "- what would confirm it: two processors 10 meters apart "
            "sharing distilled pairs above 99 percent fidelity at a "
            "sustained rate of 1 kHz, verified by Bell-inequality "
            "tomography, with the distillation overhead fully "
            "characterized. Step 5 - what would kill it: distillation "
            "overhead that grows faster than linearly with distance, or "
            "memory decoherence in the node that destroys pairs faster "
            "than purification creates them. What this does NOT claim: it "
            "does not claim to beat the fundamental loss limits of fiber "
            "or transducers, does not promise a quantum internet "
            "tomorrow, and does not remove the need for better hardware - "
            "it proposes making bad hardware useful through protocol."),
        "citations": ["H. J. Kimble, the quantum internet, Nature 453, 2008",
                      "C. H. Bennett et al., purification of noisy "
                      "entanglement, Physical Review Letters 76, 1996",
                      "U.S. DOE, quantum internet blueprint, 2020"],
    },
    {
        "key": "universal_memory",
        "name": "Universal Memory: One Memory to Replace the Hierarchy",
        "group": "Computing Hardware",
        "ladder_rank": 6,
        "ladder_tier": "approachable",
        "problem": ("Can a single non-volatile memory technology match "
                    "SRAM speed, DRAM density and endurance, and flash "
                    "cost - collapsing the memory hierarchy into one "
                    "universal memory?"),
        "background": ("Every computer today juggles a hierarchy: fast, "
                       "tiny, volatile SRAM caches; larger, slower DRAM; "
                       "and dense, cheap, non-volatile flash - with "
                       "constant, energy-hungry shuffling between levels. "
                       "A universal memory would be fast enough for "
                       "caches, dense enough for main memory, non-volatile "
                       "enough to never lose data, and cheap enough to "
                       "ship by the terabyte. Candidates have cycled for "
                       "decades: magnetoresistive RAM, phase-change "
                       "memory, resistive RAM, ferroelectric RAM. Intel's "
                       "Optane (3D XPoint) came closest commercially "
                       "before being discontinued in 2022. Each candidate "
                       "wins on two axes and loses on the third - speed "
                       "vs endurance vs cost - and the hierarchy "
                       "survives."),
        "why_it_matters": ("Memory traffic dominates the energy budget of "
                           "modern computing; collapsing the hierarchy "
                           "would cut system power dramatically and make "
                           "computers effectively instant-on, with no "
                           "boot, no lost work, and simpler software. It "
                           "is also the missing piece for brain-like "
                           "computing, where memory and processing must "
                           "merge."),
        "sig_pointer": ("The Signature approach proposes a heterogeneous "
                        "universal tier: stop demanding one physics wins "
                        "everywhere and instead bond three memory "
                        "technologies into one address space with a "
                        "hardware-managed migration engine, presenting "
                        "software with a single universal memory."),
        "signature_solution": ("Step 1 - assumption: no single device "
            "physics will ever win on speed, endurance, density, and "
            "cost simultaneously, so the universal memory should be an "
            "ARCHITECTURE, not a device - one address space, several "
            "physics underneath. Step 2 - reasoning path: operating "
            "systems already migrate pages between DRAM and flash "
            "transparently; moving that migration into hardware, at "
            "cache-line granularity and nanosecond timescales, lets each "
            "technology serve the access pattern it fits - fast "
            "low-endurance cells for hot lines, dense slow cells for "
            "cold data - while software sees one flat, persistent "
            "memory. Step 3 - proposed mechanism: a 3D-stacked cube with "
            "an SRAM-speed spintronic hot tier, a dense phase-change "
            "warm tier, and a capacious resistive cold tier, glued by a "
            "migration controller that learns access patterns with a "
            "tiny on-chip predictor and moves lines preemptively; "
            "persistence is guaranteed by capacitor-backed flush of the "
            "hot tier on power loss. Step 4 - what would confirm it: a "
            "prototype cube running unmodified server workloads within "
            "10 percent of DRAM-system performance, surviving 10 "
            "million power cycles with zero data loss, at a projected "
            "cost within 2x of DRAM per gigabyte. Step 5 - what would "
            "kill it: migration traffic that consumes more energy than "
            "the hierarchy it replaces, or endurance of the hot tier "
            "below 10^12 cycles under real write patterns. What this "
            "does NOT claim: it does not claim a single miracle device, "
            "does not promise SRAM latency for every access, and does "
            "not remove the need for continued device research - it "
            "proposes winning at the architecture level instead."),
        "citations": ["Intel Optane discontinuation, 2022",
                      "D. Apalkov et al., spin-transfer torque magnetic "
                      "random access memory, Proceedings of the IEEE 104, "
                      "2016",
                      "H.-S. P. Wong et al., phase change memory, "
                      "Proceedings of the IEEE 98, 2010"],
    },
    {
        "key": "chip_thermal_wall",
        "name": "The Chip Thermal Wall",
        "group": "Computing Hardware",
        "ladder_rank": 7,
        "ladder_tier": "approachable",
        "problem": ("How can the heat of computation be removed fast "
                    "enough to let chips keep getting faster, when power "
                    "density already forces most of a chip to stay dark?"),
        "background": ("Transistors keep shrinking but the power each "
                       "square millimeter can dissipate has barely moved: "
                       "around 100 watts per square centimeter for "
                       "affordable cooling. The result is dark silicon - "
                       "most of a modern chip must stay idle at any "
                       "moment or it would melt. Datacenters now spend "
                       "nearly as much engineering on cooling (liquid "
                       "loops, immersion baths, rear-door heat "
                       "exchangers) as on compute. Microfluidic cooling "
                       "etched directly into silicon, diamond heat "
                       "spreaders, and two-phase immersion all work in "
                       "the lab, but cost, reliability, and maintenance "
                       "keep them exotic. The thermal wall is now the "
                       "primary limiter of single-thread performance and "
                       "a major tax on AI training clusters."),
        "why_it_matters": ("Every watt of heat removed cheaply is a watt "
                           "of computation unlocked. Breaking the thermal "
                           "wall revives single-chip performance growth, "
                           "shrinks datacenter cooling plants (a major "
                           "electricity and water consumer), and makes "
                           "high-performance computing viable in hot "
                           "climates and at the edge."),
        "sig_pointer": ("The Signature approach proposes cooling as a "
                        "first-class chip layer: microfluidic channels "
                        "etched between active tiers in 3D-stacked chips, "
                        "with dielectric coolant pumped per-tier based on "
                        "live thermal maps, turning the hottest layer "
                        "into the best-cooled one."),
        "signature_solution": ("Step 1 - assumption: heat is generated "
            "inside the stack, so cooling must live inside the stack - "
            "bolting bigger heatsinks on top has diminishing returns "
            "because the thermal resistance is dominated by the silicon "
            "itself. Step 2 - reasoning path: 3D chip stacking puts the "
            "hottest logic in the middle of the sandwich, exactly where "
            "conventional cooling cannot reach. Etching microfluidic "
            "channels between tiers shortens the heat path from "
            "millimeters to tens of microns; dielectric fluids (no "
            "short-circuit risk) can carry 1 kW per square centimeter in "
            "the lab. A per-tier pump schedule driven by on-die thermal "
            "sensors concentrates flow where the hotspot is, instead of "
            "flooding the whole chip. Step 3 - proposed mechanism: a "
            "standard 3D stack with 50-micron fluid channels etched in a "
            "dedicated cooling tier, fed by piezoelectric micropumps, "
            "with a closed loop to a facility water heat exchanger; the "
            "thermal controller is part of the chip's power management "
            "firmware and throttles flow, not clocks, as the first "
            "response to heat. Step 4 - what would confirm it: a stacked "
            "processor sustaining 500 W per square centimeter for 1,000 "
            "hours with junction temperatures under 85 C and zero "
            "coolant leaks, at a manufacturing cost adder under 15 "
            "percent. Step 5 - what would kill it: channel clogging or "
            "pump failures that strand heat mid-stack, or fluid "
            "compatibility issues that corrode vias within two years. "
            "What this does NOT claim: it does not repeal thermodynamics "
            "- the heat still goes somewhere - and does not make cooling "
            "free; it proposes moving the cooling to where the heat is."),
        "citations": ["H. Esmaeilzadeh et al., dark silicon and the end of "
                      "multicore scaling, ISCA 2011",
                      "IBM Zurich, microchannel-cooled 3D chip stacks, 2013",
                      "U.S. DOE COOLERCHIPS program, 2022"],
    },
    {
        "key": "ambient_energy_harvesting",
        "name": "Harvesting Ambient Electromagnetic Energy at Useful Power",
        "group": "Wireless & RF",
        "ladder_rank": 8,
        "ladder_tier": "approachable",
        "problem": ("Can the stray radio energy filling our cities - "
                    "broadcast, cellular, Wi-Fi - be harvested at power "
                    "levels useful for real devices, not just laboratory "
                    "curiosities?"),
        "background": ("A city is bathed in radio-frequency energy, but "
                       "at power densities of microwatts to nanowatts per "
                       "square centimeter - orders of magnitude below what "
                       "even a sensor needs to transmit. Rectennas "
                       "(rectifying antennas) convert RF to DC, and "
                       "researchers have powered temperature sensors and "
                       "backscatter tags from TV towers and Wi-Fi routers. "
                       "The hard limits are fundamental: ambient power "
                       "density is tiny, diode rectifiers are inefficient "
                       "at low input power, and impedance matching across "
                       "many bands wastes what little is caught. Ambient "
                       "backscatter communication (University of "
                       "Washington, 2013) cleverly sidesteps the problem "
                       "by reflecting rather than generating signals, but "
                       "true energy harvesting at milliwatt scale from "
                       "ambient RF alone remains out of reach."),
        "why_it_matters": ("Trillions of future sensors cannot all have "
                           "their batteries changed. Milliwatt-scale "
                           "ambient harvesting would enable "
                           "deploy-and-forget sensing for infrastructure, "
                           "agriculture, and health - plus a path to "
                           "battery-free consumer devices that sip the "
                           "city's stray spectrum."),
        "sig_pointer": ("The Signature approach proposes cooperative "
                        "harvesting apertures: large-area metamaterial "
                        "surfaces that concentrate ambient RF from many "
                        "bands onto a single high-efficiency rectifier, "
                        "paired with duty-cycled devices designed from "
                        "birth to live on microwatts."),
        "signature_solution": ("Step 1 - assumption: the ambient field is "
            "weak but everywhere, so the winning move is aperture, not "
            "efficiency - a square meter of collector sees a thousand "
            "times the power of a square centimeter, and buildings have "
            "square meters to spare. Step 2 - reasoning path: "
            "metasurfaces can be engineered with absorption resonances "
            "at multiple bands simultaneously (TV, cellular, Wi-Fi), "
            "funneling caught energy through a waveguide combiner to one "
            "rectifier operating at its sweet-spot input power instead of "
            "a thousand starved diodes. Paired with devices designed for "
            "extreme duty cycling - sleep at nanowatts, burst at "
            "milliwatts for milliseconds - the energy budget closes. "
            "Step 3 - proposed mechanism: peel-and-stick metasurface "
            "tiles for walls and windows, each tile a multi-band "
            "absorber feeding a single tunnel-diode rectifier; a power "
            "management chip cold-starts from 100 nanowatts and budgets "
            "energy to the sensor's burst radio. Step 4 - what would "
            "confirm it: a 0.25-square-meter tile sustaining a "
            "temperature-plus-humidity sensor reporting every 60 seconds "
            "indefinitely in a real office, with a year of logged "
            "uptime. Step 5 - what would kill it: measured multi-band "
            "combining loss above 50 percent, or rectifier efficiency "
            "that collapses below 10 percent at the actual per-band "
            "input powers found indoors. What this does NOT claim: it "
            "does not promise to power phones or anything with a screen, "
            "does not claim ambient RF rivals a battery, and does not "
            "ignore that intentional transmitters would help enormously "
            "- it proposes making the truly ambient case useful."),
        "citations": ["V. Liu et al., ambient backscatter, SIGCOMM 2013",
                      "S. Hemour and K. Wu, radio-frequency rectifier for "
                      "electromagnetic energy harvesting, Proceedings of "
                      "the IEEE 102, 2014",
                      "H. J. Visser and R. J. M. Vullers, RF energy "
                      "harvesting and transport, Proceedings of the IEEE "
                      "101, 2013"],
    },
    {
        "key": "emi_wireless_world",
        "name": "Electromagnetic Interference in a Wireless-Everything World",
        "group": "Wireless & RF",
        "ladder_rank": 9,
        "ladder_tier": "approachable",
        "problem": ("How can billions of wireless devices coexist without "
                    "drowning each other in electromagnetic interference, "
                    "as spectrum gets more crowded every year?"),
        "background": ("Every wireless device is both a transmitter and a "
                       "victim: Wi-Fi fights Bluetooth fights Zigbee in "
                       "the 2.4 GHz band, 5G base stations desensitize "
                       "satellite weather sensors, and a single faulty LED "
                       "driver can jam an entire smart home. Traditional "
                       "answers - licensed spectrum, filters, shielding - "
                       "scale poorly and cost money and size. Cognitive "
                       "radio promised devices that sense and dodge "
                       "interference, but two decades on, real products "
                       "barely adapt. Meanwhile the device count "
                       "compounds: the average home now hosts dozens of "
                       "radios, factories hundreds. Interference is no "
                       "longer an edge case; it is the operating "
                       "environment."),
        "why_it_matters": ("Wireless is becoming the nervous system of "
                           "industry, medicine, and transport - and "
                           "nervous systems cannot tolerate constant "
                           "seizures. Solving coexistence unlocks dense "
                           "industrial IoT, reliable medical telemetry, "
                           "and autonomous systems that must communicate "
                           "in electromagnetically hostile places."),
        "sig_pointer": ("The Signature approach proposes an interference "
                        "etiquette enforced in silicon: every radio chip "
                        "carries a mandatory politeness engine that "
                        "senses, predicts, and yields spectrum the way "
                        "drivers yield lanes, with misbehaving devices "
                        "throttled by their neighbors."),
        "signature_solution": ("Step 1 - assumption: interference is a "
            "tragedy of the commons, and commons problems are solved by "
            "etiquette plus enforcement, not by more spectrum - the "
            "physics of sharing is social before it is technical. Step 2 "
            "- reasoning path: modern radios already digitize their whole "
            "band; a small always-on sensing core can classify "
            "interferers (Wi-Fi beacons, microwave ovens, arc welders) "
            "and predict their patterns. If every device yields "
            "predictably - backing off during a neighbor's known burst "
            "window, hopping before collisions rather than after - total "
            "throughput rises for everyone, a classic coordination game "
            "with a better equilibrium. Step 3 - proposed mechanism: a "
            "politeness engine in the radio firmware - sense, classify, "
            "predict, yield - plus a reputation channel where devices "
            "broadcast interference complaints; a device that ignores "
            "repeated complaints gets its transmit duty cycle throttled "
            "by consensus of its neighbors. Step 4 - what would confirm "
            "it: a 200-radio testbed in one office showing 3x median "
            "throughput and 10x worst-case latency improvement versus "
            "today's polite-but-dumb protocols, with a deliberately "
            "misbehaving device neutralized by throttling. Step 5 - what "
            "would kill it: classification that fails in real multipath "
            "clutter, or legacy devices that cannot be upgraded and "
            "defect from the etiquette, collapsing the equilibrium. What "
            "this does NOT claim: it does not create new spectrum, does "
            "not fix intentional jamming, and does not promise "
            "interference-free operation - it proposes making dense "
            "coexistence graceful instead of catastrophic."),
        "citations": ["J. Mitola and G. Q. Maguire, cognitive radio, IEEE "
                      "Personal Communications 6, 1999",
                      "FCC, spectrum policy task force report, 2002",
                      "IEEE 802.11ax (Wi-Fi 6) spatial reuse mechanisms, "
                      "2021"],
    },
    {
        "key": "ultrafast_charging_grid",
        "name": "Ultra-Fast Charging Without Breaking the Local Grid",
        "group": "Power Systems",
        "ladder_rank": 10,
        "ladder_tier": "approachable",
        "problem": ("How can electric vehicles charge in minutes at "
                    "megawatt power without overloading the local "
                    "distribution grid that was never designed for it?"),
        "background": ("A megawatt charger draws as much power as a small "
                       "neighborhood, and distribution feeders were sized "
                       "for homes, not truck stops. Ten trucks charging "
                       "at once can exceed a substation's rating, trigger "
                       "voltage collapse, and force utilities into "
                       "multi-million-dollar upgrades with multi-year "
                       "lead times. Managed charging (scheduling sessions "
                       "against grid capacity) helps but cannot serve a "
                       "highway plaza at rush hour. Battery-buffered "
                       "chargers - a big stationary battery that trickle-"
                       "charges from the grid and bursts to vehicles - "
                       "are being deployed, but the buffer itself is "
                       "expensive, degrades, and merely moves the "
                       "problem. The industry needs charging that behaves "
                       "like a good grid citizen by design."),
        "why_it_matters": ("Heavy transport electrification stalls without "
                           "it: trucks cannot wait hours, and utilities "
                           "cannot rebuild every feeder. Solving the "
                           "grid-charger interface unlocks electric "
                           "freight, electric aviation ground ops, and "
                           "charging plazas that go up in months instead "
                           "of years."),
        "sig_pointer": ("The Signature approach proposes the charger as a "
                        "grid asset: every ultra-fast station carries a "
                        "buffer plus grid-forming inverters, so it shaves "
                        "its own peaks, sells frequency services back to "
                        "the utility, and pays for its buffer with grid "
                        "revenue."),
        "signature_solution": ("Step 1 - assumption: the charger's worst "
            "enemy - its peak demand charge - is also its greatest asset, "
            "because a megawatt of flexible power electronics is exactly "
            "what the grid will pay for as frequency response. Step 2 - "
            "reasoning path: a battery-buffered charger with grid-forming "
            "inverters can cap its grid draw at a negotiated flat profile "
            "while bursting megawatts to vehicles from the buffer; in "
            "idle moments the same inverters sell synthetic inertia and "
            "voltage support. The demand-charge savings plus ancillary "
            "service revenue amortize the buffer battery, flipping the "
            "economics. Step 3 - proposed mechanism: a standardized "
            "station architecture - 2 MWh buffer, 3 MW of grid-forming "
            "inverter capacity, and a utility contract template that "
            "pre-approves the flat-draw profile and the service payments; "
            "a fleet orchestrator staggers vehicle sessions against "
            "buffer state-of-charge so the grid profile never twitches. "
            "Step 4 - what would confirm it: a 10-stall plaza running a "
            "year with grid draw never exceeding its 1-MW contract while "
            "serving full-rate sessions, publishing audited revenue "
            "showing the buffer paid back within 7 years. Step 5 - what "
            "would kill it: ancillary service prices collapsing as every "
            "station chases them, or buffer degradation under "
            "high-C-rate cycling that halves the assumed lifetime. What "
            "this does NOT claim: it does not remove the need for "
            "eventual feeder upgrades everywhere, does not make "
            "batteries free, and does not solve generation adequacy - it "
            "proposes making the charger pay its own way onto the "
            "existing grid."),
        "citations": ["U.S. DOE, Megawatt Charging System (MCS) standard "
                      "development, 2023",
                      "California Energy Commission, freight charging "
                      "infrastructure assessments, 2023",
                      "IEEE 1547-2018, interconnection of distributed "
                      "resources"],
    },
    {
        "key": "solid_state_transformers",
        "name": "Solid-State Transformers for the Grid",
        "group": "Power Systems",
        "ladder_rank": 11,
        "ladder_tier": "approachable",
        "problem": ("Can power-electronic transformers replace century-old "
                    "iron-and-copper transformers, adding controllability, "
                    "DC ports, and fault management at acceptable cost and "
                    "reliability?"),
        "background": ("The distribution transformer is a Victorian "
                       "masterpiece: two windings around an iron core, "
                       "98-plus percent efficient, lasting 40 years with "
                       "no maintenance. Its flaw is stupidity - fixed "
                       "voltage ratio, no DC interface, no fault-current "
                       "limiting, no communication. Solid-state "
                       "transformers replace the iron with high-frequency "
                       "power electronics, offering voltage regulation, "
                       "bidirectional power flow, direct DC ports for "
                       "solar and batteries, and built-in protection. "
                       "Research programs (notably FREEDM at North "
                       "Carolina State) have built impressive prototypes, "
                       "but efficiency still trails iron, the component "
                       "count hurts reliability math, and nothing yet "
                       "touches the incumbent's cost per kVA."),
        "why_it_matters": ("The future grid is power-electronics-native: "
                           "solar, batteries, EVs, and data centers all "
                           "speak DC or variable AC. An intelligent "
                           "transformer at every node turns the dumb "
                           "delivery network into a controllable, "
                           "self-healing fabric - the hardware missing "
                           "link of the smart grid."),
        "sig_pointer": ("The Signature approach proposes hybrid "
                        "transformers: keep the iron core for the bulk "
                        "power path and add a fractional-rated electronic "
                        "wrapping that provides all the smarts at a "
                        "tenth the silicon of a full solid-state design."),
        "signature_solution": ("Step 1 - assumption: 90 percent of the "
            "transformer's job is moving bulk power efficiently - a job "
            "iron does nearly perfectly - and only 10 percent needs "
            "intelligence, so the electronics should be sized for the 10 "
            "percent, not the 100. Step 2 - reasoning path: a "
            "fractional-rated series compensator injected in series with "
            "a conventional transformer can regulate voltage, limit fault "
            "current, and provide a DC auxiliary port while processing "
            "only a fraction of the throughput power - exactly how "
            "unified power-flow controllers work at transmission scale. "
            "Efficiency stays near iron levels because the bulk path "
            "never sees a switching loss. Step 3 - proposed mechanism: a "
            "standard distribution transformer with an integrated "
            "back-to-back converter rated at 15 percent of nameplate, "
            "wound into the same tank; the converter trims voltage "
            "plus-or-minus 10 percent, rides through sags, feeds a 400-V "
            "DC bus for local solar and batteries, and opens "
            "electronically on faults in microseconds. Step 4 - what "
            "would confirm it: a utility pilot of 100 hybrid units over "
            "3 years showing transformer losses within 0.3 percent of "
            "conventional units, voltage complaints down 80 percent, "
            "and converter failure rates under 1 percent per year. Step "
            "5 - what would kill it: electronic failure modes that take "
            "the whole transformer offline (defeating the reliability "
            "story), or installed cost more than 2x conventional that "
            "utilities refuse to rate-base. What this does NOT claim: it "
            "does not claim full solid-state performance, does not "
            "eliminate the iron core, and does not promise a DC-only "
            "future - it proposes getting 80 percent of the smart-grid "
            "benefit at 20 percent of the disruption."),
        "citations": ["A. Q. Huang et al., the future renewable electric "
                      "energy delivery and management (FREEDM) system, "
                      "Proceedings of the IEEE 99, 2011",
                      "X. She et al., solid state transformer topologies, "
                      "IEEE Transactions on Power Electronics 29, 2014",
                      "DOE, solid state power substation roadmap, 2021"],
    },
    {
        "key": "superconducting_cables",
        "name": "Superconducting Power Cables at Practical Scale",
        "group": "Power Systems",
        "ladder_rank": 12,
        "ladder_tier": "approachable",
        "problem": ("Can high-temperature superconducting cables carry "
                    "grid-scale power through dense cities at a total cost "
                    "that beats conventional copper and new overhead "
                    "lines?"),
        "background": ("A superconducting cable carries five to ten times "
                       "the power of a copper cable in the same duct - a "
                       "miracle for cities where digging new tunnels is "
                       "politically and financially impossible. "
                       "High-temperature superconductors (cooled by liquid "
                       "nitrogen at 77 K, not liquid helium) made "
                       "demonstration projects real: Long Island, Essen, "
                       "and Seoul have all run kilometer-scale HTS cables. "
                       "But the refrigeration plants consume power around "
                       "the clock, terminations and joints remain "
                       "hand-built art, fault currents can quench the "
                       "cable, and the installed cost per megawatt-mile "
                       "still loses to conventional cable in most "
                       "business cases. The technology works; the "
                       "economics do not, yet."),
        "why_it_matters": ("Megacities need several times more power "
                           "delivery in the same underground corridors to "
                           "electrify transport and heating. Superconducting "
                           "cables are the only technology that multiplies "
                           "corridor capacity without new tunnels - "
                           "potentially saving decades of civil works."),
        "sig_pointer": ("The Signature approach proposes cooling-as-shared-"
                        "infrastructure: one district cryogenic loop "
                        "serving many cable segments plus superconducting "
                        "fault-current limiters, so refrigeration cost is "
                        "amortized and quench risk is designed out."),
        "signature_solution": ("Step 1 - assumption: refrigeration is the "
            "cost disease, and diseases of shared infrastructure are cured "
            "by sharing - one cryoplant serving ten cable segments costs "
            "little more than one serving a single demo. Step 2 - "
            "reasoning path: district cooling loops already serve whole "
            "city blocks; a liquid-nitrogen district loop with redundant "
            "cryocoolers amortizes capital and maintenance across every "
            "HTS cable, fault-current limiter, and SMES unit on the loop. "
            "Standardized factory-built terminations (the hand-built art "
            "today) attack the second cost driver, and resistive-type "
            "fault-current limiters at each substation cap fault currents "
            "so cables never see quench-level surges. Step 3 - proposed "
            "mechanism: a city-block pilot - 3 km of HTS cable on one "
            "nitrogen loop, two standardized terminations per segment, "
            "limiters at both substations, with the cryoplant "
            "maintained under a 20-year service contract priced per "
            "megawatt-mile. Step 4 - what would confirm it: five years "
            "of operation with availability above 99.9 percent and a "
            "levelized cost per megawatt-mile within 30 percent of new "
            "conventional duct construction (the true competitor where "
            "digging is impossible). Step 5 - what would kill it: "
            "cryocooler maintenance costs that refuse to fall with "
            "scale, or a single quench event that destroys utility "
            "confidence regardless of statistics. What this does NOT "
            "claim: it does not claim HTS beats copper where ducts "
            "exist, does not promise room-temperature operation, and "
            "does not remove the need for skilled cryogenic "
            "maintenance - it proposes making the city-center business "
            "case close."),
        "citations": ["S. S. Kalsi, high temperature superconducting "
                      "cable projects review, 2011",
                      "AmpaCity project, Essen, Germany, 2014",
                      "KEPCO, Shingal HTS cable project, Korea, ongoing"],
    },
    # ---------------- COMPOUNDED (ladder 13-24) ----------------
    {
        "key": "silicon_photonics_cost",
        "name": "Silicon Photonics at Consumer Cost",
        "group": "Computing Hardware",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("How can optical interconnects - light instead of "
                    "copper for moving data - reach price points where "
                    "they ship in consumer devices, not just datacenter "
                    "transceivers?"),
        "background": ("Copper wires on chips and between servers are "
                       "running out of bandwidth per watt: moving a bit "
                       "across a server rack now costs more energy than "
                       "computing it. Silicon photonics - guiding light "
                       "in silicon waveguides built in CMOS fabs - "
                       "promises orders of magnitude more bandwidth at "
                       "lower energy. Datacenter transceivers proved the "
                       "technology, and co-packaged optics (optics bonded "
                       "directly to switch chips) is entering production. "
                       "But the laser source remains the cost and "
                       "reliability bottleneck: silicon cannot lase "
                       "efficiently, so lasers are bonded or grown as "
                       "exotic III-V chips, and packaging optics still "
                       "needs sub-micron alignment that fights "
                       "commodity economics."),
        "why_it_matters": ("AI training clusters are now limited by "
                           "interconnect, not computation - thousands of "
                           "GPUs starve waiting for data. Cheap photonics "
                           "removes that ceiling and eventually brings "
                           "optical I/O to laptops and phones, ending the "
                           "copper bottleneck everywhere."),
        "sig_pointer": ("The Signature approach proposes the laser as a "
                        "shared utility: one robust external laser feeding "
                        "dozens of silicon modulators over a photonic "
                        "interposer, so the expensive light source is "
                        "amortized and the silicon does only the cheap "
                        "modulation."),
        "signature_solution": ("Step 1 - assumption: the laser will "
            "remain the expensive, fragile part for a decade, so the "
            "architecture must need as few lasers as possible - one per "
            "package, not one per channel. Step 2 - reasoning path: a "
            "single high-power comb laser produces dozens of wavelength "
            "channels; silicon ring modulators - cheap, CMOS-native - "
            "imprint data on each wavelength independently. Distributing "
            "one comb across a photonic interposer to 64 modulators "
            "amortizes the laser cost 64 ways, and the interposer's "
            "lithographic alignment replaces active fiber alignment. "
            "Step 3 - proposed mechanism: a package with one comb laser, "
            "a silicon interposer carrying arrayed-waveguide multiplexers "
            "and ring modulators, flip-chipped to the compute die; a "
            "slow control loop trims ring resonances against temperature "
            "using integrated heaters, holding lock across a 60 C range. "
            "Step 4 - what would confirm it: a 51.2-Tb/s co-packaged "
            "module at under 5 pJ per bit with the laser representing "
            "less than 20 percent of module cost, running 5,000 hours "
            "without re-tuning. Step 5 - what would kill it: comb laser "
            "lifetime below datacenter requirements, or thermal "
            "crosstalk between rings that defeats the trimming loop at "
            "full channel count. What this does NOT claim: it does not "
            "claim silicon will ever lase well, does not promise "
            "all-optical computing, and does not remove packaging "
            "entirely - it proposes making the laser somebody else's "
            "shared problem."),
        "citations": ["C. Sun et al., single-chip microprocessor that "
                      "communicates directly using light, Nature 528, 2015",
                      "Co-packaged optics industry multi-source agreements, "
                      "2022-2024",
                      "IRDS, heterogeneous integration roadmap, 2023"],
    },
    {
        "key": "spintronics_logic",
        "name": "Spintronic Logic Beyond the Laboratory",
        "group": "Devices & Materials",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Can logic built on electron spin - rather than "
                    "electron charge - escape the laboratory and deliver "
                    "its promised non-volatility and ultra-low energy in "
                    "real products?"),
        "background": ("Spintronics manipulates the spin of electrons "
                       "instead of their charge, offering devices that "
                       "remember their state with no power and switch "
                       "with potentially far less energy than CMOS. "
                       "Spin-transfer-torque MRAM has reached commercial "
                       "production as embedded memory, proving the "
                       "materials can survive a fab. But spin LOGIC - "
                       "gates and interconnects that compute with spin - "
                       "remains a laboratory menagerie: spin-wave "
                       "devices, all-spin logic, magneto-electric "
                       "switches. The obstacles are brutal: spin signals "
                       "decay over nanometers, spin-to-charge conversion "
                       "is lossy, and no spintronic gate yet beats a CMOS "
                       "gate on the metrics that matter - speed times "
                       "energy times area - outside carefully chosen "
                       "corners."),
        "why_it_matters": ("Charge-based switching leaks and wastes; "
                           "spin promises logic that idles at zero power "
                           "and computes where the data already sits. "
                           "Even a partial win - non-volatile logic for "
                           "normally-off systems - would transform "
                           "battery-powered and energy-harvesting "
                           "devices."),
        "sig_pointer": ("The Signature approach proposes normally-off "
                        "spin-CMOS hybrids: use spintronics only for "
                        "state retention and normally-off power gating, "
                        "letting CMOS do the fast switching, so each "
                        "technology covers the other's weakness."),
        "signature_solution": ("Step 1 - assumption: spintronics will not "
            "beat CMOS at raw switching for a generation, so stop racing "
            "CMOS and instead attack the problem CMOS cannot solve - "
            "leakage and state loss when power sleeps. Step 2 - reasoning "
            "path: the energy of a mostly-idle device is dominated by "
            "keeping state alive, not by switching. Spin-based latches "
            "hold state with zero standby power; waking a normally-off "
            "block costs one spin-write per latch, far cheaper than "
            "leaking for hours. The hybrid - CMOS datapath, spintronic "
            "state - gets the best of both without demanding that spin "
            "logic win on speed. Step 3 - proposed mechanism: standard "
            "CMOS logic with spin-orbit-torque latches at every state "
            "element, a power controller that snapshots and sleeps "
            "blocks in microseconds, and magnetic immunity designed in "
            "from the start (shielding plus error coding on the spin "
            "state). Step 4 - what would confirm it: a microcontroller "
            "demonstrating 100x lower sleep energy than its CMOS-only "
            "twin on a real sensor workload, with 10-year data "
            "retention proven by accelerated aging. Step 5 - what would "
            "kill it: spin-write energy that stays above the leakage "
            "energy it saves at realistic duty cycles, or magnetic "
            "disturbance susceptibility that fails industrial "
            "qualification. What this does NOT claim: it does not claim "
            "spin logic will replace CMOS gates, does not promise "
            "faster computation, and does not ignore the fab "
            "integration cost - it proposes winning the normally-off "
            "battle first."),
        "citations": ["S. A. Wolf et al., spintronics: a spin-based "
                      "electronics vision, Science 294, 2001",
                      "A. D. Kent and D. C. Worledge, a new spin on "
                      "magnetic memories, Nature Nanotechnology 10, 2015",
                      "J. Grollier et al., neuromorphic spintronics, "
                      "Nature Electronics 3, 2020"],
    },
    {
        "key": "neuromorphic_datacenter",
        "name": "Neuromorphic Chips at Datacenter Scale",
        "group": "Computing Hardware",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Can brain-inspired neuromorphic hardware scale from "
                    "research chips to datacenter deployments that beat "
                    "GPUs on real AI workloads?"),
        "background": ("Neuromorphic chips mimic the brain's event-driven, "
                       "spiking operation: neurons fire only when needed, "
                       "memory sits beside compute, and energy per "
                       "operation can be orders of magnitude below a GPU. "
                       "IBM's TrueNorth (2014) and Intel's Loihi proved "
                       "the concept in silicon, showing remarkable "
                       "efficiency on spiking neural networks. But "
                       "datacenters run dense matrix math on conventional "
                       "deep networks, not spikes; converting workloads "
                       "loses accuracy, the software stack is immature, "
                       "and no neuromorphic system has yet beaten a GPU "
                       "cluster on a production AI task at equal "
                       "accuracy. The field faces a chicken-and-egg "
                       "problem: no workloads without hardware at scale, "
                       "no hardware at scale without workloads."),
        "why_it_matters": ("AI's energy trajectory is unsustainable on "
                           "current hardware - training runs already "
                           "consume megawatt-hours. Brain-like efficiency "
                           "is the most credible path to AI that the "
                           "planet's power grid can actually support, "
                           "plus always-on intelligence at the edge where "
                           "batteries rule."),
        "sig_pointer": ("The Signature approach proposes neuromorphic "
                        "accelerators as inference co-processors for "
                        "spike-friendly workloads (event cameras, anomaly "
                        "detection, sparse attention), earning their "
                        "datacenter slot on measured energy-per-inference "
                        "before attempting training."),
        "signature_solution": ("Step 1 - assumption: neuromorphic hardware "
            "will not displace GPUs at dense training this decade, so it "
            "should attack the workload shaped like a brain workload - "
            "sparse, event-driven, always-on inference - where its "
            "advantage is 100x, not 10 percent. Step 2 - reasoning path: "
            "event cameras, vibration monitors, and network intrusion "
            "detectors produce sparse spike-like data natively; running "
            "them on spiking hardware avoids the wasteful "
            "dense-frame-then-sparsify pipeline entirely. Winning a few "
            "production inference niches funds the software stack and "
            "manufacturing learning curve that training-scale hardware "
            "will later need. Step 3 - proposed mechanism: a PCIe "
            "neuromorphic inference card with a mature runtime that "
            "ingests ONNX models through an automated spike-conversion "
            "pipeline with accuracy guardrails; datacenter deployment "
            "starts with anomaly-detection fleets where 99 percent "
            "accuracy at 1 percent of GPU energy is already a business "
            "case. Step 4 - what would confirm it: a production "
            "deployment processing 1 million inferences per day at "
            "measured 50x lower energy per inference than the GPU "
            "baseline at equal accuracy, sustained for a year. Step 5 - "
            "what would kill it: spike-conversion accuracy loss that "
            "customers will not accept, or GPU efficiency gains that "
            "close the gap faster than neuromorphic software matures. "
            "What this does NOT claim: it does not claim spikes will "
            "replace dense math everywhere, does not promise "
            "neuromorphic training soon, and does not dismiss the "
            "software mountain - it proposes an inference beachhead."),
        "citations": ["P. A. Merolla et al., a million spiking-neuron "
                      "integrated circuit (TrueNorth), Science 345, 2014",
                      "M. Davies et al., Loihi: a neuromorphic manycore "
                      "processor, IEEE Micro 38, 2018",
                      "K. Roy et al., towards spike-based machine "
                      "intelligence, Proceedings of the IEEE 107, 2019"],
    },
    {
        "key": "single_molecule_manufacturing",
        "name": "Single-Molecule Electronics That Can Be Manufactured",
        "group": "Devices & Materials",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Can electronic devices built from individual "
                    "molecules be manufactured reliably by the billions, "
                    "not just demonstrated one at a time in a lab?"),
        "background": ("Aviram and Ratner proposed the molecular rectifier "
                       "in 1974: a single molecule as a diode, the "
                       "ultimate miniaturization. Fifty years later, "
                       "researchers can wire individual molecules between "
                       "electrodes and measure rectification, switching, "
                       "even transistor action - one molecule at a time, "
                       "with break-junction techniques that are "
                       "fundamentally unmanufacturable. The gaps are "
                       "contact chemistry (molecule-electrode interfaces "
                       "vary wildly), placement (putting the right "
                       "molecule in the right spot a billion times), and "
                       "stability (molecules migrate, degrade, and "
                       "desorb). Self-assembled monolayers offer a path "
                       "to ordered films, but defect rates remain "
                       "astronomical by semiconductor standards."),
        "why_it_matters": ("Molecules are the smallest possible electronic "
                           "components, self-assemble for free, and offer "
                           "chemical tunability no lithography can match - "
                           "sensors that recognize single molecules, "
                           "memory at the density limit, and electronics "
                           "grown rather than carved."),
        "sig_pointer": ("The Signature approach proposes giving up on "
                        "placing single molecules and instead printing "
                        "self-assembled monolayer devices where the "
                        "ensemble average is the device - statistics, not "
                        "perfection, as the manufacturing principle."),
        "signature_solution": ("Step 1 - assumption: per-molecule "
            "perfection is unachievable, so the device must be defined "
            "by the statistics of millions of molecules, the way a "
            "resistor is defined by the statistics of trillions of "
            "atoms. Step 2 - reasoning path: self-assembled monolayers "
            "form ordered films spontaneously over large areas; if the "
            "readout averages over 10^6 molecules, individual defects, "
            "misplacements, and dead molecules average out, and the "
            "device characteristic becomes reproducible. Redundancy and "
            "error coding - borrowed from flash memory's bad-block "
            "management - handle the rest. Step 3 - proposed mechanism: "
            "crossbar arrays where each junction is a monolayer patch "
            "read differentially against a reference patch, with "
            "on-chip calibration mapping each patch's offset at wafer "
            "probe; molecular design targets bistable molecules with "
            "large on-off ratios so the ensemble signal survives "
            "averaging. Step 4 - what would confirm it: a 1-kb monolayer "
            "memory array with bit error rate below 10^-6 after "
            "calibration, stable for 1 year at 85 C, built with "
            "wafer-scale self-assembly. Step 5 - what would kill it: "
            "monolayer desorption or migration that shifts calibration "
            "faster than monthly recalibration can track, or on-off "
            "ratios that collapse when molecules pack densely. What this "
            "does NOT claim: it does not claim single-molecule "
            "transistors will compute, does not promise silicon-like "
            "defect rates, and does not solve contact chemistry in "
            "general - it proposes making imperfection irrelevant by "
            "design."),
        "citations": ["A. Aviram and M. Ratner, molecular rectifiers, "
                      "Chemical Physics Letters 29, 1974",
                      "D. Xiang et al., molecular-scale electronics, "
                      "Advanced Materials 28, 2016",
                      "L. Sun et al., single-molecule electronics "
                      "review, Chem 5, 2019"],
    },
    {
        "key": "cryogenic_logic_scale",
        "name": "Cryogenic Superconducting Logic at Scale",
        "group": "Computing Hardware",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Can superconducting digital logic - switching at "
                    "hundreds of gigahertz with near-zero energy - scale "
                    "to million-gate systems anyone can afford to cool?"),
        "background": ("Superconducting logic families (RSFQ and its "
                       "energy-efficient descendants) switch Josephson "
                       "junctions in picoseconds with energy per operation "
                       "thousands of times below CMOS. In principle a "
                       "cryogenic supercomputer could outperform any "
                       "room-temperature machine. In practice the field "
                       "has been stuck for decades: memory is the "
                       "killer (no dense cryogenic RAM exists), the "
                       "cooling overhead eats the energy advantage at "
                       "small scales, chip areas are limited by "
                       "inductor-heavy layouts, and the design tool "
                       "ecosystem is primitive. Japan's and America's "
                       "multi-hundred-million-dollar programs produced "
                       "impressive demos but no sustained product line."),
        "why_it_matters": ("If the memory and cooling economics close, "
                           "cryogenic computing offers the only known "
                           "path to 100-GHz-class digital logic - "
                           "transforming scientific computing, signal "
                           "processing, and the control electronics that "
                           "quantum computers themselves need."),
        "sig_pointer": ("The Signature approach proposes cryogenic logic "
                        "as the quantum computer's control plane: small, "
                        "valuable, already-cold systems where the cooling "
                        "is free and the memory problem is sidestepped by "
                        "keeping state in the qubits."),
        "signature_solution": ("Step 1 - assumption: the technology will "
            "not win as a general-purpose supercomputer soon, so it "
            "should win first where its weaknesses do not matter and its "
            "strengths are priceless - inside the dilution refrigerator "
            "next to the qubits. Step 2 - reasoning path: quantum "
            "processors need massive classical control bandwidth at "
            "cryogenic temperatures; today it comes through hundreds of "
            "lossy room-temperature cables. Superconducting control logic "
            "sitting at 4 K beside the qubits slashes latency and wiring "
            "heat load, the cooling is already paid for, and the logic "
            "blocks are small enough that the memory problem barely "
            "bites. Success there funds the tooling and foundry base for "
            "larger ambitions. Step 3 - proposed mechanism: a "
            "standardized cryogenic control chipset - pulse generators, "
            "multiplexers, and readout discriminators in energy-efficient "
            "RSFQ - qualified for 4-K operation with bit error rates "
            "below 10^-12, delivered as chiplets that quantum startups "
            "can buy instead of building. Step 4 - what would confirm "
            "it: a 1,000-qubit system controlled entirely by on-chip "
            "cryogenic logic with measured 10x reduction in control "
            "wiring heat load and no increase in qubit error rates over "
            "6 months. Step 5 - what would kill it: flux-trapping or "
            "thermal-cycling failures that make field reliability worse "
            "than cables, or CMOS cryogenic control that improves fast "
            "enough to close the gap. What this does NOT claim: it does "
            "not claim a cryogenic supercomputer is near, does not solve "
            "cryogenic memory, and does not promise the cooling "
            "economics work at datacenter scale - it proposes a "
            "beachhead where the fridge is already running."),
        "citations": ["K. K. Likharev and V. K. Semenov, RSFQ logic/memory "
                      "family, IEEE Transactions on Applied "
                      "Superconductivity 1, 1991",
                      "D. S. Holmes et al., energy-efficient superconducting "
                      "computing, IEEE Transactions on Applied "
                      "Superconductivity 23, 2013",
                      "IARPA C3 program results, 2014-2019"],
    },
    {
        "key": "dynamic_wireless_charging",
        "name": "Dynamic Wireless Charging for Moving Vehicles",
        "group": "Wireless & RF",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("Can electric vehicles charge while driving over "
                    "electrified roads, at efficiencies and costs that "
                    "justify tearing up highways?"),
        "background": ("Dynamic wireless charging - coils buried in the "
                       "roadway transferring power to moving vehicles - "
                       "would shrink batteries, kill range anxiety, and "
                       "electrify freight without megawatt truck stops. "
                       "Pilots exist: Sweden's eRoadArlanda, Electreon's "
                       "segments in Italy and Germany, and university "
                       "test tracks have all moved real power to moving "
                       "vehicles. But efficiency drops with misalignment "
                       "and speed, the road coils must survive trucks and "
                       "frost heave, billing and safety systems are "
                       "unsettled, and the civil cost per lane-kilometer "
                       "is enormous. Nobody has shown the full-system "
                       "economics beating bigger batteries plus static "
                       "charging."),
        "why_it_matters": ("It rewrites EV economics: a car that charges "
                           "while driving needs a fraction of the battery, "
                           "cutting vehicle cost, weight, and mineral "
                           "demand. For freight corridors it could be the "
                           "difference between electrification that works "
                           "and one that does not."),
        "sig_pointer": ("The Signature approach proposes charging only "
                        "where vehicles already slow down - toll plazas, "
                        "climbing lanes, and freight corridors - using "
                        "modular coil cassettes that slide out for repair "
                        "without closing the road."),
        "signature_solution": ("Step 1 - assumption: electrifying every "
            "highway kilometer is economically absurd, so the system must "
            "win on 5 percent of the road - the segments where vehicles "
            "are slow, heavy, and predictable. Step 2 - reasoning path: "
            "at 30 km/h through a toll plaza or up a grade, coupling "
            "time per coil triples versus highway speed, misalignment "
            "falls, and efficiency climbs into the viable range; freight "
            "corridors concentrate the energy demand onto few "
            "lane-kilometers, and fleet operators (not consumers) pay "
            "for predictable energy. Modular cassettes - coil, "
            "electronics, and shielding in a swap-out tray - make "
            "maintenance a 20-minute lane closure, not a reconstruction. "
            "Step 3 - proposed mechanism: a 2-km freight climbing-lane "
            "pilot with cassette coils, vehicle-side receivers as a "
            "fleet-standard option, per-vehicle metering via the coil "
            "handshake, and foreign-object shutdown in under 100 ms. "
            "Step 4 - what would confirm it: one year of operation "
            "showing truck energy cost per km below diesel parity with "
            "coil-to-battery efficiency above 80 percent and cassette "
            "swap times under 30 minutes. Step 5 - what would kill it: "
            "road-wear failure rates demanding cassette replacement "
            "faster than every 5 years, or fleet operators refusing the "
            "receiver cost. What this does NOT claim: it does not claim "
            "whole-highway electrification is viable, does not promise "
            "passenger-car economics soon, and does not ignore the "
            "electromagnetic exposure questions - it proposes winning "
            "the freight corridor first."),
        "citations": ["S. Y. Choi et al., advances in wireless power "
                      "transfer for roadway-powered EVs, IEEE Journal of "
                      "Emerging Topics in Power Electronics 4, 2016",
                      "Electreon pilot projects, Sweden/Italy/Germany, "
                      "2020-2024",
                      "eRoadArlanda, Sweden, 2018"],
    },
    {
        "key": "emp_hardening_grid",
        "name": "EMP Hardening for the Civilian Power Grid",
        "group": "Power Systems",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("How can the civilian power grid survive a severe "
                    "electromagnetic pulse or geomagnetic storm without a "
                    "rebuild costing more than the grid itself?"),
        "background": ("A high-altitude electromagnetic pulse or a "
                       "Carrington-class solar storm induces quasi-DC "
                       "currents in long transmission lines, saturating "
                       "transformer cores, overheating windings, and "
                       "potentially cascading into continental blackout. "
                       "The 1989 Quebec blackout (a moderate storm) "
                       "collapsed a grid in 90 seconds; the 2008 EMP "
                       "Commission warned of multi-year recovery if large "
                       "transformers are destroyed, since replacements "
                       "have 1-2 year lead times. Hardening options exist "
                       "- neutral-current blockers, EMP-rated shielding, "
                       "spare transformer programs - but utilities face "
                       "an impossible cost-benefit analysis for an event "
                       "that may never come, and regulators have not "
                       "forced the issue."),
        "why_it_matters": ("The grid is the foundation every other "
                           "infrastructure stands on; a continental "
                           "transformer-loss event would take years to "
                           "repair and cost trillions. Affordable "
                           "hardening converts an existential tail risk "
                           "into a managed engineering problem."),
        "sig_pointer": ("The Signature approach proposes sacrificial "
                        "protection at the transformer: neutral-current "
                        "blockers plus a strategic spare-transformer "
                        "reserve with standardized designs, so the grid "
                        "bends instead of breaking and recovery is "
                        "measured in weeks."),
        "signature_solution": ("Step 1 - assumption: the grid cannot be "
            "made invulnerable, but it can be made repairable - the "
            "catastrophe scenario is not the pulse, it is the years-long "
            "wait for custom transformers. Step 2 - reasoning path: "
            "geomagnetically induced currents enter transformers through "
            "grounded neutrals; DC-blocking capacitors in the neutral "
            "stop the quasi-DC while passing normal AC - a solved, "
            "deployable technology. For the residual risk, a national "
            "reserve of standardized spare extra-high-voltage "
            "transformers (a handful of designs covering most of the "
            "fleet) with pre-arranged heavy transport converts a "
            "2-year lead time into a 2-week swap. Step 3 - proposed "
            "mechanism: mandatory neutral blockers on all transformers "
            "above 345 kV in high-risk latitudes, a 50-unit strategic "
            "reserve stored at rail-accessible depots, and annual "
            "grid-scale GIC drills; costs are socialized through a "
            "reliability surcharge, the way spare capacity already is. "
            "Step 4 - what would confirm it: a modeled Carrington-class "
            "event showing transformer losses under 5 percent of the "
            "fleet with blockers plus reserve, validated against the "
            "measured GIC data from the 2024 solar storms. Step 5 - "
            "what would kill it: blocker resonance problems that create "
            "new failure modes worse than the disease, or political "
            "refusal to fund a reserve for a maybe-never event. What "
            "this does NOT claim: it does not promise the grid stays up "
            "through the event, does not address the E1 fast-pulse "
            "threat to electronics in full, and does not pretend the "
            "economics are easy - it proposes bounding the catastrophe."),
        "citations": ["U.S. EMP Commission, report of the Commission to "
                      "Assess the Threat, 2008",
                      "North American Electric Reliability Corporation, "
                      "geomagnetic disturbance reliability standard "
                      "TPL-007, 2023",
                      "J. Kappenman, geomagnetic storms and their impacts, "
                      "2007"],
    },
    {
        "key": "hvdc_breakers",
        "name": "High-Voltage DC Circuit Breakers",
        "group": "Power Systems",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("How can faults be interrupted in multi-terminal "
                    "high-voltage DC grids, where there is no natural "
                    "current zero-crossing to help extinguish the arc?"),
        "background": ("AC breakers cheat: the current crosses zero 100 "
                       "or 120 times per second, giving the arc a chance "
                       "to die. DC has no zero crossing - a fault current "
                       "in a 500-kV DC line just keeps rising, fed by "
                       "converter capacitors, reaching tens of kiloamps "
                       "in milliseconds. Point-to-point HVDC links avoid "
                       "the problem by shutting down the whole link, but "
                       "a meshed DC grid - the backbone of offshore wind "
                       "and intercontinental renewables - needs breakers "
                       "that isolate only the faulted branch in under 5 "
                       "milliseconds. Hybrid designs (a fast mechanical "
                       "switch paralleled by semiconductors) have been "
                       "demonstrated by ABB and others, but cost, "
                       "reliability, and standardization for real "
                       "multi-vendor grids remain open."),
        "why_it_matters": ("Offshore wind, desert solar, and "
                           "intercontinental clean-energy trading all "
                           "want a meshed DC supergrid; without DC "
                           "breakers, every fault blacks out the whole "
                           "network, and the supergrid stays a set of "
                           "isolated point-to-point links."),
        "sig_pointer": ("The Signature approach proposes current-injection "
                        "breakers with superconducting fault-current "
                        "limiters upstream: the limiter caps the fault "
                        "so the breaker only has to interrupt a tamed "
                        "current, splitting one impossible job into two "
                        "tractable ones."),
        "signature_solution": ("Step 1 - assumption: interrupting 25 kA "
            "in 3 ms in one device is the hard way; limiting the fault "
            "to 8 kA first and then interrupting is two easy problems "
            "instead of one impossible one. Step 2 - reasoning path: "
            "resistive superconducting fault-current limiters quench "
            "in under a millisecond when current exceeds their critical "
            "value, inserting resistance that caps the fault; a hybrid "
            "mechanical-semiconductor breaker downstream then faces a "
            "current it was actually designed for. The limiter recovers "
            "superconductivity automatically after the fault clears. "
            "Step 3 - proposed mechanism: a standardized 320-kV DC "
            "breaker module - limiter stage, hybrid interrupter stage, "
            "metal-oxide surge absorber - with open interface specs so "
            "any vendor's converter can connect; protection logic uses "
            "traveling-wave fault location to identify the faulted "
            "branch in under 1 ms. Step 4 - what would confirm it: a "
            "three-terminal 320-kV test grid where a bolted fault is "
            "cleared with only the faulted branch de-energized, healthy "
            "branches undisturbed, demonstrated 50 consecutive times. "
            "Step 5 - what would kill it: limiter recovery times that "
            "exceed reclosing deadlines, or quench behavior under "
            "repeated faults that degrades the superconductor within "
            "years. What this does NOT claim: it does not claim parity "
            "with AC breaker cost yet, does not solve DC grid "
            "protection philosophy in full, and does not remove the "
            "need for converter fault tolerance - it proposes making "
            "the breaker a solvable two-stage problem."),
        "citations": ["C. M. Franck, HVDC circuit breakers: a review, IEEE "
                      "Transactions on Power Delivery 26, 2011",
                      "ABB hybrid HVDC breaker demonstration, 2012",
                      "CIGRE brochure 683, DC grid protection, 2017"],
    },
    {
        "key": "wide_bandgap_cost",
        "name": "Wide-Bandgap Semiconductors at Silicon Cost",
        "group": "Devices & Materials",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Can silicon carbide and gallium nitride power "
                    "devices - faster, cooler, more efficient than silicon "
                    "- reach cost parity so they displace silicon "
                    "everywhere it matters?"),
        "background": ("Wide-bandgap semiconductors switch faster and "
                       "withstand higher voltages and temperatures than "
                       "silicon, cutting converter losses dramatically: "
                       "SiC MOSFETs and GaN HEMTs are already taking over "
                       "EV onboard chargers and fast chargers. But SiC "
                       "wafers cost an order of magnitude more than "
                       "silicon, defect densities (micropipes, basal "
                       "plane dislocations) still hurt yield, and GaN "
                       "lacks a native low-cost substrate. The industry "
                       "is scaling - 200-mm SiC wafers are arriving - "
                       "but at system level the premium often still "
                       "erases the efficiency savings, slowing adoption "
                       "in cost-sensitive applications like solar "
                       "inverters and motor drives."),
        "why_it_matters": ("Power electronics mediate every watt from "
                           "source to load; shaving converter losses by "
                           "percentage points across the whole economy "
                           "saves terawatt-hours. Cost parity would put "
                           "wide-bandgap devices in every appliance, "
                           "charger, and industrial drive on earth."),
        "sig_pointer": ("The Signature approach proposes GaN-on-silicon "
                        "as the cost weapon and SiC reserved for where "
                        "voltage demands it: engineer the system around "
                        "cheap GaN for everything under 650 V and let "
                        "SiC own only the high-voltage niche."),
        "signature_solution": ("Step 1 - assumption: the market does not "
            "need one winner; it needs the right bandgap at the right "
            "voltage, and most power electronics lives under 650 V where "
            "GaN-on-silicon can ride silicon's cost curve. Step 2 - "
            "reasoning path: GaN grown on cheap silicon substrates "
            "inherits silicon wafer economics; the lattice mismatch "
            "defects that once killed devices are increasingly managed "
            "with buffer engineering. Reserve expensive SiC for traction "
            "inverters and grid gear above 1 kV, where its advantages "
            "are decisive and volumes justify the wafer cost. System "
            "designers stop asking which technology wins and start "
            "asking which voltage bin each serves. Step 3 - proposed "
            "mechanism: an industry voltage-bin standard - GaN-on-Si to "
            "650 V, SiC above - with shared qualification data and "
            "reference designs that let small manufacturers adopt "
            "wide-bandgap without in-house device physics teams; "
            "continued 200-mm SiC scaling attacks the high end. Step 4 "
            "- what would confirm it: GaN-on-Si power ICs at price "
            "parity with silicon superjunction MOSFETs in the 100-650 V "
            "range by bill-of-materials audit across three vendors. "
            "Step 5 - what would kill it: GaN dynamic on-resistance "
            "(current collapse) that refuses to stay tamed across "
            "temperature, or SiC defect reduction stalling so the "
            "high-voltage tier never reaches its promised reliability. "
            "What this does NOT claim: it does not claim GaN replaces "
            "SiC at high voltage, does not promise silicon's "
            "disappearance, and does not ignore packaging - which "
            "dominates fast-switching performance - it proposes a "
            "division of labor the economics can support."),
        "citations": ["J. Millan et al., a survey of wide bandgap power "
                      "semiconductor devices, IEEE Transactions on Power "
                      "Electronics 29, 2014",
                      "Yole Group, power SiC and GaN market reports, 2024",
                      "U.S. DOE, wide bandgap semiconductor R&D, ongoing"],
    },
    {
        "key": "motor_power_density",
        "name": "Electric Motors at Ten Times the Power Density",
        "group": "Devices & Materials",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("How can electric motors reach an order of magnitude "
                    "higher power density - kilowatts per kilogram - to "
                    "electrify aviation and heavy industry?"),
        "background": ("Today's best motors deliver roughly 5-10 kW per "
                       "kilogram; electric aircraft need 20-plus, and "
                       "truly transformative applications want 50. The "
                       "limits are magnetic saturation of iron, copper "
                       "losses that melt windings, and cooling that adds "
                       "more weight than it saves. NASA's high-efficiency "
                       "megawatt motor program, superconducting motor "
                       "research, and advanced cooling (oil-spray, "
                       "hollow conductors) have all pushed the frontier, "
                       "but each gain fights physics: stronger magnets "
                       "need rare earths, higher speeds need better "
                       "bearings, and every cooling scheme adds system "
                       "mass. No clear path to 10x exists in a single "
                       "technology."),
        "why_it_matters": ("Power density is the gatekeeper of electric "
                           "flight, electric ships, and compact "
                           "industrial drives. A 10x motor turns regional "
                           "electric aircraft from dream to product and "
                           "shrinks every EV drivetrain."),
        "sig_pointer": ("The Signature approach proposes stacking modest "
                        "gains multiplicatively: superconducting "
                        "windings plus iron-free topologies plus direct "
                        "conductor cooling, each contributing 2-3x, "
                        "compounding to the order of magnitude."),
        "signature_solution": ("Step 1 - assumption: no single breakthrough "
            "delivers 10x, but four independent 2x improvements multiply "
            "to 16x - the path is a system stack, not a miracle material. "
            "Step 2 - reasoning path: superconducting windings eliminate "
            "copper loss (2-3x); air-core/ironless topologies remove "
            "saturation limits and iron mass (2x); direct liquid cooling "
            "inside hollow conductors raises current density (2x); and "
            "high-speed operation with magnetic bearings raises power at "
            "fixed torque (2x). Each is demonstrated separately; the "
            "unsolved problem is integrating them without the subsystems "
            "fighting. Step 3 - proposed mechanism: a reference 1-MW "
            "aviation motor design combining MgB2 superconducting "
            "windings at 20 K, Halbach-array permanent-magnet rotor, "
            "direct-conductor cooling, and 20,000-rpm operation, built "
            "as an open reference the industry can iterate on rather "
            "than a proprietary product. Step 4 - what would confirm "
            "it: a demonstrator sustaining 25 kW/kg continuous for 100 "
            "hours with measured efficiency above 98 percent, "
            "independently tested. Step 5 - what would kill it: "
            "superconducting AC loss at high speed that erases the "
            "winding advantage, or system mass (cryocooler plus "
            "structure) that drags net density back under 10 kW/kg. "
            "What this does NOT claim: it does not promise 10x in one "
            "step, does not claim superconductors are maintenance-free, "
            "and does not ignore the rare-earth supply question - it "
            "proposes compounding demonstrated gains."),
        "citations": ["NASA, high efficiency megawatt motor (HEMM) program, "
                      "2020",
                      "K. S. Haran et al., high power density superconducting "
                      "rotating machines, Superconductor Science and "
                      "Technology 30, 2017",
                      "U.S. DOE, electric motor R&D targets, 2023"],
    },
    {
        "key": "solid_state_lidar",
        "name": "Solid-State Lidar at Automotive Cost",
        "group": "Wireless & RF",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("Can solid-state lidar - no spinning mirrors, "
                    "chip-scale beam steering - reach the cost, range, "
                    "and reliability that mass-market vehicles demand?"),
        "background": ("Lidar gives machines centimeter-accurate 3D "
                       "vision, but classic units spin lasers on "
                       "mechanical scanners: expensive, bulky, and "
                       "vibration-sensitive. Solid-state approaches - "
                       "optical phased arrays, flash lidar, FMCW "
                       "coherent detection - promise chip-scale devices "
                       "with no moving parts. Progress is real: FMCW "
                       "lidar adds velocity measurement and sunlight "
                       "immunity, and costs have fallen 10x in a decade. "
                       "But automotive qualification demands 200-meter "
                       "range in rain, eye-safe power, 15-year "
                       "reliability, and sub-hundred-dollar cost at "
                       "volume - a combination no solid-state lidar has "
                       "yet demonstrated, and several high-profile "
                       "startups have failed trying."),
        "why_it_matters": ("Affordable lidar is the missing sensor for "
                           "safe autonomy and a workhorse for robotics, "
                           "drones, and industrial automation. Solving "
                           "the cost-reliability equation unlocks "
                           "machine vision everywhere cameras alone "
                           "cannot be trusted."),
        "sig_pointer": ("The Signature approach proposes FMCW-on-silicon "
                        "with shared photonic integration: one chip "
                        "carrying laser, phased array, and coherent "
                        "receiver, so cost falls with silicon volume "
                        "economics instead of optical assembly labor."),
        "signature_solution": ("Step 1 - assumption: the cost disease is "
            "optical assembly labor - aligning discrete lasers, lenses, "
            "and detectors - so the cure is integration: everything on "
            "one photonic chip, aligned by lithography, not by hand. "
            "Step 2 - reasoning path: frequency-modulated continuous-wave "
            "lidar measures range and velocity coherently, needing only "
            "milliwatts of returned light, which relaxes the power "
            "aperture that makes flash lidar expensive; silicon "
            "photonics can host the laser (heterogeneously integrated), "
            "the optical phased array for steering, and the balanced "
            "detectors on one die. One chip, one package, tested on a "
            "wafer prober like any IC. Step 3 - proposed mechanism: a "
            "1550-nm FMCW lidar SoC - integrated laser, 128-element "
            "phased array, coherent receiver array - with automotive "
            "temperature qualification built into the design rules "
            "(athermal waveguides, redundant emitters); calibration "
            "data stored on-chip at wafer probe. Step 4 - what would "
            "confirm it: units demonstrating 200-m range on 10-percent "
            "reflective targets in rain, passing AEC-Q100-style "
            "qualification, with quoted volume pricing under 150 "
            "dollars. Step 5 - what would kill it: phased-array "
            "sidelobes that create phantom targets no algorithm can "
            "fully suppress, or laser integration yields that keep "
            "chip cost above the target at automotive volumes. What "
            "this does NOT claim: it does not claim lidar alone solves "
            "autonomy, does not promise immunity to all weather, and "
            "does not dismiss camera-radar fusion - it proposes making "
            "the lidar itself a commodity chip."),
        "citations": ["C. V. Poulton et al., coherent lidar with optical "
                      "phased arrays, IEEE JSTQE 2022",
                      "National Academies, assessment of lidar "
                      "technologies, 2021",
                      "SAE J3083, lidar performance classes, ongoing"],
    },
    {
        "key": "implant_wireless_power",
        "name": "Deep-Tissue Wireless Power for Implants",
        "group": "Wireless & RF",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": ("How can medical implants deep in the body receive "
                    "wireless power safely and efficiently, ending the "
                    "era of battery-replacement surgeries?"),
        "background": ("Pacemakers, neurostimulators, and drug pumps run "
                       "on batteries that die in 5-15 years, each "
                       "replacement a surgery with infection risk. "
                       "Wireless power through tissue is brutally hard: "
                       "tissue absorbs RF (heating limits cap exposure), "
                       "magnetic coupling falls off with distance and "
                       "misalignment, and implants must be tiny. "
                       "Research spans mid-field RF (optimized "
                       "wavelengths that focus in tissue), ultrasonic "
                       "power transfer (sound penetrates tissue well), "
                       "and piezoelectric receivers. Lab demos power "
                       "millimeter-scale devices through centimeters of "
                       "tissue, but efficiency, heating, and long-term "
                       "biocompatibility at therapeutic power levels "
                       "remain unsolved for deep implants."),
        "why_it_matters": ("Millions live with implants; eliminating "
                           "replacement surgeries removes risk, cost, and "
                           "suffering. It also enables entirely new "
                           "implants - distributed neural interfaces, "
                           "smart orthopedics - that batteries could "
                           "never support."),
        "sig_pointer": ("The Signature approach proposes ultrasonic power "
                        "as the primary channel: sound penetrates tissue "
                        "with far less heating than RF, and millimeter "
                        "piezoelectric receivers harvest it efficiently."),
        "signature_solution": ("Step 1 - assumption: tissue is kinder to "
            "sound than to radio - acoustic attenuation in soft tissue "
            "is low at sub-megahertz frequencies, and the heating per "
            "delivered milliwatt favors ultrasound by an order of "
            "magnitude. Step 2 - reasoning path: a wearable phased array "
            "can focus ultrasound to a millimeter spot at 5-10 cm depth, "
            "track the implant as the patient moves (using the implant's "
            "own backscatter as a beacon), and deliver milliwatts while "
            "staying under FDA acoustic exposure limits. Piezoelectric "
            "receivers at resonance convert efficiently at millimeter "
            "scale - exactly the implant form factor. Step 3 - proposed "
            "mechanism: a flexible wearable patch with 256 ultrasonic "
            "elements, beamforming firmware that locks onto the "
            "implant's beacon 100 times per second, and a closed-loop "
            "thermal model that throttles power before tissue heating "
            "approaches limits; the implant carries a tiny rechargeable "
            "cell as a buffer for movement gaps. Step 4 - what would "
            "confirm it: a large-animal trial powering a deep implant "
            "continuously for 6 months with measured tissue heating "
            "under 1 C and no adverse histology. Step 5 - what would "
            "kill it: bone shadowing that blocks the beam for common "
            "implant sites, or patient-motion tracking that cannot hold "
            "focus during normal activity. What this does NOT claim: it "
            "does not claim ultrasound suits every implant location, "
            "does not bypass regulatory safety testing, and does not "
            "promise to power high-draw devices like ventricular assist "
            "pumps - it proposes a safe channel for the milliwatt "
            "implants that dominate medicine."),
        "citations": ["S. Ozeri and D. Shmilovitz, ultrasonic transcutaneous "
                      "energy transfer, IEEE Transactions on Biomedical "
                      "Engineering 57, 2010",
                      "FDA guidance, RF and acoustic exposure limits for "
                      "medical devices",
                      "J. Charthad et al., wireless power for implants, "
                      "IEEE TBioCAS 2015"],
    },
    # ---------------- ADVANCED (ladder 25-34) ----------------
    {
        "key": "thz_links_range",
        "name": "Terahertz Wireless Links at Real-World Range",
        "group": "Wireless & RF",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("Can terahertz wireless links - promising terabits "
                    "per second - work beyond laboratory benches, through "
                    "real air, rain, and movement?"),
        "background": ("Terahertz frequencies offer enormous bandwidth: "
                       "a 10-GHz-wide channel at 300 GHz could carry "
                       "100 Gb/s with simple modulation. But the air "
                       "itself fights back - water vapor absorbs "
                       "terahertz strongly (tens of dB per kilometer at "
                       "humid conditions), rain scatters it, and the "
                       "pencil beams needed for link budget demand "
                       "precise tracking of moving endpoints. Research "
                       "has demonstrated 100-plus Gb/s over meters and "
                       "kilometer-range links in dry conditions, and "
                       "6G visions pencil terahertz in for 2030s "
                       "backhaul. Yet adaptive, weather-robust, mobile "
                       "terahertz networking - the thing that would "
                       "matter - remains unsolved."),
        "why_it_matters": ("Fiber-fast wireless would erase the "
                           "last-hundred-meters bottleneck: instant "
                           "datacenter interconnects, wireless VR with no "
                           "compromise, and backhaul where fiber cannot "
                           "go. It is also the only spectrum left with "
                           "room for 6G's ambitions."),
        "sig_pointer": ("The Signature approach proposes "
                        "weather-adaptive terahertz meshes: short hops, "
                        "massive antenna arrays, and machine-learned "
                        "channel prediction that routes around rain "
                        "cells the way the internet routes around "
                        "congestion."),
        "signature_solution": ("Step 1 - assumption: no single terahertz "
            "link will ever be weather-proof, so the network must be - "
            "short hops under 200 meters, dense meshes, and the "
            "intelligence to route around the storm. Step 2 - reasoning "
            "path: at 200 meters even heavy rain costs only a few dB, "
            "well within massive-MIMO array gain; water-vapor "
            "absorption windows (around 140, 220, 340 GHz) offer "
            "kilometers of range in dry air. A mesh controller with "
            "learned rain-attenuation models predicts link quality "
            "minutes ahead from weather radar and reroutes proactively, "
            "treating weather as congestion. Step 3 - proposed "
            "mechanism: rooftop mesh nodes with 256-element arrays, "
            "electronic beam steering tracking sway and thermal drift, "
            "and a software-defined controller ingesting radar data to "
            "re-mesh before links degrade; fallback to millimeter-wave "
            "keeps the mesh alive when terahertz must yield. Step 4 - "
            "what would confirm it: a 20-node urban mesh sustaining 99.9 "
            "percent availability at 50 Gb/s per link through a full "
            "year including storm season, with logged rerouting events. "
            "Step 5 - what would kill it: array power consumption that "
            "erases the energy advantage, or tracking failures during "
            "gusts that drop links faster than rerouting recovers. What "
            "this does NOT claim: it does not promise kilometer mobile "
            "terahertz to handsets, does not defeat physics of water "
            "absorption, and does not claim 6G timelines - it proposes "
            "making fixed terahertz meshes weather-proof by "
            "architecture."),
        "citations": ["T. Kurner and S. Priebe, towards THz communications, "
                      "IEEE Transactions on Terahertz Science and "
                      "Technology 4, 2014",
                      "ITU-R P.676, atmospheric attenuation models",
                      "H. Elayan et al., terahertz communication survey, "
                      "IEEE Communications Surveys 22, 2020"],
    },
    {
        "key": "smes_economics",
        "name": "Superconducting Magnetic Energy Storage Economics",
        "group": "Power Systems",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("Can superconducting magnetic energy storage - the "
                    "fastest, most efficient storage physics known - ever "
                    "compete economically with batteries and other grid "
                    "storage?"),
        "background": ("SMES stores energy in the magnetic field of a "
                       "superconducting coil: round-trip efficiency above "
                       "95 percent, response in milliseconds, unlimited "
                       "cycle life - physically perfect for grid "
                       "stabilization. Demonstrators up to multi-megajoule "
                       "scale have worked since the 1980s. But "
                       "superconductor wire costs dollars per kiloamp-"
                       "meter, the cryogenics run forever, and energy "
                       "density is poor (the magnetic pressure needs "
                       "massive structure). Batteries won on cost per "
                       "kilowatt-hour by orders of magnitude, relegating "
                       "SMES to niche power-quality applications. The "
                       "economic question - not the physics - is what "
                       "remains unsolved."),
        "why_it_matters": ("A grid dominated by inverters needs "
                           "millisecond-scale stabilization that batteries "
                           "provide wastefully (cycling degrades them). "
                           "Economic SMES would be the perfect shock "
                           "absorber for the renewable grid: infinite "
                           "cycles, instant response, near-zero losses."),
        "sig_pointer": ("The Signature approach proposes SMES not as "
                        "bulk storage but as the grid's fastest muscle: "
                        "small units monetized purely on sub-second "
                        "frequency services, where batteries cannot "
                        "compete on lifetime cost."),
        "signature_solution": ("Step 1 - assumption: SMES will never win "
            "on dollars per kilowatt-hour, so it must win on dollars per "
            "kilowatt per million cycles - the metric where its physics "
            "is unbeatable. Step 2 - reasoning path: sub-second "
            "frequency response and synthetic inertia require thousands "
            "of shallow cycles per day; batteries doing this work "
            "degrade in years, while SMES cycles forever with 95 "
            "percent-plus efficiency. Valued as a 20-year frequency "
            "asset rather than an energy asset, the levelized cost "
            "crosses batteries. High-temperature superconductors at 20-"
            "30 K (cheaper cooling than 4 K) and modular factory-built "
            "coils attack the capital cost. Step 3 - proposed mechanism: "
            "a standardized 5-MW/20-MJ SMES module - MgB2 or HTS coil, "
            "conduction-cooled cryocooler, grid-forming inverter - sold "
            "with a 20-year service contract and stacked revenue from "
            "frequency regulation, synthetic inertia, and fault "
            "ride-through support. Step 4 - what would confirm it: a "
            "3-year grid deployment with audited levelized cost per MW "
            "of fast frequency response below the battery alternative "
            "over a 20-year horizon, with zero coil degradation. Step 5 "
            "- what would kill it: HTS wire prices that plateau above "
            "the crossover, or market rules that refuse to pay for "
            "sub-second services distinctly from slower reserves. What "
            "this does NOT claim: it does not claim SMES stores bulk "
            "energy economically, does not promise wire-price miracles, "
            "and does not ignore cryocooler maintenance - it proposes "
            "winning the fast-services niche on lifetime economics."),
        "citations": ["W. V. Hassenzahl et al., superconducting magnetic "
                      "energy storage, Proceedings of the IEEE 71, 1983",
                      "C. A. Luongo, superconducting storage systems "
                      "review, IEEE Transactions on Magnetics 32, 1996",
                      "DOE energy storage grand challenge, 2020"],
    },
    {
        "key": "backscatter_city",
        "name": "Ambient Backscatter Networks at City Scale",
        "group": "Wireless & RF",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("Can city-scale networks of battery-free backscatter "
                    "devices - communicating by reflecting existing radio "
                    "signals - achieve the reliability and density a "
                    "smart city needs?"),
        "background": ("Ambient backscatter lets devices communicate "
                       "without generating their own radio signal: they "
                       "modulate reflections of ambient TV, cellular, or "
                       "Wi-Fi transmissions, consuming microwatts. The "
                       "2013 UW demonstration sparked a field - "
                       "long-range backscatter (kilometers), "
                       "battery-free phones, and even underwater variants "
                       "followed. But scaling to city density hits hard "
                       "problems: the direct ambient signal drowns the "
                       "weak reflection (the near-far problem), "
                       "uncoordinated devices collide, and data rates "
                       "stay in kilobits per second. No city-scale "
                       "deployment has proven reliable, dense, "
                       "battery-free networking."),
        "why_it_matters": ("A trillion-sensor world cannot run on "
                           "batteries or spectrum-hungry radios. "
                           "Battery-free backscatter at city scale would "
                           "make ubiquitous sensing - infrastructure "
                           "health, air quality, logistics - essentially "
                           "free to deploy and eternal to operate."),
        "sig_pointer": ("The Signature approach proposes dedicated "
                        "illuminator infrastructure with coordinated "
                        "backscatter: a few powered illuminators plus "
                        "time-slotted reflections, turning the chaos of "
                        "ambient signals into an engineered network."),
        "signature_solution": ("Step 1 - assumption: pure ambient "
            "backscatter is too chaotic for city reliability, but a "
            "hybrid - a few dedicated illuminators providing a clean, "
            "coordinated carrier - keeps devices battery-free while "
            "making the network engineerable. Step 2 - reasoning path: "
            "the killer problems (near-far interference, collisions) "
            "are coordination problems; a scheduled protocol where the "
            "illuminator assigns time-frequency slots to tags converts "
            "the shared medium into an orderly one. Tags stay "
            "microwatt-simple (reflect, do not generate); all the "
            "smarts live in the powered infrastructure. Bistatic "
            "geometry - illuminator and receiver separated - further "
            "suppresses self-interference. Step 3 - proposed mechanism: "
            "rooftop illuminators every 500 meters broadcasting a "
            "dedicated 900-MHz carrier, tags with slot assignments "
            "distributed at manufacture plus over-the-air reconfiguration, "
            "and edge receivers doing successive interference "
            "cancellation to peel apart overlapping reflections. Step 4 "
            "- what would confirm it: a 10,000-tag district pilot with "
            "99 percent packet delivery, 5-year tag lifetimes with no "
            "maintenance, and per-tag cost under one dollar at volume. "
            "Step 5 - what would kill it: multipath in dense urban "
            "canyons that defeats the slot schedule, or illuminator "
            "deployment costs that exceed the value of the sensing "
            "data. What this does NOT claim: it does not promise "
            "broadband rates, does not work where illuminators cannot "
            "be deployed, and does not eliminate the need for some "
            "powered infrastructure - it proposes making the last "
            "trillion devices free."),
        "citations": ["V. Liu et al., ambient backscatter, SIGCOMM 2013",
                      "P. Zhang et al., hitchhike: long-range backscatter, "
                      "NSDI 2017",
                      "S. N. Daskalakis et al., backscatter survey, IEEE "
                      "Open Journal of Antennas and Propagation 2021"],
    },
    {
        "key": "noninvasive_bci",
        "name": "High-Bandwidth Noninvasive Brain-Computer Interfaces",
        "group": "Devices & Materials",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("Can brain-computer interfaces read and write neural "
                    "signals at high bandwidth without opening the skull?"),
        "background": ("Implanted electrode arrays achieve remarkable "
                       "bandwidth - hundreds of neurons, robotic arm "
                       "control, speech decoding - but require brain "
                       "surgery with scarring and risk. Noninvasive "
                       "methods (EEG, fNIRS, MEG) are safe but blurry: "
                       "the skull smears electrical signals, limiting "
                       "bandwidth to spelling devices and simple "
                       "commands. The frontier - focused ultrasound, "
                       "temporal interference stimulation, optically "
                       "pumped magnetometers, high-density EEG with "
                       "machine-learned decoding - is narrowing the gap, "
                       "but no noninvasive system approaches implanted "
                       "bandwidth, and the write direction (precise "
                       "stimulation without surgery) lags further."),
        "why_it_matters": ("Noninvasive high-bandwidth BCIs would bring "
                           "neural interfaces to millions: restoring "
                           "communication for locked-in patients without "
                           "surgery, treating neurological disorders with "
                           "precision, and eventually a new human-computer "
                           "interface as profound as the touchscreen."),
        "sig_pointer": ("The Signature approach proposes fusing weak "
                        "modalities: high-density EEG plus functional "
                        "ultrasound plus learned priors, with AI "
                        "decoders trained per-user, so the combination "
                        "exceeds any single noninvasive method."),
        "signature_solution": ("Step 1 - assumption: no single noninvasive "
            "modality will match implants, but independent weak "
            "measurements combine - EEG's millisecond timing plus "
            "ultrasound's millimeter spatial resolution plus a strong "
            "generative prior of what brains do - into something "
            "greater. Step 2 - reasoning path: the skull's smearing is "
            "a known, measurable transfer function; per-user "
            "calibration with a brief high-quality session (or even a "
            "single MRI) lets learned decoders invert it far better "
            "than generic algorithms. Functional ultrasound images "
            "blood-flow changes at 100-micron resolution through the "
            "skull window; fused with EEG timing, the pair localizes "
            "activity neither could alone. Step 3 - proposed mechanism: "
            "a headset combining 256-channel dry EEG, a sparse "
            "ultrasound array, and a per-user decoder trained in a "
            "one-hour calibration session, decoding attempted speech "
            "and fine motor intent; the write path uses temporal "
            "interference stimulation steered by the same head model. "
            "Step 4 - what would confirm it: locked-in users achieving "
            "60-plus words per minute attempted-speech decoding "
            "noninvasively in a registered clinical trial, sustained "
            "across sessions. Step 5 - what would kill it: "
            "inter-session variability that forces recalibration every "
            "use, or ultrasound resolution through intact skull that "
            "proves fundamentally worse than models predict. What this "
            "does NOT claim: it does not promise implant-level "
            "bandwidth, does not claim mind-reading of unconsented "
            "thoughts (decoders require cooperative calibration), and "
            "does not bypass medical safety review - it proposes "
            "fusing modalities past the single-method wall. Screened: "
            "civilian medical and assistive scope only."),
        "citations": ["J. R. Wolpaw et al., brain-computer interfaces "
                      "review, Nature Reviews Neuroscience 2002",
                      "F. Willett et al., high-performance speech "
                      "neuroprosthesis, Nature 620, 2023",
                      "N. Grossman et al., temporal interference "
                      "stimulation, Cell 169, 2017"],
    },
    {
        "key": "picosecond_power_delivery",
        "name": "Picosecond Power Delivery Networks on Chip",
        "group": "Computing Hardware",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("How can chips deliver clean power to billions of "
                    "transistors switching in picoseconds, as voltages "
                    "fall below half a volt and currents spike ever "
                    "faster?"),
        "background": ("Every switching transistor gulps current, and "
                       "billions switching together create violent "
                       "current transients - di/dt noise that droops "
                       "the supply voltage and causes timing errors. As "
                       "supply voltages fall toward 0.5 V, the tolerable "
                       "droop shrinks to tens of millivolts while "
                       "currents rise. Traditional power delivery - "
                       "board capacitors, package planes, on-die grids - "
                       "is running out of headroom: inductance in the "
                       "path cannot be reduced further by geometry "
                       "alone. Integrated voltage regulators, on-chip "
                       "magnetic inductors, and switched-capacitor "
                       "converters help, but efficiency at the required "
                       "conversion ratios and densities remains poor, "
                       "and the problem compounds with 3D stacking."),
        "why_it_matters": ("Power integrity is the silent limiter of "
                           "chip performance: architects leave "
                           "performance on the table as voltage guard "
                           "bands against droop. Solving delivery "
                           "unlocks that margin across every processor "
                           "shipped - a free performance gain for the "
                           "whole industry."),
        "sig_pointer": ("The Signature approach proposes granular "
                        "power: hundreds of tiny on-chip regulators "
                        "with a fast digital control loop that "
                        "anticipates current spikes from the "
                        "instruction stream, delivering power where "
                        "and when the switching happens."),
        "signature_solution": ("Step 1 - assumption: the inductance "
            "problem is a distance problem - power must be regulated "
            "within microns of the load, not millimeters away, because "
            "at picosecond timescales even bond wires look like open "
            "circuits. Step 2 - reasoning path: a processor's current "
            "demand is largely predictable - the instruction stream "
            "tells the power controller what the execution units will "
            "do next. Feed-forward control, where the regulator "
            "pre-charges before the spike arrives, beats any feedback "
            "loop fighting inductance after the fact. Hundreds of "
            "switched-capacitor regulators tile the die, each serving "
            "a small region, so no current travels far. Step 3 - "
            "proposed mechanism: per-core-region integrated regulators "
            "with a lookahead controller snooping the instruction "
            "fetch queue, deep-trench on-die capacitors as local "
            "charge reservoirs, and a slow outer loop trimming for "
            "process variation; the power grid becomes an active "
            "network, not a passive mesh. Step 4 - what would confirm "
            "it: a test chip showing sub-20-mV droop under worst-case "
            "di/dt at 0.5-V supply with regulator efficiency above 85 "
            "percent and area overhead under 10 percent. Step 5 - what "
            "would kill it: switching noise from hundreds of "
            "regulators coupling into sensitive circuits worse than "
            "the droop it fixes, or lookahead prediction accuracy too "
            "low on irregular workloads. What this does NOT claim: it "
            "does not repeal inductance, does not promise zero "
            "guard bands, and does not solve 3D-stack thermal "
            "coupling - it proposes moving regulation to the point "
            "of load with prediction."),
        "citations": ["P. Hazucha et al., area-efficient integrated "
                      "switched-capacitor DC-DC converter, IEEE JSSC 40, "
                      "2005",
                      "S. Sanders et al., fully integrated voltage "
                      "regulators, IEEE Transactions on Power Electronics "
                      "2016",
                      "IRDS, power delivery roadmap, 2023"],
    },
    {
        "key": "self_healing_grid",
        "name": "Self-Healing Autonomous Power Grids",
        "group": "Power Systems",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("Can power grids detect, isolate, and recover from "
                    "faults and attacks autonomously - healing in "
                    "seconds without human operators?"),
        "background": ("Today's grid heals slowly and manually: fault "
                       "crews drive to substations, operators reclose "
                       "breakers by procedure, and restoration after "
                       "major storms takes days. Meanwhile the grid "
                       "grows more complex - millions of inverters, "
                       "bidirectional flows, cyber-attack surfaces - "
                       "while operator staffing shrinks. "
                       "Self-healing concepts (fault location, isolation, "
                       "and service restoration - FLISR) exist in "
                       "advanced distribution management systems, but "
                       "they handle simple radial faults; meshed "
                       "transmission behavior, cascading failures, and "
                       "adversarial events still need humans. True "
                       "autonomy - a grid that reconfigures itself "
                       "faster than cascades propagate - remains "
                       "unsolved, partly because operators (rightly) "
                       "distrust handing the keys to software."),
        "why_it_matters": ("Outages cost economies billions and lives "
                           "during extreme weather; autonomous healing "
                           "compresses restoration from days to seconds "
                           "for most faults. It is also the only way to "
                           "operate a future grid too complex for human "
                           "operators to fully comprehend in real time."),
        "sig_pointer": ("The Signature approach proposes healing by "
                        "pre-computed playbook: the grid's digital twin "
                        "rehearses millions of fault scenarios nightly, "
                        "so when a real fault strikes the autonomous "
                        "agent executes a validated playbook in "
                        "milliseconds instead of improvising."),
        "signature_solution": ("Step 1 - assumption: real-time "
            "improvisation during a cascade is too slow and too risky; "
            "the winning strategy is pre-computation - rehearse the "
            "disaster before it happens, then execute the rehearsed "
            "plan. Step 2 - reasoning path: a high-fidelity digital "
            "twin fed by PMU and SCADA data can simulate millions of "
            "fault-and-attack scenarios overnight on a compute cluster, "
            "distilling each into a verified switching playbook with "
            "proven stability margins. At fault time the autonomous "
            "agent matches the observed signature to a playbook and "
            "executes - no online optimization, no improvisation, "
            "millisecond response. Human operators supervise at the "
            "policy level and can always interdict. Step 3 - proposed "
            "mechanism: a three-tier system - local agents executing "
            "playbooks at substations, a regional coordinator "
            "resolving conflicts between playbooks, and the nightly "
            "twin that regenerates the playbook library; every "
            "execution is logged against the twin's prediction for "
            "continuous validation. Step 4 - what would confirm it: a "
            "utility pilot where the autonomous system clears 95 "
            "percent of distribution faults without human intervention, "
            "with SAIDI/SAIFI improving 40 percent and zero "
            "playbook-caused cascading events over 2 years. Step 5 - "
            "what would kill it: twin-model mismatch that makes "
            "playbooks wrong in unmodeled conditions, or a "
            "cyber-compromise of the playbook pipeline that turns the "
            "healer into the attacker. What this does NOT claim: it "
            "does not remove human operators, does not promise "
            "immunity to physical destruction, and does not claim the "
            "twin is ever complete - it proposes rehearsed response "
            "instead of real-time improvisation."),
        "citations": ["U.S. DOE, Grid Modernization Initiative and "
                      "self-healing grid concepts, 2016",
                      "IEEE 1547-2018 and IEEE 2030.7, microgrid "
                      "controllers",
                      "NERC, cascading outage analyses, ongoing"],
    },
    {
        "key": "reversible_logic_landauer",
        "name": "Reversible Logic at Scale Below the Landauer Limit",
        "group": "Computing Hardware",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("Can computers be built from reversible logic that "
                    "dodges the Landauer limit - the fundamental minimum "
                    "energy per erased bit - at a scale that matters?"),
        "background": ("Rolf Landauer showed in 1961 that erasing a bit "
                       "of information must dissipate at least kT ln 2 "
                       "of energy - a fundamental thermodynamic floor. "
                       "Charles Bennett then showed reversible computing "
                       "could, in principle, dodge it: never erase, just "
                       "uncompute. Reversible logic families exist - "
                       "adiabatic CMOS, superconducting nSQUIDs, "
                       "nanomagnetic logic - and lab demos confirm "
                       "sub-Landauer operation per device. But scaling "
                       "to systems hits walls: reversible architectures "
                       "need to keep every intermediate result (memory "
                       "explosion), adiabatic clocks are slow and lossy "
                       "in practice, and no reversible processor has "
                       "computed anything useful at competitive speed. "
                       "The limit looms as devices approach it; the "
                       "escape route is proven in principle but not in "
                       "practice."),
        "why_it_matters": ("As transistors approach the Landauer floor, "
                           "reversible computing is the only known "
                           "physics that lets computation continue "
                           "getting more efficient indefinitely. It is "
                           "the long-term answer to computing's energy "
                           "crisis - if it can ever be engineered."),
        "sig_pointer": ("The Signature approach proposes reversible "
                        "accelerators for naturally reversible workloads "
                        "(cryptography, signal transforms, simulation "
                        "checkpoints), where uncomputation is cheap and "
                        "the memory overhead stays bounded."),
        "signature_solution": ("Step 1 - assumption: full reversible "
            "general-purpose computing is decades away, but workloads "
            "that are already logically reversible - or can be made so "
            "cheaply - can exploit reversible hardware today without "
            "the memory explosion. Step 2 - reasoning path: many "
            "important kernels (FFT butterflies, cryptographic rounds, "
            "N-body force pipelines) compute a function and then need "
            "only the result; Bennett's uncompute trick reclaims the "
            "scratch space with modest overhead when the function is "
            "structured. An accelerator that runs these kernels "
            "adiabatically - ramping clocks slowly to approach "
            "thermodynamic reversibility - beats the Landauer floor "
            "where it counts, in the datacenter's hottest loops. Step 3 "
            "- proposed mechanism: a PCIe reversible accelerator with "
            "adiabatic CMOS datapaths, a compiler that identifies "
            "reversible regions in standard code and maps them to the "
            "accelerator, and on-chip energy recovery (recycling clock "
            "energy instead of dumping it). Step 4 - what would confirm "
            "it: measured energy per FFT below 0.1 kT ln 2 per "
            "effective bit-erasure-equivalent on a real workload, with "
            "throughput within 3x of the CMOS baseline. Step 5 - what "
            "would kill it: adiabatic clock distribution losses that "
            "exceed the recovered energy at practical speeds, or "
            "compiler coverage too narrow to matter. What this does NOT "
            "claim: it does not claim to beat Landauer for irreversible "
            "workloads, does not promise general-purpose reversible "
            "CPUs, and does not ignore the speed penalty of adiabatic "
            "operation - it proposes winning the reversible-shaped "
            "workloads first."),
        "citations": ["R. Landauer, irreversibility and heat generation, "
                      "IBM Journal of Research and Development 5, 1961",
                      "C. H. Bennett, logical reversibility of "
                      "computation, IBM JRD 17, 1973",
                      "M. P. Frank, introduction to reversible computing, "
                      "Computing Frontiers 2020"],
    },
    {
        "key": "antenna_chu_limit",
        "name": "Beating the Fundamental Antenna Size Limit",
        "group": "Wireless & RF",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Can electrically small antennas escape the Chu "
                    "limit - the fundamental bound linking antenna size, "
                    "bandwidth, and efficiency - through new physics?"),
        "background": ("In 1948 L. J. Chu proved that an antenna small "
                       "compared to the wavelength must be narrowband, "
                       "inefficient, or both: the Q factor grows as the "
                       "cube of the inverse size. Every phone, wearable, "
                       "and IoT device fights this limit - small "
                       "antennas that work across wide bands with good "
                       "efficiency should not exist, yet products demand "
                       "them. Workarounds abound: non-Foster matching "
                       "(active circuits that cancel reactance), "
                       "magneto-dielectric loading, characteristic-mode "
                       "design using the whole device chassis as the "
                       "antenna. Each buys a little, none breaks the "
                       "limit, because the limit is a theorem about "
                       "passive, linear, time-invariant systems - and "
                       "breaking it means leaving one of those "
                       "assumptions behind."),
        "why_it_matters": ("Everything wireless keeps shrinking while "
                           "bands keep widening: wearables, implants, "
                           "smart dust. Escaping the size-bandwidth-"
                           "efficiency triangle would unblock antenna "
                           "design for the next fifty years of "
                           "miniaturization."),
        "sig_pointer": ("The Signature approach proposes leaving the "
                        "theorem's assumptions: time-varying and "
                        "nonlinear matching networks that pump the "
                        "antenna parametrically, trading a little DC "
                        "power for bandwidth the passive limit forbids."),
        "signature_solution": ("Step 1 - assumption: the Chu limit binds "
            "only passive, linear, time-invariant antennas, so the "
            "escape is active, nonlinear, or time-varying matching - "
            "physics the theorem never constrained. Step 2 - reasoning "
            "path: a parametric matching network - a varactor pumped at "
            "twice the signal frequency - can present a negative "
            "resistance that cancels the antenna's reactance over a "
            "wide band, effectively widening bandwidth at the cost of "
            "pump power and added noise. Non-Foster circuits (negative "
            "capacitors/inductors) do the same statically but risk "
            "instability; parametric pumping is inherently stable when "
            "designed below oscillation threshold. The trade - DC "
            "power and noise figure for bandwidth - favors receive "
            "applications and short-range IoT. Step 3 - proposed "
            "mechanism: an antenna module pairing an electrically small "
            "element (ka < 0.5) with an integrated parametric matching "
            "IC, pump derived from the device's own clock tree, and "
            "adaptive tuning that tracks detuning from the user's hand; "
            "a link-budget calculator in firmware decides per-packet "
            "whether the pump is worth its power. Step 4 - what would "
            "confirm it: a module demonstrating 5x the bandwidth-"
            "efficiency product of its passive Chu-limited baseline at "
            "equal size, with noise figure degradation under 2 dB and "
            "unconditional stability proven across temperature. Step 5 - "
            "what would kill it: pump phase noise that ruins the noise "
            "figure, or power consumption that exceeds what the radio "
            "saves. What this does NOT claim: it does not repeal the "
            "Chu theorem (it sidesteps its assumptions), does not "
            "promise free bandwidth, and does not suit high-power "
            "transmit - it proposes buying bandwidth with a little "
            "pump power where that trade wins."),
        "citations": ["L. J. Chu, physical limitations of omni-directional "
                      "antennas, Journal of Applied Physics 19, 1948",
                      "S. E. Sussman-Fort and R. M. Rudish, non-Foster "
                      "impedance matching, IEEE Antennas and Propagation "
                      "Magazine 51, 2009",
                      "D. F. Sievenpiper, parametric antenna matching, "
                      "ongoing research"],
    },
    {
        "key": "room_temp_photon_detector",
        "name": "Room-Temperature Single-Photon Detectors",
        "group": "Quantum Electronics",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("Can single photons - the carriers of quantum "
                    "communication - be detected efficiently at room "
                    "temperature, without cryogenic superconducting "
                    "detectors?"),
        "background": ("Superconducting nanowire single-photon detectors "
                       "(SNSPDs) are magnificent: 95 percent-plus "
                       "efficiency, picosecond timing, nearly no dark "
                       "counts - but they need cooling below 4 K. That "
                       "cryogenic tax confines quantum communication to "
                       "labs and specialized nodes. Room-temperature "
                       "alternatives exist - InGaAs avalanche photodiodes "
                       "at telecom wavelengths suffer high dark counts "
                       "and afterpulsing; silicon SPADs work in the "
                       "visible but not at fiber wavelengths; "
                       "upconversion detectors add complexity and noise. "
                       "Quantum key distribution over real fiber networks "
                       "waits on a detector that is efficient, quiet, "
                       "fast, and warm."),
        "why_it_matters": ("The quantum internet needs detectors "
                           "everywhere - in every network node, data "
                           "center, and eventually device. Cryogenics at "
                           "every node makes that economically absurd; a "
                           "warm, efficient detector makes quantum "
                           "communication deployable like classical "
                           "optics."),
        "sig_pointer": ("The Signature approach proposes waveguide-"
                        "integrated avalanche detectors with "
                        "machine-learned afterpulse cancellation: accept "
                        "the noisy device physics, then clean the signal "
                        "computationally in real time."),
        "signature_solution": ("Step 1 - assumption: the device physics "
            "of warm detectors will stay noisier than SNSPDs, so the "
            "win must come from the system - better photon delivery to "
            "the detector plus computational cleanup of its flaws. Step "
            "2 - reasoning path: waveguide integration boosts absorption "
            "efficiency (the photon travels alongside the detector "
            "instead of through it); gated operation with "
            "self-differencing circuits suppresses capacitive "
            "transients; and afterpulsing - the dominant warm-detector "
            "flaw - is a statistically characterizable process that a "
            "real-time estimator can model and subtract, the way noise "
            "cancellation works in audio. Step 3 - proposed mechanism: "
            "an InGaAs/InP SPAD array waveguide-coupled on a photonic "
            "chip, thermoelectrically cooled to -40 C (no cryogen), "
            "with per-pixel afterpulse characterization at manufacture "
            "and a firmware estimator that weights each detection event "
            "by its computed validity; suspect events are flagged, not "
            "trusted. Step 4 - what would confirm it: 50 percent "
            "system detection efficiency at 1550 nm with dark counts "
            "under 100 Hz and timing jitter under 100 ps, sustained in "
            "a field QKD trial over 50 km of fiber with key rates "
            "within 2x of the SNSPD baseline. Step 5 - what would kill "
            "it: afterpulse correlations that prove unlearnable at "
            "high count rates, or waveguide coupling losses that cap "
            "efficiency below 30 percent. What this does NOT claim: it "
            "does not claim parity with cryogenic detectors, does not "
            "promise to work at full daylight free-space rates yet, "
            "and does not remove the need for better materials - it "
            "proposes making warm detectors good enough to deploy."),
        "citations": ["R. H. Hadfield, single-photon detectors review, "
                      "Nature Photonics 3, 2009",
                      "M. D. Eisaman et al., single-photon sources and "
                      "detectors review, Review of Scientific Instruments "
                      "82, 2011",
                      "Z. Yan et al., waveguide SPADs, ongoing"],
    },
    {
        "key": "million_qubit_wiring",
        "name": "Million-Qubit Wiring and Control",
        "group": "Quantum Electronics",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("How can a million qubits each be wired, controlled, "
                    "and read out when today's machines struggle with "
                    "hundreds of cables into a cryostat?"),
        "background": ("Every qubit needs control lines: microwave "
                       "pulses to operate it, flux biases to tune it, "
                       "readout resonators to measure it. A 100-qubit "
                       "chip already needs hundreds of coaxial cables "
                       "snaking into a dilution refrigerator, each "
                       "leaking heat and costing thousands of dollars. "
                       "Extrapolate to a million qubits and the wiring "
                       "alone is physically impossible - the cryostat "
                       "would be all cable. The field's answers so far: "
                       "cryogenic multiplexing, single-flux-quantum "
                       "control logic at 4 K, photonic readout, and "
                       "architectures needing fewer control lines per "
                       "qubit. None has demonstrated the thousand-fold "
                       "reduction in wires-per-qubit that million-qubit "
                       "machines require."),
        "why_it_matters": ("Fault-tolerant quantum computing needs "
                           "millions of physical qubits; the wiring "
                           "problem is the most mundane and most "
                           "blocking obstacle on that road. Solving it "
                           "turns quantum computers from physics "
                           "experiments into engineered systems."),
        "sig_pointer": ("The Signature approach proposes a control "
                        "hierarchy mirroring classical memory: row-column "
                        "addressing with on-chip cryogenic demultiplexers, "
                        "so wires scale as the square root of qubit "
                        "count, not linearly."),
        "signature_solution": ("Step 1 - assumption: one wire per qubit "
            "is the wrong architecture, full stop - classical DRAM "
            "solved the analogous problem fifty years ago with "
            "row-column addressing, and quantum control must learn "
            "the same lesson. Step 2 - reasoning path: qubits are "
            "operated in calibrated pulses; a cryogenic demultiplexer "
            "at the mixing-chamber stage can route one high-bandwidth "
            "line to any of 1,000 qubits addressed by slow digital "
            "select lines - wires scale as 2*sqrt(N) instead of N. "
            "Readout multiplexes similarly through frequency-division: "
            "hundreds of resonators on one feedline, already routine. "
            "The price is serialization - qubits addressed sequentially "
            "- which error correction can tolerate if the addressing "
            "is fast enough. Step 3 - proposed mechanism: a three-tier "
            "control stack - room-temperature arbitrary waveform "
            "generators, a 4-K single-flux-quantum routing fabric, and "
            "millikelvin demultiplexer chiplets flip-chipped to the "
            "qubit die; a compiler schedules gates through the "
            "addressing fabric the way DRAM controllers schedule "
            "accesses. Step 4 - what would confirm it: a 10,000-qubit "
            "test vehicle with fewer than 500 wires into the cryostat, "
            "demonstrating simultaneous randomized benchmarking with "
            "crosstalk below the fault-tolerance threshold. Step 5 - "
            "what would kill it: demultiplexer switching transients "
            "that decohere neighboring qubits, or addressing latency "
            "that stretches error-correction cycles past coherence "
            "times. What this does NOT claim: it does not solve qubit "
            "quality itself, does not promise million-qubit coherence, "
            "and does not remove the need for better qubits - it "
            "proposes making the wiring scale sublinearly so the "
            "qubits get their chance."),
        "citations": ["F. Arute et al., quantum supremacy using a "
                      "programmable superconducting processor, Nature "
                      "574, 2019",
                      "J. M. Martinis, control challenges review, "
                      "npj Quantum Information 2021",
                      "Intel Horse Ridge cryogenic control chip, 2019"],
    },
]

assert len(ENTRIES) == 34, "need exactly 34 entries"
assert [e["ladder_rank"] for e in ENTRIES] == list(range(1, 35))
assert len({e["key"] for e in ENTRIES}) == 34
for e in ENTRIES:
    assert "'" not in e["name"], "apostrophe in title: %s" % e["name"]
