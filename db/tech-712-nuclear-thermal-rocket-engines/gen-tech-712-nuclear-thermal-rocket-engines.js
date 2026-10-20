(function(){'use strict';
/* JAH The Nuclear Thermal Rocket Engines Database generator — jahdb-tech-712-nuclear-thermal-rocket-engines-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET712-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Nuclear Thermal Rocket Engines Is","The Current State of Nuclear Thermal Rocket Engines","Core Principles of Nuclear Thermal Rocket Engines","Key Vocabulary of Nuclear Thermal Rocket Engines","Why Nuclear Thermal Rocket Engines Matters"],"Compounded":["Piece 1 of Nuclear Thermal Rocket Engines: Launch and Transit","Piece 2 of Nuclear Thermal Rocket Engines: Power System","Piece 3 of Nuclear Thermal Rocket Engines: Thermal Control","Piece 4 of Nuclear Thermal Rocket Engines: Communications","Piece 5 of Nuclear Thermal Rocket Engines: Guidance and Navigation","Piece 6 of Nuclear Thermal Rocket Engines: Platform Structure","Piece 7 of Nuclear Thermal Rocket Engines: Mission Core Systems","Piece 8 of Nuclear Thermal Rocket Engines: Ground Operations","How the Pieces of Nuclear Thermal Rocket Engines Fit Together","Build Plan: Making Nuclear Thermal Rocket Engines Step by Step"],"Advanced":["The Working Nuclear Thermal Rocket Engine: What a Real Build Looks Like","Simulation Program: Modeling Nuclear Thermal Rocket Engines in Code","Testing and Verifying Nuclear Thermal Rocket Engines","Safety, Limits, and Responsible Use of Nuclear Thermal Rocket Engines","Scaling Nuclear Thermal Rocket Engines to Production","The Full Teaching Ladder for Nuclear Thermal Rocket Engines","Open Problems and Next Steps in Nuclear Thermal Rocket Engines"]};;
var DEMOKIND="nuclear thermal rocket engine record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# nuclear thermal rocket engine record planner — "+safe+"\n"
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
    name:topic+' — nuclear thermal rocket engine record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nuclear thermal rocket engine record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-712-nuclear-thermal-rocket-engines-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-712-nuclear-thermal-rocket-engines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
