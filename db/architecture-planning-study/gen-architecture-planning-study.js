(function(){'use strict';
/* JAH Architecture and Town Planning Signature Study Database — deterministic Signature study record generator. Property of Justin Addam Higgins (JAH). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-architecture-planning-study-S-";
var FIELD="Architecture and Town Planning";
var SHORT="architecture and town planning";
var TOPICS=["Passive Solar Orientation for Mid-Rise Housing","Urban Green Corridor Connectivity","Timber Frame Multi-Storey Fire Performance","Courtyard Housing Ventilation Modeling","Transit-Oriented Density Zoning","Heritage Facade Retrofit Insulation","Public Plaza Microclimate Comfort","Mixed-Use Street Section Design","Rain Garden Stormwater Sizing","Affordable Housing Unit Mix Analysis","Daylight Factor in Deep Floor Plates","Pedestrian Network Walkability Audits","Mass Timber Acoustic Separation","Urban Heat Island Mitigation Planting","Courtyard Microclimate Shading","Zoning Code Form-Based Calibration"];
var ANGLES=["a Signature study of design variables","controlled comparison across three districts","longitudinal post-occupancy evaluation","performance simulation and validation","standardized assessment protocols compared","field measurement of built outcomes","statistical modeling of comfort indices","cost-benefit analysis of interventions","environmental performance assessment","repeatability across building types"];
var METHODS=["computational fluid dynamics modeled airflow through courtyard typologies at three wind speeds","daylight simulations ran annual climate-based metrics across four orientations","post-occupancy surveys collected thermal comfort votes from residents over twelve seasons","thermal imaging mapped facade heat loss before and after retrofit on every elevation","pedestrian counts and intercept surveys were conducted at twenty intersections","stormwater models sized rain gardens for the hundred-year event with infiltration tested in situ","acoustic tests measured airborne and impact transmission across six mass timber assemblies","urban canopy surveys inventoried tree cover and surface temperatures block by block"];
var FINDINGS=["The Signature orientation cut cooling loads by {A}% while holding daylight factors above {B}%.","Courtyard schemes achieved {A} air changes per hour naturally, {B}% above the mechanical baseline.","Green corridor planting lowered peak surface temperatures by {A} degrees across {N} measured blocks.","Retrofit insulation cut facade heat loss by {A}% with payback inside {N} years.","Walkability scores rose {A} points where the Signature street section was built, across {N} audited routes.","Rain gardens captured {A}% of the design storm, verified in {N} monitored events.","Mass timber assemblies met acoustic class {A} with only {B} mm of added build-up.","Post-occupancy comfort votes reached {A}% satisfied, {B}% above comparable stock.","Daylight autonomy averaged {A}% in deep plates under the Signature reflector scheme.","Form-based calibration reduced variance applications by {A}% across {N} reviewed projects."];
var TERMS=["floor area ratio","setback","daylight factor","thermal mass","mixed-use","transit-oriented development","placemaking","envelope","biophilic design","permeability","density","streetscape"];
var BOOKS=["Signature Architecture: Design and Theory","Town Planning: Principles and Practice","Sustainable Urban Design Handbook","Building Construction Illustrated Companion","Urban Microclimate Design Guide","Housing Design Quality Standards","Landscape Architecture: Site Planning","Zoning and Land-Use Law Primer"];
var QUALS=["Licensed Architect","Chartered Town Planner","Urban Design Certificate","Sustainable Design Accreditation","Heritage Conservation Diploma","Housing Quality Assessor","Transport Planning Professional","Landscape Architecture License"];
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
var gen={version:"jahdb-architecture-planning-study-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("architecture-planning-study",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();