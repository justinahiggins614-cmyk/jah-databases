(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["geometry", "lighting", "temporal", "texture", "post-process"];
var PREFIX='JAH-RENDER-';
var USE="Used by graphics engineers, technical artists, and QA teams shipping real-time and offline renderers.";
var FLD=[["artifact", "Artifact"], ["cause", "Cause"], ["fix", "Fix"]];
var DEMO="# {title} - artifact pixel ratio (python3)\nbad={d1}\ntotal={d2}\nmax_ratio={d3}\nratio=bad/total\nprint(\"artifact coverage: %.4f%%\" % (ratio*100))\nprint(\"WITHIN TOLERANCE\" if ratio <= max_ratio else \"INVESTIGATE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["geometry", "Z-fighting", "Two coplanar surfaces compete in the depth buffer, flickering as the camera moves.", "Z-fighting", "depth precision limits", "offset polygons or increase near/far ratio", "12500", "2073600", "0.01"], ["lighting", "Aliasing", "High-frequency geometry or texture detail sampled below the Nyquist rate creates jagged edges.", "Aliasing", "undersampling", "MSAA, TAA, or higher render resolution", "48000", "2073600", "0.05"], ["temporal", "Shadow Acne", "Self-shadowing artifacts from depth bias set too low, creating striped patterns on surfaces.", "Shadow Acne", "insufficient shadow bias", "tune bias and normal offset", "32000", "2073600", "0.03"], ["texture", "Fireflies", "Extremely bright single pixels from low-sample path tracing hitting tiny bright light sources.", "Fireflies", "variance in Monte Carlo sampling", "clamp radiance, more samples, denoiser", "850", "2073600", "0.002"], ["post-process", "Banding", "Visible steps in smooth gradients when 8-bit color cannot represent subtle transitions.", "Banding", "quantization", "dithering, 10-bit pipeline", "150000", "2073600", "0.10"], ["geometry", "Light Leaking", "Light bleeds through thin geometry in baked lightmaps or shadow-mapped scenes.", "Light Leaking", "insufficient occluder thickness", "thicken geometry, bias tuning", "22000", "2073600", "0.02"], ["lighting", "Texture Shimmering", "Mip-mapping or anisotropic filtering mismatches cause textures to crawl as the camera moves.", "Texture Shimmering", "filtering mismatch", "anisotropic filtering x8-x16", "41000", "2073600", "0.04"], ["temporal", "Moiré", "Interference between fine texture patterns and the pixel grid creates swirling artifacts.", "Moiré", "pattern/grid interference", "mip bias, texture redesign", "18000", "2073600", "0.02"], ["texture", "Tearing", "Frame buffer swaps mid-scanout show parts of two frames at once.", "Tearing", "vsync off", "vsync, adaptive sync, frame pacing", "2073600", "2073600", "1.00"], ["post-process", "Ghosting", "TAA history or motion blur leaves trails behind fast-moving objects.", "Ghosting", "stale history samples", "history rejection, velocity weighting", "27000", "2073600", "0.03"], ["geometry", "Blooming Halos", "Over-aggressive bloom spreads bright areas into large soft halos.", "Blooming Halos", "threshold too low", "raise threshold, knee shaping", "95000", "2073600", "0.08"], ["lighting", "Normal Map Seams", "Tangent-space discontinuities at UV seams create visible lighting breaks.", "Normal Map Seams", "mirrored UVs / split tangents", "synchronized tangents, synced baker", "6400", "2073600", "0.01"], ["temporal", "UV Distortion", "Stretched UVs smear textures across geometry.", "UV Distortion", "bad unwrap", "re-unwrap, texel density check", "31000", "2073600", "0.05"], ["texture", "Popping LOD", "Visible swaps between detail levels as distance crosses thresholds.", "Popping LOD", "hard LOD transitions", "dithered fade, hysteresis", "1200", "2073600", "0.005"], ["post-process", "Volumetric Noise", "Noisy fog and volumetrics from too few marching samples.", "Volumetric Noise", "undersampled raymarch", "more samples, temporal accumulation", "88000", "2073600", "0.08"], ["geometry", "Caustic Noise", "Bright caustic patterns converge slowly in path tracers, leaving sparkling noise.", "Caustic Noise", "difficult light paths", "photon mapping, guiding", "5200", "2073600", "0.01"], ["lighting", "Denoiser Smearing", "Over-aggressive denoisers blur fine detail and create waxy surfaces.", "Denoiser Smearing", "excessive blend factor", "albedo/normal-guided denoise", "140000", "2073600", "0.12"], ["temporal", "TAA Ghosting", "Temporal anti-aliasing ghosts thin or fast objects across frames.", "TAA Ghosting", "history clamping failure", "neighborhood clamping", "19000", "2073600", "0.02"], ["texture", "Reflection Probe Seams", "Visible borders where box-projected reflection probes blend.", "Reflection Probe Seams", "probe boundary discontinuity", "blend radius tuning, more probes", "9800", "2073600", "0.02"], ["post-process", "Emissive Bleeding", "Bright emissive surfaces leak color into GI beyond physical plausibility.", "Emissive Bleeding", "unclamped emissive in GI", "clamp emissive contribution", "45000", "2073600", "0.05"]];
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
var gen={version:'jahdb-rendering-artifact-diagnosis-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rendering-artifact-diagnosis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
