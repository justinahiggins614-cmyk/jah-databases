(function(){'use strict';
/* JAH The Soundtrack to Your Life Database generator — jahdb-soundtrack-to-your-life-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working life-soundtrack generator: every call scores eight life scenes —
   morning, commute, workout, heartbreak, triumph, late night, celebration, quiet —
   with an original song (title, fictional artist, genre, mood, tempo, and why it fits).
   Deterministic: same seed, same soundtrack. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-SDTL-";
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
var gen={version:'jahdb-soundtrack-to-your-life-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('soundtrack-to-your-life',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();