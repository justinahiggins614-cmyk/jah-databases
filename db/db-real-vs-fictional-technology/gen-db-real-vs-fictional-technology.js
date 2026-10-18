(function(){'use strict';
/* JAH The Real vs. Fictional Technology Database generator — jahdb-db-real-vs-fictional-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RVFT-";
var FIELDS=["Fiction Meets Reality","Almost Here","Still Impossible"];
var TOPICS={
 "Fiction Meets Reality": [
  "Lightsaber vs Plasma Cutter: Energy Blades - Fiction Meets Reality",
  "Tricorder vs Smartphone: Handheld Scanners - Fiction Meets Reality",
  "Hoverboard vs Maglev: Floating Transport - Fiction Meets Reality",
  "Replicator vs 3D Printer: Making Anything - Fiction Meets Reality",
  "Holodeck vs VR Headset: Immersion - Fiction Meets Reality",
  "Universal Translator vs Translation App: Babel - Fiction Meets Reality",
  "Phaser vs Laser Weapon: Directed Energy - Fiction Meets Reality",
  "Force Field vs Armor: Protection - Fiction Meets Reality",
  "Teleportation vs Airplane: Travel - Fiction Meets Reality",
  "Time Machine vs History Book: Past Access - Fiction Meets Reality",
  "AI Assistant vs Human Butler: Service - Fiction Meets Reality",
  "Flying Car vs Helicopter: Sky Commute - Fiction Meets Reality"
 ],
 "Almost Here": [
  "Invisibility Cloak vs Camouflage: Unseen - Almost Here",
  "Exoskeleton (Fiction) vs Exoskeleton (Real): Power Suits - Almost Here",
  "Mind Reading vs Brain-Computer Interface: Thoughts - Almost Here",
  "Weather Control vs Cloud Seeding: Sky Power - Almost Here",
  "Android vs Humanoid Robot: Artificial People - Almost Here",
  "Food Replicator vs Lab-Grown Meat: Future Food - Almost Here",
  "Jetpack vs Jet Suit: Personal Flight - Almost Here",
  "Submarine Car vs Amphibious Vehicle: Double Duty - Almost Here",
  "Shrink Ray vs Nanotechnology: Small Tech - Almost Here"
 ],
 "Still Impossible": [
  "Perpetual Motion vs Fusion: Free Energy Dreams - Still Impossible",
  "Death Ray vs Particle Beam: Sci-Fi Weapons - Still Impossible",
  "Parallel Universe Portal vs Multiverse Theory: Many Worlds - Still Impossible",
  "Faster-Than-Light vs Alcubierre Drive: Speed Limits - Still Impossible",
  "Immortality Serum vs Life Extension: Forever - Still Impossible",
  "Gravity Gun vs Tractor Beam: Pull Things - Still Impossible",
  "Clone Army vs Cloned Sheep: Copies - Still Impossible",
  "Dyson Sphere vs Solar Farm: Star Power - Still Impossible",
  "Sentient AI vs Narrow AI: Machine Minds - Still Impossible",
  "Wormhole Travel vs Black Hole: Shortcuts - Still Impossible",
  "Freeze Ray vs Cryogenics: Cold Guns - Still Impossible",
  "Mind Upload vs Brain Scan: Digital Afterlife - Still Impossible",
  "Antimatter Bomb vs Nuclear Bomb: Ultimate Weapons - Still Impossible"
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
var gen={version:'jahdb-db-real-vs-fictional-technology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-real-vs-fictional-technology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
