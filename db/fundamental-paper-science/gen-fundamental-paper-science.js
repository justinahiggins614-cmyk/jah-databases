(function(){'use strict';
/* JAH Fundamentals of Paper Science Database generator — jahdb-fundamental-paper-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PS-";
var FIELDS=["wood and fibers", "pulping", "stock preparation", "the paper machine", "coating and converting", "paper testing"];
var TOPICS=[
    {t: "Wood as Raw Material", b: "Softwood tracheids are long and strong (packaging grades); hardwood fibers are short and smooth (printing grades) \u2014 furnish blends both."},
    {t: "Mechanical Pulping", b: "Grinding wood apart keeps nearly all the mass (high yield) but leaves lignin that yellows \u2014 the economics behind newsprint."},
    {t: "Kraft Chemical Pulping", b: "Cooking chips in sulfide liquor dissolves lignin while preserving fiber strength; chemical recovery makes kraft mills nearly closed-loop."},
    {t: "Bleaching Sequences", b: "Oxygen, chlorine dioxide, and peroxide stages whiten pulp stepwise (the ECF/TCF sequences), each targeting residual lignin and chromophores."},
    {t: "Refining and Beating", b: "Mechanical refining fibrillates fiber surfaces for hydrogen bonding \u2014 the single biggest lever on sheet strength, at the cost of drainage."},
    {t: "Wet-End Chemistry", b: "Retention aids, sizing agents, and fillers are added to the watery stock: what stays in the sheet determines strength, opacity, and printability."},
    {t: "The Fourdrinier Machine", b: "Stock jets onto a moving wire, drains, presses, and dries around steam cans at up to 2,000 m/min \u2014 continuous sheet forming at industrial scale."},
    {t: "Sizing: Controlling Water", b: "Internal and surface sizing (starch, AKD) tune how fast ink and water penetrate \u2014 unsized paper blots like a blotter."},
    {t: "Coating for Print", b: "Clay and latex coatings fill surface pores for glossy magazines; coated grades print sharper but cost more and recycle differently."},
    {t: "Paper Physics: Strength", b: "Tensile, tear, burst, and fold endurance each probe different bonding and fiber-length effects \u2014 packaging and currency need different profiles."},
    {t: "Optical Properties", b: "Brightness, whiteness, and opacity are distinct: opacity hides print-through, brightness is blue reflectance, whiteness is human preference."},
    {t: "Recycling and Sustainability", b: "Fibers survive 5\u20137 recycle loops before shortening too far; deinking, certification (FSC), and mill energy balance close the loop."}
];
var PRINCIPLES=[
    {n: "Kappa number", e: "lignin \u221d kappa", s: "Residual lignin in pulp \u2014 and thus bleach demand \u2014 is tracked by the kappa number."},
    {n: "Freeness/drainage", e: "drainage rate \u2194 refining", s: "Beating fibers improves bonding and strength but slows water drainage on the machine."},
    {n: "Basis weight", e: "g/m\u00b2 = mass per unit area", s: "The defining commercial specification of every paper grade."}
];
var USES=["Specifying packaging board grades", "Choosing printing papers", "Engineering specialty filter papers", "Running recycled-fiber operations"];
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
    id:id, t:tp.t, g:field, name:"Paper Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Paper Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-paper-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-paper-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-paper-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
