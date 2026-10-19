(function(){'use strict';
/* JAH Railway Electrification Database generator — jahdb-railway-electrification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RE-";
var FIELDS=["catenary", "substations", "traction power", "rolling stock", "signaling interfaces", "economics"];
var TOPICS=[
    {t: "Why Electrify", b: "Energy efficiency, acceleration, emissions, maintenance: the case that keeps converting diesel lines."},
    {t: "System Voltages", b: "25 kV 50/60 Hz AC (modern standard), 15 kV 16.7 Hz (Germanic), 3 kV/1.5 kV DC (legacy), third rail: history's menu."},
    {t: "Catenary Design", b: "Contact wire, messenger, droppers, tensioning: keeping the wire at constant height and stagger at 300 km/h."},
    {t: "Traction Substations", b: "Grid to railway: transformers, breakers, and autotransformer (2\u00d725 kV) feeds extending substation spacing."},
    {t: "Power Quality", b: "Harmonics, unbalance, and voltage drop: railways as demanding grid customers."},
    {t: "Electric Locomotives", b: "Transformers, converters, and traction motors: the power chain from pantograph to wheel."},
    {t: "Multiple Units", b: "Distributed traction in EMUs: acceleration and capacity advantages reshaping passenger service."},
    {t: "Signaling Compatibility", b: "Traction return currents vs track circuits: immunized signaling and bonding plans prevent interference."},
    {t: "Phase Breaks", b: "Neutral sections between grid phases: coasting through the gaps in electrified networks."},
    {t: "Battery and Hydrogen Alternatives", b: "Where wires don't pay: battery-electric and hydrogen trains for low-density lines."},
    {t: "Construction Staging", b: "Keeping trains running while stringing wire: possessions, isolations, and the choreography of conversion."},
    {t: "Economics", b: "Capex per track-km vs diesel fuel and maintenance savings: the traffic-density threshold for electrification."}
];
var PRINCIPLES=[
    {n: "Voltage sets the architecture", e: "", s: "25 kV AC vs 1.5/3 kV DC vs third rail: voltage choice cascades through substations, clearances, and fleet."},
    {n: "Regeneration needs somewhere to go", e: "", s: "Braking energy must feed other trains or the grid: receptive substations or storage complete the circuit."},
    {n: "Clearances are civil engineering", e: "", s: "Raising bridges and lowering track for wires: the unglamorous cost dominating many projects."}
];
var USES=["Designing catenary systems", "Planning traction power supply", "Evaluating electrification business cases", "Integrating signaling"];
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
    id:id, t:tp.t, g:field, name:"Railway Electrification"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Railway Electrification Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-railway-electrification-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-railway-electrification-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("railway-electrification",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
