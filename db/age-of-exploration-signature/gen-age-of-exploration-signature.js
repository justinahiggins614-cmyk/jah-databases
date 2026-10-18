(function(){'use strict';
/* JAH Signature Age of Exploration Database generator — jahdb-age-of-exploration-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AGEEXS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Age of Exploration: An Overview (Signature Edition)", "Prince Henry the Navigator (Signature Edition)", "Columbus 1492 (Signature Edition)", "Vasco da Gama 1498 (Signature Edition)", "Magellan's Circumnavigation (Signature Edition)", "The Treaty of Tordesillas (Signature Edition)", "The Spanish Conquests (Signature Edition)", "The Portuguese Spice Trade (Signature Edition)", "The Caravel (Signature Edition)", "Navigation: Astrolabe and Quadrant (Signature Edition)", "The Columbian Exchange (Signature Edition)"], "Compounded": ["The Manila Galleons (Signature Edition)", "The Dutch East India Company (Signature Edition)", "Goa, Malacca, and Macau (Signature Edition)", "The Northwest Passage Attempts (Signature Edition)", "Cartography: The Cantino Planisphere (Signature Edition)", "Mercator's Projection (1569) (Signature Edition)", "The Consequences for Indigenous Peoples (Signature Edition)", "Joint-Stock Companies (Signature Edition)", "Scientific Navigation (Signature Edition)", "Proving the Globe (Signature Edition)", "The Age's Navigators (Signature Edition)", "The Search for El Dorado (Signature Edition)"], "Advanced": ["The Search for the Spice Islands (Signature Edition)", "The Pacific: The Spanish Lake (Signature Edition)", "Shipbuilding: Naos and Galleons (Signature Edition)", "The Casa de Contratacion (Signature Edition)", "Piracy and Privateering: Drake (Signature Edition)", "The Exchange's Crops in Detail (Signature Edition)", "Disease: The Great Dying (Signature Edition)", "The Encomienda System (Signature Edition)", "Bartolome de las Casas (Signature Edition)", "The Valladolid Debate (Signature Edition)", "The Age's End and Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — age-of-exploration-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — exploration record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A exploration record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"age-of-exploration-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-age-of-exploration-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("age-of-exploration-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
