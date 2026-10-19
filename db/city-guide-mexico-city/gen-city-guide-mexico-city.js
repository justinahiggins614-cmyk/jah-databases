(function(){'use strict';
/* JAH Mexico City City Guide Database generator — jahdb-city-guide-mexico-city-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGMX-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Mexico City at a Glance",
  "When to Visit Mexico City",
  "Arriving in Mexico City: Airports and First Steps",
  "Mexico City Public Transit Basics",
  "Getting Around Mexico City on Foot",
  "Mexico City Money: Currency and Daily Budgets",
  "Essential Mexico City Phrases",
  "Mexico City Safety Basics",
  "Staying Connected in Mexico City",
  "Mexico City Districts: The Lay of the Land",
  "What to Pack for Mexico City",
  "Mexico City Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: Centro Hist\u00f3rico, Mexico City",
  "District Deep-Dive: Roma & Condesa, Mexico City",
  "District Deep-Dive: Polanco, Mexico City",
  "Landmark Guide: Z\u00f3calo & Metropolitan Cathedral, Mexico City",
  "Landmark Guide: Templo Mayor, Mexico City",
  "Landmark Guide: Chapultepec Park & Castle, Mexico City",
  "Mexico City Signature Dishes",
  "Where to Eat in Mexico City: Food Streets and Markets",
  "Mexico City Markets and Shopping",
  "Mexico City Museums and Galleries",
  "Cultural Experiences in Mexico City",
  "Mexico City Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Mexico City: Teotihuacan",
  "Day Trip from Mexico City: Puebla & Cholula",
  "The Perfect 3-Day Mexico City Itinerary",
  "Mexico City Festivals and Seasonal Events",
  "Mexico City Etiquette Masterclass",
  "Hidden Mexico City: Off the Beaten Path",
  "Mexico City After Dark",
  "Mexico City on Any Budget: Three Spending Plans",
  "Responsible Travel in Mexico City",
  "Mexico City Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# mexico city city guide — "+safe+"\n"
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
    demo:{kind:"mexico city city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-mexico-city-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-mexico-city',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
