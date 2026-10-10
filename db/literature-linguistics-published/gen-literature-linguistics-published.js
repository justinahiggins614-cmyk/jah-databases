(function(){'use strict';
/* JAH Literature and Linguistics Published Archive Database — deterministic boundless generator (jahdb-literature-linguistics-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='literature-linguistics-published';
var BASE='literature-linguistics';
var GENVER='jahdb-literature-linguistics-published-1.0';
var PREFIX='JAH-literature-linguistics-published-P-';
var CATS=["literary-theory", "poetry", "fiction", "drama", "rhetoric", "translation"];
var WORKS=[["Poetics", "Aristotle", "Penguin Classics", 335, "drama", "Aristotle\u2019s lecture notes define tragedy by plot, character, and catharsis, and rank epic below it. Two thousand years of literary theory start here.", ["mimesis", "catharsis", "plot"]], ["Course in General Linguistics", "Ferdinand de Saussure", "McGraw-Hill", 1916, "literary-theory", "Saussure\u2019s students\u2019 notes founded structural linguistics: the sign as signifier plus signified, langue versus parole, synchrony versus diachrony. The base of structuralism.", ["sign", "langue", "structuralism"]], ["Anatomy of Criticism", "Northrop Frye", "Princeton University Press", 1957, "literary-theory", "Frye\u2019s four essays map literature by modes, symbols, myths, and genres \u2014 comedy to irony \u2014 as a self-contained system. Archetypal criticism\u2019s charter.", ["archetype", "myth", "genre"]], ["The Norton Anthology of English Literature", "M.H. Abrams, editor", "W. W. Norton", 1962, "poetry", "Abrams\u2019s anthology canonized English literature for the classroom from Beowulf to the present. Its selections and headnotes shaped what generations read.", ["canon", "anthology", "period"]], ["MLA Handbook, 9th edition", "Modern Language Association", "Modern Language Association", 2021, "rhetoric", "The MLA\u2019s guide standardizes documentation, citation, and manuscript format for the humanities. The rulebook behind millions of student papers.", ["citation", "documentation", "format"]], ["The Rhetoric of Fiction", "Wayne C. Booth", "University of Chicago Press", 1961, "fiction", "Booth analyzes how authors control judgment through implied authors, reliable and unreliable narrators, and showing versus telling. Narratology\u2019s founding rhetoric.", ["narrator", "implied author", "showing"]], ["A Glossary of Literary Terms", "M.H. Abrams", "Holt, Rinehart and Winston", 1957, "literary-theory", "Abrams\u2019s glossary defines the critic\u2019s vocabulary \u2014 from allegory to zeugma \u2014 with examples. The reference shelf of every literature student.", ["term", "definition", "example"]], ["The Cambridge Grammar of the English Language", "Rodney Huddleston, Geoffrey K. Pullum", "Cambridge University Press", 2002, "rhetoric", "The 1,800-page descriptive grammar of English, built on evidence rather than prescription. The definitive reference for how English actually works.", ["grammar", "descriptive", "syntax"]], ["The Dialogic Imagination", "Mikhail Bakhtin", "University of Texas Press", 1981, "fiction", "Bakhtin\u2019s essays theorize the novel as heteroglossia \u2014 many voices in dialogue \u2014 with chronotope and carnival. The novel\u2019s deepest theorist.", ["heteroglossia", "chronotope", "carnival"]], ["The Elements of Style", "William Strunk Jr., E.B. White", "Macmillan", 1959, "rhetoric", "Strunk\u2019s rules and White\u2019s essay made concision a moral virtue: omit needless words. The most influential style manual in American English.", ["style", "concision", "usage"]], ["The Well Wrought Urn", "Cleanth Brooks", "Harcourt, Brace", 1947, "poetry", "Brooks\u2019s close readings argue the poem is a well-wrought urn \u2014 paradox and irony unified in structure. New Criticism\u2019s manifesto in practice.", ["close reading", "paradox", "irony"]], ["Orientalism", "Edward W. Said", "Pantheon", 1978, "literary-theory", "Said shows how Western scholarship constructed \u2018the Orient\u2019 as Europe\u2019s other, serving empire. The founding text of postcolonial criticism.", ["postcolonial", "discourse", "other"]], ["The Oxford English Dictionary", "Oxford University Press", "Oxford University Press", 1928, "translation", "The OED\u2019s historical dictionary traces every word\u2019s recorded life with dated quotations. The monument of English lexicography.", ["etymology", "quotation", "historical"]], ["Semiotics and the Philosophy of Language", "Umberto Eco", "Indiana University Press", 1984, "literary-theory", "Eco\u2019s essays on signs, codes, and interpretation bridge semiotics and philosophy. How meaning travels from text to reader.", ["semiotics", "code", "interpretation"]], ["The Translator\u2019s Invisibility", "Lawrence Venuti", "Routledge", 1995, "translation", "Venuti argues that fluent translation erases the translator and domesticates foreign texts, calling for visible, foreignizing strategies. Translation studies\u2019 polemic.", ["domestication", "foreignization", "visibility"]], ["AP English Literature and Composition Course Description", "College Board", "College Board", 2019, "fiction", "The College Board framework centers close reading of poetry, prose fiction, and drama with timed analytical writing. The national standard for advanced high-school literature.", ["close reading", "timed writing", "analysis"]], ["The Empty Space", "Peter Brook", "Atheneum", 1968, "drama", "Brook\u2019s four lectures divide theatre into deadly, holy, rough, and immediate. The modern director\u2019s handbook.", ["deadly theatre", "holy theatre", "immediacy"]]];
var PROJ=[["Reading in the Age of Generated Text", "Attention and trust when machines write."], ["The Future of the Novel", "Long form after the feed."], ["Machine Translation, Human Judgment", "Where the human still decides."], ["Digital Archives of World Literature", "Every text, searchable, compared."], ["Linguistics of Emoji and Meme", "Grammar of the pictographic turn."], ["The Canon Debates of 2040", "Who decides what lasts."], ["Narrative Medicine", "Stories as clinical instruments."], ["Poetry and Attention", "The poem as attention training."], ["Low-Resource Language NLP", "Models for the other six thousand languages."], ["Fan Fiction as Literature", "The archive that ate the canon."], ["Rhetoric of Synthetic Media", "Persuasion by generated voice and face."], ["Global English Literatures", "The novel in world Englishes."]];
var METHODS='corpus analysis, close reading trials, and reader-response studies';
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
