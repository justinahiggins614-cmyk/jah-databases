(function(){'use strict';
/* The The Daily Curiosity Database Signature generator — jahdb-db-daily-curiosity-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-DAILY-CURIOSITY-SIG-";
var GENVER="jahdb-db-daily-curiosity-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Why Is the Sky Blue?",
  "The Egg Drop Test",
  "How Many Heartbeats?",
  "The Color of Shadows",
  "Why Yawns Are Contagious",
  "The Ice Cube Race",
  "How Old Is Water?",
  "The Moon Tonight",
  "Why Do Onions Cry?",
  "The Ant Highway",
  "How Do Birds Sleep?",
  "The Echo Test"
 ],
 "Compounded": [
  "The Sourdough Experiment",
  "How Deep Is Deep?",
  "The Language Detective",
  "Why Dreams Feel Real",
  "The Crystal Garden",
  "How Old Are the Stars?",
  "The Compass Walk",
  "Why Is Honey Forever?",
  "The Sound Map",
  "How Do Trees Talk?",
  "The Time Perception Test",
  "Why Do Cats Purr?"
 ],
 "Advanced": [
  "The Citizen Science Project",
  "The Year-Long Experiment",
  "How Does Memory Work?",
  "The Deep Time Walk",
  "The Curiosity Interview",
  "The Replication Challenge",
  "The Unanswered Question",
  "The Curiosity Cabinet",
  "Teaching Curiosity",
  "Masterclass: The Curious Mind"
 ]
};
var BLURBS={
 "Why Is the Sky Blue?": "The real answer, in plain words: light scattering, explained.",
 "The Egg Drop Test": "Which egg survives? Kitchen physics, delicious.",
 "How Many Heartbeats?": "Count yours, estimate a lifetime: the math of being alive.",
 "The Color of Shadows": "Look closely: shadows are never just gray.",
 "Why Yawns Are Contagious": "The contagious mystery: what science actually knows.",
 "The Ice Cube Race": "Which melts fastest, and why? The kitchen lab.",
 "How Old Is Water?": "Your glass of water is ancient: the deep history of H2O.",
 "The Moon Tonight": "Find it, note the phase: the monthly cycle, witnessed.",
 "Why Do Onions Cry?": "The chemistry of tears: and how to dodge it.",
 "The Ant Highway": "Watch ants for five minutes: the tiny logistics miracle.",
 "How Do Birds Sleep?": "One eye open: the wild facts of avian rest.",
 "The Echo Test": "Clap in different rooms: the physics of sound, heard.",
 "The Sourdough Experiment": "Capture wild yeast: the living science of bread.",
 "How Deep Is Deep?": "Ocean zones, visualized: the vertical alien world.",
 "The Language Detective": "Trace one word\u2019s history: etymology as time travel.",
 "Why Dreams Feel Real": "The leading theories: your brain\u2019s night shift.",
 "The Crystal Garden": "Grow crystals in a jar: geology, fast-forwarded.",
 "How Old Are the Stars?": "Starlight is time travel: look up and back.",
 "The Compass Walk": "Navigate by sun and landmarks: the ancient GPS.",
 "Why Is Honey Forever?": "The chemistry of eternity in a jar.",
 "The Sound Map": "Map your home by ear: the hidden soundscape.",
 "How Do Trees Talk?": "The wood-wide web: forests are social networks.",
 "The Time Perception Test": "Estimate a minute, then measure: the elastic clock.",
 "Why Do Cats Purr?": "The rumble\u2019s real purposes: comfort, healing, mystery.",
 "The Citizen Science Project": "Join a real study: your observations become data.",
 "The Year-Long Experiment": "One question, twelve months: the slow science.",
 "How Does Memory Work?": "Test your own: the experiment you are running.",
 "The Deep Time Walk": "A walk where each step is a million years: perspective, exercised.",
 "The Curiosity Interview": "Ask an elder one big question: living history.",
 "The Replication Challenge": "Repeat a famous simple experiment: science, verified.",
 "The Unanswered Question": "Pick a real mystery and follow it: the edge of knowledge.",
 "The Curiosity Cabinet": "Build a physical collection of wonders: the museum of you.",
 "Teaching Curiosity": "Spark it in someone else: the wonder that multiplies.",
 "Masterclass: The Curious Mind": "How curiosity works in the brain - and how to keep it for life."
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
    name:topic+' — curiosity record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-daily-curiosity-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();