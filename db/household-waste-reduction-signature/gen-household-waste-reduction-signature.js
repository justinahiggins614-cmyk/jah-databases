(function(){'use strict';
/* JAH Household Waste Reduction Database generator — jahdb-household-waste-reduction-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HOUSWRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Week-Long Waste Audit (Signature Edition)", "Food Waste: Meal Planning (Signature Edition)", "Food Storage That Extends Life (Signature Edition)", "Understanding Date Labels (Signature Edition)", "Recycling Right (Signature Edition)", "What Not to Recycle Curbside (Signature Edition)", "Composting Basics (Signature Edition)", "Vermicomposting Indoors (Signature Edition)", "Reducing Packaging (Signature Edition)", "The Refuse Habit (Signature Edition)", "Repair Culture (Signature Edition)"], "Compounded": ["Secondhand First (Signature Edition)", "Paper Reduction (Signature Edition)", "Hazardous Waste Disposal (Signature Edition)", "E-Waste Handling (Signature Edition)", "Textile Waste (Signature Edition)", "Water Waste Awareness (Signature Edition)", "Energy Waste at Home (Signature Edition)", "Hosting Low-Waste Gatherings (Signature Edition)", "Kids and Waste Habits (Signature Edition)", "Apartment Waste Reduction (Signature Edition)", "Workplace Waste (Signature Edition)", "Holiday Waste Spikes (Signature Edition)"], "Advanced": ["Yard Waste Management (Signature Edition)", "Tracking Progress (Signature Edition)", "Community Waste Programs (Signature Edition)", "The Zero-Waste Kitchen (Signature Edition)", "The Zero-Waste Bathroom (Signature Edition)", "Minimalist Buying Rules (Signature Edition)", "Donation Systems (Signature Edition)", "Teaching Waste Literacy (Signature Edition)", "The Annual Waste Review (Signature Edition)", "Advocacy Beyond Home (Signature Edition)", "Emergency and Disaster Waste (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — waste guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — waste guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A waste guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"household-waste-reduction-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-household-waste-reduction-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("household-waste-reduction-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
