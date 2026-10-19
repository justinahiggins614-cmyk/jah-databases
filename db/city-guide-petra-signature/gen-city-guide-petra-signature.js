(function(){'use strict';
/* JAH Petra City Guide Database generator — jahdb-city-guide-petra-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGPTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Petra at a Glance",
  "When to Visit Petra",
  "Arriving in Petra: Airports and First Steps",
  "Petra Public Transit Basics",
  "Getting Around Petra on Foot",
  "Petra Money: Currency and Daily Budgets",
  "Essential Petra Phrases",
  "Petra Safety Basics",
  "Staying Connected in Petra",
  "Petra Districts: The Lay of the Land",
  "What to Pack for Petra",
  "Petra Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Wadi Musa, Petra",
  "District Deep-Dive: The Siq, Petra",
  "District Deep-Dive: Outer Siq & Street of Facades, Petra",
  "Landmark Guide: Al-Khazneh (the Treasury), Petra",
  "Landmark Guide: Ad-Deir (the Monastery), Petra",
  "Landmark Guide: The Siq, Petra",
  "Petra Signature Dishes",
  "Where to Eat in Petra: Food Streets and Markets",
  "Petra Markets and Shopping",
  "Petra Museums and Galleries",
  "Cultural Experiences in Petra",
  "Petra Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Petra: Wadi Rum",
  "Day Trip from Petra: Little Petra",
  "The Perfect 3-Day Petra Itinerary",
  "Petra Festivals and Seasonal Events",
  "Petra Etiquette Masterclass",
  "Hidden Petra: Off the Beaten Path",
  "Petra After Dark",
  "Petra on Any Budget: Three Spending Plans",
  "Responsible Travel in Petra",
  "Petra Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# petra city guide — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — city guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A city guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"petra city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
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
var gen={version:'jahdb-city-guide-petra-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-petra-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
