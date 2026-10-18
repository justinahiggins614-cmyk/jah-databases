(function(){'use strict';
/* JAH The Tribology and Lubrication Database generator — jahdb-tribology-lubrication-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Tribology Is: Friction, Wear, Lubrication \u2014 Foundations",
  "Friction Laws: Amontons and Coulomb \u2014 Foundations",
  "Static vs Kinetic Friction \u2014 Foundations",
  "Wear: What It Is and Why It Matters \u2014 Foundations",
  "Lubrication Regimes: Boundary to Hydrodynamic \u2014 Foundations",
  "Viscosity: The Core Property \u2014 Foundations",
  "Surface Roughness: Peaks and Valleys \u2014 Foundations",
  "Contact Mechanics Basics \u2014 Foundations",
  "Lubricant Types: Oils and Greases \u2014 Foundations",
  "Additives: What They Do \u2014 Foundations",
  "The Stribeck Curve \u2014 Foundations",
  "Friction Measurement: Tribometers \u2014 Foundations"
 ],
 "Compounded": [
  "Hydrodynamic Lubrication \u2014 Compounded",
  "Elastohydrodynamic Lubrication (EHL) \u2014 Compounded",
  "Boundary Lubrication \u2014 Compounded",
  "Viscosity-Temperature Behavior \u2014 Compounded",
  "Wear Mechanisms: Adhesive \u2014 Compounded",
  "Wear Mechanisms: Abrasive \u2014 Compounded",
  "Wear Mechanisms: Fatigue and Fretting \u2014 Compounded",
  "Archard Wear Law \u2014 Compounded",
  "Journal Bearings \u2014 Compounded",
  "Rolling-Element Bearings and L10 Life \u2014 Compounded",
  "Gears: Sliding, Rolling, Scuffing \u2014 Compounded",
  "Seals: Keeping Lubricant In \u2014 Compounded"
 ],
 "Advanced": [
  "Film Thickness and Lambda Ratio \u2014 Advanced",
  "Oil Analysis: Reading the Debris \u2014 Advanced",
  "Grease Lubrication and Relubrication \u2014 Advanced",
  "Solid Lubricants and Coatings \u2014 Advanced",
  "Surface Engineering: Texturing and Treatments \u2014 Advanced",
  "Fretting and False Brinelling \u2014 Advanced",
  "Lubricant Degradation: Oxidation \u2014 Advanced",
  "Lifetime Prediction Models \u2014 Advanced",
  "Tribology Test Specimens: Printable Wear Coupons \u2014 Advanced",
  "Designing for Tribology: The Systems View \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tribology — "+safe+"\n"
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
    name:topic+' — tribology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tribology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tribology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-tribology-lubrication-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tribology-lubrication',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
