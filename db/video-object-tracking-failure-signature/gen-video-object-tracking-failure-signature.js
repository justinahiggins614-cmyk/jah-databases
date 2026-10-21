(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["occlusion", "drift", "appearance-change", "initialization", "multi-object"];
var PREFIX='JAH-VOTF-S-';
var USE="Used to harden trackers for surveillance, autonomous driving, sports analytics, and video editing tools.";
var FLD=[["failure", "Failure"], ["symptom", "Symptom"], ["mitigation", "Mitigation"]];
var DEMO="# {title} - failure-rate scoring (python3)\nframes={d1}\nfailures={d2}\nmax_rate={d3}\nrate=failures/frames\nprint(\"failure rate: %.4f (%d/%d)\" % (rate, failures, frames))\nprint(\"ACCEPTABLE\" if rate <= max_rate else \"MITIGATION REQUIRED\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["occlusion", "Occlusion", "The target is hidden behind another object, so the tracker has no pixels to match and either freezes or latches onto the occluder.", "Occlusion", "bounding box sticks to occluder", "short-term memory + re-detection on reappearance", "1200", "18", "0.02"], ["drift", "Motion Blur", "Fast target or camera motion smears the target's appearance, breaking template and feature matching.", "Motion Blur", "box drifts or shrinks", "deblur-aware features, higher frame rate", "900", "27", "0.02"], ["appearance-change", "Illumination Change", "Sudden lighting shifts change pixel values beyond the appearance model's tolerance, causing match scores to collapse.", "Illumination Change", "confidence collapse", "illumination-invariant descriptors, online model update", "1500", "22", "0.02"], ["initialization", "Scale Change", "The target grows or shrinks dramatically as it approaches or recedes, and fixed-scale trackers lose it.", "Scale Change", "box no longer covers target", "multi-scale search, scale estimation", "1100", "15", "0.02"], ["multi-object", "Deformation", "Non-rigid targets (people, animals) change shape, defeating rigid templates.", "Deformation", "partial overlap, jitter", "part-based models, segmentation masks", "1300", "31", "0.02"], ["occlusion", "Fast Motion", "Displacement between frames exceeds the tracker's search window, so the target is never found.", "Fast Motion", "target jumps out of box", "motion prediction, wider search", "800", "35", "0.03"], ["drift", "Background Clutter", "Background regions resemble the target, pulling the tracker toward distractors with similar color or texture.", "Background Clutter", "box slides to background", "discriminative correlation filters", "1400", "26", "0.02"], ["appearance-change", "ID Switch", "In multi-object tracking, two identities swap when targets cross, corrupting downstream analytics.", "ID Switch", "identities exchanged", "appearance re-identification embeddings", "2000", "12", "0.01"], ["initialization", "Model Drift", "Incremental template updates absorb background pixels over time until the model no longer represents the target.", "Model Drift", "slowly expanding box", "conservative update, update gating", "1600", "20", "0.02"], ["multi-object", "Re-identification Failure", "After long disappearance the target returns but the re-ID embedding fails to match, spawning a new identity.", "Re-identification Failure", "duplicate track created", "stronger re-ID features, gallery update", "1800", "16", "0.01"], ["occlusion", "Camera Motion", "Aggressive camera pan or shake moves the whole scene, violating the tracker's smooth-motion assumption.", "Camera Motion", "global box shift", "camera-motion compensation, gyro input", "1000", "24", "0.02"], ["drift", "Out-of-View Exit", "The target leaves the frame entirely; trackers that keep predicting hallucinate a phantom box.", "Out-of-View Exit", "box stuck at frame edge", "exit detection + track termination", "700", "9", "0.02"], ["appearance-change", "Similar Distractors", "Another object of the same class and color competes for the match score.", "Similar Distractors", "box oscillates between objects", "distractor-aware training", "1250", "29", "0.02"], ["initialization", "Low Resolution", "Small targets offer too few pixels for reliable features, so matches are dominated by noise.", "Low Resolution", "jittery unstable box", "super-resolution, motion cues", "950", "33", "0.03"], ["multi-object", "Initialization Error", "A bad first box (wrong size or position) poisons the appearance model from frame one.", "Initialization Error", "immediate drift", "detector-based init, box refinement", "600", "21", "0.03"], ["occlusion", "Template Corruption", "A single bad update writes occluder pixels into the template, permanently degrading it.", "Template Corruption", "sudden quality drop", "update rollback on low confidence", "1350", "17", "0.02"], ["drift", "Long-term Disappearance", "Targets gone for minutes exceed any motion model, so prediction uncertainty explodes.", "Long-term Disappearance", "lost track", "global re-detection sweeps", "2200", "14", "0.01"], ["appearance-change", "Multi-object Merge", "Two nearby targets merge into one detection, collapsing two tracks into a single box.", "Multi-object Merge", "track count drops", "detection-level splitting", "1700", "19", "0.02"], ["initialization", "Depth Ambiguity", "In 2D tracking, overlapping targets at different depths are indistinguishable without depth cues.", "Depth Ambiguity", "wrong target followed", "depth or stereo input", "1050", "23", "0.02"], ["multi-object", "Adversarial Patch", "A crafted pattern on the target or background fools the tracker's learned features.", "Adversarial Patch", "confident wrong box", "adversarial training, randomized smoothing", "500", "41", "0.05"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-video-object-tracking-failure-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-object-tracking-failure-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
