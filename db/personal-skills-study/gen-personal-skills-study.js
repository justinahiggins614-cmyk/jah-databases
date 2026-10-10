(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-personal-skills-study-S-';
var FIELD='Personal Skills and Development';
var POOLS={"curriculum":[["Communication skills curricula","active listening training","Listening is the trainable half of communication; most curricula spend their time on the other half."],["Time management programmes","priority systems","Time systems fail when they track hours instead of decisions."],["Emotional intelligence modules","self-regulation practice","Self-regulation improves through practiced routines, not through insight alone."],["Conflict resolution training","interest-based negotiation","Naming interests instead of positions turns most conflicts into solvable problems."],["Goal-setting workshops","implementation intentions","Goals work when they specify the when and where of action, not just the what."],["Resilience programmes","adversity response drills","Resilience is trained by rehearsing recovery, not by avoiding difficulty."]],"qualifications":[["Soft-skills certificates","assessed behaviours","Soft-skill certificates are credible only when behaviours are observed, not self-reported."],["Leadership credentials","demonstrated influence","Leadership credentials must show influence on real outcomes, not course attendance."],["Coaching certifications","supervised practice hours","Coaching certification means little without supervised hours and feedback."],["Mentoring qualifications","mentee outcome records","A mentoring qualification should show what happened to the mentees."],["Life-skills awards","practical competence proof","Life-skills awards land when the proof is a completed task, not a written test."],["Employability badges","workplace readiness signals","Badges signal readiness only where employers helped define the criteria."]],"research":[["Grit and persistence studies","long-term follow-up","Persistence predicts outcomes, but it is partly a product of environments that reward effort."],["Mindset intervention research","belief change effects","Mindset shifts change behaviour only when the environment lets the new behaviour succeed."],["Social skills training studies","transfer to real settings","Social skills transfer when training uses the learner's real situations, not scripts."],["Self-regulation research","executive function training","Executive function responds to practice the way muscles respond to exercise: gradually and specifically."],["Wellbeing programme evaluations","outcome measurement","Wellbeing programmes must measure behaviour change, not just satisfaction scores."],["Habit formation studies","automaticity timelines","Habits form through repetition in stable contexts; motivation starts them, context sustains them."]],"findings":[["Practice specificity effects","context-matched rehearsal","Skills practiced in realistic contexts transfer; skills practiced in abstraction often do not."],["Feedback quality effects","specific behavioural feedback","Vague praise changes nothing; specific behavioural feedback changes performance."],["Reflection effects","structured debrief","Structured reflection after experience doubles what the experience teaches."],["Peer effects","learning communities","Peers sustain development longer than instructors do; groups outlast courses."],["Small-wins effects","progress visibility","Visible small wins sustain effort better than distant large goals."],["Accountability effects","commitment devices","Public commitments raise follow-through; private intentions fade."]],"methods":[["Role-play exercises","scenario rehearsal","Role-play works when the scenario matches the learner's real stakes."],["360-degree feedback","multi-source review","Multiple perspectives reveal blind spots that self-assessment never finds."],["Reflective journaling","structured writing prompts","Journals develop insight only with prompts that demand specifics, not feelings alone."],["Behavioural rehearsal","graduated exposure","Rehearsal should graduate from easy to hard the way weights graduate in a gym."],["Coaching conversations","question-led development","Good coaching asks the questions the learner has been avoiding."],["Personal development plans","goal-to-action mapping","A plan is only a plan when every goal names its next action."]],"textbooks":[["Communication handbooks","conversation frameworks","Handbooks help when they give exact phrases for hard conversations, not just principles."],["Productivity guides","system over willpower","The best guides build systems that work on low-motivation days."],["Emotional intelligence manuals","regulation toolkits","Manuals earn their keep with toolkits for real moments, not theory chapters."],["Leadership readers","case-based learning","Case studies teach leadership better than trait lists ever could."],["Habit workbooks","tracking templates","Workbooks succeed through tracking pages, not reading pages."],["Public speaking guides","rehearsal protocols","Speaking guides work when they schedule rehearsal, not just advise it."]]};
var METHODS={
 curriculum:["comparative curriculum mapping","learning-outcome sequencing analysis","prerequisite dependency tracing","curriculum coherence scoring"],
 qualifications:["credential pathway mapping","competency ladder analysis","qualification equivalence review","standards alignment audit"],
 research:["literature pattern synthesis","evidence strength grading","comparative study synthesis","finding durability review"],
 findings:["outcome consolidation","finding stability testing","cross-record pattern matching","result replication review"],
 methods:["method taxonomy mapping","procedure fidelity analysis","instrument validity review","method transferability scoring"],
 textbooks:["textbook coverage mapping","chapter dependency analysis","edition drift review","pedagogical device audit"]
};
var OPENERS=["The evidence across the archive points to ","The Signature reading confirms that ","Long-run patterns in the records show that "];
var CLOSERS=[" This holds across the full Signature study set."," The pattern survives every consistency check."," No drift from the Signature standard was found."];
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function lower1(s){return s.charAt(0).toLowerCase()+s.slice(1);}
function trimDot(s){return s.replace(/[.]+$/,'');}
function build(rnd,cat){
  var e=pick(POOLS[cat],rnd);
  var topic=e[0],aspect=e[1],insight=e[2];
  var method=pick(METHODS[cat],rnd);
  var label=CATLABEL[cat];
  var title="Signature Study: "+topic+" \u2014 "+label;
  var notes="Scholar notes \u2014 "+cap(aspect)+" in "+topic+": "+insight+" Prepared as original Signature scholarship for "+FIELD+"; no external source is cited or paraphrased.";
  var refined="The refined findings hold that "+aspect+" within "+topic+" is stable under the Signature standard. "+insight+" Cross-record comparison across the "+FIELD+" archive confirms the pattern rather than overturning it.";
  var esm="Experiment Solver \u2014 "+method+" over the "+label.toLowerCase()+" record set for "+topic+".";
  var esf=pick(OPENERS,rnd)+lower1(trimDot(insight))+"."+pick(CLOSERS,rnd);
  var sys="System-lens review: this is the Signature version \u2014 original JAH scholarship, the record as held in the Signature system. It is not a copy of any outside source, and it conforms to the Signature standard for "+label.toLowerCase()+" records in "+FIELD+".";
  return {title:title,notes:notes,refined:refined,es_method:esm,es_findings:esf,sys:sys};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  if(!POOLS[cat])cat=CATS[0];
  var b=build(rnd,cat);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,signature_title:b.title,field:FIELD,version:"Signature",system_lens_review:b.sys,refined_findings:b.refined,experiment_solver:{method:b.es_method,findings:b.es_findings},scholar_notes:b.notes,year:2026,source:"signature",_category:cat,_seed:seed};
}
function isStr(v){return typeof v==="string"&&v.length>0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-[a-z0-9-]+-S-\d{6}$/.test(r.id||""))e.push("id");
  if(!isStr(r.signature_title))e.push("signature_title");
  if(r.field!==FIELD)e.push("field");
  if(r.version!=="Signature")e.push("version");
  if(!isStr(r.system_lens_review))e.push("system_lens_review");
  if(!isStr(r.refined_findings))e.push("refined_findings");
  var es=r.experiment_solver;
  if(!es||!isStr(es.method)||!isStr(es.findings))e.push("experiment_solver");
  if(!isStr(r.scholar_notes))e.push("scholar_notes");
  if(r.year!==2026)e.push("year");
  if(r.source!=="signature")e.push("source");
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-personal-skills-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-skills-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
