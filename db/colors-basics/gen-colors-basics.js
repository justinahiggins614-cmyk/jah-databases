(function(){'use strict';
/* JAH The Colors Basics Database generator — jahdb-colors-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COLB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Color - Foundations",
  "How the Eye Sees Color - Foundations",
  "Hue, Value, and Chroma - Foundations",
  "Light and Pigment: Two Ways Color Is Made - Foundations",
  "The Primary Colors - Foundations",
  "The Secondary Colors - Foundations",
  "The Tertiary Colors - Foundations",
  "Warm and Cool Colors - Foundations",
  "Tints, Shades, and Tones - Foundations",
  "Neutral Colors - Foundations"
 ],
 "Compounded": [
  "The Color Wheel - Compounded",
  "Mixing Paint: Subtractive Color Mixing - Compounded",
  "Mixing Light: Additive Color Mixing - Compounded",
  "Opposites on the Wheel: Complementary Colors - Compounded",
  "Neighbors on the Wheel: Analogous Colors - Compounded",
  "Triadic Color Schemes - Compounded",
  "Color Temperature - Compounded",
  "Saturation: How Intense a Color Is - Compounded",
  "Brightness and Lightness - Compounded",
  "The Red Family - Compounded",
  "The Blue Family - Compounded",
  "The Green Family - Compounded",
  "The Yellow Family - Compounded",
  "The Purple Family - Compounded",
  "The Orange Family - Compounded",
  "Brown: The Dark Orange - Compounded",
  "Gray: Between Black and White - Compounded",
  "Black and White - Compounded"
 ],
 "Advanced": [
  "Color Harmonies and Schemes - Advanced",
  "Reading Color Codes: Hex and RGB - Advanced",
  "CMYK: Color for Print - Advanced",
  "Color Vision Differences - Advanced",
  "Color and Emotion - Advanced",
  "The Spectrum and Beyond: Infrared and Ultraviolet - Advanced"
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
var gen={version:'jahdb-colors-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('colors-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
