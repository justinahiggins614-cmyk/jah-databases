(function(){'use strict';
/* Public Depth and Spatial Geometry Database generator — jahdb-depth-and-spatial-geometry-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-DEPTH-';
var LAST='2026-10-19';
var TITLES=["Perspective Compression", "Hyperfocal Geometry", "Nodal Point", "Parallax Depth", "Vanishing Points", "Foreshortening Math", "Miniature Scale", "Forced Perspective", "Tilt-Shift Geometry", "Anamorphic Geometry", "Crop Factor", "Sensor Coverage", "Close Focus Limits", "Depth Cue Inventory", "Aerial Perspective", "Stereo Baseline", "Camera Height Grammar", "Lens Height vs Tilt", "Distance and Intimacy", "Geometry of the Reveal", "Geometry of the Trap", "Orbital Geometry", "Crane Geometry", "Dolly Geometry", "Handheld Geometry", "Gimbal Geometry", "Drone Geometry", "Virtual Geometry", "Geometry Master Check", "Field of View Math"];
var DEFS=["Long lenses flatten; wides stretch.", "H = f^2/(N*c).", "Rotate around the no-parallax point.", "Near moves faster than far.", "One, two, three point perspective.", "Limbs compress by cos(angle).", "Scale cues: grain, haze, depth.", "Align sizes by distance.", "Scheimpflug tilts the focus plane.", "Squeeze changes the math.", "Smaller sensors crop the FOV.", "Image circle must cover the sensor.", "Minimum focus distance matters.", "Overlap, size, haze, parallax, focus.", "Distance blues and pales.", "Interaxial sets the 3D volume.", "Eye level = neutral; low = power.", "Keep verticals vertical or tilt honestly.", "Shot size is emotional distance.", "Widening reveals truth.", "Tightening closes fate.", "Arcs keep distance constant.", "Arcs in vertical plane.", "Straight lines, level track.", "The body is the rig.", "Stabilized but motivated.", "Airspace is the set.", "CG cameras obey real optics.", "The final spatial audit.", "FOV = 2*atan(d/2f)."];
var GROUPS=["Geometry"];
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
window['JAHDB_GEN_depth_and_spatial_geometry']={generate:generate};
})();
