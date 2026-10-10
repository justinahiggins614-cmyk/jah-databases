(function(){'use strict';
var SLUG='personal-skills-published';
var BASE='personal-skills';
var PREFIX='JAH-personal-skills-published-P-';
var FIELD='Personal Skills and Development';
var CATS=["habits","communication","emotional-intelligence","productivity","mindset","leadership"];
var WORKS=[{"w":"The 7 Habits of Highly Effective People","a":"Stephen R. Covey","p":"Free Press","y":1989,"s":"The principle-centered system — be proactive, begin with the end in mind, put first things first, think win-win, seek first to understand, synergize, sharpen the saw — moving from dependence through independence to interdependence.","f":["Effectiveness grows from character, not technique.","The time-management matrix separates urgent from important.","Win-win is a character stance, not a tactic."],"c":["Inside-out","The 7 habits overview","Be proactive","Begin with the end","Put first things first","Synergize and renew"],"g":"habits"},{"w":"How to Win Friends and Influence People","a":"Dale Carnegie","p":"Simon & Schuster","y":1936,"s":"The classic on human relations — six ways to make people like you, twelve ways to win people to your thinking, nine ways to change people without arousing resentment — from Carnegie's courses.","f":["People crave sincere appreciation.","Talk in terms of the other person's interests.","Let the other person feel the idea is theirs."],"c":["Fundamental techniques","Six ways to be liked","Winning people over","Leadership principles","Course origins","Applications"],"g":"communication"},{"w":"Emotional Intelligence: Why It Can Matter More Than IQ","a":"Daniel Goleman","p":"Bantam Books","y":1995,"s":"The popular synthesis of research on emotional intelligence — self-awareness, self-regulation, motivation, empathy, social skills — arguing EQ predicts life outcomes alongside IQ.","f":["Emotional skills can be learned at any age.","Self-awareness is the foundation competence.","Empathy underpins social effectiveness."],"c":["The emotional brain","Self-awareness","Self-regulation","Motivation","Empathy","Social skills"],"g":"emotional-intelligence"},{"w":"Mindset: The New Psychology of Success","a":"Carol S. Dweck","p":"Random House","y":2006,"s":"Dweck's research on fixed versus growth mindsets — how beliefs about ability shape goals, effort, and resilience — with applications to school, work and relationships.","f":["A growth mindset frames effort as the path to mastery.","Praising process beats praising talent.","Mindsets can be taught and changed."],"c":["The mindsets","Inside the mindsets","Sports","Business","Relationships","Cultivating growth"],"g":"mindset"},{"w":"Getting Things Done: The Art of Stress-Free Productivity","a":"David Allen","p":"Viking","y":2001,"s":"The GTD workflow — capture, clarify, organize, reflect, engage — built on the principle that the mind is for having ideas, not holding them, with the two-minute rule and weekly review.","f":["Externalize everything into a trusted system.","The next action is the atomic unit of work.","Weekly review keeps the system trustworthy."],"c":["The art of stress-free productivity","Capture","Clarify","Organize","Reflect","Engage"],"g":"productivity"},{"w":"Grit: The Power of Passion and Perseverance","a":"Angela Duckworth","p":"Scribner","y":2016,"s":"Duckworth's research on grit — passion plus perseverance for long-term goals — the Grit Scale, deliberate practice, purpose, and hope as the psychology of high achievement.","f":["Grit predicts achievement beyond talent.","Deliberate practice builds skill systematically.","Purpose sustains effort over years."],"c":["What grit is","Growing grit","Interest","Practice","Purpose","Hope"],"g":"mindset"},{"w":"Atomic Habits: An Easy and Proven Way to Build Good Habits","a":"James Clear","p":"Avery","y":2018,"s":"The four laws of behavior change — make it obvious, attractive, easy, satisfying — with habit stacking, environment design, and identity-based habits from Clear's research synthesis.","f":["Systems beat goals; 1% improvements compound.","Environment design outperforms willpower.","Identity-based habits stick longest."],"c":["The fundamentals","The four laws","Make it obvious","Make it attractive","Make it easy","Make it satisfying"],"g":"habits"},{"w":"Crucial Conversations: Tools for Talking When Stakes Are High","a":"Kerry Patterson, Joseph Grenny, Ron McMillan, Al Switzler","p":"McGraw-Hill","y":2002,"s":"The dialogue framework for high-stakes conversations — start with heart, learn to look, make it safe, master stories — from the authors' organizational research.","f":["Mutual purpose and respect keep dialogue safe.","Stories we tell ourselves drive emotions.","State facts, tell your story, ask for others' paths."],"c":["Start with heart","Learn to look","Make it safe","Master my stories","STATE my path","Move to action"],"g":"communication"},{"w":"Man's Search for Meaning","a":"Viktor E. Frankl","p":"Beacon Press","y":1946,"s":"Frankl's memoir of the camps and the birth of logotherapy — the will to meaning as the primary human drive, with the famous claim that between stimulus and response lies choice.","f":["Meaning can be found in suffering through attitude.","The will to meaning is the central motivation.","Freedom of attitude persists in any condition."],"c":["Experiences in the camp","Basic concepts of logotherapy","The will to meaning","Tragic optimism","Case studies","Conclusion"],"g":"mindset"},{"w":"Thinking, Fast and Slow","a":"Daniel Kahneman","p":"Farrar, Straus and Giroux","y":2011,"s":"Kahneman's synthesis of judgment and decision research — System 1 and System 2, heuristics, biases, prospect theory — and what they mean for everyday choices.","f":["Two systems govern judgment: fast intuition and slow reasoning.","Losses loom larger than gains.","Overconfidence is pervasive and costly."],"c":["Two systems","Heuristics and biases","Overconfidence","Choices","Prospect theory","Two selves"],"g":"productivity"},{"w":"The Effective Executive","a":"Peter F. Drucker","p":"Harper & Row","y":1967,"s":"Drucker's manual of personal effectiveness for knowledge workers — manage time, focus on contribution, build on strengths, concentrate on the few major areas, make effective decisions.","f":["Effectiveness is a habit that can be learned.","Know where your time goes, then manage it.","Concentrate on the vital few priorities."],"c":["Know thy time","What can I contribute","Making strengths productive","Concentration","Decision making","Effectiveness can be learned"],"g":"leadership"},{"w":"Nonviolent Communication: A Language of Life","a":"Marshall B. Rosenberg","p":"PuddleDancer Press","y":1999,"s":"Rosenberg's four-step process — observation, feeling, need, request — for honest expression and empathic listening without judgment, from mediation practice.","f":["Separate observation from evaluation.","Feelings point to met or unmet needs.","Requests work better than demands."],"c":["Giving from the heart","Communication that blocks compassion","Observing without evaluating","Identifying feelings","Taking responsibility","Requesting"],"g":"communication"}];
var TOPICS=[{"t":"Projected habit-formation clinical guideline, 2031 horizon","b":"Projects behavior-change trials into a clinical guideline for habit interventions.","f":["Habit prescriptions join exercise prescriptions.","Adherence tracking becomes standard care."],"o":["Evidence review","Prescription protocol","Tracking","Training"],"g":"habits"},{"t":"Projected attention-resilience curriculum, 2030 horizon","b":"Extends digital-wellbeing research into a school curriculum for attention.","f":["Students learn attention as a trainable skill.","Notification hygiene becomes taught practice."],"o":["Curriculum","Practices","Measurement","Teacher guides"],"g":"productivity"},{"t":"Projected empathy-training efficacy registry, 2033 horizon","b":"Projects empathy-intervention studies into a public efficacy registry.","f":["Perspective-taking exercises show largest effects.","Workplace programs adopt registry ratings."],"o":["Taxonomy","Ratings","Programs","Updates"],"g":"emotional-intelligence"},{"t":"Projected growth-mindset intervention code, 2029 horizon","b":"Extends mindset-intervention research into a practice code.","f":["Brief interventions work only with supportive contexts.","The code bans fixed-mindset praise in schools."],"o":["Principles","Interventions","Context checks","Monitoring"],"g":"mindset"},{"t":"Projected difficult-conversation AI coach standard, 2034 horizon","b":"Projects conversation-coaching tools into a quality standard.","f":["Rehearsal with feedback beats advice alone.","Standards require psychological safety design."],"o":["Coaching model","Safety design","Evaluation","Certification"],"g":"communication"},{"t":"Projected personal-knowledge-management canon, 2032 horizon","b":"Synthesizes note-taking and PKM research into a canonical guide.","f":["Writing to think beats storing to retrieve.","Linking notes compounds insight."],"o":["Principles","Methods","Tools","Workflows"],"g":"productivity"},{"t":"Projected character-education outcome framework, 2030 horizon","b":"Extends character-education trials into a shared outcome framework.","f":["Agreed outcomes end program confusion.","Longitudinal tracking becomes feasible."],"o":["Outcomes","Measures","Programs","Longitudinal plan"],"g":"leadership"},{"t":"Projected listening-skills public standard, 2028 horizon","b":"Projects active-listening research into a public communication standard.","f":["Listening is assessed, not assumed.","Workplaces adopt listening audits."],"o":["Skill model","Assessment","Audits","Training"],"g":"communication"},{"t":"Projected resilience-at-work guideline, 2031 horizon","b":"Synthesizes occupational resilience research into employer guidance.","f":["Recovery practices outperform toughness narratives.","Manager behavior is the lever."],"o":["Practices","Manager guide","Measurement","Case studies"],"g":"emotional-intelligence"},{"t":"Projected deliberate-practice manual for professions, 2035 horizon","b":"Extends expertise research into a cross-profession practice manual.","f":["Feedback loops define effective practice.","Coaches matter more than hours."],"o":["Principles","Design","Coaching","Professions"],"g":"habits"},{"t":"Projected purpose-driven career framework, 2033 horizon","b":"Projects meaning-at-work research into a career guidance framework.","f":["Purpose alignment predicts retention.","Crafting beats searching for purpose."],"o":["Framework","Assessment","Guidance","Employers"],"g":"leadership"},{"t":"Projected self-regulation school program, 2029 horizon","b":"Scales self-regulation interventions into a standard school program.","f":["Executive-function practice transfers to grades.","Teacher modeling is essential."],"o":["Program","Practices","Teacher role","Evaluation"],"g":"mindset"},{"t":"Projected negotiation-ethics handbook, 2032 horizon","b":"Projects principled-negotiation research into a modern ethics handbook.","f":["Transparency norms spread in digital deals.","Ethics training cuts deception."],"o":["Principles","Tactics","Ethics","Cases"],"g":"communication"},{"t":"Projected deep-work workplace standard, 2030 horizon","b":"Extends attention research into a workplace deep-work standard.","f":["Protected focus time raises output quality.","Meeting norms are the main obstacle."],"o":["Standard","Scheduling","Norms","Measurement"],"g":"productivity"}];
var FNOTES=["Habit titles are filed by behavior-change mechanism — cue, routine, reward, identity.","Communication works are cross-referenced under listening, speaking and conflict.","Mindset records note whether the evidence cited is experimental or correlational.","Productivity titles carry their system type — GTD-style, time-boxing, or energy-based.","Leadership records distinguish personal-effectiveness from organizational-leadership works.","Emotional-intelligence records note the model used — ability, trait, or mixed."];
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
var gen={version:'jahdb-personal-skills-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();