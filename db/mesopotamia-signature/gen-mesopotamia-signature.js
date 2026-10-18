(function(){'use strict';
/* JAH Signature Mesopotamia Database generator — jahdb-mesopotamia-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MESOPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Mesopotamia: An Overview (Signature Edition)", "Sumer and the First Cities (Signature Edition)", "Cuneiform: The First Writing (Signature Edition)", "Uruk: The First Great City (Signature Edition)", "Ziggurats: Mountains of the Gods (Signature Edition)", "The Code of Hammurabi (Signature Edition)", "Sargon of Akkad: The First Empire (Signature Edition)", "Babylon: The Great City (Signature Edition)", "Assyria: The Empire of Iron (Signature Edition)", "Irrigation: Farming the Desert (Signature Edition)", "The Wheel and the Sail (Signature Edition)"], "Compounded": ["Ur of the Chaldees (Signature Edition)", "Lagash and Umma: The First Border War (Signature Edition)", "Ebla: The Archive City (Signature Edition)", "Mari: The Crossroads Kingdom (Signature Edition)", "The Epic of Gilgamesh (Signature Edition)", "The Sexagesimal System: Why 60? (Signature Edition)", "Mesopotamian Astronomy (Signature Edition)", "Mesopotamian Medicine (Signature Edition)", "Trade Networks of the Bronze Age (Signature Edition)", "Cylinder Seals: The First Signatures (Signature Edition)", "Scribal Schools: The First Education (Signature Edition)", "The Amarna Diplomacy (Signature Edition)"], "Advanced": ["The Neo-Babylonian Empire (Signature Edition)", "The Fall of Babylon to Persia (Signature Edition)", "Babylonian Mathematics (Signature Edition)", "Water Management and Canals (Signature Edition)", "The Library of Ashurbanipal (Signature Edition)", "Assyrian Siege Warfare (Signature Edition)", "The Hanging Gardens Debate (Signature Edition)", "Mesopotamian Religion and Gods (Signature Edition)", "Daily Life in Babylon (Signature Edition)", "The Kassites and the Middle Period (Signature Edition)", "Mesopotamia's Legacy: What We Kept (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — mesopotamia-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — mesopotamia record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mesopotamia record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mesopotamia-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-mesopotamia-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("mesopotamia-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
