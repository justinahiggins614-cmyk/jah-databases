(function(){'use strict';
var SLUG='design-fields-published';
var BASE='design-fields';
var PREFIX='JAH-design-fields-published-P-';
var FIELD='Fashion, Interior and Industrial Design';
var CATS=["fashion","interior","industrial","graphic","theory","sustainability"];
var WORKS=[{"w":"The Design of Everyday Things (revised ed.)","a":"Don Norman","p":"Basic Books","y":2013,"s":"Norman's classic on human-centered design — affordances, signifiers, mapping, feedback, the gulfs of execution and evaluation — the foundation text of design education.","f":["Good design makes the right action visible.","Affordances and signifiers guide use.","Human error usually signals bad design."],"c":["The psychopathology","Psychology of action","Knowledge","Constraints","Human error","Design thinking"],"g":"industrial"},{"w":"Design for the Real World: Human Ecology and Social Change","a":"Victor Papanek","p":"Pantheon Books","y":1971,"s":"Papanek's polemic for socially responsible design — design for need not greed, for the developing world, for disability — the conscience of design education.","f":["Design must serve real human needs.","Designers bear social responsibility.","Design for disability benefits everyone."],"c":["What designers do","Function","Responsibility","Developing world","Disability","The future"],"g":"theory"},{"w":"Patternmaking for Fashion Design (5th ed.)","a":"Helen Joseph Armstrong","p":"Pearson","y":2009,"s":"The standard patternmaking text — dart manipulation, slash and spread, draping, sleeves, collars — training generations of fashion designers.","f":["Dart manipulation is the grammar of patternmaking.","Slash-and-spread creates fullness systematically.","Draping and flat pattern are complementary."],"c":["Darts","Manipulation","Slash and spread","Draping","Sleeves","Collars and details"],"g":"fashion"},{"w":"Interior Design Illustrated (4th ed.)","a":"Francis D. K. Ching and Corky Binggeli","p":"Wiley","y":2020,"s":"Ching's visual introduction to interior design — space, form, light, materials, furnishings — the studio reference for interior-design students.","f":["Space is shaped by form and enclosure.","Light defines how interiors are perceived.","Materials carry tactile and visual meaning."],"c":["Space","Form","Light","Materials","Furnishings","Design process"],"g":"interior"},{"w":"Less, but Better","a":"Dieter Rams","p":"Gestalten","y":2014,"s":"Rams's ten principles of good design — innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting, thorough, environmental, minimal — from the Braun design chief.","f":["Good design is as little design as possible.","Honesty in design outlasts fashion.","The ten principles guide decisions."],"c":["The principles","Braun work","Products","Interiors","Philosophy","Legacy"],"g":"industrial"},{"w":"The Art of Color","a":"Johannes Itten","p":"Reinhold","y":1961,"s":"Itten's Bauhaus color theory — the color wheel, seven contrasts, subjective timbres — the standard color text for design students.","f":["Seven color contrasts structure all color work.","Subjective color timbres reveal personality.","Color harmony follows learnable rules."],"c":["The color wheel","Seven contrasts","Subjective timbres","Harmony","Form and color","Teaching color"],"g":"theory"},{"w":"Thinking with Type (2nd ed.)","a":"Ellen Lupton","p":"Princeton Architectural Press","y":2010,"s":"Lupton's guide to typography — letterforms, text hierarchy, grids — the graphic-design student's typographic reference.","f":["Typography is what language looks like.","Hierarchy guides the reader's eye.","Grids organize without constraining."],"c":["Letter","Text","Grid","Hierarchy","Classifications","Practice"],"g":"graphic"},{"w":"Fashion Design Course: Principles, Practice and Techniques","a":"Steven Faerm","p":"Barron's","y":2010,"s":"A representative fashion-design course text — research, silhouette, textiles, construction, portfolio — structuring studio training.","f":["Research grounds every collection.","Silhouette is the designer's signature.","Portfolio tells the design story."],"c":["Research","Silhouette","Textiles","Construction","Collection","Portfolio"],"g":"fashion"},{"w":"Human Dimension and Interior Space","a":"Julius Panero and Martin Zelnik","p":"Whitney Library of Design","y":1979,"s":"The anthropometric reference for interior designers — body measurements, clearances, the design of kitchens, baths, offices — the dimensional bible.","f":["Design dimensions derive from human bodies.","Clearances determine usability.","Standards prevent costly errors."],"c":["Anthropometrics","Clearances","Kitchens","Baths","Offices","Seating"],"g":"interior"},{"w":"Emotional Design: Why We Love (or Hate) Everyday Things","a":"Don Norman","p":"Basic Books","y":2004,"s":"Norman's three levels of design — visceral, behavioral, reflective — arguing attractive things work better and emotion is central to design.","f":["Design works at visceral, behavioral and reflective levels.","Attractive things work better.","Emotion and cognition are inseparable."],"c":["Visceral","Behavioral","Reflective","Fun","People","The future"],"g":"industrial"},{"w":"Cradle to Cradle: Remaking the Way We Make Things","a":"William McDonough and Michael Braungart","p":"North Point Press","y":2002,"s":"The manifesto for regenerative design — waste equals food, technical and biological nutrients — reshaping sustainable-design education.","f":["Waste should equal food.","Design for disassembly and cycling.","Eco-effectiveness beats eco-efficiency."],"c":["A question of design","Why being less bad fails","Eco-effectiveness","Technical nutrients","Biological nutrients","Implementation"],"g":"sustainability"},{"w":"Universal Principles of Design (revised ed.)","a":"William Lidwell, Kritina Holden, Jill Butler","p":"Rockport","y":2010,"s":"The cross-disciplinary compendium of 125 design principles — from affordance to wayfinding — the quick-reference for design students.","f":["Design principles transfer across disciplines.","Each principle carries evidence and examples.","The compendium supports critique."],"c":["Affordance","Hierarchy","Mapping","Prototyping","Wayfinding","125 principles"],"g":"theory"}];
var TOPICS=[{"t":"Projected circular-fashion design standard, 2031 horizon","b":"Extends circular-economy pilots into a fashion design standard.","f":["Design for disassembly becomes normal.","Take-back schemes fund the transition."],"o":["Standard","Materials","Disassembly","Business models"],"g":"sustainability"},{"t":"Projected AI-assisted patternmaking code, 2030 horizon","b":"Projects grading automation into a patternmaking practice code.","f":["AI grading cuts sampling waste.","Designer authorship is preserved."],"o":["Automation","Authorship","Waste","Training"],"g":"fashion"},{"t":"Projected healthy-interiors certification, 2029 horizon","b":"Extends wellbeing research into an interiors certification.","f":["Air, light and acoustics are certified.","Certified spaces command premiums."],"o":["Criteria","Measurement","Certification","Market"],"g":"interior"},{"t":"Projected inclusive-design legal standard, 2032 horizon","b":"Projects accessibility law into a product design standard.","f":["Exclusion becomes a design defect.","Enforcement follows the standard."],"o":["Standard","Testing","Enforcement","Cases"],"g":"industrial"},{"t":"Projected design-ethics curriculum requirement, 2030 horizon","b":"Extends design-ethics teaching into an accreditation requirement.","f":["Every program teaches design ethics.","Dark patterns are named and banned."],"o":["Curriculum","Dark patterns","Accreditation","Cases"],"g":"theory"},{"t":"Projected type-legibility public standard, 2028 horizon","b":"Projects legibility research into a public typography standard.","f":["Public signage meets legibility bars.","Digital interfaces follow."],"o":["Research","Bars","Signage","Digital"],"g":"graphic"},{"t":"Projected textile-recycling design guide, 2033 horizon","b":"Extends fiber-recycling research into a designer guide.","f":["Mono-materials dominate new collections.","Recycling rates are published."],"o":["Fibers","Design rules","Rates","Labels"],"g":"sustainability"},{"t":"Projected parametric-interior practice code, 2031 horizon","b":"Projects parametric tools into an interior-practice code.","f":["Generative layouts become standard service.","Human judgment gates the output."],"o":["Tools","Workflows","Judgment","Liability"],"g":"interior"},{"t":"Projected fashion-sizing inclusivity standard, 2029 horizon","b":"Extends body-diversity research into a sizing standard.","f":["Extended ranges become the norm.","Fit data is open."],"o":["Ranges","Fit data","Labels","Enforcement"],"g":"fashion"},{"t":"Projected repairable-electronics design mandate, 2030 horizon","b":"Projects right-to-repair wins into a design mandate.","f":["Repairability scores appear at sale.","Modular design returns."],"o":["Scores","Modularity","Parts","Enforcement"],"g":"industrial"},{"t":"Projected wayfinding universal-symbol set, 2032 horizon","b":"Extends pictogram research into a universal set.","f":["One symbol set serves global publics.","Testing validates comprehension."],"o":["Symbols","Testing","Adoption","Governance"],"g":"graphic"},{"t":"Projected design-history open canon, 2034 horizon","b":"Projects open-access growth into a design-history canon.","f":["Canonical works become freely available.","Non-Western design gains equal standing."],"o":["Canon","Licensing","Curation","Teaching"],"g":"theory"},{"t":"Projected biophilic-workplace standard, 2030 horizon","b":"Extends biophilia research into a workplace standard.","f":["Nature contact becomes a design requirement.","Wellbeing metrics improve."],"o":["Requirements","Metrics","Design","Verification"],"g":"interior"},{"t":"Projected slow-fashion consumer label, 2028 horizon","b":"Projects transparency pilots into a consumer label.","f":["Durability and labor data appear on labels.","Fast fashion loses share."],"o":["Label","Data","Audits","Market"],"g":"fashion"}];
var FNOTES=["Fashion records note the craft area — patternmaking, textiles, or business.","Interior records carry the space type — residential, workplace, or public.","Industrial records distinguish product, interaction, or systems design.","Graphic records note the medium — print, digital, or environmental.","Theory records name the school or movement addressed.","Sustainability records state the strategy — reduce, reuse, or regenerate."];
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
var gen={version:'jahdb-design-fields-published-1.0',generate:generate,validate:validate,selftest:selftest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();