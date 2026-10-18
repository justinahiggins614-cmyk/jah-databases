(function(){'use strict';
/* JAH Black Holes Database generator — jahdb-black-holes-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BLKH-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Black Holes: An Overview", "The Event Horizon: The Point of No Return", "Stellar-Mass Black Holes: Collapsed Stars", "Cygnus X-1: The First Black Hole", "Supermassive Black Holes: Galactic Anchors", "Sagittarius A*: Our Galaxy's Black Hole", "M87*: The First Black Hole Ever Imaged", "The Event Horizon Telescope: An Earth-Size Camera", "The Singularity: Where Physics Breaks", "Spaghettification: Tidal Forces at the Edge", "Hawking Radiation: Black Holes Evaporate"], "Compounded": ["Stellar Collapse: How Black Holes Are Born", "X-Ray Binaries: Black Holes Caught Feeding", "Accretion Disks: The Brightest Engines", "Quasars and Active Galaxies: Feeding Giants", "Gravitational Waves: Ripples from Mergers", "GW150914: The Signal That Changed Astronomy", "Black Hole Mergers: The Growing Census", "Intermediate-Mass Black Holes: The Missing Link", "Kerr vs. Schwarzschild: Spinning Black Holes", "The Penrose Process: Stealing Spin Energy", "Black Hole Thermodynamics: Four Laws", "The Information Paradox: The Unsolved Problem"], "Advanced": ["Imaging M87*: How the First Picture Was Made", "Imaging Sgr A*: Our Own Shadow", "The Photon Sphere: Light in Orbit", "The No-Hair Theorem: Bald Black Holes", "Tidal Disruption Events: Stars Shredded", "The M-Sigma Relation: Holes and Galaxies Grow Together", "Primordial Black Holes: Holes from the Big Bang", "Superradiance: Black Holes as Particle Detectors", "LISA: Hearing Supermassive Mergers", "The Firewall Debate: Fire at the Horizon", "Why Black Holes Matter"]};
var KIND="black hole record";
var SRC="public-harvest";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={
    id:id,
    name:topic+' — '+KIND,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+KIND+' of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
  if(SRC==='signature')rec.signature_label='Signature original - created in the Signature system; not a public record.';
  return rec;
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
var gen={version:"jahdb-black-holes-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("black-holes",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
