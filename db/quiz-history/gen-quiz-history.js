(function(){'use strict';
/* JAH The History Quiz Database generator — jahdb-quiz-history-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZHI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Ancient Egypt Basics Quiz - Ancient History",
  "Ancient Greece Origins Quiz - Ancient History",
  "Roman Empire Foundations Quiz - Ancient History",
  "Mesopotamia First Civilizations Quiz - Ancient History",
  "Pharaohs and Pyramids Quiz - Ancient History",
  "Athens and Sparta Quiz - Ancient History",
  "Renaissance Quiz - Modern History"
 ],
 "Compounded": [
  "Roman Republic Quiz - Ancient History",
  "Early Middle Ages Quiz - Medieval History",
  "Vikings and Norse Voyages Quiz - Medieval History",
  "Age of Exploration Quiz - Modern History",
  "Ancient China Dynasties Quiz - Ancient History",
  "Persian Empire Quiz - Ancient History",
  "Byzantine Empire Quiz - Medieval History",
  "Reformation Quiz - Modern History",
  "Roman Emperors Quiz - Ancient History",
  "Crusades Quiz - Medieval History",
  "Feudalism in Medieval Europe Quiz - Medieval History",
  "American Revolution Quiz - Modern History",
  "Silk Road Quiz - World History"
 ],
 "Advanced": [
  "Mongol Empire Quiz - Medieval History",
  "Black Death Quiz - Medieval History",
  "French Revolution Quiz - Modern History",
  "Great Empires of the Americas Quiz - World History",
  "Hundred Years War Quiz - Medieval History",
  "Ottoman Rise Quiz - Medieval History",
  "Industrial Revolution Quiz - Modern History",
  "African Kingdoms Quiz - World History",
  "Late Medieval Culture Quiz - Medieval History",
  "World War I Quiz - Modern History",
  "World Revolutions Quiz - World History",
  "World War II Quiz - Modern History",
  "Cold War Quiz - Modern History",
  "Twentieth Century Milestones Quiz - World History"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Quiz — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"quiz-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-quiz-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-history',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
