(function(){'use strict';
/* JAH Earthquake Resistant Design Database generator — jahdb-earthquake-resistant-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ERD-";
var FIELDS=["seismic hazard", "structural dynamics", "ductile design", "isolation", "retrofit", "nonstructural"];
var TOPICS=[
    {t: "Seismic Hazard", b: "Faults, recurrence, attenuation, site effects: the PSHA pipeline producing design spectra."},
    {t: "How Buildings Respond", b: "Period, damping, mode shapes: the dynamic properties deciding whether shaking is a push or a resonance."},
    {t: "Response Spectra", b: "The design tool: spectral acceleration vs period, site-adjusted \u2014 the earthquake as engineers use it."},
    {t: "Ductile Concrete Frames", b: "Strong-column/weak-beam, confinement, joint shear: detailing that lets frames sway without collapsing."},
    {t: "Steel Moment Frames", b: "Reduced beam sections (dogbones), panel zones, lateral bracing: steel's ductile seismic system after Northridge's lessons."},
    {t: "Shear Walls and Braced Frames", b: "Stiff systems for tall and essential buildings: capacity-designed walls and buckling-restrained braces."},
    {t: "Base Isolation", b: "Bearings decoupling buildings from ground motion: hospitals and data centers riding out quakes nearly still."},
    {t: "Dampers", b: "Viscous, friction, and tuned-mass dampers bleeding seismic energy: retrofit-friendly protection."},
    {t: "Nonstructural Components", b: "Suspended ceilings, piping, cladding, contents: the 70% of building value that also needs seismic design."},
    {t: "Retrofit", b: "Jacketing columns, adding walls, isolating: bringing vulnerable existing buildings to life-safety."},
    {t: "Performance-Based Design", b: "Immediate occupancy vs life safety vs collapse prevention: choosing the performance target with the owner."},
    {t: "Post-Earthquake Assessment", b: "ATC-20 placarding (green/yellow/red): the rapid decisions after the shaking stops."}
];
var PRINCIPLES=[
    {n: "Ductility saves lives", e: "", s: "Structures survive by deforming without collapsing: detailing for ductility matters more than raw strength."},
    {n: "Design to the hazard", e: "", s: "Site-specific spectra from fault and soil data: the ground motion input everything follows."},
    {n: "Nonstructural kills too", e: "", s: "Ceilings, cladding, and equipment cause most earthquake injuries and economic loss: anchor everything."}
];
var USES=["Designing ductile frames", "Specifying base isolation", "Retrofitting vulnerable buildings", "Assessing post-quake safety"];
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
    id:id, t:tp.t, g:field, name:"Earthquake Resistant Design"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Earthquake Design Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-earthquake-resistant-design-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-earthquake-resistant-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("earthquake-resistant-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
