(function(){'use strict';
/* JAH Signature Exoplanets Database generator — jahdb-exoplanets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EXOPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Census Is Biased: The Signature Reading (Signature Edition)", "51 Pegasi b: The Signature Reading (Signature Edition)", "The Radius Valley: The Signature Reading (Signature Edition)", "Hot Jupiters: The Signature Reading (Signature Edition)", "TRAPPIST-1: The Signature Reading (Signature Edition)", "The Habitable Zone: The Signature Reading (Signature Edition)", "Proxima b: The Signature Reading (Signature Edition)", "Direct Imaging: The Signature Reading (Signature Edition)", "Microlensing: The Signature Reading (Signature Edition)", "K2-18b: The Signature Reading (Signature Edition)", "The Migration Paradigm: The Signature Reading (Signature Edition)"], "Compounded": ["Super-Earths: The Signature Reading (Signature Edition)", "Mini-Neptunes: The Signature Reading (Signature Edition)", "Kepler's Legacy: The Signature Reading (Signature Edition)", "TESS: The Signature Reading (Signature Edition)", "Transmission Spectroscopy: The Signature Reading (Signature Edition)", "Phase Curves: The Signature Reading (Signature Edition)", "The Rossiter-McLaughlin Effect: The Signature Reading (Signature Edition)", "Free-Floating Planets: The Signature Reading (Signature Edition)", "The Drake Equation: The Signature Reading (Signature Edition)", "CHEOPS: The Signature Reading (Signature Edition)", "Giant Telescopes: The Signature Reading (Signature Edition)", "The Compact Multis: The Signature Reading (Signature Edition)"], "Advanced": ["Occurrence Rates: The Signature Reading (Signature Edition)", "The Fermi Paradox: The Signature Reading (Signature Edition)", "Biosignatures: The Signature Reading (Signature Edition)", "The Habitable Worlds Observatory: The Signature Reading (Signature Edition)", "Technosignatures: The Signature Reading (Signature Edition)", "The Great Filter: The Signature Reading (Signature Edition)", "Earth 2.0: The Signature Reading (Signature Edition)", "The Long Search: The Signature Closing (Signature Edition)", "The Pale Blue Dot: The Signature Coda (Signature Edition)", "The Neptune Desert: The Signature Note (Signature Edition)", "The Ultra-Short Period: The Signature Note (Signature Edition)"]};
var KIND="exoplanet record";
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
var gen={version:"jahdb-exoplanets-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("exoplanets-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
