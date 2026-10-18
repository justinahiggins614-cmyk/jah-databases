(function(){'use strict';
/* JAH Kuiper Belt Database generator — jahdb-kuiper-belt-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KB2-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Kuiper Belt: An Overview", "1992 QB1: The First Discovery", "Pluto's New Address: Heart of the Belt", "Classical KBOs: The Belt's Core", "Plutinos: In Step with Neptune", "The Scattered Disk: Neptune's Exiles", "Detached Objects: Beyond Neptune's Reach", "Arrokoth: The Snowman World", "Cold vs. Hot Classicals: Two Populations", "Size Distribution: Counting the Belt", "The Kuiper Cliff: The Edge at 50 AU"], "Compounded": ["The Haumea Family: An Impact's Children", "Quaoar: The Ringed Worldlet", "Orcus: The Anti-Pluto", "Ixion: The Dark Plutino", "Varuna: The Fast Spinner", "Chaos: The Well-Named Cubewano", "The Scattered Disk in Depth: Eris's Neighborhood", "Sedna and the Sednoids: The Inner Oort Cloud", "The Planet Nine Hypothesis: The Debate", "Binary KBOs: Doubles in the Deep", "Colors and Surfaces: Red Tholins", "Tholins: The Red Stuff"], "Advanced": ["The Nice Model: The Solar System Reshuffled", "The 50 AU Cliff: Reading the Edge", "The Missing-Mass Problem: Solved?", "Collisional Evolution: 4 Billion Years of Grinding", "New Horizons' Extended Mission: Exploring from Within", "The LSST Era: The Coming Census", "Naming KBOs: Creation Gods Only", "Resonant Dynamics: Neptune's Sheet Music", "The Belt by the Numbers", "Why the Kuiper Belt Matters", "Occultations: Weighing Shadows"]};
var KIND="Kuiper Belt record";
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
var gen={version:"jahdb-kuiper-belt-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("kuiper-belt",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
