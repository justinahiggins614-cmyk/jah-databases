(function(){'use strict';
/* JAH The Full Books: Civil War Tales Database generator - full-books-civil-war-tales-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CWT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Civil War Tales - The Complete Guide", "Ivanhoe (1819) - Complete Book Record", "Vanity Fair (1848) - Complete Book Record", "Middlemarch (1871) - Complete Book Record", "The Hunchback of Notre-Dame (1831) - Complete Book Record", "War and Peace (1869) - Complete Book Record", "The Last of the Mohicans (1826) - Complete Book Record", "Quentin Durward (1823) - Complete Book Record", "The Cloister and the Hearth (1861) - Complete Book Record", "The Three Musketeers (1844) - Complete Book Record", "The Count of Monte Cristo (1844) - Complete Book Record", "Les Miserables (1862) - Complete Book Record", "A Tale of Two Cities (1859) - Complete Book Record", "Research as Worldbuilding - Civil War Tales Craft Study", "The Everyman Witness - Civil War Tales Craft Study", "Romance Inside History - Civil War Tales Craft Study", "The Long Arc of Revenge - Civil War Tales Craft Study", "Crowds and Barricades - Civil War Tales Craft Study", "The Past as Argument - Civil War Tales Craft Study", "The Civil War Tales Reading Pathway"];
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
var gen={version:'full-books-civil-war-tales-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-civil-war-tales',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
