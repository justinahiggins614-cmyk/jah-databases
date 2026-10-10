(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-design-fields-study-S-';
var FIELD='Design (Fashion/Interior/Industrial)';
var POOLS={"curriculum":[["Design fundamentals","form and function balance","Good design resolves the tension between form and function instead of choosing sides."],["Colour theory strands","applied colour","Colour theory matters only when students apply it to real palettes under real light."],["Materials curricula","material literacy","Designers must know materials the way writers know words: intimately and practically."],["Ergonomics training","human-centred measurement","Design for the body as it is, not as the average pretends it to be."],["Sustainable design modules","lifecycle thinking","Sustainability is a design constraint like any other; the best solutions treat it as inspiration."],["Design history surveys","precedent study","History gives designers a vocabulary; ignorance of it guarantees repetition."]],"qualifications":[["Design degrees","studio and theory","Design degrees must judge the work, not just the writing about the work."],["Professional accreditation","practice standards","Accreditation protects the public when it tests real professional judgment."],["Portfolio certifications","work review","The portfolio review is the honest exam; everything else is proxy."],["Technical drafting credentials","precision skills","Precision credentials prove a designer can communicate exactly what to build."],["Sustainable design certificates","lifecycle competence","Green certificates must audit real lifecycle knowledge, not intentions."],["Apprenticeship completions","workshop mastery","Workshop apprenticeships still produce the most capable makers."]],"research":[["User-centred design studies","usability outcomes","Designs tested with real users outperform designs judged by experts alone."],["Aesthetic preference research","taste patterns","Aesthetic preferences follow patterns; research maps them so designers can use or defy them deliberately."],["Ergonomic studies","comfort and performance","Ergonomic research keeps turning up the same lesson: fit matters more than features."],["Sustainability research","material lifecycles","Lifecycle studies reveal which green choices actually help and which merely market."],["Design cognition studies","creative process","Studying how designers think shows that constraints fuel creativity rather than blocking it."],["Trend research","cycle analysis","Trends cycle; research separates the structural shifts from the seasonal noise."]],"findings":[["Prototyping effects","iteration speed","Fast prototypes beat perfect plans; each iteration teaches what planning cannot."],["Constraint effects","creative limits","Tight constraints produce more original work than open briefs."],["User testing effects","feedback loops","Testing with five users finds most problems; testing with none finds none."],["Sketching effects","thinking by drawing","Sketching externalizes thought; designers who sketch decide better and faster."],["Critique effects","structured review","Structured critique improves work; unstructured opinion mostly defends taste."],["Cross-disciplinary effects","team diversity","Mixed teams of fashion, interior, and industrial designers solve broader problems."]],"methods":[["Mood boarding","visual research","Boards align a team on feeling before anyone commits to form."],["Technical flat sketching","specification drawing","Flats communicate construction intent precisely enough to manufacture from."],["3D modelling workflows","digital prototyping","Digital models catch proportion errors that drawings hide."],["Material sampling","tactile libraries","Sampling by hand builds the material judgment no screen can teach."],["Fit and drape testing","garment trials","Fashion lives or dies on the body; the stand and the fitting are where it is decided."],["Space planning","interior layout method","Space planning is choreography: the plan must serve the movement of real life."]],"textbooks":[["Pattern-making manuals","construction geometry","Pattern manuals must be precise enough to cut from; vagueness wastes cloth."],["Interior design references","space standards","References earn shelf space with dimensions designers actually need on the job."],["Industrial design handbooks","manufacturing literacy","Handbooks should teach what factories can actually make, not just what looks good."],["Colour system guides","standardized palettes","Standardized colour guides end the arguments that swatches start."],["Design history volumes","movement surveys","History volumes should connect movements to the conditions that produced them."],["Portfolio guides","presentation craft","Portfolio guides teach the curation that turns good work into hired work."]]};
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
var gen={version:'jahdb-design-fields-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('design-fields-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
