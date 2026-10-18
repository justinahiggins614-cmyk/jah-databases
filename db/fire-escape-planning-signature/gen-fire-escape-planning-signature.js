(function(){'use strict';
/* JAH The Fire Escape Planning Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FESCS-";
var FIELDS=["Escape Foundations", "Planning Your Routes", "Bedrooms & Kids", "Apartment & Multi-Story", "Practice & Drills", "Special Needs & Pets"];
var TOPICS={
 "Escape Foundations": [
  "Why Escape Plans Save Lives (Signature Edition) - Escape Foundations",
  "The Outdoor Meeting Place (Signature Edition) - Escape Foundations",
  "Stay Low and Go: Smoke Survival (Signature Edition) - Escape Foundations",
  "Calling for Help: When and How (Signature Edition) - Escape Foundations",
  "Never Go Back Inside (Signature Edition) - Escape Foundations",
  "Closing Doors: The Simple Lifesaver (Signature Edition) - Escape Foundations",
  "Fire Extinguishers: When to Use (Signature Edition) - Escape Foundations",
  "Kitchen Fire Basics (Signature Edition) - Escape Foundations",
  "Heating Equipment Safety (Signature Edition) - Escape Foundations",
  "Electrical Fire Prevention (Signature Edition) - Escape Foundations"
 ],
 "Planning Your Routes": [
  "Mapping Two Ways Out of Every Room (Signature Edition) - Planning Your Routes"
 ],
 "Bedrooms & Kids": [
  "Bedroom Escape Plans (Signature Edition) - Bedrooms & Kids",
  "Teaching Children Fire Escape (Signature Edition) - Bedrooms & Kids",
  "Babies and Toddlers: The Adult's Job (Signature Edition) - Bedrooms & Kids",
  "Escape Ladders: Choosing and Practicing (Signature Edition) - Bedrooms & Kids"
 ],
 "Apartment & Multi-Story": [
  "Second-Floor and Multi-Story Escapes (Signature Edition) - Apartment & Multi-Story",
  "Apartment Building Fire Safety (Signature Edition) - Apartment & Multi-Story",
  "High-Rise Specific Planning (Signature Edition) - Apartment & Multi-Story",
  "Dorm and Campus Housing Fires (Signature Edition) - Apartment & Multi-Story"
 ],
 "Practice & Drills": [
  "Practice Drills That Work (Signature Edition) - Practice & Drills",
  "Guests, Babysitters, and Visitors (Signature Edition) - Practice & Drills",
  "Fire Drills With Pets (Signature Edition) - Practice & Drills",
  "Workplace and School Fire Plans (Signature Edition) - Practice & Drills",
  "The Family Fire Safety Captain (Signature Edition) - Practice & Drills",
  "Community Fire Preparedness (Signature Edition) - Practice & Drills",
  "Reviewing and Updating Your Plan Yearly (Signature Edition) - Practice & Drills"
 ],
 "Special Needs & Pets": [
  "Mobility Challenges: Escape Planning (Signature Edition) - Special Needs & Pets",
  "Sensory Disabilities and Fire Safety (Signature Edition) - Special Needs & Pets",
  "Medical Equipment and Fire Planning (Signature Edition) - Special Needs & Pets",
  "Farm and Rural Property Fire Plans (Signature Edition) - Special Needs & Pets",
  "Wildfire Evacuation Planning (Signature Edition) - Special Needs & Pets",
  "After the Fire: Immediate Steps (Signature Edition) - Special Needs & Pets",
  "Fire Safety for Home Workshops (Signature Edition) - Special Needs & Pets",
  "Holiday and Seasonal Fire Risks (Signature Edition) - Special Needs & Pets"
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
var gen={version:'jahdb-fire-escape-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fire-escape-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
