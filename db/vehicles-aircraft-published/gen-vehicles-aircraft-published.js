(function(){'use strict';
var SLUG='vehicles-aircraft-published';
var PREFIX='JAH-vehicles-aircraft-published-P-';
var STUDY='vehicles-aircraft';
var FIELD='Motor Vehicles, Ships and Aircraft';
var CATS=["aviation-maintenance","automotive-tech","marine-engineering","aircraft-systems","vehicle-electrics","regulations"];
var DATA={"works":[{"t":"Aircraft Basic Science","a":"Michael Kroes; James Rardon","p":"McGraw-Hill","y":2013,"g":"aviation-maintenance","ref":"ISBN 978-0071799171, McGraw-Hill, 8th edition.","ov":"Physics and mathematics for aviation maintenance technicians: the foundation for airframe and powerplant study.","f":["Applied physics makes maintenance procedures understandable, not just memorizable.","Weight and balance math is a daily technician task."],"ch":["physics","mathematics","aircraft drawings","weight and balance"]},{"t":"Standard Aircraft Handbook for Mechanics and Technicians","a":"Ronald Sterkenburg; Peng Hao Wang","p":"McGraw-Hill","y":2021,"g":"aviation-maintenance","ref":"ISBN 978-1260468922, McGraw-Hill, 8th edition.","ov":"Shop practices for aircraft technicians: hardware, safety wire, riveting, and corrosion control.","f":["Proper hardware installation is a safety-of-flight matter.","Corrosion control preserves airframe life."],"ch":["hardware","safety wire","riveting","corrosion control"]},{"t":"Aviation Maintenance Technician Handbook: Airframe (FAA-H-8083-31)","a":"Federal Aviation Administration","p":"FAA","y":2018,"g":"aviation-maintenance","ref":"FAA-H-8083-31, 2018, U.S. FAA.","ov":"The FAA's official airframe handbook: structures, systems, and inspections for A&P mechanics.","f":["Standardized procedures keep the national fleet airworthy.","Inspection methods catch damage before it becomes failure."],"ch":["aircraft structures","hydraulics","landing gear","inspections"]},{"t":"Aviation Maintenance Technician Handbook: Powerplant (FAA-H-8083-32)","a":"Federal Aviation Administration","p":"FAA","y":2018,"g":"aircraft-systems","ref":"FAA-H-8083-32, 2018, U.S. FAA.","ov":"The FAA's official powerplant handbook: reciprocating and turbine engines, propellers, and systems.","f":["Engine theory explains every troubleshooting step.","Turbine engine familiarity is now essential for technicians."],"ch":["reciprocating engines","turbine engines","propellers","engine inspection"]},{"t":"Aircraft Powerplants","a":"Michael Kroes; Thomas Wild","p":"McGraw-Hill","y":2013,"g":"aircraft-systems","ref":"ISBN 978-0071799171, McGraw-Hill, 9th edition.","ov":"Aircraft engine systems: operation, maintenance, and overhaul practices.","f":["Systems knowledge prevents misdiagnosis of engine faults.","Overhaul practices demand exacting measurement discipline."],"ch":["engine principles","induction and exhaust","ignition systems","overhaul"]},{"t":"Automotive Technology: Principles, Diagnosis, and Service","a":"James D. Halderman","p":"Pearson","y":2019,"g":"automotive-tech","ref":"ISBN 978-0135257272, Pearson, 6th edition.","ov":"Comprehensive automotive text covering diagnosis and service across all vehicle systems.","f":["Diagnosis strategy matters more than any single test.","Electrical understanding unlocks modern vehicle repair."],"ch":["engines","automatic transmissions","brakes","engine performance"]},{"t":"Modern Automotive Technology","a":"James E. Duffy","p":"Goodheart-Willcox","y":2020,"g":"automotive-tech","ref":"ISBN 978-1635635785, Goodheart-Willcox, 9th edition.","ov":"Automotive systems with strong coverage of hybrids, EVs, and advanced driver assistance.","f":["High-voltage safety is now core technician knowledge.","ADAS calibration is becoming routine service work."],"ch":["hybrid and electric vehicles","engine systems","chassis","advanced technologies"]},{"t":"Automotive Service: Inspection, Maintenance, Repair","a":"Tim Gilles","p":"Cengage Learning","y":2019,"g":"automotive-tech","ref":"ISBN 978-1337793392, Cengage Learning, 6th edition.","ov":"Service-oriented automotive text aligned to ASE certification areas.","f":["ASE task lists mirror real shop work orders.","Inspection routines catch failures before breakdowns."],"ch":["safety and service","engine repair","electrical","brakes"]},{"t":"Bosch Automotive Handbook","a":"Robert Bosch GmbH","p":"SAE International","y":2014,"g":"vehicle-electrics","ref":"ISBN 978-0768081527, SAE, 9th edition.","ov":"The dense reference for automotive engineering data: formulas, systems, and components.","f":["Consolidated data accelerates engineering decisions.","The handbook's diagrams are an industry standard."],"ch":["powertrain","chassis systems","electrical systems","formulas"]},{"t":"Ship Construction","a":"D. J. Eyres; George J. Bruce","p":"Butterworth-Heinemann","y":2012,"g":"marine-engineering","ref":"ISBN 978-0080972398, Butterworth-Heinemann, 7th edition.","ov":"Shipbuilding practice: hull structure, welding, launching, and outfitting.","f":["Block construction methods dominate modern shipyards.","Welding quality determines hull integrity."],"ch":["hull structure","shipbuilding methods","launching","outfitting"]},{"t":"Introduction to Naval Architecture","a":"E. C. Tupper","p":"Butterworth-Heinemann","y":2013,"g":"marine-engineering","ref":"ISBN 978-0080982373, Butterworth-Heinemann, 5th edition.","ov":"Stability, resistance, propulsion, and structures for naval architects.","f":["Stability calculations are the foundation of ship safety.","Model testing still validates computational predictions."],"ch":["stability","resistance","propulsion","ship structures"]},{"t":"Reeds Vol 8: General Engineering Knowledge for Marine Engineers","a":"Paul Russell; Leslie Jackson","p":"Reeds (Bloomsbury)","y":2015,"g":"marine-engineering","ref":"ISBN 978-1472901511, Reeds.","ov":"Marine engineering knowledge for professional certification examinations.","f":["Exam syllabi track real watchkeeping duties.","Auxiliary machinery knowledge separates engineers from fitters."],"ch":["auxiliary machinery","refrigeration","steering gear","deck machinery"]}],"lvl2":[{"t":"Projected electric aircraft maintenance curriculum","g":"aviation-maintenance","b":"Electric trainers are entering flight schools.","d":"Projects a maintenance curriculum for battery-electric aircraft: high-voltage safety, battery health, and thermal management."},{"t":"Projected autonomous ship operations handbook","g":"marine-engineering","b":"Remotely operated vessels are in commercial trials.","d":"Projects an operations handbook for shore control centers supervising autonomous ships."},{"t":"Projected EV battery service technician text","g":"automotive-tech","b":"Battery replacement is becoming routine shop work.","d":"Projects a technician text for pack diagnostics, module replacement, and thermal system service."},{"t":"Projected urban air mobility ground-ops manual","g":"regulations","b":"eVTOL certification programs are advancing.","d":"Projects a ground-operations manual for vertiports: charging, turnaround, and emergency procedures."},{"t":"Projected hydrogen marine propulsion guide","g":"marine-engineering","b":"Hydrogen and ammonia are candidate marine fuels.","d":"Projects a propulsion guide for hydrogen-fueled vessels: bunkering, storage, and safety systems."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-vehicles-aircraft-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
