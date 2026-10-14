(function(){'use strict';
/* Public Music Production Software Database generator — jahdb-public-music-production-software-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-MPS-';
var SRC='public-harvest';
var RECORD_KIND='music production software';
var GENRES=["DAW", "EQ plugin", "MIDI controller", "audio editor", "audio editor/DAW", "audio repair", "beat DAW", "cloud DAW", "cloud DAW/social", "collab jam app", "controller", "effects bundle", "entry DAW", "groovebox", "hardware/controller", "looper", "mixer/host", "mobile DAW", "mobile sampler", "modular groovebox", "open-source DAW", "pitch correction", "plugin subscription", "production tools", "reverb plugins", "sample instrument", "sample library", "sample/plugin co", "sampler", "sampler companion", "synth", "synth bundle"];
var TOPICS=["Ableton Live", "FL Studio", "Logic Pro", "Pro Tools", "Steinberg Cubase", "PreSonus Studio One", "Reason", "Bitwig Studio", "REAPER", "Apple GarageBand", "Avid Pro Tools | First", "Cakewalk by BandLab", "Tracktion Waveform", "Ardour", "LMMS", "Audacity", "Ocenaudio", "Wavosaur", "Sound Forge", "Adobe Audition", "iZotope RX", "Celemony Melodyne", "Antares Auto-Tune", "Waves Tune", "Native Instruments Kontakt", "Spectrasonics Omnisphere", "Xfer Serum", "Vital", "Arturia V Collection", "u-he Diva", "FabFilter Pro-Q", "Valhalla Reverbs", "Soundtoys Bundle", "Output Arcade", "Splice Sounds", "Loopmasters", "Cymatics", "BandLab", "Soundtrap", "Amped Studio", "Audiotool", "Endlesss", "FL Studio Mobile", "Cubasis", "GarageBand iOS", "Koala Sampler", "Drambo", "AUM", "Loopy Pro", "Quantiloop", "SP-404MKII app", "MPC Beats", "Serato Studio", "Mixed In Key Studio", "Ableton Push", "Native Instruments Maschine", "Arturia KeyLab", "Novation Launchpad", "Akai MPK Mini", "Roland Cloud"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre){
  var summary='A music production software record for '+title+' ('+genre+'). Full profile in the archive.';
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
var gen={version:'jahdb-public-music-production-software-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-music-production-software',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();