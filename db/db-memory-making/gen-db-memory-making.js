(function(){'use strict';
/* The The Memory-Making Database generator — jahdb-db-memory-making-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-MEMORY-MAKING-PUB-";
var GENVER="jahdb-db-memory-making-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Golden Hour Photo",
  "The Handwritten Note",
  "The First-Time List",
  "The Meal to Remember",
  "The Stargazing Night",
  "The Thank-You Visit",
  "The Childhood Replay",
  "The Silly Photo Series",
  "The Sunrise Shared",
  "The Recipe Inheritance",
  "The 10-Year Letter",
  "The Perfect Ordinary Day"
 ],
 "Compounded": [
  "The Milestone Celebration",
  "The Adventure Day",
  "The Reunion",
  "The Quest",
  "The Surprise Party",
  "The Road Trip",
  "The Skill Milestone",
  "The Generosity Day",
  "The Cultural Deep Dive",
  "The Night Under Stars",
  "The Home Movie",
  "The Letter to the Future"
 ],
 "Advanced": [
  "The Once-in-a-Lifetime Trip",
  "The Legacy Project",
  "The Family Saga",
  "The 50-Year Tradition",
  "The Impossible Dream",
  "The Reconciliation",
  "The Giving Fortune",
  "The Final Chapter, Well Written",
  "Teaching Memory-Making",
  "Masterclass: The Autobiographical Memory"
 ]
};
var BLURBS={
 "The Golden Hour Photo": "One perfect photo at golden hour: the day\u2019s trophy.",
 "The Handwritten Note": "A letter that will be kept: the memory in an envelope.",
 "The First-Time List": "Do one new tiny thing weekly: novelty, scheduled.",
 "The Meal to Remember": "Cook the dish they will talk about: flavor as memory.",
 "The Stargazing Night": "Blanket, sky, someone you love: the ancient memory.",
 "The Thank-You Visit": "Tell someone in person what they meant: the memory for two.",
 "The Childhood Replay": "Redo a favorite childhood thing as an adult: the loop closed.",
 "The Silly Photo Series": "A recurring ridiculous photo: the album\u2019s joy.",
 "The Sunrise Shared": "Watch dawn with someone: the quiet legend.",
 "The Recipe Inheritance": "Learn the family dish: the edible memory.",
 "The 10-Year Letter": "Write to your future self: the time-travel memory.",
 "The Perfect Ordinary Day": "Document a flawless normal day: the memory of enough.",
 "The Milestone Celebration": "Birthdays, graduations, anniversaries: the designed peak.",
 "The Adventure Day": "A full day built for stories: the legend in 24 hours.",
 "The Reunion": "Gather the scattered: the memory of together.",
 "The Quest": "A multi-stop mission with a prize: the story with chapters.",
 "The Surprise Party": "Planned joy, delivered: the memory of being loved.",
 "The Road Trip": "Miles and mixtapes: the classic memory machine.",
 "The Skill Milestone": "The recital, the race, the reveal: the earned memory.",
 "The Generosity Day": "A day of giving: the memory that warms both sides.",
 "The Cultural Deep Dive": "A festival or tradition joined fully: the memory of belonging.",
 "The Night Under Stars": "Sleep out: the primal, unforgettable night.",
 "The Home Movie": "Film the ordinary beautifully: the memory, directed.",
 "The Letter to the Future": "A capsule of today for decade-later you: the long memory.",
 "The Once-in-a-Lifetime Trip": "The big journey, planned for maximum story: the epic.",
 "The Legacy Project": "Build what outlasts you: the memory for generations.",
 "The Family Saga": "Document the whole story: the memory archive.",
 "The 50-Year Tradition": "Start what your grandchildren will do: the memory that repeats.",
 "The Impossible Dream": "Do the thing they said couldn\u2019t be done: the legend.",
 "The Reconciliation": "Mend what matters: the bravest memory.",
 "The Giving Fortune": "A generosity at scale: the memory that multiplies.",
 "The Final Chapter, Well Written": "Endings designed with care: the memory of grace.",
 "Teaching Memory-Making": "Show others the craft: the memory that teaches.",
 "Masterclass: The Autobiographical Memory": "How memories form - and how to make more of the good kind."
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
    name:topic+' — memory-making record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-memory-making',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();