(function(){'use strict';
/* JAH Athens City Guide Database generator — jahdb-city-guide-athens-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGAT-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Athens at a Glance",
  "When to Visit Athens",
  "Arriving in Athens: Airports and First Steps",
  "Athens Public Transit Basics",
  "Getting Around Athens on Foot",
  "Athens Money: Currency and Daily Budgets",
  "Essential Athens Phrases",
  "Athens Safety Basics",
  "Staying Connected in Athens",
  "Athens Districts: The Lay of the Land",
  "What to Pack for Athens",
  "Athens Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Plaka, Athens",
  "District Deep-Dive: Monastiraki, Athens",
  "District Deep-Dive: Kolonaki, Athens",
  "Landmark Guide: The Acropolis & Parthenon, Athens",
  "Landmark Guide: Acropolis Museum, Athens",
  "Landmark Guide: Ancient Agora, Athens",
  "Athens Signature Dishes",
  "Where to Eat in Athens: Food Streets and Markets",
  "Athens Markets and Shopping",
  "Athens Museums and Galleries",
  "Cultural Experiences in Athens",
  "Athens Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Athens: Delphi",
  "Day Trip from Athens: Cape Sounion",
  "The Perfect 3-Day Athens Itinerary",
  "Athens Festivals and Seasonal Events",
  "Athens Etiquette Masterclass",
  "Hidden Athens: Off the Beaten Path",
  "Athens After Dark",
  "Athens on Any Budget: Three Spending Plans",
  "Responsible Travel in Athens",
  "Athens Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# athens city guide — "+safe+"\n"
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
    demo:{kind:"athens city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-athens-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-athens',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
