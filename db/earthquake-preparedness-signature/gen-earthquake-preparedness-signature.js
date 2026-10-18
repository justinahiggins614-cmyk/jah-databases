(function(){'use strict';
/* JAH The Earthquake Preparedness Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EQPRS-";
var FIELDS=["Quake Science Basics", "Home Hazard Hunt", "Securing Your Space", "Emergency Kits", "During & After", "Family & Community Plans"];
var TOPICS={
 "Quake Science Basics": [
  "How Earthquakes Work: The Basics (Signature Edition) - Quake Science Basics",
  "Know Your Regional Risk (Signature Edition) - Quake Science Basics",
  "Drop, Cover, and Hold On (Signature Edition) - Quake Science Basics",
  "What NOT to Do During Shaking (Signature Edition) - Quake Science Basics",
  "Building Types and Vulnerability (Signature Edition) - Quake Science Basics",
  "Landslide and Liquefaction Awareness (Signature Edition) - Quake Science Basics"
 ],
 "Home Hazard Hunt": [
  "The Home Hazard Hunt (Signature Edition) - Home Hazard Hunt",
  "Hanging Objects and Wall Hangings (Signature Edition) - Home Hazard Hunt",
  "Chimneys and Masonry Hazards (Signature Edition) - Home Hazard Hunt"
 ],
 "Securing Your Space": [
  "Securing Heavy Furniture (Signature Edition) - Securing Your Space",
  "Water Heater Strapping (Signature Edition) - Securing Your Space",
  "Securing Kitchen and Cabinets (Signature Edition) - Securing Your Space",
  "Structural Retrofitting Basics (Signature Edition) - Securing Your Space"
 ],
 "Emergency Kits": [
  "The 72-Hour Emergency Kit (Signature Edition) - Emergency Kits",
  "Go-Bags for Every Member (Signature Edition) - Emergency Kits",
  "Water Storage and Purification (Signature Edition) - Emergency Kits",
  "Food Storage for Emergencies (Signature Edition) - Emergency Kits"
 ],
 "During & After": [
  "First Aid for Quake Injuries (Signature Edition) - During & After",
  "Shutting Off Gas, Water, and Power (Signature Edition) - During & After",
  "Aftershocks: The Second Danger (Signature Edition) - During & After",
  "Evacuation: When to Leave Home (Signature Edition) - During & After",
  "Communicating After a Quake (Signature Edition) - During & After",
  "Documenting for Insurance (Signature Edition) - During & After",
  "Long-Term Recovery Planning (Signature Edition) - During & After"
 ],
 "Family & Community Plans": [
  "Checking on Neighbors (Signature Edition) - Family & Community Plans",
  "Pets in Earthquake Plans (Signature Edition) - Family & Community Plans",
  "Creating a Family Communication Plan (Signature Edition) - Family & Community Plans",
  "Workplace and School Preparedness (Signature Edition) - Family & Community Plans",
  "Joining a Community Response Team (Signature Edition) - Family & Community Plans",
  "The Great ShakeOut and Drills (Signature Edition) - Family & Community Plans",
  "Tsunami Awareness for Coastal Residents (Signature Edition) - Family & Community Plans",
  "Earthquake Insurance: The Full Picture (Signature Edition) - Family & Community Plans",
  "Building a Resilient Household Culture (Signature Edition) - Family & Community Plans",
  "Teaching Quake Safety to Kids (Signature Edition) - Family & Community Plans"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Earthquake Preparedness Guide Study — "+safe+"\n"
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
    name:topic+' — earthquake preparedness record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A earthquake preparedness record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"earthquake-preparedness-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-earthquake-preparedness-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('earthquake-preparedness-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
