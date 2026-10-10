(function(){'use strict';
var SLUG="environmental-sciences-study";
var FIELD="Environmental Sciences";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-environmental-sciences-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Climate systems","analyze radiative forcing components, separating greenhouse gases, aerosols, and albedo effects","CO2 dominates long-term forcing; aerosols mask warming on short timescales - the net signal is unambiguous","global-model framing; regional projections carry wider uncertainty","forcing in, response out"],["Carbon cycle","track carbon through atmosphere, biosphere, and oceans, quantifying fluxes and reservoirs","the ocean and land each absorb roughly a quarter of anthropogenic CO2 - natural sinks currently offset half of emissions","contemporary framing; paleo records show the cycle's slower modes","fluxes matter more than stocks"],["Water cycle","balance precipitation, evapotranspiration, and runoff for a watershed, testing closure","most precipitation returns to the atmosphere through plants - transpiration, not direct evaporation, dominates the land water budget","watershed framing; arid systems shift the balance toward evaporation","follow the water uphill"],["Biodiversity loss","measure species richness and extinction rates against background rates from the fossil record","current extinction rates exceed background by orders of magnitude - the sixth mass extinction is measurable in the data","findings hold across taxa; insects show the steepest documented declines","rates, not anecdotes"],["Pollution and remediation","sample contaminated media, identify pollutant pathways, and test remediation technologies","source control outperforms cleanup at every scale; remediation costs rise exponentially with delay","findings generalize; persistent pollutants resist all remediation","prevent first, remediate second"],["Renewable energy","compare energy return on investment across solar, wind, hydro, and geothermal systems","EROI above roughly 7:1 sustains modern society; most renewables clear the bar, with wind and hydro highest","grid-scale framing; storage costs shift the economics","EROI is the real metric"],["Environmental policy","evaluate policy instruments - taxes, caps, standards - against emissions outcomes","price instruments achieve reductions cheapest; standards achieve them most predictably - the tradeoff is cost versus certainty","market-economy framing; command economies reach the same outcomes differently","incentives move faster than mandates"],["Soil science","profile soil horizons, measuring texture, organic matter, and nutrient status","a single teaspoon of healthy soil holds more microbes than people on Earth - soil biology, not chemistry, limits fertility","temperate-agriculture framing; tropical soils follow different nutrient logic","biology first, chemistry second"],["Atmospheric chemistry","track ozone formation and destruction cycles, separating natural from anthropogenic drivers","the Montreal Protocol worked: stratospheric chlorine is falling and the ozone hole is recovering - policy can fix atmospheric chemistry","findings hold for the stratosphere; tropospheric ozone remains a pollution problem","catalysis multiplies the damage"],["Waste management","audit waste streams by composition, then model diversion through reduce, reuse, and recycle","organic waste dominates landfill methane; composting and capture cut the largest single waste emission","municipal framing; industrial waste follows different economics","organics first"],["Sustainable agriculture","compare input intensity against yield and soil health across farming systems","precision agriculture cuts inputs without cutting yield - information substitutes for chemicals","findings hold where capital and connectivity exist; smallholder systems need adapted versions","measure the soil, not just the harvest"],["Environmental impact assessment","scope a project assessment, identifying significant effects and mitigation hierarchies","the mitigation hierarchy decides outcomes: avoid, then minimize, then restore, then offset - offsets work worst","regulatory framing; the hierarchy is recognized internationally","avoid beats offset every time"]];
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
