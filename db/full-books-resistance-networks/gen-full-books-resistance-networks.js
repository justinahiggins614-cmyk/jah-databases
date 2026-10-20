(function(){'use strict';
/* JAH The Full Books: Resistance Networks Database generator - full-books-resistance-networks-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RNES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Resistance Networks - The Complete Guide", "Mizora (1880) - Complete Book Record", "Caesar's Column (1890) - Complete Book Record", "Looking Backward (1888) - Complete Book Record", "The Iron Heel (1908) - Complete Book Record", "News from Nowhere (1890) - Complete Book Record", "The Machine Stops (1909) - Complete Book Record", "R.U.R. (1920) - Complete Book Record", "We (1924) - Complete Book Record", "The Sleeper Awakes (1910) - Complete Book Record", "The World Set Free (1914) - Complete Book Record", "A Journey in Other Worlds (1894) - Complete Book Record", "The Heads of Cerberus (1919) - Complete Book Record", "The Prophecy Business - Resistance Networks Craft Study", "The System Dystopia - Resistance Networks Craft Study", "Robots as Workers - Resistance Networks Craft Study", "The Network Before the Network - Resistance Networks Craft Study", "Utopia as Argument - Resistance Networks Craft Study", "Cyberpunk's Ancestors - Resistance Networks Craft Study", "The Resistance Networks Reading Pathway"];
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
var gen={version:'full-books-resistance-networks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-resistance-networks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
