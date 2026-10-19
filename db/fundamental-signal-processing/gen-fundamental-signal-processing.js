(function(){'use strict';
/* JAH Fundamentals of Signal Processing Database generator — jahdb-fundamental-signal-processing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SP-";
var FIELDS=["signals and systems", "sampling", "Fourier analysis", "digital filters", "spectral analysis", "applications"];
var TOPICS=[
    {t: "What Is a Signal", b: "A signal is information carried by a varying quantity \u2014 voltage over time, brightness over space, stock price over days \u2014 and processing extracts meaning from it."},
    {t: "Analog vs Digital", b: "Analog signals vary continuously; digital signals are sampled in time and quantized in amplitude, trading infinite resolution for noise immunity and computation."},
    {t: "Sampling and Aliasing", b: "Sampling too slowly folds high frequencies into fake low ones (aliasing \u2014 wagon wheels spinning backward on film); anti-alias filters must come first."},
    {t: "The Nyquist Limit", b: "CD audio samples at 44.1 kHz because hearing tops near 20 kHz and Nyquist demands more than double \u2014 the most famous number in digital audio."},
    {t: "Fourier: Time to Frequency", b: "The Fourier transform decomposes any signal into its sinusoidal ingredients, revealing hidden periodicities in sound, vibration, and markets."},
    {t: "The FFT Algorithm", b: "The Fast Fourier Transform computes the discrete transform in n\u00b7log(n) steps instead of n\u00b2 \u2014 the algorithm that made modern digital processing possible."},
    {t: "Filters: Shaping Frequency", b: "Low-pass, high-pass, band-pass, and notch filters keep wanted frequencies and remove the rest \u2014 the core tool of audio, radio, and image work."},
    {t: "FIR vs IIR Filters", b: "FIR filters are always stable with linear phase but need more taps; IIR filters are efficient but can ring or go unstable if designed carelessly."},
    {t: "Windowing and Spectral Leakage", b: "Cutting a signal into finite blocks smears its spectrum; window functions (Hann, Hamming) trade leakage against frequency resolution."},
    {t: "Noise and Signal-to-Noise Ratio", b: "Noise is unwanted randomness; SNR in decibels measures how far the signal stands above it, and averaging repeated measurements improves it by \u221aN."},
    {t: "Modulation and Demodulation", b: "AM, FM, and digital schemes (QAM, OFDM) impress data onto carrier waves \u2014 the entire basis of radio, Wi-Fi, and cellular."},
    {t: "Image Signals and 2-D Processing", b: "Images are two-dimensional signals: the same Fourier and filter mathematics sharpens photos, compresses JPEGs, and finds edges."}
];
var PRINCIPLES=[
    {n: "Nyquist-Shannon sampling", e: "fs > 2 * fmax", s: "A signal must be sampled faster than twice its highest frequency to be perfectly reconstructed."},
    {n: "Fourier series", e: "x(t) = \u03a3 a_n\u00b7e^{j\u00b7n\u00b7\u03c9\u2080t}", s: "Any periodic signal is a sum of sinusoids at harmonic frequencies."},
    {n: "Convolution", e: "y = x * h", s: "A linear system's output is the input convolved with its impulse response."}
];
var USES=["Cleaning up audio recordings", "Designing radio and Wi-Fi modems", "Compressing images and video", "Detecting vibrations in machinery"];
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
    id:id, t:tp.t, g:field, name:"Signal Processing"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Signal Processing demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-signal-processing-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-signal-processing-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-signal-processing",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
