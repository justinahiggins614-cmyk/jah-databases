(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-basic-programmes-study-S-';
var FIELD='Basic Programmes and Qualifications';
var POOLS={"curriculum":[["Foundation programme structures","sequenced learning outcomes","Learners advance most reliably when outcomes are sequenced from prerequisite skills to applied tasks."],["Entry-level syllabus design","core competency coverage","A foundation syllabus must name its core competencies explicitly or gaps appear at the first assessment."],["Bridging courses","transition readiness","Bridging works when it diagnoses the exact gap between a learner's level and the target programme."],["Modular programme architecture","module independence","Modules that can stand alone let learners recover from a single failure without restarting the whole programme."],["Adult basic education tracks","life-relevant content","Adult learners persist when every module connects plainly to work or daily life."],["Remedial pathways","targeted intervention timing","Remediation succeeds when it is short, specific, and scheduled before frustration sets in."]],"qualifications":[["Certificate levels","level descriptors","Clear level descriptors let employers read a certificate and know exactly what the holder can do."],["National qualification frameworks","framework alignment","A qualification gains its value from where it sits in the national framework, not from its title alone."],["Competency-based credentials","demonstrated performance","Competency credentials hold up only when assessment demands real demonstration, not attendance."],["Stackable qualifications","credit accumulation","Stackable systems reward learners for every finished step instead of punishing unfinished wholes."],["Recognition of prior learning","evidence portfolios","Prior learning is recognized fairly when the portfolio standard is published and applied evenly."],["Vocational certificates","workplace validity","A vocational certificate is only as strong as the workplaces that accept it."]],"research":[["Completion rate studies","cohort tracking","Programmes that track cohorts find their drop points fast and fix them while the cohort is still enrolled."],["Comparative framework studies","cross-system comparison","Comparing qualification frameworks reveals which design choices actually move completion rates."],["Adult learner motivation research","persistence factors","Adult persistence rises with visible progress markers more than with any single reward."],["Assessment validity research","predictive power of tests","A basic-skills test is valid when its scores predict real task performance, not just more test scores."],["Programme cost studies","cost per completer","Cost per completer, not cost per enrollee, is the honest measure of a programme's efficiency."],["Longitudinal outcome research","post-programme tracking","Follow-up studies show that programme effects fade unless the qualification leads somewhere concrete."]],"findings":[["Sequencing effects","order of instruction","Teaching prerequisites before applications raises pass rates across every subject measured."],["Modularity effects","module size and completion","Smaller modules produce higher completion because each finish renews the learner's momentum."],["Tutoring effects","one-to-one support","Even brief one-to-one tutoring closes gaps that whole-class teaching leaves open."],["Assessment frequency effects","formative checkpoints","Frequent low-stakes checks catch misunderstanding early, when it is still cheap to fix."],["Cohort effects","peer group stability","Stable cohorts complete at higher rates; churn in the group predicts churn in the individual."],["Credential signalling effects","employer recognition","Qualifications change hiring outcomes only where employers know what the credential means."]],"methods":[["Diagnostic testing","baseline measurement","A good diagnostic names the exact missing skill, not just a low score."],["Competency mapping","skill decomposition","Mapping a qualification into observable competencies makes assessment honest and teachable."],["Portfolio assessment","evidence collection","Portfolios work when the required evidence list is short, clear, and graded the same way every time."],["Standard setting","cut-score determination","Cut scores carry authority when the standard-setting panel's reasoning is published."],["Programme evaluation","outcome auditing","Programme audits must follow learners after exit, or they measure activity instead of effect."],["Curriculum alignment review","objective-to-assessment mapping","Every assessment item should trace to a stated objective; orphans reveal drift."]],"textbooks":[["Foundation textbooks","readability standards","A foundation text fails if its reading level exceeds the level it claims to teach."],["Workbook design","practice density","Workbooks build skill through dense, graduated practice, not through explanation pages."],["Instructor guides","lesson scripting","Guides help new instructors most when they script the first three lessons fully."],["Assessment banks","item quality","A question bank is only as good as its worst item; one bad item teaches the wrong lesson."],["Digital supplements","practice software","Supplements add value only when they give immediate, specific feedback on every attempt."],["Reference charts","quick-lookup design","Charts serve learners best when one page answers one question completely."]]};
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
var gen={version:'jahdb-basic-programmes-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('basic-programmes-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
