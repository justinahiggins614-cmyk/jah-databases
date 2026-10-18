(function(){'use strict';
/* JAH The Mars Colonization Technology Future Technology Database generator — jahdb-futuretech-92-mars-colonization-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT92-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1877: the Canals of Mars - Foundations",
  "1890s: Lowell's Mars - Foundations",
  "1948: Das Marsprojekt - Foundations",
  "1965: Mariner 4 - Foundations",
  "1971: Mars 3 - Foundations",
  "1976: Viking - Foundations",
  "1990: Mars Direct - Foundations",
  "1998: the Mars Society - Foundations",
  "1997: Pathfinder - Foundations",
  "2004: the Rover Twins - Foundations",
  "2012: Curiosity - Foundations"
 ],
 "Compounded": [
  "2015: The Martian - Compounded",
  "2016: the Mars Rocket - Compounded",
  "2018: InSight - Compounded",
  "2020: Mars 2020 - Compounded",
  "2021: Perseverance - Compounded",
  "2021: Ingenuity Flies - Compounded",
  "2021: Tianwen-1 - Compounded",
  "2023: Starship Tests - Compounded",
  "2024: Mars Timelines - Compounded",
  "The Mars Base - Compounded",
  "The Mars Village - Compounded",
  "The Mars Town - Compounded"
 ],
 "Advanced": [
  "Martian Industry - Advanced",
  "The Mars City - Advanced",
  "Terraforming Begins - Advanced",
  "The Martian Economy - Advanced",
  "The Mars-Born - Advanced",
  "The Martian Civilization - Advanced",
  "The Interplanetary Species - Advanced",
  "The Mars Republic - Advanced",
  "The Green Mars - Advanced",
  "The Settled Mars - Advanced",
  "Everyday Martian Life - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — Mars colonization record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A Mars colonization record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-92-mars-colonization-technology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-92-mars-colonization-technology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-92-mars-colonization-technology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
