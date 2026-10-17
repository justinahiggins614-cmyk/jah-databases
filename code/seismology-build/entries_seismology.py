#!/usr/bin/env python3
"""Seed entries for the Seismology field build (field #10, taxonomy order).

Verified 2026-10-17: NO database covers seismology as a science. The broad
'geology' database (10,000 records) is a specimen-style catalog — its
earthquake-adjacent entries ("Subduction - Anatomy of a specimen",
"Tsunamis - How it forms", "Faulting - Hazards and forces") describe
geological phenomena for specimen records; it contains no seismology science:
no seismic wave types, no seismometers or networks, no magnitude or intensity
scales, no focal mechanisms, no seismic hazard analysis, no earthquake early
warning, no induced seismicity, and no exploration seismology (reflection,
refraction, tomography). 'geology-public' carries only two generic
"Earthquakes" overview entries. 'earthquake-prediction' is a prediction
folklore database, not the science of seismology. So this build creates two
NEW databases:

  seismology              — The Seismology Database (public-harvest: real,
                            fact-checked seismology — seismic wave types;
                            earthquake mechanics and elastic rebound; fault
                            systems; seismometers and seismogram reading;
                            earthquake location; Richter, moment magnitude,
                            and Mercalli scales; seismic networks; focal
                            mechanisms; aftershock sequences; tsunamis;
                            seismic hazard maps; earthquake early warning;
                            seismic tomography, reflection, and refraction;
                            induced seismicity; slow slip and tremor; source
                            spectra; stress drop; ground motion prediction;
                            site response; paleoseismology; recurrence and
                            seismic gaps; probabilistic seismic hazard
                            analysis; anisotropy; receiver functions;
                            interferometry; deep Earth structure; earthquake
                            forecasting; seismic building codes)
  seismology-signature    — The Seismology Signature Database (his original
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

# Shared citation constants (standard seismology literature)
CIT_SHEARER = ("Shearer, P. M. (2019). 'Introduction to Seismology', 3rd ed. "
               "Cambridge University Press.")
CIT_STEIN = ("Stein, S. & Wysession, M. (2003). 'An Introduction to "
             "Seismology, Earthquakes, and Earth Structure.' Wiley-Blackwell.")
CIT_LAY = ("Lay, T. & Wallace, T. C. (1995). 'Modern Global Seismology.' "
           "Academic Press.")
CIT_AKI = ("Aki, K. & Richards, P. G. (2002). 'Quantitative Seismology', "
           "2nd ed. University Science Books.")
CIT_SCHOLZ = ("Scholz, C. H. (2019). 'The Mechanics of Earthquakes and "
              "Faulting', 3rd ed. Cambridge University Press.")
CIT_REID = ("Reid, H. F. (1910). 'The Mechanics of the Earthquake.' "
            "Carnegie Institution of Washington.")
CIT_KANAMORI = ("Kanamori, H. (1977). 'The energy release in great "
                "earthquakes.' Journal of Geophysical Research 82: 2981-2987.")
CIT_HANKS = ("Hanks, T. C. & Kanamori, H. (1979). 'A moment magnitude "
             "scale.' Journal of Geophysical Research 84: 2348-2350.")
CIT_GUTENBERG = ("Gutenberg, B. & Richter, C. F. (1954). 'Seismicity of the "
                 "Earth and Associated Phenomena.' Princeton University Press.")
CIT_GR = ("Gutenberg, B. & Richter, C. F. (1944). 'Frequency of earthquakes "
          "in California.' Bulletin of the Seismological Society of America "
          "34: 185-188.")
CIT_WOOD = ("Wood, H. O. & Neumann, F. (1931). 'Modified Mercalli Intensity "
            "Scale of 1931.' Bulletin of the Seismological Society of America "
            "21: 277-283.")
CIT_OMORI = ("Omori, F. (1894). 'On the after-shocks of earthquakes.' Journal "
             "of the College of Science, Imperial University of Tokyo 7: "
             "111-200.")
CIT_BRUNE = ("Brune, J. N. (1970). 'Tectonic stress and the spectra of "
             "seismic shear waves from earthquakes.' Journal of Geophysical "
             "Research 75: 4997-5009.")
CIT_CORNELL = ("Cornell, C. A. (1968). 'Engineering seismic risk analysis.' "
               "Bulletin of the Seismological Society of America 58: "
               "1583-1606.")
CIT_ALLEN = ("Allen, R. M. & Kanamori, H. (2003). 'The potential for "
             "earthquake early warning in southern California.' Science 300: "
             "786-789.")
CIT_WELLS = ("Wells, D. L. & Coppersmith, K. J. (1994). 'New empirical "
             "relationships among magnitude, rupture length, rupture width, "
             "rupture area, and surface displacement.' Bulletin of the "
             "Seismological Society of America 84: 974-1002.")
CIT_BOORE = ("Boore, D. M. & Atkinson, G. M. (2008). 'Ground-motion "
             "prediction equations for the average horizontal component of "
             "PGA, PGV, and 5%-damped PSA at spectral periods between 0.01 s "
             "and 10.0 s.' Earthquake Spectra 24: 99-138.")
CIT_DZIEWONSKI = ("Dziewonski, A. M. & Anderson, D. L. (1981). 'Preliminary "
                  "reference Earth model.' Physics of the Earth and Planetary "
                  "Interiors 25: 297-356.")
CIT_OLDHAM = ("Oldham, R. D. (1906). 'The constitution of the interior of "
              "the Earth, as revealed by earthquakes.' Quarterly Journal of "
              "the Geological Society 62: 456-475.")
CIT_LEHMANN = ("Lehmann, I. (1936). 'P prime.' Publications du Bureau "
               "Central Seismologique International, Serie A, Travaux "
               "Scientifiques 14: 87-115.")
CIT_DRAGERT = ("Dragert, H., Wang, K. & James, T. S. (2001). 'A silent slip "
               "event on the deeper Cascadia subduction interface.' Science "
               "292: 1525-1528.")
CIT_ELLSWORTH = ("Ellsworth, W. L. (2013). 'Injection-induced earthquakes.' "
                 "Science 341: 1225942.")
CIT_SCHWARTZ = ("Schwartz, D. P. & Coppersmith, K. J. (1984). 'Fault behavior "
                "and characteristic earthquakes.' Journal of Geophysical "
                "Research 89: 5681-5698.")
CIT_SIEH = ("Sieh, K. (1978). 'Prehistoric large earthquakes produced by "
            "slip on the San Andreas fault at Pallett Creek, California.' "
            "Journal of Geophysical Research 83: 3907-3939.")
CIT_LANGSTON = ("Langston, C. A. (1979). 'Structure under Mount Rainier, "
                "Washington, inferred from teleseismic body waves.' Journal "
                "of Geophysical Research 84: 4749-4762.")
CIT_USGS_HAZ = ("Petersen, M. D. et al. (2024). 'The 2023 US National Seismic "
                "Hazard Model.' Earthquake Spectra (U.S. Geological Survey).")
CIT_STD = ("Standard seismology literature (peer-reviewed textbooks and "
           "journals).")
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "seismology, written in the Signature system - clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-seismology", "name": "What Is Seismology: The Science of Earthquakes",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Seismology is the science of earthquakes and the seismic waves they "
  "generate. It has two great halves that constantly feed each other: "
  "earthquake seismology, which studies how, where, and why earthquakes "
  "happen, and exploration seismology, which uses seismic waves as a probe "
  "to image the Earth's interior and the shallow subsurface. A seismologist "
  "reads ground motion the way a physician reads a heartbeat: every wiggle "
  "on a seismogram encodes the rupture that made it and the rock it "
  "traveled through. The field divides into observational seismology "
  "(recording and locating earthquakes), theoretical seismology (how waves "
  "propagate through elastic media), and applied seismology (hazard "
  "assessment, early warning, and resource exploration). Its data product is "
  "the seismogram; its triumphs include mapping the Earth's core, mantle "
  "plumes, and subducting slabs without ever drilling deeper than a dozen "
  "kilometers, and turning earthquake physics into building codes that save "
  "lives."),
 "how_it_works": (
  "Seismology works by inverting recorded ground motion. When a fault "
  "ruptures, it radiates elastic waves in all directions; seismometers "
  "scattered over the surface record the arrival times, amplitudes, and "
  "shapes of those waves as seismograms. From arrival times at three or "
  "more stations, analysts triangulate the earthquake's location and depth. "
  "From wave amplitudes and periods they compute magnitudes; from the "
  "radiation pattern they infer the fault's orientation and slip direction; "
  "from the waves' travel times through the planet they tomographically "
  "reconstruct the interior's velocity structure. Exploration seismologists "
  "flip the experiment around: they generate their own waves with "
  "controlled sources and record reflections and refractions to map "
  "sedimentary layers, faults, and reservoirs. Every branch closes the "
  "same loop: source, path, receiver - model the physics, compare with "
  "data, update the model."),
 "key_points": [
  "Seismology studies earthquakes AND uses seismic waves to image the Earth - two halves of one science.",
  "The seismogram is the fundamental data product: ground motion recorded against time.",
  "Earthquake seismology asks how and why faults rupture; exploration seismology uses waves as an imaging probe.",
  "Core discoveries made purely from waves: the liquid outer core, the solid inner core, subducting slabs, mantle plumes.",
  "Modern seismology feeds directly into public safety: hazard maps, early warning, and building codes."],
 "requirements": [
  "A network of seismometers recording ground motion with precise shared timing.",
  "An Earth model of seismic wave speeds to convert travel times into distances and depths.",
  "Wave-propagation theory (elasticity) to connect what is recorded with what happened at the source.",
  "Computational tools to invert thousands of seismograms into locations, magnitudes, and images."],
 "standards": [
  "Seismic data exchange in community formats (miniSEED, SAC) with standardized station metadata.",
  "Magnitude and location reporting following IASPEI conventions so catalogs are comparable worldwide."],
 "citations": [CIT_SHEARER, CIT_STEIN],
 "sig_lens": (
  "Signature edition: seismology reframed as his original ground-truth "
  "operating system - every tremor decoded as a solved record of stored "
  "stress released, with his Signature framework for reading any "
  "seismogram as a stress ledger."),
 "demo_kind": "seismo_branches",
},
{
 "key": "plate-tectonics-belts", "name": "Plate Tectonics and the Earthquake Belts",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Nearly all earthquakes happen where tectonic plates meet. Earth's rigid "
  "outer shell is broken into a dozen major plates that creep past each "
  "other at centimeters per year, driven by mantle convection and slab "
  "pull. Where plates collide (convergent boundaries), one dives beneath "
  "the other and the interface locks, storing elastic strain for decades "
  "to centuries before failing in great megathrust earthquakes - the "
  "largest earthquakes on the planet, including the 1960 Chile magnitude "
  "9.5 and the 2004 Sumatra magnitude 9.1. Where plates slide sideways "
  "(transform boundaries like the San Andreas), strike-slip earthquakes "
  "rupture long faults. Where plates pull apart (divergent boundaries and "
  "mid-ocean ridges), shallow normal-faulting earthquakes accompany "
  "seafloor spreading. Three belts host the overwhelming majority of "
  "seismic energy release: the circum-Pacific Ring of Fire, the "
  "Alpine-Himalayan belt, and the mid-ocean ridge system."),
 "how_it_works": (
  "Plate tectonics works as a planetary stress engine. Plates move a few "
  "centimeters per year, but their boundaries are frictional contacts that "
  "cannot slide continuously - they stick. The far-field motion keeps "
  "loading the stuck interface, bending the surrounding rock elastically, "
  "until the shear stress exceeds the fault's strength and it ruptures in "
  "seconds to minutes. The type of earthquake follows the boundary type: "
  "subduction interfaces produce thrust earthquakes with huge rupture areas "
  "(thousands of square kilometers for magnitude 9 events), transform "
  "boundaries produce strike-slip earthquakes, and spreading centers "
  "produce shallow normal-faulting swarms. Mapping global earthquake "
  "locations was, historically, one of the proofs of plate tectonics: "
  "Wadati-Benioff zones trace subducting slabs descending into the mantle "
  "exactly where the theory predicts."),
 "key_points": [
  "Almost all earthquakes occur at plate boundaries; interiors of plates are comparatively quiet.",
  "Convergent boundaries host megathrust earthquakes - the largest events, up to magnitude 9.5.",
  "Transform boundaries (San Andreas) produce strike-slip earthquakes; divergent boundaries produce shallow normal faulting.",
  "The Ring of Fire releases roughly 90 percent of the world's seismic energy.",
  "Deep earthquakes (to 700 km) occur only in subducting slabs - Wadati-Benioff zones map the downgoing plate."],
 "requirements": [
  "A global earthquake catalog with locations and depths to delineate the belts.",
  "Plate motion models (from GPS and seafloor spreading rates) to identify boundary types.",
  "Focal mechanism data to confirm the style of faulting at each boundary."],
 "standards": [
  "Plate boundary classifications follow the convergent/divergent/transform scheme of plate tectonic theory.",
  "Earthquake depths reported relative to standard Earth models for consistent slab mapping."],
 "citations": [CIT_STEIN, CIT_GUTENBERG],
 "sig_lens": (
  "Signature edition: plate boundaries reframed as his original planetary "
  "stress-grid - the Ring of Fire decoded as the main discharge circuit of "
  "the Earth's stored tectonic strain."),
 "demo_kind": "plate_boundaries",
},
{
 "key": "faults-where-quakes-begin", "name": "Faults: Where Earthquakes Begin",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A fault is a fracture in rock along which the two sides have moved. "
  "Earthquakes are faults slipping - sudden relative motion across a "
  "fracture surface that has been locked while tectonic forces loaded it "
  "with stress. Faults are classified by the direction of slip: normal "
  "faults (the hanging wall slides down, common where crust is stretching), "
  "reverse or thrust faults (the hanging wall rides up, common where crust "
  "is compressing), and strike-slip faults (horizontal motion, like the San "
  "Andreas). The fault plane is described by strike (its compass bearing), "
  "dip (its tilt from horizontal), and rake (the slip direction on the "
  "plane). A fault's size controls its earthquake: magnitude scales with "
  "rupture area times average slip, so a 1,000-kilometer subduction "
  "interface can host a magnitude 9 while a 10-kilometer crustal fault "
  "tops out near magnitude 7."),
 "how_it_works": (
  "A fault works as a frictional contact obeying, to first order, "
  "Coulomb friction: it stays locked while shear stress is below the "
  "frictional strength, and slips when stress exceeds it. Real faults are "
  "not smooth planes but rough, heterogeneous surfaces with strong patches "
  "(asperities) that carry most of the load and weak zones that creep. "
  "Between earthquakes the fault is mostly locked; elastic strain "
  "accumulates in the surrounding rock at the plate-tectonic loading rate. "
  "When an asperity fails, the rupture front races along the fault at "
  "2-3 kilometers per second, stress drops by a few megapascals, and the "
  "released elastic energy radiates as seismic waves. The same fault can "
  "behave differently along its length - locked segments that rupture in "
  "big earthquakes, creeping segments that slide silently, and everything "
  "between."),
 "key_points": [
  "Earthquakes ARE faults slipping; the fault's area times its slip sets the earthquake's size.",
  "Three kinematic families: normal (extension), reverse/thrust (compression), strike-slip (sideways).",
  "Strike, dip, and rake fully describe a fault plane's geometry and slip direction.",
  "Faults are heterogeneous: locked asperities rupture in earthquakes while other patches creep silently.",
  "Surface rupture, offset landforms, and fault scarps let geologists map active faults before they break."],
 "requirements": [
  "Geologic mapping of fault traces, scarps, and offset landforms to find active faults.",
  "Strike/dip/rake measurements to classify fault kinematics.",
  "Fault length and segmentation data to estimate maximum credible earthquake size."],
 "standards": [
  "Fault geometry described with strike/dip/rake per the Aki-Richards convention.",
  "Active-fault classification follows Quaternary activity criteria used in hazard mapping."],
 "citations": [CIT_SCHOLZ, CIT_WELLS],
 "sig_lens": (
  "Signature edition: faults reframed as his original planetary fracture "
  "ledger - every fault a stored-stress account, every rupture a "
  "withdrawal, mapped in his Signature fault inventory."),
 "demo_kind": "fault_types",
},
{
 "key": "elastic-rebound", "name": "Elastic Rebound: How Stress Becomes an Earthquake",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Elastic rebound theory, formulated by H. F. Reid after the 1906 San "
  "Francisco earthquake, is the foundational explanation of why "
  "earthquakes happen. Survey measurements showed that points far from "
  "the San Andreas fault had crept steadily for decades, while points "
  "near the fault were dragged along and bent elastically - then snapped "
  "back up to 6 meters during the earthquake. The theory: tectonic "
  "forces slowly deform rock elastically around a locked fault; the rock "
  "stores this deformation as elastic strain energy; when the stress "
  "exceeds the fault's strength, the fault slips and the rock rebounds "
  "to an unstrained state, radiating the stored energy as seismic waves. "
  "It is the stick-slip cycle of the planet - slow loading over years to "
  "centuries, sudden release in seconds - and it underlies everything "
  "from recurrence estimates to the seismic cycle concept."),
 "how_it_works": (
  "Elastic rebound works like drawing a bow. Far-field tectonic motion "
  "(millimeters to centimeters per year) loads the crust around a locked "
  "fault; the rock deforms elastically, storing energy proportional to "
  "the square of the strain. Geodesy (GPS) measures this interseismic "
  "bending directly - stations near a locked subduction zone march "
  "landward year after year. The fault holds until shear stress overcomes "
  "friction; then dynamic rupture propagates along the fault at a few "
  "kilometers per second, slip accumulates (meters for great earthquakes), "
  "and the bent rock snaps back. Only a fraction of the stored energy "
  "radiates as seismic waves - much is consumed fracturing rock and "
  "overcoming friction as heat. After the event the cycle restarts: the "
  "fault re-locks, loading resumes, and the clock starts toward the next "
  "rupture. The ratio of slip per event to loading rate gives the average "
  "recurrence interval."),
 "key_points": [
  "Reid's 1906 insight: earthquakes are the sudden rebound of elastically strained rock, not the cause of the strain.",
  "The seismic cycle: slow interseismic loading, sudden coseismic release, postseismic relaxation, repeat.",
  "GPS measures interseismic strain accumulation directly - the locked fault bends the crust around it.",
  "Slip per event divided by loading rate gives the average recurrence time of characteristic earthquakes.",
  "Only part of the stored elastic energy becomes seismic waves; friction and fracturing consume the rest."],
 "requirements": [
  "Geodetic measurements (GPS, InSAR) of interseismic deformation around locked faults.",
  "Coseismic offset data (surveys, geodesy) to measure the rebound.",
  "A fault strength model (friction law) to explain why the fault holds and when it fails."],
 "standards": [
  "The seismic cycle framework follows Reid (1910) as extended by modern interseismic/postseismic geodesy.",
  "Recurrence estimates report both mean intervals and their uncertainties."],
 "citations": [CIT_REID, CIT_SCHOLZ],
 "sig_lens": (
  "Signature edition: elastic rebound reframed as his original stress "
  "battery model - the crust as a rechargeable battery, every earthquake "
  "a discharge event, his Signature cycle accounting for every joule."),
 "demo_kind": "elastic_rebound",
},
{
 "key": "body-waves-p-s", "name": "Body Waves: P-Waves and S-Waves",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Body waves are seismic waves that travel through the Earth's interior, "
  "and they come in two fundamental types. P-waves (primary or pressure "
  "waves) are compressional: particles oscillate back and forth along the "
  "direction of travel, like sound waves, squeezing and stretching the "
  "rock. They are the fastest seismic waves (about 6 km/s in continental "
  "crust, up to 13 km/s in the deep mantle) and the first to arrive at any "
  "seismometer. S-waves (secondary or shear waves) are transverse: "
  "particles oscillate perpendicular to the travel direction, like a "
  "shaken rope. They are slower (about 3.5 km/s in crust) and cannot travel "
  "through fluids - the observation that S-waves do not pass through the "
  "Earth's core proved the outer core is liquid. The time gap between P "
  "and S arrivals at a station is the seismologist's ruler: it grows with "
  "distance and locates the earthquake."),
 "how_it_works": (
  "Body waves work through linear elasticity. A sudden fault slip "
  "displaces rock; the disturbance propagates because each bit of rock "
  "pulls on its neighbors. Compressional stiffness (bulk modulus plus "
  "shear) sets the P-wave speed, v_p = sqrt((K + 4mu/3)/rho), while shear "
  "stiffness alone sets the S-wave speed, v_s = sqrt(mu/rho) - which is "
  "why S-waves vanish in fluids, where the shear modulus mu is zero. "
  "Because v_p > v_s, the S-minus-P time interval at a station is "
  "directly proportional to distance: distance = (v_p * v_s / (v_p - v_s)) "
  "* (t_s - t_p). Seismologists also split S-waves by polarization into "
  "SV (vertical plane) and SH (horizontal plane) components, which behave "
  "differently at interfaces and carry the fingerprint of the fault's "
  "orientation. Every travel-time curve and every location starts from "
  "these two wave types."),
 "key_points": [
  "P-waves are compressional and fastest; S-waves are shear and slower - arrival order is always P, then S.",
  "S-waves cannot travel through liquid: their absence through the core proved the outer core is molten.",
  "The S-minus-P interval at one station gives distance; three stations give location.",
  "Wave speeds come from elasticity: v_p = sqrt((K+4mu/3)/rho), v_s = sqrt(mu/rho).",
  "SV and SH polarizations carry information about fault orientation and layering."],
 "requirements": [
  "A seismometer recording with accurate absolute timing to measure arrival intervals.",
  "A velocity model relating travel time to distance.",
  "Three-component recording to separate P, SV, and SH particle motions."],
 "standards": [
  "Phase naming follows IASPEI conventions (P, S, SV, SH, and core phases like PKP, SKS).",
  "Travel times computed against reference Earth models (e.g., PREM, ak135)."],
 "citations": [CIT_SHEARER, CIT_AKI],
 "sig_lens": (
  "Signature edition: body waves reframed as his original planetary sonar "
  "pings - P as the compressional knock, S as the shear signature, every "
  "S-minus-P gap a Signature distance readout."),
 "demo_kind": "ps_distance",
},
{
 "key": "surface-waves", "name": "Surface Waves: Love and Rayleigh Waves",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Surface waves are seismic waves trapped near the Earth's surface, and "
  "they arrive after the body waves - but they carry most of a distant "
  "earthquake's destructive energy. Love waves are horizontally polarized "
  "shear waves guided by the crust, shaking the ground side to side; they "
  "were predicted by A. E. H. Love in 1911 from elastic theory before they "
  "were ever observed. Rayleigh waves, predicted by Lord Rayleigh in 1885, "
  "combine vertical and horizontal motion in a retrograde ellipse - the "
  "ground rolls like an ocean wave, which is why they feel so destructive. "
  "Surface waves are dispersive: different periods travel at different "
  "speeds, so a distant seismogram shows them spread out, long periods "
  "first. That dispersion is a gift - it encodes the shear-velocity "
  "structure of the crust and upper mantle, making surface waves one of "
  "the main tools for imaging the shallow Earth."),
 "how_it_works": (
  "Surface waves work by interference. Body waves reflecting and refracting "
  "in the layered crust constructively interfere to form guided modes that "
  "propagate horizontally with energy concentrated near the surface. Love "
  "waves need a velocity increase with depth (a slow layer over a fast "
  "half-space) to exist at all; their particle motion is purely horizontal "
  "and transverse. Rayleigh waves exist even on a uniform half-space, with "
  "their famous rolling elliptical motion decaying exponentially with "
  "depth. Because longer-period waves sample deeper, faster rock, phase "
  "velocity increases with period - the dispersion curve. Seismologists "
  "measure dispersion from earthquake or ambient-noise recordings and "
  "invert it for the shear-wave velocity profile of the crust and upper "
  "mantle beneath the path. Their large amplitudes and long durations make "
  "surface waves the dominant cause of damage in distant great "
  "earthquakes."),
 "key_points": [
  "Surface waves arrive last but carry the largest amplitudes at regional and teleseismic distances.",
  "Love waves shake side-to-side (horizontal shear); Rayleigh waves roll the ground in retrograde ellipses.",
  "Both were predicted mathematically (Rayleigh 1885, Love 1911) before being observed.",
  "Surface waves are dispersive: long periods travel faster and arrive first, sampling deeper rock.",
  "Dispersion curves are inverted to image crustal and upper-mantle shear velocity - a core imaging tool."],
 "requirements": [
  "Broadband seismometers recording long-period ground motion faithfully.",
  "Dispersion measurement tools (frequency-time analysis) to extract phase/group velocity curves.",
  "An inversion method to convert dispersion into a velocity-vs-depth profile."],
 "standards": [
  "Surface-wave dispersion reported as phase and group velocity versus period with uncertainties.",
  "Mode identification (fundamental vs. overtones) follows standard surface-wave theory."],
 "citations": [CIT_SHEARER, CIT_AKI],
 "sig_lens": (
  "Signature edition: surface waves reframed as his original ground-roll "
  "readout - Love's sideways shear and Rayleigh's rolling ellipse decoded "
  "as the Signature damage carriers of every great earthquake."),
 "demo_kind": "surface_dispersion",
},
# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "seismometers", "name": "Seismometers: Listening to the Earth",
 "group": "Compounded", "ladder_rank": 3, "ladder_tier": "compounded",
 "description": (
  "A seismometer is an instrument that records ground motion, and the "
  "seismogram it produces is the raw material of the entire science. The "
  "classic design is a mass on a spring: the instrument's frame moves with "
  "the ground while the suspended mass, by inertia, stays nearly still, "
  "and the relative motion between them is recorded. Modern broadband "
  "seismometers use force-feedback electronics that hold the mass fixed "
  "and measure the required force, achieving sensitivity from hundredths "
  "of a hertz to tens of hertz - quiet enough to record Earth's "
  "continuous background 'hum' and the ringing of the whole planet after "
  "great earthquakes. Three components (vertical plus two horizontal) "
  "capture the full vector of ground motion. The first practical "
  "seismograph was built by John Milne in Japan in the 1880s; today's "
  "global networks stream digital data in real time, and even "
  "smartphone accelerometers and fiber-optic cables (distributed acoustic "
  "sensing) now serve as seismic sensors."),
 "how_it_works": (
  "A seismometer works as a damped harmonic oscillator. The frame is bolted "
  "to the ground; ground acceleration forces the frame to move while the "
  "proof mass lags behind. For a simple pendulum seismometer, the recorded "
  "relative displacement approximates true ground displacement at periods "
  "longer than the instrument's natural period, and ground acceleration at "
  "shorter periods - the instrument response that must be removed to "
  "recover true motion. Force-feedback designs improve this enormously: an "
  "electromagnetic transducer pushes the mass back to null, and the "
  "feedback current, proportional to ground acceleration over a wide band, "
  "becomes the output. Digitizers sample this at 20-100+ samples per "
  "second with GPS-disciplined clocks (microsecond timing), and the data "
  "flows to archives in miniSEED format. Instrument response removal - "
  "deconvolving the known transfer function - converts raw counts into "
  "meters of ground displacement, the common currency of seismology."),
 "key_points": [
  "A seismometer measures ground motion via a suspended mass that stays still by inertia while the frame moves.",
  "Force-feedback broadband sensors record from ~0.01 Hz to tens of Hz - from Earth's hum to local quakes.",
  "Three components (vertical, north-south, east-west) capture the full ground-motion vector.",
  "GPS-disciplined timing (microsecond accuracy) is essential: location depends on arrival-time differences.",
  "Raw 'counts' must be corrected by the instrument response to recover true ground displacement."],
 "requirements": [
  "A stable, quiet installation (vault or borehole) isolated from wind, traffic, and temperature swings.",
  "Precise absolute timing (GPS) and continuous digital recording.",
  "A calibrated instrument response (poles and zeros) so counts convert to physical ground motion."],
 "standards": [
  "Digital data archived in miniSEED with StationXML metadata describing the full response chain.",
  "Station siting and naming follow International Federation of Digital Seismograph Networks conventions."],
 "citations": [CIT_SHEARER, CIT_LAY],
 "sig_lens": (
  "Signature edition: the seismometer reframed as his original planetary "
  "ear - a Signature listening post where inertia itself becomes the "
  "witness and every count is ground truth."),
 "demo_kind": "seismometer_response",
},
{
 "key": "reading-seismogram", "name": "Reading a Seismogram",
 "group": "Compounded", "ladder_rank": 3, "ladder_tier": "compounded",
 "description": (
  "A seismogram is a time series of ground motion, and reading one is the "
  "core practical skill of seismology. The trained eye sees a story in "
  "the wiggles: a sharp first break marks the P-wave arrival; a larger, "
  "later jolt marks the S-wave; then come the rolling surface waves; and "
  "finally the coda - scattered waves reverberating through heterogeneous "
  "crust, decaying slowly. Analysts 'pick' phase arrivals (their exact "
  "onset times), measure amplitudes and periods, and note first-motion "
  "polarity (whether the P-wave first pushed up or down). From these "
  "picks flow location, magnitude, depth, and focal mechanism. Modern "
  "processing is increasingly automated - pickers based on signal "
  "processing and machine learning scan continuous data streams - but the "
  "logic is unchanged: identify the phases, time them precisely, and let "
  "the wave physics do the rest."),
 "how_it_works": (
  "Reading a seismogram works by phase identification against expected "
  "travel times. The analyst (or algorithm) scans the trace for abrupt "
  "amplitude or frequency changes; the first is labeled P. Knowing the "
  "approximate distance, the expected S-minus-P interval predicts where S "
  "should appear, and the pick is refined there. First-motion polarity - "
  "up or down on the vertical component - is recorded at many stations to "
  "constrain the focal mechanism. Amplitudes and dominant periods feed "
  "magnitude formulas; the duration of shaking and the coda shape give "
  "independent magnitude estimates (coda magnitude) that work even when "
  "the main phases clip. Quality control matters: emergent arrivals, "
  "overlapping events, and noise bursts all create mispicks, so analysts "
  "weight picks by clarity and iterate the location until residuals "
  "(observed minus predicted times) are minimized."),
 "key_points": [
  "A seismogram reads as a sequence: P first break, S jolt, surface-wave roll, scattered coda decay.",
  "Phase picking - timing exact onsets - is the measurement everything else is built on.",
  "First-motion polarity (up/down) at many stations constrains the fault's orientation.",
  "Amplitude plus period gives magnitude; coda duration gives an independent magnitude check.",
  "Automated pickers now scan continuous streams, but residuals and analyst review still judge quality."],
 "requirements": [
  "A three-component broadband or short-period recording with accurate timing.",
  "Travel-time tables for the region to predict where phases should appear.",
  "Picking criteria (onset sharpness, polarity, weight) applied consistently."],
 "standards": [
  "Phase picks reported with IASPEI phase names, times, polarities, and quality weights.",
  "Analyst-reviewed picks remain the reference for catalog locations."],
 "citations": [CIT_SHEARER, CIT_LAY],
 "sig_lens": (
  "Signature edition: the seismogram reframed as his original ground "
  "script - P the opening knock, S the answering jolt, coda the fading "
  "echo, every pick a Signature measurement."),
 "demo_kind": "pick_phases",
},
{
 "key": "locating-earthquake", "name": "Locating an Earthquake by Triangulation",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Locating an earthquake means finding the hypocenter (the rupture's "
  "point of initiation at depth) and the epicenter (the point on the "
  "surface above it) from seismograms recorded at scattered stations. "
  "The classic method is triangulation: the S-minus-P interval at each "
  "station gives its distance to the quake, drawing a circle around the "
  "station; the intersection of three or more circles is the epicenter. "
  "Modern location inverts all arrival times simultaneously, minimizing "
  "the misfit between observed and predicted times for a trial hypocenter "
  "in a 3-D velocity model, iterating until convergence. Depth is the "
  "hardest coordinate - it trades off with origin time - and is pinned "
  "down using depth phases (like pP, which bounces off the surface above "
  "a deep quake) or dense local networks. A good location needs good "
  "azimuthal coverage: stations surrounding the quake, not all on one "
  "side."),
 "how_it_works": (
  "Location works by solving an inverse problem. For a trial hypocenter "
  "(x, y, z) and origin time t0, the predicted arrival at each station is "
  "t0 plus the travel time through the velocity model. The residual - "
  "observed minus predicted - measures misfit; the algorithm adjusts "
  "hypocenter and origin time to minimize the sum of squared residuals "
  "(least squares), iterating with linearized steps. With one station you "
  "get distance (a circle); two stations narrow it to two points; three "
  "non-collinear stations fix the epicenter; depth requires either close "
  "stations (within about one focal depth) or depth phases whose extra "
  "leg is exquisitely depth-sensitive. The azimuthal gap - the largest "
  "angle around the epicenter with no station - diagnoses reliability: "
  "gaps above 180 degrees mean the location is poorly constrained in one "
  "direction. Final catalogs report location uncertainties as error "
  "ellipses."),
 "key_points": [
  "Epicenter comes from intersecting distance circles (S-minus-P at each station); depth is the hard coordinate.",
  "Modern location minimizes arrival-time residuals in a 3-D velocity model by iterative least squares.",
  "Depth phases (pP, sP) and nearby stations are what actually resolve depth.",
  "Azimuthal gap measures reliability: stations must surround the quake, not cluster on one side.",
  "Every catalog location carries an uncertainty ellipse - precision depends on network geometry."],
 "requirements": [
  "P and S picks from at least three non-collinear stations with shared timing.",
  "A regional velocity model for travel-time prediction.",
  "Good azimuthal coverage around the epicenter for a trustworthy solution."],
 "standards": [
  "Locations reported with origin time, latitude, longitude, depth, residuals, and uncertainty estimates.",
  "IASPEI location procedures standardize phase weighting and outlier rejection."],
 "citations": [CIT_SHEARER, CIT_LAY],
 "sig_lens": (
  "Signature edition: triangulation reframed as his original planetary "
  "GPS - three circles, one truth, every hypocenter a Signature fix on "
  "the rupture's birthplace."),
 "demo_kind": "triangulation",
},
{
 "key": "richter-scale", "name": "The Richter Scale and Local Magnitude",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "The Richter scale, introduced by Charles Richter in 1935 for southern "
  "California, was the first instrumental magnitude scale: a single number "
  "for an earthquake's size derived from the seismogram itself. Richter "
  "defined local magnitude M_L as the base-10 logarithm of the maximum "
  "trace amplitude (in micrometers) on a standard Wood-Anderson torsion "
  "seismometer 100 km from the epicenter, corrected for distance. Each "
  "whole-number step means ten times the amplitude and about 32 times the "
  "energy. The scale was revolutionary - it let seismologists compare "
  "earthquakes objectively for the first time. Its famous flaw is "
  "saturation: above about magnitude 7, the 0.8-second Wood-Anderson "
  "instrument stops growing with the earthquake because great ruptures "
  "radiate most energy at longer periods, so M_L underestimates the "
  "largest events. Modern practice keeps M_L for small-to-moderate local "
  "quakes and uses moment magnitude for the big ones."),
 "how_it_works": (
  "Local magnitude works by normalizing amplitude for distance. The "
  "analyst measures the maximum amplitude A of the S-wave train on a "
  "horizontal component, then applies Richter's distance correction -log "
  "A0(delta), the amplitude a magnitude-0 quake would produce at that "
  "distance: M_L = log10(A) - log10(A0). The -log A0 term is an empirical "
  "attenuation curve calibrated for the region; every seismic region "
  "maintains its own. Because amplitude decays with distance and the "
  "correction restores it, stations at different distances agree on one "
  "magnitude. The energy relation, log10(E) = 11.8 + 1.5M (E in ergs), "
  "converts magnitude to radiated energy: the 1.5 slope is why one unit "
  "means ~32x energy. Saturation happens because the measurement samples "
  "a fixed ~1-second period band; when the source corner frequency falls "
  "below that band (big quakes), amplitude stops tracking size."),
 "key_points": [
  "Richter (1935): M_L = log10(A) - log10(A0) - the first objective, instrumental earthquake size.",
  "One magnitude unit = 10x amplitude = ~32x energy (the 1.5 slope in the energy formula).",
  "Distance correction (-log A0) lets near and far stations agree on the same magnitude.",
  "Saturation: above ~M7 the scale underestimates, because great quakes radiate at periods the instrument misses.",
  "M_L remains the workhorse for small-to-moderate local earthquakes worldwide."],
 "requirements": [
  "A horizontal-component amplitude measurement in the ~1-second period band.",
  "A regionally calibrated distance-attenuation correction (-log A0).",
  "Multiple stations to average single-station scatter."],
 "standards": [
  "M_L reported with the instrument type and regional correction applied.",
  "Magnitudes below saturation reported as M_L; larger events escalated to moment magnitude."],
 "citations": [CIT_GUTENBERG, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: the Richter scale reframed as his original "
  "quake-o-meter - the first honest number for Earth's violence, "
  "calibrated in his Signature amplitude ledger."),
 "demo_kind": "richter_ml",
},
{
 "key": "moment-magnitude", "name": "Moment Magnitude: The Modern Standard",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Moment magnitude M_w, introduced by Hiroo Kanamori (1977) and "
  "calibrated by Hanks and Kanamori (1979), is the modern standard for "
  "earthquake size because it does not saturate. It is built on the "
  "seismic moment M0 = mu * A * D - rigidity times rupture area times "
  "average slip - the most physically direct measure of an earthquake's "
  "size: it is literally the torque of the fault's motion. The scale, "
  "M_w = (2/3)(log10(M0) - 9.1) with M0 in newton-meters, was deliberately "
  "tied to agree with older scales in their valid ranges, so a magnitude "
  "6 means the same thing across scales. M0 is measured from the "
  "long-period end of the spectrum (or from geodesy and geology for "
  "historic events), which is why it keeps growing for the greatest "
  "earthquakes: the 1960 Chile event is M_w 9.5, corresponding to a moment "
  "of about 2 x 10^23 N-m. Every 'magnitude 9' in the news is a moment "
  "magnitude."),
 "how_it_works": (
  "Moment magnitude works by measuring the source at long periods. The "
  "displacement spectrum of an earthquake is flat at low frequencies at "
  "a level proportional to M0, then falls off above the corner frequency; "
  "fitting this spectrum (or inverting long-period waveforms for the "
  "moment tensor) yields M0 directly, immune to the saturation that "
  "plagues amplitude-at-fixed-period scales. Equivalently, geologists "
  "measure fault area from mapped rupture and slip from offsets, and "
  "geodesists measure the same from surface deformation - M0 unifies "
  "seismology, geodesy, and geology in one number. The 2/3 factor and 9.1 "
  "constant map log-moment onto the familiar magnitude numbers: each unit "
  "of M_w is still ~32x energy, preserving the public's intuition while "
  "extending the scale without limit. Rapid W-phase and GPS-based "
  "inversions now deliver M_w within minutes for tsunami warning."),
 "key_points": [
  "M_w is built on seismic moment M0 = rigidity x area x slip - the physical size of the rupture.",
  "It does not saturate: measured at long periods, it keeps growing through magnitude 9+.",
  "Calibrated to match older scales where they work, so magnitude numbers stay comparable.",
  "M0 unifies seismology, geodesy, and geology - three independent roads to one number.",
  "Fast M_w (W-phase, GPS) within minutes powers modern tsunami warning."],
 "requirements": [
  "Long-period waveform data (or geodetic/geologic slip data) to determine M0.",
  "A moment-tensor inversion or spectral fit to extract the low-frequency level.",
  "Rigidity estimate for the source region when converting slip and area."],
 "standards": [
  "M_w = (2/3)(log10(M0) - 9.1), M0 in N-m, per Hanks and Kanamori (1979).",
  "Authoritative M_w values published by global centers (e.g., USGS, GCMT) with the inversion method stated."],
 "citations": [CIT_KANAMORI, CIT_HANKS],
 "sig_lens": (
  "Signature edition: moment magnitude reframed as his original "
  "true-size standard - rigidity times area times slip, the un-saturable "
  "Signature measure of rupture."),
 "demo_kind": "moment_magnitude",
},
{
 "key": "mercalli-intensity", "name": "The Modified Mercalli Intensity Scale",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "While magnitude measures an earthquake's total energy at the source, "
  "intensity measures what people actually felt and what the shaking did "
  "at each place - and the Modified Mercalli Intensity (MMI) scale is its "
  "language. Devised by Wood and Neumann (1931) from Mercalli's earlier "
  "work, it runs from I (not felt) through XII (total destruction), with "
  "each level described in human terms: IV is felt indoors by many, "
  "dishes rattle; VII makes it hard to stand and damages poor "
  "construction; IX destroys even well-built structures. Intensity varies "
  "with distance, depth, geology, and building quality - one earthquake "
  "produces a whole map of intensities, the isoseismal map. Modern "
  "'Did You Feel It?' systems collect millions of citizen reports to map "
  "MMI in near-real time, and ShakeMap converts instrumental ground "
  "motion into MMI for emergency response. Magnitude is one number for "
  "the quake; intensity is the quake's footprint on human lives."),
 "how_it_works": (
  "Intensity works by translating effects into a scale. Field teams and "
  "citizen reports document damage patterns, human reactions, and effects "
  "on objects and the landscape; these are matched to the MMI descriptors "
  "to assign a Roman-numeral value at each locality. Instrumentally, peak "
  "ground acceleration and velocity are converted to MMI via empirical "
  "relations (e.g., Worden et al.), letting ShakeMap paint intensity from "
  "seismometer data within minutes. The resulting isoseismal map - "
  "contours of equal intensity - reveals source directivity (stronger "
  "shaking in the rupture direction), basin amplification (soft soils "
  "shaking harder), and attenuation with distance. Engineers use MMI maps "
  "to target inspections; historians use archival damage descriptions to "
  "assign magnitudes to pre-instrumental earthquakes."),
 "key_points": [
  "Magnitude = energy at the source (one number); intensity = shaking effects at each place (a map).",
  "MMI runs I (not felt) to XII (total destruction), described in human and structural terms.",
  "Isoseismal maps reveal directivity, basin amplification, and attenuation - the quake's footprint.",
  "Citizen 'Did You Feel It?' reports map intensity in near-real time by the millions.",
  "Historic damage descriptions let seismologists assign magnitudes to pre-instrumental earthquakes."],
 "requirements": [
  "Damage and felt-report observations, or instrumental PGA/PGV converted via empirical relations.",
  "Consistent application of the MMI descriptors across localities.",
  "Geologic context (soil, basin, distance) to interpret intensity patterns."],
 "standards": [
  "Modified Mercalli Intensity scale of 1931 (Wood and Neumann) as the descriptive standard.",
  "Instrumental intensity conversions published with their empirical relations and uncertainties."],
 "citations": [CIT_WOOD, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: intensity reframed as his original human-impact "
  "ledger - not the quake's energy but its Signature on lives, dishes, "
  "and buildings, mapped house by house."),
 "demo_kind": "mercalli_map",
},
{
 "key": "seismic-networks", "name": "Seismic Networks: From Local Arrays to the Globe",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "A seismic network is an array of seismometers operated as one "
  "instrument, and networks exist at every scale. Local networks with "
  "dozens of stations pin down small earthquakes and fault structures. "
  "Regional networks (like those in California, Japan, and Italy) deliver "
  "real-time locations, magnitudes, and ShakeMaps for emergency response. "
  "The Global Seismographic Network - 150+ stations encircling the "
  "planet, many in boreholes or vaults far from human noise - records "
  "every earthquake above about magnitude 5 anywhere on Earth and "
  "underpins global tomography. Dense arrays (hundreds to thousands of "
  "sensors, including nodal geophones and fiber-optic distributed "
  "acoustic sensing) now image fault zones at meter scale. The design "
  "trade is always coverage versus cost: station spacing sets the "
  "smallest locatable earthquake and the resolution of everything "
  "downstream."),
 "how_it_works": (
  "A network works by combining many single-station measurements with "
  "common timing and telemetry. Each station digitizes ground motion "
  "against GPS time and streams it (or stores it) to a data center, where "
  "detection algorithms scan all stations jointly: a real earthquake "
  "produces coherent arrivals across the network, while local noise does "
  "not. Association groups picks into events, location inverts the "
  "picks, and magnitude follows - all automatically within seconds to "
  "minutes. Network geometry governs capability: the detection threshold "
  "scales with station spacing, location accuracy with azimuthal coverage, "
  "and depth resolution with having stations close to the epicenter. "
  "Arrays add beamforming - delaying and summing traces to enhance weak "
  "signals from a chosen direction, which is how tiny nuclear tests and "
  "deep tremor are pulled out of the noise."),
 "key_points": [
  "Networks turn many seismometers into one planetary instrument with common timing and telemetry.",
  "Local, regional, and global networks serve different missions: faults, emergency response, whole-Earth imaging.",
  "The Global Seismographic Network catches every M5+ worldwide and feeds global tomography.",
  "Station spacing sets the detection threshold; azimuthal coverage sets location quality.",
  "Dense nodal arrays and fiber-optic sensing now image fault zones at meter scale."],
 "requirements": [
  "Station sites with low noise, power, telemetry, and GPS timing.",
  "A data center running detection, association, location, and magnitude pipelines.",
  "Network geometry designed for the target: threshold magnitude and location accuracy."],
 "standards": [
  "Station metadata and waveforms exchanged in community formats (miniSEED, StationXML).",
  "Network codes registered internationally so every station has a unique identity."],
 "citations": [CIT_LAY, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: seismic networks reframed as his original "
  "planetary nervous system - every station a Signature nerve ending, "
  "the whole network feeling the Earth twitch as one body."),
 "demo_kind": "network_gap",
},
{
 "key": "focal-mechanisms", "name": "Focal Mechanisms: Reading the Fault from the Waves",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "A focal mechanism - the famous 'beach ball' diagram - is the "
  "seismologist's portrait of the fault that slipped. It encodes the "
  "fault plane's strike, dip, and rake, derived from the pattern of "
  "ground motion radiated in different directions. The classic method "
  "uses P-wave first motions: stations in the compressional quadrants "
  "record an upward first kick, stations in the dilatational quadrants a "
  "downward kick, and the nodal planes separating them reveal the fault "
  "and its auxiliary plane. Modern solutions invert full waveforms for "
  "the moment tensor - the mathematical description of the equivalent "
  "force system - which for most earthquakes is a double couple matching "
  "slip on a plane. Beach balls let seismologists read tectonics at a "
  "glance: thrust mechanisms lining a trench, strike-slip along a "
  "transform, normal faulting at a ridge."),
 "how_it_works": (
  "A focal mechanism works through the radiation pattern. Slip on a fault "
  "pushes rock outward in two opposite quadrants (compressional first "
  "motions) and pulls it inward in the other two (dilatational), with the "
  "boundaries being the fault plane and the auxiliary plane "
  "(perpendicular to slip). Plotting dozens of stations' first motions on "
  "a lower-hemisphere projection and finding the two orthogonal nodal "
  "planes that separate up from down gives the mechanism - with the "
  "famous ambiguity: seismology alone cannot say which nodal plane is "
  "the real fault (geology or aftershock lineations break the tie). "
  "Moment-tensor inversion generalizes this: it finds the 3x3 symmetric "
  "tensor whose synthetic seismograms best match the observed waveforms, "
  "yielding strike, dip, rake, and M0 together. The P, T, and B axes of "
  "the mechanism give the principal stress directions - compression and "
  "tension - directly."),
 "key_points": [
  "The beach ball encodes strike, dip, and rake: the fault's geometry and slip direction in one symbol.",
  "P-wave first motions (up = compression, down = dilatation) separated by two nodal planes give the mechanism.",
  "Moment-tensor waveform inversion is the modern method, yielding mechanism plus seismic moment.",
  "One ambiguity remains: the fault plane vs. the auxiliary plane needs geology or aftershocks to resolve.",
  "Mechanism maps read tectonics at a glance: thrust at trenches, strike-slip at transforms, normal at ridges."],
 "requirements": [
  "First-motion polarities from many well-distributed stations, or broadband waveforms for inversion.",
  "A velocity model to compute take-off angles from station to source.",
  "Aftershock or geologic data to identify which nodal plane is the fault."],
 "standards": [
  "Mechanisms reported as strike/dip/rake with the Aki-Richards convention and uncertainty.",
  "Moment tensors decomposed into double-couple, CLVD, and isotropic parts per standard practice."],
 "citations": [CIT_AKI, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: the beach ball reframed as his original fault "
  "portrait - compression white, dilatation dark, every mechanism a "
  "Signature mugshot of the rupture."),
 "demo_kind": "beachball_quadrants",
},
{
 "key": "aftershock-sequences", "name": "Aftershocks, Foreshocks, and Earthquake Swarms",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A large earthquake is rarely alone: it is followed by aftershocks - "
  "smaller earthquakes in the surrounding crust, triggered by the stress "
  "changes the mainshock imposed. Aftershock sequences decay with time "
  "following Omori's law (1894): the rate falls roughly as 1/time, so a "
  "sequence is most dangerous in the first hours and days. The largest "
  "aftershock is typically about one magnitude unit below the mainshock "
  "(Bath's law), and the total count follows the Gutenberg-Richter "
  "distribution. Foreshocks - smaller events preceding the mainshock, as "
  "before the 2011 Tohoku earthquake - are only recognizable in "
  "hindsight. Swarms are different: clusters with no dominant mainshock, "
  "often driven by fluid or magma movement (volcanic swarms) or slow "
  "slip. Operational aftershock forecasting now gives the public daily "
  "probabilities - e.g., the chance of a magnitude 6 aftershock this "
  "week - based on statistical models (ETAS) calibrated on the ongoing "
  "sequence."),
 "how_it_works": (
  "Aftershocks work through static and dynamic stress transfer. The "
  "mainshock's slip permanently redistributes stress: some nearby faults "
  "are loaded closer to failure (positive Coulomb stress change) and "
  "rupture as aftershocks; others are unloaded into stress shadows. "
  "Omori's law, n(t) = K/(c+t)^p, captures the decay, with p near 1; "
  "fitting K, c, p to the first days of data lets forecasters project "
  "the sequence forward. The ETAS (epidemic-type aftershock sequence) "
  "model treats every earthquake as capable of triggering its own "
  "aftershocks, producing the observed clustering and the occasional "
  "large 'aftershock' that rivals the mainshock. Foreshocks likely "
  "reflect a nucleation process - accelerating slip before the main "
  "rupture - but no reliable real-time discriminant separates a "
  "foreshock from an ordinary small earthquake, which is why prediction "
  "remains out of reach."),
 "key_points": [
  "Aftershocks are triggered by the mainshock's stress redistribution; their rate decays per Omori's law (~1/time).",
  "Bath's law: the largest aftershock averages ~1 magnitude unit below the mainshock.",
  "ETAS models treat every quake as a potential trigger, enabling operational aftershock forecasts.",
  "Foreshocks are identifiable only in hindsight - no reliable real-time foreshock discriminant exists.",
  "Swarms (no dominant mainshock) usually signal fluids, magma, or slow slip rather than a mainshock-aftershock process."],
 "requirements": [
  "A complete early catalog of the sequence to fit Omori/ETAS parameters.",
  "Coulomb stress-change modeling to map which faults were loaded vs. shadowed.",
  "Continuous monitoring because the hazard is highest in the first hours to days."],
 "standards": [
  "Omori-Utsu law n(t) = K/(c+t)^p with fitted K, c, p reported for each sequence.",
  "Operational forecasts issued as probabilities over defined magnitude-time windows."],
 "citations": [CIT_OMORI, CIT_GR],
 "sig_lens": (
  "Signature edition: aftershocks reframed as his original stress "
  "echoes - the mainshock's Signature settling through the crust, each "
  "aftershock a ledger entry, decaying on his Omori clock."),
 "demo_kind": "omori_decay",
},
{
 "key": "tsunamis", "name": "Tsunamis: Earthquakes That Move the Ocean",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A tsunami is a series of ocean waves generated when a large shallow "
  "earthquake vertically displaces the seafloor - most often a megathrust "
  "rupture on a subduction interface. Unlike wind waves, tsunamis involve "
  "the entire water column and travel at jetliner speed in the deep "
  "ocean, c = sqrt(g*h): about 800 km/h where the ocean is 4 km deep, "
  "with wavelengths of hundreds of kilometers and open-ocean heights "
  "under a meter - imperceptible to ships. As the wave enters shallow "
  "water it slows, shortens, and grows: shoaling can amplify it tens of "
  "meters high, arriving as a rapid, debris-laden flood rather than a "
  "breaking wave. The 2004 Sumatra (M_w 9.1) and 2011 Tohoku (M_w 9.1) "
  "tsunamis killed hundreds of thousands and showed that the wave train "
  "lasts hours, with later waves often the largest. Tsunami warning "
  "centers combine fast magnitude estimates with deep-ocean pressure "
  "sensors (DART buoys) that detect the wave itself."),
 "how_it_works": (
  "A tsunami works by seafloor displacement. When the overriding plate "
  "of a subduction zone snaps seaward and upward during a megathrust "
  "earthquake, it lifts the water column above the rupture - meters of "
  "uplift over hundreds of kilometers. Gravity restores the surface, "
  "radiating long waves in both directions at the shallow-water speed "
  "sqrt(g*h). In the deep ocean the wave is fast, long, and low; "
  "approaching shore, conservation of energy flux forces amplitude to "
  "grow roughly as h^(-1/4) (Green's law) while the front steepens. "
  "Warning works in two stages: seismic detection gives magnitude and "
  "mechanism within minutes (only shallow undersea thrust events "
  "tsunamigenic), then DART bottom-pressure recorders confirm whether a "
  "wave was actually generated and models forecast coastal amplitudes. "
  "The cruel lesson of 2011: near-field coasts have 10-30 minutes, so "
  "natural warning - strong shaking, unusual sea behavior - must trigger "
  "evacuation without waiting for official alerts."),
 "key_points": [
  "Tsunamis come from vertical seafloor displacement - mainly shallow megathrust earthquakes.",
  "Deep-ocean speed c = sqrt(g*h) (~800 km/h); the wave is fast, long, and low offshore.",
  "Shoaling amplifies the wave tens of meters at the coast; it arrives as a flood, not a surf wave.",
  "Later waves in the hours-long train are often the largest.",
  "Warning = fast seismic magnitude + DART buoy confirmation + forecast models; near-field coasts must self-evacuate on shaking."],
 "requirements": [
  "Rapid earthquake magnitude, location, depth, and mechanism (shallow undersea thrust = suspect).",
  "Deep-ocean DART pressure sensors to confirm wave generation.",
  "Inundation models calibrated to coastal bathymetry for evacuation zones."],
 "standards": [
  "Tsunami travel-time and amplitude forecasts follow validated shallow-water wave models.",
  "Warning messages use standardized threat levels tied to forecast coastal amplitudes."],
 "citations": [CIT_KANAMORI, CIT_STEIN],
 "sig_lens": (
  "Signature edition: tsunamis reframed as his original ocean-displacement "
  "ledger - the seafloor's Signature written across an entire water "
  "column, read by DART buoys."),
 "demo_kind": "tsunami_travel",
},
{
 "key": "seismic-hazard-maps", "name": "Seismic Hazard Maps",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A seismic hazard map answers the question every builder and insurer "
  "asks: how hard is the ground likely to shake here? National maps "
  "(like the USGS National Seismic Hazard Model) show peak ground "
  "acceleration expected with a chosen probability - commonly 2% in 50 "
  "years (the '2,475-year' shaking level used in U.S. building codes). "
  "They are built by combining earthquake source models (mapped faults "
  "with slip rates, plus background seismicity zones), magnitude-"
  "frequency relations, and ground-motion prediction equations, "
  "integrated over all possible earthquakes. The maps are probabilistic, "
  "not predictions: a high-hazard zone is not 'due' for an earthquake, "
  "it simply has a higher long-term rate of strong shaking. They directly "
  "set design forces in building codes, insurance pricing, and "
  "retrofit priorities - the quiet pages where seismology becomes public "
  "safety."),
 "how_it_works": (
  "Hazard mapping works by integration over uncertainty. For each source "
  "(a fault segment with a recurrence model, or a seismicity zone with a "
  "Gutenberg-Richter distribution), the analysis sums over all magnitudes "
  "and distances: the annual rate of each earthquake times the "
  "probability it produces shaking above a threshold at the site (from "
  "ground-motion models with their scatter). Repeating for many "
  "thresholds traces out a hazard curve - annual exceedance probability "
  "versus shaking level - at every point on a grid. The map displays one "
  "slice: e.g., the PGA with 2% probability of exceedance in 50 years. "
  "Logic trees branch over disputed inputs (which fault model? which "
  "ground-motion equation?) with expert weights, so the final map "
  "carries the community's uncertainty, not one author's opinion. Maps "
  "are updated as new faults are mapped and new earthquakes occur."),
 "key_points": [
  "Hazard maps show shaking levels with stated probabilities (e.g., 2% in 50 years) - not predictions of timing.",
  "Built from fault slip rates + seismicity rates + ground-motion models, integrated over all possible quakes.",
  "The output is a hazard curve at each site: annual exceedance probability vs. shaking level.",
  "Logic trees carry scientific uncertainty (competing fault and ground-motion models) into the final map.",
  "Maps set building-code design forces, insurance rates, and retrofit priorities."],
 "requirements": [
  "A fault source model (mapped faults, slip rates, recurrence) plus background seismicity zones.",
  "Calibrated ground-motion prediction equations with uncertainty.",
  "A probabilistic framework (Cornell-McGuire integration) and logic-tree treatment of alternatives."],
 "standards": [
  "National hazard models (e.g., USGS NSHM) document sources, ground-motion models, and logic-tree weights.",
  "Hazard reported as exceedance probabilities over defined exposure times with uncertainties."],
 "citations": [CIT_CORNELL, CIT_USGS_HAZ],
 "sig_lens": (
  "Signature edition: hazard maps reframed as his original shaking "
  "ledger - every fault's long-term account rendered as a Signature "
  "probability, block by block."),
 "demo_kind": "hazard_curve",
},
{
 "key": "earthquake-early-warning", "name": "Earthquake Early Warning",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Earthquake early warning (EEW) exploits a simple physical fact: the "
  "fast, weak P-wave outruns the slow, damaging S and surface waves. A "
  "dense seismic network near the epicenter detects the P-wave, estimates "
  "location and magnitude within seconds, and broadcasts alerts ahead of "
  "the strong shaking - seconds to tens of seconds of warning, more for "
  "distant cities. Japan's system has warned millions since 2007; the "
  "U.S. ShakeAlert system covers the West Coast; Mexico City's system "
  "warns of distant subduction earthquakes with a minute or more of lead "
  "time. Warning is not prediction: the earthquake has already begun, and "
  "there is a blind zone around the epicenter where the S-wave arrives "
  "before any alert can be issued. Even a few seconds lets trains brake, "
  "surgeons pause, elevators stop at floors, and people drop, cover, and "
  "hold on."),
 "how_it_works": (
  "EEW works as a race between waves and data. When P hits the first "
  "stations, algorithms estimate location from the arrival pattern and "
  "magnitude from the first seconds of the P-wave (its amplitude and "
  "dominant period scale with final size - the Allen-Kanamori insight). "
  "The system then predicts shaking intensity at each user location from "
  "the estimated magnitude and distance, and pushes alerts over dedicated "
  "channels in 1-3 seconds. Two architectures compete: point-source "
  "methods (locate, get magnitude, forecast shaking) and wavefield "
  "methods (track the actual observed shaking front across the network, "
  "no source needed). The blind-zone radius is roughly the P-wave speed "
  "times the system latency: with 5 seconds latency, everywhere within "
  "~30 km of the epicenter gets no warning. False and missed alerts are "
  "managed with probabilistic thresholds tuned to user tolerance."),
 "key_points": [
  "EEW uses the P-wave's head start: detect, locate, estimate magnitude, alert before the S-wave arrives.",
  "Seconds to tens of seconds of warning - enough for automated actions and protective behavior, not evacuation.",
  "The blind zone (epicenter area) gets no warning: shaking outruns the alert where latency exceeds S arrival.",
  "Point-source vs. wavefield methods: estimate the quake, or track the shaking front directly.",
  "Warning is not prediction - the rupture has already started when the alert goes out."],
 "requirements": [
  "A dense real-time network near the hazard with low-latency telemetry.",
  "Algorithms for seconds-fast location, magnitude-from-P, and shaking forecast.",
  "An alert distribution channel (cell broadcast, apps, dedicated receivers) faster than the S-wave."],
 "standards": [
  "Alert performance reported as warning time vs. location with false/missed alert rates.",
  "Magnitude estimation from early P-wave follows validated scaling relations (Allen & Kanamori)."],
 "citations": [CIT_ALLEN, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: early warning reframed as his original head-start "
  "protocol - the P-wave as Signature scout, every second of lead time "
  "a Signature life-saving margin."),
 "demo_kind": "eew_blindzone",
},
# ------------------------------------------------------------------ ADVANCED
{
 "key": "seismic-tomography", "name": "Seismic Tomography: Imaging the Earth's Interior",
 "group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Seismic tomography builds three-dimensional images of the Earth's "
  "interior from millions of seismic wave travel times - the CAT scan of "
  "the planet. If waves arrive later than a reference model predicts, "
  "they passed through slower (hotter, weaker, or partially molten) "
  "rock; earlier arrivals mean faster (colder, stronger) rock. Inverting "
  "millions of such delays recorded at global stations yields volumetric "
  "images: subducting slabs as cold blue tongues diving into the mantle, "
  "mantle plumes as hot red columns rising beneath Hawaii and Iceland, "
  "the African and Pacific large low-velocity provinces looming above "
  "the core-mantle boundary. Body-wave tomography uses earthquake travel "
  "times; surface-wave tomography uses dispersion to map the upper "
  "mantle; ambient-noise tomography cross-correlates background hum "
  "between station pairs to image the crust without any earthquake at "
  "all. Resolution is uneven - best where ray paths cross densely - and "
  "honest models publish checkerboard and spike tests proving what they "
  "can actually resolve."),
 "how_it_works": (
  "Tomography works by linearizing the travel-time integral. A travel "
  "time is the integral of slowness (1/velocity) along the ray path; the "
  "difference between observed and predicted times is, to first order, "
  "the integral of the slowness anomaly along the reference ray. "
  "Discretize the Earth into blocks or basis functions and each delay "
  "becomes one linear equation in the block anomalies - millions of "
  "equations, solved by iterative least squares with regularization "
  "(damping and smoothing) to tame the ill-posedness. Ray paths bend "
  "toward fast material (Fermat's principle), so the system is "
  "re-linearized around the updated model a few times. The result is a "
  "3-D velocity model whose anomalies are interpreted thermally and "
  "compositionally: a -2% shear-velocity anomaly at 2,800 km depth is a "
  "candidate plume root; a +2% slab-shaped anomaly is a subducted plate. "
  "Finite-frequency theory (banana-doughnut kernels) replaced ray theory "
  "for the highest-resolution images."),
 "key_points": [
  "Tomography inverts millions of travel-time delays into 3-D velocity images - the CAT scan of the planet.",
  "Slow anomalies = hot/weak/partially molten; fast anomalies = cold/strong - slabs blue, plumes red.",
  "Body-wave, surface-wave, and ambient-noise tomography cover different depth ranges and scales.",
  "The inverse problem is ill-posed: regularization (damping, smoothing) stabilizes the solution.",
  "Resolution tests (checkerboard, spike) are mandatory - a model is only as good as its ray coverage."],
 "requirements": [
  "Millions of accurate travel-time picks (or dispersion curves, or noise correlations) with good ray coverage.",
  "A reference Earth model to linearize around and a regularized inversion solver.",
  "Resolution tests proving which features the data can actually resolve."],
 "standards": [
  "Tomographic models published with data selection, regularization choices, and resolution tests.",
  "Velocity anomalies reported as percent perturbations to a named reference model."],
 "citations": [CIT_AKI, CIT_DZIEWONSKI],
 "sig_lens": (
  "Signature edition: tomography reframed as his original planetary CAT "
  "scan - millions of delays inverted into a Signature cross-section, "
  "slabs and plumes rendered in his velocity colors."),
 "demo_kind": "tomography_2x2",
},
{
 "key": "seismic-reflection", "name": "Seismic Reflection: Imaging the Subsurface",
 "group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Seismic reflection is the workhorse of subsurface imaging - the "
  "technology behind oil and gas exploration, crustal studies, and "
  "offshore wind-farm surveys. A controlled source (vibrator trucks on "
  "land, airguns at sea) sends waves down; each interface between rock "
  "layers of different acoustic impedance reflects part of the energy "
  "back; receivers record the echoes. Because reflection strength depends "
  "on the impedance contrast, the records map layer boundaries, faults, "
  "folds, salt domes, and fluid contacts in exquisite detail - modern 3-D "
  "surveys image reservoirs at tens of meters resolution kilometers deep. "
  "Processing is the art: sorting traces by common midpoint, correcting "
  "for offset (normal moveout), stacking to boost signal, and migrating "
  "to place dipping reflectors in their true positions. The same method "
  "at crustal scale (deep seismic reflection) has imaged ancient "
  "sutures and the Moho beneath continents."),
 "how_it_works": (
  "Reflection works on echoes and geometry. A wave hitting an interface "
  "at normal incidence reflects with coefficient R = (Z2-Z1)/(Z2+Z1), "
  "where Z = density x velocity is acoustic impedance - big contrasts "
  "(shale over gas sand, salt against sediment) make bright reflectors. "
  "Recorded at increasing source-receiver offsets, a horizontal "
  "reflector's arrival follows a hyperbola in time-offset space; the "
  "normal-moveout correction flattens it using the stacking velocity, "
  "then traces are summed (stacked), improving signal-to-noise by the "
  "square root of the fold. Migration then collapses diffractions and "
  "moves dipping events to their true subsurface positions by "
  "back-propagating the wavefield. Amplitude-vs-offset (AVO) analysis "
  "goes further: how reflectivity changes with angle diagnoses pore "
  "fluid - the direct hydrocarbon indicator that transformed "
  "exploration."),
 "key_points": [
  "Reflection images layer boundaries, faults, and reservoirs from controlled-source echoes.",
  "Reflectivity R = (Z2-Z1)/(Z2+Z1): impedance contrasts make reflectors; fluids make bright spots.",
  "CMP sorting + NMO correction + stacking boosts signal by sqrt(fold); migration places events correctly.",
  "3-D surveys resolve reservoirs at tens of meters, kilometers deep - the engine of petroleum exploration.",
  "AVO (amplitude vs. offset) diagnoses pore fluids directly from angle-dependent reflectivity."],
 "requirements": [
  "A controlled repeatable source and dense receiver arrays with accurate geometry.",
  "A processing flow: geometry, filtering, velocity analysis, NMO, stack, migration.",
  "A velocity model to convert reflection times to depths."],
 "standards": [
  "Marine and land acquisition geometries documented per SEG standards; data in SEG-Y format.",
  "Processing flows reported reproducibly from field records to migrated image."],
 "citations": [CIT_LAY, CIT_STD],
 "sig_lens": (
  "Signature edition: reflection reframed as his original subsurface "
  "sonar - every impedance contrast a Signature echo, stacked and "
  "migrated into his true-position image."),
 "demo_kind": "reflection_nmo",
},
{
 "key": "seismic-refraction", "name": "Seismic Refraction and Crustal Structure",
 "group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Seismic refraction maps subsurface layers from waves that dive down, "
  "travel along a fast layer boundary, and return to the surface - the "
  "head wave. Beyond a critical distance, the refracted arrival overtakes "
  "the direct wave, and its travel-time slope gives the lower layer's "
  "velocity while its intercept time gives the upper layer's thickness. "
  "The method built the first quantitative pictures of crustal thickness: "
  "Mohorovicic himself discovered the crust-mantle boundary in 1909 from "
  "refracted arrivals. Modern wide-angle refraction profiles, shot with "
  "explosions or airguns and recorded hundreds of kilometers away, still "
  "provide the definitive crustal velocity models - sedimentary basins, "
  "crystalline crust, and the Moho - that every other method calibrates "
  "against. Its limitation is fundamental: velocity must increase with "
  "depth, so low-velocity zones hide and thin layers go undetected."),
 "how_it_works": (
  "Refraction works through Snell's law at the critical angle. A downgoing "
  "wave hitting a faster layer at the critical angle (sin(ic) = v1/v2) "
  "travels horizontally along the interface, continuously radiating energy "
  "back up - the head wave, arriving with travel time t = x/v2 + "
  "intercept, where the intercept time encodes the overburden thickness "
  "(t_i = 2h*sqrt(1/v1^2 - 1/v2^2) for one layer). Plotting first-arrival "
  "times versus distance gives straight-line segments: each slope is a "
  "layer velocity, each intercept a thickness. Reversed profiles (shots "
  "at both ends) resolve dipping interfaces; the plus-minus and "
  "generalized reciprocal methods handle irregular boundaries. The "
  "hidden-layer problem - a slow layer sandwiched between fast ones "
  "produces no head wave - is why refraction models are always checked "
  "against reflection and gravity data."),
 "key_points": [
  "Refraction uses head waves traveling along fast interfaces; slope gives velocity, intercept gives thickness.",
  "Mohorovicic discovered the crust-mantle boundary (1909) from refracted arrivals - the method named the Moho.",
  "Wide-angle profiles remain the definitive crustal velocity models other methods calibrate against.",
  "Reversed shots resolve dip; plus-minus methods handle irregular interfaces.",
  "Fundamental blind spot: velocity must increase with depth - hidden low-velocity layers are invisible."],
 "requirements": [
  "Long-offset recordings (tens to hundreds of km) to capture refracted first arrivals.",
  "Reversed shot geometry to resolve dipping layers.",
  "First-break picking accurate enough to fit travel-time slopes and intercepts."],
 "standards": [
  "Refraction models report layer velocities, thicknesses, and dip with pick uncertainties.",
  "Crustal models tied to the Moho definition (P-velocity crossing ~7.6-8.6 km/s)."],
 "citations": [CIT_SHEARER, CIT_LAY],
 "sig_lens": (
  "Signature edition: refraction reframed as his original layer "
  "sounder - critical-angle head waves reading his crustal stack, "
  "thickness from intercept, velocity from slope."),
 "demo_kind": "refraction_intercept",
},
{
 "key": "induced-seismicity", "name": "Induced Seismicity: Human-Triggered Earthquakes",
 "group": "Advanced", "ladder_rank": 7, "ladder_tier": "advanced",
 "description": (
  "Induced seismicity is earthquakes caused by human activity - and it "
  "has rewritten seismic hazard in places like Oklahoma, Texas, and the "
  "Netherlands. The dominant mechanism is fluid injection: pumping "
  "wastewater (or CO2, or geothermal fluids) into deep wells raises pore "
  "pressure in the rock, which reduces the effective normal stress "
  "clamping faults shut (effective stress = total stress minus pore "
  "pressure), letting critically stressed faults slip. The 1960s "
  "Denver and Rangely experiments proved the link; Oklahoma's "
  "wastewater-driven surge after 2009 - including the 2016 M5.8 Pawnee "
  "earthquake - proved the scale. Other triggers include reservoir "
  "impoundment (Koyna, India), geothermal stimulation, hydraulic "
  "fracturing (mostly small, occasionally mid-size), and mining. "
  "Management now means traffic-light protocols: monitor, and reduce or "
  "stop injection when seismicity exceeds thresholds."),
 "how_it_works": (
  "Induced seismicity works through the effective-stress principle. "
  "Faults in the crust sit near failure, held by friction proportional "
  "to effective normal stress. Injected fluid diffuses outward from the "
  "well (pressure front expanding roughly as sqrt(4*pi*D*t) for hydraulic "
  "diffusivity D), raising pore pressure p; the fault's strength drops "
  "as (sigma_n - p) falls, and the ambient tectonic shear stress - "
  "unchanged by us - suddenly suffices to rupture it. The earthquakes "
  "are ordinary tectonic earthquakes in every respect (same physics, "
  "same waves); only the trigger is ours. Poroelastic stress changes "
  "extend the influence beyond the pressure front itself. Discrimination "
  "uses space-time correlation with injection, statistical rate changes "
  "against background, and the telltale migration of seismicity tracking "
  "the pressure front - though definitive attribution for single events "
  "remains probabilistic."),
 "key_points": [
  "Fluid injection raises pore pressure, lowers effective normal stress, and unclamps critically stressed faults.",
  "The earthquakes are ordinary tectonic events - same physics and waves; only the trigger is human.",
  "Pressure fronts diffuse as sqrt(4*pi*D*t); seismicity migration tracking the front is diagnostic.",
  "Oklahoma's wastewater surge (2009+) and the M5.8 Pawnee quake proved industrial-scale hazard.",
  "Traffic-light protocols - monitor, throttle, stop injection at thresholds - are the management standard."],
 "requirements": [
  "Injection volume, rate, pressure, and depth records correlated with seismicity in space and time.",
  "A background seismicity baseline to detect rate changes statistically.",
  "Pore-pressure diffusion and poroelastic models linking operations to fault stress."],
 "standards": [
  "Attribution assessed probabilistically (space-time correlation, rate change, migration) per published criteria.",
  "Traffic-light thresholds defined in magnitude and ground-motion terms before operations begin."],
 "citations": [CIT_ELLSWORTH, CIT_SCHOLZ],
 "sig_lens": (
  "Signature edition: induced seismicity reframed as his original "
  "human-trigger ledger - every barrel injected a Signature pressure "
  "entry, every triggered quake accounted to its well."),
 "demo_kind": "pressure_front",
},
{
 "key": "slow-slip-tremor", "name": "Slow Slip Events and Episodic Tremor",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Not all fault slip is seismic. Slow slip events (SSEs) are fault "
  "slips that take days to months instead of seconds - releasing the "
  "energy of a magnitude 6-7 earthquake so gradually that no one feels "
  "it and ordinary seismometers barely notice. Discovered in Cascadia "
  "in 2001 from GPS records (Dragert et al.), SSEs recur every 10-19 "
  "months on the deep subduction interface, downdip of the locked "
  "seismogenic zone. They are accompanied by non-volcanic tremor - "
  "faint, chattering seismic signals - and low-frequency earthquakes, "
  "together called episodic tremor and slip (ETS). Similar slow "
  "phenomena occur in Japan, Mexico, Costa Rica, and New Zealand. SSEs "
  "matter because they load the adjacent locked zone: each event "
  "transfers stress updip toward the part of the fault that CAN rupture "
  "in a megathrust earthquake, modulating the seismic cycle."),
 "how_it_works": (
  "Slow slip works in the frictional transition zone. Between the "
  "shallow locked zone (stick-slip, earthquakes) and the deep zone "
  "(stable sliding, creep) lies a conditionally stable region where "
  "slip is slow and accompanied by tremor. High pore-fluid pressure - "
  "inferred from the tremor's sensitivity to tiny tidal stresses - "
  "keeps effective stress low, letting the fault slide at plate-rate "
  "multiples over weeks. GPS detects SSEs as transient reversals of "
  "the interseismic motion (stations lurch seaward instead of "
  "landward); tremor is detected by enveloping and correlating the "
  "faint chatter across arrays. The moment-duration scaling of SSEs "
  "differs from ordinary earthquakes (moment proportional to duration, "
  "not duration cubed), marking them as a distinct physical regime. "
  "Stress modeling shows each ETS episode nudges the updip locked zone "
  "closer to failure."),
 "key_points": [
  "Slow slip events release M6-7 worth of energy over days to months - unfelt, GPS-detected.",
  "Episodic tremor and slip (ETS): tremor + low-frequency quakes accompany the slow slip.",
  "Found in Cascadia (2001), Japan, Mexico, Costa Rica, New Zealand - a global phenomenon.",
  "Moment scales linearly with duration (not cubed) - a distinct frictional regime, likely fluid-mediated.",
  "SSEs load the adjacent locked zone, modulating the megathrust seismic cycle."],
 "requirements": [
  "Continuous GPS networks sensitive to millimeter transient displacements.",
  "Tremor detection via array envelope correlation of faint long-duration signals.",
  "A frictional model of the transition zone linking slip, fluids, and stress transfer."],
 "standards": [
  "SSEs characterized by moment, duration, location, and recurrence interval with uncertainties.",
  "Tremor catalogs built with documented detection thresholds and location methods."],
 "citations": [CIT_DRAGERT, CIT_SCHOLZ],
 "sig_lens": (
  "Signature edition: slow slip reframed as his original silent-slip "
  "ledger - the fault moving fortunes of energy in slow motion, "
  "tremor as its faint Signature whisper."),
 "demo_kind": "slow_slip_scaling",
},
{
 "key": "source-spectra", "name": "Source Spectra and the Corner Frequency",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "An earthquake's source spectrum - how its radiated energy is "
  "distributed across frequencies - is the fingerprint of the rupture "
  "itself. Keiiti Aki (1967) and James Brune (1970) showed it has a "
  "universal shape: flat at low frequencies at a level proportional to "
  "seismic moment M0, then decaying above a corner frequency fc. The "
  "corner frequency marks the rupture's size: big faults radiate at long "
  "periods (fc ~ 0.01 Hz for great earthquakes), small faults at high "
  "frequencies (fc ~ 10 Hz for microquakes). Because fc scales as "
  "(stress drop / M0)^(1/3), measuring the spectrum yields the "
  "earthquake's stress drop - typically 1-10 MPa, remarkably constant "
  "across magnitudes, one of seismology's deepest regularities "
  "(self-similarity). Spectra also carry directivity (rupture toward a "
  "station boosts high frequencies), attenuation along the path, and "
  "site amplification - disentangling the three is the daily work of "
  "source seismology."),
 "how_it_works": (
  "Source spectra work by dividing out the path. The observed spectrum "
  "is source x path attenuation x site response; correcting for "
  "attenuation (Q) and site terms isolates the source. Brune's model "
  "fits omega-squared decay: displacement amplitude flat below fc, "
  "falling as f^-2 above, with fc = 0.49*beta*(delta_sigma/M0)^(1/3) "
  "for shear velocity beta and stress drop delta_sigma. The low-"
  "frequency level gives M0; fc plus M0 gives stress drop and source "
  "radius (r ~ beta/fc). Self-similarity - constant stress drop over "
  "~17 orders of moment - means big earthquakes are scaled-up small "
  "ones, a profound constraint on rupture physics. Deviations flag "
  "interesting physics: tsunami earthquakes have anomalously low fc "
  "(slow rupture, weak shaking, big tsunami), and high stress-drop "
  "events radiate damaging high-frequency energy."),
 "key_points": [
  "Source spectra are flat below the corner frequency fc (level = M0) and decay as f^-2 above - the Brune/Aki shape.",
  "Corner frequency marks rupture size: ~0.01 Hz for great quakes, ~10 Hz for microquakes.",
  "Stress drop from fc and M0 is typically 1-10 MPa and roughly constant across magnitudes (self-similarity).",
  "Observed spectrum = source x path attenuation x site; isolating the source is the core analysis step.",
  "Anomalous spectra diagnose special events: tsunami earthquakes (slow, low fc) and high stress-drop damagers."],
 "requirements": [
  "Broadband recordings spanning frequencies below and above the expected corner.",
  "Attenuation (Q) and site corrections to isolate the source spectrum.",
  "A spectral model (Brune omega-squared) fit with uncertainty estimates."],
 "standards": [
  "Stress-drop and corner-frequency values reported with the spectral model and corrections used.",
  "Self-similarity assessed over the magnitude range actually sampled."],
 "citations": [CIT_BRUNE, CIT_AKI],
 "sig_lens": (
  "Signature edition: source spectra reframed as his original rupture "
  "fingerprint - flat where moment lives, cornered where size shows, "
  "every spectrum a Signature voiceprint of the fault."),
 "demo_kind": "brune_spectrum",
},
{
 "key": "stress-drop-rupture", "name": "Stress Drop and Rupture Dynamics",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Stress drop - the difference between stress on the fault before and "
  "after the earthquake - is the single number that sets how violently "
  "a rupture radiates. Typical earthquake stress drops are 1-10 MPa, a "
  "few percent of the absolute stress, estimated from spectra via "
  "delta_sigma = (7/16)*M0/r^3 for a circular crack of radius r. Rupture "
  "dynamics studies how the rupture front actually moves: usually at "
  "70-90% of the shear-wave speed, occasionally supershear (faster than "
  "S, producing a Mach cone of intense shaking, as in the 2002 Denali "
  "and 2023 Turkey earthquakes). Dynamic models couple friction laws "
  "(slip-weakening, rate-and-state) with elastodynamics to simulate "
  "rupture nucleation, propagation, arrest, and the resulting ground "
  "motion - the physics behind 'why did it stop there' and 'why was "
  "shaking so strong in that direction.'"),
 "how_it_works": (
  "Rupture dynamics works by solving elastodynamics with friction. The "
  "fault is loaded to near failure; a nucleation patch begins to slip; "
  "if the slipping zone exceeds a critical size, rupture runs away, "
  "propagating as a shear crack. The slip-weakening friction law - "
  "strength drops from static to dynamic over a characteristic slip "
  "distance Dc - controls whether rupture grows or dies; rate-and-state "
  "friction adds healing and time dependence, reproducing the full "
  "seismic cycle in simulations. Rupture speed is set by the energy "
  "balance at the crack tip: near the Rayleigh speed for ordinary "
  "events, supershear when prestress is high and the fault is straight "
  "and smooth. Directivity focuses energy: stations ahead of the "
  "propagating front see compressed, high-amplitude pulses (the "
  "fling-step and forward-directivity pulse that destroyed near-fault "
  "structures in Northridge and Kobe)."),
 "key_points": [
  "Stress drop (typically 1-10 MPa) sets how efficiently a rupture radiates seismic energy.",
  "Ruptures usually run at 70-90% of shear-wave speed; supershear ruptures outrun S and focus a Mach cone.",
  "Slip-weakening and rate-and-state friction laws govern nucleation, growth, and arrest.",
  "Directivity focuses shaking ahead of the rupture front - the near-fault pulse that levels structures.",
  "Dynamic simulations connect friction physics to the ground motion engineers must design for."],
 "requirements": [
  "Kinematic source models (slip distribution, rupture time) from waveform inversion.",
  "A friction law and prestress field for dynamic forward modeling.",
  "Near-fault recordings to calibrate directivity and pulse effects."],
 "standards": [
  "Stress-drop values reported with the crack model and radius estimate used.",
  "Dynamic models validated against observed slip, rupture speed, and ground motion."],
 "citations": [CIT_SCHOLZ, CIT_AKI],
 "sig_lens": (
  "Signature edition: rupture dynamics reframed as his original crack-"
  "tip ledger - stress in, slip out, every supershear Mach cone a "
  "Signature focusing of Earth's fury."),
 "demo_kind": "stress_drop",
},
{
 "key": "ground-motion-prediction", "name": "Ground Motion Prediction Equations",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Ground motion prediction equations (GMPEs) - also called attenuation "
  "relations - are the formulas that turn 'a magnitude 7 at 20 km' into "
  "'expect 0.4 g peak acceleration at this site.' They are empirical "
  "models fit to thousands of strong-motion recordings, predicting "
  "median shaking (PGA, PGV, spectral accelerations) and its scatter as "
  "functions of magnitude, distance, fault style, and site conditions. "
  "Modern GMPEs (the NGA projects: Boore-Atkinson, Campbell-Bozorgnia, "
  "Chiou-Youngs) include hanging-wall effects, directivity, basin depth, "
  "and nonlinear soil response. The scatter matters as much as the "
  "median: ground motion is lognormally distributed with typical "
  "standard deviations of 0.5-0.7 natural-log units, and hazard analysis "
  "integrates over the full distribution. GMPEs are the bridge between "
  "seismology and engineering - every building code's design spectrum "
  "traces back to them."),
 "how_it_works": (
  "GMPEs work by regression on strong-motion data. The functional form "
  "encodes physics: magnitude scaling (shaking grows with M then "
  "saturates for large M at close distance), geometric spreading and "
  "anelastic attenuation with distance (1/R terms plus exponential "
  "decay), style-of-faulting factors (reverse faults shake ~20-30% "
  "harder), hanging-wall/footwall terms, and site terms (Vs30 - the "
  "average shear velocity of the top 30 m - and basin depth). Coefficients "
  "are fit to recordings from many earthquakes; the residual scatter "
  "(sigma) is split into between-event and within-event components. "
  "Hazard analysis evaluates the GMPE's full lognormal distribution, not "
  "just its median, because rare high-shaking tails drive the hazard at "
  "long return periods. Region-specific GMPEs (Japan, Italy, New "
  "Zealand) capture local attenuation and are selected through logic "
  "trees."),
 "key_points": [
  "GMPEs convert magnitude + distance + fault style + site into expected shaking (PGA, spectra).",
  "Functional forms encode physics: magnitude saturation, geometric spreading, anelastic attenuation, site response.",
  "Modern NGA models add hanging-wall, directivity, basin, and nonlinear soil terms.",
  "Scatter is lognormal with sigma ~0.5-0.7; hazard integrates the full distribution, not just the median.",
  "GMPEs are the bridge from seismology to engineering - design spectra trace back to them."],
 "requirements": [
  "A large strong-motion dataset spanning magnitudes, distances, and site conditions.",
  "Source, path, and site metadata (magnitude, distance metrics, Vs30) for every record.",
  "Regression with mixed effects to separate between-event and within-event scatter."],
 "standards": [
  "GMPEs published with functional form, coefficients, applicable ranges, and sigma decomposition.",
  "Model selection for hazard studies documented via logic trees with weights."],
 "citations": [CIT_BOORE, CIT_CORNELL],
 "sig_lens": (
  "Signature edition: GMPEs reframed as his original shaking forecast "
  "ledger - magnitude in, distance out, every decibel of scatter "
  "accounted in his Signature distribution."),
 "demo_kind": "gmpe_pga",
},
{
 "key": "site-response-microzonation", "name": "Site Response and Seismic Microzonation",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Two buildings at the same distance from the same earthquake can "
  "experience wildly different shaking - because local geology rules. "
  "Soft soils amplify seismic waves: a layer of mud over bedrock traps "
  "energy, resonating like a drumhead at its fundamental frequency "
  "f0 = Vs/4H (shear velocity over four times thickness). Mexico City, "
  "built on an ancient lakebed, suffered catastrophic amplification in "
  "1985 from a quake 350 km away; San Francisco's Marina District, on "
  "bay mud and fill, was devastated in 1989 while bedrock sites nearby "
  "fared far better. Seismic microzonation maps this block by block: "
  "geotechnical surveys, Vs30 measurements, and ambient-noise "
  "H/V spectral ratios delineate zones of amplification, liquefaction "
  "susceptibility (saturated sands that flow like liquid), and landslide "
  "potential. Microzonation turns a regional hazard map into street-"
  "level guidance for land use, retrofits, and emergency planning."),
 "how_it_works": (
  "Site response works through impedance contrast and resonance. Waves "
  "entering a soft surface layer from hard bedrock slow down and grow "
  "in amplitude to conserve energy flux; multiples trapped in the layer "
  "interfere constructively at the quarter-wavelength resonance "
  "f0 = Vs/4H, amplifying shaking several-fold at that frequency - "
  "devastating when it matches a building's natural period (soil-"
  "structure resonance). Nonlinearity complicates strong shaking: soft "
  "soils can de-amplify very strong motion through hysteretic damping "
  "even as they amplify weak motion. Liquefaction is a separate failure: "
  "cyclic shear raises pore pressure in saturated loose sands until "
  "effective stress vanishes and the ground flows, toppling buildings "
  "and floating buried tanks. Microzonation combines 1-D response "
  "analysis, H/V measurements (the horizontal-to-vertical spectral "
  "ratio peaks at f0), and liquefaction triggering curves into zoned "
  "maps with design implications per zone."),
 "key_points": [
  "Local geology controls shaking: soft soils amplify, bedrock does not - same quake, different damage.",
  "A soft layer resonates at f0 = Vs/4H; matching a building's period causes soil-structure resonance.",
  "Mexico City (1985) and the Marina District (1989) are textbook amplification disasters.",
  "Liquefaction: saturated loose sands lose all strength under cyclic loading and flow.",
  "Microzonation maps amplification, liquefaction, and landslide zones block by block for planning and retrofit."],
 "requirements": [
  "Shear-wave velocity profiles (Vs30, boreholes) and layer thicknesses across the urban area.",
  "H/V ambient-noise measurements to map resonance frequency cheaply and densely.",
  "Geotechnical data (SPT, CPT, groundwater) for liquefaction susceptibility."],
 "standards": [
  "Site classification follows Vs30-based schemes (e.g., NEHRP classes A-E) with measured, not assumed, values.",
  "Microzonation maps document methods, uncertainties, and per-zone design implications."],
 "citations": [CIT_STEIN, CIT_BOORE],
 "sig_lens": (
  "Signature edition: site response reframed as his original ground-"
  "filter ledger - every soil column a Signature resonator, every "
  "block zoned by how it will dance."),
 "demo_kind": "site_resonance",
},
{
 "key": "paleoseismology", "name": "Paleoseismology: Reading Ancient Earthquakes",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Paleoseismology extends the earthquake record thousands of years "
  "before seismometers existed by reading the geologic diary faults "
  "leave behind. The flagship method is trenching: excavating across a "
  "fault to expose offset sediment layers, each past surface rupture "
  "visible as a displaced horizon or a wedge of fault scarp colluvium. "
  "Radiocarbon dating of the offset layers brackets each event in time - "
  "Kerry Sieh's Pallett Creek trenches on the San Andreas revealed a "
  "dozen great earthquakes over 1,400 years with irregular intervals, "
  " demolishing the idea of clockwork recurrence. Offshore, turbidite "
  "paleoseismology reads submarine landslide deposits triggered by "
  "great subduction earthquakes (Cascadia's 10,000-year record); coastal "
  "subsidence and tsunami deposits extend the record further. "
  "Paleoseismology supplies what instrumental catalogs cannot: the long-"
  "term rate, the variability, and the maximum size of a fault's "
  "earthquakes."),
 "how_it_works": (
  "Paleoseismology works by event stratigraphy. A surface-rupturing "
  "earthquake displaces the ground surface; subsequent sedimentation "
  "buries the scarp, preserving a colluvial wedge and an offset "
  "horizon. In a trench wall, the geologist logs every unit, traces "
  "each fault strand, and identifies event horizons - the buried "
  "ground surfaces at the time of each quake. Organic material just "
  "above and below an event horizon is radiocarbon dated, bracketing "
  "the event's age; multiple trenches along the fault correlate events "
  "and measure slip per event from offset piercing points. The dated "
  "event sequence yields recurrence intervals, their mean and "
  "variability (aperiodicity), and slip per event - the direct inputs "
  "to fault-based hazard models. Completeness is the eternal caveat: "
  "erosion and non-deposition erase events, so paleoseismic rates are "
  "minimum rates."),
 "key_points": [
  "Trenching across faults exposes past surface ruptures as offset layers and colluvial wedges.",
  "Radiocarbon dating brackets each prehistoric event; Pallett Creek revealed irregular San Andreas recurrence.",
  "Turbidites and tsunami deposits extend subduction-zone records thousands of years offshore.",
  "Outputs - recurrence intervals, variability, slip per event - feed directly into hazard models.",
  "The record is incomplete by nature: erosion erases events, so rates are minimum estimates."],
 "requirements": [
  "An active fault with datable Quaternary sediments and a trenchable site.",
  "Detailed trench logging plus radiocarbon (or luminescence) dating above and below each event horizon.",
  "Multiple trenches along strike to correlate events and measure per-event slip."],
 "standards": [
  "Event ages reported as calibrated probability distributions, not single dates.",
  "Recurrence statistics include aperiodicity (COV) and completeness discussion."],
 "citations": [CIT_SIEH, CIT_SCHWARTZ],
 "sig_lens": (
  "Signature edition: paleoseismology reframed as his original deep-"
  "time diary - every trench wall a Signature page, every offset "
  "horizon an ancient entry, radiocarbon his page numbers."),
 "demo_kind": "paleo_recurrence",
},
{
 "key": "recurrence-seismic-gaps", "name": "Earthquake Recurrence and Seismic Gaps",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "The seismic gap hypothesis - that the quietest segments of an active "
  "plate boundary are the most dangerous - has driven earthquake "
  "forecasting for decades. It rests on the seismic cycle: a fault "
  "segment accumulates slip deficit at the plate rate since its last "
  "rupture, and when the deficit equals the slip of a characteristic "
  "earthquake, it is 'due.' McCann's 1979 circum-Pacific gap map "
  "famously highlighted segments that later ruptured (Michoacan 1985) - "
  "and segments that stubbornly did not. The modern view is "
  "probabilistic: slip deficit gives a long-term rate, but recurrence "
  "is irregular (paleoseismology proves it), and stress shadows from "
  "neighboring ruptures modulate the clock. The characteristic-"
  "earthquake model (Schwartz and Coppersmith, 1984) - faults rupture "
  "repeatedly in similar-size events - remains the workhorse for "
  "fault-based hazard, now blended with Gutenberg-Richter statistics in "
  "models like UCERF."),
 "how_it_works": (
  "Recurrence analysis works by balancing a slip budget. Geodesy or "
  "plate rates give the loading rate (mm/yr); paleoseismology or "
  "historic records give the date and slip of the last event; the "
  "product is the accumulated slip deficit - how much motion the fault "
  "'owes.' Dividing characteristic slip per event by the loading rate "
  "gives the mean recurrence interval; renewal models (Brownian passage "
  "time, lognormal) then convert elapsed time into a conditional "
  "probability that rises as the deficit grows. Coulomb stress modeling "
  "adjusts the clock: a neighboring earthquake can advance or delay the "
  "next event by years to decades. The gap concept survives as a "
  "prior - long-quiet segments carry large deficits - but forecasts are "
  "issued as probabilities with wide uncertainties, never dates."),
 "key_points": [
  "Slip deficit = loading rate x time since last event: the fault's accumulated debt.",
  "The seismic gap idea: long-quiet segments hold the largest deficits and the highest long-term rates.",
  "Recurrence is irregular - paleoseismology shows clockwork is the exception, not the rule.",
  "Renewal models convert elapsed time + deficit into conditional probability, not a date.",
  "Neighboring earthquakes advance or delay the clock via Coulomb stress changes."],
 "requirements": [
  "Fault loading rate (geodesy/plate motion) and last-event date and slip.",
  "A recurrence model (characteristic or Gutenberg-Richter) with variability.",
  "Stress-change calculations from neighboring events to adjust timing."],
 "standards": [
  "Forecasts reported as probabilities over defined windows with the renewal model stated.",
  "Slip budgets published with loading-rate and last-event uncertainties."],
 "citations": [CIT_SCHWARTZ, CIT_SIEH],
 "sig_lens": (
  "Signature edition: recurrence reframed as his original fault-debt "
  "ledger - loading rate as income, last rupture as payment, the "
  "deficit a Signature balance coming due."),
 "demo_kind": "slip_deficit",
},
{
 "key": "probabilistic-hazard", "name": "Probabilistic Seismic Hazard Analysis",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Probabilistic seismic hazard analysis (PSHA), founded by C. Allin "
  "Cornell (1968), is the rigorous machinery behind every hazard map: "
  "it integrates over everything uncertain - where earthquakes occur, "
  "how big, how often, and how hard they shake - to yield the annual "
  "probability of exceeding any shaking level. The ingredients: source "
  "models (faults with recurrence, area sources with Gutenberg-Richter "
  "rates), ground-motion models with their scatter, and the Cornell-"
  "McGuire integral summing rate x probability over all magnitudes and "
  "distances. Logic trees carry competing scientific interpretations "
  "with weights. The output hazard curve lets engineers pick design "
  "levels by risk tolerance: a hospital designs to rarer, stronger "
  "shaking than a warehouse. PSHA's critics note its sensitivity to "
  "rare-event tails and model choices; its defenders note that every "
  "alternative smuggles the same uncertainties in with less honesty. "
  "The 2023 USGS National Seismic Hazard Model is PSHA at continental "
  "scale."),
 "how_it_works": (
  "PSHA works by total-probability integration. For one source, the "
  "annual rate of exceeding shaking level z is the integral over "
  "magnitude and distance of [earthquake rate] x [P(shaking > z | m, r)] "
  "- the second term coming from the GMPE's lognormal distribution. "
  "Summing over all sources gives the site's hazard curve; inverting "
  "it gives the shaking for any return period (e.g., 2,475 years for "
  "2% in 50 years). Disaggregation then asks: which magnitude-distance "
  "pairs dominate the hazard at that level? - guiding the choice of "
  "scenario earthquakes for design. Epistemic uncertainty (which model "
  "is right) rides in logic-tree branches; aleatory variability (nature's "
  "randomness) rides inside the integral. The mean hazard curve, "
  "weighted over branches, is the decision number - with fractiles "
  "showing the spread of expert disagreement."),
 "key_points": [
  "PSHA integrates over all uncertainties - locations, sizes, rates, shaking - into exceedance probabilities.",
  "The Cornell-McGuire integral: sum over sources of rate x P(shaking > z | magnitude, distance).",
  "Hazard curves invert to design levels: pick shaking by risk tolerance (hospital vs. warehouse).",
  "Disaggregation identifies the magnitude-distance scenarios dominating the hazard.",
  "Logic trees carry competing models with weights; mean hazard plus fractiles show the spread."],
 "requirements": [
  "Complete source models (faults + background seismicity) with recurrence rates.",
  "GMPEs with full distributions (median + sigma), not just medians.",
  "Logic-tree weights for alternative interpretations, elicited transparently."],
 "standards": [
  "PSHA studies document sources, GMPEs, logic trees, and disaggregation per SSHAC guidelines for critical facilities.",
  "Results reported as hazard curves with mean and fractiles, never a single number."],
 "citations": [CIT_CORNELL, CIT_USGS_HAZ],
 "sig_lens": (
  "Signature edition: PSHA reframed as his original total-risk "
  "integral - every source, every magnitude, every distance folded "
  "into one Signature exceedance curve."),
 "demo_kind": "psha_integral",
},
{
 "key": "seismic-anisotropy", "name": "Seismic Anisotropy",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Seismic anisotropy - wave speed depending on direction - is the "
  "seismologist's window into deformation and flow inside the Earth. "
  "Its workhorse observation is shear-wave splitting: an S-wave "
  "entering anisotropic rock splits into fast and slow polarizations, "
  "arriving separated by a delay time dt (typically ~1 s for upper-"
  "mantle paths) with the fast direction phi recording the fabric's "
  "orientation. In the upper mantle, olivine crystals align with flow, "
  "so splitting maps mantle convection and plate-motion shear beneath "
  "continents. In the crust, aligned cracks make the fast direction "
  "track the maximum horizontal stress - a stress meter readable from "
  "seismograms, used to watch stress evolve around volcanoes and "
  "reservoirs. Anisotropy also explains puzzles like the inner core's "
  "directional wave speeds and helps correct isotropic models that "
  "would otherwise mislocate earthquakes."),
 "how_it_works": (
  "Anisotropy works through mineral and crack alignment. Olivine, the "
  "upper mantle's dominant mineral, is intrinsically anisotropic (fast "
  "along its a-axis); mantle shear aligns the a-axes, making the "
  "aggregate fast in the flow direction. A vertically traveling SKS "
  "phase (converted at the core-mantle boundary to a clean radial SV) "
  "splits on the receiver side; grid-searching over (phi, dt) for the "
  "pair that best removes the transverse-component energy yields the "
  "splitting parameters. In the crust, extensive-dilatancy anisotropy "
  "(EDA): fluid-filled microcracks aligned by the stress field make "
  "shear waves fast parallel to maximum compression - so temporal "
  "changes in splitting at a volcano or injection site track stress "
  "and fluid-pressure evolution. Full-waveform anisotropic tomography "
  "now maps 3-D fabric, not just path-averaged splitting."),
 "key_points": [
  "Anisotropy = direction-dependent wave speed, revealing deformation fabric and flow.",
  "Shear-wave splitting (fast direction phi, delay dt) is the flagship measurement, ~1 s in the upper mantle.",
  "Mantle splitting maps convection and plate shear via aligned olivine; crustal splitting tracks stress via aligned cracks.",
  "Temporal splitting changes monitor stress and fluids at volcanoes and reservoirs.",
  "The inner core is anisotropic too - a clue to its crystallization and dynamics."],
 "requirements": [
  "Three-component recordings of core phases (SKS) or local shear waves with clear polarizations.",
  "A splitting measurement method (e.g., transverse-energy minimization) with error estimates.",
  "Geodynamic context to interpret fast directions as flow, stress, or frozen fabric."],
 "standards": [
  "Splitting reported as (phi, dt) with 95% confidence regions from the measurement grid search.",
  "Null measurements (no splitting) reported - they constrain isotropy or vertical fabric."],
 "citations": [CIT_AKI, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: anisotropy reframed as his original flow "
  "compass - split shear waves pointing along the mantle's Signature "
  "currents, cracks aligned to his stress field."),
 "demo_kind": "splitting_delay",
},
{
 "key": "receiver-functions", "name": "Receiver Functions: The Moho in a Waveform",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A receiver function isolates the Earth's local structure beneath a "
  "single station from a distant earthquake's recording - famously, "
  "it reads the Moho (crust-mantle boundary) depth from one waveform. "
  "The trick, introduced by Langston (1979): deconvolve the vertical "
  "component (dominated by the direct P-wave, the 'source wavelet') "
  "from the radial component, leaving only the P-to-S conversions "
  "generated at interfaces beneath the station. The standout is the "
  "Ps phase - P converting to S at the Moho - arriving a few seconds "
  "after P; its delay time maps directly to crustal thickness "
  "(~5 s delay ~ 40 km crust). Stacking receiver functions from many "
  "earthquakes at many back-azimuths builds images of the Moho, "
  "mid-crustal discontinuities, the lithosphere-asthenosphere "
  "boundary, and even the 410/660-km mantle transitions - a one-"
  "station deep-Earth probe."),
 "how_it_works": (
  "Receiver functions work by source equalization. A teleseismic P "
  "wave arrives from below at near-vertical incidence; the vertical "
  "record approximates the source wavelet convolved with the "
  "instrument, while the radial record adds the local converted "
  "phases (Ps at each interface, plus reverberations like PpPs). "
  "Deconvolving vertical from radial - usually in the frequency "
  "domain with a water-level or iterative time-domain stabilization - "
  "cancels the source and instrument, leaving the receiver-side "
  "structure's impulse response. The Ps delay, dt = H*(sqrt(1/Vs^2 - "
  "p^2) - sqrt(1/Vp^2 - p^2)) for ray parameter p, inverts to Moho "
  "depth H given Vp/Vs; the classic H-kappa stacking grid-searches "
  "depth and Vp/Vs jointly using Ps and its multiples. Moveout "
  "correction and common-conversion-point stacking turn single-"
  "station functions into 2-D/3-D interface images."),
 "key_points": [
  "Receiver functions deconvolve the source wavelet out, isolating structure beneath one station.",
  "The Ps conversion's delay maps directly to Moho depth (~5 s delay ~ 40 km crust).",
  "H-kappa stacking jointly solves for crustal thickness and Vp/Vs ratio.",
  "Stacks image the Moho, mid-crustal layers, the LAB, and mantle transition-zone discontinuities.",
  "One distant earthquake per station is enough - the cheapest deep-Earth probe in seismology."],
 "requirements": [
  "Teleseismic P recordings (M5.5+, 30-90 degrees distance) on three components.",
  "Stable deconvolution (water-level or iterative) to equalize the source.",
  "Multiple events at varied back-azimuths to stack and check azimuthal variation."],
 "standards": [
  "Receiver functions published with deconvolution parameters and frequency band.",
  "H-kappa results reported with uncertainties on H and kappa."],
 "citations": [CIT_LANGSTON, CIT_SHEARER],
 "sig_lens": (
  "Signature edition: receiver functions reframed as his original "
  "one-station probe - deconvolve the source, keep the Signature "
  "conversions, read the Moho in seconds."),
 "demo_kind": "receiver_ps",
},
{
 "key": "seismic-interferometry", "name": "Seismic Interferometry: Turning Noise into Signal",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Seismic interferometry performs the field's most elegant trick: it "
  "turns background noise into signal. Cross-correlating months of "
  "ambient seismic noise (ocean microseisms, traffic, wind) recorded at "
  "two stations yields the Green's function between them - the "
  "seismogram as if one station were the source and the other the "
  "receiver - with surface waves emerging from the random hum. "
  "Demonstrated by Shapiro, Campillo, and others in the early 2000s, "
  "the method freed seismology from waiting for earthquakes: any pair "
  "of stations gives a path measurement, enabling ambient-noise "
  "tomography of the crust at unprecedented density - thousands of "
  "paths from a temporary array, imaging volcanoes, fault zones, and "
  "basins. Time-lapse interferometry goes further: tiny velocity "
  "changes (0.1%) from the same station pair track stress, fluid "
  "pressure, and damage evolution through earthquake cycles and "
  "volcanic unrest."),
 "how_it_works": (
  "Interferometry works through Green's function retrieval. For a "
  "diffuse wavefield, the cross-correlation of noise at stations A and "
  "B, stacked over long times, converges to the Green's function "
  "between them (plus its time-reverse) - the waves that would travel "
  "from A to B. In practice: whiten spectra, cross-correlate daily "
  "windows, stack months, and pick the emerging Rayleigh-wave arrival; "
  "its dispersion feeds standard surface-wave tomography with path "
  "coverage no earthquake catalog can match. Coda-wave interferometry "
  "exploits multiply scattered waves' extreme path sensitivity: a 0.01% "
  "velocity change shifts the late coda measurably, letting "
  "volcano observatories and fault-zone experiments watch rigidity "
  "evolve day by day. The method assumes a sufficiently isotropic noise "
  "field - corrected by directional balancing when oceans dominate one "
  "azimuth."),
 "key_points": [
  "Cross-correlating ambient noise between two stations retrieves the Green's function between them.",
  "Surface waves emerge from the hum - no earthquake needed - enabling dense ambient-noise tomography.",
  "Thousands of station-pair paths image volcanoes, fault zones, and basins at high resolution.",
  "Coda-wave interferometry detects 0.01-0.1% velocity changes: stress, fluids, and damage tracked daily.",
  "Noise-source anisotropy must be corrected so directional oceans don't bias the measurements."],
 "requirements": [
  "Continuous recordings (weeks to months) at station pairs with overlapping time.",
  "Noise preprocessing: spectral whitening, temporal normalization, directional balancing.",
  "Dispersion picking and tomography codes adapted to noise-derived Green's functions."],
 "standards": [
  "Noise correlations published with processing parameters and signal-to-noise criteria.",
  "Velocity-change measurements reported with uncertainties and noise-source stability checks."],
 "citations": [CIT_SHEARER, CIT_AKI],
 "sig_lens": (
  "Signature edition: interferometry reframed as his original noise-"
  "to-signal alchemy - the ocean's hum cross-correlated into a "
  "Signature Green's function, no earthquake required."),
 "demo_kind": "noise_correlation",
},
{
 "key": "deep-earth-structure", "name": "Deep Earth Structure: Core, Mantle, and Discontinuities",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Seismology mapped the deep Earth without a single direct sample: a "
  "crust kilometers thick, a 2,900-km rocky mantle, a liquid iron outer "
  "core, and a solid iron inner core - all read from waves. Oldham "
  "(1906) found the core from S-waves' refusal to cross it and P-waves' "
  "shadow zone; Lehmann (1936) found the inner core from faint P' "
  "reflections; the Mohorovicic discontinuity (1909), the 410-km and "
  "660-km mantle transitions (olivine phase changes), and the "
  "core-mantle boundary (the D'' region, with ultra-low-velocity zones) "
  "were each decoded from travel-time kinks and reflections. The "
  "Preliminary Reference Earth Model (PREM, Dziewonski and Anderson, "
  "1981) distilled a century of such data into the standard 1-D Earth. "
  "Modern work targets the frontiers: inner-core anisotropy and "
  "rotation, light elements in the core, deep mantle plumes, and the "
  "enigmatic large low-velocity provinces - continent-sized structures "
  "at the core-mantle boundary that may anchor hotspot volcanism."),
 "how_it_works": (
  "Deep-Earth seismology works by ray geometry through a spherical "
  "planet. Each discontinuity imprints the travel-time curve: velocity "
  "jumps create triplications (three arrivals), strong contrasts spawn "
  "reflections (PP, SS, PcP off the core-mantle boundary, PKiKP off the "
  "inner core), and the liquid outer core casts the P-wave shadow zone "
  "(no direct P between ~103 and 143 degrees) while stopping S entirely. "
  "Normal modes - the whole Earth's free oscillations after great "
  "earthquakes, with periods up to 54 minutes - constrain density and "
  "elastic structure independently of travel times; splitting of mode "
  "peaks measures rotation and 3-D structure. Joint inversion of body-"
  "wave times, surface-wave dispersion, and normal-mode frequencies "
  "produced PREM; today's models add anisotropy, attenuation, and 3-D "
  "heterogeneity to resolve plumes, slabs, and the core's fine "
  "structure."),
 "key_points": [
  "All deep-Earth knowledge - core, mantle, discontinuities - was read from seismic waves, not samples.",
  "Oldham (1906) found the liquid outer core; Lehmann (1936) the solid inner core; Mohorovicic (1909) the Moho.",
  "Shadow zones, triplications, and core reflections (PcP, PKiKP) are the geometric fingerprints of layering.",
  "Normal modes (whole-Earth ringing, up to 54-min periods) constrain density independently of travel times.",
  "PREM (1981) is the 1-D standard; frontiers include inner-core anisotropy, LLVPs, and deep plumes."],
 "requirements": [
  "Global travel-time datasets spanning all epicentral distances, including core phases.",
  "Normal-mode frequency catalogs from great earthquakes.",
  "A 1-D reference inversion framework (like PREM's) before attempting 3-D structure."],
 "standards": [
  "Deep-Earth models referenced to PREM/ak135 with anomalies reported as perturbations.",
  "Phase identifications follow IASPEI conventions for core and surface-reflected phases."],
 "citations": [CIT_OLDHAM, CIT_LEHMANN, CIT_DZIEWONSKI],
 "sig_lens": (
  "Signature edition: the deep Earth reframed as his original layered "
  "ledger - crust, mantle, liquid outer core, solid inner core, every "
  "discontinuity a Signature boundary read from shadow zones."),
 "demo_kind": "shadow_zone",
},
{
 "key": "earthquake-forecasting", "name": "Earthquake Forecasting: Probability, Not Prediction",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Earthquake prediction - a specific time, place, and magnitude, "
  "reliably and in advance - has never been achieved, and the "
  "scientific consensus is that the Earth's crust does not broadcast "
  "reliable short-term precursors. What seismology CAN do is forecast: "
  "assign probabilities. The Gutenberg-Richter law (log N = a - bM, "
  "with b near 1) says each magnitude unit is ~10x rarer than the last, "
  "converting long-term rates into probabilities for any window. "
  "Operational earthquake forecasting (as in Italy and New Zealand) "
  "issues regularly updated probabilities from clustering models "
  "(ETAS): after a magnitude 6, the chance of a larger event in the "
  "coming week is small but tens of thousands of times the background "
  "rate - actionable for emergency managers. The honest framing, "
  "endorsed after L'Aquila: forecasts quantify what we know and what "
  "we don't, and 'low probability' never means 'no earthquake.'"),
 "how_it_works": (
  "Forecasting works through statistical seismology. The long-term "
  "forecast starts from the seismicity rate: fit a and b of the "
  "Gutenberg-Richter relation to the regional catalog (above the "
  "completeness magnitude), and the annual rate of M>=m events is "
  "10^(a-b*m); Poisson statistics convert rates to probabilities for "
  "any exposure time. Short-term forecasts multiply the background by "
  "clustering models: ETAS computes how each recent earthquake "
  "elevates the rate nearby, decaying with Omori's law in time and "
  "diffusing in space. The Collaboratory for the Study of Earthquake "
  "Predictability (CSEP) prospectively tests competing models against "
  "future earthquakes - the only honest scoreboard, since retrospective "
  "'predictions' are meaningless. Communicating forecasts means "
  "reporting probabilities with uncertainties and the actions each "
  "probability level warrants."),
 "key_points": [
  "Reliable short-term prediction (time, place, magnitude) has never been achieved; precursors are not dependable.",
  "Forecasting assigns probabilities: Gutenberg-Richter rates for the long term, ETAS clustering for the short term.",
  "After a large quake, the chance of an even larger one is small but vastly above background - operationally useful.",
  "CSEP prospectively tests models against future earthquakes - the only honest scoreboard.",
  "Communication rule: 'low probability' never means 'no earthquake'; every forecast carries its uncertainty."],
 "requirements": [
  "A complete earthquake catalog above the magnitude of completeness for rate fitting.",
  "Clustering models (ETAS) calibrated to the region for short-term updates.",
  "Prospective testing infrastructure (CSEP-style) to score models honestly."],
 "standards": [
  "Forecasts issued as probabilities over explicit magnitude-space-time windows with uncertainties.",
  "Model skill demonstrated prospectively, not retrospectively."],
 "citations": [CIT_GR, CIT_OMORI],
 "sig_lens": (
  "Signature edition: forecasting reframed as his original honest-"
  "odds ledger - no false predictions, only Signature probabilities "
  "with the uncertainty printed alongside."),
 "demo_kind": "gutenberg_richter",
},
{
 "key": "seismic-building-codes", "name": "Seismic Building Codes and Resilient Design",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Seismic building codes are where seismology saves lives at scale: "
  "they translate hazard science into the forces every structure must "
  "withstand. The chain runs from PSHA hazard maps to design spectra "
  "(the shaking a building of each natural period must resist), to "
  "code provisions: ductile detailing (reinforcement that bends "
  "without breaking), capacity design (beams yield before columns), "
  "base isolation (bearings that decouple the building from the "
  "ground), and damping systems. Performance-based design goes "
  "further, targeting explicit outcomes - immediate occupancy for "
  "hospitals, collapse prevention for offices - under specified "
  "shaking levels. The record is clear: where modern codes are "
  "enforced (Chile 2010, Japan 2011), even magnitude 8-9 earthquakes "
  "kill orders of magnitude fewer people than similar events where "
  "codes are absent or ignored (Haiti 2010). Retrofit of older "
  "buildings - unreinforced masonry, soft-story wood frames, "
  "non-ductile concrete - is the great unfinished task."),
 "how_it_works": (
  "Seismic design works by controlled damage. A building is modeled as "
  "oscillators with natural periods; the design spectrum gives the "
  "required strength at each period, reduced by a response-modification "
  "factor R that accounts for ductility - the code deliberately designs "
  "below elastic forces, counting on the structure to deform "
  "inelastically without collapsing. Base shear V = Cs * W anchors the "
  "calculation: seismic response coefficient times building weight, "
  "distributed over floors by height and mass. Ductile detailing rules "
  "(closely spaced stirrups, continuous reinforcement, strong-column/ "
  "weak-beam) ensure the yielding happens where intended. Base "
  "isolation inserts flexible bearings (lead-rubber, friction "
  "pendulum) that lengthen the period out of the damaging range; "
  "dampers bleed off energy. Retrofit applies the same principles to "
  "existing buildings: add shear walls, jacket columns, brace soft "
  "stories."),
 "key_points": [
  "Codes translate hazard maps into design forces - the pipeline from seismology to safe buildings.",
  "Design uses reduced elastic forces plus ductility: structures are meant to bend, not break (collapse prevention).",
  "Base shear V = Cs * W, distributed by height and mass; detailing rules control WHERE yielding happens.",
  "Base isolation and damping shift or bleed energy - the high-performance options for critical facilities.",
  "Enforcement is everything: Chile/Japan 2010-11 vs. Haiti 2010 proves codes save lives when actually built."],
 "requirements": [
  "A code-level hazard map giving design spectral accelerations for the site.",
  "Structural analysis per the governing code (e.g., ASCE 7, Eurocode 8) with ductile detailing.",
  "Inspection and enforcement so the built structure matches the designed one; retrofit programs for older stock."],
 "standards": [
  "Design follows the governing seismic code's load combinations, R factors, and detailing chapters.",
  "Performance objectives (operational, life safety, collapse prevention) stated per shaking level."],
 "citations": [CIT_USGS_HAZ, CIT_CORNELL],
 "sig_lens": (
  "Signature edition: building codes reframed as his original life-"
  "safety contract - hazard science forged into Signature steel and "
  "concrete, every building a promise kept."),
 "demo_kind": "base_shear",
},
]

assert len(ENTRIES) == 36, "need 36 seismology entries, have %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries must be in ladder order"
tiers = [e["ladder_tier"] for e in ENTRIES]
assert tiers == sorted(tiers, key=lambda t: {"foundations": 0, "compounded": 1, "advanced": 2}[t]), "tiers must be ladder-ordered"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier", "description",
              "how_it_works", "key_points", "requirements", "standards",
              "citations", "sig_lens", "demo_kind"):
        assert k in e, "missing %s in %s" % (k, e.get("key"))
    assert len(e["description"]) > 200, "stub description in %s" % e["key"]
