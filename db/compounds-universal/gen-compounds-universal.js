(function(){'use strict';
/* JAH Compounds Universal Database generator — jahdb-compounds-universal-1.0.
   Property of Justin Addam Higgins (JAH).
   A universal catalog of ALL things compounds can do: every phenomenon
   (synthesis, decomposition, redox, acid-base, precipitation, polymerization,
   catalysis, combustion, corrosion, dissolution, crystallization, isomerization,
   hydrolysis, photochemical) across every environment from the void to the
   Big Bang, with reaction factors (speed, light, temperature, pressure, catalyst).
   Deterministic: same seed always makes the same record.
   known_findings = Type 1 established chemistry (factual, never invented).
   speculative_findings = Type 2 clearly-labeled extrapolation for extreme environments. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-CMP-';
/* ---------------- compound pool: [name, formula, class, note] ---------------- */
var COMPOUNDS=[
 ['Water','H2O','inorganic','the universal solvent; polar; expands on freezing'],
 ['Carbon dioxide','CO2','inorganic','linear molecule; sublimates at -78.5 C at 1 atm'],
 ['Methane','CH4','organic','simplest hydrocarbon; tetrahedral; major greenhouse gas'],
 ['Ammonia','NH3','inorganic','trigonal pyramidal; pungent; key fertilizer feedstock'],
 ['Sodium chloride','NaCl','salt','ionic lattice; dissolves into Na+ and Cl- in water'],
 ['Iron(III) oxide','Fe2O3','oxide','rust; forms when iron oxidizes in air and moisture'],
 ['Calcium carbonate','CaCO3','salt','limestone/marble; fizzes with acids releasing CO2'],
 ['Sulfuric acid','H2SO4','acid','strong diprotic acid; powerful dehydrating agent'],
 ['Hydrochloric acid','HCl','acid','strong monoprotic acid; stomach acid component'],
 ['Sodium hydroxide','NaOH','base','strong base; caustic; saponifies fats'],
 ['Glucose','C6H12O6','carbohydrate','blood sugar; cellular respiration fuel'],
 ['Ethanol','C2H5OH','alcohol','fermentation product; flammable; common solvent'],
 ['Benzene','C6H6','aromatic','planar ring; resonance-stabilized; carcinogenic'],
 ['Polyethylene','(C2H4)n','polymer','most-produced plastic; addition polymer of ethylene'],
 ['Aspirin','C9H8O4','organic','acetylsalicylic acid; ester of salicylic acid'],
 ['Caffeine','C8H10N4O2','alkaloid','stimulant; bitter; sublimates near 178 C'],
 ['Diamond','C','allotrope','sp3 carbon lattice; hardest natural material'],
 ['Graphite','C','allotrope','sp2 carbon sheets; conducts; soft lubricant'],
 ['Ozone','O3','inorganic','bent molecule; absorbs UV; strong oxidizer'],
 ['Hydrogen peroxide','H2O2','inorganic','decomposes to water + oxygen; catalyzed by MnO2'],
 ['Copper sulfate','CuSO4','salt','blue crystals; pentahydrate common lab reagent'],
 ['Silver nitrate','AgNO3','salt','light-sensitive; forms AgCl precipitate with chlorides'],
 ['Barium sulfate','BaSO4','salt','extremely insoluble; X-ray contrast agent'],
 ['Calcium hydroxide','Ca(OH)2','base','slaked lime; low solubility; mortar component'],
 ['Nitric acid','HNO3','acid','strong oxidizing acid; nitrates organics'],
 ['Acetic acid','CH3COOH','acid','weak acid; vinegar is ~5% solution'],
 ['Urea','CO(NH2)2','organic','first synthesized organic compound (Wohler 1828)'],
 ['Nylon-6,6','(C12H22N2O2)n','polymer','condensation polymer; strong fibers'],
 ['Teflon (PTFE)','(C2F4)n','polymer','nonstick; extremely chemically inert'],
 ['Quartz','SiO2','oxide','hardness 7; piezoelectric; sand/glass base'],
 ['Table sugar','C12H22O11','carbohydrate','sucrose; caramelizes near 160 C'],
 ['Baking soda','NaHCO3','salt','leavens via CO2 release with acids or heat'],
 ['Washing soda','Na2CO3','salt','water softener; alkaline'],
 ['Bleach (sodium hypochlorite)','NaOCl','inorganic','oxidizing disinfectant'],
 ['Potassium nitrate','KNO3','salt','saltpeter; oxidizer in gunpowder'],
 ['Magnesium oxide','MgO','oxide','refractory; forms bright white flame when Mg burns'],
 ['Aluminum oxide','Al2O3','oxide','corundum; abrasive; very high melting point'],
 ['Titanium dioxide','TiO2','oxide','white pigment; photocatalyst under UV'],
 ['Zinc oxide','ZnO','oxide','sunscreen active; semiconductor'],
 ['Lead sulfide','PbS','salt','galena ore; narrow bandgap semiconductor'],
 ['Pyrite','FeS2','sulfide','fool\'s gold; metallic luster cubic crystals']
];
/* ---------------- environments: [name, temp, pressure, gravity, note] ---------------- */
var ENVS=[
 ['Interstellar void','3 K','~0 Pa','micro','near-vacuum; cosmic rays only; chemistry nearly frozen'],
 ['Earth surface','288 K','101 kPa','1 g','standard reference: air, water, sunlight'],
 ['Deep ocean vent','400 K','30 MPa','1 g','high pressure; mineral-rich superheated water'],
 ['Venus surface','737 K','9.2 MPa','0.9 g','crushing CO2 atmosphere; sulfuric acid clouds'],
 ['Stellar photosphere','5800 K','low','274 g','plasma; molecules dissociate; atoms ionize'],
 ['Stellar core','15 MK','250 GPa','274 g','fusion conditions; nuclei overcome Coulomb barrier'],
 ['Neutron star surface','1 MK','extreme','2e11 g','atoms crushed; electron degeneracy; exotic nuclei'],
 ['Black hole accretion disk','10 MK','extreme','extreme tidal','superheated plasma spiraling inward; intense X-rays'],
 ['Black hole singularity','unknown','infinite (theory)','infinite (theory)','physics breaks down; SPECULATIVE territory'],
 ['Big Bang nucleosynthesis','1 GK','extreme','n/a','first minutes: protons+neutrons fused into light nuclei']
];
/* ---------------- phenomenon builders ----------------
   Each returns {phenomenon, title, known, speculative, factors} */
function bSynthesis(s,c1,c2,env){
 var p=c1[0]+' + '+c2[0];
 return {phenomenon:'synthesis',
  title:p+' -> new compound ('+env[0]+')',
  known:'Under Earth-surface conditions, synthesis combines simpler substances into a more complex compound, releasing or absorbing a definite enthalpy. Example: 2H2 + O2 -> 2H2O releases 572 kJ/mol. The product\'s properties are fixed by its structure, not its history.',
  speculative:'At '+env[0]+' ('+env[1]+', '+env[2]+'), '+(env[0].indexOf('singularity')>=0||env[0].indexOf('Big Bang')>=0?'standard chemical bonding may not apply — nuclei and spacetime itself are the reactants; any "compound" would be unlike terrestrial chemistry. SPECULATIVE.':'synthesis pathways shift with temperature and pressure per Le Chatelier\'s principle, but the underlying bond energetics are unchanged. Extrapolated, not observed. SPECULATIVE.')};
}
function bDecomp(s,c1,c2,env){
 return {phenomenon:'decomposition',
  title:c1[0]+' breaks down ('+env[0]+')',
  known:c1[0]+' ('+c1[1]+') decomposes when heated or electrolyzed into simpler substances — e.g. CaCO3 -> CaO + CO2 above ~840 C, 2H2O2 -> 2H2O + O2 (catalyzed). Decomposition is the reverse of synthesis with matching enthalpy magnitude.',
  speculative:'At '+env[0]+', decomposition thresholds move with '+env[1]+' and '+env[2]+'. '+(env[0].indexOf('void')>=0?'In the void, photodissociation by starlight slowly breaks molecules over millennia.':'In extreme heat, compounds dissociate into atoms, then plasma. SPECULATIVE where unobserved.')};
}
function bRedox(s,c1,c2,env){
 return {phenomenon:'redox',
  title:c1[0]+' + '+c2[0]+' redox ('+env[0]+')',
  known:'Oxidation-reduction transfers electrons: one species oxidized (loses e-), one reduced (gains e-). Example: Fe -> Fe3+ + 3e- paired with O2 + 4e- -> 2O2-. Standard electrode potentials predict spontaneity; deltaG = -nFE.',
  speculative:'Redox under '+env[0]+' ('+env[1]+') follows the same electron-transfer rules wherever electrons are bound. Near a singularity, the concept of bound electrons may fail entirely. SPECULATIVE.'};
}
function bAcidBase(s,c1,c2,env){
 return {phenomenon:'acid-base',
  title:c1[0]+' + '+c2[0]+' neutralization ('+env[0]+')',
  known:'Acids donate protons, bases accept them: HCl + NaOH -> NaCl + H2O, deltaH ~ -57 kJ/mol. In water, pH measures -log[H+]; neutralization drives pH toward 7. Buffer systems resist pH change.',
  speculative:'Acid-base chemistry assumes a solvent and mobile protons. In the void or plasma environments there is no solvent — proton transfer as such does not occur; bare ion chemistry takes over. SPECULATIVE extrapolation.'};
}
function bPrecip(s,c1,c2,env){
 return {phenomenon:'precipitation',
  title:c1[0]+' + '+c2[0]+' precipitate ('+env[0]+')',
  known:'When ion product exceeds Ksp, a solid precipitates: Ag+ + Cl- -> AgCl(s), Ksp = 1.8e-10. Precipitation purifies, separates, and builds minerals; crystal habit reflects lattice energy.',
  speculative:'Precipitation needs a solvent and gravity or surfaces for settling. In microgravity void conditions, crystals grow more perfectly (as seen on the ISS). At singularity pressures the solid/liquid distinction itself may vanish. SPECULATIVE.'};
}
function bPoly(s,c1,c2,env){
 return {phenomenon:'polymerization',
  title:c1[0]+' polymerizes ('+env[0]+')',
  known:'Monomers link into chains: addition (ethylene -> polyethylene via radical initiators) or condensation (nylon from diamine + diacid, releasing water). Degree of polymerization sets strength; crosslinking sets rigidity.',
  speculative:'Polymer backbones need stable covalent bonds. Above ~5000 K all organic polymers pyrolyze; only inorganic polymers (silicones briefly) survive hotter. In stellar plasma no polymers exist. SPECULATIVE for unobserved regimes.'};
}
function bCatal(s,c1,c2,env){
 return {phenomenon:'catalysis',
  title:c1[0]+' catalyzed ('+env[0]+')',
  known:'Catalysts lower activation energy without being consumed: MnO2 catalyzes H2O2 decomposition; enzymes achieve 1e6x speedups with specificity. Heterogeneous catalysts adsorb reactants on surfaces; homogeneous ones form intermediates.',
  speculative:'Catalysis requires the catalyst to survive the environment. In the '+env[0]+' at '+env[1]+', most catalysts decompose — only refractory oxides or bare metal surfaces persist. SPECULATIVE where untested.'};
}
function bCombust(s,c1,c2,env){
 return {phenomenon:'combustion',
  title:c1[0]+' burns ('+env[0]+')',
  known:'Rapid exothermic oxidation: CH4 + 2O2 -> CO2 + 2H2O, deltaH = -890 kJ/mol. Needs fuel, oxidizer, ignition; flame temperature and products depend on stoichiometry. Incomplete combustion yields CO and soot.',
  speculative:'Combustion needs an oxidizer — in the void or on airless bodies, nothing burns without carried oxygen. In pure oxygen atmospheres, even metals burn. Near black holes, infalling matter heats to X-ray emission — "burning" by gravity, not chemistry. SPECULATIVE.'};
}
function bCorrode(s,c1,c2,env){
 return {phenomenon:'corrosion',
  title:c1[0]+' corrodes ('+env[0]+')',
  known:'Electrochemical attack: iron rusts via anodic Fe -> Fe2+ and cathodic O2 reduction, needing water as electrolyte. 4Fe + 3O2 + 2H2O -> 2Fe2O3.H2O. Passivation (Al2O3 on aluminum) and galvanization prevent it.',
  speculative:'Corrosion rates scale with temperature, moisture, and radiation. In the void, atomic oxygen erodes polymers on spacecraft; micrometeorites sandblast surfaces. At Venus, hot CO2/H2SO4 corrodes nearly everything. SPECULATIVE for unmeasured regimes.'};
}
function bDissolve(s,c1,c2,env){
 return {phenomenon:'dissolution',
  title:c1[0]+' dissolves ('+env[0]+')',
  known:'"Like dissolves like": polar NaCl dissociates in polar water (hydration enthalpy overcomes lattice energy); nonpolar oil does not. Solubility products and temperature curves are tabulated; saturation is dynamic equilibrium.',
  speculative:'Dissolution needs a liquid solvent. Supercritical CO2 dissolves nonpolar organics (used industrially). In the void there is no solvent; on Titan, liquid methane is the solvent and water ice is the "rock". SPECULATIVE beyond observed solvents.'};
}
function bCrystal(s,c1,c2,env){
 return {phenomenon:'crystallization',
  title:c1[0]+' crystallizes ('+env[0]+')',
  known:'Ordered lattices minimize energy: NaCl forms face-centered cubic; diamond forms tetrahedral sp3. Nucleation then growth; impurities and cooling rate set crystal size. X-ray diffraction reads the lattice.',
  speculative:'In microgravity, crystals grow larger and more perfect (ISS protein crystals). Under gigapascal pressures, new phases appear (metallic hydrogen predicted). At singularity densities, crystal concepts break down. SPECULATIVE.'};
}
function bIsomer(s,c1,c2,env){
 return {phenomenon:'isomerization',
  title:c1[0]+' isomerizes ('+env[0]+')',
  known:'Same formula, different arrangement: n-butane vs isobutane; cis/trans alkenes; optical enantiomers rotate polarized light oppositely. Interconversion needs bond rotation or breaking — barriers measured in kJ/mol.',
  speculative:'Isomer ratios at equilibrium follow Boltzmann distribution over the barrier heights. Intense UV can photoisomerize (retinal in vision). Extreme gravity gradients are not known to isomerize molecules. SPECULATIVE.'};
}
function bHydro(s,c1,c2,env){
 return {phenomenon:'hydrolysis',
  title:c1[0]+' hydrolyzes ('+env[0]+')',
  known:'Water splits a bond: esters -> acid + alcohol; ATP -> ADP + Pi releases ~30 kJ/mol driving biochemistry. Acid or base catalyzes; saponification makes soap from fats + NaOH.',
  speculative:'Hydrolysis needs liquid water. In supercritical water (374 C, 22 MPa) organics hydrolyze rapidly — used for waste destruction. Without water, analogous solvolysis uses the local solvent. SPECULATIVE for exotic solvents.'};
}
function bPhoto(s,c1,c2,env){
 return {phenomenon:'photochemical',
  title:c1[0]+' under light ('+env[0]+')',
  known:'Photons drive chemistry: O2 + UV -> O3 (ozone layer); AgBr + light -> Ag (photography); photosynthesis 6CO2 + 6H2O + light -> C6H12O6 + 6O2. Quantum yield counts molecules per photon absorbed.',
  speculative:'Near a black hole accretion disk, X-ray flux drives extreme photochemistry — molecules are shredded faster than they form. In the void, sparse UV slowly processes ice mantles on dust grains into organics. SPECULATIVE where unobserved.'};
}
var BUILDERS={synthesis:bSynthesis,decomposition:bDecomp,redox:bRedox,'acid-base':bAcidBase,precipitation:bPrecip,polymerization:bPoly,catalysis:bCatal,combustion:bCombust,corrosion:bCorrode,dissolution:bDissolve,crystallization:bCrystal,isomerization:bIsomer,hydrolysis:bHydro,photochemical:bPhoto};
var PHENS=Object.keys(BUILDERS);
/* ---------------- main ---------------- */
function normPhen(p){
 if(!p) return null;
 var t=String(p).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
 if(BUILDERS[t]) return t;
 for(var i=0;i<PHENS.length;i++){ if(PHENS[i].indexOf(t)>=0||t.indexOf(PHENS[i])>=0) return PHENS[i]; }
 return null;
}
function speedFactor(s){
 return pick(['thermal drift (<1 km/s)','lab collision (1-10 km/s)','hypervelocity (10-100 km/s)','relativistic (>0.1c)'],s);
}
function lightFactor(s){
 return pick(['dark (no photons)','ambient starlight','intense UV flux','X-ray bath (accretion disk)'],s);
}
function generate(seed,opts,rnd){
 opts=opts||{}; rnd=rnd||prng(seed);
 var topic=(opts.topic||'').toString().trim().slice(0,120);
 var ph=normPhen(opts.phenomenon)||normPhen(opts.genre)||pick(PHENS,rnd);
 var cs=shuffle(rnd,COMPOUNDS);
 var c1=cs[0], c2=cs[1];
 var env=pick(ENVS,rnd);
 if(opts.environment){ var t=String(opts.environment).toLowerCase(); for(var i=0;i<ENVS.length;i++){ if(ENVS[i][0].toLowerCase().indexOf(t)>=0){ env=ENVS[i]; break; } } }
 var b=BUILDERS[ph](rnd,c1,c2,env);
 var speed=speedFactor(rnd), light=lightFactor(rnd);
 var title=b.title+(topic?' — '+topic:'');
 var desc='A universal catalog entry: '+b.phenomenon+' of '+c1[0]+' ('+c1[1]+')'+(ph==='synthesis'||ph==='redox'||ph==='acid-base'||ph==='precipitation'?' with '+c2[0]+' ('+c2[1]+')':'')+' under '+env[0]+' conditions ('+env[1]+', '+env[2]+'). Reaction factors: speed '+speed+'; light '+light+'. Known chemistry and clearly-labeled speculation are kept separate.';
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:title,description:desc,phenomenon:b.phenomenon,compound:c1[0]+' ('+c1[1]+')',
  environment:env[0],reaction_factors:{speed:speed,light:light,temperature:env[1],pressure:env[2],gravity:env[3]},
  known_findings:b.known,speculative_findings:b.speculative,env_note:env[4],src:'signature',_seed:seed,topic:topic||undefined};
}
function generateIndexed(i){
 return generate(i+1,{});
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-CMP-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(PHENS.indexOf(r.phenomenon)<0)e.push('phenomenon');
 if(typeof r.known_findings!=='string'||r.known_findings.length<40)e.push('known_findings');
 if(typeof r.speculative_findings!=='string'||r.speculative_findings.length<20)e.push('speculative_findings');
 if(!r.reaction_factors||typeof r.reaction_factors!=='object')e.push('reaction_factors');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-compounds-universal-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,phenomena:PHENS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compounds-universal',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
