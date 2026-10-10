(function(){'use strict';
var SLUG="earth-sciences-study";
var FIELD="Earth Sciences";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-earth-sciences-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Plate tectonics","map earthquake and volcano distributions against plate boundaries, reconstructing plate motion","seismic and volcanic belts trace plate edges so precisely that the theory was confirmed by geography alone","findings hold globally; intraplate features need mantle-plume explanations","boundaries explain the belts"],["Rock cycle","classify hand samples, then trace each rock type through the cycle's transformations","every rock is a temporary state - the cycle has no start and no end, only transformations","findings hold for the rock cycle; metamorphic grades add the pressure-temperature dimension","identify, then place in the cycle"],["Earthquakes","locate epicenters from seismograms, computing magnitude and assessing hazard","magnitude scales logarithmically - each whole number releases about thirty-two times the energy","findings hold for tectonic quakes; induced seismicity follows different statistics","logarithmic means exponential energy"],["Volcanoes","classify eruptions by style and products, linking explosivity to magma chemistry","silica content controls explosivity - the chemistry of the magma predicts the violence of the eruption","findings hold for magmatic eruptions; phreatic eruptions add groundwater","silica predicts the style"],["Weathering and erosion","measure weathering rates on exposed surfaces, separating chemical from mechanical processes","chemical weathering dominates in the tropics, mechanical at the poles - climate writes the weathering regime","findings hold for surface processes; the balance shifts with relief","climate sets the process"],["Ocean currents","track current systems and upwelling zones, linking circulation to climate and fisheries","upwelling zones cover a fraction of the ocean but feed most of its fisheries - circulation concentrates life","findings hold for eastern boundary systems; western intensification differs","follow the upwelling"],["Atmosphere layers","profile temperature, pressure, and composition with altitude, identifying each layer's role","the ozone layer's UV absorption creates the stratosphere's temperature inversion - chemistry structures the atmosphere","findings hold for Earth's atmosphere; other planets differ","temperature defines the layers"],["Geologic time","order strata by superposition and cross-cutting, calibrating with radiometric dates","radiometric dating and fossil succession agree independently - two clocks, one history","findings hold for the dated record; Precambrian resolution is coarser","two independent clocks agree"],["Mineralogy","identify minerals by hardness, cleavage, luster, and streak, confirming with crystal form","crystal structure determines physical properties - the internal order shows in every external trait","findings hold for crystalline minerals; amorphous materials differ","structure explains properties"],["Hydrology","budget a watershed's water, separating surface flow, groundwater, and evapotranspiration","groundwater moves slowly but stores most fresh water - the visible rivers are the small, fast fraction","findings hold for most watersheds; karst systems move water fast","groundwater is the reservoir"],["Glaciers","measure mass balance and flow rates, linking glacier change to climate signals","glaciers are climate instruments - their mass balance integrates temperature and precipitation into one record","findings hold for land ice; ice-sheet dynamics add complexity","mass balance is the climate signal"],["Natural hazards","assess hazard, exposure, and vulnerability for a region, computing risk scenarios","risk equals hazard times exposure times vulnerability - reducing any factor reduces risk, and exposure is often the lever","findings hold across hazard types; cascading hazards multiply","exposure is the lever"]];
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
