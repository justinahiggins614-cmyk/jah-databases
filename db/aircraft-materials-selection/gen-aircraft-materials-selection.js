(function(){'use strict';
/* JAH Aircraft Materials Selection Database generator — jahdb-aircraft-materials-selection-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AMS-";
var FIELDS=["aluminum alloys", "titanium alloys", "composites", "fatigue and damage tolerance", "corrosion", "fasteners and joints"];
var TOPICS=[
    {t: "Why Weight Is Everything", b: "Every kilogram of structure costs payload or fuel for the aircraft's whole life: specific strength (strength/density) is the master metric."},
    {t: "Aluminum Alloys: The Workhorse", b: "2xxx (wings) and 7xxx (fuselage) series balance strength, fatigue, and corrosion; clad layers sacrifice themselves to protect the core."},
    {t: "Titanium: Hot and Strong", b: "Ti-6Al-4V keeps strength past 400\u00b0C for engine mounts and landing gear \u2014 at roughly five times aluminum's cost per kilogram."},
    {t: "Carbon-Fiber Composites", b: "Carbon/epoxy beats metals on specific stiffness and fatigue: the 787 and A350 are ~50% composite by weight."},
    {t: "Fatigue: The Real Killer", b: "Aloha 243 proved it: cyclic pressurization grows cracks from rivet holes \u2014 damage-tolerant design assumes flaws and schedules inspections."},
    {t: "Corrosion Zones", b: "Bilge, lavatory, and galley areas demand corrosion-resistant alloys plus drainage and coatings; material choice follows the zone map."},
    {t: "Fasteners and Joints", b: "Rivets, Hi-Loks, and bonded joints each transfer load differently; galvanic compatibility between fastener and skin is mandatory."},
    {t: "Fire and Heat", b: "Engine nacelles and APUs need titanium or steel: aluminum loses strength fast above 150\u00b0C \u2014 temperature maps choose materials."},
    {t: "Repairability", b: "A material you can't repair in the field grounds airplanes: bolted composite patches and stop-drilling are part of selection criteria."},
    {t: "Cost vs Performance", b: "Titanium's buy-to-fly ratio and composite cure cycles cost real money: selection optimizes lifecycle cost, not just weight."},
    {t: "New Alloys: Al-Li", b: "Aluminum-lithium shaves ~10% density off classic alloys with better fatigue \u2014 the incremental revolution in metal airframes."},
    {t: "Selection Workflow", b: "Requirements \u2192 candidate screening (Ashby charts) \u2192 detailed trade \u2192 testing: a repeatable process replacing tribal knowledge."}
];
var PRINCIPLES=[
    {n: "Specific strength rules", e: "", s: "Aerospace structures are sized by strength divided by density: aluminum 7075, titanium 6Al-4V, and carbon/epoxy each win different zones of the trade space."},
    {n: "Damage tolerance governs", e: "", s: "Fuselages are designed assuming cracks exist: inspection intervals come from crack-growth analysis, not from hoping cracks never start."},
    {n: "Corrosion is a design load", e: "", s: "Galvanic couples, exfoliation, and stress-corrosion are treated as loads in material choice \u2014 coatings and isolation are part of the selection."}
];
var USES=["Selecting wing-skin alloys", "Qualifying composite repairs", "Planning corrosion-prevention programs", "Trading weight vs cost on new designs"];
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
    id:id, t:tp.t, g:field, name:"Aircraft Materials Selection"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Aircraft Materials Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-aircraft-materials-selection-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-aircraft-materials-selection-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("aircraft-materials-selection",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
