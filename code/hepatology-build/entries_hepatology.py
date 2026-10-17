#!/usr/bin/env python3
"""Entries for the Hepatology field databases (field #39, taxonomy order).

Verified 2026-10-17: NO database covers hepatology as a clinical specialty
(liver, biliary tract, and pancreas - viral/autoimmune hepatitis, cirrhosis,
portal hypertension, NAFLD/MASLD, alcoholic liver disease, cholestasis,
liver failure, transplantation, liver function testing). Clinical-specialty
framing, liver-focused, distinct from gastroenterology (general GI specialty).

Manifest search (2,378 databases): zero 'hepatolog*' slugs/names; no
db/hepatolog* dirs. Whole-system exact-title sweep over the manifest PLUS
all 777 shard index 't' keys: zero collisions for all 34 planned titles x2
editions (68 variants). Near-neighbors confirmed different disciplines:
'gastroenterology' covers the general GI tract (its liver/biliary/pancreas
records are survey-level: "Viral Hepatitis", "Fatty Liver Disease: NAFLD
and MASLD", "Chronic Liver Disease and Cirrhosis", "Gallstone Disease and
Cholecystitis", "Acute Pancreatitis", "Biliary Obstruction and Jaundice",
"GI Cancers: Pancreatic and Hepatocellular" - all exact-titles avoided
here); 'endocrinology' covers only the hormone system; diabetes coverage is
fragmented across general health databases. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  hepatology                 - The Hepatology Database
                               (public-harvest: real, fact-checked clinical
                               hepatology; standard references Feldman et al.
                               "Sleisenger and Fordtran's Gastrointestinal and
                               Liver Disease" 11th ed 2021 (liver sections);
                               Schiff et al. "Schiff's Diseases of the Liver"
                               12th ed 2018; Jameson et al. "Harrison's
                               Principles of Internal Medicine" 21st ed 2022;
                               AASLD practice guidance: chronic hepatitis B
                               2018, hepatitis C 2018, autoimmune hepatitis
                               2019, primary biliary cholangitis 2018,
                               NAFLD/MASLD 2023, portal hypertensive bleeding
                               2016, ascites/SBP/HRS 2021, HCC 2018; EASL and
                               ACG drug-induced liver injury 2021; acute
                               liver failure reviews; MELD and Child-Pugh
                               original papers)
  hepatology-signature       - The Hepatology Signature Database
                               (his original Signature interpretation of the
                               liver as the body's chemical refinery and
                               filter works: the hepatocyte as the process
                               unit, bile as the solvent line, the biliary
                               tree as the outflow plumbing, portal blood as
                               the raw feedstock line, fibrosis as scale
                               building up in the filter, cirrhosis as the
                               clogged refinery, transplantation as the full
                               refinery rebuild; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-HEP- (public) and JAH-HEPS- (signature), both verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of the "
            "liver as the body's chemical refinery and filter works: the "
            "hepatocyte as the process unit, bile as the solvent line, the "
            "biliary tree as the outflow plumbing, portal blood as the raw "
            "feedstock line, fibrosis as scale building up in the filter, "
            "cirrhosis as the clogged refinery, transplantation as the full "
            "refinery rebuild. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_SLEIS = ("Feldman M, Friedman LS, Brandt LJ, eds. Sleisenger and Fordtran's "
             "Gastrointestinal and Liver Disease: Pathophysiology, Diagnosis, "
             "Management. 11th ed. Elsevier; 2021.")
CIT_SCHIFF = ("Schiff ER, Maddrey WC, Reddy KR, eds. Schiff's Diseases of the "
              "Liver. 12th ed. Wiley-Blackwell; 2018.")
CIT_HARRISON = ("Jameson JL, Fauci AS, Kasper DL, Hauser SL, Longo DL, "
                "Loscalzo J, eds. Harrison's Principles of Internal Medicine. "
                "21st ed. McGraw Hill; 2022.")
CIT_AASLD_HBV = ("Terrault NA, Lok ASF, McMahon BJ, et al. Update on Prevention, "
                 "Diagnosis, and Treatment of Chronic Hepatitis B: AASLD 2018 "
                 "Hepatitis B Guidance. Hepatology. 2018;67(4):1560-1599.")
CIT_AASLD_HCV = ("Chung RT, Ghany MG, Kim AY, et al. Hepatitis C Guidance 2018 "
                 "Update: AASLD-IDSA Recommendations for Testing, Managing, and "
                 "Treating Hepatitis C Virus Infection. Clin Gastroenterol "
                 "Hepatol. 2018;16(9):1336-1358.")
CIT_AASLD_MASLD = ("Rinella ME, Neuschwander-Tetri BA, Siddiqui MS, et al. AASLD "
                   "Practice Guidance on the clinical assessment and management "
                   "of nonalcoholic fatty liver disease. Hepatology. "
                   "2023;77(5):1797-1835.")
CIT_MASLD_NOMEN = ("Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety "
                   "Delphi consensus statement on new fatty liver disease "
                   "nomenclature. J Hepatol. 2023;79(6):1542-1556.")
CIT_AIH = ("Mack CL, Adams D, Assis DN, et al. Diagnosis and Management of "
           "Autoimmune Hepatitis in Adults and Children: 2019 Practice Guidance "
           "and Guidelines From the American Association for the Study of Liver "
           "Diseases. Hepatology. 2020;72(2):671-722.")
CIT_PBC = ("Lindor KD, Bowlus CL, Boyer J, Levy C, Mayo M. Primary Biliary "
           "Cholangitis: 2018 Practice Guidance from the American Association "
           "for the Study of Liver Diseases. Hepatology. 2019;69(1):394-419.")
CIT_DILI = ("Chalasani NP, Maddur H, Russo MW, Wong RJ, Reddy KR. ACG Clinical "
            "Guideline: Diagnosis and Management of Idiosyncratic Drug-Induced "
            "Liver Injury. Am J Gastroenterol. 2021;116(5):878-898.")
CIT_ALF = ("Stravitz RT, Lee WM. Acute liver failure. Lancet. "
           "2019;394(10201):869-881.")
CIT_KINGS = ("O'Grady JG, Alexander GJ, Hayllar KM, Williams R. Early indicators "
             "of prognosis in fulminant hepatic failure. Gastroenterology. "
             "1989;97(2):439-445.")
CIT_MELD = ("Wiesner R, Edwards E, Freeman R, et al. Model for end-stage liver "
            "disease (MELD) and allocation of donor livers. Gastroenterology. "
            "2003;124(1):91-96.")
CIT_CHILDPUGH = ("Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R. "
                 "Transection of the oesophagus for bleeding oesophageal "
                 "varices. Br J Surg. 1973;60(8):646-649.")
CIT_HCC = ("Heimbach JK, Kulik LM, Finn RS, et al. AASLD guidelines for the "
           "treatment of hepatocellular carcinoma. Hepatology. "
           "2018;67(1):358-380.")
CIT_PORTAL = ("Garcia-Tsao G, Abraldes JG, Berzigotti A, Bosch J. Portal "
              "hypertensive bleeding in cirrhosis: Risk stratification, "
              "diagnosis, and management: 2016 practice guidance by the American "
              "Association for the study of liver diseases. Hepatology. "
              "2017;65(1):310-335.")
CIT_ASCITES = ("Biggins SW, Angeli P, Garcia-Tsao G, et al. Diagnosis, "
               "Evaluation, and Management of Ascites, Spontaneous Bacterial "
               "Peritonitis and Hepatorenal Syndrome: 2021 Practice Guidance by "
               "the American Association for the Study of Liver Diseases. "
               "Hepatology. 2021;74(2):1014-1148.")
CIT_ACG_PANC = ("Tenner S, Baillie J, DeWitt J, Vege SS. American College of "
                "Gastroenterology Guideline: Management of Acute Pancreatitis. "
                "Am J Gastroenterol. 2013;108(9):1400-1415.")
CIT_TRANSPLANT = ("Martin P, DiMartini A, Feng S, Brown R Jr, Fallon M. "
                  "Evaluation for liver transplantation in adults: 2013 practice "
                  "guideline by the American Association for the Study of Liver "
                  "Diseases and the American Society of Transplantation. "
                  "Hepatology. 2014;59(3):1144-1165.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Hepatology: The Clinical Specialty of the Liver, Biliary Tract, and Pancreas",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hepatology is the clinical medical specialty devoted to the liver, "
            "the biliary tract, and the pancreas - the organs of the upper "
            "abdomen that refine the blood, make and move bile, and run the "
            "body's digestive chemistry. The name comes from the Greek hepar "
            "(liver) and logos (study). The hepatologist is the physician who "
            "reads the liver: diagnosing hepatitis, fatty liver, alcohol "
            "injury, drug injury, autoimmune and cholestatic disease, cirrhosis "
            "and its complications - variceal bleeding, ascites, encephalopathy "
            ", kidney failure - liver cancers, biliary obstruction, gallstone "
            "disease, and pancreatitis and pancreatic cancer, and managing them "
            "with medicines, endoscopic procedures like ERCP, and referral for "
            "liver transplantation when the organ cannot be saved. The liver is "
            "the largest internal organ, about 1.4 to 1.6 kilograms in the "
            "adult, receiving roughly a quarter of the resting cardiac output "
            "through the portal vein and hepatic artery, and making 500 to 600 "
            "milliliters of bile a day. This record frames the discipline and "
            "the ladder of records that follows."
        ),
        "how_it_works": (
            "Hepatology works on the refinery model of the liver. Raw "
            "feedstock - nutrient-rich, toxin-laden blood from the gut - "
            "arrives through the portal vein, about 75 percent of the organ's "
            "blood supply, with oxygenated blood topping it up through the "
            "hepatic artery. Inside, hepatocytes - the process units - run "
            "hundreds of reactions: building proteins like albumin and "
            "clotting factors, storing glycogen, making cholesterol and bile "
            "acids, clearing ammonia into urea, and detoxifying drugs and "
            "alcohol. Finished bile drains through the canaliculi into the "
            "biliary tree, is stored and concentrated in the gallbladder, and "
            "is released into the duodenum to dissolve fats. Cleaned blood "
            "leaves through the hepatic veins to the heart. The demo works the "
            "refinery arithmetic: the organ's share of body mass and cardiac "
            "output, and the daily bile volume projected over a year."
        ),
        "key_points": [
            "Hepatology = the clinical specialty of the liver, biliary tract, and pancreas: hepatitis, cirrhosis, portal hypertension, cholestasis, liver failure, transplantation, pancreatic disease.",
            "The liver is about 1.4 to 1.6 kg and receives roughly 25 percent of resting cardiac output via the portal vein and hepatic artery.",
            "The hepatologist manages the full complication set of cirrhosis: variceal bleeding, ascites, encephalopathy, hepatorenal syndrome.",
            "The specialty is both cognitive and procedural: antiviral therapy, immunosuppression, ERCP, paracentesis, and transplant referral all belong to it.",
            "Distinct from gastroenterology (the whole digestive tract): hepatology is the liver-centered specialty, the refinery's own medicine.",
        ],
        "requirements": [
            "The territory map: liver, gallbladder, bile ducts, pancreas, portal venous system.",
            "The refinery picture: portal feedstock in, bile and cleaned blood out.",
            "Scale literacy: organ mass, blood-flow share, daily bile volume.",
        ],
        "standards": [
            "Organ names and spellings follow standard clinical usage (hepatocyte, cholangiocyte, Kupffer cell).",
            "Quantities stated as adult averages with 'about' qualifiers since they vary by body size.",
            "Disease framing is diagnostic and management-oriented, matching the clinical-specialty scope.",
        ],
        "citations": [CIT_SCHIFF, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the liver is the body's chemical refinery "
            "and filter works - a 1.5-kilogram processing plant that takes the "
            "gut's raw, dirty blood and turns out clean blood, bile solvent, "
            "and protein product. The hepatologist is the refinery's chief "
            "engineer: reading the gauges (the LFT panel), clearing blockages "
            "in the outflow plumbing (the bile ducts), rebuilding clogged "
            "filters (cirrhosis), and ordering a full plant replacement "
            "(transplantation) when the works are beyond repair."
        ),
    },
    {
        "key": "liver_anatomy",
        "name": "The Liver: Lobes, Segments, and Vascular Architecture",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The liver sits under the right diaphragm, the largest internal "
            "organ at roughly 1.4 to 1.6 kilograms, and its anatomy is the map "
            "every hepatologist, surgeon, and radiologist navigates by. The "
            "old surface anatomy - right lobe, left lobe, quadrate, caudate - "
            "has been replaced for clinical work by the Couinaud system: eight "
            "functionally independent segments, numbered 1 through 8, each "
            "with its own portal inflow, arterial supply, and biliary "
            "drainage, so a surgeon can resect segments and leave the rest "
            "working. The caudate lobe is segment 1, with its own direct "
            "venous drainage to the vena cava. Blood arrives through the "
            "portal vein (about three quarters) and the hepatic artery (about "
            "one quarter), mixes in the sinusoids - the leaky capillaries "
            "lined by Kupffer cells, the liver's resident macrophages - and "
            "leaves through the three hepatic veins into the inferior vena "
            "cava. This record lays out the segments, the vessels, and the "
            "microanatomy of the lobule."
        ),
        "how_it_works": (
            "The segment map works like a city plan: the portal triad - portal "
            "vein branch, hepatic artery branch, bile duct - is the utility "
            "corridor at each segment's border, and blood flows from the triad "
            "inward through the sinusoids to the central vein at the lobule's "
            "center, while bile flows the opposite way, outward from the "
            "hepatocyte into the canaliculi toward the triad. That counterflow "
            "is why zone 3, around the central vein, is the first to suffer "
            "when oxygen runs short - ischemic and congestive injury strike "
            "there first. The demo works the segment arithmetic: the eight "
            "Couinaud segments as shares of total liver volume, showing how "
            "the right lobe (segments 5 through 8) carries roughly two thirds "
            "of the organ."
        ),
        "key_points": [
            "Couinaud segments 1-8 are the working map: each segment has independent portal, arterial, and biliary supply.",
            "The portal vein supplies about 75 percent of hepatic blood flow; the hepatic artery about 25 percent.",
            "Blood flows triad-to-central-vein while bile flows the opposite way - counterflow anatomy.",
            "Zone 3 (centrilobular) is the most oxygen-vulnerable: ischemic injury strikes there first.",
            "The caudate lobe (segment 1) drains directly into the vena cava, which is why it hypertrophies in Budd-Chiari syndrome.",
        ],
        "requirements": [
            "The eight-segment numbering and the caudate as segment 1.",
            "The portal triad contents: portal vein, hepatic artery, bile duct.",
            "The sinusoid path: triad to central vein to hepatic veins to vena cava.",
        ],
        "standards": [
            "Segment numbering follows Couinaud; lobe names follow standard surface anatomy.",
            "Blood-flow shares stated as approximate fractions of total hepatic flow.",
            "Microanatomy terms (sinusoid, space of Disse, Kupffer cell) follow standard histology usage.",
        ],
        "citations": [CIT_SCHIFF, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the liver is a refinery built as eight "
            "independent process modules - the Couinaud segments - each with "
            "its own feedstock line, utility corridor, and product drain, so "
            "modules can be shut down and removed while the plant keeps "
            "running. The portal triad is the utility chase at every module "
            "boundary; the sinusoid is the packed reaction bed where feedstock "
            "meets the catalyst; zone 3 is the far end of the bed, first to "
            "starve when the pumps falter."
        ),
    },
    {
        "key": "biliary_tree",
        "name": "The Biliary Tree and Pancreatic Ducts: Plumbing of the Upper Abdomen",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Bile made by the hepatocytes must travel: out of the liver, into "
            "storage, and down to the gut - and the biliary tree is that "
            "plumbing. Canaliculi drain into the canals of Hering, then into "
            "interlobular ducts, the right and left hepatic ducts, the common "
            "hepatic duct, and - after the cystic duct joins from the "
            "gallbladder - the common bile duct, which runs about 8 to 10 "
            "centimeters to the ampulla of Vater in the duodenum, where it "
            "meets the pancreatic duct in most people. The gallbladder stores "
            "and concentrates bile between meals, contracting when "
            "cholecystokinin signals fat in the duodenum. The sphincter of Oddi "
            "guards the ampulla. Normal common bile duct diameter is about 6 "
            "millimeters or less; a dilated duct on imaging is the first clue "
            "to obstruction. This record maps the ducts, the valves, and the "
            "pressures that move bile."
        ),
        "how_it_works": (
            "Bile moves by secretion pressure and gravity, not by a pump: "
            "hepatocytes secrete bile acids and water into the canaliculi, "
            "building the pressure that pushes bile downstream, while the "
            "sphincter of Oddi stays closed between meals so bile backs up the "
            "cystic duct into the gallbladder, where water is absorbed and bile "
            "is concentrated up to tenfold. After a fatty meal, "
            "cholecystokinin contracts the gallbladder and relaxes the "
            "sphincter, delivering a bolus of concentrated bile to the "
            "duodenum. The demo works the plumbing numbers: normal duct "
            "diameter against dilated, and the daily bile volume the system "
            "must move."
        ),
        "key_points": [
            "The biliary tree: canaliculi to hepatic ducts to common hepatic duct to common bile duct to the ampulla of Vater.",
            "The gallbladder concentrates bile up to tenfold between meals and empties on cholecystokinin signaling.",
            "The sphincter of Oddi guards the ampulla; the pancreatic duct usually joins the bile duct there.",
            "Normal common bile duct diameter is about 6 mm or less - dilation flags obstruction.",
            "Bile flows by secretion pressure and gravity, with no dedicated pump in the system.",
        ],
        "requirements": [
            "The duct sequence in order from hepatocyte to duodenum.",
            "The gallbladder's store-and-concentrate role and its hormonal trigger.",
            "The normal caliber of the common bile duct and what dilation means.",
        ],
        "standards": [
            "Duct names follow standard clinical anatomy (common hepatic, cystic, common bile duct, ampulla of Vater).",
            "Diameters stated as approximate adult norms with qualifiers for age and post-cholecystectomy state.",
            "Physiology described in mechanistic terms, not as a pump model.",
        ],
        "citations": [CIT_SCHIFF, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the biliary tree is the refinery's outflow "
            "plumbing - product lines running from every process module to a "
            "central main, with a surge tank (the gallbladder) that stores and "
            "concentrates the solvent between batches, and a single guarded "
            "valve (the sphincter of Oddi) metering it into the works below. A "
            "dilated main means a blockage downstream; the whole of biliary "
            "medicine is reading the pipe gauges."
        ),
    },
    {
        "key": "liver_physiology",
        "name": "Liver Physiology: The Body's Chemical Refinery",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The liver runs more chemistry than any other organ - synthesis, "
            "storage, transformation, and clearance, all at once. It builds "
            "albumin, clotting factors, and transport proteins; it stores "
            "glycogen, iron, copper, and vitamins A, D, B12; it converts "
            "ammonia - the toxic waste of protein metabolism - into urea "
            "through the urea cycle; it makes bile acids from cholesterol and "
            "cholesterol from scratch; and it detoxifies drugs, alcohol, and "
            "environmental chemicals through phase 1 oxidation (the cytochrome "
            "P450 family) and phase 2 conjugation, making fat-soluble toxins "
            "water-soluble enough for the kidney or the bile to excrete. "
            "Gluconeogenesis keeps blood sugar up between meals; ketogenesis "
            "feeds the brain in starvation. Nearly every blood test the "
            "hepatologist reads - albumin, INR, glucose, cholesterol - is a "
            "gauge on one of these lines. This record tours the refinery's "
            "process units."
        ),
        "how_it_works": (
            "The refinery works on first-pass logic: everything absorbed from "
            "the gut travels the portal vein straight to the liver before "
            "reaching the rest of the body, so the organ sees every meal, "
            "every drug, every swallowed toxin at full concentration first. "
            "Hepatocytes take up the load, run it through enzyme cascades, and "
            "release finished products - glucose, albumin, clotting factors, "
            "urea, bile - back into the blood or the bile. When the works "
            "fail, the gauges move in pattern: albumin falls and INR rises as "
            "synthesis fails, ammonia climbs as the urea cycle stalls, glucose "
            "drops as gluconeogenesis quits. The demo works the flow "
            "arithmetic: cardiac output through the portal vein and hepatic "
            "artery, and what share of the circulation the refinery processes "
            "each minute."
        ),
        "key_points": [
            "First-pass logic: portal blood brings every meal, drug, and toxin to the liver before the rest of the body.",
            "The liver synthesizes albumin and clotting factors, stores glycogen and vitamins, and runs the urea cycle.",
            "Phase 1 (cytochrome P450) oxidation plus phase 2 conjugation clear drugs and toxins.",
            "Gluconeogenesis and ketogenesis keep the brain fueled between meals and in starvation.",
            "Failed synthesis reads out as low albumin, high INR, high ammonia, low glucose - the refinery's alarm panel.",
        ],
        "requirements": [
            "The four process families: synthesis, storage, transformation, clearance.",
            "First-pass anatomy: why the portal vein makes the liver the gatekeeper.",
            "The urea cycle's job: ammonia to urea, and what rises when it stalls.",
        ],
        "standards": [
            "Enzyme family names follow standard usage (cytochrome P450, phase 1/phase 2).",
            "Metabolic claims are qualitative; quantitative rates carry 'about' qualifiers.",
            "Failure patterns are described as typical, not universal.",
        ],
        "citations": [CIT_SCHIFF, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the liver is a continuous-flow chemical "
            "plant with four process families - the synthesis shop (albumin, "
            "clotting factors), the warehouse (glycogen, vitamins, metals), "
            "the cracking unit (ammonia to urea, cholesterol to bile acids), "
            "and the waste-treatment train (phase 1 oxidation, phase 2 "
            "conjugation). First-pass anatomy is the plant's intake design: "
            "every raw feedstock passes the gates before it can reach the "
            "town downstream."
        ),
    },
    {
        "key": "bilirubin",
        "name": "Bilirubin Metabolism: From Red Cells to Bile",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Bilirubin is the yellow pigment of jaundice, and its journey from "
            "dying red blood cells to the stool is the single most-read story "
            "in hepatology. Old red cells are dismantled by macrophages, "
            "mostly in the spleen; their heme becomes unconjugated (indirect) "
            "bilirubin, which rides albumin to the liver. Hepatocytes take it "
            "up, conjugate it with glucuronic acid via UGT1A1 - making it "
            "water-soluble direct bilirubin - and secrete it into bile. Gut "
            "bacteria convert it to urobilinogen: most leaves in the stool "
            "(its brown color), some is reabsorbed in the enterohepatic "
            "circulation, and a little spills into urine. Total bilirubin "
            "above about 1.2 milligrams per deciliter is abnormal; above about "
            "2.5 to 3, jaundice becomes visible, first in the sclera. The "
            "fraction matters: mostly unconjugated points to overproduction or "
            "bad conjugation (hemolysis, Gilbert syndrome); mostly conjugated "
            "points to cholestasis or hepatocellular injury. One milligram per "
            "deciliter equals 17.1 micromoles per liter - the conversion every "
            "hepatologist does in their head."
        ),
        "how_it_works": (
            "The pathway works as a four-station line: production "
            "(macrophages crack heme to unconjugated bilirubin), delivery "
            "(albumin carries it to the liver), conjugation (UGT1A1 adds "
            "glucuronic acid), and excretion (bile carries conjugated pigment "
            "to the gut). A jam at station one - hemolysis - floods the line "
            "with unconjugated pigment the liver cannot keep up with. A jam "
            "at station three - UGT1A1 deficiency in Gilbert or Crigler-Najjar "
            "- leaves conjugation behind production. A jam at station four - "
            "cholestasis - backs conjugated bilirubin up into the blood, where "
            "it spills into urine and turns it dark while stools go pale. The "
            "demo works the unit conversion at the heart of the panel: "
            "milligrams per deciliter to micromoles per liter and back."
        ),
        "key_points": [
            "Bilirubin path: heme to unconjugated (albumin-bound) to conjugated (UGT1A1) to bile to stool.",
            "Unconjugated fraction high: hemolysis or conjugation defects; conjugated high: cholestasis or liver injury.",
            "Visible jaundice appears around 2.5 to 3 mg/dL, first in the sclera.",
            "1 mg/dL = 17.1 micromol/L - the core conversion of the liver panel.",
            "Dark urine with pale stools is the signature of conjugated hyperbilirubinemia backing up into blood.",
        ],
        "requirements": [
            "The four stations: production, delivery, conjugation, excretion.",
            "UGT1A1's role and the Gilbert/Crigler-Najjar connection.",
            "Reading the fraction: which pattern points where.",
        ],
        "standards": [
            "Pigment names follow standard usage (unconjugated/indirect, conjugated/direct, urobilinogen).",
            "Thresholds stated as approximate clinical cutoffs.",
            "Unit conversion uses the standard factor 17.1.",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: bilirubin is the refinery's tracer dye - a "
            "yellow tag on the waste stream that lets the engineer see exactly "
            "which station jammed. Flooded with untagged waste upstream, the "
            "plant cannot keep up (hemolysis); the tagging machine itself "
            "broken (conjugation defects); the outflow pipe blocked so tagged "
            "waste backs up into the feed lines (cholestasis). Read the tag, "
            "find the jam."
        ),
    },
    {
        "key": "lft",
        "name": "Liver Function Testing: Reading the LFT Panel",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The liver panel - ALT, AST, alkaline phosphatase, bilirubin, "
            "albumin, and the INR/PT - is the most-read blood panel in "
            "hepatology, and reading it is pattern recognition, not number "
            "worship. ALT and AST are hepatocellular enzymes: ALT lives mostly "
            "in liver, AST also in muscle and red cells, so ALT is the more "
            "liver-specific of the two, and values in the thousands mean "
            "hepatocyte death on a large scale - viral hepatitis, ischemia, "
            "drug injury, autoimmune flare. Alkaline phosphatase and "
            "GGT/bilirubin are the cholestatic enzymes: a high alkaline "
            "phosphatase with high bilirubin means blocked or inflamed bile "
            "flow. Albumin and INR read synthetic function - slow to fall, "
            "slow to recover, the true gauges of liver failure. The R ratio - "
            "(ALT divided by its upper limit) divided by (alkaline phosphatase "
            "divided by its upper limit) - sorts the pattern: above 5 is "
            "hepatocellular, below 2 is cholestatic, between is mixed. This "
            "record teaches the panel as an instrument panel."
        ),
        "how_it_works": (
            "The panel works as six gauges on three systems. The injury "
            "gauges (ALT, AST) spike when hepatocytes break open - the higher "
            "and faster, the more acute the death. The plumbing gauges "
            "(alkaline phosphatase, GGT, bilirubin) rise when bile cannot flow "
            "- obstruction, cholestasis, infiltrative disease. The factory "
            "gauges (albumin, INR) fall when the liver stops making product - "
            "the last to move and the most ominous. The R ratio compresses "
            "injury-versus-plumbing into one number so the pattern, not the "
            "raw heights, drives the workup: a towering ALT with a normal "
            "alkaline phosphatase is a different disease than the reverse. The "
            "demo computes the R ratio on a worked case and classifies the "
            "pattern."
        ),
        "key_points": [
            "ALT is the most liver-specific injury enzyme; values in the thousands mean large-scale hepatocyte death.",
            "Alkaline phosphatase plus bilirubin is the cholestatic pattern: blocked or inflamed bile flow.",
            "Albumin and INR are synthetic-function gauges - slow to move, ominous when they do.",
            "R ratio = (ALT/ULN)/(ALP/ULN): >5 hepatocellular, <2 cholestatic, 2-5 mixed.",
            "Read the pattern first, the absolute numbers second.",
        ],
        "requirements": [
            "What each of the six panel components measures.",
            "The R ratio formula and its three pattern bands.",
            "Why synthetic markers lag injury markers in acute failure.",
        ],
        "standards": [
            "Enzyme names and abbreviations follow standard laboratory usage.",
            "Pattern bands use the standard R-ratio cutoffs.",
            "ULN-relative reading is the standard, not absolute values alone.",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: the LFT panel is the refinery's gauge "
            "board - six dials on three systems. The rupture dials (ALT, AST) "
            "spike when process units burst; the plumbing dials (alkaline "
            "phosphatase, bilirubin) climb when the outflow lines clog; the "
            "production dials (albumin, INR) sag when the synthesis shop goes "
            "dark. The R ratio is the master selector switch: rupture pattern "
            "or plumbing pattern - which crew gets called."
        ),
    },
    {
        "key": "encounter",
        "name": "The Hepatology Clinical Encounter: History, Examination, and the Jaundiced Patient",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hepatology visit is a detective interview built around "
            "exposures and time courses. The history hunts alcohol quantity "
            "and duration, every drug and supplement (drug-induced liver "
            "injury hides in the medicine cabinet), viral hepatitis risks "
            "(transfusions, injections, sexual and household exposures, "
            "travel), autoimmune clues, family liver disease, and the tempo of "
            "the illness - hours (ischemia, toxin), weeks (acute viral), "
            "years (fatty liver, alcohol, chronic viral). The examination "
            "reads the stigmata of chronic liver disease: spider angiomata, "
            "palmar erythema, gynecomastia, caput medusae, ascites, "
            "splenomegaly, asterixis, fetor hepaticus - each a physical "
            "signature of portal hypertension or failed synthesis. Jaundice "
            "itself is graded in the sclera first. The workup then follows "
            "the bilirubin fraction: unconjugated points to hemolysis or "
            "Gilbert; conjugated to cholestasis or hepatocellular disease - "
            "and imaging (ultrasound first) separates dilated-duct plumbing "
            "problems from parenchymal ones. This record teaches the encounter "
            "as a disciplined search pattern."
        ),
        "how_it_works": (
            "The encounter works as a decision tree with three branches. "
            "Branch one is exposure: what entered the patient - alcohol, "
            "drugs, viruses, autoimmunity - and over what time course. Branch "
            "two is the body: the stigmata are read as binary features, each "
            "one a vote for chronicity and portal hypertension. Branch three "
            "is the fraction: the direct-to-total bilirubin ratio splits the "
            "jaundiced patient into hemolytic/unconjugated versus cholestatic "
            "workups, and the ultrasound then splits cholestasis into dilated "
            "ducts (go downstream to ERCP/MRCP) versus non-dilated (go to the "
            "parenchyma - serologies, autoimmunity, biopsy). The demo works "
            "the fraction split on a jaundiced case."
        ),
        "key_points": [
            "The history hunts exposures (alcohol, drugs, viral risks) and tempo (hours, weeks, years).",
            "The stigmata of chronic liver disease are physical votes for portal hypertension and failed synthesis.",
            "The bilirubin fraction splits jaundice: unconjugated toward hemolysis/Gilbert, conjugated toward cholestasis.",
            "Ultrasound is the first image: dilated ducts mean a plumbing problem, non-dilated means parenchymal.",
            "Asterixis and fetor hepaticus are bedside signs of hepatic encephalopathy.",
        ],
        "requirements": [
            "The exposure checklist and the three time courses.",
            "The stigmata list and what each signifies.",
            "The fraction-then-ultrasound decision tree.",
        ],
        "standards": [
            "Examination terms follow standard clinical usage.",
            "Workup sequencing follows standard practice (fraction, then ultrasound).",
            "Signs are described as typical associations, not pathognomonic proofs.",
        ],
        "citations": [CIT_HARRISON, CIT_SCHIFF, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: the hepatology encounter is a refinery "
            "inspection - the engineer interviews the operators about what "
            "feedstock went in and when the alarms started, walks the plant "
            "reading the rust and the bulging pipes (the stigmata), checks "
            "which waste line is backing up (the bilirubin fraction), and "
            "sends a camera down the outflow main (the ultrasound) before "
            "deciding whether the problem is in the process units or the "
            "plumbing."
        ),
    },
]
ENTRIES += [
    {
        "key": "acute_hep",
        "name": "Acute Viral Hepatitis: The A, B, C, D, and E Viruses",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Five unrelated viruses share one clinical syndrome - acute viral "
            "hepatitis - and telling them apart is route, incubation, and "
            "serology. Hepatitis A and E are fecal-oral, food and water "
            "borne; A is usually self-limited and vaccine-preventable, E can "
            "be severe in pregnancy. Hepatitis B, C, and D are blood and body-"
            "fluid borne: B is a DNA virus with a vaccine and the highest "
            "chronicity risk when acquired at birth; C is an RNA virus that "
            "once chronically infected most of its victims and is now curable; "
            "D is a defective virus that can only infect alongside B. "
            "Incubations differ: A about 15 to 50 days, B 45 to 160, C 14 to "
            "180, D 21 to 90, E 15 to 60. Clinically they converge: a prodrome "
            "of fatigue, nausea, and right-upper-quadrant ache, then jaundice "
            "with ALT in the thousands, then recovery over weeks - except "
            "when they do not, and acute liver failure follows. Serology is "
            "the fingerprint: IgM anti-HAV for A, HBsAg and IgM anti-HBc for "
            "acute B, anti-HCV with HCV RNA for C. This record is the field "
            "guide to all five."
        ),
        "how_it_works": (
            "Each virus works by the same brutal mechanism - it does not kill "
            "hepatocytes directly so much as provoke the immune system into "
            "killing infected ones, which is why the ALT spike tracks the "
            "immune attack and why immunosuppressed patients can carry huge "
            "viral loads with near-normal enzymes. The serology works as a "
            "timeline: IgM antibodies mark the acute attack, IgG marks memory, "
            "surface antigen marks active B infection, surface antibody marks "
            "immunity, core antibody marks exposure that never fully clears "
            "from the record. The demo works the incubation arithmetic: the "
            "five windows as day ranges, their midpoints, and which virus fits "
            "a given exposure-to-illness interval."
        ),
        "key_points": [
            "A and E are fecal-oral; B, C, D are blood/body-fluid borne; D needs B to replicate.",
            "Incubation windows: A 15-50, B 45-160, C 14-180, D 21-90, E 15-60 days.",
            "The ALT spike tracks the immune attack on infected hepatocytes, not direct viral killing.",
            "Serology is the fingerprint: IgM for acute, antigen for active infection, antibody patterns for immunity vs exposure.",
            "Most acute viral hepatitis is self-limited; a minority progresses to acute liver failure.",
        ],
        "requirements": [
            "The five viruses, their routes, and their incubation windows.",
            "The serologic timeline: IgM, IgG, antigen, antibody meanings.",
            "Why immunosuppression can mean high viral load with low ALT.",
        ],
        "standards": [
            "Virus taxonomy and transmission routes follow standard infectious-disease usage.",
            "Incubation ranges stated as standard clinical windows.",
            "Serology interpretation follows standard marker meanings.",
        ],
        "citations": [CIT_HARRISON, CIT_SCHIFF, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: five different saboteurs, one alarm "
            "pattern. Two arrive in the water supply, three in the blood; one "
            "is a parasite that can only ride another. The refinery's own "
            "security forces do the demolition - the ALT spike is friendly "
            "fire on infected units. Serology is the forensics log: who "
            "attacked, when, and whether they were repelled or dug in."
        ),
    },
    {
        "key": "hbv",
        "name": "Chronic Hepatitis B: Natural History and Antiviral Therapy",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Hepatitis B is a DNA virus that writes itself into the "
            "hepatocyte nucleus as cccDNA - a template the immune system "
            "cannot easily erase, which is why chronic infection is for life "
            "even when controlled. About 250 million people carry it "
            "worldwide. The natural history turns on age at infection: "
            "neonatal infection becomes chronic in about 90 percent, adult "
            "infection in under 5 percent. Phases follow: immune-tolerant "
            "(high DNA, normal ALT), immune-active (high DNA, high ALT - the "
            "liver under attack), inactive carrier (low DNA, normal ALT), and "
            "reactivation. HBeAg marks active replication; its loss with anti-"
            "HBe seroconversion is a milestone. Treatment - entecavir, "
            "tenofovir disoproxil, or tenofovir alafenamide - suppresses viral "
            "DNA by logs, not eradicates: therapy is usually indefinite. "
            "Surveillance for hepatocellular carcinoma is lifelong because B "
            "can cause cancer even without cirrhosis. The vaccine, given at "
            "birth in endemic regions, is one of medicine's great prevention "
            "victories. This record follows the virus from exposure to "
            "lifelong management."
        ),
        "how_it_works": (
            "The virus works by persistence: cccDNA sits in the nucleus as a "
            "stable minichromosome, transcribing new virus indefinitely, while "
            "integrated fragments can drive cancer even in a non-cirrhotic "
            "liver. Antivirals work by chain termination - nucleos(t)ide "
            "analogues jam the viral polymerase, and DNA levels fall by orders "
            "of magnitude: a baseline of 8 log IU per milliliter dropping to "
            "near undetectable is a 6-plus log kill, the standard measure of "
            "response. Monitoring works on three dials: HBV DNA (the virus), "
            "ALT (the immune attack), and fibrosis/cancer surveillance (the "
            "damage). The demo works the log-kill arithmetic: converting IU "
            "per milliliter to log scale and computing the treatment response."
        ),
        "key_points": [
            "cccDNA persistence makes chronic hepatitis B a lifelong infection even when fully suppressed.",
            "Chronicity risk is about 90 percent for neonatal infection, under 5 percent for adult infection.",
            "Phases: immune-tolerant, immune-active, inactive carrier, reactivation - DNA plus ALT define each.",
            "Entecavir and tenofovir suppress DNA by multiple logs; therapy is usually indefinite.",
            "HCC surveillance is lifelong - HBV causes cancer even without cirrhosis; the birth-dose vaccine prevents it all.",
        ],
        "requirements": [
            "cccDNA and why cure is elusive.",
            "The four phases and the DNA/ALT/HBeAg markers of each.",
            "Log-scale viral load reading and what a multi-log drop means.",
        ],
        "standards": [
            "Virology terms follow standard usage (cccDNA, HBeAg, seroconversion).",
            "Phase definitions follow AASLD guidance framing.",
            "Drug names are the standard first-line nucleos(t)ide analogues.",
        ],
        "citations": [CIT_AASLD_HBV, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: hepatitis B is the saboteur that bolts its "
            "blueprint to the control room wall - cccDNA the plant cannot "
            "scrape off, so the refinery runs with a permanent stowaway. The "
            "antivirals do not evict it; they cut its supply lines, dropping "
            "its output by a millionfold while the plant keeps running. "
            "Lifelong watch, because a stowaway with a blueprint can still "
            "start a fire - cancer - decades later."
        ),
    },
    {
        "key": "gallstones",
        "name": "Gallstone Disease: Formation, Symptoms, and Treatment",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Gallstones are the most common biliary disease in the Western "
            "world: about 10 to 15 percent of adults carry them, most without "
            "symptoms. They form when bile's three solutes - cholesterol, "
            "bile acids, phospholipids - fall out of balance and cholesterol "
            "crystallizes, nucleating into stones in the gallbladder's quiet "
            "storage. Risk clusters with the classic profile: female, "
            "fertile, forty, fat - plus rapid weight loss, which "
            "paradoxically concentrates bile. Silent stones are left alone; "
            "biliary colic - steady right-upper-quadrant pain after fatty "
            "meals, lasting 30 minutes to hours - earns evaluation; "
            "cholecystitis (fever, Murphy sign, wall thickening on ultrasound) "
            "earns admission and antibiotics; a stone in the common bile duct "
            "(choledocholithiasis) earns ERCP. Laparoscopic cholecystectomy is "
            "the definitive treatment for symptomatic disease - one of the "
            "most performed operations in surgery. The dreaded complication is "
            "gallstone pancreatitis, when a passing stone blocks the ampulla. "
            "This record covers formation, the symptom ladder, and the "
            "treatment algorithm."
        ),
        "how_it_works": (
            "Stone formation works on solubility physics: the liver secretes "
            "cholesterol into bile, and as long as bile acids and phospholipids "
            "hold it in micelles it stays dissolved; when secretion "
            "supersaturates - obesity, rapid weight loss, estrogen - "
            "cholesterol nucleates into crystals that grow into stones. "
            "Symptoms work on obstruction logic: a stone lodged in the cystic "
            "duct gives colic; one stuck with infection gives cholecystitis; "
            "one in the common duct gives jaundice and cholangitis risk; one "
            "at the ampulla gives pancreatitis. Treatment works by removing "
            "the reservoir: without a gallbladder there is nowhere for stones "
            "to form, and bile drips continuously into the gut. The demo works "
            "the epidemiology: cumulative stone risk from annual incidence "
            "over a decade."
        ),
        "key_points": [
            "About 10-15 percent of adults carry gallstones; most are silent and left alone.",
            "Stones form when bile supersaturates with cholesterol and it crystallizes.",
            "The symptom ladder: colic, cholecystitis, choledocholithiasis, gallstone pancreatitis - each a deeper obstruction.",
            "Laparoscopic cholecystectomy is definitive for symptomatic disease.",
            "A stone at the ampulla can trigger pancreatitis - the biliary-pancreatic shared exit.",
        ],
        "requirements": [
            "The solubility model: three solutes, micelles, supersaturation.",
            "The four-step symptom ladder and what each demands.",
            "Why removing the gallbladder prevents recurrence.",
        ],
        "standards": [
            "Disease terms follow standard usage (cholelithiasis, cholecystitis, choledocholithiasis, biliary colic).",
            "Prevalence stated as standard population ranges.",
            "Treatment sequencing follows standard surgical practice.",
        ],
        "citations": [CIT_SLEIS, CIT_HARRISON, CIT_SCHIFF],
        "sig_lens": (
            "His Signature reading: gallstones are scale precipitating in the "
            "surge tank - dissolved solids crystallizing out of the solvent "
            "when the mixture goes off-spec. Silent scale sits harmlessly; "
            "scale blocking the tank outlet gives colic; scale with infection "
            "gives cholecystitis; scale washed into the main gives jaundice "
            "and risks the shared outfall with the neighboring plant "
            "(pancreatitis). The fix is to remove the tank: no reservoir, no "
            "scale."
        ),
    },
    {
        "key": "hcv",
        "name": "Chronic Hepatitis C: From Interferon to Direct-Acting Cure",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Hepatitis C is medicine's great turnaround story: a virus that "
            "once chronically infected the majority of those exposed, marched "
            "them toward cirrhosis over decades, and answered only to a year "
            "of miserable interferon - now cured in 8 to 12 weeks by "
            "direct-acting antivirals with sustained virologic response above "
            "95 percent. An RNA virus spread by blood, it is usually silent "
            "for decades while fibrosis accumulates; the diagnosis often "
            "arrives with the cirrhosis. The DAA regimens - sofosbuvir-based "
            "combinations, glecaprevir/pibrentasvir - jam the viral protease, "
            "polymerase, and NS5A protein simultaneously, leaving the virus no "
            "escape. Cure is defined as undetectable HCV RNA 12 weeks after "
            "therapy (SVR12). Fibrosis can regress after cure, but cirrhosis "
            "that is established keeps its cancer risk - surveillance "
            "continues. The remaining battle is finding the undiagnosed: "
            "birth-cohort and universal adult screening. This record traces "
            "the arc from interferon to cure."
        ),
        "how_it_works": (
            "DAAs work by triple blockade: one drug jams the NS3/4A protease "
            "that cuts viral proteins to size, one jams the NS5B polymerase "
            "that copies the RNA genome, one jams NS5A that organizes "
            "replication - three independent targets, so resistance would "
            "require simultaneous escape mutations, which the virus cannot "
            "manage in 12 weeks. Cure is measured as SVR12: no detectable RNA "
            "three months after the last pill, which in practice means "
            "eradicated - unlike hepatitis B, there is no cccDNA hideout. "
            "The liver then does what it does best: with the attacker gone, "
            "inflammation settles and fibrosis can regress a stage or more. "
            "The demo works the cure arithmetic: the probability that a "
            "treated cohort clears, from the per-patient SVR rate."
        ),
        "key_points": [
            "Direct-acting antivirals cure over 95 percent of hepatitis C in 8-12 weeks - SVR12 defines cure.",
            "Triple blockade (protease, polymerase, NS5A) leaves the virus no resistance escape.",
            "Unlike HBV, HCV has no cccDNA hideout: SVR12 means true eradication.",
            "Fibrosis can regress after cure, but established cirrhosis keeps its HCC risk - surveillance continues.",
            "The remaining fight is case-finding: universal adult screening for the silent infected.",
        ],
        "requirements": [
            "The three DAA targets and why the combination prevents resistance.",
            "SVR12 as the definition of cure and how it differs from HBV suppression.",
            "Post-cure surveillance logic: what regresses, what risk remains.",
        ],
        "standards": [
            "Drug class names follow standard usage (DAA, NS3/4A, NS5B, NS5A).",
            "Cure rates stated as the standard SVR12 ranges.",
            "Screening framing follows current public-health recommendations.",
        ],
        "citations": [CIT_AASLD_HCV, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: hepatitis C was the saboteur the plant "
            "could never quite catch - until engineering built a triple lock "
            "that jammed its tools, its copier, and its foreman all at once, "
            "and the intruder was gone in twelve weeks with no blueprint left "
            "behind. The refinery then does its own maintenance: inflammation "
            "stands down, scar tissue remodels. The lesson the Signature "
            "works keeps: find every compromised plant - screen everyone - "
            "because the fix exists and the silent ones are still running "
            "damaged."
        ),
    },
    {
        "key": "aih",
        "name": "Autoimmune Hepatitis and Overlap Syndromes",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Autoimmune hepatitis is the immune system mistaking the liver "
            "for the enemy: a chronic, fluctuating hepatitis with high IgG, "
            "autoantibodies - ANA, smooth-muscle antibody, anti-LKM1 in type "
            "2 - and interface hepatitis on biopsy, plasma cells crowded at "
            "the portal tract's edge. It favors women, can present at any "
            "age, and untreated it marches to cirrhosis; treated, it remits. "
            "Diagnosis is scored, not guessed: the simplified International "
            "Autoimmune Hepatitis Group criteria award points for antibody "
            "titers, IgG elevation, compatible or typical histology, and "
            "absence of viral hepatitis - 6 points probable, 7 definite. "
            "Treatment is immunosuppression: prednisone to induce, "
            "azathioprine to maintain, with most patients needing long-term "
            "therapy and careful withdrawal only after sustained remission. "
            "Overlap syndromes blend AIH with cholestatic disease - AIH/PBC "
            "or AIH/PSC - and need both halves treated. This record covers the "
            "scoring, the biopsy picture, and the long game of "
            "immunosuppression."
        ),
        "how_it_works": (
            "The disease works as mistaken identity: regulatory T-cell "
            "control slips, and effector cells attack hepatocyte antigens, "
            "producing the interface hepatitis that defines the biopsy - "
            "inflammation spilling from the portal tract into the lobule, "
            "eating the limiting plate. The score works as weighted evidence: "
            "antibodies 1 to 2 points by titer, IgG 1 to 2 points by height "
            "above normal, histology 1 to 2 points by typicality, viral "
            "absence 2 points - the points sum to probable or definite. "
            "Treatment works by suppression then maintenance: steroids quench "
            "the attack fast, azathioprine holds the line at lower toxicity, "
            "and withdrawal is attempted only after years of normal enzymes "
            "and IgG, with relapse watched for. The demo scores a worked case "
            "through the simplified IAIHG criteria."
        ),
        "key_points": [
            "AIH = immune attack on hepatocytes: high IgG, autoantibodies, interface hepatitis with plasma cells.",
            "The simplified IAIHG score: 6 probable, 7 definite - antibodies, IgG, histology, viral absence.",
            "Prednisone induces remission, azathioprine maintains it; most patients need long-term therapy.",
            "Untreated AIH progresses to cirrhosis; treated, it remits - diagnosis changes the trajectory.",
            "Overlap syndromes (AIH/PBC, AIH/PSC) need both the hepatitis and the cholestatic halves treated.",
        ],
        "requirements": [
            "The antibody panel and the type 1/type 2 split.",
            "The four scored elements and the 6/7 thresholds.",
            "Induction vs maintenance therapy and the withdrawal rules.",
        ],
        "standards": [
            "Antibody names follow standard usage (ANA, SMA, anti-LKM1).",
            "Scoring follows the simplified IAIHG criteria.",
            "Treatment framing follows AASLD practice guidance.",
        ],
        "citations": [CIT_AIH, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: autoimmune hepatitis is the plant's own "
            "security force turning on the process units - friendly fire at "
            "the module boundaries, plasma cells massed at the fence line. "
            "The scoring system is the incident report, weighted evidence "
            "adding up to probable or definite sabotage-from-within. The fix "
            "is to stand the security force down - steroids first, then a "
            "lighter leash - and the plant, remarkably, goes back to work."
        ),
    },
    {
        "key": "ald",
        "name": "Alcoholic Liver Disease: Steatosis to Cirrhosis",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Alcohol injures the liver on a dose curve, and the disease "
            "marches through stages: steatosis (fatty liver, reversible in "
            "weeks of abstinence), alcoholic hepatitis (jaundice, fever, "
            "tender liver, Maddrey discriminant function to judge severity), "
            "and cirrhosis. Women are injured at lower doses than men; "
            "drinking pattern and nutrition modify the risk. The classic lab "
            "signature is AST greater than ALT, both usually under 300, with "
            "the ratio above 2 highly suggestive. Severe alcoholic hepatitis - "
            "Maddrey discriminant function 32 or higher, or MELD above 20 - "
            "carries a one-month mortality near 30 to 50 percent; "
            "corticosteroids help the responders, identified by the Lille "
            "score at day 7, and non-responders need transplant evaluation, "
            "not more steroids. Abstinence is the only therapy that changes "
            "every stage: steatosis melts, hepatitis quiets, even cirrhosis "
            "stabilizes. Transplantation for alcoholic liver disease is now "
            "routine with sobriety and psychosocial selection. This record "
            "walks the dose curve and the severity scores."
        ),
        "how_it_works": (
            "Alcohol works as a direct hepatotoxin and a metabolic hijacker: "
            "its metabolism floods the liver with NADH, shifting chemistry "
            "toward fat synthesis (steatosis); its metabolite acetaldehyde "
            "adducts proteins, provoking inflammation; chronic use induces "
            "CYP2E1, generating oxidative stress; gut permeability rises, "
            "bathing the liver in endotoxin. The Maddrey discriminant function "
            "- 4.6 times (patient PT minus control PT) plus bilirubin in "
            "mg/dL - sorts severe from non-severe at 32: above it, short-term "
            "death is common enough to justify steroids; the Lille score at "
            "day 7 then sorts steroid responders from non-responders. The demo "
            "computes the Maddrey score on a worked case and applies the 32 "
            "threshold."
        ),
        "key_points": [
            "Stages: steatosis (reversible) to alcoholic hepatitis to cirrhosis - a dose-driven march.",
            "AST greater than ALT, ratio above 2, both usually under 300: the classic signature.",
            "Maddrey discriminant function >= 32 defines severe alcoholic hepatitis: 4.6x(PT - control) + bilirubin.",
            "Steroids for severe disease; Lille score at day 7 identifies non-responders who need transplant evaluation.",
            "Abstinence is the only therapy that improves every stage.",
        ],
        "requirements": [
            "The three stages and their reversibility.",
            "The Maddrey formula and the 32 threshold.",
            "The AST/ALT signature and the Lille-based steroid decision.",
        ],
        "standards": [
            "Score formulas follow the original Maddrey and Lille definitions.",
            "Lab patterns stated as typical, with dose and sex modifiers noted.",
            "Treatment framing follows standard practice for severe alcoholic hepatitis.",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: alcohol is a corrosive feedstock the plant "
            "was never rated for - it gums the works with fat, pits the "
            "vessels with oxidative rust, and invites contamination through a "
            "leaky intake (the gut). The Maddrey number is the damage gauge: "
            "past 32, the plant is failing fast enough to risk the heavy "
            "intervention. And the first order in every Signature work order "
            "is the same: stop feeding the corrosive - abstinence - because no "
            "repair holds while the bad feedstock flows."
        ),
    },
]
ENTRIES += [
    {
        "key": "acute_panc",
        "name": "Acute Pancreatitis: Diagnosis, Severity, and Management in Hepatology",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The pancreas sits in hepatology's territory - the hepato-"
            "pancreato-biliary triangle - and acute pancreatitis is its "
            "explosive emergency. Gallstones and alcohol cause the large "
            "majority; the rest is drugs, hypertriglycerides (usually above "
            "1000 mg/dL), hypercalcemia, ERCP itself, and genetics. Diagnosis "
            "needs two of three: characteristic epigastric pain radiating to "
            "the back, lipase or amylase above three times the upper limit, "
            "and characteristic imaging. Severity is what matters: most cases "
            "are mild and self-limited, but necrosis, organ failure, and "
            "infection define severe disease - the revised Atlanta "
            "classification. Management is aggressive fluids, early feeding "
            "(not prolonged fasting), pain control, and - for gallstone "
            "pancreatitis - cholecystectomy on the same admission once "
            "settled, plus ERCP within 24 hours if cholangitis coexists. "
            "Necrosis that stays sterile is watched; infected necrosis needs "
            "drainage, stepping up from percutaneous to endoscopic to "
            "surgical. This record covers the diagnosis rule, the severity "
            "sort, and the step-up ladder."
        ),
        "how_it_works": (
            "Pancreatitis works as autodigestion: activated trypsin inside the "
            "acinar cell instead of the duodenum, digesting the gland itself, "
            "spilling lipase into the blood - which is why lipase above three "
            "times normal is diagnostic. Severity works on two axes: local "
            "(edema versus necrosis, sterile versus infected) and systemic "
            "(transient versus persistent organ failure). Fluids work by "
            "perfusing the gland before necrosis sets; early feeding works "
            "because the gut barrier fails when starved, inviting the very "
            "infection everyone fears. The step-up approach works by doing the "
            "least first: percutaneous drain, then endoscopic necrosectomy, "
            "then surgery only if needed. The demo applies the diagnostic "
            "rule: the lipase multiple of the upper limit on a worked case."
        ),
        "key_points": [
            "Gallstones and alcohol cause most acute pancreatitis; diagnosis needs 2 of 3: pain, lipase >3x ULN, imaging.",
            "Severity sorts by necrosis/infection locally and transient/persistent organ failure systemically (Atlanta).",
            "Management: aggressive fluids, early feeding, same-admission cholecystectomy for gallstone cases.",
            "ERCP within 24 hours when cholangitis coexists with gallstone pancreatitis.",
            "Infected necrosis steps up: percutaneous drain, then endoscopic necrosectomy, then surgery.",
        ],
        "requirements": [
            "The 2-of-3 diagnostic rule and the lipase threshold.",
            "The Atlanta severity axes.",
            "The step-up ladder for necrosis and the cholecystectomy timing rule.",
        ],
        "standards": [
            "Diagnosis and classification follow the revised Atlanta criteria.",
            "Management sequencing follows ACG guideline framing.",
            "Etiology list follows standard clinical teaching.",
        ],
        "citations": [CIT_ACG_PANC, CIT_SLEIS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the neighboring enzyme plant suffers a "
            "containment breach - its own product activated inside the walls, "
            "digesting the factory from within. The lipase in the blood is the "
            "leak detector: three times normal means breach confirmed. The "
            "Signature response is containment first (fluids, feed the gut "
            "barrier), then the least invasive cleanup that works, and finally "
            "removing the cause that sent the blockage downstream - the "
            "gallbladder - before it can strike again."
        ),
    },
    {
        "key": "masld_meta",
        "name": "Metabolic Liver Disease: MASLD, Hemochromatosis, and Wilson Disease",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Metabolism can wreck the liver three ways: by fat, by iron, and "
            "by copper. MASLD - metabolic dysfunction-associated steatotic "
            "liver disease, the 2023 multisociety rename of NAFLD - is the "
            "commonest liver disease on earth, tracking obesity and diabetes: "
            "fat in the liver plus metabolic dysfunction, ranging from simple "
            "steatosis to MASH (steatohepatitis) with ballooning and "
            "inflammation to fibrosis and cirrhosis. Fibrosis stage, not fat "
            "amount, predicts outcomes, and the FIB-4 score - age times AST "
            "divided by platelets times the square root of ALT - triages who "
            "needs elastography: under 1.3 low risk, over 2.67 (3.25 in some "
            "framings) high. Weight loss of 7 to 10 percent can regress MASH; "
            "resmetirom is the first approved MASH therapy. Hemochromatosis "
            "(HFE C282Y homozygosity) loads iron - bronze skin, diabetes, "
            "arthropathy, liver disease - and is treated by phlebotomy, the "
            "simplest effective therapy in hepatology. Wilson disease (ATP7B) "
            "traps copper: Kayser-Fleischer rings, low ceruloplasmin, "
            "neuropsychiatric disease in the young - treated by chelation or "
            "zinc. Three metabolic failures, three very different fixes."
        ),
        "how_it_works": (
            "MASLD works as overflow: insulin resistance floods the liver with "
            "free fatty acids beyond its export and oxidation capacity, fat "
            "accumulates, lipotoxicity injures hepatocytes, and wound healing "
            "lays down fibrosis - stage F0 to F4 - which is the outcome "
            "predictor. FIB-4 works as a triage formula from routine labs, "
            "sparing low-risk patients the elastography queue. Hemochromatosis "
            "works as unregulated iron absorption - hepcidin broken - and "
            "phlebotomy works by simple mass balance: each unit of blood "
            "removed carries away about 250 milligrams of iron. Wilson works "
            "as failed copper export into bile, and chelators or zinc (which "
            "blocks gut copper uptake) restore the balance. The demo computes "
            "FIB-4 on a worked case and applies the triage bands."
        ),
        "key_points": [
            "MASLD (renamed from NAFLD, 2023) is the commonest liver disease; fibrosis stage predicts outcomes, not fat amount.",
            "FIB-4 = age x AST / (platelets x sqrt(ALT)): <1.3 low risk, >2.67-3.25 high risk.",
            "7-10 percent weight loss regresses MASH; resmetirom is the first approved drug therapy.",
            "Hemochromatosis (HFE C282Y): iron overload treated by phlebotomy - mass balance medicine.",
            "Wilson disease (ATP7B): copper trapping with Kayser-Fleischer rings; chelation or zinc treats it.",
        ],
        "requirements": [
            "The MASLD spectrum and why fibrosis stage is the prognostic variable.",
            "The FIB-4 formula and its triage bands.",
            "The iron and copper disorders: genes, clues, and their mass-balance treatments.",
        ],
        "standards": [
            "Nomenclature follows the 2023 multisociety Delphi consensus (MASLD/MASH).",
            "FIB-4 bands follow standard clinical cutoffs.",
            "Genetic and treatment facts follow standard teaching.",
        ],
        "citations": [CIT_AASLD_MASLD, CIT_MASLD_NOMEN, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: three ways the warehouse poisons the "
            "refinery. Fat overflow from a broken metabolic supply chain "
            "(MASLD) - and the fix is to shrink the deliveries, 7 to 10 "
            "percent off the load. Iron with no export valve (hemochromatosis) "
            "- fixed by scheduled draining, the simplest mass balance in the "
            "works. Copper with a jammed export pump (Wilson) - fixed by "
            "chemical extraction or blocking the intake. The FIB-4 is the "
            "warehouse inspector's gauge: which overflow has already scarred "
            "the structure."
        ),
    },
    {
        "key": "dili",
        "name": "Drug-Induced Liver Injury",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Nearly every drug can injure the liver, and drug-induced liver "
            "injury is the great mimicker - it copies viral hepatitis, "
            "cholestasis, and autoimmune disease, and the diagnosis is made by "
            "suspicion, timing, and exclusion. Acetaminophen is the dose-"
            "dependent king: predictable, the commonest cause of acute liver "
            "failure in the West, treated with N-acetylcysteine, which "
            "replenishes glutathione. Everything else is idiosyncratic: "
            "amoxicillin-clavulanate (cholestatic, the commonest idiosyncratic "
            "cause), isoniazid, nitrofurantoin, statins, herbal and dietary "
            "supplements - a growing share. The pattern is read with the R "
            "ratio: hepatocellular, cholestatic, or mixed. Hy's law is the "
            "prognostic rule: ALT above 3 times normal plus bilirubin above 2 "
            "times normal (with alkaline phosphatase under 2 times) predicts "
            "about a 10 percent fatality - the FDA's signal for a dangerous "
            "drug. Causality is scored by RUCAM. The first treatment is always "
            "the same: stop the drug. This record covers the culprits, the "
            "patterns, and Hy's law."
        ),
        "how_it_works": (
            "Acetaminophen injury works on glutathione depletion: therapeutic "
            "doses are safely conjugated, but overdose saturates the safe "
            "pathways and shunts the drug to CYP2E1, making the toxic NAPQI "
            "metabolite that glutathione mops up - until glutathione runs out, "
            "and NAPQI binds liver proteins and kills cells. N-acetylcysteine "
            "works by resupplying glutathione's building blocks, and it helps "
            "even late. Idiosyncratic injury works by immune or metabolic "
            "quirk - unpredictable, dose-independent, with latency of days to "
            "months. Hy's law works as a mortality predictor because "
            "bilirubin rise on top of hepatocellular injury means the liver "
            "has lost both cell mass and excretory function. The demo applies "
            "Hy's law to a worked case."
        ),
        "key_points": [
            "Acetaminophen is dose-dependent and predictable; nearly everything else is idiosyncratic and unpredictable.",
            "Amoxicillin-clavulanate is the commonest idiosyncratic cause; supplements are a growing share.",
            "Hy's law: ALT >3x ULN plus bilirubin >2x ULN predicts ~10 percent fatality - the danger signal.",
            "N-acetylcysteine replenishes glutathione and treats acetaminophen injury even late.",
            "The first treatment for any DILI is stopping the drug; causality is scored by RUCAM.",
        ],
        "requirements": [
            "The two mechanisms: dose-dependent (acetaminophen) vs idiosyncratic.",
            "Hy's law components and what the 10 percent means.",
            "The NAC mechanism and the stop-the-drug rule.",
        ],
        "standards": [
            "Culprit ranking follows standard DILI teaching and ACG guidance.",
            "Hy's law stated in its standard form.",
            "Causality framing follows RUCAM.",
        ],
        "citations": [CIT_DILI, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: DILI is contamination events at the "
            "refinery - some feedstocks are corrosive past a known dose "
            "(acetaminophen, with its antidote as the emergency neutralizer), "
            "others trigger a freak reaction in one plant in ten thousand. "
            "Hy's law is the catastrophe gauge: ruptured units plus failed "
            "waste export together mean one in ten such events ends in total "
            "plant loss. The first Signature order is always the same: shut "
            "off the suspect feed."
        ),
    },
    {
        "key": "cholestatic",
        "name": "Cholestatic Liver Disease: PBC and PSC",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Cholestasis - bile that cannot flow - has two classic chronic "
            "diseases, and they are mirror images. Primary biliary cholangitis "
            "(PBC, the renamed primary biliary cirrhosis) attacks the small "
            "intrahepatic bile ducts in middle-aged women: itching, fatigue, "
            "a cholestatic enzyme pattern, and anti-mitochondrial antibody "
            "(AMA) positive in about 95 percent - one of the most specific "
            "antibodies in medicine. Ursodeoxycholic acid slows it; "
            "obeticholic acid and fibrates are second line; transplant cures "
            "the liver but the disease can recur. Primary sclerosing "
            "cholangitis (PSC) scars the large ducts inside and outside the "
            "liver in young men, most with inflammatory bowel disease: "
            "beading and strictures on MRCP, recurrent cholangitis, and a "
            "lifelong cholangiocarcinoma risk around 10 to 15 percent that "
            "drives surveillance. No drug slows PSC - transplant is the only "
            "definitive therapy. This record contrasts the small-duct and "
            "large-duct diseases."
        ),
        "how_it_works": (
            "PBC works as immune destruction of the small ducts: AMA targets "
            "the pyruvate dehydrogenase complex on cholangiocytes, ducts "
            "vanish (ductopenia), and bile backs up into the liver. "
            "Ursodeoxycholic acid works by diluting the toxic hydrophobic "
            "bile acid pool with a hydrophilic one and improving flow. PSC "
            "works as concentric fibrosis around large ducts - onion-skin "
            "lesions - producing the beaded MRCP picture; the strictures "
            "invite bacterial ascent (cholangitis) and the chronic "
            "inflammation invites malignant transformation "
            "(cholangiocarcinoma). Surveillance works by scheduled MRCP and "
            "CA19-9, hunting the cancer that complicates 1 in 7. The demo "
            "works the cholestatic pattern: the alkaline phosphatase multiple "
            "and the R ratio on a PBC-pattern case."
        ),
        "key_points": [
            "PBC: small-duct disease of middle-aged women, AMA positive ~95 percent, UDCA slows it.",
            "PSC: large-duct scarring of young men with IBD, beading on MRCP, no disease-slowing drug.",
            "PSC carries a 10-15 percent lifetime cholangiocarcinoma risk - surveillance is mandatory.",
            "Transplant treats both definitively; PBC can recur in the graft.",
            "The cholestatic pattern (high ALP, R ratio <2) is the shared laboratory signature.",
        ],
        "requirements": [
            "The small-duct vs large-duct contrast: who, what antibody, what imaging.",
            "UDCA's mechanism and the second-line options in PBC.",
            "PSC surveillance: what is hunted and how.",
        ],
        "standards": [
            "Disease names follow current usage (cholangitis, not cirrhosis, for PBC).",
            "Antibody and imaging facts follow standard teaching.",
            "Treatment framing follows AASLD practice guidance.",
        ],
        "citations": [CIT_PBC, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: two ways the outflow plumbing fails from "
            "the inside. PBC is corrosion of the small branch lines in one "
            "population - the fix is to flush the system with a gentler "
            "solvent (UDCA) that dilutes the corrosive mix. PSC is scarring of "
            "the great mains in another - no chemical fix exists, only "
            "watching the scarred pipes for the cancer that grows in chronic "
            "irritation, and ultimately replacing the whole drainage system. "
            "Same backed-up product, opposite ends of the pipe map."
        ),
    },
    {
        "key": "chronic_panc",
        "name": "Chronic Pancreatitis and Pancreatic Exocrine Insufficiency",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Chronic pancreatitis is the pancreas burned out by repeated "
            "injury: alcohol and smoking lead, but genetics (PRSS1, CFTR, "
            "SPINK1), autoimmune disease, and ductal obstruction all qualify. "
            "The gland fibroses, calcifies - the classic plain-film finding - "
            "and loses function in sequence: first exocrine (fat "
            "malabsorption, steatorrhea, weight loss), then endocrine "
            "(diabetes, often brittle, with lost glucagon counter-regulation "
            "too). Pain is the presenting complaint and the hardest problem: "
            "it can be constant, narcotic-requiring, and life-shrinking. "
            "Diagnosis rests on imaging - calcifications on CT, ductal "
            "beading and side-branch ectasia on MRCP/EUS - plus function: "
            "fecal elastase under 200 micrograms per gram marks "
            "insufficiency. Treatment is replacement and relief: pancreatic "
            "enzyme replacement with meals (tens of thousands of lipase units "
            "per meal), abstinence, smoking cessation, diabetes management, "
            "and endoscopic or surgical drainage for ductal obstruction. This "
            "record covers the burnout sequence and the replacement math."
        ),
        "how_it_works": (
            "The burnout works as repeated autodigestive hits followed by "
            "fibrotic repair: each attack lays down scar, the scar strangles "
            "ducts and acini, and function falls in the fixed order - "
            "exocrine first because enzyme output has the most reserve to "
            "lose, endocrine later because islets are hardier. Enzyme "
            "replacement works by outsourcing digestion: 50,000 to 90,000 "
            "lipase units with each meal mix with chyme and do the gland's "
            "job, dosed to the fat content of the meal and taken during it, "
            "not after. Pain treatment works stepwise: abstinence and enzymes "
            "first, then endoscopic stenting or stone clearance for "
            "obstructive pain, then surgical drainage (Puestow) or resection "
            "for the refractory. The demo computes a day's enzyme replacement "
            "from a meal plan."
        ),
        "key_points": [
            "Chronic pancreatitis = repeated injury to fibrosis: calcification, then exocrine failure, then diabetes.",
            "Fecal elastase <200 mcg/g marks exocrine insufficiency.",
            "Enzyme replacement: 50,000-90,000 lipase units per meal, taken during the meal.",
            "Alcohol and smoking are the leading causes; genetics and autoimmunity fill out the list.",
            "Pain steps up: abstinence, enzymes, endoscopic drainage, surgical drainage or resection.",
        ],
        "requirements": [
            "The function-loss sequence and why exocrine fails first.",
            "The elastase threshold and the imaging signatures.",
            "Enzyme dosing logic and the pain ladder.",
        ],
        "standards": [
            "Cause list and diagnostics follow standard clinical teaching.",
            "Dosing ranges follow standard replacement practice.",
            "Diabetes framing notes the lost glucagon counter-regulation.",
        ],
        "citations": [CIT_SLEIS, CIT_HARRISON, CIT_SCHIFF],
        "sig_lens": (
            "His Signature reading: the enzyme plant burns out the way any "
            "overworked chemical works does - repeated containment breaches, "
            "each repaired with scar, until the scar tissue chokes the "
            "production lines. First the bulk product line fails (enzymes), "
            "then the specialty line (insulin). The Signature fix is "
            "outsourcing: ship in the product from outside (enzyme capsules "
            "with every batch of raw material), stop feeding the corrosives "
            "(alcohol, smoke), and replumb the choked lines before cutting "
            "steel."
        ),
    },
]
ENTRIES += [
    {
        "key": "cirrhosis",
        "name": "Cirrhosis: From Fibrosis to End-Stage Liver Disease",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Cirrhosis is the liver's final common scar: chronic injury - "
            "viral, alcohol, fat, autoimmune, cholestatic - heals as fibrosis, "
            "and when fibrosis bridges and nodules form, the architecture is "
            "cirrhosis. It is staged F0 to F4 on the METAVIR scale, F4 being "
            "cirrhosis, but the clinical split that matters is compensated "
            "versus decompensated: compensated cirrhosis can be silent for "
            "years, with median survival over a decade; decompensation - "
            "ascites, variceal bleeding, encephalopathy, jaundice - drops "
            "median survival to about two years and is the trigger for "
            "transplant evaluation. Diagnosis is increasingly noninvasive: "
            "elastography (liver stiffness above about 12.5 to 14 kilopascals "
            "suggests cirrhosis), FIB-4, and imaging showing a nodular liver "
            "with splenomegaly - biopsy reserved for uncertainty. Every "
            "cirrhotic patient enters surveillance: ultrasound with or without "
            "AFP every six months for hepatocellular carcinoma, endoscopy for "
            "varices. Treating the cause can stabilize and even regress early "
            "cirrhosis - viral suppression, abstinence, weight loss. This "
            "record is the map of the scarred liver and its two prognoses."
        ),
        "how_it_works": (
            "Fibrosis works as wound healing gone chronic: hepatic stellate "
            "cells activate to myofibroblasts and lay down collagen in the "
            "space of Disse; the sinusoids capillarize, losing their "
            "fenestrations; resistance to portal flow climbs and the liver "
            "stiffens - which is exactly what elastography measures, shear-"
            "wave speed as stiffness in kilopascals. Decompensation works as "
            "threshold failure: portal pressure crosses the levels for "
            "varices and ascites, synthetic function falls below the needs of "
            "hemostasis and oncotic pressure, and the first decompensating "
            "event rewrites the prognosis. Regression works because the liver "
            "remodels: remove the injury and metalloproteinases can chew back "
            "early scar. The demo applies the stiffness cutoffs to worked "
            "elastography readings."
        ),
        "key_points": [
            "Cirrhosis = F4 fibrosis with nodular architecture; the clinical split is compensated vs decompensated.",
            "Compensated median survival exceeds a decade; decompensation drops it to about two years.",
            "Elastography stiffness above ~12.5-14 kPa suggests cirrhosis; biopsy is now reserved for uncertainty.",
            "Every cirrhotic patient gets HCC surveillance (ultrasound +/- AFP every 6 months) and variceal screening.",
            "Treating the cause - viral suppression, abstinence, weight loss - can stabilize or regress early cirrhosis.",
        ],
        "requirements": [
            "The F0-F4 scale and the compensated/decompensated split with its survival figures.",
            "Elastography cutoffs and the noninvasive diagnostic pathway.",
            "The surveillance bundle and the regression principle.",
        ],
        "standards": [
            "Staging follows METAVIR; stiffness cutoffs stated as standard approximate ranges.",
            "Survival figures stated as standard medians with 'about' qualifiers.",
            "Surveillance intervals follow standard practice.",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_AASLD_MASLD],
        "sig_lens": (
            "His Signature reading: cirrhosis is the refinery after decades "
            "of running damaged - the reaction beds choked with scar tissue, "
            "the vessels narrowed until feedstock backs up at the gates, the "
            "structure gone nodular and stiff. Compensated is the plant "
            "running derated but running; decompensated is the first system "
            "tripping offline, and the clock starts. The Signature lesson: "
            "stop the damage and even scarred works can remodel - but read "
            "the stiffness gauge honestly, because past a point the only fix "
            "is a new plant."
        ),
    },
    {
        "key": "portal_htn",
        "name": "Portal Hypertension: Varices, Shunts, and Bleeding",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Portal hypertension is the plumbing catastrophe of cirrhosis: "
            "scarred sinusoids resist portal flow, pressure climbs, and blood "
            "finds detours - portosystemic collaterals that become esophageal "
            "and gastric varices, a congested spleen, ascites weeping from the "
            "liver surface. The hepatic venous pressure gradient (HVPG) "
            "defines it: 10 millimeters of mercury or more is clinically "
            "significant portal hypertension, 12 or more is the threshold for "
            "variceal bleeding. Variceal hemorrhage is the emergency: "
            "vomited blood, melena, shock - managed with vasoactive drugs "
            "(octreotide, terlipressin), antibiotics, urgent endoscopy with "
            "band ligation, and balloon tamponade as a bridge. Prevention is "
            "banding or non-selective beta-blockers (carvedilol, propranolol) "
            "for high-risk varices. Refractory bleeding or ascites earns a "
            "TIPS - a transjugular intrahepatic portosystemic shunt, a stent "
            "through the liver connecting portal to hepatic vein, trading "
            "pressure relief for encephalopathy risk. This record covers the "
            "gradients, the varices, and the shunt."
        ),
        "how_it_works": (
            "The pressure works on resistance arithmetic: portal pressure "
            "equals flow times resistance, and cirrhosis multiplies "
            "resistance through fibrosis, capillarization, and active "
            "vasoconstriction - while splanchnic vasodilation paradoxically "
            "increases inflow, worsening the gradient. HVPG - wedged hepatic "
            "venous pressure minus free - measures the sinusoidal gradient "
            "directly. Varices work as thin-walled detours: at 12 mmHg they "
            "can rupture, and wall tension follows Laplace's law - bigger "
            "varices with red signs bleed first. Beta-blockers work by cutting "
            "cardiac output and splanchnic flow; banding works by strangling "
            "the varix; TIPS works by giving the blood a low-resistance "
            "shortcut through the liver. The demo computes HVPG from wedged "
            "and free pressures and applies the 10/12 thresholds."
        ),
        "key_points": [
            "HVPG >= 10 mmHg is clinically significant portal hypertension; >= 12 is variceal bleeding territory.",
            "Variceal bleeding management: vasoactive drugs, antibiotics, urgent band ligation, tamponade as bridge.",
            "Prevention: band ligation or non-selective beta-blockers for high-risk varices.",
            "TIPS trades pressure relief for encephalopathy risk - the definitive shunt for refractory cases.",
            "Wall tension follows Laplace's law: large varices with red signs are the ones that rupture.",
        ],
        "requirements": [
            "The HVPG definition and the 10/12 thresholds.",
            "The acute bleed algorithm in order.",
            "Prevention options and the TIPS trade-off.",
        ],
        "standards": [
            "Pressure thresholds follow standard HVPG teaching.",
            "Drug names follow standard acute-bleed practice.",
            "Management sequencing follows AASLD practice guidance.",
        ],
        "citations": [CIT_PORTAL, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: portal hypertension is back-pressure at "
            "the refinery gates - the reaction beds choked with scar, feed "
            "pumps still driving flow in, so pressure climbs until relief "
            "valves blow open as varices: thin-walled bypass lines never meant "
            "for the load. The engineer reads the gradient gauge (HVPG), "
            "reinforces or ties off the bulging bypasses (banding, beta-"
            "blockers), and for the desperate case bores a relief tunnel "
            "straight through the plant (TIPS) - knowing the shortcut lets "
            "unprocessed feed reach the town downstream (encephalopathy)."
        ),
    },
    {
        "key": "alf",
        "name": "Acute Liver Failure: Kings College Criteria and Transplant Listing",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Acute liver failure is the liver dying in days: coagulopathy "
            "(INR 1.5 or above) plus encephalopathy in a patient without prior "
            "liver disease, inside 26 weeks of illness. Acetaminophen leads in "
            "the West - often unintentional, staggered overdoses - followed by "
            "idiosyncratic drug injury, acute viral hepatitis, autoimmune "
            "hepatitis, Wilson disease, Budd-Chiari, and shock liver. The "
            "patient is managed in the ICU: N-acetylcysteine even for non-"
            "acetaminophen cases, intracranial pressure vigilance (the brain "
            "swells as ammonia soars), coagulopathy corrected only for "
            "procedures (the INR is not a bleeding predictor here), infection "
            "surveillance. The decision that matters is transplant listing, "
            "and the Kings College criteria make it: for acetaminophen, "
            "arterial pH below 7.30 after resuscitation, or INR above 6.5 with "
            "creatinine above 3.4 mg/dL and grade 3-4 encephalopathy; for "
            "other causes, INR above 6.5 or three of five (age under 10 or "
            "over 40, non-A non-B etiology, jaundice over 7 days before "
            "encephalopathy, INR above 3.5, bilirubin above 17.5 mg/dL). Meet "
            "criteria and the only exit is a new liver - status 1A listing. "
            "This record covers the definition, the ICU, and the listing "
            "decision."
        ),
        "how_it_works": (
            "The failure works as mass necrosis: enough hepatocytes die at "
            "once that synthesis (clotting factors - hence the INR), clearance "
            "(ammonia - hence the brain swelling), and glucose production all "
            "collapse together. Cerebral edema works on the ammonia-"
            "glutamine mechanism: astrocytes swell as they detoxify ammonia "
            "to glutamine, and intracranial pressure can herniate. The Kings "
            "College criteria work as validated prognosis: they were derived "
            "from patients who died without transplant, so meeting them means "
            "survival without a new liver is unlikely - the ethical engine of "
            "status 1A super-urgent listing. N-acetylcysteine works even in "
            "non-acetaminophen failure by improving microcirculatory flow and "
            "oxygen delivery. The demo evaluates the acetaminophen Kings "
            "College criteria on a worked case."
        ),
        "key_points": [
            "ALF = INR >= 1.5 plus encephalopathy, no prior liver disease, within 26 weeks.",
            "Acetaminophen is the leading Western cause; NAC helps even non-acetaminophen cases.",
            "Brain swelling from hyperammonemia is the killer - ICP vigilance is central ICU care.",
            "Kings College criteria decide transplant listing: pH <7.30 (acetaminophen) or the multi-factor rule.",
            "Meeting criteria means status 1A super-urgent listing - the only exit is a new liver.",
        ],
        "requirements": [
            "The ALF definition with its three elements.",
            "Both Kings College rules (acetaminophen and non-acetaminophen).",
            "ICU principles: NAC, ICP, coagulopathy, infection.",
        ],
        "standards": [
            "Criteria stated in the original Kings College formulation.",
            "Definition follows the standard 26-week framing.",
            "Management follows standard ALF critical-care teaching.",
        ],
        "citations": [CIT_ALF, CIT_KINGS, CIT_SCHIFF],
        "sig_lens": (
            "His Signature reading: acute liver failure is the refinery going "
            "dark in days - mass casualty among the process units, the gauges "
            "all red at once: synthesis dead (INR soaring), waste treatment "
            "dead (ammonia flooding the town's water - the brain swelling), "
            "power dead (glucose gone). The Kings College criteria are the "
            "point-of-no-return gauges, validated on plants that never "
            "recovered: past them, the only Signature order is a full plant "
            "replacement on the super-urgent list."
        ),
    },
    {
        "key": "biopsy",
        "name": "Liver Biopsy and Elastography: Measuring Fibrosis",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Someone has to look at the tissue - or measure its stiffness - "
            "and hepatology has both. Percutaneous liver biopsy, usually "
            "ultrasound-guided, takes a core that must be adequate: at least "
            "20 millimeters long with 11 or more portal tracts, or the "
            "pathologist is reading a sample too small to stage. It remains "
            "the reference for grading inflammation and staging fibrosis, for "
            "diagnosing AIH, DILI, and unclear cases - with bleeding as the "
            "feared complication, watched for hours after. Transjugular biopsy "
            "goes through the neck when coagulopathy forbids the percutaneous "
            "route, and measures HVPG on the way. Elastography - transient "
            "(FibroScan) or shear-wave - measures stiffness in kilopascals as "
            "the noninvasive surrogate: roughly under 7 kPa normal, 7-9.5 "
            "significant fibrosis, 9.5-12.5 advanced, above 12.5-14 cirrhosis "
            "- confounded by inflammation, congestion, and meals, so it is "
            "read with the clinical context. Together with FIB-4 and imaging, "
            "elastography has moved most fibrosis assessment out of the "
            "biopsy suite. This record covers both instruments and their "
            "cutoffs."
        ),
        "how_it_works": (
            "Biopsy works by sampling: a 1.5-millimeter core through the "
            "capsule, fixed and stained - trichrome for collagen, iron and "
            "copper stains when needed - read as grade (inflammation) and "
            "stage (fibrosis F0-F4). Sampling error is the eternal caveat: a "
            "50,000th of the liver stands in for the whole. Elastography "
            "works on shear-wave physics: a pulse is sent through the liver, "
            "and stiffer tissue conducts it faster - speed converts to "
            "kilopascals. Inflammation, congestion, and a recent meal all "
            "stiffen the liver transiently, which is why the number is never "
            "read alone. The clinical pathway works as a funnel: FIB-4 first, "
            "elastography for the indeterminate, biopsy for the still-"
            "unclear. The demo applies the adequacy rule and the stiffness "
            "bands to worked readings."
        ),
        "key_points": [
            "Adequate biopsy: >= 20 mm core with >= 11 portal tracts - smaller samples misstage.",
            "Elastography bands: <7 normal, 7-9.5 significant fibrosis, 9.5-12.5 advanced, >12.5-14 cirrhosis.",
            "Inflammation, congestion, and meals falsely stiffen - context is mandatory.",
            "Transjugular biopsy is the route when coagulopathy forbids percutaneous, and yields HVPG.",
            "The modern funnel: FIB-4, then elastography, then biopsy only for the unclear.",
        ],
        "requirements": [
            "The adequacy rule and why sampling error matters.",
            "The four stiffness bands and their three confounders.",
            "The percutaneous vs transjugular indications.",
        ],
        "standards": [
            "Adequacy and bands stated as standard clinical cutoffs.",
            "Technique descriptions follow standard practice.",
            "The funnel follows current noninvasive-assessment pathways.",
        ],
        "citations": [CIT_SCHIFF, CIT_AASLD_MASLD, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: biopsy is cutting a core sample out of "
            "the reaction bed - the definitive assay, but one core standing "
            "in for the whole vessel, and the vessel bleeds when you drill "
            "it. Elastography is the non-destructive test: ping the structure "
            "and read how fast the echo returns - stiff means scarred, with "
            "false readings when the plant is inflamed, congested, or just "
            "fed. The Signature inspection order is always cheapest test "
            "first, drill only when the gauges disagree."
        ),
    },
    {
        "key": "ercp",
        "name": "ERCP and Biliary Endoscopy: Stenting the Bile Duct",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "ERCP - endoscopic retrograde cholangiopancreatography - is the "
            "hepatologist's plumbing intervention: a duodenoscope to the "
            "ampulla, cannulation of the bile duct, contrast to map the "
            "strictures and stones, then therapy - sphincterotomy, stone "
            "extraction with balloon or basket, stricture dilation, and "
            "stenting with plastic or metal stents. Indications are "
            "obstructive: choledocholithiasis, malignant strictures "
            "(pancreatic cancer, cholangiocarcinoma), postoperative leaks, "
            "and PSC dominant strictures. It is therapeutic, not diagnostic - "
            "MRCP images first, ERCP intervenes. The signature complication is "
            "post-ERCP pancreatitis, in the single-digit percents, cut by "
            "rectal NSAIDs and prophylactic pancreatic stents in high-risk "
            "cases; bleeding, perforation, and cholangitis complete the risk "
            "list. Success is measured in drainage: bilirubin falling, "
            "cholangitis resolving, the duct open on the final cholangiogram. "
            "This record covers the indications, the toolkit, and the "
            "complication ledger."
        ),
        "how_it_works": (
            "The procedure works as remote plumbing through a natural "
            "orifice: the scope reaches the ampulla, a catheter finds the "
            "bile duct orifice, and contrast outlines the ductal map - stones "
            "as filling defects, strictures as narrowings. Sphincterotomy "
            "works by cutting the sphincter of Oddi with electrocautery, "
            "opening the outfall so stones can be swept with a balloon. "
            "Stents work as internal scaffolds: plastic for temporary "
            "drainage and leaks, self-expanding metal for malignant "
            "strictures that must stay open for months. Prophylaxis works on "
            "two proven levers: rectal indomethacin blunts the inflammatory "
            "cascade, pancreatic stents keep the pancreatic orifice draining. "
            "The demo works the drainage arithmetic: bilirubin before and "
            "after stenting, and the percent drop that marks success."
        ),
        "key_points": [
            "ERCP is therapeutic: stones, strictures, leaks, stents - MRCP diagnoses, ERCP intervenes.",
            "Sphincterotomy opens the outfall; balloons sweep stones; plastic or metal stents scaffold strictures.",
            "Post-ERCP pancreatitis is the signature complication; rectal NSAIDs and pancreatic stents prevent it.",
            "Malignant strictures get self-expanding metal stents; leaks and temporary drainage get plastic.",
            "Success reads out as falling bilirubin and a draining duct - the plumbing restored.",
        ],
        "requirements": [
            "The indication list and the MRCP-first principle.",
            "The four tools: sphincterotomy, extraction, dilation, stenting.",
            "The complication ledger and the two proven prophylaxes.",
        ],
        "standards": [
            "Technique terms follow standard endoscopy usage.",
            "Prophylaxis follows guideline-supported practice.",
            "Indication framing follows standard therapeutic-ERCP teaching.",
        ],
        "citations": [CIT_SLEIS, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: ERCP is sending a remote robot down the "
            "outfall to work the blockage from inside - cut the valve wider, "
            "sweep the scale out with a balloon, scaffold the crushed section "
            "with a stent. The neighboring enzyme plant sits at the same "
            "outfall, so the robot's wake can set it off - post-ERCP "
            "pancreatitis - and the Signature crew pre-medicates against "
            "exactly that. Diagnose with the camera outside the pipes "
            "(MRCP); send the robot only to fix."
        ),
    },
    {
        "key": "he",
        "name": "Hepatic Encephalopathy: Ammonia and the Brain",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Hepatic encephalopathy is liver failure thinking out loud: the "
            "spectrum from subtle inattention and sleep inversion through "
            "confusion, asterixis (the flapping tremor), and stupor to coma, "
            "graded 0 to 4 by West Haven. The driver is ammonia the failing "
            "liver cannot clear through the urea cycle, compounded by "
            "portosystemic shunting that bypasses the liver entirely - plus "
            "inflammation, which is why infection worsens it. Every episode "
            "has a precipitant to hunt: GI bleeding (a protein load), "
            "infection, diuretics and dehydration, constipation, sedatives, "
            "new shunting (TIPS). Treatment is precipitant-first, then "
            "ammonia-lowering: lactulose titrated to 2-3 soft stools daily "
            "(it acidifies the colon, trapping ammonia as ammonium), plus "
            "rifaximin to cut gut bacterial ammonia production for recurrent "
            "cases. Protein restriction is obsolete - the cirrhotic patient "
            "needs protein. Covert encephalopathy is tested with psychometric "
            "tools (the animal naming test, Stroop) and matters for driving "
            "and safety. This record covers the grades, the precipitants, "
            "and the ammonia trap."
        ),
        "how_it_works": (
            "The brain injury works on the ammonia-glutamine mechanism: "
            "astrocytes detoxify ammonia to glutamine, glutamine draws water "
            "osmotically, astrocytes swell, and neurotransmission derails - "
            "reversibly, which is why the patient can be comatose on Monday "
            "and lucid on Friday. Lactulose works as a colonic ammonia trap: "
            "fermented to acids, it drops colonic pH, converting absorbable "
            "ammonia (NH3) to non-absorbable ammonium (NH4+), while its "
            "laxative effect shortens bacterial contact time - dosed to the "
            "stool count, 2 to 3 soft stools a day. Rifaximin works by "
            "decimating ammonia-producing gut flora without systemic "
            "absorption. The precipitant hunt works because fixing the "
            "trigger - the bleed, the infection, the sedative - often clears "
            "the episode without changing liver function at all. The demo "
            "grades a worked case on the West Haven scale."
        ),
        "key_points": [
            "West Haven grades 0-4: inattention and sleep inversion through asterixis and confusion to coma.",
            "Ammonia plus shunting plus inflammation drive it; every episode has a precipitant - bleed, infection, drugs, dehydration.",
            "Lactulose titrated to 2-3 soft stools daily traps ammonia as ammonium in the colon.",
            "Rifaximin cuts bacterial ammonia production for recurrent episodes.",
            "Protein restriction is obsolete; covert encephalopathy is tested psychometrically and matters for driving.",
        ],
        "requirements": [
            "The five West Haven grades and the asterixis sign.",
            "The ammonia-glutamine mechanism and the precipitant list.",
            "Lactulose dosing logic and the rifaximin add-on rule.",
        ],
        "standards": [
            "Grading follows West Haven; mechanism follows standard teaching.",
            "Treatment follows standard practice (lactulose first, rifaximin for recurrence).",
            "Nutritional framing follows current guidance (no protein restriction).",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_ASCITES],
        "sig_lens": (
            "His Signature reading: encephalopathy is the town downstream "
            "getting poisoned because the waste-treatment train failed - "
            "ammonia the plant can no longer convert, shunted past the "
            "works entirely through relief tunnels, swelling the control "
            "room (astrocytes) until the operators cannot think. The fix is "
            "twofold and very Signature: find what tripped the episode (the "
            "bleed, the infection, the sedative) and trap the poison at the "
            "intake - lactulose turning the gut into an ammonia prison, "
            "rifaximin culling the poison-makers."
        ),
    },
]
ENTRIES += [
    {
        "key": "ascites",
        "name": "Ascites and Spontaneous Bacterial Peritonitis",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Ascites - fluid in the peritoneal cavity - is the commonest "
            "decompensating event of cirrhosis, and its workup is one needle "
            "and one subtraction. Diagnostic paracentesis is mandatory for "
            "new ascites: cell count, albumin, protein, culture. The serum-"
            "ascites albumin gradient (SAAG) - serum albumin minus ascitic "
            "albumin - splits the world: 1.1 g/dL or above means portal "
            "hypertension is driving it (cirrhosis, heart failure, Budd-"
            "Chiari); below means it is not (malignancy, tuberculosis, "
            "pancreatic). Management is salt restriction, diuretics "
            "(spironolactone first, furosemide added, classically 100:40), "
            "and large-volume paracentesis with albumin cover for tense or "
            "refractory cases. Spontaneous bacterial peritonitis is the "
            "dreaded infection of the fluid: fever, pain, or just "
            "encephalopathy - diagnosed at 250 neutrophils per microliter or "
            "more, treated with cefotaxime plus albumin (which cuts the "
            "hepatorenal risk), and followed by lifelong secondary "
            "prophylaxis. This record covers the tap, the gradient, and the "
            "infection."
        ),
        "how_it_works": (
            "Ascites works on Starling forces plus sodium retention: portal "
            "hypertension raises sinusoidal hydrostatic pressure, splanchnic "
            "vasodilation drops effective arterial volume, the kidney reads "
            "hypovolemia and retains sodium and water via the renin-angiotensin "
            "system - fluid weeps into the peritoneum faster than lymphatics "
            "can return it. The SAAG works because albumin equilibrates "
            "across the peritoneum except for the hydrostatic push of portal "
            "hypertension: a wide gradient proves the push exists. Diuretics "
            "work on the kidney's sodium retention - spironolactone blocking "
            "aldosterone first because secondary hyperaldosteronism dominates. "
            "SBP works as bacterial translocation: gut bacteria cross the "
            "edematous wall into ascitic fluid with no immune defense; "
            "albumin with antibiotics works by expanding volume and binding "
            "inflammatory mediators. The demo computes the SAAG on a worked "
            "case and applies the 1.1 threshold."
        ),
        "key_points": [
            "New ascites demands diagnostic paracentesis: cell count, albumin, protein, culture.",
            "SAAG >= 1.1 g/dL proves portal hypertension is driving the fluid; below points to malignancy, TB, pancreas.",
            "Management: salt restriction, spironolactone then furosemide (100:40), large-volume tap with albumin for refractory.",
            "SBP diagnosed at >= 250 neutrophils/mcL; treated with cefotaxime plus albumin, then lifelong prophylaxis.",
            "Ascites is decompensation: it starts the transplant-evaluation clock.",
        ],
        "requirements": [
            "The paracentesis panel and the SAAG formula with its 1.1 split.",
            "The diuretic sequence and the albumin-cover rule for large taps.",
            "SBP diagnosis, treatment, and secondary prophylaxis.",
        ],
        "standards": [
            "Thresholds follow standard AASLD practice guidance.",
            "Drug sequencing follows standard cirrhosis care.",
            "SBP criteria follow the standard neutrophil cutoff.",
        ],
        "citations": [CIT_ASCITES, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: ascites is the plant weeping - back-"
            "pressure forcing fluid through the vessel walls faster than the "
            "drains can return it, while the water utility (the kidney), "
            "fooled by the pressure drop, keeps pumping more in. The SAAG is "
            "the leak-forensics test: a wide gradient proves the weeping is "
            "pressure-driven. SBP is contamination of the pooled water - "
            "bacteria crossing a flooded intake wall into undefended fluid - "
            "and the Signature response is antibiotics plus volume support, "
            "then permanent guard duty against the next breach."
        ),
    },
    {
        "key": "hrs",
        "name": "Hepatorenal Syndrome and the Kidney in Liver Failure",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "In hepatorenal syndrome the kidneys are innocent: structurally "
            "normal organs failing because the cirrhotic circulation has "
            "abandoned them. Splanchnic vasodilation drops effective arterial "
            "volume; the kidney vasoconstricts to hold pressure; filtration "
            "falls. The International Club of Ascites criteria define HRS-AKI: "
            "cirrhosis with ascites, AKI by the standard rise (creatinine up "
            "0.3 mg/dL in 48 hours or 50 percent in 7 days), no response to "
            "diuretic withdrawal and albumin volume expansion, no shock, no "
            "recent nephrotoxin, no parenchymal kidney disease (proteinuria, "
            "hematuria, abnormal ultrasound all argue against). Treatment is "
            "vasoconstrictors plus albumin: terlipressin where available, "
            "norepinephrine in the ICU, or midodrine with octreotide on the "
            "ward - all aiming to reverse the splanchnic vasodilation and "
            "reperfuse the kidney. Response can be dramatic and is the bridge "
            "to transplant; without transplant, relapse is the rule. "
            "Dialysis is a bridge, not a destination. This record covers the "
            "innocent kidney and its rescue."
        ),
        "how_it_works": (
            "The syndrome works as circulatory theft: portal hypertension "
            "vasodilates the splanchnic bed via nitric oxide, effective "
            "arterial blood volume falls, baroreceptors fire the renin-"
            "angiotensin and sympathetic systems, and the renal arteries clamp "
            "down - filtration sacrificed to preserve systemic pressure. The "
            "diagnosis works by exclusion because no test proves it: volume-"
            "expand with albumin, withdraw diuretics and nephrotoxins, and if "
            "creatinine still will not fall and the urine is bland, the "
            "kidneys are victims, not culprits. Vasoconstrictors work by "
            "reversing the theft at its source: terlipressin constricts the "
            "splanchnic bed, effective volume returns, renal vasoconstriction "
            "releases, creatinine falls. Transplant works definitively "
            "because a new liver normalizes the circulation - the kidneys, "
            "never diseased, recover fully. The demo applies the AKI rise "
            "criteria to a worked creatinine series."
        ),
        "key_points": [
            "HRS = structurally normal kidneys failing from the cirrhotic circulation's splanchnic vasodilation.",
            "HRS-AKI criteria: AKI rise, no response to albumin volume expansion, no shock, no nephrotoxin, bland urine.",
            "Treatment: vasoconstrictor (terlipressin, norepinephrine, or midodrine+octreotide) plus albumin.",
            "The kidneys recover fully after liver transplant - the definitive cure.",
            "Dialysis bridges to transplant; it does not treat the syndrome.",
        ],
        "requirements": [
            "The circulatory mechanism: why the kidney vasoconstricts.",
            "The ICA diagnostic criteria as an exclusion ladder.",
            "The three vasoconstrictor regimens and the transplant cure.",
        ],
        "standards": [
            "Criteria follow the International Club of Ascites definitions.",
            "AKI thresholds follow the standard creatinine-rise rule.",
            "Treatment options follow standard practice by setting.",
        ],
        "citations": [CIT_ASCITES, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: hepatorenal syndrome is the water utility "
            "shutting its own valves because the main plant's pressure "
            "collapse fooled its sensors - the utility itself is undamaged, "
            "the pipes are clean, but the control logic starves the town to "
            "save the system. The Signature rescue does not replumb the "
            "utility; it fixes the pressure lie at the source - constrict the "
            "runaway bypass (the splanchnic bed), restore effective volume, "
            "and the utility's valves reopen on their own. Replace the main "
            "plant (transplant) and the utility never knew it was sick."
        ),
    },
    {
        "key": "meld",
        "name": "The MELD and Child-Pugh Scores: Predicting Liver Outcomes",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Two scores run liver prognostication. The Child-Pugh score - "
            "five elements (bilirubin, albumin, INR, ascites, encephalopathy), "
            "each 1 to 3 points, classes A (5-6), B (7-9), C (10-15) - is the "
            "bedside classic: A means compensated, C means decompensated, "
            "and surgical risk climbs steeply across the classes. The MELD "
            "score - 3.78 times the natural log of bilirubin plus 11.2 times "
            "ln(INR) plus 9.57 times ln(creatinine) plus 6.43, rounded - is "
            "the objective allocator: in the United States it ranks the "
            "transplant waitlist, because it predicts 90-day mortality "
            "without transplant, and MELD-Na adds sodium for the dilutional "
            "hyponatremia of advanced cirrhosis. A MELD of 6 is normal; 40 is "
            "the ceiling; each few points carry a meaning patients feel. "
            "Both scores are used far beyond their origins - Child-Pugh for "
            "operative risk, MELD for any short-term prognosis. This record "
            "teaches both formulas and what the numbers mean at the bedside."
        ),
        "how_it_works": (
            "Child-Pugh works as a compensated-to-decompensated ruler: the "
            "two lab synthesis markers (albumin, INR), the waste marker "
            "(bilirubin), and the two clinical decompensations (ascites, "
            "encephalopathy) each scored 1 to 3 - the sum sorts the patient "
            "into a class the surgeon can quote. MELD works as a mortality "
            "equation: the logarithms compress the wide ranges of bilirubin, "
            "INR, and creatinine into a single number calibrated against "
            "observed 90-day death rates, which is why it allocates organs - "
            "the sickest first, objectively. Sodium was added because "
            "hyponatremia independently predicts death in cirrhosis. The "
            "scores are never the whole patient - frailty, infection, and "
            "trajectory modify everything - but no hepatology decision about "
            "prognosis or listing happens without them. The demo computes "
            "MELD on a worked lab set."
        ),
        "key_points": [
            "Child-Pugh: 5 elements scored 1-3; classes A/B/C = compensated to decompensated; guides operative risk.",
            "MELD = 3.78 ln(bilirubin) + 11.2 ln(INR) + 9.57 ln(creatinine) + 6.43; predicts 90-day mortality.",
            "MELD ranks the US transplant waitlist - sickest first, by objective number.",
            "MELD-Na adds sodium for the dilutional hyponatremia of advanced cirrhosis.",
            "The scores frame prognosis; frailty and trajectory complete the picture.",
        ],
        "requirements": [
            "The five Child-Pugh elements and the A/B/C bands.",
            "The MELD formula and the waitlist-allocation principle.",
            "What MELD-Na adds and why.",
        ],
        "standards": [
            "Formulas follow the original Child-Pugh and MELD publications.",
            "Score ranges stated as standard integers.",
            "Allocation framing follows the standard sickest-first principle.",
        ],
        "citations": [CIT_MELD, CIT_CHILDPUGH, CIT_TRANSPLANT],
        "sig_lens": (
            "His Signature reading: Child-Pugh is the plant inspector's "
            "five-point checklist - two production gauges, one waste gauge, "
            "two flood reports - summed into a grade the whole industry "
            "understands. MELD is the triage equation: three log-compressed "
            "gauges fused into one number that predicts how many days the "
            "plant has left, and the replacement queue is ordered by exactly "
            "that number - the most failing first, no politics, just the "
            "math. Sodium joined the equation because dilution tells its own "
            "truth about how far the flood has risen."
        ),
    },
    {
        "key": "hcc",
        "name": "Hepatocellular Carcinoma: Surveillance and Treatment",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hepatocellular carcinoma is the cancer that grows in scar: "
            "nearly all cases arise in cirrhosis or chronic hepatitis B, and "
            "worldwide it is among the top causes of cancer death. "
            "Surveillance is the standard for at-risk patients - ultrasound "
            "with or without alpha-fetoprotein every six months - because "
            "curative treatment only exists for early disease found on time. "
            "Diagnosis in cirrhosis is usually radiologic, not biopsy: "
            "arterial-phase hyperenhancement with portal-venous washout on "
            "multiphase CT or MRI (LI-RADS) is diagnostic. Treatment follows "
            "the Barcelona Clinic Liver Cancer staging: very early and early "
            "disease get resection, ablation (radiofrequency or microwave), "
            "or transplant - the Milan criteria (one lesion 5 cm or less, or "
            "up to three lesions 3 cm or less) still gate transplant listing; "
            "intermediate disease gets TACE (transarterial chemoembolization); "
            "advanced disease gets systemic therapy - atezolizumab plus "
            "bevacizumab first line, then tyrosine kinase inhibitors. "
            "Prevention is treating the cause: HBV vaccination and antivirals, "
            "HCV cure, alcohol abstinence, MASLD control. This record covers "
            "the surveillance net and the stage-driven arsenal."
        ),
        "how_it_works": (
            "The cancer works on chronic regeneration: decades of injury and "
            "repair mutate hepatocytes, dysplastic nodules progress, and "
            "arterial neovascularization feeds the tumor - which is why the "
            "diagnostic signature is arterial hyperenhancement (tumor fed by "
            "artery) with washout (surrounding liver still portal-fed). "
            "Surveillance works because the doubling time gives a six-month "
            "window: catch it under 2-3 centimeters and ablation or resection "
            "cures. TACE works by selective starvation: chemotherapy plus "
            "embolic particles delivered into the tumor's hepatic-artery "
            "branches, exploiting the arterial-only supply. Immunotherapy "
            "plus anti-VEGF works by unmasking the tumor to the immune system "
            "while pruning its blood supply. The demo applies the Milan "
            "criteria to worked nodule sets."
        ),
        "key_points": [
            "HCC grows in cirrhosis or chronic HBV; surveillance is ultrasound +/- AFP every 6 months.",
            "Diagnosis in cirrhosis is radiologic: arterial hyperenhancement with washout (LI-RADS).",
            "Milan criteria gate transplant: 1 lesion <= 5 cm or up to 3 lesions <= 3 cm.",
            "Treatment is stage-driven: resection/ablation/transplant, then TACE, then systemic (atezolizumab+bevacizumab).",
            "Prevention is cause-treatment: HBV vaccine and antivirals, HCV cure, abstinence, metabolic control.",
        ],
        "requirements": [
            "The at-risk population and the surveillance interval.",
            "The radiologic diagnostic signature and why it works.",
            "Milan criteria and the BCLC treatment ladder.",
        ],
        "standards": [
            "Criteria follow Milan and BCLC as standard.",
            "Surveillance follows standard 6-month practice.",
            "Systemic therapy lines follow current standard sequencing.",
        ],
        "citations": [CIT_HCC, CIT_SCHIFF, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: HCC is what grows in a reaction bed that "
            "has been damaged and repaired ten thousand times - mutations "
            "accumulating in the maintenance logs until one unit goes rogue "
            "and starts building its own blood supply. Surveillance is the "
            "scheduled inspection that catches the rogue unit small enough to "
            "cut out. The Milan rule is the replacement-plant eligibility "
            "spec: small enough burden, and the new plant is worth the organ. "
            "TACE is siege warfare - starve the rogue unit through its "
            "private supply line. And the Signature prevention order stands: "
            "fix the chronic damage and the rogue units never get their "
            "chance."
        ),
    },
    {
        "key": "cholangio",
        "name": "Cholangiocarcinoma and Biliary Cancers",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Cholangiocarcinoma - cancer of the bile ducts - is the "
            "hepatologist's feared zebra: rare, rising, and usually late. It "
            "divides by anatomy: intrahepatic (within the liver, a liver mass "
            "like HCC but without the cirrhosis), perihilar or Klatskin "
            "(at the duct confluence - the commonest, about half to "
            "three-fifths of cases), and distal (near the ampulla). PSC is "
            "the classic risk factor, with liver flukes in endemic regions "
            "and choledochal cysts completing the list. Presentation is "
            "painless progressive jaundice with a dilated upstream ductal "
            "system and a stricture that will not let a wire through easily. "
            "Diagnosis blends MRCP, endoscopic sampling (brush cytology is "
            "insensitive; cholangioscopy-guided biopsy is better), and CA19-9 "
            "with its caveats. Only surgery cures - major hepatectomy for "
            "intrahepatic, bile-duct resection with hepaticojejunostomy for "
            "perihilar - and most patients are unresectable at presentation, "
            "leaving stenting for drainage plus chemotherapy (gemcitabine-"
            "cisplatin, now with immunotherapy). Gallbladder cancer, often "
            "found incidentally after cholecystectomy, completes the biliary "
            "cancer family. This record maps the ductal cancers and their "
            "narrow curative window."
        ),
        "how_it_works": (
            "The cancer works on chronic biliary inflammation: PSC's "
            "relentless stricturing, fluke infestation, or cyst-related "
            "stasis mutates cholangiocytes over years - which is why "
            "surveillance in PSC hunts it with scheduled MRCP. Obstruction "
            "works mechanically: the tumor narrows the duct, upstream ducts "
            "dilate, conjugated bilirubin backs into blood - painless "
            "jaundice with a palpable gallbladder (Courvoisier's law: a "
            "palpable gallbladder with jaundice is unlikely to be stones). "
            "Drainage works palliatively: metal stents hold the malignant "
            "stricture open, bilirubin falls, cholangitis risk drops, and "
            "chemotherapy becomes deliverable. Resectability works on "
            "anatomy: clear vascular margins and enough future liver remnant - "
            "perihilar tumors fail on vascular involvement. The demo works "
            "the anatomic distribution: perihilar share of a worked case "
            "series."
        ),
        "key_points": [
            "Cholangiocarcinoma divides into intrahepatic, perihilar (Klatskin, commonest), and distal.",
            "PSC is the classic Western risk factor; flukes dominate in endemic regions.",
            "Painless progressive jaundice with upstream dilation is the presentation; Courvoisier's law applies.",
            "Only surgery cures; most present unresectable - stenting plus gemcitabine-cisplatin-based chemotherapy follows.",
            "PSC patients need lifelong cholangiocarcinoma surveillance with MRCP.",
        ],
        "requirements": [
            "The three anatomic subtypes and their relative frequency.",
            "The risk-factor list and the presentation pattern.",
            "The curative vs palliative split and what decides it.",
        ],
        "standards": [
            "Anatomy and naming follow standard usage (Klatskin, perihilar).",
            "Risk factors follow standard teaching.",
            "Treatment framing follows standard practice.",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: cholangiocarcinoma is cancer growing in "
            "the outflow pipes themselves - usually where chronic irritation "
            "has been sanding the same section for years. It announces itself "
            "the way any crushed main does: product backing up upstream, the "
            "whole system yellowing. The curative fix is to cut out the "
            "ruined section and replumb - possible only when the damage is "
            "local and the margins are clean. Otherwise the Signature crew "
            "does what it can: scaffold the crushed main open, keep the "
            "product flowing, and fight the growth systemically."
        ),
    },
    {
        "key": "panc_cancer",
        "name": "Pancreatic Cancer: Detection and Management",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Pancreatic ductal adenocarcinoma is the bleakest of the HPB "
            "cancers: usually silent until late, usually unresectable at "
            "diagnosis, with five-year survival in the low single digits for "
            "metastatic disease. It favors the head of the gland, where it "
            "blocks the bile duct early - painless jaundice again - and the "
            "pancreatic duct, causing upstream dilation (the double-duct "
            "sign). Risk factors: smoking, chronic pancreatitis, long-"
            "standing diabetes, family history and germline mutations (BRCA2, "
            "PALB2, Lynch, PRSS1 families). There is no population screening; "
            "high-risk individuals get surveillance with MRI/MRCP and "
            "endoscopic ultrasound. Diagnosis is EUS with fine-needle biopsy "
            "plus staging CT. Resectability is anatomic: no arterial "
            "involvement (celiac, SMA), limited venous involvement - the "
            "borderline category gets neoadjuvant chemotherapy first. The "
            "Whipple procedure (pancreaticoduodenectomy) resects head lesions; "
            "distal pancreatectomy takes body and tail. Adjuvant modified "
            "FOLFIRINOX after resection is the standard that moved survival. "
            "This record covers the detection problem and the resectability "
            "verdict."
        ),
        "how_it_works": (
            "The cancer works by silent infiltration: a desmoplastic stroma "
            "walls it off from drugs and immune cells while it wraps vessels "
            "early - which is why anatomy, not size, decides resectability. "
            "The double-duct sign works diagnostically: one lesion blocking "
            "both the bile duct and the pancreatic duct is a head mass until "
            "proven otherwise. EUS works by proximity: the echoendoscope in "
            "the duodenum sits millimeters from the pancreatic head, imaging "
            "and needling lesions CT cannot characterize. Neoadjuvant therapy "
            "works by selection and shrinkage: borderline tumors that respond "
            "prove their biology before the surgeon commits to a Whipple. "
            "Adjuvant FOLFIRINOX works by mopping micrometastases - the "
            "reason resection alone was never enough. The demo applies the "
            "resectability rule to worked vessel-involvement cases."
        ),
        "key_points": [
            "Pancreatic cancer is usually silent until late; the head location gives painless jaundice via bile-duct blockage.",
            "The double-duct sign (dilated bile duct plus dilated pancreatic duct) points to a head mass.",
            "Resectability is anatomic: arterial involvement rules it out; limited venous involvement is borderline.",
            "EUS with fine-needle biopsy is the diagnostic standard; staging is CT.",
            "Adjuvant modified FOLFIRINOX after resection is the survival-moving standard.",
        ],
        "requirements": [
            "Why anatomy, not size, decides resectability.",
            "The double-duct sign and the EUS diagnostic role.",
            "The treatment sequence: neoadjuvant, Whipple/distal, adjuvant.",
        ],
        "standards": [
            "Resectability criteria follow standard anatomic teaching.",
            "Surveillance framing follows high-risk guidelines.",
            "Chemotherapy regimens named as current standards.",
        ],
        "citations": [CIT_HARRISON, CIT_SLEIS, CIT_SCHIFF],
        "sig_lens": (
            "His Signature reading: pancreatic cancer is the stealth failure "
            "in the enzyme plant next door - no alarms until it has wrapped "
            "the great vessels, because the plant sits deep and quiet. The "
            "double-duct sign is the giveaway: one mass choking both the "
            "neighbor's outflow and the refinery's own bile main. The "
            "resectability verdict is pure Signature engineering - can the "
            "ruined section be cut out with clean margins on the load-bearing "
            "vessels? If yes, cut and follow with systemic cleanup; if the "
            "vessels are wrapped, the plant cannot be saved by steel."
        ),
    },
]
ENTRIES += [
    {
        "key": "transplant",
        "name": "Liver Transplantation: Evaluation, Surgery, and Immunosuppression",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Liver transplantation is the definitive therapy for end-stage "
            "liver disease and acute liver failure: the only treatment that "
            "replaces the organ. Evaluation is multidisciplinary and "
            "unsparing - cardiopulmonary fitness, malignancy screening, "
            "infection screening, renal function, nutrition, substance use, "
            "and psychosocial support - because organs are scarce and the "
            "operation is among surgery's biggest. Listing is by MELD (and "
            "status 1A for acute failure); exceptions grant extra points for "
            "conditions MELD undervalues, like HCC within Milan or "
            "hepatopulmonary syndrome. The surgery has three acts: hepatectomy "
            "of the diseased liver, the anhepatic phase (no liver - clotting, "
            "glucose, and hemodynamics hand-managed), and implantation with "
            "vascular and biliary anastomoses. Immunosuppression is "
            "calcineurin-inhibitor based - tacrolimus - with mycophenolate "
            "and steroids tapering: enough to prevent rejection, little "
            "enough to limit infection, kidney injury, diabetes, and "
            "malignancy. One-year survival exceeds 90 percent at experienced "
            "centers; the long game is managing the metabolic and renal "
            "costs of lifelong immunosuppression. Living-donor transplantation "
            "expands the pool where deceased donation is scarce. This record "
            "covers the evaluation gauntlet, the operation, and the lifelong "
            "aftermath."
        ),
        "how_it_works": (
            "Allocation works on sickest-first objectivity: MELD orders the "
            "list, status 1A jumps acute failure to the front, and exception "
            "points correct the score's blind spots - a system built to be "
            "auditable. The operation works on vascular plumbing at scale: "
            "vena cava, portal vein, hepatic artery, and bile duct "
            "reconnected in sequence, with the anhepatic phase demanding "
            "minute-to-minute management of coagulation and metabolism. "
            "Immunosuppression works by T-cell blockade: tacrolimus inhibits "
            "calcineurin, silencing interleukin-2 transcription, and rejection "
            "- usually cellular, usually in the first months - is read on "
            "liver enzymes and confirmed on biopsy, then treated with steroid "
            "pulses. Tolerance is the dream; minimization is the practice: "
            "the lowest doses that hold rejection off while kidneys, "
            "metabolism, and infection risk survive. The demo works the ABO "
            "compatibility matrix for donor-recipient matching."
        ),
        "key_points": [
            "Transplant is the definitive therapy for end-stage disease and acute liver failure.",
            "Listing is by MELD (sickest first); status 1A covers acute failure; exceptions correct blind spots.",
            "The operation: hepatectomy, anhepatic phase, implantation - vascular and biliary replumbing at scale.",
            "Immunosuppression is tacrolimus-based T-cell blockade, minimized over time against infection, renal, and metabolic costs.",
            "One-year survival exceeds 90 percent at experienced centers; living donation expands the pool.",
        ],
        "requirements": [
            "The evaluation domains and why each gates listing.",
            "The allocation logic: MELD, 1A, exceptions.",
            "The immunosuppression strategy and its long-term costs.",
        ],
        "standards": [
            "Allocation framing follows the standard MELD-based system.",
            "Drug names follow standard transplant immunosuppression.",
            "Survival figures stated as standard center-level outcomes.",
        ],
        "citations": [CIT_TRANSPLANT, CIT_MELD, CIT_SCHIFF],
        "sig_lens": (
            "His Signature reading: transplantation is the full plant "
            "replacement - the Signature works' ultimate work order. The "
            "evaluation is the pre-shutdown audit: every system checked, "
            "because the new plant deserves a site that can run it. The "
            "queue is pure triage math, the most failing first. The operation "
            "is the hot-swap: old refinery out, donor refinery plumbed in - "
            "four great pipes reconnected under time pressure. Then the "
            "lifelong lease: drugs that keep the site's security from "
            "rejecting the new plant, dosed to the minimum that holds the "
            "peace."
        ),
    },
    {
        "key": "pediatric",
        "name": "Pediatric Hepatology: Biliary Atresia and Inherited Disease",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Children's liver disease is its own world, and its clock runs "
            "fast. Biliary atresia - the extrahepatic bile ducts obliterated "
            "in the newborn - is the commonest indication for pediatric liver "
            "transplant: the infant is jaundiced past two weeks of age with "
            "pale stools and dark urine, and the Kasai portoenterostomy "
            "(connecting the liver's porta hepatis directly to the bowel) "
            "must happen early - outcomes fall steeply after 60 to 90 days, "
            "so every jaundiced two-week-old gets a fractionated bilirubin. "
            "Inherited diseases fill the rest: alpha-1 antitrypsin deficiency "
            "(the commonest genetic cause of pediatric liver disease, PiZZ), "
            "Wilson disease in the older child, progressive familial "
            "intrahepatic cholestasis (PFIC) types with their transporter "
            "defects, Alagille syndrome (ductal paucity with the characteristic "
            "facies, butterfly vertebrae, cardiac disease), and neonatal "
            "hemochromatosis (now understood as gestational alloimmune liver "
            "disease). Pediatric transplant - often living-donor or split-"
            "liver - has superb outcomes, and transition to adult care is "
            "itself a managed process. This record covers the neonatal "
            "emergency and the inherited catalog."
        ),
        "how_it_works": (
            "Biliary atresia works as progressive fibro-obliteration: the "
            "extrahepatic ducts scar shut in the first weeks of life, bile "
            "cannot leave, and the liver cirrhoses within months - which is "
            "why the clock is everything. The Kasai works as a salvage "
            "plumbing bypass: the scarred ducts are excised and a loop of "
            "jejunum is sewn to the porta hepatis, draining microscopic "
            "ductules directly - success measured by bilirubin falling and "
            "stools pigmenting, best when done before 60 days. The inherited "
            "diseases work as single-gene breaks in the refinery's machinery: "
            "misfolded alpha-1 antitrypsin polymerizing in hepatocytes, "
            "ATP7B failing copper export, bile-acid transporters (BSEP, MDR3) "
            "broken in PFIC. Diagnosis works on pattern plus gene: "
            "cholestasis with low GGT points to transporter defects. The demo "
            "works the Kasai clock: days remaining in the optimal window from "
            "a worked presentation age."
        ),
        "key_points": [
            "Biliary atresia: jaundice past 2 weeks with pale stools is the neonatal emergency; Kasai before 60-90 days.",
            "Kasai portoenterostomy bypasses the obliterated ducts by sewing bowel to the porta hepatis.",
            "Alpha-1 antitrypsin deficiency (PiZZ) is the commonest genetic cause of pediatric liver disease.",
            "PFIC, Alagille, Wilson, and gestational alloimmune disease complete the inherited catalog.",
            "Pediatric transplant (living-donor/split) has superb outcomes; transition to adult care is managed.",
        ],
        "requirements": [
            "The biliary atresia presentation and the Kasai timing rule.",
            "The inherited catalog: gene, mechanism, clue for each.",
            "Why low-GGT cholestasis points to transporter defects.",
        ],
        "standards": [
            "Timing thresholds follow standard pediatric hepatology teaching.",
            "Disease names and genes follow standard usage.",
            "Transplant framing follows standard pediatric practice.",
        ],
        "citations": [CIT_SCHIFF, CIT_HARRISON, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: pediatric hepatology is commissioning "
            "inspection on a brand-new plant - and biliary atresia is the "
            "outfall pipes sealed shut at the factory, a defect that destroys "
            "the new refinery in months unless the crew replumbs it in the "
            "first sixty days. The inherited diseases are blueprint errors: a "
            "protein that misfolds and clogs the works (alpha-1), an export "
            "pump never installed (Wilson), intake valves built wrong (PFIC). "
            "Read the blueprint (the gene), name the defect, and for the "
            "sealed outfall, move fast - the Signature rule for newborn "
            "plants: jaundice past two weeks is never watched, it is worked "
            "up."
        ),
    },
    {
        "key": "pregnancy",
        "name": "Pregnancy and the Liver: AFLP, HELLP, and Cholestasis",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pregnancy stresses the liver, and three disorders belong to "
            "pregnancy alone. Intrahepatic cholestasis of pregnancy (ICP) "
            "brings tormenting itching, usually in the third trimester, with "
            "raised bile acids - above 40 micromoles per liter marking higher "
            "fetal risk - treated with ursodeoxycholic acid and timed "
            "delivery. HELLP syndrome - hemolysis, elevated liver enzymes, "
            "low platelets - complicates preeclampsia: the Mississippi "
            "classification grades it by platelet count (class 1 under 50,000 "
            "per microliter), and delivery is the treatment, with hepatic "
            "rupture the feared catastrophe. Acute fatty liver of pregnancy "
            "(AFLP) is the emergency: third-trimester liver failure from a "
            "fetal fatty-acid oxidation defect poisoning the mother, diagnosed "
            "by the Swansea criteria, treated by prompt delivery - maternal "
            "and fetal mortality that once was appalling is now low with "
            "early recognition. Hyperemesis gravidarum can raise enzymes "
            "mildly. The rule over everything: a sick liver in late pregnancy "
            "is delivered, not debated - the fetus is the removable cause. "
            "This record covers the three pregnancy-specific disorders and "
            "the delivery rule."
        ),
        "how_it_works": (
            "ICP works as hormone-exaggerated cholestasis: estrogen and "
            "progesterone metabolites impair bile-acid transport in "
            "susceptible women, bile acids rise, the mother itches, and high "
            "levels threaten the fetus - ursodeoxycholic acid improves flow "
            "and symptoms while the clock runs to delivery. HELLP works as "
            "microangiopathy: endothelial injury shears red cells, consumes "
            "platelets, and infarcts the liver - delivery removes the "
            "placental driver. AFLP works as a metabolic collision: the fetus "
            "with long-chain 3-hydroxyacyl-CoA dehydrogenase deficiency "
            "cannot oxidize fatty acids, toxic intermediates flood the "
            "mother, and her liver fills with microvesicular fat and fails - "
            "delivery removes the source. The Swansea criteria work as a "
            "checklist diagnosis (six or more of fourteen features) because "
            "biopsy is too slow for a dying liver. The demo applies the "
            "Mississippi HELLP classes to worked platelet counts."
        ),
        "key_points": [
            "ICP: third-trimester itching with raised bile acids; UDCA plus timed delivery; bile acids >40 mark fetal risk.",
            "HELLP: hemolysis, elevated enzymes, low platelets in preeclampsia; Mississippi classes by platelet count; delivery treats.",
            "AFLP: third-trimester liver failure from fetal fatty-acid oxidation defect; Swansea criteria; prompt delivery.",
            "Hepatic rupture is the feared HELLP catastrophe.",
            "The rule: a sick liver in late pregnancy is delivered, not debated.",
        ],
        "requirements": [
            "The three disorders: trigger, marker, treatment for each.",
            "Mississippi classes and the Swansea checklist concept.",
            "The delivery rule and its rationale.",
        ],
        "standards": [
            "Criteria follow Mississippi and Swansea as standard.",
            "Thresholds stated as standard clinical cutoffs.",
            "Management follows standard obstetric-hepatology practice.",
        ],
        "citations": [CIT_HARRISON, CIT_SCHIFF, CIT_SLEIS],
        "sig_lens": (
            "His Signature reading: pregnancy is the refinery running a "
            "second shift for a new plant under construction next door - and "
            "three failure modes belong to the double load alone. ICP is the "
            "solvent lines backing up under hormonal surge: itch, rising bile "
            "acids, managed with flow improvers until the shift ends "
            "(delivery). HELLP is the pressure system shearing its own "
            "workforce - red cells shredded, platelets consumed, the liver "
            "infarcting. AFLP is the new plant's broken metabolism poisoning "
            "the mother works. The Signature order for all three is the same "
            "and absolute: end the double shift - deliver - because the "
            "removable cause is the pregnancy itself."
        ),
    },
    {
        "key": "future",
        "name": "The Future of Hepatology: NASH Therapies, Artificial Liver, and Precision Transplantation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hepatology's future is being written on three fronts. First, "
            "the drug pipeline for MASH: resmetirom - a thyroid hormone "
            "receptor-beta agonist - became the first approved therapy for "
            "MASH with moderate to advanced fibrosis, and GLP-1 agonists, "
            "FGF21 analogues, and combination regimens crowd behind it, "
            "aiming at what lifestyle alone could not fix at population "
            "scale. Second, artificial liver support: albumin dialysis "
            "(MARS), plasma exchange, and bioartificial devices bridge acute "
            "liver failure and acute-on-chronic failure toward recovery or "
            "transplant - the field still hunting the dialysis-equivalent "
            "breakthrough the kidney got decades ago. Third, precision "
            "transplantation: machine perfusion (normothermic and "
            "hypothermic) resuscitates marginal donor livers and expands the "
            "pool; xenotransplantation inches forward; immunosuppression "
            "minimization and tolerance protocols aim to free recipients "
            "from lifelong drugs. Underneath it all, noninvasive fibrosis "
            "staging and liquid biopsy for HCC surveillance promise to find "
            "disease earlier and gentler. This record closes the ladder "
            "looking forward."
        ),
        "how_it_works": (
            "Resmetirom works as selective thyroid hormone receptor-beta "
            "agonism in the liver: it raises hepatic fat metabolism and "
            "lowers lipotoxicity without the systemic thyroid effects, and "
            "trials showed MASH resolution and fibrosis improvement. Machine "
            "perfusion works by keeping the donor liver alive outside the "
            "body - warm oxygenated blood (normothermic) or cold oxygenated "
            "solution (hypothermic) - so marginal organs can be tested, "
            "repaired, and transplanted instead of discarded. Artificial "
            "support works as a bridge: removing albumin-bound toxins and "
            "water-soluble waste buys the failing liver days to regenerate "
            "or the patient days to reach transplant. Tolerance protocols "
            "work by retraining the immune system - mixed chimerism, "
            "regulatory T-cell therapy - toward accepting the graft without "
            "drugs. The demo projects transplant demand growth from a worked "
            "baseline, the arithmetic behind the organ-shortage urgency."
        ),
        "key_points": [
            "Resmetirom is the first approved MASH therapy; GLP-1s, FGF21 analogues, and combos follow.",
            "Machine perfusion (normothermic/hypothermic) rescues marginal donor livers and expands the pool.",
            "Artificial liver support bridges failure toward recovery or transplant - the dialysis-equivalent is still the prize.",
            "Tolerance protocols aim to end lifelong immunosuppression.",
            "Noninvasive staging and liquid biopsy promise earlier, gentler detection.",
        ],
        "requirements": [
            "The three fronts and the lead advance on each.",
            "How resmetirom and machine perfusion work mechanistically.",
            "Why the organ shortage drives the engineering.",
        ],
        "standards": [
            "Drug and device names follow current standard usage.",
            "Trial outcomes stated qualitatively as reported.",
            "Forward-looking claims framed as directions, not promises.",
        ],
        "citations": [CIT_AASLD_MASLD, CIT_TRANSPLANT, CIT_SCHIFF],
        "sig_lens": (
            "His Signature reading: the future of the refinery works is "
            "threefold - chemistry that finally melts the fat overflow "
            "(resmetirom and its successors), life-support rigs that keep a "
            "failing plant's town alive while the plant reboots (artificial "
            "liver), and a bigger, smarter replacement pipeline: donor "
            "plants resuscitated on perfusion rigs instead of discarded, and "
            "recipients taught to accept the new plant without a lifetime of "
            "security drugs. The Signature works never stop at the current "
            "spec - every record in this database is a baseline the future "
            "builds past."
        ),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == sorted(e["ladder_rank"] for e in ENTRIES), "ladder ranks must be non-decreasing"
