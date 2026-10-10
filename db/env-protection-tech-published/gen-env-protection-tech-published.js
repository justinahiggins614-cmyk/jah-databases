(function(){'use strict';
var SLUG='env-protection-tech-published';
var PREFIX='JAH-env-protection-tech-published-P-';
var STUDY='env-protection-tech';
var FIELD='Environmental Protection Technology';
var CATS=["water-treatment","air-quality","waste-management","environmental-monitoring","regulations","sustainability"];
var DATA={"works":[{"t":"Environmental Engineering: Fundamentals, Sustainability, Design","a":"James R. Mihelcic; Julie Beth Zimmerman","p":"Wiley","y":2014,"g":"sustainability","ref":"ISBN 978-1118741498, Wiley, 2nd edition.","ov":"A sustainability-first environmental engineering text covering water, air, and waste with design examples.","f":["Sustainability constraints improve designs instead of merely restricting them.","Mass and energy balances unify all environmental media."],"ch":["sustainability and engineering","water quality","water treatment","air quality"]},{"t":"Water Treatment: Principles and Design","a":"John C. Crittenden; R. Rhodes Trussell; David W. Hand","p":"Wiley","y":2012,"g":"water-treatment","ref":"ISBN 978-0470405390, Wiley, 3rd edition.","ov":"The MWH reference on drinking water treatment: coagulation, filtration, disinfection, and membranes.","f":["Multiple barriers are the foundation of safe drinking water.","Disinfection byproduct control shapes modern plant design."],"ch":["coagulation and flocculation","sedimentation","granular filtration","disinfection"]},{"t":"Wastewater Engineering: Treatment and Reuse","a":"Metcalf & Eddy; George Tchobanoglous","p":"McGraw-Hill","y":2013,"g":"water-treatment","ref":"ISBN 978-0073401188, McGraw-Hill, 5th edition.","ov":"The definitive wastewater treatment reference: biological processes, nutrient removal, and reuse.","f":["Biological nutrient removal is now standard practice.","Water reuse turns effluent from waste into resource."],"ch":["wastewater characteristics","biological treatment","nutrient removal","water reuse"]},{"t":"Air Pollution Control Engineering","a":"Noel de Nevers","p":"Waveland Press","y":2017,"g":"air-quality","ref":"ISBN 978-1478637305, Waveland Press, 3rd edition.","ov":"Engineering analysis of particulate and gaseous air pollution control equipment.","f":["Control device selection follows from pollutant properties.","Efficiency claims must be checked against operating conditions."],"ch":["particulate control","electrostatic precipitators","gaseous pollutant control","dispersion modeling"]},{"t":"Hazardous Waste Management","a":"Michael D. LaGrega; Phillip L. Buckingham; Jeffrey C. Evans","p":"Waveland Press","y":2010,"g":"waste-management","ref":"ISBN 978-1577666936, Waveland Press, 2nd edition.","ov":"Covers hazardous waste characterization, treatment technologies, and landfill design.","f":["Waste minimization outranks treatment in the management hierarchy.","Landfill liner systems are engineered for centuries of containment."],"ch":["waste characterization","thermal treatment","stabilization","landfill design"]},{"t":"Solid Waste Engineering","a":"William A. Worrell; P. Aarne Vesilind","p":"Cengage Learning","y":2011,"g":"waste-management","ref":"ISBN 978-1439061357, Cengage Learning, 2nd edition.","ov":"Municipal solid waste collection, recycling, composting, and disposal engineering.","f":["Collection logistics dominate solid waste system costs.","Recycling markets determine what recovery is actually possible."],"ch":["waste generation","collection systems","materials recovery","composting"]},{"t":"Environmental Sampling and Analysis for Technicians","a":"Maria Csuros; Csaba Csuros","p":"CRC Press","y":2002,"g":"environmental-monitoring","ref":"ISBN 978-1566705724, CRC Press.","ov":"Field and laboratory procedures for environmental sampling, written for technicians.","f":["Sample integrity determines whether analysis means anything.","Chain of custody is a legal as well as technical requirement."],"ch":["sampling design","water sampling","soil sampling","quality assurance"]},{"t":"Industrial Waste Treatment Handbook","a":"Frank Woodard","p":"Butterworth-Heinemann","y":2001,"g":"water-treatment","ref":"ISBN 978-0750673363, Butterworth-Heinemann, 2nd edition.","ov":"Practical treatment methods for industrial wastewaters across manufacturing sectors.","f":["Segregating waste streams simplifies treatment enormously.","Pretreatment protects municipal plants from industrial shocks."],"ch":["waste surveys","physical treatment","chemical treatment","sludge handling"]},{"t":"Principles of Environmental Engineering and Science","a":"Mackenzie L. Davis; Susan J. Masten","p":"McGraw-Hill","y":2013,"g":"sustainability","ref":"ISBN 978-0073397900, McGraw-Hill, 3rd edition.","ov":"Undergraduate introduction to environmental engineering calculations and concepts.","f":["Risk assessment gives quantitative meaning to environmental standards.","Reactor models from chemical engineering apply directly."],"ch":["environmental chemistry","risk assessment","water supply","air pollution"]},{"t":"ISO 14001:2015 Environmental management systems","a":"International Organization for Standardization","p":"ISO","y":2015,"g":"regulations","ref":"ISO 14001:2015, International Organization for Standardization.","ov":"The international standard specifying requirements for an environmental management system.","f":["The plan-do-check-act cycle drives continual improvement.","Leadership commitment is an explicit requirement, not a suggestion."],"ch":["context of the organization","leadership","planning","performance evaluation"]},{"t":"Handbook of Environmental Engineering Calculations","a":"C. C. Lee","p":"McGraw-Hill","y":2007,"g":"environmental-monitoring","ref":"ISBN 978-0071475453, McGraw-Hill, 2nd edition.","ov":"Worked calculation methods for air, water, and waste engineering problems.","f":["Worked examples bridge theory and permit applications.","Unit conversions cause more errors than complex math."],"ch":["air pollution calculations","water treatment calculations","noise calculations","solid waste calculations"]},{"t":"Introduction to Environmental Engineering","a":"P. Aarne Vesilind; Susan M. Morgan; Lauren G. Heine","p":"Cengage Learning","y":2009,"g":"regulations","ref":"ISBN 978-0495295855, Cengage Learning, 3rd edition.","ov":"Accessible introduction covering the major environmental regulations and engineering responses.","f":["Regulation history explains current engineering practice.","Ethics cases show why compliance is a floor, not a ceiling."],"ch":["environmental regulations","water quality","air quality","solid and hazardous waste"]}],"lvl2":[{"t":"Projected direct-air-capture operations manual","g":"air-quality","b":"Direct air capture is moving from demonstration to deployment.","d":"Projects an operations manual for sorbent management, energy integration, and monitoring of DAC facilities."},{"t":"Projected PFAS treatment technology guide","g":"water-treatment","b":"Regulatory limits for PFAS keep tightening worldwide.","d":"Projects a technology guide comparing destruction versus separation methods for per- and polyfluoroalkyl substances."},{"t":"Projected circular-economy plant design text","g":"sustainability","b":"Industrial symbiosis is becoming standard planning practice.","d":"Projects a design text for plants where one facility's waste is another's feedstock, with mass-balance methods."},{"t":"Projected microplastics monitoring protocol","g":"environmental-monitoring","b":"Standardized microplastics measurement is still emerging.","d":"Projects a field protocol for sampling, QA, and reporting microplastics in water and soil."},{"t":"Projected e-waste recovery technician curriculum","g":"waste-management","b":"Electronics waste is the fastest-growing waste stream.","d":"Projects a technician curriculum for safe disassembly, material recovery, and data destruction."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-env-protection-tech-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
