(function(){'use strict';
/* JAH Bridge Materials Engineering Database generator — jahdb-bridge-materials-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BMS-";
var FIELDS=["structural steels", "reinforced concrete", "prestressed concrete", "cables and suspenders", "bearings and joints", "durability"];
var TOPICS=[
    {t: "Bridge Types, Material Logic", b: "Beam, arch, truss, suspension, cable-stayed: span length and site pick the form, and the form picks the material."},
    {t: "Structural Steels", b: "Grade 50 weathering steel dominates; HPS 70W/100W serve long spans \u2014 strength, weldability, and toughness balanced per member."},
    {t: "Weathering Steel", b: "Patina-forming steels skip paint where environments allow \u2014 but salt spray and tunnel-like conditions defeat the patina."},
    {t: "Reinforced Concrete", b: "Steel bars carry tension concrete cannot: bond, development length, and crack control make the composite work."},
    {t: "Prestressed Concrete", b: "Pre-compression from tensioned strands lets concrete span 30\u201350 m without cracking \u2014 the workhorse of highway overpasses."},
    {t: "Stay Cables and Suspenders", b: "Parallel-wire and strand cables with HDPE sheathing and grout: corrosion protection of the tension lifeline."},
    {t: "Decks: The Wearing Surface", b: "Concrete decks with epoxy-coated rebar, latex overlays, and waterproofing membranes fight the salt assault from above."},
    {t: "Bearings and Expansion Joints", b: "Bridges move with temperature: elastomeric and pot bearings plus sealed joints accommodate motion without damage."},
    {t: "Foundations", b: "Driven piles, drilled shafts, and spread footings reach competent ground; scour \u2014 not overload \u2014 kills most failed bridges."},
    {t: "Seismic Detailing", b: "Ductile detailing, restrainers, and isolation bearings keep bridges standing through earthquakes: capacity design philosophy."},
    {t: "Inspection and Rating", b: "Biennial inspections, load ratings, and fracture-critical member programs: the management system behind the 600,000+ US bridges."},
    {t: "Lifecycle Cost", b: "Cheapest first cost rarely wins: stainless rebar or duplex coatings pay back over 75\u2013100-year design lives."}
];
var PRINCIPLES=[
    {n: "Durability is structural", e: "", s: "A bridge that corrodes is a bridge that fails: cover depth, drainage, and coating are structural design, not finishes."},
    {n: "Prestress puts concrete in compression", e: "", s: "Tensioning steel before loading keeps concrete \u2014 strong in compression, weak in tension \u2014 permanently squeezed safe."},
    {n: "Details make fatigue life", e: "", s: "Cover plates, weld toes, and pin details decide steel bridge life far more than the grade stamped on the beam."}
];
var USES=["Selecting girder steel grades", "Specifying prestressed beam designs", "Planning bridge deck overlays", "Rating existing bridges"];
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
    id:id, t:tp.t, g:field, name:"Bridge Materials Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Bridge Materials Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-bridge-materials-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-bridge-materials-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("bridge-materials-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
