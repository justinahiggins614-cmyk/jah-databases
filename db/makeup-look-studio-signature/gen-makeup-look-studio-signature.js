(function(){'use strict';
/* JAH The Makeup Look Studio generator — jahdb-makeup-look-studio-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working makeup-look generator: every call composes a complete look —
   base, eyes, cheeks, lips, five ordered application steps, wear-time and
   occasion notes — and renders a face-chart SVG mapping each product zone.
   Deterministic per seed: same seed, same look. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MKLSS-";
var FIELDS=["Natural Day","Evening Glam","Bold Editorial"];
var LOOKS={
 "Natural Day":{base:"tinted moisturizer, sheer coverage",eyes:"taupe wash with brown mascara",cheeks:"peach cream blush",lips:"tinted balm, rosewood",steps:["Moisturize and apply tinted moisturizer with fingers.","Sweep taupe shadow across the lid; one coat of brown mascara.","Press cream blush into the apples of the cheeks.","Dab tinted balm on lips; blot once.","Set the T-zone lightly with translucent powder."],wear:"8-hour fresh wear"},
 "Evening Glam":{base:"full-coverage foundation, luminous finish",eyes:"smoky bronze with winged liner",cheeks:"sculpted contour and champagne highlight",lips:"classic red matte",steps:["Prime lids and face; apply full-coverage foundation.","Blend bronze tones into a smoky eye; wing the liner.","Contour hollows; highlight cheekbones and brow bone.","Line and fill lips with classic red matte.","Lock everything with setting spray."],wear:"12-hour event wear"},
 "Bold Editorial":{base:"matte full coverage, porcelain finish",eyes:"graphic cobalt liner, bare lash",cheeks:"draped blush, temple to apple",lips:"blackened plum gloss",steps:["Apply matte foundation; skip concealer for skin texture.","Draw graphic cobalt liner; keep lashes bare.","Drape blush from temple to apple in one sweep.","Press blackened plum gloss into lips.","Photograph in daylight; adjust liner symmetry."],wear:"shoot-day wear, touch up hourly"}};
var ZONEC=["#F5D5C8","#8A5A44","#D98E8E","#A83A4A"];
function faceSVG(look){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="300" viewBox="0 0 240 300">'
  +'<rect width="240" height="300" fill="#FFFFFF"/>'
  +'<ellipse cx="120" cy="150" rx="78" ry="105" fill="'+ZONEC[0]+'"/>'
  +'<ellipse cx="88" cy="120" rx="22" ry="12" fill="'+ZONEC[1]+'" opacity="0.55"/><ellipse cx="152" cy="120" rx="22" ry="12" fill="'+ZONEC[1]+'" opacity="0.55"/>'
  +'<ellipse cx="70" cy="170" rx="16" ry="10" fill="'+ZONEC[2]+'" opacity="0.7"/><ellipse cx="170" cy="170" rx="16" ry="10" fill="'+ZONEC[2]+'" opacity="0.7"/>'
  +'<ellipse cx="120" cy="225" rx="26" ry="12" fill="'+ZONEC[3]+'"/>'
  +'<text x="120" y="292" font-family="Georgia,serif" font-size="13" text-anchor="middle" fill="#333333">'+look+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var L=LOOKS[field];
  var svg=faceSVG(field);
  var title="The "+field+" Look — seed "+seed;
  var desc='GENERATED MAKEUP LOOK — '+field+'. Base: '+L.base+'. Eyes: '+L.eyes+'. Cheeks: '+L.cheeks+'. Lips: '+L.lips+'. '+L.wear+'. Five ordered steps take the look from bare skin to finished.';
  var prog="# Makeup look — "+field+" (seed "+seed+")\n"
    +"look = \""+field+"\"\n"+"base = \""+L.base+"\"\n"+"eyes = \""+L.eyes+"\"\n"
    +"cheeks = \""+L.cheeks+"\"\n"+"lips = \""+L.lips+"\"\n"
    +"steps = "+JSON.stringify(L.steps)+"\n"
    +"print(\"Look:\", look)\n"+"print(\"Base:\", base)\n"+"print(\"Eyes:\", eyes)\n"+"print(\"Cheeks:\", cheeks)\n"+"print(\"Lips:\", lips)\n"
    +"[print(\" %d. %s\" % (i+1, st)) for i, st in enumerate(steps)]\n"
    +"print(\"Face-chart SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — makeup record', title:title, description:desc,
    how_it_works:'The generator selects an occasion lane and reads its full look specification — base, eyes, cheeks, lips, five ordered application steps, and wear-time. The face-chart SVG maps each product zone on a stylized face — deterministic per seed.',
    key_points:['Look: '+field,'Base: '+L.base,'Eyes: '+L.eyes,'Cheeks: '+L.cheeks,'Lips: '+L.lips,'Wear: '+L.wear,'Deterministic: seed '+seed+' always rebuilds this exact look.'],
    requirements:['A seed number to regenerate this exact look','An HTML file to view the face-chart SVG'],
    standards:['All four zones specified: base, eyes, cheeks, lips','Exactly five ordered application steps','Face-chart SVG renders the look name'],
    citations:['Makeup craft references: look architecture.','Application references: ordered step design.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{look:field,base:L.base,eyes:L.eyes,cheeks:L.cheeks,lips:L.lips,steps:L.steps,wear:L.wear,svg:svg},
    svg:svg,
    demo:{kind:'makeup-plan',language:'python',program:prog,note:'Prints the full look with ordered application steps.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.base||!o.eyes||!o.cheeks||!o.lips)e.push('zones');
  if(!o.steps||o.steps.length!==5)e.push('steps');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate look in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-makeup-look-studio-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('makeup-look-studio-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();