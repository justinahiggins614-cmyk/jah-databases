(function(){'use strict';
var SLUG='software-development-published';
var PREFIX='JAH-software-development-published-P-';
var STUDY='software-development';
var FIELD='Software and Applications Development and Analysis';
var CATS=["software-engineering","design-patterns","programming-practice","algorithms","analysis","agile"];
var DATA={"works":[{"t":"The Mythical Man-Month","a":"Frederick P. Brooks Jr.","p":"Addison-Wesley","y":1995,"g":"software-engineering","ref":"ISBN 978-0201835953, Addison-Wesley, anniversary edition.","ov":"Brooks's classic essays on software project management, drawn from leading IBM's OS/360 development.","f":["Adding people to a late project makes it later.","Conceptual integrity is the most important property of a system."],"ch":["the tar pit","the mythical man-month","the surgical team","no silver bullet"]},{"t":"Design Patterns: Elements of Reusable Object-Oriented Software","a":"Erich Gamma; Richard Helm; Ralph Johnson; John Vlissides","p":"Addison-Wesley","y":1994,"g":"design-patterns","ref":"ISBN 978-0201633610, Addison-Wesley.","ov":"The Gang of Four catalog of 23 object-oriented design patterns that gave the industry a shared vocabulary.","f":["Named patterns let teams discuss designs at a higher level.","Favoring composition over inheritance reduces brittle hierarchies."],"ch":["creational patterns","structural patterns","behavioral patterns","pattern applicability"]},{"t":"Clean Code","a":"Robert C. Martin","p":"Prentice Hall","y":2008,"g":"programming-practice","ref":"ISBN 978-0132350884, Prentice Hall.","ov":"A handbook of agile software craftsmanship: readable code, meaningful names, functions, and testing discipline.","f":["Readable code is cheaper to change than clever code.","Boy-scout rule: leave the code cleaner than you found it."],"ch":["meaningful names","functions","comments","unit testing"]},{"t":"Code Complete, 2nd Edition","a":"Steve McConnell","p":"Microsoft Press","y":2004,"g":"programming-practice","ref":"ISBN 978-0735619678, Microsoft Press.","ov":"An encyclopedic, research-backed guide to software construction, from design to debugging.","f":["Construction is the largest single cost driver in most projects.","Defensive programming catches errors where they are cheapest."],"ch":["design in construction","working classes","high-quality routines","debugging"]},{"t":"The Pragmatic Programmer","a":"Andrew Hunt; David Thomas","p":"Addison-Wesley","y":2019,"g":"programming-practice","ref":"ISBN 978-0135957059, Addison-Wesley, 20th anniversary edition.","ov":"Tips and philosophy for pragmatic software development, from DRY to tracer bullets.","f":["Every piece of knowledge should have one authoritative representation.","Prototype to learn; tracer code to ship."],"ch":["a pragmatic philosophy","pragmatic tools","pragmatic paranoia","while you are coding"]},{"t":"Refactoring: Improving the Design of Existing Code","a":"Martin Fowler","p":"Addison-Wesley","y":2018,"g":"programming-practice","ref":"ISBN 978-0134757599, Addison-Wesley, 2nd edition.","ov":"The catalog of refactorings with tests-first discipline for improving code without changing behavior.","f":["Refactoring is safe only with a solid test suite.","Small, behavior-preserving steps compound into clean design."],"ch":["the first refactoring","principles in refactoring","code smells","encapsulate variable"]},{"t":"Introduction to Algorithms","a":"Thomas H. Cormen; Charles E. Leiserson; Ronald L. Rivest; Clifford Stein","p":"MIT Press","y":2009,"g":"algorithms","ref":"ISBN 978-0262033848, MIT Press, 3rd edition.","ov":"The standard algorithms textbook: analysis, sorting, data structures, graphs, and NP-completeness.","f":["Asymptotic analysis predicts real performance trends.","Choosing the right data structure dominates micro-optimization."],"ch":["foundations","sorting and order statistics","data structures","graph algorithms"]},{"t":"Structure and Interpretation of Computer Programs","a":"Harold Abelson; Gerald Jay Sussman","p":"MIT Press","y":1996,"g":"algorithms","ref":"ISBN 978-0262510875, MIT Press, 2nd edition.","ov":"MIT's legendary text teaching programming as a way to think about processes, using Scheme.","f":["Programming is about controlling complexity, not instructing machines.","Data abstraction separates use from representation."],"ch":["building abstractions with procedures","building abstractions with data","modularity and state","metalinguistic abstraction"]},{"t":"Software Engineering","a":"Ian Sommerville","p":"Pearson","y":2015,"g":"software-engineering","ref":"ISBN 978-0133943030, Pearson, 10th edition.","ov":"A broad survey of software engineering: processes, requirements, design, testing, and management.","f":["Process choice should fit project risk, not fashion.","Requirements errors are the most expensive to fix late."],"ch":["software processes","requirements engineering","system modeling","software testing"]},{"t":"Domain-Driven Design","a":"Eric Evans","p":"Addison-Wesley","y":2003,"g":"analysis","ref":"ISBN 978-0321125217, Addison-Wesley.","ov":"Tackling complexity in the heart of software by modeling the business domain explicitly.","f":["A ubiquitous language shared by developers and domain experts prevents misbuilt features.","Bounded contexts keep large models coherent."],"ch":["the ubiquitous language","model-driven design","supple design","strategic design"]},{"t":"Working Effectively with Legacy Code","a":"Michael Feathers","p":"Prentice Hall","y":2004,"g":"analysis","ref":"ISBN 978-0131177055, Prentice Hall.","ov":"Techniques for bringing untested legacy code under test so it can be changed safely.","f":["Legacy code is simply code without tests.","Seams let you break dependencies without rewriting everything."],"ch":["the mechanics of change","characterization tests","breaking dependencies","getting classes under test"]},{"t":"Agile Estimating and Planning","a":"Mike Cohn","p":"Prentice Hall","y":2005,"g":"agile","ref":"ISBN 978-0131479418, Prentice Hall.","ov":"Practical methods for estimating and planning agile projects with stories, points, and velocity.","f":["Story points estimate size, not time, and teams calibrate over iterations.","Planning is continuous; plans are disposable."],"ch":["estimating with story points","planning by theme","tracking velocity","iteration planning"]}],"lvl2":[{"t":"Projected AI-pair-programming craftsmanship guide","g":"programming-practice","b":"AI coding assistants are changing daily developer workflow.","d":"Projects a craftsmanship guide for reviewing, testing, and owning AI-generated code as a professional discipline."},{"t":"Projected formal-verification field manual","g":"software-engineering","b":"Proof assistants are reaching mainstream-critical software.","d":"Projects a field manual applying lightweight formal methods to everyday services, not just kernels and crypto."},{"t":"Projected pattern language for agent systems","g":"design-patterns","b":"Multi-agent software needs shared design vocabulary.","d":"Projects a catalog of agent coordination patterns: orchestrator, critic, tool-router, and memory-tier designs."},{"t":"Projected requirements engineering for ML features","g":"analysis","b":"Probabilistic features break traditional requirements practice.","d":"Projects methods for specifying, testing, and accepting features whose outputs are statistical rather than deterministic."},{"t":"Projected sustainable software engineering handbook","g":"agile","b":"Energy cost of software is becoming a design constraint.","d":"Projects a handbook for measuring and reducing the carbon footprint of builds, deploys, and running services."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad7(n){var s=String(n);while(s.length<7)s='0'+s;return s;}
var ANGLES=['Abstract and scope','Chapter outline','Key findings','Curriculum notes'];
var SITE_SLUGS=['signature-math','jah-calculator','jah-dictionary','jah-wiki','jah-n-wiki-leaks','signature-llama','jah-ai-models','cyber-patent-catalog','signature-one-archive','jah-computer-systems','signature-books','signature-comics','signature-newspapers','signature-backend','signature-boundless-generators','signature-ai-mixlab','signature-ai-olypics','signature-chip-maker','signature-app-archive','signature-ai-robot-matcher','signature-experiment-solver','signature-ai-image-video-maker','signature-ai-song-maker','signature-fixit','signature-university','signature-earth','signature-flight-school','signature-game-store','signature-website-creator','signature-antivirus','signature-os-updater','signature-space-mapping','signature-cookbook','signature-spell-check','signature-image-grid-measure','signature-cyber-mega-mall','signature-3d-print'];
function angleNote(angle){
  if(angle==='Chapter outline')return 'Study angle: chapter outline. Readers work the table of contents as a syllabus, summarizing each chapter\'s method before moving on. ';
  if(angle==='Key findings')return 'Study angle: key findings. This record distills the results and recommendations a practitioner would quote on the job. ';
  if(angle==='Curriculum notes')return 'Study angle: curriculum notes. Instructors can teach the material in twelve sessions, pairing each reading with a hands-on exercise. ';
  return 'Study angle: abstract and scope. This entry states what the work covers, who it is written for, and where it sits in the field. ';
}
function buildLevel1(rnd,w,angle){
  var title=w.t+' \u2014 '+angle;
  var chs=[];for(var i=0;i<w.ch.length;i++)chs.push('Chapter '+(i+1)+': '+w.ch[i]+'.');
  var content='Published work: \u201C'+w.t+'\u201D by '+w.a.replace(/;/g,',')+' ('+w.p+', '+w.y+'). '+w.ov+
   ' Key findings: '+w.f[0]+' '+w.f[1]+
   ' Contents: '+chs.join(' ')+
   ' '+angleNote(angle)+
   ' Publication: '+w.p+'. Source: '+w.ref;
  return {title:title,content:content};
}
function buildLevel2(rnd,cat){
  var pool=DATA.lvl2.filter(function(x){return !x.g||x.g===cat;});
  if(!pool.length)pool=DATA.lvl2;
  var tp=pick(pool,rnd);
  var title='Level 2: '+tp.t;
  var content='Level 2 projection record for the '+FIELD+' published archive. Projected entry: \u201C'+tp.t+'\u201D. '+
   'Trend basis: '+tp.b+' Projected content: '+tp.d+
   ' Issued in: JAH '+FIELD+' Published Archive, projection series. '+
   'Confidence: projection, derived from the direction of the archived published works, not from a real publication. Nothing here is cited as fact; the entry models where the literature points next.';
  return {title:title,content:content};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var wl=DATA.works.filter(function(w){return w.g===cat;});
  if(!wl.length)wl=DATA.works;
  var level=rnd()<0.55?1:2;
  var id=PREFIX+pad7(seed);
  var sig='../'+STUDY+'-study/index.html?sig=JAH-'+STUDY+'-STUDY-S-'+pad7(seed);
  var rec;
  if(level===1){
    var w=pick(wl,rnd);
    var b=buildLevel1(rnd,w,pick(ANGLES,rnd));
    rec={id:id,title:b.title,authors:w.a.split(';').map(function(s){return s.trim();}).filter(Boolean),
      publication:w.p,year:w.y,full_content:b.content,source_ref:w.ref,signature_link:sig,level:1,category:cat,_seed:seed};
  }else{
    var b2=buildLevel2(rnd,cat);
    var pa=pick(DATA.projAuthors,rnd);
    rec={id:id,title:b2.title,authors:[pa],publication:'JAH '+FIELD+' Published Archive, projection series',year:2026,
      full_content:b2.content,source_ref:'Projection record; no external citation. Derived from archive trend basis.',signature_link:sig,level:2,category:cat,_seed:seed};
  }
  return rec;
}
var CHECKS=[
 ['object',function(r){return (r&&typeof r==='object')?'':'not an object';}],
 ['id-type',function(r){return typeof r.id==='string'?'':'id not string';}],
 ['id-format',function(r){return new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{7}$').test(r.id)?'':'id format';}],
 ['id-seed',function(r){return r.id.slice(-7)===pad7(r._seed)?'':'id/seed mismatch';}],
 ['title-type',function(r){return typeof r.title==='string'?'':'title not string';}],
 ['title-len',function(r){return (r.title.length>=12&&r.title.length<=220)?'':'title length';}],
 ['authors-arr',function(r){return (Array.isArray(r.authors)&&r.authors.length>=1)?'':'authors array';}],
 ['authors-items',function(r){return r.authors.every(function(a){return typeof a==='string'&&a.length>=3;})?'':'author item';}],
 ['publication-type',function(r){return (typeof r.publication==='string'&&r.publication.length>=3)?'':'publication';}],
 ['year-range',function(r){return (Number.isInteger(r.year)&&r.year>=1800&&r.year<=2026)?'':'year';}],
 ['content-type',function(r){return typeof r.full_content==='string'?'':'content not string';}],
 ['content-min',function(r){return r.full_content.length>=400?'':'content too short';}],
 ['content-max',function(r){return r.full_content.length<=4000?'':'content too long';}],
 ['content-sentences',function(r){return ((r.full_content.match(/[.!?]/g)||[]).length>=3)?'':'content sentences';}],
 ['content-clean',function(r){return !/lorem|TBD|TODO|\bxxx\b/i.test(r.full_content)?'':'content placeholder';}],
 ['content-no-stub',function(r){return !/\bstub\b/i.test(r.full_content)?'':'content stub';}],
 ['source-type',function(r){return (typeof r.source_ref==='string'&&r.source_ref.length>=8)?'':'source_ref';}],
 ['siglink-type',function(r){return typeof r.signature_link==='string'?'':'signature_link type';}],
 ['siglink-format',function(r){return new RegExp('^\\.\\./'+STUDY+'-study/index\\.html\\?sig=JAH-'+STUDY+'-STUDY-S-\\d{7}$').test(r.signature_link)?'':'signature_link format';}],
 ['siglink-seed',function(r){return r.signature_link.indexOf(pad7(r._seed))>=0?'':'signature_link seed';}],
 ['level-val',function(r){return (r.level===1||r.level===2)?'':'level value';}],
 ['level2-title',function(r){return (r.level!==2||/^Level 2/.test(r.title))?'':'level2 title';}],
 ['level1-title',function(r){return (r.level!==1||!/^Level 2/.test(r.title))?'':'level1 title';}],
 ['level2-projection',function(r){return (r.level!==2||/projection/i.test(r.full_content))?'':'level2 projection word';}],
 ['level1-authors',function(r){return (r.level!==1||!/unknown/i.test(r.authors.join(' ')))?'':'level1 authors';}],
 ['category-valid',function(r){return CATS.indexOf(r.category)>=0?'':'category';}],
 ['seed-num',function(r){return (Number.isInteger(r._seed)&&r._seed>=1)?'':'_seed';}],
 ['json-roundtrip',function(r){return JSON.parse(JSON.stringify(r)).id===r.id?'':'json roundtrip';}],
 ['no-undefined',function(r){return Object.keys(r).every(function(k){return r[k]!==undefined;})?'':'undefined value';}],
 ['content-pub',function(r){return (r.level!==1||r.full_content.indexOf(r.publication)>=0)?'':'content lacks publication';}],
 ['title-id',function(r){return r.title!==r.id?'':'title==id';}],
 ['siglink-relative',function(r){return r.signature_link.indexOf('../')===0?'':'siglink relative';}],
 ['no-site-slugs',function(r){var t=(r.title+' '+r.full_content).toLowerCase();return !SITE_SLUGS.some(function(s){return t.indexOf(s)>=0;})?'':'site slug referenced';}],
 ['no-orig-website',function(r){return !/original website/i.test(r.title+' '+r.full_content)?'':'original-website phrase';}],
 ['level2-year',function(r){return (r.level!==2||r.year===2026)?'':'level2 year';}],
 ['level1-ref',function(r){return (r.level!==1||/ISBN|doi|RFC|ISO|NFPA|FAA|Codex|Tetra|Handbook|open textbook|lulu|IPC|FDA/i.test(r.source_ref))?'':'level1 ref weak';}],
 ['category-nonempty',function(r){return (typeof r.category==='string'&&r.category.length>=2)?'':'category empty';}],
 ['title-spacing',function(r){return !/  /.test(r.title)?'':'title double space';}],
 ['content-no-html',function(r){return !/[<>]/.test(r.full_content)?'':'content has angle brackets';}],
 ['content-no-breakword',function(r){return r.full_content.indexOf('word-break')<0?'':'content css leak';}]
];
function validate(r){
  var e=[];
  for(var i=0;i<CHECKS.length;i++){var m='';try{m=CHECKS[i][1](r);}catch(x){m='threw '+x.message;}if(m)e.push(CHECKS[i][0]+': '+m);}
  return {ok:!e.length,errors:e};
}
function selfTest(){
  var fails=[];
  for(var s=1;s<=40;s++){
    var r=generate(s);
    for(var i=0;i<CHECKS.length;i++){var m='';try{m=CHECKS[i][1](r);}catch(x){m='threw '+x.message;}if(m)fails.push({seed:s,check:CHECKS[i][0],msg:m});}
  }
  return {seeds:40,checksPerSeed:CHECKS.length,total:40*CHECKS.length,failures:fails,ok:fails.length===0};
}
var gen={version:'jahdb-software-development-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
