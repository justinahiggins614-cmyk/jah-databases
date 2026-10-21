(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["framework", "conversion", "quantization", "runtime", "benchmark", "deployment"] */
var CATS=["framework", "conversion", "quantization", "runtime", "benchmark", "deployment"];
var PREFIX='JAH-EDGEAI-';
var FIELDS=["platform", "model_format", "min_requirements", "conversion"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["framework", "Core ML", "Apple's on-device ML framework: run models on iPhone/Mac with the Neural Engine.", "Core ML deploys models on Apple devices, executing on the Neural Engine, GPU, or CPU via a unified API. Models convert from PyTorch/TensorFlow with coremltools, and iOS 17+ supports transformer architectures natively. It powers on-device Siri, camera features, and third-party apps — with privacy as the pitch: data never leaves the device.", "iOS/macOS", ".mlpackage / .mlmodel", "iOS 15+ for transformers; Neural Engine recommended", "coremltools from PyTorch/TF", "python", "Convert with coremltools", "import torch, coremltools as ct\nmodel = torch.nn.Sequential(torch.nn.Linear(10, 2)).eval()\ntraced = torch.jit.trace(model, torch.randn(1, 10))\nmlmodel = ct.convert(traced, inputs=[ct.TensorType(shape=(1, 10))])\nprint(\"converted:\", type(mlmodel).__name__)"],
 ["framework", "TensorFlow Lite", "Google's mobile inference runtime: small, fast models on Android, iOS, and microcontrollers.", "TensorFlow Lite runs quantized and pruned models on phones and embedded devices with delegates for GPU (Metal/OpenGL), NNAPI, and Hexagon DSP. The TFLite converter applies post-training quantization and operator fusion; the Model Maker simplifies retraining. It remains the default for Android on-device ML and TinyML on microcontrollers.", "Android/iOS/embedded", ".tflite (FlatBuffer)", "Varies; TinyML runs on MCUs", "TFLiteConverter from TF/Keras", "python", "Convert to TFLite with quantization", "import tensorflow as tf\nmodel = tf.keras.Sequential([tf.keras.layers.Dense(2, input_shape=(10,))])\nconv = tf.lite.TFLiteConverter.from_keras_model(model)\nconv.optimizations = [tf.lite.Optimize.DEFAULT]\ntflite = conv.convert()\nprint(\"tflite bytes:\", len(tflite))"],
 ["framework", "ONNX Runtime Mobile", "Run ONNX models on phones with hardware accelerators via execution providers.", "ONNX Runtime Mobile executes ONNX models on iOS/Android, dispatching to Core ML, NNAPI, or GPU execution providers for acceleration. Export from PyTorch via torch.onnx, optimize (quantize, fuse), and ship one model file across platforms. It is the cross-platform answer when you cannot commit to a single vendor stack.", "iOS/Android (cross-platform)", ".onnx", "Modern phones for transformer models", "torch.onnx.export + ORT quantize", "python", "Export PyTorch to ONNX", "import torch\nmodel = torch.nn.Sequential(torch.nn.Linear(10, 2)).eval()\ntorch.onnx.export(model, torch.randn(1, 10), \"/tmp/m.onnx\",\n                  input_names=[\"x\"], output_names=[\"y\"],\n                  dynamo=False)\nprint(\"exported /tmp/m.onnx\")"],
 ["runtime", "llama.cpp", "Run LLMs on anything: CPU-first inference with GGUF quantization, from servers to phones.", "llama.cpp is a C/C++ inference engine running quantized LLMs on CPUs, GPUs (CUDA/Metal/Vulkan), and mobile chips with no heavy dependencies. GGUF quants (Q4_K_M etc.) shrink 70B models to ~40GB; Metal and CUDA backends offload layers to GPU. It powers Ollama, LM Studio, and countless local-AI apps — the engine behind the local LLM revolution.", "CPU/GPU/mobile (cross-platform)", "GGUF", "8GB RAM for 7B Q4; 48GB+ for 70B Q4", "llama-quantize from fp16 GGUF", "shell", "Run a model with llama.cpp", "llama-cli -m model-q4k.gguf -p \"Explain gravity simply.\" -n 128\n# server mode: llama-server -m model-q4k.gguf --port 8080"],
 ["framework", "MLC LLM", "Compile LLMs to native code for phones, browsers, and GPUs via Apache TVM.", "MLC LLM (Machine Learning Compilation) uses Apache TVM to compile models into optimized native libraries for iOS, Android, WebGPU, CUDA, and more — with 4-bit quantization built in. The same model compiles to a phone app, a browser demo, or a GPU server. It is the 'write once, run anywhere fast' path for local LLMs.", "iOS/Android/Web/GPU", "MLC-compiled libs + tokenizer", "Phone with 6GB+ RAM for 7B-class", "mlc_llm gen_config + compile", "shell", "Compile a model with MLC LLM", "mlc_llm gen_config --model Llama-3-8B --quantization q4f16_1 \\\n  --conv-template llama-3 -o dist/\n# then build the lib for your target (iphone/android/webgpu)"],
 ["runtime", "ExecuTorch", "Meta's on-device runtime for PyTorch models: from research model to phone app.", "ExecuTorch (Meta/PyTorch) takes PyTorch models (via Export) and runs them on mobile and embedded devices with delegate backends (Core ML, NPU, DSP). It unifies the path from training in PyTorch to deployment on device — no framework rewrite. Powers Meta's on-device AI features and is fully open-source.", "iOS/Android/embedded", ".pte", "Varies by model size", "torch.export + executorch export", "python", "Export for ExecuTorch", "import torch\nfrom executorch import exir\nmodel = torch.nn.Sequential(torch.nn.Linear(10, 2)).eval()\nprog = exir.to_edge(exir.capture(model, (torch.randn(1, 10),)))\nprint(\"edge program dialects:\", list(prog.exported_program().dialects))"],
 ["quantization", "INT8 Quantization", "Shrink models 4x with 8-bit weights/activations — the workhorse of mobile deployment.", "INT8 post-training quantization converts weights (and optionally activations) to 8-bit integers with per-channel scales, cutting model size 4x and speeding mobile CPUs/DSPs that have INT8 units. Calibration on representative data preserves accuracy; quantization-aware training recovers the last points. Nearly every shipped mobile model uses it.", "All mobile", "INT8 variants per framework", "INT8-capable CPU/DSP/NPU", "PTQ with calibration data", "python", "INT8 scale math", "import torch\nw = torch.randn(1000)\nscale = w.abs().max() / 127\nq = torch.round(w / scale).clamp(-128, 127)\nprint(\"max abs error:\", float((w - q*scale).abs().max()))"],
 ["quantization", "INT4 / GGUF Quantization", "4-bit weights for LLMs on phones: 7B models in ~4GB of RAM.", "INT4 quantization (GPTQ/AWQ-style, GGUF K-quants) compresses LLM weights to 4 bits with grouped scales, fitting 7-8B models in ~4-5GB — phone territory. Quality loss is small at 7B+ scales. Combined with llama.cpp or MLC, it is what makes capable chatbots run fully offline on flagship phones.", "Phones/laptops", "GGUF Q4_K_M etc.", "4-6GB free RAM for 7B Q4", "llama-quantize / GPTQ / AWQ", "shell", "Check GGUF size", "ls -lh *Q4_K_M.gguf\n# 7B Q4_K_M ~= 4.1GB; 70B Q4_K_M ~= 39GB"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,title:b[1],t:b[1],g:cat,c:1,summary:b[2],details:b[3]};
  for(var i=0;i<FIELDS.length;i++){rec[FIELDS[i]]=b[4+i];}
  var di=4+FIELDS.length;
  rec.ladder_rank=1+(seed%3);
  rec.demo={language:b[di],title:b[di+1],program:b[di+2]};
  rec.provenance="JAH Databases generator (archive-style records)";
  rec.last_verified='2026-10-20';
  rec.src="public-harvest";
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.summary!=='string'||!r.summary.length)e.push('summary');
  if(typeof r.details!=='string'||!r.details.length)e.push('details');
  if(CATS.indexOf(r.g)<0)e.push('g');
  for(var i=0;i<FIELDS.length;i++){
    var v=r[FIELDS[i]];
    if(v===undefined||v===null||(typeof v==='string'&&!v.length))e.push('field:'+FIELDS[i]);
  }
  if(!(r.ladder_rank===1||r.ladder_rank===2||r.ladder_rank===3))e.push('ladder_rank');
  var d=r.demo;
  if(!d||typeof d.language!=='string'||!d.language.length||typeof d.title!=='string'||!d.title.length||typeof d.program!=='string'||!d.program.length)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-20')e.push('last_verified');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-on-device-ai-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('on-device-ai',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
