(function(){'use strict';
/* JAH Havana City Guide Database generator — jahdb-city-guide-havana-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGHVS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Havana at a Glance",
  "When to Visit Havana",
  "Arriving in Havana: Airports and First Steps",
  "Havana Public Transit Basics",
  "Getting Around Havana on Foot",
  "Havana Money: Currency and Daily Budgets",
  "Essential Havana Phrases",
  "Havana Safety Basics",
  "Staying Connected in Havana",
  "Havana Districts: The Lay of the Land",
  "What to Pack for Havana",
  "Havana Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Habana Vieja, Havana",
  "District Deep-Dive: Centro Habana, Havana",
  "District Deep-Dive: Vedado, Havana",
  "Landmark Guide: The Malec\u00f3n, Havana",
  "Landmark Guide: Plaza de la Catedral, Havana",
  "Landmark Guide: El Capitolio, Havana",
  "Havana Signature Dishes",
  "Where to Eat in Havana: Food Streets and Markets",
  "Havana Markets and Shopping",
  "Havana Museums and Galleries",
  "Cultural Experiences in Havana",
  "Havana Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Havana: Vi\u00f1ales",
  "Day Trip from Havana: Varadero",
  "The Perfect 3-Day Havana Itinerary",
  "Havana Festivals and Seasonal Events",
  "Havana Etiquette Masterclass",
  "Hidden Havana: Off the Beaten Path",
  "Havana After Dark",
  "Havana on Any Budget: Three Spending Plans",
  "Responsible Travel in Havana",
  "Havana Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# havana city guide — "+safe+"\n"
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
    demo:{kind:"havana city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-havana-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-havana-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
