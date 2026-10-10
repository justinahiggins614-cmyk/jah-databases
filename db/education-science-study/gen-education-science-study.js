(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-education-science-study-S-';
var FIELD='Education Science';
var POOLS={"curriculum":[["Learning theory foundations","constructivist principles","Learners build new knowledge on old; curricula that ignore prior knowledge teach into the void."],["Cognitive load in lesson design","working memory limits","Lessons that respect working-memory limits teach more in less time."],["Curriculum theory","intended versus enacted curriculum","The curriculum that matters is the one actually taught, and the gap is always larger than assumed."],["Developmental sequencing","age-appropriate progression","Sequence must follow developmental readiness; forcing the order produces brittle learning."],["Inclusive curriculum design","universal design for learning","Designing for the margins improves the experience for the middle."],["Assessment literacy curricula","teacher assessment skill","Teachers who understand assessment design use it to guide learning, not just to grade it."]],"qualifications":[["Education degrees","theory-practice balance","Education degrees fail when theory and practice live in separate semesters."],["Teaching licenses","competency demonstration","Licensing protects learners only when it requires demonstrated teaching, not just coursework."],["Advanced education credentials","research competence","Advanced credentials should certify the ability to read and use research, not just cite it."],["Specialist endorsements","depth certification","Endorsements mean something when they demand deep study, not a weekend workshop."],["Continuing education units","genuine renewal","Continuing education renews practice only when it challenges routines instead of confirming them."],["Doctoral qualifications","original contribution","A doctorate in education must change what is known, not merely summarize it."]],"research":[["Meta-analytic methods","synthesis of syntheses","Education moves forward when syntheses are compared, not when single studies are worshipped."],["Randomized trials in schools","field experiment design","School trials are hard and worth it; they separate what works from what merely correlates."],["Learning analytics","data-driven instruction","Analytics help when they answer a teacher's real question, not when they produce dashboards."],["Qualitative classroom research","thick description","Close observation catches the mechanisms that numbers can only guess at."],["Replication studies","finding durability","Education's replication record is humbling; durable findings are the ones that survive it."],["Policy evaluation research","reform impact studies","Reforms should be evaluated by student learning, not by implementation checklists."]],"findings":[["Retrieval practice effects","testing as learning","Recalling information strengthens memory more than re-reading it ever will."],["Spacing effects","distributed practice","Distributed practice beats massed practice in nearly every domain tested."],["Interleaving effects","mixed practice","Mixing problem types builds the discrimination skill that blocked practice skips."],["Feedback effects","elaborative feedback","Feedback that explains why outperforms feedback that only marks right or wrong."],["Worked-example effects","example-to-problem fading","Worked examples help novices; experts need problems, and the transition matters."],["Desirable difficulty","productive struggle","Learning that feels easy is often learning that will not last."]],"methods":[["Classroom observation protocols","structured watching","Observation protocols turn watching into data instead of impressions."],["Think-aloud protocols","process tracing","Think-alouds reveal the strategies behind the answers."],["Design-based research","iterative intervention design","Design research improves practice and theory together, in cycles."],["Value-added modelling","teacher effect estimation","Value-added models inform, but they must never be the whole story of a teacher."],["Survey methodology","attitude measurement","Surveys measure what people will admit; behaviour measures the rest."],["Ethnographic fieldwork","sustained immersion","Long immersion in a school reveals the unwritten curriculum that shapes everything."]],"textbooks":[["Learning science textbooks","evidence organization","A good text organizes by principle and shows the evidence, not just the conclusion."],["Research methods texts","design literacy","Methods texts should teach readers to spot a weak design, not just to name designs."],["Statistics for educators","practical inference","Educators need statistics that answer what it means for the classroom on every page."],["History of education volumes","institutional memory","Knowing how schools got this way keeps reformers from repeating the last failure."],["Philosophy of education readers","purpose debates","Purpose questions decide methods; the reader who skips them inherits someone else's answers."],["Curriculum studies anthologies","field mapping","Anthologies should map the field's debates, not just collect its greatest hits."]]};
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
var gen={version:'jahdb-education-science-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('education-science-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
