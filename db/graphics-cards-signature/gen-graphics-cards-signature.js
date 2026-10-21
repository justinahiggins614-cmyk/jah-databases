(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="graphics-cards-signature";
var VERSION="jahdb-graphics-cards-signature-1.0";
var PREFIX="JAH-GCARD-S-";
var KIND="graphics card";
var CATS=["compute","gaming","workstation","experimental"];
/* base templates: [category, ...fields] */
var B=[["compute", "Helios", "GX", "Spectral Compute Unit", 24576, 32, "GDDR7", 512, 2.8, 380, 320], ["gaming", "Helios", "GX", "Gaming Vector Card", 16384, 24, "GDDR7", 384, 3.0, 320, 300], ["workstation", "Titan Veil", "VX", "Workstation Engine", 20480, 48, "GDDR6 ECC", 384, 2.4, 300, 267], ["gaming", "Aurora Mesh", "MX", "Mesh Shader Card", 12288, 16, "GDDR6", 256, 2.7, 240, 280], ["experimental", "Nebula Weave", "NW", "Chiplet GPU", 28672, 64, "HBM3", 4096, 2.2, 500, 340], ["compute", "Quantum Drift", "QD", "Edge AI Card", 8192, 16, "GDDR6", 256, 2.0, 120, 220]];
var SRC='signature-generated-completion';

function buildRec(b,rnd){
  var lanes=b[4]+ri(rnd,-512,512);
  var boost=rf(rnd,Math.max(1.5,b[8]-0.1),b[8]+0.1,2);
  var title='JAH '+b[1]+' '+b[2]+'-'+(1+(rnd()*9|0))+' '+b[3];
  var desc='The '+title+' is a Signature-original '+b[0]+' graphics concept in the '+b[1]+
    ' family, designed by Justin Addam Higgins. Its concept specification calls for '+
    lanes.toLocaleString()+' compute lanes and '+b[5]+' GB of '+b[6]+' memory. '+
    'This is an original design concept, not a real product and not affiliated with any vendor.';
  return {title:title,description:desc,concept_family:b[1],category:b[0],
    concept_specs:{compute_lanes:lanes,vram_gb:b[5],vram_type:b[6],memory_bus_bits:b[7],
      boost_clock_ghz:boost,tdp_w:b[9],length_mm:b[10],interface:'PCIe 5.0 x16 (concept)'},
    demo:'LANES='+lanes+'\nCLOCK='+boost+'\nprint("Theoretical FP32: %.1f TFLOPS" % (LANES*CLOCK*2/1000))'};
}
function extraValidate(r,e){
  var cs=r.concept_specs||{};
  if(!(cs.compute_lanes>0))e.push('compute_lanes');
  if(!(cs.vram_gb>=4))e.push('vram_gb');
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
