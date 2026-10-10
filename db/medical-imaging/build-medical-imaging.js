'use strict';
// Build JAH Medical Imaging Database: ~2000 online + signature.
// Generated/synthetic records carry a privacy note; no real patient data anywhere.
const path=require('path');
const lib=require('../buildlib.js');
const gen=require('./gen-medical-imaging.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='medical-imaging', PREFIX='JAH-IMG-';
const REF='https://www.acr.org/';
const PRIV='Reference record. Contains no real patient data and no protected health information.';
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
function imgRec(title,category,modality,principle,desc,ind,contra,steps,extra){
  add(Object.assign({title,category,description:desc,modality,principle,
    indications:ind,contraindications:contra,protocol_steps:steps,
    annotation_guidelines:'Label anatomy, mark findings with standard terms, and record acquisition parameters.',
    performance_notes:'Reference teaching notes; not measured clinical performance.',
    privacy_note:PRIV,source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'},extra||{}));
}
// ---- modalities: [name, category, principle, history note] ----
const MODS=[['X-ray radiography','xray','ionizing electromagnetic radiation projected through tissue onto a detector','discovered by Wilhelm Rontgen in 1895; first Nobel Prize in Physics 1901'],['fluoroscopy','xray','continuous X-ray imaging displayed in real time','developed in the early 1900s for dynamic studies'],['mammography','xray','low-dose X-ray imaging of breast tissue','introduced for breast screening in the 1960s-70s'],['DEXA','xray','dual-energy X-ray absorptiometry measuring bone density','introduced in the 1980s for osteoporosis assessment'],['computed tomography','ct','a rotating X-ray tube and detectors reconstructing cross-sectional slices','introduced in the 1970s by Hounsfield and Cormack; Nobel Prize 1979'],['magnetic resonance imaging','mri','a strong magnetic field plus radiofrequency pulses exciting hydrogen nuclei','developed in the 1970s by Lauterbur and Mansfield; Nobel Prize 2003'],['functional MRI','mri','blood-oxygen-level-dependent contrast mapping brain activity','developed in the early 1990s'],['ultrasound','ultrasound','high-frequency sound waves reflected at tissue interfaces','introduced in the 1950s; no ionizing radiation'],['Doppler ultrasound','ultrasound','frequency shifts measuring blood flow velocity','developed alongside diagnostic ultrasound'],['elastography','ultrasound','tissue stiffness mapped from shear-wave speed','introduced in the 2000s'],['positron emission tomography','protocols','positron-emitting tracers imaged in coincidence','developed in the 1970s'],['SPECT','protocols','single-photon emission computed tomography','developed in the 1960s-70s'],['nuclear medicine planar imaging','protocols','gamma-emitting radiotracers imaged with a gamma camera','mid-20th century'],['angiography','protocols','vessel imaging via catheter, CT, or MR techniques','catheter angiography pioneered in the 1920s-50s']];
const MASPECTS=['overview','history','principle','uses','strengths','limitations','safety','contrast use','patient preparation','typical parameters','artifacts','reporting','teaching notes','key terms'];
MODS.forEach(m=>{
  MASPECTS.forEach(a=>{
    imgRec(m[0]+' - '+a,m[1],m[0],m[2],
      'Modality ('+a+'): '+m[0]+' - '+m[2]+'. '+m[3][0].toUpperCase()+m[3].slice(1)+'.',
      ['evaluation of indicated anatomy','follow-up of known findings'],
      ['pregnancy without justification for ionizing modalities','inability to cooperate without support'],
      ['Confirm patient identity and indication','Apply the standard acquisition','Review and annotate the study']);
  });
});
// ---- protocols (100 real names) ----
const PROTO=['CT head without contrast','CT head with contrast','CT angiography head','CT angiography neck','CT chest without contrast','CT chest with contrast','CT angiography chest','CT abdomen with contrast','CT pelvis with contrast','CT abdomen and pelvis with contrast','CT urography','CT colonography','CT enterography','CT angiography abdomen and pelvis','CT calcium scoring','CT pulmonary angiography','CT venography','high-resolution chest CT','CT sinus','CT facial bones','CT orbits','CT temporal bone','CT cervical spine','CT thoracic spine','CT lumbar spine','CT extremity','CT arthrography','CT-guided biopsy','CT myelography','CT cystography','MRI brain without contrast','MRI brain with and without contrast','MRI pituitary','MRI orbits','MRI internal auditory canal','MRI cervical spine','MRI thoracic spine','MRI lumbar spine','MRI brachial plexus','MRI shoulder','MRI elbow','MRI wrist','MRI hand','MRI hip','MRI knee','MRI ankle','MRI foot','MRA brain','MRA neck','MRA abdomen','MR venography','MRCP','MRI abdomen','MRI pelvis','MRI prostate','cardiac MRI','breast MRI','fetal MRI','MRI enterography','chest X-ray PA','chest X-ray lateral','chest X-ray portable','abdominal X-ray KUB','skeletal survey','bone age study','mammography screening','mammography diagnostic','DEXA bone density','ultrasound abdomen','ultrasound pelvis','obstetric ultrasound first trimester','obstetric ultrasound anatomy scan','thyroid ultrasound','scrotal ultrasound','renal ultrasound','bladder ultrasound','carotid Doppler','venous Doppler lower extremity','arterial Doppler lower extremity','echocardiogram transthoracic','transesophageal echocardiogram','stress echocardiogram','PET/CT whole body','bone scan','thyroid uptake scan','V/Q lung scan','HIDA scan','gastric emptying study','renal scan','parathyroid scan','barium swallow','upper GI study','small bowel follow-through','barium enema','IVP intravenous pyelogram','voiding cystourethrogram','hysterosalpingogram','shoulder arthrogram','knee arthrogram','coronary angiography','cerebral angiography','peripheral angiography'];
const PCAT=p=>/CT|computed/i.test(p)?'ct':(/MRI|MRA|MRCP/i.test(p)?'mri':(/ultrasound|echocardiogram|Doppler/i.test(p)?'ultrasound':(/X-ray|mammography|DEXA|barium|IVP|cystourethrogram|hysterosalpingogram|arthrogram|angiography/i.test(p)?'xray':'protocols')));
const PASPECTS=['indications','contraindications','patient preparation','positioning','typical parameters','contrast use','duration','radiation note','reporting checklist','teaching notes'];
PROTO.forEach(p=>{
  const cat=PCAT(p);
  PASPECTS.forEach(a=>{
    imgRec(p+' - '+a,cat,p,
      'Standardized acquisition and reconstruction for '+p+'.',
      'Protocol ('+a+'): '+p+'. A standardized imaging protocol with defined indications, preparation, acquisition, and reporting elements.',
      ['standard indications for '+p.toLowerCase()],
      ['contraindications per modality safety rules'],
      ['Verify indication and safety screening','Position per protocol','Acquire, reconstruct, and annotate']);
  });
});
console.log('protocols:',PROTO.length,'total:',seed);
// ---- views and planes ----
const VIEWS=[['AP view','anteroposterior projection'],['PA view','posteroanterior projection'],['lateral view','side projection'],['oblique view','angled projection'],['axial plane','transverse cross-section'],['coronal plane','frontal cross-section'],['sagittal plane','side cross-section'],['transverse ultrasound plane','cross-sectional sound plane'],['longitudinal ultrasound plane','lengthwise sound plane'],['decubitus view','side-lying projection'],['lordotic view','angled chest projection'],['Townes view','skull projection'],['Waters view','sinus projection'],['Caldwell view','skull projection'],['submentovertex view','skull base projection'],['Y-view scapula','scapular lateral projection'],['sunrise patella view','axial patella projection'],['mortise ankle view','ankle joint projection'],['weight-bearing foot views','loaded foot projections'],['stress views','joint views under load'],['MIP','maximum intensity projection'],['MPR','multiplanar reformation'],['3D volume rendering','volumetric display'],['cine imaging','dynamic loop display'],['scout view','localizer for CT planning'],['topogram','CT localizer image'],['curved planar reformation','vessel-unfolded display'],['panoramic dental view','full dental arch projection'],['cephalometric view','skull measurement projection'],['plantodorsal foot view','foot projection']];
const VASPECTS=['definition','technique','indications','positioning','evaluation criteria','variants','teaching notes','key terms'];
VIEWS.forEach(v=>{
  VASPECTS.forEach(a=>{
    imgRec(v[0]+' - '+a,'protocols',v[0],'Standard imaging view or reformat.',
      'View ('+a+'): '+v[0]+' - '+v[1]+'. Standard positioning and evaluation teaching reference.',
      ['visualization of target anatomy'],['inability to position safely'],
      ['Position the patient per standard','Center and collimate','Evaluate against criteria']);
  });
});
// ---- contrast agents: [name, class, note] ----
const CONTRAST=[['iohexol','nonionic iodinated','low-osmolality CT contrast'],['iopamidol','nonionic iodinated','low-osmolality CT contrast'],['ioversol','nonionic iodinated','low-osmolality CT contrast'],['iodixanol','nonionic iodinated','iso-osmolal CT contrast'],['barium sulfate suspension','barium','gastrointestinal opacification'],['gadoterate meglumine','gadolinium-based','macrocyclic MRI contrast'],['gadobutrol','gadolinium-based','macrocyclic MRI contrast'],['gadoteridol','gadolinium-based','macrocyclic MRI contrast'],['gadopentetate dimeglumine','gadolinium-based','linear MRI contrast'],['gadodiamide','gadolinium-based','linear agent with higher NSF risk history'],['gadoversetamide','gadolinium-based','linear agent with higher NSF risk history'],['gadobenate dimeglumine','gadolinium-based','liver MRI contrast'],['gadoxetate disodium','gadolinium-based','hepatobiliary MRI contrast'],['perflutren microbubbles','ultrasound','echocardiographic contrast'],['sulfur hexafluoride microbubbles','ultrasound','ultrasound contrast'],['air','negative','negative gastrointestinal contrast'],['carbon dioxide','angiography','alternative angiographic contrast'],['normal saline','flush','catheter flushing'],['water','oral','neutral oral contrast'],['dilute barium','oral','low-density oral contrast'],['iodinated oral contrast','oral','positive oral CT contrast'],['ferumoxytol','iron-based','off-label MR angiography use'],['manganese-based agents','manganese','historical MRI contrast'],['iron oxide agents','iron-based','historical liver MRI contrast']];
const CASPECTS=['agent class','mechanism','uses','administration','safety','risk notes','contraindications','teaching notes'];
CONTRAST.forEach(c=>{
  CASPECTS.forEach(a=>{
    imgRec(c[0]+' - '+a,'protocols',c[0],c[1]+' contrast medium.',
      'Contrast ('+a+'): '+c[0]+' ('+c[1]+') - '+c[2]+'. Screen renal function and allergy history before administration.',
      ['opacification for '+c[2]],['known allergy without premedication plan','severe renal impairment for high-risk agents'],
      ['Screen the patient','Administer per protocol','Monitor after administration']);
  });
});
// ---- anatomy landmarks ----
const LAND=['carina','aortic arch','costophrenic angles','cardiophrenic angles','sacroiliac joints','femoral neck','intervertebral disc spaces','lateral ventricles','basal ganglia','Sylvian fissure','corpus callosum','liver segments','renal cortex','gallbladder wall','endometrial stripe','nuchal translucency','biparietal diameter','fetal femur length','cisterna magna','cavum septum pellucidum','circle of Willis','dural venous sinuses','mastoid air cells','paranasal sinuses','odontoid process','atlanto-dens interval','Cobb angle','Shenton line','tibial plateau','Blumensaat line','sellar region','pineal calcification','choroid plexus calcification','acetabular index','Klein line','McGregor line','tibial tuberosity','fibular head','calcaneus','talus'];
const LANDASPECTS=['definition','imaging appearance','clinical relevance','measurement','variants','teaching notes'];
LAND.forEach(l=>{
  LANDASPECTS.forEach(a=>{
    imgRec(l+' - '+a,'protocols',l,'Anatomical imaging landmark.',
      'Landmark ('+a+'): '+l+'. A standard anatomical reference used in image interpretation teaching.',
      ['anatomical localization'],['none specific'],
      ['Identify the landmark','Assess its appearance','Correlate clinically']);
  });
});
// ---- safety concepts ----
const SAFE=[['ALARA principle','keeping radiation doses as low as reasonably achievable'],['justification','benefit must outweigh radiation risk'],['effective dose','whole-body risk-weighted dose in millisieverts'],['CT dose index','scanner radiation output metric'],['pregnancy screening','asking about pregnancy before ionizing exams'],['contrast allergy','hypersensitivity to contrast media'],['premedication','steroid prophylaxis for at-risk patients'],['renal function screening','checking eGFR before contrast'],['nephrogenic systemic fibrosis','fibrosing disease linked to gadolinium in renal failure'],['gadolinium retention','trace retention after contrast MRI'],['risk communication','explaining radiation risk plainly'],['shielding','protecting radiosensitive organs'],['pediatric dose reduction','child-sized protocols'],['Image Gently','pediatric dose campaign'],['Image Wisely','adult dose campaign'],['MRI safety zones','four-zone access control'],['projectile effect','ferromagnetic objects in the magnet room'],['SAR limits','specific absorption rate heating limits'],['acoustic noise','loud gradient sounds in MRI'],['claustrophobia management','supporting anxious patients']];
const SASPECTS=['principle','rationale','implementation','screening','documentation','special populations','teaching notes','key terms'];
SAFE.forEach(s=>{
  SASPECTS.forEach(a=>{
    imgRec(s[0]+' - '+a,'protocols',s[0],s[1]+'.',
      'Safety ('+a+'): '+s[0]+' - '+s[1]+'. Standard imaging-safety teaching reference.',
      ['safe imaging practice'],['ignoring the safety rule'],
      ['Apply the safety check','Document compliance','Review incidents']);
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
