(function(){'use strict';
var SLUG='audiovisual-media-published';
var BASE='audiovisual-media';
var PREFIX='JAH-audiovisual-media-published-P-';
var FIELD='Audio-Visual Techniques and Media Production';
var CATS=["film","television","audio","editing","production","media-literacy"];
var WORKS=[{"w":"Film Art: An Introduction","a":"David Bordwell and Kristin Thompson","p":"McGraw-Hill","y":1979,"s":"The standard film-studies and production text — form, style, narration, mise-en-scène, cinematography, editing, sound — teaching how films are made and mean.","f":["Form and style explain how films work.","Mise-en-scène, cinematography, editing and sound are the four domains.","Narrative form organizes viewer expectations."],"c":["Film form","Narrative","Mise-en-scène","Cinematography","Editing","Sound"],"g":"film"},{"w":"Shot by Shot: Visualizing from Concept to Screen","a":"Steven D. Katz","p":"Michael Wiese Productions","y":1991,"s":"The storyboard and visualization bible — shot design, storyboarding, staging, camera movement — used to train directors and cinematographers.","f":["Visualization precedes photography.","Storyboards are a thinking tool, not just pictures.","Staging and camera are designed together."],"c":["Visualization","Storyboards","Staging","Camera","Movement","Case studies"],"g":"film"},{"w":"In the Blink of an Eye: A Perspective on Film Editing","a":"Walter Murch","p":"Silman-James Press","y":1995,"s":"Murch's meditation on editing — the rule of six, emotion over technique, the blink as a cut point — the most influential book on film editing.","f":["Emotion is the top criterion for a cut.","The blink marks a natural edit point.","Digital editing changed the craft's rhythm."],"c":["The rule of six","Emotion","The blink","Digital editing","Sound","Philosophy"],"g":"editing"},{"w":"Television Production (14th ed.)","a":"Gerald Millerson","p":"Focal Press","y":1961,"s":"The long-running standard text on television production — studios, cameras, lighting, sound, directing multi-camera — training generations of TV crew.","f":["Multi-camera production is a team discipline.","Lighting defines the televisual image.","Directing is decision-making under time pressure."],"c":["The studio","Cameras","Lighting","Sound","Directing","Production roles"],"g":"television"},{"w":"The Filmmaker's Handbook (5th ed.)","a":"Steven Ascher and Edward Pincus","p":"Plume","y":2017,"s":"The comprehensive technical handbook — cameras, lenses, exposure, lighting, sound recording, editing, distribution — the on-set reference for independent filmmakers.","f":["Exposure and focus are the technical foundations.","Sound quality determines perceived quality.","Distribution knowledge completes production."],"c":["Cameras","Lenses","Exposure","Lighting","Sound","Editing and distribution"],"g":"production"},{"w":"Sight Sound Motion: Applied Media Aesthetics (7th ed.)","a":"Herbert Zettl","p":"Cengage","y":2013,"s":"Zettl's applied media aesthetics — light, color, space, time, motion, sound — how aesthetic choices shape meaning in television and film.","f":["Aesthetic elements carry meaning systematically.","Light and color set psychological context.","Sound structures time and attention."],"c":["Light","Color","Space","Time and motion","Sound","Aesthetic synthesis"],"g":"television"},{"w":"On Film Editing","a":"Edward Dmytryk","p":"Focal Press","y":1984,"s":"Dmytryk's director-editor guide to cutting — rules of thumb, matching action, pacing — from a classical Hollywood practitioner.","f":["Never make a cut without a positive reason.","Match action across cuts.","Pacing serves story, not showmanship."],"c":["The cut","Matching","Pacing","Transitions","Sound","The editor's role"],"g":"editing"},{"w":"The Technique of Film and Television Editing","a":"Karel Reisz and Gavin Millar","p":"Focal Press","y":1953,"s":"The classic British manual of editing craft — principles of the cut, montage, documentary editing — foundational for editing education.","f":["Editing principles transfer across genres.","Montage builds meaning from collision.","Documentary editing finds structure in reality."],"c":["Principles","Montage","Continuity","Documentary","Sound","Practice"],"g":"editing"},{"w":"Producing with Passion","a":"Dorothy Fadiman","p":"Michael Wiese Productions","y":2008,"s":"A representative producing guide — development, financing, crew, shooting, post — covering the producer's full responsibility chain.","f":["Development determines production success.","The producer owns the schedule and budget.","Passion sustains long productions."],"c":["Development","Financing","Crew","Shooting","Post-production","Distribution"],"g":"production"},{"w":"Sound for Film and Television (3rd ed.)","a":"Tomlinson Holman","p":"Focal Press","y":2010,"s":"Holman's technical guide to production and post sound — recording, dialogue, effects, mixing, surround — the audio engineer's reference.","f":["Dialogue clarity is the first duty of sound.","Production sound beats ADR.","Mixing balances story and spectacle."],"c":["Recording","Dialogue","Effects","Mixing","Surround","Delivery"],"g":"audio"},{"w":"Media Literacy: A Reader","a":"Sue Dwyer","p":"Peter Lang","y":2007,"s":"A representative media-literacy reader — analyzing messages, production contexts, audiences — used to train media educators.","f":["All media messages are constructed.","Audiences negotiate meaning.","Production context shapes content."],"c":["Construction","Contexts","Audiences","Analysis methods","Production","Teaching"],"g":"media-literacy"},{"w":"Understanding Media Production (classroom edition)","a":"Representative media-production textbook authors","p":"Routledge","y":2014,"s":"A representative classroom text on media production — pre-production, production, post-production workflows for student crews.","f":["Pre-production prevents production failure.","Workflows organize student crews.","Post-production completes the story."],"c":["Pre-production","Production","Post-production","Roles","Safety","Showcase"],"g":"production"}];
var TOPICS=[{"t":"Projected virtual-production training standard, 2031 horizon","b":"Extends LED-volume production growth into a crew training standard.","f":["Virtual production becomes a core crew skill.","Real-time engines join the curriculum."],"o":["Standard","Workflows","Engines","Crews"],"g":"production"},{"t":"Projected AI-assisted editing ethics code, 2030 horizon","b":"Projects generative editing tools into an ethics code.","f":["Disclosure of AI edits becomes mandatory.","Editor authorship is protected."],"o":["Disclosure","Authorship","Labor","Enforcement"],"g":"editing"},{"t":"Projected spatial-audio production standard, 2032 horizon","b":"Extends immersive audio growth into a production standard.","f":["Object-based audio becomes default.","Monitoring standards unify."],"o":["Formats","Monitoring","Workflows","Delivery"],"g":"audio"},{"t":"Projected media-literacy graduation requirement, 2029 horizon","b":"Projects media-literacy research into a graduation requirement.","f":["Every graduate demonstrates media literacy.","Misinformation resilience improves."],"o":["Competencies","Assessment","Curriculum","Teacher prep"],"g":"media-literacy"},{"t":"Projected documentary-consent best-practice code, 2030 horizon","b":"Extends documentary ethics into a consent code.","f":["Informed consent becomes documented standard.","Vulnerable subjects gain protections."],"o":["Consent","Vulnerability","Documentation","Oversight"],"g":"film"},{"t":"Projected multi-camera directing certification, 2031 horizon","b":"Projects live-production growth into a directing certification.","f":["Certified directors meet safety and quality bars.","Live events adopt the certification."],"o":["Competencies","Assessment","Safety","Adoption"],"g":"television"},{"t":"Projected color-pipeline open standard, 2028 horizon","b":"Extends color-management work into an open pipeline standard.","f":["Consistent color from set to screen.","Open tools implement the standard."],"o":["Pipeline","Calibration","Tools","Adoption"],"g":"production"},{"t":"Projected podcast-production curriculum, 2029 horizon","b":"Projects podcast growth into a standard production curriculum.","f":["Audio storytelling enters media courses.","Low-cost kits suffice."],"o":["Curriculum","Storytelling","Kits","Distribution"],"g":"audio"},{"t":"Projected deepfake-detection literacy module, 2030 horizon","b":"Projects synthetic-media research into a literacy module.","f":["Students learn detection techniques.","Skepticism is taught as skill."],"o":["Techniques","Curriculum","Assessment","Updates"],"g":"media-literacy"},{"t":"Projected short-form directing craft guide, 2032 horizon","b":"Projects short-form video growth into a craft guide.","f":["Vertical grammar is codified.","Craft standards rise."],"o":["Grammar","Pacing","Sound","Cases"],"g":"film"},{"t":"Projected archive-footage licensing commons, 2033 horizon","b":"Projects open-archive growth into a licensing commons.","f":["Historical footage becomes affordable.","Attribution is automated."],"o":["Commons","Licensing","Attribution","Funding"],"g":"production"},{"t":"Projected accessibility-captioning mandate, 2028 horizon","b":"Extends accessibility law into a captioning mandate.","f":["All public video is captioned.","Quality standards are enforced."],"o":["Mandate","Quality","Enforcement","Tools"],"g":"television"},{"t":"Projected film-preservation training program, 2034 horizon","b":"Projects archive-preservation needs into a training program.","f":["New archivists learn photochemical and digital.","Endangered collections are prioritized."],"o":["Curriculum","Techniques","Priorities","Funding"],"g":"film"},{"t":"Projected remote-production safety standard, 2030 horizon","b":"Extends remote workflows into a safety standard.","f":["Distributed crews meet safety bars.","Protocols cover home studios."],"o":["Protocols","Home studios","Insurance","Compliance"],"g":"television"}];
var FNOTES=["Film records note the craft area — direction, cinematography, or theory.","Television records distinguish studio from field production.","Audio records carry the stage — production, post, or broadcast.","Editing records note the tradition — continuity, montage, or digital.","Production records state the budget tier the guidance targets.","Media-literacy records note the audience level — school, higher, or public."];
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
var gen={version:'jahdb-audiovisual-media-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();