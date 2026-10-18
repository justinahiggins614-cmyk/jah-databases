(function(){'use strict';
/* JAH The Geoengineering Systems Future Technology Database generator — jahdb-futuretech-80-geoengineering-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT80-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1896: Arrhenius Calculates Warming - Foundations",
  "1965: the White House Warned - Foundations",
  "1974: Budyko's Idea - Foundations",
  "1977: the Guardrail - Foundations",
  "1991: Pinatubo Cools Earth - Foundations",
  "1992: the Academy Weighs In - Foundations",
  "2006: Crutzen Breaks the Taboo - Foundations",
  "2009: the Royal Society Reports - Foundations",
  "2010: Asilomar - Foundations",
  "2011: SPICE Canceled - Foundations",
  "2015: Twin Reports - Foundations"
 ],
 "Compounded": [
  "2018: SCoPEx Planned - Compounded",
  "2021: Research Recommended - Compounded",
  "2021: Sweden Says No - Compounded",
  "2022: the White House Plan - Compounded",
  "2022: Rogue Balloons - Compounded",
  "2024: Rules for the Thermostat - Compounded",
  "2025: Research Funded - Compounded",
  "2025: Geoengineering Governance - Compounded",
  "The Stratospheric Test - Compounded",
  "Marine Cloud Brightening - Compounded",
  "The Planetary Thermostat - Compounded",
  "Ocean Alkalinity - Compounded"
 ],
 "Advanced": [
  "Cirrus Thinning - Advanced",
  "The Managed Thermostat - Advanced",
  "Regional Climate Control - Advanced",
  "The Geoengineering Treaty - Advanced",
  "Climate Restored - Advanced",
  "Planetary HVAC - Advanced",
  "The Controlled Climate - Advanced",
  "The Stable Holocene - Advanced",
  "The Engineered Planet - Advanced",
  "The Climate Utility - Advanced",
  "Everyday Geoengineering - Working Version - Advanced"
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
    name:topic+' — geoengineering system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A geoengineering system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-80-geoengineering-systems-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-80-geoengineering-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-80-geoengineering-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
