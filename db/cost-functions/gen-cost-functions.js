(function(){'use strict';
/* JAH Cost Function Database generator — jahdb-cost-functions-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CF-";
var FIELDS=["quadratic-costs","time-optimal-costs","energy-costs","obstacle-and-safety-costs","terminal-costs","multi-objective-costs"];
var TOPICS={
 "quadratic-costs": [
  "Quadratic costs \u2014 mobile robot navigation",
  "Quadratic costs \u2014 drone racing",
  "Quadratic costs \u2014 arm reaching",
  "Quadratic costs \u2014 autonomous parking",
  "Quadratic costs \u2014 biped walking",
  "Quadratic costs \u2014 AUV depth keeping",
  "Quadratic costs \u2014 satellite slew",
  "Quadratic costs \u2014 warehouse routing",
  "Quadratic costs \u2014 manipulator tracking",
  "Quadratic costs \u2014 formation flight"
 ],
 "time-optimal-costs": [
  "Time-optimal costs \u2014 mobile robot navigation",
  "Time-optimal costs \u2014 drone racing",
  "Time-optimal costs \u2014 arm reaching",
  "Time-optimal costs \u2014 autonomous parking",
  "Time-optimal costs \u2014 biped walking",
  "Time-optimal costs \u2014 AUV depth keeping",
  "Time-optimal costs \u2014 satellite slew",
  "Time-optimal costs \u2014 warehouse routing",
  "Time-optimal costs \u2014 manipulator tracking",
  "Time-optimal costs \u2014 formation flight"
 ],
 "energy-costs": [
  "Energy costs \u2014 mobile robot navigation",
  "Energy costs \u2014 drone racing",
  "Energy costs \u2014 arm reaching",
  "Energy costs \u2014 autonomous parking",
  "Energy costs \u2014 biped walking",
  "Energy costs \u2014 AUV depth keeping",
  "Energy costs \u2014 satellite slew",
  "Energy costs \u2014 warehouse routing",
  "Energy costs \u2014 manipulator tracking",
  "Energy costs \u2014 formation flight"
 ],
 "obstacle-and-safety-costs": [
  "Obstacle and safety costs \u2014 mobile robot navigation",
  "Obstacle and safety costs \u2014 drone racing",
  "Obstacle and safety costs \u2014 arm reaching",
  "Obstacle and safety costs \u2014 autonomous parking",
  "Obstacle and safety costs \u2014 biped walking",
  "Obstacle and safety costs \u2014 AUV depth keeping",
  "Obstacle and safety costs \u2014 satellite slew",
  "Obstacle and safety costs \u2014 warehouse routing",
  "Obstacle and safety costs \u2014 manipulator tracking",
  "Obstacle and safety costs \u2014 formation flight"
 ],
 "terminal-costs": [
  "Terminal costs \u2014 mobile robot navigation",
  "Terminal costs \u2014 drone racing",
  "Terminal costs \u2014 arm reaching",
  "Terminal costs \u2014 autonomous parking",
  "Terminal costs \u2014 biped walking",
  "Terminal costs \u2014 AUV depth keeping",
  "Terminal costs \u2014 satellite slew",
  "Terminal costs \u2014 warehouse routing",
  "Terminal costs \u2014 manipulator tracking",
  "Terminal costs \u2014 formation flight"
 ],
 "multi-objective-costs": [
  "Multi-objective costs \u2014 mobile robot navigation",
  "Multi-objective costs \u2014 drone racing",
  "Multi-objective costs \u2014 arm reaching",
  "Multi-objective costs \u2014 autonomous parking",
  "Multi-objective costs \u2014 biped walking",
  "Multi-objective costs \u2014 AUV depth keeping",
  "Multi-objective costs \u2014 satellite slew",
  "Multi-objective costs \u2014 warehouse routing",
  "Multi-objective costs \u2014 manipulator tracking",
  "Multi-objective costs \u2014 formation flight"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Cost Function — "+safe+"\n"
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
    name:topic+' — cost function record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cost function record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"cost-evaluator",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-cost-functions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cost-functions',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
