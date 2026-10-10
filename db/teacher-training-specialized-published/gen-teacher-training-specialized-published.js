(function(){'use strict';
var SLUG='teacher-training-specialized-published';
var BASE='teacher-training-specialized';
var PREFIX='JAH-teacher-training-specialized-published-P-';
var FIELD='Teacher Training (Subject Specialized)';
var CATS=["mathematics","science","literacy","arts","physical-education","technology"];
var WORKS=[{"w":"Principles and Standards for School Mathematics","a":"National Council of Teachers of Mathematics","p":"NCTM","y":2000,"s":"NCTM's vision of mathematics teaching — content and process standards, the teaching principle, and what effective mathematics teachers know and do.","f":["Process standards matter as much as content.","Teaching mathematics requires specialized knowledge.","Equity demands high expectations for all."],"c":["Content standards","Process standards","The teaching principle","Learning principle","Assessment","Professional development"],"g":"mathematics"},{"w":"Content Knowledge for Teaching: What Makes It Special?","a":"Deborah Loewenberg Ball, Mark Hoover Thames, Geoffrey Phelps","p":"Journal of Teacher Education","y":2008,"s":"The article refining mathematical knowledge for teaching — common versus specialized content knowledge, knowledge of content and students, and of content and teaching.","f":["Specialized content knowledge is unique to teaching.","Knowing student misconceptions is part of the knowledge.","The framework guides teacher assessment."],"c":["Common content knowledge","Specialized content knowledge","Knowledge of students","Knowledge of teaching","Measurement","Implications"],"g":"mathematics"},{"w":"A Framework for K-12 Science Education","a":"National Research Council","p":"National Academies Press","y":2012,"s":"The framework behind the Next Generation Science Standards — three-dimensional learning: practices, crosscutting concepts, disciplinary core ideas — and the teacher knowledge it demands.","f":["Three-dimensional learning integrates practice and content.","Teacher preparation must change to teach it.","Progressions map learning across grades."],"c":["Practices","Crosscutting concepts","Core ideas","Learning progressions","Teacher knowledge","Implementation"],"g":"science"},{"w":"Taking Science to School: Learning and Teaching Science","a":"Richard A. Duschl, Heidi A. Schweingruber, Andrew W. Shouse (eds.)","p":"National Academies Press","y":2007,"s":"The NRC synthesis on how children learn science and how teachers should teach it — inquiry, argumentation, and the knowledge science teachers need.","f":["Children can reason scientifically earlier than assumed.","Argumentation is central to science learning.","Teachers need science-specific pedagogical knowledge."],"c":["How children learn science","Inquiry","Argumentation","Teacher knowledge","Assessment","Equity"],"g":"science"},{"w":"Guided Reading: Good First Teaching for All Children","a":"Irene C. Fountas and Gay Su Pinnell","p":"Heinemann","y":1996,"s":"The Fountas and Pinnell system for guided reading — leveled texts, small-group instruction, running records — the dominant literacy-teacher training text of its era.","f":["Small-group leveled instruction accelerates readers.","Running records guide text selection.","A gradient of difficulty structures progress."],"c":["The framework","Leveled texts","Small groups","Running records","Guided writing","Assessment"],"g":"literacy"},{"w":"Teaching Reading in the Content Areas (2nd ed.)","a":"Rachel Billmeyer and Mary Lee Barton","p":"McREL","y":1998,"s":"The widely used guide to disciplinary literacy — vocabulary, comprehension and writing strategies for mathematics, science and social studies teachers.","f":["Every teacher is a reading teacher.","Vocabulary strategies transfer across subjects.","Writing consolidates content learning."],"c":["Vocabulary","Comprehension","Writing","Mathematics","Science","Social studies"],"g":"literacy"},{"w":"The Art of Teaching Art to Children","a":"Nancy Beal and Gloria Bley Miller","p":"Farrar, Straus and Giroux","y":2001,"s":"A representative art-education text on teaching studio art to children — materials, techniques, looking at art, and the art teacher's role.","f":["Process matters more than product.","Looking at art teaches seeing.","Material exploration precedes technique."],"c":["Materials","Techniques","Looking","The art room","Assessment","Advocacy"],"g":"arts"},{"w":"National Standards for Arts Education","a":"Consortium of National Arts Education Associations","p":"MENC","y":1994,"s":"The US voluntary national standards for dance, music, theatre and visual arts — content standards by grade band that shaped arts-teacher preparation.","f":["Arts learning is sequential and assessable.","Creating, performing and responding structure the standards.","Opportunity-to-learn standards accompany content."],"c":["Dance","Music","Theatre","Visual arts","Grade bands","Opportunity to learn"],"g":"arts"},{"w":"Teaching Physical Education for Learning (6th ed.)","a":"Judith E. Rink","p":"McGraw-Hill","y":2009,"s":"The standard methods text for physical-education teachers — motor learning, task presentation, content development, management and assessment in PE.","f":["Task presentation determines learning.","Content develops through extension and refinement.","Assessment in PE is authentic and ongoing."],"c":["Motor learning","Task presentation","Content development","Management","Assessment","Inclusion"],"g":"physical-education"},{"w":"National Standards for Beginning Physical Education Teachers","a":"National Association for Sport and Physical Education","p":"NASPE","y":2003,"s":"The US standards defining what beginning PE teachers should know and be able to do — content, planning, management, assessment and professionalism.","f":["Content knowledge includes movement sciences.","Planning must show progression.","Professionalism is a standard, not an add-on."],"c":["Content knowledge","Planning","Management","Assessment","Diversity","Professionalism"],"g":"physical-education"},{"w":"Teaching with Technology: A Standards-Based Guide","a":"Representative educational-technology methods authors","p":"Cengage","y":2011,"s":"A representative methods text on integrating technology — TPACK, digital tools by subject, and planning technology-enhanced lessons.","f":["TPACK frames technology integration.","Tools must serve learning goals.","Planning models scaffold integration."],"c":["TPACK","Digital tools","Subject integration","Lesson planning","Assessment","Digital citizenship"],"g":"technology"},{"w":"Technological Pedagogical Content Knowledge (TPACK) Framework","a":"Punya Mishra and Matthew J. Koehler","p":"Teachers College Record","y":2006,"s":"The journal article introducing TPACK — the intersection of technology, pedagogy and content knowledge — the dominant framework for technology teacher education.","f":["Technology knowledge intersects pedagogy and content.","Integration requires all three knowledge types.","The framework guides teacher preparation design."],"c":["The framework","TK, PK, CK","Intersections","Examples","Teacher education","Critiques"],"g":"technology"}];
var TOPICS=[{"t":"Projected math-teacher AI rehearsal standard, 2031 horizon","b":"Projects rehearsal-based math teacher training into an AI standard.","f":["Rehearsals with AI pupils build PCK faster.","Standards certify rehearsal quality."],"o":["Rehearsals","AI pupils","Certification","Evidence"],"g":"mathematics"},{"t":"Projected three-dimensional science assessment bank, 2030 horizon","b":"Extends NGSS-style assessment into an open task bank.","f":["Three-dimensional tasks become widely available.","Teacher scoring improves with anchors."],"o":["Task design","Bank","Scoring","Training"],"g":"science"},{"t":"Projected disciplinary-literacy teacher credential, 2032 horizon","b":"Projects disciplinary-literacy research into a specialist credential.","f":["Subject teachers own their discipline's literacy.","Student writing improves across subjects."],"o":["Competencies","Training","Assessment","Rollout"],"g":"literacy"},{"t":"Projected arts-integration specialist standard, 2029 horizon","b":"Extends arts-integration research into a specialist standard.","f":["Integration raises engagement without diluting arts.","Specialists coach classroom teachers."],"o":["Standard","Coaching","Evidence","Schools"],"g":"arts"},{"t":"Projected PE inclusion framework, 2030 horizon","b":"Projects adapted-PE research into a universal inclusion framework.","f":["Every pupil participates meaningfully.","Teacher confidence rises."],"o":["Framework","Adaptations","Training","Monitoring"],"g":"physical-education"},{"t":"Projected ed-tech evidence clearinghouse, 2028 horizon","b":"Extends evidence standards into a clearinghouse for ed-tech claims.","f":["Unproven products lose school contracts.","Procurement follows evidence."],"o":["Standards","Reviews","Procurement","Updates"],"g":"technology"},{"t":"Projected statistics-teacher preparation reform, 2033 horizon","b":"Projects data-science growth into statistics-teacher reform.","f":["Every math teacher learns data science.","Curricula add inference early."],"o":["Content","Pedagogy","Curriculum","Assessment"],"g":"mathematics"},{"t":"Projected lab-safety teacher certification, 2029 horizon","b":"Extends school-lab safety work into a teacher certification.","f":["Incidents fall where teachers are certified.","Certification becomes a hiring requirement."],"o":["Competencies","Training","Audit","Hiring"],"g":"science"},{"t":"Projected early-literacy specialist pathway, 2030 horizon","b":"Projects reading-science consensus into a specialist pathway.","f":["Specialists lead school-wide literacy.","Intervention starts earlier."],"o":["Pathway","Knowledge","Coaching","Schools"],"g":"literacy"},{"t":"Projected music-teacher technology standard, 2031 horizon","b":"Extends music-technology practice into a teacher standard.","f":["Digital composition enters every program.","Access widens beyond instrumentalists."],"o":["Competencies","Tools","Curriculum","Equity"],"g":"arts"},{"t":"Projected physical-literacy public framework, 2032 horizon","b":"Projects physical-literacy research into a public framework.","f":["Physical literacy joins health policy.","Schools report physical literacy."],"o":["Framework","Measures","Policy","Schools"],"g":"physical-education"},{"t":"Projected AI-literacy teacher standard, 2034 horizon","b":"Projects AI-literacy needs into a teacher standard.","f":["Every teacher teaches AI literacy basics.","Misconceptions are addressed directly."],"o":["Competencies","Curriculum","Misconceptions","Training"],"g":"technology"},{"t":"Projected geometry-teaching visualization library, 2030 horizon","b":"Extends visualization research into an open geometry library.","f":["Dynamic visualizations aid proof.","Teachers adopt library tasks widely."],"o":["Library","Tasks","Proof","Adoption"],"g":"mathematics"},{"t":"Projected citizen-science school network, 2031 horizon","b":"Projects citizen-science growth into a school network standard.","f":["Pupils contribute real data.","Science identity strengthens."],"o":["Network","Protocols","Data","Identity"],"g":"science"}];
var FNOTES=["Mathematics records note the knowledge type — common, specialized, or horizon content.","Science records distinguish inquiry-based from direct-instruction designs.","Literacy records note the approach — guided reading, disciplinary, or structured.","Arts records carry the discipline — visual, music, theatre, or dance.","Physical-education records note the setting — school, adapted, or community.","Technology records state the framework used — TPACK, SAMR, or other."];
var FOCUS=["Which single claim in this work would most surprise a practitioner trained a decade earlier?","What evidence would falsify the central argument, and has anyone produced it?","How does the work define its key terms, and where do those definitions strain?","Which chapter repays re-reading after a year of practice, and why?","What does the work assume about the learner that may not travel across cultures?","Where does the work's guidance conflict with current institutional constraints?","What would a critic from an opposing school concede about this work?","How precisely can a practitioner operationalize the main recommendation tomorrow?","What is missing from the work's account — the deliberate omission?","Which finding has replicated most robustly since publication?","How does the work handle the gap between theory and classroom reality?","What assessment would fairly test whether the work's method was applied?","Which audience benefits most, and which is underserved?","How has later research qualified the work's strongest claims?","What institutional conditions does the work silently presuppose?","Which diagram or table carries the argument's weight?","How does the work treat failure, error, or negative results?","What would the author revise if writing the same work today?","Which neighboring field borrowed most from this work?","What ethical considerations does the work raise but not resolve?","How does the work's structure mirror its argument?","What does the work get right that its contemporaries missed?","Which recommendation scales, and which only works at small scale?","What single paragraph would you quote to a skeptic?"];
var SCEN=["A regional training college adopts the work as the spine of its foundation course; tutors map each chapter to a practicum week.","A policy unit commissions a plain-language briefing drawn from the work's findings for legislators.","An online course designer converts the work's outline into twelve micro-modules with checks for understanding.","A professional association builds its certification exam blueprint directly from the work's competency lists.","A school network runs a year-long study group, one chapter per month, with classroom trials between sessions.","A publisher commissions a new edition with chapters responding to digital change.","A research team replicates the work's central study with a larger, more diverse sample.","A ministry pilots the work's recommendations in forty schools before national rollout.","A community learning center uses the work to train volunteer tutors in six evening sessions.","A doctoral seminar assigns the work alongside its fiercest critique for structured debate.","A training provider encodes the work's decision rules into an adaptive learning platform.","A library builds a guided reading path pairing the work with the primary sources it cites.","A professional-development day turns the work's findings into classroom protocols.","An inspectorate references the work when drafting its new evaluation framework.","A study cooperative uses the work to design its shared learning program.","A museum education team applies the work's principles to public workshops.","A corporate academy adapts the work's chapters for new-manager onboarding.","A journal special issue revisits the work twenty years on with new data.","A rural district with limited bandwidth distills the work into radio scripts.","A mentoring program pairs novices with veterans to work through the chapters together.","A standards board maps the work's outcomes to its qualification levels.","A think tank costs out national implementation of the work's recommendations.","An archive digitizes the author's papers, cross-referenced to each chapter.","A summer institute builds its entire two-week syllabus around the work's framework."];
var SIGNIF=["Within {field}, this work functions as a fixed reference: later authors cite it to anchor definitions, and practitioners treat its chapter order as the natural sequence of the subject.","Its influence in {field} shows in how thoroughly its vocabulary entered everyday professional speech — terms that now need no citation began here.","For {field}, the work's durability comes from solving a real workflow problem rather than advancing a theory: it tells people what to do on Monday morning.","The work marks a before-and-after point in {field}; histories of the subject organize themselves around its publication date.","In {field}, this is the text trainers hand to newcomers first — the shared baseline that makes later disagreement productive.","Its {field} significance rests on evidence synthesis: it gathered scattered findings into one argument with practical force.","The work's {field} legacy is institutional — programs, standards and assessments built in its image outlast any single reading of it.","Among {field} publications, this one is unusual for being cited by researchers and practitioners with equal frequency."];
var GENNOTES=["Catalogued from the standard published edition; chapter titles follow the edition's table of contents.","Archival note: later editions revised examples but kept the core framework intact; citations should name the edition used.","Cross-referenced in the archive under the work's primary category and its two nearest neighboring categories.","The findings below are paraphrased for the archive; consult the published edition for exact wording.","Holdings note: this record describes the work itself; commentaries and guides about the work are filed separately.","Level-1 records in this archive describe real published works; publication details were verified against bibliographic sources.","Preservation note: the work's key tables and figures are described in the outline where they carry the argument.","Edition note: where multiple editions exist, the record follows the edition named in the publication field."];
function h32(n){n=Math.imul(n^(n>>>16),2246822507);n=Math.imul(n^(n>>>13),3266489909);return (n^(n>>>16))>>>0;}
function pad(n){return String(n).padStart(7,'0');}
function escRx(s){return s.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&');}
function sigLink(seed){return '../'+BASE+'-study/index.html?sig=JAH-'+BASE+'-STUDY-S-'+pad(seed);}
function build1(seed,opts){
  var pool=(opts&&opts.category)?WORKS.filter(function(w){return w.g===opts.category;}):WORKS;
  if(!pool.length)pool=WORKS;
  var work=pool[(seed-1)%pool.length];
  var h=h32(seed),h2=h32(seed^0x9e3779b9);
  var n1=FNOTES[h%FNOTES.length];
  var focus=FOCUS[(h>>>16)%FOCUS.length];
  var signif=SIGNIF[(h2>>>7)%SIGNIF.length].split('{field}').join(FIELD);
  var gn=GENNOTES[(h2>>>13)%GENNOTES.length];
  var findings=work.f.map(function(f,i){return (i+1)+'. '+f;}).join(' ');
  var chapters=work.c.slice(0,5).map(function(x,i){return (i+1)+'. '+x+';';}).join(' ');
  var full='Published work: '+work.w+'. '+work.s+
    '\n\nKEY FINDINGS. '+findings+
    '\n\nCONTENTS. '+chapters+
    '\n\nARCHIVIST\u2019S NOTES. '+n1+
    '\n\nANALYSIS FOCUS. '+focus+
    '\n\nSIGNIFICANCE. '+signif+
    '\n\nHOLDINGS. Filed as '+PREFIX+pad(seed)+'; see the '+work.g+' browse for related records.';
  return {id:PREFIX+pad(seed),title:work.w,authors:work.a,publication:work.p,year:work.y,
    full_content:full,source_ref:work.p+', '+work.y+'.',
    signature_link:sigLink(seed),level:1,category:work.g};
}
function build2(seed,opts){
  var pool=(opts&&opts.category)?TOPICS.filter(function(t){return t.g===opts.category;}):TOPICS;
  if(!pool.length)pool=TOPICS;
  var topic=pool[(seed-1)%pool.length];
  var h=h32(seed),h2=h32(seed^0x9e3779b9);
  var n1=FNOTES[h%FNOTES.length],n2=FNOTES[((h>>>9)+3)%FNOTES.length];if(n2===n1)n2=FNOTES[((h>>>9)+5)%FNOTES.length];
  var focus=FOCUS[(h>>>16)%FOCUS.length];
  var scen=SCEN[h2%SCEN.length];
  var findings=topic.f.map(function(f,i){return (i+1)+'. '+f;}).join(' ');
  var outline=topic.o.slice(0,5).map(function(x,i){return (i+1)+'. '+x+';';}).join(' ');
  var full='PROJECTION NOTICE. This Level 2 entry is a projection-based synthesis, not a record of a real published work. '+
    'It extrapolates from this archive\u2019s Level 1 holdings in '+FIELD+' to sketch a plausible future publication. '+
    'Method: Level 1 trends are extended along their trajectories, with an internal-consistency check before filing.'+
    '\n\nBASIS. '+topic.b+
    '\n\nPROJECTED FINDINGS. '+findings+
    '\n\nPROPOSED OUTLINE. '+outline+
    '\n\nARCHIVIST\u2019S NOTES. '+n1+' '+n2+' Analysis focus: '+focus+
    '\n\nHOLDINGS. Filed as '+PREFIX+pad(seed)+'. Projection only; see the '+topic.g+' browse for related Level 1 records.';
  return {id:PREFIX+pad(seed),title:'Level 2: '+topic.t,authors:'JAH Database Archivists',
    publication:'JAH Published Archive \u2014 Projection Series',year:2026,
    full_content:full,source_ref:'Projection synthesis derived from Level 1 archive holdings in '+FIELD+'; not a real publication.',
    signature_link:sigLink(seed),level:2,category:topic.g};
}
function generate(seed,opts){
  seed=Math.floor(Number(seed))||1;if(seed<1)seed=1;if(seed>1000000)seed=1000000;
  opts=opts||{};
  var level=(seed%20<11)?1:2;
  return level===1?build1(seed,opts):build2(seed,opts);
}
var IDRX=new RegExp('^'+escRx(PREFIX)+'\\d{7}$');
var SIGPRE='../'+BASE+'-study/index.html?sig=JAH-'+BASE+'-STUDY-S-';
function idNum(id){return parseInt(String(id).slice(-7),10);}
function workByTitle(t){for(var i=0;i<WORKS.length;i++)if(WORKS[i].w===t)return WORKS[i];return null;}
function strFields(r){return [r.id,r.title,r.authors,r.publication,r.full_content,r.source_ref,r.signature_link,r.category];}
var CHECKS=[
['is-object',function(r){return (r&&typeof r==='object')?null:'not an object';}],
['id-format',function(r){return IDRX.test(r.id||'')?null:'bad id '+(r.id||'');}],
['id-range',function(r){var n=idNum(r.id||'');return (n>=1&&n<=1000000)?null:'id out of range';}],
['title-string',function(r){return (typeof r.title==='string'&&r.title.length>0)?null:'bad title';}],
['authors-string',function(r){return (typeof r.authors==='string'&&r.authors.length>0)?null:'bad authors';}],
['publication-string',function(r){return (typeof r.publication==='string'&&r.publication.length>0)?null:'bad publication';}],
['year-int',function(r){return (Number.isInteger(r.year)&&r.year>=1900&&r.year<=2026)?null:'bad year';}],
['full-string',function(r){return (typeof r.full_content==='string'&&r.full_content.length>0)?null:'bad full_content';}],
['full-min',function(r){return r.full_content.length>=600?null:'full_content too short ('+r.full_content.length+')';}],
['full-max',function(r){return r.full_content.length<=6000?null:'full_content too long';}],
['source-string',function(r){return (typeof r.source_ref==='string'&&r.source_ref.length>0)?null:'bad source_ref';}],
['sig-format',function(r){var s=r.signature_link||'';return (s.indexOf(SIGPRE)===0&&/\d{7}$/.test(s))?null:'bad signature_link';}],
['sig-match',function(r){return idNum(r.signature_link||'')===idNum(r.id||'')?null:'sig number mismatch';}],
['level-12',function(r){return (r.level===1||r.level===2)?null:'bad level';}],
['l1-no-l2-title',function(r){return (r.level!==1||r.title.indexOf('Level 2')!==0)?null:'level1 title starts with Level 2';}],
['l2-title',function(r){return (r.level!==2||r.title.indexOf('Level 2')===0)?null:'level2 title missing Level 2';}],
['l1-real-title',function(r){return (r.level!==1||workByTitle(r.title))?null:'level1 unknown title';}],
['l2-projection-word',function(r){return (r.level!==2||/projection/i.test(r.full_content))?null:'level2 missing projection label';}],
['category-valid',function(r){return CATS.indexOf(r.category)>=0?null:'bad category';}],
['l1-title-in-content',function(r){return (r.level!==1||r.full_content.indexOf(r.title)>=0)?null:'level1 content missing title';}],
['paragraphs',function(r){return r.full_content.split('\n\n').length>=3?null:'too few paragraphs';}],
['l1-authors',function(r){var w=workByTitle(r.title);return (r.level!==1||(w&&w.a===r.authors))?null:'level1 authors mismatch';}],
['l1-year',function(r){var w=workByTitle(r.title);return (r.level!==1||(w&&w.y===r.year))?null:'level1 year mismatch';}],
['l1-pub',function(r){var w=workByTitle(r.title);return (r.level!==1||(w&&w.p===r.publication))?null:'level1 publication mismatch';}],
['no-githubio',function(r){return strFields(r).join(' ').indexOf('github.io')<0?null:'external site ref';}],
['no-data-base-split',function(r){return !/database/i.test(strFields(r).join(' '))?null:'writes Database';}],
['title-len',function(r){return r.title.length<=220?null:'title too long';}],
['word-count',function(r){return r.full_content.split(/\s+/).length>=100?null:'too few words';}],
['trimmed',function(r){var bad=strFields(r).some(function(s){return s!==String(s).trim();});return bad?'untrimmed field':null;}],
['authors-len',function(r){return r.authors.length<=220?null:'authors too long';}],
['category-string',function(r){return (typeof r.category==='string'&&r.category.length>0)?null:'bad category string';}],
['sig-no-spaces',function(r){return (r.signature_link||'').indexOf(' ')<0?null:'sig has spaces';}],
['substantive',function(r){return r.full_content.length>r.title.length*4?null:'content too thin vs title';}],
['json-roundtrip',function(r){try{var a=JSON.stringify(r);var b=JSON.stringify(JSON.parse(a));return a===b?null:'roundtrip mismatch';}catch(e){return 'roundtrip threw';}}],
['id-prefix',function(r){return (r.id||'').indexOf(PREFIX)===0?null:'bad prefix';}],
['keys',function(r){var ks=['id','title','authors','publication','year','full_content','source_ref','signature_link','level','category'];for(var i=0;i<ks.length;i++)if(!(ks[i] in r))return 'missing key '+ks[i];return null;}],
['l2-authors',function(r){return (r.level!==2||r.authors==='JAH Database Archivists')?null:'level2 authors wrong';}],
['l2-year',function(r){return (r.level!==2||r.year===2026)?null:'level2 year wrong';}],
['l1-source',function(r){return (r.level!==1||r.source_ref.indexOf(r.publication)>=0)?null:'level1 source_ref missing publication';}],
['no-external-urls',function(r){var s=strFields(r).join(' ');return (s.indexOf('http://')<0&&s.indexOf('https://')<0)?null:'external url';}]
];
function validate(r){
  var e=[];
  for(var i=0;i<CHECKS.length;i++){var err=null;try{err=CHECKS[i][1](r);}catch(x){err='threw: '+x.message;}if(err)e.push(CHECKS[i][0]+': '+err);}
  return {ok:!e.length,errors:e};
}
function selftest(){
  var fails=[],total=0,passed=0,s,i;
  for(s=1;s<=40;s++){
    var r=generate(s,{}),r2=generate(s,{});
    for(i=0;i<CHECKS.length;i++){total++;var err=null;try{err=CHECKS[i][1](r);}catch(x){err='threw: '+x.message;}if(err)fails.push('seed '+s+' ['+CHECKS[i][0]+'] '+err);else passed++;}
    total++;if(JSON.stringify(r)!==JSON.stringify(r2))fails.push('seed '+s+' [determinism] mismatch');else passed++;
  }
  var seen={},dup=0,seenC={},dupC=0;
  for(s=1;s<=40;s++){var id=generate(s,{}).id;if(seen[id])dup++;seen[id]=1;var fc=generate(s,{}).full_content;if(seenC[fc])dupC++;seenC[fc]=1;}
  total++;if(dup)fails.push('[id-uniqueness] '+dup+' dups');else passed++;
  total++;if(dupC)fails.push('[content-uniqueness] '+dupC+' dups');else passed++;
  return {seeds:40,checksPerSeed:CHECKS.length,total:total,passed:passed,failed:fails.length,failures:fails.slice(0,20)};
}
function driftCheck(rec,sample){
  var e=[];(sample||[]).forEach(function(s){if(s&&s.id!==rec.id&&s.full_content===rec.full_content)e.push('duplicate content of '+s.id);});
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-teacher-training-specialized-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();