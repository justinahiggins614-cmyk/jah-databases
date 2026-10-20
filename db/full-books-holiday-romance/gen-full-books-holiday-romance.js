(function(){'use strict';
/* JAH The Full Books: Holiday Romance Database generator - full-books-holiday-romance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HROL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Holiday Romance - The Complete Guide", "Persuasion (1817) - Complete Book Record", "Far from the Madding Crowd (1874) - Complete Book Record", "A Room with a View (1908) - Complete Book Record", "Pollyanna (1913) - Complete Book Record", "Pride and Prejudice (1813) - Complete Book Record", "Jane Eyre (1847) - Complete Book Record", "Wuthering Heights (1847) - Complete Book Record", "Emma (1815) - Complete Book Record", "North and South (1855) - Complete Book Record", "Anne of Green Gables (1908) - Complete Book Record", "Little Women (1868) - Complete Book Record", "The Secret Garden (1911) - Complete Book Record", "The Austen Blueprint - Holiday Romance Craft Study", "The Second-Chance Romance - Holiday Romance Craft Study", "Banter as Courtship - Holiday Romance Craft Study", "The Slow Burn - Holiday Romance Craft Study", "Obstacles That Matter - Holiday Romance Craft Study", "The Earned Happy Ending - Holiday Romance Craft Study", "The Holiday Romance Reading Pathway"];
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
var gen={version:'full-books-holiday-romance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-holiday-romance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
