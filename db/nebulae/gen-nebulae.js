(function(){'use strict';
/* JAH Nebulae Database generator — jahdb-nebulae-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NEB-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Nebulae: An Overview", "Emission Nebulae: Glowing Gas", "Reflection Nebulae: Blue by Starlight", "Dark Nebulae: Silhouettes in Space", "Planetary Nebulae: Dying Stars' Shrouds", "Supernova Remnants: Blast Waves", "The Orion Nebula: The Nearest Nursery", "The Pillars of Creation: Eroding Towers", "The Horsehead Nebula: The Iconic Silhouette", "The Ring Nebula: A Dying Star's Donut", "The Crab Nebula: A Supernova's Aftermath"], "Compounded": ["Star Formation: How Nebulae Make Stars", "H II Regions: Bubbles of Ionized Hydrogen", "The Carina Nebula: A Monster Nursery", "The Tarantula Nebula: The Local Giant", "The Lagoon Nebula: A Summer Showpiece", "The Trifid Nebula: Three in One", "The Rosette Nebula: A Floral Bubble", "The Dumbbell Nebula: The First Planetary Found", "The Cat's Eye Nebula: The Most Complex", "The Veil Nebula: A Supernova's Lace", "Bok Globules: Stars About to Be", "Herbig-Haro Objects: Newborn Stars' Jets"], "Advanced": ["Nebular Spectroscopy: Reading the Light", "Ionization Fronts: Where Light Meets Dark", "Photoevaporation: Boiling Away Nurseries", "Shaping Planetary Nebulae: The Binary Hypothesis", "Supernova Remnant Physics: The Sedov Phase", "Cosmic Dust: The Solid State of Space", "JWST's Nebulae: Infrared Revelations", "Nebula Catalogs: Messier to Sharpless", "Distances and Scales: How Big Is a Nebula", "Nebulae by the Numbers", "Why Nebulae Matter"]};
var KIND="nebula record";
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
var gen={version:"jahdb-nebulae-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("nebulae",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
