/* ✳ SIGNATURE — JAH Neuroscience Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic client-side generator: same seed + same version => same record.
   Anchor facts verified from published neuroscience sources; application studies
   are Signature-generated and labeled as such. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['neuroanatomy','neurotransmitters','neural-signaling','brain-development','sensation-perception','memory-learning','neurological-disorders','neuroimaging','neurotechnology','glial-biology'];
var PREFIX='JAH-NEU-';
/* [subject, category, type, function, key fact, [associated x3], year (0 = none)] */
var ANCH=[
['Acetylcholine','neurotransmitters','neurotransmitter','triggers muscle contraction and supports memory and attention; its deficiency is linked to Alzheimer\u2019s disease','one of the earliest neurotransmitters discovered',['muscle contraction','memory','attention'],0],
['Dopamine','neurotransmitters','neurotransmitter','drives reward processing, motivation, and motor control; its depletion leads to Parkinson\u2019s disease','produced mainly in the substantia nigra and ventral tegmental area',['reward','motivation','motor control'],0],
['Serotonin','neurotransmitters','neurotransmitter','regulates mood, appetite, and sleep; low levels are associated with depression','often called the feel-good neurotransmitter',['mood','appetite','sleep'],0],
['Norepinephrine','neurotransmitters','neurotransmitter','governs arousal, attention, and the fight-or-flight stress response; also regulates blood pressure','active in both the brain and the peripheral sympathetic nervous system',['arousal','attention','stress response'],0],
['GABA','neurotransmitters','neurotransmitter','the brain\u2019s primary inhibitory neurotransmitter; deficient activity is linked to anxiety','balances neuronal excitation and inhibition',['inhibition','anxiety regulation','calm signaling'],0],
['Glutamate','neurotransmitters','neurotransmitter','the brain\u2019s primary excitatory neurotransmitter','the most prevalent excitatory transmitter in the brain',['excitation','learning','memory'],0],
['Hippocampus','neuroanatomy','brain-region','forms new memories and supports spatial navigation; neuron death here is a hallmark of Alzheimer\u2019s disease','a core structure of the limbic system',['memory formation','spatial navigation','Alzheimer\u2019s disease'],0],
['Amygdala','neuroanatomy','brain-region','central to emotional learning, especially fear conditioning','a limbic-system structure deep in the forebrain',['fear conditioning','emotional memory','threat detection'],0],
['Broca\u2019s area','neuroanatomy','brain-region','in the frontal lobe of the left hemisphere; important for the production of speech','damage causes Broca\u2019s aphasia: halting, effortful speech',['speech production','frontal lobe','language'],0],
['Basal ganglia','neuroanatomy','brain-region','clusters including the caudate nucleus, putamen, globus pallidus, and substantia nigra; initiate movements','cell death in the substantia nigra causes Parkinson\u2019s disease',['movement initiation','habit formation','reward circuits'],0],
['Cerebellum','neuroanatomy','brain-region','the large hindbrain structure coordinating movement, balance, and motor learning','holds more neurons than the rest of the brain combined',['coordination','balance','motor learning'],0],
['Prefrontal cortex','neuroanatomy','brain-region','executive function: planning, decision-making, and impulse control','the last brain region to fully mature, into the mid-twenties',['decision-making','planning','working memory'],0],
['Occipital lobe','neuroanatomy','brain-region','visual processing, from edges and color to recognized objects','houses the primary visual cortex',['vision','visual recognition','spatial awareness'],0],
['Thalamus','neuroanatomy','brain-region','relays nearly all sensory information to the cerebral cortex','called the brain\u2019s relay station',['sensory relay','consciousness','sleep regulation'],0],
['Hypothalamus','neuroanatomy','brain-region','regulates hunger, thirst, temperature, and hormones through the pituitary gland','links the nervous and endocrine systems',['homeostasis','hormones','autonomic control'],0],
['Corpus callosum','neuroanatomy','brain-region','the great fiber bundle connecting the two cerebral hemispheres','carries millions of axons between hemispheres',['hemispheres','integration','split-brain research'],0],
['Wernicke\u2019s area','neuroanatomy','brain-region','a temporal-lobe region critical for understanding language','damage causes fluent but meaningless speech',['language comprehension','temporal lobe','aphasia'],0],
['The neuron','neural-signaling','cell','the brain\u2019s signaling cell: dendrites receive inputs, the axon transmits output; about 86 billion neurons fill the human brain','multipolar neurons are the most common type',['dendrites','axon','synapse'],0],
['Action potential','neural-signaling','process','an electrical impulse traveling down the axon, fired when the membrane passes threshold from its resting state near -70 mV','an all-or-nothing signaling event',['axon','ion channels','threshold'],0],
['The synapse','neural-signaling','process','the junction where neurotransmitters cross from one neuron to the next; synapses strengthen with use, which is the basis of learning','an estimated 100 trillion synapses in the human brain',['neurotransmitters','plasticity','learning'],0],
['Myelin','neural-signaling','structure','the insulating sheath around axons that speeds signal conduction; damaged in multiple sclerosis','made by oligodendrocytes in the brain and Schwann cells in nerves',['conduction speed','white matter','multiple sclerosis'],0],
['Golgi staining and the neuron doctrine','brain-development','technique','Camillo Golgi\u2019s 1873 stain revealed whole neurons; Santiago Ram\u00f3n y Cajal used it to show neurons are individual cells','founded modern neuroscience',['staining','Cajal','neuron doctrine'],1873],
['The case of Phineas Gage','brain-development','case','an 1848 railroad accident drove an iron rod through his frontal lobe, changing his personality and revealing the lobe\u2019s role','a landmark case in neuropsychology',['frontal lobe','personality','case study'],1848],
['The reflex arc','sensation-perception','process','the spinal circuit producing rapid involuntary responses without involving the brain','protects the body before conscious pain registers',['spinal cord','involuntary response','protection'],0],
['The visual system','sensation-perception','system','light is converted to signals by the retina, relayed through the thalamus to the occipital lobe','the most studied sensory system',['retina','optic nerve','occipital lobe'],0],
['Neuroplasticity','memory-learning','process','the brain\u2019s ability to rewire itself by strengthening or pruning synapses','underlies learning and recovery from injury',['learning','memory','rehabilitation'],0],
['Long-term potentiation','memory-learning','process','lasting strengthening of synapses after repeated stimulation; a cellular basis of memory','first described in the hippocampus',['memory','hippocampus','synaptic strength'],0],
['Alzheimer\u2019s disease','neurological-disorders','disorder','progressive dementia marked by neuron death in the hippocampus and cortex; amyloid plaques and tau tangles are hallmarks','the most common cause of dementia in the elderly',['memory loss','hippocampus','dementia'],0],
['Parkinson\u2019s disease','neurological-disorders','disorder','a movement disorder caused by death of dopamine-producing neurons in the substantia nigra','tremor, rigidity, and slowed movement are hallmark signs',['dopamine','substantia nigra','movement'],0],
['Epilepsy','neurological-disorders','disorder','recurrent seizures from abnormal, excessive neuronal activity','managed with anticonvulsant drugs that calm electrical activity',['seizures','EEG','anticonvulsants'],0],
['Stroke','neurological-disorders','disorder','brain damage from interrupted blood supply; a leading cause of adult disability','time-critical: fast treatment limits damage',['ischemia','rehabilitation','risk factors'],0],
['Electroencephalography (EEG)','neuroimaging','technique','records the brain\u2019s electrical activity through electrodes on the scalp','the first human EEG was recorded by Hans Berger in 1929',['brain waves','epilepsy diagnosis','sleep studies'],1929],
['Functional MRI','neuroimaging','technique','maps brain activity by tracking blood-flow changes during tasks','a noninvasive window into working brain networks',['brain mapping','research','presurgical planning'],0],
['Brain-computer interfaces','neurotechnology','technology','devices that translate neural signals into commands for computers or prosthetic limbs','clinical trials are restoring communication and movement',['prosthetics','neural decoding','assistive technology'],0],
['Glial cells','glial-biology','cell','the support cells of the nervous system: astrocytes, oligodendrocytes, and microglia nourish, insulate, and defend neurons','glia outnumber neurons in the human brain',['astrocytes','myelin','immune defense'],0],
['The blood-brain barrier','glial-biology','structure','a selective barrier of tightly joined cells protecting the brain from blood-borne substances','a major challenge for delivering drugs to the brain',['protection','drug delivery','astrocytes'],0]
];
var ASPECTS=['overview','function deep-dive','clinical relevance','historical timeline','research frontiers','comparative analysis'];
var CONTEXTS=['clinical case review','laboratory study','imaging study','educational module','research survey','therapeutic program'];
var TYPELBL={'neurotransmitter':'neurotransmitter','brain-region':'brain region','cell':'neural cell type','process':'neural process','structure':'neural structure','disorder':'neurological disorder','technique':'neuroimaging technique','technology':'neurotechnology','system':'sensory system','case':'historical case','molecule':'signaling molecule'};
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
  var title,desc,src,code=null,assoc=a[5].slice();
  if(mode==='profile'){
    code=serial;
    title=a[0]+': '+aspect+' ('+serial+')';
    var s1=a[0]+' is a '+(TYPELBL[a[2]]||a[2])+' of the nervous system. '+(a[6]>0?'First described in '+a[6]+'. ':'')+'Its role: '+a[3]+'.';
    var s2='Key fact: '+a[4]+'.';
    var s3='Closely associated with '+a[5][0]+', '+a[5][1]+', and '+a[5][2]+'.';
    if(aspect==='function deep-dive')desc=s1+' '+s2+' Understanding this function explains why '+a[0]+' matters across '+a[1].replace(/-/g,' ')+' research. '+s3;
    else if(aspect==='clinical relevance')desc=s1+' '+s3+' Clinicians watch '+a[0]+' because disorders of '+a[1].replace(/-/g,' ')+' trace back to it. '+s2;
    else if(aspect==='historical timeline')desc=(a[6]>0?'In '+a[6]+', ':'In the history of neuroscience, ')+a[0]+' entered the record. '+s1+' '+s2;
    else if(aspect==='research frontiers')desc=s1+' '+s2+' Current research probes '+a[0]+' with ever finer tools, from single-cell recording to whole-brain imaging. '+s3;
    else if(aspect==='comparative analysis')desc=s1+' Compared with neighboring structures and signals, '+a[0]+' is distinguished by this: '+a[3]+' '+s2;
    else desc=s1+' '+s2+' '+s3;
    src='online';
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=pick(CONTEXTS,rnd);
    var n=ri(rnd,30,4000),yr=ri(rnd,2016,2026);
    title=a[0]+' \u2014 '+ctx+' '+code;
    desc='This generated study ('+code+', compiled '+yr+') reviews '+n.toLocaleString('en-US')+' documented observations of '+a[0]+' in a '+ctx+' setting. '+
      'The established facts remain: '+a[3]+' '+
      'Observers in this illustrative study focused on '+a[5][0]+' and '+a[5][1]+', reporting patterns consistent with the published literature. '+
      'As a Signature-generated study record, the scenario is illustrative; the core facts about '+a[0]+' come from published neuroscience.';
    src='signature';assoc=[a[5][0],a[5][1],ctx+' (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{subject:a[0],subject_type:a[2],category:a[1],'function':a[3],key_fact:a[4],associated:assoc,year:a[6]||null,aspect:aspect,study_code:code},
    src:src,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-NEU-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>160)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  else{var parts=r.description.split('. ');if(parts.length<2)e.push('description-sentences');if(!/\.$/.test(r.description.trim()))e.push('description-period');}
  if(CATS.indexOf(r.category)<0)e.push('category');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(!s.subject||typeof s.subject!=='string')e.push('spec.subject');
    if(!s.subject_type||typeof s.subject_type!=='string')e.push('spec.subject_type');
    if(!s['function']||typeof s['function']!=='string')e.push('spec.function');
    if(!s.key_fact||typeof s.key_fact!=='string')e.push('spec.key_fact');
    if(!Array.isArray(s.associated)||s.associated.length<2||s.associated.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.associated');
    if(!(s.year===null||(Number.isInteger(s.year)&&s.year>=1500&&s.year<=2026)))e.push('spec.year');
  }
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-neuroscience-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('neuroscience',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
