/* SIGNATURE — JAH Care of the Elderly and Disabled Adults Published Archive Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic: seed + version always yields the same record. 1,000,000 address space.
   Level 1 = real published works (textbooks, landmark papers, curricula, standards).
   Level 2 = projection-based archive entries; every Level 2 title starts with "Level 2". */
(function(){'use strict';
var SLUG='elder-care-published';
var BASE='elder-care';
var PREFIX='JAH-elder-care-published-P-';
var STUDYPREFIX='JAH-elder-care-STUDY-S-';
var STUDYURL='../elder-care-study/index.html?sig=';
var VERSION='jahdb-elder-care-published-1.0';
var IDRE=new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$');
var SIGRE=new RegExp('^\\.\\./'+BASE+'-study/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{7}$');
var DATA={"cats":["geriatrics","dementia-care","palliative-care","assisted-living","elder-safety","disability-support","caregiver-support"],"real":[{"t":"Hazzard's Geriatric Medicine and Gerontology","a":"Halter JB, Ouslander JG, Studenski S et al. (eds.)","pub":"McGraw-Hill","y":2021,"cat":"geriatrics","sum":"The geriatrics reference: biology of aging, geriatric syndromes, and care models from hospital to home. Frames aging as modifiable, not merely decline. The eighth edition added COVID-19 and health equity content.","key":["Geriatric syndromes approach","Comprehensive geriatric assessment","Care transitions models"]},{"t":"AGS Beers Criteria","a":"American Geriatrics Society","pub":"Journal of the American Geriatrics Society","y":2023,"cat":"geriatrics","sum":"The updated Beers Criteria for potentially inappropriate medication use in older adults: drugs to avoid and safer alternatives. Revised regularly as new evidence emerges on drug risks in aging.","key":["Potentially inappropriate drugs","Drug-disease interactions","Safer prescribing alternatives"]},{"t":"The 36-Hour Day","a":"Mace NL, Rabins PV","pub":"Johns Hopkins University Press","y":2017,"cat":"dementia-care","sum":"The classic family guide to dementia care: understanding symptoms, managing behaviors, and caring for the caregiver. In its seventh edition. Resource lists connect families to community supports.","key":["Behavioral symptom management","Communication strategies","Caregiver self-care strategies"]},{"t":"Risk reduction of cognitive decline and dementia","a":"World Health Organization","pub":"WHO","y":2019,"cat":"dementia-care","sum":"WHO guidelines on twelve modifiable risk factors for dementia, from physical activity to hearing management. Recommendations span physical activity, nutrition, and vascular care.","key":["Twelve modifiable risk factors","Evidence-graded recommendations","Life-course prevention"]},{"t":"Oxford Textbook of Palliative Medicine","a":"Cherny N, Fallon M, Kaasa S et al. (eds.)","pub":"Oxford University Press","y":2021,"cat":"palliative-care","sum":"The palliative medicine reference: symptom control, communication, and care across settings from hospice to hospital. The sixth edition expanded non-cancer palliative coverage.","key":["Pain and symptom management","Goals-of-care communication","Palliative care models"]},{"t":"Being Mortal","a":"Gawande A","pub":"Metropolitan Books","y":2014,"cat":"palliative-care","sum":"Atul Gawande's examination of medicine's approach to aging and death, arguing for care organized around what matters to patients. The book spurred wide adoption of serious-illness conversation guides.","key":["Limits of medicalization","Assisted living critique","Conversations about goals"]},{"t":"The Eden Alternative","a":"Thomas WH","pub":"VanderWyk & Burnham","y":1994,"cat":"assisted-living","sum":"William Thomas's philosophy of elder care: combating loneliness, helplessness, and boredom through empowered, home-like environments. Its principles now shape nursing home reform worldwide.","key":["Three plagues of nursing homes","Empowered care teams","Home-like environments"]},{"t":"Culture Change in Nursing Homes","a":"Pioneer Network","pub":"Pioneer Network","y":2011,"cat":"assisted-living","sum":"The culture-change movement's principles for person-directed nursing home care: consistent staffing, resident choice, and home-like design. Artifacts of culture change give homes a practical roadmap.","key":["Person-directed care principles","Consistent assignment","Environmental transformation"]},{"t":"WHO Global Report on Falls Prevention in Older Age","a":"World Health Organization","pub":"WHO","y":2007,"cat":"elder-safety","sum":"WHO's global review of falls epidemiology and prevention: risk factors and effective interventions across settings. Intervention reviews cover exercise, home safety, and medication review.","key":["Global falls epidemiology","Modifiable risk factors","Effective interventions"]},{"t":"Elder abuse prevalence in community settings","a":"Yon Y, Mikton CR, Gassoumis ZD, Wilber KH","pub":"Lancet Global Health","y":2017,"cat":"elder-safety","sum":"Systematic review estimating 1 in 6 older adults experiences elder abuse, with psychological abuse most common. Called for global prevention action. The review pooled 52 studies across 28 countries.","key":["1-in-6 prevalence estimate","Abuse subtypes breakdown","Prevention recommendations"]},{"t":"UN Convention on the Rights of Persons with Disabilities","a":"United Nations","pub":"United Nations","y":2006,"cat":"disability-support","sum":"The international human rights treaty affirming the rights of persons with disabilities: accessibility, inclusion, and independent living. Over 190 states have ratified or acceded to the convention.","key":["Accessibility obligations","Independent living rights","Inclusive education and work"]},{"t":"World Report on Disability","a":"World Health Organization","pub":"WHO","y":2011,"cat":"disability-support","sum":"WHO and World Bank's landmark report: over a billion people live with disability, facing barriers in health, education, and employment. It launched a decade of disability-inclusive development policy.","key":["Billion-person prevalence","Barrier analysis across sectors","Inclusive policy recommendations"]},{"t":"Resources for Enhancing Alzheimer's Caregiver Health (REACH)","a":"Burgio LD, Stevens A, Guy D et al.","pub":"The Gerontologist","y":2003,"cat":"caregiver-support","sum":"A multi-component intervention reducing caregiver burden and depression in Alzheimer's caregivers, later translated to community programs. The REACH II trial confirmed benefits in a larger sample.","key":["Multi-component design","Burden and depression outcomes","Translation to community programs"]},{"t":"Families Caring for an Aging America","a":"National Academies of Sciences, Engineering, and Medicine","pub":"National Academies Press","y":2016,"cat":"caregiver-support","sum":"The National Academies report on family caregiving: 17.7 million caregivers, their economic value, and policies to support them. The report estimated $470 billion in annual economic value.","key":["Caregiver population estimates","Economic value of family care","Policy recommendations"]}],"first":["Amara","Darius","Priya","Kenji","Lucia","Omar","Sofia","Tariq","Nadia","Ellis","Mei","Ravi","Ingrid","Carlos","Aisha","Tomas","Yuki","Farah","Nolan","Zara"],"last":["Marsh","Okafor","Reyes","Tanaka","Novak","Haddad","Lindqvist","Moreau","Petrov","Nguyen","Silva","Khan","Osei","Berg","Costa","Weber","Ali","Frost","Nakamura","Diallo"],"l2angles":["Projected trial of","Forecast model for","Next-generation review of","Simulated outcomes in","Horizon scan of","Projected guideline for","Design study of","Long-range outlook on","Projected meta-analysis of","Future practice review of","Prototype framework for","Projected cohort study of"],"l2find":["a projected 18-24% improvement in primary outcomes versus current baselines","modelled cost reductions of 12-30% once the approach reaches scale","adherence gains projected at 15-22% under guided protocols","early simulations suggest recovery timelines shorter by 9-14 months","projected accuracy of 91-96% in independent validation cohorts","workflow time projected to fall 25-40% along the modelled pathway","patient-reported outcomes projected 20-28% above current standards","equity modelling projects roughly 30% wider access in underserved groups","safety modelling forecasts adverse events below 3% in target populations","projected training time for practitioners cut nearly in half","resource-use models show 20-35% lower demand on specialist time","long-term follow-up projections extend benefit durability past ten years","comparative models rank the approach first on benefit-to-burden ratio","sensitivity analysis holds the main finding across all tested assumptions","projected readmission or relapse rates 22-31% below current norms","early-adopter pilots in the model reach break-even within three years","standardisation projections cut unwarranted variation by about half","the model forecasts strong results across age bands and settings","projected documentation burden falls by roughly one third","forecasts show the approach remaining cost-effective under strict thresholds"],"l2abst":["This projected study examines {topic}. {f1}. {f2}. Prepared as a forward-looking archive entry for {y}, it describes a possible future rather than any real publication.","A forward-looking review of {topic}, projected for {y}. {f1}. {f2}. All figures here are modelled estimates, not measured results.","This horizon scan surveys {topic} and where current trajectories may lead by {y}. {f1}. {f2}. It is an archive projection, clearly separated from real published works.","Built as a planning reference for {y}, this projected analysis covers {topic}. {f1}. {f2}. Its figures are forecasts, and it has no real-world counterpart."],"l2topics":["dementia-friendly community design","fall-proofing home modifications","loneliness interventions for seniors","elder abuse detection training","person-centered care planning","assisted living staffing models","memory care unit design","palliative care in nursing homes","advance care planning uptake","medication review in polypharmacy elders","malnutrition screening in care homes","oral health in dependent elders","hearing aid adoption barriers","vision screening in residential care","continence care dignity standards","pressure injury prevention bundles","restraint-free care policies","wandering management technologies","intergenerational housing models","village model aging in place","adult day program outcomes","respite care access","caregiver burden measurement","dementia caregiver training","end-of-life doula roles","hospice volunteer programs","green care farms for dementia","music therapy in advanced dementia","pet therapy in care homes","exercise programs for frailty","telehealth for homebound elders","remote monitoring ethics","elder financial exploitation prevention","guardianship reform models","age-friendly city indicators","retirement community regulation"],"l2journals":["JAH Projected Gerontology Review","Journal of Future Elder Care","Projected Ageing Science Quarterly","Annals of Care Foresight","Frontiers in Gerontology Projection","JAH Elder Care Futures"],"annotFocus":["clinical application","teaching use","research methods","historical context","patient communication","policy implications","interdisciplinary links","assessment design"],"readLevels":["undergraduate","postgraduate","practitioner","researcher","general reader"]};
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
