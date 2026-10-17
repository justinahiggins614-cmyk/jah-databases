(function(){'use strict';
/* JAH The Jeet Kune Do Combat Database generator — jahdb-combat-jeet-kune-do-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBJKD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bai-Jong Stance - The On-Guard Position - Foundations",
  "Footwork Fundamentals: Advance and Retreat - Foundations",
  "The Guard: Parry and Cover Positions - Foundations",
  "The Straight Lead - Foundations",
  "The Cross - Foundations",
  "The Lead Hook - Foundations",
  "The Uppercut - Lead and Rear - Foundations",
  "Lateral Footwork: Side-Step and Circle Step - Foundations",
  "Basic Trapping Touch: Pak Sao Introduction - Foundations",
  "Defensive Timing: The Slip and the Duck - Foundations"
 ],
 "Compounded": [
  "Single Direct Attack - First Way of Attack - Compounded",
  "Attack by Combination - Second Way of Attack - Compounded",
  "Progressive Indirect Attack - Third Way of Attack - Compounded",
  "Hand Immobilization Attack - Fourth Way of Attack - Compounded",
  "Attack by Drawing - Fifth Way of Attack - Compounded",
  "Pak Sao - The Slapping Hand - Compounded",
  "Lop Sao - The Pulling Hand - Compounded",
  "Jut Sao - The Jerking Hand - Compounded",
  "The Lead Side Kick - Compounded",
  "The Hook Kick - Compounded",
  "The Low Lead Kick - Compounded",
  "Stop Hit - The Jeet Interception - Compounded",
  "Stop Kick - Intercepting the Kicker - Compounded",
  "Broken Rhythm - Timing and Cadence - Compounded"
 ],
 "Advanced": [
  "Economy of Motion - Non-Telegraphic Movement - Advanced",
  "The Intercepting Fist - Time Hit and Counter Timing - Advanced",
  "Trapping Flow Drills - Chi Sao and Hubud Basics - Advanced",
  "The Stop-Thrust - Offensive Interception - Advanced",
  "Kicking Interception - The Low Line Stop - Advanced",
  "The Counter-Offensive - Attack on Preparation - Advanced",
  "Cadence Traps - Broken Rhythm in Sparring - Advanced",
  "Centerline Theory in Combat - Advanced",
  "Simultaneous Parry and Hit - Advanced",
  "Jeet Kune Do Sparring Synthesis - The Interception Game - Advanced"
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
var gen={version:'jahdb-combat-jeet-kune-do-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-jeet-kune-do',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
