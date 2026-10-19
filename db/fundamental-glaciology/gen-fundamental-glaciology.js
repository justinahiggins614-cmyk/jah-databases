(function(){'use strict';
/* JAH Fundamentals of Glaciology Database generator — jahdb-fundamental-glaciology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GLA-";
var FIELDS=["ice physics", "glacier flow", "mass balance", "ice sheets", "sea ice", "glacial hazards"];
var TOPICS=[
    {t: "What Glaciers Are", b: "Rivers of ice: snow compacts to firn to ice, then flows downhill under its own weight \u2014 glaciers are defined by motion."},
    {t: "Ice Crystal Physics", b: "Ice Ih's hexagonal lattice, pressure melting, and regelation give ice its slipperiness and flow behavior."},
    {t: "Glen's Flow Law", b: "Ice creeps as a nonlinear viscous fluid: double the stress, get eight times the strain rate \u2014 the constitutive law of glaciology."},
    {t: "Basal Sliding", b: "Meltwater at the bed lubricates glaciers; sliding can dominate motion, and its physics controls surges and ice-stream speed."},
    {t: "Mass Balance", b: "Stake networks and snow pits measure winter gain vs summer loss: the direct vital sign of glacier health."},
    {t: "Glacier Advance and Retreat", b: "Terminus position lags climate: response times run years for small glaciers to millennia for ice sheets."},
    {t: "Ice Sheets: Greenland and Antarctica", b: "Continental ice up to 4 km thick holds ~65 m of sea-level equivalent \u2014 their dynamics set coastlines' futures."},
    {t: "Ice Shelves and Buttressing", b: "Floating shelves hold back inland ice; their collapse (Larsen B) accelerates glaciers behind them."},
    {t: "Sea Ice", b: "Frozen ocean (not land ice) doesn't raise seas when melting, but its bright surface controls polar climate via albedo feedback."},
    {t: "Glacial Landforms", b: "U-valleys, moraines, drumlins, and fjords are ice's signature on landscapes \u2014 reading them reconstructs past ice ages."},
    {t: "Ice Cores: Climate Archives", b: "Layered ice traps ancient air: bubbles and isotopes reconstruct temperature and CO\u2082 across 800,000 years."},
    {t: "Glacial Hazards", b: "Outburst floods (j\u00f6kulhlaups), surging glaciers, and calving icebergs threaten downstream communities and shipping."}
];
var PRINCIPLES=[
    {n: "Glen's flow law", e: "\u03b5\u0307 = A\u00b7\u03c4^n (n \u2248 3)", s: "Ice deforms as a power-law fluid: strain rate rises with the cube of stress."},
    {n: "Mass balance", e: "B = accumulation \u2212 ablation", s: "A glacier grows or shrinks by the difference between snowfall gained and melt lost."},
    {n: "Sea-level equivalence", e: "360 Gt ice \u2248 1 mm sea level", s: "A gigatonne of lost land ice raises global seas by about 1/360 of a millimeter."}
];
var USES=["Projecting sea-level rise", "Assessing glacial flood hazards", "Interpreting ice-core climate records", "Monitoring glacier retreat"];
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
    id:id, t:tp.t, g:field, name:"Glaciology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Glaciology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-glaciology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-glaciology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-glaciology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
