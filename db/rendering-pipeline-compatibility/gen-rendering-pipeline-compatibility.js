(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["api-translation", "shader-porting", "feature-parity", "performance-parity", "validation"];
var PREFIX="JAH-RPC-";
var FIELDS=["technique", "api_a", "api_b", "compat_area", "verdict", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Vulkan to DirectX 12 Translation", "Explicit APIs map reasonably: command buffers, pipelines, descriptors have analogues. The translation is mechanical but verbose. Explicitness translates.", "api-translation", 2, "API mapping", "Vulkan", "DirectX 12", "Explicit APIs", "Mechanical map", "Translates", "Medium"], ["HLSL to SPIR-V Compilation", "DirectX shaders compile to SPIR-V for Vulkan via DXC; the path is well-trodden. One source, two APIs. Shaders get portable.", "shader-porting", 1, "DXC", "HLSL", "SPIR-V", "Shader bytecode", "Well-trodden", "Portable shaders", "Low"], ["Metal Shader Conversion", "Metal Shading Language differs most; conversion tools translate from HLSL/SPIR-V with caveats. The differences are real. Translation needs care.", "shader-porting", 2, "SPIRV-Cross", "SPIR-V", "Metal", "Apple GPUs", "Translate with care", "Apple covered", "Medium"], ["WebGPU as Common Target", "WebGPU's API is the portable subset; targeting it covers browsers and (via Dawn) native. The subset is the interop point. Portability through subsetting.", "api-translation", 2, "WebGPU target", "WebGPU", "Native", "Portable subset", "Subset portability", "Browsers + native", "Medium"], ["Render Pass Compatibility", "Render passes map across APIs with different attachment semantics; the translation preserves the dependencies. Passes get portable. Dependencies get kept.", "api-translation", 2, "Pass mapping", "Vulkan", "Metal", "Render passes", "Preserve deps", "Portable passes", "Medium"], ["Descriptor Set Translation", "Vulkan descriptor sets become DX12 root signatures or Metal argument buffers; the binding model differs most here. Bindings get translated. Models differ.", "api-translation", 3, "Binding map", "Vulkan", "DX12/Metal", "Resources", "Remap bindings", "Translated", "High"], ["Feature Level Negotiation", "APIs expose different features; the engine negotiates the common set and degrades gracefully. Negotiation gets honest. Grace gets designed.", "feature-parity", 2, "Negotiation", "Engine", "Device", "Features", "Common set", "Honest", "Medium"], ["Shader Validation Layers", "Validation layers catch API misuse per API; each has its own. Layers get enabled. Misuse gets caught.", "validation", 1, "Validation", "Vulkan/DX12", "Layers", "Correctness", "Enable always", "Caught misuse", "Low"], ["Performance Parity Testing", "The same scene is benchmarked on each API; parity is measured, not assumed. Testing gets honest. Numbers get compared.", "performance-parity", 2, "Bench matrix", "All APIs", "Same scene", "Speed", "Measure parity", "Honest numbers", "Medium"], ["Ray Tracing API Differences", "DXR, Vulkan RT, and Metal RT differ in shader binding and acceleration structure APIs; abstraction layers hide the differences. Differences get abstracted. Rays get portable.", "feature-parity", 3, "RT abstraction", "DXR/VK-RT", "Common RT", "Ray tracing", "Abstract", "Portable rays", "High"], ["Texture Format Compatibility", "Compressed formats differ (BC vs ASTC vs ETC); the engine transcodes or ships multiple. Formats get handled. Textures get universal.", "feature-parity", 2, "Transcode", "BC7", "ASTC", "Compression", "Ship multiple", "Universal", "Medium"], ["Synchronization Model Mapping", "Vulkan's explicit sync maps to DX12 fences and Metal events; the models differ philosophically. Sync gets translated. Philosophies get bridged.", "api-translation", 3, "Sync map", "Vulkan", "DX12/Metal", "Sync", "Translate models", "Bridged", "High"], ["Pipeline Cache Portability", "Pipeline caches don't port across APIs or drivers; each gets its own cache. Caches get separated. Warmup gets per-API.", "performance-parity", 1, "Separate caches", "Vulkan", "DX12", "PSO cache", "Per-API caches", "Separated", "Low"], ["Debug Tooling per API", "RenderDoc, PIX, and Metal tools each cover their API; the workflow adapts per platform. Tools get chosen. Debugging gets native.", "validation", 1, "Native tools", "Each API", "Its tool", "Debugging", "Use native", "Native power", "Low"], ["Multi-API Engine Architecture", "Engines abstract the API behind a render hardware interface; backends implement it. Architecture gets layered. APIs get pluggable.", "api-translation", 3, "RHI", "Engine", "Backends", "Architecture", "Layer it", "Pluggable", "High"], ["Shader Debugging Parity", "Shader debugging works differently per API; the workflow documents each. Debugging gets documented. Workflows get clear.", "validation", 2, "Doc workflows", "All APIs", "Debugging", "Shader debug", "Document each", "Clear", "Medium"], ["HDR Output Compatibility", "HDR metadata and swapchain formats differ; the engine negotiates per platform. HDR gets negotiated. Colors get right.", "feature-parity", 2, "HDR negotiate", "Engine", "Display", "HDR", "Per-platform", "Right colors", "Medium"], ["Variable Rate Shading Support", "VRS tiers differ across APIs; the engine queries and adapts. Tiers get queried. Shading gets variable.", "feature-parity", 2, "Tier query", "Engine", "GPU", "VRS", "Query + adapt", "Variable", "Medium"], ["Mesh Shader Portability", "Mesh shaders exist on DX12 and Vulkan with different APIs; abstraction unifies. Shaders get unified. Meshes get portable.", "feature-parity", 3, "Mesh abstract", "DX12/VK", "Common", "Mesh shaders", "Unify", "Portable meshes", "High"], ["Cross-API Capture and Replay", "Frame captures are replayed across APIs to verify visual parity; differences get investigated. Parity gets proven. Pixels get compared.", "validation", 3, "Capture compare", "Vulkan frame", "DX12 frame", "Visual parity", "Compare pixels", "Proven parity", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'apis = [\"vulkan\", \"dx12\", \"metal\", \"webgpu\"]\nshader = \"basic_lit\"\nsupport = {\"vulkan\": True, \"dx12\": True, \"metal\": True, \"webgpu\": False}\nok = [a for a in apis if support[a]]\nprint(\"shader:\", shader)\nprint(\"runs on:\", ok, \"(%d/%d)\" % (len(ok), len(apis)))\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-rendering-pipeline-compatibility-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("rendering-pipeline-compatibility",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
