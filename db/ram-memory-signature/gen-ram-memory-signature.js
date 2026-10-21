(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="ram-memory-signature";
var VERSION="jahdb-ram-memory-signature-1.0";
var PREFIX="JAH-MEMORY-S-";
var KIND="memory module";
var CATS=["concept-memory","experimental","low-power"];
/* base templates: [category, ...fields] */
var B=[["concept-memory", "LoomWeave", "D5-X", "Phase-Cell Module", 32, 8400, 36, "DIMM", "no"], ["concept-memory", "Threadline", "T4", "Tight-Timing Kit", 16, 3600, 12, "DIMM", "no"], ["experimental", "VaultCore", "V-ECC", "Server Concept", 64, 6400, 40, "DIMM", "yes"], ["low-power", "PocketWeave", "PW-SOD", "Laptop Concept", 32, 6400, 44, "SO-DIMM", "no"], ["low-power", "FrostCell", "F-LP", "Low-Volt Concept", 16, 5200, 42, "DIMM", "no"], ["experimental", "VaultCore", "V-RD", "Datacenter Concept", 128, 5600, 44, "DIMM", "yes"]];
var SRC='signature-generated-completion';

function buildRec(b,rnd){
  var cap=b[4], mt=b[5]+(rnd()<0.5?0:200);
  var title='JAH '+b[1]+' '+b[2]+'-'+(1+(rnd()*9|0))+' '+b[3];
  var desc='The '+title+' is a Signature-original '+b[0].replace(/-/g,' ')+
    ' memory concept in the '+b[1]+' family, designed by Justin Addam Higgins. Its concept specification calls for '+
    cap+' GB at '+mt+' MT/s with CL'+b[6]+' timings. '+
    'This is an original design concept, not a real product and not affiliated with any vendor.';
  return {title:title,description:desc,concept_family:b[1],category:b[0],
    concept_specs:{capacity_gb:cap,speed_mt_s:mt,cas_latency:b[6],form_factor:b[7],ecc:b[8],
      voltage_v:1.1,interface:'concept DDR-class'},
    demo:'MT='+mt+'\nCL='+b[6]+'\nprint("Concept true latency: %.2f ns" % (CL*2000.0/MT))'};
}
function extraValidate(r,e){
  var cs=r.concept_specs||{};
  if(!(cs.capacity_gb>=4))e.push('capacity_gb');
  if(!(cs.speed_mt_s>=1000))e.push('speed_mt_s');
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
