(function(){'use strict';
/* The The Challenge Video Database generator — jahdb-db-challenge-video-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-CHALLENGE-VIDEO-PUB-";
var GENVER="jahdb-db-challenge-video-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 24-Hour Challenge",
  "The Budget Challenge",
  "The Speed Challenge",
  "The No-Hands Challenge",
  "The Tiny Budget Build",
  "The Blind Taste Test",
  "The Memory Challenge",
  "The Endurance (Safe)",
  "The Swap Challenge",
  "The DIY Duel",
  "The Trivia Gauntlet",
  "The Photo Challenge"
 ],
 "Compounded": [
  "The Week-Long Trial",
  "The Team Tournament",
  "The Skill Sprint",
  "The Survival (Staged)",
  "The Build-Off",
  "The Food Marathon",
  "The Mystery Box",
  "The Role Reversal",
  "The City Challenge",
  "The Charity Challenge",
  "The Collab Clash",
  "The Finale Challenge"
 ],
 "Advanced": [
  "The 30-Day Transformation",
  "The Expedition Challenge",
  "The World Record Try",
  "The Multi-Creator Games",
  "The Impossible Challenge",
  "The Legacy Challenge",
  "The Documentary Challenge",
  "The Global Challenge",
  "Teaching Challenge Design",
  "Masterclass: The Challenge Arc"
 ]
};
var BLURBS={
 "The 24-Hour Challenge": "One day, one constraint: the classic.",
 "The Budget Challenge": "Do it cheap: the frugal feat.",
 "The Speed Challenge": "Against the clock: the sprint.",
 "The No-Hands Challenge": "The hilarious handicap: the silly.",
 "The Tiny Budget Build": "Make with almost nothing: the maker test.",
 "The Blind Taste Test": "Guess the flavors: the delicious game.",
 "The Memory Challenge": "Remember the sequence: the brain game.",
 "The Endurance (Safe)": "Last one standing (comfortably): the gentle marathon.",
 "The Swap Challenge": "Trade lives for a day: the perspective flip.",
 "The DIY Duel": "Same materials, best build: the maker clash.",
 "The Trivia Gauntlet": "Questions, escalating: the knowledge quest.",
 "The Photo Challenge": "Best shot wins: the artistic duel.",
 "The Week-Long Trial": "Seven days transformed: the commitment.",
 "The Team Tournament": "Squads compete: the epic bracket.",
 "The Skill Sprint": "Learn it fast, prove it: the competence race.",
 "The Survival (Staged)": "Wilderness skills, safely: the adventure.",
 "The Build-Off": "Bigger builds, real stakes: the maker war.",
 "The Food Marathon": "Cooking gauntlet: the delicious endurance.",
 "The Mystery Box": "Unknown contents, best creation: the improvisation.",
 "The Role Reversal": "Experts as beginners: the humbling.",
 "The City Challenge": "Urban missions: the metropolitan game.",
 "The Charity Challenge": "Stakes for a cause: the meaningful.",
 "The Collab Clash": "Creators compete: the crossover.",
 "The Finale Challenge": "Season\u2019s ultimate test: the championship.",
 "The 30-Day Transformation": "A month, documented: the legendary arc.",
 "The Expedition Challenge": "Real wilderness, real skills: the epic.",
 "The World Record Try": "Official attempt: the historic.",
 "The Multi-Creator Games": "The olympics of creators: the spectacle.",
 "The Impossible Challenge": "The moonshot: the mythic.",
 "The Legacy Challenge": "The annual signature: the institution.",
 "The Documentary Challenge": "The human story: the meaningful epic.",
 "The Global Challenge": "Worldwide participants: the united.",
 "Teaching Challenge Design": "Show others: the format mentor.",
 "Masterclass: The Challenge Arc": "Why we love watching trials: the drama science."
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
    name:topic+' — challenge video record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-challenge-video',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();