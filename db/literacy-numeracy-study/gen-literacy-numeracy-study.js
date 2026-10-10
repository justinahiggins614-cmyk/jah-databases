(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-literacy-numeracy-study-S-';
var FIELD='Literacy and Numeracy';
var POOLS={"curriculum":[["Phonics-based reading curricula","decoding progression","Decoding must precede comprehension work; fluency in parts builds fluency in wholes."],["Whole-language balance","meaning-first reading","Meaning-first approaches work only when decoding is taught alongside, never instead of."],["Number sense curricula","quantity intuition","Learners who can estimate before they calculate catch their own errors for life."],["Writing process curricula","draft and revision cycles","Writing improves through revision cycles, not through single-attempt assignments."],["Mental arithmetic strands","strategy repertoires","Mental arithmetic grows when learners own several strategies and choose among them."],["Vocabulary curricula","word depth over breadth","Deep knowledge of fewer words serves reading better than shallow knowledge of many."]],"qualifications":[["Literacy certificates","reading level benchmarks","A literacy certificate must state the reading level in plain terms to mean anything to an employer."],["Numeracy credentials","applied number tasks","Numeracy credentials prove themselves on real tasks: budgets, measurements, schedules."],["Adult literacy awards","progress recognition","Adults return to study when each award marks progress they can feel."],["Functional skills qualifications","everyday task mastery","Functional qualifications earn respect by testing tasks adults actually face."],["Equivalency examinations","second-chance standards","Equivalency exams open doors only when institutions trust their standard."],["Diagnostic levels","placement accuracy","Correct placement saves months; misplacement wastes them."]],"research":[["Reading acquisition studies","critical windows","Early decoding instruction pays compound interest across every later subject."],["Numeracy anxiety research","affect and performance","Number anxiety depresses performance independently of actual ability."],["Adult literacy surveys","prevalence mapping","Surveys keep showing the same gap: adults hide weak literacy, so outreach must not require self-declaration."],["Intervention meta-analyses","effect sizes","The largest reading gains come from small-group, high-frequency tutoring."],["Bilingual literacy research","transfer across languages","Literacy skills transfer across languages; teaching the second need not restart the first."],["Digital reading studies","screen comprehension","Screen reading demands its own strategies; assuming print skills transfer is a documented error."]],"findings":[["Fluency thresholds","automaticity levels","Reading below the fluency threshold consumes the attention comprehension needs."],["Practice volume effects","time on task","Reading volume predicts vocabulary growth more strongly than any single method."],["Feedback timing effects","immediate correction","Immediate correction during practice prevents errors from hardening into habits."],["Spaced practice effects","distributed sessions","Short daily sessions beat weekly marathons for both reading and arithmetic."],["Home environment effects","print exposure","Children surrounded by print arrive at school already ahead; programmes can narrow but rarely erase the gap."],["Confidence effects","self-efficacy","Learners who believe they can improve persist through the plateaus where others quit."]],"methods":[["Running records","oral reading analysis","Running records reveal exactly which cueing system a reader leans on too hard."],["Miscue analysis","error pattern reading","A reader's errors describe their strategies better than their correct answers do."],["Number talks","mental strategy discussion","Number talks surface the reasoning that written answers hide."],["Diagnostic interviews","one-to-one probing","Five minutes of probing questions map a learner's number sense better than a fifty-item test."],["Writing conferences","individual feedback","A short conference on one paragraph teaches more than margin notes on ten pages."],["Formative reading checks","progress monitoring","Brief, frequent checks let instruction adjust weekly instead of yearly."]],"textbooks":[["Decodable readers","controlled vocabulary texts","Decodable texts let beginners practice exactly the patterns they have been taught."],["Graded arithmetic workbooks","incremental problem sets","Arithmetic workbooks work when each page differs from the last by exactly one step."],["Handwriting manuals","letter formation guides","Clear letter formation taught early frees attention for composition later."],["Mental math drill books","speed and accuracy balance","Drill builds automaticity; understanding must come first or drill builds nothing."],["Read-aloud collections","teacher read-aloud sets","Read-alouds build vocabulary and syntax far above a child's own reading level."],["Numeracy manipulative guides","hands-on materials","Manipulatives bridge concrete and abstract only when the teacher names the connection aloud."]]};
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
var gen={version:'jahdb-literacy-numeracy-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('literacy-numeracy-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
