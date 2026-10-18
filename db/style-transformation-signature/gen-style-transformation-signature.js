(function(){'use strict';
/* JAH The Style Transformation Database generator — jahdb-style-transformation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working style-transformation generator: every call designs a complete
   before-and-after — current style profile, target style profile, five garment
   swaps, a keep list, a focused shopping list, and a before/after panel SVG.
   Deterministic per seed: same seed, same transformation. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-STTRS-";
var FIELDS=["Wardrobe Refresh","Full Reinvention","Occasion Overhaul"];
var STYLES=["off-duty athleisure","minimalist monochrome","vintage eclectic","polished preppy","streetwear edge","soft romantic","rugged workwear","bold maximalist"];
var SWAPS=[["graphic tees","heavyweight plain tees"],["skinny jeans","straight-leg selvedge"],["fast-fashion blazer","unstructured wool blazer"],["worn sneakers","clean leather sneakers"],["logo hoodie","merino crewneck"],["baggy cargos","tapered canvas trousers"],["dated suit","modern tailored suit"],["scuffed boots","polished chelsea boots"]];
var SHOP=["the perfect white tee","dark straight jeans","a blazer that fits","versatile leather shoes","a watch with weight","quality knitwear"];
var KEEP=["the leather jacket with history","the boots already broken in","the watch from family","the denim with perfect fades"];
function panelsSVG(before,after){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="560" height="220" viewBox="0 0 560 220">'
  +'<rect width="560" height="220" fill="#FFFFFF"/>'
  +'<rect x="20" y="20" width="250" height="180" rx="10" fill="#E8E4DA"/>'
  +'<rect x="290" y="20" width="250" height="180" rx="10" fill="#2B2D42"/>'
  +'<text x="145" y="55" font-family="Georgia,serif" font-size="15" font-weight="bold" text-anchor="middle" fill="#1A1A1A">BEFORE</text>'
  +'<text x="145" y="120" font-family="Georgia,serif" font-size="13" text-anchor="middle" fill="#555555">'+before+'</text>'
  +'<text x="415" y="55" font-family="Georgia,serif" font-size="15" font-weight="bold" text-anchor="middle" fill="#F5F0E1">AFTER</text>'
  +'<text x="415" y="120" font-family="Georgia,serif" font-size="13" text-anchor="middle" fill="#F5F0E1">'+after+'</text>'
  +'<text x="280" y="115" font-family="Georgia,serif" font-size="26" text-anchor="middle" fill="#C8102E">\u2192</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var before=pick(STYLES,s), after=pick(STYLES.filter(function(x){return x!==before;}),s);
  var swaps=pickN(SWAPS,s,5), shop=pickN(SHOP,s,4), keep=pickN(KEEP,s,2);
  var svg=panelsSVG(before,after);
  var title="From "+before+" to "+after+" — seed "+seed;
  var desc='GENERATED TRANSFORMATION — a '+field.toLowerCase()+': from '+before+' to '+after+'. Five swaps: '+swaps.map(function(w){return w[0]+" \u2192 "+w[1];}).join('; ')+'. Keep: '+keep.join(', ')+'. Shop: '+shop.join(', ')+'.';
  var prog="# Style transformation — "+field+" (seed "+seed+")\n"
    +"before = \""+before+"\"\n"+"after = \""+after+"\"\n"
    +"swaps = "+JSON.stringify(swaps)+"\n"+"keep = "+JSON.stringify(keep)+"\n"+"shop = "+JSON.stringify(shop)+"\n"
    +"print(\"Before:\", before, \"-> After:\", after)\n"
    +"[print(\" Swap: %s -> %s\" % (a, b)) for a, b in swaps]\n"
    +"print(\"Keep:\", \", \".join(keep))\n"+"print(\"Shop:\", \", \".join(shop))\n"
    +"print(\"Panel SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — transformation record', title:title, description:desc,
    how_it_works:'The generator profiles a before style and a different after style, draws five garment swaps without replacement, plus a keep list and a focused shopping list, and renders a before/after panel SVG — deterministic per seed.',
    key_points:['Before: '+before,'After: '+after,'Lane: '+field,'Swaps: '+swaps.map(function(w){return w[0]+" → "+w[1];}).join('; '),'Keep: '+keep.join(', '),'Shop: '+shop.join(', '),'Deterministic: seed '+seed+' always rebuilds this exact transformation.'],
    requirements:['A seed number to regenerate this exact transformation','An HTML file to view the before/after SVG'],
    standards:['Before and after styles differ','Five distinct garment swaps','Keep list and shopping list included'],
    citations:['Style craft references: transformation design.','Wardrobe references: swap methodology.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{before:before,after:after,lane:field,swaps:swaps,keep:keep,shop:shop,svg:svg},
    svg:svg,
    demo:{kind:'transformation-plan',language:'python',program:prog,note:'Prints the before/after profiles with swaps and lists.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.before||!o.after||o.before===o.after)e.push('profiles');
  if(!o.swaps||o.swaps.length!==5)e.push('swaps');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate transformation in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-style-transformation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('style-transformation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();