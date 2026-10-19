(function(){'use strict';
/* JAH Fundamentals of Immunology Database generator — jahdb-fundamental-immunology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMM-";
var FIELDS=["innate immunity", "adaptive immunity", "antibodies", "vaccines", "autoimmunity", "immunotherapy"];
var TOPICS=[
    {t: "Innate vs Adaptive", b: "Innate immunity (fast, generic: barriers, phagocytes, complement) holds the line while adaptive (slow, specific) learns the enemy."},
    {t: "Barriers and Phagocytes", b: "Skin, mucus, stomach acid, macrophages, and neutrophils clear most invaders before adaptive immunity even notices."},
    {t: "Pattern Recognition", b: "Toll-like receptors detect molecular patterns of pathogens (PAMPs) \u2014 the innate system's eyes."},
    {t: "Antigen Presentation", b: "MHC molecules display protein fragments: MHC I shows 'what's inside me' to killer T cells, MHC II shows 'what I ate' to helpers."},
    {t: "B Cells and Antibodies", b: "B cells mature to plasma cells secreting antibodies \u2014 Y-shaped proteins that neutralize, opsonize, and activate complement."},
    {t: "T Cells: Helpers and Killers", b: "CD4 helpers orchestrate, CD8 killers execute infected cells: cellular immunity's division of labor."},
    {t: "Immunological Memory", b: "Memory B and T cells persist for decades, responding faster and stronger \u2014 the cellular basis of lasting immunity."},
    {t: "How Vaccines Work", b: "Presenting harmless antigen trains memory without disease: live-attenuated, inactivated, subunit, and mRNA platforms."},
    {t: "Herd Protection", b: "Vaccinated majorities break transmission chains, shielding those who cannot be vaccinated \u2014 immunity as a public good."},
    {t: "Autoimmunity", b: "Tolerance fails and the system attacks self: molecular mimicry, genetic risk, and regulatory T-cell breakdown behind lupus, MS, diabetes."},
    {t: "Allergy and Hypersensitivity", b: "IgE against harmless antigens (pollen, peanuts) triggers histamine cascades \u2014 desensitization retrains the response."},
    {t: "Immunotherapy", b: "Checkpoint inhibitors release T-cell brakes on cancer; CAR-T engineers patients' own cells into tumor hunters."}
];
var PRINCIPLES=[
    {n: "Clonal selection", e: "one lymphocyte, one receptor", s: "Each lymphocyte carries a unique receptor; antigen selects and expands the matching clones."},
    {n: "Antibody diversity", e: "~10\u00b9\u00b9 specificities from gene rearrangement", s: "V(D)J recombination generates astronomical receptor variety from limited genes."},
    {n: "Vaccine efficacy", e: "VE = 1 \u2212 (risk_vax/risk_unvax)", s: "Protection measured as the fractional reduction in disease risk."}
];
var USES=["Designing vaccine schedules", "Diagnosing immune deficiencies", "Developing monoclonal antibodies", "Managing transplant rejection"];
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
    id:id, t:tp.t, g:field, name:"Immunology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Immunology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-immunology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-immunology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-immunology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
