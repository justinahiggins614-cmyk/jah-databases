(function(){'use strict';
/* JAH The Advanced Exoplanet Biosignature Detection Database generator — jahdb-tech-1022-advanced-exoplanet-biosignature-detection-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET1022-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Advanced Exoplanet Biosignature Detection Is","The Current State of Advanced Exoplanet Biosignature Detection","Core Principles of Advanced Exoplanet Biosignature Detection","Key Vocabulary of Advanced Exoplanet Biosignature Detection","Why Advanced Exoplanet Biosignature Detection Matters"],"Compounded":["Piece 1 of Advanced Exoplanet Biosignature Detection: Foundational Science","Piece 2 of Advanced Exoplanet Biosignature Detection: Exploratory Instruments","Piece 3 of Advanced Exoplanet Biosignature Detection: Theoretical Frameworks","Piece 4 of Advanced Exoplanet Biosignature Detection: Prototype Platforms","Piece 5 of Advanced Exoplanet Biosignature Detection: Safety and Ethics Review","Piece 6 of Advanced Exoplanet Biosignature Detection: Long-Horizon Roadmapping","Piece 7 of Advanced Exoplanet Biosignature Detection: Cross-Disciplinary Teams","Piece 8 of Advanced Exoplanet Biosignature Detection: Knowledge Preservation","How the Pieces of Advanced Exoplanet Biosignature Detection Fit Together","Build Plan: Making Advanced Exoplanet Biosignature Detection Step by Step"],"Advanced":["The Working Advanced Exoplanet Biosignature Detection: What a Real Build Looks Like","Simulation Program: Modeling Advanced Exoplanet Biosignature Detection in Code","Testing and Verifying Advanced Exoplanet Biosignature Detection","Safety, Limits, and Responsible Use of Advanced Exoplanet Biosignature Detection","Scaling Advanced Exoplanet Biosignature Detection to Production","The Full Teaching Ladder for Advanced Exoplanet Biosignature Detection","Open Problems and Next Steps in Advanced Exoplanet Biosignature Detection"]};;
var DEMOKIND="advanced exoplanet biosignature detection record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# advanced exoplanet biosignature detection record planner — "+safe+"\n"
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
    name:topic+' — advanced exoplanet biosignature detection record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An advanced exoplanet biosignature detection record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-1022-advanced-exoplanet-biosignature-detection-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-1022-advanced-exoplanet-biosignature-detection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
