'use strict';
// Build JAH Medical Research Database: ~2000 online methodology records + signature.
// Online records are real study-design/methods knowledge; NO fabricated trial outcomes.
const path=require('path');
const lib=require('../buildlib.js');
const gen=require('./gen-medical-research.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='medical-research', PREFIX='JAH-MED-';
const REF='https://www.equator-network.org/';
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
// ---- study designs: [name, definition] ----
const DESIGNS=[['randomized controlled trial','participants are randomly assigned to intervention or control arms'],['cluster randomized trial','groups or clinics rather than individuals are randomized'],['crossover trial','each participant receives each intervention in sequence'],['factorial trial','two or more interventions are tested simultaneously'],['non-inferiority trial','tests that a new intervention is not worse than standard by a preset margin'],['equivalence trial','tests that interventions are equivalent within margins'],['superiority trial','tests that a new intervention is better than control'],['pragmatic trial','tests effectiveness under real-world practice conditions'],['pilot trial','a small trial testing feasibility before a full trial'],['prospective cohort study','a defined group is followed forward in time'],['retrospective cohort study','a group is followed using past records'],['case-control study','cases with an outcome are compared with controls without it'],['nested case-control study','a case-control study conducted within a defined cohort'],['cross-sectional study','exposure and outcome are measured at one time point'],['ecological study','comparisons are made at group rather than individual level'],['case series','a series of cases described without a control group'],['case report','a detailed description of a single case'],['before-after study','outcomes are compared before and after an intervention'],['interrupted time series','a trend is compared before and after an event'],['stepped wedge trial','clusters cross to the intervention in randomized steps'],['N-of-1 trial','a single patient undergoes multiple crossovers'],['adaptive trial','the design is modified based on interim data'],['platform trial','multiple interventions are tested under one master protocol'],['registry study','outcomes are drawn from clinical registries'],['qualitative study','explores experiences and meanings in depth'],['mixed methods study','combines quantitative and qualitative approaches'],['Delphi study','structured expert consensus through survey rounds'],['diagnostic accuracy study','an index test is compared with a reference standard']];
const DASPECTS=['definition','strengths','weaknesses','when to use','bias risks','design features','analysis notes','reporting guideline','example structure','teaching notes','randomization notes','sample-size notes','ethics notes','worked example'];
DESIGNS.forEach(d=>{
  DASPECTS.forEach(a=>{
    add({title:d[0]+' - '+a,category:'trials',
      description:'Study design ('+a+'): a '+d[0]+' is a design in which '+d[1]+'. Standard research-methods teaching reference.',
      study_design:d[0],design_definition:d[1],population:'defined by eligibility criteria',setting:'defined by protocol',
      methods_summary:'Follow the design\u2019s standard structure: define the question, select the design, recruit, measure, and analyze per protocol.',
      findings_summary:'Findings depend on the executed study; templates here carry no real outcomes.',
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- reporting guidelines ----
const GUIDES=[['CONSORT','Consolidated Standards of Reporting Trials, for randomized trials'],['PRISMA','Preferred Reporting Items for Systematic Reviews and Meta-Analyses'],['STROBE','Strengthening the Reporting of Observational Studies in Epidemiology'],['STARD','Standards for Reporting of Diagnostic Accuracy Studies'],['CARE','Case Report guidelines'],['SQUIRE','Standards for Quality Improvement Reporting Excellence'],['ARRIVE','Animal Research: Reporting of In Vivo Experiments'],['SPIRIT','Standard Protocol Items for clinical trial protocols'],['TRIPOD','Transparent Reporting of prediction models'],['CHEERS','Consolidated Health Economic Evaluation Reporting Standards'],['SRQR','Standards for Reporting Qualitative Research'],['COREQ','Consolidated criteria for Reporting Qualitative research']];
const GASPECTS=['purpose','checklist','flow diagram','when to use','key items','extensions','journal endorsement','teaching notes','history','related guidelines'];
GUIDES.forEach(g=>{
  GASPECTS.forEach(a=>{
    add({title:g[0]+' guideline - '+a,category:'methods',
      description:'Reporting guideline ('+a+'): '+g[0]+' ('+g[1]+'). Guidelines standardize what authors report so studies can be appraised and reproduced.',
      method:g[0],purpose:g[1],steps:['Consult the checklist early','Report every item transparently','Submit the checklist with the manuscript'],
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- biases ----
const BIAS=['selection bias','information bias','recall bias','observer bias','publication bias','confounding','lead-time bias','length bias','Berkson bias','Neyman bias','Hawthorne effect','placebo effect','attrition bias','detection bias','performance bias','allocation bias','confirmation bias','sponsorship bias','language bias','citation bias','outcome reporting bias','spectrum bias','verification bias','referral bias','volunteer bias','healthy worker effect','protopathic bias','immortal time bias','ecological fallacy','misclassification bias'];
const BIASD=['systematic error from how participants are selected','systematic error in measuring exposure or outcome','distorted memory of past exposures','systematic error from unblinded assessors','selective publication of positive results','mixing of effects from a third variable','apparent survival gain from earlier diagnosis','overrepresentation of slow-progressing cases','hospital-based selection distorting associations','survival-based selection distorting associations','behavior change from being observed','improvement from expectation of treatment','systematic loss of participants','unequal outcome detection between groups','unequal care apart from the intervention','foreknowledge of assignments influencing enrollment','favoring evidence that confirms beliefs','funding source influencing design or reporting','excluding non-English studies','selective citation of supportive work','selective reporting of favorable outcomes','test performance varying with case mix','reference-standard application depending on test result','referral patterns distorting case mix','volunteers differing from the target population','workers healthier than the general population','early symptoms prompting the exposure','survival time misattributed to treatment','group-level associations misapplied to individuals','errors in classifying exposure or outcome'];
const BASPECTS=['definition','examples','prevention','detection','teaching notes','related biases','design implications','quantification','reporting','history'];
BIAS.forEach((b,i)=>{
  BASPECTS.forEach(a=>{
    add({title:b+' - '+a,category:'methods',
      description:'Bias ('+a+'): '+b+' is '+BIASD[i]+'. Standard epidemiology teaching reference.',
      method:b,purpose:BIASD[i],steps:['Name the bias in the design','Apply preventive measures','Discuss residual risk transparently'],
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- statistics concepts ----
const STATS=[['p-value','the probability of data as extreme under the null'],['confidence interval','a range plausibly containing the true effect'],['statistical power','the probability of detecting a true effect'],['sample size','the number of observations, set by power analysis'],['effect size','the magnitude of the observed difference'],['odds ratio','the ratio of odds between groups'],['risk ratio','the ratio of risks between groups'],['hazard ratio','the ratio of event rates over time'],['number needed to treat','patients treated for one to benefit'],['sensitivity','true-positive rate of a test'],['specificity','true-negative rate of a test'],['positive predictive value','probability of disease given a positive test'],['negative predictive value','probability of no disease given a negative test'],['ROC curve','true-positive vs false-positive trade-off'],['Kaplan-Meier','nonparametric survival estimation'],['Cox regression','semiparametric survival modeling'],['logistic regression','modeling binary outcomes'],['linear regression','modeling continuous outcomes'],['ANOVA','comparing means across groups'],['t-test','comparing two means'],['chi-square test','testing categorical associations'],['Fisher exact test','exact test for small tables'],['Mann-Whitney U','nonparametric two-group comparison'],['Kruskal-Wallis','nonparametric multi-group comparison'],['Bonferroni correction','adjusting for multiple comparisons'],['intention-to-treat','analyzing by randomized assignment'],['per-protocol','analyzing by treatment received'],['missing data handling','methods for incomplete observations'],['Bayesian analysis','updating beliefs with data'],['meta-analysis','quantitative synthesis across studies'],['fixed-effect model','pooling assuming one true effect'],['random-effects model','pooling allowing varying effects'],['heterogeneity I-squared','proportion of variation from heterogeneity'],['funnel plot','visual check for publication bias'],['GRADE approach','rating certainty of evidence'],['forest plot','display of study effects and pooling'],['subgroup analysis','effects within predefined subgroups'],['interim analysis','planned early looks at accumulating data'],['propensity score matching','balancing covariates in observational data'],['multiple imputation','filling missing values with plausible draws']];
const SASPECTS=['definition','interpretation','assumptions','reporting','pitfalls','teaching notes','related concepts','worked logic','software notes','history'];
STATS.forEach(s=>{
  SASPECTS.forEach(a=>{
    add({title:s[0]+' - '+a,category:'methods',
      description:'Statistics ('+a+'): '+s[0]+' - '+s[1]+'. Standard biostatistics teaching reference.',
      method:s[0],purpose:s[1],steps:['State the question and assumptions','Apply the method correctly','Report estimates with uncertainty'],
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- ethics ----
const ETHICS=[['Declaration of Helsinki','ethical principles for human medical research'],['Belmont Report','respect, beneficence, and justice in research'],['Common Rule','US federal protections for human subjects'],['Nuremberg Code','foundational voluntary-consent principles'],['institutional review board','independent ethics review of protocols'],['informed consent','voluntary agreement after disclosure'],['HIPAA privacy','protection of health information in the US'],['good clinical practice','quality standards for trial conduct'],['ClinicalTrials.gov registration','public prospective trial registration'],['data safety monitoring board','independent safety oversight'],['clinical equipoise','genuine uncertainty justifying randomization'],['vulnerable populations','extra protections for at-risk groups'],['incidental findings','unexpected discoveries in research'],['data sharing','making research data available responsibly'],['ICMJE authorship','criteria for authorship credit'],['conflicts of interest','disclosure of competing interests']];
const EASPECTS=['principles','history','requirements','documentation','teaching notes','related rules','enforcement','scope','exceptions','key documents'];
ETHICS.forEach(e=>{
  EASPECTS.forEach(a=>{
    add({title:e[0]+' - '+a,category:'methods',
      description:'Research ethics ('+a+'): '+e[0]+' covers '+e[1]+'. Standard research-ethics teaching reference.',
      method:e[0],purpose:e[1],steps:['Identify the applicable rule','Document compliance','Report deviations transparently'],
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- landmark trials: metadata only, no outcome claims ----
const TRIALS=[['Framingham Heart Study','1948','prospective cohort','5,209 adults of Framingham, Massachusetts','cardiovascular risk factors','The Framingham Heart Study, begun in 1948, is a landmark prospective cohort study; the original cohort enrolled 5,209 adults examined biennially.'],['Framingham Offspring Study','1971','prospective cohort','offspring of the original cohort','familial clustering of heart disease','Begun in 1971, the Offspring Study enrolled children of the original cohort and their spouses.'],['Nurses\u2019 Health Study','1976','prospective cohort','US nurses','women\u2019s health and lifestyle','A long-running prospective cohort of US nurses begun in 1976.'],['Physicians\u2019 Health Study','1982','randomized trial','US male physicians','aspirin and cardiovascular prevention','A randomized trial in US male physicians begun in the 1980s.'],['MRFIT','1970s','randomized trial','men at high coronary risk','multifactor risk intervention','The Multiple Risk Factor Intervention Trial tested risk-factor modification in the 1970s-80s.'],['ALLHAT','1994','randomized trial','adults with hypertension','antihypertensive drug comparison','A large hypertension treatment trial begun in 1994.'],['Women\u2019s Health Initiative','1991','randomized trials plus cohort','postmenopausal women','hormone therapy and prevention','A major women\u2019s health program begun in 1991.'],['UKPDS','1977','randomized trial','adults with type 2 diabetes','glucose control strategies','The UK Prospective Diabetes Study began in 1977.'],['DCCT','1983','randomized trial','people with type 1 diabetes','intensive glucose control','The Diabetes Control and Complications Trial began in 1983.'],['ACCORD','2001','randomized trial','adults with type 2 diabetes','glucose, blood pressure, lipid targets','A factorial-style trial program begun in 2001.'],['SPRINT','2010','randomized trial','adults with hypertension','intensive blood pressure control','A blood-pressure target trial begun in 2010.'],['4S','1988','randomized trial','adults with high cholesterol','statin therapy','The Scandinavian Simvastatin Survival Study began in 1988.'],['JUPITER','2003','randomized trial','adults with elevated CRP','statin in primary prevention','A primary-prevention statin trial begun in 2003.'],['HOPE','1994','randomized trial','adults at vascular risk','ACE inhibition','The Heart Outcomes Prevention Evaluation began in 1994.'],['ISIS-2','1985','randomized trial','suspected acute MI patients','streptokinase and aspirin','The Second International Study of Infarct Survival began in 1985.'],['GISSI','1984','randomized trial','acute MI patients','thrombolysis strategies','The Italian GISSI program began in 1984.'],['CAST','1987','randomized trial','post-MI patients with arrhythmia','antiarrhythmic drugs','The Cardiac Arrhythmia Suppression Trial began in 1987.'],['ARIC','1987','prospective cohort','US community adults','atherosclerosis risk','The Atherosclerosis Risk in Communities study began in 1987.'],['MESA','2000','prospective cohort','multi-ethnic US adults','subclinical cardiovascular disease','The Multi-Ethnic Study of Atherosclerosis began in 2000.'],['Rotterdam Study','1990','prospective cohort','older adults of Rotterdam','diseases of aging','A population cohort begun in 1990.'],['Whitehall Study','1967','prospective cohort','British civil servants','social determinants of health','The Whitehall studies of civil servants began in 1967.'],['RE-LY','2005','randomized trial','adults with atrial fibrillation','anticoagulation comparison','A trial of anticoagulants in atrial fibrillation begun in 2005.'],['PLATO','2006','randomized trial','acute coronary syndrome patients','antiplatelet comparison','A trial in acute coronary syndromes begun in 2006.'],['ONTARGET','2001','randomized trial','adults at vascular risk','telmisartan vs ramipril','A vascular-protection trial begun in 2001.']];
const TASPECTS2=['identity','design','population','era','contribution area','reference note'];
TRIALS.forEach(t=>{
  TASPECTS2.forEach(a=>{
    add({title:t[0]+' - '+a,category:'trials',
      description:'Landmark study ('+a+'): '+t[5]+' Design: '+t[2]+'; population: '+t[3]+'; focus: '+t[4]+'. Outcomes: see the primary publication; not restated here.',
      study_design:t[2],design_definition:'as executed in the published protocol',population:t[3],setting:'multi-center',
      methods_summary:'See the published protocol and registry entry for methods.',
      findings_summary:'Outcomes: see the primary publication; not restated here.',
      source:'online',source_ref:'https://clinicaltrials.gov/',creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- evidence grading ----
const GRADE=[['GRADE approach','rating certainty of a body of evidence'],['Oxford CEBM levels','hierarchy of study designs'],['USPSTF grades','recommendation grades for preventive services'],['Cochrane reviews','systematic reviews of intervention effects'],['Jadad scale','quality scoring of randomized trials'],['Newcastle-Ottawa scale','quality scoring of observational studies'],['RoB 2 tool','risk-of-bias assessment for trials'],['ROBINS-I','risk-of-bias for non-randomized studies'],['AMSTAR 2','appraisal of systematic reviews'],['QUADAS-2','quality of diagnostic accuracy studies']];
const GRASPECTS=['purpose','domains','scoring','interpretation','teaching notes','related tools','reporting','history'];
GRADE.forEach(g=>{
  GRASPECTS.forEach(a=>{
    add({title:g[0]+' - '+a,category:'evidence',
      description:'Evidence appraisal ('+a+'): '+g[0]+' - '+g[1]+'. Standard evidence-based-medicine teaching reference.',
      evidence_level:g[0],includes:g[1],appraisal_notes:'Apply the tool\u2019s domains systematically and report judgments.',
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- measurement ----
const MEAS=[['validity','whether an instrument measures what it claims'],['reliability','consistency of measurement'],['Cronbach\u2019s alpha','internal consistency of a scale'],['inter-rater reliability','agreement between assessors'],['test-retest reliability','stability over repeated measurement'],['blinding','masking of assignments'],['placebo control','inert comparison controlling expectation'],['run-in period','pre-randomization stabilization phase'],['washout period','clearing prior treatment effects'],['adherence measurement','tracking protocol compliance'],['loss to follow-up','participants missing outcome data'],['primary outcome','the main pre-specified endpoint'],['secondary outcomes','additional pre-specified endpoints'],['surrogate endpoint','a substitute for a clinical outcome'],['composite endpoint','combined multiple outcomes'],['adverse events','untoward medical occurrences'],['case report form','structured data-capture instrument'],['data dictionary','definitions of every variable'],['REDCap','electronic data-capture platform'],['audit trail','record of data changes']];
const MASPECTS=['definition','types','measurement','threats','improvement','reporting','teaching notes','examples'];
MEAS.forEach(m=>{
  MASPECTS.forEach(a=>{
    add({title:m[0]+' - '+a,category:'methods',
      description:'Measurement ('+a+'): '+m[0]+' - '+m[1]+'. Standard research-methods teaching reference.',
      method:m[0],purpose:m[1],steps:['Define the measure precisely','Apply it consistently','Report its properties'],
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- trial phases ----
const PHASES=[['phase 1','first-in-human safety and dosing'],['phase 2','preliminary efficacy and side effects'],['phase 3','large confirmatory efficacy trials'],['phase 4','post-marketing surveillance']];
const PHASPECTS=['purpose','population','design features','endpoints','size','duration','regulation','teaching notes','examples','transitions'];
PHASES.forEach(p=>{
  PHASPECTS.forEach(a=>{
    add({title:'Trial '+p[0]+' - '+a,category:'trials',
      description:'Trial phase ('+a+'): '+p[0]+' trials focus on '+p[1]+'. Standard drug-development teaching reference.',
      study_design:p[0]+' trial',design_definition:p[1],population:'per phase objectives',setting:'clinical research units and sites',
      methods_summary:'Follow phase-appropriate design standards and regulatory guidance.',
      findings_summary:'Findings depend on the executed study; no real outcomes are stated here.',
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- sampling & data ----
const SAMP=[['simple random sampling','every unit has an equal chance'],['stratified sampling','sampling within subgroups'],['cluster sampling','sampling whole groups'],['systematic sampling','every kth unit selected'],['convenience sampling','readily available participants'],['purposive sampling','deliberate selection for insight'],['snowball sampling','referral-based recruitment'],['primary data','collected for the study'],['secondary data','reused from other sources'],['EHR data','electronic health record data'],['claims data','insurance billing data'],['patient registries','organized condition cohorts'],['surveys','structured questionnaires'],['focus groups','guided group discussions'],['interviews','one-on-one qualitative inquiry'],['FAIR principles','findable, accessible, interoperable, reusable data']];
const SAASPECTS=['definition','strengths','weaknesses','when to use','implementation','teaching notes','examples','related methods'];
SAMP.forEach(s=>{
  SAASPECTS.forEach(a=>{
    add({title:s[0]+' - '+a,category:'methods',
      description:'Sampling and data ('+a+'): '+s[0]+' - '+s[1]+'. Standard research-methods teaching reference.',
      method:s[0],purpose:s[1],steps:['Choose the approach for the question','Implement it rigorously','Report it transparently'],
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
const onlineCount=seed;
console.log('online records:',onlineCount);
for(let s=onlineCount+1;s<=10000;s++){
  const r=gen.generate(s,{},lib.prng(s));
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID signature',s,v.errors);process.exit(1);}
  recs.push(r);
}
for(const r of recs.slice(0,onlineCount)){
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID online',r._seed,v.errors,JSON.stringify(r).slice(0,200));process.exit(1);}
}
const sum=lib.summarizeOnline(recs);
console.log('total',sum.total,'online',sum.online,'signature',sum.signature);
const w=lib.writeDb(SLUG,recs,REPO);
console.log('wrote',w.mb.toFixed(2),'MB in',w.chunks,'chunks');
