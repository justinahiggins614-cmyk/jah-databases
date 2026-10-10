(function(){'use strict';
/* JAH Military and Defence Published Archive Database — deterministic boundless generator (jahdb-military-defence-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='military-defence-published';
var PREFIX='JAH-military-defence-published-P-';
var SIGPREFIX='JAH-military-defence-STUDY-S-';
var SIGURL='../military-defence-study/index.html?sig=';
var CATS=["strategy", "logistics", "training", "engineering", "intelligence", "veterans-affairs"];
var WORKS=[{"c": ["strategy"], "t": "On War", "a": "Carl von Clausewitz; Michael Howard and Peter Paret (translators/editors)", "p": "Princeton University Press", "y": 1989, "s": "Howard/Paret translation; original 1832", "k": "classic"}, {"c": ["strategy"], "t": "The Art of War", "a": "Sun Tzu; Lionel Giles (translator)", "p": "Luzac & Co.", "y": 1910, "s": "Giles translation; original 5th century BC", "k": "classic"}, {"c": ["strategy", "training"], "t": "FM 3-0: Operations", "a": "Headquarters, Department of the Army", "p": "U.S. Army", "y": 2022, "s": "Field Manual 3-0", "k": "field manual"}, {"c": ["strategy"], "t": "Joint Publication 1: Doctrine for the Armed Forces of the United States", "a": "Joint Chiefs of Staff", "p": "U.S. Department of Defense", "y": 2020, "s": "JP 1, change 1 (2020)", "k": "doctrine"}, {"c": ["logistics"], "t": "Supplying War: Logistics from Wallenstein to Patton", "a": "Martin van Creveld", "p": "Cambridge University Press", "y": 1977, "s": "1st edition, Cambridge", "k": "book"}, {"c": ["strategy"], "t": "Strategy", "a": "B. H. Liddell Hart", "p": "Faber & Faber", "y": 1967, "s": "2nd revised edition", "k": "book"}, {"c": ["intelligence"], "t": "Intelligence in War: Knowledge of the Enemy from Napoleon to Al-Qaeda", "a": "John Keegan", "p": "Alfred A. Knopf", "y": 2003, "s": "1st edition, Knopf", "k": "book"}, {"c": ["training"], "t": "FM 7-0: Training", "a": "Headquarters, Department of the Army", "p": "U.S. Army", "y": 2021, "s": "Field Manual 7-0", "k": "field manual"}, {"c": ["engineering"], "t": "FM 3-34: Engineer Operations", "a": "Headquarters, Department of the Army", "p": "U.S. Army", "y": 2020, "s": "Field Manual 3-34", "k": "field manual"}, {"c": ["strategy", "veterans-affairs"], "t": "The Face of Battle", "a": "John Keegan", "p": "Viking Press", "y": 1976, "s": "1st edition, Viking", "k": "book"}];
var LEADS=["This work is a classic in military thought and doctrine.", "This publication shapes how armed forces organize and fight.", "This widely studied text defines the profession of arms.", "This authoritative work links strategy to operations.", "This text anchors professional military education.", "This reference systematizes the art and science of warfare."];
var FOCUS=["strategy and operational art", "military logistics and sustainment", "training and readiness systems", "military engineering operations", "intelligence and decision-making", "veterans' transition and care"];
var FINDINGS=["logistics determines operational reach more than firepower alone", "mission command outperforms detailed control in fluid operations", "realistic collective training is the strongest predictor of unit performance", "engineer preparation of the battlespace multiplies maneuver options", "intelligence fused at the lowest level accelerates decisions", "after-action review discipline compounds institutional learning", "sustainment planning must precede maneuver planning", "veteran support programs improve long-term transition outcomes"];
var CHAPTERS=["The nature of war", "Strategy and policy", "Operational art and design", "Command and mission command", "Intelligence preparation", "Logistics and sustainment", "Engineer operations", "Training and readiness", "Joint and combined operations", "Veterans and military families"];
var AUDIENCES=["officers and staff colleges", "defense analysts and scholars", "policymakers and legislators", "veterans' service organizations", "students of strategic studies"];
var L2=[{"topic": "Autonomous logistics convoys", "horizon": "2030-2040"}, {"topic": "AI-assisted operational planning", "horizon": "2028-2038"}, {"topic": "Human-machine combat teaming", "horizon": "2032-2042"}, {"topic": "Resilient mesh communications", "horizon": "2029-2039"}, {"topic": "Predictive maintenance fleets", "horizon": "2031-2041"}, {"topic": "Immersive collective training", "horizon": "2027-2037"}, {"topic": "Quantum-secure command networks", "horizon": "2034-2044"}, {"topic": "Veteran transition platforms", "horizon": "2026-2036"}];
var L2ANGLES=["human-machine integrated forces", "decision advantage at machine speed", "resilient contested logistics", "continuous adaptive training", "assured command and control", "whole-of-life service support"];
var L2SCEN=["sustainment flows through autonomous corridors", "commanders decide with AI-generated options in minutes", "formations operate as integrated human-machine teams", "training never stops through persistent virtual environments", "veterans transition through unified digital platforms", "allied forces share a common operational picture"];
var L2FIND=["autonomous convoys sustain forces under contested conditions", "AI planning compresses course-of-action development dramatically", "teamed systems extend the reach of smaller formations", "mesh networks maintain command through disruption", "predictive maintenance raises fleet availability substantially", "immersive training delivers repetitions impossible in live exercises"];
var L2ROAD=["doctrine for human-machine teaming", "testing under contested conditions", "interoperability across allied systems", "ethical frameworks for autonomous functions", "workforce reskilling for AI-enabled roles", "veteran data-portability standards"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in military and defence, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived military and defence literature into '+pick(L2ANGLES,rnd)+'. '+
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
var gen={version:'jahdb-military-defence-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
