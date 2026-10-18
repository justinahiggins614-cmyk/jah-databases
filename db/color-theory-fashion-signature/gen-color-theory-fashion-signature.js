(function(){'use strict';
/* JAH The Color Theory Fashion Database generator — jahdb-color-theory-fashion-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CTFSS-";
var FIELDS=["Color Foundations", "Color in Practice", "Color Mastery"];
var TOPICS={
 "Color Foundations": [
  "The Color Wheel",
  "Warm vs Cool",
  "Neutrals First",
  "The Pop of Color",
  "Monochrome",
  "Complementary Pairs",
  "Analogous Flow",
  "The Skin Tone Match",
  "Black and White",
  "The Navy Alternative",
  "Earth Tones",
  "Pastels"
 ],
 "Color in Practice": [
  "Jewel Tones",
  "The Red Statement",
  "The Pink Spectrum",
  "The Green Family",
  "The Blue Mood",
  "Metallics",
  "The Print Mix",
  "The Color Seasons",
  "Spring Palette",
  "Summer Palette",
  "Autumn Palette",
  "Winter Palette",
  "The Orange Energy",
  "The Yellow Light",
  "The Purple Reign",
  "The Brown Ground",
  "The White Canvas",
  "The Gray Scale"
 ],
 "Color Mastery": [
  "The Color Confidence",
  "The Color Experiment",
  "The Color Legacy",
  "The Color Wheel Workout"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# color — "+safe+"\n"
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
    name:topic+' — color theory record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A color theory record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"color-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-color-theory-fashion-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('color-theory-fashion-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
