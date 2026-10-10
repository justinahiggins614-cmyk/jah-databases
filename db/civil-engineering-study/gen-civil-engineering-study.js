(function(){'use strict';
/* JAH Building and Civil Engineering Signature Study Database — deterministic Signature study record generator. Property of Justin Addam Higgins (JAH). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-civil-engineering-study-S-";
var FIELD="Building and Civil Engineering";
var SHORT="civil engineering";
var TOPICS=["Reinforced Concrete Beam Shear Capacity","Asphalt Pavement Rutting Resistance","Bridge Deck Waterproofing Systems","Soil Compaction for Embankments","Prestressed Girder Camber Control","Storm Drain Hydraulic Capacity","Retaining Wall Drainage Design","Concrete Curing Regime Strength Gain","Steel Connection Bolt Preload","Pavement Subgrade Modulus Testing","Tunnel Lining Segment Gaskets","Flood Levee Seepage Control","High-Strength Concrete Shrinkage","Guardrail Impact Performance","Pile Foundation Load Testing","Construction Joint Waterstops"];
var ANGLES=["a Signature study of construction variables","controlled comparison across three sites","long-term structural monitoring","failure investigation and analysis","standardized test protocols compared","field validation of laboratory results","statistical modeling of capacity","cost-durability trade-off analysis","service-life assessment","repeatability across contractors"];
var METHODS=["load tests applied incremental static loads to full-scale specimens with deflection recorded at midspan","nuclear density gauges verified compaction at thirty locations per lift","concrete cylinders were cured under three regimes and crushed at 7, 28, and 90 days","falling weight deflectometer surveys mapped pavement response at twenty-five meter intervals","pile integrity testing used low-strain dynamic methods on every tenth pile","hydraulic models were calibrated against flow gauges during eight storm events","bolt preload was verified by turn-of-nut inspection with torque checks on a sample","strain gauges embedded in the deck logged seasonal movement for two full years"];
var FINDINGS=["The Signature curing regime lifted 28-day strength by {A}% over standard practice, verified on {N} pours.","Shear capacity exceeded code predictions by {A}% across {B} tested beams.","Rutting depth after {N} million axle passes measured {A} mm, {B}% below the control section.","Pile settlement under twice the working load stayed under {A} mm in {B}% of tests.","Subgrade modulus averaged {A} MPa, supporting a {B}% thinner pavement design.","Waterproofing membranes survived {A} freeze-thaw cycles with zero adhesion loss.","Embankment settlement stabilized within {A} mm after {N} months of surcharge.","Bolt preload retention measured {A}% after {N} years in service.","Levee seepage gradients held at {A}% of the critical value through the design flood.","Guardrail deflection met test level {A} with occupant risk scores {B}% under limits."];
var TERMS=["bearing capacity","shear","deflection","compaction","slump","curing","prestress","camber","subgrade","retaining","hydraulic gradient","serviceability"];
var BOOKS=["Signature Civil Engineering: Analysis and Design","Reinforced Concrete: Mechanics and Design","Pavement Engineering Principles","Structural Steel Design Handbook","Geotechnical Engineering: Principles","Bridge Engineering Handbook","Hydraulics for Civil Engineers","Construction Materials: Testing and Specification"];
var QUALS=["Professional Engineer License","Structural Design Certification","Geotechnical Specialist Diploma","Highway Engineering Certificate","Bridge Inspection Qualification","Construction Manager Credential","Concrete Technologist License","Water Resources Engineer"];
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function fill(s,A,B,N){return s.split("{A}").join(A).split("{B}").join(B).split("{N}").join(N);}
function pickN(r,pool,n){var p=pool.slice(),o=[];for(var i=0;i<n&&p.length;i++){o.push(p.splice((r()*p.length)|0,1)[0]);}return o;}
function build(rnd,cat){
  var topic=pick(TOPICS,rnd),angle=pick(ANGLES,rnd);
  var _tt=pickN(rnd,TERMS,3),t1=_tt[0],t2=_tt[1],t3=_tt[2];
  var bk=pick(BOOKS,rnd),q=pick(QUALS,rnd),m=pick(METHODS,rnd);
  var A=ri(rnd,12,68),B=ri(rnd,75,99),N=ri(rnd,3,12);
  var _ff=pickN(rnd,FINDINGS,2);
  var f1=fill(_ff[0],A,B,N),f2=fill(_ff[1],A,B,N);
  var title=topic+": "+angle;
  return {
    signature_title:title,
    field:FIELD,
    version:"Signature",
    system_lens_review:"System-lens review of the Signature version. The study \""+title+"\" was examined for scope, rigor, and curriculum fit. Reviewers confirmed the "+cat+" coverage meets Signature standards, with "+t1+" and "+t2+" treated at professional depth. This record is approved as the Signature version for the "+SHORT+" archive.",
    refined_findings:f1+" Across "+N+" independent replicates, results held within "+B+"% of the reported means, confirming the Signature procedure as the recommended practice.",
    experiment_solver:{method:cap(m)+". All work followed the Signature "+SHORT+" methods protocol for the "+cat+" category.",findings:f2+" The Experiment Solver flags this result as field-ready and reproducible."},
    scholar_notes:"Scholar notes for teaching and qualification. Key terms: "+t1+", "+t2+", "+t3+". Recommended text: "+bk+". Aligns with the "+q+" and the "+cat+" curriculum strand.",
    year:2026,
    source:"signature"
  };
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  if(CATS.indexOf(cat)<0)cat=pick(CATS,rnd);
  var r=build(rnd,cat);
  r.id=PREFIX+String(seed).padStart(6,'0');
  r._seed=seed;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-[a-z0-9-]+-S-\d{6}$/.test(r.id||''))e.push('id');
  else if(String(r.id).indexOf(PREFIX)!==0)e.push('id-prefix');
  if(typeof r.signature_title!=='string'||!r.signature_title.length)e.push('signature_title');
  if(r.field!==FIELD)e.push('field');
  if(r.version!=="Signature")e.push('version');
  if(typeof r.system_lens_review!=='string'||r.system_lens_review.indexOf('Signature version')<0)e.push('system_lens_review');
  if(typeof r.refined_findings!=='string'||!r.refined_findings.length)e.push('refined_findings');
  var es=r.experiment_solver;
  if(!es||typeof es.method!=='string'||!es.method.length||typeof es.findings!=='string'||!es.findings.length)e.push('experiment_solver');
  if(typeof r.scholar_notes!=='string'||!r.scholar_notes.length)e.push('scholar_notes');
  if(r.year!==2026)e.push('year');
  if(r.source!=="signature")e.push('source');
  return{ok:!e.length,errors:e};
}
var gen={version:"jahdb-civil-engineering-study-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("civil-engineering-study",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();