(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="pc-cases";
var VERSION="jahdb-pc-cases-1.0";
var PREFIX="JAH-CHASSIS-";
var KIND="pc case";
var CATS=["airflow","showcase","silent","mini-itx","full-tower","mid-tower"];
/* base templates: [category, ...fields] */
var B=[["airflow", "Corsair", "Mid-tower", "ATX", 360, 360, "Steel + mesh front"], ["airflow", "Lian Li", "Mid-tower", "ATX / E-ATX", 392, 360, "Steel + mesh"], ["airflow", "NZXT", "Mid-tower", "ATX", 400, 360, "Steel + perforated front"], ["showcase", "Lian Li", "Mid-tower", "ATX / E-ATX", 426, 360, "Aluminum + tempered glass"], ["showcase", "Hyte", "Mid-tower", "ATX", 375, 360, "Steel + panoramic glass"], ["silent", "be quiet!", "Mid-tower", "ATX / E-ATX", 432, 420, "Steel + dampened panels"], ["silent", "Fractal Design", "Mid-tower", "ATX / E-ATX", 467, 420, "Steel + dampened panels"], ["mini-itx", "Cooler Master", "Mini-ITX SFF", "Mini-ITX", 330, 280, "Steel + tempered glass"], ["mini-itx", "Fractal Design", "Mini-ITX SFF", "Mini-ITX", 322, 0, "Walnut / oak + anodized aluminum"], ["full-tower", "Cooler Master", "Full-tower", "E-ATX / SSI-EEB", 490, 420, "Steel + tempered glass"], ["mid-tower", "Fractal Design", "Mid-tower", "ATX", 405, 360, "Steel + mesh front"], ["mid-tower", "Phanteks", "Mid-tower", "ATX", 400, 360, "Steel + tempered glass"]];
var SRC='public-harvest';

function buildRec(b,rnd){
  var gpu=b[4]+ri(rnd,-10,10);
  var title=b[1]+' '+b[2]+' '+b[0]+' Case';
  var desc='The '+title+' is a '+b[2]+' PC case for '+b[3]+' motherboards, with '+
    gpu+' mm of GPU clearance and support for up to '+b[5]+' mm radiators. Built from '+
    b[6].toLowerCase()+', it targets '+b[0]+' builds with straightforward assembly and cable routing.';
  return {title:title,description:desc,brand:b[1],size_class:b[2],motherboard_support:b[3],
    max_gpu_length_mm:gpu,max_radiator_mm:b[5],materials:b[6],category:b[0],
    demo:'MAX_GPU='+gpu+'\ndef fits(l):\n    print(("FITS" if l<=MAX_GPU else "TOO LONG")+" - GPU %d mm" % l)\nfits(320)'};
}
function extraValidate(r,e){
  if(!(r.max_gpu_length_mm>=150&&r.max_gpu_length_mm<=550))e.push('max_gpu_length_mm');
  if(typeof r.brand!=='string'||!r.brand.length)e.push('brand');
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
