(function(){'use strict';
var SLUG='mechanics-metal-published';
var PREFIX='JAH-mechanics-metal-published-P-';
var STUDY='mechanics-metal';
var FIELD='Mechanics and Metal Trades';
var CATS=["machining","welding","sheet-metal","blueprint-reading","metallurgy","maintenance"];
var DATA={"works":[{"t":"Machinery's Handbook","a":"Erik Oberg; Franklin D. Jones; Holbrook L. Horton","p":"Industrial Press","y":2020,"g":"machining","ref":"ISBN 978-0831136815, Industrial Press, 30th edition.","ov":"The machinist's bible since 1914: threads, feeds, speeds, tolerances, and materials data.","f":["One reference eliminates most shop-floor guesswork.","Thread and tolerance tables are consulted daily in machine shops."],"ch":["threads","machining operations","tolerances","materials"]},{"t":"Machine Tool Practices","a":"Richard R. Kibbe; Roland O. Meyer; Warren T. White","p":"Pearson","y":2014,"g":"machining","ref":"ISBN 978-0133354265, Pearson, 10th edition.","ov":"Comprehensive machine shop text: measurement, layout, and operation of manual machine tools.","f":["Measurement skill precedes machining skill.","Safe setup procedure prevents most shop accidents."],"ch":["measurement","layout","drill press","lathe operations"]},{"t":"Welding: Principles and Applications","a":"Larry Jeffus","p":"Cengage Learning","y":2016,"g":"welding","ref":"ISBN 978-1305494695, Cengage Learning, 8th edition.","ov":"The standard welding text: processes, metallurgy, symbols, and certification preparation.","f":["Understanding the arc beats memorizing settings.","Welding symbols are the language of fabrication drawings."],"ch":["oxyfuel processes","shielded metal arc","gas metal arc","welding metallurgy"]},{"t":"Modern Welding","a":"Andrew D. Althouse; Carl H. Turnquist; William A. Bowditch","p":"Goodheart-Willcox","y":2012,"g":"welding","ref":"ISBN 978-1605257952, Goodheart-Willcox, 11th edition.","ov":"Broad coverage of welding and cutting processes with strong safety emphasis.","f":["Process selection follows from joint design and production volume.","Safety discipline is inseparable from welding skill."],"ch":["welding safety","arc welding","gas tungsten arc","brazing and soldering"]},{"t":"Welding Skills","a":"B. J. Moniz","p":"American Technical Publishers","y":2015,"g":"welding","ref":"ISBN 978-0826930871, ATP, 5th edition.","ov":"Skills-based welding instruction aligned to AWS certification tasks.","f":["Guided practice sequences build certifiable skills.","Inspection criteria teach welders to judge their own work."],"ch":["safety","SMAW","GMAW","welding inspection"]},{"t":"Technology of Machine Tools","a":"Steve F. Krar; Arthur R. Gill","p":"McGraw-Hill","y":1990,"g":"machining","ref":"ISBN 978-0070354292, McGraw-Hill, 5th edition.","ov":"Machine tool technology from manual machines through CNC fundamentals.","f":["Manual machining teaches the feel CNC operators still need.","Cutting tool geometry determines surface finish."],"ch":["safety","metrology","milling machines","CNC basics"]},{"t":"Blueprint Reading for the Machine Trades","a":"Russ Schultz; Larry Smith","p":"Pearson","y":2011,"g":"blueprint-reading","ref":"ISBN 978-0132173198, Pearson, 6th edition.","ov":"Reading engineering drawings: views, dimensions, tolerances, and GD&T basics.","f":["Drawings are contracts; misreading them is expensive.","GD&T symbols carry precise manufacturing meaning."],"ch":["orthographic projection","dimensioning","tolerancing","geometric dimensioning"]},{"t":"Metallurgy Fundamentals","a":"Daniel A. Brandt; J. C. Warner","p":"Goodheart-Willcox","y":2009,"g":"metallurgy","ref":"ISBN 978-1590707122, Goodheart-Willcox, 5th edition.","ov":"Ferrous and nonferrous metallurgy: structure, heat treatment, and testing.","f":["Heat treatment transforms the same steel into different materials.","Microstructure explains mechanical properties."],"ch":["metal structure","iron and steel","heat treatment","nonferrous metals"]},{"t":"Automotive Mechanics","a":"William H. Crouse; Donald L. Anglin","p":"McGraw-Hill","y":1993,"g":"maintenance","ref":"ISBN 978-0070148399, McGraw-Hill, 10th edition.","ov":"Classic comprehensive automotive mechanics: engines, drivetrains, and chassis systems.","f":["Systems thinking diagnoses cars faster than part-swapping.","Engine theory grounds every repair procedure."],"ch":["engines","fuel systems","electrical systems","chassis"]},{"t":"Machine Shop Theory and Practice","a":"Albert A. Wagener; Harlan R. Legg","p":"Delmar Cengage","y":1992,"g":"machining","ref":"ISBN 978-0827333580, Delmar.","ov":"Shop theory paired with practice projects for machining students.","f":["Project-based learning builds both skill and judgment.","Theory sticks when the next cut depends on it."],"ch":["benchwork","lathe","milling","grinding"]},{"t":"Sheet Metal Handbook","a":"Ron Fournier; Sue Fournier","p":"HPBooks","y":1989,"g":"sheet-metal","ref":"ISBN 978-0895866465, HPBooks.","ov":"Practical sheet metal fabrication: cutting, bending, and forming for automotive and custom work.","f":["Layout skill determines fabrication quality.","Simple hand tools produce professional results with practice."],"ch":["tools","layout","cutting","forming and finishing"]},{"t":"Maintenance Engineering Handbook","a":"R. Keith Mobley","p":"McGraw-Hill","y":2014,"g":"maintenance","ref":"ISBN 978-0071826617, McGraw-Hill, 8th edition.","ov":"Plant maintenance management: preventive, predictive, and reliability-centered strategies.","f":["Predictive maintenance pays for its instruments quickly.","Reliability-centered methods focus effort where failure costs most."],"ch":["maintenance management","predictive technologies","lubrication","reliability engineering"]}],"lvl2":[{"t":"Projected additive-manufacturing machinist guide","g":"machining","b":"Metal 3D printing is entering job shops.","d":"Projects a machinist's guide to hybrid additive-subtractive workflows, from print orientation to finish machining."},{"t":"Projected robotic welding cell programming text","g":"welding","b":"Collaborative welding robots are reaching small fabricators.","d":"Projects a programming text for cobot welding cells: path teaching, weave patterns, and weld monitoring."},{"t":"Projected digital-twin maintenance curriculum","g":"maintenance","b":"Vibration and thermal data are streaming from more machines.","d":"Projects a curriculum for vibration analysis and thermography tied to digital twin dashboards."},{"t":"Projected exoskeleton ergonomics manual for metal trades","g":"sheet-metal","b":"Industrial exoskeletons are entering heavy fabrication.","d":"Projects an ergonomics manual for exoskeleton-assisted lifting, fitting, and overhead welding."},{"t":"Projected green steel fabrication handbook","g":"metallurgy","b":"Low-carbon steel is entering supply chains.","d":"Projects a fabrication handbook covering weldability and forming of hydrogen-reduced steels."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-mechanics-metal-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
