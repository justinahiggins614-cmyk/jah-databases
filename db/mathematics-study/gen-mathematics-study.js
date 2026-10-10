(function(){'use strict';
var SLUG="mathematics-study";
var FIELD="Mathematics";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-mathematics-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Number theory","prove divisibility results and test primality, working from axioms to theorems","the fundamental theorem of arithmetic makes every integer's factorization unique - the primes are the atoms of number","findings hold for integers; unique factorization fails in some rings","primes are the atoms"],["Algebra","solve equations and factor expressions, generalizing patterns to symbolic form","factoring reveals structure that expanding hides - the factored form is the informative one","findings hold for polynomial algebra; the methods generalize","factor to understand"],["Calculus","compute derivatives and integrals, applying them to rates and accumulation problems","the fundamental theorem unites differentiation and integration - two operations, one inverse relationship","findings hold for the standard functions; the theorem is the bridge","differentiation undoes integration"],["Geometry","prove congruence and similarity, computing areas and volumes from first principles","the parallel postulate's independence created non-Euclidean geometry - one axiom changed the universe","findings hold in Euclidean space; the postulate defines the geometry","postulates define the world"],["Linear algebra","solve systems with matrices, computing eigenvalues and testing linear independence","eigenvectors reveal a transformation's action - every linear map is simple in its eigenbasis","findings hold for diagonalizable matrices; the general case needs Jordan form","find the eigenbasis"],["Discrete mathematics","count with combinatorics and prove by induction, modeling discrete structures","induction proves infinitely many cases from two steps - the base case and the inductive step carry everything","findings hold for well-ordered sets; the method is the engine of discrete proof","base case, then the step"],["Differential equations","solve first and second-order equations, modeling growth, decay, and oscillation","the exponential solves linear constant-coefficient equations - e appears because it is its own derivative","findings hold for linear systems; nonlinear equations need qualitative methods","e is its own derivative"],["Logic and proof","formalize arguments in propositional and predicate logic, testing validity","a single counterexample disproves a universal claim - proof and disproof are asymmetric","findings hold in classical logic; constructive systems differ","one counterexample kills the claim"],["Trigonometry","solve triangles and model periodic phenomena with sine and cosine","the unit circle unifies all of trigonometry - every identity is a fact about the circle","findings hold for real angles; complex angles extend the picture","the circle contains everything"],["Combinatorics","count arrangements with permutations, combinations, and the pigeonhole principle","the pigeonhole principle proves existence without construction - counting alone guarantees the result","findings hold universally; the principle is pure logic","counting proves existence"],["Mathematical modeling","translate real situations into equations, validating predictions against data","the best model is the simplest that fits - parsimony predicts better than complexity","findings hold as a principle; domain knowledge sets the model form","simple models win"],["Set theory","work with unions, intersections, and cardinalities, proving countability results","Cantor's diagonal argument shows the reals exceed the naturals - infinities come in sizes","findings hold in standard set theory; the results are foundational","infinities have sizes"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  if(CATS.indexOf(cat)<0)cat=pick(CATS,rnd);
  var tp=pick(TOPICS,rnd),angle=pick(ANGLES,rnd),fr=FRAMING[cat];
  var title=fr.label+' \u2014 '+tp[0]+' ('+angle+')';
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,signature_title:title,field:FIELD,version:'Signature',
    system_lens_review:'System-lens review: '+tp[3],
    refined_findings:'Refined analysis: '+tp[2]+' '+tp[4],
    experiment_solver:{method:fr.pre+tp[1]+fr.post,findings:tp[2]},
    scholar_notes:'Signature version \u2014 scholar notes: '+tp[4],
    year:2026,source:'signature',_seed:seed,_cat:cat};
}
var KEYS=['id','signature_title','field','version','system_lens_review','refined_findings','experiment_solver','scholar_notes','year','source'];
function nonEmptyString(v){return typeof v==='string'&&v.length>0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  KEYS.forEach(function(k){if(r[k]===undefined||r[k]===null)e.push('missing:'+k);});
  Object.keys(r).forEach(function(k){if(KEYS.indexOf(k)<0&&k!=='_seed'&&k!=='_cat')e.push('extra:'+k);});
  if(!/^JAH-[a-z0-9-]+-S-\d{6}$/.test(r.id||''))e.push('id');
  if(!nonEmptyString(r.signature_title))e.push('signature_title');
  if(r.field!==FIELD)e.push('field');
  if(r.version!=='Signature')e.push('version');
  if(!nonEmptyString(r.system_lens_review))e.push('system_lens_review');
  if(!nonEmptyString(r.refined_findings))e.push('refined_findings');
  var es=r.experiment_solver;
  if(!es||typeof es!=='object'||!nonEmptyString(es.method)||!nonEmptyString(es.findings))e.push('experiment_solver');
  if(!nonEmptyString(r.scholar_notes))e.push('scholar_notes');
  if(r.year!==2026)e.push('year');
  if(r.source!=='signature')e.push('source');
  if(r._cat!==undefined&&CATS.indexOf(r._cat)<0)e.push('_cat');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){var s=sample[i];
    if(s&&s.id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-'+SLUG+'-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
