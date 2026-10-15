(function(){'use strict';
/* Public Music Theory Database generator — jahdb-music-theory-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-MUS-PUB-';
var TOPICS=[["Notes and Pitch", "The staff, clefs, and naming pitches."], ["Rhythm", "Note values, time signatures, and pulse."], ["Scales", "Major, minor, and modal scales."], ["Intervals", "Distances between pitches."], ["Chords", "Triads, sevenths, and voicings."], ["Chord Progressions", "How chords move: cadences and function."], ["Keys", "Key signatures and the circle of fifths."], ["Melody", "Contour, phrasing, and motifs."], ["Harmony", "Voice leading and part writing."], ["Counterpoint", "Independent melodic lines together."], ["Form", "Binary, ternary, sonata, and song forms."], ["Ear Training", "Hearing intervals, chords, and rhythms."], ["Sight Reading", "Reading music fluently."], ["Modes", "Dorian, Mixolydian, and modal color."], ["Jazz Theory", "Extensions, alterations, and ii-V-I."], ["Blues", "The twelve-bar form and blue notes."], ["Rhythm Changes", "The jazz standard progression."], ["Songwriting", "Melody, lyric, and structure."], ["Arranging", "Writing for ensembles."], ["Orchestration", "Colors of the orchestra."], ["Conducting", "Patterns and communication."], ["Music History", "Periods from medieval to modern."], ["World Music Theory", "Systems beyond Western tonality."], ["Electronic Music Theory", "Synthesis, sampling, and production."], ["Analysis", "Dissecting real pieces."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'music theory knowledge record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('music-theory-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();