(function(){'use strict';
/* JAH Cape Town City Guide Database generator — jahdb-city-guide-cape-town-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGCT-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Cape Town at a Glance",
  "When to Visit Cape Town",
  "Arriving in Cape Town: Airports and First Steps",
  "Cape Town Public Transit Basics",
  "Getting Around Cape Town on Foot",
  "Cape Town Money: Currency and Daily Budgets",
  "Essential Cape Town Phrases",
  "Cape Town Safety Basics",
  "Staying Connected in Cape Town",
  "Cape Town Districts: The Lay of the Land",
  "What to Pack for Cape Town",
  "Cape Town Health and Emergency Essentials"
 ],
 "Compounded": [
  "District Deep-Dive: City Bowl, Cape Town",
  "District Deep-Dive: V&A Waterfront, Cape Town",
  "District Deep-Dive: Bo-Kaap, Cape Town",
  "Landmark Guide: Table Mountain, Cape Town",
  "Landmark Guide: Robben Island, Cape Town",
  "Landmark Guide: Kirstenbosch Gardens, Cape Town",
  "Cape Town Signature Dishes",
  "Where to Eat in Cape Town: Food Streets and Markets",
  "Cape Town Markets and Shopping",
  "Cape Town Museums and Galleries",
  "Cultural Experiences in Cape Town",
  "Cape Town Transit Mastery: Passes, Apps, and Taxis"
 ],
 "Advanced": [
  "Day Trip from Cape Town: Cape Peninsula",
  "Day Trip from Cape Town: Winelands (Stellenbosch/Franschhoek)",
  "The Perfect 3-Day Cape Town Itinerary",
  "Cape Town Festivals and Seasonal Events",
  "Cape Town Etiquette Masterclass",
  "Hidden Cape Town: Off the Beaten Path",
  "Cape Town After Dark",
  "Cape Town on Any Budget: Three Spending Plans",
  "Responsible Travel in Cape Town",
  "Cape Town Master Travel Plan"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# cape town city guide — "+safe+"\n"
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
    demo:{kind:"cape town city guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-city-guide-cape-town-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('city-guide-cape-town',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
