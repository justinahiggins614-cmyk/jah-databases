(function(){'use strict';
var SLUG='teacher-training-general-published';
var BASE='teacher-training-general';
var PREFIX='JAH-teacher-training-general-published-P-';
var FIELD='Teacher Training (General)';
var CATS=["pedagogy","classroom-management","assessment","professional-standards","mentoring","research"];
var WORKS=[{"w":"Those Who Understand: Knowledge Growth in Teaching","a":"Lee S. Shulman","p":"Educational Researcher","y":1986,"s":"Shulman's landmark article introducing pedagogical content knowledge — the blending of content and pedagogy unique to teaching — reframing what teachers need to know.","f":["Teaching requires pedagogical content knowledge, not just content.","PCK includes representations and student misconceptions.","The article launched a generation of teacher-knowledge research."],"c":["The missing paradigm","Content knowledge","Pedagogical content knowledge","Curricular knowledge","Research agenda","Implications"],"g":"pedagogy"},{"w":"Powerful Teacher Education: Lessons from Exemplary Programs","a":"Linda Darling-Hammond","p":"Jossey-Bass","y":2006,"s":"The study of seven exemplary teacher-education programs — their common features of coherence, clinical practice and inquiry — setting the bar for program quality.","f":["Coherence across coursework and clinical work matters most.","Extensive supervised clinical practice is essential.","Programs should prepare teachers as adaptive experts."],"c":["The programs","Coherence","Clinical practice","Inquiry","Equity","Policy lessons"],"g":"research"},{"w":"Enhancing Professional Practice: A Framework for Teaching","a":"Charlotte Danielson","p":"ASCD","y":1996,"s":"Danielson's four-domain framework — planning, classroom environment, instruction, professional responsibilities — the most widely used teaching-evaluation framework in the US.","f":["Teaching can be described in four domains and 22 components.","Distinguished practice is observable.","The framework supports both evaluation and growth."],"c":["Planning and preparation","Classroom environment","Instruction","Professional responsibilities","Levels of performance","Uses"],"g":"professional-standards"},{"w":"Handbook of Research on Teacher Education (3rd ed.)","a":"Marilyn Cochran-Smith, Sharon Feiman-Nemser, D. John McIntyre (eds.)","p":"Routledge","y":2008,"s":"The field-defining handbook — teacher learning, program design, policy, diversity, accountability — mapping what research says about preparing teachers.","f":["Teacher learning is developmental and situated.","Program effects are hard but possible to measure.","Accountability pressures reshape preparation."],"c":["Teacher learning","Program design","Diversity","Policy","Accountability","Research methods"],"g":"research"},{"w":"The First Days of School","a":"Harry K. Wong and Rosemary T. Wong","p":"Harry K. Wong Publications","y":1991,"s":"The practical classic on classroom procedures — the first days determine the year — with scripts for routines, discipline plans and procedures that prevent management problems.","f":["Procedures, not rules alone, run classrooms.","The first days set the year's trajectory.","Effective teachers manage; ineffective ones discipline."],"c":["The effective teacher","Procedures","Routines","Discipline plans","First days scripts","Consistency"],"g":"classroom-management"},{"w":"National Board Certification Standards","a":"National Board for Professional Teaching Standards","p":"NBPTS","y":2016,"s":"The US advanced-certification standards — what accomplished teachers should know and be able to do — across certificate areas, with portfolio assessment.","f":["Accomplished teaching is definable and assessable.","Portfolio evidence captures real practice.","Certification correlates with student gains."],"c":["The five propositions","Certificate areas","Portfolio entries","Assessment","Renewal","Research base"],"g":"professional-standards"},{"w":"Learning to Teach: A Handbook for Primary and Secondary School Teachers","a":"Representative teacher-education handbook authors","p":"Routledge","y":2010,"s":"A representative comprehensive handbook for initial teacher training — planning, behavior, assessment, inclusion, and the professional year.","f":["Planning must connect aims to assessment.","Behavior management is taught, not innate.","Reflection structures professional growth."],"c":["Planning","Behavior","Assessment","Inclusion","The professional year","Reflection"],"g":"pedagogy"},{"w":"Mentoring Beginning Teachers: Guiding, Reflecting, Coaching","a":"Jean Boreen, Mary K. Johnson, Donna Niday, Joe Potts","p":"Stenhouse","y":2000,"s":"The guide to mentoring novice teachers — mentor roles, observation cycles, reflective conversation — from induction-program research.","f":["Structured mentoring cuts early-career attrition.","Observation cycles beat drop-in visits.","Reflective conversation builds judgment."],"c":["Mentor roles","The first weeks","Observation cycles","Reflective conversation","Difficult situations","Program design"],"g":"mentoring"},{"w":"Classroom Management That Works","a":"Robert J. Marzano, Jana S. Marzano, Debra J. Pickering","p":"ASCD","y":2003,"s":"The meta-analytic synthesis on classroom management — rules, disciplinary interventions, teacher-student relationships, mental set — with effect sizes for each.","f":["Rules and procedures have large effects.","Teacher-student relationships prevent problems.","Withitness — awareness — matters."],"c":["Rules and procedures","Disciplinary interventions","Relationships","Mental set","Student responsibility","Implementation"],"g":"classroom-management"},{"w":"Teacher Assessment and the Quest for Teacher Quality","a":"Mary Diez (ed.)","p":"Jossey-Bass","y":2010,"s":"The edited volume on assessing teacher candidates and practicing teachers — performance assessment, portfolios, value-added, and the politics of measurement.","f":["Performance assessment captures teaching better than tests.","Multiple measures are essential.","Assessment design shapes preparation."],"c":["Candidate assessment","Performance assessment","Value-added","Portfolios","Politics","Future directions"],"g":"assessment"},{"w":"Studying Teacher Education: The AERA Panel Report","a":"Marilyn Cochran-Smith and Kenneth M. Zeichner (eds.)","p":"Lawrence Erlbaum","y":2005,"s":"The AERA panel's research synthesis on teacher education — what is known about teacher learning, program features, and policy effects.","f":["Evidence on program effects is thin but growing.","Clinical experience quality varies widely.","Policy contexts shape everything."],"c":["Teacher learning","Program features","Diversity","Policy","Methodology","Agenda"],"g":"research"},{"w":"The Skillful Teacher: Building Your Teaching Skills","a":"Jon Saphier and Robert Gower","p":"Research for Better Teaching","y":1982,"s":"The practitioner text on the repertoire of teaching skills — classroom climate, curriculum planning, motivation, and the craft knowledge of effective teaching.","f":["Teaching is a repertoire of learnable skills.","Climate precedes curriculum.","Management and instruction are inseparable."],"c":["Climate","Planning","Motivation","Management","Instruction","Professionalism"],"g":"pedagogy"}];
var TOPICS=[{"t":"Projected global teacher-competency passport, 2033 horizon","b":"Extends qualification-recognition work into a portable teacher passport.","f":["Cross-border hiring becomes routine.","Competency evidence is standardized."],"o":["Competencies","Evidence","Recognition","Governance"],"g":"professional-standards"},{"t":"Projected clinical-practice residency standard, 2030 horizon","b":"Projects medical-residency models onto a year-long teaching residency standard.","f":["Residency graduates outperform traditionally prepared peers.","Mentor quality is the binding constraint."],"o":["Residency design","Mentors","Assessment","Funding"],"g":"mentoring"},{"t":"Projected AI classroom-simulation trainer, 2032 horizon","b":"Extends simulation training into an AI pupil-simulation standard.","f":["Simulated practice transfers to real classrooms.","Difficult scenarios are rehearsed safely."],"o":["Simulation","Scenarios","Transfer","Ethics"],"g":"classroom-management"},{"t":"Projected teacher-wellbeing national standard, 2029 horizon","b":"Projects burnout research into a binding wellbeing standard.","f":["Workload caps become enforceable.","Retention improves measurably."],"o":["Workload","Support","Measurement","Enforcement"],"g":"professional-standards"},{"t":"Projected pedagogical-content-knowledge test bank, 2031 horizon","b":"Extends PCK research into an open, validated test bank.","f":["PCK becomes directly measurable.","Programs use results to improve."],"o":["Domains","Items","Validation","Use"],"g":"assessment"},{"t":"Projected micro-teaching video library standard, 2028 horizon","b":"Projects video-based reflection into a shared library standard.","f":["Annotated exemplars accelerate novice growth.","Privacy rules protect pupils."],"o":["Library","Annotation","Privacy","Training"],"g":"pedagogy"},{"t":"Projected induction-program quality mark, 2030 horizon","b":"Extends induction research into a quality mark for programs.","f":["Marked programs retain more novices.","The mark drives funding."],"o":["Criteria","Audit","Funding","Review"],"g":"mentoring"},{"t":"Projected culturally-responsive pedagogy code, 2031 horizon","b":"Projects culturally-responsive research into a practice code.","f":["The code is co-written with communities.","Classroom climates improve."],"o":["Principles","Practices","Community role","Monitoring"],"g":"pedagogy"},{"t":"Projected teacher-researcher fellowship program, 2034 horizon","b":"Extends action-research traditions into a national fellowship.","f":["Fellows' findings change local practice.","Research literacy spreads."],"o":["Fellowship","Methods","Dissemination","Careers"],"g":"research"},{"t":"Projected classroom-observation AI protocol, 2033 horizon","b":"Extends observation research into an ethical AI-observation protocol.","f":["Observation becomes continuous and low-stakes.","Bias audits are mandatory."],"o":["Protocol","Bias audits","Teacher control","Uses"],"g":"assessment"},{"t":"Projected second-career teacher pathway, 2029 horizon","b":"Projects career-changer programs into a national pathway.","f":["Career changers fill shortage subjects.","Tailored pedagogy training is essential."],"o":["Pathway","Pedagogy","Mentoring","Retention"],"g":"mentoring"},{"t":"Projected behavior-support whole-school standard, 2030 horizon","b":"Extends positive-behavior research into a whole-school standard.","f":["Exclusions fall sharply.","Consistency across staff is the lever."],"o":["Tiers","Training","Data","Consistency"],"g":"classroom-management"},{"t":"Projected teacher-education research census, 2035 horizon","b":"A standing census of teacher-education research quality.","f":["Weak designs are flagged publicly.","Funding follows rigor."],"o":["Criteria","Flagging","Funding","Updates"],"g":"research"},{"t":"Projected professional-learning community standard, 2028 horizon","b":"Projects PLC research into an implementation standard.","f":["Structured PLCs raise achievement.","Facilitation quality decides outcomes."],"o":["Structure","Facilitation","Evidence","Scale"],"g":"professional-standards"}];
var FNOTES=["Pedagogy records note the knowledge type addressed — content, PCK, or general pedagogy.","Classroom-management records distinguish prevention from intervention strategies.","Assessment records state whether the instrument targets candidates or practicing teachers.","Standards records name the issuing body and the certification level.","Mentoring records carry the induction-phase focus — survival, consolidation, or renewal.","Research records note the synthesis type — narrative, meta-analytic, or panel report."];
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
var gen={version:'jahdb-teacher-training-general-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();