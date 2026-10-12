(function(){'use strict';
/* JAH Atom Mixes Environment Database generator — jahdb-atom-mixes-environment-1.0.
   Property of Justin Addam Higgins (JAH).
   Universal catalog of what atoms do: chemical, nuclear, quantum, plasma, spectra,
   collisions, phase changes, exotic states — every element pair of all 118 elements,
   multi-atom mixes, across environments from the void to black-hole singularity to
   the Big Bang, with speed and light as reaction factors.
   KNOWN findings = established physics (Type 1, factual only — never invented).
   SPECULATIVE findings = theoretical extrapolation, ALWAYS labeled SPECULATIVE
   (Type 2, Signature-authored). The two are never mixed.
   Deterministic: same seed always makes the same record.
   generateIndexed(seed) walks the full pair×phenomenon×environment space systematically.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ATM-';
var EL=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og'];
var ENVS=[
 {g:'deep-void',t:'Deep Void',known:[
  'At ~2.7 K and near-zero pressure, atoms are nearly motionless; the coldest, emptiest regime known.',
  'The 21-cm hydrogen line is the classic deep-space signal — a spin-flip transition of neutral hydrogen.',
  'With almost no collisions, chemistry stalls; only long-lived excited states and rare encounters matter.'],
  spec:['SPECULATIVE: if two atoms met in a true void at zero relative speed, van der Waals attraction could bind them — a molecule made by patience alone.'],
  temp:'2.7 K',press:'~0 Pa (near-perfect vacuum)',grav:'~0 g',rad:'cosmic microwave background only'},
 {g:'interstellar',t:'Interstellar Medium',known:[
  'Sparse gas (~1 atom/cm³) threaded by cosmic rays and magnetic fields.',
  'Molecular hydrogen (H2) forms on dust-grain surfaces, which absorb the reaction energy.',
  'Cold molecular clouds (10–20 K) host over 200 detected species, including water and organic molecules.'],
  spec:['SPECULATIVE: complex prebiotic molecules may assemble in cloud cores over millions of years — unproven chemistry at glacial rates.'],
  temp:'10–10,000 K',press:'~10⁻¹³ Pa',grav:'~0 g',rad:'cosmic rays + starlight'},
 {g:'planetary',t:'Planetary Surface',known:[
  'Earth surface: ~288 K, 1 atm; chemistry is driven by sunlight, liquid water, and oxygen.',
  'Combustion 2H2 + O2 → 2H2O releases 285.83 kJ/mol once ignited.',
  'Iron oxidizes in air and water to rust — familiar, everyday atomic rearrangement.'],
  spec:['SPECULATIVE: no planetary-surface speculation needed — this is the measured regime; extrapolations beyond Earth are atmospheric models.'],
  temp:'~288 K',press:'101,325 Pa (1 atm)',grav:'1 g',rad:'sunlight (visible + UV)'},
 {g:'stellar-core',t:'Stellar Core',known:[
  'Sun core: ~15 million K, ~250 billion atm; electrons are stripped and nuclei are packed close.',
  'Proton–proton chain: 4H → He-4 + 2 positrons + 2 neutrinos, releasing 26.73 MeV.',
  'The Coulomb barrier keeps nuclei apart at ordinary temperatures; only stellar heat and quantum tunneling overcome it.'],
  spec:['SPECULATIVE: in the most massive stars, silicon burning to iron proceeds in days — models are good but no direct observation exists.'],
  temp:'1.5×10⁷ K',press:'~2.5×10¹⁶ Pa',grav:'~28 g (Sun)',rad:'gamma photons trapped, diffusing outward'},
 {g:'supernova-shock',t:'Supernova Shockwave',known:[
  'Core collapse drives a shock at ~10 billion K; photodisintegration breaks iron back into alpha particles.',
  'The r-process (rapid neutron capture) builds elements heavier than iron — gold, platinum, uranium.',
  'The 2017 kilonova (GW170817) confirmed neutron-star mergers forge heavy elements.'],
  spec:['SPECULATIVE: neutrino-driven winds may set the exact r-process yields — simulations disagree on the details.'],
  temp:'~10¹⁰ K',press:'extreme, transient',grav:'collapsing',rad:'neutrino flood + gamma burst'},
 {g:'neutron-star',t:'Neutron Star',known:[
  'Surface gravity ~2×10¹¹ g crushes electron orbitals; the crust is an iron lattice over a neutron fluid.',
  'Neutron degeneracy pressure supports the star; the Chandrasekhar limit is 1.4 solar masses.',
  'Matter is fully ionized — atoms as chemistry knows them do not exist here.'],
  spec:['SPECULATIVE: the core may hold quark matter or hyperons — the equation of state is still unknown.'],
  temp:'10⁶ K surface, hotter inside',press:'beyond laboratory scale',grav:'~2×10¹¹ g',rad:'X-ray pulses'},
 {g:'black-hole-singularity',t:'Black Hole Singularity',known:[
  'Known physics ends here: general relativity predicts infinite curvature, which signals the theory breaking down — not a measured result.',
  'Tidal forces (spaghettification) would stretch any atom long before the singularity — calculated, not observed.',
  'Event-horizon physics is tested; the singularity itself is unobserved territory.'],
  spec:['SPECULATIVE: quantum gravity may resolve the singularity into a Planck-scale bounce — loop quantum cosmology suggests this.',
   'SPECULATIVE: the firewall hypothesis proposes the horizon itself destroys infalling atoms — hotly debated, unresolved.'],
  temp:'undefined by known theory',press:'undefined by known theory',grav:'beyond general relativity',rad:'Hawking radiation (theoretical)'},
 {g:'big-bang',t:'Big Bang — Early Universe',known:[
  'First 3 minutes (Big Bang nucleosynthesis): protons + neutrons → He-4 (~25% by mass), traces of D, He-3, Li-7.',
  'Observed element abundances match the BBN predictions — one of cosmology’s strongest confirmations.',
  'At 10⁻⁶ seconds the universe was quark–gluon plasma; RHIC and the LHC recreate it in miniature.'],
  spec:['SPECULATIVE: the Planck era (first 10⁻⁴³ s) needs quantum gravity — inflation, GUT symmetry breaking, and baryogenesis are all unproven.'],
  temp:'10¹⁰–10³² K (era-dependent)',press:'cosmological',grav:'cosmological expansion',rad:'primordial photon bath'}
];
var PHENS=[
 {g:'chemical-bonding',t:'Chemical Bonding',multi:false,known:[
  'Atoms bond to reach lower-energy electron configurations; H2 shares two electrons in a covalent bond (bond energy 436 kJ/mol).',
  'Ionic bonds form by electron transfer — sodium gives one electron to chlorine, forming Na+ and Cl- in table salt.',
  'Bond type follows electronegativity difference: small difference → covalent sharing, large difference → ionic transfer.'],
  spec:['SPECULATIVE: under megabar pressures, familiar elements form exotic bonds (e.g. sodium becomes an insulator) — predicted, barely probed.']},
 {g:'chemical-reaction',t:'Chemical Reaction',multi:false,known:[
  '2H2 + O2 → 2H2O releases 285.83 kJ/mol; combustion needs an ignition source to start.',
  'Reactions conserve mass: atoms are rearranged, never created or destroyed in chemistry.',
  'Catalysts speed reactions by lowering activation energy; they are not consumed.'],
  spec:['SPECULATIVE: reaction networks in exotic solvents (supercritical CO2, liquid ammonia) are far less mapped than water chemistry.']},
 {g:'fusion',t:'Nuclear Fusion',multi:false,known:[
  'Proton–proton chain: 4H → He-4 + 2 positrons + 2 neutrinos, releasing 26.73 MeV.',
  'Triple-alpha process: 3 He-4 → C-12 via the Hoyle state — the gateway to all heavier elements.',
  'Above ~3 billion K, silicon burns to iron — and fusing iron costs energy instead of releasing it.'],
  spec:['SPECULATIVE: pycnonuclear fusion in white-dwarf crusts may ignite Type Ia supernovae — the trigger is still debated.']},
 {g:'fission',t:'Nuclear Fission',multi:false,known:[
  'U-235 struck by a thermal neutron splits (e.g. into Ba-141 + Kr-92 + 3 neutrons), releasing ~200 MeV.',
  'The released neutrons can split more nuclei — the chain reaction behind reactors and weapons.',
  'Only a few isotopes (U-235, Pu-239) sustain chain reactions.'],
  spec:['SPECULATIVE: fission cycling in the r-process may shape heavy-element yields — model-dependent.']},
 {g:'radioactive-decay',t:'Radioactive Decay',multi:false,known:[
  'Alpha decay: heavy nuclei eject a helium nucleus; U-238 → Th-234, half-life 4.47 billion years.',
  'Beta-minus decay: a neutron becomes a proton, emitting an electron; C-14 → N-14, half-life 5,730 years.',
  'Gamma decay: an excited nucleus emits a high-energy photon to reach its ground state.'],
  spec:['SPECULATIVE: proton decay is predicted by grand unified theories but never observed — half-life limits exceed 10³⁴ years.']},
 {g:'transmutation',t:'Transmutation',multi:false,known:[
  'Rutherford’s 1919 experiment: alpha particles striking nitrogen-14 produced oxygen-17 and a proton — the first artificial transmutation.',
  'Neutron capture in reactors turns U-238 into Pu-239.',
  'Stellar nucleosynthesis is natural transmutation: stars forge every element from hydrogen.'],
  spec:['SPECULATIVE: controlled muon-catalyzed transmutation could burn waste — demonstrated in principle, never scaled.']},
 {g:'ionization',t:'Ionization',multi:false,known:[
  'Removing hydrogen’s electron takes 13.6 eV — its first ionization energy.',
  'Hot stars and radiation fields strip electrons; the interstellar medium is partly ionized plasma.',
  'Each element has a distinct ladder of ionization energies, tabulated to high precision.'],
  spec:['SPECULATIVE: fully stripped heavy nuclei in cosmic rays may ionize in ways lab beams cannot reproduce.']},
 {g:'excitation',t:'Excitation & Electron Transitions',multi:false,known:[
  'Hydrogen’s Balmer series (transitions to n=2) gives visible lines: red 656 nm, blue-green 486 nm.',
  'An electron dropping to a lower level emits a photon whose energy equals the level difference.',
  'Metastable excited states (e.g. He 2³S) live milliseconds — long enough to matter in plasmas.'],
  spec:['SPECULATIVE: Rydberg atoms (n > 100) in cold clouds could act as cosmic antennas — proposed, not observed.']},
 {g:'plasma',t:'Plasma Formation & Behavior',multi:false,known:[
  'Above ~10,000 K atoms lose electrons entirely; the Sun’s corona is million-kelvin plasma.',
  'Roughly 99% of visible matter in the universe is plasma.',
  'Magnetic fields thread plasma and shape it — solar flares, auroras, fusion confinement.'],
  spec:['SPECULATIVE: dusty plasmas in planet-forming disks may charge grains and alter how planets assemble.']},
 {g:'emission-spectra',t:'Emission & Absorption Spectra',multi:false,known:[
  'Each element’s spectral lines are unique — sodium’s D lines at 589 nm identify it in any flame or star.',
  'Fraunhofer absorption lines in sunlight revealed the Sun’s composition.',
  'Redshift of spectral lines measures cosmic expansion.'],
  spec:['SPECULATIVE: fine-structure constant may vary across cosmic time — some quasar spectra hint at it; disputed.']},
 {g:'quantum-tunneling',t:'Quantum Tunneling',multi:false,known:[
  'Tunneling lets nuclei fuse below the classical Coulomb barrier — Gamow showed it makes stellar fusion possible.',
  'Alpha decay is quantum tunneling of a helium nucleus through the nuclear potential barrier.',
  'Scanning tunneling microscopes image atoms using electron tunneling.'],
  spec:['SPECULATIVE: tunneling may let protons fuse in cold, dense matter (pycnonuclear) — relevant to white dwarfs, unobserved.']},
 {g:'quantum-entanglement',t:'Quantum Entanglement',multi:false,known:[
  'Entangled atoms have been prepared in laboratories; measuring one instantly constrains its partner’s correlated outcome.',
  'Bell-test experiments confirm the correlations exceed any local hidden-variable explanation.',
  'Entangled atomic clocks are being built for ultra-precise timekeeping.'],
  spec:['SPECULATIVE: whether entanglement survives in hot astrophysical plasmas is essentially unexplored.']},
 {g:'phase-change',t:'Atomic Phase Changes',multi:false,known:[
  'Cooling rubidium-87 atoms to ~170 nK formed the first Bose–Einstein condensate (1995).',
  'Melting and boiling are collective atomic rearrangements driven by thermal energy.',
  'Superfluid helium-4 flows with zero viscosity below 2.17 K.'],
  spec:['SPECULATIVE: supersolid phases — crystalline yet superfluid — were reported in 2017 and remain under investigation.']},
 {g:'particle-collision',t:'Particle Collisions at Speed',multi:false,known:[
  'Rutherford scattering (1909): alpha particles bouncing off gold foil revealed the dense atomic nucleus.',
  'Colliders reach 6.8 TeV per proton beam; new particles are made from collision energy via E=mc².',
  'Cosmic-ray protons strike the atmosphere at energies beyond any collider.'],
  spec:['SPECULATIVE: ultra-high-energy collisions might probe string-scale physics — far beyond current reach.']},
 {g:'exotic-states',t:'Exotic States of Matter',multi:false,known:[
  'Neutron stars balance gravity with neutron degeneracy pressure; the Chandrasekhar limit is 1.4 solar masses.',
  'RHIC and the LHC recreate quark–gluon plasma — the state of matter microseconds after the Big Bang.',
  'Metallic hydrogen was reported in diamond-anvil experiments (2017) — disputed, still contested.'],
  spec:['SPECULATIVE: strange-quark matter may be the true ground state of matter — the strange-matter hypothesis, unproven.']},
 {g:'multi-atom-mix',t:'Multi-Atom Mix',multi:true,known:[
  'H2O, CO2, CH4 are stable multi-atom molecules held by covalent bonds.',
  'Crystal lattices (NaCl, diamond) repeat multi-atom arrangements to macroscopic scale.',
  'Proteins fold thousands of atoms into machines — chemistry’s most complex multi-atom mixes.'],
  spec:['SPECULATIVE: exotic multi-atom clusters (e.g. metallic superatoms) may yield materials with designed properties.']}
];
var SPEEDS=['at rest (~0 m/s)','thermal drift (~10² m/s)','orbital velocity (~10⁴ m/s)','relativistic 0.1c','relativistic 0.99c'];
var LIGHTS=['dark — no photon field','cosmic microwave background only','visible sunlight','ultraviolet storm','X-ray flux','gamma-ray burst exposure'];
function buildRec(seed,envKey,phenKey,ea,eb,va,li,topic){
  var e=null,p=null,i;
  for(i=0;i<ENVS.length;i++)if(ENVS[i].g===envKey)e=ENVS[i];
  for(i=0;i<PHENS.length;i++)if(PHENS[i].g===phenKey)p=PHENS[i];
  if(!e||!p)return null;
  ea=((ea%118)+118)%118; eb=((eb%118)+118)%118;
  va=((va%5)+5)%5; li=((li%6)+6)%6;
  var atoms=p.multi?[EL[ea],EL[eb],EL[(ea+eb*7+seed)%118]]:[EL[ea],EL[eb]];
  var mixLabel=atoms.join(' × ');
  var kn=[p.known[seed%p.known.length],e.known[(seed>>2)%e.known.length]];
  var sp=[p.spec[(seed>>1)%p.spec.length],e.spec[(seed>>3)%e.spec.length]];
  var title=p.t+': '+mixLabel+' — '+e.t;
  var desc='A full atomic-phenomenon record: '+p.t.toLowerCase()+' between '+mixLabel+' under '+e.t.toLowerCase()+' conditions. Collision speed: '+SPEEDS[va]+'; light field: '+LIGHTS[li]+'. Known physics and clearly-labeled speculation are kept strictly separate — nothing is invented as fact.';
  var demo=null;
  if(phenKey==='fusion')demo={kind:'fusion-energy',program:'function fusionMeV(nH){var pairs=nH/4;return pairs*26.73;} // MeV from nH protons via pp chain\nconsole.log(fusionMeV(1e6).toExponential(2)); // MeV per million protons',note:'Runnable: energy released fusing nH protons (pp chain).'};
  else if(phenKey==='fission')demo={kind:'fission-energy',program:'function fissionMeV(nU235){return nU235*200;} // ~200 MeV per U-235 fission\nconsole.log(fissionMeV(1e6).toExponential(2)); // MeV per million fissions',note:'Runnable: energy from nU235 fissions.'};
  else if(phenKey==='emission-spectra')demo={kind:'photon-energy',program:'function photonEV(nm){return (1240/nm).toFixed(3);} // E(eV)=1240/λ(nm)\nconsole.log(photonEV(589)); // sodium D line ≈ 2.104 eV',note:'Runnable: photon energy from wavelength.'};
  else if(phenKey==='radioactive-decay')demo={kind:'decay-calc',program:'function remaining(halfLife,t){return Math.pow(0.5,t/halfLife);} // fraction left after t years\nconsole.log(remaining(5730,11460).toFixed(3)); // C-14 after 2 half-lives = 0.250',note:'Runnable: decay fraction after t.'};
  else if(phenKey==='chemical-reaction')demo={kind:'combustion-energy',program:'function h2Energy(molH2){return molH2*285.83/2;} // kJ from molH2 of H2 burned\nconsole.log(h2Energy(4)); // kJ',note:'Runnable: combustion energy.'};
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:title,description:desc,
    environment:envKey,phenomenon:phenKey,
    atom_mix:atoms,mix_class:p.multi?'multi':'pair',
    reaction_factors:{speed:SPEEDS[va],light:LIGHTS[li],temperature:e.temp,pressure:e.press},
    environment_factor:{temperature:e.temp,pressure:e.press,gravity:e.grav,radiation:e.rad},
    known_findings:kn,speculative_findings:sp,
    type:'atomic phenomenon record',
    content:{phenomenon:p.t,atoms:atoms,mix_class:p.multi?'multi':'pair',environment:e.t,
      reaction_factors:{speed:SPEEDS[va],light:LIGHTS[li]},
      known_findings:kn,speculative_findings:sp,
      note:'KNOWN = established physics (Type 1, factual). SPECULATIVE = theoretical extrapolation, always labeled (Type 2, Signature-authored).'},
    demo:demo,src:'signature',_seed:seed,topic:topic||undefined};
}
function normEnv(x){if(!x)return null;var t=String(x).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');for(var i=0;i<ENVS.length;i++){if(ENVS[i].g===t||ENVS[i].g.indexOf(t)>=0||t.indexOf(ENVS[i].g)>=0)return ENVS[i].g;}return null;}
function normPhen(x){if(!x)return null;var t=String(x).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');for(var i=0;i<PHENS.length;i++){if(PHENS[i].g===t||PHENS[i].g.indexOf(t)>=0||t.indexOf(PHENS[i].g)>=0)return PHENS[i].g;}return null;}
function elIdx(sym){var s=String(sym).trim();for(var i=0;i<EL.length;i++)if(EL[i].toLowerCase()===s.toLowerCase())return i;return -1;}
/* Indexed: walks the full pair×phenomenon×environment×speed×light space systematically.
   Total indexed space = 8 env × 16 phen × 13,924 pairs × 5 speeds × 6 lights = 53,462,880 records. */
function decompose(seed){
  var s=seed-1;
  var env=s%8; s=(s/8)|0;
  var phen=s%16; s=(s/16)|0;
  var pair=s%13924; s=(s/13924)|0;
  var va=s%5; s=(s/5)|0;
  var li=s%6;
  return {env:env,phen:phen,ea:(pair/118)|0,eb:pair%118,va:va,li:li};
}
function generateIndexed(seed){var d=decompose(seed);return buildRec(seed,ENVS[d.env].g,PHENS[d.phen].g,d.ea,d.eb,d.va,d.li,null);}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120);
  var env=normEnv(opts.environment)||ENVS[(rnd()*ENVS.length)|0].g;
  var phen=normPhen(opts.phenomenon)||PHENS[(rnd()*PHENS.length)|0].g;
  var ea,eb;
  if(opts.elements&&opts.elements.length>=2){ea=elIdx(opts.elements[0]);eb=elIdx(opts.elements[1]);if(ea<0)ea=(rnd()*118)|0;if(eb<0)eb=(rnd()*118)|0;}
  else{ea=(rnd()*118)|0;eb=(rnd()*118)|0;}
  var va=(rnd()*5)|0, li=(rnd()*6)|0;
  return buildRec(seed,env,phen,ea,eb,va,li,topic||null);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ATM-\d{6,7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  var okE=false,okP=false,i;
  for(i=0;i<ENVS.length;i++)if(ENVS[i].g===r.environment)okE=true;
  for(i=0;i<PHENS.length;i++)if(PHENS[i].g===r.phenomenon)okP=true;
  if(!okE)e.push('environment'); if(!okP)e.push('phenomenon');
  if(!Array.isArray(r.atom_mix)||r.atom_mix.length<2)e.push('atom_mix');
  else{r.atom_mix.forEach(function(a){if(EL.indexOf(a)<0)e.push('atom_mix:'+a);});}
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
var gen={version:'jahdb-atom-mixes-environment-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,
  environments:ENVS.map(function(x){return x.g;}),phenomena:PHENS.map(function(x){return x.g;}),elements:EL,
  elIdx:elIdx,indexedSpace:8*16*13924*5*6};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('atom-mixes-environment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
