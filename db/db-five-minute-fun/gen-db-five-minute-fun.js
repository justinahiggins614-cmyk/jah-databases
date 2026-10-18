(function(){'use strict';
/* The The Five-Minute Fun Database generator — jahdb-db-five-minute-fun-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-FIVE-MINUTE-FUN-PUB-";
var GENVER="jahdb-db-five-minute-fun-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 5-Minute Doodle",
  "Word Ladder",
  "The Gratitude Speed-Run",
  "Stretch Sequence",
  "The Memory Game",
  "Haiku Moment",
  "The Compliment Text",
  "Cloud Story",
  "The 5-Minute Tidy",
  "Breathing Reset",
  "The Riddle Break",
  "Dance to One Song"
 ],
 "Compounded": [
  "The Mini Crossword",
  "Speed Sketch Challenge",
  "The 5-Minute Language",
  "Origami One-Fold",
  "The Logic Puzzle",
  "Micro-Journal",
  "The Kindness Ping",
  "The 5-Minute Meditate",
  "Tongue Twister Trials",
  "The Photo Hunt",
  "Speed-Read a Poem",
  "The Balance Challenge"
 ],
 "Advanced": [
  "The 5-Minute Masterclass",
  "The Daily Design",
  "Micro-Habit Stacking",
  "The 5-Minute Pitch",
  "The Observation Log",
  "The Micro-Adventure",
  "The 5-Minute Mentor",
  "The Evening 5",
  "Legacy: The 5-Minute Life",
  "Masterclass: Attention Restoration"
 ]
};
var BLURBS={
 "The 5-Minute Doodle": "Draw the thing in front of you: bad art, good break.",
 "Word Ladder": "Change one letter at a time, word to word: the classic puzzle.",
 "The Gratitude Speed-Run": "List ten good things in five minutes: mood, hacked.",
 "Stretch Sequence": "Neck, shoulders, back: the desk worker\u2019s reset.",
 "The Memory Game": "Study ten objects, recall them: the brain\u2019s push-up.",
 "Haiku Moment": "Write a haiku about right now: poetry, instant.",
 "The Compliment Text": "Send one genuine compliment: two moods lifted.",
 "Cloud Story": "One cloud, one story: imagination, exercised.",
 "The 5-Minute Tidy": "One surface, five minutes: visible victory.",
 "Breathing Reset": "Box breathing, five rounds: the nervous system\u2019s off switch.",
 "The Riddle Break": "One good riddle: the mind\u2019s espresso shot.",
 "Dance to One Song": "Full energy, one track: the instant energizer.",
 "The Mini Crossword": "A tiny grid, a big satisfaction: wordplay, compressed.",
 "Speed Sketch Challenge": "Draw ten things in five minutes: quantity over quality, joy over judgment.",
 "The 5-Minute Language": "Learn five words: the streak-friendly lesson.",
 "Origami One-Fold": "One model, one sheet: paper magic, fast.",
 "The Logic Puzzle": "A bite-sized deduction: the satisfying click.",
 "Micro-Journal": "Three lines about today: the diary that takes no time.",
 "The Kindness Ping": "Check on one person: connection, compressed.",
 "The 5-Minute Meditate": "Guided or silent: the reset button, pocket-sized.",
 "Tongue Twister Trials": "Five tries, record the best: silly, shareable.",
 "The Photo Hunt": "Photograph something blue, round, and old: the scavenger micro-game.",
 "Speed-Read a Poem": "One poem, slowly: literature in a lunch break.",
 "The Balance Challenge": "One-foot stand, eyes closed: the wobbly minute.",
 "The 5-Minute Masterclass": "Teach one tiny skill: the expert\u2019s micro-lesson.",
 "The Daily Design": "Redesign one small thing daily: the compounding portfolio.",
 "Micro-Habit Stacking": "Attach one tiny habit to five existing ones: the invisible upgrade.",
 "The 5-Minute Pitch": "Pitch an idea in five: the founder\u2019s drill.",
 "The Observation Log": "Note one new thing daily: attention, trained.",
 "The Micro-Adventure": "Do one slightly-novel thing: the rut-breaker.",
 "The 5-Minute Mentor": "Answer one person\u2019s question: generosity, efficient.",
 "The Evening 5": "End the day with five intentional minutes: the bookend ritual.",
 "Legacy: The 5-Minute Life": "A philosophy of tiny joys: the examined life, in sips.",
 "Masterclass: Attention Restoration": "The science of micro-breaks: why five minutes works."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — five-minute activity record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-five-minute-fun',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();