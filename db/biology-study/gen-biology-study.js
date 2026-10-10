(function(){'use strict';
var SLUG="biology-study";
var FIELD="Biology";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-biology-study-S-";
var ANGLES=["foundations","core principles","worked examples","case analysis","key experiments","historical development","modern applications","common misconceptions","assessment practice","advanced topics","comparative study","quantitative methods","conceptual overview","practical skills"];
var FRAMING={"curriculum":{"label":"Curriculum","pre":"Instructional design: ","post":" Lesson sequencing builds from definitions to applied analysis."},"qualifications":{"label":"Qualifications","pre":"Assessment design: ","post":" Mastery is measured by accurate application to unseen cases."},"research":{"label":"Research","pre":"Research protocol: ","post":" Results are cross-checked against established literature."},"findings":{"label":"Findings","pre":"Experimental approach: ","post":" Findings are reported with full method detail for replication."},"methods":{"label":"Methods","pre":"Methodological review: ","post":" Method choice is justified against alternatives."},"textbooks":{"label":"Textbooks","pre":"Pedagogical treatment: ","post":" Definitions, worked examples, and exercises reinforce the material."}};
var TOPICS=[["Cell theory","examine micrographs of plant and animal cells, identifying organelles and their functions","all cells share membrane, cytoplasm, and genetic material; the organelles are variations on a common plan","universal across known life; organelle detail varies by kingdom","draw the cell; labels fix the functions"],["Mendelian genetics","work monohybrid and dihybrid crosses with Punnett squares, predicting phenotypic ratios","the 3:1 and 9:3:3:1 ratios emerge reliably when genes assort independently - segregation and independent assortment hold as statistical laws","breaks down with linkage and epistasis; the laws are the baseline, not the whole story","always test the ratio with chi-square"],["Natural selection","simulate selection on trait distributions across generations, tracking allele frequencies","heritable variation plus differential reproduction shifts populations predictably; selection needs no guidance to produce adaptation","findings hold wherever replication with variation exists, including non-biological systems","fitness means reproductive success, not strength"],["Photosynthesis","trace energy from photon capture through the Calvin cycle to glucose, balancing the inputs","the light reactions' ATP and NADPH output exactly matches the Calvin cycle's demand - the two stages are stoichiometrically coupled","C3 pathway framing; C4 and CAM plants relocate the same chemistry","light reactions make the fuel; the Calvin cycle spends it"],["Ecosystem dynamics","map energy flow and nutrient cycling in a model ecosystem, quantifying trophic transfer","roughly ten percent of energy transfers between trophic levels; the pyramid of energy is the ecosystem's hard constraint","the 10% rule is approximate; real transfer efficiencies range 5-20%","follow the energy, not the biomass"],["Human physiology","trace a red blood cell through systemic and pulmonary circuits, noting gas exchange points","the double-circuit heart separates oxygenated and deoxygenated blood, enabling the metabolic rate warm-blooded life requires","mammalian framing; other vertebrates show the same pattern with variations","circuit diagrams beat memorization"],["Microbiology","culture and stain samples, classifying microbes by morphology, Gram reaction, and metabolism","Gram staining divides bacteria by cell-wall architecture, predicting antibiotic susceptibility better than shape alone","culture-based framing; most microbes are known only from DNA","Gram status first, then morphology"],["DNA replication","walk the replication fork, assigning each enzyme its role from helicase to ligase","semi-conservative replication is error-checked at every step; proofreading keeps mutation rates near one in a billion per base","prokaryotic framing; eukaryotic replication uses the same core machinery with more regulation","leading versus lagging strand is the key diagram"],["Immune system","follow an immune response from antigen presentation through clonal expansion to memory","clonal selection explains both specificity and memory: the body keeps the lymphocytes that worked","adaptive-immunity framing; innate immunity provides the constant backdrop","innate first, adaptive second, memory last"],["Taxonomy","classify specimens through the hierarchy from domain to species using diagnostic traits","phylogenetic trees built from DNA match morphological trees far more often than chance - common descent is written in the genomes","findings hold for the tree of life; horizontal gene transfer complicates prokaryote branches","shared derived traits define the clades"],["Developmental biology","track embryonic development from zygote through gastrulation, mapping germ layers to organs","the same signaling pathways pattern embryos across phyla; development is deeply conserved","model-organism framing; vertebrate patterns generalize best","gastrulation is the most important event in your life"],["Conservation biology","assess population viability from census data, identifying minimum viable population sizes","fragmented populations below effective size lose genetic diversity within generations; connectivity is as important as area","findings generalize; island systems show the effects most sharply","corridors matter as much as reserves"]];
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
