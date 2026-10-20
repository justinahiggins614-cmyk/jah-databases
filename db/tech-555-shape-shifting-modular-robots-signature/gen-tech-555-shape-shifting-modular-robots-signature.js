(function(){'use strict';
/* JAH The Signature Shape-Shifting Modular Robots Database generator — jahdb-tech-555-shape-shifting-modular-robots-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET555S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Shape-Shifting Modular Robots Is","The Current State of Shape-Shifting Modular Robots","Core Principles of Shape-Shifting Modular Robots","Key Vocabulary of Shape-Shifting Modular Robots","Why Shape-Shifting Modular Robots Matters"],"Compounded":["Piece 1 of Shape-Shifting Modular Robots: Mobility Platform","Piece 2 of Shape-Shifting Modular Robots: Power and Energy System","Piece 3 of Shape-Shifting Modular Robots: Perception Suite","Piece 4 of Shape-Shifting Modular Robots: Onboard Compute","Piece 5 of Shape-Shifting Modular Robots: Manipulation Hardware","Piece 6 of Shape-Shifting Modular Robots: Communication Link","Piece 7 of Shape-Shifting Modular Robots: Control Software Stack","Piece 8 of Shape-Shifting Modular Robots: Safety and Recovery Systems","How the Pieces of Shape-Shifting Modular Robots Fit Together","Build Plan: Making Shape-Shifting Modular Robots Step by Step"],"Advanced":["The Working Shape-Shifting Modular Robot: What a Real Build Looks Like","Simulation Program: Modeling Shape-Shifting Modular Robots in Code","Testing and Verifying Shape-Shifting Modular Robots","Safety, Limits, and Responsible Use of Shape-Shifting Modular Robots","Scaling Shape-Shifting Modular Robots to Production","The Full Teaching Ladder for Shape-Shifting Modular Robots","Open Problems and Next Steps in Shape-Shifting Modular Robots"]};;
var DEMOKIND="signature shape-shifting modular robot record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature shape-shifting modular robot record planner — "+safe+"\n"
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
    name:topic+' — signature shape-shifting modular robot record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature shape-shifting modular robot record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-tech-555-shape-shifting-modular-robots-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-555-shape-shifting-modular-robots-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
