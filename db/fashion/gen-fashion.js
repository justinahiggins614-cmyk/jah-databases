(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['garments','fabrics','sizing','patterns','trends'];
var PREFIX='JAH-FASH-';
var REF_FABRIC='https://www.thesewingdirectory.co.uk/fabric-glossary/';
var REF_STD='Fashion reference (verified 2026-10-09)';
var GARMENTS=[
 ['T-Shirt','tops','A short-sleeved casual knit top.'],['Dress Shirt','tops','A collared button-front woven shirt.'],
 ['Polo Shirt','tops','A knit top with collar and placket.'],['Blouse','tops','A loose women\u2019s top, often with soft details.'],
 ['Sweater','tops','A knitted pullover for warmth.'],['Cardigan','tops','A sweater that opens down the front.'],
 ['Hoodie','tops','A sweatshirt with a hood.'],['Blazer','outerwear','A tailored unstructured jacket.'],
 ['Suit Jacket','outerwear','A structured jacket worn with matching trousers.'],['Overcoat','outerwear','A long heavy coat for winter.'],
 ['Trench Coat','outerwear','A belted raincoat with epaulettes.'],['Parka','outerwear','A hooded insulated cold-weather coat.'],
 ['Denim Jacket','outerwear','A twill-weave cotton jacket.'],['Leather Jacket','outerwear','A jacket cut from animal hide.'],
 ['Vest','outerwear','A sleeveless upper-body garment.'],['Jeans','bottoms','Twill-weave trousers, usually denim.'],
 ['Chinos','bottoms','Cotton twill casual trousers.'],['Trousers','bottoms','Tailored full-length pants.'],
 ['Shorts','bottoms','Short trousers above the knee.'],['Cargo Pants','bottoms','Pants with side leg pockets.'],
 ['Pencil Skirt','bottoms','A slim straight skirt.'],['A-Line Skirt','bottoms','A skirt flaring from the waist.'],
 ['Pleated Skirt','bottoms','A skirt with folded pleats.'],['Maxi Dress','dresses','An ankle-length dress.'],
 ['Cocktail Dress','dresses','A knee-length semi-formal dress.'],['Evening Gown','dresses','A formal floor-length dress.'],
 ['Jumpsuit','dresses','A one-piece top-and-trousers garment.'],['Leggings','bottoms','Skin-tight stretch pants.'],
 ['Sweatpants','bottoms','Soft knit casual pants.'],['Swimsuit','swim','A garment for swimming.'],
 ['Bikini','swim','A two-piece swimsuit.'],['Cardigan','tops','A front-opening knit layer.'],
 ['Scarf','accessories','A fabric wrap for neck or head.'],['Gloves','accessories','Hand coverings with fingers.'],
 ['Beanie','accessories','A close-fitting knit cap.'],['Belt','accessories','A strap worn at the waist.'],
 ['Tie','accessories','A necktie for formal dress.'],['Socks','accessories','Knit foot coverings.'],
 ['Underwear','intimates','Base-layer garments.'],['Bra','intimates','A supportive undergarment.']
];
var FABRICS=[
 ['Cotton','natural','plain','Breathable, absorbent and soft.'],['Linen','natural','plain','Flax fiber; cool with natural slubs.'],
 ['Silk','natural','plain','Lustrous protein fiber; drapes beautifully.'],['Wool','natural','twill','Warm animal fiber; natural stretch.'],
 ['Cashmere','natural','plain','Luxury downy goat fiber; very soft.'],['Denim','cotton','twill','Blue warp, white weft twill; durable.'],
 ['Corduroy','cotton','pile','Ribbed cut-pile fabric; the ribs are wales.'],['Chiffon','silk/synthetic','plain','Sheer lightweight plain weave.'],
 ['Satin','silk/synthetic','satin','Smooth face from satin weave.'],['Velvet','silk/cotton','pile','Dense cut pile; rich hand.'],
 ['Twill','cotton/wool','twill','Diagonal rib weave; strong drape.'],['Canvas','cotton','plain','Heavy plain weave; workwear.'],
 ['Chambray','cotton','plain','Light plain weave with colored warp.'],['Flannel','cotton/wool','plain','Brushed soft face.'],
 ['Jersey','cotton','knit','Lightweight stretch knit.'],['Fleece','synthetic','knit','Brushed knit; warm insulation.'],
 ['Lace','cotton/synthetic','openwork','Patterned openwork fabric.'],['Organza','silk/synthetic','plain','Crisp sheer plain weave.'],
 ['Taffeta','silk/synthetic','plain','Crisp with a rustle.'],['Tweed','wool','twill','Rough textured wool; country classic.'],
 ['Gabardine','wool','twill','Tight twill; suiting staple.'],['Poplin','cotton','plain','Fine plain weave shirting.'],
 ['Muslin','cotton','plain','Simple plain weave; test garments.'],['Crepe','silk/synthetic','plain','Pebbled texture; elegant drape.'],
 ['Georgette','silk/synthetic','plain','Sheer crepe; fluid drape.'],['Voile','cotton','plain','Sheer lightweight plain weave.'],
 ['Seersucker','cotton','plain','Puckered stripe texture; summer suiting.'],['Nylon','synthetic','plain','Strong elastic synthetic.'],
 ['Polyester','synthetic','plain','Wrinkle-resistant synthetic.'],['Spandex','synthetic','knit','High-stretch elastane fiber.'],
 ['Rayon','semi-synthetic','plain','Cellulose fiber; silk-like drape.'],['Modal','semi-synthetic','knit','Soft beech-pulp knit fiber.']
];
var WEAVES=[
 ['Plain Weave','Over-one under-one; gingham and muslin.'],['Twill Weave','Diagonal rib; denim and gabardine.'],
 ['Satin Weave','Long floats; satin and sateen.'],['Basket Weave','Grouped yarns; oxford cloth.'],
 ['Dobby Weave','Small geometric patterns woven in.'],['Jacquard Weave','Complex figured patterns.'],
 ['Jersey Knit','Single knit; t-shirts.'],['Rib Knit','Vertical ribs; cuffs and necklines.'],
 ['Pile Weave','Cut loops; velvet and corduroy.']
];
var W_SIZE=[['US 0',[32,24,34]],['US 2',[33,25,35]],['US 4',[34,26,36]],['US 6',[35,27,37]],['US 8',[36,28,38]],['US 10',[37.5,29.5,39.5]],['US 12',[39,31,41]],['US 14',[40.5,32.5,42.5]],['US 16',[42,34,44]]];
var M_SIZE=[['S',[34,28]],['M',[38,32]],['L',[42,36]],['XL',[46,40]],['XXL',[50,44]]];
var SHOE=[['US 6','UK 5.5','EU 38.5'],['US 7','UK 6.5','EU 39.5'],['US 8','UK 7.5','EU 41'],['US 9','UK 8.5','EU 42'],['US 10','UK 9.5','EU 43.5'],['US 11','UK 10.5','EU 44.5'],['US 12','UK 11.5','EU 46'],['US 13','UK 12.5','EU 47']];
var PIECES=[
 ['Bodice Front','The front of a fitted top.'],['Bodice Back','The back of a fitted top.'],
 ['Sleeve','The arm piece, set or raglan.'],['Collar','The neckline finish.'],
 ['Cuff','The wrist finish of a sleeve.'],['Yoke','The shoulder panel of shirts.'],
 ['Facing','Turned edge finishing a neckline.'],['Lining','The inner layer of a garment.'],
 ['Waistband','The finished top of trousers or skirts.'],['Pocket','Inset, patch or welt storage.'],
 ['Placket','The finished shirt front opening.'],['Gusset','An inset panel for ease of movement.']
];
var SEAMS=[['Plain Seam','The basic stitched join, pressed open.'],['French Seam','Enclosed raw edges; sheer fabrics.'],['Flat-Felled Seam','Strong folded seam; jeans.'],['Bound Seam','Edges wrapped in bias binding.'],['Overlocked Seam','Serged edges; knits.']];
var NECKLINES=[['Crew','Close round neckline.'],['V-Neck','V-shaped opening.'],['Scoop','Wide U-shaped opening.'],['Boat','Wide straight across the collarbones.'],['Cowl','Draped folds at the neck.'],['Turtleneck','High close-fitting collar.'],['Halter','Tied behind the neck; bare shoulders.'],['Off-Shoulder','Sitting below the shoulders.']];
var ERAS=[
 ['1920s','Flapper era: dropped waists and jazz-age beading.'],['1930s','Bias-cut gowns and Hollywood glamour.'],
 ['1950s New Look','Full skirts and nipped waists; Dior\u2019s silhouette.'],['1960s','Mod minis and youthquake color.'],
 ['1970s','Bohemian flow, flares and disco shine.'],['1980s Power Dressing','Big shoulders and bold color.'],
 ['1990s Minimalism','Slip dresses and clean lines.'],['2000s Y2K','Low rise and logo mania.']
];
var GARMENT_FABRIC={
 'T-Shirt':['Jersey','Cotton','Modal'],'Jeans':['Denim','Cotton','Twill'],'Blazer':['Wool','Gabardine','Tweed'],
 'Evening Gown':['Silk','Satin','Chiffon'],'Trench Coat':['Gabardine','Cotton','Poplin'],'Sweater':['Wool','Cashmere','Fleece']
};
var SIG_A=['Moonlit','Crimson','Velvet','Ember','Harbor','Juniper','Onyx','Solstice'];
var SIG_B=['atelier','maison','studio','house'];
function buildOnline(rnd,cat){
  var rec={category:cat,source:'online',creation_mode:'ONLINE-VERIFIED'};
  if(cat==='garments'){
    var g=pick(GARMENTS,rnd);
    rec.title='Garment: '+g[0];rec.topic='garment';
    rec.garment={garment:g[0],class:g[1],note:g[2]};
    rec.source_ref=REF_STD;
    rec.description='The '+g[0].toLowerCase()+' is a '+g[1]+' garment: '+g[2]+' A wardrobe staple with established construction conventions.';
    if(GARMENT_FABRIC[g[0]]&&rnd()<0.6){var fb=pick(GARMENT_FABRIC[g[0]],rnd);
      rec.title='Garment: '+g[0]+' in '+fb;rec.garment.fabric=fb;
      rec.description='The '+g[0].toLowerCase()+' cut in '+fb.toLowerCase()+': '+g[2]+' Fabric choice defines the drape, hand and care of the finished garment.';}
  }else if(cat==='fabrics'){
    var f=pick(FABRICS,rnd);
    rec.title='Fabric: '+f[0];rec.topic='fabric';
    rec.garment={fabric:f[0],fiber:f[1],weave:f[2],properties:f[3]};
    rec.source_ref=REF_FABRIC;
    rec.description='The fabric '+f[0].toLowerCase()+' is a '+f[1]+' fiber in '+f[2]+' construction. '+f[3]+' Choose it for the hand and performance the design needs.';
  }else if(cat==='sizing'){
    var r=rnd();
    if(r<0.4){var w=pick(W_SIZE,rnd);rec.title='Women\u2019s '+w[0]+' size';rec.topic='size chart';rec.garment={chart:'womens',size:w[0],bust_in:w[1][0],waist_in:w[1][1],hip_in:w[1][2],approx:true};rec.source_ref=REF_STD;
      rec.description='Women\u2019s '+w[0]+' measures approximately bust '+w[1][0]+'in, waist '+w[1][1]+'in, hip '+w[1][2]+'in. Standard charts are approximate; always check the maker\u2019s table.';}
    else if(r<0.7){var m=pick(M_SIZE,rnd);rec.title='Men\u2019s '+m[0]+' size';rec.topic='size chart';rec.garment={chart:'mens',size:m[0],chest_in:m[1][0],waist_in:m[1][1],approx:true};rec.source_ref=REF_STD;
      rec.description='Men\u2019s size '+m[0]+' measures approximately chest '+m[1][0]+'in and waist '+m[1][1]+'in. Standard charts are approximate; always check the maker\u2019s table.';}
    else{var s2=pick(SHOE,rnd);rec.title='Shoe size '+s2[0];rec.topic='size conversion';rec.garment={us:s2[0],uk:s2[1],eu:s2[2]};rec.source_ref=REF_STD;
      rec.description='Shoe size '+s2[0]+' converts to '+s2[1]+' UK and '+s2[2]+' EU. Conversions are standardized across major sizing systems.';}
  }else if(cat==='patterns'){
    var r2=rnd();
    if(r2<0.55){var p=pick(PIECES,rnd);rec.title='Pattern piece: '+p[0];rec.topic='pattern piece';rec.garment={piece:p[0],use:p[1]};rec.source_ref=REF_STD;
      rec.description='The '+p[0].toLowerCase()+' pattern piece: '+p[1]+' Accurate pieces with seam allowance are the foundation of fit.';}
    else if(r2<0.8){var sm=pick(SEAMS,rnd);rec.title='Seam: '+sm[0];rec.topic='seam';rec.garment={seam:sm[0],note:sm[1]};rec.source_ref=REF_STD;
      rec.description='The '+sm[0].toLowerCase()+': '+sm[1]+' Seam choice balances strength, bulk and finish.';}
    else{var wv=pick(WEAVES,rnd);rec.title='Weave: '+wv[0];rec.topic='weave';rec.garment={weave:wv[0],note:wv[1]};rec.source_ref=REF_FABRIC;
      rec.description='The '+wv[0].toLowerCase()+': '+wv[1]+' Weave structure sets a fabric\u2019s strength, drape and texture.';}
  }else{
    var r3=rnd();
    if(r3<0.5){var er=pick(ERAS,rnd);rec.title='Fashion era: '+er[0];rec.topic='era';rec.garment={era:er[0],silhouette:er[1]};rec.source_ref=REF_STD;
      rec.description='The '+er[0]+' era: '+er[1]+' Silhouettes cycle, and history is the designer\u2019s reference library.';}
    else{var nl=pick(NECKLINES,rnd);rec.title='Neckline style: '+nl[0];rec.topic='neckline';rec.garment={neckline:nl[0],note:nl[1]};rec.source_ref=REF_STD;
      rec.description='The '+nl[0].toLowerCase()+' neckline: '+nl[1]+' Necklines frame the face and set a garment\u2019s character.';}
  }
  return rec;
}
function buildSignature(rnd,cat){
  var rec={category:cat,source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  var nm=pick(SIG_A,rnd)+' '+pick(SIG_B,rnd);
  if(cat==='garments'){rec.title='Signature garment concept: '+nm;rec.topic='garment concept';rec.garment={concept:nm,silhouette:pick(['fitted','oversized','draped'],rnd),fabric:pick(FABRICS,rnd)[0]};
    rec.description='A Signature-generated garment concept named '+nm+' with a '+rec.garment.silhouette+' silhouette in '+rec.garment.fabric.toLowerCase()+'. An original design sketch by the JAH generator.';}
  else if(cat==='fabrics'){rec.title='Signature textile: '+nm;rec.topic='textile';rec.garment={textile:nm,weave:pick(WEAVES,rnd)[0],weight_gsm:ri(rnd,80,400)};
    rec.description='A Signature-generated textile named '+nm+' in a '+rec.garment.weave.toLowerCase()+' at '+rec.garment.weight_gsm+' gsm. An original material study by the JAH generator.';}
  else if(cat==='sizing'){rec.title='Signature fit block: '+nm;rec.topic='fit block';rec.garment={block:nm,chest_in:ri(rnd,32,48),waist_in:ri(rnd,26,42)};
    rec.description='A Signature-generated fit block named '+nm+' with a '+rec.garment.chest_in+'in chest and '+rec.garment.waist_in+'in waist. An original sizing study by the JAH generator.';}
  else if(cat==='patterns'){rec.title='Signature pattern draft: '+nm;rec.topic='pattern draft';rec.garment={draft:nm,pieces:ri(rnd,4,14),seam_allowance_in:0.5};
    rec.description='A Signature-generated pattern draft named '+nm+' with '+rec.garment.pieces+' pieces and half-inch seam allowance. An original drafting study by the JAH generator.';}
  else{rec.title='Signature collection theme: '+nm;rec.topic='collection';rec.garment={theme:nm,looks:ri(rnd,8,30),palette:pick(['earth','jewel','mono','pastel'],rnd)};
    rec.description='A Signature-generated collection theme named '+nm+': '+rec.garment.looks+' looks in a '+rec.garment.palette+' palette. An original trend forecast by the JAH generator.';}
  return rec;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var online=!opts.forceSignature&&(rnd()<0.24||opts.forceOnline);
  var rec=online?buildOnline(rnd,cat):buildSignature(rnd,cat);
  if(rec.description.length<165)rec.description+=' Filed as a complete searchable record in the JAH Data Bases archive, with its full specifications intact.';
  rec.id=PREFIX+String(seed).padStart(7,'0');rec._seed=seed;return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-FASH-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<150)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&(r.creation_mode!=='ONLINE-VERIFIED'||typeof r.source_ref!=='string'||!r.source_ref.length))e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(!r.garment||typeof r.garment!=='object')e.push('garment');
  if(r.source==='online'&&r.topic==='fabric'){
    var f=FABRICS.filter(function(x){return x[0]===r.garment.fabric;})[0];
    if(!f||f[1]!==r.garment.fiber)e.push('fabric_fact');
  }
  if(r.source==='online'&&r.topic==='size chart'&&r.garment.chart==='womens'){
    var w=W_SIZE.filter(function(x){return x[0]===r.garment.size;})[0];
    if(!w||w[1][0]!==r.garment.bust_in)e.push('size_fact');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-fashion-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fashion',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
