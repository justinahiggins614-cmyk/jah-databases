#!/usr/bin/env python3
"""Entries for The Holistic OTC and Natural Cures Database (public + Signature).

68 ladder-ordered records covering holistic over-the-counter and natural
approaches for sickness and injuries, plus wellness practices.

PUBLIC HALF (src public-harvest): real documented remedies - established OTC
products and their documented uses, and traditionally-documented natural
remedies (honey, ginger, chamomile, aloe, saline, and others), each with
HONEST evidence framing: what is documented by research, what is traditional
or anecdotal, and what is not established. Nothing is presented as proven
that is not. No record claims a cure for any serious disease; records for
serious conditions are limited to general wellness and support information
with direction to professional care. No dosage instructions appear anywhere.

SIGNATURE HALF (src signature): his original Signature holistic regimen
frameworks and wellness-completion content - original Signature-made
frameworks, clearly labeled Signature-made, never presented as authentic
public record.

UNIVERSAL SAFETY FRAMING (every record): educational information only, not
medical advice; consult a healthcare professional for personal guidance; do
not delay professional care; red-flag symptoms get professional-care
direction. Content screened per standing rules: no hate-adjacent, profane,
inappropriate, or religious content.
"""

SAFETY_STD = ("Educational information only - not medical advice. Consult a "
              "healthcare professional for personal medical guidance; do not "
              "delay professional care.")

SIG_TAIL = ("Signature-made content: his original holistic wellness "
            "framework, clearly labeled Signature-made, never presented as "
            "authentic public record. Educational information only - not "
            "medical advice; consult a healthcare professional.")

