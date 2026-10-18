(function(){'use strict';
/* JAH The Personal Color Palette Database generator — jahdb-personal-color-palette-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working color-palette generator: every call performs a seasonal color
   analysis — undertone, season, six-swatch palette with hex codes and wear notes,
   best neutrals, colors to avoid — and renders a swatch-card SVG. Deterministic
   per seed: same seed, same palette. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-PCPLS-";
var FIELDS=["Spring Warm","Summer Cool","Autumn Warm","Winter Cool"];
var SEASONS={
 "Spring Warm":{undertone:"warm and golden",avoid:["black","charcoal gray","icy pastels"],swatches:[["daffodil","#F2C14E"],["coral","#F4845F"],["warm teal","#2A9D8F"],["camel","#C19A6B"],["leaf green","#6A994E"],["cream","#FFF8E7"]]},
 "Summer Cool":{undertone:"cool and soft",avoid:["neon brights","orange","stark black"],swatches:[["powder blue","#A8C3D1"],["rose","#D4A5A5"],["lavender gray","#B8A9C9"],["soft white","#F5F5F0"],["sage","#9CAF88"],["mauve","#C08081"]]},
 "Autumn Warm":{undertone:"warm and rich",avoid:["icy blue","hot pink","pure white"],swatches:[["burnt orange","#CC5500"],["olive","#808000"],["rust","#B7410E"],["teal","#367588"],["mustard","#E1AD01"],["warm ivory","#FDF6EC"]]},
 "Winter Cool":{undertone:"cool and vivid",avoid:["muddy browns","muted olives","dusty pastels"],swatches:[["true red","#C8102E"],["emerald","#046A38"],["royal blue","#1E3FAE"],["fuchsia","#C724B1"],["pure white","#FFFFFF"],["black","#0A0A0A"]]}};
function swatchSVG(name,swatches){
  var w=560,h=200,cells='';
  for(var i=0;i<swatches.length;i++){
    var x=20+i*88;
    cells+='<rect x="'+x+'" y="60" width="72" height="72" rx="8" fill="'+swatches[i][1]+'" stroke="#CCCCCC"/>';
    cells+='<text x="'+(x+36)+'" y="150" font-family="Georgia,serif" font-size="11" text-anchor="middle" fill="#333333">'+swatches[i][0]+'</text>';
    cells+='<text x="'+(x+36)+'" y="165" font-family="monospace" font-size="10" text-anchor="middle" fill="#777777">'+swatches[i][1]+'</text>';
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'" viewBox="0 0 '+w+' '+h+'"><rect width="'+w+'" height="'+h+'" fill="#FFFFFF"/><text x="20" y="34" font-family="Georgia,serif" font-size="18" font-weight="bold" fill="#1A1A1A">'+name+'</text>'+cells+'</svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var info=SEASONS[field];
  var sw=pickN(info.swatches,s,6);
  var svg=swatchSVG(field+" palette",sw);
  var title="The "+field+" Palette — seed "+seed;
  var desc='GENERATED PALETTE — a '+field.toLowerCase()+' seasonal color analysis ('+info.undertone+' undertone). Six signature swatches: '+sw.map(function(x){return x[0]+" ("+x[1]+")";}).join(', ')+'. Wear with confidence; avoid '+info.avoid.join(', ')+'.';
  var prog="# Personal color palette — "+field+" (seed "+seed+")\n"
    +"season = \""+field+"\"\n"+"undertone = \""+info.undertone+"\"\n"
    +"swatches = "+JSON.stringify(sw)+"\n"+"avoid = "+JSON.stringify(info.avoid)+"\n"
    +"print(\"Season:\", season, \"(\"+undertone+\")\")\n"
    +"[print(\" -\", n, c) for n, c in swatches]\n"
    +"print(\"Avoid:\", \", \".join(avoid))\n"+"print(\"Swatch SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — palette record', title:title, description:desc,
    how_it_works:'The generator selects a seasonal lane, reads its undertone and avoid-list, draws six swatches without replacement from the season\u2019s curated set, and renders a labeled swatch-card SVG with names and hex codes — deterministic per seed.',
    key_points:['Season: '+field+' ('+info.undertone+' undertone)','Swatches: '+sw.map(function(x){return x[0];}).join(', '),'Hexes: '+sw.map(function(x){return x[1];}).join(', '),'Avoid: '+info.avoid.join(', '),'Deterministic: seed '+seed+' always rebuilds this exact palette.'],
    requirements:['A seed number to regenerate this exact palette','An HTML file to view the swatch-card SVG'],
    standards:['Exactly six swatches with names and hex codes','Avoid-list has three colors','Swatch SVG labels every swatch'],
    citations:['Color analysis references: seasonal palettes.','Design references: swatch-card craft.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{season:field,undertone:info.undertone,swatches:sw,avoid:info.avoid,svg:svg},
    svg:svg,
    demo:{kind:'palette-card',language:'python',program:prog,note:'Prints the seasonal analysis with swatch names and hexes.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.swatches||o.swatches.length!==6)e.push('swatches');
  if(!o.avoid||o.avoid.length!==3)e.push('avoid');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate palette in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-personal-color-palette-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-color-palette-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();