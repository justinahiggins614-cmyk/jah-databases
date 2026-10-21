(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="pc-cases-signature";
var VERSION="jahdb-pc-cases-signature-1.0";
var PREFIX="JAH-CHASSIS-S-";
var KIND="pc case";
var CATS=["showcase","airflow","silent","compact","full-tower","experimental"];
/* base templates: [category, ...fields] */
var B=[["showcase", "Sanctum", "Mid-tower", "ATX", 420, 360, 10, 55.0, "Aluminum + glass"], ["airflow", "Sanctum", "Mid-tower", "ATX", 400, 360, 9, 50.0, "Steel + mesh"], ["silent", "Haven", "Mid-tower", "ATX", 410, 360, 7, 52.0, "Steel + dampened panels"], ["compact", "Haven", "Mini-ITX SFF", "Mini-ITX", 320, 240, 5, 12.5, "Aluminum"], ["full-tower", "Bastion", "Full-tower", "E-ATX", 480, 420, 12, 90.0, "Steel + glass"], ["experimental", "Sanctum", "Cube", "Micro-ATX", 380, 280, 8, 40.0, "Aluminum + glass"]];
var SRC='signature-generated-completion';

function buildRec(b,rnd){
  var gpu=b[4]+ri(rnd,-10,10);
  var title='JAH '+b[1]+' '+(1+(rnd()*9|0))+' '+b[0]+' Case Concept';
  var desc='The '+title+' is a Signature-original '+b[0]+' case concept in the '+b[1]+
    ' family, designed by Justin Addam Higgins. Its concept specification calls for a '+b[2]+
    ' chassis fitting '+b[3]+' boards with '+gpu+' mm of GPU clearance. '+
    'This is an original design concept, not a real product and not affiliated with any vendor.';
  return {title:title,description:desc,concept_family:b[1],category:b[0],
    concept_specs:{size_class:b[2],motherboard_support:b[3],max_gpu_length_mm:gpu,
      max_radiator_mm:b[5],fan_slots:b[6],volume_liters:b[7],materials:b[8]},
    demo:'GPU='+gpu+'\nprint("Concept GPU clearance: %d mm" % GPU)'};
}
function extraValidate(r,e){
  var cs=r.concept_specs||{};
  if(!(cs.max_gpu_length_mm>=150))e.push('max_gpu_length_mm');
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec=buildRec(b,rnd); rec.id=id; rec.t=rec.title; rec.g=rec.category; rec.c=1;
  rec.record_kind=KIND; rec.ladder_rank=1+(seed%3); rec.src=SRC; rec.signature_original=true; rec._seed=seed;
  rec.provenance='Original hardware concept authored for the JAH Databases Signature collection.';
  rec.last_verified='2026-10-20';
  return rec;
}


function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(r.src!==SRC)e.push('src');
  if(r.signature_original!==true)e.push('signature_original');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(typeof r.demo!=='string'||r.demo.length<20)e.push('demo');
  extraValidate(r,e);
  return{ok:!e.length,errors:e};
}

function driftCheck(rec,sample){var e=[];if(!Array.isArray(sample))return{ok:true,errors:e};for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)e.push('duplicate-title');}return{ok:!e.length,errors:e};}

var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
