(function(){'use strict';
/* JAH Library Catalog Database generator — jahdb-library-catalog-1.0.
   Property of Justin Addam Higgins (JAH).
   Master catalog of library databases: live entries link real databases,
   planned entries reserve space for collections the sweep has not built yet.
   Deterministic: same seed always makes the same record. src:"signature". */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-LIBCAT-';
var KIND='library';
var REAL=[{"slug": "library-archival-study", "name": "JAH Library Information and Archival Studies Signature Study Database", "count": 5000, "section": "archives-manuscripts"}, {"slug": "library-archival-published", "name": "JAH Library, Information and Archival Studies Published Archive Database", "count": 5000, "section": "archives-manuscripts"}, {"slug": "books", "name": "The Signature Book Depository Database", "count": 48100, "section": "books"}, {"slug": "comics", "name": "The Signature Comic Store Database", "count": 18524, "section": "books"}, {"slug": "rare-books", "name": "JAH Rare Book Database", "count": 5000, "section": "books"}, {"slug": "news", "name": "The Signature Global Newspaper Archive Database", "count": 72, "section": "periodicals"}, {"slug": "journalism-study", "name": "JAH Journalism and Reporting Signature Study Database", "count": 5000, "section": "periodicals"}, {"slug": "journalism-published", "name": "JAH Journalism and Reporting Published Archive Database", "count": 5000, "section": "periodicals"}, {"slug": "encyclopedias", "name": "Encyclopedias Database", "count": 168, "section": "reference"}, {"slug": "atlases", "name": "Atlases Database", "count": 168, "section": "reference"}, {"slug": "geography-atlas", "name": "JAH Geography Atlas Database", "count": 10000, "section": "maps-cartography"}, {"slug": "music", "name": "Signature Music Studio Database", "count": 108000, "section": "audiovisual"}, {"slug": "music-theory", "name": "JAH Music Theory Database", "count": 10000, "section": "audiovisual"}, {"slug": "music-theory-public", "name": "Public Music Theory Database", "count": 150, "section": "audiovisual"}, {"slug": "music-theory-signature", "name": "Signature Music Theory Database", "count": 150, "section": "audiovisual"}, {"slug": "music-performing-arts-study", "name": "JAH Music and Performing Arts Signature Study Database", "count": 5000, "section": "audiovisual"}, {"slug": "music-performing-arts-published", "name": "JAH Music and Performing Arts Published Archive Database", "count": 5000, "section": "audiovisual"}, {"slug": "film-video", "name": "JAH Film and Video Database", "count": 10000, "section": "audiovisual"}, {"slug": "netflix", "name": "JAH Netflix Signature Archive Database", "count": 10000, "section": "audiovisual"}, {"slug": "photography", "name": "JAH Photography Database", "count": 10000, "section": "audiovisual"}, {"slug": "photography-public", "name": "Public Photography Database", "count": 150, "section": "audiovisual"}, {"slug": "photography-signature", "name": "Signature Photography Database", "count": 150, "section": "audiovisual"}];
var SECTIONS=[["books", "Books", ["Fiction novels", "Non-fiction works", "Poetry collections", "Drama and plays", "Essay collections", "Short story collections", "Biographies and memoirs", "Classic literature"]], ["periodicals", "Periodicals", ["Daily newspapers", "Magazines", "Academic journals", "Trade publications", "Newsletters", "Literary zines"]], ["reference", "Reference", ["Encyclopedias", "Dictionaries", "World atlases", "Almanacs", "Yearbooks", "Directories"]], ["archives-manuscripts", "Archives & Manuscripts", ["Historical manuscripts", "Personal letters", "Diaries and journals", "Official records", "Rare documents"]], ["maps-cartography", "Maps & Cartography", ["Historical maps", "Topographic maps", "Nautical charts", "City plans", "Celestial charts"]], ["government-documents", "Government Documents", ["Laws and statutes", "Census records", "Parliamentary papers", "Treaties", "Public reports"]], ["genealogy", "Genealogy", ["Family histories", "Birth records", "Marriage records", "Census indexes", "Immigration records"]], ["children", "Children's Collections", ["Picture books", "Early readers", "Young adult fiction", "Fairy tales", "Educational works"]], ["audiovisual", "Audiovisual", ["Films", "Music recordings", "Audiobooks", "Documentaries", "Radio broadcasts"]], ["rare-collections", "Rare Collections", ["Incunabula", "First editions", "Illuminated manuscripts", "Artists' books"]]];
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
var gen={version:'jahdb-library-catalog-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('library-catalog',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
