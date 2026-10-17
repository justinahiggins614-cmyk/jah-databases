#!/usr/bin/env python3
"""Entries for the Nephrology field databases (field #41, taxonomy order).

Verified 2026-10-17: NO database covers nephrology as a clinical specialty
(the kidney - acute kidney injury, chronic kidney disease, glomerular
diseases, tubular disorders, electrolytes and acid-base, the kidney in
hypertension, dialysis, kidney transplantation, urinalysis). Clinical-
specialty framing, kidney-focused, distinct from urology (the surgical
specialty of the urinary tract - MISSING from the manifest entirely) and
from gastroenterology/hepatology/endocrinology.

Manifest search (2,382 databases): zero 'nephrolog*' slugs/names; no
db/nephrolog* dirs; zero 'kidney'/'dialysis'/'nephron'/'glomerul*'/
'transplant' slugs/names anywhere. Whole-system exact-title sweep over the
manifest PLUS all shard index 't' keys: zero collisions for all 34 planned
titles x2 editions (68 variants). NOTE: the persisted dedupe gate dir
(data/dedupe/exact) is stale for the newest fields, so the raw
manifest+shard sweep was the authoritative preflight. ZERO full-record
discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nephrology                 - The Nephrology Database
                               (public-harvest: real, fact-checked clinical
                               nephrology; standard references Skorecki et
                               al. "Brenner and Rector's The Kidney" 11th
                               ed 2020; Jameson et al. "Harrison's
                               Principles of Internal Medicine" 21st ed
                               2022; Daugirdas et al. "Handbook of Dialysis"
                               6th ed 2023; KDIGO AKI 2012, CKD 2024, BP
                               2021, GN 2021, Diabetes 2022 guidelines;
                               CKD-EPI 2021 eGFR; landmark papers as cited
                               per record)
  nephrology-signature       - The Nephrology Signature Database
                               (his original Signature interpretation of
                               the kidneys as the body's twin water-and-
                               salt treatment plants: glomeruli as the
                               filter cartridges, tubules as the refining
                               lines, the medulla as the concentration
                               tower, dialysis as the auxiliary treatment
                               plant; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-NEPH- (public) and JAH-NEPS- (signature). JAH-NEP- was
taken by 'neptune' and JAH-NPH- by 'nanophotonics'; JAH-NEPH-/JAH-NEPS-
verified free in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "the kidneys as the body's twin water-and-salt treatment plants: "
            "the glomeruli as the filter cartridges, the tubules as the "
            "refining lines, the medulla as the concentration tower, and "
            "dialysis as the auxiliary treatment plant built beside them. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_BRENNER = ("Skorecki K, Chertow GM, Marsden PA, Taal MW, Yu ASL, eds. "
               "Brenner and Rector's The Kidney. 11th ed. Elsevier; 2020.")
CIT_HARRISON = ("Jameson JL, Fauci AS, Kasper DL, Hauser SL, Longo DL, "
                "Loscalzo J, eds. Harrison's Principles of Internal Medicine. "
                "21st ed. McGraw Hill; 2022.")
CIT_DAUGIRDAS = ("Daugirdas JT, Blake PG, Ing TS. Handbook of Dialysis. "
                 "6th ed. Wolters Kluwer; 2023.")
CIT_KDIGO_AKI = ("Kidney Disease: Improving Global Outcomes (KDIGO) Acute "
                 "Kidney Injury Work Group. KDIGO clinical practice guideline "
                 "for acute kidney injury. Kidney Int Suppl. 2012;2:1-138.")
CIT_KDIGO_CKD = ("Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work "
                 "Group. KDIGO 2024 clinical practice guideline for the "
                 "evaluation and management of chronic kidney disease. Kidney "
                 "Int. 2024;105(4S):S117-S314.")
CIT_KDIGO_BP = ("Kidney Disease: Improving Global Outcomes (KDIGO) Blood "
                "Pressure Work Group. KDIGO 2021 clinical practice guideline "
                "for the management of blood pressure in chronic kidney "
                "disease. Kidney Int. 2021;99(3S):S1-S87.")
CIT_KDIGO_GN = ("Kidney Disease: Improving Global Outcomes (KDIGO) "
                "Glomerular Diseases Work Group. KDIGO 2021 clinical practice "
                "guideline for the management of glomerular diseases. Kidney "
                "Int. 2021;100(4S):S1-S276.")
CIT_KDIGO_DIAB = ("Kidney Disease: Improving Global Outcomes (KDIGO) Diabetes "
                  "Work Group. KDIGO 2022 clinical practice guideline for "
                  "diabetes management in chronic kidney disease. Kidney Int. "
                  "2022;102(4S):S1-S127.")
CIT_CKD_EPI = ("Inker LA, Eneanya ND, Coresh J, et al. New creatinine- and "
               "cystatin C-based equations to estimate GFR without race. "
               "N Engl J Med. 2021;385:1737-1749.")
CIT_LEVEY = ("Levey AS, Coresh J. Chronic kidney disease. Lancet. "
             "2012;379(9811):165-180.")
CIT_JHA = ("Jha V, Garcia-Garcia G, Iseki K, et al. Chronic kidney disease: "
           "global dimension and perspectives. Lancet. 2013;382(9888):260-272.")
CIT_COCKCROFT = ("Cockcroft DW, Gault MH. Prediction of creatinine clearance "
                 "from serum creatinine. Kidney Int. 1976;16:31-41.")
CIT_HIMMELFARB = ("Himmelfarb J, Ikizler TA. Hemodialysis. N Engl J Med. "
                  "2010;363:1833-1845.")
CIT_MOE = ("Moe S, Drueke T, Cunningham J, et al. Definition, evaluation, and "
           "classification of renal osteodystrophy: a position statement "
           "from Kidney Disease: Improving Global Outcomes (KDIGO). Kidney "
           "Int. 2006;69(11):1945-1953.")
CIT_ADROGUE = ("Adrogue HJ, Madias NE. Hyponatremia. N Engl J Med. "
               "2000;342:1581-1589.")
CIT_KRAUT = ("Kraut JA, Madias NE. Metabolic acidosis: pathophysiology, "
             "diagnosis and management. Nat Rev Nephrol. 2010;6:274-285.")
CIT_PALMER = ("Palmer BF. Regulation of potassium homeostasis. Clin J Am Soc "
              "Nephrol. 2015;10:1050-1060.")
CIT_GRANTHAM = ("Grantham JJ. Autosomal dominant polycystic kidney disease. "
                "N Engl J Med. 2008;359:1477-1485.")
CIT_KASISKE = ("Kasiske BL, Zeier MG, Chapman JR, et al. KDIGO clinical "
               "practice guideline for the care of kidney transplant "
               "recipients. Am J Transplant. 2009;9(Suppl 3):S1-S155.")
CIT_SIBAI = ("Sibai BM. Diagnosis and management of gestational hypertension "
             "and preeclampsia. Obstet Gynecol. 2003;102:181-192.")
CIT_MEHTA = ("Mehta RL, Kellum JA, Shah SV, et al. Acute Kidney Injury "
             "Network: report of an initiative to improve outcomes in acute "
             "kidney injury. Crit Care. 2007;11:R31.")
CIT_SCHWARTZ = ("Schwartz GJ, Munoz A, Schneider MF, et al. New equations to "
                "estimate GFR in children with CKD. J Am Soc Nephrol. "
                "2009;20:629-637.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Nephrology: The Clinical Specialty of the Kidney",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Nephrology is the clinical medical specialty devoted to the "
            "kidney - the organ that filters the blood, balances water and "
            "salts, manages acid-base chemistry, regulates blood pressure, "
            "and makes the hormones that drive red cell production and bone "
            "health. The name comes from the Greek nephros (kidney) and "
            "logos (study). The nephrologist is the physician who reads the "
            "kidney's gauges - creatinine, electrolytes, urine, blood "
            "pressure - and manages acute kidney injury, chronic kidney "
            "disease, glomerular diseases, electrolyte emergencies, "
            "hypertension, dialysis, and kidney transplantation. Each kidney "
            "holds about a million nephrons, and together the two filter "
            "roughly 180 liters of blood plasma every day at a normal "
            "glomerular filtration rate of about 125 milliliters per minute. "
            "Nearly all of that filtrate is reclaimed, so the final product "
            "is only 1 to 2 liters of urine. This record frames the "
            "discipline and the ladder of records that follows."
        ),
        "how_it_works": (
            "Nephrology works on the filter-plant model of the kidney. Blood "
            "enters each glomerulus under pressure, and about a fifth of the "
            "plasma is forced across the filtration barrier into the tubule - "
            "this is the glomerular filtration rate, the single number that "
            "defines kidney function. The tubules then reclaim what the body "
            "needs - water, sodium, glucose, amino acids - and secrete what "
            "it must discard - potassium, hydrogen ions, drugs, toxins. "
            "Hormones close the loops: ADH opens water channels, aldosterone "
            "trades sodium for potassium, parathyroid hormone handles calcium "
            "and phosphate, erythropoietin orders red cell production. The "
            "nephrologist reads the plant's instruments - creatinine for "
            "filtration, electrolytes for balance, the urine for protein and "
            "blood, blood pressure for volume - and intervenes with fluids, "
            "diuretics, electrolyte correction, immunosuppression, dialysis, "
            "or transplantation. The demo works the plant's scale arithmetic: "
            "daily filtrate from the GFR, per-nephron workload, and the "
            "reclamation fraction that turns 180 liters into under 2 liters "
            "of urine."
        ),
        "key_points": [
            "Nephrology = the clinical specialty of the kidney: filtration, fluid and electrolyte balance, acid-base, blood pressure, kidney hormones; AKI, CKD, glomerular disease, dialysis, transplantation.",
            "Two kidneys filter about 180 liters of plasma per day at a normal GFR near 125 mL/min, then reclaim about 99 percent of it.",
            "Each kidney contains roughly one million nephrons; each nephron handles about 90 microliters of filtrate per day.",
            "The kidney is also an endocrine organ: erythropoietin for red cells, activated vitamin D for bone, renin for blood pressure.",
            "Distinct from urology, the surgical specialty of the urinary tract: nephrology is the kidney's own medicine, medical and metabolic.",
        ],
        "requirements": [
            "The filter-plant picture: glomerulus, tubule, medulla, collecting duct.",
            "Scale literacy: GFR, daily filtrate, per-nephron workload, urine output.",
            "The instrument panel: creatinine, electrolytes, urinalysis, blood pressure.",
        ],
        "standards": [
            "Kidney function is stated as GFR in mL/min/1.73 m2; normal adult reference near 125.",
            "Quantities are adult averages with 'about' qualifiers since they vary by body size.",
            "Disease framing is diagnostic and management-oriented, matching the clinical-specialty scope.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON, CIT_LEVEY],
        "sig_lens": (
            "His Signature reading: the kidneys are the body's twin "
            "water-and-salt treatment plants - two identical facilities "
            "running around the clock, each with a million filter "
            "cartridges (the nephrons) pulling 180 liters of raw plasma a "
            "day off the blood's main line, refining it, and returning all "
            "but two liters. The nephrologist is the plant superintendent: "
            "watching the pressure gauges (blood pressure), testing the "
            "effluent (the urine), dosing the chemistry (electrolytes), and "
            "when a plant fails, wheeling in the auxiliary treatment unit - "
            "dialysis - or swapping in a donor plant entirely."
        ),
    },
    {
        "key": "nephron_anatomy",
        "name": "Kidney Anatomy and the Nephron: The Filtering Unit",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The kidney is a bean-shaped organ about 11 centimeters long "
            "sitting against the back wall of the abdomen, each wrapped in a "
            "fibrous capsule and fed by a renal artery that delivers about "
            "20 to 25 percent of the cardiac output - the richest blood "
            "supply per gram of any organ. Inside, the cortex holds the "
            "glomeruli and the medulla holds the loops of Henle and "
            "collecting ducts arranged in pyramids. The nephron is the "
            "functional unit: a glomerulus (the filter tuft) feeding a "
            "proximal tubule, a loop of Henle dipping into the medulla, a "
            "distal tubule, and a collecting duct shared with neighbors. "
            "Blood arrives through the afferent arteriole, filters across the "
            "glomerular basement membrane, and leaves through the efferent "
            "arteriole - two arterioles in series, which lets the kidney "
            "tune filtration pressure precisely. About two million nephrons "
            "total carry the whole 180-liter daily filtrate load, roughly 90 "
            "microliters per nephron per day."
        ),
        "how_it_works": (
            "Filtration happens in three layers: the fenestrated endothelium, "
            "the glomerular basement membrane, and the podocyte slit "
            "diaphragm - a sieve that passes water and small solutes but "
            "holds back cells and most protein. Pressure does the work: the "
            "afferent arteriole is wider than the efferent, so glomerular "
            "capillary pressure stays high (about 45 mmHg) and drives "
            "filtration. The filtrate then travels the tubule: the proximal "
            "tubule reclaims about two-thirds of the salt and water plus all "
            "the glucose; the loop of Henle builds the medullary salt "
            "gradient; the distal tubule and collecting duct fine-tune sodium, "
            "potassium, calcium, and water under hormonal control. What "
            "survives is urine. The demo divides the daily filtrate by the "
            "nephron count to show each unit's share, and works the "
            "two-arteriole pressure logic that makes filtration possible."
        ),
        "key_points": [
            "Each kidney: about 11 cm long, about one million nephrons, about 20-25 percent of cardiac output - the richest perfusion per gram in the body.",
            "The nephron = glomerulus + proximal tubule + loop of Henle + distal tubule + collecting duct.",
            "The glomerular filter has three layers: fenestrated endothelium, basement membrane, podocyte slit diaphragm.",
            "Two arterioles in series (afferent wider than efferent) hold glomerular pressure near 45 mmHg and drive filtration.",
            "Total nephron count about two million; each handles roughly 90 microliters of filtrate per day.",
        ],
        "requirements": [
            "Anatomy vocabulary: cortex, medulla, pyramid, capsule, hilum, ureter.",
            "The nephron segment order and what each segment mainly does.",
            "The three-layer filtration barrier and what each layer excludes.",
        ],
        "standards": [
            "Anatomical terms follow standard clinical usage (glomerulus, proximal convoluted tubule, loop of Henle).",
            "Counts and flows stated as adult averages with 'about' qualifiers.",
            "Pressures given in mmHg with the physiological mechanism, not just the number.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: each kidney is a treatment plant the "
            "size of a fist, and the nephron is its filter cartridge - two "
            "million cartridges online, each one a three-stage sieve (coarse "
            "mesh, fine membrane, podocyte fingers) fed by a pressure valve "
            "pair. The afferent valve opens wide, the efferent valve pinches "
            "down, and the pressure between them - 45 millimeters of mercury "
            "of pure push - rams plasma water through the sieve. Downstream "
            "of every cartridge runs a refining line (the tubule) that "
            "steals back everything valuable before the effluent leaves."
        ),
    },
    {
        "key": "gfr_filter",
        "name": "Glomerular Filtration: How the Kidney Filters Blood",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Glomerular filtration is the bulk movement of protein-free "
            "plasma across the glomerular barrier into Bowman's space, "
            "driven by hydrostatic pressure. The glomerular filtration rate "
            "(GFR) - the volume filtered per minute, normalized to body "
            "surface area - is the defining number of nephrology: normal is "
            "about 90 to 120 mL/min/1.73 m2 in young adults, and staging of "
            "chronic kidney disease is built entirely on GFR bands. Renal "
            "plasma flow is about 600 mL/min, so the filtration fraction - "
            "the share of arriving plasma that gets filtered - is about 125 "
            "divided by 600, roughly 20 percent. At 125 mL/min the daily "
            "filtrate is 180 liters: the entire plasma volume filtered about "
            "60 times per day. Autoregulation holds GFR steady across a wide "
            "range of blood pressures through the myogenic response and "
            "tubuloglomerular feedback at the macula densa."
        ),
        "how_it_works": (
            "Filtration is governed by Starling forces across the capillary "
            "wall: glomerular hydrostatic pressure (about 45 mmHg pushing "
            "out) minus Bowman's space pressure (about 10 mmHg) minus plasma "
            "oncotic pressure (about 25 mmHg pulling back) leaves a net "
            "filtration pressure near 10 mmHg. Multiply by the filtration "
            "coefficient of all two million glomeruli and you get the GFR. "
            "Autoregulation protects it: when arterial pressure rises, the "
            "afferent arteriole constricts (myogenic response); when distal "
            "tubule salt delivery rises, the macula densa signals the "
            "afferent arteriole to constrict (tubuloglomerular feedback), "
            "with adenosine and ATP as messengers. Angiotensin II preferentially "
            "constricts the efferent arteriole, defending filtration pressure "
            "when perfusion falls. The demo works the Starling arithmetic "
            "and the filtration fraction: 125 of 600 mL/min, about 20 "
            "percent, yielding 180 liters a day."
        ),
        "key_points": [
            "GFR is the defining number of nephrology: normal young-adult reference about 90-120 mL/min/1.73 m2; CKD staging is built on GFR bands.",
            "Net filtration pressure is about 10 mmHg: 45 (glomerular hydrostatic) minus 10 (Bowman space) minus 25 (oncotic).",
            "Filtration fraction is about 20 percent: 125 mL/min filtered of 600 mL/min renal plasma flow.",
            "Daily filtrate is about 180 liters: the whole plasma volume filtered roughly 60 times per day.",
            "Autoregulation (myogenic response + tubuloglomerular feedback) holds GFR steady across a wide blood pressure range.",
        ],
        "requirements": [
            "The Starling forces across the glomerular wall and their approximate values.",
            "Filtration fraction arithmetic: GFR divided by renal plasma flow.",
            "The two autoregulation mechanisms and where the macula densa sits.",
        ],
        "standards": [
            "GFR reported in mL/min/1.73 m2 when normalized; pressures in mmHg.",
            "Physiologic values given as ranges with 'about' qualifiers.",
            "Mechanisms named with their mediators (adenosine/ATP for tubuloglomerular feedback).",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: filtration is the plant's intake pump - "
            "60 full passes of the entire plasma pool every day through two "
            "million cartridges, driven by 10 millimeters of mercury of net "
            "push. The plant protects its intake rate fiercely: pressure "
            "sensors in the afferent valves (the myogenic response) and salt "
            "sensors downstream (the macula densa) throttle the valves to "
            "hold flow steady whether the supply pressure surges or sags. "
            "Angiotensin II is the emergency override - it pinches the "
            "outlet valve to keep the cartridges pressurized when the supply "
            "runs thin."
        ),
    },
    {
        "key": "tubule",
        "name": "The Renal Tubule: Reabsorption and Secretion",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "If the glomerulus is the filter, the tubule is the refinery: of "
            "the 180 liters filtered daily, about 178 to 179 liters are "
            "reabsorbed and only 1 to 2 liters leave as urine. The proximal "
            "tubule does the heavy lifting, reclaiming about two-thirds of "
            "the filtered sodium and water and essentially all of the "
            "glucose and amino acids through sodium-coupled transport. The "
            "filtered sodium load is enormous - 180 liters times 140 mmol "
            "per liter, about 25,200 mmol per day - yet only around 100 mmol "
            "is excreted, so over 99 percent is reclaimed. Secretion runs "
            "the other direction: the tubule adds potassium, hydrogen ions, "
            "organic acids, drugs, and toxins to the tubular fluid for "
            "disposal. Every segment has signature transporters - NHE3 and "
            "SGLT2 proximally, NKCC2 in the thick ascending limb, NCC "
            "distally, ENaC and ROMK in the collecting duct - and every "
            "major diuretic works by blocking one of them."
        ),
        "how_it_works": (
            "Reabsorption is mostly sodium-driven. The basolateral "
            "Na+/K+-ATPase pumps sodium out of the tubule cell into the "
            "blood, keeping intracellular sodium low; apical transporters "
            "then let sodium rush back in, dragging glucose (SGLT2), amino "
            "acids, phosphate, and water with it. In the thick ascending "
            "limb, NKCC2 moves one sodium, one potassium, and two chlorides - "
            "blocked by loop diuretics. In the distal convoluted tubule, NCC "
            "moves sodium and chloride - blocked by thiazides. In the "
            "collecting duct, ENaC takes sodium and creates the electrical "
            "gradient that drives potassium out through ROMK and hydrogen "
            "through H+-ATPase - blocked by amiloride and spironolactone's "
            "target aldosterone. Secretion uses organic anion and cation "
            "transporters (OATs, OCTs) to clear drugs like penicillin and "
            "toxins. The demo works the sodium mass balance: 25,200 mmol "
            "filtered, about 100 mmol excreted, over 99 percent reclaimed."
        ),
        "key_points": [
            "The tubule reclaims about 99 percent of the 180-liter filtrate; final urine is only 1-2 liters per day.",
            "Filtered sodium load is about 25,200 mmol/day; excretion is about 100 mmol/day - over 99 percent reclaimed.",
            "Segment transporters: NHE3/SGLT2 (proximal), NKCC2 (thick ascending limb), NCC (distal), ENaC/ROMK (collecting duct).",
            "Every major diuretic blocks one transporter: loops block NKCC2, thiazides block NCC, amiloride blocks ENaC.",
            "Secretion clears potassium, hydrogen ions, drugs, and toxins via OAT/OCT transporters.",
        ],
        "requirements": [
            "The tubule segment order and each segment's main transporter.",
            "The sodium mass-balance arithmetic (filtered load vs excretion).",
            "Which diuretic blocks which transporter.",
        ],
        "standards": [
            "Transporter names in standard form (NKCC2, NCC, ENaC, SGLT2, NHE3, ROMK).",
            "Daily loads computed from GFR times plasma concentration.",
            "Diuretic-transporter pairings stated as the mechanism of action.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: downstream of every filter cartridge "
            "runs a reclaim line a mile long in miniature. The first station "
            "(proximal tubule) grabs two-thirds of everything - salt, water, "
            "every last molecule of glucose. Each later station has one "
            "specialty valve: NKCC2, NCC, ENaC. The diuretics are valve "
            "wrenches - loop diuretics jam NKCC2 open-drain, thiazides jam "
            "NCC, spironolactone cuts the aldosterone signal wire. Of 25,200 "
            "millimoles of sodium a day rolling down the line, the plant "
            "keeps all but about 100. That is 99.6 percent recovery - no "
            "human refinery on earth runs that tight."
        ),
    },
    {
        "key": "countercurrent",
        "name": "Concentration and Dilution: The Countercurrent Multiplier",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The kidney can make urine as dilute as about 50 mOsm/kg or as "
            "concentrated as about 1,200 mOsm/kg - a 24-fold range - using "
            "the countercurrent multiplier of the loop of Henle. The thick "
            "ascending limb pumps salt out (via NKCC2) but is impermeable to "
            "water, so the medullary interstitium grows progressively saltier "
            "toward the papilla: about 300 mOsm/kg at the cortex, rising to "
            "about 1,200 at the tip. The descending limb and collecting duct "
            "are water-permeable, so tubular fluid equilibrates with whatever "
            "surrounds it. Antidiuretic hormone (ADH, vasopressin) is the "
            "master switch: when plasma osmolarity rises above about 285 "
            "mOsm/kg, ADH inserts aquaporin-2 water channels into the "
            "collecting duct and water follows the salt out, concentrating "
            "the urine. Without ADH, the channels are withdrawn and large "
            "volumes of dilute urine pour out. The concentrating limit sets "
            "the minimum urine volume: excreting the day's roughly 800 mOsm "
            "of solute at 1,200 mOsm/kg needs about 0.67 liters."
        ),
        "how_it_works": (
            "The multiplier works by countercurrent flow: fluid descends the "
            "thin limb losing water to the salty medulla, then ascends the "
            "thick limb where NKCC2 pumps salt out but water cannot follow. "
            "Each pass multiplies the gradient - the 'single effect' of "
            "about 200 mOsm/kg per level stacks from cortex to papilla. Urea "
            "recycling adds roughly half the medullary osmolarity. ADH, "
            "released from the posterior pituitary when osmoreceptors sense "
            "rising plasma osmolarity or baroreceptors sense falling volume, "
            "binds V2 receptors and inserts aquaporin-2 channels: water "
            "leaves the collecting duct into the salty medulla, and urine "
            "osmolarity climbs toward 1,200. Loop diuretics flatten the "
            "gradient by blocking NKCC2 - which is why they impair "
            "concentrating ability. The demo computes the minimum obligatory "
            "urine volume from the daily solute load and the 1,200 ceiling."
        ),
        "key_points": [
            "The kidney spans about 50 to 1,200 mOsm/kg of urine concentration - a 24-fold range.",
            "The medullary gradient runs about 300 (cortex) to 1,200 (papilla) mOsm/kg, built by NKCC2 in the water-impermeable thick ascending limb.",
            "ADH is the master switch: high ADH inserts aquaporin-2 channels and concentrates; low ADH dumps dilute urine.",
            "Osmoreceptors trigger ADH above about 285 mOsm/kg plasma osmolarity.",
            "Minimum urine volume is about 0.67 L/day: 800 mOsm of solute at the 1,200 ceiling.",
        ],
        "requirements": [
            "The loop segment permeabilities (which limbs pass water, which pass salt).",
            "The ADH-aquaporin-2 mechanism and its trigger threshold.",
            "The obligatory-volume arithmetic from solute load and max osmolarity.",
        ],
        "standards": [
            "Osmolarity in mOsm/kg water; volumes in liters per day.",
            "Transporter and channel names in standard form (NKCC2, aquaporin-2, V2 receptor).",
            "Gradient values stated as cortex-to-papilla ranges.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the medulla is the plant's concentration "
            "tower - a salt gradient stacked floor by floor from 300 at the "
            "roof to 1,200 at the basement, built by pumps that move salt "
            "but refuse water. The collecting ducts run down through the "
            "tower like pipes with adjustable walls: ADH is the valve "
            "handle, and when the control room (the pituitary) turns it, "
            "aquaporin hatches open and water drains out of the pipes into "
            "the salty tower. No ADH, hatches shut, and the plant floods "
            "dilute effluent. The tower's physics sets a hard floor: about "
            "two-thirds of a liter a day minimum, or the day's salt has "
            "nowhere to go."
        ),
    },
    {
        "key": "tbw",
        "name": "Total Body Water: Fluid Compartments",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Water is about 60 percent of body weight in men and about 50 "
            "percent in women - roughly 42 liters in a 70-kilogram man. It "
            "sits in two great compartments: intracellular fluid (ICF), "
            "about two-thirds of total body water or 28 liters, rich in "
            "potassium and phosphate; and extracellular fluid (ECF), about "
            "one-third or 14 liters, rich in sodium and chloride. The ECF "
            "splits further into plasma (about 3.5 liters) and interstitial "
            "fluid (about 10.5 liters). Water follows salt: sodium is the "
            "effective osmole of the ECF, potassium of the ICF, and the "
            "sodium-potassium ATPase maintains the divide. Every fluid "
            "disorder in nephrology - dehydration, overload, hyponatremia, "
            "hypernatremia - is a disturbance of these compartments, and "
            "every correction is computed from them: the 42-liter pool is "
            "the denominator of all water arithmetic."
        ),
        "how_it_works": (
            "Osmotic equilibrium keeps all compartments at the same "
            "osmolarity (about 285-295 mOsm/kg), while the cell membrane "
            "keeps the solutes segregated: sodium outside, potassium inside. "
            "Add pure water and it distributes across total body water, "
            "diluting every compartment equally. Add isotonic saline and it "
            "stays in the ECF. Lose water without salt (diabetes insipidus, "
            "insensible loss) and the ECF concentrates, pulling water from "
            "cells - cells shrink. Gain water without salt and cells swell. "
            "Clinically, TBW is estimated as 0.6 times body weight in men "
            "and 0.5 in women (less in the elderly and obese, more in the "
            "young and lean). The demo builds the compartment map for a "
            "70-kilogram man: 42 liters total, 28 intracellular, 14 "
            "extracellular, 3.5 of that plasma."
        ),
        "key_points": [
            "Total body water is about 60 percent of weight in men, 50 percent in women: about 42 L in a 70-kg man.",
            "ICF is about two-thirds of TBW (28 L, potassium-rich); ECF is about one-third (14 L, sodium-rich).",
            "ECF splits into plasma (about 3.5 L) and interstitial fluid (about 10.5 L).",
            "Sodium is the ECF osmole, potassium the ICF osmole; water follows salt across every membrane.",
            "TBW is the denominator of all water correction arithmetic in nephrology.",
        ],
        "requirements": [
            "The TBW fractions by sex and the compartment split.",
            "Which solute dominates each compartment and why.",
            "How pure water vs isotonic saline distribute.",
        ],
        "standards": [
            "Volumes in liters; fractions stated with the population they apply to.",
            "Osmolarity in mOsm/kg; compartments named in standard form (ICF, ECF).",
            "Estimates carry 'about' qualifiers for body-composition variation.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON, CIT_ADROGUE],
        "sig_lens": (
            "His Signature reading: the body is a 42-liter water plant in a "
            "70-kilo man, and the kidneys are its level-control engineers. "
            "Two tanks hold the inventory: a 28-liter inside-the-cells tank "
            "full of potassium water, and a 14-liter outside tank full of "
            "sodium water, with a 3.5-liter plasma sump at its heart. Water "
            "itself moves freely between the tanks - only the salt is "
            "locked in place - so whoever controls the salt controls the "
            "levels. Every fluid order the nephrologist writes is a tank "
            "transfer order computed against these exact volumes."
        ),
    },
    {
        "key": "gfr_measure",
        "name": "Glomerular Filtration Rate: Measuring Kidney Function",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "GFR is never measured directly at the bedside; it is estimated "
            "from creatinine, the muscle waste product filtered freely and "
            "barely secreted. Because creatinine production is steady, a "
            "rising serum creatinine means falling filtration - but the "
            "relationship is inverse and curved, so creatinine must double "
            "before GFR halves, and early kidney disease hides behind a "
            "'normal' creatinine. The bedside workhorse is the "
            "Cockcroft-Gault equation: creatinine clearance = (140 minus "
            "age) times weight in kg, divided by 72 times serum creatinine - "
            "times 0.85 for women. For a 65-year-old, 72-kg man with "
            "creatinine 1.2 mg/dL, that gives (75 x 72) / 86.4 = 62.5 "
            "mL/min. Modern practice uses the CKD-EPI 2021 creatinine "
            "equation (no race coefficient), reported automatically with "
            "chemistry panels, and cystatin C when muscle mass confounds "
            "creatinine. A 24-hour urine creatinine clearance remains the "
            "reference when precision matters."
        ),
        "how_it_works": (
            "Creatinine clearance approximates GFR because creatinine is "
            "produced at a near-constant rate from muscle, filtered freely "
            "at the glomerulus, and neither reabsorbed nor (much) secreted: "
            "clearance = (urine creatinine x urine volume) / plasma "
            "creatinine. Cockcroft and Gault (1976) collapsed the 24-hour "
            "collection into an estimate from age, weight, sex, and serum "
            "creatinine - the numerator (140 minus age) times weight captures "
            "muscle mass, the denominator 72 times creatinine captures the "
            "steady-state level. The CKD-EPI 2021 equation refines this with "
            "a piecewise log model fitted to measured GFR, dropping the "
            "race term of its predecessor. All estimating equations assume "
            "steady state: in acute kidney injury, creatinine lags the true "
            "GFR by a day or more, and the equations mislead. The demo runs "
            "Cockcroft-Gault on the textbook case and lands on 62.5 mL/min."
        ),
        "key_points": [
            "GFR is estimated, not measured, at the bedside - from creatinine, a steady muscle waste product.",
            "Cockcroft-Gault: (140 - age) x weight(kg) / (72 x creatinine), x0.85 for women; the worked case gives 62.5 mL/min.",
            "The creatinine-GFR curve is inverse: creatinine must double for GFR to halve; early disease hides behind 'normal' values.",
            "CKD-EPI 2021 (no race term) is the modern laboratory standard; cystatin C helps when muscle mass is abnormal.",
            "Estimating equations assume steady state and mislead during acute kidney injury.",
        ],
        "requirements": [
            "The Cockcroft-Gault formula with its sex correction.",
            "Why creatinine is a usable filtration marker (free filtration, steady production).",
            "The steady-state assumption and when it breaks.",
        ],
        "standards": [
            "Creatinine in mg/dL, clearance in mL/min; CKD-EPI cited as the 2021 race-free equation.",
            "Worked examples show every arithmetic step.",
            "Limitations stated alongside the formula, not hidden.",
        ],
        "citations": [CIT_COCKCROFT, CIT_CKD_EPI, CIT_BRENNER],
        "sig_lens": (
            "His Signature reading: nobody can dip a gauge directly into "
            "the filter cartridges, so the plant superintendent reads "
            "filtration from the ash in the effluent. Creatinine is the "
            "ash - muscle burns it at a dead-steady rate, the cartridges "
            "sieve it freely, nothing reclaims it. High ash in the blood, "
            "slow filters. Cockcroft and Gault's 1976 slide rule - age, "
            "weight, ash level - still calls the number at the bedside: "
            "62.5 milliliters a minute for the textbook case. The modern "
            "CKD-EPI equation is the same trick with better math and the "
            "race dial removed."
        ),
    },
    {
        "key": "urinalysis",
        "name": "Urinalysis and Urine Microscopy: Reading the Urine",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The urinalysis is nephrology's cheapest biopsy: a dipstick, a "
            "microscope, and a protein measurement read the kidney's "
            "effluent directly. Dipstick protein at 1+ or more, especially "
            "with a urine albumin-to-creatinine ratio (ACR) above 30 mg/g, "
            "marks glomerular injury; above 300 mg/g (A3, severely "
            "increased) it predicts progression. A worked example: 120 mg "
            "of albumin per gram of creatinine gives an ACR of 120 mg/g - "
            "moderately increased (A2), the microalbuminuria range that "
            "triggers intervention in diabetes. Dipstick blood with "
            "dysmorphic red cells or red cell casts points to the glomerulus; "
            "white cell casts point to the tubulointerstitium; muddy brown "
            "granular casts mean acute tubular necrosis. Specific gravity "
            "and osmolarity report concentration; pH, glucose, ketones, "
            "nitrites, and leukocyte esterase complete the chemical screen."
        ),
        "how_it_works": (
            "The dipstick is chemistry on paper: protein error-of-indicators, "
            "blood peroxidase activity of heme, leukocyte esterase from "
            "neutrophils, nitrite from bacterial reduction of nitrate, pH "
            "and specific gravity by indicator dyes. Microscopy is pattern "
            "recognition on spun sediment: red cell casts (glomerular "
            "bleeding molded in tubules), white cell casts (interstitial "
            "inflammation), muddy brown casts (sloughed tubular cells in "
            "ATN), fatty casts and oval fat bodies (nephrotic lipiduria), "
            "crystals (calcium oxalate envelopes, uric acid diamonds, "
            "struvite coffin lids). The ACR corrects spot albumin for urine "
            "concentration using creatinine: ACR in mg/g approximates "
            "24-hour albumin in mg/day. Categories: A1 below 30 (normal to "
            "mildly increased), A2 30-300 (moderately increased), A3 above "
            "300 (severely increased). The demo computes the ACR of 120 mg/g "
            "and assigns A2."
        ),
        "key_points": [
            "Urinalysis = dipstick chemistry + sediment microscopy + albumin-to-creatinine ratio: the cheapest kidney biopsy.",
            "ACR categories: A1 <30, A2 30-300, A3 >300 mg/g; ACR 120 mg/g is moderately increased (A2).",
            "Red cell casts = glomerular bleeding; white cell casts = interstitial inflammation; muddy brown casts = acute tubular necrosis.",
            "Dipstick protein 1+ or more deserves quantification; dipstick blood needs microscopy to find the source.",
            "Spot ACR in mg/g approximates 24-hour albumin excretion in mg/day.",
        ],
        "requirements": [
            "The ACR categories and what each triggers clinically.",
            "Cast types and the lesion each reports.",
            "Dipstick pad chemistry basics (protein, blood, leukocyte esterase, nitrite).",
        ],
        "standards": [
            "ACR in mg/g with A1/A2/A3 categories per KDIGO.",
            "Cast names in standard form (red cell cast, muddy brown granular cast).",
            "Dipstick findings always paired with their confirmatory step.",
        ],
        "citations": [CIT_KDIGO_CKD, CIT_BRENNER, CIT_KDIGO_DIAB],
        "sig_lens": (
            "His Signature reading: the urinalysis is the effluent assay - "
            "the plant superintendent never needs to cut the plant open "
            "when the outflow tells the story. Protein in the outflow "
            "means the cartridges are torn. Red cells molded into casts "
            "mean the filters are bleeding. White cell casts mean the "
            "pipework between cartridges is inflamed. Muddy brown sludge "
            "means the refining lines just died and sloughed. The ACR is "
            "the assay's headline number: 120 milligrams per gram sits in "
            "the amber band - moderately increased, act now, the filters "
            "are starting to leak."
        ),
    },
    {
        "key": "sodium_water",
        "name": "Sodium and Water Balance: Osmolarity and ADH",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Sodium is the skeleton key of body water: it is the dominant "
            "extracellular solute, so plasma sodium concentration reports "
            "water balance, not sodium balance. Hyponatremia means too much "
            "water for the salt; hypernatremia means too little. Plasma "
            "osmolarity is estimated at the bedside as 2 times sodium plus "
            "glucose over 18 plus BUN over 2.8: for sodium 140, glucose 90, "
            "BUN 14, that is 280 + 5 + 5 = 290 mOsm/kg - squarely in the "
            "normal 285-295 range. ADH (vasopressin) is the effector: "
            "osmoreceptors fire above about 285 mOsm/kg, ADH inserts "
            "aquaporin-2 channels, and the kidney reclaims pure water until "
            "osmolarity falls. Thirst backs it up. Every sodium disorder is "
            "diagnosed by asking first about volume status, then about "
            "urine osmolarity and urine sodium - the kidney's own testimony "
            "about why the number moved."
        ),
        "how_it_works": (
            "The control loop is tight: a 1-2 percent rise in plasma "
            "osmolarity triggers ADH release from the posterior pituitary "
            "and a 2-3 percent rise triggers thirst. ADH binds V2 receptors "
            "on the collecting duct, inserts aquaporin-2 water channels, and "
            "water follows the medullary salt gradient out of the tubule - "
            "urine concentrates, plasma dilutes back toward normal. Volume "
            "depletion fires the same system harder through baroreceptors, "
            "which is why a dry patient holds water even at low osmolarity. "
            "The bedside osmolarity estimate - 2xNa + glucose/18 + BUN/2.8 - "
            "counts the effective osmoles; the gap between measured and "
            "calculated osmolarity (the osmolar gap, normally under 10) "
            "hunts hidden osmoles like toxic alcohols. The demo computes "
            "290 mOsm/kg for the textbook panel."
        ),
        "key_points": [
            "Plasma sodium reports water balance, not sodium balance: low sodium = excess water relative to salt.",
            "Estimated osmolarity = 2xNa + glucose/18 + BUN/2.8; the textbook panel gives 290 mOsm/kg (normal 285-295).",
            "ADH fires above about 285 mOsm/kg; thirst fires a little higher; baroreceptors override both when volume falls.",
            "Workup order: volume status first, then urine osmolarity and urine sodium - the kidney testifies about the cause.",
            "The osmolar gap (measured minus calculated, normally <10) hunts toxic alcohols.",
        ],
        "requirements": [
            "The osmolarity formula and the normal range.",
            "The ADH-thirst control loop and its thresholds.",
            "The diagnostic sequence: volume status, urine osmolarity, urine sodium.",
        ],
        "standards": [
            "Sodium in mmol/L (equivalent to mEq/L); osmolarity in mOsm/kg.",
            "Glucose and BUN divisors (18, 2.8) shown with unit conversions.",
            "Thresholds stated as approximate physiologic set points.",
        ],
        "citations": [CIT_ADROGUE, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: sodium is the plant's level gauge, not "
            "its salt inventory - the number on the dial tells you how much "
            "water sits behind the salt, never how much salt the plant "
            "holds. The control loop is a thermostat for concentration: "
            "osmoreceptors are the thermometers, the pituitary is the "
            "controller, ADH is the signal wire, and the collecting duct's "
            "aquaporin hatches are the valves. The bedside formula - twice "
            "the sodium plus the glucose and urea corrections - is the "
            "superintendent's quick assay: 290 on the textbook panel, dead "
            "center of the green band."
        ),
    },
    {
        "key": "acid_base",
        "name": "Acid-Base Balance: The Henderson-Hasselbalch Framework",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Blood pH is held between 7.35 and 7.45 by the bicarbonate "
            "buffer system, and the Henderson-Hasselbalch equation is its "
            "mathematics: pH = 6.1 + log(bicarbonate / (0.03 x pCO2)). For "
            "the textbook blood gas - bicarbonate 24, pCO2 40 - the ratio "
            "is 24/1.2 = 20, log 20 is 1.30, and pH = 7.40 exactly. The "
            "lungs control the denominator (pCO2) in minutes; the kidneys "
            "control the numerator (bicarbonate) over hours to days by "
            "reclaiming filtered bicarbonate, excreting titratable acid, and "
            "making ammonium. The kidney's daily acid job is excreting about "
            "1 mEq/kg of nonvolatile acid - roughly 70 mEq in an adult - "
            "mostly as ammonium. Every acid-base disorder is read in the "
            "same order: pH first (acidemia vs alkalemia), then which "
            "partner moved first (respiratory vs metabolic), then "
            "compensation, then the gap arithmetic."
        ),
        "how_it_works": (
            "CO2 plus water makes carbonic acid via carbonic anhydrase, "
            "which dissociates to hydrogen and bicarbonate - this is the "
            "volatile acid the lungs blow off. Nonvolatile acids from "
            "metabolism (sulfuric from protein, organic acids) must leave "
            "through the kidney: the proximal tubule reclaims all filtered "
            "bicarbonate (about 4,500 mEq/day), the distal nephron secretes "
            "hydrogen via H+-ATPase, and the collecting duct makes ammonium "
            "(NH4+) from glutamine - the expandable acid-excretion pathway "
            "that can rise fivefold in chronic acidosis. Compensation is "
            "predictable: metabolic acidosis drives hyperventilation "
            "(Winter's formula: pCO2 = 1.5 x HCO3 + 8), metabolic alkalosis "
            "hypoventilates, and the kidney compensates respiratory "
            "disorders over 3-5 days. The demo evaluates Henderson-"
            "Hasselbalch on the textbook gas and lands on pH 7.40."
        ),
        "key_points": [
            "Henderson-Hasselbalch: pH = 6.1 + log(HCO3 / (0.03 x pCO2)); the textbook gas (24, 40) gives pH 7.40.",
            "Lungs own the denominator (minutes); kidneys own the numerator (hours to days).",
            "The kidney excretes about 70 mEq/day of nonvolatile acid, mostly as ammonium - the expandable pathway.",
            "The proximal tubule reclaims about 4,500 mEq/day of filtered bicarbonate.",
            "Read every gas in order: pH, primary disorder, compensation, gap arithmetic.",
        ],
        "requirements": [
            "The Henderson-Hasselbalch equation and the 6.1/0.03 constants.",
            "The three renal acid-handling mechanisms (bicarbonate reclaim, titratable acid, ammonium).",
            "The standard reading order for a blood gas.",
        ],
        "standards": [
            "pH unitless; pCO2 in mmHg; bicarbonate in mEq/L.",
            "Worked examples show the ratio, the log, and the sum.",
            "Compensation formulas stated with their expected values.",
        ],
        "citations": [CIT_KRAUT, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: pH is the plant's chemistry dial, and "
            "the bicarbonate system is the buffer tank that holds it at "
            "7.40. The lungs are the exhaust stack - they vent the volatile "
            "acid (CO2) in minutes. The kidneys are the chemical dosing "
            "skids - slow, precise, reclaiming 4,500 milliequivalents of "
            "bicarbonate a day and manufacturing ammonium on demand to dump "
            "the day's 70 milliequivalents of fixed acid. Henderson and "
            "Hasselbalch just wrote the tank's gauge equation: 6.1 plus the "
            "log of the ratio. Textbook tank: 24 over 1.2, ratio 20, gauge "
            "reads 7.40 dead center."
        ),
    },
    {
        "key": "encounter",
        "name": "The Nephrology Clinical Encounter: Evaluating Kidney Disease",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The nephrology workup is a disciplined sequence: history "
            "(medications - NSAIDs, ACE inhibitors, diuretics - volume "
            "history, urine changes, family history of kidney disease), "
            "volume examination (orthostatics, jugular venous pressure, "
            "edema, lung crackles), the chemistry panel, and the urine. The "
            "BUN-to-creatinine ratio is the classic first branch point: both "
            "rise in kidney failure, but urea is reabsorbed with water while "
            "creatinine is not, so a ratio above 20 suggests a prerenal "
            "state - for BUN 42 and creatinine 1.0, the ratio is 42, strongly "
            "prerenal. Urine sodium and the fractional excretion of sodium "
            "(below 1 percent = prerenal, above 2 percent = tubular injury) "
            "confirm it. The encounter ends with the two staging questions "
            "every nephrologist asks: is this acute or chronic (ultrasound "
            "kidney size, old creatinines, anemia of chronic disease), and "
            "where is the lesion (prerenal, intrinsic, postrenal)?"
        ),
        "how_it_works": (
            "The encounter runs as a decision tree. First, acuity: small "
            "echogenic kidneys and a normocytic anemia say chronic; normal-"
            "sized kidneys and a prior normal creatinine say acute. Second, "
            "location: a BUN/creatinine ratio above 20, FENa below 1 percent, "
            "and concentrated urine say prerenal (perfusion failure); muddy "
            "brown casts and FENa above 2 percent say acute tubular necrosis; "
            "red cell casts say glomerular; hydronephrosis on ultrasound "
            "says obstruction. Third, reversibility: stop the nephrotoxin, "
            "restore perfusion, relieve the obstruction - the three "
            "reversible moves, in order. Blood pressure and weight track "
            "volume; potassium and bicarbonate track the dangerous chemistry. "
            "The demo computes the BUN/creatinine ratio of 42 and the "
            "prerenal call."
        ),
        "key_points": [
            "The workup sequence: history (especially drugs), volume exam, chemistry panel, urine - then acuity, then location.",
            "BUN/creatinine above 20 suggests prerenal; the worked case (42/1.0) gives 42 - strongly prerenal.",
            "FENa below 1 percent = prerenal; above 2 percent = tubular injury.",
            "Chronicity clues: small echogenic kidneys and anemia say chronic; old normal creatinines say acute.",
            "The three reversible moves in order: stop the toxin, restore perfusion, relieve obstruction.",
        ],
        "requirements": [
            "The BUN/creatinine ratio logic and the 20 threshold.",
            "FENa interpretation bands.",
            "The acute-vs-chronic and prerenal/intrinsic/postrenal branch points.",
        ],
        "standards": [
            "BUN and creatinine in mg/dL; the ratio is unitless.",
            "History elements listed as the drugs and volume clues that change management.",
            "Every branch point paired with its confirmatory test.",
        ],
        "citations": [CIT_BRENNER, CIT_KDIGO_AKI, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the nephrology encounter is the plant "
            "superintendent's walkdown - and it follows the same order "
            "every time. Check the logbook (what drugs went in, what "
            "volume went out). Walk the tanks (veins full or flat, lungs "
            "wet or dry). Read the lab board. Then the two questions that "
            "decide everything: did this plant fail today or has it been "
            "rusting for years, and is the fault in the supply line, the "
            "cartridges, or the drain? The BUN-to-creatinine ratio is the "
            "fastest tell in the building: 42 on the worked case screams "
            "supply-line failure - the pumps are dry, the cartridges are "
            "fine, fill the tanks."
        ),
    },
    {
        "key": "hyponatremia",
        "name": "Hyponatremia: Too Little Sodium",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Hyponatremia - serum sodium below 135 mmol/L - is the commonest "
            "electrolyte disorder in hospitalized patients, and it is almost "
            "always a water problem, not a sodium problem: impaired water "
            "excretion dilutes the plasma. The first correction is for "
            "glucose: every 100 mg/dL of glucose above 100 lowers measured "
            "sodium by about 1.6 mmol/L, so a sodium of 128 with glucose 400 "
            "is truly 128 + 4.8 = 132.8 mmol/L. True hyponatremia is sorted "
            "by volume status (hypovolemic, euvolemic, hypervolemic) and by "
            "urine osmolarity: a concentrated urine (above 100 mOsm/kg) "
            "means ADH is acting - SIADH, volume depletion, adrenal "
            "insufficiency, hypothyroidism - while maximally dilute urine "
            "means the kidney is appropriately dumping water (polydipsia, "
            "beer potomania). Correction speed is the safety rule: no faster "
            "than 8 mmol/L per 24 hours in chronic hyponatremia, or osmotic "
            "demyelination can destroy the pons."
        ),
        "how_it_works": (
            "Water balance sets the sodium: total body sodium divided by "
            "total body water. When ADH is inappropriately on - ectopic "
            "production in SIADH, drugs (SSRIs, carbamazepine), nausea, pain "
            "- the collecting duct reclaims pure water and sodium falls. In "
            "hypovolemia the baroreceptor drive is appropriate (give "
            "saline); in hypervolemia (heart failure, cirrhosis) the "
            "'effective' volume is low despite edema (restrict water, treat "
            "the underlying disease). Severe symptoms - seizures, coma - "
            "demand hypertonic (3 percent) saline, but the 24-hour correction "
            "ceiling of 8 mmol/L is absolute in chronic cases: the brain "
            "adapts to chronic hyponatremia by extruding osmolytes, and fast "
            "correction shrinks brain cells past recovery - osmotic "
            "demyelination syndrome. The demo applies the glucose "
            "correction: 128 at glucose 400 becomes 132.8 mmol/L true."
        ),
        "key_points": [
            "Hyponatremia is almost always excess water relative to salt, not salt loss.",
            "Correct for glucose first: +1.6 mmol/L per 100 mg/dL above 100; 128 at glucose 400 is truly 132.8.",
            "Sort by volume status (hypo/eu/hypervolemic), then urine osmolarity: >100 means ADH is acting.",
            "SIADH workup: euvolemic, concentrated urine, high urine sodium, normal adrenal/thyroid/kidney function.",
            "Correction ceiling in chronic hyponatremia: 8 mmol/L per 24 hours - faster risks osmotic demyelination.",
        ],
        "requirements": [
            "The glucose-corrected sodium formula.",
            "The volume-status sorting tree and urine osmolarity branch.",
            "The correction-rate ceiling and the demyelination mechanism.",
        ],
        "standards": [
            "Sodium in mmol/L; glucose in mg/dL; correction factor 1.6 stated explicitly.",
            "SIADH criteria listed as the exclusion diagnosis it is.",
            "Rate limits stated as absolute ceilings with the complication named.",
        ],
        "citations": [CIT_ADROGUE, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: hyponatremia is the plant's dilution "
            "alarm - the level gauge reads low because somebody left the "
            "water valve open, not because salt escaped. Before touching "
            "anything, the superintendent corrects the gauge for sugar: "
            "glucose drags water with it and fakes a low reading - 128 on "
            "the dial at glucose 400 is really 132.8. Then the sort: tanks "
            "low, tanks level, or tanks overflowing - and is the ADH signal "
            "wire stuck on? The iron safety rule of the whole plant: never "
            "raise the gauge faster than 8 points a day in a chronic case, "
            "or the brain's own cells - adapted to the dilute world - "
            "shrink past the point of no return."
        ),
    },
    {
        "key": "hypernatremia",
        "name": "Hypernatremia: Too Much Sodium",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Hypernatremia - serum sodium above 145 mmol/L - means water "
            "deficit relative to salt: too little water intake (impaired "
            "thirst, no access), too much water loss (diabetes insipidus, "
            "osmotic diuresis, diarrhea, insensible loss), or rarely sodium "
            "gain. The brain shrinks as water leaves cells, causing thirst "
            "first, then confusion, then seizures and coma. The deficit is "
            "computed from total body water: free water deficit = TBW x "
            "(sodium/140 - 1). For a 70-kg man (TBW 42 L) at sodium 160, "
            "that is 42 x (160/140 - 1) = 6.0 liters of pure water owed. "
            "Correction is the mirror of hyponatremia: no faster than about "
            "8-10 mmol/L per 24 hours in chronic cases, because the brain "
            "makes idiogenic osmoles to defend its volume and fast "
            "correction causes cerebral edema. Diabetes insipidus is sorted "
            "by the water deprivation test and the desmopressin response: "
            "central DI concentrates with desmopressin, nephrogenic DI does "
            "not."
        ),
        "how_it_works": (
            "Every cause is water out exceeding water in. Central diabetes "
            "insipidus: no ADH made (pituitary injury, surgery) - give "
            "desmopressin and the kidney answers. Nephrogenic DI: the "
            "collecting duct ignores ADH (lithium, hypercalcemia, "
            "obstruction) - desmopressin does nothing; treat the cause and "
            "use thiazides paradoxically. Osmotic diuresis (hyperglycemia, "
            "mannitol, high-protein tube feeds) drags water with solute. "
            "Replacement is hypotonic: oral water or D5W intravenously, "
            "with the deficit spread over 48-72 hours and sodium checked "
            "every few hours. In acute hypernatremia (hours, e.g. salt "
            "poisoning) correction can be faster because the brain has not "
            "adapted. The demo computes the 6.0-liter free water deficit "
            "for the textbook case."
        ),
        "key_points": [
            "Hypernatremia = water deficit relative to salt: poor intake, diabetes insipidus, osmotic diuresis, insensible loss.",
            "Free water deficit = TBW x (Na/140 - 1); the 70-kg man at Na 160 owes 6.0 liters.",
            "Central DI answers desmopressin; nephrogenic DI does not - the water deprivation test sorts them.",
            "Correct chronic hypernatremia no faster than about 8-10 mmol/L per 24 hours to avoid cerebral edema.",
            "Replace with water (oral or D5W), spread over 48-72 hours, rechecking sodium frequently.",
        ],
        "requirements": [
            "The free-water-deficit formula and the 140 reference.",
            "The central vs nephrogenic DI distinction and test.",
            "The correction-rate ceiling and the cerebral edema mechanism.",
        ],
        "standards": [
            "Sodium in mmol/L; deficit in liters; TBW from 0.6/0.5 x weight.",
            "DI sorted by mechanism (ADH absent vs ADH ignored) with the definitive test.",
            "Rate limits stated with the adapted-brain rationale.",
        ],
        "citations": [CIT_ADROGUE, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: hypernatremia is the plant running dry - "
            "the level gauge reads high because water left and salt stayed. "
            "The superintendent's first calculation is the debt ledger: "
            "total body water times the excess ratio - 42 liters times "
            "(160 over 140 minus one) - 6.0 liters of pure water owed to "
            "the tanks. Pay it back too fast and the brain, which has been "
            "manufacturing its own internal ballast to survive the dry "
            "spell, swells and herniates. So the payback runs slow - "
            "48 to 72 hours - with the gauge checked every few hours like "
            "a miser counting coins."
        ),
    },
    {
        "key": "potassium",
        "name": "Potassium Disorders: Hyperkalemia and Hypokalemia",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Potassium is the intracellular king - 98 percent inside cells - "
            "so small shifts move the serum level a lot, and the heart "
            "notices first: hyperkalemia peaks the T waves, widens the QRS, "
            "and arrests the heart in diastole. Hyperkalemia (above 5.5 "
            "mmol/L) is the nephrologist's true emergency: check "
            "pseudohyperkalemia (hemolysis, fist clenching), stop the "
            "inputs (supplements, trimethoprim, ACE inhibitors), stabilize "
            "the membrane with calcium, shift potassium into cells with "
            "insulin-glucose and bicarbonate, then remove it (diuretics, "
            "binders, dialysis). Hypokalemia (below 3.5) weakens muscle, "
            "flattens T waves, and promotes arrhythmia; the transtubular "
            "potassium gradient (TTKG) sorts renal from extrarenal loss. A "
            "worked example: urine K 40, plasma K 5.5, urine osm 600, plasma "
            "osm 290 gives TTKG = (40/5.5)/(600/290) = 3.5 - below 7, so "
            "the kidney is appropriately conserving and the loss is "
            "extrarenal."
        ),
        "how_it_works": (
            "Total body potassium is about 3,500 mmol; serum holds only "
            "about 70 mmol, so transcellular shifts swing the level: "
            "acidosis pushes potassium out of cells (about 0.6 mmol/L per "
            "0.1 pH fall), insulin and beta-agonists push it in. The kidney "
            "excretes the daily load in the collecting duct: aldosterone "
            "opens ENaC, sodium entry creates the lumen-negative gradient, "
            "and potassium exits through ROMK - flow-dependent, which is why "
            "loop diuretics waste potassium. Hyperkalemia treatment is "
            "sequenced by speed: calcium in minutes (membrane stabilization, "
            "no potassium moved), insulin/bicarbonate in 15-30 minutes "
            "(intracellular shift), binders and dialysis over hours "
            "(removal). The TTKG corrects urine potassium for water "
            "reabsorption: below 7 with hypokalemia means the kidney is "
            "conserving appropriately. The demo computes TTKG 3.5 and the "
            "extrarenal call."
        ),
        "key_points": [
            "Hyperkalemia is the cardiac emergency: peaked Ts, wide QRS, diastolic arrest - treat in sequence, not all at once.",
            "Treatment order: calcium (stabilize), insulin/bicarbonate (shift), diuretics/binders/dialysis (remove).",
            "TTKG = (urine K/plasma K)/(urine osm/plasma osm); 3.5 in the worked case (<7) means appropriate renal conservation.",
            "Acidosis shifts K out of cells (~0.6 mmol/L per 0.1 pH); insulin shifts it in.",
            "Aldosterone drives K excretion via ENaC/ROMK; ACE inhibitors, trimethoprim, and spironolactone raise K.",
        ],
        "requirements": [
            "The hyperkalemia treatment sequence with each step's mechanism and timing.",
            "The TTKG formula and the 7 threshold.",
            "Transcellular shift rules (pH, insulin).",
        ],
        "standards": [
            "Potassium in mmol/L; ECG changes described in standard terms.",
            "Drug causes listed as the inputs to stop first.",
            "TTKG worked with all four inputs shown.",
        ],
        "citations": [CIT_PALMER, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: potassium is the plant's high-voltage "
            "line - 98 percent of it locked inside the cells, a tiny "
            "fraction in the plasma, and the heart wired straight across "
            "it. Let the line voltage climb and the cardiac trace tells "
            "the story in order: peaked Ts, widening QRS, then flatline. "
            "The emergency drill is sequenced like a reactor scram: calcium "
            "first (insulate the heart, minutes), insulin next (drive the "
            "voltage back inside the cells), removal last (dialysis hauls "
            "it out for good). The TTKG is the line inspector's meter: 3.5 "
            "on the worked case means the plant's own valves are shut "
            "tight and the leak is somewhere outside the fence."
        ),
    },
    {
        "key": "ca_p_mg",
        "name": "Calcium, Phosphate, and Magnesium Disorders",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Calcium, phosphate, and magnesium are the kidney's mineral "
            "portfolio, managed jointly with bone and gut. Ionized calcium "
            "is the physiologically active fraction; total calcium must be "
            "corrected for albumin: corrected Ca = measured + 0.8 x (4.0 - "
            "albumin). A calcium of 8.0 mg/dL with albumin 2.8 g/dL corrects "
            "to 8.0 + 0.96 = 8.96 mg/dL - still low, true hypocalcemia. "
            "Hypercalcemia (malignancy, primary hyperparathyroidism, "
            "granulomatous disease) causes nephrogenic DI, stones, and "
            "tubulointerstitial injury; severe cases get saline, "
            "calcitonin, and bisphosphonates. Hypocalcemia (CKD, "
            "hypoparathyroidism, vitamin D deficiency) causes tetany and QT "
            "prolongation. Phosphate rises as GFR falls - the kidney is the "
            "phosphate excretor - driving secondary hyperparathyroidism. "
            "Magnesium follows potassium: hypomagnesemia causes refractory "
            "hypokalemia and hypocalcemia by impairing PTH release and "
            "action."
        ),
        "how_it_works": (
            "PTH is the master regulator: low ionized calcium triggers PTH, "
            "which resorbs bone, reclaims calcium in the distal tubule, "
            "wastes phosphate, and activates vitamin D (1-alpha-hydroxylase "
            "in the proximal tubule) to absorb gut calcium. FGF23 from bone "
            "opposes it, wasting phosphate when levels rise. In CKD the "
            "kidney cannot excrete phosphate or activate vitamin D: "
            "phosphate climbs, calcium falls, PTH surges - secondary "
            "hyperparathyroidism and renal osteodystrophy. Magnesium is "
            "handled in the thick ascending limb via paracellin-1; loop "
            "diuretics waste it, and low magnesium locks potassium inside "
            "deficiency by disabling the ROMK regulation and PTH secretion. "
            "The clinical rule: never chase refractory hypokalemia or "
            "hypocalcemia without checking magnesium first. The demo applies "
            "the albumin correction: 8.0 at albumin 2.8 becomes 8.96 mg/dL."
        ),
        "key_points": [
            "Corrected calcium = measured + 0.8 x (4.0 - albumin); 7.5 at albumin 2.8 corrects to 8.46 mg/dL - true hypocalcemia.",
            "PTH raises calcium (bone, gut via vitamin D, distal tubule) and wastes phosphate; FGF23 opposes it.",
            "Hypercalcemia causes nephrogenic DI, stones, and kidney injury; severe cases need saline, calcitonin, bisphosphonates.",
            "Phosphate rises as GFR falls - the kidney is the phosphate excretor - driving secondary hyperparathyroidism in CKD.",
            "Hypomagnesemia causes refractory hypokalemia and hypocalcemia: always check magnesium first.",
        ],
        "requirements": [
            "The albumin-corrected calcium formula.",
            "The PTH-vitamin D-FGF23 axis and what each hormone does.",
            "The magnesium-potassium-calcium linkage rule.",
        ],
        "standards": [
            "Calcium in mg/dL, albumin in g/dL; ionized calcium noted as the active fraction.",
            "Hormone actions stated as organ-level effects (bone, gut, kidney).",
            "Emergency therapies listed in treatment order.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON, CIT_MOE],
        "sig_lens": (
            "His Signature reading: calcium, phosphate, and magnesium are "
            "the plant's mineral inventory, co-managed with the bone "
            "warehouse and the gut loading dock. PTH is the inventory "
            "manager: low calcium on the shelf and it orders bone "
            "resorption, gut activation (vitamin D is the purchase order), "
            "and phosphate clearance. When the plant's own filters fail "
            "(CKD), phosphate piles up in the yard, calcium crashes, and "
            "the manager panics - secondary hyperparathyroidism. And the "
            "standing rule of the mineral yard: if the potassium and "
            "calcium crews will not respond to orders, check the magnesium "
            "foreman first - nothing moves without him."
        ),
    },
    {
        "key": "metabolic_acidosis",
        "name": "Metabolic Acidosis: The Anion Gap and the Delta Gap",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Metabolic acidosis - bicarbonate below 22 mEq/L with acidemia - "
            "is sorted by the anion gap: AG = sodium - (chloride + "
            "bicarbonate). For sodium 140, chloride 104, bicarbonate 18, "
            "the gap is 140 - 122 = 18 mEq/L - elevated (normal about 12), "
            "so unmeasured anions are present: lactate, ketoacids, toxins, "
            "or renal failure anions (MUDPILES). The delta gap then checks "
            "for a second disorder: delta gap = (AG - 12) - (24 - HCO3) = "
            "(18 - 12) - (24 - 18) = 0 - a pure high-gap acidosis with no "
            "hidden normal-gap or alkalosis component. Winter's formula "
            "checks the lungs: expected pCO2 = 1.5 x 18 + 8 = 35 mmHg - "
            "matching ventilation means appropriate compensation. Normal-gap "
            "(hyperchloremic) acidosis points to the kidney or gut: diarrhea "
            "bicarbonate loss, or renal tubular acidosis - type 1 (distal, "
            "cannot acidify urine), type 2 (proximal, bicarbonate wasting), "
            "type 4 (hypoaldosteronism, hyperkalemic)."
        ),
        "how_it_works": (
            "The gap arithmetic is electroneutrality bookkeeping: every "
            "unmeasured anion (lactate, ketoacid, sulfate, formate) widens "
            "the gap. High-gap causes are memorized as MUDPILES - methanol, "
            "uremia, diabetic ketoacidosis, propylene glycol, isoniazid, "
            "lactic acidosis, ethylene glycol, salicylates. The delta gap "
            "compares the gap's rise to bicarbonate's fall: both move "
            "together in a pure high-gap acidosis (delta 0); a positive "
            "delta means a concurrent metabolic alkalosis; a negative delta "
            "means a concurrent normal-gap acidosis. The delta ratio "
            "formalizes it. Treatment follows the cause: fluids and "
            "perfusion for lactate, insulin for DKA, fomepizole and dialysis "
            "for toxic alcohols, bicarbonate only for severe acidemia (pH "
            "below 7.10) or as a bridge. The demo computes AG 18, delta gap "
            "0, and Winter's pCO2 35."
        ),
        "key_points": [
            "Anion gap = Na - (Cl + HCO3); the worked case (140, 104, 18) gives AG 18 - elevated, unmeasured anions present.",
            "Delta gap = (AG - 12) - (24 - HCO3) = 0 in the worked case: pure high-gap acidosis, no second disorder.",
            "Winter's formula: expected pCO2 = 1.5 x HCO3 + 8 = 35 mmHg in the worked case - appropriate compensation.",
            "High-gap causes: MUDPILES (lactate, ketoacids, toxins, uremia); normal-gap: diarrhea or renal tubular acidosis.",
            "RTA types: 1 distal (cannot acidify urine), 2 proximal (bicarbonate wasting), 4 hypoaldosteronism (hyperkalemic).",
        ],
        "requirements": [
            "The anion gap, delta gap, and Winter's formulas with normal values.",
            "The MUDPILES mnemonic and the normal-gap differential.",
            "The three RTA types and their distinguishing features.",
        ],
        "standards": [
            "Electrolytes in mEq/L; pCO2 in mmHg; gaps as unitless mEq/L differences.",
            "Worked arithmetic shows every substitution.",
            "Treatment matched to cause, not to the number alone.",
        ],
        "citations": [CIT_KRAUT, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: metabolic acidosis is the plant's acid "
            "spill, and the anion gap is the forensic assay - sodium minus "
            "the measured anions leaves the unmeasured residue, and a gap "
            "of 18 where 12 belongs means 6 milliequivalents of mystery "
            "acid on the floor. The delta gap is the second sweep: did the "
            "spill come alone, or is an alkalosis hiding underneath? Zero "
            "on the worked case - one spill, no accomplice. Winter's "
            "formula checks whether the exhaust stack (the lungs) is "
            "keeping up: 35 expected, 35 measured, the crew is ventilating "
            "exactly right."
        ),
    },
    {
        "key": "alk_resp",
        "name": "Metabolic Alkalosis and Respiratory Acid-Base Disorders",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Metabolic alkalosis - bicarbonate above 26 mEq/L with alkalemia "
            "- is the commonest acid-base disorder in hospitalized patients, "
            "usually from vomiting or diuretics: volume depletion and "
            "aldosterone drive hydrogen and potassium loss while the kidney "
            "clings to bicarbonate. It is sorted by urine chloride: below "
            "20 mEq/L means chloride-responsive (vomiting, diuretics - give "
            "saline); above 20 means chloride-resistant (hyperaldosteronism, "
            "severe hypokalemia). Compensation is predictable: for "
            "bicarbonate 40, expected pCO2 = 0.7 x (40 - 24) + 40 = 51.2 "
            "mmHg - the lungs hypoventilate to retain CO2. Respiratory "
            "acidosis (hypoventilation: COPD, sedation, neuromuscular "
            "failure) raises pCO2; the kidney compensates over 3-5 days by "
            "raising bicarbonate about 3.5 mEq/L per 10 mmHg of chronic "
            "pCO2 rise. Respiratory alkalosis (hyperventilation: anxiety, "
            "sepsis, liver failure, salicylates, high altitude) drops "
            "pCO2; acute drops bicarbonate about 2 per 10 mmHg, chronic "
            "about 5."
        ),
        "how_it_works": (
            "Alkalosis persists only if the kidney cannot excrete the "
            "excess bicarbonate - which requires volume depletion, "
            "hypokalemia, or hyperaldosteronism keeping the distal nephron "
            "secreting hydrogen. Vomiting loses HCl (alkalosis plus "
            "hypokalemia and low urine chloride); loop and thiazide "
            "diuretics lose NaCl and water with the same result. Fix the "
            "volume and potassium and the kidney dumps the bicarbonate. "
            "Respiratory disorders are diagnosed by the pCO2-bicarbonate "
            "pair moving the wrong way for compensation: in acute "
            "respiratory acidosis bicarbonate barely moves (about 1 per 10 "
            "mmHg pCO2); a bigger move means chronicity or a second "
            "disorder. Treatment is ventilatory for respiratory disorders - "
            "the blood gas is a ventilator report card - and volume/electrolyte "
            "correction for metabolic alkalosis. The demo computes the "
            "expected pCO2 of 51.2 mmHg for bicarbonate 40."
        ),
        "key_points": [
            "Metabolic alkalosis is usually vomiting or diuretics; urine chloride <20 = chloride-responsive (give saline), >20 = resistant.",
            "Compensation: expected pCO2 = 0.7 x (HCO3 - 24) + 40; bicarbonate 40 predicts pCO2 51.2 mmHg.",
            "Alkalosis persists only if volume depletion, hypokalemia, or aldosterone excess blocks bicarbonate excretion.",
            "Respiratory acidosis = hypoventilation; chronic compensation raises HCO3 about 3.5 per 10 mmHg pCO2 over days.",
            "Respiratory alkalosis = hyperventilation; acute compensation drops HCO3 about 2 per 10 mmHg pCO2.",
        ],
        "requirements": [
            "The urine-chloride sorting rule for metabolic alkalosis.",
            "Compensation formulas for all four primary disorders.",
            "Acute vs chronic respiratory compensation values.",
        ],
        "standards": [
            "Bicarbonate in mEq/L, pCO2 in mmHg, urine chloride in mEq/L.",
            "Compensation rules stated as expected-value formulas.",
            "Causes grouped by mechanism (loss vs generation vs maintenance).",
        ],
        "citations": [CIT_KRAUT, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: metabolic alkalosis is the plant running "
            "too clean - vomiting or diuretics have flushed acid out and "
            "the dosing skids will not dump the excess bicarbonate until "
            "the tanks are refilled and the potassium crew is back on "
            "shift. The urine chloride is the tell: under 20 and the plant "
            "is begging for salt water; over 20 and the aldosterone signal "
            "wire is stuck on. The respiratory disorders are the exhaust "
            "stack's report: too little venting (acidosis) or too much "
            "(alkalosis), with the kidney's slow 3-to-5-day compensation "
            "trailing behind like a freight train catching up."
        ),
    },
    {
        "key": "aki",
        "name": "Acute Kidney Injury: KDIGO Staging and Causes",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Acute kidney injury is the sudden fall in kidney function over "
            "hours to days, defined by KDIGO (2012): creatinine rise of at "
            "least 0.3 mg/dL within 48 hours, or 1.5 times baseline within 7 "
            "days, or urine output below 0.5 mL/kg/hour for 6 hours. "
            "Staging is by the worse of creatinine and urine criteria: "
            "stage 1 is 1.5-1.9x baseline, stage 2 is 2.0-2.9x, stage 3 is "
            "3.0x or creatinine above 4.0 or dialysis. A worked example: "
            "baseline creatinine 1.0 rising to 2.8 is a 2.8-fold rise - KDIGO "
            "stage 2. Causes divide into prerenal (perfusion failure: "
            "volume depletion, heart failure, sepsis vasodilation), "
            "intrinsic (acute tubular necrosis, glomerulonephritis, "
            "interstitial nephritis, vascular), and postrenal (obstruction: "
            "stones, prostate, tumor, clot). AKI complicates about 20 "
            "percent of hospital admissions and over half of ICU stays; "
            "even stage 1 raises mortality, and severe AKI can progress to "
            "chronic kidney disease."
        ),
        "how_it_works": (
            "The KDIGO definition captures both filtration (creatinine) and "
            "output (urine) because each can fail first: creatinine lags "
            "true GFR by 24+ hours in acute injury, while oliguria is "
            "immediate but nonspecific. Prerenal AKI is a plumbing problem - "
            "restore perfusion and the kidney recovers, with concentrated "
            "urine and FENa below 1 percent as the signature. Intrinsic AKI "
            "is parenchymal damage - ATN from ischemia or toxins shows muddy "
            "brown casts and FENa above 2 percent. Postrenal AKI is a drain "
            "blockage - hydronephrosis on ultrasound, and relief can trigger "
            "a dramatic post-obstructive diuresis. Management is cause-"
            "directed: fluids and pressors for prerenal, stop the toxin for "
            "ATN and interstitial nephritis, relieve obstruction "
            "surgically, dialyze for refractory volume overload, acidosis, "
            "hyperkalemia, or uremic complications (the AEIOU indications). "
            "The demo stages the 2.8-fold creatinine rise as KDIGO stage 2."
        ),
        "key_points": [
            "KDIGO defines AKI by creatinine rise (>=0.3 mg/dL/48h or >=1.5x/7d) or urine output (<0.5 mL/kg/h x 6h).",
            "Staging: stage 1 = 1.5-1.9x, stage 2 = 2.0-2.9x, stage 3 = 3x or >4.0 or dialysis; 1.0 to 2.8 is stage 2.",
            "Three buckets: prerenal (perfusion), intrinsic (parenchyma), postrenal (obstruction).",
            "Creatinine lags true GFR by a day or more in AKI; oliguria is immediate but nonspecific.",
            "Dialysis indications: refractory acidosis, electrolytes (K), intoxications, overload, uremia (AEIOU).",
        ],
        "requirements": [
            "The KDIGO creatinine and urine-output criteria with time windows.",
            "The three-bucket causal framework with an example each.",
            "The AEIOU dialysis indications.",
        ],
        "standards": [
            "Creatinine in mg/dL; urine output in mL/kg/hour with the duration.",
            "Staging uses the worse of the creatinine and urine criteria.",
            "Epidemiology stated as hospital/ICU fractions with 'about' qualifiers.",
        ],
        "citations": [CIT_KDIGO_AKI, CIT_MEHTA, CIT_BRENNER],
        "sig_lens": (
            "His Signature reading: AKI is the plant tripping offline in "
            "hours - and the superintendent's first job is naming the "
            "fault. The KDIGO alarm panel watches two dials: the ash gauge "
            "(creatinine - slow, lags a day) and the outflow meter (urine - "
            "instant, noisy). Stage 2 on the worked case: ash up 2.8-fold, "
            "the plant is at half staff. Then the three-fault sort every "
            "operator memorizes: supply line dry (prerenal - fill the "
            "tanks), cartridges damaged (intrinsic - stop the poison, "
            "wait), drain blocked (postrenal - clear the pipe). Get the "
            "fault right and most plants restart; get it wrong and the "
            "auxiliary unit (dialysis) runs the shift."
        ),
    },
    {
        "key": "prerenal_atn",
        "name": "Prerenal AKI and Acute Tubular Necrosis",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Prerenal AKI and acute tubular necrosis are the two faces of "
            "underperfusion: prerenal is the kidney correctly conserving "
            "during low flow - intact tubules, concentrated urine, avid "
            "sodium retention - while ATN is the tubules themselves injured "
            "by prolonged ischemia or toxins, sloughing cells into muddy "
            "brown casts. The fractional excretion of sodium separates "
            "them: FENa = (urine Na x plasma creatinine) / (plasma Na x "
            "urine creatinine) x 100. A worked example - urine Na 10, "
            "plasma creatinine 2.0, plasma Na 140, urine creatinine 40 - "
            "gives (10 x 2.0)/(140 x 40) x 100 = 0.36 percent: below 1 "
            "percent, prerenal - the tubules are working, the tanks are "
            "just empty. Above 2 percent with muddy brown casts, the "
            "tubules are dead and this is ATN. Causes of ATN: prolonged "
            "hypotension, sepsis, aminoglycosides, contrast, rhabdomyolysis "
            "(myoglobin casts), hemoglobinuria. Prerenal is fixed with "
            "volume; ATN is waited out with supportive care - recovery "
            "takes 1-3 weeks, often with a diuretic recovery phase."
        ),
        "how_it_works": (
            "In prerenal states the kidney defends perfusion: afferent "
            "dilation (prostaglandins - which is why NSAIDs precipitate "
            "prerenal failure), efferent constriction (angiotensin II - "
            "which is why ACE inhibitors precipitate it in bilateral renal "
            "artery stenosis), avid proximal sodium and water reabsorption, "
            "and concentrated urine. Push ischemia too far or too long and "
            "the S3 proximal segment and thick ascending limb - the most "
            "oxygen-hungry real estate - necrose and slough, plugging "
            "tubules with cellular debris: ATN. The tubule can no longer "
            "concentrate urine or reclaim sodium, so FENa rises above 2 "
            "percent and the sediment fills with muddy brown granular "
            "casts. FENa is unreliable on diuretics (use FEUrea below 35 "
            "percent instead) and in nonoliguric ATN. The demo computes "
            "FENa 0.36 percent and the prerenal call."
        ),
        "key_points": [
            "Prerenal = intact tubules conserving during low flow; ATN = tubules injured by ischemia or toxins.",
            "FENa = (urine Na x plasma Cr)/(plasma Na x urine Cr) x 100; 0.36 percent in the worked case (<1 percent) = prerenal.",
            "Muddy brown granular casts are the ATN signature; FENa above 2 percent confirms tubular failure.",
            "NSAIDs and ACE inhibitors precipitate prerenal failure by blocking the kidney's perfusion defenses.",
            "On diuretics use FEUrea (<35 percent = prerenal) instead of FENa; ATN recovery takes 1-3 weeks.",
        ],
        "requirements": [
            "The FENa formula and the 1 percent / 2 percent bands.",
            "The perfusion-defense physiology (prostaglandins, angiotensin II) and which drugs break it.",
            "The ATN recovery timeline and the diuretic phase.",
        ],
        "standards": [
            "Sodium in mmol/L (or mEq/L), creatinine in mg/dL; FENa as a percent.",
            "Drug mechanisms stated as which defense they disable.",
            "Diuretic caveat stated alongside the FENa rule.",
        ],
        "citations": [CIT_KDIGO_AKI, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: prerenal versus ATN is the difference "
            "between a plant running on empty tanks and a plant with dead "
            "refining lines. In the first, every cartridge is intact and "
            "screaming for supply - the FENa meter reads 0.36 percent, the "
            "lines reclaiming every molecule of salt they can grab. Fill "
            "the tanks and the plant roars back the same day. In the "
            "second, the oxygen-hungry sections of the refining line have "
            "died and sloughed into the pipes - muddy brown sludge in the "
            "effluent, FENa over 2 percent, and no amount of tank-filling "
            "restarts dead pipework. Then it is 1 to 3 weeks of life "
            "support while the lines regrow - the most expensive wait in "
            "the building."
        ),
    },
    {
        "key": "ckd",
        "name": "Chronic Kidney Disease: Staging and Progression",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Chronic kidney disease is kidney damage or GFR below 60 "
            "mL/min/1.73 m2 persisting at least 3 months - the time rule "
            "that separates it from AKI. KDIGO stages it on two axes: G "
            "(G1 above 90, G2 60-89, G3a 45-59, G3b 30-44, G4 15-29, G5 "
            "below 15 or dialysis) and A (albuminuria: A1 below 30, A2 "
            "30-300, A3 above 300 mg/g). A worked example: eGFR 38 with ACR "
            "450 mg/g is G3bA3 - moderately-to-severely decreased function "
            "with severely increased albuminuria, high risk. CKD affects "
            "about 10 percent of the world's population; diabetes and "
            "hypertension cause most cases. Progression is driven by "
            "proteinuria, hypertension, hyperglycemia, smoking, and the "
            "vicious cycle of nephron loss causing hyperfiltration injury "
            "in survivors. Management: blood pressure control (KDIGO 2021), "
            "ACE inhibitor or ARB for albuminuric CKD, SGLT2 inhibitors, "
            "statins, anemia and bone management, and timely transplant "
            "referral - dialysis planning starts in G4."
        ),
        "how_it_works": (
            "The final common pathway is nephron loss begetting nephron "
            "loss: surviving glomeruli hyperfilter to compensate, the "
            "raised single-nephron GFR injures podocytes, protein leaks, "
            "and tubulointerstitial fibrosis follows - Brenner's "
            "hyperfiltration hypothesis, the reason proteinuria predicts "
            "progression and its reduction slows it. Risk stratification "
            "uses the G-by-A heat map: G3bA3 sits deep in the red zone. The "
            "kidney failure risk equation (Tangri) converts age, sex, eGFR, "
            "and ACR into 2- and 5-year dialysis risk for planning. Therapy "
            "targets the drivers: RAAS blockade and SGLT2 inhibition lower "
            "intraglomerular pressure and proteinuria; blood pressure "
            "target below 130/80 systolic per KDIGO 2021 (measured "
            "standardized); finerenone adds benefit in diabetic CKD. The "
            "demo assigns G3bA3 to the worked case and maps the risk zone."
        ),
        "key_points": [
            "CKD = kidney damage or GFR <60 for at least 3 months - the time rule separating it from AKI.",
            "G stages G1-G5 by eGFR; A stages A1-A3 by albuminuria; eGFR 38 + ACR 450 = G3bA3, high risk.",
            "About 10 percent of the world has CKD; diabetes and hypertension cause most cases.",
            "Hyperfiltration injury in surviving nephrons is the final common pathway - proteinuria reduction slows it.",
            "Treat the drivers: RAAS blockade, SGLT2 inhibitors, BP <130/80, statins; plan dialysis/transplant from G4.",
        ],
        "requirements": [
            "The G and A staging bands and the 3-month chronicity rule.",
            "The hyperfiltration hypothesis of progression.",
            "The core CKD therapies and their mechanisms.",
        ],
        "standards": [
            "eGFR in mL/min/1.73 m2; ACR in mg/g; stages written as GxAy per KDIGO.",
            "Epidemiology with 'about' qualifiers.",
            "Guideline targets cited to KDIGO 2021/2024.",
        ],
        "citations": [CIT_KDIGO_CKD, CIT_LEVEY, CIT_JHA, CIT_KDIGO_BP],
        "sig_lens": (
            "His Signature reading: CKD is the plant rusting out over "
            "years - and the cruel physics is that the surviving "
            "cartridges work harder to cover for the dead ones, and the "
            "overwork kills them faster. Hyperfiltration is overtime that "
            "destroys the crew. The G-by-A heat map is the rust chart: "
            "G3bA3 on the worked case sits deep in the red - function "
            "down to 38, albumin pouring through at 450. The "
            "superintendent's playbook is all about easing the load: "
            "pressure down, protein leak down, sugar controlled, and the "
            "new SGLT2 valves taking strain off the cartridges - while the "
            "replacement-plant paperwork (transplant referral) starts at "
            "G4, never later."
        ),
    },
    {
        "key": "nephritic",
        "name": "Nephritic Syndrome and Glomerulonephritis",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Nephritic syndrome is the inflamed-glomerulus pattern: "
            "hematuria with dysmorphic red cells and red cell casts, "
            "subnephrotic proteinuria, hypertension, and a falling GFR - "
            "often with oliguria. Causes divide by complement: low "
            "complement (post-infectious GN, lupus nephritis, "
            "cryoglobulinemia, MPGN/C3 glomerulopathy) versus normal "
            "complement (IgA nephropathy, ANCA vasculitis, anti-GBM "
            "disease). Post-infectious GN follows streptococcal pharyngitis "
            "by 1-3 weeks with a frankly low C3 that normalizes by 8 "
            "weeks. IgA nephropathy - the commonest GN worldwide - flares "
            "with synpharyngitic hematuria (with the sore throat, not weeks "
            "later). Rapidly progressive GN (crescents on biopsy, "
            "creatinine rising daily) is the emergency: ANCA vasculitis, "
            "anti-GBM (Goodpasture with lung hemorrhage), or severe lupus - "
            "treat with steroids plus cyclophosphamide or rituximab, plus "
            "plasma exchange for anti-GBM and severe ANCA disease."
        ),
        "how_it_works": (
            "Immune injury hits the glomerulus three ways: immune complexes "
            "depositing in the wall (lupus, post-infectious, IgA), "
            "antibodies attacking the basement membrane itself (anti-GBM), "
            "or pauci-immune neutrophil attack (ANCA vasculitis). The "
            "inflamed filter leaks red cells (dysmorphic, molded into "
            "casts) and some protein, while inflammatory cells and "
            "crescents choke the capillary lumens - GFR falls and sodium "
            "retention drives the hypertension. Serology sorts it: ASO "
            "titers and low C3 for post-infectious, ANA and anti-dsDNA for "
            "lupus, ANCA for vasculitis, anti-GBM antibodies for "
            "Goodpasture. Biopsy with immunofluorescence and electron "
            "microscopy is definitive - linear IgG along the GBM in "
            "anti-GBM disease, granular deposits in immune-complex GN, "
            "nothing (pauci-immune) in ANCA vasculitis. The demo works the "
            "complement-branching logic on textbook serology panels."
        ),
        "key_points": [
            "Nephritic pattern: hematuria with RBC casts, subnephrotic proteinuria, hypertension, falling GFR.",
            "Low complement: post-infectious, lupus, cryoglobulinemia, C3 glomerulopathy; normal: IgA, ANCA, anti-GBM.",
            "Post-strep GN follows pharyngitis by 1-3 weeks with low C3 normalizing by 8 weeks; IgA flares with the sore throat.",
            "Rapidly progressive GN (crescents, daily creatinine rise) is the emergency: steroids + cyclophosphamide/rituximab +/- plasma exchange.",
            "Biopsy with immunofluorescence and EM is definitive: linear vs granular vs pauci-immune patterns.",
        ],
        "requirements": [
            "The nephritic clinical pattern vs the nephrotic pattern.",
            "The complement-based causal sort.",
            "The RPGN emergency protocol.",
        ],
        "standards": [
            "Syndrome defined by the tetrad (hematuria, proteinuria range, hypertension, GFR fall).",
            "Serologic tests named with what each diagnoses.",
            "Biopsy patterns described in standard immunofluorescence terms.",
        ],
        "citations": [CIT_KDIGO_GN, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: nephritic syndrome is the filter "
            "cartridges under immune siege - the walls inflamed, red "
            "cells forcing through the torn mesh and molding into casts "
            "in the pipes downstream, the lumens choking shut so hard the "
            "whole plant's output falls. The superintendent sorts the "
            "attackers by their calling cards: low complement means "
            "immune-complex saboteurs (post-strep, lupus); normal "
            "complement with ANCA means a neutrophil riot; linear IgG on "
            "the membrane means the basement itself is the target. And "
            "when the creatinine climbs daily - crescentic, rapidly "
            "progressive - it is the plant's five-alarm fire: hit it with "
            "everything (steroids, cyclophosphamide or rituximab, plasma "
            "exchange) or lose the plant in days."
        ),
    },
    {
        "key": "nephrotic",
        "name": "Nephrotic Syndrome: Protein in the Urine",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Nephrotic syndrome is the leaky-filter pattern: proteinuria "
            "above 3.5 grams per day, hypoalbuminemia below 3.0 g/dL, edema, "
            "and hyperlipidemia - with lipiduria (fatty casts, oval fat "
            "bodies) as the classic extra. A worked example: ACR 4,200 "
            "mg/g approximates 4.2 g/day of albuminuria, and with serum "
            "albumin 2.4 g/dL the full syndrome is present. Primary causes "
            "(the glomerulus itself): minimal change disease (children, "
            "selective albuminuria, steroid-responsive), focal segmental "
            "glomerulosclerosis (adults, often steroid-resistant), "
            "membranous nephropathy (adults, anti-PLA2R antibodies in most "
            "primary cases). Secondary causes: diabetes (the commonest "
            "worldwide), lupus, amyloidosis, infections, drugs, malignancy. "
            "Complications drive management: the hypercoagulable state "
            "(membranous carries real renal-vein thrombosis risk), "
            "infection risk (urinary immunoglobulin loss), and AKI from "
            "volume depletion - so treatment is the cause plus "
            "anticoagulation awareness, RAAS blockade, statins, and sodium "
            "restriction."
        ),
        "how_it_works": (
            "The filtration barrier's charge- and size-selectivity fails: "
            "podocyte foot-process effacement (minimal change, FSGS), "
            "subepithelial immune deposits (membranous), or basement "
            "membrane thickening (diabetes, amyloid). Protein pouring into "
            "the tubule overwhelms proximal reabsorption and appears in "
            "the urine; hepatic albumin synthesis cannot keep up, so "
            "oncotic pressure falls and edema forms - plus primary renal "
            "sodium retention via ENaC activation by filtered plasmin. The "
            "liver compensates for protein loss by overproducing "
            "lipoproteins (hyperlipidemia) and clotting factors while "
            "antithrombin is lost in the urine - hence thrombosis. "
            "Membranous nephropathy is now a serologic diagnosis in many "
            "cases: anti-PLA2R positive with nephrotic proteinuria and "
            "preserved GFR often needs no biopsy. Treatment: steroids for "
            "minimal change; rituximab or calcineurin inhibitors for "
            "membranous and FSGS per KDIGO 2021; the underlying disease for "
            "secondary causes. The demo checks the worked case against all "
            "four syndrome criteria."
        ),
        "key_points": [
            "Nephrotic syndrome = proteinuria >3.5 g/day + albumin <3.0 g/dL + edema + hyperlipidemia; the worked case (4.2 g/day, albumin 2.4) meets all four.",
            "Primary causes: minimal change (children, steroid-responsive), FSGS, membranous (anti-PLA2R in most primary cases).",
            "Secondary causes: diabetes (commonest worldwide), lupus, amyloidosis, drugs, malignancy.",
            "Complications: thrombosis (renal vein in membranous), infection, AKI - they drive management as much as the cause.",
            "Lipiduria (fatty casts, oval fat bodies) is the classic urinary extra.",
        ],
        "requirements": [
            "The four syndrome criteria with their thresholds.",
            "Primary vs secondary cause lists.",
            "The complication triad and what each demands.",
        ],
        "standards": [
            "Proteinuria in g/day; albumin in g/dL; ACR-to-daily-protein approximation stated.",
            "Antibody associations (anti-PLA2R) stated with their diagnostic role.",
            "Biopsy indications distinguished from serologic diagnosis.",
        ],
        "citations": [CIT_KDIGO_GN, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: nephrotic syndrome is the cartridges "
            "torn open - the mesh ripped wide enough to dump the plant's "
            "most valuable cargo (albumin) into the effluent at 4.2 grams "
            "a day on the worked case, blood albumin sagging to 2.4. The "
            "plant floods its own grounds (edema), the liver panics and "
            "overproduces everything - cholesterol and clotting factors "
            "both - while the natural anticoagulant washes out with the "
            "protein: a thrombosis trap, especially the renal vein in "
            "membranous disease. Each tear pattern has its signature: "
            "podocytes flattened smooth (minimal change, children, melts "
            "under steroids), scarred segments (FSGS), immune crust under "
            "the membrane with a PLA2R fingerprint in the blood."
        ),
    },
    {
        "key": "dkd",
        "name": "Diabetic Kidney Disease",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Diabetic kidney disease is the leading cause of kidney failure "
            "worldwide: about 40 percent of people with diabetes develop "
            "it. Hyperglycemia injures the glomerulus through "
            "hyperfiltration, advanced glycation end-products, and "
            "podocyte loss; the clinical march is microalbuminuria (A2, "
            "30-300 mg/g) to macroalbuminuria (A3) to falling GFR over "
            "years. Screening is annual ACR plus eGFR in every diabetic "
            "patient. A worked example of rapid progression: eGFR 62 "
            "falling to 48 over 2 years is a decline of 7 mL/min/1.73 m2 "
            "per year - above the 5-per-year rapid-progression threshold "
            "that triggers intensified therapy. Treatment per KDIGO 2022: "
            "glycemic control (A1C target individualized, about 7 percent "
            "for most), blood pressure control, ACE inhibitor or ARB, "
            "SGLT2 inhibitor (the breakthrough - slows progression even "
            "at low GFR), finerenone for residual albuminuria, statins, "
            "smoking cessation. Once GFR is severely reduced, glycemic "
            "targets relax because hypoglycemia risk rises as insulin "
            "clearance falls."
        ),
        "how_it_works": (
            "Early diabetes hyperfilters: high glucose drives proximal "
            "SGLT2-mediated sodium reabsorption, tubuloglomerular feedback "
            "relaxes, the afferent arteriole dilates, and single-nephron "
            "GFR soars - injuring podocytes over years. SGLT2 inhibitors "
            "reverse exactly this: blocking proximal sodium reabsorption "
            "restores tubuloglomerular feedback, constricts the afferent "
            "arteriole, and drops intraglomerular pressure - kidney "
            "protection independent of glucose lowering, proven in CREDENCE, "
            "DAPA-CKD, and EMPA-KIDNEY. RAAS blockade cuts the efferent "
            "side of the pressure equation and proteinuria with it. "
            "Finerenone (nonsteroidal mineralocorticoid antagonist) adds "
            "albuminuria and outcome benefit on top (FIDELIO/FIGARO). "
            "Biopsy is reserved for atypical features - nephrotic-range "
            "proteinuria without retinopathy, active urine sediment, rapid "
            "GFR fall - since diabetic nephropathy is usually a clinical "
            "diagnosis. The demo computes the 7-per-year eGFR slope and "
            "the rapid-progressor call."
        ),
        "key_points": [
            "Diabetic kidney disease causes most kidney failure worldwide; about 40 percent of diabetics develop it.",
            "March: microalbuminuria (A2) to macroalbuminuria (A3) to falling GFR; screen every diabetic annually with ACR + eGFR.",
            "eGFR 62 to 48 over 2 years = 7/year decline - above the 5/year rapid-progression threshold.",
            "SGLT2 inhibitors protect by restoring tubuloglomerular feedback and cutting intraglomerular pressure (CREDENCE, DAPA-CKD, EMPA-KIDNEY).",
            "KDIGO 2022 core: A1C ~7 percent, BP control, ACEi/ARB, SGLT2 inhibitor, finerenone for residual albuminuria, statin.",
        ],
        "requirements": [
            "The DKD natural history and screening rule.",
            "The hyperfiltration mechanism and how SGLT2 blockade reverses it.",
            "The KDIGO 2022 treatment stack with landmark trials.",
        ],
        "standards": [
            "eGFR slopes in mL/min/1.73 m2 per year with the 5/year threshold.",
            "Trial names cited for the breakthrough therapies.",
            "Atypical features triggering biopsy listed explicitly.",
        ],
        "citations": [CIT_KDIGO_DIAB, CIT_KDIGO_CKD, CIT_BRENNER],
        "sig_lens": (
            "His Signature reading: diabetic kidney disease is the plant "
            "being force-fed sugar for decades until the cartridges burn "
            "out - the commonest way treatment plants die on earth, "
            "forty percent of diabetics. The injury starts as overwork: "
            "sugar drags salt into the proximal line, the feedback sensor "
            "goes quiet, the inlet valves gape open, and every cartridge "
            "hyperfilters itself to death over years. The SGLT2 "
            "inhibitors are the elegant fix - they jam the sugar-salt "
            "intake valve, wake the feedback sensor back up, and the "
            "inlet valves close to sane pressure. The worked case shows "
            "the rust accelerating: 7 points of filtration a year, past "
            "the 5-point red line - intensify everything, now."
        ),
    },
    {
        "key": "htn_kidney",
        "name": "Hypertension and the Kidney",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The kidney and blood pressure injure each other in both "
            "directions: hypertension scars the kidney (arterionephro-"
            "sclerosis), and kidney disease raises blood pressure (sodium "
            "retention, RAAS and sympathetic activation). Mean arterial "
            "pressure - the perfusion number - is DBP + (SBP - DBP)/3: for "
            "160/90 that is 90 + 70/3 = 113.3 mmHg, well above the "
            "perfusion the kidney wants to see. KDIGO 2021 sets the CKD "
            "target at systolic below 120 mmHg by standardized office "
            "measurement (the SPRINT-informed target), with ACE inhibitor "
            "or ARB first-line in albuminuric CKD. Malignant hypertension "
            "(severe elevation with papilledema, encephalopathy, or AKI) is "
            "the emergency: lower MAP by about 20-25 percent in the first "
            "hours, never to normal abruptly - the brain's autoregulation "
            "has reset upward and fast drops cause stroke. Renovascular "
            "hypertension (atherosclerotic or fibromuscular dysplasia) is "
            "the curable subset to hunt in young, abrupt, or resistant "
            "cases."
        ),
        "how_it_works": (
            "Pressure natriuresis is the long-term controller: high "
            "arterial pressure forces salt and water out until volume - "
            "and pressure - fall back (Guyton's infinite-gain principle). "
            "The kidney sets the set-point via RAAS: low perfusion releases "
            "renin, angiotensin II constricts vessels and releases "
            "aldosterone, sodium is retained, pressure rises. In CKD the "
            "set-point ratchets up as nephrons are lost. ACE inhibitors "
            "and ARBs break the loop at the angiotensin step - dilating "
            "the efferent arteriole, which lowers intraglomerular pressure "
            "(the kidney-protective effect) at the cost of a small, "
            "expected creatinine rise up to 30 percent. Resistant "
            "hypertension (three drugs including a diuretic) in CKD usually "
            "means volume: the thiazide-to-loop switch as GFR falls, plus "
            "sodium restriction. The demo computes MAP 113.3 mmHg for "
            "160/90."
        ),
        "key_points": [
            "Kidney and pressure injure each other both ways: hypertension scars nephrons; nephron loss raises pressure.",
            "MAP = DBP + (SBP - DBP)/3; 160/90 gives 113.3 mmHg.",
            "KDIGO 2021 CKD target: systolic below 120 mmHg by standardized measurement; ACEi/ARB first-line with albuminuria.",
            "Malignant hypertension: lower MAP about 20-25 percent in hours, never abruptly to normal.",
            "Resistant hypertension in CKD usually means volume: switch thiazide to loop as GFR falls, restrict sodium.",
        ],
        "requirements": [
            "The MAP formula and the pressure-natriuresis concept.",
            "The KDIGO 2021 target and first-line agents with their renal mechanism.",
            "The malignant-hypertension lowering rule and its rationale.",
        ],
        "standards": [
            "Pressures in mmHg; MAP formula shown with the one-third pulse-pressure term.",
            "Guideline targets cited to KDIGO 2021 with the measurement caveat.",
            "Expected ACEi creatinine rise (up to 30 percent) stated as normal.",
        ],
        "citations": [CIT_KDIGO_BP, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the kidney is both the victim and the "
            "enforcer of blood pressure - the plant sets the pressure of "
            "the entire municipal system through salt and the RAAS signal "
            "wires, and high pressure in turn sandblasts the plant's own "
            "arterioles into scar. MAP 113.3 on the worked case is the "
            "system running hot. The superintendent's orders per KDIGO "
            "2021: get the top number under 120 (measured properly), lead "
            "with the angiotensin blockers that ease pressure inside the "
            "cartridges themselves, and when the pressure will not budge "
            "on three drugs, look at the tanks - it is volume, it is "
            "almost always volume."
        ),
    },
    {
        "key": "pkd",
        "name": "Polycystic Kidney Disease and Inherited Kidney Disorders",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Autosomal dominant polycystic kidney disease (ADPKD) is the "
            "commonest inherited kidney disease - about 1 in 400 to 1 in "
            "1,000 people - caused by PKD1 or PKD2 mutations that make "
            "tubule cells proliferate into fluid-filled cysts. Kidneys "
            "enlarge massively (often over 16 cm) while function holds for "
            "decades, then declines as cysts strangle surviving parenchyma; "
            "about half reach kidney failure by age 60. A worked "
            "population example: in 400,000 people at 1 in 800 prevalence, "
            "about 500 cases are expected. Extrarenal flags: liver cysts, "
            "intracranial aneurysms (screen families with a history), "
            "mitral valve prolapse, colonic diverticula. Tolvaptan (a V2 "
            "receptor antagonist) slows cyst growth and GFR decline in "
            "rapid progressors - blocking the cAMP signal that drives "
            "cyst fluid secretion. Other inherited disorders: Alport "
            "syndrome (COL4A mutations - hematuria, sensorineural deafness, "
            "lenticonus), thin basement membrane disease, autosomal "
            "recessive PKD (children, with liver fibrosis), Fabry disease "
            "(X-linked, treatable with enzyme replacement)."
        ),
        "how_it_works": (
            "Polycystin-1 and -2 (the PKD1/PKD2 proteins) sit in the "
            "primary cilium of tubule cells, sensing flow; mutant "
            "polycystins derange intracellular calcium and raise cAMP, "
            "which drives both cell proliferation and chloride-driven "
            "fluid secretion into cysts via CFTR. Vasopressin acting on "
            "V2 receptors raises cAMP further - which is why tolvaptan, "
            "blocking V2, slows the disease (TEMPO trial), and why high "
            "water intake is advised. Progression is tracked by "
            "height-adjusted total kidney volume on MRI (the Mayo "
            "classification predicts GFR decline) rather than creatinine, "
            "which stays normal until late. Family screening is by "
            "ultrasound using age-specific cyst-count criteria. Alport "
            "syndrome's defective type IV collagen splits the glomerular "
            "basement membrane (basket-weave on EM); ACE inhibitors slow "
            "its progression. The demo computes the expected case count "
            "of 500 in 400,000 people."
        ),
        "key_points": [
            "ADPKD: 1 in 400-1,000, PKD1/PKD2, massive cystic kidneys; about half reach kidney failure by 60; 400,000 people at 1:800 gives about 500 cases.",
            "Mechanism: mutant polycystins raise cAMP driving cyst growth; tolvaptan (V2 blocker) slows it.",
            "Track progression by MRI kidney volume (Mayo classes), not creatinine - function holds until late.",
            "Extrarenal: liver cysts, intracranial aneurysms (screen at-risk families), valve and colon findings.",
            "Alport (COL4A, hematuria + deafness), ARPKD (children + liver fibrosis), Fabry (X-linked, enzyme-treatable).",
        ],
        "requirements": [
            "ADPKD genetics, prevalence, and natural history.",
            "The cAMP mechanism and tolvaptan's rationale.",
            "The extrarenal screening list and the other inherited disorders.",
        ],
        "standards": [
            "Prevalence as a range with the worked population example.",
            "Trial evidence cited for disease-modifying therapy (TEMPO).",
            "Gene names in standard form (PKD1, PKD2, COL4A).",
        ],
        "citations": [CIT_GRANTHAM, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: ADPKD is the plant growing its own "
            "water balloons - a single-gene defect in the flow sensors "
            "(the cilia) lets cAMP run wild, and tubule cells blow up "
            "into thousands of fluid-filled cysts that strangle the "
            "working cartridges. The organs swell to football size while "
            "the gauges read normal for decades - the cruelest lag in "
            "the building. Tolvaptan is the targeted fix: it cuts the "
            "vasopressin signal wire feeding the cAMP loop and slows the "
            "ballooning (TEMPO proved it). Track the rust by MRI volume, "
            "never by creatinine - and screen the family, because the "
            "defect ships with the bloodline."
        ),
    },
    {
        "key": "tin_drug",
        "name": "Tubulointerstitial Disease and Drug-Induced Kidney Injury",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The tubulointerstitium - tubules plus the tissue between them - "
            "is the kidney's largest compartment and the final common "
            "pathway of all chronic injury (fibrosis here is what actually "
            "predicts GFR loss). Acute interstitial nephritis (AIN) is the "
            "allergic pattern: a drug (beta-lactams, PPIs, NSAIDs, "
            "allopurinol, immune checkpoint inhibitors) triggers interstitial "
            "inflammation days to weeks later - the classic triad of fever, "
            "rash, and eosinophilia is actually uncommon; sterile pyuria "
            "with white cell casts and rising creatinine is the real "
            "signature. Chronic interstitial injury comes from obstruction, "
            "reflux, analgesics, lithium, and hypercalcemia. Drug dosing "
            "in kidney disease is the daily application: renally cleared "
            "drugs need reduction - a worked example gives 1,000 mg x "
            "(30/100) = 300 mg when creatinine clearance is 30 versus a "
            "normal 100 mL/min. Nephrotoxin watchlist: aminoglycosides "
            "(ATN), vancomycin, amphotericin, cisplatin, contrast, NSAIDs, "
            "lithium, tenofovir."
        ),
        "how_it_works": (
            "AIN is a delayed hypersensitivity reaction in the "
            "interstitium: drug as hapten, T-cell infiltration, eosinophils "
            "in the tissue - biopsy shows the interstitial infiltrate "
            "with tubulitis. Urine eosinophils are neither sensitive nor "
            "specific; gallium scan is obsolete; biopsy decides. Treatment "
            "is stopping the drug - recovery follows in days to weeks - "
            "with steroids debated but commonly given for severe or "
            "prolonged cases. Chronic injury converges on interstitial "
            "fibrosis and tubular atrophy (IFTA on biopsy reports), driven "
            "by proteinuria, hypoxia, and inflammation regardless of the "
            "original glomerular insult - which is why all CKD care targets "
            "the interstitium indirectly. Drug dosing uses creatinine "
            "clearance as the scaling factor: dose x (patient CrCl / normal "
            "CrCl), or extended intervals for concentration-dependent "
            "killers like aminoglycosides. The demo computes the 300 mg "
            "adjusted dose."
        ),
        "key_points": [
            "AIN: drug-triggered interstitial allergy (beta-lactams, PPIs, NSAIDs, checkpoint inhibitors); the fever-rash-eosinophilia triad is uncommon - sterile pyuria + WBC casts + rising creatinine is the signature.",
            "Interstitial fibrosis (IFTA) is the final common pathway predicting GFR loss in all CKD.",
            "Stop the drug first in AIN; steroids debated, used in severe/prolonged cases; biopsy decides uncertain cases.",
            "Drug dosing scales with CrCl: 1,000 mg x (30/100) = 300 mg in the worked example.",
            "Nephrotoxin watchlist: aminoglycosides, vancomycin, amphotericin, cisplatin, contrast, NSAIDs, lithium, tenofovir.",
        ],
        "requirements": [
            "The AIN presentation, culprit drugs, and diagnostic hierarchy.",
            "IFTA as the final common pathway concept.",
            "The CrCl-based dose scaling rule.",
        ],
        "standards": [
            "Drug classes named with an example each.",
            "Biopsy findings in standard pathology terms (tubulitis, IFTA).",
            "Dose arithmetic shown as the scaling fraction.",
        ],
        "citations": [CIT_BRENNER, CIT_KDIGO_AKI, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the interstitium is the plant's "
            "backfill - the packing between the pipes - and it is where "
            "every kidney disease goes to die: whatever kills the "
            "cartridges, the backfill scars over (IFTA), and the scar is "
            "what the gauges actually track. AIN is an allergic riot in "
            "the backfill, usually started by a drug the plant decided "
            "was an invader - pull the drug and the riot disperses in "
            "days. And the daily arithmetic of the dispensary: the "
            "kidney clears the drugs, so the dose scales with the "
            "clearance - 300 milligrams where 1,000 used to go when the "
            "filters run at 30 percent. The nephrotoxin watchlist hangs "
            "on the dispensary wall like a most-wanted poster."
        ),
    },
    {
        "key": "mbd",
        "name": "Mineral and Bone Disorder of CKD",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "As GFR falls, the kidney cannot excrete phosphate or activate "
            "vitamin D: phosphate rises, calcium falls, and parathyroid "
            "hormone surges - secondary hyperparathyroidism - dissolving "
            "bone to defend blood calcium while calcium-phosphate deposits "
            "calcify vessels and soft tissue. The calcium-phosphate product "
            "is the precipitation gauge: for calcium 9.8 and phosphate 6.5 "
            "mg/dL, the product is 63.7 mg2/dL2 - above the 55 target, "
            "meaning mineral is actively precipitating where it should "
            "not. KDIGO defines CKD-MBD as the triad of laboratory "
            "abnormalities, bone disease (renal osteodystrophy: high- or "
            "low-turnover), and vascular calcification. Management per "
            "KDIGO: phosphate restriction and binders (calcium-based or "
            "not, watching the calcium load), active vitamin D or analogs, "
            "calcimimetics (cinacalcet) to suppress PTH, and parathyroidectomy "
            "for refractory severe disease. Monitor calcium, phosphate, "
            "PTH, and alkaline phosphatase from CKD G3a onward."
        ),
        "how_it_works": (
            "The axis breaks in sequence: falling GFR retains phosphate; "
            "phosphate binds calcium and suppresses 1-alpha-hydroxylase, "
            "so active vitamin D falls and gut calcium absorption with it; "
            "low calcium plus low vitamin D plus high phosphate all drive "
            "parathyroid hyperplasia - PTH climbs into the hundreds (the "
            "worked case implies severe secondary hyperparathyroidism). "
            "FGF23 rises earliest of all, wasting phosphate at the cost of "
            "suppressing vitamin D further. Bone biopsy distinguishes "
            "high-turnover (osteitis fibrosa, PTH-driven) from low-turnover "
            "(adynamic, often from over-suppression) disease - critical "
            "because treatments oppose each other. Vascular calcification "
            "is active cell-mediated bone formation in vessel walls, driven "
            "by hyperphosphatemia and calcium loading - the reason "
            "calcium-based binders are used cautiously. The demo computes "
            "the Ca x P product of 63.7 against the 55 target."
        ),
        "key_points": [
            "CKD-MBD triad: lab abnormalities (Ca, P, PTH, vitamin D), renal osteodystrophy, vascular calcification.",
            "Ca x P product = 9.8 x 6.5 = 63.7 mg2/dL2 in the worked case - above the 55 target, precipitation risk.",
            "Sequence: phosphate retention -> low vitamin D -> low calcium -> PTH surge (secondary hyperparathyroidism); FGF23 rises first.",
            "Bone biopsy separates high-turnover (treat the PTH) from adynamic disease (back off suppression).",
            "Treat: phosphate binders + diet, active vitamin D, calcimimetics, parathyroidectomy for refractory cases; monitor from G3a.",
        ],
        "requirements": [
            "The Ca x P product and the 55 target.",
            "The hormonal sequence of secondary hyperparathyroidism.",
            "The high- vs low-turnover distinction and why it matters.",
        ],
        "standards": [
            "Calcium and phosphate in mg/dL; product in mg2/dL2; PTH in pg/mL.",
            "KDIGO monitoring start (G3a) stated.",
            "Binder classes distinguished by calcium load.",
        ],
        "citations": [CIT_MOE, CIT_KDIGO_CKD, CIT_BRENNER],
        "sig_lens": (
            "His Signature reading: CKD-MBD is the plant's mineral yard "
            "in revolt. The filters can no longer export phosphate or "
            "mint active vitamin D, so phosphate stockpiles, calcium "
            "crashes, and the parathyroid foremen order the bone "
            "warehouse demolished for calcium - while the excess mineral "
            "precipitates into the pipes and vessel walls like scale in "
            "a boiler. The Ca-x-P gauge reads 63.7 against a 55 redline: "
            "actively scaling. The superintendent fights it on four "
            "fronts: bind the phosphate at the loading dock (diet + "
            "binders), restock vitamin D, gag the parathyroids with "
            "calcimimetics, and if the foremen will not stand down, "
            "surgically remove them."
        ),
    },
    {
        "key": "anemia_ckd",
        "name": "Anemia of Chronic Kidney Disease",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The kidney makes erythropoietin (EPO), so CKD causes anemia: "
            "normocytic, normochromic, with inappropriately low EPO for the "
            "hemoglobin - typically emerging below eGFR 60 and universal "
            "in dialysis. A worked example: hemoglobin 9.2 g/dL against a "
            "KDIGO target range of 10.0-11.5 means 1.3 g/dL of correction "
            "is needed - but never above 13, where trials (CHOIR, CREATE, "
            "TREAT) showed harm from full normalization. Iron must be "
            "repleted first: TSAT below 30 percent and ferritin below 500 "
            "ng/mL in dialysis patients marks iron-responsive deficiency, "
            "because inflammation traps iron via hepcidin (functional iron "
            "deficiency). Treatment: IV iron (superior to oral in CKD), "
            "then erythropoiesis-stimulating agents (epoetin, darbepoetin) "
            "titrated to the lowest dose holding hemoglobin in range; "
            "newer HIF stabilizers (roxadustat and class) raise endogenous "
            "EPO orally. Anemia of CKD is a diagnosis of exclusion - check "
            "B12, folate, blood loss, and inflammation first."
        ),
        "how_it_works": (
            "Peritubular interstitial fibroblasts sense hypoxia via HIF and "
            "secrete EPO; in CKD these cells transform into myofibroblasts "
            "and go silent - the anemia of chronic disease plus true EPO "
            "deficiency, compounded by hepcidin-mediated iron blockade "
            "(inflammation raises hepcidin, ferroportin is internalized, "
            "iron locks in macrophages) and shortened red cell survival in "
            "uremia. ESAs replace the missing signal but raise blood "
            "pressure and thrombosis risk at high doses - hence the "
            "10.0-11.5 target band and the 'lowest effective dose' rule. "
            "HIF prolyl-hydroxylase inhibitors stabilize HIF "
            "pharmacologically, coaxing endogenous EPO plus improved iron "
            "mobilization. Transfusion is minimized in transplant "
            "candidates to avoid sensitization. The demo computes the 1.3 "
            "g/dL correction gap and checks the iron thresholds."
        ),
        "key_points": [
            "CKD anemia = EPO deficiency + hepcidin iron blockade + uremic red cell shortening; normocytic, emerging below eGFR 60.",
            "Hemoglobin 9.2 against the 10.0-11.5 target leaves a 1.3 g/dL gap; never target above 13 (CHOIR/CREATE/TREAT harm).",
            "Replete iron first: TSAT <30 percent and ferritin <500 ng/mL marks responsive deficiency in dialysis patients.",
            "ESAs at the lowest effective dose; HIF stabilizers raise endogenous EPO orally.",
            "Diagnosis of exclusion: check B12, folate, blood loss, inflammation; minimize transfusion in transplant candidates.",
        ],
        "requirements": [
            "The EPO-hepcidin pathophysiology.",
            "The hemoglobin target band and the trial evidence behind the ceiling.",
            "The iron-first treatment sequence.",
        ],
        "standards": [
            "Hemoglobin in g/dL; TSAT in percent; ferritin in ng/mL.",
            "Trial names cited for the normalization harm.",
            "Transplant-candidate transfusion caution stated.",
        ],
        "citations": [CIT_KDIGO_CKD, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the kidney is the fleet's recruitment "
            "office - it issues the erythropoietin orders that keep the "
            "red-cell fleet at strength. In CKD the office goes dark: "
            "orders stop, the iron quartermaster (hepcidin) locks the "
            "armory during the inflammation alert, and the fleet shrinks "
            "to 9.2 on the worked case - 1.3 below fighting strength. The "
            "superintendent restocks iron first (the armory must be open "
            "before new orders matter), then issues synthetic orders (ESAs) "
            "at the minimum effective dose - because the trials proved "
            "that over-recruiting to 13 kills. The new HIF drugs are "
            "forged orders that trick the office back open."
        ),
    },
    {
        "key": "hemodialysis",
        "name": "Hemodialysis: Principles and Prescription",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Hemodialysis is the auxiliary treatment plant: blood pumped "
            "through a dialyzer where diffusion across a semipermeable "
            "membrane clears uremic toxins into dialysate, while "
            "ultrafiltration removes water by pressure. The standard "
            "prescription is 3 sessions per week, about 4 hours each, "
            "through an arteriovenous fistula - the preferred access "
            "(fistula first: lowest infection and mortality). Adequacy is "
            "measured by single-pool Kt/V (target at least 1.2 per session) "
            "and the urea reduction ratio (target at least 65 percent). A "
            "worked Daugirdas calculation: pre-BUN 60, post-BUN 18, 4-hour "
            "session, 2.5 L ultrafiltration, 70-kg patient gives spKt/V = "
            "1.42 - above target, an adequate session. Complications are "
            "intradialytic hypotension (commonest), cramps, dialysis "
            "disequilibrium in the first sessions, and access infection or "
            "stenosis. Continuous renal replacement therapy (CRRT) is the "
            "ICU variant: slow, 24-hour, for hemodynamically unstable AKI."
        ),
        "how_it_works": (
            "Diffusion moves solute down its concentration gradient: blood "
            "urea 60 mg/dL against dialysate urea near zero, across "
            "thousands of hollow fibers with total surface 1.5-2.5 m2. "
            "Small solutes (urea, creatinine, potassium) clear fast; "
            "'middle molecules' (beta-2 microglobulin) need high-flux "
            "membranes and convection. Ultrafiltration is pressure-driven: "
            "the machine sets a transmembrane pressure, plasma water "
            "crosses, and the patient's refill from the interstitium must "
            "keep up - when it cannot, blood pressure crashes "
            "(intradialytic hypotension). Kt/V formalizes dose: K (dialyzer "
            "urea clearance) x t (time) / V (urea distribution volume, "
            "about total body water). The Daugirdas second-generation "
            "formula corrects the simple log ratio for urea generation "
            "during dialysis and ultrafiltration contraction. The demo "
            "computes spKt/V 1.42 for the worked session."
        ),
        "key_points": [
            "Hemodialysis = diffusion clears toxins + ultrafiltration removes water; standard 3x/week, ~4 hours, via AV fistula.",
            "Adequacy: spKt/V at least 1.2, URR at least 65 percent; the worked session gives spKt/V 1.42 - adequate.",
            "Fistula first: AV fistula has the lowest infection and mortality of accesses; avoid catheters long-term.",
            "Commonest complication is intradialytic hypotension - ultrafiltration outrunning vascular refill.",
            "CRRT is the slow 24-hour ICU variant for unstable AKI; disequilibrium strikes the first sessions.",
        ],
        "requirements": [
            "The diffusion/ultrafiltration mechanisms and what each removes.",
            "The Kt/V concept and the Daugirdas calculation.",
            "Access hierarchy and the top complications.",
        ],
        "standards": [
            "BUN in mg/dL; time in hours; ultrafiltration in liters; weight in kg.",
            "Adequacy targets stated per KDOQI/KDIGO.",
            "Worked example shows the full Daugirdas substitution.",
        ],
        "citations": [CIT_DAUGIRDAS, CIT_HIMMELFARB, CIT_BRENNER],
        "sig_lens": (
            "His Signature reading: hemodialysis is the auxiliary "
            "treatment plant wheeled up beside the failed one - blood "
            "out one hose, through ten thousand hollow-fiber cartridges "
            "bathed in clean dialysate, blood back the other hose, three "
            "shifts a week, four hours a shift. Diffusion does the "
            "chemical work (toxins marching down their gradients into "
            "the dialysate river), pressure does the water work. The "
            "dose gauge is Kt/V: 1.42 on the worked session, past the 1.2 "
            "redline, a full shift's work done. The fistula is the "
            "permanent hookup - a surgically fattened vein that can take "
            "the flows for years. Run the water off faster than the "
            "tissues refill and the pressure crashes: the commonest "
            "mid-shift emergency in the building."
        ),
    },
    {
        "key": "peritoneal",
        "name": "Peritoneal Dialysis and Dialysis Adequacy",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Peritoneal dialysis turns the patient's own peritoneal "
            "membrane into the dialyzer: dialysate dwells in the abdomen, "
            "toxins diffuse from peritoneal capillaries, and dextrose in "
            "the fluid osmotically pulls water (ultrafiltration). Two "
            "modalities: CAPD (continuous ambulatory - 4 manual exchanges "
            "daily) and APD (automated - a cycler overnight). A worked "
            "adequacy example: a weekly Kt/V of 1.9 clears the KDIGO/KDOQI "
            "target of at least 1.7 per week. The peritoneal equilibration "
            "test (PET) classifies transport: high transporters clear "
            "solute fast but lose the osmotic gradient early (short dwells, "
            "APD suits them); low transporters need long dwells (CAPD). "
            "Advantages: home-based, no heparin, better early survival and "
            "preserved residual kidney function. The signature complication "
            "is peritonitis - cloudy effluent with abdominal pain means "
            "cell count and culture immediately, then intraperitoneal "
            "antibiotics; exit-site and tunnel infections threaten the "
            "catheter."
        ),
        "how_it_works": (
            "Transport across the peritoneum follows the three-pore model: "
            "small pores pass small solutes, large pores pass protein "
            "(albumin loss is the chronic cost), ultrasmall aquaporin pores "
            "pass pure water (sodium sieving - early-dwell low-sodium "
            "ultrafiltrate). Dextrose (1.5, 2.5, 4.25 percent) sets the "
            "osmotic pull; icodextrin gives sustained ultrafiltration for "
            "long dwells without the glucose load. Adequacy sums renal and "
            "peritoneal Kt/V weekly - residual kidney function counts, "
            "which is why PD preserves it jealously (avoid nephrotoxins, "
            "ACEi/ARB may help). Peritonitis diagnosis is effluent white "
            "cells above 100 per microliter with at least 50 percent "
            "neutrophils after a 2-hour dwell; empiric coverage hits gram-"
            "positives (touch contamination) and gram-negatives. The demo "
            "checks the weekly Kt/V of 1.9 against the 1.7 target."
        ),
        "key_points": [
            "PD uses the peritoneum as the membrane: CAPD (4 manual exchanges/day) or APD (cycler overnight).",
            "Weekly Kt/V target at least 1.7; the worked example gives 1.9 - adequate.",
            "PET classifies transport: high transporters suit short-dwell APD; low transporters suit long-dwell CAPD.",
            "Residual kidney function counts toward adequacy - PD preserves it better than hemodialysis.",
            "Peritonitis = cloudy effluent + pain: cell count and culture at once, then intraperitoneal antibiotics.",
        ],
        "requirements": [
            "The PD transport mechanism (diffusion + dextrose osmosis).",
            "The weekly Kt/V target and the PET-based modality choice.",
            "The peritonitis diagnostic threshold and empiric treatment.",
        ],
        "standards": [
            "Kt/V weekly with the 1.7 target; effluent cell counts per microliter.",
            "Dextrose strengths in percent; icodextrin named for long dwells.",
            "Modality choice tied to transport type explicitly.",
        ],
        "citations": [CIT_DAUGIRDAS, CIT_BRENNER, CIT_KDIGO_CKD],
        "sig_lens": (
            "His Signature reading: peritoneal dialysis is the "
            "do-it-yourself treatment plant - no trips to the facility, "
            "the patient's own abdominal lining becomes the membrane. "
            "Fill the belly with dextrose dialysate, let the toxins "
            "diffuse out of the gut's blood supply for a few hours, "
            "drain, repeat - four manual swaps a day or a cycler that "
            "works the night shift while the patient sleeps. The weekly "
            "dose gauge reads 1.9 against the 1.7 redline on the worked "
            "case. The membrane even lets the surviving native plant "
            "keep contributing - residual function counts, and PD "
            "husbands it. The standing emergency drill: cloudy drain "
            "fluid plus belly pain is peritonitis until proven otherwise "
            "- sample it, culture it, flood it with antibiotics through "
            "the catheter itself."
        ),
    },
    {
        "key": "transplant",
        "name": "Kidney Transplantation: Immunology and Concepts",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Kidney transplantation is the best renal replacement therapy: "
            "longer life, better quality of life, and lower cost than "
            "dialysis - with about 95 percent one-year graft survival for "
            "living-donor kidneys (about 95 of 100 functioning at a year). "
            "Workup is the art of the possible: HLA typing (A, B, DR loci), "
            "panel reactive antibody (PRA) measuring sensitization from "
            "pregnancy, transfusion, or prior transplant, and the crossmatch "
            "(donor cells plus recipient serum - positive means hyperacute "
            "rejection risk, a hard stop). Living donation is preferred: "
            "preemptive transplant (before dialysis) gives the best "
            "outcomes. Immunosuppression is triple therapy - tacrolimus "
            "(calcineurin inhibitor), mycophenolate, steroids - with "
            "induction (basiliximab or thymoglobulin). Rejection types: "
            "hyperacute (minutes, preformed antibody), acute cellular "
            "(days-weeks, T-cell, treatable with steroid pulses), acute "
            "antibody-mediated (donor-specific antibodies, needs plasma "
            "exchange/IVIG), chronic (months-years, the long attrition). "
            "The price of the graft is lifelong infection and malignancy "
            "vigilance."
        ),
        "how_it_works": (
            "The immune barrier is HLA: the more mismatches at A, B, and "
            "DR, the stronger the alloresponse - zero-mismatch kidneys "
            "last longest. Desensitization (plasma exchange, IVIG, "
            "rituximab) can cross low-level antibody barriers; paired "
            "kidney exchange chains turn incompatible donor-recipient pairs "
            "into compatible transplants. The transplanted kidney goes in "
            "the iliac fossa (not the native bed), vessels to the iliac "
            "artery and vein, ureter to the bladder - native kidneys stay "
            "unless they cause trouble. Calcineurin inhibitors block IL-2 "
            "transcription in T cells but are nephrotoxic themselves - the "
            "central paradox of transplant nephrology, managed by drug-"
            "level monitoring. BK virus nephropathy is the signature "
            "opportunist: screen BK PCR in blood, reduce immunosuppression "
            "at the first rise. The demo works the graft-survival "
            "expectation: 95 of 100 living-donor grafts at one year."
        ),
        "key_points": [
            "Transplant beats dialysis on survival, quality of life, and cost; living-donor one-year graft survival is about 95 percent.",
            "Workup: HLA typing, PRA (sensitization), crossmatch - a positive crossmatch is a hard stop.",
            "Preemptive living-donor transplant gives the best outcomes; paired exchange chains multiply the matches.",
            "Triple immunosuppression (tacrolimus, mycophenolate, steroids) + induction; calcineurin inhibitors are nephrotoxic - monitor levels.",
            "Rejection ladder: hyperacute (minutes), acute cellular (steroid-responsive), antibody-mediated (plasma exchange/IVIG), chronic (attrition).",
        ],
        "requirements": [
            "The HLA/PRA/crossmatch workup and what each rules out.",
            "The immunosuppression stack with mechanisms.",
            "The rejection types with tempo and treatment.",
        ],
        "standards": [
            "Survival as percent with the donor type specified.",
            "Drug classes with their molecular targets.",
            "Surgical placement described (iliac fossa, not native bed).",
        ],
        "citations": [CIT_KASISKE, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: transplantation is the full plant "
            "swap - and it beats running the auxiliary unit on every "
            "measure that matters: 95 of 100 living-donor plants still "
            "online at a year. The swap's difficulty is entirely "
            "diplomatic: the recipient's immune border guards check "
            "every donor plant's papers (HLA), and pre-cleared grudges "
            "(antibodies from pregnancy, transfusion, prior swaps) mean "
            "instant demolition - hyperacute rejection in minutes. The "
            "peace treaty is triple-drug immunosuppression, with the "
            "paranoid twist that the chief peacemaker (tacrolimus) "
            "poisons the plant it protects - hence the blood-level "
            "monitoring, forever. Paired exchange chains are diplomacy "
            "at scale: your incompatible donor saves a stranger, whose "
            "donor saves you."
        ),
    },
    {
        "key": "pregnancy",
        "name": "Pregnancy and the Kidney: Preeclampsia",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Pregnancy hyperfilters: GFR rises about 50 percent, so a "
            "creatinine of 0.8 mg/dL is the new normal and 1.0 deserves "
            "workup - the reference range shifts down. Preeclampsia is the "
            "kidney-vascular emergency of pregnancy: hypertension after 20 "
            "weeks plus proteinuria (at least 300 mg/day) or end-organ "
            "signs (thrombocytopenia, liver dysfunction, pulmonary edema, "
            "neurologic symptoms). A worked example: BP 150/100 (MAP = "
            "100 + 50/3 = 116.7 mmHg) with 400 mg/day proteinuria after 20 "
            "weeks meets criteria. The placenta is the culprit: abnormal "
            "spiral-artery remodeling releases anti-angiogenic factors "
            "(sFlt-1) that injure maternal endothelium, including "
            "glomerular endotheliosis. Severe features (BP at least 160/110, "
            "platelets below 100,000, doubling creatinine, pulmonary edema, "
            "unremitting headache) demand delivery - the only cure - plus "
            "magnesium sulfate for seizure prophylaxis and controlled BP "
            "lowering. Low-dose aspirin from 12 weeks prevents preeclampsia "
            "in high-risk women."
        ),
        "how_it_works": (
            "Normal pregnancy vasodilates systemically: RAAS activates but "
            "vessels resist it, GFR and renal plasma flow climb, and "
            "proteinuria up to 300 mg/day is tolerated. In preeclampsia "
            "the ischemic placenta secretes sFlt-1 and soluble endoglin, "
            "which scavenge VEGF and PlGF - glomerular endothelial cells, "
            "addicted to VEGF, swell (endotheliosis), the filtration "
            "barrier leaks protein, and systemic endothelial dysfunction "
            "produces the hypertension, liver injury (HELLP: hemolysis, "
            "elevated liver enzymes, low platelets), and cerebral edema. "
            "The sFlt-1/PlGF ratio now aids diagnosis. Management is "
            "delivery timed to severity: at term, deliver; preterm with "
            "severe features, stabilize and deliver; mild preterm, watch "
            "closely. ACE inhibitors and ARBs are teratogenic - "
            "antihypertensives in pregnancy are labetalol, nifedipine, "
            "methyldopa, hydralazine. The demo checks the worked case "
            "against the diagnostic criteria."
        ),
        "key_points": [
            "Pregnancy raises GFR ~50 percent: creatinine 0.8 is normal, 1.0 deserves workup.",
            "Preeclampsia = hypertension after 20 weeks + proteinuria >=300 mg/day or end-organ signs; the worked case (150/100, 400 mg/day) meets criteria.",
            "Placental sFlt-1 injures maternal endothelium (glomerular endotheliosis); the sFlt-1/PlGF ratio aids diagnosis.",
            "Delivery is the only cure; magnesium sulfate prevents seizures; severe features trigger delivery regardless of gestation.",
            "ACEi/ARBs are teratogenic: use labetalol, nifedipine, methyldopa, hydralazine; low-dose aspirin from 12 weeks prevents recurrence.",
        ],
        "requirements": [
            "The shifted creatinine reference in pregnancy.",
            "The preeclampsia diagnostic criteria and severe features.",
            "The placental mechanism and the delivery-centered management.",
        ],
        "standards": [
            "Blood pressure thresholds in mmHg; proteinuria in mg/day; MAP worked explicitly.",
            "Teratogenic drugs named with safe alternatives.",
            "HELLP expanded on first use.",
        ],
        "citations": [CIT_SIBAI, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: pregnancy rebuilds the plant's "
            "operating envelope - flow up 50 percent, the ash gauge "
            "recalibrated so that 0.8 is the new normal. Preeclampsia is "
            "the placenta going rogue: a starving placenta broadcasts "
            "anti-angiogenic sabotage (sFlt-1) that swells the "
            "glomerular endothelium shut and spikes the system pressure - "
            "150/100 with 400 milligrams of protein a day on the worked "
            "case, past every diagnostic line. There is exactly one "
            "cure and it is not a drug: deliver the placenta. Until "
            "then, magnesium sulfate stands guard against seizures and "
            "the pressure is lowered gently - because the usual "
            "angiotensin blockers are poison to the fetus."
        ),
    },
    {
        "key": "peds",
        "name": "Pediatric Nephrology: The Growing Kidney",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Children are not small adults to the nephrologist: GFR is "
            "estimated by the bedside Schwartz equation - eGFR = 0.413 x "
            "height(cm) / creatinine(mg/dL). A worked example: height 110 "
            "cm, creatinine 0.8 gives 0.413 x 110 / 0.8 = 56.8 "
            "mL/min/1.73 m2 - moderately decreased, abnormal for a child. "
            "Congenital anomalies of the kidney and urinary tract (CAKUT) "
            "cause most pediatric CKD; posterior urethral valves in boys "
            "and vesicoureteral reflux lead the obstructive causes. "
            "Minimal change disease causes most childhood nephrotic "
            "syndrome and usually melts under steroids - biopsy is "
            "reserved for steroid resistance, older age, or atypical "
            "features. Hemolytic uremic syndrome (Shiga-toxin E. coli) is "
            "the classic pediatric AKI triad: microangiopathic hemolytic "
            "anemia, thrombocytopenia, and AKI - supportive care, never "
            "antibiotics or antimotility agents in the acute phase. Growth "
            "is the vital sign: CKD stunts it (growth hormone helps), and "
            "dosing is by body surface area, not adult flat doses."
        ),
        "how_it_works": (
            "Nephrogenesis finishes by 36 weeks gestation - no new nephrons "
            "after birth - so prematurity and low birth weight permanently "
            "reduce nephron endowment and raise adult CKD risk (Brenner "
            "hypothesis). The Schwartz constant 0.413 assumes the "
            "creatinine-height relationship of muscle mass in children; "
            "cystatin C refines it when muscle is abnormal. Vesicoureteral "
            "reflux is graded I-V on voiding cystourethrogram; high-grade "
            "reflux with recurrent febrile UTIs scars kidneys "
            "(reflux nephropathy) - continuous antibiotic prophylaxis vs "
            "surgical reimplantation is the long debate. Steroid-sensitive "
            "nephrotic syndrome relapses are handled with relapse protocols "
            "rather than repeated biopsies; calcineurin inhibitors and "
            "rituximab serve steroid-sparing roles. Transition to adult "
            "care is a planned handoff, not a birthday. The demo computes "
            "the Schwartz eGFR of 56.8."
        ),
        "key_points": [
            "Schwartz eGFR = 0.413 x height/creatinine; 110 cm and 0.8 mg/dL gives 56.8 mL/min/1.73 m2 - abnormal for a child.",
            "No new nephrons after 36 weeks gestation: prematurity permanently lowers nephron endowment.",
            "CAKUT causes most pediatric CKD; posterior urethral valves and reflux lead the obstructive causes.",
            "Childhood nephrotic syndrome is usually minimal change and steroid-sensitive; biopsy is for resistance or atypical features.",
            "HUS triad (Shiga-toxin E. coli): hemolytic anemia + thrombocytopenia + AKI - supportive care only, no antibiotics acutely.",
        ],
        "requirements": [
            "The Schwartz equation and when it applies.",
            "The CAKUT-first etiology pattern and the valve/reflux workup.",
            "The HUS triad and its contraindicated treatments.",
        ],
        "standards": [
            "Height in cm, creatinine in mg/dL, eGFR in mL/min/1.73 m2.",
            "Grading systems named (reflux I-V).",
            "Growth stated as the pediatric vital sign with its intervention.",
        ],
        "citations": [CIT_SCHWARTZ, CIT_BRENNER, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the pediatric plant is still under "
            "construction - and the concrete sets at 36 weeks gestation: "
            "not one new cartridge after that, ever, so a premature "
            "start means a smaller plant for life. The gauges are "
            "recalibrated for small operators: the Schwartz slide rule - "
            "0.413 times height over ash - reads 56.8 on the worked "
            "case, abnormal for a child where it would pass for an "
            "adult. Most childhood plant failures are plumbing defects "
            "from the build (CAKUT) or the classic childhood filter "
            "melt (minimal change - steroids fix it, no biopsy needed). "
            "And growth is the master gauge: a plant in trouble stunts "
            "the whole construction project."
        ),
    },
    {
        "key": "future",
        "name": "The Future of Nephrology: Wearable Kidneys and Xenotransplantation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Nephrology's future is measured against its cruelest number: "
            "about 90,000 Americans wait for a kidney while only about "
            "25,000 transplants happen yearly - a 3.6-year average wait "
            "that many do not survive. Three frontiers attack it. "
            "Xenotransplantation: gene-edited pig kidneys (knocking out "
            "alpha-gal and other xenoantigens, adding human complement "
            "regulators) have functioned for months in brain-dead recipients "
            "and early living patients - the first plausible end to the "
            "organ shortage. Wearable and implantable artificial kidneys: "
            "miniaturized dialyzers with sorbent regeneration of dialysate "
            "aim at continuous, unobtrusive clearance instead of "
            "thrice-weekly sessions. Regeneration: kidney organoids from "
            "iPS cells, and bioengineered scaffolds reseeded with patient "
            "cells, chase the truly curative graft. Precision nephrology - "
            "APOL1 genotyping guiding therapy in African-ancestry patients, "
            "molecular biopsy classifiers, AI-read pathology - is already "
            "arriving. The specialty that learned to replace its organ is "
            "learning to rebuild it."
        ),
        "how_it_works": (
            "Xenotransplant barriers fall in order: hyperacute rejection "
            "(solved by knocking out the GGTA1 alpha-gal gene), acute "
            "humoral rejection (human complement-regulatory transgenes like "
            "CD46/CD55), coagulation dysregulation (human thrombomodulin "
            "transgenes), and porcine endogenous retrovirus risk (PERV "
            "knockout). CRISPR multiplex editing makes ten-gene pigs "
            "routine. Wearable kidneys recirculate a small dialysate volume "
            "through sorbent cartridges (urease + zirconium phosphate) "
            "instead of 120 liters per session - continuous clearance, "
            "physiologic volume control. Organoids self-organize nephron "
            "structures from iPS cells but lack vascular integration; "
            "decellularized scaffolds provide the architecture that cells "
            "alone cannot. APOL1 risk variants explain much of the excess "
            "kidney failure in African-ancestry populations and now have "
            "targeted therapy in trials. The demo computes the 3.6-year "
            "waitlist arithmetic."
        ),
        "key_points": [
            "About 90,000 wait vs about 25,000 transplants/year in the US: a 3.6-year average wait driving all three frontiers.",
            "Xenotransplantation: multi-gene-edited pig kidneys (GGTA1 knockout, human complement regulators) functioning for months in humans.",
            "Wearable kidneys: sorbent-regenerated dialysate for continuous clearance instead of thrice-weekly sessions.",
            "Regeneration: iPS-derived kidney organoids and reseeded scaffolds chase the curative graft.",
            "Precision nephrology now: APOL1 genotyping with targeted therapy in trials, molecular biopsy classifiers, AI pathology.",
        ],
        "requirements": [
            "The waitlist arithmetic and why it motivates the frontiers.",
            "The xenotransplant barrier sequence and the gene edits addressing each.",
            "The wearable-kidney sorbent concept and the organoid vascularization limit.",
        ],
        "standards": [
            "Waitlist numbers as US approximations with 'about' qualifiers.",
            "Gene edits named (GGTA1, CD46/CD55, PERV).",
            "Trial-stage honesty: what is in humans vs in the lab.",
        ],
        "citations": [CIT_BRENNER, CIT_HARRISON, CIT_KASISKE],
        "sig_lens": (
            "His Signature reading: the plant superintendent's hardest "
            "number is 3.6 - years the average American waits for a donor "
            "plant while 90,000 stand in line for 25,000 annual slots. So "
            "the industry is building three escape routes at once. "
            "Xenotransplantation: gene-edited pig plants with the "
            "rejection triggers deleted and human camouflage installed - "
            "ten-gene pigs are now routine, and the organs have run for "
            "months in people. Wearables: a belt-sized auxiliary plant "
            "that regenerates its own dialysate through sorbent "
            "cartridges, running continuously instead of three brutal "
            "shifts a week. And the long bet - growing the cartridges "
            "themselves from the patient's own starter cells. The "
            "specialty that learned to replace its organ is learning to "
            "rebuild it."
        ),
    },
]
