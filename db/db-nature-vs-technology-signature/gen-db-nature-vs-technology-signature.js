(function(){'use strict';
/* JAH The Nature vs. Technology Signature Database generator — jahdb-db-nature-vs-technology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NVTS-";
var FIELDS=["Materials & Structures","Motion & Flight","Sensing & Systems"];
var TOPICS={
 "Materials & Structures": [
  "Spider Silk vs Kevlar: Fiber Duel (Signature Edition) - Materials & Structures",
  "Abalone Shell vs Ceramic Armor: Armor Duel (Signature Edition) - Materials & Structures",
  "Wood vs Steel: Building Duel (Signature Edition) - Materials & Structures",
  "Lotus Leaf vs Non-Stick Coating: Clean Duel (Signature Edition) - Materials & Structures",
  "Gecko Feet vs Adhesive Tape: Stick Duel (Signature Edition) - Materials & Structures",
  "Bone vs Concrete: Structure Duel (Signature Edition) - Materials & Structures",
  "Termite Mound vs Air Conditioner: Cooling Duel (Signature Edition) - Materials & Structures"
 ],
 "Motion & Flight": [
  "Bird Wing vs Airplane Wing: Flight Duel (Signature Edition) - Motion & Flight",
  "Fish Fin vs Propeller: Swim Duel (Signature Edition) - Motion & Flight",
  "Cheetah Leg vs Robotic Leg: Run Duel (Signature Edition) - Motion & Flight",
  "Hummingbird vs Drone: Hover Duel (Signature Edition) - Motion & Flight",
  "Whale Fin vs Ship Rudder: Steer Duel (Signature Edition) - Motion & Flight",
  "Snake vs Robot Snake: Slither Duel (Signature Edition) - Motion & Flight",
  "Kangaroo vs Pogo Stick: Hop Duel (Signature Edition) - Motion & Flight"
 ],
 "Sensing & Systems": [
  "Eye vs Camera: Vision Duel (Signature Edition) - Sensing & Systems",
  "Nose vs E-Nose: Smell Duel (Signature Edition) - Sensing & Systems",
  "Echolocation vs Sonar: Sound Duel (Signature Edition) - Sensing & Systems",
  "Lateral Line vs Pressure Sensor: Feel Duel (Signature Edition) - Sensing & Systems",
  "Skin vs Touchscreen: Touch Duel (Signature Edition) - Sensing & Systems",
  "Immune System vs Antivirus: Defense Duel (Signature Edition) - Sensing & Systems",
  "Photosynthesis vs Solar Panel: Energy Duel (Signature Edition) - Sensing & Systems",
  "Brain vs Computer: Compute Duel (Signature Edition) - Sensing & Systems",
  "Ant Colony vs Internet: Network Duel (Signature Edition) - Sensing & Systems",
  "Heart vs Pump: Flow Duel (Signature Edition) - Sensing & Systems",
  "Seed vs USB: Storage Duel (Signature Edition) - Sensing & Systems",
  "Spider Web vs Safety Net: Catch Duel (Signature Edition) - Sensing & Systems",
  "Mimic Octopus vs Camouflage Suit: Hide Duel (Signature Edition) - Sensing & Systems",
  "Beaver Dam vs Concrete Dam: Build Duel (Signature Edition) - Sensing & Systems",
  "Honeycomb vs Engineered Panel: Structure Duel (Signature Edition) - Sensing & Systems",
  "Electric Eel vs Battery: Shock Duel (Signature Edition) - Sensing & Systems",
  "Firefly vs LED: Light Duel (Signature Edition) - Sensing & Systems",
  "Shark Skin vs Hull Coating: Drag Duel (Signature Edition) - Sensing & Systems",
  "Venus Flytrap vs Mousetrap: Trap Duel (Signature Edition) - Sensing & Systems",
  "Bird Nest vs Tent: Shelter Duel (Signature Edition) - Sensing & Systems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nature Vs Technology Study — "+safe+"\n"
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
    name:topic+' — nature-vs-technology comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nature-vs-technology comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nature-vs-technology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-nature-vs-technology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-nature-vs-technology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
