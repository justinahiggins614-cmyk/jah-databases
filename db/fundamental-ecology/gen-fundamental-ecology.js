(function(){'use strict';
/* JAH Fundamentals of Ecology Database generator — jahdb-fundamental-ecology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ECO-";
var FIELDS=["populations", "communities", "ecosystems", "biomes", "conservation", "field methods"];
var TOPICS=[
    {t: "Levels of Organization", b: "Organism \u2192 population \u2192 community \u2192 ecosystem \u2192 biosphere: ecology studies every level and the links between them."},
    {t: "Population Growth", b: "Exponential when resources are endless, logistic when they aren't: r/K selection describes life-history strategies."},
    {t: "Life Tables and Survivorship", b: "Age-specific birth and death schedules predict population futures \u2014 the demography behind wildlife management."},
    {t: "Competition", b: "Interspecific competition excludes (competitive exclusion principle) or partitions niches \u2014 character displacement is evolution's answer."},
    {t: "Predation and Herbivory", b: "Predators shape prey behavior, numbers, and evolution; trophic cascades (wolves \u2192 elk \u2192 aspen) show top-down control."},
    {t: "Symbiosis", b: "Mutualism, commensalism, parasitism: the spectrum of living together, from mycorrhizae to malaria."},
    {t: "Succession", b: "Communities assemble predictably after disturbance: pioneers \u2192 intermediates \u2192 climax \u2014 ecology's directional change."},
    {t: "Energy Flow", b: "Lindeman's 10% rule: each trophic level keeps roughly a tenth of the energy \u2014 why food chains stay short and meat costs more."},
    {t: "Nutrient Cycles", b: "Carbon, nitrogen, and phosphorus cycle through biotic and abiotic pools; humans have doubled nitrogen fixation with consequences."},
    {t: "Biomes", b: "Climate sorts life into tundra, taiga, grassland, desert, rainforest: temperature and rainfall predict the vegetation."},
    {t: "Biodiversity Science", b: "Species richness, evenness, and endemism quantify variety; hotspots concentrate conservation value."},
    {t: "Conservation Biology", b: "Minimum viable populations, corridors, and reserve design turn ecological theory into species survival."}
];
var PRINCIPLES=[
    {n: "Logistic growth", e: "dN/dt = rN(1 \u2212 N/K)", s: "Populations grow exponentially until carrying capacity K brakes them."},
    {n: "Lotka-Volterra", e: "predator-prey cycles", s: "Coupled equations produce the oscillating dynamics of eaters and eaten."},
    {n: "Species-area", e: "S = c\u00b7A^z", s: "Larger areas hold more species by a power law \u2014 the quantitative basis of reserve design."}
];
var USES=["Managing wildlife populations", "Designing nature reserves", "Restoring degraded habitats", "Assessing environmental impact"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Ecology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Ecology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-ecology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-ecology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-ecology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
