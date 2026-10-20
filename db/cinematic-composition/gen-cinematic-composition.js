(function(){'use strict';
/* Public Cinematic Composition Database generator — jahdb-cinematic-composition-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-COMP-';
var LAST='2026-10-19';
var TITLES=["Golden Ratio Spiral", "Leading Lines", "Symmetry", "Negative Space", "Frame Within Frame", "Depth Layers", "Headroom Rule", "Nose Room", "Dutch Angle", "Low Angle Power", "High Angle Vulnerability", "Overhead Flat Lay", "Silhouette Framing", "Reflection Composition", "Juxtaposition", "Triangles", "Circles and Curves", "Diagonal Energy", "Foreground Framing", "Color Contrast", "Scale Contrast", "Repeating Patterns", "Fill the Frame", "Off-Center Tension", "Centered Portraits", "Layered Focus", "Environmental Portrait", "The Empty Chair", "Chaos Composition", "Rule of Thirds"];
var DEFS=["The phi spiral leads the eye to the subject.", "Roads, rails and edges pull the eye.", "Centered symmetry: order, fate, unease.", "Emptiness is emotion: isolation, awe.", "Doors and windows frame the subject.", "Foreground, midground, background: three planes.", "Small gap above the head; eyes on the upper third.", "Space in front of the gaze.", "Tilted horizon: unease, chaos.", "Camera below: the subject dominates.", "Camera above: the subject shrinks.", "Top-down: maps, tables, fate.", "Backlit shapes against bright fields.", "Mirrors double the frame.", "Two unlike things collide in frame.", "Three points stabilize or threaten.", "Round forms soften; arcs lead.", "Diagonals move; horizontals rest.", "Out-of-focus foreground adds depth.", "Complementary colors separate subject.", "Tiny human, vast world.", "Patterns with one break.", "No dead space in close-ups.", "Subject near the edge: about to leave.", "Dead-center faces confront.", "Rack focus between planes.", "The place is half the portrait.", "Absence composed.", "Controlled disorder for battle and panic.", "Place subjects on the third-lines and power points."];
var GROUPS=["Composition"];
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
window['JAHDB_GEN_cinematic_composition']={generate:generate};
})();
