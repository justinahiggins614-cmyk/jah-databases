(function(){'use strict';
/* JAH Signature Neptune Database generator — jahdb-neptune-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NEPTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Found by Math: The Signature Reading (Signature Edition)", "The Supersonic Winds: The Signature Reading (Signature Edition)", "Triton the Captive: The Signature Reading (Signature Edition)", "The Dark Spots: The Signature Reading (Signature Edition)", "The Deep Blue: The Signature Reading (Signature Edition)", "Voyager 2: The Signature Reading (Signature Edition)", "The Ring Arcs: The Signature Reading (Signature Edition)", "The Interior Heat: The Signature Reading (Signature Edition)", "The Small Moons: The Signature Reading (Signature Edition)", "The 165-Year Year: The Signature Reading (Signature Edition)", "The Farthest: The Signature Reading (Signature Edition)"], "Compounded": ["The Atmosphere's Layers: The Signature Reading (Signature Edition)", "The Methane's Depth: The Signature Reading (Signature Edition)", "The Jet Streams: The Signature Reading (Signature Edition)", "Triton's Geysers: The Signature Reading (Signature Edition)", "Triton's Capture: The Signature Reading (Signature Edition)", "The Adams Arcs: The Signature Reading (Signature Edition)", "The Windy Interior: The Signature Reading (Signature Edition)", "The Magnetic Tilt: The Signature Reading (Signature Edition)", "The 2011 Orbit: The Signature Reading (Signature Edition)", "The Neptune Orbiter: The Signature Reading (Signature Edition)", "Neptune in the Sky: The Signature Reading (Signature Edition)", "The Twin Giants: The Signature Reading (Signature Edition)"], "Advanced": ["Birth at 30 AU: The Signature Reading (Signature Edition)", "The Migration's Role: The Signature Reading (Signature Edition)", "The Dark Spot's Physics: The Signature Reading (Signature Edition)", "The Scooter: The Signature Reading (Signature Edition)", "The Stratosphere: The Signature Reading (Signature Edition)", "The Triton Plumes' Future: The Signature Reading (Signature Edition)", "The Discovery Controversy: The Signature Reading (Signature Edition)", "The Nomenclature: The Signature Reading (Signature Edition)", "The Long Night: The Signature Reading (Signature Edition)", "Why Neptune Endures: The Signature Closing (Signature Edition)", "The 164.8-Year Year: The Signature Note (Signature Edition)"]};
var KIND="neptune record";
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
var gen={version:"jahdb-neptune-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("neptune-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
