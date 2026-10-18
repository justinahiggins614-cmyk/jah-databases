(function(){'use strict';
/* JAH The Sound Effect Inventor Database generator — jahdb-sound-effect-inventor-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working sound-effect inventor: every call designs an original SFX —
   name, category, a layered recipe (sources + processing), how to record or
   synthesize it, the use case, and a waveform SVG visualization.
   Deterministic: same seed, same effect. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SDFX-";
var FIELDS=["Impacts & Whooshes","Ambiences & Textures","Creature & Sci-Fi"];
var NAMES={"Impacts & Whooshes":[["Thunderclap","Doom"], ["Glass Shatter","Cascade"], ["Cannon Bloom","Siege"], ["Meteor Strike","Impact"], ["Door Slam","Vault"], ["Sword Ring","Steel"]],
 "Ambiences & Textures":[["Rain Cathedral","Drizzle"], ["Crowd Murmur","Arena"], ["Forest Night","Canopy"], ["Engine Room","Hull"], ["Desert Wind","Dune"], ["Café Glow","Murmur"]],
 "Creature & Sci-Fi":[["Void Beast","Growl"], ["Star Drive","Ignition"], ["Plasma Arc","Surge"], ["Deep Lurker","Call"], ["Robot Wake","Boot"], ["Alien Choir","Signal"]]};
var LAYERS={"Impacts & Whooshes":["sub-bass thump (sine drop 60→30 Hz)","mid crack (celery snap, pitched down)","air rush (reversed cymbal)","tail reverb (large hall, 3s)"],
 "Ambiences & Textures":["bed loop (field recording, 2 min seamless)","movement layer (filtered noise swells)","detail sprinkle (close-mic objects)","low glue (soft pink noise)"],
 "Creature & Sci-Fi":["voice base (pitched human vocal)","texture grit (granular scraping)","movement (filter sweeps)","space (convolution reverb, alien hall)"]};
var PROCESS=["pitch-shift ±12 semitones","time-stretch 200%","reverse the transient","layer at -6 dB","sidechain to the bed","granular freeze the tail","convolve with a stairwell","bit-crush to 8-bit then smooth"];
var USES={"Impacts & Whooshes":"film trailers, game combat hits, sports stingers",
 "Ambiences & Textures":"open-world games, film backgrounds, sleep apps",
 "Creature & Sci-Fi":"sci-fi films, creature reveals, UI power-ups"};
var RECORD=["a condenser mic and a quiet room","a field recorder and the real object","a synth with a noise oscillator","household objects and a contact mic"];
function waveSVG(s,cols){
  var bars="",x;
  for(x=0;x<60;x++){var h=10+Math.round(s()*70);bars+='<rect x="'+(x*5)+'" y="'+(90-h/2)+'" width="3" height="'+h+'" fill="'+cols[0]+'"/>';}
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="180" viewBox="0 0 300 180"><rect width="300" height="180" fill="'+cols[1]+'"/>'+bars+'<line x1="0" y1="90" x2="300" y2="90" stroke="'+cols[0]+'" stroke-width="1" opacity="0.5"/></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var nm=pick(NAMES[field],s);
  var layers=LAYERS[field].slice();
  var proc1=pick(PROCESS,s), proc2=pick(PROCESS,s);
  var pal=pick([["#FF6B35","#2B2D42"],["#20BF9F","#0B4F6C"],["#EF476F","#1A1A40"]],s);
  var svg=waveSVG(s,pal);
  var title=nm[0]+" — "+nm[1]+" SFX";
  var desc='INVENTED SOUND EFFECT — "'+title+'" ('+field+'). A '+field.toLowerCase()+' effect built from '+layers.length+' layers: '+layers.join('; ')+'. Process with '+proc1+' and '+proc2+'. Use for '+USES[field]+'.';
  var prog="# SFX recipe — "+nm[0]+"\n"
    +"name = \""+nm[0]+"\"\n"+"category = \""+field+"\"\n"
    +"layers = "+JSON.stringify(layers)+"\n"
    +"process = "+JSON.stringify([proc1,proc2])+"\n"
    +"print(\"SFX:\", name, \"(\"+category+\")\")\n"
    +"print(\"Layers:\")\n"+"[print(\" %d. %s\" % (i+1, l)) for i, l in enumerate(layers)]\n"
    +"print(\"Process:\", \", \".join(process))\n"
    +"print(\"Record with:\", \""+pick(RECORD,s)+"\")\n"
    +"print(\"Waveform SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — sfx record', title:title, description:desc,
    how_it_works:'The inventor picks an effect name from the '+field+' pool, assembles its four-layer recipe (source plus role for each layer), rolls two processing moves, and names the recording setup. The waveform SVG visualizes the effect\u2019s shape — deterministic per seed, so the same seed always invents the same effect.',
    key_points:['Effect: '+nm[0]+' ('+nm[1]+') — '+field,'Layers: '+layers.join(' | '),'Process: '+proc1+'; '+proc2,'Use for: '+USES[field]+'.','Record with '+pick(RECORD,s)+'.','Deterministic: seed '+seed+' always rebuilds this exact effect.'],
    requirements:['A seed number to regenerate this exact effect','Recording gear or a synth for the layers'],
    standards:['Four distinct layers with sources','Two processing moves specified','Use case named','Waveform SVG visualizes the shape'],
    citations:['Sound design references: layering technique.','Foley references: recording the layers.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{name:nm[0],subtitle:nm[1],layers:layers,process:[proc1,proc2],use:USES[field],svg:svg},
    svg:svg,
    demo:{kind:'sfx-recipe',language:'python',program:prog,note:'Prints the four-layer recipe, processing, and recording setup.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.layers||r.output.layers.length!==4)e.push('layers');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate sfx in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-sound-effect-inventor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sound-effect-inventor',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();