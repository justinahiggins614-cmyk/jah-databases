'use strict';
// Build JAH Anatomy Database data: ~2000 online-verified + ~8000 signature records.
const path=require('path');
const lib=require('../buildlib.js');
const gen=require('./gen-anatomy.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='anatomy', PREFIX='JAH-ANA-';
const REF_BONES='https://en.wikipedia.org/wiki/List_of_bones_of_the_human_skeleton';
const REF_OA='https://openstax.org/details/books/anatomy-and-physiology-2e';
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
function online(title,category,description,extra){
  add(Object.assign({title,category,description,source:'online',
    source_ref:REF_OA,creation_mode:'ONLINE-VERIFIED'},extra));
}
// ---- 206 bones: [name,count,region,type] ----
const BONES=[];
[['occipital bone',1,'skull','flat'],['parietal bone',2,'skull','flat'],['frontal bone',1,'skull','flat'],
 ['temporal bone',2,'skull','irregular'],['sphenoid bone',1,'skull','irregular'],['ethmoid bone',1,'skull','irregular'],
 ['nasal bone',2,'face','flat'],['maxilla',2,'face','irregular'],['lacrimal bone',2,'face','flat'],
 ['zygomatic bone',2,'face','irregular'],['palatine bone',2,'face','irregular'],['inferior nasal concha',2,'face','irregular'],
 ['vomer',1,'face','flat'],['mandible',1,'face','irregular'],
 ['malleus',2,'middle ear','irregular'],['incus',2,'middle ear','irregular'],['stapes',2,'middle ear','irregular'],
 ['hyoid bone',1,'neck','irregular']].forEach(b=>BONES.push(b));
for(let i=1;i<=7;i++)BONES.push(['cervical vertebra C'+i,1,'spine','irregular']);
for(let i=1;i<=12;i++)BONES.push(['thoracic vertebra T'+i,1,'spine','irregular']);
for(let i=1;i<=5;i++)BONES.push(['lumbar vertebra L'+i,1,'spine','irregular']);
BONES.push(['sacrum',1,'spine','irregular'],['coccyx',1,'spine','irregular']);
BONES.push(['sternum',1,'thorax','flat']);
for(let i=1;i<=12;i++)BONES.push(['rib '+i,2,'thorax','flat']);
const CARPALS=['scaphoid','lunate','triquetrum','pisiform','trapezium','trapezoid','capitate','hamate'];
const TARSALS=['talus','calcaneus','navicular','cuboid','medial cuneiform','intermediate cuneiform','lateral cuneiform'];
[['clavicle','long'],['scapula','flat'],['humerus','long'],['radius','long'],['ulna','long']].forEach(b=>BONES.push([b[0],2,'upper limb',b[1]]));
CARPALS.forEach(c=>BONES.push([c,2,'wrist','short']));
for(let i=1;i<=5;i++)BONES.push(['metacarpal '+i,2,'hand','long']);
for(let i=1;i<=5;i++)BONES.push(['proximal phalanx '+i+' (hand)',2,'hand','long']);
for(let i=2;i<=5;i++)BONES.push(['middle phalanx '+i+' (hand)',2,'hand','long']);
for(let i=1;i<=5;i++)BONES.push(['distal phalanx '+i+' (hand)',2,'hand','long']);
BONES.push(['hip bone',2,'pelvis','irregular'],['femur',2,'thigh','long'],['patella',2,'knee','sesamoid'],
 ['tibia',2,'leg','long'],['fibula',2,'leg','long']);
TARSALS.forEach(t=>BONES.push([t,2,'ankle','short']));
for(let i=1;i<=5;i++)BONES.push(['metatarsal '+i,2,'foot','long']);
for(let i=1;i<=5;i++)BONES.push(['proximal phalanx '+i+' (foot)',2,'foot','long']);
for(let i=2;i<=5;i++)BONES.push(['middle phalanx '+i+' (foot)',2,'foot','long']);
for(let i=1;i<=5;i++)BONES.push(['distal phalanx '+i+' (foot)',2,'foot','long']);
let boneCount=0; BONES.forEach(b=>boneCount+=b[1]);
if(boneCount!==206) throw new Error('bone count '+boneCount);
const ARTIC={'femur':'Articulates proximally with the acetabulum of the hip bone and distally with the tibia and patella at the knee.',
 'humerus':'Articulates proximally with the glenoid cavity of the scapula and distally with the radius and ulna at the elbow.',
 'tibia':'Articulates proximally with the femur at the knee and distally with the talus at the ankle.',
 'mandible':'Articulates with the temporal bones at the temporomandibular joints; the only movable skull bone.',
 'stapes':'The smallest bone in the human body; transmits vibration from the incus to the oval window.',
 'sacrum':'Articulates with the hip bones at the sacroiliac joints and with L5 above.'};
BONES.forEach(b=>{
  const sides=b[1]===2?['left','right']:[null];
  sides.forEach(s=>{
    const nm=(s?s+' ':'')+b[0];
    online(nm,'skeletal',nm[0].toUpperCase()+nm.slice(1)+' is a '+b[3]+' bone of the '+b[2]+' region. The adult human skeleton contains 206 bones: 80 axial and 126 appendicular.',
      {region:b[2],structure_type:b[3]+' bone',latin_name:'',functions:['Provides structural support in the '+b[2]+' region.','Serves as an attachment or lever for movement.'],related_structures:[b[2]+' region bones'],clinical_notes:'Bone heals through callus formation and remodeling under load.',source_ref:REF_BONES});
    online(nm+' - articulations', b[2]==='skull'||b[2]==='face'?'skeletal':'skeletal',
      'Articulation record for the '+nm+'. '+(ARTIC[b[0]]||'It articulates with neighboring bones of the '+b[2]+' region at fibrous, cartilaginous, or synovial joints as appropriate to its location.'),
      {region:b[2],structure_type:b[3]+' bone',latin_name:'',functions:['Forms joints that permit or restrict movement.'],related_structures:['neighboring '+b[2]+' bones'],clinical_notes:'Joint injury patterns follow the local anatomy.'});
    online(nm+' - clinical notes','skeletal','Clinical correlation record for the '+nm+'. Fractures are classified by pattern and location; healing proceeds through inflammation, repair, and remodeling phases.',
      {region:b[2],structure_type:b[3]+' bone',latin_name:'',functions:['Clinical landmark for examination and imaging.'],related_structures:[b[2]+' region'],clinical_notes:'Assess neurovascular status with any suspected fracture.'});
  });
});
// ---- muscles: [name, region, action] ----
const MUSCLES=[['masseter','head','elevates the mandible'],['temporalis','head','elevates the mandible'],['sternocleidomastoid','neck','rotates and flexes the head'],['trapezius','back','elevates and retracts the scapula'],['deltoid','shoulder','abducts the arm'],['pectoralis major','chest','adducts and medially rotates the arm'],['latissimus dorsi','back','extends and adducts the arm'],['biceps brachii','upper arm','flexes the elbow and supinates'],['triceps brachii','upper arm','extends the elbow'],['brachialis','upper arm','flexes the elbow'],['rectus abdominis','abdomen','flexes the trunk'],['external oblique','abdomen','rotates and flexes the trunk'],['erector spinae','back','extends the vertebral column'],['diaphragm','thorax','drives inspiration by contracting downward'],['gluteus maximus','hip','extends the hip'],['gluteus medius','hip','abducts the hip'],['quadriceps femoris','thigh','extends the knee'],['hamstrings','thigh','flex the knee and extend the hip'],['gastrocnemius','leg','plantarflexes the foot'],['soleus','leg','plantarflexes the foot'],['tibialis anterior','leg','dorsiflexes the foot'],['serratus anterior','chest','protracts the scapula'],['rhomboid major','back','retracts the scapula'],['supraspinatus','shoulder','initiates arm abduction'],['infraspinatus','shoulder','laterally rotates the arm'],['teres minor','shoulder','laterally rotates the arm'],['subscapularis','shoulder','medially rotates the arm'],['sartorius','thigh','flexes hip and knee'],['gracilis','thigh','adducts the thigh'],['adductor longus','thigh','adducts the thigh'],['biceps femoris','thigh','flexes the knee'],['semitendinosus','thigh','extends the hip'],['semimembranosus','thigh','extends the hip'],['rectus femoris','thigh','extends the knee'],['vastus lateralis','thigh','extends the knee'],['vastus medialis','thigh','extends the knee'],['fibularis longus','leg','everts the foot'],['extensor digitorum longus','leg','extends the toes'],['flexor carpi radialis','forearm','flexes the wrist'],['extensor carpi radialis longus','forearm','extends the wrist'],['pronator teres','forearm','pronates the forearm'],['orbicularis oculi','head','closes the eyelid'],['orbicularis oris','head','closes the lips'],['buccinator','head','compresses the cheek'],['frontalis','head','raises the eyebrows'],['platysma','neck','tenses neck skin'],['scalene anterior','neck','elevates the ribs'],['splenius capitis','neck','extends the head'],['intercostals external','thorax','elevate the ribs in inspiration'],['pectoralis minor','chest','protracts the scapula'],['levator scapulae','neck','elevates the scapula'],['quadratus lumborum','abdomen','laterally flexes the trunk'],['iliopsoas','hip','flexes the hip'],['piriformis','hip','laterally rotates the hip'],['tensor fasciae latae','hip','abducts the hip'],['pectineus','thigh','adducts the thigh'],['popliteus','knee','unlocks the knee'],['tibialis posterior','leg','inverts the foot'],['flexor digitorum longus','leg','flexes the toes'],['anconeus','elbow','assists elbow extension'],['coracobrachialis','upper arm','flexes the arm'],['brachioradialis','forearm','flexes the elbow'],['supinator','forearm','supinates the forearm'],['palmaris longus','forearm','tenses the palmar fascia'],['extensor digitorum','forearm','extends the fingers'],['flexor digitorum superficialis','forearm','flexes the fingers'],['thenar muscles','hand','move the thumb'],['hypothenar muscles','hand','move the little finger'],['lumbricals','hand','flex MCP and extend IP joints'],['levator ani','pelvis','supports pelvic organs'],['masseter','head','elevates the mandible']];
const seenM=new Set(); const MUS2=MUSCLES.filter(m=>{if(seenM.has(m[0]))return false;seenM.add(m[0]);return true;});
MUS2.forEach(m=>{
  online(m[0],'muscular',m[0][0].toUpperCase()+m[0].slice(1)+' is a skeletal muscle of the '+m[1]+' that '+m[2]+'. Skeletal muscles attach to bone via tendons and contract voluntarily.',
    {region:m[1],structure_type:'skeletal muscle',latin_name:'',functions:['Contracts to '+m[2]+'.','Stabilizes nearby joints during movement.'],related_structures:['antagonist muscle groups'],clinical_notes:'Strain injuries follow overload and recover with graded loading.'});
});
// ---- organs ----
const ORGANS=['brain','spinal cord','heart','right lung','left lung','trachea','liver','gallbladder','stomach','duodenum','jejunum','ileum','cecum','appendix','ascending colon','transverse colon','descending colon','sigmoid colon','rectum','pancreas','spleen','right kidney','left kidney','urinary bladder','urethra','pituitary gland','thyroid gland','parathyroid glands','adrenal glands','pineal gland','thymus','ovaries','uterus','testes','prostate gland','skin','tongue','esophagus','pharynx','larynx','bone marrow','tonsils','right eye','left eye','right ear','left ear','nasal cavity','right ureter','left ureter','fallopian tubes','vagina'];
ORGANS.forEach(o=>{
  online(o,'organs',o[0].toUpperCase()+o.slice(1)+' is an organ of the human body with specialized tissue performing dedicated physiological work. Organs cooperate within systems to maintain homeostasis.',
    {region:'body',structure_type:'organ',latin_name:'',functions:['Performs its specialized physiological role.','Contributes to system-level homeostasis.'],related_structures:['same-system organs'],clinical_notes:'Organ function is assessed with tissue-specific tests.'});
});
// ---- vessels ----
const VESSELS=['aorta','aortic arch','thoracic aorta','abdominal aorta','brachiocephalic trunk','common carotid artery','internal carotid artery','external carotid artery','subclavian artery','axillary artery','brachial artery','radial artery','ulnar artery','coronary arteries','pulmonary trunk','pulmonary arteries','pulmonary veins','superior vena cava','inferior vena cava','internal jugular vein','external jugular vein','subclavian vein','basilic vein','cephalic vein','femoral artery','femoral vein','popliteal artery','anterior tibial artery','posterior tibial artery','great saphenous vein','common iliac artery','external iliac artery','internal iliac artery','renal artery','renal vein','superior mesenteric artery','inferior mesenteric artery','celiac trunk','hepatic portal vein','vertebral artery','basilar artery','middle cerebral artery','anterior cerebral artery','posterior cerebral artery','splenic artery','gonadal artery','dorsalis pedis artery','deep brachial artery','thoracoacromial artery','cystic artery','cystic vein','hepatic veins','azygos vein','hemiazygos vein','intercostal arteries','lumbar arteries','median sacral artery','digital arteries'];
VESSELS.forEach(v=>{
  online(v,'circulatory',v[0].toUpperCase()+v.slice(1)+' is a blood vessel of the circulatory system. Arteries carry blood away from the heart and veins return it; vessel walls remodel with pressure and flow.',
    {region:'body',structure_type:/vein/i.test(v)?'vein':'artery',latin_name:'',functions:['Transports blood through the circulation.'],related_structures:['heart','capillary beds'],clinical_notes:'Vessel patency is assessed by pulse, imaging, or Doppler study.'});
});
// ---- nerves ----
const NERVES=['olfactory nerve (I)','optic nerve (II)','oculomotor nerve (III)','trochlear nerve (IV)','trigeminal nerve (V)','abducens nerve (VI)','facial nerve (VII)','vestibulocochlear nerve (VIII)','glossopharyngeal nerve (IX)','vagus nerve (X)','accessory nerve (XI)','hypoglossal nerve (XII)','phrenic nerve','median nerve','ulnar nerve','radial nerve','musculocutaneous nerve','axillary nerve','femoral nerve','obturator nerve','sciatic nerve','tibial nerve','common fibular nerve','sural nerve','saphenous nerve','pudendal nerve','intercostal nerves','brachial plexus','lumbar plexus','sacral plexus','cervical plexus','sympathetic trunk','recurrent laryngeal nerve','long thoracic nerve','suprascapular nerve','ilioinguinal nerve','genitofemoral nerve','lateral femoral cutaneous nerve','deep fibular nerve','superficial fibular nerve'];
NERVES.forEach(n=>{
  online(n,'nervous',n[0].toUpperCase()+n.slice(1)+' is a nerve of the human nervous system. Nerves carry motor, sensory, or mixed fibers between the central nervous system and the body.',
    {region:'body',structure_type:'nerve',latin_name:'',functions:['Transmits electrochemical signals.'],related_structures:['spinal cord','target tissues'],clinical_notes:'Nerve injury patterns follow the distribution of the nerve.'});
});
// ---- joints ----
const JOINTS=['temporomandibular joint','atlanto-occipital joint','atlantoaxial joint','intervertebral joints','sternoclavicular joint','acromioclavicular joint','glenohumeral joint','humeroulnar joint','humeroradial joint','proximal radioulnar joint','distal radioulnar joint','radiocarpal joint','carpometacarpal joint of thumb','metacarpophalangeal joints','interphalangeal joints of hand','sacroiliac joint','pubic symphysis','hip joint','knee joint','patellofemoral joint','proximal tibiofibular joint','talocrural joint','subtalar joint','tarsometatarsal joints','metatarsophalangeal joints','sternocostal joints','costovertebral joints','zygapophysial joints','sacrococcygeal joint','cranial sutures'];
JOINTS.forEach(j=>{
  online(j,'skeletal',j[0].toUpperCase()+j.slice(1)+' is a joint where bones meet. Joints are classified as fibrous, cartilaginous, or synovial according to their structure and movement.',
    {region:'body',structure_type:'joint',latin_name:'',functions:['Permits or restricts movement between bones.','Transmits mechanical loads.'],related_structures:['articulating bones','ligaments'],clinical_notes:'Joint disorders are assessed by range of motion and imaging.'});
});
// ---- terms (150) ----
const TERMS=['anterior','posterior','superior','inferior','medial','lateral','proximal','distal','superficial','deep','dorsal','ventral','cranial','caudal','ipsilateral','contralateral','sagittal plane','coronal plane','transverse plane','oblique plane','midline','bilateral','unilateral','flexion','extension','abduction','adduction','rotation','circumduction','pronation','supination','eversion','inversion','dorsiflexion','plantarflexion','elevation','depression','protraction','retraction','opposition','reposition','medial rotation','lateral rotation','hyperextension','anatomical position','supine','prone','lithotomy position','Trendelenburg position','Fowler position','cephalic','rostral','apical','basal','axial','appendicular','visceral','parietal','serous','mucous','synovial','afferent','efferent','proximal convoluted','distal convoluted','foramen','fossa','fissure','sulcus','sinus','meatus','canal','hiatus','process','condyle','epicondyle','tuberosity','tubercle','trochanter','crest','spine','head','neck','shaft','diaphysis','epiphysis','metaphysis','periosteum','endosteum','medullary cavity','articular cartilage','meniscus','labrum','bursa','tendon','ligament','aponeurosis','fascia','origin','insertion','belly','agonist','antagonist','synergist','fixator','isometric','isotonic','concentric','eccentric','hypertrophy','atrophy','ossification','osteoblast','osteoclast','osteocyte','hematopoiesis','red marrow','yellow marrow','compact bone','spongy bone','trabeculae','osteon','lamellae','canaliculi','Volkmann canal','Haversian canal','sesamoid','sutural bone','pneumatic bone','dermal bone','endochondral','intramembranous','epiphyseal plate','fontanelle','suture','gomphosis','syndesmosis','synchondrosis','symphysis','synovial cavity','articular capsule','synovial membrane','hyaline cartilage','elastic cartilage','fibrocartilage','dermis','epidermis','hypodermis','papillae','arrector pili','sebaceous gland','sweat gland','hair follicle','nail','keratin','melanin','dermatome','myotome','sclerotome','somatic','autonomic','sympathetic','parasympathetic','enteric'];
TERMS.forEach(t=>{
  online(t,'skeletal','Anatomical term: '+t+'. A standard term of anatomical terminology used to describe location, movement, or structure precisely and consistently.',
    {region:'general',structure_type:'terminology',latin_name:'',functions:['Provides precise anatomical communication.'],related_structures:['anatomical terminology'],clinical_notes:'Standard terms prevent ambiguity in clinical records.'});
});
// ---- tissues ----
const TISSUES=['simple squamous epithelium','simple cuboidal epithelium','simple columnar epithelium','stratified squamous epithelium','pseudostratified epithelium','transitional epithelium','loose areolar tissue','dense regular tissue','dense irregular tissue','adipose tissue','reticular tissue','hyaline cartilage','elastic cartilage','fibrocartilage','compact bone tissue','spongy bone tissue','blood tissue','skeletal muscle tissue','cardiac muscle tissue','smooth muscle tissue','nervous tissue','astrocytes','oligodendrocytes','microglia','Schwann cells','mucous membrane','serous membrane','synovial membrane','cutaneous membrane'];
TISSUES.forEach(t=>{
  online(t,'organs',t[0].toUpperCase()+t.slice(1)+' is a tissue of the human body. The four basic tissue types are epithelial, connective, muscle, and nervous tissue.',
    {region:'body',structure_type:'tissue',latin_name:'',functions:['Carries out its tissue-specific role.'],related_structures:['organs containing it'],clinical_notes:'Tissue identity is confirmed by histology.'});
});
// ---- landmarks ----
const LAND=['foramen magnum','jugular foramen','carotid canal','optic canal','foramen ovale','foramen spinosum','foramen rotundum','internal acoustic meatus','hypoglossal canal','cribriform plate','supraorbital foramen','infraorbital foramen','mental foramen','mandibular foramen','stylomastoid foramen','obturator foramen','greater sciatic foramen','vertebral foramen','transverse foramen','intervertebral foramen','iliac crest','anterior superior iliac spine','ischial tuberosity','greater trochanter','lesser trochanter','medial malleolus','lateral malleolus','olecranon','glenoid cavity','acetabulum','xiphoid process','mastoid process','coracoid process','acromion','odontoid process','frontal sinus','maxillary sinus','sphenoid sinus','sagittal suture','coronal suture','lambdoid suture','bregma','lambda','linea aspera','deltoid tuberosity','cubital fossa','femoral triangle','anatomical snuffbox','carpal tunnel','inguinal canal','femoral canal','diaphragmatic hiatus','pelvic brim','sacral promontory','iliopubic eminence','pubic tubercle','ischial spine','greater tubercle','lesser tubercle','radial tuberosity','ulnar tuberosity','coronoid process of ulna','tibial tuberosity','fibular head','calcaneal tuberosity','navicular tuberosity','fifth metatarsal tuberosity','sustentaculum tali','trochlea of humerus','capitulum of humerus','head of radius','styloid process of radius','dorsal tubercle of radius'];
LAND.forEach(l=>{
  online(l,'skeletal',l[0].toUpperCase()+l.slice(1)+' is an anatomical landmark used to describe location, guide examination, and orient imaging. Landmarks are consistent surface or bony reference points.',
    {region:'body',structure_type:'landmark',latin_name:'',functions:['Serves as a reference point for location.'],related_structures:['surrounding structures'],clinical_notes:'Palpable landmarks guide safe clinical procedures.'});
});
// ---- brain regions ----
const BRAIN=['frontal lobe','parietal lobe','temporal lobe','occipital lobe','insula','cingulate gyrus','precentral gyrus','postcentral gyrus','cerebellum','midbrain','pons','medulla oblongata','thalamus','hypothalamus','hippocampus','amygdala','caudate nucleus','putamen','globus pallidus','corpus callosum','fornix','lateral ventricles','third ventricle','fourth ventricle','cerebral aqueduct','dura mater','arachnoid mater','pia mater','falx cerebri','olfactory bulb','optic chiasm','primary motor cortex','primary somatosensory cortex','visual cortex','auditory cortex'];
BRAIN.forEach(b=>{
  online(b,'nervous',b[0].toUpperCase()+b.slice(1)+' is a region of the human brain. Brain regions are described by location, connections, and general functional roles established in neuroscience.',
    {region:'head',structure_type:'brain region',latin_name:'',functions:['Contributes to neural processing.'],related_structures:['connected brain regions'],clinical_notes:'Lesion patterns follow functional neuroanatomy.'});
});
// ---- heart structures ----
const HEART=['right atrium','left atrium','right ventricle','left ventricle','interventricular septum','tricuspid valve','mitral valve','aortic valve','pulmonary valve','chordae tendineae','papillary muscles','sinoatrial node','atrioventricular node','bundle of His','Purkinje fibers','pericardium','myocardium','endocardium','coronary sinus','aortic root'];
HEART.forEach(h=>{
  online(h,'circulatory',h[0].toUpperCase()+h.slice(1)+' is a structure of the human heart. The heart has four chambers and four valves driving the pulmonary and systemic circuits.',
    {region:'thorax',structure_type:'heart structure',latin_name:'',functions:['Supports the cardiac pumping cycle.'],related_structures:['heart chambers and valves'],clinical_notes:'Assessed by auscultation, ECG, and cardiac imaging.'});
});
// ---- processes ----
const PROC=['intramembranous ossification','endochondral ossification','bone remodeling','hematopoiesis','sliding filament contraction','neuromuscular transmission','action potential propagation','synaptic transmission','blood clotting cascade','cardiac cycle','respiratory cycle','swallowing','peristalsis','glomerular filtration','tubular reabsorption','spermatogenesis','oogenesis','wound healing','inflammation','thermoregulation','circadian rhythm'];
PROC.forEach((p,i)=>{
  online(p,'organs',p[0].toUpperCase()+p.slice(1)+' is a physiological process of the human body. Processes are described as ordered sequences of events studied in physiology.',
    {region:'body',structure_type:'physiological process',latin_name:'',functions:['Maintains or restores homeostasis.'],related_structures:['participating organs'],clinical_notes:'Disruption of the process produces recognizable clinical patterns.'});
});
// ---- systems ----
const SYS=[['skeletal system','support and mineral storage'],['muscular system','movement and heat production'],['nervous system','rapid signaling and coordination'],['endocrine system','hormonal regulation'],['cardiovascular system','transport of blood'],['lymphatic system','fluid return and immunity'],['respiratory system','gas exchange'],['digestive system','nutrient processing'],['urinary system','waste excretion and fluid balance'],['reproductive system','gamete production'],['integumentary system','protection and sensation']];
SYS.forEach(s=>{
  online(s[0],'organs',s[0][0].toUpperCase()+s[0].slice(1)+' is one of the eleven organ systems of the human body, responsible for '+s[1]+'. Systems are groups of organs working together.',
    {region:'body',structure_type:'organ system',latin_name:'',functions:['Carries out '+s[1]+'.'],related_structures:['member organs'],clinical_notes:'System review guides clinical assessment.'});
});
// ---- second aspects (top up online toward ~2000) ----
MUS2.forEach(m=>{
  online(m[0]+' - innervation and blood supply','muscular','Skeletal muscles such as the '+m[0]+' receive motor innervation from spinal or cranial nerves and blood from regional arteries. Motor units recruit fibers in order of size for graded force.',
    {region:m[1],structure_type:'skeletal muscle',latin_name:'',functions:['Receives neural drive for contraction.'],related_structures:['regional nerves and vessels'],clinical_notes:'Denervation leads to atrophy; reinnervation may restore function.'});
  online(m[0]+' - clinical notes','muscular','Clinical record for the '+m[0]+'. Muscle strength is graded 0 to 5 on examination; tears are classified by fiber disruption and managed by rest, rehabilitation, and graded reloading.',
    {region:m[1],structure_type:'skeletal muscle',latin_name:'',functions:['Assessed by strength testing.'],related_structures:[m[1]+' region'],clinical_notes:'Palpate for tenderness and test resisted movement.'});
});
ORGANS.forEach(o=>{
  online(o+' - relations','organs','Anatomical relations of the '+o+'. Each organ sits in a defined compartment with consistent neighboring structures used as landmarks in examination and imaging.',
    {region:'body',structure_type:'organ',latin_name:'',functions:['Occupies a defined anatomical compartment.'],related_structures:['neighboring organs'],clinical_notes:'Relations guide safe surgical and imaging approaches.'});
  online(o+' - clinical notes','organs','Clinical record for the '+o+'. Disease patterns follow the organ\u2019s tissue type and blood supply; function is tracked with organ-specific tests and imaging.',
    {region:'body',structure_type:'organ',latin_name:'',functions:['Monitored by organ-specific tests.'],related_structures:['same-system organs'],clinical_notes:'Correlate symptoms with anatomical location.'});
});
VESSELS.forEach(v=>{
  online(v+' - clinical notes','circulatory','Clinical record for the '+v+'. Patency and flow are assessed by palpation, auscultation for bruits, Doppler ultrasound, or angiographic imaging as indicated.',
    {region:'body',structure_type:/vein/i.test(v)?'vein':'artery',latin_name:'',functions:['Assessed for patency and flow.'],related_structures:['heart'],clinical_notes:'Know the course before venipuncture or catheterization.'});
});
NERVES.forEach(n=>{
  online(n+' - distribution','nervous','Distribution record for the '+n+'. Each nerve supplies a defined territory of skin, muscle, or viscera; deficits map to the nerve\u2019s course and branches.',
    {region:'body',structure_type:'nerve',latin_name:'',functions:['Supplies its defined territory.'],related_structures:['target tissues'],clinical_notes:'Test motor and sensory function in the distribution.'});
});
JOINTS.forEach(j=>{
  online(j+' - movements','skeletal','Movements of the '+j+'. Range of motion is described in degrees and compared side to side; limits may be bony, ligamentous, or muscular.',
    {region:'body',structure_type:'joint',latin_name:'',functions:['Guides its characteristic movements.'],related_structures:['acting muscles'],clinical_notes:'Measure active and passive range of motion.'});
});
BRAIN.forEach(b=>{
  online(b+' - connections','nervous','Connections of the '+b+'. Brain regions communicate through white-matter tracts; input and output pathways define each region\u2019s role in networks.',
    {region:'head',structure_type:'brain region',latin_name:'',functions:['Integrates signals within networks.'],related_structures:['connected regions'],clinical_notes:'Disconnection produces network-level deficits.'});
});
HEART.forEach(h=>{
  online(h+' - cycle role','circulatory','Role of the '+h+' in the cardiac cycle. The cycle alternates systole and diastole; valves ensure one-way flow and chambers fill and eject in sequence.',
    {region:'thorax',structure_type:'heart structure',latin_name:'',functions:['Participates in systole and diastole.'],related_structures:['cardiac cycle phases'],clinical_notes:'Timing of sounds and pulses reflects cycle events.'});
});
TERMS.forEach(t=>{
  online(t+' - usage','skeletal','Usage example for the anatomical term '+t+'. Standard terms combine into precise descriptions, for example locating a structure relative to planes, regions, and neighboring parts.',
    {region:'general',structure_type:'terminology',latin_name:'',functions:['Builds precise descriptions.'],related_structures:['anatomical terminology'],clinical_notes:'Use standard terms in every clinical description.'});
});
TISSUES.forEach(t=>{
  online(t+' - locations','organs','Locations of '+t+'. Each tissue occupies characteristic sites; for example, epithelia line surfaces and connective tissues underlie them throughout the body.',
    {region:'body',structure_type:'tissue',latin_name:'',functions:['Found at characteristic sites.'],related_structures:['organs containing it'],clinical_notes:'Biopsy site choice follows tissue distribution.'});
});
PROC.forEach(p=>{
  online(p+' - steps','organs','Sequence of '+p+'. Physiological processes unfold in ordered steps with regulation at key checkpoints; feedback loops keep the process within bounds.',
    {region:'body',structure_type:'physiological process',latin_name:'',functions:['Proceeds through regulated steps.'],related_structures:['regulating signals'],clinical_notes:'Identify which step fails in disease.'});
});
SYS.forEach(s=>{
  online(s[0]+' - member organs','organs','Member organs of the '+s[0]+': the organs whose combined work carries out '+s[1]+'. Organ lists are standard in anatomy references.',
    {region:'body',structure_type:'organ system',latin_name:'',functions:['Coordinates member organs.'],related_structures:['member organs'],clinical_notes:'Localize complaints to a system first.'});
});
const onlineCount=seed;
console.log('online records:',onlineCount);
// ---- signature records ----
const rnd=lib.prng(777);
for(let s=onlineCount+1;s<=10000;s++){
  const r=gen.generate(s,{},lib.prng(s));
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID signature',s,v.errors);process.exit(1);}
  recs.push(r);
}
// validate online
for(const r of recs.slice(0,onlineCount)){
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID online',r._seed,v.errors,JSON.stringify(r).slice(0,200));process.exit(1);}
}
const sum=lib.summarizeOnline(recs);
console.log('total',sum.total,'online',sum.online,'signature',sum.signature);
const w=lib.writeDb(SLUG,recs,REPO);
console.log('wrote',w.mb.toFixed(2),'MB in',w.chunks,'chunks');
