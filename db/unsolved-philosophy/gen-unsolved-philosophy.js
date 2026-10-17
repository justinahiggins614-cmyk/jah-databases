(function(){'use strict';
/* JAH The Unsolved Philosophy Database generator \u2014 jahdb-unsolved-philosophy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Topics mirror the archive's 34
   seeded records; generated records are labeled samples, never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USPL-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS=[
 ["What is the meaning of life?", "Foundations", "Is there a meaning to human life, and if so, what is it?"],
 ["Why be moral? The amoralist's challenge", "Foundations", "Why should anyone be moral when immorality would pay?"],
 ["Can we know the external world? The problem of skepticism", "Foundations", "How do you know you are not dreaming, deceived, or a brain in a vat being fed perfect simulations?"],
 ["Do we have free will? Determinism and choice", "Foundations", "If every event, including every human decision, is fixed by prior causes and the laws of nature, can anyone genuinely choose?"],
 ["What is the self? Personal identity over time", "Foundations", "What makes you the same person as the child in your old photographs?"],
 ["How do we know what others feel? The problem of other minds", "Foundations", "You know your own pain directly, from the inside."],
 ["What is truth?", "Foundations", "What does it mean to call a sentence true?"],
 ["The liar paradox", "Foundations", "Consider the sentence: 'This sentence is false.' If it is true, then what it says holds, so it is false."],
 ["Zeno's paradoxes: is motion an illusion?", "Foundations", "To cross a room you must first cross half, then half of the remainder, and so on through infinitely many steps."],
 ["The sorites paradox: vagueness and the heap", "Foundations", "One grain of sand is not a heap."],
 ["What is beauty? Aesthetic objectivity", "Foundations", "Is beauty in the object or in the eye of the beholder?"],
 ["What is art?", "Compounded", "What makes something a work of art?"],
 ["What is justice?", "Compounded", "What makes a distribution of goods, opportunities, and burdens just?"],
 ["What justifies the state? Political obligation", "Compounded", "Why should anyone obey the law?"],
 ["Are we living in a simulation?", "Compounded", "If a civilization can run detailed simulations of its ancestors, simulated minds could vastly outnumber real ones."],
 ["Is it wrong to believe without evidence? The ethics of belief", "Compounded", "Clifford declared it 'wrong always, everywhere, and for anyone, to believe anything upon insufficient evidence.' James replied that in forced, momentous options, we may - must - believe beyond the evidence."],
 ["The problem of induction", "Compounded", "The sun has risen every day, so it will rise tomorrow - but why?"],
 ["The is-ought gap", "Compounded", "Hume observed that moral writers slide from 'is' to 'ought' without explanation: from descriptions of how things are to prescriptions of how they should be."],
 ["Are there moral facts? Moral realism and its critics", "Compounded", "When we say 'torturing the innocent is wrong,' do we state a fact - the way 'water is H2O' states a fact - or do we merely express an attitude, like 'boo to torture'?"],
 ["Moral luck: can luck make us blameworthy?", "Compounded", "Two drivers run the same red light with equal recklessness; one hits a child who darts out, the other hits nothing."],
 ["Is knowledge justified true belief? The Gettier problem", "Compounded", "For decades, knowledge was defined as justified true belief."],
 ["How is any belief justified? The Munchhausen trilemma", "Compounded", "Ask 'why?' for any belief, then ask 'why?' of the answer, and repeat."],
 ["The mind-body problem", "Compounded", "How do mind and body relate?"],
 ["The hard problem of consciousness", "Advanced", "Why is there subjective experience at all?"],
 ["Can machines understand? The Chinese room", "Advanced", "A man in a room shuffles Chinese symbols by rulebook, answering questions indistinguishably from a native speaker - yet understands no Chinese."],
 ["How can thoughts be about things? Intentionality", "Advanced", "Your thought right now is about this problem - but how?"],
 ["Do we see the world as it is? The problem of perception", "Advanced", "Hallucinations can be indistinguishable from seeing."],
 ["What is causation?", "Advanced", "We say smoking causes cancer and strikes cause fires."],
 ["What is time? Presentism, eternalism, and McTaggart", "Advanced", "Does only the present exist, or are past and future as real as now?"],
 ["Newcomb's problem: rationality and prediction", "Advanced", "A predictor who has been right 99% of the time fills boxes: box A holds $1,000 always; box B holds $1,000,000 if she predicted you would take only B, nothing otherwise."],
 ["Sleeping Beauty: probability and self-location", "Advanced", "Sleeping Beauty is put to sleep Sunday."],
 ["Are our best scientific theories true? Scientific realism", "Advanced", "Science's theories are stunningly successful - so they must be approximately true, says the realist."],
 ["Can evidence decide between theories? Underdetermination", "Advanced", "For any theory, rival theories can fit the same data - by the Duhem-Quine thesis, even a failed prediction can be blamed on auxiliary hypotheses rather than the core theory."],
 ["Why is there something rather than nothing?", "Advanced", "Leibniz called it the first question of metaphysics: why does anything exist at all?"],
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
var gen={version:"jahdb-unsolved-philosophy-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("unsolved-philosophy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
