(function(){'use strict';
/* JAH Sports Published Archive Database — deterministic boundless generator (jahdb-sports-study-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='sports-study-published';
var PREFIX='JAH-sports-study-published-P-';
var SIGPREFIX='JAH-sports-study-STUDY-S-';
var SIGURL='../sports-study-study/index.html?sig=';
var CATS=["coaching", "sports-medicine", "management", "training", "officiating", "sports-science"];
var WORKS=[{"c": ["sports-science", "training"], "t": "The Sports Gene: Inside the Science of Extraordinary Athletic Performance", "a": "David Epstein", "p": "Portfolio", "y": 2013, "s": "Portfolio/Penguin, 2013", "k": "book"}, {"c": ["training", "sports-medicine"], "t": "NASM Essentials of Personal Fitness Training", "a": "National Academy of Sports Medicine", "p": "Jones & Bartlett Learning", "y": 2021, "s": "7th edition", "k": "textbook"}, {"c": ["coaching"], "t": "Successful Coaching", "a": "Rainer Martens", "p": "Human Kinetics", "y": 2012, "s": "4th edition, Human Kinetics", "k": "textbook"}, {"c": ["sports-medicine", "training"], "t": "ACSM's Guidelines for Exercise Testing and Prescription", "a": "American College of Sports Medicine", "p": "Wolters Kluwer", "y": 2021, "s": "11th edition", "k": "manual"}, {"c": ["training"], "t": "Essentials of Strength Training and Conditioning", "a": "National Strength and Conditioning Association", "p": "Human Kinetics", "y": 2015, "s": "4th edition, Human Kinetics", "k": "textbook"}, {"c": ["management"], "t": "Principles and Practice of Sport Management", "a": "Lisa Pike Masteralexis; Carol A. Barr; Mary A. Hums", "p": "Jones & Bartlett Learning", "y": 2018, "s": "6th edition", "k": "textbook"}, {"c": ["sports-science"], "t": "Physiology of Sport and Exercise", "a": "Jack H. Wilmore; David L. Costill; W. Larry Kenney", "p": "Human Kinetics", "y": 2019, "s": "7th edition, Human Kinetics", "k": "textbook"}, {"c": ["officiating"], "t": "Laws of the Game", "a": "The International Football Association Board", "p": "IFAB", "y": 2024, "s": "2024/25 edition", "k": "rulebook"}, {"c": ["management", "officiating"], "t": "Sport Law: A Managerial Approach", "a": "Anita M. Moorman; Linda A. Sharp; Cathryn L. Claussen", "p": "Holcomb Hathaway", "y": 2020, "s": "4th edition", "k": "textbook"}, {"c": ["training", "coaching"], "t": "Periodization: Theory and Methodology of Training", "a": "Tudor O. Bompa; G. Gregory Haff", "p": "Human Kinetics", "y": 2018, "s": "6th edition, Human Kinetics", "k": "textbook"}];
var LEADS=["This work is a standard reference in sports education and coaching.", "This publication defines evidence-based practice in athletic development.", "This widely cited text shapes how athletes train and compete.", "This authoritative work links sports science to coaching practice.", "This reference anchors certification programs across the sports industry.", "This text systematizes the science of human performance."];
var FOCUS=["athlete development and periodized training", "injury prevention and rehabilitation", "coaching pedagogy and leadership", "sports organization management", "rules, officiating, and fair play", "exercise physiology and nutrition"];
var FINDINGS=["periodized programs outperform random training on strength and power gains", "structured warm-ups cut non-contact injury rates substantially", "coach-athlete communication quality predicts adherence and progress", "sleep extension improves reaction time and shooting accuracy", "clear officiating mechanics reduce contested calls and game delays", "progressive overload with deload weeks sustains long-term adaptation", "multidisciplinary support teams shorten return-to-play timelines", "goal-setting frameworks raise training consistency measurably"];
var CHAPTERS=["Foundations of sports science", "Exercise physiology", "Biomechanics of movement", "Strength and conditioning", "Periodization and program design", "Sports nutrition and hydration", "Injury prevention and care", "Coaching principles and pedagogy", "Officiating mechanics and rules", "Sports management and governance"];
var AUDIENCES=["coaches and trainers", "athletes and parents", "sports medicine professionals", "officials and administrators", "students of kinesiology"];
var L2=[{"topic": "AI coaching assistants", "horizon": "2028-2038"}, {"topic": "Biometric performance twins", "horizon": "2031-2041"}, {"topic": "Robotic training partners", "horizon": "2033-2043"}, {"topic": "Neuro-adaptive skill training", "horizon": "2034-2044"}, {"topic": "Global virtual competitions", "horizon": "2027-2037"}, {"topic": "Predictive injury prevention", "horizon": "2029-2039"}, {"topic": "Smart officiating systems", "horizon": "2030-2040"}, {"topic": "Personalized fan experiences", "horizon": "2026-2036"}];
var L2ANGLES=["data-driven athlete development", "human-AI coaching partnerships", "continuous biometric monitoring", "decentralized global competition", "injury-free performance targets", "augmented officiating accuracy"];
var L2SCEN=["every athlete trains with a live biometric digital twin", "coaches direct squads through AI-assisted game planning", "stadiums verify calls automatically in real time", "amateurs compete globally from local facilities", "injury prediction keeps squads at full strength", "fans experience matches through personalized immersive feeds"];
var L2FIND=["digital twins predict overtraining before symptoms appear", "AI assistants personalize every session to readiness scores", "smart venues automate officiating with verifiable accuracy", "virtual leagues expand participation beyond geography", "predictive models cut soft-tissue injuries substantially", "adaptive equipment customizes itself to each athlete"];
var L2ROAD=["validation of biometric prediction models", "athlete data-ownership frameworks", "certification for AI coaching tools", "pilot leagues with augmented officiating", "anti-tampering standards for performance data", "equitable access programs for adaptive tech"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in sports, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived sports literature into '+pick(L2ANGLES,rnd)+'. '+
    'Scenario: '+pick(L2SCEN,rnd)+'. '+
    'Projected findings: first, '+pick(L2FIND,rnd)+'; second, '+pick(L2FIND,rnd)+'; third, '+pick(L2FIND,rnd)+'. '+
    'Roadmap: '+pick(L2ROAD,rnd)+'; '+pick(L2ROAD,rnd)+'; '+pick(L2ROAD,rnd)+'. '+
    'Method: scenario synthesis across the Level 1 archive, checked for internal consistency.';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var idx=idxOf(seed),id=PREFIX+pad7(idx);
  var level=rnd()<0.55?1:2;
  var rec={id:id,title:'',authors:'',publication:'',year:0,full_content:'',source_ref:'',signature_link:SIGURL+SIGPREFIX+pad7(idx),category:'',level:level};
  if(level===1){
    var w=pick(WORKS,rnd);
    rec.category=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(w.c||CATS,rnd);
    rec.title=w.t;rec.authors=w.a;rec.publication=w.p;rec.year=w.y;
    rec.full_content=content1(rnd,w);rec.source_ref=w.s;
  }else{
    var t=pick(L2,rnd);
    rec.category=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
    rec.title='Level 2: '+t.topic+' - '+pick(L2ANGLES,rnd)+', '+t.horizon;
    rec.authors='JAH Signature Research Unit';rec.publication='JAH Signature Projection Series';
    rec.year=2026+ri(rnd,1,14);rec.full_content=content2(rnd,t);
    rec.source_ref='Signature projection model - scenario synthesis from the archived Level 1 works';
  }
  return rec;
}
var EXPECTED_KEYS=['authors','category','full_content','id','level','publication','signature_link','source_ref','title','year'];
/* 40 invariant checks. Each returns null (pass) or the failing check name. */
function checkList(r,seed){
  var out=[];
  function ck(name,ok){out.push([name,ok?null:name]);}
  var isObj=r&&typeof r==='object';
  ck('object',isObj);
  ck('id',isObj&&r.id===PREFIX+pad7(idxOf(seed)));
  ck('title',isObj&&typeof r.title==='string'&&r.title.length>0);
  ck('title-trim',isObj&&r.title===String(r.title).trim());
  ck('title-len',isObj&&String(r.title).length>=5&&String(r.title).length<=220);
  ck('title-nohtml',isObj&&String(r.title).indexOf('<')<0);
  var lvl=isObj&&(r.level===1||r.level===2);
  ck('level',lvl);
  ck('l2-title',!isObj||r.level!==2||/^Level 2/.test(r.title));
  ck('l1-title',!isObj||r.level!==1||!/^Level 2/.test(r.title));
  ck('authors',isObj&&typeof r.authors==='string'&&r.authors.length>0);
  ck('publication',isObj&&typeof r.publication==='string'&&r.publication.length>0);
  ck('year-int',isObj&&Number.isInteger(r.year));
  ck('l1-year',!isObj||r.level!==1||(r.year>=1500&&r.year<=2026));
  ck('l2-year',!isObj||r.level!==2||(r.year>=2026&&r.year<=2060));
  ck('content-str',isObj&&typeof r.full_content==='string');
  ck('content-min',isObj&&String(r.full_content).length>=420);
  ck('content-max',isObj&&String(r.full_content).length<=1500);
  ck('content-sent',isObj&&String(r.full_content).indexOf('. ')>0);
  ck('content-nohtml',isObj&&String(r.full_content).indexOf('<')<0);
  ck('source-ref',isObj&&typeof r.source_ref==='string'&&r.source_ref.length>0);
  ck('sig-link',isObj&&r.signature_link===SIGURL+SIGPREFIX+pad7(idxOf(seed)));
  ck('category',isObj&&(r.level===1?((WORK_BY_TITLE[r.title]||{}).c||CATS).indexOf(r.category)>=0:CATS.indexOf(r.category)>=0));
  var w=isObj&&r.level===1?WORK_BY_TITLE[r.title]:null;
  ck('l1-known',!isObj||r.level!==1||!!w);
  ck('l1-authors',!isObj||r.level!==1||!w||r.authors===w.a);
  ck('l1-pub',!isObj||r.level!==1||!w||r.publication===w.p);
  ck('l1-year2',!isObj||r.level!==1||!w||r.year===w.y);
  ck('l1-src',!isObj||r.level!==1||!w||r.source_ref===w.s);
  ck('l1-in-content',!isObj||r.level!==1||!w||String(r.full_content).indexOf(w.t)>=0);
  ck('l2-authors',!isObj||r.level!==2||r.authors==='JAH Signature Research Unit');
  ck('l2-pub',!isObj||r.level!==2||r.publication==='JAH Signature Projection Series');
  ck('l2-topic',!isObj||r.level!==2||L2.some(function(t){return String(r.title).indexOf(t.topic)>=0;}));
  ck('words',isObj&&words(r.full_content)>=70);
  var rt=false;try{rt=JSON.stringify(JSON.parse(JSON.stringify(r)))===JSON.stringify(r);}catch(x){}
  ck('roundtrip',rt);
  var keys=isObj?Object.keys(r).sort():[];
  ck('keys',keys.join(',')===EXPECTED_KEYS.join(','));
  ck('no-database-typo',!/Data\x20Base/.test(JSON.stringify(r)));
  var det=false;try{det=JSON.stringify(generate(seed,{},prng(seed)))===JSON.stringify(r);}catch(x){}
  ck('deterministic',det);
  var ec=CATS[seed%CATS.length],catOk=false;
  try{catOk=generate(seed,{category:ec},prng(seed)).category===ec;}catch(x){}
  ck('category-opt',catOk);
  ck('l1-findings',!isObj||r.level!==1||String(r.full_content).indexOf('Key findings')>=0);
  ck('l2-findings',!isObj||r.level!==2||String(r.full_content).indexOf('Projected findings')>=0);
  ck('sig-shape',isObj&&String(r.signature_link).indexOf('../')===0&&String(r.signature_link).indexOf('?sig=')>0);
  return out;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not-object']};
  if(!new RegExp('^'+escRe(PREFIX)+'\\d{7}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length||r.title.length>220)e.push('title');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===2&&!/^Level 2/.test(r.title||''))e.push('l2-title');
  if(typeof r.authors!=='string'||!r.authors.length)e.push('authors');
  if(typeof r.publication!=='string'||!r.publication.length)e.push('publication');
  if(!Number.isInteger(r.year))e.push('year');
  if(typeof r.full_content!=='string'||r.full_content.length<420||r.full_content.length>1500)e.push('full_content');
  if(typeof r.source_ref!=='string'||!r.source_ref.length)e.push('source_ref');
  if(!new RegExp('^'+escRe(SIGURL+SIGPREFIX)+'\\d{7}$').test(r.signature_link||''))e.push('signature_link');
  if(CATS.indexOf(r.category)<0)e.push('category');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){if(s&&s.id===rec.id)e.push('duplicate-id');});
  if(rec.level!==1&&rec.level!==2)e.push('level');
  return{ok:!e.length,errors:e};
}
/* 40 seeds x 40 invariant checks = 1600 assertions. */
function selfTest(){
  var errs=[],passed=0,total=0,perSeed={},nChecks=0;
  for(var s=1;s<=40;s++){
    var r=generate(s,{},prng(s));
    var list=checkList(r,s),okN=0;
    nChecks=list.length;
    for(var i=0;i<list.length;i++){
      total++;
      var e;
      try{e=list[i][1];}catch(x){e='threw:'+x.message;}
      if(e)errs.push('seed '+s+' ['+list[i][0]+'] '+e);
      else{passed++;okN++;}
    }
    perSeed[s]=okN+'/'+list.length;
  }
  return{seeds:40,checks:nChecks,total:total,passed:passed,failed:total-passed,errors:errs,perSeed:perSeed};
}
var gen={version:'jahdb-sports-study-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
