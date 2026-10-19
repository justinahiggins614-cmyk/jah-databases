#!/usr/bin/env python3
"""Entries for the Quantum Computing Network databases (Manon's 2026-10-17
17:55 order - quantum COMPUTING network database; he corrected his own
"quuaputung" typo himself).

Terminology fact-checked 2026-10-17 against: Kimble HJ. "The quantum
internet." Nature 453, 1023-1030 (2008); Wehner S, Elkouss D, Hanson R.
"Quantum internet: A vision for the road ahead." Science 362, eaam9288
(2018) - the six stages (trusted repeater networks, prepare-and-measure
networks, entanglement distribution networks, quantum memory networks,
fault-tolerant few-qubit networks, full quantum internet); Bennett CH,
Brassard G. "Quantum cryptography: Public key distribution and coin
tossing." Proc. IEEE Int. Conf. on Computers, Systems and Signal
Processing, Bangalore (1984); Ekert AK. "Quantum cryptography based on
Bell's theorem." Phys. Rev. Lett. 67, 661-663 (1991); Bennett CH et al.
"Teleporting an unknown quantum state via dual classical and
Einstein-Podolsky-Rosen channels." Phys. Rev. Lett. 70, 1895-1899 (1993)
- 1 ebit plus 2 classical bits per teleported qubit; Wootters WK, Zurek
WH. "A single quantum cannot be cloned." Nature 299, 802-803 (1982);
optimal universal 1-to-2 cloning fidelity 5/6 (Buzek-Hillery 1996);
Briegel HJ, Duer W, Cirac JI, Zoller P. "Quantum repeaters: The role of
imperfect local operations in quantum communication." Phys. Rev. Lett.
81, 5932-5935 (1998); Duan LM, Lukin MD, Cirac JI, Zoller P.
"Long-distance quantum communication with atomic ensembles and linear
optics." Nature 414, 413-418 (2001) - the DLCZ protocol; Yin J et al.
"Satellite-based entanglement distribution over 1200 kilometers."
Science 356, 1140-1144 (2017); Liao SK et al. "Satellite-to-ground
quantum key distribution." Nature 549, 43-47 (2017); Bennett CH et al.
"Purification of noisy entanglement and faithful teleportation via noisy
channels." Phys. Rev. Lett. 76, 722-725 (1996); Deutsch D et al.
"Quantum privacy amplification and the security of quantum cryptography
over noisy channels." Phys. Rev. Lett. 77, 2818-2821 (1996) - DEJMPS;
linear-optics Bell-state measurement ceiling of one half; fiber loss
about 0.2 dB per km at 1550 nm with light speed in fiber near
2.0e8 m/s; Pirandola S et al. "Advances in quantum cryptography." Adv.
Opt. Photon. 12, 1012-1236 (2020); ETSI GS QKD series (key management
control interface); ITU-T Y.3800-Y.3860 series (QKD network framework);
IETF Quantum Internet Research Group (QIRG) architectural drafts;
Dahlberg A et al. "A link layer protocol for quantum networks." Proc.
ACM SIGCOMM 2019; Caleffi M, Cacciapuoti AS, Bianchi G. "Quantum
internet: from communication to distributed computing." Proc. ACM
NANOCOM 2018; Kozlowski W, Wehner S. "Towards large-scale quantum
networks." Proc. ACM NANOCOM 2019; Broadbent A, Fitzsimons J, Kashefi E.
"Universal blind quantum computation." Proc. IEEE FOCS 2009, 517-526;
Giovannetti V, Lloyd S, Maccone L. "Advances in quantum metrology."
Nature Photon. 5, 222-229 (2011) - Heisenberg 1/N scaling versus the
standard quantum limit 1/sqrt(N); Eisert J et al. "Optimal local
implementation of nonlocal quantum gates." Phys. Rev. A 62, 052317
(2000) - distributed CNOT costs one ebit plus two classical bits each
way; Van Meter R. Quantum Networking. Wiley; 2014.

Creates two NEW databases, 34 ladder-ordered records each:

  quantum-computing-network        - The Quantum Computing Network
                                     Database (public-harvest: real,
                                     fact-checked quantum networking -
                                     quantum internet, distributed
                                     quantum computing, entanglement
                                     distribution, quantum repeaters,
                                     QKD networks, protocols, topologies,
                                     memory nodes, swapping,
                                     teleportation networking, network
                                     stacks; the NETWORK layer only,
                                     ladder-ordered basics to advanced)
  quantum-computing-network-signature - The Quantum Computing Network
                                     Signature Database (his original
                                     Signature network designs and
                                     protocols; src signature, titles
                                     suffixed " (Signature Edition)",
                                     clearly labeled Signature-made,
                                     never presented as authentic public
                                     record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-QCN- (public) and JAH-QCNS- (signature), verified free:
zero hits across ALL data/manifest.json id_prefix values and zero hits
across all record IDs in ~/workspace/jah-databases-data-1/data/ (checked
2026-10-17). Distinct from the existing quantum-computing DB (JAH-QUANT,
general quantum computing) - all 98 of its record titles checked, zero
overlap with these 68 network-layer titles; also checked the quantum DB
(JAH-QNT-) network-adjacent titles (only "Algorithm: Quantum
teleportation" and "Quantum Key Distribution (QKD) Sifted Bitstreams"
exist there - both avoided by distinct phrasing here).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_quantum_computing_network.py). Every demo prints its
real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos before writing pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/quantum-computing-network*/,
code/quantum-computing-network-build, the shard data dirs, and the
fragment file are written.

No website references. No Facebook.

SCREENING: public networking knowledge plus his Signature network
designs only - nothing hate-adjacent, profane, or inappropriate; no
religious talk; nothing on neutralizing or defeating military or
defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature network design: "
            "clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_KIMBLE = ("Kimble HJ. The quantum internet. Nature 453, 1023-1030 "
              "(2008).")
CIT_WEHNER = ("Wehner S, Elkouss D, Hanson R. Quantum internet: A vision "
              "for the road ahead. Science 362, eaam9288 (2018).")
CIT_BB84 = ("Bennett CH, Brassard G. Quantum cryptography: Public key "
            "distribution and coin tossing. Proc. IEEE Int. Conf. on "
            "Computers, Systems and Signal Processing, Bangalore (1984).")
CIT_E91 = ("Ekert AK. Quantum cryptography based on Bell's theorem. "
           "Phys. Rev. Lett. 67, 661-663 (1991).")
CIT_TELEPORT = ("Bennett CH, Brassard G, Crepeau C, Jozsa R, Peres A, "
                "Wootters WK. Teleporting an unknown quantum state via "
                "dual classical and Einstein-Podolsky-Rosen channels. "
                "Phys. Rev. Lett. 70, 1895-1899 (1993).")
CIT_NOCLONE = ("Wootters WK, Zurek WH. A single quantum cannot be cloned. "
               "Nature 299, 802-803 (1982).")
CIT_REPEATER = ("Briegel HJ, Duer W, Cirac JI, Zoller P. Quantum repeaters: "
                "The role of imperfect local operations in quantum "
                "communication. Phys. Rev. Lett. 81, 5932-5935 (1998).")
CIT_DLCZ = ("Duan LM, Lukin MD, Cirac JI, Zoller P. Long-distance quantum "
            "communication with atomic ensembles and linear optics. "
            "Nature 414, 413-418 (2001).")
CIT_MICIUS_ENT = ("Yin J et al. Satellite-based entanglement distribution "
                  "over 1200 kilometers. Science 356, 1140-1144 (2017).")
CIT_MICIUS_QKD = ("Liao SK et al. Satellite-to-ground quantum key "
                  "distribution. Nature 549, 43-47 (2017).")
CIT_PURIFY = ("Bennett CH et al. Purification of noisy entanglement and "
              "faithful teleportation via noisy channels. Phys. Rev. Lett. "
              "76, 722-725 (1996).")
CIT_DEJMPS = ("Deutsch D et al. Quantum privacy amplification and the "
              "security of quantum cryptography over noisy channels. "
              "Phys. Rev. Lett. 77, 2818-2821 (1996).")
CIT_PIRANDOLA = ("Pirandola S et al. Advances in quantum cryptography. "
                 "Adv. Opt. Photon. 12, 1012-1236 (2020).")
CIT_ETSI = ("ETSI GS QKD series. Quantum Key Distribution; Control "
            "Interface for Key Management System (QKD 015).")
CIT_ITU = ("ITU-T Y.3800-Y.3860 series. Quantum key distribution networks: "
           "framework and requirements.")
CIT_QIRG = ("IETF Quantum Internet Research Group (QIRG). Architectural "
            "principles and protocol drafts; accessed 2026-10-17.")
CIT_VANMETER = ("Van Meter R. Quantum Networking. Wiley; 2014.")
CIT_DAHLBERG = ("Dahlberg A et al. A link layer protocol for quantum "
                "networks. Proc. ACM SIGCOMM 2019.")
CIT_CALEFFI = ("Caleffi M, Cacciapuoti AS, Bianchi G. Quantum internet: "
               "from communication to distributed computing. Proc. ACM "
               "NANOCOM 2018.")
CIT_KOZLOWSKI = ("Kozlowski W, Wehner S. Towards large-scale quantum "
                 "networks. Proc. ACM NANOCOM 2019.")
CIT_BLIND = ("Broadbent A, Fitzsimons J, Kashefi E. Universal blind "
             "quantum computation. Proc. IEEE FOCS 2009, 517-526.")
CIT_SENSOR = ("Giovannetti V, Lloyd S, Maccone L. Advances in quantum "
              "metrology. Nature Photon. 5, 222-229 (2011).")
CIT_DISTGATE = ("Eisert J, Jacobs K, Papadopoulos P, Plenio MB. Optimal "
                "local implementation of nonlocal quantum gates. Phys. "
                "Rev. A 62, 052317 (2000).")
CIT_WIKI_QNET = ("Wikipedia contributors. Quantum network. Wikipedia, The "
                 "Free Encyclopedia; accessed 2026-10-17.")
CIT_WIKI_QKD = ("Wikipedia contributors. Quantum key distribution. "
                "Wikipedia, The Free Encyclopedia; accessed 2026-10-17.")
CIT_WIKI_QREP = ("Wikipedia contributors. Quantum repeater. Wikipedia, "
                 "The Free Encyclopedia; accessed 2026-10-17.")
CIT_WIKI_QINT = ("Wikipedia contributors. Quantum internet. Wikipedia, "
                 "The Free Encyclopedia; accessed 2026-10-17.")
CIT_WIKI_TELE = ("Wikipedia contributors. Quantum teleportation. "
                 "Wikipedia, The Free Encyclopedia; accessed 2026-10-17.")

ENTRIES = [
    {
        "key": "qcn-what-is",
        "name": "What a Quantum Network Is",
        "group": "Network Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A quantum network connects distant quantum devices - quantum "
            "computers, sensors, and cryptographic terminals - with links "
            "that carry quantum states, not just classical bits. Where the "
            "classical internet moves copies of data, a quantum network "
            "moves entanglement: pairs of particles whose outcomes stay "
            "correlated no matter the distance. That entanglement is the "
            "network's fundamental resource, and everything the network "
            "does - teleporting qubits, distributing secret keys, linking "
            "processors, synchronizing sensors - is built on creating, "
            "storing, purifying, and consuming it. A quantum network always "
            "runs beside a classical network, because every quantum "
            "operation needs classical messages (measurement results, "
            "heralding signals, routing instructions) to complete."
        ),
        "how_it_works": (
            "Step 1: two neighboring nodes create shared entanglement, "
            "usually by sending photons through fiber or free space and "
            "detecting them. Step 2: the nodes verify the entanglement "
            "quality with measurements exchanged over the classical "
            "channel. Step 3: the network chains short entangled links "
            "into long ones with entanglement swapping at intermediate "
            "nodes. Step 4: applications consume the entanglement - a "
            "teleportation moves a qubit from one processor to another, a "
            "QKD session turns it into a secret key, a distributed "
            "computation uses it to run gates across machines. Step 5: the "
            "classical control plane coordinates every step, because "
            "quantum operations are probabilistic and need heralding."
        ),
        "key_points": [
            "Links carry quantum states; entanglement is the core resource",
            "Always paired with a classical network for control messages",
            "Applications: teleportation, QKD, distributed computing, sensing",
            "Entanglement is created locally, then extended by swapping",
            "Every quantum step is heralded - success must be confirmed classically",
            "The network layer is distinct from the quantum computers it connects",
        ],
        "requirements": [
            "Nodes able to create, store, and measure entangled qubits",
            "A parallel classical network with low-latency messaging",
            "Photon links (fiber or free-space) between neighbors",
        ],
        "standards": [
            "Wehner et al. six-stage roadmap defines what counts as each network generation",
            "ITU-T Y.3800 series frames QKD network architecture",
            "IETF QIRG drafts define quantum network architecture vocabulary",
        ],
        "citations": [CIT_KIMBLE, CIT_WEHNER, CIT_WIKI_QNET],
        "sig_lens": (
            "His Signature reading of the quantum network: the Signature "
            "system treats entanglement the way it treats a signature - a "
            "bond between distant points that no copy can fake, carried on "
            "his own network designs where every link is a covenant line."
        ),
    },
    {
        "key": "qcn-flying-qubits",
        "name": "Flying Qubits: Photons on the Wire",
        "group": "Network Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Quantum information travels between nodes on flying qubits - "
            "almost always photons, because they move at light speed, "
            "barely interact with their surroundings, and already have a "
            "global fiber infrastructure to ride on. A stationary qubit "
            "(a trapped ion, a superconducting circuit, an atomic ensemble) "
            "holds the information at a node; a flying qubit carries it "
            "between nodes. The qubit is encoded in a photon's degree of "
            "freedom: polarization (horizontal vs vertical), time-bin "
            "(early vs late arrival), or path. Telecom wavelengths near "
            "1550 nanometers are preferred because standard fiber loses "
            "only about 0.2 dB per kilometer there - the difference between "
            "a link that works and one that does not."
        ),
        "how_it_works": (
            "Step 1: pick the encoding - polarization is simple but drifts "
            "in fiber; time-bin is stable but needs interferometers. Step 2: "
            "generate the photon at the telecom wavelength so fiber loss "
            "stays near 0.2 dB/km. Step 3: launch it into fiber, where it "
            "travels at about two-thirds light speed (roughly 2.0e8 m/s). "
            "Step 4: at the receiver, detect the photon with a "
            "single-photon detector and read the encoded degree of "
            "freedom. Step 5: for entanglement distribution, detect photons "
            "from two sources in a Bell-state measurement, which heralds "
            "that the distant stationary qubits are now entangled."
        ),
        "key_points": [
            "Photons are the flying qubits; matter qubits are the stationary ones",
            "Polarization, time-bin, and path encodings each suit different links",
            "1550 nm telecom band: about 0.2 dB/km fiber loss",
            "Light in fiber travels near 2.0e8 m/s - latency is distance times five microseconds per km",
            "Every photon lost is a failed attempt; links are probabilistic",
            "Encoding choice trades simplicity against stability in real fiber",
        ],
        "requirements": [
            "Photon sources at low-loss wavelengths matched to the fiber plant",
            "Single-photon detectors at each receiving node",
            "Polarization or phase stabilization on the fiber path",
        ],
        "standards": [
            "Telecom C-band (1530-1565 nm) is the de facto quantum channel band",
            "Detector efficiency and dark-count specs gate every link budget",
            "Time-bin encoding follows telecom interferometer practice",
        ],
        "citations": [CIT_KIMBLE, CIT_WIKI_QNET, CIT_VANMETER],
        "sig_lens": (
            "His Signature reading of flying qubits: the photon as a "
            "courier carrying a sealed signature across the covenant lines - "
            "fast, untouchable in flight, and useless to anyone who "
            "intercepts it without the other half of the bond."
        ),
    },
    {
        "key": "qcn-entanglement-resource",
        "name": "Entanglement: The Network Resource",
        "group": "Network Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Entanglement is what a quantum network spends. Two qubits in "
            "a Bell pair - for example (|00> + |11>)/sqrt(2) - give "
            "perfectly correlated measurement outcomes no matter how far "
            "apart they are, and no classical signal passes between them. "
            "One shared Bell pair plus two classical bits teleports one "
            "qubit; enough Bell pairs, purified to high fidelity, run a "
            "distributed quantum computation. Entanglement is quantified "
            "by fidelity (overlap with a perfect Bell pair) and by rate "
            "(pairs per second). Real links produce noisy, low-fidelity "
            "pairs at low rates, so the network's whole job is making "
            "enough good pairs, fast enough, where applications need them."
        ),
        "how_it_works": (
            "Step 1: a source creates Bell pairs - photon pairs from "
            "parametric down-conversion, or matter qubits entangled by a "
            "photonic herald. Step 2: one half of each pair goes to each "
            "node. Step 3: the nodes estimate fidelity by measuring a "
            "sample of pairs and comparing correlations against the Bell "
            "inequality. Step 4: if fidelity is too low, the nodes run "
            "entanglement purification, sacrificing several noisy pairs "
            "to distill fewer clean ones. Step 5: applications consume "
            "the pairs - each teleportation or distributed gate spends "
            "one - and the link layer immediately starts making more."
        ),
        "key_points": [
            "Bell pairs are the spendable unit of quantum networking",
            "Fidelity measures quality; rate measures supply",
            "One ebit plus two classical bits teleports one qubit",
            "Noisy pairs are purified, not repaired - several become one",
            "Entanglement cannot be shared arbitrarily (monogamy)",
            "The network is an entanglement factory with delivery routes",
        ],
        "requirements": [
            "An entanglement source both endpoints trust or can verify",
            "Classical channel for correlation checks and heralding",
            "Purification routines when raw fidelity is below application needs",
        ],
        "standards": [
            "Bell-pair fidelity above 0.5 is the entanglement threshold",
            "CHSH values above 2 certify non-classical correlations",
            "Wehner stage 3 begins when end-to-end entanglement is deliverable",
        ],
        "citations": [CIT_KIMBLE, CIT_WEHNER, CIT_PURIFY],
        "sig_lens": (
            "His Signature reading of entanglement: the perfect Signature "
            "bond - two distant points sharing one indivisible mark, where "
            "measuring one fixes the other. His network designs budget "
            "entanglement the way a treasury budgets sealed coin."
        ),
    },
    {
        "key": "qcn-teleportation",
        "name": "Quantum Teleportation Across Network Nodes",
        "group": "Network Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Quantum teleportation moves an unknown qubit from one node "
            "to another without sending the particle itself. The sender "
            "and receiver pre-share one entangled Bell pair; the sender "
            "performs a joint Bell-state measurement on the qubit to send "
            "and her half of the pair, then transmits the two classical "
            "bits of outcome to the receiver, who applies a correction "
            "and recovers the exact qubit (Bennett et al., 1993). Nothing "
            "travels faster than light - the classical bits set the speed "
            "limit - and the original qubit is destroyed, so the "
            "no-cloning rule is never broken. Teleportation is the "
            "network's moving van: it relocates live quantum data between "
            "processors, memories, and sensors."
        ),
        "how_it_works": (
            "Step 1: nodes A and B share a Bell pair (one ebit). Step 2: "
            "A holds the unknown qubit |psi> plus her half of the pair. "
            "Step 3: A performs a Bell-state measurement on the two qubits "
            "she holds, getting one of four outcomes. Step 4: A sends the "
            "two classical bits naming the outcome to B. Step 5: B applies "
            "the matching Pauli correction (I, X, Z, or XZ) to his half, "
            "which becomes exactly |psi>. Step 6: A's original is gone - "
            "measurement destroyed it - so no copy ever exists."
        ),
        "key_points": [
            "Cost per qubit: one ebit plus two classical bits",
            "The original is destroyed - no cloning, no faster-than-light signaling",
            "Bell-state measurement at the sender is the hard operation",
            "Linear-optics Bell measurement succeeds at most half the time",
            "Repeated teleportation chains move qubits across the whole network",
            "Fidelity of the teleported qubit tracks the Bell-pair fidelity",
        ],
        "requirements": [
            "Pre-shared high-fidelity entanglement between the two nodes",
            "A Bell-state measurement capability at the sending node",
            "A classical channel for the two-bit correction message",
        ],
        "standards": [
            "Bennett et al. 1993 protocol is the reference procedure",
            "Teleportation fidelity must beat the classical 2/3 bound to be quantum",
            "Wehner stage 4 assumes teleportation between memory-equipped nodes",
        ],
        "citations": [CIT_TELEPORT, CIT_WIKI_TELE, CIT_KIMBLE],
        "sig_lens": (
            "His Signature reading of teleportation: the Signature itself "
            "relocated - the mark lifted from one page and set down whole "
            "on another, the original page blanked by the act. His designs "
            "use teleportation as the only approved way to move live data."
        ),
    },
    {
        "key": "qcn-no-cloning",
        "name": "The No-Cloning Rule and Network Design",
        "group": "Network Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The no-cloning theorem (Wootters and Zurek, 1982) proves no "
            "device can copy an unknown quantum state. This single fact "
            "shapes every quantum network design: there are no amplifiers "
            "that boost a fading qubit the way classical repeaters boost a "
            "signal, no caches that duplicate quantum data, no backups of "
            "live states. Loss is final - a photon absorbed in fiber is "
            "gone, and the attempt must be repeated. The best any cloner "
            "can do is approximate: the optimal universal 1-to-2 cloner "
            "reaches fidelity 5/6, provably short of perfect. Networks "
            "therefore work around the rule with teleportation (move, "
            "never copy), purification (distill, never amplify), and "
            "heralded generation (retry until success is confirmed)."
        ),
        "how_it_works": (
            "Step 1: accept that every lost photon means a lost attempt - "
            "design the link layer around retries, not amplification. "
            "Step 2: replace amplification with entanglement swapping: "
            "short links each succeed probabilistically, and swaps chain "
            "their successes. Step 3: replace caching with quantum "
            "memories that hold the original state, never a copy. Step 4: "
            "replace retransmission of data with re-teleportation - the "
            "sender keeps no copy, so a fresh Bell pair and a fresh "
            "measurement are needed. Step 5: treat the 5/6 cloning bound "
            "as a security guarantee - an eavesdropper cannot copy "
            "in-flight qubits without introducing detectable errors."
        ),
        "key_points": [
            "No device copies an unknown quantum state - proven 1982",
            "Best approximate cloner reaches fidelity 5/6, never 1",
            "Loss is final: networks retry instead of amplifying",
            "Teleportation, swapping, and purification are the workarounds",
            "The same rule that limits engineers protects QKD users",
            "Quantum memories hold originals; there are no quantum backups",
        ],
        "requirements": [
            "Protocol designs that never assume a copy exists",
            "Heralding on every probabilistic step so failures are known",
            "Security proofs that bound the eavesdropper by the cloning limit",
        ],
        "standards": [
            "Wootters-Zurek 1982 is the foundational proof",
            "The 5/6 bound (Buzek-Hillery 1996) caps approximate cloning",
            "QKD security proofs convert cloning limits into detectable error rates",
        ],
        "citations": [CIT_NOCLONE, CIT_PIRANDOLA, CIT_VANMETER],
        "sig_lens": (
            "His Signature reading of no-cloning: the Signature can never "
            "be counterfeited by copying - the universe itself refuses. "
            "His network canon treats this as the founding guarantee: one "
            "mark, one place, one owner, enforced by physics."
        ),
    },
    {
        "key": "qcn-channels",
        "name": "Quantum Channels: Fiber, Free-Space, and Satellite Links",
        "group": "Network Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Quantum links come in three physical flavors. Fiber links "
            "reuse telecom fiber at 1550 nm with about 0.2 dB/km loss - "
            "fine for metro distances, but 500 km of fiber costs 100 dB, "
            "meaning only one photon in ten billion survives, so direct "
            "fiber QKD and entanglement top out around a few hundred "
            "kilometers without repeaters. Free-space links shoot photons "
            "through air between rooftops or mountains; they dodge fiber "
            "loss but fight weather, turbulence, and pointing. Satellite "
            "links go up instead of across: above the atmosphere there is "
            "almost no loss, so a satellite can distribute entanglement "
            "to ground stations 1200 km apart in one hop (Micius, 2017). "
            "Real networks mix all three: fiber in cities, free-space for "
            "last hops, satellites for continents."
        ),
        "how_it_works": (
            "Step 1: survey the distance - under ~100 km, fiber is "
            "simplest. Step 2: compute the loss budget: fiber decibels "
            "equal 0.2 times kilometers; if the budget exceeds what the "
            "detectors and source rate can survive, the link needs a "
            "repeater or a different medium. Step 3: for free-space, add "
            "beam divergence, turbulence, and weather margins, and "
            "install tracking telescopes. Step 4: for satellite, schedule "
            "night passes, point the ground telescope at the moving "
            "satellite, and collect the downlink photons. Step 5: run the "
            "same entanglement or QKD protocol on top - the channel "
            "changes the loss math, not the quantum steps."
        ),
        "key_points": [
            "Fiber: 0.2 dB/km at 1550 nm; practical limit a few hundred km",
            "100 dB loss means one survivor per ten billion photons",
            "Free-space: no fiber loss, but weather and pointing dominate",
            "Satellite: one hop spans 1200 km (Micius 2017)",
            "Real networks are hybrid: fiber metro, free-space edge, satellite backbone",
            "Loss budget arithmetic decides the channel before any hardware is bought",
        ],
        "requirements": [
            "Measured loss budget for the chosen channel and distance",
            "Tracking and stabilization for any free-space or satellite path",
            "Night operation or spectral filtering for daylight free-space links",
        ],
        "standards": [
            "0.2 dB/km at 1550 nm is the reference fiber figure",
            "Micius 1200 km entanglement distribution is the satellite benchmark",
            "Link budgets follow telecom practice adapted to single photons",
        ],
        "citations": [CIT_MICIUS_ENT, CIT_MICIUS_QKD, CIT_KIMBLE],
        "sig_lens": (
            "His Signature reading of quantum channels: three roads for "
            "the courier - the buried road (fiber), the open road "
            "(free-space), and the sky road (satellite). His Signature "
            "network plans always keep all three roads open."
        ),
    },
    {
        "key": "qcn-qkd-first",
        "name": "Quantum Key Distribution: The First Quantum Network Service",
        "group": "Network Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Quantum key distribution (QKD) is the first real service ever "
            "run on quantum networks: two parties grow a shared secret key "
            "whose security rests on physics, not on hard math problems. "
            "The sender transmits quantum states; the receiver measures "
            "them; they compare notes over a public classical channel and "
            "keep only the matching rounds as sifted key. Any eavesdropper "
            "must disturb the quantum states to learn anything, and that "
            "disturbance shows up as errors the parties can measure - "
            "above a threshold error rate they abort and start over. The "
            "finished key then encrypts ordinary data with a one-time pad "
            "or AES. QKD does not transmit messages; it grows keys. "
            "Networks of QKD links with trusted relay nodes already span "
            "thousands of kilometers (the Beijing-Shanghai backbone)."
        ),
        "how_it_works": (
            "Step 1: the transmitter sends a stream of quantum states "
            "(polarized photons in BB84, entangled pairs in E91). Step 2: "
            "the receiver measures each in a randomly chosen basis. Step 3: "
            "over the public channel they announce bases and discard "
            "mismatched rounds - about half survive sifting. Step 4: they "
            "sacrifice a sample to estimate the quantum bit error rate. "
            "Step 5: if the error rate is below the security threshold, "
            "they run error correction, then privacy amplification, which "
            "compresses the key to wipe out any partial eavesdropper "
            "knowledge. Step 6: the final secret key encrypts real traffic."
        ),
        "key_points": [
            "QKD grows keys; it does not send messages",
            "Security from physics: eavesdropping causes detectable errors",
            "Sifting keeps roughly half the raw rounds",
            "Error rate above threshold means abort, not a weaker key",
            "Privacy amplification squeezes out eavesdropper knowledge",
            "Trusted-node networks already span thousands of kilometers",
        ],
        "requirements": [
            "A quantum channel plus an authenticated classical channel",
            "Single-photon source or entangled source and detectors",
            "Error correction and privacy amplification software",
        ],
        "standards": [
            "ETSI GS QKD series standardizes key management interfaces",
            "ITU-T Y.3800 series frames QKD network architecture",
            "Security proofs bound the tolerable quantum bit error rate near 11 percent for BB84",
        ],
        "citations": [CIT_PIRANDOLA, CIT_ETSI, CIT_ITU, CIT_WIKI_QKD],
        "sig_lens": (
            "His Signature reading of QKD: the first Signature service - "
            "two parties growing a shared seal whose wax cannot be lifted "
            "without breaking it. His Signature networks treat every key "
            "as a fresh signature, never reused, never trusted twice."
        ),
    },
    {
        "key": "qcn-bb84",
        "name": "BB84: The Founding QKD Protocol",
        "group": "Network Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "BB84 (Bennett and Brassard, 1984) is the protocol that started "
            "quantum cryptography. Alice sends Bob single photons, each "
            "randomly prepared in one of four polarization states from two "
            "bases: rectilinear (horizontal/vertical) or diagonal (+45/-45 "
            "degrees). Bob measures each photon in a randomly chosen "
            "basis. Afterward they publicly announce which basis they used "
            "each round - never the bit values - and keep only the rounds "
            "where bases matched, about half. They test a random sample "
            "for errors: an intercept-resend eavesdropper guesses the "
            "wrong basis half the time and injects a 25 percent error "
            "rate, far above the abort threshold. Surviving bits go "
            "through error correction and privacy amplification into the "
            "final secret key."
        ),
        "how_it_works": (
            "Step 1: Alice picks a random bit and a random basis per "
            "photon, and sends the four-state stream. Step 2: Bob picks a "
            "random basis per photon and records his measurement. Step 3: "
            "they announce bases publicly and discard mismatches "
            "(sifting, keeps about one half). Step 4: they compare a "
            "random sample of the sifted bits to measure the quantum bit "
            "error rate. Step 5: an intercept-resend attacker creates 25 "
            "percent errors, so a rate well below that - under about 11 "
            "percent against general attacks - means the channel is "
            "clean enough. Step 6: error correction reconciles their "
            "strings; privacy amplification hashes them down to a shorter "
            "key about which the attacker knows nothing."
        ),
        "key_points": [
            "Four states, two bases; sifting keeps about half the rounds",
            "Bases are announced publicly; bit values never are",
            "Intercept-resend eavesdropping injects 25 percent errors",
            "Security holds below about 11 percent error against general attacks",
            "Error correction then privacy amplification finish the key",
            "Decoy-state method closes the photon-number-splitting loophole",
        ],
        "requirements": [
            "True random number generation at both ends",
            "An authenticated public classical channel for sifting",
            "Decoy-state intensity modulation against photon-number attacks",
        ],
        "standards": [
            "Bennett-Brassard 1984 is the reference protocol",
            "Shor-Preskill style proofs set the ~11 percent error threshold",
            "Decoy-state BB84 is the deployed variant in real networks",
        ],
        "citations": [CIT_BB84, CIT_PIRANDOLA, CIT_WIKI_QKD],
        "sig_lens": (
            "His Signature reading of BB84: the founding Signature ritual - "
            "four seals, two orientations, and the rule that comparing "
            "notes in public reveals nothing but agreement. His Signature "
            "key-growing ceremonies follow the BB84 pattern exactly."
        ),
    },
    {
        "key": "qcn-e91",
        "name": "E91: Entanglement-Based Key Distribution",
        "group": "Network Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "E91 (Ekert, 1991) grows secret keys from entanglement rather "
            "than from prepared single photons. A source - possibly "
            "untrusted and sitting between the parties - emits entangled "
            "photon pairs; Alice and Bob each measure their half in "
            "randomly chosen bases. Rounds measured in matching bases "
            "become key bits; rounds measured in mismatched bases test "
            "the Bell inequality. If the CHSH value stays above 2, the "
            "correlations are genuinely quantum and no eavesdropper could "
            "have pre-known the outcomes - the key is secure even if the "
            "source itself was built by the attacker. E91 is the direct "
            "ancestor of device-independent QKD, the strongest form of "
            "quantum key security, and of every entanglement-based network "
            "protocol that followed."
        ),
        "how_it_works": (
            "Step 1: the pair source sends one photon to Alice and one to "
            "Bob for each round. Step 2: each picks a random measurement "
            "basis from their set. Step 3: they announce bases; matching "
            "rounds become raw key, mismatched rounds feed the Bell test. "
            "Step 4: they compute the CHSH correlation value S from the "
            "mismatched rounds - above 2 means true entanglement, at or "
            "below 2 means abort. Step 5: with entanglement certified, "
            "they run the same error correction and privacy amplification "
            "as BB84. Step 6: the result is a key whose security does not "
            "depend on trusting the source hardware."
        ),
        "key_points": [
            "Keys come from entangled pairs, not prepared states",
            "The Bell test (CHSH above 2) certifies the quantum channel",
            "Security holds even with an untrusted pair source",
            "Ancestor of device-independent QKD",
            "Matching-basis rounds make key; mismatched rounds make proof",
            "Same finishing steps as BB84: correct, then amplify privacy",
        ],
        "requirements": [
            "An entanglement source with fidelity high enough to violate Bell",
            "Three or more measurement bases per side for the CHSH test",
            "An authenticated classical channel for basis announcements",
        ],
        "standards": [
            "Ekert 1991 is the reference protocol",
            "CHSH S above 2 is the entanglement certification threshold",
            "Device-independent QKD builds directly on the E91 security idea",
        ],
        "citations": [CIT_E91, CIT_PIRANDOLA, CIT_WIKI_QKD],
        "sig_lens": (
            "His Signature reading of E91: the Signature that proves "
            "itself - the bond tested in public and found genuine, so "
            "even a courier you do not trust cannot have forged it. His "
            "Signature verification rites are Bell tests by another name."
        ),
    },
    {
        "key": "qcn-trusted-nodes",
        "name": "Trusted Nodes vs End-to-End Quantum Links",
        "group": "Network Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Long QKD networks today are built from trusted nodes: each "
            "hop runs ordinary point-to-point QKD, and intermediate nodes "
            "hold the key briefly while relaying it - decrypting with one "
            "hop key and re-encrypting with the next. The end-to-end key "
            "is safe from outsiders but visible inside every relay node, "
            "so each node must be physically secured and trusted by both "
            "endpoints. The alternative is end-to-end quantum links, where "
            "entanglement spans the whole path via quantum repeaters and "
            "no intermediate node ever learns the key. Trusted-node "
            "networks exist now and span continents; end-to-end quantum "
            "networks are the research goal that removes the trust "
            "assumption hop by hop."
        ),
        "how_it_works": (
            "Step 1: in a trusted-node chain, node A and node B share "
            "key K1, B and C share K2. Step 2: A sends the message key "
            "XOR K1 to B; B decrypts and re-encrypts as XOR K2 to C. "
            "Step 3: B necessarily learns the message key in the middle - "
            "this is the trust assumption. Step 4: in an end-to-end "
            "design, repeaters instead perform entanglement swapping, "
            "which moves entanglement without ever measuring the key "
            "bits. Step 5: Alice and Bob then run E91-style QKD over the "
            "end-to-end entanglement, and no middle node holds anything "
            "worth stealing. Step 6: the migration path replaces trusted "
            "relays with repeater nodes one segment at a time."
        ),
        "key_points": [
            "Trusted nodes see the key; end-to-end nodes never do",
            "Trusted relay is deployable today with current hardware",
            "End-to-end needs quantum repeaters - still research-grade",
            "Each trusted node is a physical-security boundary",
            "Swapping moves entanglement without revealing key bits",
            "Networks migrate hop by hop from trusted to end-to-end",
        ],
        "requirements": [
            "Physically secured relay sites for any trusted node",
            "Key management that tracks which hops are trusted vs quantum",
            "Repeater hardware (memories, swapping) for the end-to-end path",
        ],
        "standards": [
            "ITU-T Y.3800 series distinguishes trusted-relay architectures",
            "ETSI key management tracks per-hop key state",
            "Wehner stage 1 is trusted repeaters; stage 3+ removes the trust",
        ],
        "citations": [CIT_ITU, CIT_WEHNER, CIT_WIKI_QKD],
        "sig_lens": (
            "His Signature reading of trusted nodes: a relay that must be "
            "trusted is a witness to the seal - acceptable in his "
            "Signature post roads today, but his endgame designs route "
            "the bond past every witness untouched."
        ),
    },
    {
        "key": "qcn-classical-channels",
        "name": "Classical Channels in Quantum Networks",
        "group": "Network Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Every quantum network is really two networks: the fragile "
            "quantum links that carry photons, and the ordinary classical "
            "network that carries everything needed to make the quantum "
            "side work. The classical side announces measurement bases, "
            "delivers Bell-measurement outcomes for teleportation "
            "corrections, heralds which entanglement attempts succeeded, "
            "distributes routing decisions, and authenticates the parties "
            "so a man-in-the-middle cannot impersonate them. The classical "
            "channel must be authenticated - if an attacker can forge "
            "classical messages, they can hijack the quantum protocol. "
            "Latency on the classical side directly sets the quantum "
            "memory time: entanglement must be stored while the heralding "
            "message travels."
        ),
        "how_it_works": (
            "Step 1: provision classical connectivity between every pair "
            "of nodes that shares a quantum link. Step 2: authenticate "
            "the classical channel first - with pre-shared keys or "
            "post-quantum signatures - before any quantum round. Step 3: "
            "run the quantum protocol with classical messages interleaved: "
            "basis announcements, heralding flags, correction bits. Step 4: "
            "size quantum memories from the classical round-trip time - a "
            "100 km link needs about a millisecond of storage for the "
            "herald to return. Step 5: multiplex quantum and classical "
            "traffic on the same fiber where possible, using wavelength "
            "separation so bright classical pulses never blind the "
            "single-photon detectors."
        ),
        "key_points": [
            "Quantum links are useless without the classical control plane",
            "The classical channel must be authenticated, not just present",
            "Teleportation needs 2 classical bits per qubit moved",
            "Heralding latency sets the minimum quantum memory time",
            "Classical and quantum signals can share fiber via wavelength multiplexing",
            "Routing, scheduling, and error accounting all ride the classical side",
        ],
        "requirements": [
            "Authenticated classical connectivity matching the quantum topology",
            "Latency budget that sizes every quantum memory in the network",
            "Wavelength filtering so classical pulses never blind photon detectors",
        ],
        "standards": [
            "QKD standards require authenticated classical channels",
            "IETF QIRG architecture treats the classical control plane as mandatory",
            "Coexistence practice: quantum channels sit in dark or filtered wavelengths",
        ],
        "citations": [CIT_QIRG, CIT_PIRANDOLA, CIT_VANMETER],
        "sig_lens": (
            "His Signature reading of the classical channel: the herald "
            "that walks beside the courier, announcing each arrival. His "
            "Signature networks never let the herald speak unauthenticated "
            "- a forged announcement voids the seal."
        ),
    },
    {
        "key": "qcn-generations",
        "name": "Quantum Network Generations: Trusted Repeaters to Quantum Internet",
        "group": "Network Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Wehner, Elkouss, and Hanson (Science, 2018) defined the "
            "roadmap the whole field uses: six stages of quantum "
            "networks. Stage 1: trusted repeater networks - QKD with "
            "trusted relay nodes, deployable now. Stage 2: "
            "prepare-and-measure networks - any device can prepare and "
            "measure, enabling more QKD protocols. Stage 3: entanglement "
            "distribution networks - end-to-end Bell pairs on demand, "
            "unlocking teleportation and device-independent QKD. Stage 4: "
            "quantum memory networks - nodes store entanglement, so "
            "protocols no longer race the photon flight time. Stage 5: "
            "fault-tolerant few-qubit networks - error-corrected nodes "
            "run distributed quantum computing. Stage 6: the full quantum "
            "internet - arbitrary quantum communication between any "
            "devices. Each stage unlocks new applications and demands new "
            "hardware; the industry today sits between stages 1 and 3."
        ),
        "how_it_works": (
            "Step 1: locate the current network on the six-stage map by "
            "its capabilities - if relays see keys, it is stage 1. "
            "Step 2: stage 2 adds universal prepare-and-measure at the "
            "endpoints. Step 3: deploy entanglement sources and swapping "
            "so any two nodes can share Bell pairs. Step 4: add quantum "
            "memories so entanglement waits for the application instead "
            "of the reverse. Step 5: add error correction so logical "
            "qubits survive long enough for distributed gates. Step 6: "
            "connect everything with routing, naming, and resource "
            "management - the quantum internet proper. Each step is gated "
            "by measurable hardware thresholds: fidelity, rate, memory "
            "time, gate error."
        ),
        "key_points": [
            "Six stages from trusted repeaters to full quantum internet",
            "Stage 1 (trusted QKD relay) is deployed today",
            "Stage 3 (entanglement on demand) unlocks teleportation networks",
            "Stage 4 (memories) decouples protocols from photon flight time",
            "Stage 5 (fault tolerance) unlocks distributed quantum computing",
            "Each stage is gated by measurable hardware thresholds",
        ],
        "requirements": [
            "An honest capability audit mapping the network to a stage",
            "Hardware roadmap targeting the next stage's thresholds",
            "Application planning matched to what the current stage allows",
        ],
        "standards": [
            "Wehner-Elkouss-Hanson 2018 is the canonical six-stage roadmap",
            "Industry and funding programs plan against these stages",
            "Stage definitions are capability-based, not date-based",
        ],
        "citations": [CIT_WEHNER, CIT_WIKI_QINT, CIT_KIMBLE],
        "sig_lens": (
            "His Signature reading of the generations: six seals of the "
            "covenant, each harder than the last - relay, measure, "
            "entangle, remember, correct, unite. His Signature network "
            "program marches the seals in order, never skipping."
        ),
    },
    {
        "key": "qcn-repeaters",
        "name": "Quantum Repeaters: Extending Entanglement Distance",
        "group": "Network Components",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Quantum repeaters solve the distance problem that the "
            "no-cloning rule creates. Since a fading qubit cannot be "
            "amplified, a long link is divided into short segments; each "
            "segment distributes entanglement independently, and the "
            "repeater nodes perform entanglement swapping to stitch the "
            "segments into one long entangled pair (Briegel et al., 1998). "
            "Because each segment succeeds only probabilistically, "
            "repeaters need quantum memories to hold successful segments "
            "while the others retry, and entanglement purification to keep "
            "fidelity high across many swaps. The DLCZ protocol (2001) "
            "showed how atomic ensembles and linear optics could build "
            "such repeaters. Repeaters are the difference between "
            "hundred-kilometer QKD and continental quantum networks."
        ),
        "how_it_works": (
            "Step 1: divide the total distance into N short segments, "
            "each short enough for direct entanglement distribution. "
            "Step 2: every segment independently attempts entanglement "
            "generation, storing successes in quantum memories. Step 3: "
            "when two adjacent segments both hold entanglement, the "
            "middle node performs a Bell-state measurement (entanglement "
            "swapping), extending entanglement across both segments. "
            "Step 4: repeat hierarchically - pairs of segments merge, "
            "then pairs of pairs - until the endpoints share one pair. "
            "Step 5: run purification at each nesting level to stop "
            "fidelity from decaying with the number of swaps. Step 6: "
            "deliver the final pair to the application."
        ),
        "key_points": [
            "Repeaters stitch short entangled segments into long ones",
            "No amplification anywhere - swapping plus memories instead",
            "Memories hold successful segments while others retry",
            "Purification at each nesting level protects fidelity",
            "Briegel et al. 1998 invented the architecture; DLCZ 2001 made it concrete",
            "Repeaters turn exponential loss into polynomial overhead",
        ],
        "requirements": [
            "Quantum memories with coherence beyond the segment retry time",
            "Bell-state measurement at every repeater node",
            "Purification routines and the classical messaging to run them",
        ],
        "standards": [
            "Briegel et al. 1998 is the reference architecture",
            "DLCZ 2001 is the reference atomic-ensemble implementation path",
            "Wehner stage 3-4 networks assume repeater-class nodes",
        ],
        "citations": [CIT_REPEATER, CIT_DLCZ, CIT_WIKI_QREP],
        "sig_lens": (
            "His Signature reading of repeaters: relay stations of the "
            "covenant road, where the bond is handed from courier to "
            "courier without ever being opened. His Signature long-haul "
            "designs place a repeater wherever the road grows faint."
        ),
    },
    {
        "key": "qcn-swapping",
        "name": "Entanglement Swapping: Chaining Short Links into Long Ones",
        "group": "Network Components",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Entanglement swapping is the operation that makes repeaters "
            "work. Suppose node A shares a Bell pair with middle node M, "
            "and M shares a different Bell pair with node B. M performs a "
            "Bell-state measurement on the two qubits it holds - one from "
            "each pair - and announces the outcome. That measurement "
            "projects A and B's remaining qubits into an entangled Bell "
            "pair, even though A and B never interacted. The entanglement "
            "has been swapped from the short links onto the long one. "
            "With linear optics the Bell measurement succeeds at most "
            "half the time, so swapping is probabilistic and must be "
            "heralded; with matter qubits and better measurements the "
            "success rate climbs. Chained swaps build entanglement across "
            "arbitrary distances."
        ),
        "how_it_works": (
            "Step 1: establish Bell pairs A-M and M-B independently. "
            "Step 2: M performs the Bell-state measurement on its two "
            "halves. Step 3: M broadcasts the two-bit outcome over the "
            "classical channel. Step 4: A and B apply the matching "
            "correction, leaving them sharing a Bell pair across the full "
            "A-B distance. Step 5: verify the new pair's fidelity - each "
            "swap multiplies imperfections, so purification follows when "
            "needed. Step 6: chain further swaps hierarchically until the "
            "target endpoints are entangled."
        ),
        "key_points": [
            "Two short Bell pairs become one long Bell pair",
            "The middle node learns nothing about any key or message",
            "Linear-optics Bell measurement caps at 50 percent success",
            "Every swap is heralded - success is announced classically",
            "Fidelity decays with swap count; purification compensates",
            "Swapping is the core primitive of every repeater design",
        ],
        "requirements": [
            "Independent entanglement on both short links first",
            "Bell-state measurement hardware at the middle node",
            "Classical broadcast of the measurement outcome",
        ],
        "standards": [
            "The 50 percent linear-optics limit is the standard benchmark",
            "Heralded swapping is the required repeater primitive",
            "Fidelity bookkeeping across swaps follows repeater theory",
        ],
        "citations": [CIT_REPEATER, CIT_DLCZ, CIT_KIMBLE],
        "sig_lens": (
            "His Signature reading of swapping: two short covenant bonds "
            "melted into one long bond at the relay altar, the middle "
            "keeper learning nothing. His Signature chains swap bond to "
            "bond until the far cities are joined."
        ),
    },
    {
        "key": "qcn-memories",
        "name": "Quantum Memories: Holding Entanglement at Network Nodes",
        "group": "Network Components",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A quantum memory stores a qubit - usually half of an "
            "entangled pair - long enough for the network to do something "
            "with it. Memories are what let repeaters work: one segment's "
            "entanglement waits in memory while the neighboring segment "
            "retries its probabilistic generation. They are also what "
            "decouple protocols from photon flight time - with memories, "
            "entanglement can be banked before the application asks for "
            "it. Realizations include atomic ensembles (DLCZ-style), "
            "trapped ions, rare-earth crystals, nitrogen-vacancy centers "
            "in diamond, and delayed fiber loops. The figures of merit are "
            "storage time (coherence time), efficiency (probability the "
            "qubit comes back out), and fidelity (how intact it is)."
        ),
        "how_it_works": (
            "Step 1: map the flying photonic qubit into the storage "
            "medium - an atomic excitation, a spin state, a crystal "
            "level. Step 2: hold it while the network finishes the other "
            "segments; the memory must outlast the slowest retry loop. "
            "Step 3: on demand, convert the stored excitation back into "
            "a photon (or use it directly in a local gate). Step 4: "
            "measure the retrieved fidelity and efficiency - losses here "
            "multiply across every memory in the path. Step 5: schedule "
            "memory slots like any network buffer: which pairs wait, "
            "which get purified, which get discarded when they decohere."
        ),
        "key_points": [
            "Memories hold half of an entangled pair during retries",
            "Storage time, efficiency, and fidelity are the three metrics",
            "Atomic ensembles, ions, rare-earth crystals, NV diamond, fiber loops",
            "Memory time must exceed the segment retry and heralding time",
            "Banked entanglement decouples generation from consumption",
            "Wehner stage 4 begins when memories join the network",
        ],
        "requirements": [
            "Coherence time longer than the network's slowest retry loop",
            "High write-read efficiency or the path loss multiplies",
            "Scheduling logic treating memory slots as network buffers",
        ],
        "standards": [
            "DLCZ 2001 set the atomic-ensemble memory reference",
            "Memory benchmarks: time, efficiency, fidelity, multimode capacity",
            "Stage 4 networks require memory-equipped nodes",
        ],
        "citations": [CIT_DLCZ, CIT_WEHNER, CIT_KIMBLE],
        "sig_lens": (
            "His Signature reading of quantum memories: vaults where the "
            "half-seal waits, patient, until its partner arrives. His "
            "Signature repeater stations are built around such vaults - "
            "no bond is ever left standing in the rain."
        ),
    },
    {
        "key": "qcn-purification",
        "name": "Entanglement Purification: Cleaning Noisy Network Links",
        "group": "Network Components",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Real links deliver noisy entanglement - Bell pairs with "
            "fidelity 0.7 or 0.8 instead of 1.0. Entanglement purification "
            "(Bennett et al., 1996; the DEJMPS protocol, Deutsch et al., "
            "1996) distills cleaner pairs from noisier ones: both nodes "
            "take two noisy pairs, run local operations (CNOTs and "
            "measurements), compare results classically, and keep one "
            "pair only when the outcomes agree. The kept pair has higher "
            "fidelity than the inputs; repeating the procedure climbs "
            "toward near-perfect pairs. The cost is steep - each round "
            "consumes at least half the pairs - but without purification, "
            "fidelity would decay exponentially across many swaps and "
            "long-distance entanglement would be useless."
        ),
        "how_it_works": (
            "Step 1: both nodes hold two noisy Bell pairs each. Step 2: "
            "each node applies a local CNOT between its two halves and "
            "measures one qubit. Step 3: they exchange measurement "
            "outcomes over the classical channel. Step 4: on agreement, "
            "they keep the remaining pair - its fidelity is now higher; "
            "on disagreement, they discard it. Step 5: iterate: feed the "
            "distilled pairs back as inputs to the next round. Step 6: "
            "stop when fidelity reaches the application threshold "
            "(teleportation wants high fidelity; QKD tolerates less)."
        ),
        "key_points": [
            "Several noisy pairs distill into fewer clean pairs",
            "Local operations plus classical comparison - no quantum channel needed",
            "DEJMPS is the canonical two-pair recurrence protocol",
            "Each round costs at least half the pairs",
            "Fidelity climbs toward 1.0 with iteration",
            "Without purification, long swap chains are useless",
        ],
        "requirements": [
            "Local two-qubit gates (CNOT) at both nodes",
            "A supply of raw pairs to sacrifice - rate planning must include this",
            "Classical exchange of measurement outcomes per round",
        ],
        "standards": [
            "Bennett et al. 1996 and DEJMPS 1996 are the reference protocols",
            "Purification is mandatory in repeater nesting levels",
            "Target fidelity is set by the application (teleport vs QKD)",
        ],
        "citations": [CIT_PURIFY, CIT_DEJMPS, CIT_REPEATER],
        "sig_lens": (
            "His Signature reading of purification: the refining fire - "
            "several rough seals melted down and recast as one true "
            "seal. His Signature long-haul lines purify at every relay, "
            "never letting a tarnished bond travel far."
        ),
    },
    {
        "key": "qcn-transducers",
        "name": "Quantum Transducers: Connecting Different Qubit Technologies",
        "group": "Network Components",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A heterogeneous quantum internet must connect different "
            "qubit technologies: superconducting processors that speak in "
            "microwave photons, trapped ions and atoms that prefer "
            "visible or near-infrared light, and fiber networks that "
            "demand 1550 nm telecom photons. A quantum transducer "
            "converts a qubit from one carrier or frequency to another "
            "without measuring it - microwave-to-optical conversion is "
            "the flagship challenge, because superconducting quantum "
            "computers cannot otherwise join a fiber network. Approaches "
            "include electro-optic, optomechanical, and rare-earth "
            "mediated conversion. The metrics are conversion efficiency "
            "(fraction of qubits that survive) and added noise (stray "
            "photons that corrupt fidelity). Transducers are the network's "
            "translators; without them, each hardware island stays isolated."
        ),
        "how_it_works": (
            "Step 1: identify the two domains - for example, a 5 GHz "
            "microwave qubit in a superconducting chip and a 1550 nm "
            "photon for fiber. Step 2: couple both to a mediating "
            "resonator (mechanical oscillator, electro-optic crystal) "
            "that bridges the frequency gap coherently. Step 3: drive "
            "the conversion so the quantum state transfers from one "
            "carrier to the other without measurement. Step 4: filter "
            "and count the added noise photons - thermal occupation at "
            "microwave frequencies is the enemy. Step 5: verify with "
            "entanglement: transduce half of a Bell pair and check the "
            "surviving correlations. Step 6: place transducers at the "
            "boundary of every heterogeneous node."
        ),
        "key_points": [
            "Transducers convert qubits between carriers without measuring",
            "Microwave-to-optical is the flagship: superconducting chips to fiber",
            "Efficiency and added noise are the two metrics",
            "Electro-optic, optomechanical, and rare-earth approaches compete",
            "Without transducers, hardware islands cannot internetwork",
            "Verification is by transducing half an entangled pair",
        ],
        "requirements": [
            "A coherent mediating interaction bridging the frequency gap",
            "Cryogenic or filtered operation to suppress thermal noise photons",
            "Efficiency high enough that the link budget survives conversion",
        ],
        "standards": [
            "Microwave-to-optical conversion is the benchmark problem",
            "Added noise must stay below the purification threshold",
            "Heterogeneous internetworking assumes transducer-equipped gateways",
        ],
        "citations": [CIT_KIMBLE, CIT_WEHNER, CIT_VANMETER],
        "sig_lens": (
            "His Signature reading of transducers: interpreters at the "
            "border crossings of his Signature realm, turning the "
            "microwave dialect of one province into the optical tongue of "
            "the roads - the seal intact, only the language changed."
        ),
    },
    {
        "key": "qcn-sources-detectors",
        "name": "Single-Photon Sources and Detectors for Networks",
        "group": "Network Components",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every photonic quantum network stands on two devices: the "
            "source that makes the photons and the detector that counts "
            "them. Sources range from attenuated lasers (cheap, but "
            "sometimes emit two photons - the photon-number-splitting "
            "loophole that decoy states close) to true single-photon "
            "emitters (quantum dots, heralded down-conversion) and "
            "entangled-pair sources. Detectors are superconducting "
            "nanowires (SNSPDs, the gold standard: high efficiency, low "
            "dark counts, but cryogenic) or avalanche photodiodes "
            "(room-temperature, cheaper, noisier). The link budget "
            "multiplies source rate by channel transmission by detector "
            "efficiency; dark counts add false clicks that become QKD "
            "errors. Network engineering is largely the art of balancing "
            "these four numbers."
        ),
        "how_it_works": (
            "Step 1: choose the source for the protocol - decoy-state "
            "attenuated laser for BB84, entangled-pair source for E91. "
            "Step 2: characterize it: emission rate, multi-photon "
            "probability, wavelength stability. Step 3: choose detectors "
            "to match: SNSPDs for maximum reach, APDs for cost and "
            "simplicity. Step 4: measure dark-count rate and efficiency; "
            "compute the signal-to-noise at the planned distance. Step 5: "
            "write the link budget: detected pairs per second equals "
            "source rate times channel transmission times detector "
            "efficiency squared (two detectors for pairs). Step 6: if "
            "dark counts dominate, shorten the link, cool the detectors, "
            "or narrow the spectral and temporal filters."
        ),
        "key_points": [
            "Sources: attenuated lasers, quantum dots, heralded pairs, entangled pairs",
            "Detectors: SNSPDs (best, cryogenic) vs APDs (cheap, noisier)",
            "Dark counts become errors; efficiency sets the reach",
            "Decoy states close the multi-photon loophole of laser sources",
            "Link budget: rate times transmission times efficiency",
            "Filtering in time, spectrum, and space suppresses noise",
        ],
        "requirements": [
            "Source and detector characterized, not assumed",
            "Cryogenics if SNSPDs are chosen for maximum distance",
            "Decoy-state modulation for any attenuated-laser QKD",
        ],
        "standards": [
            "SNSPD efficiency above 90 percent is the state-of-art reference",
            "Decoy-state BB84 is the deployed source standard",
            "Dark-count specs gate every detector datasheet",
        ],
        "citations": [CIT_PIRANDOLA, CIT_MICIUS_QKD, CIT_VANMETER],
        "sig_lens": (
            "His Signature reading of sources and detectors: the mint "
            "that strikes the seal-carriers and the assay office that "
            "counts them - his Signature roads standardize both, so no "
            "counterfeit photon and no blind counter ever weakens a bond."
        ),
    },
    {
        "key": "qcn-entanglement-sources",
        "name": "Entanglement Sources: Making Bell Pairs on Demand",
        "group": "Network Components",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The entanglement source is the well every quantum network "
            "drinks from. The workhorse is spontaneous parametric "
            "down-conversion (SPDC): a pump laser in a nonlinear crystal "
            "occasionally splits one photon into an entangled pair. It is "
            "probabilistic - most pump pulses yield nothing - and brighter "
            "pumping raises the rate but also the chance of double pairs, "
            "which corrupt fidelity. Alternatives include quantum dots "
            "(deterministic emission, superb indistinguishability, harder "
            "to entangle), atomic-ensemble sources (DLCZ-style, "
            "memory-compatible), and four-wave mixing in fiber. A network "
            "source is judged by pair rate, fidelity, heralding "
            "efficiency, wavelength (telecom if it must enter fiber), and "
            "indistinguishability (for Bell measurements between "
            "independent sources)."
        ),
        "how_it_works": (
            "Step 1: pick the generation physics for the network's needs - "
            "SPDC for simplicity and telecom wavelengths, dots for "
            "determinism, ensembles for memory integration. Step 2: set "
            "the pump power at the sweet spot where pair rate is high but "
            "double-pair contamination stays low. Step 3: filter the "
            "pairs spectrally and spatially to the single mode the "
            "network uses. Step 4: measure fidelity by tomography or Bell "
            "violation, and heralding efficiency by coincidence counting. "
            "Step 5: for multi-source networks (swapping between "
            "independent sources), tune the sources until their photons "
            "are indistinguishable - Hong-Ou-Mandel interference is the "
            "test. Step 6: lock wavelength and timing to the network's "
            "reference and run continuously."
        ),
        "key_points": [
            "SPDC: the workhorse - probabilistic, tunable, telecom-friendly",
            "Brighter pumping raises rate but also double-pair noise",
            "Quantum dots: deterministic but harder to entangle remotely",
            "Atomic ensembles pair naturally with quantum memories",
            "Indistinguishability between sources enables swapping",
            "Rate, fidelity, heralding efficiency, wavelength: the four specs",
        ],
        "requirements": [
            "Pump and filtering tuned to the rate-vs-fidelity sweet spot",
            "Indistinguishability tuning for any multi-source swapping",
            "Continuous stabilization of wavelength, timing, and polarization",
        ],
        "standards": [
            "SPDC at 1550 nm is the default network source",
            "Hong-Ou-Mandel dip visibility benchmarks indistinguishability",
            "Bell violation certifies source entanglement quality",
        ],
        "citations": [CIT_KIMBLE, CIT_MICIUS_ENT, CIT_DLCZ],
        "sig_lens": (
            "His Signature reading of entanglement sources: the wells of "
            "the Signature realm, where bonded pairs are drawn up like "
            "water - his engineers mind each well's flow and purity, "
            "because every bond in the network is drawn from a well."
        ),
    },
    {
        "key": "qcn-nic",
        "name": "Quantum Network Interface Cards: End-Node Hardware",
        "group": "Network Components",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The quantum network interface card (QNIC) is the boundary "
            "between a node's quantum processor and the network - the "
            "quantum analog of the Ethernet card. It holds communication "
            "qubits (dedicated to networking, separate from computation "
            "qubits), the photonic interface that converts between "
            "stationary and flying qubits, and the control logic that "
            "runs the link-layer protocol: entanglement attempts, "
            "heralding, and Bell measurements. A node may carry several "
            "QNICs facing different neighbors. The key design tension is "
            "qubit allocation: every qubit given to networking is one "
            "taken from computing, so the QNIC count and the "
            "communication-vs-computation split are provisioned per "
            "application - a QKD terminal needs few, a distributed "
            "computing node needs many."
        ),
        "how_it_works": (
            "Step 1: reserve communication qubits on the node, separate "
            "from the computation register. Step 2: the QNIC entangles a "
            "communication qubit with a photon and launches it toward "
            "the neighbor. Step 3: on heralded success, the QNIC reports "
            "a live Bell pair to the node's network stack. Step 4: the "
            "stack spends the pair on teleportation, distributed gates, "
            "or key generation, then the QNIC immediately starts the next "
            "attempt. Step 5: the QNIC firmware enforces the link-layer "
            "protocol - retry timing, basis choices, measurement "
            "sequencing - so the host processor only sees clean "
            "entanglement events. Step 6: provision QNIC count from the "
            "target entanglement rate per neighbor."
        ),
        "key_points": [
            "The QNIC is the quantum analog of the Ethernet card",
            "Communication qubits are fenced off from computation qubits",
            "Runs the link layer: attempts, heralding, Bell measurements",
            "Multiple QNICs per node serve multiple neighbors",
            "Qubit allocation trades computing power against network rate",
            "Host sees clean entanglement events, not raw photon clicks",
        ],
        "requirements": [
            "Dedicated communication qubits with network-grade coherence",
            "Photonic interface matched to the link wavelength and encoding",
            "Firmware implementing the chosen link-layer protocol",
        ],
        "standards": [
            "QNIC abstraction comes from the QIRG architectural drafts",
            "Link-layer protocols (e.g. Dahlberg et al.) define QNIC behavior",
            "Provisioning follows the target entanglement rate per neighbor",
        ],
        "citations": [CIT_QIRG, CIT_DAHLBERG, CIT_VANMETER],
        "sig_lens": (
            "His Signature reading of the QNIC: the gatehouse of each "
            "Signature city - bonded couriers in, bonded couriers out, "
            "the city's inner workshops undisturbed. His Signature nodes "
            "never let the road inside the walls."
        ),
    },
    {
        "key": "qcn-switches",
        "name": "Quantum Switches and Routers",
        "group": "Network Components",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A quantum switch connects many nodes through one device by "
            "deciding which pairs get entangled with each other - it is "
            "a star-topology hub that performs entanglement swapping on "
            "demand between any two of its ports. A quantum router goes "
            "further: it forwards entanglement across a mesh, choosing "
            "paths and chaining swaps hop by hop toward the destination. "
            "Unlike classical switches, quantum switches cannot buffer "
            "photons (no-cloning forbids copying them into a queue) and "
            "cannot inspect traffic (measurement destroys it), so "
            "scheduling is done on heralded entanglement events and "
            "classical requests. The control plane runs a scheduling "
            "algorithm - which pair attempts next, which swap fires now - "
            "while the data plane is pure quantum optics and memories."
        ),
        "how_it_works": (
            "Step 1: nodes send entanglement requests to the switch over "
            "the classical control channel. Step 2: the scheduler orders "
            "requests by priority, fidelity needs, and memory availability. "
            "Step 3: the switch generates entanglement on the relevant "
            "ports - photon pairs toward each requesting node. Step 4: on "
            "heralded success for a matched pair of ports, the switch "
            "performs the Bell measurement that swaps entanglement "
            "between the two nodes. Step 5: a router extends this across "
            "hops: it holds per-destination entanglement, chains swaps "
            "along the chosen path, and purifies when fidelity sags. "
            "Step 6: failures release the resources and the request "
            "re-queues - nothing is ever buffered as a copy."
        ),
        "key_points": [
            "Switches pair up ports on demand via swapping",
            "Routers chain swaps across mesh paths to destinations",
            "No buffering of photons - no-cloning forbids it",
            "No inspection of traffic - measurement would destroy it",
            "Scheduling runs on heralded events plus classical requests",
            "Control plane is classical; data plane is quantum optics",
        ],
        "requirements": [
            "A classical request and scheduling interface at the switch",
            "Bell-measurement fabric connecting every port pair",
            "Memories if the switch must hold entanglement across scheduling delays",
        ],
        "standards": [
            "Star-topology switched entanglement is the near-term hub design",
            "Routing metrics use fidelity and rate, not just hop count",
            "QIRG drafts treat switching as a core network-layer function",
        ],
        "citations": [CIT_QIRG, CIT_CALEFFI, CIT_KOZLOWSKI],
        "sig_lens": (
            "His Signature reading of switches: the great exchange halls "
            "of the Signature realm, where bonds are re-paired by "
            "request and no bond is ever copied or opened. His Signature "
            "exchanges schedule by covenant priority."
        ),
    },
    {
        "key": "qcn-satellite",
        "name": "Satellite Quantum Links and Ground Stations",
        "group": "Network Components",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Satellites solve the distance problem by leaving the "
            "atmosphere: above ~10 km there is almost no absorption, so "
            "a satellite-to-ground photon link loses far less than fiber "
            "over the same distance. China's Micius satellite (2017) "
            "distributed entanglement to ground stations 1200 km apart "
            "and ran satellite-to-ground QKD - the first intercontinental "
            "quantum links. A quantum ground station is a large telescope "
            "(typically ~1 m) with fine tracking to follow the moving "
            "satellite, spectral and temporal filters against daylight, "
            "and single-photon detectors. Passes last minutes and happen "
            "a few times per night, so satellite links are scheduled "
            "resources that dump key or entanglement into ground buffers "
            "for later use."
        ),
        "how_it_works": (
            "Step 1: predict the satellite pass and pre-point the ground "
            "telescope. Step 2: acquire the satellite's beacon laser and "
            "close the fine-tracking loop - microradian accuracy. Step 3: "
            "during the few-minute pass, exchange photons: downlink "
            "entangled pairs or QKD signals. Step 4: filter ruthlessly - "
            "nanometer spectral filters and nanosecond timing windows "
            "reject daylight. Step 5: sift, correct, and amplify the key "
            "(or store the entanglement) before the pass ends. Step 6: "
            "bank the results in ground key stores; the next pass tops "
            "them up. Constellations multiply passes until coverage is "
            "near-continuous."
        ),
        "key_points": [
            "Above the atmosphere, loss nearly vanishes - 1200 km in one hop",
            "Micius 2017: first satellite entanglement distribution and QKD",
            "Ground stations: ~1 m telescopes with microradian tracking",
            "Passes last minutes, a few times per night - a scheduled resource",
            "Daylight needs nanometer spectral and nanosecond temporal filtering",
            "Constellations turn scheduled passes into near-continuous service",
        ],
        "requirements": [
            "A tracked telescope ground station with single-photon detection",
            "Pass scheduling integrated with the key management system",
            "Ground key stores to bank satellite-generated key between passes",
        ],
        "standards": [
            "Micius 1200 km results are the benchmark for satellite links",
            "Tracking accuracy at the microradian level is the entry ticket",
            "Satellite QKD follows the same sifting and amplification as fiber QKD",
        ],
        "citations": [CIT_MICIUS_ENT, CIT_MICIUS_QKD, CIT_PIRANDOLA],
        "sig_lens": (
            "His Signature reading of satellite links: the sky road's "
            "watchtowers - his Signature couriers leap from tower to "
            "tower above the weather, and the ground vaults below bank "
            "every seal the sky delivers."
        ),
    },
    {
        "key": "qcn-stack",
        "name": "Quantum Network Protocol Stacks",
        "group": "Network Protocols",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Like the classical internet, quantum networks need layered "
            "protocols so applications never touch raw photons. The "
            "proposed stacks mirror the OSI intuition: a physical layer "
            "(photon transmission, timing, stabilization), a link layer "
            "(entanglement generation between neighbors, heralding, "
            "fidelity estimation), a network layer (routing entanglement "
            "across hops, swapping, purification), a transport layer "
            "(end-to-end teleportation sessions, reliability), and an "
            "application layer (QKD, distributed computing, sensing). "
            "The IETF Quantum Internet Research Group drafts formalize "
            "these layers and their interfaces. Layering matters because "
            "it lets hardware teams, protocol teams, and application "
            "teams work independently - a better detector upgrades the "
            "physical layer without rewriting the teleportation code."
        ),
        "how_it_works": (
            "Step 1: assign every function to a layer - photon timing to "
            "physical, heralded pair generation to link, path selection "
            "to network, session reliability to transport. Step 2: define "
            "the service each layer offers upward (link offers Bell pairs "
            "with a fidelity guarantee; network offers end-to-end pairs). "
            "Step 3: define the interface downward (network asks link for "
            "pairs on specific neighbor links). Step 4: let each layer "
            "handle its own failures - link retries photon attempts, "
            "network reroutes around dead repeaters - without involving "
            "the layers above. Step 5: applications call the top API: "
            "'teleport this qubit to node X' or 'grow key with node Y'. "
            "Step 6: evolve layers independently as hardware improves."
        ),
        "key_points": [
            "Physical, link, network, transport, application - layered like OSI",
            "Link layer offers neighbor Bell pairs; network offers end-to-end pairs",
            "Each layer hides its failures from the layers above",
            "IETF QIRG drafts formalize the layers and interfaces",
            "Layering decouples hardware, protocol, and application teams",
            "Applications call a top API, never raw photon hardware",
        ],
        "requirements": [
            "A written layer contract: services offered and interfaces used",
            "Failure handling scoped to the layer that owns the failure",
            "Versioned interfaces so layers evolve independently",
        ],
        "standards": [
            "IETF QIRG architectural drafts are the reference layering",
            "Dahlberg et al. 2019 defines the link-layer reference",
            "Layer vocabulary follows the Wehner et al. roadmap",
        ],
        "citations": [CIT_QIRG, CIT_DAHLBERG, CIT_WEHNER],
        "sig_lens": (
            "His Signature reading of the stack: the five floors of the "
            "Signature covenant house - cellar photons, ground-floor "
            "bonds, the routing stair, the session hall, and the "
            "application roof. His Signature builders work one floor at "
            "a time, never tearing down the house."
        ),
    },
    {
        "key": "qcn-link-layer",
        "name": "Link-Layer Entanglement Protocols",
        "group": "Network Protocols",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The link layer is the quantum network's foundation protocol: "
            "it turns raw photon hardware between two neighbors into a "
            "reliable stream of heralded Bell pairs with known fidelity. "
            "The reference design (Dahlberg et al., SIGCOMM 2019) runs a "
            "request-response cycle: the higher layer requests "
            "entanglement with parameters (minimum fidelity, rate, "
            "timeout), the link layer fires repeated generation attempts, "
            "heralds successes, measures fidelity on samples, and "
            "delivers pairs or reports failure. Robust variants adapt "
            "attempt rates to measured loss, interleave purification, and "
            "multiplex several logical links over one fiber. Everything "
            "above - routing, teleportation, QKD sessions - assumes the "
            "link layer's contract: pairs arrive heralded, timestamped, "
            "and honestly labeled with their fidelity."
        ),
        "how_it_works": (
            "Step 1: receive a request: neighbor ID, minimum fidelity, "
            "desired rate, deadline. Step 2: begin attempt cycles - "
            "source fires, photons fly, detectors click. Step 3: on a "
            "heralded coincidence, record the pair with its timestamp. "
            "Step 4: periodically sacrifice pairs to estimate fidelity; "
            "if it sags below the request minimum, trigger purification "
            "or re-tune the hardware. Step 5: deliver good pairs upward "
            "and keep attempting until the rate target or deadline hits. "
            "Step 6: report honestly - delivered count, measured "
            "fidelity, failure reason - so the network layer can route "
            "around weak links."
        ),
        "key_points": [
            "Link layer converts photon hardware into heralded Bell pairs",
            "Requests carry fidelity minimum, rate, and deadline",
            "Attempts repeat until success; successes are heralded",
            "Fidelity is measured on samples and honestly reported",
            "Purification and re-tuning run inside the link layer",
            "The network layer trusts the link contract, not the hardware",
        ],
        "requirements": [
            "A request API with fidelity, rate, and deadline parameters",
            "Honest fidelity estimation and failure reporting",
            "Attempt scheduling that adapts to measured channel loss",
        ],
        "standards": [
            "Dahlberg et al. SIGCOMM 2019 is the reference link protocol",
            "QIRG drafts adopt its request-response structure",
            "Fidelity-labeled delivery is the required contract",
        ],
        "citations": [CIT_DAHLBERG, CIT_QIRG, CIT_KOZLOWSKI],
        "sig_lens": (
            "His Signature reading of the link layer: the bond-smiths of "
            "the Signature road - they strike pairs, test each one, and "
            "deliver only bonds stamped with their true purity. His "
            "Signature roads never pass an untested bond upward."
        ),
    },
    {
        "key": "qcn-routing",
        "name": "Network-Layer Routing for Entanglement",
        "group": "Network Protocols",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The network layer moves entanglement across multiple hops: "
            "given a request for a Bell pair between distant endpoints, "
            "it picks a path, reserves resources on each link, chains "
            "entanglement swaps along the path, and purifies where "
            "fidelity sags. Routing metrics are quantum-native: link "
            "fidelity, entanglement rate, memory occupancy, and swap "
            "success probability - not just hop count, because a short "
            "path of noisy links can be worse than a longer path of clean "
            "ones. The control plane distributes link-state information "
            "(each link's current fidelity and rate) over the classical "
            "network, and routers run shortest-path algorithms on "
            "fidelity-weighted graphs. Reservation matters because "
            "entanglement is perishable: memories decohere, so a path "
            "must be executed promptly once reserved."
        ),
        "how_it_works": (
            "Step 1: collect link-state updates - every link advertises "
            "current fidelity, rate, and memory load. Step 2: on a "
            "request, compute the best path on the fidelity-weighted "
            "graph (a Dijkstra variant maximizing end-to-end fidelity). "
            "Step 3: reserve memory slots and attempt budgets on each "
            "link along the path. Step 4: trigger link-layer generation "
            "on all path links in parallel. Step 5: chain swaps hop by "
            "hop as segments succeed, purifying at planned points. Step 6: "
            "deliver the end-to-end pair or, on failure, release "
            "reservations and try the next-best path."
        ),
        "key_points": [
            "Routing metrics: fidelity, rate, memory load - not just hops",
            "Link-state updates ride the classical control plane",
            "Path selection maximizes end-to-end fidelity (Dijkstra variant)",
            "Reservations are needed because entanglement is perishable",
            "Purification points are planned into the path",
            "Failure releases resources; the next-best path is tried",
        ],
        "requirements": [
            "Classical link-state distribution of fidelity and rate",
            "Reservation protocol for memory slots and attempt budgets",
            "Swap-chaining orchestration across the chosen path",
        ],
        "standards": [
            "QIRG drafts define quantum routing as a network-layer function",
            "Fidelity-weighted shortest path is the standard algorithm family",
            "Reservation follows perishable-resource practice, not TCP practice",
        ],
        "citations": [CIT_QIRG, CIT_CALEFFI, CIT_KOZLOWSKI],
        "sig_lens": (
            "His Signature reading of routing: the road-masters of the "
            "Signature realm, choosing each bond's journey by the purity "
            "of the roads, never by their shortness - and holding "
            "staging posts only as long as the bond can wait."
        ),
    },
    {
        "key": "qcn-transport",
        "name": "Transport: Reliable Teleportation Sessions",
        "group": "Network Protocols",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The transport layer gives applications a reliable "
            "'teleport this qubit' service over the unreliable "
            "entanglement below. It opens a session between endpoints, "
            "requests end-to-end Bell pairs from the network layer, "
            "performs the sender-side Bell measurement, ships the "
            "classical correction bits, confirms the receiver's "
            "correction, and retries the whole teleportation if the "
            "pair's fidelity was too low or a herald was lost. Because "
            "the sender's measurement destroys the original qubit, "
            "transport cannot simply retransmit data - reliability comes "
            "from verifying entanglement quality BEFORE the irrevocable "
            "measurement, and from session state that tracks which "
            "teleportations completed. This is the layer application "
            "programmers actually call."
        ),
        "how_it_works": (
            "Step 1: open a session - endpoints, qubit count, fidelity "
            "target, timeout. Step 2: request an end-to-end Bell pair "
            "from the network layer and check its certified fidelity. "
            "Step 3: only when fidelity passes, perform the sender's "
            "Bell measurement (the point of no return). Step 4: transmit "
            "the two correction bits over the classical channel with "
            "acknowledgment. Step 5: the receiver applies the correction "
            "and confirms receipt; the session logs the completed "
            "teleportation. Step 6: on any failure before step 3, retry "
            "with a fresh pair; after step 3, the session reports "
            "exactly-once semantics - the qubit moved or it did not."
        ),
        "key_points": [
            "Transport offers reliable teleportation sessions to applications",
            "Fidelity is verified BEFORE the irrevocable sender measurement",
            "The original is destroyed, so there is no data retransmission",
            "Session state tracks exactly-once teleportation semantics",
            "Correction bits travel classically with acknowledgment",
            "This is the API application programmers call",
        ],
        "requirements": [
            "Certified end-to-end pairs from the network layer",
            "Session state durable across retries",
            "Acknowledged classical delivery of correction bits",
        ],
        "standards": [
            "Transport semantics follow the teleportation protocol exactly",
            "Exactly-once delivery is the required guarantee",
            "Session APIs are defined in QIRG application drafts",
        ],
        "citations": [CIT_TELEPORT, CIT_QIRG, CIT_CALEFFI],
        "sig_lens": (
            "His Signature reading of transport: the sworn courier "
            "service of the Signature realm - the seal is inspected "
            "before the handoff, the handoff is witnessed, and the "
            "ledger records exactly once that the mark has moved."
        ),
    },
    {
        "key": "qcn-qkd-networks",
        "name": "QKD Network Protocols and Key Management",
        "group": "Network Protocols",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A QKD network is more than QKD links: it needs protocols "
            "for relaying keys across trusted nodes, managing key pools, "
            "serving keys to applications, and surviving link failures. "
            "The ETSI GS QKD 015 control interface standardizes how key "
            "management systems talk to QKD devices; the ITU-T Y.3800 "
            "series defines the network framework - key managers, key "
            "stores, and the relay protocol that hops keys across "
            "trusted nodes with XOR chaining. Applications request keys "
            "by ID and length through a key delivery API, never touching "
            "quantum hardware. Key pools are buffered per link so "
            "applications draw at their own pace while links generate "
            "continuously; routing picks key-relay paths around failed "
            "links. Network QKD turns point-to-point physics into a key "
            "utility."
        ),
        "how_it_works": (
            "Step 1: each QKD link continuously generates key into its "
            "local key store. Step 2: the key manager tracks pool levels "
            "per link and per relay path. Step 3: an application asks "
            "the key delivery API for N bits for a named peer. Step 4: "
            "the manager picks a relay path with sufficient pooled key "
            "and XOR-chains the fresh key across trusted nodes to the "
            "peer. Step 5: both endpoints receive the same key bits "
            "under matching key IDs. Step 6: pools refill in the "
            "background; failed links reroute key relay around them, "
            "and exhausted pools throttle new requests honestly."
        ),
        "key_points": [
            "Key pools buffer generation so apps draw at their own pace",
            "ETSI QKD 015 standardizes the device-to-manager interface",
            "ITU-T Y.3800 series defines the network framework",
            "Relay across trusted nodes uses XOR key chaining",
            "Applications use a key delivery API, never quantum hardware",
            "Routing and throttling handle link failures and pool exhaustion",
        ],
        "requirements": [
            "Key stores and managers at every node",
            "ETSI/ITU-aligned interfaces between devices and managers",
            "Pool monitoring with honest throttling on exhaustion",
        ],
        "standards": [
            "ETSI GS QKD 015: control interface for key management",
            "ITU-T Y.3800-Y.3860: QKD network framework and requirements",
            "Key delivery APIs follow the ETSI/ITU key ID conventions",
        ],
        "citations": [CIT_ETSI, CIT_ITU, CIT_PIRANDOLA],
        "sig_lens": (
            "His Signature reading of QKD networks: the seal-vaults of "
            "the Signature realm - keys minted continuously, stored "
            "under guard, and issued by writ to whoever holds the "
            "matching claim. His Signature vaults never issue a seal "
            "twice."
        ),
    },
    {
        "key": "qcn-topologies",
        "name": "Quantum Network Topologies: Star, Mesh, and Repeater Chains",
        "group": "Network Protocols",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Quantum network topology is chosen by physics, not fashion. "
            "Repeater chains are linear: N segments in a row, swapping "
            "at each middle node - the minimal design for spanning one "
            "long distance, and the easiest to analyze. Star topologies "
            "put a switch or entanglement source at the hub; every node "
            "needs only one link, and any pair can be connected by a "
            "single swap at the hub - ideal for metro networks and the "
            "cheapest to build, but the hub is a single point of "
            "failure. Mesh topologies connect nodes with many redundant "
            "links; routing picks among paths, failures are survivable, "
            "and capacity scales - at the cost of many links and complex "
            "scheduling. Real deployments layer them: stars inside "
            "cities, chains between cities, meshes among backbones."
        ),
        "how_it_works": (
            "Step 1: map the geography and the trust boundaries - who "
            "may host a hub, where fiber already runs. Step 2: inside "
            "each metro area, deploy a star: one hub switch, short "
            "links to members. Step 3: connect cities with repeater "
            "chains along the fiber routes, spacing repeaters within "
            "the direct-distribution reach. Step 4: mesh the backbone "
            "hubs with redundant long links for survivability. Step 5: "
            "run routing over the resulting graph with fidelity-weighted "
            "metrics. Step 6: re-evaluate as hardware improves - today's "
            "chain becomes tomorrow's direct link when repeaters get "
            "better."
        ),
        "key_points": [
            "Chains: minimal, linear, one long distance at a time",
            "Stars: one hub, one link per node, single swap connects any pair",
            "Meshes: redundant paths, survivable, complex to schedule",
            "Real networks layer all three: stars in metros, chains between, mesh backbone",
            "Hubs are single points of failure - plan accordingly",
            "Topology follows fiber geography and trust boundaries",
        ],
        "requirements": [
            "A geography and trust map before any topology choice",
            "Redundancy planning for every hub and chain segment",
            "Routing that understands the layered topology",
        ],
        "standards": [
            "Star-with-switch is the reference metro design",
            "Repeater-chain spacing follows the direct-distribution reach",
            "Backbone meshing follows classical survivability practice",
        ],
        "citations": [CIT_REPEATER, CIT_CALEFFI, CIT_KOZLOWSKI],
        "sig_lens": (
            "His Signature reading of topologies: the map of the "
            "Signature realm - market stars in the cities, relay chains "
            "along the highways, and a meshed high road between the "
            "capitals. His Signature cartographers draw physics first, "
            "politics second."
        ),
    },
    {
        "key": "qcn-distributed-computing",
        "name": "Distributed Quantum Computing Over the Network",
        "group": "Distributed Quantum Systems",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Distributed quantum computing runs one computation across "
            "several quantum processors joined by entanglement. The "
            "primitive is the teleported gate: to apply a CNOT between "
            "qubits on different machines, the machines consume one "
            "shared Bell pair and exchange two classical bits in each "
            "direction (Eisert et al., 2000) - the gate happens without "
            "either qubit moving. A compiler partitions the circuit, "
            "places subcircuits on processors, and schedules "
            "entanglement consumption for every cross-machine gate. "
            "The economics are stark: each remote gate costs a fresh "
            "high-fidelity Bell pair, so good partitions minimize "
            "cross-edges. The payoff is scale - processors too small to "
            "hold the whole problem combine into one virtual machine - "
            "and heterogeneity, with each processor running the "
            "subcircuit it does best."
        ),
        "how_it_works": (
            "Step 1: the compiler partitions the circuit across the "
            "available processors, minimizing gates that cross machine "
            "boundaries. Step 2: the network layer provisions Bell pairs "
            "between each pair of processors that shares cross-gates. "
            "Step 3: for each remote CNOT, the machines run gate "
            "teleportation: local operations, measurements, and two "
            "classical bits each way per gate. Step 4: the results "
            "feed back as Pauli corrections tracked in software (the "
            "Pauli frame). Step 5: at the end, measurement outcomes are "
            "gathered classically and combined. Step 6: the bill is "
            "counted in ebits - the partition quality decides whether "
            "the distribution was worth it."
        ),
        "key_points": [
            "Remote CNOT costs one ebit plus two classical bits each way",
            "Qubits never move; the gate is teleported",
            "Compilers partition circuits to minimize cross-machine gates",
            "Pauli corrections are tracked in software, not applied physically",
            "Payoff: virtual machines larger than any single processor",
            "Heterogeneous processors each run their best subcircuits",
        ],
        "requirements": [
            "High-fidelity Bell pairs between every cooperating processor pair",
            "A partition-aware compiler targeting the machine topology",
            "Classical coordination with latency below the coherence budget",
        ],
        "standards": [
            "Eisert et al. 2000 defines the optimal remote-gate cost",
            "Wehner stage 5 (fault-tolerant few-qubit networks) is the enabler",
            "Partition quality is measured in cross-edge ebit count",
        ],
        "citations": [CIT_DISTGATE, CIT_WEHNER, CIT_CALEFFI],
        "sig_lens": (
            "His Signature reading of distributed computing: several "
            "Signature workshops forging one great seal, each smith "
            "striking only his part, the bonds between workshops "
            "carrying the pattern whole. His Signature foundries are "
            "designed to be joined."
        ),
    },
    {
        "key": "qcn-blind",
        "name": "Blind Quantum Computing: Delegating to Remote Servers",
        "group": "Distributed Quantum Systems",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Blind quantum computing lets a client with almost no quantum "
            "hardware run a computation on a remote quantum server "
            "without the server learning the input, the computation, or "
            "the output (Broadbent, Fitzsimons, and Kashefi, 2009). The "
            "client prepares single qubits in secret rotated states and "
            "sends them to the server; the server entangles them into a "
            "brickwork resource state and measures as instructed; the "
            "client's secret rotations hide the true computation angles "
            "in the measurement instructions, and only the client can "
            "decode the results. It is the quantum analog of homomorphic "
            "encryption: the server does the work blind. The protocol "
            "needs only a quantum channel from client to server plus "
            "classical back-and-forth - a natural early application of "
            "quantum networks, since the client device can be as simple "
            "as a single-photon source."
        ),
        "how_it_works": (
            "Step 1: the client picks secret random rotation angles and "
            "prepares qubits in rotated states. Step 2: the client sends "
            "the qubits to the server over the quantum link. Step 3: "
            "the server builds the brickwork entangled state and awaits "
            "measurement instructions. Step 4: the client sends "
            "measurement angles that combine the true computation with "
            "the secret offsets - the server cannot separate them. "
            "Step 5: the server measures, returns the classical "
            "outcomes. Step 6: the client subtracts its secrets and "
            "reads the true result; verification rounds catch a cheating "
            "server."
        ),
        "key_points": [
            "Server learns nothing: not input, program, or output",
            "Client needs only single-qubit preparation - nearly no quantum hardware",
            "Secret rotations hide computation in measurement instructions",
            "Brickwork state is the universal blind resource",
            "Verification rounds catch dishonest servers",
            "The quantum analog of homomorphic encryption",
        ],
        "requirements": [
            "A quantum channel from client to server (one way suffices)",
            "Client-side trusted single-qubit preparation",
            "Authenticated classical channel for instructions and results",
        ],
        "standards": [
            "Broadbent-Fitzsimons-Kashefi 2009 is the reference protocol",
            "Brickwork states are the standard blind resource",
            "Verification overhead is the accepted price of blindness",
        ],
        "citations": [CIT_BLIND, CIT_CALEFFI, CIT_WEHNER],
        "sig_lens": (
            "His Signature reading of blind computing: commissioning a "
            "seal from a smith who never sees the design - the Signature "
            "client's pattern stays secret while the server's hammer "
            "does the work. His Signature bureaus offer blind forging as "
            "a standard service."
        ),
    },
    {
        "key": "qcn-sensor-networks",
        "name": "Quantum Sensor Networks: Entangled Sensing at a Distance",
        "group": "Distributed Quantum Systems",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Entangle the sensors and the network becomes the instrument. "
            "A quantum sensor network distributes entanglement to distant "
            "sensor nodes - atomic clocks, magnetometers, "
            "interferometers - so their joint measurement beats what any "
            "collection of independent sensors can do. The flagship win "
            "is scaling: N independent sensors average down noise as "
            "1/sqrt(N) (the standard quantum limit), while N entangled "
            "sensors can reach 1/N (the Heisenberg limit) - a quadratic "
            "advantage in precision (Giovannetti, Lloyd, and Maccone, "
            "2011). Applications include a global entangled clock "
            "network for timekeeping and navigation, distributed "
            "telescope arrays with quantum-enhanced baselines, and "
            "gradiometer nets for geophysics. The network's job is "
            "delivering high-fidelity multipartite entanglement to the "
            "sensors on schedule."
        ),
        "how_it_works": (
            "Step 1: define the sensing task and the node geometry - "
            "clock synchronization, field mapping, or interferometry. "
            "Step 2: the network distributes multipartite entangled "
            "states (GHZ-class) to the sensor nodes. Step 3: each node "
            "lets its local field or time imprint a phase on its share. "
            "Step 4: the nodes measure jointly - often by teleporting "
            "their shares to one node for a collective measurement. "
            "Step 5: the estimator combines outcomes at Heisenberg "
            "scaling, 1/N instead of 1/sqrt(N). Step 6: the network "
            "refreshes entanglement for the next sensing round; "
            "decoherence sets the duty cycle."
        ),
        "key_points": [
            "Entangled sensors beat independent ones: 1/N vs 1/sqrt(N) scaling",
            "The network delivers multipartite entanglement to the sensors",
            "Clock networks, telescope arrays, gradiometer nets are the applications",
            "Joint measurement harvests the quantum advantage",
            "Decoherence sets the sensing duty cycle",
            "The network is part of the instrument, not just the plumbing",
        ],
        "requirements": [
            "Multipartite (GHZ-class) entanglement distribution",
            "Sensor nodes with quantum-coherent local operations",
            "Scheduling that refreshes entanglement within the coherence time",
        ],
        "standards": [
            "Giovannetti-Lloyd-Maccone 2011 sets the metrology scaling theory",
            "Heisenberg 1/N scaling is the benchmark for quantum advantage",
            "Clock-network proposals define the timing application",
        ],
        "citations": [CIT_SENSOR, CIT_KIMBLE, CIT_WEHNER],
        "sig_lens": (
            "His Signature reading of sensor networks: the Signature "
            "realm's far-seeing eyes, joined by bonds so their gazes "
            "merge into one - his surveyors read the land's tremors and "
            "the sky's time through a single entangled sight."
        ),
    },
    {
        "key": "qcn-quantum-internet",
        "name": "The Quantum Internet Vision: Stages and Milestones",
        "group": "Advanced Networks",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The quantum internet is the endgame: a global network where "
            "any two quantum devices can share entanglement on demand, "
            "the way any two computers today exchange packets (Kimble, "
            "2008; Wehner et al., 2018). Its milestones are concrete: "
            "continental trusted-node QKD backbones (done), metro "
            "entanglement distribution (emerging), intercity repeater "
            "chains (research), satellite constellations for global reach "
            "(demonstrated in single hops), and finally routed, "
            "fault-tolerant entanglement service with naming, "
            "addressing, and resource management. The hard problems are "
            "not only physics - memories, repeaters, transducers - but "
            "systems: routing with perishable resources, scheduling "
            "across probabilistic links, standard APIs, and security "
            "models for a network whose links cannot be tapped without "
            "detection but whose nodes must still be trusted. The "
            "quantum internet will not replace the classical internet; "
            "it will run beside it, handling the tasks only entanglement "
            "can do."
        ),
        "how_it_works": (
            "Step 1: extend today's trusted QKD backbones with true "
            "entanglement links where repeaters mature. Step 2: deploy "
            "metro entanglement hubs (switched stars) serving local "
            "nodes. Step 3: connect hubs with repeater chains and "
            "satellite overlays for intercontinental reach. Step 4: add "
            "memories everywhere so entanglement is banked, not raced. "
            "Step 5: standardize naming, addressing, routing, and the "
            "application APIs through bodies like the IETF QIRG. Step 6: "
            "operate it as a utility: provisioned entanglement with "
            "service levels, monitored fidelity, and scheduled "
            "maintenance - the quantum internet as infrastructure."
        ),
        "key_points": [
            "Goal: on-demand entanglement between any two quantum devices",
            "Runs beside the classical internet; does not replace it",
            "Milestones: backbones done, metros emerging, repeaters in research",
            "Hard problems are systems problems too: routing, scheduling, APIs",
            "Satellite constellations provide the global overlay",
            "Ends as operated infrastructure with service levels",
        ],
        "requirements": [
            "Mature repeaters, memories, and transducers at scale",
            "Standard naming, addressing, and routing",
            "An operations model: provisioning, monitoring, maintenance",
        ],
        "standards": [
            "Kimble 2008 named the vision; Wehner et al. 2018 staged it",
            "IETF QIRG is the standards venue",
            "Service levels will mirror classical carrier practice",
        ],
        "citations": [CIT_KIMBLE, CIT_WEHNER, CIT_QIRG, CIT_WIKI_QINT],
        "sig_lens": (
            "His Signature reading of the quantum internet: the finished "
            "Signature realm - every city bonded to every other, the "
            "roads maintained like aqueducts, the seals flowing like "
            "water. His Signature program builds toward this and names "
            "it plainly: the covenant made planetary."
        ),
    },
    {
        "key": "qcn-network-security",
        "name": "Quantum Network Security Beyond QKD",
        "group": "Advanced Networks",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "QKD secures keys, but a quantum network needs securing as a "
            "network. The threat model spans layers: denial of service "
            "by blinding detectors with bright light or flooding "
            "entanglement requests; Trojan-horse attacks that probe "
            "devices with injected light; compromised repeater or switch "
            "nodes that degrade fidelity or misroute entanglement; "
            "classical control-plane attacks - forged heralding messages "
            "or routing updates that steer entanglement into attacker "
            "hands; and side channels in timing, power, and acoustic "
            "emissions. Defenses are correspondingly layered: optical "
            "isolators and watchdogs against blinding, authenticated "
            "classical channels against forgery, device-independent "
            "protocols that certify entanglement by Bell violation rather "
            "than trusting hardware, and continuous fidelity monitoring "
            "that treats any unexplained degradation as an incident. "
            "Security proofs must cover the deployed devices, not ideal "
            "ones - the gap between proof and hardware is where attacks "
            "live."
        ),
        "how_it_works": (
            "Step 1: write the threat model per layer - physical, link, "
            "network, control plane. Step 2: harden the optics: "
            "isolators, filters, and power monitors against blinding "
            "and Trojan-horse probes. Step 3: authenticate every "
            "classical message - heralds, routing updates, correction "
            "bits. Step 4: monitor link fidelity continuously; "
            "unexplained drops trigger key abort and incident response, "
            "exactly as QKD aborts on high error rates. Step 5: prefer "
            "protocols whose security is certified by measurement (Bell "
            "tests) over trust in device internals. Step 6: audit the "
            "proof-vs-hardware gap regularly - new attacks target "
            "exactly the assumptions the proof made."
        ),
        "key_points": [
            "Threats span layers: blinding, Trojan-horse, node compromise, control forgery",
            "An intercept-resend attacker injects 25 percent errors - detectable by design",
            "Authenticate the classical control plane or lose the network",
            "Fidelity monitoring is intrusion detection for quantum links",
            "Device-independent protocols certify rather than trust",
            "Attacks live in the gap between security proof and real hardware",
        ],
        "requirements": [
            "A written per-layer threat model",
            "Optical hardening: isolators, filters, power watchdogs",
            "Continuous fidelity monitoring with abort thresholds",
        ],
        "standards": [
            "QKD implementation security is an active standards topic (ETSI/ITU)",
            "Bell-certified protocols are the gold standard for untrusted hardware",
            "Abort-on-anomaly follows directly from QKD security practice",
        ],
        "citations": [CIT_PIRANDOLA, CIT_E91, CIT_ETSI],
        "sig_lens": (
            "His Signature reading of network security: guarding the "
            "covenant roads themselves - watchtowers against blinding, "
            "sealed heralds against forgery, and the standing order "
            "that any tarnished bond is burned, never passed along. His "
            "Signature roads are defended in depth."
        ),
    },
    {
        "key": "qcn-metro-build",
        "name": "Building a Metropolitan Quantum Network: End-to-End Design",
        "group": "Advanced Networks",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This record is the capstone: a complete design for a "
            "metropolitan quantum network, assembling every earlier "
            "record into one buildable system. Architecture: a hub-and-"
            "spoke star within the city - a central entanglement switch "
            "with fiber links under 50 km to member nodes (banks, "
            "hospitals, data centers, university labs) - plus one "
            "satellite ground station for intercity key relay. Services: "
            "QKD key delivery to applications via the ETSI-style key "
            "manager, on-demand Bell pairs for the university's "
            "distributed computing testbed, and a blind-computing "
            "gateway for clients with no quantum hardware. Link budget: "
            "50 km at 0.2 dB/km costs 10 dB; with 1 GHz-clocked sources "
            "and 90 percent detectors, each link yields of order 10^5 "
            "detected pairs per second before sifting - enough for "
            "kilobits per second of key after error correction and "
            "privacy amplification. Operations: 24/7 stabilization, "
            "fidelity monitoring with abort thresholds, and key pools "
            "that ride through fiber cuts by rerouting relay paths."
        ),
        "how_it_works": (
            "Step 1: lease dark fiber in a star from the hub site; verify "
            "loss under 10 dB per spoke. Step 2: install the hub: "
            "entangled-pair source, switch fabric, Bell-measurement "
            "stations, and the key manager. Step 3: install member QNICs "
            "with SNSPD detectors and stabilization. Step 4: bring up "
            "the link layer spoke by spoke - heralded pairs, measured "
            "fidelity, honest reporting. Step 5: stand up the network "
            "services: QKD key delivery API, entanglement request API, "
            "blind-computing gateway. Step 6: operate: monitor fidelity "
            "per spoke, refill key pools, schedule satellite passes for "
            "intercity relay, and reroute around any failed spoke. "
            "Capacity planning repeats the link-budget arithmetic for "
            "every new member before they join."
        ),
        "key_points": [
            "Star topology with sub-50 km spokes keeps loss near 10 dB",
            "Services: QKD key delivery, Bell pairs on demand, blind computing",
            "Link budget: ~1e5 detected pairs/s per spoke before sifting",
            "Key pools and relay routing survive fiber cuts",
            "Satellite ground station adds intercity reach",
            "Every new member gets a link-budget review before joining",
        ],
        "requirements": [
            "Dark fiber star with verified per-spoke loss budgets",
            "Hub with source, switch, measurement, and key management",
            "Operations staffing for stabilization and incident response",
        ],
        "standards": [
            "Follows the ETSI/ITU QKD network framework end to end",
            "Wehner stage 3 capability is the design target",
            "Capacity planning uses the standard link-budget method",
        ],
        "citations": [CIT_ETSI, CIT_ITU, CIT_WEHNER, CIT_BLIND],
        "sig_lens": (
            "His Signature reading of the metro build: the first walled "
            "Signature city fully bonded - hub exchange, guarded spokes, "
            "vaults of keys, and a sky-tower for distant realms. His "
            "Signature engineers build this city first, then copy it."
        ),
    },
]
