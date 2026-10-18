(function(){'use strict';
/* JAH The Smell-Generating Devices Future Technology Database generator — jahdb-futuretech-55-smell-generating-devices-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT55-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "c. 3000 BCE: Incense - Controlled Scent Begins - Foundations",
  "c. 1000 CE: Distilled Perfume - Scent in a Bottle - Foundations",
  "1874: Synthetic Vanillin - Scent from Chemistry - Foundations",
  "1959: AromaRama - Scented Cinema - Foundations",
  "1960: Smell-O-Vision - Scent at Your Seat - Foundations",
  "1980s: Scratch-n-Sniff - Pocket Scent - Foundations",
  "1999: iSmell - Scent for the PC - Foundations",
  "2002: the Scent Dome Tries Again - Foundations",
  "2005: Fragrance Communication Research - Foundations",
  "2011: the Smelling Screen - Foundations",
  "2013: Scentee - the Phone Gets a Nose - Foundations"
 ],
 "Compounded": [
  "2014: oPhone - Texting in Smell - Compounded",
  "2015: Feelreal - VR Gets a Nose - Compounded",
  "2017: VAQSO - Scent for VR - Compounded",
  "2019: OVR ION - Scent as an API - Compounded",
  "2020: Aroma Shooter - Directional Scent - Compounded",
  "2020: Smell Training - Scent as Medicine - Compounded",
  "2021: Scented Training Simulations - Compounded",
  "2022: the Scent Cartridge Standardizes - Compounded",
  "2023: Osmo - Digitizing Scent - Compounded",
  "2023: AI Designs Fragrance - Compounded",
  "2024: Scented Attractions - Compounded",
  "2025: Consumer VR Goes Multisensory - Compounded"
 ],
 "Advanced": [
  "Streaming with Scent Tracks - Advanced",
  "Full Olfactory VR - Advanced",
  "The Smell-O-Phone - Advanced",
  "The Scent Message Standard - Advanced",
  "Smart-Home Scent Environments - Advanced",
  "Scent Alerts for Accessibility - Advanced",
  "The Scent Archive - Advanced",
  "Medical Scent Devices - Advanced",
  "Remote Presence with Scent - Advanced",
  "Personal Scent Profiles - Advanced",
  "The Everyday Olfactory Display - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — smell-generating device record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A smell-generating device record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-55-smell-generating-devices-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-55-smell-generating-devices-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-55-smell-generating-devices',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
