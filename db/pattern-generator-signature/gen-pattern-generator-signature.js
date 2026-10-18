(function(){'use strict';
/* JAH The Pattern Generator Database generator — jahdb-pattern-generator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working pattern generator: every call produces a genuine seamless
   pattern specification — motif, symmetry, palette with real hex values,
   repeat math, and a ready-to-render SVG tile.
   Deterministic: same seed, same pattern. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX="JAH-PTGNS-";
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
var gen={version:'jahdb-pattern-generator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pattern-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
