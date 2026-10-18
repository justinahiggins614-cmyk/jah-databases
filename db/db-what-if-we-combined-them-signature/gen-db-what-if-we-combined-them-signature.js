(function(){'use strict';
/* JAH The What If We Combined Them Signature Database generator — jahdb-db-what-if-we-combined-them-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WIWCTS-";
var FIELDS=["Tech Fusions","Everyday Fusions","Wild Fusions"];
var TOPICS={
 "Tech Fusions": [
  "Phone + Camera: The Smartphone (Signature Edition) - Tech Fusions",
  "Bike + Motor: The E-Bike (Signature Edition) - Tech Fusions",
  "Watch + Computer: The Smartwatch (Signature Edition) - Tech Fusions",
  "TV + Internet: Smart TV (Signature Edition) - Tech Fusions",
  "Camera + Drone: Aerial Photography (Signature Edition) - Tech Fusions",
  "Printer + Scanner: The All-in-One (Signature Edition) - Tech Fusions",
  "Flashlight + Phone: The Obvious (Signature Edition) - Tech Fusions",
  "Wallet + Phone: Mobile Pay (Signature Edition) - Tech Fusions",
  "Map + GPS: Navigation App (Signature Edition) - Tech Fusions",
  "Music + Player: Streaming (Signature Edition) - Tech Fusions"
 ],
 "Everyday Fusions": [
  "Library + Cafe: The Third Place (Signature Edition) - Everyday Fusions",
  "Gym + Social: Fitness Communities (Signature Edition) - Everyday Fusions",
  "School + Nature: Forest Schools (Signature Edition) - Everyday Fusions",
  "Office + Home: Hybrid Work (Signature Edition) - Everyday Fusions",
  "Farm + City: Urban Farming (Signature Edition) - Everyday Fusions",
  "Hotel + Home: Airbnb (Signature Edition) - Everyday Fusions",
  "Car + Share: Car Sharing (Signature Edition) - Everyday Fusions",
  "Restaurant + Farm: Farm-to-Table (Signature Edition) - Everyday Fusions",
  "Bookstore + Bar: Literary Nights (Signature Edition) - Everyday Fusions",
  "Museum + Playground: Kids Museums (Signature Edition) - Everyday Fusions"
 ],
 "Wild Fusions": [
  "Submarine + Airplane: The Dream (Signature Edition) - Wild Fusions",
  "Car + Plane: Flying Car (Again) (Signature Edition) - Wild Fusions",
  "Boat + Car: Amphibian (Signature Edition) - Wild Fusions",
  "Tent + Hammock: Hammock Tent (Signature Edition) - Wild Fusions",
  "Bike + Stroller: The Combo (Signature Edition) - Wild Fusions",
  "Desk + Bike: Pedal Desk (Signature Edition) - Wild Fusions",
  "Shower + Music: Waterproof Speaker (Signature Edition) - Wild Fusions",
  "Fridge + Screen: Smart Fridge (Signature Edition) - Wild Fusions",
  "Toilet + Bidet: Washlet (Signature Edition) - Wild Fusions",
  "Sofa + Bed: Sleeper Sofa (Signature Edition) - Wild Fusions",
  "Knife + Tools: Swiss Army (Signature Edition) - Wild Fusions",
  "Pen + Stylus: Digital Pen (Signature Edition) - Wild Fusions",
  "Glasses + Computer: Smart Glasses (Signature Edition) - Wild Fusions",
  "Drone + Delivery: Sky Drop (Signature Edition) - Wild Fusions"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# What If Combined Study — "+safe+"\n"
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
    name:topic+' — combination concept record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combination concept record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"what-if-combined-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-what-if-we-combined-them-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-what-if-we-combined-them-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
