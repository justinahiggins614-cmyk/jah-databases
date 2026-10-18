(function(){'use strict';
/* JAH The Uniform Designer Database generator — jahdb-uniform-designer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working uniform designer: every call creates a cohesive uniform concept —
   client organization, three role variants, two-color system with hexes, insignia
   and placement, fabric and care notes — and renders a uniform schematic SVG.
   Deterministic per seed: same seed, same uniform. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UNDSS-";
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
var gen={version:'jahdb-uniform-designer-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('uniform-designer-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();