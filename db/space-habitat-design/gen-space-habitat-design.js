(function(){'use strict';
/* JAH Space Habitat Design Database generator — jahdb-space-habitat-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SHD-";
var FIELDS=["pressure vessels", "life support", "radiation", "human factors", "lunar surface", "mission architecture"];
var TOPICS=[
    {t: "Habitat Requirements", b: "Pressure, temperature, atmosphere, volume per crew: the derived requirements from human physiology."},
    {t: "Pressure Vessel Design", b: "Aluminum-lithium modules, inflatables (BEAM): containing 101 kPa against vacuum with micrometeoroid protection."},
    {t: "Life Support (ECLSS)", b: "Oxygen generation, CO\u2082 removal, water recovery: the regenerative systems keeping crews alive."},
    {t: "Radiation Protection", b: "GCR and SPE shielding: water walls, regolith berms, and storm shelters \u2014 the unsolved mass problem."},
    {t: "Thermal Control", b: "Rejecting heat to space via radiators: the habitat as a thermodynamic system."},
    {t: "Human Factors", b: "Volume, privacy, lighting (circadian), acoustics: architectural design for confined crews."},
    {t: "ISS Lessons", b: "25+ years of continuous habitation: what the station taught about living in space."},
    {t: "Lunar Surface Habitats", b: "Regolith shielding, dust mitigation, day/night thermal swings: building on the Moon's terms."},
    {t: "Mars Transit Habitats", b: "0-g health, radiation, and 6-month transits: the Deep Space Transport design problem."},
    {t: "ISRU", b: "Making air, water, and fuel from local resources: the technology enabling permanent presence."},
    {t: "Mission Architectures", b: "Sortie vs outpost vs settlement: the programmatic shapes of human expansion."},
    {t: "Planetary Protection", b: "Forward and backward contamination: the protocols protecting both Earth and other worlds."}
];
var PRINCIPLES=[
    {n: "Mass is money", e: "", s: "Every kilogram costs thousands to launch: habitat design is mass optimization with humans inside."},
    {n: "Closed loops are survival", e: "", s: "Air and water recycling (ISS: 98% water recovery) decide mission duration: resupply is the alternative."},
    {n: "Humans need more than survival", e: "", s: "Privacy, windows, varied spaces: psychological habitability sustains crews on multi-year missions."}
];
var USES=["Designing habitat modules", "Sizing life-support systems", "Planning lunar bases", "Assessing radiation shielding"];
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
    id:id, t:tp.t, g:field, name:"Space Habitat Design"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Space Habitat Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-space-habitat-design-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-space-habitat-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("space-habitat-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
