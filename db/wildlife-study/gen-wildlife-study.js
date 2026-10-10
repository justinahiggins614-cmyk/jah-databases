(function(){'use strict';
var SLUG="wildlife-study";
var FIELD="Wildlife and Natural Environments";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-wildlife-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Mammal ecology","survey mammal communities by sign, track, and live trapping, estimating density and range","body size predicts home range across mammals with remarkable consistency - energetics, not taxonomy, sets the scale","terrestrial framing; marine mammals follow different scaling","sign surveys find what traps miss"],["Bird migration","track migratory routes with banding and geolocators, linking breeding and wintering grounds","migration timing is shifting earlier with warming; long-distance migrants adjust slowest and suffer most","findings hold for temperate migrants; tropical systems differ","connect the breeding and wintering grounds"],["Marine mammals","identify individuals by photo-ID, building life histories from sighting records","photo-ID catalogs reveal population structure invisible to counts - individuals, not numbers, tell the demographic story","coastal-population framing; pelagic populations need different methods","every scar is data"],["Apex predators","monitor predator-prey dynamics through scat analysis and kill-site investigation","predator removal cascades down food webs; reintroduction reverses the cascade - trophic structure is top-down sensitive","findings hold in intact systems; fragmented landscapes dampen cascades","predators structure the ecosystem"],["Pollinators","survey flower-visitor networks, measuring visitation rates and pollen transfer","pollinator networks are nested: generalists anchor the system, specialists depend on them - losing generalists collapses the web","findings generalize; island networks are most fragile","generalists hold the network together"],["Wetland ecosystems","assess wetland function through hydrology, vegetation zonation, and waterfowl use","wetlands filter water, buffer floods, and store carbon simultaneously - no other ecosystem delivers three services at once","findings hold across wetland types; function scales with area and connectivity","hydrology is the master variable"],["Forest ecosystems","inventory forest structure by plot sampling, measuring succession and disturbance history","old-growth structure takes centuries to rebuild; second-growth forests differ in every structural dimension","temperate and tropical framing; boreal dynamics differ","structure tells the history"],["Desert adaptations","study water-conservation strategies across desert taxa, from physiology to behavior","desert life converges on the same solutions - nocturnality, water storage, and metabolic water - across unrelated lineages","findings hold for hot deserts; cold deserts add freezing to the challenge","convergence reveals the constraints"],["Wildlife corridors","map movement data against landscape resistance, identifying linkage zones","corridors work when animals actually use them - movement data, not models, validates the linkage","findings hold for wide-ranging species; sedentary species need different connectivity","animals vote with their feet"],["Endangered species recovery","track population trajectories against recovery plans, measuring threat reduction","threat removal drives recovery, not captive breeding alone - wild populations rebound when the killing stops","findings hold where habitat remains; extinct-in-the-wild cases differ","remove the threat first"],["Invasive species","map invasion fronts and impacts, testing control methods from mechanical to biological","early detection is the only cheap stage - established invasions cost orders of magnitude more to manage","findings generalize; island systems suffer the worst impacts","detect early or pay forever"],["Wildlife disease","surveillance-test populations for pathogens, modeling transmission and spillover risk","stress and crowding amplify disease; healthy, connected populations resist outbreaks better than any intervention","findings hold for density-dependent pathogens; vector-borne dynamics differ","population health is disease prevention"]];
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
