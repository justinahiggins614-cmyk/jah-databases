(function(){'use strict';
/* JAH The Music, Acoustics and Sensory Phenomena Databases Database generator — jahdb-music-acoustics-databases-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MUSA-";
var FIELDS=["catalog-paste archives", "Strangest Sounds", "Cinematic Sound", "Sound Illusions"];
var TOPICS={
 "catalog-paste archives": [

 ]
,
 "Strangest Sounds": [
  "The Bloop: Revisited",
  "The Hum: The Unheard Epidemic",
  "The Sky Trumpets",
  "The Wow Signal of Sound: The Upsweep",
  "The Slowdown",
  "The Train Whistle of the Deep",
  "Bio-Duck: The Antarctic Mystery",
  "The Julia",
  "Singing Sand Dunes",
  "The Bloodhound's Roar: Iceberg Songs",
  "The Taos Hum Investigation",
  "Infrasound and Unease",
  "The Strangest Sound Archive",
  "The 52-Hertz Whale",
  "The Seismic Hum of Earth"
 ],
 "Cinematic Sound": [
  "The Wilhelm Scream",
  "Foley: The Art of Footsteps",
  "The Lightsaber Hum",
  "The TIE Fighter Scream",
  "The Inception Braam",
  "Silence as Sound Design",
  "The Shepard Tone",
  "Creature Vocals",
  "The Room Tone",
  "The Stinger",
  "The Montage Music",
  "The Diegetic Song",
  "The Sound Bridge",
  "The Final Mix",
  "The Sound of the Future"
 ],
 "Sound Illusions": [
  "The Shepard Tone Illusion",
  "The Tritone Paradox",
  "The McGurk Effect",
  "The Phantom Words",
  "The Octave Illusion",
  "The Scale Illusion",
  "The Missing Fundamental",
  "The Binaural Beats",
  "The Auditory Afterimage",
  "The Speech-to-Song Illusion",
  "The Yanny-Laurel Lesson",
  "The Risset Rhythm",
  "The Glissando Illusion",
  "The Illusion Collection",
  "Hearing the Unheard"
 ]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Music Acoustics Databases — "+safe+"\n"
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
    name:topic+' — acoustics catalog record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A acoustics catalog record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-music-acoustics-databases-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('music-acoustics-databases',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
