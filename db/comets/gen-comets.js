(function(){'use strict';
/* JAH Comets Database generator — jahdb-comets-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COM-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Comets: An Overview", "Anatomy of a Comet: Nucleus, Coma, Tails", "Halley's Comet: The Famous Visitor", "Hale-Bopp: The Great Comet of 1997", "Comet NEOWISE: The Comet of 2020", "Short-Period vs. Long-Period Comets", "The Oort Cloud: The Deep Reservoir", "The Kuiper Belt Source: Where Short-Period Comets Begin", "Rosetta and 67P: A Rendezvous with a Comet", "Deep Impact: Smashing Comet Tempel 1", "Ion Tails vs. Dust Tails: Two Tails, Two Forces"], "Compounded": ["Encke's Comet: The Frequent Flyer", "Tempel-Tuttle: Parent of the Leonids", "Swift-Tuttle: Parent of the Perseids", "Kreutz Sungrazers: Comets That Kiss the Sun", "2I/Borisov: The Interstellar Comet", "1I/'Oumuamua: The Strange Visitor", "Outgassing Physics: How Comets Turn On", "The Dirty Snowball: What Comets Are Made Of", "Nucleus Densities: Fluffier Than Snow", "The Water-Delivery Debate: Did Comets Fill Earth's Oceans?", "Stardust: Catching Comet Dust", "Giotto at Halley: The First Comet Close-Up"], "Advanced": ["Orbital Elements: A Comet's Fingerprint", "Computing a Comet's Period: Kepler's Law", "Non-Gravitational Forces: Jets That Push", "The Oort Spike: New Comets from the Deep", "Dynamically New Comets: First-Time Visitors", "Comet Showers: When Stars Shake the Cloud", "Disintegration Events: Comets That Fall Apart", "Spectroscopy of Comae: Tasting Comets", "Comet Interceptor: The Ambush Mission", "Comet Designations: Reading the Names", "Comets by the Numbers"]};
var KIND="comet record";
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
var gen={version:"jahdb-comets-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("comets",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
