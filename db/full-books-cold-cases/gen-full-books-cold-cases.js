(function(){'use strict';
/* JAH The Full Books: Cold Cases Database generator - full-books-cold-cases-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CCOL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Cold Cases - The Complete Guide", "The Woman in White (1859) - Complete Book Record", "The Mysterious Affair at Styles (1920) - Complete Book Record", "The Hound of the Baskervilles (1902) - Complete Book Record", "The Innocence of Father Brown (1911) - Complete Book Record", "The Black Mask School (1925) - Complete Book Record", "The Maltese Falcon: Origins (1929) - Complete Book Record", "The Tenth Clew (1924) - Complete Book Record", "Three Gun Terry (1923) - Complete Book Record", "The Moonstone (1868) - Complete Book Record", "The Murders in the Rue Morgue (1841) - Complete Book Record", "The Leavenworth Case (1878) - Complete Book Record", "The Red House Mystery (1922) - Complete Book Record", "The Hardboiled Voice - Cold Cases Craft Study", "The City as Character - Cold Cases Craft Study", "The Charming Villain - Cold Cases Craft Study", "Violence With Consequences - Cold Cases Craft Study", "The Pulp Magazine Machine - Cold Cases Craft Study", "Noir vs. Cozy - Cold Cases Craft Study", "The Cold Cases Reading Pathway"];
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
var gen={version:'full-books-cold-cases-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-cold-cases',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
