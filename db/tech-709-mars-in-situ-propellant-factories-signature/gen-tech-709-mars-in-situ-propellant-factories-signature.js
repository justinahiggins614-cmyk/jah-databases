(function(){'use strict';
/* JAH The Signature Mars In-Situ Propellant Factories Database generator — jahdb-tech-709-mars-in-situ-propellant-factories-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET709S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Mars In-Situ Propellant Factories Is","The Current State of Mars In-Situ Propellant Factories","Core Principles of Mars In-Situ Propellant Factories","Key Vocabulary of Mars In-Situ Propellant Factories","Why Mars In-Situ Propellant Factories Matters"],"Compounded":["Piece 1 of Mars In-Situ Propellant Factories: Launch and Transit","Piece 2 of Mars In-Situ Propellant Factories: Power System","Piece 3 of Mars In-Situ Propellant Factories: Thermal Control","Piece 4 of Mars In-Situ Propellant Factories: Communications","Piece 5 of Mars In-Situ Propellant Factories: Guidance and Navigation","Piece 6 of Mars In-Situ Propellant Factories: Platform Structure","Piece 7 of Mars In-Situ Propellant Factories: Mission Core Systems","Piece 8 of Mars In-Situ Propellant Factories: Ground Operations","How the Pieces of Mars In-Situ Propellant Factories Fit Together","Build Plan: Making Mars In-Situ Propellant Factories Step by Step"],"Advanced":["The Working Mars In-Situ Propellant Factory: What a Real Build Looks Like","Simulation Program: Modeling Mars In-Situ Propellant Factories in Code","Testing and Verifying Mars In-Situ Propellant Factories","Safety, Limits, and Responsible Use of Mars In-Situ Propellant Factories","Scaling Mars In-Situ Propellant Factories to Production","The Full Teaching Ladder for Mars In-Situ Propellant Factories","Open Problems and Next Steps in Mars In-Situ Propellant Factories"]};;
var DEMOKIND="signature mars in-situ propellant factory record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature mars in-situ propellant factory record planner — "+safe+"\n"
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
    name:topic+' — signature mars in-situ propellant factory record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature mars in-situ propellant factory record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-709-mars-in-situ-propellant-factories-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-709-mars-in-situ-propellant-factories-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
