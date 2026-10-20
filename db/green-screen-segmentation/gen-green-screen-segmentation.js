(function(){'use strict';
/* Public Green Screen Segmentation Database generator — jahdb-green-screen-segmentation-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-CHROMA-';
var LAST='2026-10-19';
var TITLES=["Distance Discipline", "Spill Kill", "Shutter and Motion", "Hair Detail", "Transparent Objects", "Motion Blur Edges", "Tracking Markers", "Wrinkle Patrol", "Color Sampling", "Edge Choke", "Light Wrap", "Shadow Retention", "Blue vs Green", "Day Exterior Key", "Night Key", "Full Body Key", "Car Key", "Water Key", "Smoke on Green", "Fire on Green", "Crowd Key", "Creature Key", "Virtual Production", "Key QC", "Roto Assist", "Spill Maps", "Edge Extend", "Final Key Review", "Master Key Bible", "Screen Evenness"];
var DEFS=["Subject off the screen.", "Green off skin.", "Crisp edges.", "Keep the flyaways.", "Glass honest.", "Blur keeps.", "For the move.", "Flat screen.", "Key the true green.", "Tighten.", "Background bleeds.", "Keep contact.", "Choose.", "Sunlit.", "Dark.", "Feet included.", "Vehicle.", "Wet.", "Atmosphere.", "Flames.", "Many.", "Fur.", "LED alternative.", "Three gates.", "Help the key.", "Targeted.", "Background.", "Big screen.", "One method.", "Light the green flat."];
var GROUPS=["Keying"];
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
window['JAHDB_GEN_green_screen_segmentation']={generate:generate};
})();
