(function(){'use strict';
/* JAH The Flying Electric Regional Aircraft Database generator — jahdb-tech-730-flying-electric-regional-aircraft-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET730-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Flying Electric Regional Aircraft Is","The Current State of Flying Electric Regional Aircraft","Core Principles of Flying Electric Regional Aircraft","Key Vocabulary of Flying Electric Regional Aircraft","Why Flying Electric Regional Aircraft Matters"],"Compounded":["Piece 1 of Flying Electric Regional Aircraft: Vehicle Platform","Piece 2 of Flying Electric Regional Aircraft: Propulsion System","Piece 3 of Flying Electric Regional Aircraft: Guidance and Autonomy","Piece 4 of Flying Electric Regional Aircraft: Traffic Coordination","Piece 5 of Flying Electric Regional Aircraft: Energy Infrastructure","Piece 6 of Flying Electric Regional Aircraft: Passenger and Cargo Interface","Piece 7 of Flying Electric Regional Aircraft: Maintenance System","Piece 8 of Flying Electric Regional Aircraft: Regulatory and Safety Case","How the Pieces of Flying Electric Regional Aircraft Fit Together","Build Plan: Making Flying Electric Regional Aircraft Step by Step"],"Advanced":["The Working Flying Electric Regional Aircraft: What a Real Build Looks Like","Simulation Program: Modeling Flying Electric Regional Aircraft in Code","Testing and Verifying Flying Electric Regional Aircraft","Safety, Limits, and Responsible Use of Flying Electric Regional Aircraft","Scaling Flying Electric Regional Aircraft to Production","The Full Teaching Ladder for Flying Electric Regional Aircraft","Open Problems and Next Steps in Flying Electric Regional Aircraft"]};;
var DEMOKIND="flying electric regional aircraft record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# flying electric regional aircraft record planner — "+safe+"\n"
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
    name:topic+' — flying electric regional aircraft record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A flying electric regional aircraft record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-730-flying-electric-regional-aircraft-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-730-flying-electric-regional-aircraft',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
