(function(){'use strict';
/* JAH The Most Surprising Result Signature Database generator — jahdb-db-most-surprising-result-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSRS-";
var FIELDS=["Accidental Discoveries","Failed Predictions","Counterintuitive Truths"];
var TOPICS={
 "Accidental Discoveries": [
  "Penicillin: The Mold That Healed (Signature Edition) - Accidental Discoveries",
  "Microwave: Melted Chocolate (Signature Edition) - Accidental Discoveries",
  "Post-its: Failed Glue (Signature Edition) - Accidental Discoveries",
  "X-Rays: Glowing Screen (Signature Edition) - Accidental Discoveries",
  "Teflon: Failed Refrigerant (Signature Edition) - Accidental Discoveries",
  "Vulcanization: Spilled Rubber (Signature Edition) - Accidental Discoveries",
  "Saccharin: Unwashed Hands (Signature Edition) - Accidental Discoveries",
  "Popsicle: Frozen Drink (Signature Edition) - Accidental Discoveries",
  "Champagne: Exploding Bottles (Signature Edition) - Accidental Discoveries",
  "Coca-Cola: Headache Tonic (Signature Edition) - Accidental Discoveries",
  "Quinine: Bitter Bark (Signature Edition) - Accidental Discoveries",
  "Insulin: Dog Pancreas (Signature Edition) - Accidental Discoveries"
 ],
 "Failed Predictions": [
  "Lord Kelvin: Heavier Than Air (Signature Edition) - Failed Predictions",
  "IBM: 5 Computers (Signature Edition) - Failed Predictions",
  "640K: Enough Memory (Signature Edition) - Failed Predictions",
  "Radio: No Future (Signature Edition) - Failed Predictions",
  "TV: 6 Months (Signature Edition) - Failed Predictions",
  "Internet: Fad (Signature Edition) - Failed Predictions",
  "iPhone: No Chance (Signature Edition) - Failed Predictions",
  "Horses: Permanent (Signature Edition) - Failed Predictions",
  "Paperless: 1975 (Signature Edition) - Failed Predictions",
  "Flying Cars: 2000 (Signature Edition) - Failed Predictions",
  "Cold Fusion: 1989 (Signature Edition) - Failed Predictions"
 ],
 "Counterintuitive Truths": [
  "Hot Water Freezes Faster: Mpemba (Signature Edition) - Counterintuitive Truths",
  "Bicycles: Stay Up Mystery (Signature Edition) - Counterintuitive Truths",
  "Bumblebees: Shouldn't Fly (Signature Edition) - Counterintuitive Truths",
  "Glass: Liquid Myth (Signature Edition) - Counterintuitive Truths",
  "Humans: 10% Brain Myth (Signature Edition) - Counterintuitive Truths",
  "Lightning: Strikes Twice (Signature Edition) - Counterintuitive Truths",
  "Goldfish: 3-Second Memory (Signature Edition) - Counterintuitive Truths",
  "Chameleons: Camouflage Myth (Signature Edition) - Counterintuitive Truths",
  "Deoxygenated Blood: Blue Myth (Signature Edition) - Counterintuitive Truths",
  "Hair/Nails: Grow After Death (Signature Edition) - Counterintuitive Truths",
  "Microwaves: Cook Inside-Out (Signature Edition) - Counterintuitive Truths"
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
var gen={version:'jahdb-db-most-surprising-result-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-most-surprising-result-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
