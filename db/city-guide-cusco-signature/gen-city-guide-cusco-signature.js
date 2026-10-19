(function(){'use strict';
/* JAH Cusco City Guide Database generator — jahdb-city-guide-cusco-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGCUS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Cusco at a Glance",
  "When to Visit Cusco",
  "Arriving in Cusco: Airports and First Steps",
  "Cusco Public Transit Basics",
  "Getting Around Cusco on Foot",
  "Cusco Money: Currency and Daily Budgets",
  "Essential Cusco Phrases",
  "Cusco Safety Basics",
  "Staying Connected in Cusco",
  "Cusco Districts: The Lay of the Land",
  "What to Pack for Cusco",
  "Cusco Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Plaza de Armas, Cusco",
  "District Deep-Dive: San Blas, Cusco",
  "District Deep-Dive: San Crist\u00f3bal, Cusco",
  "Landmark Guide: Sacsayhuam\u00e1n, Cusco",
  "Landmark Guide: Qorikancha, Cusco",
  "Landmark Guide: Cusco Cathedral, Cusco",
  "Cusco Signature Dishes",
  "Where to Eat in Cusco: Food Streets and Markets",
  "Cusco Markets and Shopping",
  "Cusco Museums and Galleries",
  "Cultural Experiences in Cusco",
  "Cusco Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Cusco: Machu Picchu",
  "Day Trip from Cusco: Sacred Valley (Pisac & Ollantaytambo)",
  "The Perfect 3-Day Cusco Itinerary",
  "Cusco Festivals and Seasonal Events",
  "Cusco Etiquette Masterclass",
  "Hidden Cusco: Off the Beaten Path",
  "Cusco After Dark",
  "Cusco on Any Budget: Three Spending Plans",
  "Responsible Travel in Cusco",
  "Cusco Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# cusco city guide — "+safe+"\n"
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
    demo:{kind:"cusco city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-cusco-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-cusco-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
