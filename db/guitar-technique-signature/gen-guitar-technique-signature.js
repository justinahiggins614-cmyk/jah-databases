(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-guitar-technique-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GUITS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Holding the Guitar (Signature edition)",
  "Guitar Tuning (Signature edition)",
  "First Chords (Signature edition)",
  "Strumming Patterns (Signature edition)",
  "Fingerpicking Basics (Signature edition)",
  "Reading Tablature (Signature edition)",
  "The CAGED System (Signature edition)",
  "Power Chords (Signature edition)",
  "Palm Muting (Signature edition)",
  "Basic Scales (Signature edition)",
  "Guitar Practice Routines (Signature edition)"
 ],
 "Compounded": [
  "Barre Chords (Signature edition)",
  "Travis Picking (Signature edition)",
  "Alternate Picking (Signature edition)",
  "Legato: Hammer-ons and Pull-offs (Signature edition)",
  "Slides and Bends (Signature edition)",
  "Guitar Vibrato (Signature edition)",
  "Fingerstyle Arranging (Signature edition)",
  "Classical Guitar Technique (Signature edition)",
  "Flamenco Techniques (Signature edition)",
  "Slide Guitar (Signature edition)",
  "Hybrid Picking (Signature edition)",
  "Chord Melody (Signature edition)"
 ],
 "Advanced": [
  "Sweep Picking (Signature edition)",
  "Tapping: Two-Hand Technique (Signature edition)",
  "Economy Picking (Signature edition)",
  "Modes and Application (Signature edition)",
  "Jazz Comping (Signature edition)",
  "Chicken Pickin' (Signature edition)",
  "Percussive Guitar (Signature edition)",
  "Advanced Fingerstyle (Signature edition)",
  "Improvisation Frameworks (Signature edition)",
  "Recording Guitar (Signature edition)",
  "Building Speed Safely (Signature edition)"
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
var gen={version:'jahdb-guitar-technique-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('guitar-technique-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
