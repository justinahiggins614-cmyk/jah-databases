(function(){'use strict';
/* JAH The Outfit Generator Database generator — jahdb-outfit-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working outfit generator: every call assembles a complete head-to-toe
   outfit — top, bottom, shoes, outerwear, two accessories, a coordinated color
   palette with hex codes, occasion and weather notes, and a flat-lay SVG that
   renders each garment as a labeled swatch card. Deterministic per seed:
   same seed, same outfit, ready to wear. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-OTGN-";
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
var gen={version:'jahdb-outfit-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('outfit-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();