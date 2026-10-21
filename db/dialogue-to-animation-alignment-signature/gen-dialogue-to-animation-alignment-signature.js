(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["lip-sync", "gesture", "facial-animation", "timing", "multilingual"];
var PREFIX='JAH-DIALOG-S-';
var USE="Used in animated films, games, virtual avatars, dubbing, and real-time VTuber pipelines.";
var FLD=[["method", "Method"], ["input", "Input"], ["output", "Output"]];
var DEMO="# {title} - phoneme rate check (python3)\nphonemes={d1}\nseconds={d2}\nmax_rate={d3}\nrate=phonemes/seconds\nprint(\"phoneme rate: %.1f per second\" % rate)\nprint(\"NATURAL PACING\" if rate <= max_rate else \"TOO FAST - retime\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["lip-sync", "Phoneme Forced Alignment", "Aligns a phoneme sequence to audio with an HMM or neural aligner, giving millisecond-accurate phoneme boundaries.", "Phoneme Forced Alignment", "audio + transcript", "phoneme timestamps", "42", "3.1", "18.0"], ["gesture", "Viseme Mapping", "Converts phonemes to visual mouth shapes (visemes), collapsing acoustically distinct but visually similar sounds.", "Viseme Mapping", "phoneme stream", "viseme sequence", "38", "2.8", "18.0"], ["facial-animation", "Lip-Sync Curve Fitting", "Fits smooth jaw and lip animation curves to the viseme timeline, avoiding robotic popping between poses.", "Lip-Sync Curve Fitting", "viseme timeline", "animation curves", "45", "3.4", "18.0"], ["timing", "Prosody-to-Gesture Mapping", "Drives hand and body gestures from speech prosody (pitch, energy, rhythm) so movement matches vocal emphasis.", "Prosody-to-Gesture Mapping", "prosody features", "gesture triggers", "30", "4.2", "18.0"], ["multilingual", "Emotion-to-Expression Transfer", "Maps detected vocal emotion onto facial expression parameters blended with the lip-sync layer.", "Emotion-to-Expression Transfer", "emotion labels", "expression weights", "28", "3.0", "18.0"], ["lip-sync", "Beat Gesture Alignment", "Places rhythmic beat gestures on stressed syllables detected from the audio envelope.", "Beat Gesture Alignment", "audio envelope", "gesture beat times", "36", "2.5", "18.0"], ["gesture", "Gaze Targeting", "Directs character eye gaze to the current speaker or referenced object during dialogue turns.", "Gaze Targeting", "dialogue turns", "gaze targets", "24", "5.0", "18.0"], ["facial-animation", "Blink Synchronization", "Schedules natural blinks at phrase boundaries and cognitive pauses instead of random intervals.", "Blink Synchronization", "phrase boundaries", "blink times", "20", "6.0", "18.0"], ["timing", "Jaw Kinematics", "Drives a physically plausible jaw joint from vowel openness, keeping lip-sync anatomically consistent.", "Jaw Kinematics", "vowel openness", "jaw rotation", "40", "3.2", "18.0"], ["multilingual", "Tongue Modeling", "Animates tongue position for alveolar and dental sounds where tongue visibility sells the phoneme.", "Tongue Modeling", "phoneme classes", "tongue pose", "33", "2.9", "18.0"], ["lip-sync", "Co-articulation Modeling", "Blends neighboring visemes so mouth shapes anticipate upcoming sounds like real speech.", "Co-articulation Modeling", "viseme context window", "blended mouth shapes", "44", "3.3", "18.0"], ["gesture", "Multilingual Viseme Sets", "Uses language-specific viseme inventories so dubbed dialogue matches mouth shapes in each language.", "Multilingual Viseme Sets", "language tag + phonemes", "localized visemes", "39", "3.0", "18.0"], ["facial-animation", "Real-time Streaming Alignment", "Aligns incrementally with bounded latency for live avatars, trading some accuracy for immediacy.", "Real-time Streaming Alignment", "streaming audio", "low-latency visemes", "35", "1.2", "25.0"], ["timing", "TTS Viseme Streams", "Extracts viseme timing directly from text-to-speech synthesis internals, perfectly synced by construction.", "TTS Viseme Streams", "TTS engine", "viseme + audio streams", "41", "3.5", "18.0"], ["multilingual", "Motion Capture Retargeting", "Retargets captured facial performance onto a different character rig while preserving timing.", "Motion Capture Retargeting", "mocap data", "retargeted animation", "26", "4.0", "18.0"], ["lip-sync", "FACS Mapping", "Translates Facial Action Coding System units into rig controls for anatomically grounded expressions.", "FACS Mapping", "AU activations", "rig control values", "22", "3.8", "18.0"], ["gesture", "Dialogue Beat Detection", "Finds dramatic beats in dialogue from text and audio cues to pace cuts and reaction shots.", "Dialogue Beat Detection", "script + audio", "beat markers", "18", "8.0", "18.0"], ["facial-animation", "Pause and Breath Insertion", "Inserts natural breaths and pauses at syntactic boundaries so long lines do not feel machine-gunned.", "Pause and Breath Insertion", "sentence structure", "breath events", "25", "5.5", "18.0"], ["timing", "Accent Adaptation", "Adjusts viseme timing and mouth shapes for accented speech where phoneme durations differ.", "Accent Adaptation", "accent profile", "adapted timing", "37", "3.1", "18.0"], ["multilingual", "Sign-Language Alignment", "Synchronizes sign-language avatar motion with spoken dialogue timing for accessible broadcasts.", "Sign-Language Alignment", "speech timing", "sign sequence", "30", "6.5", "18.0"]];
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
var gen={version:'jahdb-dialogue-to-animation-alignment-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dialogue-to-animation-alignment-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
