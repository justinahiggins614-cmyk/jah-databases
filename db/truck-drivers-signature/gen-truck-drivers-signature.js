(function(){'use strict';
/* JAH Signature Truck Drivers Database generator — jahdb-truck-drivers-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRUCKS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Pre-Trip Chant",
  "Signature Scenario: The Blowout",
  "The Signature Backing Course",
  "Signature Logbook Honesty Pledge",
  "Signature Fuel Stop Routine",
  "Signature CB Revival",
  "The Signature Sleeper Setup",
  "Signature Weigh Station Prep",
  "Signature Trucker Health Challenge",
  "Signature First-Year Survival Guide",
  "Signature Trucking Family Pact",
 ],
 "Compounded": [
  "Signature Reefer Mastery Course",
  "Signature Tarping Speed Clinic",
  "Signature Tanker Smoothness Drill",
  "Signature Hazmat Drill Day",
  "Signature Permit Mastery",
  "Signature Business Launchpad",
  "Signature Rate Negotiation Workshop",
  "Signature Breakdown Playbook",
  "Signature Border Crossing Guide",
  "Signature Team Compatibility Quiz",
  "Signature Truck Stop Awards",
  "Signature Idle-Free Challenge",
 ],
 "Advanced": [
  "Signature Backing Championship",
  "Signature Grade Descent Simulator",
  "Signature Chain-Up Speed Run",
  "Signature MPG Masters League",
  "Signature Spill Response Trailer",
  "Signature Compliance Scorecard",
  "Signature Million-Mile Club",
  "Signature Mentor Hall of Fame",
  "Signature Autonomous Transition Lab",
  "Signature Driver Bill of Rights",
  "Signature Trucking Legacy Archive",
 ],
};
var DEMOKIND="trucking calculation";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Trucking calculator — "+safe+"\n"
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
    name:topic+' — truck driver profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miners profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-truck-drivers-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('truck-drivers-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
