(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-songwriting-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SGWS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Song (Signature edition)",
  "Verse-Chorus Form (Signature edition)",
  "Writing Lyrics (Signature edition)",
  "Song Melody Basics (Signature edition)",
  "Chord Progressions for Songs (Signature edition)",
  "Hooks (Signature edition)",
  "Rhyme Schemes (Signature edition)",
  "Song Titles (Signature edition)",
  "Co-writing (Signature edition)",
  "Simple Song Structures (Signature edition)",
  "Finishing Songs (Signature edition)"
 ],
 "Compounded": [
  "Bridges and Pre-choruses (Signature edition)",
  "Lyric Imagery (Signature edition)",
  "Melodic Contour (Signature edition)",
  "Groove and Feel (Signature edition)",
  "Song Arrangement (Signature edition)",
  "Writing to a Track (Signature edition)",
  "Topline Writing (Signature edition)",
  "Story Songs (Signature edition)",
  "Love Songs (Signature edition)",
  "Writing Demos (Signature edition)",
  "Feedback and Revision (Signature edition)",
  "Songwriting Discipline (Signature edition)"
 ],
 "Advanced": [
  "Advanced Harmony in Pop (Signature edition)",
  "Modulations in Songs (Signature edition)",
  "Odd Meters in Songwriting (Signature edition)",
  "Writing for Other Artists (Signature edition)",
  "Musical Theater Songs (Signature edition)",
  "Film Songs (Signature edition)",
  "Hit Song Analysis (Signature edition)",
  "The Business of Songwriting (Signature edition)",
  "Collaboration at Scale (Signature edition)",
  "Building a Catalog (Signature edition)",
  "Signature Sound (Signature edition)"
 ]
};
var DEMOKIND="form planning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Form planner — "+safe+"\n"
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
var gen={version:'jahdb-songwriting-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('songwriting-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
