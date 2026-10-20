(function(){'use strict';
/* JAH The Interstellar Propulsion Demonstrators Database generator — jahdb-tech-1018-interstellar-propulsion-demonstrators-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET1018-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Interstellar Propulsion Demonstrators Is","The Current State of Interstellar Propulsion Demonstrators","Core Principles of Interstellar Propulsion Demonstrators","Key Vocabulary of Interstellar Propulsion Demonstrators","Why Interstellar Propulsion Demonstrators Matters"],"Compounded":["Piece 1 of Interstellar Propulsion Demonstrators: Foundational Science","Piece 2 of Interstellar Propulsion Demonstrators: Exploratory Instruments","Piece 3 of Interstellar Propulsion Demonstrators: Theoretical Frameworks","Piece 4 of Interstellar Propulsion Demonstrators: Prototype Platforms","Piece 5 of Interstellar Propulsion Demonstrators: Safety and Ethics Review","Piece 6 of Interstellar Propulsion Demonstrators: Long-Horizon Roadmapping","Piece 7 of Interstellar Propulsion Demonstrators: Cross-Disciplinary Teams","Piece 8 of Interstellar Propulsion Demonstrators: Knowledge Preservation","How the Pieces of Interstellar Propulsion Demonstrators Fit Together","Build Plan: Making Interstellar Propulsion Demonstrators Step by Step"],"Advanced":["The Working Interstellar Propulsion Demonstrator: What a Real Build Looks Like","Simulation Program: Modeling Interstellar Propulsion Demonstrators in Code","Testing and Verifying Interstellar Propulsion Demonstrators","Safety, Limits, and Responsible Use of Interstellar Propulsion Demonstrators","Scaling Interstellar Propulsion Demonstrators to Production","The Full Teaching Ladder for Interstellar Propulsion Demonstrators","Open Problems and Next Steps in Interstellar Propulsion Demonstrators"]};;
var DEMOKIND="interstellar propulsion demonstrator record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# interstellar propulsion demonstrator record planner — "+safe+"\n"
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
    name:topic+' — interstellar propulsion demonstrator record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An interstellar propulsion demonstrator record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-1018-interstellar-propulsion-demonstrators-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-1018-interstellar-propulsion-demonstrators',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
