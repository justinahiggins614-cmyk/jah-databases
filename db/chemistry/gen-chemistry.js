(function(){'use strict';
/* EXPANSION 2026-10-18 group-1: flavor/kitchen branches added. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['organic','inorganic','physical','reactions','lab', 'flavor', 'kitchen', 'flavor', 'kitchen'];
var PREFIX='JAH-CHEM-';
var AW={H:1.008,He:4.0026,Li:6.94,Be:9.0122,B:10.81,C:12.011,N:14.007,O:15.999,F:18.998,Ne:20.180,Na:22.990,Mg:24.305,Al:26.982,Si:28.085,P:30.974,S:32.06,Cl:35.45,Ar:39.948,K:39.098,Ca:40.078,Sc:44.956,Ti:47.867,V:50.942,Cr:51.996,Mn:54.938,Fe:55.845,Co:58.933,Ni:58.693,Cu:63.546,Zn:65.38,Ga:69.723,Ge:72.630,As:74.922,Se:78.971,Br:79.904,Kr:83.798,Rb:85.468,Sr:87.62,Ag:107.87,Cd:112.41,In:114.82,Sn:118.71,Sb:121.76,Te:127.60,I:126.90,Xe:131.29,Cs:132.91,Ba:137.33,W:183.84,Pt:195.08,Au:196.97,Hg:200.59,Pb:207.2,Bi:208.98,U:238.03};
function mm(comp){var m=0;for(var el in comp)m+=comp[el]*(AW[el]||0);return Math.round(m*1000)/1000;}
function fmt(comp){var s='';Object.keys(comp).forEach(function(el){s+=el+(comp[el]>1?comp[el]:'');});return s;}
function atoms(species){var t={};species.forEach(function(sp){for(var el in sp.comp)t[el]=(t[el]||0)+sp.coef*sp.comp[el];});return t;}
function sameAtoms(a,b){var k={};for(var x in a)k[x]=1;for(var y in b)k[y]=1;for(var z in k)if((a[z]||0)!==(b[z]||0))return false;return true;}
function sp(formula,coef,comp){return {formula:formula,coef:coef,comp:comp};}
var RXNS=[
 ['Methane combustion',[sp('CH4',1,{C:1,H:4}),sp('O2',2,{O:2})],[sp('CO2',1,{C:1,O:2}),sp('H2O',2,{H:2,O:1})]],
 ['Ethane combustion',[sp('C2H6',2,{C:2,H:6}),sp('O2',7,{O:2})],[sp('CO2',4,{C:1,O:2}),sp('H2O',6,{H:2,O:1})]],
 ['Propane combustion',[sp('C3H8',1,{C:3,H:8}),sp('O2',5,{O:2})],[sp('CO2',3,{C:1,O:2}),sp('H2O',4,{H:2,O:1})]],
 ['Butane combustion',[sp('C4H10',2,{C:4,H:10}),sp('O2',13,{O:2})],[sp('CO2',8,{C:1,O:2}),sp('H2O',10,{H:2,O:1})]],
 ['Water synthesis',[sp('H2',2,{H:2}),sp('O2',1,{O:2})],[sp('H2O',2,{H:2,O:1})]],
 ['Ammonia synthesis',[sp('N2',1,{N:2}),sp('H2',3,{H:2})],[sp('NH3',2,{N:1,H:3})]],
 ['Sodium chloride synthesis',[sp('Na',2,{Na:1}),sp('Cl2',1,{Cl:2})],[sp('NaCl',2,{Na:1,Cl:1})]],
 ['Magnesium oxide formation',[sp('Mg',2,{Mg:1}),sp('O2',1,{O:2})],[sp('MgO',2,{Mg:1,O:1})]],
 ['Hydrogen peroxide decomposition',[sp('H2O2',2,{H:2,O:2})],[sp('H2O',2,{H:2,O:1}),sp('O2',1,{O:2})]],
 ['Calcium carbonate decomposition',[sp('CaCO3',1,{Ca:1,C:1,O:3})],[sp('CaO',1,{Ca:1,O:1}),sp('CO2',1,{C:1,O:2})]],
 ['Zinc in hydrochloric acid',[sp('Zn',1,{Zn:1}),sp('HCl',2,{H:1,Cl:1})],[sp('ZnCl2',1,{Zn:1,Cl:2}),sp('H2',1,{H:2})]],
 ['Magnesium in hydrochloric acid',[sp('Mg',1,{Mg:1}),sp('HCl',2,{H:1,Cl:1})],[sp('MgCl2',1,{Mg:1,Cl:2}),sp('H2',1,{H:2})]],
 ['Sodium hydroxide neutralization',[sp('HCl',1,{H:1,Cl:1}),sp('NaOH',1,{Na:1,O:1,H:1})],[sp('NaCl',1,{Na:1,Cl:1}),sp('H2O',1,{H:2,O:1})]],
 ['Sulfuric acid neutralization',[sp('H2SO4',1,{H:2,S:1,O:4}),sp('NaOH',2,{Na:1,O:1,H:1})],[sp('Na2SO4',1,{Na:2,S:1,O:4}),sp('H2O',2,{H:2,O:1})]],
 ['Silver chloride precipitation',[sp('AgNO3',1,{Ag:1,N:1,O:3}),sp('NaCl',1,{Na:1,Cl:1})],[sp('AgCl',1,{Ag:1,Cl:1}),sp('NaNO3',1,{Na:1,N:1,O:3})]],
 ['Photosynthesis (simplified)',[sp('CO2',6,{C:1,O:2}),sp('H2O',6,{H:2,O:1})],[sp('C6H12O6',1,{C:6,H:12,O:6}),sp('O2',6,{O:2})]],
 ['Cellular respiration',[sp('C6H12O6',1,{C:6,H:12,O:6}),sp('O2',6,{O:2})],[sp('CO2',6,{C:1,O:2}),sp('H2O',6,{H:2,O:1})]]
];
var ORG=[['Signature alkane study','alkane chain model'],['Signature alcohol study','hydroxyl group model'],['Signature carboxylic acid study','carboxyl group model'],['Signature ester study','ester linkage model'],['Signature aromatic study','ring delocalization model']];
var LABM=[['titration','determining concentration by measured reaction'],['distillation','separating liquids by boiling point'],['chromatography','separating mixtures by differential migration'],['spectroscopy','identifying substances by light interaction'],['calorimetry','measuring heat of reaction']];
var PHYS=[['periodic trend: atomic radius','generally decreases across a period and increases down a group'],['ideal gas relation','pressure, volume, temperature and amount relate as PV = nRT'],['mole concept','one mole contains Avogadro-scale particle counts'],['conservation of mass','atoms are rearranged, never created or destroyed, in reactions']];
/* === EXPANSION 2026-10-18 group-1: Flavor Chemistry / Kitchen Chemistry ===
   Real reference chemistry in the stored schema (concept/statement, source online,
   creation_mode ONLINE-VERIFIED). Deterministic by seed. */
var FLAVOR_TOPICS=[
{t:"The Maillard Reaction — Browning and Flavor",
 d:"The Maillard reaction between amino acids and reducing sugars creates the browned flavors of seared meat, baked bread, and roasted coffee.",
 concept:"Maillard reaction",
 statement:"The Maillard reaction is a non-enzymatic browning reaction between amino acids and reducing sugars, typically above 140 C, producing hundreds of flavor compounds including melanoidins.",
 ref:"https://en.wikipedia.org/wiki/Maillard_reaction"},
{t:"Caramelization — Sugar Under Heat",
 d:"Caramelization is the thermal decomposition of sugar itself, producing the deep flavors of caramel, toffee, and crème brûlée.",
 concept:"caramelization",
 statement:"Caramelization is the pyrolysis of sugar at high temperature (sucrose around 160 C), producing volatile flavor compounds and brown polymers without amino acids.",
 ref:"https://en.wikipedia.org/wiki/Caramelization"},
{t:"Capsaicin — The Chemistry of Heat",
 d:"Capsaicin binds the TRPV1 heat receptor, which is why chili heat feels like burning — the chemistry of spiciness explained.",
 concept:"capsaicin receptor chemistry",
 statement:"Capsaicin (C18H27NO3) activates the TRPV1 receptor, producing the sensation of heat; the Scoville scale quantifies pungency by capsaicinoid concentration.",
 ref:"https://en.wikipedia.org/wiki/Capsaicin"},
{t:"Umami — Glutamate and Savory Taste",
 d:"Umami, the fifth taste, is triggered by glutamate and nucleotides — the chemistry behind savory depth in aged cheese, mushrooms, and dashi.",
 concept:"umami taste chemistry",
 statement:"Umami taste is mediated by glutamate binding to T1R1/T1R3 receptors, synergistically enhanced by inosinate and guanylate nucleotides.",
 ref:"https://en.wikipedia.org/wiki/Umami"},
{t:"Esters — The Aromas of Fruit",
 d:"Esters are the volatile compounds behind most fruit aromas — ethyl butyrate smells of pineapple, isoamyl acetate of banana.",
 concept:"ester aroma chemistry",
 statement:"Fruit aromas are dominated by esters formed from carboxylic acids and alcohols; e.g., ethyl butyrate (pineapple) and isoamyl acetate (banana).",
 ref:"https://en.wikipedia.org/wiki/Ester"},
{t:"Vanillin — The World's Favorite Flavor",
 d:"Vanillin is the primary flavor compound of vanilla — and most of the world's supply is synthesized, chemically identical to the natural molecule.",
 concept:"vanillin",
 statement:"Vanillin (C8H8O3, 4-hydroxy-3-methoxybenzaldehyde) is the principal flavor component of vanilla; synthetic vanillin is chemically identical to the natural compound.",
 ref:"https://en.wikipedia.org/wiki/Vanillin"},
{t:"Allicin — Garlic's Pungent Defense",
 d:"Crushing garlic triggers an enzymatic reaction producing allicin — the sulfur chemistry behind garlic's bite and its reputed benefits.",
 concept:"allicin formation",
 statement:"Crushing garlic converts alliin to allicin via the enzyme alliinase; allicin (diallyl thiosulfinate) gives fresh garlic its pungency.",
 ref:"https://en.wikipedia.org/wiki/Allicin"},
{t:"Citric Acid — The Chemistry of Sour",
 d:"Sour taste is the tongue detecting acidity — citric acid in citrus fruits donates protons that trigger sour receptors.",
 concept:"sour taste chemistry",
 statement:"Sour perception is triggered by acids donating protons (H+); citric acid (C6H8O7), abundant in citrus, is the characteristic food acid.",
 ref:"https://en.wikipedia.org/wiki/Citric_acid"},
{t:"Tannins — Astringency in Tea and Wine",
 d:"Tannins bind salivary proteins, creating the dry, puckering sensation of astringency in strong tea, red wine, and unripe fruit.",
 concept:"tannin astringency",
 statement:"Astringency is caused by tannins (polyphenols) precipitating salivary proteins, producing the characteristic dry mouthfeel of tea and red wine.",
 ref:"https://en.wikipedia.org/wiki/Tannin"},
{t:"Menthol — The Chemistry of Cool",
 d:"Menthol triggers the TRPM8 cold receptor, which is why mint feels cold — cooling without any temperature change.",
 concept:"menthol receptor chemistry",
 statement:"Menthol activates the TRPM8 cold receptor, producing a cooling sensation at constant temperature; it is a cyclic monoterpene alcohol (C10H20O).",
 ref:"https://en.wikipedia.org/wiki/Menthol"}
];
var KITCHEN_TOPICS=[
{t:"Leavening — Baking Soda vs Baking Powder",
 d:"Chemical leaveners produce CO2 that lifts batters — the acid-base chemistry behind the difference between soda and powder.",
 concept:"chemical leavening",
 statement:"Baking soda (NaHCO3) requires an external acid to release CO2; baking powder contains its own acid and releases CO2 in two stages (moisture, then heat).",
 ref:"https://en.wikipedia.org/wiki/Leavening_agent"},
{t:"Gluten Development — The Protein Network",
 d:"Kneading hydrates gliadin and glutenin into gluten — the elastic protein network that gives bread its structure.",
 concept:"gluten formation",
 statement:"Gluten forms when wheat proteins gliadin and glutenin hydrate and are mechanically worked, creating the viscoelastic network that traps fermentation gases.",
 ref:"https://en.wikipedia.org/wiki/Gluten"},
{t:"Egg Protein Coagulation — Heat and Structure",
 d:"Heating eggs denatures and coagulates their proteins — the chemistry that sets custards, scrambles, and meringues.",
 concept:"protein denaturation",
 statement:"Egg proteins denature and coagulate with heat (whites around 60-65 C, yolks around 65-70 C), forming the gels and foams of cooked egg dishes.",
 ref:"https://en.wikipedia.org/wiki/Egg_as_food"},
{t:"Emulsification — The Science of Mayonnaise",
 d:"Mayonnaise is an oil-in-water emulsion stabilized by egg-yolk lecithin — the colloid chemistry of creamy sauces.",
 concept:"emulsion stabilization",
 statement:"Mayonnaise is an oil-in-water emulsion in which egg-yolk lecithin acts as the emulsifier, stabilizing dispersed oil droplets in the aqueous phase.",
 ref:"https://en.wikipedia.org/wiki/Emulsion"},
{t:"Gelatin Setting — Collagen to Gel",
 d:"Gelatin gels because denatured collagen partially renatures into a network — the thermoreversible chemistry of jellies.",
 concept:"gelatin gelation",
 statement:"Gelatin (hydrolyzed collagen) forms thermoreversible gels as protein chains partially reassociate into triple-helical junction zones on cooling.",
 ref:"https://en.wikipedia.org/wiki/Gelatin"},
{t:"Sugar Crystallization — Fudge and Control",
 d:"Fudge, fondant, and rock candy are exercises in controlling sugar crystallization — nucleation, seeding, and interference.",
 concept:"sugar crystallization",
 statement:"Controlling sugar crystallization — via seeding, agitation timing, and interfering agents like corn syrup — determines the texture of crystalline confections.",
 ref:"https://en.wikipedia.org/wiki/Crystallization"},
{t:"Brining — Osmosis and Juiciness",
 d:"Brining meat in salt water uses osmosis and protein denaturation to produce juicier cooked meat — the chemistry explained.",
 concept:"brining osmosis",
 statement:"Brining raises meat's water content by osmosis and partially denatures muscle proteins, reducing moisture loss during cooking.",
 ref:"https://en.wikipedia.org/wiki/Brining"},
{t:"Fermentation — Yeast and Bread Rising",
 d:"Yeast ferments sugars into CO2 and ethanol — the biochemistry that leavens bread and brews beer.",
 concept:"alcoholic fermentation",
 statement:"Saccharomyces cerevisiae ferments sugars to carbon dioxide and ethanol (C6H12O6 -> 2 C2H5OH + 2 CO2), leavening dough and producing alcohol.",
 ref:"https://en.wikipedia.org/wiki/Fermentation"},
{t:"Anthocyanins — pH and Food Color",
 d:"Anthocyanin pigments change color with pH — red in acid, blue in base — the chemistry behind red cabbage's famous trick.",
 concept:"anthocyanin pH indicator",
 statement:"Anthocyanins are pH-sensitive pigments (red in acid, purple neutral, blue-green in base), which is why red cabbage changes color with vinegar or baking soda.",
 ref:"https://en.wikipedia.org/wiki/Anthocyanin"},
{t:"Smoke Points — Fats Under Heat",
 d:"Every cooking fat has a smoke point where it breaks down — the chemistry of choosing the right fat for the heat.",
 concept:"fat smoke point",
 statement:"A fat's smoke point is the temperature at which volatile compounds form visible smoke; refined oils smoke higher than unrefined, and exceeding it produces off-flavors.",
 ref:"https://en.wikipedia.org/wiki/Smoke_point"}
];
function flavorKitchenRec(seed,cat){
  var pool=cat==='flavor'?FLAVOR_TOPICS:KITCHEN_TOPICS;
  var tp=pool[(seed-1)%pool.length];
  return {title:tp.t,category:cat,description:tp.d,concept:tp.concept,statement:tp.statement,
    source:'online',source_ref:tp.ref,creation_mode:'ONLINE-VERIFIED',_seed:seed,
    id:PREFIX+String(seed).padStart(7,'0'),demo:null};
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(opts.category==='flavor'||opts.category==='kitchen')return flavorKitchenRec(seed,opts.category);

  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var rec={id:id,category:cat,source:'signature',source_ref:'JAH Signature Generator',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
  if(cat==='reactions'){
    var rx=pick(RXNS,rnd),n=ri(rnd,1,80);
    var eq=rx[1].map(function(s){return (s.coef>1?s.coef:'')+s.formula;}).join(' + ')+' -> '+rx[2].map(function(s){return (s.coef>1?s.coef:'')+s.formula;}).join(' + ');
    rec.title='Signature reaction study '+n+': '+rx[0];
    rec.description='A teaching record for the balanced reaction "'+eq+'". Atom counts balance on both sides; stoichiometry is verified by the independent checker. Educational model.';
    rec.reaction_name=rx[0];rec.equation=eq;
    rec.reactants=rx[1];rec.products=rx[2];rec.balanced=true;
  }else if(cat==='organic'||cat==='inorganic'){
    var o=pick(ORG,rnd),n2=ri(rnd,1,80);
    var comp=cat==='organic'?{C:ri(rnd,1,6),H:ri(rnd,4,14),O:ri(rnd,0,3)}:{Na:1,Cl:1};
    if(cat==='inorganic'){var salts=[{K:1,Cl:1},{Ca:1,O:1},{Mg:1,O:1},{Na:1,O:1,H:1},{K:1,N:1,O:3}];comp=pick(salts,rnd);}
    var f=fmt(comp);
    rec.title='Signature compound study '+n2+': '+f;
    rec.description='A teaching record for the model compound '+f+' ('+o[1]+'), molar mass '+mm(comp)+' g/mol computed from standard atomic weights. Educational model.';
    rec.formula=f;rec.composition=comp;rec.molar_mass_g_mol=mm(comp);
    rec.compound_class=o[1];
    rec.safety_note='Treat all laboratory substances with standard safety practice; this is a teaching model.';
  }else if(cat==='physical'){
    var ph=pick(PHYS,rnd);
    rec.title='Physical chemistry concept: '+ph[0];
    rec.description='A teaching record: '+ph[0]+' - '+ph[1]+'. Covers the concept in general educational terms with the defining relation stated exactly.';
    rec.concept=ph[0];rec.statement=ph[1];
  }else{
    var lb=pick(LABM,rnd);
    rec.title='Laboratory technique: '+lb[0];
    rec.description='A teaching record for '+lb[0]+' ('+lb[1]+'). Covers principle, basic steps, and reading the result in general educational terms.';
    rec.technique=lb[0];rec.principle=lb[1];
    rec.steps=['Prepare equipment and sample','Run the procedure per teaching protocol','Record and interpret the result'];
  }
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-CHEM-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.category==='reactions'){
    if(!sameAtoms(atoms(r.reactants||[]),atoms(r.products||[])))e.push('unbalanced');
    if(r.balanced!==true)e.push('balanced');
    if(typeof r.equation!=='string'||!r.equation.length)e.push('equation');
  }
  if(r.category==='organic'||r.category==='inorganic'){
    if(!r.composition||typeof r.composition!=='object')e.push('composition');
    else{
      var m=mm(r.composition);
      if(Math.abs(m-(r.molar_mass_g_mol||0))>0.05)e.push('molar_mass');
      for(var el in r.composition)if(!(el in AW))e.push('element:'+el);
      if(r.formula!==fmt(r.composition))e.push('formula');
    }
  }
  if(r.category==='physical'&&typeof r.statement!=='string')e.push('statement');
  if((r.category==='flavor'||r.category==='kitchen')&&typeof r.statement!=='string')e.push('statement');
  if(r.category==='lab'&&typeof r.technique!=='string')e.push('technique');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-chemistry-1.0',generate:generate,validate:validate,atomicWeights:AW,molarMass:mm,formulaOf:fmt,atomCounts:atoms,balancedAtoms:sameAtoms};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chemistry',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
