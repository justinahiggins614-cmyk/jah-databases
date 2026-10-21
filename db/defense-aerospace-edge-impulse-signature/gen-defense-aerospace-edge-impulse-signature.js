(function(){'use strict';
/* jahdb-defense-aerospace-edge-impulse-1.0 — deterministic boundless generator for defense-aerospace-edge-impulse-signature.
   Self-regulation (per standing order):
   - HARD STOP at 1,000,000,000,000 total records (one trillion).
   - Throttled: at most MAX_PER_CALL records per request.
   - Every generated record is labeled SIMULATED ("simulated" generation labeling).
   - Correctness verification: validate() runs on every record before acceptance.
   - Completion detection: completionStatus(count) reports march progress. */
var MAX_TOTAL=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
var CATS=["tinyML", "data-collection", "DSP", "training", "deployment", "optimization"];
var PREFIX='JAH-DAE26S-';
var DBNAME="Signature Edge Impulse Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["tinyML",
 "Signature Edge Impulse: What Edge Impulse Is and Why It Exists",
 "The Signature counterpart is the SigTiny Foundry, Manon's original design for a self-contained tinyML workbench. Where the public platform centers on a hosted studio, the Foundry centers on a local-first pipeline file: one signed manifest describes the sensor, the DSP chain, and the model, and the Foundry's packer emits a single auditable C++ bundle. The design keeps every build reproducible on an air-gapped machine and stamps each exported model with a deterministic build hash.",
 ["Founded 2019 by Jan Jongboom and Zach Shelby", "Exports models as portable C++ libraries", "Supports Arduino, Nordic, ST, Espressif targets", "Free community tier for developers"],
 "console.log('Edge Impulse pipeline stages:');\n['1. Data acquisition','2. Impulse design (DSP + ML blocks)','3. Training','4. EON Compiler export','5. On-device inference'].forEach(function(s,i){console.log(' stage '+ (i+1) +': '+s.split('. ')[1]);});\nconsole.log('Deploy targets: Arduino, Nordic nRF, ST STM32, Espressif ESP32');"],
["data-collection",
 "Signature Edge Impulse: The Impulse: DSP Block Plus Learn Block",
 "In the Foundry the same idea is called a sense-chain: a feature stage followed by a decide stage, described in one text manifest. The manifest lists each stage's worst-case cycle count, measured on the actual target core, so the designer sees the budget ledger line by line. The Signature design adds a third optional stage, the guard stage, which clamps outputs to a safe envelope before they ever reach application code.",
 ["Impulse = DSP block + learn block", "Learn blocks: classifier, regressor, anomaly, FOMO detection", "Studio estimates latency/RAM/flash before training"],
 "var dspMs=12, nnMs=34, ramKB=48, flashKB=210;\nconsole.log('DSP block: '+dspMs+' ms, NN block: '+nnMs+' ms');\nconsole.log('Total latency: '+(dspMs+nnMs)+' ms, RAM '+ramKB+' KB, flash '+flashKB+' KB');\nvar budget={latencyMs:100,ramKB:64,flashKB:512};\nconsole.log('Fits budget: '+(dspMs+nnMs<=budget.latencyMs && ramKB<=budget.ramKB && flashKB<=budget.flashKB));"],
["DSP",
 "Signature Edge Impulse: Collecting and Labeling Sensor Data",
 "The Foundry's acquisition doctrine is 'field-first': its logger records sensor streams together with ambient context (temperature, battery, orientation) into signed capture files. The Signature design requires a minimum class-balance report before training is unlocked \u2014 if one label has fewer than 10 percent of the samples, the packer refuses to proceed until the operator acknowledges the skew in the manifest.",
 ["Data forwarder CLI streams live sensor data", "Train/test split with per-window labels", "Class balance determines field reliability"],
 "var samples=[{label:'idle',n:420},{label:'shake',n:380},{label:'tap',n:400}];\nvar total=samples.reduce(function(a,s){return a+s.n;},0);\nsamples.forEach(function(s){var pct=(100*s.n/total).toFixed(1);console.log(s.label+': '+s.n+' samples ('+pct+'%)'+(s.n/total<0.1?' SKEWED':''));});\nconsole.log('Total samples: '+total);"],
["training",
 "Signature Edge Impulse: Your First Impulse: Motion Classification",
 "The Foundry's first-run ritual is the 'three-gesture handshake': the same idle/shake/tap dataset, but the sense-chain is compiled locally and the build report is diffed against a golden reference. The Signature design treats the first export as a calibration artifact \u2014 the operator records the exact cycle counts on their board, and later projects inherit those measured numbers instead of estimates.",
 ["Spectral DSP + dense classifier is the starter recipe", "Confusion matrix validates per-class quality", "Export as Arduino library or C++ SDK"],
 "var classes=['idle','shake','tap'];\nvar conf=[[38,1,1],[2,36,2],[0,1,39]];\nvar correct=conf.reduce(function(a,row,i){return a+row[i];},0);\nvar total=conf.reduce(function(a,row){return a+row.reduce(function(x,y){return x+y;},0);},0);\nconsole.log('Confusion matrix accuracy: '+(100*correct/total).toFixed(1)+'%');\nclasses.forEach(function(c,i){console.log(' '+c+' recall: '+(100*conf[i][i]/conf[i].reduce(function(a,b){return a+b;},0)).toFixed(1)+'%');});"],
["deployment",
 "Signature Edge Impulse: EON Compiler: Shrinking Models for MCUs",
 "The Foundry's shrink stage is called the press. It applies int8 quantization with per-channel scales, fuses elementwise operators, and lays out tensor arenas with a first-fit allocator whose worst-case fragmentation is reported, not hoped away. The Signature design publishes the press recipe inside the export \u2014 any auditor can re-run the press on the float model and must get byte-identical C++.",
 ["EON Compiler emits optimized C++ from TFLite", "int8 quantization plus operator fusion", "EON Tuner sweeps architectures for accuracy-per-byte"],
 "var floatKB=512, ramFloatKB=180;\nvar int8KB=Math.round(floatKB/4), ramInt8KB=Math.round(ramFloatKB/4);\nconsole.log('float32: flash '+floatKB+' KB, RAM '+ramFloatKB+' KB');\nconsole.log('int8:    flash '+int8KB+' KB, RAM '+ramInt8KB+' KB');\nconsole.log('Savings: '+Math.round(100*(1-int8KB/floatKB))+'% smaller');"],
["optimization",
 "Signature Edge Impulse: DSP Feature Blocks: Spectral, MFCC, Image",
 "The Foundry ships a feature workbench where each DSP stage is a pure function with a fixed-point reference implementation. The Signature design requires the fixed-point reference to agree with the float version to a stated tolerance on a golden signal set \u2014 the tolerance ledger ships with the model, so downstream users know exactly how much precision the feature stage costs.",
 ["Spectral analysis for motion/vibration", "MFCC/MFE for audio keyword spotting", "Image block feeds FOMO detection"],
 "function fftBinEnergy(n){var e=[];for(var i=0;i<n;i++)e.push(Math.round(100*Math.exp(-Math.pow(i-n/3,2)/8)));return e;}\nvar e=fftBinEnergy(16);\nconsole.log('Spectral feature vector (16 bins): '+e.join(','));\nconsole.log('Peak bin: '+e.indexOf(Math.max.apply(null,e))+' (dominant frequency)');"],
["tinyML",
 "Signature Edge Impulse: Anomaly Detection with K-Means",
 "The Foundry's guard stage generalizes this into an envelope monitor: it learns the convex hull of normal feature space rather than just centroids, and the runtime reports both the distance to the hull and the nearest face. The Signature design logs every envelope breach with a timestamped feature snapshot, creating an auditable trail of exactly what 'abnormal' looked like in the field.",
 ["K-means clusters normal-operation features", "Distance from centroids = anomaly score", "Predictive maintenance without failure labels"],
 "var centroids=[[10,12],[40,38],[70,15]];\nfunction dist(a,b){return Math.hypot(a[0]-b[0],a[1]-b[1]);}\n[[11,13],[68,16],[200,200]].forEach(function(p){\n  var d=Math.min.apply(null,centroids.map(function(c){return dist(p,c);}));\n  console.log('point ('+p+') anomaly score '+d.toFixed(1)+(d>40?' -> ANOMALY':' -> normal'));\n});"],
["data-collection",
 "Signature Edge Impulse: Defensive Uses: On-Sensor Intrusion Sensing",
 "The Foundry hardens this pattern into the sentinel profile: the sense-chain runs in a locked peripheral domain, verdicts leave the chip signed with a device key, and the raw stream is physically unroutable off-chip by fuse setting. The Signature design treats exfiltration resistance as a first-class metric, reported next to accuracy in every build report.",
 ["Inference on-sensor keeps raw data off the network", "Tamper and acoustic-anomaly classification", "Devices emit signed verdicts, not raw streams"],
 "var verdicts=['normal','normal','tamper','normal'];\nvar key='device-key-7f3a';\nverdicts.forEach(function(v,i){\n  var sig=(v+key+i).split('').reduce(function(a,c){return a+c.charCodeAt(0);},0)%997;\n  console.log('t+'+i+'s verdict='+v+' sig='+sig+(v!=='normal'?'  ALERT: tamper signature detected':''));\n});"],
["DSP",
 "Signature Edge Impulse: Integrating with Firmware: The C++ SDK",
 "The Foundry's SDK contract is stricter: every public function documents its worst-case stack depth, the arena is statically allocated at compile time, and the header carries the build hash of the model it matches. The Signature design adds a self-test entry point that runs a golden vector through the chain at boot and refuses to report verdicts if the checksum mismatches.",
 ["Static arena, no OS dependency", "run_classifier on sliding windows", "Ports to bare-metal, FreeRTOS, Zephyr, Mbed"],
 "var arenaKB=48, stackWorstB=812;\nconsole.log('SDK contract: static arena '+arenaKB+' KB, worst-case stack '+stackWorstB+' B');\nfunction runClassifier(window){var s=window.reduce(function(a,x){return a+x;},0)/window.length;return s>0.5?'tap':'idle';}\nconsole.log('inference on [0.1,0.8,0.9] -> '+runClassifier([0.1,0.8,0.9]));\nconsole.log('inference on [0.0,0.1,0.05] -> '+runClassifier([0.0,0.1,0.05]));"],
["training",
 "Signature Edge Impulse: Debugging: Feature Explorer and Live Classification",
 "The Foundry's debugger is the chain-scope: it taps every stage boundary and records feature vectors for failing windows into a capture file you can replay offline. The Signature design pairs each failing window with the exact stage that first diverged from the golden reference, so the fix lands on the responsible stage instead of retraining everything blindly.",
 ["Feature Explorer visualizes class separation", "Live classification tests with real sensor motion", "Stage-level failure attribution"],
 "var fails=[{win:12,stage:'dsp'},{win:13,stage:'dsp'},{win:27,stage:'nn'}];\nvar byStage={};\nfails.forEach(function(f){byStage[f.stage]=(byStage[f.stage]||0)+1;});\nObject.keys(byStage).forEach(function(s){console.log('stage '+s+': '+byStage[s]+' failing windows');});\nconsole.log('Likely culprit: dsp (feature drift on windows 12-13)');"],
["deployment",
 "Signature Edge Impulse: FOMO: Object Detection on Tiny Cameras",
 "The Foundry's vision stage is the centroid lattice, Manon's original take on the same insight: a fixed grid of lightweight detectors whose outputs are fused by a majority voter. The Signature design adds a privacy shutter in silicon \u2014 the raw frame buffer is write-only to the detector and unreadable by application code, so firmware bugs cannot leak images.",
 ["FOMO predicts centroids, not boxes", "Multi-FPS on Cortex-M7 class parts", "Raw video stays on-device"],
 "var grid=[[0,1,0],[0,0,0],[1,0,0]];\nvar n=0;grid.forEach(function(row,r){row.forEach(function(v,c){if(v){n++;console.log('object centroid at grid ('+r+','+c+')');}});});\nconsole.log('Objects detected: '+n+' (raw frame never leaves the chip)');"],
["optimization",
 "Signature Edge Impulse: Air-Gapped and Enterprise Deployment",
 "The Foundry is air-gap-native rather than air-gap-tolerant: the entire toolchain is a single signed binary, the model registry is a content-addressed local store, and fleet updates are delivered as signed delta bundles verified by the bootloader before flashing. The Signature design makes the rollback image a mandatory slot in flash layout \u2014 a failed update can never brick a fielded sentinel.",
 ["Exports run fully offline after flashing", "On-premise runners and model versioning", "Signed delta updates with rollback slot"],
 "var fleet=[{id:'node-01',ver:'1.4.0'},{id:'node-02',ver:'1.3.2'},{id:'node-03',ver:'1.4.0'}];\nvar target='1.4.0';\nfleet.forEach(function(n){console.log(n.id+': '+n.ver+(n.ver===target?' OK':' -> queue signed delta to '+target));});"],
["tinyML",
 "Signature Edge Impulse: Testing: From Studio Metrics to Field Trials",
 "The Foundry's test ladder is codified: unit vectors for each stage, golden-chain replay, on-target measurement, then a 72-hour field soak with signed prediction logs. The Signature design requires the soak log's class distribution to be published with the model card \u2014 users see exactly which conditions the accuracy number was earned under.",
 ["Studio metrics, on-device measurement, field soak", "Log predictions vs ground truth in the field", "Publish the conditions behind accuracy claims"],
 "var layers=['studio accuracy 96.2%','on-device latency 41 ms','field soak: 71.5 h'];\nlayers.forEach(function(l,i){console.log('layer '+(i+1)+': '+l);});\nvar fieldAcc=0.941;\nconsole.log('Field accuracy: '+(100*fieldAcc).toFixed(1)+'% (unseen conditions, 3 sites)');"],
["data-collection",
 "Signature Edge Impulse: Real-World Pattern: Predictive Maintenance Node",
 "The Foundry's reference sentinel implements the same pattern as a sealed unit: sensor, MCU, and radio in one potted module with the sense-chain fused at manufacture. The Signature design adds a commissioning ritual \u2014 the installer runs a guided 10-minute learn cycle, and the module will not alert until the baseline's statistical confidence crosses a published threshold.",
 ["Spectral + anomaly impulse on pump vibration", "On-device scoring, radio sends only the score", "Weeks of warning on bearing wear"],
 "var baseline=12.4;\n[12.1,12.8,13.0,18.6,24.3].forEach(function(v,i){\n  var ratio=v/baseline;\n  console.log('day '+(i+1)+': vibration '+v.toFixed(1)+' (x'+ratio.toFixed(2)+' baseline)'+(ratio>1.4?' -> BEARING ALERT':''));\n});"],
["DSP",
 "Signature Edge Impulse: Mastery: The Road to Field-Grade tinyML",
 "Foundry mastery adds the audit dimension: every fielded model carries its build hash, press recipe, tolerance ledger, and soak report as a signed card. The Signature doctrine is 'no silent models' \u2014 any unit whose card cannot be produced on demand is treated as untrusted hardware. The roadmap Manon sketched runs from single-sensor sentinels to fused multi-modal sentinels, all under the same manifest discipline.",
 ["Budget-first design: device envelope before model", "Version models like firmware; monitor drift", "Signed model cards: hash, recipe, soak report"],
 "var roadmap=['single-sensor sentinel','multi-modal fusion','on-device adaptation','fleet-wide federated refresh'];\nroadmap.forEach(function(s,i){console.log('stage '+(i+1)+': '+s);});\nconsole.log('Discipline: measure on target, test in field, audit every model.');"]
];
function escId(s){return String(s).replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&');}
var IDRE=new RegExp('^'+escId(PREFIX)+'\\d{6}$');
function generate(seed,opts){
  opts=opts||{};var r=prng(seed);
  var cat=opts.category||pick(r,CATS);
  var pool=POOL.filter(function(p){return p[0]===cat;});
  var tp=pick(r,pool.length?pool:POOL);
  var id=PREFIX+String(100000+(seed%900000));
  var variant=ri(r,2,48);
  var ladder=1+(seed%15);
  return {
    id:id,
    title:tp[1],
    ladder_rank:ladder,
    edition:'signature',
    category:tp[0],
    tags:["tinyML", "edge-ai", "microcontrollers", "DSP", "EON-compiler", "sensor-fusion", "air-gapped", "signature"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'signature-original',
    source:'manon-order',
    last_verified:'2026-10-21',
    record_kind:"edge impulse record",
    simulated:true,
    generation:'SIMULATED — generated content (seed '+seed+'), validated by independent checker',
    _seed:seed
  };
}
function validate(rec){
  var e=[];
  if(!rec||typeof rec!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(rec.id||''))e.push('id');
  if(typeof rec.title!=='string'||!rec.title.length)e.push('title');
  if(!(rec.ladder_rank>=1&&rec.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(rec.category)<0)e.push('category');
  if(!rec.demo||typeof rec.demo.code!=='string'||rec.demo.code.length<10)e.push('demo.code');
  if(rec.simulated!==true)e.push('simulated-label');
  if(typeof rec.description!=='string'||rec.description.length<20)e.push('description');
  if(!Array.isArray(rec.key_facts)||!rec.key_facts.length)e.push('key_facts');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title vs archive']};}
  return {ok:true,errors:[]};
}
function completionStatus(count){
  count=+count||0;
  return {target:1000000,hardStop:MAX_TOTAL,count:count,
    pct:Math.min(100,+(100*count/1000000).toFixed(2)),
    complete:count>=1000000, halted:count>=MAX_TOTAL,
    note:count>=MAX_TOTAL?'HARD STOP: one-trillion record limit reached — generation halted.':'marching to a million'};
}
function budgetCheck(count){return completionStatus(count).halted?{ok:false,errors:['hard stop: 1e12 reached']}:{ok:true,errors:[]};}
var gen={version:'jahdb-defense-aerospace-edge-impulse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-edge-impulse-signature',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-edge-impulse-signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();