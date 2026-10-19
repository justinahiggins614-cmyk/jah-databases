(function(){'use strict';
/* JAH Fundamentals of Textile Science Database generator — jahdb-fundamental-textile-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TS-";
var FIELDS=["fibers", "yarns", "woven fabrics", "knitted fabrics", "dyeing and finishing", "performance testing"];
var TOPICS=[
    {t: "Natural Fibers", b: "Cotton breathes, wool insulates even when damp, silk drapes, linen cools \u2014 each plant or animal fiber has a signature microstructure."},
    {t: "Synthetic Fibers", b: "Nylon, polyester, and aramids are engineered polymers: melt-spun, drawn for strength, and tuned for elasticity, heat, or cut resistance."},
    {t: "Fiber Properties That Matter", b: "Length, fineness, strength, crimp, and moisture regain determine what a fiber can become \u2014 staple vs filament changes everything downstream."},
    {t: "From Fiber to Yarn", b: "Carding, drawing, and spinning align fibers and insert twist; twist is what turns a loose bundle into a strong yarn."},
    {t: "Yarn Numbering Systems", b: "Tex, denier, and cotton count all express linear density \u2014 mass per length \u2014 the universal currency of yarn specification."},
    {t: "Weaving: Warp Meets Weft", b: "Interlacing lengthwise warp with crosswise weft on a loom makes plain, twill, and satin weaves, each with distinct strength and drape."},
    {t: "Knitting: Loops, Not Crossings", b: "Interlocking loops give knits their stretch: weft knits (T-shirts) stretch more than warp knits, and all knits beat wovens for comfort."},
    {t: "Nonwovens and Felts", b: "Bonding fibers mechanically, thermally, or chemically makes filters, wipes, and geotextiles without any weaving or knitting."},
    {t: "Dyeing: Chemistry of Color", b: "Fiber-reactive, disperse, and acid dyes each bond to specific fiber chemistry; levelness, fastness, and shade matching are the craft."},
    {t: "Finishing Treatments", b: "Wrinkle-free resins, water repellents, flame retardants, and softeners are chemical finishes applied after dyeing for performance."},
    {t: "Performance and Comfort", b: "Moisture vapor transmission, air permeability, thermal resistance (tog/clo), and abrasion cycles quantify how fabric actually performs."},
    {t: "Textile Testing Standards", b: "Tensile, tear, pilling, colorfastness, and flammability tests turn subjective 'quality' into numbers buyers can specify."}
];
var PRINCIPLES=[
    {n: "Twist multiplier", e: "TM = TPI \u00d7 \u221a(count)", s: "Yarn strength and hand are governed by twist relative to yarn size."},
    {n: "Cover factor (woven)", e: "K = n / \u221aTex", s: "Fabric tightness \u2014 and thus strength, drape, and permeability \u2014 follows from thread density and yarn size."},
    {n: "Moisture regain", e: "regain = (wet \u2212 dry)/dry \u00d7 100%", s: "Comfort fibers like wool (~14%) and cotton (~8%) absorb far more vapor than polyester (~0.4%)."}
];
var USES=["Specifying workwear fabrics", "Engineering outdoor performance apparel", "Selecting medical and filtration textiles", "Quality-testing fabric production"];
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
    id:id, t:tp.t, g:field, name:"Textile Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Textile Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-textile-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-textile-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-textile-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
