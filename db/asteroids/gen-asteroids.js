(function(){'use strict';
/* JAH Asteroids Database generator — jahdb-asteroids-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ASTR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Asteroids: An Overview", "The Main Belt: Between Mars and Jupiter", "Ceres: The Belt's Dwarf Planet", "Vesta: The Differentiated Protoplanet", "Pallas and Hygiea: The Other Giants", "Near-Earth Asteroids: Our Neighbors", "Jupiter's Trojans: The Captured Swarms", "The DART Mission: Moving an Asteroid", "OSIRIS-REx and Bennu: Seven Years, One Sample", "Hayabusa2 and Ryugu: Japan's Asteroid Triumph", "Spectral Classes: C, S, M and Beyond"], "Compounded": ["Eros: The First Asteroid Orbited", "Itokawa: The Rubble Pile Revealed", "Ida and Dactyl: The First Asteroid Moon", "Mathilde: The Gentle Giant Crater", "Gaspra: The First Close-Up", "Lutetia: The Rosetta Stone Flyby", "The Psyche Mission: A Metal World", "The Lucy Mission: Touring the Trojans", "Kirkwood Gaps: Jupiter's Resonant Broom", "The Yarkovsky Effect: Sunlight as a Thruster", "Rubble Piles: Flying Gravel Banks", "Binary Asteroids: Double Rocks"], "Advanced": ["Spectral Taxonomy: The Asteroid Zoo", "Asteroid Families: Collisional Clans", "Sizes and Masses: Weighing Rocks", "Impact Energy Math: How Bad Is It", "The Torino Scale: Rating the Threat", "Planetary Defense: The Watch", "Chelyabinsk 2013: The Wake-Up Call", "Meteorite Parent Bodies: Rocks with Return Addresses", "Resource Potential: Trillion-Dollar Rocks (Factual)", "Sky Surveys: Watching for Rocks", "Asteroids by the Numbers"]};
var KIND="asteroid record";
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
var gen={version:"jahdb-asteroids-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("asteroids",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
