(function(){'use strict';
/* The The Online Event Planner generator — jahdb-db-online-event-planner-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-ONLINE-EVENT-PLANNER-PUB-";
var GENVER="jahdb-db-online-event-planner-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Game Night",
  "The Watch Party",
  "The Trivia Night",
  "The Hangout",
  "The Book Club",
  "The Cook-Along",
  "The Craft Night",
  "The Movie Riff",
  "The Karaoke Night",
  "The Show and Tell",
  "The Meditation",
  "The Toast"
 ],
 "Compounded": [
  "The Workshop",
  "The Tournament",
  "The Conference",
  "The Concert",
  "The Fundraiser",
  "The Reunion",
  "The Launch Party",
  "The Awards Night",
  "The Hackathon",
  "The Retreat",
  "The Festival",
  "The Summit"
 ],
 "Advanced": [
  "The Convention",
  "The Global Gathering",
  "The Annual Gala",
  "The Telethon",
  "The Virtual World",
  "The Legacy Event",
  "The Movement",
  "The Archive",
  "Teaching Event Hosting",
  "Masterclass: Digital Gathering"
 ]
};
var BLURBS={
 "The Game Night": "Jackbox and friends: the classic.",
 "The Watch Party": "Synced viewing: the shared screen.",
 "The Trivia Night": "Questions and teams: the brain battle.",
 "The Hangout": "No agenda, just together: the virtual living room.",
 "The Book Club": "Discuss the chapters: the literary.",
 "The Cook-Along": "Same recipe, many kitchens: the delicious.",
 "The Craft Night": "Make together: the creative.",
 "The Movie Riff": "Commentary track, live: the funny.",
 "The Karaoke Night": "Sing together: the joyful noise.",
 "The Show and Tell": "Share treasures: the personal.",
 "The Meditation": "Breathe together: the calm.",
 "The Toast": "Raise glasses apart: the celebration.",
 "The Workshop": "Teach a skill: the learning.",
 "The Tournament": "Bracketed competition: the thrilling.",
 "The Conference": "Talks and panels: the professional.",
 "The Concert": "Live music online: the performance.",
 "The Fundraiser": "Give together: the generous.",
 "The Reunion": "The scattered, gathered: the emotional.",
 "The Launch Party": "Celebrate the release: the exciting.",
 "The Awards Night": "Honor the community: the ceremonial.",
 "The Hackathon": "Build together: the maker marathon.",
 "The Retreat": "A day apart, together: the restorative.",
 "The Festival": "Multi-act online: the big show.",
 "The Summit": "Expert voices: the insightful.",
 "The Convention": "The full online con: the epic.",
 "The Global Gathering": "Time zones united: the worldwide.",
 "The Annual Gala": "The year\u2019s big night: the institution.",
 "The Telethon": "The marathon fundraiser: the legendary.",
 "The Virtual World": "A persistent gathering place: the metaverse.",
 "The Legacy Event": "The historic online moment: the unforgettable.",
 "The Movement": "Gather for change: the purposeful.",
 "The Archive": "The event\u2019s memory: the documented.",
 "Teaching Event Hosting": "Show others: the host mentor.",
 "Masterclass: Digital Gathering": "Why online events work: the connection science."
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
    name:topic+' — online event record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-online-event-planner',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();