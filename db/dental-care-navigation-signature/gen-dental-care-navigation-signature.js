(function(){'use strict';
/* JAH Dental Care Navigation Database generator — jahdb-dental-care-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DENTCNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Daily Hygiene Fundamentals (Signature Edition)", "Choosing a Dentist (Signature Edition)", "Cleanings and Exams (Signature Edition)", "Understanding X-Rays (Signature Edition)", "Fillings Explained (Signature Edition)", "When Crowns Are Needed (Signature Edition)", "Root Canals (Signature Edition)", "Extractions (Signature Edition)", "Wisdom Teeth (Signature Edition)", "Orthodontics Basics (Signature Edition)", "Dental Implants (Signature Edition)"], "Compounded": ["Dentures and Partials (Signature Edition)", "Gum Disease (Signature Edition)", "Dental Emergencies (Signature Edition)", "Kids Dental Care (Signature Edition)", "Dental Costs and Coverage (Signature Edition)", "Second Opinions (Signature Edition)", "Dental Anxiety (Signature Edition)", "Cosmetic Dentistry (Signature Edition)", "Oral Health and Overall Health (Signature Edition)", "Nutrition for Teeth (Signature Edition)", "Tobacco and Oral Health (Signature Edition)", "Dry Mouth (Signature Edition)"], "Advanced": ["Bruxism and Grinding (Signature Edition)", "Finding Low-Cost Care (Signature Edition)", "Dental Tourism Caution (Signature Edition)", "Special Needs Dentistry (Signature Edition)", "Aging and Dental Health (Signature Edition)", "The Annual Dental Review (Signature Edition)", "Teaching Kids Hygiene (Signature Edition)", "Dental Records (Signature Edition)", "Tooth Sensitivity (Signature Edition)", "Bad Breath Causes (Signature Edition)", "Mouthguards for Sports (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — dental guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — dental guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A dental guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"dental-care-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-dental-care-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("dental-care-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
