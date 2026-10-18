(function(){'use strict';
/* JAH The Unsolved History Signature Database generator — jahdb-unsolved-history-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USHIS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Fall of Rome: The Single Cause (Signature Edition) - Ancient",
  "The Lost Colony of Roanoke (Signature Edition) - Early Modern",
  "The Princes in the Tower (Signature Edition) - Medieval",
  "The Man in the Iron Mask (Signature Edition) - Early Modern",
  "Jack the Ripper: The Historical Verdict (Signature Edition) - Modern",
  "The Black Death: Which Pathogen (Signature Edition) - Medieval",
  "The Great Divergence: Why Europe (Signature Edition) - Early Modern",
  "What Happened to the Ninth Legion (Signature Edition) - Ancient",
  "The Tunguska Event: The Cause (Signature Edition) - Modern",
  "The Dancing Plague of 1518 (Signature Edition) - Early Modern",
  "The Lost Franklin Expedition: The Full Story (Signature Edition) - Modern"
 ],
 "Compounded": [
  "Who Betrayed Anne Frank (Signature Edition) - Modern",
  "The Fate of the Romanovs: The Full Account (Signature Edition) - Modern",
  "The Green Children of Woolpit (Signature Edition) - Medieval",
  "The South Sea Bubble: Why the Mania (Signature Edition) - Early Modern",
  "The Fall of Constantinople: Could It Have Held (Signature Edition) - Medieval",
  "The English Civil War: Was It Inevitable (Signature Edition) - Early Modern",
  "The French Revolution: Why the Terror (Signature Edition) - Modern",
  "The Haitian Revolution: Why It Succeeded Alone (Signature Edition) - Modern",
  "The Taiping Rebellion: The Deadliest Civil War (Signature Edition) - Modern",
  "The Scramble for Africa: The Timing (Signature Edition) - Modern",
  "The July Crisis: Who Decided for War (Signature Edition) - Modern",
  "The Origins of WWI: The Fischer Debate (Signature Edition) - Modern"
 ],
 "Advanced": [
  "The Fall of the Qing: Why 1911 (Signature Edition) - Modern",
  "The Russian Revolution: Inevitable or Contingent (Signature Edition) - Modern",
  "The Great Depression: The True Cause (Signature Edition) - Modern",
  "The Appeasement Puzzle (Signature Edition) - Modern",
  "The Cold War: Who Started It (Signature Edition) - Modern",
  "The Cuban Missile Crisis: How Close (Signature Edition) - Modern",
  "The Fall of the USSR: Why So Sudden (Signature Edition) - Modern",
  "The Rwandan Genocide: Could It Have Been Stopped (Signature Edition) - Modern",
  "The 2008 Crisis: The Root Cause (Signature Edition) - Modern",
  "The End of History Debate: The Verdict (Signature Edition) - Theory",
  "The Synthesis Problem: Can History Unify (Signature Edition) - Theory"
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
var gen={version:'jahdb-unsolved-history-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-history-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
