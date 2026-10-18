(function(){'use strict';
/* JAH The Fire Escape Planning Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FESC-";
var FIELDS=["Escape Foundations", "Planning Your Routes", "Bedrooms & Kids", "Apartment & Multi-Story", "Practice & Drills", "Special Needs & Pets"];
var TOPICS={
 "Escape Foundations": [
  "Why Escape Plans Save Lives - Escape Foundations",
  "The Outdoor Meeting Place - Escape Foundations",
  "Stay Low and Go: Smoke Survival - Escape Foundations",
  "Calling for Help: When and How - Escape Foundations",
  "Never Go Back Inside - Escape Foundations",
  "Closing Doors: The Simple Lifesaver - Escape Foundations",
  "Fire Extinguishers: When to Use - Escape Foundations",
  "Kitchen Fire Basics - Escape Foundations",
  "Heating Equipment Safety - Escape Foundations",
  "Electrical Fire Prevention - Escape Foundations"
 ],
 "Planning Your Routes": [
  "Mapping Two Ways Out of Every Room - Planning Your Routes"
 ],
 "Bedrooms & Kids": [
  "Bedroom Escape Plans - Bedrooms & Kids",
  "Teaching Children Fire Escape - Bedrooms & Kids",
  "Babies and Toddlers: The Adult's Job - Bedrooms & Kids",
  "Escape Ladders: Choosing and Practicing - Bedrooms & Kids"
 ],
 "Apartment & Multi-Story": [
  "Second-Floor and Multi-Story Escapes - Apartment & Multi-Story",
  "Apartment Building Fire Safety - Apartment & Multi-Story",
  "High-Rise Specific Planning - Apartment & Multi-Story",
  "Dorm and Campus Housing Fires - Apartment & Multi-Story"
 ],
 "Practice & Drills": [
  "Practice Drills That Work - Practice & Drills",
  "Guests, Babysitters, and Visitors - Practice & Drills",
  "Fire Drills With Pets - Practice & Drills",
  "Workplace and School Fire Plans - Practice & Drills",
  "The Family Fire Safety Captain - Practice & Drills",
  "Community Fire Preparedness - Practice & Drills",
  "Reviewing and Updating Your Plan Yearly - Practice & Drills"
 ],
 "Special Needs & Pets": [
  "Mobility Challenges: Escape Planning - Special Needs & Pets",
  "Sensory Disabilities and Fire Safety - Special Needs & Pets",
  "Medical Equipment and Fire Planning - Special Needs & Pets",
  "Farm and Rural Property Fire Plans - Special Needs & Pets",
  "Wildfire Evacuation Planning - Special Needs & Pets",
  "After the Fire: Immediate Steps - Special Needs & Pets",
  "Fire Safety for Home Workshops - Special Needs & Pets",
  "Holiday and Seasonal Fire Risks - Special Needs & Pets"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Fire Escape Planning Guide Study — "+safe+"\n"
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
    name:topic+' — fire escape guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fire escape guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fire-escape-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fire-escape-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fire-escape-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
