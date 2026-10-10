(function(){'use strict';
var SLUG='chemical-engineering-published';
var PREFIX='JAH-chemical-engineering-published-P-';
var STUDY='chemical-engineering';
var FIELD='Chemical Engineering and Processes';
var CATS=["unit-operations","process-design","reaction-engineering","transport-phenomena","process-control","safety"];
var DATA={"works":[{"t":"Perry's Chemical Engineers' Handbook","a":"Don W. Green; Marylee Z. Southard","p":"McGraw-Hill","y":2019,"g":"process-design","ref":"ISBN 978-0071834087, McGraw-Hill, 9th edition.","ov":"The bible of chemical engineering: physical properties, unit operations, process control, and design data in one reference.","f":["Consolidated property data saves more design time than any single correlation.","The handbook's breadth makes it the first stop for any process question."],"ch":["physical and chemical data","heat and mass transfer","reactors","process control and instrumentation"]},{"t":"Unit Operations of Chemical Engineering","a":"Warren L. McCabe; Julian C. Smith; Peter Harriott","p":"McGraw-Hill","y":2004,"g":"unit-operations","ref":"ISBN 978-0072848236, McGraw-Hill, 7th edition.","ov":"The classic treatment of distillation, absorption, filtration, drying, and other unit operations.","f":["A few transport principles explain dozens of different equipment types.","Stage-wise and rate-based models cover nearly all separations."],"ch":["fluid mechanics","heat transfer","distillation","liquid-liquid extraction"]},{"t":"Chemical Engineering Design","a":"Gavin Towler; Ray Sinnott","p":"Butterworth-Heinemann","y":2021,"g":"process-design","ref":"ISBN 978-0081025994, Butterworth-Heinemann, 3rd edition.","ov":"Coulson and Richardson's design volume: from process synthesis to equipment sizing and economics.","f":["Process synthesis decisions lock in most of a plant's economics.","Safety and environmental constraints shape design from the first flowsheet."],"ch":["process synthesis","piping and instrumentation","separation columns","economic evaluation"]},{"t":"Transport Phenomena","a":"R. Byron Bird; Warren E. Stewart; Edwin N. Lightfoot","p":"Wiley","y":2006,"g":"transport-phenomena","ref":"ISBN 978-0470115398, Wiley, 2nd revised edition.","ov":"The unified treatment of momentum, heat, and mass transfer that defines the discipline.","f":["One set of balance equations describes all three transport modes.","Shell balances turn physical intuition into working models."],"ch":["viscosity and momentum transport","energy transport","mass transport","dimensional analysis"]},{"t":"Chemical Reaction Engineering","a":"Octave Levenspiel","p":"Wiley","y":1998,"g":"reaction-engineering","ref":"ISBN 978-0471254249, Wiley, 3rd edition.","ov":"Levenspiel's clear, example-driven introduction to reactor design and reaction kinetics.","f":["The design equation for each reactor type follows from one mole balance.","Residence time distribution explains real reactor deviations."],"ch":["homogeneous reactions","batch reactors","flow reactors","nonideal flow"]},{"t":"Essentials of Chemical Reaction Engineering","a":"H. Scott Fogler","p":"Pearson","y":2017,"g":"reaction-engineering","ref":"ISBN 978-0134663856, Pearson, 2nd edition.","ov":"Fogler's streamlined reaction engineering text with industrial examples and software-based problem solving.","f":["Mole balances plus rate laws size every ideal reactor.","Multiple reactions require selectivity analysis, not just conversion."],"ch":["mole balances","conversion and reactor sizing","rate laws","catalysis"]},{"t":"Plant Design and Economics for Chemical Engineers","a":"Max S. Peters; Klaus D. Timmerhaus; Ronald E. West","p":"McGraw-Hill","y":2002,"g":"process-design","ref":"ISBN 978-0072392661, McGraw-Hill, 5th edition.","ov":"Capital cost estimation, profitability analysis, and plant design practice for engineers.","f":["Early cost estimates guide process selection more than detailed design does.","Profitability methods must match the decision being made."],"ch":["capital cost estimation","interest and investment costs","profitability analysis","materials of construction"]},{"t":"Separation Process Engineering","a":"Phillip C. Wankat","p":"Pearson","y":2016,"g":"unit-operations","ref":"ISBN 978-0134181028, Pearson, 4th edition.","ov":"Modern coverage of distillation, absorption, extraction, adsorption, and membrane separations.","f":["Equilibrium-stage concepts transfer across separation methods.","Membrane processes are displacing thermal separations where selectivity allows."],"ch":["flash distillation","column distillation","absorption and stripping","membrane separations"]},{"t":"Process Dynamics and Control","a":"Dale E. Seborg; Thomas F. Edgar; Duncan A. Mellichamp","p":"Wiley","y":2010,"g":"process-control","ref":"ISBN 978-0470128671, Wiley, 3rd edition.","ov":"Dynamic modeling and control system design for chemical processes, from PID to model predictive control.","f":["Good control starts with understanding process dynamics, not tuning rules.","Model predictive control handles the multivariable loops PID cannot."],"ch":["dynamic models","feedback control","PID controller tuning","multivariable control"]},{"t":"Process Systems Analysis and Control","a":"Donald R. Coughanowr; Steven E. LeBlanc","p":"McGraw-Hill","y":2008,"g":"process-control","ref":"ISBN 978-0073397894, McGraw-Hill, 3rd edition.","ov":"Laplace-domain analysis of process control systems with worked chemical engineering examples.","f":["Transfer functions make controller comparison rigorous.","Stability analysis prevents dangerous controller designs."],"ch":["Laplace transforms","first-order systems","frequency response","control system design"]},{"t":"Guidelines for Chemical Process Quantitative Risk Analysis","a":"Center for Chemical Process Safety; AIChE","p":"Wiley-AIChE","y":2000,"g":"safety","ref":"ISBN 978-0816907205, CCPS/AIChE, 2nd edition.","ov":"The CCPS methodology for identifying hazards and quantifying process risk.","f":["Quantified risk lets engineers compare safeguards on equal terms.","Hazard identification quality determines the whole analysis."],"ch":["hazard identification","consequence analysis","frequency analysis","risk measures"]},{"t":"Chemical Process Safety: Fundamentals with Applications","a":"Daniel A. Crowl; Joseph F. Louvar","p":"Pearson","y":2011,"g":"safety","ref":"ISBN 978-0131382268, Pearson, 3rd edition.","ov":"The standard undergraduate process safety text: toxicology, fires, explosions, and relief sizing.","f":["Inherently safer design beats add-on safeguards.","Relief system sizing is a core competency, not a specialty."],"ch":["toxicology","industrial hygiene","fires and explosions","relief sizing"]}],"lvl2":[{"t":"Projected electrified chemical processing handbook","g":"process-design","b":"Industrial electrification is reshaping heat-intensive processes.","d":"Projects a handbook for electric furnaces, heat pumps, and plasma reactors replacing fired heaters in chemical plants."},{"t":"Projected carbon-capture unit operations text","g":"unit-operations","b":"Point-source capture is scaling from pilot to commercial plants.","d":"Projects a unit-operations treatment of absorption, adsorption, and membrane capture with regeneration energy analysis."},{"t":"Projected digital-twin reactor operations guide","g":"reaction-engineering","b":"Real-time reactor models are moving from R&D to operations.","d":"Projects an operations guide for calibrating and trusting digital twins of catalytic reactors in daily use."},{"t":"Projected green hydrogen process safety manual","g":"safety","b":"Hydrogen production at scale introduces new hazard profiles.","d":"Projects a safety manual for electrolyzer halls, hydrogen blending, and leak detection at industrial scale."},{"t":"Projected autonomous process control curriculum","g":"process-control","b":"Self-optimizing plants are leaving the pilot stage.","d":"Projects a curriculum for engineers supervising autonomous control layers, including override discipline and audit."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-chemical-engineering-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
