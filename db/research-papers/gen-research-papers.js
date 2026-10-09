/* ✳ JAH Research Paper Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) academic paper record generator: jahdb-research-papers-1.0 */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['cs','physics','biology','medicine','economics','engineering'];
var FIELD_NAME={cs:'Computer Science',physics:'Physics',biology:'Biology',medicine:'Medicine',economics:'Economics',engineering:'Engineering'};

var FIRST=['Aisha','Liam','Maya','Owen','Priya','Diego','Sofia','Kofi','Elena','Ravi','Nadia','Tariq','Ingrid','Marco','Yuki','Omar','Zara','Felix','Amara','Jonas','Leila','Victor','Anika','Hugo','Dana','Rafael','Mei','Kwame','Tessa','Ibrahim'];
var LAST=['Okafor','Bennett','Chen','Adeyemi','Kowalski','Rossi','Nguyen','Haddad','Larsen','Patel','Silva','Osei','Novak','Tanaka','Meyer','Ali','Costa','Weber','Rahman','Dubois','Kim','Farah','Lund','Garcia','Mensah','Khan','Ito','Petrov','Sato','Nakamura'];

var TOPICS={
cs:['neural network compression','federated learning convergence','graph neural architecture search','zero-shot program synthesis','differentially private training','transformer memory efficiency','neural program repair','retrieval-augmented reasoning'],
physics:['quantum error correction thresholds','turbulent plasma confinement','topological insulator transport','dark matter direct detection','high-temperature superconductivity','gravitational wave foregrounds','nonlinear optical lattices','spin liquid signatures'],
biology:['CRISPR off-target profiling','gut microbiome metabolomics','single-cell lineage tracing','protein folding kinetics','synthetic gene circuits','plant drought epigenetics','marine biodiversity eDNA','neural organoid development'],
medicine:['immunotherapy response biomarkers','early sepsis prediction','antibiotic stewardship outcomes','longitudinal diabetes remission','minimally invasive cardiac repair','neurodegeneration plasma markers','vaccine cold-chain logistics','postoperative delirium risk'],
economics:['labor market automation shocks','carbon pricing incidence','housing supply elasticity','central bank digital currencies','remittance corridor costs','gig worker wage dynamics','trade tariff pass-through','financial inclusion indices'],
engineering:['solid-state battery cycling','seismic retrofit composites','autonomous swarm coordination','microgrid islanding control','additive manufacturing tolerances','hydrogen pipeline embrittlement','soft robotic grasping','desalination membrane fouling']
};

var TITLE_T=[
'Advances in {t}: A Systematic Study',
'{t} Revisited: Theory and Practice',
'Toward Scalable {t}',
'A Novel Framework for {t}',
'On the Limits of {t}',
'Cross-Domain Analysis of {t}',
'{t}: Empirical Results and Open Problems',
'Robust Methods for {t}',
'Decoupling Complexity in {t}',
'A Longitudinal Study of {t}'
];
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}

var ABS_A=['This paper presents a comprehensive study of {t}.','We propose a new analytical framework for {t}.','This work revisits foundational assumptions behind {t}.','We examine the empirical landscape of {t} across recent literature.'];
var ABS_B=['Our method shows consistent gains on {m} independent benchmarks.','Experiments on {m} large-scale datasets demonstrate measurable improvements.','We validate the claims on {m} real-world experimental setups.','Ablation studies across {m} configurations confirm the main findings.'];
var ABS_C=['We discuss implications for practitioners and outline open problems.','Limitations and directions for future work are discussed in detail.','We close with open questions and a roadmap for future research.','Practical deployment considerations are examined throughout.'];
var ABS_D=['Results suggest the approach generalizes beyond the studied settings.','The findings challenge several widely held assumptions in the field.','Statistical significance is established through repeated trials.','The proposed metrics offer a sharper lens for future comparisons.'];

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var topic=cap(pick(rnd,TOPICS[cat]));
  var title=pick(rnd,TITLE_T).replace('{t}',topic);
  var nA=ri(rnd,2,4), authors=[], used={};
  for(var i=0;i<nA;i++){
    var ln;
    do{ ln=pick(rnd,LAST); }while(used[ln]); used[ln]=1;
    authors.push(pick(rnd,FIRST)+' '+ln);
  }
  var year=ri(rnd,1990,2026);
  var m=pick(rnd,['three','four','five','six']);
  var sents=[pick(rnd,ABS_A).replace('{t}',topic)];
  if(rnd()<0.9) sents.push(pick(rnd,ABS_B).replace('{m}',m));
  sents.push(pick(rnd,ABS_C));
  if(rnd()<0.5) sents.push(pick(rnd,ABS_D));
  var abstract=sents.join(' ');
  while(abstract.length>600&&sents.length>3){sents.pop();abstract=sents.join(' ');}
  var citations=ri(rnd,0,500);
  return {
    id:'JAH-PAPER-'+pad(seed),
    paper_id:'JAH-PAPER-'+pad(seed),
    title:title,
    authors:authors,
    year:year,
    field:cat,
    field_name:FIELD_NAME[cat],
    abstract:abstract,
    citation_count:citations,
    doi:'10.5555/jah.'+seed
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-PAPER-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.paper_id!=='string'||r.paper_id!==r.id)e.push('paper_id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(!Array.isArray(r.authors)||r.authors.length<2||r.authors.length>4||r.authors.some(function(a){return typeof a!=='string'||!a.length;}))e.push('authors');
  if(typeof r.year!=='number'||r.year<1990||r.year>2026||r.year!==Math.floor(r.year))e.push('year');
  if(CATS.indexOf(r.field)<0)e.push('field');
  if(typeof r.abstract!=='string'||r.abstract.length===0||r.abstract.length>600)e.push('abstract<=600');
  if(typeof r.citation_count!=='number'||r.citation_count<0||r.citation_count!==Math.floor(r.citation_count))e.push('citation_count');
  if(typeof r.doi!=='string'||!/^10\.5555\/jah\.\d+$/.test(r.doi))e.push('doi');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-research-papers-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-papers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
