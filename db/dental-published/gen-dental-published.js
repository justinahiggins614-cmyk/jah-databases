/* SIGNATURE — JAH Dental Studies Published Archive Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic: seed + version always yields the same record. 1,000,000 address space.
   Level 1 = real published works (textbooks, landmark papers, curricula, standards).
   Level 2 = projection-based archive entries; every Level 2 title starts with "Level 2". */
(function(){'use strict';
var SLUG='dental-published';
var BASE='dental';
var PREFIX='JAH-dental-published-P-';
var STUDYPREFIX='JAH-dental-STUDY-S-';
var STUDYURL='../dental-study/index.html?sig=';
var VERSION='jahdb-dental-published-1.0';
var IDRE=new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$');
var SIGRE=new RegExp('^\\.\\./'+BASE+'-study/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{7}$');
var DATA={"cats":["endodontics","orthodontics","periodontics","oral-surgery","prosthodontics","pediatric-dentistry","oral-pathology"],"real":[{"t":"Cohen's Pathways of the Pulp","a":"Hargreaves KM, Berman LH (eds.)","pub":"Elsevier","y":2021,"cat":"endodontics","sum":"The standard endodontics reference, covering pulp biology, diagnosis of pulpal and periapical disease, and root canal treatment from access to obturation. The thirteenth edition adds regenerative endodontics, vital pulp therapy, and 3D imaging in treatment planning.","key":["Step-by-step protocols for cleaning, shaping, and obturation","Diagnosis chapters linking symptoms to pulpal and periapical conditions","Regenerative procedures and vital pulp therapy updates"]},{"t":"Endodontic Microbiology","a":"Fouad AF (ed.)","pub":"Wiley-Blackwell","y":2017,"cat":"endodontics","sum":"A focused text on the microbiology of endodontic infections, from biofilm ecology in the root canal system to antimicrobial strategy. It connects laboratory findings with clinical decisions on disinfection and medicaments.","key":["Biofilm ecology of primary and persistent infections","Evidence on irrigants, medicaments, and disinfection","Microbial basis of treatment failure and retreatment"]},{"t":"Contemporary Orthodontics","a":"Proffit WR, Fields HW, Larson BE","pub":"Elsevier","y":2018,"cat":"orthodontics","sum":"The leading orthodontic text, integrating growth and development, biomechanics, and treatment planning from early intervention through orthognathic surgery. Emphasizes evidence-based mechanics and the biology of tooth movement.","key":["Biomechanics of tooth movement and anchorage","Growth modification and timing of treatment","Surgical orthodontics and interdisciplinary care"]},{"t":"Orthodontics: Current Principles and Techniques","a":"Graber LW, Vanarsdall RL, Vig KWL (eds.)","pub":"Elsevier","y":2016,"cat":"orthodontics","sum":"A comprehensive multi-author reference on contemporary orthodontic practice, from diagnosis and imaging to aligner therapy and temporary anchorage devices. Each chapter pairs technique with supporting evidence.","key":["Clear aligner therapy protocols and limitations","Temporary anchorage devices in complex cases","Retention science and long-term stability"]},{"t":"Carranza's Clinical Periodontology","a":"Newman MG, Takei HH, Klokkevold PR, Carranza FA","pub":"Elsevier","y":2018,"cat":"periodontics","sum":"The definitive periodontology text, spanning periodontal anatomy, disease classification, non-surgical therapy, and surgical and implant approaches. Reflects the current classification of periodontal diseases.","key":["Current classification of periodontal and peri-implant diseases","Scaling, root planing, and surgical decision-making","Implant site development and maintenance"]},{"t":"Clinical Periodontology and Implant Dentistry","a":"Lindhe J, Lang NP (eds.)","pub":"Wiley","y":2015,"cat":"periodontics","sum":"A two-volume reference pairing periodontology with implant dentistry, strong on epidemiology, risk assessment, and long-term maintenance. Widely used in postgraduate periodontal training.","key":["Risk assessment and prognostication models","Guided tissue regeneration techniques","Long-term supportive periodontal therapy"]},{"t":"Contemporary Oral and Maxillofacial Surgery","a":"Hupp JR, Tucker MR, Ellis E","pub":"Elsevier","y":2018,"cat":"oral-surgery","sum":"The core oral surgery text for dental training, covering exodontia, impactions, preprosthetic surgery, trauma, and orthognathic procedures. Clear surgical sequences pair with medical management of the surgical patient.","key":["Third molar assessment and removal technique","Management of odontogenic infections","Trauma and orthognathic surgery principles"]},{"t":"Peterson's Principles of Oral and Maxillofacial Surgery","a":"Miloro M (ed.)","pub":"PMPH-USA","y":2011,"cat":"oral-surgery","sum":"A three-volume surgical reference covering the full scope of oral and maxillofacial surgery, from dentoalveolar procedures to reconstruction and TMJ surgery. Written for residents and practicing surgeons.","key":["Dentoalveolar and implant surgery","Maxillofacial trauma management","Reconstructive and TMJ procedures"]},{"t":"Prosthodontic Treatment for Edentulous Patients","a":"Zarb GA, Hobkirk JA, Eckert SE, Jacob RF","pub":"Elsevier","y":2012,"cat":"prosthodontics","sum":"The classic complete-denture and implant overdenture text, covering diagnosis, impression technique, occlusion, and long-term care of edentulous patients. Balances conventional prosthodontics with implant-assisted options.","key":["Complete denture fabrication sequence","Implant overdenture design and attachments","Occlusal schemes for edentulous arches"]},{"t":"Fundamentals of Fixed Prosthodontics","a":"Shillingburg HT, Sather DA, Wilson EL et al.","pub":"Quintessence","y":2012,"cat":"prosthodontics","sum":"The standard crown-and-bridge reference, detailing tooth preparation, impression making, provisionalization, and cementation. Its preparation designs and laboratory communication chapters remain widely taught.","key":["Tooth preparation geometry and retention","Definitive impression techniques","Provisional restorations and cementation"]},{"t":"Pediatric Dentistry: Infancy through Adolescence","a":"Nowak AJ, Christensen JR, Mabry TR (eds.)","pub":"Elsevier","y":2018,"cat":"pediatric-dentistry","sum":"A complete pediatric dentistry reference from infant oral health through adolescent care, covering behavior guidance, caries management, trauma, and special health care needs. Aligned with AAPD guidelines.","key":["Behavior guidance techniques by age","Early childhood caries prevention and care","Trauma management in the primary dentition"]},{"t":"Handbook of Pediatric Dentistry","a":"Cameron AC, Widmer RP","pub":"Elsevier","y":2013,"cat":"pediatric-dentistry","sum":"A concise clinical handbook for pediatric dental practice, organized for quick reference on diagnosis, treatment planning, and common procedures in children and adolescents. Tables and algorithms support chairside decisions on sedation, trauma, and preventive care.","key":["Chairside diagnosis and treatment planning","Pulp therapy in primary teeth","Orthodontic screening in the mixed dentition"]},{"t":"Oral and Maxillofacial Pathology","a":"Neville BW, Damm DD, Allen CM, Chi AC","pub":"Elsevier","y":2015,"cat":"oral-pathology","sum":"The standard oral pathology text, correlating clinical presentation with histopathology across odontogenic tumors, mucosal disease, and salivary gland pathology. Richly illustrated throughout.","key":["Odontogenic cysts and tumors: classification","Clinical-pathologic correlation method","Premalignant lesions and oral cancer"]},{"t":"Oral Pathology: Clinical Pathologic Correlations","a":"Regezi JA, Sciubba JJ, Jordan RCK","pub":"Elsevier","y":2016,"cat":"oral-pathology","sum":"A correlation-driven pathology text teaching diagnosis by linking clinical findings with microscopic features. Strong on vesiculobullous disease, white lesions, and immune-mediated conditions.","key":["Differential diagnosis of white lesions","Vesiculobullous diseases","Soft tissue tumors of the oral cavity"]}],"first":["Amara","Darius","Priya","Kenji","Lucia","Omar","Sofia","Tariq","Nadia","Ellis","Mei","Ravi","Ingrid","Carlos","Aisha","Tomas","Yuki","Farah","Nolan","Zara"],"last":["Marsh","Okafor","Reyes","Tanaka","Novak","Haddad","Lindqvist","Moreau","Petrov","Nguyen","Silva","Khan","Osei","Berg","Costa","Weber","Ali","Frost","Nakamura","Diallo"],"l2angles":["Projected trial of","Forecast model for","Next-generation review of","Simulated outcomes in","Horizon scan of","Projected guideline for","Design study of","Long-range outlook on","Projected meta-analysis of","Future practice review of","Prototype framework for","Projected cohort study of"],"l2find":["a projected 18-24% improvement in primary outcomes versus current baselines","modelled cost reductions of 12-30% once the approach reaches scale","adherence gains projected at 15-22% under guided protocols","early simulations suggest recovery timelines shorter by 9-14 months","projected accuracy of 91-96% in independent validation cohorts","workflow time projected to fall 25-40% along the modelled pathway","patient-reported outcomes projected 20-28% above current standards","equity modelling projects roughly 30% wider access in underserved groups","safety modelling forecasts adverse events below 3% in target populations","projected training time for practitioners cut nearly in half","resource-use models show 20-35% lower demand on specialist time","long-term follow-up projections extend benefit durability past ten years","comparative models rank the approach first on benefit-to-burden ratio","sensitivity analysis holds the main finding across all tested assumptions","projected readmission or relapse rates 22-31% below current norms","early-adopter pilots in the model reach break-even within three years","standardisation projections cut unwarranted variation by about half","the model forecasts strong results across age bands and settings","projected documentation burden falls by roughly one third","forecasts show the approach remaining cost-effective under strict thresholds"],"l2abst":["This projected study examines {topic}. {f1}. {f2}. Prepared as a forward-looking archive entry for {y}, it describes a possible future rather than any real publication.","A forward-looking review of {topic}, projected for {y}. {f1}. {f2}. All figures here are modelled estimates, not measured results.","This horizon scan surveys {topic} and where current trajectories may lead by {y}. {f1}. {f2}. It is an archive projection, clearly separated from real published works.","Built as a planning reference for {y}, this projected analysis covers {topic}. {f1}. {f2}. Its figures are forecasts, and it has no real-world counterpart."],"l2topics":["caries-risk prediction in school-age children","stem-cell pulp regeneration in endodontics","AI-assisted radiographic caries detection","antimicrobial implant surfaces for peri-implantitis","teledentistry triage in rural districts","3D-printed biocompatible crowns","salivary diagnostics for oral cancer","orthodontic aligner biomechanics modelling","minimally invasive caries excavation","fluoride varnish programs in preschools","digital smile design workflows","robotic assistance in implant placement","periodontal regeneration with growth factors","dental anxiety reduction protocols","silver diamine fluoride in community care","occlusal guard personalization","oral microbiome mapping","same-day CAD/CAM restorations","geriatric denture adaptation","cleft palate care pathways","temporomandibular disorder therapy","dental trauma first-response training","water fluoridation policy modelling","mobile dental clinics for underserved areas","laser dentistry in soft-tissue surgery","nanocomposite longevity studies","dental sleep medicine screening","interceptive orthodontics timing","endodontic retreatment decision aids","oral health literacy campaigns","antibiotic stewardship in dentistry","prosthodontic digital impressions","pediatric sedation safety standards","dental workforce distribution models","chewing function rehabilitation","halitosis diagnostic protocols"],"l2journals":["JAH Projected Review of Dental Science","Journal of Future Oral Research","Projected Dental Science Quarterly","Annals of Dental Foresight","Frontiers in Dental Projection","JAH Dental Futures"],"annotFocus":["clinical application","teaching use","research methods","historical context","patient communication","policy implications","interdisciplinary links","assessment design"],"readLevels":["undergraduate","postgraduate","practitioner","researcher","general reader"]};
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
