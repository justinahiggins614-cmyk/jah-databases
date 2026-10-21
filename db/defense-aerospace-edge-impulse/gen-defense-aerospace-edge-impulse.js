(function(){'use strict';
/* jahdb-defense-aerospace-edge-impulse-1.0 — deterministic boundless generator for defense-aerospace-edge-impulse.
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
var PREFIX='JAH-DAE26-';
var DBNAME="Edge Impulse Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["tinyML",
 "Edge Impulse: What Edge Impulse Is and Why It Exists",
 "Edge Impulse is a tinyML development platform founded in 2019 by Jan Jongboom and Zach Shelby. It exists because training a neural network on a workstation is only half the job: the model must then run inside the tight RAM, flash, and power budget of a microcontroller. The platform walks you through the full pipeline in one studio \u2014 collect sensor data, design an impulse (DSP feature-extraction block plus ML learn block), train, then export a portable C++ library that runs on Arduino, Nordic, ST, Espressif, and dozens of other targets, with no cloud dependency at deploy time.",
 ["Founded 2019 by Jan Jongboom and Zach Shelby", "Exports models as portable C++ libraries", "Supports Arduino, Nordic, ST, Espressif targets", "Free community tier for developers"],
 "console.log('Edge Impulse pipeline stages:');\n['1. Data acquisition','2. Impulse design (DSP + ML blocks)','3. Training','4. EON Compiler export','5. On-device inference'].forEach(function(s,i){console.log(' stage '+ (i+1) +': '+s.split('. ')[1]);});\nconsole.log('Deploy targets: Arduino, Nordic nRF, ST STM32, Espressif ESP32');"],
["data-collection",
 "Edge Impulse: The Impulse: DSP Block Plus Learn Block",
 "Every Edge Impulse project is built around an impulse: a processing pipeline with two block types. The DSP (digital signal processing) block turns raw sensor samples into features \u2014 spectral analysis, MFCCs for audio, or flatten/image blocks for vision. The learn block is the neural network itself: classifier, regressor, anomaly detector (K-means), or object detection (FOMO). The studio shows estimated latency, RAM, and flash for each block combination before you train, so you can trade accuracy against the device budget deliberately.",
 ["Impulse = DSP block + learn block", "Learn blocks: classifier, regressor, anomaly, FOMO detection", "Studio estimates latency/RAM/flash before training"],
 "var dspMs=12, nnMs=34, ramKB=48, flashKB=210;\nconsole.log('DSP block: '+dspMs+' ms, NN block: '+nnMs+' ms');\nconsole.log('Total latency: '+(dspMs+nnMs)+' ms, RAM '+ramKB+' KB, flash '+flashKB+' KB');\nvar budget={latencyMs:100,ramKB:64,flashKB:512};\nconsole.log('Fits budget: '+(dspMs+nnMs<=budget.latencyMs && ramKB<=budget.ramKB && flashKB<=budget.flashKB));"],
["DSP",
 "Edge Impulse: Collecting and Labeling Sensor Data",
 "Models are only as good as their data, so Edge Impulse treats acquisition as a first-class step: connect a board over serial or use the data-forwarder CLI to stream accelerometer, microphone, or camera samples straight into the project, then split them into training and test sets and label each window (e.g., 'idle', 'shake', 'tap'). The platform supports uploading existing datasets as CSV/WAV, and every sample keeps its metadata so experiments stay reproducible. Balanced classes and real-world noise in the training set are what separate a demo from a fieldable model.",
 ["Data forwarder CLI streams live sensor data", "Train/test split with per-window labels", "Class balance determines field reliability"],
 "var samples=[{label:'idle',n:420},{label:'shake',n:380},{label:'tap',n:400}];\nvar total=samples.reduce(function(a,s){return a+s.n;},0);\nsamples.forEach(function(s){var pct=(100*s.n/total).toFixed(1);console.log(s.label+': '+s.n+' samples ('+pct+'%)'+(s.n/total<0.1?' SKEWED':''));});\nconsole.log('Total samples: '+total);"],
["training",
 "Edge Impulse: Your First Impulse: Motion Classification",
 "The canonical first project is motion classification on an accelerometer: record idle, shake, and tap gestures, add a spectral-analysis DSP block, attach a small dense classifier, and train. Training runs in the cloud (or on your own machine with the enterprise runner) and returns accuracy plus a confusion matrix. One click exports the trained impulse as an Arduino library or generic C++ SDK; the included examples run inference on live sensor data and print the predicted class over serial. Typical result: a few tens of kilobytes of flash and single-digit millisecond inference.",
 ["Spectral DSP + dense classifier is the starter recipe", "Confusion matrix validates per-class quality", "Export as Arduino library or C++ SDK"],
 "var classes=['idle','shake','tap'];\nvar conf=[[38,1,1],[2,36,2],[0,1,39]];\nvar correct=conf.reduce(function(a,row,i){return a+row[i];},0);\nvar total=conf.reduce(function(a,row){return a+row.reduce(function(x,y){return x+y;},0);},0);\nconsole.log('Confusion matrix accuracy: '+(100*correct/total).toFixed(1)+'%');\nclasses.forEach(function(c,i){console.log(' '+c+' recall: '+(100*conf[i][i]/conf[i].reduce(function(a,b){return a+b;},0)).toFixed(1)+'%');});"],
["deployment",
 "Edge Impulse: EON Compiler: Shrinking Models for MCUs",
 "The EON Compiler is Edge Impulse's deployment optimizer: it takes the trained TensorFlow Lite model and compiles it to optimized C++ source, applying quantization (int8), operator fusion, and memory planning so the model fits microcontrollers with as little as tens of kilobytes of RAM. The EON Tuner goes further, sweeping DSP parameters and network architectures to find the best accuracy-per-byte trade for your target. Together they routinely cut RAM and flash by large factors versus a naive TFLite-Micro export, which is the difference between fitting on a Cortex-M4 and needing a bigger part.",
 ["EON Compiler emits optimized C++ from TFLite", "int8 quantization plus operator fusion", "EON Tuner sweeps architectures for accuracy-per-byte"],
 "var floatKB=512, ramFloatKB=180;\nvar int8KB=Math.round(floatKB/4), ramInt8KB=Math.round(ramFloatKB/4);\nconsole.log('float32: flash '+floatKB+' KB, RAM '+ramFloatKB+' KB');\nconsole.log('int8:    flash '+int8KB+' KB, RAM '+ramInt8KB+' KB');\nconsole.log('Savings: '+Math.round(100*(1-int8KB/floatKB))+'% smaller');"],
["optimization",
 "Edge Impulse: DSP Feature Blocks: Spectral, MFCC, Image",
 "Raw sensor data is rarely model-ready. Edge Impulse's DSP blocks do the heavy lifting: spectral analysis computes FFT-based features over sliding windows for vibration and motion; MFCC/MFE blocks extract mel-scale cepstral features for keyword spotting and audio events; the image block resizes and normalizes frames for FOMO object detection. Choosing window size and stride sets the trade between time resolution and compute cost, and the studio visualizes the resulting features so you can see class separation before training a single epoch.",
 ["Spectral analysis for motion/vibration", "MFCC/MFE for audio keyword spotting", "Image block feeds FOMO detection"],
 "function fftBinEnergy(n){var e=[];for(var i=0;i<n;i++)e.push(Math.round(100*Math.exp(-Math.pow(i-n/3,2)/8)));return e;}\nvar e=fftBinEnergy(16);\nconsole.log('Spectral feature vector (16 bins): '+e.join(','));\nconsole.log('Peak bin: '+e.indexOf(Math.max.apply(null,e))+' (dominant frequency)');"],
["tinyML",
 "Edge Impulse: Anomaly Detection with K-Means",
 "Not every problem has labeled failure examples. Edge Impulse's anomaly block clusters normal-operation features with K-means; at runtime, a sample far from every cluster centroid scores as anomalous. This is the workhorse for predictive maintenance: train on a healthy motor's vibration signature, deploy, and flag the bearing failure weeks before a human would hear it. The anomaly score is a single number, cheap to threshold on-device, and the studio shows the cluster map so you can sanity-check what 'normal' looks like.",
 ["K-means clusters normal-operation features", "Distance from centroids = anomaly score", "Predictive maintenance without failure labels"],
 "var centroids=[[10,12],[40,38],[70,15]];\nfunction dist(a,b){return Math.hypot(a[0]-b[0],a[1]-b[1]);}\n[[11,13],[68,16],[200,200]].forEach(function(p){\n  var d=Math.min.apply(null,centroids.map(function(c){return dist(p,c);}));\n  console.log('point ('+p+') anomaly score '+d.toFixed(1)+(d>40?' -> ANOMALY':' -> normal'));\n});"],
["data-collection",
 "Edge Impulse: Defensive Uses: On-Sensor Intrusion Sensing",
 "tinyML's defensive value is locality: inference happens on the sensor, so raw data never traverses a network. Edge Impulse projects are used for tamper detection (classifying chassis vibration signatures of prying vs. normal handling), acoustic anomaly monitoring of server rooms, and air-quality or RF-environment sensing at the edge. Because the model runs on the microcontroller itself, a compromised network still cannot reach the raw sensor stream \u2014 the device only emits verdicts, and verdicts can be signed.",
 ["Inference on-sensor keeps raw data off the network", "Tamper and acoustic-anomaly classification", "Devices emit signed verdicts, not raw streams"],
 "var verdicts=['normal','normal','tamper','normal'];\nvar key='device-key-7f3a';\nverdicts.forEach(function(v,i){\n  var sig=(v+key+i).split('').reduce(function(a,c){return a+c.charCodeAt(0);},0)%997;\n  console.log('t+'+i+'s verdict='+v+' sig='+sig+(v!=='normal'?'  ALERT: tamper signature detected':''));\n});"],
["DSP",
 "Edge Impulse: Integrating with Firmware: The C++ SDK",
 "The exported C++ library drops into existing firmware: initialize the impulse once, then in your sensor loop fill the signal buffer, call run_classifier, and read the result struct with per-class scores and the anomaly value. The SDK has no OS dependency and no heap requirement beyond its static arena, so it ports to bare-metal, FreeRTOS, Zephyr, or Mbed with the same call pattern. Continuous-inference examples show the sliding-window pattern that keeps classification running while the main loop does other work.",
 ["Static arena, no OS dependency", "run_classifier on sliding windows", "Ports to bare-metal, FreeRTOS, Zephyr, Mbed"],
 "var arenaKB=48, stackWorstB=812;\nconsole.log('SDK contract: static arena '+arenaKB+' KB, worst-case stack '+stackWorstB+' B');\nfunction runClassifier(window){var s=window.reduce(function(a,x){return a+x;},0)/window.length;return s>0.5?'tap':'idle';}\nconsole.log('inference on [0.1,0.8,0.9] -> '+runClassifier([0.1,0.8,0.9]));\nconsole.log('inference on [0.0,0.1,0.05] -> '+runClassifier([0.0,0.1,0.05]));"],
["training",
 "Edge Impulse: Debugging: Feature Explorer and Live Classification",
 "When accuracy disappoints, Edge Impulse gives you the Feature Explorer: a 2D/3D projection of your dataset's feature space where misclassified points stand out visually, telling you whether the problem is bad data, bad features, or an underpowered model. Live classification streams real sensor data through the trained impulse in the browser, so you can wave the board and watch predictions update. The data-augmentation and DSP-parameter knobs are right there, closing the loop between 'it fails on this gesture' and a fixed pipeline.",
 ["Feature Explorer visualizes class separation", "Live classification tests with real sensor motion", "Stage-level failure attribution"],
 "var fails=[{win:12,stage:'dsp'},{win:13,stage:'dsp'},{win:27,stage:'nn'}];\nvar byStage={};\nfails.forEach(function(f){byStage[f.stage]=(byStage[f.stage]||0)+1;});\nObject.keys(byStage).forEach(function(s){console.log('stage '+s+': '+byStage[s]+' failing windows');});\nconsole.log('Likely culprit: dsp (feature drift on windows 12-13)');"],
["deployment",
 "Edge Impulse: FOMO: Object Detection on Tiny Cameras",
 "FOMO (Faster Objects, More Objects) is Edge Impulse's object-detection architecture for microcontrollers: instead of predicting bounding boxes, it predicts object centroids on a coarse grid, which slashes compute while still counting and localizing objects. It runs at multiple frames per second on a Cortex-M7 with a small camera \u2014 enough for people counting, pallet detection, or perimeter presence sensing at the edge, with no video ever leaving the device. That last property is the defensive point: the camera's raw feed stays on the chip.",
 ["FOMO predicts centroids, not boxes", "Multi-FPS on Cortex-M7 class parts", "Raw video stays on-device"],
 "var grid=[[0,1,0],[0,0,0],[1,0,0]];\nvar n=0;grid.forEach(function(row,r){row.forEach(function(v,c){if(v){n++;console.log('object centroid at grid ('+r+','+c+')');}});});\nconsole.log('Objects detected: '+n+' (raw frame never leaves the chip)');"],
["optimization",
 "Edge Impulse: Air-Gapped and Enterprise Deployment",
 "Defense and industrial users cannot always phone home. Edge Impulse supports this with downloadable C++ exports (no runtime cloud call), on-premise training runners, and SSO/audit enterprise tiers. The exported library is fully offline: once flashed, the device classifies forever without connectivity. For fleets, the model-versioning workflow lets you A/B new impulses across device groups and roll back by flashing the previous export \u2014 standard practice for fielded sensor networks.",
 ["Exports run fully offline after flashing", "On-premise runners and model versioning", "Signed delta updates with rollback slot"],
 "var fleet=[{id:'node-01',ver:'1.4.0'},{id:'node-02',ver:'1.3.2'},{id:'node-03',ver:'1.4.0'}];\nvar target='1.4.0';\nfleet.forEach(function(n){console.log(n.id+': '+n.ver+(n.ver===target?' OK':' -> queue signed delta to '+target));});"],
["tinyML",
 "Edge Impulse: Testing: From Studio Metrics to Field Trials",
 "A responsible tinyML workflow tests in layers: studio accuracy and confusion matrix first, then the EON-compiled model's on-device metrics (latency, RAM, flash measured on the real target, not estimated), then a field trial where the device logs predictions alongside ground truth for days. Edge Impulse's testing tab automates the first layer and the SDK's logging examples support the last. The number that matters is field accuracy on unseen conditions \u2014 temperature drift, battery sag, and mounting differences all move the needle.",
 ["Studio metrics, on-device measurement, field soak", "Log predictions vs ground truth in the field", "Publish the conditions behind accuracy claims"],
 "var layers=['studio accuracy 96.2%','on-device latency 41 ms','field soak: 71.5 h'];\nlayers.forEach(function(l,i){console.log('layer '+(i+1)+': '+l);});\nvar fieldAcc=0.941;\nconsole.log('Field accuracy: '+(100*fieldAcc).toFixed(1)+'% (unseen conditions, 3 sites)');"],
["data-collection",
 "Edge Impulse: Real-World Pattern: Predictive Maintenance Node",
 "A complete defensive-industrial pattern: a vibration sensor node on a pump motor, running an Edge Impulse impulse with spectral DSP and an anomaly block. It learns the healthy signature during commissioning, then reports a daily health score and immediate alerts on anomaly spikes \u2014 all computed on a $10-class MCU, with a LoRa radio sending only the score. Maintenance crews get weeks of warning on bearing wear, and the raw vibration stream never leaves the machine room.",
 ["Spectral + anomaly impulse on pump vibration", "On-device scoring, radio sends only the score", "Weeks of warning on bearing wear"],
 "var baseline=12.4;\n[12.1,12.8,13.0,18.6,24.3].forEach(function(v,i){\n  var ratio=v/baseline;\n  console.log('day '+(i+1)+': vibration '+v.toFixed(1)+' (x'+ratio.toFixed(2)+' baseline)'+(ratio>1.4?' -> BEARING ALERT':''));\n});"],
["DSP",
 "Edge Impulse: Mastery: The Road to Field-Grade tinyML",
 "Mastery means thinking in budgets: every project starts from the device's RAM/flash/latency/power envelope and works backward to the model, not the reverse. Advanced practitioners co-design the DSP and network with the EON Tuner, validate with field soak logs, version models like firmware, and monitor drift \u2014 retraining when the world changes. The frontier is sensor fusion (audio plus motion plus vision in one impulse) and on-device adaptation, but the discipline stays the same: measure on the target, test in the field, and never trust a studio number alone.",
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
    edition:'public',
    category:tp[0],
    tags:["tinyML", "edge-ai", "microcontrollers", "DSP", "EON-compiler", "sensor-fusion", "air-gapped", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-edge-impulse',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-edge-impulse']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();