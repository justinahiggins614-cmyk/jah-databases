(function(){'use strict';
/* JAH The Unsolved Philosophy Database generator \u2014 jahdb-unsolved-philosophy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Topics mirror the archive's 34
   seeded records; generated records are labeled samples, never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USPLS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS=[
 ["What is the meaning of life? (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["Why be moral? The amoralist's challenge (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["Can we know the external world? The problem of skepticism (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["Do we have free will? Determinism and choice (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["What is the self? Personal identity over time (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["How do we know what others feel? The problem of other minds (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["What is truth? (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["The liar paradox (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["Zeno's paradoxes: is motion an illusion? (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["The sorites paradox: vagueness and the heap (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["What is beauty? Aesthetic objectivity (Signature Edition)", "Foundations", "Signature original interpretation."],
 ["What is art? (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["What is justice? (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["What justifies the state? Political obligation (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["Are we living in a simulation? (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["Is it wrong to believe without evidence? The ethics of belief (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["The problem of induction (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["The is-ought gap (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["Are there moral facts? Moral realism and its critics (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["Moral luck: can luck make us blameworthy? (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["Is knowledge justified true belief? The Gettier problem (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["How is any belief justified? The Munchhausen trilemma (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["The mind-body problem (Signature Edition)", "Compounded", "Signature original interpretation."],
 ["The hard problem of consciousness (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Can machines understand? The Chinese room (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["How can thoughts be about things? Intentionality (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Do we see the world as it is? The problem of perception (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["What is causation? (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["What is time? Presentism, eternalism, and McTaggart (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Newcomb's problem: rationality and prediction (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Sleeping Beauty: probability and self-location (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Are our best scientific theories true? Scientific realism (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Can evidence decide between theories? Underdetermination (Signature Edition)", "Advanced", "Signature original interpretation."],
 ["Why is there something rather than nothing? (Signature Edition)", "Advanced", "Signature original interpretation."],
];
function topicFor(seed){
  return TOPICS[((seed-1)%TOPICS.length+TOPICS.length)%TOPICS.length];
}
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts){
  opts=opts||{};
  var rnd=prng(seed);
  var t=topicFor(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:t[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:t[0]+' \u2014 unsolved problem record (sample)',
    title:t[0],
    description:'SAMPLE RECORD (generated \u2014 structural sample). '+t[2]+' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'unsolved-demo',language:'python',program:demoProgram(t[0],field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-unsolved-philosophy-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("unsolved-philosophy-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
