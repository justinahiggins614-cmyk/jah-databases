(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="motherboards-signature";
var VERSION="jahdb-motherboards-signature-1.0";
var PREFIX="JAH-MBD-S-";
var KIND="motherboard";
var CATS=["compute","compact","workstation","experimental"];
/* base templates: [category, ...fields] */
var B=[["compute", "Meridian", "JAH-S1", "JAH-X1", "ATX", "DDR5", "yes", 48, 4], ["compact", "Meridian", "JAH-S1", "JAH-B1", "Mini-ITX", "DDR5", "yes", 24, 2], ["workstation", "Strata", "JAH-S2", "JAH-WX", "E-ATX", "DDR5 ECC", "yes", 128, 6], ["compact", "Pebble", "JAH-M1", "JAH-N1", "Mini-ITX", "DDR5", "yes", 20, 1], ["experimental", "Meridian", "JAH-S1", "JAH-X1", "E-ATX", "DDR5", "yes", 64, 6], ["compute", "Forge", "JAH-S1", "JAH-I1", "ATX", "DDR5 ECC", "no", 32, 3]];
var SRC='signature-generated-completion';

function buildRec(b,rnd){
  var title='JAH '+b[1]+' '+b[2].replace('JAH-','')+'-'+(1+(rnd()*9|0))+' '+b[3].replace('JAH-','')+' Concept Board';
  var desc='The '+title+' is a Signature-original '+b[0]+' motherboard concept in the '+b[1]+
    ' family, designed by Justin Addam Higgins. Its concept specification calls for the '+b[2]+
    ' socket, '+b[3]+' chipset, '+b[7]+' PCIe lanes and '+b[8]+' M.2 slots. '+
    'This is an original design concept, not a real product and not affiliated with any vendor.';
  return {title:title,description:desc,concept_family:b[1],category:b[0],
    concept_specs:{socket:b[2],chipset:b[3],form_factor:b[4],memory_type:b[5],wifi:b[6],
      pcie_lanes:b[7],m2_slots:b[8]},
    demo:'LANES='+b[7]+'\nM2='+b[8]+'\nprint("Free lanes for add-in cards: %d" % (LANES-16-M2*4))'};
}
function extraValidate(r,e){
  var cs=r.concept_specs||{};
  if(typeof cs.socket!=='string'||!cs.socket.length)e.push('socket');
  if(!(cs.pcie_lanes>=16))e.push('pcie_lanes');
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
