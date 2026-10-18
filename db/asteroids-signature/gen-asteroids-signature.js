(function(){'use strict';
/* JAH Signature Asteroids Database generator — jahdb-asteroids-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ASTRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Asteroid Belt: The Signature Reading (Signature Edition)", "Ceres, Belt Monarch: The Signature Reading (Signature Edition)", "Vesta: The Signature Reading (Signature Edition)", "Rubble Piles: The Signature Reading (Signature Edition)", "Near-Earth Asteroids: The Signature Reading (Signature Edition)", "Trojans: The Signature Reading (Signature Edition)", "Eros: The Signature Reading (Signature Edition)", "Itokawa: The Signature Reading (Signature Edition)", "Ryugu: The Signature Reading (Signature Edition)", "Bennu: The Signature Reading (Signature Edition)", "Psyche: The Signature Reading (Signature Edition)"], "Compounded": ["Ida and Dactyl: The Signature Reading (Signature Edition)", "The Kirkwood Gaps: The Signature Reading (Signature Edition)", "Pallas: The Signature Reading (Signature Edition)", "Hygiea: The Signature Reading (Signature Edition)", "Mathilde: The Signature Reading (Signature Edition)", "Gaspra: The Signature Reading (Signature Edition)", "Steins and Lutetia: The Signature Reading (Signature Edition)", "Toutatis: The Signature Reading (Signature Edition)", "Yarkovsky: The Signature Reading (Signature Edition)", "YORP: The Signature Reading (Signature Edition)", "The Spin Barrier: The Signature Reading (Signature Edition)", "Binaries: The Signature Reading (Signature Edition)"], "Advanced": ["Chelyabinsk: The Signature Reading (Signature Edition)", "Chicxulub: The Signature Reading (Signature Edition)", "Tunguska: The Signature Reading (Signature Edition)", "Meteorites: The Signature Reading (Signature Edition)", "Dawn: The Signature Reading (Signature Edition)", "DART: The Signature Reading (Signature Edition)", "Hera: The Signature Reading (Signature Edition)", "Asteroid Mining: The Signature Reading (Signature Edition)", "Deflection: The Signature Reading (Signature Edition)", "The Torino Scale: The Signature Reading (Signature Edition)", "Why Asteroids Endure: The Signature Closing (Signature Edition)"]};
var KIND="asteroid record";
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
var gen={version:"jahdb-asteroids-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("asteroids-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
