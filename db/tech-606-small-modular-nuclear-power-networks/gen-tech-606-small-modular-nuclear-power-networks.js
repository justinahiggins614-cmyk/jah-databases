(function(){'use strict';
/* JAH The Small Modular Nuclear Power Networks Database generator — jahdb-tech-606-small-modular-nuclear-power-networks-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET606-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Small Modular Nuclear Power Networks Is","The Current State of Small Modular Nuclear Power Networks","Core Principles of Small Modular Nuclear Power Networks","Key Vocabulary of Small Modular Nuclear Power Networks","Why Small Modular Nuclear Power Networks Matters"],"Compounded":["Piece 1 of Small Modular Nuclear Power Networks: Primary Conversion Unit","Piece 2 of Small Modular Nuclear Power Networks: Fuel and Resource Supply","Piece 3 of Small Modular Nuclear Power Networks: Thermal Management","Piece 4 of Small Modular Nuclear Power Networks: Power Conditioning","Piece 5 of Small Modular Nuclear Power Networks: Storage Buffer","Piece 6 of Small Modular Nuclear Power Networks: Control and Dispatch Software","Piece 7 of Small Modular Nuclear Power Networks: Safety and Containment","Piece 8 of Small Modular Nuclear Power Networks: Grid Interconnection","How the Pieces of Small Modular Nuclear Power Networks Fit Together","Build Plan: Making Small Modular Nuclear Power Networks Step by Step"],"Advanced":["The Working Small Modular Nuclear Power Network: What a Real Build Looks Like","Simulation Program: Modeling Small Modular Nuclear Power Networks in Code","Testing and Verifying Small Modular Nuclear Power Networks","Safety, Limits, and Responsible Use of Small Modular Nuclear Power Networks","Scaling Small Modular Nuclear Power Networks to Production","The Full Teaching Ladder for Small Modular Nuclear Power Networks","Open Problems and Next Steps in Small Modular Nuclear Power Networks"]};;
var DEMOKIND="small modular nuclear power network record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# small modular nuclear power network record planner — "+safe+"\n"
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
    name:topic+' — small modular nuclear power network record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A small modular nuclear power network record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-606-small-modular-nuclear-power-networks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-606-small-modular-nuclear-power-networks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
