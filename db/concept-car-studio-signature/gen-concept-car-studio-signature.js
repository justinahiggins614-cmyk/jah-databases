(function(){'use strict';
/* JAH The Concept Car Studio generator — jahdb-concept-car-studio-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working concept-car studio: every call invents an original vehicle —
   model name, class lane, design language, honest specs (range, power, 0-60),
   signature features, colorway — and renders a side-profile SVG.
   Deterministic per seed: same seed, same concept. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-CNCSS-";
var FIELDS=["City Electric","Grand Tourer","Off-Road Explorer"];
var NAME_A=["Volt","Aero","Terra","Lumen","Drift","Onyx","Zephyr","Halcyon","Vector","Ember"];
var NAME_B=["One","GT","Cross","S","Tourer","X","Prime","RS","Wagon","Coupe"];
var LANG={"City Electric":"soft-tech minimalism, flush glass, hidden seams","Grand Tourer":"long-hood elegance, fastback taper, jewelry lighting","Off-Road Explorer":"armored cladding, high beltline, honest hardware"};
var SPECS={"City Electric":{range:"280 mi",power:"201 hp","zero60":"6.9 s"},"Grand Tourer":{range:"410 mi",power:"536 hp","zero60":"3.4 s"},"Off-Road Explorer":{range:"320 mi",power:"420 hp","zero60":"5.8 s"}};
var FEATS=["panoramic electrochromic roof","lidar pod in the brow line","frunk with drain plug","vegan cabin textiles","over-the-air everything","solar hood inlay"];
var COLORS=[["#2B2D42","#F7C548"],["#0B4F6C","#F4F7F5"],["#5C1A1B","#E8DCC4"],["#1F3D2B","#DAD7CD"],["#0A0A0A","#E07A3F"]];
function carSVG(cols,name){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="560" height="240" viewBox="0 0 560 240">'
  +'<rect width="560" height="240" fill="#FFFFFF"/>'
  +'<ellipse cx="280" cy="205" rx="220" ry="10" fill="#DDDDDD"/>'
  +'<path d="M60 180 Q90 120 170 110 L220 60 Q230 50 250 52 L340 58 Q360 60 375 78 L430 110 Q500 120 510 160 L515 180 Z" fill="'+cols[0]+'" stroke="#222222" stroke-width="3"/>'
  +'<path d="M235 68 L335 72 Q350 73 360 86 L395 108 L200 108 Q215 85 235 68 Z" fill="#9AD6E8" opacity="0.85"/>'
  +'<circle cx="160" cy="180" r="30" fill="#1A1A1A"/><circle cx="160" cy="180" r="12" fill="#888888"/>'
  +'<circle cx="420" cy="180" r="30" fill="#1A1A1A"/><circle cx="420" cy="180" r="12" fill="#888888"/>'
  +'<rect x="470" y="140" width="34" height="10" rx="5" fill="'+cols[1]+'"/>'
  +'<text x="280" y="30" font-family="Georgia,serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#1A1A1A">'+name+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var name=pick(NAME_A,s)+" "+pick(NAME_B,s);
  var spec=SPECS[field], feats=pickN(FEATS,s,3), cols=pick(COLORS,s);
  var svg=carSVG(cols,name);
  var title=name+" — "+field+" concept — seed "+seed;
  var desc='GENERATED CONCEPT CAR — the '+name+', a '+field.toLowerCase()+' concept. Design language: '+LANG[field]+'. Specs: '+spec.range+' range, '+spec.power+', 0-60 in '+spec.zero60+'. Signature features: '+feats.join('; ')+'.';
  var prog="# Concept car — "+name+" (seed "+seed+")\n"
    +"model = \""+name+"\"\n"+"lane = \""+field+"\"\n"+"language = \""+LANG[field]+"\"\n"
    +"specs = "+JSON.stringify(spec)+"\n"+"features = "+JSON.stringify(feats)+"\n"+"colors = "+JSON.stringify(cols)+"\n"
    +"print(\"Model:\", model, \"[\"+lane+\"]\")\n"+"print(\"Language:\", language)\n"
    +"[print(\" %s: %s\" % (k, v)) for k, v in specs.items()]\n"
    +"[print(\" Feature:\", f) for f in features]\n"+"print(\"Car SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — concept record', title:title, description:desc,
    how_it_works:'The generator names an original model from word pairs, assigns the class lane, reads the lane\u2019s design language and honest spec block, draws three signature features without replacement, picks a two-tone colorway, and renders a side-profile SVG — deterministic per seed.',
    key_points:['Model: '+name,'Class: '+field,'Language: '+LANG[field],'Range: '+spec.range+', Power: '+spec.power+', 0-60: '+spec.zero60,'Features: '+feats.join('; '),'Colors: '+cols.join(' + '),'Deterministic: seed '+seed+' always rebuilds this exact concept.'],
    requirements:['A seed number to regenerate this exact concept','An HTML file to view the side-profile SVG'],
    standards:['Model name is original','Spec block carries range, power, and 0-60','Three signature features','Side-profile SVG renders the model name'],
    citations:['Design craft references: concept language.','Spec references: honest performance blocks.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{model:name,lane:field,language:LANG[field],specs:spec,features:feats,colors:cols,svg:svg},
    svg:svg,
    demo:{kind:'car-plan',language:'python',program:prog,note:'Prints the model, design language, specs, and features.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.model||!o.language)e.push('design');
  if(!o.specs||!o.specs.range||!o.specs.power||!o.specs.zero60)e.push('specs');
  if(!o.features||o.features.length!==3)e.push('features');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate concept in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-concept-car-studio-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('concept-car-studio-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();