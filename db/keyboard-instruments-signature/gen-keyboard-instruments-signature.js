(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-keyboard-instruments-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KYBIS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Keyboard Family (Signature edition)",
  "Piano (Signature edition)",
  "How the Piano Action Works (Signature edition)",
  "Organ (Signature edition)",
  "Harpsichord (Signature edition)",
  "Clavichord (Signature edition)",
  "Accordion (Signature edition)",
  "Celesta (Signature edition)",
  "Reading Two Staves (Signature edition)",
  "Pedals: Damper, Soft, Sostenuto (Signature edition)",
  "Sitting Posture at the Keyboard (Signature edition)"
 ],
 "Compounded": [
  "Electric Piano (Rhodes, Wurlitzer) (Signature edition)",
  "Synthesizer Keyboards (Signature edition)",
  "Digital Pianos (Signature edition)",
  "Pipe Organ Stops (Signature edition)",
  "Reed Organ and Harmonium (Signature edition)",
  "Clavinet (Signature edition)",
  "Mellotron: The Tape-Playing Keyboard (Signature edition)",
  "Keytar (Signature edition)",
  "Fortepiano (Signature edition)",
  "Tuning and Temperament (Signature edition)",
  "Keyboard Ranges Compared (Signature edition)",
  "Choosing a Keyboard (Signature edition)"
 ],
 "Advanced": [
  "Voicing and Regulating Pianos (Signature edition)",
  "Pipe Organ Building (Signature edition)",
  "Concert Grand Anatomy (Signature edition)",
  "Playing from Figured Bass (Signature edition)",
  "Keyboard Improvisation (Signature edition)",
  "Advanced Pedaling (Signature edition)",
  "The Well-Tempered Legacy (Signature edition)",
  "Maintaining Pianos (Signature edition)",
  "Vintage Electric Pianos (Signature edition)",
  "Keyboard Amplification (Signature edition)",
  "The Future of Keyboards (Signature edition)"
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
var gen={version:'jahdb-keyboard-instruments-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('keyboard-instruments-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
