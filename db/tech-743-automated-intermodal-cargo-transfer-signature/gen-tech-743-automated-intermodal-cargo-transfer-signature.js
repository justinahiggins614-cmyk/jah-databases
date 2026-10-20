(function(){'use strict';
/* JAH The Signature Automated Intermodal Cargo Transfer Database generator — jahdb-tech-743-automated-intermodal-cargo-transfer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET743S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Automated Intermodal Cargo Transfer Is","The Current State of Automated Intermodal Cargo Transfer","Core Principles of Automated Intermodal Cargo Transfer","Key Vocabulary of Automated Intermodal Cargo Transfer","Why Automated Intermodal Cargo Transfer Matters"],"Compounded":["Piece 1 of Automated Intermodal Cargo Transfer: Vehicle Platform","Piece 2 of Automated Intermodal Cargo Transfer: Propulsion System","Piece 3 of Automated Intermodal Cargo Transfer: Guidance and Autonomy","Piece 4 of Automated Intermodal Cargo Transfer: Traffic Coordination","Piece 5 of Automated Intermodal Cargo Transfer: Energy Infrastructure","Piece 6 of Automated Intermodal Cargo Transfer: Passenger and Cargo Interface","Piece 7 of Automated Intermodal Cargo Transfer: Maintenance System","Piece 8 of Automated Intermodal Cargo Transfer: Regulatory and Safety Case","How the Pieces of Automated Intermodal Cargo Transfer Fit Together","Build Plan: Making Automated Intermodal Cargo Transfer Step by Step"],"Advanced":["The Working Automated Intermodal Cargo Transfer: What a Real Build Looks Like","Simulation Program: Modeling Automated Intermodal Cargo Transfer in Code","Testing and Verifying Automated Intermodal Cargo Transfer","Safety, Limits, and Responsible Use of Automated Intermodal Cargo Transfer","Scaling Automated Intermodal Cargo Transfer to Production","The Full Teaching Ladder for Automated Intermodal Cargo Transfer","Open Problems and Next Steps in Automated Intermodal Cargo Transfer"]};;
var DEMOKIND="signature automated intermodal cargo transfer record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature automated intermodal cargo transfer record planner — "+safe+"\n"
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
    name:topic+' — signature automated intermodal cargo transfer record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature automated intermodal cargo transfer record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-743-automated-intermodal-cargo-transfer-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-743-automated-intermodal-cargo-transfer-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
