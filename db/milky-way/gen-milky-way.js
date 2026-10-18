(function(){'use strict';
/* JAH Milky Way Database generator — jahdb-milky-way-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MW-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Milky Way: An Overview", "Spiral Structure: Arms of the Galaxy", "The Galactic Center: Downtown Milky Way", "Sagittarius A*: The Heart of the Galaxy", "The Galactic Disk: Where the Stars Live", "The Bulge and Bar: The Galaxy's Core", "The Halo: The Galaxy's Ancient Outskirts", "Globular Clusters: Ancient Star Cities", "The Local Group: Our Galactic Neighborhood", "Size and Mass: Weighing the Galaxy", "The Galactic Year: Our Cosmic Orbit"], "Compounded": ["The Orion Arm: Our Local Spur", "The Perseus Arm: The Outer Neighbor", "The Sagittarius Arm: The Inner Neighbor", "Star-Forming Regions: The Galaxy's Nurseries", "The Central Molecular Zone: Extreme Star Formation", "Fermi Bubbles: The Galaxy's Eruption Scars", "The Rotation Curve: Evidence for Dark Matter", "The Dark Matter Halo: The Invisible Majority", "Stellar Streams: Fossils of Cannibalism", "The Magellanic Clouds: Our Brightest Satellites", "Galactic Cannibalism: How Galaxies Grow", "Open Clusters: Young Star Families"], "Advanced": ["The Gaia Mission: A Billion-Star Census", "Galactic Archaeology: Reading Stellar Fossils", "The Galactic Bar: Structure and Motion", "Imaging Sgr A*: Our Own Event Horizon", "The Andromeda Collision: Our Galactic Future", "The Galactic Habitable Zone: Where Life Can Be", "The Warp: The Galaxy's Bent Edge", "Satellite Dwarfs: The Galaxy's Entourage", "Stellar Populations: I, II and III", "The Milky Way by the Numbers", "Why the Milky Way Matters"]};
var KIND="galactic record";
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
var gen={version:"jahdb-milky-way-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("milky-way",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
