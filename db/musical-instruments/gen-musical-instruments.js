(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-musical-instruments-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MINS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Musical Instrument",
  "The Five Hornbostel-Sachs Families",
  "How Strings Make Sound",
  "How Air Columns Make Sound",
  "How Membranes and Bars Make Sound",
  "How Electronic Instruments Make Sound",
  "Range, Timbre, and Dynamics",
  "The Orchestra's Instrument Layout",
  "Folk Instruments Around the World",
  "Choosing Your First Instrument",
  "Caring for Instruments"
 ],
 "Compounded": [
  "String Family Deep Dive",
  "Woodwind Mechanics",
  "Brass Mechanics",
  "Percussion: Tuned vs Untuned",
  "Keyboard Action Mechanics",
  "Synthesizers and Samplers",
  "The Human Voice as Instrument",
  "Traditional Instruments of Asia",
  "Traditional Instruments of Africa",
  "Traditional Instruments of the Americas",
  "The Pipe Organ: King of Instruments",
  "Rare and Experimental Instruments"
 ],
 "Advanced": [
  "Acoustics of the Concert Hall",
  "Instrument Making: Luthiery Basics",
  "The Stradivarius Mystery",
  "Extended Techniques",
  "Prepared Piano and Extended Percussion",
  "Microtonal Instruments",
  "The Ondes Martenot and Theremin",
  "Instrument Acoustics Math",
  "Collecting and Valuing Instruments",
  "The Future of Instrument Design",
  "Restoring Vintage Instruments"
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
    description:'SAMPLE RECORD (generated — structural sample). A music genre record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-musical-instruments-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('musical-instruments',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
