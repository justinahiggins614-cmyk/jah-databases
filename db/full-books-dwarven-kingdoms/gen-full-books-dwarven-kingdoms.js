(function(){'use strict';
/* JAH The Full Books: Dwarven Kingdoms Database generator - full-books-dwarven-kingdoms-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DKWA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Dwarven Kingdoms - The Complete Guide", "The Jungle Book (1894) - Complete Book Record", "Peter Pan (1911) - Complete Book Record", "The Wind in the Willows (1908) - Complete Book Record", "The Velveteen Rabbit (1922) - Complete Book Record", "The Wonderful Wizard of Oz (1900) - Complete Book Record", "Alice's Adventures in Wonderland (1865) - Complete Book Record", "The Princess and the Goblin (1872) - Complete Book Record", "The Well at the World's End (1896) - Complete Book Record", "Five Children and It (1902) - Complete Book Record", "The Gods of Peg\u0101na (1905) - Complete Book Record", "Lilith (1895) - Complete Book Record", "The Water-Babies (1863) - Complete Book Record", "Building a Secondary World - Dwarven Kingdoms Craft Study", "The Quest Structure - Dwarven Kingdoms Craft Study", "Magic Systems That Work - Dwarven Kingdoms Craft Study", "Fairy-Tale Logic - Dwarven Kingdoms Craft Study", "The Eucatastrophe - Dwarven Kingdoms Craft Study", "Talking Animals Done Right - Dwarven Kingdoms Craft Study", "The Dwarven Kingdoms Reading Pathway"];
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
var gen={version:'full-books-dwarven-kingdoms-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-dwarven-kingdoms',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
