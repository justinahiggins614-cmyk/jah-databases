(function(){'use strict';
/* JAH Age of Exploration Database generator — "jahdb-history-age-of-exploration-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HAX-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Age of Exploration: An Overview", "Prince Henry the Navigator", "The Caravel and the Technology", "Dias Rounds the Cape (1488)", "Columbus and 1492", "Da Gama Reaches India (1498)", "Magellan's Circumnavigation", "The Treaty of Tordesillas (1494)", "Cortes and the Aztecs", "Pizarro and the Incas", "The Columbian Exchange", "Portugal's Asian Empire"], "Compounded": ["Silver: Potosi and the Treasure Fleets", "The Encomienda and Las Casas", "The Transatlantic Slave Trade", "Drake and the Sea Dogs", "The Dutch Commercial Empire", "New France", "The Manila Galleons", "Missionaries: Xavier and Ricci", "Maps and Mapmakers", "The Great Dying: Disease", "The End of the Age", "The Spanish Main: The Caribbean World"], "Advanced": ["Ships: From Caravel to Galleon", "Navigation: The Longitude Problem", "Women of the Age", "Food: The Columbian Menu", "The Failures: Roanoke and Darien", "Art of the Expansion", "Science of the New Worlds", "The Legacy: The World the Age Made", "The Crews Below Deck", "Pirates and Privateers"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-age-of-exploration demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — history record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A history record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-history-age-of-exploration-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-age-of-exploration",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
