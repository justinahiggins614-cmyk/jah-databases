(function(){'use strict';
var SLUG="law-study";
var FIELD="Law";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-law-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Constitutional law","compare constitutional text with landmark rulings, tracing how courts interpret rights and powers","judicial review concentrates interpretive power in courts, making precedent the practical constitution alongside the written text","findings hold across common-law systems; civil-law constitutions rely more on codified amendment","start with the bill of rights, then separation of powers"],["Contract formation","apply offer, acceptance, and consideration tests to sample agreements, flagging missing elements","most contract disputes turn on whether acceptance mirrored the offer - the mirror-image rule decides the majority of cases","consistent across commercial systems; consumer protections add statutory overlays","consideration need not be adequate, only sufficient"],["Tort negligence","work through duty, breach, causation, and damages on fact patterns, applying the reasonable-person standard","causation - not duty - is where negligence claims most often fail; foreseeability bounds the duty in practice","doctrine is stable; damage caps and no-fault schemes vary by jurisdiction","learn duty before breach; duty is the gatekeeper"],["Criminal procedure","map each investigative step to its constitutional safeguard, from stop-and-frisk to trial","exclusionary rules shape police behavior more than any training manual; procedure is the real constraint on state power","adversarial-system framing; inquisitorial systems reach similar safeguards by different routes","always pair the rule with its remedy"],["Property rights","classify interests in land and chattels, then test transfer and encumbrance scenarios","the bundle-of-rights model explains modern property better than ownership absolutism; rights are divisible and layered","holds in market economies; customary tenure systems need local qualification","estates in land repay careful diagramming"],["Administrative law","trace a regulation from enabling statute through notice, comment, and judicial review","deference doctrines decide most administrative challenges; who interprets the statute matters more than the statute's text","findings generalize within presidential systems; parliamentary systems differ in review intensity","deference is the load-bearing concept"],["Law of evidence","test admissibility of sample exhibits against relevance, hearsay, and privilege rules","hearsay exceptions swallow the rule in practice; most out-of-court statements enter through an exception","adversarial-trial framing; bench-trial systems apply the same logic with less formality","relevance first, then exceptions, then exclusion"],["International law","trace treaty obligations from signature through ratification to domestic enforcement","compliance rests on reciprocity and reputation, not enforcement; states obey treaties because violation costs future cooperation","findings hold for multilateral treaties; bilateral compliance dynamics differ","distinguish hard law from soft law early"],["Corporate governance","analyze board duties, shareholder rights, and disclosure obligations in model company scenarios","fiduciary duty of care is enforced lightly, loyalty strictly; courts punish self-dealing, not bad business judgment","applies to widely held corporations; closely held firms follow different dynamics","the business judgment rule is the hinge"],["Intellectual property","compare patent, copyright, and trademark protection on a single product's features","IP regimes reward disclosure with temporary monopoly; the bargain works best where the disclosure is genuinely enabling","international treaties set the global floor; national doctrines vary above it","idea-expression divide is the first principle"],["Civil rights law","follow a discrimination claim from protected class through burden-shifting to remedy","burden-shifting frameworks decide cases before trial; the prima facie case is the real battleground","findings rooted in statutory anti-discrimination systems; constitutional equality doctrines parallel them","burden-shifting order matters more than the doctrine's name"],["Legal research methods","run a research trail from secondary sources to statutes to cases, validating currency with citators","currency checking catches reversed authority that keyword search misses; it is the highest-value research step","method is system-agnostic; databases differ but the hierarchy of authority is constant","secondary sources first, always"]];
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
