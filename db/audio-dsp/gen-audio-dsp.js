(function(){'use strict';
/* JAH The Audio DSP Database generator — jahdb-audio-dsp-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AUD-";
var FIELDS=["audio"];
var TOPICS={
 "audio": [
  "Digital Audio Workstations \u2014 audio",
  "Multitrack Recorders \u2014 audio",
  "Software Synthesizers \u2014 audio",
  "Subtractive Synths \u2014 audio",
  "FM Synths \u2014 audio",
  "Wavetable Synths \u2014 audio",
  "Granular Synths \u2014 audio",
  "Additive Synths \u2014 audio",
  "Physical Modelers \u2014 audio",
  "Samplers \u2014 audio",
  "Drum Machines \u2014 audio",
  "Step Sequencers \u2014 audio",
  "Piano Rolls \u2014 audio",
  "VST Plugins \u2014 audio",
  "Audio Units \u2014 audio",
  "CLAP Plugins \u2014 audio",
  "LV2 Plugins \u2014 audio",
  "LADSPA Plugins \u2014 audio",
  "Oscillators \u2014 audio",
  "Low-Frequency Oscillators \u2014 audio",
  "ADSR Envelopes \u2014 audio",
  "Filters \u2014 audio",
  "State-Variable Filters \u2014 audio",
  "Ladder Filters \u2014 audio",
  "Comb Filters \u2014 audio",
  "Allpass Filters \u2014 audio",
  "Equalizers \u2014 audio",
  "Graphic Equalizers \u2014 audio",
  "Dynamic Equalizers \u2014 audio",
  "Compressors \u2014 audio",
  "Limiters \u2014 audio",
  "Gates \u2014 audio",
  "Expanders \u2014 audio",
  "De-Essers \u2014 audio",
  "Vocoders \u2014 audio",
  "Talkboxes \u2014 audio",
  "Pitch Shifters \u2014 audio",
  "Pitch Correctors \u2014 audio",
  "Harmonizers \u2014 audio",
  "Resamplers \u2014 audio",
  "Bitcrushers \u2014 audio",
  "Saturators \u2014 audio",
  "Distortions \u2014 audio",
  "Overdrives \u2014 audio",
  "Chorus Effects \u2014 audio",
  "Flangers \u2014 audio",
  "Phasers \u2014 audio",
  "Delays \u2014 audio",
  "Tape Delays \u2014 audio",
  "Reverbs \u2014 audio",
  "Convolution Reverbs \u2014 audio",
  "Impulse Responses \u2014 audio",
  "FFT Visualizers \u2014 audio",
  "Spectrum Analyzers \u2014 audio",
  "Loudness Meters \u2014 audio",
  "Phase Meters \u2014 audio",
  "Goniometers \u2014 audio",
  "Tuners \u2014 audio",
  "Metronomes \u2014 audio",
  "Loopers \u2014 audio"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Audio Dsp — "+safe+"\n"
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
    name:topic+' — audio record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A audio record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-audio-dsp-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('audio-dsp',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
