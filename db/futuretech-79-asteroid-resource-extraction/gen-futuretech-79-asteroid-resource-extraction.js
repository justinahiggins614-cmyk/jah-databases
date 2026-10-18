(function(){'use strict';
/* JAH The Asteroid Resource Extraction Future Technology Database generator — jahdb-futuretech-79-asteroid-resource-extraction-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT79-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1801: Ceres Found - Foundations",
  "1898: Eros - the Neighbor - Foundations",
  "1974: the High Frontier - Foundations",
  "1990s: Mapping the Belt - Foundations",
  "2001: Landing on Eros - Foundations",
  "2003: Hayabusa Launches - Foundations",
  "2005: Itokawa - Foundations",
  "2010: First Sample Returns - Foundations",
  "2012: the Asteroid Miners - Foundations",
  "2013: Deep Space Industries - Foundations",
  "2014: Hayabusa2 Launches - Foundations"
 ],
 "Compounded": [
  "2015: Miners Get Rights - Compounded",
  "2016: OSIRIS-REx Launches - Compounded",
  "2018: Ryugu - Compounded",
  "2018: the First Rush Ends - Compounded",
  "2020: Sampling Bennu - Compounded",
  "2020: Ryugu Returns - Compounded",
  "2022: DART Moves an Asteroid - Compounded",
  "2023: Bennu Returns - Compounded",
  "2023: Psyche Launches - Compounded",
  "2024: AstroForge - Compounded",
  "2024: TransAstra - Compounded",
  "2025: Prospectors Multiply - Compounded"
 ],
 "Advanced": [
  "2025: Prospecting Grows - Advanced",
  "The First Asteroid Mined - Advanced",
  "Water from Asteroids - Advanced",
  "Platinum Asteroids - Advanced",
  "Orbital Refineries - Advanced",
  "The Trillion-Dollar Rock - Advanced",
  "The Space Resource Economy - Advanced",
  "Asteroid Redirection - Advanced",
  "The Belt Economy - Advanced",
  "Self-Sustaining Space Industry - Advanced",
  "Everyday Asteroid Resources - Working Version - Advanced"
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
    name:topic+' — asteroid resource extraction record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A asteroid resource extraction record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-79-asteroid-resource-extraction-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-79-asteroid-resource-extraction-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-79-asteroid-resource-extraction',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
