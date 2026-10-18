(function(){'use strict';
/* The The Community Feedback Database generator — jahdb-db-community-feedback-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-COMMUNITY-FEEDBACK-PUB-";
var GENVER="jahdb-db-community-feedback-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Suggestion Box",
  "The Survey",
  "The Poll",
  "The Thread",
  "The Form",
  "The Office Hours",
  "The AMA",
  "The Comment Harvest",
  "The DM Review",
  "The Exit Ask",
  "The Welcome Ask",
  "The Thanks"
 ],
 "Compounded": [
  "The Theme Report",
  "The Roadmap",
  "The Beta Group",
  "The Advisory",
  "The Deep Dive",
  "The Priorities Vote",
  "The Change Log",
  "The Apology",
  "The Celebration",
  "The Follow-Up",
  "The Annual Review",
  "The Benchmark"
 ],
 "Advanced": [
  "The Governance",
  "The Co-Creation",
  "The Movement",
  "The Legacy System",
  "The Global Listen",
  "The Succession",
  "The Documentary",
  "The Standard",
  "Teaching Feedback Systems",
  "Masterclass: The Listening Organization"
 ]
};
var BLURBS={
 "The Suggestion Box": "The open channel: the welcome.",
 "The Survey": "Ask directly: the structured.",
 "The Poll": "Quick pulse: the gauge.",
 "The Thread": "Discuss openly: the forum.",
 "The Form": "Organized input: the systematic.",
 "The Office Hours": "Listen live: the personal.",
 "The AMA": "Ask anything: the brave.",
 "The Comment Harvest": "Mine the comments: the attentive.",
 "The DM Review": "Private voices: the confidential.",
 "The Exit Ask": "Why they left: the honest.",
 "The Welcome Ask": "What they need: the proactive.",
 "The Thanks": "Acknowledge all: the gracious.",
 "The Theme Report": "Patterns published: the transparent.",
 "The Roadmap": "Plans from feedback: the responsive.",
 "The Beta Group": "Test with members: the collaborative.",
 "The Advisory": "Member council: the representative.",
 "The Deep Dive": "One issue, fully: the thorough.",
 "The Priorities Vote": "Rank the asks: the democratic.",
 "The Change Log": "What changed: the proof.",
 "The Apology": "When wrong: the humble.",
 "The Celebration": "Wins shared: the joyful.",
 "The Follow-Up": "Check it worked: the diligent.",
 "The Annual Review": "The year\u2019s listening: the retrospective.",
 "The Benchmark": "Compare over time: the trending.",
 "The Governance": "Feedback as policy: the constitutional.",
 "The Co-Creation": "Members as partners: the deep.",
 "The Movement": "Feedback at scale: the historic.",
 "The Legacy System": "The enduring loop: the institution.",
 "The Global Listen": "Many voices: the universal.",
 "The Succession": "The system beyond you: the eternal.",
 "The Documentary": "The listening story: the inspiring.",
 "The Standard": "The industry model: the exemplary.",
 "Teaching Feedback Systems": "Show others: the listening mentor.",
 "Masterclass: The Listening Organization": "Why feedback wins: the trust science."
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
    name:topic+' — feedback system record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-community-feedback',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();