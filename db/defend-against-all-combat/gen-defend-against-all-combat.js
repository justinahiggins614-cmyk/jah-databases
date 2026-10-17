(function(){'use strict';
/* JAH Defend Against All Combat Database generator — jahdb-defend-against-all-combat-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record.
   Civilian personal-safety framing only: escape-first, disengage, legal boundaries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DAA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Situational Awareness and the Cooper Color Codes - Foundations",
  "The Defensive Guard Stance - Foundations",
  "Verbal De-escalation and Boundary Setting - Foundations",
  "The Palm-Heel Strike - Foundations",
  "The High Cover Against Straight Punches - Foundations",
  "Escaping a One-Hand Wrist Grab - Foundations",
  "Escaping a Two-Hand Wrist Grab - Foundations",
  "The Pluck Defense Against a Front Choke - Foundations",
  "Clearing a Clothing Grab - Foundations",
  "Clearing a Rear Hair Grab - Foundations",
  "The Technical Stand-Up - Foundations",
  "Escaping the Side Headlock - Foundations"
 ],
 "Compounded": [
  "Escaping the Rear Naked Choke - Compounded",
  "Escaping the Bear Hug, Arms Free - Compounded",
  "Escaping the Bear Hug, Arms Pinned - Compounded",
  "Defending the Hook Punch - Compounded",
  "Checking the Front Kick - Compounded",
  "Defending the Clinch and Knee Strikes - Compounded",
  "Sprawling Against the Tackle - Compounded",
  "Escaping the Mount: Buck and Roll - Compounded",
  "Defending the Guillotine Choke - Compounded",
  "Pinned Against a Wall - Compounded",
  "Defending the Shove-and-Grab - Compounded",
  "Defending the Rear Choke with the Arm Trapped - Compounded"
 ],
 "Advanced": [
  "Multiple Attackers: Stacking and Movement - Advanced",
  "Knife at Distance: The Escape-First Rule - Advanced",
  "Surviving the Knife Slash - Advanced",
  "Surviving the Overhead Stab - Advanced",
  "Defending the Stick Swing - Advanced",
  "Weapons of Opportunity - Advanced",
  "Third-Party Protection - Advanced",
  "Legal Boundaries of Self-Defense - Advanced",
  "After the Attack: Reporting and Evidence - Advanced",
  "Stress Drills and Scenario Training - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Defend Against All Study — "+safe+"\n"
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
    name:topic+' — self-defense record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A self-defense record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"defense-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-defend-against-all-combat-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defend-against-all-combat',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
