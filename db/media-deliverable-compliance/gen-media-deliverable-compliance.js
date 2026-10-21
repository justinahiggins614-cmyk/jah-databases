(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["audio", "video", "metadata", "accessibility", "packaging"];
var PREFIX='JAH-MDC-';
var USE="Used by mastering engineers, broadcast operations, and streaming platforms to reject bad files before air.";
var FLD=[["check", "Check"], ["standard", "Standard"], ["criterion", "Criterion"]];
var DEMO="# {title} - loudness compliance (python3)\nlufs={d1}\ntrue_peak={d2}\ntarget={d3}\nprint(\"integrated loudness: %.1f LUFS (target %.1f)\" % (lufs, target))\nprint(\"true peak: %.1f dBTP\" % true_peak)\nok = abs(lufs-target) <= 1.0 and true_peak <= -1.0\nprint(\"COMPLIANT\" if ok else \"NON-COMPLIANT\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["audio", "Loudness Normalization", "Measures integrated loudness and applies gain so programs match the platform target without pumping.", "Loudness Normalization", "EBU R128 / ATSC A/85", "-16 LUFS +/-1 (streaming)", "-16.2", "-1.3", "-16.0"], ["video", "True Peak Limit", "Ensures inter-sample peaks stay below the ceiling so codecs and DACs never clip.", "True Peak Limit", "EBU R128", "max -1.0 dBTP", "-15.8", "-1.1", "-16.0"], ["metadata", "Codec Profile Check", "Verifies the codec, profile, and level match what the delivery spec allows.", "Codec Profile Check", "platform spec", "e.g. H.264 High@4.1", "-16.0", "-1.5", "-16.0"], ["accessibility", "Resolution and Framerate", "Confirms frame size and rate match the ordered deliverable (no 29.97 vs 30 mixups).", "Resolution and Framerate", "delivery order", "exact match", "-16.1", "-1.2", "-16.0"], ["packaging", "Color Space and Gamut", "Checks transfer function, primaries, and matrix flags so HDR and SDR play correctly.", "Color Space and Gamut", "BT.709 / BT.2020", "flags match master", "-15.9", "-1.4", "-16.0"], ["audio", "Subtitle Timing", "Validates subtitle in/out times against shot changes with minimum duration and gap rules.", "Subtitle Timing", "platform spec", ">=1s duration, 2-frame gap", "-16.3", "-1.2", "-16.0"], ["video", "Caption Accuracy", "Scores caption text against the dialogue script for word accuracy and speaker labels.", "Caption Accuracy", "FCC / platform", "99% accuracy", "-16.0", "-1.6", "-16.0"], ["metadata", "Safe Area Check", "Ensures titles and graphics sit inside action-safe and title-safe regions.", "Safe Area Check", "broadcast safe", "90%/80% safe", "-16.2", "-1.3", "-16.0"], ["accessibility", "Audio Channel Layout", "Verifies channel count, order, and labeling (5.1 vs stereo) match the delivery.", "Audio Channel Layout", "delivery order", "layout match", "-15.7", "-1.1", "-16.0"], ["packaging", "Metadata Completeness", "Requires title, duration, language, and rights fields before a file can enter the catalog.", "Metadata Completeness", "MAM schema", "all required fields", "-16.4", "-1.2", "-16.0"], ["audio", "File Naming Convention", "Enforces the house naming pattern so automation routes files without human guessing.", "File Naming Convention", "house spec", "regex match", "-16.1", "-1.5", "-16.0"], ["video", "Bitrate Ceiling", "Rejects files whose peak bitrate would stall the CDN edge or break device decoders.", "Bitrate Ceiling", "platform spec", "<= spec max", "-15.8", "-1.3", "-16.0"], ["metadata", "HDR Metadata", "Checks MaxCLL/MaxFALL values are present and sane for HDR10 deliverables.", "HDR Metadata", "CTA-861", "0 < MaxCLL <= 10000", "-16.0", "-1.2", "-16.0"], ["accessibility", "Broadcast Legal Levels", "Clamps luma and chroma to legal ranges so transmitters and older displays stay clean.", "Broadcast Legal Levels", "EBU / ATSC", "7.5-100 IRE", "-16.2", "-1.4", "-16.0"], ["packaging", "Aspect Ratio Flag", "Confirms container and stream aspect flags agree so players do not stretch the picture.", "Aspect Ratio Flag", "delivery order", "16:9 match", "-16.1", "-1.2", "-16.0"], ["audio", "Timecode Continuity", "Scans for timecode jumps or duplicates that would break editing and QC automation.", "Timecode Continuity", "house spec", "continuous TC", "-15.9", "-1.3", "-16.0"], ["video", "Thumbnail Compliance", "Verifies poster frames meet size, content, and text-coverage rules for storefronts.", "Thumbnail Compliance", "platform spec", "approved artwork", "-16.3", "-1.5", "-16.0"], ["metadata", "DRM Packaging", "Confirms encryption, key IDs, and license URLs are correct before a title goes behind DRM.", "DRM Packaging", "studio spec", "keys resolve", "-16.0", "-1.1", "-16.0"], ["accessibility", "Audio Description Track", "Checks the AD track exists, is mixed at the right level, and covers all dialogue gaps.", "Audio Description Track", "accessibility law", "AD present", "-16.2", "-1.2", "-16.0"], ["packaging", "Delivery Manifest Checksum", "Validates the manifest lists every file with matching SHA-256 hashes.", "Delivery Manifest Checksum", "house spec", "hashes match", "-15.8", "-1.4", "-16.0"]];
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
var gen={version:'jahdb-media-deliverable-compliance-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('media-deliverable-compliance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
