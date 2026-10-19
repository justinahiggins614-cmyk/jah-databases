(function(){'use strict';
/* JAH The United Video Making Master Database generator — 1.0.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMUN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Fifteen Ways: A Map",
  "Choosing the Right Method",
  "The Strength Rule: Each Method's Best",
  "Budget Planning Across Methods",
  "Timeline Planning Across Methods",
  "Team Roles Across Methods",
  "The Pre-Production Master Checklist",
  "The Production Master Checklist",
  "The Post-Production Master Checklist",
  "The Delivery Master Checklist",
  "Method Comparison Matrix",
  "When to Use AI vs Traditional"
 ],
 "Compounded": [
  "Live Action + VFX: The Classic Hybrid",
  "Animation + Live Action Hybrids",
  "AI Video + Traditional Editing",
  "Documentary + Motion Graphics",
  "Streaming + Edited Content",
  "Sound Across All Methods",
  "Color Across All Methods",
  "Story Across All Methods",
  "The Teaching Ladder: Beginner Path",
  "The Teaching Ladder: Intermediate Path"
 ],
 "Advanced": [
  "The Teaching Ladder: Advanced Path",
  "The Solo Creator Path",
  "The Pro Studio Path",
  "Tool Ecosystem Map",
  "Format Interoperability",
  "Archival Master Strategy",
  "Quality Gates Across Methods",
  "Client Communication for Multi-Method",
  "Pricing Multi-Method Productions",
  "Portfolio Across Methods",
  "The Future of Video Making (Signature Outlook)",
  "Cross-Reference Index: All Fifteen"
 ]
};
var DEMOKIND="united video planner";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# United Video Planner — "+safe+"\n"
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
    name:topic+' — united video making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A united video making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'1.0.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-making-united',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
