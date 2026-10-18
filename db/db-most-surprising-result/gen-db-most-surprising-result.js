(function(){'use strict';
/* JAH The Most Surprising Result Database generator — jahdb-db-most-surprising-result-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSR-";
var FIELDS=["Accidental Discoveries","Failed Predictions","Counterintuitive Truths"];
var TOPICS={
 "Accidental Discoveries": [
  "Penicillin: The Mold That Healed - Accidental Discoveries",
  "Microwave: Melted Chocolate - Accidental Discoveries",
  "Post-its: Failed Glue - Accidental Discoveries",
  "X-Rays: Glowing Screen - Accidental Discoveries",
  "Teflon: Failed Refrigerant - Accidental Discoveries",
  "Vulcanization: Spilled Rubber - Accidental Discoveries",
  "Saccharin: Unwashed Hands - Accidental Discoveries",
  "Popsicle: Frozen Drink - Accidental Discoveries",
  "Champagne: Exploding Bottles - Accidental Discoveries",
  "Coca-Cola: Headache Tonic - Accidental Discoveries",
  "Quinine: Bitter Bark - Accidental Discoveries",
  "Insulin: Dog Pancreas - Accidental Discoveries"
 ],
 "Failed Predictions": [
  "Lord Kelvin: Heavier Than Air - Failed Predictions",
  "IBM: 5 Computers - Failed Predictions",
  "640K: Enough Memory - Failed Predictions",
  "Radio: No Future - Failed Predictions",
  "TV: 6 Months - Failed Predictions",
  "Internet: Fad - Failed Predictions",
  "iPhone: No Chance - Failed Predictions",
  "Horses: Permanent - Failed Predictions",
  "Paperless: 1975 - Failed Predictions",
  "Flying Cars: 2000 - Failed Predictions",
  "Cold Fusion: 1989 - Failed Predictions"
 ],
 "Counterintuitive Truths": [
  "Hot Water Freezes Faster: Mpemba - Counterintuitive Truths",
  "Bicycles: Stay Up Mystery - Counterintuitive Truths",
  "Bumblebees: Shouldn't Fly - Counterintuitive Truths",
  "Glass: Liquid Myth - Counterintuitive Truths",
  "Humans: 10% Brain Myth - Counterintuitive Truths",
  "Lightning: Strikes Twice - Counterintuitive Truths",
  "Goldfish: 3-Second Memory - Counterintuitive Truths",
  "Chameleons: Camouflage Myth - Counterintuitive Truths",
  "Deoxygenated Blood: Blue Myth - Counterintuitive Truths",
  "Hair/Nails: Grow After Death - Counterintuitive Truths",
  "Microwaves: Cook Inside-Out - Counterintuitive Truths"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Surprising Result Study — "+safe+"\n"
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
    name:topic+' — surprise science record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A surprise science record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"surprising-result-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-most-surprising-result-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-most-surprising-result',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
