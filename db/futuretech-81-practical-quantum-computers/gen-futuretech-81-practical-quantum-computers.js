(function(){'use strict';
/* JAH The Practical Quantum Computers Future Technology Database generator — jahdb-futuretech-81-practical-quantum-computers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT81-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1980: the Quantum Turing Machine - Foundations",
  "1981: Feynman Urges Quantum - Foundations",
  "1985: Deutsch Formalizes - Foundations",
  "1992: First Quantum Speedup - Foundations",
  "1994: Shor's Algorithm - Foundations",
  "1996: Grover's Search - Foundations",
  "1998: First Quantum Computer - Foundations",
  "1999: the Superconducting Qubit - Foundations",
  "2001: Shor Runs - Foundations",
  "2007: D-Wave - Foundations",
  "2011: D-Wave One Ships - Foundations"
 ],
 "Compounded": [
  "2014: Google's Quantum Lab - Compounded",
  "2016: Quantum in the Cloud - Compounded",
  "2017: 50 Qubits - Compounded",
  "2018: Bristlecone - Compounded",
  "2019: Quantum Supremacy - Compounded",
  "2020: Honeywell's Ions - Compounded",
  "2021: Eagle - 127 Qubits - Compounded",
  "2022: Osprey - 433 Qubits - Compounded",
  "2023: Heron - Quality First - Compounded",
  "2023: Error Correction Advances - Compounded",
  "2024: Logical Qubits - Compounded",
  "2024: Willow - Compounded"
 ],
 "Advanced": [
  "2025: the Field Accelerates - Advanced",
  "2025: Quantum Error Correction Milestones - Advanced",
  "Fault-Tolerant Quantum - Advanced",
  "Practical Quantum Advantage - Advanced",
  "The Quantum Data Center - Advanced",
  "Million-Qubit Machines - Advanced",
  "The Quantum Internet - Advanced",
  "The Quantum Cloud - Advanced",
  "Quantum Drug Discovery - Advanced",
  "The Quantum Economy - Advanced",
  "Everyday Quantum - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — practical quantum computer record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical quantum computer record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-81-practical-quantum-computers-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-81-practical-quantum-computers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-81-practical-quantum-computers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
