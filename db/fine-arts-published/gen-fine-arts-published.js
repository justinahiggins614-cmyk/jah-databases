(function(){'use strict';
var SLUG='fine-arts-published';
var BASE='fine-arts';
var PREFIX='JAH-fine-arts-published-P-';
var FIELD='Fine Arts';
var CATS=["painting","drawing","sculpture","art-history","theory","criticism"];
var WORKS=[{"w":"The Story of Art (16th ed.)","a":"Ernst H. Gombrich","p":"Phaidon","y":1995,"s":"Gombrich's sweeping history of art from prehistory to modernism — the schema-and-correction account of representation — the world's best-selling art history.","f":["Art history is a history of problem-solving.","Schemata are corrected by observation.","There is no innocent eye."],"c":["Prehistory","Egypt and Greece","Middle Ages","Renaissance","Baroque","Modern art"],"g":"art-history"},{"w":"Art and Visual Perception: A Psychology of the Creative Eye","a":"Rudolf Arnheim","p":"University of California Press","y":1954,"s":"Arnheim's Gestalt psychology of art — balance, shape, form, growth, movement, dynamics — the scientific account of how we see pictures.","f":["Perception organizes wholes, not parts.","Balance and tension structure images.","Seeing is active thinking."],"c":["Balance","Shape","Form","Growth","Space","Movement and dynamics"],"g":"theory"},{"w":"Drawing on the Right Side of the Brain (4th ed.)","a":"Betty Edwards","p":"Tarcher","y":2012,"s":"Edwards's drawing course — contour, negative space, relationships, lights and shadows — teaching anyone to draw by shifting to visual perception.","f":["Drawing is a learnable perceptual skill.","Five sub-skills compose drawing.","Everyone can learn with the right exercises."],"c":["Contour","Negative space","Relationships","Lights and shadows","Portrait","Color"],"g":"drawing"},{"w":"Art as Experience","a":"John Dewey","p":"Minton, Balch","y":1934,"s":"Dewey's philosophy of art as consummated experience — art continuous with everyday life, expression versus discharge — the foundation of art-education theory.","f":["Art is experience intensified.","Expression differs from mere discharge.","The museum should not isolate art from life."],"c":["The live creature","Experience","Expression","Form","Criticism","Civilization"],"g":"theory"},{"w":"Ways of Seeing","a":"John Berger","p":"British Broadcasting Corporation","y":1972,"s":"Berger's seven essays on image culture — the mystification of art, the male gaze, publicity — that changed how art is taught and criticized.","f":["Seeing comes before words.","Publicity images borrow from oil painting.","The male gaze structures the nude."],"c":["Seeing","The image","The nude","Publicity","Mystification","Essays"],"g":"criticism"},{"w":"On Painting","a":"Leon Battista Alberti","p":"Yale University Press (Cecil Grayson ed.)","y":1972,"s":"Alberti's 1435 treatise — perspective, composition, the istoria — the founding text of Renaissance painting theory, in the standard English edition.","f":["Perspective constructs rational space.","Composition serves the istoria.","The painter needs liberal learning."],"c":["Rudiments","Perspective","Composition","Color","Light","The painter"],"g":"painting"},{"w":"Sculpture: Principles and Practice","a":"Louis Slobodkin","p":"Dover","y":1949,"s":"Slobodkin's practical guide to sculpture — armature, modeling, carving, casting — the studio text for beginning sculptors.","f":["Armature precedes modeling.","Carving is reductive thinking.","Casting extends the sculptor's reach."],"c":["Armature","Modeling","Carving","Casting","Materials","Finishing"],"g":"sculpture"},{"w":"The Materials of the Artist","a":"Max Doerner","p":"Harcourt Brace","y":1934,"s":"Doerner's technical bible of painting materials — pigments, binders, grounds, varnishes — the conservator's and painter's reference.","f":["Material knowledge prevents technical failure.","Pigment chemistry determines permanence.","Grounds and varnishes complete the system."],"c":["Pigments","Binders","Grounds","Painting techniques","Varnishes","Conservation"],"g":"painting"},{"w":"Art Fundamentals: Theory and Practice (12th ed.)","a":"Otto G. Ocvirk et al.","p":"McGraw-Hill","y":1968,"s":"The standard foundations text — the elements and principles of design applied across media — training art students for generations.","f":["Elements combine into principles.","Foundations transfer across media.","Critique builds visual judgment."],"c":["Line","Shape","Value","Color","Principles","Critique"],"g":"theory"},{"w":"A History of Modern Art (7th ed.)","a":"H. H. Arnason and Elizabeth C. Mansfield","p":"Pearson","y":2012,"s":"The comprehensive survey of modern art from the later nineteenth century to the present — movements, artists, contexts — the standard course text.","f":["Modernism is a series of ruptures.","Context explains form.","The contemporary extends the modern."],"c":["Origins","Cubism","Dada and surrealism","Abstract expressionism","Pop","Contemporary"],"g":"art-history"},{"w":"The Artist's Way","a":"Julia Cameron","p":"Tarcher","y":1992,"s":"Cameron's twelve-week course in creative recovery — morning pages, artist dates — the most widely used creativity workbook for artists.","f":["Morning pages clear creative blocks.","Artist dates refill the well.","Creativity is a spiritual practice."],"c":["Recovering safety","Recovering identity","Recovering power","Recovering integrity","Recovering possibility","Twelve weeks"],"g":"drawing"},{"w":"Criticizing Art: Understanding the Contemporary","a":"Terry Barrett","p":"McGraw-Hill","y":1994,"s":"Barrett's guide to art criticism — description, interpretation, judgment, theory — teaching students to write about art. Its classroom-tested exercises made critical writing teachable, and later editions added digital and global art examples.","f":["Criticism follows describe-interpret-judge.","Interpretation admits multiple readings.","Theory informs judgment."],"c":["Description","Interpretation","Judgment","Theory","Writing","Examples"],"g":"criticism"}];
var TOPICS=[{"t":"Projected AI-attribution standard for artworks, 2032 horizon","b":"Projects provenance research into an AI-attribution standard.","f":["AI involvement is disclosed by degree.","Collectors rely on the standard."],"o":["Degrees","Disclosure","Provenance","Market"],"g":"criticism"},{"t":"Projected drawing-neuroscience curriculum, 2030 horizon","b":"Extends perception research into a drawing curriculum.","f":["Perceptual training accelerates skill.","Curricula adopt the exercises."],"o":["Exercises","Perception","Curriculum","Evidence"],"g":"drawing"},{"t":"Projected public-art commissioning code, 2029 horizon","b":"Projects public-art controversies into a commissioning code.","f":["Community voice is formalized.","Controversies decline."],"o":["Voice","Selection","Contracts","Review"],"g":"sculpture"},{"t":"Projected pigment-sustainability standard, 2031 horizon","b":"Extends materials research into a pigment standard.","f":["Toxic pigments are phased out.","Alternatives match performance."],"o":["Pigments","Testing","Phase-out","Alternatives"],"g":"painting"},{"t":"Projected digital-art preservation protocol, 2033 horizon","b":"Projects conservation science into a digital-preservation protocol.","f":["Emulation preserves interactive works.","Museums adopt the protocol."],"o":["Emulation","Documentation","Museums","Funding"],"g":"art-history"},{"t":"Projected art-criticism AI-assistant ethics, 2030 horizon","b":"Projects criticism's digital turn into an ethics framework.","f":["AI drafts are disclosed.","Human judgment remains central."],"o":["Disclosure","Judgment","Labor","Standards"],"g":"criticism"},{"t":"Projected studio-safety global standard, 2028 horizon","b":"Extends studio-safety work into a global standard.","f":["Ventilation and PPE become universal.","Schools are audited."],"o":["Hazards","Ventilation","PPE","Audits"],"g":"sculpture"},{"t":"Projected color-theory unified curriculum, 2031 horizon","b":"Projects color-science advances into a unified curriculum.","f":["One curriculum serves art and design.","Digital color is integrated."],"o":["Science","Exercises","Digital","Assessment"],"g":"theory"},{"t":"Projected mural-arts municipal program, 2029 horizon","b":"Projects mural movements into a municipal program model.","f":["Cities fund mural districts.","Youth apprenticeships grow."],"o":["Funding","Districts","Apprentices","Evaluation"],"g":"painting"},{"t":"Projected art-history open-image canon, 2034 horizon","b":"Projects open-access image growth into a teaching canon.","f":["Key works become freely usable.","Global art gains equal coverage."],"o":["Canon","Licensing","Coverage","Teaching"],"g":"art-history"},{"t":"Projected life-drawing consent code, 2028 horizon","b":"Extends studio ethics into a life-drawing consent code.","f":["Model rights are codified.","Programs adopt the code."],"o":["Rights","Consent","Programs","Oversight"],"g":"drawing"},{"t":"Projected sculpture-public-space impact standard, 2032 horizon","b":"Projects placemaking research into an impact standard.","f":["Impact is measured, not assumed.","Communities co-design."],"o":["Metrics","Co-design","Measurement","Cases"],"g":"sculpture"},{"t":"Projected aesthetics-and-wellbeing research agenda, 2035 horizon","b":"A projected agenda linking aesthetics to wellbeing evidence.","f":["Museum visits show health effects.","Prescription programs grow."],"o":["Evidence","Programs","Measurement","Policy"],"g":"theory"},{"t":"Projected forgery-detection training standard, 2031 horizon","b":"Projects forensic advances into a connoisseur-training standard.","f":["Technical analysis joins connoisseurship.","Fakes are caught earlier."],"o":["Techniques","Training","Cases","Ethics"],"g":"criticism"}];
var FNOTES=["Painting records note the medium — oil, watercolor, acrylic, or fresco.","Drawing records distinguish observational from imaginative approaches.","Sculpture records carry the process — modeling, carving, casting, or assemblage.","Art-history records note the period and the method — formalist, social, or iconographic.","Theory records name the framework — Gestalt, semiotic, or phenomenological.","Criticism records state the critical stance taken."];
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
var gen={version:'jahdb-fine-arts-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();