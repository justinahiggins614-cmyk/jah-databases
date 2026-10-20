(function(){'use strict';
/* JAH The Signature Smart Water-Leak Prevention Buildings Database generator — jahdb-tech-864-smart-water-leak-prevention-buildings-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET864S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Smart Water-Leak Prevention Buildings Is","The Current State of Smart Water-Leak Prevention Buildings","Core Principles of Smart Water-Leak Prevention Buildings","Key Vocabulary of Smart Water-Leak Prevention Buildings","Why Smart Water-Leak Prevention Buildings Matters"],"Compounded":["Piece 1 of Smart Water-Leak Prevention Buildings: Structural System","Piece 2 of Smart Water-Leak Prevention Buildings: Robotic Construction Equipment","Piece 3 of Smart Water-Leak Prevention Buildings: Materials Supply","Piece 4 of Smart Water-Leak Prevention Buildings: Building Intelligence","Piece 5 of Smart Water-Leak Prevention Buildings: Energy System","Piece 6 of Smart Water-Leak Prevention Buildings: Water and Waste","Piece 7 of Smart Water-Leak Prevention Buildings: Mobility Integration","Piece 8 of Smart Water-Leak Prevention Buildings: Resilience Engineering","How the Pieces of Smart Water-Leak Prevention Buildings Fit Together","Build Plan: Making Smart Water-Leak Prevention Buildings Step by Step"],"Advanced":["The Working Smart Water-Leak Prevention Building: What a Real Build Looks Like","Simulation Program: Modeling Smart Water-Leak Prevention Buildings in Code","Testing and Verifying Smart Water-Leak Prevention Buildings","Safety, Limits, and Responsible Use of Smart Water-Leak Prevention Buildings","Scaling Smart Water-Leak Prevention Buildings to Production","The Full Teaching Ladder for Smart Water-Leak Prevention Buildings","Open Problems and Next Steps in Smart Water-Leak Prevention Buildings"]};;
var DEMOKIND="signature smart water-leak prevention building record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature smart water-leak prevention building record planner — "+safe+"\n"
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
    name:topic+' — signature smart water-leak prevention building record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature smart water-leak prevention building record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-864-smart-water-leak-prevention-buildings-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-864-smart-water-leak-prevention-buildings-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
