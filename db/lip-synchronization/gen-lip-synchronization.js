(function(){'use strict';
/* Signature Lip Synchronization Database generator — jahdb-lip-synchronization-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-LIPSYNC-';
var LAST='2026-10-19';
var TITLES=["Viseme B", "Viseme C", "Viseme D", "Viseme E", "Viseme F", "Viseme G", "Viseme H", "Viseme X", "Phoneme Timing", "Coarticulation", "Stress Emphasis", "Emotion on the Mouth", "Singing Sync", "Whisper Sync", "Shout Sync", "Accent Shapes", "Child Speech", "Elder Speech", "Drunk Speech", "Sync QC", "Viseme Chart Standard", "Jaw Secondary", "Tongue Hints", "Breath Takes", "Off-Screen Dialogue", "ADR Matching", "Multi-Language Visemes", "Silence Acting", "Viseme Generator", "Viseme A"];
var DEFS=["Bilabials: b, m, p — lips together. Examples: buh, muh, puh.", "Alveolars and sibilants: c, d, g, k, n, s, t. Examples: kuh, duh, suh.", "Labiodentals: f, v — teeth on lip. Examples: fuh, vuh.", "L: tongue tip up. Examples: luh.", "Rounded: o. Examples: oh.", "Rounded tight: q, u, w. Examples: oo.", "R: bunched or retroflex. Examples: ruh.", "Rest: silence, breath. Examples: silence.", "Consonants 30-80ms, vowels 80-200ms at normal speech. Examples: consonant.", "Mouth shapes blend across phonemes. Examples: blend.", "Stressed syllables get bigger shapes. Examples: stress.", "The mouth carries the feeling under the words. Examples: feeling.", "Sustained vowels stretch the viseme. Examples: sing.", "Whispered lines: shapes stay, breath leads. Examples: whisper.", "Shouts widen everything. Examples: shout.", "Accents change the mouth. Examples: accent.", "Children: bigger, less precise shapes. Examples: child.", "Elders: slower, softer articulation. Examples: elder.", "Slurred: shapes melt together. Examples: drunk.", "Three checks: shape, timing, feeling. Examples: qc.", "The 9-viseme chart used across the pipeline. Examples: chart.", "The jaw follows the mouth with lag. Examples: jaw.", "The tongue shows on dentals and L. Examples: tongue.", "Breaths before long lines. Examples: breath.", "Looser sync allowed off-screen. Examples: offscreen.", "Replacement dialogue matched to picture. Examples: adr.", "Visemes adapt per language. Examples: lang.", "The mouth at rest still acts. Examples: rest.", "Text to viseme timeline, deterministic. Examples: gen.", "Open vowels: a, e, i. Examples: ah, eh, ih."];
var GROUPS=["Motion", "Performance", "Pipeline", "QC", "Reference", "Special", "Timing", "Tools", "Visemes"];
function demoFor(title,defn){return '/* '+title+' \u2014 runnable demo. Save as demo.js and run: node demo.js */\n\'use strict\';\nconsole.log('+JSON.stringify(title)+');\nconsole.log('+JSON.stringify(defn)+');';}
function generate(seed,count){
  var rnd=prng(seed*7919+13),rows=[],n=Math.max(1,Math.min(50,count||5));
  for(var i=0;i<n;i++){
    var ti=(rnd()*TITLES.length)|0, gi=(rnd()*GROUPS.length)|0;
    var title=TITLES[ti], defn=DEFS[ti%DEFS.length], grp=GROUPS[gi];
    var desc=defn.length>170?defn.slice(0,170)+'...':defn;
    var id=PREFIX+String(seed*1000+i+1).padStart(6,'0');
    var demo=demoFor(title,defn);
    rows.push({id:id,t:title,title:title,g:grp,genre:grp,description:desc,definition:defn,
      content:{generated:true,seed:seed,variant:i+1,topic:title,key_points:['Define the standard','Apply per production','Verify at the gate']},
      program_demo:demo,demo:{kind:'program',title:title+' \u2014 demo',program:demo,language:'javascript'},
      source:'signature-original',last_verified:LAST,src:'signature'});
  }
  return rows;
}
window['JAHDB_GEN_lip_synchronization']={generate:generate};
})();
