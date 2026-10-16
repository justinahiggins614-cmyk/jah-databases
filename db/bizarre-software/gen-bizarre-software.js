(function(){'use strict';
/* JAH The Bizarre Software Database generator — "jahdb-bizarre-software-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. generateChecked: every generated
   record passes validate() and driftCheck() before it may be filed. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function escQ(s){return String(s).split("\\").join("\\\\").split("'").join("\\'");}
var PREFIX="JAH-BIZ-";
var FIELDS=["Bizarre Software", "Computational Models, Math & Theoretical", "Hardware, Fabrication & Manufacturing La", "Local Ai, Quantization & Edge Inference ", "Low-Level Systems, Firmware & Bare-Metal", "Media, Synthesis & Graphics Processing /", "Network Architecture, Protocols & Data P", "Tool Matrix", "Toolset"];
var TOPICS={"Toolset": ["Wi-Fi Antenna Coil Pulse Driver", "Wi-Fi Client Isolation Bypass", "Wi-Fi Beacon Interval Stretcher", "Wi-Fi Vendor OUI Identifier", "Wi-Fi Packet Payload Injector", "Wi-Fi TCP Session Hijacker", "Wi-Fi DNS Spoofing Daemon", "Wi-Fi Channel Width Saturator", "Wi-Fi Preamble Injection Tool", "Wi-Fi Beacon Frame Customizer", "Wi-Fi EAPOL Logoff Injector", "Wi-Fi Shared Key Authentication Breaker"], "Tool Matrix": ["Environmental Gas & Particle Sniffers"], "Computational Models, Math & Theoretical": ["Deterministic Finite Automata (DFA)", "Nondeterministic Finite Automata (NFA)", "Pushdown Automata (PDA)", "Linear Bounded Automata (LBA)", "Register Machines", "Counter Machines", "Random-Access Machines (RAM Model)", "Combinator Evaluators", "Graph Reduction Machines", "Statecharts", "Abstract State Machines (ASM)", "Process Calculi"], "Low-Level Systems, Firmware & Bare-Metal": ["Multiboot Core Images", "Boot Strapping Binaries", "Initrd / Initramfs Images", "Linker Scripts (.ld / .lds)", "Interrupt Vector Tables (IVT)", "Interrupt Descriptor Tables (IDT)", "Global Descriptor Tables (GDT)", "Page Table Generators", "GOP (Graphics Output Protocol) Drivers", "VBE (VESA BIOS Extensions) Handlers", "Device Tree Blobs (DTB / DTS)", "Binary Patchers"], "Local Ai, Quantization & Edge Inference ": ["SafeTensors Archives", "FP8 / FP16 / INT8 / INT4 Quantized Weights", "K-Quants (Q4_K_M, Q5_K_S, etc.)", "Model Shards", "Local Inference Runners", "Vector Embedders", "Local Vector Indexers", "Prompt Template Parsers", "Function Calling Parsers", "Local Tool-Routing Layers", "Document Chunkers", "Text Splitters"], "Hardware, Fabrication & Manufacturing La": ["Design Rule Checkers (DRC)", "Electrical Rule Checkers (ERC)", "NC Drill File Generators", "Footprint Libraries", "Component 3D Step Model Managers", "Parametric CAD Engines", "Direct Modeling Engines", "Mesh Editors", "Toolpath Generators", "Chemical Etching Tanks", "CMM (Coordinate Measuring Machines)", "Surface Roughness Testers"], "Network Architecture, Protocols & Data P": ["Packet Crafters", "Traffic Shapers", "Network Taps", "Socket Listeners", "TUN/TAP Virtual Interfaces", "DNS Sinkholes", "Reverse Tunnels", "Serializers / Deserializers (BSON, CBOR, MessagePack, Protobuf, FlatBuffers, Cap'n Proto)", "Schema Validators (JSON Schema, XML XSD)", "Lexicographical Dictionaries", "B-Trees / B+ Trees", "Log-Structured Merge-Trees (LSM Trees)"], "Media, Synthesis & Graphics Processing /": ["Render Targets", "VST / AU / CLAP Audio Plugins", "Oscillators", "Low-Frequency Oscillators (LFOs)", "Envelopes (ADSR Generators)", "Digital Filters (Low-pass, High-pass, Band-pass, Notch)", "Pitch Detection Engines", "Audio Resamplers", "Bitcrushers / Waveshapers"], "Bizarre Software": ["Low Battery Lock-In", "Send Me To Heaven (S.M.T.H.)", "Weird Type", "ChatterBaby", "Nothing App", "Panda Video Compress", "Onion Share", "Gesture Suite", "Friendly Social Browser", "Feedbro", "TaskbarX", "F.lux"]};
function demoProgram(topic,field){
  return '# software record study demo\n'
   + "print('Study: ' + '" + escQ(topic) + "')\n"
   + "print('Field: ' + '" + escQ(field) + "')\n"
   + "print('Full entries: description, how it works, key points, requirements, citations, demo.')\n"
   + "print('Sample record - structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' - software record study',
    title:topic,
    description:'SAMPLE RECORD (generated - structural sample). A software record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'study-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
function generateChecked(seed,opts,sample){
  var r=generate(seed,opts||{});
  var v=validate(r);
  if(!v.ok)return {ok:false,errors:v.errors};
  var d=driftCheck(r,sample||[]);
  if(!d.ok)return {ok:false,errors:d.errors};
  return {ok:true,record:r};
}
var gen={version:"jahdb-bizarre-software-1.0",generate:generate,validate:validate,driftCheck:driftCheck,generateChecked:generateChecked,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("bizarre-software",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
