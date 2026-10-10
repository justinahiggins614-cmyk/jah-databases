(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['xray','mri','ct','ultrasound','protocols'];
var PREFIX='JAH-IMG-';
var MODS={
 xray:['X-ray radiography','ionizing electromagnetic radiation projected through tissue onto a detector'],
 mri:['Magnetic resonance imaging','strong magnetic field plus radiofrequency pulses exciting hydrogen nuclei'],
 ct:['Computed tomography','rotating X-ray tube and detectors reconstructing cross-sectional slices'],
 ultrasound:['Ultrasound','high-frequency sound waves reflected at tissue interfaces'],
 protocols:['Imaging protocol','a standardized sequence of acquisitions and reconstructions']
};
var IND={xray:['suspected fracture','chest evaluation'],mri:['soft-tissue characterization','neurologic evaluation'],ct:['trauma survey','acute hemorrhage detection'],ultrasound:['pregnancy assessment','abdominal organ survey'],protocols:['standardized acquisition','reproducible comparison']};
var CONTRA={xray:['pregnancy without shielding justification','repeat exposure without indication'],mri:['incompatible implanted devices','severe claustrophobia unaddressed'],ct:['pregnancy without justification','contrast allergy for contrast phases'],ultrasound:['none significant; avoid overuse'],protocols:['deviation without documentation']};
var STEPS=[['position the region of interest','set acquisition parameters','acquire and verify image quality'],['confirm patient identity and indication','apply the standard sequence','review and annotate the study'],['prepare equipment and safety checks','run the acquisition protocol','archive with annotations']];
var MODNAMES=[];for(var k in MODS)MODNAMES.push(MODS[k][0]);
var PRIV='Synthetic test case. Contains no real patient data and no protected health information.';
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var m=MODS[cat];
  var n=ri(rnd,1,80);
  var desc='A Signature-generated imaging study record for '+m[0]+' ('+m[1]+'). '+
    'This is a synthetic teaching case: '+PRIV+' Covers indications, contraindications, and protocol steps in general educational terms.';
  return {id:id,title:'Signature imaging study '+n+': '+m[0],category:cat,description:desc,
    modality:m[0],principle:m[1],
    indications:IND[cat].slice(),contraindications:CONTRA[cat].slice(),
    protocol_steps:pick(STEPS,rnd).slice(),
    annotation_guidelines:'Label anatomy, mark findings with standard terms, and record acquisition parameters.',
    performance_notes:'Synthetic benchmark notes for teaching; not measured clinical performance.',
    privacy_note:PRIV,source:'signature',source_ref:'JAH Signature Generator',
    creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-IMG-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.source==='signature'){if(MODNAMES.indexOf(r.modality)<0)e.push('modality');}
  else if(typeof r.modality!=='string'||!r.modality.length)e.push('modality');
  if(typeof r.principle!=='string'||!r.principle.length)e.push('principle');
  if(!Array.isArray(r.indications)||!r.indications.length)e.push('indications');
  if(!Array.isArray(r.contraindications)||!r.contraindications.length)e.push('contraindications');
  if(!Array.isArray(r.protocol_steps)||!r.protocol_steps.length)e.push('protocol_steps');
  if(typeof r.privacy_note!=='string'||!/no real patient data/i.test(r.privacy_note))e.push('privacy_note');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-medical-imaging-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('medical-imaging',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
