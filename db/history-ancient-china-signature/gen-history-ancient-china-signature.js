(function(){'use strict';
/* JAH Signature Ancient China Database generator — "jahdb-history-ancient-china-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HCHS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Yellow River: Cradle of Civilization (Signature Edition)", "Xia, Shang, and Zhou: The First Dynasties (Signature Edition)", "Confucius and Confucianism (Signature Edition)", "Laozi, Zhuangzi, and Daoism (Signature Edition)", "The First Emperor and the Qin (Signature Edition)", "The Han Dynasty (Signature Edition)", "The Silk Road (Signature Edition)", "The Tang: Golden Age (Signature Edition)", "The Great Wall (Signature Edition)", "Chinese Writing and the Exams (Signature Edition)", "The Song: Invention and Commerce (Signature Edition)", "Zheng He and the Treasure Fleets (Signature Edition)"], "Compounded": ["Sun Tzu and the Art of War (Signature Edition)", "Legalism: The Philosophy of Power (Signature Edition)", "Buddhism's Conquest of China (Signature Edition)", "The Fall of Tang and the Song Reunification (Signature Edition)", "The Mongol Conquest and the Yuan (Signature Edition)", "The Ming Dynasty (Signature Edition)", "The Forbidden City (Signature Edition)", "The Civil Service Examinations (Signature Edition)", "Traditional Chinese Medicine (Signature Edition)", "Chinese Painting and Calligraphy (Signature Edition)", "The Opium Wars and the Taiping (Signature Edition)", "The Warring States Period (Signature Edition)"], "Advanced": ["The Terracotta Army (Signature Edition)", "Dunhuang: The Caves of a Thousand Buddhas (Signature Edition)", "The Grand Canal (Signature Edition)", "The Four Great Inventions (Signature Edition)", "Foot-Binding: Beauty and Control (Signature Edition)", "The Mandate of Heaven in Practice (Signature Edition)", "The Tribute System (Signature Edition)", "Chinese Gardens: Philosophy in Landscape (Signature Edition)", "The Boxer Rebellion (Signature Edition)", "Dictionaries and the Character Hoard (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-china-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-ancient-china-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-china-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
