(function(){'use strict';
/* JAH The Real vs. Fictional Technology Signature Database generator — jahdb-db-real-vs-fictional-technology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RVFTS-";
var FIELDS=["Fiction Meets Reality","Almost Here","Still Impossible"];
var TOPICS={
 "Fiction Meets Reality": [
  "Lightsaber vs Plasma Cutter: Energy Blades (Signature Edition) - Fiction Meets Reality",
  "Tricorder vs Smartphone: Handheld Scanners (Signature Edition) - Fiction Meets Reality",
  "Hoverboard vs Maglev: Floating Transport (Signature Edition) - Fiction Meets Reality",
  "Replicator vs 3D Printer: Making Anything (Signature Edition) - Fiction Meets Reality",
  "Holodeck vs VR Headset: Immersion (Signature Edition) - Fiction Meets Reality",
  "Universal Translator vs Translation App: Babel (Signature Edition) - Fiction Meets Reality",
  "Phaser vs Laser Weapon: Directed Energy (Signature Edition) - Fiction Meets Reality",
  "Force Field vs Armor: Protection (Signature Edition) - Fiction Meets Reality",
  "Teleportation vs Airplane: Travel (Signature Edition) - Fiction Meets Reality",
  "Time Machine vs History Book: Past Access (Signature Edition) - Fiction Meets Reality",
  "AI Assistant vs Human Butler: Service (Signature Edition) - Fiction Meets Reality",
  "Flying Car vs Helicopter: Sky Commute (Signature Edition) - Fiction Meets Reality"
 ],
 "Almost Here": [
  "Invisibility Cloak vs Camouflage: Unseen (Signature Edition) - Almost Here",
  "Exoskeleton (Fiction) vs Exoskeleton (Real): Power Suits (Signature Edition) - Almost Here",
  "Mind Reading vs Brain-Computer Interface: Thoughts (Signature Edition) - Almost Here",
  "Weather Control vs Cloud Seeding: Sky Power (Signature Edition) - Almost Here",
  "Android vs Humanoid Robot: Artificial People (Signature Edition) - Almost Here",
  "Food Replicator vs Lab-Grown Meat: Future Food (Signature Edition) - Almost Here",
  "Jetpack vs Jet Suit: Personal Flight (Signature Edition) - Almost Here",
  "Submarine Car vs Amphibious Vehicle: Double Duty (Signature Edition) - Almost Here",
  "Shrink Ray vs Nanotechnology: Small Tech (Signature Edition) - Almost Here"
 ],
 "Still Impossible": [
  "Perpetual Motion vs Fusion: Free Energy Dreams (Signature Edition) - Still Impossible",
  "Death Ray vs Particle Beam: Sci-Fi Weapons (Signature Edition) - Still Impossible",
  "Parallel Universe Portal vs Multiverse Theory: Many Worlds (Signature Edition) - Still Impossible",
  "Faster-Than-Light vs Alcubierre Drive: Speed Limits (Signature Edition) - Still Impossible",
  "Immortality Serum vs Life Extension: Forever (Signature Edition) - Still Impossible",
  "Gravity Gun vs Tractor Beam: Pull Things (Signature Edition) - Still Impossible",
  "Clone Army vs Cloned Sheep: Copies (Signature Edition) - Still Impossible",
  "Dyson Sphere vs Solar Farm: Star Power (Signature Edition) - Still Impossible",
  "Sentient AI vs Narrow AI: Machine Minds (Signature Edition) - Still Impossible",
  "Wormhole Travel vs Black Hole: Shortcuts (Signature Edition) - Still Impossible",
  "Freeze Ray vs Cryogenics: Cold Guns (Signature Edition) - Still Impossible",
  "Mind Upload vs Brain Scan: Digital Afterlife (Signature Edition) - Still Impossible",
  "Antimatter Bomb vs Nuclear Bomb: Ultimate Weapons (Signature Edition) - Still Impossible"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Real Vs Fictional Study — "+safe+"\n"
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
    name:topic+' — real-vs-fictional comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A real-vs-fictional comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"real-vs-fictional-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-real-vs-fictional-technology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-real-vs-fictional-technology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
