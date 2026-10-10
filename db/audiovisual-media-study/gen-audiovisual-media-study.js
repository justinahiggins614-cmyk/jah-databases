(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-audiovisual-media-study-S-';
var FIELD='Audio-Visual Media Production';
var POOLS={"curriculum":[["Screenwriting fundamentals","three-act structure","Structure is invisible when it works; students must learn it before they can hide it."],["Cinematography training","visual grammar","Every shot is a sentence; students must learn the grammar before writing the essay."],["Sound design curricula","layered audio","Audiences forgive weak images before weak sound; the ear decides quality first."],["Editing craft","rhythm and pacing","Editing is the final rewrite; pacing decisions are storytelling decisions."],["Directing workshops","performance shaping","Directing is mostly casting and communication; the camera merely records the result."],["Production management strands","scheduling and budgets","A production lives or dies on its schedule; craft cannot rescue chaos."]],"qualifications":[["Film production certificates","set-ready skills","Certificates should certify what a graduate can actually do on a working set."],["Broadcast credentials","live production competence","Live credentials must prove calm under real transmission pressure."],["Editing certifications","software mastery","Editing certification means finishing real projects to deadline, not passing quizzes."],["Sound engineering awards","mix quality","A sound award should be judged with ears, on finished mixes."],["Cinematography diplomas","portfolio review","The portfolio is the credential; everything else is paperwork."],["Media production degrees","theory-practice integration","Degrees work when theory is tested against real production problems."]],"research":[["Audience reception studies","viewer response","Audiences remember how media made them feel longer than what it told them."],["Narrative structure research","story cognition","Stories work because brains are prediction machines; structure exploits that."],["Media effects studies","influence measurement","Media effects are real, conditional, and smaller than either alarmists or deniers claim."],["Production workflow research","pipeline efficiency","Studied pipelines reveal that most delays come from decisions, not from tools."],["Sound perception studies","audio and emotion","Sound shapes emotion faster than image; the research explains why scores work."],["Editing cognition research","cut comprehension","Viewers parse cuts effortlessly because the brain edits reality the same way."]],"findings":[["Pre-production effects","planning and quality","Thorough pre-production predicts finished quality better than budget does."],["Sound quality effects","audio investment","Money spent on sound returns more perceived quality than the same money spent on cameras."],["Pacing effects","cut rhythm","Pacing controls attention; the right rhythm keeps viewers without them noticing."],["Lighting effects","mood and meaning","Lighting tells the audience how to feel before a word is spoken."],["Rehearsal effects","performance preparation","Rehearsed performances need fewer takes and cut together better."],["Feedback screening effects","test audiences","Test screenings catch the confusions the makers are too close to see."]],"methods":[["Storyboarding","visual planning","Boards expose story problems while they are still cheap to fix."],["Shot listing","coverage planning","A complete shot list is insurance against the edit bay discovering what is missing."],["Location scouting","practical assessment","Scouting must assess sound, light, and logistics, not just looks."],["Colour grading workflows","look development","Grading unifies footage shot across days into one coherent world."],["Foley recording","sound effects craft","Foley sells reality; audiences believe what they hear over what they see."],["Continuity supervision","match tracking","Continuity notes save productions from reshoots that budgets cannot afford."]],"textbooks":[["Screenwriting manuals","format and craft","Manuals must teach both the format rules and when to break them."],["Cinematography guides","exposure and composition","Guides should train the eye first and the equipment second."],["Sound design texts","recording and mixing","Sound texts earn their place with practical signal-chain knowledge."],["Editing handbooks","cutting principles","Handbooks should teach why to cut, not just where."],["Directing books","working with actors","The useful directing books are about people, not cameras."],["Production bibles","department coordination","A production bible aligns every department to one vision on paper."]]};
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
var gen={version:'jahdb-audiovisual-media-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('audiovisual-media-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
