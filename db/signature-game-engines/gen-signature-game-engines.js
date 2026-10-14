(function(){'use strict';
/* Signature Game Engines Database generator — jahdb-signature-game-engines-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-SGE-';
var SRC='signature';
var RECORD_KIND='game engine concept';
var GENRES=["AI", "Animals", "Assets", "Athletics", "Aviation", "Balance", "Boundless scale", "Boundless worlds", "Builds", "Capture", "Cards", "Comfort", "Competition", "Cozy", "Design", "Direction", "Dynamics", "Ecosystem AI", "Education", "Fear", "Feel", "Finishing", "Gameplay", "HUD", "History", "Logic", "Medical", "Mood", "Motion", "Mystery", "NPCs", "Navigation", "Networking", "Pacing", "Parks", "Particles", "Phones", "Precision", "QA", "Rail", "Rewards", "Roguelike", "Sailing", "Sci-fi", "Services", "Signature graphics", "Sound", "Stability", "Story", "Streaming", "Systems", "Teaching", "Timing", "UGC", "Urban", "Writing"];
var TOPICS=["Prime World Engine", "Mosaic Build Farm", "Junction Designer", "Aperture Render", "Echo Audio Engine", "Verbatim Narrative", "Chrono Save", "Lumen VFX", "Atlas World", "Fable Character Engine", "Pulse Netcode", "Archive Asset Prime", "Codec Platform", "Input Atelier", "UI Forge", "Physics Yard", "AI Director Pro", "Lighting Stage", "Animation Junction", "Quest Weaver", "Economy Sim", "Tutorial Forge", "Boss Arena Lab", "Puzzle Box", "Racing Line Lab", "Stealth Shadow Lab", "Horror Dread Engine", "Cozy Corner Engine", "Rogue Deck Lab", "Card Table Engine", "Fighting Frame Lab", "Rhythm Beat Engine", "Sports Sim Lab", "City Sim Engine", "Farm Plot Engine", "Space Sim Lab", "Ocean Voyage Engine", "Flight Deck Lab", "Train Yard Engine", "Zoo Keeper Engine", "Theme Park Lab", "Hospital Ward Engine", "Courtroom Drama Engine", "Detective Board", "Library Prime Engine", "Render Guard Engine", "Match Build Pro", "Practice Arena", "Tournament Bracket", "Mod Workshop", "Archive Build Vault", "Mobile Port Lab", "Cloud Save Engine", "Mastering Build", "Dialogue Garden", "Cutscene Stage", "Minimap Cartographer", "Loading Screen Lab", "Achievement Forge", "Photo Mode Studio"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre){
  var summary='A game engine concept record for '+title+' ('+genre+'). Full profile in the archive.';
  var sections=[
    {heading:'Overview',body:'See the archived record '+title+' for the complete profile.'},
    {heading:'Key features',body:'Full feature list in the archived record.'},
    {heading:'Details',body:'Full details in the archived record.'}
  ];
  return{summary:summary,sections:sections,key_facts:['Deterministic generator record.','src: '+SRC+'.']};
}
function defaultDemo(){
  return{kind:'record-program',
    program:"// record viewer \u2014 run with: node demo.js\nconst r = JSON.parse(require('fs').readFileSync('record.json','utf8'));\nconsole.log(r.id+' \u2014 '+r.title);\nconsole.log(r.description);\nconsole.log('['+r.src+']');",
    note:'Prints the record. Run: node demo.js'};
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0)||1;
  var title=TOPICS[(s-1)%TOPICS.length];
  var genre=GENRES[(s-1)%GENRES.length];
  if(opts.genre&&GENRES.indexOf(opts.genre)>=0)genre=opts.genre;
  var ctopic=opts.topic?String(opts.topic).trim().slice(0,120):'';
  if(ctopic){title=ctopic;}
  var id=PREFIX+pad(s);
  var c=buildContent(title,genre);
  return{id:id,title:title,description:c.summary,genre:genre,type:RECORD_KIND,
    content:{summary:c.summary,sections:c.sections,key_facts:c.key_facts},
    demo:defaultDemo(),src:SRC,_seed:s};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0||!/\d{6}$/.test(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!r.content||typeof r.content!=='object'||typeof r.content.summary!=='string'||r.content.summary.length<10)e.push('content');
  if(!r.demo||typeof r.demo!=='object')e.push('demo');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].t===rec.title)return{ok:false,errors:['duplicate title in archive sample']};}
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-signature-game-engines-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-game-engines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();