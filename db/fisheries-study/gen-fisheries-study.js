(function(){'use strict';
/* JAH Fisheries Signature Study Database — deterministic Signature study record generator. Property of Justin Addam Higgins (JAH). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-fisheries-study-S-";
var FIELD="Fisheries";
var SHORT="fisheries";
var TOPICS=["Salmon Smolt Survival Rates","Trawl Net Bycatch Reduction Devices","Oyster Reef Restoration","Tilapia Pond Stocking Density","Cod Spawning Stock Assessment","Shrimp Trawl Turtle Excluder Performance","Lake Trout Gillnet Selectivity","Mussel Aquaculture Rope Spacing","Crab Pot Escape Ring Sizing","River Fish Passage Design","Seaweed Farm Nutrient Uptake","Tuna Longline Hook Selectivity","Estuary Nursery Habitat Mapping","Fishmeal Replacement in Feeds","Ice Storage Catch Quality","Community Quota Compliance"];
var ANGLES=["a Signature study of harvest variables","controlled comparison across three fleets","multi-season monitoring","gear selectivity trials","standardized survey protocols compared","field validation of laboratory results","statistical modeling of stock response","yield-conservation trade-off analysis","habitat assessment","repeatability across regions"];
var METHODS=["trawl hauls were standardized to thirty-minute tows with catch weighed by species","acoustic surveys ran transect grids with trawl verification of marks","tagging programs released five thousand marked fish per cohort","gillnet fleets fished mesh sizes from fifty to one hundred fifty mm","water quality loggers recorded temperature and oxygen hourly at farm sites","underwater cameras documented gear behavior on every tenth tow","otoliths were sectioned for age reading on subsamples of two hundred fish","landing records were cross-checked against observer data for the full season"];
var FINDINGS=["Smolt survival to adult return reached {A}%, {B}% above the long-term mean.","Bycatch reduction devices cut non-target catch by {A}% with {B}% retention of target species.","Restored reefs reached {A}% oyster cover within {N} years of deployment.","Optimal stocking at {A} fish per cubic meter maximized growth and survival.","Spawning stock biomass estimated at {A}% of the target reference point.","Turtle excluders passed {A}% of turtles with shrimp loss under {B}%.","Selectivity trials showed {A}% of undersized trout escaped the {B} mm mesh.","Rope spacing at {A} cm maximized mussel yield per longline.","Escape rings at {A} mm released {B}% of sublegal crab.","Fish passage efficiency reached {A}% for target species at the Signature design."];
var TERMS=["stock assessment","bycatch","recruitment","spawning stock","mesh size","trawl","aquaculture","otolith","quota","nursery habitat","excluder","landing"];
var BOOKS=["Signature Fisheries Science: Assessment and Management","Fish Stock Assessment Manual","Aquaculture Production Systems","Fishing Gear Technology","Marine Habitat Restoration","Seafood Quality and Safety","Fisheries Economics","Fish Biology and Ecology"];
var QUALS=["Fisheries Biologist Certification","Aquaculture Technician Diploma","Fishing Vessel Skipper License","Fish Health Specialist","Observer Program Credential","Seafood Safety Certification","Marine Surveyor Qualification","Fisheries Manager"];
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
var gen={version:"jahdb-fisheries-study-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fisheries-study",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();