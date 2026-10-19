#!/usr/bin/env python3
"""Entries for the Unsolved Ecology databases (Manon's 16:15 orders, Unsolved Problems Solved batch).

34 famous unsolved ecology problems, ladder-ordered by accessibility (rank 1 = most
approachable, rank 34 = most complex). Public half: JAH-USCY- (real, fact-checked problems
as the world knows them: predicting ecosystem collapse, the biodiversity-function
relationship, trophic cascade mechanics, why rainforests are hyperdiverse, microbial
ecosystem roles, restoration success principles, and the rest). Signature half:
JAH-USCYS- (same 34 problems through the Signature lens; titles suffixed
" (Signature Edition)", src signature, clearly labeled Signature-made, never presented
as authentic public record).

ID prefixes JAH-USCY- / JAH-USCYS- verified free 2026-10-17: zero hits in the manifest
id_prefix values (2,602 databases) and zero hits in every shard index file of
jah-databases-data-1 (full grep sweep over data/*/index.jsonl.gz and chunk files).
All 68 titles (34 public + 34 " (Signature Edition)") pre-checked against the
whole-system dedupe gate: zero collisions, zero refusals.

The Signature solution in every record opens with the EXACT label
"Signature-generated proposed solution - not established science."
Public halves carry a short pointer; signature halves carry the full treatment.
Honesty rule: no claims of proof, no implied peer acceptance, speculation never
presented as settled.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. All records human-readable sentences/paragraphs.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Method applied to ecology: "
            "every unsolved problem a field question, the solution explorer the "
            "Signature system's walkthrough, confirm-and-refute panels the oath of "
            "honesty. Clearly labeled Signature-made, never presented as established "
            "science or authentic public record.")

CIT_TROPICS = ("von Humboldt A, Bonpland A. Essay on the Geography of Plants. 1807; "
               "Brown JH. Why are there so many species in the tropics? J Biogeogr. 2014;41:8-22.")
CIT_SAR = ("Arrhenius O. Species and area. J Ecol. 1921;9:95-99; "
           "MacArthur RH, Wilson EO. The Theory of Island Biogeography. Princeton Univ Press; 1967.")
CIT_INVASION = ("Elton CS. The Ecology of Invasions by Animals and Plants. Methuen; 1958; "
                "Lockwood JL et al. The role of propagule pressure in explaining species invasions. "
                "Trends Ecol Evol. 2005;20:223-228.")
CIT_PREDDPREY = ("Lotka AJ. Elements of Physical Biology. Williams and Wilkins; 1925; "
                 "Volterra V. Fluctuations in the abundance of a species considered mathematically. "
                 "Nature. 1926;118:558-560.")
CIT_COLLAPSE = ("Scheffer M et al. Catastrophic shifts in ecosystems. Nature. 2001;413:591-596; "
                "Holling CS. Resilience and stability of ecological systems. Annu Rev Ecol Syst. 1973;4:1-23.")
CIT_EXTINCT = ("Pimm SL et al. The biodiversity of species and their rates of extinction, distribution, "
               "and protection. Science. 2014;344:1246752; Ceballos G et al. Accelerated modern "
               "human-induced species losses. Sci Adv. 2015;1:e1400253.")
CIT_BEF = ("Tilman D et al. The influence of functional diversity and composition on ecosystem "
           "processes. Science. 1997;277:1300-1302; Cardinale BJ et al. Biodiversity loss and its "
           "impact on humanity. Nature. 2012;486:59-67.")
CIT_MICROBES = ("van der Heijden MGA et al. The unseen majority: soil microbes as drivers of plant "
                "diversity and productivity in terrestrial ecosystems. Ecol Lett. 2008;11:296-310; "
                "Falkowski PG et al. The microbial engines that drive Earth's biogeochemical cycles. "
                "Science. 2008;320:1034-1039.")

ENTRIES = [
 {
  "key": "tropics-rich",
  "name": "Why the Tropics Hold So Many Species",
  "group": "Diversity and Richness",
  "ladder_rank": 1, "ladder_tier": "foundations",
  "description": ("Nearly every group of organisms is richest near the equator and poorest near "
                  "the poles. This latitudinal diversity gradient was noticed by Alexander von "
                  "Humboldt over two centuries ago, yet ecologists still argue about why it exists. "
                  "It is the most famous unsolved pattern in ecology: simple to state, visible from "
                  "space, and without an agreed cause."),
  "problem": "Why does species richness peak in the tropics and decline toward the poles in nearly every group of organisms?",
  "background": ("Alexander von Humboldt described the gradient in his 1807 Essay on the Geography "
                 "of Plants after his South American expeditions, noting that the same mountain "
                 "vegetation zones he climbed through reappeared, compressed, on the walk from "
                 "equator to pole. Alfred Russel Wallace later tied tropical richness to stable "
                 "climates and long evolutionary time. The modern debate offers a crowded field of "
                 "hypotheses: more solar energy supporting more individuals and hence more species, "
                 "faster evolution at higher temperatures, greater area of tropical biomes, longer "
                 "undisturbed time for speciation, stronger biotic interactions driving specialization, "
                 "and geometric null models like the mid-domain effect. Each explains part of the "
                 "pattern in some taxa and fails in others. Fossil evidence shows the gradient has "
                 "flattened and steepened through deep time, and some groups - like certain marine "
                 "mammals and parasites - reverse it. No single mechanism has survived every test, "
                 "and the field now suspects several causes act together in different proportions "
                 "for different groups."),
  "why_it_matters": ("The gradient is the master pattern of life's geography, and any conservation "
                      "plan that ignores its cause risks protecting the wrong places. If tropical "
                      "richness comes from long stable history, ancient lineages deserve priority; "
                      "if it comes from current energy, then warming could shift the whole pattern "
                      "poleward and strand tropical specialists. Understanding it is also the key "
                      "to predicting how climate change will redraw the map of biodiversity."),
  "sig_lens": ("The Signature lens treats the tropics as life's long-running workshop, where time, "
               "energy, and interaction have compounded longer than anywhere else on Earth."),
  "sol_public": ("The Signature system proposes the gradient is a compound-interest ledger: time "
                 "multiplied by energy multiplied by interaction intensity, with speciation as the "
                 "interest and extinction as the withdrawals. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) species richness is a balance sheet - speciation credits, "
              "extinction debits; (2) both rates respond to energy availability and to how tightly "
              "species interact; (3) the tropics have run this ledger longer without a reset than "
              "any other biome. Reasoning path: treat each region as an account. High solar energy "
              "raises the carrying capacity for individuals, which lowers extinction risk per species "
              "(larger populations) and raises the number of speciation lotteries run per century. "
              "Long climatic stability means fewer mass withdrawals - ice ages repeatedly zeroed the "
              "temperate account while the tropical one kept compounding. Intense biotic interaction "
              "(predation, parasitism, competition) then subdivides niches ever more finely, like a "
              "market splitting into specialties. Proposed mechanism: a three-factor product model - "
              "richness proportional to energy times stability-duration times interaction density, "
              "with region-specific weights. What would confirm it: fossil-calibrated speciation and "
              "extinction rates showing tropical lineages compound faster AND lose slower across many "
              "independent groups, with the product of the three factors predicting richness better "
              "than any single factor. What would kill it: a major group where the tropics are poorer "
              "despite higher energy and stability, with no identifiable extra withdrawal (such as "
              "extreme aridity), or proof that tropical speciation rates are no higher than temperate "
              "ones once sampling bias is removed. What it does NOT claim: that this is proven, that "
              "one factor dominates, or that the model predicts exact species counts. Where the honest "
              "answer is unknown - the true historical speciation rates for most groups - we say so: "
              "the fossil ledger is still mostly blank pages."),
  "key_points": [
   "Species richness peaks near the equator for plants, animals, and microbes alike; the pattern is over 200 years old.",
   "Competing explanations: energy, evolutionary speed, area, time-stability, biotic interactions, geometric nulls.",
   "The gradient has changed shape through deep time and reverses in some groups.",
   "No single hypothesis survives every test; the field leans toward multiple interacting causes.",
   "The cause determines conservation strategy and how climate change will redraw richness maps."],
  "requirements": [
   "Show tropical speciation credits exceed extinction debits across many independent groups.",
   "Confirm: the three-factor product predicts richness better than any single factor.",
   "Refute: a major group poorer in the tropics despite high energy and stability, with no extra withdrawal.",
   "Refute: tropical speciation rates equal temperate rates once sampling bias is corrected."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim one dominant factor or exact species-count predictions.",
   "It must survive the fossil gap: historical rates are estimated, not measured directly."],
  "citations": [CIT_TROPICS],
 },
 {
  "key": "species-area",
  "name": "What Sets How Many Species a Place Can Hold",
  "group": "Diversity and Richness",
  "ladder_rank": 2, "ladder_tier": "foundations",
  "description": ("Double the area of a habitat and the number of species rises - but by how much, "
                  "and why? The species-area relationship is ecology's oldest quantitative law, "
                  "described by Olof Arrhenius in 1921, and it underpins reserve design, extinction "
                  "forecasts, and island biogeography. Yet what actually sets the curve - more "
                  "habitats, bigger populations, or pure sampling - is still debated."),
  "problem": "What mechanism actually generates the species-area relationship, and what sets its exact shape in any given place?",
  "background": ("Olof Arrhenius found in 1921 that species counts rise with area as a power law, "
                 "S = cA^z, with the exponent z mysteriously clustering near 0.25 across wildly "
                 "different systems. Frank Preston reframed it through sampling: bigger areas sample "
                 "more individuals from the regional pool, so more species appear. MacArthur and "
                 "Wilson's 1967 Theory of Island Biogeography made area do real work - larger islands "
                 "hold larger populations with lower extinction rates, and sit as bigger targets for "
                 "colonists. Later work added habitat heterogeneity: bigger areas contain more habitat "
                 "types, each with its own species. The three mechanisms - sampling, extinction "
                 "buffering, habitat diversity - all predict the same curve, which is exactly the "
                 "problem: the law is so robust that it hides its own cause. Conservation leans on "
                 "it heavily, using species-area curves to predict extinctions from habitat loss, "
                 "yet if sampling dominates, those predictions may mislead, since sampling effects "
                 "do not kill species the way real extinction does."),
  "why_it_matters": ("Species-area curves are the workhorse behind extinction forecasts from "
                      "deforestation and the math behind how big a reserve must be. If the curve is "
                      "driven by habitat variety rather than area itself, then a small varied reserve "
                      "can outperform a large uniform one - a difference worth billions in conservation "
                      "spending and thousands of species."),
  "sig_lens": ("The Signature lens treats area as a container with three compartments - samples, "
               "populations, and habitats - and asks which compartment fills first as the container grows."),
  "sol_public": ("The Signature system proposes a compartment audit: as area grows, first sampling "
                 "fills the curve, then population buffering, then habitat variety - and the dominant "
                 "compartment can be read from how the curve bends at small, medium, and large scales. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the three mechanisms operate at different characteristic "
              "scales; (2) sampling dominates at the smallest scales, population buffering at middle "
              "scales, habitat variety at large scales; (3) the transitions leave kinks in the curve. "
              "Reasoning path: imagine expanding a survey plot. At first, each new square meter mostly "
              "adds new individuals from the same local pool - pure sampling, steep rise. Then the "
              "plot is big enough that population sizes grow and rare species stop blinking out - "
              "the extinction-buffering compartment. Finally new habitat types enter - a stream, a "
              "rocky outcrop - and each donates its specialists. Proposed mechanism: a three-segment "
              "power law, S = c1*A^z1 for the sampling reach, c2*A^z2 for the buffering reach, "
              "c3*A^z3 for the habitat reach, with segment boundaries predicted from organism body "
              "size and dispersal distance. What would confirm it: nested-plot experiments across "
              "taxa showing two detectable kinks whose positions scale with body size as predicted, "
              "and removal experiments (sterilizing habitat variety while holding area constant) "
              "flattening only the third segment. What would kill it: curves that are perfectly "
              "smooth power laws across six orders of magnitude with no kinks at any resolution, or "
              "kink positions that do not track body size. What it does NOT claim: that this is "
              "proven, that z equals 0.25 universally, or that sampling effects cause real "
              "extinctions. Where the honest answer is unknown - the true segment boundaries in "
              "most real landscapes - we say so: the kinks are predicted, not yet mapped."),
  "key_points": [
   "Species richness rises with area as S = cA^z, with z often near 0.25; the law is over a century old.",
   "Three rival mechanisms - sampling, extinction buffering, habitat variety - all predict the same curve.",
   "Island biogeography made area do real ecological work through colonization-extinction balance.",
   "Which mechanism dominates decides whether small varied reserves can beat large uniform ones.",
   "Extinction forecasts from habitat loss assume the curve means real extinctions, not sampling artifacts."],
  "requirements": [
   "Detect two kinks in nested-plot curves whose positions scale with organism body size.",
   "Confirm: removing habitat variety while holding area constant flattens only the large-scale segment.",
   "Refute: perfectly smooth power laws across six orders of magnitude at every resolution.",
   "Refute: kink positions unrelated to body size or dispersal distance."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim z is universal or that sampling effects equal real extinctions.",
   "Segment boundaries are predictions awaiting measurement, not established facts."],
  "citations": [CIT_SAR],
 },
 {
  "key": "invasions",
  "name": "Why Some Invasions Succeed and Others Fail",
  "group": "Restoration and Stewardship",
  "ladder_rank": 3, "ladder_tier": "foundations",
  "description": ("Humans move thousands of species beyond their native ranges every year, yet only "
                  "a fraction establish, and fewer still become invasive. Charles Elton's 1958 book "
                  "launched invasion ecology, but after decades of case studies the field still "
                  "cannot reliably predict which introduced species will explode and which will "
                  "vanish quietly."),
  "problem": "What combination of species traits, introduction circumstances, and recipient-community properties determines whether an introduced species establishes and becomes invasive?",
  "background": ("Charles Elton's The Ecology of Invasions (1958) framed biological invasion as "
                 "ecological explosions, and early theory emphasized community resistance: diverse "
                 "native communities were thought to repel invaders by leaving no niche unused - the "
                 "biotic resistance hypothesis. Experiments partly supported it, but field data kept "
                 "showing diverse places invaded anyway. Attention shifted to propagule pressure - "
                 "the number of individuals introduced and how often - which predicts establishment "
                 "better than almost any trait. Enemy release (leaving specialized predators behind), "
                 "novel weapons (chemicals natives never met), and disturbance opening windows of "
                 "opportunity all explain famous cases: zebra mussels in the Great Lakes, brown tree "
                 "snakes on Guam, cane toads in Australia. But each invader seems to succeed for its "
                 "own reasons, and the same species can be harmless in one region and devastating in "
                 "another. The emerging view is that invasions are probabilistic, not deterministic - "
                 "yet managers need better than probabilities; they need to know where to spend "
                 "limited control budgets."),
  "why_it_matters": ("Invasive species cost the global economy hundreds of billions of dollars yearly "
                      "and rank among the top drivers of extinction. Every quarantine list, ballast-water "
                      "rule, and eradication campaign is a bet on which introductions matter. A real "
                      "predictive framework would turn those bets into calculated risks."),
  "sig_lens": ("The Signature lens treats invasion as a three-gate audition: arrival, establishment, "
               "and spread - and asks which gate does the real filtering for each candidate."),
  "sol_public": ("The Signature system proposes a gate-weighted scorecard: establishment is mostly "
                 "propagule pressure, spread is mostly trait-environment match, and impact is mostly "
                 "about the recipient community's missing defenses. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) invasion has three sequential gates - arrival, establishment, "
              "spread - and different factors dominate each; (2) propagule pressure is the master key "
              "to gate two; (3) impact depends on the recipient community, not just the invader. "
              "Reasoning path: score each candidate at each gate. Gate one (arrival) is pure transport "
              "physics - trade volume and pathways. Gate two (establishment) is a numbers game: a "
              "population founded by ten individuals usually dies by bad luck, one founded by ten "
              "thousand usually persists; this is why propagule pressure out-predicts traits. Gate "
              "three (spread and impact) is where traits and community matter: fast growth and broad "
              "tolerance help spread, while impact depends on whether natives have defenses against "
              "the invader's weapons. Proposed mechanism: a multiplicative scorecard, "
              "Risk = Arrival x Establishment(propagule pressure, climate match) x Spread(traits) x "
              "Impact(community naivete), with each term estimated from databases rather than expert "
              "opinion. What would confirm it: retrospective scoring of hundreds of past introductions "
              "showing the scorecard separates established from failed and high-impact from low-impact "
              "cases better than trait-only or pressure-only models. What would kill it: cases where "
              "tiny propagule pressure produced massive invasion despite poor trait match, repeatedly "
              "and predictably, or proof that gate interactions are strongly non-multiplicative. "
              "What it does NOT claim: that this is proven, that it predicts exact spread rates, or "
              "that any species can be declared safe. Where the honest answer is unknown - the "
              "quantitative weights of each gate - we say so: the weights must be fitted from data, "
              "not asserted."),
  "key_points": [
   "Most introduced species fail; a minority establish; fewer still become damaging invaders.",
   "Propagule pressure (how many, how often) predicts establishment better than species traits.",
   "Famous mechanisms: enemy release, novel weapons, disturbance windows, biotic resistance.",
   "The same species can be harmless in one region and devastating in another.",
   "Invasions cost hundreds of billions yearly and rank among the top extinction drivers."],
  "requirements": [
   "Retrospectively score hundreds of introductions; the scorecard must beat single-factor models.",
   "Confirm: gate-specific factors dominate their own gate more than the others.",
   "Refute: repeated massive invasions from tiny propagule pressure with poor trait match.",
   "Refute: strong non-multiplicative gate interactions that break the scorecard structure."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim exact spread-rate predictions or that any species is certifiably safe.",
   "Gate weights are fitted parameters, not asserted constants."],
  "citations": [CIT_INVASION],
 },
 {
  "key": "predator-prey",
  "name": "Why Predator and Prey Numbers Rise and Fall",
  "group": "Food Webs and Trophic Dynamics",
  "ladder_rank": 4, "ladder_tier": "foundations",
  "description": ("Hare populations boom and crash every decade, and lynx follow a few years behind. "
                  "Predator-prey cycles are ecology's most iconic pattern, and the Lotka-Volterra "
                  "equations of the 1920s were ecology's first mathematical theory. Yet a century "
                  "later, ecologists still argue about what really drives the cycles in nature - "
                  "the predators, the prey's food, or something else entirely."),
  "problem": "What actually drives predator-prey population cycles in nature - predator-prey interaction alone, prey food limitation, or external forces?",
  "background": ("Alfred Lotka (1925) and Vito Volterra (1926) independently wrote the equations "
                 "showing that linked predator and prey populations oscillate on their own, with "
                 "predators lagging prey. The Hudson's Bay Company fur records - lynx and snowshoe "
                 "hare pelts over two centuries - seemed to confirm it beautifully. Then doubts "
                 "crept in: the hare cycle might be driven by the hares' own food (willow shoots) "
                 "rather than lynx, with predators merely following. Experiments that fenced out "
                 "predators, fenced out food, or added food showed both matter - the famous Kluane "
                 "boreal forest project found the hare cycle needed both predation and food stress. "
                 "Later theory showed cycles can also be driven by parasites, maternal stress effects "
                 "passed to offspring, or climate. The Lotka-Volterra core is mathematically elegant "
                 "but structurally fragile: tiny realistic changes (like prey carrying capacity) can "
                 "kill the cycles or make them explode. So the equations describe possible cycles, "
                 "but nature's actual cycles remain a three-way argument between top-down, bottom-up, "
                 "and external drivers."),
  "why_it_matters": ("Fisheries, pest control, and wildlife management all ride on understanding "
                      "what drives animal numbers. Collapse a fish stock by overfishing and the "
                      "question of whether it will cycle back or stay down depends on which driver "
                      "dominates. Getting cycles right is the difference between sustainable harvest "
                      "and empty seas."),
  "sig_lens": ("The Signature lens treats the cycle as a three-engine machine - predators, food, "
               "and climate - and asks which engine is actually turning the crank each decade."),
  "sol_public": ("The Signature system proposes a driver-partition method: experimental fences plus "
                 "time-series fingerprints can assign each cycle a percentage driven by predators, "
                 "food, and climate. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) real cycles are mixtures of three drivers - top-down "
              "predation, bottom-up food, external forcing; (2) each driver leaves a distinct "
              "time-series fingerprint (lag structure and phase relationships); (3) small "
              "manipulative experiments can calibrate the fingerprints. Reasoning path: run the "
              "three canonical experiments - predator exclusion, food addition, both - and record "
              "how cycle amplitude, period, and phase shift in each. These shifts form a fingerprint "
              "library. Then read any unmanipulated long-term time series against the library to "
              "partition its cycle into driver percentages. Proposed mechanism: a driver-partition "
              "model where the observed cycle is a weighted sum of three oscillators, the weights "
              "estimated by matching observed lags to the experimental library. What would confirm "
              "it: the Kluane-style results replicated across five or more systems with the library "
              "correctly predicting each system's response to a new manipulation. What would kill "
              "it: systems where removing predators and adding food both leave the cycle unchanged "
              "(implying a fourth driver dominates), or fingerprints that fail to transfer between "
              "similar systems. What it does NOT claim: that this is proven, that Lotka-Volterra "
              "describes real cycles, or exact forecasts of next year's numbers. Where the honest "
              "answer is unknown - the full driver list in most systems - we say so: the library "
              "starts with three drivers and grows only with evidence."),
  "key_points": [
   "Lotka-Volterra (1925-1926) showed predator-prey pairs can oscillate on their own.",
   "The lynx-hare fur records are the iconic example, spanning two centuries.",
   "Kluane experiments showed hare cycles need both predation and food stress.",
   "Realistic tweaks to the equations easily destroy or explode the cycles.",
   "Which driver dominates decides whether harvested populations recover or stay collapsed."],
  "requirements": [
   "Replicate predator-exclusion plus food-addition fingerprints in five or more systems.",
   "Confirm: the fingerprint library predicts responses to new manipulations.",
   "Refute: cycles unchanged by both predator removal and food addition.",
   "Refute: fingerprints that fail to transfer between ecologically similar systems."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim Lotka-Volterra describes real cycles or forecasts exact numbers.",
   "The driver list is open-ended and grows only with experimental evidence."],
  "citations": [CIT_PREDDPREY],
 },
 {
  "key": "collapse-sudden",
  "name": "Why Ecosystems Sometimes Collapse All at Once",
  "group": "Stability and Collapse",
  "ladder_rank": 5, "ladder_tier": "foundations",
  "description": ("Clear lakes flip to murky green almost overnight. Coral reefs become algal flats "
                  "within years. Grasslands turn to desert without passing through intermediate "
                  "stages. Some ecosystems decline gradually under pressure, but others hold steady "
                  "and then collapse suddenly - and ecology still cannot reliably say which kind a "
                  "given system is until it tips."),
  "problem": "Why do some ecosystems collapse suddenly under gradual pressure while others decline smoothly, and what determines which kind a system is?",
  "background": ("C.S. Holling's 1973 work on resilience introduced the idea that ecosystems can "
                 "absorb disturbance and flip between stable states, inspired by budworm outbreaks "
                 "in Canadian forests. Marten Scheffer's group formalized it: strong positive "
                 "feedback loops - like murky water blocking light for the plants that would clear "
                 "it - create alternative stable states separated by thresholds. Push the system "
                 "gently and it resists; push past the threshold and it snaps to the other state, "
                 "often with hysteresis, meaning you must push much harder to get back. Famous "
                 "examples accumulated: shallow lakes flipping between clear and turbid, coral reefs "
                 "flipping to macroalgae, the Sahara greening and drying. But critics note that "
                 "many claimed regime shifts, examined closely, look gradual or are driven by "
                 "external shocks rather than internal feedbacks. The theory is elegant and the "
                 "examples are real, yet ecologists still argue over how common true catastrophic "
                 "shifts are versus smooth responses - and managers cannot wait for the argument "
                 "to settle."),
  "why_it_matters": ("If a fishery, rangeland, or reef is a threshold system, then managing for "
                      "maximum steady yield is playing chicken with a cliff edge. Gradual systems "
                      "forgive mistakes; threshold systems punish the last mistake catastrophically. "
                      "Knowing which kind you manage changes every rule."),
  "sig_lens": ("The Signature lens treats ecosystems as landscapes of valleys: gradual systems are "
               "one wide valley, threshold systems are two valleys with a ridge between - and the "
               "feedback strength tells you which map you hold."),
  "sol_public": ("The Signature system proposes a feedback audit: measure the strength of the "
                 "system's positive feedback loops directly, and the feedback total classifies the "
                 "system as gradual or threshold before any collapse happens. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) sudden collapse requires positive feedback strong enough "
              "to create alternative stable states; (2) feedback strength can be measured from "
              "perturbation experiments without pushing the system over; (3) hysteresis size scales "
              "with feedback strength. Reasoning path: list the candidate feedback loops in the "
              "system (for a lake: turbidity blocking light, algae outcompeting plants, fish "
              "stirring sediment). Perturb each one slightly and measure how much the system "
              "amplifies versus damps the push - the loop gain. Sum the gains: if the total stays "
              "below one, disturbances fade and the system is gradual; if it exceeds one, the "
              "system has a second valley waiting. Proposed mechanism: a feedback-gain audit that "
              "outputs a single number, the system's tip-readiness, plus which loop contributes "
              "most - telling managers exactly which feedback to weaken. What would confirm it: "
              "audits on a dozen systems correctly classifying known gradual versus known threshold "
              "systems, and management that weakens the top loop measurably widening the safe "
              "operating range. What would kill it: systems that collapse suddenly with no "
              "measurable positive feedback (pure external shock), or audits that classify "
              "backwards. What it does NOT claim: that this is proven, that it locates the exact "
              "threshold, or that weakening feedbacks is always feasible. Where the honest answer "
              "is unknown - the complete feedback inventory of most ecosystems - we say so: the "
              "audit is only as good as the loop list."),
  "key_points": [
   "Some ecosystems flip suddenly between alternative stable states; others decline smoothly.",
   "Strong positive feedback loops (turbidity, algal overgrowth) create the thresholds.",
   "Hysteresis means recovery takes far more effort than the collapse did.",
   "Critics argue many claimed shifts are really gradual or externally driven.",
   "Threshold systems punish the last management mistake; gradual systems forgive."],
  "requirements": [
   "Feedback audits must correctly classify a dozen known gradual vs threshold systems.",
   "Confirm: weakening the top feedback loop widens the measured safe operating range.",
   "Refute: sudden collapses with no measurable positive feedback beforehand.",
   "Refute: audits that systematically classify known systems backwards."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim to locate exact thresholds or that feedbacks are always weakenable.",
   "The audit depends on a complete loop inventory, which most systems lack."],
  "citations": [CIT_COLLAPSE],
 },
 {
  "key": "extinction",
  "name": "What Decides Which Species Go Extinct",
  "group": "Stability and Collapse",
  "ladder_rank": 6, "ladder_tier": "foundations",
  "description": ("Species are vanishing at rates far above the fossil background, yet extinction "
                  "is strangely selective: island birds, large mammals, freshwater fish, and "
                  "amphibians suffer most, while many small widespread species persist. Ecologists "
                  "can list the correlates of extinction risk, but predicting which species goes "
                  "next - and stopping it - remains an unsolved problem."),
  "problem": "What actually determines which species go extinct under human pressure, and can the next extinctions be predicted in time to prevent them?",
  "background": ("The fossil record shows five mass extinctions and a steady background rate of "
                 "roughly one species per million per year. Current estimates put the modern rate "
                 "hundreds to a thousand times higher, driven by habitat loss, overexploitation, "
                 "invasive species, pollution, and now climate change. The pattern is selective: "
                 "large-bodied, slow-reproducing, specialized, island-dwelling, and "
                 "narrowly-distributed species die first - the same profile, repeatedly. The IUCN "
                 "Red List formalized risk assessment using population size, range, and decline "
                 "rate, and it works reasonably for vertebrates. But most species are insects, "
                 "fungi, and microbes that have never been assessed; extinction debt means species "
                 "doomed by past habitat loss have not died yet, hiding the true toll; and "
                 "co-extinctions - parasites, pollinators, and specialists dying with their hosts - "
                 "are barely counted. We know the correlates and the drivers, yet the field still "
                 "argues over the true current rate within an order of magnitude, and most "
                 "extinctions of small organisms pass entirely unnoticed."),
  "why_it_matters": ("You cannot save what you cannot see coming. Conservation triage - which "
                      "species get the limited money - depends on honest extinction forecasts. "
                      "Underestimating the rate breeds complacency; overestimating it breeds "
                      "despair and misallocated effort. Both cost species."),
  "sig_lens": ("The Signature lens treats extinction as a ledger of debts: every species carries "
               "an account, and human pressures post debits faster than evolution can credit."),
  "sol_public": ("The Signature system proposes a debt ledger for every species: habitat loss, "
                 "exploitation, invasion, and climate debits minus the species' buffering credits "
                 "(range size, reproductive rate, adaptability), with co-extinction chains counted "
                 "as linked accounts. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) extinction risk is a balance of pressure debits against "
              "biological buffering credits; (2) pressures interact multiplicatively, not "
              "additively; (3) co-extinction links transmit risk between accounts. Reasoning path: "
              "for each species, estimate four debits - habitat lost, harvest pressure, invader "
              "pressure, climate velocity across its range - and three credits - range size, "
              "reproductive output, ecological flexibility. The risk score is debits over credits, "
              "with linked species (pollinators, hosts, prey) sharing a fraction of each other's "
              "scores. Species already in extinction debt show positive scores but are still alive "
              "- these are the predictable next losses. Proposed mechanism: a linked-ledger model "
              "outputting a ranked watchlist with the dominant debit named for each species, so "
              "intervention targets the actual pressure. What would confirm it: the watchlist "
              "predicting the next decade's observed extinctions and Red List uplistings better "
              "than Red List criteria alone, across vertebrates and at least one invertebrate "
              "group. What would kill it: extinctions dominated by species the ledger ranked safe, "
              "or proof that pressure interactions are so idiosyncratic that no general weighting "
              "transfers across regions. What it does NOT claim: that this is proven, exact "
              "extinction dates, or coverage of undescribed species. Where the honest answer is "
              "unknown - the true number of species and the fate of the undescribed majority - we "
              "say so: the ledger covers assessed species and clearly marks its blind spots."),
  "key_points": [
   "Modern extinction rates run hundreds to a thousand times the fossil background.",
   "Risk is selective: large, slow-breeding, specialized, island, narrow-range species die first.",
   "Extinction debt hides doomed species that have not died yet; co-extinctions are undercounted.",
   "The true current rate is still debated within an order of magnitude.",
   "Most extinctions of insects, fungi, and microbes pass completely unnoticed."],
  "requirements": [
   "The watchlist must beat Red List criteria at predicting a decade of extinctions and uplistings.",
   "Confirm: named dominant debits respond to targeted intervention (risk scores fall).",
   "Refute: most observed extinctions coming from species the ledger ranked safe.",
   "Refute: pressure weights that fail to transfer across regions."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim exact extinction dates or coverage of undescribed species.",
   "Blind spots (undescribed taxa, unknown interactions) are marked, not hidden."],
  "citations": [CIT_EXTINCT],
 },
 {
  "key": "bef",
  "name": "How Many Species an Ecosystem Needs to Work",
  "group": "Diversity and Richness",
  "ladder_rank": 7, "ladder_tier": "foundations",
  "description": ("Remove species from a grassland and productivity falls - but how many can you "
                  "lose before the system breaks? The biodiversity-ecosystem function debate asks "
                  "whether every species matters or whether a few workhorses carry the load. "
                  "Decades of experiments say diversity helps, yet the real world keeps offering "
                  "counterexamples of simple systems that work fine."),
  "problem": "How many species, and which kinds, does an ecosystem need to maintain its functioning, and how much redundancy is real?",
  "background": ("Through the 1980s many ecologists assumed most species were redundant passengers "
                 "and a few dominants drove ecosystem processes. David Tilman's Cedar Creek "
                 "experiments in the 1990s challenged that: grassland plots with more plant species "
                 "consistently produced more biomass and used resources more completely, and the "
                 "effect grew stronger over decades as complementarity developed. Meta-analyses "
                 "across hundreds of experiments confirmed the pattern for productivity, "
                 "decomposition, and nutrient retention. But critics raised the sampling effect: "
                 "diverse plots are simply more likely to contain a superstar species, so diversity "
                 "per se might do nothing. Long-term data eventually separated the two - "
                 "complementarity is real and grows with time. Still open: how the relationship "
                 "scales to real landscapes with immigration, whether rare species contribute "
                 "measurably, and the shape of the curve at high diversity - saturating, linear, "
                 "or still rising. The practical question - the minimum viable diversity for a "
                 "working ecosystem - has no general answer yet."),
  "why_it_matters": ("This is the scientific core of the case for conserving biodiversity: if "
                      "function saturates at low diversity, then losing species is sad but harmless; "
                      "if every species contributes, then each extinction erodes the machinery. "
                      "Restoration targets, biodiversity offsets, and ecosystem-service payments all "
                      "implicitly bet on an answer."),
  "sig_lens": ("The Signature lens treats species as workers with overlapping shifts: some hours "
               "are covered by many hands, some by exactly one - and the schedule reveals the "
               "true minimum crew."),
  "sol_public": ("The Signature system proposes a shift-coverage audit: map which species perform "
                 "each ecosystem function under each condition, and the minimum crew is the smallest "
                 "set covering every function in every condition. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) ecosystem functions can be listed and measured per "
              "species per condition; (2) redundancy is condition-dependent - a backup worker only "
              "counts if it shows up when needed; (3) rare conditions reveal hidden essential "
              "workers. Reasoning path: enumerate the system's functions (production, "
              "decomposition, pollination, pest control, nutrient retention) and the conditions it "
              "faces (drought, flood, heat, disease years). For each species, record which "
              "functions it performs under which conditions - the coverage matrix. The minimum crew "
              "is the smallest species set covering every function-condition cell; everything "
              "beyond that is true redundancy. Proposed mechanism: a coverage-matrix audit that "
              "outputs the minimum set, the redundancy map, and the single most load-bearing "
              "species per function. What would confirm it: removal experiments where deleting the "
              "audit's minimum set collapses function but deleting an equal number of redundant "
              "species does not, replicated across grassland, forest, and marine systems. What "
              "would kill it: systems where function depends on species interactions the matrix "
              "cannot capture (emergent complementarity), or minimum sets that fail to transfer "
              "between similar sites. What it does NOT claim: that this is proven, that the "
              "minimum crew is safe to keep (insurance needs redundancy), or that functions are "
              "fully listable. Where the honest answer is unknown - the complete function list for "
              "most ecosystems - we say so: the audit starts with measurable functions and labels "
              "its gaps."),
  "key_points": [
   "Diverse experimental plots are more productive and stable; complementarity grows over decades.",
   "The sampling effect (diverse plots contain superstars) explains part but not all of the pattern.",
   "Whether rare species contribute measurably is still open.",
   "The curve's shape at high diversity - saturating or still rising - is unresolved.",
   "The minimum viable diversity for a working ecosystem has no general answer."],
  "requirements": [
   "Removal experiments: deleting the audit's minimum set must collapse function; deleting redundants must not.",
   "Confirm: replication across grassland, forest, and marine systems.",
   "Refute: function carried by interactions the coverage matrix cannot capture.",
   "Refute: minimum sets that fail to transfer between similar sites."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the minimum crew is a safe target - insurance requires redundancy.",
   "Function lists are partial; gaps are labeled, not hidden."],
  "citations": [CIT_BEF],
 },
 {
  "key": "microbes-role",
  "name": "What Microbes Actually Do in Ecosystems",
  "group": "Microbes and Hidden Worlds",
  "ladder_rank": 8, "ladder_tier": "foundations",
  "description": ("A teaspoon of soil holds more microbes than there are people on Earth, and they "
                  "run the planet's chemistry: decomposition, nitrogen fixation, methane cycling, "
                  "the air we breathe. Yet for most microbial species we do not know what they "
                  "eat, what eats them, or what would happen if they vanished. Ecology's biggest "
                  "workforce is its least understood."),
  "problem": "What are the actual ecological roles of microbial species in ecosystems - who does what, and which microbes are load-bearing?",
  "background": ("For a century, microbiology studied the tiny minority of microbes that grow in "
                 "lab cultures, while ecology largely treated microbes as a black box labeled "
                 "'decomposers.' DNA sequencing blew the box open: the vast majority of microbial "
                 "diversity belongs to lineages never cultured, never named, never studied. We now "
                 "know microbes drive every major biogeochemical cycle - cyanobacteria oxygenated "
                 "the atmosphere, mycorrhizal fungi feed most land plants, gut microbes shape "
                 "animal nutrition and immunity. Experiments show microbial community composition "
                 "changes plant productivity, disease resistance, and carbon storage. But linking "
                 "specific microbial taxa to specific ecosystem functions remains brutally hard: "
                 "thousands of species co-occur, most cannot be grown alone, and function may live "
                 "in the community's interactions rather than in any one member. The field can "
                 "sequence everything and still not know who does what."),
  "why_it_matters": ("Microbes control the carbon cycle, soil fertility, crop yields, and disease. "
                      "Climate models, agriculture, and restoration all need to know which microbes "
                      "matter - and whether losing microbial diversity, which is happening silently "
                      "worldwide, will break the cycles civilization depends on."),
  "sig_lens": ("The Signature lens treats the microbial world as a vast anonymous workforce and "
               "asks for job descriptions: not names and faces, but who does which job and who "
               "covers when someone is absent."),
  "sol_public": ("The Signature system proposes a job-description census: knock out microbial "
                 "groups one guild at a time and read which ecosystem functions stumble, building "
                 "a role map from functions to guilds instead of from names to jobs. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) microbial functions are carried by guilds (nitrogen "
              "fixers, decomposers, methanogens) more often than by single taxa; (2) guilds can be "
              "selectively suppressed without culturing every member; (3) function loss reveals the "
              "guild's load. Reasoning path: take intact soil, water, or gut communities and apply "
              "guild-targeted suppressions - inhibitors, size fractionation, heat treatments - "
              "knocking out one guild at a time. Measure what happens to decomposition rate, "
              "nitrogen mineralization, methane flux, plant growth, disease suppression. The "
              "functions that stumble map to the suppressed guild: that is its job description. "
              "Repeat across ecosystems to find which guilds are universal load-bearers. Proposed "
              "mechanism: a role-map matrix (guilds by functions by ecosystems) built from "
              "knockout experiments, identifying load-bearing guilds whose loss collapses function "
              "versus redundant guilds whose loss is absorbed. What would confirm it: knockout "
              "maps that predict the outcome of new suppressions and of microbial diversity-loss "
              "experiments, with the same guilds load-bearing across continents. What would kill "
              "it: function carried entirely by emergent community interactions, so no guild "
              "knockout maps cleanly to function loss, or guilds so context-dependent that no map "
              "transfers. What it does NOT claim: that this is proven, that taxa do not matter, or "
              "that every microbe gets a job description. Where the honest answer is unknown - the "
              "identity and function of most uncultured lineages - we say so: the map starts with "
              "guilds and marks the unknown as unknown."),
  "key_points": [
   "Microbes run decomposition, nitrogen fixation, methane cycling - the planet's chemistry.",
   "Most microbial diversity is uncultured, unnamed, and functionally unstudied.",
   "Microbial composition demonstrably changes plant growth, disease, and carbon storage.",
   "Linking specific taxa to specific functions remains extremely difficult.",
   "Function may live in community interactions rather than individual members."],
  "requirements": [
   "Guild knockouts must map cleanly to function losses, predicting new suppression outcomes.",
   "Confirm: the same guilds load-bearing across different continents and ecosystems.",
   "Refute: function entirely emergent, with no knockout mapping to function loss.",
   "Refute: guild roles so context-dependent that no role map transfers."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim taxa are irrelevant or that every microbe gets a job description.",
   "Uncultured lineages remain marked unknown until evidence assigns them roles."],
  "citations": [CIT_MICROBES],
 },
 {
  "key": "no-return",
  "name": "Why Some Forests Never Come Back After Disturbance",
  "group": "Stability and Collapse",
  "ladder_rank": 9, "ladder_tier": "foundations",
  "description": ("Clear a tropical forest and it may regrow - or it may lock into grassland for "
                  "centuries, even with seeds and rain available. Some disturbed ecosystems bounce "
                  "back; others settle into a new state and refuse to leave. Telling which path a "
                  "disturbed system will take, before committing to restoration, is an unsolved "
                  "problem with enormous stakes."),
  "problem": "What determines whether a disturbed ecosystem recovers its former state or locks into an alternative stable state?",
  "background": ("The alternative-stable-state framework, developed through the 1970s to 2000s, "
                 "says some ecosystems have more than one self-maintaining configuration: forest "
                 "or savanna, clear lake or turbid lake, grassland or shrubland. Each state is held "
                 "in place by feedbacks - adult trees shade out grasses and resist fire; grasses "
                 "fuel fires that kill tree seedlings. Disturbance can push the system across the "
                 "boundary, and then the new state's feedbacks hold it there: this is why "
                 "abandoned Amazonian pastures sometimes stay pasture for decades despite nearby "
                 "seed sources. Hysteresis makes return brutally hard - the conditions that caused "
                 "the flip are not the conditions needed to reverse it. But applying the framework "
                 "is messy: real landscapes are mosaics, feedbacks are hard to measure, and many "
                 "supposed alternative states turn out to be slow transients - systems still "
                 "recovering on century timescales. Managers must decide whether to assist recovery "
                 "or accept the new state, often with incomplete evidence about which state is "
                 "truly stable."),
  "why_it_matters": ("Trillions of dollars in restoration spending, plus the fate of the Amazon and "
                      "other tipping-prone systems, hinge on knowing whether a degraded landscape "
                      "can come back on its own, needs a push, or is locked. Wrong calls waste "
                      "fortunes or abandon recoverable ecosystems."),
  "sig_lens": ("The Signature lens treats the disturbed landscape as a ball on a ridged hillside: "
               "recovery is rolling back uphill, and the question is whether the old valley still "
               "exists or has been filled in."),
  "sol_public": ("The Signature system proposes a valley survey: map the feedbacks holding the "
                 "current state and test whether the old state's feedbacks can still ignite - "
                 "seed, shade, and fire trials that read the landscape's real options. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) alternative states are maintained by measurable feedbacks; "
              "(2) small ignition trials reveal whether old-state feedbacks can restart; (3) slow "
              "transients can be distinguished from true stability by feedback direction. "
              "Reasoning path: survey the disturbed site for the feedbacks of both the former state "
              "(seed rain, shade potential, mycorrhizal networks) and the current state (fire "
              "frequency, grazing pressure, soil changes). Run ignition trials: plant clusters of "
              "native trees, exclude fire and grazers from patches, add seed. If the old state's "
              "feedbacks ignite and spread from the trial patches, the valley still exists - assist "
              "recovery. If trials stall at patch edges, the new state's feedbacks dominate - the "
              "valley is filled, and management should optimize the new state or engineer a novel "
              "one. Proposed mechanism: a recovery-readiness index from feedback surveys plus "
              "ignition-trial outcomes, classifying sites as self-recovering, assistable, or "
              "locked. What would confirm it: the index correctly predicting five-year outcomes of "
              "restoration projects across forest, grassland, and wetland systems. What would kill "
              "it: sites classified locked that recover spontaneously, or assistable sites where "
              "assistance repeatedly fails for unmeasured reasons. What it does NOT claim: that "
              "this is proven, that ignition trials are cheap, or that locked states are "
              "worthless. Where the honest answer is unknown - the century-scale fate of slow "
              "transients - we say so: the survey reads current feedbacks, not deep time."),
  "key_points": [
   "Disturbed systems can recover, need assistance, or lock into alternative stable states.",
   "Feedbacks (fire-grass, shade-tree) hold each state in place; hysteresis blocks easy return.",
   "Amazonian pastures sometimes stay pasture for decades despite seed sources nearby.",
   "Many supposed stable states may be slow century-scale transients instead.",
   "The recovery question decides where restoration money goes and whether it works."],
  "requirements": [
   "The recovery-readiness index must predict five-year restoration outcomes across systems.",
   "Confirm: ignition trials correctly separate assistable from locked sites.",
   "Refute: locked-classified sites recovering spontaneously at meaningful rates.",
   "Refute: assistable sites where assistance repeatedly fails for unmeasured reasons."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim ignition trials are cheap or that locked states lack value.",
   "Century-scale transients are acknowledged as beyond the survey's reach."],
  "citations": [CIT_COLLAPSE],
 },
]

print("entries chunk 1 loaded:", len(ENTRIES))

CIT_FOODWEB = ("May RM. Will a large complex system be stable? Nature. 1972;238:413-414; "
               "Dunne JA et al. Network structure and biodiversity loss in food webs: robustness "
               "increases with connectance. Ecol Lett. 2002;5:558-567.")
CIT_DISPERSAL = ("Nathan R et al. Mechanisms of long-distance dispersal of seeds by wind. "
                 "Nature. 2002;418:409-413; Levin SA et al. The ecology and evolution of seed "
                 "dispersal: a theoretical perspective. Annu Rev Ecol Evol Syst. 2003;34:575-604.")
CIT_RESTOR = ("Suding KN et al. Alternative states and positive feedbacks in restoration ecology. "
              "Trends Ecol Evol. 2004;19:46-53; Society for Ecological Restoration International. "
              "The SER International Primer on Ecological Restoration. 2004.")
CIT_CASCADE = ("Hairston NG, Smith FE, Slobodkin LB. Community structure, population control, and "
               "competition. Am Nat. 1960;94:421-425; Estes JA et al. Trophic downgrading of planet "
               "Earth. Science. 2011;333:301-306.")
CIT_DISTURB = ("Connell JH. Diversity in tropical rain forests and coral reefs. Science. "
               "1978;199:1302-1310; Fox JW. The intermediate disturbance hypothesis should be "
               "abandoned. Trends Ecol Evol. 2013;28:86-92.")
CIT_PRODUCT = ("Lindeman RL. The trophic-dynamic aspect of ecology. Ecology. 1942;23:399-417; "
               "Field CB et al. Primary production of the biosphere: integrating terrestrial and "
               "oceanic components. Science. 1998;281:237-240.")
CIT_NEUTRAL = ("Hubbell SP. The Unified Neutral Theory of Biodiversity and Biogeography. Princeton "
               "Univ Press; 2001; Chesson P. Mechanisms of maintenance of species diversity. Annu "
               "Rev Ecol Syst. 2000;31:343-366.")
CIT_PLANKTON = ("Hutchinson GE. The paradox of the plankton. Am Nat. 1961;95:137-145; "
                "Huisman J, Weissing FJ. Biodiversity of plankton by species oscillations and chaos. "
                "Nature. 1999;402:407-410.")

ENTRIES.extend([
 {
  "key": "food-webs",
  "name": "What Keeps Food Webs From Unraveling",
  "group": "Food Webs and Trophic Dynamics",
  "ladder_rank": 10, "ladder_tier": "foundations",
  "description": ("Every ecosystem is a tangle of who-eats-whom, sometimes thousands of species "
                  "deep. Robert May's 1972 mathematics said such complex webs should be unstable - "
                  "yet they persist for millennia. Something about real food webs defies the "
                  "equations, and ecologists still argue about what that something is."),
  "problem": "What structural features of real food webs keep them stable despite the mathematical prediction that complexity destabilizes?",
  "background": ("Charles Elton mapped the first food webs in the 1920s, showing feeding "
                 "relationships organized in pyramids. Robert May's 1972 paper then dropped a "
                 "bombshell: in random networks, stability requires the product of species number, "
                 "connectance, and interaction strength to stay below a threshold - meaning large "
                 "complex webs should collapse. Real webs are large and complex, yet they endure. "
                 "The resolution hunt found several candidates: real webs are not random - they have "
                 "compartmental structure, with groups of species interacting more within than "
                 "between; most interactions are weak, and weak links dampen oscillations; "
                 "omnivory and food-web loops create alternative pathways when one link breaks; "
                 "body-size structure organizes who can eat whom. Each candidate is supported "
                 "somewhere and questioned somewhere else. The deepest puzzle is that stability "
                 "itself is hard to define and harder to measure in the field - a web can be "
                 "mathematically stable yet ecologically fragile, losing species one by one while "
                 "its equations stay well-behaved."),
  "why_it_matters": ("Fisheries management, pest control, and conservation all remove or add "
                      "species to food webs. Knowing which structural features carry stability tells "
                      "managers which species are load-bearing and which links must not be cut - "
                      "the difference between a managed web and an unraveling one."),
  "sig_lens": ("The Signature lens treats a food web as a suspension bridge: the equations count "
               "cables, but the bridge stands because of how the cables are arranged."),
  "sol_public": ("The Signature system proposes a bridge-inspection protocol: map compartmental "
                 "structure, weak-link damping, and alternative pathways, then score each species "
                 "by how much of the bridge hangs from it. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) stability lives in arrangement, not just species count; "
              "(2) compartments, weak links, and omnivory each contribute measurably; (3) targeted "
              "removals reveal load-bearing structure. Reasoning path: for a real web, compute "
              "three structural scores - modularity (compartment strength), the distribution of "
              "interaction strengths (weak-link damping), and omnivory/loop density (alternative "
              "pathways). Then simulate and, where possible, experimentally perform species "
              "removals, recording which removals cascade and which are absorbed. The species "
              "whose removal cascades are the bridge cables; the structural scores predict where "
              "they are. Proposed mechanism: a load-bearing map of the web that ranks every "
              "species by cascade risk and identifies the structural feature most responsible for "
              "holding each compartment together. What would confirm it: maps that predict "
              "removal outcomes in whole-ecosystem experiments (lake and grassland webs) better "
              "than species-count or connectance-only models. What would kill it: webs where "
              "removal outcomes are dominated by non-trophic factors (disease, behavior) the map "
              "ignores, or structural scores that fail to predict across web types. What it does "
              "NOT claim: that this is proven, that mathematical stability equals ecological "
              "persistence, or that all webs share one stabilizing feature. Where the honest "
              "answer is unknown - the true interaction strengths in most webs - we say so: "
              "strengths are estimated, and the map carries their uncertainty."),
  "key_points": [
   "May 1972: random complex networks should be unstable; real webs persist anyway.",
   "Candidate stabilizers: compartments, weak links, omnivory, body-size structure.",
   "Mathematical stability and ecological persistence are not the same thing.",
   "Real interaction strengths are estimated, rarely measured directly.",
   "Which species are load-bearing decides what management can safely remove."],
  "requirements": [
   "Load-bearing maps must predict removal outcomes in whole-ecosystem experiments.",
   "Confirm: structural scores beat species-count and connectance-only predictions.",
   "Refute: removal outcomes dominated by non-trophic factors the map ignores.",
   "Refute: structural scores that fail to transfer across web types."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not equate mathematical stability with ecological persistence.",
   "Interaction-strength estimates carry explicit uncertainty."],
  "citations": [CIT_FOODWEB],
 },
 {
  "key": "dispersal",
  "name": "How Far Seeds, Spores, and Larvae Really Travel",
  "group": "Global Change and Flux",
  "ladder_rank": 11, "ladder_tier": "foundations",
  "description": ("Every plant, fungus, and marine animal must move its offspring somewhere - yet "
                  "the distances involved are astonishingly hard to measure. A seed may fall at "
                  "the parent's feet or ride a storm across an ocean; a coral larva may settle "
                  "meters away or drift for months. Dispersal shapes everything from forest "
                  "regeneration to marine reserve design, and its long-distance tail is ecology's "
                  "most elusive measurement."),
  "problem": "How far do propagules actually travel, especially the rare long-distance events that matter most, and what controls the dispersal kernel?",
  "background": ("Ecologists have measured dispersal for a century with seed traps, marked "
                 "seeds, and parentage analysis - and consistently found that most propagules stay "
                 "close while a tiny fraction travel enormously far. These rare long-distance "
                 "events dominate colonization, invasion speed, and gene flow, yet they are "
                 "nearly impossible to observe directly: you cannot trap what passes over your "
                 "traps. Models fit dispersal kernels - probability distributions of distance - "
                 "to the data, but the kernel's tail, where the important events live, is "
                 "extrapolated, not measured. Wind dispersal models improved with turbulence "
                 "physics; animal dispersal is tracked with GPS and genetics; marine larvae are "
                 "followed with drifters and otolith chemistry. Each method sees part of the "
                 "picture. The field agrees long-distance dispersal is fat-tailed and crucial, but "
                 "disagrees on how fat, for which species, and how it will change as winds, "
                 "currents, and animal movements shift with climate."),
  "why_it_matters": ("Reserve networks, restoration seed sourcing, invasive-species containment, "
                      "and predictions of range shifts under climate change all depend on the "
                      "dispersal kernel's tail. Misjudge it and reserves are isolated islands, "
                      "restoration seeds come from the wrong climate, and invasions outrun every "
                      "barrier."),
  "sig_lens": ("The Signature lens treats dispersal as a lottery where almost everyone loses "
               "small and a few win enormously - and the jackpot winners write the future."),
  "sol_public": ("The Signature system proposes a jackpot census: combine genetics, physics, and "
                 "rare-event traps to measure the kernel's tail directly instead of extrapolating "
                 "it, then map how the tail responds to weather and behavior. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the dispersal kernel's tail, not its mean, controls "
              "colonization and gene flow; (2) tails can be measured by combining independent "
              "methods; (3) tail shape responds predictably to wind, current, and vector "
              "behavior. Reasoning path: for a target species, deploy three independent "
              "tail-readers - genetic parentage over large plots (who fathered whom, how far), "
              "mechanistic transport models driven by real weather and current data, and "
              "strategic rare-event traps placed where models say jackpots land. Where all three "
              "agree, the tail is measured, not extrapolated. Then perturb: compare tails across "
              "stormy versus calm years, intact versus fragmented landscapes, to learn the tail's "
              "controls. Proposed mechanism: a measured-tail kernel library for key species "
              "groups, with tail-fatness indexed to weather regimes and landscape structure, "
              "feeding directly into reserve-spacing and assisted-migration decisions. What would "
              "confirm it: measured tails predicting colonization of new habitat patches and "
              "invasion front speeds better than extrapolated kernels, across plants, insects, "
              "and marine larvae. What would kill it: the three methods disagreeing "
              "irreconcilably (no stable tail exists to measure), or tails so variable year to "
              "year that no library value transfers. What it does NOT claim: that this is proven, "
              "that every species gets a measured tail, or that tails stay fixed under climate "
              "change. Where the honest answer is unknown - most species' true tails - we say so: "
              "the library starts with key groups and marks the rest as extrapolated."),
  "key_points": [
   "Most propagules stay near home; rare long-distance events dominate colonization and gene flow.",
   "Long-distance events are nearly unobservable directly; kernel tails are extrapolated, not measured.",
   "Wind, animal, and marine methods each see part of the dispersal picture.",
   "The tail is fat and crucial, but how fat - and how it shifts with climate - is unresolved.",
   "Reserve spacing, seed sourcing, and invasion barriers all bet on the tail."],
  "requirements": [
   "Measured tails must beat extrapolated kernels at predicting colonization and invasion speeds.",
   "Confirm: the three independent methods converging on the same tail shape.",
   "Refute: irreconcilable disagreement between methods (no stable tail to measure).",
   "Refute: year-to-year tail variability so large that no library value transfers."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim measured tails for every species or fixed tails under climate change.",
   "Unmeasured species remain explicitly marked as extrapolated."],
  "citations": [CIT_DISPERSAL],
 },
 {
  "key": "restoration",
  "name": "Why Some Restorations Bloom and Others Fail",
  "group": "Restoration and Stewardship",
  "ladder_rank": 12, "ladder_tier": "foundations",
  "description": ("The world has pledged to restore hundreds of millions of hectares of degraded "
                  "land, yet restoration projects fail at alarming rates: planted forests die, "
                  "rewetted wetlands stay degraded, reseeded grasslands revert to weeds. "
                  "Restoration ecology knows many techniques and has famous successes - but no "
                  "reliable way to predict which projects will work before the money is spent."),
  "problem": "What principles actually predict restoration success, and why do similar techniques succeed in one place and fail in another?",
  "background": ("Restoration ecology formalized in the 1980s with the Society for Ecological "
                 "Restoration, founded on the idea that damaged ecosystems can be assisted back "
                 "to health. Early practice was recipe-driven: plant natives, remove invasives, "
                 "reconnect hydrology. Successes piled up - the Kissimmee River, Atlantic Forest "
                 "corridors - and so did failures: massive tree-planting campaigns with 90 percent "
                 "seedling mortality, wetlands that stayed biologically dead after rewetting. "
                 "Theory offered guidance: alternative stable states explain why degraded systems "
                 "resist return; assembly theory says the order of species arrival shapes the "
                 "outcome; the field-of-dreams hypothesis says build the habitat and species will "
                 "come. But each principle works somewhere and fails somewhere else. Recent "
                 "syntheses point to contingency: success depends on the degradation history, the "
                 "landscape context, and whether key feedbacks and mutualists (mycorrhizae, "
                 "pollinators, seed dispersers) are restored alongside the plants. The field has "
                 "principles but not yet a predictive science - and the UN Decade on Ecosystem "
                 "Restoration is spending against that gap."),
  "why_it_matters": ("Hundreds of millions of hectares are pledged for restoration this decade, "
                      "representing one of humanity's largest-ever ecological investments. The "
                      "difference between principled prediction and hopeful planting is measured in "
                      "billions of dollars and the credibility of the entire restoration enterprise."),
  "sig_lens": ("The Signature lens treats restoration as rebuilding a machine from salvaged "
               "parts: the blueprint matters less than which parts are missing and which still "
               "fit together."),
  "sol_public": ("The Signature system proposes a parts-inventory method: before planting, audit "
                 "which ecosystem parts survive (soil, mutualists, seed sources, feedbacks) and "
                 "match the technique to the missing parts - then predict success from inventory "
                 "completeness. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) restoration fails most often from missing parts, not "
              "wrong technique; (2) the critical parts are enumerable per system - soil "
              "structure, mycorrhizal networks, pollinators, dispersers, seed banks, hydrology; "
              "(3) parts interact, so the inventory must capture dependencies. Reasoning path: "
              "before any planting, run a standardized parts inventory of the degraded site - "
              "soil assays, mutualist surveys, seed-bank tests, landscape connectivity mapping, "
              "feedback checks. Score completeness. Then select techniques that supply exactly "
              "the missing parts: inoculate mycorrhizae where fungi are gone, reintroduce "
              "dispersers where seed rain is absent, break feedbacks where the degraded state is "
              "self-maintaining. Predict success probability from inventory completeness plus "
              "technique-to-gap match. Proposed mechanism: a pre-restoration audit protocol "
              "outputting a completeness score, a missing-parts list, and a matched technique "
              "prescription with a success probability. What would confirm it: audited projects "
              "outperforming unaudited matched controls across forests, wetlands, and grasslands, "
              "with success rates tracking the completeness score. What would kill it: projects "
              "with complete inventories and matched techniques failing as often as controls, or "
              "success driven overwhelmingly by weather luck the inventory cannot capture. What "
              "it does NOT claim: that this is proven, that audits are cheap, or that any site "
              "is restorable. Where the honest answer is unknown - the full parts list for most "
              "systems - we say so: the inventory starts with known-critical parts and grows "
              "with evidence."),
  "key_points": [
   "Global restoration pledges cover hundreds of millions of hectares; failure rates are high.",
   "Famous failures: mass plantings with 90 percent mortality, rewetted but biologically dead wetlands.",
   "Candidate principles: alternative states, assembly order, field-of-dreams - each works somewhere.",
   "Missing mutualists and self-maintaining degraded feedbacks are common hidden causes of failure.",
   "The field has principles but not yet a predictive science."],
  "requirements": [
   "Audited projects must outperform matched unaudited controls across three system types.",
   "Confirm: success rates tracking the inventory completeness score.",
   "Refute: complete-inventory projects failing as often as controls.",
   "Refute: success dominated by weather luck the inventory cannot capture."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim audits are cheap or that every site is restorable.",
   "Parts lists are provisional and grow only with evidence."],
  "citations": [CIT_RESTOR],
 },
 {
  "key": "trophic-cascades",
  "name": "How Trophic Cascades Really Work",
  "group": "Food Webs and Trophic Dynamics",
  "ladder_rank": 13, "ladder_tier": "compounded",
  "description": ("Remove wolves and elk explode, willows vanish, rivers change course - the "
                  "Yellowstone story made trophic cascades famous. Add or remove a top predator "
                  "and effects ripple down through the food web to plants and soils. Yet for "
                  "every celebrated cascade there is a predator removal that changed nothing, and "
                  "ecologists still argue about when cascades happen, how far they travel, and "
                  "how strong they really are."),
  "problem": "Under what conditions do top predators trigger trophic cascades, how far down the food web do the effects reach, and what sets their strength?",
  "background": ("The green-world hypothesis of Hairston, Smith, and Slobodkin (1960) proposed "
                 "that predators keep herbivores in check, which is why the world is green. "
                 "Robert Paine's starfish removal experiments showed a single predator holding "
                 "an entire intertidal community's diversity in place. The sea otter-urchin-kelp "
                 "cascade became the textbook marine example; the wolf-elk-aspen story became "
                 "the terrestrial one. But meta-analyses revealed the pattern is uneven: cascades "
                 "are strong and common in aquatic systems, weaker and patchier on land. "
                 "Omnivory, intraguild predation, and predator behavioral effects (prey eating "
                 "less because predators are near - the ecology of fear) all modulate the "
                 "cascade. Some celebrated cases weakened under scrutiny - the Yellowstone story "
                 "is now debated, with climate, hydrology, and human history as rival "
                 "explanations. The field has moved from asking whether cascades exist to asking "
                 "for the rules: what food-web structures transmit them, what dampens them, and "
                 "whether rewilding with predators will reliably restore them."),
  "why_it_matters": ("Rewilding - returning wolves, lynx, otters, sharks - is sold partly on the "
                      "promise of cascades that heal whole ecosystems. If cascades are conditional "
                      "rather than automatic, rewilding plans need the conditions mapped, or they "
                      "risk expensive disappointments and human-wildlife conflict for nothing."),
  "sig_lens": ("The Signature lens treats a cascade as a signal traveling down a noisy wire: the "
               "predator shouts, and each trophic level decides how much of the message to pass on."),
  "sol_public": ("The Signature system proposes a transmission audit: score each trophic link by "
                 "how faithfully it passes top-down signals versus absorbing them, and the "
                 "cascade's reach is the product of the link scores. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) cascades attenuate at each trophic link; (2) link "
              "transmission depends on measurable properties - herbivore diet breadth, plant "
              "defenses, omnivory, predator fear effects; (3) the cascade's reach is roughly the "
              "product of link transmissions. Reasoning path: for a candidate system, score "
              "each link: how specialized are the herbivores (specialists transmit, generalists "
              "absorb), how defended are the plants, how much omnivory short-circuits levels, "
              "how strong are behavior-mediated fear effects. Multiply the scores down the "
              "chain: the predicted cascade reach and strength. Test by comparing predicted "
              "versus observed cascades across predator additions and removals. Proposed "
              "mechanism: a cascade-transmission index per system, telling rewilding planners "
              "which predator returns will ripple to vegetation and which will fizzle at the "
              "herbivore level. What would confirm it: the index predicting outcomes of a dozen "
              "documented predator manipulations (aquatic and terrestrial) better than "
              "presence-absence of the predator alone. What would kill it: strong cascades where "
              "the index predicts fizzle, repeatedly, or cascades driven mainly by fear effects "
              "the link scores miss. What it does NOT claim: that this is proven, that the "
              "Yellowstone story is settled, or exact vegetation responses. Where the honest "
              "answer is unknown - link transmission values in most real webs - we say so: scores "
              "are estimated and the index reports its uncertainty."),
  "key_points": [
   "Trophic cascades: predator changes ripple down to plants and soils; famous in Yellowstone, otters, starfish.",
   "Cascades are strong in aquatic systems, weaker and patchier on land.",
   "Modulators: omnivory, intraguild predation, fear-driven behavioral effects.",
   "Some celebrated cases (Yellowstone) are now actively debated.",
   "Rewilding bets on cascades; the conditions for reliable cascades are the open question."],
  "requirements": [
   "The transmission index must beat predator presence-absence at predicting a dozen documented manipulations.",
   "Confirm: predicted reach matching observed vegetation responses.",
   "Refute: strong cascades where the index predicts fizzle, repeatedly.",
   "Refute: cascades driven mainly by fear effects the link scores miss."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not settle the Yellowstone debate or promise exact vegetation responses.",
   "Link scores are estimates carrying explicit uncertainty."],
  "citations": [CIT_CASCADE],
 },
 {
  "key": "disturbance",
  "name": "Does the Intermediate Disturbance Hypothesis Hold Up?",
  "group": "Stability and Collapse",
  "ladder_rank": 14, "ladder_tier": "compounded",
  "description": ("Too little disturbance and competitors take over; too much and only the tough "
                  "survive; in the middle, diversity peaks. Connell's 1978 intermediate "
                  "disturbance hypothesis is one of ecology's most taught ideas - and one of its "
                  "most embattled. Decades of tests have produced support, refutation, and a "
                  "growing suspicion that the elegant hump shape is an oversimplification."),
  "problem": "Is there really a general hump-shaped relationship between disturbance and diversity, and if so, what are its true conditions and limits?",
  "background": ("Joseph Connell proposed the hypothesis in 1978 to explain tropical forest and "
                 "coral reef diversity: moderate disturbance prevents competitive exclusion "
                 "without killing everything, so diversity peaks in the middle. It became "
                 "textbook orthodoxy and a management guide - mimic natural disturbance regimes. "
                 "Then the counterattack: reviews found as many studies refuting the hump as "
                 "supporting it, with flat, U-shaped, and increasing relationships all reported. "
                 "Critics argued the hypothesis is unfalsifiable as usually stated - disturbance "
                 "is rarely measured independently of its effects, and almost any result can be "
                 "rationalized. Defenders responded with refined versions: the hump appears when "
                 "disturbance is measured properly and competitive exclusion actually operates. "
                 "Recent work suggests the pattern is real but conditional - it needs a real "
                 "competitive hierarchy, disturbances that actually reset competition, and "
                 "appropriate scales. The question has shifted from whether the hump exists to "
                 "mapping exactly where it exists and where it does not."),
  "why_it_matters": ("Disturbance management - prescribed fire, flood pulses, logging regimes - "
                      "is justified by this hypothesis worldwide. If the hump is conditional, "
                      "managers need the conditions, not the slogan; applying intermediate "
                      "disturbance where it does not apply can destroy the diversity it was meant "
                      "to protect."),
  "sig_lens": ("The Signature lens treats disturbance as a referee: the hump appears only when "
               "the game has a dominant player to handicap and the referee actually blows the "
               "whistle on schedule."),
  "sol_public": ("The Signature system proposes a conditions checklist: competitive hierarchy "
                 "present, disturbance resetting competition, scales matched - and the hump is "
                 "predicted only where all three check out. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the hump needs a competitive hierarchy that would "
              "otherwise exclude; (2) disturbance must actually interrupt that exclusion; (3) "
              "the diversity response is scale-dependent. Reasoning path: before invoking the "
              "hypothesis for any system, run the checklist. One: is there a dominant competitor "
              "that wins undisturbed plots (removal experiments say yes or no)? Two: does the "
              "disturbance regime kill or set back that dominant (not just the rare species)? "
              "Three: are diversity and disturbance measured at the scale the organisms "
              "experience? Where all three pass, predict the hump and its peak position; where "
              "any fails, predict no hump - and say so in advance. Proposed mechanism: a "
              "pre-registered prediction protocol that turns the hypothesis from a just-so story "
              "into a testable conditional claim. What would confirm it: pre-registered "
              "predictions across twenty systems correctly calling hump versus no-hump, with "
              "peak positions approximately right. What would kill it: checklist-passing systems "
              "showing no hump, or humps appearing where the checklist fails - either would "
              "show the conditions are wrong. What it does NOT claim: that this is proven, that "
              "the original 1978 statement was correct, or that disturbance is the main driver "
              "of diversity generally. Where the honest answer is unknown - the checklist "
              "status of most managed systems - we say so: the protocol demands measurement, "
              "not assumption."),
  "key_points": [
   "Connell 1978: diversity peaks at intermediate disturbance; a textbook classic.",
   "Empirical record is mixed: humps, flat lines, U-shapes, and increases all reported.",
   "Critics call it unfalsifiable as usually stated; defenders offer conditional versions.",
   "The debate shifted from whether the hump exists to where its conditions hold.",
   "Prescribed fire, floods, and logging regimes worldwide are justified by it."],
  "requirements": [
   "Pre-registered predictions must correctly call hump vs no-hump across twenty systems.",
   "Confirm: peak positions approximately right where humps are predicted.",
   "Refute: checklist-passing systems showing no hump.",
   "Refute: humps appearing where the checklist fails."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not defend the original 1978 statement or claim disturbance drives diversity generally.",
   "Checklist status must be measured per system, never assumed."],
  "citations": [CIT_DISTURB],
 },
 {
  "key": "productivity",
  "name": "What Really Controls Ecosystem Productivity",
  "group": "Global Change and Flux",
  "ladder_rank": 15, "ladder_tier": "compounded",
  "description": ("Why does one grassland grow twice as fast as another a mile away? Net primary "
                  "productivity - the rate ecosystems turn sunlight into living matter - varies "
                  "enormously, and it sets the food available to every animal, the timber in "
                  "every forest, and the carbon in every climate model. Yet partitioning control "
                  "among light, water, nutrients, and biodiversity remains unresolved."),
  "problem": "What actually controls net primary productivity across ecosystems - resources, climate, biodiversity, or their interaction - and how will control shift as the planet changes?",
  "background": ("Raymond Lindeman's 1942 trophic-dynamic paper put energy flow at ecology's "
                 "center, and the International Biological Program spent the 1960s-70s measuring "
                 "productivity worldwide. The broad pattern is clear: productivity follows water "
                 "and energy - deserts are unproductive, tropical forests exuberant. But the "
                 "details resist: Liebig's law of the minimum says one scarcest resource limits "
                 "growth, yet fertilization experiments routinely show co-limitation by nitrogen "
                 "and phosphorus together. CO2 fertilization should be boosting productivity "
                 "globally, and satellites see greening - but the boost saturates and its fate "
                 "in wood versus leaves versus soil is contested. Biodiversity experiments show "
                 "diverse plots produce more, adding a biotic control on top of the abiotic ones. "
                 "Climate models need productivity right to get the carbon cycle right, but they "
                 "disagree sharply on how nutrient limitation will throttle the CO2 response this "
                 "century."),
  "why_it_matters": ("Productivity is the foundation of food security, forestry, fisheries, and "
                      "the land carbon sink. Whether ecosystems keep absorbing a third of human "
                      "CO2 emissions depends on what limits their growth - and every climate "
                      "projection inherits the uncertainty."),
  "sig_lens": ("The Signature lens treats productivity as a factory with four foremen - light, "
               "water, nutrients, diversity - and asks which foreman is actually shouting orders "
               "in each biome."),
  "sol_public": ("The Signature system proposes a foreman audit: factorial addition experiments "
                 "read which resource limits where, and the audit maps how the limiting foreman "
                 "changes with CO2, warming, and diversity. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) productivity is controlled by the interaction of "
              "resources and biotic capacity, not one master variable; (2) limitation is "
              "measurable by factorial addition; (3) the limiting factor shifts predictably with "
              "global change. Reasoning path: run coordinated factorial experiments - add water, "
              "nitrogen, phosphorus, CO2, and diversity in all combinations - across the major "
              "biomes, and read the response surface: which additions matter, which interact. "
              "This maps the current foreman in each biome. Then repeat under elevated CO2 and "
              "warming to watch the foreman change - the critical question being whether "
              "nitrogen or phosphorus limitation throttles the CO2 boost. Proposed mechanism: "
              "a global limitation atlas, updated as experiments report, that climate models and "
              "land managers query for the binding constraint in any region. What would confirm "
              "it: the atlas predicting independent fertilization results and satellite greening "
              "patterns better than single-factor models, and correctly forecasting where the "
              "CO2 boost saturates first. What would kill it: limitation so idiosyncratic per "
              "site that no biome-level atlas transfers, or biotic feedbacks (mycorrhizae mining "
              "new nutrients) systematically defeating the atlas predictions. What it does NOT "
              "claim: that this is proven, exact productivity forecasts, or that experiments are "
              "cheap. Where the honest answer is unknown - belowground limitation in most "
              "systems - we say so: the atlas marks its soil blind spots."),
  "key_points": [
   "Productivity follows water and energy broadly, but the limiting details resist simple rules.",
   "Fertilization experiments show widespread nitrogen-phosphorus co-limitation, not single limits.",
   "Satellites see global greening, but the CO2 boost saturates and its fate is contested.",
   "Diversity adds a biotic control on top of abiotic resources.",
   "Climate models disagree on how nutrient limitation throttles the future carbon sink."],
  "requirements": [
   "The limitation atlas must beat single-factor models on independent fertilization results.",
   "Confirm: correctly forecasting where the CO2 boost saturates first.",
   "Refute: site-level idiosyncrasy so strong that no biome atlas transfers.",
   "Refute: biotic feedbacks systematically defeating atlas predictions."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim exact productivity forecasts or cheap experiments.",
   "Belowground limitation gaps are marked, not papered over."],
  "citations": [CIT_PRODUCT],
 },
 {
  "key": "neutral-niche",
  "name": "Neutral Theory Versus Niche Theory: Who Is Right?",
  "group": "Diversity and Richness",
  "ladder_rank": 16, "ladder_tier": "compounded",
  "description": ("Do species coexist because each has its own special niche, or because they are "
                  "essentially equivalent and diversity is just slow drift? Stephen Hubbell's 2001 "
                  "neutral theory - which assumes species are interchangeable - predicts real "
                  "abundance patterns disturbingly well. The clash between neutral and niche "
                  "explanations is ecology's deepest theoretical divide, and it is not settled."),
  "problem": "How much of species coexistence and abundance patterns is explained by niche differences versus neutral drift of equivalent species?",
  "background": ("Niche theory, from Hutchinson onward, says species coexist by dividing resources "
                 "- different beak sizes, rooting depths, activity times. It is intuitive and "
                 "richly supported by natural history. Then Stephen Hubbell's 2001 Unified Neutral "
                 "Theory showed that assuming all individuals are ecologically equivalent - "
                 "differences are just drift and dispersal - reproduces species-abundance "
                 "distributions, species-area curves, and beta diversity with startling accuracy. "
                 "The neutral model's success was embarrassing: how could a theory that denies "
                 "everything ecologists believe predict so well? Responses came in waves: neutral "
                 "models fail on species identities and trait patterns; they need unrealistic "
                 "assumptions (a single metacommunity, point speciation); and their good fits may "
                 "come from statistical flexibility rather than truth. The emerging synthesis "
                 "treats neutral theory as a null model - the pattern expected if niches did not "
                 "matter - with real communities deviating from neutrality in informative ways. "
                 "But quantifying the split - what fraction of diversity is niche-structured, "
                 "where, and when - remains open, and the answer differs between trees, corals, "
                 "microbes, and birds."),
  "why_it_matters": ("If niches rule, conservation must protect the specific conditions each "
                      "species needs; if neutrality dominates, protecting area and connectivity "
                      "matters more than micro-managing habitats. The theories prescribe different "
                      "reserve designs, restoration recipes, and biodiversity forecasts."),
  "sig_lens": ("The Signature lens treats neutral theory as the blank map: every deviation from "
               "it is a mountain of niche, and the terrain is mapped by measuring the deviations."),
  "sol_public": ("The Signature system proposes a deviation-mapping method: fit the neutral null "
                 "to each community, then measure where reality departs - and the departures, not "
                 "the fits, are the niche signal. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) neutral theory is a valid null model, not a rival "
              "truth; (2) niche processes leave specific signatures - trait clustering, "
              "phylogenetic structure, abundance-identity links - that neutrality cannot "
              "produce; (3) the niche fraction varies by system and scale. Reasoning path: for "
              "each community, fit the neutral model to the species-abundance distribution and "
              "record the fit. Then test the niche signatures: do abundant species share traits "
              "or environments (niche), or are identities random given abundances (neutral)? Do "
              "relatives co-occur more or less than neutral expects? The pattern of deviations "
              "assigns each community a niche-fraction score. Proposed mechanism: a "
              "niche-fraction atlas across taxa and biomes, telling managers where "
              "niche-targeted action (protecting specific conditions) versus area-and-connectivity "
              "action is warranted. What would confirm it: niche-fraction scores predicting "
              "which communities respond to habitat-quality management versus which respond only "
              "to area and connectivity, across trees, birds, and microbes. What would kill it: "
              "niche signatures proving to be statistical artifacts of the neutral model itself, "
              "or scores that fail to predict any management outcome. What it does NOT claim: "
              "that this is proven, that neutrality is true anywhere, or a single global "
              "percentage. Where the honest answer is unknown - the niche fraction in most "
              "microbial and marine systems - we say so: the atlas starts where data exist."),
  "key_points": [
   "Niche theory: species coexist by dividing resources; richly supported by natural history.",
   "Hubbell 2001: assuming species are equivalent reproduces abundance patterns startlingly well.",
   "Neutral models fail on species identities, traits, and need unrealistic assumptions.",
   "Emerging synthesis: neutral as null model, deviations as the niche signal.",
   "The split differs between trees, corals, microbes, and birds - and dictates management."],
  "requirements": [
   "Niche-fraction scores must predict management responses across taxa.",
   "Confirm: deviations from neutral mapping to real trait and phylogenetic structure.",
   "Refute: niche signatures shown to be artifacts of the neutral model itself.",
   "Refute: scores that fail to predict any management outcome."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim neutrality is true anywhere or offer a single global percentage.",
   "Systems lacking data are marked unmapped, not filled in."],
  "citations": [CIT_NEUTRAL],
 },
 {
  "key": "plankton",
  "name": "The Paradox of the Plankton: Why So Many Coexist",
  "group": "Diversity and Richness",
  "ladder_rank": 17, "ladder_tier": "compounded",
  "description": ("A liter of seawater holds hundreds of phytoplankton species, all apparently "
                  "competing for the same handful of resources - light and a few nutrients - in a "
                  "well-mixed environment with no visible niches. G.E. Hutchinson named this the "
                  "paradox of the plankton in 1961, and it remains the sharpest challenge to the "
                  "idea that competition limits diversity."),
  "problem": "How do hundreds of plankton species coexist on a handful of resources in a seemingly uniform environment?",
  "background": ("The competitive exclusion principle says two species competing for the same "
                 "limiting resource cannot coexist - one wins. Yet ocean water, seemingly "
                 "homogeneous and offering only light, nitrogen, phosphorus, and silica, teems "
                 "with phytoplankton diversity. Hutchinson's 1961 paper posed the paradox and "
                 "offered first answers: the ocean is not at equilibrium - seasons, storms, and "
                 "grazing constantly reset competition before exclusion completes. Later "
                 "resolutions multiplied: Huisman and Weissing showed competition itself can "
                 "generate oscillations and chaos, keeping many species in the game; kill-the-winner "
                 "phages and grazers target whichever species gets abundant; fine-scale "
                 "patchiness and thin layers create micro-niches invisible from the deck of a "
                 "ship; light spectra and nutrient ratios offer more niche axes than first "
                 "assumed. Each mechanism demonstrably operates somewhere. But the quantitative "
                 "question stands: how much of the observed diversity does each mechanism "
                 "explain, and is the full paradox actually resolved or just renamed?"),
  "why_it_matters": ("Phytoplankton produce roughly half Earth's oxygen and anchor marine food "
                      "webs and the ocean carbon pump. Whatever maintains their diversity "
                      "maintains the ocean's productivity and its capacity to absorb carbon - and "
                      "climate change is now altering the turbulence, stratification, and nutrient "
                      "regimes the paradox depends on."),
  "sig_lens": ("The Signature lens treats the plankton sea as a game that never ends: no species "
               "wins because the rules keep changing faster than any winner can consolidate."),
  "sol_public": ("The Signature system proposes a mechanism census: in each ocean region, measure "
                 "how much diversity each candidate mechanism (fluctuation, kill-the-winner, "
                 "micro-niches, chaos) accounts for - and the paradox is solved region by region. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) no single mechanism resolves the paradox everywhere; "
              "(2) each mechanism leaves a measurable signature - fluctuation regimes in time "
              "series, phage-to-host ratios, micro-layer structure; (3) mechanisms add up to "
              "observed diversity. Reasoning path: pick contrasting ocean regions - a stable "
              "gyre, a seasonal temperate sea, an upwelling zone. In each, measure the "
              "candidate signatures: temporal variability versus exclusion timescales, viral "
              "lysis rates on dominant species, fine-scale vertical structure, and tests for "
              "chaotic versus stable dynamics. Partition the observed diversity among mechanisms "
              "by comparing regions where each is strong or weak. Proposed mechanism: a "
              "regional mechanism census that states, for each ocean province, which mechanisms "
              "carry the coexistence load and by how much - the paradox resolved as a portfolio, "
              "not a principle. What would confirm it: censuses that predict diversity changes "
              "when a mechanism is altered (e.g., stratification suppressing fluctuation-driven "
              "coexistence) and the prediction holding in time series. What would kill it: "
              "regions where all measured mechanisms are weak yet diversity stays high, implying "
              "a missing major mechanism, or mechanisms that refuse to partition (everything "
              "correlates with everything). What it does NOT claim: that this is proven, that "
              "competitive exclusion is wrong, or exact diversity numbers. Where the honest "
              "answer is unknown - the micro-scale world most plankton inhabit - we say so: "
              "thin layers and micro-patches are still largely unmapped."),
  "key_points": [
   "Hundreds of phytoplankton species share a handful of resources in seemingly uniform water.",
   "Hutchinson 1961: the paradox - competitive exclusion says this should be impossible.",
   "Candidate resolutions: non-equilibrium, chaos, kill-the-winner, micro-niches, hidden niche axes.",
   "Each mechanism works somewhere; the quantitative partition is unresolved.",
   "Phytoplankton make half Earth's oxygen and drive the ocean carbon pump."],
  "requirements": [
   "Regional censuses must predict diversity changes when a mechanism is altered.",
   "Confirm: mechanism strengths partitioning observed diversity across contrasting regions.",
   "Refute: high-diversity regions where all measured mechanisms are weak.",
   "Refute: mechanisms that refuse to partition (total confounding)."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim competitive exclusion is wrong or exact diversity numbers.",
   "The micro-scale habitat remains largely unmapped and is marked as such."],
  "citations": [CIT_PLANKTON],
 },
])

print("entries chunk 2 done:", len(ENTRIES))

CIT_DILUTION = ("Ostfeld RS, Keesing F. Effects of host diversity on infectious disease. Annu Rev "
                "Ecol Evol Syst. 2012;43:157-182; Civitello DJ et al. Biodiversity inhibits parasites: "
                "meta-analysis of the dilution effect. Proc Natl Acad Sci USA. 2015;112:8667-8671.")
CIT_CARBON = ("Pan Y et al. A large and persistent carbon sink in the world's forests. Science. "
              "2011;333:988-993; Hubau W et al. Asynchronous carbon sink saturation in African and "
              "Amazonian tropical forests. Nature. 2020;579:80-87.")
CIT_DIVSTAB = ("Tilman D, Downing JA. Biodiversity and stability in grasslands. Nature. "
               "1994;363:65-66; Ives AR, Carpenter SR. Stability and diversity of ecosystems. "
               "Science. 2007;317:58-62.")
CIT_META = ("Leibold MA et al. The metacommunity concept: a framework for multi-scale community "
            "ecology. Ecology. 2004;85:1141-1150; Holyoak M et al. Metacommunities: Spatial Dynamics "
            "and Ecological Communities. Univ Chicago Press; 2005.")
CIT_JC = ("Janzen DH. Herbivores and the number of tree species in tropical forests. Am Nat. "
          "1970;104:501-528; Connell JH. On the role of natural enemies in preventing competitive "
          "exclusion in some marine animals and in rain forest trees. In: Dynamics of Populations. 1971.")
CIT_EWS = ("Carpenter SR et al. Early warnings of regime shifts: a whole-ecosystem experiment. "
           "Science. 2011;333:1079-1082; Scheffer M et al. Early-warning signals for critical "
           "transitions. Nature. 2009;461:53-59.")
CIT_LEGACY = ("Peterson GD. Contagious disturbance, ecological memory, and the emergence of landscape "
              "pattern. Ecosystems. 2002;5:329-338; Johnstone JF et al. Changing disturbance regimes, "
              "ecological memory, and forest resilience. Front Ecol Environ. 2016;14:369-378.")

ENTRIES.extend([
 {
  "key": "dilution",
  "name": "Does Biodiversity Dilute Disease?",
  "group": "Global Change and Flux",
  "ladder_rank": 18, "ladder_tier": "compounded",
  "description": ("Lyme disease is worse where mammal diversity is low; West Nile virus hits "
                  "harder where bird diversity is low. The dilution effect proposes that diverse "
                  "communities protect against disease because incompetent hosts waste the "
                  "pathogen's transmission opportunities. It is an appealing idea with famous "
                  "examples - and a growing list of counterexamples."),
  "problem": "Does higher biodiversity generally reduce infectious disease risk (the dilution effect), or does the effect depend on the system?",
  "background": ("The dilution effect grew from Lyme disease research in the northeastern United "
                 "States: forest fragments with few mammal species had more infected ticks, "
                 "because the white-footed mouse - a superb reservoir - dominated, while diverse "
                 "forests spread tick meals across poor reservoirs like squirrels and opossums. "
                 "Similar patterns appeared for West Nile virus, hantavirus, and amphibian "
                 "chytrid fungus. The mechanism is intuitive: add species that are bad at "
                 "transmitting, and each vector bite or contact is more likely wasted. But then "
                 "the counterexamples arrived: in some systems diverse communities amplify "
                 "disease, because added species are good hosts or increase vector survival. "
                 "Meta-analyses split - one large synthesis found net dilution across systems, "
                 "others found the effect depends on scale, on whether diversity loss is "
                 "non-random (it usually is - the best reservoirs often persist), and on how "
                 "disease is measured (prevalence versus human risk). The field now debates not "
                 "whether dilution can happen but how general it is - and whether biodiversity "
                 "conservation can honestly be sold as disease protection."),
  "why_it_matters": ("If dilution is general, then conserving biodiversity is also public health "
                      "policy, and land-use decisions should weigh disease risk. If it is "
                      "conditional, then promising disease protection from conservation risks "
                      "credibility when counterexamples strike - and pandemic prevention needs "
                      "the real rules, not the slogan."),
  "sig_lens": ("The Signature lens treats hosts as gamblers at a transmission table: dilution "
               "happens when the new players at the table are bad bets for the pathogen."),
  "sol_public": ("The Signature system proposes a table audit: for each host community, score "
                 "every species' competence and the order species are lost - and dilution is "
                 "predicted only where lost species are poor transmitters. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) dilution versus amplification depends on the competence "
              "of the species gained or lost, not on richness per se; (2) species loss under "
              "disturbance is non-random and predictable; (3) competence can be measured or "
              "estimated from traits. Reasoning path: for a disease system, measure host "
              "competence (probability an infected host passes the pathogen on) for the "
              "community's species, and determine the typical disassembly order - which species "
              "vanish first as habitat degrades. If the first-lost species are poor transmitters "
              "and the persisters are good ones, diversity loss amplifies disease; reverse the "
              "order and loss dilutes it. The prediction is made before the outbreak data are "
              "consulted. Proposed mechanism: a competence-ordered audit that forecasts, per "
              "landscape, whether ongoing biodiversity loss will raise or lower disease risk - "
              "turning the dilution debate into a measurement protocol. What would confirm it: "
              "audits correctly predicting the direction of the diversity-disease relationship "
              "across a dozen systems (Lyme, West Nile, chytrid, hantavirus, schistosomiasis) "
              "better than richness alone. What would kill it: systems where competence-order "
              "predicts dilution but amplification is observed, repeatedly, or competence so "
              "plastic across contexts that no audit transfers. What it does NOT claim: that "
              "this is proven, that conservation always protects health, or exact case counts. "
              "Where the honest answer is unknown - competence values for most wildlife hosts - "
              "we say so: the audit starts with measured systems and marks the rest."),
  "key_points": [
   "Dilution effect: diverse host communities can waste pathogen transmission opportunities.",
   "Famous cases: Lyme disease, West Nile virus, amphibian chytrid fungus.",
   "Counterexamples exist where diversity amplifies disease instead.",
   "The effect hinges on which species are lost first and how competent each host is.",
   "Whether conservation can be sold as disease protection is the applied stakes."],
  "requirements": [
   "Competence-ordered audits must beat richness alone across a dozen disease systems.",
   "Confirm: correctly forecasting whether biodiversity loss raises or lowers risk per landscape.",
   "Refute: repeated cases where the audit predicts dilution but amplification is observed.",
   "Refute: host competence so plastic that no audit transfers across contexts."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim conservation always protects health or exact case counts.",
   "Unmeasured host competences are marked, not assumed."],
  "citations": [CIT_DILUTION],
 },
 {
  "key": "forest-carbon",
  "name": "The Forest Carbon Question: Sink or Source in a Warmer World",
  "group": "Global Change and Flux",
  "ladder_rank": 19, "ladder_tier": "compounded",
  "description": ("Forests currently soak up roughly a third of humanity's carbon dioxide "
                  "emissions - a free climate service worth trillions. But the sink is showing "
                  "cracks: the Amazon's uptake is weakening, droughts and fires flip regions "
                  "from sink to source, and models disagree wildly on how long the service "
                  "lasts. Whether forests remain our ally or become a carbon source is one of "
                  "the highest-stakes open questions in ecology."),
  "problem": "How long will forests keep absorbing net carbon, what will saturate or reverse the sink, and can we tell in time?",
  "background": ("The global forest carbon sink was quantified in the 2000s-2010s from forest "
                 "inventories: about 2-3 billion tons of carbon per year, roughly a third of "
                 "fossil emissions, with CO2 fertilization, nitrogen deposition, and regrowth on "
                 "abandoned farmland as drivers. Then the warnings: long-term Amazon plots "
                 "showed the sink weakening since the 1990s as mortality rose; the 2005, 2010, "
                 "and 2015 droughts each temporarily flipped the Amazon toward source; "
                 "African forests show different timing, saturating asynchronously. Fire, "
                 "drought, pests, and heat each attack the sink through different pathways - "
                 "killing trees (stock loss), slowing growth (flux loss), or both. Earth system "
                 "models span an enormous range: some keep a strong land sink through 2100, "
                 "others flip the tropics to a source within decades. The disagreement traces "
                 "to mortality - models handle growth physiology far better than they handle "
                 "tree death, which is episodic, poorly observed, and mechanistically murky."),
  "why_it_matters": ("Net-zero plans worldwide count on the forest sink continuing; carbon "
                      "budgets assume it. If the sink saturates decades early, allowable "
                      "emissions shrink drastically and warming accelerates. This is the "
                      "ecological variable with the largest direct leverage on climate policy."),
  "sig_lens": ("The Signature lens treats the forest sink as a business running on thin "
               "margins: growth is revenue, mortality is cost, and drought is a recession that "
               "can bankrupt the operation."),
  "sol_public": ("The Signature system proposes a margin watch: track growth revenue versus "
                 "mortality cost in real time across the major forest regions, and the sink's "
                 "future is read from the margin trend, not from growth alone. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the net sink is growth minus mortality, and mortality "
              "is the volatile term; (2) mortality responds to drought, heat, and pests on "
              "measurable thresholds; (3) regional margins can be tracked with plots plus "
              "remote sensing. Reasoning path: for each major forest region, maintain the "
              "margin ledger - plot-measured growth and mortality, satellite-observed "
              "disturbance, drought indices. Fit mortality's response to climate stress from "
              "past droughts (the Amazon's 2005/2010/2015 events are calibration gold). "
              "Project the margin under warming scenarios: where mortality's climate response "
              "outruns growth's CO2 response, the sink saturates and flips. The output is a "
              "regional flip-clock, not a single global date. Proposed mechanism: a living "
              "margin-watch dashboard per forest region, updated as new plot censuses and "
              "droughts arrive, giving carbon-budget planners the sink's honest trajectory. "
              "What would confirm it: margin-watch flip warnings preceding observed regional "
              "sink-to-source transitions in the coming decades, and retrospective skill on "
              "past drought events. What would kill it: mortality driven by processes with no "
              "climate signal the watch can track (novel pests, synchronized senescence), or "
              "growth responses systematically exceeding projections. What it does NOT claim: "
              "that this is proven, exact flip dates, or that management can preserve the sink "
              "everywhere. Where the honest answer is unknown - tree mortality mechanisms in "
              "most forests - we say so: the watch tracks what is measurable and marks the "
              "rest."),
  "key_points": [
   "Forests absorb roughly a third of fossil CO2 emissions - a massive free climate service.",
   "The Amazon sink has weakened since the 1990s; African forests saturate on different timing.",
   "Droughts, fires, pests, and heat attack the sink through growth loss and mortality.",
   "Models disagree hugely because tree mortality is poorly observed and poorly modeled.",
   "Net-zero plans and carbon budgets assume the sink continues."],
  "requirements": [
   "Margin-watch warnings must precede observed regional sink-to-source transitions.",
   "Confirm: retrospective skill on past drought-driven sink collapses.",
   "Refute: mortality dominated by processes with no trackable climate signal.",
   "Refute: growth responses systematically exceeding margin-watch projections."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim exact flip dates or that management can preserve every sink.",
   "Mortality mechanisms remain largely unknown and are marked as such."],
  "citations": [CIT_CARBON],
 },
 {
  "key": "diversity-stability",
  "name": "Does Biodiversity Really Make Ecosystems Stable?",
  "group": "Stability and Collapse",
  "ladder_rank": 20, "ladder_tier": "compounded",
  "description": ("Diverse grasslands weather droughts better than monocultures - or so the "
                  "experiments say. The diversity-stability hypothesis claims biodiversity "
                  "buffers ecosystems against disturbance, and it underpins much of conservation "
                  "rhetoric. But stability has many meanings, the evidence is uneven across "
                  "systems, and some diverse systems are famously fragile."),
  "problem": "Does biodiversity causally increase ecosystem stability, which kinds of stability, and under what conditions?",
  "background": ("The idea is old - Elton suggested diverse communities resist invasion - but "
                 "the modern debate ignited with May's 1972 mathematics suggesting complexity "
                 "destabilizes, directly contradicting field intuition. Tilman's Cedar Creek "
                 "experiments then showed diverse grassland plots had more stable productivity "
                 "year to year, especially through drought: when one species faltered, others "
                 "compensated - the portfolio effect. Meta-analyses largely support a positive "
                 "diversity-stability link for productivity. But complications abound: stability "
                 "means different things - resistance to change, resilience after change, low "
                 "variability - and diversity affects each differently. Diverse tropical "
                 "forests can be fragile to drought; diverse coral reefs bleach catastrophically. "
                 "Some argue the experiments measure the wrong stability, or that the "
                 "portfolio effect is statistical inevitability rather than ecology. The field "
                 "agrees diversity often stabilizes aggregate function; it disagrees on "
                 "generality, mechanism, and whether the effect is big enough to matter for "
                 "management."),
  "why_it_matters": ("'Biodiversity keeps ecosystems stable' is one of conservation's most-used "
                      "arguments, quoted to justify protected areas and restoration spending. If "
                      "the link is conditional, advocates need the conditions; overstating it "
                      "risks the argument collapsing the first time a diverse system crashes."),
  "sig_lens": ("The Signature lens treats diversity as an investment portfolio: stability is "
               "the dividend, and the question is which assets actually pay it under stress."),
  "sol_public": ("The Signature system proposes a portfolio audit: decompose stability into "
                 "statistical averaging, compensatory dynamics, and selection effects - and "
                 "credit diversity only with the portion it truly earns. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) observed stability has three components - statistical "
              "averaging, true compensatory dynamics, and dominant-species selection; (2) only "
              "the compensatory component is genuinely ecological; (3) components are "
              "separable with species-level time series. Reasoning path: for each system with "
              "long-term species-level data, decompose aggregate stability: the statistical "
              "component is what random, uncorrelated species would give; the selection "
              "component is the contribution of the single most stable dominant; the remainder "
              "is compensatory dynamics - species genuinely trading off through bad years. "
              "Credit diversity only with the compensatory remainder. Then test which systems "
              "show real compensation and under which disturbances. Proposed mechanism: a "
              "stability-decomposition protocol that reports, per system, how much stability "
              "diversity truly buys - the honest number behind the slogan. What would confirm "
              "it: decompositions across grasslands, forests, and plankton showing the "
              "compensatory component predicting which systems actually resist real "
              "disturbances, while statistical and selection components do not. What would "
              "kill it: compensatory components near zero everywhere (stability is all "
              "statistics and dominants), or components that cannot be separated in practice. "
              "What it does NOT claim: that this is proven, that diversity never stabilizes, "
              "or a single stability definition. Where the honest answer is unknown - "
              "species-level time series for most ecosystems - we say so: the protocol needs "
              "data most systems lack."),
  "key_points": [
   "Experiments show diverse plots have more stable productivity; the portfolio effect is the mechanism.",
   "May 1972 mathematics pointed the opposite way - complexity destabilizing.",
   "Stability has multiple meanings: resistance, resilience, low variability - diversity affects each differently.",
   "Diverse forests and reefs can still crash; the link is conditional.",
   "The slogan outruns the evidence; the honest magnitude is the open question."],
  "requirements": [
   "Decompositions must show the compensatory component predicting real disturbance resistance.",
   "Confirm: replication across grasslands, forests, and plankton systems.",
   "Refute: compensatory components near zero everywhere.",
   "Refute: components that cannot be separated with real data."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim diversity never stabilizes or impose one stability definition.",
   "Systems lacking species-level time series are marked unmeasurable, not assumed."],
  "citations": [CIT_DIVSTAB],
 },
 {
  "key": "metacommunity",
  "name": "Dispersal or Local Forces: What Assembles Communities?",
  "group": "Diversity and Richness",
  "ladder_rank": 21, "ladder_tier": "compounded",
  "description": ("Why does this pond hold these species and the next pond different ones? Every "
                  "local community is shaped by two forces: local conditions selecting who can "
                  "live there, and dispersal delivering who arrives. The metacommunity framework "
                  "says you cannot understand one pond without the others - but partitioning "
                  "credit between dispersal and local forces remains stubbornly difficult."),
  "problem": "How much of local community composition is set by dispersal among patches versus local environmental filtering and interactions?",
  "background": ("Early ecology treated communities as local products of climate and competition. "
                 "Island biogeography added the regional view: immigration matters. The "
                 "metacommunity concept, formalized around 2002-2004 by Leibold and colleagues, "
                 "unified four perspectives - patch dynamics, species sorting, mass effects, and "
                 "the neutral view - as points on a dispersal gradient. With little dispersal, "
                 "local forces rule and patches diverge by environment (species sorting); with "
                 "massive dispersal, everything mixes and local conditions matter less (mass "
                 "effects). The framework is elegant and widely adopted. But applying it is "
                 "hard: dispersal rates are rarely measured directly, environmental and spatial "
                 "variables are correlated (nearby ponds share climate), and statistical "
                 "partitioning methods keep being shown to misattribute. The field has the "
                 "right question and a beautiful framework, but the empirical partition - the "
                 "actual percentages for real landscapes - is still mostly guesswork."),
  "why_it_matters": ("Reserve design, corridor placement, restoration seed sourcing, and invasive "
                      "species control all hinge on whether local communities are dispersal-limited "
                      "or environmentally sorted. Build corridors where sorting rules and you waste "
                      "money; ignore dispersal where it rules and reserves become isolated zoos."),
  "sig_lens": ("The Signature lens treats the landscape as a set of kitchens: local forces are "
               "the recipes, dispersal is the delivery service - and the menu depends on which "
               "matters more."),
  "sol_public": ("The Signature system proposes a delivery audit: experimentally vary dispersal "
                 "while holding environment constant (and vice versa) to read each force's share "
                 "directly instead of partitioning it statistically. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) dispersal and local forces are separable by experiment, "
              "not just statistics; (2) small, clever manipulations can move a system along the "
              "dispersal gradient; (3) the partition is landscape-specific, not universal. "
              "Reasoning path: pick pond, patch, or fragment networks and run crossed "
              "manipulations - add or block dispersal (stocking, barriers, corridors) crossed "
              "with altering local conditions (nutrients, predators, habitat structure). The "
              "response of community composition to each manipulation, and their interaction, "
              "reads the forces' shares directly: if blocking dispersal homogenizes nothing but "
              "changing nutrients reshuffles everything, sorting rules. Proposed mechanism: a "
              "manipulative partition protocol that outputs dispersal-share versus local-share "
              "for real landscapes, replacing statistical guesswork with experimental reading. "
              "What would confirm it: protocols across pond, grassland-fragment, and marine "
              "networks yielding stable, replicable partitions that predict responses to new "
              "management (corridor building, nutrient changes). What would kill it: "
              "manipulations that cannot move systems along the gradient without side effects "
              "that confound the reading, or partitions that flip wildly between years. What it "
              "does NOT claim: that this is proven, that experiments are easy or cheap, or a "
              "universal percentage. Where the honest answer is unknown - the true dispersal "
              "rates in most landscapes - we say so: the protocol measures effects of "
              "manipulated dispersal, not natural rates directly."),
  "key_points": [
   "Local communities are shaped by both local forces and dispersal from the region.",
   "The metacommunity framework unifies four views along a dispersal gradient.",
   "Dispersal rates are rarely measured; environment and space are confounded.",
   "Statistical partitioning methods have repeatedly been shown to misattribute.",
   "Corridors, reserves, and restoration all bet on which force dominates."],
  "requirements": [
   "Manipulative partitions must yield stable, replicable shares across network types.",
   "Confirm: partitions predicting responses to new corridor or nutrient management.",
   "Refute: manipulations whose side effects confound every reading.",
   "Refute: partitions flipping wildly between years with no pattern."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim easy experiments or a universal dispersal percentage.",
   "Natural dispersal rates remain largely unmeasured and are marked as such."],
  "citations": [CIT_META],
 },
 {
  "key": "janzen-connell",
  "name": "Do Plant-Soil Feedbacks Explain Forest Diversity?",
  "group": "Diversity and Richness",
  "ladder_rank": 22, "ladder_tier": "compounded",
  "description": ("In 1970-71, Daniel Janzen and Joseph Connell proposed a beautiful idea: seeds "
                  "that fall near their parent are killed by the parent's specialized enemies, "
                  "so no tree species can dominate - and that is why tropical forests hold so "
                  "many species. The Janzen-Connell hypothesis is elegant, famous, and still "
                  "not proven to carry the weight assigned to it."),
  "problem": "How much of tropical forest diversity is actually maintained by Janzen-Connell effects - specialized enemies killing seeds and seedlings near parent trees?",
  "background": ("Janzen (1970) and Connell (1971) independently argued that host-specific "
                 "herbivores and pathogens accumulate near adult trees, creating a kill zone "
                 "where a species' own offspring cannot survive - spacing adults apart and "
                 "preventing dominance. Early tests were supportive: seedlings survived better "
                 "far from parents, and fungicide experiments fingered soil pathogens. The "
                 "hypothesis became the leading explanation for tropical tree diversity. But "
                 "quantification proved hard: most tests measure seedling survival, not the "
                 "population-level effect on diversity; enemies are often less specialized than "
                 "assumed; and models show the effect must be strong and widespread to maintain "
                 "hundreds of species, stronger than field measurements typically find. Recent "
                 "work adds nuance: mycorrhizal networks can reverse the effect (helping "
                 "seedlings near parents), and the strength varies hugely among species. The "
                 "field agrees Janzen-Connell effects are real; it disagrees on whether they "
                 "are the engine of hyperdiversity or a contributing detail."),
  "why_it_matters": ("If specialized enemies maintain tropical diversity, then forest "
                      "fragmentation - which disrupts enemy communities - could unravel "
                      "diversity from below, and restoration must replant enemy communities "
                      "alongside trees. If the effect is minor, conservation should focus "
                      "elsewhere."),
  "sig_lens": ("The Signature lens treats each adult tree as surrounded by an invisible minefield "
               "laid by its own enemies - and asks whether the minefield is dense enough to hold "
               "back an army of seedlings."),
  "sol_public": ("The Signature system proposes a minefield census: measure kill-zone strength "
                 "per species across whole forest plots, then test whether the measured "
                 "strengths are enough, in models, to maintain the observed diversity. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) Janzen-Connell strength is measurable per species as "
              "distance/density-dependent mortality; (2) whole-plot censuses can capture it for "
              "many species at once; (3) models can translate measured strengths into "
              "diversity maintained. Reasoning path: in large mapped forest plots, measure "
              "seedling survival as a function of distance to and density of conspecific "
              "adults for as many species as possible, with pathogen-exclusion treatments "
              "identifying the enemy agents. This yields a minefield-strength distribution. "
              "Feed the measured strengths into a forest simulator: does the observed diversity "
              "persist, or does the model forest collapse to a few dominants? Proposed "
              "mechanism: a minefield census plus simulator test that outputs the fraction of "
              "each forest's diversity attributable to Janzen-Connell effects - the first "
              "quantitative answer to how much the hypothesis really explains. What would "
              "confirm it: censuses in three major tropical forests where measured strengths "
              "sustain most observed diversity in the simulator, and weakening the effect "
              "(pathogen removal plots) measurably reduces local diversity. What would kill "
              "it: measured strengths too weak to maintain even a tenth of observed diversity "
              "in any forest, or mycorrhizal rescue reversing the effect for most species. "
              "What it does NOT claim: that this is proven, that enemies are always "
              "specialized, or exact diversity fractions. Where the honest answer is unknown "
              "- the enemy agents for most tree species - we say so: the census measures "
              "mortality patterns first, agents second."),
  "key_points": [
   "Janzen-Connell 1970-71: specialized enemies kill offspring near parents, preventing dominance.",
   "Seedling survival is higher away from parents; soil pathogens are implicated.",
   "Most tests measure seedling survival, not the population-level diversity effect.",
   "Enemies are often less specialized than assumed; mycorrhizae can reverse the effect.",
   "Whether it is the engine of hyperdiversity or a contributing detail is unresolved."],
  "requirements": [
   "Measured strengths must sustain most observed diversity in forest simulators.",
   "Confirm: pathogen-removal plots measurably reducing local diversity.",
   "Refute: strengths too weak to maintain even a tenth of diversity in any forest.",
   "Refute: mycorrhizal rescue reversing the effect for most species."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim enemies are always specialized or exact diversity fractions.",
   "Unidentified enemy agents are marked unknown until evidence names them."],
  "citations": [CIT_JC],
 },
 {
  "key": "early-warning",
  "name": "Can We See Ecosystem Collapse Coming?",
  "group": "Stability and Collapse",
  "ladder_rank": 23, "ladder_tier": "compounded",
  "description": ("Theory says systems approaching a tipping point show warning signs: slower "
                  "recovery from small nudges, rising variance, flickering between states. "
                  "These early-warning signals work beautifully in models and in a few "
                  "whole-lake experiments - but in messy real ecosystems they are plagued by "
                  "false alarms and missed calls. Whether we can actually see collapse coming "
                  "is still open."),
  "problem": "Do reliable early-warning signals of ecosystem tipping points exist that work in real, noisy, managed ecosystems - not just models?",
  "background": ("The theory of critical slowing down is clean: near a threshold, a system's "
                 "restoring forces weaken, so it recovers slowly from perturbations, fluctuates "
                 "more, and correlates with its own past (rising autocorrelation). Marten "
                 "Scheffer's group championed these as generic leading indicators around 2009, "
                 "and Stephen Carpenter's team demonstrated them in a whole-lake experiment - "
                 "adding predators to one lake while monitoring both, they watched variance and "
                 "autocorrelation rise before the food web flipped. It was a landmark. But "
                 "field applications stumbled: the signals need long, high-frequency, "
                 "stationary time series that management rarely has; they fire false alarms in "
                 "systems that never tip; different indicators disagree; and some collapses "
                 "come from external shocks with no internal warning at all. The field now "
                 "distinguishes what the signals can do (flag rising fragility in well-observed "
                 "systems) from what managers wish they did (give a date for the collapse)."),
  "why_it_matters": ("A working early-warning system for fisheries, rangelands, reefs, and "
                      "lakes would be the most valuable monitoring tool in applied ecology - "
                      "time to act before the flip instead of expensive restoration after. "
                      "False confidence in broken signals is worse than no signals at all."),
  "sig_lens": ("The Signature lens treats early warnings as a smoke detector: the question is "
               "not whether smoke exists before fire, but whether the detector can tell smoke "
               "from steam in a busy kitchen."),
  "sol_public": ("The Signature system proposes a detector calibration: test every candidate "
                 "signal against libraries of tipped and untipped real time series, and deploy "
                 "only the signals whose false-alarm rate is measured and acceptable. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) critical slowing down is real but not universal; (2) "
              "signal reliability can only be established empirically, against real tipped and "
              "untipped series; (3) managers need false-alarm rates, not just theory. Reasoning "
              "path: assemble the library - every long ecosystem time series where the outcome "
              "(tipped or not) is known: lakes, fisheries, rangelands, reefs. Run every "
              "candidate indicator (variance, autocorrelation, skewness, flickering, recovery "
              "rate) across the library with standardized windows. Score each indicator by "
              "hits, false alarms, and lead time. Deploy only indicators with measured "
              "reliability, reported as explicit odds: this signal at this strength has "
              "preceded tips X percent of the time with Y percent false alarms. Proposed "
              "mechanism: a calibrated warning panel - not a single magic metric but a scored "
              "set of indicators with known error rates, like a medical screening battery. "
              "What would confirm it: the panel flagging real impending transitions in "
              "ongoing monitoring programs (fisheries, lakes) with lead time enough to act, "
              "at the calibrated false-alarm rate. What would kill it: false-alarm rates so "
              "high in real series that no indicator beats chance, or tipped systems that "
              "consistently show no signal because shocks, not bifurcations, dominate. What "
              "it does NOT claim: that this is proven, that signals give collapse dates, or "
              "that unmonitored systems can be warned. Where the honest answer is unknown - "
              "the true base rate of tipping in most systems - we say so: the odds are "
              "conditional on the library, not universal."),
  "key_points": [
   "Critical slowing down: near thresholds, recovery slows, variance and autocorrelation rise.",
   "Demonstrated in models and a landmark whole-lake experiment (Carpenter 2011).",
   "Field use is hampered by short noisy series, false alarms, and disagreeing indicators.",
   "Some collapses come from external shocks with no internal warning possible.",
   "The gap is between flagging fragility and predicting collapse dates."],
  "requirements": [
   "Calibrated indicators must flag real impending transitions with actionable lead time.",
   "Confirm: observed false-alarm rates matching the calibrated rates in new systems.",
   "Refute: no indicator beating chance across the real-series library.",
   "Refute: tipped systems consistently showing no signal (shock-dominated collapses)."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim signals give collapse dates or work in unmonitored systems.",
   "Base rates are conditional on the library, never presented as universal."],
  "citations": [CIT_EWS],
 },
 {
  "key": "legacy",
  "name": "How the Past Haunts Ecosystems",
  "group": "Stability and Collapse",
  "ladder_rank": 24, "ladder_tier": "compounded",
  "description": ("A forest's future is written partly by fires a century ago; a grassland's "
                  "plants remember plowing that ended decades back. Ecological memory - the "
                  "way past conditions shape present dynamics through seed banks, soil "
                  "legacies, and surviving organisms - is widely acknowledged and poorly "
                  "quantified. How long the past grips the present, and through which "
                  "channels, remains an open question."),
  "problem": "How long do ecological legacies persist, through which mechanisms, and how do they alter ecosystem responses to new disturbances?",
  "background": ("Ecologists have long known history matters: old-field succession follows "
                 "different paths depending on past farming, and forest composition reflects "
                 "centuries-old land use. The concept sharpened into ecological memory and "
                 "legacies in the 2000s: information legacies (surviving organisms, seed "
                 "banks, sprouting roots), material legacies (soil carbon, nutrients, dead "
                 "wood), and process legacies (altered fire or flood regimes). Memory can be "
                 "adaptive - legacies help systems recover - or maladaptive, locking in "
                 "degraded states. Climate change makes memory urgent: as disturbance regimes "
                 "shift, systems with long memory may respond to today's fires with "
                 "yesterday's adaptations. But memory is hard to measure: it requires knowing "
                 "the past (often unrecorded), separating legacy effects from current "
                 "conditions, and tracking slow variables over decades. The field can list "
                 "legacy mechanisms but cannot yet say, for a given system, how much of its "
                 "behavior is memory versus present conditions."),
  "why_it_matters": ("Management assumes systems respond to current conditions; if half the "
                      "response is actually memory, then prescriptions misfire. Restoration "
                      "must work with or against legacies, and climate adaptation must reckon "
                      "with systems responding to vanished pasts."),
  "sig_lens": ("The Signature lens treats ecosystems as institutions with institutional "
               "memory: the past is stored in living archives, and every decision is "
               "appealed to precedent."),
  "sol_public": ("The Signature system proposes a memory audit: inventory the living and "
                 "material archives (seed banks, soils, survivors, altered regimes), date "
                 "them, and measure how much of current dynamics each archive explains. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) legacies are carried by identifiable archives - "
              "biological, material, and process; (2) each archive has a decay timescale that "
              "can be estimated; (3) legacy effects are separable from current-condition "
              "effects by comparing sites with shared present but different pasts. Reasoning "
              "path: for a landscape, inventory the archives - seed-bank viability and age "
              "structure, soil carbon and nutrient pools with their turnover times, surviving "
              "organisms as information carriers, and regime alterations like fire exclusion. "
              "Then exploit natural experiments: sites with similar current conditions but "
              "different histories (old fields of different ages, forests with different fire "
              "pasts). The divergence between them, tracked over time, is the memory signal; "
              "its decay rate is the memory timescale. Proposed mechanism: a memory-timescale "
              "map per landscape stating which pasts still matter and for how long - the "
              "practical answer to whether management should fight the legacy, use it, or wait "
              "it out. What would confirm it: memory timescales predicting recovery "
              "trajectories after new disturbances better than present-conditions-only models, "
              "across forests, grasslands, and wetlands. What would kill it: divergences that "
              "vanish once subtle present differences are accounted for (no real memory, just "
              "unmeasured present), or timescales so variable that no map transfers. What it "
              "does NOT claim: that this is proven, that all history matters, or exact "
              "timescales for every archive. Where the honest answer is unknown - the past of "
              "most landscapes - we say so: the audit reconstructs what evidence allows and "
              "marks the rest."),
  "key_points": [
   "Ecological memory: past conditions shape present dynamics through surviving organisms, soils, and altered regimes.",
   "Memory can aid recovery or lock in degraded states.",
   "Climate change makes memory urgent: systems may respond to vanished pasts.",
   "Measuring memory needs the past (often unrecorded) and decades of tracking.",
   "How much behavior is memory versus present conditions is unquantified."],
  "requirements": [
   "Memory timescales must beat present-conditions-only models at predicting recovery trajectories.",
   "Confirm: replication across forests, grasslands, and wetlands.",
   "Refute: divergences vanishing once subtle present differences are accounted for.",
   "Refute: timescales so variable that no map transfers between landscapes."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all history matters or exact timescales for every archive.",
   "Unreconstructable pasts are marked, not invented."],
  "citations": [CIT_LEGACY],
 },
])

print("entries chunk 3 done:", len(ENTRIES))

CIT_PREDICT = ("Clark JS et al. Ecological forecasting and the science of contingency. 2001; "
               "Biggs R et al. Turning back from the brink: detecting an impending regime shift in "
               "time to avert it. Proc Natl Acad Sci USA. 2009;106:826-831.")
CIT_RAINFOREST = ("Gentry AH. Tree species richness of upper Amazonian forests. Proc Natl Acad Sci "
                  "USA. 1988;85:156-159; Ricklefs RE. A comprehensive framework for global patterns "
                  "in biodiversity. Ecol Lett. 2004;7:1-15.")
CIT_UNCULT = ("Rappe MS, Giovannoni SJ. The uncultured microbial majority. Annu Rev Microbiol. "
              "2003;57:369-394; Locey KJ, Lennon JT. Scaling laws predict global microbial diversity. "
              "Proc Natl Acad Sci USA. 2016;113:5970-5975.")
CIT_METAB = ("Brown JH et al. Toward a metabolic theory of ecology. Ecology. 2004;85:1771-1789; "
             "West GB, Brown JH, Enquist BJ. A general model for the origin of allometric scaling "
             "laws in biology. Science. 1997;276:122-126.")
CIT_NOVEL = ("Hobbs RJ et al. Novel ecosystems: theoretical and management aspects of the new "
             "ecological world order. Glob Ecol Biogeogr. 2006;15:1-7; Williams JW, Jackson ST. "
             "Novel climates, no-analog communities, and ecological surprises. Front Ecol Environ. "
             "2007;5:475-482.")
CIT_MAY = ("May RM. Will a large complex system be stable? Nature. 1972;238:413-414; "
           "Allesina S, Tang S. Stability criteria for complex ecosystems. Nature. 2012;483:205-208.")
CIT_RARE = ("Lyons KG et al. Rare species and ecosystem functioning. Conserv Biol. 2005;19:1019-1024; "
            "Mouillot D et al. Rare species support vulnerable functions in high-diversity ecosystems. "
            "PLoS Biol. 2013;11:e1001569.")
CIT_SUBSIDY = ("Polis GA et al. Toward an integration of landscape and food web ecology: the dynamics "
               "of spatially subsidized food webs. Annu Rev Ecol Syst. 1997;28:289-316; Helfield JM, "
               "Naiman RJ. Effects of salmon-derived nitrogen on riparian forest growth and "
               "implications for stream productivity. Ecology. 2001;82:2403-2409.")
CIT_SERVICES = ("Costanza R et al. The value of the world's ecosystem services and natural capital. "
                "Nature. 1997;387:253-260; Daily GC. Nature's Services: Societal Dependence on Natural "
                "Ecosystems. Island Press; 1997.")
CIT_UNIFIED = ("Loreau M. From Populations to Ecosystems: Theoretical Foundations for a New Ecological "
               "Synthesis. Princeton Univ Press; 2010; Harte J. Maximum Entropy and Ecology: A Theory "
               "of Abundance, Distribution, and Energetics. Oxford Univ Press; 2011.")

ENTRIES.extend([
 {
  "key": "predict-collapse",
  "name": "Can We Predict Ecosystem Collapse Quantitatively?",
  "group": "Stability and Collapse",
  "ladder_rank": 25, "ladder_tier": "advanced",
  "description": ("Weather forecasters predict storms days ahead; ecologists cannot predict a "
                  "fishery collapse a season ahead with anything like that skill. Quantitative "
                  "ecological forecasting - predicting ecosystem states the way meteorology "
                  "predicts weather - is in its infancy. The models exist, the data are "
                  "growing, but the forecasts are rarely tested and often wrong."),
  "problem": "Can ecosystem collapse be forecast quantitatively with usable skill and lead time, and what limits forecast accuracy?",
  "background": ("Ecological forecasting as a discipline dates to the early 2000s, when Clark "
                 "and colleagues argued ecology should predict like meteorology: with explicit "
                 "uncertainty, iterative updating, and scored forecasts. The pieces have "
                 "arrived piecemeal: state-space models that handle observation error, data "
                 "assimilation borrowing from weather forecasting, near-term iterative "
                 "forecasts of algal blooms, mosquito outbreaks, and forest phenology. But "
                 "collapse prediction lags: collapses are rare events, so models have few "
                 "examples to learn from; ecosystems are non-stationary, so the past is a "
                 "weak guide; and forecasts are rarely published with honest skill scores, "
                 "so the field cannot tell progress from hype. The few scored efforts show "
                 "modest skill at short leads that decays fast. Meanwhile managers need "
                 "exactly what is hardest: reliable warnings of rare, high-impact "
                 "transitions, with enough lead time to act."),
  "why_it_matters": ("Every fishery quota, water allocation, and conservation intervention is "
                      "an implicit forecast. Explicit, scored, honest ecological forecasts "
                      "would transform management from reactive crisis response to planned "
                      "navigation - if the skill is real and the limits are stated."),
  "sig_lens": ("The Signature lens treats forecasting as navigation in fog: the question is "
               "not whether the fog lifts, but how far ahead the headlights honestly reach."),
  "sol_public": ("The Signature system proposes a headlight protocol: every ecological "
                 "forecast published with its measured skill at each lead time, and collapse "
                 "warnings issued only where headlights have proven reach. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) forecast skill is measurable and lead-time-dependent; "
              "(2) honest skill scores, including failures, are the only path to trust; (3) "
              "collapse forecasts need different validation than routine forecasts. Reasoning "
              "path: build a forecast scoreboard for managed ecosystems - fisheries, lakes, "
              "rangelands - where every quantitative forecast is logged with its prediction, "
              "its uncertainty, and the outcome. Score skill by lead time: how far ahead do "
              "forecasts beat naive baselines (persistence, climatology)? For collapses "
              "specifically, validate on historical collapses the model never saw, scored as "
              "probabilistic warnings. Publish the skill curves openly - including where skill "
              "is zero. Proposed mechanism: an iterative forecasting practice with mandatory "
              "scoring, where management acts only on forecasts with demonstrated skill at "
              "the needed lead time, and research targets the lead times where skill dies. "
              "What would confirm it: scoreboards showing stable, positive skill for "
              "collapse-relevant variables (recruitment failure, algal bloom onset) at "
              "management-relevant leads, improving as data assimilation matures. What would "
              "kill it: skill curves flat at zero beyond days-to-weeks across all systems "
              "despite good data, implying intrinsic unpredictability at management scales. "
              "What it does NOT claim: that this is proven, that long-lead collapse "
              "forecasts are possible, or that scoring is cheap. Where the honest answer is "
              "unknown - the true predictability limit of most ecosystems - we say so: the "
              "scoreboard discovers the limit, it does not assume one."),
  "key_points": [
   "Ecological forecasting aims for weather-like prediction with scored uncertainty.",
   "Collapses are rare, ecosystems non-stationary, and forecasts rarely published with skill scores.",
   "Early scored efforts show modest short-lead skill decaying fast.",
   "Managers need reliable warnings of rare high-impact transitions with lead time to act.",
   "Honest skill curves, including zero-skill regions, are the missing foundation."],
  "requirements": [
   "Scoreboards must show stable positive skill for collapse-relevant variables at management leads.",
   "Confirm: skill improving as data assimilation and monitoring mature.",
   "Refute: skill flat at zero beyond days-to-weeks across all systems despite good data.",
   "Refute: scored forecasts consistently beaten by naive baselines."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim long-lead collapse forecasts are possible or that scoring is cheap.",
   "Predictability limits are discovered empirically, never assumed."],
  "citations": [CIT_PREDICT],
 },
 {
  "key": "rainforest",
  "name": "Why Are Rainforests Hyperdiverse?",
  "group": "Diversity and Richness",
  "ladder_rank": 26, "ladder_tier": "advanced",
  "description": ("A single hectare of Amazonian forest can hold more tree species than all of "
                  "Europe. Tropical rainforests are the most diverse terrestrial ecosystems on "
                  "Earth by an enormous margin, and after a century of hypotheses - more time, "
                  "more energy, more niches, faster evolution, fiercer enemies - no consensus "
                  "explains the full excess."),
  "problem": "What combination of historical, evolutionary, and ecological mechanisms produces the extreme hyperdiversity of tropical rainforests?",
  "background": ("Alwyn Gentry's plot work in the 1980s quantified the staggering fact: 300+ "
                 "tree species per hectare in upper Amazonia versus a handful in temperate "
                 "forests. Explanations proliferated. The time hypothesis: rainforests are "
                 "ancient and climatically stable, accumulating species for tens of millions of "
                 "years. The energy hypothesis: high productivity supports more individuals, "
                 "lowering extinction and raising speciation. The diversification-rate "
                 "hypothesis: the tropics are both a cradle (faster speciation) and a museum "
                 "(lower extinction). The biotic-interactions hypothesis: intense predation, "
                 "parasitism, and competition subdivide niches ever more finely. The "
                 "Janzen-Connell mechanism offers a concrete engine. Phylogenetic studies now "
                 "test cradle-versus-museum directly, with mixed results across groups. The "
                 "emerging view is that hyperdiversity is overdetermined - many mechanisms push "
                 "the same direction - which paradoxically makes the question harder: when "
                 "everything contributes, partitioning credit becomes the problem, and the "
                 "field lacks a agreed accounting method."),
  "why_it_matters": ("Rainforests hold most terrestrial biodiversity and face the fastest "
                      "destruction. Knowing which mechanisms built the hyperdiversity tells us "
                      "which are reversible: if diversity needs tens of millions of stable "
                      "years, it is effectively irreplaceable; if it needs only energy and "
                      "area, restoration has better odds."),
  "sig_lens": ("The Signature lens treats hyperdiversity as a fortune built by many income "
               "streams: the accounting problem is deciding which streams mattered most."),
  "sol_public": ("The Signature system proposes a fortune audit: phylogenetic, fossil, and "
                 "ecological evidence combined to partition hyperdiversity among its candidate "
                 "income streams, forest by forest. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) hyperdiversity is overdetermined - multiple mechanisms "
              "contribute; (2) their contributions are separable with combined evidence; (3) "
              "different rainforests (Amazon, Congo, SE Asia) have different audit results. "
              "Reasoning path: for each major rainforest region, assemble three evidence "
              "streams - phylogenies giving speciation and extinction rates through time "
              "(cradle vs museum), fossils and paleoclimate giving the stability history, and "
              "ecological measurements giving the strength of niche subdivision and "
              "Janzen-Connell effects today. Combine them in a single accounting model that "
              "attributes the diversity excess to time, energy, diversification rates, and "
              "biotic interactions. Compare audits across the three great rainforest blocks: "
              "where audits agree, the mechanism is general; where they differ, history "
              "rules. Proposed mechanism: a comparative hyperdiversity audit that outputs, per "
              "region, the credited share of each mechanism - the first quantitative partition "
              "of the most famous excess in ecology. What would confirm it: audits whose "
              "credited shares predict independent facts - e.g., regions credited to stability "
              "showing the deepest endemic lineages, regions credited to energy showing the "
              "strongest productivity-diversity links. What would kill it: evidence streams "
              "that refuse to combine (phylogenies contradicting fossils irreconcilably), or "
              "audits attributing everything to everything (no partition possible). What it "
              "does NOT claim: that this is proven, exact percentages, or that the audit is "
              "cheap. Where the honest answer is unknown - deep-time speciation rates for most "
              "groups - we say so: the audit reports its uncertainty per stream."),
  "key_points": [
   "One Amazonian hectare can hold more tree species than all of Europe.",
   "Candidate mechanisms: time-stability, energy, cradle-and-museum diversification, biotic interactions.",
   "Phylogenetic tests of cradle vs museum give mixed results across groups.",
   "Hyperdiversity looks overdetermined - many mechanisms pushing the same way.",
   "Which mechanisms built it decides whether the diversity is irreplaceable."],
  "requirements": [
   "Audits must predict independent facts (endemic depth, productivity links) from credited shares.",
   "Confirm: agreement patterns across Amazon, Congo, and SE Asia audits.",
   "Refute: evidence streams that irreconcilably contradict each other.",
   "Refute: audits attributing everything to everything with no partition."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim exact percentages or a cheap audit.",
   "Deep-time rates carry explicit uncertainty per evidence stream."],
  "citations": [CIT_RAINFOREST],
 },
 {
  "key": "uncultured",
  "name": "The Uncultured Majority: What Unknown Microbes Do",
  "group": "Microbes and Hidden Worlds",
  "ladder_rank": 27, "ladder_tier": "advanced",
  "description": ("Over 99 percent of microbial species have never been grown in a lab; entire "
                  "phyla are known only from DNA fragments in seawater and soil. This uncultured "
                  "majority may run biogeochemical processes we have not discovered yet. "
                  "Ecology's largest unknown workforce is also its most invisible."),
  "problem": "What ecological functions do uncultured microbial lineages perform, and how would we know if a major biogeochemical process is microbially mediated by unknown organisms?",
  "background": ("The great plate-count anomaly - microscopes seeing far more cells than ever "
                 "grew on plates - was noted in the 1980s; environmental DNA sequencing in the "
                 "1990s-2000s revealed the scale: most bacterial and archaeal diversity belongs "
                 "to candidate phyla with no cultured representative. Single-cell genomics now "
                 "recovers genomes from individual uncultured cells, revealing metabolisms never "
                 "seen before - archaea that oxidize ammonia in the ocean, bacteria with "
                 "entirely novel carbon pathways. Yet a genome is a parts list, not a job "
                 "description: knowing an organism has the genes for a metabolism does not say "
                 "when, where, or how much it uses them in nature. The deepest worry is the "
                 "unknown unknowns: processes currently attributed to chemistry or physics that "
                 "are actually microbial, and ecosystem models missing entire functional guilds. "
                 "The field is sequencing faster than it is understanding, and the gap between "
                 "genetic inventory and ecological role widens yearly."),
  "why_it_matters": ("If major nutrient or carbon fluxes are mediated by unknown microbes, then "
                      "climate models, fertilizer strategies, and bioremediation are all missing "
                      "pieces. The uncultured majority could also hold the next antibiotics, "
                      "enzymes, and biotechnologies - if we learn what they do."),
  "sig_lens": ("The Signature lens treats uncultured microbes as an uncontacted workforce: the "
               "census counts shadows on the wall, and the task is to learn their trades without "
               "ever meeting most of them."),
  "sol_public": ("The Signature system proposes a shadow-trade method: link uncultured genomes "
                 "to in-situ activity measurements (who is eating what, right now, in the "
                 "environment) so functions attach to lineages without culturing. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) genomes plus in-situ activity can assign functions "
              "without culturing; (2) isotope labeling and single-cell methods can watch "
              "uncultured cells work in place; (3) unknown processes leave chemical "
              "fingerprints. Reasoning path: in target environments (ocean, soil, gut), "
              "combine single-cell genomics (who is there) with stable-isotope probing and "
              "nanoscale imaging (who is eating what, right now). A lineage that lights up "
              "while consuming labeled methane is a methanotroph - job description assigned "
              "without a culture. In parallel, hunt chemical fingerprints of unexplained "
              "processes - fluxes no known organism accounts for - and match them to the "
              "metabolic potential of uncultured genomes from the same site. Proposed "
              "mechanism: a function-to-lineage atlas for the uncultured majority, built "
              "from activity, not cultures, flagging any major flux whose mediators remain "
              "unknown. What would confirm it: atlas assignments predicting the outcome of "
              "targeted suppressions and nutrient additions, and at least one major "
              "previously-unexplained flux traced to a candidate phylum. What would kill it: "
              "activity methods too coarse to resolve lineage-level function, or genomes so "
              "versatile that in-situ activity never maps cleanly to genes. What it does NOT "
              "claim: that this is proven, that culturing is obsolete, or complete coverage. "
              "Where the honest answer is unknown - the function of most candidate phyla - we "
              "say so: the atlas starts with assigned trades and marks the rest as shadows."),
  "key_points": [
   "Over 99 percent of microbial species have never been cultured; whole phyla are DNA-only.",
   "Single-cell genomics reveals novel metabolisms, but genomes are parts lists, not job descriptions.",
   "Unknown microbes may mediate processes currently attributed to chemistry or physics.",
   "Sequencing outruns understanding; the inventory-role gap widens yearly.",
   "Missing guilds could bias climate models and hide biotechnologies."],
  "requirements": [
   "Atlas assignments must predict suppression and nutrient-addition outcomes.",
   "Confirm: at least one unexplained major flux traced to a candidate phylum.",
   "Refute: activity methods too coarse for lineage-level function mapping.",
   "Refute: genomes so versatile that activity never maps cleanly to genes."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim culturing is obsolete or complete coverage.",
   "Unassigned lineages remain marked as shadows, not filled in."],
  "citations": [CIT_UNCULT],
 },
 {
  "key": "metabolic",
  "name": "Can One Law Scale From Cells to Ecosystems?",
  "group": "Global Change and Flux",
  "ladder_rank": 28, "ladder_tier": "advanced",
  "description": ("A mouse burns energy faster per gram than an elephant, following a precise "
                  "three-quarter power law. The metabolic theory of ecology claims this single "
                  "scaling law, rooted in the physics of distribution networks, predicts "
                  "everything from population growth to ecosystem carbon flux. It is the "
                  "boldest unification attempt in ecology - and one of the most contested."),
  "problem": "Does metabolic scaling provide a real quantitative foundation linking individual metabolism to population, community, and ecosystem processes?",
  "background": ("Kleiber's 1930s finding that metabolic rate scales as mass to the 3/4 power "
                 "became, in West, Brown, and Enquist's 1997 model, a consequence of fractal "
                 "branching networks - blood vessels, xylem - minimizing transport costs. Brown "
                 "and colleagues' 2004 metabolic theory of ecology extended it ambitiously: "
                 "temperature-corrected metabolic rate should predict population growth rates, "
                 "species richness gradients, trophic structure, and whole-ecosystem fluxes. "
                 "Early tests were encouraging, but the backlash was fierce: the 3/4 exponent "
                 "varies in reality, the network model's assumptions are disputed, temperature "
                 "corrections oversimplify, and many predictions fail or need so many "
                 "adjustments that critics call the theory unfalsifiable. Defenders counter "
                 "that no other framework even attempts the individual-to-ecosystem bridge, and "
                 "that the failures are refinements, not refutations. The question stands: is "
                 "metabolic scaling ecology's Newtonian mechanics or its beautiful mirage?"),
  "why_it_matters": ("A working scaling theory would let ecologists predict ecosystem fluxes "
                      "from body sizes and temperatures - exactly what climate models need as "
                      "warming reshuffles both. If the theory is a mirage, models need a "
                      "different foundation, and the sooner the better."),
  "sig_lens": ("The Signature lens treats metabolic scaling as a proposed master key: the "
               "test is not whether it is beautiful, but which doors it actually opens."),
  "sol_public": ("The Signature system proposes a key-testing protocol: pre-register the "
                 "theory's quantitative predictions across scales, test them against fresh "
                 "data, and keep only the doors the key opens. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the theory makes quantitative, pre-registered "
              "predictions or it is not a theory; (2) predictions must be tested on data not "
              "used to build the theory; (3) partial success is informative - the kept doors "
              "matter. Reasoning path: enumerate the theory's distinct quantitative claims - "
              "the 3/4 exponent, temperature dependence of rates, population density scaling, "
              "ecosystem flux predictions. For each, pre-register the prediction and the "
              "acceptable error before looking at a fresh dataset (new compilations, not the "
              "classic ones). Score each door: opens cleanly, opens with adjustment, or stays "
              "shut. The result is a scored map of where metabolic scaling works - perhaps "
              "individual physiology but not community structure, or vice versa. Proposed "
              "mechanism: an adversarial collaboration protocol where proponents and critics "
              "jointly pre-register tests, ending the cycle of post-hoc adjustment. What would "
              "confirm it: a scored map showing the theory's core predictions holding on fresh "
              "data across at least two scales (individual and ecosystem), with failures "
              "bounded and explained. What would kill it: core predictions failing on fresh "
              "data even with reasonable adjustments, or the exponent varying so freely that "
              "the theory predicts nothing specific. What it does NOT claim: that this is "
              "proven, that scaling is exact, or that critics are wrong about past "
              "overreach. Where the honest answer is unknown - which doors will open - we say "
              "so: the protocol discovers the map, it does not draw it in advance."),
  "key_points": [
   "Metabolic rate scales as mass^3/4; West-Brown-Enquist (1997) derived it from network physics.",
   "The metabolic theory of ecology (2004) extends scaling to populations, communities, ecosystems.",
   "Critics: the exponent varies, assumptions are disputed, predictions need too many adjustments.",
   "Defenders: no rival framework attempts the individual-to-ecosystem bridge.",
   "Whether it is foundation or mirage decides what climate models should be built on."],
  "requirements": [
   "Pre-registered predictions must hold on fresh data across at least two scales.",
   "Confirm: a scored map with failures bounded and explained, not rationalized.",
   "Refute: core predictions failing on fresh data despite reasonable adjustments.",
   "Refute: exponent variation so free that the theory predicts nothing specific."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim scaling is exact or that past criticisms were wrong.",
   "The scored map is discovered empirically, never drawn in advance."],
  "citations": [CIT_METAB],
 },
 {
  "key": "novel-eco",
  "name": "What Happens in Ecosystems With No Past Analog?",
  "group": "Global Change and Flux",
  "ladder_rank": 29, "ladder_tier": "advanced",
  "description": ("Climate change is creating combinations of temperature and rainfall with no "
                  "past equivalent, assembling species that never coexisted into novel "
                  "ecosystems. Ecology has always learned from the past - but what do you do "
                  "when the past has no example? Managing no-analog futures may be the "
                  "hardest problem conservation has ever faced."),
  "problem": "How do we predict, manage, and set goals for novel ecosystems and no-analog climates when history offers no guide?",
  "background": ("Paleoecologists showed that past climates produced no-analog communities - "
                 "species combinations with no modern equivalent - during deglaciation. Now "
                 "the process runs in reverse: novel climates are projected to cover large "
                 "fractions of Earth this century, and human transport mixes species into "
                 "combinations evolution never tested. The novel-ecosystems concept (Hobbs "
                 "et al. 2006) argued these systems are not just degraded versions of "
                 "historical ones but new entities needing new goals. This split the field: "
                 "traditionalists hold historical fidelity as the standard and see novel "
                 "systems as failures; pragmatists argue historical targets are unreachable "
                 "and management should maximize function and services instead. Both sides "
                 "face the prediction problem: species distribution models trained on past "
                 "climates extrapolate into no-analog space where their assumptions break, "
                 "and community assembly rules for never-before-combined species are "
                 "essentially untested. We are managing the future with tools built for the "
                 "past."),
  "why_it_matters": ("Within decades, large regions will hold climates and species combinations "
                      "with no historical precedent. Every protected area, restoration target, "
                      "and forestry plan in those regions needs goals and methods for a world "
                      "without analogs - or they will chase ghosts."),
  "sig_lens": ("The Signature lens treats novel ecosystems as uncharted water: the old charts "
               "do not apply, so navigation must switch from maps to instruments."),
  "sol_public": ("The Signature system proposes instrument navigation: replace historical "
                 "reference targets with functional goals, and steer by real-time monitoring "
                 "of function rather than fidelity to a vanished past. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) historical fidelity becomes unreachable in no-analog "
              "conditions; (2) ecosystem functions (productivity, water regulation, habitat "
              "provision) remain definable and measurable without historical reference; (3) "
              "real-time monitoring can steer management adaptively. Reasoning path: for a "
              "managed landscape entering no-analog conditions, retire the historical "
              "reference community as the target and replace it with a functional charter: "
              "the measurable functions the system must provide. Monitor those functions "
              "directly - not species lists - and manage adaptively toward them: if a novel "
              "species combination delivers the functions, it succeeds by charter even with "
              "zero historical fidelity. Keep a parallel watch for harms the charter might "
              "miss (novel invasions, disease). Proposed mechanism: a functional-charter "
              "protocol for no-analog management, with instrument panels tracking function "
              "delivery and triggers for intervention when functions slip. What would confirm "
              "it: charter-managed landscapes maintaining function delivery through "
              "no-analog transitions better than fidelity-managed controls, without "
              "accumulating hidden harms. What would kill it: functions proving as "
              "history-dependent as species composition (no charter without a reference), or "
              "novel combinations repeatedly producing catastrophic surprises the instruments "
              "miss. What it does NOT claim: that this is proven, that history is "
              "irrelevant everywhere, or that any novel combination is acceptable. Where the "
              "honest answer is unknown - how novel combinations will actually behave - we "
              "say so: the instruments discover it in real time, they do not predict it."),
  "key_points": [
   "Novel climates and human-mixed species create ecosystems with no past equivalent.",
   "Paleo records show no-analog communities are natural; the current wave is human-driven.",
   "The field splits: historical fidelity versus functional pragmatism as the goal.",
   "Species models trained on the past break down in no-analog conditions.",
   "Management tools were built for the past; the future needs new navigation."],
  "requirements": [
   "Charter-managed landscapes must maintain function through no-analog transitions.",
   "Confirm: outperforming fidelity-managed controls without accumulating hidden harms.",
   "Refute: functions proving as history-dependent as species composition.",
   "Refute: novel combinations repeatedly surprising the instruments catastrophically."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim history is irrelevant everywhere or that any novel mix is acceptable.",
   "Future behavior is discovered by monitoring, never assumed."],
  "citations": [CIT_NOVEL],
 },
 {
  "key": "may-paradox",
  "name": "May's Paradox: Why Complexity Does Not Always Destabilize",
  "group": "Stability and Collapse",
  "ladder_rank": 30, "ladder_tier": "advanced",
  "description": ("Robert May proved mathematically that complex ecosystems should be unstable; "
                  "nature exhibits complex ecosystems that are stable. This contradiction - "
                  "May's paradox - has driven fifty years of theoretical ecology. Resolutions "
                  "abound, but no single answer commands consensus, and the paradox still "
                  "structures how theorists think about stability."),
  "problem": "What exactly resolves May's paradox - which features of real ecosystems, absent from random-matrix models, account for the stability of complex natural systems?",
  "background": ("May's 1972 Nature paper used random community matrices to show stability "
                 "requires the square root of species-times-connectance to stay below a "
                 "threshold - a condition real food webs wildly violate. The paradox launched "
                 "a hunt for the missing stabilizers: Allesina and Tang (2012) showed "
                 "predator-prey (antisymmetric) interaction structure is inherently more "
                 "stable than random or competitive structure; weak interactions dampen "
                 "oscillations; modularity contains disturbances; adaptive foraging lets "
                 "consumers switch away from collapsing prey; spatial structure and "
                 "dispersal rescue local extinctions. Each resolution is mathematically "
                 "sound and empirically plausible somewhere. The trouble is abundance: with "
                 "so many candidate stabilizers, the field cannot say which ones actually "
                 "carry the load in nature, in what proportions, or whether the paradox even "
                 "needs resolving - some argue real systems are not at equilibrium, so "
                 "equilibrium stability is the wrong question. The paradox persists as "
                 "ecology's defining theoretical tension."),
  "why_it_matters": ("Stability theory underlies risk assessment for extinctions, invasions, "
                      "and harvesting. If we do not know what stabilizes real systems, we "
                      "cannot know what destabilizes them - and management flies blind on the "
                      "most fundamental question."),
  "sig_lens": ("The Signature lens treats May's paradox as a stress test with the wrong "
               "dummies: random matrices were crash-test dummies, and real ecosystems are "
               "built nothing like dummies."),
  "sol_public": ("The Signature system proposes a stabilizer census: measure each candidate "
                 "stabilizer's strength in real webs and test which ones, in what combination, "
                 "actually bridge the gap between May's prediction and observed persistence. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the paradox is quantitative - the gap between "
              "predicted and observed stability can be measured; (2) candidate stabilizers "
              "are measurable in real webs; (3) their contributions combine approximately "
              "additively. Reasoning path: take well-mapped real food webs and compute May's "
              "stability criterion on the raw matrix - the predicted instability gap. Then "
              "add the candidate stabilizers one by one in the order of their measured "
              "strength in that web: antisymmetric interaction structure, weak-link "
              "distributions, modularity, adaptive foraging, spatial rescue. After each "
              "addition, recompute stability. The stabilizer (or combination) that closes "
              "the gap is the resolution for that web. Repeat across web types. Proposed "
              "mechanism: a gap-closing audit that outputs, per ecosystem type, the ranked "
              "stabilizers that reconcile theory with reality - turning fifty years of "
              "candidate resolutions into a measured account. What would confirm it: audits "
              "across marine, freshwater, and terrestrial webs where a small set of "
              "measured stabilizers consistently closes the gap, and removal of those "
              "stabilizers in models reopens it. What would kill it: gaps that no "
              "combination of measured stabilizers closes (the paradox is elsewhere - perhaps "
              "non-equilibrium), or stabilizer rankings that never replicate. What it does "
              "NOT claim: that this is proven, that equilibrium stability is the right "
              "question, or one universal resolver. Where the honest answer is unknown - "
              "whether real systems sit at equilibrium at all - we say so: the audit tests "
              "the equilibrium framing and reports if it fails."),
  "key_points": [
   "May 1972: random complex matrices are unstable; real webs violate the criterion yet persist.",
   "Candidate resolvers: antisymmetric structure, weak links, modularity, adaptive foraging, space.",
   "Each is sound somewhere; which carry the load in nature is unmeasured.",
   "Some argue equilibrium stability is the wrong question entirely.",
   "The paradox still structures theoretical ecology fifty years on."],
  "requirements": [
   "Gap-closing audits must reconcile theory with reality across web types.",
   "Confirm: small sets of measured stabilizers consistently closing the gap.",
   "Refute: gaps no combination of stabilizers closes (non-equilibrium answer).",
   "Refute: stabilizer rankings that never replicate across webs."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim equilibrium stability is the right question or one universal resolver.",
   "If the equilibrium framing fails the test, the audit reports it."],
  "citations": [CIT_MAY],
 },
 {
  "key": "rare-species",
  "name": "Do Rare Species Matter, or Are They Redundant?",
  "group": "Diversity and Richness",
  "ladder_rank": 31, "ladder_tier": "advanced",
  "description": ("Most species in most communities are rare - yet conservation and ecosystem "
                  "science focus overwhelmingly on the common ones. Rare species could be "
                  "redundant passengers, unique contributors, or insurance policies that pay "
                  "out under future conditions. Which they are, in general, is unresolved - "
                  "and most rare species are also the most extinction-prone."),
  "problem": "What is the functional role of rare species in ecosystems - redundant, uniquely contributing, or insurance - and how should that shape conservation priorities?",
  "background": ("Rarity is the norm: in tropical forests, coral reefs, and microbial "
                 "communities alike, a few species dominate and most are scarce. The "
                 "redundancy view says rare species contribute little to current function - "
                 "experiments removing rare plants often show minimal short-term effects. "
                 "The uniqueness view points to cases where a rare species carries an "
                 "irreplaceable function: the rare pollinator of a keystone plant, the "
                 "scarce predator controlling an outbreak species. The insurance view, "
                 "formalized by Yachi and Loreau, says rare species are a portfolio of "
                 "options: useless now, vital when conditions change - the species that "
                 "tolerates the drought that kills the dominant. Empirical tests are hard: "
                 "rare species are hard to manipulate, their effects may take decades to "
                 "appear, and insurance only pays during rare events. The field knows rare "
                 "species can matter enormously in specific cases; it does not know the "
                 "general ledger."),
  "why_it_matters": ("Rare species are the first to go extinct and the last to be studied. If "
                      "they are mostly redundant, triage can focus on common functional "
                      "species; if they are insurance, then every rare-species extinction is "
                      "a burned policy - and we are burning them by the thousands."),
  "sig_lens": ("The Signature lens treats rare species as insurance policies in a vault: most "
               "never pay out, but the vault's value is measured on the day disaster strikes."),
  "sol_public": ("The Signature system proposes a policy audit: score rare species by "
                 "functional uniqueness today and by option value under future conditions - "
                 "and the vault's worth is the sum of both. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) rare species have two kinds of value - current "
              "functional uniqueness and future option value; (2) both are estimable from "
              "traits and environmental tolerances; (3) insurance value is real even when "
              "unpaid. Reasoning path: for a community's rare species, measure functional "
              "traits and compare to common species - the uniqueness score is the distance "
              "to the nearest functional neighbor. Then measure tolerance breadth (drought, "
              "heat, salinity, disease) - the option score is the fraction of future "
              "conditions where the rare species persists while its common functional "
              "neighbors fail. Combine into a policy value per rare species. Validate "
              "retrospectively: in systems with long records, check whether high-option "
              "rare species actually became important after past disturbances. Proposed "
              "mechanism: a rare-species policy audit that ranks conservation priority by "
              "uniqueness plus option value - the first principled triage between redundant "
              "passengers and irreplaceable insurance. What would confirm it: retrospective "
              "tests showing high-option rare species stepping up after real disturbances "
              "(droughts, disease outbreaks), and the audit predicting which ones. What "
              "would kill it: rare species never stepping up - dominants or immigrants "
              "always covering the function instead - or option scores with no predictive "
              "power. What it does NOT claim: that this is proven, that every rare species "
              "is precious, or exact future conditions. Where the honest answer is unknown "
              "- tolerance breadths for most rare species - we say so: the audit measures "
              "what it can and marks the rest."),
  "key_points": [
   "Rarity is the norm; most species in most communities are scarce.",
   "Three views: redundant passengers, unique contributors, insurance policies.",
   "Removing rare plants often shows little short-term effect - but insurance pays over decades.",
   "Rare species are the most extinction-prone and least studied.",
   "The general ledger of rare-species value is unwritten."],
  "requirements": [
   "Retrospective tests must show high-option rare species stepping up after real disturbances.",
   "Confirm: the audit predicting which rare species become important.",
   "Refute: rare species never stepping up (dominants or immigrants always cover).",
   "Refute: option scores with no predictive power."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim every rare species is precious or exact future conditions.",
   "Unmeasured tolerances are marked, not assumed."],
  "citations": [CIT_RARE],
 },
 {
  "key": "subsidies",
  "name": "How Ecosystems Feed Each Other Across Boundaries",
  "group": "Global Change and Flux",
  "ladder_rank": 32, "ladder_tier": "advanced",
  "description": ("Salmon carry ocean nitrogen into forests; seabird guano fertilizes islands; "
                  "leaf litter feeds streams. Ecosystems are not closed - they subsidize each "
                  "other with flows of energy, nutrients, and organisms across boundaries. "
                  "These cross-ecosystem subsidies can dominate local dynamics, yet they are "
                  "routinely ignored in models, management, and conservation plans."),
  "problem": "How large are cross-ecosystem subsidies, when do they control recipient ecosystem dynamics, and how do we account for them in science and management?",
  "background": ("Gary Polis and colleagues' work in the 1990s-2000s showed subsidies are "
                 "pervasive: marine inputs fuel desert island food webs, emergent insects feed "
                 "riparian predators, salmon nitrogen measurably boosts riparian tree growth. "
                 "The conceptual advance was seeing landscapes as connected by flows, not as "
                 "collections of closed systems. But quantification lags far behind "
                 "recognition: subsidy magnitude is measured in a few famous systems and "
                 "guessed elsewhere; the conditions under which subsidies dominate versus "
                 "merely supplement are unclear; and subsidies couple systems in ways that "
                 "defeat single-ecosystem management - protect the forest but dam the salmon "
                 "run and the forest starves. Climate change and land use are rewiring "
                 "subsidy flows (shifting migrations, drying streams) with almost no "
                 "monitoring of the rewiring. The field agrees subsidies matter enormously "
                 "in principle; it lacks the general accounting."),
  "why_it_matters": ("Conservation draws boundaries around ecosystems, but subsidies cross "
                      "them: a reserve that protects forest while the salmon run collapses "
                      "protects a starving forest. Fisheries, forestry, and water management "
                      "all need subsidy accounting to avoid managing half a system."),
  "sig_lens": ("The Signature lens treats ecosystems as trading partners with unrecorded "
               "commerce: the economy is real, but nobody keeps the books."),
  "sol_public": ("The Signature system proposes trade bookkeeping: isotope and flow "
                 "measurements that ledger every major cross-boundary subsidy, flagging the "
                 "flows recipient systems depend on. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) major subsidies are measurable with isotopes, "
              "gauges, and movement tracking; (2) recipient dependence can be tested by "
              "subsidy manipulation or natural shutoffs; (3) a subsidy ledger per landscape "
              "is feasible for the largest flows. Reasoning path: for a landscape, list the "
              "candidate cross-boundary flows - animal migrations, water transport, wind "
              "deposition, human vectors. Quantify each with stable isotopes (marine versus "
              "terrestrial nitrogen signatures), flow gauges, and tracking. Then test "
              "dependence: compare recipient productivity where the subsidy arrives versus "
              "where it is blocked (dams, barriers, islands with and without seabirds). The "
              "dependence ratio - productivity with versus without - ranks each subsidy. "
              "Proposed mechanism: a landscape subsidy ledger recording each major flow, its "
              "magnitude, and the recipient's dependence ratio - the books of the "
              "cross-ecosystem economy, consulted before any management that touches a "
              "boundary. What would confirm it: ledgers predicting recipient responses to "
              "subsidy changes (dam removals, migration collapses, seabird eradications) "
              "better than closed-system models. What would kill it: subsidies proving "
              "universally supplementary - never load-bearing - or flows so variable that "
              "no ledger value transfers between years. What it does NOT claim: that this "
              "is proven, complete accounting of every flow, or that ledgers are cheap. "
              "Where the honest answer is unknown - most subsidy magnitudes worldwide - we "
              "say so: the ledger starts with measured flows and marks the rest."),
  "key_points": [
   "Ecosystems subsidize each other: salmon nitrogen, guano, leaf litter, insect emergence.",
   "Subsidies can dominate recipient dynamics yet are ignored in most models and plans.",
   "Protecting one side of a subsidy (forest) while breaking the other (salmon run) starves the system.",
   "Climate and land use are rewiring subsidy flows with almost no monitoring.",
   "Quantification exists for famous cases; general accounting does not."],
  "requirements": [
   "Ledgers must beat closed-system models at predicting responses to subsidy changes.",
   "Confirm: dependence ratios measured across multiple landscape types.",
   "Refute: subsidies universally supplementary, never load-bearing.",
   "Refute: flows so variable that no ledger value transfers between years."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim complete accounting or cheap ledgers.",
   "Unmeasured flows are marked, not invented."],
  "citations": [CIT_SUBSIDY],
 },
 {
  "key": "services-value",
  "name": "Can We Truly Measure What Ecosystems Are Worth?",
  "group": "Restoration and Stewardship",
  "ladder_rank": 33, "ladder_tier": "advanced",
  "description": ("In 1997, Costanza and colleagues valued the world's ecosystem services at "
                  "$33 trillion per year - larger than global GDP. The number made headlines "
                  "and launched an industry of natural-capital accounting. But what does it "
                  "mean to price pollination, and can such valuations ever be more than "
                  "advocacy with decimals? The measurement problem at the heart of "
                  "ecosystem-service science is unsolved."),
  "problem": "Can the value of ecosystem services be measured rigorously enough to guide decisions, and what are the fundamental limits of valuation?",
  "background": ("The ecosystem-services framework, popularized by Daily (1997) and the "
                 "Costanza et al. (1997) valuation, translates ecological function into "
                 "economic language to make conservation legible to decision-makers. The "
                 "Millennium Ecosystem Assessment (2005) and IPBES built global policy "
                 "architecture on it; payments for ecosystem services now move billions. "
                 "Methodologically, the field uses avoided costs (what a wetland's flood "
                 "protection replaces), replacement costs, contingent valuation (surveyed "
                 "willingness to pay), and production functions. Each method is contested: "
                 "contingent valuation is sensitive to survey design; marginal values change "
                 "with scarcity (the last wetland is worth more than the first); some "
                 "services - existence value, cultural meaning - resist monetization "
                 "entirely; and aggregating to global totals commits what critics call the "
                 "seriousness fallacy, implying ecosystems could be substituted at the "
                 "stated price. Defenders argue valuation was never about a true price but "
                 "about visibility - making the invisible visible. The open question is "
                 "whether the numbers can be decision-grade or only attention-grade."),
  "why_it_matters": ("Trillions in land-use, infrastructure, and climate decisions cite "
                      "ecosystem-service values. If the numbers are decision-grade, they "
                      "redirect development; if they are advocacy with decimals, policies "
                      "built on them rest on sand - and critics will eventually say so."),
  "sig_lens": ("The Signature lens treats valuation as translation: the question is not "
               "whether the translation is perfect, but which decisions each translated "
               "number can honestly carry."),
  "sol_public": ("The Signature system proposes a load-rating for valuations: every service "
                 "value published with its method, its uncertainty, and an explicit rating "
                 "of which decisions it can carry. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) different valuation methods suit different decisions; "
              "(2) uncertainty and method-dependence can be quantified and disclosed; (3) "
              "some services cannot be monetized and must be carried by other metrics. "
              "Reasoning path: for each ecosystem service in a decision context, produce "
              "not one number but a rated valuation: the estimate, the method, the "
              "uncertainty range, the sensitivity to scarcity (marginal vs average), and an "
              "explicit load rating - which decisions this number can carry (project "
              "screening, payment design, damage litigation) and which it cannot (global "
              "aggregation, irreplaceable-service trade-offs). Services that resist "
              "monetization get non-monetary accounts (biophysical metrics, deliberative "
              "rankings) instead of forced prices. Proposed mechanism: a valuation "
              "load-rating standard, like engineering load ratings for bridges, so "
              "decision-makers see what each number can honestly bear. What would confirm "
              "it: rated valuations predicting real payment and litigation outcomes "
              "better than unrated ones, and decisions surviving scrutiny when built on "
              "high-rated numbers. What would kill it: uncertainty so large in practice "
              "that no valuation earns better than the lowest rating, or decision-makers "
              "ignoring ratings exactly as they ignore caveats now. What it does NOT claim: "
              "that this is proven, that true prices exist, or that rating fixes misuse. "
              "Where the honest answer is unknown - the value of irreplaceable and "
              "cultural services - we say so: those get non-monetary accounts, never "
              "forced prices."),
  "key_points": [
   "Costanza et al. 1997: $33 trillion/year for global ecosystem services - larger than GDP.",
   "Methods: avoided costs, replacement costs, contingent valuation, production functions.",
   "Each method is contested; marginal values shift with scarcity; some services resist pricing.",
   "Global aggregation is criticized as implying substitutability at the stated price.",
   "The open question: decision-grade numbers or attention-grade advocacy."],
  "requirements": [
   "Rated valuations must predict payment and litigation outcomes better than unrated ones.",
   "Confirm: decisions on high-rated numbers surviving independent scrutiny.",
   "Refute: uncertainty so large that no valuation earns above the lowest rating.",
   "Refute: decision-makers ignoring ratings as they ignore caveats now."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim true prices exist or that rating fixes misuse.",
   "Irreplaceable services get non-monetary accounts, never forced prices."],
  "citations": [CIT_SERVICES],
 },
 {
  "key": "unified",
  "name": "What Would a Complete Theory of Ecology Look Like?",
  "group": "The Unified Picture",
  "ladder_rank": 34, "ladder_tier": "advanced",
  "description": ("Physics has its standard model; ecology has a magnificent archipelago of "
                  "theories - island biogeography, metabolic scaling, neutral theory, maximum "
                  "entropy - that rarely speak to each other. Whether ecology can or should "
                  "have a unified theory, and what it would even look like, is the field's "
                  "most ambitious open question."),
  "problem": "Is a unified theory of ecology possible, what would it have to explain, and which of the candidate frameworks comes closest?",
  "background": ("Ecology's unification attempts each conquered part of the territory. "
                 "MacArthur and Wilson unified island patterns; Hubbell unified abundance and "
                 "biogeography under neutrality; Brown's metabolic theory unified energetics "
                 "across scales; Harte's maximum entropy theory derives abundance, "
                 "species-area, and metabolic patterns from information principles with "
                 "striking parsimony. Yet each unification leaves out what another explains: "
                 "neutral theory ignores traits, metabolic theory strains at community "
                 "structure, maximum entropy is silent on dynamics. Some ecologists argue "
                 "unification is a category mistake - ecology studies historically contingent, "
                 "evolving systems where universal laws cannot hold the way they do in "
                 "physics. Others counter that the archipelago itself is the embarrassment: "
                 "a mature science should connect its islands. The debate touches identity: "
                 "is ecology a science of laws, of mechanisms, or of place-based understanding? "
                 "No candidate framework currently commands consensus, and the criteria for "
                 "what would count as success are themselves disputed."),
  "why_it_matters": ("A unified theory would do for ecology what the synthesis did for "
                      "evolutionary biology: organize teaching, focus research, and give "
                      "applied work a common foundation. Even the disciplined pursuit of "
                      "one - mapping exactly where each framework works - would be the most "
                      "useful theoretical project in the field."),
  "sig_lens": ("The Signature lens treats unification as charting an archipelago: the prize "
               "is not one island to rule them, but the first accurate map of all of them."),
  "sol_public": ("The Signature system proposes an archipelago map: score every candidate "
                 "framework on the same battery of patterns, and the unified theory is "
                 "whatever combination covers the most ground with the fewest assumptions. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) unification can be approached empirically - "
              "frameworks earn territory by predicting patterns; (2) a common pattern "
              "battery allows fair comparison; (3) the result may be a federation, not a "
              "single theory. Reasoning path: define the pattern battery - the dozen "
              "best-established macroecological patterns (species-abundance distributions, "
              "species-area curves, latitudinal gradients, body-size distributions, "
              "trophic pyramids, distance decay, metabolic scaling, occupancy patterns). "
              "Score each candidate framework (neutral, metabolic, maximum entropy, niche "
              "assembly, network theory) on each pattern: predicts quantitatively, "
              "predicts qualitatively, or silent. The archipelago map shows which "
              "frameworks own which patterns and where they overlap or conflict. Where "
              "overlaps conflict, design the discriminating test. The unified theory is "
              "then pursued as the minimal combination covering the battery - possibly a "
              "federation with explicit handoff rules between frameworks. Proposed "
              "mechanism: a living scoreboard of theoretical coverage, updated as new "
              "patterns are established and new tests run, giving the field its first "
              "shared picture of how much is explained and by what. What would confirm "
              "it: the scoreboard guiding successful discriminating tests and the "
              "minimal covering combination stabilizing across pattern additions. What "
              "would kill it: patterns proving framework-relative (no fair battery "
              "possible), or coverage so fragmented that no combination beats the "
              "archipelago. What it does NOT claim: that this is proven, that one theory "
              "will win, or that ecology must resemble physics. Where the honest answer "
              "is unknown - whether unification is even possible - we say so: the map "
              "is valuable even if the territory stays an archipelago."),
  "key_points": [
   "Ecology has powerful partial theories - neutral, metabolic, maximum entropy, island biogeography.",
   "Each explains what others ignore; no candidate commands consensus.",
   "Some argue unification is a category mistake for historically contingent systems.",
   "Even the criteria for successful unification are disputed.",
   "Mapping exactly where each framework works would itself be the most useful theory project."],
  "requirements": [
   "The scoreboard must guide successful discriminating tests between frameworks.",
   "Confirm: a minimal covering combination stabilizing as patterns are added.",
   "Refute: patterns proving framework-relative, with no fair battery possible.",
   "Refute: coverage so fragmented that no combination beats the archipelago."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim one theory will win or that ecology must resemble physics.",
   "The map is valuable even if unification proves impossible."],
  "citations": [CIT_UNIFIED],
 },
])

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
ranks = sorted(e["ladder_rank"] for e in ENTRIES)
assert ranks == list(range(1, 35)), "ladder ranks broken: %s" % ranks
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate keys"
print("entries complete:", len(ENTRIES))
