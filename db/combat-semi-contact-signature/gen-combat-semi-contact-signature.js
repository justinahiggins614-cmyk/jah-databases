(function(){'use strict';
/* JAH The Semi-Contact Combat Signature Database generator — jahdb-combat-semi-contact-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBSCS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Fighting Bounce Step (Signature Edition) - Foundations",
  "The Point-Fighting Guard (Signature Edition) - Foundations",
  "The Snap Jab (Signature Edition) - Foundations",
  "The Step-In Straight Punch (Signature Edition) - Foundations",
  "Open and Closed Stances (Signature Edition) - Foundations",
  "The Front Slide (Signature Edition) - Foundations",
  "The Retreat Step (Signature Edition) - Foundations",
  "The Lead Front Kick (Signature Edition) - Foundations",
  "The Lead Roundhouse Kick (Signature Edition) - Foundations",
  "The Lead Side Kick (Signature Edition) - Foundations",
  "The Hand Parry (Signature Edition) - Foundations",
  "The Stop-Hit (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "The Straight Blitz (Signature Edition) - Compounded",
  "The Double-Punch Blitz (Signature Edition) - Compounded",
  "Feints: The Hand Feint (Signature Edition) - Compounded",
  "Feints: The Shoulder Feint (Signature Edition) - Compounded",
  "The Draw and Counter (Signature Edition) - Compounded",
  "The Slip and Counter (Signature Edition) - Compounded",
  "Angle Steps: The L-Step (Signature Edition) - Compounded",
  "The Spinning Back Kick (Signature Edition) - Compounded",
  "The Spinning Hook Kick (Signature Edition) - Compounded",
  "The Jump Roundhouse Kick (Signature Edition) - Compounded",
  "The Fake-and-Go Combination (Signature Edition) - Compounded",
  "Ring Control and Positioning (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Counter-Fighting System (Signature Edition) - Advanced",
  "Meeting the Blitz (Signature Edition) - Advanced",
  "Foot Sweeps in Point Fighting (Signature Edition) - Advanced",
  "Clinch Control and Tie-Up Timing (Signature Edition) - Advanced",
  "WAKO Semi-Contact Rules (Signature Edition) - Advanced",
  "NASKA Open Tournament Rules (Signature Edition) - Advanced",
  "Scoring Awareness and Clock Management (Signature Edition) - Advanced",
  "The Blitz Ladder Drill (Signature Edition) - Advanced",
  "The Feint-Reaction Drill (Signature Edition) - Advanced",
  "Competition Preparation and Gear Check (Signature Edition) - Advanced",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0,i;for(i=0;i<safe.length;i++){h=((h*31)+safe.charCodeAt(i))>>>0;}
  var reps=6+(h%7);
  var rounds=2+(h%3);
  var dist=(1.8+((h>>>3)%13)/10).toFixed(1);
  var tsec=(0.35+((h>>>7)%16)/100).toFixed(2);
  return "# Semi-Contact Technique Drill — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "reps = "+reps+"\n"
   + "rounds = "+rounds+"\n"
   + "distance_m = "+dist+"\n"
   + "blitz_time_s = "+tsec+"\n"
   + "speed = distance_m / blitz_time_s\n"
   + "total_reps = reps * rounds\n"
   + "print('drill: '+str(reps)+' reps x '+str(rounds)+' rounds')\n"
   + "print('blitz distance %.1f m in %.2f s -> %.2f m/s' % (distance_m, blitz_time_s, speed))\n"
   + "assert 6 <= reps <= 12\n"
   + "assert 2 <= rounds <= 4\n"
   + "assert 1.8 <= distance_m <= 3.0\n"
   + "assert 0.35 <= blitz_time_s <= 0.50\n"
   + "assert total_reps == reps * rounds\n"
   + "assert 3.0 < speed < 9.0\n"
   + "print('demo OK: '+str(total_reps)+' total reps at %.2f m/s' % speed)\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — semi-contact technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A semi-contact technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"semi-contact-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-semi-contact-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-semi-contact-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
