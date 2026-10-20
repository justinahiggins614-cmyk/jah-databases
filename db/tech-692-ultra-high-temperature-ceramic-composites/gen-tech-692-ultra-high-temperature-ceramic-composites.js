(function(){'use strict';
/* JAH The Ultra-High-Temperature Ceramic Composites Database generator — jahdb-tech-692-ultra-high-temperature-ceramic-composites-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET692-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Ultra-High-Temperature Ceramic Composites Is","The Current State of Ultra-High-Temperature Ceramic Composites","Core Principles of Ultra-High-Temperature Ceramic Composites","Key Vocabulary of Ultra-High-Temperature Ceramic Composites","Why Ultra-High-Temperature Ceramic Composites Matters"],"Compounded":["Piece 1 of Ultra-High-Temperature Ceramic Composites: Precursor Chemistry","Piece 2 of Ultra-High-Temperature Ceramic Composites: Synthesis Reactor","Piece 3 of Ultra-High-Temperature Ceramic Composites: Structure Control","Piece 4 of Ultra-High-Temperature Ceramic Composites: Characterization Suite","Piece 5 of Ultra-High-Temperature Ceramic Composites: Property Testing","Piece 6 of Ultra-High-Temperature Ceramic Composites: Scale Manufacturing","Piece 7 of Ultra-High-Temperature Ceramic Composites: Integration Engineering","Piece 8 of Ultra-High-Temperature Ceramic Composites: Lifecycle and Safety","How the Pieces of Ultra-High-Temperature Ceramic Composites Fit Together","Build Plan: Making Ultra-High-Temperature Ceramic Composites Step by Step"],"Advanced":["The Working Ultra-High-Temperature Ceramic Composite: What a Real Build Looks Like","Simulation Program: Modeling Ultra-High-Temperature Ceramic Composites in Code","Testing and Verifying Ultra-High-Temperature Ceramic Composites","Safety, Limits, and Responsible Use of Ultra-High-Temperature Ceramic Composites","Scaling Ultra-High-Temperature Ceramic Composites to Production","The Full Teaching Ladder for Ultra-High-Temperature Ceramic Composites","Open Problems and Next Steps in Ultra-High-Temperature Ceramic Composites"]};;
var DEMOKIND="ultra-high-temperature ceramic composite record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# ultra-high-temperature ceramic composite record planner — "+safe+"\n"
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
    name:topic+' — ultra-high-temperature ceramic composite record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An ultra-high-temperature ceramic composite record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-692-ultra-high-temperature-ceramic-composites-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-692-ultra-high-temperature-ceramic-composites',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
