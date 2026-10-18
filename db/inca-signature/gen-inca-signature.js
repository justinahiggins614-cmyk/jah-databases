(function(){'use strict';
/* JAH Signature Inca Database generator — jahdb-inca-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INCAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Inca: An Overview (Signature Edition)", "Cusco: The Navel of the World (Signature Edition)", "Machu Picchu: The Inca Citadel (Signature Edition)", "Pachacuti: The Empire Builder (Signature Edition)", "The Quipu: Knots That Ruled (Signature Edition)", "Mit'a: The Labor Tax (Signature Edition)", "Terrace Agriculture (Signature Edition)", "Atahualpa and Cajamarca (Signature Edition)", "The Spanish Conquest (1532-1572) (Signature Edition)", "Quechua: The Living Language (Signature Edition)", "The Ayllu: Kinship and Land (Signature Edition)"], "Compounded": ["The Qhapaq Nan: The Royal Road (Signature Edition)", "Tambos: The Waystations (Signature Edition)", "The Sapa Inca: Divine Kingship (Signature Edition)", "Inti: The Sun God (Signature Edition)", "The Aclla: Chosen Women (Signature Edition)", "Chasqui Runners (Signature Edition)", "Inca Metallurgy: Gold and Silver (Signature Edition)", "Topa Inca: The Great Conqueror (Signature Edition)", "The Inca Civil War (Signature Edition)", "Vilcabamba: The Last Refuge (Signature Edition)", "The Conquest's Andean Allies (Signature Edition)", "Inca Justice (Signature Edition)"], "Advanced": ["Ashlar Masonry: Stones That Fit (Signature Edition)", "The Intihuatana and Inca Astronomy (Signature Edition)", "Chuno: Freeze-Dried Potatoes (Signature Edition)", "The Khipu Binary Debate (Signature Edition)", "Engineering the Vertical (Signature Edition)", "The Coricancha: Temple of the Sun (Signature Edition)", "Inca Art: Pottery and Textiles (Signature Edition)", "The Mita at Potosi (Signature Edition)", "Tupac Amaru II (Signature Edition)", "Quechua Continuity Today (Signature Edition)", "The Inca Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — inca-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — inca record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A inca record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"inca-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-inca-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("inca-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
