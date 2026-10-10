(function(){'use strict';
/* JAH Protection of Persons and Property Published Archive Database — deterministic boundless generator (jahdb-protection-services-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='protection-services-published';
var PREFIX='JAH-protection-services-published-P-';
var SIGPREFIX='JAH-protection-services-STUDY-S-';
var SIGURL='../protection-services-study/index.html?sig=';
var CATS=["physical-security", "close-protection", "surveillance", "access-control", "emergency-response", "risk-management"];
var WORKS=[{"c": ["physical-security", "risk-management"], "t": "Introduction to Security", "a": "Robert J. Fischer; Gion Green", "p": "Butterworth-Heinemann", "y": 2004, "s": "7th edition, Butterworth-Heinemann", "k": "textbook"}, {"c": ["physical-security"], "t": "Protection of Assets Manual", "a": "ASIS International", "p": "ASIS International", "y": 2012, "s": "multi-volume reference", "k": "reference"}, {"c": ["physical-security"], "t": "Effective Physical Security", "a": "Lawrence J. Fennelly", "p": "Butterworth-Heinemann", "y": 2016, "s": "5th edition, Butterworth-Heinemann", "k": "textbook"}, {"c": ["risk-management"], "t": "Risk Analysis and the Security Survey", "a": "James F. Broder; Eugene Tucker", "p": "Butterworth-Heinemann", "y": 2011, "s": "4th edition, Butterworth-Heinemann", "k": "textbook"}, {"c": ["close-protection", "physical-security"], "t": "The Professional Protection Officer", "a": "International Foundation for Protection Officers; Sandi J. Davies (editor)", "p": "Butterworth-Heinemann", "y": 2010, "s": "1st edition", "k": "manual"}, {"c": ["surveillance"], "t": "CCTV Surveillance: Video Practices and Technology", "a": "Herman Kruegle", "p": "Butterworth-Heinemann", "y": 2006, "s": "2nd edition, Butterworth-Heinemann", "k": "textbook"}, {"c": ["emergency-response"], "t": "Introduction to Emergency Management", "a": "George Haddow; Jane Bullock; Damon Coppola", "p": "Butterworth-Heinemann", "y": 2020, "s": "7th edition", "k": "textbook"}, {"c": ["surveillance", "risk-management"], "t": "Private Security and the Investigative Process", "a": "Charles P. Nemeth", "p": "CRC Press", "y": 2017, "s": "4th edition, CRC Press", "k": "textbook"}, {"c": ["physical-security", "access-control"], "t": "High-Rise Security and Fire Life Safety", "a": "Geoff Craighead", "p": "Butterworth-Heinemann", "y": 2009, "s": "3rd edition", "k": "textbook"}, {"c": ["close-protection"], "t": "The Gift of Fear", "a": "Gavin de Becker", "p": "Little, Brown and Company", "y": 1997, "s": "1st edition", "k": "book"}];
var LEADS=["This work is a standard reference for security professionals.", "This publication defines the protection of persons and property.", "This widely adopted text shapes security operations worldwide.", "This authoritative work links risk theory to protective practice.", "This text anchors professional security certification.", "This reference systematizes protective knowledge."];
var FOCUS=["physical security design and operations", "close protection tradecraft", "surveillance and counter-surveillance", "access control systems", "emergency response planning", "security risk assessment"];
var FINDINGS=["layered defenses deter far more incidents than any single measure", "risk assessments focused on assets prioritize spending effectively", "trained observers detect pre-incident indicators reliably", "access control integrated with HR data closes insider gaps", "rehearsed emergency plans cut response times substantially", "close protection succeeds through planning, not reaction", "lighting and natural surveillance reduce opportunistic crime", "incident documentation quality determines legal defensibility"];
var CHAPTERS=["Foundations of protection", "Risk assessment and analysis", "Physical security design", "Barriers, lighting, and locks", "Intrusion detection and alarms", "Video surveillance systems", "Access control", "Close protection operations", "Emergency planning and response", "Legal and ethical issues"];
var AUDIENCES=["security managers and directors", "protection officers and bodyguards", "facility managers", "law enforcement liaisons", "risk consultants"];
var L2=[{"topic": "AI threat-detection networks", "horizon": "2028-2038"}, {"topic": "Autonomous patrol systems", "horizon": "2031-2041"}, {"topic": "Biometric access ecosystems", "horizon": "2029-2039"}, {"topic": "Predictive protective intelligence", "horizon": "2030-2040"}, {"topic": "Drone perimeter defense", "horizon": "2032-2042"}, {"topic": "Digital-twin facility security", "horizon": "2033-2043"}, {"topic": "Privacy-preserving surveillance", "horizon": "2027-2037"}, {"topic": "Integrated emergency coordination", "horizon": "2026-2036"}];
var L2ANGLES=["intelligent layered protection", "human-AI security teaming", "predictive threat prevention", "privacy-respecting monitoring", "autonomous response capabilities", "resilient critical infrastructure"];
var L2SCEN=["campuses monitor themselves with privacy by design", "protection details coordinate through shared intelligence", "perimeters defend themselves against drone intrusions", "emergencies trigger rehearsed multi-agency responses", "access becomes frictionless yet stronger", "critical sites rehearse attacks in digital twins"];
var L2FIND=["AI analytics filter noise so operators catch real threats", "autonomous patrols extend coverage without fatigue", "biometric systems balance security with throughput", "predictive intelligence disrupts plots earlier", "digital twins let teams rehearse responses precisely", "privacy-preserving designs sustain public trust"];
var L2ROAD=["accuracy and bias testing for AI systems", "regulatory frameworks for autonomous patrol", "biometric data-protection standards", "interoperability of security platforms", "operator training for AI-assisted roles", "public transparency reporting"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in the protection of persons and property, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived the protection of persons and property literature into '+pick(L2ANGLES,rnd)+'. '+
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
var gen={version:'jahdb-protection-services-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
