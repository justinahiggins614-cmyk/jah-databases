"""Fashion-style GENERATOR items (9) — bespoke working client-side generators.
outfit-generator is the first_release_pick: built to highest polish.
Property of Justin Addam Higgins (JAH)."""

OUTFIT_GENJS = r"""(function(){'use strict';
/* JAH The Outfit Generator Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working outfit generator: every call assembles a complete head-to-toe
   outfit — top, bottom, shoes, outerwear, two accessories, a coordinated color
   palette with hex codes, occasion and weather notes, and a flat-lay SVG that
   renders each garment as a labeled swatch card. Deterministic per seed:
   same seed, same outfit, ready to wear. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
var FIELDS=["Casual Day","Work & Professional","Evening & Events"];
var TOPS={"Casual Day":["white heavyweight tee","striped breton top","sage henley","chambray button-down","oatmeal crewneck sweater"],"Work & Professional":["light-blue oxford shirt","white pinpoint dress shirt","navy knit polo","ivory silk blouse","charcoal merino crewneck"],"Evening & Events":["black silk camisole","ivory satin blouse","emerald velvet top","midnight wrap top","champagne sequin shell"]};
var BOTTOMS={"Casual Day":["medium-wash straight jeans","olive chinos","ecru wide-leg trousers","dark selvedge jeans"],"Work & Professional":["charcoal flat-front trousers","navy dress trousers","khaki tailored chinos","black cigarette pants"],"Evening & Events":["black tailored trousers","midnight pleated midi skirt","ivory wide-leg trousers","emerald satin slip skirt"]};
var SHOES={"Casual Day":["white leather sneakers","tan suede loafers","canvas low-tops","brown leather boots"],"Work & Professional":["black cap-toe oxfords","cognac leather loafers","nude pointed flats","dark-brown brogues"],"Evening & Events":["black strappy heels","nude stilettos","velvet loafers","metallic block heels"]};
var OUTER={"Casual Day":["indigo denim jacket","camel chore coat","forest quilted vest","stone field jacket"],"Work & Professional":["camel wool overcoat","navy blazer","charcoal topcoat","stone trench coat"],"Evening & Events":["black faux-fur stole","ivory wool wrap coat","midnight velvet blazer","champagne duster"]};
var ACC={"Casual Day":["canvas tote","leather belt","woven bracelet","silk scarf"],"Work & Professional":["structured leather tote","silver watch","silk pocket square","leather briefcase"],"Evening & Events":["gold clutch","pearl earrings","silk scarf","cuff bracelet"]};
var PALETTES=[["#F5F0E1","#2B2D42","#C8102E"],["#EAF2F8","#1A3C5E","#C9A227"],["#1A1A1A","#F5F0E1","#8A1C7C"],["#EFE9DC","#5C6650","#B4552D"],["#0B4F6C","#F4F7F5","#E07A3F"],["#2D2A32","#DAD7CD","#A3B18A"]];
var NOTES={"Casual Day":"Weekend-ready ease: comfortable layers, honest fabrics, and one polished detail so the outfit reads intentional, not accidental.","Work & Professional":"Boardroom-to-dinner polish: tailored lines, a restrained palette, and shoes that mean business — the uniform of quiet competence.","Evening & Events":"After-dark drama: rich textures, a focal shine, and accessories that catch the light — dressed for the moment, remembered after it."};
function esc(t){return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function flatlaySVG(items,pal){
  var w=460,h=120+items.length*64,rows='';
  for(var i=0;i<items.length;i++){
    var y=20+i*64, c=pal[i%pal.length];
    rows+='<rect x="20" y="'+y+'" width="420" height="54" rx="10" fill="'+c+'" opacity="0.22"/>';
    rows+='<rect x="20" y="'+y+'" width="54" height="54" rx="10" fill="'+c+'"/>';
    rows+='<text x="88" y="'+(y+22)+'" font-family="Georgia,serif" font-size="14" font-weight="bold" fill="#1A1A1A">'+esc(items[i][0])+'</text>';
    rows+='<text x="88" y="'+(y+42)+'" font-family="Georgia,serif" font-size="12" fill="#555555">'+esc(items[i][1])+'</text>';
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'" viewBox="0 0 '+w+' '+h+'"><rect width="'+w+'" height="'+h+'" fill="#FFFFFF"/>'+rows+'</svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var top=pick(TOPS[field],s), bottom=pick(BOTTOMS[field],s), shoes=pick(SHOES[field],s), outer=pick(OUTER[field],s);
  var acc=pickN(ACC[field],s,2), pal=pick(PALETTES,s);
  var items=[["TOP",top],["BOTTOM",bottom],["SHOES",shoes],["OUTERWEAR",outer],["ACCESSORY",acc[0]],["ACCESSORY",acc[1]]];
  var svg=flatlaySVG(items,pal);
  var title="The "+field+" Outfit — seed "+seed;
  var desc='GENERATED OUTFIT — a complete '+field.toLowerCase()+' look. Top: '+top+'. Bottom: '+bottom+'. Shoes: '+shoes+'. Outerwear: '+outer+'. Accessories: '+acc.join(' + ')+'. Palette: '+pal.join(', ')+'. '+NOTES[field];
  var prog="# Outfit plan — "+field+" (seed "+seed+")\n"
    +"occasion = \""+field+"\"\n"+"top = \""+top+"\"\n"+"bottom = \""+bottom+"\"\n"+"shoes = \""+shoes+"\"\n"+"outerwear = \""+outer+"\"\n"+"accessories = "+JSON.stringify(acc)+"\n"+"palette = "+JSON.stringify(pal)+"\n"
    +"print(\"Occasion:\", occasion)\n"+"print(\"Top:\", top)\n"+"print(\"Bottom:\", bottom)\n"+"print(\"Shoes:\", shoes)\n"+"print(\"Outerwear:\", outerwear)\n"
    +"print(\"Accessories:\", \", \".join(accessories))\n"+"print(\"Palette:\", \", \".join(palette))\n"+"print(\"Flat-lay SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — outfit record', title:title, description:desc,
    how_it_works:'The generator picks an occasion lane, then rolls one top, one bottom, one pair of shoes, and one outerwear piece from that lane\u2019s wardrobe pool, adds two accessories drawn without replacement, and assigns a three-color palette with hex codes. The flat-lay SVG renders every piece as a labeled swatch card — deterministic per seed, wearable as styled.',
    key_points:['Occasion: '+field,'Top: '+top,'Bottom: '+bottom,'Shoes: '+shoes,'Outerwear: '+outer,'Accessories: '+acc.join(' + '),'Palette: '+pal.join(', '),'Deterministic: seed '+seed+' always rebuilds this exact outfit.'],
    requirements:['A seed number to regenerate this exact outfit','An HTML file to view the flat-lay SVG'],
    standards:['One piece per slot: top, bottom, shoes, outerwear','Two distinct accessories, never repeated','Palette carries three hex codes','Flat-lay SVG labels every garment'],
    citations:['Outfit craft references: head-to-toe coordination.','Color references: three-color palette harmony.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{occasion:field,top:top,bottom:bottom,shoes:shoes,outerwear:outer,accessories:acc,palette:pal,svg:svg},
    svg:svg,
    demo:{kind:'outfit-plan',language:'python',program:prog,note:'Prints the full head-to-toe outfit plan with palette.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.top||!o.bottom||!o.shoes||!o.outerwear)e.push('garments');
  if(!o.accessories||o.accessories.length!==2||o.accessories[0]===o.accessories[1])e.push('accessories');
  if(!o.palette||o.palette.length!==3)e.push('palette');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate outfit in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

PALETTE_GENJS = r"""(function(){'use strict';
/* JAH The Personal Color Palette Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working color-palette generator: every call performs a seasonal color
   analysis — undertone, season, six-swatch palette with hex codes and wear notes,
   best neutrals, colors to avoid — and renders a swatch-card SVG. Deterministic
   per seed: same seed, same palette. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
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
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

MAKEUP_GENJS = r"""(function(){'use strict';
/* JAH The Makeup Look Studio generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working makeup-look generator: every call composes a complete look —
   base, eyes, cheeks, lips, five ordered application steps, wear-time and
   occasion notes — and renders a face-chart SVG mapping each product zone.
   Deterministic per seed: same seed, same look. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="__PREFIX__";
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
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

UNIFORM_GENJS = r"""(function(){'use strict';
/* JAH The Uniform Designer Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working uniform designer: every call creates a cohesive uniform concept —
   client organization, three role variants, two-color system with hexes, insignia
   and placement, fabric and care notes — and renders a uniform schematic SVG.
   Deterministic per seed: same seed, same uniform. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="__PREFIX__";
var FIELDS=["Service & Hospitality","Sports Teams","Corporate Crews"];
var ORGS={"Service & Hospitality":["Harborlight Hotel","Copper Kettle Caf\u00e9","Meridian Airways","The Juniper Spa"],"Sports Teams":["Riverside Runners","Harbor City FC","Northgate Nine","The Iron Antlers"],"Corporate Crews":["Parcel & Pine Couriers","Brightline Cleaners","VoltWorks Technicians","Cedar & Stone Builders"]};
var KIT={"Service & Hospitality":[["Front desk","ivory blouse, charcoal vest, name bar"],["Server","black apron over white oxford, bistro length"],["Concierge","navy blazer, gray trousers, gold pin"]],"Sports Teams":[["Home kit","primary jersey, white shorts, hooped socks"],["Away kit","reversed colors, tonal shorts"],["Training","heather tee, primary shorts, jacket"]],"Corporate Crews":[["Field crew","hi-vis vest over navy polo, canvas trousers"],["Supervisor","charcoal softshell, logo cap"],["Client-facing","white polo, navy chinos, belt"]]};
var COLORS=[["#1A3C5E","#C9A227"],["#0B4F6C","#F4F7F5"],["#5C1A1B","#E8DCC4"],["#1F3D2B","#DAD7CD"],["#2B2D42","#EF8354"],["#3E2A35","#F7C548"]];
var FABRIC={"Service & Hospitality":"cotton-poly twill, soil-release finish; machine wash warm.","Sports Teams":"moisture-wicking interlock knit; wash cold, hang dry.","Corporate Crews":"canvas duck and ripstop; reinforced knees and elbows."};
function uniformSVG(org,cols,kit){
  var rows='';
  for(var i=0;i<kit.length;i++){
    var y=70+i*56;
    rows+='<rect x="30" y="'+y+'" width="52" height="44" rx="8" fill="'+cols[i%2]+'"/>';
    rows+='<text x="100" y="'+(y+20)+'" font-family="Georgia,serif" font-size="13" font-weight="bold" fill="#1A1A1A">'+kit[i][0]+'</text>';
    rows+='<text x="100" y="'+(y+38)+'" font-family="Georgia,serif" font-size="11" fill="#555555">'+kit[i][1]+'</text>';
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="560" height="270" viewBox="0 0 560 270"><rect width="560" height="270" fill="#FFFFFF"/>'
  +'<text x="30" y="38" font-family="Georgia,serif" font-size="18" font-weight="bold" fill="#1A1A1A">'+org+'</text>'
  +'<rect x="470" y="18" width="30" height="30" fill="'+cols[0]+'"/><rect x="505" y="18" width="30" height="30" fill="'+cols[1]+'"/>'+rows+'</svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var org=pick(ORGS[field],s), kit=KIT[field], cols=pick(COLORS,s);
  var svg=uniformSVG(org,cols,kit);
  var title="Uniform Concept for "+org+" — seed "+seed;
  var desc='GENERATED UNIFORM — a cohesive '+field.toLowerCase()+' uniform concept for '+org+'. Three role variants: '+kit.map(function(k){return k[0]+" ("+k[1]+")";}).join('; ')+'. Color system: '+cols.join(' + ')+'. Fabric: '+FABRIC[field];
  var prog="# Uniform concept — "+org+" (seed "+seed+")\n"
    +"client = \""+org+"\"\n"+"lane = \""+field+"\"\n"+"colors = "+JSON.stringify(cols)+"\n"
    +"roles = "+JSON.stringify(kit.map(function(k){return k[0]+": "+k[1];}))+"\n"
    +"print(\"Client:\", client, \"[\"+lane+\"]\")\n"+"print(\"Colors:\", \", \".join(colors))\n"
    +"[print(\" -\", r) for r in roles]\n"+"print(\"Fabric:\", \""+FABRIC[field]+"\")\n"
    +"print(\"Schematic SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — uniform record', title:title, description:desc,
    how_it_works:'The generator picks a client organization from the lane, reads its three role variants, assigns a two-color system with hex codes, and renders a schematic SVG with swatches and role breakdowns — deterministic per seed.',
    key_points:['Client: '+org,'Lane: '+field,'Roles: '+kit.map(function(k){return k[0];}).join(', '),'Colors: '+cols.join(' + '),'Fabric: '+FABRIC[field],'Deterministic: seed '+seed+' always rebuilds this exact uniform.'],
    requirements:['A seed number to regenerate this exact uniform','An HTML file to view the schematic SVG'],
    standards:['Three role variants with garment specs','Two-color system with hex codes','Fabric and care notes included'],
    citations:['Uniform craft references: role-variant systems.','Color references: two-color identity systems.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{client:org,lane:field,roles:kit,colors:cols,fabric:FABRIC[field],svg:svg},
    svg:svg,
    demo:{kind:'uniform-plan',language:'python',program:prog,note:'Prints the client, roles, colors, and fabric spec.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.client||!o.roles||o.roles.length!==3)e.push('roles');
  if(!o.colors||o.colors.length!==2)e.push('colors');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate uniform in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

JERSEY_GENJS = r"""(function(){'use strict';
/* JAH The Team Jersey Studio generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working jersey studio: every call designs an original team jersey —
   fictional club name, kit lane, two-color system with hexes, chest graphic,
   number font, sleeve detail — and renders the jersey front as an SVG.
   Deterministic per seed: same seed, same jersey. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="__PREFIX__";
var FIELDS=["Home Kit","Away Kit","Special Edition"];
var CLUB_A=["Harbor","Iron","Northgate","Copper","Riverside","Juniper","Falcon","Meridian","Onyx","Lantern"];
var CLUB_B=["Wolves","Antlers","FC","Athletic","Rovers","United","Kings","Comets","Forge","Harbor"];
var GRAPHIC=["hooped chest band","vertical sash","tonal pinstripes","shoulder yoke panel","chevron chest","half-and-half split"];
var NUMFONT=["block collegiate","condensed modern","retro varsity","sharp italic"];
var SLEEVE=["contrast cuff band","tonal trim","sponsor-free clean","piped edge"];
var COLORS=[["#C8102E","#F5F0E1"],["#0B4F6C","#F4F7F5"],["#1F3D2B","#DAD7CD"],["#3E2A35","#F7C548"],["#1A3C5E","#C9A227"],["#0A0A0A","#E07A3F"]];
function jerseySVG(cols,graphic,num){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="340" viewBox="0 0 300 340">'
  +'<rect width="300" height="340" fill="#FFFFFF"/>'
  +'<path d="M95 40 L60 60 L40 110 L70 120 L80 100 L80 300 L220 300 L220 100 L230 120 L260 110 L240 60 L205 40 Q150 70 95 40 Z" fill="'+cols[0]+'" stroke="#222222" stroke-width="3"/>'
  +'<rect x="80" y="150" width="140" height="26" fill="'+cols[1]+'" opacity="0.9"/>'
  +'<text x="150" y="235" font-family="Georgia,serif" font-size="72" font-weight="bold" text-anchor="middle" fill="'+cols[1]+'">'+num+'</text>'
  +'<text x="150" y="325" font-family="Georgia,serif" font-size="12" text-anchor="middle" fill="#333333">'+graphic+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var club=pick(CLUB_A,s)+" "+pick(CLUB_B,s);
  var cols=pick(COLORS,s), graphic=pick(GRAPHIC,s), numfont=pick(NUMFONT,s), sleeve=pick(SLEEVE,s);
  var num=1+((s()*98)|0);
  var svg=jerseySVG(cols,graphic,num);
  var title=club+" "+field+" — seed "+seed;
  var desc='GENERATED JERSEY — the '+field.toLowerCase()+' for '+club+'. Colors: '+cols.join(' + ')+'. Chest: '+graphic+'. Numbers in '+numfont+'; sleeves: '+sleeve+'. Star number '+num+'.';
  var prog="# Jersey design — "+club+" (seed "+seed+")\n"
    +"club = \""+club+"\"\n"+"kit = \""+field+"\"\n"+"colors = "+JSON.stringify(cols)+"\n"
    +"graphic = \""+graphic+"\"\n"+"number_font = \""+numfont+"\"\n"+"sleeves = \""+sleeve+"\"\n"+"star_number = "+num+"\n"
    +"print(\"Club:\", club, \"[\"+kit+\"]\")\n"+"print(\"Colors:\", \", \".join(colors))\n"
    +"print(\"Chest:\", graphic, \"| Numbers:\", number_font, \"| Sleeves:\", sleeves)\n"
    +"print(\"Jersey SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — jersey record', title:title, description:desc,
    how_it_works:'The generator names a fictional club from word pairs, assigns the kit lane, picks a two-color system with hexes, a chest graphic, a number font, and a sleeve detail, then renders the jersey front as an SVG with the star number — deterministic per seed.',
    key_points:['Club: '+club,'Kit: '+field,'Colors: '+cols.join(' + '),'Chest: '+graphic,'Numbers: '+numfont,'Sleeves: '+sleeve,'Star number: '+num,'Deterministic: seed '+seed+' always rebuilds this exact jersey.'],
    requirements:['A seed number to regenerate this exact jersey','An HTML file to view the jersey SVG'],
    standards:['Club name is original','Two-color system with hex codes','Chest graphic and number font specified','Jersey SVG renders the star number'],
    citations:['Kit craft references: jersey design systems.','Identity references: fictional club naming.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{club:club,kit:field,colors:cols,graphic:graphic,numberFont:numfont,sleeves:sleeve,starNumber:num,svg:svg},
    svg:svg,
    demo:{kind:'jersey-plan',language:'python',program:prog,note:'Prints the club, kit spec, and design details.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.club||!o.graphic||!o.numberFont)e.push('design');
  if(!o.colors||o.colors.length!==2)e.push('colors');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate jersey in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

SHOOT_GENJS = r"""(function(){'use strict';
/* JAH The Personal Photo Shoot Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working photo-shoot planner: every call plans a complete session —
   session title, lane, location, three styled outfits, five directed poses,
   lighting plan, and a six-shot shot list — plus a storyboard SVG.
   Deterministic per seed: same seed, same shoot. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
var FIELDS=["Portrait Session","Fashion Editorial","Lifestyle Story"];
var TITLE_A=["Golden","Amber","Quiet","Neon","Paper","Velvet","Halo","Drift","Ember","Lumen"];
var TITLE_B=["Hour","Muse","Study","Frames","Light","Season","Portrait","Reverie","Static","Bloom"];
var LOC={"Portrait Session":["rooftop at golden hour","botanical garden greenhouse","old library reading room","harbor pier at dawn"],"Fashion Editorial":["abandoned theater lobby","concrete parking structure","desert roadside motel","industrial loft with skylights"],"Lifestyle Story":["morning kitchen, real life","city farmers market","rainy bookstore aisle","backyard garden party"]};
var OUTFITS=["linen suit, open collar","slip dress and boots","denim-on-denim with scarf","knit set, gold hoops","trench over monochrome","velvet blazer, dark jeans"];
var POSES=["chin down, eyes to lens","walking away, glance back","seated, elbows on knees","laughing, mid-motion","profile against the light"];
var LIGHT={"Portrait Session":"soft window key, silver reflector fill","Fashion Editorial":"hard direct flash, deep shadows","Lifestyle Story":"available light only, embrace the grain"};
var SHOTS=["wide establishing frame","medium portrait, 85mm","detail: hands and texture","over-the-shoulder environmental","low-angle hero frame","candid between poses"];
function boardSVG(title,shots){
  var cells='';
  for(var i=0;i<shots.length;i++){
    var x=20+(i%3)*180, y=70+((i/3)|0)*120;
    cells+='<rect x="'+x+'" y="'+y+'" width="160" height="90" rx="6" fill="#2B2D42"/>';
    cells+='<circle cx="'+(x+80)+'" cy="'+(y+45)+'" r="20" fill="#F7C548"/>';
    cells+='<text x="'+(x+80)+'" y="'+(y+108)+'" font-family="Georgia,serif" font-size="10" text-anchor="middle" fill="#333333">'+(i+1)+'. '+shots[i].slice(0,22)+'</text>';
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="580" height="330" viewBox="0 0 580 330"><rect width="580" height="330" fill="#FFFFFF"/><text x="20" y="38" font-family="Georgia,serif" font-size="18" font-weight="bold" fill="#1A1A1A">'+title+' — storyboard</text>'+cells+'</svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var title=pick(TITLE_A,s)+" "+pick(TITLE_B,s);
  var loc=pick(LOC[field],s), outfits=pickN(OUTFITS,s,3), poses=pickN(POSES,s,5), shots=pickN(SHOTS,s,6);
  var svg=boardSVG(title,shots);
  var stitle='“'+title+'” — '+field+" — seed "+seed;
  var desc='GENERATED SHOOT — “'+title+'”, a '+field.toLowerCase()+' at '+loc+'. Three outfits: '+outfits.join('; ')+'. Five directed poses. Lighting: '+LIGHT[field]+'. Six-shot list planned.';
  var prog="# Photo shoot plan — "+title+" (seed "+seed+")\n"
    +"title = \""+title+"\"\n"+"lane = \""+field+"\"\n"+"location = \""+loc+"\"\n"
    +"outfits = "+JSON.stringify(outfits)+"\n"+"poses = "+JSON.stringify(poses)+"\n"
    +"lighting = \""+LIGHT[field]+"\"\n"+"shots = "+JSON.stringify(shots)+"\n"
    +"print(\"Shoot:\", title, \"[\"+lane+\"]\")\n"+"print(\"Location:\", location)\n"+"print(\"Lighting:\", lighting)\n"
    +"[print(\" Outfit %d: %s\" % (i+1, o)) for i, o in enumerate(outfits)]\n"
    +"[print(\" Pose %d: %s\" % (i+1, p)) for i, p in enumerate(poses)]\n"
    +"[print(\" Shot %d: %s\" % (i+1, sh)) for i, sh in enumerate(shots)]\n"
    +"print(\"Storyboard SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:stitle+' — shoot record', title:stitle, description:desc,
    how_it_works:'The generator titles the session from evocative word pairs, picks the lane\u2019s location, draws three outfits, five poses, and six shots without replacement, reads the lane\u2019s lighting plan, and renders a storyboard SVG — deterministic per seed.',
    key_points:['Session: “'+title+'”','Lane: '+field,'Location: '+loc,'Outfits: '+outfits.join('; '),'Poses: '+poses.join('; '),'Lighting: '+LIGHT[field],'Shots: '+shots.length+' planned','Deterministic: seed '+seed+' always rebuilds this exact shoot.'],
    requirements:['A seed number to regenerate this exact shoot','An HTML file to view the storyboard SVG'],
    standards:['Three distinct outfits','Five distinct directed poses','Six-shot shot list','Storyboard SVG numbers every shot'],
    citations:['Photography craft references: session planning.','Direction references: pose libraries.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{session:title,lane:field,location:loc,outfits:outfits,poses:poses,lighting:LIGHT[field],shots:shots,svg:svg},
    svg:svg,
    demo:{kind:'shoot-plan',language:'python',program:prog,note:'Prints the full session plan: outfits, poses, shots.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.session||!o.location||!o.lighting)e.push('plan');
  if(!o.outfits||o.outfits.length!==3)e.push('outfits');
  if(!o.poses||o.poses.length!==5)e.push('poses');
  if(!o.shots||o.shots.length!==6)e.push('shots');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate shoot in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

TRANSFORM_GENJS = r"""(function(){'use strict';
/* JAH The Style Transformation Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working style-transformation generator: every call designs a complete
   before-and-after — current style profile, target style profile, five garment
   swaps, a keep list, a focused shopping list, and a before/after panel SVG.
   Deterministic per seed: same seed, same transformation. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
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
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

CAR_GENJS = r"""(function(){'use strict';
/* JAH The Concept Car Studio generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working concept-car studio: every call invents an original vehicle —
   model name, class lane, design language, honest specs (range, power, 0-60),
   signature features, colorway — and renders a side-profile SVG.
   Deterministic per seed: same seed, same concept. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
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
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

ARM_GENJS = r"""(function(){'use strict';
/* JAH The Robot Arm Playground generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working robot-arm designer: every call designs an original arm concept —
   name, lane, segment plan with joint types, degrees of freedom, end effector,
   payload and reach specs, control notes — and renders an arm diagram SVG.
   Deterministic per seed: same seed, same arm. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
var FIELDS=["Desktop Maker Arm","Industrial Helper","Expressive Performer"];
var NAME_A=["Tinker","Atlas","Wren","Pivot","Juno","Cog","Mira","Axle","Nova","Gimbal"];
var NAME_B=["Arm","MK-II","Hand","Rig","Crane","Limb","Helper","Dancer","Builder","Scout"];
var JOINTS=["revolute base yaw","shoulder pitch","shoulder roll","elbow pitch","elbow roll","wrist pitch","wrist roll","tool flange rotate"];
var EFFECTOR={"Desktop Maker Arm":"magnetic quick-swap toolhead (pen, gripper, solder)","Industrial Helper":"vacuum gripper with force feedback","Expressive Performer":"soft silicone hand, five compliant fingers"};
var SPEC={"Desktop Maker Arm":{dof:5,payload:"0.5 kg",reach:"62 cm"},"Industrial Helper":{dof:6,payload:"8 kg",reach:"140 cm"},"Expressive Performer":{dof:7,payload:"1.2 kg",reach:"95 cm"}};
var CONTROL=["teach-pendant jogging","drag-to-teach waypoints","Python SDK scripting","safety-rated monitored stop"];
function armSVG(dof,name){
  var segs='',x=70,y=190,ang=-55;
  for(var i=0;i<dof;i++){
    var len=52-(i*3), nx=x+len*Math.cos(ang*Math.PI/180), ny=y+len*Math.sin(ang*Math.PI/180);
    segs+='<line x1="'+x+'" y1="'+y+'" x2="'+nx+'" y2="'+ny+'" stroke="#2B2D42" stroke-width="12" stroke-linecap="round"/>';
    segs+='<circle cx="'+x+'" cy="'+y+'" r="10" fill="#C8102E"/>';
    x=nx;y=ny;ang+=18;
  }
  segs+='<circle cx="'+x+'" cy="'+y+'" r="10" fill="#C8102E"/><rect x="'+(x-4)+'" y="'+(y-26)+'" width="26" height="22" rx="4" fill="#F7C548" stroke="#222"/>';
  return '<svg xmlns="http://www.w3.org/2000/svg" width="420" height="280" viewBox="0 0 420 280">'
  +'<rect width="420" height="280" fill="#FFFFFF"/>'
  +'<rect x="40" y="190" width="60" height="50" rx="8" fill="#8A8D93"/>'+segs
  +'<text x="210" y="268" font-family="Georgia,serif" font-size="15" font-weight="bold" text-anchor="middle" fill="#1A1A1A">'+name+' — '+dof+' DOF</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var name=pick(NAME_A,s)+" "+pick(NAME_B,s);
  var spec=SPEC[field], joints=pickN(JOINTS,s,spec.dof), ctrl=pickN(CONTROL,s,2);
  var svg=armSVG(spec.dof,name);
  var title=name+" — "+field+" — seed "+seed;
  var desc='GENERATED ROBOT ARM — the '+name+', a '+field.toLowerCase()+'. '+spec.dof+' degrees of freedom ('+joints.join(', ')+'). End effector: '+EFFECTOR[field]+'. Payload '+spec.payload+', reach '+spec.reach+'. Control: '+ctrl.join(' + ')+'.';
  var prog="# Robot arm concept — "+name+" (seed "+seed+")\n"
    +"name = \""+name+"\"\n"+"lane = \""+field+"\"\n"+"dof = "+spec.dof+"\n"
    +"joints = "+JSON.stringify(joints)+"\n"+"effector = \""+EFFECTOR[field]+"\"\n"
    +"payload = \""+spec.payload+"\"\n"+"reach = \""+spec.reach+"\"\n"+"control = "+JSON.stringify(ctrl)+"\n"
    +"print(\"Arm:\", name, \"[\"+lane+\"]\", dof, \"DOF\")\n"
    +"[print(\" Joint %d: %s\" % (i+1, j)) for i, j in enumerate(joints)]\n"
    +"print(\"Effector:\", effector)\n"+"print(\"Payload:\", payload, \"| Reach:\", reach)\n"
    +"print(\"Control:\", \", \".join(control))\n"+"print(\"Diagram SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — arm record', title:title, description:desc,
    how_it_works:'The generator names an original arm, assigns the lane, reads its DOF/payload/reach spec, draws that many joint types without replacement, reads the lane\u2019s end effector, picks two control modes, and renders a jointed arm diagram SVG — deterministic per seed.',
    key_points:['Arm: '+name,'Lane: '+field,'DOF: '+spec.dof,'Joints: '+joints.join(', '),'Effector: '+EFFECTOR[field],'Payload: '+spec.payload+', Reach: '+spec.reach,'Control: '+ctrl.join(' + '),'Deterministic: seed '+seed+' always rebuilds this exact arm.'],
    requirements:['A seed number to regenerate this exact arm','An HTML file to view the diagram SVG'],
    standards:['Joint count matches the lane DOF','End effector specified per lane','Payload and reach in the spec block'],
    citations:['Robotics craft references: arm kinematics.','Design references: concept diagramming.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{arm:name,lane:field,dof:spec.dof,joints:joints,effector:EFFECTOR[field],payload:spec.payload,reach:spec.reach,control:ctrl,svg:svg},
    svg:svg,
    demo:{kind:'arm-plan',language:'python',program:prog,note:'Prints the arm spec: joints, effector, payload, reach.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.arm||!o.effector)e.push('design');
  if(!o.joints||o.joints.length!==o.dof)e.push('joints');
  if(!o.payload||!o.reach)e.push('specs');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate arm in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

def _item(slug, name, tagline, record_kind, ai_name, role, greet, searchph, chatph, short, fields, genjs, gen_desc, sig_tagline, first_release_pick=False):
    return {
        'slug': slug, 'cls': 'gen', 'renderer': None,
        'name': name, 'tagline': tagline, 'record_kind': record_kind,
        'ai_name': ai_name, 'role': role, 'greet': greet, 'searchph': searchph,
        'chatph': chatph, 'short': short, 'fields': fields,
        'hero_extra': 'Every record carries the full entry: description, how it works, key points, requirements, standards, citations, and a working demonstration program. Records are ordered by the teaching ladder, simple to complex.',
        'sig_tagline': sig_tagline, 'genjs': genjs, 'gen_desc': gen_desc,
        'prefix': None,  # filled from prefixes.json by build.py
        'first_release_pick': first_release_pick,
    }

ITEMS = [
_item('outfit-generator', 'The Outfit Generator Database',
 'Build complete outfits from the clothes you have: occasion, weather, and personal style in — head-to-toe looks with tops, bottoms, shoes, outerwear, accessories, and a coordinated palette, every seed a new outfit worth wearing.',
 'outfit generator record', 'JAH Outfit Generator Archivist',
 'outfit generator archivist — operating a real working outfit builder and teaching outfit coordination; answering from many angles using only archive data',
 'Ask me to build an outfit — pick an occasion or let the seed decide.',
 'Search outfits, occasions, palettes, styling...', 'Ask for an outfit...', 'outfit',
 ['Casual Day','Work & Professional','Evening & Events'], OUTFIT_GENJS,
 'A real working outfit builder: pick an occasion and seed, get a complete head-to-toe outfit — garments, accessories, palette, and flat-lay art.',
 'The Signature treatment of outfit generation: the same real builder carried forward, plus Signature-original occasion lanes and impossible combinations original to this system.',
 first_release_pick=True),
_item('personal-color-palette', 'The Personal Color Palette Database',
 'Find the colors that love you back: seasonal color analysis with undertones, six-swatch palettes with hex codes, best neutrals, and colors to avoid — every seed a palette built for self-expression.',
 'color palette record', 'JAH Personal Color Palette Archivist',
 'personal color palette archivist — operating a real working palette analyst and teaching color analysis; answering from many angles using only archive data',
 'Ask me for your palette — pick a season or let the seed decide.',
 'Search palettes, seasons, undertones, swatches...', 'Ask for a palette...', 'palette',
 ['Spring Warm','Summer Cool','Autumn Warm','Winter Cool'], PALETTE_GENJS,
 'A real working color analyst: pick a season and seed, get a full palette — swatches, hexes, neutrals, and avoid-list.',
 'The Signature treatment of color palettes: the same real analyst carried forward, plus Signature-original seasonal readings original to this system.'),
_item('makeup-look-studio', 'The Makeup Look Studio',
 'Design your face like a canvas: complete makeup looks by occasion — base, eyes, cheeks, lips, ordered application steps, and a face chart mapping every zone, every seed a new look to try.',
 'makeup look record', 'JAH Makeup Look Studio Archivist',
 'makeup look studio archivist — operating a real working look designer and teaching makeup craft; answering from many angles using only archive data',
 'Ask me for a makeup look — pick an occasion or let the seed decide.',
 'Search makeup looks, occasions, application...', 'Ask for a look...', 'makeup',
 ['Natural Day','Evening Glam','Bold Editorial'], MAKEUP_GENJS,
 'A real working look designer: pick an occasion and seed, get a complete look — four zones, five steps, and a face chart.',
 'The Signature treatment of makeup looks: the same real designer carried forward, plus Signature-original look lanes original to this system.'),
_item('uniform-designer', 'The Uniform Designer Database',
 'Dress the whole team as one: cohesive uniform concepts for clubs, teams, and businesses — role variants, color systems, insignia, fabrics, and care, every seed a new identity in cloth.',
 'uniform designer record', 'JAH Uniform Designer Archivist',
 'uniform designer archivist — operating a real working uniform designer and teaching uniform systems; answering from many angles using only archive data',
 'Ask me to design a uniform — pick a lane or let the seed decide.',
 'Search uniforms, roles, colors, insignia...', 'Ask for a uniform...', 'uniform',
 ['Service & Hospitality','Sports Teams','Corporate Crews'], UNIFORM_GENJS,
 'A real working uniform designer: pick a lane and seed, get a cohesive concept — client, roles, colors, fabrics.',
 'The Signature treatment of uniform design: the same real designer carried forward, plus Signature-original client lanes original to this system.'),
_item('team-jersey-studio', 'The Team Jersey Studio',
 'Kit out your fictional club: original jersey designs with team identity, color systems, chest graphics, number fonts, and sleeve details — every seed a jersey worth wearing on match day.',
 'team jersey record', 'JAH Team Jersey Studio Archivist',
 'team jersey studio archivist — operating a real working jersey studio and teaching kit design; answering from many angles using only archive data',
 'Ask me to design a jersey — pick a kit or let the seed decide.',
 'Search jerseys, kits, clubs, graphics...', 'Ask for a jersey...', 'jersey',
 ['Home Kit','Away Kit','Special Edition'], JERSEY_GENJS,
 'A real working jersey studio: pick a kit and seed, get an original design — club, colors, graphics, numbers.',
 'The Signature treatment of jersey design: the same real studio carried forward, plus Signature-original kit lanes original to this system.'),
_item('personal-photo-shoot', 'The Personal Photo Shoot Database',
 'Plan your perfect shoot: session concepts with locations, styled outfits, directed poses, lighting plans, and shot lists — every seed a shoot worth booking the photographer for.',
 'photo shoot record', 'JAH Personal Photo Shoot Archivist',
 'personal photo shoot archivist — operating a real working shoot planner and teaching photo direction; answering from many angles using only archive data',
 'Ask me to plan a shoot — pick a lane or let the seed decide.',
 'Search photo shoots, poses, locations, lighting...', 'Ask for a shoot plan...', 'photoshoot',
 ['Portrait Session','Fashion Editorial','Lifestyle Story'], SHOOT_GENJS,
 'A real working shoot planner: pick a lane and seed, get a full session — location, outfits, poses, shots.',
 'The Signature treatment of shoot planning: the same real planner carried forward, plus Signature-original session lanes original to this system.'),
_item('style-transformation', 'The Style Transformation Database',
 'Reinvent how you dress: before-and-after style concepts with current and target profiles, garment swaps, keep lists, and shopping lists — every seed a new you to try on.',
 'style transformation record', 'JAH Style Transformation Archivist',
 'style transformation archivist — operating a real working transformation designer and teaching style evolution; answering from many angles using only archive data',
 'Ask me for a transformation — pick a lane or let the seed decide.',
 'Search transformations, before-and-after, style...', 'Ask for a transformation...', 'transformation',
 ['Wardrobe Refresh','Full Reinvention','Occasion Overhaul'], TRANSFORM_GENJS,
 'A real working transformation designer: pick a lane and seed, get a before-and-after — swaps, keeps, and shop list.',
 'The Signature treatment of style transformation: the same real designer carried forward, plus Signature-original transformation lanes original to this system.'),
_item('concept-car-studio', 'The Concept Car Studio',
 'Invent the car of tomorrow: original vehicle concepts with design language, honest specs, signature features, and colorways — every seed a machine worth sketching.',
 'concept car record', 'JAH Concept Car Studio Archivist',
 'concept car studio archivist — operating a real working vehicle inventor and teaching concept design; answering from many angles using only archive data',
 'Ask me to invent a car — pick a class or let the seed decide.',
 'Search concept cars, classes, specs, design...', 'Ask for a concept car...', 'car',
 ['City Electric','Grand Tourer','Off-Road Explorer'], CAR_GENJS,
 'A real working vehicle inventor: pick a class and seed, get an original concept — design language, specs, features.',
 'The Signature treatment of concept cars: the same real inventor carried forward, plus Signature-original vehicle classes original to this system.'),
_item('robot-arm-playground', 'The Robot Arm Playground',
 'Design arms that work and play: robot-arm concepts for making, helping, and performing — joints, end effectors, payload, reach, and control, every seed a new machine to build.',
 'robot arm record', 'JAH Robot Arm Playground Archivist',
 'robot arm playground archivist — operating a real working arm designer and teaching robot design; answering from many angles using only archive data',
 'Ask me to design an arm — pick a lane or let the seed decide.',
 'Search robot arms, joints, effectors, control...', 'Ask for an arm design...', 'robot',
 ['Desktop Maker Arm','Industrial Helper','Expressive Performer'], ARM_GENJS,
 'A real working arm designer: pick a lane and seed, get a full concept — joints, effector, payload, reach.',
 'The Signature treatment of robot arms: the same real designer carried forward, plus Signature-original arm lanes original to this system.'),
]
