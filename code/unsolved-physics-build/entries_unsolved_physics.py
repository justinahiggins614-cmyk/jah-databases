#!/usr/bin/env python3
"""Entries for The Unsolved Physics Database (unsolved-physics) and its
Signature half (unsolved-physics-signature).

34 famous unsolved problems in physics, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Where the honest
answer is "we don't know," the record says so.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof.")

STD_COMMON = [
    "Quantitative claims cross-checked against the Review of Particle Physics (Particle Data Group) and standard cosmological parameters (Planck 2018).",
    "Problem statements verified against the published literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "matter-antimatter",
 "name": "Matter-Antimatter Asymmetry",
 "group": "Particle Physics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Why does the observable universe contain essentially only matter, with almost no primordial antimatter, when the laws of physics treat matter and antimatter nearly symmetrically?",
 "description": "Every known law of particle physics creates matter and antimatter in nearly equal amounts, yet the observable universe is made almost entirely of matter: about six baryons survive for every ten billion photons, and no primordial antimatter regions have ever been found. Explaining this imbalance requires conditions the known laws barely provide.",
 "background": "Paul Dirac's 1928 equation predicted antimatter, and Carl Anderson discovered the positron in 1932. In 1967 Andrei Sakharov listed three necessary conditions for generating a matter surplus: baryon number violation, C and CP symmetry violation, and a departure from thermal equilibrium. CP violation was found in kaon decays in 1964 (Cronin and Fitch, Nobel 1980) and later in B mesons, but the Standard Model's CP violation is roughly ten orders of magnitude too small to explain the observed baryon-to-photon ratio of about 6.1 x 10^-10, measured independently by Big Bang nucleosynthesis and the cosmic microwave background. Leptogenesis, electroweak baryogenesis, and Affleck-Dine scenarios all remain unconfirmed. As of 2026 the origin of the matter surplus is still open.",
 "why_it_matters": "This asymmetry is the reason anything exists at all: without it, matter and antimatter would have annihilated completely and the universe would hold only light. Solving it would reveal physics beyond the Standard Model and connect the smallest scales of particle physics to the largest scales of cosmology in one story.",
 "sig_pointer": "The Signature system's proposed approach treats the asymmetry as a bookkeeping residue of a scale transition in the early universe, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the matter surplus is a residue left when the universe's matter-antimatter ledger passed through a one-way scale transition. "
  "Assumptions: (1) baryon number is an emergent bookkeeping quantity that can leak during rapid scale transitions; (2) the early universe passed through at least one transition where the effective rules changed faster than the plasma could re-equilibrate; (3) CP-violating phases in the lepton sector are large. "
  "Reasoning path: Sakharov's conditions are treated as ledger rules rather than particle rules; a transition that changes the ledger's own definition leaves a remainder, just as changing currency mid-counting leaves rounding. The proposal therefore expects the asymmetry to track the size of the transition, not the size of particle-level CP violation alone. "
  "Proposed mechanism: heavy right-handed neutrinos decay out of equilibrium (leptogenesis), and the Signature addition is that the decay rates were modulated by the transition's rate of change, amplifying a modest CP phase into the observed eta of 6.1 x 10^-10. "
  "What would confirm it: a measured leptonic CP phase far from 0 or 180 degrees (DUNE, Hyper-Kamiokande) together with evidence of a sharp early-universe transition at the matching energy scale. "
  "What would kill it: a measured CP phase consistent with zero, or proof that the early universe expanded smoothly with no sharp transitions at any relevant scale. "
  "What this does not claim: it does not claim the mechanism is established, does not claim to predict the exact value of eta from first principles, and does not replace the need for direct experimental evidence."),
 "sig_lens": "The Signature lens reads the matter surplus as the universe's ledger failing to balance across a one-way scale transition, and asks what transition could leave exactly this remainder.",
 "how_it_works": "Physicists attack the problem three ways: measuring CP violation ever more precisely (LHCb, Belle II, DUNE, Hyper-Kamiokande), hunting for baryon-number-violating processes like proton decay (Super-Kamiokande, DUNE) and neutrinoless double-beta decay, and computing whether proposed early-universe scenarios can produce the observed eta of 6.1 x 10^-10 without contradicting the cosmic microwave background.",
 "key_points": [
  "The baryon-to-photon ratio is about 6.1 x 10^-10, measured two independent ways.",
  "Sakharov's three conditions (1967) remain the framework every proposal must satisfy.",
  "Known CP violation in the Standard Model is roughly ten orders of magnitude too small.",
  "No primordial antimatter domains have ever been observed.",
  "Leptogenesis, electroweak baryogenesis, and Affleck-Dine are the leading unconfirmed scenarios.",
 ],
 "requirements": [
  "A measurement of leptonic CP violation (the delta_CP phase).",
  "Either an observed baryon-number-violating process or a verified mechanism that works without one.",
  "An early-universe scenario whose predicted eta matches 6.1 x 10^-10.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sakharov AD. Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe. JETP Letters. 1967;5:24-27.",
  "Christenson JH, Cronin JW, Fitch VL, Turlay R. Evidence for the 2-pi decay of the K2(0) meson. Physical Review Letters. 1964;13:138-140.",
  "Planck Collaboration. Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics. 2020;641:A6.",
  "Particle Data Group. Review of Particle Physics. Physical Review D. 2024;110:030001 (baryon asymmetry and CP violation sections).",
 ],
},
# ------------------------------------------------------------------ rank 2
{
 "key": "fate-of-the-universe",
 "name": "The Fate of the Universe",
 "group": "Cosmology",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Will the universe expand forever, and if so, toward what end state \u2014 heat death, a Big Rip, or something stranger?",
 "description": "Since 1998 we have known the universe's expansion is accelerating, driven by something called dark energy. Whether that acceleration continues forever, strengthens, weakens, or reverses decides the universe's ultimate fate \u2014 yet the physics driving it is unknown, so the ending is unwritten.",
 "background": "Alexander Friedmann's 1922 solutions to Einstein's equations showed the universe could expand or contract, and Edwin Hubble's 1929 observations showed it is expanding. For most of the 20th century cosmologists debated whether gravity would eventually halt the expansion (Big Crunch) or not (eternal expansion, Big Freeze). In 1998 two supernova teams (Perlmutter's Supernova Cosmology Project; Riess and Schmidt's High-z team, Nobel Prize 2011) found distant supernovae dimmer than expected: the expansion is accelerating. The standard model (Lambda-CDM) attributes this to a cosmological constant making up about 69 percent of the energy budget, which predicts eternal accelerating expansion toward heat death. Alternatives \u2014 phantom energy leading to a Big Rip, or a slowly changing dark energy \u2014 remain compatible with parts of the data. As of 2026 the fate is still inferred, not known.",
 "why_it_matters": "This is the longest-range forecast science can attempt: the destiny of everything. Pinning it down forces us to understand dark energy, the dominant component of the universe, and it sets the ultimate boundary conditions for the far future of life and complexity.",
 "sig_pointer": "The Signature system's proposed approach treats the fate as a contest between the universe's expansion ledger and its structure ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the universe's fate is decided by a slow competition between two ledgers: the expansion ledger (dark energy) and the structure ledger (matter clumping into bound systems). "
  "Assumptions: (1) dark energy's equation of state can drift over cosmic time rather than being exactly constant; (2) bound structures decouple from the expansion once formed and keep their own local clocks; (3) the drift rate is set by how fast new structure stops forming. "
  "Reasoning path: instead of asking what dark energy 'is,' the proposal asks what it 'does' to the structure ledger over time; a dark energy that weakens as structure formation ends would brake the acceleration gently, while one that strengthens would tear structures apart. The observed near-constancy of dark energy is then read as the system sitting near a balance point, not as a fixed constant of nature. "
  "Proposed mechanism: a quintessence-like field whose potential slope is coupled to the cosmic star-formation rate; as star formation declines, the field rolls and the equation of state drifts. "
  "What would confirm it: next-generation surveys (DESI, Euclid, Rubin) measuring the dark energy equation of state w drifting away from -1 in correlation with the declining cosmic star-formation history. "
  "What would kill it: w measured at exactly -1 with no drift across all redshifts, or star formation shown to have no statistical link to expansion history. "
  "What this does not claim: it does not claim to identify dark energy's fundamental nature, does not claim the drift is detectable with current data, and does not predict which fate wins \u2014 it proposes a mechanism by which the fate could be dynamical rather than fixed."),
 "sig_lens": "The Signature lens reads cosmic fate as a slow contest between the expansion ledger and the structure ledger, and asks what would have to drift for the ending to change.",
 "how_it_works": "Cosmologists measure the expansion history with standard candles (type Ia supernovae), standard rulers (baryon acoustic oscillations), weak gravitational lensing, and galaxy clustering, then fit the dark energy equation of state w and its possible evolution. Each generation of surveys \u2014 DESI, Euclid, the Vera Rubin Observatory \u2014 tightens the allowed drift of w, which is what separates heat death from a Big Rip.",
 "key_points": [
  "The expansion of the universe is accelerating (discovered 1998, Nobel 2011).",
  "About 69 percent of the energy budget is dark energy; about 31 percent is matter.",
  "Lambda-CDM predicts eternal acceleration toward heat death, but w may evolve.",
  "A Big Rip requires phantom energy with w less than -1; a Big Crunch requires dark energy to fade or reverse.",
  "Current data are consistent with a cosmological constant but do not prove it.",
 ],
 "requirements": [
  "A measurement of the dark energy equation of state w(z) across cosmic time.",
  "A physical theory of dark energy, not just a fitted parameter.",
  "Ruling in or out phantom energy (w < -1) and evolving dark energy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Riess AG et al. Observational evidence from supernovae for an accelerating universe and a cosmological constant. Astronomical Journal. 1998;116:1009-1038.",
  "Perlmutter S et al. Measurements of Omega and Lambda from 42 high-redshift supernovae. Astrophysical Journal. 1999;517:565-586.",
  "Planck Collaboration. Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics. 2020;641:A6.",
  "Caldwell RR, Kamionkowski M, Weinberg NN. Phantom energy: dark energy with w < -1 causes a cosmic doomsday. Physical Review Letters. 2003;91:071301.",
 ],
},
# ------------------------------------------------------------------ rank 3
{
 "key": "fermi-question",
 "name": "The Fermi Question: Where Is Everybody?",
 "group": "Astrophysics",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "If intelligent life should be common in a galaxy of hundreds of billions of stars, why have we seen no sign of anyone?",
 "description": "The Milky Way holds hundreds of billions of stars, many billions of them older than the Sun with potentially habitable planets. Even at modest expansion speeds, a technological civilization could cross the galaxy in far less than its age \u2014 yet every search for technosignatures has returned silence. The contradiction between 'they should be everywhere' and 'we see no one' is the Fermi question.",
 "background": "Enrico Fermi reportedly posed the question over lunch in 1950: 'Where is everybody?' Frank Drake formalized it with the Drake equation in 1961, and Project Ozma the same year began the Search for Extraterrestrial Intelligence. Decades of radio searches, optical SETI, and now Breakthrough Listen (the most comprehensive search, surveying millions of stars since 2015) have found no confirmed technosignature. Proposed resolutions multiply: the Rare Earth hypothesis (complex life is genuinely rare), the Great Filter (some step from chemistry to galactic civilization is nearly impossible), the zoo hypothesis (they are hiding), and the simple possibility that interstellar expansion is far harder than assumed. Exoplanet surveys (Kepler, TESS) keep raising the number of habitable-zone planets, which sharpens rather than resolves the paradox. As of 2026 the silence is data, and unexplained.",
 "why_it_matters": "The answer rewrites our place in the universe: a galaxy teeming with minds, a galaxy where intelligence is vanishingly rare, or a galaxy where something systematically prevents civilizations from spreading are three profoundly different realities. It also bears directly on humanity's own long-term survival odds.",
 "sig_pointer": "The Signature system's proposed approach treats the silence as a selection effect of how detectable technologies scale, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the Fermi silence is a detectability bottleneck: civilizations predictably become undetectable to distant observers at a specific technological stage, so the galaxy can be inhabited yet silent. "
  "Assumptions: (1) energy use per civilization saturates rather than growing without bound, because efficiency gains outpace demand; (2) communication shifts to narrow, low-leakage channels as technology matures; (3) expansion across stars is limited by economics and timescales, not physics. "
  "Reasoning path: our searches assume leakage \u2014 radio spillover, waste heat, megastructures \u2014 that a mature civilization has economic reasons to eliminate; the proposal inverts the search logic and asks what a civilization looks like after it has optimized away every signal we know how to look for. The predicted signature is then not loudness but absence: mature systems should look suspiciously quiet and efficient. "
  "Proposed mechanism: a 'quiet transition' in which civilizations move from broadcast technologies to tight-beam and then to physics we have not yet learned to detect (neutrino or gravitational channels at low power), while waste heat drops as computation approaches thermodynamic limits. "
  "What would confirm it: finding nearby planetary systems with anomalously low waste-heat signatures combined with chemical or structural anomalies, or detecting a narrow-beam signal only when the beam happens to sweep Earth. "
  "What would kill it: a confirmed detection of a loud, wasteful, galaxy-spanning civilization \u2014 or proof that interstellar expansion is trivially easy and always pursued, which would make the silence demand a different explanation. "
  "What this does not claim: it does not claim anyone is out there, does not claim the Great Filter is behind us, and does not predict when or whether humanity will be detected."),
 "sig_lens": "The Signature lens reads the Fermi silence as a detectability bottleneck rather than an absence, and asks what a civilization looks like after it optimizes away every signal we search for.",
 "how_it_works": "Astronomers search for technosignatures: narrowband radio signals (Breakthrough Listen), optical laser pulses, infrared waste heat (WISE all-sky survey), and anomalous stellar dimming. Theorists refine the Drake equation's factors with exoplanet statistics and model the possible 'filters.' The work is statistical: each null result tightens the upper bound on how common loud civilizations can be.",
 "key_points": [
  "The Milky Way has hundreds of billions of stars; billions of habitable-zone planets are estimated.",
  "No confirmed technosignature has ever been detected despite decades of searching.",
  "Breakthrough Listen is the most comprehensive search program, running since 2015.",
  "Proposed resolutions include Rare Earth, the Great Filter, the zoo hypothesis, and the quiet-transition idea.",
  "Exoplanet discoveries sharpen the paradox by raising the expected number of habitats.",
 ],
 "requirements": [
  "A confirmed technosignature \u2014 or searches deep enough to rule out loud civilizations galaxy-wide.",
  "Better statistics on how often life starts and how often it becomes technological.",
  "A physical or economic theory of why expansion may stall.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Drake F. Project Ozma. Physics Today. 1961;14(4):40-46.",
  "Hart MH. Explanation for the absence of extraterrestrials on Earth. Quarterly Journal of the Royal Astronomical Society. 1975;16:128-135.",
  "Wright JT et al. The Breakthrough Listen search. Various publications, 2015-present.",
  "Ward PD, Brownlee D. Rare Earth: Why Complex Life Is Uncommon in the Universe. Copernicus/Springer; 2000.",
 ],
},
# ------------------------------------------------------------------ rank 4
{
 "key": "dark-matter",
 "name": "What Is Dark Matter?",
 "group": "Cosmology",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Galaxies, clusters, and the cosmic microwave background all demand about five times more gravitating mass than visible matter provides \u2014 what is it made of?",
 "description": "Stars, gas, and dust account for only about one-sixth of the gravitating mass in the universe. Galaxies rotate too fast, clusters bind too tightly, and the cosmic microwave background's ripples fit only if a cold, invisible, nearly collisionless component \u2014 dark matter \u2014 makes up about 27 percent of the cosmic energy budget. Decades of direct searches have found nothing.",
 "background": "Fritz Zwicky found the Coma cluster's galaxies moving too fast for its visible mass in 1933 and coined 'dunkle Materie.' Vera Rubin and Kent Ford's rotation curves of spiral galaxies in the 1970s made the missing mass undeniable. The cosmic microwave background (Planck 2018: cold dark matter density Omega_c h^2 = 0.120) and the Bullet Cluster's lensing map (Clowe et al. 2006), which shows mass separated from hot gas, cemented the case for a new form of matter rather than a measurement error. Candidates have cycled through the decades: MACHOs (ruled out as the bulk by microlensing surveys), WIMPs (cornered by null results from XENONnT and LUX-ZEPLIN), axions (being hunted by ADMX), sterile neutrinos, and primordial black holes. As of 2026 every direct detection experiment reports only limits.",
 "why_it_matters": "Dark matter is the scaffolding the visible universe was built on: without its gravity, galaxies and clusters could never have formed. Identifying it would complete the inventory of matter, likely reveal new particles or new physics, and rewrite the first chapters of cosmic history.",
 "sig_pointer": "The Signature system's proposed approach treats dark matter as a condensation residue of the universe's gravitational ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dark matter is a condensation of the gravitational ledger itself: where ordinary matter clumps, a weak residue of the clumping process remains as an invisible, nearly collisionless component. "
  "Assumptions: (1) gravity's bookkeeping is not perfectly conservative across the transition from smooth plasma to structured halos; (2) the residue interacts only gravitationally because it is a property of the ledger, not a new particle species; (3) its abundance is therefore fixed by the amount of structure that formed, explaining the observed 5-to-1 ratio without tuning. "
  "Reasoning path: instead of postulating a new particle, the proposal asks what gravity must leave behind when it organizes matter into halos; the residue would naturally trace the dark halos, be cold (slow-moving), and be undetectable in particle detectors because there is no particle to detect. The observed ratio of dark to visible matter then becomes a prediction of structure formation, not a free parameter. "
  "Proposed mechanism: during nonlinear collapse, a small fraction of the gravitational binding bookkeeping condenses into a long-lived, pressureless component that stays bound to the halo. "
  "What would confirm it: a precise, environment-independent 5-to-1 dark-to-visible ratio across all halo masses and epochs, with no particle ever detected despite detectors reaching the neutrino floor \u2014 plus a measured correlation between a halo's assembly history and its dark fraction. "
  "What would kill it: a direct detection of a dark matter particle (WIMP, axion, or other), or dark matter behaving differently from the visible structure's history in any system. "
  "What this does not claim: it does not claim to derive the condensation from known physics, does not claim particle dark matter is ruled out, and does not predict the residue's behavior inside the densest halo cores."),
 "sig_lens": "The Signature lens reads dark matter as the gravitational ledger's own condensation residue \u2014 invisible because it is bookkeeping, not particles \u2014 and asks whether structure formation alone can fix the 5-to-1 ratio.",
 "how_it_works": "Astronomers weigh dark matter with galaxy rotation curves, gravitational lensing (weak and strong), cluster dynamics, and the cosmic microwave background's acoustic peaks. Particle physicists hunt it directly (XENONnT, LUX-ZEPLIN), indirectly (Fermi-LAT, AMS-02 looking for annihilation products), and at colliders (missing-energy signatures at the LHC). Each null result eliminates candidate masses and interaction strengths.",
 "key_points": [
  "Dark matter is about 27 percent of the cosmic energy budget; visible matter is about 5 percent.",
  "Zwicky (1933) and Rubin and Ford (1970s) provided the founding evidence.",
  "The Bullet Cluster shows gravitating mass separated from visible gas.",
  "Direct detection experiments have found only limits, now approaching the neutrino floor.",
  "Leading candidates: WIMPs, axions, sterile neutrinos, primordial black holes.",
 ],
 "requirements": [
  "A direct detection, an unambiguous annihilation signal, or a collider production.",
  "A theory predicting the particle's mass and interactions that survives all null results.",
  "Agreement between galactic, cluster, and cosmological measures of its distribution.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Zwicky F. Die Rotverschiebung von extragalaktischen Nebeln. Helvetica Physica Acta. 1933;6:110-127.",
  "Rubin VC, Ford WK Jr. Rotation of the Andromeda Nebula from a spectroscopic survey of emission regions. Astrophysical Journal. 1970;159:379-403.",
  "Clowe D et al. A direct empirical proof of the existence of dark matter. Astrophysical Journal Letters. 2006;648:L109-L113.",
  "Planck Collaboration. Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics. 2020;641:A6.",
 ],
},
# ------------------------------------------------------------------ rank 5
{
 "key": "dark-energy",
 "name": "What Is Dark Energy?",
 "group": "Cosmology",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Something making up 69 percent of the universe is accelerating cosmic expansion \u2014 is it vacuum energy, a new field, or a sign that gravity itself needs rewriting?",
 "description": "The 1998 supernova discovery showed the universe's expansion is speeding up, not slowing down. The simplest explanation \u2014 a constant vacuum energy, Einstein's cosmological constant \u2014 fits the data with an equation of state w near -1, but its predicted value misses observation by 120 orders of magnitude, and hints from DESI (2024-2025) suggest w may evolve with time. No one knows what dark energy is.",
 "background": "Einstein introduced the cosmological constant in 1917 and later discarded it. The 1998 supernova results (Riess et al.; Perlmutter et al., Nobel 2011) forced it back: something with negative pressure dominates the energy budget. The leading candidates are a true cosmological constant (vacuum energy), a dynamical scalar field (quintessence, phantom energy, k-essence), or modified gravity (f(R), DGP braneworlds). Precision cosmology \u2014 Planck's microwave background, baryon acoustic oscillations, supernova surveys \u2014 pins w close to -1 but cannot yet distinguish a constant from a slowly evolving field. The DESI collaboration's 2024-2025 analyses hint that dark energy may be weakening over time; the collaboration itself stresses these are hints requiring confirmation, not a discovery. As of 2026 dark energy's nature is the biggest single unknown in the cosmic inventory.",
 "why_it_matters": "Dark energy is the majority shareholder of the universe: understanding it means understanding what 69 percent of reality is and where cosmic history is headed. It is also where quantum field theory and gravity clash most violently, so its resolution will likely rewrite fundamental physics.",
 "sig_pointer": "The Signature system's proposed approach treats dark energy as the expansion ledger's balancing entry, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dark energy is the expansion ledger's balancing entry: as matter dilutes with expansion, the ledger posts an offsetting entry to keep the universe's total bookkeeping consistent, and we observe that entry as acceleration. "
  "Assumptions: (1) the universe's total energy bookkeeping includes a term that tracks the expansion rate itself; (2) this term behaves like a cosmological constant only while the matter content dilutes smoothly; (3) episodes of rapid structure change (reionization, the end of star formation) perturb the entry. "
  "Reasoning path: the proposal treats the coincidence problem \u2014 why dark energy dominates exactly now \u2014 as the clue rather than the embarrassment; a balancing entry naturally becomes dominant when matter has diluted enough, i.e., 'now' is when the ledgers cross, which is also when observers like us exist to notice. The DESI hints of evolving w are read as the first glimpse of the entry adjusting. "
  "Proposed mechanism: a geometric backreaction in which the averaged expansion rate feeds back into the effective energy budget, mimicking a near-constant w with slow, structure-correlated drift. "
  "What would confirm it: DESI, Euclid, and Rubin measuring w(z) drifting in lockstep with the cosmic star-formation and structure-growth history, with no new particle or field ever required. "
  "What would kill it: w measured at exactly -1 at all redshifts with percent precision, or a laboratory/astrophysical detection of a quintessence field or a confirmed modification of gravity explaining the acceleration. "
  "What this does not claim: it does not claim to derive the backreaction from full general relativity (the averaging problem is genuinely hard), does not claim the cosmological constant is ruled out, and does not predict the sign or size of the drift."),
 "sig_lens": "The Signature lens reads dark energy as the expansion ledger's balancing entry \u2014 dominant 'now' because now is when the ledgers cross \u2014 and asks whether structure history drives its drift.",
 "how_it_works": "Cosmologists constrain dark energy by measuring the expansion history: type Ia supernova distances, baryon acoustic oscillation standard rulers (DESI), weak lensing and clustering (Euclid, Rubin), and the microwave background's geometric anchor (Planck). Theorists test whether w = -1 exactly or evolves, and whether modified-gravity models can match all probes simultaneously.",
 "key_points": [
  "Dark energy is about 69 percent of the cosmic energy budget.",
  "Its equation of state is measured near w = -1, consistent with a cosmological constant.",
  "DESI 2024-2025 analyses hint w may evolve; the collaboration stresses this needs confirmation.",
  "Candidates: cosmological constant, quintessence/phantom fields, modified gravity.",
  "The coincidence problem asks why dark energy dominates at this epoch.",
 ],
 "requirements": [
  "A precision measurement of w(z) distinguishing constant from evolving dark energy.",
  "A physical theory \u2014 field, vacuum mechanism, or gravity modification \u2014 with testable predictions.",
  "Resolution of the 120-order-of-magnitude vacuum energy discrepancy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Riess AG et al. Observational evidence from supernovae for an accelerating universe and a cosmological constant. Astronomical Journal. 1998;116:1009-1038.",
  "Perlmutter S et al. Measurements of Omega and Lambda from 42 high-redshift supernovae. Astrophysical Journal. 1999;517:565-586.",
  "DESI Collaboration. DESI 2024 results: cosmological constraints from baryon acoustic oscillations. arXiv:2404.03002; DESI DR2 (2025) extensions.",
  "Peebles PJE, Ratra B. The cosmological constant and dark energy. Reviews of Modern Physics. 2003;75:559-606.",
 ],
},
# ------------------------------------------------------------------ rank 6
{
 "key": "hubble-tension",
 "name": "The Hubble Tension",
 "group": "Cosmology",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "The universe's current expansion rate measures about 73 km/s/Mpc from the local distance ladder but about 67 km/s/Mpc from the early-universe microwave background \u2014 a disagreement near five sigma that will not go away.",
 "description": "Two of cosmology's most careful measurement programs disagree about the Hubble constant. The local ladder (SH0ES: Cepheids plus supernovae) gives 73.04 +/- 1.04 km/s/Mpc; the Planck microwave-background inference under standard cosmology gives 67.4 +/- 0.5 km/s/Mpc. The gap has survived a decade of scrutiny, new instruments, and independent cross-checks \u2014 it looks like new physics or an unrecognized error, and no one knows which.",
 "background": "Edwin Hubble's 1929 expansion discovery began a century of H0 measurements that slowly converged \u2014 until precision broke the consensus. The SH0ES program (Riess et al.), using Hubble Space Telescope Cepheid calibrations of type Ia supernovae, has reported H0 near 73 since 2016 with shrinking errors. Planck's 2018 microwave-background analysis infers 67.4 under Lambda-CDM. Independent methods split: gravitational-lens time delays (H0LiCOW/TDCOSMO) and megamasers lean high; the tip of the red giant branch (TRGB, Freedman et al.) lands in the middle near 69-70; gravitational-wave standard sirens are still too few to decide. Proposed new physics includes early dark energy, extra relativistic species, and interacting neutrinos \u2014 none confirmed. As of 2026 the tension persists near 5 sigma.",
 "why_it_matters": "The Hubble constant anchors the age, size, and expansion history of the universe; a real tension means the standard cosmological model is missing an ingredient. Resolving it \u2014 new physics or subtle systematics \u2014 either way upgrades the foundations of cosmology.",
 "sig_pointer": "The Signature system's proposed approach treats the tension as two ledgers measuring different epochs of the same drift, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the Hubble tension is not an error but a real drift: the expansion ledger's calibration changed slightly between the microwave-background epoch and today, so early and late measurements honestly disagree. "
  "Assumptions: (1) the sound-horizon ruler used by Planck depends on pre-recombination physics that included a brief extra energy component; (2) that component decayed away before structure formation, leaving late-universe physics standard; (3) the local ladder measurements are essentially correct. "
  "Reasoning path: the proposal follows the 'early dark energy' family of ideas but frames it as ledger recalibration \u2014 a short-lived entry in the expansion ledger near recombination that shrinks the sound horizon, making the early-universe inference of H0 come out low while the true late value is the local 73. The test is then specific: the recalibration must fade fast enough to leave the microwave background's peak structure intact. "
  "Proposed mechanism: a scalar field that briefly contributes a few percent of the energy density around matter-radiation equality and then redshifts away faster than radiation. "
  "What would confirm it: next-generation microwave-background experiments (Simons Observatory, CMB-S4) detecting the specific peak-shift pattern of a brief early component, plus standard-siren H0 measurements converging on the local value. "
  "What would kill it: CMB-S4 ruling out any early extra component at the needed level, or the local ladder found to harbor a shared systematic (e.g., Cepheid crowding bias) that brings it down to 67. "
  "What this does not claim: it does not claim early dark energy is established, does not specify the field's particle identity, and does not rule out that the whole tension is systematics."),
 "sig_lens": "The Signature lens reads the Hubble tension as two honest ledgers from two epochs, and asks what brief recalibration near recombination would make both right.",
 "how_it_works": "The local ladder builds distance step by step: parallax to Cepheids, Cepheids to supernovae, supernovae to the Hubble flow. The early-universe route measures the microwave background's acoustic peaks, infers the sound horizon, and extrapolates forward with Lambda-CDM. New independent routes \u2014 standard sirens from gravitational waves, lensing time delays, TRGB \u2014 arbitrate. Each method's systematics are attacked separately.",
 "key_points": [
  "SH0ES local ladder: 73.04 +/- 1.04 km/s/Mpc; Planck early-universe inference: 67.4 +/- 0.5 km/s/Mpc.",
  "The disagreement is near five sigma and a decade old.",
  "TRGB measurements land between the two; standard sirens are not yet decisive.",
  "Proposed physics: early dark energy, extra relativistic species, interacting dark sectors.",
  "Proposed systematics: Cepheid crowding, supernova calibration, Planck modeling.",
 ],
 "requirements": [
  "A third, fully independent H0 route at percent precision (standard sirens, lensing).",
  "Either a confirmed systematic in one ladder or a new-physics model fitting all data.",
  "CMB-S4 / Simons Observatory verdict on early-universe modifications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Riess AG et al. A comprehensive measurement of the local value of the Hubble constant with 1 km/s/Mpc uncertainty from the Hubble Space Telescope and the SH0ES team. Astrophysical Journal Letters. 2022;934:L7.",
  "Planck Collaboration. Planck 2018 results. VI. Cosmological parameters. Astronomy & Astrophysics. 2020;641:A6.",
  "Freedman WL et al. The Carnegie-Chicago Hubble Program. VIII. The distance to NGC 1365 via the tip of the red giant branch. Astrophysical Journal. 2019;882:34.",
  "Verde L, Treu T, Riess AG. Tensions between the early and late Universe. Nature Astronomy. 2019;3:891-895.",
 ],
},
# ------------------------------------------------------------------ rank 7
{
 "key": "corona-heating",
 "name": "The Solar Corona Heating Problem",
 "group": "Astrophysics",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "The Sun's outer atmosphere is over a hundred times hotter than its visible surface \u2014 about a million degrees versus 5,800 K \u2014 and eight decades of work have not settled why.",
 "description": "Heat should flow from hot to cold, yet the solar corona blazes at 1-3 million kelvin while the photosphere below sits at 5,800 K. Something pumps enormous energy into the corona \u2014 magnetic reconnection, waves, nanoflares, or a mix \u2014 but which mechanism dominates, and how the energy gets there, remains unsolved after 80 years.",
 "background": "Bengt Edl\u00e9n identified the mysterious coronal spectral lines as highly ionized iron in the 1940s, proving million-degree temperatures. Eugene Parker proposed nanoflares \u2014 countless tiny magnetic explosions \u2014 in 1988, while Alfv\u00e9n-wave heating models argue waves traveling up from the surface dump their energy in the corona. Modern observatories (SDO, Hinode, IRIS) and the Parker Solar Probe, flying closer to the Sun than any craft before, have mapped magnetic braiding and switchbacks in exquisite detail, yet the energy budget still does not close cleanly: proposed mechanisms each explain part of the heating in part of the corona. As of 2026 the coronal heating problem is the oldest unsolved problem in solar physics.",
 "why_it_matters": "The corona drives space weather \u2014 solar wind, flares, and coronal mass ejections that can black out power grids and satellites. Understanding its heating means understanding the star we live next to, and stellar coronae are universal, so the answer applies to stars across the galaxy.",
 "sig_pointer": "The Signature system's proposed approach treats coronal heating as magnetic ledger braiding discharging at a critical tangle density, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that coronal heating is a critical-tangle discharge: the Sun's magnetic ledger braids itself through surface motions until the tangle density crosses a threshold, then releases the stored energy in a cascade of nano-events. "
  "Assumptions: (1) photospheric motions braid coronal field lines at a steady rate; (2) the braided field stores energy until a critical tangle density, then reconnects in avalanches; (3) the avalanche size distribution follows a power law set by the threshold, not by the driver details. "
  "Reasoning path: the proposal borrows the logic of self-organized criticality \u2014 like a sandpile that avalanches at a critical slope regardless of how sand is added \u2014 and applies it to the magnetic ledger; the million-degree temperature is then the natural thermostat of a system hovering at its discharge threshold, which explains why the corona's temperature is so uniform despite chaotic drivers. "
  "Proposed mechanism: braiding-driven nanoflare avalanches with a universal power-law index, testable against the observed flare energy distribution. "
  "What would confirm it: Parker Solar Probe and DKIST measuring a universal flare-energy power-law index matching the critical-tangle prediction across quiet Sun, coronal holes, and active regions. "
  "What would kill it: wave-heating signatures (specific Alfv\u00e9n-wave damping profiles) accounting for the full energy budget with no room left for reconnection avalanches, or flare statistics varying strongly with driver details. "
  "What this does not claim: it does not claim waves contribute nothing, does not derive the critical index from first principles, and does not claim the problem solved \u2014 it proposes the thermostat logic behind the temperature."),
 "sig_lens": "The Signature lens reads the corona as a magnetic ledger hovering at a critical tangle threshold, and asks what thermostat keeps it at a million degrees.",
 "how_it_works": "Solar physicists combine remote sensing (SDO/AIA imaging, Hinode/XRT, IRIS spectroscopy) with in-situ measurements from the Parker Solar Probe and Solar Orbiter, plus 3D magnetohydrodynamic simulations. They test heating models by comparing predicted energy fluxes, temperature structures, and flare statistics against observations across different coronal regions.",
 "key_points": [
  "Corona: 1-3 million K; photosphere: about 5,800 K \u2014 a factor over 170.",
  "Identified as hot by Edl\u00e9n in the 1940s via highly ionized iron lines.",
  "Leading candidates: nanoflares (Parker 1988), Alfv\u00e9n-wave heating, magnetic reconnection.",
  "Active regions require energy fluxes around 10^7 erg/cm^2/s.",
  "Parker Solar Probe provides the closest-ever in-situ measurements.",
 ],
 "requirements": [
  "Closing the energy budget: matching observed heating to a mechanism's predicted flux.",
  "A universal explanation working in quiet Sun, coronal holes, and active regions.",
  "Direct evidence distinguishing wave dissipation from reconnection avalanches.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Edl\u00e9n B. Die Deutung der Emissionslinien im Spektrum der Sonnenkorona. Zeitschrift f\u00fcr Astrophysik. 1943;22:30-64.",
  "Parker EN. Nanoflares and the solar X-ray corona. Astrophysical Journal. 1988;330:474-479.",
  "Klimchuk JA. On solving the coronal heating problem. Solar Physics. 2006;234:41-77.",
  "Alfv\u00e9n H. Existence of electromagnetic-hydrodynamic waves. Nature. 1942;150:405-406.",
 ],
},
# ------------------------------------------------------------------ rank 8
{
 "key": "sonoluminescence",
 "name": "Sonoluminescence",
 "group": "Condensed Matter",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "A collapsing bubble in water, driven by nothing but sound, flashes with light hotter than the Sun's surface \u2014 and no one fully agrees how.",
 "description": "In single-bubble sonoluminescence, an air bubble trapped in water by an acoustic standing wave collapses once per cycle and emits a flash of light lasting picoseconds, with an effective temperature of tens of thousands of kelvin. The energy concentration \u2014 from sound waves to optical photons in a micron-scale collapse \u2014 is extraordinary, and the emission mechanism is still debated.",
 "background": "The effect was first reported by Frenzel and Schultes in 1934 with photographic plates. Single-bubble sonoluminescence was achieved by Gaitan in 1990, turning a curiosity into a precision laboratory: one stable bubble, flashing like clockwork, emitting roughly a million photons per flash. Proposed mechanisms include thermal bremsstrahlung from a hot plasma core, collision-induced emission, and Julian Schwinger's provocative suggestion of dynamical Casimir (vacuum) radiation from the rapidly moving bubble wall. Measurements of the flash duration (tens of picoseconds), spectrum (featureless, blue-weighted), and timing are exquisite \u2014 yet no single mechanism reproduces all of them. As of 2026 the light's origin remains contested.",
 "why_it_matters": "Sonoluminescence is the most extreme energy focusing known in a tabletop experiment: twelve orders of magnitude in energy density. Understanding it could illuminate plasma physics, cavitation damage (propellers, pumps, medical ultrasound), and even speculative energy schemes \u2014 and the vacuum-radiation proposals touch the quantum vacuum itself.",
 "sig_pointer": "The Signature system's proposed approach treats the flash as the collapse ledger discharging through the fastest available channel, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the sonoluminescence flash is a ledger discharge: the collapsing bubble concentrates energy faster than any thermal channel can radiate it, so the system dumps the surplus through the fastest available quantum channel \u2014 photon emission from the accelerating wall itself. "
  "Assumptions: (1) the bubble wall accelerates so violently that the electromagnetic vacuum cannot adiabatically follow; (2) the dominant emission scales with wall acceleration, not with the core plasma temperature; (3) the collapse remains spherically symmetric enough for coherent wall emission. "
  "Reasoning path: the proposal notes that thermal models struggle with the flash's brevity and featureless spectrum, while acceleration-driven (Unruh-like, dynamical Casimir) emission naturally gives short, broadband, blue-weighted flashes; the Signature addition is a scaling law \u2014 flash energy proportional to the peak wall acceleration cubed \u2014 testable by varying the drive. "
  "Proposed mechanism: dynamical Casimir / acceleration radiation from the bubble wall dominating over plasma bremsstrahlung in the final picoseconds of collapse. "
  "What would confirm it: measured flash energy tracking peak wall acceleration (via Mie scattering radius-time curves) across different gases and drive levels, with spectra staying featureless even as plasma models predict lines. "
  "What would kill it: detection of atomic emission lines in the flash spectrum (proving a hot dense plasma core dominates), or flash energy tracking core temperature rather than wall acceleration. "
  "What this does not claim: it does not claim the dynamical Casimir effect is proven here, does not rule out hybrid mechanisms, and does not claim a path to net energy gain."),
 "sig_lens": "The Signature lens reads the flash as a collapse ledger discharging through its fastest channel, and asks whether wall acceleration \u2014 not plasma temperature \u2014 sets the light.",
 "how_it_works": "Experimentalists trap a single bubble acoustically and measure the radius-versus-time curve with Mie scattering, the flash duration with time-correlated photon counting, and the spectrum with sensitive spectrometers. Theorists model the collapse with Rayleigh-Plesset dynamics coupled to plasma, radiative, and quantum-vacuum emission models, and compare predicted flash energies, durations, and spectra.",
 "key_points": [
  "First reported 1934 (Frenzel and Schultes); single-bubble version 1990 (Gaitan).",
  "Flash duration: tens of picoseconds; effective temperature: tens of thousands of kelvin.",
  "About a million photons per flash, clocklike with the acoustic drive.",
  "Spectrum is broad and featureless, weighted toward the blue/UV.",
  "Candidate mechanisms: plasma bremsstrahlung, collision-induced emission, dynamical Casimir radiation.",
 ],
 "requirements": [
  "A mechanism reproducing flash energy, duration, spectrum, and timing simultaneously.",
  "Decisive evidence for or against plasma emission lines in the spectrum.",
  "A scaling law verified across gases, drive pressures, and bubble sizes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Frenzel H, Schultes H. Luminescenz im ultraschallbeschickten Wasser. Zeitschrift f\u00fcr Physikalische Chemie. 1934;27B:421-424.",
  "Gaitan DF et al. Sonoluminescence and bubble dynamics for a single, stable, cavitation bubble. Journal of the Acoustical Society of America. 1992;91:3166-3183.",
  "Barber BP, Putterman SJ. Observation of synchronous picosecond sonoluminescence. Nature. 1991;352:318-320.",
  "Brenner MP, Hilgenfeldt S, Lohse D. Single-bubble sonoluminescence. Reviews of Modern Physics. 2002;74:425-484.",
 ],
},
# ------------------------------------------------------------------ rank 9
{
 "key": "arrow-of-time",
 "name": "The Arrow of Time",
 "group": "Foundations of Physics",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "The fundamental laws of physics work the same forward and backward in time \u2014 so why does time itself have a preferred direction?",
 "description": "Newton's laws, Maxwell's equations, and even Schr\u00f6dinger's equation are time-symmetric: run the film backward and the equations still hold. Yet eggs break and never unbreak, we remember the past and not the future, and entropy climbs. The microscopic laws do not pick a direction \u2014 so where does the arrow come from?",
 "background": "Ludwig Boltzmann's H-theorem (1870s) derived irreversible entropy increase from reversible mechanics, but Josef Loschmidt's 1876 reversibility objection showed the derivation smuggled in a time-asymmetric assumption about molecular chaos. The modern consensus traces the arrow to cosmology: the universe began in an extraordinarily low-entropy state (the 'past hypothesis'), and everything since is the working-out of that initial condition. Roger Penrose sharpened the puzzle with the Weyl curvature hypothesis, noting the Big Bang's gravitational entropy was absurdly low. CP violation in particle physics provides a genuine microscopic arrow, but far too small to explain thermodynamics. Quantum measurement and decoherence add further candidate arrows. As of 2026 there is agreement on the shape of the answer \u2014 a low-entropy beginning plus symmetric laws \u2014 but no agreement on why the beginning was that way.",
 "why_it_matters": "The arrow of time underlies causality, memory, aging, and the very possibility of records and history. Explaining it means explaining why the universe started in such a special state \u2014 which is arguably the deepest 'why' in cosmology.",
 "sig_pointer": "The Signature system's proposed approach treats the arrow as the universe's ledger being written once and read many times, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the arrow of time is a write-once property of the universe's ledger: the Big Bang wrote an initial entry of extremely low entropy, and the laws of physics are read-rules that can only increase the ledger's disorder \u2014 the asymmetry lives in the initial entry, not in the rules. "
  "Assumptions: (1) the fundamental dynamical laws are exactly time-symmetric; (2) the initial state was a special low-entropy boundary condition; (3) no dynamical mechanism within the universe can 'reset' the ledger to a lower-entropy state. "
  "Reasoning path: the proposal accepts the past hypothesis but asks what enforces it \u2014 and answers that a ledger written once cannot be unwritten by its own read-rules, making the arrow a logical consequence of a single-write cosmology rather than a dynamical mystery; the observed uniformity of the arrow (everywhere, everywhen) then follows from the single shared initial entry. "
  "Proposed mechanism: none dynamical \u2014 the proposal is structural: time's arrow is the direction of increasing ledger entries, and the low-entropy beginning is taken as the universe's defining boundary condition, to be explained only by whatever theory explains the beginning itself (quantum cosmology). "
  "What would confirm it: it is largely confirmed in shape already \u2014 the proposal predicts no local violations of the thermodynamic arrow will ever be found, and that all candidate 'new arrows' (CP violation, quantum measurement) will prove too small or derivative. "
  "What would kill it: a verified macroscopic entropy decrease in an isolated system, or a cosmological model with no special initial condition that still reproduces the arrow. "
  "What this does not claim: it does not explain why the initial entry was low-entropy \u2014 it relocates the mystery to the beginning, honestly, rather than dissolving it \u2014 and does not claim the past hypothesis is proven."),
 "sig_lens": "The Signature lens reads time's arrow as a write-once ledger property \u2014 the asymmetry in the initial entry, not the rules \u2014 and asks what enforces the single writing.",
 "how_it_works": "Physicists study the arrow through statistical mechanics (deriving irreversibility from symmetric laws plus boundary conditions), cosmology (testing the past hypothesis against inflationary and bouncing models), quantum foundations (whether measurement or decoherence adds an arrow), and particle physics (measuring CP violation's contribution). The work is largely theoretical, anchored by the observed entropy history of the universe.",
 "key_points": [
  "Microscopic laws are time-symmetric; macroscopic behavior is not.",
  "Boltzmann's H-theorem plus Loschmidt's 1876 objection frame the core puzzle.",
  "The past hypothesis: the universe began in an extremely low-entropy state.",
  "Penrose's Weyl curvature hypothesis addresses gravitational entropy.",
  "CP violation gives a real but tiny microscopic arrow.",
 ],
 "requirements": [
  "An explanation of the low-entropy initial condition (quantum cosmology, inflationary measure, or other).",
  "Proof that no dynamical arrow beyond boundary conditions is needed \u2014 or discovery of one.",
  "Reconciliation of the thermodynamic, cosmological, quantum, and psychological arrows.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boltzmann L. Weitere Studien \u00fcber das W\u00e4rmegleichgewicht unter Gasmolek\u00fclen. Sitzungsberichte der Akademie der Wissenschaften, Wien. 1872;66:275-370.",
  "Penrose R. The Road to Reality. Jonathan Cape; 2004 (Weyl curvature hypothesis, ch. 27-28).",
  "Albert DZ. Time and Chance. Harvard University Press; 2000.",
  "Price H. Time's Arrow and Archimedes' Point. Oxford University Press; 1996.",
 ],
},
]

ENTRIES += [
# ----------------------------------------------------------------- rank 10
{
 "key": "high-tc-superconductivity",
 "name": "High-Temperature Superconductivity Mechanism",
 "group": "Condensed Matter",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Cuprate superconductors carry current with zero resistance at temperatures far above any conventional theory's limit \u2014 what is the pairing glue?",
 "description": "In conventional superconductors, lattice vibrations (phonons) pair electrons, and theory caps the critical temperature around 30-40 K. Cuprates superconduct above 130 K, iron pnictides above 50 K, and pressurized hydrides above 200 K \u2014 yet after nearly four decades no consensus exists on what binds the electron pairs in the cuprates, the most studied family.",
 "background": "Georg Bednorz and Alex M\u00fcller's 1986 discovery of superconductivity at 35 K in a copper oxide (Nobel Prize 1987) shattered the phonon ceiling. Ching-Wu Chu's group pushed YBCO past 90 K in 1987 \u2014 above liquid nitrogen's boiling point \u2014 and mercury cuprates later reached 138 K at ambient pressure. The phase diagram is baroque: antiferromagnetism, the mysterious pseudogap, charge stripes, and a strange metal surround the superconducting dome. Proposed pairing glues include antiferromagnetic spin fluctuations, Anderson's resonating-valence-bond state, charge stripes, and loop currents; each explains some experiments and fails others. Iron pnictides (Hosono, 2008) and high-pressure hydrides added new families without settling the cuprate question. As of 2026 the mechanism remains the most famous open problem in condensed matter physics.",
 "why_it_matters": "Room-temperature superconductivity would revolutionize power grids, maglev transport, medical imaging, and computing \u2014 lossless everything. The mechanism is the map to that prize: whoever understands the pairing glue can search for it deliberately instead of by luck.",
 "sig_pointer": "The Signature system's proposed approach treats the pairing glue as a ledger resonance between charge order and spin order, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cuprate pairing is a resonance phenomenon: the charge ledger and the spin ledger of the copper-oxide plane oscillate against each other, and superconductivity condenses at the resonance where the two ledgers exchange energy most efficiently. "
  "Assumptions: (1) the pseudogap is a competing ledger order, not a precursor pairing state; (2) the pairing interaction peaks where antiferromagnetic spin fluctuations and charge-stripe fluctuations have matched energy scales; (3) the d-wave symmetry follows from the resonance geometry of the square lattice. "
  "Reasoning path: the proposal notes that Tc peaks exactly where the competing orders are most evenly balanced \u2014 the 'sweet spot' of the phase diagram \u2014 and reads this as resonance, not coincidence; the superconducting dome is then the resonance curve, which explains its shape and why Tc is so sensitive to doping and pressure. "
  "Proposed mechanism: spin-fluctuation-mediated pairing amplified by charge-order resonance, with the pseudogap as the off-resonance shadow of the same interaction. "
  "What would confirm it: a measured quantitative match between the doping dependence of the spin/charge fluctuation energy scales and the superconducting dome's shape across multiple cuprate families, plus the pseudogap's energy scale tracking the detuning from resonance. "
  "What would kill it: a cuprate family whose Tc peak does not coincide with balanced competing orders, or direct proof that the pseudogap is preformed pairing (which would make it the precursor, not the competitor). "
  "What this does not claim: it does not claim a microscopic derivation of the resonance from the Hubbard model (still unsolved numerically at the relevant scales), does not claim phonons play no role, and does not predict the maximum achievable Tc."),
 "sig_lens": "The Signature lens reads the superconducting dome as a resonance curve between the charge ledger and the spin ledger, and asks what tunes the copper-oxide plane to its peak.",
 "how_it_works": "Experimentalists map the phase diagram with ARPES (electronic structure), neutron scattering (spin fluctuations), STM (local orders), and transport under pressure and magnetic fields. Theorists attack the Hubbard and t-J models numerically (DMRG, quantum Monte Carlo, cluster DMFT) and test pairing-glue candidates against the measured gap symmetry, isotope effects, and fluctuation spectra.",
 "key_points": [
  "Bednorz and M\u00fcller 1986 (35 K, Nobel 1987); YBCO 93 K (1987); Hg-cuprates 138 K.",
  "Conventional phonon theory caps Tc near 30-40 K; cuprates far exceed it.",
  "Pairing symmetry is d-wave; the glue is disputed: spin fluctuations, RVB, stripes, loop currents.",
  "The pseudogap phase's nature \u2014 precursor or competitor \u2014 is central to the debate.",
  "Iron pnictides (2008) and pressurized hydrides are newer families with their own puzzles.",
 ],
 "requirements": [
  "Identifying the pairing glue experimentally (which fluctuation spectrum tracks Tc).",
  "A controlled theoretical solution of the doped Hubbard/t-J model matching the phase diagram.",
  "Settling the pseudogap's nature: preformed pairs or competing order.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bednorz JG, M\u00fcller KA. Possible high Tc superconductivity in the Ba-La-Cu-O system. Zeitschrift f\u00fcr Physik B. 1986;64:189-193.",
  "Wu MK et al. Superconductivity at 93 K in a new mixed-phase Y-Ba-Cu-O compound system at ambient pressure. Physical Review Letters. 1987;58:908-910.",
  "Anderson PW. The resonating valence bond state in La2CuO4 and superconductivity. Science. 1987;235:1196-1198.",
  "Keimer B et al. From quantum matter to high-temperature superconductivity in copper oxides. Nature. 2015;518:179-186.",
 ],
},
# ----------------------------------------------------------------- rank 11
{
 "key": "glass-transition",
 "name": "The Glass Transition",
 "group": "Condensed Matter",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "When a liquid cools into glass, its viscosity rises fourteen orders of magnitude with barely any structural change \u2014 is this a true phase transition, and what actually freezes?",
 "description": "Cool most liquids fast enough and they skip crystallization, becoming glass: a solid with a liquid's disordered structure. Near the glass temperature Tg the viscosity hits 10^12 pascal-seconds and molecular motion arrests \u2014 yet diffraction shows almost no structural change, and after a century there is still no consensus theory of what, precisely, is transitioning.",
 "background": "Glass is humanity's oldest engineered material, but the glass transition became a scientific puzzle with Kauzmann's 1948 entropy paradox: extrapolating a supercooled liquid's entropy suggests it would fall below the crystal's \u2014 impossible \u2014 hinting at a hidden ideal transition. Competing theories multiplied: free-volume models, mode-coupling theory (which predicts a dynamical arrest that experiments evade), the random first-order transition (RFOT) mosaic picture, dynamical facilitation, and geometric frustration. Each captures part of the phenomenology \u2014 the super-Arrhenius viscosity rise, dynamical heterogeneity, aging \u2014 and none commands consensus. Ultrastable glasses (vapor-deposited, Ediger 2007) opened a window on deep supercooling and sharpened the debate. As of 2026 the field still cannot agree whether a thermodynamic glass transition exists at all.",
 "why_it_matters": "Glasses are everywhere: windows, fiber optics, phone screens, pharmaceuticals, metallic glasses, even the plastics in your walls. A real theory of the glass transition would let us design amorphous materials \u2014 stability, strength, dissolution rates \u2014 from principles instead of recipes, and it would settle one of statistical physics' deepest questions about what a phase transition can be.",
 "sig_pointer": "The Signature system's proposed approach treats the glass transition as the motion ledger fragmenting into mutually inaccessible regions, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the glass transition is a fragmentation of the motion ledger: as the liquid cools, the set of configurations reachable by molecular motion splits into mutually inaccessible regions, and the laboratory glass transition is the point where the experimental timescale can no longer cross between regions. "
  "Assumptions: (1) configuration space develops barriers that grow as temperature falls; (2) the barriers' growth is cooperative \u2014 each frozen region raises its neighbors' barriers; (3) no sharp thermodynamic singularity is required; the arrest is a timescale crossing. "
  "Reasoning path: the proposal takes the experimental fact \u2014 fourteen orders of magnitude in viscosity with no structural signature \u2014 at face value and concludes the transition is in the accessibility of configurations, not in the configurations themselves; the Kauzmann paradox is then resolved because the 'ideal' transition is unreachable in finite time, making it a horizon rather than a phase boundary. "
  "Proposed mechanism: cooperatively growing activation barriers (in the spirit of RFOT and facilitation pictures) with the laboratory Tg set by the condition that the structural relaxation time exceeds the observation time. "
  "What would confirm it: ultrastable-glass and swap-Monte-Carlo experiments showing the relaxation time diverging only at an unreachable temperature, with barrier growth quantitatively matching the cooperative prediction across fragile and strong glass-formers. "
  "What would kill it: discovery of a genuine thermodynamic signature \u2014 a diverging static correlation length or latent heat \u2014 at a reachable temperature, proving a true phase transition. "
  "What this does not claim: it does not claim the ideal glass transition is proven unreachable, does not pick between RFOT and facilitation microscopics, and does not predict Tg from molecular structure alone."),
 "sig_lens": "The Signature lens reads the glass transition as the motion ledger fragmenting into unreachable regions, and asks whether the arrest is a horizon rather than a boundary.",
 "how_it_works": "Researchers measure viscosity, dielectric relaxation, and heat capacity across the supercooled regime; image dynamical heterogeneity with microscopy and NMR; create ultrastable glasses by vapor deposition to probe deep supercooling; and simulate with molecular dynamics plus swap algorithms that equilibrate far below the laboratory Tg. Theories are tested against the fragility spectrum and the growth of cooperative length scales.",
 "key_points": [
  "Viscosity rises ~10^14-fold near Tg with almost no change in static structure.",
  "Kauzmann's 1948 entropy paradox suggests a hidden ideal transition.",
  "Competing theories: RFOT mosaic, mode-coupling, dynamical facilitation, frustration.",
  "Ultrastable vapor-deposited glasses (2007) probe deeper supercooling than bulk cooling allows.",
  "No consensus on whether a true thermodynamic transition underlies the kinetic arrest.",
 ],
 "requirements": [
  "Deciding whether a thermodynamic glass transition exists at finite temperature.",
  "A theory predicting fragility and Tg from molecular properties.",
  "Measuring a diverging static length scale \u2014 or proving none exists.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kauzmann W. The nature of the glassy state and the behavior of liquids at low temperatures. Chemical Reviews. 1948;43:219-256.",
  "Ediger MD, Harrowell P. Perspective: Supercooled liquids and glasses. Journal of Chemical Physics. 2012;137:080901.",
  "Berthier L, Biroli G. Theoretical perspective on the glass transition and amorphous materials. Reviews of Modern Physics. 2011;83:587-645.",
  "Angell CA. Formation of glasses from liquids and biopolymers. Science. 1995;267:1924-1935.",
 ],
},
# ----------------------------------------------------------------- rank 12
{
 "key": "uhe-cosmic-rays",
 "name": "Ultra-High-Energy Cosmic Rays",
 "group": "Astrophysics",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Particles arrive from space carrying the energy of a thrown baseball in a single proton \u2014 10^20 electronvolts \u2014 and no known accelerator in the nearby universe can make them.",
 "description": "Cosmic rays span twelve orders of magnitude in energy, but the rarest \u2014 ultra-high-energy cosmic rays above 10^18 eV \u2014 defy explanation. Above about 6 x 10^19 eV, protons should lose energy to the cosmic microwave background (the GZK cutoff), limiting their sources to within ~100 megaparsecs; yet events above the cutoff arrive, and no matching nearby accelerator has been identified.",
 "background": "Victor Hess discovered cosmic rays in 1912 (Nobel 1936). In 1966 Greisen, and Zatsepin and Kuzmin, independently predicted that the microwave background \u2014 discovered just a year earlier \u2014 would brake the most energetic protons via photopion production, creating a cutoff near 6 x 10^19 eV. Modern observatories, the Pierre Auger Observatory (Argentina) and the Telescope Array (Utah), have mapped the spectrum's suppression and the arrival directions: there is a cutoff-like steepening, but also events beyond it, a composition trending heavy at the highest energies, and only weak correlations with candidate sources like active galactic nuclei. Proposed accelerators \u2014 AGN jets, gamma-ray bursts, newborn magnetars, cluster shocks \u2014 each strain to reach 10^20 eV within the GZK horizon. As of 2026 the sources remain unidentified.",
 "why_it_matters": "These are the most energetic particles in nature, millions of times beyond the LHC. Finding their accelerators means finding the universe's most extreme engines \u2014 and if no engine suffices, the particles may be messengers of new physics, such as decaying superheavy dark matter.",
 "sig_pointer": "The Signature system's proposed approach treats UHECRs as the acceleration ledger's rare overflow events, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ultra-high-energy cosmic rays are overflow events of the acceleration ledger: most cosmic accelerators have a strict energy budget, but rare multi-stage 'relay' acceleration \u2014 a particle handed from one shock to the next \u2014 occasionally compounds gains beyond any single engine's limit. "
  "Assumptions: (1) no single shock or jet reaches 10^20 eV alone; (2) particles can be re-accelerated by successive structures (jet, then lobe, then cluster shock); (3) only particles threading a specific sequence of structures achieve the compounding. "
  "Reasoning path: the proposal explains both the rarity and the weak source correlation \u2014 the sources are ordinary powerful objects, but the 10^20 eV events require winning a sequence of acceleration lotteries, so arrival directions point only statistically at source populations, never cleanly at individuals; the heavy composition trend follows because heavy nuclei survive the relay better than protons. "
  "Proposed mechanism: sequential diffusive shock re-acceleration across nested astrophysical structures, with energy multiplying at each stage that the particle's rigidity allows it to enter. "
  "What would confirm it: AugerPrime composition and anisotropy data showing the highest-energy events statistically associated with regions containing multiple nested accelerators (e.g., AGN inside merging clusters), with a rigidity-dependent cutoff matching relay predictions. "
  "What would kill it: a clean identification of single sources each demonstrably capable of 10^20 eV alone, or arrival directions proving an isotropic, non-astrophysical origin such as superheavy dark matter decay. "
  "What this does not claim: it does not claim to have modeled the relay quantitatively, does not rule out exotic origins, and does not predict the exact maximum energy."),
 "sig_lens": "The Signature lens reads the rarest cosmic rays as overflow from a relay of accelerators, and asks what sequence of handoffs could compound a proton to 10^20 eV.",
 "how_it_works": "Auger and the Telescope Array measure air showers: fluorescence telescopes track the shower's development (revealing composition via depth of maximum), and ground arrays sample the particle footprint (revealing energy and direction). Theorists model candidate accelerators' maximum energies (Hillas criterion) and propagate particles through cosmic photon fields to predict the spectrum, composition, and anisotropy each source class should produce.",
 "key_points": [
  "Cosmic rays discovered 1912 (Hess); the spectrum spans 10^9 to 10^20 eV.",
  "GZK cutoff predicted 1966: protons above ~6 x 10^19 eV brake on the microwave background.",
  "Auger and Telescope Array see a suppression plus events beyond it.",
  "Composition trends heavy at the highest energies; source correlations are weak.",
  "Candidate accelerators: AGN jets, gamma-ray bursts, magnetars, cluster shocks.",
 ],
 "requirements": [
  "Identifying the sources via anisotropy, composition, and multi-messenger coincidences.",
  "An accelerator model reaching 10^20 eV within the GZK horizon \u2014 or proof none can.",
  "AugerPrime's upgraded composition measurements at the highest energies.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Greisen K. End to the cosmic-ray spectrum? Physical Review Letters. 1966;16:748-750.",
  "Zatsepin GT, Kuzmin VA. Upper limit of the spectrum of cosmic rays. JETP Letters. 1966;4:78-80.",
  "Pierre Auger Collaboration. Observation of a large-scale anisotropy in the arrival directions of cosmic rays above 8 x 10^18 eV. Science. 2017;357:1266-1270.",
  "Hillas AM. The origin of ultra-high-energy cosmic rays. Annual Review of Astronomy and Astrophysics. 1984;22:425-444.",
 ],
},
# ----------------------------------------------------------------- rank 13
{
 "key": "lithium-problem",
 "name": "The Cosmological Lithium Problem",
 "group": "Cosmology",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Big Bang nucleosynthesis predicts about three times more lithium-7 than the oldest stars actually contain \u2014 where did it go?",
 "description": "The Big Bang's nuclear furnace made hydrogen, helium, and traces of lithium in the first minutes, and its predictions for hydrogen, helium, and deuterium match observations beautifully. But lithium-7 comes out high by a factor of about three: theory says 4.7 x 10^-10 relative to hydrogen, the Spite plateau in old halo stars says about 1.6 x 10^-10. Everything else in BBN works \u2014 lithium alone rebels.",
 "background": "Big Bang nucleosynthesis (Gamow, Alpher, Herman, 1940s) became precision science when the microwave background fixed the baryon density: with eta = 6.1 x 10^-10, BBN predicts the light-element abundances with essentially no free parameters. Deuterium and helium-4 agree spectacularly. Lithium-7, measured in the atmospheres of the oldest metal-poor halo stars (the Spite plateau, discovered 1982), sits a factor of ~3 low \u2014 and the discrepancy has survived better nuclear cross-section measurements, better stellar modeling, and the Planck-era baryon density. Proposed fixes split three ways: stellar astrophysics (lithium destroyed or settled inside the stars), nuclear physics (a missed resonance altering BBN yields), and new physics (decaying particles altering nucleosynthesis). As of 2026 none has closed the gap cleanly.",
 "why_it_matters": "BBN is one of cosmology's three pillars, alongside the microwave background and the Hubble expansion. A persistent factor-of-three failure in its most delicate prediction either exposes missing stellar physics or is the fingerprint of new particles in the first minutes \u2014 both worth knowing.",
 "sig_pointer": "The Signature system's proposed approach treats the missing lithium as a stellar-ledger processing effect calibrated by the BBN ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the lithium problem is a stellar processing effect, not a cosmological one: the oldest stars quietly destroyed or buried their surface lithium over 13 billion years, and the Spite plateau measures the processed remainder, not the primordial value. "
  "Assumptions: (1) BBN's prediction of 4.7 x 10^-10 is correct; (2) atomic diffusion plus turbulent mixing operates in old halo stars at a level just below what standard stellar models include; (3) the plateau's remarkable flatness reflects a saturation of the depletion process, not pristine abundances. "
  "Reasoning path: the proposal notes that every alternative \u2014 new nuclear resonances, exotic BBN physics \u2014 must thread the needle of fixing lithium while preserving the perfect deuterium and helium agreement, whereas stellar depletion only needs a modest, independently plausible mixing process; the Signature reading is that the BBN ledger is right and the stellar ledger has been quietly editing its entries for 13 billion years. "
  "Proposed mechanism: atomic diffusion and rotationally induced mixing depleting surface lithium-7 by a factor of ~3 over the stars' lifetimes, saturating at the observed plateau. "
  "What would confirm it: detection of the predicted depletion signature \u2014 correlated lithium-6/lithium-7 behavior or diffusion-induced abundance patterns in the most pristine stars \u2014 matching quantitative stellar models with diffusion. "
  "What would kill it: a star found with lithium at the full BBN value and no depletion signature, or laboratory nuclear measurements revealing the missed resonance that fixes BBN directly. "
  "What this does not claim: it does not claim stellar models already include the needed mixing (they do not, fully), does not rule out new BBN physics, and does not explain why the plateau is so flat without fine-tuning the mixing."),
 "sig_lens": "The Signature lens reads the lithium gap as the stellar ledger quietly editing 13-billion-year-old entries, and asks whether the BBN ledger was right all along.",
 "how_it_works": "Observers measure lithium absorption lines in metal-poor halo stars (the Spite plateau) and increasingly in extragalactic systems. Nuclear physicists remeasure the key BBN reaction cross-sections at astrophysical energies. Stellar modelers add diffusion, rotation, and mixing to evolutionary codes. Cosmologists test exotic BBN scenarios against the full light-element suite \u2014 any fix must preserve deuterium and helium.",
 "key_points": [
  "BBN predicts 7Li/H \u2248 4.7 x 10^-10; the Spite plateau observes \u2248 1.6 x 10^-10.",
  "Deuterium and helium-4 predictions match observations precisely.",
  "The discrepancy is a factor of ~3 and decades old.",
  "Candidate fixes: stellar depletion, nuclear resonances, exotic early-universe physics.",
  "The Spite plateau (1982) is flat across stars, deepening the puzzle.",
 ],
 "requirements": [
  "Either a stellar mechanism quantitatively depleting lithium by ~3x, or new BBN physics.",
  "Any fix must preserve the deuterium and helium-4 agreements.",
  "Better nuclear cross-sections at BBN energies and better stellar atmosphere models.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Spite F, Spite M. Abundance of lithium in unevolved halo stars and old disk stars: interpretation and consequences. Astronomy & Astrophysics. 1982;115:357-366.",
  "Cyburt RH, Fields BD, Olive KA, Yeh TH. Big bang nucleosynthesis: present status. Reviews of Modern Physics. 2016;88:015004.",
  "Sbordone L et al. The metal-poor end of the Spite plateau. I. Astronomy & Astrophysics. 2010;522:A26.",
  "Fields BD. The primordial lithium problem. Annual Review of Nuclear and Particle Science. 2011;61:47-68.",
 ],
},
# ----------------------------------------------------------------- rank 14
{
 "key": "r-process-sites",
 "name": "Rapid Neutron-Capture Process Sites",
 "group": "Astrophysics",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Half the elements heavier than iron \u2014 gold, platinum, uranium \u2014 are forged by rapid neutron capture, but we still do not know which cosmic sites do most of the forging.",
 "description": "The r-process builds heavy nuclei by flooding seed nuclei with neutrons faster than they can beta-decay, climbing to uranium and beyond in seconds. It needs the most neutron-rich explosions in nature. The 2017 neutron-star-merger kilonova proved mergers do it \u2014 but whether mergers, rare supernovae, or something else dominate the galaxy's supply is still unsettled.",
 "background": "Burbidge, Burbidge, Fowler, and Hoyle's 1957 landmark paper identified neutron capture as the origin of heavy elements. For decades core-collapse supernovae were the assumed site, but simulations struggled to get conditions neutron-rich enough. The August 2017 gravitational-wave event GW170817 and its kilonova AT2017gfo changed everything: the glowing merger remnant's light curve matched radioactive decay of freshly made r-process elements, with an estimated ~0.05 solar masses ejected. Yet galactic chemical evolution models suggest mergers alone may be too rare or too slow to explain the earliest r-process-enriched stars, reviving magneto-rotational supernovae and collapsars as contributors. As of 2026 the merger-versus-supernova budget is still being argued.",
 "why_it_matters": "This is the origin story of the heavy half of the periodic table \u2014 the gold in rings, the iodine in medicine, the uranium in reactors. Settling the site budget tells us how the galaxy was chemically enriched and how often the universe's most violent events seed their surroundings with heavy elements.",
 "sig_pointer": "The Signature system's proposed approach treats heavy-element production as a two-ledger budget with mergers writing the late entries, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes a two-ledger budget: rare magneto-rotational supernovae wrote the early r-process entries (explaining the oldest enriched stars), and neutron star mergers dominate the late entries (explaining the kilonova and the modern budget) \u2014 the debate persists because each probe reads a different epoch's ledger. "
  "Assumptions: (1) both sites operate, with different delay-time distributions; (2) early galactic enrichment required a prompt source, which mergers \u2014 needing two supernovae plus inspiral time \u2014 struggle to provide; (3) kilonova ejecta masses like 0.05 solar masses are typical. "
  "Reasoning path: the proposal reconciles the apparently contradictory evidence by epoch: ancient halo stars enriched in r-process elements demand prompt sources (fast-rotating massive-star deaths), while the 2017 kilonova and merger-rate estimates account for the bulk of later enrichment; models that force a single site fail because the data span two regimes. "
  "Proposed mechanism: prompt magneto-rotational supernovae/collapsars for early enrichment, neutron star mergers for the dominant late budget, with the transition epoch set by the merger delay-time distribution. "
  "What would confirm it: galactic chemical evolution models requiring both components to fit the full stellar record, plus a second kilonova with measured ejecta confirming mergers' per-event yield while ancient-star statistics confirm a prompt component. "
  "What would kill it: merger rates and yields proving sufficient for the entire record including the earliest stars, or a confirmed r-process supernova with yields dwarfing mergers. "
  "What this does not claim: it does not claim the site fractions are known, does not specify the supernova mechanism's details, and does not rule out additional exotic sites."),
 "sig_lens": "The Signature lens reads heavy-element history as two ledgers \u2014 a prompt early one and a merger-dominated late one \u2014 and asks which epoch each probe is actually reading.",
 "how_it_works": "Gravitational-wave detectors (LIGO/Virgo/KAGRA) catch mergers; telescopes chase the kilonova light to weigh the ejecta. Stellar spectroscopists read r-process abundances in ancient halo stars as fossil records. Nuclear physicists measure masses and decay rates of exotic neutron-rich isotopes (FRIB) that set the r-process path. Chemical-evolution modelers combine rates, yields, and delay times to fit the galaxy's enrichment history.",
 "key_points": [
  "The r-process makes about half the elements heavier than iron, in seconds.",
  "B2FH (1957) identified neutron capture as the heavy-element origin.",
  "GW170817/AT2017gfo (2017): first confirmed r-process kilonova, ~0.05 solar masses ejected.",
  "Ancient r-process-enriched stars suggest a prompt source mergers struggle to provide.",
  "Magneto-rotational supernovae and collapsars are the leading additional candidates.",
 ],
 "requirements": [
  "Merger rates and per-event yields pinned down by more kilonovae.",
  "A confirmed r-process supernova, or proof supernovae cannot do it.",
  "Nuclear data for the exotic isotopes on the r-process path (FRIB program).",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Burbidge EM, Burbidge GR, Fowler WA, Hoyle F. Synthesis of the elements in stars. Reviews of Modern Physics. 1957;29:547-650.",
  "Abbott BP et al. (LIGO/Virgo). GW170817: observation of gravitational waves from a binary neutron star inspiral. Physical Review Letters. 2017;119:161101.",
  "Kasen D et al. Origin of the heavy elements in binary neutron-star mergers from a gravitational-wave event. Nature. 2017;551:80-84.",
  "Cowan JJ et al. Origin of the heaviest elements: the rapid neutron-capture process. Reviews of Modern Physics. 2021;93:015002.",
 ],
},
# ----------------------------------------------------------------- rank 15
{
 "key": "muon-g-2",
 "name": "The Muon g-2 Anomaly",
 "group": "Particle Physics",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "The muon's magnetic wobble disagrees with the Standard Model's prediction \u2014 but the disagreement keeps shifting as the theory calculation improves.",
 "description": "Dirac's theory says a muon's magnetic moment should be g = 2; quantum fluctuations nudge it higher by the 'anomaly' a_mu = (g-2)/2. The Brookhaven and Fermilab experiments measure a_mu with exquisite precision, and for years it sat about 4-5 sigma above the Standard Model consensus \u2014 until improved lattice-QCD calculations of the hadronic contribution moved the theory, shrinking the gap. The anomaly's status is genuinely in flux.",
 "background": "Julian Schwinger's 1948 calculation of the first quantum correction (alpha/2pi) made g-2 the flagship precision test of quantum electrodynamics. The Brookhaven E821 experiment (final 2006) found a 3.7-sigma excess over theory. Fermilab's Muon g-2 experiment confirmed the experimental value with better precision (2021, 2023), pushing the discrepancy past 5 sigma against the 2020 Theory Initiative consensus. Then the plot twisted: the BMW lattice-QCD collaboration's 2021 calculation of the hadronic vacuum polarization \u2014 the theory's hardest piece \u2014 came out higher, closer to experiment, and subsequent lattice results plus reanalyses of the e+e- data behind the old consensus have steadily eroded the discrepancy. As of 2026 the field is converging on the view that the 'anomaly' was substantially a theory-calculation problem, though the final word awaits the complete Fermilab dataset and further lattice cross-checks.",
 "why_it_matters": "A confirmed g-2 discrepancy would be a roadmap to new particles \u2014 supersymmetry, dark photons, leptoquarks all predict shifts. The saga is also a masterclass in how precision science self-corrects: the resolution, whichever way it lands, sharpens both experiment and theory for the next anomaly.",
 "sig_pointer": "The Signature system's proposed approach treats the shifting anomaly as the theory ledger catching up to the measurement ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the muon g-2 story is a ledger reconciliation: the measurement ledger was right all along, and the theory ledger contained an undervalued entry \u2014 the hadronic vacuum polarization \u2014 whose correction dissolves most of the 'new physics' signal. "
  "Assumptions: (1) the Fermilab experimental value stands; (2) lattice QCD, with all systematics controlled, is the more reliable route to the hadronic contribution than the dispersive e+e- data; (3) any remaining residual discrepancy is small. "
  "Reasoning path: the proposal applies Occam's ledger \u2014 before invoking new particles, audit the hardest theory entry; the BMW lattice result did exactly that and the discrepancy shrank, which the Signature reading takes as the expected outcome when a precision anomaly lives in the least-controlled calculation; new physics is then constrained to hide in whatever small residual survives. "
  "Proposed mechanism: no new mechanism \u2014 the proposal is methodological: the Standard Model prediction, correctly computed, matches the measurement, and the episode becomes a calibration of how hadronic uncertainties can masquerade as new physics. "
  "What would confirm it: independent lattice groups converging on the higher hadronic value, the final Fermilab analysis agreeing with the corrected theory, and no new-physics model needed. "
  "What would kill it: a persistent, lattice-robust residual above ~3 sigma after all cross-checks \u2014 which would resurrect the new-physics interpretation (dark photon, SUSY, etc.). "
  "What this does not claim: it does not claim the story is over (the final Fermilab result and more lattice confirmations are pending), does not claim new physics is excluded, and does not dismiss the dispersive approach's internal tensions, which themselves need understanding."),
 "sig_lens": "The Signature lens reads the g-2 saga as a ledger audit \u2014 the hardest theory entry was undervalued \u2014 and asks what small residual, if any, survives the reconciliation.",
 "how_it_works": "Fermilab stores muons in a precision magnetic ring and measures their spin precession relative to their orbit \u2014 the anomaly appears directly as a frequency. Theorists compute a_mu from QED (five loops), electroweak, and hadronic contributions; the hadronic vacuum polarization dominates the uncertainty and is attacked two ways: dispersively from e+e- collision data, and directly from lattice QCD. J-PARC plans an independent experimental approach.",
 "key_points": [
  "Schwinger 1948: first quantum correction alpha/2pi; g-2 is the flagship precision test.",
  "Brookhaven E821: 3.7-sigma excess; Fermilab confirmed the experimental value (2021/2023).",
  "The 2020 theory consensus put the discrepancy above 4 sigma.",
  "BMW lattice QCD (2021) raised the hadronic contribution, shrinking the gap.",
  "As of 2026 the anomaly is substantially reduced; final verdict pending.",
 ],
 "requirements": [
  "The complete Fermilab dataset and its final uncertainty.",
  "Independent lattice-QCD confirmations of the hadronic contribution.",
  "Resolution of the tension between lattice and dispersive (e+e-) determinations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bennett GW et al. (Muon g-2 Collaboration). Final report of the E821 muon anomalous magnetic moment measurement at BNL. Physical Review D. 2006;73:072003.",
  "Abi B et al. (Muon g-2 Collaboration). Measurement of the positive muon anomalous magnetic moment to 0.46 ppm. Physical Review Letters. 2021;127:072001.",
  "Aoyama T et al. The anomalous magnetic moment of the muon in the Standard Model. Physics Reports. 2020;887:1-166.",
  "Borsanyi S et al. (BMW Collaboration). Leading hadronic contribution to the muon magnetic moment from lattice QCD. Nature. 2021;593:51-55.",
 ],
},
# ----------------------------------------------------------------- rank 16
{
 "key": "strong-cp",
 "name": "The Strong CP Problem",
 "group": "Particle Physics",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Quantum chromodynamics permits a CP-violating parameter, theta, that could be anything from 0 to 2pi \u2014 yet measurements force it below 10^-10. Why is it so tiny?",
 "description": "The equations of the strong force naturally include a term that violates CP symmetry, with a free angle theta. Nothing in the theory prefers small theta \u2014 yet the neutron's electric dipole moment, which theta would generate, is unobservably small, bounding theta below 10^-10. A parameter that could be of order one is at least ten orders of magnitude smaller, with no accepted reason.",
 "background": "The theta term's CP violation was recognized in the 1970s as QCD matured. The neutron electric dipole moment (nEDM) experiments \u2014 ultracold neutrons in precision electromagnetic traps \u2014 have pushed the limit down to |d_n| < 1.8 x 10^-26 e-cm, which translates to theta < 10^-10. The leading solution, Peccei and Quinn's 1977 proposal of a new symmetry whose breaking dynamically relaxes theta to zero, predicts the axion \u2014 now also a premier dark matter candidate, hunted by ADMX and other haloscopes. Alternatives include the Nelson-Barr mechanism (CP as a spontaneously broken symmetry) and a massless up quark (excluded by lattice QCD). Decades of nEDM searches and axion hunts have found neither a dipole moment nor an axion. As of 2026 the strong CP problem stands unsolved, with the axion its most beautiful unconfirmed answer.",
 "why_it_matters": "A number that 'should' be of order one but is 10^-10 cries out for explanation \u2014 this is the original naturalness problem. Its leading solution, the axion, would simultaneously solve a second cosmic mystery as dark matter, making this one problem's answer potentially two discoveries.",
 "sig_pointer": "The Signature system's proposed approach treats theta as a ledger angle pinned by a cosmic relaxation process, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that theta is small because the early universe dynamically relaxed it: a Peccei-Quinn-like angular ledger existed, rolled to its minimum during cosmic history, and the axion is the leftover ripple of that rolling \u2014 making the axion's existence the testable residue of the relaxation. "
  "Assumptions: (1) a global symmetry broken in the early universe produced an angular degree of freedom; (2) QCD effects generated a potential minimized at theta = 0; (3) the field settled before nucleosynthesis, leaving cold axion oscillations as dark matter. "
  "Reasoning path: the proposal treats small numbers as dynamical outcomes rather than tuned inputs \u2014 the Signature reading is that whenever physics presents an absurdly small parameter, look for a rolling process that drove it there; the axion is then not an add-on but the required exhaust of the relaxation, which is why the axion dark matter program doubles as a strong-CP test. "
  "Proposed mechanism: standard Peccei-Quinn relaxation, with the Signature emphasis that the relaxation epoch's imprint (axion mass, abundance) is fixed by when the rolling completed. "
  "What would confirm it: a haloscope detection (ADMX or successor) of the axion at a mass and coupling consistent with the dark matter abundance \u2014 one discovery solving both problems. "
  "What would kill it: axion searches excluding the full plausible mass window with no signal, or a measured nonzero nEDM at a level implying theta is small but not dynamically relaxed (favoring Nelson-Barr or anthropic selection). "
  "What this does not claim: it does not claim the axion exists (unconfirmed), does not derive the Peccei-Quinn scale from deeper principles, and does not rule out that theta's smallness is environmental or accidental."),
 "sig_lens": "The Signature lens reads theta's tininess as the endpoint of a cosmic rolling process, and asks what ripple \u2014 the axion \u2014 that rolling must have left behind.",
 "how_it_works": "nEDM experiments trap ultracold neutrons and look for a minuscule energy shift in electric fields \u2014 the current limit is 1.8 x 10^-26 e-cm. Axion haloscopes (ADMX, CAPP, MADMAX concepts) search for dark-matter axions converting to photons in strong magnetic fields; helioscopes (CAST, IAXO) look for solar axions; light-shining-through-walls experiments probe axion-like particles. Lattice QCD tests the massless-up-quark escape route (closed).",
 "key_points": [
  "QCD's theta parameter could be order one; experiment bounds it below 10^-10.",
  "The neutron EDM limit (|d_n| < 1.8 x 10^-26 e-cm) sets the bound.",
  "Peccei-Quinn (1977) symmetry predicts the axion, also a dark matter candidate.",
  "Alternatives: Nelson-Barr mechanism; massless up quark (excluded by lattice).",
  "Neither an nEDM nor an axion has been detected.",
 ],
 "requirements": [
  "An axion detection, a nonzero nEDM, or a verified alternative mechanism.",
  "Haloscope coverage of the full plausible axion mass window.",
  "A theory explaining why the Peccei-Quinn scale takes its value.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Peccei RD, Quinn HR. CP conservation in the presence of pseudoparticles. Physical Review Letters. 1977;38:1440-1443.",
  "Weinberg S. A new light boson? Physical Review Letters. 1978;40:223-226.",
  "Wilczek F. Problem of strong P and T invariance in the presence of instantons. Physical Review Letters. 1978;40:279-282.",
  "Abel C et al. Measurement of the permanent electric dipole moment of the neutron. Physical Review Letters. 2020;124:081803.",
 ],
},
# ----------------------------------------------------------------- rank 17
{
 "key": "proton-spin-crisis",
 "name": "The Proton Spin Crisis",
 "group": "Particle Physics",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "The proton's spin is 1/2, but its quarks' spins add up to only about a third of it \u2014 where is the rest hiding?",
 "description": "The naive quark model says the proton's spin comes from its three quarks. The 1988 European Muon Collaboration measurement found the quarks contribute only ~30 percent. Nearly four decades later, gluon spin and orbital angular momentum are the prime suspects, but the full accounting \u2014 who carries the missing 70 percent \u2014 is still incomplete.",
 "background": "The crisis began with EMC's polarized deep-inelastic scattering result in 1988: the quark spin contribution Delta Sigma measured about 0.3, not 1. The 'spin crisis' launched a generation of spin-physics experiments \u2014 SMC, COMPASS, HERMES, and RHIC's polarized proton program \u2014 which established that gluon spin contributes (Delta G is nonzero but modest in the measured range) and that orbital angular momentum must carry a large share. The theoretical framework matured too: Ji's spin sum rule and generalized parton distributions (GPDs) formalized how quark/gluon spin and orbital pieces add to 1/2. The planned Electron-Ion Collider (EIC) is designed to map the gluon and sea-quark contributions precisely. As of 2026 the ledger is partially filled \u2014 quarks ~30 percent, gluons a meaningful but range-limited share, orbital motion the balance \u2014 but the complete, precise accounting awaits the EIC.",
 "why_it_matters": "Spin is as fundamental as charge and mass, and the proton is the building block of visible matter. Completing its spin budget tests quantum chromodynamics in its full glory \u2014 spin, orbital motion, and the glue that binds \u2014 and the EIC's 3D imaging of the proton is the microscope that will do it.",
 "sig_pointer": "The Signature system's proposed approach treats the missing spin as orbital motion in the proton's internal ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the missing proton spin is carried as orbital angular momentum of quarks and gluons swirling inside the proton \u2014 the proton is a tiny dynamical system, and like any spinning system, much of its angular momentum lives in orbital motion rather than intrinsic spins. "
  "Assumptions: (1) Ji's spin decomposition is the physically meaningful ledger; (2) the gluon orbital contribution is large and positive; (3) the EIC will measure the generalized parton distributions needed to complete the accounting. "
  "Reasoning path: the proposal notes that the 'crisis' was only a crisis for the naive static quark model \u2014 once the proton is treated as a relativistic, interacting many-body system, orbital angular momentum is expected to dominate, just as Earth's orbital angular momentum dwarfs its spin; the Signature reading is that the ledger was always complete in principle, and the missing entries are orbital ones that existing experiments could not itemize. "
  "Proposed mechanism: no new mechanism \u2014 the proposal is that standard QCD, via Ji's sum rule, already contains the full 1/2, with the orbital pieces to be measured by the EIC's deeply virtual Compton scattering program. "
  "What would confirm it: EIC measurements of GPDs yielding quark and gluon orbital contributions that, added to the known spin pieces, sum to 1/2 within uncertainties. "
  "What would kill it: the completed ledger failing to sum to 1/2, which would signal a fundamental problem in the QCD spin decomposition itself. "
  "What this does not claim: it does not claim the orbital pieces are already measured (they are not), does not predict their individual sizes, and does not rule out surprises in the gluon sector."),
 "sig_lens": "The Signature lens reads the spin crisis as an incomplete ledger rather than a broken theory, and asks what orbital entries the next microscope must itemize.",
 "how_it_works": "Polarized deep-inelastic scattering (COMPASS, HERMES, JLab) measures quark and gluon helicity distributions; RHIC's polarized proton collisions constrain gluon spin; deeply virtual Compton scattering accesses generalized parton distributions encoding orbital motion. The Electron-Ion Collider will combine high luminosity, polarization, and wide kinematics to complete the decomposition.",
 "key_points": [
  "EMC 1988: quarks carry only ~30 percent of the proton's spin (Delta Sigma ~ 0.3).",
  "Gluon spin is nonzero; orbital angular momentum must carry much of the rest.",
  "Ji's sum rule formalizes the complete spin budget: 1/2 = quark spin + gluon spin + orbital.",
  "RHIC, COMPASS, and JLab progressively filled in the entries.",
  "The Electron-Ion Collider is designed to finish the accounting.",
 ],
 "requirements": [
  "EIC measurements of generalized parton distributions (orbital motion).",
  "Gluon spin pinned down across the full momentum range.",
  "The complete ledger summing to 1/2 within uncertainties.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ashman J et al. (EMC). A measurement of the spin asymmetry and determination of the structure function g1 in deep inelastic muon-proton scattering. Physics Letters B. 1988;206:364-370.",
  "Ji XD. Gauge-invariant decomposition of nucleon spin. Physical Review Letters. 1997;78:610-613.",
  "Aidala CA, Bass SD, Hasch D, Mallot GK. The spin structure of the nucleon. Reviews of Modern Physics. 2013;85:655-691.",
  "Accardi A et al. Electron-Ion Collider: the next QCD frontier. European Physical Journal A. 2016;52:268.",
 ],
},
]

ENTRIES += [
# ----------------------------------------------------------------- rank 18
{
 "key": "quark-confinement",
 "name": "Quark Confinement",
 "group": "Particle Physics",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Quarks can never be isolated \u2014 pull two apart and the force between them stays constant until new quarks materialize \u2014 yet no one has derived this from the equations of quantum chromodynamics.",
 "description": "The strong force between quarks does not weaken with distance like gravity or electromagnetism; it stays roughly constant, so separating quarks takes ever more energy until it becomes cheaper to create new quark-antiquark pairs from the vacuum. This 'confinement' is confirmed experimentally beyond doubt \u2014 no free quark has ever been seen \u2014 but it has never been proven from first principles. The related Yang-Mills mass-gap problem is a Clay Millennium Prize.",
 "background": "Quarks were proposed by Gell-Mann and Zweig in 1964; deep-inelastic scattering at SLAC (1968) proved pointlike constituents inside the proton. Asymptotic freedom (Gross, Politzer, Wilczek, Nobel 2004) explained why quarks behave almost freely at short distances \u2014 but the flip side, confinement at long distances, resisted derivation. Lattice QCD demonstrates confinement numerically with overwhelming evidence, yet an analytic proof that pure Yang-Mills theory confines and has a mass gap remains one of the Clay Mathematics Institute's seven Millennium Prize Problems (one solved: Poincar\u00e9). Dual-superconductor pictures, center vortices, and string models each capture aspects. As of 2026 confinement is observed, simulated, modeled \u2014 but not proven.",
 "why_it_matters": "Confinement is why matter looks the way it does: it locks quarks into protons and neutrons, setting the mass of everything (most of your mass is confinement energy, not Higgs mass). Proving it would complete quantum chromodynamics and crack a Millennium Prize; the techniques would advance quantum field theory everywhere.",
 "sig_pointer": "The Signature system's proposed approach treats confinement as the color ledger's no-exit rule enforced by flux-tube bookkeeping, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that confinement is a bookkeeping rule of the color ledger: color charge must always sum to neutral within any observable region, and the flux tube between separated quarks is the ledger's way of keeping the accounts \u2014 its constant energy per unit length is the cost of carrying unbalanced color across space. "
  "Assumptions: (1) the QCD vacuum behaves as a dual superconductor that squeezes color flux into tubes; (2) the tube's string tension (~0.9 GeV/fm) is set by the vacuum's properties, not by the quarks; (3) pair creation is the ledger's cheaper alternative once the tube's stored energy exceeds two quark masses. "
  "Reasoning path: the proposal takes the linear potential as the primary fact and asks what ledger rule makes linearity inevitable \u2014 a no-exit rule for color, where the tube is the accounting string; the mass gap (no massless glueballs) then follows because the tube itself has tension, giving every excitation a minimum energy. "
  "Proposed mechanism: dual-superconductor flux tubes with pair-creation cutoff, in the spirit of the Lund string model but elevated to the confinement explanation. "
  "What would confirm it: lattice measurements pinning the flux-tube profile and string tension to the dual-superconductor prediction across temperatures, plus a demonstrated analytic path from the tube picture to the mass gap. "
  "What would kill it: an analytic proof of confinement via a completely different mechanism (e.g., center vortices alone), or experimental discovery of a free quark or stable colored exotic contradicting the no-exit rule. "
  "What this does not claim: it does not claim to supply the missing Millennium proof, does not derive the string tension from first principles, and does not choose between dual-superconductor and vortex pictures."),
 "sig_lens": "The Signature lens reads confinement as the color ledger's no-exit rule, and asks what accounting string \u2014 the flux tube \u2014 enforces it.",
 "how_it_works": "Lattice QCD simulates the theory on supercomputers and measures the static quark potential (linear rise), flux-tube profiles, and glueball spectra. Experimentally, deep-inelastic scattering and jet physics confirm the short-distance side; the absence of free quarks in cosmic rays, colliders, and Millikan-style searches confirms the long-distance side. Theorists pursue analytic proofs via dualities, vortices, and string models.",
 "key_points": [
  "No free quark has ever been observed; the interquark potential rises linearly (~0.9 GeV/fm).",
  "Asymptotic freedom (Nobel 2004) explains short distances; confinement rules long distances.",
  "Lattice QCD demonstrates confinement numerically but does not prove it analytically.",
  "The Yang-Mills existence and mass-gap problem is a Clay Millennium Prize.",
  "Most of the proton's (and your) mass is confinement energy, not Higgs-derived quark mass.",
 ],
 "requirements": [
  "An analytic proof that Yang-Mills theory confines and has a mass gap.",
  "Derivation of the string tension from the QCD Lagrangian.",
  "A unified picture connecting flux tubes, vortices, and the mass gap.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gell-Mann M. A schematic model of baryons and mesons. Physics Letters. 1964;8:214-215.",
  "Gross DJ, Wilczek F. Ultraviolet behavior of non-abelian gauge theories. Physical Review Letters. 1973;30:1343-1346.",
  "Politzer HD. Reliable perturbative results for strong interactions? Physical Review Letters. 1973;30:1346-1349.",
  "Greensite J. An Introduction to the Confinement Problem. Lecture Notes in Physics 821, Springer; 2011.",
 ],
},
# ----------------------------------------------------------------- rank 19
{
 "key": "quantum-measurement",
 "name": "The Quantum Measurement Problem",
 "group": "Quantum Foundations",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Quantum mechanics describes systems as superpositions evolving smoothly \u2014 yet measurements yield single, definite outcomes. What counts as a measurement, and what selects the outcome?",
 "description": "The Schr\u00f6dinger equation never produces a single outcome; it evolves superpositions deterministically. But every experiment ends with one definite result. The textbook 'collapse' postulate is an add-on, not a derivation: the theory does not say what constitutes a measurement, when collapse happens, or what picks the outcome. A century in, the interpretations multiply and the problem stands.",
 "background": "Von Neumann's 1932 formalism split the world into smooth evolution and abrupt collapse. Schr\u00f6dinger's 1935 cat dramatized the absurdity of collapse-at-observation. Everett's 1957 many-worlds removed collapse by keeping every outcome; Bohm's pilot wave (1952) added hidden positions; GRW (1986) and Penrose proposed objective physical collapse; QBism reframed quantum states as personal beliefs. Decoherence theory (Zeh, Zurek, 1970s-80s) explained why interference vanishes in practice \u2014 the environment measures everything continuously \u2014 but not why one outcome becomes actual. Loophole-free Bell tests (2015) confirmed entanglement's nonlocal correlations without settling the interpretation. As of 2026 the measurement problem is philosophy-grade physics: empirically equivalent interpretations, no consensus, active experiments probing collapse models.",
 "why_it_matters": "This is the question of what quantum mechanics says about reality \u2014 whether the moon is there when nobody looks, whether the universe splits, whether consciousness matters. It also has teeth: collapse models make testable predictions (spontaneous heating, anomalous decoherence) that tabletop experiments are now probing, and quantum computing's error models depend on understanding decoherence deeply.",
 "sig_pointer": "The Signature system's proposed approach treats measurement as the universe's ledger committing an entry when information becomes irreversible, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that measurement is ledger commitment: a quantum event becomes definite when its information spreads irreversibly into the environment \u2014 at that point the universe's ledger has recorded it, and no operation within the universe can un-record it. "
  "Assumptions: (1) unitarity holds universally \u2014 nothing ever truly collapses; (2) irreversibility is a practical, thermodynamic fact about information dispersal, not a new dynamical law; (3) the appearance of a single outcome is what commitment looks like from inside the ledger. "
  "Reasoning path: the proposal sides with decoherence but adds the commitment criterion \u2014 interference is lost when the environment learns the outcome (decoherence), and the outcome becomes 'the' outcome when the record is thermodynamically irreversible; the Signature reading dissolves the problem by locating definiteness in the ledger's write-once property rather than in consciousness, many worlds, or new physics. "
  "Proposed mechanism: environmental decoherence plus thermodynamic irreversibility as the joint criterion for measurement; no modification of the Schr\u00f6dinger equation. "
  "What would confirm it: collapse-model experiments (e.g., MAQRO-style, LISA Pathfinder heritage, optomechanical tests) continuing to find zero anomalous collapse noise down to the most sensitive scales, and quantum computers' error budgets fully explained by environmental decoherence with no residual 'fundamental' decoherence. "
  "What would kill it: a verified objective-collapse signal \u2014 spontaneous heating or decoherence with no environmental source \u2014 which would prove measurement is a new physical process, not ledger commitment. "
  "What this does not claim: it does not claim to derive the Born rule's probabilities from commitment alone (the probability question remains), does not refute many-worlds (empirically equivalent), and does not explain why we experience one branch."),
 "sig_lens": "The Signature lens reads measurement as the universe's ledger committing an entry \u2014 definite when the record becomes irreversible \u2014 and asks what, physically, makes a record un-erasable.",
 "how_it_works": "Foundations experimentalists test collapse models by looking for anomalous decoherence or heating in optomechanical resonators, matter-wave interferometers with large molecules, and space-based test masses. Theorists sharpen the interpretations' differing predictions (where they differ at all) and study decoherence in quantum computing platforms, where the measurement problem meets engineering.",
 "key_points": [
  "The Schr\u00f6dinger equation predicts superpositions; experiments yield single outcomes.",
  "Von Neumann (1932) formalized the collapse postulate; Schr\u00f6dinger's cat (1935) exposed its strangeness.",
  "Interpretations: Copenhagen, many-worlds (1957), pilot-wave, objective collapse, QBism.",
  "Decoherence explains the disappearance of interference, not the selection of outcomes.",
  "Collapse models (GRW, Penrose) make testable predictions now being probed.",
 ],
 "requirements": [
  "An experiment distinguishing collapse models from no-collapse interpretations \u2014 or proof none can.",
  "A derivation of the Born rule acceptable across interpretations.",
  "Agreement on what, physically, constitutes a measurement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "von Neumann J. Mathematische Grundlagen der Quantenmechanik. Springer; 1932.",
  "Everett H III. 'Relative state' formulation of quantum mechanics. Reviews of Modern Physics. 1957;29:454-462.",
  "Zurek WH. Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics. 2003;75:715-775.",
  "Schlosshauer M. Decoherence and the Quantum-to-Classical Transition. Springer; 2007.",
 ],
},
# ----------------------------------------------------------------- rank 20
{
 "key": "black-hole-information",
 "name": "The Black Hole Information Paradox",
 "group": "Quantum Gravity",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Black holes evaporate by Hawking radiation \u2014 but if the radiation carries no information about what fell in, quantum mechanics' most sacred principle is violated. Does information escape, and how?",
 "description": "Hawking's 1974 calculation showed black holes radiate and slowly evaporate. The radiation looks thermal \u2014 featureless \u2014 which suggests the information about infalling matter is destroyed, violating unitarity, the quantum principle that information is never truly lost. Fifty years of debate have produced firewalls, fuzzballs, islands, and replica wormholes \u2014 but no consensus on how (or whether) the information gets out.",
 "background": "Jacob Bekenstein (1973) proposed black holes have entropy proportional to horizon area; Hawking's 1974-75 work fixed the temperature and made evaporation inevitable. In 1976 Hawking argued the radiation's thermality meant information loss. The AdS/CFT correspondence (Maldacena 1997) strongly suggested quantum gravity is unitary, sharpening the paradox: the boundary theory preserves information, so the bulk must too \u2014 but how? AMPS (2012) argued the assumptions lead to a 'firewall' at the horizon, trading one paradox for another. The 2019-2020 'island' and replica-wormhole calculations reproduced the expected Page curve (information returning in late radiation) within semiclassical gravity \u2014 a breakthrough in calculation, though its physical interpretation is still debated. As of 2026 the Page curve can be derived; what it means for an infalling observer remains contested.",
 "why_it_matters": "Unitarity is the load-bearing wall of quantum mechanics; black holes are where gravity seems to knock it down. Resolving the paradox means understanding how spacetime, quantum information, and gravity fit together \u2014 the core of quantum gravity \u2014 and the new tools (islands, wormholes) are already reshaping the field.",
 "sig_pointer": "The Signature system's proposed approach treats the paradox as a ledger-reading problem: the information is in the radiation ledger all along, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that there is no paradox because the information was never inside in the ledger's accounting: the black hole's degrees of freedom live at the horizon, and Hawking radiation is the horizon ledger being read out slowly \u2014 the information 'escapes' because it was never behind the horizon in the bookkeeping. "
  "Assumptions: (1) the holographic principle holds \u2014 a region's information content scales with its boundary area; (2) Hawking radiation, though locally thermal, carries subtle correlations encoding the horizon state; (3) an infalling observer's experience is complementary to, not contradictory with, the outside account. "
  "Reasoning path: the proposal takes black hole complementarity seriously and adds the ledger principle \u2014 bookkeeping done at the horizon makes 'inside' a derived concept; the Page curve's turnover is then simply the point where the radiation ledger holds more entries than the remaining horizon ledger, which is why information starts coming out; islands and replica wormholes are the mathematics catching up to this bookkeeping. "
  "Proposed mechanism: horizon-stored information leaking via entangled Hawking pairs, with the late radiation purifying the early radiation (ER=EPR-style connectivity in the semiclassical description). "
  "What would confirm it: a complete, agreed-upon derivation of the Page curve from a UV-complete theory (string theory) with a clear account of the infalling observer \u2014 or laboratory analog-gravity experiments showing information recovery in analog Hawking radiation. "
  "What would kill it: proof that the island calculation is a mathematical artifact with no physical meaning, or a verified violation of unitarity in black hole evaporation. "
  "What this does not claim: it does not claim the paradox is solved (the interpretation debate is live), does not resolve the firewall question for infalling observers, and does not claim analog experiments are equivalent to real black holes."),
 "sig_lens": "The Signature lens reads the paradox as a bookkeeping confusion \u2014 the information was always in the horizon ledger \u2014 and asks what the Page curve's turnover means for who holds the entries.",
 "how_it_works": "Theorists compute Hawking radiation's entanglement structure (Page curve), test unitarity via AdS/CFT, and model horizons as fuzzballs, firewalls, or islands. Experimentalists build analog black holes \u2014 Bose-Einstein condensates, optical fibers, water tanks \u2014 where analog Hawking radiation is measured and its correlations studied. Quantum information theorists reframe the paradox in terms of error correction and scrambling.",
 "key_points": [
  "Hawking (1974): black holes radiate thermally and evaporate.",
  "Thermal radiation implies information loss, violating quantum unitarity.",
  "Bekenstein-Hawking entropy: S proportional to horizon area.",
  "AdS/CFT (1997) suggests the full theory is unitary, sharpening the paradox.",
  "Island/replica-wormhole calculations (2019-2020) reproduce the Page curve; interpretation debated.",
 ],
 "requirements": [
  "A UV-complete account of how information returns (string theory derivation).",
  "Resolution of the firewall debate for infalling observers.",
  "Agreement on what the island calculation physically means.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hawking SW. Black hole explosions? Nature. 1974;248:30-31.",
  "Hawking SW. Breakdown of predictability in gravitational collapse. Physical Review D. 1976;14:2460-2473.",
  "Maldacena JM. The large N limit of superconformal field theories and supergravity. Advances in Theoretical and Mathematical Physics. 1998;2:231-252.",
  "Almheiri A, Marolf D, Polchinski J, Sully J. Black holes: complementarity or firewalls? Journal of High Energy Physics. 2013;02:062.",
 ],
},
# ----------------------------------------------------------------- rank 21
{
 "key": "singularity-resolution",
 "name": "Black Hole Singularity Resolution",
 "group": "Quantum Gravity",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "General relativity predicts that inside a black hole, matter collapses to a point of infinite density \u2014 but infinities in physics are a sign the theory has broken down. What actually happens at the center?",
 "description": "Penrose's singularity theorems prove that, under reasonable conditions, gravitational collapse in general relativity cannot stop: it ends at a singularity where curvature and density become infinite. Physicists read 'infinity' as 'new physics needed' \u2014 quantum gravity should take over at the Planck scale (10^-35 m, 10^96 kg/m^3) \u2014 but no agreed theory says what replaces the singularity: a bounce, a fuzzball, a wormhole, or something without a name yet.",
 "background": "The Schwarzschild solution (1916) already contained the singularity; Penrose's 1965 singularity theorems (Nobel Prize 2020) made it unavoidable in classical GR. Candidate resolutions come from every quantum gravity program: loop quantum gravity predicts a bounce (the interior rebounds into a new expanding region \u2014 loop quantum cosmology), string theory's fuzzball proposal replaces the horizon-and-singularity with a horizonless quantum fuzz, and some models connect the interior to another universe via a wormhole-like throat. The Planck density, about 5 x 10^96 kg/m^3, marks where quantum gravity must dominate \u2014 80 orders of magnitude beyond anything testable. As of 2026 every resolution is theoretical; the singularity's true nature is pure quantum-gravity territory.",
 "why_it_matters": "The singularity is where our two great theories collide most violently \u2014 GR says 'infinite,' quantum mechanics says 'impossible.' Whatever resolves it is a direct window into quantum gravity, and different resolutions predict different fates: bounce cosmologies, baby universes, or information-preserving fuzzballs.",
 "sig_pointer": "The Signature system's proposed approach treats the singularity as the ledger's overflow point where a new entry type begins, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the singularity is a ledger overflow: the collapsing matter's bookkeeping entries pile up until the spacetime ledger can no longer represent them, at which point the ledger starts a new page \u2014 a bounce \u2014 rather than writing an infinite entry. "
  "Assumptions: (1) spacetime has a minimum representable scale (Planck scale discreteness); (2) collapse halts when density reaches the Planck density, where quantum geometry repulsion balances gravity; (3) the bounce is asymmetric in time from the outside view but symmetric in the ledger's own accounting. "
  "Reasoning path: the proposal follows loop quantum cosmology's bounce but frames it as bookkeeping necessity \u2014 an infinite entry is not a physical prediction but a ledger failure, and the minimal fix is a new page; the interior then connects to an expanding region, making black holes potential seeds of new expanding spacetimes (in the spirit of Smolin's cosmological natural selection, without endorsing its details). "
  "Proposed mechanism: quantum-geometry repulsion at Planck density triggering a bounce, with the pre-bounce collapse and post-bounce expansion as two pages of one ledger. "
  "What would confirm it: gravitational-wave echoes following merger ringdowns \u2014 repeating, fading signals from a structure just outside where the horizon would be \u2014 matching bounce/fuzzball templates; or a complete loop-quantum-gravity derivation of the bounce with unique predictions. "
  "What would kill it: LIGO/Virgo/KAGRA data ruling out echoes at the sensitivity where bounce models require them, or a UV-complete theory (e.g., string theory) proving horizons are exactly as GR says with singularities resolved differently. "
  "What this does not claim: it does not claim echoes have been detected (claimed detections are disputed), does not claim loop quantum gravity is the correct theory, and does not predict what an infalling observer experiences at the bounce."),
 "sig_lens": "The Signature lens reads the singularity as a ledger overflow \u2014 infinity as bookkeeping failure \u2014 and asks what new page the ledger starts when it cannot write the old one.",
 "how_it_works": "Quantum gravity theorists model the interior with loop quantum cosmology, string fuzzballs, and regular-black-hole metrics, deriving predictions like gravitational-wave echoes or modified ringdowns. Gravitational-wave observatories search merger signals for echo templates. Analog-gravity experiments test singularity-like behavior in fluids and condensates. The work is theoretical, with echoes as the main observational hope.",
 "key_points": [
  "Penrose's singularity theorems (1965, Nobel 2020) make singularities unavoidable in classical GR.",
  "The Planck density (~5 x 10^96 kg/m^3) marks where quantum gravity must take over.",
  "Candidate resolutions: loop-quantum bounce, string fuzzballs, wormhole throats, regular black holes.",
  "Gravitational-wave 'echoes' are the leading observational test; claimed detections are disputed.",
  "No resolution is confirmed; the interior is pure quantum-gravity territory.",
 ],
 "requirements": [
  "A UV-complete quantum gravity theory deriving the interior from first principles.",
  "Observational evidence: confirmed echoes, or another interior probe.",
  "Agreement between the singularity resolution and the information paradox resolution.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Penrose R. Gravitational collapse and space-time singularities. Physical Review Letters. 1965;14:57-59.",
  "Ashtekar A, Singh P. Loop quantum cosmology: a status report. Classical and Quantum Gravity. 2011;28:213001.",
  "Mathur SD. The fuzzball proposal for black holes: an elementary review. Fortschritte der Physik. 2005;53:793-827.",
  "Cardoso V, Pani P. Tests for the existence of black holes through gravitational wave echoes. Nature Astronomy. 2017;1:0067.",
 ],
},
# ----------------------------------------------------------------- rank 22
{
 "key": "vacuum-metastability",
 "name": "Vacuum Metastability",
 "group": "Particle Physics",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "The Higgs field's measured properties suggest our vacuum may not be the true lowest-energy state \u2014 the universe could be metastable, awaiting a catastrophic decay to a deeper vacuum.",
 "description": "The Higgs boson's mass (125 GeV) and the top quark's mass together determine how the Higgs self-interaction evolves with energy: the calculation says the interaction turns negative around 10^10-10^12 GeV, meaning our vacuum sits in a local minimum \u2014 a 'false vacuum' \u2014 with a deeper minimum elsewhere. Quantum tunneling could one day nucleate a bubble of true vacuum expanding at light speed, rewriting physics inside. The calculated lifetime exceeds the universe's age by absurd margins \u2014 but 'metastable' is not 'stable.'",
 "background": "The stability analysis matured after the 2012 Higgs discovery, when the measured 125 GeV mass plus the top mass (~173 GeV) let theorists run the Higgs quartic coupling to high energies (Degrassi et al. 2012; Buttazzo et al. 2013). The coupling crosses zero near 10^10-10^12 GeV \u2014 the instability scale \u2014 putting the Standard Model vacuum in the metastable region of parameter space, though within uncertainties of the stable region. The tunneling lifetime comes out around 10^100+ years, making decay utterly negligible in practice. But the near-criticality \u2014 the universe sitting almost exactly at the stability boundary \u2014 is itself a puzzle: it looks fine-tuned. Proposed explanations range from new physics stabilizing the vacuum (supersymmetry, extra scalars) to anthropic selection to the near-criticality being a hint of deeper principles. As of 2026 the metastability conclusion holds at current central values, with the top-quark mass uncertainty dominating.",
 "why_it_matters": "This is the ultimate existential physics question \u2014 is the ground beneath reality solid? Practically, the near-criticality is a clue: parameters sitting exactly at a stability boundary often signal a deeper principle (like self-organized criticality), and whatever explains it likely involves new physics at high scales.",
 "sig_pointer": "The Signature system's proposed approach treats near-criticality as the vacuum ledger balancing on a knife-edge by construction, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the vacuum's near-criticality is not an accident but a balancing condition: the universe's ledger sits at the stability boundary because the same dynamics that set the Higgs and top masses enforce the boundary \u2014 the parameters are correlated, not independent. "
  "Assumptions: (1) the Higgs mass, top mass, and strong coupling are not independent inputs but joint outcomes of a higher-scale dynamics; (2) that dynamics has an attractor near the stability boundary; (3) the tunneling lifetime's enormity is a consequence of the barrier shape, not a separate tuning. "
  "Reasoning path: the proposal treats 'sitting at the boundary' as data rather than coincidence \u2014 in the Signature reading, boundaries in parameter space are where ledgers balance, and physical parameters are drawn to them; the test is then whether the correlation between the masses is tighter than independent-input models allow. "
  "Proposed mechanism: a high-scale attractor (unspecified UV dynamics) that correlates the Higgs quartic, top Yukawa, and gauge couplings along the near-critical line. "
  "What would confirm it: future colliders measuring the Higgs self-coupling and top mass with precision that reveals the parameters tracking the stability boundary more tightly than chance allows \u2014 or discovery of the stabilizing new physics (extra scalar, supersymmetry) at the predicted scale. "
  "What would kill it: precision measurements moving the central values firmly into the stable region (making near-criticality a mirage of current uncertainties), or proof the parameters are truly independent. "
  "What this does not claim: it does not claim vacuum decay is a practical danger (the lifetime is ~10^100 years), does not identify the UV attractor, and does not claim metastability is established \u2014 the uncertainties still allow stability."),
 "sig_lens": "The Signature lens reads near-criticality as a ledger balancing on its boundary by construction, and asks what higher dynamics correlates the masses along that edge.",
 "how_it_works": "Theorists compute the renormalization-group running of the Higgs quartic coupling using the measured Higgs mass, top mass, and strong coupling, mapping the stability/metastability boundary in parameter space and the tunneling lifetime. Experimentalists shrink the dominant uncertainty \u2014 the top-quark mass \u2014 at the LHC and future colliders, and measure the Higgs self-coupling to test the potential's shape directly.",
 "key_points": [
  "Higgs 125 GeV + top ~173 GeV drive the quartic coupling negative near 10^10-10^12 GeV.",
  "Our vacuum appears metastable: a local minimum with a deeper one elsewhere.",
  "The tunneling lifetime is ~10^100+ years \u2014 no practical danger.",
  "Near-criticality (sitting at the stability boundary) may itself be the clue.",
  "Top-mass uncertainty dominates; central values could still allow stability.",
 ],
 "requirements": [
  "Precision top mass and Higgs self-coupling measurements (HL-LHC, future colliders).",
  "Either stabilizing new physics or an explanation of the near-criticality.",
  "A tunneling calculation robust against Planck-scale unknowns.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Degrassi G et al. Higgs mass and vacuum stability in the Standard Model at NNLO. Journal of High Energy Physics. 2012;08:098.",
  "Buttazzo D et al. Investigating the near-criticality of the Higgs boson. Journal of High Energy Physics. 2013;12:089.",
  "Espinosa JR. Implications of the top (and Higgs) mass for vacuum stability. PoS TOP2015:043.",
  "Particle Data Group. Review of Particle Physics. Physical Review D. 2024;110:030001 (Higgs and top sections).",
 ],
},
# ----------------------------------------------------------------- rank 23
{
 "key": "turbulence-problem",
 "name": "The Turbulence Problem",
 "group": "Classical Physics",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Turbulent flow \u2014 the chaotic swirling in rivers, air, and pipes \u2014 still lacks a complete predictive theory, and the underlying equations' basic behavior is a Millennium Prize problem.",
 "description": "The Navier-Stokes equations describe fluid flow, but in the turbulent regime their solutions become chaotic across scales, from whirlpools to eddies to microscopic swirls. Engineers use statistical models and supercomputer simulations, yet there is no general theory predicting turbulence from first principles \u2014 and mathematicians cannot even prove the equations always have smooth solutions in three dimensions (a Clay Millennium Prize).",
 "background": "Navier and Stokes formulated the equations in the 1820s-40s; Osborne Reynolds' 1883 experiments revealed the laminar-to-turbulent transition. Kolmogorov's 1941 theory predicted the famous -5/3 energy spectrum of the turbulent cascade \u2014 energy injected at large scales cascades to ever-smaller eddies until viscosity dissipates it \u2014 a triumph confirmed experimentally. But Kolmogorov's theory is statistical and incomplete: intermittency, the precise transition mechanism, and wall-bounded turbulence resist it. The Clay Institute's Millennium Prize asks whether 3D Navier-Stokes solutions always remain smooth \u2014 finite-time blowup would mean the equations themselves break down. Direct numerical simulation resolves all scales only at modest Reynolds numbers; real engineering flows rely on modeled approximations (RANS, LES). As of 2026 turbulence remains, in Feynman's phrase, the most important unsolved problem of classical physics.",
 "why_it_matters": "Turbulence governs aircraft drag, weather, climate, combustion, blood flow, and pipeline transport \u2014 a sizable fraction of global energy use fights it. A predictive theory would transform engineering design, climate modeling, and our basic understanding of chaos in continuous systems.",
 "sig_pointer": "The Signature system's proposed approach treats turbulence as the flow ledger's cascade hitting a scale where bookkeeping must change form, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that turbulence is what the flow ledger does when energy input exceeds what smooth bookkeeping can carry: the excess cascades to smaller scales not by accident but as the ledger's required overflow channel, with Kolmogorov's -5/3 spectrum as the ledger's fixed exchange rate between scales. "
  "Assumptions: (1) the cascade rate is set by the large-scale energy input, independent of viscosity (Kolmogorov's core insight, adopted as a ledger rule); (2) intermittency \u2014 the burstiness of dissipation \u2014 reflects the ledger occasionally bunching its transfers; (3) the laminar-turbulent transition is the point where smooth bookkeeping becomes impossible. "
  "Reasoning path: the proposal reads the universality of the -5/3 spectrum as evidence for a ledger-level law rather than a dynamical accident \u2014 whenever a conserved quantity must cross scales, the transfer organizes into the same cascade; the Signature addition is predicting that intermittency corrections follow from the statistics of ledger bunching, testable against high-Reynolds-number data. "
  "Proposed mechanism: scale-cascade as required overflow, with a multifractal ledger-bunching model for intermittency corrections to Kolmogorov scaling. "
  "What would confirm it: high-Reynolds-number experiments (e.g., Princeton superpipe, Gottingen tunnel) showing intermittency exponents matching the ledger-bunching prediction across different flows \u2014 pipes, boundary layers, and free shear \u2014 with no flow-specific tuning. "
  "What would kill it: intermittency proving flow-dependent in a way no universal ledger statistics can capture, or a first-principles derivation of turbulence statistics from Navier-Stokes that leaves no role for the ledger picture. "
  "What this does not claim: it does not claim to solve the Millennium regularity problem, does not derive the cascade from the equations, and does not predict transition in any specific geometry."),
 "sig_lens": "The Signature lens reads turbulence as the flow ledger's required overflow channel, and asks what fixed exchange rate \u2014 the -5/3 law \u2014 governs transfers between scales.",
 "how_it_works": "Experimentalists measure velocity statistics with hot-wire anemometry, particle image velocimetry, and laser Doppler in wind tunnels, pipes, and boundary layers at ever-higher Reynolds numbers. Computationalists run direct numerical simulations (resolving all scales) at moderate Re and large-eddy simulations for engineering. Theorists pursue statistical closures, dynamical-systems approaches to transition, and the Millennium regularity question.",
 "key_points": [
  "Navier-Stokes (1820s-40s) governs flow; turbulence is its chaotic multi-scale regime.",
  "Reynolds (1883) revealed the laminar-turbulent transition.",
  "Kolmogorov (1941) predicted the -5/3 cascade spectrum, experimentally confirmed.",
  "3D Navier-Stokes smoothness is a Clay Millennium Prize problem.",
  "Intermittency and the transition mechanism remain incompletely understood.",
 ],
 "requirements": [
  "A statistical theory predicting turbulence from first principles, including intermittency.",
  "Resolution of the Navier-Stokes existence/smoothness Millennium problem.",
  "A predictive theory of laminar-turbulent transition in real geometries.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kolmogorov AN. The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers. Doklady Akademii Nauk SSSR. 1941;30:299-303.",
  "Reynolds O. An experimental investigation of the circumstances which determine whether the motion of water shall be direct or sinuous. Philosophical Transactions of the Royal Society. 1883;174:935-982.",
  "Frisch U. Turbulence: The Legacy of A. N. Kolmogorov. Cambridge University Press; 1995.",
  "Fefferman CL. Existence and smoothness of the Navier-Stokes equation. Clay Mathematics Institute Millennium description; 2000.",
 ],
},
# ----------------------------------------------------------------- rank 24
{
 "key": "neutrino-mass",
 "name": "Neutrino Mass and Nature",
 "group": "Particle Physics",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Neutrinos have mass \u2014 the only confirmed crack in the Standard Model \u2014 but we do not know how much, how the masses order, or whether the neutrino is its own antiparticle.",
 "description": "The Standard Model predicted massless neutrinos; the 1998-2001 oscillation discoveries proved they morph between flavors, which requires mass. Oscillation experiments measure the mass-squared differences precisely \u2014 but not the absolute scale, not whether the ordering is 'normal' or 'inverted,' and not whether neutrinos are Dirac (distinct antiparticles) or Majorana (their own antiparticles). The mass mechanism is unknown.",
 "background": "Pauli proposed the neutrino in 1930; Reines and Cowan detected it in 1956 (Nobel 1995). Super-Kamiokande's 1998 atmospheric-neutrino result and SNO's 2001 solar-neutrino result proved oscillations (Nobel 2015). We now know: delta-m^2_21 = 7.5 x 10^-5 eV^2 and |delta-m^2_32| = 2.5 x 10^-3 eV^2, implying the heaviest neutrino weighs at least ~0.05 eV \u2014 a million times lighter than the electron. KATRIN's tritium-decay experiment bounds the absolute scale below 0.45 eV (2024-2025 analyses). The seesaw mechanism \u2014 heavy right-handed partners suppressing the light masses \u2014 is the leading theoretical idea and would elegantly enable leptogenesis (see the matter-antimatter record). Whether neutrinos are Majorana is tested by neutrinoless double-beta decay searches (KamLAND-Zen, GERDA/LEGEND, nEXO planned). As of 2026 the ordering, the absolute mass, and the Dirac/Majorana question are all open.",
 "why_it_matters": "Neutrino mass is the one laboratory-confirmed fact the Standard Model cannot accommodate \u2014 the guaranteed window into new physics. The seesaw mechanism ties it to the universe's matter surplus and to grand-unified scales; a Majorana discovery would reveal a new kind of matter and a new mass mechanism.",
 "sig_pointer": "The Signature system's proposed approach treats neutrino lightness as the mass ledger's suppressed entry via a heavy partner, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that neutrino masses are small because the mass ledger pairs each light neutrino with a heavy, unseen partner: the light mass is the suppressed remainder of a much larger scale \u2014 the seesaw \u2014 and the same heavy partners' decays wrote the universe's matter surplus. "
  "Assumptions: (1) right-handed neutrinos exist at a high scale (10^9-10^14 GeV); (2) the light masses follow the seesaw relation m_light ~ m_Dirac^2 / M_heavy; (3) the heavy partners decayed out of equilibrium in the early universe (leptogenesis). "
  "Reasoning path: the proposal treats the absurd lightness (a million times below the electron) as the signature of suppression rather than tuning \u2014 in the Signature reading, whenever a ledger entry is inexplicably small, look for the large entry it is the remainder of; the seesaw provides exactly that, and its heavy scale simultaneously supplies the out-of-equilibrium decays needed for the matter-antimatter asymmetry, unifying two records' solutions. "
  "Proposed mechanism: type-I seesaw with hierarchical heavy neutrinos, with leptogenesis as the cosmological consequence. "
  "What would confirm it: a neutrinoless double-beta decay signal establishing the Majorana nature (required by the simplest seesaw), plus a measured leptonic CP phase consistent with successful leptogenesis \u2014 two independent confirmations of the same heavy sector. "
  "What would kill it: proof that neutrinos are Dirac (no double-beta decay at any sensitivity, plus theoretical exclusion), which would force a completely different mass mechanism. "
  "What this does not claim: it does not claim the heavy scale is known (it spans orders of magnitude), does not claim leptogenesis is established, and does not predict the mass ordering \u2014 which experiments (JUNO, DUNE) will decide directly."),
 "sig_lens": "The Signature lens reads neutrino lightness as a suppressed remainder of a heavy partner scale, and asks what single heavy sector could explain both the tiny masses and the matter surplus.",
 "how_it_works": "Oscillation experiments (T2K, NOvA, JUNO, DUNE, Hyper-Kamiokande) pin down the mixing angles, mass ordering, and CP phase. KATRIN measures the tritium beta-decay endpoint for the absolute mass scale; cosmology bounds the sum of masses via structure formation. Neutrinoless double-beta decay searches (KamLAND-Zen, LEGEND, nEXO) test the Majorana nature \u2014 the key that unlocks the seesaw.",
 "key_points": [
  "Oscillations (1998/2001, Nobel 2015) prove neutrinos have mass: physics beyond the Standard Model.",
  "Mass-squared differences known; heaviest neutrino at least ~0.05 eV.",
  "KATRIN bounds the absolute scale below 0.45 eV.",
  "Ordering (normal vs inverted) and Dirac vs Majorana are open.",
  "The seesaw mechanism is the leading idea, linking mass to leptogenesis.",
 ],
 "requirements": [
  "The mass ordering (JUNO, DUNE, Hyper-Kamiokande).",
  "The absolute mass scale (KATRIN, cosmology).",
  "Dirac vs Majorana via neutrinoless double-beta decay.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fukuda Y et al. (Super-Kamiokande). Evidence for oscillation of atmospheric neutrinos. Physical Review Letters. 1998;81:1562-1567.",
  "Ahmad QR et al. (SNO). Measurement of the rate of nu_e + d -> p + p + e- interactions. Physical Review Letters. 2001;87:071301.",
  "Aker M et al. (KATRIN). Direct neutrino-mass measurement with sub-electronvolt sensitivity. Nature Physics. 2022;18:160-166.",
  "Minkowski P. mu -> e gamma at a rate of one out of 10^9 muon decays? Physics Letters B. 1977;67:421-428 (seesaw).",
 ],
},
# ----------------------------------------------------------------- rank 25
{
 "key": "hierarchy-problem",
 "name": "The Hierarchy Problem",
 "group": "Particle Physics",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "The Higgs boson's mass (125 GeV) sits 17 orders of magnitude below the Planck scale (10^19 GeV) \u2014 yet quantum corrections should drag it up. Why is the Higgs so light?",
 "description": "In quantum field theory, the Higgs mass receives corrections from every heavier scale, pulling it toward the highest scale in the theory \u2014 the Planck scale, 10^17 times larger. Keeping it at 125 GeV requires cancellations precise to about one part in 10^34, unless new physics intervenes. The LHC has found the Higgs but no sign of the expected intervening physics.",
 "background": "The hierarchy problem crystallized in the late 1970s as the Standard Model's triumph made its gaps visible. The leading solutions each predicted new phenomena near the TeV scale: supersymmetry (superpartners canceling the corrections), extra dimensions (ADD large extra dimensions; Randall-Sundrum warped geometry lowering the fundamental scale), and composite Higgs models (the Higgs as a bound state). The LHC's Runs 1-3 found the Higgs at 125 GeV and excluded the simplest versions of all these ideas \u2014 no superpartners, no extra-dimensional signatures, no compositeness \u2014 pushing viable models into more baroque territory or higher scales. Responses split: double down on subtler natural models, accept fine-tuning via anthropic/multiverse selection, or question whether naturalness was ever a reliable guide. As of 2026 the problem is as sharp as ever and its hoped-for experimental resolution has not arrived.",
 "why_it_matters": "The hierarchy problem is the flagship 'naturalness' puzzle: it asks why the universe's parameters look absurdly fine-tuned. Its resolution \u2014 new symmetry, new geometry, or a new philosophy of tuning \u2014 decides the direction of particle physics for decades and determines what future colliders should hunt.",
 "sig_pointer": "The Signature system's proposed approach treats the Higgs mass as protected by a ledger symmetry that only breaks softly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the Higgs mass is protected by a ledger symmetry: the quantum corrections do cancel, but the cancellation is enforced by a symmetry of the full ledger that is only softly broken \u2014 so the Higgs stays light not by accident but by a bookkeeping rule we have not yet identified. "
  "Assumptions: (1) the ultimate theory possesses a symmetry relating the Higgs sector's corrections; (2) the symmetry breaking that yields 125 GeV is soft, generating the weak scale without large corrections; (3) the symmetry's other signatures lie just beyond current LHC reach or in subtle precision observables. "
  "Reasoning path: the proposal keeps faith with naturalness but relocates it \u2014 instead of superpartners at the TeV scale, the protective symmetry might manifest as a 'neutral naturalness' sector (twin Higgs) with few LHC-visible states, or as a cosmological relaxation (the relaxion) that dynamically selected the small Higgs mass in the early universe; the Signature reading is that ledgers abhor unprotected large cancellations, so the protection exists \u2014 we are misjudging where it hides. "
  "Proposed mechanism: a softly broken protective symmetry (twin-Higgs-like or relaxion-like) that cancels the dominant corrections while evading current searches. "
  "What would confirm it: discovery of top partners with nonstandard quantum numbers, Higgs-coupling deviations at a future Higgs factory, or a relaxion-like cosmological signature \u2014 any protection mechanism made concrete. "
  "What would kill it: a future 100-TeV collider finding nothing new up to 30+ TeV while precision measurements confirm the Standard Model to ever-tighter accuracy \u2014 which would force the field toward anthropic or 'unnatural' resolutions. "
  "What this does not claim: it does not claim any specific model is correct, does not predict the new scale, and does not dismiss the possibility that naturalness was a false guide."),
 "sig_lens": "The Signature lens reads the light Higgs as a ledger protected by an unidentified bookkeeping rule, and asks where the protection hides given the LHC's null results.",
 "how_it_works": "The LHC hunts top partners, superpartners, and resonances directly, and measures Higgs couplings for deviations from Standard Model predictions (a Higgs factory would sharpen these a hundredfold). Theorists build natural models compatible with null results \u2014 neutral naturalness, relaxion, composite variants \u2014 and compute their signatures. Cosmologists test relaxion and anthropic scenarios against early-universe constraints.",
 "key_points": [
  "Higgs 125 GeV vs Planck 10^19 GeV: a 10^17 gap needing ~10^34 cancellation without new physics.",
  "SUSY, extra dimensions, and composite Higgs were the leading solutions; LHC excluded simple versions.",
  "Surviving ideas: neutral naturalness (twin Higgs), relaxion, subtler SUSY.",
  "Alternative: accept tuning via anthropic/multiverse selection.",
  "A future Higgs factory and 100-TeV collider would decide between protection and tuning.",
 ],
 "requirements": [
  "Discovery of the protective mechanism's signatures \u2014 or exclusion up to decisive scales.",
  "Higgs coupling measurements at the percent-to-permille level.",
  "A verdict on naturalness as a physical principle.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Weinberg S. Implications of dynamical symmetry breaking. Physical Review D. 1976;13:974-996.",
  "Susskind L. Dynamics of spontaneous symmetry breaking in the Weinberg-Salam theory. Physical Review D. 1979;20:2619-2625.",
  "'t Hooft G. Naturalness, chiral symmetry, and spontaneous chiral symmetry breaking. NATO ASI Series. 1980;59:135-157.",
  "Craig N. The state of supersymmetry after Run I of the LHC. arXiv:1309.0528; updated in Ann. Rev. Nucl. Part. Sci. 2015.",
 ],
},
# ----------------------------------------------------------------- rank 26
{
 "key": "cosmological-constant-problem",
 "name": "The Cosmological Constant Problem",
 "group": "Cosmology",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Quantum field theory predicts a vacuum energy 10^120 times larger than the observed dark energy density \u2014 the worst prediction in the history of physics. Why is the vacuum so light?",
 "description": "Every quantum field contributes zero-point energy to the vacuum; summing them to the Planck scale gives a vacuum density around 10^112 erg/cm^3, while the observed dark energy density is about 10^-8 erg/cm^3. The prediction overshoots by 120 orders of magnitude. Supersymmetry would cancel the contributions \u2014 but supersymmetry is broken, and no other cancellation is known.",
 "background": "The problem was framed sharply by Zel'dovich (1967-68), who connected vacuum energy to the cosmological constant, and elevated by Weinberg's 1989 review calling it the deepest problem in physics. The 1998 discovery that the cosmological constant is small but nonzero made it worse: now the vacuum energy must cancel to 120 decimal places but not quite completely. Proposed solutions span the spectrum: anthropic selection in a multiverse (Weinberg's 1987 bound correctly anticipated a small-but-nonzero value), dynamical adjustment mechanisms, unimodular gravity (where the constant is an integration constant, not a vacuum prediction), and sequestering scenarios. None is established; the anthropic argument remains the only one that 'predicted' the observed value, which many physicists find unsatisfying. As of 2026 the 120-order gap stands untouched.",
 "why_it_matters": "This is where quantum field theory \u2014 our most precise framework \u2014 fails most spectacularly. Any theory of quantum gravity must explain why the vacuum gravitates so weakly; the answer will likely reveal how spacetime and quantum fields actually relate, dissolving or solving the dark energy problem with it.",
 "sig_pointer": "The Signature system's proposed approach treats the 120-order gap as a ledger-cancellation enforced by a symmetry of the full accounting, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the vacuum energy cancels because the universe's ledger must: the zero-point entries of all fields sum against a geometric counter-entry, and the cancellation is enforced by a bookkeeping symmetry \u2014 with the tiny observed remainder as the symmetry's soft breaking. "
  "Assumptions: (1) the full ledger includes a gravitational counter-term for vacuum energy (in the spirit of sequestering/unimodular proposals); (2) the cancellation symmetry is exact in the UV and only softly broken at low energies; (3) the breaking scale is what we observe as dark energy. "
  "Reasoning path: the proposal treats 120 orders of magnitude not as a tuning but as evidence of a mechanism \u2014 no accident reaches 10^120; the Signature reading is that exact-seeming cancellations signal exact symmetries, so the task is to find the symmetry, not to explain the tuning; the small remainder is then the interesting physics, possibly connected to the same drift discussed in the dark energy record. "
  "Proposed mechanism: a sequestering-type mechanism in which vacuum energy is prevented from gravitating by a global constraint, with soft breaking generating the observed Lambda. "
  "What would confirm it: a concrete sequestering or unimodular formulation that is theoretically consistent, reproduces all gravitational tests, and predicts the remainder's scale or drift \u2014 or a laboratory/astrophysical signature of the cancellation mechanism. "
  "What would kill it: proof that no such global mechanism can be consistent with quantum gravity (e.g., swampland arguments against global symmetries extended to sequestering), leaving anthropic selection as the remaining explanation. "
  "What this does not claim: it does not claim to have the symmetry in hand, does not claim the anthropic explanation is wrong, and does not predict the remainder's value."),
 "sig_lens": "The Signature lens reads the 120-order cancellation as evidence of an exact bookkeeping symmetry, and asks what symmetry could forbid the vacuum from gravitating.",
 "how_it_works": "Theorists construct cancellation mechanisms \u2014 supersymmetry, sequestering, unimodular gravity, adjustment fields \u2014 and test them for consistency with general relativity's precision tests and quantum gravity conjectures (swampland). Cosmologists measure whether the remainder (dark energy) is truly constant, since a dynamical remainder favors dynamical mechanisms. The anthropic line is tested by whether multiverse measures can be made predictive.",
 "key_points": [
  "QFT predicts vacuum energy ~10^112 erg/cm^3; observed ~10^-8 erg/cm^3: a 10^120 gap.",
  "Weinberg (1989): the deepest problem; the small-but-nonzero value worsened it.",
  "Weinberg's 1987 anthropic bound anticipated the observed scale \u2014 the only 'successful prediction.'",
  "Candidate mechanisms: SUSY cancellation, sequestering, unimodular gravity, adjustment.",
  "No dynamical solution is established.",
 ],
 "requirements": [
  "A consistent mechanism canceling vacuum energy while leaving the observed remainder.",
  "Compatibility with quantum gravity (swampland) constraints.",
  "Either a dynamical prediction or a predictive multiverse measure.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Weinberg S. The cosmological constant problem. Reviews of Modern Physics. 1989;61:1-23.",
  "Weinberg S. Anthropic bound on the cosmological constant. Physical Review Letters. 1987;59:2607-2610.",
  "Zel'dovich YaB. The cosmological constant and the theory of elementary particles. Soviet Physics Uspekhi. 1968;11:381-393.",
  "Martin J. Everything you always wanted to know about the cosmological constant problem (but were afraid to ask). Comptes Rendus Physique. 2012;13:566-665.",
 ],
},
]

ENTRIES += [
# ----------------------------------------------------------------- rank 27
{
 "key": "horizon-flatness",
 "name": "The Horizon and Flatness Problems",
 "group": "Cosmology",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "The microwave background is uniform to one part in 100,000 across regions that could never have exchanged signals \u2014 and space is geometrically flat to better than 0.1 percent. Why is the universe so precisely balanced?",
 "description": "At recombination, the observable universe contained roughly 40,000 causally disconnected patches \u2014 regions too far apart for light to have traveled between them \u2014 yet they share the same temperature to 10^-5. Meanwhile the universe's spatial curvature is measured at |Omega_k| < 0.001, though any initial curvature should have grown enormously. Inflation \u2014 a burst of exponential expansion \u2014 explains both, but inflation itself is unconfirmed and its details unknown.",
 "background": "The horizon problem was sharpened by the discovery of the microwave background's isotropy (Penzias and Wilson 1965; COBE 1992 measured the 10^-5 uniformity). The flatness problem was framed by Dicke and Peebles: curvature grows with expansion, so near-flatness today demands absurdly precise initial flatness. Alan Guth's 1981 inflationary proposal \u2014 a brief exponential expansion stretching a tiny smooth patch across the observable universe \u2014 solved both at a stroke and predicted the nearly scale-invariant fluctuation spectrum that Planck later confirmed exquisitely. But inflation's driver (the inflaton) is unidentified, its energy scale unknown, and alternatives exist: bouncing cosmologies, ekpyrotic scenarios, varying-speed-of-light models. As of 2026 inflation is the leading paradigm with no direct confirmation \u2014 no primordial gravitational waves (B-mode polarization) detected, no inflaton found.",
 "why_it_matters": "These problems ask about the universe's initial conditions \u2014 the deepest 'why' in cosmology. Confirming inflation (or replacing it) would reveal physics at 10^16 GeV, far beyond any collider, and explain the origin of all cosmic structure from quantum fluctuations.",
 "sig_pointer": "The Signature system's proposed approach treats the uniformity as the ledger being written once before the pages separated, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the uniformity is primordial in the strongest sense: the observable universe's ledger was written as a single entry before expansion separated the pages \u2014 the 40,000 'disconnected' patches were never disconnected in the ledger's accounting, because the writing preceded the separation. "
  "Assumptions: (1) the pre-expansion state was a single causally connected domain; (2) a rapid expansion phase (inflation-like) then stretched it beyond causal contact; (3) the flatness follows because the same stretching irons out curvature. "
  "Reasoning path: the proposal accepts inflation's core logic but frames it as ledger mechanics \u2014 uniformity is cheap if the entries were written before the pages were torn apart; the Signature addition is a testable emphasis: the fluctuation spectrum's near-scale-invariance is then the 'handwriting' of the writing process, and any deviation from it encodes the writer's dynamics. "
  "Proposed mechanism: an inflation-like rapid expansion from a single connected domain, with the inflaton's potential shape imprinted on the primordial spectrum's tilt and running. "
  "What would confirm it: detection of primordial B-mode polarization (gravitational waves from inflation) pinning the energy scale, plus measured running of the spectral index matching a specific inflaton potential \u2014 the handwriting identified. "
  "What would kill it: B-mode searches (BICEP/Keck, Simons Observatory, LiteBIRD) ruling out all simple inflationary models while a bouncing or alternative cosmology reproduces the spectrum \u2014 which would keep the uniformity but change the writer. "
  "What this does not claim: it does not claim inflation is proven (it is not), does not identify the inflaton, and does not address the multiverse measure problems that eternal inflation raises."),
 "sig_lens": "The Signature lens reads cosmic uniformity as a single ledger entry written before the pages separated, and asks what handwriting \u2014 the fluctuation spectrum \u2014 identifies the writer.",
 "how_it_works": "Cosmologists measure the microwave background's temperature and polarization (Planck, ACT, SPT, Simons Observatory, LiteBIRD) to extract the fluctuation spectrum's tilt, running, and any primordial gravitational-wave B-modes. Theorists build inflationary and alternative models and test them against these spectra plus large-scale structure. The B-mode hunt is the decisive near-term experiment.",
 "key_points": [
  "The microwave background is uniform to 10^-5 across ~40,000 causally disconnected patches.",
  "Spatial curvature is bounded by |Omega_k| < 0.001 though it should grow with expansion.",
  "Guth's 1981 inflation explains both via rapid exponential expansion.",
  "Planck confirmed the predicted near-scale-invariant fluctuation spectrum.",
  "No inflaton identified; no primordial B-modes detected; alternatives (bounce, ekpyrotic) survive.",
 ],
 "requirements": [
  "Direct evidence for inflation: primordial B-mode polarization or the inflaton's identity.",
  "Ruling in or out the leading alternatives with the same data.",
  "A measure for eternal inflation's multiverse, if inflation is eternal.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Guth AH. Inflationary universe: a possible solution to the horizon and flatness problems. Physical Review D. 1981;23:347-356.",
  "Penzias AA, Wilson RW. A measurement of excess antenna temperature at 4080 Mc/s. Astrophysical Journal. 1965;142:419-421.",
  "Planck Collaboration. Planck 2018 results. X. Constraints on inflation. Astronomy & Astrophysics. 2020;641:A10.",
  "Dicke RH, Peebles PJE. The big bang cosmology \u2014 enigmas and nostrums. In General Relativity: An Einstein Centenary Survey. 1979.",
 ],
},
# ----------------------------------------------------------------- rank 28
{
 "key": "flavor-puzzle",
 "name": "The Flavor Puzzle",
 "group": "Particle Physics",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Matter comes in three generations with masses spanning five orders of magnitude \u2014 from the electron to the top quark \u2014 in a pattern no theory predicts. Why three, and why these masses?",
 "description": "The Standard Model's matter particles replicate three times: electron/muon/tau, up/charm/top, down/strange/bottom \u2014 same charges, wildly different masses. The top quark outweighs the electron by a factor of ~340,000. The mixing matrices (CKM for quarks, PMNS for neutrinos) that rotate between generations add more unexplained numbers. The Standard Model accommodates 19+ free parameters of flavor and explains none.",
 "background": "Rabi's quip on the muon's 1936 discovery \u2014 'Who ordered that?' \u2014 still stands. The three-generation structure was completed with the tau (1975, Perl), bottom (1977), and top (1995) discoveries; LEP's Z-boson width proved exactly three light neutrinos. The masses show striking hierarchies and the mixings show striking patterns (small quark mixing, large neutrino mixing), but every 'explanation' \u2014 Froggatt-Nielsen flavor symmetries, extra-dimensional geography, composite models \u2014 adds assumptions to fit the data retroactively. Koide's 1981 mass formula for charged leptons predicts the tau mass eerily well and is almost certainly numerology \u2014 a cautionary tale. As of 2026 no flavor theory makes a confirmed prediction; the pattern remains the Standard Model's largest unexplained dataset.",
 "why_it_matters": "Flavor parameters are most of the Standard Model's free parameters \u2014 explaining them would shrink 'input' into 'output' and likely reveal the organizing principle behind matter's replication. It is also where new physics may already be whispering: flavor anomalies (B-meson decay tensions) are watched as possible cracks.",
 "sig_pointer": "The Signature system's proposed approach treats the generations as harmonic overtones of a single matter ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the three generations are overtones: a single matter ledger vibrates at a fundamental mode (the first generation) and two higher harmonics, with the masses set by the overtone structure rather than by independent inputs. "
  "Assumptions: (1) generation number is a quantum number of an internal ledger oscillation; (2) the mass hierarchy follows the overtone spacing, distorted by the Higgs coupling's own structure; (3) the mixing matrices are the misalignment between the overtone basis and the interaction basis. "
  "Reasoning path: the proposal takes the replication itself as the clue \u2014 three copies differing mainly in mass suggests one underlying object with excited states; the Signature reading asks what 'instrument' is being played, with the top quark's heaviness as the highest clearly resolved overtone and the mass ratios as the spectrum to fit. "
  "Proposed mechanism: an unspecified internal dynamics generating exactly three overtones (the cutoff at three being the key prediction to explain), with masses from the overtone eigenvalues. "
  "What would confirm it: discovery of a fourth generation (falsifying 'exactly three' \u2014 a kill, not a confirmation) \u2014 rather, confirmation would be a flavor model deriving the mass ratios and mixings from an overtone structure with a successful new prediction, e.g., a precise relation between quark and lepton hierarchies. "
  "What would kill it: a fourth sequential generation discovered at colliders, or proof that the mass pattern is environmental/anthropic with no dynamical origin. "
  "What this does not claim: it does not claim to know the 'instrument,' does not derive the overtone spacing, and honestly notes that Koide-style numerology warns against pattern-fitting without mechanism \u2014 the proposal is a research direction, not an answer."),
 "sig_lens": "The Signature lens reads the three generations as overtones of one matter ledger, and asks what instrument plays exactly three notes.",
 "how_it_works": "Experimentalists measure masses, lifetimes, and mixing parameters ever more precisely (LHCb, Belle II for quark flavor; oscillation experiments for lepton flavor) and hunt flavor anomalies \u2014 deviations from Standard Model predictions in rare decays. Theorists build flavor-symmetry models and test them against the full parameter set; any model must survive the tight constraints from flavor-changing neutral currents.",
 "key_points": [
  "Three generations: same charges, masses spanning ~10^5 (electron to top).",
  "Top/electron mass ratio ~340,000; no theory predicts it.",
  "CKM (quark) mixing is small; PMNS (neutrino) mixing is large \u2014 unexplained contrast.",
  "LEP proved exactly three light neutrino generations.",
  "Koide's formula: eerily accurate lepton-mass numerology, almost certainly coincidence.",
 ],
 "requirements": [
  "A flavor theory predicting masses and mixings, not fitting them.",
  "Explaining why exactly three generations.",
  "Resolution of the B-physics flavor anomalies (real new physics or systematics).",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cabibbo N. Unitary symmetry and leptonic decays. Physical Review Letters. 1963;10:531-533.",
  "Kobayashi M, Maskawa T. CP-violation in the renormalizable theory of weak interaction. Progress of Theoretical Physics. 1973;49:652-657.",
  "Froggatt CD, Nielsen HB. Hierarchy of quark masses, Cabibbo angles and CP violation. Nuclear Physics B. 1979;147:277-298.",
  "Particle Data Group. Review of Particle Physics. Physical Review D. 2024;110:030001 (CKM/PMNS sections).",
 ],
},
# ----------------------------------------------------------------- rank 29
{
 "key": "quantum-gravity",
 "name": "Quantum Gravity",
 "group": "Quantum Gravity",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "General relativity and quantum mechanics \u2014 the two pillars of modern physics \u2014 are mutually incompatible. What is the quantum theory of gravity?",
 "description": "General relativity describes gravity as spacetime curvature: smooth, deterministic, geometric. Quantum mechanics describes everything else as probabilistic fields. Directly quantizing gravity fails \u2014 the theory is non-renormalizable, producing infinite answers. String theory, loop quantum gravity, asymptotic safety, and causal dynamical triangulations all propose answers; none is confirmed, and they disagree about the nature of space and time themselves.",
 "background": "The clash was clear by the 1960s: perturbative quantum GR generates uncontrollable infinities (proven non-renormalizable by 't Hooft and Veltman-era methods applied to gravity; Goroff and Sagnotti 1986 showed the two-loop divergence explicitly). String theory (1968 onward; Green-Schwarz 1984) replaces point particles with extended objects, yielding finite gravity plus extra dimensions. Loop quantum gravity (Ashtekar 1986; Rovelli-Smolin) quantizes geometry itself, predicting discrete area and volume spectra. Asymptotic safety (Weinberg 1979) proposes gravity is nonperturbatively renormalizable via a UV fixed point. Causal dynamical triangulations build spacetime from simplices numerically. Each program has real achievements \u2014 string theory's black hole microstate counting (Strominger-Vafa 1996), LQG's bounce cosmology, AdS/CFT's holographic dictionary \u2014 and none has experimental confirmation. The Planck scale (10^-35 m, 10^19 GeV) is 16 orders beyond the LHC. As of 2026 quantum gravity is a theoretical archipelago with no bridge to experiment.",
 "why_it_matters": "This is the unification problem: the final incompatibility in fundamental physics. Its solution decides what spacetime is \u2014 fundamental or emergent, continuous or discrete \u2014 and must resolve the singularity and information paradoxes as special cases. Every other record at this end of the ladder depends on it.",
 "sig_pointer": "The Signature system's proposed approach treats quantum gravity as the ledger theory from which spacetime bookkeeping emerges, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that quantum gravity is not the quantization of spacetime but the theory of the ledger from which spacetime emerges: geometry is the large-scale bookkeeping of underlying quantum informational entries, and quantizing GR directly fails because it quantizes the books instead of the business. "
  "Assumptions: (1) the fundamental degrees of freedom are quantum-informational, not geometric; (2) spacetime and its dynamics (Einstein's equations) emerge thermodynamically, in the spirit of Jacobson's 1995 derivation of GR from thermodynamics; (3) the Planck scale marks the ledger's grain, not a length to be probed directly. "
  "Reasoning path: the proposal takes the non-renormalizability of perturbative quantum GR as a hint rather than a technical obstacle \u2014 in the Signature reading, you cannot quantize the emergent books; the repeated appearance of holography and thermodynamics in gravity (black hole entropy, Jacobson, AdS/CFT) is then the ledger showing through, and the research program becomes deriving the Einstein equations from informational postulates rather than quantizing the metric. "
  "Proposed mechanism: emergent gravity from quantum informational degrees of freedom, with the Einstein equations as equations of state (Jacobson-style) and holography as the ledger's area-scaling. "
  "What would confirm it: a rigorous derivation of the full Einstein equations \u2014 with the correct Newton's constant \u2014 from stated informational postulates, or tabletop experiments (gravitationally induced entanglement, Bose et al./Marletto-Vedral proposals) proving gravity mediates quantum entanglement and must itself be quantum. "
  "What would kill it: a consistent, UV-complete quantization of the metric itself (e.g., asymptotic safety decisively confirmed with all predictions working), showing the books were the business after all. "
  "What this does not claim: it does not claim the emergence derivation exists in full (it does not), does not choose between string theory and loop gravity (both contain emergent hints), and does not claim the Planck grain is experimentally accessible."),
 "sig_lens": "The Signature lens reads quantum gravity as the theory of the ledger beneath spacetime, and asks what informational entries the geometric books are keeping.",
 "how_it_works": "Theorists develop the candidate frameworks \u2014 strings, loops, asymptotic safety, CDT \u2014 and hunt for shared predictions (holography, minimal length, modified dispersion). Experimentalists pursue the only reachable handles: gravitationally induced entanglement tests, precision tests of Lorentz invariance, cosmological imprints (B-modes, non-Gaussianity), and analog-gravity systems. The field advances mainly through theoretical consistency and thought experiments.",
 "key_points": [
  "Perturbative quantum GR is non-renormalizable: infinite answers at two loops and beyond.",
  "Candidates: string theory, loop quantum gravity, asymptotic safety, causal dynamical triangulations.",
  "The Planck scale (10^-35 m, 10^19 GeV) is 16 orders of magnitude beyond the LHC.",
  "Holography and black hole thermodynamics hint spacetime is emergent.",
  "No candidate has experimental confirmation.",
 ],
 "requirements": [
  "A UV-complete theory reducing to GR and quantum field theory where tested.",
  "An experimental handle: entanglement-via-gravity tests, cosmological imprints, or other.",
  "Derivation (not assumption) of spacetime's emergence, or proof of fundamental discreteness.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Goroff MH, Sagnotti A. The ultraviolet behavior of Einstein gravity. Nuclear Physics B. 1986;266:709-736.",
  "Rovelli C. Quantum Gravity. Cambridge University Press; 2004.",
  "Jacobson T. Thermodynamics of spacetime: the Einstein equation of state. Physical Review Letters. 1995;75:1260-1263.",
  "Strominger A, Vafa C. Microscopic origin of the Bekenstein-Hawking entropy. Physics Letters B. 1996;379:99-104.",
 ],
},
# ----------------------------------------------------------------- rank 30
{
 "key": "emergent-spacetime",
 "name": "Emergent Spacetime",
 "group": "Quantum Gravity",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Is spacetime fundamental, or does it emerge from something deeper \u2014 quantum entanglement, information, or a structure with no notion of 'place' at all?",
 "description": "Black hole entropy scales with area, not volume \u2014 as if the universe's information lives on surfaces. The AdS/CFT correspondence builds a gravitational spacetime from a nongravitational quantum theory on its boundary. Entropic-gravity proposals derive Newton's laws from thermodynamics. Together they suggest space and time are not the stage but the play \u2014 emergent from deeper quantum bookkeeping. But emergence of what, from what, remains unknown.",
 "background": "Bekenstein (1973) and Hawking (1975) found black hole entropy proportional to horizon area \u2014 the first hint that gravity counts surface degrees of freedom. 't Hooft and Susskind's holographic principle (1990s) elevated this to a principle. Maldacena's 1997 AdS/CFT correspondence made it concrete: a gravity theory in anti-de Sitter space is exactly equivalent to a conformal field theory on its boundary \u2014 spacetime geometry encoded in quantum entanglement (later sharpened by Ryu-Takayanagi: entanglement entropy equals minimal surface area). Jacobson (1995) derived Einstein's equations from thermodynamics; Verlinde (2010) proposed gravity as an entropic force. Tensor-network (MERA) models build spatial geometry from entanglement structure explicitly. As of 2026 the evidence for emergence is circumstantial but convergent; the underlying 'atoms' of spacetime are unidentified and the emergence of time itself (not just space) is barely understood.",
 "why_it_matters": "If spacetime emerges, then 'where' and 'when' are not fundamental \u2014 locality, causality, and the whole stage of physics are collective phenomena. That reframes every question about singularities, the Big Bang, and quantum gravity: they become questions about the underlying entries, not the emergent books.",
 "sig_pointer": "The Signature system's proposed approach treats spacetime as the large-scale shape of the universe's entanglement ledger, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that spacetime is the shape of the entanglement ledger: regions of space are patterns of quantum entanglement, distances measure entanglement structure, and Einstein's equations describe how the ledger updates \u2014 geometry is what entanglement looks like from the inside. "
  "Assumptions: (1) the holographic principle holds generally, not just in AdS/CFT; (2) entanglement entropy's area law is the microscopic origin of geometric area; (3) dynamics (Einstein's equations) follow from the ledger's update rules, in Jacobson's thermodynamic spirit. "
  "Reasoning path: the proposal takes Ryu-Takayanagi literally as a definition \u2014 area IS entanglement entropy \u2014 and runs it backward: build the entanglement pattern, and geometry follows; the Signature addition is the prediction that spacetime defects (singularities, horizons) correspond to specific entanglement-ledger pathologies (discontinuities, maximal mixing), making the dictionary testable in principle via the pattern of quantum corrections to geometry. "
  "Proposed mechanism: entanglement-to-geometry mapping (tensor-network/MERA-like), with Einstein's equations as the ledger's equations of state. "
  "What would confirm it: deriving the Einstein equations with matter from entanglement postulates in a general setting (beyond AdS/CFT's specific duality), or observing the predicted pattern of quantum corrections to geometry near horizons. "
  "What would kill it: proof that entanglement cannot account for the full dynamical content of GR (e.g., a no-go theorem), or a confirmed fundamentally geometric quantum gravity (discrete spacetime atoms with no entanglement origin). "
  "What this does not claim: it does not claim the emergence of time is understood (it is the hardest part), does not identify the fundamental entries, and does not claim AdS/CFT describes our de Sitter-like universe."),
 "sig_lens": "The Signature lens reads spacetime as the shape of the entanglement ledger \u2014 area as entanglement, geometry as its pattern \u2014 and asks what ledger pathology a singularity is.",
 "how_it_works": "Theorists develop holographic dualities, tensor-network models of geometry, and thermodynamic derivations of the Einstein equations, testing how much of GR can be recovered from informational postulates. Quantum information theorists study entanglement structure in many-body systems as toy ledgers. Experimental handles are scarce: analog systems, cosmological imprints, and thought experiments carry most of the weight.",
 "key_points": [
  "Black hole entropy scales with area, not volume (Bekenstein 1973; Hawking 1975).",
  "AdS/CFT (1997): a gravitational spacetime equals a boundary quantum theory.",
  "Ryu-Takayanagi: entanglement entropy equals minimal surface area.",
  "Jacobson (1995) derived Einstein's equations from thermodynamics.",
  "The emergence of time is far less understood than the emergence of space.",
 ],
 "requirements": [
  "Identifying the fundamental 'entries' from which spacetime emerges.",
  "Deriving full GR dynamics (not just kinematics) from informational postulates.",
  "Understanding the emergence of time and causality.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bekenstein JD. Black holes and entropy. Physical Review D. 1973;7:2333-2346.",
  "Maldacena JM. The large N limit of superconformal field theories and supergravity. Advances in Theoretical and Mathematical Physics. 1998;2:231-252.",
  "Ryu S, Takayanagi T. Holographic derivation of entanglement entropy from the anti-de Sitter space/conformal field theory correspondence. Physical Review Letters. 2006;96:181602.",
  "Jacobson T. Thermodynamics of spacetime: the Einstein equation of state. Physical Review Letters. 1995;75:1260-1263.",
 ],
},
# ----------------------------------------------------------------- rank 31
{
 "key": "closed-timelike-curves",
 "name": "Closed Timelike Curves",
 "group": "Relativity",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "General relativity permits solutions containing paths that loop back in time \u2014 does physics actually allow time travel to the past, or does something forbid it?",
 "description": "Einstein's equations admit spacetimes with closed timelike curves (CTCs): worldlines that return to their own past. G\u00f6del found one in 1949; traversable wormholes and near-light-speed cylinders generate more. If CTCs exist, the grandfather paradox looms \u2014 yet the Novikov self-consistency principle and Hawking's chronology protection conjecture offer escape routes. No CTC has ever been observed, and quantum gravity may forbid them.",
 "background": "Kurt G\u00f6del's 1949 rotating-universe solution stunned Einstein by containing CTCs. Tipler's 1974 infinite rotating cylinder and Morris and Thorne's 1988 traversable wormholes showed CTCs arising from seemingly physical setups \u2014 though all require exotic matter (negative energy density) or unphysical infinities. Novikov's self-consistency principle (1980s) argued paradoxes resolve themselves: only consistent histories occur. Hawking's 1992 chronology protection conjecture proposed that quantum effects destroy any CTC before it forms \u2014 'the laws of physics conspire to prevent time travel.' Quantum treatments (Deutsch's CTC model, Lloyd's postselected teleportation) give contradictory answers about what quantum mechanics would do with a time loop. As of 2026 the question is open: GR says maybe, quantum field theory in curved spacetime leans no, quantum gravity is silent.",
 "why_it_matters": "CTCs test the logical consistency of physics itself: causality is the scaffolding of science \u2014 explanation, prediction, and experiment all assume effects follow causes. Whether the universe permits its own history to be edited decides if causality is a law or an accident of our epoch's spacetime.",
 "sig_pointer": "The Signature system's proposed approach treats CTCs as ledger loops the universe's bookkeeping refuses to close, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that closed timelike curves are forbidden by ledger consistency: a CTC would require the universe's ledger to contain its own future entries as inputs, and the bookkeeping admits no consistent assignment \u2014 chronology protection is not a dynamical conspiracy but a logical property of write-once ledgers. "
  "Assumptions: (1) the universe's ledger is written once, in a globally consistent order; (2) quantum fields on CTC backgrounds develop divergences (the standard QFT-in-curved-spacetime result) because the ledger cannot assign consistent values around the loop; (3) any would-be time machine's required exotic matter is the ledger's way of pricing the impossible. "
  "Reasoning path: the proposal sides with Hawking's chronology protection but grounds it structurally \u2014 the stress-energy divergences found by Hawking and others are read as the ledger refusing the loop, not as a separate physical mechanism; the Novikov principle is then the special case where the loop is almost closable and consistency trims the possibilities. "
  "Proposed mechanism: no new mechanism \u2014 the proposal is that write-once ledger consistency plus standard semiclassical backreaction already forbids CTC formation, and quantum gravity will make the prohibition exact. "
  "What would confirm it: a general proof that semiclassical backreaction always diverges on CTC-forming spacetimes, or a quantum gravity derivation showing CTCs are absent from the physical state space. "
  "What would kill it: a consistent quantum gravity solution containing a traversable CTC, or (most decisively) an observed CTC \u2014 which would overturn the proposal completely. "
  "What this does not claim: it does not claim the semiclassical divergence proof exists in full generality (it does not), does not resolve the Deutsch vs. Lloyd dispute about quantum computation with CTCs, and does not claim time travel is logically impossible \u2014 only that this universe's bookkeeping forbids it."),
 "sig_lens": "The Signature lens reads time travel as a ledger loop the write-once bookkeeping cannot close, and asks what divergence \u2014 the ledger's refusal \u2014 guards each would-be time machine.",
 "how_it_works": "Relativists construct CTC spacetimes and test their matter requirements (invariably exotic) and stability. Quantum field theorists compute stress-energy on CTC backgrounds, finding the divergences behind chronology protection. Quantum information theorists study what computation with CTCs would imply (Deutsch's model gives PSPACE power). The work is theoretical; observation offers no examples to study.",
 "key_points": [
  "G\u00f6del (1949) found the first CTC-containing solution of Einstein's equations.",
  "Wormholes (Morris-Thorne 1988) and Tipler cylinders (1974) generate CTCs with exotic matter.",
  "Novikov self-consistency vs. Hawking chronology protection (1992): the two escape routes.",
  "Quantum models of CTCs (Deutsch, Lloyd) disagree on the consequences.",
  "No CTC has ever been observed; all constructions require unphysical ingredients.",
 ],
 "requirements": [
  "A verdict from quantum gravity: are CTCs in the physical state space?",
  "A general proof (or refutation) of chronology protection in semiclassical gravity.",
  "Either an observed CTC or a no-go theorem with the force of a law.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "G\u00f6del K. An example of a new type of cosmological solutions of Einstein's field equations of gravitation. Reviews of Modern Physics. 1949;21:447-450.",
  "Morris MS, Thorne KS. Wormholes in spacetime and their use for interstellar travel. American Journal of Physics. 1988;56:395-412.",
  "Hawking SW. Chronology protection conjecture. Physical Review D. 1992;46:603-611.",
  "Friedman J et al. Cauchy problem in spacetimes with closed timelike curves. Physical Review D. 1990;42:1915-1930.",
 ],
},
# ----------------------------------------------------------------- rank 32
{
 "key": "fine-tuning",
 "name": "The Fine-Tuning of Constants",
 "group": "Cosmology",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "The constants of nature \u2014 masses, couplings, the cosmological constant \u2014 sit in narrow ranges permitting complex chemistry and life. Is this a clue, a selection effect, or a coincidence?",
 "description": "Small changes in the fundamental constants would unmake the universe's complexity: shift the Hoyle resonance slightly and stars make no carbon; tweak the quark masses and there are no stable atoms; raise the cosmological constant and no galaxies form. The observed values look fine-tuned for structure and life. Explanations on offer: a multiverse with anthropic selection, a deeper theory fixing the values, or brute coincidence \u2014 and the multiverse itself may be untestable.",
 "background": "Fred Hoyle's 1954 prediction of the 7.65 MeV carbon-12 resonance \u2014 required for stars to forge carbon, found experimentally soon after \u2014 is the classic fine-tuning exhibit. Brandon Carter formalized anthropic reasoning in 1974; Weinberg's 1987 anthropic bound on the cosmological constant gave the program its only quantitative success. String theory's landscape (circa 2003) and eternal inflation supplied a concrete multiverse to select from \u2014 but the measure problem (how to count universes) has resisted solution, leaving anthropic 'predictions' disputed. Critics argue fine-tuning claims are often overstated: some studies find stars and chemistry persist across wider parameter ranges than claimed, and 'life-permitting' is not the same as 'structure-permitting.' As of 2026 the fine-tuning debate is as much philosophy as physics, with the multiverse neither confirmed nor refuted.",
 "why_it_matters": "This is the 'why these laws' question \u2014 the boundary between physics and metaphysics. If the values are environmentally selected, physics' job description changes: some 'constants' are local accidents. If they are fixed by deeper theory, the fine-tuning is a clue pointing at it. Getting this right decides what counts as an explanation.",
 "sig_pointer": "The Signature system's proposed approach treats apparent fine-tuning as the ledger's structural requirements for complex entries, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that much apparent fine-tuning is structural, not tunable: the constants are not independent dials but interlocked ledger entries, and the 'narrow range' is the range where the interlocking holds \u2014 change one entry and the books rebalance the others. "
  "Assumptions: (1) the fundamental parameters are not independent \u2014 a UV theory correlates them; (2) the correlations are tightest exactly where complex structure is possible, because structure requires the interlocking to be consistent; (3) genuinely independent tunings (like the cosmological constant) are fewer than they appear. "
  "Reasoning path: the proposal questions the premise \u2014 fine-tuning arguments typically vary one constant while holding the rest fixed, but if the ledger interlocks them, the single-dial analysis overstates the tuning; the Signature program is then to find the interlocks (relations between masses, couplings, and the vacuum) rather than to explain each value separately. "
  "Proposed mechanism: UV correlations between parameters (in the spirit of grand unification relating couplings, extended to masses and the vacuum energy), making the viable region a correlated surface rather than a tiny hypercube. "
  "What would confirm it: discovery of precise relations between seemingly independent constants \u2014 the Koide formula made respectable, so to speak \u2014 or a UV theory deriving multiple parameters from fewer inputs with the life-permitting region emerging naturally. "
  "What would kill it: proof that the parameters are truly independent (e.g., a landscape where they scan independently and we inhabit a rare viable patch), vindicating the multiverse reading. "
  "What this does not claim: it does not claim the interlocks are known (they are not), does not dismiss the cosmological constant's tuning problem (the hardest case), and does not claim anthropic reasoning is never valid \u2014 only that single-dial tuning arguments assume the independence they need to prove."),
 "sig_lens": "The Signature lens reads fine-tuning as interlocked ledger entries rather than independent dials, and asks which correlations would make the 'narrow range' a structural necessity.",
 "how_it_works": "Physicists vary constants in stellar-evolution and nuclear-reaction codes to map which ranges permit stars, carbon, and chemistry; study the string landscape and eternal inflation's measure problem; and hunt for UV theories (GUTs, strings) that reduce the parameter count. Philosophers of physics formalize what counts as an explanation versus a selection effect.",
 "key_points": [
  "Hoyle's 1954 prediction of the 7.65 MeV carbon resonance: the classic fine-tuning exhibit.",
  "Small shifts in quark masses, couplings, or Lambda would remove stars, atoms, or galaxies.",
  "Weinberg's 1987 anthropic bound is the program's one quantitative success.",
  "The string landscape + eternal inflation supply a multiverse; the measure problem blocks predictions.",
  "Critics note single-constant variation may overstate the tuning.",
 ],
 "requirements": [
  "A UV theory reducing the parameter count \u2014 or a predictive multiverse measure.",
  "Honest mapping of the truly viable parameter region (multi-parameter variation).",
  "Deciding whether 'fine-tuned for life' differs from 'fine-tuned for structure.'",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hoyle F. On nuclear reactions occurring in very hot stars. I. Astrophysical Journal Supplement. 1954;1:121-146.",
  "Carter B. Large number coincidences and the anthropic principle in cosmology. In Confrontation of Cosmological Theories with Observational Data (IAU Symp. 63). 1974.",
  "Weinberg S. Anthropic bound on the cosmological constant. Physical Review Letters. 1987;59:2607-2610.",
  "Barnes LA. The fine-tuning of the universe for intelligent life. Publications of the Astronomical Society of Australia. 2012;29:529-564.",
 ],
},
# ----------------------------------------------------------------- rank 33
{
 "key": "cosmic-magnetic-fields",
 "name": "The Origin of Cosmic Magnetic Fields",
 "group": "Astrophysics",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Galaxies and clusters are threaded by microgauss magnetic fields coherent over vast scales \u2014 but no one knows where the original seed fields came from.",
 "description": "Magnetic fields of a few microgauss organize spiral galaxies' arms, shape galaxy clusters, and may even thread the voids between them. Galactic dynamos can amplify weak seeds into microgauss strengths \u2014 but the seeds themselves, perhaps a billion-billion times weaker, need an origin: astrophysical batteries in the first stars and galaxies, or primordial fields from inflation or early-universe phase transitions. The seed problem is unsolved.",
 "background": "Cosmic magnetism was established by radio synchrotron emission and Faraday rotation measures through the 20th century. The dynamo theory \u2014 turbulent, rotating plasmas amplifying seed fields exponentially \u2014 explains galactic microgauss fields given enough time and a seed around 10^-20 gauss. But observed fields in young galaxies (high-redshift) and the lower bounds on intergalactic void fields from blazar gamma-ray spectra (Neronov and Vovk 2010: fields above ~10^-16 gauss in voids) strain purely astrophysical seeding: voids should be pristine, yet they seem magnetized. Primordial candidates \u2014 inflationary magnetogenesis, electroweak or QCD phase-transition fields \u2014 each face theoretical hurdles (strong coupling, backreaction, or insufficient strength). The cosmic microwave background bounds primordial fields but does not exclude them. As of 2026 neither astrophysical nor primordial seeding is established, and the void fields are the sharpest clue.",
 "why_it_matters": "Magnetic fields shape how galaxies form, how cosmic rays travel, and how the intergalactic medium behaves \u2014 they are a major dynamical player we cannot yet source. A primordial origin would make them fossils of the universe's first moments, carrying information about inflation or phase transitions no other probe preserves.",
 "sig_pointer": "The Signature system's proposed approach treats seed fields as the magnetic ledger's primordial entries amplified by structure formation, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the seeds are primordial ledger entries: a tiny magnetic field was written into the universe's initial conditions \u2014 during inflation or a phase transition \u2014 and every later dynamo merely amplified the books, never created them. "
  "Assumptions: (1) a primordial seed of at least ~10^-20 gauss was generated in the early universe; (2) galactic and cluster dynamos amplified it by the ~30 e-folds needed to reach microgauss; (3) the void fields are the least-processed surviving entries, closest to the primordial value. "
  "Reasoning path: the proposal takes the void-field lower bounds as decisive \u2014 voids cannot run astrophysical batteries, so magnetized voids mean primordial seeds; the Signature reading then treats the seed amplitude and spectrum as a fossil record of its generation epoch, with inflationary seeds predicting near-scale-invariant spectra and phase-transition seeds predicting peaked spectra. "
  "Proposed mechanism: inflationary or phase-transition magnetogenesis writing the seed entries, followed by standard turbulent dynamo amplification during structure formation. "
  "What would confirm it: measurement of the intergalactic field's power spectrum (via next-generation gamma-ray and radio observations) matching a primordial template \u2014 scale-invariant for inflation, peaked for phase transitions \u2014 plus CMB bounds consistent with that template. "
  "What would kill it: void fields proven to be zero (the blazar bounds overturned by plasma-instability effects), which would reopen purely astrophysical seeding \u2014 or a demonstrated astrophysical mechanism seeding even the voids. "
  "What this does not claim: it does not claim to know the generation mechanism (inflation vs phase transition is open), does not predict the seed amplitude from first principles, and does not claim dynamo theory's details are settled."),
 "sig_lens": "The Signature lens reads cosmic magnetism as primordial ledger entries amplified by structure, and asks what fossil spectrum the voids preserve of the first writing.",
 "how_it_works": "Radio astronomers map galactic and cluster fields with synchrotron emission and Faraday rotation; gamma-ray astronomers bound void fields via blazar spectra (pair-cascade deficits imply intervening fields); CMB experiments bound primordial fields via their effects on the plasma. Theorists model inflationary and phase-transition magnetogenesis and galactic dynamo amplification, testing each against the field strengths, coherence scales, and spectra observed.",
 "key_points": [
  "Galaxies and clusters host microgauss fields coherent over kiloparsecs.",
  "Dynamos amplify seeds (~10^-20 G) by ~30 e-folds \u2014 but need the seeds.",
  "Blazar gamma-ray bounds suggest even intergalactic voids are magnetized (>~10^-16 G).",
  "Primordial candidates: inflationary magnetogenesis, electroweak/QCD phase transitions.",
  "CMB observations bound but do not exclude primordial fields.",
 ],
 "requirements": [
  "The intergalactic field's strength and power spectrum (next-generation gamma-ray/radio).",
  "A magnetogenesis mechanism that works without theoretical pathologies.",
  "Reconciling high-redshift galactic fields with dynamo timescales.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Neronov A, Vovk I. Evidence for strong extragalactic magnetic fields from Fermi observations of TeV blazars. Science. 2010;328:73-75.",
  "Durrer R, Neronov A. Cosmological magnetic fields: their generation, evolution and observation. Astronomy & Astrophysics Review. 2013;21:62.",
  "Widrow LM. Origin of galactic and extragalactic magnetic fields. Reviews of Modern Physics. 2002;74:775-823.",
  "Subramanian K. The origin, evolution and signatures of primordial magnetic fields. Reports on Progress in Physics. 2016;79:076901.",
 ],
},
# ----------------------------------------------------------------- rank 34
{
 "key": "theory-of-everything",
 "name": "The Theory of Everything",
 "group": "Quantum Gravity",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Is there a single framework from which all of physics \u2014 every force, every particle, spacetime itself \u2014 follows? And if so, what is it?",
 "description": "Physics has unified before: electricity and magnetism (Maxwell), the electromagnetic and weak forces (Glashow-Weinberg-Salam, Nobel 1979). The dream is the final unification \u2014 gravity with the quantum forces, all particles as aspects of one structure, the constants derived rather than measured. String theory is the most developed candidate; loop quantum gravity, asymptotically safe gravity, and others compete. No candidate is confirmed, and they may not even be the right kind of answer.",
 "background": "Einstein spent his last decades on unified field theory without success. The Standard Model's SU(3)xSU(2)xU(1) structure begged for grand unification: Georgi and Glashow's SU(5) (1974) predicted proton decay, which experiments (Super-Kamiokande: lifetime > 10^34 years) have not seen, ruling out the simplest GUTs. String theory (Green-Schwarz 1984; the 1995 M-theory revolution) remains the only framework naturally containing gravity plus gauge forces, but its landscape of ~10^500 vacua and lack of testable predictions trouble critics. The couplings' near-miss unification at ~10^16 GeV (without supersymmetry they miss; with it, they meet) is either a clue or a coincidence. As of 2026 the theory of everything is an aspiration with candidates, not a result \u2014 and some physicists question whether final unification is a well-posed goal.",
 "why_it_matters": "A theory of everything would be the complete fundamental law \u2014 the answer to 'what is the world made of and why these rules.' Even the failed attempts pay off: the search produced the Standard Model, the Higgs mechanism, and modern cosmology. And the question disciplines the field: every partial theory must fit inside whatever the final answer is.",
 "sig_pointer": "The Signature system's proposed approach treats unification as the discovery that all ledgers are one ledger kept at the deepest level, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the theory of everything is the theory of the single deepest ledger: the apparently separate books \u2014 gauge forces, matter generations, spacetime \u2014 are views of one underlying accounting, and unification is the discovery of the entries from which all the separate ledgers derive. "
  "Assumptions: (1) the Standard Model's gauge structure plus gravity emerge from one underlying structure; (2) the 19+ free parameters are not fundamental but derived; (3) the correct theory is unique or nearly so \u2014 the landscape's 10^500 vacua reflect our ignorance of the selection principle, not the final answer. "
  "Reasoning path: the proposal takes the historical pattern of unification as its guide \u2014 each past unification revealed the previous 'separate' phenomena as one ledger (Maxwell, electroweak) \u2014 and extrapolates: the remaining separations (gravity vs gauge forces, the three generations, the constants) are the current ledger boundaries, and the theory of everything is whatever dissolves them; the Signature criterion for progress is parameter reduction, not mathematical elegance alone. "
  "Proposed mechanism: no specific mechanism proposed \u2014 the proposal is meta-theoretical: judge candidate theories by derived parameters and testable predictions, with string theory currently the only candidate containing gravity, but the verdict reserved for experiment. "
  "What would confirm it: a theory deriving the Standard Model's gauge group, three generations, and parameter values \u2014 plus gravity \u2014 with at least one confirmed novel prediction (proton decay at an observed rate, superpartners, extra dimensions, or something unanticipated). "
  "What would kill it: proof that no such unification exists \u2014 e.g., the parameters proven environmentally selected across a multiverse, making 'why these values' unanswerable in principle. "
  "What this does not claim: it does not claim string theory is correct (unconfirmed), does not claim unification is achievable or even well-posed, and \u2014 in full honesty \u2014 notes that the theory of everything may be the one problem on this list that outlives us all; the proposal is a stance on how to pursue it, not a solution."),
 "sig_lens": "The Signature lens reads unification as the discovery of the single deepest ledger, and asks what parameter reduction \u2014 not elegance \u2014 would prove the separate books are one.",
 "how_it_works": "Theorists develop candidate frameworks and extract predictions: proton decay rates (GUTs), superpartner spectra (SUSY), string resonances or extra dimensions (strings), area spectra (loops). Experimentalists push proton-decay limits (Super-Kamiokande, DUNE, Hyper-Kamiokande), hunt for new particles at colliders, and test coupling unification through precision measurements. The work spans the highest energies and the deepest mathematics.",
 "key_points": [
  "Past unifications: electromagnetism (Maxwell); electroweak (Nobel 1979).",
  "Simplest grand unified theories ruled out by proton-decay limits (>10^34 years).",
  "String theory uniquely contains gravity but has ~10^500 vacua and no confirmed predictions.",
  "Gauge couplings nearly unify at ~10^16 GeV \u2014 with supersymmetry, they meet.",
  "Whether final unification is well-posed is itself debated.",
 ],
 "requirements": [
  "A framework deriving the Standard Model + gravity with fewer free parameters.",
  "At least one confirmed novel prediction distinguishing it from rivals.",
  "Either a selection principle for the vacuum or proof the parameters are environmental.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Georgi H, Glashow SL. Unity of all elementary-particle forces. Physical Review Letters. 1974;32:438-441.",
  "Green MB, Schwarz JH. Anomaly cancellation in supersymmetric D=10 gauge theory and superstring theory. Physics Letters B. 1984;149:117-122.",
  "Witten E. String theory dynamics in various dimensions. Nuclear Physics B. 1995;443:85-126.",
  "Ade PA et al. (Planck). Planck 2015 results. XIII. Cosmological parameters. Astronomy & Astrophysics. 2016;594:A13 (coupling constraints context).",
 ],
},
]
