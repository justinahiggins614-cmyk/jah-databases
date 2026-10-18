(function(){'use strict';
/* JAH Signature Nebulae Database generator — jahdb-nebulae-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NEBS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Orion Nebula: The Signature Reading (Signature Edition)", "The Pillars of Creation: The Signature Reading (Signature Edition)", "Emission vs. Darkness: The Signature Reading (Signature Edition)", "The Horsehead: The Signature Reading (Signature Edition)", "Planetary Nebulae: The Signature Reading (Signature Edition)", "The Ring Nebula: The Signature Reading (Signature Edition)", "The Crab: The Signature Reading (Signature Edition)", "Star Formation: The Signature Reading (Signature Edition)", "The Tarantula: The Signature Reading (Signature Edition)", "Dark Nebulae: The Signature Reading (Signature Edition)", "The Veil: The Signature Reading (Signature Edition)"], "Compounded": ["H II Regions: The Signature Reading (Signature Edition)", "The Carina Nebula: The Signature Reading (Signature Edition)", "Bok Globules: The Signature Reading (Signature Edition)", "Herbig-Haro Objects: The Signature Reading (Signature Edition)", "The Lagoon: The Signature Reading (Signature Edition)", "The Trifid: The Signature Reading (Signature Edition)", "The Rosette: The Signature Reading (Signature Edition)", "The Dumbbell: The Signature Reading (Signature Edition)", "The Cat's Eye: The Signature Reading (Signature Edition)", "Spectroscopy: The Signature Reading (Signature Edition)", "Dust: The Signature Reading (Signature Edition)", "The Helix: The Signature Reading (Signature Edition)"], "Advanced": ["Ionization Fronts: The Signature Reading (Signature Edition)", "Photoevaporation: The Signature Reading (Signature Edition)", "Shaping Planetaries: The Signature Reading (Signature Edition)", "Sedov Physics: The Signature Reading (Signature Edition)", "JWST's Nebulae: The Signature Reading (Signature Edition)", "Catalogs: The Signature Reading (Signature Edition)", "Scales: The Signature Reading (Signature Edition)", "The Ecosystem: The Signature Reading (Signature Edition)", "Why Nebulae Endure: The Signature Closing (Signature Edition)", "The Infrared Dark: The Signature Note (Signature Edition)", "The Palette: The Signature Note (Signature Edition)"]};
var KIND="nebula record";
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
var gen={version:"jahdb-nebulae-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("nebulae-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
