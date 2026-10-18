(function(){'use strict';
/* JAH The Critical Thinking Arena Signature Database generator — jahdb-db-critical-thinking-arena-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRITHIARS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Bout: Everyone at the party loved the cake, so it must be th...",
  "Bout: It rained right after I washed my car, so washing my c...",
  "Bout: My grandfather smoked and lived to 90, so smoking is n...",
  "Bout: The new phone costs more, so it must be better...",
  "Bout: Nobody complained about the new rule, so everyone like...",
  "Bout: She is the boss's daughter, so she only got promoted b...",
  "Bout: The team lost after changing coaches, so the new coach...",
  "Bout: This medicine worked for my friend, so it will work fo...",
  "Bout: The article has a scary headline, so the danger must b...",
  "Bout: He was quiet in the meeting, so he must disagree...",
  "Bout: Organic food costs more, so it must be healthier..."
 ],
 "Compounded": [
  "Bout: Crime rose after the new mayor took office, so the may...",
  "Bout: The study was funded by the soda company, so its resul...",
  "Bout: Test scores fell when phones were allowed, so phones c...",
  "Bout: She predicted the upset, so she must have inside infor...",
  "Bout: The restaurant is always full, so the food must be gre...",
  "Bout: He has a degree from a famous school, so he must be ri...",
  "Bout: The poll says 60% agree, so the public agrees...",
  "Bout: Violent games rose with game sales, so games cause vio...",
  "Bout: The ancient text says it, so it must be true...",
  "Bout: Nobody has proven him wrong, so he must be right...",
  "Bout: The app has 5 stars, so it must be perfect...",
  "Bout: If we allow this small change, disaster will follow..."
 ],
 "Advanced": [
  "Bout: The regression shows X predicts Y, so X causes Y...",
  "Bout: The expert panel agreed unanimously, so the conclusion...",
  "Bout: The AI passed the test, so it understands the subject...",
  "Bout: After the policy, outcomes improved, so the policy wor...",
  "Bout: The p-value is 0.049, so the effect is real...",
  "Bout: Survivors all did X, so X saves lives...",
  "Bout: The model fit the past perfectly, so it predicts the f...",
  "Bout: Both sides have experts, so the truth must be in the m...",
  "Bout: The anecdote is vivid, so it must be representative...",
  "Bout: We must act now, so deliberation is cowardice...",
  "Bout: The system is complex, so no one can judge it..."
 ]
};
var DEMOKIND="reasoning-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Critical Thinking Study — "+safe+"\n"
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
    name:topic+' — thinking bout record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A thinking bout record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-critical-thinking-arena-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-critical-thinking-arena-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
