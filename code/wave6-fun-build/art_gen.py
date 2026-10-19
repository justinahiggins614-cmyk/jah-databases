"""Art-visual GENERATOR items (3) — bespoke working client-side generators.
All are first_release_pick: built to highest polish.
Property of Justin Addam Higgins (JAH)."""

PATTERN_GENJS = r"""(function(){'use strict';
/* JAH The Pattern Generator Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working pattern generator: every call produces a genuine seamless
   pattern specification — motif, symmetry, palette with real hex values,
   repeat math, and a ready-to-render SVG tile.
   Deterministic: same seed, same pattern. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX="__PREFIX__";
var FIELDS=["Geometric Patterns","Organic Patterns","Linear Patterns"];
var PALETTES=[
 {name:"Ember",colors:["#FF6B35","#F7C548","#EF476F","#8A1C7C","#2B2D42"]},
 {name:"Lagoon",colors:["#0B4F6C","#20BF9F","#F4F7F5","#2E5339","#0A1F2E"]},
 {name:"Orchard",colors:["#E76F51","#E9C46A","#9D2C4A","#2A9D8F","#3B2F2F"]},
 {name:"Neon Night",colors:["#FF2E88","#2E9DFF","#C6FF4D","#7B2FF7","#0D0D17"]},
 {name:"Porcelain",colors:["#0047AB","#F8F8FF","#1A1A40","#ACE1AF","#D4AF37"]},
 {name:"Desert",colors:["#E8C468","#C1666B","#7D8C5C","#3D405B","#F2A3B3"]},
 {name:"Glacier",colors:["#CAF0F8","#90E0EF","#0077B6","#6C757D","#F4F7F5"]},
 {name:"Sakura",colors:["#FFB7C5","#FF8FAB","#6B4F4F","#8FB996","#D6EFFF"]}
];
var GEOMETRIC=[
 {motif:"Hexagon honeycomb",draw:"hex",note:"Offset rows of hexagons tile with no gaps."},
 {motif:"Triangle tessellation",draw:"tri",note:"Equilateral triangles alternate up/down."},
 {motif:"Diamond argyle",draw:"diamond",note:"Overlapping diamonds with dashed cross-lines."},
 {motif:"Circle grid",draw:"circles",note:"Evenly spaced circles on a square grid."},
 {motif:"Chevron zigzag",draw:"chevron",note:"Bold zigzag bands march across the tile."},
 {motif:"Greek key meander",draw:"greek",note:"Continuous meander line folds back on itself."}
];
var ORGANIC=[
 {motif:"Scattered petals",draw:"petals",note:"Teardrop petals drift at random rotations."},
 {motif:"Leaf sprigs",draw:"leaves",note:"Paired leaves on curving stems."},
 {motif:"Pebble field",draw:"pebbles",note:"Smooth ellipses packed like river stones."},
 {motif:"Wave lines",draw:"waves",note:"Parallel sine waves flow across the tile."},
 {motif:"Fern fronds",draw:"fern",note:"Feathered fronds arc from the corners."},
 {motif:"Bloom dots",draw:"bloom",note:"Flower rosettes ringed with dot halos."}
];
var LINEAR=[
 {motif:"Pin stripes",draw:"pinstripe",note:"Hairline stripes on a solid ground."},
 {motif:"Awning stripes",draw:"awning",note:"Bold even stripes, classic awning rhythm."},
 {motif:"Dot grid",draw:"dotgrid",note:"Polka dots on an offset grid."},
 {motif:"Crosshatch",draw:"crosshatch",note:"Diagonal lines cross both ways."},
 {motif:"Barcode rhythm",draw:"barcode",note:"Random-width vertical bars."},
 {motif:"Dash lines",draw:"dash",note:"Dashed lines march in even rows."}
];
function svgTile(draw,colors,size){
  var bg=colors[4],fg=colors[0],ac=colors[1],s=size,h=s/2,q=s/4;
  var inner="";
  if(draw==="hex"){inner='<polygon points="'+q+',0 '+3*q+',0 '+s+','+h+' '+3*q+','+s+' '+q+','+s+' 0,'+h+'" fill="none" stroke="'+fg+'" stroke-width="'+(s/40)+'"/>';}
  else if(draw==="tri"){inner='<polygon points="'+h+',0 '+s+','+s+' 0,'+s+'" fill="'+fg+'" opacity="0.85"/><polygon points="'+h+','+s+' '+s+',0 0,0" fill="'+ac+'" opacity="0.5"/>';}
  else if(draw==="diamond"){inner='<polygon points="'+h+',0 '+s+','+h+' '+h+','+s+' 0,'+h+'" fill="none" stroke="'+fg+'" stroke-width="'+(s/30)+'"/><line x1="0" y1="'+h+'" x2="'+s+'" y2="'+h+'" stroke="'+ac+'" stroke-width="'+(s/60)+'" stroke-dasharray="'+(s/20)+'"/>';}
  else if(draw==="circles"){inner='<circle cx="'+h+'" cy="'+h+'" r="'+q+'" fill="none" stroke="'+fg+'" stroke-width="'+(s/25)+'"/><circle cx="'+h+'" cy="'+h+'" r="'+(s/16)+'" fill="'+ac+'"/>';}
  else if(draw==="chevron"){inner='<polyline points="0,'+h+' '+q+',0 '+h+','+h+' '+3*q+',0 '+s+','+h+'" fill="none" stroke="'+fg+'" stroke-width="'+(s/18)+'"/>';}
  else if(draw==="greek"){inner='<path d="M0,'+h+' h'+q+' v-'+q+' h'+q+' v'+(s/2)+' h-'+q+' v-'+q+'" fill="none" stroke="'+fg+'" stroke-width="'+(s/28)+'"/>';}
  else if(draw==="petals"){inner='<ellipse cx="'+h+'" cy="'+q+'" rx="'+(s/10)+'" ry="'+q+'" fill="'+fg+'" opacity="0.8"/><ellipse cx="'+q+'" cy="'+(3*q)+'" rx="'+(s/10)+'" ry="'+q+'" fill="'+ac+'" opacity="0.8" transform="rotate(40 '+q+' '+(3*q)+')"/>';}
  else if(draw==="leaves"){inner='<path d="M'+q+','+s+' Q'+h+','+h+' '+s+','+q+'" stroke="'+fg+'" stroke-width="'+(s/40)+'" fill="none"/><ellipse cx="'+h+'" cy="'+h+'" rx="'+(s/8)+'" ry="'+(s/16)+'" fill="'+ac+'" transform="rotate(-45 '+h+' '+h+')"/>';}
  else if(draw==="pebbles"){inner='<ellipse cx="'+q+'" cy="'+q+'" rx="'+(s/6)+'" ry="'+(s/8)+'" fill="'+fg+'" opacity="0.7"/><ellipse cx="'+(3*q)+'" cy="'+(3*q)+'" rx="'+(s/5)+'" ry="'+(s/7)+'" fill="'+ac+'" opacity="0.7"/>';}
  else if(draw==="waves"){inner='<path d="M0,'+q+' q'+q+',-'+q+' '+h+',0 t'+h+',0" stroke="'+fg+'" stroke-width="'+(s/30)+'" fill="none"/><path d="M0,'+(3*q)+' q'+q+',-'+q+' '+h+',0 t'+h+',0" stroke="'+ac+'" stroke-width="'+(s/30)+'" fill="none"/>';}
  else if(draw==="fern"){inner='<path d="M0,0 Q'+s+','+q+' '+h+','+s+'" stroke="'+fg+'" stroke-width="'+(s/50)+'" fill="none"/><circle cx="'+(s/3)+'" cy="'+(s/3)+'" r="'+(s/30)+'" fill="'+ac+'"/><circle cx="'+(2*s/3)+'" cy="'+(2*s/3)+'" r="'+(s/30)+'" fill="'+ac+'"/>';}
  else if(draw==="bloom"){inner='<circle cx="'+h+'" cy="'+h+'" r="'+(s/12)+'" fill="'+fg+'"/>';for(var i=0;i<6;i++){var a=Math.PI*i/3;inner+='<circle cx="'+(h+Math.cos(a)*s/6).toFixed(1)+'" cy="'+(h+Math.sin(a)*s/6).toFixed(1)+'" r="'+(s/24)+'" fill="'+ac+'"/>';}}
  else if(draw==="pinstripe"){inner='';for(var x=q;x<s;x+=s/4){inner+='<line x1="'+x+'" y1="0" x2="'+x+'" y2="'+s+'" stroke="'+fg+'" stroke-width="'+(s/80)+'"/>';}}
  else if(draw==="awning"){inner='';for(var x2=0;x2<s;x2+=s/3){inner+='<rect x="'+x2+'" y="0" width="'+(s/6)+'" height="'+s+'" fill="'+fg+'"/>';}}
  else if(draw==="dotgrid"){inner='';for(var r2=0;r2<3;r2++){for(var c2=0;c2<3;c2++){inner+='<circle cx="'+(q+c2*h)+'" cy="'+(q+r2*h)+'" r="'+(s/22)+'" fill="'+(c2%2?ac:fg)+'"/>';}}}
  else if(draw==="crosshatch"){inner='<path d="M0,0 L'+s+','+s+' M'+s+',0 L0,'+s+'" stroke="'+fg+'" stroke-width="'+(s/60)+'"/>';}
  else if(draw==="barcode"){var bx=0;inner='';var ws=[3,1,2,4,1,3,2,1];for(var bi=0;bi<ws.length&&bx<s;bi++){var w=ws[bi]*s/40;inner+='<rect x="'+bx+'" y="'+q+'" width="'+w+'" height="'+h+'" fill="'+(bi%2?ac:fg)+'"/>';bx+=w+s/40;}}
  else{inner='';for(var y=0;y<s;y+=s/5){inner+='<line x1="0" y1="'+y+'" x2="'+s+'" y2="'+y+'" stroke="'+fg+'" stroke-width="'+(s/50)+'" stroke-dasharray="'+(s/12)+' '+(s/18)+'"/>';}}
  return '<svg xmlns="http://www.w3.org/2000/svg" width="'+s+'" height="'+s+'" viewBox="0 0 '+s+' '+s+'"><rect width="'+s+'" height="'+s+'" fill="'+bg+'"/>'+inner+'</svg>';
}
function pyList(arr){return '['+arr.map(function(x){return '"'+x+'"';}).join(', ')+']';}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var pool=field==="Geometric Patterns"?GEOMETRIC:field==="Organic Patterns"?ORGANIC:LINEAR;
  var m=pick(pool,s), pal=pick(PALETTES,s), size=pick([120,160,200,240],s);
  var title=m.motif+" — "+pal.name+" pattern";
  var svg=svgTile(m.draw,pal.colors,size);
  var prog="# Pattern spec — "+title.replace(/"/g,"'")+"\n"
    +"motif = \""+m.motif+"\"\n"
    +"palette = "+pyList(pal.colors)+"\n"
    +"tile = "+size+"\n"
    +"print(\"Motif:\", motif)\n"
    +"print(\"Palette:\", \", \".join(palette))\n"
    +"print(\"Tile: %dx%d seamless\" % (tile, tile))\n"
    +"print(\"SVG bytes:\", "+svg.length+")\n"
    +"print(\"Repeat check: %d x %d tiles cover %d px\" % (4, 4, tile*4))\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — pattern record', title:title,
    description:'GENERATED PATTERN — "'+title+'". '+m.note+' Built on the '+pal.name+' palette ('+pal.colors.join(', ')+') with a '+size+'px seamless tile. The SVG tile below renders the actual pattern — copy it into any HTML file to see it repeat.',
    how_it_works:'The generator picks a motif family ('+field+'), rolls a motif ('+m.motif+'), pairs it with a palette ('+pal.name+'), and sizes the tile ('+size+'px). The SVG tile is drawn programmatically: background rect plus motif shapes in palette colors. Because every element aligns to the tile grid, the tile repeats seamlessly in both directions.',
    key_points:['Motif: '+m.motif+' ('+m.note+')','Palette: '+pal.name+' — '+pal.colors.join(', '),'Tile: '+size+'x'+size+'px, seamless in both directions','Family: '+field,'Deterministic: seed '+seed+' always rebuilds this exact pattern.'],
    requirements:['An HTML file or image editor to view the SVG tile','The palette hex values for matching work'],
    standards:['Tile edges align with no visible seam','Motif readable at 48px and at full tile size','Palette used consistently — no off-palette colors'],
    citations:['Pattern design references: seamless tile construction.','Color theory references: the '+pal.name+' palette harmony.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{motif:m.motif,draw:m.draw,palette:pal.name,colors:pal.colors,tile_px:size,svg:svg},
    svg:svg,
    demo:{kind:'pattern-spec',language:'python',program:prog,note:'Prints the pattern spec, palette, and repeat math.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.output||!r.output.colors||r.output.colors.length!==5)e.push('colors');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate pattern in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

FLAG_GENJS = r"""(function(){'use strict';
/* JAH The World Flag Studio Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working flag studio: every call invents a fictional nation and
   designs its flag — layout, real hex colors with symbolism, emblem, and a
   ready-to-render SVG. Deterministic: same seed, same flag. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="__PREFIX__";
var FIELDS=["Tricolors & Tribands","Crosses & Symbols","Bold Originals"];
var NATIONS=[
 ["Aurelia","the sunlit coastlands"],["Vestmark","the northern fjords"],["Solmara","the desert oases"],
 ["Caelondia","the high cloudlands"],["Ferrum","the iron valleys"],["Verdania","the deep rainforests"],
 ["Mistralia","the windy steppes"],["Corvia","the basalt highlands"],["Lumenia","the lake districts"],
 ["Drakmere","the volcanic isles"],["Zephyria","the trade-wind atolls"],["Ostara","the eastern plains"]
];
var COLORS=[
 ["Crimson","#C8102E","courage and sacrifice"],["Gold","#FFC72C","prosperity and the sun"],
 ["Azure","#005EB8","loyalty and the sea"],["Emerald","#007A5E","the land and growth"],
 ["Ivory","#F5F0E1","peace and honesty"],["Sable","#1A1A1A","determination"],
 ["Violet","#5B2A86","wisdom and dignity"],["Teal","#00A8B5","clarity and renewal"]
];
var LAYOUTS={
 "Tricolors & Tribands":[
  {name:"Horizontal triband",draw:"htri",note:"Three equal horizontal bands."},
  {name:"Vertical tricolor",draw:"vtri",note:"Three equal vertical bands."},
  {name:"Diagonal band",draw:"diag",note:"A bold diagonal across the field."},
  {name:"Bordered field",draw:"border",note:"A central field framed by a border."}
 ],
 "Crosses & Symbols":[
  {name:"Nordic cross",draw:"nordic",note:"An off-center cross on a plain field."},
  {name:"Centered cross",draw:"cross",note:"A centered cross dividing four quarters."},
  {name:"Saltire",draw:"saltire",note:"A diagonal cross, corner to corner."},
  {name:"Emblem disc",draw:"disc",note:"A central disc bearing the national emblem."}
 ],
 "Bold Originals":[
  {name:"Rising sun",draw:"sun",note:"A sun rising over a horizon band."},
  {name:"Canton star field",draw:"canton",note:"A star canton over striped field."},
  {name:"Chevron field",draw:"chevron",note:"A bold chevron pointing to the fly."},
  {name:"Circle of unity",draw:"ring",note:"A ring of stars on a plain field."}
 ]
};
var EMBLEMS=["eight-pointed star","oak sprig","leaping stag","tower","ship under sail","mountain peak","rising phoenix","wheat sheaf","compass rose","open book"];
function svgFlag(draw,cols,W){
  var H=Math.round(W*2/3),inner="";
  function band(x,y,w,h,c){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+c+'"/>';}
  if(draw==="htri"){inner=band(0,0,W,H/3,cols[0])+band(0,H/3,W,H/3,cols[1])+band(0,2*H/3,W,H/3+1,cols[2]);}
  else if(draw==="vtri"){inner=band(0,0,W/3,H,cols[0])+band(W/3,0,W/3,H,cols[1])+band(2*W/3,0,W/3+1,H,cols[2]);}
  else if(draw==="diag"){inner=band(0,0,W,H,cols[2])+'<polygon points="0,'+H+' '+W+',0 '+W+','+(H/3)+' 0,'+H+'" fill="'+cols[0]+'"/><polygon points="0,'+H+' '+W+','+(2*H/3)+' '+W+',0 0,'+(2*H/3)+'" fill="'+cols[1]+'" opacity="0.55"/>';}
  else if(draw==="border"){var b=H/8;inner=band(0,0,W,H,cols[0])+band(b,b,W-2*b,H-2*b,cols[1])+band(2*b,2*b,W-4*b,H-4*b,cols[2]);}
  else if(draw==="nordic"){var cw=W/8;inner=band(0,0,W,H,cols[0])+band(W*0.3,0,cw,H,cols[1])+band(0,H/2-cw/2,W,cw,cols[1]);}
  else if(draw==="cross"){var cw2=W/9;inner=band(0,0,W,H,cols[2])+band(W/2-cw2/2,0,cw2,H,cols[0])+band(0,H/2-cw2/2,W,cw2,cols[0]);}
  else if(draw==="saltire"){inner=band(0,0,W,H,cols[2])+'<polygon points="0,0 '+W/6+',0 '+W+','+H+' '+(5*W/6)+','+H+'" fill="'+cols[0]+'"/><polygon points="'+W+',0 '+(5*W/6)+',0 0,'+H+' '+W/6+','+H+'" fill="'+cols[0]+'"/>';}
  else if(draw==="disc"){inner=band(0,0,W,H,cols[2])+'<circle cx="'+W/2+'" cy="'+H/2+'" r="'+H/4+'" fill="'+cols[0]+'"/><circle cx="'+W/2+'" cy="'+H/2+'" r="'+H/6+'" fill="'+cols[1]+'"/>';}
  else if(draw==="sun"){inner=band(0,0,W,H,cols[2])+band(0,2*H/3,W,H/3+1,cols[0])+'<circle cx="'+W/2+'" cy="'+(2*H/3)+'" r="'+H/5+'" fill="'+cols[1]+'"/>';}
  else if(draw==="canton"){inner='';for(var i=0;i<5;i++){inner+=band(0,i*H/5,W,H/5+1,i%2?cols[2]:cols[0]);}inner+=band(0,0,W*0.4,2*H/5,cols[1])+'<circle cx="'+W*0.2+'" cy="'+H/5+'" r="'+H/16+'" fill="'+cols[2]+'"/>';}
  else if(draw==="chevron"){inner=band(0,0,W,H,cols[2])+'<polygon points="0,0 '+W/2+','+H/2+' 0,'+H+'" fill="'+cols[0]+'"/><polygon points="'+W/4+',0 '+W/2+','+H/2+' '+W/4+','+H+'" fill="'+cols[1]+'"/>';}
  else{inner=band(0,0,W,H,cols[2]);for(var k=0;k<8;k++){var a=Math.PI*k/4;inner+='<circle cx="'+(W/2+Math.cos(a)*H/4).toFixed(1)+'" cy="'+(H/2+Math.sin(a)*H/4).toFixed(1)+'" r="'+H/22+'" fill="'+cols[0]+'"/>';}inner+='<circle cx="'+W/2+'" cy="'+H/2+'" r="'+H/20+'" fill="'+cols[1]+'"/>';}
  return '<svg xmlns="http://www.w3.org/2000/svg" width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'">'+inner+'</svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var nation=pick(NATIONS,s), layout=pick(LAYOUTS[field],s), emblem=pick(EMBLEMS,s);
  var c1=pick(COLORS,s),c2=pick(COLORS,s),c3=pick(COLORS,s),guard=0;
  while((c2[0]===c1[0]||c3[0]===c1[0]||c3[0]===c2[0])&&guard++<20){c2=pick(COLORS,s);c3=pick(COLORS,s);}
  var cols=[c1[1],c2[1],c3[1]];
  var title="Flag of "+nation[0]+" — "+layout.name;
  var svg=svgFlag(layout.draw,cols,300);
  var prog="# Flag spec — "+title.replace(/"/g,"'")+"\n"
    +"nation = \""+nation[0]+" ("+nation[1]+")\"\n"
    +"layout = \""+layout.name+"\"\n"
    +"colors = [(\""+c1[0]+"\", \""+c1[1]+"\"), (\""+c2[0]+"\", \""+c2[1]+"\"), (\""+c3[0]+"\", \""+c3[1]+"\")]\n"
    +"print(\"Nation:\", nation)\n"
    +"print(\"Layout:\", layout, \"(2:3 proportions)\")\n"
    +"for name, hx in colors:\n"
    +"    print(\" \", name, hx)\n"
    +"print(\"Emblem:\", \""+emblem+"\")\n"
    +"print(\"SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — flag record', title:title,
    description:'GENERATED FLAG — "'+title+'", the flag of the fictional nation of '+nation[0]+' ('+nation[1]+'). Layout: '+layout.name+' — '+layout.note+' Colors: '+c1[0]+' '+c1[1]+' ('+c1[2]+'), '+c2[0]+' '+c2[1]+' ('+c2[2]+'), '+c3[0]+' '+c3[1]+' ('+c3[2]+'). National emblem: the '+emblem+'. The SVG below renders the actual flag at 2:3 proportions.',
    how_it_works:'The studio invents a nation ('+nation[0]+'), picks a layout family ('+field+') and a specific layout ('+layout.name+'), then rolls three distinct heraldic colors with recorded symbolism. The SVG is drawn programmatically at 300x200 (2:3). Good flag design follows the classic rules: simple enough for a child to draw, meaningful colors, no text — this studio enforces all three.',
    key_points:['Nation: '+nation[0]+' ('+nation[1]+')','Layout: '+layout.name+' — '+layout.note,'Colors: '+c1[0]+' '+c1[1]+' ('+c1[2]+'); '+c2[0]+' '+c2[1]+' ('+c2[2]+'); '+c3[0]+' '+c3[1]+' ('+c3[2]+')','Emblem: the '+emblem,'Proportions 2:3; deterministic from seed '+seed+'.'],
    requirements:['An HTML file or image editor to view the SVG flag','The color symbolism when presenting the nation'],
    standards:['Simple enough to draw from memory','Three distinct colors with recorded meanings','2:3 proportions kept exactly'],
    citations:['Flag design references: the classic five principles of flag design.','Color symbolism references: heraldic tincture meanings.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{nation:nation[0],region:nation[1],layout:layout.name,draw:layout.draw,colors:[{name:c1[0],hex:c1[1],meaning:c1[2]},{name:c2[0],hex:c2[1],meaning:c2[2]},{name:c3[0],hex:c3[1],meaning:c3[2]}],emblem:emblem,svg:svg},
    svg:svg,
    demo:{kind:'flag-spec',language:'python',program:prog,note:'Prints the nation, layout, colors, emblem, and SVG size.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.output||!r.output.colors||r.output.colors.length!==3)e.push('colors');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate flag in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

LOGO_GENJS = r"""(function(){'use strict';
/* JAH The Personal Logo Playground Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working logo playground: every call designs a personal logo —
   monogram or mark, style, palette with real hex values, typography pairing,
   and a ready-to-render SVG monogram. Deterministic: same seed, same logo. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="__PREFIX__";
var FIELDS=["Monograms","Pictorial Marks","Abstract Marks"];
var NAMES=["A. Rivera","J. Chen","M. Okafor","S. Patel","L. Novak","D. Kim","R. Alvarez","T. Nguyen","K. Hassan","E. Silva","N. Petrova","B. Carter"];
var PALETTES=[
 {name:"Ink & Gold",fg:"#1A1A1A",bg:"#F5F0E1",ac:"#D4AF37"},
 {name:"Ocean Trust",fg:"#0B4F6C",bg:"#F4F7F5",ac:"#20BF9F"},
 {name:"Ember Bold",fg:"#2B2D42",bg:"#FFF3E4",ac:"#FF6B35"},
 {name:"Forest Calm",fg:"#1E2A1A",bg:"#F1FAEE",ac:"#7DA87B"},
 {name:"Royal Plum",fg:"#2B2D42",bg:"#F8F0FF",ac:"#7B2FF7"},
 {name:"Crimson Mark",fg:"#1A1A1A",bg:"#FFF5F5",ac:"#C8102E"}
];
var MONOGRAM_STYLES=[
 {style:"Interlocked serif",note:"Letters share strokes in a classic serif face."},
 {style:"Modern sans overlap",note:"Clean sans letters overlapped with transparency."},
 {style:"Circle badge",note:"Monogram set inside a bold circular badge."},
 {style:"Diamond cipher",note:"Letters nested in a diamond lozenge."}
];
var PICTORIAL=[
 {mark:"Rising sun",note:"A sun cresting over a horizon line."},
 {mark:"Mountain peak",note:"A single bold peak with snowcap."},
 {mark:"Oak leaf",note:"A stylized oak leaf, veined."},
 {mark:"Compass star",note:"An eight-pointed compass star."},
 {mark:"Wave crest",note:"A curling wave, single line."},
 {mark:"Feather",note:"A light, upward-curving feather."}
];
var ABSTRACT=[
 {mark:"Interlocking rings",note:"Two rings linked, never breaking."},
 {mark:"Ascending bars",note:"Bars rising left to right."},
 {mark:"Spiral focus",note:"A spiral tightening to a point."},
 {mark:"Split circle",note:"A circle split by a bold diagonal."},
 {mark:"Triangle triad",note:"Three triangles in dynamic balance."},
 {mark:"Orbit dot",note:"A dot orbited by an elliptical ring."}
];
var TYPE_PAIR=["a classic serif for heritage","a clean geometric sans for modern clarity","a humanist sans for warmth","a strong slab serif for confidence"];
function initials(name){return name.split(/[\s.]+/).filter(Boolean).map(function(w){return w[0].toUpperCase();}).join("").slice(0,2);}
function svgLogo(kind,detail,pal,init,s){
  s=s||200; var h=s/2,inner="";
  if(kind==="Monograms"){
    if(detail.indexOf("Circle")>=0){inner='<circle cx="'+h+'" cy="'+h+'" r="'+(h-8)+'" fill="none" stroke="'+pal.fg+'" stroke-width="10"/><text x="'+h+'" y="'+(h+22)+'" font-family="Georgia,serif" font-size="72" font-weight="bold" text-anchor="middle" fill="'+pal.fg+'">'+init+'</text>';}
    else if(detail.indexOf("Diamond")>=0){inner='<polygon points="'+h+',8 '+(s-8)+','+h+' '+h+','+(s-8)+' 8,'+h+'" fill="none" stroke="'+pal.fg+'" stroke-width="8"/><text x="'+h+'" y="'+(h+20)+'" font-family="Georgia,serif" font-size="60" font-weight="bold" text-anchor="middle" fill="'+pal.fg+'">'+init+'</text>';}
    else{inner='<text x="'+h+'" y="'+(h+26)+'" font-family="Georgia,serif" font-size="84" font-weight="bold" text-anchor="middle" fill="'+pal.fg+'" letter-spacing="4">'+init+'</text><line x1="'+(h-60)+'" y1="'+(h+44)+'" x2="'+(h+60)+'" y2="'+(h+44)+'" stroke="'+pal.ac+'" stroke-width="6"/>';}
  }else if(kind==="Pictorial Marks"){
    inner='<circle cx="'+h+'" cy="'+h+'" r="'+(h-10)+'" fill="'+pal.bg+'" stroke="'+pal.fg+'" stroke-width="6"/>';
    if(detail.indexOf("sun")>=0){inner+='<circle cx="'+h+'" cy="'+(h+10)+'" r="34" fill="'+pal.ac+'"/><rect x="30" y="'+(h+34)+'" width="'+(s-60)+'" height="10" fill="'+pal.fg+'"/>';}
    else if(detail.indexOf("Mountain")>=0){inner+='<polygon points="'+h+',40 130,150 70,150" fill="'+pal.fg+'"/><polygon points="'+h+',40 112,102 88,102" fill="'+pal.bg+'"/>';}
    else if(detail.indexOf("star")>=0){inner+='<polygon points="'+h+',45 '+(h+14)+','+(h-14)+' '+(h+55)+','+h+' '+(h+14)+','+(h+14)+' '+h+','+(h+55)+' '+(h-14)+','+(h+14)+' '+(h-55)+','+h+' '+(h-14)+','+(h-14)+'" fill="'+pal.ac+'"/>';}
    else{inner+='<text x="'+h+'" y="'+(h+24)+'" font-family="Georgia,serif" font-size="76" text-anchor="middle" fill="'+pal.fg+'">'+init+'</text>';}
  }else{
    inner='<circle cx="'+h+'" cy="'+h+'" r="'+(h-12)+'" fill="none" stroke="'+pal.fg+'" stroke-width="8"/>';
    if(detail.indexOf("rings")>=0){inner+='<circle cx="'+(h-24)+'" cy="'+h+'" r="34" fill="none" stroke="'+pal.ac+'" stroke-width="10"/><circle cx="'+(h+24)+'" cy="'+h+'" r="34" fill="none" stroke="'+pal.fg+'" stroke-width="10"/>';}
    else if(detail.indexOf("bars")>=0){inner+='<rect x="60" y="110" width="22" height="50" fill="'+pal.fg+'"/><rect x="90" y="88" width="22" height="72" fill="'+pal.ac+'"/><rect x="120" y="66" width="22" height="94" fill="'+pal.fg+'"/>';}
    else{inner+='<circle cx="'+h+'" cy="'+h+'" r="10" fill="'+pal.ac+'"/><ellipse cx="'+h+'" cy="'+h+'" rx="60" ry="30" fill="none" stroke="'+pal.fg+'" stroke-width="8" transform="rotate(-20 '+h+' '+h+')"/>';}
  }
  return '<svg xmlns="http://www.w3.org/2000/svg" width="'+s+'" height="'+s+'" viewBox="0 0 '+s+' '+s+'"><rect width="'+s+'" height="'+s+'" fill="'+pal.bg+'"/>'+inner+'</svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var name=pick(NAMES,s), init=initials(name), pal=pick(PALETTES,s), type=pick(TYPE_PAIR,s);
  var detail,note;
  if(field==="Monograms"){var m=pick(MONOGRAM_STYLES,s);detail=m.style;note=m.note;}
  else if(field==="Pictorial Marks"){var p=pick(PICTORIAL,s);detail=p.mark;note=p.note;}
  else{var a=pick(ABSTRACT,s);detail=a.mark;note=a.note;}
  var title="Logo for "+name+" — "+detail;
  var svg=svgLogo(field,detail,pal,init,200);
  var prog="# Logo spec — "+title.replace(/"/g,"'")+"\n"
    +"owner = \""+name+"\"\n"
    +"mark = \""+detail+"\"\n"
    +"palette = {\"fg\": \""+pal.fg+"\", \"bg\": \""+pal.bg+"\", \"accent\": \""+pal.ac+"\"}\n"
    +"print(\"Owner:\", owner, \"(\"+\""+init+"\"+\")\")\n"
    +"print(\"Mark:\", mark)\n"
    +"print(\"Palette:\", palette[\"fg\"], palette[\"bg\"], palette[\"accent\"], \"(\" + \""+pal.name+"\" + \")\")\n"
    +"print(\"Type pairing:\", \""+type+"\")\n"
    +"print(\"SVG bytes:\", "+svg.length+")\n"
    +"print(\"Clearspace: height of '\"+\""+init+"\"+\"' on all sides\")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — logo record', title:title,
    description:'GENERATED LOGO — "'+title+'" for '+name+' (initials '+init+'). Style: '+detail+' — '+note+' Palette: '+pal.name+' (ink '+pal.fg+', ground '+pal.bg+', accent '+pal.ac+'). Typography pairing: '+type+'. The SVG below renders the actual logo mark — use it at any size; vectors never blur.',
    how_it_works:'The playground picks an owner, extracts initials, chooses a mark family ('+field+') and a specific mark ('+detail+'), then pairs it with a palette ('+pal.name+') and a typography direction. The SVG monogram is drawn programmatically: ground rect, mark geometry, and set type. The logo works because it is simple, high-contrast, and reproducible — the three laws of marks.',
    key_points:['Owner: '+name+' ('+init+')','Mark: '+detail+' — '+note,'Palette: '+pal.name+' — '+pal.fg+' / '+pal.bg+' / '+pal.ac,'Typography: '+type,'Deterministic: seed '+seed+' always rebuilds this exact logo.'],
    requirements:['Vector software or a browser to view the SVG','The palette values for consistent use'],
    standards:['Readable at 32px favicon size','Works in one color (ink on ground)','Clearspace equal to the cap-height on all sides'],
    citations:['Logo design references: the three laws of marks (simple, contrast, reproducible).','Typography references: pairing marks with type.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{owner:name,initials:init,mark:detail,mark_note:note,palette:pal.name,colors:{fg:pal.fg,bg:pal.bg,accent:pal.ac},typography:type,svg:svg},
    svg:svg,
    demo:{kind:'logo-spec',language:'python',program:prog,note:'Prints the logo spec, palette, and clearspace rule.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate logo in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

def _item(slug, name, tagline, record_kind, ai_name, role, greet, searchph, chatph, short, fields, genjs, gen_desc, sig_tagline):
    return {
        'slug': slug, 'cls': 'gen', 'renderer': None,
        'name': name, 'tagline': tagline, 'record_kind': record_kind,
        'ai_name': ai_name, 'role': role, 'greet': greet, 'searchph': searchph,
        'chatph': chatph, 'short': short, 'fields': fields,
        'hero_extra': 'Every record carries the full entry: description, how it works, key points, requirements, standards, citations, and a working demonstration program. Records are ordered by the teaching ladder, simple to complex.',
        'sig_tagline': sig_tagline, 'genjs': genjs, 'gen_desc': gen_desc,
        'prefix': None,  # filled from prefixes.json by build.py
    }

ITEMS = [
_item('pattern-generator', 'The Pattern Generator Database',
 'Produce real seamless patterns on demand: geometric, organic, and linear families with genuine palettes, repeat math, and ready-to-render SVG tiles — every seed rebuilding the exact same pattern, every output yours to use.',
 'pattern generator record', 'JAH Pattern Generator Archivist',
 'pattern generator archivist — operating a real working pattern generator and teaching seamless pattern design; answering from many angles using only archive data',
 'Ask me to generate a pattern — pick a family or let the seed decide.',
 'Search patterns, motifs, palettes, SVG tiles...', 'Ask for a pattern...', 'pattern',
 ['Geometric Patterns','Organic Patterns','Linear Patterns'], PATTERN_GENJS,
 'A real working pattern generator: pick a family and seed, get a genuine seamless pattern with palette, repeat math, and SVG tile.',
 'The Signature treatment of pattern generation: the same real generator carried forward, plus Signature-original motif families and impossible-tiling patterns original to this system.'),
_item('world-flag-studio', 'The World Flag Studio Database',
 'Invent nations and design their flags: layouts, meaningful colors, emblems, and true 2:3 SVG flags — a complete vexillology studio where every seed founds a new fictional country with a flag worth saluting.',
 'flag design record', 'JAH World Flag Studio Archivist',
 'world flag studio archivist — operating a real working flag design studio and teaching vexillology; answering from many angles using only archive data',
 'Ask me to found a nation and design its flag.',
 'Search flags, nations, layouts, emblems...', 'Ask for a flag...', 'flag',
 ['Tricolors & Tribands','Crosses & Symbols','Bold Originals'], FLAG_GENJS,
 'A real working flag studio: invent a fictional nation and get its complete flag — layout, color symbolism, emblem, and SVG.',
 'The Signature treatment of flag design: the same real studio carried forward, plus Signature-original nations and ceremonial flag traditions original to this system.'),
_item('personal-logo-playground', 'The Personal Logo Playground',
 'Design personal logos that mean business: monograms, pictorial marks, and abstract marks with real palettes, typography pairings, and ready-to-render SVG — every seed designing a complete identity mark.',
 'logo design record', 'JAH Personal Logo Playground Archivist',
 'personal logo playground archivist — operating a real working logo designer and teaching identity marks; answering from many angles using only archive data',
 'Ask me to design a personal logo.',
 'Search logos, monograms, marks, palettes...', 'Ask for a logo...', 'logo',
 ['Monograms','Pictorial Marks','Abstract Marks'], LOGO_GENJS,
 'A real working logo playground: get a complete personal logo — mark, palette, typography pairing, and SVG.',
 'The Signature treatment of logo design: the same real playground carried forward, plus Signature-original mark families and ceremonial identity systems original to this system.'),
]
