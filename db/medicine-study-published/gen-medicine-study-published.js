/* SIGNATURE — JAH Medicine Published Archive Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic: seed + version always yields the same record. 1,000,000 address space.
   Level 1 = real published works (textbooks, landmark papers, curricula, standards).
   Level 2 = projection-based archive entries; every Level 2 title starts with "Level 2". */
(function(){'use strict';
var SLUG='medicine-study-published';
var BASE='medicine-study';
var PREFIX='JAH-medicine-study-published-P-';
var STUDYPREFIX='JAH-medicine-study-STUDY-S-';
var STUDYURL='../medicine-study-study/index.html?sig=';
var VERSION='jahdb-medicine-study-published-1.0';
var IDRE=new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$');
var SIGRE=new RegExp('^\\.\\./'+BASE+'-study/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{7}$');
var DATA={"cats":["cardiology","neurology","oncology","infectious-disease","pediatrics","surgery","psychiatry"],"real":[{"t":"Braunwald's Heart Disease","a":"Libby P, Bonow RO, Mann DL, Tomaselli GF (eds.)","pub":"Elsevier","y":2021,"cat":"cardiology","sum":"The reference text of cardiology, covering cardiovascular biology, imaging, coronary disease, heart failure, and electrophysiology. Each edition integrates landmark trial evidence into practice guidance.","key":["Coronary artery disease: diagnosis and revascularization","Heart failure pathophysiology and device therapy","Preventive cardiology and risk stratification"]},{"t":"A Randomized Trial of Intensive versus Standard Blood-Pressure Control","a":"SPRINT Research Group","pub":"New England Journal of Medicine","y":2015,"cat":"cardiology","sum":"A randomized trial of intensive versus standard blood-pressure control in high-risk hypertensive patients. Targeting systolic pressure below 120 mm Hg lowered cardiovascular events and mortality.","key":["Intensive control reduced composite cardiovascular events","All-cause mortality lower with intensive targets","Risk-benefit framing for hypertension guidelines"]},{"t":"Adams and Victor's Principles of Neurology","a":"Ropper AH, Samuels MA, Klein JP, Prasad S","pub":"McGraw-Hill","y":2019,"cat":"neurology","sum":"A clinical neurology reference organized by presenting symptom, guiding the reader from history and examination to diagnosis. Strong on stroke, epilepsy, movement disorders, and neuromuscular disease.","key":["Symptom-based approach to neurologic diagnosis","Stroke syndromes and acute management","Epilepsy classification and treatment"]},{"t":"Principles of Neural Science","a":"Kandel ER, Koester JD, Mack SH, Siegelbaum SA (eds.)","pub":"McGraw-Hill","y":2021,"cat":"neurology","sum":"The foundational neuroscience text, from cellular signaling to cognition and behavior. Bridges molecular mechanisms with systems neuroscience and clinical relevance.","key":["Synaptic transmission and plasticity","Sensory and motor systems organization","Neural basis of learning and memory"]},{"t":"The Biology of Cancer","a":"Weinberg RA","pub":"Garland Science","y":2013,"cat":"oncology","sum":"A mechanistic tour of cancer biology: oncogenes, tumor suppressors, and the hallmarks that define malignancy. Expanded coverage of tumor heterogeneity and targeted therapy.","key":["Hallmarks of cancer framework","Oncogenes and tumor suppressor genes","Tumor microenvironment and metastasis"]},{"t":"DeVita, Hellman, and Rosenberg's Cancer","a":"DeVita VT, Lawrence TS, Rosenberg SA (eds.)","pub":"Wolters Kluwer","y":2018,"cat":"oncology","sum":"The standard oncology reference spanning molecular biology, site-specific cancers, and systemic therapy. Integrates surgical, radiation, and medical oncology with supportive care.","key":["Site-specific cancer staging and management","Chemotherapy, targeted, and immune therapies","Oncologic emergencies and supportive care"]},{"t":"Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases","a":"Bennett JE, Dolin R, Blaser MJ (eds.)","pub":"Elsevier","y":2019,"cat":"infectious-disease","sum":"The comprehensive infectious disease reference, from microbial pathogenesis to antimicrobial therapy and infection control. Organized by organism and by clinical syndrome.","key":["Antimicrobial selection and resistance","Syndrome-based diagnostic approach","Healthcare-associated infection prevention"]},{"t":"Isolation of a T-lymphotropic retrovirus from a patient at risk for AIDS","a":"Barre-Sinoussi F, Chermann JC, Rey F et al.","pub":"Science","y":1983,"cat":"infectious-disease","sum":"The landmark report isolating the retrovirus later named HIV from a patient with lymphadenopathy. It launched the virologic era of AIDS research and earned the 2008 Nobel Prize.","key":["First isolation of the AIDS-associated retrovirus","Virus characterization from patient lymphocytes","Foundation of HIV diagnostics and therapy"]},{"t":"Nelson Textbook of Pediatrics","a":"Kliegman RM, St Geme JW, Blum NJ, Shah SS (eds.)","pub":"Elsevier","y":2019,"cat":"pediatrics","sum":"The core pediatrics reference, covering growth, development, and disease from neonatology through adolescence. Balances pathophysiology with practical management guidance.","key":["Neonatal assessment and common conditions","Growth charts and developmental milestones","Pediatric emergency recognition"]},{"t":"Red Book: Report of the Committee on Infectious Diseases","a":"American Academy of Pediatrics","pub":"American Academy of Pediatrics","y":2021,"cat":"pediatrics","sum":"The AAP report on infectious diseases in children, giving immunization schedules, disease summaries, and antimicrobial guidance. Updated every three years.","key":["Childhood immunization schedules","Disease-specific management summaries","Infection control in childcare settings"]},{"t":"Sabiston Textbook of Surgery","a":"Townsend CM, Beauchamp RD, Evers BM, Mattox KL (eds.)","pub":"Elsevier","y":2021,"cat":"surgery","sum":"The foundational surgery text, from perioperative care and technique to specialty procedures. Pairs operative detail with the biological basis of surgical disease.","key":["Perioperative evaluation and risk reduction","Wound healing and surgical infection","Gastrointestinal surgical disease"]},{"t":"A Surgical Safety Checklist to Reduce Morbidity and Mortality","a":"Haynes AB, Weiser TG, Berry WR et al.","pub":"New England Journal of Medicine","y":2009,"cat":"surgery","sum":"The WHO surgical safety checklist study across eight hospitals worldwide. Checklist use was associated with large reductions in surgical complications and mortality.","key":["19-item checklist across three surgical phases","Complications fell from 11% to 7%","Mortality fell from 1.5% to 0.8%"]},{"t":"Diagnostic and Statistical Manual of Mental Disorders (DSM-5-TR)","a":"American Psychiatric Association","pub":"American Psychiatric Association","y":2022,"cat":"psychiatry","sum":"The text revision of the Diagnostic and Statistical Manual of Mental Disorders, defining diagnostic criteria used across psychiatry, with refined criteria text and cultural formulation. It is the common language for diagnosis, billing, and research across mental health care.","key":["Diagnostic criteria sets by disorder","Dimensional and cross-cutting measures","Cultural formulation interview"]},{"t":"Kaplan & Sadock's Synopsis of Psychiatry","a":"Sadock BJ, Sadock VA, Ruiz P","pub":"Wolters Kluwer","y":2021,"cat":"psychiatry","sum":"A compact yet complete psychiatry reference covering diagnosis, psychopharmacology, and psychotherapy. Widely used for board review and clinical practice.","key":["Psychopharmacology by drug class","Psychotherapy modalities overview","Emergency psychiatry and suicide risk"]}],"first":["Amara","Darius","Priya","Kenji","Lucia","Omar","Sofia","Tariq","Nadia","Ellis","Mei","Ravi","Ingrid","Carlos","Aisha","Tomas","Yuki","Farah","Nolan","Zara"],"last":["Marsh","Okafor","Reyes","Tanaka","Novak","Haddad","Lindqvist","Moreau","Petrov","Nguyen","Silva","Khan","Osei","Berg","Costa","Weber","Ali","Frost","Nakamura","Diallo"],"l2angles":["Projected trial of","Forecast model for","Next-generation review of","Simulated outcomes in","Horizon scan of","Projected guideline for","Design study of","Long-range outlook on","Projected meta-analysis of","Future practice review of","Prototype framework for","Projected cohort study of"],"l2find":["a projected 18-24% improvement in primary outcomes versus current baselines","modelled cost reductions of 12-30% once the approach reaches scale","adherence gains projected at 15-22% under guided protocols","early simulations suggest recovery timelines shorter by 9-14 months","projected accuracy of 91-96% in independent validation cohorts","workflow time projected to fall 25-40% along the modelled pathway","patient-reported outcomes projected 20-28% above current standards","equity modelling projects roughly 30% wider access in underserved groups","safety modelling forecasts adverse events below 3% in target populations","projected training time for practitioners cut nearly in half","resource-use models show 20-35% lower demand on specialist time","long-term follow-up projections extend benefit durability past ten years","comparative models rank the approach first on benefit-to-burden ratio","sensitivity analysis holds the main finding across all tested assumptions","projected readmission or relapse rates 22-31% below current norms","early-adopter pilots in the model reach break-even within three years","standardisation projections cut unwarranted variation by about half","the model forecasts strong results across age bands and settings","projected documentation burden falls by roughly one third","forecasts show the approach remaining cost-effective under strict thresholds"],"l2abst":["This projected study examines {topic}. {f1}. {f2}. Prepared as a forward-looking archive entry for {y}, it describes a possible future rather than any real publication.","A forward-looking review of {topic}, projected for {y}. {f1}. {f2}. All figures here are modelled estimates, not measured results.","This horizon scan surveys {topic} and where current trajectories may lead by {y}. {f1}. {f2}. It is an archive projection, clearly separated from real published works.","Built as a planning reference for {y}, this projected analysis covers {topic}. {f1}. {f2}. Its figures are forecasts, and it has no real-world counterpart."],"l2topics":["polypill strategies for cardiovascular prevention","CRISPR-based therapies for sickle cell disease","liquid biopsy for early cancer detection","AI triage in emergency departments","antimicrobial resistance surveillance networks","digital twins for diabetes management","long-COVID rehabilitation protocols","microbiome therapies for inflammatory bowel disease","wearable arrhythmia detection at scale","vaccine platforms for emerging pathogens","personalized oncology dosing models","hospital-at-home acute care models","sepsis early-warning algorithms","gene therapy for inherited blindness","obesity pharmacotherapy pathways","mental-health integration in primary care","stroke thrombectomy access modelling","antifungal stewardship programs","pediatric asthma remote monitoring","frailty screening in surgical candidates","point-of-care ultrasound training","tele-ICU coverage models","opioid-sparing pain protocols","maternal mortality reduction bundles","tuberculosis elimination strategies","malaria vaccine rollout modelling","dementia risk-reduction programs","rare-disease registry networks","surgical robotics learning curves","blood-supply resilience planning","climate-linked disease surveillance","nutrition interventions in oncology","sleep-apnea screening pathways","transplant organ allocation models","antibiotic allergy de-labelling","palliative care early integration"],"l2journals":["JAH Projected Medical Review","Journal of Future Clinical Medicine","Projected Medical Science Quarterly","Annals of Medical Foresight","Frontiers in Clinical Projection","JAH Medicine Futures"],"annotFocus":["clinical application","teaching use","research methods","historical context","patient communication","policy implications","interdisciplinary links","assessment design"],"readLevels":["undergraduate","postgraduate","practitioner","researcher","general reader"]};
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
