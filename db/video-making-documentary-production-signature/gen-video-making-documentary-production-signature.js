(function(){'use strict';
/* JAH The Documentary Production Database — Signature Edition generator — 1.0.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMDPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Finding Documentary Stories",
  "Research: The Foundation",
  "Pre-Interviews",
  "Treatments and Proposals",
  "Funding and Grants",
  "Legal: Releases and Clearances",
  "Documentary Ethics",
  "Interview Technique",
  "Verite Shooting",
  "B-Roll for Documentaries",
  "Narration and Voiceover",
  "Archival Footage Research"
 ],
 "Compounded": [
  "Fair Use in Documentary",
  "Reenactments: Ethics and Craft",
  "Animation in Documentary",
  "Editing Documentary: Finding the Story",
  "Fact-Checking",
  "Music for Documentary",
  "Color and Sound for Docs",
  "Festival Strategy",
  "Distribution: The Long Tail",
  "Impact Campaigns",
  "Producing Documentaries: The Manager's Craft"
 ],
 "Advanced": [
  "Character-Driven vs Issue-Driven",
  "Historical Documentaries",
  "Nature Documentaries",
  "True Crime Documentaries",
  "Observational Ethics in the Field",
  "Translation and Subtitles for Docs",
  "The Documentary Career",
  "Documentary Series and Limited Series",
  "The Verite Canon: Studying the Masters",
  "Documentary Distribution in the Streaming Era",
  "Legacy: Archiving Your Documentary Work"
 ]
};
var DEMOKIND="signature documentary planner";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature Documentary Planner — "+safe+"\n"
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
    name:topic+' — documentary production record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A documentary production record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-making-documentary-production-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
