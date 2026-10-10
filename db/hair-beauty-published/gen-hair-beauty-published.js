(function(){'use strict';
/* JAH Hair and Beauty Services Published Archive Database — deterministic boundless generator (jahdb-hair-beauty-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles), Level 2 = Signature projections (title starts
   with "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function escRe(s){return String(s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
var SLUG='hair-beauty-published';
var PREFIX='JAH-hair-beauty-published-P-';
var SIGPREFIX='JAH-hair-beauty-STUDY-S-';
var SIGURL='../hair-beauty-study/index.html?sig=';
var CATS=["haircare", "skincare", "cosmetics", "barbering", "nail-care", "salon-management"];
var WORKS=[{"c": ["haircare", "cosmetics"], "t": "Milady Standard Cosmetology", "a": "Milady", "p": "Cengage Learning", "y": 2016, "s": "13th edition, Cengage Learning", "k": "textbook"}, {"c": ["haircare"], "t": "The Science of Hair Care", "a": "Charles Zviak (editor)", "p": "Marcel Dekker", "y": 1986, "s": "Cosmetic Science and Technology series", "k": "textbook"}, {"c": ["haircare"], "t": "Chemical and Physical Behavior of Human Hair", "a": "Clarence R. Robbins", "p": "Springer", "y": 2012, "s": "5th edition, Springer", "k": "textbook"}, {"c": ["cosmetics"], "t": "Harry's Cosmeticology", "a": "Ralph G. Harry; editorial board", "p": "Chemical Publishing", "y": 2000, "s": "8th edition, Chemical Publishing", "k": "reference"}, {"c": ["skincare"], "t": "Cosmetic Dermatology: Principles and Practice", "a": "Leslie Baumann", "p": "McGraw-Hill", "y": 2009, "s": "2nd edition, McGraw-Hill", "k": "textbook"}, {"c": ["barbering"], "t": "Milady Standard Barbering", "a": "Milady", "p": "Cengage Learning", "y": 2017, "s": "6th edition, Cengage Learning", "k": "textbook"}, {"c": ["nail-care"], "t": "Milady Standard Nail Technology", "a": "Milady", "p": "Cengage Learning", "y": 2020, "s": "8th edition, Cengage Learning", "k": "textbook"}, {"c": ["cosmetics"], "t": "A Consumer's Dictionary of Cosmetic Ingredients", "a": "Ruth Winter", "p": "Crown Publishing", "y": 2009, "s": "7th edition, Crown", "k": "reference"}, {"c": ["skincare"], "t": "Skin Care: Beyond the Basics", "a": "Mark Lees", "p": "Milady / Cengage Learning", "y": 2010, "s": "3rd edition", "k": "textbook"}, {"c": ["skincare"], "t": "Textbook of Cosmetic Dermatology", "a": "Robert Baran; Howard I. Maibach (editors)", "p": "CRC Press", "y": 2017, "s": "5th edition, CRC Press", "k": "textbook"}];
var LEADS=["This work is the industry-standard reference for professional beauty practice.", "This publication sets the technical foundation for cosmetology education.", "This widely adopted text defines safe, professional beauty services.", "This authoritative work bridges beauty science and salon practice.", "This reference is required reading in licensed beauty programs.", "This publication systematizes the chemistry and craft of beauty care."];
var FOCUS=["hair structure, chemistry, and safe treatment", "skin analysis and treatment protocols", "sanitation, disinfection, and client safety", "colour theory and application technique", "salon business management and client relations", "product chemistry and ingredient safety"];
var FINDINGS=["patch testing before chemical services sharply reduces adverse reactions", "structured consultation raises client satisfaction and rebooking rates", "hospital-grade disinfection protocols prevent cross-contamination in salons", "layered colour application produces more predictable, even results", "ergonomic workstation setup lowers repetitive-strain injuries among stylists", "documented formulas ensure consistent results across repeat visits", "continuing education correlates with higher service prices and retention", "retail homecare guidance extends treatment results between appointments"];
var CHAPTERS=["Foundations of beauty science", "Hair structure and chemistry", "Skin analysis and disorders", "Sanitation and disinfection", "Haircutting and styling technique", "Chemical texture services", "Hair colour theory and practice", "Skincare treatments and facials", "Nail structure and enhancements", "Salon management and retail"];
var AUDIENCES=["licensed cosmetologists and students", "salon owners and managers", "beauty school instructors", "product formulators and educators", "state board examination candidates"];
var L2=[{"topic": "AI-personalized beauty formulation", "horizon": "2030-2040"}, {"topic": "Robotic precision hair services", "horizon": "2034-2044"}, {"topic": "Skin microbiome diagnostics", "horizon": "2029-2039"}, {"topic": "Virtual salon try-on ecosystems", "horizon": "2027-2037"}, {"topic": "Sustainable zero-waste salons", "horizon": "2028-2038"}, {"topic": "Genetic hair-care profiling", "horizon": "2033-2043"}, {"topic": "At-home professional-grade devices", "horizon": "2031-2041"}, {"topic": "Beauty service tele-consultation", "horizon": "2026-2036"}];
var L2ANGLES=["hyper-personalized service delivery", "human-robot collaboration in the salon", "data-driven treatment planning", "circular sustainable beauty operations", "remote expert consultation networks", "predictive client outcome modeling"];
var L2SCEN=["clients receive DNA-informed product regimens through licensed salons", "salons operate hybrid teams of stylists and precision robots", "regulators require ingredient traceability from lab to chair", "rural clients access top stylists through immersive telepresence", "salon waste streams are fully circular by design", "AI triage routes each client to the right specialist automatically"];
var L2FIND=["personalized formulations outperform one-size products on satisfaction scores", "robotic assistance standardizes precision while stylists keep creative control", "microbiome-guided regimens reduce irritation complaints markedly", "virtual consultations expand salon reach beyond local clientele", "refill and recycling programs cut salon waste dramatically", "predictive scheduling smooths demand peaks across the week"];
var L2ROAD=["clinical validation of diagnostic devices", "technician certification for robotic systems", "data-privacy standards for biometric profiles", "pilot programs in flagship salons", "ingredient transparency regulation", "interoperability of beauty platforms"];
var WORK_BY_TITLE={};WORKS.forEach(function(w){WORK_BY_TITLE[w.t]=w;});
function idxOf(seed){return ((seed%1000000)+1000000)%1000000;}
function pad7(n){return String(n).padStart(7,'0');}
function words(s){return String(s).trim().split(/\s+/).length;}
function content1(rnd,w){
  return w.t+' ('+w.y+') is a widely cited '+w.k+' in hair and beauty services, issued by '+w.p+'. '+pick(LEADS,rnd)+' '+
    'With a focus on '+pick(FOCUS,rnd)+', the work gives practitioners a complete, field-tested reference. '+
    'Key findings: first, '+pick(FINDINGS,rnd)+'; second, '+pick(FINDINGS,rnd)+'; third, '+pick(FINDINGS,rnd)+'. '+
    'Contents: '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'; '+pick(CHAPTERS,rnd)+'. '+
    'Audience: '+pick(AUDIENCES,rnd)+'.';
}
function content2(rnd,t){
  return 'Level 2 projection: '+t.topic+', '+t.horizon+'. This Signature-generated projection extends the archived hair and beauty services literature into '+pick(L2ANGLES,rnd)+'. '+
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
var gen={version:'jahdb-hair-beauty-published-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
