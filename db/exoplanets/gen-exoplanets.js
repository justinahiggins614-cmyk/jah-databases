(function(){'use strict';
/* JAH Exoplanets Database generator — jahdb-exoplanets-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EXOP-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Exoplanets: An Overview", "51 Pegasi b: The First of Its Kind", "The Transit Method: Shadows of Distant Worlds", "Radial Velocity: Weighing Planets by Starlight", "Direct Imaging: Photographing Other Worlds", "Gravitational Microlensing: Planets as Lenses", "The Habitable Zone: Where Water Can Flow", "TRAPPIST-1: Seven Worlds Around a Cool Star", "Proxima Centauri b: Our Nearest Exoplanet Neighbor", "The Kepler Mission: A Census of Planets", "Naming Exoplanets: Letters from b"], "Compounded": ["Hot Jupiters: Roasters That Should Not Exist", "Super-Earths: The Most Common Planets", "Mini-Neptunes: Puffy Worlds Without Analogs", "Kepler-186f: The First Earth-Size Habitable-Zone World", "Kepler-452b: Earth's Older Cousin", "K2-18b: The Hycean Candidate", "55 Cancri e: The Lava World", "HD 209458 b (Osiris): The Evaporating Planet", "Reading Alien Air: Atmospheric Spectroscopy", "The Radius Valley: Where Super-Earths End", "TESS: The All-Sky Planet Hunter", "JWST and the Exoplanet Era"], "Advanced": ["5,000 Worlds and Counting: The Census", "Demographics: What the Numbers Say", "Transmission Spectroscopy in Depth", "Phase Curves: Mapping Alien Weather", "The Rossiter-McLaughlin Effect: Tilted Orbits", "Planetary Migration: Worlds on the Move", "Habitability Metrics: Ranking Candidates", "Free-Floating Planets: Worlds Without Suns", "CHEOPS: The Follow-Up Specialist", "Giant Telescopes: The Next Eyes", "What Comes Next: The Search for Life"]};
var KIND="exoplanet record";
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
var gen={version:"jahdb-exoplanets-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("exoplanets",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
