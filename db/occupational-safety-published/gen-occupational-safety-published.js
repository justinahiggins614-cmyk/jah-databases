(function(){'use strict';
/* JAH Occupational Health and Safety Published Archive Database — deterministic boundless generator (jahdb-occupational-safety-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='occupational-safety-published';
var PREFIX='JAH-occupational-safety-published-P-';
var SIGPREFIX='JAH-occupational-safety-STUDY-S-';
var SIGURL='../occupational-safety-study/index.html?sig=';
var CATS=["risk-assessment", "ppe", "ergonomics", "fire-safety", "incident-investigation", "health-surveillance"];
var WORKS=[{"c": ["risk-assessment", "ppe"], "t": "Occupational Safety and Health Standards (29 CFR 1910)", "a": "U.S. Occupational Safety and Health Administration", "p": "U.S. Government Publishing Office", "y": 2024, "s": "Code of Federal Regulations, revised annually", "k": "standard"}, {"c": ["risk-assessment"], "t": "Promotional Framework for Occupational Safety and Health (Convention 187)", "a": "International Labour Organization", "p": "International Labour Organization", "y": 2006, "s": "ILO Convention C187, adopted at the 95th International Labour Conference", "k": "convention"}, {"c": ["risk-assessment"], "t": "Fundamentals of Occupational Safety and Health", "a": "Mark A. Friend; James P. Kohn", "p": "Bernan Press", "y": 2010, "s": "5th edition, Bernan Press", "k": "textbook"}, {"c": ["incident-investigation"], "t": "Accident Prevention Manual: Administration & Programs", "a": "National Safety Council", "p": "National Safety Council", "y": 2009, "s": "13th edition", "k": "manual"}, {"c": ["risk-assessment"], "t": "Industrial Safety and Health Management", "a": "C. Ray Asfahl; David W. Rieske", "p": "Pearson", "y": 2009, "s": "6th edition, Pearson", "k": "textbook"}, {"c": ["fire-safety"], "t": "Fire Protection Handbook", "a": "National Fire Protection Association", "p": "NFPA", "y": 2008, "s": "20th edition, NFPA", "k": "handbook"}, {"c": ["ppe"], "t": "Quick Selection Guide to Chemical Protective Clothing", "a": "Krister Forsberg; S. Z. Mansdorf", "p": "John Wiley & Sons", "y": 2014, "s": "6th edition, Wiley", "k": "guide"}, {"c": ["ergonomics"], "t": "Ergonomics: How to Design for Ease and Efficiency", "a": "Karl H. E. Kroemer; Henrike B. Kroemer; Katrin E. Kroemer-Elbert", "p": "Pearson", "y": 2000, "s": "2nd edition, Pearson", "k": "textbook"}, {"c": ["health-surveillance"], "t": "Criteria for a Recommended Standard: Occupational Exposure to Heat and Hot Environments", "a": "National Institute for Occupational Safety and Health", "p": "NIOSH", "y": 2016, "s": "DHHS (NIOSH) Publication No. 2016-106", "k": "standard"}, {"c": ["incident-investigation"], "t": "Guidelines for Investigating Process Safety Incidents", "a": "Center for Chemical Process Safety", "p": "Wiley-AIChE", "y": 2003, "s": "2nd edition, CCPS", "k": "manual"}];
var LEADS=["This work is a standard reference for safety professionals.", "This publication defines the practice of occupational safety and health.", "This widely adopted text shapes workplace safety programs.", "This authoritative work links regulation to daily safety practice.", "This text anchors professional safety certification.", "This reference systematizes hazard control knowledge."];
var FOCUS=["hazard identification and risk assessment", "personal protective equipment programs", "ergonomic workplace design", "fire prevention and emergency response", "incident investigation and root cause analysis", "occupational health surveillance"];
var FINDINGS=["hierarchy-of-controls thinking eliminates hazards more reliably than PPE alone", "near-miss reporting systems surface risks before injuries occur", "ergonomic redesign cuts musculoskeletal disorders substantially", "permit-to-work systems reduce high-risk task incidents", "root-cause investigations prevent recurrence far better than blame", "health surveillance detects occupational disease at treatable stages", "contractor prequalification lifts safety performance across sites", "leadership safety walks strengthen culture measurably"];
var CHAPTERS=["Safety management systems", "Hazard identification and risk assessment", "The hierarchy of controls", "Personal protective equipment", "Ergonomics and human factors", "Fire safety and prevention", "Electrical and machine safety", "Chemical safety and exposure control", "Incident investigation", "Emergency preparedness"];
var AUDIENCES=["safety managers and officers", "operations supervisors", "HR and occupational health staff", "regulators and inspectors", "workers and safety representatives"];
var L2=[{"topic": "Wearable exposure monitoring", "horizon": "2028-2038"}, {"topic": "AI hazard vision systems", "horizon": "2029-2039"}, {"topic": "Exoskeletons for manual work", "horizon": "2031-2041"}, {"topic": "Digital-twin safety planning", "horizon": "2030-2040"}, {"topic": "Autonomous inspection drones", "horizon": "2032-2042"}, {"topic": "Predictive fatigue management", "horizon": "2027-2037"}, {"topic": "Immersive safety training", "horizon": "2026-2036"}, {"topic": "Zero-harm autonomous sites", "horizon": "2034-2044"}];
var L2ANGLES=["continuous risk sensing", "human-robot shared workspaces", "predictive incident prevention", "immersive competency assurance", "autonomous hazard response", "total worker health integration"];
var L2SCEN=["every worker carries continuous exposure monitoring", "cameras coach safe behavior privately and instantly", "heavy lifting is routinely assisted by exoskeletons", "high-risk jobs are rehearsed in digital twins first", "sites pause automatically when fatigue risk spikes", "regulators audit safety through live data feeds"];
var L2FIND=["wearables flag dangerous exposures before symptoms appear", "vision AI spots unsafe acts in real time", "exoskeletons cut lifting injuries substantially", "digital twins rehearse high-risk tasks safely", "fatigue models schedule rest before errors occur", "autonomous sites approach zero recordable incidents"];
var L2ROAD=["validation of predictive safety models", "worker-privacy frameworks for wearables", "exoskeleton ergonomic standards", "pilot zero-harm facilities", "AI oversight and accountability rules", "competency-based immersive curricula"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in occupational health and safety, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived occupational health and safety literature into '+pick(L2ANGLES,rnd)+'. '+
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
var gen={version:'jahdb-occupational-safety-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
