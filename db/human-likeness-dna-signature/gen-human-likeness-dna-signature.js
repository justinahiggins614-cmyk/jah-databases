(function(){'use strict';
/* JAH The Human Likeness DNA Signature Database generator — jahdb-human-likeness-dna-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HLDNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What the Human Likeness Method Is (Signature Edition) - Foundations",
  "The Deterministic Pipeline: Sequence to Representation (Signature Edition) - Foundations",
  "DNA Sequence Basics for This Database (Signature Edition) - Foundations",
  "Seeded Randomness: Same Input, Same Output (Signature Edition) - Foundations",
  "Reading a Synthetic Sequence (Signature Edition) - Foundations",
  "The Trait-Parameter Vector (Signature Edition) - Foundations",
  "The Abstract Visualization Spec (Signature Edition) - Foundations",
  "What This Method Cannot Do: The Limits Record (Signature Edition) - Foundations",
  "Sequence Hygiene and Validation (Signature Edition) - Foundations",
  "The Determinism Verification Procedure (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Deriving the Height Band from a Sequence (Signature Edition) - Compounded",
  "Deriving the Build Band from a Sequence (Signature Edition) - Compounded",
  "Deriving the Skin-Tone Band from a Sequence (Signature Edition) - Compounded",
  "Deriving Hair Texture from a Sequence (Signature Edition) - Compounded",
  "Deriving Hair Shade from a Sequence (Signature Edition) - Compounded",
  "Deriving Eye Color from a Sequence (Signature Edition) - Compounded",
  "Deriving the Face Width Ratio from a Sequence (Signature Edition) - Compounded",
  "Deriving the Jaw Angle from a Sequence (Signature Edition) - Compounded",
  "Deriving Nose Bridge Geometry from a Sequence (Signature Edition) - Compounded",
  "Deriving Brow Density from a Sequence (Signature Edition) - Compounded",
  "Deriving Lip Fullness from a Sequence (Signature Edition) - Compounded",
  "Deriving Freckle Density from a Sequence (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Combining All Traits into One Representation (Signature Edition) - Advanced",
  "Full Likeness Derivation A: Sequence HLX-0001 (Signature Edition) - Advanced",
  "Full Likeness Derivation B: Sequence HLX-0002 (Signature Edition) - Advanced",
  "Full Likeness Derivation C: Sequence HLX-0003 (Signature Edition) - Advanced",
  "Full Likeness Derivation D: Sequence HLX-0004 (Signature Edition) - Advanced",
  "Full Likeness Derivation E: Sequence HLX-0005 (Signature Edition) - Advanced",
  "Full Likeness Derivation F: Sequence HLX-0006 (Signature Edition) - Advanced",
  "Full Likeness Derivation G: Sequence HLX-0007 (Signature Edition) - Advanced",
  "Full Likeness Derivation H: Sequence HLX-0008 (Signature Edition) - Advanced",
  "The Determinism Proof: Same Sequence, Byte-Identical Representation (Signature Edition) - Advanced",
  "The Sensitivity Check: One Base Changed, a Different Representation (Signature Edition) - Advanced",
  "The Generator Record: The Working Pipeline (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Human Likeness Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — human likeness record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A human likeness record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"human-likeness-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-human-likeness-dna-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('human-likeness-dna-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();

/* HLX-1 deterministic pipeline - JavaScript mirror of the frozen Python
   implementation. Input: one DNA sequence string (ACGT, 16-4096 bases).
   Output: the deterministic representation (model label, digests, trait
   vector JSON, abstract glyph SVG). Byte-identical with the Python demos.
   Every representation is a Signature-generated deterministic model - a
   stylized parametric abstraction, never a real person's appearance. */
(function(){
'use strict';
var MASK64 = (1n << 64n) - 1n;
var FNV_OFFSET = 14695981039346656037n;
var FNV_PRIME = 1099511628211n;
var XORMULT = 2685821657736338717n;
var ZERO_SEED = 0x9E3779B97F4A7C15n;
var HEIGHT = ["compact","below-average","average","above-average","tall"];
var BUILD = ["slight","lean","sturdy","broad"];
var HAIR_TEX = ["straight","wavy","curly","coily"];
var EYE = ["brown","hazel","green","blue","gray","amber"];
var NOSE = ["low","medium","high"];
var BROW = ["light","medium","full"];
var LIP = ["thin","medium","full"];
var FRECKLE = ["none","sparse","moderate","dense"];
var EYE_HEX = {"brown":"#6B4226","hazel":"#8A6D3B","green":"#4F7942",
  "blue":"#3B6EA5","gray":"#7D7D7D","amber":"#B8860B"};
var TRAIT_ORDER = ["height_band","build","skin_band","hair_texture",
  "hair_shade","eye_color","face_width_ratio","jaw_angle",
  "nose_bridge","brow_density","lip_fullness","freckle_density"];
var MODEL_LABEL = "Signature-generated deterministic model - a stylized " +
  "parametric abstraction. Never a real person's appearance.";
function validate(seq){
  if(typeof seq !== "string" || seq.length === 0)
    throw new Error("sequence must be a non-empty string");
  if(seq.length < 16) throw new Error("sequence too short (minimum 16 bases)");
  if(seq.length > 4096) throw new Error("sequence too long (maximum 4096 bases)");
  for(var i = 0; i < seq.length; i++){
    var c = seq.charAt(i);
    if(c !== "A" && c !== "C" && c !== "G" && c !== "T")
      throw new Error("invalid base: only A, C, G, T allowed");
  }
  return seq;
}
function fnv1a64(str){
  var h = FNV_OFFSET;
  for(var i = 0; i < str.length; i++){
    h ^= BigInt(str.charCodeAt(i));
    h = (h * FNV_PRIME) & MASK64;
  }
  return h;
}
function makeRng(seed){
  var s = (seed & MASK64) || ZERO_SEED;
  return {
    next64: function(){
      var x = s;
      x ^= x >> 12n; x &= MASK64;
      x ^= (x << 25n) & MASK64;
      x ^= x >> 27n;
      s = x & MASK64;
      return (s * XORMULT) & MASK64;
    },
    int: function(n){ return this.next64() % BigInt(n); }
  };
}
function deriveTraits(seq){
  validate(seq);
  var rng = makeRng(fnv1a64(seq));
  var hi = rng.int(5), bi = rng.int(4), si = rng.int(6), ti = rng.int(4),
      sh = rng.int(6), ei = rng.int(6), fq = rng.int(21), ja = rng.int(41),
      ni = rng.int(3), br = rng.int(3), li = rng.int(3), fi = rng.int(4);
  var traits = {
    height_band: HEIGHT[Number(hi)],
    build: BUILD[Number(bi)],
    skin_band: "band-" + (Number(si) + 1),
    hair_texture: HAIR_TEX[Number(ti)],
    hair_shade: "shade-" + (Number(sh) + 1),
    eye_color: EYE[Number(ei)],
    face_width_ratio: (72 + Number(fq)) / 100,
    jaw_angle: 100 + Number(ja),
    nose_bridge: NOSE[Number(ni)],
    brow_density: BROW[Number(br)],
    lip_fullness: LIP[Number(li)],
    freckle_density: FRECKLE[Number(fi)]
  };
  var idx = {height_idx: Number(hi), skin_idx: Number(si),
    texture_idx: Number(ti), face_q: Number(fq), jaw_angle: 100 + Number(ja),
    nose_idx: Number(ni), brow_idx: Number(br), freckle_idx: Number(fi)};
  return {traits: traits, idx: idx};
}
function svgSpec(traits, idx){
  var bgHue = (idx.skin_idx * 47 + idx.height_idx * 23) % 360;
  var discR = 52 + idx.face_q;
  var discHue = (bgHue + 180) % 360;
  var jawH = 20 + (idx.jaw_angle - 100);
  var noseH = 20 + idx.nose_idx * 15;
  var browH = 20 + idx.brow_idx * 15;
  var nArcs = idx.texture_idx + 1;
  var nFreck = idx.freckle_idx * 5;
  var eyeHex = EYE_HEX[traits.eye_color];
  var L = [];
  L.push('<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">');
  L.push('<rect width="240" height="240" fill="hsl(' + bgHue + ',45%,88%)"/>');
  L.push('<circle cx="120" cy="112" r="' + discR + '" fill="hsl(' + discHue +
    ',40%,72%)" stroke="#333333" stroke-width="2"/>');
  L.push('<rect x="56" y="' + (214 - jawH) + '" width="18" height="' + jawH + '" fill="#555555"/>');
  L.push('<rect x="86" y="' + (214 - noseH) + '" width="18" height="' + noseH + '" fill="#777777"/>');
  L.push('<rect x="116" y="' + (214 - browH) + '" width="18" height="' + browH + '" fill="#999999"/>');
  var top = 112 - discR - 8, a, y, d, style = idx.texture_idx;
  for(a = 0; a < nArcs; a++){
    y = top - a * 9;
    if(style === 0) d = "M " + (120 - discR) + " " + y + " L " + (120 + discR) + " " + y;
    else if(style === 1) d = "M " + (120 - discR) + " " + y + " Q 120 " + (y - 10) + " " + (120 + discR) + " " + y;
    else if(style === 2) d = "M " + (120 - discR) + " " + y +
      " Q " + (120 - Math.floor(discR / 2)) + " " + (y - 12) + " 120 " + y +
      " Q " + (120 + Math.floor(discR / 2)) + " " + (y + 12) + " " + (120 + discR) + " " + y;
    else d = "M " + (120 - discR) + " " + y +
      " L " + (120 - Math.floor(discR / 3)) + " " + (y - 10) +
      " L " + (120 + Math.floor(discR / 3)) + " " + (y + 10) +
      " L " + (120 + discR) + " " + y;
    L.push('<path d="' + d + '" stroke="#222222" stroke-width="2" fill="none"/>');
  }
  L.push('<circle cx="104" cy="106" r="6" fill="' + eyeHex + '"/>');
  L.push('<circle cx="136" cy="106" r="6" fill="' + eyeHex + '"/>');
  var f, fx, fy;
  for(f = 0; f < nFreck; f++){
    fx = 84 + (f * 37) % 72; fy = 96 + (f * 53) % 40;
    L.push('<circle cx="' + fx + '" cy="' + fy + '" r="1.6" fill="#4a3220"/>');
  }
  L.push('<text x="120" y="232" text-anchor="middle" font-size="8" fill="#333333">' +
    'HLX-1 abstract glyph - deterministic model, not a person</text>');
  L.push('</svg>');
  return L.join("\n");
}
function hex16(h){
  var s = h.toString(16);
  while(s.length < 16) s = "0" + s;
  return s;
}
function represent(seq){
  var dt = deriveTraits(seq), traits = dt.traits, idx = dt.idx;
  var vec = {}, i;
  for(i = 0; i < TRAIT_ORDER.length; i++) vec[TRAIT_ORDER[i]] = traits[TRAIT_ORDER[i]];
  return {
    model_label: MODEL_LABEL,
    sequence_length: seq.length,
    digest_fnv1a64: hex16(fnv1a64(validate(seq))),
    trait_vector: vec,
    trait_vector_json: JSON.stringify(vec),
    svg_spec: svgSpec(traits, idx)
  };
}
var HLX1 = {version: "hlx-1", validate: validate, fnv1a64: fnv1a64,
  deriveTraits: deriveTraits, svgSpec: svgSpec, represent: represent,
  model_label: MODEL_LABEL};
if(typeof module !== "undefined" && module.exports) module.exports.HLX1 = HLX1;
if(typeof window !== "undefined") window.JAHDB_HLX1 = HLX1;
})();
