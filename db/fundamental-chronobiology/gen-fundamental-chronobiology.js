(function(){'use strict';
/* JAH Fundamentals of Chronobiology Database generator — jahdb-fundamental-chronobiology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHR-";
var FIELDS=["circadian clocks", "entrainment", "ultradian rhythms", "seasonal rhythms", "chronomedicine", "shift work"];
var TOPICS=[
    {t: "Rhythms Are Everywhere", b: "From millisecond neural firing to annual migrations, biology is organized in time \u2014 chronobiology studies the clocks behind it."},
    {t: "The Molecular Clockwork", b: "Transcription-translation feedback loops (CLOCK/BMAL1, PER/CRY) tick in nearly every cell \u2014 a 24-hour oscillator built from genes."},
    {t: "Master Clock: The SCN", b: "The suprachiasmatic nucleus synchronizes the body's peripheral clocks via neural and hormonal signals \u2014 the conductor of the orchestra."},
    {t: "Entrainment by Light", b: "Intrinsically photosensitive retinal ganglion cells report dawn and dusk, resetting the clock daily against its natural drift."},
    {t: "Chronotypes: Larks and Owls", b: "Clock period and phase vary genetically; morningness and eveningness are biology, not character \u2014 with real performance consequences."},
    {t: "Ultradian Rhythms", b: "Shorter-than-day cycles \u2014 90-minute sleep cycles, 90-minute alertness cycles (BRAC), hourly hormone pulses \u2014 structure the day within the day."},
    {t: "Infradian and Seasonal Rhythms", b: "Menstrual cycles, hibernation, and migration run on monthly and annual clocks, often entrained by day length (photoperiod)."},
    {t: "Hormonal Timing", b: "Cortisol peaks at waking, growth hormone in deep sleep, insulin sensitivity by day \u2014 the same drug at different hours is a different drug."},
    {t: "Chronopharmacology", b: "Timing doses to circadian biology improves efficacy and cuts toxicity: chemotherapy, statins, and vaccines all show time effects."},
    {t: "Shift Work Disorder", b: "Night work misaligns clocks from behavior, raising metabolic, cardiovascular, and cancer risk \u2014 rotation direction and light therapy matter."},
    {t: "Jet Lag Science", b: "Eastward travel (phase advance) is harder than westward; timed light exposure and melatonin shift the clock ~1\u20131.5 h per day."},
    {t: "Social Jetlag", b: "Sleeping differently on weekends than weekdays is a weekly mini jet lag \u2014 regularity is the cheapest chronobiotic."}
];
var PRINCIPLES=[
    {n: "Free-running period", e: "\u03c4 \u2248 24.2 h (humans)", s: "Isolated from time cues, the human clock runs slightly longer than a day."},
    {n: "Phase response curve", e: "light timing \u2192 phase shift", s: "Light before the temperature minimum delays the clock; after it, advances it."},
    {n: "Entrainment condition", e: "|\u03c4 \u2212 T| < range of entrainment", s: "A clock locks to a cycle only when their periods are close enough."}
];
var USES=["Timing medication doses", "Designing shift schedules", "Treating circadian sleep disorders", "Planning light therapy"];
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
    id:id, t:tp.t, g:field, name:"Chronobiology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Chronobiology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-chronobiology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-chronobiology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-chronobiology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
