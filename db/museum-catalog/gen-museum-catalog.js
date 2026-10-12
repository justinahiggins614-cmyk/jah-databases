(function(){'use strict';
/* JAH Museum Catalog Database generator — jahdb-museum-catalog-1.0.
   Property of Justin Addam Higgins (JAH).
   Master catalog of museum databases: live entries link real databases,
   planned entries reserve space for collections the sweep has not built yet.
   Deterministic: same seed always makes the same record. src:"signature". */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-MUSCAT-';
var KIND='museum';
var REAL=[{"slug": "paleontology", "name": "JAH Paleontology Database", "count": 10000, "section": "natural-history"}, {"slug": "fine-arts-study", "name": "JAH Fine Arts Signature Study Database", "count": 5000, "section": "art"}, {"slug": "fine-arts-published", "name": "JAH Fine Arts Published Archive Database", "count": 5000, "section": "art"}, {"slug": "art-market", "name": "JAH Art Market Database", "count": 5000, "section": "art"}, {"slug": "painting-public", "name": "Public Painting Database", "count": 150, "section": "art"}, {"slug": "painting-signature", "name": "Signature Painting Database", "count": 150, "section": "art"}, {"slug": "sculpture-public", "name": "Public Sculpture Database", "count": 150, "section": "art"}, {"slug": "sculpture-signature", "name": "Signature Sculpture Database", "count": 150, "section": "art"}, {"slug": "face-painting", "name": "Signature Face Painting Database", "count": 150, "section": "art"}];
var SECTIONS=[["art", "Art Museums", ["Paintings", "Sculptures", "Prints and drawings", "Decorative arts", "Modern art", "Portrait collections"]], ["history", "History Museums", ["Ancient artifacts", "Medieval collections", "Modern history", "Military history", "Local history"]], ["science", "Science Museums", ["Physics exhibits", "Chemistry displays", "Space and astronomy", "Technology halls", "Mathematics galleries"]], ["natural-history", "Natural History", ["Fossils", "Minerals and gems", "Specimen collections", "Botanical specimens", "Dinosaur halls"]], ["anthropology-culture", "Anthropology & Culture", ["Tribal artifacts", "Textiles", "Masks", "Pottery", "Ritual objects"]], ["specialized", "Specialized Museums", ["Maritime museums", "Aviation museums", "Railway museums", "Musical instruments", "Toy museums"]]];
var BASE='https://justinahiggins614-cmyk.github.io/jah-databases/db/';
function secLabel(k){for(var i=0;i<SECTIONS.length;i++)if(SECTIONS[i][0]===k)return SECTIONS[i][1];return k;}
function liveEntry(seed,ref){
  var s=prng(seed*7919+13);
  var others=[];for(var i=0;i<REAL.length&&others.length<3;i++){var c=REAL[(seed+i*3)%REAL.length];if(c.slug!==ref.slug)others.push(c.slug);}
  return {id:PREFIX+String(seed).padStart(6,'0'),
    title:ref.name+' — catalog entry',
    kind:KIND,section:ref.section,section_label:secLabel(ref.section),
    db_slug:ref.slug,db_name:ref.name,record_count:ref.count,
    db_url:BASE+ref.slug+'/',status:'live',
    description:'Cataloged '+KIND+' database: '+ref.name+', holding '+Number(ref.count).toLocaleString()+' records in the '+secLabel(ref.section)+' section. Open the database link to browse its full archive.',
    cross_refs:others,src:'signature',_seed:seed};
}
function plannedEntry(seed){
  var s=prng(seed*104729+7);
  var sec=SECTIONS[(seed-1)%SECTIONS.length];
  var focuses=sec[2];
  var fi=Math.floor((seed-1)/SECTIONS.length)%focuses.length;
  var part=Math.floor((seed-1)/(SECTIONS.length*focuses.length))+1;
  var focus=focuses[fi]+(part>1?' (Part '+part+')':'');
  var others=[];for(var i=0;i<REAL.length&&others.length<3;i++){others.push(REAL[(seed+i*5)%REAL.length].slug);}
  return {id:PREFIX+String(seed).padStart(6,'0'),
    title:focus+' — '+sec[1]+' (planned collection)',
    kind:KIND,section:sec[0],section_label:sec[1],
    db_slug:null,db_name:null,record_count:0,db_url:null,status:'planned',
    description:'Planned '+KIND+' collection for the '+sec[1]+' section: '+focus+'. The sweep has not built this database yet — this catalog entry reserves its place and will link the full database once it lands. Check back as the catalog grows over time.',
    cross_refs:others,src:'signature',_seed:seed};
}
function generate(seed,opts,rnd){
  opts=opts||{};
  seed=Math.max(1,seed|0);
  var secFilter=(opts.section||'').toString().trim();
  if(seed<=REAL.length&&!secFilter)return liveEntry(seed,REAL[seed-1]);
  if(secFilter){
    var s=prng(seed*31+5);
    for(var i=0;i<SECTIONS.length;i++)if(SECTIONS[i][0]===secFilter){
      var focuses=SECTIONS[i][2];
      var focus=focuses[(seed-1)%focuses.length];
      var others=[];for(var j=0;j<REAL.length&&others.length<3;j++)others.push(REAL[(seed+j*5)%REAL.length].slug);
      return {id:PREFIX+String(seed).padStart(6,'0'),
        title:focus+' — '+SECTIONS[i][1]+' (planned collection)',
        kind:KIND,section:secFilter,section_label:SECTIONS[i][1],
        db_slug:null,db_name:null,record_count:0,db_url:null,status:'planned',
        description:'Planned '+KIND+' collection for the '+SECTIONS[i][1]+' section: '+focus+'. The sweep has not built this database yet — this catalog entry reserves its place and will link the full database once it lands.',
        cross_refs:others,src:'signature',_seed:seed};
    }
  }
  return plannedEntry(seed);
}
var SECTKEYS=SECTIONS.map(function(x){return x[0];});
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(SECTKEYS.indexOf(r.section)<0)e.push('section');
  if(['live','planned'].indexOf(r.status)<0)e.push('status');
  if(r.status==='live'&&!r.db_slug)e.push('db_slug');
  if(r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var d=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return d.length?{ok:false,errors:['duplicate title']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-museum-catalog-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('museum-catalog',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
