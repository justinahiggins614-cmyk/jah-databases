#!/usr/bin/env python3
"""Entries for The Unsolved Cosmology Database (unsolved-cosmology) and its
Signature half (unsolved-cosmology-signature).

34 famous unsolved problems in cosmology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USCO- / JAH-USCOS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "cosmology",
 "disp": "cosmology",
 "name": "The Unsolved Cosmology Database",
 "sig_name": "The Unsolved Cosmology Signature Database",
 "prefix": "JAH-USCO-",
 "sig_prefix": "JAH-USCOS-",
 "ai": "JAH Unsolved Cosmology Archivist",
 "tagline": ("Thirty-four famous open problems in cosmology, from the Hubble tension to the ultimate fate of the "
             "fate: real, fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of cosmology: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in cosmology, real and fact-checked: the Hubble tension, "
              "the identity of dark matter, the nature of dark energy, the cosmic coincidence, matter-antimatter asymmetry, "
              "the flatness and horizon problems, first stars, reionization, missing satellites, and the core-cusp "
              "problem - every record carrying the problem statement, background, why it matters, key points, "
              "requirements, standards, citations, and a working solution-explorer demonstration, organized in the "
              "Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "cosmology problems approached as a covenant between the known and the unknown, each carrying the "
              "full Signature-generated proposed solution with its assumptions declared, its confirm and refute "
              "conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never presented "
              "as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (Hubble tension, dark matter identity, "
                 "dark energy nature, cosmic coincidence, matter-antimatter asymmetry, flatness, horizon, first "
                 "stars, reionization, missing satellites, core-cusp) -> Compounded (too-big-to-fail, baryonic "
                 "Tully-Fisher, lithium problem, cosmological constant, vacuum energy, inflation models, "
                 "trans-Planckian, eternal inflation, multiverse testability, CMB anomalies, axis of evil, cold "
                 "spot) -> Advanced (primordial black holes, dark-ages 21cm, fast radio bursts, gravitational-wave "
                 "background, ultra-high-energy cosmic rays, homogeneity scale, backreaction, arrow of time, "
                 "fine-tuning, ultimate fate, unified cosmology)."),
 "search_ph": ("Search Hubble tension, dark matter, dark energy, inflation, CMB anomalies, black holes, cosmic "
               "rays..."),
 "chat_ph": "Ask about the great open problems of cosmology...",
 "greet_pub": ("I am the JAH Unsolved Cosmology Archivist. Ask me about the great open problems of cosmology - "
               "from the Hubble tension, dark matter, and dark energy through inflation and CMB anomalies, to "
               "black holes, cosmic rays, and the ultimate fate of the universe."),
 "greet_sig": ("I am the JAH Unsolved Cosmology Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of cosmology - every approach labeled as a proposal, never "
               "established science."),
 "role_pub": ("unsolved cosmology archivist - the great open problems of cosmology, from the Hubble tension, "
              "dark matter, and dark energy through inflation and CMB anomalies, to black holes, cosmic rays, "
              "and the ultimate fate of the universe; teaches progressively along the ladder from foundations through "
              "compounded to advanced; answers from many angles - definition, example, analogy, application, "
              "history, math - using only archive data from this system"),
 "role_sig": ("unsolved cosmology archivist - Signature editions: his original Signature solution method applied "
              "to the 34 great open problems of cosmology, each carrying the full Signature-generated proposed "
              "solution, clearly labeled Signature-made and never presented as established science; teaches "
              "progressively along the ladder from foundations through compounded to advanced; answers from many "
              "angles - definition, example, analogy, application, history, math - using only archive data from "
              "this system"),
 "gen_desc": "Generate clearly-labeled unsolved cosmology studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Planck Collaboration cosmological parameters; PDG Review of Particle Physics, astrophysical constants).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "co-hubble",
 "name": "The Hubble Tension Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "The universe's expansion rate measures differently nearby and far away - but which measurement is right, and is new physics needed?",
 "background": "The Hubble tension - the ~5-sigma disagreement between the local distance-ladder H0 (~73 km/s/Mpc, SH0ES) and the CMB-inferred H0 (~67 km/s/Mpc, Planck) - is cosmology's most famous crisis: the error bars no longer overlap, and the systematics hunt (Cepheid calibration, CMB modeling) has not resolved it. Proposed solutions range from early dark energy to modified gravity to new neutrino physics - each fixing the tension while straining other data. The tension is either the biggest systematic error in modern cosmology or the first crack in Lambda-CDM.",
 "why_it_matters": "H0 sets the universe's age, size, and the dark-energy budget. A 5-sigma disagreement is either a mistake or a discovery.",
 "sig_lens": "The Signature lens reads the tension as two witnesses disagreeing: the protocol must cross-examine both before declaring new physics.",
 "sig_solution": LABEL + " Assumptions: (1) the 5-sigma gap survives systematics checks so far; (2) proposed new physics strains other data. Reasoning path: build the third witness - independent H0 measures (gravitational-wave standard sirens, time-delay lensing) that share neither ladder's systematics. Proposed mechanism: a witnesses protocol prioritizing independent H0 methods, requiring new-physics proposals to fit the full dataset (not just H0), and treating the tension as unresolved until the third witness speaks. Confirm: independent measures converge on one value. Kill: the third witness splits too and the tension is systematics all the way down. Does NOT claim: the true H0 - it cross-examines before declaring.",
 "pointer": "The Signature system's proposed approach resolves the Hubble tension with independent third-witness measurements; the companion Signature Edition record specifies the witnesses protocol.",
 "key_points": [
  "Local H0 (~73) and CMB H0 (~67) disagree at ~5 sigma.",
  "Systematics hunts have not closed the gap.",
  "New-physics proposals strain other datasets.",
  "The tension is cosmology's most famous crisis.",
 ],
 "requirements": [
  "Independent H0 methods (standard sirens, time-delay lensing).",
  "New-physics proposals fitting the full dataset.",
  "No new-physics declaration until the third witness speaks.",
 ],
 "citations": [
  "Riess AG et al. (2022) A comprehensive measurement of the local value of the Hubble constant. ApJ 934.",
  "Planck Collaboration (2020) Planck 2018 results VI: Cosmological parameters. A&A 641.",
 ],
 "demo": {"h0": 73.0, "d_mpc": 100.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "co-dark-matter",
 "name": "The Dark Matter Identity Problem",
 "group": "Dark Sector",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Dark matter outweighs normal matter five to one - but what is it made of, and why has every direct search come up empty?",
 "background": "Dark matter's gravitational evidence (galaxy rotation curves, lensing, CMB) is overwhelming; its particle identity is unknown. The WIMP - the favorite for decades - is cornered by null direct-detection results (XENON, LUX-ZEPLIN pushing limits down orders of magnitude); axions, sterile neutrinos, and primordial black holes each have followings and gaps. The small-scale problems (missing satellites, core-cusp, too-big-to-fail) may point to dark-matter physics (self-interaction, warmth) or to baryonic feedback. The most abundant matter in the universe is unidentified.",
 "why_it_matters": "Dark matter is most of the matter. Its identity decides galaxy formation, the early universe, and possibly new particle physics.",
 "sig_lens": "The Signature lens reads dark matter as the universe's missing person: the protocol must search every hiding place (detectors, colliders, skies) and read the small-scale clues.",
 "sig_solution": LABEL + " Assumptions: (1) gravitational evidence overwhelming; particle identity unknown; (2) WIMPs cornered but not excluded. Reasoning path: search all channels simultaneously - direct, indirect, collider, astrophysical - and let the small-scale structure arbitrate between particle physics and feedback. Proposed mechanism: a missing-person protocol with coordinated multi-channel searches, small-scale-structure tests discriminating dark-matter physics from baryonic feedback, and candidate evaluation on the full evidence. Confirm: one channel yields a consistent signal. Kill: all channels stay null and the small scales are all feedback. Does NOT claim: dark matter's identity - it searches every hiding place.",
 "pointer": "The Signature system's proposed approach hunts dark matter across all channels with small-scale arbitration; the companion Signature Edition record specifies the missing-person protocol.",
 "key_points": [
  "Dark matter outweighs baryons ~5:1; evidence is gravitational.",
  "WIMPs are cornered by null direct searches.",
  "Axions, sterile neutrinos, PBHs each have gaps.",
  "Small-scale problems may be particle physics or feedback.",
 ],
 "requirements": [
  "Coordinated direct, indirect, collider, astrophysical searches.",
  "Small-scale tests discriminating physics from feedback.",
  "Candidate evaluation on full evidence.",
 ],
 "citations": [
  "Bertone G, Hooper D (2018) History of dark matter. Reviews of Modern Physics 90.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 150.0},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "co-dark-energy",
 "name": "The Dark Energy Nature Problem",
 "group": "Dark Sector",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "The universe's expansion is accelerating, driven by 'dark energy' - but is it the cosmological constant, a dynamical field, or a sign that gravity is wrong?",
 "background": "Dark energy - ~70 percent of the cosmic energy budget, discovered 1998 via supernovae - accelerates the expansion, but its nature is unknown: the cosmological constant (vacuum energy) fits the data but is theoretically absurd (120 orders of magnitude off); quintessence (dynamical field) adds unobserved physics; modified gravity (f(R), DGP) rewrites Einstein. DESI's hints of evolving dark energy (2024-2025) may be the first crack - or systematics. The biggest energy component is the least understood.",
 "why_it_matters": "Dark energy decides the universe's fate. Its nature is the largest unknown in the cosmic budget.",
 "sig_lens": "The Signature lens reads dark energy as the budget's mystery line item: the protocol must audit it with time-resolved measurements before rewriting the ledger (gravity).",
 "sig_solution": LABEL + " Assumptions: (1) Lambda fits but is theoretically absurd; (2) DESI's evolving hints may be systematics. Reasoning path: measure dark energy's time evolution precisely - the equation-of-state history discriminates constant from dynamical from modified gravity. Proposed mechanism: a ledger protocol with Stage-IV dark-energy surveys (DESI, Euclid, Rubin) measuring w(z), modified-gravity tests on growth-vs-expansion consistency, and no gravity-rewriting until the time evolution demands it. Confirm: measured w(z) deviates from -1 robustly. Kill: w stays -1 and the constant stands unexplained. Does NOT claim: dark energy's nature - it audits the line item.",
 "pointer": "The Signature system's proposed approach measures dark energy's time evolution to discriminate models; the companion Signature Edition record specifies the ledger protocol.",
 "key_points": [
  "Dark energy is ~70% of the cosmic budget; nature unknown.",
  "Vacuum energy is 120 orders of magnitude off theory.",
  "DESI hints at evolving dark energy (unconfirmed).",
  "Modified gravity rewrites Einstein instead.",
 ],
 "requirements": [
  "Stage-IV surveys measuring w(z).",
  "Growth-versus-expansion modified-gravity tests.",
  "No gravity rewrite until evolution demands it.",
 ],
 "citations": [
  "Riess AG et al. (1998) Observational evidence from supernovae for an accelerating universe. AJ 116.",
  "DESI Collaboration (2024) DESI 2024 results.",
 ],
 "demo": {"h0": 67.4, "d_mpc": 200.0},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "co-coincidence",
 "name": "The Cosmic Coincidence Problem",
 "group": "Dark Sector",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Matter and dark energy have comparable densities right now - but why do we live in the brief era when they are equal?",
 "background": "The cosmic coincidence - matter density and dark-energy density are the same order of magnitude today, though matter dilutes as a^-3 while dark energy stays constant - means we live in the narrow transitional era: billions of years earlier, matter dominated utterly; billions later, dark energy dominates utterly. Anthropic explanations (we observe when observers can exist) are unsatisfying to many; dynamical explanations (tracker quintessence, interacting dark sectors) add physics to remove the coincidence. The 'why now' question is cosmology's fine-tuning in time.",
 "why_it_matters": "The coincidence is either a clue to new physics or an observer-selection effect. Telling which decides how the budget's mystery is read.",
 "sig_lens": "The Signature lens reads the coincidence as 'why now': the protocol must test whether the timing is physics (a mechanism) or perspective (selection).",
 "sig_solution": LABEL + " Assumptions: (1) the densities match only in a narrow era; (2) anthropic vs dynamical explanations compete. Reasoning path: test the dynamical explanations - if dark energy evolves or couples to matter, the coincidence may dissolve into mechanism. Proposed mechanism: a why-now protocol measuring dark-energy evolution and dark-sector coupling, and evaluating anthropic predictions against the measured cosmology. Confirm: measured evolution explains the timing. Kill: Lambda stands and the coincidence is brute fact or selection. Does NOT claim: the coincidence's resolution - it tests timing vs perspective.",
 "pointer": "The Signature system's proposed approach tests dynamical explanations of the cosmic coincidence; the companion Signature Edition record specifies the why-now protocol.",
 "key_points": [
  "Matter and dark-energy densities match only in a narrow era.",
  "Matter dilutes as a^-3; dark energy does not.",
  "Anthropic explanations compete with dynamical ones.",
  "The coincidence is fine-tuning in time.",
 ],
 "requirements": [
  "Dark-energy evolution and coupling measurements.",
  "Anthropic predictions tested against measured cosmology.",
  "No coincidence claim until dynamics are measured.",
 ],
 "citations": [
  "Zlatev I et al. (1999) Quintessence, cosmic coincidence, and the cosmological constant. PRL 82.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 120.0},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "co-baryogenesis",
 "name": "The Matter Antimatter Asymmetry Problem",
 "group": "Early Universe",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "The universe is made of matter, not antimatter - but the Big Bang should have made equal amounts, so where did the antimatter go?",
 "background": "Baryogenesis - the origin of the matter-antimatter asymmetry (one part in a billion) - requires Sakharov's conditions: baryon-number violation, C/CP violation, and out-of-equilibrium dynamics. The Standard Model has all three in principle but quantitatively fails (the electroweak phase transition is not strongly first-order; CP violation is too small). Candidates - leptogenesis (neutrino physics), Affleck-Dine, electroweak baryogenesis in extensions - each need new physics. The asymmetry is observed everywhere (no antimatter galaxies); its origin is new physics waiting to be found.",
 "why_it_matters": "Every atom exists because of the asymmetry. Its origin is guaranteed new physics - the question is which.",
 "sig_lens": "The Signature lens reads baryogenesis as the universe's original imbalance: the protocol must find which Sakharov condition the new physics strengthens.",
 "sig_solution": LABEL + " Assumptions: (1) Standard Model Sakharov conditions quantitatively fail; (2) asymmetry needs new physics. Reasoning path: test the candidate mechanisms where they touch experiment - CP violation, neutrino masses (leptogenesis), collider-accessible baryogenesis. Proposed mechanism: an imbalance protocol with neutrino-physics tests of leptogenesis, EDM searches for new CP violation, and collider probes of extended Higgs sectors. Confirm: one mechanism's predictions verified. Kill: all candidates excluded and the asymmetry stays mysterious. Does NOT claim: the baryogenesis mechanism - it tests where candidates touch experiment.",
 "pointer": "The Signature system's proposed approach tests baryogenesis candidates at experimental touchpoints; the companion Signature Edition record specifies the imbalance protocol.",
 "key_points": [
  "Sakharov conditions exist in the SM but quantitatively fail.",
  "The asymmetry is one part in a billion - and total.",
  "Leptogenesis, Affleck-Dine, electroweak variants compete.",
  "No antimatter galaxies observed.",
 ],
 "requirements": [
  "Neutrino-physics tests of leptogenesis.",
  "EDM searches for new CP violation.",
  "Collider probes of extended Higgs sectors.",
 ],
 "citations": [
  "Sakharov AD (1967) Violation of CP invariance, C asymmetry, and baryon asymmetry. JETP Letters 5.",
 ],
 "demo": {"h0": 71.0, "d_mpc": 180.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "co-flatness",
 "name": "The Flatness Problem",
 "group": "Early Universe",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "The universe's spatial geometry is flat to within a percent - but flatness is an unstable equilibrium, so why is it so precisely flat?",
 "background": "The flatness problem - Omega_total = 1 to ~0.5% (Planck) though any deviation grows with time - means the early universe was flat to absurd precision (one part in 10^62 at the Planck time). Inflation solves it by stretching any curvature flat, but the solution assumes inflation happened; alternatives (ekpyrotic, variable-speed-of-light) solve it differently. The flatness is measured exquisitely; its explanation is inflation-dependent. Without inflation, the flatness is the fine-tuning problem's flagship.",
 "why_it_matters": "The flatness is measured to half a percent. Its explanation is the main evidence for - and assumption of - inflation.",
 "sig_lens": "The Signature lens reads flatness as a pencil balanced for 14 billion years: the protocol must check whether inflation really steadied it, or something else did.",
 "sig_solution": LABEL + " Assumptions: (1) flatness measured to ~0.5%; (2) inflation explains it but is assumed. Reasoning path: test inflation's other predictions (see inflation entries) - flatness alone cannot confirm it; test alternatives' flatness mechanisms. Proposed mechanism: a pencil protocol measuring curvature ever more precisely, testing inflationary versus alternative flatness mechanisms on their distinct predictions. Confirm: curvature bounds tighten with inflation's other predictions holding. Kill: curvature detected nonzero and inflation's simplest versions strain. Does NOT claim: inflation confirmed - it checks the steadying hand.",
 "pointer": "The Signature system's proposed approach tests flatness explanations against distinct predictions; the companion Signature Edition record specifies the pencil protocol.",
 "key_points": [
  "Omega_total = 1 to ~0.5% though deviations grow with time.",
  "Early flatness needed absurd precision (1 in 10^62).",
  "Inflation stretches curvature flat - assuming inflation.",
  "Alternatives solve flatness differently.",
 ],
 "requirements": [
  "Ever-tighter curvature measurements.",
  "Flatness mechanisms tested on distinct predictions.",
  "No inflation confirmation from flatness alone.",
 ],
 "citations": [
  "Planck Collaboration (2020) Planck 2018 results VI. A&A 641.",
 ],
 "demo": {"h0": 69.0, "d_mpc": 90.0},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "co-horizon",
 "name": "The Horizon Problem",
 "group": "Early Universe",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "The cosmic microwave background is the same temperature in opposite directions - but those regions were never in causal contact, so how did they agree?",
 "background": "The horizon problem - the CMB's uniformity (1 part in 100,000) across causally disconnected patches - is inflation's original motivation (Guth, 1981): exponential expansion puts the patches in contact before inflation, then carries them apart. Alternatives (varying speed of light, ekpyrotic contraction) arrange contact differently. The problem is solved conditionally - given inflation (or an alternative), the uniformity follows. The uniformity is the observation; the contact mechanism is the open question.",
 "why_it_matters": "The CMB's uniformity is the early universe's deepest clue. The contact mechanism behind it is the Big Bang's missing prologue.",
 "sig_lens": "The Signature lens reads the horizon problem as distant thermometers agreeing: the protocol must find how they compared notes before the expansion separated them.",
 "sig_solution": LABEL + " Assumptions: (1) CMB uniform to 1 in 100,000 across disconnected patches; (2) inflation's contact is assumed. Reasoning path: test the contact mechanisms' distinct predictions - inflation predicts specific perturbation spectra; alternatives differ. Proposed mechanism: a thermometers protocol measuring the primordial perturbation spectrum ever more precisely (tilt, running, non-Gaussianity, tensors) to discriminate contact mechanisms. Confirm: measurements match one mechanism's full prediction set. Kill: all mechanisms fit and the contact stays ambiguous. Does NOT claim: the contact mechanism - it tests how the notes were compared.",
 "pointer": "The Signature system's proposed approach discriminates horizon-problem solutions via perturbation spectra; the companion Signature Edition record specifies the thermometers protocol.",
 "key_points": [
  "CMB uniform to 1 part in 100,000 across disconnected patches.",
  "Inflation arranges pre-expansion causal contact.",
  "Alternatives (VSL, ekpyrotic) arrange contact differently.",
  "The uniformity is observed; the mechanism is open.",
 ],
 "requirements": [
  "Precision primordial spectrum measurements.",
  "Contact mechanisms discriminated on full prediction sets.",
  "No mechanism declared from uniformity alone.",
 ],
 "citations": [
  "Guth AH (1981) Inflationary universe. Physical Review D 23.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 110.0},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "co-first-stars",
 "name": "The First Stars Problem",
 "group": "Structure Formation",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "The first stars - Population III - lit up the dark ages, but none have been seen: what were they like, and how did they form?",
 "background": "Population III stars - the first, metal-free stars - are predicted to be massive (tens to hundreds of solar masses) because metal-free gas cools inefficiently, but the prediction is theoretical: no Pop III star has been observed (they died long ago), and the initial mass function is debated (recent simulations suggest fragmentation into smaller masses). Their supernovae seeded the first metals and may have made the first black holes. JWST hunts their galaxies; the 21-cm line may see their era. The first stars are known only by their predicted shadows.",
 "why_it_matters": "The first stars made the first metals, the first light, possibly the first black holes. Everything began with stars nobody has seen.",
 "sig_lens": "The Signature lens reads Pop III as the universe's first fire: the protocol must find its smoke (metals, 21-cm, black holes) since the flames are gone.",
 "sig_solution": LABEL + " Assumptions: (1) no Pop III star observed; predictions theoretical; (2) mass function debated. Reasoning path: hunt the shadows - metal-poor stars' abundance patterns, 21-cm cosmic dawn, JWST's earliest galaxies, gravitational waves from Pop III remnants. Proposed mechanism: a first-fire protocol with coordinated Pop III remnant hunts, 21-cm cosmic-dawn measurements, and simulation predictions published as falsifiable mass-function tests. Confirm: multiple shadows agree on the mass function. Kill: the shadows contradict and the predictions stay theoretical. Does NOT claim: the first stars' nature - it hunts their smoke.",
 "pointer": "The Signature system's proposed approach hunts Population III through remnant and 21-cm shadows; the companion Signature Edition record specifies the first-fire protocol.",
 "key_points": [
  "No Population III star has ever been observed.",
  "Metal-free gas predicted to make massive stars - debated.",
  "Their supernovae seeded the first metals.",
  "JWST and 21-cm experiments hunt the era.",
 ],
 "requirements": [
  "Coordinated remnant and abundance-pattern hunts.",
  "21-cm cosmic-dawn measurements.",
  "Falsifiable mass-function predictions from simulations.",
 ],
 "citations": [
  "Bromm V, Larson RB (2004) The first stars. Annual Review A&A 42.",
 ],
 "demo": {"h0": 68.0, "d_mpc": 130.0},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "co-reionization",
 "name": "The Reionization Problem",
 "group": "Structure Formation",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "The universe's hydrogen was reionized by the first galaxies - but which sources did it, when, and how did the process unfold?",
 "background": "Cosmic reionization - the ionization of intergalactic hydrogen by the first stars and galaxies (redshift ~6-10) - is constrained by the CMB optical depth (Planck: tau ~0.05, midpoint z~7-8) and quasar absorption, but the sources are debated: faint dwarf galaxies (many, individually dim) versus bright galaxies versus quasars - the ionizing photon budget does not quite close. The topology (inside-out vs outside-in) and the timeline's details are open. JWST is finding the candidate sources; the 21-cm line will map the process. The universe's last phase transition is half-mapped.",
 "why_it_matters": "Reionization is the universe's last global phase transition, driven by the first galaxies. Its sources are galaxy formation's first chapter.",
 "sig_lens": "The Signature lens reads reionization as the dawn: the protocol must find what lit it (the sources) and map how the light spread.",
 "sig_solution": LABEL + " Assumptions: (1) the ionizing photon budget does not close; (2) topology and timeline details open. Reasoning path: close the budget - count the ionizing photons from JWST's galaxies and check against the CMB optical depth; map the topology with 21-cm. Proposed mechanism: a dawn protocol with ionizing-photon censuses, escape-fraction measurements, and 21-cm tomography of the ionization topology. Confirm: the counted photons match the optical depth. Kill: the budget never closes and exotic sources are needed. Does NOT claim: the reionization sources - it counts the dawn's light.",
 "pointer": "The Signature system's proposed approach closes the reionization photon budget with JWST and 21-cm; the companion Signature Edition record specifies the dawn protocol.",
 "key_points": [
  "Reionization at z~6-10; CMB optical depth tau~0.05.",
  "The ionizing photon budget does not quite close.",
  "Faint dwarfs vs bright galaxies vs quasars debated.",
  "Topology (inside-out vs outside-in) is open.",
 ],
 "requirements": [
  "Ionizing-photon censuses from deep surveys.",
  "Escape-fraction measurements.",
  "21-cm tomography of ionization topology.",
 ],
 "citations": [
  "Planck Collaboration (2020) Planck 2018 results VI. A&A 641.",
 ],
 "demo": {"h0": 67.0, "d_mpc": 160.0},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "co-missing-sat",
 "name": "The Missing Satellites Problem",
 "group": "Structure Formation",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Dark-matter simulations predict hundreds of Milky Way satellite galaxies, but far fewer are seen - so where are the missing satellites?",
 "background": "The missing satellites problem - CDM predicts ~hundreds of subhalos around the Milky Way; only ~60 satellites are known - was the first small-scale crisis. Resolutions compete: baryonic physics (reionization and supernova feedback suppress star formation in small halos, leaving dark subhalos), observational incompleteness (faint dwarfs await discovery - and dozens have been found), or dark-matter physics (warm dark matter suppresses small halos). The ultra-faint dwarfs keep being found; the count rises toward the prediction. The problem is shrinking but not closed.",
 "why_it_matters": "The satellite count tests dark matter on small scales. Each new dwarf is a vote for CDM-plus-feedback over new dark physics.",
 "sig_lens": "The Signature lens reads the missing satellites as a census with undercounted districts: the protocol must finish the census before rewriting the demographics (dark matter).",
 "sig_solution": LABEL + " Assumptions: (1) predictions exceed observations; (2) baryonic suppression, incompleteness, and dark physics compete. Reasoning path: complete the census - deep surveys for ultra-faint dwarfs - and test whether the found count matches feedback-suppressed predictions. Proposed mechanism: a census protocol with complete ultra-faint dwarf surveys, star-formation-suppression modeling, and dark-matter-model tests on the completed count. Confirm: the census matches CDM-plus-feedback. Kill: the census completes far below prediction and dark physics is needed. Does NOT claim: the satellites all found - it finishes the census first.",
 "pointer": "The Signature system's proposed approach completes the dwarf census before judging dark-matter models; the companion Signature Edition record specifies the census protocol.",
 "key_points": [
  "CDM predicts hundreds of subhalos; ~60 satellites known.",
  "Reionization and feedback may leave subhalos dark.",
  "Dozens of ultra-faint dwarfs found recently; count rising.",
  "Warm dark matter would suppress small halos.",
 ],
 "requirements": [
  "Complete ultra-faint dwarf surveys.",
  "Star-formation-suppression modeling.",
  "Dark-matter tests on the completed census.",
 ],
 "citations": [
  "Bullock JS, Boylan-Kolchin M (2017) Small-scale challenges to Lambda-CDM. Annual Review A&A 55.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 140.0},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "co-core-cusp",
 "name": "The Core Cusp Problem",
 "group": "Structure Formation",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Dark-matter simulations predict cuspy (peaked) halo centers, but dwarf galaxies show flat cores - so is the dark matter wrong, or are the simulations missing physics?",
 "background": "The core-cusp problem - CDM's NFW cusps (density rising steeply inward) versus dwarf galaxies' observed flat cores - is the sharpest small-scale challenge: the rotation curves of dwarfs prefer cores. Baryonic solutions (supernova feedback flattening cusps via bursty outflows) work in simulations but need the bursty star formation to be real; dark-matter solutions (self-interacting dark matter thermalizing the center) fit elegantly but add physics. The observations (rotation-curve decompositions) carry their own uncertainties (inclination, non-circular motions). The cusp-core debate is the small-scale crisis in miniature.",
 "why_it_matters": "Cores versus cusps is the most direct test of dark matter's nature on galactic scales. The answer is particle physics or feedback - profoundly different.",
 "sig_lens": "The Signature lens reads cores vs cusps as the crime scene: the protocol must determine whether the suspect (dark matter) or the witness (feedback) shaped the scene.",
 "sig_solution": LABEL + " Assumptions: (1) dwarfs prefer cores; simulations predict cusps; (2) feedback vs SIDM compete. Reasoning path: discriminate - test whether the bursty feedback the simulations need is observed, and whether SIDM's other predictions (cluster scales) hold. Proposed mechanism: a crime-scene protocol with star-formation-burstiness observations in dwarfs, SIDM tests on cluster scales, and rotation-curve systematics quantified. Confirm: one suspect's full prediction set verified. Kill: both suspects fit and the scene stays ambiguous. Does NOT claim: the core's cause - it interrogates both suspects.",
 "pointer": "The Signature system's proposed approach discriminates feedback from self-interacting dark matter in dwarf cores; the companion Signature Edition record specifies the crime-scene protocol.",
 "key_points": [
  "CDM predicts NFW cusps; dwarfs show flat cores.",
  "Supernova feedback can flatten cusps if bursty.",
  "Self-interacting dark matter thermalizes centers elegantly.",
  "Rotation-curve decompositions carry systematics.",
 ],
 "requirements": [
  "Dwarf star-formation-burstiness observations.",
  "SIDM tests on cluster scales.",
  "Quantified rotation-curve systematics.",
 ],
 "citations": [
  "de Blok WJG (2010) The core-cusp problem. Advances in Astronomy 2010.",
 ],
 "demo": {"h0": 69.5, "d_mpc": 125.0},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "co-tbtf",
 "name": "The Too Big To Fail Problem",
 "group": "Structure Formation",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "The Milky Way's brightest satellites live in halos too small for their brightness - but the simulations say halos that big should host brighter galaxies, so which is wrong?",
 "background": "Too-big-to-fail - the most massive CDM subhalos are too dense to host the brightest observed dwarfs (they are 'too big to fail' to form stars, yet appear starless) - sharpens the small-scale crisis: it is not just the count (missing satellites) but the densities. Resolutions mirror core-cusp: baryonic feedback lowering central densities, or the Milky Way's mass being lower than assumed (lighter host, lighter subhalos), or self-interacting dark matter. The problem's severity depends on the Milky Way's total mass - itself uncertain by a factor of two.",
 "why_it_matters": "Too-big-to-fail is the small-scale crisis at its sharpest: the densest predicted subhalos have no observed counterparts. The mismatch is structural, not just counting.",
 "sig_lens": "The Signature lens reads too-big-to-fail as overbuilt houses with no tenants: the protocol must check whether the houses (subhalos) are really that big, or the census missed the tenants.",
 "sig_solution": LABEL + " Assumptions: (1) most massive subhalos too dense for brightest dwarfs; (2) Milky Way mass uncertain 2x. Reasoning path: pin the host mass first - the problem's severity scales with it - then test feedback vs SIDM on the densities. Proposed mechanism: an overbuilt protocol with improved Milky Way mass measurements (stellar streams, satellites), subhalo-density tests against the pinned host, and feedback/SIDM discrimination. Confirm: the pinned mass dissolves or confirms the problem cleanly. Kill: the mass stays uncertain and the problem stays ambiguous. Does NOT claim: the subhalo densities' cause - it measures the houses first.",
 "pointer": "The Signature system's proposed approach pins the Milky Way's mass to judge too-big-to-fail; the companion Signature Edition record specifies the overbuilt protocol.",
 "key_points": [
  "Most massive subhalos too dense to host brightest dwarfs.",
  "Milky Way total mass uncertain by factor ~2.",
  "Feedback, lighter host, or SIDM compete as resolutions.",
  "The problem is structural, not just counting.",
 ],
 "requirements": [
  "Improved Milky Way mass measurements.",
  "Subhalo-density tests against pinned host mass.",
  "Feedback versus SIDM discrimination.",
 ],
 "citations": [
  "Boylan-Kolchin M et al. (2011) Too big to fail? MNRAS 415.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 135.0},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "co-btf",
 "name": "The Baryonic Tully Fisher Problem",
 "group": "Structure Formation",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Galaxies obey a tight relation between baryonic mass and rotation speed - but why is it so tight when galaxy formation is so messy?",
 "background": "The baryonic Tully-Fisher relation (BTFR) - M_baryon proportional to V^4 over six decades in mass, with tiny scatter - is unreasonably tight for messy hierarchical formation: CDM simulations reproduce it approximately but with more scatter and wrong systematics. MOND predicts it exactly (it was built to), making the BTFR the modified-gravity camp's best evidence. The tightness suggests a law-like regularity - either a dark-matter conspiracy (feedback tuning) or new dynamics. The relation that should be messy is the cleanest in extragalactic astronomy.",
 "why_it_matters": "The BTFR's tightness is either dark matter's greatest conspiracy or modified gravity's greatest triumph. The cleanest relation is the deepest puzzle.",
 "sig_lens": "The Signature lens reads the BTFR as a suspiciously clean ledger: the protocol must audit whether the cleanliness is physics (a law) or accounting (tuned feedback).",
 "sig_solution": LABEL + " Assumptions: (1) BTFR tight over 6 decades; (2) CDM reproduces approximately; MOND exactly. Reasoning path: test the discriminators - the relation's scatter at the extremes (dwarfs, giants), its redshift evolution, and the residuals' correlation with other properties. Proposed mechanism: a ledger protocol measuring BTFR at extremes and high redshift, testing feedback-tuning versus law-like predictions on the residuals. Confirm: one camp's full prediction set verified. Kill: both camps fit and the tightness stays mysterious. Does NOT claim: the BTFR's cause - it audits the clean ledger.",
 "pointer": "The Signature system's proposed approach tests the BTFR at extremes and high redshift; the companion Signature Edition record specifies the ledger protocol.",
 "key_points": [
  "BTFR: M_baryon ~ V^4 over six decades, tiny scatter.",
  "CDM reproduces approximately with more scatter.",
  "MOND predicts it exactly.",
  "Tightness suggests law or conspiracy.",
 ],
 "requirements": [
  "BTFR measurements at mass extremes and high redshift.",
  "Residual-correlation tests.",
  "Feedback-tuning versus law discrimination.",
 ],
 "citations": [
  "McGaugh SS et al. (2000) The baryonic Tully-Fisher relation. ApJ 533.",
 ],
 "demo": {"h0": 71.0, "d_mpc": 145.0},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "co-lithium",
 "name": "The Cosmological Lithium Problem",
 "group": "Early Universe",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Big Bang nucleosynthesis predicts three times more lithium-7 than old stars show - so is the theory wrong, the stars deceptive, or new physics at work?",
 "background": "The lithium problem - BBN predicts Li-7/H ~5e-10; metal-poor halo stars (the Spite plateau) show ~1.6e-10, a factor-3 gap - persists despite nuclear cross-section remeasurements: the nuclear physics is now too precise to blame. Stellar depletion (lithium burned in the stars) is the astrophysical suspect but needs to be uniform across the plateau; new physics (decaying dark matter, varying constants) is the exotic suspect. BBN works beautifully for hydrogen, helium, deuterium - and fails by 3x on lithium. The one-element failure is the theory's embarrassment.",
 "why_it_matters": "BBN is the early universe's precision test; it passes on three elements and fails on the fourth. The failure is either stellar or new physics.",
 "sig_lens": "The Signature lens reads lithium as the one wrong answer on an otherwise perfect exam: the protocol must check whether the student (stars) or the exam (theory) is at fault.",
 "sig_solution": LABEL + " Assumptions: (1) nuclear physics too precise to blame; (2) stellar depletion vs new physics compete. Reasoning path: test the stellar suspect - measure lithium in the most pristine stars and model depletion; test new physics on its other predictions. Proposed mechanism: a wrong-answer protocol with ultra-metal-poor lithium measurements, stellar-depletion modeling, and new-physics candidates tested on full prediction sets. Confirm: one suspect confirmed, the other excluded. Kill: both remain viable and the factor 3 stands. Does NOT claim: the lithium gap's cause - it interrogates student and exam.",
 "pointer": "The Signature system's proposed approach tests stellar depletion versus new physics for the lithium gap; the companion Signature Edition record specifies the wrong-answer protocol.",
 "key_points": [
  "BBN predicts 3x more Li-7 than the Spite plateau shows.",
  "Nuclear cross-sections remeasured; physics too precise to blame.",
  "Stellar depletion needs uniformity across the plateau.",
  "BBN succeeds on H, He, D - fails only on Li.",
 ],
 "requirements": [
  "Lithium in ultra-metal-poor stars.",
  "Stellar-depletion modeling.",
  "New-physics candidates on full prediction sets.",
 ],
 "citations": [
  "Fields BD (2011) The primordial lithium problem. Annual Review Nuclear and Particle Science 61.",
 ],
 "demo": {"h0": 68.5, "d_mpc": 155.0},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "co-cc-problem",
 "name": "The Cosmological Constant Problem",
 "group": "Dark Sector",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Quantum field theory predicts vacuum energy 10^120 times larger than observed - the worst prediction in physics, so what cancels it?",
 "background": "The cosmological constant problem - QFT's vacuum energy exceeds the observed Lambda by ~120 orders of magnitude - is the worst theoretical prediction in science: every known cancellation mechanism (supersymmetry, etc.) fails or is excluded, and the observed value sits absurdly close to zero without being zero. Anthropic selection in a multiverse is the most-discussed resolution (Weinberg's prediction of the rough value); dynamical cancellation mechanisms remain speculative. The problem is not that Lambda is unexplained - it is that theory predicts something monstrous and observation finds nearly nothing.",
 "why_it_matters": "The 120-order gap is physics' worst prediction. Its resolution rewrites quantum field theory, gravity, or our place in the multiverse.",
 "sig_lens": "The Signature lens reads the constant problem as a bill for 10^120 with a payment of ~0: the protocol must find the accountant (the cancellation) or accept the multiverse's lottery.",
 "sig_solution": LABEL + " Assumptions: (1) QFT predicts monstrous vacuum energy; (2) cancellation mechanisms fail or excluded. Reasoning path: pursue the live options - test dynamical dark energy (which reframes the problem), develop cancellation mechanisms, and test anthropic predictions. Proposed mechanism: an accountant protocol measuring dark-energy dynamics (a dynamical Lambda changes the problem), advancing sequester/unimodular proposals, and testing multiverse predictions where testable. Confirm: one approach yields verified predictions. Kill: all approaches stall and the 120 orders stand. Does NOT claim: the cancellation - it hunts the accountant.",
 "pointer": "The Signature system's proposed approach attacks the cosmological constant problem via dynamics and cancellation mechanisms; the companion Signature Edition record specifies the accountant protocol.",
 "key_points": [
  "QFT vacuum energy exceeds observed Lambda by ~10^120.",
  "Worst theoretical prediction in physics.",
  "Cancellation mechanisms fail or are excluded.",
  "Anthropic multiverse is the most-discussed resolution.",
 ],
 "requirements": [
  "Dark-energy dynamics measurements.",
  "Cancellation-mechanism development (sequester, unimodular).",
  "Multiverse predictions tested where testable.",
 ],
 "citations": [
  "Weinberg S (1989) The cosmological constant problem. Reviews of Modern Physics 61.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 170.0},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "co-vacuum",
 "name": "The Vacuum Energy Problem",
 "group": "Dark Sector",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Empty space has energy - but what is the vacuum, and why does its energy gravitate so differently from every theoretical expectation?",
 "background": "The vacuum energy problem - the physical nature of the energy of empty space - underlies the cosmological constant problem: QFT says the vacuum seethes with zero-point energy; general relativity says all energy gravitates; together they predict absurd curvature. But the vacuum's energy may not gravitate as naive QFT suggests (the Casimir effect measures differences, not absolutes). The problem touches the foundations: what is 'nothing', and does it weigh? The observed acceleration says the vacuum (or something) has tiny positive energy; theory cannot produce tiny.",
 "why_it_matters": "The vacuum is physics' 'nothing' - and it may drive the cosmic acceleration. Understanding nothing is the prerequisite to understanding everything.",
 "sig_lens": "The Signature lens reads the vacuum as the heaviest nothing: the protocol must weigh nothing carefully (Casimir, Lamb shift) and ask why it weighs so little cosmologically.",
 "sig_solution": LABEL + " Assumptions: (1) QFT vacuum seethes; GR says it gravitates; (2) lab measures differences, not absolutes. Reasoning path: probe the vacuum's gravity directly - test whether vacuum energy gravitates as expected, and develop theories where it does not. Proposed mechanism: a nothing protocol with precision tests of vacuum-energy gravitation, theoretical development on degravitation/sequester ideas, and cosmological measurements of vacuum-like behavior. Confirm: vacuum gravitation measured or a working degravitation theory. Kill: the vacuum's gravity stays untestable. Does NOT claim: the vacuum's nature - it weighs nothing carefully.",
 "pointer": "The Signature system's proposed approach probes whether vacuum energy gravitates as expected; the companion Signature Edition record specifies the nothing protocol.",
 "key_points": [
  "QFT: vacuum seethes with zero-point energy.",
  "GR: all energy gravitates - predicting absurd curvature.",
  "Lab effects (Casimir) measure differences, not absolute energy.",
  "Observed acceleration needs tiny positive vacuum-like energy.",
 ],
 "requirements": [
  "Precision tests of vacuum-energy gravitation.",
  "Degravitation/sequester theory development.",
  "Cosmological vacuum-behavior measurements.",
 ],
 "citations": [
  "Carroll SM (2001) The cosmological constant. Living Reviews in Relativity 4.",
 ],
 "demo": {"h0": 69.0, "d_mpc": 185.0},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "co-inflation-models",
 "name": "The Inflation Model Problem",
 "group": "Early Universe",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Hundreds of inflation models exist - but which one actually inflated the universe, and how can they be told apart?",
 "background": "The inflation model problem - ~100+ published potentials, most fitting current data - is the paradigm's flexibility embarrassment: with enough model-building freedom, any (n_s, r) outcome can be accommodated. Planck's tight constraints (n_s ~0.965, r < 0.06) killed many models but left dozens; the inflaton's identity (Higgs? axion? modulus?) is unknown; and the reheating physics connecting inflation to the hot Big Bang is unconstrained. Inflation predicts the perturbation pattern generically; the specific model is underdetermined. The paradigm works; the model is a menu.",
 "why_it_matters": "Inflation is the early universe's paradigm; its model is unknown. The menu of 100+ is the paradigm's unfalsifiability risk.",
 "sig_lens": "The Signature lens reads inflation models as a menu with 100 dishes: the protocol must find the dish the universe ordered - via the check (precision data), not the menu description.",
 "sig_solution": LABEL + " Assumptions: (1) 100+ models fit current data; (2) inflaton identity unknown. Reasoning path: shrink the menu with precision data - tensor modes (r), non-Gaussianity, running, reheating constraints - each kills model classes. Proposed mechanism: a menu protocol with B-mode polarization hunts for tensors, non-Gaussianity constraints, and reheating-physics probes, eliminating model classes systematically. Confirm: surviving models converge on an identity. Kill: the data never discriminates and the menu stays. Does NOT claim: the inflation model - it shrinks the menu by the check.",
 "pointer": "The Signature system's proposed approach discriminates inflation models with tensors and non-Gaussianity; the companion Signature Edition record specifies the menu protocol.",
 "key_points": [
  "100+ inflation models fit current data.",
  "Planck: n_s~0.965, r<0.06 - killed many, left dozens.",
  "Inflaton identity unknown; reheating unconstrained.",
  "Flexibility is the paradigm's unfalsifiability risk.",
 ],
 "requirements": [
  "B-mode polarization tensor hunts.",
  "Non-Gaussianity and running constraints.",
  "Reheating-physics probes.",
 ],
 "citations": [
  "Martin J et al. (2014) Encyclopaedia inflationaris. Physics of the Dark Universe 5-6.",
 ],
 "demo": {"h0": 70.5, "d_mpc": 150.0},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "co-transplanckian",
 "name": "The Trans Planckian Problem",
 "group": "Early Universe",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Inflation stretches quantum fluctuations from below the Planck scale - but can physics be trusted when the seeds of galaxies came from beyond its validity?",
 "background": "The trans-Planckian problem - the CMB's fluctuations originated as sub-Planckian modes stretched by inflation, beyond QFT's validity - questions inflation's predictions: if the initial conditions were set in unknown quantum-gravity territory, the predicted spectrum might carry trans-Planckian imprints (or the predictions might be robust - the debate). The trans-Planckian censorship conjecture (no trans-Planckian mode ever exits the horizon) would constrain inflation's duration. The problem is the paradigm's foundation touching the unknown: the seeds are trusted, their nursery is not.",
 "why_it_matters": "The CMB's seeds came from beyond known physics. If the nursery matters, inflation's predictions need quantum gravity; if not, the robustness needs proof.",
 "sig_lens": "The Signature lens reads trans-Planckian modes as seeds from an unknown nursery: the protocol must check whether the nursery left marks on the grown tree (the CMB).",
 "sig_solution": LABEL + " Assumptions: (1) CMB modes were sub-Planckian; (2) robustness debated. Reasoning path: hunt the nursery's marks - trans-Planckian imprints would appear as specific spectral features; test the censorship conjecture's predictions. Proposed mechanism: a nursery protocol with precision CMB spectral-feature hunts, trans-Planckian-censorship tests on inflation's duration, and quantum-gravity phenomenology tied to observables. Confirm: imprints found or robustness proven. Kill: neither imprint nor proof emerges. Does NOT claim: quantum gravity - it checks the nursery marks.",
 "pointer": "The Signature system's proposed approach hunts trans-Planckian imprints in the CMB spectrum; the companion Signature Edition record specifies the nursery protocol.",
 "key_points": [
  "CMB fluctuations began as sub-Planckian modes.",
  "QFT validity fails at the Planck scale.",
  "Trans-Planckian imprints would mark the spectrum.",
  "Censorship conjecture would limit inflation's duration.",
 ],
 "requirements": [
  "Precision CMB spectral-feature hunts.",
  "Trans-Planckian-censorship tests.",
  "Quantum-gravity phenomenology tied to observables.",
 ],
 "citations": [
  "Martin J, Brandenberger RH (2001) The trans-Planckian problem of inflationary cosmology. PRD 63.",
 ],
 "demo": {"h0": 68.0, "d_mpc": 190.0},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "co-eternal",
 "name": "The Eternal Inflation Problem",
 "group": "Early Universe",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Inflation, once started, may never end globally - but if our universe is one bubble in an eternal inflating sea, how can anything be predicted?",
 "background": "Eternal inflation - most inflation models inflate forever globally, spawning bubble universes - creates the measure problem: with infinite bubbles, every outcome occurs infinitely often, and probabilities need a measure (a way to count infinities) that is arbitrary - different measures give different predictions. The youngness paradox, the Boltzmann-brain problem, and measure-dependence each challenge prediction. Eternal inflation may be generic; the measure is not. The paradigm predicts everything and therefore nothing, until the measure is found.",
 "why_it_matters": "If inflation is eternal, prediction needs a measure over infinities. The measure problem is the paradigm's prediction crisis.",
 "sig_lens": "The Signature lens reads eternal inflation as an infinite lottery: the protocol must find the fair way to count the tickets before announcing the odds.",
 "sig_solution": LABEL + " Assumptions: (1) eternal inflation generic in models; (2) measures arbitrary, predictions measure-dependent. Reasoning path: derive the measure from physics, not choice - seek principles (holography, quantum cosmology) fixing the counting. Proposed mechanism: a lottery protocol developing physical measure principles, testing measures on their predictions, and quarantining measure-dependent claims. Confirm: a principled measure yields stable predictions. Kill: no principle found and eternal inflation stays unpredictive. Does NOT claim: the measure - it seeks the fair counting.",
 "pointer": "The Signature system's proposed approach derives eternal-inflation measures from physical principles; the companion Signature Edition record specifies the lottery protocol.",
 "key_points": [
  "Most inflation models inflate eternally, spawning bubbles.",
  "Infinite bubbles need a measure for probabilities.",
  "Measures are arbitrary; predictions depend on choice.",
  "Boltzmann brains and youngness paradoxes result.",
 ],
 "requirements": [
  "Physical (not chosen) measure principles.",
  "Measure testing on predictions.",
  "Quarantine of measure-dependent claims.",
 ],
 "citations": [
  "Guth AH (2007) Eternal inflation and its implications. J. Physics A 40.",
 ],
 "demo": {"h0": 71.5, "d_mpc": 175.0},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "co-multiverse",
 "name": "The Multiverse Testability Problem",
 "group": "Early Universe",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "The multiverse may explain fine-tuning - but if other universes are unobservable, is it science or metaphysics?",
 "background": "The multiverse testability problem - whether unobservable other universes count as science - is cosmology's demarcation debate: the multiverse explains fine-tuning (constants vary across bubbles; we live where observers can), but direct observation is impossible by construction. Defenders cite indirect testability (predictions for our universe's constants); critics cite Popper and call it metaphysics. The debate entangles physics with philosophy of science - and with the cosmological constant and string landscape. The multiverse is either the explanation or the abdication.",
 "why_it_matters": "The multiverse is the leading explanation of fine-tuning - and possibly untestable. The demarcation decides whether cosmology's biggest idea is science.",
 "sig_lens": "The Signature lens reads the multiverse as an explanation that cannot be visited: the protocol must demand it pay rent - predictions for our universe - or evict it from science.",
 "sig_solution": LABEL + " Assumptions: (1) other universes unobservable by construction; (2) fine-tuning explained conditionally. Reasoning path: demand rent - the multiverse must predict our universe's constants' distributions better than single-universe theories. Proposed mechanism: a rent protocol requiring multiverse proposals to make testable predictions for our constants, comparing against single-universe explanations, and labeling untestable variants as metaphysics. Confirm: rent paid in verified predictions. Kill: no rent forthcoming and the multiverse stays philosophy. Does NOT claim: the multiverse's existence - it demands the rent.",
 "pointer": "The Signature system's proposed approach demands testable predictions from multiverse proposals; the companion Signature Edition record specifies the rent protocol.",
 "key_points": [
  "Multiverse explains fine-tuning via varied constants.",
  "Other universes unobservable by construction.",
  "Indirect testability (our constants' distributions) debated.",
  "Demarcation: science or metaphysics.",
 ],
 "requirements": [
  "Testable predictions for our universe's constants.",
  "Comparison against single-universe explanations.",
  "Untestable variants labeled metaphysics.",
 ],
 "citations": [
  "Ellis GFR (2011) Does the multiverse really exist? Scientific American 305.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 200.0},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "co-cmb-anomalies",
 "name": "The Cosmic Microwave Background Anomalies Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "The CMB is beautifully consistent with Lambda-CDM - except for a handful of anomalies that will not go away, so are they new physics or statistical flukes?",
 "background": "CMB anomalies - the low quadrupole, the hemispherical power asymmetry, the cold spot, alignments of low multipoles - persist from WMAP through Planck: individually ~2-3 sigma, collectively suggestive, each possibly a fluke (look-elsewhere effect) or new physics (nontrivial topology, pre-inflationary relics, cosmic textures). The anomalies' significance is debated because they were found a posteriori. Planck's final word: consistent with Lambda-CDM, anomalies intriguing but inconclusive. The beautiful model's blemishes will not fade.",
 "why_it_matters": "The anomalies are the CMB's blemishes on a beautiful model. Flukes or physics - the answer is either nothing or the next discovery.",
 "sig_lens": "The Signature lens reads the anomalies as blemishes: the protocol must determine whether they are birthmarks (physics) or smudges (statistics) - with pre-registered tests.",
 "sig_solution": LABEL + " Assumptions: (1) anomalies 2-3 sigma, found a posteriori; (2) look-elsewhere effect inflates significance. Reasoning path: test pre-registered - define the anomaly tests before the next dataset, and require new-data confirmation. Proposed mechanism: a blemishes protocol with pre-registered anomaly tests for future CMB data, blinded analyses, and new-physics models required to predict (not postdict) the anomalies. Confirm: pre-registered tests confirm an anomaly. Kill: new data washes them out. Does NOT claim: the anomalies' reality - it tests without smudging.",
 "pointer": "The Signature system's proposed approach tests CMB anomalies with pre-registered blinded analyses; the companion Signature Edition record specifies the blemishes protocol.",
 "key_points": [
  "Low quadrupole, hemispherical asymmetry, cold spot persist.",
  "Individually 2-3 sigma; found a posteriori.",
  "Look-elsewhere effect inflates significance.",
  "Planck: consistent with Lambda-CDM, anomalies inconclusive.",
 ],
 "requirements": [
  "Pre-registered anomaly tests for future data.",
  "Blinded CMB analyses.",
  "New-physics models predicting, not postdicting.",
 ],
 "citations": [
  "Planck Collaboration (2020) Planck 2018 results VII: Isotropy and statistics. A&A 641.",
 ],
 "demo": {"h0": 69.0, "d_mpc": 165.0},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "co-axis",
 "name": "The Axis of Evil Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "The CMB's largest patterns align along a mysterious axis - but is the 'axis of evil' real cosmology, or a foreground subtraction artifact?",
 "background": "The axis of evil - the alignment of the CMB quadrupole and octopole along a common axis (roughly toward Virgo) - challenges statistical isotropy: the chance alignment is ~1-in-1000 in naive estimates, though the a posteriori statistics are debated. Explanations range from foreground/systematic residuals to nontrivial cosmic topology to pre-inflationary physics. Planck confirmed the alignments exist in the cleaned maps; whether they are cosmological is unresolved. The axis is either the universe's preferred direction or the foreground-removal's fingerprint.",
 "why_it_matters": "A preferred cosmic direction would break the cosmological principle. The axis is either revolutionary or a cleaning artifact.",
 "sig_lens": "The Signature lens reads the axis as a possible fingerprint: the protocol must check whether the print belongs to the universe or to the cleaners (foreground removal).",
 "sig_solution": LABEL + " Assumptions: (1) alignments confirmed in cleaned maps; (2) cosmological vs systematic unresolved. Reasoning path: vary the cleaning - test whether the axis survives independent foreground-removal methods and frequencies. Proposed mechanism: a fingerprint protocol with multi-method foreground cleaning, frequency-dependence tests of the alignments, and topological models tested on full predictions. Confirm: the axis survives all cleanings achromatically. Kill: it varies with cleaning method. Does NOT claim: a cosmic axis - it checks the print's owner.",
 "pointer": "The Signature system's proposed approach tests the CMB axis against foreground-cleaning variations; the companion Signature Edition record specifies the fingerprint protocol.",
 "key_points": [
  "Quadrupole and octopole align along a common axis.",
  "Naive chance ~1-in-1000; a posteriori stats debated.",
  "Planck confirmed alignments in cleaned maps.",
  "Topology, pre-inflation physics, or systematics compete.",
 ],
 "requirements": [
  "Multi-method foreground-cleaning comparisons.",
  "Frequency-dependence tests of alignments.",
  "Topological models on full predictions.",
 ],
 "citations": [
  "Land K, Magueijo J (2005) Examination of evidence for the preferred axis in the cosmic radiation. PRL 95.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 155.0},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "co-cold-spot",
 "name": "The Cold Spot Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "A giant cold region mars the CMB - but is the Cold Spot a supervoid's shadow, a cosmic texture, or just the coldest random fluctuation?",
 "background": "The CMB Cold Spot - a ~10-degree, ~70-microK cold region - is the most significant single anomaly: supervoid explanations (a giant void's integrated Sachs-Wolfe shadow) need a void bigger than observed (the Eridanus supervoid is too small); cosmic textures (topological defects) fit the profile but need independent evidence; and the random-fluctuation explanation is statistically allowed but unsatisfying. The Cold Spot is either the largest structure's shadow, new physics' signature, or the coldest dice roll. Three explanations, one spot.",
 "why_it_matters": "The Cold Spot is the CMB's single strangest feature. Its explanation is either the largest void, new physics, or chance - three profoundly different universes.",
 "sig_lens": "The Signature lens reads the Cold Spot as a bruise: the protocol must find what struck - the void, the defect, or the dice.",
 "sig_solution": LABEL + " Assumptions: (1) Eridanus supervoid too small for full ISW explanation; (2) textures need independent evidence. Reasoning path: complete the void census along the line of sight and hunt texture signatures elsewhere. Proposed mechanism: a bruise protocol with deep void mapping toward the Cold Spot, texture-model predictions tested on other CMB features, and statistical reanalysis with proper a posteriori accounting. Confirm: the census or the textures explain it. Kill: none do and the dice stand. Does NOT claim: the Cold Spot's cause - it finds what struck.",
 "pointer": "The Signature system's proposed approach completes the Cold Spot void census and tests texture models; the companion Signature Edition record specifies the bruise protocol.",
 "key_points": [
  "~10-degree, ~70-microK cold region.",
  "Eridanus supervoid too small for full explanation.",
  "Cosmic textures fit but lack independent evidence.",
  "Random fluctuation statistically allowed.",
 ],
 "requirements": [
  "Deep void census toward the Cold Spot.",
  "Texture predictions tested on other features.",
  "Proper a posteriori statistical accounting.",
 ],
 "citations": [
  "Vielva P et al. (2004) Detection of non-Gaussianity in the WMAP 1-year data using spherical wavelets. ApJ 609.",
 ],
 "demo": {"h0": 68.0, "d_mpc": 180.0},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "co-pbh",
 "name": "The Primordial Black Holes Problem",
 "group": "Dark Sector",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Black holes may have formed in the Big Bang's first second - but do primordial black holes exist, and could they be the dark matter?",
 "background": "Primordial black holes (PBHs) - formed from direct collapse of overdense regions in the early universe, not from stars - could span asteroid to solar masses: the asteroid-mass window remains open for all-dark-matter PBHs, while LIGO's black holes revived solar-mass interest. Constraints (microlensing, CMB accretion, Hawking evaporation) carve the allowed windows; the formation needs enhanced primordial fluctuations. PBHs are the dark-matter candidate needing no new particles - just gravity and the early universe. The windows are narrow but open.",
 "why_it_matters": "PBHs could be the dark matter with no new particles - the most economical solution, if the windows hold.",
 "sig_lens": "The Signature lens reads PBHs as the economical suspect: the protocol must check the remaining windows (microlensing, evaporation) before closing the case.",
 "sig_solution": LABEL + " Assumptions: (1) asteroid-mass window open for all-DM; (2) formation needs enhanced fluctuations. Reasoning path: probe the windows - next-generation microlensing (Roman) and evaporation searches (gamma rays) - and test formation models on the fluctuation spectrum. Proposed mechanism: a suspect protocol with microlensing surveys of the open windows, Hawking-evaporation gamma-ray searches, and formation models tied to measured fluctuation constraints. Confirm: a window yields detections. Kill: the windows close and PBHs are ruled out as all-DM. Does NOT claim: PBH dark matter - it checks the economical suspect.",
 "pointer": "The Signature system's proposed approach probes primordial-black-hole dark-matter windows; the companion Signature Edition record specifies the suspect protocol.",
 "key_points": [
  "PBHs form from early-universe collapse, not stars.",
  "Asteroid-mass window open for all-dark-matter.",
  "LIGO revived solar-mass PBH interest.",
  "No new particles needed - just gravity.",
 ],
 "requirements": [
  "Next-generation microlensing window surveys.",
  "Hawking-evaporation gamma-ray searches.",
  "Formation models tied to fluctuation constraints.",
 ],
 "citations": [
  "Carr B, Kuhnel F (2020) Primordial black holes as dark matter. Annual Review Nuclear and Particle Science 70.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 195.0},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "co-21cm",
 "name": "The Dark Ages 21cm Problem",
 "group": "Structure Formation",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "The 21-cm line could map the universe's dark ages - but the EDGES claimed a signal twice as deep as possible, so what is the 21-cm sky actually saying?",
 "background": "The 21-cm dark-ages problem - the EDGES experiment's claimed z~17 absorption trough, twice as deep as standard cosmology allows - sparked exotic explanations (dark-matter-baryon cooling, extra radio background) before SARAS-3 failed to confirm it: the signal may be systematic. Meanwhile HERA, LOFAR, and MWA hunt the power spectrum; the lunar far side (LuSEE, FARSIDE concepts) offers RFI-free observing. The 21-cm line is the only probe of the dark ages - and the claimed first detection is disputed. The dark ages are cosmology's unobserved era.",
 "why_it_matters": "The 21-cm line is the only window into the dark ages. A confirmed signal would be the first data from the universe's unobserved era.",
 "sig_lens": "The Signature lens reads the 21-cm dispute as a contested telegram: the protocol must verify the sender (independent experiments) before decoding the message.",
 "sig_solution": LABEL + " Assumptions: (1) EDGES unconfirmed by SARAS-3; (2) systematics plague global-signal experiments. Reasoning path: confirm independently - multiple experiments, lunar far-side observations, and power-spectrum cross-checks. Proposed mechanism: a telegram protocol with independent global-signal verification, power-spectrum measurements (HERA), and lunar far-side missions, decoding only confirmed signals. Confirm: independent experiments agree. Kill: the signal is systematic and the dark ages stay silent. Does NOT claim: the dark-ages signal - it verifies the sender first.",
 "pointer": "The Signature system's proposed approach verifies 21-cm dark-ages signals independently; the companion Signature Edition record specifies the telegram protocol.",
 "key_points": [
  "EDGES claimed a z~17 trough twice the allowed depth.",
  "SARAS-3 did not confirm; systematics suspected.",
  "HERA, LOFAR, MWA hunt the power spectrum.",
  "Lunar far side offers RFI-free observing.",
 ],
 "requirements": [
  "Independent global-signal verification.",
  "Power-spectrum cross-checks.",
  "Lunar far-side mission development.",
 ],
 "citations": [
  "Bowman JD et al. (2018) An absorption profile centred at 78 MHz in the sky-averaged spectrum. Nature 555.",
 ],
 "demo": {"h0": 67.5, "d_mpc": 210.0},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "co-frb",
 "name": "The Fast Radio Burst Origin Problem",
 "group": "High Energy",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Millisecond radio flashes arrive from across the universe - but what makes fast radio bursts, and why do some repeat?",
 "background": "Fast radio bursts (FRBs) - millisecond, Jansky-level radio transients from cosmological distances - were a mystery until the 2020 Galactic magnetar burst (SGR 1935+2154) proved magnetars make at least some: but the repeating vs non-repeating populations may differ, the emission mechanism (coherent curvature, maser) is debated, and the energy requirements strain magnetar models for the brightest. CHIME finds hundreds; host galaxies are being identified. FRBs are also becoming cosmological probes (dispersion-measure cosmology, the missing baryons). The flashes are found; the engine is half-known.",
 "why_it_matters": "FRBs are the brightest radio transients known. Their engines - and their use as cosmic probes - hinge on the origin.",
 "sig_lens": "The Signature lens reads FRBs as cosmic lighthouses: the protocol must find the lamp (the engine) and then use the light (the probes).",
 "sig_solution": LABEL + " Assumptions: (1) magnetars make some FRBs; (2) repeaters vs non-repeaters may differ. Reasoning path: classify the populations - compare repeater and apparent-non-repeater hosts, energetics, and polarization - and test emission mechanisms. Proposed mechanism: a lighthouse protocol with population-classified FRB samples, host-galaxy and local-environment studies, and emission-mechanism tests against polarization and spectra. Confirm: the populations separate cleanly with mechanisms. Kill: the populations blur and one mechanism strains. Does NOT claim: the FRB engine - it finds the lamp, then uses the light.",
 "pointer": "The Signature system's proposed approach classifies FRB populations to pin the engines; the companion Signature Edition record specifies the lighthouse protocol.",
 "key_points": [
  "FRBs: millisecond radio flashes from cosmological distances.",
  "The 2020 Galactic magnetar burst proved magnetars make some.",
  "Repeating vs non-repeating populations may differ.",
  "Emission mechanism (curvature vs maser) debated.",
 ],
 "requirements": [
  "Population-classified FRB samples.",
  "Host and environment studies per population.",
  "Emission-mechanism tests on polarization/spectra.",
 ],
 "citations": [
  "CHIME/FRB Collaboration (2021) The first CHIME/FRB Fast Radio Burst catalog. ApJS 257.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 220.0},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "co-gwb",
 "name": "The Gravitational Wave Background Problem",
 "group": "High Energy",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Pulsar timing arrays hear a nanohertz gravitational-wave hum - but is it supermassive black-hole binaries, or something from the early universe?",
 "background": "The gravitational-wave background problem - NANOGrav, EPTA, PPTA's 2023 evidence for a nanohertz stochastic background - is the attribution question: supermassive black-hole binaries (the expected source) fit approximately but need efficient binary merger physics; cosmological sources (inflation, phase transitions, cosmic strings) fit too. The spectrum's shape and any anisotropy will discriminate - but the current data cannot. LISA (millihertz) and pulsar arrays (nanohertz) will bracket the background; the hum's composer is unknown.",
 "why_it_matters": "The nanohertz hum is either the universe's biggest black holes or the early universe's echo. The composer decides what the hum teaches.",
 "sig_lens": "The Signature lens reads the hum as a cosmic chord: the protocol must resolve its notes (spectrum, anisotropy) to name the composer.",
 "sig_solution": LABEL + " Assumptions: (1) SMBH binaries expected but need efficient mergers; (2) cosmological sources fit too. Reasoning path: resolve the chord - measure the spectral shape and anisotropy precisely; each composer predicts differently. Proposed mechanism: a chord protocol with extended pulsar-timing datasets, spectral-shape and anisotropy measurements, and binary-population models tested against the resolved background. Confirm: the resolved background matches one composer. Kill: the data never resolves and both fit. Does NOT claim: the background's source - it resolves the chord.",
 "pointer": "The Signature system's proposed approach resolves the nanohertz background's spectrum and anisotropy; the companion Signature Edition record specifies the chord protocol.",
 "key_points": [
  "Pulsar timing arrays found nanohertz background evidence (2023).",
  "SMBH binaries fit approximately; need efficient mergers.",
  "Cosmological sources (inflation, strings) fit too.",
  "Spectrum shape and anisotropy will discriminate.",
 ],
 "requirements": [
  "Extended pulsar-timing datasets.",
  "Spectral-shape and anisotropy measurements.",
  "Binary-population models tested on resolved data.",
 ],
 "citations": [
  "NANOGrav Collaboration (2023) The NANOGrav 15-year data set. ApJ 951.",
 ],
 "demo": {"h0": 69.0, "d_mpc": 230.0},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "co-uhecr",
 "name": "The Ultra High Energy Cosmic Ray Problem",
 "group": "High Energy",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Particles arrive with the energy of a thrown baseball in a single proton - but what accelerates ultra-high-energy cosmic rays, and why is there a cutoff?",
 "background": "Ultra-high-energy cosmic rays (UHECRs, >10^18 eV) - the Oh-My-God particle's kin - need extreme accelerators (AGN jets, gamma-ray bursts, starbursts?) that remain unidentified: arrival directions are nearly isotropic (magnetic deflections blur them), composition is debated (Auger suggests heavier nuclei at the top), and the GZK cutoff (interaction with the CMB) shapes the spectrum's end. The sources are the universe's most extreme accelerators - unidentified. Multi-messenger (neutrinos, gamma rays) may triangulate them.",
 "why_it_matters": "UHECRs are nature's most extreme accelerators, dwarfing the LHC by a million. Their identity is the high-energy universe's biggest question.",
 "sig_lens": "The Signature lens reads UHECRs as bullets without a gun: the protocol must triangulate the shooter with every messenger (particles, neutrinos, light).",
 "sig_solution": LABEL + " Assumptions: (1) arrival directions blurred by magnetic fields; (2) composition debated. Reasoning path: triangulate - combine UHECR composition, anisotropy, neutrinos, and gamma rays to corner the sources. Proposed mechanism: a bullets protocol with composition-resolved anisotropy studies, neutrino-UHECR correlation hunts, and source-population modeling against the multi-messenger data. Confirm: one source class triangulated. Kill: the deflections defeat triangulation. Does NOT claim: the UHECR sources - it triangulates the shooter.",
 "pointer": "The Signature system's proposed approach triangulates UHECR sources multi-messenger; the companion Signature Edition record specifies the bullets protocol.",
 "key_points": [
  "UHECRs exceed 10^18 eV - a million times the LHC.",
  "Sources unidentified; directions blurred magnetically.",
  "Composition debated (Auger: heavier at top).",
  "GZK cutoff shapes the spectrum's end.",
 ],
 "requirements": [
  "Composition-resolved anisotropy studies.",
  "Neutrino-UHECR correlation hunts.",
  "Multi-messenger source-population modeling.",
 ],
 "citations": [
  "Pierre Auger Collaboration (2017) Observation of a large-scale anisotropy. Science 357.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 240.0},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "co-homogeneity",
 "name": "The Cosmic Homogeneity Scale Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "The cosmological principle assumes large-scale homogeneity - but structures keep being found at ever-larger scales, so where does homogeneity actually begin?",
 "background": "The homogeneity-scale problem - giant structures (the Huge-LQG at ~1 Gpc, the Hercules-Corona Borealis Great Wall at ~2-3 Gpc, the Giant Arc) challenge the expected ~370 Mpc homogeneity scale: each discovery is debated (selection effects? a posteriori statistics?), but the pattern of ever-larger structures strains the cosmological principle's comfortable assumptions. The fractal-vs-homogeneous debate is old; the new structures reopen it. If homogeneity fails at Gpc scales, the FLRW metric - all of precision cosmology - needs re-examination.",
 "why_it_matters": "The cosmological principle underlies every cosmological measurement. Gpc-scale structures would crack its foundation.",
 "sig_lens": "The Signature lens reads the great structures as stress tests: the protocol must verify each structure rigorously before declaring the principle broken.",
 "sig_solution": LABEL + " Assumptions: (1) structures reported at ever-larger scales; (2) selection effects debated. Reasoning path: verify rigorously - homogeneous surveys, blinded structure searches, and proper a posteriori statistics. Proposed mechanism: a stress-test protocol with blinded large-scale-structure searches, homogeneity-scale measurements on uniform surveys, and FLRW-violation thresholds defined in advance. Confirm: verified Gpc structures break the scale. Kill: the structures dissolve under rigorous statistics. Does NOT claim: homogeneity violated - it stress-tests the principle.",
 "pointer": "The Signature system's proposed approach stress-tests cosmic homogeneity with blinded structure searches; the companion Signature Edition record specifies the stress-test protocol.",
 "key_points": [
  "Giant structures reported at Gpc scales.",
  "Expected homogeneity scale ~370 Mpc.",
  "Selection effects and a posteriori stats debated.",
  "FLRW metric assumes the principle.",
 ],
 "requirements": [
  "Blinded large-scale-structure searches.",
  "Homogeneity measurements on uniform surveys.",
  "Pre-defined FLRW-violation thresholds.",
 ],
 "citations": [
  "Clowes RG et al. (2013) A structure in the early universe at z~1.3 (Huge-LQG). MNRAS 429.",
 ],
 "demo": {"h0": 68.5, "d_mpc": 250.0},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "co-backreaction",
 "name": "The Cosmological Backreaction Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "The universe is lumpy, but cosmology averages it smooth - but does the averaging itself change the expansion, mimicking dark energy?",
 "background": "The backreaction problem - whether small-scale inhomogeneities, averaged via Einstein's nonlinear equations, produce large-scale expansion effects - asks if dark energy is partly an averaging artifact: the timescape and related proposals argue the apparent acceleration comes from averaging over voids and walls with different clocks. The effect's size is fiercely debated (most cosmologists: negligible; proponents: significant). The averaging problem in GR is real mathematics; its cosmological relevance is the open question. If backreaction matters, the dark-energy budget is mismeasured.",
 "why_it_matters": "If averaging artifacts mimic acceleration, the dark-energy discovery is partly a math error. The budget's biggest line item hangs on the averaging.",
 "sig_lens": "The Signature lens reads backreaction as the averaging's hidden bill: the protocol must compute the bill exactly (relativistic averaging) and check whether it pays for the acceleration.",
 "sig_solution": LABEL + " Assumptions: (1) GR averaging is real math; (2) the effect's size fiercely debated. Reasoning path: compute the bill - relativistic averaging in realistic simulations - and test whether it mimics acceleration. Proposed mechanism: a bill protocol with fully relativistic inhomogeneous cosmological simulations, averaging-scheme comparisons, and backreaction predictions tested against expansion data. Confirm: the computed backreaction matches the apparent acceleration. Kill: it computes negligible and dark energy stands. Does NOT claim: backreaction explains acceleration - it computes the hidden bill.",
 "pointer": "The Signature system's proposed approach computes cosmological backreaction in relativistic simulations; the companion Signature Edition record specifies the bill protocol.",
 "key_points": [
  "Einstein's equations are nonlinear; averaging is nontrivial.",
  "Timescape and related proposals mimic acceleration via averaging.",
  "Most cosmologists judge the effect negligible.",
  "The averaging problem is real mathematics.",
 ],
 "requirements": [
  "Fully relativistic inhomogeneous simulations.",
  "Averaging-scheme comparisons.",
  "Backreaction predictions vs expansion data.",
 ],
 "citations": [
  "Buchert T (2008) Dark energy from structure. General Relativity and Gravitation 40.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 260.0},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "co-arrow",
 "name": "The Cosmological Arrow of Time Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "The universe's entropy rises - but why did it start so low, and what sets the cosmic arrow of time?",
 "background": "The arrow-of-time problem - why the early universe had absurdly low entropy (Penrose's estimate: 1 part in 10^10^123) - is cosmology's deepest puzzle: the dynamical laws are time-symmetric, yet the universe has a definite past-future direction. Explanations compete: inflationary initial conditions (pushing the problem back), the Past Hypothesis (low entropy as a law), Carroll-Chen's eternal bidirectional time, Penrose's conformal cyclic cosmology (aeons). The low-entropy beginning is observed (the smooth CMB); its reason is unknown. Time's direction is the universe's unexplained initial condition.",
 "why_it_matters": "Time's arrow is the most familiar mystery: every irreversible process needs the low-entropy past. Its reason is cosmology's deepest question.",
 "sig_lens": "The Signature lens reads the arrow as the universe's one-way street: the protocol must find who paved it - the initial condition, a law, or a larger cycle.",
 "sig_solution": LABEL + " Assumptions: (1) early entropy absurdly low; laws time-symmetric; (2) explanations compete. Reasoning path: test the explanations' predictions - CCC predicts CMB signatures (Hawking points, debated); eternal models predict measure consequences; the Past Hypothesis predicts nothing new. Proposed mechanism: a one-way protocol hunting the explanations' distinctive predictions (CCC circles, inflationary initial-condition tests), and developing the quantum-gravity account of initial entropy. Confirm: one explanation's predictions verified. Kill: none verified and the arrow stays axiomatic. Does NOT claim: time's origin - it seeks who paved the street.",
 "pointer": "The Signature system's proposed approach tests arrow-of-time explanations on distinctive predictions; the companion Signature Edition record specifies the one-way protocol.",
 "key_points": [
  "Early-universe entropy low to 1 in 10^10^123 (Penrose).",
  "Dynamical laws are time-symmetric.",
  "Inflation, Past Hypothesis, CCC compete.",
  "The smooth CMB is the low-entropy evidence.",
 ],
 "requirements": [
  "Tests of CCC and cyclic predictions.",
  "Inflationary initial-condition tests.",
  "Quantum-gravity accounts of initial entropy.",
 ],
 "citations": [
  "Penrose R (1989) The Emperor's New Mind (Weyl curvature hypothesis). Oxford.",
 ],
 "demo": {"h0": 69.5, "d_mpc": 270.0},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "co-finetuning",
 "name": "The Cosmological Fine Tuning Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "The universe's constants seem tuned for complexity - but is the fine-tuning real, and does it need an explanation?",
 "background": "Cosmological fine-tuning - the constants and initial conditions (Lambda, the density fluctuations' amplitude Q~10^-5, the matter-antimatter asymmetry) sitting in narrow life-permitting ranges - is debated at the meta level: is tuning real or an artifact of varying one constant at a time (Stenger's critique: varying several together opens viable regions)? Explanations - multiverse selection, design, brute fact - are philosophical as much as physical. The fine-tuning that survives scrutiny (Lambda, Q) still demands an account. The question is whether the universe is special or we are.",
 "why_it_matters": "Fine-tuning is the why-is-there-something question in physical form. Its answer is multiverse, design, or brute fact - the deepest fork.",
 "sig_lens": "The Signature lens reads fine-tuning as the universe's narrow doorway: the protocol must measure the doorway's true width (multi-parameter variation) before asking who built it.",
 "sig_solution": LABEL + " Assumptions: (1) single-parameter tuning may be artifactual; (2) explanations are philosophical too. Reasoning path: measure the doorway honestly - vary constants together (multi-parameter habitability studies) and quantify the true tuning. Proposed mechanism: a doorway protocol with multi-parameter habitability mapping, tuning quantification on the full space, and explanation-comparison (multiverse vs brute fact) on the measured tuning. Confirm: the tuning survives multi-parameter scrutiny. Kill: it dissolves and the question was artifactual. Does NOT claim: the tuning's explanation - it measures the doorway first.",
 "pointer": "The Signature system's proposed approach quantifies fine-tuning with multi-parameter habitability studies; the companion Signature Edition record specifies the doorway protocol.",
 "key_points": [
  "Lambda, Q~10^-5, asymmetry sit in narrow ranges.",
  "Single-constant variation may artifactually inflate tuning.",
  "Multiverse, design, brute fact compete.",
  "The question is philosophical as well as physical.",
 ],
 "requirements": [
  "Multi-parameter habitability mapping.",
  "Tuning quantification on full parameter space.",
  "Explanation comparison on measured tuning.",
 ],
 "citations": [
  "Barnes LA (2012) The fine-tuning of the universe for intelligent life. PASA 29.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 280.0},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "co-fate",
 "name": "The Ultimate Fate Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "How does the universe end - heat death, Big Rip, Big Crunch, or something stranger - and what decides?",
 "background": "The ultimate-fate problem - the universe's end state - hinges on dark energy: a true cosmological constant gives heat death (eternal de Sitter expansion, the cosmos emptying); phantom energy (w < -1) gives the Big Rip (tearing bound structures); evolving dark energy could reverse to a Big Crunch; quantum effects might nucleate vacuum decay (a bubble of true vacuum expanding at light speed). The fate is the dark-energy equation of state extrapolated eternally - the least certain extrapolation in science. Every ending is consistent with current data.",
 "why_it_matters": "The universe's ending is the longest-term question there is. Its answer is dark energy's nature written across eternity.",
 "sig_lens": "The Signature lens reads the fate as the ledger's final balance: the protocol must read dark energy's equation of state ever more precisely, for it writes the ending.",
 "sig_solution": LABEL + " Assumptions: (1) fate hinges on dark energy's true nature; (2) extrapolation is the least certain in science. Reasoning path: pin w(z) - the equation-of-state history decides among heat death, Rip, and Crunch; probe vacuum stability for the decay scenario. Proposed mechanism: a final-balance protocol with precision dark-energy evolution measurements, vacuum-metastability tests, and fate scenarios updated as w(z) tightens. Confirm: w(z) converges on one fate. Kill: w stays consistent with all fates. Does NOT claim: the universe's ending - it reads the ledger toward the balance.",
 "pointer": "The Signature system's proposed approach pins dark energy's evolution to discriminate cosmic fates; the companion Signature Edition record specifies the final-balance protocol.",
 "key_points": [
  "Lambda: heat death; phantom (w<-1): Big Rip.",
  "Evolving dark energy could reverse to Crunch.",
  "Vacuum decay is the stranger option.",
  "Every ending fits current data.",
 ],
 "requirements": [
  "Precision w(z) evolution measurements.",
  "Vacuum-metastability probes.",
  "Fate scenarios updated with w(z).",
 ],
 "citations": [
  "Caldwell RR et al. (2003) Phantom energy and cosmic doomsday. PRL 91.",
 ],
 "demo": {"h0": 67.0, "d_mpc": 300.0},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "co-unified",
 "name": "The Unified Cosmology Problem",
 "group": "Cosmic Expansion",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Inflation, dark matter, dark energy, baryogenesis - the universe's ingredients each need new physics, so can they be unified in one framework?",
 "background": "The unified-cosmology problem - one framework for inflation, dark matter, dark energy, and baryogenesis - is the field's grand synthesis: each ingredient currently needs separate new physics (an inflaton, a dark-matter particle, dark energy, a baryogenesis mechanism), and the coincidences between them (why comparable densities? related scales?) hint at common origin. Candidates - axion frameworks (inflation + dark matter), modified gravity (dark energy + dark matter phenomenology), string cosmology - each unify partially. The universe's ingredient list is four mysteries; the unified theory would be one answer.",
 "why_it_matters": "Four mysteries, four separate new physics - or one. The unified framework would be cosmology's standard model.",
 "sig_lens": "The Signature lens reads the ingredients as four locked boxes: the protocol must find the master key - the framework whose one mechanism opens several.",
 "sig_solution": LABEL + " Assumptions: (1) each ingredient needs new physics separately; (2) coincidences hint at common origin. Reasoning path: demand multi-duty - unified proposals must explain several ingredients with one mechanism and predict the coincidences. Proposed mechanism: a master-key protocol developing unified frameworks (axion, modified gravity, string cosmology), requiring each to predict the inter-ingredient relations, and testing on the combined dataset. Confirm: one framework's multi-duty predictions verified. Kill: the ingredients need separate physics and unity is aesthetic. Does NOT claim: the unified theory - it seeks the master key.",
 "pointer": "The Signature system's proposed approach demands multi-duty predictions from unified cosmological frameworks; the companion Signature Edition record specifies the master-key protocol.",
 "key_points": [
  "Inflation, dark matter, dark energy, baryogenesis each need new physics.",
  "Density coincidences hint at common origin.",
  "Axion, modified-gravity, string frameworks unify partially.",
  "Four mysteries or one answer.",
 ],
 "requirements": [
  "Unified frameworks with multi-duty mechanisms.",
  "Predictions for inter-ingredient relations.",
  "Testing on the combined cosmological dataset.",
 ],
 "citations": [
  "Peebles PJE (2020) Cosmology's Century. Princeton.",
 ],
 "demo": {"h0": 70.0, "d_mpc": 320.0},
},
]