ENTRIES = [
{
 "key": "honey-cough-soother",
 "name": "Honey as a traditional cough soother",
 "group": "minor-ailments",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("Honey has been used for generations as a soothing agent for "
  "coughs and throat irritation, and modern research gives it documented "
  "support in a narrow, honest scope: a randomized trial (Paul et al., 2007) "
  "found that a small evening serving of buckwheat honey reduced nighttime "
  "cough and improved sleep in children older than one year better than no "
  "treatment, performing comparably to a common OTC cough medicine in that "
  "study. Evidence status: documented for soothing cough symptoms, NOT a cure "
  "for the cold or flu causing the cough. Critical safety boundary: never "
  "give honey to infants under 12 months because of the risk of infant "
  "botulism. People with pollen or bee-product allergies should avoid it, "
  "and anyone with diabetes should factor in the sugar content."),
 "how_it_works": ("Honey coats the throat with a thick, soothing layer that "
  "can calm the tickle triggering a cough, and its sweetness may stimulate "
  "saliva and mucus secretions that ease throat dryness. Researchers also "
  "note mild antioxidant content. The practical framework in this record is "
  "a decision tree, not a prescription: confirm the person is over 12 "
  "months old, confirm no bee-product allergy, use honey only as a comfort "
  "measure for a mild cough, and seek professional care for coughs with "
  "wheezing, difficulty breathing, chest pain, coughing blood, or fever that "
  "does not resolve. The included demo runs an age-and-allergy safety gate "
  "that classifies scenarios as safe to consider or not safe."),
 "key_points": [
  "Documented: honey soothed nighttime cough in children over one year in a randomized trial (Paul et al., 2007).",
  "Never give honey to infants under 12 months - infant botulism risk is the hard boundary.",
  "Honey soothes the symptom (the cough); it does not cure the cold or flu behind it.",
  "Avoid with bee-product or pollen allergies; people managing blood sugar should count the sugar.",
  "Escalate to professional care for wheezing, breathing difficulty, chest pain, or persistent fever.",
 ],
 "requirements": [
  "Reader must confirm the 12-month age boundary before considering honey.",
  "Reader must check for bee-product allergy and blood-sugar considerations.",
  "Reader must know the red-flag cough symptoms that require professional care.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented (trial support) vs traditional vs not established.",
  SAFETY_STD,
 ],
 "citations": [
  "Paul IM et al. Effect of honey, dextromethorphan, and no treatment on nocturnal cough and sleep quality for coughing children and their parents. Archives of Pediatrics and Adolescent Medicine; 2007.",
  "National Center for Complementary and Integrative Health. Honey and cough in children over one year; infant botulism warning for under 12 months.",
 ],
},
{
 "key": "warm-salt-gargle",
 "name": "Warm salt-water gargle for sore-throat comfort",
 "group": "minor-ailments",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Gargling with warm salt water is one of the oldest "
  "documented home comfort measures for a sore throat. Evidence status: "
  "traditional with plausible mechanism and low risk - clinical guidance "
  "(including Mayo Clinic self-care guidance for sore throat) lists it as a "
  "reasonable comfort measure, though high-quality trials are limited. The "
  "warmth increases local blood flow and the salt creates a mildly "
  "hypertonic environment that may draw fluid from swollen tissues, easing "
  "the raw feeling. It does not treat strep throat, which requires "
  "professional diagnosis and antibiotics, and it does not cure the viral "
  "infection behind most sore throats. Anyone with high blood pressure "
  "concerns should spit the solution out fully rather than swallowing it."),
 "how_it_works": ("The record teaches a comfort ritual in four parts. "
  "First, the preparation principle: comfortably warm (not hot) water with a "
  "small amount of dissolved table salt, mixed until clear. Second, the "
  "technique: tilt the head back, gargle for about half a minute, spit, and "
  "repeat a few times. Third, the boundary: this is for mild sore-throat "
  "comfort alongside rest and fluids - it is not a treatment for bacterial "
  "throat infection. Fourth, the escalation ladder: severe throat pain, "
  "trouble swallowing or breathing, drooling, rash, joint pain, or symptoms "
  "lasting beyond a few days all point to professional evaluation. The demo "
  "verifies the correct step order of the ritual and flags unsafe variants."),
 "key_points": [
  "Traditional comfort measure with plausible mechanism; listed in mainstream sore-throat self-care guidance.",
  "Warmth plus mild saltiness eases the raw feeling; it does not cure the underlying infection.",
  "Strep throat needs professional diagnosis and antibiotics - gargling is not a substitute.",
  "Use comfortably warm water, never hot; spit the solution out fully.",
  "Seek care for severe pain, swallowing or breathing trouble, rash, or symptoms lasting days.",
 ],
 "requirements": [
  "Reader must distinguish comfort measure from treatment of bacterial infection.",
  "Reader must use warm-not-hot water and spit the solution out.",
  "Reader must know the escalation symptoms that require professional care.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional with plausible mechanism, limited trial data.",
  SAFETY_STD,
 ],
 "citations": [
  "Mayo Clinic. Sore throat self-care guidance: warm salt-water gargle as a comfort measure.",
  "Traditional practice documented across cultures; mechanism consistent with basic physiology of hypertonic solutions.",
 ],
},
{
 "key": "ginger-nausea-ease",
 "name": "Ginger for nausea and motion unease",
 "group": "minor-ailments",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Ginger root has centuries of traditional use for settling "
  "the stomach, and modern evidence gives it honest, moderate support: "
  "reviews of clinical trials find ginger reduces nausea in specific "
  "contexts such as motion sickness and pregnancy-related nausea better than "
  "placebo in several studies, though results are mixed and effect sizes "
  "modest. Evidence status: documented with moderate, context-specific "
  "support - NOT a cure for vomiting illnesses and not a substitute for "
  "rehydration when fluids are being lost. People taking blood-thinning "
  "medication, those with gallbladder disease, and anyone facing surgery "
  "should consult a professional before using ginger in medicinal amounts, "
  "since ginger can affect clotting. Culinary amounts in food are generally "
  "regarded as safe for most people."),
 "how_it_works": ("The record frames ginger as a traditional stomach-settling "
  "agent with a plausible mechanism: gingerols and shogaols in the root "
  "appear to interact with serotonin receptors in the gut involved in the "
  "nausea signal, and ginger may speed gastric emptying. The practical "
  "framework covers the common traditional forms - fresh ginger tea, small "
  "pieces of candied or fresh ginger, and ginger in food - as comfort "
  "measures for mild nausea, alongside the honest boundary: for vomiting "
  "with dehydration signs, fever, severe abdominal pain, blood, or head "
  "injury, professional care comes first. The demo computes an "
  "evidence-strength score from a small study table and labels the result "
  "as moderate and context-specific."),
 "key_points": [
  "Documented moderate support for nausea in specific contexts (motion sickness, pregnancy-related nausea); results mixed.",
  "Traditional forms: ginger tea, fresh ginger, ginger in food - used as comfort measures, not cures.",
  "Consult a professional first with blood-thinning medication, gallbladder disease, or before surgery.",
  "Does not replace rehydration when vomiting or diarrhea cause fluid loss.",
  "Seek care for dehydration signs, severe pain, blood, fever, or head injury with nausea.",
 ],
 "requirements": [
  "Reader must state the medication-interaction cautions before considering ginger.",
  "Reader must distinguish mild nausea comfort from vomiting illness needing care.",
  "Reader must describe the evidence as moderate and context-specific, never absolute.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented with moderate, context-specific trial support.",
  SAFETY_STD,
 ],
 "citations": [
  "Ernst E, Pittler MH. Efficacy of ginger for nausea and vomiting: a systematic review of randomized clinical trials. British Journal of Anaesthesia; 2000.",
  "National Center for Complementary and Integrative Health. Ginger: what the science says about nausea relief.",
 ],
},
{
 "key": "chamomile-evening-cup",
 "name": "Chamomile tea as an evening calming ritual",
 "group": "minor-ailments",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Chamomile tea is one of the most widely used herbal evening "
  "drinks in the world, traditionally taken to unwind before sleep and to "
  "settle mild digestive unease. Evidence status: traditional with modest "
  "emerging support - a randomized trial (Zick et al., 2011) found modest "
  "benefit for generalized anxiety symptoms, and small studies suggest "
  "possible sleep-quality support, but the evidence base is limited and "
  "chamomile is not an insomnia treatment. It is caffeine-free, which is the "
  "most defensible part of the ritual: replacing an evening caffeinated "
  "drink with chamomile removes a known sleep disruptor. People allergic to "
  "ragweed or related plants should avoid it, and anyone on blood-thinning "
  "or sedative medication should consult a professional first."),
 "how_it_works": ("The record presents chamomile as a ritual-first remedy: "
  "the calming effect comes substantially from the ritual itself - a warm, "
  "caffeine-free drink, dimmed lights, and a wind-down routine signal the "
  "body that sleep is coming. The plant contributes apigenin, a flavonoid "
  "that binds weakly to brain receptors involved in calm, though human "
  "evidence for strong effects is limited. The framework teaches the honest "
  "version: build the evening ritual, keep expectations modest, watch for "
  "ragweed-family allergy, and treat persistent insomnia or anxiety as "
  "reasons to consult a professional rather than doubling down on tea. The "
  "demo scores an evening routine checklist and reports which sleep-hygiene "
  "elements are present."),
 "key_points": [
  "Traditional evening calming ritual; modest trial support for anxiety symptoms, limited sleep evidence.",
  "Caffeine-free by nature - the ritual of replacing evening caffeine is itself the strongest mechanism.",
  "Not an insomnia or anxiety-disorder treatment; persistent problems need professional care.",
  "Avoid with ragweed-family allergies; check with a professional on blood-thinning or sedative medication.",
  "Expectations stay modest and honest: a gentle ritual, not a remedy with proven power.",
 ],
 "requirements": [
  "Reader must describe the evidence as modest and limited, never proven.",
  "Reader must name the ragweed-allergy and medication cautions.",
  "Reader must treat persistent insomnia or anxiety as a prompt for professional care.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional with modest emerging trial support.",
  SAFETY_STD,
 ],
 "citations": [
  "Zick SM et al. Preliminary examination of the efficacy and safety of a standardized chamomile extract for chronic generalized anxiety disorder. BMC Complementary and Alternative Medicine; 2011.",
  "National Center for Complementary and Integrative Health. Chamomile: what the science says.",
 ],
},
{
 "key": "fluids-rest-cold",
 "name": "Fluids and rest: supporting the body through a common cold",
 "group": "minor-ailments",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("The common cold has no cure - no OTC product, herb, or "
  "supplement shortens it in any established way - and this record is "
  "honest about that from the first line. What mainstream guidance "
  "(including CDC and Mayo Clinic cold self-care guidance) does document is "
  "supportive care: staying hydrated, resting, and using comfort measures "
  "while the immune system does the real work over 7 to 10 days. Evidence "
  "status: documented for supportive care; the no-cure statement is itself "
  "the documented fact. Dehydration makes every cold symptom feel worse, and "
  "rest conserves the energy the immune response needs. Antibiotics do not "
  "help colds (colds are viral), and requesting them contributes to "
  "antibiotic resistance - a documented public-health fact this record "
  "states plainly."),
 "how_it_works": ("The record teaches the cold as a managed week, not a "
  "battle to win: days 1-3 (sore throat, congestion onset) call for fluids, "
  "rest, and comfort measures; days 4-7 (peak congestion) call for patience "
  "and continued hydration; days 8-10 (resolution) call for gradual return "
  "to activity. Hydration keeps mucus thinner and easier to clear; rest "
  "reduces the energy deficit. The escalation ladder is explicit: difficulty "
  "breathing, chest pain, dehydration, fever above the normal range that "
  "persists, symptoms worsening after 10 days, or illness in infants, older "
  "adults, or immunocompromised people all warrant professional care. The "
  "demo walks a day-by-day timeline and classifies each day into the right "
  "care phase."),
 "key_points": [
  "Documented fact: no cure exists for the common cold; supportive care is the established approach.",
  "Hydration and rest are the documented core - they support the immune system doing its work.",
  "Antibiotics do not help viral colds; unnecessary use drives antibiotic resistance.",
  "Comfort measures (this database records many) ease symptoms; none shortens the illness in established evidence.",
  "Escalate for breathing difficulty, chest pain, dehydration, persistent fever, or worsening after 10 days.",
 ],
 "requirements": [
  "Reader must state plainly that no cure exists for the common cold.",
  "Reader must explain why antibiotics are not appropriate for colds.",
  "Reader must know the escalation symptoms and vulnerable groups needing earlier care.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented supportive care; no-cure statement is the documented fact.",
  SAFETY_STD,
 ],
 "citations": [
  "Centers for Disease Control and Prevention. Common cold: self-care and when antibiotics are not needed.",
  "Mayo Clinic. Common cold self-care: fluids, rest, and comfort measures while the illness runs its course.",
 ],
},
{
 "key": "cold-compress-bumps",
 "name": "Cold compress for minor bumps and bruises",
 "group": "minor-ailments",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "description": ("A cold compress on a fresh minor bump is standard first-aid "
  "practice worldwide. Evidence status: documented as first aid - cold "
  "constricts local blood vessels, which limits swelling and numbs the area "
  "enough to ease pain. It does not heal tissue faster in any established "
  "sense; it manages the acute response. The safety rules are part of the "
  "record, not an afterthought: wrap ice or a cold pack in a cloth, never "
  "apply ice directly to skin, limit sessions to about 15 minutes with "
  "breaks between, and never use cold on areas with poor circulation or on "
  "open wounds. Bumps involving head injury with confusion, vomiting, "
  "unequal pupils, or loss of consciousness need emergency care, not a "
  "compress."),
 "how_it_works": ("The record teaches the compress as a timed cycle: cold "
  "on (wrapped, about 15 minutes), cold off (at least as long), repeat as "
  "needed through the first day while monitoring the skin for excessive "
  "paleness or numbness. Elevation of the bumped area alongside the compress "
  "further limits swelling. The demo computes duty-cycle math for on/off "
  "intervals across a session plan and verifies that no interval exceeds the "
  "safe single-session length, then checks a head-injury red-flag list that "
  "routes to emergency care instead of home care."),
 "key_points": [
  "Documented first aid: cold limits swelling and eases pain by constricting vessels and numbing.",
  "Always wrap the cold source in cloth; never apply ice directly to skin.",
  "About 15 minutes on with breaks; watch for excessive paleness or numbness.",
  "Not for open wounds or areas with poor circulation.",
  "Head injury with confusion, vomiting, unequal pupils, or lost consciousness needs emergency care.",
 ],
 "requirements": [
  "Reader must state the wrap-in-cloth rule and the session-length limit.",
  "Reader must list the head-injury red flags that override home care.",
  "Reader must describe cold as symptom management, not accelerated healing.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented standard first aid.",
  SAFETY_STD,
 ],
 "citations": [
  "American Red Cross. First aid guidance: cold application for minor bumps, bruises, and sprains.",
  "Standard sports-medicine first-aid references on cryotherapy timing and skin protection.",
 ],
},
{
 "key": "acetaminophen-guide",
 "name": "Acetaminophen: the documented pain and fever reliever",
 "group": "minor-ailments",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "description": ("Acetaminophen (known as paracetamol outside the United "
  "States) is one of the most studied OTC medicines in the world, with "
  "documented effectiveness for mild-to-moderate pain and fever reduction. "
  "Evidence status: documented - it is a first-line option in mainstream "
  "guidance for many everyday pains and for fever. This record gives NO "
  "dosage instructions; dosing belongs on the product label and with a "
  "pharmacist or clinician. The honest safety core: the liver processes "
  "acetaminophen, and exceeding the labeled amount - easy to do because the "
  "drug hides in many combination cold, flu, and sleep products - can cause "
  "severe liver injury. People with liver disease, regular alcohol use, or "
  "who take multiple medicines must consult a professional first. It does "
  "not reduce inflammation the way NSAIDs do."),
 "how_it_works": ("The record teaches label literacy, not dosing: how to "
  "find acetaminophen (or paracetamol, or APAP) on ingredient lists, why "
  "combination products are the main overdose trap, and why the daily "
  "maximum on the label is a hard ceiling rather than a suggestion. It "
  "covers the documented uses (headache, muscle aches, minor arthritis pain, "
  "fever, cold and flu symptom formulas) and the documented limits (not "
  "anti-inflammatory, liver risk in excess, many drug interactions possible). "
  "The escalation rule: pain or fever that is severe, persistent, or "
  "unexplained needs professional diagnosis rather than repeated self-"
  "medication. The demo runs a label-literacy quiz that flags hidden "
  "acetaminophen in combination-product ingredient lists."),
 "key_points": [
  "Documented effectiveness for mild-to-moderate pain and fever; a first-line OTC option in mainstream guidance.",
  "No dosage instructions in this record - dosing lives on the product label and with professionals.",
  "Liver injury is the documented risk of exceeding labeled amounts; combination products are the main trap.",
  "Check every label for acetaminophen, paracetamol, or APAP before combining products.",
  "Liver disease, regular alcohol use, or multiple medicines: consult a professional first.",
 ],
 "requirements": [
  "Reader must identify acetaminophen under its alternate names on labels.",
  "Reader must explain the combination-product overdose trap.",
  "Reader must state that persistent or severe pain or fever needs professional diagnosis.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented OTC medicine; no dosing given, label and professional directed.",
  SAFETY_STD,
 ],
 "citations": [
  "U.S. Food and Drug Administration. Acetaminophen OTC labeling and liver-injury warnings.",
  "MedlinePlus (U.S. National Library of Medicine). Acetaminophen: uses, warnings, and drug interactions.",
 ],
},
{
 "key": "ibuprofen-guide",
 "name": "Ibuprofen and NSAIDs: documented pain and inflammation relief",
 "group": "minor-ailments",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "description": ("Ibuprofen is a non-steroidal anti-inflammatory drug (NSAID) "
  "with documented effectiveness for pain, fever, and inflammation - the "
  "anti-inflammatory action is what distinguishes it from acetaminophen. "
  "Evidence status: documented - a mainstay of mainstream guidance for "
  "muscle aches, minor arthritis pain, menstrual cramps, dental pain, and "
  "fever. This record gives NO dosage instructions; dosing belongs on the "
  "product label and with a pharmacist or clinician. The honest safety "
  "core: NSAIDs can irritate the stomach lining and, with regular use, raise "
  "the risk of stomach bleeding, kidney effects, and cardiovascular events - "
  "documented in FDA labeling. People with ulcer history, kidney disease, "
  "heart disease, asthma sensitive to NSAIDs, or on blood thinners must "
  "consult a professional first."),
 "how_it_works": ("The record teaches NSAID literacy: how ibuprofen reduces "
  "the prostaglandins that drive pain, fever, and inflammation; the "
  "documented uses where the anti-inflammatory action matters (sprains, "
  "dental pain, menstrual cramps); and the documented risk profile that "
  "makes it a poor choice for some people. It covers the food-with-medicine "
  "convention for stomach comfort, the interaction with alcohol, and why "
  "stacking multiple NSAIDs (ibuprofen plus naproxen, for example) is a "
  "documented hazard. The escalation rule mirrors the acetaminophen record: "
  "severe, persistent, or unexplained pain needs diagnosis, not repeated "
  "self-medication. The demo scores an NSAID caution checklist against "
  "reader-selected risk factors."),
 "key_points": [
  "Documented for pain, fever, and inflammation; the anti-inflammatory action distinguishes it from acetaminophen.",
  "No dosage instructions in this record - dosing lives on the product label and with professionals.",
  "Documented risks: stomach irritation and bleeding, kidney effects, cardiovascular risk with regular use.",
  "Never stack multiple NSAIDs; check labels before combining pain products.",
  "Ulcer history, kidney or heart disease, NSAID-sensitive asthma, or blood thinners: consult a professional first.",
 ],
 "requirements": [
  "Reader must explain the difference between ibuprofen and acetaminophen.",
  "Reader must name the documented NSAID risk profile.",
  "Reader must state that severe or persistent pain needs professional diagnosis.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented OTC medicine; no dosing given, label and professional directed.",
  SAFETY_STD,
 ],
 "citations": [
  "U.S. Food and Drug Administration. NSAID labeling: stomach, kidney, and cardiovascular risk information.",
  "MedlinePlus (U.S. National Library of Medicine). Ibuprofen: uses, warnings, and drug interactions.",
 ],
},
{
 "key": "antihistamine-guide",
 "name": "Antihistamines for seasonal allergy symptoms",
 "group": "minor-ailments",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "description": ("Antihistamines such as loratadine, cetirizine, and "
  "fexofenadine are documented OTC medicines for allergy symptoms - sneezing, "
  "itchy and watery eyes, and runny nose driven by histamine release. "
  "Evidence status: documented - second-generation antihistamines are "
  "first-line in mainstream allergy guidance, with less drowsiness than "
  "older formulas. This record gives NO dosage instructions; dosing belongs "
  "on the product label and with a pharmacist or clinician. The honest "
  "framing: antihistamines manage allergy symptoms; they do not cure "
  "allergies and they do not help the common cold much, since colds are not "
  "histamine-driven. Older formulas cause drowsiness that impairs driving. "
  "Anyone with glaucoma, urinary difficulty, or on sedating medicines "
  "should consult a professional first."),
 "how_it_works": ("The record teaches allergy literacy in three parts. "
  "First, the mechanism: blocking histamine receptors calms the sneeze-itch-"
  "watery-eye cascade. Second, the generations: older antihistamines cross "
  "into the brain and sedate; newer ones mostly do not, which is why "
  "guidance prefers them for daytime use. Third, the differential: allergy "
  "symptoms (itchy eyes and nose, clear runny nose, seasonal pattern, no "
  "fever) versus cold symptoms (sore throat first, body aches, possible "
  "fever) - because the right remedy depends on the right identification. "
  "Severe allergic reactions with breathing difficulty or swelling need "
  "emergency care, not an OTC tablet. The demo classifies symptom sets as "
  "allergy-like, cold-like, or emergency."),
 "key_points": [
  "Documented for allergy symptoms: sneezing, itchy watery eyes, histamine-driven runny nose.",
  "Newer formulas cause less drowsiness; older ones impair driving and alertness.",
  "They manage symptoms; they do not cure allergies and help colds little.",
  "Allergy vs cold identification matters - itchy eyes and seasonal pattern point to allergy.",
  "Breathing difficulty or swelling with an allergic reaction needs emergency care.",
 ],
 "requirements": [
  "Reader must distinguish allergy symptoms from cold symptoms.",
  "Reader must explain the drowsiness difference between antihistamine generations.",
  "Reader must know the emergency signs of severe allergic reaction.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented OTC medicine; no dosing given, label and professional directed.",
  SAFETY_STD,
 ],
 "citations": [
  "U.S. Food and Drug Administration. OTC antihistamine labeling and drowsiness warnings.",
  "MedlinePlus (U.S. National Library of Medicine). Loratadine, cetirizine, fexofenadine: uses and warnings.",
 ],
},
{
 "key": "saline-nasal-care",
 "name": "Saline nasal rinse and spray for congestion",
 "group": "minor-ailments",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "description": ("Saline nasal irrigation - rinsing the nasal passages with "
  "salt water - has documented support: a Cochrane review (King et al., "
  "2015) found saline irrigation likely improves symptoms of chronic "
  "rhinosinusitis, and mainstream guidance lists saline spray or rinse as a "
  "reasonable comfort measure for colds and allergies. Evidence status: "
  "documented with moderate support for symptom relief; NOT a cure for "
  "infection. The mechanism is straightforward: the rinse thins mucus and "
  "washes out irritants and allergens. The critical safety rule is water "
  "source: use distilled, sterile, or previously boiled-then-cooled water, "
  "never untreated tap water, because of the rare but severe risk of "
  "waterborne infection. Devices must be cleaned and dried between uses."),
 "how_it_works": ("The record teaches the rinse as a hygiene ritual with "
  "three non-negotiable safety parts. First, water: distilled, sterile, or "
  "boiled-then-cooled only. Second, solution: a mild salt concentration "
  "mixed until fully dissolved, comfortably lukewarm. Third, device care: "
  "rinse and air-dry the device after every use. The technique - leaning "
  "over a sink, breathing through the mouth, letting the solution flow in "
  "one nostril and out the other - is described as a learned skill that "
  "feels strange before it feels routine. Congestion with high fever, facial "
  "pain and swelling, or symptoms beyond ten days warrants professional "
  "evaluation. The demo runs a water-source and device-hygiene safety audit "
  "over sample routines."),
 "key_points": [
  "Documented moderate support (Cochrane review) for symptom relief in congestion and sinus symptoms.",
  "Thins mucus and washes out irritants; a comfort measure, not a cure for infection.",
  "Water rule is absolute: distilled, sterile, or boiled-then-cooled only - never untreated tap water.",
  "Clean and fully dry the device between uses.",
  "Seek care for high fever, facial pain with swelling, or congestion beyond ten days.",
 ],
 "requirements": [
  "Reader must state the safe-water rule and the reason behind it.",
  "Reader must describe device cleaning between uses.",
  "Reader must describe saline as symptom relief, never a cure.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented moderate support; water-safety rule is the documented hazard control.",
  SAFETY_STD,
 ],
 "citations": [
  "King D et al. Saline nasal irrigation for acute upper respiratory tract infections. Cochrane Database of Systematic Reviews; 2015.",
  "U.S. Food and Drug Administration. Guidance on safe water for nasal rinsing devices.",
 ],
},
{
 "key": "aloe-minor-sunburn",
 "name": "Aloe vera for minor sunburn comfort",
 "group": "minor-ailments",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "description": ("Aloe vera gel has long traditional use on minor burns and "
  "sunburn, and the evidence gives it modest, specific support: a systematic "
  "review (Maenthaisong et al., 2007) found aloe may shorten healing time "
  "for first- and second-degree burns compared with conventional care in "
  "the included trials, though the evidence quality was limited. Evidence "
  "status: traditional with modest trial support for minor burns; NOT a "
  "treatment for serious burns. For sunburn specifically, aloe is a cooling "
  "comfort measure alongside cool water, fluids, and staying out of the sun "
  "while skin recovers. Severe sunburn - blistering over large areas, fever, "
  "chills, or signs of heat illness - needs professional care. This record "
  "covers gel from the plant or commercial pure gel, not homemade mixtures "
  "with unlisted ingredients."),
 "how_it_works": ("The record frames aloe as cooling comfort plus a "
  "possible mild healing assist: the gel is mostly water, which cools "
  "through evaporation, and contains compounds studied for skin-soothing "
  "properties. The practical framework: cool the skin first with cool (not "
  "ice-cold) water, apply plain aloe gel to intact mildly burned skin, "
  "reapply as it dries, keep hydrating, and protect healing skin from "
  "further sun. The boundary is explicit - aloe is for minor sunburn "
  "comfort; it does not repair deep burns, prevent skin damage already "
  "done, or replace sun protection. The demo grades sunburn scenarios by "
  "severity and routes each to home comfort or professional care."),
 "key_points": [
  "Traditional use with modest trial support for minor burns (Maenthaisong et al., 2007).",
  "Cooling comfort for minor sunburn; pair with cool water, fluids, and shade.",
  "Use plain gel on intact skin; not for serious burns or broken blistered skin without guidance.",
  "Does not undo sun damage or replace sun protection.",
  "Seek care for large-area blistering, fever, chills, or heat-illness signs.",
 ],
 "requirements": [
  "Reader must describe the evidence as modest and limited, never proven.",
  "Reader must state the severity boundary between home comfort and professional care.",
  "Reader must list the companion measures: cool water, fluids, shade, sun protection.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional with modest limited trial support.",
  SAFETY_STD,
 ],
 "citations": [
  "Maenthaisong R et al. The efficacy of aloe vera used for burn wound healing: a systematic review. Burns; 2007.",
  "National Center for Complementary and Integrative Health. Aloe vera: what the science says.",
 ],
},
{
 "key": "rice-sprain-basics",
 "name": "Rest, ice, compression, elevation for minor sprains",
 "group": "minor-ailments",
 "ladder_rank": 12, "ladder_tier": "foundations",
 "description": ("Rest, ice, compression, and elevation - RICE - is the "
  "classic first-aid framework for minor sprains and strains, taught in "
  "sports medicine worldwide. Evidence status: documented as standard first "
  "aid; modern guidance adds nuance (some clinicians now emphasize "
  "protection and gradual loading alongside rest), but the core remains "
  "mainstream. Rest prevents re-injury, ice limits swelling and pain, light "
  "compression controls swelling, and elevation drains fluid away from the "
  "injury. This record is honest that RICE manages the acute phase; it does "
  "not diagnose the injury. Inability to bear weight, visible deformity, "
  "numbness, or swelling that worsens after a day or two means professional "
  "evaluation for possible fracture or severe ligament injury."),
 "how_it_works": ("The record walks the four elements as a sequence: stop "
  "using the injured part (rest), apply wrapped cold in 15-minute sessions "
  "with breaks (ice), wrap with an elastic bandage snug but not tight "
  "enough to cause numbness or color change (compression), and raise the "
  "injury above heart level when possible (elevation). It teaches the "
  "compression check - fingers or toes should stay warm and pink - and the "
  "loading principle: gentle movement as pain allows in the following days, "
  "not prolonged immobilization for minor injuries. The demo verifies a "
  "RICE sequence for correct order and flags the compression-too-tight "
  "hazard plus the fracture red flags."),
 "key_points": [
  "Documented standard first aid for the acute phase of minor sprains and strains.",
  "Rest, wrapped ice in 15-minute sessions, snug-not-tight compression, elevation above heart level.",
  "Compression check: digits stay warm and pink; numbness or color change means rewrap looser.",
  "RICE manages the acute phase; it does not diagnose fractures or severe ligament injury.",
  "Seek care for inability to bear weight, deformity, numbness, or worsening swelling.",
 ],
 "requirements": [
  "Reader must recite the four elements and the compression safety check.",
  "Reader must state the fracture red flags that require professional evaluation.",
  "Reader must describe RICE as acute-phase management, not a diagnosis.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented standard first aid with modern nuance noted.",
  SAFETY_STD,
 ],
 "citations": [
  "National Athletic Trainers Association. Position statement on acute sprain and strain management.",
  "American Red Cross. First aid guidance for sprains: rest, ice, compression, elevation.",
 ],
},
{
 "key": "soap-water-wound-care",
 "name": "Soap and water: first-line minor wound cleaning",
 "group": "injury-and-recovery-care",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "description": ("For minor cuts and scrapes, mainstream wound-care guidance "
  "is clear and this record states it plainly: clean with mild soap and "
  "running water. Evidence status: documented - reviews including a "
  "Cochrane review (Fernandez and Griffiths, 2012) support water-based "
  "cleansing, and wound-care literature documents that harsh antiseptics "
  "such as hydrogen peroxide can damage the very tissue trying to heal. The "
  "old ritual of pouring peroxide on every scrape is traditional but "
  "counterproductive by current evidence. Cleaning removes dirt and "
  "bacteria mechanically; it does not sterilize, and no home cleaning "
  "method makes a wound sterile. Deep wounds, heavily contaminated wounds, "
  "animal or human bites, puncture wounds, or wounds that will not stop "
  "bleeding need professional care, and tetanus status should be current."),
 "how_it_works": ("The record teaches wound cleaning as a calm sequence: "
  "wash hands first, hold the wound under clean running water, wash the "
  "surrounding skin gently with mild soap (keeping soap mostly out of the "
  "wound itself), rinse thoroughly, pat dry with clean gauze, and cover. "
  "It explains why peroxide and alcohol sting: they injure healing cells "
  "along with germs. The boundary section covers bleeding control (firm "
  "direct pressure; pressure that does not stop bleeding in about 15 "
  "minutes means professional care) and the infection watch (increasing "
  "redness, warmth, swelling, pus, red streaks, or fever). The demo "
  "classifies cleaning agents as recommended, discouraged, or neutral with "
  "reasons."),
 "key_points": [
  "Documented: mild soap and clean running water are first-line for minor wounds (Cochrane-supported).",
  "Hydrogen peroxide and rubbing alcohol can damage healing tissue - traditional but counterproductive.",
  "Home cleaning removes contaminants; it does not sterilize a wound.",
  "Wash hands first; keep soap mostly out of the wound; pat dry with clean gauze.",
  "Seek care for deep or dirty wounds, bites, punctures, unstoppable bleeding, or infection signs.",
 ],
 "requirements": [
  "Reader must explain why peroxide is discouraged by current evidence.",
  "Reader must recite the cleaning sequence including hand washing.",
  "Reader must list the infection signs and the wounds that need professional care.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented; traditional peroxide ritual honestly corrected.",
  SAFETY_STD,
 ],
 "citations": [
  "Fernandez R, Griffiths R. Water for wound cleansing. Cochrane Database of Systematic Reviews; 2012.",
  "Centers for Disease Control and Prevention. Wound care guidance: cleaning minor cuts and scrapes.",
 ],
},
{
 "key": "moist-wound-covering",
 "name": "Covered moist wound care with petroleum jelly",
 "group": "injury-and-recovery-care",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "description": ("Since Winter's landmark 1962 work on moist wound healing, "
  "documented evidence has favored keeping minor wounds covered and "
  "slightly moist rather than letting them dry and scab: moist environments "
  "support faster re-epithelialization in the studied models. Evidence "
  "status: documented principle. The practical home version taught here: "
  "after soap-and-water cleaning, a thin layer of plain petroleum jelly "
  "under an adhesive bandage keeps the wound from drying out, and the "
  "American Academy of Dermatology lists petroleum jelly as the preferred "
  "home wound ointment - noting that antibiotic ointments add allergy risk "
  "without benefit for clean minor wounds. Change the covering daily or "
  "when wet or dirty. This is for minor wounds; anything deep, gaping, or "
  "heavily contaminated needs professional care."),
 "how_it_works": ("The record teaches the cover-and-moisten cycle: clean "
  "(previous record), thin layer of plain petroleum jelly, adhesive bandage "
  "or sterile gauze, change daily or sooner if wet or dirty, and watch the "
  "wound as it heals. It explains the mechanism honestly: the jelly is an "
  "occlusive barrier that prevents drying and keeps the bandage from "
  "sticking to new tissue; it has no antibiotic action and does not "
  "disinfect. The record also covers when to leave a minor wound uncovered "
  "(small clean scrapes once sealed) and the allergy note on antibiotic "
  "ointments. The demo builds a dressing-change schedule and checks each "
  "change interval against the daily-or-sooner rule."),
 "key_points": [
  "Documented principle: moist covered healing outperforms dry-and-scab for minor wounds (Winter, 1962).",
  "Plain petroleum jelly plus a bandage is the AAD-preferred home approach for clean minor wounds.",
  "Petroleum jelly is a moisture barrier, not a disinfectant; it has no antibiotic action.",
  "Change the covering daily or whenever wet or dirty.",
  "Deep, gaping, or heavily contaminated wounds need professional care, not home dressing.",
 ],
 "requirements": [
  "Reader must explain the moist-healing principle in plain language.",
  "Reader must state the dressing-change rule.",
  "Reader must distinguish minor wounds suited to home care from wounds needing professionals.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented wound-healing principle and dermatology guidance.",
  SAFETY_STD,
 ],
 "citations": [
  "Winter GD. Formation of the scab and the rate of epithelization of superficial wounds in the skin of the young domestic pig. Nature; 1962.",
  "American Academy of Dermatology. Wound care guidance: petroleum jelly for minor cuts and scrapes.",
 ],
},
{
 "key": "epsom-warm-soak",
 "name": "Warm Epsom salt soak for muscle soreness",
 "group": "injury-and-recovery-care",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "description": ("Soaking sore muscles in warm water with Epsom salt "
  "(magnesium sulfate) is a long-standing traditional practice. Evidence "
  "status: traditional with honest limits - warm water immersion itself has "
  "documented comfort benefits for muscle soreness (heat relaxes muscle and "
  "the soak is restful), but the claim that meaningful amounts of magnesium "
  "absorb through intact skin into the bloodstream is NOT established by "
  "quality evidence. This record separates the two: the warm soak is the "
  "documented comfort; the magnesium-absorption story is the unproven "
  "addition. Safety: water comfortably warm, never hot enough to scald; "
  "people with diabetes should check water temperature carefully and "
  "inspect feet afterward; never ingest Epsom salt as a remedy without "
  "professional direction."),
 "how_it_works": ("The record teaches the soak as a rest ritual: a basin or "
  "tub of comfortably warm water, Epsom salt dissolved per the package "
  "directions, a 15-to-20-minute soak window, then drying and rest. The "
  "honest mechanism section credits heat and rest for the relief and labels "
  "transdermal magnesium absorption as unproven. It covers the diabetes "
  "foot-care caution (reduced sensation plus warm water is a burn risk) and "
  "the cardiovascular caution (very hot baths stress the heart; keep water "
  "moderate and sessions reasonable). Muscle pain with weakness, numbness, "
  "dark urine after exertion, or pain that worsens needs professional "
  "evaluation. The demo plans soak sessions and verifies temperature and "
  "duration stay within the safe window."),
 "key_points": [
  "Traditional practice; the warm-water comfort is the documented part, magnesium absorption is unproven.",
  "Heat plus rest explains the relief honestly - no need for the absorption story.",
  "Comfortably warm water only; diabetes and circulation issues demand extra temperature care.",
  "Never ingest Epsom salt as a home remedy without professional direction.",
  "Seek care for muscle pain with weakness, numbness, dark urine, or worsening pain.",
 ],
 "requirements": [
  "Reader must separate the documented warm-water benefit from the unproven magnesium claim.",
  "Reader must state the temperature and diabetes cautions.",
  "Reader must know the muscle-injury red flags needing professional care.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional; absorption claim honestly marked not established.",
  SAFETY_STD,
 ],
 "citations": [
  "Traditional practice across spa and home-care literature; warm-water immersion comfort documented in musculoskeletal self-care guidance.",
  "Magnesium absorption through intact skin: no quality evidence establishing clinically meaningful uptake; claim marked not established.",
 ],
},
{
 "key": "turmeric-traditional-use",
 "name": "Turmeric in traditional wellness practice",
 "group": "injury-and-recovery-care",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "description": ("Turmeric - the golden spice of South Asian cooking and "
  "Ayurvedic tradition - is among the most studied culinary herbs in the "
  "world. Evidence status: traditional with emerging but limited clinical "
  "support - laboratory studies show anti-inflammatory activity of curcumin "
  "in cells and animals, and small human trials suggest possible benefit "
  "for some inflammatory conditions, but the evidence is preliminary and "
  "curcumin is famously poorly absorbed (Anand et al., 2007 documented the "
  "bioavailability problem). This record is explicit: turmeric as a cooking "
  "spice is a wholesome traditional food; turmeric as a disease treatment "
  "is not established. People on blood thinners, with gallbladder disease, "
  "or facing surgery should consult a professional before concentrated use."),
 "how_it_works": ("The record teaches turmeric honestly in two lanes. Lane "
  "one, the kitchen: turmeric as a regular cooking spice - in lentils, "
  "rice, soups, and the traditional golden-milk style warm drink - where "
  "its value is culinary tradition plus a plausible-but-unproven wellness "
  "bonus. Lane two, the supplement aisle: concentrated curcumin products "
  "make strong claims on weak evidence, often with absorption-enhancing "
  "additives that raise interaction questions. The record directs "
  "supplement-curious readers to professional guidance rather than "
  "self-experimentation. The demo classifies turmeric claims as kitchen "
  "tradition, plausible-but-unproven, or not established."),
 "key_points": [
  "Traditional culinary and Ayurvedic use; lab evidence of anti-inflammatory activity, limited human trials.",
  "Curcumin is poorly absorbed - the documented bioavailability problem (Anand et al., 2007).",
  "As a cooking spice: wholesome tradition. As a disease treatment: not established.",
  "Concentrated supplements make strong claims on weak evidence; consult a professional first.",
  "Blood thinners, gallbladder disease, or upcoming surgery: professional guidance required.",
 ],
 "requirements": [
  "Reader must explain the bioavailability problem in plain language.",
  "Reader must separate kitchen-spice tradition from supplement claims.",
  "Reader must state that turmeric is not an established treatment for any disease.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional with limited emerging support; disease claims marked not established.",
  SAFETY_STD,
 ],
 "citations": [
  "Anand P et al. Bioavailability of curcumin: problems and promises. Molecular Pharmaceutics; 2007.",
  "National Center for Complementary and Integrative Health. Turmeric: what the science says.",
 ],
},
{
 "key": "peppermint-tension-head",
 "name": "Peppermint oil for tension-headache comfort",
 "group": "injury-and-recovery-care",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "description": ("Topical peppermint oil is one of the few herbal headache "
  "approaches with genuine trial support: randomized trials (notably Gobel "
  "et al., published in Cephalalgia) found peppermint oil applied to the "
  "forehead and temples eased tension-type headache comparably to a common "
  "OTC pain reliever in the studied setting. Evidence status: documented "
  "with moderate, specific support for tension-type headache - NOT for "
  "migraine as an established treatment, and not a cure for headache "
  "disorders. The oil must be diluted in a carrier and kept away from eyes; "
  "undiluted essential oils can irritate skin. Headaches that are sudden "
  "and severe, follow head injury, or come with neurological symptoms need "
  "emergency evaluation, not peppermint."),
 "how_it_works": ("The record teaches the honest mechanism: menthol in "
  "peppermint creates a cooling sensation that may relax the pericranial "
  "muscles involved in tension headache and provides a competing sensory "
  "signal that eases perceived pain. The practical framework covers proper "
  "dilution in a carrier oil, a small skin-patch check for sensitivity, "
  "application to forehead and temples avoiding eyes, and pairing with the "
  "documented basics - hydration, rest, and reduced screen glare. The "
  "headache diary concept helps readers distinguish tension patterns from "
  "migraine patterns that need professional diagnosis. The demo analyzes a "
  "sample headache diary and routes tension-like patterns to comfort "
  "measures and red-flag patterns to professional care."),
 "key_points": [
  "Documented moderate support: peppermint oil eased tension-type headache in randomized trials (Gobel et al.).",
  "Specific to tension-type headache; migraine treatment is not established.",
  "Dilute in a carrier oil; keep away from eyes; patch-check sensitive skin.",
  "Pair with hydration, rest, and glare reduction - the documented basics.",
  "Sudden severe headache, post-injury headache, or neurological symptoms need emergency care.",
 ],
 "requirements": [
  "Reader must state the trial support accurately without overstating it.",
  "Reader must describe dilution and eye-avoidance safety rules.",
  "Reader must know the headache red flags requiring emergency care.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented moderate support for tension-type headache specifically.",
  SAFETY_STD,
 ],
 "citations": [
  "Gobel H et al. Essential plant oils and headache mechanisms. Trials of peppermint oil in tension-type headache. Cephalalgia.",
  "National Center for Complementary and Integrative Health. Peppermint oil: what the science says.",
 ],
},
{
 "key": "steam-congestion-care",
 "name": "Steam inhalation for nasal congestion",
 "group": "injury-and-recovery-care",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "description": ("Leaning over a bowl of hot water with a towel over the "
  "head is a classic traditional congestion remedy. Evidence status: "
  "traditional with limited direct evidence - the warm moist air feels "
  "soothing and may loosen mucus subjectively, but quality trials showing "
  "meaningful benefit are lacking, and the practice carries a documented "
  "hazard: scald burns from spilled water or steam, with pediatric burn "
  "cases reported in medical literature. This record teaches the safer "
  "modern alternative first - a hot shower, which delivers the same warm "
  "moist air without a bowl of scalding water to knock over - and gives "
  "strict safety rules for anyone who still chooses the bowl method. "
  "Congestion with high fever, facial swelling, or symptoms beyond ten days "
  "needs professional evaluation."),
 "how_it_works": ("The record is structured as harm reduction: the "
  "preferred method is simply standing in a hot shower and breathing the "
  "warm moist air, which captures the traditional benefit with minimal burn "
  "risk. For the bowl method, the rules are strict - water hot but not "
  "boiling, bowl on a stable surface, face at a safe distance, children "
  "supervised at arm's length or excluded entirely, and never leave the "
  "setup unattended. The mechanism section is honest: subjective soothing "
  "is the main documented effect; claims of clearing infection are not "
  "established. The demo runs a burn-risk audit over sample steam routines "
  "and recommends the shower alternative where risk is high."),
 "key_points": [
  "Traditional practice; subjective soothing is the main effect, strong benefit not established.",
  "Scald burns are the documented hazard - pediatric cases reported in medical literature.",
  "A hot shower delivers the warm moist air with far less burn risk; prefer it.",
  "Bowl method rules: stable surface, safe distance, supervised children, never unattended.",
  "Seek care for high fever, facial swelling, or congestion beyond ten days.",
 ],
 "requirements": [
  "Reader must name the scald hazard and the safer shower alternative.",
  "Reader must recite the bowl-method safety rules.",
  "Reader must describe the benefit as subjective soothing, not established treatment.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional; burn hazard documented and addressed first.",
  SAFETY_STD,
 ],
 "citations": [
  "Burn-injury case literature on steam-inhalation scalds, including pediatric cases.",
  "Traditional practice; symptomatic soothing consistent with warm humid air physiology.",
 ],
},
{
 "key": "oral-rehydration-basics",
 "name": "Oral rehydration for dehydration support",
 "group": "injury-and-recovery-care",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "description": ("Oral rehydration - replacing water, salts, and sugars lost "
  "to vomiting, diarrhea, heat, or exertion - is among the most documented "
  "interventions in medicine: the World Health Organization lists oral "
  "rehydration salts (ORS) as essential medicine, credited with saving "
  "millions of lives from diarrheal dehydration. Evidence status: documented "
  "and foundational. The science is the glucose-sodium co-transport "
  "mechanism: a precise balance of salt and sugar pulls water into the "
  "bloodstream far more effectively than plain water during active fluid "
  "loss. This record gives NO homemade ORS recipe - the salt-sugar ratio "
  "matters and errors can harm, so commercial ORS packets or professional "
  "guidance are the directed sources. Severe dehydration (little or no "
  "urine, dizziness on standing, confusion, sunken eyes in children) needs "
  "urgent professional care."),
 "how_it_works": ("The record teaches dehydration literacy: the early signs "
  "(thirst, dark urine, dry mouth, fatigue), the moderate signs (dizziness, "
  "headache, reduced urine), and the severe signs that end home care and "
  "start urgent care. It explains the co-transport mechanism in plain "
  "language - why ORS outperforms water, juice, or sports drinks during "
  "real fluid loss - and the practical rule of small frequent sips rather "
  "than large gulps when nauseated. It is explicit that this record "
  "educates about rehydration; it does not formulate ORS at home. The demo "
  "counts dehydration signs from a symptom checklist and classifies the "
  "result as mild, moderate, or seek-urgent-care."),
 "key_points": [
  "Documented and foundational: WHO essential medicine; the glucose-sodium co-transport mechanism is established science.",
  "ORS outperforms plain water during active fluid loss - the salt-sugar balance is the mechanism.",
  "No homemade recipe in this record; the ratio matters, so commercial ORS or professional guidance is directed.",
  "Small frequent sips beat large gulps when nausea is present.",
  "Severe signs - no urine, confusion, dizziness on standing, sunken eyes - need urgent care.",
 ],
 "requirements": [
  "Reader must explain the co-transport mechanism in plain language.",
  "Reader must list the dehydration sign ladder from mild to severe.",
  "Reader must state that no home ORS formulation is given and why.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented foundational medicine; formulation withheld for safety.",
  SAFETY_STD,
 ],
 "citations": [
  "World Health Organization. Oral rehydration salts: essential medicine listing and diarrheal-disease guidance.",
  "UNICEF and WHO joint guidance on oral rehydration therapy for dehydration from diarrheal illness.",
 ],
},
{
 "key": "heat-menstrual-comfort",
 "name": "Heat therapy for menstrual-cramp comfort",
 "group": "injury-and-recovery-care",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "description": ("Applying heat to the lower abdomen for menstrual cramps "
  "(dysmenorrhea) has documented support: a Cochrane review (Proctor and "
  "Farquhar, 2006, with updates) found heat therapy relieved menstrual pain "
  "in the included trials, performing comparably to a common OTC pain "
  "reliever in some comparisons. Evidence status: documented with moderate "
  "support as a comfort measure. The mechanism is straightforward: heat "
  "relaxes the uterine muscle contractions behind cramp pain and increases "
  "local blood flow. This record is honest that heat manages the symptom; "
  "it does not treat underlying conditions such as endometriosis, and "
  "cramps that are severe, worsening, or new in pattern warrant "
  "professional evaluation. Standard burn precautions apply: warm, not "
  "scalding, with a cloth barrier for direct heat sources."),
 "how_it_works": ("The record teaches heat as a first-line comfort ritual: "
  "a heating pad on a moderate setting, a warm water bottle wrapped in "
  "cloth, or a warm bath, applied to the lower abdomen during cramp peaks, "
  "paired with rest and the documented option of OTC pain relievers for "
  "those who use them. It covers the honest comparison - heat alone helps "
  "many people; heat plus an OTC pain reliever helps more in the studied "
  "data - without prescribing either. The escalation section covers red "
  "flags: pain that disrupts life monthly, pain with heavy bleeding, pain "
  "between periods, or pain that suddenly worsens - all reasons for "
  "professional evaluation rather than silent endurance. The demo builds a "
  "comfort-plan schedule across a cramp day and checks heat-source safety."),
 "key_points": [
  "Documented moderate support: heat relieved menstrual pain in trials, comparable to OTC options in some comparisons (Cochrane).",
  "Mechanism: heat relaxes uterine muscle contractions and increases local blood flow.",
  "Warm, not scalding; cloth barrier for direct heat sources - burn precautions apply.",
  "Manages the symptom; does not treat underlying conditions like endometriosis.",
  "Seek care for severe, worsening, life-disrupting, or new-pattern pelvic pain.",
 ],
 "requirements": [
  "Reader must describe the heat mechanism in plain language.",
  "Reader must state the burn precautions for heat application.",
  "Reader must know the pelvic-pain red flags needing professional evaluation.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented moderate support as a comfort measure.",
  SAFETY_STD,
 ],
 "citations": [
  "Proctor M, Farquhar C. Diagnosis and management of dysmenorrhoea. Cochrane-linked review literature on heat therapy for menstrual pain.",
  "Mainstream gynecologic guidance listing heat as first-line self-care for primary dysmenorrhea.",
 ],
},
{
 "key": "lavender-calm-ritual",
 "name": "Lavender scent for everyday calm",
 "group": "injury-and-recovery-care",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "description": ("Lavender scent is among the most studied aromas in "
  "relaxation research. Evidence status: modest and preliminary - small "
  "trials and reviews (such as Koulivand et al., 2013) report lavender "
  "aromatherapy associated with reduced self-reported stress and improved "
  "sleep quality in some settings, but studies are small, blinding is "
  "difficult, and lavender is not an established treatment for anxiety "
  "disorders or insomnia. This record frames lavender honestly: a pleasant "
  "sensory cue that can anchor a calming ritual, with the ritual doing much "
  "of the work. Safety: keep essential oils away from eyes and mucous "
  "membranes, dilute for skin use, keep away from small children and pets "
  "in concentrated form, and never ingest essential oils."),
 "how_it_works": ("The record teaches scent-anchored calming: choose one "
  "consistent lavender product (a sachet, a diluted roller, a room spray), "
  "pair it deliberately with an existing wind-down routine, and let the "
  "brain build the association between the scent and the calm state - the "
  "mechanism is classical conditioning more than pharmacology, and the "
  "record says so. It covers the honest evidence summary, the safety rules "
  "for concentrated oils, and the boundary: persistent anxiety, panic, or "
  "insomnia are reasons for professional care, not stronger scents. The "
  "demo scores a wind-down routine for its calming elements and reports "
  "which evidence-backed components are present."),
 "key_points": [
  "Modest preliminary evidence for stress and sleep-quality associations; small trials, difficult blinding.",
  "The ritual pairing does much of the work - scent as a conditioned calm cue, honestly framed.",
  "Not an established treatment for anxiety disorders or insomnia.",
  "Essential-oil safety: away from eyes, diluted for skin, away from small children and pets, never ingested.",
  "Persistent anxiety, panic, or insomnia warrant professional care.",
 ],
 "requirements": [
  "Reader must describe the evidence as modest and preliminary.",
  "Reader must explain the conditioning mechanism honestly.",
  "Reader must recite the essential-oil safety rules.",
 ],
 "standards": [
  "Evidence status labeled per claim: modest preliminary support; ritual mechanism honestly credited.",
  SAFETY_STD,
 ],
 "citations": [
  "Koulivand PH et al. Lavender and the nervous system. Evidence-Based Complementary and Alternative Medicine; 2013.",
  "National Center for Complementary and Integrative Health. Lavender: what the science says.",
 ],
},
{
 "key": "echinacea-evidence-review",
 "name": "Echinacea for colds: what the evidence actually says",
 "group": "injury-and-recovery-care",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "description": ("Echinacea is the classic case study this database uses to "
  "teach evidence honesty. Evidence status: mixed and weak overall - the "
  "Cochrane review (Karsch-Volk et al., 2014, updating earlier reviews) "
  "concluded that echinacea products show, at best, a small possible "
  "benefit for preventing or treating the common cold, with many trials "
  "showing no effect and product variability making comparisons difficult. "
  "Different species, plant parts, and preparations behave differently, so "
  "\"echinacea\" on a label does not name a single consistent thing. This "
  "record neither endorses nor forbids echinacea; it reports the evidence "
  "as it stands. People with ragweed-family allergies or autoimmune "
  "conditions should consult a professional before use."),
 "how_it_works": ("The record walks the reader through reading the "
  "Cochrane conclusion like a literate consumer: what \"weak evidence of "
  "possible small benefit\" means, why product variability undermines "
  "strong claims, and how marketing routinely outruns the data. It teaches "
  "the label-reading skill - species, plant part, preparation type, and "
  "standardization claims - so readers can see what a product actually "
  "contains versus what its marketing implies. The boundary is clear: "
  "echinacea does not cure colds, does not replace the supportive care in "
  "this database, and cold symptoms with red flags still need professional "
  "care. The demo tallies a small table of trial outcomes and computes the "
  "proportion showing benefit, labeling the result honestly."),
 "key_points": [
  "Mixed and weak overall: Cochrane review found at best a small possible benefit; many trials showed none.",
  "Product variability (species, part, preparation) makes strong claims unreliable.",
  "This record reports the evidence; it neither endorses nor forbids echinacea.",
  "Label literacy matters: marketing routinely outruns the trial data.",
  "Ragweed-family allergies or autoimmune conditions: consult a professional first.",
 ],
 "requirements": [
  "Reader must summarize the Cochrane conclusion accurately.",
  "Reader must explain why product variability weakens echinacea claims.",
  "Reader must state that echinacea does not cure colds.",
 ],
 "standards": [
  "Evidence status labeled per claim: mixed and weak; the record models evidence honesty.",
  SAFETY_STD,
 ],
 "citations": [
  "Karsch-Volk M et al. Echinacea for preventing and treating the common cold. Cochrane Database of Systematic Reviews; 2014.",
  "National Center for Complementary and Integrative Health. Echinacea: what the science says.",
 ],
},
{
 "key": "vitamin-c-cold-review",
 "name": "Vitamin C and the common cold: honest evidence",
 "group": "injury-and-recovery-care",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "description": ("Vitamin C and colds is the most famous supplement story "
  "in the world, and the evidence deserves its honest telling. Evidence "
  "status: documented with narrow, modest findings - the Cochrane review "
  "(Hemilä and Chalker, 2013) found regular vitamin C supplementation did "
  "not prevent colds in the general population, but did modestly reduce "
  "cold duration (about 8 percent in adults, 14 percent in children in the "
  "pooled data) and showed stronger effects in people under heavy physical "
  "stress. It does not cure colds, does not treat flu, and megadoses add "
  "gastrointestinal upset without added benefit. This record separates the "
  "sensible baseline - vitamin C from fruits and vegetables as everyday "
  "nutrition - from the supplement mythology."),
 "how_it_works": ("The record teaches the numbers plainly: what an 8 "
  "percent duration reduction means on a 7-day cold (roughly half a day), "
  "why prevention claims fail in the general-population data, and which "
  "subgroup (heavy physical stress) showed the real signal. It covers the "
  "food-first framing - citrus, peppers, berries, and leafy greens as "
  "reliable sources - and the honest supplement boundary: routine high-dose "
  "supplementation for cold prevention is not supported, and very high "
  "doses cause digestive upset. The demo computes the expected duration "
  "reduction from the Cochrane percentages for sample cold lengths and "
  "prints the modest results without exaggeration."),
 "key_points": [
  "Documented narrow findings: no prevention in the general population (Cochrane, Hemilä and Chalker, 2013).",
  "Modest duration reduction: about 8 percent in adults, 14 percent in children in pooled data.",
  "Does not cure colds or treat flu; megadoses add stomach upset, not benefit.",
  "Food-first: fruits and vegetables are the sensible baseline source.",
  "Stronger signal only in people under heavy physical stress - a narrow subgroup.",
 ],
 "requirements": [
  "Reader must state the prevention finding and the duration finding separately and accurately.",
  "Reader must translate the percentage into plain days for a sample cold.",
  "Reader must explain why megadosing is not supported.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented narrow findings; mythology honestly separated.",
  SAFETY_STD,
 ],
 "citations": [
  "Hemilä H, Chalker E. Vitamin C for preventing and treating the common cold. Cochrane Database of Systematic Reviews; 2013.",
  "National Institutes of Health, Office of Dietary Supplements. Vitamin C fact sheet: cold findings and upper intake guidance.",
 ],
},
{
 "key": "arnica-traditional-review",
 "name": "Arnica in traditional practice: honest evidence",
 "group": "injury-and-recovery-care",
 "ladder_rank": 24, "ladder_tier": "compounded",
 "description": ("Arnica montana - the mountain daisy of European folk "
  "medicine - is traditionally applied to bruises, sprains, and muscle "
  "soreness, and taken in highly diluted homeopathic preparations. Evidence "
  "status: traditional with weak clinical support - systematic reviews find "
  "insufficient quality evidence that arnica (topical or homeopathic) "
  "meaningfully improves bruising, pain, or swelling beyond placebo, though "
  "it remains popular. This record reports that finding plainly rather than "
  "repeating marketing claims. Safety: arnica is for external use on "
  "unbroken skin in traditional practice; it should never be applied to "
  "open wounds and never ingested as the raw plant, which is toxic. "
  "Homeopathic dilutions contain negligible active ingredient, which is "
  "itself part of the honest evidence picture."),
 "how_it_works": ("The record uses arnica to teach the popularity-versus-"
  "evidence distinction: a remedy can be beloved for centuries and still "
  "lack quality trial support, and both facts can be true at once. It "
  "covers the traditional topical use (bruises and soreness, unbroken skin "
  "only), the homeopathic-dilution reality (negligible active content), "
  "and the safety boundaries (not on open wounds, never ingested as plant "
  "material). It directs readers with real injuries to the documented "
  "first-aid records in this database - cold, compression, rest - rather "
  "than relying on arnica for injuries that need real care. The demo "
  "classifies arnica claims as traditional, weakly supported, or not "
  "established."),
 "key_points": [
  "Traditional European folk use for bruises, sprains, and soreness; clinical support is weak.",
  "Systematic reviews find insufficient quality evidence beyond placebo effects.",
  "External use on unbroken skin only in traditional practice; never on open wounds.",
  "Raw arnica plant is toxic if ingested; homeopathic dilutions contain negligible active ingredient.",
  "Real injuries deserve the documented first-aid records in this database, not reliance on arnica.",
 ],
 "requirements": [
  "Reader must state the evidence finding accurately without repeating marketing claims.",
  "Reader must explain the popularity-versus-evidence distinction.",
  "Reader must recite the external-use-only and open-wound safety boundaries.",
 ],
 "standards": [
  "Evidence status labeled per claim: traditional with weak clinical support, honestly reported.",
  SAFETY_STD,
 ],
 "citations": [
  "Systematic review literature on arnica for bruising and musculoskeletal pain: insufficient quality evidence of meaningful benefit.",
  "National Center for Complementary and Integrative Health. Arnica: traditional use and safety notes.",
 ],
},
{
 "key": "sleep-hygiene-practice",
 "name": "Sleep hygiene: the documented foundation of wellness",
 "group": "wellness-practices",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "description": ("Sleep hygiene - the set of habits that protect sleep "
  "quality - is among the best-documented wellness practices in medicine: "
  "sleep-medicine guidance (including American Academy of Sleep Medicine "
  "and CDC guidance) consistently lists consistent sleep timing, a dark "
  "cool quiet bedroom, daytime light exposure, regular exercise, and "
  "caffeine and alcohol limits as first-line behavioral foundations. "
  "Evidence status: documented. Poor sleep degrades immunity, mood, pain "
  "tolerance, and healing - which is why this database places sleep hygiene "
  "at the advanced tier: it amplifies every other remedy. This record is "
  "honest that sleep hygiene manages habits, not sleep disorders; chronic "
  "insomnia, loud snoring with breathing pauses, or excessive daytime "
  "sleepiness warrant professional evaluation for conditions like sleep "
  "apnea."),
 "how_it_works": ("The record teaches sleep hygiene as a checklist with "
  "mechanisms: consistent wake time anchors the circadian clock; morning "
  "daylight sets the melatonin timer; the dark cool quiet bedroom removes "
  "the three sleep enemies; daytime exercise deepens night sleep; caffeine "
  "has a long half-life so afternoon cutoffs matter; alcohol fragments "
  "sleep architecture despite its sedative feel; and screens lose to a "
  "wind-down routine. The framework is behavioral and free - no products "
  "required - which the record presents as its strength. The demo scores "
  "a sample week of habits against the checklist and reports the coverage "
  "with specific gaps named."),
 "key_points": [
  "Documented first-line behavioral foundation in sleep-medicine guidance (AASM, CDC).",
  "Consistent wake time, daylight, dark cool quiet room, exercise, caffeine and alcohol limits.",
  "Poor sleep degrades immunity, mood, pain tolerance, and healing - it amplifies every remedy.",
  "Behavioral and free: no products required, which is presented as its strength.",
  "Chronic insomnia, breathing pauses in sleep, or severe daytime sleepiness need professional evaluation.",
 ],
 "requirements": [
  "Reader must list the core sleep-hygiene habits with their mechanisms.",
  "Reader must explain why sleep amplifies every other remedy in this database.",
  "Reader must know the sleep-disorder red flags needing professional evaluation.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented behavioral foundation.",
  SAFETY_STD,
 ],
 "citations": [
  "American Academy of Sleep Medicine. Healthy sleep habits guidance.",
  "Centers for Disease Control and Prevention. Sleep hygiene guidance for adults.",
 ],
},
{
 "key": "slow-breathing-practice",
 "name": "Slow breathing exercises for everyday stress",
 "group": "wellness-practices",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "description": ("Slow, deliberate breathing - including the box-breathing "
  "pattern used in military and first-responder training - has documented "
  "support for acute stress reduction: reviews (such as Zaccaro et al., "
  "2018) find slow breathing reliably lowers self-reported stress and "
  "physiological arousal markers in the studied settings. Evidence status: "
  "documented with moderate support for stress and arousal reduction. The "
  "mechanism is the vagus nerve and baroreflex: extended exhales signal "
  "safety to the autonomic nervous system and slow the heart. This record "
  "is honest that breathing exercises manage the stress response; they do "
  "not treat anxiety disorders, and anyone with breathing difficulties "
  "should practice gently and consult a professional about underlying "
  "conditions."),
 "how_it_works": ("The record teaches two patterns as skills. Box "
  "breathing: inhale for a slow count of four, hold four, exhale four, hold "
  "four, repeated for several minutes. Extended-exhale breathing: inhale "
  "for four, exhale for six to eight, which emphasizes the calming "
  "parasympathetic signal. The framework covers posture, nasal versus mouth "
  "breathing, session length, and the practice principle: the calm is "
  "trained, not summoned, so brief daily practice outperforms occasional "
  "long sessions. The demo computes breath-cycle timing math for sample "
  "patterns and verifies the exhale emphasis of each pattern."),
 "key_points": [
  "Documented moderate support for stress and arousal reduction (Zaccaro et al., 2018).",
  "Mechanism: extended exhales signal safety via the vagus nerve and slow the heart.",
  "Box breathing and extended-exhale breathing taught as trainable skills.",
  "Brief daily practice outperforms occasional long sessions - calm is trained, not summoned.",
  "Manages the stress response; not a treatment for anxiety disorders or breathing conditions.",
 ],
 "requirements": [
  "Reader must demonstrate both breathing patterns with correct counts.",
  "Reader must explain the exhale-emphasis mechanism in plain language.",
  "Reader must state the boundary between stress management and clinical anxiety.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented moderate support for stress and arousal reduction.",
  SAFETY_STD,
 ],
 "citations": [
  "Zaccaro A et al. How breath-control can change your life: a systematic review on psycho-physiological correlates of slow breathing. Frontiers in Human Neuroscience; 2018.",
  "National Center for Complementary and Integrative Health. Relaxation techniques: what the science says.",
 ],
},
{
 "key": "gentle-walking-practice",
 "name": "Gentle walking for stiffness and mood",
 "group": "wellness-practices",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "description": ("Walking is the most documented low-intensity wellness "
  "practice in existence: public-health guidance (including CDC physical "
  "activity guidance) consistently finds regular walking associated with "
  "better cardiovascular markers, mood, sleep quality, and musculoskeletal "
  "comfort, and clinical guidance for low back pain favors staying active "
  "over bed rest. Evidence status: documented. For the stiffness and low "
  "mood that accompany minor illness and recovery, gentle walking is the "
  "database's advanced-tier answer: it moves lymph, loosens stiff joints, "
  "lifts mood through documented mechanisms, and costs nothing. This "
  "record is honest that walking supports recovery; it does not treat "
  "disease. Chest pain, severe shortness of breath, or dizziness with "
  "exertion are stop-and-seek-care signals, not push-through signals."),
 "how_it_works": ("The record teaches walking as a graded practice: start "
  "with comfortable short walks on flat ground, add minutes gradually "
  "across weeks, keep a conversational pace where breathing stays easy, "
  "and treat consistency as the entire goal. It covers the honest "
  "mechanisms - joint lubrication through movement, mood lift through "
  "documented neurochemical and behavioral pathways, sleep deepening "
  "through daytime activity - and the progression principle: the body "
  "adapts to what it repeatedly does. Footwear, surface, weather, and "
  "hydration get practical notes. The demo builds a graded walking plan "
  "across four weeks and verifies the progression stays gradual."),
 "key_points": [
  "Documented across public-health guidance for cardiovascular, mood, sleep, and musculoskeletal benefit.",
  "Clinical back-pain guidance favors staying active over bed rest.",
  "Graded progression: comfortable starts, minutes added across weeks, conversational pace.",
  "Consistency is the entire goal; the practice costs nothing.",
  "Chest pain, severe breathlessness, or dizziness with exertion are stop-and-seek-care signals.",
 ],
 "requirements": [
  "Reader must describe the graded progression principle.",
  "Reader must explain the mechanisms in plain language.",
  "Reader must know the exertion red flags that stop the walk.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented public-health and clinical guidance.",
  SAFETY_STD,
 ],
 "citations": [
  "Centers for Disease Control and Prevention. Physical activity guidance: walking as aerobic activity.",
  "Clinical guidance on low back pain favoring maintained activity over prolonged bed rest.",
 ],
},
{
 "key": "fermented-foods-gut",
 "name": "Fermented foods and gut wellness",
 "group": "wellness-practices",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "description": ("Fermented foods - yogurt with live cultures, kefir, "
  "kimchi, sauerkraut, miso, and similar traditional foods - are the "
  "food-first lane of the probiotic story. Evidence status: honestly "
  "mixed and strain-specific - specific probiotic strains show documented "
  "benefit for specific conditions (certain strains for antibiotic-"
  "associated diarrhea, for example), but effects do not transfer across "
  "strains, and generic \"supports gut health\" claims on foods outrun the "
  "evidence. This record teaches the strain-specificity principle as its "
  "core lesson: the right question is always which organism, for which "
  "condition, in what dose, with what evidence. Fermented foods as "
  "traditional dietary variety are wholesome; fermented foods as disease "
  "treatment are not established. People with compromised immunity should "
  "consult a professional about live-culture products."),
 "how_it_works": ("The record teaches a traditional-foods framework: build "
  "dietary variety with fermented foods as part of an overall vegetable-"
  "rich, fiber-rich eating pattern - the pattern with the documented gut "
  "benefit - rather than chasing single products. It covers label literacy "
  "(live and active cultures versus heat-treated), the strain-specificity "
  "principle with concrete examples, and the honest boundary between "
  "dietary tradition and medical treatment. Digestive symptoms that are "
  "severe, persistent, or involve bleeding or unexplained weight loss need "
  "professional evaluation, not yogurt. The demo scores a sample week of "
  "meals for fermented-food variety and fiber-rich pattern elements."),
 "key_points": [
  "Strain-specificity is the core lesson: documented benefits belong to specific strains for specific conditions.",
  "Generic gut-health claims on foods routinely outrun the evidence.",
  "Fermented foods as traditional dietary variety are wholesome; as disease treatment, not established.",
  "The fiber-rich, vegetable-rich overall pattern carries the documented gut benefit.",
  "Compromised immunity: professional guidance on live-culture products; severe digestive symptoms need evaluation.",
 ],
 "requirements": [
  "Reader must explain the strain-specificity principle with an example.",
  "Reader must distinguish dietary tradition from medical treatment claims.",
  "Reader must know the digestive red flags needing professional evaluation.",
 ],
 "standards": [
  "Evidence status labeled per claim: mixed and strain-specific, honestly reported.",
  SAFETY_STD,
 ],
 "citations": [
  "National Center for Complementary and Integrative Health. Probiotics: what the science says on strain-specific effects.",
  "Sanders ME et al. Probiotics and prebiotics: strain-specificity and evidence frameworks in the scientific literature.",
 ],
},
{
 "key": "red-flag-literacy",
 "name": "Red-flag symptoms: knowing when to seek professional care",
 "group": "wellness-practices",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "description": ("This is the most important record in the database: the "
  "complete red-flag literacy framework that bounds every other record. "
  "Evidence status: documented emergency and urgent-care guidance, drawn "
  "from mainstream triage standards. The core principle: home remedies and "
  "OTC comfort measures are for mild, familiar, stable symptoms in "
  "otherwise well people; everything else belongs to professionals. The "
  "record organizes red flags by system - chest pain or pressure, "
  "difficulty breathing, signs of stroke (face drooping, arm weakness, "
  "speech difficulty), severe headache of sudden onset, stiff neck with "
  "fever, severe abdominal pain, signs of severe dehydration, high or "
  "persistent fever, wounds that will not stop bleeding, head injury with "
  "neurological signs, allergic reaction with swelling or breathing "
  "difficulty, and any symptom that is rapidly worsening. When in doubt, "
  "professional evaluation wins over home care."),
 "how_it_works": ("The record teaches a three-tier decision framework. "
  "Tier one, emergency now: call emergency services for chest pain, "
  "breathing difficulty, stroke signs, severe sudden headache, major "
  "bleeding, or head injury with neurological change. Tier two, urgent "
  "professional care today: high or persistent fever, severe pain, "
  "dehydration signs, wounds needing closure, bites, or any rapidly "
  "worsening symptom. Tier three, home comfort measures: mild familiar "
  "symptoms in an otherwise well person, with a defined recheck point - "
  "if not improving on the expected timeline, escalate. Special "
  "populations - infants, older adults, pregnant people, the "
  "immunocompromised - escalate earlier. The demo classifies symptom "
  "scenarios into the three tiers with zero tolerance for under-triage."),
 "key_points": [
  "The bounding record: home measures are for mild, familiar, stable symptoms only.",
  "Emergency tier: chest pain, breathing difficulty, stroke signs, sudden severe headache, major bleeding.",
  "Urgent tier: persistent fever, severe pain, dehydration, bites, wounds needing closure, worsening symptoms.",
  "Home tier always carries a recheck point - not improving on schedule means escalate.",
  "Infants, older adults, pregnant people, and the immunocompromised escalate earlier.",
 ],
 "requirements": [
  "Reader must recite the three-tier framework with examples.",
  "Reader must list the emergency-tier symptoms without hesitation.",
  "Reader must explain the recheck-point principle for home care.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented emergency and urgent-care triage guidance.",
  SAFETY_STD,
 ],
 "citations": [
  "Mainstream emergency-medicine triage guidance on red-flag symptoms across body systems.",
  "Centers for Disease Control and Prevention. Guidance on when to seek care for common acute symptoms.",
 ],
},
{
 "key": "evidence-literacy",
 "name": "Reading a remedy claim: documented, traditional, or anecdotal",
 "group": "wellness-practices",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "description": ("This record teaches the skill that protects readers from "
  "every misleading remedy claim they will ever meet: evidence literacy. "
  "Evidence status: documented educational framework drawn from the "
  "hierarchy of evidence used across medicine and science. The ladder runs "
  "from strongest to weakest: systematic reviews of randomized trials, "
  "individual randomized trials, observational studies, traditional use "
  "across generations, expert opinion, and finally anecdote and "
  "testimonial - with marketing claims sitting outside the ladder entirely. "
  "The record teaches that traditional use is real evidence of cultural "
  "persistence, not evidence of efficacy; that testimonials prove nothing "
  "about cause; and that the honest question is always \"compared to what, "
  "measured how, in whom.\""),
 "how_it_works": ("The record works through claim-dissection drills: take a "
  "real-style marketing claim, identify which evidence tier it actually "
  "rests on, name the missing comparison, and restate the claim honestly. "
  "It covers the classic traps - the naturalistic fallacy (natural equals "
  "safe), the ancient-wisdom fallacy (old equals effective), the "
  "testimonial trap, the single-study trap, and the mechanism trap "
  "(plausible biology is not proof of benefit). Every record in this "
  "database is labeled with its tier, so readers can verify the system "
  "practices what it teaches. The demo grades sample claims by evidence "
  "tier and flags the fallacy in each."),
 "key_points": [
  "The evidence hierarchy: systematic reviews, randomized trials, observational studies, tradition, opinion, anecdote.",
  "Traditional use proves cultural persistence, not efficacy - both facts held at once.",
  "Testimonials prove nothing about cause; marketing sits outside the evidence ladder.",
  "The honest question: compared to what, measured how, in whom.",
  "Classic traps named: naturalistic, ancient-wisdom, testimonial, single-study, and mechanism fallacies.",
 ],
 "requirements": [
  "Reader must recite the evidence hierarchy in order.",
  "Reader must dissect a sample claim to its actual evidence tier.",
  "Reader must name at least three of the classic reasoning traps.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented educational framework from evidence-based medicine.",
  SAFETY_STD,
 ],
 "citations": [
  "Evidence-based medicine literature on the hierarchy of evidence (systematic reviews through anecdote).",
  "National Center for Complementary and Integrative Health. Guidance on evaluating health claims and the science behind them.",
 ],
},
{
 "key": "home-wellness-kit",
 "name": "Assembling a home wellness and first-aid kit",
 "group": "wellness-practices",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "description": ("A well-assembled home kit turns every other record in "
  "this database from reading material into ready practice. Evidence "
  "status: documented preparedness guidance, aligned with American Red "
  "Cross first-aid kit recommendations. The record lists the kit in "
  "categories: wound care (adhesive bandages in assorted sizes, sterile "
  "gauze, medical tape, plain petroleum jelly), comfort tools (reusable "
  "cold pack, thermometer, saline nasal spray), OTC basics kept per label "
  "and checked for expiry (pain and fever relievers, antihistamines), "
  "traditional comforts (honey for those over one year, ginger tea, "
  "chamomile), and information (poison-control number, allergy and "
  "medication list, this database's red-flag record printed or bookmarked). "
  "This record lists supplies; it gives no dosing and no treatment "
  "protocols beyond the records that teach them."),
 "how_it_works": ("The record teaches kit logic: organize by urgency (the "
  "bleeding-control and wound-care items most accessible), check expiry "
  "dates twice a year, store medicines up high and locked away from "
  "children, keep one kit at home and a smaller one for travel, and "
  "restock what gets used. It covers the child-safety principle (OTC "
  "medicines are a leading cause of pediatric poisoning) and the "
  "information principle (a kit without the red-flag record and a "
  "medication list is only half a kit). The demo runs a kit-inventory "
  "audit over a sample kit and reports missing categories."),
 "key_points": [
  "Organized by urgency: wound-care and bleeding-control items most accessible.",
  "Aligned with Red Cross first-aid kit guidance; expiry checked twice yearly.",
  "OTC medicines stored high and locked away from children - a leading pediatric poisoning cause.",
  "A kit without information (red-flag record, medication list, poison-control number) is half a kit.",
  "This record lists supplies only; dosing lives on product labels, treatment in the teaching records.",
 ],
 "requirements": [
  "Reader must list the kit categories from memory.",
  "Reader must explain the child-safety storage principle.",
  "Reader must state the expiry-check routine.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented preparedness guidance; supply list only, no dosing.",
  SAFETY_STD,
 ],
 "citations": [
  "American Red Cross. First-aid kit contents guidance.",
  "U.S. poison-control guidance on safe medicine storage around children.",
 ],
},
{
 "key": "recovery-nutrition",
 "name": "Everyday nutrition that supports recovery",
 "group": "wellness-practices",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "description": ("Recovery - from illness, injury, or exertion - runs on "
  "ordinary good nutrition, not on superfoods. Evidence status: documented "
  "nutritional science at the pattern level - adequate protein supports "
  "tissue repair, fruits and vegetables supply the micronutrients of immune "
  "function, and overall energy adequacy matters more than any single "
  "ingredient. This record is honest that no food cures disease and no "
  "single ingredient drives recovery; the pattern does the work. It teaches "
  "the plate as the unit of analysis: protein at each meal during "
  "recovery, colorful plant foods daily, whole grains for steady energy, "
  "and fluids alongside. People with diabetes, kidney disease, or other "
  "conditions with dietary restrictions should follow their professional's "
  "guidance over general patterns."),
 "how_it_works": ("The record teaches recovery eating as a pattern, not a "
  "prescription: regular meals rather than skipped ones, protein spread "
  "across the day, plants for micronutrient density, and attention to "
  "appetite (illness suppresses appetite, so smaller frequent meals beat "
  "ambitious ones). It covers the honest limits - nutrition supports the "
  "body's repair systems; it does not replace medical treatment - and the "
  "hydration pairing from this database's rehydration record. The demo "
  "scores sample recovery-day menus for pattern elements (protein spread, "
  "plant variety, meal regularity) without prescribing amounts."),
 "key_points": [
  "Documented at the pattern level: protein for repair, plants for micronutrients, energy adequacy overall.",
  "The pattern does the work; no single food or superfood drives recovery.",
  "Protein spread across the day; smaller frequent meals when illness suppresses appetite.",
  "Nutrition supports repair systems; it does not replace medical treatment.",
  "Dietary-restriction conditions follow professional guidance over general patterns.",
 ],
 "requirements": [
  "Reader must describe the recovery pattern without naming miracle foods.",
  "Reader must explain why the pattern outperforms single ingredients.",
  "Reader must state the boundary between nutritional support and medical treatment.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented nutritional science at the pattern level.",
  SAFETY_STD,
 ],
 "citations": [
  "Mainstream clinical nutrition guidance on protein and micronutrients in recovery and immune function.",
  "Dietary guidance on eating patterns versus single-nutrient claims.",
 ],
},
{
 "key": "sun-protection-practice",
 "name": "Sun protection as daily wellness practice",
 "group": "wellness-practices",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "description": ("Sun protection is the rare wellness practice where the "
  "evidence is overwhelming and the action is simple: ultraviolet radiation "
  "is a documented cause of skin cancer and premature skin aging, and "
  "mainstream dermatology guidance (including American Academy of "
  "Dermatology guidance) documents that shade, protective clothing, and "
  "broad-spectrum sunscreen reduce that risk. Evidence status: documented "
  "and strong. This record pairs naturally with the aloe sunburn record: "
  "aloe comforts the burn, but prevention is the documented strategy. It "
  "covers the honest sunscreen notes - broad-spectrum, water-resistant, "
  "reapplied with sweating or swimming - and the stronger-than-sunscreen "
  "measures: midday shade and covering clothing. Changing moles, non-"
  "healing sores, or new unusual growths warrant professional skin "
  "evaluation."),
 "how_it_works": ("The record teaches the protection hierarchy: timing and "
  "shade first (midday sun is strongest), clothing second (woven fabrics, "
  "wide-brim hats, sunglasses), sunscreen third as the exposed-skin layer. "
  "It explains UV index literacy - checking the day's index and scaling "
  "protection to it - and the reapplication principle honestly: sunscreen "
  "works while it is on the skin at adequate coverage, and it leaves the "
  "skin through sweat, water, and touch. The demo maps sample UV-index "
  "values to protection levels and verifies the hierarchy order."),
 "key_points": [
  "Documented and strong: UV causes skin cancer and aging; protection reduces the risk (AAD).",
  "Hierarchy: shade and timing first, clothing second, sunscreen third.",
  "Sunscreen notes: broad-spectrum, water-resistant, reapplied with sweat or water.",
  "UV-index literacy scales daily protection to the day's actual risk.",
  "Changing moles, non-healing sores, or unusual growths need professional skin evaluation.",
 ],
 "requirements": [
  "Reader must recite the protection hierarchy in order.",
  "Reader must explain UV-index literacy.",
  "Reader must know the skin-change signs needing professional evaluation.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented strong evidence.",
  SAFETY_STD,
 ],
 "citations": [
  "American Academy of Dermatology. Sun protection guidance: shade, clothing, and sunscreen.",
  "U.S. Environmental Protection Agency and dermatology guidance on the UV index.",
 ],
},
{
 "key": "rest-as-medicine",
 "name": "Rest as a recovery practice",
 "group": "wellness-practices",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "description": ("Rest is the oldest remedy in this database and the capstone "
  "of its ladder: every healing process the body runs - immune response, "
  "tissue repair, inflammation resolution - competes for the same energy "
  "budget, and rest frees that budget. Evidence status: documented "
  "principle across medicine; clinical guidance for colds, sprains, and "
  "post-exertion recovery consistently prescribes relative rest in the "
  "acute phase. This record is honest that rest is necessary but not "
  "sufficient: rest without the other measures is just waiting, while rest "
  "paired with hydration, nutrition, and appropriate care is recovery. It "
  "also teaches the modern nuance - relative rest and gradual return beat "
  "prolonged total immobilization for most musculoskeletal injuries - and "
  "the boundary: fatigue that is profound, persistent, or unexplained "
  "warrants professional evaluation rather than more rest."),
 "how_it_works": ("The record teaches rest as an active practice with "
  "three parts. First, permission: the cultural pressure to push through "
  "illness is named and set aside, because training or working through a "
  "feverish illness prolongs it in documented experience. Second, "
  "structure: sleep, horizontal rest, and screen-light days are scheduled "
  "like any treatment. Third, the return ladder: symptom-free milestones "
  "before resuming full activity, with the honest rule that returning too "
  "early restarts the clock. The demo builds a rest-and-return schedule "
  "for a sample recovery week and verifies the milestones precede the "
  "return."),
 "key_points": [
  "Documented principle: rest frees the energy budget that healing processes compete for.",
  "Necessary but not sufficient - rest paired with hydration, nutrition, and care is recovery.",
  "Relative rest plus gradual return beats prolonged total immobilization for most injuries.",
  "Pushing through feverish illness prolongs it; permission to rest is part of the prescription.",
  "Profound, persistent, or unexplained fatigue warrants professional evaluation.",
 ],
 "requirements": [
  "Reader must explain the energy-budget principle in plain language.",
  "Reader must describe the return ladder with symptom-free milestones.",
  "Reader must know the fatigue red flags needing professional evaluation.",
 ],
 "standards": [
  "Evidence status labeled per claim: documented principle across clinical guidance.",
  SAFETY_STD,
 ],
 "citations": [
  "Clinical guidance on acute-phase rest for colds, sprains, and post-exertion recovery.",
  "Sports-medicine literature on relative rest and graded return to activity.",
 ],
},
]

