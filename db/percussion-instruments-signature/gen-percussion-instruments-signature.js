(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-percussion-instruments-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PERIS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Percussion Family (Signature edition)",
  "Snare Drum (Signature edition)",
  "Bass Drum (Signature edition)",
  "Timpani (Signature edition)",
  "Cymbals (Signature edition)",
  "Xylophone (Signature edition)",
  "Marimba (Signature edition)",
  "Vibraphone (Signature edition)",
  "Tambourine (Signature edition)",
  "Hand Drums: Congas and Bongos (Signature edition)",
  "Mallets and Sticks (Signature edition)"
 ],
 "Compounded": [
  "Glockenspiel (Signature edition)",
  "Tubular Bells (Signature edition)",
  "Triangle and Small Percussion (Signature edition)",
  "Cajon (Signature edition)",
  "Djembe (Signature edition)",
  "Tabla (Signature edition)",
  "Taiko Drums (Signature edition)",
  "Steelpan: Trinidad's Tuned Drums (Signature edition)",
  "Drum Kit Anatomy (Signature edition)",
  "Latin Percussion (Signature edition)",
  "Frame Drums (Signature edition)",
  "Gongs and Tam-tams (Signature edition)"
 ],
 "Advanced": [
  "Four-Mallet Technique (Signature edition)",
  "Timpani Tuning (Signature edition)",
  "Rudiments Mastery (Signature edition)",
  "Orchestral Percussion Excerpts (Signature edition)",
  "Polyrhythms (Signature edition)",
  "Drum Corps and Marching (Signature edition)",
  "Electronic Percussion (Signature edition)",
  "Studio Percussion Recording (Signature edition)",
  "Building a Percussion Rig (Signature edition)",
  "World Percussion Ensemble (Signature edition)",
  "Caring for Percussion (Signature edition)"
 ]
};
var DEMOKIND="instrument acoustics";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Instrument acoustics sketch — "+safe+"\n"
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
var gen={version:'jahdb-percussion-instruments-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('percussion-instruments-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
