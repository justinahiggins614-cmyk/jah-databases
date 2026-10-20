(function(){'use strict';
/* JAH The Post-Quantum Secure Consumer Devices Database generator — jahdb-tech-818-post-quantum-secure-consumer-devices-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET818-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Post-Quantum Secure Consumer Devices Is","The Current State of Post-Quantum Secure Consumer Devices","Core Principles of Post-Quantum Secure Consumer Devices","Key Vocabulary of Post-Quantum Secure Consumer Devices","Why Post-Quantum Secure Consumer Devices Matters"],"Compounded":["Piece 1 of Post-Quantum Secure Consumer Devices: Front End","Piece 2 of Post-Quantum Secure Consumer Devices: Signal Processing Core","Piece 3 of Post-Quantum Secure Consumer Devices: Spectrum and Channel Management","Piece 4 of Post-Quantum Secure Consumer Devices: Network Protocol Stack","Piece 5 of Post-Quantum Secure Consumer Devices: Hardware Platform","Piece 6 of Post-Quantum Secure Consumer Devices: Power Management","Piece 7 of Post-Quantum Secure Consumer Devices: Security Layer","Piece 8 of Post-Quantum Secure Consumer Devices: Test and Measurement","How the Pieces of Post-Quantum Secure Consumer Devices Fit Together","Build Plan: Making Post-Quantum Secure Consumer Devices Step by Step"],"Advanced":["The Working Post-Quantum Secure Consumer Device: What a Real Build Looks Like","Simulation Program: Modeling Post-Quantum Secure Consumer Devices in Code","Testing and Verifying Post-Quantum Secure Consumer Devices","Safety, Limits, and Responsible Use of Post-Quantum Secure Consumer Devices","Scaling Post-Quantum Secure Consumer Devices to Production","The Full Teaching Ladder for Post-Quantum Secure Consumer Devices","Open Problems and Next Steps in Post-Quantum Secure Consumer Devices"]};;
var DEMOKIND="post-quantum secure consumer device record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# post-quantum secure consumer device record planner — "+safe+"\n"
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
    name:topic+' — post-quantum secure consumer device record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A post-quantum secure consumer device record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-818-post-quantum-secure-consumer-devices-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-818-post-quantum-secure-consumer-devices',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
