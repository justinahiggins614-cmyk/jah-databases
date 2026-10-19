(function(){'use strict';
/* JAH Istanbul City Guide Database generator — jahdb-city-guide-istanbul-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGISS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Istanbul at a Glance",
  "When to Visit Istanbul",
  "Arriving in Istanbul: Airports and First Steps",
  "Istanbul Public Transit Basics",
  "Getting Around Istanbul on Foot",
  "Istanbul Money: Currency and Daily Budgets",
  "Essential Istanbul Phrases",
  "Istanbul Safety Basics",
  "Staying Connected in Istanbul",
  "Istanbul Districts: The Lay of the Land",
  "What to Pack for Istanbul",
  "Istanbul Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Sultanahmet, Istanbul",
  "District Deep-Dive: Beyo\u011flu & Taksim, Istanbul",
  "District Deep-Dive: Galata & Karak\u00f6y, Istanbul",
  "Landmark Guide: Hagia Sophia, Istanbul",
  "Landmark Guide: Sultanahmet Camii (Blue), Istanbul",
  "Landmark Guide: Topkap\u0131 Palace, Istanbul",
  "Istanbul Signature Dishes",
  "Where to Eat in Istanbul: Food Streets and Markets",
  "Istanbul Markets and Shopping",
  "Istanbul Museums and Galleries",
  "Cultural Experiences in Istanbul",
  "Istanbul Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Istanbul: Princes\u2019 Islands",
  "Day Trip from Istanbul: Bursa",
  "The Perfect 3-Day Istanbul Itinerary",
  "Istanbul Festivals and Seasonal Events",
  "Istanbul Etiquette Masterclass",
  "Hidden Istanbul: Off the Beaten Path",
  "Istanbul After Dark",
  "Istanbul on Any Budget: Three Spending Plans",
  "Responsible Travel in Istanbul",
  "Istanbul Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# istanbul city guide — "+safe+"\n"
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
    demo:{kind:"istanbul city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-istanbul-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-istanbul-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
