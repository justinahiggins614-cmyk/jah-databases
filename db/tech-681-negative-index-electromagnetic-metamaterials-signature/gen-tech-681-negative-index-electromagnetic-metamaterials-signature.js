(function(){'use strict';
/* JAH The Signature Negative-Index Electromagnetic Metamaterials Database generator — jahdb-tech-681-negative-index-electromagnetic-metamaterials-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET681S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Negative-Index Electromagnetic Metamaterials Is","The Current State of Negative-Index Electromagnetic Metamaterials","Core Principles of Negative-Index Electromagnetic Metamaterials","Key Vocabulary of Negative-Index Electromagnetic Metamaterials","Why Negative-Index Electromagnetic Metamaterials Matters"],"Compounded":["Piece 1 of Negative-Index Electromagnetic Metamaterials: Precursor Chemistry","Piece 2 of Negative-Index Electromagnetic Metamaterials: Synthesis Reactor","Piece 3 of Negative-Index Electromagnetic Metamaterials: Structure Control","Piece 4 of Negative-Index Electromagnetic Metamaterials: Characterization Suite","Piece 5 of Negative-Index Electromagnetic Metamaterials: Property Testing","Piece 6 of Negative-Index Electromagnetic Metamaterials: Scale Manufacturing","Piece 7 of Negative-Index Electromagnetic Metamaterials: Integration Engineering","Piece 8 of Negative-Index Electromagnetic Metamaterials: Lifecycle and Safety","How the Pieces of Negative-Index Electromagnetic Metamaterials Fit Together","Build Plan: Making Negative-Index Electromagnetic Metamaterials Step by Step"],"Advanced":["The Working Negative-Index Electromagnetic Metamaterial: What a Real Build Looks Like","Simulation Program: Modeling Negative-Index Electromagnetic Metamaterials in Code","Testing and Verifying Negative-Index Electromagnetic Metamaterials","Safety, Limits, and Responsible Use of Negative-Index Electromagnetic Metamaterials","Scaling Negative-Index Electromagnetic Metamaterials to Production","The Full Teaching Ladder for Negative-Index Electromagnetic Metamaterials","Open Problems and Next Steps in Negative-Index Electromagnetic Metamaterials"]};;
var DEMOKIND="signature negative-index electromagnetic metamaterial record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature negative-index electromagnetic metamaterial record planner — "+safe+"\n"
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
    name:topic+' — signature negative-index electromagnetic metamaterial record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature negative-index electromagnetic metamaterial record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-681-negative-index-electromagnetic-metamaterials-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-681-negative-index-electromagnetic-metamaterials-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
