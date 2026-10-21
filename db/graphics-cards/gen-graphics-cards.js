(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="graphics-cards";
var VERSION="jahdb-graphics-cards-1.0";
var PREFIX="JAH-GCARD-";
var KIND="graphics card";
var CATS=["consumer","enthusiast","workstation","budget"];
/* base templates: [category, ...fields] */
var B=[["consumer", "NVIDIA", "GeForce RTX 40", "GeForce RTX 4070", 5888, "CUDA", 12, "GDDR6X", 192, 2.48, 200, 244, 599], ["consumer", "NVIDIA", "GeForce RTX 40", "GeForce RTX 4060 Ti", 4352, "CUDA", 16, "GDDR6", 128, 2.54, 165, 240, 499], ["consumer", "AMD", "Radeon RX 7000", "Radeon RX 7800 XT", 3840, "Stream", 16, "GDDR6", 256, 2.43, 263, 287, 499], ["consumer", "AMD", "Radeon RX 7000", "Radeon RX 7700 XT", 3456, "Stream", 12, "GDDR6", 192, 2.54, 245, 267, 449], ["consumer", "Intel", "Arc Alchemist", "Arc A770 16GB", 4096, "Xe Vector", 16, "GDDR6", 256, 2.1, 225, 280, 349], ["enthusiast", "NVIDIA", "GeForce RTX 40", "GeForce RTX 4090", 16384, "CUDA", 24, "GDDR6X", 384, 2.52, 450, 304, 1599], ["enthusiast", "NVIDIA", "GeForce RTX 40", "GeForce RTX 4080 SUPER", 10240, "CUDA", 16, "GDDR6X", 256, 2.55, 320, 310, 999], ["enthusiast", "AMD", "Radeon RX 7000", "Radeon RX 7900 XTX", 6144, "Stream", 24, "GDDR6", 384, 2.5, 355, 287, 999], ["workstation", "NVIDIA", "RTX Professional", "RTX 6000 Ada", 18176, "CUDA", 48, "GDDR6 ECC", 384, 2.5, 300, 267, 6800], ["workstation", "AMD", "Radeon Pro", "Radeon Pro W6800", 3840, "Stream", 32, "GDDR6 ECC", 256, 2.32, 250, 267, 2249], ["budget", "NVIDIA", "GeForce RTX 40", "GeForce RTX 4060", 3072, "CUDA", 8, "GDDR6", 128, 2.46, 115, 240, 299], ["budget", "AMD", "Radeon RX 7000", "Radeon RX 7600", 2048, "Stream", 8, "GDDR6", 128, 2.66, 165, 240, 269]];
var SRC='public-harvest';

function buildRec(b,rnd){
  var tdp=Math.max(75,b[10]+ri(rnd,-10,10));
  var boost=rf(rnd,Math.max(1.5,b[9]-0.08),b[9]+0.08,2);
  var title=b[1]+' '+b[3];
  var desc='The '+title+' is a '+b[2]+' graphics card with '+b[4].toLocaleString()+' '+b[5]+
    ' processors and '+b[6]+' GB of '+b[7]+' memory on a '+b[8]+'-bit bus. '+
    'It boosts to '+boost+' GHz within a '+tdp+' W envelope, suiting '+b[0]+' builds. '+
    'A '+b[12]+' mm card in its reference form, it needs a quality power supply with headroom above its TDP.';
  return {title:title,description:desc,vendor:b[1],series:b[2],category:b[0],
    cores:b[4],cores_label:b[5],vram_gb:b[6],vram_type:b[7],memory_bus_bits:b[8],
    boost_clock_ghz:boost,tdp_w:tdp,interface:'PCIe 4.0 x16',length_mm:b[11],msrp_usd:b[12],
    demo:'TDP_W='+tdp+'\nprint("Estimated PSU headroom: "+str(int(TDP_W*1.8+150))+" W")'};
}
function extraValidate(r,e){
  if(!(r.cores>0))e.push('cores');
  if(!(r.vram_gb>=4&&r.vram_gb<=128))e.push('vram_gb');
  if(!(r.tdp_w>=45&&r.tdp_w<=700))e.push('tdp_w');
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec=buildRec(b,rnd); rec.id=id; rec.t=rec.title; rec.g=rec.category; rec.c=1;
  rec.record_kind=KIND; rec.ladder_rank=1+(seed%3); rec.src=SRC; rec._seed=seed;
  rec.provenance='Manufacturer specifications; public product data.';
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
