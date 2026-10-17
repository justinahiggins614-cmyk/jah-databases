(function(){'use strict';
/* JAH The Colors Basics Signature Database generator — jahdb-colors-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COLBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Color (Signature Edition) - Foundations",
  "How the Eye Sees Color (Signature Edition) - Foundations",
  "Hue, Value, and Chroma (Signature Edition) - Foundations",
  "Light and Pigment: Two Ways Color Is Made (Signature Edition) - Foundations",
  "The Primary Colors (Signature Edition) - Foundations",
  "The Secondary Colors (Signature Edition) - Foundations",
  "The Tertiary Colors (Signature Edition) - Foundations",
  "Warm and Cool Colors (Signature Edition) - Foundations",
  "Tints, Shades, and Tones (Signature Edition) - Foundations",
  "Neutral Colors (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Color Wheel (Signature Edition) - Compounded",
  "Mixing Paint: Subtractive Color Mixing (Signature Edition) - Compounded",
  "Mixing Light: Additive Color Mixing (Signature Edition) - Compounded",
  "Opposites on the Wheel: Complementary Colors (Signature Edition) - Compounded",
  "Neighbors on the Wheel: Analogous Colors (Signature Edition) - Compounded",
  "Triadic Color Schemes (Signature Edition) - Compounded",
  "Color Temperature (Signature Edition) - Compounded",
  "Saturation: How Intense a Color Is (Signature Edition) - Compounded",
  "Brightness and Lightness (Signature Edition) - Compounded",
  "The Red Family (Signature Edition) - Compounded",
  "The Blue Family (Signature Edition) - Compounded",
  "The Green Family (Signature Edition) - Compounded",
  "The Yellow Family (Signature Edition) - Compounded",
  "The Purple Family (Signature Edition) - Compounded",
  "The Orange Family (Signature Edition) - Compounded",
  "Brown: The Dark Orange (Signature Edition) - Compounded",
  "Gray: Between Black and White (Signature Edition) - Compounded",
  "Black and White (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Color Harmonies and Schemes (Signature Edition) - Advanced",
  "Reading Color Codes: Hex and RGB (Signature Edition) - Advanced",
  "CMYK: Color for Print (Signature Edition) - Advanced",
  "Color Vision Differences (Signature Edition) - Advanced",
  "Color and Emotion (Signature Edition) - Advanced",
  "The Spectrum and Beyond: Infrared and Ultraviolet (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Color Basics Study — "+safe+"\n"
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
    name:topic+' — colors basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A colors basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"color-basics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-colors-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('colors-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
