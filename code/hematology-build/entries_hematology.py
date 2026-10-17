#!/usr/bin/env python3
"""Entries for the Hematology field databases (field #40, taxonomy order).

Verified 2026-10-17: NO database covers hematology as a clinical specialty
(blood and blood-forming organs - anemias, hemoglobinopathies, leukemias,
lymphomas, myeloma, bleeding and clotting disorders, transfusion medicine,
bone marrow, CBC interpretation, the coagulation cascade).
Clinical-specialty framing, blood-focused, distinct from oncology (general
cancer) and immunology (the immune system).

Manifest search (2,380 databases): zero 'hematolog*' slugs/names; no
db/hematolog* dirs. Whole-system exact-title sweep over the manifest PLUS
all 779 shard index 't' keys (1,130,197 rows): zero collisions for all 34
planned titles x2 editions (68 variants). Near-neighbors confirmed
different disciplines: 'medical-diagnostics-study' holds only formulaic
"Signature Study of Hematology testing: ..." study-format records (a
different discipline - study methodology, not the clinical specialty);
'oncology' covers general cancer; 'immunology' covers the immune system.
ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  hematology                 - The Hematology Database
                               (public-harvest: real, fact-checked clinical
                               hematology; standard references Kaushansky et
                               al. "Williams Hematology" 10th ed 2021;
                               Hoffman et al. "Hematology: Basic Principles
                               and Practice" 8th ed 2023; Hoffbrand and
                               Moss "Hoffbrand's Essential Haematology" 8th
                               ed 2019; Jameson et al. "Harrison's
                               Principles of Internal Medicine" 21st ed
                               2022; ASH/ISTH/WFH/ELN/IMWG/ESMO/AABB/CHEST
                               guidelines and landmark papers as cited per
                               record)
  hematology-signature       - The Hematology Signature Database
                               (his original Signature interpretation of
                               blood as the body's freight and supply line -
                               red cells as the oxygen freight fleet, white
                               cells as the patrol fleet, platelets as the
                               rapid-repair crews, plasma as the river they
                               sail, the marrow as the shipyard; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-HEM- (public) and JAH-HEMS- (signature), both verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "blood as the body's freight and supply line: red cells as the "
            "oxygen freight fleet, white cells as the patrol fleet, platelets "
            "as the rapid-repair crews, plasma as the river they sail, and "
            "the marrow as the shipyard that builds them all. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_WILLIAMS = ("Kaushansky K, Lichtman MA, Prchal JT, Levi MM, Press OW, "
                "Burns LJ, Caligiuri M, eds. Williams Hematology. 10th ed. "
                "McGraw Hill; 2021.")
CIT_HOFFMAN = ("Hoffman R, Benz EJ Jr, Silberstein LE, Heslop HE, Weitz JI, "
               "Anastasi J, eds. Hematology: Basic Principles and Practice. "
               "8th ed. Elsevier; 2023.")
CIT_HOFFBRAND = ("Hoffbrand AV, Moss PAH. Hoffbrand's Essential Haematology. "
                 "8th ed. Wiley-Blackwell; 2019.")
CIT_HARRISON = ("Jameson JL, Fauci AS, Kasper DL, Hauser SL, Longo DL, "
                "Loscalzo J, eds. Harrison's Principles of Internal Medicine. "
                "21st ed. McGraw Hill; 2022.")
CIT_CAMASCHELLA = ("Camaschella C. Iron deficiency. Blood. "
                   "2019;133(1):30-39.")
CIT_GREEN_B12 = ("Green R. Vitamin B12 deficiency from the perspective of a "
                 "practicing hematologist. Blood. 2017;129(19):2603-2611.")
CIT_WEISS = ("Weiss G, Ganz T, Goodnough LT. Anemia of inflammation. Blood. "
             "2019;133(1):40-50.")
CIT_PIEL = ("Piel FB, Steinberg MH, Rees DC. Sickle cell disease. N Engl J "
            "Med. 2017;376(16):1561-1573.")
CIT_TAHER = ("Taher AT, Weatherall DJ, Cappellini MD. Thalassaemia. Lancet. "
             "2018;391(10116):155-167.")
CIT_KILLICK = ("Killick SB, Bown N, Cavenagh J, et al. Guidelines for the "
               "diagnosis and management of adult aplastic anaemia. Br J "
               "Haematol. 2016;172(2):187-207.")
CIT_GREENBERG = ("Greenberg PL, Tuechler H, Schanz J, et al. Revised "
                 "international prognostic scoring system for myelodysplastic "
                 "syndromes. Blood. 2012;120(12):2454-2465.")
CIT_NEUNERT = ("Neunert C, Terrell DR, Arnold DM, et al. American Society of "
               "Hematology 2019 guidelines for immune thrombocytopenia. Blood "
               "Adv. 2019;3(23):3829-3866.")
CIT_VERSTEEG = ("Versteeg HH, Heemskerk JWM, Levi M, Reitsma PH. New "
                "fundamentals in hemostasis. Physiol Rev. 2013;93(1):327-358.")
CIT_WFH = ("Srivastava A, Santagostini E, Dougall A, et al. WFH guidelines "
           "for the management of hemophilia, 3rd edition. Haemophilia. "
           "2020;26(Suppl 6):1-158.")
CIT_VWD = ("James PD, Connell NT, Ameer B, et al. ASH ISTH NHF WFH 2021 "
           "guidelines on the diagnosis of von Willebrand disease. Blood "
           "Adv. 2021;5(1):280-300.")
CIT_CHEST = ("Stevens SM, Woller SC, Kreuziger LB, et al. Antithrombotic "
             "therapy for VTE disease: second update of the CHEST guideline "
             "and expert panel report. Chest. 2021;160(6):e545-e608.")
CIT_DOHNER = ("Dohner H, Wei AH, Appelbaum FR, et al. Diagnosis and "
              "management of AML in adults: 2022 recommendations of the "
              "European LeukemiaNet. Blood. 2022;140(10):1145-1177.")
CIT_HOCHHAUS = ("Hochhaus A, Baccarani M, Silver RT, et al. European "
                "LeukemiaNet 2020 recommendations for treating chronic "
                "myeloid leukemia. Leukemia. 2020;34(4):966-984.")
CIT_HALLEK = ("Hallek M, Cheson BD, Catovsky D, et al. iwCLL guidelines for "
              "diagnosis, indications for treatment, response assessment, and "
              "supportive management of CLL. Blood. 2018;131(25):2745-2760.")
CIT_RAJKUMAR = ("Rajkumar SV, Dimopoulos MA, Palumbo A, et al. International "
                "Myeloma Working Group updated criteria for the diagnosis of "
                "multiple myeloma. Lancet Oncol. 2014;15(12):e538-e548.")
CIT_EICHENAUER = ("Eichenauer DA, Aleman BMP, Andre M, et al. Hodgkin "
                  "lymphoma: ESMO clinical practice guidelines for "
                  "diagnosis, treatment and follow-up. Ann Oncol. "
                  "2018;29(Suppl 4):iv19-iv29.")
CIT_TEFFERI = ("Tefferi A, Barbui T. Polycythemia vera and essential "
               "thrombocythemia: 2021 update on diagnosis, risk-stratification "
               "and management. Am J Hematol. 2020;95(12):1599-1613.")
CIT_LEVI = ("Levi M, Toh CH, Thachil J, Watson HG. Guidelines for the "
            "diagnosis and management of disseminated intravascular "
            "coagulation. Br J Haematol. 2009;145(1):24-33.")
CIT_CARSON = ("Carson JL, Guyatt G, Heddle NM, et al. Red blood cell "
              "transfusion: 2023 AABB International Guidelines. JAMA. "
              "2023;330(19):1892-1902.")
CIT_MAJHAIL = ("Majhail NS, Farnia SH, Carpenter PA, et al. Indications for "
               "autologous and allogeneic hematopoietic cell transplantation: "
               "guidelines from the American Society for Blood and Marrow "
               "Transplantation. Biol Blood Marrow Transplant. "
               "2015;21(11):1863-1869.")
CIT_CUKER = ("Cuker A, Arepally GM, Chong BH, et al. American Society of "
             "Hematology 2018 guidelines for management of venous "
             "thromboembolism: heparin-induced thrombocytopenia. Blood Adv. "
             "2018;2(22):3360-3392.")
CIT_MAUDE = ("Maude SL, Laetsch TW, Buechner J, et al. Tisagenlecleucel in "
             "children and young adults with B-cell lymphoblastic leukemia. "
             "N Engl J Med. 2018;378(5):439-448.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Hematology: The Clinical Specialty of Blood",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Hematology is the clinical medical specialty devoted to blood "
            "and the blood-forming organs - the red cells that carry oxygen, "
            "the white cells that patrol for infection, the platelets that "
            "seal leaks, the plasma proteins that clot and transport, and "
            "the bone marrow that manufactures them all. The name comes from "
            "the Greek haima (blood) and logos (study). The hematologist is "
            "the physician who reads the blood: diagnosing anemias, "
            "hemoglobin disorders, leukemias, lymphomas, myeloma, bleeding "
            "and clotting disorders, and marrow failure, and managing them "
            "with iron and vitamins, transfusions, anticoagulants, "
            "chemotherapy, targeted agents, and stem cell transplantation. "
            "Blood is about 7 percent of body weight - roughly 5 liters in a "
            "70-kilogram adult - and carries some 25 trillion red cells, "
            "each living about 120 days, so the marrow must launch around "
            "200 billion new red cells every single day. This record frames "
            "the discipline and the ladder of records that follows."
        ),
        "how_it_works": (
            "Hematology works on the fleet model of blood. The marrow is the "
            "shipyard: hematopoietic stem cells divide and differentiate "
            "down the myeloid and lymphoid lines, launching red cells, "
            "white cells, and platelets into the circulation. Red cells are "
            "the freight fleet, each packed with about 270 million "
            "hemoglobin molecules hauling oxygen from lungs to tissues. "
            "White cells are the patrol fleet, hunting microbes and "
            "abnormal cells. Platelets are the rapid-repair crews, plugging "
            "breaches in vessel walls within seconds. Plasma is the river "
            "they all sail on, carrying clotting factors, albumin, hormones, "
            "and nutrients. The hematologist reads the fleet's gauges - the "
            "CBC, the smear, iron studies, clotting times - finds which "
            "fleet is failing, and repairs the shipyard, resupplies the "
            "cargo, or replaces the fleet. The demo works the fleet "
            "arithmetic: blood volume from body weight, total red cell count "
            "from concentration, and the daily production the marrow must "
            "sustain."
        ),
        "key_points": [
            "Hematology = the clinical specialty of blood and blood-forming organs: anemias, hemoglobinopathies, leukemias, lymphomas, myeloma, bleeding and clotting disorders, marrow failure, transfusion medicine.",
            "Blood is about 7 percent of body weight (roughly 5 liters in a 70-kg adult) and carries on the order of 25 trillion red cells.",
            "Red cells live about 120 days, so the marrow must produce around 200 billion new red cells every day just to hold steady.",
            "The specialty spans the benign (iron deficiency) to the malignant (acute leukemia) and is both cognitive and procedural: marrow biopsy, apheresis, transfusion, transplant.",
            "Distinct from oncology (all cancers) and immunology (the immune system): hematology is the blood's own medicine, benign and malignant together.",
        ],
        "requirements": [
            "The fleet picture: red cells, white cells, platelets, plasma proteins, marrow shipyard.",
            "Scale literacy: blood volume, cell counts, daily production rates.",
            "The territory map: marrow, circulating blood, spleen, clotting system.",
        ],
        "standards": [
            "Cell names and spellings follow standard clinical usage (erythrocyte, neutrophil, thrombocyte).",
            "Quantities stated as adult averages with 'about' qualifiers since they vary by body size.",
            "Disease framing is diagnostic and management-oriented, matching the clinical-specialty scope.",
        ],
        "citations": [CIT_HOFFBRAND, CIT_WILLIAMS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: blood is the body's freight and supply "
            "line - a river highway carrying oxygen freight, patrol boats, "
            "and repair crews to every tissue, built fresh daily in the "
            "marrow shipyard. The hematologist is the fleet admiral: "
            "counting the ships (the CBC), inspecting the hulls (the smear), "
            "resupplying the cargo holds (iron, B12, folate), patching leaks "
            "(clotting factors, platelets), and when the shipyard itself "
            "turns mutinous (leukemia), burning it down and rebuilding it "
            "with a transplant."
        ),
    },
    {
        "key": "blood_composition",
        "name": "Blood Composition and Hematopoiesis: How the Body Makes Blood",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Blood is a tissue: about 45 percent cells and 55 percent "
            "plasma by volume, the cell fraction being the hematocrit. The "
            "cells are red cells (erythrocytes, oxygen transport), white "
            "cells (leukocytes: neutrophils, lymphocytes, monocytes, "
            "eosinophils, basophils - defense and immunity), and platelets "
            "(thrombocytes - clotting). Plasma is 90 percent water carrying "
            "albumin, clotting factors, immunoglobulins, hormones, and "
            "nutrients. All of it is manufactured by hematopoiesis in the "
            "bone marrow, where a single hematopoietic stem cell divides and "
            "differentiates down myeloid and lymphoid branches under the "
            "direction of growth factors - erythropoietin for red cells, "
            "thrombopoietin for platelets, G-CSF and GM-CSF for white cells. "
            "Steady state is a balance: daily production times cell lifespan "
            "equals the circulating pool, so the 120-day red cell, the "
            "10-day platelet, and the hours-to-days neutrophil each demand "
            "their own production rate."
        ),
        "how_it_works": (
            "Hematopoiesis works as a branching production line. The "
            "pluripotent stem cell commits to the common myeloid progenitor "
            "(red cells, platelets, granulocytes, monocytes) or the common "
            "lymphoid progenitor (B, T, and NK cells). Erythropoietin, made "
            "by the kidney in response to low oxygen, drives red cell "
            "output; thrombopoietin drives platelet output; "
            "colony-stimulating factors drive white cell output. Maturing "
            "cells shrink their nuclei (red cells eject theirs entirely), "
            "load their cargo, and squeeze through the marrow sinusoids into "
            "blood. The demo checks the steady-state arithmetic: daily "
            "production multiplied by lifespan reproduces the circulating "
            "pool, and the platelet pool divided by blood volume lands "
            "inside the normal 150,000 to 400,000 per microliter band."
        ),
        "key_points": [
            "Blood is about 45 percent cells (the hematocrit) and 55 percent plasma; plasma is 90 percent water plus proteins.",
            "Every blood cell descends from the hematopoietic stem cell through myeloid and lymphoid branches, steered by growth factors (erythropoietin, thrombopoietin, colony-stimulating factors).",
            "Steady state: circulating pool = daily production x cell lifespan; red cells 120 days, platelets about 10 days, neutrophils hours to days.",
            "Red cells eject their nuclei to make room for hemoglobin; platelets are fragments of megakaryocytes, not true cells.",
            "The demo verifies the arithmetic: production x lifespan reproduces the pools, and platelet concentration lands in the normal band.",
        ],
        "requirements": [
            "The composition fractions: hematocrit, plasma, the three cell lines.",
            "The branching production line: stem cell to myeloid and lymphoid progenitors.",
            "The growth-factor steering: erythropoietin, thrombopoietin, colony-stimulating factors.",
        ],
        "standards": [
            "Lineage names follow standard hematology usage (myeloid, lymphoid, megakaryocyte).",
            "Lifespans stated as typical adult values; they vary with conditions.",
            "Production rates stated as order-of-magnitude daily values.",
        ],
        "citations": [CIT_WILLIAMS, CIT_HOFFBRAND, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: hematopoiesis is the shipyard's "
            "assembly line - one master stem-cell dry dock launching three "
            "vessel classes down branching slipways. Erythropoietin is the "
            "production order faxed from the kidney when oxygen runs low; "
            "thrombopoietin is the standing order for repair crews. Red "
            "cells are launched as stripped-down freighters with the crew "
            "quarters (the nucleus) ripped out to maximize cargo space - "
            "the most extreme weight-saving design in the body."
        ),
    },
    {
        "key": "cbc",
        "name": "The Complete Blood Count: Reading the CBC",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The complete blood count is the most ordered test in medicine "
            "and the hematologist's first gauge panel. It reports hemoglobin "
            "and hematocrit (oxygen-carrying capacity), the red cell indices "
            "MCV (mean cell volume), MCH (mean cell hemoglobin), MCHC, and "
            "RDW (size variation), the white cell count with differential, "
            "and the platelet count, plus the smear when morphology matters. "
            "The MCV sorts anemias at a glance: low (microcytic - iron "
            "deficiency, thalassemia), normal (normocytic - chronic disease, "
            "blood loss, marrow failure), high (macrocytic - B12 or folate "
            "deficiency, alcohol, drugs). The RDW flags mixed populations. "
            "The differential apportions the white cells. The platelet count "
            "separates bleeding risk from clotting risk. Read in order - "
            "hemoglobin, MCV, white cells, platelets - the CBC narrows every "
            "hematologic diagnosis before a single further test is ordered."
        ),
        "how_it_works": (
            "The CBC works as a four-gauge panel read in fixed order. First "
            "hemoglobin: low means anemia, high suggests polycythemia or "
            "hemoconcentration. Second the MCV: it triages the anemia into "
            "microcytic, normocytic, or macrocytic buckets, each with its "
            "own short differential. Third the white count and differential: "
            "high suggests infection, inflammation, or leukemia; low "
            "suggests marrow suppression or consumption. Fourth platelets: "
            "low means bleeding risk and a marrow or destruction problem; "
            "high suggests reactive thrombocytosis or a myeloproliferative "
            "disorder. The demo runs the panel logic on a sample CBC - "
            "hemoglobin 9.8 with MCV 72 - and returns the correct first "
            "read: microcytic anemia, with iron studies next."
        ),
        "key_points": [
            "The CBC is read in order: hemoglobin, then MCV, then white cells, then platelets.",
            "MCV triages anemia: low = microcytic (iron deficiency, thalassemia), normal = normocytic, high = macrocytic (B12/folate deficiency).",
            "RDW measures red cell size variation; a high RDW with low MCV points toward iron deficiency over thalassemia trait.",
            "The differential apportions white cells; the platelet count separates bleeding risk from clotting risk.",
            "The demo runs the four-gauge read on a sample panel and returns the correct first interpretation.",
        ],
        "requirements": [
            "The four gauges: hemoglobin, red cell indices, white count with differential, platelets.",
            "The MCV triage buckets and what each one means.",
            "Reference-range literacy: what counts as low, normal, high for each gauge.",
        ],
        "standards": [
            "Units stated explicitly (g/dL, fL, per microliter) with every value.",
            "Reference ranges given as typical adult values; labs vary slightly.",
            "The CBC never diagnoses alone - it triages toward the next test.",
        ],
        "citations": [CIT_HOFFBRAND, CIT_HARRISON, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: the CBC is the fleet admiral's morning "
            "status board - four gauges glowing on the bridge. Hemoglobin is "
            "the fuel gauge, MCV is the hull-size inspector, the white count "
            "is the patrol roster, platelets are the damage-control crew "
            "headcount. A good admiral reads the board in the same order "
            "every morning and never orders a new test before the board has "
            "spoken."
        ),
    },
    {
        "key": "hemoglobin_rbc",
        "name": "Hemoglobin and Red Blood Cell Physiology",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Hemoglobin is the oxygen-handling molecule: four globin chains "
            "(two alpha, two beta in adult HbA) each cradling a heme group "
            "with one iron atom that reversibly binds one oxygen molecule, "
            "so each hemoglobin carries four oxygens and each red cell "
            "carries about 270 million hemoglobins. One gram of hemoglobin "
            "binds 1.34 milliliters of oxygen (Hufner's constant), so "
            "arterial oxygen content is essentially 1.34 times hemoglobin "
            "times saturation. The oxygen-hemoglobin dissociation curve is "
            "sigmoid: hemoglobin loads oxygen steeply in the lungs and "
            "unloads it in the tissues, with the P50 (the oxygen tension at "
            "50 percent saturation, normally about 27 mmHg) marking the "
            "curve's position. Acidosis, high carbon dioxide, fever, and "
            "2,3-BPG shift the curve right (unload more oxygen); alkalosis "
            "and cold shift it left. Fetal hemoglobin (two alpha, two gamma "
            "chains) binds oxygen more tightly to pull it across the "
            "placenta."
        ),
        "how_it_works": (
            "Hemoglobin works as a four-seat oxygen shuttle with teamwork "
            "built in: when one heme grabs oxygen, the whole molecule "
            "changes shape and the other three seats load more easily "
            "(cooperative binding), which is what makes the dissociation "
            "curve S-shaped instead of a straight line. In the lungs, high "
            "oxygen tension fills nearly every seat; in the tissues, lower "
            "tension plus acid, carbon dioxide, and warmth persuade "
            "hemoglobin to hand the oxygen over. Each red cell is a "
            "biconcave disc - maximum surface area, no nucleus, built to "
            "deform through capillaries half its diameter. The demo computes "
            "arterial oxygen content from hemoglobin 15 g/dL at 98 percent "
            "saturation (about 20 mL per dL) and multiplies by cardiac "
            "output to get total oxygen transport near 1,000 mL per minute."
        ),
        "key_points": [
            "Hemoglobin: four globin chains, four hemes, four oxygens per molecule; about 270 million hemoglobins per red cell.",
            "Hufner's constant: 1 gram of hemoglobin carries 1.34 mL of oxygen; arterial content is 1.34 x hemoglobin x saturation.",
            "The sigmoid dissociation curve loads oxygen in the lungs and unloads it in tissues; P50 is normally about 27 mmHg.",
            "Acid, carbon dioxide, heat, and 2,3-BPG shift the curve right (release oxygen); alkalosis and cold shift it left.",
            "Fetal hemoglobin (alpha2 gamma2) holds oxygen tighter to draw it across the placenta.",
        ],
        "requirements": [
            "The four-seat shuttle: globin chains, heme iron, cooperative binding.",
            "Hufner's constant and the arterial oxygen content formula.",
            "The dissociation curve, P50, and the right/left shifters.",
        ],
        "standards": [
            "Hemoglobin types named by chain composition (HbA alpha2 beta2, HbF alpha2 gamma2, HbS).",
            "Oxygen content stated in mL per dL with the dissolved fraction noted as small.",
            "P50 stated in mmHg as the standard curve-position marker.",
        ],
        "citations": [CIT_WILLIAMS, CIT_HOFFMAN, CIT_HOFFBRAND],
        "sig_lens": (
            "His Signature reading: hemoglobin is the perfect freight "
            "container - four seats that load cooperatively, so the first "
            "crate aboard makes the next three easier to lift. The "
            "dissociation curve is the union contract: load heavy where "
            "oxygen is plentiful (the lungs), unload where the tissues pay "
            "in acid and carbon dioxide. Fetal hemoglobin is the apprentice "
            "crew that grips the cargo tighter to steal it across the "
            "placental dock."
        ),
    },
    {
        "key": "marrow",
        "name": "The Bone Marrow: The Body's Blood Factory",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The bone marrow is the blood factory: about 1.5 kilograms of "
            "red marrow in the adult pelvis, vertebrae, ribs, sternum, and "
            "proximal long bones, producing all circulating blood cells. "
            "Marrow cellularity - the fraction of marrow space occupied by "
            "blood-forming cells versus fat - falls with age, roughly "
            "following the 100-minus-age rule (about 60 percent cellular at "
            "40, about 40 percent at 60). The marrow biopsy reads the "
            "factory floor: cellularity, the myeloid-to-erythroid ratio "
            "(normally about 3 to 1), blast percentage (under 5 percent is "
            "normal; 20 percent or more defines acute leukemia), iron "
            "stores, fibrosis, and infiltrating disease. Marrow failure - "
            "aplastic anemia, where the factory goes quiet - and marrow "
            "replacement - leukemia, myeloma, fibrosis, where the floor is "
            "taken over - are read directly from this tissue."
        ),
        "how_it_works": (
            "The marrow works as a cellular factory with quality control. "
            "Stem cells sit in niches along the bone, dividing rarely; "
            "their progeny amplify enormously as they mature, so a handful "
            "of stem cell divisions yields billions of circulating cells. "
            "Maturing cells migrate toward the central sinusoids and squeeze "
            "into the blood only when finished - the marrow-blood barrier "
            "keeps half-built cells inside, which is why blasts in the blood "
            "mean trouble. The biopsy samples the floor with a core needle, "
            "usually from the posterior iliac crest, and the pathologist "
            "reads cellularity, lineage ratios, and blasts. The demo applies "
            "the 100-minus-age rule across adult ages and checks that "
            "cellularity falls from about 80 percent at 20 to about 20 "
            "percent at 80."
        ),
        "key_points": [
            "Red marrow (about 1.5 kg) in pelvis, vertebrae, ribs, sternum, and proximal long bones makes all blood cells.",
            "Cellularity follows the 100-minus-age rule: about 60 percent at age 40, about 40 percent at age 60.",
            "The biopsy reads the factory floor: cellularity, myeloid-to-erythroid ratio (about 3:1), blast percentage, iron stores, fibrosis.",
            "Under 5 percent blasts is normal; 20 percent or more defines acute leukemia.",
            "Blasts belong in the marrow, not the blood: circulating blasts mean the factory barrier has been breached.",
        ],
        "requirements": [
            "The factory map: red marrow sites and the 100-minus-age rule.",
            "The biopsy read: cellularity, M:E ratio, blasts, iron, fibrosis.",
            "The barrier principle: finished cells only in the blood.",
        ],
        "standards": [
            "Cellularity stated as a percentage of marrow space.",
            "Blast thresholds stated exactly: under 5 percent normal, 20 percent or more acute leukemia.",
            "Biopsy site named: posterior iliac crest is the standard adult site.",
        ],
        "citations": [CIT_WILLIAMS, CIT_HOFFBRAND, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: the marrow is the shipyard itself - "
            "1.5 kilograms of slipways inside the bones, launching the "
            "entire fleet. Cellularity is the yard's occupancy rate, "
            "falling as the yard ages and fills with fat. The biopsy is the "
            "surprise inspection: walk the floor, count the workers, check "
            "the blast cradles. A quiet yard is aplastic anemia; a yard "
            "overrun by half-built hulls is leukemia."
        ),
    },
    {
        "key": "iron_b12_folate",
        "name": "Iron, Vitamin B12, and Folate: The Red Cell Supply Lines",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Red cell production runs on three supply lines. Iron is the "
            "oxygen-binding atom at the heart of heme: the adult body holds "
            "3 to 4 grams, two-thirds of it in circulating hemoglobin, and "
            "recycles it almost perfectly - about 20 milligrams a day from "
            "dying red cells - so only 1 to 2 milligrams must be absorbed "
            "daily from food to cover losses. Vitamin B12 and folate are the "
            "DNA-synthesis vitamins: without them, red cell precursors "
            "cannot divide their nuclei properly and grow into oversized, "
            "fragile megaloblasts. B12 comes only from animal foods, needs "
            "intrinsic factor from the stomach for absorption, and the body "
            "stores a 2-to-5-year supply in the body's reserves; folate comes from "
            "green vegetables, needs no carrier, and stores run out in "
            "months. Cut any one line and the marrow stalls: iron loss gives "
            "small pale cells, B12 or folate loss gives large fragile ones."
        ),
        "how_it_works": (
            "The supply lines work as a just-in-time inventory with very "
            "different buffers. Iron is absorbed in the duodenum through the "
            "ferroportin gate, which the hormone hepcidin locks during "
            "inflammation; absorbed iron rides transferrin to the marrow, "
            "where each red cell precursor loads it into heme. B12 binds "
            "intrinsic factor in the stomach, is absorbed in the terminal "
            "ileum, and serves as a cofactor for methionine synthase in DNA "
            "production; folate feeds the same pathway one step upstream. "
            "The demo works the inventory math: a 500 mL blood donation "
            "removes about 250 mg of iron, and at 1.5 mg absorbed per day "
            "the body needs about 167 days to replace it - which is why "
            "frequent donors run iron-deficient."
        ),
        "key_points": [
            "Iron: 3 to 4 grams total body, two-thirds in hemoglobin; only 1 to 2 mg absorbed daily because 20 mg is recycled daily.",
            "Hepcidin locks the ferroportin iron gate during inflammation, starving both microbes and the marrow.",
            "B12 needs intrinsic factor and the terminal ileum; stores last 2 to 5 years, so deficiency creeps up slowly.",
            "Folate needs no carrier and stores last months, so deficiency arrives fast (pregnancy, alcohol use, drugs).",
            "Iron loss makes small pale cells; B12 or folate loss makes large fragile megaloblasts.",
        ],
        "requirements": [
            "The three supply lines and what each one builds.",
            "The inventory math: total stores, daily need, absorption rate.",
            "The hepcidin gate and the intrinsic factor pathway.",
        ],
        "standards": [
            "Iron quantities in milligrams, B12 in picograms per mL, folate in ng per mL.",
            "Store durations stated as ranges since they vary.",
            "Absorption sites named: duodenum for iron, terminal ileum for B12.",
        ],
        "citations": [CIT_CAMASCHELLA, CIT_GREEN_B12, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: the supply lines are the fleet's "
            "logistics chain - iron is the specialty steel for the freight "
            "containers, B12 and folate are the blueprint paper the yard "
            "needs to cut hulls to size. Iron runs on a near-perfect "
            "recycling loop with a tiny daily top-up; B12 is the deep "
            "warehouse stock that lasts years; folate is the fresh produce "
            "that spoils in months. Break the chain anywhere and the yard "
            "launches deformed ships."
        ),
    },
    {
        "key": "wbc_diff",
        "name": "White Blood Cells and the Differential Count",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "White blood cells are the patrol fleet: neutrophils (the "
            "first responders, 40 to 70 percent of white cells), lymphocytes "
            "(the targeted-attack force, 20 to 40 percent), monocytes (the "
            "cleanup crew that becomes tissue macrophages), eosinophils "
            "(parasite and allergy fighters), and basophils (histamine "
            "carriers). The differential counts each type, and the absolute "
            "neutrophil count (ANC) - white count times the neutrophil "
            "fraction - is the number that matters: below 1,500 per "
            "microliter is neutropenia, below 1,000 moderate, below 500 "
            "severe, and below 500 the infection risk climbs steeply. A "
            "left shift (band forms in the blood) means the marrow is "
            "rushing immature neutrophils out to meet an acute infection. "
            "High white counts suggest infection, inflammation, steroids, or "
            "leukemia; low counts suggest marrow suppression, "
            "autoimmunity, or overwhelming sepsis."
        ),
        "how_it_works": (
            "The differential works as a patrol roster audit. Each white "
            "cell type has a job and a normal share; the pattern of which "
            "rises or falls names the threat. Neutrophils rise in bacterial "
            "infection and fall with chemotherapy or marrow failure; "
            "lymphocytes rise in viral infection and in chronic lymphocytic "
            "leukemia; eosinophils rise in parasites, allergy, and certain "
            "drugs. The ANC compresses the roster into one readiness number: "
            "multiply the total white count by the neutrophil fraction "
            "(segments plus bands). The demo computes the ANC for a white "
            "count of 2,500 with 30 percent segments and 5 percent bands - "
            "875 per microliter - and returns the correct grade: moderate "
            "neutropenia."
        ),
        "key_points": [
            "The five white cell types: neutrophils, lymphocytes, monocytes, eosinophils, basophils, each with a normal share.",
            "ANC = white count x neutrophil fraction; below 1,500 is neutropenia, below 500 severe.",
            "A left shift (bands in blood) means the marrow is rushing immature neutrophils to an acute infection.",
            "High counts suggest infection, inflammation, steroids, or leukemia; low counts suggest marrow suppression or consumption.",
            "The demo computes an ANC of 875 and grades it moderate neutropenia.",
        ],
        "requirements": [
            "The five patrol types and their normal percentage shares.",
            "The ANC formula and the neutropenia thresholds.",
            "The left shift and what it signals.",
        ],
        "standards": [
            "Counts in cells per microliter; differentials as percentages of the total.",
            "ANC thresholds stated exactly: 1,500 / 1,000 / 500.",
            "Bands named as the immature neutrophil form.",
        ],
        "citations": [CIT_HOFFBRAND, CIT_WILLIAMS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: the white cells are the patrol fleet - "
            "neutrophils the rapid-response cutters, lymphocytes the "
            "special forces, monocytes the salvage tugs, eosinophils the "
            "exotic-warfare unit. The ANC is the fleet readiness score: one "
            "number that tells the admiral whether the harbor is defended. "
            "A left shift is the yard launching cadets before graduation - "
            "proof the battle is already joined."
        ),
    },
    {
        "key": "encounter",
        "name": "The Hematology Clinical Encounter: History, Examination, and Workup",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hematology encounter is the detective work before the labs: "
            "a history that hunts bleeding and clotting (nosebleeds, gum "
            "bleeding, heavy periods, blood in urine or stool, bruising, "
            "clots, miscarriages), fatigue and pallor (anemia), fevers, "
            "night sweats, and weight loss (the B symptoms of lymphoma), "
            "plus drugs, alcohol, diet, family history, and ancestry "
            "(thalassemia in Mediterranean and Southeast Asian families, "
            "sickle cell in African ancestry). The examination checks "
            "pallor, jaundice, petechiae and purpura, lymph nodes, and the "
            "spleen - the organ that filters blood and swells in "
            "lymphomas, leukemias, hemolysis, and portal hypertension. The "
            "workup follows the CBC's lead: iron studies and ferritin for "
            "microcytic anemia, B12 and folate for macrocytic, reticulocyte "
            "count for hemolysis, the peripheral smear for morphology, and "
            "the marrow biopsy when the factory itself is suspect."
        ),
        "how_it_works": (
            "The encounter works as a funnel: history narrows the field, "
            "examination localizes it, labs confirm it. Bleeding history "
            "separates platelet problems (mucosal bleeding, petechiae) from "
            "clotting-factor problems (deep tissue bleeding, joint bleeds, "
            "delayed bleeding after cuts). The Mentzer index - MCV divided "
            "by red cell count - is a bedside arithmetic trick: under 13 "
            "favors thalassemia trait, over 13 favors iron deficiency. The "
            "demo runs it on two cases: MCV 68 with red cells 5.9 gives "
            "11.5 (thalassemia pattern), while MCV 70 with red cells 3.8 "
            "gives 18.4 (iron deficiency pattern)."
        ),
        "key_points": [
            "History hunts bleeding vs clotting, B symptoms, drugs, diet, family history, and ancestry.",
            "Examination checks pallor, jaundice, petechiae, lymph nodes, and spleen size.",
            "Platelet-type bleeding is mucosal and immediate; factor-type bleeding is deep, delayed, and into joints.",
            "The Mentzer index (MCV / red cell count): under 13 favors thalassemia trait, over 13 favors iron deficiency.",
            "The workup follows the CBC: iron studies, B12/folate, reticulocytes, smear, then marrow biopsy.",
        ],
        "requirements": [
            "The bleeding history: mucosal vs deep, immediate vs delayed.",
            "The B symptoms: fevers, night sweats, weight loss.",
            "The Mentzer index arithmetic and its two patterns.",
        ],
        "standards": [
            "Bleeding and clotting histories taken separately and completely.",
            "Ancestry asked as it guides hemoglobinopathy testing.",
            "The smear reviewed before the marrow is biopsied.",
        ],
        "citations": [CIT_HOFFBRAND, CIT_HARRISON, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: the encounter is the admiral's "
            "intelligence briefing before the fleet review - interrogate "
            "the witnesses (history), walk the docks (examination), then "
            "read the gauges (labs). The Mentzer index is field arithmetic "
            "for telling two look-alike small-ship problems apart without "
            "waiting for the full laboratory."
        ),
    },
]

ENTRIES += [
    {
        "key": "iron_def",
        "name": "Iron Deficiency Anemia: The Most Common Anemia",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Iron deficiency is the most common cause of anemia worldwide "
            "and the most common nutritional deficiency on earth. It "
            "develops in stages: first iron stores fall (low ferritin), "
            "then iron transport to the marrow falters (low transferrin "
            "saturation), and finally hemoglobin production drops and the "
            "anemia appears - small (low MCV), pale (low MCH) red cells with "
            "a high RDW. Causes are blood loss (heavy periods, "
            "gastrointestinal bleeding - colon cancer in an older adult with "
            "new iron deficiency until proven otherwise), increased demand "
            "(pregnancy, growth, frequent blood donation), and poor "
            "absorption (gastric bypass, celiac disease). Clues beyond the "
            "labs: fatigue, pica (ice craving), restless legs, spoon-shaped "
            "nails (koilonychia), and cracks at the mouth corners. Diagnosis "
            "rests on ferritin under 15 ng per mL (under 30 with "
            "inflammation), transferrin saturation under 16 percent, and "
            "the microcytic picture; treatment is ferrous sulfate by mouth, "
            "intravenous iron when oral fails or blood loss is ongoing, plus "
            "finding and fixing the source of loss."
        ),
        "how_it_works": (
            "Iron deficiency works as a supply-chain collapse in three "
            "stages. Stage one drains the warehouse: ferritin, the storage "
            "protein, falls while hemoglobin still holds. Stage two "
            "starves the trucks: transferrin saturation - serum iron "
            "divided by total iron-binding capacity - drops under 16 "
            "percent, so the marrow gets too little iron to fill each new "
            "red cell. Stage three shows in the product: red cells come out "
            "small and pale, the MCV falls, the RDW climbs as old normal "
            "cells mix with new small ones. The demo runs the stage-two "
            "math on serum iron 28 with TIBC 460 - transferrin saturation "
            "6.1 percent, squarely deficient - and returns the correct "
            "stage and next step: replace iron and find the bleeding."
        ),
        "key_points": [
            "The most common anemia worldwide; develops in three stages: low ferritin, then low transferrin saturation, then anemia.",
            "Ferritin under 15 ng/mL (under 30 with inflammation) and transferrin saturation under 16 percent define deficiency.",
            "Microcytic, hypochromic cells with high RDW; Mentzer index over 13 separates it from thalassemia trait.",
            "New iron deficiency in an older adult means gastrointestinal blood loss - colon evaluation - until proven otherwise.",
            "Treatment: oral ferrous sulfate first, intravenous iron when oral fails, plus fixing the source of loss.",
        ],
        "requirements": [
            "The three stages and the lab marker of each.",
            "The ferritin and transferrin saturation thresholds.",
            "The blood-loss hunt: periods, gut, donation, surgery.",
        ],
        "standards": [
            "Ferritin in ng per mL, serum iron and TIBC in mcg per dL, saturation as a percent.",
            "Inflammation raises ferritin, so the threshold rises to 30 with it.",
            "Oral iron taken with vitamin C, away from tea, coffee, and antacids.",
        ],
        "citations": [CIT_CAMASCHELLA, CIT_HOFFBRAND, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: iron deficiency is the steel shortage - "
            "the warehouse empties first (ferritin), then the supply trucks "
            "run half-empty (transferrin saturation), then the yard starts "
            "launching undersized freighters. The admiral's rule: never just "
            "restock the steel without finding where it is leaking - "
            "especially in an older sailor, where the leak may be a tumor "
            "in the gut."
        ),
    },
    {
        "key": "b12_folate_def",
        "name": "Vitamin B12 and Folate Deficiency: Megaloblastic Anemia",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "B12 and folate deficiency produce megaloblastic anemia: red "
            "cell precursors that cannot synthesize DNA properly grow into "
            "oversized, fragile megaloblasts with an MCV over 100 fL, while "
            "hypersegmented neutrophils (six or more lobes) appear on the "
            "smear. B12 deficiency comes from pernicious anemia "
            "(autoimmune destruction of intrinsic factor), gastric or ileal "
            "surgery, strict vegan diet without supplementation, and "
            "metformin or acid-suppressing drugs; it adds neurologic injury "
            "found in no other anemia - numbness, gait instability, memory "
            "loss, and subacute combined degeneration of the spinal cord - "
            "which can become permanent if treatment is delayed. Folate "
            "deficiency comes from poor diet, alcohol use, pregnancy's "
            "increased demand, and drugs like methotrexate and "
            "trimethoprim; it spares the nerves but threatens the fetus "
            "with neural tube defects. B12 under 200 pg per mL is deficient; "
            "methylmalonic acid rises in B12 deficiency specifically, "
            "homocysteine in both. Never give folate alone when B12 "
            "deficiency is possible - it corrects the anemia while the "
            "nerves keep dying."
        ),
        "how_it_works": (
            "Megaloblastic anemia works as a blueprint-paper jam. B12 and "
            "folate feed the DNA-synthesis pathway; without them, the "
            "nucleus cannot divide on schedule while the cytoplasm keeps "
            "growing, so precursors swell into megaloblasts that die in the "
            "marrow (ineffective erythropoiesis) and the survivors emerge "
            "oversized. B12's absorption chain is long and fragile - "
            "stomach acid frees it, intrinsic factor carries it, the "
            "terminal ileum takes it up - so autoimmunity, surgery, or "
            "drugs at any link starve the marrow years after stores run "
            "dry. The demo classifies a case - MCV 112, B12 140 pg per mL, "
            "folate normal - as B12-deficiency megaloblastic anemia and "
            "flags the rule: replace B12 first, urgently, for the nerves."
        ),
        "key_points": [
            "Megaloblastic anemia: MCV over 100, hypersegmented neutrophils, ineffective marrow production.",
            "B12 deficiency causes irreversible neurologic injury (numbness, gait failure, cognitive loss); folate deficiency does not.",
            "Pernicious anemia, ileal disease or surgery, vegan diet, metformin: the B12 risk list.",
            "B12 under 200 pg/mL is deficient; methylmalonic acid confirms B12 deficiency specifically.",
            "Never folate alone when B12 deficiency is possible: the anemia improves while nerves keep dying.",
        ],
        "requirements": [
            "The megaloblastic picture: high MCV, hypersegmented neutrophils.",
            "The B12 absorption chain and where it breaks.",
            "The neurologic stakes that make B12 urgent.",
        ],
        "standards": [
            "B12 in pg per mL, folate in ng per mL, MCV in fL.",
            "Methylmalonic acid as the specific B12 marker.",
            "B12 replaced by injection when absorption is broken.",
        ],
        "citations": [CIT_GREEN_B12, CIT_HOFFBRAND, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: megaloblastic anemia is the blueprint "
            "crisis - the yard has steel and labor but the copying machine "
            "is jammed, so hulls come out oversized and shatter on launch. "
            "B12 is the one shortage that also rots the telegraph lines "
            "(the nerves) - and folate alone is the cruel fix that repaints "
            "the hulls while the wiring keeps burning."
        ),
    },
    {
        "key": "acd",
        "name": "Anemia of Chronic Disease and Inflammation",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Anemia of inflammation - also called anemia of chronic disease "
            "- is the anemia of the long war: chronic infection, autoimmune "
            "disease, cancer, and kidney failure all produce it. The "
            "mechanism is hepcidin, the iron-regulatory hormone: "
            "inflammation drives hepcidin up, hepcidin locks the ferroportin "
            "iron gates in the gut and macrophages, and iron is trapped in "
            "storage where the marrow cannot reach it - an ancient defense "
            "that starves invading microbes of iron, now misfiring against "
            "the patient's own red cells. The labs show the trap: low "
            "serum iron and low transferrin saturation like iron deficiency, "
            "but ferritin high (inflammation raises it) and TIBC low or "
            "normal (not high as in true deficiency). The anemia is usually "
            "mild to moderate and normocytic. Treatment is the underlying "
            "disease; iron helps only when true deficiency coexists, and "
            "erythropoiesis-stimulating agents have narrow, cautious roles."
        ),
        "how_it_works": (
            "The anemia of inflammation works as a siege economy. Cytokines "
            "from the chronic disease - interleukin-6 chief among them - "
            "order hepcidin production to surge; hepcidin binds "
            "ferroportin, the only iron-export channel, and destroys it, so "
            "iron absorbed from food cannot enter the blood and iron in "
            "macrophages cannot leave. The marrow sees an iron famine while "
            "the warehouse overflows - ferritin high, transferrin "
            "saturation low. The demo applies the pattern rule to a case: "
            "ferritin 380, transferrin saturation 11 percent, TIBC low - "
            "the trap pattern, not true deficiency - and returns the "
            "correct call: treat the inflammation, not the iron."
        ),
        "key_points": [
            "Hepcidin locks iron in storage during inflammation: an ancient anti-microbe defense that causes anemia.",
            "The trap pattern: low iron and low saturation like deficiency, but ferritin high and TIBC low or normal.",
            "Causes: chronic infection, autoimmune disease, cancer, kidney failure.",
            "Usually mild to moderate and normocytic; treatment is the underlying disease.",
            "Iron helps only with coexisting true deficiency; the demo's pattern rule separates the two.",
        ],
        "requirements": [
            "The hepcidin-ferroportin lock and why inflammation triggers it.",
            "The trap labs vs true deficiency labs, side by side.",
            "The treatment principle: the disease, not the iron.",
        ],
        "standards": [
            "Ferritin interpreted against the inflammatory state.",
            "C-reactive protein or ESR documents the inflammation.",
            "Erythropoiesis-stimulating agents used only within their narrow indications.",
        ],
        "citations": [CIT_WEISS, CIT_WILLIAMS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: this is the siege-economy anemia - the "
            "body locks the steel vaults against invaders and starves its "
            "own shipyard in the process. The warehouse is full (ferritin "
            "high) while the assembly line begs for metal. Pouring in more "
            "iron is shipping steel to a locked vault; the fix is lifting "
            "the siege - treating the war underneath."
        ),
    },
    {
        "key": "hemolysis",
        "name": "Hemolytic Anemia: When Red Cells Break Apart",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Hemolytic anemia is anemia from red cells dying young - "
            "destroyed faster than the marrow can replace them. The "
            "signature labs: a high reticulocyte count (the marrow working "
            "overtime), high LDH and indirect bilirubin (spilled cell "
            "contents), low haptoglobin (consumed mopping up free "
            "hemoglobin), and often an enlarged spleen doing the destroying. "
            "Causes divide by where the fault lies: inside the cell "
            "(membrane defects like hereditary spherocytosis, enzyme "
            "defects like G6PD deficiency, hemoglobin defects like sickle "
            "cell), or outside it (autoimmune attack with a positive Coombs "
            "test, mechanical shearing by artificial heart valves or "
            "marching, toxins, infections like malaria). The corrected "
            "reticulocyte count - reticulocyte percent times patient "
            "hematocrit over 45 - tells whether the marrow is answering: "
            "over 2 percent means it is trying, pointing to hemolysis or "
            "bleeding rather than marrow failure. Treatment follows the "
            "cause: stop the destruction, remove the spleen in selected "
            "membrane defects, suppress immunity in autoimmune cases, "
            "transfuse through crises."
        ),
        "how_it_works": (
            "Hemolysis works as a demolition outpacing construction. "
            "Normally about 1 percent of red cells retire daily; in "
            "hemolysis the rate multiplies, and the marrow answers by "
            "releasing young reticulocytes - big, bluish cells visible on "
            "the smear as polychromasia. Inside-cell faults make fragile "
            "cells: spherocytes that the spleen traps and eats, G6PD- "
            "deficient cells that shatter under oxidative stress from "
            "fava beans or certain drugs. Outside-cell faults attack normal "
            "cells: antibodies tag them for splenic removal, valves shear "
            "them into schistocytes. The demo computes the corrected "
            "reticulocyte count for hematocrit 27 with 8 percent "
            "reticulocytes - 4.8 percent, well over the 2 percent line - "
            "confirming the marrow is answering and the problem is "
            "destruction, not production."
        ),
        "key_points": [
            "Hemolysis labs: high reticulocytes, high LDH and indirect bilirubin, low haptoglobin, often splenomegaly.",
            "Corrected reticulocyte count over 2 percent proves the marrow is answering: destruction, not failure.",
            "Inside-cell causes: spherocytosis, G6PD deficiency, sickle cell; outside-cell: autoimmune (Coombs positive), mechanical, toxins, malaria.",
            "Schistocytes mean shearing (valves, microangiopathy); spherocytes mean membrane loss.",
            "Treatment follows the cause: stop destruction, selected splenectomy, immunosuppression, transfusion.",
        ],
        "requirements": [
            "The four hemolysis labs and what each one measures.",
            "The corrected reticulocyte formula and the 2 percent line.",
            "Inside-cell vs outside-cell cause families.",
        ],
        "standards": [
            "Reticulocytes as a percent, corrected against hematocrit 45.",
            "Coombs (direct antiglobulin) test for immune destruction.",
            "Smear morphology named: schistocytes, spherocytes, polychromasia.",
        ],
        "citations": [CIT_WILLIAMS, CIT_HOFFBRAND, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: hemolysis is the fleet losing hulls "
            "faster than the yard can launch them - sabotage from within "
            "(defective hulls) or enemy action without (antibodies, "
            "shearing). The corrected reticulocyte count is the yard's "
            "overtime report: over 2 percent and the yard is screaming that "
            "it is doing its part - so the admiral hunts the saboteur, not "
            "the shipwrights."
        ),
    },
    {
        "key": "thalassemia",
        "name": "Thalassemia: The Inherited Hemoglobin Disorders",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Thalassemia is the family of inherited disorders where globin "
            "chain production is unbalanced: too few alpha chains (alpha "
            "thalassemia) or too few beta chains (beta thalassemia), so "
            "hemoglobin cannot assemble properly and red cells come out "
            "small, pale, and short-lived. Beta thalassemia trait - one "
            "faulty gene - is usually a mild microcytic anemia with a high "
            "red cell count and a Mentzer index under 13, diagnosed by "
            "hemoglobin electrophoresis showing raised HbA2 over 3.5 "
            "percent; it needs no treatment but must never be mistaken for "
            "iron deficiency (iron does not fix it). Beta thalassemia major "
            "- two faulty genes - is a transfusion-dependent disease of "
            "childhood with marrow expansion, bone deformity, and iron "
            "overload from repeated transfusions, managed with regular "
            "transfusions plus iron chelation and cured by stem cell "
            "transplant. Alpha thalassemia ranges from silent carrier to "
            "hemoglobin H disease to hydrops fetalis, the fatal four-gene "
            "deletion. The disorders cluster where malaria once ruled - the "
            "Mediterranean, Middle East, South and Southeast Asia - because "
            "carriers resisted malaria."
        ),
        "how_it_works": (
            "Thalassemia works as an assembly-line imbalance. Hemoglobin "
            "needs alpha and beta chains in equal numbers; when one chain "
            "runs short, the surplus partner chains precipitate inside the "
            "red cell precursor, damaging the membrane and triggering "
            "destruction in the marrow (ineffective erythropoiesis) and the "
            "spleen. In beta trait the imbalance is mild - the marrow "
            "compensates by making more, smaller cells, which is why the "
            "red count stays high while the MCV falls. HbA2 (alpha2 "
            "delta2) rises over 3.5 percent because delta-chain production "
            "is spared. The demo checks the trait pattern: HbA2 5.8 "
            "percent, MCV 66, red cells 6.1 million, Mentzer 10.8 - every "
            "marker pointing to beta thalassemia trait, and the iron "
            "studies left alone."
        ),
        "key_points": [
            "Unbalanced globin chains: too few alpha or beta chains; surplus chains damage the cell.",
            "Beta trait: mild microcytic anemia, high red count, Mentzer under 13, HbA2 over 3.5 percent; no treatment, never iron.",
            "Beta major: transfusion-dependent childhood disease; transfusions plus iron chelation; cure by transplant.",
            "Alpha thalassemia: silent carrier to hemoglobin H disease to fatal hydrops fetalis.",
            "Geography follows old malaria zones: Mediterranean, Middle East, South and Southeast Asia.",
        ],
        "requirements": [
            "The chain-imbalance mechanism and ineffective erythropoiesis.",
            "The trait diagnostics: HbA2, Mentzer, red count.",
            "The iron-overload management of transfusion-dependent disease.",
        ],
        "standards": [
            "HbA2 over 3.5 percent as the beta-trait marker on electrophoresis.",
            "Trait distinguished from iron deficiency before any iron is given.",
            "Genetic counseling for carrier couples.",
        ],
        "citations": [CIT_TAHER, CIT_WILLIAMS, CIT_HOFFBRAND],
        "sig_lens": (
            "His Signature reading: thalassemia is the parts-shortage "
            "disorder - the yard runs out of one hull component and the "
            "surplus parts pile up and wreck the assembly line. Trait is "
            "the yard coping by building smaller boats in greater numbers; "
            "major is the yard drowning in scrap. And the cruelest trap in "
            "the fleet: mistaking the parts shortage for a steel shortage "
            "and pouring in iron that only rusts the organs."
        ),
    },
    {
        "key": "sickle",
        "name": "Sickle Cell Disease",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Sickle cell disease is the most common inherited blood "
            "disorder in the United States: a single DNA letter change "
            "swaps glutamic acid for valine in the beta globin chain, "
            "creating hemoglobin S. Deoxygenated HbS polymerizes into stiff "
            "fibers that deform red cells into sickles, which jam small "
            "vessels (vaso-occlusive pain crises), destroy themselves "
            "(chronic hemolytic anemia), and damage organs over a lifetime "
            "- acute chest syndrome, stroke, splenic infarction in "
            "childhood, kidney disease, leg ulcers, and pulmonary "
            "hypertension. About 1 in 365 Black births in the US carries "
            "the disease; newborn screening catches it at birth. Management "
            "is prevention layered on treatment: penicillin prophylaxis "
            "and full vaccination in childhood, hydroxyurea to raise fetal "
            "hemoglobin and cut crises, transfusions for stroke prevention "
            "and acute chest, aggressive pain control in crisis, and now "
            "curative options - stem cell transplant and gene therapies "
            "that turn fetal hemoglobin back on."
        ),
        "how_it_works": (
            "Sickle cell works as a polymerization catastrophe. Oxygenated "
            "HbS behaves normally; when oxygen unloads in the tissues, the "
            "valine patch on each HbS molecule sticks to a pocket on its "
            "neighbor, and millions of molecules zip into rigid 14-strand "
            "fibers that stretch the red cell into a sickle. Sickled cells "
            "are stiff and sticky: they lodge in post-capillary venules, "
            "and each jam lowers local oxygen further, sickling more cells "
            "in a vicious cycle - the vaso-occlusive crisis. Fetal "
            "hemoglobin (HbF) interrupts the fibers, which is why "
            "hydroxyurea (which raises HbF) prevents crises and why "
            "gene therapy aims to switch HbF back on. The demo works the "
            "epidemiology: 1 in 365 Black births means 36,500 such births "
            "yield about 100 affected newborns."
        ),
        "key_points": [
            "One amino acid swap (glutamic acid to valine) creates HbS, which polymerizes when deoxygenated.",
            "Sickled cells jam vessels (pain crises), destroy themselves (hemolytic anemia), and injure organs over time.",
            "About 1 in 365 Black births in the US; newborn screening catches every case at birth.",
            "Hydroxyurea raises fetal hemoglobin and cuts crises; transfusions prevent stroke and treat acute chest.",
            "Curative horizon: stem cell transplant and gene therapies that reactivate fetal hemoglobin.",
        ],
        "requirements": [
            "The polymerization mechanism and the vicious cycle of vaso-occlusion.",
            "The complication map: acute chest, stroke, spleen, kidney, lungs.",
            "The prevention stack: penicillin, vaccines, hydroxyurea, transfusion, cure.",
        ],
        "standards": [
            "Newborn screening as the universal catch.",
            "Pain crises treated aggressively and without delay or judgment.",
            "Stroke screening with transcranial Doppler in childhood.",
        ],
        "citations": [CIT_PIEL, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: sickle cell is the mutinous cargo - one "
            "bad rivet in the container design, and the whole load "
            "crystallizes into spars the moment the air gets thin. The "
            "jammed harbors (pain crises) feed themselves: each blockage "
            "breeds more blockage. Fetal hemoglobin is the old reliable "
            "container design the fleet is learning to switch back on - "
            "first with hydroxyurea's coaxing, now with gene therapy's "
            "rewiring."
        ),
    },
    {
        "key": "aplastic",
        "name": "Aplastic Anemia and Bone Marrow Failure",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Aplastic anemia is the empty marrow: the blood factory goes "
            "quiet and all three cell lines fall - anemia, neutropenia, "
            "and thrombocytopenia together (pancytopenia) with a marrow "
            "that is mostly fat. Most cases are autoimmune: the patient's "
            "own T cells destroy the hematopoietic stem cells, sometimes "
            "triggered by drugs, chemicals like benzene, or viruses. "
            "Severity is graded by Camitta criteria - marrow cellularity "
            "under 25 percent plus two of: neutrophils under 500, platelets "
            "under 20,000, reticulocytes under 20,000 per microliter - "
            "into non-severe, severe, and very severe (neutrophils under "
            "200). Severe disease kills by infection and bleeding without "
            "treatment. The two curative-intent paths are allogeneic stem "
            "cell transplant (best in young patients with a matched donor) "
            "and immunosuppression with anti-thymocyte globulin plus "
            "cyclosporine plus eltrombopag, which can wake the marrow. "
            "Supportive care - transfusions, infection precautions - "
            "bridges the gap."
        ),
        "how_it_works": (
            "Aplastic anemia works as a factory shutdown by friendly fire. "
            "Autoreactive T lymphocytes infiltrate the marrow and destroy "
            "stem and progenitor cells; the few surviving stem cells cannot "
            "amplify enough to fill the blood, so every line falls together "
            "- the pancytopenia that separates marrow failure from single- "
            "line diseases. Because the defect is immune attack rather than "
            "a broken stem cell, suppressing the attackers can let the "
            "remnant stem cells regrow: anti-thymocyte globulin wipes the T "
            "cells, cyclosporine keeps them down, eltrombopag stimulates "
            "the surviving stem cells directly. The demo applies the "
            "Camitta grading to a case - cellularity 15 percent, neutrophils "
            "320, platelets 14,000, reticulocytes low - and returns the "
            "correct grade: severe aplastic anemia, transplant or "
            "immunosuppression urgently."
        ),
        "key_points": [
            "Empty marrow, pancytopenia: all three lines fall together with a fatty marrow.",
            "Most cases are autoimmune T-cell destruction of stem cells; drugs, benzene, and viruses can trigger it.",
            "Camitta criteria grade severity: cellularity under 25 percent plus two of neutrophils under 500, platelets under 20,000, reticulocytes under 20,000.",
            "Severe disease kills by infection and bleeding; treatment is transplant (young, matched donor) or ATG plus cyclosporine plus eltrombopag.",
            "Pancytopenia with a full marrow points elsewhere (leukemia, myeloma); with an empty marrow it is failure.",
        ],
        "requirements": [
            "The pancytopenia-plus-empty-marrow signature.",
            "The Camitta severity thresholds.",
            "The two treatment paths and who gets which.",
        ],
        "standards": [
            "Marrow biopsy required: cellularity under 25 percent defines the disease.",
            "Paroxysmal nocturnal hemoglobinuria testing, as the two overlap.",
            "No marrow-stimulating guesswork: grade first, then treat.",
        ],
        "citations": [CIT_KILLICK, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: aplastic anemia is the shipyard strike "
            "- the workers (stem cells) are driven out by the yard's own "
            "security force (T cells), and every slipway goes dark at once. "
            "The Camitta criteria are the strike severity scale. The fix is "
            "either importing a whole new workforce (transplant) or calling "
            "off the security forces and coaxing the remaining workers "
            "back (immunosuppression plus eltrombopag)."
        ),
    },
    {
        "key": "mds",
        "name": "Myelodysplastic Syndromes: Clonal Marrow Disorders",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Myelodysplastic syndromes (MDS) are clonal marrow disorders of "
            "older adults where the factory is full but the products are "
            "defective: stem cells acquire mutations, the marrow looks busy "
            "or even crowded, yet the cells it releases are misshapen "
            "(dysplastic) and die young, so the blood shows cytopenias - "
            "often anemia first - despite a cellular marrow. This "
            "ineffective production separates MDS from aplastic anemia "
            "(empty marrow). Diagnosis needs the biopsy: dysplasia in at "
            "least 10 percent of a lineage, blast percentage under 20 "
            "(20 or more is acute leukemia), and cytogenetics - chromosome "
            "5q deletion, monosomy 7, complex karyotypes - which drive "
            "prognosis. The Revised International Prognostic Scoring System "
            "(IPSS-R) combines cytogenetics, blast percent, hemoglobin, "
            "neutrophils, and platelets into risk from very low to very "
            "high; higher risk means faster progression to acute leukemia. "
            "Treatment runs from watchful waiting and growth factors in low "
            "risk, through hypomethylating agents (azacitidine) and "
            "lenalidomide for 5q deletion, to stem cell transplant - the "
            "only cure - in fit higher-risk patients."
        ),
        "how_it_works": (
            "MDS works as a factory taken over by a defective franchise. A "
            "mutated stem cell clone outcompetes normal stem cells, fills "
            "the marrow, but manufactures dysplastic cells that apoptose "
            "before or soon after release - full factory, empty shelves. "
            "The clone's genetic damage sets the trajectory: 5q deletion "
            "alone behaves gently, complex karyotypes race toward leukemia, "
            "and rising blast counts mark the slide - 5 to 10 percent is "
            "excess blasts, 20 percent is the leukemia line. IPSS-R scores "
            "the danger arithmetically. The demo scores a case - 7 percent "
            "blasts, poor cytogenetics, hemoglobin 8.5, neutrophils 600, "
            "platelets 65,000 - at 7.0 points: very high risk, transplant "
            "evaluation now."
        ),
        "key_points": [
            "Clonal disorder of older adults: full or crowded marrow, defective products, peripheral cytopenias.",
            "Ineffective production separates MDS (full marrow) from aplastic anemia (empty marrow).",
            "Diagnosis: dysplasia in 10 percent or more of a lineage, blasts under 20 percent, plus cytogenetics.",
            "IPSS-R combines cytogenetics, blasts, hemoglobin, neutrophils, platelets into very low to very high risk.",
            "Treatment: watch and support in low risk, azacitidine or lenalidomide (5q-) in the middle, transplant as the only cure in fit high-risk patients.",
        ],
        "requirements": [
            "The ineffective-production concept and the MDS vs aplasia split.",
            "The IPSS-R inputs and what each one measures.",
            "The 20 percent blast line between MDS and acute leukemia.",
        ],
        "standards": [
            "Cytogenetics on every new MDS marrow.",
            "Blast percent counted on a 500-cell differential.",
            "Transplant discussed early in higher-risk fit patients.",
        ],
        "citations": [CIT_GREENBERG, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: MDS is the franchise takeover - a "
            "mutant crew seizes the shipyard, keeps every slipway busy, "
            "and launches hulls so defective they sink at the dock. The "
            "shelves stay empty while the factory roars. IPSS-R is the "
            "takeover threat assessment: the worse the crew's rap sheet "
            "(cytogenetics) and the more half-built warships on the floor "
            "(blasts), the sooner the yard becomes a leukemia."
        ),
    },
    {
        "key": "itp",
        "name": "Immune Thrombocytopenia (ITP)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Immune thrombocytopenia is the platelet-destruction disease: "
            "autoantibodies tag the patient's own platelets, and the spleen "
            "clears them, so the count falls - often under 30,000 per "
            "microliter - while the marrow, trying to compensate, shows "
            "increased megakaryocytes. Bleeding is mucosal and skin-deep: "
            "petechiae, purpura, nosebleeds, gum bleeding, heavy periods; "
            "deep joint or muscle bleeds point away from ITP toward "
            "clotting-factor disease. ITP is a diagnosis of exclusion - no "
            "single test proves it - made by isolated thrombocytopenia "
            "with a normal smear and no other cause. Children often "
            "recover spontaneously after a viral illness; adults usually "
            "need treatment. First line is corticosteroids or IVIG; "
            "thrombopoietin receptor agonists (romiplostim, eltrombopag) "
            "drive the marrow to outproduce the destruction; rituximab and "
            "splenectomy are later options. Platelet transfusion is "
            "reserved for life-threatening bleeding - transfused platelets "
            "are destroyed just as fast."
        ),
        "how_it_works": (
            "ITP works as a bounty on the repair crews. Antiplatelet "
            "antibodies (usually against GPIIb/IIIa) coat circulating "
            "platelets; splenic macrophages read the antibody flags and "
            "devour them, cutting platelet lifespan from 10 days to hours. "
            "The marrow senses the shortage and ramps up megakaryocytes, "
            "releasing young, large platelets - which is why the MPV is "
            "often high. Treatment either disarms the bounty hunters "
            "(steroids dampen macrophages, IVIG blocks their receptors, "
            "rituximab deletes the antibody factories) or outbuilds the "
            "killing (TPO receptor agonists push megakaryocyte output past "
            "the destruction rate). The demo applies the treatment "
            "threshold: platelets 18,000 means treat; 75,000 with no "
            "bleeding means watch."
        ),
        "key_points": [
            "Autoantibodies tag platelets for splenic destruction; marrow shows compensatory megakaryocytes.",
            "Bleeding is mucosal and cutaneous (petechiae, purpura); deep bleeds suggest factor deficiency instead.",
            "Diagnosis of exclusion: isolated thrombocytopenia, normal smear, no other cause.",
            "Treat under 30,000 or with bleeding: steroids or IVIG first, TPO receptor agonists next, rituximab or splenectomy later.",
            "Platelet transfusion only for life-threatening bleeding; transfused platelets are destroyed too.",
        ],
        "requirements": [
            "The antibody-to-spleen destruction loop.",
            "The bleeding pattern that names platelets vs factors.",
            "The treatment ladder and the transfusion rule.",
        ],
        "standards": [
            "Smear reviewed to exclude pseudothrombocytopenia (EDTA clumping) and blasts.",
            "HCV and HIV checked as secondary causes.",
            "Children watched first; adults treated by the threshold.",
        ],
        "citations": [CIT_NEUNERT, CIT_HOFFBRAND, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: ITP is the bounty-hunter crisis - "
            "wanted posters (antibodies) on every repair crew, and the "
            "harbor patrol (the spleen) executes them on sight. The yard "
            "builds replacements frantically, but the hunters work faster. "
            "The admiral can bribe the hunters (steroids, IVIG), burn the "
            "poster printers (rituximab), close the execution dock "
            "(splenectomy), or simply outbuild the killing (TPO agonists)."
        ),
    },
    {
        "key": "coag_cascade",
        "name": "The Coagulation Cascade: How Blood Clots",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The coagulation cascade is the clotting chain reaction: a "
            "sequence of plasma proteases, each activating the next, that "
            "amplifies a tiny vessel-wall signal into a fibrin mesh. The "
            "classic map has two starting paths converging on factor X: "
            "the extrinsic (tissue factor plus factor VII - fast, measured "
            "by the PT/INR) and the intrinsic (factors XII, XI, IX, VIII - "
            "measured by the aPTT), joining at the common pathway (X, V, "
            "II/prothrombin, I/fibrinogen, XIII) that builds the clot. In "
            "the living vessel the cell-based model rules: tissue-factor- "
            "bearing cells initiate, platelets propagate, and the clot is "
            "built on cell surfaces. Natural brakes - antithrombin, protein "
            "C and S, tissue factor pathway inhibitor - keep the reaction "
            "from running away; their absence means thrombosis. The PT/INR "
            "watches the extrinsic and common paths (warfarin territory); "
            "the aPTT watches the intrinsic path (heparin territory, "
            "hemophilia screening). The mixing study sorts prolongations: "
            "correction with normal plasma means a factor is missing; no "
            "correction means an inhibitor is present."
        ),
        "how_it_works": (
            "The cascade works as an amplifier chain with brakes. One "
            "molecule of activated factor VII with tissue factor activates "
            "many molecules of factor X; each Xa with factor Va converts "
            "prothrombin to thrombin by the thousand; each thrombin "
            "converts fibrinogen to fibrin by the thousand more - three "
            "amplification steps turn a scratch into a seal in minutes. "
            "Factor XIII cross-links the fibrin for strength, and "
            "plasmin later dissolves the mesh when healing is done. The "
            "INR standardizes the PT across laboratories: patient PT over "
            "mean normal PT, raised to the ISI power. The demo computes it "
            "for PT 19.2 against normal 12.0 with ISI 1.1 - INR 1.68 - and "
            "states the mixing-study rule that sorts deficiency from "
            "inhibitor."
        ),
        "key_points": [
            "Two starting paths (extrinsic VII, intrinsic XII-XI-IX-VIII) converge on factor X and the common pathway to fibrin.",
            "Each step amplifies: one VIIa makes many Xa, each Xa makes a thousand thrombins, each thrombin makes a thousand fibrins.",
            "Natural brakes - antithrombin, protein C/S, TFPI - prevent runaway clotting; their loss means thrombosis.",
            "PT/INR watches extrinsic plus common (warfarin); aPTT watches intrinsic (heparin, hemophilia).",
            "Mixing study: correction means factor deficiency, no correction means inhibitor.",
        ],
        "requirements": [
            "The cascade map: factors in order, the convergence on X, the common pathway.",
            "The amplification logic and the three brakes.",
            "PT/INR vs aPTT territory and the mixing-study rule.",
        ],
        "standards": [
            "Factors named by Roman numeral; activated forms with 'a'.",
            "INR formula: (patient PT / mean normal PT) raised to ISI.",
            "Therapeutic INR 2.0 to 3.0 for most warfarin indications.",
        ],
        "citations": [CIT_VERSTEEG, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: the cascade is the fleet's emergency "
            "welding protocol - a chain of foremen where each one shouts "
            "ten times louder than the last, so a pinhole leak summons a "
            "full repair crew in minutes. The brakes are the safety "
            "inspectors who stop the welders from sealing the whole harbor. "
            "The INR is the standardized weld gauge; the mixing study is "
            "the interrogation that tells a missing welder from a saboteur."
        ),
    },
    {
        "key": "hemophilia_vwd",
        "name": "Hemophilia and von Willebrand Disease",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Hemophilia and von Willebrand disease are the inherited "
            "bleeding disorders of the clotting chain. Hemophilia A "
            "(factor VIII deficiency) and B (factor IX deficiency) are "
            "X-linked, so they strike boys: severe disease (under 1 percent "
            "factor) bleeds spontaneously into joints (hemarthrosis) and "
            "muscles, moderate (1 to 5 percent) bleeds with minor trauma, "
            "mild (5 to 40 percent) bleeds with surgery. The aPTT is "
            "prolonged; the PT is normal. Treatment is factor replacement - "
            "now extended half-life products and, for hemophilia A, the "
            "bispecific antibody emicizumab - with the great complication "
            "being inhibitors (antibodies against the replacement factor). "
            "Von Willebrand disease, the most common inherited bleeding "
            "disorder, is usually autosomal dominant: defective or low von "
            "Willebrand factor impairs platelet sticking and carries less "
            "factor VIII, causing mucosal bleeding - nosebleeds, heavy "
            "periods, bleeding after dental work - in both sexes. "
            "Desmopressin releases stored VWF in mild type 1; VWF "
            "concentrates cover the rest."
        ),
        "how_it_works": (
            "These disorders work as missing links in the welding chain. "
            "Factor VIII is the essential cofactor that lets factor IXa "
            "activate factor X efficiently - without it, the intrinsic "
            "path stalls and the aPTT stretches while the PT, which bypasses "
            "VIII, stays normal. Von Willebrand factor is the double agent: "
            "it glues platelets to injured vessel walls and chaperones "
            "factor VIII in the blood, so its loss bleeds from both the "
            "platelet side and the factor side. Severity follows the factor "
            "level arithmetically. The demo grades two cases: factor VIII "
            "0.4 percent is severe hemophilia A, VWF activity 28 percent "
            "with mucosal bleeding is von Willebrand disease."
        ),
        "key_points": [
            "Hemophilia A (VIII) and B (IX) are X-linked: severe under 1 percent bleeds spontaneously into joints and muscles.",
            "aPTT prolonged with normal PT is the hemophilia lab signature.",
            "Inhibitors - antibodies against replacement factor - are the great treatment complication.",
            "Von Willebrand disease is the most common inherited bleeding disorder, autosomal dominant, with mucosal bleeding in both sexes.",
            "Desmopressin for mild type 1 VWD; factor or VWF concentrates for the rest.",
        ],
        "requirements": [
            "The X-linked inheritance and the severity bands.",
            "The aPTT-prolonged/PT-normal signature.",
            "VWF's double job: platelet glue and factor VIII chaperone.",
        ],
        "standards": [
            "Factor levels as percent of normal; severity bands 1 / 5 / 40.",
            "Inhibitor screening with the Bethesda assay.",
            "Genetic counseling for X-linked families.",
        ],
        "citations": [CIT_WFH, CIT_VWD, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: hemophilia is the missing foreman - "
            "the welding crew stands ready but the one foreman who "
            "amplifies the whole line never shows, so deep hulls bleed "
            "where the inspectors cannot see. Von Willebrand disease is "
            "the faulty harbor glue - the tugboats (platelets) cannot grip "
            "the dock walls, and the foreman they were carrying (factor "
            "VIII) drifts away unprotected."
        ),
    },
    {
        "key": "vte",
        "name": "Venous Thromboembolism and Thrombophilia",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Venous thromboembolism - deep vein thrombosis and pulmonary "
            "embolism - is clotting in the wrong place: a DVT forms in the "
            "leg or arm veins (pain, swelling, warmth), and pieces can break "
            "off, ride to the lungs, and become a pulmonary embolism "
            "(sudden breathlessness, chest pain, fast heart rate), which "
            "can kill in minutes when massive. Virchow's triad names the "
            "three triggers: stasis (immobility, long flights, hospital "
            "beds), endothelial injury (surgery, catheters, trauma), and "
            "hypercoagulability (cancer, pregnancy, hormones, inherited "
            "thrombophilia like factor V Leiden and the prothrombin gene "
            "mutation). The Wells score grades pretest probability from "
            "bedside features - 2 or more means DVT is likely - and the "
            "diagnostic path runs D-dimer for low probability, compression "
            "ultrasound for the leg, CT angiography for the lung. "
            "Treatment is anticoagulation: heparin or a direct oral "
            "anticoagulant first, at least 3 months, longer with cancer or "
            "recurrence."
        ),
        "how_it_works": (
            "VTE works as Virchow's triad in action: slow blood lets "
            "clotting factors linger and meet, injured endothelium exposes "
            "tissue factor, and hypercoagulable blood over-answers both. "
            "The thrombus grows in the valve pockets of deep veins where "
            "flow is slowest; a fragile tail can embolize to the pulmonary "
            "arteries, where it raises dead-space ventilation and strains "
            "the right heart. The Wells score turns bedside findings into "
            "arithmetic: active cancer, immobilization, whole-leg swelling, "
            "calf asymmetry, pitting edema, prior DVT each add a point, an "
            "alternative diagnosis subtracts two. The demo scores a case - "
            "cancer, whole-leg swelling, calf asymmetry, edema, prior DVT, "
            "no alternative - at 5 points: DVT likely, ultrasound now."
        ),
        "key_points": [
            "DVT in the limb veins can embolize to the lungs as pulmonary embolism; massive PE kills by right-heart strain.",
            "Virchow's triad: stasis, endothelial injury, hypercoagulability.",
            "Inherited thrombophilia: factor V Leiden and prothrombin G20210A are the common ones; test after unprovoked clots.",
            "Wells score 2 or more means DVT likely; D-dimer rules out low probability, ultrasound and CT confirm.",
            "Anticoagulate at least 3 months; longer with cancer, recurrence, or ongoing risk.",
        ],
        "requirements": [
            "Virchow's triad and an example of each trigger.",
            "The Wells score items and the 2-point likely line.",
            "The diagnostic path: D-dimer, ultrasound, CT angiography.",
        ],
        "standards": [
            "Wells scored before the D-dimer, not after.",
            "D-dimer only rules out in low-probability patients.",
            "Provoked vs unprovoked clots set the treatment duration.",
        ],
        "citations": [CIT_CHEST, CIT_WILLIAMS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: VTE is the harbor silting up - slow "
            "water (stasis), damaged docks (endothelial injury), and "
            "over-eager welders (hypercoagulability) conspire to seal a "
            "channel that should stay open, and a chunk of the blockage can "
            "break free and jam the lung harbor's entrance. The Wells score "
            "is the harbor master's risk arithmetic; anticoagulation is "
            "the dredging operation that keeps the channels open for "
            "months."
        ),
    },
]

ENTRIES += [
    {
        "key": "acute_leuk",
        "name": "Acute Leukemia: AML and ALL",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Acute leukemias are the marrow overrun by blasts: immature "
            "white-cell precursors multiply without maturing, crowd out "
            "normal production, and spill into the blood. Twenty percent or "
            "more blasts in marrow or blood defines acute leukemia. Acute "
            "myeloid leukemia (AML) is the adult disease - median age near "
            "70 - presenting with fatigue and bleeding from marrow failure, "
            "infections from neutropenia, and sometimes gum or skin "
            "infiltration; genetics rule prognosis and treatment, from the "
            "favorable NPM1 and core-binding-factor subtypes to the grim "
            "TP53 and complex karyotypes, with FLT3, IDH1, and IDH2 now "
            "directly druggable. Acute lymphoblastic leukemia (ALL) is the "
            "childhood disease - the most common childhood cancer - and the "
            "pediatric success story, with cure rates over 85 percent from "
            "multi-agent chemotherapy; adult ALL is harder and increasingly "
            "uses blinatumomab, inotuzumab, and CAR-T cells. Both can "
            "present as emergencies: leukostasis when blast counts soar, "
            "tumor lysis when treatment starts, and disseminated "
            "intravascular coagulation in acute promyelocytic leukemia, "
            "which is itself curable with all-trans retinoic acid plus "
            "arsenic."
        ),
        "how_it_works": (
            "Acute leukemia works as a differentiation blockade plus a "
            "proliferation license. Mutations freeze precursors at the "
            "blast stage - they divide but never mature - so blasts "
            "accumulate, fill the marrow, and suppress normal red cell, "
            "neutrophil, and platelet production; the patient feels the "
            "crowding as fatigue, bleeding, and infection. Cytogenetics and "
            "molecular profiling read the blockade's wiring: each mutation "
            "pattern predicts behavior and, increasingly, dictates a "
            "targeted drug. Treatment clears the blasts in phases - "
            "induction to empty the marrow, consolidation to kill remnants, "
            "maintenance in ALL - and transplant replaces the factory when "
            "genetics demand it. The demo checks the diagnostic line: a "
            "white count of 42,000 with 55 percent blasts is 23,100 blasts "
            "per microliter - acute leukemia by the 20 percent rule, workup "
            "and treatment as an emergency."
        ),
        "key_points": [
            "Twenty percent or more blasts in marrow or blood defines acute leukemia.",
            "AML is the adult disease, genetics-driven (NPM1, FLT3, IDH1/2, TP53); ALL is the childhood disease, over 85 percent cured.",
            "Presentation is marrow failure: fatigue, bleeding, infection - plus leukostasis and tumor lysis as emergencies.",
            "Acute promyelocytic leukemia brings DIC but is curable with all-trans retinoic acid plus arsenic.",
            "Treatment phases: induction, consolidation, maintenance (ALL); transplant for adverse genetics.",
        ],
        "requirements": [
            "The 20 percent blast rule and the differentiation-blockade concept.",
            "AML vs ALL: age patterns, genetic drivers, targeted drugs.",
            "The emergencies: leukostasis, tumor lysis, APL with DIC.",
        ],
        "standards": [
            "Blast percent counted on marrow aspirate differential.",
            "Cytogenetics and molecular panel on every new acute leukemia.",
            "APL treated as a medical emergency on suspicion, not confirmation.",
        ],
        "citations": [CIT_DOHNER, CIT_MAUDE, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: acute leukemia is the mutiny of the "
            "cadets - the yard's apprentices seize the slipways, multiply "
            "without ever graduating, and crowd the real ships out of the "
            "harbor. The 20 percent line is the mutiny threshold. Genetics "
            "is the mutineers' manifesto: read it and you know which "
            "rebellion negotiates (targeted drugs), which needs the yard "
            "burned and rebuilt (transplant), and which surrenders to the "
            "right signal (ATRA in APL)."
        ),
    },
    {
        "key": "chronic_leuk",
        "name": "Chronic Leukemias: CLL and CML",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Chronic leukemias are the slow accumulations: mature-looking "
            "white cells pile up over years rather than exploding in "
            "weeks. Chronic lymphocytic leukemia (CLL), the most common "
            "adult leukemia in the West, is a disease of accumulation, not "
            "proliferation - long-lived B lymphocytes that refuse to die "
            "gather in blood, marrow, and nodes; many patients need no "
            "treatment for years, and treatment starts on criteria (rapid "
            "lymphocyte doubling under 12 months, bulky nodes, marrow "
            "failure, B symptoms), not on the count alone. Prognosis is "
            "read in the genes: mutated IGHV is gentle, unmutated IGHV, "
            "TP53, and 17p deletion are aggressive - and modern therapy "
            "follows: BTK inhibitors (ibrutinib, acalabrutinib) and BCL2 "
            "inhibition (venetoclax) have displaced chemotherapy for most. "
            "Chronic myeloid leukemia (CML) is the Philadelphia-chromosome "
            "disease - BCR-ABL1, one translocation driving everything - and "
            "the targeted-therapy miracle: tyrosine kinase inhibitors "
            "(imatinib and its successors) turned a fatal leukemia into a "
            "chronic condition with near-normal life expectancy, monitored "
            "by BCR-ABL1 transcript levels, with treatment-free remission "
            "possible after deep, sustained response."
        ),
        "how_it_works": (
            "Chronic leukemias work as immortal-hoarding, not wildfire. In "
            "CLL the malignant B cells divide slowly but die even more "
            "slowly - defective apoptosis - so the count climbs month by "
            "month; the lymphocyte doubling time measures the hoard's "
            "speed, and under 12 months signals active disease needing "
            "treatment. In CML a single translocation fuses BCR to ABL1, "
            "creating a always-on tyrosine kinase that drives myeloid "
            "overproduction; blocking that one kinase with imatinib "
            "collapses the whole disease, which is why CML became the "
            "proof that targeted therapy can tame leukemia. The demo "
            "computes a lymphocyte doubling time - 25,000 to 50,000 in 9 "
            "months gives 9.0 months, under the 12-month line - and returns "
            "the correct call: active CLL, treatment indicated."
        ),
        "key_points": [
            "CLL is accumulation by failed apoptosis; CML is overproduction driven by one kinase (BCR-ABL1).",
            "CLL treatment starts on criteria - doubling under 12 months, bulky disease, marrow failure - not on count alone.",
            "IGHV, TP53, and 17p deletion set CLL prognosis; BTK and BCL2 inhibitors are the modern backbone.",
            "CML's Philadelphia chromosome made it the targeted-therapy miracle: TKIs give near-normal life expectancy.",
            "BCR-ABL1 transcript monitoring guides CML therapy; deep sustained response can allow treatment-free remission.",
        ],
        "requirements": [
            "Accumulation vs proliferation: the CLL/CML conceptual split.",
            "The CLL treatment triggers and prognostic markers.",
            "The BCR-ABL1 story and transcript monitoring.",
        ],
        "standards": [
            "Lymphocyte doubling time computed from two counts and the interval.",
            "FISH and IGHV/TP53 testing before CLL treatment selection.",
            "CML response graded by BCR-ABL1 transcript milestones.",
        ],
        "citations": [CIT_HALLEK, CIT_HOCHHAUS, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: chronic leukemias are the slow "
            "hoarders, not the mutineers - CLL is the warehouse that never "
            "throws anything away, filling with immortal clerks; CML is "
            "the single broken throttle (BCR-ABL1) stuck wide open. The "
            "doubling time is the hoard's speedometer. And CML is the "
            "fleet's proudest proof: find the one broken part, jam it "
            "with a precision tool (imatinib), and a death sentence "
            "becomes a maintenance schedule."
        ),
    },
    {
        "key": "lymphoma",
        "name": "Lymphoma: Hodgkin and Non-Hodgkin",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Lymphomas are cancers of the lymphatic system - lymph nodes, "
            "spleen, and lymphoid tissue - presenting with painless node "
            "enlargement and, in Hodgkin lymphoma, the B symptoms: fevers, "
            "drenching night sweats, and weight loss. Hodgkin lymphoma is "
            "defined by the Reed-Sternberg cell and spreads in orderly "
            "fashion from node group to node group; it is one of the most "
            "curable cancers, with ABVD chemotherapy curing the large "
            "majority of early-stage patients. Non-Hodgkin lymphomas are "
            "the diverse majority: diffuse large B-cell lymphoma (DLBCL), "
            "the common aggressive one, cured about 60 percent of the time "
            "with R-CHOP chemoimmunotherapy; follicular lymphoma, the "
            "common indolent one, often watched for years before treatment; "
            "Burkitt lymphoma, the fastest-growing human tumor, demanding "
            "urgent intensive therapy; and mantle cell, marginal zone, and "
            "T-cell varieties each with their own behavior. Staging follows "
            "Ann Arbor: I (one region), II (two or more, same side of the "
            "diaphragm), III (both sides), IV (disseminated), with A/B for "
            "absence or presence of B symptoms - and the biopsy, with "
            "immunophenotyping, names the enemy before any treatment."
        ),
        "how_it_works": (
            "Lymphoma works as a lymph-node rebellion with a postal code. "
            "The malignant lymphocytes home to lymphoid tissue and multiply "
            "there, so the disease announces itself as nodal masses; "
            "Hodgkin's Reed-Sternberg cells are rare giants (often under 1 "
            "percent of the tumor) orchestrating an inflammatory crowd, "
            "while non-Hodgkin lymphomas are sheets of the malignant clone. "
            "Ann Arbor staging maps the rebellion's territory: count the "
            "involved regions, note which side of the diaphragm, add B for "
            "systemic symptoms. Treatment matches aggression to aggression: "
            "curative-intent chemoimmunotherapy for DLBCL and Hodgkin, "
            "watchful waiting for asymptomatic follicular, blitz therapy "
            "for Burkitt. The demo stages a case - cervical plus axillary "
            "nodes on one side with night sweats - as stage IIB, and notes "
            "the rule: biopsy with immunophenotyping first, always."
        ),
        "key_points": [
            "Hodgkin: Reed-Sternberg cells, orderly spread, B symptoms, highly curable with ABVD.",
            "DLBCL: the common aggressive NHL, about 60 percent cured with R-CHOP.",
            "Follicular: the common indolent NHL, often watched for years; Burkitt: fastest-growing, treated as an emergency.",
            "Ann Arbor I-IV by regions and diaphragm side, A/B by B symptoms.",
            "Excisional biopsy with immunophenotyping names the lymphoma before treatment.",
        ],
        "requirements": [
            "Hodgkin vs non-Hodgkin: the Reed-Sternberg definition and the spread pattern.",
            "The big three NHL behaviors: aggressive, indolent, blastic.",
            "Ann Arbor staging arithmetic.",
        ],
        "standards": [
            "Excisional node biopsy preferred over needle for architecture.",
            "PET-CT for staging aggressive lymphomas.",
            "B symptoms documented as they change stage and prognosis.",
        ],
        "citations": [CIT_EICHENAUER, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: lymphoma is the rebellion of the "
            "harbor garrisons - the lymph nodes, the fleet's own coastal "
            "forts, turning against the command. Hodgkin marches in "
            "formation, fort to neighboring fort, and surrenders reliably "
            "to ABVD. The non-Hodgkin rebels are a rabble of factions: the "
            "DLBCL shock troops (hit hard with R-CHOP), the follicular "
            "slow-burners (watch and wait), the Burkitt blitzkrieg "
            "(fastest assault in human oncology - answer in hours)."
        ),
    },
    {
        "key": "myeloma",
        "name": "Multiple Myeloma and Plasma Cell Disorders",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Multiple myeloma is the plasma cell cancer: malignant plasma "
            "cells fill the marrow and pour out a single useless antibody - "
            "the M-protein or M-spike - while crowding out normal blood "
            "production. The CRAB criteria name the organ damage that "
            "defines active disease: Calcium elevation, Renal failure, "
            "Anemia, Bone lesions (lytic holes and fractures, with the "
            "classic raindrop skull). The M-protein injures kidneys as "
            "cast nephropathy and light chains deposit as amyloidosis; "
            "suppressed normal immunoglobulins bring recurrent infections. "
            "Diagnosis needs 10 percent or more clonal marrow plasma cells "
            "plus a myeloma-defining event (CRAB or biomarkers like 60 "
            "percent plasma cells, extreme light-chain ratio, or focal "
            "MRI lesions). Precursors - MGUS and smoldering myeloma - are "
            "watched, not treated. Treatment layers proteasome inhibitors "
            "(bortezomib), immunomodulators (lenalidomide), anti-CD38 "
            "antibodies (daratumumab), autologous transplant in fit "
            "patients, and now bispecific antibodies and CAR-T cells; "
            "myeloma is increasingly a chronic, managed disease."
        ),
        "how_it_works": (
            "Myeloma works as a counterfeit factory inside the shipyard. "
            "One plasma cell clone multiplies and manufactures a single "
            "antibody type by the ton - useless for defense, toxic in "
            "bulk: it thickens the blood, clogs kidney tubules as casts, "
            "and its light chains poison organs as amyloid. Meanwhile the "
            "malignant cells secrete factors that activate osteoclasts, "
            "drilling lytic holes in bone while suppressing rebuilding - "
            "the punched-out lesions and fractures. The CRAB checklist "
            "turns organ damage into arithmetic: calcium over 11.5, "
            "creatinine over 2, hemoglobin under 10, any lytic lesion. The "
            "demo runs it on calcium 11.8, creatinine 2.3, hemoglobin 9.2, "
            "plus skull lesions with an M-spike of 3.2 - four of four CRAB, "
            "active myeloma, treatment now."
        ),
        "key_points": [
            "Malignant plasma cells fill marrow and secrete a useless monoclonal M-protein.",
            "CRAB defines active disease: Calcium over 11.5, Renal creatinine over 2, Anemia hemoglobin under 10, Bone lytic lesions.",
            "M-protein injures kidneys (cast nephropathy); light chains deposit as amyloidosis.",
            "MGUS and smoldering myeloma are watched, not treated.",
            "Modern layers: proteasome inhibitors, immunomodulators, anti-CD38, autologous transplant, bispecifics, CAR-T.",
        ],
        "requirements": [
            "The counterfeit-factory concept: clonal plasma cells plus M-protein.",
            "The CRAB thresholds as diagnostic arithmetic.",
            "Precursor states and why they are watched.",
        ],
        "standards": [
            "M-protein quantified by serum protein electrophoresis with immunofixation.",
            "Marrow plasma cells counted at 10 percent as the diagnostic line.",
            "Skeletal survey or advanced imaging for lytic disease.",
        ],
        "citations": [CIT_RAJKUMAR, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: myeloma is the counterfeit mint inside "
            "the shipyard - one rogue press stamping a single worthless "
            "coin by the ton, jamming the kidneys' filters, while its "
            "demolition crews (osteoclasts) drill the drydock full of "
            "holes. CRAB is the damage audit: four checkboxes that turn "
            "suspicion into a treatment order. The modern answer is layered "
            "siege warfare - and the mint is increasingly besieged, not "
            "victorious."
        ),
    },
    {
        "key": "mpn",
        "name": "Myeloproliferative Neoplasms: PV, ET, and Myelofibrosis",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Myeloproliferative neoplasms are the overproduction disorders: "
            "clonal stem cells churn out too many mature blood cells. "
            "Polycythemia vera (PV) overproduces red cells - hemoglobin "
            "over 16.5 in men or 16.0 in women with JAK2 mutation nearly "
            "always present - thickening the blood toward clotting and "
            "treated by phlebotomy to a hematocrit under 45 percent plus "
            "low-dose aspirin, with cytoreduction for high-risk patients. "
            "Essential thrombocythemia (ET) overproduces platelets, often "
            "over a million, with clotting and sometimes paradoxical "
            "bleeding from acquired von Willebrand factor loss at extreme "
            "counts. Primary myelofibrosis scars the marrow itself: "
            "fibrosis crowds out production, blood-making moves to the "
            "spleen (extramedullary hematopoiesis, massive "
            "spleen), and teardrop red cells appear on the smear. JAK2, "
            "CALR, and MPL mutations drive the family; JAK inhibitors "
            "(ruxolitinib) shrink spleens and ease symptoms; transplant is "
            "the only cure for myelofibrosis in fit patients."
        ),
        "how_it_works": (
            "MPNs work as a stuck accelerator on the production line. JAK2 "
            "mutations (especially V617F) leave the growth-factor signaling "
            "switch jammed on, so progenitors multiply without orders - red "
            "cells in PV, platelets in ET, and in myelofibrosis a storm of "
            "cytokines that scars the marrow with reticulin fibrosis. "
            "Thick blood in PV raises viscosity and clot risk in direct "
            "proportion to the hematocrit, which is why phlebotomy targets "
            "under 45 percent: each 500 mL removal drops the red cell mass "
            "measurably. The demo computes the phlebotomy arithmetic for "
            "hematocrit 57 percent in a 5-liter blood volume: about 1.05 "
            "liters of whole blood must come off to reach the 45 percent "
            "target."
        ),
        "key_points": [
            "PV: red cell overproduction, JAK2 nearly always, phlebotomy to hematocrit under 45 percent plus aspirin.",
            "ET: platelet overproduction, clotting risk, paradoxical bleeding at extreme counts.",
            "Myelofibrosis: marrow scarring, extramedullary blood-making, massive spleen, teardrop cells.",
            "Driver mutations: JAK2, CALR, MPL; JAK inhibitors shrink spleens and ease symptoms.",
            "Thrombosis is the shared killer; transplant is the myelofibrosis cure in fit patients.",
        ],
        "requirements": [
            "The stuck-accelerator concept and the three driver mutations.",
            "The PV diagnostic pair: hemoglobin thresholds plus JAK2.",
            "The 45 percent hematocrit target and why it exists.",
        ],
        "standards": [
            "Hemoglobin over 16.5 (men) or 16.0 (women) as the PV red flag.",
            "JAK2/CALR/MPL testing in every suspected MPN.",
            "Cardiovascular risk managed alongside the counts.",
        ],
        "citations": [CIT_TEFFERI, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: MPNs are the runaway assembly line - "
            "the throttle (JAK2) welded wide open, the yard launching "
            "freighters (PV) or repair crews (ET) far past demand until "
            "the harbor silts with traffic. Myelofibrosis is the yard "
            "paving its own slipways in concrete and outsourcing "
            "construction to the spleen. Phlebotomy is the controlled "
            "release valve; JAK inhibitors are the throttle repair crew."
        ),
    },
    {
        "key": "dic",
        "name": "Disseminated Intravascular Coagulation (DIC)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Disseminated intravascular coagulation is clotting and bleeding "
            "at once: a massive trigger - sepsis, trauma, obstetric "
            "catastrophe, acute promyelocytic leukemia, severe burns - "
            "activates coagulation everywhere in the bloodstream, forming "
            "microthrombi that consume platelets and clotting factors until "
            "nothing is left to seal real wounds, so the patient clots in "
            "the microcirculation and bleeds from every line and puncture "
            "at the same time. The labs show the consumption: falling "
            "platelets, prolonged PT and aPTT, low fibrinogen, and soaring "
            "D-dimer and fibrin degradation products. The ISTH scoring "
            "system grades it: platelets under 100,000 (1 point) or under "
            "50,000 (2), strong D-dimer rise (2 to 3), PT prolonged 3 to 6 "
            "seconds (1) or 6-plus (2), fibrinogen under 100 mg per dL (1) - "
            "5 or more means overt DIC. Treatment is the trigger: control "
            "the sepsis, evacuate the uterus, treat the leukemia; blood "
            "products replace what is consumed in the bleeding patient; "
            "heparin has narrow, debated roles."
        ),
        "how_it_works": (
            "DIC works as a bank run on the clotting system. Tissue factor "
            "flooding the blood from the trigger flips the extrinsic path "
            "on everywhere at once; thrombin generation explodes; "
            "fibrin forms in thousands of small vessels while platelets and "
            "factors are spent wholesale. The microthrombi injure organs - "
            "kidneys, lungs, brain - even as the emptied accounts leave "
            "venipuncture sites oozing. Natural anticoagulants (antithrombin, "
            "protein C) are consumed too, removing the brakes. The ISTH "
            "score audits the accounts. The demo scores a case - platelets "
            "38,000, D-dimer strongly elevated, PT prolonged 7 seconds, "
            "fibrinogen 85 - at 8 points: overt DIC, treat the trigger and "
            "replace products in the bleeding patient."
        ),
        "key_points": [
            "Simultaneous microvascular clotting and bleeding from consumption of platelets and factors.",
            "Triggers: sepsis, trauma, obstetric catastrophe, acute promyelocytic leukemia, burns.",
            "Labs: falling platelets, prolonged PT/aPTT, low fibrinogen, soaring D-dimer.",
            "ISTH score 5 or more means overt DIC.",
            "Treatment is the trigger; products for the bleeding patient; heparin narrowly and debatably.",
        ],
        "requirements": [
            "The consumption concept: clotting everywhere empties the accounts.",
            "The trigger list and why each one fires tissue factor.",
            "The ISTH score items and the 5-point line.",
        ],
        "standards": [
            "Fibrinogen under 100 mg per dL as the critical threshold.",
            "Scores repeated as the trigger evolves.",
            "No isolated D-dimer diagnosis: the full panel scores together.",
        ],
        "citations": [CIT_LEVI, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: DIC is the bank run - every welder in "
            "the harbor striking at once on a false alarm, spending the "
            "entire parts inventory in minutes, so the harbor is both "
            "jammed with half-built seals and unable to patch a real leak. "
            "The ISTH score is the audit of the empty accounts. The "
            "admiral does not restock during the run - he stops the panic "
            "(treats the trigger) and only then refills the shelves."
        ),
    },
    {
        "key": "transfusion",
        "name": "Transfusion Medicine: Blood Products and Compatibility",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Transfusion medicine is the logistics of borrowed blood: "
            "collecting, testing, separating, and matching blood so it "
            "helps instead of harms. Whole blood is separated into red "
            "cells (for anemia and bleeding), platelets (for low counts "
            "and platelet dysfunction), plasma (for clotting-factor "
            "replacement), and cryoprecipitate (concentrated fibrinogen). "
            "Compatibility is the ABO system plus Rh: group O red cells go "
            "to anyone, AB recipients take anyone's red cells, and plasma "
            "compatibility runs in reverse (AB plasma is the universal "
            "donor). The type and screen - ABO/Rh typing plus antibody "
            "screen - with crossmatch for red cells prevents hemolytic "
            "reactions. Modern practice is restrictive: the 2023 AABB "
            "guidelines recommend transfusion thresholds of 7 g per dL for "
            "stable hospitalized adults (8 with heart disease or "
            "orthopedic surgery), because trials show restrictive "
            "transfusion is as safe as liberal and spares a scarce, "
            "precious resource. Every unit is tested for HIV, HBV, HCV, "
            "and other transmissible infections."
        ),
        "how_it_works": (
            "Transfusion works as a matched-parts exchange. Donor red cells "
            "carry A and/or B antigens; recipient plasma carries antibodies "
            "against whichever antigens it lacks - anti-A, anti-B, or both - "
            "so mismatched red cells are destroyed on arrival in an acute "
            "hemolytic reaction. Group O cells carry neither antigen and "
            "dodge all three antibodies: the universal red cell donor. "
            "RhD-negative blood goes to RhD-negative recipients and to "
            "women of childbearing potential to prevent sensitization. The "
            "demo encodes the ABO compatibility matrix - donor O to all, "
            "donor AB to AB only, recipient AB from all - and verifies six "
            "pairings against the matrix."
        ),
        "key_points": [
            "Components: red cells, platelets, plasma, cryoprecipitate - each for its own indication.",
            "ABO compatibility: O red cells to anyone, AB recipients from anyone; plasma runs in reverse.",
            "Type and screen plus crossmatch prevents hemolytic reactions; RhD-negative for childbearing-potential women.",
            "Restrictive thresholds: 7 g per dL stable adults, 8 with cardiac disease (2023 AABB).",
            "Every unit screened for HIV, HBV, HCV, and other infections.",
        ],
        "requirements": [
            "The ABO antigen-antibody logic and the universal donor/recipient rules.",
            "The component list and what each one replaces.",
            "The restrictive threshold numbers and who they apply to.",
        ],
        "standards": [
            "Two-identifier patient check at the bedside before every unit.",
            "Type and screen valid per local policy, usually 72 hours.",
            "Transfusion consent with risks disclosed.",
        ],
        "citations": [CIT_CARSON, CIT_WILLIAMS, CIT_HOFFBRAND],
        "sig_lens": (
            "His Signature reading: transfusion is the allied resupply "
            "convoy - borrowed hulls and parts sailed into a friendly "
            "harbor. ABO is the harbor's recognition-signal code: fly the "
            "wrong flag (antigen) and the shore batteries (antibodies) open "
            "fire. Group O is the plain-flagged freighter every harbor "
            "accepts. The restrictive threshold is wartime rationing "
            "wisdom: spend the convoy's cargo only where it changes the "
            "battle."
        ),
    },
    {
        "key": "transfusion_reactions",
        "name": "Transfusion Reactions and Hemovigilance",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Transfusion reactions are what goes wrong with borrowed blood, "
            "and hemovigilance is the system that watches for them. The "
            "reactions sort by timing and signature: acute hemolytic "
            "(ABO mismatch - fever, chills, flank pain, red urine, "
            "hypotension during the unit; stop the transfusion, hydrate, "
            "notify the blood bank), febrile non-hemolytic (fever and "
            "chills from recipient antibodies to donor white cells; "
            "leukoreduction has made it rarer), allergic (hives alone - "
            "pause, antihistamine, resume; anaphylaxis with airway "
            "involvement - stop, epinephrine), TRALI - transfusion-related "
            "acute lung injury (breathlessness and low oxygen within 6 "
            "hours, no fluid overload; supportive care, the leading cause "
            "of transfusion death), and TACO - transfusion-associated "
            "circulatory overload (breathlessness with hypertension, "
            "jugular distension, and fluid overload; sit up, diurese, slow "
            "future transfusions). Delayed hemolytic reactions surface days "
            "later as falling hemoglobin with a positive antibody screen. "
            "The iron rule: any concerning symptom during transfusion - "
            "stop the unit first, assess second."
        ),
        "how_it_works": (
            "Reactions sort by a two-question triage: when did it start, "
            "and what is the signature? During the unit with flank pain "
            "and red urine means acute hemolytic - the ABO mismatch alarm, "
            "complement destroying donor cells intravascularly. Within 6 "
            "hours with breathlessness splits on volume: low oxygen without "
            "overload signs is TRALI (donor antibodies attacking recipient "
            "neutrophils in the lungs); with hypertension and distended "
            "neck veins it is TACO (too much volume too fast). Fever with "
            "chills alone is febrile non-hemolytic; hives alone is "
            "allergic. The demo runs the triage on three vignettes - "
            "flank pain during the unit, breathlessness without overload "
            "at 3 hours, hives alone - and returns hemolytic, TRALI, and "
            "allergic."
        ),
        "key_points": [
            "Acute hemolytic (ABO mismatch): flank pain, red urine, hypotension during the unit - stop, hydrate, call the blood bank.",
            "TRALI: breathlessness and low oxygen within 6 hours without overload - leading cause of transfusion death.",
            "TACO: breathlessness with hypertension and overload signs - sit up, diurese, slow future units.",
            "Febrile non-hemolytic: fever and chills alone; allergic: hives alone.",
            "The iron rule: stop the unit first with any concerning symptom, assess second.",
        ],
        "requirements": [
            "The five reaction signatures and their timing.",
            "The TRALI vs TACO split: overload signs present or absent.",
            "The stop-first rule and the hemovigilance reporting chain.",
        ],
        "standards": [
            "Vital signs before, during, and after every unit.",
            "Suspected hemolytic reaction: return the bag and tubing to the blood bank.",
            "Every reaction reported through hemovigilance.",
        ],
        "citations": [CIT_CARSON, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: reactions are the convoy gone wrong - "
            "friendly fire (ABO mismatch), sabotage in the lungs (TRALI), "
            "flooding the harbor (TACO), or mere seasickness (febrile, "
            "allergic). Hemovigilance is the harbor's incident-report "
            "system: every collision logged, every near-miss studied, so "
            "the next convoy sails safer. And the standing order never "
            "changes: when the alarm sounds, stop the ships first and ask "
            "questions second."
        ),
    },
]

ENTRIES += [
    {
        "key": "hsct",
        "name": "Hematopoietic Stem Cell Transplantation",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hematopoietic stem cell transplantation replaces the entire "
            "blood factory: high-dose chemotherapy (with or without "
            "radiation) empties the diseased marrow, and infused donor or "
            "rescued stem cells home to the bone and rebuild it. Allogeneic "
            "transplant (donor cells) adds the graft-versus-leukemia effect "
            "- donor immune cells hunting residual cancer - which is why "
            "it cures leukemias, aplastic anemia, thalassemia major, sickle "
            "cell disease, and immune deficiencies; its price is graft- "
            "versus-host disease, where the graft attacks the patient's "
            "skin, gut, and bile ducts. Autologous transplant (the patient's own "
            "cells, collected before high-dose therapy) rescues the marrow "
            "after dose-intensive treatment of myeloma and lymphoma, with "
            "no graft-versus-host disease but no graft-versus-tumor effect "
            "either. Donors are matched siblings first, then unrelated "
            "registry volunteers, then half-matched (haploidentical) family "
            "with modern protocols. Engraftment - neutrophils returning - "
            "typically arrives 2 to 3 weeks after infusion; the CD34 stem "
            "cell dose target is 2 million or more per kilogram."
        ),
        "how_it_works": (
            "Transplant works as a controlled demolition and rebuild. "
            "Conditioning (busulfan, cyclophosphamide, total body "
            "irradiation in classic regimens) destroys the diseased marrow "
            "and suppresses the immune system so it cannot reject the "
            "graft; infused stem cells, given intravenously like a "
            "transfusion, follow homing signals (SDF-1/CXCR4) back to the "
            "marrow niches, lodge, and begin producing - neutrophils first "
            "around day 14 to 21, then platelets, then full immune "
            "reconstitution over months. In allogeneic transplant the new "
            "immune system may turn on residual leukemia (graft-versus- "
            "leukemia, the cure's engine) or on the patient (graft-versus- "
            "host disease, its tax). The demo checks the cell-dose "
            "arithmetic: a 75-kilogram patient needs at least 150 million "
            "CD34 cells at 2 million per kilogram."
        ),
        "key_points": [
            "Conditioning empties the diseased marrow; infused stem cells home to bone and rebuild it.",
            "Allogeneic (donor) transplant brings graft-versus-leukemia - the cure's engine - and graft-versus-host disease - its tax.",
            "Autologous (own cells) rescues marrow after high-dose therapy for myeloma and lymphoma.",
            "Donor order: matched sibling, unrelated registry, haploidentical family.",
            "Engraftment at 2 to 3 weeks; CD34 dose target 2 million or more per kilogram.",
        ],
        "requirements": [
            "The demolition-and-rebuild sequence: conditioning, infusion, homing, engraftment.",
            "Allogeneic vs autologous: who gets which and why.",
            "Graft-versus-leukemia vs graft-versus-host disease.",
        ],
        "standards": [
            "HLA matching at high resolution for donor selection.",
            "CD34 dose in millions per kilogram of recipient weight.",
            "Infection isolation until neutrophil engraftment.",
        ],
        "citations": [CIT_MAJHAIL, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: transplant is the full shipyard "
            "rebuild - demolish the mutinous yard (conditioning), sail in "
            "a new workforce (the graft), and let it reoccupy the "
            "slipways. The new crew hunts leftover mutineers "
            "(graft-versus-leukemia) but may also riot against the town "
            "(graft-versus-host). Autologous is subtler: evacuate your own "
            "best workers, burn the yard clean, and sail them home."
        ),
    },
    {
        "key": "anticoag",
        "name": "Anticoagulant and Antiplatelet Therapy",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Antithrombotic therapy keeps the welding crews from sealing "
            "the wrong pipes, in two families. Anticoagulants slow the "
            "clotting-factor chain: warfarin (vitamin K antagonist, "
            "monitored by INR with a therapeutic window of 2.0 to 3.0 for "
            "most indications, reversed by vitamin K and prothrombin "
            "complex concentrate), heparins (unfractionated and low "
            "molecular weight, potentiating antithrombin; monitored by "
            "aPTT or anti-Xa; reversible with protamine), and the direct "
            "oral anticoagulants - apixaban, rivaroxaban (anti-Xa) and "
            "dabigatran (anti-IIa) - fixed dose, no routine monitoring, "
            "preferred for most venous thromboembolism and atrial "
            "fibrillation. Antiplatelets disarm the repair crews: aspirin "
            "(irreversible COX blockade, the cornerstone after heart attack "
            "and stent), clopidogrel and ticagrelor (P2Y12 blockers, paired "
            "with aspirin as dual therapy after stents). Every "
            "antithrombotic trades clotting for bleeding - the art is "
            "dosing the protection without buying a hemorrhage, and every "
            "choice names its reversal plan before the first dose."
        ),
        "how_it_works": (
            "Anticoagulants work by starving the cascade at chosen steps. "
            "Warfarin blocks vitamin K recycling, so factors II, VII, IX, "
            "and X emerge without their calcium-binding claws - functional but toothless; the INR measures the "
            "toothlessness, with 2.0 to 3.0 the standard window. Heparin "
            "supercharges antithrombin a thousand-fold, which then "
            "neutralizes thrombin and factor Xa. Direct oral agents bind "
            "their single target - Xa or thrombin - directly and "
            "predictably. Antiplatelets work upstream at the vessel wall: "
            "aspirin permanently disables platelet COX, clopidogrel blocks "
            "the ADP receptor. The demo audits warfarin control: an INR of "
            "1.4 is subtherapeutic (below 2.0), calling for a dose increase, "
            "and 7 of 10 readings in range is 70 percent time in "
            "therapeutic range."
        ),
        "key_points": [
            "Anticoagulants slow the factor chain (warfarin, heparins, direct oral agents); antiplatelets disarm platelets (aspirin, P2Y12 blockers).",
            "Warfarin: INR 2.0 to 3.0 for most indications; reversed by vitamin K and prothrombin complex concentrate.",
            "Direct oral anticoagulants: fixed dose, no monitoring, preferred for most VTE and atrial fibrillation.",
            "Dual antiplatelet therapy (aspirin plus P2Y12 blocker) after coronary stents.",
            "Every antithrombotic names its reversal plan before the first dose; bleeding is the universal price.",
        ],
        "requirements": [
            "The two families and where each one strikes.",
            "Warfarin's mechanism, INR window, and reversal.",
            "The direct oral agents and why they displaced warfarin for most uses.",
        ],
        "standards": [
            "INR 2.0 to 3.0 as the standard warfarin window (higher for mechanical valves).",
            "Renal function checked before direct oral agent dosing.",
            "Perioperative hold times planned for every agent.",
        ],
        "citations": [CIT_CHEST, CIT_WILLIAMS, CIT_HARRISON],
        "sig_lens": (
            "His Signature reading: antithrombotics are the harbor's "
            "traffic control - anticoagulants thin the welding crews' "
            "zeal, antiplatelets stand down the repair tugs. Warfarin is "
            "the old adjustable valve, powerful but twitchy, needing the "
            "INR gauge checked constantly; the direct oral agents are the "
            "set-and-forget modern valves. Every traffic plan is priced in "
            "the same coin - bleeding - and every wise admiral charts the "
            "escape route (reversal) before opening the channel."
        ),
    },
    {
        "key": "aps_hit",
        "name": "Antiphospholipid Syndrome and Heparin-Induced Thrombocytopenia",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Two disorders where the immune system turns clotting against "
            "the patient. Antiphospholipid syndrome (APS) is autoantibodies "
            "(lupus anticoagulant, anticardiolipin, anti-beta2-glycoprotein "
            "I) that paradoxically cause clotting - venous, arterial, and "
            "microvascular - plus recurrent pregnancy loss; the lupus "
            "anticoagulant prolongs the aPTT in the laboratory while the "
            "patient clots in life, the classic paradox. Diagnosis needs a "
            "clinical event plus persistent antibodies 12 weeks apart; "
            "treatment is long-term anticoagulation, usually warfarin, "
            "since direct oral agents have failed in high-risk APS. "
            "Heparin-induced thrombocytopenia (HIT) is antibodies against "
            "the heparin-PF4 complex that activate platelets: the platelet "
            "count falls 5 to 10 days after heparin starts (faster with "
            "prior exposure) and the patient clots - the 4Ts score grades "
            "probability (thrombocytopenia degree, timing, thrombosis, "
            "other causes; 6 to 8 is high). Management: stop all heparin "
            "immediately, start a non-heparin anticoagulant (argatroban, "
            "fondaparinux), and never transfuse platelets for the low "
            "count - it feeds the fire."
        ),
        "how_it_works": (
            "Both work as immune sabotage of the clotting controls. In APS, "
            "antiphospholipid antibodies bind beta2-glycoprotein I on cell "
            "surfaces and activate endothelial cells, platelets, and "
            "complement, tipping the balance toward thrombosis everywhere "
            "while prolonging phospholipid-dependent lab tests - the "
            "laboratory bleeds, the patient clots. In HIT, heparin binds "
            "platelet factor 4, the complex becomes a neoantigen, IgG "
            "antibodies form, and the immune complexes activate platelets "
            "through their Fc receptors - consuming platelets while "
            "generating thrombin, so the count falls as clots form. The "
            "demo scores a HIT case on the 4Ts - platelet fall over 50 "
            "percent with nadir above 20,000 (2), onset day 7 (2), "
            "suspected thrombosis (1), no other cause (2) - totaling 7: "
            "high probability, stop heparin now."
        ),
        "key_points": [
            "APS: antiphospholipid antibodies cause venous, arterial, and microvascular clotting plus pregnancy loss.",
            "The APS paradox: lupus anticoagulant prolongs the aPTT while the patient clots.",
            "APS diagnosis needs a clinical event plus antibodies persistent at 12 weeks; treat with long-term warfarin.",
            "HIT: platelet fall 5 to 10 days after heparin with new clotting; 4Ts score 6 to 8 is high probability.",
            "HIT management: stop all heparin, start a non-heparin anticoagulant, never transfuse platelets for the count.",
        ],
        "requirements": [
            "The two paradoxes: lab bleeding with clinical clotting (APS), falling platelets with new clots (HIT).",
            "The APS antibody trio and the 12-week persistence rule.",
            "The 4Ts score and the stop-heparin imperative.",
        ],
        "standards": [
            "Antibody testing repeated at 12 weeks to confirm persistence.",
            "4Ts scored before ordering HIT immunoassays.",
            "Warfarin, not direct oral agents, for high-risk APS.",
        ],
        "citations": [CIT_CUKER, CIT_WILLIAMS, CIT_HOFFMAN],
        "sig_lens": (
            "His Signature reading: these are the inside jobs - the "
            "harbor's own signal corps forging orders. APS forges the "
            "welders' work orders so they seal healthy channels, and the "
            "laboratory gauge reads the forgery backwards (prolonged "
            "aPTT, clotting patient). HIT turns the standard-issue rope "
            "(heparin) into a tripwire: the crew's own antibodies seize it "
            "and start a riot that sinks platelets and launches clots at "
            "once. The response to a forged order is always the same: "
            "countermand it instantly - stop the heparin."
        ),
    },
    {
        "key": "pediatric",
        "name": "Pediatric Hematology: Blood Disease in Children",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Children's blood is not small adults' blood: hemoglobin "
            "norms shift with age - 14 to 24 g per dL at birth, a "
            "physiologic nadir of 9 to 11 around 2 months as fetal "
            "hemoglobin fades, then 11.5 to 13.5 through childhood - so a "
            "hemoglobin of 9.8 is alarming in a newborn and perfectly "
            "normal at 2 months. The pediatric hematologist meets a "
            "distinct cast: iron deficiency from rapid growth and excess "
            "cow's milk, newborn screening catching sickle cell disease "
            "and thalassemia at birth, immune thrombocytopenia that "
            "usually resolves on its own, hemophilia presenting when a "
            "toddler starts to walk and bruise, and acute lymphoblastic "
            "leukemia - the most common childhood cancer and the great "
            "success story, over 85 percent cured. Dosing, transfusion "
            "thresholds, and chemotherapy are all weight- and age-based, "
            "and every plan weighs growth, development, and decades of "
            "life ahead: iron chelation must spare growing bones, "
            "transfusions must consider alloimmunization over a lifetime, "
            "and survivorship starts at diagnosis."
        ),
        "how_it_works": (
            "Pediatric hematology works as age-calibrated hematology. Every "
            "reference range is a curve, not a number: hemoglobin, white "
            "count, and platelet norms all slide with age, and the "
            "interpreter's first job is placing the child on the right "
            "curve before calling anything abnormal. Disease behavior is "
            "age-specific too: the 2-month nadir is physiology, not "
            "disease; ITP in childhood is usually post-viral and self- "
            "limited while adult ITP is chronic; ALL in children is "
            "highly curable while adult ALL is stubborn. Treatment scales "
            "by weight and body surface area, and late effects - growth, "
            "fertility, second cancers - are designed against from day "
            "one. The demo checks the age curve: hemoglobin 9.8 at 2 "
            "months lands inside the 9 to 11 nadir - physiologic, no "
            "workup."
        ),
        "key_points": [
            "Hemoglobin norms are age curves: 14 to 24 at birth, nadir 9 to 11 at 2 months, 11.5 to 13.5 in childhood.",
            "Newborn screening catches sickle cell disease and thalassemia at birth.",
            "Childhood ITP usually resolves spontaneously; adult ITP is usually chronic.",
            "ALL is the most common childhood cancer and over 85 percent curable; hemophilia declares itself when toddlers walk.",
            "Every plan weighs decades ahead: growth, fertility, alloimmunization, survivorship from day one.",
        ],
        "requirements": [
            "The age curves for hemoglobin and why the 2-month nadir is normal.",
            "The pediatric cast: growth-related iron deficiency, newborn-screened hemoglobinopathies, childhood ITP, ALL.",
            "The long-horizon principle: late effects designed against from diagnosis.",
        ],
        "standards": [
            "Age-specific reference ranges used for every interpretation.",
            "Weight-based dosing for all pediatric hematology drugs.",
            "Survivorship planning begins at diagnosis.",
        ],
        "citations": [CIT_HOFFBRAND, CIT_WILLIAMS, CIT_PIEL],
        "sig_lens": (
            "His Signature reading: pediatric hematology is the new-fleet "
            "commissioning office - every gauge reads on a different scale "
            "while the ships are still being fitted out, and the admiral "
            "must know the commissioning curves by heart or he will condemn "
            "a healthy vessel. The childhood diseases are their own "
            "squadron with their own rules of engagement - and every "
            "battle plan is drawn with seventy years of sailing left on "
            "the hull."
        ),
    },
    {
        "key": "pregnancy",
        "name": "Pregnancy and Blood: Hematologic Change and Disease",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pregnancy rewrites the blood: plasma volume expands 40 to 50 "
            "percent while red cell mass grows only 20 to 30 percent, so "
            "hemoglobin dilutes - the physiologic anemia of pregnancy, "
            "with thresholds of 11 g per dL in the first trimester and "
            "10.5 in the second and third. Clotting factors rise and "
            "natural anticoagulants fall, making pregnancy a hypercoagulable "
            "state - protection against childbirth bleeding that raises "
            "venous thromboembolism risk five-fold. Platelets drift down "
            "(gestational thrombocytopenia, usually mild and harmless), "
            "while HELLP syndrome - hemolysis, elevated enzymes, low "
            "platelets - and preeclampsia threaten both lives and end with "
            "birth. Iron demand soars: the fetus, the placenta, and the "
            "expanded red cell mass need about a gram of iron, so "
            "supplementation is routine and deficiency is the commonest "
            "true anemia of pregnancy. Sickle cell disease and "
            "thrombophilias need specialist co-management; warfarin is "
            "teratogenic and heparins, which do not cross the placenta, "
            "carry the anticoagulation load."
        ),
        "how_it_works": (
            "Pregnancy hematology works as a planned flood. The plasma "
            "expansion outruns red cell production by design - lower "
            "viscosity improves placental flow - so hemoglobin falls even "
            "as total red cell mass rises; the trimester thresholds (11, "
            "then 10.5) separate this dilution from true anemia. The "
            "hypercoagulable shift is equally deliberate: factors VII, "
            "VIII, X, and fibrinogen climb while protein S falls, arming "
            "the uterus against hemorrhage at the cost of clot risk. Iron "
            "accounting runs a deficit of about a gram across the "
            "pregnancy, repaid by supplementation. The demo applies the "
            "third-trimester threshold: hemoglobin 10.8 at 30 weeks clears "
            "the 10.5 line - physiologic dilution, not anemia."
        ),
        "key_points": [
            "Plasma expands 40 to 50 percent vs red cell mass 20 to 30 percent: physiologic anemia of pregnancy.",
            "Anemia thresholds: 11 g per dL first trimester, 10.5 second and third.",
            "Pregnancy is hypercoagulable by design: VTE risk rises five-fold.",
            "HELLP and preeclampsia end with birth; gestational thrombocytopenia is usually mild and harmless.",
            "Iron demand is about a gram: supplement routinely; heparins (not warfarin) anticoagulate in pregnancy.",
        ],
        "requirements": [
            "The dilution arithmetic and the trimester thresholds.",
            "The hypercoagulable shift and its evolutionary logic.",
            "HELLP vs gestational thrombocytopenia: danger vs benign.",
        ],
        "standards": [
            "Trimester-specific hemoglobin thresholds applied, not the nonpregnant range.",
            "Warfarin avoided; heparins used for anticoagulation.",
            "HELLP managed as an obstetric emergency ending in birth.",
        ],
        "citations": [CIT_WILLIAMS, CIT_HARRISON, CIT_CHEST],
        "sig_lens": (
            "His Signature reading: pregnancy is the fleet's planned "
            "flood - the harbor deliberately deepened (plasma up) faster "
            "than the fleet grows, thinning every gauge by design to feed "
            "the new construction in the drydock (the placenta). The "
            "welding crews are doubled against the great hemorrhage to "
            "come, at the price of silted channels. HELLP is the flood "
            "turning mutinous - and the admiral's answer is the oldest in "
            "the book: bring the ship safely to harbor and save the crew."
        ),
    },
    {
        "key": "future",
        "name": "The Future of Hematology: Gene Therapy and CAR-T Cells",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hematology is becoming the first curative specialty of the "
            "genetic age, because blood is the accessible tissue: draw it, "
            "engineer it, return it. Gene therapy for sickle cell disease "
            "and beta thalassemia edits the patient's own stem cells - "
            "reactivating fetal hemoglobin (exagamglogene autotemcel) or "
            "adding a corrected beta-globin gene (lovotibeglogene "
            "autotemcel) - and early trials show the large majority of "
            "treated patients freed from transfusions and crises. "
            "Hemophilia gene therapy introduces a functional factor VIII or "
            "IX gene via viral vector, converting severe "
            "disease toward mild with a single infusion. CAR-T cells - the "
            "patient's T cells engineered with a chimeric antigen receptor "
            "against CD19 or BCMA - produce remissions around 80 percent "
            "in relapsed childhood ALL and have transformed relapsed "
            "myeloma and lymphoma care; bispecific antibodies (blinatumomab, "
            "teclistamab) bring similar targeting without the cell "
            "manufacturing. The frontiers now are access and durability: "
            "million-dollar prices, conditioning toxicity, and making the "
            "cures last decades, not years."
        ),
        "how_it_works": (
            "The future works as precision reprogramming of the fleet. "
            "Gene therapy harvests the patient's stem cells, edits them "
            "outside the body (CRISPR cutting the BCL11A switch that "
            "silences fetal hemoglobin, or lentivirus inserting a working "
            "globin gene), wipes the marrow with conditioning, and returns "
            "the corrected crew - which then manufactures healthy red "
            "cells for life. CAR-T therapy engineers T cells with a "
            "synthetic receptor: an antibody fragment that grabs CD19 on "
            "leukemia cells fused to T-cell activation machinery, turning "
            "each engineered cell into a guided hunter that multiplies on "
            "contact. The demo works the landmark numbers: an 81 percent "
            "remission rate means about 81 of 100 relapsed ALL children "
            "respond, and 32 of 35 gene-therapy patients transfusion-free "
            "is 91.4 percent."
        ),
        "key_points": [
            "Blood is the accessible tissue: draw, engineer, return - making hematology the first curative genetic specialty.",
            "Sickle cell and thalassemia gene therapy: reactivate fetal hemoglobin or add a corrected globin gene.",
            "Hemophilia gene therapy: one vector infusion converting severe toward mild disease.",
            "CAR-T (CD19, BCMA): around 80 percent remissions in relapsed ALL; transformed relapsed myeloma and lymphoma.",
            "Frontiers: price, conditioning toxicity, and decades-long durability.",
        ],
        "requirements": [
            "The ex vivo edit-and-return sequence for gene therapy.",
            "The CAR-T construct: antibody fragment fused to T-cell machinery.",
            "The access and durability frontiers.",
        ],
        "standards": [
            "Trial results reported as intention-to-treat remission rates.",
            "Long-term follow-up mandated for gene and cell therapies.",
            "Cures measured in decades, claimed only with the follow-up to prove it.",
        ],
        "citations": [CIT_MAUDE, CIT_PIEL, CIT_WILLIAMS],
        "sig_lens": (
            "His Signature reading: the future is the shipyard learning "
            "to rewrite its own blueprints - CRISPR as the master "
            "shipwright's eraser, switching the old reliable hull design "
            "(fetal hemoglobin) back on; CAR-T as the press-ganged hunter "
            "fleet, each T cell fitted with a custom targeting scope and "
            "turned loose on the mutineers. Hematology got here first "
            "because its fleet sails in open water - drawable, "
            "engineerable, returnable. The last battles are not science "
            "but logistics: price, toxicity, and time."
        ),
    },
]
