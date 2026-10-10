(function(){'use strict';
var SLUG='electronics-automation-published';
var PREFIX='JAH-electronics-automation-published-P-';
var STUDY='electronics-automation';
var FIELD='Electronics and Automation';
var CATS=["basic-electronics","digital-electronics","plc-automation","instrumentation","mechatronics","soldering-standards"];
var DATA={"works":[{"t":"The Art of Electronics","a":"Paul Horowitz; Winfield Hill","p":"Cambridge University Press","y":2015,"g":"basic-electronics","ref":"ISBN 978-0521809269, Cambridge University Press, 3rd edition.","ov":"The definitive practical electronics text: circuit design wisdom from decades of laboratory experience.","f":["Good design is mostly about avoiding known pitfalls.","The transistor chapters alone justify the book's reputation."],"ch":["foundations","transistors","operational amplifiers","filters"]},{"t":"Practical Electronics for Inventors","a":"Paul Scherz; Simon Monk","p":"McGraw-Hill","y":2016,"g":"basic-electronics","ref":"ISBN 978-1259587542, McGraw-Hill, 4th edition.","ov":"Hands-on electronics for makers: components, circuits, and projects from theory to bench.","f":["Building circuits teaches what equations only describe.","A stocked bench beats a bigger textbook for beginners."],"ch":["components","basic theory","power supplies","digital electronics"]},{"t":"Grob's Basic Electronics","a":"Mitchel E. Schultz","p":"McGraw-Hill","y":2020,"g":"basic-electronics","ref":"ISBN 978-1260500056, McGraw-Hill, 4th edition.","ov":"Introductory electronics covering DC, AC, semiconductors, and digital fundamentals.","f":["DC mastery is the prerequisite for everything electronic.","Troubleshooting skill comes from measuring real circuits."],"ch":["DC circuits","magnetism and AC","semiconductors","digital basics"]},{"t":"Programmable Logic Controllers","a":"Frank D. Petruzella","p":"McGraw-Hill","y":2016,"g":"plc-automation","ref":"ISBN 978-0073373843, McGraw-Hill, 5th edition.","ov":"The standard PLC text: ladder logic, programming, and industrial applications.","f":["Ladder logic maps directly to the relay circuits it replaced.","Structured troubleshooting beats guessing at I/O faults."],"ch":["PLC hardware","ladder logic programming","timers and counters","industrial applications"]},{"t":"Make: Electronics","a":"Charles Platt","p":"Maker Media","y":2015,"g":"basic-electronics","ref":"ISBN 978-1680450262, Maker Media, 2nd edition.","ov":"Learning electronics by destruction and discovery: hands-on experiments that burn things safely.","f":["Deliberate mistakes teach component limits permanently.","Experiment-first learning sticks better than lecture-first."],"ch":["switching and relays","capacitors","transistors","integrated circuits"]},{"t":"Getting Started in Electronics","a":"Forrest M. Mims III","p":"Master Publishing","y":2003,"g":"basic-electronics","ref":"ISBN 978-0945053286, Master Publishing, 3rd edition.","ov":"The classic beginner's notebook: hand-drawn circuits and clear explanations.","f":["Simple circuits build intuition that scales to complex systems.","Mims's 555 timer circuits remain the best introduction."],"ch":["electronic components","basic circuits","the 555 timer","digital circuits"]},{"t":"Digital Design","a":"M. Morris Mano; Michael D. Ciletti","p":"Pearson","y":2012,"g":"digital-electronics","ref":"ISBN 978-0132774208, Pearson, 5th edition.","ov":"Combinational and sequential logic design from gates to registers and processors.","f":["Boolean algebra minimization still matters for real hardware.","State machine design is the heart of digital systems."],"ch":["binary systems","combinational logic","sequential circuits","registers and counters"]},{"t":"Mechatronics: Electronic Control Systems in Mechanical and Electrical Engineering","a":"William Bolton","p":"Pearson","y":2015,"g":"mechatronics","ref":"ISBN 978-1292076683, Pearson, 6th edition.","ov":"Integrated treatment of mechanical systems, electronics, and control.","f":["Mechatronic thinking dissolves the mechanical-electrical divide.","Sensor selection determines system capability."],"ch":["sensors","actuators","control systems","microprocessor systems"]},{"t":"Automating Manufacturing Systems with PLCs","a":"Hugh Jack","p":"Hugh Jack (open text)","y":2007,"g":"plc-automation","ref":"Open textbook, ver 5.0, lulu.com. Free educational use.","ov":"Free, comprehensive PLC and automation text used worldwide in technical education.","f":["Open texts can match commercial books in technical depth.","Continuous revision keeps automation content current."],"ch":["continuous control","ladder logic","structured text","networking"]},{"t":"IPC-A-610 Acceptability of Electronic Assemblies","a":"IPC","p":"IPC","y":2020,"g":"soldering-standards","ref":"IPC-A-610H, 2020, IPC.","ov":"The industry standard defining acceptable workmanship for electronic assemblies.","f":["Illustrated accept/reject criteria align the whole supply chain.","Workmanship standards reduce field failures measurably."],"ch":["soldering criteria","component mounting","cable and wire","conformal coating"]},{"t":"Process Control Instrumentation Technology","a":"Curtis D. Johnson","p":"Pearson","y":2013,"g":"instrumentation","ref":"ISBN 978-0135117341, Pearson, 8th edition.","ov":"Sensors, transmitters, and control elements for process industries.","f":["Calibration discipline is the foundation of process control.","The 4-20 mA loop remains the workhorse of industry."],"ch":["measurement fundamentals","pressure and level","temperature","final control elements"]},{"t":"Robotics, Vision and Control","a":"Peter Corke","p":"Springer","y":2017,"g":"mechatronics","ref":"ISBN 978-3319544120, Springer, 2nd edition.","ov":"Fundamental algorithms for robotic manipulation and vision with MATLAB examples.","f":["Homogeneous transforms unify robot kinematics.","Vision-based control closes the loop on uncertainty."],"ch":["kinematics","dynamics","computer vision","visual servoing"]}],"lvl2":[{"t":"Projected collaborative-robot cell design guide","g":"mechatronics","b":"Cobots are moving into small shops without cages.","d":"Projects a design guide for risk-assessed cobot cells: force limiting, task allocation, and operator training."},{"t":"Projected open-PLC curriculum for technicians","g":"plc-automation","b":"Open-source PLC runtimes are reaching industrial reliability.","d":"Projects a technician curriculum around open PLC platforms, from IEC 61131-3 to networked I/O."},{"t":"Projected lead-free reliability handbook","g":"soldering-standards","b":"High-reliability sectors still debate lead-free solder joint life.","d":"Projects a reliability handbook for lead-free assemblies in harsh environments with accelerated test data."},{"t":"Projected wireless sensor retrofit manual","g":"instrumentation","b":"Battery-powered sensors are retrofitting legacy plants.","d":"Projects a retrofit manual for wirelessHART and LoRa sensors on existing process equipment."},{"t":"Projected edge-AI vision inspection text","g":"digital-electronics","b":"On-camera inference is replacing PC-based vision.","d":"Projects a text on deploying quantized vision models at the edge for quality inspection."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-electronics-automation-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
