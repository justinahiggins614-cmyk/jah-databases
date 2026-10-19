(function(){'use strict';
/* JAH Solar Farm Design Database generator — jahdb-solar-farm-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SFD-";
var FIELDS=["site assessment", "array layout", "inverters", "transformers", "interconnection", "yield modeling"];
var TOPICS=[
    {t: "Site Selection", b: "Irradiance (GHI/DNI), land, slope, floodplain, environmental review, and proximity to transmission: the fatal-flaw checklist."},
    {t: "Solar Resource Assessment", b: "TMY data, pyranometers, and satellite models: quantifying the fuel before spending millions."},
    {t: "Fixed-Tilt vs Tracking", b: "Single-axis trackers add 15\u201325% energy at higher cost and complexity: latitude and land cost decide."},
    {t: "Row Spacing and Shading", b: "Ground-cover ratio trades land use against inter-row shading losses: the geometry of the field."},
    {t: "Module Technology", b: "Mono PERC, TOPCon, HJT, bifacial: efficiency, temperature coefficient, and degradation rates compared."},
    {t: "Inverter Architectures", b: "Central vs string vs micro: fault tolerance, MPPT granularity, and O&M access traded at megawatt scale."},
    {t: "Collection and Substation", b: "34.5-kV collection, pad-mount transformers, and the substation stepping up to transmission voltage."},
    {t: "Interconnection Process", b: "Utility queues, system-impact studies, and upgrade costs: the bureaucratic physics of connecting gigawatts."},
    {t: "Yield Modeling", b: "PVsyst energy models with soiling, mismatch, wiring, inverter, transformer, and availability losses \u2014 P50/P90 for finance."},
    {t: "Soiling and Cleaning", b: "Dust cuts output 5\u201325% in arid sites: robotic vs manual cleaning economics per soiling station data."},
    {t: "O&M", b: "Monitoring, preventive maintenance, vegetation, and inverter replacement reserves: the 25-year operations plan."},
    {t: "Decommissioning and Recycling", b: "End-of-life module recycling and land restoration: the plan lenders now require up front."}
];
var PRINCIPLES=[
    {n: "Yield is modeled, not guessed", e: "", s: "Irradiance data, soiling, temperature, and losses combine in PVsyst-class models: bankable numbers or no financing."},
    {n: "Interconnection is the gate", e: "", s: "Utility studies (feasibility \u2192 impact \u2192 facilities) set cost and timeline: the queue decides the project."},
    {n: "DC/AC ratio is an optimization", e: "", s: "Oversizing panels relative to inverters clips midday peaks but harvests mornings and evenings: economics picks the ratio."}
];
var USES=["Laying out utility arrays", "Modeling project yield", "Planning interconnection", "Managing solar O&M"];
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
    id:id, t:tp.t, g:field, name:"Solar Farm Design"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Solar Farm Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-solar-farm-design-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-solar-farm-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("solar-farm-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
