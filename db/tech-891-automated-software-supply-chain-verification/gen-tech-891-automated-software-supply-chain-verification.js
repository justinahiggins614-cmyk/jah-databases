(function(){'use strict';
/* JAH The Automated Software Supply-Chain Verification Database generator — jahdb-tech-891-automated-software-supply-chain-verification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET891-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Automated Software Supply-Chain Verification Is","The Current State of Automated Software Supply-Chain Verification","Core Principles of Automated Software Supply-Chain Verification","Key Vocabulary of Automated Software Supply-Chain Verification","Why Automated Software Supply-Chain Verification Matters"],"Compounded":["Piece 1 of Automated Software Supply-Chain Verification: Sensor and Data Layer","Piece 2 of Automated Software Supply-Chain Verification: Detection Engine","Piece 3 of Automated Software Supply-Chain Verification: Identity and Access","Piece 4 of Automated Software Supply-Chain Verification: Response Coordination","Piece 5 of Automated Software Supply-Chain Verification: Communications Backbone","Piece 6 of Automated Software Supply-Chain Verification: Recovery Systems","Piece 7 of Automated Software Supply-Chain Verification: Audit and Evidence","Piece 8 of Automated Software Supply-Chain Verification: Human Oversight","How the Pieces of Automated Software Supply-Chain Verification Fit Together","Build Plan: Making Automated Software Supply-Chain Verification Step by Step"],"Advanced":["The Working Automated Software Supply-Chain Verification: What a Real Build Looks Like","Simulation Program: Modeling Automated Software Supply-Chain Verification in Code","Testing and Verifying Automated Software Supply-Chain Verification","Safety, Limits, and Responsible Use of Automated Software Supply-Chain Verification","Scaling Automated Software Supply-Chain Verification to Production","The Full Teaching Ladder for Automated Software Supply-Chain Verification","Open Problems and Next Steps in Automated Software Supply-Chain Verification"]};;
var DEMOKIND="automated software supply-chain verification record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# automated software supply-chain verification record planner — "+safe+"\n"
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
    name:topic+' — automated software supply-chain verification record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An automated software supply-chain verification record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-891-automated-software-supply-chain-verification-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-891-automated-software-supply-chain-verification',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
