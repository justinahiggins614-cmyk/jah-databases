#!/usr/bin/env python3
"""Entries 20-34 (advanced tier) for the Unsolved Geology databases."""

ENTRIES_20_34 = [
# ---------------------------------------------------------------- 20
{
 "key": "core-light-elements",
 "name": "What Light Elements Hide in Earths Core?",
 "group": "Deep Earth",
 "ladder_rank": 20, "ladder_tier": "advanced",
 "problem": ("Earths core is about 10 percent less dense than pure iron at core "
             "pressures - the famous density deficit. Something light is alloyed "
             "into the iron, and the leading candidates - silicon, oxygen, "
             "sulfur, carbon, hydrogen - each imply a different origin story."),
 "background": ("Seismology gives the cores density and sound speed precisely; "
             "high-pressure experiments give the properties of pure iron at the "
             "same conditions. The mismatch demands light elements: roughly 10 "
             "percent by weight in the liquid outer core, less in the solid inner "
             "core, which is how the inner core grows - freezing out iron and "
             "rejecting light elements upward, powering the geodynamo. Silicon "
             "entered iron during a reducing early magma ocean; oxygen entered "
             "under more oxidizing conditions; sulfur and carbon track the "
             "building blocks Earth accreted; hydrogen could have arrived with "
             "the oceans. Each candidate fits some data - sound speeds favor "
             "silicon and oxygen, cosmochemistry favors sulfur - and no "
             "combination is uniquely required."),
 "why_it_matters": ("The light-element recipe is a direct record of the conditions "
             "under which Earth formed - how reducing the early mantle was, what "
             "the building blocks were, when water arrived. It also controls how "
             "the inner core grows today and how much power the geodynamo has "
             "left."),
 "sig_pointer": ("The Signature system proposes a core-recipe inversion: combine "
             "seismic sound speeds, mineral-physics data, and cosmochemical "
             "constraints in one joint inversion with honest uncertainties. See "
             "the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the density deficit "
             "as a recipe with several possible ingredient lists - and proposes "
             "the joint inversion that would show which list the data actually "
             "require."),
 "signature_solution": (
     "Proposed approach. Step 1: assemble the three constraint families in one "
     "open database - seismic density and P/S sound speeds versus depth, "
     "mineral-physics measurements of iron alloys at core conditions, and "
     "cosmochemical abundances from chondrites and mantle samples. Step 2: run "
     "a joint Bayesian inversion over alloy compositions, reporting the full "
     "posterior - which recipes are allowed, which are ruled out, and how much "
     "the answer depends on prior assumptions. Step 3: test the winners against "
     "the inner-core growth constraint - the recipe must also explain the "
     "smaller deficit in the solid inner core via partitioning. Step 4: "
     "publish the sensitivity map - which single future measurement (a better "
     "sound speed, a new partitioning experiment) would shrink the allowed "
     "recipes most.\n"
     "Assumptions: that mineral-physics experiments reach true core conditions "
     "(pressure yes, temperature approximately); that seismic reference models "
     "are unbiased; that Earths building blocks resembled known chondrites.\n"
     "What would confirm it: the posterior collapsing onto one recipe family "
     "that also satisfies inner-core partitioning and cosmochemistry.\n"
     "What would kill it: the posterior staying broad no matter the data - the "
     "recipe genuinely underdetermined - or the winning recipe violating "
     "partitioning constraints.\n"
     "What this does NOT claim: it does not claim a unique recipe exists; it "
     "does not claim the core is homogeneous; it is not established science."),
 "citations": [
     "Hirose K et al. Composition and state of the core. Annu Rev Earth Planet Sci; 2013.",
     "Badro J et al. Core formation and core composition. Treatise on Geophysics; 2015.",
     "Litasov K D, Shatskiy A. Composition of the Earths core. Geochem Int; 2016."],
 "explorer": {
   "blurb": ("A deficit calculator: from the density shortfall it estimates how "
             "much light element each candidate would need, and compares the "
             "implied recipes."),
   "assumptions": {"deficit_pct": 10.0, "core_mass_kg": 1.94e24,
                   "si_density_effect": 1.6, "o_density_effect": 2.2},
   "model_src": (
     "def run(A):\n"
     "    si_wt = A[\"deficit_pct\"] / A[\"si_density_effect\"]\n"
     "    o_wt = A[\"deficit_pct\"] / A[\"o_density_effect\"]\n"
     "    si_mass_kg = si_wt / 100.0 * A[\"core_mass_kg\"]\n"
     "    return {\"silicon_wt_pct\": si_wt, \"oxygen_wt_pct\": o_wt,\n"
     "            \"silicon_mass_kg\": si_mass_kg}\n"),
   "steps": [("Silicon needed for a 10 percent deficit", "silicon_wt_pct", "wt%"),
             ("Oxygen needed for the same deficit", "oxygen_wt_pct", "wt%"),
             ("Implied silicon mass in the core", "silicon_mass_kg", "kg")],
   "confirm": ["The posterior collapses onto one recipe family satisfying partitioning and cosmochemistry.",
               "The sensitivity map identifies the decisive future measurement."],
   "refute": ["The posterior stays broad regardless of data, or the winning recipe violates partitioning."],
   "checks": [("silicon_wt_pct", 4.0, 10.0),
              ("oxygen_wt_pct", 3.0, 8.0),
              ("silicon_mass_kg", 5e22, 3e23)],
   "honesty": ("We do not know the recipe; this explorer only converts the "
               "density deficit into candidate abundances, which is the "
               "accounting every recipe must satisfy.")}
},
# ---------------------------------------------------------------- 21
{
 "key": "core-seismology",
 "name": "How Do Seismic Waves Constrain the Cores Chemistry?",
 "group": "Seismology",
 "ladder_rank": 21, "ladder_tier": "advanced",
 "problem": ("Seismic waves that traverse the core - PKP phases, normal modes - "
             "carry chemical information in their speeds, but extracting "
             "composition from wave speed requires untangling temperature, "
             "pressure, and alloying, which trade off against each other."),
 "background": ("The Preliminary Reference Earth Model has given density and "
             "seismic velocities versus depth since 1981, and modern arrays have "
             "sharpened them: the outer core is liquid (no S waves), the inner "
             "core is solid and seismically anisotropic - waves travel faster "
             "along the rotation axis. Mineral physicists compress iron alloys "
             "in diamond-anvil cells and shock experiments, measuring sound "
             "speeds to compare. The degeneracy is the problem: a hotter pure "
             "iron and a cooler iron-silicon alloy can have the same sound "
             "speed. Breaking it needs independent temperature anchors - the "
             "iron melting curve at 330 GPa, still uncertain by hundreds of "
             "degrees - and the inner-cores anisotropy, which constrains crystal "
             "structure and therefore which alloys are even possible."),
 "why_it_matters": ("Seismology is the only remote sensing of the core we will "
             "ever have - no drill will reach it. How much chemistry can truly "
             "be extracted from wave speeds sets the ceiling on what humanity "
             "can ever know about the center of its own planet."),
 "sig_pointer": ("The Signature system proposes a degeneracy-mapping program: "
             "quantify exactly which temperature-composition pairs the seismic "
             "data allow, and identify the single measurement that breaks the "
             "trade-off. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats core seismology as "
             "an underdetermined puzzle - and proposes mapping the solution "
             "space honestly instead of picking a favorite point in it."),
 "signature_solution": (
     "Proposed approach. Step 1: compile every core-traversing seismic "
     "observable - PKP travel times, normal-mode frequencies, inner-core "
     "anisotropy and attenuation - with full covariance, not just best "
     "values. Step 2: forward-model the observables for a grid of "
     "temperature-composition pairs using the latest mineral-physics equations "
     "of state, and map the misfit surface - the degeneracy made visible. "
     "Step 3: add the independent anchors one at a time - the melting curve, "
     "cosmochemical priors, the geodynamo power budget - and watch the allowed "
     "region shrink or refuse to. Step 4: compute the value of information - "
     "which unmade measurement collapses the allowed region most, and propose "
     "that experiment.\n"
     "Assumptions: that equations of state extrapolate correctly to core "
     "conditions; that seismic observables are free of systematic bias from "
     "mantle heterogeneity; that the inner core is close to uniform in the "
     "average.\n"
     "What would confirm it: the allowed region collapsing to a compact "
     "temperature-composition neighborhood consistent across all anchors.\n"
     "What would kill it: the region refusing to shrink - proof the data "
     "cannot determine chemistry - or anchors contradicting each other, "
     "implying a wrong equation of state.\n"
     "What this does NOT claim: it does not claim seismology alone determines "
     "composition; it does not claim the melting curve is known; it is not "
     "established science."),
 "citations": [
     "Dziewonski A M, Anderson D L. Preliminary reference Earth model. Phys Earth Planet Inter; 1981.",
     "Deuss A. Heterogeneity and anisotropy of Earths inner core. Annu Rev Earth Planet Sci; 2014.",
     "Antonangeli D et al. Sound velocities of iron alloys in the Earths core. Rev Geophys; 2018."],
 "explorer": {
   "blurb": ("A trade-off visualizer: it shows how temperature and light-element "
             "content compensate in matching observed wave speeds, mapping the "
             "degeneracy."),
   "assumptions": {"observed_vp_kms": 11.0, "pure_fe_vp_kms": 11.5,
                   "temp_coefficient": 0.0004, "alloy_coefficient": 0.06},
   "model_src": (
     "def run(A):\n"
     "    dv = A[\"pure_fe_vp_kms\"] - A[\"observed_vp_kms\"]\n"
     "    temp_only_C = dv / A[\"temp_coefficient\"]\n"
     "    alloy_only_wt = dv / A[\"alloy_coefficient\"]\n"
     "    mixed_temp_C = temp_only_C / 2.0\n"
     "    mixed_alloy_wt = alloy_only_wt / 2.0\n"
     "    return {\"temperature_only_C\": temp_only_C,\n"
     "            \"alloy_only_wt_pct\": alloy_only_wt,\n"
     "            \"mixed_temp_C\": mixed_temp_C,\n"
     "            \"mixed_alloy_wt_pct\": mixed_alloy_wt}\n"),
   "steps": [("Temperature rise explaining the speed drop alone", "temperature_only_C", "C"),
             ("Light elements explaining it alone", "alloy_only_wt_pct", "wt%"),
             ("A 50-50 mixed solution: extra temperature", "mixed_temp_C", "C"),
             ("A 50-50 mixed solution: alloy content", "mixed_alloy_wt_pct", "wt%")],
   "confirm": ["The allowed region collapses to a compact temperature-composition neighborhood across all anchors.",
               "The value-of-information analysis identifies the decisive experiment."],
   "refute": ["The region refuses to shrink, or independent anchors contradict each other."],
   "checks": [("temperature_only_C", 500.0, 2500.0),
              ("alloy_only_wt_pct", 4.0, 15.0),
              ("mixed_alloy_wt_pct", 2.0, 8.0)],
   "honesty": ("We do not know how much chemistry seismology can extract; this "
               "explorer only demonstrates the trade-off that makes the "
               "question hard.")}
},
# ---------------------------------------------------------------- 22
{
 "key": "core-formation",
 "name": "How Did Earths Core Form in the First Place?",
 "group": "Deep Earth",
 "ladder_rank": 22, "ladder_tier": "advanced",
 "problem": ("Earths iron core segregated from its rocky mantle within the first "
             "tens of millions of years - but whether it rained through a global "
             "magma ocean, ponded and diapired down, or arrived pre-formed in "
             "the building blocks is still contested."),
 "background": ("The hafnium-tungsten clock is the key witness: hafnium-182 "
             "decays to tungsten-182 with a 9-million-year half-life, and "
             "because hafnium stays in rock while tungsten follows metal, the "
             "tungsten isotopes of the mantle date core segregation to within "
             "about 30 million years of solar-system formation. But the "
             "mechanism is open. In the magma-ocean model, iron rained through "
             "thousands of kilometers of molten rock, equilibrating chemically "
             "on the way down. In the diapir model, metal ponded at the base of "
             "a shallower ocean and sank as giant blobs with little "
             "equilibration. The two predict different siderophile-element "
             "patterns in the mantle - and the mantle shows a puzzling excess "
             "of highly siderophile elements, explained either by a late veneer "
             "of meteorites after core formation or by inefficient segregation."),
 "why_it_matters": ("Core formation set the chemistry of everything above it - "
             "the mantles composition, the atmosphere, the oceans, and the "
             "availability of the elements life uses. It is the first great "
             "differentiation event, and its mechanism is written into every "
             "rock on Earth."),
 "sig_pointer": ("The Signature system proposes a segregation-mechanism test: "
             "use siderophile-element patterns and tungsten isotopes to "
             "discriminate magma-ocean rain from diapir descent, including the "
             "late veneer question. See the Signature Edition record for the "
             "full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats core formation as a "
             "race between raining iron and sinking blobs - and proposes the "
             "chemical fingerprints that would show which won."),
 "signature_solution": (
     "Proposed approach. Step 1: compile high-precision tungsten-isotope and "
     "highly-siderophile-element data for mantle samples spanning the "
     "accessible record - modern basalts, Archean komatiites, lunar samples as "
     "a no-plate-tectonics control. Step 2: forward-model the two segregation "
     "mechanisms - equilibrium rain versus disequilibrium diapirs - predicting "
     "the siderophile patterns and tungsten signatures each leaves. Step 3: "
     "test the late veneer separately: does the highly-siderophile excess "
     "require post-core meteorite addition, or can inefficient segregation "
     "supply it? Step 4: require the winning model to also match the "
     "light-element recipe constraints from the core-composition program.\n"
     "Assumptions: that mantle samples represent the bulk mantle (plume "
     "heterogeneity is a caveat); that metal-silicate partitioning experiments "
     "scale to planetary conditions; that the lunar control is informative "
     "about Earth.\n"
     "What would confirm it: one mechanism matching tungsten, siderophile, "
     "and light-element constraints simultaneously, with the veneer question "
     "resolved the same way.\n"
     "What would kill it: both mechanisms fitting with tuned parameters, or "
     "the veneer and segregation signals proving inseparable.\n"
     "What this does NOT claim: it does not claim the magma ocean was global "
     "or single; it does not date the Moons formation from this; it is not "
     "established science."),
 "citations": [
     "Kleine T et al. Hf-W chronology of the accretion and early evolution of asteroids and terrestrial planets. Geochim Cosmochim Acta; 2009.",
     "Rubie D C et al. Accretion and differentiation of the terrestrial planets. Space Sci Rev; 2015.",
     "Walker R J. Highly siderophile elements in the Earth, Moon and Mars. Chem Erde; 2009."],
 "explorer": {
   "blurb": ("A segregation-clock calculator: from hafnium-tungsten systematics "
             "it estimates core-formation timescales and compares rain versus "
             "diapir equilibration."),
   "assumptions": {"hf182_halflife_Ma": 8.9, "core_formation_Ma": 30.0,
                   "rain_equilibration": 0.9, "diapir_equilibration": 0.3},
   "model_src": (
     "def run(A):\n"
     "    halflives = A[\"core_formation_Ma\"] / A[\"hf182_halflife_Ma\"]\n"
     "    decayed = 1.0 - 0.5 ** halflives\n"
     "    contrast = A[\"rain_equilibration\"] / A[\"diapir_equilibration\"]\n"
     "    return {\"hf182_halflives_elapsed\": halflives,\n"
     "            \"hf182_decayed_fraction\": decayed,\n"
     "            \"equilibration_contrast\": contrast}\n"),
   "steps": [("Hf-182 half-lives elapsed in 30 Myr", "hf182_halflives_elapsed", ""),
             ("Fraction of Hf-182 decayed", "hf182_decayed_fraction", ""),
             ("Rain versus diapir equilibration contrast", "equilibration_contrast", "x")],
   "confirm": ["One mechanism matches tungsten, siderophile, and light-element constraints simultaneously.",
               "The late veneer question resolves the same way."],
   "refute": ["Both mechanisms fit with tuned parameters, or veneer and segregation signals prove inseparable."],
   "checks": [("hf182_halflives_elapsed", 2.0, 5.0),
              ("hf182_decayed_fraction", 0.8, 1.0),
              ("equilibration_contrast", 2.0, 5.0)],
   "honesty": ("We do not know the segregation mechanism; this explorer only "
               "shows why the hafnium-tungsten clock ticks fast enough to time "
               "it, and how different the mechanisms chemical fingerprints "
               "should be.")}
},
# ---------------------------------------------------------------- 23
{
 "key": "moho-nature",
 "name": "What Is the Moho Really Like?",
 "group": "Seismology",
 "ladder_rank": 23, "ladder_tier": "advanced",
 "problem": ("The Mohorovicic discontinuity - the crust-mantle boundary - was "
             "discovered in 1909 as a seismic velocity jump, but whether it is a "
             "sharp chemical boundary, a phase change, or a gradational "
             "alteration front differs between oceans and continents, and is "
             "still debated."),
 "background": ("Andrija Mohorovicic found that seismic waves speed up abruptly "
             "about 7 kilometers beneath the ocean floor and 30 to 70 kilometers "
             "beneath continents. Under oceans the Moho is often sharp: fresh "
             "basaltic crust over depleted mantle. But drilling has never "
             "penetrated an intact oceanic Moho - the deepest hole stopped in "
             "gabbros above it - and seismic profiles increasingly show a "
             "complex transition zone of interlayered gabbro and serpentinized "
             "peridotite. Beneath continents the Moho is stranger: in some "
             "places a sharp jump, in others a 10-kilometer-thick gradient, and "
             "in cratons sometimes seismically invisible. Whether the Moho is "
             "primarily compositional, metamorphic, or partly an artifact of "
             "how we image it remains open."),
 "why_it_matters": ("The Moho is the most fundamental boundary in solid-Earth "
             "geology - the floor of the crustal world. Its nature decides how "
             "continents grow (does new crust weld on from below?), how "
             "subduction starts, and what drilling the mantle would actually "
             "encounter."),
 "sig_pointer": ("The Signature system proposes a Moho-typology program: "
             "classify the boundary worldwide from uniform seismic analysis and "
             "test whether sharp, gradational, and invisible Mohos map onto "
             "tectonic history. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the Moho not as one "
             "surface but as a family of boundaries - and proposes the "
             "classification that would reveal what makes each type."),
 "signature_solution": (
     "Proposed approach. Step 1: reprocess a global set of wide-angle seismic "
     "profiles with one modern workflow, measuring Moho sharpness - the "
     "velocity gradient thickness - uniformly instead of inheriting "
     "historical picks. Step 2: classify every profile: sharp, gradational, "
     "layered, or absent, with uncertainty. Step 3: correlate the classes with "
     "tectonic age and history - do sharp Mohos mark young ocean crust and "
     "invisible ones mark reworked cratons? Step 4: confront the classes with "
     "petrology - can serpentinization fronts, magmatic underplating, and "
     "metamorphic gradients reproduce each class in forward models?\n"
     "Assumptions: that reprocessing removes analyst bias rather than adding "
     "workflow bias; that the profile set samples all tectonic settings; that "
     "petrological models capture the real velocity structure.\n"
     "What would confirm it: Moho classes mapping cleanly onto tectonic "
     "history, with forward models reproducing each class from known "
     "processes.\n"
     "What would kill it: sharpness proving to be mostly a function of seismic "
     "frequency and profile geometry - an imaging artifact, not geology.\n"
     "What this does NOT claim: it does not claim the Moho is not a real "
     "boundary; it does not claim drilling would find any particular rock; it "
     "is not established science."),
 "citations": [
     "Mooney W D, Meissner R. Multi-genetic origin of crustal reflectivity. Geophys J Int; 1992.",
     "Collins J A et al. Seismic structure of the oceanic crust. Treatise on Geophysics; 2015.",
     "Prodehl C, Mooney W D. Exploring the Earths crust - history and results of controlled-source seismology. GSA Memoir; 2012."],
 "explorer": {
   "blurb": ("A boundary-sharpness calculator: from velocity profiles it "
             "quantifies Moho gradient thickness and shows how imaging "
             "frequency can blur a sharp boundary."),
   "assumptions": {"oceanic_moho_km": 7.0, "continental_moho_km": 40.0,
                   "vp_crust_kms": 6.8, "vp_mantle_kms": 8.1,
                   "seismic_wavelength_km": 2.0},
   "model_src": (
     "def run(A):\n"
     "    jump = A[\"vp_mantle_kms\"] - A[\"vp_crust_kms\"]\n"
     "    contrast = A[\"vp_mantle_kms\"] / A[\"vp_crust_kms\"]\n"
     "    resolvable = A[\"seismic_wavelength_km\"] / 4.0\n"
     "    return {\"velocity_jump_kms\": jump,\n"
     "            \"velocity_contrast\": contrast,\n"
     "            \"resolution_limit_km\": resolvable,\n"
     "            \"crust_thickness_ratio\": A[\"continental_moho_km\"] / A[\"oceanic_moho_km\"]}\n"),
   "steps": [("P-wave velocity jump at the Moho", "velocity_jump_kms", "km/s"),
             ("Velocity contrast ratio", "velocity_contrast", "x"),
             ("Thinnest resolvable transition zone", "resolution_limit_km", "km"),
             ("Continental versus oceanic crust thickness", "crust_thickness_ratio", "x")],
   "confirm": ["Moho classes map cleanly onto tectonic history, with forward models reproducing each class.",
               "Reprocessing converges across independent teams."],
   "refute": ["Sharpness proves to be mostly a function of frequency and geometry - an imaging artifact."],
   "checks": [("velocity_jump_kms", 0.8, 2.0),
              ("velocity_contrast", 1.1, 1.3),
              ("resolution_limit_km", 0.2, 1.0),
              ("crust_thickness_ratio", 4.0, 8.0)],
   "honesty": ("We do not know the Mohos true nature; this explorer only "
               "quantifies the velocity jump and the resolution limit, which "
               "together define what seismology can and cannot say.")}
},
# ---------------------------------------------------------------- 24
{
 "key": "tibet-uplift",
 "name": "Why Is Tibet So High and So Flat?",
 "group": "Orogeny",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": ("The Tibetan Plateau averages 5 kilometers high yet is remarkably "
             "flat - a combination no simple mountain-building model produces. "
             "When and how it rose, and why it did not crumple into jagged "
             "peaks, is one of orogenys deepest puzzles."),
 "background": ("India collided with Asia about 50 million years ago, doubling "
             "crustal thickness beneath Tibet to 70 kilometers. Simple "
             "shortening should build a jagged high range like the Himalaya "
             "next door; instead Tibet is a vast, low-relief plateau. Rival "
             "models: stepwise uplift as thrust sheets stacked from south to "
             "north; wholesale uplift when dense lower lithosphere delaminated "
             "and the plateau bobbed up; and lower-crustal channel flow, where "
             "weak deep crust flowed outward and inflated the plateau like a "
             "balloon. Paleoaltimetry - oxygen isotopes in ancient soils, fossil "
             "leaves - gives contradictory answers: some proxies say Tibet was "
             "high by 40 million years ago, others say the north rose only in "
             "the last 15 million years."),
 "why_it_matters": ("Tibet steers the Asian monsoon that waters billions of "
             "people, and its uplift history is the type case for how "
             "continental collisions build plateaus rather than just ranges. "
             "The mechanism decides how the deep crust behaves when continents "
             "collide - a process with no modern analogue anywhere else."),
 "sig_pointer": ("The Signature system proposes a plateau-timing transect: "
             "paleoaltimetry at uniform resolution from south to north Tibet "
             "to test stepwise versus wholesale uplift directly. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats Tibets flatness as "
             "the clue - and proposes that the north-to-south timing of uplift "
             "is the measurement that separates the rival mechanisms."),
 "signature_solution": (
     "Proposed approach. Step 1: run a south-to-north paleoaltimetry transect "
     "across Tibet with three independent proxies at each site - clumped "
     "isotope temperatures, fossil-leaf physiognomy, and volcanic glass "
     "hydrogen isotopes - so proxy disagreement is measured, not hidden. Step "
     "2: date each site with the same geochronology, building an uplift "
     "history per latitude band. Step 3: test the predictions - stepwise "
     "models predict uplift sweeping northward over tens of millions of years; "
     "delamination predicts rapid, plateau-wide uplift in one pulse; channel "
     "flow predicts early southern uplift with gradual northern inflation. "
     "Step 4: require the winner to also explain the flatness - low relief "
     "demands a smoothing process, and each model must name its own.\n"
     "Assumptions: that paleoaltimetry proxies record elevation rather than "
     "climate shifts (the central ambiguity); that the transect samples the "
     "plateaus history representatively; that one mechanism dominated.\n"
     "What would confirm it: all three proxies agreeing on an uplift history "
     "matching one models predictions, including the flatness.\n"
     "What would kill it: proxies disagreeing irreconcilably at the same "
     "sites - the data cannot resolve the history - or the timing matching no "
     "models predictions.\n"
     "What this does NOT claim: it does not claim Tibet rose in any particular "
     "way; it does not claim paleoaltimetry is reliable; it is not established "
     "science."),
 "citations": [
     "Royden L H et al. Surface deformation and lower crustal flow in eastern Tibet. Science; 1997.",
     "Molnar P et al. Mantle dynamics, uplift of the Tibetan Plateau. Tectonics; 1993.",
     "Rowley D B, Currie B S. Palaeo-altimetry of the late Eocene to Miocene Lunpola basin. Nature; 2006."],
 "explorer": {
   "blurb": ("An isostasy calculator: from crustal thickness it predicts "
             "Tibets elevation under Airy compensation, and shows how much "
             "extra buoyancy each mechanism needs."),
   "assumptions": {"tibet_crust_km": 70.0, "normal_crust_km": 35.0,
                   "crust_density": 2.8, "mantle_density": 3.3,
                   "observed_elevation_km": 5.0},
   "model_src": (
     "def run(A):\n"
     "    excess = A[\"tibet_crust_km\"] - A[\"normal_crust_km\"]\n"
     "    predicted = excess * (A[\"mantle_density\"] - A[\"crust_density\"]) / A[\"mantle_density\"]\n"
     "    residual = A[\"observed_elevation_km\"] - predicted\n"
     "    return {\"predicted_elevation_km\": predicted,\n"
     "            \"elevation_residual_km\": residual,\n"
     "            \"crustal_excess_km\": excess}\n"),
   "steps": [("Airy-predicted elevation from 70 km crust", "predicted_elevation_km", "km"),
             ("Observed minus predicted (needs extra mechanism)", "elevation_residual_km", "km"),
             ("Excess crustal thickness", "crustal_excess_km", "km")],
   "confirm": ["All three proxies agree on an uplift history matching one models predictions, including the flatness.",
               "The transect timing is unambiguous."],
   "refute": ["Proxies disagree irreconcilably at the same sites, or the timing matches no models predictions."],
   "checks": [("predicted_elevation_km", 3.0, 7.0),
              ("elevation_residual_km", -2.0, 2.0),
              ("crustal_excess_km", 25.0, 45.0)],
   "honesty": ("We do not know how Tibet rose; this explorer only computes "
               "what simple isostasy predicts, so the gap the rival mechanisms "
               "must fill is explicit.")}
},
# ---------------------------------------------------------------- 25
{
 "key": "rift-success",
 "name": "Why Do Some Rifts Split Continents and Others Fail?",
 "group": "Tectonics",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": ("The East African Rift is tearing a continent apart, but the "
             "equally dramatic Midcontinent Rift under Lake Superior - with "
             "kilometers of basalt - stalled a billion years ago and never made "
             "an ocean. What decides whether a rift succeeds or fails is not "
             "understood."),
 "background": ("Continental rifting starts the same way everywhere: the "
             "lithosphere stretches, thins, and melts. The Atlantic opened where "
             "Pangea rifted; the North Sea rifted hard and then stopped, leaving "
             "a failed rift full of oil. Classical models split rifting into "
             "active (a mantle plume pushes from below) and passive (far-field "
             "plate forces pull from the sides), but real rifts mix both, and "
             "the plume-or-pull debate has never cleanly predicted outcomes. "
             "Newer ideas invoke magma-assisted rifting - dikes doing the "
             "mechanical work of stretching - and structural inheritance, where "
             "ancient weaknesses steer new rifts. The Midcontinent Rifts "
             "failure despite enormous magma output is the hardest case: if "
             "magma does not guarantee success, what does?"),
 "why_it_matters": ("Every ocean basin began as a rift, so rift success is the "
             "gatekeeper of the supercontinent cycle. Failed rifts host some of "
             "the worlds great ore deposits - Sudbury nickel, the Midcontinent "
             "copper - and major petroleum systems, so the question is economic "
             "as well as academic."),
 "sig_pointer": ("The Signature system proposes a rift-outcome census: compare "
             "successful and failed rifts worldwide on identical structural, "
             "magmatic, and stress measurements to find the discriminating "
             "variables. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats rifts as a "
             "controlled comparison - successes versus failures - and proposes "
             "measuring both the same way to find what actually differs."),
 "signature_solution": (
     "Proposed approach. Step 1: build a global rift database - thirty "
     "successful (now oceans) and thirty failed - with uniform fields: total "
     "extension, magmatic volume, strain rate history, lithospheric thickness, "
     "and pre-rift structural grain. Step 2: run blind classification - which "
     "variables separate successes from failures? Step 3: test the leading "
     "discriminants mechanically in numerical models - does the variable that "
     "separates them in the data actually cause breakup in the physics? Step "
     "4: hindcast - hide five rifts, predict their outcomes from the "
     "discriminants, and score.\n"
     "Assumptions: that ancient rifts outcomes are known correctly (some "
     "failed rifts were later overprinted); that extension and magmatism can "
     "be reconstructed comparably across ages; that numerical models capture "
     "the controlling physics.\n"
     "What would confirm it: a small set of discriminants classifying rifts "
     "correctly, hindcasting successfully, and working mechanically in models.\n"
     "What would kill it: successes and failures overlapping on every measured "
     "variable - the outcome decided by unrecorded contingencies.\n"
     "What this does NOT claim: it does not claim plumes are irrelevant; it "
     "does not predict any active rifts fate; it is not established science."),
 "citations": [
     "Sengor A M C, Burke K. Relative timing of rifting and volcanism on Earth. Geology; 1978.",
     "Ebinger C J, Casey M. Continental breakup in magmatic provinces. Annu Rev Earth Planet Sci; 2001.",
     "Dunbar J A, Sawyer D S. How preexisting weaknesses control rift architecture. Geology; 1989."],
 "explorer": {
   "blurb": ("A stretching calculator: from extension factors it computes "
             "lithospheric thinning and melt generation, showing the "
             "mechanical path from rift to ocean."),
   "assumptions": {"beta": 3.0, "lithosphere_km": 120.0,
                   "mantle_temp_C": 1350.0, "stretch_Ma": 20.0},
   "model_src": (
     "def run(A):\n"
     "    thinned = A[\"lithosphere_km\"] / A[\"beta\"]\n"
     "    melt_km = max(0.0, (A[\"mantle_temp_C\"] - 1300.0) / 100.0) * thinned / 10.0\n"
     "    strain_rate = (A[\"beta\"] - 1.0) / (A[\"stretch_Ma\"] * 1e6 * 3.15e7)\n"
     "    return {\"thinned_lithosphere_km\": thinned,\n"
     "            \"melt_thickness_km\": melt_km,\n"
     "            \"strain_rate_per_s\": strain_rate}\n"),
   "steps": [("Lithosphere thickness after beta=3 stretching", "thinned_lithosphere_km", "km"),
             ("Melt generated by decompression", "melt_thickness_km", "km"),
             ("Mean strain rate over 20 Myr", "strain_rate_per_s", "per s")],
   "confirm": ["A small set of discriminants classifies rifts correctly and hindcasts successfully.",
               "The discriminants work mechanically in numerical models."],
   "refute": ["Successes and failures overlap on every measured variable."],
   "checks": [("thinned_lithosphere_km", 20.0, 80.0),
              ("melt_thickness_km", 0.5, 10.0),
              ("strain_rate_per_s", 1e-16, 1e-13)],
   "honesty": ("We do not know what decides rift fate; this explorer only "
               "quantifies the stretching and melting, which are the inputs "
               "every outcome theory starts from.")}
},
# ---------------------------------------------------------------- 26
{
 "key": "petm-cause",
 "name": "What Caused the Paleocene-Eocene Thermal Maximum?",
 "group": "Paleoclimate",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": ("56 million years ago Earth warmed 5 to 8 degrees in a geological "
             "instant, oceans acidified, and carbon isotopes plunged - the "
             "PETM. The carbon came from somewhere massive and fast, and the "
             "source is still disputed."),
 "background": ("The PETM is the closest ancient analogue to modern warming: a "
             "sharp negative carbon-isotope excursion marks a huge injection of "
             "light carbon, deep-sea benthic foraminifera suffered mass "
             "extinction, and the Arctic Ocean may have been subtropical. Two "
             "suspects dominate. Methane clathrates - ice-trapped methane on "
             "continental slopes - could have destabilized as oceans warmed, a "
             "feedback that needs only a nudge to start. Or the North Atlantic "
             "Igneous Province, erupting as the Atlantic opened, could have "
             "baked carbon-rich sediments and released CO2 directly. The isotope "
             "excursion is bigger than volcanism alone easily explains but "
             "smaller than pure methane demands; recent work favors a mix, "
             "without agreement on the proportions or the trigger."),
 "why_it_matters": ("The PETM is the natural experiment for rapid carbon "
             "release: how fast the climate responds, how long recovery takes "
             "(over 100,000 years), and which ecosystems collapse. Every "
             "climate model used for the future is tested against it - and the "
             "test is only as good as the carbon-source story."),
 "sig_pointer": ("The Signature system proposes a carbon-source apportionment: "
             "use the shape of the isotope excursion and independent warming "
             "proxies to partition the carbon between methane and volcanism. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the PETM carbon as "
             "a mixture to be unmixed - and proposes the measurements that "
             "would give each sources share."),
 "signature_solution": (
     "Proposed approach. Step 1: build the highest-resolution records of the "
     "excursion - carbon isotopes, boron-isotope pH, and temperature proxies - "
     "from expanded sections where the onset is not condensed. Step 2: invert "
     "the excursion shape for the source mix: methane gives a sharp, light "
     "spike; volcanic CO2 gives a broader, heavier one; the observed shape "
     "constrains the blend. Step 3: test the trigger separately - was there a "
     "volcanic pulse immediately before the onset (mercury, ash layers), or "
     "does warming lead carbon (clathrate feedback)? Step 4: run carbon-cycle "
     "models with the winning mix and require them to reproduce the recovery "
     "timescale, the hardest constraint.\n"
     "Assumptions: that the isotope records are global and not diagenetically "
     "overprinted; that boron isotopes record pH faithfully; that the "
     "sections capture the true onset rate.\n"
     "What would confirm it: a source mix reproducing the excursion shape, "
     "the trigger ordering, and the 100-thousand-year recovery in one model.\n"
     "What would kill it: the onset proving instantaneous beyond any "
     "resolvable structure - no shape to invert - or models requiring "
     "unphysical carbon amounts.\n"
     "What this does NOT claim: it does not claim the PETM predicts exact "
     "modern outcomes; it does not claim clathrates are safe today; it is not "
     "established science."),
 "citations": [
     "McInerney F A, Wing S L. The Paleocene-Eocene Thermal Maximum. Annu Rev Earth Planet Sci; 2011.",
     "Dickens G R et al. Dissociation of oceanic methane hydrate as a cause of the carbon isotope excursion. Geology; 1995.",
     "Gutjahr M et al. Very large release of mostly volcanic carbon during the PETM. Nature; 2017."],
 "explorer": {
   "blurb": ("A carbon-mixing calculator: from the isotope excursion it "
             "partitions the released carbon between methane and volcanic "
             "sources, and scales the warming."),
   "assumptions": {"excursion_permil": -8.0, "methane_permil": -60.0,
                   "volcanic_permil": -5.0, "total_carbon_Gt": 10000.0,
                   "sensitivity_C_per_double": 3.0},
   "model_src": (
     "def run(A):\n"
     "    f = (A[\"excursion_permil\"] - A[\"volcanic_permil\"]) / (A[\"methane_permil\"] - A[\"volcanic_permil\"])\n"
     "    methane_Gt = f * A[\"total_carbon_Gt\"]\n"
     "    volcanic_Gt = (1.0 - f) * A[\"total_carbon_Gt\"]\n"
     "    import math\n"
     "    warming = A[\"sensitivity_C_per_double\"] * math.log2(1.0 + A[\"total_carbon_Gt\"] / 2000.0)\n"
     "    return {\"methane_fraction\": f, \"methane_Gt\": methane_Gt,\n"
     "            \"volcanic_Gt\": volcanic_Gt, \"implied_warming_C\": warming}\n"),
   "steps": [("Methane fraction of the carbon", "methane_fraction", ""),
             ("Methane-source carbon", "methane_Gt", "Gt"),
             ("Volcanic-source carbon", "volcanic_Gt", "Gt"),
             ("Implied warming at 3C sensitivity", "implied_warming_C", "C")],
   "confirm": ["A source mix reproduces the excursion shape, the trigger ordering, and the recovery timescale in one model.",
               "The proportions are stable across sections."],
   "refute": ["The onset proves structureless, or models require unphysical carbon amounts."],
   "checks": [("methane_fraction", 0.0, 0.3),
              ("methane_Gt", 0.0, 3000.0),
              ("volcanic_Gt", 5000.0, 12000.0),
              ("implied_warming_C", 3.0, 10.0)],
   "honesty": ("We do not know the carbon source; this explorer only shows "
               "how the isotope math partitions it, which is the constraint "
               "every source story must satisfy.")}
},
# ---------------------------------------------------------------- 27
{
 "key": "zanclean-flood",
 "name": "How Did the Mediterranean Refill After the Messinian Crisis?",
 "group": "Stratigraphy",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": ("5.33 million years ago the Atlantic broke through at Gibraltar and "
             "the Mediterranean refilled - possibly in a megaflood, possibly "
             "gradually. The largest flood deposit on Earth may record it, or "
             "the evidence may say otherwise."),
 "background": ("The Zanclean flood hypothesis, proposed in 2009, holds that "
             "once the Gibraltar sill was breached, the Atlantic poured in at "
             "up to 100 million cubic meters per second - a thousand Amazon "
             "rivers - refilling the basin in months to two years and carving a "
             "200-kilometer-long channel into the sill. Seismic images show a "
             "giant erosional channel at Gibraltar, and the abrupt base of "
             "Zanclean deep-sea muds marks the refill. Skeptics note the channel "
             "could be older, the refill could have taken thousands of years "
             "through a rising sill, and some basins show gradual transitions. "
             "The flood rate, the duration, and even the catastrophism itself "
             "remain contested."),
 "why_it_matters": ("If the megaflood happened, it is the largest known flood "
             "in Earth history - a natural experiment in catastrophic landscape "
             "change, with implications for how fast sea level and coastlines "
             "can reorganize. It also bookends the Messinian crisis, closing "
             "the strangest chapter in Mediterranean geology."),
 "sig_pointer": ("The Signature system proposes a flood-forensics program: date "
             "the Gibraltar channel, the refill sediments, and the sill "
             "erosion surfaces on one timeline to test catastrophic versus "
             "gradual refill. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the refill as a "
             "crime scene with two stories - deluge or slow rise - and proposes "
             "the timeline that would convict one of them."),
 "signature_solution": (
     "Proposed approach. Step 1: date the Gibraltar erosional channel directly "
     "- cosmogenic burial dating of the channel floor versus the surrounding "
     "sill - to test whether the channel is Zanclean or older. Step 2: measure "
     "the refill rate from the basal Zanclean sediments: a catastrophic refill "
     "predicts a single sharp flooding surface with ripped-up Messinian clasts "
     "in deep basins; a gradual refill predicts a transgressive sequence over "
     "thousands of years. Step 3: model the hydraulics - given the sill "
     "geometry, what discharge does breaching produce, and does it carve the "
     "observed channel in the available time? Step 4: check the biological "
     "clock - how fast did marine fauna recolonize, and does that match months "
     "or millennia?\n"
     "Assumptions: that the channel can be dated (burial dating at these ages "
     "is at its limit); that the basal Zanclean is complete; that hydraulic "
     "models capture sill erosion feedback.\n"
     "What would confirm it: a Zanclean-dated channel, a single sharp flooding "
     "surface basin-wide, hydraulics matching the channel, and rapid "
     "recolonization.\n"
     "What would kill it: an older channel, gradual transgressive sequences, "
     "or fauna returning over millennia.\n"
     "What this does NOT claim: it does not claim the flood carved the "
     "Strait; it does not claim the desiccation was total; it is not "
     "established science."),
 "citations": [
     "Garcia-Castellanos D et al. Catastrophic flood of the Mediterranean after the Messinian salinity crisis. Nature; 2009.",
     "Estrada F et al. The Gibraltar Strait. Mar Geol; 2011.",
     "Bache F et al. Evolution of the Strait of Gibraltar. Basin Res; 2012."],
 "explorer": {
   "blurb": ("A megaflood calculator: from basin volume and sill geometry it "
             "estimates refill discharge and duration, comparing catastrophic "
             "and gradual scenarios."),
   "assumptions": {"basin_volume_km3": 3750000.0, "sill_width_km": 12.0,
                   "sill_depth_m": 300.0, "flow_speed_ms": 40.0},
   "model_src": (
     "def run(A):\n"
     "    area_m2 = A[\"sill_width_km\"] * 1000.0 * A[\"sill_depth_m\"]\n"
     "    discharge_m3s = area_m2 * A[\"flow_speed_ms\"]\n"
     "    seconds = A[\"basin_volume_km3\"] * 1e9 / discharge_m3s\n"
     "    years = seconds / 3.15e7\n"
     "    amazons = discharge_m3s / 2.09e5\n"
     "    return {\"discharge_m3_s\": discharge_m3s,\n"
     "            \"refill_years\": years,\n"
     "            \"amazon_equivalents\": amazons}\n"),
   "steps": [("Flood discharge through the sill", "discharge_m3_s", "m3/s"),
             ("Time to refill the basin", "refill_years", "yr"),
             ("Discharge in Amazon rivers", "amazon_equivalents", "Amazons")],
   "confirm": ["The channel dates Zanclean, the flooding surface is sharp and basin-wide, hydraulics match, and recolonization is rapid.",
               "All four lines agree."],
   "refute": ["The channel is older, sequences are gradual, or fauna return over millennia."],
   "checks": [("discharge_m3_s", 1e7, 5e8),
              ("refill_years", 0.1, 5.0),
              ("amazon_equivalents", 100.0, 2000.0)],
   "honesty": ("We do not know if the megaflood happened; this explorer only "
               "converts the sill geometry into a discharge, which is the "
               "physical claim at the heart of the debate.")}
},
# ---------------------------------------------------------------- 28
{
 "key": "ordovician-extinction",
 "name": "What Caused the End-Ordovician Mass Extinction?",
 "group": "Paleontology",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": ("444 million years ago, the second-largest mass extinction struck "
             "during an ice age - the only big-five extinction tied to "
             "glaciation rather than warming or impacts. Why an icehouse killed "
             "so thoroughly, in two distinct pulses, is unresolved."),
 "background": ("The end-Ordovician extinction removed about 85 percent of "
             "marine species in two pulses: the first as Gondwana glaciated and "
             "sea level fell, draining the shallow epicontinental seas where "
             "most life lived; the second as the ice melted, sea level rose, "
             "and deep waters turned anoxic. The Hirnantian glaciation itself "
             "is the puzzle - CO2 was high by modern standards, yet ice sheets "
             "grew. Hypotheses for the trigger range from enhanced weathering "
             "drawing down CO2, to a gamma-ray burst stripping the ozone layer "
             "(exotic, unproven), to ocean circulation changes. The two-pulse "
             "structure demands two kill mechanisms or one mechanism reversing, "
             "and the selectivity - brachiopods and trilobites devastated, "
             "others spared - must match whatever is proposed."),
 "why_it_matters": ("The Ordovician crisis is the only mass extinction caused "
             "by cooling, making it the critical test of how ice ages kill - "
             "directly relevant to understanding glaciations as evolutionary "
             "bottlenecks. It also reset marine ecosystems just before the "
             "rise of fish-dominated seas."),
 "sig_pointer": ("The Signature system proposes a two-pulse dissection: "
             "separate the kill mechanisms of the glaciation pulse and the "
             "deglaciation pulse with independent proxies, and require each to "
             "match its selectivity. See the Signature Edition record for the "
             "full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the two pulses as "
             "two crime scenes - and proposes that each needs its own "
             "conviction, not one theory stretched over both."),
 "signature_solution": (
     "Proposed approach. Step 1: build separate timelines for pulse one "
     "(glaciation, sea-level fall) and pulse two (deglaciation, anoxia) at "
     "high resolution from Anticosti Island, Sweden, and China sections. Step "
     "2: test pulse one against habitat loss - does the extinction track the "
     "draining of shallow seas quantitatively, with deep-water taxa spared? "
     "Step 3: test pulse two against anoxia - do uranium-isotope and "
     "pyrite-framoid proxies show anoxia expanding exactly where the second "
     "pulse hits? Step 4: attack the glaciation trigger itself - which CO2 "
     "drawdown mechanism (weathering, burial, circulation) can glaciate a "
     "high-CO2 world in models?\n"
     "Assumptions: that the two pulses are globally synchronous (still "
     "tested); that sea-level curves record eustasy not local tectonics; that "
     "anoxia proxies are not reset by later diagenesis.\n"
     "What would confirm it: pulse one tracking habitat loss and pulse two "
     "tracking anoxia, with one trigger mechanism glaciating the models.\n"
     "What would kill it: the pulses proving diachronous, or neither proxy "
     "matching its pulses selectivity.\n"
     "What this does NOT claim: it does not claim the gamma-ray burst "
     "happened; it does not claim CO2 levels are precisely known; it is not "
     "established science."),
 "citations": [
     "Sheehan P M. The Late Ordovician mass extinction. Annu Rev Earth Planet Sci; 2001.",
     "Finnegan S et al. The magnitude and duration of Late Ordovician-Early Silurian glaciation. Science; 2011.",
     "Harper D A T et al. The end Ordovician extinction. Palaeontology; 2014."],
 "explorer": {
   "blurb": ("A habitat-loss calculator: from sea-level fall and shelf "
             "hypsometry it estimates how much shallow-marine habitat vanished "
             "in pulse one."),
   "assumptions": {"sea_level_fall_m": 100.0, "shelf_area_km2": 30000000.0,
                   "habitat_loss_per_m": 0.008, "pulse1_loss_pct": 60.0},
   "model_src": (
     "def run(A):\n"
     "    habitat_lost = A[\"sea_level_fall_m\"] * A[\"habitat_loss_per_m\"]\n"
     "    area_lost_km2 = A[\"shelf_area_km2\"] * habitat_lost\n"
     "    implied_per_pct = habitat_lost * 100.0 / A[\"pulse1_loss_pct\"]\n"
     "    return {\"habitat_fraction_lost\": habitat_lost,\n"
     "            \"shelf_area_lost_km2\": area_lost_km2,\n"
     "            \"habitat_per_extinction_pct\": implied_per_pct}\n"),
   "steps": [("Fraction of shallow habitat drained", "habitat_fraction_lost", ""),
             ("Shelf area lost", "shelf_area_lost_km2", "km2"),
             ("Habitat loss per percent of species lost", "habitat_per_extinction_pct", "")],
   "confirm": ["Pulse one tracks habitat loss quantitatively and pulse two tracks anoxia.",
               "One trigger mechanism glaciates the high-CO2 models."],
   "refute": ["The pulses prove diachronous, or neither proxy matches its pulses selectivity."],
   "checks": [("habitat_fraction_lost", 0.3, 1.0),
              ("shelf_area_lost_km2", 1e7, 4e7),
              ("habitat_per_extinction_pct", 0.5, 3.0)],
   "honesty": ("We do not know the kill mechanisms; this explorer only "
               "quantifies the habitat loss, which is the physical quantity "
               "pulse-one theories must work with.")}
},
# ---------------------------------------------------------------- 29
{
 "key": "craton-destruction",
 "name": "Why Are Some Ancient Cratons Destroyed While Others Survive?",
 "group": "Precambrian",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": ("Cratons - the ancient hearts of continents - are supposed to be "
             "indestructible, with deep buoyant keels. Yet the eastern North "
             "China Craton lost its 200-kilometer keel in the Mesozoic while "
             "its western half kept it. What destroys a craton is an open "
             "question."),
 "background": ("Cratonic keels are cold, depleted, buoyant mantle roots that "
             "have survived for billions of years - the Kaapvaal, Siberian, "
             "and Canadian keels are intact. Eastern China is the "
             "counterexample: in the Jurassic and Cretaceous, its lithosphere "
             "thinned from 200 to under 80 kilometers, accompanied by massive "
             "volcanism and gold mineralization. Proposed destroyers include "
             "Pacific slab rollback hydrating and weakening the keel from "
             "below, delamination of the dense lower keel, and thermo-chemical "
             "erosion by upwelling asthenosphere. Seismic tomography shows a "
             "stagnant Pacific slab in the transition zone beneath the region - "
             "suggestive but not conclusive, since correlation is not mechanism, "
             "and the timing of destruction versus slab arrival is debated."),
 "why_it_matters": ("Craton destruction remade eastern Asias geology - its "
             "volcanoes, its earthquakes, its gold deposits - and it is the "
             "only observed case of a supposedly permanent continental root "
             "being removed. Understanding it decides whether cratons are "
             "truly forever or merely long-lived, with consequences for "
             "continental stability everywhere."),
 "sig_pointer": ("The Signature system proposes a destruction-mechanism test: "
             "compare the timing of keel loss, slab arrival, and volcanism in "
             "eastern China, and require the winning mechanism to match all "
             "three. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the destroyed keel "
             "as a demolished building - and proposes that the order of "
             "demolition, fire, and new construction identifies the "
             "demolition method."),
 "signature_solution": (
     "Proposed approach. Step 1: date the destruction precisely - xenolith "
     "thermobarometry and basalt geochemistry to track when the keel thinned, "
     "at 10-million-year resolution. Step 2: date the suspects on the same "
     "clock - Pacific slab arrival from plate reconstructions and tomography, "
     "delamination from the magmatic record, extension from basin histories. "
     "Step 3: test ordering - hydration-weakening predicts slab arrival "
     "before thinning; delamination predicts thinning before or with "
     "volcanism; each mechanism has a distinct sequence. Step 4: check the "
     "survivor - why did the western North China Craton keep its keel under "
     "the same Pacific regime? The mechanism must explain the contrast.\n"
     "Assumptions: that xenoliths record keel thickness faithfully; that plate "
     "reconstructions place the slab correctly in time; that the west-east "
     "contrast is real and not sampling bias.\n"
     "What would confirm it: one suspects arrival consistently preceding "
     "thinning, with the western survival explained by the same mechanism.\n"
     "What would kill it: thinning preceding all suspects, or the mechanism "
     "predicting western destruction that never happened.\n"
     "What this does NOT claim: it does not claim subduction destroys keels "
     "generally; it does not claim the keel is gone everywhere in the east; "
     "it is not established science."),
 "citations": [
     "Zhu R X et al. Destruction of the North China Craton. Natl Sci Rev; 2015.",
     "Menzies M A et al. Lithospheric thinning of the eastern North China Craton. Geol Soc London Spec Publ; 2007.",
     "Griffin W L et al. The origin and evolution of cratonic lithospheric mantle. Precambrian Res; 2009."],
 "explorer": {
   "blurb": ("A keel-buoyancy calculator: from depletion and temperature it "
             "estimates how buoyant a cratonic keel is, and how much "
             "weakening it takes to destroy it."),
   "assumptions": {"keel_km": 200.0, "thinned_km": 80.0,
                   "depletion_buoyancy_pct": 1.5, "thermal_deficit_C": 400.0},
   "model_src": (
     "def run(A):\n"
     "    lost_km = A[\"keel_km\"] - A[\"thinned_km\"]\n"
     "    lost_fraction = lost_km / A[\"keel_km\"]\n"
     "    thermal_density_pct = A[\"thermal_deficit_C\"] * 0.003\n"
     "    net_buoyancy = A[\"depletion_buoyancy_pct\"] - thermal_density_pct\n"
     "    return {\"keel_lost_km\": lost_km,\n"
     "            \"keel_lost_fraction\": lost_fraction,\n"
     "            \"net_keel_buoyancy_pct\": net_buoyancy}\n"),
   "steps": [("Keel thickness lost", "keel_lost_km", "km"),
             ("Fraction of the keel destroyed", "keel_lost_fraction", ""),
             ("Net buoyancy of the intact keel", "net_keel_buoyancy_pct", "pct")],
   "confirm": ["One suspects arrival consistently precedes thinning, with western survival explained by the same mechanism.",
               "All three clocks agree on the sequence."],
   "refute": ["Thinning precedes all suspects, or the mechanism predicts western destruction that never happened."],
   "checks": [("keel_lost_km", 80.0, 160.0),
              ("keel_lost_fraction", 0.4, 0.8),
              ("net_keel_buoyancy_pct", 0.0, 1.0)],
   "honesty": ("We do not know the destroyer; this explorer only quantifies "
               "how much keel vanished and how buoyant it was, which bounds "
               "what any destroyer had to overcome.")}
},
# ---------------------------------------------------------------- 30
{
 "key": "mantle-viscosity",
 "name": "How Fast Does the Mantle Really Flow?",
 "group": "Geodynamics",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": ("Mantle viscosity - the stiffness that sets the speed of "
             "convection, plate motions, and postglacial rebound - is "
             "uncertain by a factor of a hundred or more in the lower mantle. "
             "The deepest, largest part of the mantle is the least known."),
 "background": ("Viscosity is measured three ways, and they disagree. "
             "Postglacial rebound - Scandinavia and Canada still rising after "
             "the ice melted - probes the upper mantle well, giving about 10^20 "
             "to 10^21 pascal-seconds, but barely samples the deep mantle. "
             "The geoid - Earths gravity field - is sensitive to deep "
             "viscosity but trades off against unknown density anomalies. "
             "Laboratory deformation of lower-mantle minerals extrapolates "
             "over ten orders of magnitude in strain rate. The result: upper "
             "mantle viscosity is known within a factor of a few; lower mantle "
             "estimates span 10^21 to 10^23 pascal-seconds or more. Whether the "
             "mantle convects as one layer or two - the longest-running debate "
             "in geodynamics - hinges on this number."),
 "why_it_matters": ("Viscosity sets the tempo of the solid Earth: how fast "
             "plates move, how quickly the mantle mixes, whether subducted "
             "slabs stall at 660 kilometers or sink to the core. It is the "
             "single most important unknown in every model of Earths thermal "
             "evolution."),
 "sig_pointer": ("The Signature system proposes a viscosity-triangulation "
             "program: force the rebound, geoid, and laboratory estimates to "
             "confront each other in one inversion and map where they can and "
             "cannot agree. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the three viscosity "
             "estimates as three witnesses - and proposes putting them in one "
             "room to find where their stories overlap."),
 "signature_solution": (
     "Proposed approach. Step 1: assemble the three witness datasets with "
     "honest uncertainties - rebound uplift histories, the geoid with density "
     "anomaly covariances, and mineral-physics flow laws with extrapolation "
     "errors stated, not hidden. Step 2: run a joint inversion for a radial "
     "viscosity profile, reporting where the witnesses agree (the upper "
     "mantle) and the allowed range where they do not (the lower mantle). "
     "Step 3: test layered versus whole-mantle convection explicitly - which "
     "viscosity profiles permit slabs to penetrate 660 kilometers, and do "
     "those profiles survive the joint inversion? Step 4: identify the "
     "decisive future observation - a rebound measurement, a geoid "
             "improvement, a new mineral experiment - that would collapse the "
     "deep uncertainty most.\n"
     "Assumptions: that rebound, geoid, and labs sample the same effective "
     "viscosity (non-Newtonian rheology complicates this); that density "
     "anomalies driving the geoid are known well enough; that flow laws "
     "extrapolate meaningfully.\n"
     "What would confirm it: the three witnesses converging on one profile "
     "that also predicts slab penetration correctly.\n"
     "What would kill it: the witnesses proving irreconcilable - different "
     "effective viscosities because the rheology is stress-dependent, meaning "
     "no single profile exists.\n"
     "What this does NOT claim: it does not claim a single viscosity profile "
     "exists; it does not claim the lab extrapolations are valid; it is not "
     "established science."),
 "citations": [
     "Mitrovica J X, Forte A M. A new inference of mantle viscosity based on joint inversion of convection and glacial isostatic adjustment data. Earth Planet Sci Lett; 2004.",
     "Karato S I, Wu P. Rheology of the upper mantle. Science; 1993.",
     "King S D. Reconciling laboratory and observational models of mantle rheology. C R Geosci; 2016."],
 "explorer": {
   "blurb": ("A convection-tempo calculator: from viscosity it estimates "
             "mantle flow speeds and overturn times, showing what the "
             "uncertainty range implies."),
   "assumptions": {"visc_low_Pas": 1e21, "visc_high_Pas": 1e23,
                   "calibration_m_yr_Pas": 5e19, "mantle_m": 2.9e6},
   "model_src": (
     "def run(A):\n"
     "    k = A[\"calibration_m_yr_Pas\"]\n"
     "    v_fast = k / A[\"visc_low_Pas\"]\n"
     "    v_slow = k / A[\"visc_high_Pas\"]\n"
     "    t_fast_Ma = A[\"mantle_m\"] / v_fast / 1e6\n"
     "    t_slow_Ma = A[\"mantle_m\"] / v_slow / 1e6\n"
     "    return {\"flow_speed_fast_m_yr\": v_fast,\n"
     "            \"flow_speed_slow_m_yr\": v_slow,\n"
     "            \"overturn_fast_Ma\": t_fast_Ma,\n"
     "            \"overturn_slow_Ma\": t_slow_Ma}\n"),
   "steps": [("Flow speed at low viscosity", "flow_speed_fast_m_yr", "m/yr"),
             ("Flow speed at high viscosity", "flow_speed_slow_m_yr", "m/yr"),
             ("Overturn time, fast end", "overturn_fast_Ma", "Ma"),
             ("Overturn time, slow end", "overturn_slow_Ma", "Ma")],
   "confirm": ["The three witnesses converge on one profile that predicts slab penetration correctly.",
               "The decisive future observation is identified and pursued."],
   "refute": ["The witnesses prove irreconcilable - no single viscosity profile exists."],
   "checks": [("flow_speed_fast_m_yr", 0.01, 2.0),
              ("flow_speed_slow_m_yr", 0.0001, 0.05),
              ("overturn_fast_Ma", 1.0, 300.0),
              ("overturn_slow_Ma", 50.0, 30000.0)],
   "honesty": ("We do not know the deep viscosity; this explorer only "
               "converts the uncertainty range into flow speeds and overturn "
               "times, which is what the number means for the planet.")}
},
# ---------------------------------------------------------------- 31
{
 "key": "true-polar-wander",
 "name": "What Drives True Polar Wander?",
 "group": "Geodynamics",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": ("True polar wander - the entire solid Earth rotating relative to "
             "its spin axis - may have swung the planet 60 degrees or more in "
             "the past. Whether the big claimed events really happened, and "
             "what mass redistribution could drive them, is contested."),
 "background": ("A spinning planet is stabilized by its equatorial bulge; "
             "redistributing mass - growing ice sheets, sinking slabs, rising "
             "plumes - can tip the whole solid Earth so a different face "
             "points at the spin axis. The physics is uncontroversial; the "
             "history is not. A claimed 84-million-year-ago event would have "
             "moved the continents 60 degrees in a few million years - "
             "supported by some Pacific seamount paleomagnetism, contradicted "
             "by other datasets. Older proposed events in the Neoproterozoic "
             "are entangled with the Snowball Earth glaciations they might "
             "explain or be explained by. The core difficulty: distinguishing "
             "true polar wander (whole Earth tips) from ordinary plate motion "
             "(plates move over a fixed spin axis) requires a global "
             "paleomagnetic dataset that rarely exists."),
 "why_it_matters": ("If true polar wander is real and large, paleogeographic "
             "maps - the foundation of ancient climate and evolution stories - "
             "need a correction no textbook applies. It is also the largest-"
             "scale motion the solid Earth can undergo, linking mantle "
             "convection directly to the planets orientation in space."),
 "sig_pointer": ("The Signature system proposes a wander-verification program: "
             "define the statistical signature that separates true polar "
             "wander from plate motion, and test each claimed event against "
             "it. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats each claimed "
             "wander event as a suspect identification - and proposes the "
             "lineup procedure that would confirm or acquit it."),
 "signature_solution": (
     "Proposed approach. Step 1: formalize the discriminator - true polar "
     "wander moves all continents coherently around one equatorial axis, "
     "while plate motion moves them independently; write the statistical test "
     "before touching the data. Step 2: apply the test to the 84-million-year "
     "event with a compiled global paleomagnetic dataset, scoring coherence "
     "versus independence. Step 3: forward-model the mass redistribution - "
     "can sinking slabs or rising plumes at 84 million years supply the "
     "inertia change the claimed wander requires? Step 4: extend to the "
     "Neoproterozoic claims, where the test is harder and the stakes (Snowball "
     "Earth) are higher.\n"
     "Assumptions: that paleomagnetic datasets are globally representative "
     "(Pacific data dominate); that the inertia modeling captures the real "
     "mass anomalies; that the spin axis itself is stable.\n"
     "What would confirm it: multiple continents showing coherent motion "
     "about one axis at the same time, with a modeled mass redistribution "
     "sufficient to drive it.\n"
     "What would kill it: the coherence dissolving with better data - the "
     "events resolving into ordinary plate motions - or no mass anomaly big "
     "enough to drive the claimed wander.\n"
     "What this does NOT claim: it does not claim any wander event is real; "
     "it does not claim the physics is in doubt; it is not established "
     "science."),
 "citations": [
     "Evans D A D. True polar wander and supercontinents. Tectonophysics; 2003.",
     "Mitchell R N et al. True polar wander and the Cambrian explosion. Nature Geosci; 2012.",
     "Steinberger B, Torsvik T H. Absolute plate motions and true polar wander. Geophys J Int; 2008."],
 "explorer": {
   "blurb": ("A wander-speed calculator: from claimed rotation angles and "
             "durations it computes true polar wander rates and compares them "
             "with plate-motion speeds."),
   "assumptions": {"wander_deg": 60.0, "duration_Ma": 5.0,
                   "plate_speed_cm_yr": 5.0, "earth_radius_km": 6371.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    rate_deg_Ma = A[\"wander_deg\"] / A[\"duration_Ma\"]\n"
     "    arc_km = math.radians(A[\"wander_deg\"]) * A[\"earth_radius_km\"]\n"
     "    wander_cm_yr = arc_km * 1e5 / (A[\"duration_Ma\"] * 1e6)\n"
     "    vs_plate = wander_cm_yr / A[\"plate_speed_cm_yr\"]\n"
     "    return {\"wander_rate_deg_Ma\": rate_deg_Ma,\n"
     "            \"surface_shift_km\": arc_km,\n"
     "            \"wander_cm_yr\": wander_cm_yr,\n"
     "            \"vs_plate_speed\": vs_plate}\n"),
   "steps": [("Wander rate", "wander_rate_deg_Ma", "deg/Ma"),
             ("Surface shift at the equator", "surface_shift_km", "km"),
             ("Equivalent surface speed", "wander_cm_yr", "cm/yr"),
             ("Versus typical plate speed", "vs_plate_speed", "x")],
   "confirm": ["Multiple continents show coherent motion about one axis, with sufficient modeled mass redistribution.",
               "The statistical test separates wander from plate motion cleanly."],
   "refute": ["Coherence dissolves with better data, or no mass anomaly is big enough."],
   "checks": [("wander_rate_deg_Ma", 5.0, 25.0),
              ("surface_shift_km", 4000.0, 9000.0),
              ("wander_cm_yr", 50.0, 250.0),
              ("vs_plate_speed", 8.0, 60.0)],
   "honesty": ("We do not know if the great wander events happened; this "
               "explorer only converts the claims into speeds, which is what "
               "makes them extraordinary - or impossible.")}
},
# ---------------------------------------------------------------- 32
{
 "key": "kimberlite-ascent",
 "name": "How Do Kimberlite Pipes Rocket Up From the Deep Mantle?",
 "group": "Volcanology",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": ("Kimberlite magmas rise from 150 kilometers or deeper at meters "
             "per second - fast enough to carry diamonds intact - yet they are "
             "tiny-volume, volatile-rich melts that should freeze or stall. "
             "The ascent mechanism defies the standard rules of magma "
             "transport."),
 "background": ("Kimberlites are the deepest-sourced magmas on Earth, "
             "originating below the diamond stability field, and they erupt "
             "through thick cratonic keels that should be impassable. Their "
             "cargo proves the speed: diamonds graphitize if they rise slowly "
             "through hot mantle, so ascent from 200 kilometers in hours is "
             "required - meters per second, comparable to water in a pipe. "
             "Standard dike models struggle because kimberlite volumes are "
             "small and the melts are cold and viscous at depth. Proposed "
             "solutions invoke volatile exsolution - CO2 and water flashing to "
             "gas and driving the magma like a rocket - and pre-existing "
             "lithospheric weaknesses, but no model yet reproduces the speed, "
             "the volume, and the survival of the diamonds simultaneously."),
 "why_it_matters": ("Kimberlites are the primary source of diamonds and the "
             "only direct samples of the deep cratonic mantle - they are how "
             "we know what the keels are made of. Their ascent is also the "
             "extreme end-member of magma transport physics, testing every "
             "model of how melts move through rock."),
 "sig_pointer": ("The Signature system proposes an ascent-physics program: "
             "constrain the speed from diamond survival, the driving pressure "
             "from volatile contents, and require one model to satisfy both. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats each kimberlite "
             "pipe as a timed race from depth - and proposes that the "
             "diamonds themselves are the stopwatch."),
 "signature_solution": (
     "Proposed approach. Step 1: use diamond resorption - the rounding of "
     "diamond surfaces during ascent - as a speedometer: calibrate resorption "
     "rates experimentally and read ascent times from natural diamond suites. "
     "Step 2: measure pre-eruption volatile contents from melt inclusions to "
     "quantify the available gas-driving pressure. Step 3: build coupled "
     "ascent models - volatile exsolution driving fracture propagation - and "
     "require them to match both the diamond stopwatch and the pipe "
     "geometries observed in mines. Step 4: test the lithospheric-weakness "
     "hypothesis structurally - do pipes cluster on ancient faults, or "
     "punch through intact keel?\n"
     "Assumptions: that resorption calibrations apply to natural ascent "
     "conditions; that melt inclusions record pre-eruption volatiles; that "
     "mine exposures represent the pipes truly.\n"
     "What would confirm it: one coupled model matching diamond-derived "
     "speeds, volatile budgets, and pipe geometries, with structural control "
     "explaining the locations.\n"
     "What would kill it: resorption times contradicting volatile-driven "
     "models - speeds the physics cannot supply - or pipes showing no "
     "structural control and no consistent speed.\n"
     "What this does NOT claim: it does not claim all kimberlites ascend the "
     "same way; it does not locate new pipes; it is not established science."),
 "citations": [
     "Sparks R S J et al. Dynamical constraints on kimberlite volcanism. J Volcanol Geotherm Res; 2006.",
     "Kavanagh J L, Sparks R S J. Dynamics of dike intrusion. J Geophys Res; 2011.",
     "Russell J K et al. Kimberlite ascent. Lithos; 2012."],
 "explorer": {
   "blurb": ("An ascent calculator: from depth and required speed it computes "
             "ascent time, and compares volatile-driving pressure with the "
             "lithostatic load."),
   "assumptions": {"depth_km": 200.0, "speed_ms": 5.0,
                   "volatile_wt_pct": 15.0, "rock_density": 3300.0},
   "model_src": (
     "def run(A):\n"
     "    time_s = A[\"depth_km\"] * 1000.0 / A[\"speed_ms\"]\n"
     "    time_hr = time_s / 3600.0\n"
     "    lithostatic_MPa = A[\"rock_density\"] * 9.8 * A[\"depth_km\"] * 1000.0 / 1e6\n"
     "    gas_pressure_MPa = A[\"volatile_wt_pct\"] * 40.0\n"
     "    return {\"ascent_time_hr\": time_hr,\n"
     "            \"lithostatic_MPa\": lithostatic_MPa,\n"
     "            \"gas_pressure_MPa\": gas_pressure_MPa,\n"
     "            \"pressure_ratio\": gas_pressure_MPa / lithostatic_MPa}\n"),
   "steps": [("Ascent time from 200 km at 5 m/s", "ascent_time_hr", "hr"),
             ("Lithostatic pressure at source depth", "lithostatic_MPa", "MPa"),
             ("Gas pressure from 15 wt percent volatiles", "gas_pressure_MPa", "MPa"),
             ("Gas versus lithostatic pressure", "pressure_ratio", "x")],
   "confirm": ["One coupled model matches diamond-derived speeds, volatile budgets, and pipe geometries.",
               "Structural control explains pipe locations."],
   "refute": ["Resorption times demand speeds the physics cannot supply, or no consistent pattern emerges."],
   "checks": [("ascent_time_hr", 5.0, 25.0),
              ("lithostatic_MPa", 5000.0, 8000.0),
              ("gas_pressure_MPa", 300.0, 1000.0)],
   "honesty": ("We do not know the ascent mechanism; this explorer only "
               "converts depth and speed into times and pressures, which are "
               "the quantities any mechanism must produce.")}
},
# ---------------------------------------------------------------- 33
{
 "key": "supercontinent-rhythm",
 "name": "What Sets the Rhythm of the Supercontinent Cycle?",
 "group": "Geodynamics",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": ("Supercontinents have assembled roughly every 300 to 500 million "
             "years - but with only a handful of cycles in the record, "
             "geologists cannot tell whether the rhythm is a true period set "
             "by mantle physics or an episodic accident of plate geometry."),
 "background": ("The canonical sequence - Columbia/Nuna around 1.8 billion "
             "years ago, Rodinia at 1.0, Pangea at 0.3 - suggests a 500 to 700 "
             "million year beat, but each reconstruction is debated, the "
             "existence of some supercontinents (Pannotia) is contested, and "
             "three to four data points cannot establish periodicity. "
             "Theoretical candidates for a true period include the thermal "
             "time constant of the mantle - how long it takes heat to build "
             "under an insulating supercontinent - and the timescale of "
             "whole-mantle overturn. Episodic alternatives invoke contingent "
             "plate geometries: subduction zones happen to ring a "
             "supercontinent, slab pull happens to tear it apart, with no "
             "clock involved. Distinguishing a period from a pattern needs "
             "either more cycles or a mechanism whose timescale matches."),
 "why_it_matters": ("A true period would mean the solid Earth has a heartbeat "
             "- a predictable long-term rhythm governing sea level, climate, "
             "and evolution. An episodic cycle means the future is "
             "contingent, not clockwork. The difference decides whether "
             "geodynamics is ultimately predictable on the longest "
             "timescales."),
 "sig_pointer": ("The Signature system proposes a rhythm test: measure the "
             "mantle thermal time constant and the observed cycle intervals "
             "independently, and test whether they match better than chance. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the cycle as "
             "either a clock or a coincidence - and proposes the statistical "
             "test that would tell them apart."),
 "signature_solution": (
     "Proposed approach. Step 1: compile the best-supported supercontinent "
             "assembly dates with honest uncertainties - including the "
             "contested ones flagged as contested, not averaged away. Step 2: "
             "compute the mantle thermal time constant from first principles - "
             "diffusivity, mantle thickness, heat production - with uncertainty "
             "propagation, independent of the cycle record. Step 3: run the "
             "statistical test - do the observed intervals cluster around the "
             "thermal time better than random intervals would? Step 4: test in "
             "numerical models - do convection simulations with Earth-like "
             "parameters spontaneously produce periodic supercontinents, "
             "episodic ones, or none?\n"
     "Assumptions: that the supercontinent dates are meaningful (the weakest "
             "link - Nuna and Pannotia are debated); that the thermal time "
             "constant is the right candidate clock; that models capture the "
             "relevant physics.\n"
     "What would confirm it: observed intervals matching the thermal time "
             "within uncertainties, with models producing the same period "
             "spontaneously.\n"
     "What would kill it: intervals scattering with no relation to any "
             "physical timescale, or models producing supercontinents "
             "aperiodically under all parameters.\n"
     "What this does NOT claim: it does not claim the cycle is proven "
             "periodic; it does not claim Nuna or Pannotia existed; it is not "
             "established science."),
 "citations": [
     "Rogers J J W, Santosh M. Continents and Supercontinents. Oxford Univ Press; 2004.",
     "Zhao G C et al. Precambrian supercontinents. Gondwana Res; 2004.",
     "Silver P G, Behn M D. Intermittent plate tectonics? Science; 2008."],
 "explorer": {
   "blurb": ("A rhythm calculator: from supercontinent dates it measures the "
             "intervals, and compares them with the mantle thermal time "
             "constant."),
   "assumptions": {"nuna_Ma": 1800.0, "rodinia_Ma": 1000.0, "pangea_Ma": 300.0,
                   "mantle_thickness_m": 2.9e6, "diffusivity_m2_s": 1e-6},
   "model_src": (
     "def run(A):\n"
     "    i1 = A[\"nuna_Ma\"] - A[\"rodinia_Ma\"]\n"
     "    i2 = A[\"rodinia_Ma\"] - A[\"pangea_Ma\"]\n"
     "    mean_interval = (i1 + i2) / 2.0\n"
     "    scatter = abs(i1 - i2) / mean_interval\n"
     "    thermal_s = A[\"mantle_thickness_m\"] ** 2 / A[\"diffusivity_m2_s\"]\n"
     "    thermal_Ma = thermal_s / 3.15e7 / 1e6\n"
     "    return {\"interval_1_Ma\": i1, \"interval_2_Ma\": i2,\n"
     "            \"mean_interval_Ma\": mean_interval,\n"
     "            \"interval_scatter\": scatter,\n"
     "            \"thermal_time_Ma\": thermal_Ma}\n"),
   "steps": [("Nuna to Rodinia interval", "interval_1_Ma", "Ma"),
             ("Rodinia to Pangea interval", "interval_2_Ma", "Ma"),
             ("Mean interval", "mean_interval_Ma", "Ma"),
             ("Fractional scatter of the intervals", "interval_scatter", ""),
             ("Mantle thermal diffusion time", "thermal_time_Ma", "Ma")],
   "confirm": ["Observed intervals match the thermal time within uncertainties.",
               "Models spontaneously produce the same period."],
   "refute": ["Intervals scatter with no relation to any physical timescale, or models produce only aperiodic supercontinents."],
   "checks": [("interval_1_Ma", 600.0, 1000.0),
              ("interval_2_Ma", 500.0, 900.0),
              ("mean_interval_Ma", 500.0, 1000.0),
              ("thermal_time_Ma", 100000.0, 500000.0)],
   "honesty": ("We do not know if the cycle has a period; this explorer only "
               "lays the intervals beside the physical clock so the comparison "
               "is explicit - with three data points, the honest answer may "
               "be that the test cannot decide.")}
},
# ---------------------------------------------------------------- 34
{
 "key": "supereruption-clustering",
 "name": "Why Do Some Super-Eruptions Cluster in Geologic Time?",
 "group": "Volcanology",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": ("The largest volcanic eruptions in Earth history - the Siberian "
             "Traps, the Deccan Traps, CAMP - are not spread evenly through "
             "time but cluster in certain intervals, and several coincide with "
             "mass extinctions. Whether the clustering is real, and what "
             "synchronizes eruptions across a planet, is the deepest question "
             "in large-igneous-province geology."),
 "background": ("Large igneous provinces (LIPs) erupt a million cubic kilometers "
             "or more of basalt in under a few million years. Their timing "
             "correlates uncomfortably well with four of the five big mass "
             "extinctions - end-Permian with Siberia, end-Triassic with CAMP, "
             "end-Cretaceous with Deccan - and intriguingly with supercontinent "
             "breakup. Proposed synchronizers include mantle-plume clusters "
             "generated by deep-mantle upwelling episodes, plate-tectonic "
             "triggers such as slab avalanches at the 660-kilometer boundary "
             "sending pulses through the mantle, and pure coincidence "
             "amplified by better dating of young LIPs. The statistics are "
             "marginal: with only a dozen major LIPs in 500 million years, "
             "clustering tests have low power, and the extinction correlation "
             "may partly reflect that both LIPs and extinctions are easier to "
             "date when they coincide."),
 "why_it_matters": ("If LIPs cluster for a physical reason, the trigger is a "
             "planetary-scale process linking the deep mantle to the "
             "biosphere - the ultimate kill mechanism behind the volcanic "
             "mass extinctions. It would also mean super-eruptions are "
             "partially predictable from mantle state, not random lightning "
             "strikes."),
 "sig_pointer": ("The Signature system proposes a clustering-verification "
             "program: test LIP timing against randomness with full dating "
             "uncertainties, then test each synchronizer against the verified "
             "clusters. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats LIP clustering as "
             "either a signal from the deep mantle or a statistical mirage - "
             "and proposes the test that would tell them apart before arguing "
             "about mechanisms."),
 "signature_solution": (
     "Proposed approach. Step 1: build a uniform LIP catalog - volume, "
             "duration, and age with full uncertainties - and run the "
             "clustering statistics honestly, including the dating-precision "
             "bias that makes young LIPs look more clustered. Step 2: if "
             "clustering survives, test the plume-cluster hypothesis against "
             "deep-mantle structure - do clustered LIPs sit above the same "
             "large low-shear-velocity provinces? Step 3: test the slab-"
             "avalanche hypothesis - do clusters follow episodes of slab "
             "stagnation and penetration at 660 kilometers in plate "
             "reconstructions? Step 4: test the extinction link separately - "
             "for each LIP-extinction pair, require the kill mechanism "
             "(warming, anoxia, acidification) to match the extinction "
             "selectivity, not just the date.\n"
     "Assumptions: that the LIP catalog is complete for large events "
             "(older ones are lost to subduction); that dating uncertainties "
             "are honest; that mantle provinces have been stable long enough "
             "to correlate.\n"
     "What would confirm it: clustering surviving bias correction, with "
             "clusters matching one synchronizers predictions and the "
             "extinction mechanisms matching selectivity.\n"
     "What would kill it: the clustering dissolving under honest "
             "uncertainties - a mirage - or clusters matching no "
             "synchronizer.\n"
     "What this does NOT claim: it does not claim LIPs cause all mass "
             "extinctions; it does not claim the next super-eruption is "
             "predictable; it is not established science."),
 "citations": [
     "Ernst R E. Large Igneous Provinces. Cambridge Univ Press; 2014.",
     "Bryan S E, Ernst R E. Revised definition of large igneous provinces. Earth Sci Rev; 2008.",
     "Courtillot V, Renne P R. On the ages of flood basalt events. C R Geosci; 2003."],
 "explorer": {
   "blurb": ("A clustering calculator: from LIP ages it tests whether the "
             "timing differs from random, and scales the erupted volumes "
             "against extinction severity."),
   "assumptions": {"lip_ages_Ma": [16.0, 66.0, 132.0, 183.0, 201.0, 252.0, 260.0, 510.0],
                   "window_Ma": 500.0, "siberian_volume_km3": 4000000.0},
   "model_src": (
     "def run(A):\n"
     "    ages = sorted(A[\"lip_ages_Ma\"])\n"
     "    gaps = [ages[i+1] - ages[i] for i in range(len(ages) - 1)]\n"
     "    mean_gap = sum(gaps) / len(gaps)\n"
     "    expected_gap = A[\"window_Ma\"] / len(ages)\n"
     "    min_gap = min(gaps)\n"
     "    clustering_index = expected_gap / mean_gap\n"
     "    return {\"n_lips\": float(len(ages)),\n"
     "            \"mean_gap_Ma\": mean_gap,\n"
     "            \"expected_random_gap_Ma\": expected_gap,\n"
     "            \"smallest_gap_Ma\": min_gap,\n"
     "            \"siberian_volume_km3\": float(A[\"siberian_volume_km3\"])}\n"),
   "steps": [("LIPs in the catalog", "n_lips", ""),
             ("Mean interval between LIPs", "mean_gap_Ma", "Ma"),
             ("Expected interval if random", "expected_random_gap_Ma", "Ma"),
             ("Smallest gap (closest pair)", "smallest_gap_Ma", "Ma"),
             ("Siberian Traps volume", "siberian_volume_km3", "km3")],
   "confirm": ["Clustering survives bias correction, with clusters matching one synchronizers predictions.",
               "Extinction mechanisms match selectivity for each LIP-extinction pair."],
   "refute": ["The clustering dissolves under honest uncertainties, or clusters match no synchronizer."],
   "checks": [("n_lips", 5.0, 12.0),
              ("mean_gap_Ma", 40.0, 120.0),
              ("expected_random_gap_Ma", 40.0, 120.0),
              ("smallest_gap_Ma", 1.0, 30.0),
              ("siberian_volume_km3", 1e6, 1e7)],
   "honesty": ("We do not know if the clustering is real; this explorer only "
               "lays the intervals out plainly - with eight data points, the "
               "honest answer may be that randomness cannot be ruled out.")}
},
]
