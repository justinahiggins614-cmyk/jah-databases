(function(){'use strict';
/* JAH The Signature Self-Purifying Drinking Water Networks Database generator — jahdb-tech-778-self-purifying-drinking-water-networks-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET778S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Self-Purifying Drinking Water Networks Is","The Current State of Self-Purifying Drinking Water Networks","Core Principles of Self-Purifying Drinking Water Networks","Key Vocabulary of Self-Purifying Drinking Water Networks","Why Self-Purifying Drinking Water Networks Matters"],"Compounded":["Piece 1 of Self-Purifying Drinking Water Networks: Source Capture","Piece 2 of Self-Purifying Drinking Water Networks: Purification and Production Core","Piece 3 of Self-Purifying Drinking Water Networks: Quality Sensing","Piece 4 of Self-Purifying Drinking Water Networks: Distribution Network","Piece 5 of Self-Purifying Drinking Water Networks: Storage Buffer","Piece 6 of Self-Purifying Drinking Water Networks: Energy Integration","Piece 7 of Self-Purifying Drinking Water Networks: Waste Recovery","Piece 8 of Self-Purifying Drinking Water Networks: Community Interface","How the Pieces of Self-Purifying Drinking Water Networks Fit Together","Build Plan: Making Self-Purifying Drinking Water Networks Step by Step"],"Advanced":["The Working Self-Purifying Drinking Water Network: What a Real Build Looks Like","Simulation Program: Modeling Self-Purifying Drinking Water Networks in Code","Testing and Verifying Self-Purifying Drinking Water Networks","Safety, Limits, and Responsible Use of Self-Purifying Drinking Water Networks","Scaling Self-Purifying Drinking Water Networks to Production","The Full Teaching Ladder for Self-Purifying Drinking Water Networks","Open Problems and Next Steps in Self-Purifying Drinking Water Networks"]};;
var DEMOKIND="signature self-purifying drinking water network record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature self-purifying drinking water network record planner — "+safe+"\n"
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
    name:topic+' — signature self-purifying drinking water network record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature self-purifying drinking water network record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-778-self-purifying-drinking-water-networks-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-778-self-purifying-drinking-water-networks-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
