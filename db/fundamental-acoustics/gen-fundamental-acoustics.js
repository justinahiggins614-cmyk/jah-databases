(function(){'use strict';
/* JAH Fundamentals of Acoustics Database generator — jahdb-fundamental-acoustics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ACO-";
var FIELDS=["wave propagation", "reflection and refraction", "resonance and standing waves", "the decibel scale", "room acoustics", "ultrasound and infrasound"];
var TOPICS=[
    {t: "What Sound Is", b: "Sound is a traveling pressure disturbance: molecules oscillate about rest positions while the wave itself carries energy forward, with no net transport of matter."},
    {t: "Speed of Sound in Air", b: "At 20\u00b0C sound travels about 343 m/s in air, rising roughly 0.6 m/s per degree Celsius because warmer molecules move faster and transmit disturbances sooner."},
    {t: "Frequency, Wavelength, and Pitch", b: "Frequency sets perceived pitch: concert A is 440 Hz with a wavelength near 0.78 m in air; doubling frequency halves wavelength and raises pitch one octave."},
    {t: "The Decibel Scale", b: "The decibel compresses huge pressure ratios into manageable numbers: 0 dB is the hearing threshold, normal speech about 60 dB, and 120 dB approaches pain."},
    {t: "Reflection, Refraction, Diffraction", b: "Sound reflects off hard surfaces (echoes), bends toward cooler air (refraction), and spreads around obstacles smaller than its wavelength (diffraction)."},
    {t: "Standing Waves and Resonance", b: "When a wave reflects onto itself at matching lengths, nodes and antinodes lock in: this resonance is why organ pipes and guitar strings sound specific notes."},
    {t: "Beats and Interference", b: "Two close frequencies played together produce beats at their difference frequency \u2014 the physical basis of tuning instruments by ear."},
    {t: "Absorption and Transmission Loss", b: "Soft porous materials convert sound energy to heat; transmission loss through a wall roughly doubles (6 dB) each time its mass per area doubles \u2014 the mass law."},
    {t: "Room Acoustics and Reverberation", b: "Reverberation time (Sabine: T = 0.161\u00b7V/A) measures how long sound lingers; concert halls target about 2 seconds, classrooms under 0.6."},
    {t: "Hearing and Psychoacoustics", b: "Human hearing spans roughly 20 Hz\u201320 kHz with peak sensitivity near 3\u20134 kHz; equal-loudness contours show bass needs more energy to sound as loud."},
    {t: "Ultrasound and Infrasound", b: "Above 20 kHz lies ultrasound (medical imaging, cleaning, sonar); below 20 Hz lies infrasound (elephants, earthquakes, wind turbines)."},
    {t: "Noise Control Engineering", b: "Quiet design works at source, path, and receiver: isolate vibration, add mass and absorption to the path, and protect the ear as the last resort."}
];
var PRINCIPLES=[
    {n: "Wave speed", e: "v = f * \u03bb", s: "Wave speed equals frequency times wavelength in any linear medium."},
    {n: "Sound pressure level", e: "L = 20 * log10(p / p0)", s: "Level in decibels relative to the 20-micropascal reference pressure in air."},
    {n: "Standing-wave resonance", e: "f_n = n * v / (2 * L)", s: "A tube or string of length L resonates at integer multiples of v/(2L)."}
];
var USES=["Designing concert halls with even sound coverage", "Setting safe workplace noise exposure limits", "Building ultrasound medical scanners", "Quieting machinery with mufflers and barriers"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Acoustics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Acoustics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-acoustics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-acoustics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-acoustics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
