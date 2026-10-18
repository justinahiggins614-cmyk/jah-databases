(function(){'use strict';
/* JAH The World Flag Studio Database generator — jahdb-world-flag-studio-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working flag studio: every call invents a fictional nation and
   designs its flag — layout, real hex colors with symbolism, emblem, and a
   ready-to-render SVG. Deterministic: same seed, same flag. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WFLGS-";
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
var gen={version:'jahdb-world-flag-studio-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('world-flag-studio-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
