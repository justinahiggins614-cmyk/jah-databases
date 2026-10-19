(function(){'use strict';
/* JAH Marrakech City Guide Database generator — jahdb-city-guide-marrakech-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGMKS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Marrakech at a Glance",
  "When to Visit Marrakech",
  "Arriving in Marrakech: Airports and First Steps",
  "Marrakech Public Transit Basics",
  "Getting Around Marrakech on Foot",
  "Marrakech Money: Currency and Daily Budgets",
  "Essential Marrakech Phrases",
  "Marrakech Safety Basics",
  "Staying Connected in Marrakech",
  "Marrakech Districts: The Lay of the Land",
  "What to Pack for Marrakech",
  "Marrakech Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: The Medina, Marrakech",
  "District Deep-Dive: Jemaa el-Fna, Marrakech",
  "District Deep-Dive: Gueliz, Marrakech",
  "Landmark Guide: Jemaa el-Fna, Marrakech",
  "Landmark Guide: Koutoubia minaret, Marrakech",
  "Landmark Guide: Bahia Palace, Marrakech",
  "Marrakech Signature Dishes",
  "Where to Eat in Marrakech: Food Streets and Markets",
  "Marrakech Markets and Shopping",
  "Marrakech Museums and Galleries",
  "Cultural Experiences in Marrakech",
  "Marrakech Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Marrakech: Ourika Valley & the Atlas",
  "Day Trip from Marrakech: Essaouira",
  "The Perfect 3-Day Marrakech Itinerary",
  "Marrakech Festivals and Seasonal Events",
  "Marrakech Etiquette Masterclass",
  "Hidden Marrakech: Off the Beaten Path",
  "Marrakech After Dark",
  "Marrakech on Any Budget: Three Spending Plans",
  "Responsible Travel in Marrakech",
  "Marrakech Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# marrakech city guide — "+safe+"\n"
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
    demo:{kind:"marrakech city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-marrakech-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-marrakech-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
