(function(){'use strict';
/* JAH Ottoman Empire Database generator — "jahdb-history-ottoman-empire-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HOT-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Osman and the Frontier Beylik", "Mehmed II and the Fall of Constantinople", "Suleiman the Magnificent", "The Sultan and the Imperial Divan", "The Janissaries", "The Millet System", "Istanbul: The Imperial Capital", "Sinan and Ottoman Architecture", "Trade and the Treasury", "The Harem and the Sultanate of Women", "The Empire at Its Height", "The Timar System"], "Compounded": ["Selim the Grim", "The Siege of Vienna (1529)", "Lepanto (1571)", "The Second Siege of Vienna (1683)", "The Tulip Era", "The Sick Man of Europe", "The Tanzimat Reforms", "Abdulhamid II", "The Young Turks and World War I", "Ataturk and the Turkish Republic", "The Conquest of the Mamluks (1516–17)", "Barbarossa Hayreddin Pasha"], "Advanced": ["The Devshirme System", "Ottoman Art: Calligraphy, Miniatures, Tiles", "Coffee and the Coffeehouse", "The Ottoman Navy and the Corsairs", "The Caliphate and the Hajj", "Ottoman Cuisine", "The Armenian Tragedy of 1915", "Gallipoli (1915)", "The Ottoman Legacy", "The Palace School and the Eunuchs"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ottoman-empire demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-ottoman-empire-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ottoman-empire",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
