(function(){'use strict';
/* JAH The Compassionate Statements Signature Database generator — jahdb-compassionate-statements-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSTTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Simple Presence: I Am Here With You (Signature Edition) - Foundations",
  "Naming What You See: This Looks Really Hard (Signature Edition) - Foundations",
  "Permission to Feel: It Is Okay to Feel This Way (Signature Edition) - Foundations",
  "The Honest Admission: I Do Not Know What to Say (Signature Edition) - Foundations",
  "Listening First: Silence Before Solutions (Signature Edition) - Foundations",
  "Comfort for a Hard Day: Small Words, Real Weight (Signature Edition) - Foundations",
  "Honoring Effort: Your Work Matters Even When It Fails (Signature Edition) - Foundations",
  "Words for Disappointment: When Hopes Fall Through (Signature Edition) - Foundations",
  "Visiting the Sick: Comfort Without Cliches (Signature Edition) - Foundations",
  "After a Mistake: Comfort Without Shame (Signature Edition) - Foundations",
  "Standing With Someone in Fear (Signature Edition) - Foundations",
  "Words for Exhaustion: When Someone Is Running Empty (Signature Edition) - Foundations",
  "Acknowledging Pain Without Trying to Fix It (Signature Edition) - Foundations",
  "Comfort for Loneliness: You Are Not Invisible (Signature Edition) - Foundations",
  "Supporting the Caregiver: Who Cares for the Carer (Signature Edition) - Foundations",
  "When Plans Fall Apart: Comfort for Shattered Expectations (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Grief in the First Hours: What to Say at the Start (Signature Edition) - Compounded",
  "Comfort After Job Loss: Dignity in the In-Between (Signature Edition) - Compounded",
  "Words for a Difficult Diagnosis (Signature Edition) - Compounded",
  "Standing With Someone Through Separation (Signature Edition) - Compounded",
  "When Grief Comes Back: Anniversaries and Triggers (Signature Edition) - Compounded",
  "Comforting a Child Through Loss (Signature Edition) - Compounded",
  "Words for Financial Hardship: Shame-Free Support (Signature Edition) - Compounded",
  "Supporting Someone With Chronic Illness (Signature Edition) - Compounded",
  "Sitting With Anger Inside Grief (Signature Edition) - Compounded",
  "Comfort for Regret: When the Past Will Not Let Go (Signature Edition) - Compounded",
  "For the One Who Feels Unworthy of Care (Signature Edition) - Compounded",
  "The Long Goodbye: Words During Slow Decline (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "After Sudden Loss: Words When There Was No Warning (Signature Edition) - Advanced",
  "Supporting a Survivor: Belief as the First Comfort (Signature Edition) - Advanced",
  "For a Parent After the Loss of a Child (Signature Edition) - Advanced",
  "Complicated Grief: Comfort Without Judgment (Signature Edition) - Advanced",
  "When Words Run Out: Presence as the Statement (Signature Edition) - Advanced",
  "The Long Companion: Years of Quiet Support (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Compassionate Statement Study — "+safe+"\n"
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
    name:topic+' — compassionate statement record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A compassionate statement record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"compassionate-statement-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-compassionate-statements-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('compassionate-statements-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
