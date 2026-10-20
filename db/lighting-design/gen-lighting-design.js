(function(){'use strict';
/* Public Lighting Design Database generator — jahdb-lighting-design-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-LIGHT-';
var LAST='2026-10-19';
var TITLES=["Rembrandt Lighting", "Butterfly / Paramount", "Split Lighting", "Loop Lighting", "Broad Lighting", "Short Lighting", "Noir Low-Key", "High-Key Comedy", "Motivated Practicals", "Moonlight Night", "Firelight Flicker", "Neon Night", "Overcast Day", "Golden Hour", "Blue Hour", "Window Light Portrait", "Top Light Dread", "Underlight Horror", "Silhouette Setup", "Car Interior Night", "Candlelit Scene", "Fluorescent Office", "Stage Wash", "Day Interior Balance", "Night Exterior Street", "Underwater Light", "Storm Light", "Desert Noon Tame", "Snow Bounce", "Three-Point Lighting"];
var DEFS=["Triangle of light on the shadow cheek.", "Key above camera: glamour.", "Half the face lit, half dark.", "Key slightly off-axis: gentle modeling.", "Light the camera-side cheek: widen.", "Light the far cheek: slim.", "Deep shadows, hard sources.", "Bright, even, shadowless.", "Lamps in frame justify the light.", "Blue backlight, cool fill.", "Warm dancing source.", "Colored practicals motivate.", "Giant softbox sky.", "Low warm sun, long shadows.", "After sunset: blue ambience.", "Single window: nature's softbox.", "Overhead hard: skull shadows.", "Light from below: the monster.", "Expose for background only.", "Dashboard glow + passing lights.", "Warm practical cluster.", "Green-corrected overheads.", "Theatrical color from above.", "Window vs interior levels.", "Sodium + moon + car beams.", "Top shafts, green murk.", "Dark sky, single warm window.", "Brutal sun controlled.", "Nature's bounce card.", "Key, fill, back: the foundation."];
var GROUPS=["Setup"];
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
window['JAHDB_GEN_lighting_design']={generate:generate};
})();
