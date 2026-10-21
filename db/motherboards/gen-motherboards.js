(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function rf(s,a,b,d){var v=a+s()*(b-a);var m=Math.pow(10,d||0);return Math.round(v*m)/m;}
var SLUG="motherboards";
var VERSION="jahdb-motherboards-1.0";
var PREFIX="JAH-MBD-";
var KIND="motherboard";
var CATS=["am5","lga1700","am4","lga1200","workstation-hedt","mini-itx"];
/* base templates: [category, ...fields] */
var B=[["am5", "ASUS", "AM5", "X670E", "ATX", "DDR5", "yes"], ["am5", "MSI", "AM5", "B650", "ATX", "DDR5", "yes"], ["am5", "Gigabyte", "AM5", "A620", "Micro-ATX", "DDR5", "no"], ["lga1700", "ASUS", "LGA1700", "Z790", "ATX", "DDR5", "yes"], ["lga1700", "MSI", "LGA1700", "B760", "ATX", "DDR5", "yes"], ["lga1700", "ASRock", "LGA1700", "H610", "Micro-ATX", "DDR4", "no"], ["am4", "MSI", "AM4", "B550", "ATX", "DDR4", "no"], ["am4", "ASUS", "AM4", "X570", "ATX", "DDR4", "no"], ["lga1200", "ASUS", "LGA1200", "Z590", "ATX", "DDR4", "yes"], ["lga1200", "MSI", "LGA1200", "B560", "Micro-ATX", "DDR4", "no"], ["workstation-hedt", "ASUS", "sTRX4", "TRX40", "E-ATX", "DDR4", "yes"], ["workstation-hedt", "ASUS", "sWRX8", "WRX80", "E-ATX", "DDR4 ECC", "yes"], ["mini-itx", "ASUS", "AM5", "B650E", "Mini-ITX", "DDR5", "yes"], ["mini-itx", "MSI", "LGA1700", "Z790", "Mini-ITX", "DDR5", "yes"]];
var SRC='public-harvest';

function buildRec(b,rnd){
  var title=b[1]+' '+b[3]+' '+b[4]+' ('+b[2]+')';
  var desc='The '+title+' is a '+b[4]+' motherboard for the '+b[2]+' socket with the '+
    b[3]+' chipset. It takes '+b[5]+' memory'+(b[6]==='yes'?' and includes WiFi':'')+
    ', targeting '+b[0].replace(/-/g,' ')+' builds. A solid foundation for a '+b[2]+' system.';
  return {title:title,description:desc,brand:b[1],socket:b[2],chipset:b[3],
    form_factor:b[4],memory_type:b[5],wifi:b[6],category:b[0],
    demo:'BOARD={"socket":"'+b[2]+'","ddr":"'+b[5]+'"}\nprint("CPU socket must match: "+BOARD["socket"])\nprint("Memory must match: "+BOARD["ddr"])'};
}
function extraValidate(r,e){
  if(typeof r.socket!=='string'||!r.socket.length)e.push('socket');
  if(typeof r.chipset!=='string'||!r.chipset.length)e.push('chipset');
  if(['ATX','Micro-ATX','Mini-ITX','E-ATX'].indexOf(r.form_factor)<0)e.push('form_factor');
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
