(function(){'use strict';
var SLUG="biochemistry-study";
var FIELD="Biochemistry";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-biochemistry-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Amino acids and proteins","classify the twenty amino acids by side-chain chemistry, then predict folding behavior","side-chain chemistry determines everything downstream: hydrophobic cores, salt bridges, and active-site geometry all follow from it","standard-code framing; rare noncanonical amino acids extend the set","learn the one-letter codes early"],["Enzyme kinetics","plot reaction rates against substrate concentration, extracting Km and Vmax from the curve","Michaelis-Menten kinetics fits most enzymes; deviations diagnose allostery or cooperativity","in-vitro framing; cellular conditions complicate the picture","Km is affinity in disguise"],["Glycolysis","balance each of the ten steps, tracking ATP investment against payoff","glycolysis nets two ATP but its real product is pyruvate and NADH - the payoff phase exists to feed the mitochondria","universal pathway; regulated steps differ by organism","investment phase then payoff phase"],["Citric acid cycle","follow acetyl-CoA through the cycle, accounting for every CO2, NADH, and FADH2","the cycle's eight steps turn once per acetyl-CoA, extracting high-energy electrons rather than ATP directly","aerobic framing; the cycle runs partially in anaerobes","count the electron carriers, not the ATP"],["Oxidative phosphorylation","trace electron flow down the transport chain, mapping proton pumping to ATP synthesis","the chemiosmotic mechanism unifies respiration: electron flow builds the gradient, ATP synthase spends it","mitochondrial framing; bacteria run the same chemistry on membranes","the gradient is the battery"],["DNA replication biochemistry","assign each replisome protein its chemistry: unwinding, priming, synthesis, proofreading","the replisome couples unwinding to synthesis so tightly that the fork never exposes vulnerable single strands","findings generalize; archaeal and eukaryotic replisomes add regulatory layers","processivity is the design problem"],["Membrane lipids","model bilayer assembly from phospholipid geometry, predicting permeability and fluidity","membrane fluidity is actively regulated - cells remodel their lipids to hold the bilayer at working viscosity","findings hold for cellular membranes; archaeal ether lipids are the exception","the hydrophobic effect builds the bilayer"],["Signal transduction","map a hormone signal from receptor through second messengers to cellular response","cascades amplify: one receptor activates many enzymes, each activating many more - amplification is the point of the cascade","GPCR framing; other receptor classes use the same logic","follow the amplification"],["Protein folding","predict folding outcomes from sequence, identifying chaperone-dependent steps","folding funnels explain speed: proteins fold in milliseconds because the energy landscape guides every step downhill","findings hold for small domains; large proteins need chaperone machinery","misfolding causes disease; folding is destiny"],["Carbohydrate metabolism","connect glycogen storage, gluconeogenesis, and glycolysis through their shared intermediates","reciprocal regulation prevents futile cycles - the liver never runs glycolysis and gluconeogenesis at full speed together","mammalian framing; the logic generalizes to all heterotrophs","reciprocal regulation is the theme"],["Bioenergetics","compute free-energy changes for coupled reactions, testing thermodynamic feasibility","ATP's hydrolysis energy drives unfavorable reactions by coupling - life runs on energy transfer, not energy creation","universal principle; actual delta-G values are condition-dependent","couple the reactions, don't memorize the numbers"],["Vitamins and coenzymes","match each B-vitamin to its coenzyme form and the reactions that depend on it","coenzyme deficiencies produce the vitamin-deficiency diseases directly - each classic deficiency maps to a stalled enzyme","human-nutrition framing; microbial coenzyme use is broader","one vitamin, one coenzyme, one reaction class"]];
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
