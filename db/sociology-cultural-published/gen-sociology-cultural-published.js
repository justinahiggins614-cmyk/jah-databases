(function(){'use strict';
var SLUG='sociology-cultural-published';
var BASE='sociology-cultural';
var PREFIX='JAH-sociology-cultural-published-P-';
var FIELD='Sociology and Cultural Studies';
var CATS=["theory","research-methods","culture","inequality","institutions","social-change"];
var WORKS=[{"w":"The Sociological Imagination","a":"C. Wright Mills","p":"Oxford University Press","y":1959,"s":"Mills's call for the quality of mind connecting private troubles with public issues — biography and history grasped together.","f":["The sociological imagination joins biography to history.","Private troubles are rooted in public issues.","Social science must address the great problems of the age."],"c":["The promise","Grand theory","Abstracted empiricism","Types of practicality","The bureaucratic ethos","The politics of truth"],"g":"theory"},{"w":"The Presentation of Self in Everyday Life","a":"Erving Goffman","p":"Doubleday","y":1959,"s":"Goffman's dramaturgical model of social life as performance — front stage and back stage, teams, and the arts of impression management.","f":["People manage impressions in front-stage performances.","Back-stage regions let performers drop the act.","Teams sustain a shared definition of the situation."],"c":["Performances","Teams","Regions","Discrepant roles","Out-of-character communication","Impression management"],"g":"theory"},{"w":"Suicide: A Study in Sociology","a":"Émile Durkheim","p":"Free Press","y":1951,"s":"Durkheim's founding study of social facts: suicide rates vary with degrees of social integration and regulation — egoistic, altruistic, and anomic types. (Standard English edition; original 1897.)","f":["Suicide rates are social facts with social causes.","Egoistic suicide rises where integration is weak.","Anomic suicide follows broken regulation."],"c":["Extra-social factors","Egoistic suicide","Altruistic suicide","Anomic suicide","Suicide as social fact","Practical consequences"],"g":"research-methods"},{"w":"The Protestant Ethic and the Spirit of Capitalism","a":"Max Weber","p":"Charles Scribner's Sons","y":1930,"s":"Weber's thesis linking Calvinist asceticism to modern capitalist rationality — and the iron cage. (Standard English edition; original 1905.)","f":["The Calvinist calling sanctified disciplined labor.","Rational asceticism shaped the capitalist spirit.","Modernity tends toward an iron cage."],"c":["Religious affiliation","The capitalist spirit","Luther's calling","Worldly asceticism","Asceticism and capitalism","Conclusion"],"g":"theory"},{"w":"Distinction: A Social Critique of the Judgement of Taste","a":"Pierre Bourdieu","p":"Harvard University Press","y":1984,"s":"Bourdieu's survey-based argument that taste expresses class position — cultural capital, habitus, and the social space of life-styles.","f":["Taste marks class position.","Cultural capital converts to advantage.","The aesthetic disposition marks the dominant class."],"c":["The aristocracy of culture","Social space","Habitus and life-styles","Field dynamics","Distinction and the dominated","Conclusion"],"g":"inequality"},{"w":"The Interpretation of Cultures","a":"Clifford Geertz","p":"Basic Books","y":1973,"s":"Geertz's interpretive anthropology — culture as webs of significance, thick description of meaning, modeled in the cockfight essay.","f":["Culture is a web of significance humans spin.","Thick description interprets meaning.","The cockfight essay models symbolic analysis."],"c":["Thick description","The culture concept","Cultural growth","Deep play","Person and time in Bali","The cerebral savage"],"g":"culture"},{"w":"Culture and Society, 1780-1950","a":"Raymond Williams","p":"Chatto & Windus","y":1958,"s":"Williams's history of the idea of culture from the Industrial Revolution to the mid-twentieth century — a founding text of British cultural studies.","f":["The idea of culture emerged against industrialism.","Culture names a way of life and artistic works.","Literary critics became social critics."],"c":["Contrasts","The romantic artist","Mill on Bentham and Coleridge","Thomas Carlyle","Maurice and Kingsley","Conclusion"],"g":"culture"},{"w":"The Social Construction of Reality","a":"Peter L. Berger and Thomas Luckmann","p":"Doubleday","y":1966,"s":"The treatise arguing that reality is socially constructed — habitualization, institutionalization, and legitimation building the symbolic universe.","f":["Everyday knowledge is socially constructed.","Institutions grow from habitualized action.","Legitimation maintains the symbolic universe."],"c":["Everyday reality","Institutionalization","Legitimation","Internalization","Internalization and structure","Conclusion"],"g":"theory"},{"w":"Stigma: Notes on the Management of Spoiled Identity","a":"Erving Goffman","p":"Prentice-Hall","y":1963,"s":"Goffman's study of how stigmatized persons manage information about discrediting attributes — passing, covering, and group alignment.","f":["Stigma discredits in interaction.","The discredited manage visibility; the discreditable, information.","Passing and covering manage spoiled identity."],"c":["Stigma and identity","Information control","Group alignment","The self and its other","Deviance","Conclusion"],"g":"inequality"},{"w":"Encoding and Decoding in the Television Discourse","a":"Stuart Hall","p":"Centre for Contemporary Cultural Studies, University of Birmingham","y":1973,"s":"Hall's landmark paper proposing that audiences actively decode media texts — producing dominant, negotiated, or oppositional readings.","f":["Encoding and decoding are distinct moments.","Audiences produce dominant, negotiated, or oppositional readings.","Meaning is struggled over, not transmitted."],"c":["The traditional model","Encoding","Decoding","Three reading positions","Misunderstandings","Conclusion"],"g":"culture"},{"w":"Bowling Alone","a":"Robert D. Putnam","p":"Simon & Schuster","y":2000,"s":"Putnam's account of the decline of American social capital — civic associations, trust, and connectedness — and its consequences for democracy and well-being.","f":["Social capital declined after the 1960s.","TV and generational turnover drive the decline.","Disengagement harms health, education, democracy."],"c":["Social capital","Political participation","Civic participation","Religious participation","Workplace connections","Conclusion"],"g":"institutions"},{"w":"The McDonaldization of Society","a":"George Ritzer","p":"Pine Forge Press","y":1993,"s":"Ritzer's application of Weber's rationalization thesis to fast food — efficiency, calculability, predictability, control — and the irrationality of rationality.","f":["Rationalization spreads via efficiency, calculability, predictability, control.","Fast-food principles colonize other sectors.","Irrationality is the cost of rationality."],"c":["Introducing McDonaldization","Past, present, future","Efficiency","Calculability","Predictability","The irrationality of rationality"],"g":"social-change"}];
var TOPICS=[{"t":"Projected global care-work valuation study, 2034 horizon","b":"Extrapolates from time-use surveys and feminist economics to a standardized valuation of unpaid care labor.","f":["Unpaid care is measured in national accounts.","Care deficits predict inequality more strongly than income gaps."],"o":["Measurement design","Valuation methods","Policy uses","Country pilots"],"g":"inequality"},{"t":"Projected algorithmic-culture ethnography, 2032 horizon","b":"Projects current platform ethnography onto fully algorithmic cultural production.","f":["Recommendation systems become primary culture-makers.","Ethnographers study audiences through their feeds."],"o":["Field methods","Data access","Ethics","Findings"],"g":"culture"},{"t":"Projected post-work social integration index, 2038 horizon","b":"Extends Durkheimian integration theory to societies with mass technological unemployment.","f":["Integration is measured without employment as the anchor.","New rituals replace the workplace."],"o":["Theory","Indicators","Validation","Policy links"],"g":"social-change"},{"t":"Projected climate-migration sociology, 2031 horizon","b":"Builds on displacement research to a standing sociology of climate-driven movement.","f":["Climate displacement reshapes urban hierarchies.","Host-community integration follows predictable stages."],"o":["Migration flows","Urban impact","Integration stages","Governance"],"g":"institutions"},{"t":"Projected digital-trace research ethics code, 2030 horizon","b":"Extends existing human-subjects frameworks to large-scale digital trace data.","f":["Consent models adapt to ambient data collection.","An ethics code governs trace-data sociology."],"o":["Consent models","Data minimization","Review boards","Enforcement"],"g":"research-methods"},{"t":"Projected status-economy theory, 2035 horizon","b":"Projects Bourdieu's capital theory onto platform-mediated status markets.","f":["Status becomes directly tradable online.","New hierarchies mix economic and cultural capital."],"o":["Capital forms","Platforms","Measurement","Stratification"],"g":"inequality"},{"t":"Projected institutional-trust longitudinal study, 2033 horizon","b":"Extends social-capital surveys into a continuous global trust panel.","f":["Trust is tracked in real time across institutions.","Trust shocks are detected within weeks."],"o":["Panel design","Indicators","Shock detection","Reporting"],"g":"institutions"},{"t":"Projected ritual-in-digital-life theory, 2036 horizon","b":"Projects interaction-ritual theory onto fully mediated social life.","f":["Digital rituals generate real solidarity.","Ritual failure predicts community collapse."],"o":["Ritual forms","Solidarity measures","Failure modes","Design lessons"],"g":"theory"},{"t":"Projected comparative de-urbanization study, 2029 horizon","b":"Builds on remote-work migration data to a comparative sociology of de-urbanization.","f":["Secondary cities gain selectively.","De-urbanization follows infrastructure, not preference alone."],"o":["Migration data","City typology","Infrastructure","Policy"],"g":"social-change"},{"t":"Projected synthetic-population research methods, 2037 horizon","b":"Extends simulation methods to validated synthetic populations for survey pre-testing.","f":["Synthetic populations pre-test surveys at scale.","Validation protocols make results publishable."],"o":["Synthesis methods","Validation","Pre-testing","Ethics"],"g":"research-methods"},{"t":"Projected meaning-making in AI-mediated culture, 2034 horizon","b":"Projects interpretive methods onto cultures co-authored with generative systems.","f":["Thick description adapts to machine-generated symbols.","Authorship ambiguity reshapes interpretation."],"o":["Methods","Symbol analysis","Authorship","Case studies"],"g":"culture"},{"t":"Projected grand-theory synthesis volume, 2040 horizon","b":"Projects current theory fragmentation toward a new synthetic framework.","f":["Micro and macro levels reconnect formally.","A shared framework ends the theory wars."],"o":["Framework","Formalization","Evidence","Reception"],"g":"theory"}];
var FNOTES=["Theory records are filed by school — classical, interpretive, critical, or structural — in the holdings line. Cross-references link each record to its nearest neighboring schools.","Method records distinguish quantitative, qualitative, and historical-comparative approaches in the notes. Mixed-method designs are flagged where the work combines approaches.","Culture records name the medium or practice studied — ritual, media, taste, or everyday life. Comparative cases are cross-filed under each medium named.","Inequality records note the stratification dimension — class, status, gender, or race — in the category field. Intersectional analyses carry all applicable dimensions.","Institutions records name the institution studied and the period covered. Longitudinal studies note each wave in the holdings line.","Social-change records carry their transformation thesis in the summary line. The direction and pace of change are stated explicitly."];
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
  var chapters=work.c.slice(0,5).map(function(x,i){return 'Part '+(i+1)+' \u2014 '+x+';';}).join(' ');
  var full='Published work: '+work.w+'. '+work.s+
    '\n\nKEY FINDINGS. '+findings+
    '\n\nCONTENTS. '+chapters+
    '\n\nARCHIVIST\u2019S NOTES. '+n1+
    '\n\nANALYSIS FOCUS. '+focus+
    '\n\nSIGNIFICANCE. '+signif+
    '\n\nHOLDINGS. Filed as '+PREFIX+pad(seed)+'.';
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
  var outline=topic.o.slice(0,5).map(function(x,i){return 'Part '+(i+1)+' \u2014 '+x+';';}).join(' ');
  var full='PROJECTION NOTICE. This Level 2 entry is a projection-based synthesis, not a record of a real published work. '+
    'It extrapolates from this archive\u2019s Level 1 holdings in '+FIELD+' to sketch a plausible future publication. '+
    'Method: trends observed across the Level 1 record set are extended along their trajectories, and the resulting outline is checked for internal consistency before filing.'+
    '\n\nBASIS. '+topic.b+
    '\n\nPROJECTED FINDINGS. '+findings+
    '\n\nPROPOSED OUTLINE. '+outline+
    '\n\nARCHIVIST\u2019S NOTES. '+n1+' '+n2+' Analysis focus: '+focus+
    '\n\nHOLDINGS. Filed as '+PREFIX+pad(seed)+'. Projection only.';
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
['word-count',function(r){return r.full_content.split(/\s+/).length>=120?null:'too few words';}],
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
var gen={version:'jahdb-sociology-cultural-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();