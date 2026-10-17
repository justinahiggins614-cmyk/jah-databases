#!/usr/bin/env python3
"""Entries for the Gastroenterology field databases (field #38, taxonomy order).

Verified 2026-10-17: NO database covers gastroenterology as a clinical
specialty (esophagus, stomach, small/large intestine, liver/biliary,
pancreas; GERD, ulcers, IBD, IBS, celiac, GI bleeding, liver disease,
pancreatitis, GI cancers, endoscopy concepts, gut microbiome clinical
aspects). Clinical-specialty framing, distinct from anatomy/histology.

Manifest search (2,376 databases): zero 'gastroenterolog*' slugs/names; no
db/gastroenterolog* dirs. Whole-system exact-title sweep over the manifest
plus every shard index 't' key: zero collisions for all 34 planned titles
x2 editions (68 variants). The persisted dedupe gate dir (data/dedupe/exact)
is stale for the newest fields, so the raw sweep above is the authoritative
preflight; the build's in-run gate admission still applies for the new slugs.
Near-neighbors confirmed different disciplines: 'hepatology' is MISSING
(n=558, not yet built), 'endocrinology' covers the hormone system including
only pancreatic endocrine function, diabetes coverage is fragmented across
general health databases, 'nutrition' databases cover food science not the
clinical GI specialty. ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  gastroenterology              - The Gastroenterology Database
                                  (public-harvest: real, fact-checked clinical
                                  gastroenterology; standard references
                                  Feldman et al. "Sleisenger and Fordtran's
                                  Gastrointestinal and Liver Disease" 11th ed
                                  2021; Podolsky et al. "Yamada's Textbook of
                                  Gastroenterology" 7th ed 2022; Jameson et
                                  al. "Harrison's Principles of Internal
                                  Medicine" 21st ed 2022; ACG/AGA/AASLD
                                  clinical guidelines)
  gastroenterology-signature    - The Gastroenterology Signature Database
                                  (his original Signature interpretation of
                                  the digestive system as the body's intake,
                                  refining, and logistics works; src
                                  signature, titles suffixed
                                  " (Signature Edition)", never presented as
                                  authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-GAS- (public) and JAH-GASS- (signature), both verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of the "
            "digestive system as the body's intake, refining, and logistics "
            "works: the gut as the receiving dock, enzymes as the processing "
            "crews, the liver as the refinery, bile as the solvent line, the "
            "microbiome as the resident workforce, and every disorder a "
            "breakdown in the works with a signed work order for the repair. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_SLEIS = ("Feldman M, Friedman LS, Brandt LJ, eds. Sleisenger and Fordtran's "
             "Gastrointestinal and Liver Disease: Pathophysiology, Diagnosis, "
             "Management. 11th ed. Elsevier; 2021.")
CIT_YAMADA = ("Podolsky DK, Camilleri M, Fitz JG, Kalloo AN, Shanahan F, "
              "Wang TC, eds. Yamada's Textbook of Gastroenterology. 7th ed. "
              "Wiley-Blackwell; 2022.")
CIT_HARRISON = ("Jameson JL, Fauci AS, Kasper DL, Hauser SL, Longo DL, "
                "Loscalzo J, eds. Harrison's Principles of Internal Medicine. "
                "21st ed. McGraw Hill; 2022.")
CIT_GERD = ("Katz PO, Dunbar KB, Schnoll-Sussman FH, Greer KB, Yadlapati R, "
            "Spechler SJ. ACG Clinical Guideline for the Diagnosis and "
            "Management of Gastroesophageal Reflux Disease. Am J Gastroenterol. "
            "2022;117(1):27-56.")
CIT_HPYLORI = ("Chey WD, Howden CW, Moss SF, et al. ACG Clinical Guideline: "
               "Treatment of Helicobacter pylori Infection. Am J Gastroenterol. "
               "2017;112(2):212-239.")
CIT_UC = ("Rubin DT, Ananthakrishnan AN, Siegel CA, Sauer BG, Long MD. ACG "
          "Clinical Guideline: Ulcerative Colitis in Adults. Am J Gastroenterol. "
          "2019;114(3):384-413.")
CIT_CROHN = ("Lichtenstein GR, Loftus EV, Isaacs KL, Regueiro MD, Gerson LB, "
             "Sands BE. ACG Clinical Guideline: Management of Crohn's Disease "
             "in Adults. Am J Gastroenterol. 2018;113(4):481-517.")
CIT_CRC = ("Rex DK, Boland CR, Dominitz JA, et al. Colorectal Cancer Screening: "
           "Recommendations for Physicians and Patients From the U.S. "
           "Multi-Society Task Force on Colorectal Cancer. Am J Gastroenterol. "
           "2017;112(7):1016-1030.")
CIT_PANC = ("Tenner S, Baillie J, DeWitt J, Vege SS. American College of "
            "Gastroenterology Guideline: Management of Acute Pancreatitis. "
            "Am J Gastroenterol. 2013;108(9):1400-1415.")
CIT_UGIB = ("Barkun AN, Almadi M, Kuipers EJ, et al. Management of Nonvariceal "
            "Upper Gastrointestinal Bleeding: Guideline Recommendations From "
            "the International Consensus Group. Ann Intern Med. "
            "2019;171(11):805-822.")
CIT_ROME = ("Mearin F, Lacy BE, Chang L, et al. Bowel Disorders. "
            "Gastroenterology. 2016;150(6):1393-1407.")
CIT_CELIAC = ("Rubio-Tapia A, Hill ID, Kelly CP, Calderwood AH, Murray JA. "
              "ACG Clinical Guidelines: Diagnosis and Management of Celiac "
              "Disease. Am J Gastroenterol. 2013;108(5):656-676.")
CIT_HBV = ("Terrault NA, Lok ASF, McMahon BJ, et al. Update on Prevention, "
           "Diagnosis, and Treatment of Chronic Hepatitis B: AASLD 2018 "
           "Hepatitis B Guidance. Hepatology. 2018;67(4):1560-1599.")
CIT_ALD = ("European Association for the Study of the Liver. EASL Clinical "
           "Practice Guidelines: Management of alcohol-related liver disease. "
           "J Hepatol. 2018;69(1):154-181.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Gastroenterology: The Clinical Specialty of the Digestive System",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Gastroenterology is the clinical medical specialty devoted to the "
            "digestive system - the esophagus, stomach, small intestine, large "
            "intestine, liver, gallbladder, biliary tree, and pancreas - and to "
            "the diseases that strike them. The name comes from the Greek "
            "gaster (stomach), enteron (intestine), and logos (study). The "
            "gastroenterologist is the physician who reads the gut: "
            "diagnosing reflux, ulcers, infections, inflammation, obstruction, "
            "bleeding, liver failure, pancreatic disease, and digestive "
            "cancers, and treating them with medicines, diet, endoscopic "
            "procedures, and referral for surgery when the gut cannot be "
            "fixed from the inside. The specialty owns the endoscope - the "
            "camera that travels the inside of the tract - so it is both a "
            "thinking specialty and a procedural one. Roughly nine meters of "
            "tubing, from lips to anus, plus the two great chemical plants "
            "(liver and pancreas) that feed it, form the territory: an "
            "assembly line that turns food into fuel, building blocks, and "
            "waste, and a border post that decides what enters the blood. "
            "This record frames the discipline and the ladder of records that "
            "follows."
        ),
        "how_it_works": (
            "Gastroenterology works on the processing-line model of the gut. "
            "The esophagus (about 25 cm) delivers, the stomach (about 25 cm "
            "along its greater curve) churns and acid-bathes, the small "
            "intestine (about 600 cm) absorbs, and the large intestine (about "
            "150 cm) reclaims water and compacts waste: roughly 800 cm - "
            "eight meters - of tubing in series. Folds, villi, and microvilli "
            "multiply the small intestine's inner surface to about 250 square "
            "meters, some 147 times the skin's 1.7 square meters, which is why "
            "a tube that fits in the abdomen can absorb a day's nutrition. "
            "The liver (about 1.5 kg) and pancreas ride alongside as chemical "
            "plants, injecting bile and enzyme juice into the line. The demo "
            "works the line arithmetic: summing the segment lengths to the "
            "full eight-meter line and showing how surface amplification, not "
            "length alone, gives the gut its absorptive power."
        ),
        "key_points": [
            "Gastroenterology = the clinical specialty of the digestive system: esophagus, stomach, intestines, liver, biliary tree, pancreas.",
            "About 8 meters of tubing in series: 25 cm esophagus, 25 cm stomach, 600 cm small intestine, 150 cm large intestine.",
            "Small-intestine surface amplification reaches about 250 square meters - roughly 147 times the skin area.",
            "The specialty is both cognitive and procedural: diagnosis, medicines, diet, and endoscopy all belong to it.",
            "Distinct from nutrition science (food and diets) and from anatomy (structure alone): gastroenterology is the clinical function-and-failure specialty.",
        ],
        "requirements": [
            "The organ map in order: esophagus, stomach, duodenum, jejunum, ileum, colon, rectum, plus liver, gallbladder, pancreas.",
            "The processing-line picture: delivery, churning, absorption, water recovery, waste compaction.",
            "Length literacy: centimeters per segment and the summed eight-meter line.",
        ],
        "standards": [
            "Organ names and spellings follow standard clinical usage (esophagus, duodenum, jejunum, ileum, colon).",
            "Lengths stated as adult averages with 'about' qualifiers since they vary by body size.",
            "Disease framing is diagnostic and management-oriented, matching the clinical-specialty scope.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the digestive tract is the body's receiving "
            "dock and refining works - eight meters of conveyor where raw "
            "material becomes signed inventory, and the gastroenterologist is "
            "the works inspector with a camera, a repair crew, and the work "
            "orders to fix the line from the inside."
        ),
    },
    {
        "key": "tract",
        "name": "The Digestive Tract: A Processing Line from Mouth to Anus",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The digestive tract is a single continuous tube, open at both "
            "ends, that runs from the mouth to the anus and processes every "
            "meal in stations. Chewing and saliva start carbohydrate digestion "
            "in the mouth; the esophagus moves the bolus down in seconds; the "
            "stomach holds, churns, and acidifies food for two to four hours; "
            "the duodenum receives bile and pancreatic juice; the jejunum "
            "absorbs most nutrients over three to five hours of small-bowel "
            "transit; the ileum finishes absorption including vitamin B12 and "
            "bile salts; and the colon spends thirty to forty hours reclaiming "
            "water and electrolytes before the rectum stores and expels waste. "
            "Typical whole-gut transit is on the order of forty hours, and the "
            "colon owns more than eighty percent of that time - which is why "
            "constipation is almost always a colon-time problem, not a stomach "
            "one. Each station has its own chemistry, its own microbes, and "
            "its own failure modes, and the gastroenterologist reads symptoms "
            "by station: heartburn points up, cramping midline points to small "
            "bowel, and altered stool points down."
        ),
        "how_it_works": (
            "The tract works as a timed conveyor. A swallow's esophageal wave "
            "clears the 25-cm esophagus in about eight seconds at three "
            "centimeters per second. The stomach meters chyme into the "
            "duodenum in small squirts over two to four hours - about three "
            "hours nominally - so the small intestine is never flooded. "
            "Small-bowel transit of about four hours spreads absorption along "
            "six meters of villus-covered wall. Then the colon takes its slow "
            "thirty-three hours, wringing water from liquid chyme until stool "
            "is formed: 33 of the 40 nominal hours, or 82.5 percent of total "
            "transit, happen in the last 150 centimeters. The demo adds the "
            "station times - three hours stomach, four hours small bowel, "
            "thirty-three hours colon - to the forty-hour whole-gut total and "
            "computes the colon's share, showing why transit-time symptoms "
            "are read from the bottom up."
        ),
        "key_points": [
            "One continuous tube in stations: mouth, esophagus, stomach, duodenum, jejunum, ileum, colon, rectum.",
            "Nominal station times: stomach 3 hours, small bowel 4 hours, colon 33 hours - about 40 hours whole-gut transit.",
            "The colon owns 82.5 percent of transit time, so constipation is read as a colon-time problem first.",
            "Symptoms localize by station: reflux points to the esophagus, midline cramping to small bowel, stool changes to colon.",
            "The stomach meters chyme in squirts so the six meters of small bowel are never flooded.",
        ],
        "requirements": [
            "The station order and each station's nominal transit time.",
            "The water-recovery picture: liquid chyme in, formed stool out.",
            "Transit-time arithmetic: adding station hours to the whole-gut total.",
        ],
        "standards": [
            "Transit times stated as nominal adult averages with stated ranges in the text.",
            "Segment names spelled per clinical convention (duodenum, jejunum, ileum).",
            "Symptom localization described as typical patterns, not absolute rules.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the tract is a timed conveyor with eight "
            "workstations - each with its clock, its crew, and its quota - and "
            "the whole line's throughput is set by the slowest station, which "
            "is the colon; read the bottleneck and you read the symptom."
        ),
    },
    {
        "key": "chemistry",
        "name": "Digestion Chemistry: Enzymes, Acid, Bile, and Absorption",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Digestion is chemistry: the gut breaks the three macronutrients "
            "down with acid, enzymes, and bile, then absorbs the pieces. The "
            "stomach secretes about 1.5 to 2 liters of gastric juice a day at "
            "roughly pH 1.5 to 2 - an acid bath near 31.6 millimolar hydrogen "
            "ion - which unfolds proteins and kills most swallowed microbes. "
            "Pepsin starts protein digestion there; then the pancreas pours "
            "about 1.5 liters of bicarbonate-rich juice into the duodenum, "
            "neutralizing the acid and delivering lipase, amylase, trypsin, "
            "and chymotrypsin to finish the job. The liver contributes 500 to "
            "1000 milliliters of bile a day - about 750 milliliters nominally "
            "- whose bile salts emulsify fat into droplets the lipase can "
            "attack. Carbohydrates finish at the brush border as glucose, "
            "proteins as amino acids and small peptides, fats as fatty acids "
            "and monoglycerides packed into chylomicrons. Daily, the stomach "
            "pours about 200 milliequivalents of acid and the pancreas answers "
            "with about 150 milliequivalents of bicarbonate: the line runs "
            "hot, then gets neutralized, by design."
        ),
        "how_it_works": (
            "The chemistry works in three timed pours. First the stomach's "
            "parietal cells pump hydrogen ions until the lumen sits near pH "
            "1.5, which is 10 to the minus 1.5 molar - about 0.0316 molar, or "
            "31.6 millimolar. Two liters a day at that strength is on the "
            "order of 200 milliequivalents of acid. Second, secretin senses the "
            "acid arriving in the duodenum and orders the pancreas to release "
            "bicarbonate, about 1.5 liters a day near 100 milliequivalents per "
            "liter, for roughly 150 milliequivalents - enough to bring the "
            "chyme back toward neutral where pancreatic enzymes work best. "
            "Third, cholecystokinin contracts the gallbladder and the liver's "
            "bile salts emulsify fat. The demo computes the acid strength "
            "from pH 1.5, the daily acid load, and the neutralizing "
            "bicarbonate answer, showing the hot-then-neutralized budget the "
            "line runs on."
        ),
        "key_points": [
            "Gastric pH 1.5 to 2 unfolds proteins and kills most swallowed microbes; pepsin starts protein digestion.",
            "Pancreatic juice (~1.5 L/day, bicarbonate-rich) neutralizes acid and delivers lipase, amylase, trypsin, chymotrypsin.",
            "Bile (500-1000 mL/day, ~750 mL nominal) emulsifies fat so lipase can digest it.",
            "End products: glucose, amino acids and small peptides, fatty acids and monoglycerides in chylomicrons.",
            "Daily budget: about 200 mEq of gastric acid answered by about 150 mEq of pancreatic bicarbonate.",
        ],
        "requirements": [
            "The pH-to-concentration conversion: pH 1.5 means about 31.6 mM hydrogen ion.",
            "The three-pour sequence: acid, then bicarbonate, then bile.",
            "Milliequivalent arithmetic for the daily acid-bicarbonate budget.",
        ],
        "standards": [
            "pH, volumes, and concentrations stated as adult daily averages with ranges.",
            "Enzyme names per standard clinical usage (pepsin, lipase, amylase, trypsin, chymotrypsin).",
            "Hormone triggers named correctly (secretin, cholecystokinin).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: digestion is a three-pour chemical works - "
            "the acid bath crew, the neutralizer crew, and the solvent crew - "
            "each pouring on a sensor's order, each signed off by the next "
            "station; a failure at any pour reads out downstream as "
            "undigested cargo."
        ),
    },
    {
        "key": "gut_wall",
        "name": "The Gut Wall: Layers, Motility, and Peristalsis",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The gut wall is built in four layers from the inside out: the "
            "mucosa (epithelium, lamina propria, muscularis mucosae) that "
            "absorbs and secretes; the submucosa carrying blood vessels, "
            "nerves, and lymphatics; the muscularis propria with its inner "
            "circular and outer longitudinal muscle that squeezes the tube; "
            "and the serosa or adventitia wrapping the outside. Between the "
            "muscle coats sits the myenteric plexus - the enteric nervous "
            "system, a second brain of about 100 million neurons - that runs "
            "motility locally. Peristalsis is the coordinated wave: circular "
            "muscle contracts behind the bolus while longitudinal muscle "
            "shortens ahead, pushing contents forward. An esophageal wave "
            "travels about 2 to 4 centimeters per second, so a 25-centimeter "
            "esophagus clears a swallow in roughly eight seconds at 3 cm/s. "
            "The stomach grinds with three contractions per minute; the small "
            "bowel mixes with segmental contractions and sweeps with the "
            "migrating motor complex between meals; the colon moves in slow "
            "mass movements a few times a day. Every motility disorder is a "
            "wall-layer or wave-pattern failure."
        ),
        "how_it_works": (
            "The wall works as a four-layer pressure machine. The mucosa "
            "handles chemistry, the submucosa carries supply lines, and the "
            "two muscle coats do the work: the inner circular coat narrows "
            "the tube and the outer longitudinal coat shortens it. The "
            "myenteric plexus fires them in sequence - contract behind, relax "
            "ahead - and the wave advances. At 3 centimeters per second, the "
            "wave crosses the 25-centimeter esophagus in 25 divided by 3, "
            "about 8.33 seconds: one clean peristaltic sweep per swallow. "
            "Between meals the migrating motor complex runs a housekeeping "
            "sweep every 90 to 120 minutes, clearing debris and bacteria "
            "downstream. The demo computes the esophageal wave transit time "
            "and counts the four wall layers, showing how wave speed times "
            "length sets every station's clearing time."
        ),
        "key_points": [
            "Four wall layers: mucosa, submucosa, muscularis propria (circular + longitudinal), serosa/adventitia.",
            "The enteric nervous system (~100 million neurons) runs motility locally between the muscle coats.",
            "Peristalsis = contract behind, relax ahead; esophageal waves run 2-4 cm/s.",
            "A 25-cm esophagus clears a swallow in about 8.33 seconds at 3 cm/s.",
            "The migrating motor complex sweeps debris and bacteria downstream every 90-120 minutes between meals.",
        ],
        "requirements": [
            "The four layers in inside-out order and what each contributes.",
            "The peristaltic wave rule: circular contracts behind, longitudinal shortens ahead.",
            "Wave arithmetic: transit time equals length divided by wave speed.",
        ],
        "standards": [
            "Layer names per standard histologic terminology.",
            "Wave speeds and sweep intervals stated as adult typical ranges.",
            "Neuron count stated as the standard estimate (~100 million).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the wall is a four-ply pressure vessel "
            "with its own local control room - a hundred million neurons "
            "running the pumps without asking the head office - and peristalsis "
            "is the signed handoff protocol, station to station, never backward."
        ),
    },
    {
        "key": "liver",
        "name": "The Liver and Biliary System: Detoxification, Bile, and Metabolism",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The liver is the body's largest internal organ - about 1.5 "
            "kilograms in the adult - and its chemical refinery. It receives "
            "about 1.5 liters of blood per minute, roughly 30 percent of the "
            "resting cardiac output of 5 liters per minute: about 75 percent "
            "(1.125 L/min) through the portal vein straight from the gut, and "
            "about 25 percent (0.375 L/min) through the hepatic artery. That "
            "portal stream is the point - everything absorbed from the "
            "intestine passes the liver first for inspection, the first-pass "
            "effect. Hepatocytes make bile (500 to 1000 mL a day), synthesize "
            "albumin and clotting factors, store glycogen and vitamins, "
            "convert ammonia to urea, and detoxify drugs and alcohol. Bile "
            "flows through canaliculi into ducts, concentrates in the "
            "gallbladder between meals, and squirts into the duodenum when fat "
            "arrives. When the refinery fails, the signs are unmistakable: "
            "jaundice, coagulopathy, low albumin, ascites, and encephalopathy "
            "- each a named refinery output gone missing."
        ),
        "how_it_works": (
            "The liver works as a two-feed refinery. The portal vein delivers "
            "nutrient-rich, toxin-carrying blood from the gut at about 1.125 "
            "liters per minute; the hepatic artery delivers oxygen at about "
            "0.375 liters per minute; together 1.5 liters per minute, which "
            "is 30 percent of a 5-liter-per-minute cardiac output - nearly a "
            "third of the body's blood visits the refinery every minute. "
            "Hepatocytes arranged around the sinusoids extract, transform, "
            "and repackage: glucose to glycogen, ammonia to urea, cholesterol "
            "to bile salts, drugs to excretable metabolites. Bile salts are "
            "recycled through the enterohepatic circulation about 6 to 10 "
            "times a day - roughly 8 nominally - so a small bile-salt pool "
            "does a large day's emulsifying work. The demo computes the "
            "portal-arterial split, the liver's share of cardiac output, and "
            "the daily recycling turns of the bile-salt pool."
        ),
        "key_points": [
            "Liver ~1.5 kg; blood flow ~1.5 L/min, about 30% of resting cardiac output.",
            "Dual supply: portal vein ~1.125 L/min (75%) from the gut, hepatic artery ~0.375 L/min (25%).",
            "First-pass effect: everything absorbed intestinally is inspected by the liver before reaching the body.",
            "Core outputs: bile, albumin, clotting factors, glycogen storage, urea from ammonia, drug detoxification.",
            "Bile salts recycle through the enterohepatic circulation ~8 times daily.",
        ],
        "requirements": [
            "The portal-vs-arterial split and why the portal stream defines liver function.",
            "The first-pass picture: gut to portal vein to liver to systemic blood.",
            "Flow-share arithmetic: hepatic flow divided by cardiac output.",
        ],
        "standards": [
            "Masses, flows, and volumes stated as adult typical values with ranges.",
            "Anatomical terms per standard usage (portal vein, hepatic artery, sinusoids, canaliculi).",
            "Failure signs listed as the classic clinical set (jaundice, coagulopathy, ascites, encephalopathy).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the liver is the refinery at the end of "
            "the receiving dock - every crate from the gut passes its "
            "inspectors before it ships to the body, and its outputs (bile, "
            "albumin, clotting factors, clean blood) are the signed manifests "
            "of a refinery doing its job."
        ),
    },
    {
        "key": "pancreas",
        "name": "The Pancreas: Digestive Enzymes and the Insulin Balance",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The pancreas is two organs in one: an exocrine chemical plant "
            "and an endocrine control room. The exocrine pancreas pours about "
            "1.5 liters of juice a day into the duodenum - bicarbonate to "
            "neutralize stomach acid plus the full enzyme set (lipase, "
            "amylase, trypsin, chymotrypsin, elastase) that finishes "
            "digestion. The endocrine pancreas is the islets of Langerhans, "
            "scattered clusters where beta cells make insulin and alpha cells "
            "make glucagon. Insulin lowers blood glucose by driving it into "
            "muscle and fat and shutting off liver glucose output; glucagon "
            "raises it by ordering the liver to release stored glucose. The "
            "ratio is the instruction: fed state means high insulin and low "
            "glucagon (store), fasted state means low insulin and high "
            "glucagon (mobilize). A typical adult with type 1 diabetes needs "
            "on the order of 0.6 units of insulin per kilogram per day - 42 "
            "units for a 70-kilogram adult, split roughly half basal (about "
            "21 units a day, near 0.875 units an hour) and half mealtime "
            "boluses. Pancreatic failure reads two ways: undigested fat in "
            "the stool (exocrine) and rising glucose (endocrine)."
        ),
        "how_it_works": (
            "The pancreas works as a dual-output plant on hormonal orders. "
            "Secretin and cholecystokinin arrive from the duodenum when acid "
            "and fat show up; the acinar cells answer with enzymes and the "
            "duct cells with bicarbonate - about 1.5 liters a day of "
            "finished juice. Meanwhile the islets sample blood glucose "
            "continuously: above target, beta cells release insulin; below "
            "target, alpha cells release glucagon. Dosing follows body mass: "
            "at 0.6 units per kilogram per day, a 70-kilogram adult needs 42 "
            "units total, about 21 units as round-the-clock basal - 21 "
            "divided by 24 is 0.875 units per hour - and about 21 units as "
            "mealtime boluses. The demo computes the total daily dose, the "
            "basal-bolus split, and the hourly basal rate, showing how the "
            "control room's output scales with the body's mass."
        ),
        "key_points": [
            "Exocrine pancreas: ~1.5 L/day of bicarbonate plus enzymes (lipase, amylase, trypsin, chymotrypsin).",
            "Endocrine islets: beta cells make insulin (lowers glucose), alpha cells make glucagon (raises glucose).",
            "The insulin:glucagon ratio is the instruction - store when fed, mobilize when fasted.",
            "Typical type 1 total daily insulin ~0.6 U/kg/day: 42 units for 70 kg, half basal, half bolus.",
            "Basal rate near 0.875 units/hour for that 70-kg adult; failure reads as fatty stool, rising glucose, or both.",
        ],
        "requirements": [
            "The exocrine/endocrine split and which failure produces which symptom.",
            "The insulin-glucagon seesaw and the fed-vs-fasted instruction.",
            "Weight-based dosing arithmetic: units per kilogram per day, basal-bolus split, hourly basal rate.",
        ],
        "standards": [
            "Volumes and doses stated as typical adult values with the weight-based rule explicit.",
            "Enzyme and hormone names per standard clinical usage.",
            "Insulin arithmetic labeled as the standard type 1 dosing estimate, not a prescription.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the pancreas is the dual plant - the "
            "chemical works pouring enzymes on the line, and the control "
            "room across the hall balancing the fuel gauge - two crews, one "
            "roof, and the whole body's energy ledger kept in their logbook."
        ),
    },
    {
        "key": "microbiome",
        "name": "The Gut Microbiome: Clinical Aspects of the Resident Ecosystem",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The gut microbiome is the trillions-strong community of bacteria, "
            "archaea, fungi, and viruses living in the intestines - a resident "
            "workforce the body did not build but cannot run without. The "
            "modern estimate (Sender, Fuchs, and Milo, Cell 2016) puts the "
            "bacterial count near 38 trillion against about 30 trillion human "
            "cells: a ratio of about 1.27 to 1, roughly one-to-one, retiring "
            "the old ten-to-one myth. The collective microbial gene catalog "
            "runs near 3 million non-redundant genes against the human "
            "genome's 20,000 - about 150 times the human gene count - which "
            "is why the microbiome functions as a second metabolic organ: "
            "fermenting fiber into short-chain fatty acids, synthesizing "
            "vitamin K and B vitamins, training the immune system, and "
            "holding colonization resistance against pathogens. Clinically it "
            "matters in Clostridioides difficile infection (fecal microbiota "
            "transplant cures about 90 percent of recurrent cases), in "
            "inflammatory bowel disease, in irritable bowel syndrome, and in "
            "antibiotic-associated diarrhea. Manipulating it is now therapy: "
            "probiotics with modest evidence, prebiotics as fiber fuel, and "
            "transplant as the heavy tool."
        ),
        "how_it_works": (
            "The microbiome works as a fermentation and defense workforce. "
            "Undigested fiber reaches the colon, where bacteria ferment it "
            "into short-chain fatty acids - butyrate, propionate, acetate - "
            "that feed colonocytes and signal systemically. The arithmetic of "
            "the workforce: 38 trillion bacteria divided by 30 trillion human "
            "cells gives 1.27, the famous near-parity ratio; 3 million "
            "microbial genes divided by 20,000 human genes gives 150, the "
            "metabolic leverage ratio. Colonization resistance is competitive "
            "exclusion at scale: a full workforce leaves no niche for "
            "Clostridioides difficile, and antibiotics that clear the "
            "workforce open the niche - which is why transplanting a healthy "
            "workforce cures about 90 of 100 recurrent C. difficile cases. "
            "The demo computes the cell ratio, the gene-leverage ratio, and "
            "the expected cures in 100 transplant-treated patients."
        ),
        "key_points": [
            "About 38 trillion gut bacteria vs about 30 trillion human cells: ratio ~1.27 to 1 (near parity, not 10:1).",
            "Microbial genes (~3 million) outnumber human genes (~20,000) about 150 to 1.",
            "Core jobs: fiber fermentation to short-chain fatty acids, vitamin K and B synthesis, immune training, colonization resistance.",
            "Fecal microbiota transplant cures about 90% of recurrent C. difficile infections.",
            "Antibiotics clear the workforce and open the niche - dysbiosis is an occupational hazard of the drugs.",
        ],
        "requirements": [
            "The cell-count ratio and why the 10:1 myth was retired.",
            "The fermentation picture: fiber in, short-chain fatty acids out.",
            "Colonization resistance as competitive exclusion at workforce scale.",
        ],
        "standards": [
            "Counts cited to the Sender/Fuchs/Milo 2016 revised estimates with 'about' qualifiers.",
            "C. difficile named per current taxonomy (Clostridioides difficile).",
            "Transplant cure rate stated as the recurrent-disease figure (~90%), not first-episode.",
        ],
        "citations": [
            "Sender R, Fuchs S, Milo R. Revised Estimates for the Number of Human and Bacteria Cells in the Body. Cell. 2016;164(3):337-340.",
            CIT_SLEIS,
            CIT_YAMADA,
        ],
        "sig_lens": (
            "His Signature reading: the microbiome is the resident workforce - "
            "thirty-eight trillion strong, never on the payroll, doing the "
            "fermentation shifts the body cannot staff itself - and every "
            "antibiotic course is a layoff the works must survive."
        ),
    },
    {
        "key": "encounter",
        "name": "The GI Clinical Encounter: History, Exam, and Basic Tests",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The GI clinical encounter is the diagnostic interview and "
            "examination that turns symptoms into a differential. The history "
            "runs the gut top to bottom: appetite and weight change, "
            "swallowing trouble, heartburn, nausea, vomiting (and whether "
            "blood or bile appears), abdominal pain (onset, location, "
            "radiation, relation to meals and stool), bowel habits (frequency, "
            "consistency on the Bristol scale, blood, mucus), jaundice, "
            "fevers, travel, medicines (especially NSAIDs, which ulcerate), "
            "alcohol, and family history of bowel cancer or inflammatory bowel "
            "disease. The exam checks for jaundice, wasting, and anemia, "
            "palpates for tenderness, masses, liver and spleen size, and "
            "almost always includes the rectal exam and a stool blood check. "
            "Basic tests follow the story: complete blood count for anemia, "
            "liver panel (bilirubin, ALT, AST, alkaline phosphatase, albumin), "
            "lipase for pancreatic pain, stool studies for infection and "
            "inflammation (fecal calprotectin), and celiac serology where "
            "malabsorption is suspected. Every test is read against pretest "
            "probability: a 90-percent-sensitive, 85-percent-specific test in "
            "a patient with 10 percent pretest probability yields a positive "
            "predictive value of only 40 percent - the number teaches "
            "restraint."
        ),
        "how_it_works": (
            "The encounter works as a Bayesian funnel. The history sets the "
            "pretest probability; the exam adjusts it; the test result "
            "updates it. Take a test with 90 percent sensitivity and 85 "
            "percent specificity applied where the pretest probability is 10 "
            "percent: true positives are 0.9 times 0.1 = 0.09, false "
            "positives are 0.15 times 0.9 = 0.135, and the positive "
            "predictive value is 0.09 divided by (0.09 + 0.135) = 0.40 - 40 "
            "percent. Six of ten positives are false alarms at low "
            "prevalence, which is why the gastroenterologist tests the story, "
            "not the symptom alone, and why alarm features (bleeding, weight "
            "loss, obstruction, jaundice, anemia) jump the queue to "
            "endoscopy. The demo runs the predictive-value arithmetic, "
            "showing how prevalence - not the test's quality alone - decides "
            "what a positive means."
        ),
        "key_points": [
            "History runs the gut top to bottom: swallowing, reflux, pain, vomiting, bowel habits, bleeding, jaundice, weight.",
            "Alarm features - bleeding, weight loss, obstruction, jaundice, anemia - jump the queue to endoscopy.",
            "Core basic tests: CBC, liver panel, lipase, stool studies, fecal calprotectin, celiac serology.",
            "A 90%-sensitive, 85%-specific test at 10% pretest probability has only 40% positive predictive value.",
            "Prevalence decides what a positive means; the gastroenterologist tests the story, not the symptom.",
        ],
        "requirements": [
            "The top-to-bottom history sequence and the alarm-feature list.",
            "The basic test panel and what each test answers.",
            "Bayes arithmetic: sensitivity, specificity, prevalence, predictive value.",
        ],
        "standards": [
            "Test names per standard clinical usage (fecal calprotectin, tTG-IgA, liver panel components).",
            "NSAIDs named as the classic medication cause of ulceration.",
            "Predictive-value example labeled as illustrative arithmetic with stated inputs.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the encounter is the intake interview at "
            "the works gate - the foreman's questions, the walk-around "
            "inspection, the first lab samples - and every number after that "
            "is read against what the interview already said the odds were."
        ),
    },
    {
        "key": "gerd",
        "name": "GERD: Gastroesophageal Reflux Disease",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Gastroesophageal reflux disease is the failure of the "
            "anti-reflux barrier: stomach contents wash back into the "
            "esophagus often enough to cause troublesome symptoms or injury. "
            "The barrier is the lower esophageal sphincter plus the "
            "diaphragm's crural pinch; transient sphincter relaxations - "
            "brief openings unrelated to swallowing - cause most reflux "
            "episodes, and a hiatal hernia weakens the pinch. Typical "
            "symptoms are heartburn and regurgitation, worse after meals, "
            "when bending, and at night; alarm features (dysphagia, bleeding, "
            "anemia, weight loss, persistent vomiting) demand endoscopy. "
            "Untreated chronic reflux can inflame the esophagus (erosive "
            "esophagitis), narrow it (stricture), or replace its lining with "
            "intestinal-type cells - Barrett's esophagus - the precursor of "
            "esophageal adenocarcinoma. Diagnosis is clinical when classic "
            "symptoms respond to acid suppression; 24-hour pH monitoring "
            "calls reflux abnormal when acid exposure time exceeds 6 percent "
            "of the day - for example 90 minutes of the 1440-minute day is "
            "6.25 percent, over the line. Treatment climbs a ladder: "
            "weight loss, head-of-bed elevation, and trigger avoidance; then "
            "daily proton pump inhibitors, which heal esophagitis in the "
            "great majority; then endoscopic or surgical fundoplication for "
            "the refractory few."
        ),
        "how_it_works": (
            "GERD works as a pressure-and-timing failure. The stomach "
            "sits at positive pressure and the esophagus near atmospheric; "
            "the sphincter holds a 10 to 30 mmHg pressure zone against that "
            "gradient. When it relaxes out of turn, the gradient drives acid "
            "upward, and clearance depends on peristalsis plus swallowed "
            "saliva's bicarbonate. The diagnostic number is acid exposure "
            "time: minutes with esophageal pH below 4 divided by 1440 "
            "minutes, times 100. Ninety minutes gives 90/1440 = 6.25 "
            "percent - above the 6 percent abnormal threshold of the Lyon "
            "consensus (under 4 percent normal, 4 to 6 inconclusive). "
            "Proton pump inhibitors work upstream of the symptom: they "
            "irreversibly block the parietal cell's H+/K+ ATPase, cutting "
            "acid output by about 90 percent once steady state is reached. "
            "The demo computes acid exposure time from monitored minutes and "
            "tests it against the 6 percent line."
        ),
        "key_points": [
            "GERD = anti-reflux barrier failure: transient lower esophageal sphincter relaxations cause most episodes; hiatal hernia weakens the barrier.",
            "Classic symptoms: heartburn and regurgitation; alarm features (dysphagia, bleeding, weight loss) demand endoscopy.",
            "Complications of chronic reflux: erosive esophagitis, stricture, Barrett's esophagus (adenocarcinoma precursor).",
            "Acid exposure time >6% of the day is abnormal (90 min of 1440 = 6.25%); <4% normal, 4-6% inconclusive.",
            "Treatment ladder: lifestyle, daily proton pump inhibitors, then endoscopic or surgical fundoplication.",
        ],
        "requirements": [
            "The barrier anatomy: lower esophageal sphincter plus diaphragmatic crural pinch.",
            "The acid-exposure-time definition and the 4/6 percent thresholds.",
            "The PPI mechanism: irreversible H+/K+ ATPase blockade.",
        ],
        "standards": [
            "Thresholds per the Lyon consensus on pH monitoring (4% and 6% lines).",
            "Barrett's esophagus described as intestinal metaplasia and adenocarcinoma precursor.",
            "Alarm features listed as the standard endoscopy triggers.",
        ],
        "citations": [CIT_GERD, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: GERD is a check-valve failure on the "
            "works' intake line - the gate opens out of turn, the upstream "
            "station floods, and the fix runs from adjusting the line's "
            "pressure (lifestyle) to rebuilding the valve (fundoplication)."
        ),
    },
    {
        "key": "dyspepsia",
        "name": "Functional Dyspepsia and Disorders of Gut-Brain Interaction",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Functional dyspepsia is chronic upper-abdominal discomfort - "
            "fullness, early satiety, epigastric pain or burning - with no "
            "structural disease to explain it after workup: a disorder of "
            "gut-brain interaction, not of damaged tissue. Rome IV divides it "
            "into two syndromes: postprandial distress syndrome (bothersome "
            "fullness after normal-size meals, early satiety) and epigastric "
            "pain syndrome (bothersome epigastric pain or burning not relieved "
            "by stool or gas). The mechanisms are real physiology gone "
            "awry: impaired gastric accommodation (the upper stomach fails to "
            "relax for the meal), visceral hypersensitivity (normal stretch "
            "read as pain), delayed emptying in a minority, and amplified "
            "gut-brain signaling under stress and anxiety. The four cardinal "
            "symptoms pair into six possible two-symptom patterns, which is "
            "why presentations vary so widely. Management starts by ruling "
            "out alarm features and testing for H. pylori (treat if "
            "positive), then acid suppression, prokinetics where emptying is "
            "slow, and neuromodulators - low-dose tricyclics - plus "
            "gut-directed behavioral therapy for the brain side of the loop."
        ),
        "how_it_works": (
            "Functional dyspepsia works as a sensor-and-software fault. The "
            "hardware - mucosa, muscle - is intact on endoscopy, but the "
            "sensors misreport: impaired fundic accommodation means the "
            "proximal stomach does not relax to receive the meal, so normal "
            "volumes generate abnormal wall tension; visceral "
            "hypersensitivity means the brain's gain is turned up and normal "
            "tension reads as pain. The combinatorics explain the clinical "
            "variety: with four cardinal symptoms (fullness, early satiety, "
            "pain, burning), the number of distinct two-symptom patterns is "
            "4 choose 2 = 6, and patients distribute across all six plus the "
            "full four-symptom picture. Treatment addresses both ends of the "
            "wire: acid suppression and prokinetics for the gut end, "
            "neuromodulators and behavioral therapy for the brain end. The "
            "demo computes the six two-symptom patterns from the four "
            "cardinal symptoms, showing why 'dyspepsia' is six presentations "
            "wearing one name."
        ),
        "key_points": [
            "Functional dyspepsia = chronic upper-abdominal symptoms with no structural disease: a gut-brain interaction disorder.",
            "Rome IV subtypes: postprandial distress syndrome (fullness, early satiety) and epigastric pain syndrome (pain, burning).",
            "Mechanisms: impaired gastric accommodation, visceral hypersensitivity, delayed emptying (minority), amplified gut-brain signaling.",
            "Four cardinal symptoms yield 6 distinct two-symptom patterns - presentations vary widely.",
            "Management: exclude alarms, test/treat H. pylori, acid suppression, prokinetics, neuromodulators, gut-directed behavioral therapy.",
        ],
        "requirements": [
            "The Rome IV two-syndrome split and which symptoms belong to each.",
            "The accommodation-vs-hypersensitivity mechanism distinction.",
            "The H. pylori test-and-treat step before labeling symptoms functional.",
        ],
        "standards": [
            "Criteria cited to Rome IV (Mearin et al., Gastroenterology 2016).",
            "Alarm features required to be excluded before the functional label.",
            "Neuromodulator use described as low-dose, gut-brain-directed therapy.",
        ],
        "citations": [CIT_ROME, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: functional dyspepsia is a sensor "
            "calibration fault - the tanks and pipes test fine, but the "
            "gauges over-read and the control room overreacts - so the repair "
            "is recalibration at both ends of the wire, not new plumbing."
        ),
    },
    {
        "key": "ulcer",
        "name": "Peptic Ulcer Disease and Helicobacter pylori",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Peptic ulcer disease is a break in the stomach or duodenal lining "
            "deeper than the mucosa - an acid burn that outran the defenses. "
            "Two causes own the great majority: Helicobacter pylori "
            "infection and nonsteroidal anti-inflammatory drugs. H. pylori, a "
            "spiral bacterium colonizing the stomach of about 44 percent of "
            "the world's people, burrows under the mucus and injects toxins "
            "(CagA, VacA) that inflame and weaken the lining; NSAIDs block "
            "prostaglandins and strip the mucus-bicarbonate barrier the same "
            "way. Classic ulcer pain is epigastric, gnawing, eased by food or "
            "antacids in duodenal ulcer and sometimes worsened by food in "
            "gastric ulcer - though many ulcers are silent until they bleed "
            "or perforate. Diagnosis is endoscopy with biopsy, or H. pylori "
            "stool antigen or urea breath testing. Eradication therapy - "
            "typically 14 days of acid suppression plus two or three "
            "antibiotics - cures about 85 percent: in 1000 infected patients "
            "at 44 percent prevalence (440 infected), about 374 are cured and "
            "66 need salvage regimens. Every gastric ulcer is biopsied "
            "because cancer can mimic it; duodenal ulcers are essentially "
            "never malignant."
        ),
        "how_it_works": (
            "The ulcer works as a breached defense line. The mucosa defends "
            "itself with mucus, bicarbonate, rapid cell turnover, and "
            "prostaglandin-driven blood flow; acid and pepsin attack "
            "continuously. H. pylori tilts the balance by living inside the "
            "mucus layer - safe from acid - and inflaming the wall beneath "
            "it; NSAIDs tilt it by removing prostaglandin protection "
            "systemically. Population arithmetic sets the scale: at 44 "
            "percent global prevalence, 1000 people hold 440 infections; at "
            "85 percent eradication, 440 times 0.85 = 374 cures, leaving 66 "
            "for second-line therapy. Acid suppression buys the healing "
            "time: PPIs hold intragastric pH above 4 for most of the day, "
            "under which pepsin is inactive and clot is stable. The demo "
            "computes the infected pool, the cured pool, and the salvage "
            "pool from prevalence and eradication rate."
        ),
        "key_points": [
            "Peptic ulcer = mucosal break deeper than the mucosa; H. pylori and NSAIDs cause the great majority.",
            "H. pylori infects ~44% of the world's people via CagA/VacA toxin-driven mucosal injury.",
            "Duodenal ulcer pain typically eases with food; many ulcers are silent until bleed or perforation.",
            "Eradication (~85%): of 440 infected per 1000 people, ~374 cured, ~66 need salvage therapy.",
            "Every gastric ulcer is biopsied - cancer can mimic it; duodenal ulcers are essentially never malignant.",
        ],
        "requirements": [
            "The defense-vs-attack balance picture (mucus/bicarbonate/prostaglandins vs acid/pepsin).",
            "The two dominant causes and how each breaches the defense.",
            "Prevalence-times-eradication arithmetic for the cure/salvage split.",
        ],
        "standards": [
            "Prevalence and eradication figures stated as global/typical values with 'about' qualifiers.",
            "Gastric-ulcer biopsy rule stated as the standard malignancy precaution.",
            "NSAIDs named as the medication cause; H. pylori toxins named (CagA, VacA).",
        ],
        "citations": [CIT_HPYLORI, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: the ulcer is a breached containment wall - "
            "either saboteurs living inside the insulation (H. pylori) or the "
            "protective coating stripped plant-wide (NSAIDs) - and the repair "
            "order is always the same: evict the saboteurs, recoat the wall, "
            "hold the acid back while it cures."
        ),
    },
    {
        "key": "ugib",
        "name": "Upper GI Bleeding",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Upper gastrointestinal bleeding is blood loss from the esophagus, "
            "stomach, or duodenum - above the ligament of Treitz. It "
            "announces itself as hematemesis (vomited blood, bright red or "
            "coffee-ground), melena (black tarry stool from digested blood), "
            "or unexplained anemia and faintness. The usual culprits are "
            "peptic ulcers, erosive gastritis, esophageal varices in liver "
            "disease, and Mallory-Weiss tears from forceful vomiting. "
            "Management is a timed runbook: resuscitate first (large-bore "
            "IVs, type and crossmatch), give high-dose IV proton pump "
            "inhibitor, transfuse restrictively at hemoglobin below 7 g/dL "
            "(below 8 with heart disease), and scope urgently - within 24 "
            "hours - to find and treat the lesion with clips, bands, or "
            "thermal therapy. The transfusion arithmetic is bedside-simple: "
            "one unit of packed red cells raises hemoglobin about 1 g/dL, so "
            "a patient at 6 g/dL needing 9 needs about 3 units. Variceal "
            "bleeding gets vasoactive drugs (octreotide) and band ligation. "
            "Mortality tracks the cause and the comorbidity, not the "
            "milliliters: resuscitation and early endoscopy are what move the "
            "number."
        ),
        "how_it_works": (
            "Upper GI bleeding works as a leak-above-the-valve emergency. "
            "Blood entering the stomach is partly digested by acid - "
            "hemoglobin's iron oxidizes - which is why upper bleeding makes "
            "melena, black and tarry, while brisk bleeding overwhelms "
            "digestion and appears as red hematemesis. The runbook is "
            "ordered by physics: restore circulating volume first, because a "
            "pressureless patient cannot be scoped safely; suppress acid "
            "because clot is stable above pH 6 and pepsin dissolves it "
            "below pH 4; then look and fix. The bedside arithmetic: each "
            "unit of packed red cells lifts hemoglobin roughly 1 g/dL, so "
            "from 6 to the 9 g/dL target is 3 units. The restrictive "
            "threshold - transfuse below 7 g/dL - comes from trials showing "
            "less is safer than liberal transfusion. The demo computes the "
            "units needed from the hemoglobin gap and states the threshold "
            "rule."
        ),
        "key_points": [
            "Upper GI bleed = above the ligament of Treitz: hematemesis, melena, or unexplained anemia/faintness.",
            "Top causes: peptic ulcers, erosive gastritis, esophageal varices, Mallory-Weiss tears.",
            "Runbook order: resuscitate, high-dose IV PPI, restrictive transfusion (Hb <7 g/dL), endoscopy within 24 hours.",
            "One unit of packed red cells raises hemoglobin ~1 g/dL: 6 to 9 g/dL needs ~3 units.",
            "Variceal bleeding adds vasoactive drugs (octreotide) and band ligation.",
        ],
        "requirements": [
            "The above-vs-below Treitz landmark and why melena points upward.",
            "The resuscitation-first ordering and the acid-suppression rationale (clot stability vs pH).",
            "Unit-to-hemoglobin arithmetic for bedside transfusion planning.",
        ],
        "standards": [
            "Transfusion thresholds per the restrictive strategy (7 g/dL; 8 with cardiovascular disease).",
            "Endoscopy timing stated as within 24 hours per consensus guidance.",
            "Cause list ordered by typical frequency (ulcer first).",
        ],
        "citations": [CIT_UGIB, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: an upper GI bleed is a burst pipe above "
            "the main valve - first restore line pressure, then seal the "
            "chemistry so the patch holds, then send the camera crew in to "
            "clamp the exact leak; order is the therapy."
        ),
    },
    {
        "key": "celiac",
        "name": "Celiac Disease and the Malabsorption Workup",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Celiac disease is an autoimmune attack on the small intestine "
            "triggered by gluten - the wheat, barley, and rye protein - in "
            "genetically susceptible people (HLA-DQ2 or DQ8). Gluten's "
            "gliadin fragments cross the epithelium, tissue transglutaminase "
            "modifies them, and the immune system answers by flattening the "
            "villi: villous atrophy with crypt hyperplasia and intraepithelial "
            "lymphocytosis. Flat villi cannot absorb, so the disease reads "
            "as malabsorption - diarrhea, bloating, weight loss, iron "
            "deficiency, low B12, low vitamin D, osteoporosis - though many "
            "adults present with anemia or fatigue alone. About 1 percent of "
            "most populations carries it. Diagnosis is serology first: "
            "tissue transglutaminase IgA (about 95 percent sensitive and "
            "specific) with total IgA to catch IgA deficiency, confirmed by "
            "duodenal biopsy showing the atrophy. The numbers teach the test: "
            "screening 10,000 people at 1 percent prevalence finds 100 true "
            "cases, catches about 95, and generates about 495 false positives "
            "(5 percent of 9,900) - a positive predictive value of 95 of 590, "
            "about 16.1 percent - which is why biopsy confirms. Treatment is "
            "the strict gluten-free diet, for life; the mucosa heals, the "
            "antibodies fall, and the cancers-in-waiting (enteropathy-type "
            "lymphoma) recede."
        ),
        "how_it_works": (
            "Celiac works as a mistaken-identity demolition. Tissue "
            "transglutaminase deamidates gliadin; HLA-DQ2/DQ8 presents it; "
            "T cells authorize the demolition of the villi they mistake for "
            "the threat. Surface area collapses, and with it absorption of "
            "iron, folate, B12, vitamin D, and calories. The screening "
            "arithmetic: 10,000 people at 1 percent prevalence = 100 true "
            "cases; 95 percent sensitivity catches 95; 95 percent "
            "specificity on 9,900 healthy people yields 0.05 x 9900 = 495 "
            "false positives; positive predictive value = 95/(95+495) = "
            "95/590 = 16.1 percent. Most positives in a screening population "
            "are false - hence biopsy confirmation and hence testing the "
            "symptomatic, not the curious. Remove gluten and the immune "
            "system stands down: antibodies normalize in months, villi "
            "regrow over one to two years. The demo computes the screening "
            "table and the 16.1 percent predictive value."
        ),
        "key_points": [
            "Celiac = autoimmune villous atrophy triggered by gluten in HLA-DQ2/DQ8 carriers; ~1% of populations.",
            "Flattened villi cause malabsorption: diarrhea, bloating, weight loss, iron/B12/D deficiency; many present with anemia alone.",
            "Diagnosis: tTG-IgA (~95% sensitive/specific) plus total IgA, confirmed by duodenal biopsy.",
            "Screening 10,000 at 1% prevalence: ~95 true positives vs ~495 false positives - PPV only ~16.1%, so biopsy confirms.",
            "Treatment: strict lifelong gluten-free diet; mucosa heals, antibodies fall, lymphoma risk recedes.",
        ],
        "requirements": [
            "The gliadin-transglutaminase-HLA-DQ2/DQ8 immune sequence.",
            "The villous-atrophy-to-malabsorption consequence chain.",
            "Screening-table arithmetic: sensitivity, specificity, prevalence, predictive value.",
        ],
        "standards": [
            "Serology named per standard usage (tTG-IgA with total IgA).",
            "Histology described by the classic triad (villous atrophy, crypt hyperplasia, intraepithelial lymphocytosis).",
            "Prevalence and test performance stated as typical values with 'about' qualifiers.",
        ],
        "citations": [CIT_CELIAC, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: celiac is a friendly-fire demolition - "
            "the security system mistakes a food protein for an intruder and "
            "tears down the warehouse shelving - and the only work order that "
            "holds is removing the mistaken trigger, permanently, from the "
            "loading dock."
        ),
    },
    {
        "key": "ibs",
        "name": "Irritable Bowel Syndrome",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Irritable bowel syndrome is the commonest disorder of gut-brain "
            "interaction: recurrent abdominal pain tied to defecation, with "
            "altered stool form or frequency, and no structural disease. Rome "
            "IV defines it as pain at least one day a week in the last three "
            "months - at least 12 pain days in 12 weeks - plus two or more "
            "of: pain related to defecation, change in stool frequency, "
            "change in stool form. Subtypes follow the stool: IBS with "
            "diarrhea (IBS-D), with constipation (IBS-C), mixed (IBS-M), and "
            "unclassified (IBS-U) - four patterns from the Bristol stool "
            "scale's seven types. The machinery is dysregulated, not "
            "damaged: visceral hypersensitivity, altered motility, low-grade "
            "mucosal immune activation, microbiome shifts, and amplified "
            "gut-brain signaling, often after gastroenteritis "
            "(post-infectious IBS). Management is subtype-directed: fiber and "
            "osmotic laxatives for IBS-C, antidiarrheals and bile-acid "
            "binders for IBS-D, antispasmodics for pain, low-FODMAP diet "
            "trials, gut-directed hypnotherapy or cognitive behavioral "
            "therapy, and neuromodulators for the refractory. Alarm features "
            "are excluded first; then the diagnosis is clinical and the "
            "therapy is functional."
        ),
        "how_it_works": (
            "IBS works as a miscalibrated control loop. The gut's sensors "
            "(visceral afferents) report distension, the brain amplifies the "
            "report under stress, and the motor response overshoots - too "
            "fast (diarrhea) or too slow (constipation). The diagnostic "
            "threshold is frequency arithmetic: pain at least one day per "
            "week over three months means 12 weeks x 1 = 12 pain days "
            "minimum. Subtyping is stool-form arithmetic on the Bristol "
            "scale: more than a quarter of stools hard (types 1-2) with less "
            "than a quarter loose (types 6-7) is IBS-C; the reverse is "
            "IBS-D; both over a quarter is IBS-M; neither is IBS-U - four "
            "subtypes covering the seven stool types. Therapy tunes the "
            "loop at both ends: motility agents and diet for the gut, "
            "brain-directed therapies for the amplifier. The demo verifies "
            "the 12-day pain threshold and enumerates the four subtypes."
        ),
        "key_points": [
            "IBS = recurrent abdominal pain linked to defecation with altered stool form/frequency; no structural disease.",
            "Rome IV: pain >=1 day/week for 3 months (>=12 pain days) plus >=2 of: related to defecation, frequency change, form change.",
            "Four subtypes: IBS-D, IBS-C, IBS-M, IBS-U - mapped from the Bristol scale's 7 stool types.",
            "Mechanisms: visceral hypersensitivity, dysmotility, immune activation, microbiome shifts, gut-brain amplification.",
            "Management is subtype-directed: fiber/laxatives, antidiarrheals, antispasmodics, low-FODMAP, brain-gut therapies, neuromodulators.",
        ],
        "requirements": [
            "The Rome IV pain-frequency threshold and the two-of-three feature rule.",
            "The Bristol-scale-to-subtype mapping.",
            "The alarm-feature exclusion before the functional diagnosis.",
        ],
        "standards": [
            "Criteria cited to Rome IV (Mearin et al., Gastroenterology 2016).",
            "Subtype names per Rome IV convention (IBS-D, IBS-C, IBS-M, IBS-U).",
            "Post-infectious IBS named as the classic onset pattern.",
        ],
        "citations": [CIT_ROME, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: IBS is a miscalibrated conveyor - the "
            "belts run too fast or too slow, the sensors over-report every "
            "bump, and the control room amplifies the alarms - so the fix is "
            "recalibrating sensors and software, because the machinery itself "
            "is sound."
        ),
    },
    {
        "key": "motility",
        "name": "Motility Disorders: Gastroparesis and Esophageal Dysmotility",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Motility disorders are pump failures: the gut's muscle and "
            "nerves move contents too slowly, too weakly, or in the wrong "
            "pattern. Gastroparesis is delayed stomach emptying without "
            "mechanical obstruction - food sits, so patients report early "
            "satiety, nausea, vomiting of undigested food, and bloating; "
            "diabetes (vagal nerve injury) is the classic cause. Scintigraphy "
            "is the test: a radiolabeled meal, with more than 10 percent "
            "retained at four hours marking delay - a patient retaining 25 "
            "percent is two and a half times the cutoff. Achalasia is the "
            "esophageal mirror image: the lower sphincter fails to relax and "
            "the esophageal body loses peristalsis, so food and liquid hang "
            "up - dysphagia to solids and liquids, regurgitation, weight "
            "loss - diagnosed by high-resolution manometry and treated by "
            "pneumatic dilation, peroral endoscopic myotomy (POEM), or "
            "surgical myotomy. Diffuse esophageal spasm and hypercontractile "
            "(jackhammer) esophagus add chest pain to the dysphagia. "
            "Treatment is cause-directed: tight glucose control and "
            "prokinetics (metoclopramide, erythromycin) for gastroparesis, "
            "sphincter disruption for achalasia, smooth-muscle relaxants for "
            "spasm."
        ),
        "how_it_works": (
            "Motility disorders work as failed pump curves. In gastroparesis "
            "the antral pump weakens - vagal injury in diabetes, "
            "post-viral or idiopathic the rest - and the emptying curve "
            "flattens: normal stomachs retain at most 10 percent of a test "
            "meal at four hours, so 25 percent retained is 25/10 = 2.5 times "
            "the diagnostic cutoff. In achalasia the lower esophageal "
            "sphincter never gets the relax signal (inhibitory neuron loss) "
            "and the tubular esophagus loses its wave: manometry shows the "
            "integrated relaxation pressure stuck high and peristalsis "
            "absent. Therapy is mechanical logic: prokinetics push a weak "
            "pump harder, while achalasia treatment cuts or stretches the "
            "sphincter that will not open - dilation, POEM, or Heller "
            "myotomy. The demo computes the retention multiple against the "
            "10 percent cutoff and states the achalasia manometry pattern."
        ),
        "key_points": [
            "Motility disorders = pump failures: too slow, too weak, or wrong-pattern gut movement.",
            "Gastroparesis: delayed emptying without obstruction; >10% meal retained at 4 hours is diagnostic; 25% retained = 2.5x the cutoff.",
            "Diabetes (vagal injury) is the classic gastroparesis cause; prokinetics and glucose control are the therapy.",
            "Achalasia: sphincter will not relax + aperistalsis; dysphagia to solids and liquids; treated by dilation, POEM, or myotomy.",
            "Esophageal spasm variants add chest pain; manometry is the defining test.",
        ],
        "requirements": [
            "The pump-curve picture: normal vs flattened emptying.",
            "The 10-percent-at-4-hours scintigraphy cutoff and the retention multiple.",
            "The achalasia pattern: non-relaxing sphincter plus aperistalsis on manometry.",
        ],
        "standards": [
            "Scintigraphy cutoff per standard gastric-emptying protocol (>10% at 4 hours).",
            "Procedure names per standard usage (pneumatic dilation, POEM, Heller myotomy).",
            "Diabetes named as the classic gastroparesis etiology.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: motility disorders are pump-station "
            "failures on the line - the stomach's grinder stalls, the "
            "esophageal gate welds shut - and the work orders split cleanly: "
            "push a weak pump harder, or cut open a gate that will not obey "
            "its signal."
        ),
    },
    {
        "key": "crohn",
        "name": "Inflammatory Bowel Disease: Crohn's Disease",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Crohn's disease is chronic, transmural inflammation of the gut - "
            "through the full wall thickness - that can strike anywhere from "
            "mouth to anus but favors the terminal ileum and colon. "
            "Transmural is the word that explains the complications: deep "
            "ulcers become fissures, fissures become fistulas (tunnels to "
            "skin, bladder, or other bowel), and chronic scarring becomes "
            "strictures that obstruct. Skip lesions - diseased segments "
            "between healthy ones - and granulomas on biopsy distinguish it "
            "from ulcerative colitis. Presentation mixes gut and body: "
            "crampy right-lower-quadrant pain, diarrhea, weight loss, fevers, "
            "perianal disease, plus mouth ulcers, arthritis, skin lesions "
            "(erythema nodosum, pyoderma gangrenosum), and eye inflammation. "
            "The Montreal classification sorts every case three ways - age "
            "at diagnosis (3 groups), location (3 groups), behavior (3 "
            "groups: inflammatory, stricturing, penetrating) - for 3 x 3 x 3 "
            "= 27 phenotypes. Activity is scored by indices like the "
            "Harvey-Bradshaw (remission under 5). Therapy steps up: "
            "corticosteroids for flares, immunomodulators and biologics "
            "(anti-TNF, anti-integrin, anti-IL-12/23) for maintenance, "
            "surgery for strictures, fistulas, and failed medicine - "
            "resecting the worst segment while knowing the disease can "
            "recur at the join."
        ),
        "how_it_works": (
            "Crohn's works as a wall-deep immune siege. The immune system "
            "attacks the gut wall through all four layers; ulcers deepen "
            "into the muscle, and the body's repair tunnels outward - "
            "fistulas - or scars inward - strictures. Because inflammation is "
            "patchy, the classification is combinatorial: Montreal gives 3 "
            "age groups (under 17, 17-40, over 40), 3 locations (ileal, "
            "colonic, ileocolonic, plus upper modifiers), and 3 behaviors "
            "(nonstricturing-nonpenetrating, stricturing, penetrating): 3 x "
            "3 x 3 = 27 phenotypes, each with its own complication odds. The "
            "Harvey-Bradshaw index scores five items (well-being, pain, "
            "liquid stools, mass, complications); under 5 is remission. "
            "Biologics work by intercepting the siege's messengers - TNF, "
            "integrins, interleukins - before they recruit the next wave. "
            "The demo computes the 27 Montreal phenotypes and states the "
            "remission cutoff."
        ),
        "key_points": [
            "Crohn's = transmural (full-wall) inflammation anywhere mouth-to-anus, favoring terminal ileum and colon.",
            "Transmural depth explains fistulas (tunnels out) and strictures (scarring in); skip lesions and granulomas distinguish it.",
            "Montreal classification: 3 ages x 3 locations x 3 behaviors = 27 phenotypes.",
            "Harvey-Bradshaw index under 5 = remission; tracks flare vs control.",
            "Step-up therapy: steroids for flares, immunomodulators/biologics for maintenance, surgery for complications.",
        ],
        "requirements": [
            "The transmural-vs-mucosal distinction and the complications each depth produces.",
            "The Montreal three-axis classification and the 27-phenotype product.",
            "The step-up therapy sequence and what surgery can and cannot cure.",
        ],
        "standards": [
            "Montreal classification per standard IBD usage.",
            "Biologic classes named per standard usage (anti-TNF, anti-integrin, anti-IL-12/23).",
            "Extraintestinal manifestations listed as the classic set.",
        ],
        "citations": [CIT_CROHN, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: Crohn's is a siege that goes through the "
            "wall - not a surface scratch but a full-thickness breach - and "
            "the works responds the way any plant does under siege: seal the "
            "tunnels, cut out the ruined sections, and intercept the enemy's "
            "messengers before the next assault."
        ),
    },
    {
        "key": "uc",
        "name": "Inflammatory Bowel Disease: Ulcerative Colitis",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Ulcerative colitis is chronic inflammation limited to the "
            "colon's mucosa - the inner lining only - starting at the rectum "
            "and extending upward continuously, without skip lesions. "
            "Mucosal-only is the word that explains everything: bloody "
            "diarrhea (the raw lining weeps blood and mucus), urgency and "
            "tenesmus (the inflamed rectum misfires), crampy left-sided pain "
            "relieved by defecation - but no fistulas and no small-bowel "
            "disease, because the siege never goes through the wall. Extent "
            "is graded E1 (proctitis, rectum only), E2 (left-sided, to the "
            "splenic flexure), E3 (extensive, beyond it). Activity is scored "
            "by the Mayo score: four components (stool frequency, rectal "
            "bleeding, endoscopic findings, physician assessment) each 0 to "
            "3, for a 0-to-12 total - a patient scoring 2+2+1+1 = 6 sits in "
            "moderate disease. Severe flares can dilate the colon into toxic "
            "megacolon, a surgical emergency. Long-standing extensive "
            "colitis raises colorectal cancer risk, so surveillance "
            "colonoscopy runs every one to three years after eight to ten "
            "years of disease. Therapy: 5-aminosalicylates (mesalamine) for "
            "mild disease, steroids for flares, immunomodulators and "
            "biologics for maintenance - and colectomy, which removes the "
            "diseased organ entirely and cures the colitis."
        ),
        "how_it_works": (
            "Ulcerative colitis works as a surface fire spreading up from "
            "the rectum. The immune attack stays in the mucosa, so the wall "
            "holds - no tunnels, no strictures - but the lining ulcerates "
            "and bleeds into the lumen: bloody diarrhea with mucus, urgency "
            "from the irritable rectum. The Mayo score quantifies the fire: "
            "stool frequency (0-3) + rectal bleeding (0-3) + endoscopic "
            "severity (0-3) + physician global assessment (0-3) = 0 to 12. "
            "A 2+2+1+1 = 6 is moderate disease; 0-2 with no subscore above 1 "
            "is remission. Extent arithmetic sets cancer surveillance: E1 "
            "proctitis carries little excess risk, E3 extensive colitis of "
            "long duration carries the most, hence colonoscopy every 1-3 "
            "years after 8-10 years. Colectomy is the unique cure - remove "
            "the colon, remove the disease - which no Crohn's surgery can "
            "claim. The demo computes a Mayo total and maps it to severity."
        ),
        "key_points": [
            "Ulcerative colitis = mucosal-only colonic inflammation, continuous from the rectum upward; no skip lesions, no fistulas.",
            "Hallmarks: bloody diarrhea with mucus, urgency, tenesmus, left-sided pain relieved by defecation.",
            "Extent: E1 proctitis, E2 left-sided, E3 extensive; Mayo score 0-12 (four 0-3 components); 6 = moderate.",
            "Complications: toxic megacolon in severe flares; colorectal cancer risk in long-standing extensive disease.",
            "Therapy: mesalamine, steroids, immunomodulators/biologics; colectomy cures the colitis.",
        ],
        "requirements": [
            "The mucosal-only vs transmural distinction against Crohn's disease.",
            "The Mayo four-component scoring and the 0-12 severity reading.",
            "The extent-to-surveillance logic (E1/E2/E3 and the 8-10 year rule).",
        ],
        "standards": [
            "Montreal extent grades (E1/E2/E3) and Mayo score per standard IBD usage.",
            "Surveillance intervals per standard guidance (every 1-3 years after 8-10 years of extensive disease).",
            "Toxic megacolon named as the severe-flare surgical emergency.",
        ],
        "citations": [CIT_UC, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: ulcerative colitis is a surface fire in "
            "the last warehouse - the walls stand, but the floor coating "
            "burns and bleeds - and because the fire never leaves the "
            "building, demolishing the building ends the fire for good."
        ),
    },
    {
        "key": "lgib",
        "name": "Lower GI Bleeding and Diverticular Disease",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Lower gastrointestinal bleeding is blood loss from the colon or "
            "rectum - below the ligament of Treitz - and it shows as "
            "hematochezia: bright red blood per rectum, on the stool, or in "
            "the toilet. The common sources are diverticular bleeding, "
            "hemorrhoids and anal fissures, colorectal polyps and cancers, "
            "inflammatory bowel disease, and angiodysplasia in older adults. "
            "Diverticula are small pouches herniating through weak spots in "
            "the colonic wall where vessels penetrate; they are rare at 40 "
            "(about 5 percent of people), common at 60 (about 30 percent), "
            "and the rule past 80 (over 50 percent) - so in 1000 "
            "eighty-year-olds, more than 500 carry diverticulosis. Only a "
            "few percent ever bleed: at a 4 percent bleed rate, those 500 "
            "yield about 20 bleeders, usually painless and often stopping on "
            "its own. Diverticulitis - infection of a pouch - is the painful "
            "cousin: left-lower-quadrant pain, fever, and tenderness, treated "
            "with antibiotics for uncomplicated cases and surgery for "
            "perforation or abscess. Workup of lower bleeding is colonoscopy "
            "after bowel prep, with CT angiography when bleeding is brisk; "
            "most diverticular bleeds stop spontaneously, and endoscopic "
            "clipping handles the rest."
        ),
        "how_it_works": (
            "Lower GI bleeding works as a downstream leak: blood never meets "
            "stomach acid, so it stays red - hematochezia points below "
            "Treitz the way melena points above it. Diverticula form where "
            "the vasa recta pierce the circular muscle; high intraluminal "
            "pressure (low-fiber stool) herniates mucosa through those "
            "weak points, and the stretched vessel over the dome can rupture "
            "arterially - hence painless, sometimes dramatic bleeding. The "
            "age arithmetic: 5 percent at 40, 30 percent at 60, over 50 "
            "percent past 80 - in 1000 eighty-year-olds that is 500-plus "
            "with diverticulosis; a 4 percent bleed rate gives 500 x 0.04 = "
            "20 expected bleeders. Diverticulitis flips the picture: a "
            "pouch obstructs, bacteria overgrow, and the wall inflames - "
            "pain plus fever, the surgeon's disease rather than the "
            "endoscopist's. The demo computes the diverticulosis pool and "
            "the expected bleeders by age cohort."
        ),
        "key_points": [
            "Lower GI bleed = below the ligament of Treitz: hematochezia (bright red blood per rectum).",
            "Top sources: diverticular bleeding, hemorrhoids/fissures, polyps/cancer, IBD, angiodysplasia.",
            "Diverticulosis prevalence: ~5% at 40, ~30% at 60, >50% past 80 - 1000 octogenarians hold 500+ cases.",
            "About 4% of diverticulosis bleeds: ~20 expected bleeders per 1000 octogenarians, usually painless and self-limited.",
            "Diverticulitis (infected pouch) is the painful cousin: LLQ pain, fever; antibiotics if uncomplicated, surgery if perforated.",
        ],
        "requirements": [
            "The Treitz landmark: hematochezia points below, melena above.",
            "The diverticulum formation picture: pressure herniating mucosa where vessels pierce muscle.",
            "Age-cohort arithmetic for the diverticulosis pool and bleed rate.",
        ],
        "standards": [
            "Prevalence figures stated as typical age-cohort values with 'about' qualifiers.",
            "Diverticulosis (pouches present) vs diverticulitis (infected) kept terminologically distinct.",
            "Colonoscopy after prep stated as the standard workup; CT angiography for brisk bleeding.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the colon's wall develops weak-spot "
            "blisters where the supply lines pierce it - most never matter, "
            "a few burst their pipes, and the infected ones become the "
            "surgeon's problem; age writes the odds, pressure writes the "
            "blisters."
        ),
    },
    {
        "key": "polyps",
        "name": "Colorectal Polyps and Cancer Screening",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Colorectal polyps are growths on the colon's inner lining, and "
            "the adenoma is the one that matters: most colorectal cancers "
            "grow from adenomas through the adenoma-carcinoma sequence, a "
            "slow march of accumulating mutations over ten to fifteen years. "
            "That long dwell time is what makes screening work - find the "
            "adenoma, remove it, and the cancer never happens. Risk tracks "
            "size and histology: polyps under 1 centimeter are usually low "
            "risk, while those 1 centimeter or larger, with villous "
            "features or high-grade dysplasia, are advanced adenomas. "
            "Screening starts at age 45 for average-risk adults: colonoscopy "
            "every ten years is the reference standard (see and remove), "
            "annual fecal immunochemical testing (FIT) is the noninvasive "
            "alternative with about 74 percent sensitivity for cancer, and "
            "flexible sigmoidoscopy every five years covers the left side. "
            "The yield arithmetic: in 1000 average-risk 50-year-olds, "
            "roughly 250 to 300 harbor adenomas, and removing them prevents "
            "the majority of the cancers those adenomas would have become. "
            "After polypectomy, surveillance intervals follow the findings: "
            "ten years for one or two small adenomas, three years for "
            "advanced adenomas."
        ),
        "how_it_works": (
            "Polyp screening works as an interception program on a slow "
            "timeline. The adenoma-carcinoma sequence needs ten to fifteen "
            "years: normal mucosa to small adenoma to large adenoma to "
            "cancer, each step adding mutations (APC, KRAS, p53 in the "
            "classic Vogelstein model). A ten-year colonoscopy interval fits "
            "inside that window - the sweep passes before any adenoma can "
            "finish the march. Size is the triage number: under 1 cm, "
            "low-risk; 1 cm or more, advanced until proven otherwise. FIT "
            "detects the blood cancers shed: at 74 percent sensitivity, 100 "
            "cancers yield 100 x 0.74 = 74 detected and 26 missed - good "
            "enough for annual repetition, not good enough alone. The demo "
            "computes FIT-detected vs missed cancers in 100 cases and states "
            "the size threshold that separates routine from advanced "
            "adenomas."
        ),
        "key_points": [
            "Most colorectal cancers arise from adenomas via the 10-15 year adenoma-carcinoma sequence.",
            "Size triage: <1 cm usually low risk; >=1 cm, villous, or high-grade dysplasia = advanced adenoma.",
            "Screening starts at 45: colonoscopy every 10 years, annual FIT (~74% cancer sensitivity), sigmoidoscopy every 5 years.",
            "FIT on 100 cancers: ~74 detected, ~26 missed - repeat annually; colonoscopy sees and removes.",
            "Post-polypectomy surveillance: 10 years for 1-2 small adenomas, 3 years for advanced adenomas.",
        ],
        "requirements": [
            "The adenoma-carcinoma sequence and why the 10-year interval fits inside it.",
            "The 1-centimeter size threshold and the advanced-adenoma criteria.",
            "Test-tradeoff arithmetic: FIT sensitivity vs colonoscopy's see-and-remove.",
        ],
        "standards": [
            "Screening start age 45 and intervals per the U.S. Multi-Society Task Force guidance.",
            "FIT sensitivity stated as the approximate cancer figure (~74%).",
            "Surveillance intervals per standard post-polypectomy guidance.",
        ],
        "citations": [CIT_CRC, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: the adenoma is a slow-motion fault "
            "growing on the warehouse wall - ten to fifteen years from "
            "blemish to breach - and screening is the scheduled inspection "
            "that walks the walls on a shorter cycle than the fault needs to "
            "mature."
        ),
    },
    {
        "key": "endoscopy",
        "name": "Endoscopy and Colonoscopy: Concepts and Techniques",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Endoscopy is the specialty's camera: a flexible tube with a "
            "light, a lens, air and water channels, and a working port, "
            "steered through the gut's curves to see, photograph, biopsy, "
            "and treat. Upper endoscopy (EGD) examines esophagus, stomach, "
            "and duodenum - the workup for dysphagia, reflux complications, "
            "ulcers, and upper bleeding. Colonoscopy examines the full colon "
            "and terminal ileum after bowel prep - the screening, polyp, "
            "bleeding, and colitis instrument. Quality is measured, not "
            "assumed: the adenoma detection rate (ADR) - the share of "
            "screening colonoscopies finding at least one adenoma - must "
            "reach at least 25 percent overall (about 30 percent in men, 20 "
            "percent in women), and withdrawal time must average at least 6 "
            "minutes of careful looking on the way out. The yield: an "
            "endoscopist doing 200 screening colonoscopies at a 30 percent "
            "ADR finds adenomas in 200 x 0.30 = 60 patients - 60 cancers "
            "intercepted or prevented. Sedation (usually propofol or "
            "midazolam plus opioid), monitoring, and informed consent are "
            "part of every procedure; perforation and bleeding are the rare "
            "but real risks, quoted before every scope."
        ),
        "how_it_works": (
            "Endoscopy works as a steerable inspection robot with tools. "
            "Angulation wires bend the tip up-down and left-right; air "
            "insufflation opens the lumen; suction clears fluid; the working "
            "channel passes biopsy forceps, snares, clips, and needles. The "
            "exam has two passes - insertion to the cecum (confirmed by "
            "appendix orifice, ileocecal valve, and transillumination), then "
            "the slow withdrawal where the looking happens. Quality "
            "arithmetic keeps everyone honest: ADR = adenoma-positive "
            "screening exams divided by all screening exams; 200 exams at "
            "0.30 ADR = 60 patients with adenomas found and removed. "
            "Withdrawal under 6 minutes correlates with missed adenomas, so "
            "the clock is part of the standard. The demo computes the "
            "adenoma yield from exam volume and ADR and states the "
            "withdrawal-time floor."
        ),
        "key_points": [
            "Endoscopy = steerable camera with light, air/water, and a working channel for biopsy and therapy.",
            "Upper endoscopy (EGD): esophagus, stomach, duodenum. Colonoscopy: full colon and terminal ileum after prep.",
            "Adenoma detection rate must be >=25% (>=30% men, >=20% women); withdrawal time >=6 minutes.",
            "200 screening exams at 30% ADR = 60 patients with adenomas found - 60 cancers intercepted or prevented.",
            "Sedation, monitoring, consent, and quoted risks (perforation, bleeding) are part of every procedure.",
        ],
        "requirements": [
            "The instrument's parts and what each does (angulation, insufflation, working channel).",
            "The two-pass exam structure and cecal landmarks.",
            "ADR and withdrawal-time arithmetic as quality measures.",
        ],
        "standards": [
            "ADR benchmarks and withdrawal-time floor per standard colonoscopy quality guidance.",
            "Cecal landmarks named per standard usage (appendix orifice, ileocecal valve).",
            "Risks disclosed as the standard pair (perforation, bleeding).",
        ],
        "citations": [CIT_CRC, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: the endoscope is the inspector's crawler - "
            "sent down the pipe with lights, cameras, and tools - and the "
            "ADR is the inspector's batting average, published and audited, "
            "because an inspection that misses the faults is worse than none."
        ),
    },
    {
        "key": "endo_therapy",
        "name": "Endoscopic Therapy: Polypectomy, Banding, and ERCP",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Endoscopic therapy is surgery without the incision: treating "
            "disease through the scope's working channel. Polypectomy snares "
            "and removes colon polyps with a wire loop and electric current, "
            "retrieving them for pathology - the act that makes screening "
            "prevent cancer rather than merely find it. Variceal band "
            "ligation slips rubber bands over bleeding esophageal varices, "
            "strangling them; eradication typically takes two to four "
            "sessions. Endoscopic retrograde cholangiopancreatography "
            "(ERCP) is the biliary-pancreatic intervention: a side-viewing "
            "duodenoscope cannulates the ampulla of Vater, contrast maps the "
            "bile and pancreatic ducts, and stones are extracted, strictures "
            "stented, and sphincterotomies cut - with expert cannulation "
            "success above 90 percent (92 of 100 attempts). Endoscopic "
            "ultrasound (EUS) adds a sonar eye for staging cancers and "
            "draining pancreatic collections. Hemostasis tools - clips, "
            "thermal probes, injected epinephrine - stop bleeding lesions on "
            "sight. Complications are real and quoted: post-ERCP "
            "pancreatitis in a few percent, bleeding and perforation under "
            "one percent for polypectomy. The therapy end of the scope is "
            "why gastroenterology is procedural: diagnosis and treatment in "
            "one insertion."
        ),
        "how_it_works": (
            "Endoscopic therapy works by bringing the operating room to the "
            "lesion. The snare closes around a polyp's stalk, blended "
            "current cuts and coagulates, and the specimen is retrieved - "
            "complete resection confirmed when pathology reports clear "
            "margins. Band ligation works by ischemia: the banded varix "
            "thromboses, sloughs, and scars over two to four sessions. ERCP "
            "works by retrograde access: from the duodenum, a catheter "
            "enters the common bile duct against the normal flow direction, "
            "and a sphincterotomy opens the ampulla so stones up to the "
            "duct's diameter can be swept out with a balloon or basket. "
            "Success arithmetic: at 92 percent cannulation, 100 attempts "
            "yield 100 x 0.92 = 92 successful duct accesses. The demo "
            "computes ERCP successes from attempts and states the banding "
            "session range."
        ),
        "key_points": [
            "Polypectomy: snare resection through the scope - the act that makes screening prevent cancer.",
            "Variceal band ligation: rubber bands strangulate varices; eradication in 2-4 sessions.",
            "ERCP: retrograde bile/pancreatic duct access - stone extraction, stenting, sphincterotomy; >90% cannulation success.",
            "EUS adds sonar staging and drainage; clips, thermal probes, and epinephrine give on-sight hemostasis.",
            "Quoted risks: post-ERCP pancreatitis in a few percent; polypectomy bleeding/perforation under 1%.",
        ],
        "requirements": [
            "The snare-resection sequence and why margin pathology matters.",
            "The band-ligation ischemia mechanism and session count.",
            "Retrograde access logic: entering the bile duct against normal flow from the duodenum.",
        ],
        "standards": [
            "Procedure names per standard usage (ERCP, EUS, POEM-adjacent myotomy not conflated).",
            "Success and complication rates stated as typical expert-center values with 'about' qualifiers.",
            "Ampulla of Vater named as the cannulation target.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: therapeutic endoscopy is the repair crew "
            "that travels inside the pipe - snipping faults, banding burst "
            "weak spots, rodding the drains from the downstream end - the "
            "works fixed without opening the building."
        ),
    },
    {
        "key": "pancreatitis",
        "name": "Acute Pancreatitis",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Acute pancreatitis is the pancreas digesting itself: enzymes "
            "activate inside the gland instead of in the duodenum, and the "
            "organ inflames - sometimes mildly, sometimes catastrophically. "
            "Two causes own about 80 percent of cases: gallstones lodging at "
            "the ampulla and alcohol. The pain is classic - sudden, severe, "
            "epigastric, boring through to the back, worse lying flat - with "
            "nausea and vomiting. Diagnosis needs two of three: characteristic "
            "pain, lipase more than three times the upper limit of normal, "
            "and imaging showing inflammation. Severity is scored early: "
            "Ranson's eleven criteria (five at admission, six at 48 hours) "
            "with three or more marking severe disease, or the Glasgow and "
            "APACHE systems. Management is supportive and aggressive: "
            "vigorous IV fluids (often 250-500 mL per hour initially - 300 "
            "mL/h for 12 hours is 3.6 liters), pain control, antiemetics, "
            "and early feeding when possible; antibiotics only for infected "
            "necrosis, proven by fine-needle aspiration or gas on imaging. "
            "Gallstone pancreatitis gets its stone dealt with - ERCP for "
            "cholangitis or persistent obstruction, cholecystectomy before "
            "discharge to prevent recurrence. Necrosis, organ failure, and "
            "infection are the killers; most mild cases resolve in days."
        ),
        "how_it_works": (
            "Pancreatitis works as premature detonation. Trypsinogen "
            "activates to trypsin inside the acinar cell - normally it "
            "activates only in the duodenum via enterokinase - and trypsin "
            "then activates the whole enzyme cascade in place: autodigestion. "
            "Capillaries leak, the gland swells, and systemic inflammatory "
            "mediators spill over - third-spacing fluid out of the vessels, "
            "which is why aggressive fluids are the therapy: 300 mL per hour "
            "x 12 hours = 3600 mL, replacing what the inflammation "
            "sequesters. Lipase above three times normal is the diagnostic "
            "line because the pancreas holds the body's largest lipase "
            "reserve; Ranson's eleven criteria count the systemic toll "
            "(age, white cells, glucose, LDH, AST at admission; hematocrit "
            "fall, BUN rise, calcium fall, PaO2, base deficit, fluid "
            "sequestration at 48 hours), with 3+ marking severe. The demo "
            "computes the 12-hour fluid total and states the lipase and "
            "Ranson thresholds."
        ),
        "key_points": [
            "Acute pancreatitis = premature enzyme activation inside the gland: autodigestion; gallstones and alcohol cause ~80%.",
            "Classic pain: sudden severe epigastric, boring to the back, worse supine; with nausea and vomiting.",
            "Diagnosis needs 2 of 3: characteristic pain, lipase >3x upper limit of normal, imaging inflammation.",
            "Ranson's 11 criteria: >=3 = severe; management is aggressive IV fluids (300 mL/h x 12 h = 3.6 L), pain control, early feeding.",
            "Antibiotics only for infected necrosis; gallstone cases get ERCP/cholecystectomy to prevent recurrence.",
        ],
        "requirements": [
            "The premature-activation mechanism (trypsinogen to trypsin in the wrong place).",
            "The 2-of-3 diagnostic rule and the lipase threshold.",
            "Fluid-resuscitation arithmetic and the Ranson severity count.",
        ],
        "standards": [
            "Diagnostic criteria per standard clinical usage (2 of 3 rule).",
            "Ranson criteria count stated as 5 at admission + 6 at 48 hours.",
            "Fluid rates stated as typical initial resuscitation ranges.",
        ],
        "citations": [CIT_PANC, CIT_SLEIS, CIT_YAMADA],
        "sig_lens": (
            "His Signature reading: pancreatitis is a munitions plant "
            "detonating its own stockpile - the shells armed on the assembly "
            "line instead of at the target - and the response is the "
            "firefighter's: flood the building, let it burn out, and remove "
            "whatever jammed the loading dock."
        ),
    },
    {
        "key": "gallstones",
        "name": "Gallstone Disease and Cholecystitis",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Gallstones are solidified bile: cholesterol stones (about 80 "
            "percent in Western populations) when bile carries more "
            "cholesterol than its salts can dissolve, pigment stones from "
            "excess bilirubin in hemolysis or infection. Most stones sit "
            "quietly for life; trouble starts when one lodges in the "
            "gallbladder neck or cystic duct. Biliary colic is the warning - "
            "steady right-upper-quadrant pain after fatty meals, lasting "
            "minutes to hours, then passing. Cholecystitis is the "
            "complication: the lodged stone obstructs, the gallbladder "
            "inflames, and pain becomes constant with fever and a positive "
            "Murphy's sign (inspiratory arrest on palpation of the right "
            "upper quadrant). Ultrasound is the test - stones, wall "
            "thickening, pericholecystic fluid - and HIDA scanning confirms "
            "cystic-duct obstruction when ultrasound equivocal; a gallbladder "
            "ejection fraction under 35 percent marks dyskinesia. Of 100 "
            "symptomatic stone carriers, about 80 carry cholesterol stones. "
            "Treatment of symptomatic disease is laparoscopic "
            "cholecystectomy - the gallbladder is expendable, the bile duct "
            "is not - with antibiotics and fluids bridging acute "
            "cholecystitis to surgery. Asymptomatic stones found incidentally "
            "are left alone."
        ),
        "how_it_works": (
            "Gallstones work as a solubility failure. Bile holds cholesterol "
            "in mixed micelles of bile salts and lecithin; when cholesterol "
            "exceeds the solubilizing capacity - the lithogenic index above "
            "1 - crystals nucleate, aggregate, and grow into stones. A "
            "floating stone is harmless; a lodged stone converts pressure "
            "into inflammation: the obstructed gallbladder distends, its "
            "wall becomes ischemic, bacteria overgrow, and cholecystitis "
            "follows. Murphy's sign is the inflamed gallbladder meeting the "
            "examiner's hand as the diaphragm descends. HIDA quantifies "
            "pump function: after cholecystokinin, counts ejected divided by "
            "counts at fill give the ejection fraction - 40 percent is "
            "normal (above the 35 percent cutoff), 20 percent is dyskinesia. "
            "Composition arithmetic: in 100 Western stone patients, 100 x "
            "0.80 = 80 carry cholesterol stones. The demo computes the "
            "cholesterol-stone share and tests an ejection fraction against "
            "the 35 percent line."
        ),
        "key_points": [
            "Gallstones = solidified bile; cholesterol stones ~80% in Western populations; pigment stones from bilirubin excess.",
            "Biliary colic: steady RUQ pain after fatty meals, minutes to hours, then passes - the warning.",
            "Cholecystitis: lodged stone + inflammation = constant pain, fever, positive Murphy's sign.",
            "Ultrasound is the test; HIDA confirms obstruction; ejection fraction <35% marks dyskinesia.",
            "Symptomatic disease gets laparoscopic cholecystectomy; asymptomatic stones are left alone.",
        ],
        "requirements": [
            "The micelle-solubility picture and what makes bile lithogenic.",
            "The colic-vs-cholecystitis distinction (transient vs constant + fever).",
            "The HIDA ejection-fraction definition and the 35 percent cutoff.",
        ],
        "standards": [
            "Stone composition share stated as the Western-population figure (~80% cholesterol).",
            "Murphy's sign described per standard examination usage.",
            "Surgery stated as laparoscopic cholecystectomy for symptomatic disease.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: gallstones are scale in the solvent "
            "tank's settling sump - the fluid chemistry drifted past its "
            "dissolving limit and precipitated - and when a lump jams the "
            "sump's outlet, the sump itself is expendable but the main drain "
            "is not."
        ),
    },
    {
        "key": "biliary",
        "name": "Biliary Obstruction and Jaundice",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Biliary obstruction is a blocked bile drain, and jaundice is its "
            "visible signature: yellow skin and eyes when bilirubin exceeds "
            "about 2 to 3 mg/dL. The fraction tells the location: "
            "unconjugated (indirect) bilirubinemia points before the liver "
            "(hemolysis, Gilbert's), conjugated (direct) bilirubinemia "
            "points at or after the liver (cholestasis, obstruction). A "
            "classic obstructive pattern is total bilirubin 5.2 mg/dL with "
            "direct 4.1 - the direct share is 4.1/5.2 = 78.8 percent, "
            "overwhelmingly conjugated, the cholestatic signature. Causes "
            "divide by level: intrahepatic (drug injury, primary biliary "
            "cholangitis, sepsis) and extrahepatic (common bile duct stones, "
            "pancreatic head cancer, cholangiocarcinoma, strictures). "
            "Obstruction backs up the whole biliary tree: pruritus from "
            "retained bile salts, pale stools and dark urine (conjugated "
            "bilirubin spills into urine, none reaches stool), fat "
            "malabsorption, and - if infected - Charcot's triad of fever, "
            "jaundice, and right-upper-quadrant pain, the cholangitis alarm. "
            "Workup climbs from ultrasound (duct dilation?) to MRCP "
            "(noninvasive mapping) to ERCP (mapping plus therapy: stone "
            "extraction, stenting). Unit fluency matters: 3 mg/dL equals 3 x "
            "17.1 = 51.3 micromol/L."
        ),
        "how_it_works": (
            "Biliary obstruction works as a dammed river. Hepatocytes "
            "conjugate bilirubin and pump it into the canaliculi; the common "
            "bile duct carries it to the duodenum. A dam - stone, stricture, "
            "tumor - raises upstream pressure, conjugated bilirubin "
            "regurgitates into blood, and the labs show the direct fraction "
            "dominating: 4.1 of 5.2 mg/dL is 78.8 percent direct, the "
            "obstructive signature (hemolysis would show the indirect "
            "fraction dominating instead). Retained bile salts deposit in "
            "skin (pruritus); absent intestinal bilirubin pales the stool; "
            "spilled conjugated bilirubin darkens the urine. Conversion "
            "arithmetic keeps units straight: mg/dL x 17.1 = micromol/L, so "
            "3 mg/dL = 51.3 micromol/L. The demo computes the direct "
            "fraction, classifies the pattern, and converts the units."
        ),
        "key_points": [
            "Jaundice appears when bilirubin exceeds ~2-3 mg/dL; the direct/indirect fraction locates the lesion.",
            "Direct-dominant (e.g. 4.1 of 5.2 mg/dL = 78.8%) = cholestatic/obstructive; indirect-dominant = pre-hepatic.",
            "Obstruction signs: pruritus, pale stools, dark urine, fat malabsorption; Charcot's triad (fever, jaundice, RUQ pain) = cholangitis.",
            "Causes by level: intrahepatic (drugs, PBC, sepsis) vs extrahepatic (CBD stones, pancreatic cancer, strictures).",
            "Workup: ultrasound for dilation, MRCP for mapping, ERCP for therapy; bilirubin mg/dL x 17.1 = micromol/L.",
        ],
        "requirements": [
            "The conjugation sequence and why the fraction locates the block.",
            "The dammed-river consequence chain (pruritus, stool, urine, malabsorption).",
            "Charcot's triad as the infected-obstruction alarm.",
        ],
        "standards": [
            "Bilirubin thresholds and conversion factor (17.1) per standard laboratory usage.",
            "Charcot's triad stated as fever, jaundice, RUQ pain.",
            "Imaging sequence per standard practice (ultrasound, MRCP, ERCP).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: biliary obstruction is a dammed effluent "
            "channel - the refinery's waste line backs up, the yellow marker "
            "dye spills where it should never be seen, and the gauge that "
            "reads which fraction dominates tells the crew exactly which "
            "side of the dam they're standing on."
        ),
    },
    {
        "key": "cirrhosis",
        "name": "Chronic Liver Disease and Cirrhosis",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Chronic liver disease is long-standing hepatic injury - from "
            "alcohol, viral hepatitis, or fatty liver - and cirrhosis is its "
            "end stage: fibrosis plus regenerative nodules that remodel the "
            "organ into scar. Scarred liver resists portal blood flow "
            "(portal hypertension) and fails its chemistry (synthetic "
            "failure). Portal hypertension's consequences are mechanical: "
            "esophageal and gastric varices that can bleed catastrophically, "
            "splenomegaly with low platelets, and ascites - fluid weeping "
            "into the abdomen. Synthetic failure's consequences are "
            "chemical: low albumin, prolonged INR (clotting factors "
            "missing), and hepatic encephalopathy when ammonia bypasses the "
            "liver through portosystemic collaterals. Prognosis is scored by "
            "Child-Pugh: five parameters (bilirubin, albumin, INR, ascites, "
            "encephalopathy) each 1 to 3 points, total 5 to 15 - class A "
            "5-6, B 7-9, C 10-15. A patient scoring 2+2+1+2+1 = 8 sits in "
            "class B, moderate dysfunction. Management treats complications, "
            "not the scar: band varices, diurese ascites, lactulose and "
            "rifaximin for encephalopathy, screen for hepatocellular "
            "carcinoma every six months - and transplant evaluation for the "
            "decompensated, because no drug un-scars a cirrhotic liver."
        ),
        "how_it_works": (
            "Cirrhosis works as a two-failure machine. Fibrosis stiffens the "
            "sinusoids, so portal pressure rises: normal portal pressure "
            "under 5 mmHg becomes hypertensive above 10, and varices form "
            "where the high-pressure portal system meets low-pressure "
            "systemic veins (esophagus, rectum, umbilicus). Simultaneously "
            "hepatocyte mass falls, so albumin, clotting factors, and "
            "ammonia clearance fail together. Child-Pugh quantifies both "
            "failures in one number: five 1-to-3 scales summed - a 2+2+1+2+1 "
            "= 8 lands in class B (7-9), the middle ground where "
            "complications are managed but transplant is discussed. "
            "Encephalopathy therapy is ammonia arithmetic: lactulose "
            "acidifies the colon, converting absorbable NH3 to trapped "
            "NH4+, and rifaximin suppresses the ammonia-making bacteria. "
            "The demo computes a Child-Pugh total and assigns its class."
        ),
        "key_points": [
            "Cirrhosis = fibrosis + regenerative nodules: portal hypertension (mechanical) plus synthetic failure (chemical).",
            "Portal hypertension: varices, splenomegaly, ascites. Synthetic failure: low albumin, high INR, encephalopathy.",
            "Child-Pugh: five 1-3 point parameters, total 5-15; A 5-6, B 7-9, C 10-15; 8 = class B.",
            "Management treats complications: band varices, diurese ascites, lactulose/rifaximin for encephalopathy.",
            "HCC screening every 6 months; transplant evaluation for decompensation - no drug reverses established cirrhosis.",
        ],
        "requirements": [
            "The two-failure model: pressure consequences vs chemistry consequences.",
            "The Child-Pugh five parameters and the 5-15 scoring with class boundaries.",
            "The encephalopathy-ammonia mechanism and the lactulose trapping chemistry.",
        ],
        "standards": [
            "Child-Pugh classes per standard usage (A 5-6, B 7-9, C 10-15).",
            "Portal hypertension threshold concepts stated qualitatively per standard teaching.",
            "HCC surveillance interval per standard guidance (every 6 months).",
        ],
        "citations": [CIT_ALD, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: cirrhosis is a refinery rebuilt in scar "
            "tissue - the pipes narrowed so pressure backs up and bursts the "
            "relief valves, the chemistry halls half-staffed so the outputs "
            "fail - and the only work order left is managing the failures "
            "while the replacement plant is commissioned."
        ),
    },
    {
        "key": "hepatitis",
        "name": "Viral Hepatitis",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Viral hepatitis is liver inflammation caused by hepatotropic "
            "viruses, named A through E with distinct routes and fates. "
            "Hepatitis A and E spread fecal-orally (contaminated food and "
            "water) and cause acute, self-limited illness - no chronic "
            "carrier state. Hepatitis B spreads by blood and sex, and "
            "hepatitis C by blood: both can go chronic, and chronic B and C "
            "drive cirrhosis and hepatocellular carcinoma over decades. "
            "Hepatitis D is the satellite - it infects only with B. "
            "Serology reads the timeline: surface antigen (HBsAg) means "
            "current infection, surface antibody (anti-HBs) means immunity, "
            "core antibody (anti-HBc) means exposure - three markers, 2 x 2 "
            "x 2 = 8 possible patterns, each with a meaning. Viral load is "
            "read in logs: 8 log10 IU/mL is 10 to the 8th, 100,000,000 "
            "IU/mL of HBV DNA. The modern triumph is hepatitis C: "
            "direct-acting antivirals cure over 95 percent in 8 to 12 weeks, "
            "one of medicine's cleanest victories. Hepatitis B is suppressed, "
            "not cured, with tenofovir or entecavir; A and E are prevented "
            "by sanitation and the A vaccine. Every chronic carrier gets HCC "
            "surveillance: the viruses that linger are the ones that cause "
            "cancer."
        ),
        "how_it_works": (
            "Viral hepatitis works as five different tenancy agreements. A "
            "and E are short-stay visitors - in through the gut, out through "
            "immunity. B and C sign long leases: B integrates its DNA into "
            "hepatocytes (hence suppression, not cure), C replicates in the "
            "cytoplasm (hence curable when replication is blocked). The "
            "serology panel is three binary markers - HBsAg, anti-HBs, "
            "anti-HBc - giving 2^3 = 8 patterns: all negative is naive, "
            "anti-HBs alone is vaccinated, HBsAg positive is infected, and "
            "so on. Viral-load logs compress the enormous: 8 log10 IU/mL = "
            "100,000,000 IU/mL, and a 4-log drop on therapy means 99.99 "
            "percent of virus gone. Cure arithmetic for C: at 95 percent "
            "cure, 100 treated patients yield 95 sustained virologic "
            "responses. The demo computes the 8 serology patterns, the "
            "log-to-linear viral load, and the expected cures per 100 "
            "treated."
        ),
        "key_points": [
            "Hepatitis A/E: fecal-oral, acute and self-limited. B: blood/sex, can chronify. C: blood, can chronify. D: needs B.",
            "Chronic B and C drive cirrhosis and hepatocellular carcinoma over decades.",
            "Serology: HBsAg (current infection), anti-HBs (immunity), anti-HBc (exposure) - 8 patterns from 3 markers.",
            "Viral loads read in logs: 8 log10 IU/mL = 100,000,000 IU/mL.",
            "Direct-acting antivirals cure >95% of hepatitis C in 8-12 weeks; hepatitis B is suppressed with tenofovir/entecavir.",
        ],
        "requirements": [
            "The five viruses' routes and chronicity fates.",
            "The three-marker serology panel and pattern reading.",
            "Log-scale viral load literacy and the cure-vs-suppression distinction.",
        ],
        "standards": [
            "Transmission routes per standard epidemiologic usage.",
            "Serology markers named per standard laboratory usage (HBsAg, anti-HBs, anti-HBc).",
            "Cure and suppression claims stated with 'over 95%' and drug names per standard guidance.",
        ],
        "citations": [CIT_HBV, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the hepatitis viruses are five different "
            "squatters in the refinery - two passing through, two signing "
            "long leases, one that can only squat where another already "
            "does - and the eviction record runs from total victory (C) to "
            "permanent containment (B)."
        ),
    },
    {
        "key": "nafld",
        "name": "Fatty Liver Disease: NAFLD and MASLD",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Nonalcoholic fatty liver disease - renamed metabolic "
            "dysfunction-associated steatotic liver disease (MASLD) to tie "
            "it to its cause - is fat in the liver without significant "
            "alcohol: the hepatic face of the metabolic syndrome. It runs a "
            "spectrum: simple steatosis (fat without inflammation, usually "
            "benign), steatohepatitis (fat plus inflammation and ballooned "
            "hepatocytes - NASH/MASH), fibrosis, and cirrhosis. Roughly a "
            "quarter to a third of adults worldwide carry some degree of "
            "it, tracking obesity and type 2 diabetes. Most patients are "
            "found by accident - mildly raised ALT on routine labs, bright "
            "liver on ultrasound - and most never progress; the clinical "
            "question is always who has fibrosis. The FIB-4 index answers "
            "without a biopsy: (age x AST) / (platelets x sqrt(ALT)). A "
            "55-year-old with AST 45, ALT 60, platelets 200 gives (55 x 45) "
            "/ (200 x 7.746) = 2475 / 1549.2 = 1.60 - in the indeterminate "
            "zone (under 1.3 rules out, over 2.67 rules in advanced "
            "fibrosis; over 2.0 for age 65+). Management is metabolic: "
            "weight loss of 7-10 percent can regress steatohepatitis, "
            "diabetes and lipid control, no safe alcohol threshold in "
            "fibrosis - and the new incretin-era drugs are rewriting the "
            "weight-loss side of the equation."
        ),
        "how_it_works": (
            "MASLD works as an overflow injury. When adipose storage "
            "overflows - obesity, insulin resistance - free fatty acids "
            "flood the liver; hepatocytes store them as triglyceride "
            "droplets. Stored fat is inert, but lipotoxic species inflame: "
            "steatohepatitis is the liver's wound-healing response running "
            "chronically, laying down fibrosis year by year. FIB-4 reads "
            "the fibrosis risk from routine labs: age times AST in the "
            "numerator (injury accumulating with time), platelets times the "
            "square root of ALT in the denominator (falling platelets mark "
            "portal hypertension, ALT normalizes the injury). For age 55, "
            "AST 45, ALT 60, platelets 200: numerator 55 x 45 = 2475; "
            "denominator 200 x sqrt(60) = 200 x 7.746 = 1549.2; FIB-4 = "
            "2475/1549.2 = 1.597 - indeterminate, neither ruled out nor "
            "ruled in, the honest middle where elastography decides. The "
            "demo computes FIB-4 and tests it against the 1.3 and 2.67 "
            "cutoffs."
        ),
        "key_points": [
            "NAFLD renamed MASLD: hepatic fat from metabolic dysfunction, not alcohol; ~25-30% of adults affected.",
            "Spectrum: simple steatosis -> steatohepatitis (NASH/MASH) -> fibrosis -> cirrhosis.",
            "FIB-4 = (age x AST)/(platelets x sqrt(ALT)): <1.3 rules out, >2.67 rules in advanced fibrosis.",
            "Example: 55 y/o, AST 45, ALT 60, platelets 200 -> FIB-4 = 1.60, indeterminate - elastography decides.",
            "Management: 7-10% weight loss regresses steatohepatitis; metabolic control; no safe alcohol in fibrosis.",
        ],
        "requirements": [
            "The steatosis-to-fibrosis spectrum and the overflow-injury mechanism.",
            "The FIB-4 formula and its two decision cutoffs.",
            "The rename rationale: metabolic dysfunction as the named cause.",
        ],
        "standards": [
            "Terminology per the 2023 multisociety rename (NAFLD -> MASLD, NASH -> MASH).",
            "FIB-4 cutoffs per standard usage (1.3 and 2.67; 2.0 for age 65+).",
            "Prevalence stated as the approximate global adult range.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: MASLD is the refinery flooded with more "
            "feedstock than its tanks were built for - the overflow first "
            "just sits in the yard, then starts corroding the works - and "
            "the FIB-4 gauge reads the corrosion from the control room "
            "without opening a single tank."
        ),
    },
    {
        "key": "cancer_upper",
        "name": "GI Cancers: Esophageal and Gastric",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Upper GI cancers are diagnosed late and kill quickly, which is "
            "why their risk factors and alarms matter. Esophageal cancer "
            "comes in two diseases: squamous cell carcinoma of the upper and "
            "mid esophagus (tobacco, alcohol, hot beverages, achalasia) and "
            "adenocarcinoma of the lower esophagus (Barrett's esophagus from "
            "chronic reflux, obesity) - the latter rising in Western "
            "countries. Gastric cancer follows chronic Helicobacter pylori "
            "gastritis through atrophy, intestinal metaplasia, and dysplasia "
            "over decades; salt-preserved foods and smoking add risk. The "
            "presenting alarm is dysphagia that progresses from solids to "
            "liquids, or early satiety with weight loss - never ignore new "
            "dysphagia in an older adult. Staging is TNM: depth of wall "
            "invasion (T), nodes (N), metastases (M) - three axes that set "
            "resectability. Tumor bulk follows the cube law: a lesion "
            "doubling in diameter from 2 to 4 cm grows 2^3 = 8 times in "
            "volume, which is why size so often tracks prognosis. Treatment "
            "is stage-driven: endoscopic resection for the earliest, "
            "chemoradiation plus esophagectomy or gastrectomy for "
            "locoregional disease, systemic therapy for the metastatic. "
            "Five-year survival overall remains near 20 percent for "
            "esophageal and just over 30 percent for gastric cancer in most "
            "Western series - the argument for finding them early."
        ),
        "how_it_works": (
            "Upper GI cancers work as decades-long mutation accumulations "
            "surfacing as mechanical obstruction. In the esophagus, chronic "
            "acid bathes the lower lining until intestinal metaplasia "
            "(Barrett's) appears, then dysplasia, then adenocarcinoma; in "
            "the stomach, H. pylori's chronic gastritis walks the Correa "
            "cascade - atrophy, metaplasia, dysplasia, cancer. TNM staging "
            "is three-axis arithmetic: T (wall depth, 1-4), N (node count), "
            "M (0 or 1) - M1 ends curative intent. The volume arithmetic "
            "explains the urgency: a sphere's volume scales with the cube "
            "of diameter, so 2 cm to 4 cm is (4/2)^3 = 8 times the tumor "
            "burden - each doubling of diameter multiplies the disease "
            "eightfold. Screening the high-risk (Barrett's surveillance "
            "every 3-5 years by dysplasia grade; H. pylori eradication as "
            "gastric cancer prevention) is the only lever that moves the "
            "survival number. The demo computes the 8x volume multiple and "
            "states the TNM axes."
        ),
        "key_points": [
            "Esophageal cancer: squamous (tobacco/alcohol, upper/mid) vs adenocarcinoma (Barrett's/reflux/obesity, lower).",
            "Gastric cancer follows H. pylori gastritis through the Correa cascade (atrophy -> metaplasia -> dysplasia -> cancer).",
            "Alarm: progressive dysphagia (solids to liquids) or early satiety with weight loss - never ignore in older adults.",
            "TNM staging: wall depth (T), nodes (N), metastases (M); tumor volume scales with diameter cubed (2->4 cm = 8x).",
            "Overall 5-year survival ~20% esophageal, ~30%+ gastric in Western series - early detection is the lever.",
        ],
        "requirements": [
            "The two esophageal histologies and their distinct risk factors.",
            "The Correa cascade for gastric carcinogenesis.",
            "TNM three-axis logic and the cube-law volume arithmetic.",
        ],
        "standards": [
            "Histology and risk-factor pairings per standard oncologic usage.",
            "Survival figures stated as approximate overall Western-series values.",
            "Barrett's surveillance concept stated per standard practice.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: upper GI cancers are slow corrosion "
            "finally breaking through - decades of acid or bacterial "
            "irritation rewriting the lining's work orders until the tissue "
            "stops taking orders at all - and the cube law is why the "
            "inspection schedule cannot slip."
        ),
    },
    {
        "key": "cancer_crc",
        "name": "GI Cancers: Colorectal",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Colorectal cancer is the GI cancer screening was built to "
            "defeat - and largely does, where screening reaches people. It "
            "is among the most common cancers worldwide and a leading cancer "
            "killer, yet most cases begin as removable adenomas (see the "
            "polyps record). Risk concentrates with age, family history "
            "(first-degree relative with colorectal cancer or advanced "
            "adenoma), long-standing inflammatory bowel disease, and the "
            "inherited syndromes - familial adenomatous polyposis (hundreds "
            "to thousands of polyps, near-certain cancer without colectomy) "
            "and Lynch syndrome (mismatch-repair defect, early cancers "
            "across several organs). Presentation is often silent until "
            "advanced: iron-deficiency anemia from chronic oozing, change in "
            "bowel habit, rectal bleeding, obstruction on the left, "
            "vague pain on the right. Stage sets survival more than anything "
            "in oncology: stage I five-year survival near 90 percent, stage "
            "IV near 14 percent - a 76-point gap that is the entire argument "
            "for screening. Treatment is surgical resection for localized "
            "disease (with the lymph-node harvest staging it), plus "
            "chemotherapy for node-positive and metastatic disease, and "
            "rectal cancers add radiation. FIT detects about 74 of 100 "
            "cancers; colonoscopy finds and removes the precursors."
        ),
        "how_it_works": (
            "Colorectal cancer works as the adenoma-carcinoma sequence "
            "completed: APC mutation starts the adenoma, KRAS accelerates "
            "it, p53 loss unlocks invasion - the Vogelstein model in three "
            "genetic hits over ten to fifteen years. Staging is anatomic "
            "arithmetic: T (through the wall?), N (how many nodes?), M "
            "(distant spread?) - and each step up roughly halves the "
            "survival odds, from ~90 percent at stage I to ~14 percent at "
            "stage IV, a 76-percentage-point fall. Screening breaks the "
            "sequence at the adenoma step: remove the polyp and the three "
            "hits never complete. FIT's 74 percent sensitivity means 100 "
            "cancers give 100 x 0.74 = 74 detected; colonoscopy's value is "
            "the other column - the adenomas removed before they count as "
            "cancer at all. The demo computes the stage-survival gap and "
            "the FIT detection count."
        ),
        "key_points": [
            "Colorectal cancer: common and deadly, yet largely preventable via adenoma removal - the screening success story.",
            "Risk: age, family history, long-standing IBD, FAP (hundreds-thousands of polyps), Lynch syndrome.",
            "Often silent until advanced: iron-deficiency anemia, bowel-habit change, rectal bleeding, obstruction.",
            "Stage I 5-year survival ~90%, stage IV ~14% - a 76-point gap that justifies screening.",
            "Treatment: surgical resection for localized disease, chemotherapy for node-positive/metastatic, radiation for rectal.",
        ],
        "requirements": [
            "The Vogelstein three-hit model (APC, KRAS, p53) and the 10-15 year timeline.",
            "The stage-survival gradient and what each stage means anatomically.",
            "The inherited syndromes and why they change screening rules.",
        ],
        "standards": [
            "Survival figures stated as approximate stage-specific values.",
            "Syndrome names per standard usage (FAP, Lynch syndrome / HNPCC).",
            "Screening modalities per the U.S. Multi-Society Task Force guidance.",
        ],
        "citations": [CIT_CRC, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: colorectal cancer is the fault the "
            "inspection program was designed to catch - three bad work "
            "orders accumulating over a decade on the warehouse wall - and "
            "the 76-point survival gap between caught-early and caught-late "
            "is the inspection program's report card."
        ),
    },
    {
        "key": "cancer_pancliver",
        "name": "GI Cancers: Pancreatic and Hepatocellular",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Pancreatic and liver cancers are the GI malignancies with the "
            "grimmest numbers, for opposite anatomic reasons. Pancreatic "
            "ductal adenocarcinoma hides deep in the retroperitoneum behind "
            "the stomach: painless jaundice (head tumors blocking the bile "
            "duct), vague back pain, weight loss, and new-onset diabetes in "
            "an older adult are the classic whispers - usually heard too "
            "late, with overall five-year survival near 12 percent and only "
            "the small resectable minority (no vascular encasement, no "
            "metastases) reaching for cure via the Whipple procedure. "
            "Hepatocellular carcinoma (HCC) grows in cirrhotic livers - "
            "chronic hepatitis B and C, alcohol, MASLD - which is why every "
            "cirrhotic gets ultrasound surveillance every six months: 100 "
            "cirrhotics under surveillance generate 200 scans a year, the "
            "net that catches small curable tumors. HCC can be cured by "
            "resection, ablation, or transplant (Milan criteria: one lesion "
            "under 5 cm or up to three under 3 cm) when found early; "
            "pancreatic cancer's marker CA 19-9 tracks disease but screens "
            "no one - it rises in benign biliary obstruction too. Both "
            "cancers share the lesson: anatomy decides detectability, and "
            "detectability decides survival."
        ),
        "how_it_works": (
            "These cancers work as location tragedies. The pancreas sits "
            "retroperitoneal, without a capsule alarm: a head tumor "
            "silently dams the bile duct (painless jaundice - the "
            "Courvoisier pattern of a palpable gallbladder), a body/tail "
            "tumor grows mute until it invades the celiac plexus (back "
            "pain). Resectability is vascular geometry: tumor wrapping the "
            "superior mesenteric artery or vein beyond repair means no "
            "surgery. HCC works as field cancerization: the whole cirrhotic "
            "liver is premalignant soil, so surveillance is calendar "
            "arithmetic - every 6 months, 2 scans per patient per year, 100 "
            "patients x 2 = 200 scans - and the Milan criteria (single "
            "lesion <5 cm, or 3 lesions each <3 cm) ration transplant organs "
            "to curable disease. CA 19-9's flaw is specificity: obstruction "
            "raises it without cancer, so it monitors but never screens. "
            "The demo computes the annual surveillance scan load and states "
            "the Milan cutoffs."
        ),
        "key_points": [
            "Pancreatic cancer hides retroperitoneally: painless jaundice, back pain, weight loss, new diabetes - usually late; 5-year survival ~12%.",
            "Only the resectable minority (clean vessels, no metastases) reaches for cure via Whipple resection.",
            "HCC grows in cirrhotic livers (HBV, HCV, alcohol, MASLD); cirrhotics get ultrasound every 6 months.",
            "Surveillance load: 100 cirrhotics x 2 scans/year = 200 scans; Milan criteria ration transplant to curable disease.",
            "CA 19-9 tracks pancreatic disease but screens no one - benign obstruction raises it too.",
        ],
        "requirements": [
            "The retroperitoneal-hiding mechanism and the painless-jaundice pattern.",
            "Vascular resectability geometry for pancreatic cancer.",
            "The cirrhosis-to-HCC field-cancerization logic and Milan criteria.",
        ],
        "standards": [
            "Survival figure stated as the approximate overall value (~12%).",
            "Milan criteria per standard transplant usage.",
            "CA 19-9 limitation stated per standard clinical teaching.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: these are the fires in the locked rooms - "
            "the pancreas with no windows, the cirrhotic liver as "
            "tinder-dry timber throughout - and the only strategy that works "
            "is scheduled patrols of the timber (HCC surveillance) and "
            "accepting how few locked-room fires get found in time."
        ),
    },
    {
        "key": "emergencies",
        "name": "GI Emergencies: Perforation, Obstruction, and Ischemia",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "GI emergencies are the minutes-to-hours diagnoses: perforation, "
            "obstruction, and mesenteric ischemia. Perforation - a hole "
            "through the gut wall from ulcer, diverticulitis, or trauma - "
            "spills contents into the peritoneum: sudden severe pain, a "
            "board-like rigid abdomen, free air under the diaphragm on "
            "upright imaging, and the clock running toward sepsis. Small "
            "bowel obstruction - usually adhesions from prior surgery, then "
            "hernias - is colicky pain, vomiting, distension, and no gas or "
            "stool; most resolve with nasogastric decompression and fluids, "
            "but strangulation (compromised blood supply) is the surgical "
            "trigger. Mesenteric ischemia is the deadliest: an embolus to "
            "the superior mesenteric artery starves the midgut, and the "
            "classic clue is pain out of proportion to the exam - agony "
            "with a soft abdomen - in an older patient with atrial "
            "fibrillation. Lactate tells the tale: above 2 mmol/L is "
            "concerning, above 4 is severe, and a fall from 5 to 3 mmol/L "
            "is (5-3)/5 = 40 percent clearance - resuscitation working. "
            "All three share one rule: the exam and the lactate decide "
            "faster than any scan, and delay kills bowel."
        ),
        "how_it_works": (
            "GI emergencies work as pressure, blockage, and starvation. "
            "Perforation converts a sterile cavity into a contaminated one: "
            "chemical peritonitis (acid, bile, pancreatic juice) becomes "
            "bacterial peritonitis within hours, and rigidity is the "
            "peritoneum splinting itself. Obstruction is a closed-loop "
            "pressure problem: proximal bowel dilates, vomits, and "
            "third-spaces fluid; strangulation adds vascular compromise, "
            "read as tachycardia, fever, and peritoneal signs. Ischemia is "
            "supply failure: the SMA embolus stops midgut perfusion while "
            "the wall is still intact - hence pain without findings, the "
            "trap for the unwary. Lactate arithmetic tracks resuscitation: "
            "(5 - 3)/5 = 0.40, 40 percent clearance, the number that says "
            "perfusion is returning. The demo computes lactate clearance "
            "and states the three emergency patterns with their deciding "
            "signs."
        ),
        "key_points": [
            "Perforation: sudden severe pain, rigid abdomen, free air under the diaphragm - toward sepsis fast.",
            "Small bowel obstruction: colicky pain, vomiting, distension, obstipation; adhesions first, hernias second.",
            "Mesenteric ischemia: pain out of proportion to exam in AFib patients - the deadliest, the subtlest.",
            "Lactate >2 mmol/L concerning, >4 severe; 5->3 mmol/L = 40% clearance = resuscitation working.",
            "Rule: exam plus lactate decide faster than scans; strangulation signs trigger surgery; delay kills bowel.",
        ],
        "requirements": [
            "The three patterns and each one's deciding sign (rigidity, obstipation, pain-exam mismatch).",
            "The strangulation triggers that convert obstruction to surgery.",
            "Lactate thresholds and clearance arithmetic.",
        ],
        "standards": [
            "Lactate thresholds per standard critical-care usage (>2 concerning, >4 severe).",
            "Adhesions and hernias ordered by typical frequency as obstruction causes.",
            "Atrial fibrillation named as the classic embolic source for mesenteric ischemia.",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: these are the plant's three alarms - the "
            "burst vessel flooding the clean room, the jammed conveyor "
            "building pressure upstream, the power cut starving a whole wing "
            "while the walls still look fine - and every one of them is "
            "answered by the oldest instruments: hands, eyes, and the "
            "blood's own distress signal."
        ),
    },
    {
        "key": "nutrition",
        "name": "Nutritional Support: Enteral and Parenteral Feeding",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Nutritional support feeds patients whose gut cannot do its job: "
            "enteral nutrition (through the gut, via tube) when the gut "
            "works, parenteral nutrition (into the vein, TPN) when it does "
            "not. The rule is absolute - if the gut works, use it: enteral "
            "feeding preserves mucosal integrity, carries fewer infections, "
            "and costs less. Nasogastric tubes serve the short term; "
            "percutaneous endoscopic gastrostomy (PEG) serves the long term. "
            "Needs are computed, not guessed: the Mifflin-St Jeor equation "
            "sets basal metabolic rate - for men, 10 x weight(kg) + 6.25 x "
            "height(cm) - 5 x age + 5. A 70-kg, 175-cm, 40-year-old man: "
            "700 + 1093.75 - 200 + 5 = 1598.75 kcal/day basal, roughly 1600 "
            "- then multiplied by stress and activity factors. Protein runs "
            "1.2 to 2.0 g/kg/day in illness: 70 kg at 1.5 g/kg = 105 grams "
            "daily. Parenteral nutrition - dextrose, amino acids, lipids, "
            "electrolytes, vitamins through a central line - is the "
            "life-support of intestinal failure, short bowel, and prolonged "
            "ileus, with its own hazards: line sepsis, hyperglycemia, liver "
            "injury, and refeeding syndrome when the starved are fed too "
            "fast. Refeeding is started low and advanced slow - the starved "
            "body punishes enthusiasm."
        ),
        "how_it_works": (
            "Nutritional support works as prescribed fueling. The Mifflin-St "
            "Jeor equation estimates the idling engine: for the 70-kg, "
            "175-cm, 40-year-old man, 10x70 = 700, 6.25x175 = 1093.75, "
            "5x40 = 200, so 700 + 1093.75 - 200 + 5 = 1598.75 kcal/day - "
            "about 1600 basal, before stress multipliers (1.2-2.0x for "
            "sepsis, burns, trauma). Protein is dosed by mass: 70 kg x 1.5 "
            "g/kg = 105 g/day in catabolic illness, the nitrogen that "
            "rebuilds. Enteral formulas deliver this through the working "
            "gut; TPN delivers dextrose plus amino acids plus lipids "
            "intravenously when the gut is out of service - glucose infusion "
            "rate watched to avoid hyperglycemia, phosphate/magnesium/potassium "
            "watched to avoid refeeding collapse. The demo computes the "
            "basal rate and the daily protein prescription from the "
            "weight-based rules."
        ),
        "key_points": [
            "Enteral (tube through the gut) whenever the gut works; parenteral (IV/TPN) only when it does not.",
            "Mifflin-St Jeor basal: 10w + 6.25h - 5a + 5 (men); 70 kg/175 cm/40 y = ~1600 kcal/day.",
            "Protein 1.2-2.0 g/kg/day in illness: 70 kg x 1.5 = 105 g/day.",
            "PEG for long-term enteral access; TPN needs central access with dextrose, amino acids, lipids, electrolytes, vitamins.",
            "Hazards: line sepsis, hyperglycemia, liver injury, refeeding syndrome - start low, advance slow.",
        ],
        "requirements": [
            "The if-the-gut-works-use-it rule and why enteral beats parenteral.",
            "The Mifflin-St Jeor equation and the stress/activity multipliers.",
            "Weight-based protein dosing and the refeeding-syndrome caution.",
        ],
        "standards": [
            "Equation per the Mifflin-St Jeor standard with the male constant (+5).",
            "Protein range per standard critical-care nutrition guidance (1.2-2.0 g/kg/day).",
            "Access choices per standard practice (NG short-term, PEG long-term, central line for TPN).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: nutritional support is the works on "
            "auxiliary fueling - run the normal loading dock if it still "
            "takes deliveries, otherwise pipe fuel straight to the boilers - "
            "and the fueling order is always computed from the engine's "
            "spec plate, never guessed."
        ),
    },
    {
        "key": "pediatric",
        "name": "Pediatric Gastroenterology",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pediatric gastroenterology is the specialty scaled to growing "
            "bodies: congenital anomalies, growth failure, and the "
            "childhood faces of adult diseases. Pyloric stenosis - "
            "hypertrophy of the pyloric muscle in young infants, four boys "
            "to every girl, about 1 to 3 per 1000 live births - presents at "
            "2 to 6 weeks with progressive projectile non-bilious vomiting "
            "and the olive-shaped mass on exam; Ramstedt pyloromyotomy cures "
            "it. Hirschsprung disease - missing ganglion cells in the "
            "distal colon, about 1 in 5000 births - presents with delayed "
            "passage of meconium beyond 48 hours and downstream obstruction; "
            "in 5000 newborns, expect about 1 case, versus 5 to 15 pyloric "
            "stenoses in 5000 births at 1-3 per 1000. Intussusception "
            "telescopes bowel into bowel (currant-jelly stool, episodic "
            "pain); air-contrast enema both diagnoses and treats. "
            "Celiac disease, inflammatory bowel disease, and eosinophilic "
            "esophagitis all debut in childhood with growth failure as the "
            "shared alarm - a falling growth curve is the pediatric GI "
            "vital sign. Biliary atresia jaundices the newborn past two "
            "weeks and needs the Kasai procedure before 60 days. Dosing, "
            "endoscopy, and counseling all scale to the child; the diseases "
            "are the specialty's, the patients are new."
        ),
        "how_it_works": (
            "Pediatric GI works as the adult specialty re-tuned for "
            "development. The newborn gut is tested by its first jobs: pass "
            "meconium within 48 hours (Hirschsprung fails this), tolerate "
            "feeds without projectile vomiting at 2-6 weeks (pyloric "
            "stenosis fails this), clear jaundice by two weeks (biliary "
            "atresia fails this). Incidence arithmetic sets the differential: "
            "in 5000 births, Hirschsprung at 1/5000 gives 5000/5000 = 1 "
            "expected case; pyloric stenosis at 2/1000 gives 5000 x 0.002 = "
            "10 expected cases - an order of magnitude more common, which is "
            "why the vomiting infant's workup runs pylorus-first. Growth is "
            "the longitudinal vital sign: crossing two percentile lines "
            "downward triggers the malabsorption and inflammation workup "
            "(celiac serology, fecal calprotectin, endoscopy) regardless of "
            "which disease is suspected. The demo computes the expected case "
            "counts per 5000 births for both conditions."
        ),
        "key_points": [
            "Pyloric stenosis: 1-3/1000 births, 4:1 male, projectile vomiting at 2-6 weeks; pyloromyotomy cures.",
            "Hirschsprung disease: 1/5000 births, aganglionic distal colon, delayed meconium >48 hours.",
            "Per 5000 births: ~1 Hirschsprung vs ~10 pyloric stenoses - vomiting workup runs pylorus-first.",
            "Intussusception: telescoped bowel, currant-jelly stool; air enema diagnoses and treats.",
            "Growth failure is the shared pediatric GI alarm; biliary atresia needs Kasai before 60 days.",
        ],
        "requirements": [
            "The newborn-gut first-jobs sequence (meconium, feeds, jaundice clearance).",
            "Incidence arithmetic per birth cohort for the key congenital lesions.",
            "Growth-curve monitoring as the longitudinal vital sign.",
        ],
        "standards": [
            "Incidence figures per standard pediatric epidemiologic usage.",
            "Procedure names per standard usage (Ramstedt pyloromyotomy, Kasai portoenterostomy).",
            "Meconium and Kasai timing thresholds per standard teaching (>48 h, <60 days).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: pediatric GI is the new plant's "
            "shakedown cruise - every station tested by its first real job, "
            "the birth defects as factory faults caught on the shake-down "
            "run, and the growth curve as the long-term output gauge that "
            "never lies."
        ),
    },
    {
        "key": "future",
        "name": "The Future of Gastroenterology: AI Endoscopy and Engineered Microbiomes",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The future of gastroenterology is being written by two "
            "revolutions: machine eyes and engineered ecosystems. "
            "Artificial-intelligence polyp detection - computer-aided "
            "detection (CADe) highlighting adenomas in real time during "
            "colonoscopy - raises the adenoma detection rate by roughly half "
            "again: a 25 percent baseline ADR becomes 25 x 1.5 = 37.5 "
            "percent, turning average endoscopists into high detectors and "
            "narrowing the miss-rate gap that lets interval cancers happen. "
            "Computer-aided characterization (CADx) predicts polyp histology "
            "optically, enabling resect-and-discard strategies. On the "
            "ecosystem side, fecal microbiota transplant's ~90 percent cure "
            "rate in recurrent Clostridioides difficile proved the "
            "microbiome is a druggable organ; next come defined bacterial "
            "consortia, engineered probiotics, and phage therapy - "
            "precision ecology instead of whole-stool transplant. Capsule "
            "endoscopy already images the small bowel no scope can reach; "
            "AI-read capsules and magnetically steered capsules extend the "
            "reach further. In 100 recurrent C. difficile patients, "
            "transplant cures about 90 where vancomycin cures about 30 - a "
            "60-patient gap that is the entire case for the ecosystem "
            "revolution. The specialty's trajectory is clear: see more, miss "
            "less, and treat the ecosystem as deliberately as the organ."
        ),
        "how_it_works": (
            "The future works as augmented inspection plus programmed "
            "ecology. CADe systems run convolutional networks over the "
            "colonoscopy video feed, boxing suspected polyps in real time; "
            "the ADR arithmetic is multiplicative - 25 percent baseline "
            "times a 1.5x relative lift gives 37.5 percent assisted ADR, "
            "which compounds over a career into hundreds of additionally "
            "intercepted adenomas. CADx adds optical biopsy: predicting "
            "adenomatous vs hyperplastic histology from the polyp's surface "
            "pattern with high negative predictive value for diminutive "
            "rectosigmoid polyps. The microbiome arm works by "
            "colonization-resistance restoration at scale: recurrent C. "
            "difficile cure 90 of 100 with transplant vs 30 of 100 with "
            "vancomycin - the 60-patient gap is the effect size that "
            "justifies defined consortia and engineered strains as the "
            "refined successors. The demo computes the AI-assisted ADR and "
            "the transplant-vs-antibiotic cure gap."
        ),
        "key_points": [
            "CADe (AI polyp detection) lifts ADR ~1.5x: 25% baseline -> 37.5% assisted - interval cancers fall.",
            "CADx predicts polyp histology optically, enabling resect-and-discard for diminutive polyps.",
            "FMT cures ~90% of recurrent C. difficile vs ~30% for vancomycin - a 60-patient gap per 100.",
            "Next: defined bacterial consortia, engineered probiotics, phage therapy - precision ecology.",
            "Capsule endoscopy + AI reading extends inspection to the un-scopeable small bowel.",
        ],
        "requirements": [
            "The CADe real-time detection loop and the multiplicative ADR arithmetic.",
            "The FMT effect size and why it proves the microbiome is druggable.",
            "The consortia/phage successors and what 'precision ecology' means.",
        ],
        "standards": [
            "ADR lift stated as the approximate relative figure from CADe trials (~1.5x).",
            "Cure rates stated as the recurrent-disease comparison (~90% vs ~30%).",
            "Technology names per standard usage (CADe, CADx, capsule endoscopy).",
        ],
        "citations": [CIT_SLEIS, CIT_YAMADA, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the future is the works with machine "
            "eyes on every inspector and programmed crews restocking the "
            "resident workforce - see every fault, miss nothing, and manage "
            "the living ecosystem with the same deliberate work orders as "
            "the steel."
        ),
    },
]
