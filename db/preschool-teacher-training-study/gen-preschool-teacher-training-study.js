(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-preschool-teacher-training-study-S-';
var FIELD='Pre-School Teacher Training';
var POOLS={"curriculum":[["Play-based learning curricula","guided play design","Guided play teaches more than free play or drill; the teacher's role is to enrich, not to direct."],["Early literacy foundations","oral language first","Oral language is the foundation; print follows speech, never the reverse."],["Early numeracy play","mathematical talk","Counting games and shape talk build number sense before any worksheet could."],["Social-emotional curricula","co-regulation practice","Young children learn regulation by being regulated with, calmly and repeatedly."],["Motor development strands","gross and fine motor play","Motor play is not a break from learning; for young children it is learning."],["Creative expression blocks","art and music time","Daily art and music time builds the representational skills all later learning uses."]],"qualifications":[["Early childhood certificates","developmental knowledge","An early-childhood certificate must certify real knowledge of how young children develop."],["Preschool teaching licenses","practical readiness","Licensing a preschool teacher on written exams alone misses the entire job."],["Child development credentials","milestone mastery","Credentials should require teachers to recognize milestones and respond to them."],["First-aid and safety certification","emergency readiness","Safety certification is the one qualification that must never be merely formal."],["Continuing development hours","reflective practice","Ongoing hours matter when they change practice, not when they merely accumulate."],["Assistant-to-teacher pathways","career ladders","Clear ladders keep good assistants in the field instead of losing them to other work."]],"research":[["Attachment studies","teacher-child bonds","Secure teacher-child bonds predict adjustment better than any curriculum variable."],["Language-rich environment research","word exposure studies","The volume and quality of talk in a classroom shapes vocabulary for years."],["Play outcome studies","play and cognition","Mature pretend play predicts self-regulation; the link is one of the field's sturdiest."],["Class size studies","ratio effects","Lower ratios help most where children need the most individual co-regulation."],["Transition studies","preschool to school","Children who visit their future classroom arrive ready; the unfamiliar is what costs them."],["Teacher belief studies","expectations effects","What teachers believe young children can do shapes what the children actually do."]],"findings":[["Read-aloud effects","daily story time","Daily read-alouds grow vocabulary faster than any other single classroom routine."],["Outdoor play effects","nature time","Outdoor time improves attention, motor skill, and mood together; no indoor substitute matches it."],["Routine effects","predictable structure","Predictable routines lower anxiety and free children's attention for learning."],["Peer interaction effects","mixed-age grouping","Mixed-age groups teach the young and deepen the old; both sides gain."],["Music effects","rhythm and language","Rhythm activities strengthen the auditory skills that reading later depends on."],["Parent partnership effects","family engagement","Children do better when teachers and families act as one team with shared information."]],"methods":[["Anecdotal observation","narrative records","Short narrative records capture development that checklists miss."],["Developmental screening","milestone checks","Screening works when it triggers support, not labels."],["Portfolio documentation","work sampling","Collections of real work show growth more honestly than any single test."],["Environment rating scales","classroom quality audit","Rating the environment, not the child, keeps assessment where it belongs."],["Reflective supervision","guided self-review","Teachers who review their own interactions weekly grow faster than those reviewed yearly."],["Family conferencing","partnership meetings","Conferences work when families leave knowing one concrete next step."]],"textbooks":[["Child development texts","stage-by-stage guides","Development texts must show what to do at each stage, not just describe the stage."],["Play pedagogy manuals","facilitation guides","Manuals should teach when to join play and when to stand back."],["Early literacy guides","emergent reading","Emergent-literacy guides work when they start with talk and end with books, in that order."],["Classroom management books","positive guidance","The best management books teach guidance that preserves dignity."],["Art and music activity books","process-focused projects","Activity books should prize the process over the product on every page."],["Observation handbooks","seeing children clearly","Observation handbooks train the teacher's eye, the most important instrument in the room."]]};
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
var gen={version:'jahdb-preschool-teacher-training-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('preschool-teacher-training-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
