#!/usr/bin/env python3
"""Seed entries for the Ornithology field build (field #6, taxonomy order).

Verified 2026-10-17: the manifest holds 'public-birds' (60 species-catalog
records: identification, habitat, diet — no science) and 'signature-birds'
(30 original Signature bird concepts). Neither covers ornithology as a
science — no avian anatomy/physiology, flight mechanics, migration,
song/communication, breeding systems, foraging ecology, avian taxonomy,
conservation ornithology, or field methods. So this build creates two NEW
databases:

  ornithology              — The Ornithology Database (public-harvest: real,
                             fact-checked ornithology — avian anatomy and
                             physiology, feathers, flight mechanics,
                             migration and navigation, song and
                             communication, breeding systems, foraging
                             ecology, avian taxonomy, conservation
                             ornithology, field methods)
  ornithology-signature    — The Ornithology Signature Database (his original
                             Signature interpretation; src signature, titles
                             suffixed " (Signature Edition)", never presented
                             as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation constants (standard ornithology literature)
CIT_GILL = ("Gill, F. B. (2007). 'Ornithology', 3rd ed. W. H. Freeman.")
CIT_HANDBOOK = ("Lovette, I. J. & Fitzpatrick, J. W. (eds.) (2016). "
                "'Handbook of Bird Biology', 3rd ed. Cornell Lab of "
                "Ornithology / Wiley.")
CIT_PROCTOR = ("Proctor, N. S. & Lynch, P. J. (1993). 'Manual of Ornithology: "
               "Avian Structure and Function'. Yale University Press.")
CIT_PENNYCUICK = ("Pennycuick, C. J. (2008). 'Modelling the Flying Bird'. "
                  "Academic Press.")
CIT_NEWTON = ("Newton, I. (2008). 'The Migration Ecology of Birds'. "
              "Academic Press.")
CIT_CATCHPOLE = ("Catchpole, C. K. & Slater, P. J. B. (2008). 'Bird Song: "
                 "Biological Themes and Variations', 2nd ed. Cambridge "
                 "University Press.")
CIT_SUTHERLAND = ("Sutherland, W. J., Newton, I. & Green, R. E. (2004). "
                  "'Bird Ecology and Conservation: A Handbook of Techniques'. "
                  "Oxford University Press.")
CIT_STD = "Standard ornithology literature (peer-reviewed textbooks and journals)."
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "ornithology, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-ornithology", "name": "What Is Ornithology: The Science of Birds",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Ornithology is the scientific study of birds — their anatomy, behavior, "
  "ecology, evolution, and conservation. About 11,000 bird species have been "
  "formally described, and unlike insects or fungi, the great majority of the "
  "world's birds are already known to science: estimates put the true total "
  "at roughly 11,000 to 13,000, so ornithologists may already know 85 percent "
  "or more of all living bird species, with only a handful of new species "
  "described each year. Birds are the most intensively studied wild animals "
  "on Earth: millions of people watch them, hundreds of thousands of "
  "ornithologists band and count them, and birds serve as the leading "
  "indicators of environmental health — when bird populations shift, "
  "ecosystems are shifting. From Darwin's finches to the discovery of the "
  "magnetic compass in migratory birds, ornithology has repeatedly opened "
  "new chapters in biology."),
 "how_it_works": (
  "Ornithology works the way any field science works: observe, measure, "
  "mark, and follow. Ornithologists identify birds by sight and sound in the "
  "field, capture and band them with individually numbered leg bands to "
  "track survival and movement, census populations with point counts and "
  "transects, record songs and analyze them as spectrograms, and dissect the "
  "link between form and function in the lab — how a wing's shape predicts "
  "flight style, how a beak's shape predicts diet. Museum collections of "
  "millions of study skins anchor taxonomy: when a new population is found, "
  "its feathers, measurements, voice, and DNA are compared against the "
  "archive. Long-term datasets — some running for over a century — let "
  "ornithologists separate real population trends from year-to-year noise, "
  "which is why birds are the gold standard for tracking biodiversity "
  "change."),
 "key_points": [
  "Ornithology: the scientific study of birds — anatomy, behavior, ecology, evolution, conservation",
  "About 11,000 species described; the great majority of world birds are already known (unlike insects)",
  "Birds are the leading environmental indicators: their trends reveal ecosystem health",
  "Core methods: field identification, banding, censuses, song recording, museum collections",
  "Long-term datasets (some 100+ years) separate real trends from annual noise",
  "Birds repeatedly opened new chapters in biology: evolution, navigation, communication",
 ],
 "requirements": [
  "Binoculars and a field guide for identification practice",
  "Access to an outdoor site with wild birds for observation",
  "A notebook or app for recording sightings, counts, and behaviors",
 ],
 "standards": [
  "Taxonomy follows the eBird/Clements checklist conventions",
  "Field methods per Sutherland, Newton & Green (2004) standard techniques",
 ],
 "citations": [CIT_GILL, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: ornithology is the master class in reading a living "
  "system — every feather, note, and migration route is data. Manon's "
  "Signature take treats the bird as the original flying sensor platform: "
  "identify the mission from the hardware, then design the study the same "
  "way — observe first, measure second, conclude last."),
 "demo_kind": "bird_diversity",
},
{
 "key": "feather-definition", "name": "Feathers: The Defining Innovation of Birds",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Feathers are the defining innovation of birds — no other living animal "
  "has them. A feather is a branching structure of keratin: a central shaft "
  "(the rachis) carries barbs on each side, each barb carries smaller "
  "barbules, and the barbules lock together with microscopic hooks to form "
  "the smooth, airtight vane. A single flight feather can hold over a "
  "thousand barbs per side, each carrying hundreds of barbules — millions "
  "of interlocking parts per feather. Feathers do far more than enable "
  "flight: they insulate (trapping air against the skin), waterproof "
  "(oiled with preen-gland secretions), camouflage, display (the peacock's "
  "tail), and even produce sound. Fossils show feathers evolved in "
  "dinosaurs long before flight — first as insulation and display, with "
  "flight coming later."),
 "how_it_works": (
  "A feather works like a zipper made of branches. The rachis is the "
  "backbone; barbs branch off it at an angle; each barb's barbules carry "
  "tiny hooks (hamuli) on one side and smooth flanges on the other. When a "
  "bird preens, it draws the feather through its beak and the hooks "
  "re-engage — that is why a ruffled feather smooths back into a perfect "
  "vane. The interlocked vane is light, flexible, and nearly airtight, so "
  "it can push against the air on the downstroke and slice through it on "
  "the upstroke. Because keratin wears out, birds replace their feathers on "
  "a schedule called molt. Feather color comes two ways: pigments "
  "(melanins for blacks and browns, carotenoids for reds and yellows) and "
  "structural color — microscopic ridges that diffract light, making the "
  "iridescent blues and greens of hummingbirds and starlings."),
 "key_points": [
  "Feathers are unique to birds — the defining innovation of the group",
  "Structure: rachis -> barbs -> barbules -> hooklets, forming an interlocking vane",
  "Jobs: flight, insulation, waterproofing, camouflage, display, sound production",
  "Feathers evolved in dinosaurs before flight — insulation and display came first",
  "Color from pigments (melanin, carotenoids) and structural light diffraction",
  "Preening re-zips the barbule hooks; worn feathers are replaced by molt",
 ],
 "requirements": [
  "A shed feather (or photo) to examine barb structure under a hand lens",
  "Understanding of keratin as a protein building material",
  "A fossil-feather reference image (e.g. Archaeopteryx) for the deep-time context",
 ],
 "standards": [
  "Feather anatomy terminology per Proctor & Lynch (1993)",
  "Fossil context per current theropod-dinosaur literature",
 ],
 "citations": [CIT_PROCTOR, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: the feather is the original smart material — "
  "millions of self-repairing interlocks, lighter than any fabric humans "
  "make, replaced on schedule. Manon's Signature take: build systems like "
  "feathers — modular at the microscopic level, self-healing by routine, "
  "and scheduled for replacement before failure."),
 "demo_kind": "feather_structure",
},
{
 "key": "feather-types", "name": "Feather Types: Contour, Flight, Down, and More",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A bird wears several kinds of feathers, each engineered for its job. "
  "Flight feathers — the long primaries on the outer wing and secondaries "
  "on the inner wing, plus the tail rectrices — are stiff, asymmetric vanes "
  "that form the airfoil. Contour feathers tile the body like shingles, "
  "giving the bird its streamlined shape and first layer of insulation. "
  "Down feathers have a short shaft and loose, fluffy barbs with no "
  "hooks: they trap still air against the skin and do most of the "
  "insulating. Semipolumes sit between down and contour, adding loft; "
  "filoplumes are hair-like sensory feathers that report feather position "
  "to the brain; bristles around the beak and eyes act as guards and "
  "insect-catching nets in nightjars and flycatchers. Powder down in "
  "herons and parrots crumbles into waterproofing dust. Knowing the six "
  "types is the foundation of reading any bird's plumage."),
 "how_it_works": (
  "Each feather type works by tuning the same parts list. Flight feathers "
  "maximize vane stiffness: dense, hooked barbules and an asymmetric vane "
  "(narrow leading edge, wide trailing edge) so air pressure seals rather "
  "than leaks through. Down feathers do the opposite — unhooked, flexible "
  "barbules that splay into a three-dimensional tangle, trapping air in "
  "tiny pockets; still air is a superb insulator. Contour feathers overlap "
  "like roof tiles so water runs off and wind slides past. Filoplumes have "
  "almost no vane at all — just a shaft with a tuft — and sit beside the "
  "big feathers as strain gauges, telling the bird when a flight feather "
  "is bent or displaced. The bird's feather coat is thus layered: down "
  "against the skin for insulation, contour over it for shape and "
  "weatherproofing, flight feathers on wings and tail for the airfoil."),
 "key_points": [
  "Flight feathers (primaries, secondaries, rectrices): stiff asymmetric vanes form the airfoil",
  "Contour feathers: shingle-like tiling gives streamlined shape and weatherproofing",
  "Down feathers: loose unhooked barbs trap still air — the main insulation layer",
  "Semiplumes add loft; filoplumes sense feather position; bristles guard eyes and catch insects",
  "Powder down (herons, parrots) crumbles into waterproofing dust",
  "Six types, one parts list — each tuned by changing hook density and vane shape",
 ],
 "requirements": [
  "Reference images of each feather type for comparison",
  "A down feather or pillow down sample to feel the loft",
  "A flight feather to see vane asymmetry (narrow leading edge)",
 ],
 "standards": [
  "Feather-type terminology per Proctor & Lynch (1993)",
  "Functional descriptions per the Handbook of Bird Biology",
 ],
 "citations": [CIT_PROCTOR, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: one parts list, six products — contour, flight, "
  "down, semiplume, filoplume, bristle. Manon's Signature take treats the "
  "feather types as the masterclass in product-line engineering: same "
  "factory, same keratin, different tuning for different missions."),
 "demo_kind": "feather_types",
},
{
 "key": "bird-skeleton", "name": "The Bird Skeleton: Light, Rigid, and Built to Fly",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A bird's skeleton is a paradox: lighter than a mammal's skeleton of the "
  "same size, yet rigid enough to anchor the most powerful flight muscles "
  "in the animal kingdom. Weight is saved three ways. First, many bones "
  "are hollow with internal struts (pneumatized bones connected to the air "
  "sacs), cutting mass while keeping bending strength. Second, bones are "
  "fused where flexibility is not needed: the backbone is a rigid rod "
  "except at the neck and tail, the collarbones fuse into the furcula "
  "(wishbone) that springs with each wingbeat, and hand bones fuse into the "
  "carpometacarpus that carries the flight feathers. Third, the sternum "
  "carries a deep keel (carina) — a bony sail that gives the flight "
  "muscles a huge attachment area. In flying birds the skeleton is only "
  "about 5 percent of body weight, yet the pectoralis muscle alone can be "
  "15 to 25 percent."),
 "how_it_works": (
  "The skeleton works as a rigid airframe. Fusion is the key trick: a "
  "fused backbone cannot twist, so every newton of muscle force goes into "
  "the wings instead of bending the body — engineers call this a "
  "monocoque structure. The furcula acts as a spring, flexing outward as "
  "the wings rise and snapping back to help drive them down, storing "
  "elastic energy each stroke. The coracoid bones are struts bracing the "
  "wing joint against the sternum so the downstroke does not collapse the "
  "shoulder. Hollow bones resist bending nearly as well as solid ones "
  "because bending strength depends on material placed far from the "
  "center — a thin tube beats a solid rod of the same weight. The payoff: "
  "a frigatebird with a 2-meter wingspan weighs about as much as a "
  "house cat, and a huge fraction of that weight is engine, not airframe."),
 "key_points": [
  "Hollow, strut-braced (pneumatized) bones cut weight while keeping bending strength",
  "Fusion (backbone, furcula, carpometacarpus) makes a rigid airframe — force goes to the wings",
  "The keeled sternum anchors flight muscles that can be 15-25% of body weight",
  "Skeleton ~5% of body weight in flying birds — most weight is muscle, not bone",
  "The furcula springs with each wingbeat, storing elastic energy",
 ],
 "requirements": [
  "A bird skeleton diagram or model showing fusions and the keel",
  "A hollow bone cross-section (or tube vs rod demo) for the strength lesson",
  "Comparison weights: skeleton vs flight muscle percentages",
 ],
 "standards": [
  "Skeletal terminology per Proctor & Lynch (1993)",
  "Mass fractions per Pennycuick's flight-mechanics literature",
 ],
 "citations": [CIT_PROCTOR, CIT_PENNYCUICK],
 "sig_lens": (
  "Signature reading: the bird skeleton is the original lightweight "
  "airframe — fuse what must not flex, hollow what must not weigh, and "
  "spend the saved weight on engine. Manon's Signature take: every "
  "design has a weight budget; the bird spends its budget on muscle, "
  "never on frame."),
 "demo_kind": "hollow_bone",
},
{
 "key": "beak-anatomy", "name": "Beaks: The Bird's All-Purpose Tool",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A bird's beak is its hands, teeth, and toolbox combined — and its shape "
  "is the single best predictor of what the bird eats. Hummingbird beaks "
  "are slender probes matched to flower tubes; raptor beaks are hooked "
  "knives for tearing meat; duck beaks carry fine lamellae that strain "
  "food from water like a sieve; finch beaks are seed-cracking nutcrackers; "
  "woodpecker beaks are chisels backed by shock-absorbing skulls; heron "
  "beaks are spears. The beak is a keratin sheath over bone, growing "
  "continuously to offset wear. Darwin's finches made the beak famous: on "
  "the Galapagos, one ancestral finch radiated into species with beaks "
  "tuned to seeds, insects, cactus, and even blood — adaptive radiation "
  "written in keratin. Ornithologists measure beak length, depth, and width "
  "(morphometrics) to read diet, and even to track evolution in real time."),
 "how_it_works": (
  "The beak works as a lever system tuned to its food. Crushing beaks "
  "(finches, parrots) are short and deep: a short lever arm near the jaw "
  "joint multiplies bite force, and deep cross-sections resist the "
  "bending of cracking hard seeds. Probing beaks (hummingbirds, "
  "sandpipers) are long and slender: reach matters more than force, and "
  "some can open just the tip to pluck prey from crevices. Tearing beaks "
  "(hawks, shrikes) hook downward so the tip pierces and the tomial edge "
  "shears like a can opener. Straining beaks (ducks, flamingos) press the "
  "tongue against lamellae ridges, pumping water out and trapping food — "
  "flamingos even feed upside down to use the same trick. Because the "
  "keratin sheath grows continuously, wear from the diet sculpts the final "
  "shape: the beak you see is the running balance of growth and use."),
 "key_points": [
  "Beak shape is the best single predictor of a bird's diet",
  "Crushers (finches): short, deep levers multiply bite force",
  "Probers (hummingbirds, sandpipers): long, slender for reach",
  "Tearers (raptors): hooked tips pierce and shear meat",
  "Strainers (ducks, flamingos): lamellae sieve food from water",
  "Darwin's finches: one ancestor radiated into beaks for seeds, insects, cactus, blood",
 ],
 "requirements": [
  "Beak-shape photo set across diets for comparison",
  "Caliper measurements (length, depth, width) for morphometrics",
  "Darwin's finch beak chart for the adaptive-radiation lesson",
 ],
 "standards": [
  "Morphometric methods per standard field-ornithology practice",
  "Adaptive-radiation framing per Grant's finch research tradition",
 ],
 "citations": [CIT_GILL, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: the beak is the original interchangeable tool head "
  "— one interface, dozens of attachments, each matched to a job. "
  "Manon's Signature take: read the tool to know the trade, and when the "
  "job changes, evolve the tool — Darwin's finches did it in a few "
  "million years."),
 "demo_kind": "beak_tools",
},
{
 "key": "feet-legs", "name": "Feet and Legs: Built for a Lifestyle",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Bird feet are as specialized as beaks, and toe arrangement tells you "
  "how a bird lives. Most perching birds are anisodactyl — three toes "
  "forward, one back — the classic grip for branches. Woodpeckers and "
  "parrots are zygodactyl — two forward, two back — a climbing clamp. "
  "Ducks and gulls are totipalmate or palmate: webbed feet that double as "
  "paddles. Raptors carry talons — curved, needle-tipped killing tools "
  "driven by the strongest grip in the bird world. Ostriches run on two "
  "toes. And perching birds have a mechanical marvel: a tendon-locking "
  "system where crouching automatically tightens the toes around the "
  "branch, so a sleeping bird cannot fall off — the grip tightens as the "
  "body relaxes. What looks like a backward knee is actually the ankle "
  "(the intertarsal joint); the real knee is hidden up inside the body "
  "feathers."),
 "how_it_works": (
  "The foot works as a lifestyle-specific gripping or paddling machine. "
  "In perching birds, flexor tendons run from the leg muscles down behind "
  "the ankle to the toes; when the bird crouches, the tendons are pulled "
  "taut over the joint like a pulley, curling the toes automatically — "
  "no muscle effort needed, which is why roosting birds stay put all "
  "night. Ratchet-like tubercles on the tendon sheath add friction so the "
  "lock holds. Raptors trade the delicate lock for raw power: massive "
  "flexor muscles and talons with a piercing tip and a cutting inner edge "
  "can exert hundreds of newtons, enough to puncture and hold struggling "
  "prey. Webbed feet work as collapsible paddles — spreading on the power "
  "stroke, folding on the recovery — the same trick as a swim fin. Leg "
  "scales (the scutes) are reptilian skin retained where feathers would "
  "only get in the way."),
 "key_points": [
  "Toe arrangements: anisodactyl (perch), zygodactyl (climb), webbed (swim), raptorial (kill)",
  "Tendon-locking mechanism: crouching auto-tightens the grip — sleeping birds cannot fall",
  "The visible 'backward knee' is the ankle; the true knee is hidden in the body",
  "Raptor talons: curved piercing tips + massive flexor muscles = the strongest bird grip",
  "Webbed feet work as collapsible paddles: spread on power stroke, fold on recovery",
  "Leg scutes are retained reptilian skin where feathers would hinder",
 ],
 "requirements": [
  "Foot-type photo set (perching, raptor, duck, woodpecker)",
  "A perching-bird foot diagram showing the flexor tendon path",
  "Understanding of pulley mechanics for the locking lesson",
 ],
 "standards": [
  "Foot-type terminology per standard ornithological references",
  "Tendon-lock mechanism per Proctor & Lynch (1993)",
 ],
 "citations": [CIT_PROCTOR, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: the perching foot is the original passive safety "
  "lock — no power, no control loop, just geometry that grips tighter "
  "when it matters. Manon's Signature take: the best safety systems "
  "need no electricity; design the mechanism so the dangerous state is "
  "the locked state."),
 "demo_kind": "foot_types",
},
{
 "key": "avian-respiration", "name": "The Avian Respiratory System: Breathing on the Move",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Birds have the most efficient respiratory system of any vertebrate — "
  "and it is built completely differently from ours. Instead of "
  "dead-end lungs that fill and empty, birds have small, rigid lungs "
  "plus a system of thin-walled air sacs (usually nine) that act as "
  "bellows. Air flows through the lung in ONE direction — in during both "
  "inhalation and exhalation — so the lung always sees fresh air, and "
  "oxygen extraction is far more complete. Inside the lung, blood flows "
  "at right angles to the airflow (cross-current exchange), squeezing "
  "even more oxygen from each breath. This is the machinery that lets "
  "bar-headed geese fly over the Himalayas and hummingbirds hover: at "
  "altitudes where a mammal would collapse, a bird's lungs still deliver. "
  "The air sacs also reach into the hollow bones, lightening the "
  "skeleton, and help dump the enormous heat of flight muscles."),
 "how_it_works": (
  "The system works in two breaths for one parcel of air. First "
  "inhalation: fresh air bypasses the lung and fills the posterior air "
  "sacs. First exhalation: that air is pushed forward through the lung, "
  "where parabronchi (tiny parallel tubes) carry it past blood "
  "capillaries in cross-current flow — blood and air moving at right "
  "angles, which keeps a diffusion gradient along the whole tube. Second "
  "inhalation: the now-stale air moves into the anterior air sacs. Second "
  "exhalation: it is expelled. Net result: unidirectional flow through "
  "the gas-exchange surface at all times, unlike our tidal in-and-out "
  "lungs that always mix fresh air with stale. Because the lung itself "
  "is rigid and does not expand, the air sacs do all the pumping — "
  "squeezed by the same body movements as flight, so breathing and "
  "wingbeats can synchronize in small birds."),
 "key_points": [
  "Rigid lungs + bellows-like air sacs replace our expandable tidal lungs",
  "Unidirectional airflow: the lung sees fresh air on both inhale and exhale",
  "Cross-current exchange (air vs blood at right angles) maximizes oxygen uptake",
  "Air sacs also pneumatize bones and dump flight-muscle heat",
  "This system powers Himalayan overflights and hovering — unmatched among vertebrates",
  "Breathing can synchronize with wingbeats in small birds",
 ],
 "requirements": [
  "Air-sac/lung airflow diagram showing the two-breath cycle",
  "Comparison with mammalian tidal breathing for contrast",
  "Altitude context: oxygen partial pressures at sea level vs 6,000 m",
 ],
 "standards": [
  "Respiratory anatomy per Proctor & Lynch (1993)",
  "Cross-current model per standard avian-physiology literature",
 ],
 "citations": [CIT_PROCTOR, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: the bird lung is the original continuous-flow "
  "reactor — no batch mixing, no stale dead volume, fresh feed at all "
  "times. Manon's Signature take: wherever a process mixes fresh input "
  "with stale output, redesign it for one-way flow like the bird did."),
 "demo_kind": "air_sac_breathing",
},
{
 "key": "bird-senses", "name": "Bird Senses: Seeing the World Like a Bird",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Birds live by sight to a degree no mammal matches. A bird's eyes are "
  "enormous — an eagle's eye is about the same size as a human's despite "
  "the eagle weighing far less — and they see a world we cannot: most "
  "birds are tetrachromatic, with four cone types including one tuned to "
  "ultraviolet, plus colored oil droplets that sharpen color "
  "discrimination. A kestrel can see a vole's urine trail glowing in UV; "
  "many songbirds have UV patterns on their plumage invisible to us but "
  "blazing to mates. Birds also process vision faster: small birds have "
  "flicker-fusion rates over 100 frames per second (humans manage about "
  "60), so they perceive motion in finer slices of time — the world moves "
  "slower for a flycatcher snapping insects midair. Hearing is the second "
  "great sense: owls locate prey in total darkness by sound alone, and "
  "songbirds hear fine details in song we need slow-motion playback to "
  "catch. Smell, long dismissed in birds, is now known to guide "
  "tubenoses across oceans and help songbirds recognize kin."),
 "how_it_works": (
  "The eye works as a high-speed, four-channel camera. The large eye "
  "gathers light and the dense retina packs photoreceptors; many birds "
  "have two foveae per eye — one for sharp forward binocular vision, one "
  "for sharp lateral monocular vision — so a hawk can watch ahead and "
  "sideways at full resolution. The fourth cone plus oil droplets extends "
  "color into the near-ultraviolet (down to about 300 nm) and sharpens "
  "each channel's tuning, giving birds arguably the finest color vision "
  "in the animal kingdom. Fast photoreceptor recovery gives the high "
  "flicker-fusion rate: each 'frame' of vision refreshes quicker, so fast "
  "motion stays sharp. The pecten, a comb-like structure inside the eye, "
  "is thought to nourish the retina and may aid motion detection. Hearing "
  "works through the same inner-ear plan as ours but tuned: barn owls "
  "have vertically asymmetrical ears, so a sound arriving a microsecond "
  "earlier at one ear gives elevation as well as direction."),
 "key_points": [
  "Tetrachromatic vision: four cone types including UV (down to ~300 nm) + oil droplets",
  "Two foveae per eye in many birds: sharp vision forward and sideways at once",
  "Flicker fusion 100+ Hz in small birds vs ~60 in humans — finer slices of time",
  "UV vision reveals hidden plumage signals and prey trails (kestrels track vole urine)",
  "Owl hearing: asymmetrical ears give 3D sound localization in total darkness",
  "Smell matters: tubenoses navigate oceans by scent; songbirds recognize kin by odor",
 ],
 "requirements": [
  "UV vs human-visible plumage comparison images",
  "A flicker-fusion demo (or video frame-rate analogy) for the speed lesson",
  "Barn owl ear-asymmetry diagram for the hearing lesson",
 ],
 "standards": [
  "Visual physiology per the Handbook of Bird Biology",
  "Sensory ecology per standard ornithology textbooks",
 ],
 "citations": [CIT_HANDBOOK, CIT_GILL],
 "sig_lens": (
  "Signature reading: the bird eye is the original multispectral "
  "high-speed camera — four channels, dual foveae, 100+ frames per "
  "second, in a package lighter than a marble. Manon's Signature take: "
  "when you think you have seen the whole picture, check the channels "
  "you cannot see — the bird found a whole spectrum we missed."),
 "demo_kind": "bird_vision",
},
{
 "key": "thermoregulation", "name": "Staying Warm: Bird Thermoregulation",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Birds are endothermic — warm-blooded — and they run hot: most birds "
  "hold body temperatures around 40 to 42 degrees Celsius, hotter than "
  "any mammal. That heat is the price of the avian lifestyle: flight "
  "muscles are furnaces, and a small bird can starve in a single cold "
  "night if it cannot keep the furnace fed. Birds stay warm with the "
  "best insulation in nature (fluffed feathers trap still air; a chickadee "
  "can nearly double its insulation by fluffing), with countercurrent "
  "heat exchangers in the legs (warm arterial blood gives up its heat to "
  "cool venous blood returning from the feet, so heat stays in the body "
  "core instead of bleeding into ice water), and with behavior — huddling, "
  "sunning, shivering, and torpor. Hummingbirds and swifts drop into "
  "nocturnal torpor, letting body temperature fall by 20 degrees or more "
  "to survive the night on yesterday's nectar. In heat, birds pant, "
  "flutter the throat (gular flutter), and shunt blood to unfeathered "
  "skin to dump warmth."),
 "how_it_works": (
  "Thermoregulation works as a layered control system. The feather coat "
  "is the first layer: each feather can be raised or lowered by tiny "
  "muscles, changing the trapped-air thickness and thus the insulation "
  "value in seconds. Beneath it, the countercurrent exchanger in the legs "
  "recovers heat that would otherwise be lost through the unfeathered "
  "feet — arterial and venous vessels run side by side in opposite "
  "directions, so heat flows from outgoing to incoming blood and the foot "
  "stays just above freezing while the core stays at 41 degrees. When "
  "insulation is not enough, shivering burns fuel for heat, and torpor "
  "deliberately lowers the thermostat set-point overnight, cutting "
  "energy use by more than half. In heat the system reverses: blood is "
  "shunted to the feet, beak, and throat surfaces, and evaporative "
  "cooling (panting, gular flutter) dumps heat without wasting water the "
  "way sweating would."),
 "key_points": [
  "Birds run hotter than mammals: 40-42 C body temperature",
  "Fluffed feathers are adjustable insulation — a chickadee can nearly double its loft",
  "Countercurrent heat exchange in legs keeps core heat from bleeding into cold water",
  "Nocturnal torpor: hummingbirds drop 20+ degrees overnight to survive on stored fuel",
  "Heat dumping: panting, gular flutter, blood shunted to bare skin",
  "Insulation + circulation + behavior form a layered control system",
 ],
 "requirements": [
  "Thermometer/IR-camera imagery of a bird's warm core vs cool feet",
  "Countercurrent exchanger diagram (artery/vein side-by-side flow)",
  "Torpor temperature curve (evening drop, dawn rewarming)",
 ],
 "standards": [
  "Thermal physiology per the Handbook of Bird Biology",
  "Torpor energetics per standard avian-physiology literature",
 ],
 "citations": [CIT_HANDBOOK, CIT_GILL],
 "sig_lens": (
  "Signature reading: the bird is the original adaptive thermal system "
  "— adjustable insulation, heat recovery plumbing, and a thermostat "
  "that can be deliberately lowered overnight. Manon's Signature take: "
  "never fight heat loss with brute force alone; recover it, reroute "
  "it, and when fuel is short, lower the set-point."),
 "demo_kind": "countercurrent",
},
# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "flight-physics", "name": "How Birds Fly: Lift, Drag, Thrust, and Weight",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Flight is a four-force balance: lift opposes weight, thrust opposes "
  "drag, and a bird stays aloft only while the books balance. Lift comes "
  "from the wing as an airfoil — air moving faster over the curved upper "
  "surface drops in pressure, and the wing is pushed up; the standard "
  "lift equation says lift grows with air density, the square of "
  "airspeed, wing area, and the lift coefficient. That square on speed "
  "is why takeoff is the hardest part of flight: a bird must accelerate "
  "to flying speed before the wings can carry it, which is why heavy "
  "birds run, hop, or dive off cliffs to launch. Drag comes in two main "
  "flavors — parasitic drag from the body's shape and induced drag, the "
  "unavoidable cost of making lift (the wingtip vortices). Thrust in "
  "flapping flight comes from the wings themselves, tilted to push air "
  "backward as well as down. Gliding birds skip thrust and spend "
  "altitude instead, trading height for distance."),
 "how_it_works": (
  "The wing works as a shape-shifting airfoil. On the downstroke the "
  "wing is spread, twisted nose-down, and driven through the air: the "
  "outer wing acts like a propeller blade, generating both lift and "
  "forward thrust, while the inner wing mostly makes lift. On the "
  "upstroke the wing folds and feathers — rotating so the leading edge "
  "cuts the air — to minimize drag while it resets. Wing twist "
  "(washout) keeps the angle of attack safe along the whole span so no "
  "section stalls first. The tail works as an adjustable extra wing and "
  "rudder: spread for more lift and braking at landing, fanned for "
  "steering, folded away at speed to cut drag. Alula — the 'thumb' "
  "feather on the leading edge — pops up at high angles of attack like "
  "an aircraft slat, keeping airflow attached and delaying the stall "
  "during slow flight and landing."),
 "key_points": [
  "Four forces: lift vs weight, thrust vs drag — flight is a balance sheet",
  "Lift = 0.5 * air density * speed^2 * wing area * lift coefficient (speed matters most)",
  "Takeoff is hardest because lift needs speed first — heavy birds run or dive to launch",
  "Induced drag is the unavoidable cost of making lift (wingtip vortices)",
  "Downstroke makes lift + thrust; upstroke folds and feathers to cut drag",
  "Alula acts as a leading-edge slat, delaying stall at slow speeds",
 ],
 "requirements": [
  "The lift equation with each term defined",
  "Slow-motion wingbeat video or diagram showing downstroke vs upstroke",
  "An aircraft-wing analogy reference for the airfoil lesson",
 ],
 "standards": [
  "Aerodynamics per Pennycuick (2008) 'Modelling the Flying Bird'",
  "Force-balance framing per standard flight-mechanics texts",
 ],
 "citations": [CIT_PENNYCUICK, CIT_GILL],
 "sig_lens": (
  "Signature reading: the wing is the original variable-geometry "
  "airfoil — it retunes itself every half-second. Manon's Signature "
  "take: the four-force balance is a universal design ledger; every "
  "flying machine, bird or built, must balance the same four books."),
 "demo_kind": "lift_eq",
},
{
 "key": "wing-shapes", "name": "Wing Shapes and Flight Styles",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Wing shape predicts flight style the way beak shape predicts diet. "
  "Long, narrow, high-aspect-ratio wings (albatross, aspect ratio 15+) "
  "are soaring machines: they minimize induced drag and glide for hours "
  "without flapping. Short, broad, low-aspect-ratio wings (sparrows, "
  "pheasants) are built for explosive takeoff and tight maneuvering in "
  "clutter. Pointed wings (falcons, swifts) cut drag for sheer speed. "
  "Slotted wings (eagles, vultures) — broad wings with finger-like "
  "primary tips — spread the tip vortex into smaller pieces, cutting "
  "induced drag while keeping the wing short enough to maneuver. "
  "Elliptical wings (most songbirds) are the all-rounders. Two numbers "
  "capture most of it: aspect ratio (wingspan squared divided by wing "
  "area — high means glider) and wing loading (weight divided by wing "
  "area — high means fast, low means maneuverable). Read a bird's wings "
  "and you can predict where it flies, how fast, and how it hunts."),
 "how_it_works": (
  "Wing shape works by trading induced drag against maneuverability. "
  "Induced drag falls as aspect ratio rises — long slender wings make "
  "less tip vortex per unit lift — which is why the albatross can "
  "dynamic-soar for days: its wings are the closest thing in nature to "
  "a sailplane's. But long wings are slow to accelerate and hard to "
  "turn, so forest birds go the other way: short broad wings beat the "
  "air into quick bursts of lift for near-vertical takeoff and "
  "doorway-tight turns. Slotted tips work like winglets on airliners: "
  "each 'finger' carries its own small vortex instead of one big one, "
  "so eagles get glider efficiency from a wing short enough to thread "
  "between trees. Wing loading sets the speed: heavily loaded wings "
  "(falcons, auks) must fly fast to stay up but slice through wind; "
  "lightly loaded wings (harriers, owls) fly slow and turn on a dime."),
 "key_points": [
  "High aspect ratio (albatross 15+): soaring efficiency, minimal induced drag",
  "Low aspect ratio (sparrows, pheasants): explosive takeoff, tight maneuvering",
  "Pointed wings (falcons, swifts): speed; slotted wings (eagles): efficiency + maneuver",
  "Aspect ratio = wingspan^2 / wing area; wing loading = weight / wing area",
  "Slotted primary tips work like airliner winglets, splitting the tip vortex",
  "Read the wings: predict habitat, speed, and hunting style",
 ],
 "requirements": [
  "Wing-shape silhouette set (albatross, falcon, eagle, sparrow, swift)",
  "Aspect ratio and wing loading formulas with worked examples",
  "Sailplane/airliner analogy references for the engineering lesson",
 ],
 "standards": [
  "Wing-shape classification per Pennycuick (2008)",
  "Aspect-ratio conventions per standard flight literature",
 ],
 "citations": [CIT_PENNYCUICK, CIT_HANDBOOK],
 "sig_lens": (
  "Signature reading: the wing planform is the original mission "
  "profile in hardware — long for endurance, short for agility, "
  "slotted for the compromise. Manon's Signature take: two numbers "
  "(aspect ratio, wing loading) predict the whole flight envelope; "
  "find the two numbers that predict any system's envelope."),
 "demo_kind": "wing_shape",
},
{
 "key": "flapping-mechanics", "name": "Flapping Flight: The Power Stroke and Recovery",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Flapping is the most expensive form of locomotion per unit time in "
  "the animal kingdom — and birds do it for hours. The engine is the "
  "pectoralis, the great breast muscle, which drives the downstroke "
  "(the power stroke); the smaller supracoracoideus, routed over the "
  "shoulder by a pulley-like tendon, lifts the wing for the upstroke. "
  "Together they can be a quarter of the bird's weight. Flapping comes "
  "in styles: continuous flapping (ducks, pigeons), flap-gliding "
  "(raptors, gulls — flap to gain height, glide to spend it), and "
  "bounding flight (finches, woodpeckers — flap in bursts, then fold "
  "the wings and ballistic-coast). Hummingbirds take flapping to the "
  "extreme: wings beating 50+ times per second in a figure-eight, "
  "generating lift on both strokes to hover. The physics is momentum "
  "theory: the wing accelerates a disc of air downward, and the "
  "reaction pushes the bird up — hovering power scales with weight to "
  "the 3/2 power divided by the disc area, which is why only small "
  "birds hover well."),
 "how_it_works": (
  "The stroke works as an asymmetric pump. Downstroke: the wing is "
  "fully spread and pronated (twisted nose-down); the pectoralis fires "
  "and the outer wing sweeps down and forward, accelerating air down "
  "and back — lift plus thrust. Upstroke: the wing supinates, partially "
  "folds, and the supracoracoideus hauls it up with minimal resistance; "
  "in slow flight the upstroke still makes some lift, in fast flight it "
  "makes nearly none. Bounding flight exploits the square law of drag: "
  "flapping hard at high speed then coasting folded can beat continuous "
  "flapping because drag rises with speed squared while lift is banked "
  "as altitude. Asynchronous (myogenic) flight muscle in some insects "
  "fires multiple strokes per nerve impulse, but birds use synchronous "
  "muscle — one impulse, one stroke — driven by nerves firing up to "
  "hundreds of times per second in hummingbirds. Elastic storage in "
  "tendons and the furcula spring returns some energy each stroke."),
 "key_points": [
  "Pectoralis drives the downstroke; supracoracoideus (via shoulder pulley) drives the upstroke",
  "Flight muscles can be ~25% of body weight — the largest engine fraction in vertebrates",
  "Styles: continuous flapping, flap-gliding, bounding (flap-burst + folded coast)",
  "Hummingbirds hover with 50+ Hz figure-eight strokes, lift on both strokes",
  "Hovering power scales as weight^1.5 / disc area — only small birds hover well",
  "Elastic storage in furcula and tendons returns energy each stroke",
 ],
 "requirements": [
  "Pectoralis/supracoracoideus anatomy diagram with the shoulder pulley",
  "Slow-motion footage references for each flapping style",
  "Momentum-theory hover equation with a hummingbird worked example",
 ],
 "standards": [
  "Muscle anatomy per Proctor & Lynch (1993)",
  "Hover power scaling per Pennycuick (2008)",
 ],
 "citations": [CIT_PROCTOR, CIT_PENNYCUICK],
 "sig_lens": (
  "Signature reading: flapping is the original high-frequency "
  "reciprocating engine — a quarter of the machine's weight is motor, "
  "and the recovery stroke is engineered to cost almost nothing. "
  "Manon's Signature take: in any cyclic machine, the return stroke "
  "is where efficiency is won or lost."),
 "demo_kind": "power_stroke",
},
{
 "key": "soaring-gliding", "name": "Soaring and Gliding: The Free Ride",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Soaring birds fly for free — or close to it. A frigatebird can stay "
  "aloft for weeks, an albatross can circle the Southern Ocean without "
  "landing, and a vulture can cross a continent on a few wingbeats. The "
  "trick is to harvest energy from the air itself. Thermal soaring uses "
  "rising columns of warm air: the bird circles inside the updraft, "
  "gaining altitude for free, then glides to the next thermal. Slope "
  "soaring rides wind deflected upward by ridges and cliffs. Dynamic "
  "soaring — the albatross's specialty — harvests the wind gradient "
  "over ocean waves, climbing into faster air and diving into slower "
  "air in a looping maneuver that adds energy each cycle. The currency "
  "is the glide ratio: distance forward per unit of height lost. An "
  "albatross glides about 20 meters forward for every meter it sinks; "
  "from 1,000 meters up, that is 20 kilometers of free travel."),
 "how_it_works": (
  "Soaring works by spending the atmosphere's energy instead of the "
  "bird's. In a thermal, the air rises faster than the bird sinks "
  "through it, so circling inside the column converts the atmosphere's "
  "heat into the bird's altitude — the bird is effectively climbing an "
  "invisible elevator. Between thermals the bird glides at its best-glide "
  "speed, the speed where the ratio of lift to drag is highest, losing "
  "altitude as slowly as possible per kilometer. Dynamic soaring is "
  "subtler: by climbing windward into faster-moving air, the bird's "
  "airspeed jumps without effort; it turns, dives downwind gaining "
  "ground speed, and repeats — each loop nets energy from the wind "
  "gradient, like a sailboat tacking. Vultures read the sky for "
  "thermals the way sailors read water for wind: cumulus clouds mark "
  "the tops of thermals, and experienced birds chain them across "
  "hundreds of kilometers."),
 "key_points": [
  "Three soaring styles: thermal (rising warm air), slope (ridge lift), dynamic (wind gradient)",
  "Glide ratio = forward distance per unit height lost (albatross ~20:1)",
  "Thermals convert atmospheric heat into free altitude; best-glide speed maximizes range",
  "Dynamic soaring harvests the wind gradient over waves — energy gained each loop",
  "Frigatebirds stay aloft for weeks; albatrosses circle oceans without landing",
  "Reading the sky (cumulus = thermal tops) is the soaring bird's navigation skill",
 ],
 "requirements": [
  "Thermal/slope/dynamic soaring diagrams",
  "Glide-polar concept: sink rate vs airspeed, best-glide point",
  "Tracking-map examples (frigatebird, albatross) for the endurance lesson",
 ],
 "standards": [
  "Soaring mechanics per Pennycuick (2008)",
  "Tracking data per modern biologging literature",
 ],
 "citations": [CIT_PENNYCUICK, CIT_GILL],
 "sig_lens": (
  "Signature reading: soaring is the original free-energy harvesting "
  "— the bird spends the sky's budget, not its own. Manon's Signature "
  "take: before burning fuel, look for the gradient — heat, wind, or "
  "slope — that will carry you for free."),
 "demo_kind": "glide_polar",
},
{
 "key": "migration-why", "name": "Migration I: Why Birds Travel the World",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Every year, billions of birds undertake some of the longest journeys "
  "on Earth. The Arctic tern flies some 70,000 kilometers a year, pole "
  "to pole, chasing an endless summer. The bar-tailed godwit flies "
  "11,000 kilometers nonstop from Alaska to New Zealand — over open "
  "ocean, with no landmarks, no rest, no food — burning half its body "
  "weight in fat. Why? Migration is an arbitrage on the seasons: breed "
  "where summer brings explosive food (Arctic insects, tundra daylight "
  "around the clock), winter where survival is cheap (tropical food "
  "year-round). The journey is timed to arrive exactly when food peaks "
  "— and the penalty for mistiming is starvation. Migration is "
  "controlled by an internal clock: changing day length triggers "
  "restlessness (zugunruhe), fattening, and even the shrinking and "
  "regrowth of digestive organs to make room for fuel and flight "
  "muscles."),
 "how_it_works": (
  "Migration works as a programmed seasonal commute. Photoperiod "
  "(day length) is the reliable calendar: as days shorten or lengthen "
  "past a threshold, hormones trigger hyperphagia (extreme eating) and "
  "the bird doubles its weight in fat — the fuel of migration, packing "
  "about 37 kilojoules per gram. The gut and liver shrink while flight "
  "muscles and heart grow, converting the bird from a digestion machine "
  "into a flying fuel tank. Departure is timed to weather windows; "
  "en route, birds ride tailwinds and stop at staging sites to refuel "
  "(except the nonstop champions like godwits, which carry it all). "
  "Arrival must match the food peak: insect-eaters arriving after the "
  "caterpillar flush starve. Young birds on their first migration often "
  "fly the route on pure instinct — clock-and-compass orientation with "
  "no guide — while experienced birds refine the route with learned "
  "landmarks and wind knowledge."),
 "key_points": [
  "Migration arbitrages the seasons: breed in food-rich summers, winter where survival is cheap",
  "Arctic tern ~70,000 km/year; bar-tailed godwit 11,000 km nonstop over open ocean",
  "Day length triggers zugunruhe (migratory restlessness), fattening, and organ remodeling",
  "Fat packs ~37 kJ/g — the flight fuel; godwits burn half their body weight",
  "Arrival must match the food peak; mistiming means starvation",
  "First-time migrants navigate by instinct; veterans refine routes with experience",
 ],
 "requirements": [
  "Migration-route maps (Arctic tern, godwit) for scale",
  "Zugunruhe/fattening physiology diagram",
  "Fat-energy math: grams of fat per kilometer of flight",
 ],
 "standards": [
  "Migration ecology per Newton (2008)",
  "Physiological remodeling per standard migration literature",
 ],
 "citations": [CIT_NEWTON, CIT_GILL],
 "sig_lens": (
  "Signature reading: migration is the original logistics operation — "
  "fuel up at the depot, remodel the vehicle for the journey, depart "
  "on the weather window, arrive exactly on schedule. Manon's "
  "Signature take: the godwit proves that with enough fuel and a "
  "perfect plan, even an ocean is just a distance."),
 "demo_kind": "migration_math",
},
{
 "key": "migration-navigation", "name": "Migration II: How Birds Navigate",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A young warbler flying alone at night from Canada to South America — "
  "never having made the trip — still arrives. Birds navigate with a "
  "toolkit no human engineer has matched: a sun compass (with an "
  "internal clock to correct for the sun's movement), a star compass "
  "(learning the rotation center of the night sky), a magnetic compass "
  "(sensing the Earth's field, including its inclination angle), "
  "polarized-light patterns, landmarks, and even smell. Clock-shift "
  "experiments proved the sun compass: shift a bird's internal clock "
  "by 6 hours and its chosen direction rotates by 90 degrees — exactly "
  "what a time-compensated sun compass predicts. The magnetic sense is "
  "the strangest: evidence points to quantum effects in the retina "
  "(cryptochrome proteins forming radical pairs sensitive to magnetic "
  "inclination) — birds may literally see the magnetic field. Redundant "
  "compasses cross-check each other; when one is unreliable (cloudy "
  "nights hide the stars), the others take over."),
 "how_it_works": (
  "Navigation works as a multi-sensor fusion system with a map and a "
  "compass. The compasses give direction: the sun compass reads the "
  "sun's azimuth and corrects with the circadian clock; the star "
  "compass uses the center of celestial rotation as north; the magnetic "
  "compass reads the inclination (dip) angle of field lines — steep at "
  "the poles, flat at the equator — which tells the bird its latitude "
  "band and gives an axis for direction. The map sense — true "
  "navigation, knowing where you are relative to home — is still "
  "partly mysterious, but experiments show displaced birds correct "
  "toward home, implying a large-scale coordinate sense built from "
  "magnetic intensity gradients, infrasound, and odors. Young birds use "
  "a simpler 'clock-and-compass' program (fly direction X for Y days); "
  "adults upgrade to true navigation with experience. Redundancy is the "
  "design principle: no single cue is trusted alone."),
 "key_points": [
  "Toolkit: sun compass (+clock correction), star compass, magnetic compass, landmarks, smell",
  "Clock-shift proof: 6-hour shift rotates heading 90 degrees — the sun compass confirmed",
  "Magnetic sense may use quantum radical pairs in retinal cryptochrome — birds may see the field",
  "Inclination compass: field-line dip angle gives latitude band and direction axis",
  "Juveniles use clock-and-compass; adults graduate to true map-based navigation",
  "Redundant compasses cross-check — no single cue is trusted alone",
 ],
 "requirements": [
  "Compass-toolkit diagram (sun, stars, magnetic, landmarks)",
  "Clock-shift experiment explanation for the proof lesson",
  "Inclination-angle vs latitude chart for the magnetic lesson",
 ],
 "standards": [
  "Orientation mechanisms per Newton (2008) and standard reviews",
  "Cryptochrome hypothesis per current magnetoreception literature",
 ],
 "citations": [CIT_NEWTON, CIT_STD],
 "sig_lens": (
  "Signature reading: the bird is the original multi-sensor navigator "
  "— five compasses, cross-checked, with a quantum sensor in the eye. "
  "Manon's Signature take: never trust one instrument; fuse many, "
  "and let the strange ones (quantum vision) stay on the table until "
  "disproven."),
 "demo_kind": "navigation_cues",
},
{
 "key": "syrinx", "name": "The Syrinx: The Bird Voice Box",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Birds sing with an instrument mammals do not have: the syrinx, "
  "located deep in the chest where the windpipe forks into the lungs. "
  "Because it sits at the fork, the syrinx has TWO independent sound "
  "sources — one in each bronchus — and many songbirds can play them "
  "separately, singing two notes at once or switching between sides "
  "mid-song faster than any single voice box could. The brown thrasher "
  "can produce two simultaneous tones; some birds sing duets with "
  "themselves. Sound is made by vibrating membranes (the labia) driven "
  "by air from the air sacs, tuned by syringeal muscles — songbirds "
  "have up to seven pairs of these muscles for fine control. The upper "
  "vocal tract (throat, beak) then filters the sound, the way a "
  "trumpet's bell shapes its tone. This is why a 20-gram warbler can "
  "fill a forest with sound: a double instrument, precision-muscled, "
  "driven by the most efficient lungs in nature."),
 "how_it_works": (
  "The syrinx works as a dual-reed wind instrument. Air from the "
  "posterior air sacs flows up through each bronchus; at the syrinx, "
  "the labia (membranous folds) are set into vibration, like lips "
  "buzzing into a trumpet. Tension in the labia — controlled by the "
  "syringeal muscles — sets the pitch: tighter means higher, the same "
  "way a guitar string works. Because each side is independently "
  "muscled and valved, the left and right bronchi can produce "
  "different frequencies simultaneously, or alternate in rapid "
  "succession to build complex syllables no single source could "
  "produce. The bird then shapes the raw tone with its vocal tract: "
  "opening the beak wide emphasizes higher harmonics, and throat "
  "movements tune resonances. Neural control comes from dedicated "
  "brain song nuclei — the most specialized vocal-learning circuitry "
  "outside humans — which is why only some birds (songbirds, parrots, "
  "hummingbirds) truly learn their songs."),
 "key_points": [
  "The syrinx sits where the trachea forks — giving TWO independent sound sources",
  "Many songbirds sing two notes at once or switch sides mid-song",
  "Pitch set by labial tension (syringeal muscles); tone shaped by beak and throat",
  "Driven by air-sac pressure — the efficient avian lung powers the loudest small voices",
  "Dedicated brain song nuclei control it — the basis of vocal learning",
  "Only songbirds, parrots, and hummingbirds truly learn songs; others are innate",
 ],
 "requirements": [
  "Syrinx anatomy diagram (tracheal fork, labia, syringeal muscles)",
  "Two-voice spectrogram example (brown thrasher) for the dual-source lesson",
  "Mammal-larynx comparison for contrast",
 ],
 "standards": [
  "Syrinx anatomy per Proctor & Lynch (1993)",
  "Vocal-production framing per Catchpole & Slater (2008)",
 ],
 "citations": [CIT_PROCTOR, CIT_CATCHPOLE],
 "sig_lens": (
  "Signature reading: the syrinx is the original stereo synthesizer — "
  "two oscillators, independent control, one air supply. Manon's "
  "Signature take: when one channel limits you, add a second channel "
  "at the fork, not at the end."),
 "demo_kind": "syrinx_voices",
},
{
 "key": "song-learning", "name": "Birdsong II: Learning, Dialects, and Repertoires",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Many birds are not born knowing their songs — they learn them, the "
  "way human children learn speech. A young songbird listens during a "
  "sensitive period, memorizes a tutor's song as a template, then "
  "practices in a babbling 'subsong' phase until its own song matches "
  "the memory. Because songs are learned, they drift: neighborhoods "
  "develop dialects, and researchers can map song dialects the way "
  "linguists map human accents. Repertoires vary wildly — a brown "
  "thrasher commands over a thousand song types, a marsh wren over a "
  "hundred, while some species sing a single song for life. Females "
  "listen hard: in many species, larger repertoires and more complex "
  "songs signal a healthier, better-developed male, and females choose "
  "mates partly by song. Song is also a territory weapon — the dawn "
  "chorus is males announcing 'this ground is taken' to every rival "
  "within earshot."),
 "how_it_works": (
  "Song learning works in two phases under dedicated brain hardware. "
  "Phase one (sensory): the young bird hears adult song and stores a "
  "neural template in the song system. Phase two (sensorimotor): it "
  "babbles subsong, hears its own errors, and iteratively corrects "
  "toward the template — a biological version of gradient descent, "
  "running on the HVC and RA brain nuclei. Deafen a bird before "
  "learning and it sings only a crude innate song; tutor it with "
  "recordings and it learns the recording. Dialects form because "
  "learning is imperfect and local: each generation copies its "
  "neighbors with small errors, so songs diverge between populations "
  "the way languages do. Repertoire size is built by recombining "
  "learned syllables — the thrasher's thousand songs are variations "
  "on a learned theme. The dawn chorus works by honest signaling: "
  "singing all morning is energetically expensive, so only a male in "
  "good condition can keep it up — rivals and females both read the "
  "effort."),
 "key_points": [
  "Songbirds learn songs: memorize a tutor template, then practice (subsong) to match it",
  "Learning runs on dedicated brain nuclei (HVC, RA) — the most specialized vocal circuitry outside humans",
  "Imperfect local copying creates dialects — mappable like human accents",
  "Repertoires: brown thrasher 1,000+ types; marsh wren 100+; some species just one",
  "Complex songs honestly signal male quality — females choose partly by song",
  "The dawn chorus is a territory broadcast: 'this ground is taken'",
 ],
 "requirements": [
  "Song-learning timeline diagram (sensory -> sensorimotor phases)",
  "Dialect-map example for the cultural-evolution lesson",
  "Spectrogram pairs (tutor vs pupil) showing the match",
 ],
 "standards": [
  "Song learning per Catchpole & Slater (2008)",
  "Dialect methods per standard bioacoustics literature",
 ],
 "citations": [CIT_CATCHPOLE, CIT_STD],
 "sig_lens": (
  "Signature reading: birdsong is the original learned communication "
  "protocol — template, practice loop, local dialects, honest "
  "signaling. Manon's Signature take: any signal worth trusting "
  "should be expensive to fake; the dawn chorus is honest because "
  "exhaustion cannot be counterfeited."),
 "demo_kind": "song_learning",
},
# ---- appended compounded entries 18-24 + advanced entries 25-36 ----
{
 "key": "bird-calls", "name": "Calls: The Bird's Everyday Language",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Songs get the glory, but calls do the daily work of bird life. Calls "
  "are the short, simple, usually innate vocalizations birds use for "
  "alarms, contact, begging, aggression, and coordination — distinct "
  "from the long, learned, musical songs of the breeding season. A "
  "chickadee's famous 'chick-a-dee-dee-dee' encodes predator danger: "
  "more 'dee' notes mean a more dangerous predator, a code other "
  "species eavesdrop on. Nuthatches and titmice join mixed-species "
  "flocks that share a common alarm-call network — a forest-wide early "
  "warning system. Flight calls keep migrating flocks together in the "
  "dark; begging calls tell parents which chick is hungriest; mobbing "
  "calls summon a crowd to harass a perched owl until it leaves. "
  "Because calls are largely innate, they evolve slowly and carry deep "
  "evolutionary signal — ornithologists use call structure to sort out "
  "species relationships."),
 "how_it_works": (
  "Calls work as a compact codebook shared by signaler and receiver. "
  "Alarm calls in many songbirds use high, thin, hard-to-locate "
  "frequencies — easy for flockmates to hear, hard for the hawk to "
  "pinpoint — while mobbing calls are broadband and locatable, designed "
  "to recruit: 'come here, there is a predator to harass.' The "
  "chickadee's graded 'dee' system works like an urgency dial: acoustic "
  "analysis shows note number and structure shift continuously with "
  "threat level, and playback experiments prove receivers respond "
  "proportionally. Contact calls maintain cohesion: each bird's call is "
  "individually distinctive enough that mates and flockmates recognize "
  "voices, and flight calls given on the wing keep nocturnal migrants "
  "spaced and oriented. Because the syrinx produces calls with the same "
  "dual-source machinery as song, even simple calls can be surprisingly "
  "rich — parrots embed individual 'names' in contact calls that "
  "flockmates imitate when addressing them."),
 "key_points": [
  "Calls: short, usually innate vocalizations for alarm, contact, begging, coordination",
  "Chickadee 'dee' notes grade with predator danger — a code other species eavesdrop on",
  "Alarm calls are hard to locate (protect the caller); mobbing calls are locatable (recruit help)",
  "Mixed-species flocks share alarm networks — a forest-wide early warning system",
  "Flight calls keep nocturnal migrants together; contact calls carry individual identity",
  "Innate calls evolve slowly — useful for sorting out species relationships",
 ],
 "requirements": [
  "Call-type chart (alarm, mobbing, contact, begging, flight) with spectrograms",
  "Chickadee 'dee'-grading playback results for the coding lesson",
  "A mixed-flock observation session for the eavesdropping lesson",
 ],
 "standards": [
  "Call classification per Catchpole & Slater (2008)",
  "Graded-signal analysis per standard bioacoustics methods",
 ],
 "citations": [CIT_CATCHPOLE, CIT_STD],
 "sig_lens": (
  "Signature reading: calls are the original operations radio net — "
  "short codes, graded urgency, shared across species lines. Manon's "
  "Signature take: separate the broadcast channel (song: 'hear my "
  "quality') from the ops channel (calls: 'act now'); never mix them."),
 "demo_kind": "call_functions",
},
{
 "key": "breeding-systems", "name": "Breeding Systems: Monogamy, Polygyny, Leks, and More",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Birds show every mating system in the vertebrate playbook — and one "
  "stands out: over 90 percent of bird species are socially monogamous, "
  "pairing for a season or for life, a rate unmatched in any other "
  "vertebrate group. Monogamy pays because bird chicks are so demanding: "
  "two parents can feed twice the young. But 'social' monogamy hides "
  "genetic complexity — DNA fingerprinting revealed that many 'faithful' "
  "pairs engage in extra-pair mating, and the chicks in a nest often have "
  "more than one father. Where one parent can raise young alone, other "
  "systems appear: polygyny (one male, several females — common in "
  "marsh-nesting blackbirds), polyandry (one female, several males — "
  "jacanas and phalaropes, where males incubate), and leks, where males "
  "gather to display and females choose, with a few top males winning "
  "most matings (sage-grouse, birds of paradise). Cooperative breeding "
  "adds helpers — grown offspring that stay to raise siblings, as in "
  "Florida scrub-jays and bee-eaters."),
 "how_it_works": (
  "Breeding systems work as economic solutions to the chick-feeding "
  "problem. The logic: if two parents are needed to fledge young, "
  "monogamy wins; if one parent suffices, the freed sex can seek more "
  "mates. In polygynous marsh blackbirds, males defend food-rich "
  "territories and females choose the best real estate, accepting a "
  "shared male for a superior nest site — the polygyny threshold model. "
  "Leks are the extreme: males contribute nothing but sperm and display, "
  "so females choose purely on display quality, and sexual selection runs "
  "riot — a few males get most matings, driving the evolution of "
  "peacock tails and birds-of-paradise dances. Extra-pair mating works "
  "as genetic bet-hedging: the social mate provides the territory and "
  "parental care, while extra-pair sires may provide better genes. "
  "Cooperative breeding works through kin selection: helpers raise "
  "siblings (sharing half their genes) when independent breeding chances "
  "are poor, gaining indirect fitness while waiting for a territory."),
 "key_points": [
  "Over 90% of birds are socially monogamous — unmatched among vertebrates",
  "Monogamy pays when two parents are needed to feed demanding chicks",
  "DNA revealed widespread extra-pair mating inside 'faithful' pairs",
  "Polygyny (blackbirds), polyandry (jacanas), leks (sage-grouse) where one parent suffices",
  "Leks: males give only sperm + display; a few top males win most matings",
  "Cooperative breeding: helpers raise siblings via kin selection (scrub-jays, bee-eaters)",
 ],
 "requirements": [
  "Mating-system comparison chart with example species",
  "Polygyny-threshold model diagram for the economics lesson",
  "DNA-fingerprinting results summary for the extra-pair lesson",
 ],
 "standards": [
  "Mating-system classification per Gill (2007)",
  "Kin-selection framing per standard behavioral-ecology literature",
 ],
 "citations": [CIT_GILL, CIT_STD],
 "sig_lens": (
  "Signature reading: breeding systems are the original resource-allocation "
  "contracts — each one is an economic solution to who feeds the young. "
  "Manon's Signature take: partnerships form around the work that must be "
  "done; when the work needs two, pair up; when it needs one, compete."),
 "demo_kind": "breeding_payoffs",
},
{
 "key": "nests", "name": "Nests: Architecture for Eggs",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "A nest is a life-support structure: it must hold eggs safely, keep "
  "them at incubation temperature, hide them from predators, and "
  "survive weather — built by an animal with no hands, often in days. "
  "The variety is staggering: eagles pile tons of sticks into eyries "
  "reused for decades; weaverbirds knot grass into hanging baskets "
  "with entrance tunnels; ovenbirds bake mud domes; swifts glue "
  "feathers with saliva; megapodes bury eggs in compost mounds and let "
  "microbial heat incubate them — the only birds that outsource "
  "incubation entirely. Cavity nesters (woodpeckers, owls, bluebirds) "
  "let wood do the structural work, excavating or borrowing holes. "
  "Nest placement is a predator-avoidance decision: island colonies, "
  "cliff ledges, thorny bushes, and hanging nests over water all put "
  "distance between eggs and predators. Some birds build decoy nests; "
  "marsh wrens build several and let the female choose."),
 "how_it_works": (
  "A nest works as insulation, cradle, and fortress in one. The cup "
  "shape centers the eggs under the parent's brood patch (a bare, "
  "blood-rich belly patch) for heat transfer; the lining — down, "
  "moss, fur — traps air and slows cooling when the parent leaves to "
  "feed. Structural strength comes from weaving and felting: weaver "
  "strips are knotted with the beak into tension structures, mud "
  "nests harden into compression domes, and stick nests interlock "
  "like log cabins. Drainage matters as much as warmth — a soggy nest "
  "kills chicks with cold, so nests shed water with shaped rims and "
  "porous floors. The megapode mound works as a compost reactor: "
  "decomposing vegetation holds the egg chamber near 33-35 C, and the "
  "male tests the temperature with his beak-tongue and adds or removes "
  "material to regulate it — avian agriculture. Predator defense is "
  "architectural: entrances sized to admit the owner but not the "
  "predator, tunnels that slow snakes, colonies where many eyes watch."),
 "key_points": [
  "A nest is life support: cradle + insulation + fortress, built without hands",
  "Cup shape centers eggs under the brood patch; lining traps air against cooling",
  "Weaving (tension), mud domes (compression), stick piles (interlock) — real structural engineering",
  "Megapodes outsource incubation to compost mounds, regulating temperature like farmers",
  "Placement is predator avoidance: islands, cliffs, thorns, over-water hangs",
  "Drainage is as vital as warmth — a soggy nest kills chicks with cold",
 ],
 "requirements": [
  "Nest-type photo set (cup, cavity, mound, hanging, scrape, platform)",
  "Brood-patch heat-transfer diagram for the insulation lesson",
  "Megapode mound temperature-regulation explanation",
 ],
 "standards": [
  "Nest classification per the Handbook of Bird Biology",
  "Mound-incubation data per megapode literature",
 ],
 "citations": [CIT_HANDBOOK, CIT_STD],
 "sig_lens": (
  "Signature reading: the nest is the original rapid-prototyped "
  "life-support — specified by predators, weather, and thermodynamics, "
  "built in days with a beak. Manon's Signature take: constraints "
  "breed architecture; the weaverbird never had a blueprint, only "
  "physics and predators."),
 "demo_kind": "nest_insulation",
},
{
 "key": "eggs-incubation", "name": "Eggs, Incubation, and Parental Care",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "A bird's egg is a self-contained life-support capsule: shell for "
  "protection and calcium, membranes for plumbing, albumen for water "
  "and protein, yolk for energy — everything a chick needs except "
  "warmth. Egg size follows a famous formula (Hoyt's: volume = 0.51 x "
  "length x breadth squared): a chicken egg holds about 57 cubic "
  "centimeters, an ostrich egg about 1,300 — the largest single cell "
  "in nature. Shell color and pattern are functional: pigments "
  "camouflage ground nests, strengthen thin spots, and in brood "
  "parasites (cuckoos) mimic host eggs. Incubation is precise work: "
  "most birds hold eggs near 36-38 C, turning them regularly so the "
  "embryo does not stick to the shell. After hatching, chicks fall "
  "on a spectrum: precocial chicks (ducks, chickens) hatch downy and "
  "mobile, while altricial chicks (songbirds) hatch blind, naked, and "
  "utterly dependent — the price of growing a big brain fast."),
 "how_it_works": (
  "The egg works as a sealed development chamber with gas exchange. "
  "The shell is calcium carbonate pierced by thousands of pores: "
  "oxygen diffuses in, carbon dioxide and water vapor diffuse out, "
  "and pore number is tuned to the nest humidity — too many pores in "
  "a dry nest desiccates the embryo. The air cell at the blunt end "
  "gives the chick its first breaths before pipping. Incubation "
  "works through the brood patch: the parent sheds belly feathers, "
  "floods the skin with blood, and presses the hot patch to the "
  "eggs, transferring heat by conduction; turning (up to dozens of "
  "times a day) keeps the embryo centered and membranes from "
  "adhering. After hatching, parental care splits by chick type: "
  "precocial parents mostly guard and guide (the chicks feed "
  "themselves), while altricial parents become food-delivery machines "
  "— a songbird pair may make hundreds of feeding trips a day, and "
  "chick begging calls honestly signal hunger because only the "
  "hungriest can afford the loudest begging."),
 "key_points": [
  "The egg: shell + membranes + albumen + yolk — a sealed capsule with pore-tuned gas exchange",
  "Hoyt's formula: volume = 0.51 x length x breadth^2 (chicken ~57 cm^3, ostrich ~1,300 cm^3)",
  "Shell pigments camouflage, strengthen, and (in cuckoos) mimic host eggs",
  "Incubation: brood-patch conduction at 36-38 C + regular turning",
  "Precocial chicks (ducks): downy and mobile; altricial chicks (songbirds): blind, naked, dependent",
  "Begging calls honestly signal hunger — only the hungriest afford the loudest begging",
 ],
 "requirements": [
  "Egg cross-section diagram (shell, membranes, albumen, yolk, air cell)",
  "Hoyt's formula with chicken and ostrich worked examples",
  "Precocial vs altricial chick comparison photos",
 ],
 "standards": [
  "Egg morphometrics per standard oology references",
  "Incubation physiology per the Handbook of Bird Biology",
 ],
 "citations": [CIT_HANDBOOK, CIT_STD],
 "sig_lens": (
  "Signature reading: the egg is the original sealed product — every "
  "dependency included, only warmth and air required. Manon's "
  "Signature take: ship self-contained; the egg needs no supply "
  "chain, only the right environment."),
 "demo_kind": "egg_math",
},
{
 "key": "foraging-ecology", "name": "Foraging Ecology: How Birds Make a Living",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Every bird is a foraging machine, and foraging ecology is the study "
  "of how they earn their energy. The founding idea is optimal foraging "
  "theory: natural selection favors birds that maximize net energy per "
  "unit time, so a bird should prefer the prey with the best energy "
  "payoff after handling time — and ignore poor prey even when hungry, "
  "if searching for better prey pays more. Real birds approximate this "
  "remarkably well: oystercatchers learn to hammer or stab mussels "
  "depending on shell shape, great tits adjust their diet as prey "
  "densities change, and hummingbirds trapline flowers in repeatable "
  "routes like delivery drivers. Foraging shapes everything else: flock "
  "feeding (many eyes spot predators), mixed-species flocks (different "
  "species glean different layers of the forest), tool use (woodpecker "
  "finches probe with cactus spines, herons fish with bait), and even "
  "migration — many migrants are simply following the foraging "
  "calendar across latitudes."),
 "how_it_works": (
  "Foraging works as an economic optimization running on instinct and "
  "learning. The profitability of a prey item is energy divided by "
  "handling time; the bird's decision rule is to take prey in order of "
  "profitability and drop items whose profitability falls below the "
  "average rate of the habitat — the marginal value theorem, which also "
  "predicts when to leave a patch: leave when the patch's return drops "
  "to the habitat average. Birds estimate these rates by sampling: "
  "great tits encountering a new feeder first take small samples, then "
  "commit. Handling skill is learned — young oystercatchers take years "
  "to master mussel-opening, and specialize for life in the technique "
  "they learn first. Social foraging adds information: in a flock, each "
  "bird watches neighbors' success, effectively running a distributed "
  "search algorithm across the habitat. The whole system is testable: "
  "change prey densities in an aviary and the birds' diets shift exactly "
  "as the equations predict."),
 "key_points": [
  "Optimal foraging theory: maximize net energy per unit time",
  "Prey profitability = energy / handling time; take prey in profitability order",
  "Marginal value theorem: leave a patch when its return drops to the habitat average",
  "Handling skill is learned and specialized (oystercatchers: hammer vs stab)",
  "Flocks run distributed search — each bird reads neighbors' success",
  "Foraging economics drive flocking, tool use, and migration timing",
 ],
 "requirements": [
  "Profitability calculation worksheet with prey energy/handling-time data",
  "Marginal-value-theorem patch diagram for the leaving rule",
  "Oystercatcher handling-technique photos for the learning lesson",
 ],
 "standards": [
  "Optimal foraging per standard behavioral-ecology texts",
  "Patch-use models per Charnov's marginal value theorem",
 ],
 "citations": [CIT_GILL, CIT_STD],
 "sig_lens": (
  "Signature reading: foraging is the original resource-optimization "
  "algorithm — rank options by profit, quit losers at the average, "
  "learn the handling tricks. Manon's Signature take: the marginal "
  "value theorem is a universal quit rule; apply it to patches, "
  "projects, and prey alike."),
 "demo_kind": "foraging_profit",
},
{
 "key": "bird-taxonomy", "name": "Avian Taxonomy: The Orders of Birds",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Bird taxonomy organizes 11,000 species into about 40 orders — and DNA "
  "has rewritten the tree in the last two decades. The giant order is "
  "Passeriformes, the perching songbirds: over 6,000 species, more than "
  "half of all birds. Other major orders: Apodiformes (swifts and "
  "hummingbirds), Charadriiformes (shorebirds, gulls, auks), "
  "Accipitriformes (hawks and eagles), Strigiformes (owls), Piciformes "
  "(woodpeckers and toucans), Psittaciformes (parrots), Anseriformes "
  "(ducks and geese), Galliformes (pheasants and chickens), and "
  "Columbiformes (pigeons and doves). DNA surprises abound: falcons are "
  "closer to parrots and songbirds than to hawks; flamingos and grebes "
  "are sisters; hummingbirds evolved from swifts. The deepest split "
  "divides the flightless ratites (ostriches, emus) and tinamous "
  "(Palaeognathae) from all other living birds (Neognathae). Taxonomy "
  "is not stamp collecting — the tree predicts: close relatives share "
  "diseases, behaviors, and conservation needs."),
 "how_it_works": (
  "Modern taxonomy works as a DNA-anchored family tree. Researchers "
  "sequence thousands of genetic markers across species and build "
  "phylogenies — branching diagrams showing who shares the most recent "
  "common ancestor. Orders group families with deep shared ancestry; "
  "the passerine radiation (~6,000 species) is traced to an ancestor "
  "that evolved the perching foot plus the learned-song brain, a "
  "combination that conquered the world's forests. Field identification "
  "uses the same tree in reverse: jizz (overall impression), shape, "
  "behavior, and voice place a bird to family, then plumage details "
  "nail the species. The tree is predictive: knowing a bird is a "
  "charadriiform tells you to expect precocial chicks and long-distance "
  "migration; knowing it is a psittaciform predicts zygodactyl feet and "
  "a hooked bill. Conservation triage uses the tree too — evolutionarily "
  "distinct lineages (like the kagu of New Caledonia) get priority as "
  "irreplaceable branches."),
 "key_points": [
  "~40 orders hold 11,000 species; Passeriformes (songbirds) alone hold 6,000+",
  "DNA rewrote the tree: falcons ally with parrots/songbirds, not hawks",
  "Deepest split: Palaeognathae (ratites + tinamous) vs Neognathae (all other birds)",
  "Phylogenies from thousands of DNA markers show most-recent-common-ancestor relationships",
  "The tree predicts: relatives share diseases, behaviors, conservation needs",
  "Evolutionarily distinct lineages (kagu) get conservation priority as irreplaceable branches",
 ],
 "requirements": [
  "Avian order tree diagram with the major orders labeled",
  "DNA-surprise examples (falcon-parrot, flamingo-grebe) for the revision lesson",
  "Order-to-trait prediction table for the applied lesson",
 ],
 "standards": [
  "Order-level taxonomy per the eBird/Clements checklist",
  "Phylogeny per recent avian genomics literature",
 ],
 "citations": [CIT_GILL, CIT_STD],
 "sig_lens": (
  "Signature reading: the bird tree is the original version-control "
  "history — every branch a release, every split a fork, DNA as the "
  "commit log. Manon's Signature take: when the log contradicts the "
  "labels (falcons vs hawks), trust the log."),
 "demo_kind": "bird_orders",
},
{
 "key": "molt", "name": "Molt: Replacing the Plumage",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Feathers wear out — sun, abrasion, and parasites degrade them — so "
  "birds replace their entire plumage on a schedule called molt, usually "
  "once a year after breeding. Molt is one of the most energetically "
  "expensive things a bird does: growing feathers demands huge protein "
  "synthesis, which is why molt, breeding, and migration are scheduled "
  "to never overlap — a bird cannot afford two of these at once. Flight "
  "feathers are replaced in sequence from the innermost primary outward, "
  "symmetrically on both wings, so the bird never loses the ability to "
  "fly (ducks and geese are the exception: they drop all flight feathers "
  "at once and hide, flightless, for weeks). Ornithologists score molt "
  "by rating each primary 0 (old) to 5 (fully grown) and summing — a "
  "molt score out of 50 that precisely stages a bird's progress. Molt "
  "also delivers the breeding plumage: many birds molt into bright "
  "alternate plumage for courtship, then back into camouflaged basic "
  "plumage for winter."),
 "how_it_works": (
  "Molt works as a scheduled, sequenced replacement program. Hormones "
  "(thyroid, prolactin, sex steroids) triggered by day length initiate "
  "the cycle; each old feather's follicle activates, pushing the new "
  "feather (still sheathed in a waxy pin) out as the old one drops. The "
  "sequence is fixed by evolution: primaries molt descendantly (inner "
  "to outer), secondaries ascendantly, the two sides mirrored — "
  "symmetry preserves balanced flight throughout. Blood quills (growing "
  "feathers with active blood supply) are fragile and painful if "
  "broken, which is why molting birds are secretive. The energy budget "
  "is the master constraint: feather keratin is pure protein, so molt "
  "is scheduled in the food-rich post-breeding window, and stressed or "
  "starving birds suspend molt mid-sequence, leaving a visible fault "
  "line researchers can read like a diary of hardship. The prealternate "
  "molt that produces breeding colors is timed so the bird is at peak "
  "display exactly when mates are choosing."),
 "key_points": [
  "Molt replaces worn plumage, usually annually after breeding",
  "Molt + breeding + migration never overlap — each is too energetically expensive",
  "Primaries replaced inner-to-outer, symmetrically — flight is never lost (except ducks/geese)",
  "Molt scoring: each primary 0-5, summed to a /50 score that stages progress precisely",
  "Stress suspends molt, leaving readable fault lines — a diary of hardship",
  "Prealternate molt delivers breeding plumage timed to mate choice",
 ],
 "requirements": [
  "Spread-wing molt-sequence diagram (primary numbering, descendant order)",
  "Molt-scoring worksheet (0-5 per primary, /50 total)",
  "Annual-cycle chart showing molt/breeding/migration separation",
 ],
 "standards": [
  "Molt terminology (Humphrey-Parkes system) per standard references",
  "Scoring methods per banding-manual conventions",
 ],
 "citations": [CIT_HANDBOOK, CIT_STD],
 "sig_lens": (
  "Signature reading: molt is the original scheduled maintenance "
  "window — sequenced, symmetric, never overlapping production. "
  "Manon's Signature take: plan the downtime before the wear forces "
  "it, replace in order, and never schedule two overhauls at once."),
 "demo_kind": "molt_score",
},
]

# ------------------------------------------------------------------ ADVANCED
_MORE = [
{
 "key": "flight-energy", "name": "The Energy Cost of Flight",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Flapping flight is the most expensive sustained locomotion per unit "
  "time in nature: a flying bird burns energy at roughly 8 to 12 times "
  "its basal metabolic rate — a human equivalent of sprinting for "
  "hours. The power curve is U-shaped: hovering and very slow flight "
  "are costly (huge induced power), there is a sweet spot at moderate "
  "speed where total power is minimized, and costs rise again at high "
  "speed as parasitic drag takes over. Birds pay with fat — the "
  "lightest fuel, packing about 37 kilojoules per gram — and with "
  "protein when fat runs out. A migrating warbler may burn a gram of "
  "fat per hour of flight; a godwit's nonstop Pacific crossing spends "
  "half its body weight. Soaring birds cheat the curve by not flapping: "
  "a vulture's gliding metabolism barely exceeds resting. Understanding "
  "the power curve explains wing shape, migration strategy, and why "
  "only small birds hover — the physics sets hard limits."),
 "how_it_works": (
  "Flight power works as the sum of three costs. Induced power — the "
  "cost of generating lift — dominates at low speed and falls as speed "
  "rises (faster air means less downwash needed). Parasitic power — the "
  "cost of pushing the body through the air — rises with the cube of "
  "speed. Profile power — dragging the wings themselves around — sits "
  "in the middle. Add the three and you get the U-shaped power curve: "
  "minimum power speed (cheapest staying aloft) and maximum range "
  "speed (cheapest per kilometer) are different optima, and birds "
  "choose between them — climbing flocks use minimum power, migrants "
  "use maximum range. Fat is the currency: at 37 kJ/g, a 10-gram "
  "warbler carrying 3 grams of fat holds 111 kJ, and at a flight cost "
  "of ~30 kJ/hour that is under four hours of range — which is why "
  "small migrants hop between stopover sites while godwits, with "
  "enormous fuel fractions, go nonstop. When fat runs out, birds burn "
  "flight muscle itself — arriving migrants are literally lighter in "
  "engine, not just fuel."),
 "key_points": [
  "Flapping flight costs ~8-12x basal metabolic rate — the priciest sustained locomotion",
  "Power curve is U-shaped: induced power dominates slow, parasitic power dominates fast",
  "Minimum-power speed (cheapest aloft) differs from maximum-range speed (cheapest per km)",
  "Fat at ~37 kJ/g is the flight fuel; protein (muscle) burns when fat runs out",
  "Soaring birds cheat: gliding metabolism barely exceeds resting",
  "The power curve explains wing shape, stopover strategy, and why only small birds hover",
 ],
 "requirements": [
  "U-shaped power-curve diagram with the three components labeled",
  "Fat-energy budget worksheet (grams of fat vs hours of flight)",
  "Minimum-power vs maximum-range speed comparison",
 ],
 "standards": [
  "Power-curve modeling per Pennycuick (2008)",
  "Metabolic multiples per standard flight-energetics literature",
 ],
 "citations": [CIT_PENNYCUICK, CIT_STD],
 "sig_lens": (
  "Signature reading: flight economics is the original energy-budget "
  "discipline — three costs, one U-curve, two optima, and a fuel that "
  "weighs. Manon's Signature take: find your U-curve before you "
  "spend; the cheapest speed and the farthest speed are never the "
  "same."),
 "demo_kind": "flight_cost",
},
{
 "key": "high-altitude", "name": "High-Altitude Flight: Thin-Air Physiology",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Bar-headed geese migrate over the Himalayas, crossing passes above "
  "7,000 meters where the air holds less than half its sea-level "
  "oxygen — an environment that would knock a human unconscious in "
  "minutes. Ruppell's griffon vultures have been struck by aircraft "
  "above 11,000 meters. Birds manage this through stacked adaptations: "
  "the cross-current lung extracts far more oxygen per breath than any "
  "mammalian lung; their hemoglobin binds oxygen more tightly "
  "(higher affinity); their capillaries are denser and their hearts "
  "relatively larger; and they hyperventilate without the blood-chemistry "
  "penalty mammals pay. The physics is unforgiving: at 6,000 meters the "
  "oxygen partial pressure is roughly half of sea level's 21 kilopascals, "
  "so every breath carries half the oxygen — the bird must move twice "
  "the air, extract more from it, and deliver it with a heart and "
  "hemoglobin tuned for the thin end of the atmosphere."),
 "how_it_works": (
  "High-altitude flight works by upgrading every step of the oxygen "
  "cascade. Step one, breathing: the unidirectional lung keeps fresh "
  "air flowing over the exchange surface continuously, and the bird "
  "increases ventilation — mammals hyperventilating this hard would "
  "blow off too much CO2 and alkalinize their blood, but birds tolerate "
  "the shift. Step two, pickup: bar-headed goose hemoglobin has amino-acid "
  "changes that raise oxygen affinity, loading up even at low partial "
  "pressures. Step three, delivery: denser muscle capillaries shorten "
  "the diffusion distance to mitochondria, and a relatively larger heart "
  "pumps more blood per beat. Step four, use: flight muscles pack "
  "mitochondria densely. The barometric formula sets the stage — "
  "pressure falls exponentially with altitude — so at 6,000 m the "
  "inspired oxygen pressure is roughly 10 kPa versus 21 at sea level. "
  "The goose's upgrades roughly double extraction efficiency, closing "
  "the gap that physics opens."),
 "key_points": [
  "Bar-headed geese cross the Himalayas above 7,000 m; vultures recorded above 11,000 m",
  "At 6,000 m, oxygen partial pressure is ~half of sea level's 21 kPa",
  "Cross-current lungs extract far more oxygen per breath than mammalian lungs",
  "High-affinity hemoglobin loads oxygen even at low partial pressures",
  "Denser capillaries + larger hearts + dense mitochondria complete the cascade",
  "Birds hyperventilate without the blood-chemistry penalty mammals pay",
 ],
 "requirements": [
  "Barometric-formula altitude vs oxygen-pressure chart",
  "Oxygen-cascade diagram (breathe -> pick up -> deliver -> use)",
  "Bar-headed goose hemoglobin-affinity comparison",
 ],
 "standards": [
  "Altitude physiology per standard avian-physiology literature",
  "Barometric formula per atmospheric-physics conventions",
 ],
 "citations": [CIT_HANDBOOK, CIT_STD],
 "sig_lens": (
  "Signature reading: the high-altitude bird is the original "
  "thin-environment operator — when the resource halves, upgrade "
  "every stage of the pipeline instead of forcing one. Manon's "
  "Signature take: never solve a scarcity at a single point; tune "
  "the whole cascade."),
 "demo_kind": "altitude_oxygen",
},
{
 "key": "magnetic-compass", "name": "The Magnetic Compass: Quantum Navigation",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "The strangest compass in nature may be quantum. Migratory birds "
  "sense the Earth's magnetic field with a precision that lets them "
  "hold migratory headings on cloudy nights — and the leading "
  "hypothesis says the sensor is a quantum-chemical reaction in the "
  "eye. The radical-pair model: blue light excites cryptochrome "
  "proteins in the retina, creating pairs of radicals whose spin "
  "states interconvert at rates sensitive to the magnetic field's "
  "alignment — the bird's visual field would carry a magnetic "
  "modulation, a pattern overlaid on sight. Birds do not read "
  "magnetic north like a compass needle; they read the field's "
  "inclination — the dip angle of field lines, steep near the poles "
  "and flat at the equator — which gives a reliable axis for "
  "'poleward vs equatorward.' Experiments support it: disrupting the "
  "right wavelengths of light disorients migrants, and weak radio "
  "frequencies that should disturb radical pairs do. A second "
  "magnetite-based sensor in the beak may serve the map sense. "
  "Quantum biology, flying at night, in a warbler."),
 "how_it_works": (
  "The radical-pair compass works through spin chemistry. A photon "
  "kicks cryptochrome into forming a radical pair — two molecules "
  "each with an unpaired electron. The pair oscillates between "
  "singlet and triplet spin states, and the oscillation rate depends "
  "on how the external magnetic field aligns with the molecules. "
  "Different alignments yield different chemical products, so the "
  "retina effectively reports field direction as a visual pattern — "
  "the bird may see the magnetic field as a shading across its view. "
  "Because the effect depends on the field's angle relative to the "
  "molecule (not its polarity), the compass reads inclination: field "
  "lines dipping steeply mean 'poleward,' lines running horizontal "
  "mean 'equator.' The inclination angle follows a clean rule with "
  "magnetic latitude (dip angle = arctan(2 x tan(latitude))), so the "
  "same sensor doubles as a latitude gauge. Light-dependence is the "
  "signature prediction: the compass needs specific wavelengths to "
  "form the radical pairs, and shifting the light spectrum shifts or "
  "kills orientation — confirmed in robins and warblers."),
 "key_points": [
  "Leading hypothesis: quantum radical pairs in retinal cryptochrome sense the field",
  "Birds may literally see magnetic information as a pattern overlaid on vision",
  "The compass reads inclination (dip angle), not polarity — poleward vs equatorward",
  "Dip angle = arctan(2 x tan(magnetic latitude)): the sensor doubles as a latitude gauge",
  "Light-wavelength and radio-frequency disruption experiments support the model",
  "A magnetite-based beak sensor may separately serve the map sense",
 ],
 "requirements": [
  "Radical-pair mechanism diagram (photon -> radical pair -> spin-dependent products)",
  "Inclination-angle vs latitude chart",
  "Disruption-experiment summary (light spectrum, radio frequency)",
 ],
 "standards": [
  "Magnetoreception per current quantum-biology literature",
  "Inclination-compass behavior per Wiltschko's experimental tradition",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: the magnetic compass is the original quantum "
  "sensor — single-molecule spin chemistry, in an eye, guiding a "
  "10-gram bird across continents. Manon's Signature take: the "
  "frontier instrument is already flying; study it before reinventing "
  "it."),
 "demo_kind": "magnetic_compass",
},
{
 "key": "population-ecology", "name": "Population Ecology: Banding, Survival, Recruitment",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Ornithology's greatest practical power is counting birds well "
  "enough to know whether populations are rising or falling — and "
  "why. The foundation is bird banding (ringing): over a century of "
  "numbered leg bands has mapped migration routes, measured survival "
  "rates, and revealed longevity records (a Manx shearwater banded as "
  "an adult was still breeding 50+ years later). Population size is "
  "estimated by mark-recapture: band M birds, later catch C birds of "
  "which R are already banded, and the Lincoln-Petersen estimator "
  "says total N = (M x C) / R. Modern analysis goes further — "
  "Cormack-Jolly-Seber models separate survival probability from "
  "recapture probability using years of re-encounter data, telling "
  "managers whether a decline comes from poor adult survival or failed "
  "breeding. This machinery underpins every harvest regulation, every "
  "endangered-species recovery plan, and the discovery that North "
  "America has lost 3 billion birds since 1970."),
 "how_it_works": (
  "Population estimation works by turning recaptures into "
  "probabilities. The Lincoln-Petersen logic: if 200 birds are banded "
  "(M), and a later sample of 150 (C) contains 30 banded birds (R), "
  "then banded birds are 30/150 = 1/5 of the population, so the "
  "population is 5 x 200 = 1,000. The assumptions matter — no "
  "immigration, no band loss, equal catchability — and violations "
  "bias the answer, which is why modern studies use robust designs "
  "with multiple occasions. Survival analysis works on encounter "
  "histories: a bird seen in years 1, 3, and 4 but not 2 was alive "
  "in year 2 (it was simply missed), and across thousands of such "
  "histories the models estimate annual survival vs. detection "
  "separately. Recruitment (young entering the population) comes from "
  "age ratios in catches. Managers combine survival, recruitment, "
  "and counts into population models that test interventions before "
  "spending: will predator control, habitat work, or harvest limits "
  "move the needle? The models answer first."),
 "key_points": [
  "A century of banding mapped migrations, measured survival, set longevity records (shearwater 50+ yrs)",
  "Lincoln-Petersen estimator: N = (M x C) / R from marked/recaptured samples",
  "Cormack-Jolly-Seber models separate survival probability from recapture probability",
  "Encounter histories let analysts distinguish 'dead' from 'alive but missed'",
  "Survival + recruitment + counts feed models that test interventions before spending",
  "This machinery revealed North America's 3-billion-bird loss since 1970",
 ],
 "requirements": [
  "Lincoln-Petersen worked example with assumption checks",
  "Encounter-history table showing alive-but-missed logic",
  "Banding-data workflow: capture -> band -> release -> re-encounter",
 ],
 "standards": [
  "Mark-recapture per Sutherland, Newton & Green (2004)",
  "Banding protocols per national banding-office manuals",
 ],
 "citations": [CIT_SUTHERLAND, CIT_STD],
 "sig_lens": (
  "Signature reading: banding is the original longitudinal tracking "
  "system — mark once, re-encounter for decades, separate signal "
  "from detection noise. Manon's Signature take: never confuse 'not "
  "seen' with 'gone'; model the detection process itself."),
 "demo_kind": "banding_stats",
},
{
 "key": "conservation", "name": "Conservation Ornithology: Declines and Recoveries",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Birds are the best-measured barometer of biodiversity, and the "
  "reading is alarming: North America has lost nearly 3 billion "
  "breeding birds since 1970 — about 29 percent — including familiar "
  "species like meadowlarks and swallows, not just rarities. Europe's "
  "farmland birds fell by more than half. The drivers are well "
  "documented: habitat loss and fragmentation, agricultural "
  "intensification (pesticides removing insect food), cats (billions "
  "of kills yearly), window collisions (hundreds of millions), and "
  "climate disruption. But ornithology also wrote the recovery "
  "manual: the bald eagle rebounded from DDT-era collapse after the "
  "pesticide ban; the peregrine falcon was rebuilt by captive "
  "breeding and reintroduction; California condors were pulled back "
  "from 27 individuals. The pattern is consistent — diagnose the "
  "limiting factor with population models, remove it, and birds "
  "rebound with astonishing speed because high fecundity is their "
  "superpower."),
 "how_it_works": (
  "Conservation ornithology works as diagnose-then-treat at population "
  "scale. Step one is trend detection: long-term surveys (Breeding "
  "Bird Survey, Christmas Bird Count, European schemes) feed "
  "hierarchical models that estimate true trends beneath noisy "
  "counts — this is how the 3-billion loss was quantified from "
  "decades of data. Step two is limiting-factor diagnosis: is the "
  "decline driven by adult survival (wintering-ground problem), "
  "breeding failure (nest predators, pesticides), or recruitment "
  "(habitat loss)? Banding recoveries, nest monitoring, and tracking "
  "pinpoint the life stage and the place. Step three is targeted "
  "action: pesticide bans (eagles), captive breeding (condors, "
  "peregrines), predator control on islands (seabirds), habitat "
  "easements (grassland birds). Step four is monitoring the response "
  "— the same surveys that found the decline verify the recovery. "
  "Island eradications of invasive rats show the method's power: "
  "seabird colonies rebound within years of rat removal."),
 "key_points": [
  "North America lost ~3 billion birds (~29%) since 1970; Europe's farmland birds fell by half+",
  "Drivers: habitat loss, agricultural intensification, cats, windows, climate disruption",
  "Trend detection via decades-long surveys + hierarchical models beneath noisy counts",
  "Limiting-factor diagnosis: which life stage, which place — via banding, nests, tracking",
  "Recoveries prove the method: eagles (DDT ban), peregrines (captive breeding), condors (27 to 500+)",
  "Island rat eradications rebound seabird colonies within years",
 ],
 "requirements": [
  "The 3-billion-loss study summary (Rosenberg et al. 2019) for the scale lesson",
  "Driver-ranking chart (habitat, cats, windows, pesticides, climate)",
  "Recovery case timelines (eagle, peregrine, condor) for the hope lesson",
 ],
 "standards": [
  "Trend analysis per standard survey-methodology literature",
  "Recovery planning per IUCN species-action conventions",
 ],
 "citations": [CIT_SUTHERLAND, CIT_STD],
 "sig_lens": (
  "Signature reading: conservation ornithology is the original "
  "closed-loop control on a living system — measure, diagnose, "
  "intervene, verify. Manon's Signature take: the birds prove that "
  "measured decline is reversible decline; despair is what happens "
  "before the diagnosis."),
 "demo_kind": "decline_stats",
},
{
 "key": "climate-birds", "name": "Climate Change and Birds",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Birds are documenting climate change in real time. Ranges are "
  "shifting poleward and uphill — North American birds moved north "
  "an average of tens of kilometers in recent decades, and montane "
  "species are being squeezed toward summits with nowhere higher to "
  "go. Timing is shifting too: egg-laying advances roughly 2 days "
  "per decade in many species as springs warm. The danger is "
  "phenological mismatch — the food peak moves faster than the bird: "
  "Dutch pied flycatchers now arrive after the caterpillar peak their "
  "chicks depend on, because the caterpillars track temperature while "
  "the birds' migration is cued by day length, which does not change. "
  "Seabirds face ocean warming that redistributes the fish they dive "
  "for; Arctic breeders lose the tundra itself as shrubs advance. "
  "Ornithology's century of records makes birds the sharpest "
  "early-warning system for climate impacts on wildlife."),
 "how_it_works": (
  "Climate impacts work through cues, ranges, and mismatches. Range "
  "shifts follow the climate envelope: as isotherms move poleward "
  "(roughly 1-2 km per year in many regions), bird distributions "
  "track them — but only where habitat corridors allow, which is why "
  "fragmentation turns a shift into a trap. Phenology shifts follow "
  "temperature: insects and plants respond directly to warmth, "
  "advancing fast, while long-distance migrants time departure by "
  "day length at their tropical wintering grounds — a cue that never "
  "changes — so they arrive at a spring that has already peaked. "
  "Mismatch is measured by comparing long-term datasets: caterpillar "
  "peak dates vs. flycatcher laying dates, year by year, and the gap "
  "widens as warming accelerates. Montane squeeze is geometric: a "
  "species moving uphill loses habitat area with every meter (mountains "
  "narrow toward the top) until the summit population blinks out. "
  "Models project future ranges by mapping the climate envelope onto "
  "tomorrow's geography — and the maps say many current ranges will "
  "simply cease to exist."),
 "key_points": [
  "Ranges shift poleward/uphill tracking isotherms (~1-2 km/yr); fragmentation turns shifts into traps",
  "Egg-laying advances ~2 days per decade as springs warm",
  "Phenological mismatch: food peaks move faster than day-length-cued migrants (pied flycatcher vs caterpillars)",
  "Montane squeeze: uphill movement loses habitat area geometrically toward summits",
  "Seabirds track warming-driven fish redistributions; Arctic breeders lose tundra to shrubs",
  "A century of bird records makes ornithology the sharpest climate early-warning system",
 ],
 "requirements": [
  "Range-shift map example (poleward movement over decades)",
  "Mismatch diagram: caterpillar peak vs flycatcher laying dates diverging",
  "Montane-squeeze geometry sketch for the area-loss lesson",
 ],
 "standards": [
  "Phenology analysis per standard long-term-study methods",
  "Range modeling per climate-envelope conventions",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: birds are the original distributed sensor "
  "network for climate — millions of observers, a century of "
  "records, no batteries required. Manon's Signature take: when the "
  "cues disagree (temperature vs day length), the system breaks at "
  "the mismatch; design for cue agreement."),
 "demo_kind": "range_shift",
},
{
 "key": "field-methods", "name": "Field Methods: Counts, Transects, and Mist Nets",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Ornithology runs on standardized field methods — the protocols "
  "that turn birdwatching into data. Point counts: stand at a fixed "
  "point for a set time (often 5-10 minutes), record every bird seen "
  "or heard within a fixed radius, and convert to density using the "
  "surveyed area and an estimated detection probability. Transects: "
  "walk a line at steady pace recording birds by distance band, which "
  "lets analysts model how detectability falls with distance. Mist "
  "netting: fine nets that safely catch birds for banding, measuring, "
  "and release — the source of survival data, molt scores, and "
  "physiological samples. Territory mapping: visit a plot repeatedly "
  "through the season and cluster singing locations into territories. "
  "The discipline is standardization: same points, same dates, same "
  "effort, year after year — because only strictly comparable counts "
  "reveal true trends beneath the noise of weather, observers, and "
  "luck."),
 "how_it_works": (
  "Each method works by controlling effort so counts become "
  "comparable. Point-count density: count n birds within radius r, "
  "divide by the circle area (pi x r^2), then divide by detection "
  "probability p (the fraction of birds present that are actually "
  "detected) — D = n / (pi r^2 p). If p is ignored, shy species look "
  "rarer than they are; distance sampling estimates p from how "
  "detections fall off with distance. Mist nets work as passive "
  "traps: birds fly into nearly invisible mesh and slide into pockets; "
  "captures per net-hour standardize effort across sites and days. "
  "Banding adds the individual: weight, wing length, fat score, molt, "
  "age, and sex turn a count into a demographic sample. Territory "
  "mapping works by triangulation of behavior: eight visits across "
  "the season, singing males plotted each time, clusters of "
  "registrations marking territory centers. All methods share the "
  "rule: record effort (minutes, net-hours, kilometers) alongside "
  "birds, or the numbers mean nothing."),
 "key_points": [
  "Point counts: fixed point + fixed time + fixed radius -> density via D = n / (pi r^2 p)",
  "Detection probability p corrects for missed birds; distance sampling estimates it",
  "Transects model detectability falloff with distance from the walked line",
  "Mist nets: captures per net-hour standardize effort; banding adds demographics",
  "Territory mapping clusters repeated singing locations into territories",
  "Golden rule: record effort (minutes, net-hours, km) alongside birds — or numbers mean nothing",
 ],
 "requirements": [
  "Point-count protocol sheet (radius, duration, recording rules)",
  "Mist-net setup and safe-extraction procedure",
  "Effort-recording template (the standardization lesson)",
 ],
 "standards": [
  "Survey protocols per Sutherland, Newton & Green (2004)",
  "Banding methods per national banding-office manuals",
 ],
 "citations": [CIT_SUTHERLAND, CIT_STD],
 "sig_lens": (
  "Signature reading: field methods are the original measurement "
  "discipline — standardize the effort, correct the detection, and "
  "the noise becomes signal. Manon's Signature take: unstandardized "
  "counting is storytelling; standardized counting is science."),
 "demo_kind": "point_count",
},
{
 "key": "bioacoustics", "name": "Bioacoustics: Recording and Analyzing Birdsong",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Bioacoustics turns birdsong into data you can measure, compare, "
  "and archive. The core tool is the spectrogram — a picture of sound "
  "with time on one axis and frequency on the other, computed by "
  "slicing the recording into short windows and running a Fourier "
  "transform on each (the same math behind music visualizers). On a "
  "spectrogram, a song becomes a readable signature: upsweeps, "
  "downsweeps, trills, and buzzes each draw a distinct shape, and "
  "individual birds, dialects, and species can be told apart by eye "
  "once you learn the alphabet. Modern autonomous recorders capture "
  "months of sound unattended; machine-learning classifiers now scan "
  "thousands of hours and flag species detections. Playback experiments "
  "close the loop: play a recorded song to a territorial male and "
  "measure his response to test what the song means. Archives of "
  "millions of recordings preserve voices of populations — and "
  "species — that no longer exist."),
 "how_it_works": (
  "Analysis works as signal processing plus pattern matching. "
  "Recording: a directional microphone and recorder capture sound at "
  "44,100 samples per second (enough for the full bird hearing range, "
  "roughly up to 10-15 kHz for most songbirds). Spectrogram: each "
  "short window (a few milliseconds) is Fourier-transformed to find "
  "which frequencies are present, and the windows are stacked into the "
  "time-frequency image. Measurement: software traces the pitch "
  "contour, measures syllable durations, intervals, frequency range, "
  "and entropy (disorder) — numbers that distinguish individuals and "
  "dialects objectively. Classification: template matching or neural "
  "networks compare new recordings against libraries, enabling "
  "continent-scale monitoring from autonomous units. Playback "
  "experiments test function: degrade the recording (remove trills, "
  "shift pitch) and see which features the birds respond to — "
  "revealing which parts of the song carry the message."),
 "key_points": [
  "Spectrogram = time vs frequency image via windowed Fourier transforms",
  "Song elements (upsweeps, trills, buzzes) draw distinct readable shapes",
  "Measurements: pitch contour, syllable timing, frequency range, entropy",
  "Autonomous recorders + ML classifiers enable continent-scale acoustic monitoring",
  "Playback experiments test function by degrading features and measuring response",
  "Recording archives preserve voices of vanished populations and extinct species",
 ],
 "requirements": [
  "Spectrogram examples of 3-4 distinct song shapes",
  "A short recording (or synthetic chirp) to Fourier-analyze",
  "Playback-experiment design template for the function lesson",
 ],
 "standards": [
  "Recording standards per the Macaulay Library conventions",
  "Analysis methods per standard bioacoustics references",
 ],
 "citations": [CIT_CATCHPOLE, CIT_STD],
 "sig_lens": (
  "Signature reading: bioacoustics is the original signal-intelligence "
  "pipeline — capture, transform, measure, classify, test. Manon's "
  "Signature take: any sound worth studying is worth picturing; the "
  "spectrogram turns hearing into seeing."),
 "demo_kind": "spectrogram_dft",
},
{
 "key": "avian-cognition", "name": "Avian Cognition: Tool Use, Memory, and Problem Solving",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Birds are far smarter than their small brains suggest — because "
  "avian brains are built differently: densely packed neurons give a "
  "parrot or crow the neuron count of a small primate in a walnut-sized "
  "package. New Caledonian crows manufacture hooked tools from "
  "pandanus leaves and save their favorite tools for reuse; rooks drop "
  "stones into tubes to raise water levels (the Aesop's fable test, "
  "passed); woodpecker finches probe with cactus spines. Clark's "
  "nutcrackers cache up to 30,000 pine seeds across a mountainside in "
  "autumn and recover roughly two-thirds months later under snow — a "
  "spatial memory feat few mammals match. Scrub-jays remember what "
  "food they cached, where, and when — episodic-like memory — and "
  "re-cache if they were watched, showing they model what others know. "
  "Pigeons categorize images, parrots learn labels and count, and crows "
  "hold grudges against individual humans for years. Bird intelligence "
  "evolved independently from ours — a second, parallel experiment in "
  "building a mind."),
 "how_it_works": (
  "Avian cognition works on dense, differently-wired hardware. Birds "
  "lack the layered neocortex mammals use; instead the pallium packs "
  "neurons at far higher density, and corvids and parrots carry "
  "primate-scale neuron counts. Tool manufacture works through "
  "causal understanding plus practice: New Caledonian crows shape "
  "hooks with a precision that improves with experience, and lab tests "
  "show they select tools by length and diameter for the task — not "
  "trial and error alone. Nutcracker caching works as spatial memory "
  "at scale: each cache site is encoded relative to landmarks, and "
  "recovery experiments (with landmarks shifted) prove the birds use "
  "true spatial maps, not smell. Scrub-jay re-caching works as "
  "perspective-taking: jays that have stolen others' caches re-cache "
  "their own when watched — they apply their thief's knowledge to "
  "predict another's behavior. The independent evolution matters: "
  "convergent smarts in crows and apes reveal which cognitive designs "
  "are universal, not accidents of mammalian history."),
 "key_points": [
  "Dense pallium neurons give corvids/parrots primate-scale counts in walnut-sized brains",
  "New Caledonian crows manufacture and curate hooked tools; rooks pass the Aesop's fable test",
  "Clark's nutcrackers cache ~30,000 seeds and recover two-thirds months later under snow",
  "Scrub-jays show episodic-like memory (what/where/when) and re-cache when watched",
  "Crows recognize and remember individual humans for years",
  "Bird minds evolved independently — a parallel experiment in building intelligence",
 ],
 "requirements": [
  "Tool-use case gallery (crow hooks, finch spines, rook stones)",
  "Nutcracker cache-recovery experiment summary",
  "Scrub-jay re-caching study summary for the perspective-taking lesson",
 ],
 "standards": [
  "Cognition studies per standard comparative-psychology literature",
  "Neuron-density data per current avian-neuroanatomy research",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: the crow is the original proof that there are "
  "many hardware paths to a mind — density over volume, pallium over "
  "cortex. Manon's Signature take: never mistake size for capacity; "
  "count the neurons, not the skull."),
 "demo_kind": "nutcracker_memory",
},
{
 "key": "speciation", "name": "Speciation in Birds: How New Species Arise",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Birds wrote the textbook on speciation — literally, in Darwin's "
  "finches. New bird species arise when populations stop exchanging "
  "genes and diverge: most often by geographic isolation (a mountain "
  "range, a sea gap, a habitat split), then by the slow accumulation "
  "of differences in plumage, song, beak, and genetics. Song is a "
  "powerful speciation engine: when learned songs drift apart, "
  "females no longer recognize foreign males' songs, and reproductive "
  "isolation follows — behavior first, genes later. Ring species show "
  "speciation in progress: greenish warblers ringed around the "
  "Himalayas interbreed neighbor-to-neighbor all the way around, but "
  "the two end populations meeting in Siberia behave as separate "
  "species. Genomic studies now catch speciation red-handed: hybrid "
  "zones where genomes mix at the edges, 'islands of divergence' "
  "where selection resists mixing, and cases of hybrid speciation "
  "where two species' genomes fuse into a third (as in a Galapagos "
  "finch lineage observed forming within decades)."),
 "how_it_works": (
  "Speciation works as divergence plus isolation, measurable with a "
  "reproductive-isolation index: RI = 1 - (hybrid fitness / parental "
  "fitness), running from 0 (free interbreeding) to 1 (complete "
  "isolation). The stages: first, populations separate (geography, "
  "habitat, or timing); second, differences accumulate — song drifts "
  "fastest because it is learned, plumage follows under sexual "
  "selection, genes slowest; third, when they meet again, prezygotic "
  "barriers (song, courtship, timing) or postzygotic barriers (hybrid "
  "sterility, like mules) keep them apart. Reinforcement sharpens the "
  "split: where hybrids do poorly, selection favors ever-stronger "
  "mate discrimination. Ring species work as a geographic proof: gene "
  "flow connects the ring, but distance accumulates differences until "
  "the ends cannot communicate — speciation as a continuous variable, "
  "caught mid-act. Conservation relevance is direct: hybridizing "
  "populations (golden-winged vs blue-winged warblers) force hard "
  "decisions about what a species is."),
 "key_points": [
  "Speciation = populations stop exchanging genes and diverge (usually via geographic isolation)",
  "Learned song drift is a fast speciation engine: females stop recognizing foreign songs",
  "Reproductive isolation index: RI = 1 - (hybrid fitness / parental fitness), 0 to 1",
  "Ring species (greenish warblers): interbreeding around the ring, separate species at the ends",
  "Genomics catches speciation red-handed: hybrid zones, islands of divergence, hybrid speciation",
  "Darwin's finches remain the living laboratory — new hybrid lineages observed forming",
 ],
 "requirements": [
  "Greenish warbler ring-species map for the in-progress lesson",
  "RI calculation worksheet with hybrid-fitness data",
  "Darwin's finch radiation tree for the classic lesson",
 ],
 "standards": [
  "Speciation concepts per Gill (2007)",
  "Genomic methods per current speciation literature",
 ],
 "citations": [CIT_GILL, CIT_STD],
 "sig_lens": (
  "Signature reading: speciation is the original forking protocol — "
  "isolate, diverge, test compatibility on merge. Manon's Signature "
  "take: the ring species proves speciation is a gradient, not a "
  "switch; version your branches before they stop merging."),
 "demo_kind": "speciation_index",
},
{
 "key": "avian-epidemiology", "name": "Avian Disease Ecology: Bird Flu and Beyond",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Birds are the original global disease network: billions of migrants "
  "connect every continent twice a year, carrying their microbes with "
  "them. Wild waterfowl are the natural reservoir of avian influenza "
  "viruses — low-pathogenic strains circulate harmlessly in ducks, but "
  "in dense poultry the virus can evolve into highly pathogenic forms "
  "(H5N1 and relatives) that kill both birds and, rarely, mammals. "
  "The 2020s panzootic of H5N1 clade 2.3.4.4b killed millions of wild "
  "birds across every continent including Antarctica, plus seal and sea "
  "lion die-offs — the largest wildlife disease event ever recorded. "
  "Other avian diseases shape populations too: avian malaria "
  "(Plasmodium) transmitted by mosquitoes devastated Hawaii's "
  "honeycreepers, which evolved with no exposure; West Nile virus "
  "swept North American crows and jays after 1999; trichomonosis "
  "crashes finch populations at garden feeders. Disease ecology models "
  "all of this with the same R0 math as human epidemiology: if each "
  "infection causes more than one new infection, it spreads."),
 "how_it_works": (
  "Avian disease dynamics work through the same SIR logic as human "
  "epidemics, with migration as the coupling. R0 — the basic "
  "reproduction number — is transmission rate x susceptible population "
  "divided by recovery rate: in a dense duck flock with a fast-spreading "
  "strain, R0 climbs well above 1 and the virus sweeps through. "
  "Migration spreads it spatially: stopover wetlands mix flocks from "
  "different flyways, the avian equivalent of international airports "
  "during flu season. Virulence evolves with transmission mode: "
  "waterborne fecal-oral spread (the duck way) lets even deadly strains "
  "transmit, because the host does not need to stay mobile — unlike "
  "respiratory viruses that need a walking host. Surveillance works "
  "through dead-bird reporting, hunter-harvested sampling, and "
  "satellite-tracked migrants: when H5N1 moves, ornithologists see it "
  "in wild-bird mortality before poultry outbreaks. Control is "
  "ecological: biosecurity at the wild-domestic interface, wetland "
  "management to reduce crowding, and in Hawaii, mosquito control to "
  "shield the last honeycreepers."),
 "key_points": [
  "Wild waterfowl are the natural reservoir of avian influenza viruses",
  "H5N1 clade 2.3.4.4b panzootic: millions of wild birds dead on every continent, largest wildlife disease event recorded",
  "R0 = transmission x susceptibles / recovery — above 1, it spreads (same math as human epidemics)",
  "Stopover wetlands mix flyways like airports mix travelers",
  "Avian malaria devastated Hawaii's honeycreepers; West Nile swept crows and jays after 1999",
  "Surveillance: dead-bird reporting + harvest sampling + tracked migrants give early warning",
 ],
 "requirements": [
  "R0 calculation worksheet for a waterfowl flock scenario",
  "Flyway-mixing diagram (stopover wetlands as transmission hubs)",
  "H5N1 panzootic timeline for the scale lesson",
 ],
 "standards": [
  "Disease ecology per standard wildlife-epidemiology literature",
  "Surveillance protocols per international animal-health conventions",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: the flyway is the original global network — "
  "and every network carries packets and pathogens alike. Manon's "
  "Signature take: monitor the hubs (wetlands), model the R0, and "
  "never forget the reservoir hosts that feel nothing."),
 "demo_kind": "avian_flu_r0",
},
{
 "key": "conservation-genetics", "name": "Conservation Genetics: Reading Feathers for DNA",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A single molted feather holds a bird's genome — and conservation "
  "genetics reads it without ever touching the bird. DNA from feathers, "
  "eggshells, and droppings lets researchers census elusive species, "
  "assign seized parrots to wild populations, and prove which "
  "population a migrant came from. The core danger it measures is the "
  "bottleneck: when a population crashes to a handful of individuals, "
  "genetic diversity drains each generation by roughly 1/(2 x effective "
  "population size) — heterozygosity decays as Ht = H0 x (1 - 1/(2Ne))^t. "
  "A population of 10 effective breeders loses about 5 percent of its "
  "remaining diversity every generation; after 10 generations nearly "
  "40 percent is gone, along with disease resistance and adaptability. "
  "Famous rescues ran on genetics: the Mauritius kestrel rebuilt from "
  "a handful of birds, the California condor's studbook managed to "
  "minimize inbreeding from 27 founders. Environmental DNA (eDNA) now "
  "detects secretive marsh birds from water samples — conservation "
  "without capture."),
 "how_it_works": (
  "Conservation genetics works as diversity accounting plus "
  "forensics. Sampling: a feather's calamus (quill base) holds enough "
  "cells for microsatellite or SNP genotyping; non-invasive sampling "
  "means endangered birds are never stressed. Bottleneck math: each "
  "generation, drift removes a fraction 1/(2Ne) of heterozygosity — "
  "small Ne means fast erosion, and the loss compounds "
  "multiplicatively, so the first generations after a crash matter "
  "most. Inbreeding depression is the mechanism: harmful recessive "
  "alleles, normally masked, meet in homozygous offspring and cut "
  "fertility and survival. Management fights back with studbooks: "
  "pairing the least-related founders (minimum-kinship mating) slows "
  "the loss, and genetic rescue — introducing individuals from "
  "another population — can restore diversity in one generation "
  "(Florida panthers are the textbook mammal case; songbird "
  "translocations show it in birds). Assignment tests use allele "
  "frequencies to trace a feather, a carcass, or a trafficked chick "
  "back to its source population — DNA as a passport stamp."),
 "key_points": [
  "Feathers, eggshells, droppings yield DNA — conservation without capture",
  "Bottleneck decay: Ht = H0 x (1 - 1/(2Ne))^t — small populations bleed diversity fast",
  "Ne=10 loses ~5%/generation; ~40% gone after 10 generations",
  "Inbreeding depression: harmful recessives meet in homozygous offspring",
  "Studbooks + minimum-kinship mating slow the loss; genetic rescue can restore it",
  "Assignment tests trace feathers and trafficked birds to source populations",
 ],
 "requirements": [
  "Bottleneck-decay curve worksheet (vary Ne and t)",
  "Non-invasive sampling protocol (feather calamus collection)",
  "Studbook minimum-kinship pairing explanation",
 ],
 "standards": [
  "Population-genetics methods per standard conservation-genetics texts",
  "Sampling ethics per non-invasive genetics conventions",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: the feather is the original backup medium — "
  "the whole genome, shed freely, readable without touching the "
  "bird. Manon's Signature take: diversity is the system's error "
  "budget; the bottleneck equation tells you exactly how fast you "
  "are spending it."),
 "demo_kind": "bottleneck_heterozygosity",
},
]
ENTRIES.extend(_MORE)
