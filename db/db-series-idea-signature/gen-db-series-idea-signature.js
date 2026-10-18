(function(){'use strict';
/* The The Series Idea Database Signature generator — jahdb-db-series-idea-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-SERIES-IDEA-SIG-";
var GENVER="jahdb-db-series-idea-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Weekly Roundup",
  "The Beginner\u2019s Guide",
  "The Try-It Series",
  "The Q&A Show",
  "The Top 5",
  "The Day in the Life",
  "The Challenge Series",
  "The Review Show",
  "The Interview Series",
  "The Tutorial Ladder",
  "The Unboxing Ritual",
  "The Vlog Series"
 ],
 "Compounded": [
  "The Documentary Arc",
  "The Competition",
  "The Makeover",
  "The Experiment",
  "The Travel Series",
  "The History Hunt",
  "The Collab Circuit",
  "The Build Log",
  "The Debate Club",
  "The Retrospective",
  "The Prediction Show",
  "The Awards"
 ],
 "Advanced": [
  "The Anthology",
  "The Saga",
  "The Franchise",
  "The Live Series",
  "The Global Series",
  "The Legacy Series",
  "The Reboot",
  "The Finale Season",
  "Teaching Series Design",
  "Masterclass: Serial Storytelling"
 ]
};
var BLURBS={
 "The Weekly Roundup": "This week in your niche: the appointment.",
 "The Beginner\u2019s Guide": "One topic explained simply, weekly: the teacher.",
 "The Try-It Series": "New things attempted: the adventure.",
 "The Q&A Show": "Audience questions answered: the connection.",
 "The Top 5": "Ranked lists, weekly: the debatable.",
 "The Day in the Life": "Process revealed: the intimate.",
 "The Challenge Series": "Escalating dares: the thrilling.",
 "The Review Show": "Honest takes, weekly: the trusted.",
 "The Interview Series": "Fascinating guests: the conversational.",
 "The Tutorial Ladder": "Skills, step by step: the school.",
 "The Unboxing Ritual": "New things, first looks: the exciting.",
 "The Vlog Series": "Life, documented: the personal.",
 "The Documentary Arc": "Deep dives, multi-part: the prestige.",
 "The Competition": "Bracketed battles: the dramatic.",
 "The Makeover": "Transformations: the satisfying.",
 "The Experiment": "Hypotheses tested: the scientific.",
 "The Travel Series": "Places explored: the wanderlust.",
 "The History Hunt": "Stories unearthed: the fascinating.",
 "The Collab Circuit": "Guest creators: the network.",
 "The Build Log": "Projects documented: the maker saga.",
 "The Debate Club": "Ideas clashed: the thought-provoking.",
 "The Retrospective": "Looking back: the nostalgic.",
 "The Prediction Show": "Forecasts made: the bold.",
 "The Awards": "Bests celebrated: the ceremonial.",
 "The Anthology": "Stories in a universe: the expansive.",
 "The Saga": "Years-long narrative: the epic.",
 "The Franchise": "Spin-offs and specials: the empire.",
 "The Live Series": "Real-time unfolding: the event.",
 "The Global Series": "Worldwide scope: the ambitious.",
 "The Legacy Series": "The definitive work: the masterpiece.",
 "The Reboot": "The classic, reimagined: the return.",
 "The Finale Season": "Ending well: the graceful close.",
 "Teaching Series Design": "Show others: the format mentor.",
 "Masterclass: Serial Storytelling": "Why series hook us: the narrative science."
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
    name:topic+' — series concept record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-series-idea-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();