(function(){'use strict';
/* JAH The Signature Nuclear-Electric Deep-Space Propulsion Database generator — jahdb-tech-711-nuclear-electric-deep-space-propulsion-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET711S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Nuclear-Electric Deep-Space Propulsion Is","The Current State of Nuclear-Electric Deep-Space Propulsion","Core Principles of Nuclear-Electric Deep-Space Propulsion","Key Vocabulary of Nuclear-Electric Deep-Space Propulsion","Why Nuclear-Electric Deep-Space Propulsion Matters"],"Compounded":["Piece 1 of Nuclear-Electric Deep-Space Propulsion: Launch and Transit","Piece 2 of Nuclear-Electric Deep-Space Propulsion: Power System","Piece 3 of Nuclear-Electric Deep-Space Propulsion: Thermal Control","Piece 4 of Nuclear-Electric Deep-Space Propulsion: Communications","Piece 5 of Nuclear-Electric Deep-Space Propulsion: Guidance and Navigation","Piece 6 of Nuclear-Electric Deep-Space Propulsion: Platform Structure","Piece 7 of Nuclear-Electric Deep-Space Propulsion: Mission Core Systems","Piece 8 of Nuclear-Electric Deep-Space Propulsion: Ground Operations","How the Pieces of Nuclear-Electric Deep-Space Propulsion Fit Together","Build Plan: Making Nuclear-Electric Deep-Space Propulsion Step by Step"],"Advanced":["The Working Nuclear-Electric Deep-Space Propulsion: What a Real Build Looks Like","Simulation Program: Modeling Nuclear-Electric Deep-Space Propulsion in Code","Testing and Verifying Nuclear-Electric Deep-Space Propulsion","Safety, Limits, and Responsible Use of Nuclear-Electric Deep-Space Propulsion","Scaling Nuclear-Electric Deep-Space Propulsion to Production","The Full Teaching Ladder for Nuclear-Electric Deep-Space Propulsion","Open Problems and Next Steps in Nuclear-Electric Deep-Space Propulsion"]};;
var DEMOKIND="signature nuclear-electric deep-space propulsion record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature nuclear-electric deep-space propulsion record planner — "+safe+"\n"
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
    name:topic+' — signature nuclear-electric deep-space propulsion record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature nuclear-electric deep-space propulsion record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-711-nuclear-electric-deep-space-propulsion-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-711-nuclear-electric-deep-space-propulsion-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
