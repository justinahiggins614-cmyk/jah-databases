(function(){'use strict';
/* JAH The Full Books: First Contact Database generator - full-books-alien-first-contact-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AFC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Alien First Contact - The Complete Guide", "A Princess of Mars (1912) - Complete Book Record", "The First Men in the Moon (1901) - Complete Book Record", "Frankenstein (1818) - Complete Book Record", "The Machine Stops (1909) - Complete Book Record", "R.U.R. (1920) - Complete Book Record", "We (1924) - Complete Book Record", "Twenty Thousand Leagues Under the Sea (1870) - Complete Book Record", "The Invisible Man (1897) - Complete Book Record", "The Sleeper Awakes (1910) - Complete Book Record", "The Time Machine (1895) - Complete Book Record", "The War of the Worlds (1898) - Complete Book Record", "From the Earth to the Moon (1865) - Complete Book Record", "The Sense of Wonder - Alien First Contact Craft Study", "Hard SF vs. Soft SF - Alien First Contact Craft Study", "First Contact Protocols - Alien First Contact Craft Study", "The Dystopia Toolkit - Alien First Contact Craft Study", "Worldbuilding That Works - Alien First Contact Craft Study", "Robots and Rights - Alien First Contact Craft Study", "The Alien First Contact Reading Pathway"];
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
var gen={version:'full-books-alien-first-contact-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-books-alien-first-contact',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
