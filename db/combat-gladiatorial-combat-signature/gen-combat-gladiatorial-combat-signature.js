(function(){'use strict';
/* JAH Gladiatorial Combat Signature Database generator — jahdb-combat-gladiatorial-combat-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBGLDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Combat Oath (Signature Edition) (Signature Edition)",
  "The Sand Teaches: First Lesson of the Arena (Signature Edition) (Signature Edition)",
  "The Forward Guard: The Shield Wall Principle (Signature Edition) (Signature Edition)",
  "Measure: The Signature Measure of Distance (Signature Edition) (Signature Edition)",
  "The Thrust Line: Geometry of the Gladius Thrust (Signature Edition) (Signature Edition)",
  "The Rudis Mind: Training With the Wooden Sword (Signature Edition) (Signature Edition)",
  "Breath Under Bronze: Breathing in the Galea (Signature Edition) (Signature Edition)",
  "The Hordearii Table: Signature Fuel Doctrine (Signature Edition) (Signature Edition)",
  "Rest as Weapon: Recovery in the Ludus (Signature Edition) (Signature Edition)",
  "The Post and the Partner: Palus Drills (Signature Edition) (Signature Edition)",
  "Watching the Games: Signature Study Method (Signature Edition) (Signature Edition)",
  "The Oath of the Class: Choosing Your Armatura (Signature Edition) (Signature Edition)",
 ],
 "Compounded": [
  "Murmillo, the Signature Way: The Wall Advance (Signature Edition) (Signature Edition)",
  "Retiarius, the Signature Way: The Net Cast Reconstructed (Signature Edition) (Signature Edition)",
  "Secutor, the Signature Way: The Closing Pursuit (Signature Edition) (Signature Edition)",
  "Thraex, the Signature Way: The Hooking Sica (Signature Edition) (Signature Edition)",
  "Dimachaerus, the Signature Way: Two Swords, One Rhythm (Signature Edition) (Signature Edition)",
  "Hoplomachus, the Signature Way: The Spear at Distance (Signature Edition) (Signature Edition)",
  "Provocator, the Signature Way: The Opening Exchange (Signature Edition) (Signature Edition)",
  "Eques, the Signature Way: Mounted Measure (Signature Edition) (Signature Edition)",
  "The Net Defense: Signature Counters to the Rete (Signature Edition) (Signature Edition)",
  "Shield Binding: Signature Shield Play (Signature Edition) (Signature Edition)",
  "The Turn and Re-measure: Signature Footwork Chain (Signature Edition) (Signature Edition)",
  "Ground and Rise: Signature Recovery Drill (Signature Edition) (Signature Edition)",
 ],
 "Advanced": [
  "The Pursuers Gambit: Signature Secutor Tactic (Signature Edition) (Signature Edition)",
  "The Fishermans Patience: Signature Retiarius Tactic (Signature Edition) (Signature Edition)",
  "The Wall Break: Signature Murmillo vs Thraex Plan (Signature Edition) (Signature Edition)",
  "Double-Edge Storm: Signature Dimachaerus Combination (Signature Edition) (Signature Edition)",
  "The Referees Eye: Signature Bout Control (Signature Edition) (Signature Edition)",
  "Reading the Crowd: Signature Arena Awareness (Signature Edition) (Signature Edition)",
  "The Mercy Finger: Signature Missio Protocol (Signature Edition) (Signature Edition)",
  "The Champions Season: Signature Campaign Plan (Signature Edition) (Signature Edition)",
  "After the Rudis: Signature Freedman Doctrine (Signature Edition) (Signature Edition)",
  "The Arena Code: The Complete Signature Combat Method (Signature Edition) (Signature Edition)",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Gladiatorial Combat Signature Study — "+safe+"\n"
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
    demo:{kind:"gladiatorial-combat-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-gladiatorial-combat-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-gladiatorial-combat-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
