(function(){'use strict';
/* JAH The Unsolved Musicology Database generator — jahdb-unsolved-musicology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USMU-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Music Moves Us - Psychology",
  "The Origins of Music - History",
  "Universals in Music - Theory",
  "Absolute Music: What Does It Mean - Aesthetics",
  "The Work Concept Problem - Aesthetics",
  "Musical Emotion: Real or Perceived - Psychology",
  "Why We Like Sad Music - Psychology",
  "The Earworm Problem - Psychology",
  "Perfect Pitch: Nature or Nurture - Psychology",
  "Rhythm: Why We Move - Theory",
  "Consonance: Nature or Culture - Theory"
 ],
 "Compounded": [
  "The Mozart Effect Myth - Psychology",
  "Music and Memory: Why Songs Stick - Psychology",
  "The Canon Problem - History",
  "Authorship in Early Music - History",
  "Improvisation Versus Composition - History",
  "The Notation Problem - Theory",
  "Tuning Systems: The Compromise - Theory",
  "Timbre: The Neglected Parameter - Theory",
  "The Album Problem - Sociology",
  "Popular Versus Classical: The Divide - Sociology",
  "Music and Identity - Sociology",
  "The Cover Song Question - Sociology"
 ],
 "Advanced": [
  "AI Composition: Is It Music - Technology",
  "The Copyright Problem in Music - Technology",
  "Streaming: What It Did to Music - Sociology",
  "The Live Music Problem - Sociology",
  "Music Therapy: Does It Work - Psychology",
  "The Evolution of Musical Style - History",
  "Lost Music: What We Cannot Hear - History",
  "The Future of the Orchestra - Sociology",
  "Notation After the Digital Turn - Technology",
  "The Ontology of Recorded Music - Aesthetics",
  "A Unified Theory of Music - Aesthetics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Musicology Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-musicology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-musicology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-musicology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
