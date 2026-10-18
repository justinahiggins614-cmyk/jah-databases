(function(){'use strict';
/* JAH The Pixel Art Database generator — jahdb-pixel-art-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PIXELA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Pixel Art Is",
  "Pixel Art Software",
  "The Pixel Grid",
  "Basic Pixel Shapes",
  "Pixel Lines and Curves",
  "Pixel Color Palettes",
  "Shading with Pixels",
  "Dithering",
  "Anti-Aliasing by Hand",
  "Sprites: First Character",
  "Saving and Formats"
 ],
 "Compounded": [
  "Character Sprites",
  "Tilesets",
  "Animation: Walk Cycles",
  "Isometric Pixel Art",
  "Pixel Portraits",
  "Pixel Landscapes",
  "Limited Palettes",
  "Pixel Textures: Wood, Metal, Water",
  "UI and Icons in Pixels",
  "Game Backgrounds",
  "Color Ramps",
  "Pixel Art Style Studies"
 ],
 "Advanced": [
  "Finished Pixel Art Pieces",
  "Large Pixel Murals",
  "Pixel Art for Games",
  "The Pixel Artist's Business",
  "Teaching Pixel Art",
  "Famous Pixel Artists",
  "Pixel Art Animation: Advanced",
  "Procedural Pixel Techniques",
  "Printing Pixel Art",
  "Pixel Art and Mixed Media",
  "Exhibition and Display"
 ]
};
var DEMOKIND="pixel sprite planning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Pixel Sprite Planner — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — pixel art record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A pixel art record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-pixel-art-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pixel-art',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
