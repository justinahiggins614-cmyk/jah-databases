#!/usr/bin/env python3
"""Entries for The Unsolved Surgery Database (unsolved-surgery) and its
Signature half (unsolved-surgery-signature).

34 famous unsolved problems in surgery, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never medical advice,
never a treatment recommendation, no dosages, no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "medical advice.")

STD_COMMON = [
    "Problem statements verified against the published surgical literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never medical advice, never a treatment recommendation; no dosages and no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "ssi-prevention",
 "name": "Preventing Surgical Site Infections",
 "group": "Perioperative Care",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Why do surgical site infections still occur in 2 to 5 percent of inpatient operations despite antibiotics, sterile technique, and checklists - and how can they be driven toward zero?",
 "description": "A surgical site infection (SSI) is an infection at or near the incision within 30 days of surgery (or a year with an implant). The CDC estimates hundreds of thousands occur annually in the United States alone, adding roughly a week to hospital stays and billions in costs. Because most SSIs arise from the patient's own skin flora contaminating the wound, they persist even where technique is excellent, and no single preventive measure has eliminated them.",
 "background": "Joseph Lister's 1867 antisepsis papers and the later aseptic technique of von Bergmann and Schimmelbusch cut operative mortality dramatically, but SSIs never vanished. The CDC's 1999 guideline (Mangram et al.) and its 2017 update (Berrios-Torres et al., JAMA Surgery) codified bundles: timely prophylactic antibiotics, chlorhexidine-alcohol skin prep, normothermia, glycemic control, and oxygenation. The WHO issued global SSI prevention guidelines in 2016, updated in 2018. Randomized trials keep showing bundle components help, yet SSI rates plateau around 2-5% for inpatient surgery, and surveillance definitions keep shifting, which muddies comparisons. As of 2026 the residual infection rate resists every bundle.",
 "why_it_matters": "SSIs are among the most common and costly healthcare-associated infections: they prolong suffering, drive antibiotic resistance through treatment courses, and kill. Eliminating the residual rate would save thousands of lives and billions of dollars yearly, and the lessons would transfer to every invasive procedure in medicine.",
 "sig_pointer": "The Signature system's proposed approach treats the residual SSI rate as a colonization-timing problem rather than a sterility problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that residual SSIs persist because prevention targets the moment of incision while colonization is an hours-long race. "
  "Assumptions: (1) the decisive variable is not whether bacteria reach the wound but whether they reach it before the host's local defenses organize; (2) skin flora recolonize the prep zone within hours; (3) tissue oxygenation and temperature set the speed of the host side of the race. "
  "Reasoning path: bundles are scored as checklists, but the biology is a kinetic competition; the proposal reframes each bundle element by which side of the race it accelerates or delays, predicting that synchronized timing matters more than any single element. "
  "Proposed mechanism: a perioperative 'race window' model in which antibiotic tissue levels, skin recolonization curves, and neutrophil arrival times are co-optimized so the host always wins the first six hours. "
  "What would confirm it: trials showing that re-timing the same bundle components (rather than adding new ones) moves the SSI rate, with effect sizes tracking the model's predicted window. "
  "What would kill it: randomized data showing timing variations change nothing, or evidence that most residual SSIs come from hematogenous seeding rather than wound colonization. "
  "What this does not claim: it does not claim a protocol ready for patients, does not claim antibiotics can be reduced, and does not constitute medical advice - it is a research hypothesis about mechanism."),
 "sig_lens": "The Signature lens reads the stubborn SSI rate as a lost race between colonizing flora and organizing host defenses, and asks what re-timing the same defenses would change.",
 "how_it_works": "Surgeons and infection-control teams study SSIs through surveillance registries (NHSN in the US), bundle-compliance audits, randomized trials of prep agents and antibiotic timing, whole-genome sequencing of wound isolates to trace sources, and implementation science studying why bundles fail at the bedside.",
 "key_points": [
  "SSIs complicate roughly 2-5% of inpatient operations despite modern prevention.",
  "Most SSIs come from the patient's own flora, not the operating room environment.",
  "CDC (1999, 2017) and WHO (2016, 2018) guidelines codified prevention bundles.",
  "Timely antibiotics, chlorhexidine-alcohol prep, normothermia, and glycemic control are the best-evidenced elements.",
  "Rates have plateaued: no bundle has driven SSIs to zero.",
 ],
 "requirements": [
  "A mechanistic account of why the residual 2-5% escapes every bundle.",
  "Surveillance definitions stable enough to compare rates across hospitals and decades.",
  "Prevention strategies that work against resistant organisms, not just sensitive ones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mangram AJ et al. Guideline for prevention of surgical site infection. Infection Control and Hospital Epidemiology. 1999;20:247-280.",
  "Berrios-Torres SI et al. Centers for Disease Control and Prevention guideline for the prevention of surgical site infection, 2017. JAMA Surgery. 2017;152(8):784-791.",
  "World Health Organization. Global guidelines for the prevention of surgical site infection. 2nd ed. Geneva: WHO; 2018.",
  "de Lissovoy G et al. Surgical site infection: incidence and impact on hospital utilization and treatment costs. American Journal of Infection Control. 2009;37(5):387-397.",
 ],
 "demo_data": {"a": ("SSI rate in inpatient surgery, percent (CDC range midpoint)", 3.0),
               "b": ("percent scale", 100.0), "bounds": (0.02, 0.05),
               "step1": "about three in every hundred inpatient operations still ends in infection",
               "confirm": "re-timed bundles move SSI rates in the direction the race-window model predicts",
               "refute": "timing variations change nothing in randomized trials"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "anastomotic-leak",
 "name": "Predicting and Preventing Anastomotic Leaks",
 "group": "Gastrointestinal Surgery",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "After a surgeon joins two ends of bowel, the join leaks in a stubborn minority of cases - why can no test reliably predict which anastomosis will fail before it does?",
 "description": "An anastomotic leak is the escape of intestinal contents through a surgically created join between two segments of bowel. After colorectal surgery it occurs in roughly 3 to 20 percent of cases depending on the height of the join, and it is the most feared technical complication: leaks cause sepsis, demand reoperation, often end in a permanent stoma, and raise cancer recurrence risk. Surgeons judge bowel viability by color, bleeding edges, and experience - and still get surprised.",
 "background": "The hand-sewn anastomosis dates to the 19th century; stapling devices arrived in the 1960s-70s and standardized the mechanics, yet leak rates barely moved. Research has chased predictors for decades: blood supply (studied with Doppler, then indocyanine green fluorescence angiography), tension, microbiome shifts (notably collagenase-producing Enterococcus faecalis, shown by Alverdy's group to degrade anastomotic tissue in animal models), and patient factors like malnutrition and steroids. Intraoperative fluorescence imaging is now common but trials have not consistently shown it prevents leaks. As of 2026 no predictor or technique has made leaks rare.",
 "why_it_matters": "A leak turns a curative cancer operation into a catastrophe: mortality after a major leak reaches double digits, survivors face worse cancer outcomes, and health systems absorb enormous costs. Solving prediction would let surgeons reinforce or divert only the joins that need it instead of guessing.",
 "sig_pointer": "The Signature system's proposed approach treats the anastomosis as a negotiated truce between healing tissue and resident microbes, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that leaks are not primarily mechanical failures but ecological ones: the join creates a new niche, and whichever community - healing host tissue or collagenase-producing microbes - colonizes it first decides the outcome. "
  "Assumptions: (1) every anastomosis is simultaneously a wound and a fresh microbial habitat; (2) the first 48 hours decide the winner; (3) perfusion matters mainly as it changes the local oxygen landscape both sides compete in. "
  "Reasoning path: instead of asking whether the join is 'good,' the proposal asks who wins the 48-hour colonization race, reframing perfusion, antibiotics, and bowel prep as levers on race conditions rather than as independent risk factors. "
  "Proposed mechanism: a peri-anastomotic 'niche engineering' strategy - seeding the join zone with defined commensals that outcompete collagenase producers while secreting pro-healing signals, combined with perfusion optimization. "
  "What would confirm it: trials in which niche-engineered joins show leak reductions tracking the predicted microbial succession, with collagenase activity as the mediating biomarker. "
  "What would kill it: evidence that leaks occur with identical frequency in germ-free models, or that collagenase-producer abundance does not predict leaks in humans. "
  "What this does not claim: it does not claim a therapy ready for patients, does not claim probiotics prevent leaks, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the anastomosis as contested ground in a 48-hour colonization race, and asks what would guarantee the healing side wins.",
 "how_it_works": "Surgeons study leaks through registries, intraoperative perfusion imaging trials, microbiome sequencing of drain fluid and tissue, animal models of anastomotic healing, and randomized trials of diverting stomas, sealants, and reinforcement techniques.",
 "key_points": [
  "Colorectal anastomotic leaks occur in roughly 3-20% of cases, worst for low joins.",
  "Leaks cause sepsis, reoperation, permanent stomas, and worse cancer outcomes.",
  "Staplers standardized technique in the 1960s-70s but did not solve leaks.",
  "Collagenase-producing bacteria (e.g. Enterococcus faecalis) can degrade healing tissue in models.",
  "Fluorescence perfusion imaging has not consistently reduced leak rates in trials.",
 ],
 "requirements": [
  "A predictor that identifies the failing join before the abdomen is closed.",
  "A causal account separating mechanical, vascular, and microbial contributions.",
  "An intervention proven in randomized trials, not just associated in registries.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Alverdy JC et al. The gut microbiome and anastomotic leak. Nature Reviews Gastroenterology and Hepatology. 2017;14:673-683.",
  "Shogan BD et al. Collagenase-producing Enterococcus faecalis contributes to anastomotic leak. Science Translational Medicine. 2015;7(286):286ra68.",
  "McDermott FD et al. Systematic review of risk factors for anastomotic leakage after colorectal surgery. British Journal of Surgery. 2015;102(4):e115-e126.",
  "Degett TH et al. Indocyanine green fluorescence angiography for intraoperative assessment of bowel perfusion. Cochrane Database of Systematic Reviews. 2021;8:CD013280.",
 ],
 "demo_data": {"a": ("anastomotic leak rate, low colorectal joins, percent (upper range)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.21),
               "step1": "up to one in five low bowel joins leaks - the surgeon's most feared complication",
               "confirm": "microbial succession at the join predicts leaks and niche engineering reduces them",
               "refute": "leak rates prove identical in germ-free models or collagenase abundance predicts nothing"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "postoperative-ileus",
 "name": "Postoperative Ileus: Mechanism and Prevention",
 "group": "Perioperative Care",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "After abdominal surgery the gut commonly shuts down for days - why does postoperative ileus happen, and why has no treatment reliably shortened it?",
 "description": "Postoperative ileus is the temporary paralysis of gastrointestinal motility after surgery, lasting hours to days. It causes nausea, vomiting, bloating, delayed feeding, longer hospital stays, and occasional dangerous complications like aspiration. It follows most major abdominal operations to some degree, yet its mechanism remains contested and treatments - from chewing gum to alvimopan - have shown only modest or inconsistent benefit.",
 "background": "Ileus was long blamed on sympathetic overactivity and handled with nasogastric tubes and starvation. Research since the 1990s reframed it as an inflammatory response: surgical manipulation activates muscularis macrophages, recruiting leukocytes that paralyze smooth muscle (pioneering work by Kalff and Wehner). Opioids worsen it via gut mu-receptors, motivating peripherally acting antagonists like alvimopan, which shortens ileus modestly but carries cost and safety baggage. Enhanced Recovery After Surgery (ERAS) protocols bundle minimally invasive technique, opioid sparing, and early feeding, and have shortened stays overall - but ileus itself remains incompletely solved. As of 2026 no therapy targets its root mechanism.",
 "why_it_matters": "Ileus is the single biggest driver of delayed discharge after abdominal surgery: every extra day costs money, exposes patients to hospital harms, and delays cancer treatment. A true mechanistic cure would change the economics and experience of abdominal surgery.",
 "sig_pointer": "The Signature system's proposed approach treats ileus as the gut's immune system mistaking surgical handling for invasion, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ileus is a miscalibrated defense program: muscularis macrophages interpret mechanical manipulation as microbial invasion and trigger a motility shutdown that would, in nature, quarantine a breached gut. "
  "Assumptions: (1) the macrophage response scales with handling intensity, not with actual contamination; (2) the shutdown program is all-or-nothing once triggered; (3) resolution requires an active 'all-clear' signal, not merely time. "
  "Reasoning path: if ileus is a defense program rather than damage, the therapeutic target is the trigger threshold and the all-clear signal - explaining why anti-inflammatories help modestly and why minimal handling helps most. "
  "Proposed mechanism: pre-emptive macrophage 'reassurance' - vagal or pharmacologic signaling that raises the trigger threshold before incision, plus a defined resolution signal after, so the gut stands down faster. "
  "What would confirm it: interventions timed to the macrophage activation window outperforming the same drugs given later, with muscularis inflammation markers as mediators. "
  "What would kill it: evidence that ileus duration is set by neural reflexes alone with no inflammatory component, or that macrophage depletion changes nothing. "
  "What this does not claim: it does not claim a drug ready for patients, does not claim vagal stimulation treats ileus, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads ileus as a quarantine program misfiring at sterile handling, and asks what 'all-clear' signal would stand the gut down.",
 "how_it_works": "Researchers study ileus with animal models of intestinal manipulation, muscularis whole-mount immunology, transit measurements in patients, randomized trials of prokinetics and opioid antagonists, and ERAS implementation studies.",
 "key_points": [
  "Ileus follows most major abdominal operations and delays discharge by days.",
  "Surgical handling activates muscularis macrophages, triggering inflammatory paralysis.",
  "Opioids worsen ileus through gut mu-opioid receptors.",
  "Alvimopan shortens ileus modestly; chewing gum and coffee show small effects.",
  "ERAS protocols shortened stays but did not mechanistically solve ileus.",
 ],
 "requirements": [
  "A causal mechanism distinguishing neural, inflammatory, and pharmacologic components.",
  "A therapy targeting the root trigger, proven in randomized trials.",
  "A bedside marker of when the gut has truly recovered, not just passed flatus.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kalff JC, Wehner S. The inflammatory response to surgical trauma. Nature Reviews Immunology. 2012;12:369-378.",
  "Vather R et al. Postoperative ileus: a review. Diseases of the Colon and Rectum. 2014;57(5):654-666.",
  "Wolff BG et al. Alvimopan for postoperative ileus. Annals of Surgery. 2004;240(4):728-735.",
  "Gustafsson UO et al. Guidelines for perioperative care in elective colonic surgery: Enhanced Recovery After Surgery (ERAS) Society guidelines. World Journal of Surgery. 2013;37(2):259-284.",
 ],
 "demo_data": {"a": ("ileus-attributable extra stay, days (typical range midpoint)", 3.0),
               "b": ("days per week", 7.0), "bounds": (0.2, 0.7),
               "step1": "ileus commonly costs patients several extra days in hospital after abdominal surgery",
               "confirm": "macrophage-window-timed interventions shorten ileus beyond current best therapy",
               "refute": "macrophage depletion or pure neural blockade leaves ileus duration unchanged"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "adhesions",
 "name": "Preventing Peritoneal Adhesions",
 "group": "Wound Healing",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "After abdominal surgery, internal scar bands glue organs together in most patients - why does the peritoneum heal with adhesions, and why has nothing reliably prevented them?",
 "description": "Peritoneal adhesions are fibrous bands that form between abdominal organs and the abdominal wall after surgery, occurring after the majority of open abdominal operations. Most are silent, but adhesions cause small-bowel obstruction, chronic pelvic pain, infertility, and make every reoperation harder and riskier. Decades of barriers, gels, and drugs have produced, at best, partial reductions - never prevention.",
 "background": "Adhesions were described in the 19th century as surgery became survivable. The biology: peritoneal injury triggers fibrin deposition; normally fibrinolysis clears it, but surgical trauma, ischemia, and inflammation tip the balance toward persistent fibrin that fibroblasts colonize into permanent bands (detailed by diZerega and others). Hundreds of animal studies claimed prevention with barriers (hyaluronate films like Seprafilm), icodextrin solutions, and anti-inflammatories; human trials showed modest adhesion reduction at second-look laparoscopy but rarely translated into fewer obstructions - the outcome patients care about. As of 2026 no strategy prevents clinically meaningful adhesion disease.",
 "why_it_matters": "Adhesive small-bowel obstruction hospitalizes hundreds of thousands yearly, kills a fraction, and complicates fertility and chronic pain care. Reoperations through dense adhesions injure bowel in a meaningful minority. Prevention would remove one of surgery's commonest long-term harms.",
 "sig_pointer": "The Signature system's proposed approach treats adhesion formation as a fibrinolysis-timing failure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that adhesions are a timing failure of fibrinolysis: the peritoneum can dissolve fibrin bridges, but only within a narrow hours-long window before fibroblasts arrive and make them permanent. "
  "Assumptions: (1) every peritoneal injury deposits fibrin bridges; (2) the fibrinolytic window closes when fibroblast ingrowth begins, roughly 24-72 hours; (3) ischemia and inflammation shorten the window rather than merely adding fibrin. "
  "Reasoning path: barriers try to separate surfaces, but the proposal argues the decisive variable is keeping fibrin soluble until mesothelial regrowth - reframing prevention as window extension rather than separation. "
  "Proposed mechanism: a transient, locally delivered fibrinolysis extender applied at closure that holds fibrin bridges soluble through the fibroblast-arrival window, then switches off so healing completes. "
  "What would confirm it: adhesion reductions that track measured fibrinolytic activity duration rather than barrier presence, in randomized trials with obstruction endpoints. "
  "What would kill it: evidence that adhesions form even when fibrin is kept soluble through the full window, implicating direct fibroblast invasion independent of fibrin scaffolds. "
  "What this does not claim: it does not claim a product ready for patients, does not claim barriers are useless, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads adhesions as fibrin bridges that outlived their demolition window, and asks what would keep them soluble just long enough.",
 "how_it_works": "Researchers study adhesions in rodent and large-animal peritoneal injury models, second-look laparoscopy trials scoring adhesion extent, registry studies of obstruction readmissions, and trials of barriers, solutions, and laparoscopic versus open technique.",
 "key_points": [
  "Adhesions form after most open abdominal operations; many after laparoscopic ones too.",
  "They cause bowel obstruction, chronic pain, infertility, and hazardous reoperations.",
  "The biology is fibrin deposition outpacing fibrinolysis, then fibroblast colonization.",
  "Barriers like hyaluronate films reduce adhesion scores but rarely reduce obstructions.",
  "No strategy has prevented clinically meaningful adhesion disease.",
 ],
 "requirements": [
  "An intervention that reduces obstructions and reoperation injury, not just adhesion scores.",
  "A way to extend fibrinolysis without causing bleeding.",
  "Prevention compatible with normal wound healing elsewhere.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "diZerega GS. Contemporary adhesion prevention. Fertility and Sterility. 1994;61(2):219-235.",
  "ten Broek RPG et al. Burden of adhesions in abdominal and pelvic surgery: systematic review and meta-analysis. BMJ. 2013;347:f5588.",
  "Ahmad G et al. Barrier agents for adhesion prevention after gynaecological surgery. Cochrane Database of Systematic Reviews. 2020;3:CD000475.",
  "Diamond MP, Freeman ML. Clinical implications of postsurgical adhesions. Human Reproduction Update. 2001;7(6):567-576.",
 ],
 "demo_data": {"a": ("adhesive small-bowel obstructions, US admissions per year (approx thousands)", 300.0),
               "b": ("thousands scale", 1000.0), "bounds": (0.1, 0.6),
               "step1": "adhesions drive hundreds of thousands of bowel-obstruction admissions yearly",
               "confirm": "fibrinolysis-window extension cuts obstruction endpoints in randomized trials",
               "refute": "adhesions form at full rate even with fibrin held soluble through the window"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "surgical-timing",
 "name": "Optimal Timing of Surgery",
 "group": "Perioperative Care",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "For many conditions surgery can be done now, later, or never - why is the optimal timing still guesswork for so many diseases?",
 "description": "Timing questions haunt surgery: operate on acute cholecystitis today or in six weeks, fix an asymptomatic hernia now or watchfully wait, intervene on a small abdominal aortic aneurysm at 5.0 or 5.5 centimeters, resect a pancreatic cancer after chemotherapy or upfront. For a few conditions trials settled timing; for most, surgeons extrapolate from experience and local habit, and practice varies wildly between hospitals.",
 "background": "Landmark timing trials exist in pockets: early versus delayed cholecystectomy trials favored early surgery for acute cholecystitis; the UK small-aneurysm trial showed surveillance was safe below 5.5 cm; watchful waiting proved acceptable for minimally symptomatic hernias in the Fitzgibbons trial. But these are islands. For most conditions - when to operate on diverticulitis recurrences, prolapse, spine degeneration, early cancers - evidence is observational and confounded by the fact that sicker patients get operated sooner. Decision science has formalized the trade-off (operate now risks overtreatment; wait risks progression), yet personalized timing models remain research tools. As of 2026 most timing decisions rest on consensus, not proof.",
 "why_it_matters": "Wrong timing harms both ways: operating too early exposes patients to surgical risk for disease that would never have hurt them; waiting too long turns curable disease into emergency surgery with far worse outcomes. Getting timing right is among the highest-leverage decisions in all of surgery.",
 "sig_pointer": "The Signature system's proposed approach treats timing as an optimal-stopping problem with disease-specific clocks, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that timing decisions fail because surgeons track calendar time while diseases run on event clocks - progression events (rupture, obstruction, metastasis) that arrive stochastically, not on schedule. "
  "Assumptions: (1) each condition has a hazard function for its catastrophic event; (2) operative risk is roughly constant over the decision window while event hazard rises; (3) the optimal moment is when marginal event risk first exceeds marginal operative risk. "
  "Reasoning path: reframing 'when to operate' as optimal stopping converts a judgment call into an estimable crossing point, explaining why one-size thresholds (like 5.5 cm) work on average yet fail individuals with different hazard curves. "
  "Proposed mechanism: disease-specific hazard clocks learned from longitudinal registries, updated with each patient's measurements, emitting a personalized operate-now signal when the curves cross. "
  "What would confirm it: prospective trials where clock-guided timing beats guideline-threshold timing on combined harm endpoints. "
  "What would kill it: evidence that event hazards are dominated by unpredictable shocks with no learnable structure, making any clock no better than clinical judgment. "
  "What this does not claim: it does not claim an algorithm ready for patients, does not replace surgical judgment, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads timing as an optimal-stopping problem on a disease event-clock, and asks when the risk curves cross for this patient.",
 "how_it_works": "Surgeons study timing through randomized timing trials, registry analyses with causal methods, decision-analytic modeling, and watchful-waiting cohorts; guidelines committees synthesize these into threshold recommendations.",
 "key_points": [
  "Timing trials settled a few questions (early cholecystectomy, aneurysm surveillance) but most remain open.",
  "Practice varies widely between hospitals for the same condition.",
  "Observational timing data are confounded: sicker patients get earlier surgery.",
  "Threshold rules (e.g. 5.5 cm aneurysms) work on average, fail individuals.",
  "Personalized timing models remain research tools, not bedside practice.",
 ],
 "requirements": [
  "Disease-specific hazard curves for catastrophic progression events.",
  "Trials comparing personalized timing against fixed thresholds.",
  "Decision tools that integrate patient values, not just risks.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gurusamy KS et al. Early versus delayed laparoscopic cholecystectomy for acute cholecystitis. Cochrane Database of Systematic Reviews. 2013;6:CD005440.",
  "United Kingdom Small Aneurysm Trial Participants. Long-term outcomes of immediate repair versus surveillance of small abdominal aortic aneurysms. New England Journal of Medicine. 2002;346:1445-1452.",
  "Fitzgibbons RJ et al. Watchful waiting vs repair of inguinal hernia in minimally symptomatic men. JAMA. 2006;295(3):285-292.",
  "Birkmeyer JD et al. Hospital volume and surgical mortality in the United States. New England Journal of Medicine. 2002;346:1128-1137.",
 ],
 "demo_data": {"a": ("aneurysm repair threshold, centimeters (UK trial)", 5.5),
               "b": ("centimeters per decimeter", 10.0), "bounds": (0.4, 0.7),
               "step1": "a single 5.5 cm threshold governs aneurysm timing for millions - an average, not a person",
               "confirm": "clock-guided timing beats fixed thresholds on combined harm endpoints",
               "refute": "progression events prove dominated by unpredictable shocks with no learnable hazard"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "skill-assessment",
 "name": "Objective Assessment of Surgical Skill",
 "group": "Surgical Education",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Surgeons learn by apprenticeship and are judged by reputation - why is there still no objective, validated measure of who operates well?",
 "description": "Surgical skill varies enormously between operators, and that variation moves patient outcomes: landmark work by Birkmeyer showed that peer ratings of technical skill predicted complication rates in bariatric surgery. Yet skill is still certified by case logs, years in training, and subjective faculty ratings. Video-based assessment tools exist but are labor-intensive, and no health system credentials or pays surgeons by measured technical quality.",
 "background": "The apprenticeship model ('see one, do one, teach one', attributed to Halsted's residency system) dominated for a century. In 2013 Birkmeyer et al. (NEJM) had surgeons' videos peer-rated and found the bottom quartile had markedly higher complication and mortality rates - the first hard link between measured skill and outcomes. Objective Structured Assessment of Technical Skill (OSATS) and Global Evaluative Assessment of Robotic Skills (GEARS) formalized rating, and AI video analysis now promises automation, with early studies showing algorithms can distinguish skill levels from instrument motion. But validation against patient outcomes at scale, gaming resistance, and acceptance by the profession remain unsolved. As of 2026 no jurisdiction licenses surgeons by measured skill.",
 "why_it_matters": "If skill can be measured, it can be taught, coached, and selected for: the patients of the worst-quartile surgeons suffer preventable complications today. Objective measurement could also end training by the clock and start training to demonstrated competence.",
 "sig_pointer": "The Signature system's proposed approach treats surgical skill as a measurable economy of motion with tissue-specific signatures, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that technical skill is not a mysterious gift but a compressible quantity: expert motion contains less wasted energy, fewer corrective submovements, and force profiles matched to tissue type. "
  "Assumptions: (1) instrument kinematics plus force data capture most of what peer raters see; (2) tissue-specific force envelopes separate safe from dangerous technique; (3) skill is task-general enough that measurement transfers across similar procedures. "
  "Reasoning path: if expertise equals economy of motion tuned to tissue, then assessment reduces to measuring deviation from expert envelopes - explaining why motion metrics already predict peer ratings and why coaching toward economy improves outcomes. "
  "Proposed mechanism: a 'skill fingerprint' combining kinematic efficiency, force-envelope adherence, and decision latency, validated directly against complication rates rather than against peer ratings. "
  "What would confirm it: prospective data showing fingerprint scores predict patient outcomes across procedures and surgeons better than case volume does. "
  "What would kill it: evidence that outcomes are dominated by decision-making and patient factors with technique contributing too little to measure, or that fingerprints fail to transfer between procedures. "
  "What this does not claim: it does not claim an assessment ready for credentialing, does not claim AI replaces surgical judgment, and makes no claim about any individual surgeon."),
 "sig_lens": "The Signature lens reads surgical mastery as measurable economy of motion inside tissue-specific force envelopes, and asks what deviation predicts harm.",
 "how_it_works": "Researchers study skill through blinded video peer review, kinematic analysis of instrument motion, force-sensing instruments, AI models trained on annotated video, and linkage of scores to registry outcomes.",
 "key_points": [
  "Peer-rated technical skill predicts complication rates (Birkmeyer 2013, NEJM).",
  "Certification still rests on case logs, time in training, and subjective ratings.",
  "OSATS and GEARS formalized structured rating; AI video analysis is emerging.",
  "No health system credentials or pays by measured technical quality.",
  "Validation against patient outcomes at scale remains the missing step.",
 ],
 "requirements": [
  "Skill metrics validated directly against patient outcomes, not just peer ratings.",
  "Measurement that resists gaming and transfers across procedures.",
  "Professional and legal acceptance of skill-based credentialing.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Birkmeyer JD et al. Surgical skill and complication rates after bariatric surgery. New England Journal of Medicine. 2013;369:1694-1704.",
  "Martin JA et al. Objective structured assessment of technical skill (OSATS) for surgical residents. British Journal of Surgery. 1997;84(2):273-278.",
  "Goh AC et al. Global Evaluative Assessment of Robotic Skills (GEARS). Journal of Endourology. 2012;26(7):850-856.",
  "Halsted WS. The training of the surgeon. Bulletin of the Johns Hopkins Hospital. 1904;15:267-275.",
 ],
 "demo_data": {"a": ("surgeons in Birkmeyer peer-rating study", 20.0),
               "b": ("skill quartiles compared", 4.0), "bounds": (3.0, 8.0),
               "step1": "just twenty rated surgeons were enough to link measured skill to patient outcomes",
               "confirm": "kinematic fingerprints predict complications better than case volume across procedures",
               "refute": "outcomes prove dominated by decisions and patient factors with technique unmeasurable"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "chronic-postsurgical-pain",
 "name": "Chronic Post-Surgical Pain",
 "group": "Perioperative Care",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "A meaningful minority of patients still hurt months after their wound has healed - why does acute surgical pain become chronic, and how can the transition be stopped?",
 "description": "Chronic post-surgical pain (CPSP) is pain persisting at least three months after surgery, beyond normal healing. After thoracotomy it affects up to half of patients; after hernia repair, mastectomy, and amputation the rates are substantial. Nerve injury during surgery is the strongest risk factor, but most patients with similar nerve handling recover pain-free - the transition from acute to chronic pain remains mechanistically murky and largely unpreventable.",
 "background": "CPSP was characterized as a distinct entity by Macrae (2001, British Journal of Anaesthesia), with definitions refined by the International Association for the Study of Pain. Risk factors emerged: pre-existing pain, severe acute postoperative pain, nerve injury, and psychological vulnerability. The mechanistic story centers on peripheral nerve injury plus central sensitization - the spinal cord and brain amplifying signals - but why sensitization resolves in most and persists in some is unknown. Preventive trials (gabapentinoids, ketamine, regional anesthesia) show modest or inconsistent effects; once established, CPSP responds poorly to treatment. As of 2026 prevention remains the unsolved frontier.",
 "why_it_matters": "CPSP ruins recoveries: patients cured of their surgical disease trade it for a chronic pain condition, with disability, opioid exposure, depression, and lost work. With hundreds of millions of operations yearly, even single-digit percentages mean millions of new chronic pain patients.",
 "sig_pointer": "The Signature system's proposed approach treats the acute-to-chronic transition as a learning event in pain circuits, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that CPSP is the pain system's memory: intense perioperative nociceptive input writes a persistent pattern into spinal and cortical circuits, and the transition is a learning event with a consolidation window. "
  "Assumptions: (1) central sensitization follows learning-like rules including a time-limited consolidation phase; (2) the strength of the 'lesson' scales with acute pain intensity times duration; (3) reconsolidation can be disrupted, as in fear-memory research. "
  "Reasoning path: if chronicity is consolidation, then prevention must target the consolidation window - explaining why severe acute pain predicts CPSP and why pre-emptive analgesia trials (which blunt input but miss the window) underwhelm. "
  "Proposed mechanism: a perioperative 'memory interference' protocol combining profound acute pain control with agents or stimulation timed to disrupt consolidation in the days after surgery, plus early detection of the patients whose circuits are consolidating. "
  "What would confirm it: interventions delivered in the consolidation window outperforming identical treatment given later, with quantitative sensory testing tracking the effect. "
  "What would kill it: evidence that CPSP is fully determined by peripheral nerve pathology with no central learning component, or that consolidation-window timing changes nothing. "
  "What this does not claim: it does not claim a treatment for established chronic pain, does not recommend any drug, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the acute-to-chronic transition as a pain memory being consolidated, and asks what would interfere with the writing.",
 "how_it_works": "Researchers study CPSP through prospective cohorts with quantitative sensory testing, nerve-injury models, brain imaging of sensitization, genetic association studies, and randomized prevention trials of analgesic regimens.",
 "key_points": [
  "CPSP is pain persisting 3+ months after surgery; rates reach ~50% after thoracotomy.",
  "Nerve injury and severe acute pain are the strongest risk factors.",
  "Central sensitization is implicated but its persistence mechanism is unknown.",
  "Preventive trials show modest, inconsistent effects; established CPSP is hard to treat.",
  "Macrae (2001) and IASP formalized CPSP as a distinct entity.",
 ],
 "requirements": [
  "A mechanistic account of why sensitization persists in some and resolves in most.",
  "A biomarker identifying consolidating patients before pain becomes chronic.",
  "Prevention proven in trials, not just association of risk factors.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Macrae WA. Chronic post-surgical pain: 10 years on. British Journal of Anaesthesia. 2008;101(1):77-86.",
  "Kehlet H et al. Persistent postsurgical pain: risk factors and prevention. Lancet. 2006;367:1618-1625.",
  "Schug SA, Bruce J. Risk stratification for the development of chronic postsurgical pain. Pain Reports. 2017;2(6):e627.",
  "Werner MU, Kongsgaard UE. Defining persistent post-surgical pain. British Journal of Anaesthesia. 2014;113(1):1-4.",
 ],
 "demo_data": {"a": ("CPSP rate after thoracotomy, percent (upper range)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.6),
               "step1": "up to half of thoracotomy patients still hurt months after healing",
               "confirm": "consolidation-window interventions outperform identical later treatment",
               "refute": "CPSP proves fully determined by peripheral pathology with no central component"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "wound-dehiscence",
 "name": "Predicting Wound Dehiscence",
 "group": "Wound Healing",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Some abdominal wounds burst open days after closure - why can surgeons not predict which closures will fail?",
 "description": "Fascial dehiscence - the separation of the abdominal wall layers after laparotomy - occurs in roughly 1 to 3 percent of cases and carries mortality around 15 percent when evisceration follows. It strikes days after an apparently sound closure, driven by rising intra-abdominal pressure against a healing wound, but the patients it strikes are only partly predictable by known risk factors.",
 "background": "Dehiscence has been recognized since abdominal surgery began; the classic teaching blamed technique (sutures too tight, bites too small). The STITCH trial (Millbourn et al., Lancet 2015) showed small bites with slowly absorbable suture cut hernia and dehiscence rates, refining technique meaningfully. Risk models combine patient factors - age, malnutrition, steroids, infection, raised pressure from coughing or ileus - yet discrimination remains modest: most dehiscences still surprise. Biological research points to collagen metabolism defects in some patients, but no bedside test measures wound strength during healing. As of 2026 prediction remains imprecise and prevention is technique plus risk-factor control.",
 "why_it_matters": "Dehiscence is a catastrophe: emergency reoperation, prolonged critical care, high mortality, and near-certain incisional hernia afterward. Predicting the failing closure would allow prophylactic mesh or retention sutures in exactly the patients who need them.",
 "sig_pointer": "The Signature system's proposed approach treats the healing wound as a structure whose load-bearing capacity can be tracked, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dehiscence is a structural engineering failure with a measurable prodrome: the wound's tensile strength follows a predictable curve, and failure occurs when rising abdominal pressure crosses falling early strength. "
  "Assumptions: (1) wound strength over the first two weeks is the dominant variable; (2) intra-abdominal pressure spikes are the triggering loads; (3) collagen subtype ratios in wound fluid track the strength curve. "
  "Reasoning path: reframing dehiscence as load-versus-capacity makes prediction a measurement problem - track capacity (wound fluid biomarkers, elastography) and load (pressure monitoring) and intervene when the margin narrows. "
  "Proposed mechanism: a postoperative 'wound margin monitor' combining noninvasive stiffness measurement of the healing fascia with pressure tracking, triggering prophylactic support when the safety margin collapses. "
  "What would confirm it: prospective data showing margin-narrowing precedes dehiscence and that margin-triggered reinforcement prevents it. "
  "What would kill it: evidence that dehiscence is dominated by sudden catastrophic suture failure with no prodromal weakening, or that wound fluid markers do not track strength. "
  "What this does not claim: it does not claim a device ready for patients, does not claim prediction is currently possible, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads dehiscence as load crossing capacity on a measurable strength curve, and asks what would reveal the crossing before it happens.",
 "how_it_works": "Surgeons study dehiscence through closure-technique trials, risk-prediction modeling from registries, wound-fluid biomarker research, and trials of prophylactic mesh in high-risk closures.",
 "key_points": [
  "Fascial dehiscence complicates ~1-3% of laparotomies with high mortality when evisceration occurs.",
  "The STITCH trial showed small-bite closure reduces failure rates.",
  "Known risk factors (age, malnutrition, steroids, infection, pressure) predict only modestly.",
  "No bedside test measures healing wound strength during the vulnerable weeks.",
  "Prophylactic mesh helps high-risk patients but selection remains crude.",
 ],
 "requirements": [
  "A bedside measure of healing wound strength or its trajectory.",
  "A load-versus-capacity model validated prospectively.",
  "Proof that margin-triggered reinforcement prevents dehiscence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Millbourn D et al. Effect of stitch length on wound complications after midline incision (STITCH trial). Lancet. 2015;386:2026-2034.",
  "van Ramshorst GH et al. Risk factors for abdominal wound dehiscence. JAMA Surgery. 2014;149(5):463-469.",
  "Hodgson NCF et al. The search for an ideal method of abdominal fascial closure. Annals of Surgery. 2000;231(3):436-442.",
  "Deerenberg EB et al. Small bites versus large bites for closure of abdominal midline incisions. New England Journal of Medicine. 2015;373:1662.",
 ],
 "demo_data": {"a": ("fascial dehiscence rate, percent (midpoint)", 2.0),
               "b": ("mortality with evisceration, percent", 15.0), "bounds": (0.05, 0.25),
               "step1": "dehiscence is uncommon but its mortality reaches double digits when bowel eviscerates",
               "confirm": "margin-narrowing precedes dehiscence and triggered reinforcement prevents it",
               "refute": "dehiscence proves sudden suture failure with no measurable prodromal weakening"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "transfusion-thresholds",
 "name": "Transfusion Thresholds in Surgery",
 "group": "Perioperative Care",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "How anemic can a surgical patient safely be - and why does the 'right' transfusion trigger still differ between trials, tissues, and patients?",
 "description": "Blood transfusion saves lives in hemorrhage, but for stable anemia the trigger has been debated for decades. Liberal transfusion (trigger near 10 g/dL hemoglobin) was traditional; restrictive strategies (7-8 g/dL) proved non-inferior in landmark trials - yet subgroups (cardiac surgery, brain injury, elderly) keep showing signals that one size does not fit all, and tissue-level oxygen needs remain unmeasured at the bedside.",
 "background": "The 10/30 rule (transfuse below hemoglobin 10 g/dL or hematocrit 30%) ruled unchallenged until the TRICC trial (Hebert et al., NEJM 1999) showed a restrictive 7 g/dL trigger was at least as good in critical care. Surgical trials followed: FOCUS (hip fracture), TRACS (cardiac surgery), and others largely supported restrictiveness, and patient blood management programs cut usage worldwide. But transfused blood is not benign - lung injury (TRALI), circulatory overload (TACO), immunomodulation, and infections are real - while anemia impairs healing and cognition. The frontier question is physiologic: hemoglobin is a crude proxy for tissue oxygen delivery, and no bedside measure of whether a given patient's tissues need blood exists. As of 2026 the trigger remains a population number, not a personal one.",
 "why_it_matters": "Blood is scarce, costly, and risky: every unnecessary unit exposes a patient to harm and drains the supply. Every withheld-but-needed unit risks organ injury. A personal, tissue-based trigger would end decades of one-size-fits-all transfusion.",
 "sig_pointer": "The Signature system's proposed approach treats the transfusion decision as a tissue-oxygen debt problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hemoglobin triggers fail because they measure the delivery truck, not the delivery: what matters is tissue oxygen debt, which depends on cardiac output, extraction, and metabolic demand as much as on hemoglobin. "
  "Assumptions: (1) organ injury from anemia occurs when cumulative oxygen debt crosses tissue-specific thresholds; (2) debt can be estimated from perfusion signals already monitored; (3) thresholds differ by organ and by patient reserve. "
  "Reasoning path: reframing transfusion as debt repayment explains why the same hemoglobin is safe in one patient and injurious in another, and why trials keep finding subgroup exceptions to restrictive rules. "
  "Proposed mechanism: a 'tissue oxygen ledger' fusing hemoglobin, perfusion, and metabolic signals into a running debt estimate per organ system, transfusing when debt - not hemoglobin - crosses the line. "
  "What would confirm it: trials where ledger-guided transfusion beats hemoglobin-guided on organ-injury endpoints with equal or less blood used. "
  "What would kill it: evidence that hemoglobin alone captures all the predictive information, or that debt estimates add no discrimination beyond hemoglobin plus clinical judgment. "
  "What this does not claim: it does not claim a monitor ready for patients, does not recommend withholding transfusion, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads transfusion as repaying a tissue oxygen debt, and asks what ledger would show the debt directly.",
 "how_it_works": "Researchers study transfusion through randomized trigger trials, blood-management implementation programs, near-infrared tissue oximetry studies, and mechanistic work on storage lesion and transfusion immunomodulation.",
 "key_points": [
  "TRICC (1999) established that restrictive transfusion (7 g/dL) is safe in critical care.",
  "Surgical trials (FOCUS, TRACS) largely extended restrictiveness to operative patients.",
  "Transfusion carries real harms: TRALI, TACO, immunomodulation, infection.",
  "Subgroups (cardiac, brain injury, elderly) keep challenging one-size-fits-all triggers.",
  "Hemoglobin is a crude proxy; tissue oxygen need is unmeasured at the bedside.",
 ],
 "requirements": [
  "A bedside measure of tissue oxygen debt, not just hemoglobin.",
  "Trials of physiologic triggers against hemoglobin triggers.",
  "Subgroup-specific evidence for cardiac, neurologic, and elderly patients.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hebert PC et al. A multicenter, randomized, controlled clinical trial of transfusion requirements in critical care (TRICC). New England Journal of Medicine. 1999;340:409-417.",
  "Carson JL et al. Liberal or restrictive transfusion in high-risk patients after hip surgery (FOCUS). New England Journal of Medicine. 2011;365:2453-2462.",
  "Hajjar LA et al. Transfusion requirements after cardiac surgery (TRACS). JAMA. 2010;304(14):1559-1567.",
  "Mueller MM et al. Patient blood management: recommendations from the 2018 Frankfurt Consensus Conference. JAMA. 2019;321(10):983-997.",
 ],
 "demo_data": {"a": ("restrictive trigger, hemoglobin g/dL (TRICC)", 7.0),
               "b": ("liberal trigger, hemoglobin g/dL (traditional)", 10.0), "bounds": (0.6, 0.9),
               "step1": "the restrictive trigger uses thirty percent less hemoglobin as its line - yet proved as safe",
               "confirm": "ledger-guided transfusion beats hemoglobin-guided on organ injury with equal blood use",
               "refute": "hemoglobin alone captures all predictive information about transfusion need"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "sham-surgery",
 "name": "The Placebo Effect of Surgery",
 "group": "Surgical Evidence",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Some operations work no better than sham surgery - how much of surgery's benefit is the ritual itself, and which procedures survive a placebo control?",
 "description": "Sham-controlled surgical trials - where the control group receives anesthesia and incisions but not the therapeutic maneuver - have produced genuine shocks: arthroscopic debridement for knee osteoarthritis (Moseley et al., NEJM 2002) and vertebroplasty for osteoporotic fractures (Buchbinder and Kallmes, NEJM 2009) both proved no better than placebo. These results imply that a meaningful share of some operations' benefit comes from expectation, the care ritual, and natural history rather than the procedure's mechanism.",
 "background": "The first famous sham surgery trial was Cobb's 1959 internal mammary ligation study for angina, which killed the procedure by showing sham worked equally well. The modern era began with Moseley's 2002 knee arthroscopy trial, then vertebroplasty's double sham trials in 2009. Since then, sham controls have been applied sparingly - they are expensive, ethically fraught, and surgeons resist them - but where used, they keep humbling: sham-controlled trials of subacromial decompression (CSAWH trial) and others narrowed indications. The deeper problem is that most of the thousands of surgical procedures in use have never faced any placebo control, and the placebo mechanisms in surgery (expectation, conditioning, the meaning response) are poorly mapped. As of 2026 sham surgery remains rare and controversial.",
 "why_it_matters": "If an operation's benefit is mostly placebo, patients bear surgical risk for no mechanistic gain - and health systems pay billions for theater. Identifying which procedures survive sham controls would prune low-value surgery and redirect effort to what truly works.",
 "sig_pointer": "The Signature system's proposed approach treats surgical placebo as a measurable neurobiological response to be isolated, not a nuisance, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the surgical placebo response is not noise but a quantifiable neurobiological event - expectation-driven endogenous opioid and dopamine release triggered by the surgical ritual - and that it can be measured and subtracted. "
  "Assumptions: (1) the ritual components (anesthesia, incision, surgeon confidence, postoperative care) produce a real, time-limited neurochemical response; (2) this response is separable from the mechanical effect by comparing trajectories, not just endpoints; (3) individual placebo responsiveness is a stable trait. "
  "Reasoning path: if placebo is a real response with its own time course, then sham trials need not be all-or-nothing - the ritual response can be modeled from the sham arm and subtracted to reveal the true mechanical effect, even in trials without full sham surgery. "
  "Proposed mechanism: a 'ritual-response model' that predicts each patient's expected placebo trajectory from baseline psychology and early postoperative markers, allowing mechanistic efficacy to be estimated from ordinary randomized trials. "
  "What would confirm it: the model predicting sham-arm outcomes in existing sham trials, and de-confounded effect sizes changing which procedures look effective. "
  "What would kill it: evidence that sham responses are entirely regression to the mean and natural history with no ritual-driven neurobiology, or that placebo responsiveness has no stable individual component. "
  "What this does not claim: it does not claim any specific operation is placebo, does not recommend forgoing surgery, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the surgical ritual as a drug with its own dose-response curve, and asks what remains when that curve is subtracted.",
 "how_it_works": "Researchers study surgical placebo through sham-controlled trials, meta-analyses of sham versus no-treatment arms, neuroimaging of expectation effects, and ethical frameworks for when sham controls are justified.",
 "key_points": [
  "Knee arthroscopy for osteoarthritis proved no better than sham (Moseley 2002).",
  "Vertebroplasty failed against sham in two 2009 NEJM trials.",
  "Internal mammary ligation was killed by a 1959 sham trial.",
  "Most surgical procedures have never faced any placebo control.",
  "Sham trials remain rare: expensive, ethically fraught, and resisted.",
 ],
 "requirements": [
  "Ethical frameworks defining when sham surgical controls are justified.",
  "A mechanistic map of expectation and conditioning effects in surgical contexts.",
  "Methods to estimate mechanistic efficacy without full sham surgery.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Moseley JB et al. A controlled trial of arthroscopic surgery for osteoarthritis of the knee. New England Journal of Medicine. 2002;347:81-88.",
  "Buchbinder R et al. A randomized trial of vertebroplasty for painful osteoporotic vertebral fractures. New England Journal of Medicine. 2009;361:557-568.",
  "Kallmes DF et al. A randomized trial of vertebroplasty for osteoporotic spinal fractures. New England Journal of Medicine. 2009;361:569-579.",
  "Wartolowska K et al. Use of placebo controls in the evaluation of surgery: systematic review. BMJ. 2014;348:g3256.",
 ],
 "demo_data": {"a": ("sham-controlled surgical trials published, approximate count", 60.0),
               "b": ("surgical procedures in common use, approximate count", 3000.0), "bounds": (0.01, 0.05),
               "step1": "only a tiny fraction of surgical procedures has ever faced a placebo control",
               "confirm": "the ritual-response model predicts sham-arm outcomes in existing sham trials",
               "refute": "sham responses prove entirely regression to the mean with no ritual neurobiology"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "surgical-smoke",
 "name": "Surgical Smoke Hazards",
 "group": "Occupational Surgery",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Every electrocautery cut fills the operating room with smoke - what does a career of breathing it do to surgical teams, and why is evacuation still optional in most rooms?",
 "description": "Surgical smoke is the plume produced when energy devices vaporize tissue: it contains volatile organic compounds (benzene, formaldehyde), fine particulate matter, and viable cellular material including viral DNA. Operating room staff breathe it daily for entire careers. Studies find mutagenic compounds in the plume and measurable uptake in staff, yet smoke evacuation remains inconsistently used and long-term epidemiologic data on staff health are missing.",
 "background": "Concerns date to the 1980s with the spread of electrocautery and lasers. Chemical analyses identified dozens of hazardous compounds; in vitro work showed the plume is mutagenic, and case reports documented transmission of human papillomavirus to surgeons via laser plume. Professional bodies (AORN, NIOSH) issued evacuation guidance, and a few jurisdictions legislated evacuation, but adoption lags: evacuators are noisy, cumbersome, and add cost. The evidence gap is epidemiologic - no large cohort has tracked cancer or respiratory outcomes in exposed versus protected staff over careers. As of 2026 the hazard is chemically plausible, biologically suggestive, and epidemiologically unproven.",
 "why_it_matters": "Millions of operating-room workers worldwide inhale surgical smoke as a condition of employment. If the plume carries real long-term risk, evacuation is one of the cheapest preventive interventions in medicine; if it does not, mandates waste resources. Only data can settle it.",
 "sig_pointer": "The Signature system's proposed approach treats the plume as a dosable occupational exposure to be measured per-procedure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the smoke question is stuck because exposure is discussed as present-or-absent while the biology is dose-and-composition: different devices, tissues, and durations produce wildly different plumes. "
  "Assumptions: (1) plume composition varies systematically by energy device and tissue type; (2) staff dose accumulates as a career integral, not a binary exposure; (3) the relevant health endpoints are chronic (respiratory, neoplastic), requiring dose reconstruction. "
  "Reasoning path: reframing smoke as a measurable dose converts an unanswerable 'is it harmful' into an estimable dose-response - explaining why crude exposed-versus-unexposed studies keep failing and what study would actually work. "
  "Proposed mechanism: a procedure-level plume dosimetry (particle counts plus key volatiles, logged per case) linked to staff career dose registries, enabling the first real dose-response epidemiology. "
  "What would confirm it: dose registries showing graded health effects with cumulative plume dose, or conversely a clean null at high doses. "
  "What would kill it: evidence that plume constituents at real concentrations are biologically inert in chronic inhalation models, making dosimetry moot. "
  "What this does not claim: it does not claim smoke is proven harmful, does not claim evacuation mandates are warranted today, and makes no occupational-health recommendation."),
 "sig_lens": "The Signature lens reads the plume as an unmeasured career dose, and asks what dosimetry would turn a debate into a dose-response curve.",
 "how_it_works": "Researchers study surgical smoke through chemical analysis of plume constituents, in vitro mutagenicity assays, particle counting in operating rooms, staff biomarker studies, and the slow accumulation of occupational cohort data.",
 "key_points": [
  "Surgical smoke contains benzene, formaldehyde, fine particulates, and viral DNA.",
  "The plume is mutagenic in laboratory assays; HPV transmission via plume is documented.",
  "AORN and NIOSH recommend evacuation, but use remains inconsistent.",
  "No large cohort has tracked long-term staff health by exposure level.",
  "A few jurisdictions have legislated smoke evacuation.",
 ],
 "requirements": [
  "Procedure-level plume dosimetry that is practical in real operating rooms.",
  "Career dose registries linked to staff health outcomes.",
  "Device and tissue-specific composition data to target evacuation where it matters.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "National Institute for Occupational Safety and Health. Control of smoke from laser/electric surgical procedures. NIOSH Publication No. 96-128. 1996.",
  "Hill DS et al. Surgical smoke: a systematic review. Occupational Medicine. 2012;62(4):242-253.",
  "Barrett WL, Garber SM. Surgical smoke: a review of the literature. Surgical Endoscopy. 2003;17:979-987.",
  "Association of periOperative Registered Nurses. Guideline for surgical smoke safety. AORN Guidelines for Perioperative Practice. 2021.",
 ],
 "demo_data": {"a": ("hazardous compounds identified in surgical plume (approx)", 80.0),
               "b": ("compounds routinely monitored in operating rooms", 1.0), "bounds": (40.0, 150.0),
               "step1": "dozens of hazardous compounds are known in the plume, yet rooms monitor essentially none",
               "confirm": "career dose registries reveal a graded dose-response for staff health endpoints",
               "refute": "chronic inhalation models show plume constituents biologically inert at real doses"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "organ-preservation",
 "name": "Extending Organ Preservation Time",
 "group": "Transplantation",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "A donor heart lasts about four hours on ice - why does cold storage injure organs, and what would let a liver wait days instead of hours?",
 "description": "Static cold storage - flushing an organ with preservation solution and packing it on ice - has been transplantation's workhorse since the 1980s. But cold ischemia injures: hearts tolerate roughly 4 hours, lungs 6-8, livers and kidneys 12-24. Every year organs are discarded because no recipient can be reached in time, and longer ischemia means worse graft function. Machine perfusion (pumping oxygenated fluid through the organ at cold or body temperature) is extending limits, but the biology of preservation injury remains incompletely mapped.",
 "background": "Collins solution (1969) and later University of Wisconsin solution (Belzer, 1988) made multi-organ procurement practical. The injury mechanisms - ATP depletion, sodium pump failure, cell swelling, and then reperfusion injury when blood returns - were worked out in the 1980s-90s. Hypothermic machine perfusion improved kidneys; normothermic perfusion (keeping the organ warm and metabolizing, pioneered for livers by Friend's group in Oxford and for lungs by Steen) lets surgeons assess and even repair organs before transplant. Trials show perfusion reduces complications, but each organ needs its own protocol, costs are high, and the dream - banking organs for days or weeks - remains distant. As of 2026 normothermic perfusion is spreading but cold ischemia limits still discard organs daily.",
 "why_it_matters": "The organ shortage kills people on waitlists every day; a meaningful fraction of recovered organs goes unused, often for logistical time reasons. Doubling safe preservation time would convert geography from a barrier into a detail and let marginal organs be repaired before transplant.",
 "sig_pointer": "The Signature system's proposed approach treats preservation as suspended animation to be tuned per organ, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that preservation injury is not one process but a sequence of metabolic checkpoints, and that current protocols fail because they apply one static recipe to a dynamic decay. "
  "Assumptions: (1) each organ's injury follows a predictable cascade with organ-specific rate-limiting steps; (2) the cascade can be paused at checkpoints rather than merely slowed; (3) reperfusion injury is programmed during storage, not just triggered at reperfusion. "
  "Reasoning path: if injury is a checkpoint sequence, preservation becomes a control problem - sense which checkpoint the organ approaches and intervene there - explaining why static cold storage plateaus and why perfusion helps without solving banking. "
  "Proposed mechanism: checkpoint-targeted perfusion that adjusts temperature, oxygen, and metabolic substrates in response to real-time organ biomarkers, holding each organ at its own optimal pause point. "
  "What would confirm it: checkpoint-guided protocols extending viable storage beyond current best times with equal or better graft function in trials. "
  "What would kill it: evidence that injury is dominated by stochastic membrane damage with no controllable checkpoints, or that biomarker-guided adjustments add nothing to fixed protocols. "
  "What this does not claim: it does not claim organs can be banked today, does not claim a protocol ready for clinical use, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads cold ischemia as a cascade of pausable checkpoints, and asks what control loop would hold each organ at its best pause.",
 "how_it_works": "Transplant researchers study preservation through animal transplant models, perfusate biomarker discovery, randomized trials of perfusion versus cold storage, and efforts to resuscitate declined organs on pumps.",
 "key_points": [
  "Hearts tolerate ~4 hours of cold ischemia; livers and kidneys 12-24 hours.",
  "UW solution (1988) and machine perfusion progressively extended limits.",
  "Normothermic perfusion keeps organs metabolizing and assessable before transplant.",
  "Organs are still discarded daily because no recipient can be reached in time.",
  "Reperfusion injury is programmed during storage, not only at blood return.",
 ],
 "requirements": [
  "Organ-specific checkpoint maps of preservation injury.",
  "Real-time biomarkers of organ viability during perfusion.",
  "Protocols that extend storage toward days, not just hours.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Belzer FO, Southard JH. Principles of solid-organ preservation by cold storage. Transplantation. 1988;45(4):673-676.",
  "Ravikumar R et al. Liver transplantation after normothermic machine preservation. Nature. 2016;538:73-76.",
  "Nasralla D et al. A randomized trial of normothermic preservation in liver transplantation. Nature. 2018;557:50-56.",
  "Steen S et al. Transplantation of lungs from non-heart-beating donors after functional assessment ex vivo. Lancet. 2001;357:825-829.",
 ],
 "demo_data": {"a": ("safe cold ischemia, donor heart, hours", 4.0),
               "b": ("safe cold ischemia, donor kidney, hours", 24.0), "bounds": (0.1, 0.3),
               "step1": "a heart gets hours on ice while a kidney gets a day - preservation is organ-specific",
               "confirm": "checkpoint-guided perfusion extends viable storage beyond current best times",
               "refute": "injury proves stochastic membrane damage with no controllable checkpoints"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "transplant-tolerance",
 "name": "Immune Tolerance Without Lifelong Immunosuppression",
 "group": "Transplantation",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Transplant recipients trade organ failure for lifelong immune suppression - why can the immune system not be taught to accept the graft and then left alone?",
 "description": "Modern immunosuppression (calcineurin inhibitors since cyclosporine's 1983 introduction) made organ transplantation routine, but the price is permanent: infections, cancers, kidney damage, diabetes, and cardiovascular disease from the drugs themselves. True tolerance - a graft accepted without drugs - occurs spontaneously in a tiny minority (operational tolerance, best documented in liver recipients), but no protocol reliably induces it, and attempts have sometimes ended in rejection or graft-versus-host disease.",
 "background": "Medawar's 1950s mouse experiments proved acquired tolerance was possible, launching transplantation immunology. Clinical tolerance trials used mixed chimerism (donor bone marrow plus organ, pioneered by Sachs, Sykes, and Spitzer), regulatory T-cell infusions, and costimulation blockade (belatacept). Results tantalize: some kidney recipients have come off drugs for years, but protocols are complex, require toxic conditioning, and fail unpredictably. The liver's relative tolerogenicity - 20-40% of liver recipients can eventually stop drugs in weaning trials - hints the biology exists but is organ-specific and unmapped. As of 2026 tolerance remains experimental, and every recipient is counseled to expect lifelong drugs.",
 "why_it_matters": "Lifelong immunosuppression shortens the lives it saves: recipients die of drug-caused infections, malignancies, and organ damage. Tolerance would convert transplantation from a managed chronic condition into a cure, and slash costs.",
 "sig_pointer": "The Signature system's proposed approach treats tolerance as an immune education problem with a teachable window, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tolerance fails because protocols suppress the immune system while trying to teach it - like shouting a lesson at a sedated student. "
  "Assumptions: (1) the peritransplant period is a genuine learning window when the immune repertoire is plastic; (2) broad suppression during that window prevents the very learning tolerance requires; (3) the liver's tolerogenicity comes from its constant low-grade antigen presentation, a teachable mechanism. "
  "Reasoning path: if tolerance is education, protocols should minimize suppression precisely when teaching is most intense, then verify learning with biomarkers before withdrawing drugs - explaining why heavy conditioning regimens both enable and sabotage tolerance. "
  "Proposed mechanism: a 'teaching protocol' with minimal early suppression, deliberate donor-antigen presentation in tolerogenic contexts, regulatory T-cell support, and biomarker-gated drug withdrawal. "
  "What would confirm it: teaching protocols producing durable drug-free survival at higher rates than conventional trials, with regulatory signatures predicting success. "
  "What would kill it: evidence that the repertoire is not plastic in adults regardless of context, or that biomarker-gated withdrawal fails as often as empirical weaning. "
  "What this does not claim: it does not claim tolerance is achievable today, does not advise stopping immunosuppression, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads tolerance as a lesson the immune system must learn while awake, and asks what teaching protocol would make it stick.",
 "how_it_works": "Immunologists study tolerance through mixed-chimerism trials, regulatory T-cell therapy trials, drug-weaning studies with immune monitoring, and animal models of costimulation blockade.",
 "key_points": [
  "Cyclosporine (1983) made transplantation routine but mandated lifelong drugs.",
  "Drug toxicities - infection, cancer, kidney damage - limit recipient survival.",
  "Operational tolerance occurs spontaneously in a minority, mostly liver recipients.",
  "Mixed chimerism and Treg trials show promise but remain experimental and complex.",
  "No protocol reliably induces drug-free graft acceptance.",
 ],
 "requirements": [
  "A teaching protocol simpler and safer than current conditioning regimens.",
  "Biomarkers that verify tolerance before drugs are withdrawn.",
  "Understanding of why the liver tolerates and other organs do not.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Billingham RE, Brent L, Medawar PB. Actively acquired tolerance of foreign cells. Nature. 1953;172:603-606.",
  "Kawai T et al. HLA-mismatched renal transplantation without maintenance immunosuppression. New England Journal of Medicine. 2008;358:353-361.",
  "Todo S et al. Cell therapy for liver transplantation. Hepatology. 2016;64(5):1763-1772.",
  "Vincenti F et al. Costimulation blockade with belatacept in renal transplantation. New England Journal of Medicine. 2005;353:770-781.",
 ],
 "demo_data": {"a": ("liver recipients achieving operational tolerance, percent (weaning trials)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.4),
               "step1": "nearly a third of liver recipients can eventually stop drugs - proof tolerance biology exists",
               "confirm": "teaching protocols beat conventional trials in durable drug-free survival",
               "refute": "the adult repertoire proves unplastic regardless of presentation context"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "xenotransplantation",
 "name": "Xenotransplantation Barriers",
 "group": "Transplantation",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Pig organs could end the organ shortage - what still stands between gene-edited pig kidneys and routine human transplants?",
 "description": "Xenotransplantation - transplanting animal organs into humans - promises an unlimited organ supply. Pigs are the donor of choice: similar organ size, fast breeding, and editable genomes. In 2022-2024, gene-edited pig hearts and kidneys were transplanted into living patients and brain-dead recipients, surviving weeks to months. But hyperacute rejection (solved by knocking out pig sugar antigens), coagulation dysregulation, porcine endogenous retroviruses, and long-term immune injury remain partially unsolved.",
 "background": "Early xenotransplantation (Hardy's 1964 chimpanzee heart, Baby Fae's 1984 baboon heart) failed within days to weeks from rejection. The molecular era began with alpha-Gal knockout pigs (2002), removing the main hyperacute target; CRISPR then enabled multi-gene edits - knocking out three major xenoantigens, adding human complement and coagulation regulators, and inactivating porcine endogenous retroviruses (eGenesis, 2017). The 2022 Maryland pig-heart transplant (Bennett, survived 2 months) and 2024 pig-kidney transplants at Mass General and NYU proved months-long function possible. Yet grafts still fail from thrombotic microangiopathy and antibody-mediated injury, PERV transmission risk is theoretical but unquantified long-term, and the ethics of creating organ-donor animals remain contested. As of 2026 xenotransplantation is in early clinical trials, not practice.",
 "why_it_matters": "Over 100,000 Americans alone wait for organs; thousands die yearly waiting. A working pig-organ supply would end the shortage, end waitlist deaths, and make transplantation schedulable rather than a race against someone else's tragedy.",
 "sig_pointer": "The Signature system's proposed approach treats the pig organ as a platform requiring co-evolved compatibility, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that xenotransplantation stalls because edits are made to the pig while rejection is a conversation: each human immune pathway needs its pig-side counterpart tuned, in the right tissue, at the right level. "
  "Assumptions: (1) residual graft injury comes from many small incompatibilities, not one big one; (2) over-expressing human regulators can have pig-side side effects; (3) the coagulation incompatibility is as important as the immune one. "
  "Reasoning path: treating the donor genome as a compatibility platform - edited iteratively against measured human-response profiles - explains why single-antigen knockouts plateaued and predicts that the edit list must be tuned per organ. "
  "Proposed mechanism: 'conversation-mapped' editing where each pig organ's human incompatibility profile is measured ex vivo, edits are prioritized by measured contribution to injury, and the minimal sufficient edit set is validated before clinical use. "
  "What would confirm it: conversation-mapped grafts outperforming fixed-edit-list grafts in survival and injury markers in trials. "
  "What would kill it: evidence that residual injury is dominated by a single uneditable pathway, or that PERV or other safety barriers prove absolute. "
  "What this does not claim: it does not claim pig organs are ready for routine use, does not minimize zoonosis risk, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the pig organ as one side of an immune conversation, and asks what minimal edits would make the human side stop objecting.",
 "how_it_works": "Researchers study xenotransplantation through gene-edited pig production, ex vivo human blood perfusion of pig organs, nonhuman primate transplant models, decedent-recipient studies, and early living-patient trials under expanded access.",
 "key_points": [
  "Pig organs are the leading xenotransplant platform: size-matched, editable, breedable.",
  "Alpha-Gal knockout (2002) solved hyperacute rejection; CRISPR enabled multi-gene edits.",
  "2022-2024 pig heart and kidney transplants functioned for weeks to months.",
  "Thrombotic microangiopathy and antibody-mediated injury still limit grafts.",
  "PERV inactivation (2017) addressed retrovirus risk; long-term safety unproven.",
 ],
 "requirements": [
  "Edit sets that control coagulation as well as immunity, per organ.",
  "Long-term safety data on zoonosis and chronic rejection.",
  "Ethical and regulatory frameworks for organ-donor animals.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cooper DKC et al. Xenotransplantation: the transplantation of organs and tissues between species. 2nd ed. Springer; 2017.",
  "Griffith BP et al. Genetically modified pig heart transplanted into a human. New England Journal of Medicine. 2022;387:35-44.",
  "Niu D et al. Inactivation of porcine endogenous retrovirus in pigs using CRISPR-Cas9. Science. 2017;357:1303-1307.",
  "Montgomery RA et al. Results of two cases of pig-to-human kidney xenotransplantation. New England Journal of Medicine. 2022;386:1889-1898.",
 ],
 "demo_data": {"a": ("US organ waitlist, approximate thousands", 100.0),
               "b": ("pig gestation, months", 4.0), "bounds": (15.0, 40.0),
               "step1": "a hundred thousand wait while a pig gestates in months - the supply arithmetic favors xenotransplantation",
               "confirm": "conversation-mapped grafts outperform fixed-edit grafts in survival and injury markers",
               "refute": "residual injury proves dominated by a single uneditable pathway"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "nerve-regeneration",
 "name": "Functional Nerve Regeneration After Transection",
 "group": "Neurosurgery",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Cut a peripheral nerve and surgeons can sew it back - so why does function so often return incomplete, miswired, or painful?",
 "description": "Peripheral nerves can regenerate at roughly a millimeter a day, and microsurgical repair (epineurial or fascicular suturing) reconnects the stumps. Yet outcomes disappoint: motor recovery is partial, sensory return is distorted, and painful neuromas form. The biology conspires - regenerating axons must cross the repair site, find their original targets among thousands of possibilities, and do it before denervated muscle irreversibly atrophies (about 12-18 months).",
 "background": "Nerve repair began with 19th-century suturing; the operating microscope (1960s) and microsuture made fascicular repair possible. Seddon and Sunderland's classification of nerve injury grades still guides prognosis. Research attacked each bottleneck: nerve conduits and allografts to bridge gaps (avoiding donor-site cost of autografts), growth factors (NGF, GDNF), electrical stimulation to accelerate outgrowth (shown effective in rats by Gordon's group, with early human data), and processed nerve allografts. But the core problems - axonal misdirection (axons entering wrong fascicles), slow speed versus muscle atrophy deadlines, and neuroma formation - persist. As of 2026 no repair restores normal function after major mixed-nerve transection.",
 "why_it_matters": "Nerve injuries disable the young disproportionately - brachial plexus injuries from motorcycle crashes, battlefield trauma, industrial accidents. Incomplete recovery means lifelong disability; solving regeneration would restore hands, faces, and livelihoods.",
 "sig_pointer": "The Signature system's proposed approach treats the repair site as a guidance problem with a deadline, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nerve repair fails on two coupled variables - guidance accuracy and speed - and that fixing either alone is insufficient because misdirected fast growth is as useless as accurate slow growth. "
  "Assumptions: (1) axons follow local guidance cues that are scrambled at the repair site; (2) muscle atrophy sets a hard deadline around 12-18 months; (3) neuroma is regeneration without a target, a guidance failure mode. "
  "Reasoning path: reframing repair as 'accurate growth before the deadline' explains why conduits help gaps but not function, and why acceleration alone disappoints - both variables must move together. "
  "Proposed mechanism: a 'guided sprint' repair combining a patterned conduit that preserves fascicular topography with timed growth acceleration, so axons grow faster AND into the right channels before muscle expires. "
  "What would confirm it: guided-sprint repairs outperforming standard repair on both speed of reinnervation and accuracy of target matching in trials. "
  "What would kill it: evidence that misdirection is intrinsic to mammalian regeneration regardless of guidance, or that acceleration always trades against accuracy. "
  "What this does not claim: it does not claim normal function is restorable today, does not recommend any therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the severed nerve as a race between accurate regrowth and muscle expiration, and asks what would make axons both fast and faithful.",
 "how_it_works": "Surgeons and neuroscientists study regeneration in rodent transection models, conduit and allograft trials, electrical stimulation studies, and long-term functional outcome cohorts after plexus repair.",
 "key_points": [
  "Peripheral axons regenerate at roughly 1 mm per day.",
  "Denervated muscle irreversibly atrophies in about 12-18 months.",
  "Microsurgical repair reconnects stumps but axons misdirect into wrong targets.",
  "Conduits and allografts bridge gaps; they do not solve misdirection.",
  "Electrical stimulation accelerates outgrowth in animals with early human data.",
 ],
 "requirements": [
  "Guidance that preserves fascicular topography across the repair.",
  "Acceleration that does not trade accuracy for speed.",
  "Neuroma prevention by giving every axon a target.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sunderland S. Nerves and Nerve Injuries. 2nd ed. Churchill Livingstone; 1978.",
  "Gordon T et al. Electrical stimulation accelerates and increases expression of BDNF and trkB in regenerating axons. Journal of Neuroscience. 2009;29(9):2869-2881.",
  "Wiberg M, Terenghi G. Will it be possible to produce peripheral nerves? Surgical Technology International. 2003;11:303-310.",
  "Kuffler DP. The role of growth factors in nerve regeneration. Molecular Neurobiology. 1994;9:77-89.",
 ],
 "demo_data": {"a": ("axon regrowth speed, millimeters per day (approx)", 1.0),
               "b": ("muscle expiration deadline, months (approx)", 15.0), "bounds": (0.04, 0.12),
               "step1": "at a millimeter a day, a shoulder-to-hand regrowth barely beats the muscle deadline",
               "confirm": "guided-sprint repairs beat standard repair on speed and target accuracy together",
               "refute": "misdirection proves intrinsic to mammalian regeneration regardless of guidance"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "spinal-cord-repair",
 "name": "Surgical Repair of Spinal Cord Injury",
 "group": "Neurosurgery",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "The spinal cord does not heal like a cut nerve - why is central nervous system regeneration blocked, and can surgery ever reconnect a severed cord?",
 "description": "Spinal cord injury paralyzes by interrupting the cord's long tracts; unlike peripheral nerves, central axons essentially do not regenerate. The injured cord forms a glial scar rich in growth inhibitors (Nogo, MAG, OMgp, chondroitin sulfate proteoglycans), oligodendrocytes fail to remyelinate, and severed axons retract. Surgical decompression and stabilization prevent further damage but do not restore lost function, and every regenerative therapy has so far failed in humans.",
 "background": "Ramon y Cajal declared in 1928 that central pathways, once cut, do not regenerate - a dogma that stood for decades. Aguayo's 1980s experiments showed central axons CAN grow when given a peripheral nerve graft environment, proving the block is extrinsic, not intrinsic. That launched the inhibitor hunt: Schwab's Nogo-A, then MAG, OMgp, and CSPGs. Anti-Nogo antibodies, chondroitinase, stem cell transplants, and epidural stimulation have all shown signals in animals; human trials have been disappointing or modest (epidural stimulation restores some voluntary movement below the lesion in a few patients, but not regeneration). As of 2026 no therapy reconnects the injured human cord.",
 "why_it_matters": "Spinal cord injury strikes the young and lasts a lifetime: paralysis, loss of bowel/bladder/sexual function, pressure injuries, and shortened lifespan. Reconnection would be among the most transformative cures in all of medicine.",
 "sig_pointer": "The Signature system's proposed approach treats the lesion as an environment to be reprogrammed rather than a gap to be bridged, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cord repair fails because therapies address one inhibitor while the lesion presents a committee: scar, myelin debris, CSPGs, and missing trophic support act together, and removing any single one leaves the rest. "
  "Assumptions: (1) the inhibitory environment is redundant by design; (2) the therapeutic window extends months, not days, because the scar matures slowly; (3) reconnection requires guidance, not just disinhibition. "
  "Reasoning path: reframing the lesion as a redundant inhibitory environment explains the pattern of animal success and human failure - single-target drugs beat single-target models but lose to the real committee. "
  "Proposed mechanism: a staged 'environment reprogramming' combining scar modulation, multi-inhibitor blockade, trophic support, and patterned rehabilitation that trains whatever connections form - delivered as a coordinated program, not a single agent. "
  "What would confirm it: multi-target programs producing tract regrowth with functional correlation in models and early human signals beyond any single agent's effect. "
  "What would kill it: evidence that adult human central axons lack intrinsic growth capacity regardless of environment, or that the mature scar is truly irreversible. "
  "What this does not claim: it does not claim the cord can be reconnected today, offers no therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the lesion as a committee of inhibitors acting together, and asks what coordinated program would outvote them all.",
 "how_it_works": "Researchers study cord repair in contusion and transection models, inhibitor-knockout animals, stem cell and biomaterial trials, epidural and transcutaneous stimulation studies, and natural-history cohorts.",
 "key_points": [
  "Central axons do not spontaneously regenerate; peripheral axons do.",
  "Aguayo (1980s) proved the block is environmental, not intrinsic to the neuron.",
  "Inhibitors include Nogo-A, MAG, OMgp, and chondroitin sulfate proteoglycans.",
  "Epidural stimulation restores some voluntary movement in a few patients - modulation, not regeneration.",
  "No therapy has reconnected the injured human spinal cord.",
 ],
 "requirements": [
  "Multi-target strategies addressing the redundant inhibitory environment.",
  "Proof of true axonal regrowth with functional correlation, not just sprouting.",
  "Delivery that reaches the lesion without new damage.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ramon y Cajal S. Degeneration and Regeneration of the Nervous System. Oxford University Press; 1928.",
  "David S, Aguayo AJ. Axonal elongation into peripheral nervous system bridges after central nervous system injury in adult rats. Science. 1981;214:931-933.",
  "Schwab ME, Strittmatter SM. Nogo limits neural plasticity and recovery from injury. Current Opinion in Neurobiology. 2014;27:53-60.",
  "Angeli CA et al. Recovery of over-ground walking after chronic motor complete spinal cord injury. New England Journal of Medicine. 2018;379:1244-1250.",
 ],
 "demo_data": {"a": ("years since Cajal declared central regeneration impossible", 98.0),
               "b": ("inhibitory factors in the lesion committee (Nogo, MAG, OMgp, CSPGs)", 4.0), "bounds": (15.0, 35.0),
               "step1": "nearly a century after Cajal's verdict, the lesion's inhibitor committee still wins",
               "confirm": "multi-target programs produce tract regrowth with functional correlation",
               "refute": "adult human central axons prove intrinsically growth-incompetent regardless of environment"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "scarless-healing",
 "name": "Scarless Wound Healing in Adults",
 "group": "Regenerative Surgery",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "A fetus heals skin wounds without scars, but adults scar every time - what changes at birth, and can adult healing be switched back?",
 "description": "Mammalian fetuses heal cutaneous wounds scarlessly up to a gestational age threshold (around the third trimester in humans), regenerating normal dermal architecture including hair follicles. After the transition, every deep wound heals with fibrotic scar: collagen laid down in parallel bundles instead of the basket-weave of normal dermis, without appendages, weaker and less elastic. The switch correlates with the maturation of the inflammatory response, but its master regulators remain unidentified.",
 "background": "Scarless fetal healing was described in the 1970s-80s (Rowlatt; later Longaker's group at Stanford showed the transition timing precisely). Research implicated differences in TGF-beta isoforms (fetal wounds have more TGF-beta3, less TGF-beta1/2), hyaluronic acid richness, and a muted inflammatory response. This inspired anti-scarring trials: TGF-beta3 (avotermin/Juvista) reached phase 3 and failed; anti-CTGF and other antifibrotics have disappointed in skin. Meanwhile, oral mucosal wounds heal with minimal scarring in adults, offering a second natural model. As of 2026 the fetal-to-adult switch has no master regulator identified and no therapy reproduces scarless healing.",
 "why_it_matters": "Scars are not cosmetic trivia: burn scars contract joints and disfigure, surgical scars cause pain and restrict motion, and internal fibrosis (the same process) destroys organs in liver, lung, and kidney disease. Unlocking scarless healing would transform surgery, trauma, and burns - and illuminate fibrosis everywhere.",
 "sig_pointer": "The Signature system's proposed approach treats scarring as the default program that the fetus actively suppresses, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that scarless healing is not the absence of a program but an active suppression program that the fetus runs and the adult has lost - meaning the therapeutic goal is restoring suppression, not blocking healing. "
  "Assumptions: (1) the fetus actively maintains a pro-regenerative wound environment; (2) the adult default is fibrosis because suppression was developmentally switched off; (3) oral mucosa retains a partial suppression program, proving adults can run one. "
  "Reasoning path: if scarring is a lost suppression, single-molecule antifibrotics were bound to underwhelm - the target is the regulatory state of the wound, explaining both the fetal transition and why mucosa heals better. "
  "Proposed mechanism: a 'fetal-state induction' that reprograms the adult wound's regulatory environment (inflammatory profile, TGF-beta isoform balance, matrix composition) toward the fetal configuration for the critical first days. "
  "What would confirm it: induced fetal-state wounds regenerating appendages and basket-weave dermis in models, with transcriptomic convergence on fetal profiles. "
  "What would kill it: evidence that the fetal advantage is purely structural (e.g. sterile amniotic environment) with no reprogrammable regulatory state, or that adult cells cannot re-enter the fetal program. "
  "What this does not claim: it does not claim scarless healing is achievable today, offers no therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the scar as a suppression program switched off at birth, and asks what would switch it back on.",
 "how_it_works": "Researchers study scarless healing in fetal wound models across gestational ages, comparative transcriptomics of fetal versus adult wounds, oral mucosa as an adult low-scarring model, and antifibrotic clinical trials.",
 "key_points": [
  "Fetal skin heals scarlessly until the third trimester, regenerating follicles.",
  "Adult wounds heal with parallel-bundle collagen scar, weaker and inelastic.",
  "TGF-beta isoform balance and muted inflammation mark fetal healing.",
  "Avotermin (TGF-beta3) failed in phase 3; antifibrotics have disappointed.",
  "Oral mucosa heals with minimal scarring in adults - a second natural model.",
 ],
 "requirements": [
  "The master regulators of the fetal-to-adult healing switch.",
  "A way to induce the fetal regulatory state without impairing wound closure.",
  "Proof of true regeneration (appendages, architecture), not just flatter scars.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Longaker MT et al. Studies in fetal wound healing. Annals of Surgery. 1990;211(3):292-296.",
  "Ferguson MWJ, O'Kane S. Scar-free healing: from embryonic mechanisms to adult therapeutic intervention. Philosophical Transactions of the Royal Society B. 2004;359:839-850.",
  "So K et al. Avotermin for scar improvement following skin excisions. Plastic and Reconstructive Surgery. 2011;127:4S.",
  "Eming SA et al. Wound repair and regeneration: mechanisms, signaling, and translation. Science Translational Medicine. 2014;6(265):265sr6.",
 ],
 "demo_data": {"a": ("gestational weeks when human fetal healing turns scarring (approx)", 28.0),
               "b": ("weeks of human gestation (approx)", 40.0), "bounds": (0.6, 0.9),
               "step1": "the scarless window closes around the third trimester - a developmental switch, not a missing part",
               "confirm": "induced fetal-state wounds regenerate appendages with fetal transcriptomic profiles",
               "refute": "the fetal advantage proves purely environmental with no reprogrammable state"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "anastomotic-biology",
 "name": "The Biology of Anastomotic Healing",
 "group": "Gastrointestinal Surgery",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Skin wounds heal by well-mapped phases, but a bowel join heals under bacterial flood and mechanical load - what is the actual biology of anastomotic healing, and why is it so fragile?",
 "description": "An anastomosis must heal while bathed in intestinal contents, stretched by peristalsis, and relatively hypoxic at the cut edges. Unlike skin, its healing biology was long treated as a black box: surgeons optimized technique empirically while the cellular sequence - inflammation, proliferation, remodeling - at a leaking versus healing join remained unmapped. Recent work shows the anastomosis is immunologically distinct, but a complete biology is still missing.",
 "background": "For most of surgical history, anastomotic healing was assumed to mirror skin healing. The microbial dimension entered with Alverdy's work showing collagenase-producing bacteria degrade the join; the immunological dimension with studies of anastomotic macrophages differing from cutaneous wound macrophages. Oxygen tension at the anastomosis is lower than in skin wounds, collagen subtypes differ, and the microbiome shifts dramatically after bowel prep and antibiotics. Yet there is no accepted phase-map of anastomotic healing, no validated biomarker panel distinguishing the healing from the doomed join in the first 48 hours, and technique trials proceed largely without biological readouts. As of 2026 the biology remains fragmentary.",
 "why_it_matters": "Every leak-prevention strategy is shooting in the dark without the underlying biology: you cannot fix what you cannot map. A true biology of anastomotic healing would turn leak prevention from empirical tinkering into targeted therapy.",
 "sig_pointer": "The Signature system's proposed approach maps the anastomosis as a distinct healing organ with its own phase sequence, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the anastomosis is not a wound but a temporary organ: a structured, multi-tissue construct with its own phase sequence, immune profile, and failure modes, deserving the same systematic mapping that skin received. "
  "Assumptions: (1) anastomotic healing has discrete phases with distinct cellular actors; (2) the doomed join diverges from the healing join early, within 24-48 hours; (3) the divergence is detectable in wound fluid before it is visible to the surgeon. "
  "Reasoning path: treating the join as a mappable system explains why single-factor studies (perfusion alone, microbes alone) underperform - the phases interact, and the therapeutic targets are phase-specific. "
  "Proposed mechanism: a complete phase-map of anastomotic healing built from serial wound-fluid proteomics, single-cell profiling, and mechanical testing, yielding phase-specific interventions and a 48-hour divergence signature. "
  "What would confirm it: the divergence signature predicting leaks in prospective cohorts, and phase-matched interventions outperforming phase-blind ones. "
  "What would kill it: evidence that healing versus leaking joins are biologically indistinguishable until catastrophic failure, or that the phases are too patient-variable to map usefully. "
  "What this does not claim: it does not claim the map exists today, offers no therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the bowel join as an unmapped temporary organ, and asks what its phase sequence would reveal about failure.",
 "how_it_works": "Researchers study anastomotic biology with animal healing models, wound-fluid proteomics, single-cell RNA sequencing of the join, mechanical strength testing over time, and microbiome profiling.",
 "key_points": [
  "The anastomosis heals under bacterial load, stretch, and relative hypoxia.",
  "Its cellular phase sequence was never mapped the way skin healing was.",
  "Collagenase-producing microbes and distinct macrophage populations are implicated.",
  "No validated early biomarker distinguishes healing from doomed joins.",
  "Technique trials proceed largely without biological readouts.",
 ],
 "requirements": [
  "A complete phase-map of cellular and molecular events at the join.",
  "A 24-48 hour divergence signature predicting failure.",
  "Phase-specific interventions tested against phase-blind ones.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Alverdy JC et al. The gut microbiome and anastomotic leak. Nature Reviews Gastroenterology and Hepatology. 2017;14:673-683.",
  "Thompson SK et al. The anastomosis: a distinct wound healing environment. ANZ Journal of Surgery. 2006;76(5):341-345.",
  "Bosmans JWAM et al. Anastomotic healing and the gut microbiome. Techniques in Coloproctology. 2017;21:1-6.",
  "Eming SA et al. Wound repair and regeneration: mechanisms, signaling, and translation. Science Translational Medicine. 2014;6(265):265sr6.",
 ],
 "demo_data": {"a": ("hours when healing and doomed joins are hypothesized to diverge", 48.0),
               "b": ("hours in two days", 48.0), "bounds": (0.9, 1.1),
               "step1": "the fate of the join may be decided within the first two days - before any symptom",
               "confirm": "a divergence signature predicts leaks prospectively and phase-matched therapy wins",
               "refute": "healing and doomed joins prove indistinguishable until catastrophic failure"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "postoperative-delirium",
 "name": "Postoperative Delirium and Cognitive Dysfunction",
 "group": "Perioperative Care",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Elderly patients often emerge from successful surgery confused, and some never fully recover mentally - what does surgery and anesthesia do to the aging brain?",
 "description": "Postoperative delirium - acute confusion, inattention, and disorientation - strikes up to half of elderly patients after major surgery, especially hip fracture and cardiac operations. Most episodes resolve, but delirium predicts longer stays, institutionalization, dementia, and death. Beyond delirium lies postoperative cognitive dysfunction (POCD): subtler, longer-lasting deficits in memory and executive function whose very existence as a distinct entity remains debated.",
 "background": "Delirium was medicalized as a postoperative complication in the late 20th century (Inouye's confusion assessment method, 1990, gave it a measurable definition). The ISPOCD studies (1998 onward) documented cognitive dysfunction weeks to months after surgery, sparking fierce debate about whether anesthesia, surgery, or the underlying disease causes it. Inflammation emerged as the leading mechanism: surgical trauma releases cytokines that breach or signal across the blood-brain barrier, activating microglia (pioneering work by Maze and colleagues). Trials of dexmedetomidine, EEG-guided anesthesia depth, and anti-inflammatories show modest or inconsistent delirium reduction. As of 2026 no intervention reliably protects the aging brain, and whether POCD is real or residual delirium is still argued.",
 "why_it_matters": "Delirium is terrifying for families and dangerous for patients: it multiplies mortality risk and accelerates paths to dementia. With populations aging and surgery volumes rising, the cognitively safe operation is one of geriatric medicine's great needs.",
 "sig_pointer": "The Signature system's proposed approach treats delirium as a brain-immune communication failure with a prehabilitation window, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that delirium is the brain misreading the body's post-surgical immune signals: in the aging brain, microglia primed by years of low-grade inflammation overreact to the cytokine surge, producing a transient but sometimes scarring encephalopathy. "
  "Assumptions: (1) microglial priming varies between patients and is measurable; (2) the cytokine-to-brain signal has a dose-response for delirium; (3) the vulnerable window opens before incision, when priming could be calmed. "
  "Reasoning path: if delirium is primed-microglia overreaction, then prevention belongs before surgery (de-priming) rather than during it - explaining why intraoperative interventions underwhelm and why pre-existing cognitive vulnerability predicts delirium. "
  "Proposed mechanism: a 'brain prehabilitation' protocol that measures microglial priming, calms it preoperatively, and blunts the cytokine surge, with delirium as the primary endpoint. "
  "What would confirm it: prehabilitation protocols reducing delirium beyond current best care, with priming markers mediating the effect. "
  "What would kill it: evidence that delirium is driven by anesthetic drugs directly with no immune component, or that priming markers do not predict delirium. "
  "What this does not claim: it does not claim delirium is preventable today, does not recommend any drug, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads delirium as primed microglia overreacting to the surgical cytokine surge, and asks what pre-surgical calming would prevent.",
 "how_it_works": "Researchers study delirium through prospective cohorts with cognitive testing, CSF and blood biomarker studies, microglial PET imaging, animal models of surgery-induced neuroinflammation, and prevention trials.",
 "key_points": [
  "Delirium strikes up to half of elderly patients after major surgery.",
  "It predicts longer stays, institutionalization, dementia, and death.",
  "Neuroinflammation via primed microglia is the leading mechanism.",
  "The ISPOCD studies documented longer-term cognitive deficits after surgery.",
  "Whether POCD is distinct from residual delirium remains debated.",
 ],
 "requirements": [
  "A measurable marker of microglial priming before surgery.",
  "Prevention targeting the pre-incision window, proven in trials.",
  "Resolution of whether POCD is a real entity or prolonged delirium.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Inouye SK et al. Clarifying confusion: the confusion assessment method. Annals of Internal Medicine. 1990;113(12):941-948.",
  "Moller JT et al. Long-term postoperative cognitive dysfunction in the elderly: ISPOCD1 study. Lancet. 1998;351:857-861.",
  "Cerejeira J et al. The neuroinflammatory hypothesis of delirium. Acta Neuropathologica. 2010;119:737-754.",
  "Evered L et al. Postoperative cognitive dysfunction: nomenclature update. British Journal of Anaesthesia. 2018;121(5):1005-1006.",
 ],
 "demo_data": {"a": ("delirium rate after major surgery in the elderly, percent (upper range)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.6),
               "step1": "up to half of elderly patients emerge from major surgery acutely confused",
               "confirm": "prehabilitation protocols cut delirium with priming markers mediating the effect",
               "refute": "delirium proves driven by anesthetic drugs directly with no immune component"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "implant-biofilm",
 "name": "Biofilms on Surgical Implants",
 "group": "Implant Surgery",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Bacteria on an implant build fortresses that antibiotics cannot storm - why do biofilm infections defeat every drug, and how can implants be made uninhabitable for them?",
 "description": "A biofilm is a structured bacterial community encased in a self-made polymer matrix, adherent to a surface. On joint replacements, heart valves, and fracture hardware, biofilms cause infections that antibiotics cannot clear: bacteria inside are up to a thousand-fold more tolerant, and the only reliable cure is removing the implant. Periprosthetic joint infection complicates 1-2% of arthroplasties and its treatment - staged removal, spacers, months of antibiotics - is grueling.",
 "background": "Biofilms were characterized by Costerton in the 1970s-80s; their role in device infection was established by Gristina in the 1980s ('the race for the surface' between host cells and bacteria). The tolerance mechanisms - slow growth, persister cells, matrix diffusion barriers, quorum sensing - were mapped in the 1990s-2000s. Prevention strategies followed: antibiotic-loaded cement, silver and iodine coatings, hydrophilic surfaces. Results are partial: antibiotic cement helps in some settings, coatings have disappointed or raised toxicity concerns, and once a mature biofilm forms, salvage without removal remains rare. As of 2026 no surface reliably prevents biofilm, and no drug reliably eradicates mature biofilm on an implant.",
 "why_it_matters": "Millions of implants go in yearly and populations are aging into more of them: even 1-2% infection rates mean enormous suffering and cost. Solving biofilm would make implants nearly as safe as the day they are placed, for life.",
 "sig_pointer": "The Signature system's proposed approach treats the implant surface as territory in a race the host must win in hours, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that biofilm prevention is winnable only in the first hours: once host tissue integrates the surface ('the race for the surface' won by the host), bacteria cannot gain the foothold biofilm requires. "
  "Assumptions: (1) the decisive window is the first 6-12 hours after implantation; (2) mature biofilm is effectively unreachable, so all effort belongs pre-attachment; (3) surfaces can be engineered to favor host-cell adhesion over bacterial adhesion selectively. "
  "Reasoning path: reframing prevention as winning a timed race explains why antibiotic coatings (which fade) underperform and why rapid osseointegration correlates with low infection - the target is host victory in the window, not perpetual sterility. "
  "Proposed mechanism: 'race-winning' surfaces that actively recruit host cells in the first hours while presenting bacteria with anti-adhesive nanotopography, validated by time-to-integration versus time-to-colonization metrics. "
  "What would confirm it: surfaces whose host-integration speed predicts infection rates in trials, outperforming antibiotic-eluting designs. "
  "What would kill it: evidence that biofilms establish even on fully host-integrated surfaces, or that bacterial adhesion cannot be selectively disfavored without harming host cells. "
  "What this does not claim: it does not claim a coating ready for patients, does not claim mature biofilm is treatable, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the implant as territory in an hours-long race, and asks what surface would guarantee the host wins it.",
 "how_it_works": "Researchers study biofilms with in vitro flow-cell models, animal implant-infection models, retrieved-implant analysis, coating and surface-topography trials, and work on quorum-sensing inhibitors and phage therapy.",
 "key_points": [
  "Biofilm bacteria tolerate antibiotics up to ~1000-fold more than free bacteria.",
  "Periprosthetic joint infection complicates 1-2% of arthroplasties.",
  "Gristina's 'race for the surface' frames host versus bacterial colonization.",
  "Mature biofilm on an implant usually requires implant removal to cure.",
  "Coatings and antibiotic cement give partial protection at best.",
 ],
 "requirements": [
  "Surfaces that win the host-versus-bacteria race in the first hours.",
  "A therapy that eradicates mature biofilm without removing the implant.",
  "Diagnostics distinguishing biofilm infection from aseptic loosening.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Costerton JW et al. Microbial biofilms. Annual Review of Microbiology. 1995;49:711-745.",
  "Gristina AG. Biomaterial-centered infection: microbial adhesion versus tissue integration. Science. 1987;237:1588-1595.",
  "Zimmerli W et al. Prosthetic-joint infections. New England Journal of Medicine. 2004;351:1645-1654.",
  "Arciola CR et al. Biofilm formation in Staphylococcus implant infections. Nature Reviews Microbiology. 2018;16:397-409.",
 ],
 "demo_data": {"a": ("biofilm antibiotic tolerance multiplier (order of magnitude)", 1000.0),
               "b": ("tolerance of free-floating bacteria (baseline)", 1.0), "bounds": (100.0, 10000.0),
               "step1": "biofilm bacteria can be a thousand times harder to kill than free bacteria",
               "confirm": "host-integration speed predicts infection rates better than antibiotic elution",
               "refute": "biofilms prove able to establish even on fully host-integrated surfaces"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "mesh-complications",
 "name": "Mesh Complications in Hernia Repair",
 "group": "Implant Surgery",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Mesh made hernia repair durable - so why do some patients develop chronic pain, erosion, or recurrence years later, and which mesh belongs in which patient?",
 "description": "Synthetic mesh (usually polypropylene) revolutionized hernia repair after Lichtenstein's 1989 tension-free technique, cutting recurrence from double digits to low single digits. But mesh is a permanent foreign body: a minority of patients develop chronic groin pain, mesh infection, erosion into organs, or late recurrence. The 2010s saw mesh litigation, regulatory scrutiny, and a swing toward questioning mesh in some settings - yet the biology of who reacts badly remains unmapped.",
 "background": "Bassini's 1887 tissue repair ruled for a century with high recurrence; Usher's polypropylene mesh (1958) and Lichtenstein's technique (1989) made tension-free repair standard. Long-term follow-up then revealed the price: chronic pain in a meaningful minority (definitions vary, 5-15% with significant pain), meshoma, erosion, and difficult reoperations. Biologic meshes (acellular dermal matrix) were developed for contaminated fields but are costly and stretch over time. Lightweight and partially absorbable meshes aimed to reduce foreign-body reaction with mixed evidence. As of 2026 mesh selection - synthetic versus biologic, heavy versus light, plane of placement - rests on surgeon preference and weak evidence more than biology.",
 "why_it_matters": "Hernias are among the commonest operations on earth: millions of meshes go in yearly. Even small complication rates mean large absolute suffering, and chronic post-herniorrhaphy pain disables working-age people. Matching mesh to patient biology would keep the recurrence benefit while shedding the harm.",
 "sig_pointer": "The Signature system's proposed approach treats mesh reaction as a patient-specific foreign-body trajectory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that mesh complications are not random but the predictable end of divergent foreign-body trajectories: most patients encapsulate quietly, while a minority mount a progressive fibrotic or neuropathic response set in the first months. "
  "Assumptions: (1) the foreign-body trajectory is set early and is patient-specific; (2) chronic pain has both nociceptive (mesh-nerve interaction) and neuropathic components; (3) mesh properties interact with patient biology rather than acting alone. "
  "Reasoning path: reframing complications as trajectories makes them predictable from early markers and mesh-patient matching computable - explaining why the same mesh succeeds in one patient and tortures another. "
  "Proposed mechanism: a mesh-patient matching system combining preoperative foreign-body-response profiling with mesh property databases, plus early-trajectory monitoring to intervene before chronicity locks in. "
  "What would confirm it: matched mesh selection outperforming surgeon-choice on chronic pain and recurrence in trials, with early markers predicting trajectories. "
  "What would kill it: evidence that complications are dominated by technical factors (nerve handling, fixation) with mesh biology contributing little, or that trajectories are not predictable from early markers. "
  "What this does not claim: it does not claim a mesh recommendation for any patient, does not claim mesh is unsafe, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the mesh as a lifelong foreign-body relationship with divergent trajectories, and asks what early signal predicts which path.",
 "how_it_works": "Surgeons study mesh through long-term registries (notably Scandinavian hernia registries), randomized mesh-type trials, pain phenotyping studies, explant analysis, and litigation-driven safety reviews.",
 "key_points": [
  "Mesh cut hernia recurrence from double digits to low single digits.",
  "Chronic significant pain affects a meaningful minority after mesh repair.",
  "Mesh infection, erosion, and meshoma are rare but severe.",
  "Biologic meshes suit contaminated fields but are costly and stretch.",
  "Mesh choice rests more on surgeon preference than on patient biology.",
 ],
 "requirements": [
  "A predictor of who mounts a pathological foreign-body response.",
  "Mesh designs that integrate without chronic inflammation or nerve entrapment.",
  "Evidence-based mesh-patient matching rules.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lichtenstein IL et al. The tension-free hernioplasty. American Journal of Surgery. 1989;157(2):188-193.",
  "Burger JWP et al. Long-term follow-up of a randomized controlled trial of suture versus mesh repair of incisional hernia. Annals of Surgery. 2004;240(4):578-585.",
  "Kokotovic D et al. Chronic pain after mesh repair. Cochrane Database of Systematic Reviews. 2016;9:CD011322.",
  "Jenkins JT, O'Dwyer PJ. Inguinal hernias with meshes. BMJ. 2008;336:269-272.",
 ],
 "demo_data": {"a": ("chronic significant pain after mesh repair, percent (midpoint)", 10.0),
               "b": ("recurrence with mesh, percent (approx)", 3.0), "bounds": (2.0, 6.0),
               "step1": "mesh trades a small recurrence rate for a larger chronic-pain rate - an unsolved exchange",
               "confirm": "matched mesh selection beats surgeon-choice on pain and recurrence in trials",
               "refute": "complications prove dominated by technique with mesh biology contributing little"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "bariatric-mechanism",
 "name": "Why Bariatric Surgery Resolves Diabetes",
 "group": "Metabolic Surgery",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Diabetes often vanishes within days of gastric bypass - before any meaningful weight loss. What is the surgery actually doing to metabolism?",
 "description": "Roux-en-Y gastric bypass and sleeve gastrectomy resolve type 2 diabetes in a majority of patients, frequently within days - far too fast for weight loss to explain. Something about rerouting the gut rewires glucose metabolism immediately. Candidate mechanisms multiply: gut hormones (GLP-1, PYY), bile acid signaling, microbiome shifts, intestinal glucose uptake, vagal signaling - yet no unified account exists, and the effect varies by procedure and patient.",
 "background": "Bariatric surgery began for weight loss (Mason's gastric bypass, 1967); the diabetes remission was noticed as a side effect and became the main event. Pories et al. (1995) documented durable diabetes resolution after bypass. The STAMPEDE trial (Schauer et al., NEJM 2012, extended 2017) proved surgery beats intensive medical therapy for diabetes control. Mechanistic work implicated the incretin surge (GLP-1 rises sharply after bypass), altered bile acid pools activating FXR/TGR5, and microbiome transfer experiments in which post-bypass microbiota improved metabolism in recipients. Pharmaceutical GLP-1 agonists now mimic part of the effect - but not all of it. As of 2026 the full mechanism remains unassembled and no pill replicates surgery.",
 "why_it_matters": "Type 2 diabetes afflicts half a billion people; surgery is effective but invasive, costly, and scarce. Understanding its mechanism is the blueprint for a non-surgical cure - the most valuable mechanistic prize in metabolic medicine.",
 "sig_pointer": "The Signature system's proposed approach treats the rerouted gut as a reprogrammed endocrine organ, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that bariatric surgery works by reprogramming the gut's endocrine geography: rerouting nutrients changes which intestinal segments see food when, and each segment broadcasts a different hormonal program. "
  "Assumptions: (1) the intestine is a spatially programmed endocrine organ; (2) the diabetic state is partly maintained by the wrong program running (foregut-driven insulin resistance signals); (3) the speed of remission reflects signal switching, not tissue remodeling. "
  "Reasoning path: reframing surgery as endocrine reprogramming explains the days-scale remission, the procedure differences (bypass versus sleeve reroute differently), and why GLP-1 drugs capture only part of the effect. "
  "Proposed mechanism: a complete 'endocrine geography' map of the post-surgical gut - which segments broadcast what, when - identifying the minimal signal set that reproduces remission, as a blueprint for non-surgical mimicry. "
  "What would confirm it: the mapped signal set reproducing remission in models without anatomy change, and procedure comparisons tracking the map's predictions. "
  "What would kill it: evidence that remission is driven by caloric restriction alone in the early days, or that no signal set reproduces the effect without rerouting. "
  "What this does not claim: it does not claim a pill equivalent exists, does not recommend surgery for diabetes, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the rerouted gut as reprogrammed endocrine geography, and asks which broadcast signals carry the remission.",
 "how_it_works": "Researchers study the mechanism through procedure-comparison trials, gut hormone profiling, bile acid metabolomics, microbiome transfer experiments, vagal recordings, and pharmaceutical mimicry attempts.",
 "key_points": [
  "Diabetes remission often occurs within days of bypass, before weight loss.",
  "STAMPEDE proved surgery beats intensive medical therapy for diabetes.",
  "GLP-1 surges after bypass; bile acids and microbiome shift too.",
  "GLP-1 drugs mimic part of the effect but not all of it.",
  "No unified mechanism and no full non-surgical replication exist.",
 ],
 "requirements": [
  "A complete map of post-surgical gut endocrine signaling.",
  "Proof of which signals are causal versus correlated.",
  "A non-surgical intervention reproducing the full remission.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Pories WJ et al. Who would have thought it? An operation proves to be the most effective therapy for adult-onset diabetes mellitus. Annals of Surgery. 1995;222(3):339-352.",
  "Schauer PR et al. Bariatric surgery versus intensive medical therapy for diabetes (STAMPEDE). New England Journal of Medicine. 2012;367:433-442.",
  "Rubino F et al. Metabolic surgery and type 2 diabetes. Nature Reviews Endocrinology. 2016;12:267-280.",
  "Tremaroli V et al. Roux-en-Y gastric bypass and gut microbiota. Cell Host and Microbe. 2015;18(3):355-364.",
 ],
 "demo_data": {"a": ("days to diabetes remission after bypass (typical)", 7.0),
               "b": ("days to meaningful weight loss (typical)", 90.0), "bounds": (0.05, 0.15),
               "step1": "diabetes remits in days while weight loss takes months - the mechanism is not the weight",
               "confirm": "a mapped signal set reproduces remission without anatomy change",
               "refute": "remission proves driven by early caloric restriction alone"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "tumor-margins",
 "name": "Real-Time Tumor Margin Assessment",
 "group": "Surgical Oncology",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "The surgeon must remove all of the cancer and none of the healthy tissue - why is margin assessment still a frozen-section guess made while the patient waits?",
 "description": "A positive margin - cancer cells at the cut edge - predicts recurrence and often mandates reoperation, as in the roughly 20% of breast lumpectomies that return for re-excision. The current standard, frozen-section pathology, samples a fraction of the margin, takes 20-40 minutes, and is unavailable in many hospitals. The surgeon's eyes and fingers remain the primary margin instrument, and they cannot see microscopic disease.",
 "background": "Margin assessment has relied on palpation and frozen section since the early 20th century. The re-excision burden in breast conservation (about one in five) quantified the failure. Technologies emerged: intraoperative ultrasound, specimen radiography, radiofrequency spectroscopy (MarginProbe), fluorescence imaging (pegulicianine/Lumisight, FDA approved 2024 for breast lumpectomy), mass spectrometry (iKnife), and Raman spectroscopy. Each shows promise in trials; none is universal, real-time, and definitive across cancer types. As of 2026 the surgeon still largely guesses, waits, and sometimes reoperates.",
 "why_it_matters": "Positive margins mean recurrence, reoperation, worse survival, and enormous cost - while overly wide margins sacrifice function, appearance, and organs. Perfect margin assessment would maximize cure and minimize harm in every cancer operation.",
 "sig_pointer": "The Signature system's proposed approach treats the margin as a molecular boundary to be imaged, not a line to be guessed, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that margin assessment fails because it samples the boundary instead of imaging it: frozen section examines a fraction of the surface, so the miss rate is structural, not technical. "
  "Assumptions: (1) the tumor-host boundary has a molecular signature distinct from both; (2) the signature is detectable in vivo at microscopic resolution; (3) whole-surface imaging beats any sampling strategy regardless of sample quality. "
  "Reasoning path: reframing the problem as whole-boundary imaging explains why better sampling never solved it and predicts that only continuous in-vivo molecular imaging can - which is exactly where the successful technologies point. "
  "Proposed mechanism: a universal molecular-boundary imager combining tumor-agnostic contrast (metabolic, stromal, or immune signatures rather than tumor-specific markers) with real-time overlay on the surgical field. "
  "What would confirm it: whole-boundary imaging driving re-excision rates toward zero across cancer types in trials, with missed cancers proven absent on follow-up. "
  "What would kill it: evidence that tumor boundaries lack any consistent molecular signature across patients, or that in-vivo resolution cannot reach the single-cell level needed. "
  "What this does not claim: it does not claim such an imager exists today, endorses no device, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the margin as a molecular boundary awaiting whole-surface imaging, and asks what contrast would reveal it continuously.",
 "how_it_works": "Surgeons study margins through re-excision rate tracking, frozen-section accuracy studies, and trials of fluorescence, spectroscopy, mass spectrometry, and AI-assisted pathology.",
 "key_points": [
  "About 20% of breast lumpectomies require re-excision for positive margins.",
  "Frozen section samples a fraction of the margin and takes 20-40 minutes.",
  "Fluorescence agents (e.g. pegulicianine, FDA 2024) show real-time promise.",
  "Mass spec (iKnife) and Raman spectroscopy are investigational.",
  "No universal, real-time, definitive margin technology exists.",
 ],
 "requirements": [
  "Whole-boundary molecular imaging, not sampling.",
  "Tumor-agnostic contrast working across cancer types.",
  "Proof that imaging-guided margins improve survival, not just re-excision rates.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McCahill LE et al. Variability in reexcision following breast conservation surgery. JAMA. 2012;307(5):467-475.",
  "Smith BL et al. Pegulicianine fluorescence-guided surgery. NEJM Evidence. 2024 (INSECT/Lumicell trials).",
  "Balog J et al. Intraoperative tissue identification using rapid evaporative ionization mass spectrometry. Science Translational Medicine. 2013;5(194):194ra93.",
  "Taghian A et al. Margin assessment in breast cancer surgery. Annals of Surgical Oncology. 2017;24:2468-2476.",
 ],
 "demo_data": {"a": ("breast lumpectomy re-excision rate, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.25),
               "step1": "one in five breast cancer operations returns for re-excision - the margin guess fails openly",
               "confirm": "whole-boundary imaging drives re-excision toward zero across cancer types",
               "refute": "tumor boundaries prove to lack any consistent molecular signature"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "eye-transplantation",
 "name": "Whole-Eye Transplantation",
 "group": "Transplantation",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Corneas transplant routinely, but a whole eye never has - what would it take to transplant an eye and restore sight?",
 "description": "Corneal transplantation (over 100,000 yearly worldwide) works because the cornea is avascular and immune-privileged. A whole eye adds the retina, the optic nerve with its million-plus axons, and the ocular immune environment. In May 2024 surgeons at NYU performed the first whole-eye transplant combined with a face transplant; the eye survived with blood flow but vision was not restored - the optic nerve did not reconnect. The barrier is central nervous system regeneration, not surgical technique.",
 "background": "Corneal transplant dates to Zirm (1905) and is among medicine's most successful transplants. Whole-eye transplant was long considered impossible because the optic nerve is central nervous system tissue that does not regenerate. The 2024 NYU case (Rodriguez et al.) proved the plumbing possible: vascular anastomoses sustained the globe, and the retina showed electrical responses, but no purposeful vision resulted. Research directions include optic-nerve regeneration strategies borrowed from spinal cord work, stem-cell retinal repopulation, and brain-computer bypasses of the nerve entirely. As of 2026 the transplanted eye lives but does not see.",
 "why_it_matters": "Millions are blind from whole-globe disease - trauma, end-stage glaucoma, retinal destruction - for whom no current therapy offers sight. A seeing eye transplant would be the first cure for currently incurable blindness.",
 "sig_pointer": "The Signature system's proposed approach treats the optic nerve as a million-channel cable requiring guided reconnection, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that whole-eye transplant will succeed not through nerve regeneration alone but through a three-part strategy: preserve the donor retina's function, guide a fraction of axons to roughly correct targets, and let the brain's plasticity sort the rest. "
  "Assumptions: (1) the adult visual cortex retains enough plasticity to interpret imperfect input; (2) partial, topographically rough reconnection suffices for useful vision; (3) the donor retina can be kept viable through procurement and reperfusion. "
  "Reasoning path: if the brain can learn from noisy input - as cochlear implants prove for hearing - then the reconnection bar is lower than perfect wiring, reframing the problem from 'regrow a million axons precisely' to 'deliver a learnable signal.' "
  "Proposed mechanism: a 'learnable-signal' transplant combining optic-nerve guidance scaffolds, retinal viability preservation, and postoperative visual training protocols that teach the cortex to decode the novel input. "
  "What would confirm it: transplanted eyes producing measurable cortical responses that improve with training toward useful vision. "
  "What would kill it: evidence that the adult visual cortex cannot decode roughly-wired input, or that donor retinas cannot survive procurement. "
  "What this does not claim: it does not claim sight restoration is achievable today, offers no therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the optic nerve as a cable the brain could learn to decode, and asks how rough the wiring may be while still carrying sight.",
 "how_it_works": "Researchers study eye transplant through the 2024 NYU clinical case, optic-nerve regeneration models, retinal viability preservation, and visual-cortex plasticity studies including retinal-implant and sensory-substitution work.",
 "key_points": [
  "Corneal transplant is routine; whole-eye transplant was first done in 2024.",
  "The NYU eye survived with blood flow but did not restore vision.",
  "The optic nerve's million-plus axons are central nervous system tissue.",
  "Retinal electrical responses were detected without purposeful vision.",
  "Cochlear implants prove the brain can learn from rough artificial input.",
 ],
 "requirements": [
  "Optic-nerve axon guidance achieving topographically rough reconnection.",
  "Donor retina viability through procurement and reperfusion.",
  "Proof that cortex can decode the transplanted signal into useful vision.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rodriguez ED et al. First whole-eye and partial-face transplantation. NYU Langone reports; JAMA. 2024.",
  "Zirm E. Eine erfolgreiche totale Keratoplastik. Albrecht von Graefes Archiv fur Ophthalmologie. 1906;64:580-593.",
  "Benowitz LI et al. Optic nerve regeneration. Annual Review of Vision Science. 2017;3:301-323.",
  "Chichilnisky EJ. The neural basis of vision. Annual Review of Neuroscience. 2020;43:1-20.",
 ],
 "demo_data": {"a": ("optic nerve axons, approximate millions", 1.2),
               "b": ("cochlear implant electrodes (a learnable-signal precedent)", 22.0), "bounds": (0.03, 0.1),
               "step1": "the optic nerve carries over a million fibers - yet twenty-two electrodes taught brains to hear",
               "confirm": "transplanted eyes yield cortical responses improving with training toward useful vision",
               "refute": "the adult visual cortex proves unable to decode roughly-wired input"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "spinal-reconnection",
 "name": "Functional Spinal Cord Reconnection",
 "group": "Neurosurgery",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Sever the cord completely and function below is lost - is there any surgical path to true reconnection, or is the injured cord permanently unbridgeable?",
 "description": "Complete spinal cord transection - from trauma, tumor resection, or experimental models - leaves permanent paralysis below the lesion. Unlike peripheral nerve, the cord's severed tracts do not regrow across the gap. The 2010s saw controversial claims (notably Canavero's head-transplant proposals invoking cord fusion with polyethylene glycol) that mainstream neuroscience regards as unproven. The honest state: surgical reconnection of a severed human cord has never restored function.",
 "background": "Spinal cord transection models in animals showed the same inhibitory environment as contusion injuries, plus the added problem of a physical gap. Polyethylene glycol (PEG) as a membrane fusogen showed axon fusion in animal models (Bittner, 2010s), and was invoked in head-transplant proposals that never produced credible human evidence. Spinal cord stimulation restores some function by modulating surviving circuits, not by reconnection. Stem cell bridges, biomaterial scaffolds, and growth-factor cocktails each address part of the problem in animals. As of 2026 no approach has reconnected a severed cord with functional recovery in humans, and extraordinary claims in this space have repeatedly failed verification.",
 "why_it_matters": "Complete injuries are the most devastating spinal trauma: young patients, total dependence, shortened lives. Reconnection would be the single most dramatic surgical cure imaginable - and the field must distinguish real paths from spectacle.",
 "sig_pointer": "The Signature system's proposed approach treats reconnection as a bridge-plus-environment problem requiring both span and soil, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that reconnection needs two solved problems at once: a physical bridge that axons will cross, and a chemical environment that lets them keep going - and that all failures to date solved at most one. "
  "Assumptions: (1) the gap and the inhibitory environment are independent failure modes; (2) membrane fusion agents can seal cut axons but cannot guide them; (3) functional recovery needs only a fraction of tracts reconnected, topographically approximate. "
  "Reasoning path: separating span from soil explains why PEG fusion (span without soil) and inhibitor blockade (soil without span) each disappoint alone, and predicts only combined bridge-plus-environment strategies can work. "
  "Proposed mechanism: a 'living bridge' - a patterned biomaterial scaffold seeded with guidance cells and growth factors, implanted into a pharmacologically disinhibited lesion, followed by intensive patterned rehabilitation. "
  "What would confirm it: combined strategies producing tract continuity with correlated functional recovery in models, exceeding either component alone. "
  "What would kill it: evidence that severed central axons cannot be coaxed across any gap regardless of environment, or that fusion agents' effects are artifacts. "
  "What this does not claim: it does not claim reconnection is achievable today, endorses no experimental surgery, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the severed cord as needing both a bridge and welcoming soil, and asks what combined construct would supply both.",
 "how_it_works": "Researchers study reconnection in transection models, fusogen experiments, scaffold and stem-cell bridge trials, and stimulation studies - with strict attention to distinguishing regeneration from compensation.",
 "key_points": [
  "Complete transection causes permanent paralysis below the lesion.",
  "PEG membrane fusion works in animal models but has no credible human evidence.",
  "Head-transplant cord-fusion claims remain unverified by mainstream science.",
  "Stimulation modulates surviving circuits; it does not reconnect severed ones.",
  "No approach has restored function after human cord transection.",
 ],
 "requirements": [
  "A bridge axons will cross plus an environment that sustains growth.",
  "Proof of true reconnection, not compensatory plasticity.",
  "Verification standards that exclude spectacle from science.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bittner GD et al. Rapid morphological fusion of severed myelinated axons by polyethylene glycol. Journal of Neuroscience Research. 1986;15:127-136.",
  "Canavero S. HEAVEN: the head anastomosis venture project. Surgical Neurology International. 2013;4(Suppl 2):S335-S342.",
  "Courtine G et al. Transformation of nonfunctional spinal circuits into functional states. Nature Medicine. 2009;15:685-693.",
  "Tuszynski MH et al. Spinal cord injury: advances and challenges. Nature Reviews Neurology. 2022;18:657-670.",
 ],
 "demo_data": {"a": ("spinal tracts requiring reconnection for useful function (approx)", 5.0),
               "b": ("major ascending/descending tracts total (approx)", 30.0), "bounds": (0.1, 0.25),
               "step1": "only a fraction of the cord's tracts may need reconnection for useful recovery",
               "confirm": "combined bridge-plus-environment strategies beat either component alone with functional correlation",
               "refute": "severed central axons prove uncoaxable across any gap regardless of environment"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "uterus-transplant",
 "name": "Scaling Uterus Transplantation",
 "group": "Transplantation",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Uterus transplant has produced healthy babies - so why does it remain a rare experimental procedure instead of a routine infertility treatment?",
 "description": "Uterus transplantation treats absolute uterine factor infertility (absent or nonfunctional uterus, affecting roughly 1 in 500 women of childbearing age). After early failures, the Swedish team (Brannstrom) achieved the first live birth in 2014; by the mid-2020s dozens of babies had been born worldwide. Yet it remains confined to a handful of centers: the surgery is long and risky for donor and recipient, immunosuppression must cover pregnancy, and the graft is removed after childbearing - a transplant intended to be temporary.",
 "background": "Animal work in the 2000s established feasibility; the first human attempt (Saudi Arabia, 2000) failed from thrombosis. Brannstrom's Gothenburg program systematically solved the steps - living-donor procurement, vascular technique, immunosuppression compatible with pregnancy - culminating in the 2014 birth (Lancet). Deceased-donor programs followed (Cleveland Clinic, 2016). Robotic procurement reduced donor morbidity. But scale-up barriers persist: 10+ hour operations, donor risk (including living donors undergoing radical hysterectomy), rejection monitoring during pregnancy, preterm birth rates, and the ethics of a non-life-saving transplant requiring major surgery in healthy donors. As of 2026 it is a proven but boutique therapy.",
 "why_it_matters": "For women without a functioning uterus, transplant is the only path to carrying a pregnancy - surrogacy being unavailable or illegal in many places. Scaling it safely would convert a heroic exception into a real reproductive option.",
 "sig_pointer": "The Signature system's proposed approach treats the uterus as a temporary transplant whose temporariness is a design feature, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that uterus transplant's scalability problem is really a donor-surgery problem: the recipient operation is now reliable, but living-donor procurement remains formidably invasive. "
  "Assumptions: (1) recipient outcomes are already acceptable at expert centers; (2) donor morbidity is the rate-limiting harm; (3) deceased-donor supply cannot meet demand alone. "
  "Reasoning path: reframing scale-up around donor safety explains why the field advances through procurement innovation (robotics, deceased donors) rather than recipient technique, and predicts bioengineered uteri as the eventual solution. "
  "Proposed mechanism: a scale-up pathway through minimally invasive procurement plus expanded deceased-donor programs, converging on a bioengineered uterus (decellularized scaffold reseeded with recipient cells) that eliminates donor surgery and rejection together. "
  "What would confirm it: bioengineered uterine constructs supporting pregnancy in models, and procurement innovations cutting donor morbidity in trials. "
  "What would kill it: evidence that the uterus's complex vascular and muscular function cannot be bioengineered, or that rejection during pregnancy proves uncontrollable at scale. "
  "What this does not claim: it does not claim transplant is appropriate for any individual, offers no recommendation, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the uterus transplant as proven but donor-limited, and asks what would remove the donor from the equation.",
 "how_it_works": "Teams study uterus transplant through living-donor and deceased-donor programs, robotic procurement trials, pregnancy-outcome registries, and bioengineered uterus research in animals.",
 "key_points": [
  "First live birth after uterus transplant: Sweden, 2014 (Brannstrom).",
  "Dozens of babies born worldwide by the mid-2020s.",
  "The graft is temporary - removed after childbearing is complete.",
  "Living-donor procurement is a 10+ hour operation with real donor risk.",
  "Absolute uterine factor infertility affects roughly 1 in 500 women of childbearing age.",
 ],
 "requirements": [
  "Procurement with acceptable donor morbidity at scale.",
  "Rejection control compatible with healthy pregnancy.",
  "Long-term, a bioengineered uterus eliminating donor surgery.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brannstrom M et al. Livebirth after uterus transplantation. Lancet. 2015;385:607-616.",
  "Testa G et al. Deceased donor uterus transplantation. JAMA Surgery. 2018;153(11):e183344.",
  "Johannesson L, Järvholm S. Uterus transplantation: current progress and future prospects. Human Reproduction Update. 2016;22(1):121-133.",
  "Brannstrom M et al. Uterus transplantation: a rapidly expanding field. Fertility and Sterility. 2023;120(3 Pt 1):455-464.",
 ],
 "demo_data": {"a": ("women of childbearing age with absolute uterine factor infertility, per 500", 1.0),
               "b": ("women per 500 (scale)", 500.0), "bounds": (0.001, 0.004),
               "step1": "about one in five hundred women could need this option - rare individually, large in absolute numbers",
               "confirm": "bioengineered constructs support pregnancy and procurement morbidity falls in trials",
               "refute": "uterine function proves unbioengineerable or rejection uncontrollable at scale"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "bioartificial-organs",
 "name": "Implantable Bioartificial Organs",
 "group": "Regenerative Surgery",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Lab-grown tissues exist, but no lab-grown solid organ sustains a human - what stands between engineered tissue and a transplantable bioartificial organ?",
 "description": "Tissue engineering has produced skin, cartilage, and small hollow structures (notably Macchiarini-era trachea scaffolds, later discredited). But solid organs - liver, kidney, heart - need billions of cells, hierarchical vasculature down to capillaries, and integration with the host's blood, nerves, and immune system. Decellularized scaffolds reseeded with cells, 3D bioprinting, and organoids each solve part of the problem; none has produced a transplantable solid organ.",
 "background": "The field launched with Vacanti's ear on a mouse (1997) and Atala's engineered bladders (2006, Lancet). Decellularization - stripping a donor organ of cells while keeping its matrix (Ott's rat hearts, 2008, Nature Medicine) - offered scaffolds with native architecture; repopulating them with functional cells proved enormously harder. Bioprinting builds structures layer by layer but cannot yet print perfusable capillary beds. Organoids self-organize impressively but lack scale and vasculature. The Macchiarini trachea scandal (2010s) - patients died after synthetic scaffolds seeded with stem cells - set the field back and hardened standards. As of 2026 no bioartificial solid organ has functioned in a human.",
 "why_it_matters": "A working bioartificial organ - grown from the patient's own cells - would end both the organ shortage and rejection: the two fundamental limits of transplantation. It is the summit of regenerative medicine.",
 "sig_pointer": "The Signature system's proposed approach treats vascularization as the gating problem everything else waits on, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that bioartificial organs fail on vascularization first and everything else second: without a perfusable, hierarchical vascular tree, no cell mass survives, and all other challenges are downstream of that. "
  "Assumptions: (1) diffusion limits viable tissue thickness to ~200 micrometers without perfusion; (2) hierarchical branching cannot be printed directly at capillary scale today; (3) the host will vascularize an implant if given the right scaffold signals and time. "
  "Reasoning path: making vascularization the gating problem reorders the field's priorities - perfusion before parenchyma - explaining why cell-dense constructs keep dying at their cores and why pre-vascularized scaffolds outperform. "
  "Proposed mechanism: a 'vasculature-first' construction sequence - establish the perfusable tree in the scaffold, verify perfusion, then populate parenchyma - with in-vivo maturation doing the finest branching. "
  "What would confirm it: vasculature-first constructs sustaining thicker, more functional parenchyma than parenchyma-first builds in models. "
  "What would kill it: evidence that immune rejection of scaffolds or cell sourcing dominates even with perfect vasculature, or that hierarchical perfusion cannot be maintained in vivo. "
  "What this does not claim: it does not claim bioartificial organs are near, offers no therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the engineered organ as a plumbing problem first and a cell problem second, and asks what build order would satisfy the plumbing.",
 "how_it_works": "Researchers study bioartificial organs through decellularization-recellularization, bioprinting, organoid vascularization, and large-animal implantation of constructs.",
 "key_points": [
  "No bioartificial solid organ has functioned in a human.",
  "Diffusion limits unperfused tissue to about 200 micrometers thick.",
  "Decellularized scaffolds keep native architecture but resist repopulation.",
  "Bioprinting cannot yet print perfusable capillary beds.",
  "The Macchiarini trachea scandal hardened the field's standards.",
 ],
 "requirements": [
  "A perfusable hierarchical vascular tree in the construct.",
  "Cell sourcing at organ scale (billions of functional cells).",
  "Immune acceptance without lifelong suppression.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ott HC et al. Perfusion-decellularized matrix for whole-heart engineering. Nature Medicine. 2008;14:213-221.",
  "Atala A et al. Tissue-engineered autologous bladders for patients needing cystoplasty. Lancet. 2006;367:1241-1246.",
  "Murphy SV, Atala A. 3D bioprinting of tissues and organs. Nature Biotechnology. 2014;32:773-785.",
  "Takebe T et al. Vascularized and functional human liver from an iPSC-derived organ bud transplant. Nature. 2013;499:481-484.",
 ],
 "demo_data": {"a": ("diffusion limit for unperfused tissue, micrometers (approx)", 200.0),
               "b": ("liver thickness, millimeters (approx)", 150.0), "bounds": (0.8, 2.5),
               "step1": "unperfused tissue dies beyond a fifth of a millimeter - organs are a thousand times thicker",
               "confirm": "vasculature-first constructs sustain thicker functional parenchyma than parenchyma-first",
               "refute": "rejection or cell sourcing dominates even with perfect engineered vasculature"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "fetal-surgery",
 "name": "Expanding Fetal Surgery Safely",
 "group": "Fetal Surgery",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Operating on a fetus can cure disease before birth - but the womb must be opened to do it. How far can fetal surgery expand without the maternal risk outweighing the benefit?",
 "description": "Fetal surgery treats conditions like twin-twin transfusion syndrome (laser ablation), severe congenital diaphragmatic hernia (tracheal occlusion), and spina bifida (in-utero repair). The MOMS trial (Adzick et al., NEJM 2011) proved prenatal spina bifida repair improves outcomes versus postnatal repair - but at the cost of maternal morbidity: uterine dehiscence, preterm birth, and risks to future pregnancies. Every fetal operation is really two patients, and the healthy one assumes all the risk.",
 "background": "Fetal surgery began at UCSF in the 1980s (Harrison) with open procedures for hydronephrosis and diaphragmatic hernia. Fetoscopy enabled minimally invasive approaches: laser for twin-twin transfusion (De Lia, 1990s; Eurofetus trial proved benefit), and fetoscopic tracheal occlusion for CDH (TOTAL trials). The MOMS trial randomized spina bifida repair and showed halved shunt rates and improved motor function - but a third of mothers had uterine complications. As techniques moved fetoscopic, maternal risk fell but never vanished: membrane rupture and preterm birth remain the field's tax. As of 2026 indications are narrow, centers few, and each new indication must clear the two-patient ethical bar.",
 "why_it_matters": "For conditions like spina bifida, operating before birth changes a child's life trajectory: walking instead of wheelchair, fewer brain shunts. Expanding safe fetal surgery extends that promise to more congenital diseases - if maternal risk can be contained.",
 "sig_pointer": "The Signature system's proposed approach treats the uterus as an access problem to be minimized, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that fetal surgery's future is entirely about access trauma: the fetal therapy usually works, and the field's ceiling is set by what opening the uterus costs the mother. "
  "Assumptions: (1) fetal therapeutic efficacy is proven or provable for more conditions than currently treated; (2) maternal-fetal membrane injury is the dominant complication driver; (3) access trauma scales with instrument diameter and uterine manipulation. "
  "Reasoning path: reframing expansion as an access problem predicts the field grows through ever-smaller, ever-gentler entry - explaining why fetoscopy expanded indications faster than open technique ever could. "
  "Proposed mechanism: an 'access ladder' development program that qualifies each new indication only with a matched minimally invasive access method, plus membrane-sealing technologies that make entry nearly free. "
  "What would confirm it: new indications succeeding as access trauma falls, with membrane-seal technologies cutting preterm birth in trials. "
  "What would kill it: evidence that even minimal access carries irreducible membrane risk, capping expansion regardless of technique. "
  "What this does not claim: it does not claim any new indication is warranted today, offers no recommendation, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads fetal surgery as two patients sharing one incision, and asks what access would make the mother's share negligible.",
 "how_it_works": "Surgeons study fetal surgery through indication trials (MOMS, TOTAL, Eurofetus), fetoscopic technique development, membrane biology research, and maternal-fetal outcome registries.",
 "key_points": [
  "MOMS (2011) proved prenatal spina bifida repair beats postnatal repair.",
  "A third of MOMS mothers had uterine complications from open surgery.",
  "Fetoscopic laser treats twin-twin transfusion syndrome minimally invasively.",
  "Membrane rupture and preterm birth remain the field's core risks.",
  "Every fetal operation puts a healthy mother at risk for the fetus's benefit.",
 ],
 "requirements": [
  "Access methods with near-zero maternal-fetal membrane injury.",
  "Trial evidence for each new indication clearing the two-patient bar.",
  "Long-term follow-up of both children and mothers.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Adzick NS et al. A randomized trial of prenatal versus postnatal repair of myelomeningocele (MOMS). New England Journal of Medicine. 2011;364:993-1004.",
  "Senat MV et al. Endoscopic laser surgery versus serial amnioreduction for severe twin-to-twin transfusion syndrome (Eurofetus). New England Journal of Medicine. 2004;351:136-144.",
  "Deprest JA et al. Fetoscopic tracheal occlusion for severe congenital diaphragmatic hernia (TOTAL trials). Various; 2021.",
  "Harrison MR et al. Fetal surgery. American Journal of Obstetrics and Gynecology. 1982;143:331-335.",
 ],
 "demo_data": {"a": ("MOMS mothers with uterine complications, percent (approx)", 33.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.4),
               "step1": "a third of mothers paid a uterine price for the fetal benefit - the two-patient arithmetic",
               "confirm": "membrane-seal technologies cut preterm birth as new indications succeed",
               "refute": "even minimal access proves to carry irreducible membrane risk capping expansion"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "bci-longevity",
 "name": "Chronic Brain-Computer Interface Longevity",
 "group": "Neurosurgery",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Brain implants restore movement and speech - then slowly go silent as scar tissue chokes the electrodes. Why does the brain reject chronic interfaces, and how can they last decades?",
 "description": "Intracortical brain-computer interfaces (Utah arrays, Neuropixels) let paralyzed people control cursors, robotic arms, and speech decoders - until signal quality decays over months to years. The culprit is the foreign-body response: microglia and astrocytes encapsulate the stiff silicon shanks, neurons near the electrode die or retreat, and impedance rises. Every long-term human BCI study shows the same decay curve; no interface has lasted a decade at full fidelity.",
 "background": "The modern BCI era began with Kennedy's neurotrophic electrodes (1990s) and Donoghue's BrainGate trials (2006), decoding movement intent from motor cortex. Hochberg's group showed multi-year control; Willett's 2023-2024 speech-decoding work set accuracy records. But histology from explanted arrays consistently shows glial scarring and neuronal loss around shanks, and signal amplitude falls with a characteristic time course. Strategies - softer materials, smaller footprints (Neuralink's threads, Synchron's endovascular stentrode avoiding brain penetration entirely), anti-inflammatory coatings, adaptive decoders - each help partially. As of 2026 no chronic interface is proven to last decades, which is what a young paralyzed patient needs.",
 "why_it_matters": "A BCI that dies in five years condemns its user to repeated brain surgeries. Lifelong paralysis needs a lifelong interface: solving longevity converts BCIs from experiments into prostheses.",
 "sig_pointer": "The Signature system's proposed approach treats the electrode-tissue interface as a mechanical mismatch to be eliminated, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that BCI decay is fundamentally mechanical: stiff electrodes in soft, pulsing brain tissue cause chronic micromotion injury, and the scar is the brain's response to an unhealed wound that never stops moving. "
  "Assumptions: (1) mechanical mismatch dominates over chemical foreign-body signaling; (2) the brain's micromotion (cardiac and respiratory pulsation) is the persistent irritant; (3) an interface that moves with the tissue would not scar. "
  "Reasoning path: if mismatch is the driver, then softer, smaller, and untethered interfaces should decay slower - which matches the observed ranking of thread, mesh, and endovascular approaches - and the endpoint is an interface with zero mechanical footprint. "
  "Proposed mechanism: 'mechanically invisible' interfaces - ultra-compliant, untethered, subcellular-scale electrodes that ride tissue motion instead of resisting it - validated by decade-scale signal stability in models. "
  "What would confirm it: compliance-matched interfaces showing dramatically slower decay than stiff ones, with histology confirming minimal scarring. "
  "What would kill it: evidence that decay is dominated by electrochemical or biological factors independent of mechanics, with soft interfaces failing just as fast. "
  "What this does not claim: it does not claim any current device lasts decades, endorses no product, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads electrode decay as a wound that never stops moving, and asks what interface would be mechanically invisible.",
 "how_it_works": "Researchers study BCI longevity through explant histology, impedance and signal tracking in chronic implants, materials science of compliant electrodes, and adaptive decoding algorithms.",
 "key_points": [
  "Intracortical BCIs restore movement and speech decoding in paralyzed people.",
  "Signal quality decays over months to years in every long-term study.",
  "Glial scarring and neuronal loss around stiff shanks drive the decay.",
  "Softer threads, mesh electronics, and endovascular stentrodes aim to reduce mismatch.",
  "No chronic interface is proven to last decades.",
 ],
 "requirements": [
  "Interfaces with decade-scale signal stability in humans.",
  "Histological proof of minimal chronic tissue reaction.",
  "Decoders that adapt to slow signal drift without retraining burden.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hochberg LR et al. Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature. 2006;442:164-171.",
  "Willett FR et al. A high-performance speech neuroprosthesis. Nature. 2023;620:1031-1036.",
  "Polikov VS et al. Response of brain tissue to chronically implanted neural electrodes. Journal of Neuroscience Methods. 2005;148:1-18.",
  "Oxley TJ et al. Minimally invasive endovascular stent-electrode array (stentrode). Nature Biotechnology. 2016;34:320-327.",
 ],
 "demo_data": {"a": ("useful BCI signal lifetime, years (typical upper range)", 5.0),
               "b": ("lifetime needed by a young paralyzed patient, years", 50.0), "bounds": (0.06, 0.2),
               "step1": "implants fade in years while patients need decades - an order-of-magnitude longevity gap",
               "confirm": "compliance-matched interfaces show dramatically slower decay with minimal scarring",
               "refute": "soft interfaces prove to fail as fast as stiff ones, implicating non-mechanical decay"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "limb-regeneration",
 "name": "Regrowing Human Limbs",
 "group": "Regenerative Surgery",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "A salamander regrows a perfect limb; a human grows a stump. What blocks mammalian limb regeneration, and could surgery ever regrow an arm?",
 "description": "Salamanders regenerate complete limbs - bone, muscle, nerve, skin - through a blastema, a mass of dedifferentiated cells that rebuilds the structure with positional memory. Mammals form scar instead. Mice can regenerate digit tips (up to a point), and human children regrow fingertips similarly, but beyond that the program is absent. The difference is not missing genes - mammals have most of the same genes - but missing regulation.",
 "background": "Limb regeneration was studied since Spallanzani (1768); the blastema's properties were mapped in the 20th century (Thornton, Tassava). Key findings: nerves are required (denervated limbs do not regenerate), positional information is encoded in the blastema (Gardiner), and mammalian wound healing actively suppresses the program via rapid fibrosis. Digit-tip regeneration in mice (Borgens, Muneoka) proved mammals retain a fragment of the program. Recent work identified pro-regenerative signals (e.g. Lin28a enhancing repair in mice, Shyh-Chang 2013) and showed that modulating inflammation can shift healing toward regeneration. As of 2026 no intervention regrows a mammalian limb beyond the digit tip.",
 "why_it_matters": "Millions live with limb loss from trauma, diabetes, and war; prosthetics, however advanced, are not limbs. Regrowing the real thing would be the ultimate surgical achievement - and the program, once unlocked, would apply to every injured tissue.",
 "sig_pointer": "The Signature system's proposed approach treats regeneration as a suppressed program to be reactivated, not a missing capability, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that mammals did not lose regeneration but actively suppress it: rapid fibrotic healing outcompetes the slower blastema program because, in nature, fast closure beats perfect regrowth for survival. "
  "Assumptions: (1) the genetic toolkit for regeneration is largely present but silenced; (2) the suppression is executed by the early wound environment, especially inflammation and fibrosis speed; (3) reactivation requires both releasing suppression and providing patterning information. "
  "Reasoning path: if regeneration is suppressed rather than absent, the therapeutic sequence is suppress-the-suppressor then guide-the-pattern - explaining why single growth factors disappoint and why digit tips (small, slow to fibrose) still regenerate. "
  "Proposed mechanism: a staged 'program reactivation' - first reprogram the amputation wound environment away from rapid fibrosis toward blastema-permissive signaling, then supply positional cues and nerve-derived factors to organize regrowth. "
  "What would confirm it: staged reactivation producing patterned multi-tissue regrowth beyond the digit tip in mammals. "
  "What would kill it: evidence that the patterning information itself is lost in mammals (not just suppressed), or that blastema formation is impossible in adult mammalian tissue. "
  "What this does not claim: it does not claim limbs can be regrown today, offers no therapy, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the stump as a regeneration program outrun by scar, and asks what would slow the scar enough for the program to run.",
 "how_it_works": "Researchers study limb regeneration in salamander blastema biology, mouse digit-tip models, comparative genomics of regenerative versus fibrotic healing, and pro-regenerative factor screens.",
 "key_points": [
  "Salamanders regenerate complete limbs via a blastema with positional memory.",
  "Mammals regenerate digit tips but form scar beyond that.",
  "Nerves are required: denervated amphibian limbs do not regenerate.",
  "The gene toolkit is largely shared; the difference is regulation.",
  "No intervention regrows a mammalian limb beyond the digit tip.",
 ],
 "requirements": [
  "Identification of the mammalian suppression program's master switches.",
  "A way to hold the wound blastema-permissive without inviting infection.",
  "Positional patterning cues that rebuild correct anatomy, not just tissue.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brockes JP, Kumar A. Comparative aspects of animal regeneration. Annual Review of Cell and Developmental Biology. 2008;24:525-549.",
  "Muneoka K et al. Digit regeneration in mammals. Developmental Biology. 2008;318(2):239-247.",
  "Shyh-Chang N et al. Lin28 enhances tissue repair by reprogramming cellular metabolism. Cell. 2013;155(4):778-792.",
  "Gardiner DM et al. Regulation of retinoid signaling during limb regeneration. Developmental Biology. 1995;172:282-291.",
 ],
 "demo_data": {"a": ("salamander limb regrowth completeness, percent", 100.0),
               "b": ("fraction of limb mammals regrow, percent (digit tip only)", 2.0), "bounds": (20.0, 100.0),
               "step1": "the salamander regrows everything while mammals regrow nothing past the fingertip",
               "confirm": "staged reactivation yields patterned multi-tissue regrowth beyond the digit tip",
               "refute": "patterning information proves lost in mammals, not merely suppressed"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "metastasis-seeding",
 "name": "Preventing Tumor Seeding During Surgery",
 "group": "Surgical Oncology",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Surgery cures by removing cancer - but can the operation itself scatter cancer cells and seed metastases?",
 "description": "The 'no-touch' principle in cancer surgery is old: surgeons avoid squeezing tumors for fear of shedding cells into blood and lymph. Circulating tumor cells spike during operations; wound recurrences and port-site metastases after laparoscopy documented the risk. Yet whether surgical manipulation meaningfully changes long-term survival - versus cells that had already disseminated - remains unproven, and preventive strategies are empirical.",
 "background": "The seeding fear dates to the 19th century; Turnbull's no-touch colectomy technique (1960s) formalized caution. Laparoscopy's port-site metastases in the 1990s (initially alarming, later shown rare with technique) reignited the debate. Modern liquid-biopsy studies confirm circulating tumor DNA and cells rise intraoperatively, and animal models show surgical stress (catecholamines, inflammation, immunosuppression) can awaken dormant micrometastases. Perioperative trials - beta-blockers, anti-inflammatories, regional anesthesia - test whether blunting surgical stress improves cancer outcomes, with intriguing but inconclusive results. As of 2026 the contribution of surgical seeding to recurrence is real but unquantified.",
 "why_it_matters": "If surgical technique and perioperative care influence metastasis, then the operation is not just an excision but an oncologic intervention whose details affect survival. Getting this right could improve cure rates without any new drug.",
 "sig_pointer": "The Signature system's proposed approach treats the perioperative period as a metastatic window to be closed, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that surgery creates a transient metastatic window: shed cells meet a stressed, inflamed, immunosuppressed host, and the window's danger is the product of shedding rate times host vulnerability. "
  "Assumptions: (1) most shed cells die; the window matters because vulnerability is temporarily high; (2) vulnerability has measurable components (NK cell suppression, inflammation, catecholamines); (3) the window opens before incision (anxiety, fasting) and closes days later. "
  "Reasoning path: reframing risk as shedding-times-vulnerability explains why gentle technique alone disappoints - it addresses only one factor - and predicts combined shedding-reduction plus vulnerability-blunting will outperform either alone. "
  "Proposed mechanism: a 'window-closure' perioperative protocol minimizing shedding (no-touch technique, wound protection) while blunting vulnerability (stress and inflammation control), with circulating tumor DNA as the readout. "
  "What would confirm it: window-closure protocols reducing recurrence versus standard care in trials, with ctDNA dynamics mediating the effect. "
  "What would kill it: evidence that metastases are entirely predetermined before surgery, with perioperative events contributing nothing to outcomes. "
  "What this does not claim: it does not claim surgery spreads cancer in any individual case, recommends no drug, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the operation as opening a metastatic window, and asks what would close it faster than it opens.",
 "how_it_works": "Oncologic surgeons study seeding through circulating tumor cell/DNA monitoring, no-touch technique trials, perioperative beta-blocker and anti-inflammatory trials, and animal models of surgical stress and metastasis.",
 "key_points": [
  "Circulating tumor cells and DNA spike during cancer operations.",
  "Port-site metastases after laparoscopy proved seeding is possible but rare.",
  "Surgical stress suppresses NK cells and raises catecholamines in models.",
  "Perioperative beta-blocker/anti-inflammatory trials show intriguing signals.",
  "Whether surgical seeding changes survival remains unquantified.",
 ],
 "requirements": [
  "Quantification of surgery's contribution to recurrence versus pre-existing dissemination.",
  "A window-closure protocol proven in survival trials.",
  "Real-time shedding monitors to guide technique.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Tohme S et al. Surgery for cancer: a trigger for metastases. Cancer Research. 2017;77(7):1548-1552.",
  "Horowitz M et al. Exploiting the perioperative period to improve long-term cancer outcomes. Nature Reviews Clinical Oncology. 2015;12:213-226.",
  "Neeman E, Ben-Eliyahu S. Surgery and stress promote tumor metastasis. Nature Reviews Cancer. 2013;13:272-274.",
  "Turnbull RB et al. Cancer of the colon: the influence of the no-touch isolation technique. Annals of Surgery. 1967;166:420-427.",
 ],
 "demo_data": {"a": ("fold-rise in circulating tumor cells during operation (typical reported)", 10.0),
               "b": ("baseline (fold scale)", 1.0), "bounds": (5.0, 50.0),
               "step1": "tumor cells in blood can spike tenfold during the operation itself",
               "confirm": "window-closure protocols cut recurrence with ctDNA dynamics mediating the effect",
               "refute": "metastases prove entirely predetermined before surgery with perioperative events contributing nothing"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "brain-mapping",
 "name": "Limits of Awake Brain Mapping",
 "group": "Neurosurgery",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Awake craniotomy lets surgeons map language and movement while they resect - but what can mapping actually guarantee, and what eloquent function remains unmappable?",
 "description": "In awake brain surgery, direct electrical stimulation temporarily disrupts small cortical regions while the patient performs tasks, identifying critical language, motor, and sensory sites to preserve. Penfield pioneered the method in the 1930s-40s; modern series show it extends safe resection in gliomas. But stimulation maps what is tested, not what matters: higher cognition, personality, and network functions resist point-mapping, and negative mapping (no disruption found) does not prove safety.",
 "background": "Penfield and Boldrey's 1937 homunculus maps founded functional neurosurgery. Ojemann's work refined language mapping; the modern awake-craniotomy era (Berger, Duffau) demonstrated that stimulation-guided resection improves glioma outcomes. Yet limitations are structural: stimulation tests simple tasks, misses distributed networks, and cannot map functions like executive control or social cognition. Connectomics now shows the brain as networks, and Duffau's own hodotopical model argues function lives in networks, not points - which stimulation disrupts crudely. Intraoperative MRI, tractography, and soon brain-machine readouts supplement but do not replace the fundamental limit. As of 2026 surgeons map points while tumors invade networks.",
 "why_it_matters": "Brain tumor surgery trades survival against selfhood: resect too little and cancer remains; too much and the person is diminished. Mapping the unmappable - networks, cognition, personality - is the frontier of preserving who the patient is.",
 "sig_pointer": "The Signature system's proposed approach treats function as a network property to be mapped as networks, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that stimulation mapping is inherently point-based while function is network-based, and that the miss rate comes from this category error - not from insufficient stimulation points. "
  "Assumptions: (1) cognitive functions emerge from distributed networks, not cortical points; (2) disrupting a point tests the network crudely and incompletely; (3) network state can be read in real time with sufficient recording. "
  "Reasoning path: reframing mapping as network-state reading explains why more stimulation points yield diminishing returns and predicts that whole-network monitoring will outperform denser point mapping. "
  "Proposed mechanism: 'network-state mapping' that records distributed activity during tasks and resection, identifying when the network - not a point - approaches functional failure, guiding the resection margin. "
  "What would confirm it: network-state-guided resections preserving function better than point-mapping-guided ones in trials, with network metrics predicting deficits. "
  "What would kill it: evidence that point mapping already captures all mappable function, or that network states cannot be read fast enough to guide surgery. "
  "What this does not claim: it does not claim networks are fully mappable today, offers no clinical method, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the brain as networks being probed with point tools, and asks what whole-network reading would change.",
 "how_it_works": "Neurosurgeons study mapping through stimulation case series, connectomic tractography, intraoperative recording research, and outcome studies linking mapping extent to function and survival.",
 "key_points": [
  "Penfield's 1930s-40s stimulation work founded functional brain mapping.",
  "Awake mapping extends safe glioma resection (Duffau, Berger series).",
  "Stimulation maps tested points, not distributed networks.",
  "Negative mapping does not prove a region is safe to resect.",
  "Higher cognition and personality resist point-mapping entirely.",
 ],
 "requirements": [
  "Real-time network-state reading during resection.",
  "Proof that network guidance preserves function better than point mapping.",
  "Mapping methods for distributed cognitive functions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Penfield W, Boldrey E. Somatic motor and sensory representation in the cerebral cortex of man. Brain. 1937;60:389-443.",
  "Duffau H. Stimulation mapping of white matter tracts. Journal of Neurosurgery. 2008;109:886-894.",
  "Sanai N, Berger MS. Glioma extent of resection and its impact on patient outcome. Neurosurgery. 2008;62(4):753-766.",
  "Ojemann G et al. Cortical language localization in left, dominant hemisphere. Journal of Neurosurgery. 1989;71:316-326.",
 ],
 "demo_data": {"a": ("years since Penfield's cortical maps (1937)", 89.0),
               "b": ("mapping dimensions tested by classic stimulation (motor, sensory, language ~3)", 3.0), "bounds": (20.0, 40.0),
               "step1": "nearly ninety years of point-mapping still tests only a handful of functions",
               "confirm": "network-state guidance preserves function better than point mapping in trials",
               "refute": "point mapping proves to capture all mappable function with networks unreadable in real time"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "autonomous-surgery",
 "name": "Safe Autonomous Tissue Handling",
 "group": "Surgical Technology",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Robots already hold the camera and sew under supervision - but can a machine ever safely cut living tissue on its own, and what would prove it?",
 "description": "Surgical robots (notably the da Vinci system, FDA-cleared 2000) are master-slave tools: every motion comes from the surgeon. Supervised autonomy exists in narrow tasks - the STAR robot sutured bowel autonomously in pigs (Shademan et al., Science Robotics 2016), and TSolution One mills bone for knee replacements. But tissue deforms, bleeds, and varies; no system handles the unexpected, and the regulatory, ethical, and liability frameworks for autonomous cutting do not exist.",
 "background": "Surgical robotics began with PUMA 560 (1985, neurosurgical biopsy) and PROBOT; da Vinci's 2000 clearance made teleoperated surgery mainstream. Autonomy research progressed through levels: camera holding, then supervised subtasks (suturing, STAR 2016), with recent work on autonomous tissue manipulation using learning-based control. The hard problems are perception (deformable tissue tracking), safety guarantees (proving the robot will not cut the wrong thing), and the long tail of anatomical variation. Aviation's autopilot analogy misleads: the sky is structured, the abdomen is not. As of 2026 autonomy remains at supervised subtasks in research settings.",
 "why_it_matters": "Safe surgical autonomy could democratize expert-level surgery: every patient, everywhere, operated at the standard of the best human hands, without fatigue or tremor. It could also extend surgery to battlefields, space, and places with no surgeons - if safety can be proven, not just asserted.",
 "sig_pointer": "The Signature system's proposed approach treats surgical autonomy as a verification problem before a capability problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that surgical autonomy is blocked less by capability than by proof: regulators, surgeons, and patients need guarantees, not demos, and the field has no verification science for deformable-tissue autonomy. "
  "Assumptions: (1) perception of deformable tissue will keep improving; (2) the binding constraint is certifiable safety, not raw skill; (3) verification must cover the long tail of anatomy, not just standard cases. "
  "Reasoning path: reframing autonomy as verification-first explains why impressive demos do not advance regulation and predicts the winning systems will be those designed for provability - constrained, monitored, and formally verified. "
  "Proposed mechanism: a 'provable autonomy' stack with verified perception bounds, runtime monitors that halt on uncertainty, and formal safety proofs for each autonomous subtask before clinical deployment. "
  "What would confirm it: verified subtasks passing regulatory review and outperforming humans on safety metrics in trials. "
  "What would kill it: evidence that deformable-tissue perception has fundamental limits making verification impossible, or that the long tail of anatomy defeats any bounded guarantee. "
  "What this does not claim: it does not claim autonomous surgery is safe today, endorses no system, and makes no prediction about deployment timelines."),
 "sig_lens": "The Signature lens reads the robot as needing proof before permission, and asks what verification science would make autonomy certifiable.",
 "how_it_works": "Engineers study surgical autonomy through deformable-tissue tracking research, learning-based control, simulation environments, supervised-autonomy trials in animals, and formal methods for robotics safety.",
 "key_points": [
  "da Vinci (2000) is teleoperated: every motion comes from the surgeon.",
  "STAR sutured bowel autonomously in pigs (Science Robotics, 2016).",
  "Tissue deforms, bleeds, and varies - the long tail defeats current systems.",
  "No regulatory framework exists for autonomous cutting.",
  "The binding constraint may be provable safety, not capability.",
 ],
 "requirements": [
  "Perception that tracks deformable tissue reliably.",
  "Formal verification of safety for autonomous subtasks.",
  "Regulatory, ethical, and liability frameworks for machine cutting.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shademan A et al. Supervised autonomous robotic soft tissue surgery. Science Robotics. 2016;1(1):eaat9393.",
  "Marescaux J et al. Surgery without scars: report of transluminal cholecystectomy. Archives of Surgery. 2007;142:823-826.",
  "Fleming I et al. The da Vinci surgical system. Various FDA clearances; 2000.",
  "Yang GZ et al. Medical robotics: regulatory, ethical, and legal considerations. Science Robotics. 2017;2(8):eaam8638.",
 ],
 "demo_data": {"a": ("years of teleoperated da Vinci surgery (since 2000)", 26.0),
               "b": ("years per decade", 10.0), "bounds": (2.0, 3.0),
               "step1": "a quarter-century of surgical robotics, zero autonomous cutting in routine use",
               "confirm": "verified subtasks pass regulatory review and beat humans on safety metrics",
               "refute": "deformable-tissue perception proves to have fundamental limits defeating verification"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "cryopreservation",
 "name": "Vitrification and Revival of Whole Organs",
 "group": "Cryobiology",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Cells and embryos freeze and thaw routinely - so why can no whole organ be vitrified and revived, and what would organ banking change?",
 "description": "Vitrification - cooling so fast that water becomes glass instead of ice - preserves oocytes, embryos, and cell suspensions routinely. Scale defeats it: a kidney is billions of cells thick, cryoprotectants are toxic at the concentrations needed, cooling is uneven (cracking from thermal stress), and rewarming must be uniformly fast or ice nucleates. Frog and tardigrade natural cryoprotection hint it is possible; human organs remain impossible.",
 "background": "Cryobiology began with Polge's 1949 glycerol discovery for sperm; Mazur's two-factor hypothesis (1960s-70s) formalized freezing injury. Fahy's vitrification work (1980s-90s) showed ice-free cryopreservation was possible in principle; his group vitrified and revived a rabbit kidney in 2009 - the high-water mark, still not replicated at human scale. Nanowarming (using magnetic nanoparticles for uniform rewarming, Bischof's group, 2017) attacked the rewarming bottleneck. Cryoprotectant toxicity, cracking, and scale remain unsolved. As of 2026 whole human organs cannot be banked, and 'cryonics' revival claims remain outside science.",
 "why_it_matters": "Organ banking would end the geographic tyranny of transplantation: harvest anywhere, bank, match perfectly, transplant electively. It would also make the organ shortage a solvable logistics problem rather than a biological lottery.",
 "sig_pointer": "The Signature system's proposed approach treats the organ as a thermal system to be cooled and warmed uniformly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that organ cryopreservation fails on uniformity, not on cold: every bottleneck - toxicity, cracking, ice nucleation - is a gradient problem, and gradients are an engineering problem. "
  "Assumptions: (1) cryoprotectant toxicity is concentration-times-time, reducible by faster uniform loading; (2) cracking comes from thermal gradients, not from cold per se; (3) nanowarming can scale if particle distribution is uniform. "
  "Reasoning path: reframing all three bottlenecks as uniformity problems unifies the research program - perfuse uniformly, cool uniformly, warm uniformly - and explains why the rabbit kidney (small, uniform) worked where human organs fail. "
  "Proposed mechanism: a 'uniformity stack' combining vascular perfusion loading of low-toxicity protectants, electromagnetic uniform cooling, and nanowarming with verified particle distribution, validated stepwise from small to human-scale organs. "
  "What would confirm it: stepwise scale-up reviving progressively larger organs with function, tracking uniformity metrics. "
  "What would kill it: evidence of a fundamental size limit from cryoprotectant toxicity that uniformity cannot beat, or that ice nucleation is unavoidable at human scale. "
  "What this does not claim: it does not claim organs can be banked today, does not endorse cryonics revival claims, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the frozen organ as a uniformity problem wearing a cold disguise, and asks what would make every cell experience the same thermal history.",
 "how_it_works": "Cryobiologists study vitrification through protectant-toxicity assays, thermal modeling, nanowarming experiments, and stepwise scale-up from cells to small organs.",
 "key_points": [
  "Vitrification avoids ice by cooling water into glass.",
  "A rabbit kidney was vitrified and revived (Fahy, 2009) - the high-water mark.",
  "Nanowarming (2017) attacks the uniform-rewarming bottleneck.",
  "Toxicity, cracking, and scale block human organs.",
  "Cryonics revival claims remain outside science.",
 ],
 "requirements": [
  "Low-toxicity protectants loadable uniformly at human-organ scale.",
  "Cooling and rewarming uniform enough to avoid cracking and nucleation.",
  "Functional revival proven at human scale, not just small models.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fahy GM et al. Physical and biological aspects of renal vitrification. Organogenesis. 2009;5(3):167-175.",
  "Mazur P. Freezing of living cells: mechanisms and implications. American Journal of Physiology. 1984;247:C125-C142.",
  "Manuchehrabadi N et al. Improved tissue cryopreservation using inductive heating of magnetic nanoparticles. Science Translational Medicine. 2017;9(379):eaah4586.",
  "Polge C et al. Revival of spermatozoa after vitrification and dehydration at low temperatures. Nature. 1949;164:666.",
 ],
 "demo_data": {"a": ("rabbit kidney revived after vitrification (2009), count", 1.0),
               "b": ("vital transplantable organs per donor (approx)", 8.0), "bounds": (0.05, 0.25),
               "step1": "one rabbit kidney revived versus zero human organs banked - the scale gap is everything",
               "confirm": "stepwise scale-up revives progressively larger organs tracking uniformity metrics",
               "refute": "a fundamental toxicity size limit proves unbeatable by uniformity engineering"},
},
]



