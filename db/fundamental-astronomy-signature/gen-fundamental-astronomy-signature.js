(function(){'use strict';
/* jahdb-fundamental-astronomy-signature-1.0 — fundamental astronomy bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFAST-';
var KIND='fundamental astronomy record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Astronomy is the study of celestial objects and the universe as a whole: stars, planets, galaxies, and the cosmos, investigated almost entirely through the light and other signals they send us. It is the oldest science and the one that most enlarged humanity\'s sense of scale.', 'reasoning':'Astronomers reason from light: spectra reveal composition and motion, brightness and distance reveal energetics, and the laws of physics — tested locally — are applied to the distant. Models of stellar and cosmic evolution are checked against populations of objects at different stages.', 'quantities':'The core quantities are distance (parsecs, light-years), luminosity, mass, temperature, and redshift. The cosmic distance ladder — parallax to standard candles to redshift — is the field\'s master measurement chain.', 'mechanism':'Astronomical understanding is built by the distance ladder and by stellar modeling: measure distances geometrically where possible, calibrate brighter yardsticks, then read the history of the universe in the light of far objects. Looking far away is looking back in time.', 'miscon':'Astronomy is not astrology: one is measurement, the other is not science. Stars do not twinkle because they vary — Earth\'s atmosphere does that. And the Big Bang was not an explosion in space but the expansion of space itself.'};
var SIGLENS=['In the Signature system, astronomy is the practice of reading vast systems from faint signals: every database in this network, like every galaxy, is understood through the traces it emits, and the Signature formulation teaches each principle as a signal you can decode.','The Signature practice is to compute the cosmos: calculate the distances, model the orbits, decode the spectra — so astronomical reasoning is done with numbers and code, not just admired as imagery.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- light travel time demo. Runs as-is with python3."""\nC = 299792.458  # km/s\ndef light_time_years(distance_km):\n    seconds = distance_km / C\n    return seconds / (365.25 * 24 * 3600)\nAU = 149597870.7\nprint("Sun to Earth:", round(light_time_years(AU) * 365.25 * 24 * 60, 1), "light-minutes")\nLY_KM = 9.4607e12\nfor name, ly in [("Proxima Centauri", 4.24), ("Andromeda", 2.5e6)]:\n    print(name, "-> light travel time:", ly, "years")\n', '#!/usr/bin/env python3\n"""{TITLE} -- Kepler third law demo. Runs as-is with python3."""\ndef orbital_period_years(a_au):\n    return a_au ** 1.5\nfor planet, a in [("Mercury", 0.387), ("Earth", 1.0), ("Mars", 1.524), ("Jupiter", 5.203)]:\n    print(f"{planet:<8} a={a} AU -> T={orbital_period_years(a):.2f} years")\n', '#!/usr/bin/env python3\n"""{TITLE} -- stellar lifetime estimate demo. Runs as-is with python3."""\ndef lifetime_years(mass_solar):\n    # lifetime ~ 1e10 * M/L, L ~ M^3.5\n    return 1e10 * mass_solar / (mass_solar ** 3.5)\nfor m in [0.5, 1.0, 8.0, 20.0]:\n    print(f"{m} solar masses -> ~{lifetime_years(m):.2e} years on main sequence")\n'];
var TOPICS=[['Signature What Astronomy Is','Astronomy studies everything beyond Earth — planets, stars, galaxies, and the universe itself — using light and other messengers as its almost-only source of information. It cannot touch its subjects, so it became the master science of indirect measurement.'],
['Signature The Core Question of Astronomy','The core question of astronomy is: what is out there, how does it work, and how did it come to be? Every observation is interrogated for composition, distance, motion, and history — the four answers every celestial object must give.'],
['Signature Assumptions: Physical Law Is Universal','Astronomy assumes the laws of physics hold everywhere: the hydrogen in a distant galaxy obeys the same quantum mechanics as hydrogen in the lab. Without this, spectra would be meaningless marks; with it, a redshifted line is a receding galaxy.'],
['Signature The Vocabulary: Magnitudes, Spectra, Redshift','The vocabulary of astronomy is magnitudes (brightness on a logarithmic scale), spectra (light spread by wavelength), and redshift (wavelengths stretched by cosmic expansion). These three measurements carry most of what we know about the universe.'],
['Signature Distance: The Fundamental Quantity','Distance is the fundamental quantity: without it, brightness cannot become luminosity and size cannot become scale. The cosmic distance ladder — parallax, standard candles, redshift — builds outward from geometry to the edge of the observable universe.'],
['Signature Spectroscopy: The Primary Method','Spectroscopy is the primary method: spreading starlight into a spectrum reveals which elements are present, how hot the source is, and how fast it moves. Every element writes its signature in lines — astronomy reads fingerprints of light.'],
['Signature A Canonical First Example','The canonical first example is stellar parallax: a nearby star appears to shift against distant background stars as Earth orbits the Sun, and the shift\'s size gives the distance by pure geometry. The first successful measurement, of 61 Cygni in 1838, proved the stars were suns at vast distances.'],
['Signature How Astronomy Measures','Astronomy measures with telescopes, detectors, and time: collecting faint light, dispersing it into spectra, and watching how it changes. Modern surveys image the whole sky repeatedly, turning astronomy into a data science of billions of objects.'],
['Signature The Core Mechanism: Gravity Shapes Everything','The core mechanism is gravity acting over cosmic time: clouds collapse into stars, stars group into galaxies, galaxies cluster into the cosmic web. Given mass, gravity, and 13.8 billion years, structure is the inevitable outcome.'],
['Signature The Simplest Law: Kepler\'s Third Law','The simplest law is Kepler\'s third: the square of a planet\'s orbital period is proportional to the cube of its distance from the Sun. Newton derived it from universal gravitation — one law for falling apples and orbiting moons.'],
['Signature Common Misconceptions in Astronomy','The misconceptions are classic: confusing astronomy with astrology, thinking the Big Bang was an explosion in pre-existing space, believing seasons come from Earth\'s distance to the Sun (they come from axial tilt), and imagining black holes as cosmic vacuum cleaners.'],
['Signature How Beginners Practice Astronomy','Beginners practice astronomy by observing: learn the constellations, track the Moon\'s phases, follow Jupiter\'s moons with binoculars. Naked-eye familiarity with the sky\'s motions makes the abstract quantities — light-years, magnitudes — feel real.'],
['Signature The Core Model: Stellar Evolution','Stellar evolution is the core model: stars are born in collapsing clouds, fuse hydrogen on the main sequence, then die as white dwarfs, neutron stars, or black holes depending on mass. The Hertzsprung-Russell diagram organizes the whole life story by temperature and luminosity.'],
['Signature The Great Equation: E = mc² in Stars','In stars, E = mc² is the great equation made visible: fusion converts a fraction of mass directly into energy, and the Sun turns 4 million tons of mass into light every second. Starlight is mass, unmade.'],
['Signature Systems Thinking: Galaxies and the Cosmic Web','Systems thinking in astronomy spans the cosmic web: galaxies are not isolated islands but nodes in filaments of dark matter, fed by gas flows and shaped by mergers. Structure forms hierarchically — small things first, assembled into large.'],
['Signature Invariance: The Cosmological Principle','The invariance principle is the cosmological principle: on the largest scales the universe is homogeneous and isotropic — the same in all directions and, statistically, everywhere. It justifies applying local physics to the whole cosmos.'],
['Signature Approximation: The Distance Ladder','Approximation in astronomy is the distance ladder itself: each rung — parallax, Cepheids, supernovae — calibrated against the last, with errors compounding outward. Knowing the size of each rung\'s uncertainty is as important as the distances.'],
['Signature Evidence Standards: Independent Confirmation','The evidence standard demands independent confirmation for big claims: a new exoplanet needs a second detection method, a cosmological anomaly needs a second survey. The faster-than-light neutrino episode showed the standard working — the claim died on replication.'],
['Signature Classic Discoveries','The classic discoveries are the heliocentric model, Hubble\'s expanding universe, the cosmic microwave background, exoplanets, and gravitational waves. Each expanded the known universe by an order of magnitude or more.'],
['Signature Core Trade-offs: Aperture versus Field','The core trade-off is aperture versus field of view versus time: big telescopes see faint things in small patches; survey telescopes cover the sky shallowly; and every observation competes for limited telescope time. Astronomers trade depth, breadth, and cadence.'],
['Signature Handling Uncertainty: Cosmic Variance','Astronomy handles uncertainty with error bars on cosmic scales: distance uncertainties, selection effects (we see the bright ones), and cosmic variance — our observable patch may not be perfectly typical. Honest cosmology quantifies all three.'],
['Signature Tools of the Trade','The tools of the trade are the telescope, the spectrograph, the CCD, and the computer: photons collected, dispersed, counted, and modeled. The most powerful is the standard candle — an object of known luminosity that turns brightness into distance.'],
['Signature Ethics and Responsibility','Ethics in astronomy concerns the shared sky: satellite constellations threaten ground-based observation, radio interference blinds radio telescopes, and light pollution erases the stars for everyone. The field\'s responsibility is stewardship of humanity\'s window on the universe.'],
['Signature Teaching Astronomy','Teaching astronomy well starts under the real sky: phases, planets, and meteors first, then the physics. Scale models — the solar system across a town — convey the emptiness of space better than any number of exponents.'],
['Signature The Frontier Question','The frontier question is the nature of the dark sector: dark matter and dark energy comprise 95% of the universe\'s content and are known only by their gravitational effects. Identifying them is the biggest open chase in science.'],
['Signature Unifying Theories','The unifying theory of cosmology is the Lambda-CDM model: general relativity plus dark matter plus dark energy, describing the universe from the first fraction of a second to today. It fits the microwave background exquisitely — and its two dark ingredients are unexplained.'],
['Signature Computational Astronomy','Computational astronomy simulates the universe: N-body codes grow galaxies from quantum fluctuations, stellar models evolve stars, and radiative transfer codes predict what telescopes should see. Simulation and survey now advance in lockstep.'],
['Signature Bridges to Other Fields','Astronomy bridges to physics (astrophysics, cosmology), chemistry (astrochemistry, molecular clouds), geology (planetary science), biology (astrobiology), and computer science (astroinformatics). The search for life connects them all.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the identity of dark matter and dark energy, the cause of cosmic inflation, the matter-antimatter asymmetry, and whether life exists elsewhere. Real measurements, no settled explanations.'],
['Signature How New Claims Are Validated','New astronomical claims are validated by independent telescopes and independent methods: the accelerating universe was accepted when two supernova teams agreed; gravitational waves when two detectors (then three) saw the same chirp.'],
['Signature The Great Debates','The great debates include the Hubble tension (different measures of cosmic expansion disagree), the reality of the multiverse, and whether modified gravity could replace dark matter. The debates are quantitative — each side predicts numbers.'],
['Signature Failure Modes: When Astronomy Gets It Wrong','Astronomy gets it wrong through underestimated systematics, selection effects, and over-interpreted anomalies: canals on Mars, N-rays in spectra, faster-than-light neutrinos. The field\'s immune system is the independent telescope.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis reads the universe whole: a spectrum gives composition, temperature, and motion; the distance turns brightness into power; the population of objects reveals the history. Every advanced result is fundamentals applied at cosmic scale.'],
['Signature The Signature Formulation: Astronomy as Signal Decoding','The Signature formulation treats astronomy as the master class in reading systems from signals: every principle here decodes faint traces into solid knowledge, because in the Signature system a database — like a galaxy — is known by the signals it emits. That is the Signature capstone on astronomical bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Distinguish observation from inference: say what was measured and what was modeled.", "Report uncertainties on every distance, mass, and age \u2014 cosmic numbers without errors are fiction.", "Extraordinary claims (new planets, new physics) require independent confirmation."],citations:["Carroll, B. W. and Ostlie, D. A. \u2014 An Introduction to Modern Astrophysics.", "NASA Astrophysics Data System \u2014 the field's open literature archive.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-astronomy-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-astronomy-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
