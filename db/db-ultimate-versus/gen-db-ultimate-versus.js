(function(){'use strict';
/* JAH The Ultimate Versus Database generator — jahdb-db-ultimate-versus-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UV-";
var FIELDS=["Animal Showdowns","Machine Showdowns","Idea & Design Showdowns"];
var TOPICS={
 "Animal Showdowns": [
  "Cheetah vs Peregrine Falcon: Ultimate Speed - Animal Showdowns",
  "Blue Whale vs African Elephant: Heavyweight Giants - Animal Showdowns",
  "Mantis Shrimp vs Pistol Shrimp: Punch vs Blast - Animal Showdowns",
  "Tardigrade vs Cockroach: Survival Extremes - Animal Showdowns",
  "Honey Badger vs Wolverine: Fearless Showdown - Animal Showdowns",
  "Ant vs Human: Relative Strength - Animal Showdowns",
  "Bald Eagle vs Great Horned Owl: Raptor Duel - Animal Showdowns",
  "Great White Shark vs Saltwater Crocodile: Apex Clash - Animal Showdowns",
  "Octopus vs Cuttlefish: Masters of Disguise - Animal Showdowns",
  "Gray Wolf vs Lion: Pack vs Pride - Animal Showdowns",
  "Hummingbird vs Honeybee: Tiny Aviators - Animal Showdowns",
  "Giraffe vs Okapi: Long-Neck Lineage - Animal Showdowns"
 ],
 "Machine Showdowns": [
  "Saturn V vs Falcon Heavy: Moon Rocket vs Reusable Giant - Machine Showdowns",
  "Shinkansen vs Maglev: Rail Speed Kings - Machine Showdowns",
  "Formula 1 Car vs NASCAR Stock Car: Racing Philosophies - Machine Showdowns",
  "Quantum Computer vs Supercomputer: Computing Futures - Machine Showdowns",
  "Steam Engine vs Electric Motor: Power Revolutions - Machine Showdowns",
  "Printing Press vs Internet: Knowledge Explosions - Machine Showdowns",
  "Hoover Dam vs Solar Farm: Power Giants - Machine Showdowns",
  "Bicycle vs E-Bike: Human Power Plus - Machine Showdowns",
  "Abacus vs Calculator: Computing Roots - Machine Showdowns",
  "Hubble vs James Webb: Eyes on the Cosmos - Machine Showdowns",
  "Submarine vs Airplane: Domain Masters - Machine Showdowns"
 ],
 "Idea & Design Showdowns": [
  "Wheel vs Lever: Simple Machine Duel - Idea & Design Showdowns",
  "Zero vs Alphabet: Idea Showdown - Idea & Design Showdowns",
  "Map vs Compass: Navigation Aids - Idea & Design Showdowns",
  "Paper vs Screen: Reading Rivals - Idea & Design Showdowns",
  "Pen vs Keyboard: Writing Tools - Idea & Design Showdowns",
  "Nail vs Screw: Fastener Face-Off - Idea & Design Showdowns",
  "Mirror vs Lens: Light Shapers - Idea & Design Showdowns",
  "Plow vs Irrigation: Farming Foundations - Idea & Design Showdowns",
  "Calendar vs Clock: Time Tamers - Idea & Design Showdowns",
  "Rope vs Chain: Binding Rivals - Idea & Design Showdowns",
  "Trebuchet vs Cannon: Siege Engines - Idea & Design Showdowns"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Ultimate Versus Study — "+safe+"\n"
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
    name:topic+' — versus showdown record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A versus showdown record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ultimate-versus-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-ultimate-versus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-ultimate-versus',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
