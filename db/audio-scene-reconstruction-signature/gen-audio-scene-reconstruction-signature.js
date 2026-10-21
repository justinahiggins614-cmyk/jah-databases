(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["source-separation", "spatial-audio", "room-acoustics", "enhancement", "localization"];
var PREFIX='JAH-AUDIOS2-S-';
var USE="Used in hearing aids, conference systems, VR audio, forensic audio, and film post-production.";
var FLD=[["technique", "Technique"], ["inputs", "Inputs"], ["output", "Output"]];
var DEMO="# {title} - SNR improvement check (python3)\nsnr_in={d1}\nsnr_out={d2}\ntarget={d3}\ngain=snr_out-snr_in\nprint(\"SNR gain: %.1f dB (%.1f -> %.1f)\" % (gain, snr_in, snr_out))\nprint(\"TARGET MET\" if snr_out >= target else \"BELOW TARGET\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["source-separation", "Blind Source Separation", "Separates mixed audio into individual sources using only statistical independence, no prior knowledge of the sources.", "Blind Source Separation", "multi-channel mixture", "isolated source stems", "2.0", "14.5", "12.0"], ["spatial-audio", "Beamforming", "Combines microphone array signals with delays and weights to amplify sound from one direction while suppressing others.", "Beamforming", "array recordings", "directionally enhanced audio", "0.0", "11.0", "10.0"], ["room-acoustics", "Room Impulse Response Estimation", "Recovers the acoustic fingerprint of a room from recordings, capturing reflections, reverb time, and frequency response.", "Room Impulse Response Estimation", "sweeps or speech in room", "impulse response (RIR)", "-5.0", "18.0", "15.0"], ["enhancement", "Spatial Audio Rendering", "Places reconstructed sources in 3D space using HRTFs or Ambisonics so listeners perceive direction and distance.", "Spatial Audio Rendering", "source stems + positions", "binaural or Ambisonic mix", "3.0", "16.0", "14.0"], ["localization", "Dereverberation", "Removes room reflections from speech recordings, restoring clarity for recognition and listening.", "Dereverberation", "reverberant speech", "dry speech estimate", "1.0", "13.0", "12.0"], ["source-separation", "Speaker Diarization", "Answers who spoke when by segmenting audio and clustering speaker embeddings across the recording.", "Speaker Diarization", "meeting recording", "speaker-labeled timeline", "4.0", "15.5", "13.0"], ["spatial-audio", "Sound Event Localization", "Detects sound events and estimates their direction of arrival from array phase differences.", "Sound Event Localization", "array audio", "event labels + azimuth/elevation", "-2.0", "12.5", "11.0"], ["room-acoustics", "Ambisonics Decoding", "Converts spherical-harmonic Ambisonic recordings into speaker feeds or binaural audio for any playback layout.", "Ambisonics Decoding", "B-format audio", "decoded playback mix", "5.0", "17.0", "15.0"], ["enhancement", "Acoustic Echo Modeling", "Models the echo path between loudspeaker and microphone so echo cancellers can subtract it.", "Acoustic Echo Modeling", "far-end + mic signals", "echo-free near-end", "-8.0", "20.0", "18.0"], ["localization", "Noise Field Mapping", "Estimates the spatial distribution of background noise to steer enhancement toward the quietest directions.", "Noise Field Mapping", "array noise samples", "noise field map", "0.0", "9.5", "9.0"], ["source-separation", "Binaural Rendering", "Synthesizes two-ear signals with interaural time and level differences for headphone spatialization.", "Binaural Rendering", "mono sources + HRTFs", "binaural stereo", "2.0", "14.0", "13.0"], ["spatial-audio", "Microphone Array Calibration", "Estimates array geometry and channel mismatches from test signals so downstream algorithms stay accurate.", "Microphone Array Calibration", "calibration recordings", "geometry + gain corrections", "1.0", "12.0", "11.0"], ["room-acoustics", "Wavefield Synthesis", "Reconstructs a physical sound field with dense loudspeaker arrays using the Kirchhoff-Helmholtz integral.", "Wavefield Synthesis", "source positions", "driving signals per speaker", "-3.0", "13.5", "12.0"], ["enhancement", "Parametric Spatial Coding", "Encodes direction and diffuseness parameters per time-frequency tile for efficient spatial audio transmission.", "Parametric Spatial Coding", "multichannel audio", "compact spatial parameters", "6.0", "16.5", "15.0"], ["localization", "Distance Estimation", "Infers source distance from direct-to-reverberant ratio and level cues in the recording.", "Distance Estimation", "single or array mic", "distance estimate in meters", "0.0", "8.0", "7.0"], ["source-separation", "Reflection Tracking", "Tracks early reflections over time to reconstruct room geometry and moving reflectors.", "Reflection Tracking", "RIR sequence", "reflector trajectories", "-4.0", "11.5", "10.0"], ["spatial-audio", "Occlusion Modeling", "Models how obstacles attenuate and diffract sound so virtual sources behind objects sound correct.", "Occlusion Modeling", "scene geometry", "occlusion filters", "-1.0", "10.0", "9.0"], ["room-acoustics", "Multi-channel Wiener Filtering", "Optimal linear estimator that suppresses noise across channels using estimated speech and noise statistics.", "Multi-channel Wiener Filtering", "noisy multichannel", "enhanced speech", "0.0", "12.8", "12.0"], ["enhancement", "Neural Acoustic Fields", "Learns a continuous neural representation of a room's acoustics from sparse recordings for novel-listener rendering.", "Neural Acoustic Fields", "sparse recordings", "queryable acoustic field", "-6.0", "15.0", "13.0"], ["localization", "Foley Reconstruction", "Rebuilds missing production sound with synthesized or library-matched effects aligned to picture.", "Foley Reconstruction", "video + script notes", "finished foley track", "-10.0", "19.0", "17.0"]];
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
var gen={version:'jahdb-audio-scene-reconstruction-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('audio-scene-reconstruction-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
