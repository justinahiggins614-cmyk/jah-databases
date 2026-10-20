(function(){'use strict';
/* Public Spatial Audio Database generator — jahdb-spatial-audio-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-SPAT-';
var LAST='2026-10-19';
var TITLES=["ITD: Time Differences", "ILD: Level Differences", "HRTF Basics", "Distance Cues", "Doppler Effect", "Reverb Zones", "5.1 Layout", "7.1 Layout", "Atmos Objects", "Binaural", "Ambisonics", "Panning Automation", "Dialogue Panning", "Music Panning", "Effects Panning", "LFE Discipline", "Height Channels", "Downmix Compatibility", "Mono Compatibility", "Headphone Check", "Theater Calibration", "Home Theater", "VR Audio", "Game Audio", "Live Recording Spatial", "Foley Panning", "Crowd Panning", "Master Spatial Bible", "Stereo Panning Laws", "ITD: Time Differences"];
var DEFS=["Ears hear at different times.", "Head shadows sound.", "Ears filter direction.", "Far sounds duller, quieter, wetter.", "Pitch shifts with motion.", "Rooms have sound.", "Cinema standard.", "More surrounds.", "Sound as objects.", "Headphones 3D.", "Sphere of sound.", "Moves drawn.", "Voices placed.", "Stage.", "World.", "Sub-bass channel.", "Overhead.", "Folds down.", "Phase.", "Binaural test.", "85dB.", "Smaller rooms.", "Head-tracked.", "Interactive.", "Capture the room.", "Movement placed.", "Masses wide.", "One method.", "Sine, linear, constant power.", "Ears hear at different times."];
var GROUPS=["Spatial"];
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
window['JAHDB_GEN_spatial_audio']={generate:generate};
})();
