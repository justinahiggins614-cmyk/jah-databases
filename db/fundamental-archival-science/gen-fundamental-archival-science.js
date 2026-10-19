(function(){'use strict';
/* JAH Fundamentals of Archival Science Database generator — jahdb-fundamental-archival-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AS-";
var FIELDS=["appraisal", "arrangement", "description", "preservation", "digital archives", "access and ethics"];
var TOPICS=[
    {t: "Archives vs Libraries", b: "Libraries collect published items by subject; archives keep unique records by creator \u2014 provenance, not topic, organizes archives."},
    {t: "The Principle of Provenance", b: "Records of different creators must never mix: context of creation is what makes records trustworthy evidence."},
    {t: "Original Order", b: "A creator's filing arrangement reveals how work was actually done \u2014 archivists preserve it rather than re-sorting by subject."},
    {t: "Appraisal: What to Keep", b: "No institution can keep everything: appraisal weighs evidential, informational, and legal value against cost \u2014 forever decisions."},
    {t: "Arrangement and Description", b: "Fonds \u2192 series \u2192 files \u2192 items: hierarchical arrangement with multilevel description (ISAD(G)) makes masses navigable."},
    {t: "Finding Aids", b: "Inventories, guides, and now EAD-encoded online aids are the maps researchers use to navigate holdings."},
    {t: "Preservation Basics", b: "Acid-free housings, stable climate, careful handling: paper, film, and magnetic media each decay on their own schedule."},
    {t: "Digital Preservation", b: "Bit rot, format obsolescence, and media failure threaten digital records; migration, emulation, and fixity checks fight back."},
    {t: "The OAIS Reference Model", b: "Ingest, archival storage, data management, access: the international blueprint every trustworthy digital repository follows."},
    {t: "Access and Restrictions", b: "Privacy, copyright, and donor agreements gate access: reading-room rules and redaction balance openness with obligation."},
    {t: "Reference and Outreach", b: "Archivists connect researchers with records and communities with their history \u2014 access is the point of preservation."},
    {t: "Records Management Upstream", b: "Retention schedules and classification at creation decide what survives to become archives \u2014 the pipeline starts at the desk."}
];
var PRINCIPLES=[
    {n: "Provenance", e: "keep records of one creator together", s: "Respect des fonds: archives preserve the context of creation, not just content."},
    {n: "Original order", e: "preserve creator's arrangement", s: "The order a creator kept records in is itself evidence \u2014 disturbing it destroys meaning."},
    {n: "OAIS model", e: "ingest \u2192 storage \u2192 access", s: "The reference model for digital preservation systems: packages in, integrity kept, access served."}
];
var USES=["Setting up organizational archives", "Appraising records for retention", "Building digital preservation systems", "Writing access policies"];
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
    id:id, t:tp.t, g:field, name:"Archival Science"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Archival Science demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-archival-science-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-archival-science-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-archival-science",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
