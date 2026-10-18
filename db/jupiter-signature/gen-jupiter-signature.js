(function(){'use strict';
/* JAH Signature Jupiter Database generator — jahdb-jupiter-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JUPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Great Red Spot: The Signature Reading (Signature Edition)", "The Gas Giant: The Signature Reading (Signature Edition)", "Europa: The Signature Reading (Signature Edition)", "Io: The Signature Reading (Signature Edition)", "Ganymede: The Signature Reading (Signature Edition)", "Callisto: The Signature Reading (Signature Edition)", "The Giant's Magnetosphere: The Signature Reading (Signature Edition)", "Juno: The Signature Reading (Signature Edition)", "The Belts and Zones: The Signature Reading (Signature Edition)", "The Trojan Camps: The Signature Reading (Signature Edition)", "The Comet Catcher: The Signature Reading (Signature Edition)"], "Compounded": ["The Dilute Core: The Signature Reading (Signature Edition)", "The Winds' Depth: The Signature Reading (Signature Edition)", "The Polar Cyclones: The Signature Reading (Signature Edition)", "The Auroras: The Signature Reading (Signature Edition)", "The Irregular Moons: The Signature Reading (Signature Edition)", "The Ring: The Signature Reading (Signature Edition)", "The Formation: The Signature Reading (Signature Edition)", "The Migration: The Signature Reading (Signature Edition)", "The Water: The Signature Reading (Signature Edition)", "Jovian Lightning: The Signature Reading (Signature Edition)", "The 12-Year Orbit: The Signature Reading (Signature Edition)", "Giants Compared: The Signature Reading (Signature Edition)"], "Advanced": ["The Interior Structure: The Signature Reading (Signature Edition)", "The Metallic Hydrogen: The Signature Reading (Signature Edition)", "The Heat Excess: The Signature Reading (Signature Edition)", "The Helium Rain: The Signature Reading (Signature Edition)", "The Galilean Resonances: The Signature Reading (Signature Edition)", "Clipper and JUICE: The Signature Reading (Signature Edition)", "Four Centuries of Jupiter: The Signature Reading (Signature Edition)", "The Exoplanet Analog: The Signature Reading (Signature Edition)", "Saturn in the Sky: The Signature Reading (Signature Edition)", "Why Jupiter Endures: The Signature Closing (Signature Edition)", "The 11.86-Year Year: The Signature Note (Signature Edition)"]};
var KIND="jupiter record";
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
var gen={version:"jahdb-jupiter-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("jupiter-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
