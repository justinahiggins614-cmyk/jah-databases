(function(){'use strict';
/* JAH The Marriage Signature Database generator — jahdb-marriage-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MARRS-";
var FIELDS=["Communication Foundations","Conflict Resolution","Money & Marriage","Intimacy & Romance","Parenting Together","Extended Family & In-Laws","Keeping Connection"];
var TOPICS={
 "Communication Foundations": [
  "Listening to Understand, Not to Reply (Signature Edition) - Communication Foundations",
  "I-Statements: Saying Hard Things Safely (Signature Edition) - Communication Foundations",
  "The Daily Check-In: 15 Minutes That Save Marriages (Signature Edition) - Communication Foundations",
  "Repair Attempts: Fixing Conversations Mid-Fight (Signature Edition) - Communication Foundations",
  "Appreciation: The 5-to-1 Ratio (Signature Edition) - Communication Foundations",
  "Dreams and Goals: Knowing Each Other's Inner World (Signature Edition) - Communication Foundations"
 ],
 "Conflict Resolution": [
  "The Four Horsemen: Conflict Patterns That Kill Marriages (Signature Edition) - Conflict Resolution",
  "Fighting Fair: Rules for Disagreements (Signature Edition) - Conflict Resolution",
  "Gentle Startup: Beginning Hard Conversations Well (Signature Edition) - Conflict Resolution",
  "Compromise: Finding the Third Option (Signature Edition) - Conflict Resolution",
  "Apologizing and Forgiving for Real (Signature Edition) - Conflict Resolution",
  "When to Get Counseling (and How to Choose) (Signature Edition) - Conflict Resolution"
 ],
 "Money & Marriage": [
  "The Money Talk: Values Before Budgets (Signature Edition) - Money & Marriage",
  "Joint, Separate, or Hybrid Accounts (Signature Edition) - Money & Marriage",
  "Budgeting as a Team (Signature Edition) - Money & Marriage",
  "Debt and Financial Secrets (Signature Edition) - Money & Marriage",
  "Saving for Shared Goals (Signature Edition) - Money & Marriage"
 ],
 "Intimacy & Romance": [
  "Keeping Romance Alive After the Honeymoon (Signature Edition) - Intimacy & Romance",
  "Physical Intimacy Through Life's Seasons (Signature Edition) - Intimacy & Romance",
  "Love Languages: Giving Love They Can Receive (Signature Edition) - Intimacy & Romance",
  "Reconnecting After Disconnection (Signature Edition) - Intimacy & Romance"
 ],
 "Parenting Together": [
  "United Front: Parenting as a Team (Signature Edition) - Parenting Together",
  "Dividing the Mental Load Fairly (Signature Edition) - Parenting Together",
  "Protecting Couple Time With Kids at Home (Signature Edition) - Parenting Together",
  "Discipline Differences: Getting Aligned (Signature Edition) - Parenting Together"
 ],
 "Extended Family & In-Laws": [
  "In-Law Boundaries That Preserve Peace (Signature Edition) - Extended Family & In-Laws",
  "Holiday Negotiation Without the War (Signature Edition) - Extended Family & In-Laws",
  "When Parents Need Care: The Sandwich Season (Signature Edition) - Extended Family & In-Laws",
  "Blending Families With Grace (Signature Edition) - Extended Family & In-Laws"
 ],
 "Keeping Connection": [
  "Rituals of Connection: The Small Things That Bind (Signature Edition) - Keeping Connection",
  "Growing Together, Not Apart (Signature Edition) - Keeping Connection",
  "Anniversaries and Milestones That Matter (Signature Edition) - Keeping Connection",
  "The Marriage Mission Statement (Signature Edition) - Keeping Connection",
  "Legacy: The Marriage You Leave Behind (Signature Edition) - Keeping Connection"
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
var gen={version:'jahdb-marriage-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('marriage-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
