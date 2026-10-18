(function(){'use strict';
/* JAH The Personal Photo Shoot Database generator — jahdb-personal-photo-shoot-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working photo-shoot planner: every call plans a complete session —
   session title, lane, location, three styled outfits, five directed poses,
   lighting plan, and a six-shot shot list — plus a storyboard SVG.
   Deterministic per seed: same seed, same shoot. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-PPSTS-";
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
var gen={version:'jahdb-personal-photo-shoot-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-photo-shoot-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();