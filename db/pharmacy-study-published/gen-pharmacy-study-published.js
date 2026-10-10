/* SIGNATURE — JAH Pharmacy Published Archive Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic: seed + version always yields the same record. 1,000,000 address space.
   Level 1 = real published works (textbooks, landmark papers, curricula, standards).
   Level 2 = projection-based archive entries; every Level 2 title starts with "Level 2". */
(function(){'use strict';
var SLUG='pharmacy-study-published';
var BASE='pharmacy-study';
var PREFIX='JAH-pharmacy-study-published-P-';
var STUDYPREFIX='JAH-pharmacy-study-STUDY-S-';
var STUDYURL='../pharmacy-study-study/index.html?sig=';
var VERSION='jahdb-pharmacy-study-published-1.0';
var IDRE=new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$');
var SIGRE=new RegExp('^\\.\\./'+BASE+'-study/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{7}$');
var DATA={"cats":["pharmacology","clinical-pharmacy","pharmaceutics","medicinal-chemistry","pharmacognosy","pharmacy-law","pharmaceutical-care"],"real":[{"t":"Goodman & Gilman's The Pharmacological Basis of Therapeutics","a":"Brunton LL, Hilal-Dandan R, Knollmann BC (eds.)","pub":"McGraw-Hill","y":2023,"cat":"pharmacology","sum":"The definitive pharmacology text: drug mechanisms, therapeutics, and the scientific basis of prescribing. The fourteenth edition integrates precision medicine throughout.","key":["Receptor theory and pharmacodynamics","Pharmacokinetics principles","Drug class therapeutics"]},{"t":"Katzung's Basic & Clinical Pharmacology","a":"Vanderah TW (ed.)","pub":"McGraw-Hill","y":2024,"cat":"pharmacology","sum":"A clear, case-anchored pharmacology text pairing basic science with clinical application. Widely used in medical and pharmacy curricula. Case studies open each chapter with clinical context.","key":["Autonomic pharmacology","Cardiovascular and renal drugs","Antimicrobial chemotherapy"]},{"t":"Pharmacotherapy: A Pathophysiologic Approach","a":"DiPiro JT, Yee GC, Haines ST et al. (eds.)","pub":"McGraw-Hill","y":2020,"cat":"clinical-pharmacy","sum":"The clinical pharmacy reference organizing drug therapy by disease pathophysiology. Key chapters pair algorithms with evidence summaries. Online updates keep therapy recommendations current.","key":["Disease-based therapy algorithms","Key concept summaries","Patient care process"]},{"t":"ASHP Therapeutic Guidelines","a":"American Society of Health-System Pharmacists","pub":"ASHP","y":2023,"cat":"clinical-pharmacy","sum":"ASHP's therapeutic guidelines and statements on pharmacy practice, from antimicrobial stewardship to sterile compounding standards. Statements cover workforce wellbeing and medication safety culture.","key":["Therapeutic position statements","Stewardship guidance","Pharmacy practice standards"]},{"t":"Remington: The Science and Practice of Pharmacy","a":"Pharmaceutical Press","pub":"Pharmaceutical Press","y":2020,"cat":"pharmaceutics","sum":"The pharmacy profession's encyclopedic reference: pharmaceutics, manufacturing, and pharmacy practice across two volumes. The twenty-third edition reorganized content around patient care.","key":["Dosage form design science","Manufacturing and compounding","Biopharmaceutics and pharmacokinetics"]},{"t":"Pharmaceutics: The Science of Dosage Form Design","a":"Aulton ME, Taylor KM (eds.)","pub":"Elsevier","y":2021,"cat":"pharmaceutics","sum":"A student-friendly pharmaceutics text covering formulation science from preformulation through dosage form design and delivery. Worked examples teach calculation and formulation design.","key":["Preformulation studies","Solid and liquid dosage forms","Drug delivery systems"]},{"t":"Foye's Principles of Medicinal Chemistry","a":"Roche VF, Zito SW, Lemke TL, Williams DA (eds.)","pub":"Wolters Kluwer","y":2019,"cat":"medicinal-chemistry","sum":"The standard medicinal chemistry text linking chemical structure to drug action, metabolism, and design. Organized by therapeutic class. Chapters link drug classes to their molecular targets.","key":["Structure-activity relationships","Drug metabolism pathways","Drug design strategies"]},{"t":"The Organic Chemistry of Drug Design and Drug Action","a":"Silverman RB, Holladay MW","pub":"Elsevier","y":2014,"cat":"medicinal-chemistry","sum":"A mechanistic tour of drug design through organic chemistry: how drugs bind targets and how chemists optimize them. The third edition added biologics and fragment-based design.","key":["Drug-receptor interactions","Enzyme inhibitor design","Prodrug design strategies"]},{"t":"Pharmacognosy","a":"Heinrich M, Barnes J, Prieto JM et al.","pub":"CRC Press","y":2017,"cat":"pharmacognosy","sum":"A modern pharmacognosy text on natural product medicines: phytochemistry, quality, and evidence for herbal drugs. Regional chapters cover African, Asian, and European traditions. Safety sections address herb-drug interactions.","key":["Phytochemical classes","Quality and standardization","Evidence for herbal medicines"]},{"t":"Trease and Evans' Pharmacognosy","a":"Evans WC","pub":"Saunders/Elsevier","y":2009,"cat":"pharmacognosy","sum":"The classic pharmacognosy reference on crude drugs of plant and animal origin: identification, constituents, and uses. The sixteenth edition modernized phytochemical coverage. Monographs detail microscopy for identification.","key":["Crude drug identification","Active constituent chemistry","Traditional uses documentation"]},{"t":"Guide to Federal Pharmacy Law","a":"Reiss BS, Hall GD","pub":"Apothecary Press","y":2022,"cat":"pharmacy-law","sum":"A review of federal pharmacy law covering the FD&C Act, Controlled Substances Act, and HIPAA as tested on the MPJE. Practice questions mirror the MPJE format.","key":["Controlled Substances Act schedules","FD&C Act provisions explained","Pharmacy practice regulations"]},{"t":"United States Pharmacopeia-National Formulary","a":"United States Pharmacopeial Convention","pub":"USP","y":2023,"cat":"pharmacy-law","sum":"The official compendia of drug standards: identity, strength, quality, and purity requirements enforceable under US law. General chapters give enforceable test methods and procedures.","key":["Drug monograph standards","Compounding chapters 795 and 797","Reference standard program"]},{"t":"Pharmaceutical Care Practice","a":"Cipolle RJ, Strand LM, Morley PC","pub":"McGraw-Hill","y":2012,"cat":"pharmaceutical-care","sum":"The patient-centered pharmaceutical care model: identifying, resolving, and preventing drug therapy problems through structured practice. The third edition added outcomes and business planning chapters.","key":["Drug therapy problem categories","Patient care process","Documentation systems"]},{"t":"Martindale: The Complete Drug Reference","a":"Pharmaceutical Press","pub":"Pharmaceutical Press","y":2023,"cat":"pharmaceutical-care","sum":"The international drug reference: monographs on drugs worldwide with uses, doses, and adverse effects. The pharmacist's global desk reference. The forty-first edition covers over 6,000 drug monographs.","key":["International drug monographs","Dosing and adverse effects","Proprietary preparation index"]}],"first":["Amara","Darius","Priya","Kenji","Lucia","Omar","Sofia","Tariq","Nadia","Ellis","Mei","Ravi","Ingrid","Carlos","Aisha","Tomas","Yuki","Farah","Nolan","Zara"],"last":["Marsh","Okafor","Reyes","Tanaka","Novak","Haddad","Lindqvist","Moreau","Petrov","Nguyen","Silva","Khan","Osei","Berg","Costa","Weber","Ali","Frost","Nakamura","Diallo"],"l2angles":["Projected trial of","Forecast model for","Next-generation review of","Simulated outcomes in","Horizon scan of","Projected guideline for","Design study of","Long-range outlook on","Projected meta-analysis of","Future practice review of","Prototype framework for","Projected cohort study of"],"l2find":["a projected 18-24% improvement in primary outcomes versus current baselines","modelled cost reductions of 12-30% once the approach reaches scale","adherence gains projected at 15-22% under guided protocols","early simulations suggest recovery timelines shorter by 9-14 months","projected accuracy of 91-96% in independent validation cohorts","workflow time projected to fall 25-40% along the modelled pathway","patient-reported outcomes projected 20-28% above current standards","equity modelling projects roughly 30% wider access in underserved groups","safety modelling forecasts adverse events below 3% in target populations","projected training time for practitioners cut nearly in half","resource-use models show 20-35% lower demand on specialist time","long-term follow-up projections extend benefit durability past ten years","comparative models rank the approach first on benefit-to-burden ratio","sensitivity analysis holds the main finding across all tested assumptions","projected readmission or relapse rates 22-31% below current norms","early-adopter pilots in the model reach break-even within three years","standardisation projections cut unwarranted variation by about half","the model forecasts strong results across age bands and settings","projected documentation burden falls by roughly one third","forecasts show the approach remaining cost-effective under strict thresholds"],"l2abst":["This projected study examines {topic}. {f1}. {f2}. Prepared as a forward-looking archive entry for {y}, it describes a possible future rather than any real publication.","A forward-looking review of {topic}, projected for {y}. {f1}. {f2}. All figures here are modelled estimates, not measured results.","This horizon scan surveys {topic} and where current trajectories may lead by {y}. {f1}. {f2}. It is an archive projection, clearly separated from real published works.","Built as a planning reference for {y}, this projected analysis covers {topic}. {f1}. {f2}. Its figures are forecasts, and it has no real-world counterpart."],"l2topics":["pharmacist-led hypertension clinics","medication therapy management in polypharmacy","antimicrobial stewardship in hospitals","opioid stewardship programs","vaccine administration by pharmacists","pharmacogenomic-guided antidepressant selection","biosimilar substitution policies","compounding quality oversight","cold-chain logistics for biologics","adherence packaging interventions","deprescribing in older adults","anticoagulation clinic models","telepharmacy for rural hospitals","pharmacist prescribing pilots","medication reconciliation at discharge","high-alert medication safeguards","chemotherapy compounding robotics","radiopharmacy standards","cannabis-based medicine guidance","drug shortage mitigation strategies","falsified medicine detection","pharmacovigilance signal detection","real-world evidence in formularies","value-based pharmacy contracts","specialty pharmacy accreditation","medication access in disasters","pharmacy deserts mapping","technician role expansion","continuous manufacturing in pharma","green chemistry in drug synthesis","AI in drug discovery pipelines","mRNA platform manufacturing","personalized dosing algorithms","pediatric formulation development","geriatric dosing guidance","digital therapeutics formularies"],"l2journals":["JAH Projected Pharmaceutical Review","Journal of Future Pharmacy Science","Projected Pharmacology Quarterly","Annals of Pharmacy Foresight","Frontiers in Pharmaceutical Projection","JAH Pharmacy Futures"],"annotFocus":["clinical application","teaching use","research methods","historical context","patient communication","policy implications","interdisciplinary links","assessment design"],"readLevels":["undergraduate","postgraduate","practitioner","researcher","general reader"]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function cap1(s){return s.charAt(0).toUpperCase()+s.slice(1);}
var RKEYS=['id','t','title','authors','publication','year','category','level','full_content','source_ref','signature_link'];
var FACETS=[['record',''],['guide',' \u2014 Reading Guide'],['cite',' \u2014 Citation Map'],['curric',' \u2014 Curriculum Module']];
var FACET_LEAD={record:'',guide:'Reading guide for this work. ',cite:'Citation and influence map for this work. ',curric:'Curriculum module built from this work. '};
function sents(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>3;});}
function sigLink(seed){return STUDYURL+STUDYPREFIX+pad7(seed);}
function buildLevel1(rnd,seed,k){
  var pool=DATA.real;
  var w=pool[(k-1)%pool.length];
  var fx=FACETS[(((k-1)/pool.length)|0)%FACETS.length];
  var focus=pick(rnd,DATA.annotFocus), rl=pick(rnd,DATA.readLevels);
  var title=w.t+fx[1];
  return {id:PREFIX+pad7(seed),t:title,title:title,authors:w.a,publication:w.pub,year:w.y,category:w.cat,level:1,
    full_content:{abstract:FACET_LEAD[fx[0]]+w.sum,key_findings:w.key.slice(),archive_note:'Archive annotation (entry '+k+'): focus on '+focus+'; reading level '+rl+'; cross-filed under '+w.cat+'. Annotations are archive metadata; the work itself is the real publication cited above.'},
    source_ref:w.a+'. '+w.t+'. '+w.pub+'; '+w.y+'.',
    signature_link:sigLink(seed)};
}
function distinct3(rnd,a){
  var x=pick(rnd,a),y=pick(rnd,a),z=pick(rnd,a),guard=0;
  while((y===x||z===x||z===y)&&guard++<12){y=pick(rnd,a);z=pick(rnd,a);}
  return [x,y,z];
}
function buildLevel2(rnd,seed,cat){
  cat=cat||pick(rnd,DATA.cats);
  var topic=pick(rnd,DATA.l2topics), angle=pick(rnd,DATA.l2angles), y=ri(rnd,2027,2036);
  var f=distinct3(rnd,DATA.l2find);
  var f1=cap1(f[0]), f2=cap1(f[1]);
  var tmpl=pick(rnd,DATA.l2abst);
  var abstract=tmpl.split('{topic}').join(topic).split('{y}').join(String(y)).split('{f1}').join(f1).split('{f2}').join(f2);
  var title='Level 2: '+angle+' '+topic;
  var authors=pick(rnd,DATA.last)+' '+pick(rnd,DATA.first).charAt(0)+', '+pick(rnd,DATA.last)+' '+pick(rnd,DATA.first).charAt(0);
  return {id:PREFIX+pad7(seed),t:title,title:title,authors:authors,publication:pick(rnd,DATA.l2journals),year:y,category:cat,level:2,
    full_content:{abstract:abstract,key_findings:[cap1(f[0])+'.',cap1(f[1])+'.',cap1(f[2])+'.'],archive_note:'Projection generated by the JAH archive generator (seed '+seed+') \u2014 not a real publication and with no real-world counterpart.'},
    source_ref:'Signature projection archive \u2014 projected work; no real-world counterpart.',
    signature_link:sigLink(seed)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  seed=Math.floor(Number(seed)||1);
  var level=(seed%5===0)?1:2;
  var cat=opts.category||null;
  if(cat&&DATA.cats.indexOf(cat)<0)cat=null;
  if(level===1){var rec=buildLevel1(rnd,seed,Math.floor(seed/5));if(cat)rec.category=cat;return rec;}
  return buildLevel2(rnd,seed,cat);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<3||r.title.length>180)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(r.title!==String(r.title).trim())e.push('title-trim');
  if(typeof r.authors!=='string'||r.authors.length<3||/https?:\/\//.test(r.authors))e.push('authors');
  if(typeof r.publication!=='string'||r.publication.length<2)e.push('publication');
  if(!(r.year%1===0))e.push('year-int');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===1&&(r.year<1||r.year>2026))e.push('year-l1');
  if(r.level===2&&(r.year<2027||r.year>2036))e.push('year-l2');
  if(DATA.cats.indexOf(r.category)<0)e.push('category');
  if(r.level===2&&!/^Level 2/.test(r.title))e.push('l2-title');
  if(r.level===1&&/^Level 2/.test(r.title))e.push('l1-title');
  var fc=r.full_content;
  if(!fc||typeof fc!=='object'||Array.isArray(fc))e.push('full_content');
  else{
    if(Object.keys(fc).sort().join(',')!=='abstract,archive_note,key_findings')e.push('fc-keys');
    if(typeof fc.abstract!=='string'||fc.abstract.length<150)e.push('abstract-len');
    else if(sents(fc.abstract).length<2)e.push('abstract-sentences');
    if(!Array.isArray(fc.key_findings)||fc.key_findings.length<3)e.push('findings-count');
    else fc.key_findings.forEach(function(x){if(typeof x!=='string'||x.length<20)e.push('finding-len');});
    if(typeof fc.archive_note!=='string'||fc.archive_note.length<20)e.push('note');
    if(r.level===2&&!/projection/i.test(fc.archive_note))e.push('note-l2');
    if(r.level===1&&!/archive annotation/i.test(fc.archive_note))e.push('note-l1');
  }
  if(typeof r.source_ref!=='string'||r.source_ref.length<10||/https?:\/\//.test(r.source_ref))e.push('source_ref');
  if(r.level===2&&!/projection/i.test(r.source_ref))e.push('source-l2');
  if(r.level===1&&/projection/i.test(r.source_ref))e.push('source-l1');
  if(!SIGRE.test(r.signature_link||''))e.push('signature_link');
  if(Object.keys(r).sort().join(',')!==RKEYS.slice().sort().join(','))e.push('keys');
  var js=JSON.stringify(r);
  if(/Database/.test(js))e.push('database-two-words');
  if(/https?:\/\//.test(js))e.push('url-in-record');
  if(/<script/i.test(js))e.push('script-in-record');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];(sample||[]).forEach(function(s){
    if(s&&s.id===rec.id)e.push('duplicate id in archive sample');
    if(s&&s.t===rec.title)e.push('duplicate title in archive sample');});
  return {ok:!e.length,errors:e};
}
function selfTest(){
  var checks=[
   ['is-object',function(r){return (r&&typeof r==='object')?null:'not an object';}],
   ['id-format',function(r){return IDRE.test(r.id)?null:'bad id '+r.id;}],
   ['id-seed',function(r,c){return r.id===PREFIX+pad7(c.seed)?null:'id/seed mismatch';}],
   ['title-string',function(r){return (typeof r.title==='string'&&r.title.length>=3&&r.title.length<=180)?null:'bad title';}],
   ['t-equals-title',function(r){return r.t===r.title?null:'t!=title';}],
   ['title-trimmed',function(r){return r.title===r.title.trim()?null:'untrimmed title';}],
   ['level-value',function(r){return (r.level===1||r.level===2)?null:'bad level';}],
   ['level-formula',function(r,c){return r.level===((c.seed%5===0)?1:2)?null:'level/seed mismatch';}],
   ['l2-title-prefix',function(r){return r.level!==2||/^Level 2/.test(r.title)?null:'L2 missing prefix';}],
   ['l1-title-clean',function(r){return r.level!==1||!/^Level 2/.test(r.title)?null:'L1 has L2 prefix';}],
   ['authors',function(r){return (typeof r.authors==='string'&&r.authors.length>=3&&!/https?:\/\//.test(r.authors))?null:'bad authors';}],
   ['publication',function(r){return (typeof r.publication==='string'&&r.publication.length>=2)?null:'bad publication';}],
   ['year-int',function(r){return r.year%1===0?null:'year not int';}],
   ['year-range',function(r){return (r.level===1?(r.year>=1&&r.year<=2026):(r.year>=2027&&r.year<=2036))?null:'year out of range';}],
   ['category-valid',function(r){return DATA.cats.indexOf(r.category)>=0?null:'bad category';}],
   ['category-override',function(r,c){var q=generate(c.seed,{category:DATA.cats[0]},prng(c.seed));return q.category===DATA.cats[0]?null:'category opt ignored';}],
   ['fc-object',function(r){return (r.full_content&&typeof r.full_content==='object'&&!Array.isArray(r.full_content))?null:'bad full_content';}],
   ['fc-keys',function(r){return Object.keys(r.full_content).sort().join(',')==='abstract,archive_note,key_findings'?null:'bad fc keys';}],
   ['abstract-len',function(r){return r.full_content.abstract.length>=150?null:'abstract short';}],
   ['abstract-sentences',function(r){return sents(r.full_content.abstract).length>=2?null:'abstract <2 sentences';}],
   ['findings-count',function(r){return Array.isArray(r.full_content.key_findings)&&r.full_content.key_findings.length>=3?null:'findings<3';}],
   ['findings-len',function(r){return r.full_content.key_findings.every(function(x){return typeof x==='string'&&x.length>=20;})?null:'finding short';}],
   ['note-len',function(r){return r.full_content.archive_note.length>=20?null:'note short';}],
   ['note-l2',function(r){return r.level!==2||/projection/i.test(r.full_content.archive_note)?null:'L2 note missing projection';}],
   ['note-l1',function(r){return r.level!==1||/archive annotation/i.test(r.full_content.archive_note)?null:'L1 note missing annotation';}],
   ['source-string',function(r){return (typeof r.source_ref==='string'&&r.source_ref.length>=10&&!/https?:\/\//.test(r.source_ref))?null:'bad source_ref';}],
   ['source-l2',function(r){return r.level!==2||/projection/i.test(r.source_ref)?null:'L2 source missing projection';}],
   ['source-l1',function(r){return r.level!==1||!/projection/i.test(r.source_ref)?null:'L1 source mentions projection';}],
   ['siglink-format',function(r){return SIGRE.test(r.signature_link)?null:'bad signature_link';}],
   ['siglink-seed',function(r,c){return r.signature_link.slice(-(STUDYPREFIX.length+7))===STUDYPREFIX+pad7(c.seed)?null:'siglink/seed mismatch';}],
   ['no-database-two-words',function(r){return !/Database/.test(JSON.stringify(r))?null:'two-word Database found';}],
   ['no-url',function(r){return !/https?:\/\//.test(JSON.stringify(r))?null:'url in record';}],
   ['no-script',function(r){return !/<script/i.test(JSON.stringify(r))?null:'script in record';}],
   ['record-keys',function(r){return Object.keys(r).sort().join(',')===RKEYS.slice().sort().join(',')?null:'bad keys '+Object.keys(r).sort().join(',');}],
   ['determinism',function(r,c){var a=JSON.stringify(generate(c.seed,{},prng(c.seed)));var b=JSON.stringify(generate(c.seed,{},prng(c.seed)));return a===b?null:'nondeterministic';}],
   ['validate-ok',function(r){var v=validate(r);return v.ok?null:'validate: '+v.errors.join(',');}],
   ['drift-dup',function(r){return driftCheck(r,[{id:r.id,t:'other'}]).ok===false?null:'drift missed dup id';}],
   ['drift-clean',function(r){return driftCheck(r,[]).ok?null:'drift false positive';}],
   ['l1-real-work',function(r,c){if(r.level!==1)return null;var k=Math.floor(c.seed/5);var w=DATA.real[(k-1)%DATA.real.length];return (r.authors===w.a&&r.publication===w.pub&&r.year===w.y)?null:'L1 not mapped to real work';}],
   ['size-budget',function(r){var n=JSON.stringify(r).length;return (n>=400&&n<=2600)?null:'size '+n+' out of budget';}]
  ];
  var fails=[];
  for(var s=1;s<=40;s++){
    var rec=generate(s,{},prng(s));
    var ctx={seed:s};
    for(var i=0;i<checks.length;i++){
      var err=null;
      try{err=checks[i][1](rec,ctx);}catch(x){err='threw '+x.message;}
      if(err)fails.push('seed '+s+' ['+checks[i][0]+'] '+err);
    }
  }
  return {seeds:40,checksPerSeed:checks.length,total:40*checks.length,failed:fails.length,failures:fails.slice(0,25)};
}
var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest,prng:prng};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
