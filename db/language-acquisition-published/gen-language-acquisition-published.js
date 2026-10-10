(function(){'use strict';
/* JAH Language Acquisition Published Archive Database — deterministic boundless generator (jahdb-language-acquisition-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='language-acquisition-published';
var BASE='language-acquisition';
var GENVER='jahdb-language-acquisition-published-1.0';
var PREFIX='JAH-language-acquisition-published-P-';
var CATS=["phonetics", "syntax", "semantics", "sociolinguistics", "psycholinguistics", "pedagogy"];
var WORKS=[["Aspects of the Theory of Syntax", "Noam Chomsky", "MIT Press", 1965, "syntax", "Chomsky\u2019s standard theory distinguished deep and surface structure, arguing that children could not learn language without innate universal grammar. The poverty-of-the-stimulus argument that launched generative linguistics.", ["universal grammar", "deep structure", "innateness"]], ["The Language Instinct", "Steven Pinker", "William Morrow", 1994, "psycholinguistics", "Pinker argues that language is a human instinct, shaped by evolution and unfolding in children on a maturational schedule. The popular synthesis of Chomskyan nativism.", ["instinct", "evolution", "critical period"]], ["Principles and Practice in Second Language Acquisition", "Stephen Krashen", "Pergamon Press", 1982, "pedagogy", "Krashen\u2019s input hypothesis: acquisition happens through comprehensible input, with the affective filter gating progress. The monitor model that reshaped language teaching.", ["comprehensible input", "affective filter", "acquisition"]], ["Thought and Language", "Lev Vygotsky", "MIT Press", 1962, "psycholinguistics", "Vygotsky traces how children\u2019s egocentric speech becomes inner speech, arguing thought and language develop together socially. The zone of proximal development reframed learning itself.", ["inner speech", "zone of proximal development", "social"]], ["Common European Framework of Reference for Languages", "Council of Europe", "Cambridge University Press", 2001, "pedagogy", "The CEFR\u2019s A1\u2013C2 scales standardized proficiency levels across Europe and beyond. \u2018Can-do\u2019 descriptors now anchor curricula, tests, and textbooks worldwide.", ["proficiency", "can-do", "A1-C2"]], ["ACTFL Proficiency Guidelines", "American Council on the Teaching of Foreign Languages", "ACTFL", 1986, "pedagogy", "ACTFL\u2019s Novice-to-Distinguished scale defines U.S. foreign-language proficiency for speaking, writing, listening, and reading. The national standard for program outcomes.", ["proficiency", "novice", "distinguished"]], ["Early language acquisition: cracking the speech code", "Patricia K. Kuhl", "Nature Reviews Neuroscience", 2004, "phonetics", "Kuhl reviews how infants\u2019 perceptual narrowing tunes them to native phonemes by the first birthday. The neuroscience of the critical period\u2019s opening.", ["perceptual narrowing", "phoneme", "infancy"]], ["Maturational Constraints on Language Learning", "Elissa L. Newport", "Cognitive Science", 1990, "syntax", "Newport\u2019s \u2018less is more\u2019 hypothesis: children\u2019s limited processing may actually help them extract linguistic structure. Evidence for maturational limits on first and second language learning.", ["maturational", "less is more", "constraint"]], ["Verbal Behavior", "B.F. Skinner", "Appleton-Century-Crofts", 1957, "semantics", "Skinner analyzed language as operant behavior shaped by reinforcement \u2014 mands, tacts, echoics. Chomsky\u2019s famous review made the book the behaviorist foil for nativism.", ["operant", "reinforcement", "mand"]], ["Naming and Necessity", "Saul Kripke", "Harvard University Press", 1980, "semantics", "Kripke\u2019s lectures argue names are rigid designators, reviving essentialism against descriptivism. Analytic philosophy of language\u2019s landmark.", ["rigid designator", "necessity", "reference"]], ["First Language Acquisition", "Eve V. Clark", "Cambridge University Press", 2003, "psycholinguistics", "Clark\u2019s textbook follows children from babbling to complex syntax, weighing nativist and usage-based accounts. The field\u2019s standard developmental survey.", ["babbling", "overgeneralization", "development"]], ["Second Language Acquisition: An Introductory Course", "Susan M. Gass, Larry Selinker", "Lawrence Erlbaum", 1994, "pedagogy", "Gass and Selinker\u2019s course text maps SLA: interlanguage, input and interaction, and individual differences. The classroom standard for the discipline.", ["interlanguage", "input", "interaction"]], ["A Course in Phonetics", "Peter Ladefoged", "Harcourt Brace Jovanovich", 1975, "phonetics", "Ladefoged\u2019s phonetics text teaches articulatory description, the IPA, and acoustic analysis with practical exercises. How linguists hear and transcribe speech sounds.", ["IPA", "articulation", "acoustic"]], ["Bilingual: Life and Reality", "Fran\u00e7ois Grosjean", "Harvard University Press", 2010, "sociolinguistics", "Grosjean dismantles myths about bilinguals \u2014 they are not two monolinguals \u2014 and describes language modes and dominance. The humane introduction to bilingual life.", ["bilingualism", "language mode", "dominance"]], ["Sociolinguistics: An Introduction to Language and Society", "Peter Trudgill", "Penguin", 1974, "sociolinguistics", "Trudgill\u2019s introduction shows how class, region, and network shape speech, from Norwich to New York. The field\u2019s first popular text.", ["variation", "class", "network"]], ["Techniques and Principles in Language Teaching", "Diane Larsen-Freeman", "Oxford University Press", 1986, "pedagogy", "Larsen-Freeman surveys methods from Grammar-Translation to Communicative Language Teaching through classroom observation. The methods course in a book.", ["method", "communicative", "observation"]], ["WIDA English Language Development Standards", "WIDA Consortium", "Board of Regents, UW-Madison", 2020, "pedagogy", "WIDA\u2019s 2020 standards define what multilingual learners can do with language in content areas. The framework behind ACCESS testing in U.S. schools.", ["multilingual", "ACCESS", "can-do"]], ["The Language and Thought of the Child", "Jean Piaget", "Routledge & Kegan Paul", 1923, "psycholinguistics", "Piaget\u2019s early study found children\u2019s speech egocentric before it becomes socialized, tying language to cognitive stages. The constructivist starting point for developmental psycholinguistics.", ["egocentric speech", "stages", "constructivism"]]];
var PROJ=[["AI Conversation Partners", "Classroom trials of always-patient interlocutors."], ["Sign Language Acquisition at Scale", "What large datasets reveal about visual language."], ["Heritage Language Revival", "Programs bringing family languages back."], ["Brain-Computer Interfaces and Learning", "Neural feedback in vocabulary training."], ["The Critical Period Revisited", "New data on age effects."], ["Multilingual AI Tutors", "One tutor, forty languages."], ["Virtual Immersion", "Presence and proficiency in simulated worlds."], ["Early Screening for Language Delay", "Catching delay in the first thousand days."], ["Neuroscience of Bilingualism 2040", "What imaging finally settled."], ["Endangered Language Documentation", "Recording the last fluent speakers."], ["Accent and Identity", "Global Englishes and belonging."], ["Literacy After Screens", "Reading when text talks back."]];
var METHODS='longitudinal learner data, classroom trials, and corpus analysis';
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
