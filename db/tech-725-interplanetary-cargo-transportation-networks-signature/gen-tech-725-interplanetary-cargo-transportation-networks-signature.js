(function(){'use strict';
/* JAH The Signature Interplanetary Cargo Transportation Networks Database generator — jahdb-tech-725-interplanetary-cargo-transportation-networks-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET725S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Interplanetary Cargo Transportation Networks Is","The Current State of Interplanetary Cargo Transportation Networks","Core Principles of Interplanetary Cargo Transportation Networks","Key Vocabulary of Interplanetary Cargo Transportation Networks","Why Interplanetary Cargo Transportation Networks Matters"],"Compounded":["Piece 1 of Interplanetary Cargo Transportation Networks: Launch and Transit","Piece 2 of Interplanetary Cargo Transportation Networks: Power System","Piece 3 of Interplanetary Cargo Transportation Networks: Thermal Control","Piece 4 of Interplanetary Cargo Transportation Networks: Communications","Piece 5 of Interplanetary Cargo Transportation Networks: Guidance and Navigation","Piece 6 of Interplanetary Cargo Transportation Networks: Platform Structure","Piece 7 of Interplanetary Cargo Transportation Networks: Mission Core Systems","Piece 8 of Interplanetary Cargo Transportation Networks: Ground Operations","How the Pieces of Interplanetary Cargo Transportation Networks Fit Together","Build Plan: Making Interplanetary Cargo Transportation Networks Step by Step"],"Advanced":["The Working Interplanetary Cargo Transportation Network: What a Real Build Looks Like","Simulation Program: Modeling Interplanetary Cargo Transportation Networks in Code","Testing and Verifying Interplanetary Cargo Transportation Networks","Safety, Limits, and Responsible Use of Interplanetary Cargo Transportation Networks","Scaling Interplanetary Cargo Transportation Networks to Production","The Full Teaching Ladder for Interplanetary Cargo Transportation Networks","Open Problems and Next Steps in Interplanetary Cargo Transportation Networks"]};;
var DEMOKIND="signature interplanetary cargo transportation network record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature interplanetary cargo transportation network record planner — "+safe+"\n"
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
    name:topic+' — signature interplanetary cargo transportation network record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature interplanetary cargo transportation network record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-725-interplanetary-cargo-transportation-networks-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-725-interplanetary-cargo-transportation-networks-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
