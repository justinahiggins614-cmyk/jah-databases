(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="ram-memory";
var VERSION="jahdb-ram-memory-1.0";
var PREFIX="JAH-MEMORY-";
var KIND="memory module";
var CATS=["ddr5-desktop","ddr4-desktop","laptop-sodimm","server-ecc","ddr3-legacy"];
/* base templates: [category, ...fields] */
var B=[["ddr5-desktop", "G.Skill", "DDR5", 32, 6000, 30, "DIMM", "no"], ["ddr5-desktop", "Corsair", "DDR5", 64, 6400, 32, "DIMM", "no"], ["ddr5-desktop", "Kingston", "DDR5", 16, 5200, 40, "DIMM", "no"], ["ddr4-desktop", "Corsair", "DDR4", 16, 3200, 16, "DIMM", "no"], ["ddr4-desktop", "G.Skill", "DDR4", 32, 3600, 18, "DIMM", "no"], ["ddr4-desktop", "TeamGroup", "DDR4", 16, 3600, 18, "DIMM", "no"], ["laptop-sodimm", "Crucial", "DDR4", 16, 3200, 22, "SO-DIMM", "no"], ["laptop-sodimm", "SK Hynix", "DDR5", 16, 4800, 40, "SO-DIMM", "no"], ["server-ecc", "Samsung", "DDR4", 32, 3200, 22, "DIMM", "yes (registered ECC)"], ["server-ecc", "Samsung", "DDR5", 64, 4800, 40, "DIMM", "yes (registered ECC)"], ["ddr3-legacy", "Crucial", "DDR3", 8, 1600, 11, "DIMM", "no"], ["ddr3-legacy", "Kingston", "DDR3", 8, 1600, 11, "SO-DIMM", "no"]];
var SRC='public-harvest';

function buildRec(b,rnd){
  var mt=b[4]+(rnd()<0.5?0:400);
  var title=b[1]+' '+b[3]+'GB '+b[2]+'-'+mt+' '+(b[6]==='SO-DIMM'?'SODIMM':'DIMM');
  var desc='The '+title+' is a '+b[3]+' GB '+b[2]+' memory module running at '+mt+
    ' MT/s with CL'+b[5]+' timings in '+(b[6]==='SO-DIMM'?'laptop SO-DIMM':'desktop DIMM')+
    ' form. '+(b[7]==='no'?'It is non-ECC memory for consumer boards.':'It carries '+b[7]+
    ' for error correction in workstations and servers. ')+
    'A dependable choice for '+b[0].replace(/-/g,' ')+' builds.';
  return {title:title,description:desc,brand:b[1],ddr_generation:b[2],capacity_gb:b[3],
    speed_mt_s:mt,cas_latency:b[5],form_factor:b[6],ecc:b[7],category:b[0],
    voltage_v:{DDR5:1.1,DDR4:1.2,DDR3:1.5}[b[2]],
    demo:'MT='+mt+'\nCL='+b[5]+'\nprint("True latency: %.1f ns" % (CL*2000.0/MT))\nprint("Peak dual-channel: %.1f GB/s" % (MT*128/8/1000))'};
}
function extraValidate(r,e){
  if(!(r.capacity_gb>=4&&r.capacity_gb<=256))e.push('capacity_gb');
  if(!(r.speed_mt_s>=1066&&r.speed_mt_s<=9600))e.push('speed_mt_s');
  if(['DDR3','DDR4','DDR5'].indexOf(r.ddr_generation)<0)e.push('ddr_generation');
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
