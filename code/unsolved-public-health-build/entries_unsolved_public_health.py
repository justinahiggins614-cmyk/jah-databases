#!/usr/bin/env python3
"""Entries for the Unsolved Public Health databases (Manon's 16:15 orders,
Unsolved Problems Solved series).

34 famous unsolved public-health problems, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex). Public half: JAH-USPU-
(real, fact-checked problems as the world knows them: pandemic prediction and
prevention, health-equity gaps, the obesity epidemic's drivers, vaccine
hesitancy mechanics, aging-population care models, and the rest). Signature
half: JAH-USPUS- (same 34 problems through the Signature lens; titles
suffixed " (Signature Edition)", src signature, clearly labeled
Signature-made, never presented as authentic public record).

ID prefixes JAH-USPU- / JAH-USPUS- verified free 2026-10-17: zero hits in the
manifest id_prefix values and zero hits among all record IDs in
jah-databases-data-1.

Every signature_solution opens with the EXACT label
"Signature-generated proposed solution - not established science."
Public halves carry a short pointer; signature halves carry the full
treatment. Honesty rule: no claims of proof, no implied peer acceptance,
speculation never presented as settled. Where the honest answer is "we do not
know," we say so.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. All records human-readable sentences/paragraphs. Screened.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Method applied to public "
            "health: every unsolved problem a covenant question, the solution "
            "explorer the Signature system's walkthrough, confirm-and-refute "
            "panels the oath of honesty. Clearly labeled Signature-made, never "
            "presented as established science or authentic public record.")

CIT_HESITANCY = ("Larson HJ et al. Understanding vaccine hesitancy around vaccines and "
                 "vaccination. Vaccine. 2014;32:2150-2159; MacDonald NE. Vaccine hesitancy: "
                 "definition, scope and determinants. Vaccine. 2015;33:4161-4164; Dubé E et "
                 "al. Vaccine hesitancy, vaccine refusal and the anti-vaccine movement. "
                 "Expert Rev Vaccines. 2015;14:99-117.")
CIT_OBESITY = ("Swinburn BA et al. The global obesity pandemic: shaped by global drivers "
               "and local environments. Lancet. 2011;378:804-814; Hall KD et al. Quantification "
               "of the effect of energy imbalance on bodyweight. Lancet. 2011;378:826-837; "
               "NCD Risk Factor Collaboration. Lancet. 2017;390:2627-2642.")
CIT_FLU = ("WHO. Influenza (seasonal) fact sheet; Krammer F et al. Influenza. Nat Rev Dis "
           "Primers. 2018;4:18006; CDC. Disease burden of influenza; Iuliano AD et al. "
           "Lancet. 2018;391:1285-1300.")
CIT_TOBACCO = ("WHO Framework Convention on Tobacco Control. 2003; Jha P. Avoidable global "
               "cancer deaths and total deaths from smoking. Nat Rev Cancer. 2009;9:655-664; "
               "WHO. Global report on trends in prevalence of tobacco use.")
CIT_FOOD = ("USDA Economic Research Service. Food access research atlas; Walker RE et al. "
            "Disparities and access to healthy food in the United States. Int J Behav Nutr "
            "Phys Act. 2010;7:65; Beaulac J et al. A systematic review of food deserts. "
            "Prev Chronic Dis. 2009;6:A105.")
CIT_LEAD = ("Lanphear BP et al. Low-level lead exposure and mortality in US adults. Lancet "
            "Public Health. 2018;3:e177-e184; WHO. Lead poisoning and health fact sheet; "
            "NTP. Monograph on health effects of low-level lead. 2012.")
CIT_WATER = ("WHO/UNICEF Joint Monitoring Programme. Progress on household drinking water, "
             "sanitation and hygiene; Prüss-Ustün A et al. Burden of disease from inadequate "
             "water, sanitation and hygiene. Trop Med Int Health. 2019;24:553-570.")
CIT_LONELINESS = ("Holt-Lunstad J et al. Social relationships and mortality risk. PLoS Med. "
                  "2010;7:e1000316; Cacioppo JT, Patrick W. Loneliness: Human Nature and the "
                  "Need for Social Connection. Norton; 2008; National Academies. Social "
                  "Isolation and Loneliness in Older Adults. 2020.")
CIT_MENTAL = ("Patel V et al. The Lancet Commission on global mental health and sustainable "
              "development. Lancet. 2018;392:1553-1598; WHO. Mental Health Atlas; Wang PS et "
              "al. Use of mental health services for anxiety, mood, and substance disorders. "
              "Lancet. 2007;370:841-850.")
CIT_MATERNAL = ("Say L et al. Global causes of maternal death. Lancet Glob Health. "
                "2014;2:e323-e333; WHO. Trends in maternal mortality 2000-2020; Creanga AA et "
                "al. Pregnancy-related mortality in the United States. Obstet Gynecol. "
                "2017;130:366-373.")
CIT_CHRONIC = ("Wagner EH. Chronic disease management: what will it take to improve care for "
               "chronic illness? Eff Clin Pract. 1998;1:2-4; McGlynn EA et al. The quality of "
               "health care delivered to adults in the United States. N Engl J Med. "
               "2003;348:2635-2645.")
CIT_AIR = ("Cohen AJ et al. Estimates and 25-year trends of the global burden of disease "
           "attributable to ambient air pollution. Lancet. 2017;389:1907-1918; Lelieveld J et "
           "al. Effects of fossil fuel and total anthropogenic emission removal on public "
           "health and climate. PNAS. 2019;116:7192-7197.")
CIT_PREDICT = ("Jones KE et al. Global trends in emerging infectious diseases. Nature. "
               "2008;451:990-993; Morse SS et al. Prediction and prevention of the next "
               "pandemic zoonosis. Lancet. 2012;380:1956-1965; Carroll D et al. The Global "
               "Virome Project. Science. 2018;359:872-874.")
CIT_SPILLOVER = ("Plowright RK et al. Pathways to zoonotic spillover. Nat Rev Microbiol. "
                 "2017;15:502-510; IPBES. Workshop report on biodiversity and pandemics. 2020; "
                 "Allen T et al. Global hotspots and correlates of emerging zoonotic diseases. "
                 "Nat Commun. 2017;8:1124.")
CIT_EQUITY = ("Marmot M et al. Closing the gap in a generation: WHO Commission on Social "
              "Determinants of Health. Lancet. 2008;372:1661-1669; Chetty R et al. The "
              "association between income and life expectancy in the United States. JAMA. "
              "2016;315:1750-1766; Dwyer-Lindgren L et al. JAMA Intern Med. 2017.")
CIT_COLDCHAIN = ("WHO. Immunization supply chain and logistics; Lee BY et al. The impact of "
                 "making vaccines thermostable. Hum Vaccin Immunother. 2017;13:3044-3052; "
                 "PATH. Controlled temperature chain resources.")
CIT_AGING = ("WHO. World Report on Ageing and Health. 2015; Beard JR et al. The World "
             "Report on Ageing and Health. Lancet. 2016;387:2145-2154; UN. World Population "
             "Prospects.")
CIT_OPIOID = ("Dasgupta N et al. Opioid crisis: no easy fix to its social and economic "
              "determinants. Am J Public Health. 2018;108:182-186; Volkow ND et al. The "
              "changing opioid crisis. Annu Rev Med. 2019;70:133-151; Ciccarone D. Int J "
              "Drug Policy. 2019;71:86-96.")
CIT_DIABETES = ("NCD Risk Factor Collaboration. Lancet. 2016;387:1513-1530; Lean MEJ et al. "
                "Primary care-led weight management for remission of type 2 diabetes "
                "(DiRECT). Lancet. 2018;391:541-551; Taylor R. Diabetes Care. 2013.")
CIT_HYPERTENSION = ("NCD Risk Factor Collaboration. Lancet. 2021;398:957-980; Frieden TR et "
                    "al. Reducing premature mortality from cardiovascular and other "
                    "non-communicable diseases. Bull WHO. 2020;98:122-133.")
CIT_AMR = ("Murray CJL et al. Global burden of bacterial antimicrobial resistance in 2019. "
           "Lancet. 2022;399:629-655; O'Neill J. Review on Antimicrobial Resistance. 2016; "
           "WHO. Global action plan on antimicrobial resistance. 2015.")
CIT_MISINFO = ("Kata A. Anti-vaccine activists, Web 2.0, and the postmodern paradigm. "
               "Vaccine. 2012;30:3778-3789; Lewandowsky S et al. Misinformation and its "
               "correction. Psychol Sci Public Interest. 2012;13:106-131; WHO. Infodemic "
               "management resources.")
CIT_WORKFORCE = ("WHO. Global strategy on human resources for health: Workforce 2030; "
                 "Boniol M et al. Human resources for health. Bull WHO; Liu JX et al. "
                 "Human resources for health. Lancet. 2017;390:e20-e21.")
CIT_TBMAL = ("WHO. The End TB Strategy; Bhatt S et al. The effect of malaria control on "
             "Plasmodium falciparum in Africa. Nature. 2015;526:207-211; WHO. World malaria "
             "report.")
CIT_ONEHEALTH = ("Zinsstag J et al. One Health: The Theory and Practice of Integrated Health "
                 "Approaches. CABI; 2015; WHO/FAO/WOAH/UNEP. One Health Joint Plan of Action. "
                 "2022; Lancet. One Health series.")
CIT_UHC = ("WHO. Universal health coverage fact sheet; Wagstaff A et al. Progress on "
           "catastrophic health spending. Lancet Glob Health. 2018;6:e1202-e1211; Evans DB "
           "et al. Health systems financing. WHO. 2010.")
CIT_POSTVIRAL = ("Davis HE et al. Long COVID: major findings, mechanisms and recommendations. "
                 "Nat Rev Microbiol. 2023;21:133-146; Nalbandian A et al. Post-acute COVID-19 "
                 "syndrome. Nat Med. 2021;27:601-615.")
CIT_CLIMATE = ("Watts N et al. The 2023 report of the Lancet Countdown on health and climate "
               "change. Lancet. 2023;402:2346-2394; Ebi KL et al. Hot weather and heat "
               "extremes. Annu Rev Public Health. 2021;42:315-335.")
CIT_INTEROP = ("Mandl KD, Kohane IS. Escaping the EHR trap. N Engl J Med. 2012;366:2240-2242; "
               "HL7 FHIR standard; Adler-Milstein J et al. Health information exchange. "
               "Health Aff. 2013.")
CIT_SURVEIL = ("Henning KJ. What is syndromic surveillance? MMWR. 2004;53:7-11; WHO. Early "
               "warning alert and response; Brownstein JS et al. Digital disease detection. "
               "N Engl J Med. 2009;360:2153-2157.")
CIT_BEHAVIOR = ("Michie S et al. The behaviour change wheel. Implement Sci. 2011;6:42; Rose "
                "G. Sick individuals and sick populations. Int J Epidemiol. 1985;14:32-38; "
                "Marteau TM et al. Judging nudging. BMJ. 2011;342:d228.")
CIT_DEMENTIA = ("Livingston G et al. Dementia prevention, intervention, and care: 2020 report "
                "of the Lancet Commission. Lancet. 2020;396:413-446; WHO. Global status report "
                "on the public health response to dementia. 2021.")
CIT_NCD = ("Omran AR. The epidemiologic transition. Milbank Mem Fund Q. 1971;49:509-538; "
           "NCD Countdown 2030. Lancet. 2020;396:574-576; WHO. Global status report on "
           "noncommunicable diseases.")
CIT_THEORY = ("Evans RG, Stoddart GL. Producing health, consuming health care. Soc Sci Med. "
              "1990;31:1347-1363; Kindig DA, Stoddart G. What is population health? Am J "
              "Public Health. 2003;93:380-383; McKinlay JB. A case for refocusing upstream. "
              "Int J Health Serv. 2019.")

ENTRIES = [
 {
  "key": "vaccine-hesitancy",
  "name": "Why Do People Refuse Safe Vaccines?",
  "group": "Prevention and Behavior",
  "ladder_rank": 1, "ladder_tier": "foundations",
  "description": ("Vaccines are among the most effective tools in public health history, "
                  "credited with saving hundreds of millions of lives, yet refusal and "
                  "delay cluster in communities everywhere and have grown louder in the "
                  "internet age. The puzzle is not ignorance alone: hesitancy concentrates "
                  "among educated parents, in wealthy countries, and around specific "
                  "vaccines rather than all of them. After decades of campaigns, no "
                  "intervention reliably converts the hesitant at scale."),
  "problem": "What drives vaccine hesitancy, and why has no communication strategy reliably reversed it?",
  "background": ("The WHO's SAGE working group formalized vaccine hesitancy in 2015 as "
                 "delay in acceptance or refusal of vaccines despite availability, mapping "
                 "determinants to confidence, complacency, and convenience. Measles "
                 "resurgences in Europe and the United States in the 2010s were traced to "
                 "pockets of under-vaccination rather than supply failure. Research by "
                 "Larson and colleagues documented that hesitancy is vaccine-specific and "
                 "community-shaped, rooted in trust in institutions as much as in facts. "
                 "Corrective messaging studies repeatedly found that facts alone rarely "
                 "move the hesitant and can backfire, entrenching prior beliefs. Mandates "
                 "raise coverage but shift the conflict rather than resolving the trust "
                 "gap. The field knows what hesitancy looks like; it does not know a "
                 "general cure."),
  "why_it_matters": ("Herd immunity is a collective good that individual refusal can "
                     "break: measles needs roughly 95 percent coverage, and sub-threshold "
                     "pockets have repeatedly seeded outbreaks. Understanding hesitancy is "
                     "the difference between vaccines that exist and vaccines that "
                     "protect, and the same trust mechanics govern every future "
                     "immunization campaign."),
  "sig_lens": ("The Signature lens treats hesitancy not as a knowledge deficit but as a "
               "broken covenant between institutions and communities: the question is "
               "not what people do not know, but whom they no longer trust to tell them."),
  "sol_public": ("The Signature system proposes hesitancy is a trust-ledger problem: "
                 "communities keep accounts of institutional reliability, and vaccine "
                 "acceptance follows the ledger balance, not the fact sheet. Rebuild the "
                 "ledger - consistent honesty, visible accountability, trusted local "
                 "messengers - and acceptance follows. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) vaccine decisions are social trust decisions, "
              "not individual knowledge decisions; (2) trust behaves like a ledger - "
              "deposits and withdrawals accumulate over years across all institutional "
              "contacts, not just health ones; (3) messengers inherit the ledger balance "
              "of the institution they represent. Reasoning path: if hesitancy were about "
              "facts, more facts would fix it, but correction studies show facts "
              "entrench. If it were about access, the wealthy would not hesitate. The "
              "remaining variable is the ledger: communities that experienced "
              "institutional betrayal - medical or otherwise - show durable refusal "
              "patterns across generations. Proposed mechanism: the trust ledger is "
              "written by every interaction a community has with authority - a denied "
              "claim, a dismissed complaint, a broken promise - and vaccine campaigns "
              "draw on the balance. Interventions that deposit first (listening "
              "clinics, admitted uncertainty, local credible voices) change uptake; "
              "fact campaigns that withdraw (dismissal, coercion) do not. What would "
              "confirm it: community-level ledger metrics - measured institutional "
              "trust, complaint-resolution rates - predicting vaccine uptake better "
              "than education levels or income. What would kill it: a community with "
              "high measured institutional trust and high hesitancy, or a fact-only "
              "campaign that durably converts the hesitant at scale. What it does NOT "
              "claim: that misinformation is harmless, that mandates never work, or "
              "that any messenger can substitute for institutional honesty. The honest "
              "unknown: how long ledger repair takes - the decay rate of distrust is "
              "the missing measurement."),
  "key_points": [
   "SAGE (2015): hesitancy is delay or refusal despite availability; determinants are confidence, complacency, convenience.",
   "Measles resurgences trace to under-vaccinated pockets, not supply failure; roughly 95 percent coverage is needed.",
   "Hesitancy is vaccine-specific and community-shaped, rooted in institutional trust as much as in facts.",
   "Correction studies show facts alone rarely move the hesitant and can entrench prior beliefs.",
   "Mandates raise coverage but shift the conflict; the trust gap remains unresolved."],
  "requirements": [
   "Confirm: community institutional-trust metrics predict vaccine uptake better than education or income.",
   "Confirm: trust-deposit interventions (listening clinics, admitted uncertainty) durably raise uptake.",
   "Refute: a high-trust community with high hesitancy, breaking the ledger model.",
   "Refute: a fact-only campaign that durably converts the hesitant at population scale."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim misinformation is harmless or that mandates never work.",
   "Must measure the decay rate of distrust - currently the missing constant."],
  "citations": [CIT_HESITANCY],
 },
 {
  "key": "obesity-drivers",
  "name": "What Is Really Driving the Obesity Epidemic?",
  "group": "Prevention and Behavior",
  "ladder_rank": 2, "ladder_tier": "foundations",
  "description": ("Since 1975, global obesity has nearly tripled, and most of the world's "
                  "population now lives in countries where overweight kills more people "
                  "than underweight. The rise is too fast for genes: it happened within "
                  "one generation. Yet the field still argues over the prime mover - "
                  "calories, sugar, ultra-processing, inactivity, sleep, stress, "
                  "endocrine disruptors, the microbiome - with no settled ranking of "
                  "causes."),
  "problem": "Which drivers actually caused the obesity epidemic, and in what order of importance?",
  "background": ("Swinburn and colleagues' 2011 Lancet series framed obesity as the "
                 "product of global drivers acting through local food environments, not "
                 "of individual gluttony. Hall's energy-balance models quantified how "
                 "small sustained surpluses compound into large weight gains over "
                 "years. The food system transformed in parallel: ultra-processed "
                 "products, larger portions, cheap sweetened drinks, and engineered "
                 "palatability spread worldwide just as the epidemic curve bent "
                 "upward. Competing hypotheses multiplied - the carbohydrate-insulin "
                 "model blaming refined carbs, the protein-leverage hypothesis, "
                 "endocrine-disruptor theories, microbiome theories - each with "
                 "supporting trials, none explaining the whole curve. Policy "
                 "experiments from soda taxes to front-of-pack labels show modest "
                 "effects, but no country has reversed the epidemic at population "
                 "scale. The causes are plural; their weights are not."),
  "why_it_matters": ("Obesity drives the noncommunicable disease wave - diabetes, heart "
                     "disease, many cancers - that now causes most deaths on earth. A "
                     "correct causal ranking decides where trillions in health spending "
                     "and regulation should aim; a wrong one wastes the decisive "
                     "decade."),
  "sig_lens": ("The Signature lens treats the epidemic as an engineered-environment "
               "problem: human appetite regulation, tuned for scarcity, was placed "
               "inside an abundance machine built to defeat it."),
  "sol_public": ("The Signature system proposes the driver ranking is knowable through "
                 "natural-experiment accounting: the epidemic curve is the sum of dated "
                 "environmental shocks - ultra-processing rollout, portion growth, "
                 "sweetener substitution, activity collapse - and each shock's "
                 "population weight can be decomposed. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the epidemic's speed rules out genetic change, "
              "so the cause is environmental and dated; (2) environmental shocks have "
              "fingerprints - each candidate driver changed at a known place and time; "
              "(3) body-weight dynamics are slow integrators, so a sustained small "
              "surplus explains large gains (Hall's models). Reasoning path: stack the "
              "dated shocks against the epidemic curve country by country. "
              "Ultra-processing penetration, sweetened-drink availability, portion "
              "sizes, occupational activity, sleep duration, and car dependence each "
              "shifted at measurable dates; the weight-gain curve's inflection should "
              "match the dominant shock's arrival with the integrator's lag. "
              "Proposed mechanism: an appetite-defeat environment - engineered "
              "hyper-palatability plus ubiquitous availability plus shrinking activity "
              "demands - overwhelms a scarcity-tuned regulatory system; the integrator "
              "accumulates a few dozen kilocalories of daily surplus into kilograms "
              "per year. What would confirm it: cross-country decomposition showing "
              "the same dated shocks predicting inflection points with the predicted "
              "lag, and the summed shocks accounting for the full observed gain. "
              "What would kill it: countries where the dated shocks arrived but the "
              "curve did not bend, or a single biological driver (a pathogen, a "
              "pollutant) that explains the curve better. What it does NOT claim: "
              "that willpower is irrelevant, that any single food is the villain, or "
              "that decomposition replaces physiology. The honest unknown: the exact "
              "weights - decomposition gives a ranking, not a settled proof."),
  "key_points": [
   "Global obesity nearly tripled since 1975; the rise is too fast for genes.",
   "Swinburn (2011): global drivers act through local food environments, not individual gluttony.",
   "Hall's models: small sustained energy surpluses compound into large weight gains over years.",
   "Candidate drivers - sugar, ultra-processing, inactivity, sleep, disruptors, microbiome - all have evidence; none explains the whole curve.",
   "No country has reversed the epidemic at population scale; policies show modest effects."],
  "requirements": [
   "Confirm: dated environmental shocks predict each country's obesity inflection with the integrator lag.",
   "Confirm: summed dated shocks account for the full observed population weight gain.",
   "Refute: shock arrival without curve bending in matched countries.",
   "Refute: a single biological driver explaining the curve better than the shock stack."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim willpower is irrelevant or that one food is the villain.",
   "Decomposition yields a ranking, not a settled proof - weights stay provisional."],
  "citations": [CIT_OBESITY],
 },
 {
  "key": "seasonal-flu-burden",
  "name": "Why Does Seasonal Flu Still Kill Hundreds of Thousands?",
  "group": "Infectious Disease Control",
  "ladder_rank": 3, "ladder_tier": "foundations",
  "description": ("Every year influenza infects roughly a billion people and kills an "
                  "estimated 290,000 to 650,000, despite a century of virology, annual "
                  "vaccines, and antiviral drugs. Vaccine effectiveness hovers around "
                  "40 to 60 percent in good years and far less in bad ones, because "
                  "the virus drifts and the vaccine must be reformulated on a guess. "
                  "A universal flu vaccine has been a stated goal for decades; none "
                  "has arrived."),
  "problem": "Why can we not reliably prevent or neutralize seasonal influenza after a century of effort?",
  "background": ("Influenza's segmented RNA genome reassorts and its surface proteins "
                 "drift under immune pressure, which is why last year's immunity "
                 "partly fails this year. The current vaccine strategy, built in the "
                 "1940s, grows that year's best-guess strains in eggs and hopes the "
                 "match holds - a system that mismatches badly in seasons like "
                 "2017-2018. Iuliano and colleagues estimated up to 650,000 annual "
                 "respiratory deaths, concentrated in the elderly and the poor. "
                 "Antivirals help if given early, which rarely happens in the "
                 "settings where most deaths occur. Universal-vaccine programs "
                 "targeting the conserved stalk of hemagglutinin have shown promise "
                 "in trials but no licensed product. The virus's evolvability "
                 "systematically outruns a fixed annual countermeasure."),
  "why_it_matters": ("Flu is the recurring proof that a known, watched pathogen can "
                     "still defeat preparedness: it rehearses every pandemic "
                     "response gap annually. Cracking flu would validate the "
                     "platforms - universal vaccines, rapid reformulation, real-time "
                     "surveillance - that the next pandemic will demand."),
  "sig_lens": ("The Signature lens treats flu as an adversary running an annual "
               "red-team exercise against human immunity: the defense is static "
               "and annual; the attack is continuous and evolutionary."),
  "sol_public": ("The Signature system proposes the fix is to stop aiming at the "
                 "moving target: a universal vaccine aimed at conserved viral "
                 "machinery, paired with continuous surveillance that treats every "
                 "season as a live experiment. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the virus's mutable surface is a decoy - "
              "conserved internal machinery cannot drift freely or the virus "
              "breaks; (2) immune memory can be trained toward conserved targets "
              "if vaccines present them without the mutable decoys; (3) annual "
              "reformulation is a losing race against a continuous mutator. "
              "Reasoning path: every failed season is the same failure - aiming "
              "at hemagglutinin's head, the most mutable part. Stalk-directed and "
              "T-cell approaches aim at what the virus cannot change; the "
              "constraint is not biology but attention, because conserved targets "
              "are less immunodominant and need engineered presentation. "
              "Proposed mechanism: chimeric-hemagglutinin and mRNA platforms "
              "presenting conserved stalk and internal proteins, updated only "
              "when the conserved targets themselves shift - measured in "
              "decades, not seasons - with surveillance re-tasked from "
              "strain-guessing to escape-monitoring. What would confirm it: a "
              "stalk-based vaccine showing multi-season protection against "
              "drifted strains in field trials, and escape mutations carrying "
              "measurable fitness costs. What would kill it: conserved targets "
              "proving unreachable by human immunity at protective titers, or "
              "the virus escaping them without fitness cost. What it does NOT "
              "claim: that a universal vaccine is proven, that egg-based "
              "vaccines should be abandoned before a replacement exists, or "
              "that flu can be eradicated. The honest unknown: the durability "
              "of stalk immunity in real populations over many seasons."),
  "key_points": [
   "Influenza infects about a billion people yearly; an estimated 290,000-650,000 die (Iuliano et al. 2018).",
   "Antigenic drift defeats last year's immunity; vaccines are reformulated annually on a best guess.",
   "Vaccine effectiveness is 40-60 percent in good years, far less when the guess mismatches.",
   "The mutable hemagglutinin head is the target; the conserved stalk is the harder, better target.",
   "No universal flu vaccine is licensed despite decades as a stated goal."],
  "requirements": [
   "Confirm: a conserved-target vaccine protects across drifted seasons in field trials.",
   "Confirm: escape mutations at conserved targets carry measurable fitness costs.",
   "Refute: conserved targets unreachable at protective titers by human immunity.",
   "Refute: escape without fitness cost, collapsing the conserved-target strategy."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim a universal vaccine is proven or that current vaccines should be dropped.",
   "Durability of stalk immunity in real populations remains the open measurement."],
  "citations": [CIT_FLU],
 },
 {
  "key": "tobacco-persistence",
  "name": "Why Does Tobacco Still Kill 8 Million a Year?",
  "group": "Prevention and Behavior",
  "ladder_rank": 4, "ladder_tier": "foundations",
  "description": ("The harms of smoking have been settled science since the 1950s, "
                  "advertising is banned in most countries, taxes are high, and plain "
                  "packaging spreads - yet tobacco still kills over 8 million people "
                  "a year, and 1.3 billion people still use it. Smoking has fallen "
                  "in rich countries while rising or stalling where regulation is "
                  "weakest. The industry adapts faster than the controls: new "
                  "products, new markets, new loopholes."),
  "problem": "Why do proven tobacco controls not extinguish the epidemic, and what would actually end it?",
  "background": ("The 2003 WHO Framework Convention on Tobacco Control gave the world "
                 "its first global health treaty, built on the MPOWER package: taxes, "
                 "smoke-free spaces, cessation help, warnings, ad bans. Where fully "
                 "implemented, smoking fell sharply - Australia, the UK, Brazil. But "
                 "the industry shifted volume to low- and middle-income countries, "
                 "introduced heated tobacco and e-cigarettes that split the public "
                 "health community, and exploited regulatory gaps with aggressive "
                 "marketing to youth. Jha estimated that a billion tobacco deaths "
                 "this century are avoidable under full control. Nicotine addiction "
                 "is a pharmacological trap with a social delivery system; taxes "
                 "and bans attack the delivery while the trap resets in each new "
                 "generation. No country has reached the endgame - near-zero "
                 "prevalence - though New Zealand, the UK, and others have set "
                 "endgame targets."),
  "why_it_matters": ("Tobacco is the largest single preventable cause of death on "
                     "earth. The endgame question - what combination finally drives "
                     "prevalence to near zero - is the template for every other "
                     "commercial determinant of health, from alcohol to ultra-"
                     "processed food."),
  "sig_lens": ("The Signature lens treats tobacco as a captured market problem: a "
               "product engineered for addiction, sold by an industry that profits "
               "from the trap and spends to protect it."),
  "sol_public": ("The Signature system proposes the endgame is a supply-side phaseout "
                 "paired with a nicotine-offramp: sinking the legal sales quota while "
                 "offering every smoker a funded, supported exit. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) demand-side measures asymptote - taxes and "
              "bans reduce but never reach the addicted core; (2) the industry's "
              "political spending is the binding constraint on policy, not public "
              "opinion; (3) nicotine demand without smoke is separable from "
              "nicotine demand with smoke. Reasoning path: countries that "
              "implemented full MPOWER plateaued at 10-15 percent smoking; the "
              "remaining smokers are the most addicted and least reached. "
              "Endgame requires attacking supply: a sinking lid on retail "
              "licenses, a generational sales ban (no sales to anyone born after "
              "a cutoff year), and denicotinization standards - while funding a "
              "universal cessation offramp so the phaseout is a rescue, not a "
              "punishment. Proposed mechanism: the sinking lid steadily raises "
              "the real price of legal supply and shrinks availability; the "
              "generational ban makes initiation structurally impossible; the "
              "offramp converts the addicted core rather than criminalizing it. "
              "What would confirm it: jurisdictions with generational bans or "
              "sinking lids showing initiation collapse and no compensating "
              "illicit market at scale. What would kill it: illicit supply fully "
              "replacing legal supply, or denicotinized products failing to "
              "satisfy the addicted core. What it does NOT claim: that prohibition "
              "works - this is phased supply reduction, not a ban on possession - "
              "or that e-cigarettes are safe. The honest unknown: the size of "
              "the illicit replacement market under a real phaseout."),
  "key_points": [
   "Tobacco kills over 8 million yearly; 1.3 billion people still use it despite settled harms.",
   "The 2003 Framework Convention and MPOWER package cut smoking where fully implemented.",
   "Full-MPOWER countries plateau around 10-15 percent - the addicted core resists demand measures.",
   "The industry shifted volume to poorer countries and new products, outpacing regulation.",
   "No country has reached endgame prevalence near zero; several have set targets."],
  "requirements": [
   "Confirm: generational sales bans collapse initiation without large-scale illicit replacement.",
   "Confirm: sinking-lid jurisdictions show steady prevalence decline below the demand-side plateau.",
   "Refute: illicit supply fully replacing legal supply under phaseout.",
   "Refute: the addicted core unconvertible by any funded offramp."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Not prohibition of possession - phased supply reduction with a funded exit.",
   "The illicit-market response is the decisive unknown and must be measured, not assumed."],
  "citations": [CIT_TOBACCO],
 },
 {
  "key": "food-deserts",
  "name": "Why Can't Everyone Reach Healthy Food?",
  "group": "Equity and Access",
  "ladder_rank": 5, "ladder_tier": "foundations",
  "description": ("In rich and poor countries alike, the neighborhoods with the worst "
                  "health are the ones where fresh food is hardest to buy. The USDA "
                  "maps millions of Americans living more than a mile from a "
                  "supermarket; in much of the world the problem is not distance but "
                  "price. Yet studies keep finding that simply opening a supermarket "
                  "in a food desert barely changes what people eat - the puzzle is "
                  "deeper than geography."),
  "problem": "Why does poor food access persist, and why do supply-side fixes change diets so little?",
  "background": ("Walker and colleagues' 2010 review established that low-income and "
                 "minority neighborhoods face systematically worse food environments - "
                 "fewer supermarkets, more fast food, higher prices for fresh "
                 "produce. The food-desert concept drove policy: financing for new "
                 "stores in underserved areas. Then the evaluations came in: new "
                 "supermarkets improved perceptions and property values but shifted "
                 "diets only marginally, because shopping habits, prices, time, "
                 "cooking skills, and the pull of nearby cheap calories dominate "
                 "the store's presence. Research pivoted to food swamps - areas "
                 "flooded with unhealthy options - and to affordability, which "
                 "consistently predicts diet quality better than distance. The "
                 "access problem is real; the naive fix was not."),
  "why_it_matters": ("Diet is now the leading behavioral risk factor for ill health "
                     "worldwide. If access interventions miss the mechanism, the "
                     "money flows to stores that do not change health, while the "
                     "real levers - price, time, habit - go unfunded."),
  "sig_lens": ("The Signature lens treats the food desert as a symptom of a food "
               "swamp: the problem was never the missing store but the surrounding "
               "flood of cheap engineered calories."),
  "sol_public": ("The Signature system proposes access must be rebuilt as a full "
                 "food environment: affordability first, swamp drainage second, "
                 "store placement third - measured by diet change, not by stores "
                 "opened. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) people eat what is cheap, fast, and nearby - "
              "in that order; (2) a new store changes none of the three if the "
              "swamp remains; (3) cooking time and skill are real constraints, not "
              "excuses. Reasoning path: the failed supermarket experiments are "
              "data, not mysteries - they prove geography was the wrong binding "
              "constraint. The binding constraints are relative price (healthy "
              "calories cost more per calorie), time poverty (two jobs leave no "
              "cooking hour), and habit infrastructure. Proposed mechanism: a "
              "three-lever environment rebuild - targeted healthy-food subsidies "
              "that flip the price ratio, swamp drainage (zoning and licensing "
              "limits on fast-food density near schools and in poor areas), and "
              "time-saving healthy defaults (prepared healthy meals at fast-food "
              "prices). What would confirm it: neighborhoods where the price "
              "ratio flipped showing diet change at population scale, with the "
              "effect tracking the subsidy, not the store count. What would kill "
              "it: price-ratio flips with no diet change, implying the constraint "
              "is purely cultural. What it does NOT claim: that supermarkets are "
              "useless, that education does not matter, or that this is proven. "
              "The honest unknown: how large the price flip must be to move the "
              "median diet."),
  "key_points": [
   "Low-income neighborhoods face systematically worse food environments: fewer stores, more fast food, higher fresh prices.",
   "New supermarkets in food deserts improved perceptions but barely changed diets.",
   "Research pivoted to food swamps - flooding with unhealthy options - and to affordability.",
   "Price predicts diet quality better than distance in most studies.",
   "Time poverty and cooking constraints are binding for working households."],
  "requirements": [
   "Confirm: flipping the healthy-vs-unhealthy price ratio moves population diets at scale.",
   "Confirm: swamp drainage (density limits) adds diet improvement beyond subsidies alone.",
   "Refute: large price flips with zero diet change, implying purely cultural constraints.",
   "Refute: store placement alone achieving diet change without price or swamp changes."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim supermarkets are useless or education irrelevant.",
   "The required price-flip magnitude is the open measurement."],
  "citations": [CIT_FOOD],
 },
 {
  "key": "lead-exposure",
  "name": "Why Is Lead Poisoning Still With Us?",
  "group": "Equity and Access",
  "ladder_rank": 6, "ladder_tier": "foundations",
  "description": ("Lead was removed from gasoline and paint decades ago in rich "
                  "countries, yet it still poisons children everywhere: old "
                  "housing, water pipes, soil, informal battery recycling, "
                  "spices, cookware. Lanphear's 2018 study tied even low-level "
                  "lead exposure to hundreds of thousands of adult deaths "
                  "yearly in the US alone. There is no safe level, and the "
                  "damage - to brains, hearts, kidneys - is largely "
                  "irreversible."),
  "problem": "Why does a solved toxicology problem keep poisoning new generations?",
  "background": ("The lead story is public health's great partial victory: "
                 "blood lead levels in American children fell over 90 percent "
                 "after leaded gasoline was phased out, and average IQ rose. "
                 "But the sources diversified as the obvious one vanished. "
                 "Lead paint remains in millions of old homes; lead service "
                 "lines still deliver drinking water in older cities - Flint "
                 "made this visible in 2014; informal used-battery recycling "
                 "poisons children across South Asia and Africa; contaminated "
                 "spices and traditional remedies add more. Research keeps "
                 "lowering the harm threshold: effects on IQ, behavior, and "
                 "cardiovascular mortality appear at levels once called "
                 "background. Remediation is expensive, piecemeal, and "
                 "invisible - no ribbon-cuttings for pipe replacement - so it "
                 "loses every budget fight."),
  "why_it_matters": ("Lead steals IQ points from children and years from adults, "
                     "concentrated in the poorest neighborhoods - a permanent "
                     "tax on the life chances of the already disadvantaged. "
                     "Unlike most health problems, this one has a complete "
                     "technical solution: remove the sources."),
  "sig_lens": ("The Signature lens treats lead as a maintenance problem, not a "
               "science problem: the knowledge is complete, the funding "
               "mechanism is missing."),
  "sol_public": ("The Signature system proposes a source-removal bond: fund the "
                 "unseen remediation - pipes, paint, soil, recycling - with "
                 "bonds repaid from the measured IQ and health gains, making "
                 "the invisible visible to budgets. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the toxicology is settled - the only "
              "missing piece is removal; (2) remediation loses budgets because "
              "its benefits are diffuse, delayed, and invisible; (3) lead "
              "sources are enumerable per city - pipes, pre-1978 housing, "
              "recycling sites. Reasoning path: cost-benefit studies already "
              "show lead remediation returns many times its cost in earnings "
              "and health, yet it is never funded at scale - a classic "
              "externality-and-visibility failure, not a knowledge failure. "
              "Proposed mechanism: municipal source-removal bonds - borrow "
              "against the documented future earnings and health savings, "
              "remediate every enumerated source on a fixed schedule, and "
              "repay from the measured gains, with independent blood-lead "
              "surveillance as the audit. What would confirm it: bond-funded "
              "cities showing blood-lead declines tracking the remediation "
              "schedule and earnings gains covering the bond. What would kill "
              "it: enumerated sources proving unfindable at scale, or "
              "remediation failing to move blood lead because of unknown "
              "sources. What it does NOT claim: that bonds are the only "
              "funding route, or that all sources are currently known. The "
              "honest unknown: the true inventory of minor sources - spices, "
              "cookware, informal recycling - in each setting."),
  "key_points": [
   "No safe level of lead exposure; damage to brain, heart, and kidneys is largely irreversible.",
   "US child blood lead fell over 90 percent after the gasoline phaseout - the partial victory.",
   "Remaining sources: old paint, lead water pipes, contaminated soil, informal battery recycling, spices.",
   "Lanphear (2018): low-level lead tied to hundreds of thousands of adult deaths yearly in the US.",
   "Remediation is proven cost-beneficial but loses budgets because it is invisible and slow."],
  "requirements": [
   "Confirm: bond-funded cities show blood-lead declines tracking the remediation schedule.",
   "Confirm: measured earnings and health gains cover the bond costs.",
   "Refute: enumerated sources unfindable at scale, breaking the inventory premise.",
   "Refute: remediation without blood-lead movement, implying dominant unknown sources."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim all sources are currently known.",
   "The minor-source inventory per setting is the open measurement."],
  "citations": [CIT_LEAD],
 },
 {
  "key": "clean-water-gaps",
  "name": "Why Do Billions Still Lack Safe Water?",
  "group": "Equity and Access",
  "ladder_rank": 7, "ladder_tier": "foundations",
  "description": ("Two billion people still drink water contaminated with feces, "
                  "and unsafe water, sanitation, and hygiene kill over a million "
                  "people a year, mostly children under five. The germ theory is "
                  "160 years old; chlorination is over a century old. The "
                  "technology to fix this fits in a bucket. The gap is not "
                  "knowledge - it is the last mile of infrastructure, "
                  "maintenance, and money."),
  "problem": "Why does a century-old, bucket-scale technology still not reach two billion people?",
  "background": ("The WHO/UNICEF Joint Monitoring Programme tracks a slow "
                 "climb: billions gained improved water since 2000, but "
                 "population growth, urbanization, and climate stress keep the "
                 "absolute unserved numbers high. Prüss-Ustün and colleagues "
                 "attributed over a million deaths a year to inadequate WASH. "
                 "The pattern is familiar: a borehole is drilled, the pump "
                 "breaks within years, no one maintains it, the community "
                 "returns to the river. Point-of-use chlorination and filters "
                 "work in trials but adherence collapses without behavior "
                 "support. Utilities in poor cities cannot collect tariffs "
                 "from the poorest, so they do not extend the pipes. The "
                 "failure is institutional durability, not chemistry."),
  "why_it_matters": ("Safe water is the highest-return investment in public "
                     "health history: every dollar returns several in health "
                     "and time, mostly to women and girls who haul water. "
                     "Closing the gap would cut child mortality faster than "
                     "almost any other single intervention."),
  "sig_lens": ("The Signature lens treats water as a maintenance covenant: the "
               "pump that breaks and is never fixed is a broken promise, and "
               "the fix is institutional, not chemical."),
  "sol_public": ("The Signature system proposes maintenance-first water: every "
                 "new source funded with its 20-year maintenance contract and "
                 "a sensor-verified uptime bond, so the pump that breaks gets "
                 "fixed by contract, not by charity. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) water technology is solved - only "
              "delivery durability is not; (2) broken infrastructure is "
              "predictable - pumps fail on known schedules; (3) communities "
              "will pay small tariffs if the water actually flows. Reasoning "
              "path: the graveyard of broken boreholes proves that "
              "capital-without-maintenance is the failure mode. Sensor "
              "technology now makes uptime verifiable remotely and cheaply, "
              "which turns maintenance from a hope into a contract. Proposed "
              "mechanism: every new water point is financed as a 20-year "
              "service contract - capital plus scheduled maintenance plus "
              "sensor-verified uptime - with payment tied to flow, not to "
              "construction, and tariffs sized to willingness-to-pay "
              "studies. What would confirm it: contract-funded water points "
              "showing multi-year uptime far above the charity-built "
              "baseline, with tariff collection sustaining the contract. "
              "What would kill it: sensors and contracts failing to survive "
              "the same institutional decay, or willingness to pay proving "
              "too low to sustain any model. What it does NOT claim: that "
              "technology alone fixes governance, or that all water "
              "problems are maintenance problems. The honest unknown: the "
              "tariff level that sustains service without excluding the "
              "poorest."),
  "key_points": [
   "Two billion people drink fecally contaminated water; inadequate WASH kills over a million yearly.",
   "The technology is century-old and bucket-scale; the gap is infrastructure, maintenance, and money.",
   "The classic failure: a borehole is drilled, the pump breaks, no one maintains it.",
   "Point-of-use treatment works in trials but adherence collapses without behavior support.",
   "Utilities cannot collect tariffs from the poorest, so pipes never extend to them."],
  "requirements": [
   "Confirm: service-contract water points sustain multi-year uptime above charity-built baselines.",
   "Confirm: tariff collection sustains the maintenance contract without excluding the poorest.",
   "Refute: contracts decaying like charity projects, proving the failure is deeper than funding form.",
   "Refute: willingness to pay too low to sustain any service model."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim technology fixes governance.",
   "The sustainable tariff level is the open measurement."],
  "citations": [CIT_WATER],
 },
 {
  "key": "loneliness-epidemic",
  "name": "Why Is Loneliness a Public Health Crisis?",
  "group": "Prevention and Behavior",
  "ladder_rank": 8, "ladder_tier": "foundations",
  "description": ("Loneliness predicts early death about as strongly as smoking "
                  "fifteen cigarettes a day, raising risks of heart disease, "
                  "dementia, depression, and immune dysfunction. Rates have "
                  "climbed for decades as households shrink, communities thin, "
                  "and screens replace gathering places. Health systems built "
                  "for germs and genes have no prescription for a missing "
                  "social fabric."),
  "problem": "Why is social disconnection rising despite unprecedented connectivity, and how can public health reverse it?",
  "background": ("Holt-Lunstad's 2010 meta-analysis of 148 studies found social "
                 "relationships rivaling classic risk factors in mortality "
                 "prediction - an effect size medicine could not ignore. "
                 "Cacioppo's work showed loneliness is not solitude but "
                 "perceived isolation, with distinct biology: heightened "
                 "vigilance, inflammation, fragmented sleep. The US Surgeon "
                 "General declared loneliness an epidemic in 2023. Yet "
                 "interventions are thin: befriending schemes, social "
                 "prescribing, community hubs - all small, all under-"
                 "evaluated. The drivers are structural - car-dependent "
                 "sprawl, the decline of third places, precarious work "
                 "schedules, the attention economy - which no clinic can "
                 "prescribe away."),
  "why_it_matters": ("If loneliness kills like smoking, it deserves smoking-"
                     "scale policy: the built environment, work schedules, "
                     "and digital design are health exposures. Cracking it "
                     "would cut the burden of depression, dementia, and "
                     "cardiovascular disease simultaneously."),
  "sig_lens": ("The Signature lens treats connection as infrastructure: "
               "loneliness is what happens when the social grid - the third "
               "places, the rituals, the casual contact - is demolished and "
               "never rebuilt."),
  "sol_public": ("The Signature system proposes social infrastructure as a "
                 "health intervention: fund third places, protect shared "
                 "rituals, and design neighborhoods for casual contact, then "
                 "measure loneliness like blood pressure. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) loneliness is driven by the "
              "disappearance of low-friction social contact, not by "
              "individual social failure; (2) the built environment and "
              "schedules are modifiable health exposures; (3) perceived "
              "isolation can be measured reliably enough to manage. "
              "Reasoning path: the risk factor is structural, so the "
              "intervention must be structural - befriending one lonely "
              "person treats the symptom while the grid stays down. "
              "Proposed mechanism: municipal social-infrastructure standards "
              "- walkable third places within reach, protected community "
              "rituals, work schedules that preserve shared free time - "
              "with loneliness surveillance (brief validated scales in "
              "routine health surveys) guiding investment the way air "
              "monitors guide pollution control. What would confirm it: "
              "neighborhoods rebuilt for contact showing loneliness and "
              "downstream disease declines tracking the investment. What "
              "would kill it: contact-rich environments with unchanged "
              "loneliness, implying the driver is internal, not "
              "environmental. What it does NOT claim: that introversion is "
              "pathology, that digital contact is worthless, or that this "
              "is proven. The honest unknown: the dose-response - how much "
              "contact, of what kind, moves the needle."),
  "key_points": [
   "Loneliness predicts mortality comparably to smoking 15 cigarettes a day (Holt-Lunstad 2010).",
   "It is perceived isolation with distinct biology: vigilance, inflammation, fragmented sleep.",
   "Drivers are structural: sprawl, lost third places, precarious schedules, the attention economy.",
   "Interventions (befriending, social prescribing) are small and under-evaluated.",
   "Health systems have no prescription for a missing social fabric."],
  "requirements": [
   "Confirm: contact-rebuilt neighborhoods show loneliness and disease declines tracking investment.",
   "Confirm: loneliness surveillance predicts downstream health costs well enough to guide budgets.",
   "Refute: contact-rich environments with unchanged loneliness.",
   "Refute: no dose-response between contact and loneliness at any feasible scale."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not pathologize introversion or dismiss digital contact.",
   "The contact dose-response is the open measurement."],
  "citations": [CIT_LONELINESS],
 },
 {
  "key": "mental-health-access",
  "name": "Why Can't People Get Mental Health Care?",
  "group": "Equity and Access",
  "ladder_rank": 9, "ladder_tier": "foundations",
  "description": ("Depression and anxiety are among the leading causes of "
                  "disability worldwide, effective treatments exist - "
                  "therapy, medication, community care - yet the treatment "
                  "gap is staggering: in low- and middle-income countries, "
                  "76 to 85 percent of people with serious mental disorders "
                  "receive no treatment, and even rich countries leave half "
                  "unserved. The shortage is not of knowledge but of hands, "
                  "money, and permission."),
  "problem": "Why does the mental-health treatment gap persist when effective treatments are known and cheap?",
  "background": ("The 2018 Lancet Commission on global mental health called "
                 "the treatment gap a moral and economic failure, noting "
                 "that most countries spend under 2 percent of health budgets "
                 "on mental health. The workforce math is brutal: some "
                 "African countries have fewer than one psychiatrist per "
                 "million people. Task-shifting trials - training lay "
                 "counselors to deliver structured therapy - showed real "
                 "effects, yet scale-up stalled on funding and supervision. "
                 "Stigma keeps people from seeking care and governments from "
                 "funding it; insurance carve-outs and low reimbursement "
                 "keep providers scarce even where money exists. Digital "
                 "tools promise reach but the evidence for apps as "
                 "stand-alone treatment remains thin."),
  "why_it_matters": ("Mental disorders cost the global economy trillions in "
                     "lost productivity and cut lives short by a decade or "
                     "more through suicide and physical comorbidity. Closing "
                     "the gap is among the highest-return investments in "
                     "health - the treatments are cheap, the suffering is "
                     "vast."),
  "sig_lens": ("The Signature lens treats the gap as a delivery-design "
               "problem: the therapy works, the clinic model does not "
               "scale, so the care must be redesigned for the workforce "
               "that exists."),
  "sol_public": ("The Signature system proposes a stepped, task-shifted "
                 "mental-health grid: lay counselors delivering structured "
                 "therapy under remote specialist supervision, funded as "
                 "primary care, measured by recovery rates. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) structured therapies can be "
              "delivered faithfully by trained non-specialists - the trials "
              "say so; (2) the binding constraints are supervision, funding, "
              "and stigma, not efficacy; (3) integration into primary care "
              "beats standalone clinics for reach. Reasoning path: the "
              "psychiatrist-per-million math will not change in a decade, "
              "so any solution requiring specialists at the point of care "
              "is a fantasy. Task-shifting is the only arithmetic that "
              "works; the design problem is quality control at scale. "
              "Proposed mechanism: a three-step grid - community screening "
              "and peer support, lay-counselor structured therapy with "
              "remote specialist supervision via session sampling, and "
              "specialist referral for complex cases - funded inside "
              "primary-care budgets with recovery-rate accountability. "
              "What would confirm it: districts running the grid showing "
              "recovery rates matching specialist care at a fraction of "
              "the cost, sustained over years. What would kill it: "
              "quality collapse at scale - lay delivery degrading "
              "irrecoverably without in-person specialists. What it does "
              "NOT claim: that apps replace humans, that severe illness "
              "needs no specialists, or that this is proven. The honest "
              "unknown: the supervision ratio that holds quality - how "
              "many counselors per specialist."),
  "key_points": [
   "76-85 percent of people with serious mental disorders in poorer countries get no treatment; rich countries leave half unserved.",
   "Most countries spend under 2 percent of health budgets on mental health.",
   "Some countries have fewer than one psychiatrist per million people - the math rules out specialist-only care.",
   "Task-shifting trials show lay counselors can deliver structured therapy effectively.",
   "Stigma, funding, and supervision - not efficacy - are the binding constraints."],
  "requirements": [
   "Confirm: grid districts match specialist recovery rates at a fraction of the cost, sustained for years.",
   "Confirm: remote supervision via session sampling holds therapy quality at scale.",
   "Refute: quality collapse at scale without in-person specialists.",
   "Refute: no supervision ratio sustains quality - the grid degrading universally."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim apps replace humans or severe illness needs no specialists.",
   "The supervision ratio is the open measurement."],
  "citations": [CIT_MENTAL],
 },
 {
  "key": "maternal-disparities",
  "name": "Why Do Mothers Die at Such Different Rates?",
  "group": "Equity and Access",
  "ladder_rank": 10, "ladder_tier": "foundations",
  "description": ("A woman's lifetime risk of dying in childbirth ranges from "
                  "about 1 in 16,000 in the safest countries to 1 in 45 in "
                  "the most dangerous - a thousand-fold gap for a "
                  "physiological event every society manages. Even within "
                  "rich countries the gaps are stark: in the United States, "
                  "Black mothers die at three times the rate of white "
                  "mothers. Almost all of these deaths are preventable with "
                  "known care."),
  "problem": "Why do maternal death rates vary a thousand-fold when the life-saving care is fully known?",
  "background": ("Say and colleagues' 2014 analysis of global causes found "
                 "hemorrhage, hypertension, and sepsis - all treatable - "
                 "dominating maternal deaths, with the burden concentrated "
                 "where skilled birth attendance and emergency obstetric "
                 "care are absent. The US trend runs the wrong way: maternal "
                 "mortality rose for decades while most countries fell, and "
                 "the racial gap persists after adjusting for income and "
                 "education, pointing to care quality and bias, not just "
                 "resources. Interventions with strong evidence exist - "
                 "antenatal care, skilled attendance, emergency transport, "
                 "postpartum follow-up - yet coverage gaps, user fees, "
                 "distance, and disrespect in facilities keep women away or "
                 "arriving too late. The three-delays model (deciding to "
                 "seek care, reaching care, receiving adequate care) has "
                 "described the problem for thirty years without closing "
                 "it."),
  "why_it_matters": ("Every maternal death orphans children and scars a "
                     "community; the thousand-fold gap is the sharpest single "
                     "measure of global health inequity. Because the care is "
                     "known, every excess death is a system failure with a "
                     "named fix."),
  "sig_lens": ("The Signature lens treats maternal death as a chain-of-"
               "survival problem: the care exists in pieces, and mothers "
               "die in the gaps between the pieces."),
  "sol_public": ("The Signature system proposes closing the three delays as "
                 "one engineered chain: birth preparedness, guaranteed "
                 "emergency transport, and facility accountability for "
                 "respectful adequate care - audited by maternal death "
                 "surveillance. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) the clinical care is settled - the "
              "variable is the chain; (2) each delay is measurable - "
              "decision time, transport time, facility response time; (3) "
              "disrespect and bias are delay mechanisms, not side issues. "
              "Reasoning path: mothers die of hemorrhage waiting for "
              "transport, of eclampsia turned away at the door, of sepsis "
              "after a facility ignored warning signs - each a chain "
              "break, each timed. Proposed mechanism: a closed-loop "
              "maternity chain - every pregnancy registered, a transport "
              "guarantee (voucher, ambulance network, or community fund) "
              "activated by a single call, facilities scored publicly on "
              "response times and respectful care, and every maternal death "
              "reviewed with the findings binding on the chain. What would "
              "confirm it: districts running the closed loop showing "
              "maternal mortality falling toward the achievable floor with "
              "each delay's time shrinking. What would kill it: the chain "
              "closing on paper while deaths persist, implying the cause "
              "is clinical quality beyond the chain's reach. What it does "
              "NOT claim: that transport alone suffices, that bias "
              "training alone fixes care, or that this is proven. The "
              "honest unknown: which delay dominates in each setting - "
              "the chain must be measured before it is fixed."),
  "key_points": [
   "Lifetime risk of maternal death ranges from about 1 in 16,000 to 1 in 45 - a thousand-fold gap.",
   "Hemorrhage, hypertension, and sepsis dominate - all treatable (Say et al. 2014).",
   "In the US, Black mothers die at three times the rate of white mothers, beyond income and education.",
   "The three-delays model has described the problem for thirty years without closing it.",
   "Almost all maternal deaths are preventable with known care - each excess death is a system failure."],
  "requirements": [
   "Confirm: closed-loop districts drive maternal mortality toward the achievable floor.",
   "Confirm: each delay's measured time shrinks in step with the mortality decline.",
   "Refute: chains closing on paper while deaths persist - the clinical-quality refutation.",
   "Refute: a setting where no delay measurement predicts deaths, breaking the chain model."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim transport alone suffices or bias training alone fixes care.",
   "The dominant delay per setting is the open measurement."],
  "citations": [CIT_MATERNAL],
 },
 {
  "key": "chronic-care-gap",
  "name": "Why Does Prevention Lose to Treatment?",
  "group": "Aging and Chronic Care",
  "ladder_rank": 11, "ladder_tier": "foundations",
  "description": ("Preventing disease is cheaper and kinder than treating it, "
                  "yet health systems spend the overwhelming share of money "
                  "on treatment: McGlynn's landmark 2003 study found "
                  "Americans received only about half of recommended care, "
                  "with preventive care faring worst. The pattern repeats "
                  "worldwide - hospitals grow while prevention starves. "
                  "Everyone agrees prevention is better; the money disagrees."),
  "problem": "Why do health systems systematically underinvest in prevention despite its superior returns?",
  "background": ("Wagner's chronic care model in 1998 argued that health "
                 "systems designed for acute episodes cannot manage "
                 "long-term conditions, and the decades since have "
                 "confirmed it: fee-for-service pays for procedures, not "
                 "for the counseling, follow-up, and community work that "
                 "prevents them. Prevention's benefits are delayed, "
                 "diffuse, and accrue to other budgets - the insurer who "
                 "pays for smoking cessation may not insure the patient "
                 "when the heart attack is avoided. Political cycles reward "
                 "visible hospitals over invisible averted disease. "
                 "Behavioral economics adds the human side: patients and "
                 "clinicians both discount the future, skipping the "
                 "screening for the urgent complaint. Pay-for-performance "
                 "and capitation experiments show modest gains but have not "
                 "reversed the structural tilt."),
  "why_it_matters": ("The treatment tilt is why chronic disease keeps "
                     "winning: systems optimized for rescue will always be "
                     "outrun by preventable illness. Flipping the tilt is "
                     "the master key to every chronic-disease goal on this "
                     "list."),
  "sig_lens": ("The Signature lens treats prevention as an investment with "
               "a broken ownership chain: the payer, the beneficiary, and "
               "the time horizon never meet in the same budget."),
  "sol_public": ("The Signature system proposes prevention bonds with "
                 "cross-budget accounting: fund prevention from the budgets "
                 "that harvest its savings, with the returns measured and "
                 "returned. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) prevention's returns are real and "
              "measurable - the evidence base is strong; (2) the barrier is "
              "misaligned ownership, not missing evidence; (3) delayed "
              "rewards can be priced and traded. Reasoning path: if returns "
              "are real but unfunded, the market failure is in who captures "
              "them - so repair the capture. Proposed mechanism: "
              "prevention bonds and cross-budget pools - hospitals, "
              "insurers, and employers co-fund prevention programs, with "
              "independently measured averted costs returned to the fund; "
              "providers paid partly on population prevention metrics, not "
              "procedures. What would confirm it: funded prevention pools "
              "showing measured averted costs exceeding program costs over "
              "5-10 year horizons, with the tilt visibly shifting. What "
              "would kill it: prevention programs failing to show net "
              "savings under honest measurement, or payers refusing "
              "cross-budget deals even when profitable. What it does NOT "
              "claim: that all prevention saves money - some buys health "
              "at fair cost - or that this is proven. The honest unknown: "
              "the discount rate - how far into the future the system will "
              "actually pay for."),
  "key_points": [
   "Americans received only about half of recommended care; preventive care fared worst (McGlynn 2003).",
   "Fee-for-service pays for procedures, not for the counseling and follow-up that prevent them.",
   "Prevention's benefits are delayed, diffuse, and accrue to other budgets than the one that pays.",
   "Political cycles reward visible hospitals over invisible averted disease.",
   "Pay-for-performance experiments show modest gains; the structural tilt persists."],
  "requirements": [
   "Confirm: funded prevention pools show measured averted costs exceeding program costs over 5-10 years.",
   "Confirm: population prevention metrics in provider pay visibly shift the spending tilt.",
   "Refute: honest measurement showing prevention programs with no net savings or health gain.",
   "Refute: payers refusing cross-budget deals even when demonstrably profitable."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim all prevention saves money - some buys health at fair cost.",
   "The system's true discount rate on future health is the open measurement."],
  "citations": [CIT_CHRONIC],
 },
 {
  "key": "air-pollution-burden",
  "name": "What Is the True Cost of Dirty Air?",
  "group": "Global Systems",
  "ladder_rank": 12, "ladder_tier": "foundations",
  "description": ("Air pollution is the largest environmental risk factor for "
                  "disease: the Global Burden of Disease study attributes "
                  "millions of deaths a year to ambient and household air "
                  "pollution, rivaling tobacco. Yet it remains oddly "
                  "invisible in health policy - no patient is diagnosed "
                  "with air pollution, no hospital ward is named for it, "
                  "and its victims are counted by statistical models, not "
                  "death certificates."),
  "problem": "Why does the largest environmental health risk command so little health-system attention and funding?",
  "background": ("Cohen and colleagues' 2017 analysis traced 25-year trends "
                 "showing air pollution's toll rising in South and East Asia "
                 "even as it fell in rich countries that cleaned their air. "
                 "Lelieveld's work showed fossil-fuel combustion alone "
                 "drives a huge share of the burden - meaning climate policy "
                 "and health policy are the same policy. The attribution "
                 "problem is structural: a heart attack caused partly by "
                 "decades of PM2.5 exposure is recorded as a heart attack, "
                 "so the risk never appears in clinical data. Household air "
                 "pollution from cooking fires still harms billions, with "
                 "clean-stove programs repeatedly failing on adoption and "
                 "sustained use. Regulation works where applied - the US "
                 "Clean Air Act's benefits dwarf its costs - but the "
                 "politics of energy and transport keep it partial."),
  "why_it_matters": ("Cleaning air is among the fastest ways to extend "
                     "life expectancy at population scale, and the same "
                     "tons of emissions drive both the health burden and "
                     "climate change. Making the invisible visible would "
                     "unlock the largest win-win in public policy."),
  "sig_lens": ("The Signature lens treats dirty air as an unpriced "
               "exposure: the deaths are real, the emitters never see the "
               "bill, and the victims never get a diagnosis."),
  "sol_public": ("The Signature system proposes health-priced air: put the "
                 "measured health damage into every emissions decision - "
                 "permits, fuels, transport plans - so the bill lands where "
                 "the smoke starts. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) exposure-response science is strong "
              "enough to price health damage per ton; (2) the barrier is "
              "institutional - health agencies do not control energy "
              "permits; (3) co-benefits with climate make the economics "
              "overwhelming once priced. Reasoning path: the Clean Air Act "
              "proves regulation works when the health bill is made "
              "visible; the failure is that most emissions decisions are "
              "made by agencies that never see it. Proposed mechanism: a "
              "health-damage price on emissions - permits and fuel "
              "standards set with the per-ton mortality cost inside the "
              "calculation, household clean-cooking programs funded as "
              "health interventions with adoption engineered (not assumed), "
              "and air-quality health surveillance published like weather. "
              "What would confirm it: jurisdictions pricing health damage "
              "into permits showing faster pollution declines and "
              "measurable mortality drops than matched controls. What "
              "would kill it: priced damage failing to move emissions "
              "because energy politics override any price, or "
              "exposure-response proving too uncertain to price. What it "
              "does NOT claim: that pricing alone suffices without "
              "enforcement, or that this is proven. The honest unknown: "
              "the price level that actually moves the energy system."),
  "key_points": [
   "Air pollution is the largest environmental risk factor for disease, killing millions yearly.",
   "Fossil-fuel combustion drives a huge share - climate policy and health policy are the same policy.",
   "Victims are counted by statistical models, not death certificates; the risk is clinically invisible.",
   "The US Clean Air Act's health benefits dwarf its costs - regulation works where applied.",
   "Clean-stove programs repeatedly fail on adoption and sustained use."],
  "requirements": [
   "Confirm: health-priced permits accelerate pollution declines and cut mortality vs matched controls.",
   "Confirm: clean-cooking programs engineered for adoption sustain use and cut household exposure.",
   "Refute: priced damage failing to move emissions under real energy politics.",
   "Refute: exposure-response too uncertain to support per-ton pricing."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim pricing alone suffices without enforcement.",
   "The price level that moves the energy system is the open measurement."],
  "citations": [CIT_AIR],
 },
 {
  "key": "pandemic-prediction",
  "name": "Can We Predict the Next Pandemic?",
  "group": "Infectious Disease Control",
  "ladder_rank": 13, "ladder_tier": "compounded",
  "description": ("Most pandemics begin as animal viruses spilling into "
                  "people, yet we cannot say where, when, or which virus "
                  "will do it next. Jones and colleagues showed in 2008 "
                  "that emerging diseases are mostly zoonotic and "
                  "increasing, driven by land use and travel. Programs "
                  "like PREDICT sampled wildlife viruses by the thousands, "
                  "and the Global Virome Project proposed cataloging them "
                  "all - but prediction, the actual forecast of the next "
                  "spillover, remains beyond reach."),
  "problem": "Can the next pandemic be forecast in time to prevent it, or is prediction fundamentally out of reach?",
  "background": ("Morse and colleagues argued in 2012 that prediction and "
                 "prevention of the next pandemic zoonosis required "
                 "understanding the human-animal interface, not just "
                 "cataloging viruses. PREDICT, the USAID program, discovered "
                 "over a thousand new viruses and trained surveillance "
                 "capacity in 30 countries before its funding ended in "
                 "2020. Critics noted the paradox: discovering viruses "
                 "does not predict which will emerge, since emergence "
                 "depends on contact, opportunity, and chance as much as "
                 "on viral genetics. Hotspot mapping by Allen and "
                 "colleagues identified where emergence is likeliest, but "
                 "hotspots are large and spillover is rare per contact. "
                 "The field split between catalogers, modelers, and "
                 "preventionists - and the next pandemic arrived on "
                 "schedule, unpredicted in specifics."),
  "why_it_matters": ("The difference between prediction and surprise is the "
                     "difference between a contained outbreak and a "
                     "trillion-dollar catastrophe. Even imperfect "
                     "forecasting - narrowing where and what to watch - "
                     "would transform preparedness spending from guesswork "
                     "to targeting."),
  "sig_lens": ("The Signature lens treats prediction as a contact problem, "
               "not a virus-catalog problem: the question is not which "
               "virus exists but which human-animal contacts are about to "
               "become dangerous."),
  "sol_public": ("The Signature system proposes contact-risk forecasting: "
                 "monitor the interfaces - markets, farms, deforestation "
                 "fronts - for the contact patterns that precede "
                 "spillover, and forecast risk the way meteorologists "
                 "forecast storms. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) spillover requires contact plus "
              "opportunity plus viral compatibility - contact is the "
              "measurable term; (2) contact patterns change on observable "
              "schedules - new roads, new farms, new markets; (3) a "
              "forecast need not name the virus to be useful - a "
              "place-and-season risk map suffices. Reasoning path: virus "
              "catalogs grow but predictive power does not, because the "
              "virus is only one factor. The interface is where "
              "prediction lives: satellite-visible land change, "
              "market and farm registries, and syndromic signals in "
              "livestock and wildlife. Proposed mechanism: a spillover "
              "weather service - continuous ingestion of land-use change, "
              "animal-health signals, and human-interface activity into "
              "risk models that issue graded alerts (watch, warning) for "
              "places and seasons, triggering targeted surveillance and "
              "prevention. What would confirm it: alerts preceding "
              "real spillover events at rates beating chance and "
              "hotspot baselines, with prevention actions tied to "
              "alerts. What would kill it: spillovers consistently "
              "arriving without interface warning signs, or alerts so "
              "frequent they are ignored - the false-alarm death. What "
              "it does NOT claim: that any specific virus can be named "
              "in advance, or that this is proven. The honest unknown: "
              "the false-alarm tolerance - how many warnings the "
              "system can issue before they are tuned out."),
  "key_points": [
   "Most emerging diseases are zoonotic and increasing, driven by land use and travel (Jones et al. 2008).",
   "PREDICT discovered 1,000+ new viruses but could not say which would emerge.",
   "Emergence depends on contact, opportunity, and chance as much as on viral genetics.",
   "Hotspot maps identify likely regions, but hotspots are large and spillover is rare per contact.",
   "The field split between cataloging, modeling, and prevention - and the next pandemic arrived unpredicted."],
  "requirements": [
   "Confirm: interface-based alerts precede real spillovers, beating chance and hotspot baselines.",
   "Confirm: alert-triggered prevention actions measurably reduce spillover probability.",
   "Refute: spillovers arriving consistently without interface warning signs.",
   "Refute: alert frequency destroying credibility - the false-alarm death of the system."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim any specific virus can be named in advance.",
   "False-alarm tolerance is the open measurement."],
  "citations": [CIT_PREDICT],
 },
 {
  "key": "spillover-prevention",
  "name": "Can We Stop Zoonotic Spillover at the Source?",
  "group": "Infectious Disease Control",
  "ladder_rank": 14, "ladder_tier": "compounded",
  "description": ("If pandemics start at the human-animal interface, the "
                  "cheapest place to stop them is there - before the "
                  "virus reaches people. The IPBES 2020 workshop "
                  "estimated pandemic prevention at the source would cost "
                  "a tiny fraction of a single pandemic's damage. Yet "
                  "prevention at the source is the least funded link in "
                  "the chain: deforestation continues, wildlife trade "
                  "persists, and livestock intensification accelerates."),
  "problem": "Why is source-level pandemic prevention - the cheapest link - the least funded, and what would make it work?",
  "background": ("Plowright and colleagues mapped the pathways to spillover: "
                 "land-use change stressing wildlife, wildlife trade and "
                 "markets mixing species, and livestock systems bridging "
                 "wildlife and people. Each pathway is observable and, in "
                 "principle, interruptible: regulate high-risk trade, "
                 "protect forest buffers, improve farm biosecurity. The "
                 "IPBES pandemic report priced prevention at roughly two "
                 "orders of magnitude below pandemic cost - the best "
                 "bargain in public health. But the beneficiaries of "
                 "prevention are everyone while the costs fall on specific "
                 "industries and communities - loggers, traders, farmers - "
                 "who fight it. Conservation and health agencies rarely "
                 "share budgets or authority, so the interface belongs to "
                 "no one."),
  "why_it_matters": ("A prevented pandemic is worth trillions and millions "
                     "of lives; source prevention is also biodiversity "
                     "protection and climate policy in the same spending. "
                     "It is the rare intervention where the economics are "
                     "not in doubt - only the politics."),
  "sig_lens": ("The Signature lens treats spillover as an externality: the "
               "pandemic risk of a cleared forest or a wildlife market is "
               "never priced into the transaction that creates it."),
  "sol_public": ("The Signature system proposes pricing spillover risk into "
                 "the interface: spillover-risk bonds on high-risk land "
                 "conversion and trade, with the proceeds funding the "
                 "buffers and biosecurity that prevent it. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) spillover pathways are enumerable "
              "per landscape - markets, farms, forest frontiers; (2) the "
              "risk is priceable enough to bond; (3) the political barrier "
              "is concentrated costs vs diffuse benefits, solvable by "
              "compensation. Reasoning path: the IPBES arithmetic proves "
              "the bargain; the funding gap proves the politics. Make the "
              "risk visible in the transaction and compensate the losers. "
              "Proposed mechanism: spillover-risk bonds and interface "
              "compacts - high-risk land conversion and wildlife trade "
              "post bonds priced by pathway risk; the pool funds forest "
              "buffers, market hygiene upgrades, farm biosecurity, and "
              "livelihood alternatives for affected communities, with "
              "spillover surveillance as the audit. What would confirm "
              "it: bonded interfaces showing measured contact-risk "
              "declines and no compensating displacement to unbonded "
              "frontiers. What would kill it: risk proving unpriceable - "
              "spillover too rare and stochastic to bond - or displacement "
              "fully offsetting local gains. What it does NOT claim: that "
              "all spillover is preventable, that wildlife trade can be "
              "abolished by decree, or that this is proven. The honest "
              "unknown: the displacement rate - how much prevented risk "
              "simply moves."),
  "key_points": [
   "Spillover pathways - land change, wildlife trade, livestock bridging - are observable and interruptible.",
   "IPBES (2020): source prevention costs roughly two orders of magnitude less than a pandemic.",
   "Costs fall on specific industries and communities; benefits accrue to everyone - the political trap.",
   "Conservation and health agencies rarely share budgets or authority; the interface belongs to no one.",
   "Prevention at the source is the least funded link in the preparedness chain."],
  "requirements": [
   "Confirm: bonded interfaces show measured contact-risk declines without displacement.",
   "Confirm: bond pools sustain buffers, hygiene, and livelihood alternatives over years.",
   "Refute: spillover too rare and stochastic to price - the unbondable-risk refutation.",
   "Refute: full displacement of prevented risk to unbonded frontiers."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim all spillover is preventable or trade abolishable by decree.",
   "The displacement rate is the open measurement."],
  "citations": [CIT_SPILLOVER],
 },
 {
  "key": "health-equity",
  "name": "Why Does Your Zip Code Predict Your Lifespan?",
  "group": "Equity and Access",
  "ladder_rank": 15, "ladder_tier": "compounded",
  "description": ("In every country, the poor die younger - by years, "
                  "sometimes by decades. Chetty and colleagues showed "
                  "that in the US, the richest 1 percent outlive the "
                  "poorest 1 percent by 10 to 15 years, and the gap "
                  "varies dramatically by city: place matters as much as "
                  "income. The Marmot Commission called these the social "
                  "determinants of health. Yet decades of documentation "
                  "have not closed the gaps - in some places they are "
                  "widening."),
  "problem": "Why do health gaps by income and place persist - and widen - despite decades of measurement?",
  "background": ("The Whitehall studies of British civil servants in the "
                 "1970s first showed the gradient runs through the whole "
                 "social ladder, not just the poor. Marmot's WHO "
                 "Commission in 2008 framed the causes - the conditions "
                 "in which people are born, grow, live, work, and age - "
                 "and issued recommendations most governments filed away. "
                 "Chetty's 2016 JAMA study sharpened the puzzle: the "
                 "income-longevity gap differs enormously between American "
                 "cities, proving the gap is not destiny but policy and "
                 "place. Dwyer-Lindgren mapped county-level life "
                 "expectancy gaps exceeding 20 years within one country. "
                 "Interventions exist - early childhood programs, housing, "
                 "income support, education - but they live in other "
                 "ministries' budgets, measured on other timelines, while "
                 "health ministries count the bodies."),
  "why_it_matters": ("The gradient is the master fact of population health: "
                     "fix the conditions and you fix dozens of diseases at "
                     "once. Every health-equity gap that persists is "
                     "preventable death distributed by class and postcode."),
  "sig_lens": ("The Signature lens treats the gradient as a compounded-"
               "interest problem: advantage and disadvantage accrue daily "
               "across a lifetime, and health systems only meet people at "
               "the moment of accounting."),
  "sol_public": ("The Signature system proposes health-in-all-policies "
                 "accounting: every major policy - housing, transport, "
                 "wages, schooling - scored for its health-gradient "
                 "effect before adoption, with the gradient published "
                 "like inflation. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) the gradient's causes are "
              "mostly outside health care - conditions, not clinics; (2) "
              "governments optimize what they measure on their own "
              "timeline; (3) Chetty's city variation proves the gap is "
              "malleable. Reasoning path: health ministries cannot fix "
              "wages or zoning, and the ministries that can are never "
              "scored on health. Make the gradient visible in every "
              "ministry's accounts. Proposed mechanism: mandatory "
              "health-gradient impact scoring for major policies - "
              "housing, transport, labor, education - with county-level "
              "life-expectancy gaps published annually like economic "
              "statistics, and a cross-government equity fund that "
              "rewards measured gradient narrowing. What would confirm "
              "it: scored policies showing gradient-aware choices, and "
              "funded jurisdictions narrowing their gaps faster than "
              "controls. What would kill it: scoring that changes "
              "nothing - governments optimizing around the metric - or "
              "gradients proving immovable even under full "
              "cross-government effort. What it does NOT claim: that "
              "health care is irrelevant, that scoring alone changes "
              "politics, or that this is proven. The honest unknown: "
              "the time constant - how fast a narrowed policy gap "
              "becomes a narrowed health gap."),
  "key_points": [
   "The richest 1 percent outlive the poorest 1 percent by 10-15 years in the US (Chetty et al. 2016).",
   "The gap varies enormously by city - proving it is policy and place, not destiny.",
   "County-level life expectancy gaps exceed 20 years within one country.",
   "The gradient runs through the whole social ladder (Whitehall studies), not just the poor.",
   "Effective levers - early childhood, housing, income, education - live in other ministries' budgets."],
  "requirements": [
   "Confirm: scored policies shift toward gradient-narrowing choices vs unscored controls.",
   "Confirm: funded jurisdictions narrow life-expectancy gaps faster than matched controls.",
   "Refute: scoring changing nothing - optimization around the metric.",
   "Refute: gradients immovable under full cross-government effort."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim health care is irrelevant or scoring alone changes politics.",
   "The policy-to-health time constant is the open measurement."],
  "citations": [CIT_EQUITY],
 },
 {
  "key": "cold-chain",
  "name": "How Do We Get Vaccines to the Last Mile?",
  "group": "Global Systems",
  "ladder_rank": 16, "ladder_tier": "compounded",
  "description": ("Most vaccines must stay cold from factory to arm - 2 to 8 "
                  "degrees, unbroken, across deserts, jungles, and war "
                  "zones. The cold chain is one of public health's "
                  "greatest logistical achievements and its most fragile: "
                  "a single warm afternoon can destroy a village's "
                  "vaccines, and up to half of vaccines globally may be "
                  "lost to cold-chain failures. The last mile - the final "
                  "village, the final child - is where the chain most "
                  "often breaks."),
  "problem": "Why does the cold chain still fail at the last mile, and what would make vaccines survive it?",
  "background": ("The Expanded Programme on Immunization built the cold "
                 "chain from the 1970s onward - refrigerators, cold boxes, "
                 "ice packs, temperature monitors - and it works where "
                 "power and roads work. At the last mile, power is "
                 "intermittent, roads wash out, and the health worker "
                 "carries vaccines for hours in the heat. Lee and "
                 "colleagues modeled how thermostable vaccines would "
                 "transform reach, but most vaccines remain cold-dependent. "
                 "The controlled-temperature chain - allowing some "
                 "vaccines brief excursions out of cold - helped, as did "
                 "solar direct-drive refrigerators. Yet wastage rates "
                 "remain high, freeze damage (from over-chilling) ruins as "
                 "many doses as heat, and monitoring is spotty where it "
                 "matters most."),
  "why_it_matters": ("Every broken cold chain is a child who made the trip "
                     "but got a dead vaccine - the cruelest failure in "
                     "immunization. Fixing the last mile is the difference "
                     "between 80 percent coverage on paper and 80 percent "
                     "protected in reality."),
  "sig_lens": ("The Signature lens treats the last mile as a reliability "
               "engineering problem: the chain is only as strong as its "
               "weakest, hottest, most powerless link."),
  "sol_public": ("The Signature system proposes a last-mile redesign: "
                 "thermostable formulations where possible, passive "
                 "cold-chain devices with days of autonomy, and "
                 "sensor-verified potency at the point of use - so the "
                 "worker knows the dose is alive before giving it. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the failure is thermodynamic and "
              "logistical, not medical - the dose is fine until heat or "
              "freeze kills it; (2) health workers cannot be the "
              "refrigerator - the device must carry the burden; (3) "
              "potency verification at the point of use is now cheap "
              "enough to deploy. Reasoning path: every link that depends "
              "on perfect power and perfect handling at the last mile "
              "will fail there - so remove the dependence. Proposed "
              "mechanism: a three-layer last mile - accelerated "
              "thermostable formulations for the highest-burden vaccines, "
              "passive carriers holding temperature for days without "
              "power, and vial-level temperature indicators with potency "
              "verified by the worker's phone before administration, "
              "with wastage data feeding back to supply planning. What "
              "would confirm it: last-mile wastage collapsing and "
              "verified-potency coverage rising in pilot districts vs "
              "controls. What would kill it: thermostability proving "
              "unattainable for key vaccines, or indicators too costly "
              "or unreliable for field use. What it does NOT claim: that "
              "thermostability is near for all vaccines, or that this "
              "is proven. The honest unknown: the cost curve - whether "
              "the full stack is affordable at the scale of national "
              "programs."),
  "key_points": [
   "Most vaccines need 2-8 degrees unbroken from factory to arm; a warm afternoon can destroy a village's supply.",
   "Up to half of vaccines globally may be lost to cold-chain failures; freeze damage ruins as many as heat.",
   "The last mile - intermittent power, bad roads, hours on foot - is where the chain breaks.",
   "Controlled-temperature chain and solar refrigerators helped but wastage stays high.",
   "Thermostable vaccines would transform reach, but most vaccines remain cold-dependent."],
  "requirements": [
   "Confirm: pilot districts show collapsed wastage and rising verified-potency coverage vs controls.",
   "Confirm: vial-level indicators reliable and cheap enough for routine field use.",
   "Refute: thermostability unattainable for the highest-burden vaccines.",
   "Refute: the full stack unaffordable at national-program scale."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim thermostability is near for all vaccines.",
   "The cost curve at national scale is the open measurement."],
  "citations": [CIT_COLDCHAIN],
 },
 {
  "key": "aging-care-models",
  "name": "How Will Societies Care for Aging Populations?",
  "group": "Aging and Chronic Care",
  "ladder_rank": 17, "ladder_tier": "compounded",
  "description": ("The world is aging faster than any care system was built "
                  "for: by 2050, one in six people will be over 65, and in "
                  "many countries the share will be one in three or more. "
                  "The WHO's 2015 World Report on Ageing and Health "
                  "reframed the goal as healthy aging - functional ability, "
                  "not just years. But the care models - who provides "
                  "daily help, who pays, where it happens - are still "
                  "designed for a young world."),
  "problem": "What care model can support dignity and function for a world where the old outnumber the young?",
  "background": ("Beard and colleagues' Lancet analysis of the WHO report "
                 "stressed that aging is not a disease but a life stage, "
                 "and that functional ability depends on environments as "
                 "much as on bodies. The arithmetic is stark: old-age "
                 "dependency ratios are doubling and tripling; family "
                 "caregivers - mostly women - provide most long-term care "
                 "unpaid and unsupported; formal care workforces are "
                 "underpaid and scarce; and dementia prevalence doubles "
                 "every 20 years. Japan, the oldest society, experiments "
                 "with robotics and community care; Scandinavia with "
                 "universal home services; most of the world with nothing "
                 "at scale. Long-term care insurance exists in a handful "
                 "of countries. The models that work are small, local, and "
                 "unfunded for the coming wave."),
  "why_it_matters": ("How societies treat their oldest members is the "
                     "defining moral and fiscal question of the century: "
                     "get it wrong and aging becomes a crisis of "
                     "neglect and bankruptcy; get it right and the "
                     "longevity dividend pays for itself."),
  "sig_lens": ("The Signature lens treats aging care as a capacity "
               "problem with a dignity constraint: the need is "
               "predictable decades out, and the answer must preserve "
               "autonomy, not just extend supervision."),
  "sol_public": ("The Signature system proposes the functional-ability "
                 "grid: age-friendly environments, supported family "
                 "caregivers, community care teams, and long-term care "
                 "insurance - funded before the wave crests, measured by "
                 "years of independent function. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the demographic wave is "
              "predictable - the 2050 elderly are already born; (2) "
              "most care will always be informal - the model must "
              "support caregivers, not replace them; (3) function, not "
              "survival, is the outcome that matters. Reasoning path: "
              "no plausible workforce can institutionalize the coming "
              "wave, so the model must keep people functional at home "
              "longer and make caregiving sustainable. Proposed "
              "mechanism: a four-layer grid - age-friendly housing and "
              "transport that extend independent years, paid and trained "
              "family-caregiver support (respite, stipends, training), "
              "community care teams for the frail, and universal "
              "long-term-care insurance prefunded before the dependency "
              "peak. What would confirm it: grid districts showing more "
              "independent-function years per elder at sustainable cost "
              "vs institutional baselines. What would kill it: "
              "caregiver support failing to prevent burnout at scale, "
              "or prefunding proving politically impossible everywhere "
              "tried. What it does NOT claim: that robotics replaces "
              "human care, that aging can be medicalized away, or that "
              "this is proven. The honest unknown: the cost curve of "
              "supported home care at true population scale."),
  "key_points": [
   "By 2050 one in six people will be over 65; in many countries one in three or more.",
   "The WHO (2015) reframed the goal as healthy aging - functional ability, not just years.",
   "Family caregivers, mostly women, provide most long-term care unpaid and unsupported.",
   "Dementia prevalence doubles every 20 years; formal care workforces are scarce and underpaid.",
   "Working models are small, local, and unfunded for the coming wave."],
  "requirements": [
   "Confirm: grid districts deliver more independent-function years per elder at sustainable cost.",
   "Confirm: supported caregivers show lower burnout and longer care duration than unsupported.",
   "Refute: caregiver support failing to prevent burnout at population scale.",
   "Refute: prefunding politically impossible everywhere attempted."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim robotics replaces human care or aging can be medicalized away.",
   "The cost curve of supported home care at scale is the open measurement."],
  "citations": [CIT_AGING],
 },
 {
  "key": "opioid-crisis",
  "name": "Why Does the Overdose Crisis Keep Escalating?",
  "group": "Prevention and Behavior",
  "ladder_rank": 18, "ladder_tier": "compounded",
  "description": ("The overdose crisis has moved through waves - "
                  "prescription pills, then heroin, then illicit fentanyl - "
                  "each deadlier than the last, killing over 100,000 "
                  "Americans a year at its peak and spreading globally. "
                  "Crackdowns on one wave seeded the next: restricting "
                  "prescriptions pushed users to heroin; squeezing heroin "
                  "opened the door to fentanyl, 50 times more potent. "
                  "Every supply victory has been followed by a deadlier "
                  "adaptation."),
  "problem": "Why do supply crackdowns keep producing deadlier drug waves, and what actually reduces overdose deaths?",
  "background": ("Dasgupta and colleagues argued in 2018 that the crisis's "
                 "roots are social and economic - despair, pain, "
                 "disconnection - not just pills. Volkow's reviews traced "
                 "how the prescription wave (1990s-2010s) created a vast "
                 "dependent population; when prescribing tightened, the "
                 "market answered with heroin, then with illicitly "
                 "manufactured fentanyl that made every dose a lottery. "
                 "Ciccarone documented the iron law of prohibition: "
                 "enforcement selects for potency, because smugglers "
                 "maximize effect per smuggled gram. Naloxone distribution, "
                 "medication-assisted treatment, and supervised "
                 "consumption all show strong evidence - yet reach a "
                 "fraction of those at risk, while the policy debate "
                 "stays locked on supply."),
  "why_it_matters": ("Overdose is now a leading killer of young adults in "
                     "the hardest-hit countries, and the fentanyl playbook "
                     "is exportable worldwide. Understanding why "
                     "crackdowns backfire is the difference between "
                     "policies that save lives and policies that upgrade "
                     "the poison."),
  "sig_lens": ("The Signature lens treats the crisis as a hydra market: "
               "each severed supply head regrows more potent, because "
               "enforcement is the selection pressure."),
  "sol_public": ("The Signature system proposes flipping from supply war "
                 "to survival strategy: universal naloxone, treatment on "
                 "demand, safe supply pilots, and demand-side repair of "
                 "the despair underneath - measured in deaths averted, "
                 "not drugs seized. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) the iron law of prohibition holds "
              "- enforcement selects for potency; (2) demand is rooted in "
              "pain, trauma, and economic despair, not in drug "
              "availability alone; (3) dead people cannot recover - "
              "survival is the prerequisite intervention. Reasoning path: "
              "three waves prove that supply victories are pyrrhic; the "
              "jurisdictions with the lowest overdose deaths (Portugal, "
              "Switzerland) prioritized survival and treatment over "
              "seizures. Proposed mechanism: a survival-first stack - "
              "naloxone saturation (in every at-risk household and "
              "public space), medication-assisted treatment on demand "
              "with no waiting lists, supervised consumption and "
              "drug-checking to break the potency lottery, and "
              "parallel investment in the despair drivers (jobs, pain "
              "care, community). What would confirm it: stacked "
              "jurisdictions showing sustained overdose-death declines "
              "while supply-focused neighbors keep rising. What would "
              "kill it: survival measures failing to bend the curve "
              "where fully implemented, or safe-supply pilots "
              "expanding initiation. What it does NOT claim: that "
              "treatment alone ends the crisis, that enforcement is "
              "useless, or that this is proven. The honest unknown: "
              "the initiation rate under safe supply - whether it "
              "expands or merely displaces the market."),
  "key_points": [
   "The crisis moved in waves - pills, heroin, fentanyl - each deadlier than the last.",
   "The iron law of prohibition: enforcement selects for potency (Ciccarone 2019).",
   "Restricting prescriptions pushed users to heroin; squeezing heroin opened the door to fentanyl.",
   "Naloxone, medication-assisted treatment, and supervised consumption show strong evidence but low reach.",
   "Dasgupta (2018): roots are social and economic - despair, pain, disconnection - not just supply."],
  "requirements": [
   "Confirm: survival-stack jurisdictions show sustained overdose declines vs supply-focused neighbors.",
   "Confirm: naloxone saturation measurably cuts deaths per overdose event.",
   "Refute: full survival stacks failing to bend the curve.",
   "Refute: safe-supply pilots expanding initiation rates."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim treatment alone ends the crisis or enforcement is useless.",
   "Initiation under safe supply is the open measurement."],
  "citations": [CIT_OPIOID],
 },
 {
  "key": "diabetes-reversal",
  "name": "Can the Type 2 Diabetes Epidemic Be Reversed?",
  "group": "Aging and Chronic Care",
  "ladder_rank": 19, "ladder_tier": "compounded",
  "description": ("Over 400 million adults live with diabetes, most of it "
                  "type 2, and the number keeps climbing with the obesity "
                  "wave. For decades type 2 was taught as chronic and "
                  "progressive - manage it, never reverse it. Then the "
                  "DiRECT trial in 2018 showed structured weight "
                  "management put nearly half of recent-onset patients "
                  "into remission at one year. The biology allows "
                  "reversal; the system does not deliver it."),
  "problem": "If type 2 diabetes can be put into remission, why does the epidemic keep growing and remission stay rare?",
  "background": ("Taylor's twin-cycle hypothesis proposed that excess fat "
                 "in liver and pancreas drives the disease and that "
                 "removing it restores function - a mechanism the DiRECT "
                 "trial then confirmed in primary care: 46 percent "
                 "remission at one year with sustained weight loss, "
                 "against 4 percent with standard care. Bariatric surgery "
                 "had already shown remission was possible, but surgery "
                 "does not scale to hundreds of millions. The gap is "
                 "delivery: structured weight-management programs are "
                 "rare, underfunded, and poorly reimbursed; the food "
                 "environment that caused the weight gain is unchanged; "
                 "and clinical guidelines still emphasize glycemic "
                 "control over remission as the goal. Meanwhile new "
                 "GLP-1 drugs produce dramatic weight loss but at prices "
                 "and supply levels that cannot cover the epidemic."),
  "why_it_matters": ("Diabetes drives blindness, amputation, kidney "
                     "failure, and heart disease across the lifespan of "
                     "hundreds of millions. A scalable remission model "
                     "would convert the fastest-growing chronic disease "
                     "from a life sentence into a reversible condition."),
  "sig_lens": ("The Signature lens treats diabetes as a reversible "
               "state trapped by an irreversible system: the biology "
               "has an exit, but the clinic, the food environment, and "
               "the payment model block the door."),
  "sol_public": ("The Signature system proposes remission as the "
                 "default pathway: every new diagnosis enters a "
                 "structured remission program - nutrition, activity, "
                 "medication support - with the food environment and "
                 "payment model rebuilt around the exit. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the twin-cycle mechanism is "
              "correct for most early type 2 - remission is "
              "physiologically real; (2) the barrier is delivery "
              "economics and environment, not biology; (3) remission "
              "must be maintained for years to count. Reasoning path: "
              "DiRECT proves the exit exists in primary care; the "
              "question is why the door stays shut - programs are not "
              "funded, the food environment refills the fat, and "
              "guidelines aim at control. Proposed mechanism: a "
              "remission-default pathway - structured weight "
              "management offered at every new diagnosis with "
              "remission-rate accountability for clinics, "
              "GLP-1-class drugs reserved as program adjuncts with "
              "negotiated pricing, and food-environment measures "
              "that stop refilling the cycle. What would confirm "
              "it: pathway districts showing population remission "
              "rates an order of magnitude above standard care, "
              "sustained at five years. What would kill it: "
              "remission proving unmaintainable outside trials - "
              "weight regain erasing the exit at scale. What it does "
              "NOT claim: that all type 2 is reversible, that drugs "
              "alone solve it, or that this is proven. The honest "
              "unknown: the maintenance rate - what fraction stay in "
              "remission at ten years under real-world conditions."),
  "key_points": [
   "Over 400 million adults live with diabetes, mostly type 2, and numbers keep climbing.",
   "DiRECT (2018): structured weight management put 46 percent of recent-onset patients in remission at one year.",
   "Taylor's twin-cycle hypothesis: excess liver and pancreas fat drives the disease; removing it restores function.",
   "Remission programs are rare, underfunded, and poorly reimbursed; guidelines still aim at control.",
   "GLP-1 drugs work dramatically but cannot cover the epidemic at current prices and supply."],
  "requirements": [
   "Confirm: pathway districts show population remission rates far above standard care, sustained at five years.",
   "Confirm: clinic remission-rate accountability moves the default from control to remission.",
   "Refute: remission unmaintainable outside trials - weight regain erasing the exit at scale.",
   "Refute: the twin-cycle mechanism failing in major subgroups."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim all type 2 is reversible or drugs alone solve it.",
   "The ten-year maintenance rate is the open measurement."],
  "citations": [CIT_DIABETES],
 },
 {
  "key": "hypertension-control",
  "name": "Why Is the Leading Risk Factor the Least Controlled?",
  "group": "Aging and Chronic Care",
  "ladder_rank": 20, "ladder_tier": "compounded",
  "description": ("High blood pressure is the leading modifiable risk "
                  "factor for death worldwide - 1.28 billion adults have "
                  "it - and the treatment costs pennies a day with "
                  "drugs off patent for decades. Yet control rates are "
                  "dismal: in many countries fewer than one in five "
                  "hypertensives have it controlled. The cheapest, "
                  "best-understood intervention in chronic disease is "
                  "the one most often missed."),
  "problem": "Why does hypertension - cheap to treat, easy to measure - remain uncontrolled in most of the world?",
  "background": ("The NCD Risk Factor Collaboration's 2021 analysis of "
                 "hypertension in 184 countries found treatment and "
                 "control improving in rich countries but stagnating or "
                 "worsening across much of Africa, South Asia, and "
                 "Oceania. The drugs - thiazides, ACE inhibitors, "
                 "calcium-channel blockers - are generic, safe, and "
                 "pennies per day. The failure is pure systems: no "
                 "screening where people are, no refills without "
                 "monthly clinic visits, no registries to find the "
                 "lost-to-follow-up, and clinicians who do not "
                 "titrate. Frieden's HEARTS package showed the fix is "
                 "protocol-driven, team-based care with reliable drug "
                 "supply - demonstrated in India, Bangladesh, and Sri "
                 "Lanka at scale. The paradox stands: the better the "
                 "evidence and the cheaper the drug, the less excuse "
                 "remains, yet control lags."),
  "why_it_matters": ("Controlling blood pressure at population scale "
                     "would prevent more strokes and heart attacks than "
                     "almost any other single intervention - millions of "
                     "events a year, with drugs that cost less than a "
                     "cup of tea."),
  "sig_lens": ("The Signature lens treats hypertension as a logistics "
               "problem wearing a medical mask: the medicine is "
               "solved, the refill is not."),
  "sol_public": ("The Signature system proposes protocol-driven "
                 "hypertension grids: screening where people gather, "
                 "fixed-dose combinations, community refills, and "
                 "registries that chase the lost - with control rates "
                 "published like election results. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the pharmacology is settled - "
              "no new drug is needed; (2) the failure points are "
              "screening, titration, refills, and follow-up - all "
              "logistical; (3) protocols beat physician discretion at "
              "scale. Reasoning path: HEARTS proves the model works in "
              "poor settings; the question is why it is not the "
              "default everywhere. Proposed mechanism: a hypertension "
              "grid - opportunistic screening at every health contact "
              "plus community campaigns, standardized stepped "
              "protocols with fixed-dose combinations, 90-day "
              "prescriptions refilled by community health workers, "
              "and digital registries that flag every uncontrolled "
              "patient for outreach, with district control rates "
              "published quarterly. What would confirm it: grid "
              "districts reaching 70 percent control at low cost, "
              "sustained for years. What would kill it: adherence "
              "proving unfixable even with free drugs at the "
              "doorstep, or protocols failing across diverse "
              "populations. What it does NOT claim: that drugs "
              "alone suffice without salt and lifestyle measures, "
              "or that this is proven. The honest unknown: the "
              "adherence ceiling - the maximum control rate "
              "achievable in each setting."),
  "key_points": [
   "1.28 billion adults have hypertension; in many countries fewer than one in five is controlled.",
   "The drugs are generic, safe, and cost pennies a day - the pharmacology has been settled for decades.",
   "Failure points are screening, titration, refills, and follow-up - all logistical, not medical.",
   "Frieden's HEARTS package: protocol-driven, team-based care demonstrated at scale in South Asia.",
   "Control is improving in rich countries but stagnating across much of Africa, South Asia, and Oceania."],
  "requirements": [
   "Confirm: grid districts reach 70 percent control at low cost, sustained for years.",
   "Confirm: registries plus community refills recover the lost-to-follow-up at scale.",
   "Refute: adherence unfixable even with free drugs at the doorstep.",
   "Refute: protocols failing across diverse populations."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim drugs alone suffice without salt and lifestyle measures.",
   "The adherence ceiling per setting is the open measurement."],
  "citations": [CIT_HYPERTENSION],
 },
 {
  "key": "amr",
  "name": "Are We Headed for a Post-Antibiotic Era?",
  "group": "Infectious Disease Control",
  "ladder_rank": 21, "ladder_tier": "compounded",
  "description": ("Antibiotics underpin modern medicine - surgery, "
                  "chemotherapy, childbirth all assume treatable "
                  "infection - yet resistance is eroding them. Murray "
                  "and colleagues estimated 1.27 million deaths "
                  "directly attributable to bacterial antimicrobial "
                  "resistance in 2019, and the O'Neill Review warned "
                  "of 10 million a year by 2050 without action. The "
                  "drug pipeline is nearly dry: no major new class "
                  "for resistant Gram-negative bacteria in decades."),
  "problem": "Can the antibiotic era be preserved, or is a post-antibiotic age unavoidable?",
  "background": ("Resistance is evolution doing its job: every "
                 "antibiotic selects for the bacteria that survive it. "
                 "Overuse in human medicine - much of it for viral "
                 "illnesses antibiotics cannot treat - and mass use in "
                 "livestock as growth promoters accelerated the "
                 "process. Murray's 2022 Lancet study put AMR among the "
                 "leading causes of death globally, worse than HIV or "
                 "malaria in its toll. The economics are broken: a new "
                 "antibiotic is used sparingly by design, so it cannot "
                 "earn back its development cost - the market punishes "
                 "exactly the stewardship it needs. The WHO's 2015 "
                 "global action plan called for stewardship, "
                 "surveillance, and new drugs; progress on all three "
                 "has been slow, and last-resort drugs like "
                 "colistin now face resistant strains."),
  "why_it_matters": ("Losing antibiotics unwinds a century of medicine: "
                     "routine surgery becomes Russian roulette, "
                     "pneumonia becomes deadly again, and childbirth "
                     "carries its old risks. Preserving the antibiotic "
                     "era is preserving modernity itself."),
  "sig_lens": ("The Signature lens treats antibiotics as a "
               "commons: every use spends a shared, finite resource, "
               "and the market rewards spending it."),
  "sol_public": ("The Signature system proposes managing antibiotics "
                 "like a strategic reserve: delinked rewards for new "
                 "drugs, global stewardship with teeth, and "
                 "alternatives - phages, vaccines, diagnostics - that "
                 "reduce the draw on the reserve. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) resistance is inevitable "
              "evolution - the goal is slowing it, not stopping it; "
              "(2) the pipeline failure is economic, not scientific; "
              "(3) most selection pressure is measurable and "
              "modifiable - human overuse and agricultural use. "
              "Reasoning path: stewardship alone cannot outrun "
              "evolution without new drugs, and new drugs will not "
              "come while the market punishes them - so fix the "
              "market and the use together. Proposed mechanism: a "
              "strategic-reserve model - delinked pull incentives "
              "(subscription payments for new antibiotics regardless "
              "of volume), global stewardship standards with "
              "surveillance-enforced targets for human and "
              "agricultural use, rapid diagnostics to end empirical "
              "overprescribing, and accelerated alternatives (phage "
              "therapy, vaccines against resistant pathogens). What "
              "would confirm it: delinked incentives reviving the "
              "pipeline, and stewardship-plus-diagnostics bending "
              "resistance curves in participating systems. What "
              "would kill it: evolution outpacing even a revived "
              "pipeline - new drugs met by rapid resistance - or "
              "agricultural use proving politically untouchable "
              "everywhere. What it does NOT claim: that resistance "
              "can be reversed wholesale, that phages replace "
              "antibiotics soon, or that this is proven. The honest "
              "unknown: the sustainable use rate - how much "
              "antibiotic use the commons can bear indefinitely."),
  "key_points": [
   "1.27 million deaths were directly attributable to bacterial AMR in 2019 (Murray et al. 2022).",
   "The O'Neill Review warned of 10 million AMR deaths a year by 2050 without action.",
   "No major new class for resistant Gram-negative bacteria in decades - the pipeline is nearly dry.",
   "A new antibiotic used sparingly cannot earn back its cost - the market punishes stewardship.",
   "Overuse in human medicine and mass agricultural use accelerate resistance."],
  "requirements": [
   "Confirm: delinked incentives revive the antibiotic pipeline with licensed new classes.",
   "Confirm: stewardship plus diagnostics bend resistance curves in participating systems.",
   "Refute: evolution outpacing even a revived pipeline - rapid resistance to every new drug.",
   "Refute: agricultural use politically untouchable everywhere attempted."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim resistance can be reversed wholesale or phages replace antibiotics soon.",
   "The sustainable use rate of the commons is the open measurement."],
  "citations": [CIT_AMR],
 },
 {
  "key": "misinformation",
  "name": "Why Does Health Misinformation Outrun the Truth?",
  "group": "Prevention and Behavior",
  "ladder_rank": 22, "ladder_tier": "compounded",
  "description": ("False health claims travel faster and farther than "
                  "true ones: studies of online diffusion find "
                  "misinformation out-shared, out-liked, and "
                  "out-remembered, while corrections reach a fraction "
                  "of the audience and sometimes entrench the myth. The "
                  "WHO coined infodemic for the COVID-era flood. "
                  "Public health, built for pamphlets and press "
                  "conferences, is losing an information war fought on "
                  "platforms it does not control."),
  "problem": "Why does health misinformation systematically beat corrections, and what communication architecture could win?",
  "background": ("Kata's 2012 analysis of anti-vaccine web content "
                 "showed how misinformation mimics scientific form - "
                 "citations, experts, victim stories - while "
                 "optimizing for emotion and shareability. "
                 "Lewandowsky's reviews of misinformation correction "
                 "found the continued-influence effect: retractions "
                 "rarely fully erase the myth, and repeating the myth "
                 "to debunk it can reinforce it. Platform incentives "
                 "amplify the gap: engagement rewards outrage and "
                 "novelty, the exact properties of misinformation, "
                 "while accurate health guidance is boring by design. "
                 "Prebunking - inoculating audiences against "
                 "manipulation techniques - shows promise in trials "
                 "but has never been deployed at the scale of the "
                 "problem. Health agencies still communicate as if "
                 "the audience were rational and the channel neutral; "
                 "neither is true."),
  "why_it_matters": ("Misinformation now kills measurably - through "
                     "vaccine refusal, bogus cures, and distrust that "
                     "outlives any single outbreak. The information "
                     "environment is a health exposure as real as air "
                     "quality, and it is currently unregulated."),
  "sig_lens": ("The Signature lens treats misinformation as an "
               "adversarial information market: the lie is "
               "engineered for the platform's reward function, and "
               "the truth is not."),
  "sol_public": ("The Signature system proposes competing on the "
                 "platform's own terms: prebunking at population "
                 "scale, trusted-messenger networks, and friction "
                 "engineered into viral falsehoods - with the "
                 "information environment monitored like disease "
                 "surveillance. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) the asymmetry is structural - "
              "engagement incentives, not evil geniuses; (2) "
              "correction will always lag, so prevention "
              "(prebunking) must lead; (3) messengers matter more "
              "than messages. Reasoning path: fact-checking is "
              "whack-a-mole against an engagement-optimized "
              "adversary; the wins must come from changing the "
              "market - inoculating audiences, elevating trusted "
              "voices, adding friction to virality. Proposed "
              "mechanism: an infodemic defense stack - population-"
              "scale prebunking campaigns teaching manipulation "
              "techniques, standing networks of community trusted "
              "messengers activated in outbreaks, platform "
              "agreements for friction on viral health claims "
              "(context labels, share delays), and infodemic "
              "surveillance dashboards guiding response like "
              "epidemic curves. What would confirm it: stacked "
              "jurisdictions showing misinformation belief and "
              "harmful behavior declining vs controls during "
              "outbreaks. What would kill it: prebunking failing "
              "outside labs, or platforms proving unregulable - "
              "friction technically or legally impossible. What it "
              "does NOT claim: that censorship is the answer, that "
              "all misinformation is malicious, or that this is "
              "proven. The honest unknown: the durability of "
              "prebunking - how long inoculation lasts in a live "
              "feed."),
  "key_points": [
   "False health claims are out-shared and out-remembered; corrections reach a fraction of the audience.",
   "The continued-influence effect: retractions rarely fully erase the myth (Lewandowsky).",
   "Misinformation mimics scientific form while optimizing for emotion and shareability (Kata 2012).",
   "Platform engagement incentives structurally amplify misinformation over accurate guidance.",
   "Prebunking shows trial promise but has never been deployed at the scale of the problem."],
  "requirements": [
   "Confirm: stacked jurisdictions show misinformation belief and harmful behavior declining vs controls.",
   "Confirm: prebunking effects durable in live-feed conditions over months.",
   "Refute: prebunking failing outside laboratory settings.",
   "Refute: virality friction technically or legally impossible on major platforms."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim censorship is the answer or all misinformation is malicious.",
   "Prebunking durability is the open measurement."],
  "citations": [CIT_MISINFO],
 },
 {
  "key": "workforce-shortage",
  "name": "Who Will Staff the Health System?",
  "group": "Global Systems",
  "ladder_rank": 23, "ladder_tier": "compounded",
  "description": ("The WHO projects a shortfall of 10 million health "
                  "workers by 2030, concentrated where the disease "
                  "burden is heaviest. Rich countries fill their gaps "
                  "by recruiting from poor ones - a subsidy from the "
                  "sick to the healthy. Training pipelines take a "
                  "decade; burnout is emptying them faster than "
                  "schools fill them. The people who keep everyone "
                  "alive are running out."),
  "problem": "How can the world close a 10-million health-worker gap when training takes a decade and migration drains the poorest systems?",
  "background": ("The WHO's Global Strategy on Human Resources for "
                 "Health (Workforce 2030) set targets most countries "
                 "are missing. The maldistribution is extreme: Africa "
                 "bears a quarter of the disease burden with a few "
                 "percent of the workforce. International recruitment "
                 "codes exist but are weakly enforced; the flow from "
                 "poor to rich continues, with destination countries "
                 "saving billions in training costs. COVID-19 "
                 "accelerated burnout and exits across nursing and "
                 "primary care. Task-shifting and community health "
                 "workers extend reach, but supervision, pay, and "
                 "career paths remain broken - community workers are "
                 "often unpaid volunteers doing professional work. "
                 "The pipeline math does not close without structural "
                 "change."),
  "why_it_matters": ("Every health goal - vaccines, maternal survival, "
                     "chronic care, pandemic response - is a workforce "
                     "goal in disguise. A system without workers is a "
                     "plan without hands."),
  "sig_lens": ("The Signature lens treats the workforce as a "
               "circulation system with a leak: training flows one "
               "way, burnout drains the pool, and the poorest "
               "systems pay the training cost for the richest."),
  "sol_public": ("The Signature system proposes closing the loop: paid "
                 "community health workforces with career ladders, "
                 "retention bonds on international recruitment, and "
                 "training scaled to the burden - measured in "
                 "workers per thousand, not promises. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the gap cannot be trained "
              "away in time - redesign must extend every worker; (2) "
              "unpaid community work is exploitation, not a model; (3) "
              "migration follows money and will not stop - it must be "
              "priced. Reasoning path: the arithmetic of a decade-long "
              "pipeline against a 2030 deadline means the solution is "
              "part retention, part redesign, part fair circulation. "
              "Proposed mechanism: a workforce compact - every "
              "community health worker paid, supervised, and on a "
              "career ladder into nursing and midwifery; destination "
              "countries paying training-compensation bonds into "
              "source-country workforce funds; task-shifting protocols "
              "that legally extend each clinician's reach; and "
              "burnout measured and managed as a system metric. What "
              "would confirm it: compact regions showing workforce "
              "density rising toward need, retention improving, and "
              "coverage gains tracking the workforce gains. What would "
              "kill it: paid community models proving unaffordable at "
              "national scale, or compensation bonds rejected by every "
              "destination country. What it does NOT claim: that "
              "technology replaces workers, that migration can be "
              "banned, or that this is proven. The honest unknown: "
              "the affordable density - the workers-per-thousand "
              "each system can actually sustain."),
  "key_points": [
   "WHO projects a 10 million health-worker shortfall by 2030, concentrated where burden is heaviest.",
   "Africa bears a quarter of the disease burden with a few percent of the workforce.",
   "Rich countries recruit from poor ones - a training subsidy from the sick to the healthy.",
   "Training takes a decade; burnout is emptying pipelines faster than schools fill them.",
   "Community health workers extend reach but are often unpaid volunteers doing professional work."],
  "requirements": [
   "Confirm: compact regions raise workforce density toward need with improving retention.",
   "Confirm: coverage gains track workforce gains in compact districts.",
   "Refute: paid community models unaffordable at national scale everywhere tried.",
   "Refute: destination countries universally rejecting compensation bonds."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim technology replaces workers or migration can be banned.",
   "The affordable workers-per-thousand is the open measurement."],
  "citations": [CIT_WORKFORCE],
 },
 {
  "key": "tb-malaria-endgame",
  "name": "Why Haven't We Finished Off TB and Malaria?",
  "group": "Infectious Disease Control",
  "ladder_rank": 24, "ladder_tier": "compounded",
  "description": ("Tuberculosis and malaria are ancient, curable or "
                  "preventable, and still among the top infectious "
                  "killers - TB the leading single-pathogen killer "
                  "before COVID, malaria killing over half a million "
                  "a year, mostly African children. The tools exist: "
                  "drugs, diagnostics, bed nets, and now malaria "
                  "vaccines. The endgame - driving transmission to "
                  "zero - keeps receding."),
  "problem": "Why do curable, preventable ancient killers persist, and what would actually finish them?",
  "background": ("Bhatt and colleagues showed malaria control cut "
                 "African prevalence dramatically between 2000 and "
                 "2015 - bed nets, indoor spraying, and artemisinin "
                 "therapies working at scale. Then progress stalled: "
                 "insecticide and drug resistance spread, funding "
                 "flatlined, and the easy gains were banked. TB's "
                 "story is grimmer: drug-resistant strains now "
                 "resist first- and second-line drugs, treatment "
                 "takes months, and case-finding misses millions "
                 "each year. The WHO's End TB Strategy targets "
                 "elimination, but the last mile of any disease is "
                 "the hardest - each remaining case is harder to "
                 "find and costlier to cure than the last. New "
                 "malaria vaccines (RTS,S, R21) add a powerful tool, "
                 "but delivery at scale is unproven."),
  "why_it_matters": ("TB and malaria are the proof-of-concept for "
                     "disease elimination: if the world cannot finish "
                     "diseases it can cure and prevent, the grander "
                     "eradication ambitions are fantasy. Millions of "
                     "preventable deaths a year hang on the answer."),
  "sig_lens": ("The Signature lens treats the endgame as a "
               "last-mile economics problem: the cost per case "
               "averted rises as cases fall, and funding built for "
               "the cheap middle cannot survive the expensive end."),
  "sol_public": ("The Signature system proposes endgame financing "
                 "and finding: dedicated last-mile funds that grow as "
                 "cases shrink, active case-finding with new "
                 "diagnostics, and resistance surveillance - so the "
                 "final cases are hunted, not waited for. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the tools suffice for "
              "elimination in most settings - the gap is delivery "
              "and durability; (2) resistance is the moving target "
              "that can undo gains; (3) the last mile needs "
              "different economics than the mass campaign. "
              "Reasoning path: the stall after 2015 proves that "
              "mass tools plateau; the endgame needs hunting - "
              "finding the missed millions - and financing that "
              "increases per case as cases fall. Proposed "
              "mechanism: endgame compacts per region - active "
              "case-finding with molecular diagnostics and "
              "contact investigation, malaria vaccines layered "
              "onto vector control, resistance surveillance "
              "triggering regimen switches, and last-mile funds "
              "with per-case budgets that rise as incidence "
              "falls. What would confirm it: compact regions "
              "driving incidence to near zero and holding it "
              "against importation. What would kill it: "
              "resistance outpacing every regimen - untreatable "
              "TB or untreatable malaria at scale - or "
              "last-mile costs proving politically unfundable "
              "everywhere. What it does NOT claim: that "
              "eradication is near, that vaccines alone finish "
              "malaria, or that this is proven. The honest "
              "unknown: the true last-mile cost per case in "
              "each setting."),
  "key_points": [
   "TB and malaria remain top infectious killers despite curable, preventable tools.",
   "Malaria control cut African prevalence sharply 2000-2015 (Bhatt et al.), then stalled on resistance and flat funding.",
   "Drug-resistant TB resists first- and second-line drugs; treatment takes months; millions of cases are missed yearly.",
   "New malaria vaccines (RTS,S, R21) add power, but delivery at scale is unproven.",
   "The last mile is the hardest: each remaining case is costlier to find and cure."],
  "requirements": [
   "Confirm: compact regions drive incidence to near zero and hold it against importation.",
   "Confirm: active case-finding finds the missed millions at feasible cost.",
   "Refute: resistance outpacing every regimen - untreatable disease at scale.",
   "Refute: last-mile costs politically unfundable everywhere attempted."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim eradication is near or vaccines alone finish malaria.",
   "The true last-mile cost per case is the open measurement."],
  "citations": [CIT_TBMAL],
 },
 {
  "key": "one-health",
  "name": "Can Human, Animal, and Environmental Health Be Governed Together?",
  "group": "Global Systems",
  "ladder_rank": 25, "ladder_tier": "advanced",
  "description": ("Most human infections come from animals, most food "
                  "comes from managed ecosystems, and most health "
                  "threats - pandemics, antimicrobial resistance, "
                  "foodborne disease - cross the human-animal-"
                  "environment boundary. One Health is the idea that "
                  "these must be governed together. The 2022 One Health "
                  "Joint Plan of Action by WHO, FAO, WOAH, and UNEP "
                  "finally gave it institutional form - but ministries, "
                  "budgets, and data systems remain stubbornly separate."),
  "problem": "Why does One Health remain a slogan rather than a working governance system, and what would make it real?",
  "background": ("Zinsstag and colleagues formalized One Health theory: "
                 "human, animal, and ecosystem health are one "
                 "interdependent system, and interventions at the "
                 "interface beat siloed ones - rabies control through "
                 "dog vaccination is cheaper and more effective than "
                 "treating human bites. The quadripartite Joint Plan of "
                 "Action (2022) committed the four agencies to joint "
                 "work. Yet on the ground, the veterinarian, the "
                 "physician, and the ecologist report to different "
                 "ministers, compete for different budgets, and cannot "
                 "see each other's data. Antimicrobial use in "
                 "agriculture - a One Health textbook case - remains "
                 "largely outside health governance. The concept is "
                 "thirty years old; the institutions are four."),
  "why_it_matters": ("The next pandemic, the resistance crisis, and the "
                     "food-safety burden all live at the interface. "
                     "Governing the interface is governing the "
                     "largest shared risks humanity faces - separately, "
                     "we keep being surprised by the same boundary."),
  "sig_lens": ("The Signature lens treats One Health as a boundary-"
               "ownership problem: the risks live in the gaps between "
               "ministries, and nobody is paid to watch the gaps."),
  "sol_public": ("The Signature system proposes interface institutions: "
                 "joint human-animal-environment surveillance, pooled "
                 "interface budgets, and shared data - with the "
                 "interface owned, measured, and funded as one system. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) interface risks are "
              "systematically under-governed because they fall between "
              "mandates; (2) joint surveillance and response are "
              "provably more cost-effective (rabies, avian flu); (3) "
              "data sharing is the technical prerequisite. Reasoning "
              "path: the Joint Plan of Action provides the mandate; "
              "the missing pieces are pooled money and shared "
              "visibility at country level. Proposed mechanism: "
              "national One Health compacts - a joint surveillance "
              "platform ingesting human, veterinary, and "
              "environmental signals; a pooled interface budget that "
              "no single ministry can raid; and joint response teams "
              "with authority across the boundary, exercised in "
              "simulations and real events. What would confirm it: "
              "compact countries detecting and containing interface "
              "events faster and cheaper than siloed neighbors. What "
              "would kill it: ministries refusing to pool budgets or "
              "share data even under compact agreements - the "
              "sovereignty refutation. What it does NOT claim: that "
              "One Health replaces sectoral health systems, that "
              "governance alone stops spillover, or that this is "
              "proven. The honest unknown: the minimum viable "
              "institution - how little joint structure suffices."),
  "key_points": [
   "Most human infections come from animals; pandemics, AMR, and foodborne disease all cross the boundary.",
   "Rabies control via dog vaccination beats treating human bites - the textbook One Health win.",
   "The 2022 quadripartite Joint Plan of Action gave One Health institutional form.",
   "Veterinarians, physicians, and ecologists report to different ministers, budgets, and data systems.",
   "Agricultural antimicrobial use remains largely outside health governance."],
  "requirements": [
   "Confirm: compact countries detect and contain interface events faster and cheaper than siloed neighbors.",
   "Confirm: pooled interface budgets survive political cycles without being raided.",
   "Refute: ministries refusing to pool budgets or share data under compact agreements.",
   "Refute: joint surveillance adding no speed over siloed systems."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim One Health replaces sectoral systems or governance alone stops spillover.",
   "The minimum viable joint institution is the open measurement."],
  "citations": [CIT_ONEHEALTH],
 },
 {
  "key": "uhc-financing",
  "name": "How Do You Finance Universal Health Coverage?",
  "group": "Global Systems",
  "ladder_rank": 26, "ladder_tier": "advanced",
  "description": ("Universal health coverage - everyone getting the care "
                  "they need without financial ruin - is the world's "
                  "agreed health goal, yet nearly a billion people face "
                  "catastrophic health spending and over half the world "
                  "lacks full coverage of essential services. The "
                  "medicine is known; the money is not. Every country "
                  "must answer: who pays, for what, and how do the poor "
                  "avoid the bill."),
  "problem": "What financing architecture actually delivers universal coverage without bankrupting states or patients?",
  "background": ("Wagstaff and colleagues documented the financial "
                 "protection crisis: hundreds of millions pushed into "
                 "poverty yearly by health payments, with the trend "
                 "worsening in some regions. The financing debate has "
                 "run for decades: tax-funded systems (UK, Scandinavia) "
                 "achieve universality but need broad tax bases; social "
                 "health insurance (Germany, Japan, Thailand) covers "
                 "formal workers first and struggles with informal "
                 "economies; community insurance rarely scales. "
                 "Thailand's 2002 universal coverage reform showed a "
                 "middle-income country could do it - through general "
                 "taxation, a defined benefit package, and strategic "
                 "purchasing. Rwanda's community-based insurance showed "
                 "another path. But most low-income countries face the "
                 "same wall: narrow tax bases, huge informal sectors, "
                 "and donor dependence that evaporates."),
  "why_it_matters": ("Financing is the operating system of every other "
                     "health goal: without it, vaccines, maternal care, "
                     "and chronic treatment are promises without "
                     "budgets. The right architecture decides whether "
                     "illness means treatment or ruin."),
  "sig_lens": ("The Signature lens treats UHC financing as a risk-"
               "pooling problem with a political constraint: the pool "
               "must be big enough to share risk and legitimate enough "
               "to collect."),
  "sol_public": ("The Signature system proposes the pooled-purchaser "
                 "model: general-revenue financing, a defined essential "
                 "package, and one strategic purchaser per population - "
                 "with financial protection measured and published. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) risk pooling requires the "
              "largest possible pool - fragmentation is the enemy; (2) "
              "informal economies rule out contribution-based models as "
              "the primary base; (3) the benefit package must be "
              "explicit and costed, or universality is a slogan. "
              "Reasoning path: Thailand proves general-revenue "
              "financing works at middle income; the design problem is "
              "adapting it to narrow tax bases and donor dependence. "
              "Proposed mechanism: a pooled-purchaser architecture - "
              "general taxation (plus earmarked health taxes on "
              "tobacco, alcohol, sugary drinks) funding a single "
              "national pool; a defined, costed essential package; "
              "one strategic purchaser contracting public and "
              "private providers on performance; catastrophic-"
              "spending rates published like inflation, with "
              "political accountability. What would confirm it: "
              "adopting countries showing catastrophic spending "
              "falling toward zero while service coverage rises, "
              "on sustainable domestic revenue. What would kill "
              "it: tax bases too narrow to fund the package "
              "anywhere tried, or strategic purchasing captured "
              "by provider interests. What it does NOT claim: that "
              "one model fits all countries, that donor money is "
              "unnecessary in transition, or that this is proven. "
              "The honest unknown: the minimum revenue base - how "
              "poor a country can be and still fund the package."),
  "key_points": [
   "Nearly a billion people face catastrophic health spending; over half the world lacks full essential coverage.",
   "Hundreds of millions are pushed into poverty yearly by health payments (Wagstaff et al.).",
   "Tax-funded and social-insurance models each have universality paths and limits; community insurance rarely scales.",
   "Thailand (2002) showed a middle-income country can achieve UHC via general taxation and strategic purchasing.",
   "Narrow tax bases, informal economies, and donor dependence wall off most low-income countries."],
  "requirements": [
   "Confirm: adopting countries drive catastrophic spending toward zero with rising coverage on domestic revenue.",
   "Confirm: earmarked health taxes sustainably widen the revenue base.",
   "Refute: tax bases too narrow to fund the package anywhere attempted.",
   "Refute: strategic purchasing universally captured by provider interests."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim one model fits all or donor money is unnecessary in transition.",
   "The minimum viable revenue base is the open measurement."],
  "citations": [CIT_UHC],
 },
 {
  "key": "postviral-syndromes",
  "name": "What Causes Post-Viral Syndromes Like Long COVID?",
  "group": "Aging and Chronic Care",
  "ladder_rank": 27, "ladder_tier": "advanced",
  "description": ("Long COVID showed the world what patients with ME/CFS "
                  "had reported for decades: a viral infection can leave "
                  "months or years of fatigue, brain fog, dysautonomia, "
                  "and pain, with normal test results and no agreed "
                  "mechanism. Davis and colleagues estimated hundreds of "
                  "millions affected worldwide. Post-viral syndromes are "
                  "now one of the largest chronic-disease burdens - and "
                  "among the least understood."),
  "problem": "What biological mechanism drives post-viral syndromes, and why do standard tests miss it?",
  "background": ("Post-viral fatigue syndromes were described after "
                 "influenza, SARS, Ebola, and Epstein-Barr long before "
                 "COVID, but research funding was minimal and patients "
                 "were often disbelieved. Long COVID changed the scale: "
                 "with hundreds of millions infected, even a small "
                 "percentage with persistent symptoms became a "
                 "population catastrophe. Davis's 2023 review mapped "
                 "candidate mechanisms - viral persistence, immune "
                 "dysregulation, autoimmunity, endothelial and clotting "
                 "abnormalities, microbiome disruption, autonomic "
                 "dysfunction - each with supporting evidence, none "
                 "sufficient. Nalbandian's clinical reviews showed "
                 "multi-organ involvement defying single-specialty "
                 "care. Trials of antivirals, immunomodulators, and "
                 "rehabilitation show hints, not answers. The field is "
                 "where AIDS research was in 1983: a syndrome in "
                 "search of its mechanism."),
  "why_it_matters": ("Hundreds of millions of people live diminished "
                     "lives with a disease medicine cannot yet explain "
                     "or treat. Finding the mechanism would unlock "
                     "treatments for long COVID and validate decades "
                     "of dismissed patients with ME/CFS and related "
                     "syndromes."),
  "sig_lens": ("The Signature lens treats post-viral syndromes as a "
               "control-systems failure: the infection ends, but the "
               "body's regulatory loops never return to their "
               "setpoints."),
  "sol_public": ("The Signature system proposes mechanism-first "
                 "research at scale: deep phenotyping of large "
                 "patient cohorts against recovered controls, with "
                 "the leading mechanisms tested in platform trials "
                 "- so the syndrome is solved like a system, not a "
                 "symptom. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) post-viral syndromes are "
              "biological, not psychological - the multi-organ "
              "evidence says so; (2) the mechanism is likely "
              "plural - different drivers in different patients; "
              "(3) normal standard tests mean the tests are wrong, "
              "not the patients. Reasoning path: single-mechanism "
              "hunting has failed for decades; the syndrome needs "
              "systems phenotyping - immune, vascular, autonomic, "
              "microbial - at a scale that can stratify patients "
              "into mechanistic subtypes. Proposed mechanism: a "
              "post-viral observatory - tens of thousands of "
              "patients deeply phenotyped longitudinally against "
              "recovered controls, machine-stratified into "
              "mechanistic subtypes (persistent-viral, autoimmune, "
              "endothelial, dysautonomic), each subtype routed to "
              "platform trials of targeted interventions. What "
              "would confirm it: stable subtypes with distinct "
              "biomarkers, and subtype-targeted treatments "
              "outperforming one-size-fits-all care. What would "
              "kill it: no stable subtypes emerging at any "
              "phenotyping depth - the syndrome proving "
              "irreducibly heterogeneous - or all candidate "
              "mechanisms refuted in well-powered trials. What it "
              "does NOT claim: that the mechanism is known, that "
              "any current treatment is proven, or that "
              "stratification will be simple. The honest unknown: "
              "whether the subtypes are few or many - the "
              "granularity of the answer."),
  "key_points": [
   "Long COVID affects an estimated hundreds of millions worldwide (Davis et al. 2023).",
   "Post-viral syndromes were described after influenza, SARS, Ebola, and EBV - long dismissed and underfunded.",
   "Candidate mechanisms: viral persistence, immune dysregulation, autoimmunity, endothelial dysfunction, dysautonomia.",
   "Multi-organ involvement defies single-specialty care (Nalbandian et al.).",
   "Standard tests are normal - the tests are inadequate, not the patients."],
  "requirements": [
   "Confirm: stable mechanistic subtypes with distinct biomarkers emerge from deep phenotyping.",
   "Confirm: subtype-targeted treatments outperform one-size-fits-all care in platform trials.",
   "Refute: no stable subtypes at any phenotyping depth - irreducible heterogeneity.",
   "Refute: all leading mechanisms refuted in well-powered trials."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim the mechanism is known or any current treatment proven.",
   "Subtype granularity is the open measurement."],
  "citations": [CIT_POSTVIRAL],
 },
 {
  "key": "climate-adaptation",
  "name": "How Do Health Systems Adapt to a Changing Climate?",
  "group": "Global Systems",
  "ladder_rank": 28, "ladder_tier": "advanced",
  "description": ("The Lancet Countdown documents the toll rising year "
                  "by year: heat deaths climbing, dengue and malaria "
                  "vectors expanding their range, crop failures "
                  "threatening nutrition, floods destroying clinics. "
                  "Health systems built for a stable climate now face "
                  "a moving target - and adaptation planning lags far "
                  "behind mitigation debate."),
  "problem": "What does a climate-resilient health system look like, and why is adaptation so far behind?",
  "background": ("Watts and colleagues' annual Lancet Countdown reports "
                 "have tracked heat-related mortality rising for two "
                 "decades, with the elderly and outdoor workers hit "
                 "hardest. Ebi's reviews showed health adaptation "
                 "needs span early warning, vector control, water "
                 "security, nutrition, and mental health - nearly the "
                 "whole public-health portfolio, under new extremes. "
                 "Yet national adaptation plans rarely include "
                 "health-sector specifics; climate finance flows "
                 "overwhelmingly to mitigation and energy, not to "
                 "clinics and surveillance. Heat action plans (as in "
                 "Ahmedabad) prove early warning saves lives, but "
                 "few cities have them. Hospitals themselves are "
                 "vulnerable - flooded, overheated, powerless in the "
                 "storms they must respond to."),
  "why_it_matters": ("Climate change is now a health exposure affecting "
                     "billions, and its health burden will exceed many "
                     "diseases on this list. Adaptation is the difference "
                     "between a managed transition and cascading health "
                     "crises."),
  "sig_lens": ("The Signature lens treats climate adaptation as "
               "stress-testing: the health system must be engineered "
               "for the extremes it will face, not the averages it "
               "was built for."),
  "sol_public": ("The Signature system proposes climate-proofing as "
                 "a health discipline: heat early-warning everywhere, "
                 "resilient facilities, climate-informed surveillance, "
                 "and adaptation finance scored by lives protected. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the direction of change is "
              "certain enough to engineer for - hotter, more "
              "extreme, shifting vectors; (2) adaptation is "
              "mostly repurposed public health - warning, "
              "surveillance, infrastructure - not new science; (3) "
              "the binding constraint is finance and mandate, not "
              "knowledge. Reasoning path: Ahmedabad's heat plan "
              "proves the interventions work; the gap is that "
              "almost no health system is required to have one. "
              "Proposed mechanism: mandatory climate-resilience "
              "standards for health systems - heat early-warning "
              "in every at-risk city, facilities hardened "
              "against flood, heat, and outage, disease "
              "surveillance fused with climate forecasts, and "
              "adaptation finance with health outcomes in its "
              "scoring. What would confirm it: standardized "
              "districts showing lower climate-attributable "
              "mortality and faster post-disaster service "
              "recovery than controls. What would kill it: "
              "extremes exceeding engineered tolerances "
              "everywhere - adaptation physically impossible "
              "beyond some threshold - or finance never "
              "materializing at any advocacy level. What it does "
              "NOT claim: that adaptation substitutes for "
              "mitigation, that all impacts are adaptable, or "
              "that this is proven. The honest unknown: the "
              "adaptation limit - the warming level beyond which "
              "health systems cannot cope."),
  "key_points": [
   "The Lancet Countdown tracks heat deaths, expanding vector ranges, and nutrition threats rising yearly.",
   "Heat action plans (Ahmedabad) prove early warning saves lives - few cities have them.",
   "Adaptation needs span the whole public-health portfolio under new extremes (Ebi et al.).",
   "Climate finance flows overwhelmingly to mitigation, not to clinics and surveillance.",
   "Hospitals themselves are vulnerable - flooded, overheated, powerless in the storms they must answer."],
  "requirements": [
   "Confirm: standardized districts show lower climate-attributable mortality than controls.",
   "Confirm: hardened facilities recover services faster post-disaster.",
   "Refute: extremes exceeding engineered tolerances everywhere - the physical adaptation limit.",
   "Refute: adaptation finance never materializing at any advocacy level."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim adaptation substitutes for mitigation.",
   "The warming level beyond which systems cannot cope is the open measurement."],
  "citations": [CIT_CLIMATE],
 },
 {
  "key": "health-data-interop",
  "name": "Why Can't Health Records Talk to Each Other?",
  "group": "Global Systems",
  "ladder_rank": 29, "ladder_tier": "advanced",
  "description": ("A patient's records are scattered across clinics, "
                  "hospitals, labs, and pharmacies that cannot exchange "
                  "them - in rich countries with billion-dollar systems "
                  "and in poor ones with paper registers alike. "
                  "Mandl and Kohane called the electronic health record "
                  "a trap: digitization without interoperability "
                  "reproduced the fragmentation in silicon. The "
                  "result is duplicated tests, missed allergies, "
                  "broken care continuity, and surveillance blind to "
                  "its own data."),
  "problem": "Why has decades of health IT investment not produced interoperable records, and what architecture would?",
  "background": ("The US spent tens of billions incentivizing EHR "
                 "adoption, yet hospitals still fax records and "
                 "patients carry CDs of their own scans. "
                 "Adler-Milstein's work showed health information "
                 "exchange lagging because vendors profit from lock-in "
                 "and providers gain no revenue from sharing. The HL7 "
                 "FHIR standard finally offered a modern API "
                 "framework, and regulations now mandate patient "
                 "access APIs - progress, but exchange between "
                 "institutions remains patchy. In low-income "
                 "settings, DHIS2 and paper registers coexist, and "
                 "the bigger gap is digitization itself. Privacy "
                 "fears, real and invoked, block sharing that "
                 "patients would want. The technical problem was "
                 "solved years ago; the incentive problem was not."),
  "why_it_matters": ("Interoperability is the nervous system every "
                     "other goal needs: surveillance, chronic care, "
                     "maternal chains, and pandemic response all fail "
                     "on fragmented data. The data exists; it just "
                     "cannot move."),
  "sig_lens": ("The Signature lens treats interoperability as an "
               "incentive problem wearing a technical mask: the "
               "standard exists, the will to implement it does not "
               "pay."),
  "sol_public": ("The Signature system proposes patient-mediated "
                 "interoperability: the patient holds the key, open "
                 "APIs are mandatory, and data blocking is penalized "
                 "- with privacy enforced by design, not by "
                 "obstruction. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) FHIR-class APIs are "
              "technically sufficient - no new standard is needed; "
              "(2) vendors and providers block sharing because "
              "it pays to block; (3) patients want their data to "
              "move. Reasoning path: the decades of failure are "
              "not a standards problem, so another standard will "
              "not fix it - only changed payoffs will. Proposed "
              "mechanism: patient-mediated exchange as the "
              "default - every record accessible to the patient "
              "via open API, sharing consent managed by the "
              "patient, data-blocking penalized financially, and "
              "a public interoperability scorecard per "
              "institution, with privacy protected by "
              "purpose-limited access and audit, not by refusing "
              "to share. What would confirm it: scored "
              "jurisdictions showing record-exchange rates and "
              "care-continuity measures rising with penalties "
              "and scorecards. What would kill it: blocking "
              "proving technically unavoidable - legacy systems "
              "incapable of APIs at any price - or privacy "
              "breaches destroying public consent for sharing. "
              "What it does NOT claim: that technology alone "
              "suffices, that privacy concerns are trivial, or "
              "that this is proven. The honest unknown: the "
              "penalty level that makes blocking unprofitable."),
  "key_points": [
   "Records are fragmented across institutions in rich and poor countries alike.",
   "The US spent tens of billions on EHR adoption; hospitals still fax records.",
   "Vendors profit from lock-in; providers gain no revenue from sharing (Adler-Milstein).",
   "FHIR offers a modern API framework and access mandates exist - institutional exchange stays patchy.",
   "The technical problem was solved years ago; the incentive problem was not."],
  "requirements": [
   "Confirm: scored jurisdictions raise exchange rates and care continuity with penalties and scorecards.",
   "Confirm: patient-mediated consent sustains public trust without blocking needed sharing.",
   "Refute: blocking technically unavoidable - legacy systems incapable of APIs at any price.",
   "Refute: privacy breaches destroying public consent for sharing."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim technology alone suffices or privacy concerns are trivial.",
   "The penalty level that makes blocking unprofitable is the open measurement."],
  "citations": [CIT_INTEROP],
 },
 {
  "key": "syndromic-surveillance",
  "name": "Can We Build a Global Early-Warning Nervous System?",
  "group": "Infectious Disease Control",
  "ladder_rank": 30, "ladder_tier": "advanced",
  "description": ("Outbreaks are detected late: the median time from "
                  "spillover to recognition is measured in weeks or "
                  "months, during which a local cluster becomes a "
                  "regional epidemic. Syndromic surveillance - "
                  "watching symptom patterns, pharmacy sales, "
                  "absenteeism, search queries - promises detection "
                  "before diagnoses exist. Brownstein's digital "
                  "disease detection work showed the signals are "
                  "real; turning them into a trusted global nervous "
                  "system has not happened."),
  "problem": "Why is outbreak detection still slow when the data exhaust of modern life could warn us in days?",
  "background": ("Henning's 2004 MMWR review defined syndromic "
                 "surveillance: automated, near-real-time analysis of "
                 "pre-diagnostic data. Systems like ESSENCE in the US "
                 "and EWARS in humanitarian settings proved the "
                 "concept for known threats. Digital streams - "
                 "search queries, social media, news aggregation "
                 "(HealthMap, ProMED) - detected signals for H1N1 "
                 "and Ebola ahead of official reports. But false "
                 "alarms plagued early systems (Google Flu Trends' "
                 "famous overestimates), data access is fragmented "
                 "across private platforms, and low-income countries "
                 "lack even basic electronic reporting. The WHO's "
                 "epidemic intelligence (EIOS) aggregates open "
                 "sources, but a true global nervous system - "
                 "continuous, trusted, acted upon - does not exist."),
  "why_it_matters": ("Every week of earlier detection is exponential "
                     "cases avoided: with a pathogen doubling weekly, "
                     "two weeks of warning is a fourfold smaller "
                     "outbreak. Early warning is the highest-leverage "
                     "investment in pandemic preparedness."),
  "sig_lens": ("The Signature lens treats surveillance as a "
               "signal-to-action problem: the data exhaust exists, "
               "the trusted pipeline from signal to response does "
               "not."),
  "sol_public": ("The Signature system proposes a verified signal "
                 "pipeline: open data streams fused with clinical "
                 "sentinels, graded alerts with known false-alarm "
                 "rates, and pre-committed response playbooks - so "
                 "the warning is trusted because its track record "
                 "is public. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) pre-diagnostic signals "
              "genuinely precede official detection - the "
              "retrospective evidence says so; (2) false alarms "
              "killed trust in early systems, so credibility must "
              "be engineered; (3) a warning without a playbook is "
              "noise. Reasoning path: Google Flu Trends failed on "
              "calibration, not on concept - the fix is verified "
              "signals with published accuracy, fused across "
              "streams, tied to pre-committed responses. Proposed "
              "mechanism: a global signal pipeline - open digital "
              "streams plus clinical and pharmacy sentinels fused "
              "into graded alerts, every alert scored publicly for "
              "accuracy over time, and alert levels wired to "
              "pre-funded response playbooks (investigate, "
              "contain, escalate). What would confirm it: the "
              "pipeline detecting real events days to weeks ahead "
              "of official channels with a published, tolerable "
              "false-alarm rate, and playbook responses "
              "measurably shrinking outbreaks. What would kill "
              "it: signals proving inseparable from noise at "
              "usable false-alarm rates, or playbooks never "
              "funded - warnings without response. What it does "
              "NOT claim: that digital signals replace "
              "laboratory confirmation, that all outbreaks are "
              "detectable early, or that this is proven. The "
              "honest unknown: the usable false-alarm rate - "
              "how many false warnings the system can survive."),
  "key_points": [
   "Outbreaks are detected weeks to months late; a local cluster becomes a regional epidemic in the gap.",
   "Syndromic surveillance watches pre-diagnostic data: symptoms, pharmacy sales, absenteeism, search queries.",
   "Digital streams detected H1N1 and Ebola signals ahead of official reports (Brownstein et al.).",
   "False alarms (Google Flu Trends) damaged trust; data access is fragmented across private platforms.",
   "No true global nervous system - continuous, trusted, acted upon - exists."],
  "requirements": [
   "Confirm: the pipeline detects real events days to weeks ahead with a published tolerable false-alarm rate.",
   "Confirm: playbook responses measurably shrink outbreaks vs unwarned controls.",
   "Refute: signals inseparable from noise at usable false-alarm rates.",
   "Refute: playbooks never funded - warnings without response."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim digital signals replace lab confirmation.",
   "The survivable false-alarm rate is the open measurement."],
  "citations": [CIT_SURVEIL],
 },
 {
  "key": "behavior-change-scale",
  "name": "Why Do Population Behavior Campaigns Fail?",
  "group": "Prevention and Behavior",
  "ladder_rank": 31, "ladder_tier": "advanced",
  "description": ("Public health runs on behavior change - quit "
                  "smoking, eat better, move more, vaccinate, use "
                  "the bed net - yet population campaigns "
                  "notoriously underperform: awareness rises, "
                  "behavior barely moves. Michie's behaviour change "
                  "wheel gave the field a rigorous framework "
                  "(capability, opportunity, motivation), and Rose "
                  "showed the population strategy's paradox - but "
                  "the gap between campaigns and changed lives "
                  "persists."),
  "problem": "Why do well-designed behavior campaigns move awareness but not behavior at population scale?",
  "background": ("Rose's 1985 classic distinguished the high-risk "
                 "strategy (treat the sick) from the population "
                 "strategy (shift the whole curve) - and showed "
                 "the population approach prevents more disease "
                 "while motivating nobody, since most people gain "
                 "little individually. Michie's COM-B model and "
                 "behaviour change wheel systematized intervention "
                 "design: behavior needs capability, opportunity, "
                 "and motivation together. Marteau's reviews of "
                 "nudging found small effects that fade. The "
                 "pattern repeats: mass-media campaigns raise "
                 "knowledge without changing the environment that "
                 "shapes choice, while structural changes - taxes, "
                 "bans, defaults - change behavior without "
                 "campaigns. The field knows behavior follows "
                 "structure; it keeps funding persuasion."),
  "why_it_matters": ("Nearly every preventable disease burden runs "
                     "through behavior. Cracking population behavior "
                     "change - or admitting persuasion's limits and "
                     "funding structure instead - would redirect "
                     "billions from theater to impact."),
  "sig_lens": ("The Signature lens treats campaigns as persuasion "
               "aimed at a structural problem: behavior is the "
               "output of environments, and campaigns try to "
               "override the output without touching the "
               "environment."),
  "sol_public": ("The Signature system proposes the structure-first "
                 "doctrine: diagnose the COM-B binding constraint, "
                 "change the environment that binds it, and use "
                 "campaigns only to announce the new default - "
                 "measured in behavior, never awareness. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) behavior follows "
              "structure more than persuasion - the evidence "
              "pattern says so; (2) COM-B correctly identifies "
              "the binding constraint when honestly applied; (3) "
              "campaigns are cheap and visible, which is why "
              "they are overfunded, not why they work. "
              "Reasoning path: the repeated failure mode is "
              "funding motivation while opportunity binds - "
              "telling people to eat vegetables they cannot "
              "afford. Proposed mechanism: a structure-first "
              "protocol - every behavior program must name its "
              "COM-B binding constraint with evidence, fund the "
              "structural change first (price, availability, "
              "default, time), and use communication only to "
              "make the new default legible; programs are "
              "evaluated on measured behavior change, with "
              "awareness-only outcomes scored as failures. "
              "What would confirm it: protocol programs "
              "showing behavior change at scale where "
              "matched persuasion-only programs do not. What "
              "would kill it: structural changes failing to "
              "move behavior either - implying the binding "
              "constraints are cultural beyond policy reach. "
              "What it does NOT claim: that communication is "
              "useless, that all behavior is structural, or "
              "that this is proven. The honest unknown: the "
              "cultural remainder - how much behavior "
              "resists even well-designed structure."),
  "key_points": [
   "Population campaigns reliably raise awareness while behavior barely moves.",
   "Rose (1985): the population strategy prevents more disease while motivating nobody.",
   "Michie's COM-B: behavior needs capability, opportunity, and motivation together.",
   "Structural changes - taxes, bans, defaults - change behavior without campaigns.",
   "The field funds persuasion while knowing behavior follows structure."],
  "requirements": [
   "Confirm: structure-first protocol programs change behavior at scale vs persuasion-only matches.",
   "Confirm: awareness-only outcomes correctly predict program failure when used as the metric.",
   "Refute: structural changes failing to move behavior - the cultural-beyond-policy refutation.",
   "Refute: COM-B misidentifying binding constraints systematically."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim communication is useless or all behavior is structural.",
   "The cultural remainder is the open measurement."],
  "citations": [CIT_BEHAVIOR],
 },
 {
  "key": "dementia-scale",
  "name": "How Do Societies Care for Millions with Dementia?",
  "group": "Aging and Chronic Care",
  "ladder_rank": 32, "ladder_tier": "advanced",
  "description": ("Dementia already affects over 55 million people, "
                  "a number set to triple by 2050, and there is no "
                  "disease-modifying treatment that works at "
                  "population scale. The Livingston Commission "
                  "estimated 40 percent of cases are attributable to "
                  "twelve modifiable risk factors - yet prevention "
                  "is barely funded, diagnosis comes late, and care "
                  "falls on exhausted families. Societies are "
                  "sleepwalking into the largest care crisis in "
                  "history."),
  "problem": "With no cure and tripling prevalence, what societal model can deliver dementia prevention and dignified care at scale?",
  "background": ("Livingston and colleagues' 2020 Lancet Commission "
                 "synthesized the hopeful half: twelve modifiable "
                 "risk factors - education, hearing loss, "
                 "hypertension, obesity, smoking, depression, "
                 "inactivity, diabetes, social contact, alcohol, "
                 "head injury, air pollution - account for about 40 "
                 "percent of dementia, meaning prevention is "
                 "substantially possible. The other half is bleak: "
                 "anti-amyloid drugs show marginal benefits at "
                 "enormous prices with real harms; diagnosis "
                 "typically arrives years late; and the care "
                 "economy - mostly unpaid family, mostly women - "
                 "is invisible in health budgets. The WHO's Global "
                 "Dementia Observatory tracks national plans, but "
                 "few countries fund them. Dementia care is where "
                 "the aging wave hits hardest: long duration, high "
                 "intensity, no cure."),
  "why_it_matters": ("Dementia will touch nearly every family within "
                     "a generation - as patients, caregivers, or "
                     "payers. A societal model for it is a societal "
                     "model for the entire aging century."),
  "sig_lens": ("The Signature lens treats dementia as a "
               "prevention-plus-dignity problem: 40 percent is "
               "preventable in principle, 100 percent needs "
               "humane care in practice, and current systems "
               "deliver neither."),
  "sol_public": ("The Signature system proposes the dementia "
                 "compact: midlife risk-factor programs that "
                 "prevent the preventable, early detection "
                 "pathways, and a funded care economy - "
                 "dementia-friendly communities measured in "
                 "years of dignified life. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the 40 percent "
              "preventable fraction is actionable - the risk "
              "factors overlap with existing chronic-disease "
              "programs; (2) care will remain human and "
              "labor-intensive - no technology substitutes for "
              "presence; (3) families cannot absorb tripling "
              "prevalence unpaid. Reasoning path: prevention "
              "and care are usually separate agendas - here "
              "they must be one compact, because the same "
              "midlife programs that prevent dementia prevent "
              "the other chronic diseases, and the care "
              "economy needs funding before the wave. "
              "Proposed mechanism: a national dementia "
              "compact - midlife brain-health programs "
              "folded into existing chronic-care grids "
              "(hearing, hypertension, activity, social "
              "contact), early-detection pathways with "
              "post-diagnostic support, paid caregiver "
              "workforces with dementia training, and "
              "dementia-friendly community standards - "
              "funded as long-term care, measured in "
              "dignified years. What would confirm it: "
              "compact regions showing dementia incidence "
              "bending down and caregiver burden and cost "
              "sustainable vs controls. What would kill "
              "it: the preventable fraction proving "
              "unreachable - risk factors unmodifiable at "
              "population scale - or care costs "
              "overwhelming any funding model. What it does "
              "NOT claim: that dementia is curable, that "
              "prevention reaches everyone, or that this is "
              "proven. The honest unknown: the achievable "
              "prevention fraction in real populations - 40 "
              "percent is attributable, not necessarily "
              "avertable."),
  "key_points": [
   "Over 55 million people live with dementia; prevalence will roughly triple by 2050.",
   "Twelve modifiable risk factors account for about 40 percent of cases (Livingston et al. 2020).",
   "Anti-amyloid drugs show marginal benefits at enormous prices with real harms.",
   "Diagnosis arrives years late; the care economy is mostly unpaid family, mostly women.",
   "Few countries fund their national dementia plans."],
  "requirements": [
   "Confirm: compact regions bend dementia incidence down vs controls.",
   "Confirm: funded caregiver workforces sustain care quality without family collapse.",
   "Refute: the preventable fraction unreachable - risk factors unmodifiable at scale.",
   "Refute: care costs overwhelming any funding model attempted."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim dementia is curable or prevention reaches everyone.",
   "The achievable prevention fraction is the open measurement."],
  "citations": [CIT_DEMENTIA],
 },
 {
  "key": "ncd-transition",
  "name": "How Do You Stop the Noncommunicable Disease Wave?",
  "group": "Global Systems",
  "ladder_rank": 33, "ladder_tier": "advanced",
  "description": ("Noncommunicable diseases - heart disease, cancer, "
                  "diabetes, chronic lung disease - now cause about "
                  "three-quarters of all deaths on earth, and the "
                  "wave is still rising in low- and middle-income "
                  "countries. Omran's 1971 epidemiologic transition "
                  "theory predicted the shift from infection to "
                  "chronic disease; the NCD Countdown 2030 showed "
                  "most countries will miss the UN target of "
                  "cutting premature NCD mortality by a third. The "
                  "drivers are shared - tobacco, diet, inactivity, "
                  "alcohol, air - but the response is fragmented by "
                  "disease."),
  "problem": "Why is the NCD wave still rising in most of the world despite shared, known drivers and proven interventions?",
  "background": ("Omran's transition theory described societies "
                 "moving from pestilence to degenerative disease "
                 "as they develop - and the developing world is "
                 "now mid-transition, carrying a double burden of "
                 "infection and chronic disease. The WHO's "
                 "'best buys' list the most cost-effective "
                 "interventions: tobacco taxes, salt reduction, "
                 "alcohol controls, physical activity promotion - "
                 "cheap, proven, and barely implemented where the "
                 "wave is rising. The NCD Countdown 2030 "
                 "collaboration found only a handful of countries "
                 "on track for the mortality target. The "
                 "fragmentation problem: cardiologists, "
                 "oncologists, and diabetologists each run "
                 "vertical programs while the drivers are "
                 "horizontal. Commercial determinants - the "
                 "industries profiting from tobacco, alcohol, "
                 "and ultra-processed food - actively oppose the "
                 "best buys."),
  "why_it_matters": ("The NCD wave is the dominant fact of 21st-"
                     "century mortality. Stopping it is not one "
                     "disease goal but the whole of adult health - "
                     "and the best buys are the cheapest policies "
                     "in public health."),
  "sig_lens": ("The Signature lens treats the NCD wave as a "
               "shared-driver problem attacked with "
               "disease-siloed tools: the drivers are "
               "horizontal, the programs are vertical, and the "
               "opposition is organized."),
  "sol_public": ("The Signature system proposes the driver-level "
                 "offensive: implement the WHO best buys as a "
                 "package, regulate the commercial determinants "
                 "as health hazards, and run NCD control as one "
                 "horizontal program - measured in premature "
                 "mortality bent downward. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the drivers are few, "
              "shared, and modifiable - tobacco, diet, "
              "inactivity, alcohol, air; (2) the best buys are "
              "genuinely cost-effective - the evidence is "
              "strong; (3) the binding constraint is political "
              "opposition from commercial determinants, not "
              "knowledge. Reasoning path: the countries "
              "missing the target are not missing science - "
              "they are missing implemented best buys, blocked "
              "by industry opposition and fragmented programs. "
              "Proposed mechanism: a driver-level offensive - "
              "the full best-buy package legislated together "
              "(taxes, marketing restrictions, labeling, salt "
              "targets), commercial-determinant regulation "
              "treating harmful industries like the tobacco "
              "playbook, and horizontal NCD programs replacing "
              "disease silos, with premature mortality "
              "published as the accountability metric. What "
              "would confirm it: offensive jurisdictions "
              "bending premature NCD mortality down faster "
              "than siloed controls. What would kill it: "
              "best buys failing where fully implemented - "
              "the drivers proving unmodifiable by policy - "
              "or commercial opposition defeating every "
              "legislative attempt. What it does NOT claim: "
              "that behavior change is easy, that industry "
              "can be wished away, or that this is proven. "
              "The honest unknown: the political formula - "
              "what coalition actually passes the package."),
  "key_points": [
   "NCDs cause about three-quarters of all deaths; the wave is still rising in poorer countries.",
   "Omran (1971): societies transition from infectious to chronic disease as they develop.",
   "The WHO best buys - tobacco taxes, salt reduction, alcohol controls - are cheap, proven, barely implemented.",
   "NCD Countdown 2030: only a handful of countries are on track for the mortality target.",
   "Drivers are horizontal but programs are vertical; harmful industries actively oppose the best buys."],
  "requirements": [
   "Confirm: offensive jurisdictions bend premature NCD mortality down faster than siloed controls.",
   "Confirm: the full best-buy package implemented together outperforms piecemeal adoption.",
   "Refute: best buys failing where fully implemented - drivers unmodifiable by policy.",
   "Refute: commercial opposition defeating every legislative attempt."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim behavior change is easy or industry can be wished away.",
   "The political formula that passes the package is the open measurement."],
  "citations": [CIT_NCD],
 },
 {
  "key": "population-health-theory",
  "name": "What Would a Complete Theory of Population Health Look Like?",
  "group": "Global Systems",
  "ladder_rank": 34, "ladder_tier": "advanced",
  "description": ("Population health has facts in abundance and theory "
                  "in scarcity: Evans and Stoddart's 1990 framework "
                  "mapped the determinants - biology, behavior, "
                  "environment, health care, prosperity - but no "
                  "integrated theory predicts how they combine to "
                  "produce the health of a population. Kindig and "
                  "Stoddart defined the field; McKinlay demanded it "
                  "refocus upstream. Without theory, every "
                  "intervention is a guess about a system nobody "
                  "has modeled."),
  "problem": "Can the determinants of population health be unified into a predictive theory, or is the system irreducibly complex?",
  "background": ("Evans and Stoddart's landmark 1990 paper gave the "
                 "field its map: health is produced by interacting "
                 "fields - genetic endowment, physical environment, "
                 "social environment, behavior, prosperity, and "
                 "health care - with feedback loops between them. "
                 "Kindig and Stoddart (2003) defined population "
                 "health as an outcome to be optimized. McKinlay "
                 "(2019) argued the field keeps drifting downstream "
                 "to clinical fixes because upstream causes are "
                 "politically hard. Systems modelers have built "
                 "pieces - microsimulations of disease, agent-based "
                 "models of behavior - but no unified, validated "
                 "theory predicts a population's health from its "
                 "determinants. The field advances by enumeration "
                 "of risk factors, not by theory that unifies them."),
  "why_it_matters": ("A predictive theory would turn public health "
                     "from reactive to architectural: policy "
                     "choices could be scored for their health "
                     "effects before adoption, and the field's "
                     "hundreds of interventions could be composed "
                     "instead of merely listed."),
  "sig_lens": ("The Signature lens treats population health as a "
               "production function waiting to be written: the "
               "inputs are mapped, the combining function is "
               "missing."),
  "sol_public": ("The Signature system proposes building the "
                 "theory as a calibrated production function: "
                 "determinant inputs, interaction terms, feedback "
                 "loops - validated by predicting real "
                 "populations' health before the fact. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the Evans-Stoddart "
              "fields are the right inputs - the map is "
              "correct; (2) interactions and feedbacks are "
              "modelable, not mystical; (3) a theory must "
              "predict out-of-sample to count. Reasoning "
              "path: the field has the parts list and the "
              "arrows between parts; what is missing is the "
              "quantified combining function with feedback. "
              "Proposed mechanism: a population-health "
              "production function - determinant inputs with "
              "estimated interaction terms and feedback "
              "loops, calibrated on historical population "
              "data, validated by pre-registered predictions "
              "of real populations' health trajectories, "
              "then used to score policies before adoption. "
              "What would confirm it: pre-registered "
              "predictions beating naive and "
              "single-determinant baselines across diverse "
              "populations. What would kill it: the system "
              "proving irreducibly complex - no model "
              "beating naive baselines out-of-sample - or "
              "feedback loops too slow to validate within "
              "a research lifetime. What it does NOT claim: "
              "that the theory exists, that modeling "
              "replaces politics, or that this is proven. "
              "The honest unknown: whether the combining "
              "function is learnable at all - the deepest "
              "question on this list, and the fitting final "
              "one."),
  "key_points": [
   "Evans and Stoddart (1990): health is produced by interacting fields - biology, behavior, environment, care, prosperity.",
   "No integrated theory predicts how the determinants combine to produce a population's health.",
   "The field advances by enumerating risk factors, not by unifying theory.",
   "McKinlay (2019): the field drifts downstream because upstream causes are politically hard.",
   "Pieces exist - microsimulations, agent-based models - but no validated unified theory."],
  "requirements": [
   "Confirm: pre-registered predictions beat naive and single-determinant baselines across diverse populations.",
   "Confirm: policy scoring from the theory guides real adoption decisions.",
   "Refute: no model beating naive baselines out-of-sample - irreducible complexity.",
   "Refute: feedback loops too slow to validate within a research lifetime."],
  "standards": [
   "Proposed path only; no proof claimed, no peer acceptance implied.",
   "Does not claim the theory exists or modeling replaces politics.",
   "Whether the combining function is learnable at all is the open measurement."],
  "citations": [CIT_THEORY],
 },
]
