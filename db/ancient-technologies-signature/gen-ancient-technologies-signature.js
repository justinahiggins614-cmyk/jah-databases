(function(){'use strict';
/* JAH Signature Ancient Technologies Database generator — jahdb-ancient-technologies-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ANCTECS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Ancient Technologies: An Overview (Signature Edition)", "The Lever and the Pulley (Signature Edition)", "The Wheel (Signature Edition)", "Bronze Metallurgy (Signature Edition)", "Iron Metallurgy (Signature Edition)", "The Arch (Signature Edition)", "Roman Concrete (Signature Edition)", "The Water Clock (Signature Edition)", "The Sundial (Signature Edition)", "Papermaking (Cai Lun) (Signature Edition)", "The Compass (Signature Edition)"], "Compounded": ["Gunpowder (Signature Edition)", "The Printing Press (Predecessors) (Signature Edition)", "The Aqueduct (Signature Edition)", "The Water Mill (Signature Edition)", "The Windmill (Signature Edition)", "The Crane (Signature Edition)", "The Screw (Archimedes') (Signature Edition)", "The Odometer (Signature Edition)", "The Seismoscope (Zhang Heng) (Signature Edition)", "The Steam Aeolipile (Hero) (Signature Edition)", "The Mechanical Clock (Su Song) (Signature Edition)", "The Astrolabe (Signature Edition)"], "Advanced": ["The Antikythera Mechanism (Deep Dive) (Signature Edition)", "The Baghdad Battery: The Parthian Jar (Signature Edition)", "Damascus Steel (Signature Edition)", "Greek Fire: Byzantium's Secret Weapon (Signature Edition)", "The Silk Loom (Signature Edition)", "The Qanat System (Signature Edition)", "The Inca Quipu (Signature Edition)", "The Mesoamerican Calendar (Signature Edition)", "The Polynesian Navigation (Signature Edition)", "The Lost Technologies (Signature Edition)", "The Technology's Method (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — ancient-technologies-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
  return {
    id:id,
    name:topic+' — ancient technology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A ancient technology record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ancient-technologies-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
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
var gen={version:"jahdb-ancient-technologies-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ancient-technologies-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
