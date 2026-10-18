(function(){'use strict';
/* JAH The Unsolved History Database generator — jahdb-unsolved-history-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USHI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Fall of Rome: The Single Cause - Ancient",
  "The Lost Colony of Roanoke - Early Modern",
  "The Princes in the Tower - Medieval",
  "The Man in the Iron Mask - Early Modern",
  "Jack the Ripper: The Historical Verdict - Modern",
  "The Black Death: Which Pathogen - Medieval",
  "The Great Divergence: Why Europe - Early Modern",
  "What Happened to the Ninth Legion - Ancient",
  "The Tunguska Event: The Cause - Modern",
  "The Dancing Plague of 1518 - Early Modern",
  "The Lost Franklin Expedition: The Full Story - Modern"
 ],
 "Compounded": [
  "Who Betrayed Anne Frank - Modern",
  "The Fate of the Romanovs: The Full Account - Modern",
  "The Green Children of Woolpit - Medieval",
  "The South Sea Bubble: Why the Mania - Early Modern",
  "The Fall of Constantinople: Could It Have Held - Medieval",
  "The English Civil War: Was It Inevitable - Early Modern",
  "The French Revolution: Why the Terror - Modern",
  "The Haitian Revolution: Why It Succeeded Alone - Modern",
  "The Taiping Rebellion: The Deadliest Civil War - Modern",
  "The Scramble for Africa: The Timing - Modern",
  "The July Crisis: Who Decided for War - Modern",
  "The Origins of WWI: The Fischer Debate - Modern"
 ],
 "Advanced": [
  "The Fall of the Qing: Why 1911 - Modern",
  "The Russian Revolution: Inevitable or Contingent - Modern",
  "The Great Depression: The True Cause - Modern",
  "The Appeasement Puzzle - Modern",
  "The Cold War: Who Started It - Modern",
  "The Cuban Missile Crisis: How Close - Modern",
  "The Fall of the USSR: Why So Sudden - Modern",
  "The Rwandan Genocide: Could It Have Been Stopped - Modern",
  "The 2008 Crisis: The Root Cause - Modern",
  "The End of History Debate: The Verdict - Theory",
  "The Synthesis Problem: Can History Unify - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved History Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-history-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-history',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
