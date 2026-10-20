(function(){'use strict';
/* JAH The Full Books: Buccaneers Database generator - full-books-buccaneers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BUCC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Buccaneers - The Complete Guide", "The Coral Island (1858) - Complete Book Record", "White Fang (1906) - Complete Book Record", "Around the World in Eighty Days (1872) - Complete Book Record", "The Swiss Family Robinson (1812) - Complete Book Record", "Allan Quatermain (1887) - Complete Book Record", "Treasure Island (1883) - Complete Book Record", "King Solomon's Mines (1885) - Complete Book Record", "Robinson Crusoe (1719) - Complete Book Record", "The Call of the Wild (1903) - Complete Book Record", "Heart of Darkness (1899) - Complete Book Record", "Kidnapped (1886) - Complete Book Record", "She (1887) - Complete Book Record", "The Chapter-End Hook - Buccaneers Craft Study", "Maps and Itineraries - Buccaneers Craft Study", "Competence as Pleasure - Buccaneers Craft Study", "The Ordeal Sequence - Buccaneers Craft Study", "Wonder Without Empire - Buccaneers Craft Study", "The Return Changed - Buccaneers Craft Study", "The Buccaneers Reading Pathway"];
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+"\n# Field: "+field+"\nrecord={'title': \""+safe+"\", 'field': \""+field+"\"}\nprint('Record: '+record['title']+' ['+record['field']+']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var topic=pick(TOPICS,rnd);
  return {id:PREFIX+String(seed).padStart(6,'0'),title:topic,field:field,src:'public-harvest',
    summary:'Generated record for '+topic+'.',demo:{language:'python',program:demoProgram(topic,field)},_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'full-books-buccaneers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-buccaneers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
