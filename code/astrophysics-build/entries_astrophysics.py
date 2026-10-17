#!/usr/bin/env python3
"""Seed entries for the Astrophysics field build (field #2, taxonomy order).

Public database `astrophysics`: "The Astrophysics Database" — real, fact-checked
astrophysics: stellar structure and evolution, radiative processes, the
interstellar medium, accretion physics, compact objects, galactic dynamics, the
cosmology interface, observational techniques, and numerical methods
(src public-harvest).

Signature database `astrophysics-signature`: "The Astrophysics Signature
Database" — his original Signature take on astrophysics (src signature, titles
suffixed " (Signature Edition)", never presented as authentic public record).

Every record carries ladder_rank (1-10) + ladder_tier
(foundations/compounded/advanced); pages render in ladder order (simple ->
compounded -> complex).

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable, stdlib-only
Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Physical constants (exact or CODATA values)
C = 299792458.0            # m/s, exact by SI definition
G = 6.67430e-11            # m^3 kg^-1 s^-2
H_PLANCK = 6.62607015e-34  # J s, exact
K_B = 1.380649e-23         # J/K, exact
SIGMA = 5.670374419e-8     # W m^-2 K^-4, Stefan-Boltzmann
SIGMA_T = 6.6524587321e-29 # m^2, Thomson cross-section
M_P = 1.67262192369e-27    # kg, proton mass
M_E = 9.1093837015e-31     # kg, electron mass
PC = 3.085677581e16        # m
AU = 1.495978707e11        # m, exact
LY = 9.4607304725808e15    # m
M_SUN = 1.98847e30         # kg
R_SUN = 6.957e8            # m
L_SUN = 3.828e26           # W
WIEN = 2.897771955e-3      # m K, Wien displacement constant

# Shared citation tails
CIT_CO = ("Carroll, B. W. & Ostlie, D. A. (2017). 'An Introduction to Modern "
          "Astrophysics', 2nd ed. Cambridge University Press.")
CIT_RL = ("Rybicki, G. B. & Lightman, A. P. (1979). 'Radiative Processes in "
          "Astrophysics'. Wiley-VCH.")
CIT_SHU = ("Shu, F. H. (1982). 'The Physical Universe: An Introduction to "
           "Astronomy'. University Science Books.")
CIT_BT = ("Binney, J. & Tremaine, S. (2008). 'Galactic Dynamics', 2nd ed. "
          "Princeton University Press.")
CIT_PEACOCK = ("Peacock, J. A. (1999). 'Cosmological Physics'. Cambridge "
               "University Press.")
CIT_STD = "Standard astrophysics literature (peer-reviewed textbooks and journals)."
SIG_TAIL = ("Signature editions are original Signature interpretations of the "
            "astrophysics, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-astrophysics", "name": "What Is Astrophysics: The Physics of the Universe",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Astrophysics is the branch of astronomy that applies the laws of physics — "
  "gravity, thermodynamics, electromagnetism, nuclear physics, and quantum "
  "mechanics — to understand celestial objects and the universe as a whole. Where "
  "classical astronomy catalogued the positions and motions of the stars, "
  "astrophysics asks what stars are made of, how they shine, how they are born "
  "and die, and how galaxies and the cosmos itself evolve. Almost everything "
  "astrophysicists know comes from light: its intensity, color, spectrum, "
  "polarization, and arrival time carry the temperature, composition, velocity, "
  "and distance of its source. The observable universe spans about 93 billion "
  "light-years across, is 13.8 billion years old, and holds on the order of two "
  "trillion galaxies — and every one of those numbers was measured, not assumed."),
 "how_it_works": (
  "Astrophysics works by turning observations into physical models and then "
  "testing the models against new observations. A telescope collects photons; a "
  "spectrograph spreads them by wavelength; the resulting spectrum is compared "
  "with the predictions of atomic physics and radiative transfer to read off "
  "temperature, density, composition, and motion. Stellar models solve the "
  "equations of hydrostatic equilibrium, energy transport, and nuclear energy "
  "generation simultaneously and are checked against real stars' luminosities, "
  "radii, and ages. On the largest scales, the equations of general relativity "
  "applied to a homogeneous universe predict an expanding cosmos whose expansion "
  "history is measured with supernovae and the cosmic microwave background. "
  "Every rung of the subject is anchored the same way: a physical law, a "
  "mathematical model, and a measurement that agrees."),
 "key_points": [
  "Astrophysics explains celestial objects with the same physical laws used in laboratories on Earth.",
  "Nearly all cosmic information arrives as light; spectra decode temperature, composition, and motion.",
  "The field spans scales from atomic nuclei in stellar cores to the 93-billion-light-year observable universe.",
  "Models are tested quantitatively: a stellar model must reproduce real luminosities, radii, and ages.",
  "It unifies the very small and the very large — nuclear physics powers stars; gravity shapes galaxies."],
 "requirements": [
  "Curiosity about the night sky; no mathematics needed for this overview.",
  "Later tiers use high-school algebra, then calculus and physics.",
  "Comfort with very large and very small numbers (scientific notation)."],
 "standards": ["SI units throughout", "IAU nomenclature for objects and units"],
 "citations": [CIT_CO, CIT_SHU],
 "demo_kind": "astro_overview",
 "sig_lens": (
  "The Signature reading of astrophysics treats the universe as the ultimate "
  "engineering system: every star a furnace with a fuel budget, every galaxy a "
  "structure under load, every measurement a sensor reading. This database keeps "
  "that discipline — every record names the physical law, the model, and the "
  "measurement that proves it."),
},
{
 "key": "cosmic-units", "name": "Cosmic Units: Parsecs, Light-Years, and Solar Masses",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Astronomical distances are so vast that meters and kilometers become useless, "
  "so astrophysics uses units matched to the scales involved. The astronomical "
  "unit (AU), about 150 million kilometers, is the mean Earth-Sun distance and "
  "the yardstick of the solar system. The light-year, about 9.46 trillion "
  "kilometers, is the distance light travels in one year and the natural unit "
  "for interstellar distances. The parsec, about 3.26 light-years, is defined "
  "geometrically: it is the distance at which one AU subtends an angle of one "
  "arcsecond, and it is the professional unit of stellar and galactic distance. "
  "Masses are quoted in solar masses (one solar mass is about 1.989 x 10^30 kg), "
  "luminosities in solar luminosities, and cosmic time in gigayears. Learning "
  "these units is learning to think at cosmic scale: the nearest star is 1.3 "
  "parsecs away, the Milky Way is 30,000 parsecs across, and the nearest large "
  "galaxy is 780,000 parsecs distant."),
 "how_it_works": (
  "Each cosmic unit is defined from something measurable. The AU comes from "
  "planetary radar ranging and spacecraft telemetry, pinned down exactly by "
  "definition since 2012. The parsec comes from parallax: as Earth orbits the "
  "Sun, a nearby star appears to shift against distant background stars by an "
  "angle p in arcseconds, and its distance is simply 1/p parsecs — the first "
  "direct rung of the cosmic distance ladder. The light-year follows from the "
  "exact speed of light. Converting between them is exact arithmetic: one "
  "parsec equals 3.26156 light-years because a parsec is defined as the "
  "distance giving one arcsecond of parallax for a one-AU baseline. Solar "
  "masses and luminosities are measured from orbital dynamics and calibrated "
  "stellar models, so quoting a galaxy's mass as 10^12 solar masses says "
  "exactly how many Suns' worth of gravity it contains."),
 "key_points": [
  "The AU (Earth-Sun distance) measures the solar system; the parsec and light-year measure the stars and beyond.",
  "One parsec is defined by parallax: 1 AU subtending 1 arcsecond, equal to 3.26156 light-years.",
  "Parallax (distance = 1/parallax-arcseconds parsecs) is the only direct geometric distance method.",
  "Solar masses, solar radii, and solar luminosities keep stellar numbers human-sized.",
  "Unit fluency is prerequisite: every later record quotes distances in parsecs and masses in solar masses."],
 "requirements": [
  "Scientific notation (powers of ten).",
  "Basic trigonometry idea: small angles (for the parsec definition).",
  "A calculator or the demonstration program."],
 "standards": ["IAU 2012 exact AU = 149,597,870,700 m", "SI units throughout"],
 "citations": [CIT_SHU, CIT_STD],
 "demo_kind": "scale_units",
 "sig_lens": (
  "The Signature reading treats units as interface specifications: a number "
  "without its unit contract is a bug. This database enforces the contract — "
  "every quantity in every record carries explicit, convertible, checkable units."),
},
{
 "key": "em-spectrum", "name": "Light and the Electromagnetic Spectrum",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Light is electromagnetic radiation, and the full range of it — from radio "
  "waves kilometers long to gamma rays smaller than an atomic nucleus — is the "
  "electromagnetic spectrum. Visible light, the rainbow band from violet "
  "(about 380 nanometers) to red (about 750 nanometers), is only a sliver of "
  "what the universe broadcasts. Hot young stars blaze in ultraviolet; cool "
  "dust glows in infrared; the afterglow of the Big Bang peaks in microwaves; "
  "accreting black holes and exploding stars scream in X-rays and gamma rays. "
  "A photon's energy is inversely proportional to its wavelength (E = hc/λ), so "
  "each band probes different physics: radio maps cold gas and magnetic fields, "
  "infrared sees through dust to stellar nurseries, optical reveals stars and "
  "galaxies, X-rays trace million-degree gas, and gamma rays flag the most "
  "violent events in nature. Modern astrophysics is multi-wavelength by "
  "necessity — no single band tells the whole story."),
 "how_it_works": (
  "Every band of the spectrum is detected with technology matched to its "
  "photons. Radio dishes collect long-wavelength photons with antennas; "
  "infrared and optical telescopes use mirrors and semiconductor detectors; "
  "ultraviolet needs space telescopes above the ozone layer; X-rays require "
  "grazing-incidence mirrors because they pass straight through normal ones; "
  "gamma rays are caught by scintillators or by the particle showers they "
  "trigger in the atmosphere. Earth's atmosphere blocks most bands, which is "
  "why the great observatories for infrared, ultraviolet, X-ray, and gamma-ray "
  "astronomy fly in space. The energy-wavelength relation E = hc/λ converts "
  "every measurement: a 21-centimeter radio photon carries a millionth of an "
  "electronvolt, while a gamma-ray photon from a burst can carry billions. "
  "Matching the band to the physics is the first decision in any observation."),
 "key_points": [
  "The spectrum runs from kilometer radio waves to sub-nuclear gamma rays; visible light is a thin slice.",
  "Photon energy E = hc/λ: short wavelength means high energy and different physics.",
  "Each band needs its own detectors, and most bands require space telescopes.",
  "Infrared penetrates dust; X-rays trace million-degree gas; gamma rays mark cataclysms.",
  "Multi-wavelength observing is standard practice — one band never tells the whole story."],
 "requirements": [
  "Scientific notation and the idea of wavelength.",
  "The relation E = hc/λ (used numerically in the demo).",
  "No calculus needed."],
 "standards": ["SI units throughout", "Photon energies quoted in electronvolts"],
 "citations": [CIT_RL, CIT_CO],
 "demo_kind": "spectrum",
 "sig_lens": (
  "The Signature reading treats the spectrum as a sensor suite: each band is a "
  "channel with its own noise floor, calibration, and failure modes. The "
  "database keeps that discipline — every band is named with its detectors, "
  "its atmospheric windows, and what it can and cannot see."),
},
{
 "key": "blackbody", "name": "Blackbody Radiation: Why Stars Have Colors",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A blackbody is an idealized object that absorbs all radiation falling on it "
  "and emits a characteristic spectrum depending only on its temperature. Real "
  "stars approximate blackbodies remarkably well, which is why star color is a "
  "thermometer: blue stars are hot (surface temperatures above 10,000 K), "
  "yellow stars like the Sun are middle-aged at about 5,778 K, and red stars "
  "are cool (below 4,000 K). Two laws govern the glow. Wien's displacement law "
  "says the peak wavelength shifts inversely with temperature (λ_max = "
  "2.898 mm·K / T), so the Sun peaks in green-yellow light while a human body "
  "at 310 K peaks deep in the infrared. The Stefan-Boltzmann law says total "
  "emitted power per unit area grows as the fourth power of temperature "
  "(F = σT^4) — a star twice as hot radiates sixteen times more energy per "
  "square meter. Together they explain stellar colors, the cosmic microwave "
  "background's perfect 2.725 K spectrum, and why cooling embers fade from "
  "white to red to black."),
 "how_it_works": (
  "Blackbody radiation arises because the electromagnetic field inside a warm "
  "cavity can only hold energy in discrete packets — photons — and thermal "
  "equilibrium distributes them according to Planck's law, which Max Planck "
  "derived in 1900 by introducing the quantum of action. Integrating Planck's "
  "law over all wavelengths gives the Stefan-Boltzmann T^4 law; differentiating "
  "it to find the peak gives Wien's law. In a star, the dense interior is so "
  "opaque that radiation thermalizes completely, and the photosphere — the "
  "visible surface — radiates very nearly as a blackbody at the star's "
  "effective temperature. Astronomers therefore measure a star's color "
  "(the ratio of brightness in blue versus visual filters, B−V) and convert it "
  "directly to temperature. Deviations from a perfect blackbody — absorption "
  "lines stamped by atoms in the stellar atmosphere — then reveal composition, "
  "which is the business of spectroscopy."),
 "key_points": [
  "Blackbody spectra depend only on temperature — the foundation of stellar thermometry.",
  "Wien's law (λ_max ∝ 1/T) explains star colors and the infrared glow of cool objects.",
  "The Stefan-Boltzmann law (F = σT^4) makes luminosity extremely sensitive to temperature.",
  "Stars approximate blackbodies; their absorption lines then reveal composition.",
  "The cosmic microwave background is the most perfect blackbody ever measured (2.725 K)."],
 "requirements": [
  "Powers and the T^4 idea (no calculus for the laws themselves).",
  "Wavelength and temperature units (nm, K).",
  "The demonstration program evaluates both laws numerically."],
 "standards": ["SI units throughout", "σ = 5.670374419e-8 W m^-2 K^-4"],
 "citations": [
  "Planck, M. (1901). 'On the Law of Distribution of Energy in the Normal Spectrum.' Annalen der Physik, 4, 553-563.",
  CIT_RL],
 "demo_kind": "blackbody",
 "sig_lens": (
  "The Signature reading treats a blackbody curve as a calibration standard: "
  "if your model cannot reproduce Planck's law exactly, your model is wrong. "
  "Every temperature quoted in this database is traceable to these two laws."),
},
{
 "key": "magnitude-system", "name": "The Magnitude System: Measuring Starlight",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Astronomers measure brightness with the magnitude system, inherited from the "
  "ancient Greek star catalogues and formalized in 1856: a difference of 5 "
  "magnitudes equals exactly a factor of 100 in brightness, so each magnitude "
  "step is the fifth root of 100 (about 2.512). The scale runs backwards — "
  "brighter objects have smaller or negative magnitudes: the Sun blazes at "
  "−26.7, Sirius at −1.46, and the faintest stars visible to the naked eye are "
  "about magnitude 6. Apparent magnitude (m) is how bright an object looks from "
  "Earth; absolute magnitude (M) is how bright it would look from the standard "
  "distance of 10 parsecs. The two are linked by the distance modulus, "
  "m − M = 5 log₁₀(d/10 pc), which turns a brightness comparison into a "
  "distance measurement. Measure how bright a star of known intrinsic "
  "brightness appears, and the distance modulus hands you its distance — this "
  "is the workhorse behind standard candles from Cepheid variables to Type Ia "
  "supernovae."),
 "how_it_works": (
  "The magnitude scale is logarithmic because human vision responds "
  "logarithmically to light, and the 1856 formalization made the ancient "
  "1-to-6 scale exact. Flux — energy per second per square meter received at "
  "Earth — falls as the inverse square of distance, so comparing a star's "
  "apparent magnitude with its absolute magnitude (its brightness at 10 pc) "
  "cancels the intrinsic luminosity and isolates distance. In practice, "
  "astronomers measure flux through standardized filters (U, B, V, R, I and "
  "beyond), correct for interstellar dust dimming, look up or calibrate the "
  "absolute magnitude for that class of object, and solve the distance modulus "
  "for d. The method's power is its range: the same equation measures a "
  "Cepheid at 50 kiloparsecs and a supernova at 2 gigaparsecs, provided the "
  "absolute magnitude is trustworthy."),
 "key_points": [
  "5 magnitudes = factor of 100 in brightness; the scale runs backwards (negative = brighter).",
  "Apparent magnitude m is observed brightness; absolute magnitude M is brightness at 10 parsecs.",
  "The distance modulus m − M = 5 log₁₀(d/10 pc) converts brightness into distance.",
  "Standard candles (Cepheids, Type Ia supernovae) supply the trusted absolute magnitudes.",
  "Dust extinction must be corrected first, or distances come out too large."],
 "requirements": [
  "Logarithms (base 10) — the demo walks through them.",
  "Inverse-square law intuition.",
  "No calculus needed."],
 "standards": ["Vega-relative photometric system", "Distances in parsecs"],
 "citations": [
  "Pogson, N. R. (1856). 'Magnitudes of Thirty-six of the Minor Planets for the First Day of Each Month of the Year 1857.' MNRAS, 17, 12-15.",
  CIT_CO],
 "demo_kind": "magnitude",
 "sig_lens": (
  "The Signature reading treats the distance modulus as a measurement "
  "pipeline: raw flux in, calibrated distance out, with every correction "
  "(filters, dust, calibration) logged. A distance quoted without its error "
  "budget is not a Signature measurement."),
},
{
 "key": "stefan-boltzmann-stars", "name": "The Stefan-Boltzmann Law and Stellar Luminosity",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A star's total power output — its luminosity — follows from just two "
  "numbers: its radius and its surface temperature, via L = 4πR²σT⁴. The "
  "4πR² is the star's surface area; the σT⁴ is the blackbody power per unit "
  "area. This single equation organizes the zoo of stars. The Sun "
  "(R = 6.957×10⁸ m, T = 5,778 K) radiates 3.828×10²⁶ watts — about 63 "
  "megawatts per square meter of solar surface, the output of a large power "
  "station from every square meter. Betelgeuse is cool (3,600 K) but enormous "
  "(764 solar radii), so its vast area wins and it shines ~90,000 times "
  "brighter than the Sun. Rigel is smaller but ferociously hot (12,100 K), and "
  "the T⁴ factor makes it ~120,000 solar luminosities. The law also runs "
  "backwards: measure a star's luminosity and temperature, and its radius is "
  "determined — the standard route to stellar sizes."),
 "how_it_works": (
  "The Stefan-Boltzmann law is the integral of Planck's law over all "
  "wavelengths and all outward directions, giving σT⁴ watts per square meter "
  "for a perfect blackbody. A star's photosphere radiates nearly as a "
  "blackbody at the effective temperature, so multiplying by the spherical "
  "surface area 4πR² gives the total luminosity. Astronomers use it in both "
  "directions: from stellar models (which predict R and T) to check predicted "
  "luminosities against observations, and from observations (L from the "
  "distance modulus plus apparent brightness, T from color or spectrum) to "
  "infer radii that can never be resolved directly — most stars are far too "
  "distant to image as disks. Because luminosity depends on the fourth power "
  "of temperature, a modest temperature error becomes a large luminosity "
  "error, so precise temperatures are prized."),
 "key_points": [
  "L = 4πR²σT⁴: luminosity from radius and temperature alone.",
  "The T⁴ dependence makes hot stars disproportionately luminous.",
  "Betelgeuse wins by area, Rigel wins by temperature — the law explains both.",
  "Inverting the law gives stellar radii from luminosity and temperature.",
  "The Sun's surface emits ~63 MW per square meter."],
 "requirements": [
  "Powers and scientific notation.",
  "The blackbody record (Wien's law, σT⁴).",
  "No calculus needed."],
 "standards": ["SI units throughout", "L☉ = 3.828e26 W (IAU 2015 nominal)"],
 "citations": [CIT_CO, CIT_STD],
 "demo_kind": "sb_law",
 "sig_lens": (
  "The Signature reading treats L = 4πR²σT⁴ as an acceptance test: any stellar "
  "model whose radius, temperature, and luminosity do not satisfy it to the "
  "measurement precision fails review. The demo runs that test on real stars."),
},
{
 "key": "telescopes", "name": "Telescopes: How Astronomers Collect Light",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A telescope is a light bucket and a magnifier of detail. Its two "
  "fundamental figures of merit both grow with aperture diameter D. "
  "Light-gathering power scales as D² — the 10-meter Keck mirror collects "
  "about two million times more light than the dark-adapted human eye — which "
  "is why bigger telescopes see fainter objects. Angular resolution, the "
  "finest detail discernible, is set by diffraction: θ ≈ 1.22λ/D radians, the "
  "Rayleigh criterion. The Hubble Space Telescope (2.4 m) resolves about 0.05 "
  "arcseconds in visible light, sharp enough to see a coin from 100 km away; "
  "the 39-meter Extremely Large Telescope will reach ~0.003 arcseconds. "
  "Ground-based telescopes fight atmospheric turbulence ('seeing', typically "
  "~1 arcsecond), which adaptive optics — deformable mirrors reshaped a "
  "thousand times per second using a laser guide star — can largely cancel. "
  "Radio astronomers beat the diffraction limit differently: interferometers "
  "like ALMA combine dishes kilometers apart to synthesize a single "
  "kilometer-scale aperture."),
 "how_it_works": (
  "Telescopes work by collecting plane waves from a distant source over a "
  "large area and bringing them to a common focus. Reflectors use precisely "
  "figured mirrors (polished to tens of nanometers); refractors use lenses but "
  "are limited by chromatic aberration and glass size. The diffraction limit "
  "arises because light is a wave: a circular aperture spreads a point source "
  "into an Airy disk, and two sources closer than ~1.22λ/D blur together. "
  "Adaptive optics measures the atmosphere's distortion with a wavefront "
  "sensor hundreds of times per second and deforms a flexible mirror to cancel "
  "it in real time. Interferometry records the wave's amplitude and phase at "
  "many dishes and combines them in a correlator, achieving the resolution of "
  "an aperture as large as the array's longest baseline. Every gain in "
  "aperture, site quality, or correction technology directly converts into "
  "fainter limits and sharper images."),
 "key_points": [
  "Light-gathering ∝ D²: aperture buys sensitivity to faint objects.",
  "Resolution is diffraction-limited: θ ≈ 1.22λ/D — aperture buys sharpness too.",
  "Atmospheric seeing (~1 arcsecond) limits ground telescopes; adaptive optics cancels it.",
  "Space telescopes escape the atmosphere entirely for ultraviolet and infrared.",
  "Radio interferometers synthesize kilometer-scale apertures from many dishes."],
 "requirements": [
  "The wavelength idea from the spectrum record.",
  "Small-angle intuition (arcseconds).",
  "No calculus needed."],
 "standards": ["Angles in arcseconds", "SI units throughout"],
 "citations": [
  "Wilson, R. N. (2007). 'Reflecting Telescope Optics', Vols. I-II. Springer.",
  CIT_STD],
 "demo_kind": "telescope",
 "sig_lens": (
  "The Signature reading treats a telescope as a sensor with a datasheet: "
  "aperture, diffraction limit, throughput, and noise floor. This record is "
  "that datasheet pattern — every instrument in the database gets its limits "
  "stated up front, in numbers."),
},
{
 "key": "doppler-shift", "name": "The Doppler Shift: Reading Motion in Starlight",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Motion along the line of sight stretches or squeezes light waves, shifting "
  "the entire spectrum: receding sources are redshifted to longer wavelengths, "
  "approaching sources blueshifted to shorter ones. For speeds far below light "
  "speed, Δλ/λ = v/c — a star receding at 30 km/s (Earth's orbital speed) "
  "shifts its lines by one part in 10,000. This single effect is "
  "astrophysics' speedometer. It revealed the expansion of the universe "
  "(galaxies' redshifts grow with distance), weighed unseen exoplanets (51 "
  "Pegasi's star wobbles at just 55 m/s, betraying its hot Jupiter), mapped "
  "galactic rotation (one side of a spinning galaxy redshifts, the other "
  "blueshifts), and measures stellar surface motions and gas flows. Modern "
  "spectrographs measure shifts of one part in a hundred million — the width "
  "of a human hair seen from a kilometer — routinely."),
 "how_it_works": (
  "Each chemical element imprints absorption or emission lines at fixed "
  "laboratory wavelengths. A spectrograph spreads starlight finely enough to "
  "locate those lines, and any systematic offset from the laboratory "
  "wavelengths is the Doppler shift. Dividing the shift by the rest wavelength "
  "gives v/c directly, with sign indicating direction. Calibration is "
  "everything: the spectrograph is referenced against thorium-argon lamps or "
  "laser frequency combs stable to centimeters per second, and Earth's own "
  "motions (rotation, orbit) are subtracted to leave the star's true radial "
  "velocity. Repeated measurements trace velocity curves — the sinusoidal "
  "wobble of a star tugged by an orbiting planet, or the rotation curve of a "
  "galaxy — and the amplitude and period of the curve give masses and orbits "
  "through Kepler's laws. At cosmological distances the same shift, "
  "interpreted as cosmic expansion, becomes redshift z and a distance "
  "indicator."),
 "key_points": [
  "Δλ/λ = v/c: spectral line shifts directly measure line-of-sight velocity.",
  "Redshift means receding; blueshift means approaching.",
  "Exoplanets are found by stellar wobbles as small as meters per second.",
  "Galaxy rotation curves from Doppler shifts revealed dark matter.",
  "Cosmological redshift measures the expansion of the universe."],
 "requirements": [
  "Ratios and the idea of a spectrum with lines.",
  "The speed of light c.",
  "No calculus needed."],
 "standards": ["Velocities in km/s (m/s for exoplanets)", "Wavelengths in nm"],
 "citations": [
  "Mayor, M. & Queloz, D. (1995). 'A Jupiter-mass companion to a solar-type star.' Nature, 378, 355-359.",
  CIT_CO],
 "demo_kind": "doppler_spec",
 "sig_lens": (
  "The Signature reading treats every spectrum as a signed measurement: the "
  "line positions, the calibration source, and the subtracted Earth motions "
  "are all part of the record. A velocity without its calibration chain is "
  "not a Signature result."),
},
]
# ------------------------------------------------------------------ COMPOUNDED
ENTRIES += [
{
 "key": "hydrostatic-equilibrium", "name": "Hydrostatic Equilibrium: What Holds a Star Up",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "A star is a continuous tug-of-war: gravity pulls every gram of gas inward, "
  "and pressure pushes outward. Hydrostatic equilibrium is the balance "
  "condition, written as dP/dr = −GM(r)ρ(r)/r² — at each radius, the pressure "
  "gradient exactly supports the weight of the layers above. This one equation, "
  "together with mass conservation, is the skeleton of every stellar model. "
  "It dictates that pressure and temperature must rise steeply toward the "
  "center: the Sun's core sits at about 15.7 million K and 2.5×10¹⁶ pascals "
  "(250 billion atmospheres), while its surface is a mild 5,778 K at near "
  "vacuum. The equation also sets a star's response to disturbance — squeeze a "
  "star and the pressure rises faster than gravity, so it bounces back; this "
  "restoring behavior is why stars are stable for billions of years rather "
  "than collapsing or exploding on a whim. When equilibrium fails — when the "
  "core runs out of fuel and pressure support vanishes — the star collapses, "
  "and stellar evolution begins in earnest."),
 "how_it_works": (
  "Consider a thin spherical shell of gas at radius r with thickness dr. The "
  "gravitational force on it is GM(r)dm/r² inward, where M(r) is the mass "
  "interior to r. For the shell to hover motionless, the pressure below must "
  "exceed the pressure above by exactly enough to balance that weight, giving "
  "dP = −ρGM(r)dr/r². Stellar-structure codes integrate this equation outward "
  "from the center (with M(0) = 0 and finite central pressure) together with "
  "the energy-generation and energy-transport equations, adjusting until the "
  "surface conditions match an observable star. The demonstration integrates "
  "the constant-density case analytically and numerically: even this toy model "
  "reproduces the order of magnitude of stellar central pressures, and the "
  "gap between the toy value and the real Sun's 2.5×10¹⁶ Pa measures how "
  "centrally condensed a real star is. Real models replace constant density "
  "with the equation of state of hot plasma and iterate to consistency."),
 "key_points": [
  "dP/dr = −GM(r)ρ/r²: pressure gradient balances gravity at every radius.",
  "Central conditions are extreme: 15.7 million K and 250 billion atmospheres in the Sun.",
  "The balance is stable — compression raises pressure faster than gravity, restoring equilibrium.",
  "Hydrostatic equilibrium plus energy equations define all stellar models.",
  "Loss of pressure support (fuel exhaustion) triggers collapse and evolution."],
 "requirements": [
  "The cosmic-units and blackbody records.",
  "Derivatives intuition (the demo integrates numerically).",
  "High-school physics: pressure, density, gravity."],
 "standards": ["SI units throughout", "Pressures in pascals"],
 "citations": [
  "Eddington, A. S. (1926). 'The Internal Constitution of the Stars'. Cambridge University Press.",
  CIT_CO],
 "demo_kind": "hydrostatic",
 "sig_lens": (
  "The Signature reading treats hydrostatic equilibrium as a load-bearing "
  "specification: every stellar model must show its pressure profile "
  "supporting its own weight, layer by layer, or it does not ship. The demo "
  "runs that structural check numerically."),
},
{
 "key": "nuclear-fusion-stars", "name": "Nuclear Fusion: The Proton-Proton Chain and the CNO Cycle",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Stars shine by fusing light nuclei into heavier ones, converting a small "
  "fraction of mass into energy via E = mc². In the Sun and lighter stars the "
  "proton-proton chain dominates: four protons become one helium-4 nucleus, "
  "two positrons, and two neutrinos, releasing 26.73 MeV per helium nucleus — "
  "about 0.7% of the starting mass becomes energy. The chain's first step, two "
  "protons fusing, requires quantum tunneling through their electric repulsion "
  "and is so improbable that a given proton waits ~10¹⁰ years — which is why "
  "the Sun burns slowly for billions of years instead of detonating. In stars "
  "heavier than about 1.3 solar masses, core temperatures exceed ~17 million K "
  "and the CNO cycle takes over: carbon, nitrogen, and oxygen catalyze the "
  "same net fusion of hydrogen into helium but at a rate scaling as ~T²⁰, "
  "fiercely temperature-sensitive. Later burning stages fuse helium into "
  "carbon and oxygen (the triple-alpha process), then carbon, neon, oxygen, "
  "and silicon in massive stars, climbing the periodic table toward iron — "
  "each stage faster and shorter than the last."),
 "how_it_works": (
  "Fusion rates come from nuclear cross-sections folded with the Maxwell-"
  "Boltzmann distribution of particle speeds at the core temperature, "
  "integrated over the quantum-tunneling probability (the Gamow peak). Hans "
  "Bethe worked out the chains in 1939, showing the pp chain's rate scales "
  "roughly as T⁴ near solar temperatures while the CNO cycle scales as ~T²⁰. "
  "That steepness is why energy generation concentrates in a tiny central "
  "volume and why massive stars, with slightly hotter cores, burn enormously "
  "faster. Each helium nucleus forged releases 26.73 MeV; dividing the Sun's "
  "luminosity by this energy gives ~9×10³⁷ fusions per second, consuming about "
  "600 million tons of hydrogen every second (of which ~4 million tons becomes "
  "energy). Neutrinos escape immediately, carrying ~2% of the energy, and "
  "their measured flux — about 6×10¹⁰ per cm² per second at Earth — "
  "independently confirms the fusion rate in the solar core."),
 "key_points": [
  "4 protons → helium-4 + 2 positrons + 2 neutrinos + 26.73 MeV (pp chain).",
  "Quantum tunneling makes the first step improbable — hence billion-year stellar lifetimes.",
  "The CNO cycle (∝ T²⁰) dominates above ~1.3 solar masses.",
  "Successive burning stages (He, C, Ne, O, Si) run faster and shorter toward iron.",
  "Solar neutrino flux independently confirms the core fusion rate."],
 "requirements": [
  "E = mc² and electronvolts.",
  "The hydrostatic-equilibrium record (core conditions).",
  "Powers and exponentials; the demo evaluates rate scalings."],
 "standards": ["Energies in MeV", "Temperatures in millions of K (T₆)"],
 "citations": [
  "Bethe, H. A. (1939). 'Energy Production in Stars.' Physical Review, 55, 434-456.",
  CIT_CO],
 "demo_kind": "fusion",
 "sig_lens": (
  "The Signature reading treats a star as a reactor with a fuel ledger: "
  "hydrogen in, helium plus energy out, neutrinos as the auditable exhaust. "
  "The demo balances that ledger for the Sun and shows why the CNO cycle's "
  "T²⁰ scaling makes massive stars live fast and die young."),
},
{
 "key": "hr-diagram", "name": "The Hertzsprung-Russell Diagram",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Plot stars by surface temperature (hot to the left) against luminosity "
  "(bright upward) and a striking pattern emerges: the Hertzsprung-Russell "
  "diagram. Most stars — about 90%, including the Sun — lie on the diagonal "
  "main sequence, fusing hydrogen in their cores. Above it sit the giants and "
  "supergiants: cool but hugely luminous because they are enormous. Below it "
  "huddle the white dwarfs: hot but dim because they are Earth-sized. The "
  "diagram, developed independently by Ejnar Hertzsprung and Henry Norris "
  "Russell around 1910, is the central organizing map of stellar astrophysics. "
  "A star's position encodes its mass, age, and evolutionary state: newborn "
  "clusters show a full main sequence, while old clusters show it truncated — "
  "the massive stars have already died — with the 'turnoff point' giving the "
  "cluster's age directly. Reading an HR diagram is reading stellar life "
  "stories in bulk."),
 "how_it_works": (
  "Building an HR diagram requires two observables per star: temperature and "
  "luminosity. Temperature comes from color (B−V) or spectral type via the "
  "blackbody relation; luminosity comes from apparent brightness plus distance "
  "(the distance modulus). Plotting hundreds of cluster stars — all at nearly "
  "the same distance and age — reveals the sequences cleanly. The main "
  "sequence's tightness reflects a physical law: for hydrogen-burning stars, "
  "mass determines everything, and luminosity scales as ~M^3.5, so the "
  "sequence is really a mass sequence in disguise. Stellar-evolution theory "
  "predicts tracks across the diagram: a star leaves the main sequence when "
  "core hydrogen exhausts, swelling into a red giant (moving up and right), "
  "then shedding its envelope to become a white dwarf (dropping down and "
  "left). Fitting theoretical isochrones (equal-age curves) to an observed "
  "diagram dates the cluster — the standard method for star-cluster and "
  "galactic ages."),
 "key_points": [
  "Main sequence (90% of stars): core hydrogen fusion; a mass sequence in disguise.",
  "Giants/supergiants above: luminous through huge size; white dwarfs below: dim through tiny size.",
  "Position encodes mass, age, and evolutionary state.",
  "Cluster turnoff points date star clusters via isochrone fitting.",
  "The diagram is the master map linking observation to stellar-evolution theory."],
 "requirements": [
  "The blackbody and magnitude records.",
  "Logarithmic axes intuition.",
  "No calculus needed."],
 "standards": ["Luminosities in L☉", "Temperatures in K (hot left by convention)"],
 "citations": [
  "Russell, H. N. (1914). 'Relations Between the Spectra and Other Characteristics of the Stars.' Popular Astronomy, 22, 275-294.",
  CIT_CO],
 "demo_kind": "hr",
 "sig_lens": (
  "The Signature reading treats the HR diagram as a fleet-status board: every "
  "star a unit reporting temperature and power, the sequences revealing the "
  "physics governing the fleet. The demo places real stars on the board and "
  "checks each lands in its correct region."),
},
{
 "key": "mass-luminosity", "name": "The Mass-Luminosity Relation and Stellar Lifetimes",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "For main-sequence stars, luminosity scales as roughly the 3.5 power of "
  "mass: L ∝ M^3.5. A 2-solar-mass star shines ~11 times brighter than the "
  "Sun; a 10-solar-mass star ~3,000 times brighter. This relation is the "
  "reason massive stars live fast and die young. A star's fuel supply grows "
  "linearly with mass, but its burn rate grows as M^3.5, so its main-sequence "
  "lifetime shrinks as t ∝ M/L ∝ M^−2.5. The Sun gets ~10 billion years; a "
  "10-solar-mass star gets ~30 million; a 0.5-solar-mass red dwarf gets "
  "~60 billion years — longer than the universe has existed, which is why no "
  "red dwarf has ever died of old age. The relation emerges from stellar "
  "structure: more massive stars need higher central temperatures to support "
  "their weight, and nuclear rates are ferociously temperature-sensitive, so "
  "luminosity climbs steeply. It underpins distance estimates, cluster dating, "
  "and the accounting of how galaxies build their light."),
 "how_it_works": (
  "The M^3.5 scaling can be derived from homology relations: assume stars are "
  "scaled copies of one another, combine hydrostatic equilibrium with "
  "radiative energy transport and a Kramers-type opacity, and luminosity "
  "emerges proportional to μ^7.5 M^5.5 / R^0.5, which with the mass-radius "
  "relation for main-sequence stars reduces to ~M^3.5 (the exponent varies "
  "from ~2.5 to ~4 across the mass range in detailed models). Observationally "
  "it is calibrated with binary stars, whose masses come directly from "
  "orbital dynamics via Kepler's third law, and whose luminosities come from "
  "the distance modulus. Lifetime follows immediately: t_MS ≈ 10¹⁰ yr × "
  "(M/M☉)/(L/L☉). The demonstration evaluates lifetimes across the mass range "
  "and verifies the exponent against the binary-star calibration points, "
  "showing quantitatively why the night sky's brightest stars are cosmic "
  "mayflies and its dimmest are nearly immortal."),
 "key_points": [
  "L ∝ M^3.5 on the main sequence (calibrated by binary-star masses).",
  "Lifetime t ∝ M^−2.5: 10 M☉ → 30 Myr; 0.5 M☉ → 60 Gyr.",
  "No red dwarf has ever exhausted its fuel — all still shine.",
  "Steep nuclear temperature sensitivity is the physical root of the relation.",
  "The relation powers distance estimates and galaxy light accounting."],
 "requirements": [
  "The fusion and HR-diagram records.",
  "Power-law manipulation.",
  "No calculus needed."],
 "standards": ["Masses in M☉", "Lifetimes in years (Myr, Gyr)"],
 "citations": [
  "Salpeter, E. E. (1955). 'The Luminosity Function and Stellar Evolution.' ApJ, 121, 161-167.",
  CIT_CO],
 "demo_kind": "masslum",
 "sig_lens": (
  "The Signature reading treats the mass-luminosity relation as a burn-rate "
  "specification: mass in, lifetime out, with the exponent audited against "
  "binary-star measurements. The demo runs that audit and prints the "
  "lifetimes the relation guarantees."),
},
{
 "key": "radiative-transfer", "name": "Radiative Transfer: How Light Escapes a Star",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "A photon born in the Sun's core does not fly straight out — it is "
  "absorbed and re-emitted countless times, random-walking outward for "
  "~170,000 years before reaching the surface, while the energy it carries "
  "would cross in 2 seconds at light speed. Radiative transfer is the theory "
  "of this journey. Its central quantity is optical depth τ, the number of "
  "mean free paths along a ray: intensity falls as I = I₀e^−τ (the "
  "Beer-Lambert law), so τ = 1 marks one e-folding of attenuation. The "
  "stellar photosphere — the visible 'surface' — is defined at τ ≈ 2/3, the "
  "depth from which photons typically escape to space. Where the gas is "
  "ionized and opaque, radiation diffuses slowly and carries the star's "
  "luminosity outward; where it is transparent, photons stream freely. The "
  "same mathematics governs planetary atmospheres, interstellar dust "
  "extinction, and the cosmic microwave background's last scattering — "
  "wherever light and matter exchange energy, optical depth is the ledger."),
 "how_it_works": (
  "The radiative transfer equation balances, along every ray, the light added "
  "by emission against the light removed by absorption and scattering: "
  "dI/dτ = −I + S, where S is the source function (the Planck function in "
  "thermal equilibrium). In stellar interiors the diffusion approximation "
  "applies: the radiation field is nearly isotropic, energy flows down the "
  "temperature gradient, and the luminosity at each radius follows from the "
  "local opacity. Opacity — the cross-section per gram — comes from atomic "
  "physics: bound-free and free-free absorption plus electron scattering, "
  "tabulated in modern OPAL tables as functions of temperature and density. "
  "Near the surface the full angle-dependent equation must be solved, giving "
  "limb darkening (the Sun's edge looks dimmer because the line of sight "
  "exits at a slant through cooler, higher layers). The demonstration "
  "evaluates the attenuation law across optical depths and locates the "
  "τ = 2/3 photosphere, then shows how limb darkening follows from geometry."),
 "key_points": [
  "Optical depth τ counts mean free paths; intensity falls as e^−τ.",
  "The photosphere sits at τ ≈ 2/3 — the escape depth of the photons we see.",
  "Core photons random-walk out over ~10⁵ years; the energy flow is diffusive.",
  "Opacity from atomic physics (OPAL tables) controls the transport.",
  "The same equation governs atmospheres, dust extinction, and the CMB."],
 "requirements": [
  "The blackbody record.",
  "Exponentials (e^−τ).",
  "No calculus needed for the concepts; the demo integrates numerically."],
 "standards": ["Optical depth dimensionless", "SI units throughout"],
 "citations": [CIT_RL, CIT_CO],
 "demo_kind": "radtransfer",
 "sig_lens": (
  "The Signature reading treats optical depth as a transparency ledger: every "
  "layer of material posts its attenuation, and the τ = 2/3 line marks where "
  "the books close and photons go free. The demo audits that ledger layer by "
  "layer."),
},
{
 "key": "eddington-limit", "name": "The Eddington Limit: How Bright a Star Can Be",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "There is a maximum luminosity any object can sustain: the Eddington limit, "
  "L_Edd = 4πGMm_p c/σ_T ≈ 1.26×10³⁸ (M/M☉) erg/s, about 32,000 solar "
  "luminosities per solar mass. The physics is a force balance — radiation "
  "pushing outward on electrons (via Thomson scattering) against gravity "
  "pulling inward on protons. Exceed the limit and radiation pressure blows "
  "the outer layers away; the object sheds mass until it dims back below the "
  "ceiling. Real stars respect it: the most luminous known stars hover just "
  "under their Eddington luminosity, driving ferocious winds. Accreting black "
  "holes and neutron stars use it as a benchmark — the Eddington ratio "
  "L/L_Edd classifies quasars and X-ray binaries, and ultraluminous X-ray "
  "sources were once mysterious precisely because they appeared to break it "
  "(beaming and super-Eddington accretion flows explain them). The limit "
  "assumes spherical symmetry and fully ionized gas; real systems cheat with "
  "disks, jets, and clumpy winds, but always pay in mass loss."),
 "how_it_works": (
  "Equate the outward radiation force on one electron-proton pair to the "
  "inward gravitational force. Radiation pressure gives F_rad = σ_T L/(4πr²c) "
  "(Thomson cross-section times flux over c); gravity gives F_grav = GMm_p/r² "
  "(the proton carries the mass, the electron the cross-section, and "
  "electrostatic coupling binds them). Setting F_rad = F_grav, the r² cancels "
  "— the limit is independent of radius — leaving L_Edd = 4πGMm_p c/σ_T. "
  "Arthur Eddington derived it in the 1920s while modeling stellar "
  "interiors. For accretion, the same luminosity caps the steady accretion "
  "rate (the Eddington accretion rate Ṁ_Edd = L_Edd/ηc² with η ~ 0.1 "
  "efficiency). The demonstration evaluates the limit for stars, stellar-mass "
  "black holes, and supermassive black holes, and computes the Eddington "
  "ratio of a luminous quasar to show where real objects sit relative to the "
  "ceiling."),
 "key_points": [
  "L_Edd = 4πGMm_p c/σ_T: radiation pressure vs. gravity, radius cancels out.",
  "≈ 32,000 L☉ per solar mass; the most luminous stars sit just beneath it.",
  "Exceeding it drives mass loss until the object dims back down.",
  "The Eddington ratio L/L_Edd classifies accreting black holes and quasars.",
  "Disks, jets, and beaming let systems appear to cheat — at a price."],
 "requirements": [
  "The hydrostatic-equilibrium and blackbody records.",
  "Force-balance algebra.",
  "No calculus needed."],
 "standards": ["Luminosities in erg/s and L☉", "SI units in the demo"],
 "citations": [
  "Eddington, A. S. (1926). 'The Internal Constitution of the Stars'. Cambridge University Press.",
  CIT_RL],
 "demo_kind": "eddington",
 "sig_lens": (
  "The Signature reading treats the Eddington limit as a hard safety rating: "
  "no steady spherical source may exceed it without shedding mass, and the "
  "demo enforces the rating across stars, stellar black holes, and quasars, "
  "flagging anything that runs hot."),
},
{
 "key": "interstellar-medium", "name": "The Interstellar Medium: Gas and Dust Between the Stars",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The space between stars is not empty: the interstellar medium (ISM) holds "
  "about 5-10% of a galaxy's visible mass as gas and dust, and it is the raw "
  "material of future stars and planets. The ISM is multiphase — coexisting "
  "states in rough pressure equilibrium. Cold molecular clouds (10-20 K, "
  "hundreds of particles per cm³) are the stellar nurseries, dark and dense. "
  "The cold and warm neutral medium (50-8,000 K) fills much of the disk. Warm "
  "ionized gas (~8,000 K) glows around hot stars. And the hot ionized medium "
  "(~10⁶ K, thousandths of a particle per cm³), carved by supernova blasts, "
  "fills much of the volume. Threading it all are dust grains — silicate and "
  "carbon soot making up ~1% of the mass — which dim and redden starlight "
  "(extinction), catalyze molecule formation on their surfaces, and re-radiate "
  "in the infrared. The ISM is a cycle: stars forge heavy elements, winds and "
  "supernovae return them to the gas, and gravity gathers the enriched gas "
  "into the next generation."),
 "how_it_works": (
  "The phases persist because heating and cooling balance differently at "
  "different densities: photoelectric heating by starlight on dust grains "
  "warms diffuse gas, while line emission from carbon, oxygen, and molecules "
  "cools dense gas efficiently. Field, Goldsmith, and Habing showed in 1969 "
  "that thermal equilibrium allows two stable phases (cold dense, warm "
  "diffuse) at the same pressure — the theoretical backbone of the multiphase "
  "model later extended by McKee and Ostriker to include supernova-driven hot "
  "gas. Observers dissect the ISM with complementary tracers: the 21-cm line "
  "of atomic hydrogen maps neutral gas; CO rotational lines trace molecular "
  "clouds; infrared emission maps dust; X-rays reveal the hot phase. Pressure "
  "balance (nT roughly constant across phases) is the quick check: cold "
  "dense gas and hot tenuous gas carry comparable pressures, so they can "
  "coexist. The demonstration verifies that balance numerically across the "
  "canonical phases."),
 "key_points": [
  "Multiphase gas (10 K to 10⁶ K) coexists in rough pressure equilibrium.",
  "Cold molecular clouds are stellar nurseries; supernovae carve the hot phase.",
  "Dust (~1% by mass) causes extinction, forms molecules, and glows in infrared.",
  "The ISM is a recycling system: stellar ejecta become the next generation's fuel.",
  "21-cm, CO, infrared, and X-ray tracers each map a different phase."],
 "requirements": [
  "The blackbody and spectrum records.",
  "Ideal-gas pressure intuition (P ∝ nT).",
  "No calculus needed."],
 "standards": ["Densities in cm⁻³", "Temperatures in K", "Pressures as nT (K cm⁻³)"],
 "citations": [
  "Field, G. B., Goldsmith, D. W. & Habing, H. J. (1969). 'Cosmic-Ray Heating of the Interstellar Gas.' ApJ, 155, L149.",
  "McKee, C. F. & Ostriker, J. P. (1977). 'A Theory of the Interstellar Medium.' ApJ, 218, 148-169."],
 "demo_kind": "ism",
 "sig_lens": (
  "The Signature reading treats the ISM as a materials inventory with "
  "phase-separated stock: each phase logged with temperature, density, and "
  "pressure, the books balanced across phases. The demo audits that balance "
  "and flags any phase that will not coexist."),
},
{
 "key": "jeans-criterion", "name": "Star Formation: The Jeans Criterion and Collapsing Clouds",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A cloud of gas collapses into stars when gravity overcomes thermal "
  "pressure — the Jeans criterion, derived by James Jeans in 1902. The Jeans "
  "mass, M_J ∝ T^3/2 / ρ^1/2, is the minimum mass that can collapse at a "
  "given temperature and density: cold, dense clouds collapse easily, hot "
  "diffuse ones resist. A typical molecular cloud core (10 K, 10⁴ particles "
  "per cm³) has a Jeans mass of a few solar masses — exactly the scale of "
  "individual stars. Collapse is not gentle: as the core contracts it heats, "
  "dust radiates the heat away (keeping the gas cold and the Jeans mass "
  "falling, which fragments the cloud into many cores), until densities rise "
  "enough to trap radiation and a protostar forms. Conservation of angular "
  "momentum spins the infalling gas into a protoplanetary disk, and magnetic "
  "fields and outflows shed the excess spin. Triggering helps: supernova "
  "shock waves and spiral-arm compression push stable clouds over the edge, "
  "which is why star formation propagates through galaxies in waves."),
 "how_it_works": (
  "Jeans analyzed small perturbations in a uniform gas: pressure waves "
  "oscillate, but wavelengths longer than λ_J = √(πc_s²/Gρ) grow "
  "exponentially under self-gravity instead of oscillating — sound cannot "
  "cross the region fast enough to restore pressure balance before gravity "
  "wins. The Jeans mass is the mass inside a sphere of diameter λ_J. In real "
  "clouds the criterion is local and time-dependent: as a cloud contracts, ρ "
  "rises and M_J falls, so a collapsing cloud fragments hierarchically into "
  "ever-smaller pieces — the origin of stellar clusters and the stellar "
  "initial mass function. Observers test it by comparing measured core masses "
  "(from dust emission) with the Jeans mass at the measured temperature and "
  "density: cores above M_J show infall signatures (asymmetric line profiles), "
  "cores below it do not. The demonstration evaluates the Jeans mass for "
  "molecular-cloud conditions and checks the fragmentation logic as density "
  "rises."),
 "key_points": [
  "M_J ∝ T^3/2/ρ^1/2: cold dense gas collapses; hot diffuse gas resists.",
  "Typical core Jeans mass is a few M☉ — the scale of individual stars.",
  "Falling Jeans mass during collapse drives hierarchical fragmentation.",
  "Angular momentum makes disks; outflows and fields shed excess spin.",
  "Supernova shocks and spiral arms trigger collapse — star formation propagates."],
 "requirements": [
  "The ISM record.",
  "Sound-speed intuition (hot gas pushes back faster).",
  "No calculus needed for the criterion; the demo evaluates it."],
 "standards": ["Densities in cm⁻³", "Masses in M☉"],
 "citations": [
  "Jeans, J. H. (1902). 'The Stability of a Spherical Nebula.' Phil. Trans. R. Soc. A, 199, 1-53.",
  "Shu, F. H., Adams, F. C. & Lizano, S. (1987). 'Star Formation in Molecular Clouds.' ARA&A, 25, 23-81."],
 "demo_kind": "jeans",
 "sig_lens": (
  "The Signature reading treats the Jeans mass as a go/no-go gauge for "
  "collapse: above the line gravity wins, below it pressure holds, and the "
  "demo sweeps the gauge across cloud conditions to map exactly where star "
  "formation is permitted."),
},
{
 "key": "accretion-disks", "name": "Accretion Disks: How Matter Spirals In",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Gas falling toward a compact object rarely falls straight in — it carries "
  "angular momentum, so it settles into a rotating accretion disk and spirals "
  "slowly inward as viscosity transports angular momentum outward. The "
  "gravitational energy released is enormous: accreting onto a black hole "
  "converts ~10% of the infalling mass to radiation (versus 0.7% for stellar "
  "fusion), making accretion the most efficient power source in the universe. "
  "The standard thin-disk model of Shakura and Sunyaev (1973) predicts the "
  "disk's temperature profile, T(r) ∝ r^−3/4, so the inner disk glows in "
  "X-rays while the outer disk shines in optical and infrared — the "
  "multi-temperature blackbody spectrum is the observational fingerprint of "
  "disks around black holes, neutron stars, white dwarfs, and young stars "
  "alike. The same physics powers quasars (supermassive black holes "
  "accreting whole solar masses per year), X-ray binaries, and planet "
  "formation in protoplanetary disks. Jets — collimated outflows launched "
  "along the disk's rotation axis, likely by magnetic fields threading the "
  "inner disk — carry away a share of the energy across the cosmos."),
 "how_it_works": (
  "In a Keplerian disk each annulus orbits at v = √(GM/r). Neighboring "
  "annuli shear past one another; turbulent viscosity (parameterized by "
  "Shakura and Sunyaev's α) exerts torques that move angular momentum outward "
  "and mass inward, dissipating orbital energy as heat. Energy balance at "
  "each radius — viscous heating radiated locally as blackbody emission — "
  "gives σT⁴ = 3GMṀ/8πr³ (1 − √(r_in/r)), hence the r^−3/4 profile outside "
  "the inner edge. The inner edge sits at the innermost stable circular orbit "
  "(6GM/c² for a non-spinning black hole); inside it, gas plunges. The total "
  "luminosity L = ηṀc² with η ~ 0.06-0.42 depending on spin is what makes "
  "quasars outshine galaxies. The demonstration evaluates the temperature "
  "profile for a 10-solar-mass black hole accreting at a tenth of Eddington "
  "and locates the X-ray-emitting inner region versus the optical outer disk."),
 "key_points": [
  "Angular momentum forces infalling gas into disks; viscosity drives the inward spiral.",
  "Accretion efficiency ~10% beats fusion's 0.7% — the universe's best power source.",
  "T(r) ∝ r^−3/4: inner disk X-rays, outer disk optical/infrared.",
  "The inner edge is the innermost stable orbit; inside it gas plunges.",
  "Same physics: quasars, X-ray binaries, young stars, planet formation."],
 "requirements": [
  "The Eddington-limit record.",
  "Keplerian orbit intuition.",
  "Power laws; no calculus needed for the profile."],
 "standards": ["Accretion rates in M☉/yr", "Temperatures in K"],
 "citations": [
  "Shakura, N. I. & Sunyaev, R. A. (1973). 'Black Holes in Binary Systems. Observational Appearance.' A&A, 24, 337-355.",
  "Bondi, H. (1952). 'On Spherically Symmetrical Accretion.' MNRAS, 112, 195-204."],
 "demo_kind": "accretion",
 "sig_lens": (
  "The Signature reading treats an accretion disk as a power plant with a "
  "published efficiency curve: mass flow in, radiation out at 10% conversion, "
  "temperature mapped radius by radius. The demo runs the plant at a tenth of "
  "Eddington and prints its thermal map."),
},
{
 "key": "stellar-evolution", "name": "Stellar Evolution: From Protostar to Remnant",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "A star's life is written at its birth: initial mass decides everything. "
  "Protostars contract and heat until core hydrogen ignites, landing on the "
  "main sequence. Low-mass stars (< 0.5 M☉) burn hydrogen steadily for "
  "trillions of years and fade as helium white dwarfs. Sun-like stars (0.5-8 "
  "M☉) exhaust core hydrogen after billions of years, swell into red giants "
  "burning hydrogen in a shell, ignite helium in the core (the helium flash "
  "for the lightest of them), climb the asymptotic giant branch shedding their "
  "envelopes as planetary nebulae, and leave carbon-oxygen white dwarfs. "
  "Massive stars (8-25 M☉) burn through successive fuels — carbon, neon, "
  "oxygen, silicon — in ever-shorter stages, ending with an iron core that "
  "collapses in seconds and rebounds as a core-collapse supernova, leaving a "
  "neutron star. The most massive (> 25 M☉) leave black holes. Each stage is "
  "shorter than the last: a 20-solar-mass star spends 10 million years on the "
  "main sequence, then burns its remaining fuels in under a million — silicon "
  "burning lasts about a day."),
 "how_it_works": (
  "Stellar-evolution codes (such as MESA) solve the four structure equations "
  "— hydrostatic equilibrium, mass continuity, energy generation, energy "
  "transport — at thousands of mass shells and thousands of time steps, "
  "updating composition as nuclear networks burn and convective zones mix. "
  "The evolution is driven by fuel exhaustion: when a core fuel runs out, "
  "the core contracts and heats until the next fuel ignites or degeneracy "
  "pressure halts contraction. Shell burning (a thin burning layer around an "
  "inert core) makes giants unstable and luminous. Mass loss — winds on the "
  "main sequence, violent shedding as giants, explosive ejection as "
  "supernovae — means the remnant is always lighter than the birth mass. The "
  "demonstration implements the standard initial-to-final mapping: main-"
  "sequence lifetime from the mass-luminosity relation and the remnant type "
  "from initial mass, reproducing the textbook fate table quantitatively."),
 "key_points": [
  "Initial mass decides the entire life story and the final remnant.",
  "0.5-8 M☉ → white dwarf; 8-25 M☉ → neutron star; > 25 M☉ → black hole.",
  "Each burning stage is shorter than the last; silicon burning lasts ~1 day.",
  "Shell burning and mass loss shape giants, nebulae, and remnant masses.",
  "Modern codes (MESA) evolve thousands of shells through all stages."],
 "requirements": [
  "The fusion, HR-diagram, and mass-luminosity records.",
  "Comfort with long causal chains.",
  "No new mathematics."],
 "standards": ["Masses in M☉", "Timescales in Myr/Gyr"],
 "citations": [
  "Paxton, B. et al. (2011). 'Modules for Experiments in Stellar Astrophysics (MESA).' ApJS, 192, 3.",
  CIT_CO],
 "demo_kind": "stevol",
 "sig_lens": (
  "The Signature reading treats stellar evolution as a lifecycle specification "
  "with mass as the single input parameter: birth mass in, remnant out, every "
  "intermediate stage timed. The demo executes that specification across the "
  "mass range and prints the fate table."),
},
{
 "key": "supernovae", "name": "Supernovae: The Deaths of Stars",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Supernovae are stellar explosions that briefly outshine galaxies, and they "
  "come in two fundamentally different kinds. Type Ia supernovae are "
  "thermonuclear: a carbon-oxygen white dwarf, gaining mass from a companion "
  "or merging with one, approaches the Chandrasekhar limit and ignites "
  "runaway carbon fusion that unbinds the entire star — no remnant remains. "
  "Because the exploding mass is always near 1.4 solar masses, their peak "
  "brightness is standardizable (peak absolute magnitude ≈ −19.3), making "
  "them the premier cosmological distance indicators that revealed the "
  "accelerating universe. Core-collapse supernovae (Types II, Ib, Ic) are "
  "gravitational: a massive star's iron core collapses to a neutron star or "
  "black hole in under a second, and the rebounding shock — revived by "
  "neutrinos — ejects the envelope at ~10,000 km/s. They forge and scatter "
  "the heavy elements: the oxygen you breathe and the iron in your blood "
  "were ejected this way. SN 1987A, in the Large Magellanic Cloud, confirmed "
  "the neutrino burst (19 neutrinos caught on Earth) hours before the light "
  "arrived."),
 "how_it_works": (
  "Type Ia light curves are powered by the radioactive decay chain nickel-56 "
  "→ cobalt-56 → iron-56 (half-lives 6 and 77 days): the expanding debris is "
  "heated from within, and the width-luminosity relation (brighter explosions "
  "fade more slowly, because more nickel means more opacity) standardizes "
  "them to ~0.15 magnitude precision. Core collapse begins when the iron core "
  "exceeds ~1.4 M☉: electron captures and photodisintegration remove pressure "
  "support, the core falls at a quarter of light speed, and nuclear density "
  "halts it — the core bounces, launching a shock that stalls until neutrino "
  "heating (about 1% of the 10⁵³ erg neutrino burst coupling to the gas) "
  "revives it. The light we see comes from shock-heated ejecta and later "
  "radioactive decay. The demonstration applies the distance modulus to a "
  "Type Ia supernova, recovering its distance from its apparent magnitude the "
  "way cosmologists do."),
 "key_points": [
  "Type Ia: thermonuclear white-dwarf explosion; standardizable candle (M ≈ −19.3).",
  "Core-collapse: iron-core implosion → neutron star/black hole + ejected envelope.",
  "Supernovae forge and disperse the heavy elements — stellar nucleosynthesis made visible.",
  "SN 1987A's neutrinos confirmed the collapse mechanism before the light arrived.",
  "Type Ia distances revealed cosmic acceleration (1998)."],
 "requirements": [
  "The magnitude-system and stellar-evolution records.",
  "Radioactive decay intuition (half-lives).",
  "No calculus needed."],
 "standards": ["Peak absolute magnitude M ≈ −19.3 (Type Ia)", "Velocities in km/s"],
 "citations": [
  "Baade, W. & Zwicky, F. (1934). 'On Super-Novae.' PNAS, 20, 254-259.",
  "Riess, A. G. et al. (1998). 'Observational Evidence from Supernovae for an Accelerating Universe.' AJ, 116, 1009-1038."],
 "demo_kind": "supernova",
 "sig_lens": (
  "The Signature reading treats each supernova type as a distinct failure "
  "mode with a distinct signature: thermonuclear runaway leaves a "
  "standardizable light curve and no remnant; core collapse leaves a compact "
  "remnant and a neutrino burst. The demo reads the Type Ia standard candle "
  "and converts it to distance."),
},
{
 "key": "rotation-curves", "name": "Galactic Rotation Curves and Dark Matter",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Stars and gas in spiral galaxies orbit far too fast for the visible matter "
  "to hold them: rotation curves stay flat at ~200 km/s out to the visible "
  "edge instead of falling as 1/√r the way Kepler's laws predict for the "
  "observed stars and gas. Vera Rubin and Kent Ford's 1970 measurements of "
  "Andromeda made the discrepancy undeniable. The inference is dark matter — "
  "about five times more mass than all the stars, gas, and dust combined, "
  "forming an extended halo whose gravity supplies the missing pull. It is "
  "invisible because it neither emits nor absorbs light, interacting (so far "
  "as detected) only through gravity — though underground detectors and "
  "colliders hunt for rare non-gravitational interactions. Independent lines "
  "of evidence converge: galaxy-cluster motions (Zwicky, 1933), gravitational "
  "lensing mass maps, the cosmic microwave background's acoustic peaks "
  "(Planck: 26.8% dark matter, 4.9% ordinary matter), and the growth of cosmic "
  "structure, which requires dark matter's gravity to assemble galaxies on "
  "schedule. Whatever it is, it outweighs everything that shines."),
 "how_it_works": (
  "A rotation curve plots orbital speed v(r) versus radius from Doppler "
  "shifts of gas emission lines (21-cm hydrogen in the outer disk, optical "
  "lines inside). Newtonian expectation: v = √(GM(<r)/r) using the luminous "
  "mass profile from starlight plus gas maps. The observed flat curves demand "
  "M(<r) ∝ r — mass growing linearly with radius well beyond the light — the "
  "signature of an extended roughly-isothermal halo. Modelers fit halo "
  "profiles (isothermal spheres, NFW profiles from cosmological simulations) "
  "to the curves; the fits require halo masses ~10¹² M☉ for Milky Way-class "
  "galaxies. The demonstration computes the Newtonian expectation from the "
  "luminous mass alone at large radius, compares it with the observed flat "
  "value, and derives the missing-mass factor — the quantitative gap dark "
  "matter fills."),
 "key_points": [
  "Rotation curves stay flat where Kepler predicts a 1/√r fall — the founding discrepancy.",
  "Dark matter outweighs luminous matter ~5:1 and forms extended halos.",
  "Independent confirmations: clusters, lensing, CMB peaks, structure growth.",
  "It is detected only by gravity so far; its particle nature is unknown.",
  "Fitting halo profiles to curves weighs galaxies' invisible bulk."],
 "requirements": [
  "The Doppler-shift record.",
  "Circular-orbit speed v = √(GM/r).",
  "No calculus needed."],
 "standards": ["Velocities in km/s", "Radii in kpc", "Masses in M☉"],
 "citations": [
  "Rubin, V. C. & Ford, W. K. (1970). 'Rotation of the Andromeda Nebula.' ApJ, 159, 379-403.",
  "Zwicky, F. (1933). 'Die Rotverschiebung von extragalaktischen Nebeln.' Helvetica Physica Acta, 6, 110-127."],
 "demo_kind": "rotation",
 "sig_lens": (
  "The Signature reading treats the rotation curve as a load test the visible "
  "galaxy fails: the measured speeds demand mass the light cannot supply, and "
  "the demo quantifies exactly how much invisible mass the test requires at "
  "each radius."),
},
]
# -------------------------------------------------------------------- ADVANCED
ENTRIES += [
{
 "key": "white-dwarfs", "name": "White Dwarfs and the Chandrasekhar Limit",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A white dwarf is the exposed carbon-oxygen core of a dead Sun-like star: a "
  "solar mass packed into an Earth-sized sphere, with densities around a ton "
  "per cubic centimeter — a teaspoon weighing as much as a car. It shines "
  "only from stored heat, cooling over billions of years. What supports it "
  "against gravity is not pressure from heat but electron degeneracy pressure, "
  "a quantum-mechanical effect: the Pauli exclusion principle forbids "
  "electrons from crowding into the same states, and the resulting resistance "
  "to compression holds the star up even at zero temperature. Subrahmanyan "
  "Chandrasekhar showed in 1931 that degeneracy pressure has a limit: above "
  "1.44 solar masses, electrons become relativistic, the support softens, and "
  "no stable white dwarf can exist — the Chandrasekhar limit. Exceed it and "
  "collapse continues to a neutron star or black hole. The mass-radius "
  "relation is inverted: more massive white dwarfs are smaller (R ∝ M^−1/3), "
  "so adding mass shrinks the star until the limit is reached. Sirius B, the "
  "first white dwarf identified, packs a solar mass into a sphere 0.008 solar "
  "radii across."),
 "how_it_works": (
  "Degeneracy pressure follows from counting quantum states: squeeze N "
  "electrons into volume V and the Fermi momentum grows as (N/V)^1/3; the "
  "pressure scales as the Fermi energy density. For non-relativistic "
  "electrons P ∝ ρ^5/3, which combined with hydrostatic equilibrium gives "
  "stable solutions with R ∝ M^−1/3. But as density rises the electrons' Fermi "
  "energy approaches their rest energy, they become relativistic, and the "
  "equation of state softens to P ∝ ρ^4/3 — the exact scaling at which "
  "gravity wins at all radii, so only one mass (the Chandrasekhar limit, "
  "1.44 M☉ for carbon-oxygen composition) marginally balances. Chandrasekhar "
  "derived this at age 20 on a ship from India to England. Observers weigh "
  "white dwarfs in binaries (Sirius B: 1.02 M☉ from its orbit) and measure "
  "radii from luminosity plus temperature, confirming the inverted "
  "mass-radius relation. The demonstration evaluates the relation and the "
  "density scale, showing why a solar mass in an Earth volume is mandatory, "
  "not optional."),
 "key_points": [
  "Electron degeneracy pressure (Pauli principle) supports white dwarfs without heat.",
  "Chandrasekhar limit: 1.44 M☉ — no stable white dwarf above it.",
  "Inverted mass-radius relation: R ∝ M^−1/3; adding mass shrinks the star.",
  "Densities ~10⁹ kg/m³: a teaspoon weighs tons.",
  "White dwarfs cool over gigayears; the faintest date the galactic disk."],
 "requirements": [
  "The hydrostatic-equilibrium and stellar-evolution records.",
  "The Pauli principle idea (no two electrons share a state).",
  "Power laws; no calculus needed."],
 "standards": ["Masses in M☉", "Radii in km and R☉", "The 1.44 M☉ limit"],
 "citations": [
  "Chandrasekhar, S. (1931). 'The Maximum Mass of Ideal White Dwarfs.' ApJ, 74, 81-82.",
  CIT_CO],
 "demo_kind": "whitedwarf",
 "sig_lens": (
  "The Signature reading treats the Chandrasekhar limit as a certified maximum "
  "rating: 1.44 solar masses, derived from first principles, confirmed by "
  "every white dwarf weighed since. The demo enforces the rating and prints "
  "the inverted mass-radius curve the quantum rules require."),
},
{
 "key": "neutron-stars", "name": "Neutron Stars and Pulsars",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A neutron star is the collapsed core of a massive star: ~1.4 solar masses "
  "crushed into a sphere ~12 km across, with central densities exceeding "
  "nuclear density (~3×10¹⁷ kg/m³) — a teaspoon outweighing a mountain range, "
  "and a sugar-cube of core material outweighing humanity. Gravity is so "
  "extreme that escape velocity reaches ~0.6c and a dropped object hits the "
  "surface at relativistic speed. Support comes from neutron degeneracy "
  "pressure plus repulsive nuclear forces; the Tolman-Oppenheimer-Volkoff "
  "limit (~2-3 M☉, equation-of-state dependent) marks where even that fails "
  "and a black hole forms. Many neutron stars are pulsars: spinning up to "
  "716 times per second, their misaligned magnetic beams sweep past Earth "
  "like lighthouse beacons with atomic-clock regularity — the Hulse-Taylor "
  "binary pulsar's decaying orbit confirmed gravitational-wave energy loss "
  "decades before direct detection. Magnetars, with fields of 10¹⁴-10¹⁵ "
  "gauss, power the most magnetic explosions known short of mergers."),
 "how_it_works": (
  "During core collapse, protons and electrons merge into neutrons "
  "(neutronization), and the inner core — about a solar mass inside 12 km — "
  "halts at nuclear density where the strong force turns repulsive. The "
  "structure follows the Tolman-Oppenheimer-Volkoff equation, general "
  "relativity's version of hydrostatic equilibrium, fed with a nuclear "
  "equation of state that laboratories cannot fully reproduce — neutron-star "
  "radii and maximum masses (the 2.14 M☉ pulsar J0740+6620, weighed by "
  "Shapiro delay) constrain it from the sky instead. Pulsar timing exploits "
  "the spin stability: arrival times of pulses measured to microseconds over "
  "years reveal orbital dynamics, companion masses, and spacetime effects. "
  "The 2017 neutron-star merger GW170817, seen in gravitational waves and "
  "across the spectrum, confirmed mergers forge heavy rapid-neutron-capture "
  "elements (gold, platinum) and cemented multi-messenger astrophysics. The "
  "demonstration computes the density and escape velocity that make neutron "
  "stars the densest stable matter in the universe."),
 "key_points": [
  "1.4 M☉ in 12 km: densities above nuclear density, escape velocity ~0.6c.",
  "Neutron degeneracy + nuclear repulsion support; TOV limit ~2-3 M☉.",
  "Pulsars: lighthouse beams from misaligned rotators, microsecond timing precision.",
  "Binary pulsars confirmed gravitational-wave losses before LIGO.",
  "Mergers (GW170817) forge gold and platinum — multi-messenger confirmed."],
 "requirements": [
  "The white-dwarf record (degeneracy pressure idea).",
  "Density and escape-velocity concepts.",
  "No calculus needed."],
 "standards": ["Densities in kg/m³", "Magnetic fields in gauss", "Masses in M☉"],
 "citations": [
  "Oppenheimer, J. R. & Volkoff, G. M. (1939). 'On Massive Neutron Cores.' Physical Review, 55, 374-381.",
  "Hewish, A. et al. (1968). 'Observation of a Rapidly Pulsating Radio Source.' Nature, 217, 709-713."],
 "demo_kind": "neutronstar",
 "sig_lens": (
  "The Signature reading treats a neutron star as matter pushed to its final "
  "certified state: the density where nuclei dissolve, the spin where "
  "centrifugal breakup looms, the mass where collapse becomes mandatory. The "
  "demo computes those ratings from the measured 12-km scale."),
},
{
 "key": "black-holes-astro", "name": "Black Holes: From Stellar Mass to Supermassive",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "A black hole is a region where mass has collapsed inside its event "
  "horizon — the boundary within which escape requires exceeding light "
  "speed. Stellar-mass black holes (3-100 M☉) are the remnants of the most "
  "massive stars, found in X-ray binaries and by gravitational-wave mergers "
  "(LIGO's detections run from ~3 to ~150 M☉). Supermassive black holes "
  "(10⁶-10¹⁰ M☉) anchor essentially every large galaxy: Sagittarius A*, the "
  "Milky Way's 4.3-million-solar-mass central black hole, was weighed by "
  "tracking stars orbiting the invisible mass (Nobel Prize 2020) and imaged "
  "as a shadow by the Event Horizon Telescope. Between them may lie "
  "intermediate-mass black holes, the missing link. The Schwarzschild radius "
  "r_s = 2GM/c² sets the scale: 3 km per solar mass, so Sgr A* spans 0.08 AU "
  "while M87's 6.5-billion-solar-mass giant spans larger than the solar "
  "system. Black holes grow by accretion and mergers, power quasars when fed, "
  "and shape galaxies through feedback — the mass of the central black hole "
  "correlates tightly with its host galaxy's properties, a fossil record of "
  "co-evolution."),
 "how_it_works": (
  "Karl Schwarzschild found the first exact solution of Einstein's field "
  "equations in 1916: a non-rotating mass M curves spacetime so severely that "
  "inside r_s = 2GM/c² all paths lead inward. Real black holes spin (the Kerr "
  "solution), dragging spacetime and allowing accretion efficiency up to 42%. "
  "Matter spirals in through an accretion disk down to the innermost stable "
  "circular orbit (6GM/c² non-spinning), heating to X-ray temperatures; "
  "inside the ISCO it plunges. Stellar orbits near Sgr A* — S2's 16-year "
  "ellipse with pericenter at 120 AU — give the mass directly from Kepler's "
  "laws applied in strong gravity. The Event Horizon Telescope images the "
  "photon ring: light bent into near-circular orbits at 1.5 r_s, framing the "
  "shadow. Hawking radiation (quantum emission at T ∝ 1/M) is negligible for "
  "astrophysical masses but completes the thermodynamic picture. The "
  "demonstration sizes horizons from stellar to supermassive and computes the "
  "ISCO orbital period at Sgr A* — about half an hour."),
 "key_points": [
  "Event horizon at r_s = 2GM/c²: 3 km per solar mass.",
  "Stellar (3-100 M☉), supermassive (10⁶-10¹⁰ M☉), and candidate intermediate masses.",
  "Sgr A* (4.3×10⁶ M☉) weighed by stellar orbits; imaged by the Event Horizon Telescope.",
  "Accretion disks reach the ISCO; inside it, gas plunges.",
  "Black-hole mass correlates with host-galaxy properties — co-evolution fossil record."],
 "requirements": [
  "The accretion-disk and neutron-star records.",
  "The Schwarzschild-radius idea.",
  "Kepler's third law."],
 "standards": ["Masses in M☉", "Radii in km and AU"],
 "citations": [
  "Schwarzschild, K. (1916). 'Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie.' Sitzungsberichte der Preussischen Akademie der Wissenschaften.",
  "Event Horizon Telescope Collaboration (2019). 'First M87 Event Horizon Telescope Results.' ApJ, 875, L1."],
 "demo_kind": "bh",
 "sig_lens": (
  "The Signature reading treats the event horizon as the ultimate containment "
  "specification: mass in, no signal out, with the horizon radius, ISCO, and "
  "orbital clock all derived from the mass alone. The demo sizes that "
  "specification from a stellar remnant to Sgr A* to M87."),
},
{
 "key": "microlensing", "name": "Gravitational Microlensing: Weighing Invisible Objects",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "When a dark object — a rogue planet, a dim star, a stellar black hole — "
  "drifts across the line of sight to a background star, its gravity acts as "
  "a lens: the background star temporarily brightens and fades in a "
  "characteristic symmetric curve, even though the lens itself emits no "
  "light. This is gravitational microlensing, and it is one of the few ways "
  "to detect and weigh completely dark objects. The Einstein radius sets the "
  "scale: for a half-solar-mass lens halfway to the galactic center it is "
  "under a milliarcsecond, but the magnification can exceed a factor of 100 "
  "for near-perfect alignment. Surveys like OGLE and MOA monitor hundreds of "
  "millions of stars toward the galactic bulge and catch thousands of events "
  "per year; follow-up networks hunt the brief planetary anomalies — hours-"
  "long deviations — that reveal exoplanets, including rogue planets "
  "wandering starless between the stars. In 2022, astrometric microlensing "
  "measured the first isolated stellar-mass black hole's mass (~7 M☉) from "
  "the deflection of the background star's position alone."),
 "how_it_works": (
  "A point lens creates two images of the background source; when unresolved, "
  "their combined magnification follows A(u) = (u²+2)/(u√(u²+4)), where u is "
  "the angular separation in units of the Einstein radius θ_E = "
  "√(4GM/c² · D_ls/(D_l D_s)). The event timescale t_E = θ_E/μ_rel (weeks to "
  "months for stellar lenses) encodes the lens mass, distances, and relative "
  "proper motion in one degenerate combination. Breaking the degeneracy needs "
  "more: parallax from Earth's orbit (or a space telescope) gives a second "
  "viewpoint, and astrometric measurement of the image centroid's looping "
  "motion gives θ_E directly — combined, they yield the lens mass with no "
  "light required. Planetary companions add short spikes to the smooth "
  "stellar curve; modeling the spike gives the planet-to-star mass ratio and "
  "projected separation. The demonstration evaluates θ_E and the event "
  "timescale for a typical bulge event and shows the magnification curve's "
  "symmetric shape."),
 "key_points": [
  "Dark lenses reveal themselves by temporarily magnifying background stars.",
  "θ_E = √(4GM/c² · D_ls/(D_l D_s)): the lensing scale, typically sub-milliarcsecond.",
  "Event timescales (weeks-months) encode mass, distance, and motion degenerately.",
  "Parallax + astrometry break the degeneracy and weigh invisible lenses.",
  "Planetary anomalies (hours-long spikes) find exoplanets, including rogues."],
 "requirements": [
  "The Doppler-shift and magnitude records.",
  "Small-angle geometry.",
  "No calculus needed."],
 "standards": ["Angles in milliarcseconds", "Timescales in days"],
 "citations": [
  "Einstein, A. (1936). 'Lens-Like Action of a Star by the Deviation of Light in the Gravitational Field.' Science, 84, 506-507.",
  "Sahu, K. C. et al. (2022). 'An Isolated Stellar-Mass Black Hole Detected Through Astrometric Microlensing.' ApJ, 933, 83."],
 "demo_kind": "microlens",
 "sig_lens": (
  "The Signature reading treats microlensing as a blind-weighing protocol: no "
  "photon from the lens is ever required, yet mass, distance, and motion are "
  "all recoverable from the light curve plus geometry. The demo executes that "
  "protocol for a canonical bulge event."),
},
{
 "key": "exoplanets", "name": "Exoplanets: The Transit and Radial-Velocity Methods",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Over 5,500 exoplanets are now confirmed, found mostly by two methods. The "
  "transit method watches a star dim by the fraction (R_p/R_★)² when a planet "
  "crosses its disk — 1% for a Jupiter around a Sun-like star, 0.008% (84 "
  "parts per million) for an Earth. Kepler stared at 150,000 stars for four "
  "years and found thousands, revealing that planets are common: most stars "
  "host at least one, compact multi-planet systems are the norm, and hot "
  "Jupiters are the rare exception. The radial-velocity method measures the "
  "star's wobble: a planet tugs its star around their common center of mass, "
  "and the Doppler amplitude K gives M_p sin i (minimum mass). 51 Pegasi b, "
  "the first exoplanet around a Sun-like star (Mayor and Queloz, 1995), "
  "showed K = 55.6 m/s — a half-Jupiter mass whipping around its star in 4.2 "
  "days, a configuration theorists had declared impossible. Together the "
  "methods give mass and radius, hence density and bulk composition; "
  "transmission spectroscopy during transits now probes atmospheres for "
  "water, carbon dioxide, and potential biosignatures."),
 "how_it_works": (
  "Transits require edge-on geometry (probability ~R_★/a, ~10% for hot "
  "Jupiters, ~0.5% for Earth analogs), so transit surveys play a numbers "
  "game: monitor hundreds of thousands of stars, catch the few aligned "
  "systems, and correct statistically for the missed ones. The light curve's "
  "depth gives the radius ratio; its shape gives the orbital inclination and "
  "stellar density. Radial velocity needs spectrographs stable to ~1 m/s "
  "(ESPRESSO reaches ~10 cm/s), calibrated with laser frequency combs; the "
  "velocity semi-amplitude K = (M_p sin i / M_★^2/3) × (2πG/P)^1/3 /√(1−e²). "
  "Combining K (mass) with transit depth (radius) yields density: rocky, "
  "watery, or gaseous. During transit, starlight filtering through the "
  "planet's atmosphere imprints molecular absorption — transmission "
  "spectroscopy — and secondary eclipses (planet passing behind the star) "
  "measure its thermal emission. The demonstration computes transit depths "
  "for Jupiter and Earth analogs and the 51 Pegasi wobble amplitude."),
 "key_points": [
  "Transit depth (R_p/R_★)²: 1% for Jupiter/Sun, 84 ppm for Earth/Sun.",
  "Radial velocity gives M_p sin i; 51 Peg b: K = 55.6 m/s, P = 4.2 days.",
  "Mass + radius → density → bulk composition.",
  "Kepler showed planets are common; compact multis are typical.",
  "Transmission spectroscopy probes atmospheres for water and biosignatures."],
 "requirements": [
  "The Doppler-shift and magnitude records.",
  "Ratios and Kepler's third law.",
  "No calculus needed."],
 "standards": ["Radii in Earth/Jupiter radii", "Masses in Earth/Jupiter masses"],
 "citations": [
  "Mayor, M. & Queloz, D. (1995). 'A Jupiter-mass companion to a solar-type star.' Nature, 378, 355-359.",
  "Borucki, W. J. et al. (2010). 'Kepler Planet-Detection Mission.' Science, 327, 977-980."],
 "demo_kind": "exoplanet",
 "sig_lens": (
  "The Signature reading treats planet detection as a signal-extraction "
  "problem with published sensitivity floors: transit depth in parts per "
  "million, velocity precision in meters per second. The demo checks both "
  "founding detections against those floors."),
},
{
 "key": "cmb", "name": "The Cosmic Microwave Background",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "The cosmic microwave background (CMB) is the afterglow of the Big Bang: "
  "radiation released 380,000 years after the beginning, when the universe "
  "cooled to ~3,000 K and protons captured electrons (recombination), making "
  "the cosmos transparent. Expanded and redshifted by a factor of 1,091 "
  "since, it arrives today as a near-perfect blackbody at 2.7255 K, peaking "
  "at 1.06 mm, bathing every cubic centimeter in ~411 photons — the oldest "
  "light in existence, a baby photograph of the universe. It is uniform to "
  "one part in 100,000, and those tiny temperature ripples are the seeds of "
  "all structure: slightly denser patches that gravity grew into galaxies "
  "and clusters. The ripple pattern's harmonic peaks encode the universe's "
  "contents — Planck's 2020 analysis gives 4.9% ordinary matter, 26.8% dark "
  "matter, 68.3% dark energy, with space flat to 0.2%. Penzias and Wilson's "
  "1965 discovery of the uniform glow (Nobel 1978) and the COBE/FIRAS "
  "measurement of its perfect blackbody spectrum anchor modern cosmology."),
 "how_it_works": (
  "Before recombination the universe was an opaque plasma: photons scattered "
  "off free electrons every instant, coupling matter and radiation into a "
  "single fluid that rang with sound waves — baryon acoustic oscillations — "
  "driven by gravity and resisted by radiation pressure. At recombination the "
  "electrons vanished into atoms, the photons free-streamed, and the sound "
  "horizon froze at ~150 Mpc comoving, imprinting a characteristic angular "
  "scale (~1 degree, the first acoustic peak) that serves as a standard "
  "ruler. Satellites (COBE, WMAP, Planck) map the full sky in microwave "
  "bands, subtract galactic foregrounds (dust, synchrotron), and expand the "
  "temperature map in spherical harmonics; the power spectrum's peak "
  "positions and heights fit the six-parameter ΛCDM model to percent "
  "precision. Polarization of the CMB (E-modes confirmed, primordial B-modes "
  "still hunted) adds an independent channel on early-universe physics. The "
  "demonstration verifies the blackbody peak, photon density, and "
  "recombination temperature from the measured 2.7255 K."),
 "key_points": [
  "2.7255 K blackbody: the Big Bang's afterglow, released at recombination (z ≈ 1090).",
  "~411 photons/cm³ everywhere — the oldest light in existence.",
  "One-part-in-10⁵ ripples are the seeds of all galaxies and clusters.",
  "Acoustic peaks encode contents: 4.9% ordinary, 26.8% dark matter, 68.3% dark energy.",
  "The 1° first peak is a standard ruler confirming spatial flatness."],
 "requirements": [
  "The blackbody and expanding-universe records.",
  "Redshift idea (z ≈ 1090 means 1091× expansion).",
  "No calculus needed."],
 "standards": ["T_CMB = 2.7255 K", "Frequencies in GHz", "z_ls ≈ 1090"],
 "citations": [
  "Penzias, A. A. & Wilson, R. W. (1965). 'A Measurement of Excess Antenna Temperature at 4080 Mc/s.' ApJ, 142, 419-421.",
  "Planck Collaboration (2020). 'Planck 2018 results. VI. Cosmological parameters.' A&A, 641, A6."],
 "demo_kind": "cmb",
 "sig_lens": (
  "The Signature reading treats the CMB as the system's oldest calibration "
  "source: a blackbody measured to 50 parts per million, whose ripple pattern "
  "is the acceptance test every cosmological model must pass. The demo "
  "verifies the calibration numbers from first principles."),
},
{
 "key": "friedmann-expansion", "name": "The Expanding Universe: Hubble's Law and the Friedmann Equations",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "In 1929 Edwin Hubble found that galaxies recede with speeds proportional "
  "to their distances — v = H₀d, with H₀ ≈ 70 km/s/Mpc — the observational "
  "birth of the expanding universe. Space itself stretches: galaxies are "
  "carried apart like raisins in rising dough, and light traveling through "
  "expanding space is redshifted by the expansion factor. The dynamics follow "
  "the Friedmann equations, Alexander Friedmann's 1922 solutions of "
  "Einstein's field equations for a homogeneous, isotropic universe: "
  "H² = (8πG/3)ρ − kc²/a² + Λc²/3. The expansion rate H, the mean density ρ, "
  "the curvature k, and the cosmological constant Λ jointly decide the "
  "universe's fate. The critical density ρ_c = 3H₀²/8πG (≈ 9.2×10⁻²⁷ kg/m³, "
  "about five hydrogen atoms per cubic meter) divides open from closed "
  "geometries; measurements put the actual density at the critical value — "
  "space is flat. The Hubble time 1/H₀ ≈ 14 billion years sets the age scale, "
  "refined to 13.8 Gyr by the full model. Run the expansion backward and "
  "everything converges: a hot, dense beginning 13.8 billion years ago."),
 "how_it_works": (
  "Friedmann derived his equations by inserting the "
  "Friedmann-Lemaître-Robertson-Walker metric — the spacetime of a uniform "
  "expanding universe — into general relativity. The first equation is an "
  "energy balance for the cosmic scale factor a(t): kinetic energy of "
  "expansion versus gravitational binding plus vacuum energy. Dividing "
  "densities by the critical density gives the familiar Ω parameters "
  "(Ω_m ≈ 0.315 matter, Ω_Λ ≈ 0.685 dark energy, Ω_k ≈ 0 curvature). "
  "Observationally, H₀ comes from the distance ladder (Cepheids calibrating "
  "Type Ia supernovae: the SH0ES program) and independently from the CMB "
  "sound horizon (Planck) — the two disagree at ~5σ (73 vs 67 km/s/Mpc), the "
  "'Hubble tension,' cosmology's most-watched anomaly. The demonstration "
  "evaluates the critical density and Hubble time from H₀ = 70 km/s/Mpc and "
  "shows how the Ω parameters must sum to one in a flat universe."),
 "key_points": [
  "v = H₀d: recession speed proportional to distance — space itself expands.",
  "Friedmann equations govern a(t) from density, curvature, and Λ.",
  "Critical density ≈ 5 H atoms/m³ divides open/closed; the universe is flat.",
  "Hubble time 1/H₀ ≈ 14 Gyr sets the age scale (13.8 Gyr in full ΛCDM).",
  "Hubble tension: local (73) vs CMB (67) km/s/Mpc — cosmology's open anomaly."],
 "requirements": [
  "The Doppler-shift record (redshift).",
  "Density and energy-balance intuition.",
  "Algebra; the demo evaluates the equations."],
 "standards": ["H₀ in km/s/Mpc", "Densities in kg/m³ and H atoms/m³"],
 "citations": [
  "Hubble, E. (1929). 'A Relation Between Distance and Radial Velocity Among Extra-Galactic Nebulae.' PNAS, 15, 168-173.",
  "Friedmann, A. (1922). 'Über die Krümmung des Raumes.' Zeitschrift für Physik, 10, 377-386."],
 "demo_kind": "friedmann",
 "sig_lens": (
  "The Signature reading treats the Friedmann equation as the universe's "
  "energy ledger: expansion kinetic against gravity and vacuum, with the Ω "
  "parameters required to balance to unity. The demo posts the entries and "
  "checks the balance."),
},
{
 "key": "dark-energy", "name": "Dark Energy and the Accelerating Universe",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "In 1998 two supernova teams found that distant Type Ia supernovae are "
  "dimmer — hence farther — than a decelerating universe allows: the cosmic "
  "expansion is accelerating, driven by dark energy comprising ~68% of the "
  "universe's energy budget (Nobel Prize 2011). In the standard model it is "
  "the cosmological constant Λ, vacuum energy with negative pressure "
  "(p = −ρc²): unlike matter, whose gravity brakes expansion, vacuum energy's "
  "gravity repels, and because its density stays constant while matter "
  "dilutes, it inevitably comes to dominate — the deceleration parameter "
  "q₀ = Ω_m/2 − Ω_Λ ≈ −0.53 is negative, the mathematical statement that "
  "expansion speeds up. Alternatives include dynamical scalar fields "
  "(quintessence) and modified gravity, distinguished by whether dark "
  "energy's equation of state w = p/ρc² differs from −1 or evolves with time. "
  "The measured value is absurdly small by particle-physics standards "
  "(ρ_Λ ~ 10⁻²⁷ kg/m³, Λ ~ 10⁻⁵² m⁻²) — the worst fine-tuning problem in "
  "physics, 10¹²⁰ off naive quantum estimates. Surveys (DES, Euclid, Rubin) "
  "now map expansion history and structure growth to test whether Λ is truly "
  "constant."),
 "how_it_works": (
  "Acceleration was discovered by fitting the magnitude-redshift relation of "
  "Type Ia supernovae: at z ~ 0.5 the supernovae are ~0.25 magnitudes too "
  "dim for any matter-only model, requiring Ω_Λ ≈ 0.7. The result survived "
  "two decades of scrutiny — calibration, dust, evolution systematics — and "
  "was confirmed independently by the CMB (which demands flatness, hence a "
  "missing 70%) and baryon acoustic oscillations (which trace expansion "
  "history). The deceleration parameter comes from the second Friedmann "
  "equation: ä/a = −(4πG/3)(ρ + 3p/c²) + Λc²/3; with p = −ρc² for vacuum "
  "energy the pressure term flips sign and drives acceleration once Λ "
  "dominates. Measuring w(z) is the current campaign: supernovae, BAO, weak "
  "lensing, and cluster counts each constrain the expansion history, and any "
  "evolution of w away from −1 would overthrow the cosmological constant. "
  "The demonstration computes q₀ from the Planck Ω values and evaluates Λ "
  "from the dark-energy density."),
 "key_points": [
  "1998 supernovae: distant Type Ia too dim → expansion accelerates (Nobel 2011).",
  "Dark energy ≈ 68% of the cosmic budget; Λ has p = −ρc² (negative pressure).",
  "q₀ = Ω_m/2 − Ω_Λ ≈ −0.53 < 0: the acceleration, quantified.",
  "Vacuum-energy density is 10¹²⁰ below naive estimates — physics' worst fine-tuning.",
  "Current surveys test whether w = −1 exactly and forever."],
 "requirements": [
  "The Friedmann-expansion and supernova records.",
  "Pressure and density intuition.",
  "Algebra; the demo evaluates q₀ and Λ."],
 "standards": ["Ω parameters dimensionless", "Λ in m⁻²"],
 "citations": [
  "Riess, A. G. et al. (1998). 'Observational Evidence from Supernovae for an Accelerating Universe.' AJ, 116, 1009-1038.",
  "Perlmutter, S. et al. (1999). 'Measurements of Ω and Λ from 42 High-Redshift Supernovae.' ApJ, 517, 565-586."],
 "demo_kind": "darkenergy",
 "sig_lens": (
  "The Signature reading treats dark energy as an open work order: the "
  "measurements (acceleration, Ω_Λ ≈ 0.685) are certified, the physical "
  "mechanism is not. The demo certifies the numbers and marks the mechanism "
  "as the largest unsolved item in the database."),
},
{
 "key": "agn-quasars", "name": "Active Galactic Nuclei and Quasars",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Some galactic centers blaze with the light of trillions of stars from a "
  "region light-days across: active galactic nuclei (AGN), powered by "
  "supermassive black holes accreting gas at up to solar masses per year. The "
  "most luminous, quasars, reach 10⁴⁷ erg/s — ten thousand times a giant "
  "galaxy — and are visible across the observable universe; 3C 273, the "
  "first identified (Maarten Schmidt, 1963), shines at 2.5 billion light-"
  "years with the light of trillions of suns. The unified model explains the "
  "zoo — Seyferts, radio galaxies, blazars, quasars — as one engine viewed "
  "at different angles and accretion rates: a hot accretion disk, a dusty "
  "torus, and relativistic jets, with blazars aimed at us and radio galaxies "
  "seen side-on. AGN feedback regulates galaxies: quasar winds and radio jets "
  "heat and expel gas, quenching star formation — the mechanism behind the "
  "tight black-hole/galaxy mass correlations. Reverberation mapping (timing "
  "the echo of disk flares in surrounding gas) weighs black holes millions of "
  "light-years away."),
 "how_it_works": (
  "The engine is the accretion disk around a 10⁶-10¹⁰ M☉ black hole: gas "
  "spiraling through the disk heats to 10⁵ K (the 'big blue bump' in the "
  "spectrum), while a hot corona Compton-scatters photons into X-rays and "
  "magnetic fields launch jets at near light speed. Luminosity tracks the "
  "accretion rate via L = ηṀc²; the Eddington ratio λ = L/L_Edd classifies "
  "the mode — near-Eddington quasars versus dim, jet-dominated nuclei. "
  "Orientation unifies the classes: the dusty torus hides the broad-line "
  "region from edge-on views (Type 2 Seyferts, radio galaxies) but not from "
  "face-on views (Type 1, quasars); relativistic beaming makes aligned jets "
  "blazars. Black-hole masses come from stellar/gas dynamics nearby and from "
  "reverberation mapping far away (light-travel time across the broad-line "
  "region gives its radius; line widths give velocities; virial theorem gives "
  "mass). The demonstration computes the Eddington ratio of a luminous quasar "
  "and the accretion rate its luminosity demands."),
 "key_points": [
  "AGN = accreting supermassive black holes; quasars reach 10⁴⁷ erg/s.",
  "Unified model: one engine, many appearances by viewing angle and accretion rate.",
  "Eddington ratio λ = L/L_Edd classifies the accretion mode.",
  "AGN feedback (winds, jets) quenches star formation and co-regulates galaxies.",
  "Reverberation mapping weighs black holes across cosmic distances."],
 "requirements": [
  "The accretion-disk and Eddington-limit records.",
  "The black-hole record.",
  "Ratios; no calculus needed."],
 "standards": ["Luminosities in erg/s", "Accretion rates in M☉/yr"],
 "citations": [
  "Schmidt, M. (1963). '3C 273: A Star-Like Object with Large Red-Shift.' Nature, 197, 1040.",
  "Urry, C. M. & Padovani, P. (1995). 'Unified Schemes for Radio-Loud Active Galactic Nuclei.' PASP, 107, 803."],
 "demo_kind": "agn",
 "sig_lens": (
  "The Signature reading treats an AGN as an engine test stand: fuel rate in "
  "via the Eddington ratio, power out in erg/s, orientation as a viewing "
  "parameter — one machine, many test configurations. The demo runs the stand "
  "at quasar power and checks the fuel accounting."),
},
]
ENTRIES += [
{
 "key": "gamma-ray-bursts", "name": "Gamma-Ray Bursts: The Most Energetic Explosions",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Gamma-ray bursts (GRBs) are the most luminous explosions in the universe: "
  "for seconds to minutes, one outshines everything else in the gamma-ray "
  "sky, releasing ~10⁵³ erg if assumed isotropic — the energy the Sun will "
  "radiate over its entire 10-billion-year life, set free in under a minute. "
  "Long bursts (> 2 s) come from the collapse of rapidly rotating massive "
  "stars (collapsars), confirmed by accompanying supernovae; short bursts "
  "(< 2 s) come from neutron-star mergers, confirmed spectacularly by "
  "GW170817, seen in gravitational waves and then as a short GRB. The "
  "fireball model explains the light: an ultra-relativistic jet (Lorentz "
  "factors of hundreds) launched by the newborn black hole or magnetar "
  "converts kinetic energy to gamma rays in internal shocks, then sweeps up "
  "surrounding gas, producing the fading multi-wavelength afterglow. Because "
  "the emission is beamed into narrow jets, the true energy is ~10⁵¹ erg — "
  "still staggering, collimated like a lighthouse. GRBs are cosmic probes: "
  "their afterglows backlight the intergalactic medium at high redshift, and "
  "their host galaxies trace star formation across cosmic time."),
 "how_it_works": (
  "The central engine — accreting newborn black hole or millisecond magnetar "
  "— launches bipolar jets with bulk Lorentz factors Γ ~ 100-1000. "
  "Variability in the outflow makes faster shells collide with slower ones "
  "(internal shocks), accelerating electrons that radiate synchrotron gamma "
  "rays; the observed millisecond variability implies emitting regions of "
  "~c·δt·Γ². When the jet decelerates against the circumburst medium, the "
  "external shock powers the afterglow, fading as a power law from X-ray to "
  "radio over days to months. The isotropic-equivalent energy E_iso = "
  "4πd_L²S/(1+z) overestimates the true budget; jet breaks in the afterglow "
  "light curve reveal the opening angle θ_j, giving the beaming-corrected "
  "E_γ = E_iso·θ_j²/2. The Amati relation (E_iso vs spectral peak energy) "
  "hints at standardizable physics. The demonstration computes E_iso for a "
  "canonical burst and applies the beaming correction, showing why geometry "
  "dominates the energy ledger."),
 "key_points": [
  "~10⁵³ erg isotropic-equivalent in seconds — the universe's brightest explosions.",
  "Long GRBs: collapsing massive stars; short GRBs: neutron-star mergers (GW170817).",
  "Ultra-relativistic jets (Γ ~ 100-1000); internal shocks make gamma rays, external shocks the afterglow.",
  "Beaming correction (θ_j²/2) brings true energies to ~10⁵¹ erg.",
  "Afterglows backlight the high-redshift intergalactic medium."],
 "requirements": [
  "The supernova and neutron-star records.",
  "Relativistic beaming intuition.",
  "Power laws; no calculus needed."],
 "standards": ["Energies in erg", "Fluences in erg/cm²"],
 "citations": [
  "Klebesadel, R. W., Strong, I. B. & Olson, R. A. (1973). 'Observations of Gamma-Ray Bursts of Cosmic Origin.' ApJ, 182, L85.",
  "Abbott, B. P. et al. (2017). 'GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral.' PRL, 119, 161101."],
 "demo_kind": "grb",
 "sig_lens": (
  "The Signature reading treats a GRB as an energy audit under extreme "
  "beaming: isotropic-equivalent energy is the naive invoice, the jet opening "
  "angle is the correction factor, and only the beaming-corrected number "
  "ships. The demo runs that audit on a canonical burst."),
},
{
 "key": "nucleosynthesis", "name": "Nucleosynthesis: Forging the Elements in Stars",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Every atom heavier than hydrogen in your body was forged in stars or their "
  "deaths. Big Bang nucleosynthesis made hydrogen, helium, and traces of "
  "lithium in the first minutes; everything else is stellar. The 1957 B²FH "
  "paper mapped the factories: hydrogen burning makes helium; the triple-"
  "alpha process (three helium nuclei → carbon-12, via the beryllium-8 "
  "bottleneck and Hoyle's resonant state) makes carbon and oxygen in red "
  "giants; successive burning stages in massive stars climb to silicon and "
  "iron. Iron-56 has the highest binding energy per nucleon (8.8 MeV), so "
  "fusion stops paying there — heavier elements form by neutron capture. The "
  "slow s-process builds elements up to lead in asymptotic giant branch "
  "stars over thousands of years; the rapid r-process, in neutron-star "
  "mergers and supernovae, floods seed nuclei with neutrons in seconds, "
  "making gold, platinum, and uranium before beta decay walks them back to "
  "stability. Stellar winds, planetary nebulae, and supernovae then scatter "
  "the products into the interstellar medium for the next generation — "
  "chemical evolution written across cosmic time."),
 "how_it_works": (
  "The binding-energy-per-nucleon curve dictates the energetics: fusing light "
  "nuclei toward iron-56 releases energy (up to 8.8 MeV/nucleon), while "
  "building beyond iron costs energy and needs neutron captures instead. "
  "The triple-alpha rate hinges on Fred Hoyle's prediction of a 7.65 MeV "
  "resonance in carbon-12 — without it, the universe would have almost no "
  "carbon, and Hoyle predicted it precisely because carbon exists. Reaction "
  "networks in stellar codes track hundreds of isotopes through thousands of "
  "reactions, with rates from laboratory measurements extrapolated to stellar "
  "energies. Abundance patterns test the story: the Sun's composition, "
  "meteoritic isotopic ratios, and metal-poor halo stars (fossils of early "
  "enrichment) all match predictions. GW170817's kilonova light curve, "
  "powered by r-process radioactive decay, confirmed mergers as heavy-element "
  "factories. The demonstration evaluates binding energy per nucleon from "
  "measured nuclear masses and locates iron's peak."),
 "key_points": [
  "B²FH (1957): stars forge every element heavier than helium.",
  "Triple-alpha (via Hoyle's resonance) makes the carbon chemistry needs.",
  "Iron-56 peaks at 8.8 MeV/nucleon — fusion's endpoint.",
  "s-process (AGB stars) and r-process (mergers, supernovae) build the heavy elements.",
  "Winds, nebulae, and supernovae recycle products into the next generation."],
 "requirements": [
  "The fusion and supernova records.",
  "Binding energy intuition.",
  "No calculus needed."],
 "standards": ["Energies in MeV per nucleon", "Isotopes by mass number"],
 "citations": [
  "Burbidge, E. M., Burbidge, G. R., Fowler, W. A. & Hoyle, F. (1957). 'Synthesis of the Elements in Stars.' Reviews of Modern Physics, 29, 547-650.",
  "Hoyle, F. (1954). 'On Nuclear Reactions Occurring in Very Hot Stars.' ApJS, 1, 121-146."],
 "demo_kind": "nucleosynth",
 "sig_lens": (
  "The Signature reading treats nucleosynthesis as a manufacturing ledger: "
  "each stellar factory certified for its product range, iron marked as the "
  "end of the fusion line, neutron captures as the subcontractor for "
  "everything heavier. The demo verifies the ledger's keystone — iron's "
  "binding-energy peak."),
},
{
 "key": "habitable-zone", "name": "The Habitable Zone: Where Liquid Water Can Exist",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The habitable zone (HZ) is the range of orbits where a planet with an "
  "Earth-like atmosphere could sustain liquid water on its surface — the "
  "starting filter in the search for life. Its boundaries scale with the "
  "star's luminosity: d ≈ √(L/L☉) × (0.95-1.67 AU), so the Sun's HZ spans "
  "~0.95-1.67 AU (conservative to optimistic estimates), while dim Proxima "
  "Centauri's (0.0017 L☉) squeezes to ~0.04-0.07 AU — Proxima b orbits at "
  "0.0485 AU, inside it. The inner edge is set by the runaway greenhouse "
  "(oceans evaporate, water vapor traps heat, the planet desiccates — Venus's "
  "fate); the outer edge by the maximum greenhouse (CO₂ condenses out, the "
  "planet freezes — Mars sits near it). But the HZ is necessary, not "
  "sufficient: atmosphere, magnetic shielding, plate tectonics, and a stable "
  "climate all matter, and tidal locking around red dwarfs brings its own "
  "challenges (permanent day/night sides, stellar flares). Dozens of "
  "HZ planets are known; characterizing their atmospheres with JWST and "
  "future direct-imaging missions is the current frontier."),
 "how_it_works": (
  "HZ boundaries come from one-dimensional climate models: place an "
  "Earth-like planet at distance d, compute the stellar flux S = L/4πd², and "
  "find where radiative-convective equilibrium permits liquid water. "
  "Kasting, Whitmire, and Reynolds (1993) set the classic limits; Kopparapu "
  "et al. (2013) updated them with modern radiative transfer — the "
  "conservative HZ (0.95-1.67 AU for the Sun) versus the optimistic "
  "empirical HZ (0.75-1.77 AU, from Venus/Mars history). The √L scaling "
  "follows directly from the inverse-square law at fixed flux. Observers "
  "apply it by combining stellar luminosity (from the Stefan-Boltzmann law "
  "or models) with planet orbital distance (from period via Kepler's third "
  "law). Follow-up prioritizes HZ rocky planets around quiet stars for "
  "transmission spectroscopy: JWST measures atmospheric absorption during "
  "transit, hunting water, CO₂, and potential biosignature gases. The "
  "demonstration computes HZ boundaries for the Sun, Proxima Centauri, and "
  "a luminous A-star, and checks known planets against them."),
 "key_points": [
  "HZ: orbits where an Earth-like planet could hold liquid water; d ∝ √L.",
  "Sun: ~0.95-1.67 AU; Proxima: ~0.04-0.07 AU (Proxima b inside it).",
  "Inner edge: runaway greenhouse (Venus); outer edge: CO₂ condensation (Mars).",
  "Necessary, not sufficient — atmosphere, magnetosphere, and climate all matter.",
  "JWST transmission spectroscopy now probes HZ atmospheres for biosignatures."],
 "requirements": [
  "The Stefan-Boltzmann and exoplanet records.",
  "Inverse-square law.",
  "No calculus needed."],
 "standards": ["Distances in AU", "Fluxes in Earth fluxes (S⊕)"],
 "citations": [
  "Kasting, J. F., Whitmire, D. P. & Reynolds, R. T. (1993). 'Habitable Zones Around Main Sequence Stars.' Icarus, 101, 108-128.",
  "Kopparapu, R. K. et al. (2013). 'Habitable Zones Around Main-Sequence Stars.' ApJ, 765, 131."],
 "demo_kind": "habitable",
 "sig_lens": (
  "The Signature reading treats the habitable zone as a screening filter with "
  "published pass criteria: flux range, not a habitability certificate. The "
  "demo applies the filter to three stellar types and reports which known "
  "planets pass the screen — and what further tests each survivor still owes."),
},
{
 "key": "sed", "name": "Spectral Energy Distributions: Reading a Star's Light",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A spectral energy distribution (SED) is the full accounting of an object's "
  "light across all wavelengths — flux versus wavelength from X-rays to "
  "radio — and it is the richest single diagnostic in observational "
  "astrophysics. A bare star's SED is nearly a blackbody with absorption "
  "lines; add a dusty disk and an infrared excess appears (dust re-radiating "
  "absorbed starlight); add an accretion disk and ultraviolet/X-ray excesses "
  "appear; add a jet and radio synchrotron emission appears. Fitting model "
  "SEDs to multi-wavelength photometry decomposes an object into its "
  "physical components and measures each: stellar temperature and radius "
  "from the optical peak, dust mass and temperature from the infrared bump, "
  "accretion rate from the ultraviolet excess. Galaxy SEDs go further — "
  "stellar-population synthesis models fit the combined light of billions of "
  "stars to recover a galaxy's star-formation history, stellar mass, dust "
  "content, and photometric redshift. The technique is only as good as its "
  "wavelength coverage, which is why modern surveys coordinate from space "
  "ultraviolet to ground-based radio."),
 "how_it_works": (
  "Building an SED means gathering calibrated flux measurements in as many "
  "bands as possible — survey photometry (optical/infrared), targeted "
  "observations (ultraviolet, X-ray, radio) — correcting each for distance "
  "and dust extinction, and plotting λF_λ versus λ (equal area under the "
  "curve means equal energy per logarithmic interval). Model fitting then "
  "minimizes χ² between the data and composite models: stellar atmospheres "
  "(Kurucz/PHOENIX grids), dust emission (modified blackbodies), accretion "
  "disks (multi-temperature blackbodies), and synchrotron power laws. The "
  "integral under the SED is the bolometric luminosity — the total power "
  "across all bands. For the demonstration, a synthetic stellar SED (Planck "
  "function sampled across wavelengths) is integrated numerically with the "
  "trapezoid rule and checked against the analytic Stefan-Boltzmann value, "
  "proving the pipeline conserves energy: what the models emit is what the "
  "detectors must collect."),
 "key_points": [
  "The SED (flux vs wavelength, X-ray to radio) is the richest single diagnostic.",
  "Excesses diagnose components: IR → dust, UV/X-ray → accretion, radio → jets.",
  "Model fitting decomposes objects and measures temperatures, masses, rates.",
  "Galaxy SEDs recover star-formation histories and photometric redshifts.",
  "The SED integral is the bolometric luminosity — energy must balance."],
 "requirements": [
  "The blackbody, spectrum, and magnitude records.",
  "Numerical integration intuition (the demo uses trapezoid rule).",
  "Logarithmic plotting."],
 "standards": ["Fluxes in SI or Jy with conversions", "λF_λ convention noted"],
 "citations": [
  "Kurucz, R. L. (1993). 'Model Atmospheres.' In 'Light on Dark Matter' (ed. F. P. Israel). Springer.",
  CIT_RL],
 "demo_kind": "sed",
 "sig_lens": (
  "The Signature reading treats an SED as a full energy audit: every "
  "wavelength band accounted, the integral required to match the "
  "Stefan-Boltzmann total, discrepancies investigated as missing components "
  "rather than rounding error. The demo runs that audit numerically."),
},
{
 "key": "numerical-astrophysics", "name": "Numerical Astrophysics: Simulating the Universe",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Many astrophysical systems defeat pencil-and-paper analysis — "
  "three-body orbits, turbulent magnetized gas, galaxy collisions, the "
  "growing cosmic web — so astrophysics leans on numerical simulation. "
  "N-body codes integrate gravity for millions to trillions of particles "
  "(the Millennium and IllustrisTNG runs evolved virtual universes that "
  "reproduce the observed galaxy population); hydrodynamics codes solve the "
  "fluid equations on grids or with particles (adaptive mesh refinement zooms "
  "into collapsing cores); magnetohydrodynamics adds magnetic fields; "
  "radiative-transfer modules track the light. Symplectic integrators (like "
  "leapfrog) are prized for orbital dynamics because they conserve energy "
  "over billions of steps instead of drifting. The discipline's rule is "
  "verification and validation: codes are tested against analytic solutions "
  "(a circular orbit must stay circular, a shock tube must match the exact "
  "Riemann solution) before being trusted on the unknown, and results are "
  "checked for resolution convergence — the answer must not change when the "
  "grid is refined. Simulation is now the third pillar of the field alongside "
  "theory and observation."),
 "how_it_works": (
  "An N-body step computes gravitational forces (direct O(N²) summation for "
  "small N; tree codes or particle-mesh for large N, reaching O(N log N)), "
  "then advances positions and velocities. Leapfrog (kick-drift-kick) "
  "updates velocities half a step, positions a full step, velocities half a "
  "step — time-reversible and symplectic, so energy oscillates around the "
  "true value rather than drifting. Hydrodynamics discretizes the Euler "
  "equations: grid codes (FLASH, Athena) use finite-volume Godunov methods "
  "with Riemann solvers at cell faces; particle codes (Gadget's smoothed "
  "particle hydrodynamics) smear fluid quantities over neighbor particles. "
  "Gravity plus gas plus subgrid recipes (star formation, supernova feedback, "
  "black-hole accretion — physics below the resolution limit, parameterized "
  "and calibrated) produce galaxies in cosmological volumes. The "
  "demonstration integrates a circular binary orbit with leapfrog for one "
  "full period and verifies energy conservation and orbital closure — the "
  "canonical verification test every dynamics code must pass."),
 "key_points": [
  "N-body, hydrodynamics, MHD, and radiative transfer cover the physics; subgrid recipes cover the rest.",
  "Leapfrog/symplectic integrators conserve energy over billions of steps.",
  "Tree and particle-mesh methods make million-to-trillion-particle runs feasible.",
  "Verification (analytic tests) and convergence (resolution independence) are mandatory.",
  "Cosmological runs (Millennium, IllustrisTNG) reproduce the observed galaxy population."],
 "requirements": [
  "The hydrostatic-equilibrium record.",
  "Newton's gravity and basic differential-equation intuition.",
  "The demo is the verification test itself."],
 "standards": ["SI units in the demo", "Energy conservation quoted relatively"],
 "citations": [
  "Springel, V. et al. (2005). 'Simulations of the Formation, Evolution and Clustering of Galaxies and Quasars.' Nature, 435, 629-636.",
  "Pillepich, A. et al. (2018). 'Simulating Galaxy Formation with the IllustrisTNG Model.' MNRAS, 473, 4077-4106."],
 "demo_kind": "numerics",
 "sig_lens": (
  "The Signature reading treats a simulation as an instrument requiring "
  "calibration: it must pass its analytic verification tests and demonstrate "
  "convergence before its predictions are admitted as evidence. The demo is "
  "that calibration certificate for orbital dynamics."),
},
]
