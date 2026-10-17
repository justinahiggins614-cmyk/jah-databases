#!/usr/bin/env python3
"""Seed entries for the Entomology field build (field #5, taxonomy order).

Verified 2026-10-17: the manifest holds no dedicated entomology database —
only 'inventors' matched an "ento" substring search, and the biology-family
databases (microbiology, biology-study, biology, everything-biology, ...)
carry only incidental insect coverage. So this build creates two NEW
databases:

  entomology              — The Entomology Database (public-harvest: real,
                            fact-checked entomology — insect anatomy and
                            morphology, insect orders and taxonomy,
                            metamorphosis, insect physiology, behavior and
                            social insects, pollination ecology,
                            agricultural and medical entomology, pest
                            management, beneficial insects, collection and
                            identification methods)
  entomology-signature    — The Entomology Signature Database (his original
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

# Shared citation constants (standard entomology literature)
CIT_GULLAN = ("Gullan, P. J. & Cranston, P. S. (2014). 'The Insects: An "
              "Outline of Entomology', 5th ed. Wiley-Blackwell.")
CIT_CHAPMAN = ("Chapman, R. F. (2013). 'The Insects: Structure and Function', "
               "5th ed. Cambridge University Press.")
CIT_TRIPLEHORN = ("Triplehorn, C. A. & Johnson, N. F. (2005). 'Borror and "
                  "DeLong's Introduction to the Study of Insects', 7th ed. "
                  "Thomson Brooks/Cole.")
CIT_PEDIGO = ("Pedigo, L. P. & Rice, M. E. (2014). 'Entomology and Pest "
              "Management', 6th ed. Waveland Press.")
CIT_RESH = ("Resh, V. H. & Cardé, R. T. (2009). 'Encyclopedia of Insects', "
            "2nd ed. Academic Press.")
CIT_NORRIS = ("Klowden, M. J. (2013). 'Physiological Systems in Insects', "
              "3rd ed. Academic Press.")
CIT_GODFRAY = ("Godfray, H. C. J. (1994). 'Parasitoids: Behavioral and "
               "Evolutionary Ecology'. Princeton University Press.")
CIT_STD = "Standard entomology literature (peer-reviewed textbooks and journals)."
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "entomology, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-insect", "name": "What Is an Insect: The Six-Legged Kingdom",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Insects are six-legged arthropods forming the class Insecta — the most "
  "diverse and abundant group of animals on Earth. Roughly 1 million insect "
  "species have been formally described, and estimates of the true total "
  "range from 5.5 to 10 million, meaning the vast majority of insects "
  "remain unknown to science. Insects make up about three quarters of all "
  "described animal species, and at any moment the living biomass of "
  "insects outweighs that of all vertebrates combined — a single estimate "
  "puts the number of individual insects alive at about 10 quintillion "
  "(10^19). Every insect shares the same body plan: three tagmata (head, "
  "thorax, abdomen), three pairs of walking legs attached to the thorax, "
  "one pair of antennae, and usually one or two pairs of wings in the "
  "adult. They arose around 480 million years ago and were the first "
  "animals to fly, some 100 million years before birds. Insects pollinate "
  "most flowering plants, recycle nutrients, feed nearly every land "
  "predator, and shape human agriculture, health, and industry."),
 "how_it_works": (
  "An insect works as a compact, armored, six-legged machine. The body is "
  "divided into three fused functional units called tagmata: the head "
  "carries the sensors (eyes, antennae) and mouthparts; the thorax carries "
  "all three pairs of legs and usually the wings, packed with the flight "
  "muscles that power movement; the abdomen holds the digestive, "
  "reproductive, and most respiratory organs. A rigid exoskeleton of chitin "
  "and protein protects the body and anchors the muscles, but because it "
  "cannot stretch, the insect must periodically shed it in a process called "
  "molting (ecdysis) to grow. Oxygen reaches tissues directly through a "
  "network of air tubes called tracheae that open at pores (spiracles) "
  "along the body — no lungs needed. Instead of red blood cells, insects "
  "circulate hemolymph, a greenish fluid that carries nutrients, hormones, "
  "and immune cells but carries little oxygen. Growth happens in steps: "
  "each molt brings a larger instar, and the transformation between life "
  "stages — metamorphosis — lets one species live in two or three "
  "completely different ecological roles during its lifetime."),
 "key_points": [
  "Class Insecta: 3 tagmata, 3 pairs of legs, 1 pair of antennae, usually winged adults",
  "About 1 million species described; 5.5-10 million estimated — the dominant animal group",
  "Exoskeleton of chitin requires molting (ecdysis) for growth",
  "Tracheal breathing delivers oxygen directly to tissues through spiracles",
  "First animals to fly (~480 million years of evolution; flight ~400 million years ago)",
  "Pollinators, decomposers, prey base, pests — insects run the terrestrial food web",
 ],
 "requirements": [
  "A hand lens or microscope to see tagmata, legs, and antennae",
  "Reference specimens or photos showing the three body regions",
  "Ability to count legs (6), antennae pairs (1), and wing pairs (0-2)",
 ],
 "standards": [
  "Classification follows Triplehorn & Johnson's ordinal system",
  "Species counts per Stork et al. (2015) global estimate methods",
 ],
 "citations": [CIT_GULLAN, CIT_TRIPLEHORN],
 "sig_lens": (
  "Signature reading: the insect is the original modular machine — three "
  "fused modules, six standardized legs, plug-in sensors on the head, and "
  "an armor shell that gets swapped out to upgrade the frame. Manon's "
  "Signature take treats tagmosis as the master lesson in modular "
  "engineering: specialize each module, standardize the interfaces."),
 "demo_kind": "insect_diversity",
},
{
 "key": "insect-anatomy", "name": "Insect Anatomy I: Head, Thorax, Abdomen",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Every insect body is organized into three tagmata — fused groups of "
  "segments with distinct jobs. The head is the sensory and feeding "
  "module: it carries the compound eyes, the ocelli (simple eyes), one "
  "pair of antennae, and the mouthparts, all wired to the brain "
  "(supraesophageal ganglion). The thorax is the locomotion module, made "
  "of three segments (prothorax, mesothorax, metathorax), each bearing one "
  "pair of jointed legs; the mesothorax and metathorax usually each bear "
  "one pair of wings. It is packed with flight and leg muscles — the "
  "densest muscle concentration in the animal kingdom. The abdomen is the "
  "visceral module: up to 11 segments housing the gut, the reproductive "
  "system, the heart (dorsal vessel), and most of the tracheal air tubes; "
  "in many species it also carries the ovipositor, stinger, or sound "
  "organs. The three-tagma plan is the quickest field identification "
  "check: if it does not have head-thorax-abdomen plus six thoracic legs, "
  "it is not an insect — spiders have two body parts and eight legs, "
  "millipedes have dozens of segments."),
 "how_it_works": (
  "Tagmosis works by fusing ancestral segments into task-specific modules. "
  "In the head, appendages were converted into mouthparts and antennae, "
  "and the brain fused from several segment ganglia. In the thorax, the "
  "three leg-bearing segments fused into a rigid box that can withstand "
  "the enormous forces of flight — flight muscles deform the thorax "
  "itself, and the wings hinge on the deformation, beating up to 1,000 "
  "times per second in some midges. Because the thorax is a rigid "
  "powerplant, the abdomen stays soft and expandable: it stretches to hold "
  "a blood meal many times the insect's weight (in a mosquito), carries "
  "developing eggs, and pumps air through the tracheae with rhythmic "
  "abdominal contractions. Segmentation is still visible as sclerites "
  "(hardened plates) separated by flexible membranes, letting each tagma "
  "bend, expand, and articulate while staying armored."),
 "key_points": [
  "Head: sensors + mouthparts + brain (supraesophageal ganglion)",
  "Thorax: 3 segments, 3 leg pairs, usually 2 wing pairs; flight-muscle powerplant",
  "Abdomen: up to 11 segments; gut, reproduction, dorsal vessel heart, most tracheae",
  "Tagmosis = segment fusion into task modules; the 3-tagma check identifies insects",
  "Thorax deforms to drive wings — up to ~1,000 beats/second in midges",
 ],
 "requirements": [
  "Diagram or specimen showing all three tagmata",
  "Ability to locate prothorax, mesothorax, metathorax",
 ],
 "standards": [
  "Morphological terminology per Chapman (2013)",
 ],
 "citations": [CIT_CHAPMAN, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: three modules, three missions — sense, move, sustain. "
  "The thorax is the engine room, the abdomen the cargo hold, the head the "
  "bridge. Manon's Signature take: any machine that lasts should copy this "
  "division — never mix the engine with the cargo."),
 "demo_kind": "body_tagma",
},
{
 "key": "exoskeleton-molting", "name": "The Exoskeleton and Molting",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The insect exoskeleton (cuticle) is a layered armor of chitin fibers "
  "embedded in protein, hardened where needed by tanning (sclerotization) "
  "and in some species by mineralization. It is the insect's skeleton, "
  "skin, waterproofing, and muscle-attachment surface all at once — "
  "muscles anchor to internal ridges (apodemes) of the cuticle the way "
  "human muscles anchor to bone. The cuticle has three main layers: the "
  "thin outer epicuticle (the wax waterproofing layer), the thick "
  "exocuticle (hardened), and the endocuticle (tough but flexible). Because "
  "the hardened cuticle cannot stretch, growth requires molting — the old "
  "cuticle splits and the insect crawls out larger, then hardens the new "
  "soft cuticle by pumping it full of air or fluid. Each stage between "
  "molts is an instar; most insects pass through 3 to 7 instars. Molting "
  "is hormonally choreographed: ecdysone (the molting hormone) from the "
  "prothoracic gland triggers the new cuticle, and falling juvenile "
  "hormone levels allow the molt to proceed toward the adult form. A "
  "newly molted insect is soft, pale, and helpless for minutes to hours — "
  "the most vulnerable moment of its life."),
 "how_it_works": (
  "Molting runs in four phases. First, apolysis: the epidermis pulls away "
  "from the old cuticle and secretes molting fluid containing chitinase "
  "enzymes that digest the inner old layers — the insect recycles up to "
  "90 percent of the old cuticle's chitin. Second, the epidermis secretes "
  "the new epicuticle and exocuticle beneath the old skin. Third, ecdysis: "
  "the insect swallows air (or water) to build pressure, splits the old "
  "cuticle along a weakened seam, and wriggles out, often hanging to let "
  "gravity help. Fourth, expansion and tanning: the new cuticle is pumped "
  "up larger than the old one, then phenolic compounds cross-link the "
  "proteins (sclerotization) and the wax layer is laid down, hardening and "
  "waterproofing within hours. Dyar's law notes that the head-capsule "
  "width grows by a roughly constant ratio (often ~1.4x) per molt, so "
  "entomologists can count instars by measuring head capsules."),
 "key_points": [
  "Cuticle: epicuticle (wax) + exocuticle (hard) + endocuticle (flexible); chitin + protein",
  "Muscles attach to cuticle apodemes — exoskeleton is the skeleton",
  "Ecdysis: apolysis -> new cuticle secreted -> old skin split -> expansion -> tanning",
  "Ecdysone triggers molting; juvenile hormone controls whether it stays a larva",
  "Dyar's law: head-capsule width grows ~1.4x per instar",
  "Newly molted = soft, pale, vulnerable until tanning completes",
 ],
 "requirements": [
  "Shed skins (exuviae) or molting sequence photos",
  "Ruler/caliper for head-capsule measurements (Dyar's law)",
 ],
 "standards": [
  "Instar staging per standard entomological practice",
 ],
 "citations": [CIT_CHAPMAN, CIT_NORRIS],
 "sig_lens": (
  "Signature reading: the upgrade ritual — shed the old shell, expand the "
  "frame, re-harden stronger. Manon's Signature take: growth requires a "
  "planned vulnerability window; schedule the soft phase, guard it, and "
  "come out larger. Never molt without a safe place to harden."),
 "demo_kind": "molting_math",
},
{
 "key": "insect-legs", "name": "Insect Legs: Walking, Jumping, Swimming",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The insect leg is a jointed lever of six segments: coxa (hip), "
  "trochanter, femur (thigh), tibia (shin), tarsus (foot, usually 2-5 "
  "sub-segments), and the pretarsus with its claws and adhesive pads. "
  "Legs are modified per lifestyle into a toolkit of specializations. "
  "Cursorial (running) legs — long and slender, as in tiger beetles and "
  "cockroaches — are built for speed; a cockroach can sprint about 50 body "
  "lengths per second. Saltatorial (jumping) legs — the grasshopper's "
  "huge hind femur — store elastic energy in the cuticle and release it "
  "like a catapult, launching some fleas 150 times their body length. "
  "Raptorial (grasping) legs — the mantis's folded forelegs with spines — "
  "strike in 50-70 milliseconds to snag prey. Natatorial (swimming) legs "
  "bear fringes of hairs that act as oars in diving beetles and water "
  "boatmen. Fossorial (digging) legs — the mole cricket's shovel-like "
  "forelegs — excavate soil. Most walking insects use the alternating "
  "tripod gait: three legs (front+rear on one side, middle on the other) "
  "form a stable triangle while the other three swing forward, so the "
  "insect is always balanced — the same gait engineers copy for "
  "six-legged robots."),
 "how_it_works": (
  "The leg works as a lever system driven by muscles inside the thorax and "
  "leg segments. Extensor and flexor muscles pivot the femur-tibia joint; "
  "the tarsus flexes to grip. Adhesion comes from the pretarsus: paired "
  "claws hook rough surfaces while soft pads (arolia, pulvilli) use "
  "capillary films or dry van-der-Waals-like contact to cling to smooth "
  "glass — a fly's foot can support many times its body weight. Jumping "
  "legs cheat muscle limits with elastic storage: the grasshopper slowly "
  "contracts its huge femoral extensor, deforming a rubbery protein pad "
  "(resilin) and the semi-lunar process of the cuticle; a latch releases "
  "and the stored energy dumps into the tibia in milliseconds, producing "
  "accelerations over 100 g. The tripod gait is neurally simple — each "
  "leg's stepping is coordinated by local ganglia with rules like 'do not "
  "lift while the neighbor is swinging' — which is why hexapod robots run "
  "the same algorithm."),
 "key_points": [
  "6 segments: coxa, trochanter, femur, tibia, tarsus, pretarsus (claws + pads)",
  "Cursorial (run), saltatorial (jump), raptorial (grasp), natatorial (swim), fossorial (dig)",
  "Tripod gait: alternating stable triangle — copied by hexapod robots",
  "Fleas jump ~150x body length via elastic resilin catapult (>100 g acceleration)",
  "Adhesive pads + claws: grip smooth glass and rough bark alike",
 ],
 "requirements": [
  "Specimens or images of at least 3 leg specializations",
  "Slow-motion video reference for jump or strike mechanics (optional)",
 ],
 "standards": [
  "Leg segment terminology per Chapman (2013)",
 ],
 "citations": [CIT_CHAPMAN, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: one standard leg chassis, five mission kits. The "
  "insect never redesigns the leg — it re-kits it. Manon's Signature take: "
  "standardize the platform, specialize the attachment; and when muscle is "
  "not enough, store the energy and release it all at once."),
 "demo_kind": "leg_leverage",
},
{
 "key": "insect-mouthparts", "name": "Insect Mouthparts: Chewing, Piercing, Sponging",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Insect mouthparts are modified head appendages, and their form reveals "
  "the insect's diet at a glance. The chewing (mandibulate) type is the "
  "ancestral toolkit: paired toothed mandibles that shear like jaws, "
  "maxillae that manipulate food, and the labium (fused lower lip) and "
  "labrum (upper lip) framing the mouth — grasshoppers, beetles, and "
  "caterpillars use it to bite leaves and wood. The piercing-sucking type "
  "bundles the mandibles and maxillae into needle-like stylets inside a "
  "sheath (the labium) — mosquitoes, bed bugs, aphids, and assassin bugs "
  "stab and pump fluids; the maxillary stylets interlock to form two "
  "canals, one injecting saliva and one drawing up food. The sponging "
  "type of house flies turns the labium into a soft pad (labellum) with "
  "grooves that soak up liquids like a sponge, after saliva liquefies "
  "solids. The siphoning type — the butterfly's coiled proboscis — is a "
  "drinking straw formed from the two maxillae that uncoils hydraulically "
  "to sip nectar. Bees carry chewing-lapping mouthparts: mandibles for wax "
  "work plus a long tongue (glossa) for lapping nectar. Mouthpart type is "
  "a primary key character in identification and predicts whether an "
  "insect is a chewer of crops, a sucker of sap or blood, or a pollinator."),
 "how_it_works": (
  "All mouthpart types are remodels of the same five parts — labrum, "
  "mandibles, maxillae, labium, hypopharynx. In chewers, the mandibles "
  "oppose each other with strong adductor muscles anchored inside the "
  "head capsule, generating shearing force; caterpillar mandibles can "
  "slice leaf tissue all day. In piercers, the stylet bundle works like a "
  "hypodermic set: the barbed maxillary stylets saw into tissue while the "
  "labium folds back as a guide; cibarial and pharyngeal pumps in the head "
  "create suction, and salivary glands inject anticoagulants (mosquito) or "
  "digestive enzymes (assassin bug). The butterfly proboscis uncoils when "
  "hemolymph pressure inflates it and recoils via intrinsic muscles. Fly "
  "sponging uses capillary action through the labellar grooves after "
  "regurgitated saliva dissolves the meal. Because each type is a "
  "structural commitment, mouthparts rarely change within a lineage — "
  "they are among the most reliable clues to an insect's order and "
  "ecology."),
 "key_points": [
  "Chewing: mandibles + maxillae + labium (grasshoppers, beetles, caterpillars)",
  "Piercing-sucking: stylet bundle in labial sheath; dual canals (aphids, mosquitoes, bugs)",
  "Sponging: labellum pad soaks liquefied food (house flies)",
  "Siphoning: coiled maxillary proboscis uncoils hydraulically (butterflies, moths)",
  "Chewing-lapping: mandibles + long glossa tongue (bees)",
  "Mouthpart type predicts diet and is a key identification character",
 ],
 "requirements": [
  "Magnified images of at least 3 mouthpart types",
  "Order-level ID key using mouthpart characters",
 ],
 "standards": [
  "Mouthpart terminology per Triplehorn & Johnson (2005)",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_CHAPMAN],
 "sig_lens": (
  "Signature reading: five tools from one parts bin — cut, stab, sponge, "
  "sip, lap. The head never invents new parts; it reassigns the old ones. "
  "Manon's Signature take: master a small parts inventory deeply instead "
  "of inventing new parts for every job."),
 "demo_kind": "mouthpart_matrix",
},
{
 "key": "insect-eyes-vision", "name": "Insect Eyes and Vision",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Most adult insects see with compound eyes — arrays of independent "
  "visual units called ommatidia, each with its own lens, crystalline "
  "cone, and photoreceptor cluster. A dragonfly packs about 30,000 "
  "ommatidia per eye, giving nearly 360-degree vision; an ant worker may "
  "have fewer than 100. Each ommatidium samples one point of light, so "
  "the compound eye trades resolution for superb motion detection and a "
  "huge field of view — a fly detects movement far faster than a human "
  "eye. Many insects also carry up to three ocelli, simple single-lens "
  "eyes on top of the head that sense light intensity and horizon level "
  "to stabilize flight. Insect color vision commonly extends into the "
  "ultraviolet: bees see UV patterns on flowers (nectar guides) invisible "
  "to humans, and many insects navigate by the polarization pattern of "
  "the sky. Some nocturnal insects have superposition eyes that pool "
  "light from many ommatidia, gaining up to 1,000x sensitivity for night "
  "flight. Larvae of holometabolous insects use simple stemmata instead, "
  "rebuilt into compound eyes during metamorphosis."),
 "how_it_works": (
  "In the common apposition eye, each ommatidium is optically isolated by "
  "pigment cells: light entering its facet lens is funneled down the "
  "crystalline cone to the rhabdom — a stack of microvilli membranes "
  "loaded with visual pigments (rhodopsins). Photon absorption triggers a "
  "neural signal; the brain assembles the mosaic of ommatidial signals "
  "into a coarse image. Resolution is set by the interommatidial angle "
  "(about 1 degree in a dragonfly, worse in small eyes) — the eye cannot "
  "resolve detail finer than the spacing of its facets. Flicker-fusion "
  "frequency is high (200-300 Hz in flies vs ~60 Hz in humans), which is "
  "why a fly sees your approaching hand in slow motion and escapes. "
  "Polarized-light navigation works through specialized dorsal-rim "
  "ommatidia whose microvilli are aligned to analyze sky polarization; "
  "bees and ants combine this sky compass with a sun compass and step "
  "counting (odometry) to navigate home."),
 "key_points": [
  "Ommatidia: independent facets; dragonfly ~30,000/eye, ant <100",
  "Trade-off: poor resolution, superb motion detection, near-360 deg field",
  "Ocelli: 0-3 simple eyes sensing light level for flight stability",
  "UV vision + polarized-sky compass in bees, ants, and many others",
  "Flicker fusion 200-300 Hz — flies perceive fast motion in slow motion",
  "Superposition eyes: up to 1000x light pooling for night fliers",
 ],
 "requirements": [
  "Close-up images of compound eyes and ocelli",
  "UV flower photos to show nectar guides (optional)",
 ],
 "standards": [
  "Eye-type terminology per Chapman (2013)",
 ],
 "citations": [CIT_CHAPMAN, CIT_RESH],
 "sig_lens": (
  "Signature reading: thousands of cheap sensors beat one expensive lens "
  "when speed matters. The compound eye is a parallel array — resolution "
  "sacrificed for frame rate and coverage. Manon's Signature take: match "
  "the sensor to the mission; a guard needs wide fast eyes, not a "
  "telescope."),
 "demo_kind": "eye_facets",
},
{
 "key": "antennae-smell", "name": "Antennae and Smell",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The antennae are the insect's chemical and mechanical sensing array — "
  "its nose, ears, and fingertips combined. Each antenna has three "
  "sections: the scape (base), the pedicel (housing Johnston's organ, "
  "which detects vibration and sound), and the long flagellum bearing "
  "thousands of sensory hairs (sensilla). Olfactory sensilla house "
  "receptor neurons tuned to odor molecules; a male silkmoth's feathery "
  "antennae carry about 17,000 sensilla and can detect a single molecule "
  "of the female's pheromone, tracking her plume from kilometers away. "
  "Antenna shapes are wildly diverse and diagnostic: filiform (threadlike, "
  "cockroaches), moniliform (beaded, termites), clavate (clubbed, "
  "butterflies), lamellate (fan plates, scarab beetles), plumose "
  "(feathery, male moths and mosquitoes), aristate (bristled, house "
  "flies), and geniculate (elbowed, ants and bees). Beyond smell, "
  "antennae detect humidity, temperature, carbon dioxide, air movement, "
  "touch, and — via Johnston's organ — the wingbeat songs of mates "
  "(mosquitoes tune to each other's flight tones). Because antenna form "
  "is so consistent within groups, entomologists use it as a front-line "
  "identification character."),
 "how_it_works": (
  "Olfaction works through porous sensilla: odor molecules diffuse "
  "through cuticular pores into the sensillum lymph, where odorant-binding "
  "proteins ferry them to receptor proteins on the dendrite membrane of "
  "olfactory receptor neurons. Binding opens ion channels, firing the "
  "neuron; the pattern of firing across hundreds of receptor types encodes "
  "the odor, and the antennal lobe of the brain (analogous to the "
  "vertebrate olfactory bulb) decodes it. Pheromone systems are "
  "extraordinarily sensitive because the receptor neurons express huge "
  "numbers of one receptor type and the sensilla are tuned to a single "
  "compound — the male moth's brain devotes a dedicated macroglomerular "
  "complex just to the female's blend. Mechanosensation runs in parallel: "
  "hair sensilla bend with touch and air currents, and Johnston's organ "
  "in the pedicel detects antennal vibration, letting male mosquitoes "
  "hear the ~400 Hz wingbeat of females and adjust their own tone to "
  "match."),
 "key_points": [
  "3 parts: scape, pedicel (Johnston's organ), flagellum with sensilla",
  "Male silkmoth: ~17,000 sensilla; single-molecule pheromone detection over kilometers",
  "7+ diagnostic shapes: filiform, moniliform, clavate, lamellate, plumose, aristate, geniculate",
  "Senses: odor, humidity, temperature, CO2, touch, air flow, sound/vibration",
  "Antennal lobe decodes odor patterns like a vertebrate olfactory bulb",
 ],
 "requirements": [
  "Antenna shape chart for ID practice",
  "Magnified antenna images across orders",
 ],
 "standards": [
  "Antennal terminology per Triplehorn & Johnson (2005)",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_CHAPMAN],
 "sig_lens": (
  "Signature reading: one mast, every sensor that matters — chemical, "
  "thermal, mechanical, acoustic. The antenna proves the Signature rule: "
  "put all passive sensing on one upgradeable array so the rest of the "
  "machine stays simple. Manon's take: sense first, act second, always."),
 "demo_kind": "antenna_odors",
},
{
 "key": "insect-wings-flight", "name": "Insect Wings and Flight",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Insects were the first animals to fly, and flight is the single "
  "greatest reason for their dominance: it opened the air for escape, "
  "dispersal, migration, and mate-finding some 400 million years ago. "
  "Insect wings are not modified legs — they are outgrowths of the "
  "thoracic body wall, stiffened by a branching network of veins "
  "(tubes carrying hemolymph, nerves, and air) and covered in membrane. "
  "Most flying insects have two pairs: the forewings and hindwings beat "
  "in coordination. Evolution has remodeled them repeatedly: beetles "
  "turned forewings into armored elytra that protect the folded flight "
  "wings beneath; true flies reduced the hindwings to halteres — tiny "
  "gyroscopic clubs that sense rotation and stabilize flight; "
  "grasshoppers made leathery tegmina forewings; true bugs made half-"
  "leathery hemelytra; thrips and some parasitoid wasps fringe theirs "
  "with hairs. Flight performance is extreme: dragonflies intercept prey "
  "in midair with ~95% success, hawk moths hover like hummingbirds, and "
  "locust swarms fly hundreds of kilometers. Wingbeat frequencies range "
  "from ~5 Hz in large butterflies to ~1,000 Hz in midges, driven by "
  "asynchronous flight muscles that contract multiple times per nerve "
  "impulse through a stretch-activation cycle."),
 "how_it_works": (
  "Insect flight muscles do not pull the wings directly. Instead, massive "
  "dorsal longitudinal and dorsoventral muscles deform the thoracic box: "
  "contracting the vertical muscles arches the thorax up and drives the "
  "wings down; contracting the longitudinal muscles flattens it and drives "
  "the wings up. The wing hinge converts this oscillation into the "
  "wingbeat, with a click mechanism snapping the wing between up and down "
  "positions. In asynchronous fliers (flies, bees, beetles), each nerve "
  "impulse sets off a self-sustaining oscillation — the muscle contracts "
  "when stretched by its antagonist, so one neural signal yields many "
  "beats, reaching the hundreds of hertz needed. Aerodynamically, insects "
  "fly at low Reynolds numbers where air feels syrupy; they generate lift "
  "with a leading-edge vortex that stays attached through the stroke "
  "(delayed stall), plus rotational lift at stroke reversal and wake "
  "capture — mechanisms unknown to classical fixed-wing theory until "
  "high-speed cameras revealed them. Halteres in flies beat in "
  "anti-phase and bend with Coriolis forces during rotation, giving the "
  "brain gyroscopic feedback within milliseconds."),
 "key_points": [
  "Wings = thoracic wall outgrowths with veins, not modified legs; first flight ~400 mya",
  "Remodels: elytra (beetles), halteres (flies), tegmina (grasshoppers), hemelytra (bugs)",
  "Indirect flight muscles deform the thorax; hinge + click mechanism drives the beat",
  "Asynchronous muscle: stretch-activation gives many beats per nerve impulse (up to ~1000 Hz)",
  "Leading-edge vortex + delayed stall generate lift at low Reynolds numbers",
  "Dragonfly aerial predation success ~95%; locust swarms travel hundreds of km",
 ],
 "requirements": [
  "Wing-type chart (elytra, halteres, tegmina, hemelytra, membranous)",
  "Slow-motion flight footage reference (optional)",
 ],
 "standards": [
  "Wing venation terminology per standard entomological practice",
 ],
 "citations": [CIT_CHAPMAN, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: the first true aircraft — indirect drive, "
  "oscillating airframe, gyroscopic stabilizers. The fly's halteres are "
  "the original IMU. Manon's Signature take: when the mission needs "
  "speed, drive the frame, not the limb — and always ship a gyro."),
 "demo_kind": "wingbeat",
},
{
 "key": "hemolymph-tracheae", "name": "Insect Blood and Breathing: Hemolymph and Tracheae",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Insects run an open circulatory system and a direct-delivery breathing "
  "system — no lungs, no red blood cells, no closed blood vessels. The "
  "'blood', called hemolymph, bathes the organs directly in the body "
  "cavity (hemocoel); a simple tube heart, the dorsal vessel, pumps it "
  "forward through peristaltic waves, with valved openings (ostia) letting "
  "hemolymph re-enter. Hemolymph carries nutrients, hormones, wastes, and "
  "immune cells (hemocytes), but carries little oxygen — that job belongs "
  "to the tracheal system. Air enters through paired openings called "
  "spiracles along the thorax and abdomen, travels down branching tracheae "
  "reinforced with spiral thickenings (taenidia), and reaches microscopic "
  "tracheoles that end directly on or inside individual cells. Oxygen "
  "diffuses the final micrometers to mitochondria; carbon dioxide "
  "diffuses out. Spiracles have closable valves, letting desert insects "
  "seal their airways and lose almost no water. Because diffusion only "
  "works over short distances, the tracheal system caps how large insects "
  "can grow — the giant dragonflies of the Carboniferous (wingspans over "
  "70 cm) flew when atmospheric oxygen was ~35% instead of today's 21%."),
 "how_it_works": (
  "Breathing is driven by diffusion plus active ventilation. At rest, "
  "oxygen diffuses down the tracheae; during flight, abdominal pumping "
  "and thoracic movements ventilate the big tracheal trunks, and air sacs "
  "(thin-walled expansions) act as bellows and buoyancy tanks. Many "
  "insects use discontinuous gas exchange: spiracles stay closed, then "
  "flutter, then open fully — a cycle that flushes CO2 while minimizing "
  "water loss, cutting respiratory water loss dramatically in arid "
  "species. The dorsal vessel pumps hemolymph forward into the head; it "
  "then percolates backward through the hemocoel, washing the organs. "
  "Accessory pulsatile organs boost flow into the wings, legs, and "
  "antennae. Hemocytes patrol for pathogens, encapsulating parasites and "
  "sealing wounds by clotting (hemolymph darkens at a wound as phenoloxidase "
  "cascades deposit melanin). The system's elegance is its minimalism: "
  "deliver oxygen straight to the cell and let an open bath handle "
  "everything else — sufficient for the most successful animals ever."),
 "key_points": [
  "Hemolymph: open circulation; dorsal vessel heart; carries nutrients/hormones/immune cells, not O2",
  "Tracheae: spiracles -> taenidia-reinforced tubes -> tracheoles ending at cells",
  "Diffusion distance limits body size (Carboniferous giants needed 35% O2)",
  "Discontinuous gas exchange: closed-flutter-open spiracle cycle saves water",
  "Hemocytes encapsulate parasites; melanin clots seal wounds",
 ],
 "requirements": [
  "Tracheal system diagram",
  "Spiracle valve concept (closable pores)",
 ],
 "standards": [
  "Respiratory terminology per Chapman (2013)",
 ],
 "citations": [CIT_CHAPMAN, CIT_NORRIS],
 "sig_lens": (
  "Signature reading: point-to-point delivery beats hub-and-spoke — "
  "oxygen goes straight to the cell, no warehouse, no fleet. Manon's "
  "Signature take: cut the middleman out of every supply line you can; "
  "direct delivery is always cheaper and faster."),
 "demo_kind": "tracheal_diffusion",
},
]

# ------------------------------------------------------------------ COMPOUNDED
ENTRIES += [
{
 "key": "metamorphosis-hemi", "name": "Metamorphosis I: Hemimetaboly (Incomplete)",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Hemimetabolous insects develop by incomplete metamorphosis: the young, "
  "called nymphs (or naiads when aquatic), look like small wingless "
  "versions of the adult and share its habitat and diet. Each molt brings "
  "a larger nymph with slightly more developed wing pads — external "
  "wing buds that grow visibly bigger every instar — until the final molt "
  "produces the winged adult. There is no pupal stage and no radical "
  "rebuild: a grasshopper nymph eats leaves, hops, and dodges predators "
  "just like the adult, only smaller and flightless. Orders with "
  "hemimetaboly include the Orthoptera (grasshoppers, crickets), Hemiptera "
  "(true bugs, aphids, cicadas), Odonata (dragonflies, damselflies — "
  "aquatic naiads), Blattodea (cockroaches, termites), Mantodea (mantids), "
  "and Phasmatodea (stick insects). The strategy's strength is continuity: "
  "every instar can feed and flee, so there is no helpless pupal period. "
  "Its cost is competition — nymphs and adults eat the same food, so "
  "crowding hits every life stage at once, as locust plagues demonstrate."),
 "how_it_works": (
  "Hemimetabolous development is driven by the juvenile hormone (JH) "
  "gradient across molts. High JH at each molt keeps the insect in "
  "nymphal form; as JH production fades in the final instars, the last "
  "molt produces adult structures — functional wings, mature genitalia, "
  "adult coloration. Wing pads develop externally because the wing "
  "primordia were never internalized. Aquatic naiads add special "
  "adaptations: dragonfly naiads breathe with rectal gills and hunt with "
  "a lightning-fast extendable labium (the 'mask') that shoots out to "
  "grab prey. Growth is stepwise but the body plan never dissolves — the "
  "nervous system, gut, and muscles are remodeled incrementally at each "
  "ecdysis rather than rebuilt. Because nymphs occupy the adult niche, "
  "many hemimetabolous species stagger generations or migrate to reduce "
  "competition, and some (like periodical cicadas) use extreme "
  "synchronization — 13- or 17-year emergences — to satiate predators."),
 "key_points": [
  "Nymphs resemble small wingless adults; share habitat and diet",
  "Wing pads grow externally each instar; no pupal stage",
  "Orders: Orthoptera, Hemiptera, Odonata, Blattodea, Mantodea, Phasmatodea",
  "Juvenile hormone decline across molts unlocks the adult form",
  "Strength: every instar feeds and flees; cost: nymph-adult competition",
  "Dragonfly naiads: rectal gills + ballistic labium 'mask'",
 ],
 "requirements": [
  "Nymph-to-adult image series (e.g., grasshopper instars)",
  "Wing-pad development diagram",
 ],
 "standards": [
  "Developmental terminology per Gullan & Cranston (2014)",
 ],
 "citations": [CIT_GULLAN, CIT_NORRIS],
 "sig_lens": (
  "Signature reading: ship early, upgrade in place — the nymph is a "
  "working prototype that never goes offline. Manon's Signature take: "
  "when downtime is fatal, evolve the live system instar by instar; never "
  "take the machine apart while it is running."),
 "demo_kind": "hemimetaboly_table",
},
{
 "key": "metamorphosis-holo", "name": "Metamorphosis II: Holometaboly (Complete)",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Holometabolous insects develop by complete metamorphosis — the most "
  "successful life-history strategy in the animal kingdom, used by about "
  "85 percent of all insect species. Four radically different stages: egg, "
  "larva, pupa, adult. The larva (caterpillar, grub, maggot) is a feeding "
  "machine, often wormlike and completely unlike the adult; it eats, "
  "grows, and molts through several instars. Then comes the pupa — the "
  "chrysalis or cocoon stage — where the larval body is largely dissolved "
  "and rebuilt from clusters of dormant cells called imaginal discs into "
  "the winged adult. The adult (imago) is typically a short-lived "
  "dispersal and reproduction machine that may not feed at all (as in "
  "mayflies and some moths). Orders with holometaboly: Coleoptera "
  "(beetles), Diptera (flies), Hymenoptera (ants, bees, wasps), "
  "Lepidoptera (butterflies, moths), plus fleas, caddisflies, lacewings, "
  "and scorpionflies. The genius of the strategy is niche partitioning: "
  "larvae and adults eat different foods in different places, so a "
  "caterpillar and a butterfly never compete — one species occupies two "
  "ecological niches, doubling its opportunities."),
 "how_it_works": (
  "The larva grows under high juvenile hormone, which forces every molt "
  "to produce another larval instar. When the larva reaches critical "
  "weight, JH drops, ecdysone surges, and the insect pupates. Inside the "
  "pupa, most larval tissues undergo programmed cell death (histolysis); "
  "the adult is constructed from imaginal discs — about 19 pairs of "
  "cell clusters set aside in the embryo that sat dormant through larval "
  "life. Each disc everts and unfolds into a structure: wing discs become "
  "wings, leg discs become legs, eye discs become compound eyes. The "
  "transformation is powered entirely by stored larval fat body — the "
  "pupa cannot eat. Hormonal timing is precise: a pulse of ecdysone "
  "without JH makes pupal cuticle; the next pulse makes adult cuticle, "
  "and the adult emerges (eclosion) by swallowing air to split the pupal "
  "case. The cost is total helplessness during the pupal weeks — hence "
  "cocoons, chrysalises, soil cells, and chemical defenses — but the "
  "payoff is the radiation of beetles, flies, wasps, and moths into "
  "nearly every niche on Earth."),
 "key_points": [
  "4 stages: egg -> larva -> pupa -> adult; ~85% of insect species",
  "Larva = feeding machine; pupa = rebuild; adult = dispersal/reproduction",
  "Imaginal discs: dormant cell clusters that build the adult during pupation",
  "JH high = stay larva; JH drop + ecdysone = pupate; next ecdysone = adult",
  "Niche partitioning: larvae and adults never compete for food",
  "Orders: Coleoptera, Diptera, Hymenoptera, Lepidoptera, Siphonaptera, Trichoptera",
 ],
 "requirements": [
  "Four-stage life cycle diagram (e.g., butterfly)",
  "Imaginal disc concept explanation",
 ],
 "standards": [
  "Developmental terminology per Gullan & Cranston (2014)",
 ],
 "citations": [CIT_GULLAN, CIT_NORRIS],
 "sig_lens": (
  "Signature reading: the full teardown rebuild — dissolve the working "
  "machine and reassemble it as something greater from cached blueprints "
  "(imaginal discs). Manon's Signature take: when incremental upgrades "
  "cannot reach the next form, schedule a chrysalis phase — protected, "
  "fully funded by stored reserves, and non-negotiable in duration."),
 "demo_kind": "holometaboly_energy",
},
{
 "key": "order-coleoptera", "name": "The Insect Orders: Coleoptera, the Beetles",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Coleoptera — the beetles — is the largest order in the animal kingdom: "
  "about 400,000 described species, roughly 40 percent of all described "
  "insects and a quarter of all described life. The beetle signature is "
  "the elytra: hardened forewings that meet in a straight line down the "
  "back, armoring the folded, membranous hindwings used for flight. "
  "Beetles are holometabolous, with larvae (grubs, wireworms) that often "
  "live entirely different lives from the adults. They occupy nearly "
  "every habitat: ground beetles (Carabidae) hunt as nocturnal predators; "
  "scarab beetles (Scarabaeidae) include dung rollers and the sacred "
  "scarabs of Egypt; weevils (Curculionidae, ~60,000 species, the largest "
  "animal family) bore into seeds, stems, and stored grain with their "
  "long snouts; ladybird beetles (Coccinellidae) devour aphids; fireflies "
  "(Lampyridae) signal with bioluminescent lanterns; stag beetles "
  "(Lucanidae) joust with enormous mandibles. The elytra let beetles "
  "colonize harsh microhabitats — under bark, in soil, in deserts — by "
  "sealing moisture in and predators out, and many desert beetles harvest "
  "fog on their elytra. Identification starts with the elytra: straight "
  "midline suture, chewing mouthparts, holometabolous development."),
 "how_it_works": (
  "The elytra work as a protective shell and flight case. At rest they "
  "lock together along the straight elytral suture, sealing the abdomen "
  "and the delicate folded hindwings beneath; the subelytral cavity traps "
  "humid air, cutting water loss — the key to beetle success in deserts. "
  "For takeoff, muscles rotate the elytra up and out to the sides, the "
  "hindwings unfold (some beetles unfold via wing-base muscles, others "
  "with leg assistance), and the hindwings alone power flight while the "
  "elytra act as stabilizers. Larval forms are diverse: scarab grubs are "
  "C-shaped soil dwellers chewing roots; wireworms (click beetle larvae) "
  "are hard, cylindrical soil predators and pests; ladybird larvae are "
  "spiny, alligator-like aphid hunters. Weevil snouts (rostra) carry the "
  "chewing mouthparts at the tip, letting the female drill a precise hole "
  "in a seed or nut, lay one egg inside, and seal it — the larva then "
  "develops in a private pantry. Firefly lanterns produce cold light by "
  "the luciferin-luciferase reaction, flashing species-specific codes to "
  "attract mates."),
 "key_points": [
  "~400,000 described species — 40% of insects, 25% of all described life",
  "Elytra: hardened forewings meeting in a straight dorsal suture",
  "Holometabolous; larvae (grubs/wireworms) differ radically from adults",
  "Weevils (Curculionidae): ~60,000 species, largest animal family",
  "Elytra seal moisture in — the desert-colonization trick; fog-harvesting elytra",
  "Firefly bioluminescence: luciferin-luciferase cold light for mate signaling",
 ],
 "requirements": [
  "Elytra suture diagram",
  "Representative family images (Carabidae, Scarabaeidae, Curculionidae, Coccinellidae)",
 ],
 "standards": [
  "Ordinal diagnosis per Triplehorn & Johnson (2005)",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_RESH],
 "sig_lens": (
  "Signature reading: armor first, flight second — the beetle carries its "
  "hangar on its back. Manon's Signature take: the most successful design "
  "in nature protects the delicate mechanism with a hard case; ruggedize "
  "the shell and the fragile tech inside survives anywhere."),
 "demo_kind": "coleoptera_share",
},
{
 "key": "orders-diptera-hymenoptera", "name": "The Insect Orders: Diptera and Hymenoptera",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Diptera (true flies) and Hymenoptera (ants, bees, wasps) are the two "
  "orders that most directly touch human life — one as disease vectors "
  "and decomposers, the other as pollinators and social marvels. Diptera "
  "means 'two wings': flies fly with only the forewings; the hindwings "
  "are reduced to halteres, gyroscopic stabilizers. With ~160,000 "
  "described species, flies include mosquitoes (Culicidae) — the "
  "deadliest animals to humans via malaria, dengue, and Zika; house flies "
  "(Muscidae); hover flies (Syrphidae), the striped bee mimics whose "
  "larvae eat aphids; fruit flies (Drosophilidae), the geneticists' "
  "workhorse; and tachinid flies, parasitoids of caterpillars. Fly larvae "
  "(maggots) are legless feeding machines driving decomposition. "
  "Hymenoptera (~150,000 described species) is defined by two pairs of "
  "membranous wings hooked together in flight, chewing mouthparts "
  "(often with a nectar-lapping tongue), and — in the stinging lineages — "
  "an ovipositor modified into a venomous stinger. It holds the ants "
  "(Formicidae), bees (Anthophila), and wasps, including the parasitoid "
  "wasps — possibly the most species-rich group on Earth, most still "
  "undescribed. Hymenoptera invented eusociality multiple times and "
  "haplodiploid sex determination, and bees pollinate roughly a third of "
  "human crops."),
 "how_it_works": (
  "Fly flight is the most maneuverable in the insect world: halteres beat "
  "in antiphase to the wings and bend under Coriolis forces when the body "
  "rotates, firing sensory neurons that report rotation within "
  "milliseconds — the fly corrects course faster than its brain could "
  "compute it, a reflex loop. Mosquito females locate hosts by CO2 plumes, "
  "body heat, and skin odors, then pierce with six stylets and inject "
  "anticoagulant saliva; males feed only on nectar. In Hymenoptera, the "
  "forewing and hindwing hook together with tiny hamuli, beating as one "
  "surface for efficient flight. The wasp waist (petiole) gives the "
  "abdomen extreme articulation for stinging, egg-laying precision, and "
  "nest construction. Parasitoid wasps lay eggs in or on host insects; "
  "the larva consumes the host alive, often manipulating its behavior — "
  "some inject polydnaviruses that suppress the host immune system. "
  "Haplodiploidy (fertilized eggs become females, unfertilized become "
  "males) makes sisters share 75% of their genes, a genetic foundation "
  "that repeatedly enabled the evolution of worker castes and eusocial "
  "colonies."),
 "key_points": [
  "Diptera: 2 wings + haltere gyroscopes; ~160,000 species; mosquitoes = deadliest vectors",
  "Halteres sense rotation via Coriolis bending — millisecond course correction",
  "Hymenoptera: hooked wing pairs, wasp waist, ovipositor-to-stinger; ~150,000 species",
  "Parasitoid wasps: possibly the most species-rich animal group; polydnavirus immune suppression",
  "Haplodiploidy: sisters share 75% genes — repeated foundation of eusociality",
  "Bees pollinate ~1/3 of human crops; hover fly larvae are aphid predators",
 ],
 "requirements": [
  "Haltere diagram and wing-coupling (hamuli) diagram",
  "Mosquito vs. hover fly comparison images",
 ],
 "standards": [
  "Ordinal diagnosis per Triplehorn & Johnson (2005)",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: the fly perfected reflex-speed stabilization; the "
  "wasp weaponized the egg-layer. Two orders, two masteries — sense-and-"
  "correct versus strike-and-build. Manon's Signature take: pick one "
  "superpower per platform and push it past what seems possible."),
 "demo_kind": "order_lookup",
},
{
 "key": "orders-lep-orth-hem", "name": "The Insect Orders: Lepidoptera, Orthoptera, Hemiptera",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Three more giant orders complete the field entomologist's core set. "
  "Lepidoptera (butterflies and moths, ~180,000 described species) means "
  "'scale wings': wings and bodies are tiled with microscopic pigmented "
  "scales that create color by pigment and by structural iridescence. "
  "Adults siphon nectar through a coiled proboscis; larvae (caterpillars) "
  "are chewing herbivores, some major crop pests, others silk producers "
  "(the silkworm Bombyx mori). Butterflies fly by day with clubbed "
  "antennae; most moths fly by night with feathery or threadlike "
  "antennae. Orthoptera (grasshoppers, crickets, katydids; ~28,000 "
  "species) are the musicians and jumpers: huge saltatorial hind legs, "
  "leathery tegmina forewings, and sound production by stridulation "
  "(file-and-scraper on wing or leg) with ears (tympana) on the abdomen "
  "or forelegs. Swarming locusts — the same species as solitary "
  "grasshoppers, transformed by crowding — form plagues of billions. "
  "Hemiptera (true bugs, ~100,000 species) are the piercers: piercing-"
  "sucking mouthparts in a labial sheath, and forewings half-hardened "
  "(hemelytra). They include aphids, cicadas, leafhoppers, stink bugs, "
  "assassin bugs, bed bugs, and kissing bugs. Aphids reproduce by "
  "parthenogenesis — telescoping generations where a female carries "
  "daughters already carrying granddaughters — and many farm honeydew "
  "with attendant ants."),
 "how_it_works": (
  "Lepidopteran scales are flattened cuticular hairs; each scale's "
  "ridges diffract light, so a Morpho butterfly's blue is structural, "
  "not pigment — the color cannot fade. The proboscis uncoils by "
  "hemolymph pressure and recoils with muscles, sipping nectar through "
  "capillary action. Caterpillars grow through 4-6 instars, then pupate "
  "as chrysalises (butterflies) or in silk cocoons (moths). Orthopteran "
  "stridulation: crickets rub a file on one forewing against a scraper "
  "on the other, each pulse train encoding species identity; females "
  "choose mates by the song's rhythm. The locust phase change is "
  "density-triggered: crowding raises serotonin, transforming solitary "
  "green hoppers into gregarious, dark, long-winged swarmers within a "
  "generation. Hemipteran feeding: stylets probe between plant cells to "
  "the phloem; saliva prevents sieve-tube sealing while the cibarial "
  "pump draws sugary sap — excess sugar is excreted as honeydew, which "
  "ants harvest and defend, forming a protection mutualism. Aphid "
  "parthenogenesis clones females all summer; only autumn's short days "
  "trigger sexual forms that lay overwintering eggs."),
 "key_points": [
  "Lepidoptera: scale wings (pigment + structural color); coiled siphoning proboscis; ~180,000 spp.",
  "Butterflies: day, clubbed antennae; moths: mostly night, feathery/threadlike antennae",
  "Orthoptera: saltatorial hind legs, tegmina, stridulation songs, tympanal ears; ~28,000 spp.",
  "Locust phase change: crowding -> serotonin -> gregarious swarming morph",
  "Hemiptera: piercing-sucking beak + hemelytra; aphids clone by parthenogenesis; ~100,000 spp.",
  "Ant-aphid honeydew mutualism: protection traded for sugar",
 ],
 "requirements": [
  "Scale-wing close-up image",
  "Stridulation mechanism diagram",
 ],
 "standards": [
  "Ordinal diagnosis per Triplehorn & Johnson (2005)",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_RESH],
 "sig_lens": (
  "Signature reading: three display technologies — structural color, "
  "acoustic broadcast, chemical farming. The moth wears light itself; the "
  "cricket sings its ID; the aphid outsources defense to ants. Manon's "
  "Signature take: advertise in the channel your audience actually "
  "receives."),
 "demo_kind": "lepidoptera_scales",
},
{
 "key": "insect-taxonomy", "name": "Insect Taxonomy and Classification",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Insect taxonomy organizes ~1 million described species into about 30 "
  "living orders nested in the class Insecta, phylum Arthropoda. The "
  "deepest split separates the wingless Apterygota (silverfish, bristle-"
  "tails — primitively wingless) from the Pterygota (winged insects and "
  "their secondarily wingless descendants like fleas and lice). Within "
  "Pterygota, the Paleoptera (dragonflies, mayflies — wings held out "
  "flat, cannot fold) branch from the Neoptera (wings fold back over the "
  "body), which then split into the hemimetabolous Polyneoptera and "
  "Paraneoptera and the holometabolous Holometabola — the super-"
  "radiation containing beetles, flies, wasps, and moths. Modern "
  "classification is phylogenetic, built from DNA sequences plus "
  "morphology: the current consensus (e.g., Misof et al., 2014, 1,478 "
  "genes across all orders) places fleas inside scorpionflies and "
  "confirms the Holometabola as a single radiation. Below order come "
  "family (e.g., Apidae — bees), genus, and species — the binomial "
  "(Apis mellifera) governed by the International Code of Zoological "
  "Nomenclature. DNA barcoding (the COI gene) now identifies species "
  "from a leg fragment, accelerating discovery of the estimated millions "
  "still undescribed."),
 "how_it_works": (
  "Classification works by shared derived characters (synapomorphies). "
  "All Holometabola share complete metamorphosis with a pupal stage — "
  "one evolutionary invention. All Hemiptera share piercing-sucking "
  "mouthparts in a sheath. Taxonomists score hundreds of such characters "
  "across specimens, then phylogenetic algorithms find the tree requiring "
  "the fewest evolutionary changes (parsimony) or the most probable "
  "history given a DNA-evolution model (maximum likelihood, Bayesian "
  "inference). A dichotomous key operationalizes this: each couplet "
  "offers two contrasting character states ('wings present / wings "
  "absent'), and following the matching path narrows order, then family, "
  "then genus. Type specimens anchor names — the single preserved "
  "individual to which a species name is permanently attached, housed in "
  "museums. When DNA shows a 'species' is actually several cryptic "
  "species, taxonomists revise: split, rename, designate new types. The "
  "system stays stable because the Code's priority rule keeps the oldest "
  "valid name, so Apis mellifera Linnaeus, 1758 remains the honey bee "
  "regardless of reclassification around it."),
 "key_points": [
  "~30 living orders in class Insecta; deepest split: Apterygota vs Pterygota",
  "Pterygota -> Paleoptera vs Neoptera -> Polyneoptera/Paraneoptera vs Holometabola",
  "Phylogenetic classification from DNA + morphology (Misof et al. 2014: 1,478 genes)",
  "Binomial nomenclature under the ICZN; type specimens anchor names",
  "Dichotomous keys: couplet-by-couplet narrowing by contrasting characters",
  "DNA barcoding (COI gene) identifies species from fragments; cryptic species keep being split",
 ],
 "requirements": [
  "Order-level phylogenetic tree diagram",
  "A working dichotomous key (order level)",
 ],
 "standards": [
  "Classification per Misof et al. (2014) phylogenomic framework",
  "Nomenclature per the International Code of Zoological Nomenclature",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: the master filing system — every specimen gets a "
  "permanent address in the tree of life, anchored by a physical type. "
  "Manon's Signature take: name things once, anchor the name to a real "
  "artifact, and let the tree reorganize around stable names."),
 "demo_kind": "taxonomy_tree",
},
{
 "key": "insect-behavior", "name": "Insect Behavior: Communication",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Insects communicate across every channel physics allows — chemical, "
  "acoustic, visual, vibrational, and tactile — often with sophistication "
  "that rivals vertebrates. Chemical signaling dominates: pheromones "
  "(invisible messenger molecules) coordinate mating, alarm, aggregation, "
  "and trail-following. A female silkmoth releases bombykol; the male's "
  "antennae detect single molecules kilometers downwind. Ants lay "
  "pheromone trails that foragers reinforce — the shortest path to food "
  "emerges without any ant understanding the map. Acoustic signaling: "
  "crickets and cicadas sing species-specific songs by stridulation or "
  "tymbal buckling (cicada songs reach ~120 decibels); mosquitoes duet "
  "by matching wingbeat frequencies. Visual signaling: fireflies flash "
  "coded light patterns; butterflies display wing patterns for mate "
  "choice and warning; jumping spiders are not insects, but male peacock "
  "spiders' dances show how far arthropod display goes. Vibrational "
  "signaling: leafhoppers and treehoppers send songs through plant stems, "
  "a private channel predators cannot easily eavesdrop. Tactile: honey "
  "bee workers dance — the waggle dance encodes the angle to food "
  "relative to the sun and the distance via waggle duration — and ants "
  "antennate nestmates to exchange food and colony odor."),
 "how_it_works": (
  "Pheromone communication is a chemical broadcast with extreme "
  "specificity: blends of a few compounds in exact ratios, detected by "
  "dedicated receptor neurons and decoded in the antennal lobe's "
  "macroglomerular complex. Trail pheromones evaporate, so the trail is "
  "a living computation — strong trails mean recent heavy traffic, and "
  "the colony's foraging network self-organizes like a neural net. "
  "Sound production has three mechanisms: stridulation (file-scraper "
  "friction), tymbal buckling (a ribbed membrane popping in and out, in "
  "cicadas), and crepitation (wing snapping). Hearing uses tympanal "
  "organs — thin membranes backed by air sacs with attached sensory "
  "neurons — tuned to the species' own frequency band, letting moths "
  "hear hunting bats' ultrasound and dive evasively. The waggle dance "
  "translates a flight vector into a walking pattern on the vertical "
  "comb: the angle of the waggle run from vertical equals the angle of "
  "the food from the sun's azimuth; each second of waggling encodes "
  "roughly a kilometer of distance. Substrate vibration travels through "
  "stems as bending waves; treehoppers press their bodies to the stem "
  "and drum, and rivals jam each other's signals in vibrational duels."),
 "key_points": [
  "Chemical: pheromones (mate, alarm, trail, aggregation); single-molecule sensitivity in moths",
  "Acoustic: stridulation, tymbal buckling (cicadas ~120 dB), wingbeat duets",
  "Visual: firefly flash codes, butterfly displays, UV patterns",
  "Vibrational: stem-borne songs — a private, predator-proof channel",
  "Tactile: waggle dance encodes sun-angle + distance; antennation shares colony odor",
  "Ant trails: evaporating pheromones compute shortest paths with no central planner",
 ],
 "requirements": [
  "Signal-channel matrix (channel x example x mechanism)",
  "Waggle-dance angle diagram",
 ],
 "standards": [
  "Behavioral terminology per Resh & Cardé (2009)",
 ],
 "citations": [CIT_RESH, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: five channels, zero central control — the colony "
  "computes with evaporating ink. Manon's Signature take: broadcast in "
  "the cheapest channel that reaches the receiver, and let simple local "
  "rules produce the swarm's intelligence."),
 "demo_kind": "signal_matrix",
},
{
 "key": "social-ants-termites", "name": "Social Insects: Ants and Termites",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Eusociality — cooperative brood care, overlapping generations, and a "
  "reproductive division of labor — evolved independently in ants, "
  "termites, some bees and wasps, and a few others, and it produced the "
  "ecologically dominant insects. Ants (Formicidae, ~14,000 described "
  "species) are eusocial wasps: every colony centers on one or more "
  "queens that lay all the eggs, while sterile female workers forage, "
  "nurse, build, and defend, and males exist briefly to mate. A single "
  "leafcutter colony can house 8 million workers farming fungus gardens "
  "on harvested leaf pulp; army ant colonies of 20 million march in "
  "raiding swarms; Argentine ant supercolonies span hundreds of "
  "kilometers with millions of queens cooperating. Termites (Blattodea, "
  "~3,000 species) are eusocial cockroaches — the only eusocial insects "
  "with both male and female workers (the king stays with the queen for "
  "life). A termite queen can lay 30,000 eggs a day for decades, attended "
  "by workers and defended by soldiers with chemical-spraying or "
  "snapping mandibles. Termites digest wood with symbiotic gut "
  "protozoa and bacteria, and their mounds — engineered with passive "
  "ventilation that holds internal temperature within a degree — are the "
  "largest animal-built structures relative to builder size. Together, "
  "ants and termites can make up a third or more of animal biomass in "
  "tropical forests."),
 "how_it_works": (
  "A colony runs on division of labor without a boss. In ants, caste is "
  "set by larval nutrition and pheromones: well-fed larvae become queens "
  "(in species with queen-worker dimorphism), others become workers, and "
  "in polymorphic species like leafcutters, continuous size variation "
  "produces minims (gardeners), medias (foragers), and majors (soldiers). "
  "Age polyethism schedules tasks by age — young workers nurse brood "
  "inside, older workers take the dangerous foraging outside. Foraging "
  "is coordinated by pheromone trails with positive feedback: the first "
  "finder's trail recruits nestmates, and the trail strengthens with "
  "traffic, converging the colony on the richest source. Termite "
  "societies add lifelong royal pairs and soldier castes; workers feed "
  "the queen and soldiers by trophallaxis (mouth-to-mouth food sharing), "
  "which also spreads gut symbionts to newly molted nestmates — the "
  "microbiome is socially transmitted. Mound ventilation works by "
  "stack effect: warm air rises through the central chimney, drawing "
  "cool air through lower galleries, passively air-conditioning millions "
  "of inhabitants. Defense ranges from formic acid spraying to suicidal "
  "colony defense (Malaysian exploding ants rupture their bodies to "
  "spray toxins)."),
 "key_points": [
  "Eusociality: cooperative brood care + overlapping generations + reproductive division of labor",
  "Ants: eusocial wasps; queens lay, sterile female workers do everything; ~14,000 spp.",
  "Leafcutter colonies: ~8M workers farming fungus; Argentine ants: 100s-of-km supercolonies",
  "Termites: eusocial cockroaches; king + queen for life; queen lays ~30,000 eggs/day",
  "Caste by nutrition/pheromones; age polyethism schedules tasks by worker age",
  "Mound ventilation: passive stack-effect air conditioning; gut symbionts spread by trophallaxis",
 ],
 "requirements": [
  "Caste diagram (queen, workers, soldiers, males)",
  "Trail-pheromone feedback concept",
 ],
 "standards": [
  "Social-insect terminology per Resh & Cardé (2009)",
 ],
 "citations": [CIT_RESH, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: the original distributed workforce — no manager, "
  "just pheromone protocols and age-based job rotation. Manon's "
  "Signature take: design the protocol, not the hierarchy; when every "
  "agent follows simple local rules, the colony out-plans any commander."),
 "demo_kind": "colony_castes",
},
{
 "key": "social-bees-wasps", "name": "Social Insects: Bees and Wasps",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Bees and wasps (Hymenoptera) evolved eusociality repeatedly, from "
  "solitary hunters to superorganism colonies. Paper wasps (Polistes) "
  "show the flexible middle: small colonies where the dominant female "
  "becomes queen and subordinates may still reproduce. Honey bees (Apis "
  "mellifera) are the pinnacle of the annual-to-perennial spectrum: a "
  "colony of 20,000-60,000 workers, one queen laying up to 2,000 eggs a "
  "day, and seasonal drones. Workers progress through age castes — "
  "cleaner, nurse, builder, guard, forager — and communicate flower "
  "locations with the waggle dance. Bumble bees (Bombus) run annual "
  "colonies of a few hundred, founded each spring by a single overwintered "
  "queen. Stingless bees (Meliponini) of the tropics build elaborate "
  "resin-and-wax nests and defend with biting swarms. Solitary wasps "
  "remain master engineers: mud daubers build clay nurseries, digger "
  "wasps paralyze prey as living pantries for their larvae, and "
  "parasitoid wasps (the majority of Hymenoptera) lay eggs in or on "
  "other insects. The haplodiploid sex-determination system — females "
  "from fertilized eggs, males from unfertilized — makes full sisters "
  "75% related, repeatedly favoring the evolution of sterile worker "
  "castes that raise sisters instead of daughters."),
 "how_it_works": (
  "A honey bee colony functions as a single thermoregulating "
  "superorganism. In winter the cluster holds 20-30 C at its core while "
  "workers shiver their flight muscles; in summer, foragers fan water "
  "evaporation to cool the hive. The queen's mandibular pheromone "
  "suppresses worker ovary development and advertises her presence; if "
  "she fails, workers raise a new queen by flooding a larva with royal "
  "jelly. Foraging decisions are democratic: scout bees dance for "
  "candidate nest sites (during swarming) or flower patches, and the "
  "colony converges on the option with the most vigorous dancers — a "
  "quorum-sensing vote with no central tally. Defense is collective and "
  "costly: a worker's barbed stinger tears free and keeps pumping venom, "
  "killing the bee — economical only because the colony, not the "
  "individual, is the unit of selection. Solitary wasps show the "
  "ancestral program: each female is queen and worker in one, digging "
  "burrows, hunting, and sealing brood cells alone — eusociality "
  "evolved when daughters stayed home to help instead of dispersing."),
 "key_points": [
  "Eusociality evolved repeatedly: paper wasps (flexible) -> bumble bees (annual) -> honey bees (perennial)",
  "Honey bee colony: 20k-60k workers, queen lays ~2,000 eggs/day, age polyethism task schedule",
  "Waggle dance + quorum sensing: democratic foraging and nest-site votes",
  "Queen mandibular pheromone suppresses worker reproduction; royal jelly makes queens",
  "Haplodiploidy: sisters 75% related — the repeated genetic basis of worker castes",
  "Solitary wasps: master engineers (mud daubers, digger wasps); parasitoids dominate the order",
 ],
 "requirements": [
  "Honey bee age-caste timeline",
  "Waggle dance decoding diagram",
 ],
 "standards": [
  "Social-insect terminology per Resh & Cardé (2009)",
 ],
 "citations": [CIT_RESH, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: democracy without ballots — dances vote, quorums "
  "decide, and the barbed stinger proves the unit of selection is the "
  "colony. Manon's Signature take: when the mission outlives the agent, "
  "optimize for the collective; individual sacrifice becomes cheap."),
 "demo_kind": "waggle_dance",
},
{
 "key": "pollination-ecology", "name": "Pollination Ecology",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Pollination — the transfer of pollen from anther to stigma — is the "
  "deal insects struck with flowering plants 140 million years ago, and "
  "it now underpins most terrestrial ecosystems and a third of human "
  "food. About 87% of flowering plant species depend on animal "
  "pollinators, the great majority insects: bees (the premier "
  "pollinators, with branched body hairs that trap pollen and floral "
  "constancy that keeps them loyal to one species per trip), "
  "butterflies and moths, flies (hover flies are major pollinators; "
  "midges pollinate cacao — no midges, no chocolate), beetles (the "
  "original pollinators of magnolias and other ancient flowers), and "
  "wasps (fig wasps and figs are locked in a 80-million-year obligate "
  "mutualism: each of ~750 fig species has its own wasp species). "
  "Pollination syndromes match flowers to couriers: bee flowers are "
  "blue/yellow with nectar guides and landing platforms; moth flowers "
  "are white, tubular, night-scented; bird flowers are red and odorless "
  "(bees cannot see red well); wind-pollinated flowers are small, green, "
  "and scentless with feathery stigmas. The economic value of insect "
  "pollination to global agriculture is estimated at hundreds of "
  "billions of dollars annually — almonds, apples, blueberries, and "
  "squash are essentially bee-dependent. Pollinator declines from "
  "pesticides, habitat loss, parasites (Varroa mites), and disease now "
  "threaten both wild ecosystems and food security."),
 "how_it_works": (
  "Pollination works through the pollinator's foraging economics. A bee "
  "visits flowers to collect nectar (fuel) and pollen (protein for "
  "larvae); pollen grains stick to branched hairs and the bee grooms "
  "most into pollen baskets (corbiculae), but enough grains remain on "
  "the body to dust the next flower's stigma. Floral constancy — a "
  "forager's habit of visiting one plant species per trip — makes bees "
  "efficient pollen couriers rather than random dust-movers. Flowers "
  "pay with nectar secreted from nectaries, and advertise with color "
  "(including UV nectar guides), scent bouquets, and shaped landing "
  "platforms; some orchids cheat, mimicking female bee pheromones or "
  "flower shapes without offering reward (sexual deception). "
  "Coevolution tightens the fit: long-tongued hawk moths and deep-"
  "tubed orchids (Darwin's famous predicted moth with a 30 cm tongue "
  "was found decades later), yucca moths that actively pack pollen "
  "into the yucca stigma and lay eggs in the flower — pollination "
  "mutualisms policed against cheating. At the landscape scale, "
  "pollination is a network: generalist bees link plant species "
  "together, and removing key pollinators cascades through the plant "
  "community."),
 "key_points": [
  "~87% of flowering plants need animal pollinators — mostly insects",
  "Bees: branched hairs + floral constancy = premier pollen couriers",
  "Syndromes: bee/moth/bird/beetle/wind flowers matched to courier senses",
  "Fig-fig wasp: ~750 species pairs in 80-million-year obligate mutualism",
  "Midges pollinate cacao; hover flies are major wild pollinators",
  "Economic value: hundreds of billions USD/year; declines threaten food security",
 ],
 "requirements": [
  "Pollination syndrome matching chart",
  "Flower-visitor observation protocol",
 ],
 "standards": [
  "Pollination terminology per Resh & Cardé (2009)",
 ],
 "citations": [CIT_RESH, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: the original logistics contract — courier paid in "
  "fuel, cargo delivered with loyalty (floral constancy). Manon's "
  "Signature take: the best delivery networks pay the courier in the "
  "cargo's own currency and reward repeat routes; loyalty is engineered, "
  "not hoped for."),
 "demo_kind": "pollination_value",
},
{
 "key": "insect-plant-herbivory", "name": "Insect-Plant Interactions: Herbivory",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Herbivorous insects eat plants, and plants fight back — the resulting "
  "arms race has generated much of Earth's biodiversity. About half of "
  "all insect species feed on plants, and most are specialists: the "
  "monarch caterpillar eats milkweed, the yucca moth's larva eats yucca "
  "seeds, and many leaf miners live inside a single host species' "
  "leaves. Plants defend with an arsenal: physical barriers (thorns, "
  "trichome hairs, tough cuticles, silica), chemical weapons (alkaloids "
  "like nicotine and caffeine, cyanogenic glycosides, tannins that bind "
  "proteins, latex that gums up mouthparts), and indirect defenses — "
  "releasing volatile distress signals that summon parasitoid wasps to "
  "attack the herbivore. Insects counter-adapt: monarchs sequester "
  "milkweed cardiac glycosides and become poisonous themselves, "
  "advertised by warning coloration; cabbage white caterpillars "
  "detoxify mustard oils with a specialized gut enzyme; some "
  "caterpillars cut leaf veins to drain latex before feeding. This "
  "coevolutionary escalation (Ehrlich & Raven, 1964) explains why "
  "closely related plants host closely related insects — they "
  "diversified together. Agriculture sits inside this war: crop pests "
  "are herbivores that escaped their coevolved controls, and pest "
  "management is applied chemical ecology."),
 "how_it_works": (
  "Feeding starts with host finding: herbivores read plant volatiles "
  "and surface chemistry with their antennae and tarsi ('tasting' with "
  "their feet, as butterflies do). Chewers shear tissue with mandibles; "
  "sap-suckers thread stylets to the phloem. Once feeding begins, the "
  "plant detects herbivore-associated molecular patterns in saliva and "
  "activates jasmonic-acid signaling, manufacturing defensive chemicals "
  "within hours (induced defense) — and emitting volatile organic "
  "compounds that recruit the herbivore's enemies (indirect defense: the "
  "'cry for help'). Specialists defeat specific defenses: the diamondback "
  "moth's gut sulfatase disarms mustard-oil bombs; monarch Na+/K+-ATPase "
  "mutations confer resistance to milkweed toxins, which the caterpillar "
  "then stores in its own tissues. Generalists (like many grasshoppers) "
  "cope with mixed diets and broad detoxification enzymes (cytochrome "
  "P450s). The plant's ultimate defense is tolerance — regrowing lost "
  "tissue — which is why moderate herbivory rarely kills wild plants, "
  "while monoculture crops with no genetic diversity collapse under "
  "the same pressure."),
 "key_points": [
  "~50% of insects are herbivores; most are host-plant specialists",
  "Plant defenses: physical (trichomes, silica), chemical (alkaloids, tannins, latex), indirect (volatile SOS)",
  "Counter-adaptations: sequestration (monarch), detox enzymes (cabbage white), vein-cutting",
  "Ehrlich & Raven (1964): coevolutionary arms race drives joint diversification",
  "Induced defense via jasmonic acid; volatiles recruit parasitoid bodyguards",
  "Crop pests = herbivores escaped from coevolved controls",
 ],
 "requirements": [
  "Defense/counter-defense pairing chart",
  "Host-specificity examples (monarch-milkweed, yucca moth-yucca)",
 ],
 "standards": [
  "Coevolution terminology per standard ecological literature",
 ],
 "citations": [CIT_GULLAN, CIT_STD],
 "sig_lens": (
  "Signature reading: the longest-running arms race on Earth — every "
  "shield breeds a better spear. Manon's Signature take: never build a "
  "static defense; build a defense that learns, signals for help, and "
  "tolerates damage — the plant's three-layer doctrine."),
 "demo_kind": "herbivory_damage",
},
{
 "key": "beneficial-insects", "name": "Beneficial Insects: Predators and Parasitoids",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Most insects are not pests — the overwhelming majority are neutral "
  "or actively beneficial, and predators and parasitoids provide pest "
  "control worth billions of dollars annually, free of charge. Predators "
  "hunt and eat many prey: ladybird beetles and their larvae devour "
  "aphids (a single ladybird eats ~5,000 aphids in its lifetime); "
  "lacewing larvae ('aphid lions') impale prey with hollow jaws and "
  "suck them dry; ground beetles patrol soil at night; dragonflies take "
  "mosquitoes on the wing; praying mantids ambush anything that moves. "
  "Parasitoids — mostly tiny wasps and some flies — are more surgical: "
  "the female lays eggs in or on a single host insect, and her larva "
  "consumes it alive from the inside, killing it. Trichogramma wasps "
  "(smaller than a pinhead) parasitize moth eggs; Cotesia wasps inject "
  "caterpillars along with polydnaviruses that disable host immunity; "
  "tachinid flies glue eggs to caterpillars. Parasitoids are the most "
  "important natural enemies in agriculture — classical biological "
  "control (importing a pest's coevolved parasitoid) has permanently "
  "suppressed pests like the cassava mealybug across Africa, saving an "
  "estimated billions in crop losses. Conservation biological control — "
  "planting insectary strips of nectar flowers to feed adult parasitoids "
  "— recruits this free army on any farm."),
 "how_it_works": (
  "Predators find prey by vision, vibration, and chemical cues; many "
  "are generalists whose populations track prey density (a numerical "
  "response), creating boom-bust cycles described by Lotka-Volterra "
  "dynamics. Parasitoids are usually specialists with a precise host-"
  "finding sequence: long-range attraction to plant volatiles released "
  "by herbivore damage, short-range tracking of host frass or silk "
  "chemicals, then examination with the antennae and ovipositor probing. "
  "The ovipositor injects the egg plus venom and often symbiotic viruses "
  "(polydnaviruses) that shut down the host's encapsulation immune "
  "response; the larva then feeds strategically — consuming non-vital "
  "tissues first to keep the host alive and fresh, killing it only at "
  "the end (koinobiont strategy) — or paralyzes the host permanently "
  "first (idiobiont strategy). Hyperparasitoids parasitize the "
  "parasitoids, adding a fourth trophic level. Biological control "
  "programs exploit this: mass-rear Trichogramma by the billions on "
  "factitious hosts, release them timed to pest egg-laying, and measure "
  "parasitism rates to confirm establishment — a living, self-"
  "replicating pesticide."),
 "key_points": [
  "Predators (ladybirds, lacewings, ground beetles, dragonflies): many prey each, numerical response to prey density",
  "Parasitoids (mostly Hymenoptera + Tachinidae): one host per larva, consumed alive",
  "Host-finding sequence: plant volatiles -> host chemicals -> antennal exam -> oviposition",
  "Polydnaviruses disable host immunity; koinobiont vs idiobiont strategies",
  "Classical biocontrol: cassava mealybug suppressed across Africa by imported parasitoid",
  "Conservation biocontrol: nectar strips feed adult parasitoids on-farm",
 ],
 "requirements": [
  "Predator/parasitoid field ID images",
  "Parasitism-rate sampling protocol",
 ],
 "standards": [
  "Biological control terminology per Pedigo & Rice (2014)",
 ],
 "citations": [CIT_PEDIGO, CIT_GODFRAY],
 "sig_lens": (
  "Signature reading: the free security force — predators patrol "
  "generally, parasitoids assassinate specifically, and the whole system "
  "self-replicates. Manon's Signature take: before buying a weapon, "
  "check whether nature already deployed a better one for free; then "
  "feed it, house it, and let it work."),
 "demo_kind": "parasitoid_rates",
},
{
 "key": "insect-nervous-system", "name": "Insect Physiology: The Nervous System",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The insect nervous system is a decentralized command network: a brain "
  "in the head linked by a ventral nerve cord to a chain of segmental "
  "ganglia, each capable of running its local body region semi-"
  "independently. The brain (supraesophageal ganglion) has three fused "
  "regions — protocerebrum (vision, mushroom bodies for learning and "
  "memory), deutocerebrum (antennae), tritocerebrum (mouthparts) — "
  "connected around the esophagus to the subesophageal ganglion "
  "controlling mouthparts and neck. Down the cord, each thoracic ganglion "
  "drives its leg pair (and wings), each abdominal ganglion drives its "
  "segment — a headless cockroach can still walk, right itself, and "
  "even learn simple tasks, because the thoracic ganglia hold the "
  "walking programs. Mushroom bodies are the learning centers: honey "
  "bees form long-term memories of flower locations, colors, and scents "
  "there, and fruit flies learn to avoid odors paired with shocks. The "
  "system is fast despite tiny neurons: giant fiber escape circuits in "
  "cockroaches and flies fire in milliseconds, and the fly's haltere "
  "reflex arc corrects flight without brain involvement. Insect "
  "neurobiology underpins both pesticide design (most insecticides "
  "attack the nervous system) and bio-inspired robotics (the decentralized "
  "ganglion architecture is the model for hexapod robot controllers)."),
 "how_it_works": (
  "Neurons communicate by action potentials and chemical synapses, as in "
  "vertebrates, but the architecture is ventral and ganglionated. "
  "Sensory neurons feed each ganglion; interneurons integrate; motor "
  "neurons drive muscles. Central pattern generators — small networks "
  "that oscillate without input — produce the rhythmic leg movements of "
  "walking and the wingbeats of flight; sensory feedback tunes them. "
  "Neuromodulators (octopamine — the insect 'adrenaline'; dopamine; "
  "serotonin) switch behavioral states: octopamine triggers fight-or-"
  "flight arousal, and the locust's solitary-to-gregarious transformation "
  "is driven by serotonin. Learning is associative: in the mushroom "
  "bodies, Kenyon cells encode odors sparsely, and dopamine-reinforced "
  "synapses link odor to reward or punishment — the same circuit logic "
  "as vertebrate basal ganglia, evolved independently. Insecticides "
  "exploit this system: organophosphates block acetylcholinesterase "
  "(signal won't switch off), pyrethroids hold sodium channels open "
  "(nerves fire uncontrollably), neonicotinoids overstimulate nicotinic "
  "receptors — which is also why they harm bees at sublethal doses, "
  "impairing navigation memory."),
 "key_points": [
  "Brain (3 fused regions + mushroom bodies) + ventral cord + segmental ganglia",
  "Decentralized: thoracic ganglia run walking; headless cockroach still walks",
  "Mushroom bodies: learning/memory centers (bee flower memory, fly odor learning)",
  "Central pattern generators produce walking/flight rhythms; octopamine = arousal signal",
  "Giant-fiber escape circuits fire in milliseconds; haltere reflex bypasses the brain",
  "Most insecticides target this system (AChE, sodium channels, nicotinic receptors)",
 ],
 "requirements": [
  "Nervous system diagram (brain regions + ventral cord)",
  "Insecticide mode-of-action mapping",
 ],
 "standards": [
  "Neuroanatomical terminology per Chapman (2013)",
 ],
 "citations": [CIT_CHAPMAN, CIT_NORRIS],
 "sig_lens": (
  "Signature reading: command decentralized to the edge — each ganglion "
  "runs its territory, the brain handles strategy. Manon's Signature "
  "take: never route every decision through headquarters; push control "
  "to the segment closest to the action and keep the brain for learning."),
 "demo_kind": "neuron_speed",
},
{
 "key": "insect-reproduction", "name": "Insect Reproduction and Eggs",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Insect reproduction is a numbers game played with astonishing "
  "variety. Most insects reproduce sexually with internal fertilization: "
  "the male transfers sperm via an aedeagus, and the female stores it "
  "in a spermatheca, fertilizing eggs over days, months, or — in ant "
  "and honey bee queens — years from a single mating flight. Fecundity "
  "is extreme: a queen termite lays ~30,000 eggs a day, a house fly ~500 "
  "in a lifetime, a mosquito ~300 per blood meal. Eggs are laid with "
  "strategy: butterflies glue them singly under host leaves, mantids "
  "pack them in foamy oothecae, cockroaches carry the ootheca until "
  "hatching, and parasitoid wasps inject them into living hosts. Beyond "
  "standard sex, insects showcase reproductive oddities: aphids clone "
  "by parthenogenesis all summer (telescoping generations — embryos "
  "within embryos); honey bee workers can lay unfertilized eggs that "
  "become drones; some stick insects and weevils are entirely "
  "parthenogenetic with no males known; gall midges practice paedogenesis "
  "(larvae giving birth to larvae); and Strepsiptera males find females "
  "that never leave their host. Courtship is equally elaborate — "
  "firefly flash codes, cricket songs, butterfly pheromone perfumes, "
  "dance-fly nuptial gifts of silk-wrapped prey — because the female's "
  "choice drives sexual selection as powerfully as in any vertebrate."),
 "how_it_works": (
  "Oogenesis builds each egg with yolk (vitellogenin proteins from the "
  "fat body) and a protective chorion shell, often sculptured and with "
  "a micropyle pore for sperm entry. Mating systems revolve around "
  "sperm competition: males deliver sperm plus accessory-gland secretions "
  "that form mating plugs, manipulate female receptivity, or provide "
  "nuptial nutrition; females of many species mate multiply and bias "
  "fertilization toward preferred males (cryptic female choice), storing "
  "competing ejaculates in separate spermathecal compartments. "
  "Parthenogenesis types: apomixis (cloning, in aphids), automixis "
  "(meiosis followed by fusion, restoring diploidy), and androgenesis "
  "(rare). Haplodiploidy in Hymenoptera gives precise sex control — the "
  "queen chooses per egg whether to release stored sperm. "
  "Environmental sex determination is rare in insects, but nutrition "
  "sets caste in social species (royal jelly -> queen). The payoff of "
  "high fecundity is demographic resilience: even 99% mortality leaves "
  "a mosquito population growing, which is why control must target "
  "reproduction itself (sterile insect technique, mating disruption) "
  "rather than just killing adults."),
 "key_points": [
  "Internal fertilization; spermatheca stores sperm for months to years",
  "Fecundity: termite queen ~30,000 eggs/day; mosquito ~300 per blood meal",
  "Egg strategies: singly glued, oothecae, carried, injected into hosts",
  "Parthenogenesis (aphids), haplodiploidy (Hymenoptera), paedogenesis (gall midges)",
  "Sperm competition + cryptic female choice shape mating systems",
  "High fecundity = demographic resilience; control must target reproduction",
 ],
 "requirements": [
  "Reproductive strategy comparison chart",
  "Ootheca and egg-mass images",
 ],
 "standards": [
  "Reproductive terminology per Gullan & Cranston (2014)",
 ],
 "citations": [CIT_GULLAN, CIT_RESH],
 "sig_lens": (
  "Signature reading: reproduction as strategy portfolio — store "
  "resources (sperm), clone when winning (aphids), invest heavily when "
  "established (queens). Manon's Signature take: match the reproductive "
  "strategy to the environment's stability; clone the winners, diversify "
  "the bets."),
 "demo_kind": "fecundity_table",
},
{
 "key": "insect-migration", "name": "Insect Migration",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Insect migration moves biomass on a continental scale — trillions of "
  "individuals riding seasonal winds between breeding and overwintering "
  "grounds. The monarch butterfly (Danaus plexippus) is the icon: "
  "eastern North American monarchs fly up to 4,000 km to a few "
  "mountain forests in Mexico, navigating by a time-compensated sun "
  "compass calibrated against polarized skylight, with the antennae's "
  "circadian clocks correcting for the sun's movement; no single "
  "butterfly makes the round trip — it takes 3-4 generations, yet the "
  "great-grandchildren find the same groves. Desert locusts ride winds "
  "hundreds of kilometers in swarms of billions, tracking rains. The "
  "painted lady (Vanessa cardui) migrates in a multi-generational "
  "circuit from Africa to Europe and back — up to 12,000-14,000 km "
  "round trip, the longest known insect migration. Bogong moths "
  "aestivate in Australian alpine caves by the millions. Dragonflies "
  "like the globe skimmer (Pantala flavescens) cross the Indian Ocean, "
  "riding monsoon winds between India and Africa — possibly the longest "
  "regular insect ocean crossing. Migration is distinguished from "
  "dispersal by its persistence, straightness, and seasonal timing, "
  "often triggered by photoperiod and juvenile hormone changes that "
  "switch the insect into a migratory physiological state (oogenesis "
  "paused, flight muscles built, fat loaded)."),
 "how_it_works": (
  "Migratory physiology is a distinct syndrome: juvenile hormone drops, "
  "reproduction pauses, flight muscles hypertrophy, and fat body loads "
  "fuel — the insect becomes a flying fuel tank. Navigation combines "
  "multiple compasses: the sun compass (with circadian time compensation "
  "so a 3 PM sun bearing is read correctly), the polarized-light sky "
  "compass (dorsal rim ommatidia), and in some species a magnetic "
  "compass (magnetite-based or radical-pair). Monarchs integrate these "
  "in the central complex of the brain; clock-shift experiments (shifting "
  "the antennae's circadian clock by 6 hours) rotate their flight "
  "direction by ~90 degrees, proving the time-compensated mechanism. "
  "Most migrants cheat the wind: high-altitude nocturnal migrants "
  "(moths, locusts) ascend into fast air streams and ride them, "
  "steering only to stay in the flow — radar studies show locust "
  "swarms aligning downwind at altitude. Stopover ecology matters as "
  "much as flight: migrants refuel at nectar corridors (monarchs on "
  "fall wildflowers) or seasonal flushes, and habitat loss at any "
  "node collapses the whole circuit — the monarch's decline traces to "
  "milkweed loss in breeding grounds and logging at overwintering sites."),
 "key_points": [
  "Monarch: up to 4,000 km to Mexican groves; 3-4 generations per round trip",
  "Painted lady: up to ~14,000 km Africa-Europe circuit — longest insect migration",
  "Globe skimmer dragonfly crosses the Indian Ocean on monsoon winds",
  "Time-compensated sun compass + polarized skylight + magnetic cues; antennae hold the clock",
  "Migratory syndrome: JH drop, reproduction paused, flight muscle + fat loaded",
  "Wind-riding at altitude; stopover habitat loss collapses migration circuits",
 ],
 "requirements": [
  "Migration route maps (monarch, painted lady)",
  "Sun-compass mechanism diagram",
 ],
 "standards": [
  "Migration terminology per Resh & Cardé (2009)",
 ],
 "citations": [CIT_RESH, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: the relay expedition — no individual finishes the "
  "journey, but the lineage never misses the destination. Manon's "
  "Signature take: encode the destination in the system, not the "
  "traveler; build relays where each generation inherits the compass "
  "and the route."),
 "demo_kind": "migration_distance",
},
{
 "key": "collection-identification", "name": "Collection and Identification Methods",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Entomology is a specimen science: identification, taxonomy, and "
  "monitoring all depend on collecting insects correctly. Active methods: "
  "the sweep net (standardized arcs through vegetation for grassland "
  "insects), the aerial net (butterflies, dragonflies), beating sheets "
  "(jarring branches over a sheet for canopy arthropods), aspirators "
  "(pooters) for tiny specimens, and hand-picking with forceps. Passive "
  "methods: pitfall traps (cups sunk in soil for ground beetles, ants), "
  "Malaise traps (tent-like intercept traps — the workhorse of "
  "biodiversity surveys), light traps (UV/blacklight for nocturnal "
  "moths and beetles), pan traps (colored bowls for bees and flies), "
  "pheromone traps (species-specific monitoring of pests like codling "
  "moth), and Berlese funnels (heat-extracting soil microarthropods). "
  "Killing and preservation: ethyl acetate jars for most insects; "
  "pinning through the thorax (with the pin at standardized heights on "
  "setting boards) for beetles, bugs, and moths; minuten pins for tiny "
  "specimens; ethanol (95%) for soft-bodied insects, larvae, and DNA "
  "work; slide-mounting for aphids, thrips, and mites. Every specimen "
  "gets a label: locality (GPS), date, collector, habitat, method — "
  "without data, a specimen is scientifically worthless. Identification "
  "then runs through dichotomous keys, reference collections, and "
  "increasingly DNA barcoding and image-recognition AI. Ethical and "
  "legal practice: collect only what the study needs, never take "
  "protected species, and secure permits for parks and reserves."),
 "how_it_works": (
  "Each trap exploits an insect behavior. Pitfall traps intercept "
  "ground-runners that fall in and cannot climb out (a little propylene "
  "glycol preserves them). Malaise traps exploit the upward-flight "
  "reflex: insects hitting the mesh climb toward the light and funnel "
  "into the collecting head — running one trap for a season can sample "
  "thousands of species. Light traps exploit positive phototaxis; "
  "mercury-vapor and UV LEDs each attract different assemblages. "
  "Pheromone traps exploit mate-finding: a synthetic lure draws males "
  "of one species, giving precise population monitoring for IPM "
  "decisions. Standardization makes catches comparable: sweep-netting "
  "uses fixed arc counts, pitfall arrays use fixed trap-nights, and "
  "Malaise samples are reported per trap-day. In the lab, relaxing "
  "chambers (humid jars) soften dried specimens for pinning; spreading "
  "boards set wings symmetrically; and genitalia dissection (clearing "
  "in KOH) reveals the species-specific structures that separate "
  "lookalike species — in many groups, only the genitalia diagnose the "
  "species. Modern surveys pair morphology with COI barcoding: one leg "
  "yields a DNA sequence matched against reference libraries (BOLD), "
  "flagging cryptic species the eye cannot split."),
 "key_points": [
  "Active: sweep nets, aerial nets, beating sheets, aspirators, hand-picking",
  "Passive: pitfalls, Malaise traps, light traps, pan traps, pheromone traps, Berlese funnels",
  "Preservation: pinning (standard heights), ethanol 95% (DNA/larvae), slide-mounting (micro-insects)",
  "Every specimen needs full data labels (GPS, date, collector, habitat, method)",
  "ID pipeline: dichotomous keys -> reference collections -> genitalia dissection -> DNA barcoding",
  "Standardized effort (trap-nights, sweep counts) makes catches comparable",
 ],
 "requirements": [
  "Trap-type reference images",
  "Label format template and pinning-height standard",
  "Permits for protected areas (legal requirement)",
 ],
 "standards": [
  "Collection standards per Triplehorn & Johnson (2005)",
  "Nomenclature and voucher practice per ICZN",
 ],
 "citations": [CIT_TRIPLEHORN, CIT_STD],
 "sig_lens": (
  "Signature reading: sample the world with behavior-exploiting sensors, "
  "then label every capture with full provenance — data without "
  "provenance is noise. Manon's Signature take: standardize the trap, "
  "standardize the label, and the collection becomes a permanent "
  "instrument, not a pile of bugs."),
 "demo_kind": "trap_counts",
},
]

# ------------------------------------------------------------------ ADVANCED
ENTRIES += [
{
 "key": "ipm", "name": "Integrated Pest Management",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Integrated Pest Management (IPM) is the decision framework for "
  "controlling pests with minimum cost and collateral damage: monitor "
  "pests, act only when they exceed the economic threshold, and combine "
  "tactics — biological, cultural, mechanical, and chemical — so no "
  "single method bears the whole load. The core economics: the Economic "
  "Injury Level (EIL) is the pest density where damage value equals "
  "control cost (EIL = C / (V x D x K), with C = control cost, V = crop "
  "value, D = damage per pest, K = control efficacy); the Economic "
  "Threshold (ET) is the lower density that triggers action, set below "
  "the EIL to leave response time. IPM tactics stack: cultural controls "
  "(crop rotation, resistant varieties, planting dates, sanitation), "
  "biological controls (conserved predators, released parasitoids, "
  "microbial Bt), mechanical controls (traps, barriers, vacuuming), "
  "behavioral controls (mating disruption with pheromones, sterile "
  "insect technique), and chemical controls as the last resort — "
  "selective, timed, and rotated to slow resistance. Monitoring is the "
  "engine: pheromone traps, sweep counts, and degree-day models tell the "
  "manager exactly when the ET is crossed. IPM programs have cut "
  "insecticide use 50-90% in crops from cotton to apples while holding "
  "yields — proof that knowledge substitutes for chemistry."),
 "how_it_works": (
  "An IPM program runs as a seasonal loop. First, identify the key pests "
  "and their natural enemies in the crop system, and establish sampling "
  "plans (e.g., 100 sweeps per field for lygus bugs, pheromone trap "
  "counts per week for codling moth). Second, compute or adopt "
  "thresholds: the ET for each pest-stage-crop combination, adjusted for "
  "crop value and control cost that season. Third, scout on schedule and "
  "record densities against thresholds — no spray without a number. "
  "Fourth, when the ET is crossed, select the tactic with the best "
  "efficacy-to-disruption ratio: release Trichogramma against moth eggs, "
  "apply Bt against young caterpillars, disrupt mating with pheromone "
  "dispensers, or spray a selective insecticide timed to the vulnerable "
  "stage. Fifth, evaluate: did the treatment work, what did it cost, "
  "what happened to beneficials — and update next year's plan. "
  "Degree-day models sharpen timing: each pest needs a known heat sum "
  "to reach the vulnerable stage, so trap biofix + weather data predicts "
  "the spray window days ahead. Resistance management is built in: "
  "rotate modes of action (IRAC groups), preserve refuges of "
  "susceptible pests (the Bt-cotton refuge strategy), and never spray "
  "on a calendar — calendar sprays are how resistance and secondary "
  "pest outbreaks are manufactured."),
 "key_points": [
  "EIL = C/(V*D*K): spray only when damage value exceeds control cost; ET set below EIL",
  "Tactic stack: cultural + biological + mechanical + behavioral + chemical (last resort)",
  "Monitoring engine: pheromone traps, sweep counts, degree-day models",
  "Mating disruption and sterile insect technique control reproduction, not just numbers",
  "Resistance management: rotate IRAC modes of action; maintain susceptible refuges",
  "Documented 50-90% insecticide reductions with yields held",
 ],
 "requirements": [
  "Pest ID + sampling plan per crop",
  "Pheromone traps and degree-day calculator",
  "Threshold tables (ET per pest-stage-crop)",
 ],
 "standards": [
  "IPM framework per Pedigo & Rice (2014)",
  "IRAC mode-of-action rotation guidelines",
 ],
 "citations": [CIT_PEDIGO, CIT_STD],
 "sig_lens": (
  "Signature reading: warfare by accounting — every shot must pay for "
  "itself (EIL), every tactic covers the others' weaknesses, and "
  "intelligence (monitoring) replaces firepower. Manon's Signature take: "
  "never fight on a schedule; fight on a threshold, with combined arms."),
 "demo_kind": "ipm_threshold",
},
{
 "key": "agricultural-entomology", "name": "Agricultural Entomology: Crop Pests",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Agricultural entomology studies the insects that eat crops — and the "
  "arthropod allies that protect them. Globally, arthropod pests destroy "
  "an estimated 18-26% of potential crop production, worth hundreds of "
  "billions of dollars, with the heaviest losses in the tropics. The "
  "major guilds: chewing defoliators (armyworms, cutworms, Colorado "
  "potato beetle — the beetle that defeated arsenicals, DDT, and dozens "
  "of insecticides in sequence); sap-suckers (aphids, whiteflies, "
  "planthoppers — which also vector plant viruses); borers (European "
  "corn borer, stem borers tunneling inside stalks); fruit feeders "
  "(codling moth, fruit flies); soil pests (wireworms, white grubs, "
  "rootworms — the western corn rootworm costs US corn ~$1-2 billion "
  "yearly); and storage pests (weevils, grain moths eating harvested "
  "grain). Invasive species repeatedly rewrite the map: the fall "
  "armyworm (Spodoptera frugiperda) reached Africa in 2016 and Asia by "
  "2018, threatening maize for hundreds of millions; the spotted "
  "lanternfly spreads through North American vineyards and orchards. "
  "Modern agricultural entomology answers with resistant varieties "
  "(Bt crops expressing bacterial toxins), precision monitoring, "
  "biological control, and IPM — because the treadmill of broad-"
  "spectrum insecticides reliably produces resistance, resurgence, and "
  "secondary pests."),
 "how_it_works": (
  "Pest status emerges from ecology, not evil: monocultures provide "
  "unlimited host plants, no plant diversity for natural enemies, and "
  "uniform microclimates — an all-you-can-eat buffet with the guards "
  "removed. Sap-suckers damage crops doubly: direct sap removal plus "
  "virus transmission (whitefly-transmitted begomoviruses devastate "
  "tomatoes; aphid-transmitted potyviruses hit legumes) — a few viruliferous "
  "insects can ruin a field, which is why virus-vector thresholds are "
  "near zero. Borers escape contact insecticides inside plant tissue, "
  "so control targets the brief egg-hatch window (degree-day timed) or "
  "uses systemic/ transgenic toxins (Bt Cry proteins that perforate the "
  "larval gut). Soil pests are fought with crop rotation (rootworm "
  "larvae starve without corn roots), entomopathogenic nematodes, and "
  "seed treatments. Invasion biology drives quarantine: pest risk "
  "analysis, pheromone-trap detection grids at ports, and eradication "
  "campaigns (sterile insect technique wiped the screwworm from North "
  "America; male-annihilation traps target fruit flies). Bt crops work "
  "by high-dose/refuge strategy — plants express enough toxin to kill "
  "heterozygous resistant insects, while nearby non-Bt refuges maintain "
  "susceptible mates, diluting resistance genes."),
 "key_points": [
  "Arthropod pests destroy ~18-26% of potential crop production globally",
  "Guilds: defoliators, sap-suckers (+ virus vectors), borers, fruit feeders, soil pests, storage pests",
  "Virus vectors need near-zero thresholds — a few insects can ruin a field",
  "Monoculture creates pest status: unlimited hosts, no enemy habitat",
  "Bt crops + high-dose/refuge strategy delay resistance",
  "Invasives (fall armyworm, spotted lanternfly) met with quarantine + detection grids + SIT",
 ],
 "requirements": [
  "Pest guild ID guide for the crop",
  "Degree-day models for borer egg-hatch windows",
  "Quarantine/detection protocols for invasives",
 ],
 "standards": [
  "Pest management per Pedigo & Rice (2014)",
 ],
 "citations": [CIT_PEDIGO, CIT_STD],
 "sig_lens": (
  "Signature reading: the pest is a symptom of the system's design — "
  "monoculture manufactures its own enemies. Manon's Signature take: "
  "redesign the field (diversity, refuges, resistant varieties) before "
  "reaching for the sprayer; the cheapest pest control is ecology."),
 "demo_kind": "pest_loss",
},
{
 "key": "medical-entomology", "name": "Medical and Veterinary Entomology: Vectors",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Medical entomology studies the arthropods that transmit disease — "
  "vectors — plus the ones that bite, sting, or parasitize directly. "
  "Vector-borne diseases kill over 700,000 people yearly; mosquitoes "
  "alone (Anopheles transmitting malaria, Aedes transmitting dengue, "
  "Zika, chikungunya, yellow fever, Culex transmitting West Nile) are "
  "the deadliest animals to humans in history. The vector roster: ticks "
  "(Lyme disease, Rocky Mountain spotted fever, tick-borne encephalitis "
  "— ticks transmit the widest variety of pathogens of any vector); "
  "tsetse flies (African sleeping sickness); sandflies (leishmaniasis); "
  "kissing bugs (Chagas disease); blackflies (river blindness/ "
  "onchocerciasis); fleas (plague, murine typhus); lice (epidemic "
  "typhus, trench fever). Transmission modes: biological (pathogen "
  "develops or multiplies in the vector — malaria sporozoites in "
  "mosquito salivary glands), mechanical (pathogen hitchhikes on "
  "mouthparts — less common), and vertical (mother to offspring). "
  "Veterinary entomology covers the same for livestock: screwworms, "
  "cattle ticks (babesiosis), stable flies, and myiasis-causing "
  "bot flies cost animal agriculture billions. Control blends vector "
  "suppression (insecticide-treated bed nets, indoor residual spraying, "
  "larval source reduction), personal protection, vaccines where they "
  "exist, and genetic approaches (Wolbachia-infected Aedes that block "
  "dengue; gene-drive mosquitoes under evaluation)."),
 "how_it_works": (
  "Vectorial capacity — the daily rate at which future infections arise "
  "from one case — depends on vector density, biting rate, vector "
  "competence (can the pathogen develop in this species?), and daily "
  "survival rate, with survival entering exponentially: a mosquito must "
  "live through the pathogen's extrinsic incubation period (10-14 days "
  "for malaria) to transmit, so small reductions in adult longevity "
  "crash transmission — the mathematical basis of bed nets and indoor "
  "spraying. The basic reproduction number R0 for vector-borne disease "
  "scales with the square of the biting rate (the mosquito bites twice: "
  "once to acquire, once to transmit), which is why biting-rate "
  "reduction is so powerful. Biological transmission requires "
  "pathogen-vector molecular compatibility: Plasmodium ookinetes must "
  "cross the mosquito midgut, evade its immune system, and reach the "
  "salivary glands — most mosquito species are refractory to most "
  "Plasmodium species. Wolbachia biocontrol exploits cytoplasmic "
  "incompatibility: released Wolbachia-carrying males sterilize wild "
  "females' eggs, or Wolbachia-infected females spread a dengue-"
  "blocking symbiont through the population. Surveillance runs on "
  "trap networks (CDC light traps, gravid traps, ovitraps), human "
  "landing catches where ethical, and molecular xenomonitoring of "
  "caught vectors for pathogen RNA."),
 "key_points": [
  "Vectors kill 700,000+/year; mosquitoes are history's deadliest animals to humans",
  "Key vectors: Anopheles/Aedes/Culex mosquitoes, ticks, tsetse, sandflies, kissing bugs, blackflies, fleas, lice",
  "Biological transmission: pathogen develops in vector; survival through incubation is the bottleneck",
  "R0 scales with biting-rate squared — biting reduction is disproportionately powerful",
  "Control: bed nets, indoor residual spraying, source reduction, Wolbachia, gene drives",
  "Veterinary vectors (screwworm, cattle ticks, stable flies) cost livestock agriculture billions",
 ],
 "requirements": [
  "Vector ID keys (mosquito genera, tick species)",
  "Trap network protocol (light traps, gravid traps, ovitraps)",
  "Personal protection standards for field work",
 ],
 "standards": [
  "Vector surveillance per WHO guidance",
 ],
 "citations": [CIT_RESH, CIT_STD],
 "sig_lens": (
  "Signature reading: the vector is a logistics network for pathogens — "
  "break the network at its exponential bottleneck (adult survival), not "
  "at its strongest point. Manon's Signature take: find the term that "
  "enters the equation exponentially and attack exactly there."),
 "demo_kind": "vector_r0",
},
{
 "key": "insecticide-resistance", "name": "Insecticide Modes of Action and Resistance",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Insecticides are neurotoxins, growth regulators, and metabolic "
  "poisons classified by mode of action under the IRAC system (32+ "
  "groups). The classics: organophosphates and carbamates (block "
  "acetylcholinesterase — the nerve signal cannot switch off); "
  "pyrethroids (hold voltage-gated sodium channels open — nerves fire "
  "uncontrollably; derived from chrysanthemum flowers); neonicotinoids "
  "(overstimulate nicotinic acetylcholine receptors — systemic, seed-"
  "applied, and implicated in bee harm); organochlorines like DDT "
  "(sodium-channel, largely banned). Newer groups: diamides (ryanodine "
  "receptor — paralyze muscles), spinosyns (fermentation-derived, "
  "nicotinic/GABA), insect growth regulators (juvenile hormone mimics "
  "and chitin-synthesis inhibitors — the insect cannot molt correctly), "
  "and microbials (Bt Cry toxins perforating the larval gut; "
  "entomopathogenic fungi like Beauveria). Resistance — the evolved "
  "ability to survive insecticides — is universal where selection is "
  "intense: mechanisms include target-site mutations (kdr sodium-channel "
  "mutation vs. pyrethroids/DDT), metabolic detoxification (upregulated "
  "P450s, esterases, GSTs), reduced penetration (thicker cuticle), and "
  "behavioral avoidance. The Colorado potato beetle resists 50+ "
  "compounds; malaria mosquitoes resist pyrethroids across Africa. "
  "Management: rotate IRAC groups, mix modes of action, preserve "
  "refuges, and never rely on chemistry alone."),
 "how_it_works": (
  "Resistance evolves by selection on standing genetic variation. A "
  "field population carries rare resistant alleles (e.g., the kdr "
  "mutation L1014F in the sodium channel); each insecticide application "
  "kills susceptibles and leaves resistants to breed — the resistance "
  "ratio (LC50 resistant / LC50 susceptible) climbs from 1x to 10x, "
  "100x, 1000x over seasons. Metabolic resistance works by gene "
  "amplification or upregulation: extra esterase enzymes sequester or "
  "cleave the insecticide before it reaches the target. Cross-resistance "
  "occurs when one mechanism defeats multiple chemicals (kdr protects "
  "against both DDT and pyrethroids); multiple resistance stacks "
  "independent mechanisms. The high-dose/refuge strategy (Bt crops) "
  "works genetically: the plant dose kills heterozygotes (resistance "
  "is functionally recessive), and refuge-grown susceptibles mate with "
  "rare resistant survivors, keeping resistance alleles heterozygous "
  "and ineffective. Monitoring uses discriminating-dose bioassays and "
  "molecular diagnostics (PCR for kdr alleles). When resistance is "
  "confirmed, the response is to rotate to an unrelated IRAC group, "
  "add a synergist (e.g., PBO blocking P450s), or switch tactics "
  "entirely (biological, behavioral) — repeating the failed chemistry "
  "only selects harder."),
 "key_points": [
  "IRAC groups: organophosphates/carbamates (AChE), pyrethroids (Na channels), neonics (nAChR), diamides, IGRs, Bt microbials",
  "Resistance mechanisms: target-site mutation (kdr), metabolic detox (P450/esterase), penetration, behavior",
  "Selection drives resistance ratios from 1x to 1000x+ over seasons",
  "Cross-resistance (kdr vs DDT + pyrethroids); multiple resistance stacks mechanisms",
  "High-dose/refuge keeps resistance functionally recessive",
  "Monitor with discriminating-dose bioassays + kdr PCR; rotate IRAC groups on confirmation",
 ],
 "requirements": [
  "IRAC mode-of-action chart",
  "Discriminating-dose bioassay protocol",
 ],
 "standards": [
  "IRAC mode-of-action classification",
  "Resistance monitoring per WHO/FAO protocols",
 ],
 "citations": [CIT_PEDIGO, CIT_STD],
 "sig_lens": (
  "Signature reading: every weapon breeds its own countermeasure — "
  "selection is the enemy's R&D department. Manon's Signature take: "
  "rotate arsenals, keep the enemy's susceptible genes alive in refuges, "
  "and never let one weapon become the whole strategy."),
 "demo_kind": "resistance_ratio",
},
{
 "key": "stored-product-entomology", "name": "Stored-Product Entomology",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Stored-product entomology protects harvested grain, flour, dried "
  "fruit, nuts, and processed foods from the insects that eat them "
  "after harvest — post-harvest losses to insects reach 10-20% in "
  "tropical storage systems. The primary pests attack whole grain: the "
  "rice weevil and granary weevil (Sitophilus spp.) drill into kernels "
  "and develop inside; the lesser grain borer chews through kernels "
  "and packaging. Secondary pests attack damaged grain, flour, and "
  "processed goods: the red flour beetle (Tribolium castaneum — also a "
  "genetics model organism), sawtoothed grain beetle, cigarette beetle, "
  "drugstore beetle, and the Indianmeal moth (Plodia interpunctella), "
  "whose webbing in pantry goods announces infestation. Damage is "
  "physical (weight loss, broken kernels), qualitative (contamination "
  "with frass, webbing, and insects — flour with insect fragments "
  "violates food law), and thermal: insect respiration heats and "
  "moistens grain bulks, triggering hot spots and mold. Management is "
  "IPM for buildings: sanitation (the foundation — clean bins starve "
  "pests), drying grain below ~13% moisture, aeration cooling, "
  "monitoring with probe traps and pheromone lures, hermetic storage "
  "(sealed bags where insect respiration depletes oxygen), diatomaceous "
  "earth, and fumigation (phosphine) as the last resort — with "
  "phosphine resistance now widespread requiring resistance monitoring. "
  "HACCP-style food safety plans treat stored-product insects as "
  "physical contaminants with legal defect action levels."),
 "how_it_works": (
  "Infestation dynamics are exponential: one mated female weevil lays "
  "~300 eggs inside kernels; at 30 C the generation time is ~4 weeks, "
  "so a few founders become thousands within months — the mathematics "
  "of neglect. Detection uses probe traps pushed into grain (capturing "
  "wandering adults), pheromone-baited sticky traps for moths "
  "(Indianmeal moth, Mediterranean flour moth), and temperature cables "
  "that reveal hot spots from insect respiration. Hermetic storage "
  "works by biology: sealed in airtight bags or cocoons, insects and "
  "grain respire the oxygen down below ~2-3%, and the pests asphyxiate "
  "— no chemistry needed, ideal for smallholders. Phosphine fumigation "
  "requires gas-tight sealing and multi-day exposure at monitored "
  "concentrations; resistance (first confirmed in the 1970s, now "
  "global) is managed by ensuring full label rates and exposure times — "
  "under-dosing selects resistance fastest. Heat treatment (raising "
  "facility temperature to 50-60 C for 24+ hours) kills all stages "
  "without chemicals and is standard in flour mills. Prevention "
  "dominates: clean harvest equipment, seal cracks, rotate stock "
  "first-in-first-out, and cool grain with aeration — insects develop "
  "slowly below 18 C and stop below ~13 C."),
 "key_points": [
  "Post-harvest insect losses: 10-20% in tropical storage systems",
  "Primary pests (weevils, lesser grain borer) attack whole kernels; secondary pests (flour beetles, moths) attack milled goods",
  "Damage: weight loss + contamination (legal defect levels) + respiration hot spots and mold",
  "Exponential growth: one female -> thousands in months at warm temperatures",
  "Hermetic storage asphyxiates pests below ~2-3% O2 — no chemistry",
  "Phosphine resistance is global; full rates + exposure times are mandatory; heat treatment is the chemical-free alternative",
 ],
 "requirements": [
  "Probe traps + pheromone lures + temperature cables",
  "Moisture meter (keep grain below ~13%)",
  "Gas-tight sealing capability for fumigation",
 ],
 "standards": [
  "Food safety defect action levels (FDA) for insect contamination",
 ],
 "citations": [CIT_PEDIGO, CIT_STD],
 "sig_lens": (
  "Signature reading: the harvest is not finished at the field edge — "
  "storage is the second battlefield, and sanitation is the cheapest "
  "fortification. Manon's Signature take: seal it, cool it, dry it, "
  "monitor it; chemistry is the last resort, not the plan."),
 "demo_kind": "storage_loss",
},
{
 "key": "forensic-entomology", "name": "Forensic Entomology",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Forensic entomology uses insects to answer legal questions — most "
  "famously, estimating the postmortem interval (PMI, time since death) "
  "from the insects colonizing a body. Blow flies (Calliphoridae) find "
  "a corpse within minutes and lay eggs; the larvae (maggots) develop "
  "through three instars at temperature-dependent rates, so the oldest "
  "specimens' developmental stage — converted via accumulated degree "
  "days (ADD/ADH) — gives a minimum PMI accurate to hours or days in "
  "the first weeks. As decomposition advances, a predictable succession "
  "arrives: blow flies, then flesh flies, then hide beetles "
  "(Dermestidae) and clown beetles (Histeridae) on dried remains, then "
  "clothes moths on hair — each wave timestamping longer PMIs up to "
  "months or years. Forensic entomologists also detect drugs and "
  "poisons in maggot tissues (entomotoxicology — when blood and organs "
  "are gone, maggots retain the chemistry), determine whether a body "
  "was moved (mismatched local fauna), and estimate neglect timelines "
  "in myiasis cases. The discipline demands rigorous chain of custody: "
  "live larvae reared to adults for definitive species ID (many "
  "maggots are indistinguishable as larvae), temperature data from "
  "the scene, and voucher specimens preserved in ethanol."),
 "how_it_works": (
  "The degree-day model converts development to thermal time. Each "
  "species has a lower developmental threshold (e.g., ~6 C for the "
  "common green bottle fly Lucilia sericata); each hour above it "
  "accumulates degree-hours toward the known thermal constant for "
  "each life stage (egg hatch, instar transitions, pupariation). The "
  "entomologist collects the oldest larvae at the scene, measures "
  "their instar (posterior spiracle slits: 1, 2, or 3 per instar), "
  "rears subsamples to adults to confirm species, pulls scene "
  "temperature data (or a nearby weather station corrected for the "
  "microclimate), and sums degree-hours backward from collection to "
  "find when the eggs were laid — colonization typically begins "
  "within minutes to hours of death in open conditions. Succession "
  "analysis extends the clock: the presence of late-arriving dermestid "
  "beetles with no blow fly larvae remaining indicates months. "
  "Entomotoxicology works because maggots bioaccumulate drugs from "
  "tissue — cocaine, for instance, accelerates maggot development, "
  "which must be corrected for or the PMI underestimates. Courts "
  "admit the testimony under standard scientific-evidence rules, so "
  "methods, error rates, and scene documentation must be publication-"
  "grade."),
 "key_points": [
  "Blow flies colonize within minutes; larval instar + degree-days = minimum PMI",
  "Accumulated degree hours above the species' developmental threshold convert stage to time",
  "Succession waves (blow flies -> flesh flies -> dermestids -> clothes moths) timestamp months",
  "Entomotoxicology: maggots retain drugs/poisons after tissues are gone",
  "Species ID by rearing larvae to adults; scene temperature data is mandatory",
  "Moved bodies betrayed by mismatched local fauna",
 ],
 "requirements": [
  "Rearing chambers for larval grow-out",
  "Scene temperature loggers + weather-station correction",
  "Chain-of-custody documentation",
 ],
 "standards": [
  "Forensic entomology practice per Amendt et al. standards",
 ],
 "citations": [CIT_STD, CIT_RESH],
 "sig_lens": (
  "Signature reading: the body clock written in insects — development "
  "is a thermometer-integrating timer no one can tamper with. Manon's "
  "Signature take: when you need the truth about timing, read the "
  "system's own logs; nature keeps receipts."),
 "demo_kind": "pmi_calc",
},
{
 "key": "diapause-cold-hardiness", "name": "Insect Physiology: Diapause and Cold Hardiness",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Insects survive winter and drought not by enduring but by shutting "
  "down on schedule: diapause, a hormonally programmed dormancy entered "
  "before conditions turn bad, distinct from quiescence (a direct, "
  "immediate slowdown). Photoperiod is the main token stimulus — "
  "shortening days in late summer switch development into the "
  "overwintering stage (egg, larva, pupa, or adult depending on "
  "species), mediated by juvenile hormone and ecdysteroid shifts. A "
  "diapausing insect suppresses metabolism to a fraction of active "
  "levels, accumulates cryoprotectants (glycerol, sorbitol, trehalose), "
  "and often dehydrates partially — concentrated body fluids freeze at "
  "lower temperatures. Cold-hardiness strategies: freeze avoidance "
  "(supercooling — cooling below 0 C without ice forming, down to the "
  "supercooling point where spontaneous nucleation occurs; the "
  "overwintering goldenrod gall fly larva supercools to about -50 C) "
  "versus freeze tolerance (surviving internal ice by controlling where "
  "it forms — extracellular — using ice-nucleating proteins; the woolly "
  "bear caterpillar freezes solid and thaws). Some Arctic insects add "
  "antifreeze proteins that bind ice crystals and halt their growth "
  "(thermal hysteresis). Diapause timing is heritable and locally "
  "adapted — critical daylength varies with latitude — and climate "
  "change is already desynchronizing insects from their host plants "
  "and from the birds that eat them."),
 "how_it_works": (
  "Diapause induction runs through the brain's photoperiodic clock: "
  "circadian neurons measure night length, and when nights exceed the "
  "critical duration, neurosecretory cells alter prothoracicotropic "
  "hormone signaling, dropping ecdysteroid production and locking the "
  "insect in the current stage. Metabolic suppression is active — "
  "mitochondria are downregulated and specific diapause proteins "
  "expressed — not merely cold slowing chemistry. Cryoprotectant "
  "synthesis converts glycogen stores into glycerol and trehalose, "
  "which colligatively depress the freezing point and stabilize "
  "membranes and proteins during dehydration. Freeze-avoiders purge "
  "ice nucleators from the gut (empty gut, no food particles to seed "
  "crystals) and coat with cuticular waxes; the supercooling point "
  "marks the hard limit — below it, ice nucleates spontaneously and "
  "the insect dies. Freeze-tolerant species do the opposite: they "
  "manufacture ice-nucleating proteins in the hemolymph so freezing "
  "starts at high subzero temperatures, slowly and extracellularly, "
  "while cells dehydrate safely and cryoprotectants guard membranes. "
  "Spring termination requires chilling fulfillment (a cold requirement "
  "like vernalization) followed by warming — the insect counts winter "
  "before trusting spring."),
 "key_points": [
  "Diapause: programmed dormancy entered before stress; quiescence: direct slowdown",
  "Photoperiod (night length) is the token stimulus; JH/ecdysteroid shifts execute it",
  "Cryoprotectants (glycerol, trehalose) + dehydration depress freezing points",
  "Freeze avoidance: supercooling to the nucleation limit (gall fly larva ~-50 C)",
  "Freeze tolerance: controlled extracellular ice via ice-nucleating proteins (woolly bear)",
  "Critical daylength is locally adapted; climate change desynchronizes phenology",
 ],
 "requirements": [
  "Programmable cooling stage for supercooling-point measurement",
  "Photoperiod chambers for diapause induction studies",
 ],
 "standards": [
  "Cold-hardiness terminology per standard insect physiology literature",
 ],
 "citations": [CIT_NORRIS, CIT_CHAPMAN],
 "sig_lens": (
  "Signature reading: scheduled hibernation with antifreeze protocols — "
  "the insect does not fight winter, it opts out on a calendar trigger. "
  "Manon's Signature take: the best way to survive a predictable crisis "
  "is a pre-programmed shutdown, not heroics; sense the season, not the "
  "storm."),
 "demo_kind": "supercooling",
},
{
 "key": "insect-genetics", "name": "Insect Genetics and Genomics",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Insects are genetics' model citizens: the fruit fly Drosophila "
  "melanogaster founded modern genetics (Morgan's white-eye mutants, "
  "1910), and insect genomics now drives pest control and evolutionary "
  "biology. Insect genomes are compact and diverse: Drosophila's ~180 "
  "megabases and ~14,000 genes versus the migratory locust's ~6.5 "
  "gigabases bloated with transposable elements. Key systems: sex "
  "determination varies wildly — XY (Drosophila), XO (grasshoppers), "
  "haplodiploidy (Hymenoptera), and even paternal genome elimination "
  "(mealybugs); developmental genetics revealed the Hox gene clusters "
  "patterning insect segments, work that earned a Nobel Prize. Modern "
  "applied insect genetics: the sterile insect technique (SIT) mass-"
  "rears, sterilizes (radiation), and releases males that mate "
  "fruitlessly — eradicating screwworm from North America and "
  "suppressing Mediterranean fruit fly; Wolbachia-infected mosquitoes "
  "that block dengue transmission; RNA interference sprays that silence "
  "essential pest genes species-specifically; and CRISPR gene drives "
  "that bias inheritance to spread engineered traits (malaria-"
  "refractory mosquitoes, population suppression) — powerful, and "
  "under intense ecological and ethical evaluation before any field "
  "release. Population genomics now tracks insecticide-resistance "
  "alleles (kdr) spreading across continents in real time."),
 "how_it_works": (
  "Classical insect genetics exploits short generations and huge "
  "families: cross mutants, score phenotypes in the F2, map genes by "
  "recombination — Drosophila's polytene chromosomes (giant banded "
  "salivary chromosomes) let early geneticists literally see deletions "
  "and inversions under the microscope. Modern genomics sequences and "
  "assembles genomes, annotates genes by homology, and compares across "
  "the insect tree (the i5K initiative targets 5,000 arthropod genomes). "
  "SIT works demographically: flooding the field with sterile males "
  "means most wild females mate sterilely, and each generation shrinks "
  "— effective when the ratio exceeds ~10:1 and immigration is low. "
  "Gene drives cheat Mendel: a CRISPR cassette on one chromosome cuts "
  "the homologous chromosome and copies itself, converting "
  "heterozygotes to homozygotes so the trait spreads to nearly all "
  "offspring instead of half — models show continent-scale spread in "
  "dozens of generations, which is why governance frameworks (WHO, "
  "national regulators) require staged testing. RNAi biopesticides are "
  "sprayed as double-stranded RNA matching a vital pest gene; the "
  "insect's own RNAi machinery degrades the matching messenger RNA "
  "and the pest dies — sequence-specific, so non-target insects with "
  "different sequences are unaffected, though environmental RNA "
  "stability and resistance evolution remain active research areas."),
 "key_points": [
  "Drosophila founded modern genetics (1910); Hox patterning work won a Nobel",
  "Genome sizes: fruit fly ~180 Mb; migratory locust ~6.5 Gb",
  "Sex determination: XY, XO, haplodiploidy, paternal genome elimination",
  "SIT: sterile males crash populations (screwworm eradicated from N. America)",
  "Gene drives bias inheritance to ~100% — continent-scale spread in models; strictly governed",
  "RNAi sprays silence pest genes sequence-specifically; resistance alleles tracked by population genomics",
 ],
 "requirements": [
  "Drosophila culture capability for teaching labs",
  "Regulatory compliance for any genetic biocontrol work",
 ],
 "standards": [
  "Genetic biocontrol governance per WHO/regulatory frameworks",
 ],
 "citations": [CIT_STD, CIT_GULLAN],
 "sig_lens": (
  "Signature reading: rewrite the inheritance rules and the population "
  "rewrites itself — the gene drive is the ultimate leverage point. "
  "Manon's Signature take: the most powerful edits are the ones that "
  "copy themselves; wield that power only inside governance that can "
  "say no."),
 "demo_kind": "genome_size",
},
{
 "key": "insect-diversity-success", "name": "Insect Diversity: Why Insects Rule",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Why are there so many insects? About 1 million described species and "
  "5.5-10 million estimated — insects outnumber all other animals "
  "combined several times over. The success formula has interlocking "
  "parts. Small size: most insects are millimeters long, so the world "
  "offers them vastly more niches (a single tree holds hundreds of "
  "microhabitats) and populations can be enormous. Flight: wings "
  "enabled escape, colonization, and mate-finding 100 million years "
  "before vertebrates flew. Metamorphosis: holometaboly lets one genome "
  "occupy two niches (leaf-chewing caterpillar, nectar-sipping moth), "
  "halving competition. The exoskeleton: armor plus waterproofing opened "
  "deserts and dry microhabitats. Short generations and high fecundity: "
  "rapid evolution outruns plant defenses and insecticides alike. "
  "Coevolution with flowering plants: the angiosperm radiation 140-100 "
  "million years ago offered endless new niches, and herbivorous and "
  "pollinating insects radiated with them (roughly half of insect "
  "species eat plants). Specialization: most herbivores and parasitoids "
  "are specialists, and specialists speciate faster — split one host "
  "plant into two, and its insects can split too. The numbers keep "
  "growing: tropical canopy fogging routinely returns 80%+ undescribed "
  "species, and parasitoid wasps alone may number in the millions. "
  "Understanding the formula matters: it predicts where the unknown "
  "diversity hides and why insect declines (documented 1-2% yearly "
  "losses in monitored populations) threaten ecosystem function."),
 "how_it_works": (
  "Diversification is measured as speciation minus extinction over "
  "time, and insect clades with key innovations show elevated net "
  "diversification rates. Phylogenetic studies test each candidate "
  "innovation: wings correlate with the Pterygota radiation; "
  "holometaboly with the Holometabola's dominance (85% of species); "
  "phytophagy with the great herbivore radiations (beetles, moths, "
  "true bugs each radiated alongside plant groups). The escape-and-"
  "radiate model (Ehrlich & Raven): insects evolve a detoxification "
  "breakthrough, colonize a defended plant lineage, then speciate as "
  "they specialize on its descendant species — repeated thousands of "
  "times. Parasitoids add a multiplier: each herbivore species hosts "
  "several specialist parasitoids, stacking a whole trophic level of "
  "diversity on top. Small body size enters mathematically: niche "
  "number scales inversely with organism size, and generation time "
  "scales with size, so small insects both subdivide habitat more "
  "finely and evolve faster. The same formula explains vulnerability: "
  "specialists with narrow niches and short generations respond "
  "rapidly to habitat change — which is why monitored insect biomass "
  "is falling 1-2% per year in many regions, a decline rate that "
  "compounds catastrophically over decades."),
 "key_points": [
  "~1M described, 5.5-10M estimated — insects outnumber all other animals combined",
  "Success factors: small size, flight, metamorphosis, exoskeleton, fecundity, angiosperm coevolution",
  "Holometaboly = one genome, two niches; phytophagy = half of all insect species",
  "Escape-and-radiate: detox breakthrough -> colonize plant lineage -> speciate with it",
  "Parasitoids stack a whole diversity level on top of herbivores",
  "Same formula explains declines: monitored biomass falling 1-2%/year compounds fast",
 ],
 "requirements": [
  "Phylogenetic diversification-rate references",
  "Long-term monitoring datasets for decline statistics",
 ],
 "standards": [
  "Diversity estimates per Stork et al. (2015) methods",
 ],
 "citations": [CIT_GULLAN, CIT_STD],
 "sig_lens": (
  "Signature reading: dominance by formula — small, flying, "
  "transforming, armored, fecund, and partnered with the green kingdom. "
  "Manon's Signature take: success compounds from stacked advantages, "
  "not one trick; and the same specialization that wins makes you "
  "fragile — diversify the base you stand on."),
 "demo_kind": "success_factors",
},
{
 "key": "urban-entomology", "name": "Urban Entomology: Bed Bugs, Cockroaches, Termites",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Urban entomology manages the insects that moved in with humanity: "
  "bed bugs, cockroaches, termites, ants, and stored-product pests in "
  "homes and businesses. The common bed bug (Cimex lectularius) — a "
  "flat, apple-seed-sized blood-feeder that hides in mattress seams "
  "and feeds at night — resurged globally since the 2000s after "
  "decades of DDT-era suppression, now resistant to pyrethroids "
  "nearly everywhere; control requires integrated methods (heat "
  "treatment at ~50 C, mattress encasements, desiccant dusts, "
  "monitoring interceptors) because chemistry alone fails. German "
  "cockroaches (Blattella germanica) infest kitchens, trigger asthma "
  "and allergies (their frass and shed skins are potent allergens), "
  "and carry pathogens mechanically; gel baits with slow-acting "
  "toxins exploit their coprophagy and trophallaxis to poison the "
  "whole aggregation. Subterranean termites (Reticulitermes, "
  "Coptotermes) cause billions in structural damage yearly, eating "
  "wood from the inside while foraging through mud tubes; control "
  "uses soil termiticide barriers, bait stations with chitin-synthesis "
  "inhibitors that collapse the colony, and building design (concrete, "
  "steel, treated wood). Urban IPM emphasizes inspection, monitoring, "
  "exclusion (sealing entry points), sanitation, and targeted "
  "treatments — the same threshold logic as agricultural IPM, applied "
  "to structures, with customer cooperation as a required input."),
 "how_it_works": (
  "Urban pests exploit the built environment's constancy: stable "
  "warmth, moisture, food, and harborage year-round remove the "
  "seasonal bottlenecks that limit outdoor populations. Bed bugs "
  "find hosts by CO2 and heat, feed 5-10 minutes, then retreat to "
  "harborages where aggregation pheromones concentrate them — "
  "interceptor traps under bed legs exploit their climbing behavior "
  "to monitor and confirm elimination. Their traumatic insemination "
  "(males pierce the female's abdomen) and resistance alleles "
  "spreading globally make them a case study in rapid evolution. "
  "German cockroach aggregations run on cuticular-hydrocarbon "
  "recognition and shared harborages; baiting works because foragers "
  "carry slow-acting bait back and the colony shares it — kill the "
  "forager too fast and the colony learns avoidance (bait aversion "
  "is documented). Termite foraging is coordinated by trail "
  "pheromones from the sternal gland; bait stations intercept "
  "foraging tunnels, and workers distribute the chitin inhibitor "
  "through trophallaxis — molting workers die, and because the "
  "inhibitor persists, the colony spirals down over months. "
  "Structural protection adds physical termite barriers (graded "
  "stone, stainless mesh) that force termites into the open where "
  "inspection finds them."),
 "key_points": [
  "Bed bugs resurged since 2000s; pyrethroid resistance near-global; heat + encasement + desiccants beat chemistry",
  "German cockroaches: asthma/allergy triggers; gel baits exploit trophallaxis — slow poison wins",
  "Subterranean termites: billions in damage/year; bait stations with chitin inhibitors collapse colonies",
  "Buildings remove seasonal bottlenecks — constant warmth, food, harborage",
  "Urban IPM: inspection, monitoring, exclusion, sanitation, targeted treatment + customer cooperation",
  "Interceptor traps and bait stations turn pest behavior into the control mechanism",
 ],
 "requirements": [
  "Interceptor traps + mattress encasements (bed bug protocol)",
  "Termite bait station array + inspection schedule",
  "Customer sanitation cooperation checklist",
 ],
 "standards": [
  "Urban IPM per NPMA best practices",
 ],
 "citations": [CIT_PEDIGO, CIT_STD],
 "sig_lens": (
  "Signature reading: the enemy moved into your house — so fight "
  "with the house, not just the spray can. Manon's Signature take: "
  "exclusion and monitoring are permanent fortifications; chemistry "
  "is a raid. Fortify first, raid only on evidence."),
 "demo_kind": "urban_ipm",
},
{
 "key": "insect-conservation", "name": "Conservation of Insects: Pollinator Declines",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Insect conservation is the newest and most urgent branch of "
  "entomology: monitored insect populations are falling 1-2% per year "
  "in many regions — a compounding loss that threatens pollination, "
  "decomposition, and food webs. The drivers are quantified: habitat "
  "loss and fragmentation (the largest), pesticides (especially "
  "systemic neonicotinoids impairing bee navigation and reproduction "
  "at field-realistic doses), intensive agriculture (monocultures "
  "without floral resources), light pollution (disrupting nocturnal "
  "moths), climate change (phenological mismatch — bees emerging "
  "before flowers bloom), and invasive species. Case studies: the "
  "western monarch population fell from millions in the 1980s-90s to "
  "tens of thousands; the rusty patched bumble bee (Bombus affinis) "
  "became the first US bumble bee listed endangered (2017); UK "
  "butterfly monitoring shows long-term declines across habitat "
  "specialists. Conservation tools: habitat restoration (wildflower "
  "strips, hedgerows, reduced mowing — 'no-mow' corridors measurably "
  "raise pollinator abundance), pesticide risk reduction (IPM, "
  "banning the most harmful systemics near bloom), protected areas "
  "designed for insects (not just vertebrates), captive breeding and "
  "reintroduction (the large blue butterfly's successful UK "
  "reintroduction after its ant-host ecology was decoded), and "
  "long-term monitoring (standardized transects, Malaise trap networks, "
  "citizen science like eButterfly/iNaturalist). The economic case is "
  "direct: pollinator-dependent crops are worth hundreds of billions "
  "globally, and insectivorous birds and fish depend on insect biomass."),
 "how_it_works": (
  "Conservation starts with measurement: standardized butterfly "
  "transects (fixed routes walked weekly in season), Malaise trap "
  "time series, and bee bowl-trap arrays produce comparable abundance "
  "indices; occupancy modeling corrects for imperfect detection. "
  "Decline attribution uses driver analysis — correlating population "
  "trends with land-use, pesticide-use, and climate layers across "
  "sites. Habitat interventions are engineered: wildflower strips are "
  "seeded with region-appropriate native forbs sequenced for continuous "
  "bloom (spring to fall), because pollinators need unbroken floral "
  "resources; nesting habitat is added alongside (bare ground for "
  "mining bees, pithy stems for cavity nesters, undisturbed leaf "
  "litter for bumble bee queens). Pesticide mitigation follows the "
  "risk equation (toxicity x exposure): apply IPM, avoid spraying bloom, "
  "choose selective compounds, and respect buffer zones. The large blue "
  "reintroduction is the textbook success: the butterfly's larvae must "
  "be adopted by a specific Myrmica ant species, so conservationists "
  "restored the grassland sward height that favors that ant — saving "
  "the butterfly by managing for the ant. Policy levers include "
  "agri-environment payments for pollinator habitat, endangered-species "
  "listings that trigger habitat protection, and municipal no-spray "
  "and reduced-mowing ordinances — small land areas, large insect "
  "returns."),
 "key_points": [
  "Monitored insect populations falling 1-2%/year in many regions — compounding loss",
  "Drivers: habitat loss (#1), pesticides (neonics), monocultures, light pollution, climate mismatch, invasives",
  "Western monarch: millions -> tens of thousands; rusty patched bumble bee listed endangered 2017",
  "Interventions: wildflower strips with continuous bloom + nesting habitat + IPM + no-mow corridors",
  "Large blue butterfly: reintroduced by managing grassland for its host ant",
  "Monitoring: transects, Malaise time series, citizen science; policy: agri-payments, listings, no-spray zones",
 ],
 "requirements": [
  "Region-appropriate native forb seed mixes (continuous bloom sequence)",
  "Standardized monitoring protocol (transects or trap arrays)",
  "Pesticide risk assessment for pollinators",
 ],
 "standards": [
  "Pollinator habitat standards per Xerces Society guidelines",
 ],
 "citations": [CIT_GULLAN, CIT_STD],
 "sig_lens": (
  "Signature reading: the foundation crew is quitting — 1-2% a year, "
  "compounding, and the whole food web stands on their backs. Manon's "
  "Signature take: measure relentlessly, fix the habitat first, and "
  "treat pollinator strips as infrastructure, not decoration."),
 "demo_kind": "decline_stats",
},
]

