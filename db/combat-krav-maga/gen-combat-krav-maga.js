(function(){'use strict';
/* JAH Krav Maga Combat Database generator — jahdb-combat-krav-maga-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBKM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Krav Maga Fighting Stance - Foundations",
  "Krav Maga Footwork and Movement - Foundations",
  "Krav Maga Punch Combatives - Foundations",
  "Krav Maga Palm-Heel Strike - Foundations",
  "Krav Maga Elbow Strikes - Foundations",
  "Krav Maga Knee Strikes - Foundations",
  "Krav Maga Front Kick to the Groin - Foundations",
  "Krav Maga Hammerfist Strike - Foundations"
 ],
 "Compounded": [
  "Krav Maga Inside Defense Against a Straight Punch - Compounded",
  "Krav Maga Defense Against a Wrist Grab - Compounded",
  "Krav Maga 360-Degree Outside Defense - Compounded",
  "Krav Maga Defense Against a Front Choke - Compounded",
  "Krav Maga Defense Against a Side Headlock - Compounded",
  "Krav Maga Defense Against a Two-Handed Shirt Grab - Compounded",
  "Krav Maga Defense Against a Bear Hug with Arms Free - Compounded",
  "Krav Maga Defense Against a Bear Hug with Arms Pinned - Compounded",
  "Krav Maga Defense Against a Hair Grab - Compounded",
  "Krav Maga Defense Against a Rear Choke - Compounded",
  "Krav Maga Ground Survival and the Technical Stand-Up - Compounded",
  "Krav Maga Kicking from the Ground - Compounded",
  "Krav Maga Clinch Fighting and Close-Quarter Combatives - Compounded",
  "Krav Maga Bursting: Closing Distance Under Attack - Compounded"
 ],
 "Advanced": [
  "Krav Maga Retzev: Continuous Combat Motion - Advanced",
  "Krav Maga Defense Against a Knife Threat on the Live Side - Advanced",
  "Krav Maga Defense Against a Knife Threat on the Dead Side - Advanced",
  "Krav Maga Defense Against a Stick Attack - Advanced",
  "Krav Maga Defense Against a Slashing Knife Attack - Advanced",
  "Krav Maga Defense Against an Overhead Knife Stab - Advanced",
  "Krav Maga Defense Against a Handgun Threat from the Front - Advanced",
  "Krav Maga Multiple Attacker Defense - Advanced",
  "Krav Maga Defense Against a Handgun Threat from Behind - Advanced",
  "Krav Maga Defense Against a Long Gun Threat - Advanced",
  "Krav Maga Third-Party Protection - Advanced",
  "Krav Maga Stress Drills and Scenario Training - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Krav Maga Study — "+safe+"\n"
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
    demo:{kind:"krav-maga-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-krav-maga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-krav-maga',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
