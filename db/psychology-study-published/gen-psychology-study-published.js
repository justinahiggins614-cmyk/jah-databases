(function(){'use strict';
/* JAH Psychology Published Archive Database — deterministic boundless generator (jahdb-psychology-study-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='psychology-study-published';
var BASE='psychology-study';
var GENVER='jahdb-psychology-study-published-1.0';
var PREFIX='JAH-psychology-study-published-P-';
var CATS=["clinical", "cognitive", "developmental", "social", "behavioral", "neuroscience"];
var WORKS=[["The Interpretation of Dreams", "Sigmund Freud", "Franz Deuticke", 1900, "clinical", "Freud\u2019s dream book presents the unconscious, wish fulfillment, and the Oedipus complex through dream analysis. Psychoanalysis\u2019 founding text.", ["unconscious", "dream", "repression"]], ["The Principles of Psychology", "William James", "Henry Holt", 1890, "cognitive", "James\u2019s two-volume Principles covers habit, attention, memory, and the stream of thought. American psychology\u2019s founding textbook.", ["stream of thought", "habit", "attention"]], ["Beyond Freedom and Dignity", "B.F. Skinner", "Alfred A. Knopf", 1971, "behavioral", "Skinner argues that behavior is shaped by contingencies of reinforcement, not inner freedom. Radical behaviorism\u2019s public manifesto.", ["reinforcement", "contingency", "behaviorism"]], ["The Psychology of the Child", "Jean Piaget, B\u00e4rbel Inhelder", "Basic Books", 1969, "developmental", "Piaget and Inhelder summarize the stages \u2014 sensorimotor to formal operations \u2014 of children\u2019s cognitive growth. Development\u2019s stage theory.", ["stages", "schema", "assimilation"]], ["Diagnostic and Statistical Manual of Mental Disorders, 5th edition", "American Psychiatric Association", "American Psychiatric Publishing", 2013, "clinical", "The DSM-5 standardizes psychiatric diagnosis by symptom criteria across hundreds of disorders. Clinical psychology\u2019s shared language.", ["diagnosis", "criteria", "disorder"]], ["Motivation and Personality", "Abraham H. Maslow", "Harper & Brothers", 1954, "developmental", "Maslow\u2019s hierarchy \u2014 physiological needs to self-actualization \u2014 reframed motivation positively. Humanistic psychology\u2019s landmark.", ["hierarchy of needs", "self-actualization", "motivation"]], ["Client-Centered Therapy", "Carl R. Rogers", "Houghton Mifflin", 1951, "clinical", "Rogers presents unconditional positive regard, empathy, and congruence as therapy\u2019s curative conditions. Person-centered practice began here.", ["empathy", "congruence", "unconditional regard"]], ["Cognitive Psychology", "Ulric Neisser", "Appleton-Century-Crofts", 1967, "cognitive", "Neisser\u2019s book named the cognitive revolution, treating mind as information processing. The field-defining text of modern cognitive science.", ["information processing", "cognition", "revolution"]], ["Eyewitness Testimony", "Elizabeth F. Loftus", "Harvard University Press", 1979, "cognitive", "Loftus showed how easily memory is distorted by suggestion, challenging courtroom reliance on eyewitnesses. Memory\u2019s most consequential research.", ["memory", "misinformation", "eyewitness"]], ["Obedience to Authority", "Stanley Milgram", "Harper & Row", 1974, "social", "Milgram\u2019s experiments showed ordinary people administering apparent shocks under authority. Social psychology\u2019s most famous \u2014 and debated \u2014 finding.", ["obedience", "authority", "experiment"]], ["AP Psychology Course and Exam Description", "College Board", "College Board", 2019, "developmental", "The College Board framework spans biological bases, cognition, and social psychology for secondary students. The U.S. standard for high-school psychology.", ["biological bases", "cognition", "exam"]], ["The Social Animal", "Elliot Aronson", "W.H. Freeman", 1972, "social", "Aronson\u2019s text presents social psychology through experiments on conformity, persuasion, and prejudice. The humane classic of the field.", ["conformity", "persuasion", "prejudice"]], ["Influence: The Psychology of Persuasion", "Robert Cialdini", "William Morrow", 1984, "social", "Cialdini\u2019s six principles of persuasion \u2014 reciprocity, commitment, social proof, authority, liking, scarcity \u2014 from field experiments. Social psychology\u2019s practical classic.", ["persuasion", "reciprocity", "social proof"]], ["Mindset: The New Psychology of Success", "Carol S. Dweck", "Random House", 2006, "developmental", "Dweck\u2019s research contrasts fixed and growth mindsets, showing beliefs about ability shape achievement. The mindset idea that entered classrooms worldwide.", ["growth mindset", "fixed mindset", "achievement"]], ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "Summit Books", 1985, "neuroscience", "Sacks\u2019s case histories \u2014 visual agnosia, Tourette\u2019s, phantom limbs \u2014 reveal the brain through its disorders. Neurology written as human story.", ["case study", "agnosia", "brain"]], ["The Brain That Changes Itself", "Norman Doidge", "Viking", 2007, "neuroscience", "Doidge\u2019s case studies present neuroplasticity \u2014 the brain rewiring itself through experience. The popular account of the plastic brain.", ["neuroplasticity", "rewiring", "recovery"]], ["Conditioned Reflexes", "Ivan P. Pavlov", "Oxford University Press", 1927, "behavioral", "Pavlov\u2019s lectures detail classical conditioning from the salivating dog experiments. Learning theory\u2019s experimental foundation.", ["conditioning", "stimulus", "response"]]];
var PROJ=[["Digital Phenotyping", "Mental health signals in phone data."], ["Psychedelic-Assisted Therapy", "Trial evidence and protocols."], ["Psychology of Algorithmic Feeds", "What recommendation does to mind."], ["Longevity and the Aging Mind", "Cognition across longer lives."], ["AI Therapists", "Efficacy, alliance, and ethics."], ["Collective Trauma and Recovery", "How communities heal."], ["Attention Restoration", "Recovering focus in noisy environments."], ["The Science of Belonging", "Measuring what connection does."], ["Sleep in the Always-On City", "Rest under constant light and ping."], ["Moral Psychology of Machines", "How we judge artificial agents."], ["Resilience Curricula", "Teaching bounce-back in schools."], ["Climate Anxiety", "The psychology of a warming world."]];
var METHODS='controlled trials, longitudinal cohorts, and meta-analysis';
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
