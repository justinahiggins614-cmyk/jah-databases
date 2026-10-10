(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var CATS=['composition','color','scenes','viewpoints','attributes'];
var PREFIX='JAH-VIS-';
var HEX=/^#[0-9a-fA-F]{6}$/;

/* Original Signature visual concepts: scene descriptions with composition
   parameters — generated artwork briefs, never presented as real photographs. */
var T=[
{cat:'scenes',scene:'A lighthouse on a rocky headland at golden hour, waves breaking below, gulls in the distance.',
 comp:['Rule of thirds','Lighthouse on the right vertical third; horizon on the lower third.'],
 pal:[['amber','#FF9E4F','key light'],['dusk blue','#2E4A62','sky'],['warm sand','#F5D9A0','highlights'],['deep shadow','#1A2B3C','shadows'],['burnt orange','#C96F2E','accents']],
 light:'Golden-hour sunlight, warm key from the west, cool ambient fill.',view:'Eye level from the cliff path.',mood:'Serene and timeless.',
 par:{aspect_ratio:'16:9',depth_of_field:'deep',focal_length:'35mm',detail_level:'high'}},
{cat:'color',scene:'A rain-slicked cyberpunk alley at night, neon signs reflecting in puddles, a lone figure with an umbrella.',
 comp:['Framing','Overhead wires and sign brackets frame the alley; figure centered in the gap.'],
 pal:[['neon magenta','#FF2E88','signs'],['electric cyan','#00E5FF','reflections'],['wet asphalt','#1B1E26','ground'],['acid yellow','#F5E900','accents'],['deep violet','#2A0A4A','shadows']],
 light:'Practical neon sources only; cyan rim on the figure, magenta wash on walls.',view:'Eye level, slight low angle up the alley.',mood:'Electric and lonely.',
 par:{aspect_ratio:'2.39:1',depth_of_field:'medium',focal_length:'50mm',detail_level:'high'}},
{cat:'composition',scene:'A misty forest path winding between tall pines, light shafts cutting through fog.',
 comp:['Leading lines','The path leads from the lower-left corner to a bright clearing.'],
 pal:[['fog white','#E8ECEF','atmosphere'],['pine green','#2D4A35','trees'],['moss','#6B8E5A','undergrowth'],['bark brown','#4A3728','trunks'],['pale gold','#D9C58A','light shafts']],
 light:'Diffused overcast with volumetric shafts; low contrast, soft shadows.',view:'Eye level on the path, centered.',mood:'Quiet and mysterious.',
 par:{aspect_ratio:'3:2',depth_of_field:'medium',focal_length:'35mm',detail_level:'medium'}},
{cat:'composition',scene:'Vast desert dunes under a clear sky, a single distant caravan silhouette.',
 comp:['Negative space','Dunes fill the lower fifth; empty sky dominates to emphasize scale.'],
 pal:[['sand','#E3C188','dunes'],['sky blue','#7FB2D9','sky'],['shadow mauve','#8A6F7D','dune shadows'],['sun white','#FFF8E7','highlights']],
 light:'Harsh midday sun; strong short shadows defining dune curves.',view:'Slightly elevated, wide.',mood:'Vast and humbling.',
 par:{aspect_ratio:'21:9',depth_of_field:'deep',focal_length:'24mm',detail_level:'medium'}},
{cat:'attributes',scene:'A portrait of an elderly craftswoman, half her face in deep shadow, hands weathered.',
 comp:['Chiaroscuro','Face split by dramatic side light; background falls to black.'],
 pal:[['skin warm','#C98A5E','key side'],['umber shadow','#3A2418','shadow side'],['linen','#D8CFC0','clothing'],['black','#0D0B09','background']],
 light:'Single hard key at 90 degrees, minimal fill; Rembrandt-style triangle under the eye.',view:'Eye level, close.',mood:'Grave and dignified.',
 par:{aspect_ratio:'4:5',depth_of_field:'shallow',focal_length:'85mm',detail_level:'ultra'}},
{cat:'composition',scene:'A still mountain lake at dawn mirroring snow peaks perfectly.',
 comp:['Symmetry','Horizon dead center; the reflection completes the mirror.'],
 pal:[['dawn pink','#F2B8C6','sky'],['glacier blue','#A8C8D8','peaks'],['pine dark','#22382B','treeline'],['mist white','#F4F6F7','water']],
 light:'Pre-sunrise alpenglow; soft, directionless, pastel.',view:'Low, near water level.',mood:'Perfect stillness.',
 par:{aspect_ratio:'16:9',depth_of_field:'deep',focal_length:'24mm',detail_level:'high'}},
{cat:'color',scene:'An autumn forest path carpeted in red and gold leaves, low sun flaring through branches.',
 comp:['Color dominance','Warm analogous palette fills the frame; a cool shadow path cuts through.'],
 pal:[['crimson','#B33A2B','leaves'],['gold','#E0A030','canopy'],['rust','#8A4A1F','bark'],['cool shadow','#4A5A6A','path'],['sun flare','#FFE9B0','accents']],
 light:'Low backlit sun; flare and long shadows.',view:'Eye level down the path.',mood:'Nostalgic and warm.',
 par:{aspect_ratio:'3:2',depth_of_field:'medium',focal_length:'35mm',detail_level:'high'}},
{cat:'scenes',scene:'A small wooden cabin in deep snow at night, warm windows glowing, aurora overhead.',
 comp:['Contrast of warm/cool','Tiny warm cabin against vast cold night; aurora arcs across the top third.'],
 pal:[['aurora green','#4AE3B5','sky'],['night blue','#101B33','night'],['window gold','#FFC45E','cabin'],['snow blue','#C9D8E8','snow'],['wood brown','#5A3D28','cabin']],
 light:'Moonlight plus window glow; aurora as ambient color wash.',view:'Eye level from a snowy rise.',mood:'Cozy against the infinite.',
 par:{aspect_ratio:'16:9',depth_of_field:'deep',focal_length:'24mm',detail_level:'high'}},
{cat:'scenes',scene:'A coral reef canyon with a sea turtle gliding overhead, sun rays piercing blue water.',
 comp:['Depth layers','Foreground coral, midground turtle, background blue gradient.'],
 pal:[['ocean blue','#0E5A7D','water'],['coral orange','#FF7A4D','reef'],['turtle green','#4A7D5A','turtle'],['sand light','#E8D9B0','seabed'],['ray white','#DFF2F8','light shafts']],
 light:'Filtered sunlight from above; caustic patterns on the sand.',view:'Slightly below the turtle, looking up.',mood:'Weightless wonder.',
 par:{aspect_ratio:'16:9',depth_of_field:'medium',focal_length:'28mm',detail_level:'high'}},
{cat:'viewpoints',scene:'Colorful hot-air balloons drifting over a green valley at sunrise, seen from above.',
 comp:['Aerial pattern','Balloons scattered as color dots over the patchwork valley.'],
 pal:[['balloon red','#D94A4A','balloons'],['balloon yellow','#F2C14E','balloons'],['valley green','#5A8A4A','fields'],['morning mist','#E8E4D8','valley'],['sky peach','#F7C8A0','sky']],
 light:'Low sunrise; long balloon shadows on the fields.',view:'High aerial, top-down tilt.',mood:'Joyful and free.',
 par:{aspect_ratio:'16:9',depth_of_field:'deep',focal_length:'35mm',detail_level:'high'}},
{cat:'color',scene:'A rainy city street at night, reflections of traffic lights smearing across wet pavement.',
 comp:['Reflections as subject','The reflection occupies more frame than the source lights.'],
 pal:[['signal red','#E33A2E','reflections'],['taxi yellow','#F7B500','reflections'],['wet black','#14161C','pavement'],['neon white','#F2F5F7','headlights'],['teal','#1E7A8A','accents']],
 light:'Mixed practicals; glossy reflections double every source.',view:'Low angle near the pavement.',mood:'Melancholy neon.',
 par:{aspect_ratio:'2.39:1',depth_of_field:'shallow',focal_length:'50mm',detail_level:'high'}},
{cat:'scenes',scene:'An ancient stone temple courtyard at dawn, incense smoke curling, monks crossing.',
 comp:['Framing through architecture','Courtyard seen through a carved stone doorway.'],
 pal:[['stone gray','#8A8578','temple'],['saffron','#E8930C','robes'],['smoke white','#EDEAE2','incense'],['dawn gold','#F2C879','light'],['deep teal','#1F4A4A','shadows']],
 light:'Dawn raking light across carved stone; smoke backlit.',view:'Eye level through the doorway.',mood:'Sacred calm.',
 par:{aspect_ratio:'4:3',depth_of_field:'medium',focal_length:'35mm',detail_level:'ultra'}},
{cat:'viewpoints',scene:'Extreme macro of a dewdrop on a petal, the garden refracted inside the drop.',
 comp:['World in a drop','The refracted garden fills the drop; petal texture as landscape.'],
 pal:[['petal pink','#F2A7C3','petal'],['dew white','#F7FBFD','drop'],['leaf green','#3E7D44','refraction'],['sky blue','#A8D0E8','refraction']],
 light:'Soft morning backlight; the drop glows.',view:'Macro, nearly touching.',mood:'Delicate revelation.',
 par:{aspect_ratio:'1:1',depth_of_field:'ultra-shallow',focal_length:'100mm macro',detail_level:'ultra'}},
{cat:'scenes',scene:'Storm waves smashing against black sea cliffs, spray exploding upward.',
 comp:['Diagonal energy','Cliff diagonal from lower-left; wave crest frozen mid-crash.'],
 pal:[['storm gray','#5A6672','sky'],['foam white','#F4F7F8','spray'],['cliff black','#1E2226','cliffs'],['sea green','#2E6B5E','water']],
 light:'Storm-diffused; spray backlit by a break in cloud.',view:'Elevated on the cliff edge.',mood:'Raw power.',
 par:{aspect_ratio:'3:2',depth_of_field:'medium',focal_length:'70mm',detail_level:'high'}},
{cat:'composition',scene:'Lavender rows receding to a stone farmhouse under a summer sky.',
 comp:['Leading lines','Purple rows converge on the farmhouse at the horizon.'],
 pal:[['lavender','#9A7BC8','rows'],['sky blue','#87B5E0','sky'],['stone','#B0A58E','farmhouse'],['leaf green','#5E8F4E','stems'],['cloud white','#F7F9FB','sky']],
 light:'Bright midday; saturated colors.',view:'Low, down the rows.',mood:'Idyllic order.',
 par:{aspect_ratio:'3:2',depth_of_field:'deep',focal_length:'24mm',detail_level:'high'}},
{cat:'scenes',scene:'A nebula vista with newborn stars, dark dust lanes sculpting the clouds.',
 comp:['Cosmic depth','Dust lanes lead the eye to the bright stellar nursery.'],
 pal:[['nebula violet','#6A3FA0','clouds'],['star white','#F4F6FF','stars'],['dust black','#0A0A14','lanes'],['hydrogen pink','#E86A92','emission'],['deep blue','#16224A','background']],
 light:'Self-lit gas; no external source — emission and reflection.',view:'Impossible deep-space vantage.',mood:'Awe at scale.',
 par:{aspect_ratio:'21:9',depth_of_field:'infinite',focal_length:'n/a (space)',detail_level:'ultra'}},
{cat:'viewpoints',scene:'A grand old library interior, ladders and galleries, dust in sunbeams.',
 comp:['Vertical emphasis','Tall shelves draw the eye up to the domed ceiling.'],
 pal:[['wood mahogany','#5A3226','shelves'],['book red','#8A2E2E','spines'],['parchment','#E8D9B8','pages'],['sunbeam','#F7E3A8','light'],['shadow brown','#2E1E14','corners']],
 light:'High windows; volumetric sunbeams through dust.',view:'Low angle from the floor center.',mood:'Reverent hush.',
 par:{aspect_ratio:'4:5',depth_of_field:'deep',focal_length:'16mm',detail_level:'ultra'}},
{cat:'color',scene:'A street lined with cherry blossoms in full bloom, petals drifting, a cyclist passing.',
 comp:['Color wash','Pink canopy fills the top two-thirds; street anchors below.'],
 pal:[['blossom pink','#F7B8C8','canopy'],['petal white','#FDF3F5','petals'],['bark dark','#3A2A28','trunks'],['asphalt','#4A4E54','street'],['sky pale','#D8E8F2','gaps']],
 light:'Soft overcast; blossoms glow without harsh shadow.',view:'Eye level down the street.',mood:'Fleeting beauty.',
 par:{aspect_ratio:'16:9',depth_of_field:'medium',focal_length:'35mm',detail_level:'high'}},
{cat:'attributes',scene:'A volcano erupting at night, lava fountains against a star field, glowing crater.',
 comp:['Scale contrast','Tiny human silhouettes on a ridge against the eruption column.'],
 pal:[['lava orange','#FF5A1F','lava'],['magma yellow','#FFC93C','fountains'],['night black','#05070D','sky'],['ash gray','#6E6A63','plume'],['star white','#EEF2FF','stars']],
 light:'The eruption lights itself; lava as key light.',view:'Distant ridge, telephoto compression.',mood:'Terrifying majesty.',
 par:{aspect_ratio:'16:9',depth_of_field:'deep',focal_length:'200mm',detail_level:'high'}},
{cat:'composition',scene:'A minimalist zen garden: raked gravel, three stones, one pruned pine.',
 comp:['Ma (negative space)','Gravel emptiness dominates; stones placed off-center.'],
 pal:[['gravel gray','#C9C4B8','gravel'],['stone dark','#5A564E','stones'],['pine green','#2E4A2E','pine'],['sky pale','#E8EEF2','sky']],
 light:'Soft overcast; almost shadowless.',view:'Slightly elevated, contemplative.',mood:'Profound stillness.',
 par:{aspect_ratio:'4:3',depth_of_field:'deep',focal_length:'50mm',detail_level:'medium'}}
];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var pool=opts.category?T.filter(function(x){return x.cat===opts.category;}):T;
  if(!pool.length)pool=T;
  var t=pick(pool,rnd);
  var pal=shuffle(t.pal,rnd).slice(0,3+((rnd()*3)|0)); /* 3..5 */
  var palette=pal.map(function(p){return {color:p[0],hex:p[1],role:p[2]};});
  var par={};Object.keys(t.par).forEach(function(k){par[k]=t.par[k];});
  /* deterministic parameter variation */
  var ars=['16:9','3:2','4:3','1:1','21:9'];
  if(rnd()<0.5)par.aspect_ratio=pick(ars,rnd);
  var dofs=['shallow','medium','deep'];
  if(rnd()<0.4)par.depth_of_field=pick(dofs,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:'Visual concept — '+t.scene.split(',')[0].slice(0,60),category:t.cat,
    scene:t.scene+' This is a Signature-generated visual concept brief: an original artwork description, not a photograph of a real place.',
    composition:{rule:t.comp[0],layout:t.comp[1]},palette:palette,
    lighting:t.light,viewpoint:t.view,mood:t.mood,parameters:par,
    param_count:Object.keys(par).length,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-VIS-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.scene!=='string'||r.scene.length<60)e.push('scene');
  if(!r.composition||typeof r.composition.rule!=='string'||!r.composition.rule.length)e.push('composition.rule');
  if(!r.composition||typeof r.composition.layout!=='string'||!r.composition.layout.length)e.push('composition.layout');
  if(!Array.isArray(r.palette)||r.palette.length<3||r.palette.length>6)e.push('palette');
  else r.palette.forEach(function(p){
    if(!p||typeof p.color!=='string'||!p.color.length)e.push('palette.color');
    if(!p||!HEX.test(p.hex||''))e.push('palette.hex');
    if(!p||typeof p.role!=='string'||!p.role.length)e.push('palette.role');
  });
  if(typeof r.lighting!=='string'||!r.lighting.length)e.push('lighting');
  if(typeof r.viewpoint!=='string'||!r.viewpoint.length)e.push('viewpoint');
  if(typeof r.mood!=='string'||!r.mood.length)e.push('mood');
  if(!r.parameters||typeof r.parameters!=='object')e.push('parameters');
  else{
    var ks=Object.keys(r.parameters);
    if(ks.length<2)e.push('parameters');
    /* REAL invariant: param_count must equal the parameters key count. */
    if(r.param_count!==ks.length)e.push('param_count');
    ks.forEach(function(k){if(typeof r.parameters[k]!=='string'||!r.parameters[k].length)e.push('parameter');});
  }
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-visual-concepts-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('visual-concepts',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
