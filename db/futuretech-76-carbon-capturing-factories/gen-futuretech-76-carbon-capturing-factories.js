(function(){'use strict';
/* JAH The Carbon-Capturing Factories Future Technology Database generator — jahdb-futuretech-76-carbon-capturing-factories-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT76-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1930s: Amine Catches Carbon - Foundations",
  "1972: Carbon Goes Underground - Foundations",
  "1996: Sleipner - First CCS - Foundations",
  "2000: Weyburn Monitored - Foundations",
  "2000s: Catching Sky Carbon - Foundations",
  "2014: Boundary Dam - Foundations",
  "2009: Climeworks Founded - Foundations",
  "2017: Petra Nova - Foundations",
  "2017: First Commercial DAC - Foundations",
  "2015: Air to Fuel - Foundations",
  "2021: Orca - Foundations"
 ],
 "Compounded": [
  "2022: $85 a Ton - Compounded",
  "2022: DAC Hubs Funded - Compounded",
  "2023: Stratos Rises - Compounded",
  "2024: Mammoth - Compounded",
  "2024: Heirloom's Limestone - Compounded",
  "2025: the Megaton Era - Compounded",
  "2025: Carbon Has a Price - Compounded",
  "2025: Direct Air Capture Scales - Compounded",
  "Gigaton Capture - Compounded",
  "$50-a-Ton Air Capture - Compounded",
  "Carbon to Products - Compounded",
  "The Home Carbon Unit - Compounded"
 ],
 "Advanced": [
  "The Carbon-Negative Industry - Advanced",
  "Ocean Carbon Capture - Advanced",
  "CO2 to Rock - Advanced",
  "The Carbon Refinery - Advanced",
  "Atmospheric Restoration - Advanced",
  "Carbon-Negative Concrete - Advanced",
  "The Drawdown Economy - Advanced",
  "Factory Forests - Advanced",
  "The Global Capture Grid - Advanced",
  "The Carbon-Negative Civilization - Advanced",
  "Everyday Capture - Working Version - Advanced"
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
    name:topic+' — carbon-capturing factory record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A carbon-capturing factory record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-76-carbon-capturing-factories-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-76-carbon-capturing-factories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-76-carbon-capturing-factories',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
