(function(){'use strict';
/* JAH Accessible Travel Database generator — jahdb-accessible-travel-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ACTR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Accessible Travel?",
  "Know Your Rights: Air Travel Accessibility",
  "Wheelchair-Accessible Destinations",
  "Accessible Hotel Rooms, Explained",
  "Flying with a Wheelchair",
  "Accessible Ground Transportation",
  "Traveling with a Service Animal",
  "Accessible Cruise Travel",
  "Travel Insurance and Accessibility",
  "Planning Buffer Time",
  "The Accessibility Research Method"
 ],
 "Compounded": [
  "Accessible National Parks (US)",
  "Accessible European City Breaks",
  "Accessible Beach Destinations",
  "Traveling with Visual Impairments",
  "Traveling with Hearing Impairments",
  "Traveling with Cognitive Disabilities",
  "Accessible Adventure Travel",
  "Medical Equipment While Traveling",
  "Accessible Tour Operators, Explained",
  "Airport Assistance Services, Explained",
  "Accessible Travel Apps and Tools",
  "The Access Statement: Asking Hotels the Right Questions"
 ],
 "Advanced": [
  "Advanced: The Accessibility Audit Trip",
  "Advanced: Accessible Safari Travel",
  "Advanced: Accessible Winter Sports",
  "Advanced: Traveling with Complex Medical Needs",
  "Advanced: The Accessible Travel Advocate",
  "Advanced: Teaching Accessible Travel",
  "Advanced: Accessibility Ratings Systems",
  "Advanced: The Accessible Honeymoon",
  "Advanced: Accessible Solo Travel",
  "Advanced: The Accessible Travel Year",
  "The Accessible Travel Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete accessible travel record entries with real measurement math.";
function demoProgram(topic,field){
  return "'use strict';\n// "+topic+" \u2014 sample demo.\n// Field: "+field+"\nconst a = 12;\nconst b = 4;\nconst r = a / b;\nconsole.log('sample ratio = ' + r.toFixed(2));\nif (!isFinite(r)) throw new Error('bad');\nconsole.log('DEMO_OK');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — accessible travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A accessible travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'node',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-accessible-travel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-travel',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
