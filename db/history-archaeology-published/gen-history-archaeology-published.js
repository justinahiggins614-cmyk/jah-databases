(function(){'use strict';
/* JAH History and Archaeology Published Archive Database — deterministic boundless generator (jahdb-history-archaeology-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='history-archaeology-published';
var BASE='history-archaeology';
var GENVER='jahdb-history-archaeology-published-1.0';
var PREFIX='JAH-history-archaeology-published-P-';
var CATS=["ancient", "medieval", "modern", "archaeology", "historiography", "methods"];
var WORKS=[["The Histories", "Herodotus", "Penguin Classics", 440, "ancient", "Herodotus inquires into the Greco-Persian wars, digressing into the customs of Egypt, Scythia, and Persia. Called both the father of history and the father of lies, he invented historical narrative from travel and testimony.", ["inquiry", "ethnography", "narrative"]], ["History of the Peloponnesian War", "Thucydides", "Penguin Classics", 411, "ancient", "Thucydides\u2019 unfinished account of Athens versus Sparta pursues political causes with speeches and analysis. His claim \u2014 history as a possession for all time \u2014 founded political realism.", ["power", "realism", "cause"]], ["The Tomb of Tutankhamen", "Howard Carter, A.C. Mace", "Cassell", 1923, "archaeology", "Carter\u2019s account of discovering Tutankhamun\u2019s intact tomb in 1922: the sealed doorway, the antechamber\u2019s treasures, and the slow clearance. The find that made archaeology front-page news.", ["excavation", "tomb", "artifact"]], ["The Mediterranean and the Mediterranean World in the Age of Philip II", "Fernand Braudel", "Harper & Row", 1949, "historiography", "Braudel\u2019s doctoral thesis made the case for the longue dur\u00e9e \u2014 geography and structure over events. The Mediterranean itself, not kings, becomes the historical actor.", ["longue dur\u00e9e", "structure", "event"]], ["What is History?", "E.H. Carr", "Alfred A. Knopf", 1961, "historiography", "Carr\u2019s lectures argue that history is a dialogue between past and present: facts become historical when the historian selects them. The classic statement of history as interpretation.", ["interpretation", "fact", "selection"]], ["The Historian\u2019s Craft", "Marc Bloch", "Alfred A. Knopf", 1949, "historiography", "Bloch, writing under Nazi occupation before his execution, defends history as the science of change, built from relics and critical method. A founder of the Annales school\u2019s testament.", ["Annales", "relic", "method"]], ["The Guns of August", "Barbara Tuchman", "Macmillan", 1962, "modern", "Tuchman\u2019s narrative of August 1914 follows Europe\u2019s armies into the Marne campaign, showing how plans outran politics. The Pulitzer-winning account of how the Great War began.", ["mobilization", "Marne", "narrative"]], ["Guns, Germs, and Steel", "Jared Diamond", "W. W. Norton", 1997, "ancient", "Diamond argues that Eurasia\u2019s dominance came from geography \u2014 domesticable plants and animals, east-west axes \u2014 not racial superiority. A sweeping environmental explanation of inequality.", ["geography", "domestication", "diffusion"]], ["SPQR: A History of Ancient Rome", "Mary Beard", "Liveright", 2015, "ancient", "Beard retells Rome\u2019s first millennium from Romulus to Caracalla, questioning the sources as she goes. Citizenship, power, and empire seen through a skeptical classicist\u2019s eye.", ["citizenship", "empire", "source criticism"]], ["The Oxford History of Ancient Egypt", "Ian Shaw, editor", "Oxford University Press", 2000, "ancient", "Shaw\u2019s multi-author volume covers Egypt from prehistory to the Roman conquest with current archaeology. The scholarly one-volume reference for pharaonic civilization.", ["pharaoh", "dynasty", "chronology"]], ["Archaeology: Theories, Methods, and Practice", "Colin Renfrew, Paul Bahn", "Thames & Hudson", 1991, "archaeology", "The standard archaeology textbook: survey, excavation, dating, and interpretation from stratigraphy to post-processual theory. How archaeologists know what they claim to know.", ["stratigraphy", "dating", "survey"]], ["Archaeology from the Earth", "Mortimer Wheeler", "Oxford University Press", 1954, "archaeology", "Wheeler codified grid excavation and stratigraphic method from his work in Britain and India. The book taught a generation to dig by context, not by treasure.", ["grid method", "context", "stratigraphy"]], ["The Crusades Through Arab Eyes", "Amin Maalouf", "Al Saqi", 1984, "medieval", "Maalouf retells the Crusades from Arab chroniclers \u2014 Ibn al-Athir, Usama ibn Munqidh \u2014 reversing the usual Western narrative. A landmark of perspective in medieval history.", ["crusade", "chronicler", "perspective"]], ["The Time Traveler\u2019s Guide to Medieval England", "Ian Mortimer", "Simon & Schuster", 2008, "medieval", "Mortimer\u2019s handbook walks readers through fourteenth-century England year by year \u2014 food, law, travel, hygiene. Medieval daily life reconstructed as a visitor\u2019s guide.", ["daily life", "manor", "guild"]], ["1776", "David McCullough", "Simon & Schuster", 2005, "modern", "McCullough narrates the Revolutionary War\u2019s pivotal year through Washington\u2019s army and the British command. A character-driven account of the campaign for New York.", ["revolution", "Washington", "campaign"]], ["The Age of Extremes: The Short Twentieth Century", "Eric Hobsbawm", "Pantheon", 1994, "modern", "Hobsbawm\u2019s history of 1914\u20131991 treats the century as an age of catastrophe, golden years, and landslide. The Marxist historian\u2019s panoramic synthesis of the modern era.", ["century", "catastrophe", "synthesis"]], ["AP World History: Modern Course and Exam Description", "College Board", "College Board", 2019, "methods", "The College Board framework defines the modern world-history course: periodization, comparison, causation, and document-based argument. The standard for secondary world history in the U.S.", ["periodization", "causation", "DBQ"]], ["Historians\u2019 Fallacies", "David Hackett Fischer", "Harper & Row", 1970, "methods", "Fischer catalogs the logical errors historians commit \u2014 from the fallacy of the single cause to presentism. A logic manual for historical argument.", ["fallacy", "evidence", "argument"]]];
var PROJ=[["Satellite Archaeology at Scale", "Machine-read landscapes revealing buried cities."], ["DNA and Migration Histories", "Ancient genomes rewriting who moved where."], ["Digital Twins of Heritage Sites", "Millimeter-accurate models for study and repair."], ["Climate Archives", "Ice cores and mud as historical documents."], ["Decolonized Museum Practice", "Restitution as standard curatorial method."], ["Urban Archaeology of the 21st Century", "Excavating our own recent past."], ["Oral History at Scale", "Million-interview archives and how to search them."], ["The Internet as Primary Source", "Historians confront the archived web."], ["Underwater Heritage Mapping", "Sonar surveys of drowned landscapes."], ["AI-Assisted Epigraphy", "Machine reading of damaged inscriptions."], ["Histories of Pandemics", "What disease did to states and societies."], ["Teaching History with AI", "Primary-source tutors in every classroom."]];
var METHODS='archival research, site survey data, and comparative case studies';
var FRAMES=["Early pilots suggest the approach could improve outcomes markedly where it is adopted first in community settings.", "Practitioners report faster skill transfer when the method is taught in cohorts rather than through solo study.", "The study projects mainstream adoption within a decade, beginning in specialist programs and spreading to general curricula.", "Reviewers note the strongest effects where the method is paired with mentorship rather than delivered as content alone."];
var POOL={};
CATS.forEach(function(c){POOL[c]=WORKS.filter(function(w){return w[4]===c;});});
function pad7(n){return String(n).padStart(7,'0');}
function sigLink(seed){return '../'+BASE+'-study/index.html?sig=JAH-'+BASE+'-STUDY-S-'+pad7(seed);}
/* work layout: [title, authors, publication, year, category, abstract, [terms]] */
function aspectBody(w,aspect){
  var b=w[5]+'\n\nKey terms: '+w[6].join('; ')+'.';
  if(aspect==='focus'){
    b+='\n\nStudy focus: How does \u201c'+w[6][0]+'\u201d shape this work\u2019s central argument? '+
       'What would a practitioner carry from \u201c'+w[6][1]+'\u201d into daily practice?';
  }
  b+='\n\nPublished: '+w[2]+', '+w[3]+'.';
  return b;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[(seed-1)%CATS.length];
  var lvl=rnd()<0.35?2:1;
  var id=PREFIX+pad7(seed);
  var link=sigLink(seed);
  if(lvl===1){
    var pool=(POOL[cat]&&POOL[cat].length)?POOL[cat]:WORKS;
    var w=pick(pool,rnd);
    var aspect=pick(['abstract','focus'],rnd);
    var title=w[0];
    return {id:id,title:title,authors:w[1],publication:w[2],year:w[3],
      full_content:aspectBody(w,aspect),
      source_ref:'WorldCat \u2014 \u201c'+title+'\u201d / '+w[1]+' ('+w[3]+')',
      signature_link:link,level:1,category:cat};
  }
  var p=pick(PROJ,rnd);
  var frame=pick(FRAMES,rnd);
  var ptitle='Level 2 \u2014 '+p[0];
  var full='This is a Level 2 projection record: a forward-looking study sketched from the archive\u2019s patterns, '+
    'not a real publication. \u201c'+p[0]+'.\u201d '+p[1]+' Projected method: '+METHODS+'. '+frame;
  return {id:id,title:ptitle,authors:'JAH Signature Projection Office',
    publication:'JAH Published Archive \u2014 Projection Series',year:2026+(seed%3),
    full_content:full,
    source_ref:'JAH Published Archive \u2014 Projection Series (generated projection)',
    signature_link:link,level:2,category:cat};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX+'\\d{7}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.level===2&&r.title.slice(0,7)!=='Level 2')e.push('level2-title');
  if(r.level===1&&r.title.slice(0,7)==='Level 2')e.push('level1-title');
  if(typeof r.authors!=='string'||!r.authors.length)e.push('authors');
  if(typeof r.publication!=='string'||!r.publication.length)e.push('publication');
  if(typeof r.year!=='number'||(r.year|0)!==r.year||r.year<100||r.year>2028)e.push('year');
  if(typeof r.full_content!=='string'||r.full_content.length<120||r.full_content.length>3000)e.push('full_content');
  if(typeof r.source_ref!=='string'||!r.source_ref.length)e.push('source_ref');
  if(!/^\.\.\/[a-z0-9-]+\-study\/index\.html\?sig=JAH\-[a-z0-9-]+\-STUDY\-S\-\d{7}$/.test(r.signature_link||''))e.push('signature_link');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(CATS.indexOf(r.category)<0)e.push('category');
  return {ok:!e.length,errors:e};
}
/* 40 seeds x 40 invariant checks = 1600 assertions. */
function selftest(){
  var seeds=[],i;
  for(i=1;i<=40;i++)seeds.push(i);
  var fails=[],passed=0,total=0;
  function chk(seed,name,cond){total++;if(cond){passed++;}else{fails.push('seed '+seed+': '+name);}}
  function bad(r,over){var c={},k;for(k in r)c[k]=r[k];for(k in over)c[k]=over[k];return c;}
  seeds.forEach(function(seed){
    var r=generate(seed,{},prng(seed));
    var r2=generate(seed,{},prng(seed));
    chk(seed,'is-object',!!r&&typeof r==='object');
    chk(seed,'id-format',new RegExp('^'+PREFIX+'\\d{7}$').test(r.id));
    chk(seed,'id-prefix',r.id.slice(0,PREFIX.length)===PREFIX);
    chk(seed,'id-seq',r.id===PREFIX+pad7(seed));
    chk(seed,'title-nonempty',typeof r.title==='string'&&r.title.length>0);
    chk(seed,'authors-nonempty',typeof r.authors==='string'&&r.authors.length>0);
    chk(seed,'publication-nonempty',typeof r.publication==='string'&&r.publication.length>0);
    chk(seed,'year-range',typeof r.year==='number'&&(r.year|0)===r.year&&r.year>=100&&r.year<=2028);
    chk(seed,'full-min',typeof r.full_content==='string'&&r.full_content.length>=120);
    chk(seed,'full-max',r.full_content.length<=3000);
    chk(seed,'full-sentences',(r.full_content.match(/\./g)||[]).length>=3);
    chk(seed,'source-nonempty',typeof r.source_ref==='string'&&r.source_ref.length>0);
    chk(seed,'siglink-format',/^\.\.\/[a-z0-9-]+\-study\/index\.html\?sig=JAH\-[a-z0-9-]+\-STUDY\-S\-\d{7}$/.test(r.signature_link||''));
    chk(seed,'siglink-seq',r.signature_link.slice(-10)==='-S-'+pad7(seed));
    chk(seed,'level-12',r.level===1||r.level===2);
    chk(seed,'l2-title',r.level!==2||r.title.slice(0,7)==='Level 2');
    chk(seed,'l1-title',r.level!==1||r.title.slice(0,7)!=='Level 2');
    chk(seed,'category-valid',CATS.indexOf(r.category)>=0);
    chk(seed,'validate-ok',validate(r).ok);
    chk(seed,'deterministic',JSON.stringify(r)===JSON.stringify(r2));
    chk(seed,'title-no-html',r.title.indexOf('<')<0);
    chk(seed,'full-no-wordbreak',r.full_content.indexOf('word-break')<0);
    chk(seed,'full-grounded',r.level===1?r.full_content.indexOf(String(r.year))>=0:r.full_content.indexOf('Level 2 projection')>=0);
    chk(seed,'id-unique',seed===1||r.id!==PREFIX+pad7(seed-1));
    chk(seed,'rej-bad-id',!validate(bad(r,{id:'BAD'})).ok);
    chk(seed,'rej-no-title',!validate(bad(r,{title:''})).ok);
    chk(seed,'rej-bad-year',!validate(bad(r,{year:50})).ok);
    chk(seed,'rej-bad-level',!validate(bad(r,{level:3})).ok);
    chk(seed,'rej-short-full',!validate(bad(r,{full_content:'x'})).ok);
    chk(seed,'rej-bad-sig',!validate(bad(r,{signature_link:'nope'})).ok);
    chk(seed,'rej-l2-title',!validate(bad(r,{level:2,title:'No Prefix Here'})).ok);
    chk(seed,'rej-l1-title',!validate(bad(r,{level:1,title:'Level 2 Sneaky'})).ok);
    chk(seed,'category-opt',generate(seed,{category:CATS[0]},prng(seed)).category===CATS[0]);
    chk(seed,'jahdb-registered',typeof JAHDB==='undefined'||!!JAHDB.getGenerator(SLUG));
    chk(seed,'runGenerator-ok',typeof JAHDB==='undefined'?true:JAHDB.runGenerator(SLUG,seed,{}).ok);
    chk(seed,'no-underscore-keys',Object.keys(r).every(function(k){return k.charAt(0)!=='_';}));
    chk(seed,'authors-no-database',r.authors.indexOf('Database')<0);
    chk(seed,'pub-no-database',r.publication.indexOf('Database')<0);
    chk(seed,'title-no-database',r.title.indexOf('Database')<0);
    chk(seed,'l2-honesty',r.level!==2||r.full_content.indexOf('not a real publication')>=0);
    chk(seed,'l1-pubnote',r.level!==1||r.full_content.indexOf('Published:')>=0);
    chk(seed,'json-roundtrip',JSON.parse(JSON.stringify(r)).id===r.id);
  });
  return {seeds:seeds.length,per_seed:total/seeds.length,passed:passed,failed:total-passed,total:total,failures:fails};
}
var gen={version:GENVER,generate:generate,validate:validate,selftest:selftest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
