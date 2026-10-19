(function(){'use strict';
/* JAH Geothermal Power Systems Database generator — jahdb-geothermal-power-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GPS-";
var FIELDS=["resources", "drilling", "plant cycles", "reservoir engineering", "direct use", "enhanced systems"];
var TOPICS=[
    {t: "Geothermal Resources", b: "Hydrothermal systems at plate boundaries and hotspots: temperature, permeability, and fluid \u2014 the three requirements."},
    {t: "Exploration", b: "Geology, geochemistry (geothermometers), and geophysics (MT, gravity) find blind systems before drilling."},
    {t: "Drilling Geothermal Wells", b: "High-temperature, hard-rock, lost-circulation drilling: oilfield technology adapted to volcanic conditions."},
    {t: "Well Testing", b: "Flow tests measure deliverability (MW per well): the data that sizes the power plant."},
    {t: "Dry-Steam Plants", b: "The Geysers model: direct steam to turbine \u2014 simplest, limited to rare vapor-dominated fields."},
    {t: "Flash Plants", b: "High-pressure brine flashes to steam in separators: single, double, and triple flash squeezing more from the fluid."},
    {t: "Binary Plants", b: "Organic Rankine cycles harvest 100\u2013180\u00b0C resources: the technology unlocking moderate-temperature fields worldwide."},
    {t: "Reservoir Engineering", b: "Tracer tests, pressure monitoring, and numerical models manage the underground heat mine sustainably."},
    {t: "Induced Seismicity", b: "Injection triggers small quakes: traffic-light protocols and community engagement manage the risk."},
    {t: "Direct Use", b: "District heating, greenhouses, spas, industrial drying: using heat directly beats converting it at 10\u201315% efficiency."},
    {t: "Enhanced Geothermal (EGS)", b: "Fracking hot dry rock to create reservoirs anywhere: the technology that could make geothermal ubiquitous."},
    {t: "Economics", b: "High capex, low opex, 90%+ capacity factor: baseload renewables financed on resource certainty."}
];
var PRINCIPLES=[
    {n: "Temperature sets the technology", e: "", s: "Above ~180\u00b0C flash plants, below it binary cycles: the resource temperature picks the power plant."},
    {n: "Reservoir management is forever", e: "", s: "Sustainable extraction balances withdrawal against recharge: overpumping kills fields, as The Geysers learned."},
    {n: "Drilling is the cost", e: "", s: "Wells are 30\u201350% of project cost: drilling success rate is the project's risk profile."}
];
var USES=["Assessing geothermal resources", "Designing binary power plants", "Managing steamfield operations", "Planning EGS projects"];
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
    id:id, t:tp.t, g:field, name:"Geothermal Power Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Geothermal Power Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-geothermal-power-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-geothermal-power-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("geothermal-power-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
