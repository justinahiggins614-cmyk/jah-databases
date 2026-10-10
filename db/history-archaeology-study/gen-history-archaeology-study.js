(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-history-archaeology-study-S-";
var FIELD="History and Archaeology";
var TOPICS={"curriculum":["Ancient Mesopotamian civilizations","Classical Greece and Rome","Medieval Europe survey","Modern world history","Archaeological field methods"],"qualifications":["Archaeological excavation certification","Museum curation standards","Historical research methodology exams","Artifact conservation assessment","Heritage site management criteria"],"research":["Stratigraphy and dating techniques","Trade networks of the Bronze Age","Urbanization patterns in antiquity","Colonial archive analysis","Climate and civilizational change"],"findings":["Radiocarbon dating of settlement layers","Pottery typology sequences at dig sites","Ancient DNA and migration mapping","Shipwreck cargo manifest reconstruction","Census records and demographic shifts"],"methods":["Stratigraphic excavation","Radiocarbon and dendrochronology dating","Archival source criticism","GIS mapping of sites","Artifact conservation science"],"textbooks":["The Ancient World: A Comprehensive Survey","Archaeology: Methods and Theory","Medieval Europe: Sources and Society","Modernity and Its Discontents","Field Archaeology Manual"]};
var METHODS=["Stratigraphic excavation","Radiocarbon and dendrochronology dating","Archival source criticism","GIS mapping of sites","Artifact conservation science","Comparative site analysis","Numismatic study","Oral history collection"];
var ASPECTS=["primary source analysis","chronology construction","material culture study","historiography debates","oral history methods","archival research","field survey techniques","conservation practice"];
var MTPL=["A structured {field} inquiry into {topic}, documented step by step and independently reviewed against Signature scholarly standards.","Controlled comparative analysis of {topic} using {method}, with documented procedures, matched conditions, and blinded assessment.","Archival and field reconstruction of {topic}: primary sources gathered, cross-checked, and validated through {method}.","Longitudinal observation of {topic} over extended study windows, with {method} applied at each review checkpoint.","Experimental protocol applied to {topic}: hypothesis registered in advance, {method} executed, and results independently re-examined.","Systematic survey of {topic} combining quantitative measurement with qualitative review via {method}.","Multi-site inquiry into {topic}: {n3} teams applied {method} to {n1} cases and pooled the {aspect} logs.","Replication drive on {topic}: the original {method} protocol was re-run with {n1} fresh cases over {n2} weeks."];
var M2=["The {aspect} phase was carried out in full and logged step by step, so any Signature scholar can retrace the work.","Particular attention went to {aspect}, where the protocol required triple-checked measurements before filing.","A dedicated {aspect} pass confirmed the headline observations and ruled out the most likely confounds.","The study tracked {n1} cases over {n2} weeks, with {aspect} logged at every checkpoint.","Across {n3} independent {aspect} runs, the measures agreed within tight tolerance."];
var FTPL=["Primary finding: {topic} shows consistent, reproducible patterns when examined through {method}; the Signature-system review confirms internal coherence with established {field} scholarship.","Key result: repeated trials on {topic} converge on a stable outcome; variance across runs stays within the tolerance set by {method}, and the record is filed as a Signature version.","Finding: the evidence on {topic} supports the working hypothesis with clear margins; independent re-analysis using {method} reproduces the headline result.","Result: {topic} yields measurable, teachable regularities; the study documents procedures in full so future Signature scholars can replicate the work.","Conclusion: {topic} behaves in line with {field} theory while revealing new detail; the refined findings below supersede earlier provisional notes in this Signature record.","Outcome: {topic} produces actionable insight for practitioners; all measurements are preserved in this full Signature file for future study.","Headline: across {n1} {aspect} observations, {topic} shows an effect that survives every robustness check the {method} protocol requires.","Result: {n2} weeks of {method} work on {topic} moved the field forward; the {n3}-run {aspect} replication held firm."];
var F2=["A second line of evidence, drawn from {aspect}, points the same way and strengthens the conclusion.","The {aspect} record independently corroborates the main result, with deviations fully documented.","Practitioners should note the {aspect} implications: the study spells out what to do differently on Monday morning.","In the {n1}-case {aspect} sample, the effect held across {n2} subgroups with no reversals.","Follow-up work is scoped: the {aspect} questions left open are listed so future Signature scholars can take them up."];
var RTPL=["System-lens review: this Signature version of the {topic} study passed coherence, scope, and ethics checks; claims are internally consistent and aligned with {field} scholarly standards; approved for the Signature archive.","System-lens review: the {topic} record was examined for logical drift, scope creep, and unsupported claims; none found; the Signature version stands as filed.","System-lens review: methods, evidence, and conclusions on {topic} trace cleanly to the documented protocol; the study meets the Signature archive bar for {field}.","System-lens review: all {n1} {aspect} entries for {topic} were machine-checked for drift; the Signature version is clean.","System-lens review: the {n3}-analyst {method} panel on {topic} reached consensus; dissent, where it existed, is on file."];
var R2=["The {aspect} component was traced end to end; no drift, no unsupported leaps, no scope creep.","Cross-checks against neighboring {field} studies found the claims consistent and properly bounded.","All {n1} {aspect} observations were re-verified against the raw logs before filing.","Documentation depth was graded excellent: every number in this file can be traced to a logged observation."];
var NTPL=["Scholar notes: this Signature record treats {topic} as a living study object — future Signature scholars should extend, not overwrite, the findings filed here.","Scholar notes: the full procedure for {topic} is preserved in this file so the work can be audited end to end; no step is summarized away.","Scholar notes: {topic} connects naturally to neighboring studies in {field}; cross-linking is encouraged once those Signature records exist.","Scholar notes: the {n1}-case {aspect} dataset behind this {topic} study is the one future scholars should build on.","Scholar notes: {n2} weeks in, the {aspect} team on {topic} reports the protocol held; the log is worth reading in full."];
var N2=["On {aspect}, the record recommends starting small, measuring honestly, and scaling only what replicates.","The {aspect} notes are written for the next scholar, not the last one: open questions are flagged, not hidden.","With {n1} cases now on file, the {aspect} baseline for {field} is set; future studies should beat it, not redo it."];
var RFTPL=["Refined findings: after re-examination, the evidence on {topic} holds under {method}. Earlier provisional readings were tightened: effect boundaries are now explicit, exceptions are documented, and the full data trail is preserved in this Signature file.","Refined findings: the {topic} study was re-run against its own protocol. The headline result survives; two secondary observations were reclassified as contextual rather than general, and the record now states the limits plainly.","Refined findings: peer-style critique within the Signature system tested {topic} for overreach. The core finding stands; the surrounding claims were pruned to what the evidence supports, and the method trail ({method}) is fully documented.","Refined findings: with {n1} cases, the {topic} result is no longer provisional; the {aspect} breakdown is now the headline table in this Signature file.","Refined findings: the {n3}-team {method} replication of {topic} closed the last open question; the file now states the finding without qualification."];
var RF2=["The {aspect} analysis was re-run from raw notes and landed in the same place, which is why it stays in the file.","Limits are stated plainly: what the study does not cover on {aspect} is listed alongside what it does.","After {n2} weeks of re-checks, the {aspect} numbers moved by less than rounding error."];
function tpl(s,o){return s.split('{topic}').join(o.topic).split('{method}').join(o.method).split('{field}').join(o.field).split('{aspect}').join(o.aspect).split('{n1}').join(o.n1).split('{n2}').join(o.n2).split('{n3}').join(o.n3);}
function build(rnd,cat){
 var topic=pick(TOPICS[cat],rnd), method=pick(METHODS,rnd), aspect=pick(ASPECTS,rnd);
 var o={topic:topic,method:method,field:FIELD,aspect:aspect,n1:String(ri(rnd,50,5000)),n2:String(ri(rnd,2,52)),n3:String(ri(rnd,3,40))};
 var exM=tpl(pick(MTPL,rnd),o)+' '+tpl(pick(M2,rnd),o), exF=tpl(pick(FTPL,rnd),o)+' '+tpl(pick(F2,rnd),o);
 return {
  signature_title: topic+' \u2014 '+FIELD+' Signature study',
  g: cat,
  system_lens_review: tpl(pick(RTPL,rnd),o)+' '+tpl(pick(R2,rnd),o),
  refined_findings: tpl(pick(RFTPL,rnd),o)+' '+tpl(pick(RF2,rnd),o),
  experiment_solver: {method: exM, findings: exF},
  scholar_notes: tpl(pick(NTPL,rnd),o)+' '+tpl(pick(N2,rnd),o)
 };
}
function generate(seed,opts,rnd){
 opts=opts||{};rnd=rnd||prng(seed);
 var cat=opts.category||pick(CATS,rnd);
 var b=build(rnd,cat);
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,signature_title:b.signature_title,field:FIELD,version:'Signature',system_lens_review:b.system_lens_review,refined_findings:b.refined_findings,experiment_solver:b.experiment_solver,scholar_notes:b.scholar_notes,year:2026,source:'signature',g:cat,_seed:seed};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-[a-z0-9-]+-S-\d{6}$/.test(r.id||''))e.push('id');
 if(r.id!==PREFIX+String(r._seed).padStart(6,'0'))e.push('id_seed');
 if(typeof r.signature_title!=='string'||!r.signature_title.length)e.push('signature_title');
 if(r.field!==FIELD)e.push('field');
 if(r.version!=='Signature')e.push('version');
 if(typeof r.system_lens_review!=='string'||!r.system_lens_review.length)e.push('system_lens_review');
 if(typeof r.refined_findings!=='string'||!r.refined_findings.length)e.push('refined_findings');
 var es=r.experiment_solver;
 if(!es||typeof es.method!=='string'||!es.method.length||typeof es.findings!=='string'||!es.findings.length)e.push('experiment_solver');
 if(typeof r.scholar_notes!=='string'||!r.scholar_notes.length)e.push('scholar_notes');
 if(r.year!==2026)e.push('year');
 if(r.source!=='signature')e.push('source');
 if(CATS.indexOf(r.g)<0)e.push('g');
 return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-history-archaeology-study-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-archaeology-study",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
