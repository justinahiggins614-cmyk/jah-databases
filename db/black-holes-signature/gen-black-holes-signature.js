(function(){'use strict';
/* JAH Signature Black Holes Database generator — jahdb-black-holes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BLKHS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Horizon: The Signature Reading (Signature Edition)", "Singularity: The Signature Reading (Signature Edition)", "Hawking Radiation: The Signature Reading (Signature Edition)", "Spaghettification: The Signature Reading (Signature Edition)", "Cygnus X-1: The Signature Reading (Signature Edition)", "Supermassive Holes: The Signature Reading (Signature Edition)", "Sgr A*: The Signature Reading (Signature Edition)", "M87*: The Signature Reading (Signature Edition)", "The EHT: The Signature Reading (Signature Edition)", "Accretion: The Signature Reading (Signature Edition)", "Quasars: The Signature Reading (Signature Edition)"], "Compounded": ["Gravitational Waves: The Signature Reading (Signature Edition)", "GW150914: The Signature Reading (Signature Edition)", "Mergers: The Signature Reading (Signature Edition)", "Intermediate Masses: The Signature Reading (Signature Edition)", "Kerr Holes: The Signature Reading (Signature Edition)", "The Penrose Process: The Signature Reading (Signature Edition)", "Thermodynamics: The Signature Reading (Signature Edition)", "The Information Paradox: The Signature Reading (Signature Edition)", "Tidal Disruptions: The Signature Reading (Signature Edition)", "M-Sigma: The Signature Reading (Signature Edition)", "Primordial Holes: The Signature Reading (Signature Edition)", "Superradiance: The Signature Reading (Signature Edition)"], "Advanced": ["The Photon Sphere: The Signature Reading (Signature Edition)", "No-Hair: The Signature Reading (Signature Edition)", "The Firewall Debate: The Signature Reading (Signature Edition)", "LISA: The Signature Reading (Signature Edition)", "Shadows: The Signature Reading (Signature Edition)", "Jets: The Signature Reading (Signature Edition)", "The Information Ledger: The Signature Reading (Signature Edition)", "Why Black Holes Endure: The Signature Closing (Signature Edition)", "The Holographic Principle: The Signature Reading (Signature Edition)", "The Trench Solution: The Signature Tribute (Signature Edition)", "The Next Century: The Signature Forecast (Signature Edition)"]};
var KIND="black hole record";
var SRC="signature";
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
var gen={version:"jahdb-black-holes-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("black-holes-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
