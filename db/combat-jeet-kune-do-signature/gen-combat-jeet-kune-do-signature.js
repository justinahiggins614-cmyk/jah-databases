(function(){'use strict';
/* JAH The Jeet Kune Do Combat Signature Database generator — jahdb-combat-jeet-kune-do-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBJKDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bai-Jong Stance - The On-Guard Position (Signature Edition) - Foundations",
  "Footwork Fundamentals: Advance and Retreat (Signature Edition) - Foundations",
  "The Guard: Parry and Cover Positions (Signature Edition) - Foundations",
  "The Straight Lead (Signature Edition) - Foundations",
  "The Cross (Signature Edition) - Foundations",
  "The Lead Hook (Signature Edition) - Foundations",
  "The Uppercut - Lead and Rear (Signature Edition) - Foundations",
  "Lateral Footwork: Side-Step and Circle Step (Signature Edition) - Foundations",
  "Basic Trapping Touch: Pak Sao Introduction (Signature Edition) - Foundations",
  "Defensive Timing: The Slip and the Duck (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Single Direct Attack - First Way of Attack (Signature Edition) - Compounded",
  "Attack by Combination - Second Way of Attack (Signature Edition) - Compounded",
  "Progressive Indirect Attack - Third Way of Attack (Signature Edition) - Compounded",
  "Hand Immobilization Attack - Fourth Way of Attack (Signature Edition) - Compounded",
  "Attack by Drawing - Fifth Way of Attack (Signature Edition) - Compounded",
  "Pak Sao - The Slapping Hand (Signature Edition) - Compounded",
  "Lop Sao - The Pulling Hand (Signature Edition) - Compounded",
  "Jut Sao - The Jerking Hand (Signature Edition) - Compounded",
  "The Lead Side Kick (Signature Edition) - Compounded",
  "The Hook Kick (Signature Edition) - Compounded",
  "The Low Lead Kick (Signature Edition) - Compounded",
  "Stop Hit - The Jeet Interception (Signature Edition) - Compounded",
  "Stop Kick - Intercepting the Kicker (Signature Edition) - Compounded",
  "Broken Rhythm - Timing and Cadence (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Economy of Motion - Non-Telegraphic Movement (Signature Edition) - Advanced",
  "The Intercepting Fist - Time Hit and Counter Timing (Signature Edition) - Advanced",
  "Trapping Flow Drills - Chi Sao and Hubud Basics (Signature Edition) - Advanced",
  "The Stop-Thrust - Offensive Interception (Signature Edition) - Advanced",
  "Kicking Interception - The Low Line Stop (Signature Edition) - Advanced",
  "The Counter-Offensive - Attack on Preparation (Signature Edition) - Advanced",
  "Cadence Traps - Broken Rhythm in Sparring (Signature Edition) - Advanced",
  "Centerline Theory in Combat (Signature Edition) - Advanced",
  "Simultaneous Parry and Hit (Signature Edition) - Advanced",
  "Jeet Kune Do Sparring Synthesis - The Interception Game (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Jeet Kune Do Study — "+safe+"\n"
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
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"jeet-kune-do-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-jeet-kune-do-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-jeet-kune-do-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
