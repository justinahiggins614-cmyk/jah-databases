#!/usr/bin/env python3
"""Entries for The Unsolved Particle Physics Database (unsolved-particle-physics) and its
Signature half (unsolved-particle-physics-signature).

34 famous unsolved problems in particle physics, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USPP- / JAH-USPPS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "particle-physics",
 "disp": "particle physics",
 "name": "The Unsolved Particle Physics Database",
 "sig_name": "The Unsolved Particle Physics Signature Database",
 "prefix": "JAH-USPP-",
 "sig_prefix": "JAH-USPPS-",
 "ai": "JAH Unsolved Particle Physics Archivist",
 "tagline": ("Thirty-four famous open problems in particle physics, from the hierarchy problem to a unified "
             "theory: real, fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of particle "
                 "physics: Signature-generated proposed solutions with assumptions declared, confirm and refute "
                 "conditions stated, and limits honestly marked. Clearly labeled Signature-made, never established "
                 "science."),
 "pub_line": ("Public records - 34 famous open problems in particle physics, real and fact-checked: the hierarchy "
              "problem, the strong CP problem, neutrino masses and ordering, proton decay, magnetic monopoles, "
              "electroweak baryogenesis, the flavor problem, CKM unitarity, and the muon g-2 anomaly - every "
              "record carrying the problem statement, background, why it matters, key points, requirements, "
              "standards, citations, and a working solution-explorer demonstration, organized in the Signature "
              "system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "particle physics problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (hierarchy, strong CP, neutrino mass, "
                 "mass ordering, sterile neutrinos, proton decay, magnetic monopoles, electroweak baryogenesis, "
                 "flavor, CKM unitarity, muon g-2) -> Compounded (supersymmetry absence, naturalness, extra "
                 "dimensions, quantum gravity, black-hole information, proton radius, proton spin, glueballs, "
                 "quark-gluon plasma, confinement, Yang-Mills mass gap, axion quality) -> Advanced (light dark "
                 "matter, dark photons, fifth forces, lepton universality, B-meson anomalies, direct CP "
                 "violation, neutrinoless double beta decay, seesaw scale, grand unification, theory of "
                 "everything, unified particle physics)."),
 "search_ph": ("Search hierarchy, neutrinos, supersymmetry, dark matter, CP violation, confinement, unification..."),
 "chat_ph": "Ask about the great open problems of particle physics...",
 "greet_pub": ("I am the JAH Unsolved Particle Physics Archivist. Ask me about the great open problems of "
               "particle physics - from the hierarchy problem, neutrinos, and supersymmetry through confinement "
               "and CP violation, to dark matter, unification, and the theory of everything."),
 "greet_sig": ("I am the JAH Unsolved Particle Physics Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of particle physics - every approach labeled as "
               "a proposal, never established science."),
 "role_pub": ("unsolved particle physics archivist - the great open problems of particle physics, from the "
              "hierarchy problem, neutrinos, and supersymmetry through confinement and CP violation, to dark "
              "matter, unification, and the theory of everything; teaches progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - definition, example, "
              "analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved particle physics archivist - Signature editions: his original Signature solution method "
              "applied to the 34 great open problems of particle physics, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, "
              "math - using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved particle physics studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Particle Data Group, Review of Particle Physics; Peskin and Schroeder, Quantum Field Theory).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "pp-hierarchy",
 "name": "The Hierarchy Problem",
 "group": "Beyond Standard Model",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "The Higgs mass is 125 GeV, but quantum corrections want to drag it to the Planck scale - so why is the weak scale so light?",
 "background": "The hierarchy problem - the Higgs mass's quantum sensitivity to the highest scales (the Planck scale, 10^19 GeV) versus its measured 125 GeV - is the naturalness problem's flagship: the bare mass must cancel the corrections to ~1 part in 10^34. Supersymmetry, composite Higgs, and extra dimensions were invented largely to solve it - and the LHC has found none of them. The problem is either a clue to new physics at higher energies or a sign that naturalness is a bad guide. The light Higgs is either protected or tuned.",
 "why_it_matters": "The hierarchy problem drove decades of beyond-Standard-Model physics. Its resolution - or dissolution - decides the field's direction.",
 "sig_lens": "The Signature lens reads the hierarchy as a suspicious cancellation: the protocol must find the protector (new physics) or accept the tuning - by experiment, not taste.",
 "sig_solution": LABEL + " Assumptions: (1) 1-in-10^34 cancellation needed without new physics; (2) LHC found no protectors. Reasoning path: search the protector's hiding places - higher-energy colliders, precision Higgs couplings (deviations reveal compositeness), and cosmological probes. Proposed mechanism: a cancellation protocol with precision Higgs-coupling measurements, future-collider direct searches, and naturalness reconsidered only after the searches complete. Confirm: a protector found (superpartners, resonances, coupling deviations). Kill: all searches null and the tuning stands. Does NOT claim: the hierarchy's solution - it hunts the protector experimentally.",
 "pointer": "The Signature system's proposed approach hunts hierarchy protectors via precision Higgs and future colliders; the companion Signature Edition record specifies the cancellation protocol.",
 "key_points": [
  "Higgs at 125 GeV vs Planck-scale corrections: 1-in-10^34 tuning.",
  "SUSY, composite Higgs, extra dimensions invented to solve it.",
  "LHC found none of the expected protectors.",
  "Naturalness may be a bad guide.",
 ],
 "requirements": [
  "Precision Higgs-coupling deviation hunts.",
  "Future-collider direct protector searches.",
  "Naturalness judged after searches, not before.",
 ],
 "citations": [
  "Martin SP (1998) A supersymmetry primer. Perspectives on Supersymmetry.",
 ],
 "demo": {"e1": 45.0, "e2": 55.0, "theta_deg": 60.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "pp-strong-cp",
 "name": "The Strong CP Problem",
 "group": "Standard Model",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "QCD allows CP violation, but none is seen - so why is the theta angle essentially zero when it could be anything?",
 "background": "The strong CP problem - QCD's theta parameter could be order-one but measures < 10^-10 (from neutron electric-dipole-moment limits) - is the Standard Model's most elegant fine-tuning: the Peccei-Quinn solution (a new symmetry, predicting the axion) is beautiful and gives a dark-matter candidate; alternatives (massless up quark - excluded; Nelson-Barr) are less compelling. The axion hunt (ADMX, CASPEr, helioscopes) is the strong-CP hunt. The zero that should not be zero is either a symmetry or an accident.",
 "why_it_matters": "The strong CP zero is the Standard Model's most suspicious number. Its explanation - the axion - would also solve dark matter.",
 "sig_lens": "The Signature lens reads theta as a dial set to zero: the protocol must find who set it (Peccei-Quinn) or measure it ever more precisely.",
 "sig_solution": LABEL + " Assumptions: (1) theta < 1e-10 vs order-one natural; (2) axion is the leading explanation. Reasoning path: hunt the axion across its mass range and push EDM limits - either the symmetry is found or the tuning tightens. Proposed mechanism: a dial protocol with broadband axion searches (haloscopes, helioscopes, lab), next-generation neutron-EDM measurements, and axion-dark-matter cross-tests. Confirm: axion detected or theta bounded tighter. Kill: the full axion window excluded and no alternative. Does NOT claim: the theta solution - it hunts who set the dial.",
 "pointer": "The Signature system's proposed approach hunts the axion and tightens EDM limits; the companion Signature Edition record specifies the dial protocol.",
 "key_points": [
  "QCD theta < 1e-10; naturally order-one.",
  "Peccei-Quinn symmetry predicts the axion.",
  "Axion doubles as a dark-matter candidate.",
  "Neutron EDM limits set the bound.",
 ],
 "requirements": [
  "Broadband axion searches across mass ranges.",
  "Next-generation neutron-EDM measurements.",
  "Axion dark-matter cross-testing.",
 ],
 "citations": [
  "Peccei RD, Quinn HR (1977) CP conservation in the presence of pseudoparticles. PRL 38.",
 ],
 "demo": {"e1": 50.0, "e2": 50.0, "theta_deg": 90.0},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "pp-neutrino-mass",
 "name": "The Neutrino Mass Problem",
 "group": "Neutrinos",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Neutrinos have mass - but the Standard Model says they should not, so where does the mass come from?",
 "background": "The neutrino mass problem - oscillations prove neutrinos have mass, but the Standard Model's Higgs mechanism gives mass only to charged fermions (no right-handed neutrinos exist in the SM) - needs new physics: the seesaw mechanism (heavy right-handed neutrinos), radiative models, or extra dimensions. The absolute mass scale is unknown (KATRIN: < 0.8 eV; cosmology: sum < ~0.12 eV); the nature (Dirac vs Majorana) is unknown. The only confirmed beyond-Standard-Model physics is a mass without a mechanism.",
 "why_it_matters": "Neutrino mass is the only laboratory-confirmed new physics. Its mechanism is the first beyond-Standard-Model door.",
 "sig_lens": "The Signature lens reads neutrino mass as the confirmed crack: the protocol must find the mechanism behind the crack - Dirac, Majorana, or seesaw.",
 "sig_solution": LABEL + " Assumptions: (1) oscillations prove mass; SM cannot give it; (2) scale and nature unknown. Reasoning path: pin the scale (KATRIN, cosmology) and the nature (neutrinoless double beta decay) - the mechanism must fit both. Proposed mechanism: a crack protocol with absolute-mass measurements, Majorana-vs-Dirac tests, and seesaw-scale probes (collider, lepton-flavor violation). Confirm: scale and nature point to one mechanism. Kill: the scale goes to zero-ish and the nature stays hidden. Does NOT claim: the mass mechanism - it characterizes the crack fully.",
 "pointer": "The Signature system's proposed approach pins neutrino mass scale and nature; the companion Signature Edition record specifies the crack protocol.",
 "key_points": [
  "Oscillations prove mass; the SM cannot provide it.",
  "Absolute scale unknown (KATRIN < 0.8 eV).",
  "Dirac vs Majorana nature unknown.",
  "Only confirmed beyond-SM physics.",
 ],
 "requirements": [
  "Absolute neutrino-mass measurements.",
  "Neutrinoless-double-beta-decay Majorana tests.",
  "Seesaw-scale collider and LFV probes.",
 ],
 "citations": [
  "Super-Kamiokande Collaboration (1998) Evidence for oscillation of atmospheric neutrinos. PRL 81.",
 ],
 "demo": {"e1": 40.0, "e2": 60.0, "theta_deg": 45.0},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "pp-ordering",
 "name": "The Neutrino Mass Ordering Problem",
 "group": "Neutrinos",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Are neutrino masses ordered normally (lightest mostly electron) or inverted - and why does the ordering matter so much?",
 "background": "The mass-ordering problem - normal (m1 < m2 < m3) vs inverted (m3 < m1 < m2) - matters because the ordering sets the neutrinoless-double-beta-decay target (inverted guarantees a signal in next-gen experiments; normal may not), constrains flavor models, and affects supernova neutrino physics. Current hints favor normal ordering (~2-3 sigma from oscillations + cosmology) but are not definitive. JUNO (reactor) and DUNE/Hyper-K (long-baseline) will decide within the decade. The ordering is the neutrino sector's binary question.",
 "why_it_matters": "The ordering sets the double-beta-decay target and constrains every flavor model. The binary question gates the next decade's program.",
 "sig_lens": "The Signature lens reads the ordering as the neutrino family's seating chart: the protocol must seat them definitively - the experiments are already at the table.",
 "sig_solution": LABEL + " Assumptions: (1) hints favor normal at 2-3 sigma; (2) JUNO/DUNE/Hyper-K will decide. Reasoning path: let the experiments decide - support the complementary programs and prepare the physics for either answer. Proposed mechanism: a seating protocol with JUNO, DUNE, and Hyper-K each pursued, combined analyses, and theory ready for both orderings' implications. Confirm: the experiments converge on one ordering. Kill: they disagree and systematics dominate. Does NOT claim: the ordering - it seats the family by experiment.",
 "pointer": "The Signature system's proposed approach decides neutrino mass ordering with complementary experiments; the companion Signature Edition record specifies the seating protocol.",
 "key_points": [
  "Normal vs inverted ordering: the binary question.",
  "Ordering sets the double-beta-decay target.",
  "Hints favor normal at 2-3 sigma.",
  "JUNO, DUNE, Hyper-K will decide.",
 ],
 "requirements": [
  "Complementary ordering experiments pursued.",
  "Combined global analyses.",
  "Theory prepared for both outcomes.",
 ],
 "citations": [
  "DUNE Collaboration (2020) Deep Underground Neutrino Experiment design report.",
 ],
 "demo": {"e1": 55.0, "e2": 45.0, "theta_deg": 75.0},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "pp-sterile",
 "name": "The Sterile Neutrino Problem",
 "group": "Neutrinos",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Anomalies hint at a fourth, sterile neutrino - but do the hints survive, and what would a sterile neutrino mean?",
 "background": "The sterile-neutrino problem - LSND, MiniBooNE, reactor, and gallium anomalies each hinting at eV-scale sterile neutrinos - is the neutrino field's longest-running controversy: MicroBooNE's null results challenged MiniBooNE; reactor anomaly re-evaluations weakened that hint; yet the gallium anomaly persists. A sterile neutrino would be new physics (a right-handed singlet) with cosmological consequences (N_eff). The anomalies may be systematics or the first sighting - the field is split. The fourth neutrino is the most wanted and most doubted particle.",
 "why_it_matters": "A sterile neutrino would be new physics beyond the three flavors. The anomalies are either systematics or the first sighting - the split must be resolved.",
 "sig_lens": "The Signature lens reads the sterile hints as a disputed sighting: the protocol must run the definitive lineup (short-baseline program) and accept the verdict.",
 "sig_solution": LABEL + " Assumptions: (1) anomalies individually challenged; gallium persists; (2) field split. Reasoning path: run the definitive test - the Fermilab short-baseline program (SBND, MicroBooNE, ICARUS) covers the LSND region decisively. Proposed mechanism: a lineup protocol completing the short-baseline program, global fits including nulls, and cosmological N_eff cross-checks. Confirm: the program sees or excludes decisively. Kill: results stay ambiguous. Does NOT claim: the sterile neutrino - it runs the lineup.",
 "pointer": "The Signature system's proposed approach resolves sterile neutrinos with the short-baseline program; the companion Signature Edition record specifies the lineup protocol.",
 "key_points": [
  "LSND, MiniBooNE, reactor, gallium anomalies hint at eV sterile.",
  "MicroBooNE nulls challenged MiniBooNE.",
  "Gallium anomaly persists.",
  "A sterile neutrino would reshape N_eff cosmology.",
 ],
 "requirements": [
  "Complete Fermilab short-baseline program.",
  "Global fits including null results.",
  "Cosmological N_eff cross-checks.",
 ],
 "citations": [
  "MicroBooNE Collaboration (2022) Search for neutrino-induced neutral-current excess. PRL 128.",
 ],
 "demo": {"e1": 48.0, "e2": 52.0, "theta_deg": 30.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "pp-proton-decay",
 "name": "The Proton Decay Problem",
 "group": "Unification",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Grand unified theories say protons must decay - but no proton has ever been seen to decay, so how long do they live, and what does the limit mean?",
 "background": "Proton decay - the GUT prediction that baryon number is violated at high scales - has never been observed: Super-Kamiokande sets lifetimes > 10^34 years (for p -> e+ pi0), killing minimal SU(5) and constraining every GUT. But the non-observation is itself the result: each decade of lifetime excludes model classes. Hyper-Kamiokande and DUNE will push further. The proton's stability is either baryon-number conservation as law or GUT scales beyond reach. The longest-lived particle is the quietest test of unification.",
 "why_it_matters": "Proton decay is grand unification's cleanest prediction. The lifetime limit is the unification scale's lower bound.",
 "sig_lens": "The Signature lens reads the proton as the patient immortal: the protocol must keep watching - each decade of life excludes another would-be killer (model).",
 "sig_solution": LABEL + " Assumptions: (1) no decay seen; limits > 1e34 yr; (2) minimal SU(5) dead. Reasoning path: push the watch - Hyper-K and DUNE extend the lifetime reach; each null result constrains the GUT landscape. Proposed mechanism: a watch protocol with next-generation decay searches, model-survey updates per limit, and GUT model-building on the surviving space. Confirm: decay seen (unification's triumph) or limits exclude the minimal landscape. Kill: limits stall and the scale stays unreachable. Does NOT claim: proton decay - it keeps the watch.",
 "pointer": "The Signature system's proposed approach pushes proton-decay lifetime limits with next-gen detectors; the companion Signature Edition record specifies the watch protocol.",
 "key_points": [
  "No proton decay observed; lifetime > 1e34 years.",
  "Minimal SU(5) excluded by the limit.",
  "Each null decade constrains GUT classes.",
  "Hyper-K and DUNE will push further.",
 ],
 "requirements": [
  "Next-generation decay searches.",
  "GUT landscape updates per limit.",
  "Model-building on surviving space.",
 ],
 "citations": [
  "Super-Kamiokande Collaboration (2020) Search for proton decay. PRD 102.",
 ],
 "demo": {"e1": 60.0, "e2": 40.0, "theta_deg": 90.0},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "pp-monopole",
 "name": "The Magnetic Monopole Problem",
 "group": "Unification",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Maxwell's equations would be symmetric with magnetic charges - but no magnetic monopole has ever been found, so where are they?",
 "background": "The magnetic-monopole problem - Dirac's quantization argument and GUTs both predict monopoles, yet none observed - is solved partially by inflation (diluting primordial monopoles beyond detection), but the solution assumes inflation; non-inflationary cosmologies need another answer. Searches (MACRO, IceCube, MoEDAL at the LHC) set flux limits; the Parker bound limits galactic flux. A found monopole would confirm Dirac quantization and GUTs spectacularly. The most beautiful predicted particle is the most absent.",
 "why_it_matters": "Monopoles would symmetrize electromagnetism and confirm GUTs. Their absence is either inflation's success or the prediction's failure.",
 "sig_lens": "The Signature lens reads monopoles as the predicted guest who never arrived: the protocol must check whether the invitation (inflation) explains the absence, or the guest was never real.",
 "sig_solution": LABEL + " Assumptions: (1) Dirac and GUTs predict monopoles; (2) inflation dilutes them - conditionally. Reasoning path: keep searching the plausible windows (cosmic, collider, trapped) while testing inflation's dilution account. Proposed mechanism: a guest protocol with continued monopole searches (IceCube, MoEDAL, induction), Parker-bound-respecting flux limits, and inflation-model constraints from the non-observation. Confirm: a monopole found. Kill: searches exhaust the windows. Does NOT claim: monopoles exist - it checks the invitation.",
 "pointer": "The Signature system's proposed approach continues monopole searches while testing inflation's dilution; the companion Signature Edition record specifies the guest protocol.",
 "key_points": [
  "Dirac quantization and GUTs predict monopoles.",
  "None observed; inflation dilutes them (conditionally).",
  "MACRO, IceCube, MoEDAL set flux limits.",
  "A found monopole would confirm GUTs spectacularly.",
 ],
 "requirements": [
  "Continued cosmic, collider, and induction searches.",
  "Flux limits against the Parker bound.",
  "Inflation constraints from non-observation.",
 ],
 "citations": [
  "Dirac PAM (1931) Quantised singularities in the electromagnetic field. Proc. Roy. Soc. A 133.",
 ],
 "demo": {"e1": 42.0, "e2": 58.0, "theta_deg": 120.0},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "pp-ew-baryogenesis",
 "name": "The Electroweak Baryogenesis Problem",
 "group": "Early Universe",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Could the matter-antimatter asymmetry have been made at the electroweak phase transition - and what new physics would that require?",
 "background": "Electroweak baryogenesis - making the asymmetry at the ~100 GeV phase transition - is the most testable baryogenesis scenario (it happens at collider-accessible energies), but the Standard Model fails it: the phase transition is a smooth crossover (not first-order), and SM CP violation is far too small. Extensions (singlet-extended Higgs, two-Higgs-doublet models) can fix both - and predict observable consequences: modified Higgs couplings, new scalars, gravitational waves from the transition. EDM limits already squeeze the CP-violation sources. The testable baryogenesis is cornered but alive.",
 "why_it_matters": "Electroweak baryogenesis would make the universe's matter at collider energies - the most testable origin story, and the most constrained.",
 "sig_lens": "The Signature lens reads electroweak baryogenesis as the origin story told at our energy: the protocol must check whether the stage (first-order transition) and the actors (new CP violation) exist.",
 "sig_solution": LABEL + " Assumptions: (1) SM transition is crossover; SM CP too small; (2) extensions predict observables. Reasoning path: test the requirements - hunt extended Higgs sectors (colliders), new CP violation (EDMs), and phase-transition gravitational waves. Proposed mechanism: a stage protocol with collider searches for extended scalars, EDM pushes on CP sources, and gravitational-wave probes of the transition. Confirm: the stage and actors found. Kill: EDMs exclude the CP sources. Does NOT claim: electroweak baryogenesis - it checks the stage.",
 "pointer": "The Signature system's proposed approach tests electroweak baryogenesis requirements at colliders and EDMs; the companion Signature Edition record specifies the stage protocol.",
 "key_points": [
  "Most testable baryogenesis scenario (100 GeV scale).",
  "SM fails: crossover transition, tiny CP violation.",
  "Extensions predict new scalars and gravitational waves.",
  "EDM limits squeeze the CP sources.",
 ],
 "requirements": [
  "Collider hunts for extended Higgs sectors.",
  "EDM measurements of new CP violation.",
  "Gravitational-wave transition probes.",
 ],
 "citations": [
  "Morrissey DE, Ramsey-Musolf MJ (2012) Electroweak baryogenesis. New Journal of Physics 14.",
 ],
 "demo": {"e1": 52.0, "e2": 48.0, "theta_deg": 65.0},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "pp-flavor",
 "name": "The Flavor Problem",
 "group": "Standard Model",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Why three generations of matter, with the bizarre mass hierarchy from electron to top - and what sets the mixing angles?",
 "background": "The flavor problem - three generations, masses spanning 12 orders (electron to top), mixing angles (CKM small, PMNS large) unexplained - is the Standard Model's ugliest sector: the Yukawa couplings are 22 free parameters fitted, not predicted. Flavor symmetries, Froggatt-Nielsen, extra dimensions, and string models each try to derive the pattern; none is confirmed. The flavor anomalies (B-decays, g-2) may be the first beyond-SM flavor physics. The periodic table of particles has no Mendeleev - the pattern is data without theory.",
 "why_it_matters": "Flavor is most of the Standard Model's parameters. The unexplained pattern is the theory's biggest ugliness - and the anomalies' home.",
 "sig_lens": "The Signature lens reads flavor as a code without a key: the protocol must gather more ciphertext (precision flavor data) and test the proposed keys.",
 "sig_solution": LABEL + " Assumptions: (1) 22 Yukawa parameters fitted, not predicted; (2) flavor models unconfirmed. Reasoning path: over-constrain the pattern - precision CKM/PMNS, rare decays, and anomaly follow-ups - and test flavor-symmetry predictions. Proposed mechanism: a code protocol with precision flavor-factory measurements (Belle II, LHCb), rare-decay hunts, and flavor-model predictions tested on the full pattern. Confirm: one key decodes the pattern. Kill: the pattern stays parametric. Does NOT claim: the flavor theory - it gathers ciphertext and tests keys.",
 "pointer": "The Signature system's proposed approach over-constrains flavor with precision factories; the companion Signature Edition record specifies the code protocol.",
 "key_points": [
  "Three generations; masses span 12 orders of magnitude.",
  "22 Yukawa parameters are fitted, not predicted.",
  "CKM mixing small; PMNS mixing large - unexplained.",
  "Flavor models (symmetries, FN) unconfirmed.",
 ],
 "requirements": [
  "Precision flavor-factory measurements.",
  "Rare-decay and anomaly follow-ups.",
  "Flavor-model predictions on the full pattern.",
 ],
 "citations": [
  "Froggatt CD, Nielsen HB (1979) Hierarchy of quark masses. Nuclear Physics B 147.",
 ],
 "demo": {"e1": 46.0, "e2": 54.0, "theta_deg": 80.0},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "pp-ckm",
 "name": "The CKM Unitarity Problem",
 "group": "Standard Model",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "The quark mixing matrix should be unitary - but the first-row measurements do not quite add up, so is it new physics or underestimated uncertainties?",
 "background": "The CKM unitarity problem (the Cabibbo-angle anomaly) - |Vud|^2 + |Vus|^2 + |Vub|^2 = 0.9985(5), ~3 sigma below 1 - is the precision frontier's sharpest tension: Vud from superallowed beta decays, Vus from kaon decays, each with theory uncertainties (radiative corrections, lattice inputs) that are contested. New physics (right-handed currents, exotic fermions) could explain it; underestimated uncertainties could dissolve it. The unitarity test is the Standard Model's audit - and the books do not quite balance.",
 "why_it_matters": "CKM unitarity is the Standard Model's audit. A 3-sigma imbalance is either new physics or the audit's error - the precision frontier's verdict.",
 "sig_lens": "The Signature lens reads CKM unitarity as the audit: the protocol must recheck the bookkeeping (radiative corrections, lattice) before declaring embezzlement (new physics).",
 "sig_solution": LABEL + " Assumptions: (1) 3-sigma first-row deficit; (2) theory uncertainties contested. Reasoning path: audit the books - improve the radiative corrections and lattice inputs independently, and test new-physics explanations on their other predictions. Proposed mechanism: an audit protocol with independent Vud/Vus determinations, theory-uncertainty reduction programs, and new-physics candidates tested broadly. Confirm: the deficit survives improved bookkeeping. Kill: it dissolves into uncertainties. Does NOT claim: new physics - it rechecks the books first.",
 "pointer": "The Signature system's proposed approach re-audits CKM unitarity with improved theory inputs; the companion Signature Edition record specifies the audit protocol.",
 "key_points": [
  "First-row CKM sum 0.9985(5): ~3 sigma below unity.",
  "Vud from beta decays; Vus from kaon decays.",
  "Radiative-correction and lattice uncertainties contested.",
  "Right-handed currents could explain it.",
 ],
 "requirements": [
  "Independent Vud and Vus determinations.",
  "Theory-uncertainty reduction programs.",
  "New-physics candidates tested broadly.",
 ],
 "citations": [
  "Seng CY et al. (2020) Reduced hadronic uncertainty in the CKM unitarity test. PRL 124.",
 ],
 "demo": {"e1": 58.0, "e2": 42.0, "theta_deg": 55.0},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "pp-g2",
 "name": "The Muon g-2 Problem",
 "group": "Precision",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "The muon's magnetic moment disagrees with theory - but is the discrepancy new physics, or is the theory's hadronic part miscalculated?",
 "background": "The muon g-2 problem - Fermilab's measurement vs Standard Model prediction, ~4-5 sigma with data-driven hadronic vacuum polarization - is the precision anomaly of the decade: but lattice-QCD calculations (BMW) of the hadronic part shrink the discrepancy, and CMD-3 e+e- data disagree with earlier datasets. The discrepancy's fate hinges on the hadronic contribution - the theory's hardest part. New physics (SUSY, dark photons, leptoquarks) would love the gap; the gap may be hadronic. The most exciting number is the most contested calculation.",
 "why_it_matters": "Muon g-2 is the decade's precision anomaly. Its fate - new physics or hadronic error - is the precision frontier's verdict.",
 "sig_lens": "The Signature lens reads g-2 as the contested score: the protocol must settle the hadronic calculation (lattice vs data-driven) before awarding the new-physics prize.",
 "sig_solution": LABEL + " Assumptions: (1) 4-5 sigma with data-driven HVP; (2) lattice BMW shrinks it; datasets disagree. Reasoning path: settle the hadronic part - resolve the lattice vs data-driven vs CMD-3 disagreements - then read the verdict. Proposed mechanism: a score protocol with hadronic-contribution reconciliation programs, improved e+e- cross-section data, and new-physics interpretations gated on the settled theory. Confirm: the discrepancy survives reconciliation. Kill: it dissolves into hadronic error. Does NOT claim: new physics - it settles the score first.",
 "pointer": "The Signature system's proposed approach reconciles the muon g-2 hadronic contribution; the companion Signature Edition record specifies the score protocol.",
 "key_points": [
  "Fermilab vs data-driven SM: ~4-5 sigma.",
  "Lattice BMW result shrinks the discrepancy.",
  "CMD-3 e+e- data disagree with earlier sets.",
  "Hadronic vacuum polarization is the contested part.",
 ],
 "requirements": [
  "Hadronic-contribution reconciliation (lattice vs data).",
  "Improved e+e- cross-section measurements.",
  "New-physics claims gated on settled theory.",
 ],
 "citations": [
  "Muon g-2 Collaboration (2023) Measurement of the positive muon anomalous magnetic moment. PRL 131.",
 ],
 "demo": {"e1": 44.0, "e2": 56.0, "theta_deg": 70.0},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "pp-susy-absence",
 "name": "The Supersymmetry Absence Problem",
 "group": "Beyond Standard Model",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Supersymmetry was the great hope - but the LHC found no superpartners, so is SUSY dead, hiding, or simply at higher energies?",
 "background": "The supersymmetry absence problem - the LHC's null results excluding the 'natural' SUSY spectrum (stops below ~TeV) - killed the paradigm's most attractive versions: the remaining SUSY is split, compressed, or heavy - less motivated, harder to test. But SUSY's other virtues (gauge-coupling unification, dark-matter candidate, string theory's need) survive the LHC. The absence is either the paradigm's falsification or its relocation to higher energies. The great hope is unconfirmed, not disproven.",
 "why_it_matters": "SUSY was particle physics' dominant paradigm for decades. Its absence redirects the field - or relocates the hope.",
 "sig_lens": "The Signature lens reads SUSY as the missing heir: the protocol must search the remaining estates (compressed, split, heavy) before declaring the line extinct.",
 "sig_solution": LABEL + " Assumptions: (1) natural SUSY excluded; (2) split/compressed/heavy variants survive. Reasoning path: search the remaining hiding places - compressed spectra, long-lived particles, precision unification tests - and weigh the virtues against the fine-tuning cost. Proposed mechanism: an heir protocol with targeted exotic-SUSY searches, gauge-unification precision tests, and paradigm reassessment on the full search record. Confirm: superpartners found in hiding. Kill: the hiding places empty and the virtues insufficient. Does NOT claim: SUSY's fate - it searches the estates.",
 "pointer": "The Signature system's proposed approach searches remaining SUSY hiding places; the companion Signature Edition record specifies the heir protocol.",
 "key_points": [
  "LHC excluded natural SUSY spectra.",
  "Split, compressed, heavy variants survive.",
  "Unification, dark matter, string virtues survive.",
  "Absence is unfalsified, not disproven.",
 ],
 "requirements": [
  "Compressed-spectrum and long-lived-particle searches.",
  "Gauge-unification precision tests.",
  "Paradigm reassessment on full search record.",
 ],
 "citations": [
  "ATLAS and CMS SUSY search summaries (2024).",
 ],
 "demo": {"e1": 62.0, "e2": 38.0, "theta_deg": 85.0},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "pp-naturalness",
 "name": "The Naturalness Problem",
 "group": "Beyond Standard Model",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Physics long assumed parameters should be 'natural' - but the LHC's null results challenge the principle itself, so is naturalness a law or a prejudice?",
 "background": "The naturalness problem - the principle that dimensionless parameters should be order-one, which motivated SUSY, technicolor, and more - is in crisis: the LHC found the Higgs light but no naturalness-restoring physics, and the cosmological constant violates naturalness by 120 orders. Responses split: abandon naturalness (anthropic/multiverse), postpone it (new physics at higher scales), or reformulate it (new naturalness measures). The principle that guided the field may have been a prejudice. The null results are naturalness's trial.",
 "why_it_matters": "Naturalness guided decades of theory. If it was prejudice, the field's compass needs replacing.",
 "sig_lens": "The Signature lens reads naturalness as the field's compass: the protocol must check whether the compass pointed to treasure (it found the Higgs mass scale argued) or to nowhere - by results, not loyalty.",
 "sig_solution": LABEL + " Assumptions: (1) LHC nulls challenge naturalness; (2) CC violates it by 120 orders. Reasoning path: judge the compass by results - keep what worked (the Higgs scale argument had successes), test alternatives (relaxion, N-naturalness), and let experiment arbitrate. Proposed mechanism: a compass protocol with alternative-naturalness model tests, continued protector searches, and principle-reassessment tied to experimental outcomes. Confirm: a new principle predicts successfully. Kill: no principle works and model-building goes anthropic. Does NOT claim: naturalness dead or alive - it judges by results.",
 "pointer": "The Signature system's proposed approach tests naturalness alternatives experimentally; the companion Signature Edition record specifies the compass protocol.",
 "key_points": [
  "Naturalness motivated SUSY, technicolor, composite Higgs.",
  "LHC found no naturalness-restoring physics.",
  "Cosmological constant violates naturalness 1e120.",
  "Responses: abandon, postpone, or reformulate.",
 ],
 "requirements": [
  "Alternative-naturalness model tests.",
  "Continued protector searches.",
  "Principle reassessment on experimental outcomes.",
 ],
 "citations": [
  "Giudice GF (2013) Naturalness after LHC8. arXiv:1307.7879.",
 ],
 "demo": {"e1": 50.0, "e2": 50.0, "theta_deg": 100.0},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "pp-extra-dim",
 "name": "The Extra Dimensions Problem",
 "group": "Beyond Standard Model",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "String theory needs extra dimensions - but where are they, how big, and how would we know?",
 "background": "The extra-dimensions problem - ADD (large extra dimensions), Randall-Sundrum (warped), universal extra dimensions - predicts signatures: Kaluza-Klein towers, missing energy, microscopic black holes, deviations from Newton's law at short distances. The LHC and torsion-balance experiments have pushed limits: large extra dimensions below ~microns excluded for two flat ones; warped scales pushed up. But the string landscape's compactifications remain untestable in detail. The dimensions are either tiny, warped away, or absent - the tests keep pushing, never quite reaching.",
 "why_it_matters": "Extra dimensions are string theory's core prediction. Their non-observation bounds the theory's hiding places.",
 "sig_lens": "The Signature lens reads extra dimensions as hidden rooms: the protocol must keep knocking on the walls (short-distance gravity, collider KK) and map where the rooms are not.",
 "sig_solution": LABEL + " Assumptions: (1) limits pushed: microns (gravity), TeV (colliders); (2) string compactifications untestable in detail. Reasoning path: map the exclusion - push short-distance gravity tests and collider KK searches, and demand compactification models make testable predictions. Proposed mechanism: a rooms protocol with next-gen short-distance gravity tests, collider resonance hunts, and compactification-model testability requirements. Confirm: a hidden room found. Kill: the exclusions cover the motivated space. Does NOT claim: extra dimensions - it maps where they are not.",
 "pointer": "The Signature system's proposed approach maps extra-dimension exclusions with gravity and collider tests; the companion Signature Edition record specifies the rooms protocol.",
 "key_points": [
  "ADD, Randall-Sundrum, UED predict KK towers and missing energy.",
  "Short-distance gravity tested to microns.",
  "Collider limits push warped scales up.",
  "String compactifications remain untestable in detail.",
 ],
 "requirements": [
  "Next-generation short-distance gravity tests.",
  "Collider Kaluza-Klein resonance hunts.",
  "Testability requirements on compactifications.",
 ],
 "citations": [
  "Arkani-Hamed N et al. (1998) The hierarchy problem and new dimensions at a millimeter. Physics Letters B 436.",
 ],
 "demo": {"e1": 47.0, "e2": 53.0, "theta_deg": 40.0},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "pp-qg",
 "name": "The Quantum Gravity Problem",
 "group": "Beyond Standard Model",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "General relativity and quantum mechanics are incompatible - but what is the quantum theory of gravity, and how can it be tested?",
 "background": "The quantum-gravity problem - quantizing GR gives a non-renormalizable theory; the candidates (string theory, loop quantum gravity, asymptotic safety, causal sets) are mathematically developed but experimentally remote: the Planck scale (10^19 GeV) is unreachable. Phenomenology hunts for low-energy imprints: Lorentz-invariance violation (gamma-ray bursts), modified dispersion, black-hole echoes. The problem is the deepest in physics - and the least testable. The theories proliferate; the experiments strain.",
 "why_it_matters": "Quantum gravity is the unification of physics' two pillars. Its testability gap is the field's deepest methodological crisis.",
 "sig_lens": "The Signature lens reads quantum gravity as the unreachable summit: the protocol must build base camps (phenomenology) and demand every route show its handholds (testable predictions).",
 "sig_solution": LABEL + " Assumptions: (1) Planck scale unreachable directly; (2) candidates lack testable predictions. Reasoning path: build the phenomenology - hunt low-energy imprints (LIV, echoes, modified dispersion) and require candidate theories to predict them. Proposed mechanism: a summit protocol with quantum-gravity phenomenology programs, candidate-theory prediction requirements, and analogue/lower-scale tests where available. Confirm: an imprint found matching one candidate. Kill: no imprints and the candidates stay untestable. Does NOT claim: quantum gravity - it builds base camps.",
 "pointer": "The Signature system's proposed approach hunts quantum-gravity phenomenology imprints; the companion Signature Edition record specifies the summit protocol.",
 "key_points": [
  "Quantizing GR is non-renormalizable.",
  "String, LQG, asymptotic safety lack experimental tests.",
  "Planck scale (1e19 GeV) unreachable directly.",
  "Phenomenology: LIV, echoes, modified dispersion.",
 ],
 "requirements": [
  "Low-energy quantum-gravity imprint hunts.",
  "Testable-prediction requirements on candidates.",
  "Analogue and lower-scale tests.",
 ],
 "citations": [
  "Rovelli C (2004) Quantum Gravity. Cambridge University Press.",
 ],
 "demo": {"e1": 55.0, "e2": 45.0, "theta_deg": 110.0},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "pp-bh-info",
 "name": "The Black Hole Information Paradox",
 "group": "Beyond Standard Model",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Black holes evaporate - but does the information that fell in come out, and if so, how?",
 "background": "The black-hole information paradox - Hawking radiation appears thermal (information destroyed, violating quantum mechanics) - has evolved: the Page curve (entanglement entropy must fall) is now derived in toy models via replica wormholes/islands - but the derivation's assumptions (ensemble averaging, replica trick) are debated, and the physical mechanism (how the information gets out) remains mysterious. Firewalls, fuzzballs, and complementarity compete. The paradox is quantum gravity's sharpest thought experiment - and its resolution is claimed but not settled.",
 "why_it_matters": "The paradox pits quantum mechanics against general relativity at their sharpest. Its resolution is quantum gravity's Rosetta stone.",
 "sig_lens": "The Signature lens reads the paradox as the locked room: the protocol must find how the information escapes - demanding the mechanism, not just the entropy curve.",
 "sig_solution": LABEL + " Assumptions: (1) Page curve derived in toy models; (2) mechanism mysterious; assumptions debated. Reasoning path: demand the mechanism - test the competing proposals (firewalls, fuzzballs, islands) on distinctive predictions like echoes or microstructure. Proposed mechanism: a locked-room protocol with black-hole-echo searches (LIGO/Virgo), fuzzball/complementarity prediction tests, and replica-derivation assumption audits. Confirm: a mechanism's predictions verified. Kill: no distinctive predictions testable. Does NOT claim: the paradox resolved - it demands the escape route.",
 "pointer": "The Signature system's proposed approach tests black-hole information proposals on distinctive predictions; the companion Signature Edition record specifies the locked-room protocol.",
 "key_points": [
  "Hawking radiation appears thermal; information seemingly lost.",
  "Page curve derived via islands/replicas - assumptions debated.",
  "Firewalls, fuzzballs, complementarity compete.",
  "The physical escape mechanism remains mysterious.",
 ],
 "requirements": [
  "Black-hole-echo searches in gravitational waves.",
  "Proposal-specific prediction tests.",
  "Audits of replica-derivation assumptions.",
 ],
 "citations": [
  "Hawking SW (1976) Breakdown of predictability in gravitational collapse. PRD 14.",
 ],
 "demo": {"e1": 60.0, "e2": 40.0, "theta_deg": 95.0},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "pp-proton-radius",
 "name": "The Proton Radius Puzzle",
 "group": "Precision",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Muonic hydrogen says the proton is smaller than electronic measurements say - but which atom is right, and why do they disagree?",
 "background": "The proton-radius puzzle - muonic hydrogen spectroscopy giving 0.841 fm vs electronic (hydrogen spectroscopy + electron scattering) 0.877 fm, a 5-sigma gap - challenged QED and the Rydberg constant: new measurements (PRad electron scattering, new hydrogen spectroscopy) now favor the smaller value, suggesting the electronic extractions had systematics. But the resolution is not fully settled: two-photon-exchange corrections and scattering systematics are still debated. The puzzle shrank but the lesson stands: the proton's size was mismeasured by the standard methods.",
 "why_it_matters": "The proton's radius anchors the Rydberg constant and atomic physics. A 5-sigma atomic disagreement was the precision frontier's embarrassment.",
 "sig_lens": "The Signature lens reads the puzzle as two rulers disagreeing: the protocol must calibrate both rulers (systematics) before declaring new physics.",
 "sig_solution": LABEL + " Assumptions: (1) 5-sigma muonic vs electronic gap; (2) new data favors smaller value. Reasoning path: finish the calibration - resolve the two-photon-exchange and scattering systematics definitively. Proposed mechanism: a rulers protocol with next-generation electron-scattering (PRad-style), muonic-atom cross-checks, and two-photon-exchange theory completion. Confirm: the rulers agree with understood systematics. Kill: the gap persists and new physics returns. Does NOT claim: the puzzle solved - it calibrates the rulers.",
 "pointer": "The Signature system's proposed approach calibrates proton-radius systematics definitively; the companion Signature Edition record specifies the rulers protocol.",
 "key_points": [
  "Muonic hydrogen: 0.841 fm; electronic: 0.877 fm (5 sigma).",
  "New PRad and spectroscopy favor the smaller value.",
  "Two-photon exchange corrections debated.",
  "The puzzle shrank; systematics lesson stands.",
 ],
 "requirements": [
  "Next-generation electron-scattering measurements.",
  "Muonic-atom cross-checks.",
  "Two-photon-exchange theory completion.",
 ],
 "citations": [
  "Pohl R et al. (2010) The size of the proton. Nature 466.",
 ],
 "demo": {"e1": 43.0, "e2": 57.0, "theta_deg": 50.0},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "pp-proton-spin",
 "name": "The Proton Spin Problem",
 "group": "QCD",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "The proton's spin is 1/2 - but quarks carry only a fraction, so where is the rest: gluons, orbital motion, or both?",
 "background": "The proton-spin problem (the 'spin crisis', EMC 1988) - quarks carry ~30% of the proton's spin - launched decades of polarized DIS: gluon polarization (RHIC spin: modest, uncertain), quark/gluon orbital angular momentum (GPDs, TMDs - the frontier), each hard to pin down. The spin sum rule must balance, but the decomposition is scheme-dependent. The Electron-Ion Collider (EIC) is built largely to solve it: mapping the gluon spin and orbital contributions. The proton's spin is accounted for in pieces - the ledger does not yet balance.",
 "why_it_matters": "The proton's spin is its defining quantum number. The unbalanced ledger is QCD's structural mystery.",
 "sig_lens": "The Signature lens reads the spin as an unbalanced ledger: the protocol must audit every entry - quarks, gluons, orbital - until it balances.",
 "sig_solution": LABEL + " Assumptions: (1) quarks ~30%; gluons modest/uncertain; orbital unknown; (2) decomposition scheme-dependent. Reasoning path: complete the audit - EIC measurements of gluon spin and orbital angular momentum (GPDs/TMDs). Proposed mechanism: a ledger protocol with EIC spin-structure program, global polarized-PDF fits, and scheme-consistent decompositions. Confirm: the spin sums to 1/2 with all entries measured. Kill: the entries stay scheme-mired. Does NOT claim: the spin's location - it audits until balanced.",
 "pointer": "The Signature system's proposed approach completes the proton-spin audit with the EIC; the companion Signature Edition record specifies the ledger protocol.",
 "key_points": [
  "Quarks carry ~30% of proton spin (EMC 1988).",
  "Gluon polarization modest and uncertain.",
  "Orbital angular momentum is the frontier (GPDs, TMDs).",
  "Decomposition is scheme-dependent.",
 ],
 "requirements": [
  "EIC spin-structure measurements.",
  "Global polarized-PDF fits.",
  "Scheme-consistent spin decompositions.",
 ],
 "citations": [
  "Ashman J et al. (EMC) (1988) A measurement of the spin asymmetry. Physics Letters B 206.",
 ],
 "demo": {"e1": 51.0, "e2": 49.0, "theta_deg": 60.0},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "pp-glueball",
 "name": "The Glueball Problem",
 "group": "QCD",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "QCD predicts bound states of pure glue - but which observed mesons are glueballs, and why are they so hard to identify?",
 "background": "The glueball problem - QCD's prediction of gluonic bound states (no quarks) - is the theory's unconfirmed signature: lattice QCD predicts the spectrum (scalar ~1.7 GeV lightest), but the observed scalars (f0(1370), f0(1500), f0(1710)) mix glue with quark-antiquark, and the mixing is unresolvable with current data. Candidates come and go; none is confirmed pure glue. BESIII, GlueX, and PANDA hunt the spectrum. The pure-glue states are QCD's prediction awaiting its particle.",
 "why_it_matters": "Glueballs are QCD's unique prediction - bound states of the force itself. Their confirmation is the theory's signature.",
 "sig_lens": "The Signature lens reads glueballs as the force's own particles: the protocol must separate the glue from the quark mixture - by decay patterns the mixing cannot fake.",
 "sig_solution": LABEL + " Assumptions: (1) lattice predicts spectrum; (2) observed scalars mix glue with qqbar unresolvably. Reasoning path: find the mixing-proof signatures - decay patterns (flavor-blind decays) and production mechanisms distinctive of glue. Proposed mechanism: a glue protocol with high-statistics scalar spectroscopy (BESIII, GlueX, PANDA), mixing analyses on decay patterns, and lattice predictions as falsifiable targets. Confirm: a state matches glueball predictions mixing-proof. Kill: all candidates prove mixed. Does NOT claim: a glueball found - it separates glue from mixture.",
 "pointer": "The Signature system's proposed approach identifies glueballs via mixing-proof decay signatures; the companion Signature Edition record specifies the glue protocol.",
 "key_points": [
  "QCD predicts pure-glue bound states.",
  "Lattice: lightest scalar ~1.7 GeV.",
  "Observed scalars mix glue with quark-antiquark.",
  "No confirmed pure-glue state.",
 ],
 "requirements": [
  "High-statistics scalar spectroscopy.",
  "Mixing analyses on decay patterns.",
  "Lattice predictions as falsifiable targets.",
 ],
 "citations": [
  "Morningstar CJ, Peardon M (1999) The glueball spectrum from an anisotropic lattice study. PRD 60.",
 ],
 "demo": {"e1": 56.0, "e2": 44.0, "theta_deg": 75.0},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "pp-qgp",
 "name": "The Quark Gluon Plasma Problem",
 "group": "QCD",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Heavy-ion collisions make quark-gluon plasma - but is it really a near-perfect liquid, and what are its exact properties?",
 "background": "The quark-gluon plasma problem - characterizing the QGP's transport properties (shear viscosity, jet quenching parameter q-hat) - advanced hugely: RHIC/LHC flow measurements show a near-perfect liquid (eta/s near the KSS bound), but the temperature dependence, the small-system question (do pp/pA make QGP?), and the hadronization mechanism are open. The viscosity's exact value and the plasma's weakly-vs-strongly-coupled nature at different temperatures are debated. The hottest fluid ever made is characterized approximately.",
 "why_it_matters": "The QGP is the early universe's matter recreated. Its exact properties are the Big Bang's first microsecond, measured.",
 "sig_lens": "The Signature lens reads the QGP as the universe's first fluid: the protocol must measure its viscosity's temperature curve - the fluid's fingerprint.",
 "sig_solution": LABEL + " Assumptions: (1) near-perfect liquid established; (2) temperature dependence, small systems open. Reasoning path: map the properties vs temperature - Bayesian inference on flow data, jet-quenching tomography, and small-system tests. Proposed mechanism: a fluid protocol with Bayesian QGP property extraction, jet-tomography programs, and small-system QGP tests. Confirm: the properties mapped vs temperature. Kill: the small systems never clarify. Does NOT claim: exact QGP properties - it fingerprints the first fluid.",
 "pointer": "The Signature system's proposed approach maps QGP transport properties vs temperature; the companion Signature Edition record specifies the fluid protocol.",
 "key_points": [
  "QGP flows as a near-perfect liquid (eta/s near KSS bound).",
  "Temperature dependence of viscosity debated.",
  "Small-system (pp/pA) QGP question open.",
  "Hadronization mechanism uncertain.",
 ],
 "requirements": [
  "Bayesian transport-property extraction.",
  "Jet-quenching tomography.",
  "Small-system QGP tests.",
 ],
 "citations": [
  "Shuryak EV (2005) What RHIC experiments and theory tell us about properties of quark-gluon plasma. Nuclear Physics A 750.",
 ],
 "demo": {"e1": 49.0, "e2": 51.0, "theta_deg": 90.0},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "pp-confinement",
 "name": "The Confinement Problem",
 "group": "QCD",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Quarks are never seen free - but what is the exact mechanism that confines them, and can it be proven?",
 "background": "The confinement problem - why color charge is never isolated - is QCD's deepest unsolved analytic question: lattice QCD demonstrates confinement numerically, but the analytic mechanism (dual superconductivity? center vortices? Gribov-Zwanziger?) is unproven, and the Clay Millennium prize for Yang-Mills existence and mass gap stands unclaimed. The confinement-deconfinement transition (QGP) is mapped; the zero-temperature mechanism is not derived. The most certain fact (no free quarks) has no proven explanation.",
 "why_it_matters": "Confinement is QCD's defining fact without a proven mechanism. The Clay prize waits on the proof.",
 "sig_lens": "The Signature lens reads confinement as the perfect prison: the protocol must find the lock's mechanism - analytically, not just numerically.",
 "sig_solution": LABEL + " Assumptions: (1) lattice demonstrates; analytic mechanism unproven; (2) Clay prize unclaimed. Reasoning path: attack analytically - develop the candidate mechanisms (dual superconductor, vortices) to derivable predictions and test on the lattice. Proposed mechanism: a prison protocol with analytic confinement-mechanism development, lattice tests discriminating mechanisms, and mass-gap proof attempts. Confirm: one mechanism derived and verified. Kill: the analytic proof stays out of reach. Does NOT claim: confinement explained - it seeks the lock's mechanism.",
 "pointer": "The Signature system's proposed approach attacks confinement analytically with lattice discrimination; the companion Signature Edition record specifies the prison protocol.",
 "key_points": [
  "No free quarks ever observed.",
  "Lattice demonstrates confinement numerically.",
  "Analytic mechanism (dual SC, vortices) unproven.",
  "Clay Millennium prize unclaimed.",
 ],
 "requirements": [
  "Analytic mechanism development.",
  "Lattice discrimination of mechanisms.",
  "Mass-gap proof attempts.",
 ],
 "citations": [
  "Clay Mathematics Institute: Yang-Mills existence and mass gap problem.",
 ],
 "demo": {"e1": 54.0, "e2": 46.0, "theta_deg": 105.0},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "pp-mass-gap",
 "name": "The Yang Mills Mass Gap Problem",
 "group": "QCD",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Pure Yang-Mills theory should have a mass gap - but can it be proven that the lightest glueball is massive?",
 "background": "The Yang-Mills mass-gap problem - proving that pure SU(3) gauge theory has a positive mass gap (lightest excitation massive) - is the Clay Millennium problem for particle physics: lattice QCD shows the gap numerically (~1.5 GeV scale), but the rigorous proof from the axioms is missing. The gap's existence underlies confinement and the hadronic mass scale; its proof would be the first rigorous bridge from QFT axioms to the strong force's spectrum. The numerical evidence is overwhelming; the proof is absent.",
 "why_it_matters": "The mass gap is the strong force's mass scale, proven only numerically. The Clay proof would rigorize quantum field theory's core.",
 "sig_lens": "The Signature lens reads the mass gap as the unproven foundation: the protocol must build the rigorous bridge - or map exactly where the planks are missing.",
 "sig_solution": LABEL + " Assumptions: (1) lattice shows the gap numerically; (2) rigorous proof missing. Reasoning path: build toward proof - constructive QFT programs, Hamiltonian approaches, and gap estimates with rigorous error bounds. Proposed mechanism: a foundation protocol with constructive-QFT mass-gap programs, rigorous lattice error bounds, and proof-attempt documentation. Confirm: the gap proven. Kill: the proof stays beyond methods. Does NOT claim: the proof - it builds the bridge plank by plank.",
 "pointer": "The Signature system's proposed approach pursues the Yang-Mills mass-gap proof constructively; the companion Signature Edition record specifies the foundation protocol.",
 "key_points": [
  "Clay Millennium problem: prove the Yang-Mills mass gap.",
  "Lattice shows ~1.5 GeV scale gap numerically.",
  "Rigorous proof from QFT axioms missing.",
  "The gap underlies confinement and hadronic masses.",
 ],
 "requirements": [
  "Constructive-QFT proof programs.",
  "Rigorous lattice error bounds.",
  "Documented proof attempts.",
 ],
 "citations": [
  "Jaffe A, Witten E: Quantum Yang-Mills theory (Clay problem description).",
 ],
 "demo": {"e1": 57.0, "e2": 43.0, "theta_deg": 35.0},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "pp-axion-quality",
 "name": "The Axion Quality Problem",
 "group": "Beyond Standard Model",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "The axion solves strong CP - but quantum gravity should spoil the Peccei-Quinn symmetry, so how good must the symmetry be, and is it?",
 "background": "The axion quality problem - the Peccei-Quinn symmetry must be good to ~1 part in 10^10 (to keep theta < 1e-10), but quantum gravity is expected to violate all global symmetries - threatens the axion solution: if Planck-suppressed operators break PQ badly, the axion does not solve strong CP. Solutions (accidental symmetries, composite axions, extra-dimensional protection) each add structure. The quality problem is the axion's fine print: the beautiful solution needs an implausibly good symmetry. The axion's quality is its vulnerability.",
 "why_it_matters": "The axion is the best strong-CP solution and a dark-matter candidate. Its quality problem is the solution's fine print.",
 "sig_lens": "The Signature lens reads axion quality as the fine print: the protocol must check whether the symmetry is good enough - by UV completions that protect it.",
 "sig_solution": LABEL + " Assumptions: (1) PQ must hold to 1e-10; (2) quantum gravity violates global symmetries. Reasoning path: build protected axions - UV completions (composite, extra-dimensional, accidental) with the quality built in - and test their predictions. Proposed mechanism: a fine-print protocol with protected-axion model building, quality-quantified predictions, and axion searches covering the protected models' ranges. Confirm: a protected axion found. Kill: protection needs implausible structure. Does NOT claim: the axion's quality - it reads the fine print.",
 "pointer": "The Signature system's proposed approach builds quantum-gravity-protected axion models; the companion Signature Edition record specifies the fine-print protocol.",
 "key_points": [
  "PQ symmetry must hold to ~1e-10.",
  "Quantum gravity violates global symmetries.",
  "Composite/extra-dimensional axions protect it.",
  "Quality is the axion solution's vulnerability.",
 ],
 "requirements": [
  "Protected-axion UV completions.",
  "Quality-quantified model predictions.",
  "Searches covering protected ranges.",
 ],
 "citations": [
  "Kamionkowski M, March-Russell J (1992) Planck-scale physics and the Peccei-Quinn mechanism. Physics Letters B 282.",
 ],
 "demo": {"e1": 45.0, "e2": 55.0, "theta_deg": 125.0},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "pp-light-dm",
 "name": "The Light Dark Matter Problem",
 "group": "Dark Sector",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Dark matter could be light - MeV to GeV - but how can particles too light for standard detectors be found?",
 "background": "The light-dark-matter problem - sub-GeV dark matter evades standard nuclear-recoil detectors (the recoil is below threshold) - opened a new search frontier: electron-recoil detectors (SENSEI, DAMIC, SuperCDMS), accelerator searches (LDMX, Belle II), and astrophysical probes. The thermal-relic target gives a sharp milestone (the Lee-Weinberg bound evaded via new mediators). The light window is vast and barely probed - the WIMP hunt's null results pushed the field here. The dark matter may be light; the detectors must get lighter.",
 "why_it_matters": "The WIMP window narrows; the light window is vast and unprobed. The dark matter's mass is unknown by orders of magnitude.",
 "sig_lens": "The Signature lens reads light dark matter as the whisper: the protocol must build quieter microphones (lower thresholds) and listen at the thermal target.",
 "sig_solution": LABEL + " Assumptions: (1) sub-GeV evades nuclear-recoil detectors; (2) thermal target gives milestones. Reasoning path: go low-threshold - electron-recoil detectors, accelerator missing-momentum searches - aimed at the thermal-relic milestones. Proposed mechanism: a whisper protocol with low-threshold detector development, accelerator light-DM searches, and thermal-target milestone tracking. Confirm: the thermal targets probed or a signal found. Kill: the milestones excluded and the window stays vast. Does NOT claim: light dark matter - it builds quieter microphones.",
 "pointer": "The Signature system's proposed approach hunts light dark matter with low-threshold detectors; the companion Signature Edition record specifies the whisper protocol.",
 "key_points": [
  "Sub-GeV dark matter evades standard detectors.",
  "Electron-recoil and accelerator searches open the window.",
  "Thermal-relic targets give sharp milestones.",
  "The light window is vast and barely probed.",
 ],
 "requirements": [
  "Low-threshold detector development.",
  "Accelerator missing-momentum searches.",
  "Thermal-target milestone tracking.",
 ],
 "citations": [
  "Battaglieri M et al. (2017) US Cosmic Visions: New Ideas in Dark Matter. arXiv:1707.04591.",
 ],
 "demo": {"e1": 48.0, "e2": 52.0, "theta_deg": 68.0},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "pp-dark-photon",
 "name": "The Dark Photon Problem",
 "group": "Dark Sector",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "A dark photon - a hidden-sector force carrier - could connect to our world - but does it exist, and how would it show itself?",
 "background": "The dark-photon problem - a hypothetical U(1) gauge boson kinetically mixing with the photon - is the dark sector's simplest portal: it predicts visible signatures (resonant e+e- bumps, missing-energy events, beam-dump signals) across MeV-GeV masses. Searches (NA64, HPS, Belle II, LHCb) carve the parameter space; the muon g-2 favored region is largely excluded. The dark photon remains the benchmark hidden-sector particle - simple, predictive, and still possibly hiding in the gaps. The portal is either open or closed; the gaps are closing.",
 "why_it_matters": "The dark photon is the dark sector's simplest door to our world. Its existence would open the hidden sector.",
 "sig_lens": "The Signature lens reads the dark photon as the hidden door: the protocol must check every gap in the wall (parameter space) systematically.",
 "sig_solution": LABEL + " Assumptions: (1) kinetic mixing predicts visible signatures; (2) g-2 region largely excluded. Reasoning path: close the gaps systematically - bump hunts, missing-energy, beam dumps across the mass-coupling plane. Proposed mechanism: a door protocol with coordinated dark-photon searches, parameter-space gap mapping, and hidden-sector model updates per exclusion. Confirm: a dark photon found. Kill: the gaps close fully. Does NOT claim: the dark photon - it checks the wall's gaps.",
 "pointer": "The Signature system's proposed approach closes dark-photon parameter gaps systematically; the companion Signature Edition record specifies the door protocol.",
 "key_points": [
  "Dark photon: U(1) boson mixing with the photon.",
  "Predicts bumps, missing energy, beam-dump signals.",
  "Muon g-2 favored region largely excluded.",
  "Benchmark hidden-sector portal.",
 ],
 "requirements": [
  "Coordinated multi-experiment searches.",
  "Parameter-space gap mapping.",
  "Model updates per exclusion.",
 ],
 "citations": [
  "Alexander J et al. (2016) Dark Sectors 2016 Workshop Report. arXiv:1608.08632.",
 ],
 "demo": {"e1": 53.0, "e2": 47.0, "theta_deg": 88.0},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "pp-fifth-force",
 "name": "The Fifth Force Problem",
 "group": "Dark Sector",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Four forces are known - but could a fifth force hide at short ranges or in dark sectors, and how would it be detected?",
 "background": "The fifth-force problem - hypothetical new forces (Yukawa-type deviations from gravity or electromagnetism) - is tested by torsion balances (Eot-Wash to microns), Casimir measurements, neutron bouncing, and astrophysical bounds: no deviation found, but the tests cover limited ranges and couplings. Dark-sector fifth forces (coupled to dark matter) could evade visible tests. The X17 anomaly (a claimed 17-MeV boson in nuclear transitions) is the controversial hint. The fifth force is either absent or exquisitely hidden.",
 "why_it_matters": "A fifth force would rewrite the force inventory. Its absence bounds every new-physics model with light mediators.",
 "sig_lens": "The Signature lens reads the fifth force as the unheard voice: the protocol must quiet every known noise (systematics) and listen at every range.",
 "sig_solution": LABEL + " Assumptions: (1) no deviation found; tests cover limited ranges; (2) X17 controversial. Reasoning path: listen everywhere - push short-range gravity tests, resolve the X17 claim independently, and test dark-sector forces astrophysically. Proposed mechanism: a voice protocol with next-gen torsion-balance and neutron tests, independent X17 replication, and dark-force astrophysical bounds. Confirm: a force found. Kill: the ranges excluded and X17 refuted. Does NOT claim: a fifth force - it quiets the noise and listens.",
 "pointer": "The Signature system's proposed approach tests fifth forces at every range and resolves X17; the companion Signature Edition record specifies the voice protocol.",
 "key_points": [
  "Torsion balances test gravity to microns; no deviation.",
  "Dark-sector forces could evade visible tests.",
  "X17 17-MeV anomaly is controversial.",
  "Tests cover limited ranges and couplings.",
 ],
 "requirements": [
  "Next-generation short-range force tests.",
  "Independent X17 replication.",
  "Dark-force astrophysical bounds.",
 ],
 "citations": [
  "Adelberger EG et al. (2009) Tests of the gravitational inverse-square law. Annual Review Nuclear and Particle Science 59.",
 ],
 "demo": {"e1": 41.0, "e2": 59.0, "theta_deg": 58.0},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "pp-lfu",
 "name": "The Lepton Flavor Universality Problem",
 "group": "Flavor",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "The Standard Model treats electron, muon, and tau identically - but B-decay ratios hint otherwise, so is lepton universality violated?",
 "background": "The lepton-flavor-universality problem - R_K and R_K* (B -> K l+l-) ratios deviating from 1 - was the B-anomaly flagship: LHCb's 2021-2022 updates brought the ratios back toward the SM, deflating the excitement, but R_D/R_D* (B -> D tau nu) tensions persist. The rise and fall of R_K is the cautionary tale: systematics and statistics versus new physics (leptoquarks, Z'). The universality tests continue at Belle II and LHCb upgrades. The principle is either exact or violated - the data wobbles.",
 "why_it_matters": "Lepton universality is a Standard Model pillar. Its violation would be new physics in the flavor sector - the wobble must be resolved.",
 "sig_lens": "The Signature lens reads universality as the equality law: the protocol must recount the votes (ratios) with better ballots (data) before declaring the law broken.",
 "sig_solution": LABEL + " Assumptions: (1) R_K back to SM; R_D(*) tensions persist; (2) rise-and-fall cautions. Reasoning path: recount with better ballots - Belle II and LHCb-upgrade ratios with reduced systematics - and test leptoquark/Z' models on the full pattern. Proposed mechanism: a recount protocol with high-statistics universality ratios, systematics-limited measurements, and model tests on the complete anomaly pattern. Confirm: a ratio violates universality robustly. Kill: all ratios converge to SM. Does NOT claim: universality violated - it recounts the votes.",
 "pointer": "The Signature system's proposed approach recounts lepton-universality ratios with better data; the companion Signature Edition record specifies the recount protocol.",
 "key_points": [
  "R_K/R_K* anomalies faded with LHCb updates.",
  "R_D/R_D* tensions persist.",
  "Leptoquarks and Z' models competed.",
  "Belle II and LHCb upgrades will recount.",
 ],
 "requirements": [
  "High-statistics universality ratio measurements.",
  "Systematics-limited experimental designs.",
  "Model tests on the complete pattern.",
 ],
 "citations": [
  "LHCb Collaboration (2023) Test of lepton universality in b -> s l+l- decays. PRL 131.",
 ],
 "demo": {"e1": 59.0, "e2": 41.0, "theta_deg": 72.0},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "pp-b-anomalies",
 "name": "The B Meson Anomalies Problem",
 "group": "Flavor",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "B-meson decays showed coherent deviations - but as the data grew, the anomalies faded, so what remains, and what did the episode teach?",
 "background": "The B-anomalies problem - the rise (2013-2021) and partial fall of b -> s l+l- deviations - is the field's object lesson: coherent ~3-4 sigma effects across channels inspired hundreds of leptoquark/Z' papers, then LHCb's larger datasets pulled R_K(*) back to the SM. What remains: R_D(*) tensions, some angular observables, each needing confirmation. The episode taught humility about systematics and the look-elsewhere effect - and left the leptoquark models constrained but alive. The anomalies faded; the lesson persists.",
 "why_it_matters": "The B-anomalies were the decade's new-physics hope. Their fading is the field's lesson in statistics - and the remnants still need verdicts.",
 "sig_lens": "The Signature lens reads the anomalies as the risen-and-fallen hope: the protocol must give the remnants their verdicts (confirm or bury) and keep the lesson.",
 "sig_solution": LABEL + " Assumptions: (1) R_K(*) back to SM; remnants need verdicts; (2) systematics lesson learned. Reasoning path: verdict the remnants - R_D(*), angular observables - with Belle II/LHCb-upgrade data, blinded and systematics-limited. Proposed mechanism: a verdict protocol with blinded remnant analyses, pre-registered anomaly tests, and leptoquark models held to the surviving data. Confirm: a remnant confirmed. Kill: all remnants dissolve. Does NOT claim: new physics - it verdicts the remnants.",
 "pointer": "The Signature system's proposed approach verdicts remaining B-anomalies with blinded analyses; the companion Signature Edition record specifies the verdict protocol.",
 "key_points": [
  "b -> s l+l- anomalies faded with more data.",
  "R_D(*) and angular tensions remain.",
  "Hundreds of leptoquark/Z' papers constrained.",
  "The episode taught systematics humility.",
 ],
 "requirements": [
  "Blinded remnant-anomaly analyses.",
  "Pre-registered anomaly tests.",
  "Models held to surviving data.",
 ],
 "citations": [
  "Bifani S et al. (2019) Review of lepton universality tests in B decays. J. Physics G 46.",
 ],
 "demo": {"e1": 46.0, "e2": 54.0, "theta_deg": 98.0},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "pp-direct-cp",
 "name": "The Direct CP Violation Problem",
 "group": "Flavor",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "CP violation in kaon decays (epsilon'/epsilon) was measured - but does the Standard Model predict its size, or is new physics hiding in the hadronic uncertainties?",
 "background": "The direct-CP-violation problem - epsilon'/epsilon measured at ~1.7e-3 (NA48, KTeV), but the SM prediction plagued by hadronic matrix-element uncertainties - is the precision frontier's hadronic swamp: lattice QCD (RBC-UKQCD) now computes it with ~20-30% errors, roughly consistent with experiment, but the uncertainties still allow new-physics room. Kaon physics (KOTO, NA62) hunts rarer modes (K -> pi nu nubar) where the theory is cleaner. The measured violation is confirmed; its SM account is approximate.",
 "why_it_matters": "Direct CP violation is the confirmed matter-antimatter asymmetry in the lab. Its SM account's precision decides whether new physics hides there.",
 "sig_lens": "The Signature lens reads epsilon' as the confirmed asymmetry in a hadronic fog: the protocol must clear the fog (lattice precision) to see what stands behind it.",
 "sig_solution": LABEL + " Assumptions: (1) epsilon'/epsilon measured; SM prediction hadronic-limited; (2) lattice errors ~20-30%. Reasoning path: clear the fog - push lattice matrix elements to <10%, and hunt the clean rare kaon decays. Proposed mechanism: a fog protocol with precision lattice-QCD programs, rare-kaon-decay hunts (KOTO, NA62), and new-physics tests on the cleared prediction. Confirm: the cleared SM matches or misses definitively. Kill: the fog never clears. Does NOT claim: new physics in kaons - it clears the fog first.",
 "pointer": "The Signature system's proposed approach clears kaon hadronic uncertainties with lattice precision; the companion Signature Edition record specifies the fog protocol.",
 "key_points": [
  "epsilon'/epsilon ~1.7e-3 measured (NA48, KTeV).",
  "SM prediction limited by hadronic matrix elements.",
  "Lattice errors now ~20-30%, roughly consistent.",
  "Rare K -> pi nu nubar modes are theoretically cleaner.",
 ],
 "requirements": [
  "Sub-10% lattice matrix elements.",
  "Rare-kaon-decay hunts.",
  "New-physics tests on cleared predictions.",
 ],
 "citations": [
  "RBC-UKQCD Collaboration (2020) Direct CP violation and the Delta I=1/2 rule. PRD 102.",
 ],
 "demo": {"e1": 52.0, "e2": 48.0, "theta_deg": 62.0},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "pp-0nubb",
 "name": "The Neutrinoless Double Beta Decay Problem",
 "group": "Neutrinos",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "If neutrinos are their own antiparticles, nuclei should sometimes decay without emitting neutrinos - but has it been seen, and what would it prove?",
 "background": "The neutrinoless-double-beta-decay problem - the hunt for (A,Z) -> (A,Z+2) + 2e- with no neutrinos - is the Majorana question's experimental face: observation proves neutrinos are Majorana (Schechter-Valle theorem) and measures the effective mass; non-observation to tonne-scale excludes the inverted ordering. KamLAND-Zen, GERDA/LEGEND, EXO/nEXO, CUORE push the half-life limits past 10^26 years. The decay is either the rarest process ever seen or forbidden - the tonne-scale experiments will say which.",
 "why_it_matters": "0nubb observation proves the Majorana nature - new physics in the neutrino's identity. The tonne scale decides the inverted ordering.",
 "sig_lens": "The Signature lens reads 0nubb as the identity test: the protocol must reach the tonne scale - the inverted ordering cannot hide there.",
 "sig_solution": LABEL + " Assumptions: (1) limits past 1e26 yr; (2) inverted ordering guarantees tonne-scale signal. Reasoning path: build to the tonne scale - LEGEND-1000, nEXO - and read the verdict: signal or inverted-ordering exclusion. Proposed mechanism: an identity protocol with tonne-scale 0nubb experiments, nuclear-matrix-element uncertainty reduction, and Majorana-mechanism discrimination if seen. Confirm: the decay observed. Kill: tonne-scale null excludes inverted ordering. Does NOT claim: Majorana neutrinos - it runs the identity test.",
 "pointer": "The Signature system's proposed approach reaches tonne-scale 0nubb sensitivity; the companion Signature Edition record specifies the identity protocol.",
 "key_points": [
  "0nubb proves Majorana nature (Schechter-Valle).",
  "Half-life limits past 1e26 years.",
  "Inverted ordering guarantees tonne-scale signal.",
  "LEGEND, nEXO, KamLAND-Zen lead the hunt.",
 ],
 "requirements": [
  "Tonne-scale 0nubb experiments.",
  "Nuclear-matrix-element uncertainty reduction.",
  "Mechanism discrimination if observed.",
 ],
 "citations": [
  "Dolinski MJ et al. (2019) Neutrinoless double-beta decay: status and prospects. Annual Review Nuclear and Particle Science 69.",
 ],
 "demo": {"e1": 50.0, "e2": 50.0, "theta_deg": 115.0},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "pp-seesaw",
 "name": "The Seesaw Scale Problem",
 "group": "Neutrinos",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "The seesaw mechanism explains tiny neutrino masses with heavy partners - but how heavy: GUT-scale, TeV-scale, or anywhere in between?",
 "background": "The seesaw-scale problem - the right-handed neutrino mass could be 10^14 GeV (GUT seesaw, untestable) or TeV (testable at colliders) or keV (warm dark matter) - is the mechanism's testability question: high-scale seesaw is elegant but untestable; low-scale variants (inverse, linear seesaw) predict collider signatures (displaced vertices, lepton-number violation) and lepton-flavor violation. Leptogenesis needs the scale for the asymmetry calculation. The seesaw's scale is its falsifiability - spanning 20 orders of magnitude.",
 "why_it_matters": "The seesaw is the leading neutrino-mass mechanism; its scale decides whether it is science or metaphysics. Twenty orders of magnitude is the testability gap.",
 "sig_lens": "The Signature lens reads the seesaw scale as the hidden floor: the protocol must sound every floor - colliders, LFV, cosmology - until the mechanism is found or cornered.",
 "sig_solution": LABEL + " Assumptions: (1) scale spans 1e3 to 1e14 GeV; (2) low-scale variants testable. Reasoning path: sound the testable floors - collider displaced vertices, charged-lepton-flavor violation, and cosmological bounds - and corner the scale. Proposed mechanism: a floors protocol with low-scale seesaw collider searches, LFV experiments (Mu2e, COMET), and leptogenesis-scale consistency tests. Confirm: the heavy partners found. Kill: the testable floors empty and only GUT-scale remains. Does NOT claim: the seesaw scale - it sounds every floor.",
 "pointer": "The Signature system's proposed approach sounds seesaw scales from colliders to cosmology; the companion Signature Edition record specifies the floors protocol.",
 "key_points": [
  "Seesaw scale spans keV to 1e14 GeV.",
  "GUT-scale seesaw elegant but untestable.",
  "Low-scale variants predict collider/LFV signals.",
  "Leptogenesis needs the scale.",
 ],
 "requirements": [
  "Low-scale seesaw collider searches.",
  "Charged-lepton-flavor-violation experiments.",
  "Leptogenesis-scale consistency tests.",
 ],
 "citations": [
  "Minkowski P (1977) mu -> e gamma at a rate of one out of 1e9 muon decays? Physics Letters B 67.",
 ],
 "demo": {"e1": 44.0, "e2": 56.0, "theta_deg": 82.0},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "pp-gut",
 "name": "The Grand Unification Problem",
 "group": "Unification",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "The three forces' couplings nearly meet at high energies - but do they truly unify, and what is the unified theory?",
 "background": "The grand-unification problem - SU(3)xSU(2)xU(1) into SU(5), SO(10), or larger - is motivated by the couplings' near-meeting (~10^16 GeV, exact with SUSY): but minimal SU(5) is dead (proton decay), SO(10) needs the Higgs sector specified, and the unification scale is untestable directly. The doublet-triplet splitting problem and the flavor structure's origin within GUTs are unsolved. Unification is the most beautiful idea with the least direct evidence - the couplings' meeting may be coincidence or destiny.",
 "why_it_matters": "Grand unification would merge three forces into one - the Standard Model's completion. The near-meeting demands explanation or dismissal.",
 "sig_lens": "The Signature lens reads unification as the forces' family reunion: the protocol must check whether the couplings really meet (precision running) and find the family's house (the GUT).",
 "sig_solution": LABEL + " Assumptions: (1) couplings nearly meet at 1e16 GeV; (2) minimal SU(5) dead. Reasoning path: test the meeting precisely - coupling-constant running with threshold corrections - and build viable GUTs on the surviving space. Proposed mechanism: a reunion protocol with precision coupling measurements, GUT-model building (SO(10) variants), and proton-decay predictions as the test. Confirm: a GUT's full predictions verified. Kill: the meeting proves coincidental. Does NOT claim: grand unification - it checks the reunion.",
 "pointer": "The Signature system's proposed approach tests coupling unification precisely and builds viable GUTs; the companion Signature Edition record specifies the reunion protocol.",
 "key_points": [
  "Couplings nearly meet at ~1e16 GeV.",
  "Minimal SU(5) excluded by proton decay.",
  "SO(10) needs its Higgs sector specified.",
  "Doublet-triplet splitting unsolved.",
 ],
 "requirements": [
  "Precision coupling-constant running.",
  "Viable GUT model building.",
  "Proton-decay predictions as tests.",
 ],
 "citations": [
  "Georgi H, Glashow SL (1974) Unity of all elementary-particle forces. PRL 32.",
 ],
 "demo": {"e1": 58.0, "e2": 42.0, "theta_deg": 92.0},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "pp-toe",
 "name": "The Theory of Everything Problem",
 "group": "Unification",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Can all forces and particles - including gravity - be described by one theory, and what would it take to know it is right?",
 "background": "The theory-of-everything problem - unifying quantum mechanics and gravity with all particles and forces - is physics' ultimate goal: string theory is the leading candidate (mathematically rich, experimentally remote), loop quantum gravity quantizes geometry (matter unincorporated), and the landscape/swampland program tries to derive predictions. The testability gap is the crisis: a ToE without experimental confirmation is mathematics. The problem is as much epistemological as physical - what counts as knowing the final theory?",
 "why_it_matters": "The ToE is physics' ultimate goal. Its testability gap is the field's epistemological crisis.",
 "sig_lens": "The Signature lens reads the ToE as the final map: the protocol must demand the map predict the territory's unexplored regions - or admit it is a beautiful drawing.",
 "sig_solution": LABEL + " Assumptions: (1) string theory rich but remote; LQG incomplete; (2) testability gap is the crisis. Reasoning path: demand predictions - swampland conjectures, string phenomenology, LQG phenomenology - and test them. Proposed mechanism: a map protocol with candidate-theory prediction requirements, phenomenology programs per candidate, and epistemological honesty about confirmation standards. Confirm: a candidate predicts verified new phenomena. Kill: no candidate predicts testably. Does NOT claim: the final theory - it demands the map prove itself.",
 "pointer": "The Signature system's proposed approach demands testable predictions from ToE candidates; the companion Signature Edition record specifies the map protocol.",
 "key_points": [
  "String theory: mathematically rich, experimentally remote.",
  "Loop quantum gravity: geometry quantized, matter missing.",
  "Swampland program seeks derived predictions.",
  "Testability gap is epistemological too.",
 ],
 "requirements": [
  "Testable-prediction requirements per candidate.",
  "Phenomenology programs (string, LQG).",
  "Honest confirmation standards.",
 ],
 "citations": [
  "Greene B (1999) The Elegant Universe. Norton.",
 ],
 "demo": {"e1": 47.0, "e2": 53.0, "theta_deg": 108.0},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "pp-unified",
 "name": "The Unified Particle Physics Problem",
 "group": "Unification",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "The Standard Model works - but its 19+ parameters, three generations, and missing gravity show it is incomplete, so what completes it as one framework?",
 "background": "The unified-particle-physics problem - the Standard Model's completion - collects every gap: the parameter count, the flavor pattern, neutrino masses, dark matter, dark energy, the hierarchy, strong CP, quantum gravity. No single framework addresses all: SUSY handles some, GUTs others, strings promise all but deliver few testably. The completion may be one theory or several layers. The Standard Model is the most successful incomplete theory - its completion is the field's collective project.",
 "why_it_matters": "The Standard Model's incompleteness is the field's collective project. Its completion - one framework or layers - is the century's physics.",
 "sig_lens": "The Signature lens reads the Standard Model as the unfinished cathedral: the protocol must complete it stone by stone - each gap a stone, each experiment a mason.",
 "sig_solution": LABEL + " Assumptions: (1) gaps span parameters to gravity; (2) no framework addresses all. Reasoning path: complete stone by stone - prioritize the gaps by testability (neutrinos, flavor, Higgs, dark sectors) and build the framework from confirmed stones. Proposed mechanism: a cathedral protocol with gap-prioritized experimental programs, framework-building on confirmed results, and unification judged by multi-gap explanation. Confirm: a framework explains multiple gaps with verified predictions. Kill: the gaps need separate physics. Does NOT claim: the completed theory - it builds stone by stone.",
 "pointer": "The Signature system's proposed approach completes the Standard Model gap by gap; the companion Signature Edition record specifies the cathedral protocol.",
 "key_points": [
  "SM gaps: parameters, flavor, neutrinos, dark sectors, gravity.",
  "No framework addresses all gaps.",
  "SUSY, GUTs, strings each partial.",
  "Completion may be one theory or layers.",
 ],
 "requirements": [
  "Gap-prioritized experimental programs.",
  "Framework building on confirmed results.",
  "Multi-gap explanation as unification test.",
 ],
 "citations": [
  "Particle Data Group (2024) Review of Particle Physics.",
 ],
 "demo": {"e1": 55.0, "e2": 45.0, "theta_deg": 118.0},
},
]
