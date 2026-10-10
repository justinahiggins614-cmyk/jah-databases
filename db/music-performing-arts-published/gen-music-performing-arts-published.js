(function(){'use strict';
/* JAH Music and Performing Arts Published Archive Database — deterministic boundless generator (jahdb-music-performing-arts-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='music-performing-arts-published';
var BASE='music-performing-arts';
var GENVER='jahdb-music-performing-arts-published-1.0';
var PREFIX='JAH-music-performing-arts-published-P-';
var CATS=["music-theory", "performance", "composition", "dance", "theater", "ethnomusicology"];
var WORKS=[["The Joy of Music", "Leonard Bernstein", "Simon & Schuster", 1959, "performance", "Bernstein\u2019s essays and Young People\u2019s Concerts scripts argue that musical meaning is heard, not explained \u2014 from Beethoven\u2019s Fifth to jazz. The book demystifies form, melody, and orchestration for general readers without dumbing them down.", ["musical form", "orchestration", "listening"]], ["What to Listen for in Music", "Aaron Copland", "McGraw-Hill", 1939, "music-theory", "Copland teaches three planes of listening \u2014 sensuous, expressive, and musical \u2014 and walks readers through rhythm, melody, harmony, tone color, and form. A classic listener\u2019s guide that treats attention itself as a skill.", ["rhythm", "melody", "musical form"]], ["Theory of Harmony", "Arnold Schoenberg", "University of California Press", 1978, "music-theory", "Schoenberg\u2019s Harmonielehre teaches harmony from the overtone series through diatonic and chromatic practice, insisting that rules serve musical ideas. It bridges common-practice tonality and the path to atonality.", ["overtone series", "chromaticism", "voice leading"]], ["The History of Musical Instruments", "Curt Sachs", "W. W. Norton", 1940, "ethnomusicology", "Sachs surveys instruments worldwide by his Hornbostel-Sachs classification \u2014 idiophones, membranophones, chordophones, aerophones \u2014 tracing how instrument design follows musical need across cultures.", ["Hornbostel-Sachs", "aerophone", "chordophone"]], ["An Actor Prepares", "Constantin Stanislavski", "Theatre Arts Books", 1936, "theater", "Stanislavski\u2019s fictional acting student learns the \u2018system\u2019: relaxation, concentration, emotion memory, and the through-line of action. The book founded modern realist acting and the Method that grew from it.", ["emotion memory", "objective", "through-line"]], ["Towards a Poor Theatre", "Jerzy Grotowski", "Simon & Schuster", 1968, "theater", "Grotowski strips theatre to the actor-audience encounter, rejecting spectacle for the performer\u2019s total physical and vocal act. The book records his laboratory productions and the via negativa \u2014 removing blocks rather than adding skills.", ["poor theatre", "via negativa", "performer"]], ["Brecht on Theatre", "Bertolt Brecht", "Hill and Wang", 1964, "theater", "Willett\u2019s selection of Brecht\u2019s writings presents epic theatre: the alienation effect, gestus, and historicization, all aimed at making audiences think rather than merely feel. The theoretical backbone of political theatre.", ["alienation effect", "gestus", "epic theatre"]], ["Modern Educational Dance", "Rudolf Laban", "Macdonald & Evans", 1948, "dance", "Laban\u2019s movement theory \u2014 effort, space, and shape \u2014 gave dance education a vocabulary for analyzing how bodies move. His notation ideas and movement choirs made dance teachable as a discipline of expression.", ["effort", "kinesphere", "notation"]], ["Apollo\u2019s Angels: A History of Ballet", "Jennifer Homans", "Random House", 2010, "dance", "Homans traces ballet from the French courts through Petipa\u2019s Russia, Diaghilev, and Balanchine to the present, arguing that ballet\u2019s story is inseparable from aristocratic patronage, revolution, and national identity.", ["ballet", "Petipa", "Balanchine"]], ["The Study of Ethnomusicology", "Bruno Nettl", "University of Illinois Press", 1983, "ethnomusicology", "Nettl defines the field\u2019s core questions \u2014 what music is, how it changes, and what fieldwork can know \u2014 reviewing thirty-one issues from transcription to urban musical life. The standard map of the discipline.", ["fieldwork", "transcription", "musical culture"]], ["The Enjoyment of Music", "Kristine Forney, Joseph Machlis", "W. W. Norton", 1955, "performance", "The long-running appreciation textbook pairs listening guides with cultural context from chant to contemporary. Its outline-based listening maps teach students to hear structure in real time.", ["listening guide", "style period", "texture"]], ["Harmony", "Walter Piston", "W. W. Norton", 1941, "music-theory", "Piston\u2019s harmony text codified American conservatory practice: triads, seventh chords, modulation, and chromatic harmony with exercises drawn from the literature. Generations of composers learned voice leading from it.", ["triad", "modulation", "voice leading"]], ["Counterpoint", "Kent Kennan", "Prentice-Hall", 1959, "composition", "Kennan teaches species counterpoint through fugue, grounding strict technique in Bach\u2019s practice. The book\u2019s graded exercises move from cantus firmus to full fugue exposition.", ["species counterpoint", "fugue", "cantus firmus"]], ["The Study of Orchestration", "Samuel Adler", "W. W. Norton", 1982, "composition", "Adler\u2019s orchestration manual details every orchestral instrument\u2019s range, transposition, and color, with score excerpts and workbook exercises. The working reference for arrangers and composers.", ["transposition", "range", "timbre"]], ["The Craft of Musical Composition", "Paul Hindemith", "Schott", 1937, "composition", "Hindemith builds composition technique from two-part writing upward, with his own theory of harmonic tension. A composer\u2019s craft manual from a working master.", ["harmonic tension", "two-part writing", "craft"]], ["AP Music Theory Course and Exam Description", "College Board", "College Board", 2019, "music-theory", "The College Board\u2019s framework for AP Music Theory covers pitch, rhythm, harmony, voice leading, and aural skills. It standardizes what secondary students must hear, read, and write.", ["sight-singing", "figured bass", "cadence"]]];
var PROJ=[["AI-Assisted Orchestration Pedagogy", "Tutors that critique student scorings against repertoire models."], ["Holographic Stagecraft Standards", "Safety and sightline norms for volumetric performance."], ["A Unified Rhythm Notation", "One system spanning West African, Indian, and Western meters."], ["Adaptive Music Therapy Protocols", "Personalized interventions measured against clinical outcomes."], ["The 2040 Conservatory Curriculum", "What elite training keeps, and what it finally drops."], ["Immersive Opera", "Audience members staged as the chorus."], ["Motion-Capture Dance Preservation", "Full-body archives of endangered dance forms."], ["Generative Counterpoint Tutors", "Species exercises with instant stylistic feedback."], ["Post-Screen Concert Formats", "Live music designed for shared physical space again."], ["Cross-Cultural Improvisation Method", "A pedagogy bridging jazz, maqam, and raga improvisation."], ["Biometric Performance Training", "Heart-rate and breath data guiding practice sessions."], ["Community Choir Networks", "Thousands of local choirs linked in seasonal festivals."]];
var METHODS='rehearsal observation, score analysis, and interviews with performers';
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
