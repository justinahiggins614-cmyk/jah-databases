(function(){"use strict";
/* JAH JAH Combat Under Uncertainty Database generator — jahdb-combat-under-uncertainty-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBUU-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Situational Awareness and the Color Codes - Foundations",
  "Reading Pre-Incident Indicators - Foundations",
  "Avoidance: The First and Best Strategy - Foundations",
  "Verbal Boundaries and De-escalation - Foundations",
  "Managing Distance: The Reactionary Gap - Foundations",
  "The Protective Fence Posture - Foundations",
  "Voice as a Defensive Tool - Foundations",
  "Exit Scanning: Knowing Your Way Out - Foundations",
  "The Legal Boundaries of Self-Defense - Foundations",
  "Improvised Barriers: Objects Between You and Harm - Foundations",
  "Safe Falling: Protecting Yourself on the Way Down - Foundations",
  "Intuition as an Instrument: The Survival Signals - Foundations"
 ],
 "Compounded": [
  "The Unknown Opponent Doctrine - Compounded",
  "Surprise Attack: Converting the Flinch - Compounded",
  "Darkness: When You Cannot See the Threat - Compounded",
  "Confined Space: Walls That Limit and Protect - Compounded",
  "Uneven Ground: Footing Under Uncertainty - Compounded",
  "Adrenaline: Reading Your Own Body Alarms - Compounded",
  "Improvised Shields: Everyday Objects as Cover - Compounded",
  "Improvised Tools: Lawful Everyday Objects - Compounded",
  "Multiple Attackers: Stacking and Movement - Compounded",
  "Taken Down on Unknown Ground - Compounded",
  "De-escalation When Adrenaline Is Spiking - Compounded",
  "After the Incident: Reporting and Protecting Yourself - Compounded"
 ],
 "Advanced": [
  "Decision-Making Under Stress: The OODA Loop - Advanced",
  "The Unknown Style: Universal Attack Vectors - Advanced",
  "Environmental Weapon Awareness - Advanced",
  "Vehicle Encounters: Carjackings and Road Rage - Advanced",
  "Home Intrusion: The Unknown Intruder - Advanced",
  "Third-Party Defense: When Someone Else Is Attacked - Advanced",
  "Crowds: Ambiguity in Public Spaces - Advanced",
  "Weapon Uncertainty: The Armed Assumption - Advanced",
  "Tactical Breathing: Controlling the Body Under Fire - Advanced",
  "The Legal Aftermath: Protecting Your Future - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,"\\\\").replace(/"/g,"'");
  return "# Uncertainty Principle Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "QA = [\n"
   + "    (\"What is the core principle?\", \""+safe+"\"),\n"
   + "    (\"What field does it belong to?\", \""+field+"\"),\n"
   + "]\n"
   + "for i, (q, a) in enumerate(QA, 1):\n"
   + "    print(\"Q%d: %s\" % (i, q))\n"
   + "    print(\"   A: %s\" % a)\n"
   + "print(\"Reviewed %d principle points.\\n\" % len(QA))\n"
   + "print(\"Sample record — structural sample, not an archive entry.\")\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,"0");
  return {
    id:id,
    name:topic+" — uncertainty principle record",
    title:topic,
    description:"SAMPLE RECORD (generated — structural sample). An uncertainty principle record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-generated-sample",
    sample:true,
    disclaimer:"Generated sample record — not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"uncertainty-demo",language:"python",program:demoProgram(topic,field),note:"Structural sample demo."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.src)e.push("src");
  if(!r.demo||!r.demo.program)e.push("demo");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:["duplicate topic+field in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-combat-under-uncertainty-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("combat-under-uncertainty",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
