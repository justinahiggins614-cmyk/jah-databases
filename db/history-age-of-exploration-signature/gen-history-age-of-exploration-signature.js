(function(){'use strict';
/* JAH Signature Age of Exploration Database generator — "jahdb-history-age-of-exploration-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HAXS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Age of Exploration: An Overview (Signature Edition)", "Prince Henry the Navigator (Signature Edition)", "The Caravel and the Technology (Signature Edition)", "Dias Rounds the Cape (1488) (Signature Edition)", "Columbus and 1492 (Signature Edition)", "Da Gama Reaches India (1498) (Signature Edition)", "Magellan's Circumnavigation (Signature Edition)", "The Treaty of Tordesillas (1494) (Signature Edition)", "Cortes and the Aztecs (Signature Edition)", "Pizarro and the Incas (Signature Edition)", "The Columbian Exchange (Signature Edition)", "Portugal's Asian Empire (Signature Edition)"], "Compounded": ["Silver: Potosi and the Treasure Fleets (Signature Edition)", "The Encomienda and Las Casas (Signature Edition)", "The Transatlantic Slave Trade (Signature Edition)", "Drake and the Sea Dogs (Signature Edition)", "The Dutch Commercial Empire (Signature Edition)", "New France (Signature Edition)", "The Manila Galleons (Signature Edition)", "Missionaries: Xavier and Ricci (Signature Edition)", "Maps and Mapmakers (Signature Edition)", "The Great Dying: Disease (Signature Edition)", "The End of the Age (Signature Edition)", "The Spanish Main: The Caribbean World (Signature Edition)"], "Advanced": ["Ships: From Caravel to Galleon (Signature Edition)", "Navigation: The Longitude Problem (Signature Edition)", "Women of the Age (Signature Edition)", "Food: The Columbian Menu (Signature Edition)", "The Failures: Roanoke and Darien (Signature Edition)", "Art of the Expansion (Signature Edition)", "Science of the New Worlds (Signature Edition)", "The Legacy: The World the Age Made (Signature Edition)", "The Crews Below Deck (Signature Edition)", "Pirates and Privateers (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-age-of-exploration-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original history record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original history record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-history-age-of-exploration-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-age-of-exploration-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
