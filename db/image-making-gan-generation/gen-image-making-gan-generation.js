(function(){'use strict';
/* JAH The GAN Generation Image-Making Database generator — jahdb-image-making-gan-generation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMGN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What GANs Are", "Latent Space: The Map of Possibilities", "StyleGAN: Faces and Beyond", "Training a GAN: Data and Discipline", "Deepfakes: How They Work", "GAN Art and Creative Coding", "Image-to-Image with GANs", "Super-Resolution GANs (ESRGAN)", "Inpainting with GANs", "Evaluating GAN Output", "The Ethics of Synthetic Faces"], "Compounded": ["GANs vs Diffusion: Choosing", "Latent Direction Discovery Methods", "Style Mixing in StyleGAN", "Projection: Real Images into Latent Space", "GAN Inversion Techniques", "Text-Guided GAN Editing", "Few-Shot GAN Adaptation", "GANs for Data Augmentation", "Anomaly Detection with GANs", "Super-Resolution Comparisons", "Denoising with GANs", "Paired Translation Masterclass"], "Advanced": ["Training StyleGAN from Scratch", "Dataset Design for GAN Training", "Compute Planning for Training", "Evaluating with Precision and Recall", "Bias in Generative Models", "Watermarking Synthetic Media", "Detection of GAN Images", "Legal Status of Training Data", "GANs in Production Systems", "The Research Frontier: Diffusion vs GAN", "Building a GAN Product"]};
var DEMOKIND="latent planning";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+DEMOKIND+" — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — gan generation image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A gan generation image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-image-making-gan-generation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-gan-generation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
