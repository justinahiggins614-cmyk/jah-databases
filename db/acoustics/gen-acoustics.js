(function(){'use strict';
/* JAH Acoustics Database generator — jahdb-acoustics-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record. src:"online" = core facts
   verified against published acoustics references; src:"signature" = Signature-authored
   study (physically consistent, clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['sound-sources','hearing-safety','musical-instruments','acoustic-materials','measurement','environments'];
var PREFIX='JAH-ACO-';
/* Real decibel chart anchors: [source, level, note] */
var CHART=[
 ['Threshold of hearing','0 dB','the faintest sound a healthy human ear can detect'],
 ['Rustling leaves','20 dB','just audible in a quiet setting'],
 ['Quiet whisper / library','30 dB','very quiet; a silent reading room'],
 ['Refrigerator hum','40 dB','gentle background noise in a quiet room'],
 ['Normal conversation','60 dB','typical speech measured at about 1 meter'],
 ['Vacuum cleaner','70 dB','steady noise that grows annoying over time'],
 ['Busy city traffic','80 dB','loud but not immediately harmful'],
 ['Average factory floor','85 dB','sustained exposure here risks hearing loss'],
 ['Lawn mower','90 dB','hearing damage can begin after about 2 hours'],
 ['Subway train','95 dB','measured inside the car'],
 ['Jackhammer','100 dB','hearing protection is recommended'],
 ['Rock concert','110 dB','very loud; a chainsaw measures about the same'],
 ['Car horn / siren','120 dB','extremely loud; thunderclaps reach this too'],
 ['Jet engine / gun blast','140 dB','pain threshold; immediate danger to hearing'],
 ['Rocket launch','180 dB','can perforate eardrums instantly']
];
/* Real musical-instrument anchors: [instrument, level, frequency range] */
var MUSIC=[
 ['Grand piano','60–70 dB practice','27.5 Hz (A0) to 4,186 Hz (C8), the full 88-key range'],
 ['Violin','82–92 dB','G3 196 Hz upward through the highest positions'],
 ['Cello','85–111 dB','C2 65.4 Hz to A5 880 Hz'],
 ['Flute','92–103 dB','C4 261.6 Hz to C7 2,093 Hz'],
 ['Clarinet','85–114 dB','from about 147 Hz into the altissimo register'],
 ['Trumpet','88–108 dB','F♯3 185 Hz to C6 1,047 Hz'],
 ['Timpani','106 dB peaks','D2 73.4 Hz to A2 110 Hz across the drums'],
 ['Pipe organ','up to 120 dB','16.35 Hz (C0, 32-foot stop) to 8,372 Hz'],
 ['Human voice, speech','60–70 dB','fundamental 85–255 Hz'],
 ['Symphonic peak','120–137 dB','full orchestra fortissimo; the bass drum carries about a third of the power']
];
/* Real hearing-safety anchors */
var SAFETY=[
 ['85 dB exposure limit','Sustained exposure above 85 dB risks permanent hearing loss.'],
 ['OSHA 8-hour rule','OSHA permits 8 hours per day at 90 dB, halving allowed time every 5 dB above it.'],
 ['100 dB / 15 minutes','At 100 dB — a jackhammer — damage can begin after about 15 minutes.'],
 ['125 dB pain begins','Pain begins around 125 dB; a pneumatic riveter measures about this.'],
 ['140 dB immediate damage','At 140 dB — a jet engine at close range — damage is immediate.'],
 ['2–4 kHz danger zone','High-frequency sound of 2,000–4,000 Hz is the most damaging to hearing.']
];
/* Real measurement anchors */
var MEASURE=[
 'The decibel scale is logarithmic: a 10 dB rise means ten times the sound power.',
 'A 1 dB change is imperceptible; 3 dB is barely perceptible; 10 dB sounds about twice as loud.',
 'Sound intensity falls with the square of distance from the source (inverse-square law).',
 'Sound travels about 343 meters per second in air at 20°C.',
 'Human hearing spans roughly 20 Hz to 20,000 Hz; the top piccolo octave is 2,048–4,096 Hz.',
 'Decibels are measured with a sound level meter using A-weighting (dBA) for human hearing.'
];
var ENVIRON=[
 ['Quiet library','30 dB','whisper-quiet reading rooms'],
 ['Suburban bedroom','40 dB','refrigerator hum level background'],
 ['Busy restaurant','70 dB','noisy dining room at peak hour'],
 ['City traffic, inside car','85 dB','windows up on a congested street'],
 ['Subway platform','95 dB','train arriving at the station'],
 ['Construction site','100 dB','jackhammers and heavy equipment'],
 ['Rock concert hall','115 dB','sandblasting measures about the same']
];
/* Signature study anchors — general, true acoustics principles, clearly labeled */
var MATERIALS=[
 ['porous absorber panel','Porous absorbers turn sound energy into heat through air friction inside the pores; thicker panels reach lower frequencies.'],
 ['bass trap','Bass traps are deep porous or resonant absorbers placed in corners where low-frequency pressure builds up.'],
 ['quadratic diffuser','Diffusers scatter reflections in many directions, evening out a room without deadening it.'],
 ['mass-loaded vinyl barrier','Mass law: doubling a wall\u2019s mass adds roughly 6 dB of transmission loss.'],
 ['perforated wood panel','Perforated panels backed by an air cavity absorb mid frequencies by Helmholtz resonance.'],
 ['heavy curtain','Heavy drapes absorb high frequencies and tame flutter echo between parallel walls.']
];
function build(rnd,cat){
 var sp={},title,desc,src='online';
 if(cat==='sound-sources'){
  var s=pick(CHART,rnd);
  sp={source_name:s[0],db_level:s[1],reference_note:s[2],measured_at:'measured near the source',application:pick(['noise ordinance checks','hearing protection planning','environmental surveys','product noise ratings'],rnd)};
  title=s[0]+' — '+s[1];
  desc='The reference chart rates '+s[0].toLowerCase()+' at '+s[1]+': '+s[2]+'. '+
   'All chart ratings are taken standing near the sound; distance lowers the reading fast. '+
   'Used for '+sp.application+'.';
 }else if(cat==='hearing-safety'){
  var h=pick(SAFETY,rnd);
  sp={guideline:h[0],detail:h[1],protection:pick(['earplugs','earmuffs','limiting exposure time','moving farther from the source'],rnd),application:'hearing conservation programs'};
  title='Hearing Safety — '+h[0];
  desc=h[1]+' This is a published hearing-safety reference value, not an estimate. '+
   'Recommended protection: '+sp.protection+'.';
 }else if(cat==='musical-instruments'){
  var m=pick(MUSIC,rnd);
  sp={instrument:m[0],db_level:m[1],frequency_range:m[2],application:pick(['orchestral seating plans','rehearsal room design','hearing protection for musicians','recording sessions'],rnd)};
  title=m[0]+' — '+m[1];
  desc='Measured performance levels for '+m[0].toLowerCase()+' run '+m[1]+', spanning '+m[2]+'. '+
   'High frequencies of 2,000–4,000 Hz are the most damaging, and aging steals the highs first. '+
   'Used in '+sp.application+'.';
 }else if(cat==='environments'){
  var e=pick(ENVIRON,rnd);
  sp={environment:e[0],db_level:e[1],description_detail:e[2],application:pick(['urban planning','workplace noise audits','real-estate disclosure','sleep studies'],rnd)};
  title=e[0]+' — '+e[1];
  desc='A typical '+e[0].toLowerCase()+' measures about '+e[1]+' ('+e[2]+'). '+
   'Because the scale is logarithmic, 70 dB carries ten times the power of 60 dB. '+
   'Used for '+sp.application+'.';
 }else if(cat==='measurement'){
  var f=pick(MEASURE,rnd);
  sp={principle:'acoustic measurement',statement:f,tool:'sound level meter (dBA)',application:pick(['calibrating meters','teaching acoustics','field surveys','lab reports'],rnd)};
  title='Measurement Principle — '+f.split(':')[0].split('.')[0].slice(0,48);
  desc=f+' Field readings use a sound level meter with A-weighting, which mimics human hearing. '+
   'Used when '+sp.application+'.';
 }else{
  var mt=pick(MATERIALS,rnd);
  sp={material:mt[0],principle:mt[1],placement:pick(['wall panels','ceiling clouds','corner traps','behind fabric'],rnd),application:'room acoustic treatment'};
  title='Signature Study — '+mt[0];
  desc='This is a Signature-authored acoustic treatment study on the '+mt[0]+'. '+
   mt[1]+' Typical placement: '+sp.placement+'.';
  src='signature';
 }
 return {title:title,description:desc,src:src,spec:sp};
}
function generate(seed,opts,rnd){
 opts=opts||{};rnd=rnd||prng(seed);
 var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
 var b=build(rnd,cat);
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,category:cat,src:b.src,spec:b.spec,_seed:seed};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-ACO-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<10)e.push('title');
 if(typeof r.description!=='string'||r.description.length<80)e.push('description');
 if(CATS.indexOf(r.category)<0)e.push('category');
 if(r.src!=='online'&&r.src!=='signature')e.push('src');
 var s=r.spec;
 if(!s||typeof s!=='object')e.push('spec');
 else{
  if(typeof s.application!=='string'||!s.application)e.push('spec.application');
  ['db_level','guideline','statement','material'].forEach(function(k){
   if(s[k]!==undefined&&(typeof s[k]!=='string'||!/[0-9A-Za-z]/.test(s[k])))e.push('spec.'+k);
  });
  if(s.db_level&&!/\d/.test(s.db_level))e.push('spec.db_level');
 }
 return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-acoustics-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('acoustics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
