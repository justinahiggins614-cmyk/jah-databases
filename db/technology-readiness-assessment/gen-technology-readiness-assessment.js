(function(){'use strict';
/* JAH The Technology Readiness Assessment Database generator — jahdb-technology-readiness-assessment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Technology Readiness Assessment: What It Is Today, Honestly — foundations",
  "Technology Readiness Assessment: The TRL Scale Applied — foundations",
  "Technology Readiness Assessment: How It Could Develop — foundations",
  "Technology Readiness Assessment: What Is Useful Now — foundations",
  "Technology Readiness Assessment: Evaluating Bold Claims — foundations",
  "Technology Readiness Assessment: The History Rhymes — foundations",
  "Technology Readiness Assessment: Key Players Map — foundations",
  "Technology Readiness Assessment: The Economics — foundations",
  "Technology Readiness Assessment: Risks and Downsides — foundations",
  "Technology Readiness Assessment: Regulation on the Horizon — foundations",
  "Technology Readiness Assessment: Skills for the Transition — foundations",
  "Technology Readiness Assessment: Building With It Today — foundations"
 ],
 "compounded": [
  "Technology Readiness Assessment: Measuring Progress — compounded",
  "Technology Readiness Assessment: The Skeptic's Toolkit — compounded",
  "Technology Readiness Assessment: Where It Meets Your Work — compounded",
  "Technology Readiness Assessment: Teaching Emerging Tech — compounded",
  "Technology Readiness Assessment: The 5-Year View — compounded",
  "Technology Readiness Assessment: The 20-Year View — compounded",
  "Technology Readiness Assessment: Integration Patterns — compounded",
  "Technology Readiness Assessment: AI Meets Everything — compounded",
  "Technology Readiness Assessment: Toolchain Building — compounded",
  "Technology Readiness Assessment: Continuous Improvement — compounded",
  "Technology Readiness Assessment: Advanced: Deep Tech Diligence — compounded",
  "Technology Readiness Assessment: Advanced: Standards Shaping — compounded"
 ],
 "advanced": [
  "Technology Readiness Assessment: Advanced: The Research Frontier — advanced",
  "Technology Readiness Assessment: Advanced: Systems Integration — advanced",
  "Technology Readiness Assessment: Advanced: Policy Engagement — advanced",
  "Technology Readiness Assessment: Advanced: Building the Ecosystem — advanced",
  "Technology Readiness Assessment: Advanced: Long Bets — advanced",
  "Technology Readiness Assessment: Advanced: Teaching the Future — advanced",
  "Technology Readiness Assessment: Advanced: The Wise Adopter — advanced",
  "Technology Readiness Assessment: Advanced: Legacy Thinking — advanced",
  "Technology Readiness Assessment: Advanced: The United View — advanced",
  "Technology Readiness Assessment: Advanced: Staying Human — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Technology Readiness Assessment Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-technology-readiness-assessment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('technology-readiness-assessment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
