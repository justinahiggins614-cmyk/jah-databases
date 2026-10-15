(function(){'use strict';
/* JAH Robot Position Database generator — jahdb-robot-positions-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RP-";
var FIELDS=["ground-robots","aerial-robots","manipulator-arms","marine-robots","humanoid-robots","multi-robot-teams"];
var TOPICS={
 "ground-robots": [
  "Compiled pose \u2014 differential-drive rover #1",
  "Compiled pose \u2014 differential-drive rover #2",
  "Compiled pose \u2014 differential-drive rover #3",
  "Compiled pose \u2014 differential-drive rover #4",
  "Compiled pose \u2014 differential-drive rover #5",
  "Compiled pose \u2014 differential-drive rover #6",
  "Compiled pose \u2014 differential-drive rover #7",
  "Compiled pose \u2014 differential-drive rover #8",
  "Compiled pose \u2014 differential-drive rover #9",
  "Compiled pose \u2014 differential-drive rover #10"
 ],
 "aerial-robots": [
  "Compiled pose \u2014 quadrotor #1",
  "Compiled pose \u2014 quadrotor #2",
  "Compiled pose \u2014 quadrotor #3",
  "Compiled pose \u2014 quadrotor #4",
  "Compiled pose \u2014 quadrotor #5",
  "Compiled pose \u2014 quadrotor #6",
  "Compiled pose \u2014 quadrotor #7",
  "Compiled pose \u2014 quadrotor #8",
  "Compiled pose \u2014 quadrotor #9",
  "Compiled pose \u2014 quadrotor #10"
 ],
 "manipulator-arms": [
  "Compiled pose \u2014 6-DOF articulated arm #1",
  "Compiled pose \u2014 6-DOF articulated arm #2",
  "Compiled pose \u2014 6-DOF articulated arm #3",
  "Compiled pose \u2014 6-DOF articulated arm #4",
  "Compiled pose \u2014 6-DOF articulated arm #5",
  "Compiled pose \u2014 6-DOF articulated arm #6",
  "Compiled pose \u2014 6-DOF articulated arm #7",
  "Compiled pose \u2014 6-DOF articulated arm #8",
  "Compiled pose \u2014 6-DOF articulated arm #9",
  "Compiled pose \u2014 6-DOF articulated arm #10"
 ],
 "marine-robots": [
  "Compiled pose \u2014 autonomous underwater vehicle #1",
  "Compiled pose \u2014 autonomous underwater vehicle #2",
  "Compiled pose \u2014 autonomous underwater vehicle #3",
  "Compiled pose \u2014 autonomous underwater vehicle #4",
  "Compiled pose \u2014 autonomous underwater vehicle #5",
  "Compiled pose \u2014 autonomous underwater vehicle #6",
  "Compiled pose \u2014 autonomous underwater vehicle #7",
  "Compiled pose \u2014 autonomous underwater vehicle #8",
  "Compiled pose \u2014 autonomous underwater vehicle #9",
  "Compiled pose \u2014 autonomous underwater vehicle #10"
 ],
 "humanoid-robots": [
  "Compiled pose \u2014 biped humanoid #1",
  "Compiled pose \u2014 biped humanoid #2",
  "Compiled pose \u2014 biped humanoid #3",
  "Compiled pose \u2014 biped humanoid #4",
  "Compiled pose \u2014 biped humanoid #5",
  "Compiled pose \u2014 biped humanoid #6",
  "Compiled pose \u2014 biped humanoid #7",
  "Compiled pose \u2014 biped humanoid #8",
  "Compiled pose \u2014 biped humanoid #9",
  "Compiled pose \u2014 biped humanoid #10"
 ],
 "multi-robot-teams": [
  "Compiled pose \u2014 fleet centroid #1",
  "Compiled pose \u2014 fleet centroid #2",
  "Compiled pose \u2014 fleet centroid #3",
  "Compiled pose \u2014 fleet centroid #4",
  "Compiled pose \u2014 fleet centroid #5",
  "Compiled pose \u2014 fleet centroid #6",
  "Compiled pose \u2014 fleet centroid #7",
  "Compiled pose \u2014 fleet centroid #8",
  "Compiled pose \u2014 fleet centroid #9",
  "Compiled pose \u2014 fleet centroid #10"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Robot Position — "+safe+"\n"
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
    name:topic+' — compiled robot position record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A compiled robot position record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"pose-fuser",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-robot-positions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,
xdbUses:[{slug:'predictive-trajectories',fields:['waypoints'],min:1},{slug:'dynamics-models',fields:['parameters'],min:1},{slug:'cost-functions',fields:['mathematical_form'],min:1},{slug:'optimal-plans',fields:['goal'],min:1},{slug:'model-predictive-control',fields:['formulation'],min:1}]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('robot-positions',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
