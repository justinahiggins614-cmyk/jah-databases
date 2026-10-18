(function(){'use strict';
/* JAH The Technological Singularity Technology Database generator — jahdb-futuretech-technological-singularity-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT002-";
var FIELDS=["Oldest Concepts","Early Development","Working Versions","State of the Art"];
var TOPICS={
 "Oldest Concepts": [
  "The Technological Singularity \u2014 Condorcet: the indefinite perfectibility of mind",
  "The Technological Singularity \u2014 Malthus: the mathematics of compounding",
  "The Technological Singularity \u2014 The industrial acceleration as lived experience",
  "The Technological Singularity \u2014 Von Neumann's 'essential singularity' via Ulam",
  "The Technological Singularity \u2014 I.J. Good: the intelligence explosion",
  "The Technological Singularity \u2014 Moore's Law stated",
  "The Technological Singularity \u2014 Vinge: 'The Coming Technological Singularity'",
  "The Technological Singularity \u2014 Kurzweil: The Age of Spiritual Machines"
 ],
 "Early Development": [
  "The Technological Singularity \u2014 The Law of Accelerating Returns",
  "The Technological Singularity \u2014 Bostrom: Superintelligence",
  "The Technological Singularity \u2014 Deep learning takeoff: capability jumps",
  "The Technological Singularity \u2014 GPT era: sudden generality",
  "The Technological Singularity \u2014 AI improves AI: early recursive tooling",
  "The Technological Singularity \u2014 The takeoff-speeds debate: fast vs slow",
  "The Technological Singularity \u2014 Compute scaling laws",
  "The Technological Singularity \u2014 The alignment problem enters mainstream",
  "The Technological Singularity \u2014 Forecasting tournaments on AI timelines"
 ],
 "Working Versions": [
  "The Technological Singularity \u2014 Current capability curves: tracking the trend",
  "The Technological Singularity \u2014 Recursive self-improvement: narrow versions working today",
  "The Technological Singularity \u2014 AI-designed chips and AI-written code",
  "The Technological Singularity \u2014 Economic indicators: watching for acceleration",
  "The Technological Singularity \u2014 The slow-takeoff evidence: bottlenecks",
  "The Technological Singularity \u2014 The fast-takeoff evidence: discontinuities",
  "The Technological Singularity \u2014 Governance proposals: preparedness frameworks",
  "The Technological Singularity \u2014 Differential technological development",
  "The Technological Singularity \u2014 Intelligence explosion vs. singularity: distinguishing scenarios"
 ],
 "State of the Art": [
  "The Technological Singularity \u2014 2026 status: no singularity; debate continues",
  "The Technological Singularity \u2014 Hard takeoff scenarios: the arguments",
  "The Technological Singularity \u2014 Soft takeoff scenarios: the arguments",
  "The Technological Singularity \u2014 Post-singularity economics: the models",
  "The Technological Singularity \u2014 Post-singularity governance: the proposals",
  "The Technological Singularity \u2014 Existential risk framing vs. techno-optimism",
  "The Technological Singularity \u2014 What would count as evidence the singularity began",
  "The Technological Singularity \u2014 The working version: trend-tracking and preparedness"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Technological Singularity study — "+safe+"\n"
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
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-technological-singularity-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-technological-singularity',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
