(function(){'use strict';
/* Public Camera and Lens Database generator — jahdb-camera-and-lens-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-CAM-';
var LAST='2026-10-19';
var TITLES=["18mm Wide", "24mm Wide", "28mm Wide", "35mm Wide-Normal", "40mm Normal", "50mm Normal", "58mm Portrait", "85mm Portrait", "100mm Macro", "135mm Telephoto", "200mm Telephoto", "300mm Super-Tele", "24-70mm Zoom", "70-200mm Zoom", "16-35mm Zoom", "Anamorphic 40mm", "Anamorphic 75mm", "Fisheye 8mm", "Tilt-Shift 24mm", "200-600mm Zoom", "35mm T1.5 Cine", "50mm T1.5 Cine", "85mm T1.5 Cine", "18mm T2 Cine", "135mm T2 Cine", "25mm Vintage", "50mm Vintage", "90mm Tilt-Shift Macro", "12mm Extreme Wide", "14mm Ultra-Wide"];
var DEFS=["Wide without chaos.", "The classic wide: context with control.", "Documentary wide.", "The storyteller: wide enough for context, tight enough for faces.", "Near-human vision.", "The nifty fifty: portraits and low light.", "Slight compression flatters faces.", "The portrait king: compression + bokeh.", "1:1 detail: inserts with intent.", "Compressed emotion from a distance.", "Flattened layers, distant drama.", "Extreme reach, paper-thin depth.", "The workhorse range.", "The event telephoto.", "Wide zoom for tight spaces.", "2x squeeze: oval bokeh, horizontal flare.", "Portrait anamorphic.", "180-degree funhouse.", "Miniature effect, plane of focus control.", "Wildlife reach.", "Cinema housing, smooth focus throw.", "Cinema normal.", "Cinema portrait.", "Cinema ultra-wide.", "Cinema telephoto.", "Character glass: flare and softness.", "Swirly bokeh character lens.", "Precision focus control.", "Reality-bending width.", "Vast interiors, exaggerated depth."];
var GROUPS=["Lens"];
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
window['JAHDB_GEN_camera_and_lens']={generate:generate};
})();
