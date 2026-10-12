(function(){'use strict';
/* JAH Quarks Subatomic Database generator — jahdb-quarks-subatomic-1.0.
   Property of Justin Addam Higgins (JAH).
   Universal catalog of what subatomic particles do: quarks, leptons, bosons,
   hadrons — confinement, hadronization, decay, pair production/annihilation,
   scattering, CP violation, neutrino oscillation, Higgs interaction, color
   dynamics, asymptotic freedom, electroweak processes, quark–gluon plasma —
   across environments from the void to black-hole singularity to the Big Bang,
   with energy, speed, and field as reaction factors.
   KNOWN findings = established Standard Model physics (Type 1, factual only — never invented).
   SPECULATIVE findings = beyond-Standard-Model theory, ALWAYS labeled SPECULATIVE
   (Type 2, Signature-authored). The two are never mixed.
   Deterministic: same seed always makes the same record.
   generateIndexed(seed) walks the particle-pair×phenomenon×environment space systematically.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-QRK-';
var PT=[
 'u','d','s','c','b','t',
 'ubar','dbar','sbar','cbar','bbar','tbar',
 'e-','mu-','tau-','nue','numu','nutau',
 'gamma','g','W+','W-','Z0','H',
 'p','n','pi+','pi-','pi0','K+','K-','J/psi','phi','D0','B0','Lambda0','Sigma+','Delta++'
];
var PNAME={'u':'up quark','d':'down quark','s':'strange quark','c':'charm quark','b':'bottom quark','t':'top quark',
 'ubar':'anti-up quark','dbar':'anti-down quark','sbar':'anti-strange quark','cbar':'anti-charm quark','bbar':'anti-bottom quark','tbar':'anti-top quark',
 'e-':'electron','mu-':'muon','tau-':'tau lepton','nue':'electron neutrino','numu':'muon neutrino','nutau':'tau neutrino',
 'gamma':'photon','g':'gluon','W+':'W+ boson','W-':'W- boson','Z0':'Z boson','H':'Higgs boson',
 'p':'proton','n':'neutron','pi+':'pion+','pi-':'pion-','pi0':'pion0','K+':'kaon+','K-':'kaon-','J/psi':'J/psi meson','phi':'phi meson','D0':'D0 meson','B0':'B0 meson','Lambda0':'Lambda baryon','Sigma+':'Sigma+ baryon','Delta++':'Delta++ baryon'};
var ENVS=[
 {g:'deep-void',t:'Deep Void',known:[
  'At ~2.7 K and near-zero pressure, free particles are rare; cosmic rays are the main visitors — mostly protons and helium nuclei.',
  'Neutrinos from the Big Bang (the cosmic neutrino background, ~1.95 K) stream through the void unimpeded.',
  'Quantum fluctuations briefly create particle–antiparticle pairs even in vacuum — the Casimir effect confirms vacuum energy is real.'],
  spec:['SPECULATIVE: virtual particles might occasionally tunnel into real ones near cosmic voids — no evidence exists.'],
  temp:'2.7 K',press:'~0 Pa (near-perfect vacuum)',grav:'~0 g',rad:'cosmic microwave background only'},
 {g:'interstellar',t:'Interstellar Medium',known:[
  'Cosmic-ray protons (up to 10²⁰ eV) collide with interstellar gas, producing pions that decay to muons, electrons, and neutrinos.',
  'Supernova remnants accelerate particles via diffusive shock acceleration — the leading explanation for galactic cosmic rays.',
  'Antimatter positrons detected by AMS-02 on the ISS may come from pulsars or dark-matter annihilation — source disputed.'],
  spec:['SPECULATIVE: strangelets (stable strange-quark matter) might travel as cosmic rays — searched for, never found.'],
  temp:'10–10,000 K',press:'~10⁻¹³ Pa',grav:'~0 g',rad:'cosmic rays + starlight'},
 {g:'planetary',t:'Planetary Surface',known:[
  'Cosmic-ray muons (~1 per cm² per minute at sea level) are detected in every basement — time-dilated survivors of pion decay.',
  'Natural radioactivity: K-40 beta decay in bananas, U-238 chains in granite — subatomic processes in ordinary rock.',
  'The 2015 Daya Bay experiment measured neutrino oscillation parameters with reactor antineutrinos on Earth.'],
  spec:['SPECULATIVE: no planetary-surface speculation needed — this is the measured regime; tabletop beyond-Standard-Model searches continue.'],
  temp:'~288 K',press:'101,325 Pa (1 atm)',grav:'1 g',rad:'sunlight + background radiation'},
 {g:'stellar-core',t:'Stellar Core',known:[
  'Sun core (~15 million K): proton–proton fusion — 4p → He-4 + 2e⁺ + 2νe — powered by weak-interaction beta-plus decay.',
  'Neutrinos escape the Sun in ~2 seconds; the 2002 SNO experiment proved they change flavor en route (neutrino oscillation).',
  'Electron capture in collapsing cores turns protons into neutrons — the trigger of core-collapse supernovae.'],
  spec:['SPECULATIVE: axions produced in stellar cores could drain extra energy — stellar cooling bounds constrain but do not rule them out.'],
  temp:'1.5×10⁷ K',press:'~2.5×10¹⁶ Pa',grav:'~28 g (Sun)',rad:'gamma photons trapped, diffusing outward'},
 {g:'supernova-shock',t:'Supernova Shockwave',known:[
  'The 1987A supernova delivered 24 detected neutrinos — confirming core collapse releases ~10⁵⁸ neutrinos in seconds.',
  'Neutrino-driven winds in the explosion forge elements heavier than iron via rapid neutron capture.',
  'Shock acceleration in remnants boosts protons to PeV energies — galactic cosmic-ray factories.'],
  spec:['SPECULATIVE: a quark-matter phase transition in the collapsing core could trigger a second shock — simulated, unobserved.'],
  temp:'~10¹⁰ K',press:'extreme, transient',grav:'collapsing',rad:'neutrino flood + gamma burst'},
 {g:'neutron-star',t:'Neutron Star',known:[
  'A teaspoon of neutron-star matter weighs ~10⁹ tons; neutrons are packed at nuclear density (~10¹⁷ kg/m³).',
  'Beta equilibrium: neutrons ↔ protons + electrons + antineutrinos — weak interactions set the composition.',
  'Pulsar glitches reveal a superfluid neutron interior coupled to the crust.'],
  spec:['SPECULATIVE: the inner core may be deconfined quark matter — the equation of state is unknown; gravitational-wave data is narrowing it.'],
  temp:'10⁶ K surface, hotter inside',press:'beyond laboratory scale',grav:'~2×10¹¹ g',rad:'X-ray pulses'},
 {g:'black-hole-singularity',t:'Black Hole Singularity',known:[
  'Hawking radiation: black holes emit particles via quantum effects at the horizon — temperature inversely proportional to mass.',
  'No-hair theorem: a black hole is described by mass, charge, spin — infalling particle identity is erased from outside view.',
  'The information paradox (does infalling quantum information survive?) remains unresolved after 50 years.'],
  spec:['SPECULATIVE: the firewall hypothesis says the horizon burns infalling particles — contradicts smooth general relativity; debated.',
   'SPECULATIVE: loop quantum gravity replaces the singularity with a bounce into a white hole — untestable with current instruments.'],
  temp:'undefined by known theory',press:'undefined by known theory',grav:'beyond general relativity',rad:'Hawking radiation (theoretical)'},
 {g:'big-bang',t:'Big Bang — Early Universe',known:[
  'At 10⁻⁶ s the universe was quark–gluon plasma; RHIC and LHC recreate it — a near-perfect fluid, the hottest matter ever made.',
  'Electroweak symmetry broke at ~10⁻¹² s, giving particles mass via the Higgs field (confirmed 2012 at the LHC).',
  'Big Bang nucleosynthesis (first 3 minutes) fused protons and neutrons into He-4 — observed abundances match prediction.'],
  spec:['SPECULATIVE: the Planck era needs quantum gravity; inflation, GUT symmetry breaking, and the origin of matter–antimatter asymmetry are all unproven.'],
  temp:'10¹⁰–10³² K (era-dependent)',press:'cosmological',grav:'cosmological expansion',rad:'primordial photon bath'}
];
var PHENS=[
 {g:'quark-confinement',t:'Quark Confinement',known:[
  'No free quark has ever been observed — quarks are permanently bound inside hadrons by the strong force.',
  'Pulling quarks apart creates new quark–antiquark pairs from the vacuum instead of freeing them (string breaking).',
  'Lattice QCD calculations reproduce hadron masses from confinement dynamics — a triumph of the Standard Model.'],
  spec:['SPECULATIVE: magnetic monopoles, if they exist, might confine differently — searched for since 1982, never found.']},
 {g:'hadronization',t:'Hadronization',known:[
  'In colliders, a struck quark showers into a jet of hadrons — observed as collimated sprays in detectors.',
  'Fragmentation functions measured at LEP describe how quarks dress themselves into pions, kaons, and protons.',
  'Heavy quarks (charm, bottom) hadronize before decaying — D and B mesons carry the original quark flavor.'],
  spec:['SPECULATIVE: hadronization in the quark–gluon plasma may differ from vacuum fragmentation — heavy-ion data is still being interpreted.']},
 {g:'particle-decay',t:'Particle Decay',known:[
  'Free neutrons decay in ~880 s: n → p + e⁻ + anti-νe — the weak interaction changing quark flavor (d → u).',
  'The top quark decays in ~10⁻²⁵ s, before it can hadronize — the only quark observed "bare".',
  'Muon decay (μ⁻ → e⁻ + anti-νe + νμ, 2.2 μs) was the first weak decay studied in detail.'],
  spec:['SPECULATIVE: proton decay (p → e⁺ + π⁰) is predicted by grand unified theories; Super-Kamiokande sets half-life > 10³⁴ years.']},
 {g:'pair-production',t:'Pair Production',known:[
  'A photon above 1.022 MeV near a nucleus converts to electron–positron pairs — routine in detectors and astrophysics.',
  'The LHC creates top–antitop pairs from gluon fusion — the heaviest particle pairs ever produced.',
  'Dirac predicted antimatter from his equation in 1928; the positron was found in 1932.'],
  spec:['SPECULATIVE: dark-matter annihilation into particle pairs is the leading indirect-detection signal — searched for, not seen.']},
 {g:'annihilation',t:'Annihilation',known:[
  'Electron–positron annihilation yields two 511 keV photons — the brightest gamma line in the galaxy, mapped by INTEGRAL.',
  'Proton–antiproton annihilation at rest produces ~5 pions on average — measured precisely at LEAR/CERN.',
  'PET medical scanners image the body using positron annihilation.'],
  spec:['SPECULATIVE: why the universe kept matter over antimatter (baryogenesis) is unsolved — Sakharov conditions are necessary but no mechanism is confirmed.']},
 {g:'scattering',t:'Scattering',known:[
  'Rutherford scattering (1909) revealed the nucleus; deep-inelastic scattering (1968) revealed quarks inside it.',
  'The LHC collides protons at 13.6 TeV; scattering cross-sections test the Standard Model to exquisite precision.',
  'Neutrino–electron scattering measured the weak mixing angle — a cornerstone electroweak test.'],
  spec:['SPECULATIVE: scattering at 100 TeV (a future collider) could reveal compositeness — no deviation seen yet at LHC energies.']},
 {g:'cp-violation',t:'CP Violation',known:[
  'Cronin and Fitch (1964) found kaons violating CP symmetry — the first crack in matter–antimatter symmetry.',
  'B-meson factories (BaBar, Belle) measured CP violation in B decays, confirming the CKM mechanism — Nobel 2008.',
  'CP violation in the Standard Model is far too small to explain the universe’s matter excess.'],
  spec:['SPECULATIVE: CP violation in neutrino oscillations (DUNE, Hyper-Kamiokande will probe) might explain baryogenesis via leptogenesis.']},
 {g:'neutrino-oscillation',t:'Neutrino Oscillation',known:[
  'Neutrinos change flavor in flight — proven by Super-Kamiokande (1998, atmospheric) and SNO (2002, solar). Nobel 2015.',
  'Oscillation requires nonzero neutrino mass — the first confirmed physics beyond the original Standard Model.',
  'Reactor experiments (Daya Bay, RENO) pinned down the mixing angle θ₁₃.'],
  spec:['SPECULATIVE: sterile neutrinos (a fourth flavor) are hinted by anomalies (LSND, MiniBooNE) but unconfirmed — hotly debated.']},
 {g:'higgs-interaction',t:'Higgs Interaction',known:[
  'The Higgs boson (125 GeV) was discovered at the LHC in 2012 — the quantum of the field giving particles mass. Nobel 2013.',
  'Higgs couplings to W, Z, tau, bottom, and top match Standard Model predictions within current precision.',
  'Without the Higgs field, electrons would be massless and atoms could not exist.'],
  spec:['SPECULATIVE: the Higgs may be composite, or one of several Higgs bosons (supersymmetry predicts five) — LHC data still allows room.']},
 {g:'color-charge-dynamics',t:'Color Charge Dynamics',known:[
  'Quarks carry red, green, or blue color charge; gluons carry color–anticolor — the strong force is a color interaction.',
  'Only color-neutral combinations exist freely: baryons (rgb) and mesons (color–anticolor).',
  'Eight gluons mediate the force; unlike photons, gluons interact with each other — making QCD nonlinear.'],
  spec:['SPECULATIVE: glueballs (bound states of pure gluons) are predicted by QCD but no confirmed observation exists.']},
 {g:'asymptotic-freedom',t:'Asymptotic Freedom',known:[
  'At high energies quarks behave almost free — Gross, Politzer, Wilczek showed the strong force weakens at short distances. Nobel 2004.',
  'This is why deep-inelastic scattering sees pointlike quarks inside the proton.',
  'At low energies the force grows — the flip side that causes confinement.'],
  spec:['SPECULATIVE: whether a similar freedom/confinement duality hides in other forces is an open theoretical question.']},
 {g:'electroweak-process',t:'Electroweak Processes',known:[
  'Beta decay (d → u + W⁻) unites electromagnetism and the weak force — Glashow, Salam, Weinberg. Nobel 1979.',
  'The W and Z bosons (80 and 91 GeV) were discovered at CERN in 1983 — direct proof of electroweak unification.',
  'Neutral currents (Z exchange) were found in 1973 at Gargamelle — the electroweak theory’s first triumph.'],
  spec:['SPECULATIVE: at ~10¹⁶ GeV the electroweak and strong forces may unify (GUT scale) — far beyond experimental reach.']},
 {g:'quark-gluon-plasma',t:'Quark–Gluon Plasma',known:[
  'RHIC (2005) and LHC recreate the universe’s first microseconds — a near-perfect fluid, not the predicted gas.',
  'Jet quenching: fast quarks lose energy plowing through the plasma — measured via suppressed high-momentum hadrons.',
  'The plasma’s temperature (~10¹² K) is the hottest matter ever created in a laboratory.'],
  spec:['SPECULATIVE: the plasma may have existed in neutron-star mergers — gravitational-wave signatures are being modeled.']},
 {g:'flavor-changing',t:'Flavor-Changing Processes',known:[
  'Strange particles decay via flavor change (s → u): the kaon’s long life revealed the weak interaction’s flavor rules.',
  'B_s mixing (particle ↔ antiparticle oscillation) was measured at the Tevatron — a precision CKM test.',
  'Top quarks decay ~100% to W + bottom — flavor change is the top’s only exit.'],
  spec:['SPECULATIVE: charged-lepton flavor violation (μ → eγ) is forbidden in the Standard Model; any sighting means new physics — intensely searched for.']},
 {g:'virtual-particles',t:'Virtual Particles',known:[
  'The Lamb shift (1947): virtual photons shift hydrogen’s energy levels — measured to parts per billion.',
  'The electron’s magnetic moment matches theory including virtual-particle loops to 12 decimal places — physics’ most precise prediction.',
  'The Casimir effect: virtual particles push metal plates together in vacuum — measured.'],
  spec:['SPECULATIVE: whether virtual particles "exist" or are just calculational tools is a philosophical debate among physicists.']},
 {g:'multi-particle-event',t:'Multi-Particle Events',known:[
  'A single LHC collision can produce hundreds of particles — tracked individually by silicon detectors.',
  'Cosmic-ray air showers cascade into billions of secondaries across kilometers of atmosphere.',
  'Heavy-ion collisions at the LHC create ~20,000 particles per event — a droplet of quark–gluon plasma.'],
  spec:['SPECULATIVE: microscopic black holes in multi-TeV collisions were predicted by extra-dimension models — LHC saw none.']}
];
var ENERGIES=['thermal meV scale','keV X-ray scale','MeV nuclear scale','GeV collider scale','TeV LHC scale','PeV cosmic-ray scale'];
var SPEEDS=['at rest (~0 m/s)','thermal drift (~10² m/s)','relativistic 0.1c','relativistic 0.99c','ultra-relativistic (LHC beam)'];
var FIELDS=['no external field','magnetic field (1 T)','strong magnetic field (magnetar-like)','electric field gradient','color field background'];
function buildRec(seed,envKey,phenKey,pa,pb,en,va,fi,topic){
  var e=null,p=null,i;
  for(i=0;i<ENVS.length;i++)if(ENVS[i].g===envKey)e=ENVS[i];
  for(i=0;i<PHENS.length;i++)if(PHENS[i].g===phenKey)p=PHENS[i];
  if(!e||!p)return null;
  var n=PT.length;
  pa=((pa%n)+n)%n; pb=((pb%n)+n)%n;
  en=((en%6)+6)%6; va=((va%5)+5)%5; fi=((fi%5)+5)%5;
  var parts=[PT[pa],PT[pb]];
  var mixLabel=parts.map(function(x){return PNAME[x]||x;}).join(' × ');
  var kn=[p.known[seed%p.known.length],e.known[(seed>>2)%e.known.length]];
  var sp=[p.spec[(seed>>1)%p.spec.length],e.spec[(seed>>3)%e.spec.length]];
  var title=p.t+': '+mixLabel+' — '+e.t;
  var desc='A full subatomic-phenomenon record: '+p.t.toLowerCase()+' involving '+mixLabel+' under '+e.t.toLowerCase()+' conditions. Energy scale: '+ENERGIES[en]+'; speed: '+SPEEDS[va]+'; field: '+FIELDS[fi]+'. Known Standard Model physics and clearly-labeled beyond-Standard-Model speculation are kept strictly separate — nothing is invented as fact.';
  var demo=null;
  if(phenKey==='particle-decay')demo={kind:'decay-calc',program:'function remaining(halfLife,t){return Math.pow(0.5,t/halfLife);} // fraction left after time t\nconsole.log(remaining(880,1760).toFixed(3)); // free neutron after 2 half-lives = 0.250',note:'Runnable: decay fraction (free neutron, 880 s half-life).'};
  else if(phenKey==='pair-production')demo={kind:'pair-threshold',program:'function pairThresholdMeV(){return 2*0.511;} // e+e- pair needs 2 electron masses\nconsole.log(pairThresholdMeV().toFixed(3)); // 1.022 MeV',note:'Runnable: minimum photon energy for electron–positron pair production.'};
  else if(phenKey==='annihilation')demo={kind:'annihilation-energy',program:'function eMeV(massMeV){return 2*massMeV;} // two photons share 2mc^2\nconsole.log(eMeV(0.511).toFixed(3)); // e+e- annihilation = 1.022 MeV',note:'Runnable: total photon energy from annihilation.'};
  else if(phenKey==='quark-gluon-plasma')demo={kind:'qgp-temp',program:'function qgpKelvin(){return 2e12;} // ~2 trillion K transition temperature\nconsole.log((qgpKelvin()/1.5e7).toExponential(2)); // × hotter than the Sun core',note:'Runnable: QGP temperature vs Sun core.'};
  else if(phenKey==='neutrino-oscillation')demo={kind:'osc-length',program:'function oscKm(dm2,eV){return 2.48*eV/dm2;} // vacuum oscillation length in km\nconsole.log(oscKm(2.5e-3,1000).toExponential(2)); // ~1 GeV atmospheric neutrino',note:'Runnable: oscillation length L=2.48·E/Δm².'};
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:title,description:desc,
    environment:envKey,phenomenon:phenKey,
    particles:parts,particle_names:parts.map(function(x){return PNAME[x]||x;}),
    reaction_factors:{energy:ENERGIES[en],speed:SPEEDS[va],field:FIELDS[fi],temperature:e.temp,pressure:e.press},
    environment_factor:{temperature:e.temp,pressure:e.press,gravity:e.grav,radiation:e.rad},
    known_findings:kn,speculative_findings:sp,
    type:'subatomic phenomenon record',
    content:{phenomenon:p.t,particles:parts,particle_names:parts.map(function(x){return PNAME[x]||x;}),
      environment:e.t,
      reaction_factors:{energy:ENERGIES[en],speed:SPEEDS[va],field:FIELDS[fi]},
      known_findings:kn,speculative_findings:sp,
      note:'KNOWN = established Standard Model physics (Type 1, factual). SPECULATIVE = beyond-Standard-Model theory, always labeled (Type 2, Signature-authored).'},
    demo:demo,src:'signature',_seed:seed,topic:topic||undefined};
}
function normEnv(x){if(!x)return null;var t=String(x).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');for(var i=0;i<ENVS.length;i++){if(ENVS[i].g===t||ENVS[i].g.indexOf(t)>=0||t.indexOf(ENVS[i].g)>=0)return ENVS[i].g;}return null;}
function normPhen(x){if(!x)return null;var t=String(x).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');for(var i=0;i<PHENS.length;i++){if(PHENS[i].g===t||PHENS[i].g.indexOf(t)>=0||t.indexOf(PHENS[i].g)>=0)return PHENS[i].g;}return null;}
function ptIdx(sym){var s=String(sym).trim().toLowerCase();for(var i=0;i<PT.length;i++)if(PT[i].toLowerCase()===s)return i;return -1;}
/* Indexed: walks the full pair×phenomenon×environment×energy×speed×field space systematically.
   Total indexed space = 8 env × 16 phen × 1444 pairs × 6 energies × 5 speeds × 5 fields = 27,724,800 records. */
var NPT=PT.length, PAIRS=NPT*NPT;
function decompose(seed){
  var s=seed-1;
  var env=s%8; s=(s/8)|0;
  var phen=s%16; s=(s/16)|0;
  var pair=s%PAIRS; s=(s/PAIRS)|0;
  var en=s%6; s=(s/6)|0;
  var va=s%5; s=(s/5)|0;
  var fi=s%5;
  return {env:env,phen:phen,pa:(pair/NPT)|0,pb:pair%NPT,en:en,va:va,fi:fi};
}
function generateIndexed(seed){var d=decompose(seed);return buildRec(seed,ENVS[d.env].g,PHENS[d.phen].g,d.pa,d.pb,d.en,d.va,d.fi,null);}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120);
  var env=normEnv(opts.environment)||ENVS[(rnd()*ENVS.length)|0].g;
  var phen=normPhen(opts.phenomenon)||PHENS[(rnd()*PHENS.length)|0].g;
  var pa,pb;
  if(opts.particles&&opts.particles.length>=2){pa=ptIdx(opts.particles[0]);pb=ptIdx(opts.particles[1]);if(pa<0)pa=(rnd()*NPT)|0;if(pb<0)pb=(rnd()*NPT)|0;}
  else{pa=(rnd()*NPT)|0;pb=(rnd()*NPT)|0;}
  var en=(rnd()*6)|0, va=(rnd()*5)|0, fi=(rnd()*5)|0;
  return buildRec(seed,env,phen,pa,pb,en,va,fi,topic||null);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-QRK-\d{6,8}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  var okE=false,okP=false,i;
  for(i=0;i<ENVS.length;i++)if(ENVS[i].g===r.environment)okE=true;
  for(i=0;i<PHENS.length;i++)if(PHENS[i].g===r.phenomenon)okP=true;
  if(!okE)e.push('environment'); if(!okP)e.push('phenomenon');
  if(!Array.isArray(r.particles)||r.particles.length<2)e.push('particles');
  else{r.particles.forEach(function(x){if(PT.indexOf(x)<0)e.push('particles:'+x);});}
  if(!r.reaction_factors||typeof r.reaction_factors!=='object')e.push('reaction_factors');
  if(!Array.isArray(r.known_findings)||!r.known_findings.length)e.push('known_findings');
  if(!Array.isArray(r.speculative_findings)||!r.speculative_findings.length)e.push('speculative_findings');
  else{r.speculative_findings.forEach(function(s){if(String(s).indexOf('SPECULATIVE')<0)e.push('speculative unlabeled');});}
  if(!r.content||typeof r.content!=='object')e.push('content');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-quarks-subatomic-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,
  environments:ENVS.map(function(x){return x.g;}),phenomena:PHENS.map(function(x){return x.g;}),particles:PT,
  ptIdx:ptIdx,indexedSpace:8*16*PAIRS*6*5*5};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quarks-subatomic',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
