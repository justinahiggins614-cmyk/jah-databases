(function(){'use strict';
/* JAH Nanotechnology Database generator — jahdb-nanotechnology-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record. src:"online" = material facts
   verified against published nanotechnology references; src:"signature" = Signature-authored
   nanomaterial study (clearly labeled; no invented real-world facts). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=['carbon-materials','2d-materials','nanoparticles','nanowires','fabrication','applications'];
var PREFIX='JAH-NANO-';
var GRAPHENE={
 tensile_strength:'130 GPa intrinsic',youngs_modulus:'1 TPa',thermal_conductivity:'1500–5000 W/(m·K)',
 thickness:'0.345 nm (one atom)',electron_mobility:'200,000 cm²/(V·s) at room temperature',
 optical_absorption:'2.3% of visible light (nearly transparent)',electronic:'zero-gap semiconductor',
 discovered:'isolated in 2004 by Andre Geim and Konstantin Novoselov by mechanical exfoliation of graphite',
 nobel:'2010 Nobel Prize in Physics'
};
var CNT={tensile_strength:'~100 GPa intrinsic',youngs_modulus:'~1 TPa',dimensionality:'1D fiber/cylinder',best_for:'composite reinforcement and fibers'};
var METHODS={
 'mechanical exfoliation':'Peeling atomic layers from bulk graphite — the 2004 method that first isolated graphene.',
 'chemical vapor deposition':'Growing films from vapor precursors; the most common mass-production method for graphene.',
 'arc discharge':'Vaporizing carbon electrodes in inert gas to grow nanotubes.',
 'laser ablation':'Vaporizing a graphite target with a laser to form nanotubes.',
 'sol-gel process':'Forming nanoparticles from a liquid chemical solution.',
 'molecular beam epitaxy':'Depositing atomic layers one at a time in ultra-high vacuum.'
};
var MATS={
 'carbon-materials':[
  ['graphene monolayer','carbon',{tensile_strength:GRAPHENE.tensile_strength,youngs_modulus:GRAPHENE.youngs_modulus,thermal_conductivity:GRAPHENE.thermal_conductivity},'chemical vapor deposition'],
  ['graphene bilayer','carbon',{electronic:'tunable bandgap under electric field',thickness:'0.69 nm'},'chemical vapor deposition'],
  ['graphene nanoribbon','carbon',{electronic:'bandgap depends on width and edge shape',width:'under 10 nm typical'},'lithographic patterning of graphene'],
  ['carbon nanotube (single-wall)','carbon',CNT,'arc discharge'],
  ['carbon nanotube (multi-wall)','carbon',{tensile_strength:'~100 GPa class',dimensionality:'concentric 1D cylinders'},'chemical vapor deposition'],
  ['fullerene C60','carbon',{structure:'60 carbon atoms in a soccer-ball cage',diameter:'0.7 nm'},'arc discharge']
 ],
 '2d-materials':[
  ['graphene monolayer','2D',{tensile_strength:GRAPHENE.tensile_strength,optical_absorption:GRAPHENE.optical_absorption},'chemical vapor deposition'],
  ['graphene oxide','2D',{chemistry:'graphene functionalized with oxygen groups',dispersibility:'disperses in water'},'chemical oxidation of graphite'],
  ['reduced graphene oxide','2D',{conductivity:'partially restored versus graphene oxide',production:'made by chemical or thermal reduction of graphene oxide'},'chemical or thermal reduction'],
  ['graphene nanomesh','2D',{structure:'graphene sheet with a nanoscale hole array',electronic:'bandgap opened by the mesh pattern'},'block-copolymer lithography']
 ],
 'nanoparticles':[
  ['gold nanoparticle','0D',{definition:'1–100 nm in at least one dimension',optical:'size-tunable surface plasmon resonance'},'sol-gel process'],
  ['silver nanoparticle','0D',{definition:'1–100 nm in at least one dimension',antimicrobial:'studied for antimicrobial coatings'},'chemical reduction'],
  ['titanium dioxide nanoparticle','0D',{definition:'1–100 nm in at least one dimension',uv:'absorbs ultraviolet light'},'sol-gel process'],
  ['silica nanoparticle','0D',{definition:'1–100 nm in at least one dimension',use:'fillers and catalyst supports'},'Stöber process'],
  ['iron oxide nanoparticle','0D',{definition:'1–100 nm in at least one dimension',magnetic:'superparamagnetic below ~20 nm'},'co-precipitation']
 ],
 'nanowires':[
  ['silicon nanowire','1D',{diameter:'10–100 nm typical',battery:'studied as high-capacity lithium-ion anodes'},'vapor-liquid-solid growth'],
  ['zinc oxide nanowire','1D',{diameter:'10–100 nm typical',piezoelectric:'studied for nanogenerators'},'chemical vapor deposition'],
  ['silver nanowire','1D',{diameter:'20–100 nm typical',transparent:'studied for transparent conductive films'},'polyol process'],
  ['gallium nitride nanowire','1D',{diameter:'10–100 nm typical',optical:'studied for nanoscale LEDs'},'molecular beam epitaxy']
 ]
};
var APPL=[
 ['lithium-ion battery anodes','Silicon nanowires are studied as high-capacity anodes because they swell less destructively than bulk silicon.'],
 ['transparent conductive films','Silver nanowire meshes and graphene are studied as replacements for brittle indium tin oxide.'],
 ['composite reinforcement','Carbon nanotubes carry load in polymer matrices far beyond the strength of steel by weight.'],
 ['water filtration membranes','Graphene-oxide membranes are studied for selective water permeation and desalination.'],
 ['rapid diagnostic tests','Gold nanoparticles give the visible red line in lateral-flow test strips.'],
 ['sunscreens','Titanium dioxide and zinc oxide nanoparticles absorb and scatter ultraviolet light.'],
 ['flexible electronics','Graphene\u2019s strength and conductivity suit bendable displays and sensors.'],
 ['drug delivery carriers','Nanoparticles are studied as carriers that release medicine at targeted sites.']
];
var SCALE='The nanoscale runs 1–100 nm; a nanometer is a billionth of a meter — about 100,000 times smaller than a human hair\u2019s width.';
function build(rnd,cat){
 var online=rnd()<0.62;
 var title,desc,sp,src=online?'online':'signature';
 if(cat==='fabrication'){
  var m=pick(Object.keys(METHODS),rnd);
  title='Fabrication — '+m;
  desc=(online?'':'This is a Signature-authored fabrication study. ')+METHODS[m]+' '+
   'Method class: '+(m==='mechanical exfoliation'?'top-down':'bottom-up')+'. '+SCALE;
  sp={method:m,description:METHODS[m],method_class:m==='mechanical exfoliation'?'top-down':'bottom-up',scale_note:SCALE};
  src='online';
 }else if(cat==='applications'){
  var a=pick(APPL,rnd);
  title='Application — '+a[0];
  desc=(online?'Reference application record. ':'This is a Signature-authored application study. ')+a[1]+' '+SCALE;
  sp={application:a[0],detail:a[1],scale_note:SCALE};
  src=online?'online':'signature';
 }else{
  var e=pick(MATS[cat],rnd);
  var mat=e[0],kind=e[1],props=e[2],meth=e[3];
  var propStr=Object.keys(props).map(function(k){return k.replace(/_/g,' ')+': '+props[k];}).join('; ');
  title=cap(mat)+' — '+cat.replace(/-/g,' ');
  desc=(online?'':'This is a Signature-authored nanomaterial study. ')+
   'The '+mat+' is a '+kind+' nanomaterial with '+propStr+'. '+
   'Fabrication route: '+meth+'. '+SCALE;
  sp={material:mat,dimensionality:kind,key_properties:props,fabrication_method:meth,scale_note:SCALE};
 }
 return {title:title,description:desc,src:src,spec:sp};
}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function generate(seed,opts,rnd){
 opts=opts||{};rnd=rnd||prng(seed);
 var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
 var b=build(rnd,cat);
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,category:cat,src:b.src,spec:b.spec,_seed:seed};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-NANO-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<10)e.push('title');
 if(typeof r.description!=='string'||r.description.length<80)e.push('description');
 if(CATS.indexOf(r.category)<0)e.push('category');
 if(r.src!=='online'&&r.src!=='signature')e.push('src');
 var s=r.spec;
 if(!s||typeof s!=='object')e.push('spec');
 else{
  if(r.category==='fabrication'){
   if(typeof s.method!=='string'||!METHODS[s.method])e.push('spec.method');
  }else if(r.category==='applications'){
   if(typeof s.application!=='string'||!s.application)e.push('spec.application');
  }else{
   if(typeof s.material!=='string'||!s.material)e.push('spec.material');
   if(!s.key_properties||typeof s.key_properties!=='object'||Object.keys(s.key_properties).length<2)e.push('spec.key_properties');
   if(typeof s.fabrication_method!=='string'||!s.fabrication_method)e.push('spec.fabrication_method');
  }
 }
 return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-nanotechnology-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanotech',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
