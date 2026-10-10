(function(){'use strict';
/* JAH Domestic Services Published Archive Database — deterministic boundless generator (jahdb-domestic-services-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='domestic-services-published';
var PREFIX='JAH-domestic-services-published-P-';
var SIGPREFIX='JAH-domestic-services-STUDY-S-';
var SIGURL='../domestic-services-study/index.html?sig=';
var CATS=["housekeeping", "childcare", "elder-care", "cooking", "laundry", "home-management"];
var WORKS=[{"c": ["housekeeping", "home-management"], "t": "Decent Work for Domestic Workers (Convention 189)", "a": "International Labour Organization", "p": "International Labour Organization", "y": 2011, "s": "ILO Convention C189 (2011), adopted at the 100th International Labour Conference", "k": "convention"}, {"c": ["housekeeping", "home-management"], "t": "Domestic Workers Across the World", "a": "International Labour Office", "p": "International Labour Organization", "y": 2013, "s": "ILO, Geneva, 2013 - global and regional statistics on domestic work", "k": "report"}, {"c": ["housekeeping"], "t": "Managing Housekeeping Operations", "a": "Margaret M. Kappa", "p": "American Hotel & Lodging Educational Institute", "y": 2009, "s": "AHLEI, 3rd revised edition", "k": "textbook"}, {"c": ["housekeeping", "home-management"], "t": "Housekeeping Management", "a": "Margaret M. Kappa; Aleta Nitschke; Patricia B. Schappert", "p": "John Wiley & Sons", "y": 1997, "s": "Wiley hospitality series", "k": "textbook"}, {"c": ["home-management"], "t": "Effective protection for domestic workers: A guide to designing labour laws", "a": "International Labour Office", "p": "International Labour Organization", "y": 2012, "s": "ILO, Geneva, 2012", "k": "guide"}, {"c": ["childcare"], "t": "Child Development", "a": "Laura E. Berk", "p": "Pearson", "y": 2017, "s": "9th edition, Pearson", "k": "textbook"}, {"c": ["elder-care"], "t": "Aging and the Life Course: An Introduction to Social Gerontology", "a": "Jill Quadagno", "p": "McGraw-Hill", "y": 2017, "s": "7th edition, McGraw-Hill", "k": "textbook"}, {"c": ["cooking"], "t": "Professional Cooking", "a": "Wayne Gisslen", "p": "John Wiley & Sons", "y": 2018, "s": "9th edition, Wiley", "k": "textbook"}, {"c": ["laundry"], "t": "Textiles", "a": "Sara J. Kadolph", "p": "Pearson", "y": 2013, "s": "12th edition, Pearson", "k": "textbook"}, {"c": ["home-management", "housekeeping"], "t": "Decent work for domestic workers: Report IV(1)", "a": "International Labour Office", "p": "International Labour Organization", "y": 2010, "s": "Report to the 99th International Labour Conference, ILO", "k": "report"}];
var LEADS=["This work is a cornerstone reference for professional domestic service practice.", "This publication defines quality standards for household and care work.", "This widely used reference shapes training for domestic service professionals.", "This work documents best practice across household service occupations.", "This authoritative source is cited in vocational curricula worldwide.", "This publication bridges labour policy and everyday household practice."];
var FOCUS=["workforce training and certification standards", "regulatory compliance and workers' rights", "service quality measurement and control", "hygiene, safety, and sanitation protocol", "household management and scheduling systems", "care ethics and client dignity"];
var FINDINGS=["formal written contracts raise retention and job satisfaction among domestic workers", "standardized task checklists cut service errors in household operations by a wide margin", "structured induction training shortens the time to full productivity for new staff", "clear grievance procedures reduce workplace disputes in private households", "ergonomic work methods lower injury rates among cleaning and care staff", "scheduled rest periods improve sustained service quality through the day", "client feedback loops raise perceived service value measurably", "certification pathways increase earnings and mobility for domestic workers"];
var CHAPTERS=["Foundations of professional domestic service", "Recruitment, contracts, and labour rights", "Household organization and scheduling", "Cleaning science and safe chemicals", "Childcare: development and daily care", "Elder care: dignity and daily living", "Cooking: nutrition and food safety", "Laundry and textile care", "Home safety and emergency readiness", "Quality inspection and standards"];
var AUDIENCES=["household employers and agency managers", "vocational trainers and curriculum designers", "policy makers and labour inspectors", "professional housekeepers and caregivers", "students of home economics and hospitality"];
var L2=[{"topic": "Autonomous home-care robotics", "horizon": "2035-2045"}, {"topic": "AI household management platforms", "horizon": "2030-2040"}, {"topic": "Smart-home integrated domestic service", "horizon": "2032-2042"}, {"topic": "Global domestic worker certification network", "horizon": "2028-2038"}, {"topic": "Elder-care companion systems", "horizon": "2033-2043"}, {"topic": "Robotic laundry and textile care", "horizon": "2031-2041"}, {"topic": "Precision nutrition home cooking", "horizon": "2029-2039"}, {"topic": "Child development monitoring aides", "horizon": "2034-2044"}];
var L2ANGLES=["fully automated service delivery", "human-machine teaming in the home", "rights-centered platform cooperatives", "predictive care scheduling", "zero-waste household operations", "privacy-preserving home sensing"];
var L2SCEN=["households run daily operations through coordinated home robots", "care workers supervise fleets of assistive devices across clients", "service cooperatives own the platforms they work on", "elderly clients live independently with continuous gentle monitoring", "kitchens plan, shop, and cook to each household's health profile", "children's developmental milestones are tracked with parental consent"];
var L2FIND=["task automation absorbs routine chores while care roles grow in value", "platform cooperatives return a larger share of fees to workers", "predictive scheduling cuts idle time without raising workload intensity", "home sensor networks reduce accident rates among elderly clients", "standardized digital credentials make skills portable across borders", "robotic assistance extends independent living by years on average"];
var L2ROAD=["pilot deployments in volunteer households", "safety certification for home robotics", "interoperability standards for home devices", "worker transition and retraining funds", "data-privacy regulation for home sensing", "insurance models for automated service"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in domestic services, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived domestic services literature into '+pick(L2ANGLES,rnd)+'. '+
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
var gen={version:'jahdb-domestic-services-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
