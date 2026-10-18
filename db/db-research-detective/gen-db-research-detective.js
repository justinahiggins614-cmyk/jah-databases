(function(){'use strict';
/* JAH The Research Detective Database generator — jahdb-db-research-detective-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RSD-";
var FIELDS=["Sources","Searching","Synthesis"];
var TOPICS={
 "Sources": [
  "The Case File: Defining Your Question - Sources",
  "Source Hierarchy: Know Your Witnesses - Sources",
  "Spotting Credible Sources - Sources",
  "Wikipedia: Launchpad, Not Destination - Sources",
  "Academic Papers: Reading the Real Thing - Sources",
  "Books vs Articles - Sources",
  "Government and Institutional Data - Sources",
  "News: Reading the First Draft - Sources",
  "Interviews as Sources - Sources",
  "Evaluating Websites - Sources",
  "The Reference Trail - Sources",
  "When Sources Disagree - Sources"
 ],
 "Searching": [
  "Search Like a Detective - Searching",
  "Keywords: Think in Synonyms - Searching",
  "Scholarly Search Tools - Searching",
  "Library Superpowers - Searching",
  "Interviewing Experts - Searching",
  "FOIA and Public Records - Searching",
  "Data Hunting - Searching",
  "Searching in Other Languages - Searching",
  "Staying Organized: The Case Board - Searching",
  "Alerts and Feeds - Searching",
  "Patent Searching - Searching",
  "Asking an Archivist - Searching"
 ],
 "Synthesis": [
  "Note-Taking That Thinks - Synthesis",
  "Outlining: Structure Before Sentences - Synthesis",
  "Synthesizing Multiple Sources - Synthesis",
  "Citing: Giving Credit - Synthesis",
  "Writing the Report - Synthesis",
  "Presenting Findings - Synthesis",
  "Peer Review: Surviving Scrutiny - Synthesis",
  "Updating Beliefs - Synthesis",
  "The Detective's Oath - Synthesis",
  "Case Closed: Your First Investigation - Synthesis"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Research Detective Study — "+safe+"\n"
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
    name:topic+' — research lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A research lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"research-detective-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-research-detective-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-research-detective',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
