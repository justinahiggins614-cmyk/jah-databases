(function(){'use strict';
/* JAH The Text-to-Image AI Image-Making Database generator — jahdb-image-making-text-to-image-ai-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMTI-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["How Diffusion Models Make Images", "Anatomy of a Great Prompt", "Samplers and Steps", "CFG Scale: Prompt Obedience", "Seeds: Controlling Randomness", "Negative Prompts That Work", "Aspect Ratios and Composition", "Styles: Photoreal to Anime", "Fixing Hands and Faces", "Upscaling AI Generations", "Inpainting Fixes on Generations"], "Compounded": ["Prompt Weighting and Emphasis", "Checkpoints and Fine-Tunes", "LoRAs: Teaching Concepts", "ControlNet: Posing the Model", "ComfyUI Workflows", "Batch Generation and X/Y Plots", "Ethics and Disclosure", "Copyright and AI Images", "Training Your Own Checkpoint", "Prompt Libraries and Versioning", "AI for Concept Art", "Photorealism Techniques"], "Advanced": ["Avoiding the AI Look", "Selling AI-Assisted Art", "The Future: Video and 3D from Diffusion", "Regional Prompting and Composition Control", "IP-Adapter: Image Prompts", "Multi-ControlNet Stacks", "Training LoRAs Professionally", "Dataset Curation for Training", "Model Merging", "API Deployment of Diffusion Models", "The AI Art Director's Workflow"]};
var DEMOKIND="prompt planning";
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
    name:topic+' — text-to-image ai image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A text-to-image ai image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
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
var gen={version:'jahdb-image-making-text-to-image-ai-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-text-to-image-ai-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
