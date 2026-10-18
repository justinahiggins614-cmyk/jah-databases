(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-musical-instruments-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MINSS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Musical Instrument (Signature edition)",
  "The Five Hornbostel-Sachs Families (Signature edition)",
  "How Strings Make Sound (Signature edition)",
  "How Air Columns Make Sound (Signature edition)",
  "How Membranes and Bars Make Sound (Signature edition)",
  "How Electronic Instruments Make Sound (Signature edition)",
  "Range, Timbre, and Dynamics (Signature edition)",
  "The Orchestra's Instrument Layout (Signature edition)",
  "Folk Instruments Around the World (Signature edition)",
  "Choosing Your First Instrument (Signature edition)",
  "Caring for Instruments (Signature edition)"
 ],
 "Compounded": [
  "String Family Deep Dive (Signature edition)",
  "Woodwind Mechanics (Signature edition)",
  "Brass Mechanics (Signature edition)",
  "Percussion: Tuned vs Untuned (Signature edition)",
  "Keyboard Action Mechanics (Signature edition)",
  "Synthesizers and Samplers (Signature edition)",
  "The Human Voice as Instrument (Signature edition)",
  "Traditional Instruments of Asia (Signature edition)",
  "Traditional Instruments of Africa (Signature edition)",
  "Traditional Instruments of the Americas (Signature edition)",
  "The Pipe Organ: King of Instruments (Signature edition)",
  "Rare and Experimental Instruments (Signature edition)"
 ],
 "Advanced": [
  "Acoustics of the Concert Hall (Signature edition)",
  "Instrument Making: Luthiery Basics (Signature edition)",
  "The Stradivarius Mystery (Signature edition)",
  "Extended Techniques (Signature edition)",
  "Prepared Piano and Extended Percussion (Signature edition)",
  "Microtonal Instruments (Signature edition)",
  "The Ondes Martenot and Theremin (Signature edition)",
  "Instrument Acoustics Math (Signature edition)",
  "Collecting and Valuing Instruments (Signature edition)",
  "The Future of Instrument Design (Signature edition)",
  "Restoring Vintage Instruments (Signature edition)"
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
var gen={version:'jahdb-musical-instruments-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('musical-instruments-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
