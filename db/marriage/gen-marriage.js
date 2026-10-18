(function(){'use strict';
/* JAH The Marriage Database generator — jahdb-marriage-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MARR-";
var FIELDS=["Communication Foundations","Conflict Resolution","Money & Marriage","Intimacy & Romance","Parenting Together","Extended Family & In-Laws","Keeping Connection"];
var TOPICS={
 "Communication Foundations": [
  "Listening to Understand, Not to Reply - Communication Foundations",
  "I-Statements: Saying Hard Things Safely - Communication Foundations",
  "The Daily Check-In: 15 Minutes That Save Marriages - Communication Foundations",
  "Repair Attempts: Fixing Conversations Mid-Fight - Communication Foundations",
  "Appreciation: The 5-to-1 Ratio - Communication Foundations",
  "Dreams and Goals: Knowing Each Other's Inner World - Communication Foundations"
 ],
 "Conflict Resolution": [
  "The Four Horsemen: Conflict Patterns That Kill Marriages - Conflict Resolution",
  "Fighting Fair: Rules for Disagreements - Conflict Resolution",
  "Gentle Startup: Beginning Hard Conversations Well - Conflict Resolution",
  "Compromise: Finding the Third Option - Conflict Resolution",
  "Apologizing and Forgiving for Real - Conflict Resolution",
  "When to Get Counseling (and How to Choose) - Conflict Resolution"
 ],
 "Money & Marriage": [
  "The Money Talk: Values Before Budgets - Money & Marriage",
  "Joint, Separate, or Hybrid Accounts - Money & Marriage",
  "Budgeting as a Team - Money & Marriage",
  "Debt and Financial Secrets - Money & Marriage",
  "Saving for Shared Goals - Money & Marriage"
 ],
 "Intimacy & Romance": [
  "Keeping Romance Alive After the Honeymoon - Intimacy & Romance",
  "Physical Intimacy Through Life's Seasons - Intimacy & Romance",
  "Love Languages: Giving Love They Can Receive - Intimacy & Romance",
  "Reconnecting After Disconnection - Intimacy & Romance"
 ],
 "Parenting Together": [
  "United Front: Parenting as a Team - Parenting Together",
  "Dividing the Mental Load Fairly - Parenting Together",
  "Protecting Couple Time With Kids at Home - Parenting Together",
  "Discipline Differences: Getting Aligned - Parenting Together"
 ],
 "Extended Family & In-Laws": [
  "In-Law Boundaries That Preserve Peace - Extended Family & In-Laws",
  "Holiday Negotiation Without the War - Extended Family & In-Laws",
  "When Parents Need Care: The Sandwich Season - Extended Family & In-Laws",
  "Blending Families With Grace - Extended Family & In-Laws"
 ],
 "Keeping Connection": [
  "Rituals of Connection: The Small Things That Bind - Keeping Connection",
  "Growing Together, Not Apart - Keeping Connection",
  "Anniversaries and Milestones That Matter - Keeping Connection",
  "The Marriage Mission Statement - Keeping Connection",
  "Legacy: The Marriage You Leave Behind - Keeping Connection"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Marriage Study — "+safe+"\n"
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
    name:topic+' — marriage guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A marriage guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"marriage-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-marriage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('marriage',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
