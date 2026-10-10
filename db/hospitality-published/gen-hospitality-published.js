(function(){'use strict';
/* JAH Hotel, Restaurants and Catering Published Archive Database — deterministic boundless generator (jahdb-hospitality-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='hospitality-published';
var PREFIX='JAH-hospitality-published-P-';
var SIGPREFIX='JAH-hospitality-STUDY-S-';
var SIGURL='../hospitality-study/index.html?sig=';
var CATS=["hotels", "restaurants", "catering", "front-office", "food-beverage", "service-management"];
var WORKS=[{"c": ["hotels", "restaurants"], "t": "Introduction to Hospitality", "a": "John R. Walker", "p": "Pearson", "y": 2021, "s": "9th edition, Pearson", "k": "textbook"}, {"c": ["front-office", "hotels"], "t": "Managing Front Office Operations", "a": "Michael L. Kasavana", "p": "American Hotel & Lodging Educational Institute", "y": 2017, "s": "10th edition, AHLEI", "k": "textbook"}, {"c": ["hotels"], "t": "Hotel Housekeeping: Operations and Management", "a": "G. Raghubalan; Smritee Raghubalan", "p": "Oxford University Press", "y": 2015, "s": "3rd edition, Oxford University Press", "k": "textbook"}, {"c": ["hotels", "restaurants"], "t": "Hospitality Marketing Management", "a": "Robert D. Reid; David C. Bojanic", "p": "John Wiley & Sons", "y": 2009, "s": "5th edition, Wiley", "k": "textbook"}, {"c": ["hotels", "service-management"], "t": "Introduction to Hospitality Management", "a": "John R. Walker; Josielyn T. Walker", "p": "Pearson", "y": 2020, "s": "5th edition, Pearson", "k": "textbook"}, {"c": ["service-management"], "t": "Managing Hospitality Human Resources", "a": "Robert H. Woods; Jack D. Ninemeier", "p": "American Hotel & Lodging Educational Institute", "y": 2012, "s": "5th edition, AHLEI", "k": "textbook"}, {"c": ["hotels", "restaurants"], "t": "Cornell Hospitality Quarterly", "a": "Cornell University School of Hotel Administration (editorial board)", "p": "SAGE Publishing", "y": 2020, "s": "peer-reviewed journal, volume 61", "k": "journal"}, {"c": ["food-beverage", "restaurants"], "t": "Food and Beverage Management", "a": "Bernard Davis; Andrew Lockwood; Peter Alcott; Ioannis S. Pantelidis", "p": "Routledge", "y": 2018, "s": "6th edition, Routledge", "k": "textbook"}, {"c": ["restaurants"], "t": "Restaurant Success by the Numbers", "a": "Roger Fields", "p": "Ten Speed Press", "y": 2014, "s": "2nd edition, Ten Speed Press", "k": "handbook"}, {"c": ["food-beverage", "catering"], "t": "On Food and Cooking: The Science and Lore of the Kitchen", "a": "Harold McGee", "p": "Scribner", "y": 2004, "s": "revised edition, Scribner", "k": "reference"}];
var LEADS=["This work is a core text in hospitality management education.", "This publication defines professional standards for guest service.", "This widely used reference shapes hotel and restaurant operations.", "This authoritative work links service theory to daily operations.", "This text is standard in hospitality degree programs worldwide.", "This reference systematizes the management of guest experiences."];
var FOCUS=["front-office operations and revenue management", "food and beverage service excellence", "housekeeping operations and quality control", "guest relations and complaint resolution", "hospitality human resources and training", "catering logistics and event execution"];
var FINDINGS=["empowered front-line staff resolve complaints faster and retain more guests", "standard operating procedures cut service variability across shifts", "revenue management systems lift occupancy-adjusted yields measurably", "preventive maintenance reduces guest-facing defects and compensation costs", "structured onboarding halves time-to-competence for new hires", "menu engineering raises contribution margins without hurting satisfaction", "housekeeping inspection scores predict online review ratings", "event run-sheets eliminate most day-of coordination failures"];
var CHAPTERS=["The hospitality industry landscape", "Front-office operations", "Reservations and revenue management", "Housekeeping operations", "Food and beverage service", "Catering and banquet operations", "Guest relations and service recovery", "Hospitality marketing and sales", "Human resources and training", "Financial control in hospitality"];
var AUDIENCES=["hotel and restaurant managers", "hospitality students and educators", "catering and event professionals", "owners and investors", "front-line service staff"];
var L2=[{"topic": "Autonomous hotel operations", "horizon": "2032-2042"}, {"topic": "AI concierge ecosystems", "horizon": "2028-2038"}, {"topic": "Robotic kitchen brigades", "horizon": "2031-2041"}, {"topic": "Hyper-personalized guest journeys", "horizon": "2029-2039"}, {"topic": "Zero-waste catering systems", "horizon": "2027-2037"}, {"topic": "Immersive pre-arrival experiences", "horizon": "2030-2040"}, {"topic": "Dynamic workforce platforms", "horizon": "2026-2036"}, {"topic": "Climate-resilient resorts", "horizon": "2033-2043"}];
var L2ANGLES=["fully orchestrated guest experiences", "human-robot service teaming", "predictive demand management", "circular hospitality operations", "emotionally intelligent service AI", "decentralized hospitality workforces"];
var L2SCEN=["guests move through hotels with near-invisible automated support", "AI concierges coordinate entire stays across partner venues", "kitchens run hybrid human-robot brigades at scale", "catering operations achieve verified zero waste", "remote teams staff front desks across time zones", "resorts adapt operations to extreme weather in real time"];
var L2FIND=["automation absorbs back-of-house tasks while hosts focus on guests", "personalization engines raise repeat-visit rates substantially", "predictive staffing matches labour to demand curves precisely", "waste-tracking systems cut food waste dramatically", "dynamic pricing balances occupancy and rate integrity", "robotic delivery proves reliable for room-service operations"];
var L2ROAD=["pilot smart-hotels in gateway cities", "service-robot safety certification", "guest-data privacy frameworks", "workforce transition programs", "interoperability standards for property systems", "sustainability reporting mandates"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in hotels, restaurants and catering, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived hotels, restaurants and catering literature into '+pick(L2ANGLES,rnd)+'. '+
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
var gen={version:'jahdb-hospitality-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
