(function(){'use strict';
/* JAH The Strongest Things Signature Database generator — jahdb-db-strongest-things-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STTS-";
var FIELDS=["Strength Foundations","Might of Nature","Engineered Might"];
var TOPICS={
 "Strength Foundations": [
  "Ant vs Elephant: Relative vs Absolute (Signature Edition) - Strength Foundations",
  "Gorilla vs Grizzly Bear: Primate vs Predator (Signature Edition) - Strength Foundations",
  "Spider Silk vs Steel: Fiber vs Metal (Signature Edition) - Strength Foundations",
  "Diamond vs Graphene: Carbon Champions (Signature Edition) - Strength Foundations",
  "Titanium vs Steel: Metal Duel (Signature Edition) - Strength Foundations",
  "Oak vs Bamboo: Wood Strength (Signature Edition) - Strength Foundations",
  "Hydraulic Press vs Car Crusher: Machine Muscle (Signature Edition) - Strength Foundations",
  "Crane vs Forklift: Lifting Styles (Signature Edition) - Strength Foundations",
  "Tugboat vs Cargo Ship: Pulling Power (Signature Edition) - Strength Foundations",
  "Python vs Anaconda: Constriction (Signature Edition) - Strength Foundations",
  "Eagle Talon vs Crocodile Jaw: Grip vs Bite (Signature Edition) - Strength Foundations",
  "Mantis Shrimp Punch vs Bullet: Impact (Signature Edition) - Strength Foundations"
 ],
 "Might of Nature": [
  "Lion vs Tiger: Big Cat Power (Signature Edition) - Might of Nature",
  "Hippo vs Rhino: Armored Tanks (Signature Edition) - Might of Nature",
  "Wolverine vs Honey Badger: Pound for Pound (Signature Edition) - Might of Nature",
  "Orca vs Great White: Ocean Hunters (Signature Edition) - Might of Nature",
  "Elephant Seal vs Walrus: Beach Brawlers (Signature Edition) - Might of Nature",
  "Grizzly vs Polar Bear: Bear Kings (Signature Edition) - Might of Nature",
  "Tornado vs Hurricane: Wind Fury (Signature Edition) - Might of Nature",
  "Volcano vs Earthquake: Earth Power (Signature Edition) - Might of Nature",
  "Lightning vs Power Plant: Electric Might (Signature Edition) - Might of Nature",
  "Waterfall vs Dam Release: Water Force (Signature Edition) - Might of Nature"
 ],
 "Engineered Might": [
  "Excavator vs Bulldozer: Earth Movers (Signature Edition) - Engineered Might",
  "Rocket Engine vs Jet Engine: Thrust (Signature Edition) - Engineered Might",
  "Diamond Saw vs Waterjet: Cutting Power (Signature Edition) - Engineered Might",
  "Pile Driver vs Jackhammer: Impact Machines (Signature Edition) - Engineered Might",
  "Industrial Robot vs Human Arm: Precision Strength (Signature Edition) - Engineered Might",
  "Bridge Cable vs Rope: Tension Champions (Signature Edition) - Engineered Might",
  "Locomotive vs Truck: Hauling (Signature Edition) - Engineered Might",
  "Dam vs Levee: Water Holders (Signature Edition) - Engineered Might",
  "Skyscraper vs Pyramid: Standing Strong (Signature Edition) - Engineered Might",
  "Aircraft Carrier vs Icebreaker: Hull Strength (Signature Edition) - Engineered Might",
  "Saturn V vs Nimitz: Power Plants (Signature Edition) - Engineered Might",
  "Human vs Chimp: Pound-for-Pound (Signature Edition) - Engineered Might"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Strongest Things Study — "+safe+"\n"
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
    name:topic+' — strength comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A strength comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"strongest-things-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-strongest-things-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-strongest-things-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
