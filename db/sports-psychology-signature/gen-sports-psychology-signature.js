(function(){'use strict';
/* JAH Sports Psychology Signature Database generator — jahdb-sports-psychology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPORTPSYS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Sports Psychology Studies (Signature Edition)", "Goal Setting (SMART) (Signature Edition)", "Arousal and the Inverted-U (Signature Edition)", "Focus and Concentration Basics (Signature Edition)", "Self-Talk Fundamentals (Signature Edition)", "Imagery and Visualization Basics (Signature Edition)", "Pre-Performance Routines (Signature Edition)", "Confidence Building (Signature Edition)", "Motivation Types (Intrinsic/Extrinsic) (Signature Edition)", "Handling Nerves (Signature Edition)", "Enjoyment and Burnout Prevention (Signature Edition)"], "Compounded": ["The Yips: Causes and Cures (Signature Edition)", "Choking Under Pressure (Signature Edition)", "Mindfulness for Athletes (Signature Edition)", "Cognitive Restructuring (Signature Edition)", "Performance Profiling (Signature Edition)", "Team Cohesion Science (Signature Edition)", "Leadership in Sport (Signature Edition)", "Communication Under Stress (Signature Edition)", "Dealing with Slumps (Signature Edition)", "Injury Psychology (Signature Edition)", "Retirement and Identity (Signature Edition)", "The Parent-Coach-Athlete Triangle (Signature Edition)"], "Advanced": ["Flow State Engineering (Signature Edition)", "Attentional Control Theory (Signature Edition)", "Quiet Eye Training (Signature Edition)", "Biofeedback and HRV Training (Signature Edition)", "Pressure Training Design (Signature Edition)", "Decision-Making Under Fatigue (Signature Edition)", "Superstition vs Routine (Signature Edition)", "Cultural Psychology in Global Sport (Signature Edition)", "Working with a Sports Psychologist (Signature Edition)", "Ethics in Applied Sports Psychology (Signature Edition)", "Measuring Mental Skills Gains (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# routine-builder-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 sports psychology record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A sports psychology record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"routine-builder-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-sports-psychology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-psychology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
