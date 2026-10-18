(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-singing-technique-vocal-training-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SGVTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "How the Voice Works (Signature edition)",
  "Posture for Singing (Signature edition)",
  "Breathing: Diaphragmatic (Signature edition)",
  "Warm-ups (Signature edition)",
  "Finding Your Range (Signature edition)",
  "Pitch Matching (Signature edition)",
  "Head Voice vs Chest Voice (Signature edition)",
  "Diction (Signature edition)",
  "Simple Songs (Signature edition)",
  "Listening Skills (Signature edition)",
  "Vocal Practice Routines (Signature edition)"
 ],
 "Compounded": [
  "Breath Control (Signature edition)",
  "Vocal Vibrato (Signature edition)",
  "Resonance (Signature edition)",
  "The Passaggio (Signature edition)",
  "Belting Safely (Signature edition)",
  "Falsetto (Signature edition)",
  "Articulation (Signature edition)",
  "Vocal Phrasing (Signature edition)",
  "Sight-Singing (Signature edition)",
  "Harmony Singing (Signature edition)",
  "Vocal Microphone Technique (Signature edition)",
  "Vocal Health and Care (Signature edition)"
 ],
 "Advanced": [
  "Coloratura Technique (Signature edition)",
  "Operatic Technique (Signature edition)",
  "Jazz Vocal Improvisation (Signature edition)",
  "Gospel Vocal Style (Signature edition)",
  "Extended Vocal Techniques (Signature edition)",
  "Audition Preparation (Signature edition)",
  "Recording Vocals (Signature edition)",
  "Vocal Pedagogy (Signature edition)",
  "Aging Voice Care (Signature edition)",
  "Performance Anxiety (Signature edition)",
  "Building a Repertoire (Signature edition)"
 ]
};
var DEMOKIND="practice planning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Practice planner — "+safe+"\n"
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
    name:topic+' — music genre record',
    title:topic,
    description:'SIGNATURE SAMPLE (generated — structural sample). A music genre record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-singing-technique-vocal-training-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('singing-technique-vocal-training-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
