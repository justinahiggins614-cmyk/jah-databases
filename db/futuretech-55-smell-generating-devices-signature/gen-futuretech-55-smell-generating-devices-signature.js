(function(){'use strict';
/* JAH The Smell-Generating Devices Future Technology Database — Signature Edition generator — jahdb-futuretech-55-smell-generating-devices-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT55-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Smell Generating Devices — Incense - Controlled Scent Begins (Signature Edition)", "Smell Generating Devices — Distilled Perfume - Scent in a Bottle (Signature Edition)", "Smell Generating Devices — Synthetic Vanillin - Scent from Chemistry (Signature Edition)", "Smell Generating Devices — AromaRama - Scented Cinema (Signature Edition)", "Smell Generating Devices — Smell-O-Vision - Scent at Your Seat (Signature Edition)", "Smell Generating Devices — Scratch-n-Sniff - Pocket Scent (Signature Edition)", "Smell Generating Devices — iSmell - Scent for the PC (Signature Edition)", "Smell Generating Devices — the Scent Dome Tries Again (Signature Edition)", "Smell Generating Devices — Fragrance Communication Research (Signature Edition)", "Smell Generating Devices — the Smelling Screen (Signature Edition)", "Smell Generating Devices — Scentee - the Phone Gets a Nose (Signature Edition)"], "Compounded": ["Smell Generating Devices — oPhone - Texting in Smell (Signature Edition)", "Smell Generating Devices — Feelreal - VR Gets a Nose (Signature Edition)", "Smell Generating Devices — VAQSO - Scent for VR (Signature Edition)", "Smell Generating Devices — OVR ION - Scent as an API (Signature Edition)", "Smell Generating Devices — Aroma Shooter - Directional Scent (Signature Edition)", "Smell Generating Devices — Smell Training - Scent as Medicine (Signature Edition)", "Smell Generating Devices — Scented Training Simulations (Signature Edition)", "Smell Generating Devices — the Scent Cartridge Standardizes (Signature Edition)", "Smell Generating Devices — Osmo - Digitizing Scent (Signature Edition)", "Smell Generating Devices — AI Designs Fragrance (Signature Edition)", "Smell Generating Devices — Scented Attractions (Signature Edition)", "Smell Generating Devices — Consumer VR Goes Multisensory (Signature Edition)"], "Advanced": ["Smell Generating Devices — Streaming with Scent Tracks (Signature Edition)", "Smell Generating Devices — Full Olfactory VR (Signature Edition)", "Smell Generating Devices — The Smell-O-Phone (Signature Edition)", "Smell Generating Devices — The Scent Message Standard (Signature Edition)", "Smell Generating Devices — Smart-Home Scent Environments (Signature Edition)", "Smell Generating Devices — Scent Alerts for Accessibility (Signature Edition)", "Smell Generating Devices — The Scent Archive (Signature Edition)", "Smell Generating Devices — Medical Scent Devices (Signature Edition)", "Smell Generating Devices — Remote Presence with Scent (Signature Edition)", "Smell Generating Devices — Personal Scent Profiles (Signature Edition)", "Smell Generating Devices — The Everyday Olfactory Display (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Smell Generating Devices study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-55-smell-generating-devices-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-55-smell-generating-devices-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
