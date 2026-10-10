(function(){'use strict';
var SLUG='computer-use-published';
var PREFIX='JAH-computer-use-published-P-';
var STUDY='computer-use';
var FIELD='Computer Use';
var CATS=["computer-basics","hardware","software-use","digital-literacy","certification"];
var DATA={"works":[{"t":"Computer Systems: A Programmer's Perspective","a":"Randal E. Bryant; David R. O'Hallaron","p":"Pearson","y":2015,"g":"computer-basics","ref":"ISBN 978-0134092669, Pearson, 3rd edition.","ov":"A landmark text that teaches computer systems from the programmer's point of view, covering data representation, machine-level programming, and program optimization.","f":["Students who learn machine-level representation write programs that run measurably faster and use less memory.","Understanding caching and memory hierarchy explains most real-world performance puzzles."],"ch":["information storage and manipulation","machine-level representation of programs","processor architecture","optimizing program performance"]},{"t":"Code: The Hidden Language of Computer Hardware and Software","a":"Charles Petzold","p":"Microsoft Press","y":2000,"g":"computer-basics","ref":"ISBN 978-0735611313, Microsoft Press.","ov":"Builds a working computer from first principles, starting with Morse code and relays and ending with a programmable machine.","f":["Every abstraction in computing can be grounded in switches, relays, and binary codes.","Readers finish able to explain how hardware executes software without hand-waving."],"ch":["codes and combinations","relays and logic gates","building an adder","automating addition and subtraction"]},{"t":"The Pattern on the Stone","a":"W. Daniel Hillis","p":"Basic Books","y":1998,"g":"computer-basics","ref":"ISBN 978-0465025961, Basic Books.","ov":"Explains the simple ideas behind computers — stored programs, universality, and parallelism — for a general audience.","f":["A handful of simple ideas explains the entire architecture of modern computers.","Parallelism, not raw clock speed, is the path to greater computing power."],"ch":["building blocks","universal building blocks","programming","how computers remember"]},{"t":"How Computers Work","a":"Ron White","p":"Que","y":2014,"g":"hardware","ref":"ISBN 978-0789749840, Que, 10th edition.","ov":"An illustrated tour of PC hardware, from boot-up to networking, aimed at everyday users and technicians.","f":["Visual explanations let non-specialists diagnose common hardware failures.","Each subsystem is shown in the context of the whole machine it serves."],"ch":["how computers boot up","microchips and memory","storage devices","how the internet works"]},{"t":"Inside the Machine","a":"Jon Stokes","p":"No Starch Press","y":2007,"g":"hardware","ref":"ISBN 978-1593271046, No Starch Press.","ov":"An engineering introduction to microprocessors and computer architecture, from transistors to superscalar pipelines.","f":["Instruction-level parallelism is the central idea behind modern CPU design.","RISC and CISC converged because both hit the same physical limits."],"ch":["transistors and logic","the von Neumann model","pipelining","caches and memory systems"]},{"t":"The Elements of Computing Systems","a":"Noam Nisan; Shimon Schocken","p":"MIT Press","y":2005,"g":"hardware","ref":"ISBN 978-0262640688, MIT Press.","ov":"The Nand2Tetris course: students build a complete computer and operating system from NAND gates up.","f":["Building every layer demystifies the hardware-software interface.","A working Hack computer can be assembled from first principles in one course."],"ch":["Boolean logic","machine language","computer architecture","the operating system"]},{"t":"Upgrading and Repairing PCs","a":"Scott Mueller","p":"Que","y":2015,"g":"hardware","ref":"ISBN 978-0789756107, Que, 22nd edition.","ov":"The standard technician reference for PC components, assembly, troubleshooting, and upgrades.","f":["Systematic diagnosis beats part-swapping for repair success.","Component specifications determine compatibility more than brand names do."],"ch":["system components","processors","motherboards","troubleshooting and maintenance"]},{"t":"Absolute Beginner's Guide to Computer Basics","a":"Michael Miller","p":"Que","y":2013,"g":"software-use","ref":"ISBN 978-0789754516, Que, 6th edition.","ov":"A plain-language guide to everyday computing: files, applications, email, and the web.","f":["New users learn fastest by doing real tasks, not memorizing menus.","File management is the skill that unlocks everything else."],"ch":["understanding your computer","working with files","using the internet","staying safe online"]},{"t":"Computer Literacy BASICS: A Comprehensive Guide to IC3","a":"Connie Morrison; Dolores Wells","p":"Cengage Learning","y":2014,"g":"digital-literacy","ref":"ISBN 978-1285766587, Cengage Learning, 4th edition.","ov":"Curriculum aligned to the IC3 digital literacy certification: computing fundamentals, key applications, and living online.","f":["Certification-aligned curricula raise measurable digital skills.","The three IC3 domains map cleanly to workplace computer tasks."],"ch":["computing fundamentals","key applications","living online","practice assessments"]},{"t":"Using Information Technology","a":"Brian K. Williams; Stacey C. Sawyer","p":"McGraw-Hill","y":2012,"g":"digital-literacy","ref":"ISBN 978-0073516776, McGraw-Hill, 10th edition.","ov":"A complete introduction to information technology concepts, applications, and issues for college students.","f":["Conceptual understanding outlasts any single software version.","Ethics and security belong in every IT course, not an appendix."],"ch":["the internet and the web","system software","application software","networks and security"]},{"t":"Digital Competence Framework for Citizens (DigComp 2.2)","a":"European Commission; Joint Research Centre","p":"Publications Office of the European Union","y":2022,"g":"digital-literacy","ref":"JRC Science for Policy Report, doi 10.2760/490274, Publications Office of the EU.","ov":"The European reference framework defining digital competence across five areas and eight proficiency levels.","f":["Digital competence can be described in 21 competences across 5 areas.","AI-related competences were added to reflect emerging technology."],"ch":["information and data literacy","communication and collaboration","digital content creation","safety and problem solving"]},{"t":"CompTIA A+ Certification All-in-One Exam Guide","a":"Mike Meyers","p":"McGraw-Hill","y":2022,"g":"certification","ref":"ISBN 978-1264711122, McGraw-Hill, 11th edition.","ov":"The best-selling study guide for the CompTIA A+ technician certification exams.","f":["Hands-on labs predict exam success better than reading alone.","The A+ objectives mirror real help-desk and technician duties."],"ch":["operational procedures","PC hardware","networking","security and troubleshooting"]}],"lvl2":[{"t":"Projected 2031 desktop literacy curriculum","g":"digital-literacy","b":"Rising AI-assisted interfaces are changing what basic computer skills mean.","d":"Projects a curriculum where prompt literacy, file hygiene, and verification habits replace menu memorization as core skills."},{"t":"Projected home lab hardware syllabus","g":"hardware","b":"Low-cost single-board computers keep getting more capable.","d":"Projects a build-your-own syllabus around modular boards, covering power, storage, and networking with real measurements."},{"t":"Projected accessibility-first software guide","g":"software-use","b":"Regulations and user demand push accessibility into default design.","d":"Projects a guide teaching screen readers, voice control, and keyboard workflows as primary skills rather than accommodations."},{"t":"Projected technician certification roadmap","g":"certification","b":"Certifications increasingly test troubleshooting under time pressure.","d":"Projects a performance-based exam roadmap with live labs for hardware, OS, and network faults."},{"t":"Projected first-principles computing course","g":"computer-basics","b":"Nand2Tetris-style courses keep proving construction beats memorization.","d":"Projects a one-semester build-a-computer course ending in a student-written operating system on student-built hardware."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-computer-use-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
