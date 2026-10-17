#!/usr/bin/env python3
"""Nanotoxicology field entries for JAH Databases (field #34, taxonomy order).

Verified 2026-10-17: NO database covers nanotoxicology as a discipline.
Manifest search (2,368 databases): zero 'nanotox*' slugs; zero 'tox' slugs
at all. Nearest neighbors are 'occupational-safety-study' /
'occupational-safety-published' (occupational safety as a study field, not
nanoscale hazard science), 'nanotech' (general nanotechnology, 10,001
records - no toxicology discipline), 'nanomechanics', 'nanocomposites',
'nanofluidics' - all different disciplines. Whole-system exact-title sweep:
zero collisions for all 34 planned titles. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nanotoxicology              - The Nanotoxicology Database
                               (public-harvest: real, fact-checked
                               nanotoxicology; standard references
                               Oberdorster et al. 'Nanotoxicology: An
                               emerging discipline evolving from studies of
                               ultrafine particles' Environ. Health
                               Perspect. 2005; Nel et al. 'Toxic potential
                               of materials at the nanolevel' Science 2006;
                               Donaldson et al. 'Carbon nanotubes: a review
                               of their properties in relation to pulmonary
                               toxicology and workplace safety' Toxicol.
                               Sci. 2006; NIOSH CIB 65 'Occupational
                               Exposure to Carbon Nanotubes and Nanofibers'
                               2013; ISO/TS 12901-2:2014; OECD inhalation
                               test guidelines)
  nanotoxicology-signature    - The Nanotoxicology Signature Database
                               (his original Signature interpretation of
                               nanotoxicology as safety engineering; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

CONTENT SAFETY (this is toxicology): records describe hazards, exposure
science, and SAFETY engineering only. No instructions facilitating harm;
every hazard record pairs with controls and mitigation. Nothing disallowed.

Subtitle disambiguation (fields #13-33 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Dose Metrics:
Mass, Surface Area, and Particle Number".

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds, and ends with the OK marker; the build machine-executes all
68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "nanotoxicology as safety engineering, clearly labeled "
            "Signature-made and never presented as authentic public record.")

ENTRIES = [
{
"key": "what_is",
"name": "What Is Nanotoxicology: The Engineering of Nanoscale Hazard and Safety",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Nanotoxicology is the science of how materials between 1 and 100 "
"nanometres interact with living tissue - and the engineering discipline "
"that turns that knowledge into safe products, safe workplaces, and safe "
"regulations. The field was born from a simple, unsettling observation: "
"the same gram of titanium dioxide can be nearly inert as a coarse powder "
"and strongly inflammatory as 20-nanometre particles. Shrinking a particle "
"multiplies its surface area per gram (6 divided by density times "
"diameter), and surface is where chemistry happens: a 20 nm particle of "
"titanium dioxide carries about 77 square metres of surface per gram, ten "
"times what a 200 nm particle carries. Nanotoxicology asks, for every "
"nanoscale material, what the surface does to cells, where the particles "
"go in the body, what dose metric predicts the harm, and which engineering "
"control removes the risk. It is distinct from nanomedicine (which "
"designs therapies) and from environmental nanotechnology (which designs "
"remediation): nanotoxicology designs safety."),
"how_it_works": (
"A nanotoxicology study follows a fixed chain. First, the material is "
"characterized as it actually exists in exposure: primary size, "
"agglomeration state, crystal form, surface chemistry, and dissolution "
"rate - because the powder in the bag is not the particle in the lung. "
"Second, the exposure is defined by route (inhalation, skin, ingestion), "
"duration, and dose expressed in the metric that best predicts effect: "
"mass for soluble materials, surface area for poorly soluble particles, "
"particle number for fibers. Third, the biological response is measured: "
"cell death and inflammation in dishes (in vitro), lung inflammation and "
"organ distribution in animals (in vivo), and molecular markers of "
"oxidative stress. Fourth, the dose-response curve is built and a "
"no-effect level is estimated. Fifth, engineers and regulators convert "
"that curve into exposure limits, control bands, and safer material "
"designs. Every record in this database walks one link of that chain."),
"key_points": [
"Nanotoxicology = the hazard and exposure science of 1-100 nm materials, turned into safety engineering.",
"A 20 nm TiO2 particle has ~77 m2/g of surface; a 200 nm particle has ~7.7 m2/g - surface is where the chemistry happens.",
"Characterize the material AS EXPOSED: size, agglomeration, crystal form, surface, dissolution.",
"Dose must use the right metric: mass, surface area, or particle number - the wrong metric hides the risk.",
"Every hazard finding pairs with a control: ventilation, containment, coating, or redesign.",
"Distinct from nanomedicine (therapies) and environmental nanotech (remediation) - this field designs safety."],
"requirements": [
"A defined nanomaterial with measured size, surface area, and surface chemistry.",
"An exposure scenario: route, duration, and concentration in air, liquid, or on skin.",
"A biological test system: cells, animals, or validated non-animal methods.",
"A dose-response design with enough doses to find the no-effect level."],
"standards": [
"ISO/TS 80004-1:2023 - nanotechnology vocabulary (nano-object, nanomaterial, nanoform).",
"ISO/TR 13014:2012 - guidance on physico-chemical characterization of nano-objects for toxicologic testing."],
"citations": [
"Oberdorster, G., Oberdorster, E. & Oberdorster, J. 'Nanotoxicology: An emerging discipline evolving from studies of ultrafine particles' Environ. Health Perspect. 113, 823-839 (2005).",
"Nel, A., Xia, T., Madler, L. & Li, N. 'Toxic potential of materials at the nanolevel' Science 311, 622-627 (2006)."],
"sig_lens": (
"Signature lens: treat every nanomaterial as a Signature surface first "
"and a substance second. The Signature reading asks how much chemistry "
"each gram can do (surface area), where the particles can travel "
"(exposure routes), and which dial - size, coating, crystal form - "
"engineers the hazard down without losing the function. Safety is a "
"design output, not a test result.")},
{
"key": "dose_metrics",
"name": "Dose Metrics: Mass, Surface Area, and Particle Number",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"The oldest lesson in nanotoxicology is that a milligram is not a "
"milligram. Take one milligram of titanium dioxide per cubic metre of "
"air. As 100-nanometre particles that is about 4.9e14 particles carrying "
"15 square metres of surface per cubic metre. Grind the same milligram to "
"10-nanometre particles and it becomes 4.9e17 particles carrying 154 "
"square metres of surface - one thousand times the particle number, ten "
"times the surface area, the same mass. If the harm comes from surface "
"chemistry (reactive oxygen species generated at the particle surface), "
"the mass dose says 'same risk' while the surface-area dose says 'ten "
"times the risk'. Studies of poorly soluble particles - titanium dioxide, "
"carbon black, barium sulfate - show lung inflammation tracks total "
"deposited surface area far better than deposited mass. For fibers "
"(carbon nanotubes), neither mass nor surface area works: the count and "
"length of long fibers predicts the asbestos-like response. The three "
"metrics answer three different questions: mass asks 'how much material', "
"surface area asks 'how much chemistry', particle number asks 'how many "
"objects'. A competent study reports all three."),
"how_it_works": (
"Converting between metrics is arithmetic on spheres. Particle mass = "
"density times pi/6 times diameter cubed. Particle number concentration = "
"mass concentration divided by particle mass. Surface-area concentration "
"= number concentration times pi times diameter squared. The demo "
"performs the full conversion for titanium dioxide (density 3900 kg/m3) "
"at 1 mg/m3 for 10 nm and 100 nm particles and shows the 1000x number "
"and 10x surface-area jumps explicitly. In practice the conversion needs "
"the real size distribution (count median diameter, geometric standard "
"deviation) measured by electron microscopy or differential mobility "
"sizing, because agglomerates behave as larger effective particles and "
"dissolving particles shed the metric entirely. Regulators increasingly "
"set limits in the predictive metric: NIOSH set the ultrafine titanium "
"dioxide limit at 0.3 mg/m3 versus 2.4 mg/m3 for fine, precisely because "
"surface area, not mass, drives the response."),
"key_points": [
"1 mg/m3 of TiO2: 10 nm particles = 4.9e17/m3 and 154 m2/m3; 100 nm = 4.9e14/m3 and 15.4 m2/m3 - same mass.",
"Lung inflammation from poorly soluble particles tracks deposited SURFACE AREA, not mass.",
"Fiber hazard tracks fiber COUNT and LENGTH (the fiber paradigm), not mass.",
"Conversions: N = C_mass / (rho*pi/6*d^3); SA = N*pi*d^2.",
"Report all three metrics; measure the real size distribution, not the label size.",
"Regulators follow the predictive metric (NIOSH ultrafine TiO2 limit 0.3 mg/m3 vs 2.4 fine)."],
"requirements": [
"A measured particle size distribution (electron microscopy or mobility sizing).",
"Material density and an assumption about shape (spheres unless measured otherwise).",
"An airborne mass concentration from gravimetric or real-time sampling.",
"Awareness that agglomerates and dissolving particles change the effective metric."],
"standards": [
"ISO 10808:2010 - characterization of nanoparticles in exposure chambers for inhalation toxicity testing.",
"NIOSH Method 0600 - respirable particulate mass sampling (basis for gravimetric dose)."],
"citations": [
"Oberdorster, G., Ferin, J. & Lehnert, B. E. 'Correlation between particle size, in vivo particle persistence, and lung injury' Environ. Health Perspect. 102 (Suppl 5), 173-179 (1994).",
"Tran, C. L. et al. 'Inhalation of poorly soluble particles. II. Influence of particle surface area on inflammation and clearance' Inhal. Toxicol. 12, 1113-1126 (2000)."],
"sig_lens": (
"Signature lens: the dose metric is a Signature translation problem - "
"the same physical reality (a cloud of particles) has three true "
"numbers, and only one of them predicts harm. The Signature habit is to "
"compute all three from the size distribution before any toxicology "
"begins, then let the biology vote on which one the dose-response "
"follows.")},
{
"key": "exposure_routes",
"name": "Exposure Routes: Inhalation, Dermal, and Ingestion",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"A nanomaterial can only harm tissue it reaches, so nanotoxicology "
"starts by mapping the three doors: lungs, skin, and gut. Inhalation "
"dominates workplace risk because engineered nanoparticles are "
"manufactured, weighed, and poured as dry powders - and a worker doing "
"light work breathes about 20 litres per minute, 9.6 cubic metres over "
"an 8-hour shift. At the NIOSH carbon nanotube limit of 1 microgram per "
"cubic metre that is 9.6 micrograms inhaled per shift; at 100 micrograms "
"per cubic metre it is nearly a milligram. Particles below 100 nm "
"deposit deep in the alveolar region by diffusion, exactly where "
"clearance is slowest. Dermal exposure matters for sunscreens (nanoscale "
"zinc oxide and titanium dioxide) and workplace spills, but intact skin "
"is a strong barrier: measured fluxes of nano-titanium dioxide through "
"intact skin are on the order of nanograms per square centimetre per "
"hour, and most studies find no penetration past the outer dead layer. "
"Ingestion arrives through food additives, food-contact materials, and "
"hand-to-mouth transfer; the gut absorbs very little (oral "
"bioavailability of nano-TiO2 is a fraction of a percent), but what "
"crosses can reach liver and spleen. Route determines everything: the "
"same particle is a lung hazard, a skin non-event, and a gut footnote."),
"how_it_works": (
"Route assessment is bookkeeping: inhaled dose = breathing rate times "
"exposure time times airborne concentration times the deposition "
"fraction for that size. The demo does the shift arithmetic - 20 L/min "
"for 8 hours gives 9.6 m3, and shows the inhaled mass at the nanotube "
"limit versus a dusty 100 ug/m3 operation. Deposition fraction comes "
"from the ICRP lung model: diffusion dominates below 100 nm (alveolar "
"deposition peaks around 20 nm), impaction and settling dominate above "
"a micrometre. Dermal flux is measured in Franz diffusion cells on real "
"skin: flux J times area times time gives the absorbed mass, and for "
"intact skin the numbers are reassuringly tiny - until the skin is "
"damaged, sunburned, or flexed at joints, when penetration rises. Gut "
"uptake is measured as the fraction of an oral dose found in blood and "
"organs. The engineering consequence is direct: control the airborne "
"powder and you control the dominant risk."),
"key_points": [
"Light work breathing (20 L/min, 8 h) inhales 9.6 m3 of air per shift.",
"At the 1 ug/m3 CNT limit that is 9.6 ug inhaled; at 100 ug/m3 it is ~1 mg.",
"Sub-100 nm particles deposit in the alveoli by diffusion - deepest, slowest clearance.",
"Intact skin blocks nano-TiO2/ZnO effectively (nanogram-scale fluxes); damaged skin is the exception.",
"Gut uptake of nano-TiO2 is a fraction of a percent - but liver and spleen are the destinations.",
"Route determines the hazard: control airborne powder and you control the dominant risk."],
"requirements": [
"A defined exposure scenario: concentration, duration, activity level.",
"Breathing rates matched to the work (rest 6-8 L/min, light 20, heavy 40+).",
"Skin condition assessment (intact vs damaged) for dermal scenarios.",
"Deposition and uptake fractions from the ICRP model or measured data."],
"standards": [
"ICRP Publication 66 - human respiratory tract model for radiological protection (deposition fractions).",
"ISO 13138:2012 - sampling conventions for airborne particle deposition in the human respiratory system."],
"citations": [
"Maynard, A. D. et al. 'Exposure to carbon nanotube material: aerosol release during the handling of unrefined single-walled carbon nanotube material' J. Toxicol. Environ. Health A 67, 87-107 (2004).",
"Krug, H. F. & Wick, P. 'Nanotoxicology: An interdisciplinary challenge' Angew. Chem. Int. Ed. 50, 1260-1278 (2011)."],
"sig_lens": (
"Signature lens: the three routes are three Signature gates, and "
"engineering closes them in priority order - lungs first, because air "
"carries powder everywhere; skin second, because contact is local; gut "
"third, because the barrier is strong. The Signature design question is "
"always 'which gate does this product open, and how do we keep it "
"shut?'")},
{
"key": "translocation",
"name": "The Nanoparticle's Journey: Translocation From Contact to Target Organ",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Once a nanoparticle lands on tissue, its size lets it do something "
"coarse dust cannot: keep moving. Below about 100 nm, Brownian motion "
"is violent - a 10 nm particle in air jitters through roughly 70 "
"micrometres of random walk every second, a 100 nm particle about 22. "
"In the deep lung, particles that dodge the alveolar macrophages can "
"cross the air-blood barrier (about half a micrometre of tissue) into "
"the capillaries. Studies with inhaled ultrafine particles - iridium, "
"carbon, titanium dioxide - find small fractions in blood within hours "
"and later in liver, spleen, heart, and even brain via the olfactory "
"nerve. The fractions are small (typically well under 1 percent of the "
"deposited dose for insoluble particles), but the principle matters: "
"the lung is not a sealed bag, it is a gateway. Soluble particles "
"translocate as ions after dissolving; poorly soluble ones travel as "
"particles, often inside macrophages that migrate to lymph nodes. "
"Surface chemistry steers the journey: positively charged particles "
"stick to negatively charged cell membranes and enter cells more "
"readily; PEGylated (polyethylene-glycol-coated) particles circulate "
"longer because the immune system notices them less. Toxicology follows "
"the particle: find where it goes, then look for harm there."),
"how_it_works": (
"Translocation is quantified with tracers: radiolabeled or "
"neutron-activatable particles, or particles with an elemental "
"fingerprint (iridium, gold) measured by mass spectrometry in blood and "
"organs over time. The demo computes the Brownian random-walk distance - "
"square root of 2*D*t with D from the Stokes-Einstein equation - "
"showing a 10 nm particle covers ~70 um per second, far more than the "
"0.5 um air-blood barrier, which is why diffusion delivers particles to "
"the barrier in the first place. Biokinetic studies then fit "
"compartment models: lung to blood rate, blood to liver rate, "
"excretion rates. The olfactory route is special: inhaled nanoparticles "
"deposit on the olfactory epithelium and travel along the olfactory "
"nerve directly to the brain, bypassing the blood-brain barrier - "
"demonstrated with ultrafine carbon and manganese oxide in rats. "
"Engineers use this knowledge in reverse: the same pathways that carry "
"hazard are the ones drug delivery exploits, and the coatings that "
"reduce translocation (dense silica shells, stable PEG layers) are "
"safety features."),
"key_points": [
"A 10 nm particle random-walks ~70 um/s; a 100 nm particle ~22 um/s (Stokes-Einstein in air).",
"Sub-1% of deposited insoluble particles typically translocate - small fraction, real pathway.",
"Olfactory nerve transport can carry inhaled nanoparticles directly to the brain.",
"Positive surface charge increases cell entry; PEG coatings extend circulation, dense shells reduce translocation.",
"Soluble particles translocate as dissolved ions; insoluble ones travel as particles, often in macrophages.",
"Find where the particle goes, then look for harm there - toxicology follows the particle."],
"requirements": [
"Traceable particles: radiolabel, neutron activation, or elemental fingerprint.",
"Time-course sampling of blood, lung, liver, spleen, brain, and excreta.",
"A defined exposure (inhalation preferred over instillation for realism).",
"Compartment modeling to extract transfer rates between organs."],
"standards": [
"OECD TG 412/413 - repeated-dose inhalation studies (28/90-day) with organ burden options.",
"ISO/TR 16197:2014 - guidance on toxicological screening methods for manufactured nanomaterials."],
"citations": [
"Oberdorster, G. et al. 'Translocation of inhaled ultrafine particles to the brain' Inhal. Toxicol. 16, 437-445 (2004).",
"Kreyling, W. G. et al. 'Translocation of ultrafine insoluble iridium particles from lung epithelium to extrapulmonary organs is size dependent but very low' J. Toxicol. Environ. Health A 65, 1513-1530 (2002)."],
"sig_lens": (
"Signature lens: translocation is the Signature travel map - every "
"particle has a passport (size, charge, coating) and the body's borders "
"inspect it. The Signature engineer stamps the passport deliberately: "
"coatings that say 'stay in the lung, dissolve harmlessly' or 'do not "
"enter cells', so the journey ends at a safe destination.")},
{
"key": "oxidative_stress",
"name": "Oxidative Stress and ROS: The Common Toxicity Pathway",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Ask what titanium dioxide, carbon black, silica, zinc oxide, and "
"ambient soot have in common toxicologically and the answer is not "
"their chemistry - it is reactive oxygen species (ROS). Particle "
"surfaces generate superoxide, hydrogen peroxide, and hydroxyl "
"radicals: transition metals on the surface run Fenton chemistry, "
"semiconductor band gaps split water under light, and even 'inert' "
"surfaces carry radicals from manufacturing. Cells defend with "
"antioxidants - glutathione, superoxide dismutase, catalase - but the "
"defense has a finite capacity. Nel's hierarchical oxidative stress "
"model (2006) describes three tiers: at low ROS, cells activate "
"protective antioxidant genes (Nrf2 pathway); at higher ROS, "
"inflammation switches on (NF-kB, cytokine release); at the highest "
"ROS, mitochondria fail and cells die by apoptosis or necrosis. This "
"single ladder explains why dose-response curves for wildly different "
"particles look alike, why antioxidants blunt particle toxicity in "
"experiments, and why the band gap of a metal oxide predicts its "
"toxicity (Zhang et al. 2012): band energies overlapping cellular redox "
"potentials drive electron theft from biomolecules. Measure a "
"particle's ROS generation and you have its toxicity forecast."),
"how_it_works": (
"ROS generation is measured cell-free first: electron spin resonance "
"with spin traps, or fluorescent probes (DCFH) that light up when "
"oxidized - always with particle-only controls, because particles "
"quench and scatter light. The demo models the core arithmetic: a "
"particle ROS production rate (moles per second per milligram) against "
"the cell's antioxidant clearance rate. Below the threshold dose where "
"production exceeds clearance, glutathione recycles the radicals and "
"nothing happens; above it, the buffer drains - the demo computes the "
"drain time for a fixed glutathione pool (about 200 seconds at 1 mg in "
"the example) - and inflammation begins. In cells, the tiers are read "
"with markers: Nrf2-driven genes (heme oxygenase-1) for tier 1, IL-8 "
"and TNF-alpha for tier 2, mitochondrial membrane potential collapse "
"for tier 3. Safer-by-design follows directly: dope the oxide to shift "
"its band gap away from cellular redox potentials, coat the surface to "
"block catalytic sites, or choose a non-redox-active crystal form."),
"key_points": [
"ROS (superoxide, H2O2, hydroxyl radical) is the shared mechanism across chemically different particles.",
"Nel's three tiers: antioxidant defense -> inflammation -> cell death, as ROS rises.",
"Metal oxide band gaps overlapping cellular redox potentials predict toxicity (band-gap paradigm).",
"Threshold arithmetic: harm begins where ROS production exceeds antioxidant clearance.",
"Antioxidants blunt particle toxicity experimentally - confirming the mechanism.",
"Safer-by-design: shift the band gap, coat catalytic sites, or pick a redox-quiet crystal form."],
"requirements": [
"A cell-free ROS assay (ESR spin trap or DCFH) with particle-only controls.",
"Cellular tier markers: Nrf2/HO-1, cytokines, mitochondrial potential.",
"An antioxidant-depletion control to confirm the mechanism.",
"Band-gap and dissolution data to separate ROS from ion effects."],
"standards": [
"OECD TG 487 - in vitro mammalian cell micronucleus test (genotoxicity tier).",
"ISO 10993-5 - in vitro cytotoxicity testing framework (adapted for nanomaterials with interference controls)."],
"citations": [
"Nel, A., Xia, T., Madler, L. & Li, N. 'Toxic potential of materials at the nanolevel' Science 311, 622-627 (2006).",
"Xia, T. et al. 'Comparison of the abilities of ambient and manufactured nanoparticles to induce cellular toxicity according to an oxidative stress paradigm' Nano Lett. 6, 1794-1807 (2006).",
"Zhang, H. et al. 'Use of metal oxide nanoparticle band gap to develop a predictive paradigm for oxidative stress and acute pulmonary inflammation' ACS Nano 6, 4349-4368 (2012)."],
"sig_lens": (
"Signature lens: oxidative stress is the Signature ledger - every "
"particle surface writes ROS debits, every cell holds antioxidant "
"credit, and toxicity is the overdraft. The Signature engineer balances "
"the ledger at the design stage: measure the ROS rate, price the "
"antioxidant cost, and reformulate until the account never goes red.")},
{
"key": "tio2",
"name": "Titanium Dioxide Nanoparticles: The Most Studied Case",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"No nanomaterial has a thicker toxicology file than titanium dioxide. "
"As a pigment it has been eaten, inhaled, and worn for a century; as "
"a nanomaterial (P25, anatase/rutile mixes around 20-30 nm) it became "
"the field's reference particle - the one every new assay is tested "
"against. The story has three chapters. Chapter one: inhalation. Rats "
"breathing high concentrations develop lung inflammation, and at "
"extreme overload, tumors - but the tumors track particle overload "
"(failed clearance), not a nano-specific carcinogenicity, and the "
"inflammation tracks deposited surface area, which is why NIOSH set "
"the ultrafine limit at 0.3 mg/m3, eight times lower than the 2.4 mg/m3 "
"fine-particle limit. Chapter two: photocatalysis. Anatase TiO2 absorbs "
"UV (band gap 3.2 eV, ~388 nm) and generates ROS under sunlight - the "
"property that makes it a self-cleaning coating and a sunscreen "
"ingredient simultaneously, with the sunscreen question settled by "
"penetration studies showing no passage through intact skin. Chapter "
"three: ingestion. Food-grade TiO2 (E171) contains a nano fraction; "
"France suspended it in 2020 over genotoxicity concerns while EFSA "
"concluded it could no longer be considered safe as a food additive in "
"2021. The lesson of TiO2: crystal form, coating, and route decide "
"everything - 'titanium dioxide' alone is not a hazard description."),
"how_it_works": (
"The TiO2 file is built from inhalation studies at multiple "
"concentrations with lung burden measured over time: inflammation "
"markers (neutrophils in lavage fluid, cytokines) plotted against "
"deposited mass, deposited surface area, and deposited particle "
"number. Surface area wins the correlation. The demo does the "
"regulatory arithmetic: an 8-hour shift at 20 L/min inhales 9.6 m3, "
"so the ultrafine limit of 0.3 mg/m3 allows 2.88 mg inhaled - and at "
"P25's 50 m2/g that is 0.144 m2 of reactive surface delivered to the "
"lung per shift at the limit. Photocatalytic ROS is measured under "
"standardized UV: anatase generates hydroxyl radicals that rutile "
"largely does not, which is why sunscreen grades are rutile, coated "
"with silica or alumina, and tested for ROS suppression. The coating "
"is the safety device: a dense 5-10 nm silica shell cuts both ROS "
"generation and direct surface contact while keeping the UV "
"absorption that makes the product work. Every 'nano TiO2' safety "
"claim must name the crystal form and the coating, or it says "
"nothing."),
"key_points": [
"Thickest toxicology file in nanotoxicology: the reference particle for assay validation.",
"Lung inflammation tracks deposited SURFACE AREA - basis for the 0.3 mg/m3 ultrafine limit (vs 2.4 fine).",
"Anatase is photocatalytically active (3.2 eV band gap); sunscreen grades use coated rutile.",
"Rat lung tumors at extreme doses track particle OVERLOAD, not nano-specific carcinogenicity.",
"Food-grade TiO2 (E171): France suspended it 2020; EFSA 2021 could no longer deem it safe as a food additive.",
"Crystal form + coating + route = the hazard description; 'TiO2' alone is not one."],
"requirements": [
"Crystal form identification (XRD: anatase vs rutile) and coating characterization.",
"Specific surface area by BET gas adsorption.",
"Photocatalytic ROS activity under standardized UV illumination.",
"Route-specific testing: inhalation for powders, dermal penetration for sunscreens."],
"standards": [
"NIOSH Current Intelligence Bulletin 63 (2011) - occupational exposure to titanium dioxide (0.3 mg/m3 ultrafine REL).",
"ISO/TS 11931:2012 - nanoscale calcium carbonate and titanium dioxide characteristics (powder characterization)."],
"citations": [
"NIOSH 'Current Intelligence Bulletin 63: Occupational Exposure to Titanium Dioxide' DHHS (NIOSH) Publication No. 2011-160 (2011).",
"Lee, K. P., Trochimowicz, H. J. & Reinhardt, C. F. 'Pulmonary response of rats exposed to titanium dioxide (TiO2) by inhalation for two years' Toxicol. Appl. Pharmacol. 79, 179-192 (1985).",
"EFSA Panel on Food Additives and Flavourings 'Safety assessment of titanium dioxide (E171) as a food additive' EFSA J. 19, e06585 (2021)."],
"sig_lens": (
"Signature lens: TiO2 is the Signature reference standard - the "
"particle every new material is measured against. The Signature "
"practice is to file every candidate material next to TiO2's three "
"chapters (inhalation surface-area response, photocatalytic ROS, "
"ingestion questions) and require the newcomer to answer the same "
"three before it ships.")},
{
"key": "silver",
"name": "Silver Nanoparticles: Ion Release and the Antimicrobial Trade-Off",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Silver nanoparticles are the most commercialized nanomaterial in "
"history - socks, washing machines, wound dressings, food containers - "
"and their toxicology is a trade-off written in chemistry. The "
"antimicrobial power and much of the mammalian toxicity both come from "
"the same process: oxidative dissolution releasing silver ions (Ag+). "
"Ions bind thiol groups in proteins, disrupt membranes, and generate "
"ROS; nanoparticles act as ion reservoirs that keep releasing long "
"after a silver salt would have washed away. Dissolution is "
"size-dependent - smaller particles dissolve faster per gram - and "
"coating-dependent: citrate-coated silver releases ions readily while "
"dense polymer or silica shells slow it. In the environment this makes "
"nanosilver a special concern: wastewater treatment plants convert "
"much of it to silver sulfide (far less toxic), but the fraction that "
"escapes is acutely toxic to algae and daphnia at microgram-per-litre "
"levels. In mammals, inhaled and injected nanosilver distributes to "
"liver and spleen, and high oral doses in rats produce the classic "
"silver effect - argyria-like tissue deposition. The engineering "
"answer is controlled release: bind the silver so it kills microbes on "
"contact but releases almost no free ions into the body or the drain."),
"how_it_works": (
"Ion release is measured by dialysis or ultrafiltration: particles on "
"one side of a membrane, ions crossing to be measured by ICP-MS over "
"days. The rate follows surface-area-normalized kinetics - the demo "
"uses a simple linear model where 10 nm silver dissolves at 2% of its "
"mass per day and 50 nm at 0.4% per day (the 1/diameter scaling), "
"showing 14% versus 2.8% dissolved after a week. Real kinetics are "
"more complex (oxygen, pH, chloride, and thiols all matter - chloride "
"precipitates AgCl, thiols complex the ion), but the size scaling "
"holds. Toxicity testing must therefore separate particle effects "
"from ion effects: run the ionic silver control (AgNO3) at the "
"released-ion concentration alongside the particle, and test the "
"particle in the presence of a strong ion chelator. If the ion "
"control reproduces the toxicity, the particle is a delivery device, "
"not a new hazard - and the safety fix is to slow the delivery: "
"sulfidation, alloying, or impermeable shells."),
"key_points": [
"Antimicrobial power and much of mammalian toxicity both come from Ag+ ion release - one chemistry, two outcomes.",
"Dissolution scales with 1/diameter: 10 nm Ag releases ~2%/day vs ~0.4%/day for 50 nm in the model.",
"Always run the ionic silver (AgNO3) control: if ions explain the toxicity, the particle is a delivery device.",
"Wastewater converts much nanosilver to low-toxicity Ag2S; escaped fractions threaten algae/daphnia at ug/L.",
"High oral doses in rats produce silver tissue deposition (argyria-like).",
"Safety engineering = controlled release: sulfidation, alloying, or impermeable shells."],
"requirements": [
"Dissolution rate measured by dialysis/ultrafiltration with ICP-MS ion analysis.",
"An ionic silver control at the released-ion concentration in every toxicity test.",
"Coating characterization (citrate vs polymer vs silica) since coating controls release.",
"Environmental transformation testing (sulfidation in wastewater conditions)."],
"standards": [
"ISO/TS 16578:2013 - vocabulary for silver nanoparticle characterization in toxicology.",
"OECD TG 201/202 - freshwater alga and daphnia acute toxicity (environmental hazard tiers)."],
"citations": [
"Fabrega, J., Luoma, S. N., Fishers, C. R., Tinker, N. A. & Lead, J. R. 'Silver nanoparticles: behaviour and effects in the aquatic environment' Environ. Int. 37, 517-531 (2011).",
"Hadrup, N. & Lam, H. R. 'Oral toxicity of silver ions, silver nanoparticles and colloidal silver - a review' Regul. Toxicol. Pharmacol. 68, 1-7 (2014)."],
"sig_lens": (
"Signature lens: nanosilver is the Signature controlled-release "
"problem - the product IS the ion, so banning the ion bans the "
"product. The Signature solution engineers the release curve itself: "
"fast enough at the microbe surface, near-zero everywhere else, with "
"the dissolution rate as a release specification printed on the "
"datasheet like any other performance number.")},
{
"key": "zno",
"name": "Zinc Oxide Nanoparticles: Sunscreens, Band Gaps, and Dissolution",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Zinc oxide nanoparticles sit on hundreds of millions of faces every "
"summer as sunscreen, and their toxicology is a tale of two "
"mechanisms. Mechanism one is the band gap: ZnO at 3.37 eV absorbs "
"UVA (absorption edge near 368 nm), and the excited electrons can "
"generate reactive oxygen species - the same physics that makes it a "
"photocatalyst. Mechanism two is dissolution: unlike titanium "
"dioxide, zinc oxide dissolves in biological fluids, releasing Zn2+ "
"ions, and zinc ions are toxic to cells at elevated concentrations. "
"Cell studies consistently rank nano-ZnO among the most cytotoxic "
"metal oxides, and the toxicity largely disappears when the released "
"ions are chelated away - the particle is guilty mainly as an ion "
"source. The sunscreen question was settled the same way as "
"titanium's: intact skin does not let the particles through, so the "
"dissolution happens on top of the skin, not inside the body. But "
"inhaled ZnO is a different story - welding fumes of zinc oxide have "
"caused metal fume fever for a century, and nano-ZnO dust is treated "
"with the same respect. The safety engineering is elegant: dope the "
"ZnO with iron and both dissolution and ROS generation drop "
"dramatically while UV absorption survives (Xia et al. 2008) - a "
"safer-by-design material made by changing a few percent of the "
"atoms."),
"how_it_works": (
"The band-gap mechanism is tested by comparing toxicity in light "
"versus dark and across oxides of different band gaps; the "
"dissolution mechanism is tested by measuring Zn2+ release (ICP-MS) "
"and by repeating the toxicity test with the ions chelated or with "
"the particle-free supernatant. The demo computes the optical "
"absorption edge from the band gap (wavelength = 1240 / eV): ZnO at "
"3.37 eV absorbs from 368 nm, TiO2 at 3.20 eV from 388 nm - placing "
"both squarely in the UVA band that reaches skin. Iron doping works "
"because Fe substitution changes the dissolution kinetics and the "
"electronic structure together: published work shows Fe-doped ZnO "
"dissolves far more slowly and generates less ROS, with cell death "
"falling in step. Sunscreen safety is assessed by dermal penetration "
"studies on human skin (Franz cells, tape stripping): the particles "
"stay in the stratum corneum, the dead outer layer. Workplace safety "
"is assessed by inhalation: treat nano-ZnO dust like any reactive "
"dust - capture it at the source, because the lung has no stratum "
"corneum."),
"key_points": [
"Two mechanisms: band-gap ROS (3.37 eV -> 368 nm UVA absorption) and Zn2+ ion release by dissolution.",
"Nano-ZnO ranks among the most cytotoxic metal oxides in vitro - mostly as an ion source (chelation removes it).",
"Intact skin blocks sunscreen ZnO (stays in the stratum corneum); inhaled ZnO dust is the real hazard (metal fume fever).",
"Fe-doping cuts both dissolution and ROS while keeping UV absorption - textbook safer-by-design.",
"Absorption edge arithmetic: wavelength(nm) = 1240 / band gap(eV).",
"Dissolution rate, not just size, belongs on the material safety datasheet."],
"requirements": [
"Band gap measurement (UV-vis diffuse reflectance) and light/dark toxicity comparison.",
"Dissolution rate in relevant fluids (lung simulant, sweat, culture medium) by ICP-MS.",
"Dermal penetration data for skin products; inhalation data for powders.",
"Ion-chelation controls to separate particle from ion effects."],
"standards": [
"ISO 18473-3:2018 - functional pigments: zinc oxide for sunscreen applications (characterization).",
"SCCS (EU) opinions on nano-ZnO in cosmetic products - dermal safety assessment framework."],
"citations": [
"Xia, T. et al. 'Comparison of the abilities of ambient and manufactured nanoparticles to induce cellular toxicity according to an oxidative stress paradigm' Nano Lett. 6, 1794-1807 (2006).",
"George, S. et al. 'Use of a rapid cytotoxicity screening approach to engineer a safer zinc oxide nanoparticle through iron doping' ACS Nano 4, 15-29 (2010)."],
"sig_lens": (
"Signature lens: ZnO is the Signature dual-mechanism case - light "
"chemistry plus ion chemistry in one particle. The Signature method "
"separates the mechanisms with controls (dark vs light, chelated vs "
"free), then engineers each one down independently: dope against "
"dissolution, coat against ROS, verify the sunscreen still blocks "
"UV.")},
{
"key": "quantum_dots",
"name": "Quantum Dots: Capped Heavy Metals in Bright Packages",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Quantum dots are semiconductor nanocrystals - typically cadmium "
"selenide or cadmium telluride cores a few nanometres across - whose "
"fluorescence color is set by their size: smaller dots glow bluer, "
"larger dots redder. They are among the brightest labels in biology "
"and the light source in premium displays, and they are also packages "
"of heavy metal: a 4 nm CdSe core holds roughly 600 cadmium atoms, each "
"one toxic if released. The entire safety story of quantum dots is the "
"integrity of the cap. Bare CdSe dots shed Cd2+ ions in oxidizing, "
"acidic, or UV-lit environments - exactly the conditions inside a cell "
"or a landfill - and the released cadmium drives the toxicity. Grow an "
"epitaxial zinc sulfide shell around the core and ion release drops by "
"orders of magnitude; add a polymer or silica outer coat and the dot "
"becomes a sealed package that cells tolerate far better. The field "
"has additionally moved toward cadmium-free dots (indium phosphide, "
"carbon dots) for consumer products, removing the hazard at the "
"source rather than containing it. The lesson generalizes: for any "
"nanomaterial with a toxic core, the coating is not packaging - it is "
"the safety device, and its lifetime under real conditions is the "
"safety specification."),
"how_it_works": (
"Quantum dot safety testing starts with the ion-release assay: dots "
"incubated in cell culture medium, lysosomal simulant (pH 4.5, the "
"acidic compartment cells use to digest particles), and under UV "
"illumination, with free Cd2+ measured by ICP-MS over days to weeks. "
"The demo computes the cadmium inventory of a 4 nm CdSe core (about "
"614 cadmium atoms from density 5.82 g/cm3) and the volume of a 1 nm "
"ZnS shell around it - showing how much toxic metal one invisible "
"particle carries and how thin the barrier containing it is. Shell "
"integrity is then challenged: oxidative conditions, ligand exchange "
"with biological thiols, and mechanical stress. Cytotoxicity is tested "
"with and without shell damage (e.g., UV pre-weathering); the "
"difference between intact and weathered dots is the safety margin of "
"the coating. For products, accelerated aging - heat, humidity, UV - "
"estimates the coating lifetime, and the design rule is simple: the "
"coating must outlive the product, or the product must use a "
"cadmium-free dot."),
"key_points": [
"A 4 nm CdSe core holds ~614 cadmium atoms - the hazard is the inventory, the safety is the cap.",
"Bare dots shed Cd2+ under oxidation, acidity (lysosomal pH 4.5), or UV; ZnS shells cut release by orders of magnitude.",
"Test ion release in lysosomal simulant and under UV - the conditions that break caps.",
"Cytotoxicity of weathered vs intact dots measures the coating's safety margin.",
"Cadmium-free dots (InP, carbon dots) remove the hazard at the source for consumer products.",
"For any toxic-core nanomaterial, the coating lifetime under real conditions is the safety specification."],
"requirements": [
"Ion-release kinetics in culture medium, lysosomal simulant (pH 4.5), and under UV.",
"Shell thickness and integrity characterization (TEM, XPS).",
"Cytotoxicity of intact versus pre-weathered (UV/oxidation-aged) dots.",
"Accelerated aging to estimate coating lifetime versus product lifetime."],
"standards": [
"ISO/TS 17200:2013 - nanotechnology: nanoparticles in powder form - characteristics and measurements.",
"IEC 62607-6 series - nanomanufacturing key control characteristics for nano-enabled products."],
"citations": [
"Derfus, A. M., Chan, W. C. W. & Bhatia, S. N. 'Probing the cytotoxicity of semiconductor quantum dots' Nano Lett. 4, 11-18 (2004).",
"Hardman, R. 'A toxicologic review of quantum dots: toxicity depends on physicochemical and environmental factors' Environ. Health Perspect. 114, 165-172 (2006)."],
"sig_lens": (
"Signature lens: quantum dots are the Signature sealed-package "
"problem - brilliant function wrapped around a toxic inventory. The "
"Signature audit counts the atoms inside, prices the shell in years "
"of integrity, and refuses any design where the package dies before "
"the product does.")},
{
"key": "nanoplastics",
"name": "Nanoplastics: Fragmentation and the Particle-Number Explosion",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Nanoplastics are the newest member of the nanotoxicology family and "
"the hardest to count. They are not manufactured - they are born when "
"macro- and microplastics fragment under UV, waves, and abrasion, "
"shedding ever-smaller pieces. The arithmetic of fragmentation is "
"terrifying: one gram of plastic (density ~1 g/cm3) fragmented into "
"100-nanometre spheres becomes about 1.9e15 particles carrying 60 "
"square metres of surface - a number no cleanup can chase. The "
"toxicology is young but the early signals follow familiar "
"nanotoxicology scripts: small polystyrene spheres cross the gut "
"barrier in animal studies at low fractions, accumulate in liver and "
"spleen, trigger oxidative stress and inflammation in cells, and their "
"large hydrophobic surfaces adsorb pollutants and additives "
"(plasticizers, flame retardants) that hitchhike into tissue. Two "
"features make nanoplastics special. First, the dose is "
"environmental and involuntary - drinking water, seafood, air - so "
"exposure assessment means measuring the invisible in complex "
"matrices. Second, every particle is chemically different: polymer "
"type, additives, weathering state, and adsorbed pollutants vary "
"piece by piece, defeating the 'one material, one dossier' model "
"that works for manufactured nanomaterials. The engineering response "
"is upstream: stop the fragmentation by designing plastics that do "
"not shed, and capture microplastics before they become "
"nanoplastics."),
"how_it_works": (
"Nanoplastic research has a measurement problem first and a "
"toxicology problem second: below ~1 micrometre, FTIR and Raman "
"microscopy go blind, so the field uses pyrolysis-GC-MS (burn the "
"particles, identify the polymer from the smoke), asymmetric flow "
"field-flow fractionation, and single-particle ICP-MS with carbon "
"detection. The demo performs the fragmentation arithmetic for one "
"gram of plastic at 100 nm - 1.9e15 particles, 60 m2 of new surface - "
"to show why mass-based monitoring misses the story. Toxicity "
"testing uses model polystyrene spheres (well-characterized, "
"fluorescently labeled) to establish the mechanisms - gut "
"translocation fractions, oxidative stress, inflammation - then "
"checks the findings against weathered, additive-containing real "
"fragments, which are consistently more active. The Trojan-horse "
"effect is tested by loading particles with a pollutant, then "
"measuring tissue levels with and without the particle carrier. "
"Because the particles are heterogeneous, risk assessment works "
"with bounding scenarios (worst-plausible polymer, highest additive "
"load) rather than single-material dossiers - and the durable fix "
"is material design: polymers that resist fragmentation and "
"products that do not shed."),
"key_points": [
"1 g of plastic at 100 nm = ~1.9e15 particles and 60 m2 of surface - fragmentation is a number explosion.",
"Below ~1 um, standard microplastic methods go blind; pyrolysis-GC-MS and AF4 take over.",
"Early toxicology follows familiar scripts: gut translocation, liver/spleen accumulation, oxidative stress.",
"Trojan-horse effect: hydrophobic surfaces carry adsorbed pollutants and additives into tissue.",
"Every particle differs (polymer, additives, weathering) - risk works in bounding scenarios, not single dossiers.",
"The durable fix is upstream: non-shedding materials and microplastic capture before nano formation."],
"requirements": [
"Polymer identification in the nano range (pyrolysis-GC-MS, AF4, sp-ICP-MS).",
"Model particle studies (labeled polystyrene) plus weathered-fragment verification.",
"Trojan-horse testing: pollutant-loaded versus clean particles.",
"Bounding-scenario exposure estimates for drinking water, food, and air."],
"standards": [
"ISO/DIS 24187 - principles for the analysis of microplastics (nano extension in development).",
"OECD test guidelines for particle toxicity (adapted): TG 412/413 inhalation, TG 407 oral."],
"citations": [
"Gigault, J. et al. 'Current opinion: What is a nanoplastic?' Environ. Pollut. 235, 1030-1034 (2018).",
"Lehner, R., Weder, C., Petri-Fink, A. & Rothen-Rutishauser, B. 'Emergence of nanoplastic in the environment and possible impact on human health' Environ. Sci. Technol. 53, 1748-1765 (2019)."],
"sig_lens": (
"Signature lens: nanoplastics are the Signature uncountable problem - "
"a hazard manufactured by accident, in numbers no instrument can "
"fully census. The Signature response refuses to chase particles "
"and instead chokes the source: materials engineered not to shed, "
"products engineered not to fragment, capture placed where micro "
"becomes nano.")},
{
"key": "cnt",
"name": "Carbon Nanotubes: The Fiber Paradigm and the Asbestos Analogy",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Carbon nanotubes forced nanotoxicology to remember an old lesson: "
"shape can matter more than chemistry. A multi-walled carbon "
"nanotube 10 micrometres long and 50 nanometres wide has an aspect "
"ratio of 200 - a fiber by any definition - and when such fibers "
"reach the lung or the abdominal cavity, macrophages try to engulf "
"them, fail, and spill inflammatory signals in a process called "
"frustrated phagocytosis. In 2008, Poland and colleagues injected "
"long multi-walled nanotubes into the abdominal cavity of mice and "
"observed asbestos-like inflammation and granulomas - the pilot "
"study that made the asbestos analogy concrete. The fiber paradigm "
"(Donaldson et al. 2006) states the rules: fibers longer than ~5 "
"micrometres, thinner than ~3 micrometres, with aspect ratio above "
"3:1, that persist in tissue, behave like asbestos. Short, tangled, "
"or rapidly cleared tubes do not. This is why regulators treat "
"carbon nanotubes and nanofibers as a category of concern rather "
"than banning 'carbon nanotubes' as a substance: a 200 nm tangled "
"clump and a 15 um rigid fiber share a name and almost nothing "
"else. NIOSH's response was the first nanomaterial-specific "
"exposure limit in the United States: 1 microgram per cubic metre "
"of elemental carbon as an 8-hour average (CIB 65, 2013). The "
"engineering controls follow the fiber: never handle dry long "
"tubes in the open, grow them bound to substrates where possible, "
"and design short or functionalized tubes that macrophages can "
"clear."),
"how_it_works": (
"The fiber paradigm is tested by length-fractionated samples: the "
"same nanotube material separated into long (>5 um) and short "
"fractions, then compared in macrophage assays (frustrated "
"phagocytosis scored by microscopy), in lung instillation studies "
"(inflammation and fibrosis at equal mass doses), and in the "
"peritoneal model that revealed the asbestos-like response. The "
"demo applies the WHO fiber counting rules to a 10 um by 50 nm "
"multi-walled tube - length 10 um (>5), diameter 0.05 um (<3), "
"aspect ratio 200 (>3) - and confirms it meets all three fiber "
"criteria, then shows a 50 nm sphere failing them. Biopersistence "
"is measured in parallel: how long the fibers survive in lung "
"simulant fluid, because a fiber that dissolves in weeks is a "
"different hazard than one that persists for years. Workplace "
"exposure is measured as elemental carbon by NIOSH Method 5040, "
"since weighing nanotubes directly is impractical at microgram "
"levels. Control verification closes the loop: enclosures and "
"local exhaust are tested by measuring airborne elemental carbon "
"during real handling tasks, proving the fiber never reaches the "
"breathing zone."),
"key_points": [
"Shape beats chemistry: long rigid CNTs trigger frustrated phagocytosis and asbestos-like pathology.",
"Fiber paradigm (WHO rules): length >5 um, diameter <3 um, aspect ratio >3:1, biopersistent.",
"Poland et al. 2008: long MWCNTs in mouse peritoneum produced asbestos-like inflammation - the analogy made concrete.",
"Short, tangled, or fast-clearing tubes do not follow the paradigm - regulate the fiber, not the name.",
"NIOSH CIB 65 (2013): 1 ug/m3 elemental carbon, 8-h TWA - the first US nanomaterial-specific limit.",
"Controls: no open handling of dry long tubes; substrate-bound growth; short/functionalized designs that clear."],
"requirements": [
"Length and diameter distributions by electron microscopy (fiber counting per WHO rules).",
"Length-fractionated samples for paradigm testing (long vs short fractions).",
"Biopersistence in lung simulant fluid.",
"Workplace elemental carbon measurement (NIOSH 5040) during real tasks."],
"standards": [
"NIOSH CIB 65 (2013) - occupational exposure to carbon nanotubes and nanofibers (1 ug/m3 REL).",
"ISO/TS 12025:2012 - quantification of nano-object release from powders by generation of aerosols."],
"citations": [
"Poland, C. A. et al. 'Carbon nanotubes introduced into the abdominal cavity of mice show asbestos-like pathogenicity in a pilot study' Nat. Nanotechnol. 3, 423-428 (2008).",
"Donaldson, K. et al. 'Carbon nanotubes: a review of their properties in relation to pulmonary toxicology and workplace safety' Toxicol. Sci. 92, 5-22 (2006)."],
"sig_lens": (
"Signature lens: nanotubes are the Signature shape problem - the "
"same atoms, arranged as a fiber, become a different hazard class. "
"The Signature rule sorts every high-aspect material through the "
"fiber gate first (length, thinness, persistence) and designs away "
"from the gate: short, tangled, clearable, or bound - never long, "
"rigid, and loose.")},
{
"key": "graphene",
"name": "Graphene and Graphene Oxide: Sheets With Sharp Edges",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"Graphene is a single atomic layer of carbon - all surface, no "
"bulk - and its toxicology is written on its edges. A gram of "
"1-micrometre graphene flakes carries roughly 5 million kilometres "
"of edge, and edges are chemically reactive: dangling bonds, "
"oxidized groups on graphene oxide, sites that generate ROS and "
"snag cell membranes. Cell studies show graphene-family materials "
"can slice or extract lipids from membranes (the 'nanosheet "
"piercing' seen in simulations and microscopy), trigger oxidative "
"stress, and - for graphene oxide - cause dose-dependent lung "
"inflammation when inhaled, with the lateral size deciding the "
"fate: large sheets frustrate macrophages like fibers do, small "
"sheets are engulfed and cleared. Graphene oxide adds its own "
"chemistry: a dense coat of epoxide, hydroxyl, and carboxyl groups "
"that makes it dispersible in water (good for processing, bad for "
"keeping it out of biology) and redox-active. The occupational "
"picture resembles the nanotube one - dry powder handling of "
"platelets demands the same containment - but the material offers "
"its own safety dials: smaller lateral size, reduced (less "
"oxidized) forms, and covalent functionalization that blunts edge "
"reactivity while keeping conductivity. As graphene moves from lab "
"to ton-scale production, the edge is the hazard to engineer."),
"how_it_works": (
"Graphene toxicology starts with lateral-size fractionation: the "
"same chemistry in 100 nm, 1 um, and 10 um sheets, tested in "
"macrophage uptake assays (can the cell engulf it?), membrane "
"integrity assays (LDH leakage as sheets pierce membranes), and "
"lung instillation (inflammation versus lateral size). The demo "
"computes the edge inventory - for 1 um flakes at graphene's areal "
"density of 7.7e-7 kg/m2, one gram holds ~1.3e15 flakes with ~5.2 "
"million kilometres of total edge - to make the 'all surface, no "
"bulk' claim quantitative. Edge reactivity is measured by ROS "
"assays and by lipid extraction experiments; functionalization "
"coverage (degree of oxidation, grafted groups) is measured by "
"XPS and Raman, then correlated with the toxicity readouts to "
"find the coverage that pacifies the edge. Graphene oxide's "
"dispersibility is both the processing advantage and the "
"exposure risk: stable aqueous dispersions aerosolize easily, so "
"drying and powder-transfer steps get the containment, and "
"workplace air is monitored for respirable platelets."),
"key_points": [
"One gram of 1 um graphene flakes carries ~5.2 million km of reactive edge - all surface, no bulk.",
"Edges pierce membranes and generate ROS; large sheets frustrate macrophages like fibers.",
"Lateral size decides fate: small sheets engulfed and cleared, large sheets persist and inflame.",
"Graphene oxide's oxygen groups make it water-dispersible (processable) and redox-active (hazardous).",
"Safety dials: smaller lateral size, reduced oxidation, covalent edge functionalization.",
"Dry platelet handling gets nanotube-grade containment; monitor respirable platelets in air."],
"requirements": [
"Lateral-size distribution (AFM/SEM) and layer number (Raman).",
"Oxidation state and functionalization coverage (XPS).",
"Size-fractionated toxicity comparison (same chemistry, different lateral size).",
"Workplace monitoring for respirable platelets during powder handling."],
"standards": [
"ISO/TS 80004-13:2017 - vocabulary for graphene and related 2D materials.",
"ISO/TS 21356-2:2021 - structural characterization of graphene (layer number, lateral size)."],
"citations": [
"Seabra, A. B., Paula, A. J., de Lima, R., Alves, O. L. & Duran, N. 'Nanotoxicity of graphene and graphene oxide' Chem. Res. Toxicol. 27, 159-168 (2014).",
"Hu, X. & Zhou, Q. 'Health and ecosystem risks of graphene' Chem. Rev. 113, 3815-3835 (2013)."],
"sig_lens": (
"Signature lens: graphene is the Signature edge problem - a "
"material whose hazard lives entirely on its perimeter. The "
"Signature practice inventories the edge like a coastline, then "
"pacifies it: functionalize the border, shrink the territory, and "
"never let a dry platelet become airborne.")},
{
"key": "protein_corona",
"name": "The Protein Corona: A Nanoparticle's Biological Identity",
"group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
"description": (
"The moment a nanoparticle enters blood, lung fluid, or culture "
"medium, it stops being the particle the manufacturer made. "
"Proteins adsorb to its surface within seconds, forming the "
"protein corona - a 'hard' inner layer of tightly bound proteins "
"and a 'soft' outer layer that exchanges with the surroundings. "
"Cells never meet the bare particle; they meet the corona, and "
"the corona decides the outcome: which receptors engage, whether "
"macrophages attack or ignore, where the particle distributes. "
"A striking finding (Monopoli et al. 2012): the corona, not the "
"synthetic surface, is the particle's biological identity. The "
"corona depends on the particle (size, charge, hydrophobicity "
"select which proteins bind) and on the fluid (blood versus lung "
"lining fluid give different coronas), which is why the same "
"particle behaves differently in different assays - and why "
"serum-free cell tests can mislead. For safety engineering the "
"corona is a dial: dense PEG brushes suppress protein adsorption "
"and extend circulation; certain surface chemistries recruit "
"albumin (a 'don't eat me' signal) over complement proteins (an "
"'eat me' signal). Characterize the corona and you can predict "
"the biology; ignore it and you are testing a stranger."),
"how_it_works": (
"The corona is isolated by incubating particles in the biological "
"fluid, then separating particle-protein complexes by "
"centrifugation and identifying the bound proteins by mass "
"spectrometry (proteomics) - typically dozens to hundreds of "
"proteins, with the hard corona enriched in specific binders. "
"Binding is quantified by adsorption isotherms: the demo uses a "
"Langmuir model (bound fraction = Bmax*C/(Kd+C)) showing ~91% "
"surface coverage at 1 mg/mL protein but only ~9% at 0.01 mg/mL, "
"which is why dilute assays behave differently from blood. "
"Corona thickness adds ~10 nm to the hydrodynamic diameter - "
"measured by dynamic light scattering before and after "
"incubation - changing diffusion and deposition. The safety "
"relevance is tested by comparing bare versus pre-coronated "
"particles in cell uptake and inflammation assays: pre-forming an "
"albumin corona often reduces macrophage uptake and cytokine "
"release. The design rule: engineer the surface for the corona "
"you want (PEG density, charge, hydrophobicity), then verify the "
"corona in the actual exposure fluid - blood for injectables, "
"lung lining fluid for inhaled particles."),
"key_points": [
"Cells meet the protein corona, never the bare particle - the corona is the biological identity.",
"Hard corona (tightly bound) + soft corona (exchanging); composition depends on particle AND fluid.",
"Same particle, different fluid = different corona = different biology - serum-free tests can mislead.",
"Langmuir binding: ~91% coverage at 1 mg/mL protein vs ~9% at 0.01 mg/mL in the model.",
"Corona is a design dial: PEG brushes suppress adsorption; albumin recruitment calms macrophages.",
"Verify the corona in the real exposure fluid (blood, lung lining fluid), not just culture medium."],
"requirements": [
"Corona isolation (incubation + centrifugation) and proteomic identification.",
"Adsorption isotherms across protein concentrations.",
"Hydrodynamic size before/after corona formation (DLS).",
"Bare vs pre-coronated comparison in uptake and inflammation assays."],
"standards": [
"ISO/TR 16197:2014 - toxicological screening methods for manufactured nanomaterials (fluid considerations).",
"MIRIBEL (Minimum Information Reporting in Bio-Nano Experimental Literature) - reporting standard for corona studies."],
"citations": [
"Monopoli, M. P., Aberg, C., Salvati, A. & Dawson, K. A. 'Biomolecular coronas provide the biological identity of nanosized materials' Nat. Nanotechnol. 7, 779-786 (2012).",
"Walkey, C. D. & Chan, W. C. W. 'Understanding and controlling the interaction of nanomaterials with proteins in a physiological environment' Chem. Soc. Rev. 41, 2780-2799 (2012)."],
"sig_lens": (
"Signature lens: the corona is the Signature disguise problem - "
"the particle arrives in costume and the body reacts to the "
"costume. The Signature engineer designs the costume deliberately: "
"choose the surface that recruits a calm corona in the fluid the "
"product will actually meet, and prove it with proteomics.")},
{
"key": "in_vitro",
"name": "In Vitro Screening: The Tier-1 Assay Toolbox",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Before any animal is involved, nanomaterials face the tier-1 "
"toolbox: cell-based assays that rank hazard quickly and cheaply. "
"The standard battery covers the mechanisms that matter - cell "
"death (MTT, LDH, ATP assays), oxidative stress (DCFH fluorescence, "
"glutathione depletion), inflammation (IL-6, IL-8, TNF-alpha "
"release from macrophages), and DNA damage (comet assay, "
"micronucleus). Lung models use alveolar epithelial cells and "
"macrophages, often co-cultured, because inhalation is the "
"workplace route; dose is expressed per cell-surface area or per "
"millilitre, and - critically - the delivered dose (what reaches "
"the cells) is distinguished from the administered dose (what was "
"pipetted), since particles settle, diffuse, and agglomerate "
"differently. In vitro screening is fast and mechanism-rich, but "
"it has two famous failure modes: particles interfere with the "
"assays themselves (the subject of the next record), and a dish "
"lacks clearance, translocation, and chronic inflammation - so a "
"clean in vitro result reduces concern but never proves safety, "
"while a dirty one reliably flags materials needing deeper "
"testing. Used correctly, the toolbox triages dozens of material "
"variants to the few worth testing in animals."),
"how_it_works": (
"A tier-1 screen runs the material across 4-6 doses plus "
"controls in 96-well plates: viability at 24 h, ROS at 4-6 h, "
"cytokines at 24 h, DNA damage at 4-24 h. The demo illustrates "
"the central arithmetic pitfall with the MTT viability assay: a "
"true viability of 40% (OD 0.40 on a 1.00 control) plus a "
"nanoparticle absorbance artifact of 0.15 OD reads as 55% "
"viability - a 15-point underestimate of toxicity that vanishes "
"only when the cell-free particle control is subtracted. Dose "
"is converted to delivered dose with sedimentation-diffusion "
"models (the ISDD model): for dense, large agglomerates most of "
"the administered dose reaches the cells within hours; for small, "
"buoyant particles, a fraction does. Results are reported as "
"EC50 values with the interference controls shown, and materials "
"are ranked - not judged - because the dish cannot model the "
"lung's clearance or the body's distribution. The output of "
"tier 1 is a priority list, and the top (most hazardous) entries "
"earn the expensive in vivo follow-up."),
"key_points": [
"Tier-1 battery: viability, oxidative stress, inflammation (cytokines), DNA damage - in lung-relevant cells.",
"Delivered dose (reaching cells) differs from administered dose (pipetted) - model it (ISDD).",
"MTT example: true 40% viability + 0.15 OD particle artifact reads as 55% - always run cell-free controls.",
"Clean in vitro reduces concern but never proves safety; dirty in vitro reliably flags deeper testing.",
"Report EC50s with interference controls shown; the output is a priority ranking, not a verdict.",
"Triages dozens of variants to the few worth animal testing - speed with honesty about limits."],
"requirements": [
"Lung-relevant cells (alveolar epithelial + macrophages, ideally co-cultured).",
"4-6 dose levels plus full interference controls (cell-free, dye-only, particle-only).",
"Delivered-dose modeling (sedimentation-diffusion) for the specific particles.",
"Standardized dispersion protocol so the tested material matches the exposure material."],
"standards": [
"ISO 10993-5:2009 - in vitro cytotoxicity (framework; nanomaterial interference controls required).",
"OECD Guidance Document 317 (2022) - aquatic and sediment toxicological testing of nanomaterials (assay adaptation principles)."],
"citations": [
"Drasler, B., Sayre, P., Steinhaueser, K. G., Petri-Fink, A. & Rothen-Rutishauser, B. 'In vitro approaches to assess the hazard of nanomaterials' NanoImpact 8, 99-116 (2017).",
"Gottardo, S. et al. 'Towards safe and sustainable innovation in nanotechnology: State-of-play for smart nanomaterials' NanoImpact 8, 1-3 (2017)."],
"sig_lens": (
"Signature lens: tier-1 screening is the Signature triage desk - "
"fast, cheap, and honest about its blind spots. The Signature "
"rule runs every material variant through the same battery with "
"the same interference controls, ranks without mercy, and spends "
"animal testing only on the winners of the hazard ranking.")},
{
"key": "assay_interference",
"name": "When Nanoparticles Lie to the Assay: Interference and Artifacts",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Nanoparticles are the worst-behaved guests in the toxicology lab: "
"they absorb light, scatter light, quench fluorescence, adsorb dyes, "
"bind assay proteins, and catalyze the very reactions the assay "
"measures. Carbon nanotubes absorb across the visible spectrum, so a "
"MTT viability assay reads their blackness as living cells. Titanium "
"dioxide scatters the excitation light of fluorescent ROS probes. "
"Silver nanoparticles quench fluorescence by energy transfer. Porous "
"particles soak up the cytokine the ELISA is trying to measure, "
"reporting 'no inflammation' while the cells scream. The literature "
"carries the scars: early studies that declared materials safe or "
"toxic on the basis of pure artifact, corrected only when someone ran "
"the cell-free controls. The defense is procedural and non-negotiable: "
"every colorimetric or fluorescent assay gets a particle-only control "
"(particles + reagents, no cells), a spike-recovery control (known "
"analyte + particles, measuring how much signal the particles eat), "
"and wherever possible an orthogonal label-free readout (impedance, "
"microscopy counts) that the particles cannot fool optically. A "
"nanotoxicology result without interference controls is not a result - "
"it is a rumor. The competent lab treats every new particle-assay "
"pair as guilty until proven innocent."),
"how_it_works": (
"Interference testing follows a fixed panel. Optical interference: "
"run the full assay chemistry with particles and no cells across the "
"dose range - any signal is artifact, and it is subtracted or the "
"assay is abandoned for that particle. Adsorption: spike a known "
"amount of the analyte (cytokine standard, formazan dye) into "
"particle suspension and measure recovery - the demo models a DCF "
"ROS probe quenched 30% by particles (100 RFU true reads 70), giving "
"a correction factor of 1.43 that must divide every reading. "
"Catalytic interference: some particles (ceria, iron oxides) run "
"redox chemistry that mimics or masks the biological endpoint - "
"tested by comparing the particle's chemistry in cell-free buffer "
"versus its cellular effect. Endotoxin: bacterial contamination on "
"particles fakes inflammation perfectly, so every particle batch is "
"LAL-tested, with the caveat that particles also interfere with "
"the LAL assay itself (test at multiple dilutions). The reporting "
"rule: publish the interference panel alongside the toxicity data, "
"because a reader who cannot see the controls cannot judge the "
"claim."),
"key_points": [
"Particles absorb, scatter, quench, adsorb, and catalyze - every optical assay is a suspect.",
"Cell-free particle-only controls are non-negotiable; a result without them is a rumor.",
"Spike-recovery measures signal eaten by particles (demo: 30% quench -> 1.43x correction factor).",
"Porous particles adsorb cytokines and dyes - use orthogonal label-free readouts (impedance, counts).",
"Endotoxin contamination fakes inflammation; LAL-test every batch (particles interfere with LAL too).",
"Publish the interference panel with the toxicity data - controls are part of the result."],
"requirements": [
"Particle-only controls for every colorimetric/fluorescent assay at every dose.",
"Spike-recovery controls for adsorption-prone endpoints (cytokines, dyes).",
"At least one orthogonal non-optical readout per key finding.",
"Endotoxin testing of every particle batch."],
"standards": [
"ISO 29701:2010 - endotoxin test on nanomaterial samples for in vitro systems (LAL test).",
"OECD GD 317 - assay interference considerations for nanomaterial testing."],
"citations": [
"Kroll, A., Pillukat, M. H., Hahn, D. & Schnekenburger, J. 'Interference of engineered nanoparticles with in vitro toxicity assays' Arch. Toxicol. 86, 1123-1136 (2012).",
"Guadagnini, R. et al. 'Toxicity screenings of nanomaterials: challenges due to interference with assay processes and components of classic in vitro tests' Nanotoxicology 9 (Suppl 1), 13-24 (2015)."],
"sig_lens": (
"Signature lens: interference is the Signature honesty tax - the "
"instrument lies, and the tax is paid in controls. The Signature "
"lab budgets the tax upfront: every assay ships with its "
"particle-only and spike-recovery receipts, and any finding that "
"cannot survive its controls is discarded, not published.")},
{
"key": "in_vivo",
"name": "In Vivo Testing: Biokinetics and Lung Burden in Animal Models",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Cells in dishes cannot cough, clear mucus, or distribute particles "
"through a body - so the decisive nanotoxicology still happens in "
"animals, usually rats. The workhorse is the repeated-dose "
"inhalation study: rats breathe the test aerosol 6 hours a day, 5 "
"days a week, for 28 days (OECD TG 412) or 90 days (TG 413), at a "
"control plus three concentrations. Endpoints are the lung's "
"complaint log: inflammatory cells and proteins in bronchoalveolar "
"lavage fluid, lung weight, histopathology (inflammation, fibrosis, "
"granulomas), plus the lung burden - how much material stayed - and "
"organ burdens in liver, spleen, and brain for translocation. A "
"critical design choice is the top dose: it must produce a response "
"without causing lung overload, the state where deposited particles "
"paralyze macrophage clearance and every subsequent dose piles onto "
"a failing system (the overload line sits near 1 mg per rat lung for "
"poorly soluble particles). Studies that blow past overload measure "
"the overload, not the material - the TiO2 rat tumors came from "
"exactly this regime. Done right, the study yields the two numbers "
"regulators need: the no-observed-adverse-effect concentration "
"(NOAEC) and the lung burden at that concentration, which - scaled "
"by deposition and clearance differences - becomes the human "
"exposure limit."),
"how_it_works": (
"Dose arithmetic opens the study design: the demo computes a rat "
"6-hour exposure at 5 mg/m3 - minute volume 0.15 L/min gives 54 "
"litres (0.054 m3) inhaled, 0.27 mg total, and at 30% alveolar "
"deposition, 0.081 mg deposited - about 8% of the ~1 mg overload "
"threshold, safely in the responsive-but-not-overloaded window. "
"Aerosol generation must hold the particle size distribution steady "
"for 6 hours (dry powder dispersers or nebulizers with real-time "
"sizing), because a drifting aerosol is a drifting dose. Lung "
"burden is measured by elemental analysis of digested lung tissue "
"at multiple time points, giving the clearance curve; lavage at "
"the end of exposure and after recovery periods separates "
"reversible inflammation from persistent fibrosis. Biokinetics - "
"blood and organ time courses - feed compartment models that "
"predict human burden from the rat data. The ethical and economic "
"pressure is real (a TG 413 study uses 80 rats and costs "
"accordingly), which is why tier-1 in vitro screening triages "
"materials first and why new approach methods aim to replace the "
"90-day study - but today, the inhalation study remains the "
"regulatory gold standard."),
"key_points": [
"Workhorse: OECD TG 412 (28-day) / TG 413 (90-day) repeated-dose inhalation in rats, 6 h/day.",
"Demo: 5 mg/m3 x 6 h in the rat = 0.081 mg deposited - ~8% of the ~1 mg overload threshold.",
"Top dose must respond WITHOUT causing lung overload - overloaded studies measure overload, not the material.",
"Outputs regulators need: NOAEC + lung burden at NOAEC, scaled to humans.",
"Endpoints: lavage inflammation, histopathology, lung burden over time, organ translocation.",
"TG 413 uses 80 rats - tier-1 screening triages first; new methods aim to replace it."],
"requirements": [
"Stable test aerosol with continuous size-distribution monitoring for 6 h/day.",
"Control + 3 concentrations with the top dose below overload.",
"Lung burden time course (elemental analysis) plus recovery-period lavage.",
"Organ burdens (liver, spleen, brain) for translocation assessment."],
"standards": [
"OECD TG 412 - subacute inhalation toxicity: 28-day study.",
"OECD TG 413 - subchronic inhalation toxicity: 90-day study."],
"citations": [
"Warheit, D. B., Sayes, C. M., Reed, K. L. & Swain, K. A. 'Health effects related to nanoparticle exposures: environmental, health and safety considerations for assessing hazards and risks' Pharmacol. Ther. 120, 35-42 (2008).",
"Pauluhn, J. 'Subchronic 13-week inhalation exposure of rats to multiwalled carbon nanotubes: toxic effects on the lung and relevance for human risk assessment' Toxicology 280, 152-157 (2011)."],
"sig_lens": (
"Signature lens: the inhalation study is the Signature courtroom - "
"expensive, formal, and final. The Signature practice never enters "
"it unprepared: tier-1 screening builds the case, dose arithmetic "
"sets the charges (below overload), and the verdict sought is a "
"number - the NOAEC - clean enough to become law.")},
{
"key": "clearance",
"name": "Pulmonary Clearance: Macrophages and the Overload Line",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"The lung has a cleaning crew - alveolar macrophages that patrol "
"the air sacs, engulf deposited particles, and ride the mucociliary "
"escalator up and out - and nanotoxicology is largely the study of "
"what defeats that crew. For ordinary dust the system works: "
"retained particle burden in the rat lung halves roughly every 60-70 "
"days. But macrophages have a finite appetite. When the deposited "
"volume overwhelms them - around 1 mg of poorly soluble particles "
"per rat lung, the overload threshold identified by Morrow - "
"clearance stalls, particles accumulate, chronic inflammation sets "
"in, and at the extreme, tumors follow. This is the mechanistic "
"explanation for the high-dose TiO2 and carbon black rat tumors: "
"not a nano-specific carcinogen, but a janitor strike. Nanoparticles "
"reach overload at lower MASS than coarse dust because the same mass "
"is far more particles and surface - the crew counts objects, not "
"milligrams. And some materials defeat clearance without overload: "
"long fibers that macrophages cannot fully engulf (frustrated "
"phagocytosis), and biopersistent sheets that resist digestion. The "
"engineering lesson is quantitative: keep workplace air "
"concentrations such that a working lifetime of deposition stays "
"far below the human-scaled overload burden, and design particles "
"that macrophages can actually finish - small, compact, and not "
"fibrous."),
"how_it_works": (
"Clearance is measured as the lung burden over time after exposure "
"ends: elemental analysis of lungs at intervals, fitted to an "
"exponential (or two-phase) decay. The demo runs the textbook "
"numbers - normal rat clearance half-time of 65 days leaves only "
"~2% of the burden after a year, while an overloaded lung (half-"
"time stretched to 300 days) still holds ~43% - showing how "
"overload converts a self-cleaning organ into a particle "
"reservoir. Macrophage function is tested directly: lavaged "
"macrophages fed fluorescent particles, measuring uptake rate and "
"the volume at which uptake stalls (the volumetric overload "
"hypothesis says the crew fills up by volume, ~6% of macrophage "
"volume, which is why low-density agglomerates overload at lower "
"mass). Fiber clearance gets its own assay: length-dependent "
"phagocytosis scoring under the microscope. For risk assessment, "
"the rat overload burden is scaled to humans by lung surface area "
"or macrophage pool size, and exposure limits are set so that a "
"45-year working lifetime accumulates a small fraction of it - "
"the quantitative backbone behind every particle exposure limit."),
"key_points": [
"Alveolar macrophages clear particles up the mucociliary escalator; normal rat half-time ~65 days.",
"Overload threshold ~1 mg per rat lung: clearance stalls, inflammation becomes chronic.",
"Demo: after 1 year, normal clearance leaves ~2% of burden; overloaded leaves ~43%.",
"Nanoparticles overload at lower mass - macrophages count objects and volume, not milligrams.",
"Long fibers and biopersistent sheets defeat clearance without overload (frustrated phagocytosis).",
"Limits are set so a working lifetime accumulates a small fraction of the human-scaled overload burden."],
"requirements": [
"Post-exposure lung burden time course (elemental analysis at multiple intervals).",
"Macrophage uptake and volumetric capacity assays.",
"Fiber length-dependent phagocytosis scoring.",
"Human scaling by lung surface area or macrophage pool for limit-setting."],
"standards": [
"OECD TG 413 - 90-day inhalation study with recovery period (clearance assessment).",
"ISO/TR 16197:2014 - toxicological screening methods (clearance considerations)."],
"citations": [
"Morrow, P. E. 'Possible mechanisms to explain dust overloading of the lungs and implications for pulmonary particle dosimetry' Toxicol. Pathol. 16, 113-114 (1988).",
"Oberdorster, G. 'Lung particle overload: implications for occupational exposures to particles' Regul. Toxicol. Pharmacol. 27, 123-135 (1995)."],
"sig_lens": (
"Signature lens: clearance is the Signature janitor contract - "
"the lung agrees to clean up what industry deposits, up to a "
"stated volume. The Signature engineer reads the contract before "
"designing the particle: small enough to be carried, compact "
"enough to be finished, never fibrous, and emitted at rates the "
"crew can actually clear in a working lifetime.")},
{
"key": "genotoxicity",
"name": "Genotoxicity: DNA Damage at the Nanoscale",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Can a nanoparticle damage DNA? The answer matters more than "
"almost any other endpoint, because DNA damage is the gateway to "
"mutation and cancer. Nanoparticles damage DNA by three routes. "
"Direct: particles small enough to enter the nucleus (or present "
"during cell division when the nuclear membrane dissolves) can "
"physically interact with DNA - demonstrated for some metal "
"particles. Indirect and dominant: reactive oxygen species generated "
"at particle surfaces oxidize DNA bases (8-oxo-guanine is the "
"classic lesion) without the particle ever touching the nucleus. "
"Secondary: chronic inflammation recruits neutrophils whose own ROS "
"barrage damages DNA in neighboring cells - the route behind "
"fiber-induced genotoxicity. Testing follows the standard battery "
"adapted for particles: the comet assay (single-cell gel "
"electrophoresis - damaged DNA streams out of the nucleus like a "
"comet tail), the micronucleus test (chromosome fragments left "
"behind as small satellite nuclei), and the Ames bacterial test "
"(largely useless for particles - bacteria don't engulf them, a "
"famous false-negative trap). A positive in vitro result triggers "
"in vivo follow-up (bone marrow or lung micronucleus); a positive "
"there triggers risk management. The TiO2 food-additive saga turned "
"on exactly this endpoint: genotoxicity concerns that could not be "
"ruled out."),
"how_it_works": (
"The comet assay is the workhorse: cells embedded in agarose, "
"lysed, electrophoresed - broken DNA migrates, forming a tail "
"whose moment (tail length times fraction of DNA in the tail) "
"quantifies damage. The demo computes a tail moment of 6.0 for "
"exposed cells (20 um tail, 30% of DNA migrated) versus 1.5 for "
"controls (15 um, 10%) - a 4-fold increase, the kind of signal "
"that demands follow-up. Nanoparticle-specific controls are "
"essential: run the assay in the dark versus light for "
"photocatalytic particles (UV during the assay can fake damage), "
"check that particles don't quench the DNA stain, and include an "
"antioxidant rescue arm - if antioxidants erase the damage, the "
"mechanism is ROS (indirect), which changes the risk picture "
"versus direct DNA binders. The micronucleus test (OECD TG 487 in "
"vitro, TG 474 in vivo) catches chromosome breakage the comet "
"misses. Interpretation rule: in vitro positive + in vivo "
"negative at relevant doses = lower concern; in vivo positive = "
"manage as a genotoxicant, because the dose-response may have no "
"safe threshold."),
"key_points": [
"Three routes: direct nuclear entry, ROS-mediated base oxidation (dominant), inflammation-driven secondary damage.",
"Comet assay tail moment quantifies damage (demo: 6.0 exposed vs 1.5 control = 4x signal).",
"Ames bacterial test gives false negatives for particles - bacteria don't engulf them.",
"Controls: dark vs light (photocatalytic artifacts), stain quenching, antioxidant rescue to prove ROS mechanism.",
"In vitro positive triggers in vivo follow-up; in vivo positive is managed as a genotoxicant.",
"TiO2 food-additive decisions turned on genotoxicity that could not be ruled out."],
"requirements": [
"Comet assay with nanoparticle-specific controls (light/dark, stain quenching).",
"Micronucleus test in vitro (TG 487) with in vivo follow-up (TG 474) on positives.",
"Antioxidant rescue arm to distinguish ROS-mediated from direct mechanisms.",
"Demonstrated cellular uptake (or nuclear access during mitosis) for direct-mechanism claims."],
"standards": [
"OECD TG 487 - in vitro mammalian cell micronucleus test.",
"OECD TG 474 - mammalian erythrocyte micronucleus test (in vivo)."],
"citations": [
"Karlsson, H. L. 'The comet assay in nanotoxicology research' Anal. Bioanal. Chem. 398, 651-666 (2010).",
"Gonzalez, L., Lison, D. & Kirsch-Volders, M. 'Genotoxicity of engineered nanomaterials: a critical review' Nanotoxicology 2, 252-273 (2008)."],
"sig_lens": (
"Signature lens: genotoxicity is the Signature red line - the "
"endpoint where uncertainty itself becomes the verdict. The "
"Signature protocol attacks it with the full battery plus "
"mechanism proof (antioxidant rescue), because a material that "
"cannot clear the DNA question cannot ship, whatever its "
"performance.")},
{
"key": "immune",
"name": "The Immune Response: Inflammation Cascades and the Cytokine Signal",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Inflammation is the immune system's fire alarm, and nanoparticles "
"are good at pulling it. When macrophages engulf particles they "
"cannot digest - or are frustrated by fibers too long to engulf - "
"they release cytokines: TNF-alpha, IL-1beta, IL-6, IL-8, the "
"molecular shouting that recruits neutrophils and starts the "
"inflammatory cascade. Acute inflammation resolves when the "
"particles clear; persistent particles produce persistent "
"signaling, and persistent signaling remodels tissue into "
"fibrosis - the stiffened, scarred lung of chronic particle "
"disease. The NLRP3 inflammasome is a key molecular tripwire: "
"long fibers and certain crystals activate it, triggering IL-1beta "
"release, which is why the fiber paradigm and the inflammation "
"paradigm are the same story told twice. Dose-response for "
"cytokines follows the classic Hill curve - the demo fits IL-6 "
"release (Emax 1000 pg/mL, EC50 50 ug/mL) showing 500 pg/mL at the "
"EC50 and ~889 pg/mL at 200 ug/mL. But the immune system also "
"learns: some nanoparticles act as adjuvants, boosting allergic "
"responses to co-exposures, while others suppress immune function "
"at high doses. For the safety engineer, cytokines are the "
"earliest quantitative warning - measurable long before fibrosis, "
"and the endpoint that moves first when a safer-by-design "
"reformulation works."),
"how_it_works": (
"Cytokine testing uses macrophage or co-culture systems exposed "
"across a dose range, with supernatants analyzed by ELISA or "
"multiplex bead arrays at 6 and 24 hours - always with the "
"adsorption controls from the interference record, since particles "
"eat cytokines. The demo fits the Hill equation E = Emax*C^n / "
"(EC50^n + C^n) to IL-6 data, giving the EC50 that ranks materials "
"by inflammatory potency - the number that feeds safer-by-design "
"comparisons (does the coated variant shift EC50 right?). The "
"NLRP3 inflammasome is probed specifically: IL-1beta release that "
"vanishes with inflammasome inhibitors identifies the pathway, "
"flagging fiber-like behavior. In vivo, bronchoalveolar lavage "
"cell counts (neutrophils) and lavage cytokines at multiple time "
"points distinguish transient from persistent inflammation - the "
"distinction that separates a nuisance dust from a fibrogenic "
"one. Adjuvant activity is tested by co-exposure with a model "
"allergen: enhanced IgE or eosinophilia marks the material as an "
"allergy amplifier, a separate risk column on the safety sheet."),
"key_points": [
"Macrophages release TNF-alpha, IL-1beta, IL-6, IL-8 when they meet indigestible particles or frustrating fibers.",
"Persistent particles -> persistent signaling -> fibrosis: the chronic particle disease pathway.",
"NLRP3 inflammasome activation (IL-1beta) is the molecular tripwire behind fiber inflammation.",
"Hill fit demo: IL-6 EC50 50 ug/mL; 200 ug/mL gives ~889 pg/mL - EC50 ranks inflammatory potency.",
"Cytokines are the earliest quantitative warning and the first endpoint to improve with redesign.",
"Some particles act as adjuvants (allergy amplifiers) - test co-exposure, not just the particle alone."],
"requirements": [
"Macrophage/co-culture cytokine panel (TNF-alpha, IL-1beta, IL-6, IL-8) across a dose range.",
"Adsorption controls for every cytokine readout.",
"NLRP3/inflammasome pathway probing for fiber-like materials.",
"In vivo lavage time courses distinguishing transient from persistent inflammation."],
"standards": [
"ISO 10993-20:2006 - immunotoxicology evaluation principles (framework adapted for nanomaterials).",
"OECD TG 413 - 90-day inhalation (lavage cytology and histopathology endpoints)."],
"citations": [
"Palomaki, J. et al. 'Long, needle-like carbon nanotubes and asbestos activate the NLRP3 inflammasome through a similar mechanism' ACS Nano 5, 6861-6870 (2011).",
"Moller, P. et al. 'Role of oxidative damage in toxicity of particulates' Free Radic. Res. 44, 1-46 (2010)."],
"sig_lens": (
"Signature lens: inflammation is the Signature early-warning "
"system - the cytokine signal moves before any tissue is "
"remodeled. The Signature engineer instruments every material "
"variant with this alarm, ranks by EC50, and treats a rightward "
"EC50 shift as the first proof that a redesign worked.")},
{
"key": "dermal",
"name": "Dermal Exposure: What Crosses the Skin Barrier",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Skin is the body's best armor against nanoparticles, and the "
"evidence is consistent: intact human skin lets essentially no "
"nanoscale titanium dioxide or zinc oxide past the stratum "
"corneum, the 10-20 micrometre layer of dead cells that is the "
"real barrier. Tape-stripping studies of sunscreen on volunteers "
"find the particles in the outer strips and nothing in the living "
"layers; Franz diffusion-cell studies measure fluxes around "
"2.5e-9 mg/cm2/h - over an 8-hour shift on 100 cm2 of skin, about "
"2 nanograms total, a pharmacological nothing. The exceptions "
"define the risk assessment: damaged skin (eczema, abrasions, "
"sunburn) penetrates more; flexed skin at joints opens "
"micro-channels; hair follicles act as shunt routes where "
"particles accumulate in the follicular shaft (a reservoir, mostly, "
"rather than a highway to blood); and particles below ~5 nm or "
"with extreme surface activity deserve individual assessment. "
"Workplace dermal exposure - handling powders with bare hands, "
"spills on forearms - is therefore managed as a hygiene problem "
"(gloves, washing, no hand-to-mouth) rather than a systemic "
"toxicity problem, with the crucial caveat to reassess whenever "
"the skin is not intact. For products worn on skin, the dossier "
"question is binary and answerable: does it cross intact skin, "
"yes or no - and for the regulated sunscreen minerals, the "
"answer is no."),
"how_it_works": (
"Dermal penetration is measured in Franz cells: excised human "
"(or pig) skin clamped between a donor chamber (the sunscreen or "
"particle suspension) and a receptor fluid, with penetration "
"quantified over 24 hours by elemental analysis of the receptor "
"and by tape-stripping the skin layer by layer. The demo runs "
"the flux arithmetic: 2.5e-9 mg/cm2/h times 8 hours times 100 "
"cm2 equals 2.0e-6 mg - 2 nanograms - the number that lets "
"regulators sleep. Follicular penetration is assessed "
"separately by cyanoacrylate biopsy of follicle casts or by "
"confocal microscopy of labeled particles in follicles. Damaged-"
"skin protocols (tape-stripped or abraded skin in the Franz "
"cell) bracket the worst case. The assessment logic is a "
"decision tree: intact-skin penetration negligible -> manage as "
"hygiene; measurable penetration -> quantify systemic dose and "
"compare with the oral/inhalation toxicity data; damaged-skin "
"penetration significant -> label restrictions (not for broken "
"skin) or reformulation. Sunscreen-grade minerals passed this "
"tree years ago; each new particle walks it again."),
"key_points": [
"Intact skin blocks nano-TiO2/ZnO: particles stay in the stratum corneum; flux ~2.5e-9 mg/cm2/h.",
"Demo: 8 h on 100 cm2 at that flux = 2 nanograms total - a pharmacological nothing.",
"Exceptions: damaged/eczematous skin, flexed joints, follicular shunts - reassess when skin isn't intact.",
"Workplace dermal exposure is a hygiene problem (gloves, washing), not a systemic toxicity problem.",
"Decision tree: negligible intact-skin penetration -> hygiene; measurable -> systemic dose vs toxicity data.",
"Each new particle walks the tree again - past approvals don't transfer."],
"requirements": [
"Franz-cell penetration on intact human/pig skin with tape-strip profiling.",
"Damaged-skin (abraded/tape-stripped) worst-case protocol.",
"Follicular shunt assessment (biopsy or confocal on labeled particles).",
"Receptor-fluid elemental analysis with full mass balance."],
"standards": [
"OECD TG 428 - skin absorption: in vitro method.",
"SCCS Notes of Guidance - dermal absorption assessment for cosmetic ingredients (including nanomaterials)."],
"citations": [
"Cross, S. E. et al. 'Human skin penetration of sunscreen nanoparticles: in-vitro assessment of a novel micronized zinc oxide formulation' Skin Pharmacol. Physiol. 20, 148-154 (2007).",
"Larese, F. F. et al. 'Human skin penetration of silver nanoparticles through intact and damaged skin' Toxicology 255, 33-37 (2009)."],
"sig_lens": (
"Signature lens: skin is the Signature armor audit - the one "
"barrier that usually holds. The Signature practice verifies the "
"armor per particle (Franz cell, intact and damaged), manages "
"workplace contact as hygiene, and never extrapolates one "
"particle's 'no penetration' to the next.")},
{
"key": "ingestion",
"name": "Oral Exposure: The Gut Barrier and Food Contact",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"The gut meets nanoparticles in food additives (titanium dioxide "
"as E171, silica as E551, iron oxides as colorants), food-contact "
"materials, and hand-to-mouth transfer in workplaces - and the "
"gut is a reluctant absorber. Oral bioavailability of nanoscale "
"titanium dioxide is a fraction of a percent: of each ingested "
"milligram, roughly a microgram reaches systemic circulation, "
"the rest transits and exits. What little crosses tends toward "
"liver and spleen, the reticuloendothelial system's catch basins. "
"The toxicology questions are therefore about the gut itself "
"rather than distant organs: does chronic low-dose exposure "
"inflame the intestinal lining, alter the microbiome, or damage "
"the barrier? Studies report nano-TiO2 and nano-Ag shifting gut "
"microbial communities in rodents and, at high doses, intestinal "
"inflammation - findings that drove the European food-safety "
"reassessment of E171, where genotoxicity concerns that could not "
"be ruled out ended the additive's approval. Food-contact "
"materials add a migration question: do nanoparticles migrate "
"from packaging into food? Simulant testing (acidic, fatty, "
"aqueous food mimics) generally finds migration of intact "
"particles negligible, with ions the measurable migrants. The "
"engineering controls are formulation and containment: keep "
"food-grade particles agglomerated and bound in matrices, verify "
"migration in simulants, and treat the gut barrier as guilty "
"until proven innocent for each new additive."),
"how_it_works": (
"Oral bioavailability is measured by gavage studies with "
"elemental analysis of blood, liver, spleen, and excreta over "
"days: the demo uses the literature-typical 0.1% figure - 1 mg "
"ingested, 1 microgram systemic - to show why ingestion ranks "
"below inhalation for systemic risk while remaining relevant "
"for gut-local effects. Gut models run in parallel: Caco-2 cell "
"monolayers (sometimes with mucus-secreting co-culture) measure "
"translocation fractions across an intestinal barrier in vitro, "
"and 28- or 90-day feeding studies (OECD TG 407/408) examine "
"intestinal histopathology and microbiome shifts (16S sequencing) "
"at human-relevant doses. Migration from food-contact materials "
"is tested in food simulants under time-temperature conditions "
"matching real use, with single-particle ICP-MS distinguishing "
"migrated particles from dissolved ions. The risk arithmetic "
"multiplies: daily intake (dietary surveys) times bioavailable "
"fraction times organ distribution, compared against the "
"toxicity reference values - and for E171 that arithmetic, "
"combined with unresolvable genotoxicity questions, ended in "
"withdrawal."),
"key_points": [
"Oral bioavailability of nano-TiO2 is ~0.1%: 1 mg ingested -> ~1 ug systemic; the rest transits.",
"Systemic distribution favors liver and spleen; the gut itself is the main toxicology question.",
"Nano-TiO2/Ag shift rodent gut microbiomes and can inflame the intestine at high doses.",
"E171 withdrawn in the EU: genotoxicity concerns could not be ruled out.",
"Food-contact migration: intact particles negligible in simulants; ions are the measurable migrants.",
"Controls: bound/agglomerated food-grade particles, simulant migration testing, per-additive assessment."],
"requirements": [
"Oral bioavailability study (gavage + elemental analysis of blood, organs, excreta).",
"Intestinal barrier model (Caco-2/mucus co-culture) for translocation fractions.",
"Subchronic feeding study (TG 407/408) with gut histopathology and microbiome analysis.",
"Food-simulant migration testing with single-particle ICP-MS (particles vs ions)."],
"standards": [
"OECD TG 407 - repeated dose 28-day oral toxicity study in rodents.",
"OECD TG 408 - repeated dose 90-day oral toxicity study in rodents.",
"EU Regulation 10/2011 - plastic materials and articles intended for food contact (migration testing)."],
"citations": [
"EFSA Panel on Food Additives and Flavourings 'Safety assessment of titanium dioxide (E171) as a food additive' EFSA J. 19, e06585 (2021).",
"Bettini, S. et al. 'Food-grade TiO2 impairs intestinal and systemic immune homeostasis, initiates preneoplastic lesions and promotes aberrant crypt development in the rat colon' Sci. Rep. 7, 40373 (2017)."],
"sig_lens": (
"Signature lens: the gut is the Signature reluctant gate - "
"almost everything passes through, almost nothing gets in. The "
"Signature practice respects the gate's terms: prove low uptake "
"per additive, watch the gut lining and its microbes (the locals "
"the gate protects), and keep food-grade particles bound in "
"their matrix so the question never arises.")},
{
"key": "biomarkers",
"name": "Biomarkers and Omics: Reading the Molecular Response",
"group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"When a nanoparticle perturbs a cell, the cell writes it down - in "
"messenger RNA, proteins, and metabolites - and omics technologies "
"read the whole diary at once. Transcriptomics (RNA sequencing) "
"reveals which of the cell's ~20,000 genes change activity: "
"oxidative-stress genes (HMOX1, NQO1) for tier-1 ROS responses, "
"cytokine genes for inflammation, DNA-repair genes for genotoxic "
"stress. Proteomics and metabolomics add the protein and small-"
"molecule layers. The power is pattern: a particle's gene-expression "
"signature can be matched against libraries of known toxicants, "
"identifying the mechanism without guessing - nano-ZnO's signature "
"screams metal-ion stress, long CNTs scream fiber inflammation. "
"Fold-changes are the currency: the demo computes a log2 fold "
"change of 4.0 (16-fold upregulation) for a stress gene going from "
"50 to 800 read counts - the magnitude that marks a real response "
"rather than noise. The challenges are interpretation, not "
"measurement: thousands of changing genes need pathway analysis "
"(which biological programs moved?), dose-response modeling (at "
"what dose does the pathway activate?), and anchoring to real "
"outcomes (does the gene signature predict the lung fibrosis?). "
"Used with that discipline, omics turns each material into a "
"mechanistic fingerprint - and fingerprints can be compared, "
"grouped, and read-across, so that testing one well-chosen "
"material predicts its cousins."),
"how_it_works": (
"A biomarker study exposes cells or animals across doses and time, "
"extracts RNA, and sequences it: differential-expression analysis "
"(DESeq2-style statistics) lists genes changed versus control with "
"fold-change and significance, then pathway enrichment asks which "
"biological programs (Nrf2 antioxidant response, NF-kB "
"inflammation, p53 DNA damage) moved together. The demo shows the "
"core computation - log2 fold change from normalized counts - and "
"the interpretation rule: |log2FC| > 1 with statistical "
"significance marks a candidate, but candidates become biomarkers "
"only when they track dose and predict an apical outcome. Dose-"
"response modeling on pathway scores yields a point of departure "
"(the dose where the pathway activates), which feeds directly "
"into risk assessment - a molecular NOAEC. Read-across is the "
"payoff: materials whose omics fingerprints cluster together "
"share mechanisms, so the well-tested member's hazard data "
"covers the group - the scientific basis for grouping nanoforms "
"under REACH. The quality controls are strict: batch-effect "
"correction, interference checks (particles in RNA extraction), "
"and validation of key genes by qPCR, because a sequencer will "
"happily quantify noise."),
"key_points": [
"Omics reads the cell's full response diary: transcriptomics, proteomics, metabolomics.",
"Fold-change is the currency (demo: 50 -> 800 counts = log2FC 4.0 = 16x upregulation).",
"Pathway analysis identifies the mechanism: Nrf2 (ROS), NF-kB (inflammation), p53 (DNA damage).",
"Pathway dose-response gives a molecular point of departure for risk assessment.",
"Read-across: materials with matching fingerprints share mechanisms - test one, cover the group.",
"Controls: batch effects, particle interference in extraction, qPCR validation of key genes."],
"requirements": [
"Dose- and time-course exposure design with matched controls.",
"RNA sequencing with differential-expression and pathway-enrichment analysis.",
"Interference controls for particle carryover into extraction/sequencing.",
"Anchoring of molecular changes to apical outcomes (inflammation, fibrosis)."],
"standards": [
"OECD Guidance Document on omics technologies in regulatory toxicology (in development; TG 439/431 contexts).",
"MIAME/MINSEQE reporting standards for transcriptomics experiments."],
"citations": [
"Stone, V. et al. 'Nanomaterials versus ambient ultrafine particles: an opportunity to exchange toxicology knowledge' Environ. Health Perspect. 115, 1438-1442 (2007).",
"Schmid, O. & Stoeger, T. 'Surface area is the biologically most effective dose metric for acute nanoparticle toxicity in the lung' J. Aerosol Sci. 99, 133-143 (2016)."],
"sig_lens": (
"Signature lens: omics is the Signature fingerprint bureau - "
"every material leaves a molecular print at the scene. The "
"Signature investigator files prints by mechanism, matches "
"newcomers against the archive, and lets one well-tested "
"material vouch for its fingerprint family.")},
{
"key": "niosh_cib65",
"name": "NIOSH CIB 65: The Carbon Nanotube Exposure Limit",
"group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"In 2013, the US National Institute for Occupational Safety and "
"Health did something it had never done: set an exposure limit for "
"a nanomaterial as such. Current Intelligence Bulletin 65 "
"recommends 1 microgram of elemental carbon per cubic metre of air, "
"as an 8-hour time-weighted average, for carbon nanotubes and "
"nanofibers - about a thousand times lower than the 1 mg/m3 limit "
"for ordinary carbon black dust. The number came from the fiber "
"paradigm plus quantitative risk assessment: animal studies "
"showing lung inflammation and fibrosis at low deposited doses, "
"modeled to human working lifetimes, with the limit set where the "
"excess risk becomes small. Elemental carbon is the measurable "
"proxy - weighing nanotubes at microgram levels is impractical, "
"but thermal-optical analysis (NIOSH Method 5040) quantifies "
"elemental carbon on a filter reliably. The bulletin also set the "
"template for nano regulation: characterize the material, control "
"exposure with the hierarchy (elimination, substitution, "
"engineering controls, work practice, PPE - in that order), and "
"run medical surveillance. Compliance arithmetic is stark: the "
"demo shows a workplace measuring 8 ug/m3 needs 87.5% control "
"efficiency just to reach the limit - open powder handling "
"cannot comply, only enclosures and local exhaust can. CIB 65 "
"remains the reference case for how a nano-specific limit is "
"built: hazard mechanism, dose-response, measurable proxy, "
"achievable controls."),
"how_it_works": (
"The limit rests on benchmark-dose modeling of rat inhalation "
"and instillation data: the dose causing a defined excess of "
"lung inflammation or fibrosis, extrapolated to humans with "
"deposition and dosimetric adjustments, then divided by "
"uncertainty factors. The demo does the compliance side - "
"measured concentration over the limit gives the exceedance "
"factor (8 ug/m3 / 1 ug/m3 = 8x), and the required control "
"efficiency is 1 minus the reciprocal (87.5%). Exposure "
"assessment uses NIOSH 5040: full-shift personal breathing-zone "
"samples on quartz filters, thermal-optical analysis separating "
"elemental carbon (the tubes) from organic carbon (background "
"soot) - with careful background subtraction in facilities "
"that also produce combustion particles. The hierarchy of "
"controls is applied in order: can the tubes be bought as "
"dispersions instead of powder (substitution)? Can synthesis be "
"enclosed (engineering)? Only after those come respirators - "
"and the bulletin is explicit that respirators are the last "
"resort, not the plan. Medical surveillance (respiratory "
"questionnaires, spirometry) watches the workforce for the "
"effects the limit is meant to prevent."),
"key_points": [
"CIB 65 (2013): 1 ug/m3 elemental carbon, 8-h TWA - the first US nano-specific exposure limit.",
"A thousand times lower than ordinary carbon black dust limits - the fiber paradigm priced in.",
"Elemental carbon by NIOSH 5040 is the measurable proxy (weighing tubes at ug levels is impractical).",
"Built from benchmark-dose modeling of animal lung data, human-scaled, with uncertainty factors.",
"Demo: 8 ug/m3 measured needs 87.5% control efficiency - only enclosures and exhaust comply.",
"Template for nano regulation: mechanism, dose-response, measurable proxy, hierarchy of controls."],
"requirements": [
"Full-shift personal breathing-zone sampling on quartz filters.",
"NIOSH Method 5040 thermal-optical elemental carbon analysis with background subtraction.",
"Material characterization confirming CNT/CNF identity (the limit's scope).",
"Hierarchy-of-controls documentation and medical surveillance program."],
"standards": [
"NIOSH CIB 65 (2013) - occupational exposure to carbon nanotubes and nanofibers.",
"NIOSH Method 5040 - diesel particulate matter as elemental carbon (thermal-optical analysis)."],
"citations": [
"NIOSH 'Current Intelligence Bulletin 65: Occupational Exposure to Carbon Nanotubes and Nanofibers' DHHS (NIOSH) Publication No. 2013-145 (2013).",
"Pauluhn, J. 'Subchronic 13-week inhalation exposure of rats to multiwalled carbon nanotubes: toxic effects on the lung and relevance for human risk assessment' Toxicology 280, 152-157 (2011)."],
"sig_lens": (
"Signature lens: CIB 65 is the Signature precedent - proof that "
"a nano-specific limit can be built from mechanism plus "
"measurement. The Signature compliance engineer works the "
"arithmetic backwards from 1 ug/m3: every handling step gets an "
"emission budget, and the process is redesigned until the "
"budgets sum below the limit.")},
{
"key": "oecd_guidelines",
"name": "OECD Test Guidelines: The Harmonized Testing Suite",
"group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
"description": (
"When regulators in thirty countries need the same test to mean "
"the same thing, they use OECD Test Guidelines - and "
"nanotoxicology runs on a adapted subset of them. The inhalation "
"pair is the core: TG 412 (28-day repeated-dose inhalation) for "
"screening and TG 413 (90-day subchronic inhalation) for the "
"definitive study, with the nano-specific adaptations published "
"in Guidance Document 39 - stable aerosol generation, particle "
"size monitoring throughout exposure, lung burden measurement, "
"and bronchoalveolar lavage. The oral pair (TG 407 28-day, TG 408 "
"90-day) covers ingestion; the genotoxicity battery (TG 471 "
"Ames - with the particle false-negative caveat, TG 487 in vitro "
"micronucleus, TG 474 in vivo micronucleus) covers DNA damage. "
"Mutual Acceptance of Data means a TG 413 study done in one "
"member country is accepted in all - the economic engine that "
"justifies the cost of a proper study. The demo counts the "
"animals: a TG 413 needs 10 rats per sex per group times 2 "
"sexes times 4 groups (control + 3 doses) = 80 rats, versus 40 "
"for a TG 412 - the price tag that makes tier-1 in vitro "
"triage and grouping/read-across (test one representative "
"nanoform, cover the group) essential strategy, not just "
"ethics."),
"how_it_works": (
"A guideline study is a contract: the protocol (OECD TG text "
"plus the nano adaptations of GD 39) specifies species, group "
"sizes, dose spacing, exposure regimen, and every endpoint, so "
"the result is comparable across labs and decades. Dose spacing "
"typically uses a factor of 2-4 between concentrations, with "
"the top dose set below lung overload (the validity criterion "
"that invalidates studies drowning the clearance system). "
"Aerosol characterization runs continuously: mass concentration "
"(gravimetric), size distribution (SMPS/APS), and morphology "
"(TEM of collected particles) - because the guideline demands "
"proof that the animals breathed what the protocol says. "
"Endpoints cascade from the general (body weight, organ "
"weights) to the nano-specific (lavage cytology, lung burden "
"time course, translocation organs). The study director's "
"hardest job is the dose-range finder: a 5-day pilot that "
"locates the responsive-but-not-overloaded window the main "
"study will live in. Reports follow the guideline's data "
"tables exactly - regulators review hundreds, and "
"non-standard formats slow everything."),
"key_points": [
"Core inhalation pair: TG 412 (28-day) screening, TG 413 (90-day) definitive, with nano adaptations (GD 39).",
"Mutual Acceptance of Data: one country's TG study is accepted in all OECD countries.",
"Top dose must stay below lung overload - overloaded studies are invalid for limit-setting.",
"Continuous aerosol proof required: mass, size distribution, and morphology throughout exposure.",
"Demo: TG 413 = 80 rats, TG 412 = 40 - the cost that makes in vitro triage and read-across essential.",
"A guideline study is a contract: fixed protocol, fixed tables, comparable across labs and decades."],
"requirements": [
"OECD TG text plus nano adaptations (GD 39) as the binding protocol.",
"Dose-range-finding pilot to locate the responsive non-overloaded window.",
"Continuous aerosol characterization (mass, SMPS/APS sizing, TEM morphology).",
"Guideline-exact reporting tables for regulatory review."],
"standards": [
"OECD TG 412 - subacute inhalation toxicity: 28-day study.",
"OECD TG 413 - subchronic inhalation toxicity: 90-day study.",
"OECD GD 39 - guidance on inhalation toxicity studies with nanomaterials."],
"citations": [
"OECD 'Test No. 413: Subchronic Inhalation Toxicity: 90-day Study' OECD Guidelines for the Testing of Chemicals (2018).",
"OECD 'Guidance Document 39 on Inhalation Toxicity Studies' Series on Testing and Assessment No. 39 (2018)."],
"sig_lens": (
"Signature lens: OECD guidelines are the Signature rulebook - "
"the agreed language in which safety is argued across borders. "
"The Signature strategist plays the rulebook to win: triage in "
"vitro, group nanoforms for read-across, run one definitive TG "
"413 instead of three mediocre studies, and file it where every "
"regulator reads the same tables.")},
{
"key": "reach",
"name": "REACH Nanoforms: Europe's Registration Rules",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Since January 2020, Europe's REACH chemical regulation treats "
"nanoforms as substances in their own right: a company "
"manufacturing or importing a nanomaterial must register each "
"nanoform - defined by size, shape, and surface chemistry - with "
"its own characterization and hazard dataset. The 2018 nanoform "
"amendments closed the old loophole where a bulk registration "
"quietly covered the nano version. The data demands scale with "
"tonnage: 1-10 tonnes per year needs Annex VII and VIII "
"(physicochemical, acute toxicity, irritation, sensitization, "
"mutagenicity screening); 10-100 tonnes adds Annex IX "
"(subchronic, reproductive screening); above 100 tonnes adds "
"Annex X (chronic, full reproductive). The nano-specific "
"requirements bite at every band: dissolution rate in relevant "
"media, dustiness, particle size distribution, surface "
"functionalization - and the grouping/read-across rules that let "
"one tested nanoform cover similar ones, provided the "
"justification holds. The demo encodes the tonnage logic: 5 "
"tonnes per year lands in the 1-10 band (Annexes VII+VIII). For "
"industry the strategic question is portfolio design - how many "
"distinct nanoforms to commercialize, since each one carries a "
"registration dossier - and for safety science, REACH created "
"the world's largest structured demand for nano hazard data."),
"how_it_works": (
"Registration starts with nanoform identification: the set of "
"nanoforms is defined by ranges of size, shape (including "
"high-aspect-ratio), crystallinity, and surface treatment, with "
"each distinct combination a separate registration unit. "
"Characterization follows the REACH nano guidance (RIP-oN "
"reports): TEM size distributions, BET surface area, dustiness "
"(rotating drum), dissolution in water and biological simulants, "
"surface chemistry by XPS. Hazard testing fills the annex "
"requirements with the OECD battery, adapted per GD 39 for "
"inhalation. The grouping justification - the document that lets "
"one dossier cover several nanoforms - must argue similarity in "
"the properties driving hazard (dissolution, shape, surface "
"reactivity) with data, not assertions; ECHA rejects hand-"
"waving. The demo implements the tonnage-band decision table "
"that opens every registration strategy meeting: below 1 tonne "
"reduced requirements, 1-10 tonnes Annex VII+VIII, 10-100 plus "
"IX, above 100 plus X - and the cost curve that follows it, "
"which is why companies consolidate nanoform portfolios before "
"registering."),
"key_points": [
"Since 2020, each nanoform (size, shape, surface chemistry) needs its own REACH registration.",
"Data scales with tonnage: 1-10 t (VII+VIII), 10-100 t (+IX), >100 t (+X). Demo: 5 t -> VII+VIII.",
"Nano-specific demands: dissolution rate, dustiness, size distribution, surface functionalization.",
"Grouping/read-across lets one tested nanoform cover similar ones - with a data-backed justification.",
"Portfolio strategy: each distinct nanoform carries a dossier cost - consolidate before registering.",
"Created the world's largest structured demand for nano hazard data."],
"requirements": [
"Nanoform set definition (size/shape/crystallinity/surface-treatment ranges).",
"Full nano characterization per RIP-oN guidance (TEM, BET, dustiness, dissolution, XPS).",
"Tonnage-band hazard dataset (OECD battery with nano adaptations).",
"Data-backed grouping justification for read-across between nanoforms."],
"standards": [
"Regulation (EC) 1907/2006 (REACH) as amended by Regulation (EU) 2018/1881 (nanoforms).",
"ECHA Guidance R.7a, R.7b, R.7c - endpoint-specific guidance including nanoform appendices."],
"citations": [
"European Commission 'Commission Regulation (EU) 2018/1881 amending Regulation (EC) No 1907/2006 as regards Annexes I, III, VI, VII, VIII, IX, X, XI, and XII to address nanoforms of substances' Official Journal of the European Union (2018).",
"ECHA 'Guidance on information requirements and chemical safety assessment - Appendix R.6-1 for nanoforms' (2019)."],
"sig_lens": (
"Signature lens: REACH nanoforms are the Signature portfolio "
"problem - every variant is a dossier, so variety has a price. "
"The Signature strategist designs the product line around the "
"regulation: fewer, well-separated nanoforms, each with a "
"grouping story, registered once and sold everywhere.")},
{
"key": "epa_tsca",
"name": "EPA TSCA: America's Nanoscale Reporting Rules",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"America regulates nanomaterials through the Toxic Substances "
"Control Act's existing machinery, extended by nanoscale-specific "
"rules. The landmark is the 2017 TSCA section 8(a) reporting rule: "
"anyone who manufactured or processed a reportable nanoscale "
"material (1-100 nm, solid at room temperature, with nano-specific "
"properties) since 2014 had to report it to EPA - identity, "
"production volume, uses, exposure and release information - in a "
"one-time census of the US nano industry. Alongside it run the "
"Significant New Use Rules (SNURs): for specific nanomaterials "
"(certain carbon nanotubes, for example), EPA requires 90-day "
"pre-notification before any new use, letting the agency demand "
"testing or impose controls. New chemicals that are nanoscale go "
"through premanufacture notice (PMN) review where EPA can - and "
"has - restricted production pending data. Compared with REACH, "
"TSCA is more targeted and less tonnage-driven: fewer universal "
"dossiers, more substance-specific orders. The demo encodes the "
"2017 rule's decision logic: manufactured a reportable nanoscale "
"material in the window - report; below the exclusions - document "
"why not. For companies the discipline is inventory: know every "
"nanoscale substance in your products and processes, because the "
"regulator's first question is always 'what do you have?'"),
"how_it_works": (
"TSCA compliance is an inventory exercise first and a testing "
"exercise second. The 8(a) rule defined reportability by "
"criteria: solid nanoscale material, 1-100 nm primary size, "
"exhibiting size-dependent properties, manufactured or processed "
"after the cutoff - with exclusions (naturally occurring, certain "
"biological materials). The demo implements that decision tree "
"on a case: 100 kg of engineered nanosilver produced in 2016 - "
"reportable, file the notice. SNURs work differently: they name "
"a substance and the significant new uses, and anyone planning "
"such a use files a Significant New Use Notice 90 days ahead; "
"EPA can then issue orders requiring testing (often the OECD "
"inhalation battery), workplace controls, or use restrictions. "
"PMN review for new nanoscale chemicals routinely produces "
"consent orders with exposure limits and PPE requirements baked "
"in. The record-keeping duty is continuous: production volumes, "
"exposure monitoring, and customer notifications must be "
"retrievable, because EPA enforcement starts with the files. "
"State rules (California's Safer Consumer Products program, for "
"example) add a second layer for products sold nationally."),
"key_points": [
"2017 TSCA 8(a) rule: one-time census of nanoscale materials manufactured/processed since 2014.",
"SNURs: 90-day pre-notification before significant new uses of listed nanomaterials (e.g., certain CNTs).",
"PMN review for new nanoscale chemicals can impose testing and controls via consent orders.",
"More targeted than REACH: substance-specific orders rather than universal tonnage dossiers.",
"Demo: 100 kg engineered nanosilver made in 2016 -> reportable under the 8(a) rule.",
"Core discipline is inventory: know every nanoscale substance in products and processes."],
"requirements": [
"Complete inventory of nanoscale substances manufactured, processed, or imported.",
"8(a) reportability determination per material (size, properties, dates, exclusions).",
"SNUR watch: significant-new-use screening before product or process changes.",
"Retrievable records: volumes, exposure data, customer communications."],
"standards": [
"TSCA section 8(a) - Chemical Data Reporting and nanoscale materials reporting rule (2017).",
"TSCA section 5 - premanufacture notice (PMN) and Significant New Use Rules (SNURs)."],
"citations": [
"U.S. EPA 'Chemical substances when manufactured or processed as nanoscale materials: TSCA reporting and recordkeeping requirements' Federal Register 82, 3641-3658 (2017).",
"U.S. EPA 'Control of nanoscale materials under the Toxic Substances Control Act' - EPA nanotechnology white paper and program documents (2007-2017)."],
"sig_lens": (
"Signature lens: TSCA is the Signature inventory problem - "
"the regulator's first question is 'what do you have?' and "
"the wrong answer is expensive. The Signature practice keeps a "
"living nanoscale inventory with reportability pre-computed, so "
"every new product or process change clears the SNUR screen "
"before it clears engineering.")},
{
"key": "iso12901",
"name": "ISO/TS 12901: The Control Banding Standard",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Most workplaces handling nanomaterials will never commission a "
"90-day inhalation study - so how do they choose controls? "
"ISO/TS 12901-2 (2014) gives the answer: control banding, the "
"method of assigning a control level from limited information. "
"The scheme crosses two axes: the hazard band of the material "
"(five bands, from low-solubility low-toxicity particles up to "
"fibrous, biopersistent high-toxicity materials - carbon "
"nanotubes land in the top band) and the exposure band (from "
"dustiness and the amount handled, in four bands). The matrix "
"cell where they meet names the control: general ventilation, "
"fume hoods or local exhaust, containment, or full containment "
"with specialist review. The demo runs the logic: a fibrous "
"biopersistent material (hazard band 5) handled as a dusty "
"powder in kilogram quantities (exposure band 4) lands in the "
"highest control band - full containment, no open handling. "
"Control banding is explicitly precautionary - it over-controls "
"rather than under-controls when data are thin - and it is a "
"starting point, not a substitute for measurement: the standard "
"demands verification by exposure monitoring wherever feasible. "
"For the thousands of small labs and startups in the nano "
"economy, this standard is the practical bridge between "
"toxicology's knowledge and Tuesday morning's powder transfer."),
"how_it_works": (
"Applying the standard is a four-step desk exercise followed by "
"field verification. Step one: gather what is known - SDS, "
"published toxicology, particle size, solubility, fiber "
"status - and assign the hazard band (1-5) per the standard's "
"decision logic; unknown or fibrous-biopersistent materials "
"default upward. Step two: score dustiness (manufacturer data "
"or the rotating-drum test) and task quantity to get the "
"exposure band (1-4). Step three: read the matrix - the demo "
"encodes a simplified version mapping (hazard 5, exposure 4) "
"to control level 5, full containment. Step four: implement "
"the control and verify with exposure monitoring (filter "
"samples, direct-reading particle counters with background "
"subtraction), because banding predicts the control class, not "
"the concentration. The standard also covers what banding "
"cannot do: it does not set exposure limits, does not replace "
"risk assessment for new materials with novel hazards, and "
"must be revisited when new toxicology arrives. Training is "
"part of the control - the best enclosure fails with the sash "
"up and the worker leaning in."),
"key_points": [
"Control banding assigns controls from limited data: hazard band (1-5) x exposure band (1-4) -> control level.",
"CNTs land in hazard band 5 (fibrous, biopersistent); dusty kg-scale powder handling -> exposure band 4.",
"Demo: (5,4) -> control level 5, full containment - no open handling.",
"Explicitly precautionary: over-controls when data are thin; a starting point, not a substitute for measurement.",
"Verification required: exposure monitoring must confirm the banded control works.",
"The practical bridge for small labs and startups: toxicology's knowledge translated to Tuesday's powder transfer."],
"requirements": [
"Material hazard data (or precautionary default): solubility, fiber status, known toxicity.",
"Dustiness data and task quantity for the exposure band.",
"Matrix readout implemented as specified engineering control.",
"Post-implementation exposure monitoring and worker training."],
"standards": [
"ISO/TS 12901-2:2014 - occupational risk management applied to engineered nanomaterials: control banding approach.",
"ISO/TS 12901-1:2012 - occupational risk management: principles and approaches."],
"citations": [
"ISO 'ISO/TS 12901-2:2014 Nanotechnologies - Occupational risk management applied to engineered nanomaterials - Part 2: Use of the control banding approach' (2014).",
"Paik, S. Y., Zalk, D. M. & Swuste, P. 'Application of a pilot control banding tool for risk level assessment and control of nanoparticle exposures' Ann. Occup. Hyg. 52, 419-428 (2008)."],
"sig_lens": (
"Signature lens: control banding is the Signature triage for "
"the rest of us - no 90-day study, no problem. The Signature "
"shop runs the matrix before the first bag is opened, installs "
"the banded control, then measures to prove it - precaution "
"first, verification always.")},
{
"key": "safer_by_design",
"name": "Safer by Design: Engineering the Hazard Out",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Safer by design is nanotoxicology's answer to its own findings: "
"if hazard lives in size, shape, surface chemistry, and "
"dissolution, then change those and the hazard changes. The "
"canon examples are now textbook. Iron-doped zinc oxide: a few "
"percent iron in the crystal lattice slows dissolution and "
"quenches ROS generation, and cell death falls in step - the "
"same UV-blocking particle, a fraction of the toxicity (George "
"et al. 2010). Silica-coated titanium dioxide: a dense shell "
"blocks photocatalytic ROS while the core still absorbs UV - "
"the sunscreen that protects skin without attacking it. Short, "
"functionalized carbon nanotubes: cut below the fiber length "
"threshold and decorated with groups macrophages recognize, "
"clearing instead of frustrating. The methodology is a loop: "
"identify the hazard driver (band gap? dissolution? fiber "
"length?), modify the material to blunt it, re-test in the "
"same assays, and confirm the function survived - because a "
"safe particle that doesn't work is just expensive sand. The "
"demo quantifies the ZnO case: undoped dissolution at 0.02/h "
"leaves 38% dissolved in 24 hours; Fe-doped at 0.004/h leaves "
"9% - a four-fold hazard cut from a lattice tweak. Regulators "
"are beginning to reward the loop: reduced testing for "
"well-justified safer variants, and grouping rules that let "
"the safer member's data cover the family."),
"how_it_works": (
"A safer-by-design program runs in four stages. Stage one, "
"hazard mapping: test the base material across the tier-1 "
"battery to find which mechanism dominates (ROS? ions? "
"fibers?). Stage two, design hypotheses: if ions, dope the "
"lattice or seal the surface; if ROS, shift the band gap or "
"coat catalytic sites; if fibers, shorten or functionalize; "
"if uptake, change charge or add PEG. Stage three, parallel "
"synthesis: make the base plus 3-5 variants in one campaign, "
"characterizing each (did the doping actually incorporate? "
"is the shell continuous?). Stage four, head-to-head testing: "
"the same assays, the same doses, ranking hazard against "
"function - UV absorption for sunscreens, conductivity for "
"composites, antimicrobial activity for silver. The demo's "
"dissolution arithmetic is the stage-four scoreboard for the "
"ZnO case. The documentation matters as much as the result: "
"the safer-by-design dossier records what was changed, why, "
"and the before/after data - the evidence package that earns "
"regulatory credit and defends the design if questions come "
"later."),
"key_points": [
"Hazard lives in tunable properties: dope the lattice, coat the surface, shorten the fiber - hazard follows.",
"Fe-doped ZnO: dissolution 0.02/h -> 0.004/h; 24-h dissolved fraction 38% -> 9% (demo).",
"Silica-coated TiO2: shell blocks ROS, core keeps UV absorption - function preserved.",
"Short functionalized CNTs clear instead of frustrating macrophages.",
"Loop: map the mechanism -> modify -> re-test head-to-head -> confirm function survived.",
"Document the before/after - the dossier earns regulatory credit for safer variants."],
"requirements": [
"Tier-1 hazard mapping of the base material to identify the dominant mechanism.",
"Parallel synthesis of base + 3-5 variants with full characterization of the modification.",
"Head-to-head testing in identical assays plus function verification.",
"Safer-by-design dossier: what changed, why, and before/after data."],
"standards": [
"ISO/TS 12901 series - occupational risk management (design-stage considerations).",
"OECD guidance on Safe and Sustainable by Design (SSbD) for nanomaterials (2022+)."],
"citations": [
"George, S. et al. 'Use of a rapid cytotoxicity screening approach to engineer a safer zinc oxide nanoparticle through iron doping' ACS Nano 4, 15-29 (2010).",
"Auffan, M. et al. 'Towards a definition of inorganic nanoparticles from an environmental, health and safety perspective' Nat. Nanotechnol. 4, 634-641 (2009)."],
"sig_lens": (
"Signature lens: safer by design is the Signature home game - "
"hazard as an engineering variable, not a verdict. The "
"Signature material program never asks 'is it safe' once; it "
"asks 'which atom do we change' repeatedly, until the hazard "
"curve bends and the function curve doesn't.")},
{
"key": "surface_chemistry",
"name": "Surface Chemistry as the Safety Dial: Coatings, Charge, and PEGylation",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"If the particle's surface is where hazard happens, then surface "
"chemistry is the safety dial - and it has three main settings. "
"Setting one: barrier coatings. A dense silica or alumina shell a "
"few nanometres thick physically separates the reactive core from "
"biology: coated rutile TiO2 keeps its UV absorption while its "
"photocatalytic ROS drops to near zero, and the demo shows a 5 nm "
"silica shell on ZnO cutting 24-hour ion release from 38% to under "
"5%. Setting two: charge. Cell membranes are negatively charged, "
"so cationic particles enter cells far more readily than anionic "
"ones - flipping a particle's zeta potential from +30 mV to -30 mV "
"can cut cellular uptake several-fold, at the cost of colloidal "
"stability that must be re-engineered. Setting three: stealth "
"polymers. Grafted polyethylene glycol (PEG) brushes suppress "
"protein adsorption, calm the corona (the previous record's "
"subject), and extend circulation - the difference between a "
"particle macrophages eat on sight and one they ignore. The "
"dial has a catch: coatings are consumed. Ligands desorb, shells "
"dissolve, PEG oxidizes - so every coating choice carries a "
"lifetime specification, tested under the real conditions of use "
"(lysosomal acid, UV, mechanical shear). A safety dial that "
"drifts back to hazard is not a control; it is a timer."),
"how_it_works": (
"Coating performance is measured in three assays. Barrier "
"integrity: ion release (ICP-MS) and ROS generation of coated "
"versus uncoated particles in relevant fluids - the demo runs "
"the ZnO numbers, 38% versus 4.7% dissolved in 24 hours, the "
"quantitative payoff of 5 nm of silica. Charge: zeta potential "
"versus pH curves plus cellular uptake (flow cytometry of "
"labeled particles) across the charge series, confirming the "
"uptake ranking cationic > neutral > anionic. Stealth: protein "
"adsorption (BCA assay on the corona) and macrophage uptake "
"with PEG grafting density varied - the brush regime (dense, "
"extended chains) suppresses adsorption far better than the "
"mushroom regime (sparse coils), so grafting density is the "
"reported specification, not just 'PEGylated'. Durability "
"closes the loop: coated particles aged in lysosomal simulant "
"(pH 4.5), under UV, and under shear, then re-tested - the "
"coating lifetime must exceed the product lifetime with "
"margin. Formulation records the full recipe: core, shell "
"material and thickness, ligand identity and density, zeta "
"potential - because the coating is the safety device, its "
"specification is a safety specification."),
"key_points": [
"Three dial settings: barrier coatings (silica/alumina shells), surface charge, stealth polymers (PEG).",
"Demo: 5 nm silica shell on ZnO cuts 24-h dissolution 38% -> 4.7% while the core keeps working.",
"Cationic particles enter cells far more readily; flipping zeta potential +30 to -30 mV cuts uptake.",
"PEG brush regime (dense) suppresses protein adsorption; grafting density is the specification.",
"Coatings are consumed: ligands desorb, shells dissolve - every coating needs a tested lifetime.",
"A safety dial that drifts back to hazard is a timer, not a control."],
"requirements": [
"Coated vs uncoated head-to-head: ion release, ROS, and uptake in relevant fluids.",
"Zeta potential vs pH curves and charge-series uptake data.",
"PEG grafting density measurement (not just 'PEGylated').",
"Durability aging (lysosomal pH 4.5, UV, shear) with re-testing; coating lifetime > product lifetime."],
"standards": [
"ISO/TS 16578:2013 - molecular spectroscopy methods for nanoparticle surface characterization.",
"ISO 10808:2010 - nanoparticle characterization in exposure chambers (surface state)."],
"citations": [
"Suk, J. S., Xu, Q., Kim, N., Hanes, J. & Ensign, L. M. 'PEGylation as a strategy for improving nanoparticle-based drug and gene delivery' Adv. Drug Deliv. Rev. 99, 28-51 (2016).",
"Walkey, C. D., Olsen, J. B., Guo, H., Emili, A. & Chan, W. C. W. 'Nanoparticle size and surface chemistry determine serum protein adsorption and macrophage uptake' J. Am. Chem. Soc. 134, 2139-2147 (2012)."],
"sig_lens": (
"Signature lens: surface chemistry is the Signature control "
"panel - three dials, each with a calibrated effect and a "
"known drift rate. The Signature formulator sets the dials, "
"prints the settings on the datasheet, and warranties the "
"coating for longer than the product will live.")},
{
"key": "exposure_modeling",
"name": "Exposure Modeling: From Emission to Breathing Zone",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Exposure limits protect workers only if someone computes the "
"exposure - and measurement campaigns cannot cover every task, "
"so nanotoxicology models it. The workhorse is the two-box "
"(near-field/far-field) model: the worker's breathing zone is a "
"small well-mixed box around the source, nested in the larger "
"room box, each with airflows between them. Given an emission "
"rate (milligrams per minute from pouring, weighing, or "
"synthesis), the model predicts the breathing-zone "
"concentration: the demo's case - 1 mg/min emitted into a near-"
"field ventilated at 10 m3/min - gives 0.1 mg/m3 (100 ug/m3) "
"in the breathing zone, instantly comparable with the 1 ug/m3 "
"CNT limit (a hundred times over - enclose the process). "
"Emission rates come from dustiness tests (rotating drum, small "
"drum) or task-based measurements, scaled by handling energy "
"and quantity. Nanoparticles add model twists: agglomeration "
"shrinks number counts while barely changing mass, deposition "
"to room surfaces removes the smallest particles fastest, and "
"background particles (traffic soot, cooking) confound "
"number-based monitors - so models track mass and surface area "
"alongside number. The model's job is prospective: before the "
"process runs, predict the exposure, choose the control, and "
"size the ventilation - then verify with a measurement day. "
"A model that is never verified is a story; a verified model "
"is an engineering tool."),
"how_it_works": (
"The two-box steady state is simple arithmetic: near-field "
"concentration equals emission rate divided by the near-field "
"ventilation rate (C = G/beta), and far-field equals emission "
"over room ventilation - the demo computes both, 100 ug/m3 "
"near-field and 10 ug/m3 far-field for the 1 mg/min case. "
"Time-dependent versions add the task timeline (pour for 2 "
"minutes, weigh for 5) and clearance between tasks. Emission "
"rates are the hard input: measured with task-based sampling "
"(filter + CPC during the actual operation) or estimated from "
"dustiness indices times handling-energy factors, with "
"uncertainty factors of 3-10 acknowledged openly. Particle "
"dynamics enter for number-based predictions: coagulation "
"kernels for agglomeration, deposition velocities for surface "
"losses. Verification is a measurement campaign on a "
"representative day: personal breathing-zone filters (mass, "
"elemental carbon) plus a direct-reading instrument for the "
"time pattern, compared against the model prediction - "
"agreement within a factor of 2-3 is good performance for "
"workplace models, and systematic over- or under-prediction "
"recalibrates the emission factors. The deliverable is a "
"task-exposure matrix: every operation, its predicted "
"concentration, its control, its verification date."),
"key_points": [
"Two-box model: breathing-zone C = emission rate / near-field ventilation (demo: 1 mg/min -> 100 ug/m3).",
"Compare prediction to the limit BEFORE the process runs: 100 ug/m3 vs 1 ug/m3 CNT limit = enclose it.",
"Emission rates from dustiness tests or task measurements, with honest 3-10x uncertainty factors.",
"Nano twists: agglomeration, surface deposition losses, background-particle confounding.",
"Verification required: measurement day vs prediction; factor-of-2-3 agreement is good.",
"Deliverable: a task-exposure matrix - every operation, its concentration, its control, its verification date."],
"requirements": [
"Emission rates per task (measured or dustiness-derived with uncertainty factors).",
"Room and near-field ventilation rates (measured, not nameplate).",
"Background particle characterization for number-based monitoring.",
"Verification measurement campaign against model predictions."],
"standards": [
"EN 689:2018 - workplace exposure: measurement of exposure by inhalation (strategy and statistics).",
"ISO/TS 12025:2012 - quantification of nano-object release from powders by aerosol generation."],
"citations": [
"Jensen, K. A. et al. 'Dustiness behaviour of loose and compacted Bentonite and organoclay powders' Ann. Occup. Hyg. 53, 269-279 (2009).",
"Cherrie, J. W. 'The effect of room size and general ventilation on the relationship between near and far-field concentrations' Appl. Occup. Environ. Hyg. 14, 539-546 (1999)."],
"sig_lens": (
"Signature lens: exposure modeling is the Signature forecast - "
"the exposure computed before the first batch runs. The "
"Signature engineer sizes the control from the forecast, "
"measures to verify, and files the task-exposure matrix as "
"the living proof that the process stays under its limits.")},
{
"key": "ppe",
"name": "PPE and Engineering Controls: Hoods, Respirators, and Containment",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Controls for nanomaterials follow the hierarchy, and the "
"hierarchy is not a suggestion: elimination and substitution "
"first, engineering controls second, work practices third, "
"personal protective equipment last. Engineering controls do "
"the heavy lifting: fume hoods and ventilated enclosures for "
"powder transfer (a well-used hood cuts breathing-zone "
"particles by 90-99%), local exhaust ventilation at emission "
"points, and full containment - glove boxes, closed reactors - "
"for the highest-hazard materials like long carbon nanotubes. "
"Dust control starts at the source: buy dispersions instead of "
"dry powder, use closed transfer (drum-to-reactor couplings), "
"and clean with HEPA vacuums, never dry sweeping or compressed "
"air, which re-aerosolize everything. Respirators sit at the "
"bottom of the hierarchy because they protect only the wearer, "
"only while worn correctly: a half-face elastomeric respirator "
"with P100 filters carries an assigned protection factor (APF) "
"of 10 - it reduces exposure tenfold - and the demo shows why "
"that fails at 50 ug/m3 against the 1 ug/m3 CNT limit (50-fold "
"reduction needed; half-face gives 10; full-face gives 50, "
"exactly at the edge; supplied-air gives 1000). Fit-testing, "
"medical clearance, and a written program are not paperwork - "
"an unsealed respirator is a decoration. Gloves and lab coats "
"handle the dermal route; the hygiene rule is simple: no "
"eating, drinking, or face-touching in nano work areas, and "
"hand-washing before leaving."),
"how_it_works": (
"Control selection starts from the exposure model or "
"measurement: required reduction factor equals workplace "
"concentration divided by the limit. The demo runs the "
"respirator arithmetic - 50 ug/m3 against 1 ug/m3 needs 50x; "
"half-face APF 10 insufficient, full-face APF 50 marginal, "
"supplied-air APF 1000 adequate - and the engineering "
"conclusion: respirators alone cannot bridge large gaps, "
"which is why enclosures come first. Hood performance is "
"verified by face-velocity measurement (80-120 fpm typical) "
"and by tracer or particle-release tests at the sash: a hood "
"that contains on paper but leaks with the worker's arms "
"inside fails the test that matters. Containment for CNT "
"work means closed synthesis reactors vented through HEPA, "
"powder handling in glove boxes, and waste bagged inside "
"the enclosure. Cleaning validation uses surface wipe "
"samples (elemental carbon or metal analysis): a bench that "
"wipes dirty gets re-cleaned and the procedure rewritten. "
"The program is audited on a schedule - controls degrade, "
"filters load, sashes creep up - and every audit asks the "
"same question: does the breathing-zone measurement still "
"beat the limit?"),
"key_points": [
"Hierarchy: elimination/substitution -> engineering controls -> work practices -> PPE last.",
"Hoods cut breathing-zone particles 90-99%; containment (glove boxes, closed reactors) for top-hazard materials.",
"Never dry-sweep or blow down nano powders - HEPA vacuum only.",
"Demo: 50 ug/m3 vs 1 ug/m3 limit needs 50x; half-face APF 10 fails, supplied-air APF 1000 succeeds.",
"Respirators need fit-testing, medical clearance, and a written program - unsealed = decoration.",
"Verify everything: hood face velocity, containment leak tests, surface wipes, breathing-zone measurements."],
"requirements": [
"Exposure assessment (modeled or measured) giving the required reduction factor.",
"Engineering controls sized to the gap: hoods, LEV, or full containment.",
"Respiratory protection program (fit test, medical, training) where respirators are used.",
"Scheduled verification: face velocity, leak tests, surface wipes, breathing-zone sampling."],
"standards": [
"ANSI/ASSE Z9.5 - laboratory ventilation (fume hood performance).",
"OSHA 29 CFR 1910.134 - respiratory protection standard.",
"ISO/TS 12901-2:2014 - control banding (control selection framework)."],
"citations": [
"NIOSH 'Current Intelligence Bulletin 65: Occupational Exposure to Carbon Nanotubes and Nanofibers' DHHS (NIOSH) Publication No. 2013-145 (2013).",
"NIOSH 'General Safe Practices for Working with Engineered Nanomaterials in Research Laboratories' DHHS (NIOSH) Publication No. 2012-147 (2012)."],
"sig_lens": (
"Signature lens: controls are the Signature layered defense - "
"each layer independent, each verified, none trusted alone. "
"The Signature shop designs the process so the respirator is "
"bored: enclosures do the work, measurements prove it, and "
"PPE is the backup that never gets called.")},
{
"key": "lifecycle",
"name": "Lifecycle Thinking: From Synthesis to End of Life",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"A nanomaterial's hazard story does not end at the factory "
"gate - synthesis, formulation, use, and end of life each open "
"different exposure doors. Synthesis is the highest-exposure "
"stage: reactors opened, powders harvested, filters changed - "
"the operations that put the most material in the air per "
"kilogram made. Formulation (compounding into polymers, "
"coatings, dispersions) generally binds the particles into "
"matrices, dropping release by orders of magnitude - a carbon "
"nanotube locked in epoxy is not an airborne fiber. Use-phase "
"release depends on the product: textiles shed silver with "
"washing, sunscreens wash off skin into water, composites "
"release particles when sanded, drilled, or burned. End of "
"life decides the environmental loading: incineration destroys "
"carbon nanomaterials but concentrates metals in ash; "
"landfilling buries them until liners age; recycling streams "
"can re-aerosolize what formulation had bound. The demo runs "
"a mass balance for a 100 kg production batch: 2% fugitive "
"emission (2 kg) captured at 99% leaves 20 grams released - "
"the arithmetic that turns 'some escapes' into a number. "
"Lifecycle assessment forces the honest question: where, "
"across the whole life, does this material actually meet "
"biology - and is the control placed there?"),
"how_it_works": (
"Lifecycle analysis maps the material flow stage by stage: "
"production volume in, product distribution out, release "
"fractions per stage from measurements or conservative "
"defaults. The demo's mass balance is the template - "
"production times fugitive fraction times (1 minus capture "
"efficiency) equals environmental release - applied at each "
"stage with stage-specific numbers (synthesis 1-5% fugitive "
"without containment; formulation 0.01-0.1%; use-phase from "
"product testing; end-of-life from waste statistics). "
"Use-phase release is tested directly: washing machines for "
"textiles (silver in effluent per wash cycle), weathering "
"chambers for coatings, abrasion/sanding rigs for composites "
"with particle counting of the debris, and combustion tests "
"for incineration fate. End-of-life modeling uses waste-flow "
"statistics: what fraction goes to incineration, landfill, "
"recycling in each market. The output is a release inventory "
"by stage and compartment (air, water, soil), which feeds "
"environmental exposure models - and the design feedback: "
"if the inventory shows use-phase sanding dominates, the "
"product gets a no-sanding label or a bound formulation; if "
"washing dominates, the silver gets bound tighter or the "
"loading drops."),
"key_points": [
"Four stages, four exposure doors: synthesis (highest), formulation (binding), use (product-specific), end of life.",
"Demo: 100 kg made, 2% fugitive, 99% captured -> 20 g released - 'some escapes' as a number.",
"Formulation binds particles into matrices (CNT in epoxy is not an airborne fiber) - until sanding/drilling/burning.",
"Textiles shed silver in washing; sunscreens wash into water; incineration destroys carbon but concentrates metals.",
"End of life: incineration vs landfill vs recycling fates differ completely - model the waste flows.",
"Design feedback: place the control where the inventory says the release actually happens."],
"requirements": [
"Stage-by-stage material flow mapping with release fractions (measured or conservative).",
"Use-phase release testing: washing, weathering, abrasion, combustion as applicable.",
"Waste-flow statistics for end-of-life routing (incineration/landfill/recycling shares).",
"Release inventory by compartment (air, water, soil) feeding exposure models."],
"standards": [
"ISO 14040/14044 - life cycle assessment: principles, framework, requirements.",
"OECD GD 317 - environmental exposure assessment considerations for nanomaterials."],
"citations": [
"Gottschalk, F., Sonderer, T., Scholz, R. W. & Nowack, B. 'Modeled environmental concentrations of engineered nanomaterials (TiO2, ZnO, Ag, CNT, fullerenes) for different regions' Environ. Sci. Technol. 43, 9216-9222 (2009).",
"Nowack, B. et al. 'Potential scenarios for nanomaterial release and subsequent alteration in the environment' Environ. Toxicol. Chem. 31, 50-59 (2012)."],
"sig_lens": (
"Signature lens: lifecycle is the Signature whole-story "
"audit - no stage gets to hide. The Signature product file "
"carries the release inventory from reactor to landfill, "
"and every design change re-runs the mass balance, because "
"a hazard moved downstream is not a hazard removed.")},
{
"key": "risk_assessment",
"name": "Risk Assessment Arithmetic: Hazard Times Exposure",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Risk assessment is where nanotoxicology's two halves - hazard "
"and exposure - multiply. The paradigm is four steps old and "
"unmoved: hazard identification (what harm can it do?), "
"dose-response assessment (at what dose?), exposure assessment "
"(what dose do people get?), and risk characterization (is the "
"exposure below the safe dose?). The safe dose comes from the "
"animal or cell data divided by uncertainty factors - typically "
"10 for animal-to-human, 10 for human variability, and extras "
"for database gaps or severity - applied to the NOAEC or a "
"benchmark dose. The risk quotient (RQ) is the single number: "
"exposure divided by the reference value; below 1, acceptable; "
"above 1, manage. The demo runs two: CNT at 0.5 ug/m3 against "
"the 1 ug/m3 REL gives RQ 0.5 (acceptable with controls "
"verified); TiO2 at 0.05 mg/m3 against the 0.3 mg/m3 ultrafine "
"REL gives RQ 0.17. Nanomaterials strain the paradigm at every "
"step: hazard identification must pick the right dose metric "
"(surface area for insoluble particles), dose-response must "
"avoid overload artifacts, exposure assessment must handle "
"agglomeration and background particles, and the uncertainty "
"factors grow when the database is thin - which is why "
"read-across and grouping matter economically. Probabilistic "
"risk assessment is gaining ground: instead of single numbers, "
"distributions for exposure and hazard, giving the probability "
"that RQ exceeds 1 - an honest accounting of what is known "
"and what is guessed."),
"how_it_works": (
"The quantitative core is the reference value derivation: "
"take the point of departure (NOAEC from TG 413, or BMDL from "
"benchmark-dose modeling), adjust for dosimetric differences "
"(deposited dose per lung surface area, the MPPD model "
"standard), and divide by the uncertainty factors - the demo "
"uses the finished reference values (the RELs) to keep the "
"arithmetic on the risk quotient, the number decision-makers "
"actually read. Exposure comes from the task-exposure matrix "
"(modeled) or the measurement campaign (measured), as an "
"8-hour TWA in the predictive metric. RQ = exposure / "
"reference: the demo's 0.5 and 0.17 both sit below 1, but the "
"assessment doesn't stop there - sensitivity analysis asks "
"which input moves RQ most (usually the emission rate or the "
"dose metric choice), and the uncertainty narrative states "
"what would change the verdict. For new materials without a "
"REL, the reference value is derived fresh: read-across from "
"a tested analog with justification, or a new dose-response "
"study - the expensive path that grouping avoids. The "
"assessment is a living document: new toxicology, new "
"exposure data, or a process change re-opens it."),
"key_points": [
"Four steps: hazard ID -> dose-response -> exposure assessment -> risk characterization.",
"Risk quotient = exposure / reference value; below 1 acceptable, above 1 manage.",
"Demo: CNT 0.5 ug/m3 vs 1 ug/m3 REL -> RQ 0.5; TiO2 0.05 vs 0.3 mg/m3 -> RQ 0.17.",
"Reference values = point of departure / uncertainty factors (10x animal-human, 10x human variability).",
"Nano strains every step: right dose metric, no overload artifacts, agglomeration-aware exposure.",
"Probabilistic assessment (distributions, not points) honestly accounts for what is guessed."],
"requirements": [
"Point of departure (NOAEC/BMDL) in the predictive dose metric, overload-free.",
"Dosimetric adjustment to humans (deposited dose per lung surface area, MPPD).",
"Exposure as 8-h TWA in the same metric (modeled task matrix or measured campaign).",
"Uncertainty narrative + sensitivity analysis: which input moves the verdict."],
"standards": [
"ECHA Guidance R.8 - dose-response characterization and DNEL derivation (nanoform appendices).",
"WHO/IPCS 'Principles for modelling dose-response for the risk assessment of chemicals' (EHC 239)."],
"citations": [
"Kuempel, E. D., Geraci, C. L. & Schulte, P. A. 'Risk assessment and risk management of nanomaterials in the workplace: translating research to practice' Ann. Occup. Hyg. 56, 467-483 (2012).",
"Schulte, P. A. et al. 'Occupational exposure limits for nanomaterials: state of the art' J. Nanopart. Res. 12, 363-372 (2010)."],
"sig_lens": (
"Signature lens: risk assessment is the Signature ledger "
"close - hazard times exposure, divided by uncertainty, "
"equals a number a manager can act on. The Signature "
"assessor shows every input, prices the guesses openly, "
"and re-opens the books the moment new data arrives.")},
{
"key": "future",
"name": "The Future of Nanotoxicology: Pathways and New Approach Methods",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Nanotoxicology is outgrowing the 90-day rat study - not "
"abandoning it, but surrounding it with faster, more "
"mechanistic tools. The organizing framework is the Adverse "
"Outcome Pathway (AOP): a chain from the molecular initiating "
"event (a particle surface generating ROS, a fiber engaging "
"the inflammasome) through key events at increasing "
"biological scale (oxidative stress, cytokine release, "
"macrophage recruitment) to the adverse outcome (fibrosis, "
"tumors). AOPs turn scattered findings into testable chains: "
"measure the early key events in vitro, and the pathway "
"predicts the outcome without the 90-day wait. New Approach "
"Methods (NAMs) supply the measurements: lung-on-chip devices "
"with breathing membranes and flowing blood mimics, 3D "
"airway organoids, high-throughput transcriptomics across "
"doses, and computational models (QSARs for nanomaterials, "
"read-across engines) that predict hazard from properties. "
"The demo scores a NAM battery - 5 assays times 20 reference "
"chemicals at 85% concordance gives 85 correct calls out of "
"100 - the validation arithmetic regulators demand before "
"accepting a method. The destination is integrated testing: "
"characterize deeply, screen in tier-1, probe key events in "
"NAMs, and reserve animals for the questions only animals "
"can answer - with grouping and read-across multiplying "
"every data point across material families."),
"how_it_works": (
"Building an AOP starts from the established knowledge in "
"this database: the fiber paradigm becomes 'frustrated "
"phagocytosis (MIE) -> NLRP3 activation (KE1) -> IL-1beta "
"release (KE2) -> chronic inflammation (KE3) -> fibrosis "
"(AO)', each link supported by cited evidence and each key "
"event measurable in vitro. NAMs then operationalize the "
"key events: lung-on-chip for the tissue-level events, "
"reporter cell lines for the molecular ones, omics for the "
"pathway scores. Validation follows the OECD Guidance "
"Document 34 principles: a defined endpoint, a defined "
"protocol, demonstrated reproducibility across labs, and a "
"reference-chemical set proving the applicability domain - "
"the demo's 85/100 concordance is the shape of that proof. "
"Regulatory acceptance moves through the AOP Wiki and OECD "
"adoption: once an AOP-informed testing strategy is "
"endorsed, industry can file NAM data in place of animal "
"studies for covered endpoints. The strategy for a new "
"material in 2030: full characterization, tier-1 screen, "
"AOP-mapped NAM battery, read-across to the family - and "
"the 90-day study only if the pathway leaves a question "
"open."),
"key_points": [
"AOPs chain mechanism to outcome: molecular initiating event -> key events -> adverse outcome (fibrosis, tumors).",
"Example: frustrated phagocytosis -> NLRP3 -> IL-1beta -> chronic inflammation -> fibrosis.",
"NAMs: lung-on-chip, airway organoids, high-throughput transcriptomics, nano-QSARs and read-across engines.",
"Demo: 5-assay battery x 20 reference chemicals at 85% concordance = 85/100 correct - the validation shape.",
"Validation per OECD GD 34: defined endpoint, protocol, inter-lab reproducibility, applicability domain.",
"Destination: integrated testing - animals reserved for questions only animals can answer."],
"requirements": [
"AOP construction from established evidence (AOP Wiki format) with measurable key events.",
"NAM battery mapped to the AOP's key events (chip, organoid, reporter, omics).",
"Validation against reference chemicals with published concordance.",
"Read-across/grouping justification multiplying data across the material family."],
"standards": [
"OECD Guidance Document 34 - validation of (Q)SAR and test methods.",
"OECD AOP Wiki and AOP development programme (Effectopedia/AOP knowledge base)."],
"citations": [
"Ankley, G. T. et al. 'Adverse outcome pathways: a conceptual framework to support ecotoxicology research and risk assessment' Environ. Toxicol. Chem. 29, 730-741 (2010).",
"Krewski, D. et al. 'Toxicity testing in the 21st century: a vision and a strategy' J. Toxicol. Environ. Health B 13, 51-138 (2010)."],
"sig_lens": (
"Signature lens: the future is the Signature shortcut - "
"mechanism mapped once, then read at speed. The Signature "
"lab builds the pathway library, validates the fast "
"instruments against it, and spends its animal budget only "
"where the map says 'unknown territory'.")},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == sorted(e["ladder_rank"] for e in ENTRIES), "ladder ranks not non-decreasing"
assert all(1 <= e["ladder_rank"] <= 10 for e in ENTRIES)
assert all(e["ladder_tier"] in ("foundations", "compounded", "advanced") for e in ENTRIES)
