(function(){'use strict';
/* JAH Fundamentals of Fracture Mechanics Database generator — jahdb-fundamental-fracture-mechanics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FM2-";
var FIELDS=["stress concentration", "stress intensity", "fracture toughness", "fatigue crack growth", "environmental cracking", "damage tolerance"];
var TOPICS=[
    {t: "Why Strength Isn't Enough", b: "High-strength parts still fail suddenly from small cracks: strength measures uncracked resistance, toughness measures cracked resistance."},
    {t: "Stress Concentration", b: "Holes, notches, and sharp corners multiply local stress (Kt up to 3+ for a hole) \u2014 cracks are the ultimate concentrators."},
    {t: "Griffith's Energy Idea", b: "A crack grows when released strain energy exceeds the cost of new surface: the energy balance that founded fracture mechanics."},
    {t: "The Stress Intensity Factor K", b: "K packages load, crack size, and geometry into one number characterizing the crack-tip field \u2014 the master variable."},
    {t: "Fracture Toughness K_IC", b: "A true material property (MPa\u221am): aluminum ~30, structural steel ~50\u2013150, ceramics ~1\u20135 \u2014 it sets the critical flaw size."},
    {t: "Plane Strain vs Plane Stress", b: "Thick sections constrain plasticity (plane strain, lower toughness); thin sheets yield more freely \u2014 thickness changes the answer."},
    {t: "Fatigue: Cracks Grow Slowly", b: "Most cracks grow a little each cycle; the Paris law integrates growth from detectable size to critical \u2014 the basis of inspection intervals."},
    {t: "Damage-Tolerant Design", b: "Assume cracks exist: size inspections to catch them at half the critical length, and prove the structure survives until the next check."},
    {t: "Stress-Corrosion Cracking", b: "Tensile stress plus a corrosive environment cracks alloys far below their toughness \u2014 stainless in chlorides, brass in ammonia."},
    {t: "Hydrogen Embrittlement", b: "Atomic hydrogen diffuses to crack tips and embrittles high-strength steels \u2014 delayed, silent, and catastrophic without controls."},
    {t: "Fractography: Reading Breaks", b: "Beach marks, chevrons, and dimples on fracture surfaces record the failure history \u2014 the forensic language of broken parts."},
    {t: "Proof Testing and NDT", b: "Ultrasonic, eddy-current, dye-penetrant, and X-ray methods find cracks before K reaches K_IC; proof loads screen the rest."}
];
var PRINCIPLES=[
    {n: "Stress intensity", e: "K = Y * \u03c3 * \u221a(\u03c0 * a)", s: "Crack-tip severity scales with stress times the square root of crack size."},
    {n: "Fracture criterion", e: "K \u2265 K_IC \u2192 fracture", s: "Rapid fracture occurs when stress intensity reaches the material's toughness."},
    {n: "Paris law", e: "da/dN = C * (\u0394K)^m", s: "Fatigue crack growth per cycle follows a power law in stress-intensity range."}
];
var USES=["Setting aircraft inspection intervals", "Qualifying pressure-vessel steels", "Analyzing failed components", "Designing fail-safe structures"];
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
    id:id, t:tp.t, g:field, name:"Fracture Mechanics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Fracture Mechanics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-fracture-mechanics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-fracture-mechanics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-fracture-mechanics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
