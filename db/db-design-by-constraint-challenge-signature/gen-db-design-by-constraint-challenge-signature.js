(function(){'use strict';
/* JAH The Design by Constraint Challenge Signature Database generator — jahdb-db-design-by-constraint-challenge-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DSGCS-";
var FIELDS=["Space & Weight Limits","Time & Money Limits","Form Limits"];
var TOPICS={
 "Space & Weight Limits": [
  "Apollo 13 vs Planned Mission: Crisis Design (Signature Edition) - Space & Weight Limits",
  "Tiny House vs Mansion: Space Constraint (Signature Edition) - Space & Weight Limits",
  "CubeSat vs Flagship: Space Budget (Signature Edition) - Space & Weight Limits",
  "Haiku vs Novel: Word Constraint (Signature Edition) - Space & Weight Limits",
  "Twitter (140) vs Essay: Brevity (Signature Edition) - Space & Weight Limits",
  "One-Color vs Full Palette: Art (Signature Edition) - Space & Weight Limits",
  "Acoustic vs Electric: Music (Signature Edition) - Space & Weight Limits",
  "Black & White vs Color: Film (Signature Edition) - Space & Weight Limits",
  "Silent vs Talkie: Cinema (Signature Edition) - Space & Weight Limits",
  "Manual vs Auto: Photography (Signature Edition) - Space & Weight Limits",
  "Paper Map vs GPS: Navigation (Signature Edition) - Space & Weight Limits"
 ],
 "Time & Money Limits": [
  "Cash Only vs Cards: Budget (Signature Edition) - Time & Money Limits",
  "30-Day vs Big Budget: Film (Signature Edition) - Time & Money Limits",
  "Hackathon vs R&D Lab: Build Speed (Signature Edition) - Time & Money Limits",
  "Food Truck vs Restaurant: Startup (Signature Edition) - Time & Money Limits",
  "Garage vs Lab: Startup (Signature Edition) - Time & Money Limits",
  "One-Pan vs Full Kitchen: Cooking (Signature Edition) - Time & Money Limits",
  "Capsule vs Full Closet: Wardrobe (Signature Edition) - Time & Money Limits",
  "Sprint vs Marathon: Work (Signature Edition) - Time & Money Limits",
  "Deadline vs Open-Ended: Creativity (Signature Edition) - Time & Money Limits",
  "Shoestring vs Funded: Travel (Signature Edition) - Time & Money Limits"
 ],
 "Form Limits": [
  "Sonnet vs Free Verse: Poetry (Signature Edition) - Form Limits",
  "Three Chords vs Symphony: Music (Signature Edition) - Form Limits",
  "Dogme 95 vs Hollywood: Film (Signature Edition) - Form Limits",
  "Oulipo vs Free Writing: Literature (Signature Edition) - Form Limits",
  "Speedrun vs Casual: Gaming (Signature Edition) - Form Limits",
  "Ironman vs Casual: Triathlon (Signature Edition) - Form Limits",
  "Tiny Canvas vs Mural: Art (Signature Edition) - Form Limits",
  "One-Take vs Edited: Film (Signature Edition) - Form Limits",
  "A Cappella vs Full Band: Music (Signature Edition) - Form Limits",
  "Fixed Gear vs Geared: Cycling (Signature Edition) - Form Limits",
  "Noir vs Color: Comics (Signature Edition) - Form Limits",
  "Monochrome vs Color: Photography (Signature Edition) - Form Limits",
  "Unplugged vs Produced: Albums (Signature Edition) - Form Limits"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Constraint Design Study — "+safe+"\n"
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
    name:topic+' — constraint design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A constraint design record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"constraint-design-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-design-by-constraint-challenge-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-design-by-constraint-challenge-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
