(function(){'use strict';
/* JAH The Personal Logo Playground Database generator — jahdb-personal-logo-playground-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working logo playground: every call designs a personal logo —
   monogram or mark, style, palette with real hex values, typography pairing,
   and a ready-to-render SVG monogram. Deterministic: same seed, same logo. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PLGO-";
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
var gen={version:'jahdb-personal-logo-playground-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-logo-playground',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
