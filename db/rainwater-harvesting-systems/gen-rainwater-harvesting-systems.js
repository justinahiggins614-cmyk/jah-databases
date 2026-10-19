(function(){'use strict';
/* JAH Rainwater Harvesting Systems Database generator — jahdb-rainwater-harvesting-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RHS-";
var FIELDS=["catchment", "conveyance", "storage", "treatment", "plumbing integration", "codes"];
var TOPICS=[
    {t: "Why Harvest Rain", b: "Stormwater reduction, water independence, and quality: the motivations from homestead to commercial building."},
    {t: "Catchment Surfaces", b: "Metal roofs are ideal (clean, efficient); asphalt shingles and treated wood raise quality questions \u2014 material matters."},
    {t: "Rainfall Yield", b: "Area \u00d7 rainfall \u00d7 runoff coefficient (0.8\u20130.95): the simple math sizing every system."},
    {t: "Gutters and Conveyance", b: "Sizing for cloudburst intensity, leaf screening, and freeze protection: getting water to the tank."},
    {t: "First-Flush Diverters", b: "Automatically discarding the first dirty runoff: diverters, and why they need maintenance."},
    {t: "Storage Tanks", b: "Polyethylene, concrete, steel: below vs above ground, light exclusion (algae), and access for cleaning."},
    {t: "Treatment Trains", b: "Sediment filtration, carbon, UV, chlorination: matching treatment to potable vs non-potable use."},
    {t: "Pumps and Pressure", b: "Demand pumps with pressure tanks vs gravity: delivering harvested water like municipal supply."},
    {t: "Plumbing Integration", b: "Dual plumbing, backflow prevention (RPZ), and purple pipe: safely tying rainwater into buildings."},
    {t: "Codes and Permits", b: "Varying by state and country: some mandate, some restrict \u2014 the legal landscape of rainwater."},
    {t: "Maintenance", b: "Gutter cleaning, tank inspection, filter changes: the chores that keep systems working for decades."},
    {t: "Economics", b: "Water rates vs system cost: payback in high-rate areas, resilience value everywhere."}
];
var PRINCIPLES=[
    {n: "Size storage to the dry spell", e: "", s: "Tank volume bridges the longest expected dry period at the demand rate: rainfall statistics size the cistern."},
    {n: "First flush protects quality", e: "", s: "Diverting the dirty first millimeters keeps bird droppings and dust out of storage: simple, essential."},
    {n: "Treat to the use", e: "", s: "Irrigation needs screening; potable needs filtration plus disinfection: treatment matches the exposure."}
];
var USES=["Sizing residential cisterns", "Designing commercial systems", "Treating harvested rainwater", "Navigating local codes"];
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
    id:id, t:tp.t, g:field, name:"Rainwater Harvesting Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Rainwater Harvesting Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-rainwater-harvesting-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-rainwater-harvesting-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("rainwater-harvesting-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
