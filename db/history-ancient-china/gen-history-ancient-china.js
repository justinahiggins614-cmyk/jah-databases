(function(){'use strict';
/* JAH Ancient China Database generator — "jahdb-history-ancient-china-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HCH-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Yellow River: Cradle of Civilization", "Xia, Shang, and Zhou: The First Dynasties", "Confucius and Confucianism", "Laozi, Zhuangzi, and Daoism", "The First Emperor and the Qin", "The Han Dynasty", "The Silk Road", "The Tang: Golden Age", "The Great Wall", "Chinese Writing and the Exams", "The Song: Invention and Commerce", "Zheng He and the Treasure Fleets"], "Compounded": ["Sun Tzu and the Art of War", "Legalism: The Philosophy of Power", "Buddhism's Conquest of China", "The Fall of Tang and the Song Reunification", "The Mongol Conquest and the Yuan", "The Ming Dynasty", "The Forbidden City", "The Civil Service Examinations", "Traditional Chinese Medicine", "Chinese Painting and Calligraphy", "The Opium Wars and the Taiping", "The Warring States Period"], "Advanced": ["The Terracotta Army", "Dunhuang: The Caves of a Thousand Buddhas", "The Grand Canal", "The Four Great Inventions", "Foot-Binding: Beauty and Control", "The Mandate of Heaven in Practice", "The Tribute System", "Chinese Gardens: Philosophy in Landscape", "The Boxer Rebellion", "Dictionaries and the Character Hoard"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-china demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-ancient-china-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-china",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
