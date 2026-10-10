(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['skeletal','muscular','nervous','circulatory','organs'];
var PREFIX='JAH-ANA-';
var STRUCT={
 skeletal:[['Long bone model','appendicular','diaphysis and epiphyses','long'],['Flat bone model','axial','cranial vault','flat'],['Short bone model','appendicular','carpal group','short'],['Irregular bone model','axial','vertebral body','irregular'],['Sesamoid bone model','appendicular','patellar region','sesamoid']],
 muscular:[['Skeletal muscle fiber model','limb','sarcomere unit','striated'],['Smooth muscle sheet model','visceral wall','organ wall','smooth'],['Cardiac muscle model','thoracic','myocardium','cardiac'],['Tendon junction model','musculotendinous','tendon interface','connective']],
 nervous:[['Motor neuron model','spinal cord','anterior horn','motor'],['Sensory neuron model','dorsal root','ganglion','sensory'],['Interneuron model','central','gray matter','association'],['Myelinated axon model','peripheral','nerve trunk','myelinated']],
 circulatory:[['Artery segment model','systemic','arterial wall','artery'],['Vein segment model','systemic','venous wall','vein'],['Capillary bed model','micro','exchange zone','capillary'],['Heart chamber model','thoracic','myocardium','chamber']],
 organs:[['Parenchymal organ model','abdominal','capsule','solid'],['Hollow organ model','abdominal','lumen','hollow'],['Glandular tissue model','endocrine','lobule','gland'],['Lymphoid tissue model','immune','follicle','lymphoid']]
};
var FUNC={
 skeletal:['provides structural support for the body frame','serves as a lever for muscle-driven movement','houses marrow involved in blood cell formation'],
 muscular:['converts chemical energy into contractile force','stabilizes joints during movement','generates heat through sustained contraction'],
 nervous:['transmits electrochemical signals between tissues','integrates sensory input into motor output','coordinates rapid reflex responses'],
 circulatory:['transports blood between heart and tissues','regulates pressure across the vascular tree','enables exchange at the microcirculation'],
 organs:['performs the specialized work of its tissue type','maintains local homeostasis within its capsule','interacts with neighboring systems']
};
var CLIN={
 skeletal:'Fractures heal through callus formation and remodeling under mechanical load.',
 muscular:'Strain injuries follow the overload principle and recover with graded loading.',
 nervous:'Peripheral axons can regenerate slowly after injury when the pathway remains intact.',
 circulatory:'Vessel walls remodel in response to sustained changes in pressure and flow.',
 organs:'Organ function is assessed through tissue-specific functional tests.'
};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var s=pick(STRUCT[cat],rnd);
  var variant=ri(rnd,1,40);
  var title=s[0].replace(' model','')+' — Signature study model '+variant;
  var f1=pick(FUNC[cat],rnd),f2=pick(FUNC[cat],rnd);
  var desc='A Signature-generated anatomical study model of a '+s[3]+' '+cat+' structure in the '+s[1]+' region. '+
    'It illustrates '+f1+' and '+f2+'. Educational model; not a verified clinical reference.';
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:title,category:cat,description:desc,region:s[1],structure_type:s[3],
    latin_name:'modelum anatomicum '+variant,
    functions:[f1[0].toUpperCase()+f1.slice(1)+'.',f2[0].toUpperCase()+f2.slice(1)+'.'],
    related_structures:[pick(STRUCT[cat],rnd)[0].replace(' model',''),pick(STRUCT[cat],rnd)[0].replace(' model','')],
    clinical_notes:CLIN[cat],source:'signature',source_ref:'JAH Signature Generator',
    creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ANA-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(typeof r.region!=='string'||!r.region.length)e.push('region');
  if(typeof r.structure_type!=='string'||!r.structure_type.length)e.push('structure_type');
  if(!Array.isArray(r.functions)||r.functions.length<1)e.push('functions');
  if(!Array.isArray(r.related_structures)||r.related_structures.length<1)e.push('related_structures');
  if(typeof r.clinical_notes!=='string'||!r.clinical_notes.length)e.push('clinical_notes');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(typeof r.source_ref!=='string'||!r.source_ref.length)e.push('source_ref');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-anatomy-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('anatomy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
