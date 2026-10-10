/* ✳ SIGNATURE — JAH Pharmacology Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic client-side generator: same seed + same version => same record.
   Anchor facts (drug classes, mechanisms of action, example drugs, therapeutic
   uses) verified from published pharmacology references. EDUCATIONAL mechanism
   data only — no dosage instructions anywhere in this database. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['cardiovascular','antibiotics','analgesics','cns-drugs','endocrine','gastrointestinal','respiratory','oncology','biologics','antimicrobials'];
var PREFIX='JAH-PHR-';
var EDU='Educational reference only; not medical advice. No dosage information is stored in this database.';
/* [drug class, category, mechanism of action, [example drugs], [therapeutic uses], naming suffix hint, year anchor (0 = none)] */
var ANCH=[
['Beta blockers','cardiovascular','block beta-adrenergic receptors, lowering heart rate, contractility, and blood pressure',['propranolol','metoprolol','atenolol'],['hypertension','arrhythmias','migraine prevention'],'-olol',0],
['ACE inhibitors','cardiovascular','block angiotensin-converting enzyme, preventing angiotensin I to angiotensin II conversion; bradykinin buildup can cause a dry cough',['lisinopril','captopril','enalapril'],['hypertension','heart failure','diabetic kidney protection'],'-pril',0],
['Angiotensin II receptor blockers (ARBs)','cardiovascular','block angiotensin II receptors directly, without affecting bradykinin levels',['losartan','valsartan','irbesartan'],['hypertension','heart failure','diabetic kidney disease'],'-sartan',0],
['Calcium channel blockers','cardiovascular','block calcium entry into heart and vessel cells, relaxing blood vessels',['amlodipine','nifedipine','verapamil'],['hypertension','angina','arrhythmias'],'-dipine',0],
['Statins','cardiovascular','inhibit HMG-CoA reductase, the rate-limiting enzyme of cholesterol synthesis in the liver',['atorvastatin','simvastatin','rosuvastatin'],['high cholesterol','heart attack prevention','stroke prevention'],'-statin',0],
['Loop diuretics','cardiovascular','block sodium reabsorption in the kidney\u2019s loop of Henle, increasing urine output',['furosemide','bumetanide','torsemide'],['heart failure','edema','hypertension'],'-semide',0],
['Antiplatelet drugs','cardiovascular','prevent platelet aggregation; aspirin blocks thromboxane production and clopidogrel blocks ADP receptors',['aspirin','clopidogrel','ticagrelor'],['heart attack prevention','stroke prevention','stent protection'],'',0],
['Anticoagulants','cardiovascular','interrupt the blood-clotting cascade; warfarin antagonizes vitamin K',['warfarin','heparin','apixaban'],['atrial fibrillation','deep vein thrombosis','pulmonary embolism'],'',0],
['Nitrates','cardiovascular','release nitric oxide, dilating coronary vessels and easing the heart\u2019s workload',['nitroglycerin','isosorbide dinitrate','isosorbide mononitrate'],['angina','heart failure'],'',0],
['Penicillins','antibiotics','beta-lactam antibiotics that block bacterial cell-wall synthesis; discovered by Alexander Fleming in 1928 and mass-produced from 1942',['penicillin G','amoxicillin','flucloxacillin'],['strep throat','syphilis','skin infections'],'',1928],
['Cephalosporins','antibiotics','beta-lactam antibiotics related to penicillins that disrupt cell-wall synthesis, in generations of widening spectrum',['cephalexin','ceftriaxone','cefepime'],['pneumonia','urinary infections','surgical prophylaxis'],'-cef-',0],
['Macrolides','antibiotics','bind the bacterial 50S ribosomal subunit, blocking protein synthesis',['azithromycin','erythromycin','clarithromycin'],['respiratory infections','atypical pneumonia','certain STIs'],'-thromycin',0],
['Tetracyclines','antibiotics','bind the bacterial 30S ribosomal subunit, blocking protein synthesis; broad spectrum',['doxycycline','tetracycline','minocycline'],['acne','Lyme disease','respiratory infections'],'-cycline',0],
['Fluoroquinolones','antibiotics','inhibit bacterial DNA gyrase and topoisomerase, blocking DNA replication',['ciprofloxacin','levofloxacin','moxifloxacin'],['urinary infections','anthrax exposure','pneumonia'],'-floxacin',0],
['NSAIDs','analgesics','inhibit cyclooxygenase (COX) enzymes, reducing prostaglandin production and thus pain, fever, and inflammation',['ibuprofen','naproxen','diclofenac'],['pain','fever','arthritis inflammation'],'',0],
['Acetaminophen (paracetamol)','analgesics','reduces pain and fever, acting mainly in the central nervous system',['acetaminophen','paracetamol'],['mild-to-moderate pain','fever reduction'],'',0],
['Opioid analgesics','analgesics','activate opioid receptors in the brain and spinal cord, reducing pain perception',['morphine','codeine','oxycodone'],['severe pain','post-surgical pain','palliative care'],'',0],
['Local anesthetics','analgesics','block voltage-gated sodium channels in nerves, preventing pain-signal conduction',['lidocaine','bupivacaine','procaine'],['dental procedures','minor surgery','epidural anesthesia'],'-caine',0],
['SSRIs','cns-drugs','selectively block serotonin reuptake, increasing serotonin signaling between neurons',['fluoxetine','sertraline','escitalopram'],['depression','anxiety disorders','obsessive-compulsive disorder'],'',0],
['Benzodiazepines','cns-drugs','enhance GABA activity at its receptor, calming excessive neural activity',['diazepam','lorazepam','alprazolam'],['anxiety','seizures','muscle spasm'],'-zepam',0],
['Antipsychotics','cns-drugs','block dopamine D2 receptors, reducing psychotic symptoms',['haloperidol','risperidone','olanzapine'],['schizophrenia','bipolar mania','severe agitation'],'',0],
['ADHD stimulants','cns-drugs','increase dopamine and norepinephrine signaling, improving focus and impulse control',['methylphenidate','amphetamine','lisdexamfetamine'],['ADHD','narcolepsy'],'',0],
['Anticonvulsants','cns-drugs','reduce abnormal electrical activity in the brain to prevent seizures',['valproate','lamotrigine','levetiracetam'],['epilepsy','bipolar disorder','neuropathic pain'],'',0],
['General anesthetics','cns-drugs','produce reversible unconsciousness and insensitivity to pain for surgery',['propofol','sevoflurane','ketamine'],['surgery','procedural sedation'],'',0],
['Insulin','endocrine','increases glucose uptake into cells, lowering blood sugar',['insulin glargine','insulin lispro','regular insulin'],['type 1 diabetes','type 2 diabetes','diabetic emergencies'],'',0],
['Metformin','endocrine','decreases glucose production in the liver and improves insulin sensitivity',['metformin','metformin extended-release'],['type 2 diabetes'],'',0],
['Sulfonylureas','endocrine','stimulate the pancreas to release more insulin',['glipizide','glyburide','glimepiride'],['type 2 diabetes'],'',0],
['Thyroid hormones','endocrine','replace deficient natural thyroid hormone with synthetic T4/T3',['levothyroxine','liothyronine'],['hypothyroidism'],'',0],
['Corticosteroids','endocrine','suppress inflammation and immune responses by mimicking cortisol',['prednisone','dexamethasone','hydrocortisone'],['asthma flares','autoimmune disease','allergic reactions'],'',0],
['Proton pump inhibitors (PPIs)','gastrointestinal','irreversibly block the stomach\u2019s proton pumps (H+/K+ ATPase), strongly reducing acid secretion',['omeprazole','esomeprazole','pantoprazole'],['GERD','ulcers','heartburn'],'-prazole',0],
['H2 blockers','gastrointestinal','block histamine H2 receptors in the stomach, reducing acid secretion',['famotidine','cimetidine','nizatidine'],['heartburn','ulcers','GERD'],'-tidine',0],
['Antacids','gastrointestinal','neutralize stomach acid directly on contact',['calcium carbonate','magnesium hydroxide','aluminum hydroxide'],['heartburn','indigestion'],'',0],
['Beta-2 agonists','respiratory','stimulate beta-2 receptors in the airways, relaxing bronchial smooth muscle',['albuterol','salmeterol','formoterol'],['asthma attacks','COPD','bronchospasm'],'',0],
['Inhaled corticosteroids','respiratory','reduce airway inflammation when inhaled directly into the lungs',['fluticasone','budesonide','beclomethasone'],['asthma control','COPD'],'',0],
['Leukotriene blockers','respiratory','block leukotriene receptors, reducing airway inflammation and constriction',['montelukast','zafirlukast'],['asthma','allergic rhinitis'],'-lukast',0],
['H1 antihistamines','respiratory','block histamine H1 receptors, easing allergy symptoms',['cetirizine','loratadine','diphenhydramine'],['hay fever','hives','itching'],'',0],
['Alkylating chemotherapy','oncology','damage cancer-cell DNA, preventing replication',['cyclophosphamide','cisplatin','temozolomide'],['lymphoma','solid tumors','conditioning regimens'],'',0],
['Antimetabolites','oncology','mimic cell building blocks, sabotaging DNA synthesis in dividing cells',['methotrexate','5-fluorouracil','cytarabine'],['leukemia','breast cancer','colon cancer'],'',0],
['HER2-targeted therapy','oncology','antibodies that block the HER2 growth receptor on cancer cells',['trastuzumab','pertuzumab'],['HER2-positive breast cancer','gastric cancer'],'-mab',0],
['TNF blockers','biologics','monoclonal antibodies that neutralize tumor necrosis factor, a key inflammation cytokine',['adalimumab','etanercept','infliximab'],['rheumatoid arthritis','Crohn\u2019s disease','psoriasis'],'-mab',0],
['Vaccines (as medicines)','biologics','train the immune system with antigens, preventing disease before exposure',['influenza vaccine','MMR vaccine','HPV vaccine'],['infectious disease prevention'],'',0],
['Antifungals','antimicrobials','disrupt fungal cell membranes or cell walls',['fluconazole','amphotericin B','terbinafine'],['yeast infections','systemic mycoses','athlete\u2019s foot'],'-azole',0],
['Antivirals','antimicrobials','block viral replication steps such as entry, reverse transcription, or protease cleavage',['oseltamivir','acyclovir','tenofovir'],['influenza','herpes infections','HIV'],'',0],
['Antimalarials','antimicrobials','kill malaria parasites in their blood stages',['chloroquine','artemisinin','mefloquine'],['malaria treatment','malaria prevention'],'',0]
];
var ASPECTS=['overview','mechanism deep-dive','therapeutic uses','naming and classes','safety profile','comparative analysis'];
var CONTEXTS=['formulary review','clinical education module','pharmacology survey','therapeutic class study','medication safety review','prescribing reference study'];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ANCH.filter(function(a){return a[1]===cat;});
  if(!pool.length)pool=ANCH;
  var a=pick(pool,rnd);
  var mode=rnd()<0.45?'profile':'study';
  var aspect=pick(ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var serial='R-'+(10000+seed);
  var title,desc,src,code=null,ex=a[3].slice(),us=a[4].slice();
  if(mode==='profile'){
    code=serial;
    title=a[0]+': '+aspect+' ('+serial+')';
    var s1=a[0]+' '+(a[6]>0?'were introduced in '+a[6]+' and ':'')+'are drugs whose mechanism of action is: '+a[2]+'.';
    var s2='Example drugs include '+a[3].join(', ')+'.';
    var s3='Therapeutic uses include '+a[4].join(', ')+'.';
    var s4=a[5]?('Naming hint: members of this class often carry the suffix '+a[5]+'.'):'This class has no single naming suffix.';
    if(aspect==='mechanism deep-dive')desc=s1+' '+s2+' The mechanism is what unites every member of this class. '+s3;
    else if(aspect==='therapeutic uses')desc=s1+' '+s3+' Prescribers choose this class when these conditions call for its mechanism. '+s2;
    else if(aspect==='naming and classes')desc=s1+' '+s4+' '+s2;
    else if(aspect==='safety profile')desc=s1+' '+s2+' Like all medicines, this class carries risks and interactions that clinicians weigh before use. '+s3+' '+EDU;
    else if(aspect==='comparative analysis')desc=s1+' Compared with related classes, '+a[0]+' are distinguished by this mechanism: '+a[2]+' '+s3;
    else desc=s1+' '+s2+' '+s3+' '+s4;
    src='online';
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=pick(CONTEXTS,rnd);
    var n=ri(rnd,20,1500),yr=ri(rnd,2016,2026);
    title=a[0]+' \u2014 '+ctx+' '+code;
    desc='This generated study ('+code+', compiled '+yr+') surveys '+n.toLocaleString('en-US')+' published references on '+a[0]+' for a '+ctx+'. '+
      'The established facts remain: '+a[2]+' '+
      'Example drugs covered include '+a[3].slice(0,2).join(' and ')+'; therapeutic uses surveyed include '+a[4].slice(0,2).join(' and ')+'. '+
      'As a Signature-generated study record, the survey scenario is illustrative; the class facts come from published pharmacology. '+EDU;
    src='signature';ex=[a[3][0],a[3][1]||a[3][0]];us=[a[4][0],ctx+' (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{drug_class:a[0],mechanism:a[2],category:a[1],example_drugs:ex,therapeutic_uses:us,suffix_hint:a[5]||null,year_anchor:a[6]||null,aspect:aspect,study_code:code,educational:EDU},
    src:src,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PHR-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>160)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  else{var parts=r.description.split('. ');if(parts.length<2)e.push('description-sentences');if(!/\.$/.test(r.description.trim()))e.push('description-period');
    var nodesc=r.description.split(EDU)[0];
    if(/\btake \d+|\bgive \d+|\d+\s?mg\b|\d+\s?mcg\b|twice daily|three times daily|\d+-\d+\s?mg/i.test(nodesc))e.push('description-dosage');}
  var s0=JSON.stringify(r);
  if(/take \d+ tablets|\d+\s?mg per dose|dosing schedule/i.test(s0))e.push('dosage-content');
  if(CATS.indexOf(r.category)<0)e.push('category');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(!s.drug_class||typeof s.drug_class!=='string')e.push('spec.drug_class');
    if(!s.mechanism||typeof s.mechanism!=='string')e.push('spec.mechanism');
    if(!Array.isArray(s.example_drugs)||s.example_drugs.length<2||s.example_drugs.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.example_drugs');
    if(!Array.isArray(s.therapeutic_uses)||!s.therapeutic_uses.length||s.therapeutic_uses.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.therapeutic_uses');
    if(!(s.year_anchor===null||(Number.isInteger(s.year_anchor)&&s.year_anchor>=1500&&s.year_anchor<=2026)))e.push('spec.year_anchor');
    if(s.educational!==EDU)e.push('spec.educational');
  }
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-pharmacology-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pharmacology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
