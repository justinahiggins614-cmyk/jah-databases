"""Music-audio GENERATOR items (4) — bespoke working client-side generators.
All are first_release_pick: built to highest polish.
Property of Justin Addam Higgins (JAH)."""

BAND_GENJS = r"""(function(){'use strict';
/* JAH The Fictional Band Generator Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working band generator: every call invents a complete fictional band —
   name, genre, lineup with personalities, origin story, debut album with full
   tracklist, signature sound, and a ready-to-render album-cover SVG.
   Deterministic: same seed, same band. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
var FIELDS=["Rock Bands","Electronic Acts","Eclectic Ensembles"];
var BAND_A=["Velvet","Neon","Copper","Midnight","Solar","Paper","Thunder","Glass","Iron","Honey","Static","Crimson","Electric","Wild","Golden","Silent"];
var BAND_B=["Revolver","Parade","Antler","Meridian","Foxglove","Static","Harbor","Comet","Juniper","Anthem","Mirage","Circuit","Lantern","Wolves","Arrow","Choir"];
var GENRES={"Rock Bands":["garage rock","indie rock","post-punk","stoner rock","art rock","heartland rock"],
 "Electronic Acts":["synthwave","techno","downtempo","hyperpop","ambient house","electroclash"],
 "Eclectic Ensembles":["art pop","chamber folk","jazz fusion","worldbeat","baroque pop","experimental"]};
var FIRST=["Mara","Jules","Theo","Priya","Dario","Wren","Kai","Lena","Otis","Suki","Rafe","Nadia","Ellis","June","Milo","Tessa","Idris","Noor","Felix","Ada"];
var LAST=["Vance","Okafor","Lindqvist","Marsh","Delacroix","Kim","Reyes","Novak","Ashby","Quill","Thorne","Ibarra","Sato","Wilder","Frost","Hale"];
var ROLES={"Rock Bands":["lead vocals / rhythm guitar","lead guitar","bass","drums","keyboards"],
 "Electronic Acts":["synth / programming","vocals","drums / pads","bass synth","visuals"],
 "Eclectic Ensembles":["vocals / strings","guitar","keys / accordion","bass","percussion"]};
var TRAITS=["the quiet perfectionist","the wild card","the diplomat","the night owl","the archivist","the prankster","the philosopher","the engine"];
var CITIES=["Portland","Glasgow","Lagos","Melbourne","Austin","Oslo","Mexico City","Seoul","Bristol","Detroit","Lisbon","Toronto"];
var ALBUM_A=["Static","Half-Light","Thunder","Paper","Neon","Low","Golden","Glass","Midnight","Wild","Electric","Silent"];
var ALBUM_B=["Bloom","Reverie","Parade","Mirage","Anthem","Harbor","Circuit","Lantern","Meridian","Choir","Arrow","Foxglove"];
var TRACKS=["Opener","Ignition","City Lights","Halfway Home","Static Bloom","The Long Parade","Glasshouse","Midnight Run","Paper Moons","Anthem for Nobody","Last Train","Reverie","Thunderhead","The Quiet","Neon Harbor","Foxglove","Meridian","Home Signal","Wild Choir","Golden Hour","Low Orbit","The Lantern"];
var PALETTES=[["#FF6B35","#F7C548","#2B2D42"],["#0B4F6C","#20BF9F","#F4F7F5"],["#8A1C7C","#EF476F","#F7C548"],["#1A1A40","#ACE1AF","#D4AF37"],["#C8102E","#F5F0E1","#1A1A1A"],["#005EB8","#FFC72C","#F5F0E1"]];
function coverSVG(initial,cols){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><rect width="300" height="300" fill="'+cols[2]+'"/><circle cx="150" cy="150" r="95" fill="'+cols[0]+'"/><circle cx="150" cy="150" r="62" fill="'+cols[1]+'"/><text x="150" y="172" font-family="Georgia,serif" font-size="72" font-weight="bold" text-anchor="middle" fill="'+cols[2]+'">'+initial+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var name=pick(BAND_A,s)+" "+pick(BAND_B,s);
  var genre=pick(GENRES[field],s);
  var roles=ROLES[field];
  var members=pickN(FIRST,s,5).map(function(fn,i){return {name:fn+" "+pick(LAST,s),role:roles[i],trait:pick(TRAITS,s)};});
  var city=pick(CITIES,s), year=1988+((s()*36)|0);
  var album=pick(ALBUM_A,s)+" "+pick(ALBUM_B,s);
  var tracklist=pickN(TRACKS,s,10);
  var pal=pick(PALETTES,s);
  var svg=coverSVG(name.charAt(0),pal);
  var title=name+" — "+genre+" band";
  var desc='GENERATED BAND — "'+name+'". A '+genre+' '+field.toLowerCase().slice(0,-1)+' from '+city+', formed '+year+'. Lineup: '+members.map(function(m){return m.name+" ("+m.role+")";}).join(", ")+'. Debut album "'+album+'" ('+tracklist.length+' tracks). Signature sound: '+genre+' built on '+members[0].role+' and '+members[1].role+'.';
  var prog="# Band dossier — "+name+"\n"
    +"band = \""+name+"\"\n"+"genre = \""+genre+"\"\n"+"formed = "+year+"\n"+"city = \""+city+"\"\n"
    +"lineup = "+JSON.stringify(members.map(function(m){return m.name+" — "+m.role;}))+"\n"
    +"album = \""+album+"\"\n"+"tracks = "+tracklist.length+"\n"
    +"print(\"Band:\", band)\n"+"print(\"Genre:\", genre)\n"+"print(\"Formed:\", formed, \"in\", city)\n"
    +"print(\"Debut album:\", album, \"(%d tracks)\" % tracks)\n"
    +"print(\"Lineup:\")\n"+"[print(\" -\", m) for m in lineup]\n"
    +"print(\"Cover SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — band record', title:title, description:desc,
    how_it_works:'The generator rolls a band name from evocative word pairs, assigns a genre from the '+field+' pool, builds a five-member lineup with names, roles, and personality traits, sets a formation city and year, titles a debut album, and picks a ten-track tracklist. The album-cover SVG renders the band initial in a generated palette — deterministic per seed.',
    key_points:['Band: '+name+' — '+genre+' ('+field+')','Formed '+year+' in '+city,'Lineup: '+members.map(function(m){return m.name;}).join(', '),'Debut album: "'+album+'" — '+tracklist.join('; '),'Cover palette: '+pal.join(', '),'Deterministic: seed '+seed+' always rebuilds this exact band.'],
    requirements:['A seed number to regenerate this exact band','An HTML file to view the cover SVG'],
    standards:['Band name is original and pronounceable','Lineup covers all five roles','Tracklist has exactly ten titles','Cover SVG renders the band initial'],
    citations:['Band-naming references: evocative compound names.','Album craft references: debut tracklist architecture.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{band:name,genre:genre,formed:year,city:city,members:members,album:album,tracklist:tracklist,palette:pal,svg:svg},
    svg:svg,
    demo:{kind:'band-dossier',language:'python',program:prog,note:'Prints the full band dossier: lineup, album, and tracklist.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.members||r.output.members.length!==5)e.push('members');
  if(!r.output||!r.output.tracklist||r.output.tracklist.length!==10)e.push('tracklist');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate band in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

LIFE_GENJS = r"""(function(){'use strict';
/* JAH The Soundtrack to Your Life Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working life-soundtrack generator: every call scores eight life scenes —
   morning, commute, workout, heartbreak, triumph, late night, celebration, quiet —
   with an original song (title, fictional artist, genre, mood, tempo, and why it fits).
   Deterministic: same seed, same soundtrack. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
var FIELDS=["Daily Scenes","Big Moments","Quiet Hours"];
var SCENES={"Daily Scenes":["Morning Alarm","Commute","Workout","Cooking Dinner"],
 "Big Moments":["Triumph","Heartbreak","Celebration","New Beginning"],
 "Quiet Hours":["Late Night","Rainy Afternoon","Stargazing","Sunday Morning"]};
var SONG_A=["Half-Light","Paper","Static","Golden","Neon","Low","Thunder","Glass","Midnight","Wild","Electric","Silent","Copper","Velvet","Solar","Honey"];
var SONG_B=["Bloom","Reverie","Parade","Mirage","Anthem","Harbor","Circuit","Lantern","Meridian","Choir","Arrow","Foxglove","Signal","Hour","Orbit","Run"];
var ARTIST_A=["The","Velvet","Neon","Copper","Midnight","Solar","Paper","Glass"];
var ARTIST_B=["Foxgloves","Circuits","Lanterns","Meridians","Choirs","Arrows","Harbor","Mirages"];
var GENRES=["indie folk","synth-pop","lo-fi hip-hop","ambient","garage rock","neo-soul","dream pop","post-rock","jazz-hop","chamber pop"];
var MOODS=["hopeful","wistful","electric","tender","defiant","calm","joyful","aching","weightless","grounded"];
var WHY=["its rising chorus matches the moment lift","the tempo walks at your pace","the lyric says what you cannot","the groove steadies the nerves","the melody opens the feeling","the beat carries the stride","the texture softens the edges","the hook makes it unforgettable"];
function tapeSVG(cols){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="190" viewBox="0 0 300 190"><rect width="300" height="190" rx="12" fill="'+cols[0]+'"/><rect x="20" y="60" width="260" height="70" rx="8" fill="'+cols[1]+'"/><circle cx="105" cy="95" r="22" fill="'+cols[0]+'"/><circle cx="195" cy="95" r="22" fill="'+cols[0]+'"/><circle cx="105" cy="95" r="7" fill="'+cols[1]+'"/><circle cx="195" cy="95" r="7" fill="'+cols[1]+'"/><rect x="20" y="20" width="260" height="24" rx="4" fill="'+cols[1]+'"/></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var allScenes=SCENES["Daily Scenes"].concat(SCENES["Big Moments"],SCENES["Quiet Hours"]);
  var scenes=pickN(allScenes,s,8);
  var seen={},uniq=[];scenes.forEach(function(x){if(!seen[x]){seen[x]=1;uniq.push(x);}});
  var si=0;while(uniq.length<8&&si<allScenes.length){var c=allScenes[si++];if(!seen[c]){seen[c]=1;uniq.push(c);}}
  var tracks=uniq.map(function(scene){
    var song=pick(SONG_A,s)+" "+pick(SONG_B,s);
    var artist=pick(ARTIST_A,s)+" "+pick(ARTIST_B,s);
    var genre=pick(GENRES,s), mood=pick(MOODS,s), bpm=70+((s()*90)|0);
    return {scene:scene,song:song,artist:artist,genre:genre,mood:mood,bpm:bpm,why:pick(WHY,s)};
  });
  var pal=pick([["#FF6B35","#2B2D42"],["#0B4F6C","#F4F7F5"],["#8A1C7C","#F7C548"],["#1A1A40","#ACE1AF"]],s);
  var svg=tapeSVG(pal);
  var title="Your Life Soundtrack — "+field;
  var desc='GENERATED SOUNDTRACK — "'+title+'". Eight life scenes, each scored with an original song: '+tracks.map(function(t){return t.scene+' — "'+t.song+'" by '+t.artist;}).join('; ')+'.';
  var prog="# Life soundtrack — "+field+"\n"
    +"tracks = "+JSON.stringify(tracks.map(function(t){return t.scene+": "+t.song+" — "+t.artist+" ("+t.genre+", "+t.bpm+" BPM)";}))+"\n"
    +"print(\"YOUR LIFE SOUNDTRACK — "+field.toUpperCase()+"\")\n"
    +"[print(\"%d. %s\" % (i+1, t)) for i, t in enumerate(tracks)]\n"
    +"print(\"Total runtime mood: scored\")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — soundtrack record', title:title, description:desc,
    how_it_works:'The generator picks eight distinct life scenes (weighted to the '+field+' field), then scores each with an original song: a two-word title, a fictional artist, a genre, a mood, a tempo, and the reason it fits the scene. The cassette SVG renders the mixtape. Deterministic per seed.',
    key_points:tracks.map(function(t){return t.scene+': "'+t.song+'" by '+t.artist+' — '+t.genre+', '+t.mood+', '+t.bpm+' BPM ('+t.why+').';}).concat(['Deterministic: seed '+seed+' always rebuilds this exact soundtrack.']),
    requirements:['A seed number to regenerate this exact soundtrack','An HTML file to view the cassette SVG'],
    standards:['Eight distinct scenes','Every track has song, artist, genre, mood, tempo, and reason','Song and artist names are original'],
    citations:['Soundtrack craft references: scoring life moments.','Music supervision references: scene-to-song matching.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{tracks:tracks,palette:pal,svg:svg},
    svg:svg,
    demo:{kind:'soundtrack-list',language:'python',program:prog,note:'Prints the eight-scene soundtrack with songs and tempos.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.tracks||r.output.tracks.length!==8)e.push('tracks');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate soundtrack in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

SFX_GENJS = r"""(function(){'use strict';
/* JAH The Sound Effect Inventor Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working sound-effect inventor: every call designs an original SFX —
   name, category, a layered recipe (sources + processing), how to record or
   synthesize it, the use case, and a waveform SVG visualization.
   Deterministic: same seed, same effect. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="__PREFIX__";
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
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

PODCAST_GENJS = r"""(function(){'use strict';
/* JAH The Podcast Idea Factory Database generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working podcast factory: every call creates a complete show concept —
   title, tagline, format, two hosts with bios, six episode ideas, target audience,
   and a ready-to-render cover-art SVG.
   Deterministic: same seed, same show. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="__PREFIX__";
var FIELDS=["Talk & Interview","Story & Narrative","Comedy & Play"];
var TITLES={"Talk & Interview":[["The Long Table","conversations that run past midnight"],["Signal & Noise","finding the story in the static"],["Second Draft","creators on the work before the work"],["The Green Room","what guests say after the show"]],
 "Story & Narrative":[["The Paper Trail","mysteries told in documents"],["Low Orbit","dispatches from the edge"],["The Lantern Archive","stories kept in the dark"],["Halfway Home","journeys that changed the teller"]],
 "Comedy & Play":[["The Pun Also Rises","wordplay with ambition"],["Serious Nonsense","very silly, very smart"],["The Laugh Track","comedy, examined"],["Yes, And...","improv games with real stakes"]]};
var FORMATS={"Talk & Interview":"weekly long-form conversation, 60–90 minutes, one guest, cold open with the best moment",
 "Story & Narrative":"serialized narrative, 30–45 minutes, scored and sound-designed, season arcs of eight episodes",
 "Comedy & Play":"panel games and bits, 45 minutes, recurring segments, audience call-ins"};
var FIRST=["Mara","Jules","Theo","Priya","Dario","Wren","Kai","Lena","Otis","Suki","Rafe","Nadia"];
var LAST=["Vance","Okafor","Lindqvist","Marsh","Delacroix","Kim","Reyes","Novak"];
var BIOS=["a former radio producer who asks the question nobody asks","a comedian with a researcher\u2019s heart","a novelist who treats every guest like a character","a sound designer who hears stories in noise","a journalist who laughs at the wrong moments","an archivist of other people\u2019s best stories"];
var EPISODES={"Talk & Interview":["The guest who almost didn\u2019t come","Failure, ranked","The 3am question","Mentors and rivals","The episode with no guest","Live from the green room"],
 "Story & Narrative":["The letter that started it","Static: episode one","The map room","What the tape caught","The return","Season finale: the lantern"],
 "Comedy & Play":["Pun championship semifinals","The bit that bombed (and why)","Call-in chaos hour","Improv: the haunted studio","The roast of the hosts","Live show spectacular"]};
var AUDIENCES={"Talk & Interview":"curious commuters and late-night thinkers","Story & Narrative":"headphone people who finish every series","Comedy & Play":"anyone who laughs at wordplay in traffic"};
function coverSVG(initial,cols){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><rect width="300" height="300" fill="'+cols[1]+'"/><rect x="30" y="30" width="240" height="240" rx="24" fill="'+cols[0]+'"/><text x="150" y="185" font-family="Georgia,serif" font-size="110" font-weight="bold" text-anchor="middle" fill="'+cols[1]+'">'+initial+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var tt=pick(TITLES[field],s);
  var hosts=[{name:pick(FIRST,s)+" "+pick(LAST,s),bio:pick(BIOS,s)},{name:pick(FIRST,s)+" "+pick(LAST,s),bio:pick(BIOS,s)}];
  var eps=pickN(EPISODES[field],s,6);
  var pal=pick([["#FF6B35","#2B2D42"],["#20BF9F","#0B4F6C"],["#8A1C7C","#F7C548"],["#005EB8","#F5F0E1"]],s);
  var svg=coverSVG(tt[0].charAt(0),pal);
  var title=tt[0]+" — podcast concept";
  var desc='GENERATED PODCAST — "'+tt[0]+'": '+tt[1]+'. A '+field.toLowerCase()+' show ('+FORMATS[field]+'), hosted by '+hosts[0].name+' and '+hosts[1].name+'. Six launch episodes planned. For '+AUDIENCES[field]+'.';
  var prog="# Podcast concept — "+tt[0]+"\n"
    +"title = \""+tt[0]+"\"\n"+"tagline = \""+tt[1]+"\"\n"+"format_ = \""+FORMATS[field]+"\"\n"
    +"hosts = "+JSON.stringify(hosts.map(function(h){return h.name;}))+"\n"
    +"episodes = "+JSON.stringify(eps)+"\n"
    +"print(\"Podcast:\", title)\n"+"print(\"Tagline:\", tagline)\n"+"print(\"Format:\", format_)\n"
    +"print(\"Hosts:\", \", \".join(hosts))\n"+"print(\"Launch episodes:\")\n"
    +"[print(\" %d. %s\" % (i+1, e)) for i, e in enumerate(episodes)]\n"
    +"print(\"Cover SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — podcast record', title:title, description:desc,
    how_it_works:'The factory picks a show title and tagline from the '+field+' pool, assigns the field\u2019s format, creates two hosts with names and bios, and plans six launch episode titles. The cover-art SVG renders the show initial in a generated palette — deterministic per seed.',
    key_points:['Show: "'+tt[0]+'" — '+tt[1],'Format: '+FORMATS[field],'Hosts: '+hosts.map(function(h){return h.name+" ("+h.bio+")";}).join('; '),'Episodes: '+eps.join('; '),'Audience: '+AUDIENCES[field]+'.','Deterministic: seed '+seed+' always rebuilds this exact show.'],
    requirements:['A seed number to regenerate this exact show','An HTML file to view the cover SVG'],
    standards:['Title and tagline are original','Two hosts with distinct bios','Six episode titles planned','Cover SVG renders the show initial'],
    citations:['Podcast craft references: format design.','Audio storytelling references: episode architecture.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{show:tt[0],tagline:tt[1],format:FORMATS[field],hosts:hosts,episodes:eps,audience:AUDIENCES[field],svg:svg},
    svg:svg,
    demo:{kind:'podcast-plan',language:'python',program:prog,note:'Prints the show concept, hosts, and six launch episodes.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.hosts||r.output.hosts.length!==2)e.push('hosts');
  if(!r.output||!r.output.episodes||r.output.episodes.length!==6)e.push('episodes');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate podcast in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

def _item(slug, name, tagline, record_kind, ai_name, role, greet, searchph, chatph, short, fields, genjs, gen_desc, sig_tagline):
    return {
        'slug': slug, 'cls': 'gen', 'renderer': None,
        'name': name, 'tagline': tagline, 'record_kind': record_kind,
        'ai_name': ai_name, 'role': role, 'greet': greet, 'searchph': searchph,
        'chatph': chatph, 'short': short, 'fields': fields,
        'hero_extra': 'Every record carries the full entry: description, how it works, key points, requirements, standards, citations, and a working demonstration program. Records are ordered by the teaching ladder, simple to complex.',
        'sig_tagline': sig_tagline, 'genjs': genjs, 'gen_desc': gen_desc,
        'prefix': None,  # filled from prefixes.json by build.py
    }

ITEMS = [
_item('fictional-band-generator', 'The Fictional Band Generator Database',
 'Invent complete fictional bands on demand: names, genres, five-member lineups with personalities, origin stories, debut albums with full tracklists, and album-cover art — every seed founding a new band with a sound worth hearing.',
 'band generator record', 'JAH Fictional Band Generator Archivist',
 'fictional band generator archivist — operating a real working band inventor and teaching band-building craft; answering from many angles using only archive data',
 'Ask me to invent a band — pick a family or let the seed decide.',
 'Search bands, lineups, albums, genres...', 'Ask for a band...', 'band',
 ['Rock Bands','Electronic Acts','Eclectic Ensembles'], BAND_GENJS,
 'A real working band inventor: pick a family and seed, get a complete fictional band — lineup, debut album, tracklist, and cover art.',
 'The Signature treatment of band invention: the same real generator carried forward, plus Signature-original band families and impossible lineups original to this system.'),
_item('soundtrack-to-your-life', 'The Soundtrack to Your Life Database',
 'Score your life like a film: eight life scenes — mornings, commutes, triumphs, heartbreaks, late nights — each with an original song, fictional artist, genre, mood, and tempo, plus a mixtape cassette to prove it.',
 'life soundtrack record', 'JAH Life Soundtrack Archivist',
 'life soundtrack archivist — operating a real working soundtrack composer and teaching scene-to-song craft; answering from many angles using only archive data',
 'Ask me to score your life — pick a chapter or let the seed decide.',
 'Search soundtracks, scenes, songs, moods...', 'Ask for a soundtrack...', 'soundtrack',
 ['Daily Scenes','Big Moments','Quiet Hours'], LIFE_GENJS,
 'A real working soundtrack composer: pick a chapter and seed, get eight scored life scenes with original songs and a mixtape cassette.',
 'The Signature treatment of life soundtracks: the same real composer carried forward, plus Signature-original life chapters and impossible scenes original to this system.'),
_item('sound-effect-inventor', 'The Sound Effect Inventor Database',
 'Invent original sound effects on demand: impacts, whooshes, ambiences, textures, creatures, and sci-fi — each with a four-layer recipe, processing moves, recording setup, use case, and waveform visualization.',
 'sound effect record', 'JAH Sound Effect Inventor Archivist',
 'sound effect inventor archivist — operating a real working SFX inventor and teaching sound design; answering from many angles using only archive data',
 'Ask me to invent a sound effect — pick a category or let the seed decide.',
 'Search sound effects, layers, recipes, waveforms...', 'Ask for a sound effect...', 'sfx',
 ['Impacts & Whooshes','Ambiences & Textures','Creature & Sci-Fi'], SFX_GENJS,
 'A real working SFX inventor: pick a category and seed, get an original effect with layered recipe, processing, and waveform.',
 'The Signature treatment of SFX invention: the same real inventor carried forward, plus Signature-original effect categories and impossible sounds original to this system.'),
_item('podcast-idea-factory', 'The Podcast Idea Factory Database',
 'Launch a podcast from one seed: complete show concepts with titles, taglines, formats, two hosts with bios, six launch episode ideas, target audiences, and cover art — every seed a show worth subscribing to.',
 'podcast concept record', 'JAH Podcast Idea Factory Archivist',
 'podcast idea factory archivist — operating a real working podcast factory and teaching show development; answering from many angles using only archive data',
 'Ask me to create a podcast — pick a lane or let the seed decide.',
 'Search podcasts, formats, hosts, episodes...', 'Ask for a podcast...', 'podcast',
 ['Talk & Interview','Story & Narrative','Comedy & Play'], PODCAST_GENJS,
 'A real working podcast factory: pick a lane and seed, get a complete show — hosts, format, six episodes, and cover art.',
 'The Signature treatment of podcast ideas: the same real factory carried forward, plus Signature-original show lanes and impossible formats original to this system.'),
]
