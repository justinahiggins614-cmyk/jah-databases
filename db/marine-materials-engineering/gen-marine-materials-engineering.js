(function(){'use strict';
/* JAH Marine Materials Engineering Database generator — jahdb-marine-materials-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MME-";
var FIELDS=["hull steels", "stainless and nickel alloys", "copper alloys", "composites afloat", "corrosion protection", "fouling control"];
var TOPICS=[
    {t: "The Sea Attacks Everything", b: "Saltwater combines corrosion, fouling, fatigue, and UV: marine material selection is multi-threat defense."},
    {t: "Hull Steels", b: "Grade A through DH36/EH36: higher-strength steels save weight but demand stricter welding and fatigue detailing."},
    {t: "Stainless in Seawater", b: "316L resists general corrosion but pits in crevices; duplex 2205 earns its place in shafts, pumps, and fasteners."},
    {t: "Copper-Nickel Piping", b: "90/10 and 70/30 Cu-Ni resist biofouling and corrosion in seawater piping \u2014 the quiet standard for decades."},
    {t: "Propeller Bronzes", b: "Nickel-aluminum bronze balances strength, cavitation resistance, and repairability for propellers and running gear."},
    {t: "Cathodic Protection", b: "Sacrificial zinc/aluminum anodes or impressed current hold hulls below corrosion potential \u2014 electrochemistry as maintenance."},
    {t: "Coating Systems", b: "Epoxy primers plus antifouling topcoats: surface prep (Sa 2\u00bd) decides whether the system lasts 5 years or 15."},
    {t: "Antifouling Strategies", b: "Copper biocides, foul-release silicones, and ultrasonic systems each fight the billion-dollar drag of hull fouling."},
    {t: "Composites Afloat", b: "Glass/carbon hulls and superstructures cut weight and never rust \u2014 but need fire and impact engineering metals don't."},
    {t: "Welding at Sea Scale", b: "Welding procedure qualification, preheat, and NDT keep kilometer-long welds sound; hydrogen cracking is the enemy."},
    {t: "Fatigue of Ship Details", b: "Bracket toes and hatch corners are where cracks start: detail catalogs (IACS) standardize what works."},
    {t: "Material Selection Workflow", b: "Zone maps (splash, submerged, interior) \u00d7 threats \u00d7 cost: a matrix that picks the right alloy for each location."}
];
var PRINCIPLES=[
    {n: "Seawater is an electrolyte", e: "", s: "Every dissimilar-metal joint underwater is a battery: galvanic series position predicts which metal sacrifices itself."},
    {n: "Coatings are systems", e: "", s: "Surface prep plus primer plus antifouling is one engineered system \u2014 skipping prep wastes the expensive topcoat."},
    {n: "Fatigue at welds rules", e: "", s: "Ship structures fail at weld toes and cutouts: detail design and post-weld treatment matter more than plate grade."}
];
var USES=["Specifying hull plate grades", "Designing cathodic protection", "Selecting propeller alloys", "Planning drydock coating work"];
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
    id:id, t:tp.t, g:field, name:"Marine Materials Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Marine Materials Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-marine-materials-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-marine-materials-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("marine-materials-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
