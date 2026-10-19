(function(){'use strict';
/* JAH Lisbon City Guide Database generator — jahdb-city-guide-lisbon-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGLBS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Lisbon at a Glance",
  "When to Visit Lisbon",
  "Arriving in Lisbon: Airports and First Steps",
  "Lisbon Public Transit Basics",
  "Getting Around Lisbon on Foot",
  "Lisbon Money: Currency and Daily Budgets",
  "Essential Lisbon Phrases",
  "Lisbon Safety Basics",
  "Staying Connected in Lisbon",
  "Lisbon Districts: The Lay of the Land",
  "What to Pack for Lisbon",
  "Lisbon Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Alfama, Lisbon",
  "District Deep-Dive: Bairro Alto, Lisbon",
  "District Deep-Dive: Chiado, Lisbon",
  "Landmark Guide: Bel\u00e9m Tower, Lisbon",
  "Landmark Guide: Jer\u00f3nimos Monastery, Lisbon",
  "Landmark Guide: S\u00e3o Jorge Castle, Lisbon",
  "Lisbon Signature Dishes",
  "Where to Eat in Lisbon: Food Streets and Markets",
  "Lisbon Markets and Shopping",
  "Lisbon Museums and Galleries",
  "Cultural Experiences in Lisbon",
  "Lisbon Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Lisbon: Sintra",
  "Day Trip from Lisbon: Cascais",
  "The Perfect 3-Day Lisbon Itinerary",
  "Lisbon Festivals and Seasonal Events",
  "Lisbon Etiquette Masterclass",
  "Hidden Lisbon: Off the Beaten Path",
  "Lisbon After Dark",
  "Lisbon on Any Budget: Three Spending Plans",
  "Responsible Travel in Lisbon",
  "Lisbon Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# lisbon city guide — "+safe+"\n"
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
    demo:{kind:"lisbon city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-lisbon-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-lisbon-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