SIG_ENTRIES = [
{
 "key": "sig-morning-reset",
 "name": "The Signature Morning Reset",
 "group": "minor-ailments",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "description": ("Signature original: his Morning Reset framework opens the "
  "day the way the public honey record opens the ladder - with a small, "
  "deliberate comfort act. The framework has four beats: water first "
  "(rehydration after sleep), light (daylight or bright indoor light to "
  "set the day clock), movement (two minutes of gentle motion to loosen "
  "the night's stiffness), and intention (one sentence naming what the day "
  "is for). It is a ritual framework, not a medical protocol: it claims "
  "no treatment of any condition and carries the same safety framing as "
  "every record in this database - educational information only, not "
  "medical advice, professional care for anything beyond mild familiar "
  "symptoms. Clearly labeled Signature-made, never presented as authentic "
  "public record."),
 "how_it_works": ("The framework works through sequence psychology: the "
  "same four beats in the same order each morning build a conditioned "
  "start signal, and the record is honest that the ritual structure does "
  "the work rather than any single element. Water addresses overnight "
  "fluid loss; light anchors circadian timing (documented sleep-medicine "
  "principle, referenced not claimed); gentle movement addresses morning "
  "stiffness; the intention sentence gives the day a steering input. The "
  "framework includes the honesty clause: a morning ritual supports "
  "wellness; it diagnoses and treats nothing. The demo verifies a sample "
  "morning routine contains all four beats in order."),
 "key_points": [
  "Signature original framework: water, light, movement, intention - four beats in fixed order.",
  "A ritual framework, not a medical protocol; claims no treatment of any condition.",
  "The sequence psychology does the work: same order daily builds the start signal.",
  "References documented principles (hydration, light timing) without claiming them as Signature discovery.",
  "Clearly labeled Signature-made; educational information only, not medical advice.",
 ],
 "requirements": [
  "Reader must recite the four beats in order.",
  "Reader must state that the framework treats nothing and diagnoses nothing.",
  "Reader must repeat the Signature-made labeling honestly to others.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Sleep-medicine literature on morning light and circadian timing (referenced principle, not Signature discovery).",
 ],
},
{
 "key": "sig-evening-winddown",
 "name": "The Signature Evening Wind-Down",
 "group": "minor-ailments",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "description": ("Signature original: his Evening Wind-Down framework "
  "mirrors the public chamomile record - the calm before sleep, built as "
  "a Signature ritual. Three gates close the day: the light gate (dimming "
  "lights an hour before bed), the input gate (screens and news off, a "
  "calming input on - a warm caffeine-free drink, quiet music, or slow "
  "reading), and the body gate (slow breathing or gentle stretching to "
  "downshift the nervous system). The framework claims no treatment of "
  "insomnia or anxiety; persistent sleep problems are directed to "
  "professional care. Clearly labeled Signature-made, educational "
  "information only, not medical advice."),
 "how_it_works": ("The framework works by stacking three documented "
  "sleep-hygiene principles into one named ritual so they actually get "
  "done: dim light permits melatonin timing, cutting stimulating input "
  "lowers arousal, and the body gate gives the nervous system a deliberate "
  "downshift signal. The Signature contribution is the packaging - named "
  "gates, fixed order, a finish line - because the record is honest that "
  "adherence is the hard part of sleep hygiene and rituals solve "
  "adherence. The demo scores a sample evening against the three gates "
  "and names which gate is open."),
 "key_points": [
  "Signature original: three gates - light, input, body - closed in fixed order each evening.",
  "Stacks documented sleep-hygiene principles into one named, doable ritual.",
  "The Signature contribution is adherence packaging: named gates and a finish line.",
  "Claims no treatment of insomnia or anxiety; persistent problems go to professional care.",
  "Clearly labeled Signature-made; educational information only, not medical advice.",
 ],
 "requirements": [
  "Reader must name the three gates and their order.",
  "Reader must explain why ritual packaging aids adherence.",
  "Reader must state the professional-care boundary for persistent sleep problems.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "American Academy of Sleep Medicine healthy-sleep-habits guidance (referenced principle).",
 ],
},
{
 "key": "sig-hydration-ritual",
 "name": "The Signature Hydration Ritual",
 "group": "minor-ailments",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "description": ("Signature original: his Hydration Ritual framework turns "
  "the public fluids record into a daily Signature practice. The rule is "
  "rhythm over volume: water at waking, water with each meal, water at "
  "mid-afternoon, water in the evening wind-down - anchored to existing "
  "habits so no willpower is required. The framework teaches the honest "
  "hydration signs (pale straw urine, steady energy) and the honest limits "
  "(hydration supports wellness; it treats no disease). It carries no "
  "prescribed volumes - amounts are personal and belong to professional "
  "guidance for anyone with kidney, heart, or fluid-restriction conditions. "
  "Clearly labeled Signature-made, educational information only."),
 "how_it_works": ("The framework works through habit anchoring: each water "
  "moment attaches to an event that already happens daily, which the "
  "record presents as the entire behavioral technology. The check-in is "
  "observational - urine color, thirst, headache patterns - teaching "
  "readers to read their own signals rather than follow a number. The "
  "illness mode of the framework points to this database's rehydration "
  "record for vomiting, diarrhea, or heat illness, where professional-grade "
  "guidance applies. The demo audits a sample day for anchored hydration "
  "moments and reports coverage."),
 "key_points": [
  "Signature original: rhythm over volume - water anchored to waking, meals, afternoon, evening.",
  "Habit anchoring is the behavioral technology; no willpower required.",
  "Teaches observational check-ins (urine color, thirst) rather than prescribed volumes.",
  "Fluid-restriction conditions follow professional guidance, not this framework.",
  "Illness-mode dehydration points to the rehydration record and professional care.",
 ],
 "requirements": [
  "Reader must list the four anchored hydration moments.",
  "Reader must explain habit anchoring in plain language.",
  "Reader must state the fluid-restriction boundary.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Public-health hydration guidance (referenced principle, not Signature discovery).",
 ],
},
{
 "key": "sig-rest-covenant",
 "name": "The Signature Rest Covenant",
 "group": "minor-ailments",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "description": ("Signature original: his Rest Covenant reframes the "
  "public rest record as a personal agreement - a covenant the reader "
  "makes with their own body. The covenant has three articles: Article One, "
  "symptoms are information, not weakness - a feverish body asking for "
  "rest gets rest. Article Two, rest is scheduled like medicine - sleep, "
  "horizontal rest, and low-demand days go on the calendar during illness. "
  "Article Three, return is earned - symptom-free milestones precede full "
  "activity, and returning early restarts the clock. The covenant treats "
  "nothing and diagnoses nothing; it organizes the documented rest "
  "principle into a commitment device. Clearly labeled Signature-made, "
  "educational information only, not medical advice."),
 "how_it_works": ("The framework works as a commitment device: writing the "
  "three articles down and signing them converts a vague intention into "
  "a kept promise, which the record presents honestly as behavioral "
  "psychology rather than medicine. The illness protocol runs the articles "
  "in order - recognize the signal, schedule the rest, earn the return - "
  "and the recheck rule from the red-flag record governs throughout: rest "
  "at home is for mild familiar symptoms with a defined improvement "
  "timeline, and anything else escalates to professional care. The demo "
  "builds a rest-and-return schedule from the three articles and verifies "
  "milestones precede the return."),
 "key_points": [
  "Signature original: a three-article personal covenant organizing the documented rest principle.",
  "Article One: symptoms are information. Article Two: rest is scheduled. Article Three: return is earned.",
  "Works as a commitment device - behavioral psychology, honestly labeled as such.",
  "Treats nothing, diagnoses nothing; organizes rest into kept promises.",
  "The red-flag recheck rule governs throughout; escalation beats endurance.",
 ],
 "requirements": [
  "Reader must recite the three articles.",
  "Reader must explain the commitment-device mechanism honestly.",
  "Reader must state the recheck-and-escalate rule.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Clinical guidance on acute-phase rest (referenced principle).",
 ],
},
{
 "key": "sig-comfort-cup",
 "name": "The Signature Comfort Cup Framework",
 "group": "minor-ailments",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "description": ("Signature original: his Comfort Cup framework generalizes "
  "the public honey, ginger, and chamomile records into one Signature "
  "ritual for mild cold-season discomfort. The framework: one warm, "
  "caffeine-free drink, prepared slowly and deliberately, consumed seated "
  "and unhurried, with the honest understanding that the warmth, the "
  "fluids, the pause, and the traditional ingredient together make the "
  "comfort. The ingredient lane stays inside this database's documented "
  "pantry - honey (over one year only, never for infants), ginger tea, "
  "chamomile - and the framework repeats their safety boundaries rather "
  "than replacing them. Clearly labeled Signature-made, educational "
  "information only, not medical advice."),
 "how_it_works": ("The framework works through ritual density: slowing "
  "down the preparation, engaging the senses, and sitting with the warm "
  "cup converts a beverage into a calming event, which the record honestly "
  "credits as the main mechanism alongside the documented comfort of warm "
  "fluids. The ingredient is chosen from the documented pantry by symptom "
  "- honey-style soothing for cough, ginger-style for nausea, chamomile-"
  "style for evening - and every choice carries that record's safety "
  "rules. The boundary is explicit: the Comfort Cup comforts mild "
  "symptoms; red-flag symptoms bypass the cup entirely for professional "
  "care. The demo matches sample symptom sets to pantry ingredients and "
  "rejects unsafe matches."),
 "key_points": [
  "Signature original: one warm caffeine-free drink, prepared slowly, consumed unhurried.",
  "Ritual density is the mechanism: the pause and the senses do the work, honestly credited.",
  "Ingredients drawn only from this database's documented pantry, with their safety rules repeated.",
  "Honey lane keeps the 12-month boundary; ginger lane keeps the medication cautions.",
  "Red-flag symptoms bypass the cup entirely for professional care.",
 ],
 "requirements": [
  "Reader must describe the ritual-density mechanism honestly.",
  "Reader must match ingredients to symptoms with safety rules intact.",
  "Reader must state the red-flag bypass rule.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "The public honey, ginger, and chamomile records of this database (referenced).",
 ],
},
{
 "key": "sig-bump-care",
 "name": "The Signature Bump-and-Bruise Protocol",
 "group": "minor-ailments",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "description": ("Signature original: his Bump-and-Bruise Protocol turns "
  "the public cold-compress record into a named Signature sequence for "
  "minor bumps. The protocol runs C-A-L-M: Cold (wrapped compress, timed "
  "sessions), Assess (check skin, check function, check for head-injury "
  "signs), Limit (rest the area, avoid re-bumping), Monitor (recheck "
  "through the day for worsening). The head-injury branch is the "
  "protocol's most important part: any confusion, vomiting, unequal "
  "pupils, or lost consciousness routes to emergency care before the "
  "protocol continues. Clearly labeled Signature-made, educational "
  "information only, not medical advice."),
 "how_it_works": ("The protocol works as a mnemonic checklist that "
  "prevents the two classic home errors: forgetting the wrap (ice "
  "directly on skin) and forgetting the assessment (treating a head "
  "injury like a bruise). Each letter is a gate - Cold cannot proceed "
  "without the wrap rule, Assess cannot be skipped, Limit protects the "
  "healing window, Monitor catches the worsening case. The record is "
  "honest that the protocol organizes documented first aid; it adds "
  "structure, not medicine. The demo walks sample bump scenarios through "
  "C-A-L-M and routes head-injury variants to emergency care."),
 "key_points": [
  "Signature original mnemonic: C-A-L-M - Cold, Assess, Limit, Monitor.",
  "Prevents the two classic errors: unwrapped ice and skipped assessment.",
  "The head-injury branch routes to emergency care before the protocol continues.",
  "Organizes documented first aid; adds structure, not medicine.",
  "Clearly labeled Signature-made; educational information only, not medical advice.",
 ],
 "requirements": [
  "Reader must recite C-A-L-M with each step's content.",
  "Reader must state the head-injury emergency branch without hesitation.",
  "Reader must explain what the protocol adds (structure) and does not add (medicine).",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "American Red Cross first-aid guidance on cold application (referenced principle).",
 ],
},
{
 "key": "sig-pain-wisdom",
 "name": "The Signature Pain-Relief Wisdom Ledger",
 "group": "minor-ailments",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "description": ("Signature original: his Pain-Relief Wisdom Ledger is a "
  "personal record-keeping framework companion to the public acetaminophen "
  "and ibuprofen records. The ledger has four columns: what was taken (from "
  "the label, exact product name), when (date and time), why (the symptom), "
  "and what else (every other product taken that day, to catch the "
  "combination-product trap). The framework's honest purpose is overdose "
  "prevention through visibility: most accidental acetaminophen excess "
  "comes from not realizing two products share the ingredient, and a "
  "written ledger makes the invisible visible. It gives no dosing, makes "
  "no recommendations, and directs all dosing questions to labels and "
  "professionals. Clearly labeled Signature-made, educational information "
  "only."),
 "how_it_works": ("The framework works through externalized memory: pain "
  "and fever degrade exactly the attention needed to track medicines, so "
  "the ledger carries the tracking load. The daily review step - scanning "
  "the \"what else\" column for shared ingredients - is the trap-catching "
  "mechanism, and the record teaches the alternate-name literacy "
  "(acetaminophen, paracetamol, APAP) that makes the review work. The "
  "boundary is explicit: the ledger records, it never advises; persistent "
  "or severe pain goes to professional diagnosis. The demo audits sample "
  "ledger days and flags shared-ingredient overlaps."),
 "key_points": [
  "Signature original: a four-column personal ledger - what, when, why, what else.",
  "Overdose prevention through visibility: the written record catches the combination-product trap.",
  "Teaches alternate-name literacy (acetaminophen, paracetamol, APAP) for the daily review.",
  "Records only; never advises, never doses - dosing lives on labels and with professionals.",
  "Persistent or severe pain goes to professional diagnosis, not to the ledger.",
 ],
 "requirements": [
  "Reader must set up the four columns correctly.",
  "Reader must explain the combination-product trap the ledger catches.",
  "Reader must state that the ledger never gives dosing advice.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "FDA acetaminophen liver-injury warnings on combination products (referenced).",
 ],
},
{
 "key": "sig-inflammation-calm",
 "name": "The Signature Inflammation-Calm Framework",
 "group": "minor-ailments",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "description": ("Signature original: his Inflammation-Calm Framework is "
  "the Signature companion to the public ibuprofen record - a decision "
  "framework, not a dosing guide. The framework asks three questions "
  "before any NSAID use: Is inflammation actually the problem (swelling, "
  "heat, stiffness - the documented NSAID lane) or is it plain pain or "
  "fever (the acetaminophen lane)? Are any of my personal risk factors "
  "present (ulcer history, kidney or heart disease, NSAID-sensitive "
  "asthma, blood thinners)? Have I checked every label for a second "
  "NSAID hiding in a combination product? Only documented label literacy "
  "follows; the framework itself prescribes nothing. Clearly labeled "
  "Signature-made, educational information only, not medical advice."),
 "how_it_works": ("The framework works as a pre-use checklist that slows "
  "down automatic medicine-taking: the three questions force the "
  "distinction between pain types, surface personal risk factors, and "
  "catch stacking before it happens. The record is honest that the "
  "framework's value is entirely in the pause - most NSAID harm comes "
  "from casual, unexamined use, and a structured pause is the "
  "countermeasure. Anyone answering yes to a risk factor is directed to "
  "professional guidance before proceeding. The demo runs sample profiles "
  "through the three questions and routes risk-positive profiles to "
  "professional guidance."),
 "key_points": [
  "Signature original: three pre-use questions - right problem, risk factors, hidden second NSAID.",
  "A decision framework, not a dosing guide; prescribes nothing.",
  "The structured pause is the countermeasure to casual unexamined use.",
  "Risk-positive answers route to professional guidance before proceeding.",
  "Clearly labeled Signature-made; educational information only, not medical advice.",
 ],
 "requirements": [
  "Reader must recite the three questions.",
  "Reader must explain the pain-type distinction behind question one.",
  "Reader must state the professional-guidance routing for risk-positive answers.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "FDA NSAID labeling on stomach, kidney, and cardiovascular risks (referenced).",
 ],
},
{
 "key": "sig-seasonal-clarity",
 "name": "The Signature Seasonal Clarity Framework",
 "group": "minor-ailments",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "description": ("Signature original: his Seasonal Clarity Framework "
  "companions the public antihistamine record with an identification-first "
  "approach. The framework's core is the Allergy-or-Cold differentiation "
  "drill: itchy eyes and nose plus sneezing plus a seasonal pattern plus "
  "no fever points toward allergy; sore throat first plus body aches plus "
  "possible fever points toward cold - because the right comfort measures "
  "depend on the right identification. The framework then layers the "
  "non-drug lane first (pollen-hygiene habits: windows, showering after "
  "outdoor time, bedding) before the documented OTC lane, and it carries "
  "the emergency branch: breathing difficulty or swelling with allergy "
  "needs emergency care. Clearly labeled Signature-made, educational "
  "information only."),
 "how_it_works": ("The framework works through correct identification "
  "before action: the differentiation drill is run first, the non-drug "
  "habits second, and the OTC lane third with label literacy from the "
  "public record. The record is honest that the framework's contribution "
  "is sequencing - identification, habits, then medicine - rather than "
  "new medicine. The pollen-hygiene habits are presented as the "
  "underused lane: reducing exposure reduces the symptom load that "
  "medicine must then manage. The demo classifies symptom sets through "
  "the drill and sequences the response lanes."),
 "key_points": [
  "Signature original: identification first - the Allergy-or-Cold differentiation drill.",
  "Sequences the response: identify, then pollen-hygiene habits, then the documented OTC lane.",
  "The non-drug exposure-reduction lane is presented as the underused lever.",
  "Emergency branch: breathing difficulty or swelling with allergy needs emergency care.",
  "Clearly labeled Signature-made; educational information only, not medical advice.",
 ],
 "requirements": [
  "Reader must run the differentiation drill on sample symptom sets.",
  "Reader must list the pollen-hygiene habits.",
  "Reader must state the emergency branch without hesitation.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Mainstream allergy guidance on antihistamine generations and drowsiness (referenced).",
 ],
},
{
 "key": "sig-breath-easy",
 "name": "The Signature Breathe-Easy Ritual",
 "group": "minor-ailments",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "description": ("Signature original: his Breathe-Easy Ritual companions "
  "the public saline nasal record with a comfort ritual for congested "
  "days. The ritual: warm shower steam first (the safer traditional "
  "method), saline rinse or spray second (with the absolute safe-water "
  "rule repeated verbatim), rest with the head elevated third, and fluids "
  "throughout. The framework repeats the public record's safety core - "
  "distilled, sterile, or boiled-then-cooled water only; device cleaned "
  "and dried between uses - because a ritual that skips safety is not a "
  "Signature ritual. Congestion with high fever, facial swelling, or "
  "symptoms beyond ten days bypasses the ritual for professional care. "
  "Clearly labeled Signature-made, educational information only."),
 "how_it_works": ("The ritual works by sequencing the documented comfort "
  "measures so each amplifies the next: steam loosens, saline clears, "
  "elevation drains, fluids thin. The record is honest that the ritual "
  "organizes comfort measures; it treats no infection and shortens "
  "nothing. The safety repetition is deliberate - the safe-water rule "
  "appears in the ritual steps, not just in a warning box, because the "
  "record treats safety as choreography rather than fine print. The demo "
  "verifies a sample ritual sequence for correct order and safety-rule "
  "inclusion."),
 "key_points": [
  "Signature original ritual: steam, saline, elevation, fluids - sequenced so each amplifies the next.",
  "Repeats the safe-water rule verbatim inside the ritual steps, not just as a warning.",
  "Safety as choreography: the rules are part of the dance, not fine print.",
  "Organizes comfort measures; treats no infection and shortens nothing.",
  "High fever, facial swelling, or symptoms beyond ten days bypass the ritual for professional care.",
 ],
 "requirements": [
  "Reader must recite the ritual sequence with the safe-water rule embedded.",
  "Reader must explain the sequencing logic honestly.",
  "Reader must state the bypass conditions for professional care.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "FDA guidance on safe water for nasal rinsing (referenced).",
 ],
},
{
 "key": "sig-sun-aftercare",
 "name": "The Signature Sun-Aftercare Ritual",
 "group": "minor-ailments",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "description": ("Signature original: his Sun-Aftercare Ritual companions "
  "the public aloe record with a complete mild-sunburn response in "
  "Signature form. The ritual: get out of the sun first (the step people "
  "skip), cool the skin with cool water second, plain aloe gel on intact "
  "mildly burned skin third, fluids and shade for the rest of the day "
  "fourth, and a protection vow fifth - the burn becomes the teacher that "
  "installs tomorrow's sun-protection habit. The severity gate is built "
  "in: large-area blistering, fever, chills, or heat-illness signs bypass "
  "the ritual for professional care. Clearly labeled Signature-made, "
  "educational information only, not medical advice."),
 "how_it_works": ("The ritual works through completeness and conversion: "
  "completeness, because mild sunburn care fails when steps are skipped "
  "(especially leaving the sun); conversion, because the fifth step turns "
  "the painful lesson into a durable protection habit, which the record "
  "presents as the ritual's real product. The mechanism section is "
  "honest: cooling and aloe comfort the skin, fluids replace losses, and "
  "nothing in the ritual undoes UV damage already done - prevention is "
  "the documented strategy, referenced from this database's sun-protection "
  "record. The demo grades sunburn scenarios and routes severe cases past "
  "the ritual to professional care."),
 "key_points": [
  "Signature original: five steps - exit the sun, cool, aloe, fluids and shade, the protection vow.",
  "The severity gate is built in; serious burns bypass the ritual for professional care.",
  "The fifth step converts the painful lesson into a durable protection habit.",
  "Honest boundary: comforts the burn, undoes no UV damage; prevention is the documented strategy.",
  "Clearly labeled Signature-made; educational information only, not medical advice.",
 ],
 "requirements": [
  "Reader must recite the five steps in order.",
  "Reader must state the severity gate conditions.",
  "Reader must explain the conversion logic of the fifth step.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "American Academy of Dermatology sun-protection guidance (referenced).",
 ],
},
{
 "key": "sig-sprain-support",
 "name": "The Signature Sprain-Support Protocol",
 "group": "minor-ailments",
 "ladder_rank": 12, "ladder_tier": "foundations",
 "description": ("Signature original: his Sprain-Support Protocol gives "
  "the public RICE record a Signature memory structure - P-R-O-T-E-C-T: "
  "Pause (stop using it), Rest (the injured part), Observe (swelling, "
  "color, function, and the fracture red flags), Treat with cold (wrapped, "
  "timed), Elevate (above heart level), Compress (snug, never numbing), "
  "Track (recheck through the coming days). The fracture branch - "
  "inability to bear weight, deformity, numbness, worsening swelling - "
  "routes to professional evaluation before the protocol continues. The "
  "protocol organizes documented first aid; it diagnoses nothing. Clearly "
  "labeled Signature-made, educational information only, not medical "
  "advice."),
 "how_it_works": ("The protocol works as an extended mnemonic that adds "
  "the two steps home care usually forgets: Observe (the deliberate "
  "assessment that catches fractures masquerading as sprains) and Track "
  "(the multi-day recheck that catches the worsening case). The "
  "compression safety check - digits warm and pink - is embedded in the "
  "C step as a gate. The record is honest that PROTECT is a memory aid "
  "for documented first aid, and that the Observe step is the protocol's "
  "most valuable contribution. The demo walks sample sprain scenarios "
  "through PROTECT and routes fracture-flag cases to professional care."),
 "key_points": [
  "Signature original mnemonic: P-R-O-T-E-C-T with Observe and Track as the added steps.",
  "Observe catches fractures masquerading as sprains; Track catches the worsening case.",
  "Compression gate: digits warm and pink, or rewrap looser.",
  "Fracture branch routes to professional evaluation before the protocol continues.",
  "A memory aid for documented first aid; diagnoses nothing.",
 ],
 "requirements": [
  "Reader must recite PROTECT with each step's content.",
  "Reader must explain why Observe and Track were added.",
  "Reader must state the fracture red flags and the routing rule.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "National Athletic Trainers Association sprain-management guidance (referenced).",
 ],
},
{
 "key": "sig-wound-watch",
 "name": "The Signature Wound-Watch Protocol",
 "group": "injury-and-recovery-care",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "description": ("Signature original: his Wound-Watch Protocol companions "
  "the public soap-and-water record with a calm-sequence framework for "
  "minor cuts and scrapes. The protocol: Clean hands first, Irrigate with "
  "clean running water, Soap the surrounding skin gently, Pat dry with "
  "clean gauze, Observe and decide (minor and shallow continues to home "
  "care; deep, gaping, dirty, bite, puncture, or nonstop bleeding routes "
  "to professional care), then Watch the healing days for infection signs. "
  "The protocol repeats the public record's honest correction - no "
  "peroxide, no alcohol on the wound - as a named rule: the Sting Means "
  "Harm rule. Clearly labeled Signature-made, educational information "
  "only, not medical advice."),
 "how_it_works": ("The protocol works by making the unglamorous steps "
  "unskippable: hand washing and the observe-and-decide gate are the steps "
  "home wound care usually skips, and the protocol puts them in the name. "
  "The Sting Means Harm rule gives readers a one-line reason to abandon "
  "the peroxide ritual. The Watch phase teaches the infection-sign "
  "checklist (increasing redness, warmth, swelling, pus, red streaks, "
  "fever) as a daily 10-second scan. The record is honest that the "
  "protocol organizes documented wound care; its contribution is sequence "
  "discipline. The demo runs sample wounds through the decide gate and "
  "classifies each as home-care or professional-care."),
 "key_points": [
  "Signature original sequence with the decide gate built in: minor continues, serious routes out.",
  "The Sting Means Harm rule retires the peroxide ritual with a memorable line.",
  "Hand washing and the decide gate are the usually-skipped steps the protocol protects.",
  "The Watch phase: a daily 10-second infection-sign scan during healing.",
  "Organizes documented wound care; contributes sequence discipline.",
 ],
 "requirements": [
  "Reader must recite the protocol steps including the decide gate.",
  "Reader must explain the Sting Means Harm rule.",
  "Reader must list the infection signs watched for during healing.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Cochrane review on water for wound cleansing (referenced principle).",
 ],
},
{
 "key": "sig-dressing-rite",
 "name": "The Signature Dressing-Change Rite",
 "group": "injury-and-recovery-care",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "description": ("Signature original: his Dressing-Change Rite turns the "
  "public moist-wound record into a small ceremony of care. The rite: "
  "wash hands, remove the old covering gently (warm water loosens stuck "
  "edges - never rip), observe the wound honestly, thin layer of plain "
  "petroleum jelly, fresh covering, and the daily vow - changed daily or "
  "sooner if wet or dirty, without exception. The rite's honest teaching "
  "is that consistency heals: the moist-covered principle only works when "
  "the covering discipline holds. For clean minor wounds only; anything "
  "deep, gaping, or showing infection signs belongs to professional care. "
  "Clearly labeled Signature-made, educational information only."),
 "how_it_works": ("The rite works through ritualized consistency: naming "
  "the steps and performing them the same way each day removes the "
  "decision fatigue that lets dressings go unchanged. The observe step is "
  "the rite's diagnostic moment - the daily look that catches infection "
  "early - and the record teaches what healthy healing looks like versus "
  "the warning signs. The petroleum-jelly mechanism is stated honestly: a "
  "moisture barrier that keeps the covering from sticking to new tissue, "
  "with no antibiotic action. The demo builds a dressing-change schedule "
  "and verifies every interval meets the daily-or-sooner rule."),
 "key_points": [
  "Signature original: a six-step rite with the daily vow - changed daily or sooner, no exceptions.",
  "Ritualized consistency removes the decision fatigue that lets dressings go unchanged.",
  "The observe step is the diagnostic moment that catches infection early.",
  "Petroleum jelly honestly described: moisture barrier, no antibiotic action.",
  "Clean minor wounds only; deep, gaping, or infected wounds go to professional care.",
 ],
 "requirements": [
  "Reader must recite the six rite steps.",
  "Reader must explain the consistency mechanism honestly.",
  "Reader must distinguish healthy healing appearance from warning signs.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Winter 1962 on moist wound healing; AAD petroleum-jelly guidance (referenced).",
 ],
},
{
 "key": "sig-soak-sanctuary",
 "name": "The Signature Soak Sanctuary",
 "group": "injury-and-recovery-care",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "description": ("Signature original: his Soak Sanctuary framework takes "
  "the public Epsom-salt record and builds the restful container around "
  "it. The sanctuary has four walls: the water wall (comfortably warm, "
  "tested with the wrist, never hot), the time wall (a bounded soak "
  "window, then out), the mind wall (no screens - the soak is rest, not "
  "entertainment time), and the honesty wall (the relief comes from heat "
  "and rest; magnesium-absorption claims are not established, and the "
  "framework says so on its own walls). Diabetes and circulation cautions "
  "are built into the water wall. Clearly labeled Signature-made, "
  "educational information only, not medical advice."),
 "how_it_works": ("The sanctuary works by protecting the rest inside the "
  "soak: the time wall prevents the prune-and-chill overshoot, the mind "
  "wall converts bath time into genuine nervous-system rest, and the "
  "honesty wall keeps the framework trustworthy by refusing the unproven "
  "claim. The record presents the honesty wall as the Signature "
  "contribution - a wellness framework that polices its own claims. "
  "Muscle pain with weakness, numbness, dark urine, or worsening pain "
  "bypasses the sanctuary for professional evaluation. The demo audits "
  "sample soak plans against the four walls."),
 "key_points": [
  "Signature original: four walls - water, time, mind, honesty - around the traditional soak.",
  "The honesty wall refuses the unproven magnesium-absorption claim inside the framework itself.",
  "The mind wall (no screens) converts bath time into genuine rest.",
  "Diabetes and circulation cautions built into the water wall.",
  "Weakness, numbness, dark urine, or worsening muscle pain bypass the sanctuary for professional care.",
 ],
 "requirements": [
  "Reader must name the four walls and their rules.",
  "Reader must explain the honesty wall's function.",
  "Reader must state the muscle-injury red flags.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Musculoskeletal self-care guidance on warm-water comfort (referenced).",
 ],
},
{
 "key": "sig-golden-kitchen",
 "name": "The Signature Golden Kitchen Practice",
 "group": "injury-and-recovery-care",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "description": ("Signature original: his Golden Kitchen Practice takes "
  "the public turmeric record's honest lane - turmeric as wholesome "
  "cooking tradition - and builds a Signature kitchen ritual on it. The "
  "practice: turmeric used as a regular cooking spice in everyday meals, "
  "paired with the honest statement spoken in the kitchen - \"tradition "
  "on the tongue, humility in the claim.\" The practice explicitly "
  "excludes the supplement lane: concentrated curcumin products and their "
  "strong claims are directed to professional guidance, not to the home "
  "kitchen. Blood-thinner, gallbladder, and pre-surgery cautions are "
  "repeated from the public record. Clearly labeled Signature-made, "
  "educational information only."),
 "how_it_works": ("The practice works through culinary integration: "
  "turmeric becomes an everyday ingredient rather than a medicine ritual, "
  "which the record presents as the honest relationship to a traditional "
  "spice with limited clinical evidence. The spoken honesty line is the "
  "Signature mechanism - a verbal commitment device that keeps the "
  "kitchen's claims aligned with the evidence. The record teaches the "
  "bioavailability reality in one plain sentence so readers understand why "
  "the kitchen lane, not the cure lane, is the framework's home. The demo "
  "classifies turmeric statements as kitchen-honest or claim-overrun."),
 "key_points": [
  "Signature original: turmeric as everyday cooking spice, not as medicine ritual.",
  "The spoken honesty line - tradition on the tongue, humility in the claim - is the commitment device.",
  "The supplement lane is explicitly excluded; concentrated products go to professional guidance.",
  "Bioavailability reality taught in one plain sentence.",
  "Blood-thinner, gallbladder, and pre-surgery cautions repeated from the public record.",
 ],
 "requirements": [
  "Reader must explain the kitchen-lane versus cure-lane distinction (the cure lane is not established).",
  "Reader must state the bioavailability reality plainly.",
  "Reader must repeat the medication and surgery cautions.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Anand et al. 2007 on curcumin bioavailability; NCCIH turmeric summary (referenced).",
 ],
},
{
 "key": "sig-head-ease",
 "name": "The Signature Head-Ease Ritual",
 "group": "injury-and-recovery-care",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "description": ("Signature original: his Head-Ease Ritual companions the "
  "public peppermint record with a full tension-headache response in "
  "Signature form. The ritual: pause and assess (tension pattern versus "
  "red flags - sudden severe onset, post-injury, or neurological symptoms "
  "route to emergency care first), hydrate, dim the glare, diluted "
  "peppermint on forehead and temples with eyes protected, then quiet "
  "rest. The dilution and eye-avoidance rules are choreographed into the "
  "steps, and the record is honest that the ritual organizes documented "
  "comfort measures - it treats no headache disorder. A simple headache "
  "diary habit is included to separate tension patterns from migraine "
  "patterns needing professional diagnosis. Clearly labeled "
  "Signature-made, educational information only."),
 "how_it_works": ("The ritual works through layered calming: hydration "
  "addresses a common headache contributor, glare reduction removes a "
  "trigger, the cooling peppermint sensation provides the studied comfort "
  "signal, and quiet rest lets the episode pass. The assess-first "
  "choreography is the safety contribution - the ritual cannot be "
  "performed without passing the red-flag gate. The diary habit is the "
  "long-term contribution: pattern recognition that directs migraine-like "
  "patterns to professional diagnosis instead of repeated self-treatment. "
  "The demo routes sample headache scenarios through the assess gate and "
  "scores diary entries by pattern."),
 "key_points": [
  "Signature original: assess, hydrate, dim glare, diluted peppermint, quiet rest.",
  "The red-flag gate is choreographed first - the ritual cannot proceed without passing it.",
  "Dilution and eye-avoidance rules embedded in the steps, not appended as warnings.",
  "The headache diary habit separates tension patterns from migraine patterns needing diagnosis.",
  "Organizes documented comfort measures; treats no headache disorder.",
 ],
 "requirements": [
  "Reader must recite the ritual with the assess gate first.",
  "Reader must state the dilution and eye-avoidance rules.",
  "Reader must explain the diary's pattern-recognition purpose.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Gobel et al. trials of peppermint oil in tension-type headache (referenced).",
 ],
},
{
 "key": "sig-steam-sanctuary",
 "name": "The Signature Steam Sanctuary",
 "group": "injury-and-recovery-care",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "description": ("Signature original: his Steam Sanctuary takes the public "
  "steam record's harm-reduction teaching and builds the Signature version "
  "around the safest method. The sanctuary rule is one line: the shower "
  "is the sanctuary - warm moist air breathed in a hot shower, with no "
  "bowl of scalding water anywhere in the ritual. For readers who insist "
  "on the bowl method, the framework imposes the full safety liturgy - "
  "stable surface, safe distance, supervised children at arm's length or "
  "excluded, never unattended - and names the scald cases from medical "
  "literature as the reason. The benefit is honestly labeled subjective "
  "soothing. Clearly labeled Signature-made, educational information only."),
 "how_it_works": ("The sanctuary works by removing the hazard rather than "
  "managing it: the shower method delivers the traditional warm-moist-air "
  "comfort with the burn risk designed out, which the record presents as "
  "the Signature design principle - engineer the danger away before "
  "warning about it. The bowl-method liturgy exists as harm reduction for "
  "the stubborn, with each rule traceable to the documented scald hazard. "
  "The record closes the loop to professional care for high fever, facial "
  "swelling, or prolonged congestion. The demo audits sample steam "
  "routines and recommends the shower method wherever bowl risk appears."),
 "key_points": [
  "Signature original: the shower is the sanctuary - the burn risk designed out, not managed.",
  "Design principle stated plainly: engineer the danger away before warning about it.",
  "Bowl-method safety liturgy exists as harm reduction, each rule traced to the scald hazard.",
  "Benefit honestly labeled subjective soothing, not established treatment.",
  "High fever, facial swelling, or prolonged congestion route to professional care.",
 ],
 "requirements": [
  "Reader must state the one-line sanctuary rule.",
  "Reader must explain the design principle in plain language.",
  "Reader must recite the bowl-method liturgy for harm-reduction contexts.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Burn-injury case literature on steam-inhalation scalds (referenced).",
 ],
},
{
 "key": "sig-rehydrate-rite",
 "name": "The Signature Rehydration Rite",
 "group": "injury-and-recovery-care",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "description": ("Signature original: his Rehydration Rite companions the "
  "public oral-rehydration record with a memorable response framework for "
  "fluid-loss situations. The rite: Spot the signs (the mild-to-severe "
  "ladder), Sip small and often (never large gulps when nauseated), Seek "
  "the real solution (commercial ORS or professional guidance - the rite "
  "gives no home recipe, repeating the public record's ratio warning), "
  "and Surrender to care (severe signs end the rite and start urgent "
  "care). The four S's make the dehydration response recallable under "
  "stress, which is when recall matters. Clearly labeled Signature-made, "
  "educational information only, not medical advice."),
 "how_it_works": ("The rite works as a stress-proof mnemonic: four S's in "
  "order, each a gate. Spot classifies severity and can end the rite at "
  "urgent care immediately. Sip governs the technique. Seek directs to "
  "proper ORS rather than improvised mixtures, with the ratio-danger "
  "reasoning repeated so readers understand the rule. Surrender is the "
  "explicit permission to stop home care - the rite names surrender as "
  "wisdom, not failure. The record is honest that the rite organizes "
  "documented rehydration science; its contribution is recall under "
  "pressure. The demo classifies dehydration scenarios through the four "
  "S's."),
 "key_points": [
  "Signature original: four S's - Spot, Sip, Seek, Surrender - recallable under stress.",
  "No home ORS recipe; the ratio-danger reasoning is repeated inside the rite.",
  "Surrender names stopping home care as wisdom, not failure.",
  "Spot can end the rite at urgent care immediately - severity gates the sequence.",
  "Organizes documented rehydration science; contributes recall under pressure.",
 ],
 "requirements": [
  "Reader must recite the four S's with each gate's content.",
  "Reader must explain why no home recipe is given.",
  "Reader must list the severe signs that trigger Surrender.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "WHO oral rehydration guidance (referenced principle).",
 ],
},
{
 "key": "sig-cycle-comfort",
 "name": "The Signature Cycle-Comfort Framework",
 "group": "injury-and-recovery-care",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "description": ("Signature original: his Cycle-Comfort Framework "
  "companions the public heat-therapy record with a complete menstrual-"
  "comfort practice. The framework: track the cycle (prediction beats "
  "surprise), prepare the comfort kit (heat source, rest space, fluids), "
  "apply heat early at the first sign of cramps, rest without apology, "
  "and know the line - severe, worsening, life-disrupting, or new-pattern "
  "pain goes to professional evaluation, never to silent endurance. The "
  "framework's Signature statement is that pain that disrupts life is "
  "information demanding investigation, not a burden to be carried "
  "quietly. Burn precautions are choreographed into the heat step. "
  "Clearly labeled Signature-made, educational information only."),
 "how_it_works": ("The framework works through preparation and "
  "permission: tracking converts surprise into readiness, the prepared "
  "kit removes friction at the painful moment, early heat application "
  "catches cramps before they peak, and the permission structure counters "
  "the cultural training to endure silently. The know-the-line gate is "
  "the framework's medical contribution - explicit criteria for "
  "professional evaluation that many sufferers never receive. The record "
  "is honest that the framework organizes documented comfort measures; it "
  "treats no underlying condition. The demo builds a cycle-comfort plan "
  "and checks the evaluation gate against sample pain histories."),
 "key_points": [
  "Signature original: track, prepare, heat early, rest without apology, know the line.",
  "Preparation converts surprise into readiness; the kit removes friction at the painful moment.",
  "The Signature statement: life-disrupting pain is information demanding investigation.",
  "Know-the-line gate gives explicit criteria for professional evaluation.",
  "Burn precautions choreographed into the heat step; treats no underlying condition.",
 ],
 "requirements": [
  "Reader must list the five framework elements.",
  "Reader must explain the preparation mechanism.",
  "Reader must state the evaluation-gate criteria.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Cochrane-linked literature on heat therapy for dysmenorrhea (referenced).",
 ],
},
{
 "key": "sig-calm-scent",
 "name": "The Signature Calm-Scent Practice",
 "group": "injury-and-recovery-care",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "description": ("Signature original: his Calm-Scent Practice takes the "
  "public lavender record's honest mechanism - scent as a conditioned "
  "calm cue - and builds a Signature conditioning protocol. The protocol: "
  "choose one consistent scent, pair it deliberately with an existing "
  "calming routine for two weeks, then use the scent alone as the cue "
  "that calls up the calm state. The record is explicit that this is "
  "classical conditioning, honestly labeled, with modest evidence behind "
  "the scent itself. Essential-oil safety rules are built into the "
  "selection step: away from eyes, diluted for skin, away from small "
  "children and pets, never ingested. Persistent anxiety or panic goes to "
  "professional care. Clearly labeled Signature-made, educational "
  "information only."),
 "how_it_works": ("The practice works through deliberate conditioning: "
  "the two-week pairing phase builds the association, the cue phase tests "
  "it, and the record teaches readers to evaluate honestly whether the "
  "cue works for them - the framework includes its own reality check. "
  "The Signature contribution is the protocol structure: a defined "
  "pairing period, a defined test, and permission to conclude the scent "
  "is simply pleasant rather than powerful. The safety rules are "
  "prerequisites, not footnotes. The demo scores a sample conditioning "
  "plan for protocol completeness."),
 "key_points": [
  "Signature original: a two-week deliberate conditioning protocol with a defined test phase.",
  "The mechanism is classical conditioning, honestly labeled as such.",
  "Includes its own reality check: permission to conclude the scent is simply pleasant.",
  "Essential-oil safety rules are prerequisites built into selection.",
  "Persistent anxiety or panic goes to professional care, not to stronger scents.",
 ],
 "requirements": [
  "Reader must describe the pairing phase and the test phase.",
  "Reader must explain the conditioning mechanism honestly.",
  "Reader must recite the essential-oil safety rules.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Koulivand et al. 2013 on lavender and the nervous system (referenced).",
 ],
},
{
 "key": "sig-evidence-compass",
 "name": "The Signature Evidence Compass",
 "group": "injury-and-recovery-care",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "description": ("Signature original: his Evidence Compass is the "
  "Signature companion to this database's evidence-literacy record - a "
  "pocket tool for judging any remedy claim in under a minute. The "
  "compass has four points: North - what tier of evidence (trial, "
  "tradition, anecdote, marketing)? East - who benefits if I believe "
  "this? South - what is the harm if it is wrong? West - what would "
  "change my mind? The framework's Signature line is that a claim which "
  "cannot survive its own compass was never a claim worth carrying. The "
  "compass is applied to this database's own records as the demonstration, "
  "including the Signature records themselves. Clearly labeled "
  "Signature-made, educational information only."),
 "how_it_works": ("The compass works as a portable skepticism ritual: four "
  "questions asked in order, every time, until they become reflex. North "
  "places the claim on the evidence hierarchy; East surfaces conflicts of "
  "interest; South prices the downside (with health claims, the downside "
  "is often delayed real care); West tests falsifiability, the mark of an "
  "honest claim. The record demonstrates the compass on three sample "
  "claims - one documented, one traditional, one marketing - showing the "
  "different verdicts. The demo grades sample claims through the four "
  "points and reports the verdict."),
 "key_points": [
  "Signature original: four compass points - evidence tier, beneficiary, harm if wrong, what would change my mind.",
  "A portable skepticism ritual; the four questions become reflex with practice.",
  "South (harm if wrong) prices the real downside: often delayed real care.",
  "Demonstrated on this database's own records, Signature ones included.",
  "A claim that cannot survive its own compass was never worth carrying.",
 ],
 "requirements": [
  "Reader must recite the four compass points.",
  "Reader must run the compass on a sample claim.",
  "Reader must explain why the compass is applied to Signature records too.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Evidence-based medicine hierarchy literature (referenced framework).",
 ],
},
{
 "key": "sig-honest-supplement",
 "name": "The Signature Honest Supplement Ledger",
 "group": "injury-and-recovery-care",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "description": ("Signature original: his Honest Supplement Ledger is the "
  "Signature companion to the public vitamin C record - a personal "
  "accounting framework for anyone considering supplements. The ledger "
  "asks four questions per product: what is the specific claim, what "
  "tier of evidence supports it, what does it cost per year, and what "
  "would I spend that money on instead? The framework's honest premise is "
  "that most supplement spending buys expensive reassurance, and the "
  "ledger makes the trade visible. It neither endorses nor forbids "
  "supplements; it prices them. Anyone with medical conditions or on "
  "medication is directed to professional guidance before adding "
  "supplements. Clearly labeled Signature-made, educational information "
  "only."),
 "how_it_works": ("The ledger works through opportunity-cost visibility: "
  "writing the annual cost beside the evidence tier lets readers see what "
  "their reassurance budget actually buys, and the instead-question "
  "redirects the budget toward documented wellness (better food, a walking "
  "shoe fund, sleep-hygiene improvements). The record teaches the "
  "evidence-tier placement honestly - most products land on tradition or "
  "marketing, a few on modest trial support - and the interaction warning: "
  "supplements are pharmacologically active until proven otherwise. The "
  "demo audits a sample supplement shelf through the ledger and reports "
  "the annual reassurance budget."),
 "key_points": [
  "Signature original: four ledger questions per product - claim, evidence tier, annual cost, instead-what.",
  "Makes the supplement trade visible through opportunity-cost accounting.",
  "Neither endorses nor forbids; it prices.",
  "Supplements are pharmacologically active until proven otherwise - interaction caution.",
  "Medical conditions or medications: professional guidance before adding supplements.",
 ],
 "requirements": [
  "Reader must run the ledger on a sample product.",
  "Reader must explain the opportunity-cost mechanism.",
  "Reader must state the interaction caution and the professional-guidance routing.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "NIH Office of Dietary Supplements guidance (referenced).",
 ],
},
{
 "key": "sig-tradition-bridge",
 "name": "The Signature Tradition Bridge",
 "group": "injury-and-recovery-care",
 "ladder_rank": 24, "ladder_tier": "compounded",
 "description": ("Signature original: his Tradition Bridge is the "
  "Signature companion to the public arnica record - a framework for "
  "honoring traditional remedies without surrendering evidence honesty. "
  "The bridge has two spans: the respect span (traditional practices "
  "carry cultural wisdom, comfort, and identity - real human goods) and "
  "the evidence span (efficacy claims still need efficacy evidence, and "
  "popularity is not proof). The framework's Signature line is that a "
  "tradition can be loved and limited at the same time. It teaches the "
  "practical rule: enjoy traditional remedies as tradition, evaluate them "
  "as medicine, and never let tradition delay professional care for real "
  "injury or illness. Clearly labeled Signature-made, educational "
  "information only."),
 "how_it_works": ("The bridge works by refusing the false choice between "
  "dismissing tradition and believing everything: the two spans let "
  "readers hold both truths - the practice matters culturally and the "
  "claim needs evidence. The record demonstrates the bridge on arnica, "
  "on the Epsom magnesium story, and on a beloved family remedy, showing "
  "the different verdicts each span delivers. The safety teaching is the "
  "delay rule: tradition earns patience, but symptoms with red flags earn "
  "professional care on schedule regardless of tradition. The demo runs "
  "sample traditional claims across the two spans and reports both "
  "verdicts."),
 "key_points": [
  "Signature original: two spans - respect for tradition's human goods, evidence for its medical claims.",
  "Refuses the false choice between dismissing tradition and believing everything.",
  "A tradition can be loved and limited at the same time.",
  "Practical rule: enjoy as tradition, evaluate as medicine.",
  "The delay rule: red-flag symptoms get professional care on schedule regardless of tradition.",
 ],
 "requirements": [
  "Reader must explain both spans with an example.",
  "Reader must state the loved-and-limited line in their own words.",
  "Reader must recite the delay rule.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "NCCIH guidance on evaluating traditional and complementary practices (referenced).",
 ],
},
{
 "key": "sig-sleep-sanctuary",
 "name": "The Signature Sleep Sanctuary",
 "group": "wellness-practices",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "description": ("Signature original: his Sleep Sanctuary framework takes "
  "the public sleep-hygiene record and builds the bedroom as a named "
  "place. The sanctuary has five furnishings: the dark (blackout or "
  "eye mask), the cool (a cool room beats a warm one), the quiet (ear "
  "protection or steady background sound), the clean (a bed reserved for "
  "sleep, not for work screens), and the consistent (the same sleep and "
  "wake times, weekends included). The framework's Signature teaching is "
  "that the bedroom is a temple with one god - sleep - and every object "
  "in it either serves or steals. Chronic insomnia, breathing pauses, or "
  "severe daytime sleepiness bypass the sanctuary for professional "
  "evaluation. Clearly labeled Signature-made, educational information "
  "only, not medical advice."),
 "how_it_works": ("The sanctuary works through environmental design: each "
  "furnishing removes one documented sleep enemy, and the naming makes "
  "the bedroom's purpose legible to everyone in the household. The "
  "consistency furnishing is the load-bearing wall - the record is honest "
  "that irregular timing undermines the other four. The framework "
  "includes a two-week furnishing plan (one furnishing per few days) so "
  "the sanctuary is built gradually rather than attempted overnight. The "
  "demo audits sample bedrooms against the five furnishings and reports "
  "the gaps in build order."),
 "key_points": [
  "Signature original: five furnishings - dark, cool, quiet, clean, consistent.",
  "The bedroom as a temple with one god: every object serves sleep or steals it.",
  "Consistency is the load-bearing wall; irregular timing undermines the rest.",
  "Built over two weeks, one furnishing at a time - gradual, not overnight.",
  "Chronic insomnia, breathing pauses, or severe daytime sleepiness go to professional evaluation.",
 ],
 "requirements": [
  "Reader must name the five furnishings.",
  "Reader must explain why consistency is load-bearing.",
  "Reader must state the sleep-disorder bypass conditions.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "American Academy of Sleep Medicine healthy-sleep-habits guidance (referenced).",
 ],
},
{
 "key": "sig-breathing-ladder",
 "name": "The Signature Breathing Ladder",
 "group": "wellness-practices",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "description": ("Signature original: his Breathing Ladder takes the "
  "public slow-breathing record and arranges it as a climbable skill "
  "ladder. Rung one: notice the breath for one minute, no control. Rung "
  "two: slow the exhale slightly for two minutes. Rung three: the "
  "extended-exhale pattern (in four, out six to eight) for five minutes. "
  "Rung four: box breathing for five minutes. Rung five: the pattern "
  "deployed in a real stressful moment. The ladder's rule is one rung at "
  "a time - mastery of each rung before the next - because the record is "
  "honest that calm is trained progressively, not summoned on demand. "
  "Anyone with breathing difficulties practices gently and consults a "
  "professional about underlying conditions. Clearly labeled "
  "Signature-made, educational information only."),
 "how_it_works": ("The ladder works through progressive skill acquisition: "
  "each rung is small enough to succeed at, and the success builds the "
  "self-efficacy that makes the next rung attemptable. The record teaches "
  "the honest mechanism at each rung - attention regulation, then "
  "parasympathetic signaling through extended exhales - without "
  "mysticism. Rung five is the transfer test: using the trained pattern "
  "when it counts, which the record presents as the entire point of the "
  "first four rungs. The demo verifies sample practice plans follow the "
  "one-rung-at-a-time rule and computes the timing math for each pattern."),
 "key_points": [
  "Signature original: five rungs from noticing the breath to deploying calm under stress.",
  "One rung at a time; mastery before ascent - calm is trained, not summoned.",
  "Each rung small enough to succeed at; success builds the next rung's attemptability.",
  "Honest mechanisms at each rung; no mysticism.",
  "Breathing difficulties: practice gently, professional guidance for underlying conditions.",
 ],
 "requirements": [
  "Reader must climb the rungs in order with correct patterns.",
  "Reader must explain the progressive-training logic.",
  "Reader must state the transfer test that is rung five's purpose.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Zaccaro et al. 2018 systematic review on slow breathing (referenced).",
 ],
},
{
 "key": "sig-walking-meditation",
 "name": "The Signature Walking Meditation",
 "group": "wellness-practices",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "description": ("Signature original: his Walking Meditation fuses the "
  "public gentle-walking record with attention training. The practice: a "
  "comfortable flat route, a conversational pace, and the attention "
  "anchor - breath, footfall, or the passing environment, returned to "
  "gently each time the mind wanders. The framework's honest claim is "
  "modest: walking delivers the documented physical benefits while the "
  "attention anchor trains the noticing muscle, and the combination is "
  "more restorative than either alone for many people. It claims no "
  "spiritual attainment and no medical treatment. Chest pain, severe "
  "breathlessness, or dizziness with exertion stop the walk and seek "
  "care. Clearly labeled Signature-made, educational information only."),
 "how_it_works": ("The practice works through dual training: the body "
  "gets the graded movement the public record documents, while the mind "
  "gets repetitions of noticing-and-returning - the fundamental attention "
  "repetition. The record teaches the wandering protocol honestly: the "
  "mind will wander, the return is the rep, and frustration is just "
  "another wandering to return from. Session structure is simple - five "
  "minutes of settling, the main walk with the anchor, five minutes of "
  "open noticing - and progression follows the public record's graded "
  "principle. The demo builds a four-week walking-meditation plan and "
  "verifies gradual progression."),
 "key_points": [
  "Signature original: graded walking fused with an attention anchor - breath, footfall, or environment.",
  "The return is the rep: mind wanders, attention returns, the noticing muscle trains.",
  "Modest honest claim: more restorative than either alone for many people; no spiritual or medical claims.",
  "Session structure: settle, anchor, open noticing.",
  "Exertion red flags stop the walk: chest pain, severe breathlessness, dizziness.",
 ],
 "requirements": [
  "Reader must describe the wandering protocol.",
  "Reader must explain the dual-training logic honestly.",
  "Reader must state the exertion stop signals.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "CDC physical activity guidance on walking (referenced).",
 ],
},
{
 "key": "sig-gut-kindness",
 "name": "The Signature Gut-Kindness Kitchen",
 "group": "wellness-practices",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "description": ("Signature original: his Gut-Kindness Kitchen takes the "
  "public fermented-foods record's honest lesson - strain-specificity, "
  "pattern over product - and builds a Signature kitchen practice. The "
  "practice: weekly fermented-food variety (a different traditional "
  "fermented food across the week), fiber-rich plant foundations at every "
  "meal, and the label-honesty habit (live cultures versus heat-treated, "
  "claims versus evidence). The framework's Signature line is that the "
  "kitchen feeds the gut's ecosystem, not its marketing department. It "
  "claims no treatment of digestive disease; severe or persistent "
  "digestive symptoms go to professional evaluation. Compromised immunity: "
  "professional guidance on live-culture products. Clearly labeled "
  "Signature-made, educational information only."),
 "how_it_works": ("The kitchen works through pattern and variety: the "
  "documented gut benefit lives in the overall fiber-rich, plant-rich "
  "pattern, and the fermented variety adds traditional dietary diversity "
  "without depending on any single product's claims. The label-honesty "
  "habit is the skepticism contribution - readers learn to read culture "
  "labels the way the public record teaches. The record is explicit that "
  "the practice is dietary tradition organized well, not therapy. The "
  "demo scores a sample week for fermented variety and plant-pattern "
  "elements."),
 "key_points": [
  "Signature original: weekly fermented variety on fiber-rich plant foundations, plus label honesty.",
  "Feeds the gut's ecosystem, not its marketing department.",
  "The documented benefit lives in the overall pattern, not in single products.",
  "Dietary tradition organized well; not therapy, treats no digestive disease.",
  "Severe or persistent digestive symptoms go to professional evaluation.",
 ],
 "requirements": [
  "Reader must describe the weekly variety practice.",
  "Reader must explain the pattern-over-product lesson.",
  "Reader must state the digestive red flags and the immunity caution.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "NCCIH probiotics summary on strain-specific effects (referenced).",
 ],
},
{
 "key": "sig-red-flag-ledger",
 "name": "The Signature Red-Flag Ledger",
 "group": "wellness-practices",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "description": ("Signature original: his Red-Flag Ledger is the Signature "
  "companion to this database's most important public record - a personal, "
  "household-ready version of the red-flag framework. The ledger is a "
  "single page kept where the home kit lives: the emergency tier symptoms "
  "in red (chest pain, breathing difficulty, stroke signs, sudden severe "
  "headache, major bleeding), the urgent tier in amber (persistent fever, "
  "severe pain, dehydration signs, bites, worsening symptoms), and the "
  "household's escalation plan (emergency number, poison control, clinic "
  "contact, each member's conditions and medications). The framework's "
  "Signature line is that courage is calling early - the ledger removes "
  "the midnight decision fatigue that delays care. Clearly labeled "
  "Signature-made, educational information only."),
 "how_it_works": ("The ledger works through pre-decision: the hard "
  "choices - when to call, who to call, what to say - are made on a calm "
  "afternoon instead of a frightening night. The record teaches the "
  "household drill: fill the page together, post it with the kit, review "
  "it when the kit's expiry is checked. The special-populations rule is "
  "written on the page: infants, older adults, pregnant people, and the "
  "immunocompromised escalate earlier. The demo audits sample ledger pages "
  "for tier completeness and escalation-plan presence."),
 "key_points": [
  "Signature original: a single household page - red tier, amber tier, escalation plan.",
  "Pre-decision removes the midnight decision fatigue that delays care.",
  "Courage is calling early: the framework's Signature line.",
  "Posted with the home kit; reviewed at each expiry check.",
  "Special populations escalate earlier - written on the page itself.",
 ],
 "requirements": [
  "Reader must produce a complete ledger page from memory.",
  "Reader must explain the pre-decision mechanism.",
  "Reader must list the emergency-tier symptoms without hesitation.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Mainstream emergency-triage guidance on red-flag symptoms (referenced).",
 ],
},
{
 "key": "sig-claim-reader",
 "name": "The Signature Claim-Reader Method",
 "group": "wellness-practices",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "description": ("Signature original: his Claim-Reader Method is the "
  "Signature companion to this database's evidence-literacy record - a "
  "five-second label drill for the supplement aisle and the remedy "
  "internet. The drill: read the claim, name the evidence tier it "
  "actually rests on, find the weasel word (supports, boosts, may help - "
  "the vocabulary of unproven claims), check for the disease-treatment "
  "implication the label legally avoids stating, and ask the compass "
  "question - what would change my mind? The method's Signature line is "
  "that the label tells the truth in the fine print and the lie in the "
  "headline - the drill teaches reading the fine print first. Clearly "
  "labeled Signature-made, educational information only."),
 "how_it_works": ("The method works as a reflex drill: five steps in "
  "order, practiced on real labels until automatic. The weasel-word "
  "vocabulary lesson is the pattern-recognition core - once readers see "
  "the hedge words, they cannot unsee them. The disease-implication check "
  "teaches the regulatory reality: structure-function claims are legal "
  "precisely because they avoid disease claims, which tells the reader "
  "exactly how much is proven. The record demonstrates the drill on three "
  "real-style labels. The demo runs sample claims through the drill and "
  "names the weasel words."),
 "key_points": [
  "Signature original: a five-step label drill - claim, tier, weasel words, implication, what-would-change-my-mind.",
  "The weasel-word vocabulary (supports, boosts, may help) is the pattern-recognition core.",
  "The label tells the truth in the fine print and the lie in the headline - read fine print first.",
  "Structure-function claims are legal because they avoid disease claims - which reveals how much is proven.",
  "A reflex drill: practiced on real labels until automatic.",
 ],
 "requirements": [
  "Reader must run the drill on a sample label.",
  "Reader must list the weasel-word vocabulary.",
  "Reader must explain the structure-function regulatory reality.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "FDA structure-function claim framework (referenced).",
 ],
},
{
 "key": "sig-home-kit",
 "name": "The Signature Home Wellness Kit",
 "group": "wellness-practices",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "description": ("Signature original: his Home Wellness Kit framework "
  "takes the public kit record and adds the Signature organization "
  "system - the kit as four stations. Station one, urgent (wound care and "
  "bleeding control, most accessible). Station two, comfort (cold pack, "
  "thermometer, saline spray, the documented pantry). Station three, "
  "medicines (OTC basics per label, expiry-checked, locked away from "
  "children). Station four, information (the Red-Flag Ledger, medication "
  "lists, poison-control number). The framework's Signature rule is that "
  "a kit is a system, not a box - every item has a station, every station "
  "has a check rhythm, and the twice-yearly audit keeps it alive. Lists "
  "supplies only; no dosing. Clearly labeled Signature-made, educational "
  "information only."),
 "how_it_works": ("The kit works through station logic: in a stressful "
  "moment, hands go to the right station without searching, which the "
  "record presents as the difference between a box of supplies and a "
  "working system. The audit rhythm - twice yearly, paired with the "
  "daylight-saving clock change as the memory anchor - keeps expiry and "
  "completeness current. The information station is the Signature "
  "emphasis: the ledger and medication lists make the kit usable by any "
  "household member or visitor. The demo audits sample kits against the "
  "four stations and reports the gaps."),
 "key_points": [
  "Signature original: four stations - urgent, comfort, medicines, information.",
  "A kit is a system, not a box: every item has a station, every station a check rhythm.",
  "The audit rhythm pairs with the clock change as its memory anchor, twice yearly.",
  "The information station makes the kit usable by any household member or visitor.",
  "Supplies only; dosing lives on labels, treatment in the teaching records.",
 ],
 "requirements": [
  "Reader must lay out the four stations with their contents.",
  "Reader must explain the station-logic advantage under stress.",
  "Reader must state the audit rhythm and its memory anchor.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "American Red Cross first-aid kit guidance (referenced).",
 ],
},
{
 "key": "sig-recovery-table",
 "name": "The Signature Recovery Table",
 "group": "wellness-practices",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "description": ("Signature original: his Recovery Table framework takes "
  "the public recovery-nutrition record and sets it as a literal table "
  "practice. The table rule: during recovery, meals happen at the table, "
  "seated, unhurried - because appetite is fragile in illness and the "
  "environment is part of the nutrition. The pattern guidance is the "
  "public record's: protein spread across the day, colorful plants, "
  "steady whole-grain energy, fluids alongside, smaller frequent meals "
  "when appetite is low. The framework's Signature teaching is that the "
  "table is treatment-adjacent: not medicine, but the setting in which "
  "the body's repair nutrition actually gets eaten. Dietary-restriction "
  "conditions follow professional guidance. Clearly labeled "
  "Signature-made, educational information only."),
 "how_it_works": ("The table works through environment design: the seated "
  "unhurried meal protects appetite and digestion in ways the record "
  "presents honestly as behavioral rather than biochemical. The pattern "
  "checklist - protein at each meal, plants for color, grains for steady "
  "energy - is run lightly, not obsessively, because the framework warns "
  "that food anxiety during recovery is its own harm. The smaller-frequent "
  "meals rule addresses the appetite reality of illness directly. The demo "
  "scores sample recovery days for table-practice elements without "
  "prescribing amounts."),
 "key_points": [
  "Signature original: the table rule - seated, unhurried meals during recovery.",
  "The environment is part of the nutrition; appetite is fragile in illness.",
  "Pattern checklist run lightly: protein, plants, grains, fluids - never obsessively.",
  "Smaller frequent meals answer the appetite reality of illness.",
  "Treatment-adjacent, not treatment; dietary restrictions follow professional guidance.",
 ],
 "requirements": [
  "Reader must state the table rule and its reasoning.",
  "Reader must describe the pattern checklist.",
  "Reader must explain why the checklist stays light, not obsessive.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "Clinical nutrition guidance on recovery eating patterns (referenced).",
 ],
},
{
 "key": "sig-sun-smart",
 "name": "The Signature Sun-Smart Practice",
 "group": "wellness-practices",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "description": ("Signature original: his Sun-Smart Practice takes the "
  "public sun-protection record's documented hierarchy and makes it a "
  "daily Signature habit. The practice: check the UV index with the "
  "morning weather (the two-second habit), shade and timing first, "
  "covering clothing second, sunscreen as the exposed-skin layer third "
  "with honest reapplication. The framework's Signature line is that the "
  "best sunscreen is the one between you and the sun - a roof, a tree, a "
  "hat. It teaches the skin-watch habit alongside: monthly self-checks "
  "for changing moles, non-healing sores, or unusual growths, with "
  "professional evaluation for anything suspicious. Clearly labeled "
  "Signature-made, educational information only, not medical advice."),
 "how_it_works": ("The practice works through the two-second habit: "
  "pairing the UV-index check with the existing morning weather check "
  "makes daily protection calibration automatic. The hierarchy is taught "
  "as a spending order - spend shade first because it is free and total, "
  "clothing second, sunscreen third as the gap-filler - which the record "
  "presents as the honest economics of protection. The skin-watch habit "
  "is the early-detection contribution: knowing one's own skin makes "
  "change visible. The demo maps sample UV days to protection levels and "
  "audits the hierarchy order."),
 "key_points": [
  "Signature original: the two-second UV-index habit paired with the morning weather check.",
  "Spending order: shade first (free and total), clothing second, sunscreen third as gap-filler.",
  "The best sunscreen is the one between you and the sun - a roof, a tree, a hat.",
  "Monthly skin-watch habit: know your skin so change is visible.",
  "Changing moles, non-healing sores, or unusual growths get professional evaluation.",
 ],
 "requirements": [
  "Reader must describe the two-second habit and its anchor.",
  "Reader must recite the protection spending order with reasoning.",
  "Reader must explain the skin-watch habit's early-detection logic.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "American Academy of Dermatology sun-protection guidance (referenced).",
 ],
},
{
 "key": "sig-whole-person",
 "name": "The Signature Whole-Person Wellness Charter",
 "group": "wellness-practices",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "description": ("Signature original: his Whole-Person Wellness Charter "
  "is the capstone of the Signature ladder - the single page that binds "
  "all 34 Signature frameworks into one personal constitution. The "
  "charter's articles: the body is the first instrument (sleep, movement, "
  "nourishment, and rest are maintenance, not luxury); comfort before "
  "cure-seeking (mild familiar symptoms get the comfort rituals; the "
  "charter forbids remedy-shopping for serious conditions); honesty in "
  "every claim (the compass and the claim-reader govern what enters the "
  "household); care without delay (the red-flag ledger overrides every "
  "other article); and the household covenant (wellness practiced together "
  "outlasts wellness practiced alone). The charter claims no medical "
  "authority and establishes none - it is a personal constitution for "
  "living the documented principles. Clearly labeled Signature-made, "
  "educational information only, not medical advice."),
 "how_it_works": ("The charter works as a constitutional layer: when "
  "individual frameworks conflict or a new remedy arrives, the articles "
  "decide. The comfort-before-cure-seeking article - comfort for mild symptoms, "
  "never cure-seeking for serious conditions - is the load-bearing "
  "one - it encodes this database's central safety rule as personal law. "
  "The record teaches the signing ritual: the charter is read aloud, "
  "signed, and kept with the home kit, which converts principles into "
  "commitment. The charter review is annual - the framework grows with "
  "the household. The demo verifies a sample charter contains all five "
  "articles and the safety precedence of the care-without-delay article."),
 "key_points": [
  "Signature original capstone: five articles binding all 34 Signature frameworks.",
  "Comfort before cure-seeking (never cure-seeking at home): mild familiar symptoms get rituals; serious conditions get professionals.",
  "Honesty in every claim: the compass and claim-reader govern what enters the household.",
  "Care without delay overrides every other article - safety precedence is constitutional.",
  "The household covenant: wellness practiced together outlasts wellness practiced alone.",
 ],
 "requirements": [
  "Reader must recite the five articles.",
  "Reader must explain the constitutional-layer function.",
  "Reader must state the safety precedence rule.",
 ],
 "standards": [
  "Signature-made content, clearly labeled; never presented as authentic public record.",
  SAFETY_STD,
 ],
 "citations": [
  SIG_TAIL,
  "The 34 Signature frameworks of this database, bound by this charter (self-reference).",
 ],
},
]
