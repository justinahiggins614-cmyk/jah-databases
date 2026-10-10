(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var CATLABEL={curriculum:"Curriculum",qualifications:"Qualifications",research:"Research",findings:"Findings",methods:"Methods",textbooks:"Textbooks"};
var PREFIX='JAH-fine-arts-study-S-';
var FIELD='Fine Arts';
var POOLS={"curriculum":[["Drawing foundations","observational skill","Drawing teaches seeing; the hand follows the eye, never the reverse."],["Painting technique strands","medium mastery","Each medium has its own logic; mastery means respecting it rather than fighting it."],["Sculpture training","three-dimensional thinking","Sculpture teaches students to think in the round, which changes how they see everything."],["Colour study","perceptual colour","Colour is relational; students learn it by mixing and comparing, not by reading about it."],["Composition curricula","pictorial structure","Composition is the silent language of pictures; fluency takes years of looking."],["Art history integration","context and practice","History studied alongside practice gives students ancestors instead of just assignments."]],"qualifications":[["Fine arts degrees","studio assessment","Art degrees must assess the work in the studio, where it was made and can be questioned."],["Teaching artist credentials","practice and pedagogy","Teaching artists need both a real practice and the ability to unlock others'."],["Conservation certificates","technical expertise","Conservation credentials certify chemistry and craft in equal measure."],["Curatorial qualifications","exhibition judgment","Curating is an art of selection; qualifications should test the eye, not just the essay."],["Public art commissions","civic process","Public art qualifications must include navigating the civic process, not just making the work."],["Master workshop completions","apprenticeship lineage","The old workshop model still produces the deepest technical mastery."]],"research":[["Creativity studies","process research","Creativity research shows process can be taught even when talent cannot."],["Visual perception research","seeing science","Perception science explains why the old masters' techniques still work."],["Art education outcomes","longitudinal effects","Long-term studies show art education strengthens the attention and persistence all subjects need."],["Material science for artists","pigment and support","Material research keeps centuries of craft knowledge alive and extends it."],["Aesthetic response studies","viewer experience","Studies of viewers show that looking longer changes what is seen; museums are built on this."],["Studio pedagogy research","critique effectiveness","Research on critique shows that specific, work-focused feedback grows artists fastest."]],"findings":[["Deliberate practice effects","focused repetition","Focused, feedback-rich practice builds skill; casual hours mostly pass time."],["Master study effects","copying the masters","Copying masterworks trains the eye faster than any exercise invented since."],["Critique frequency effects","regular review","Frequent critique keeps work from drifting; the mirror must be held up often."],["Sketchbook effects","daily drawing","Daily sketchbooks compound into fluency the way daily reading compounds into literacy."],["Exhibition effects","public showing","Showing work publicly sharpens it; the coming audience edits the hand."],["Cross-medium effects","discipline transfer","Working in a second medium refreshes the first; sculptors draw better for sculpting."]],"methods":[["Life drawing sessions","sustained observation","Long poses teach sustained looking, the root skill of all representational art."],["Value studies","tonal mapping","Value structure carries a picture; colour without value is decoration."],["Underpainting techniques","layered construction","Underpainting builds luminosity that direct painting cannot reach."],["Maquette building","small-scale modelling","Small models let sculptors solve big problems cheaply."],["Palette discipline","limited colour","Limited palettes teach colour harmony faster than full ones."],["Portfolio review method","structured critique","Structured reviews separate the work's problems from the artist's worth."]],"textbooks":[["Anatomy for artists","structural drawing","Anatomy texts for artists must show structure in action, not just label parts."],["Perspective manuals","constructed space","Perspective learned by construction stays with the artist for life."],["Colour theory texts","mixing guides","Colour texts should be tested at the palette, not just admired on the page."],["Art history surveys","canon and context","Surveys should show why each movement mattered, not just what it looked like."],["Technique compendiums","medium references","Compendiums earn their keep with recipes that actually work in the studio."],["Critique guides","looking and talking","Guides that teach precise visual language make every critique more useful."]]};
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
var gen={version:'jahdb-fine-arts-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fine-arts-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
