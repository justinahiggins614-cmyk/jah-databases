(function(){'use strict';
/* The The Tutorial Content Database Signature generator — jahdb-db-tutorial-content-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-TUTORIAL-CONTENT-SIG-";
var GENVER="jahdb-db-tutorial-content-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 5-Minute Skill",
  "The First Steps",
  "The Common Mistakes",
  "The Tool Tour",
  "The Warm-Up",
  "The Follow-Along",
  "The Cheat Sheet",
  "The FAQ Lesson",
  "The Speed Run",
  "The Slow Motion",
  "The Practice Drill",
  "The Check-In"
 ],
 "Compounded": [
  "The Full Course",
  "The Project Build",
  "The Master the Basics",
  "The Intermediate Leap",
  "The Style Guide",
  "The Troubleshooting Clinic",
  "The Workflow",
  "The Theory Lesson",
  "The Challenge Lesson",
  "The Guest Expert",
  "The Live Lesson",
  "The Series Course"
 ],
 "Advanced": [
  "The Masterclass",
  "The Certification Path",
  "The Mentorship",
  "The Textbook",
  "The Academy",
  "The Research Tutorial",
  "The Pedagogy",
  "The Legacy Course",
  "Teaching Tutorial Design",
  "Masterclass: How Humans Learn"
 ]
};
var BLURBS={
 "The 5-Minute Skill": "One tiny skill, fully taught: the quick win.",
 "The First Steps": "Absolute beginner lesson: the welcome.",
 "The Common Mistakes": "What goes wrong: the troubleshooting.",
 "The Tool Tour": "Know your gear: the orientation.",
 "The Warm-Up": "Prepare properly: the foundation.",
 "The Follow-Along": "Do it with me: the companion.",
 "The Cheat Sheet": "The essentials, condensed: the reference.",
 "The FAQ Lesson": "Answer everything: the comprehensive.",
 "The Speed Run": "The skill, fast: the overview.",
 "The Slow Motion": "Frame by frame: the detailed.",
 "The Practice Drill": "Reps that build: the workout.",
 "The Check-In": "Test yourself: the milestone.",
 "The Full Course": "Beginner to competent: the curriculum.",
 "The Project Build": "Learn by making: the applied.",
 "The Master the Basics": "Foundations, deeply: the thorough.",
 "The Intermediate Leap": "Beyond basics: the progression.",
 "The Style Guide": "Develop your voice: the artistic.",
 "The Troubleshooting Clinic": "Fix anything: the diagnostic.",
 "The Workflow": "The pro process: the efficient.",
 "The Theory Lesson": "Why it works: the understanding.",
 "The Challenge Lesson": "Test the skill: the proving.",
 "The Guest Expert": "Another teacher\u2019s take: the perspective.",
 "The Live Lesson": "Real-time teaching: the interactive.",
 "The Series Course": "Multi-part mastery: the school.",
 "The Masterclass": "The definitive teaching: the legacy course.",
 "The Certification Path": "Structured to mastery: the credential.",
 "The Mentorship": "One-on-one guidance: the personal.",
 "The Textbook": "The complete written guide: the reference.",
 "The Academy": "The full school: the institution.",
 "The Research Tutorial": "Cutting-edge teaching: the frontier.",
 "The Pedagogy": "Teaching teachers: the meta.",
 "The Legacy Course": "The life\u2019s work, taught: the magnum opus.",
 "Teaching Tutorial Design": "Show others: the teacher\u2019s teacher.",
 "Masterclass: How Humans Learn": "The learning science: the foundation."
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
    name:topic+' — tutorial record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-tutorial-content-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();