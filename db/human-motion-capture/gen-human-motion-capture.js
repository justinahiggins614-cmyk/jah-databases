(function(){'use strict';
/* Public Human Motion Capture Database generator — jahdb-human-motion-capture-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-MOCAP-';
var LAST='2026-10-19';
var TITLES=["FBX Format", "C3D Format", "Joint Hierarchy", "Marker Sets", "Capture Volume", "Frame Rates", "Occlusion Handling", "Retargeting", "Foot Contacts", "Root Motion", "Facial Capture", "Finger Capture", "Prop Capture", "Multi-Actor Capture", "Stunt Capture", "Animal Capture", "Cleanup Passes", "Filtering Rules", "Looping Takes", "Mirroring", "Time Warping", "Layering", "Crowd Mocap", "Real-Time Preview", "Data Management", "Calibration", "Suit Fit", "Performance Direction", "Mocap QC", "BVH Format"];
var DEFS=["Autodesk interchange: rigs, meshes, animation in one binary.", "Optical mocap: 3D point trajectories with analog data.", "Hips root, spine chain, limbs as children.", "Standard sets: 41, 53, 76 markers.", "Calibrated camera volume defines the stage.", "120-240 fps for fast action; 60-120 for dialogue.", "Markers hide; solve with rigid bodies and gap fill.", "Map source skeleton to character rig.", "Feet must plant: detect and lock contacts.", "Separate locomotion from in-place cycles.", "Head-mounted cameras track the face.", "Data gloves or optical finger markers.", "Rigid props tracked as bodies.", "Interactions captured together.", "Wires and pads alter the data.", "Quadruped marker sets and patience.", "Standard order: fill, filter, contacts, polish.", "Filter noise, never performance.", "Find the cycle, blend the seam.", "Mirror for variety; mind asymmetry.", "Retiming without reshooting.", "Additive layers for directed changes.", "Background cycles from short takes.", "Live retarget to the character.", "Takes named, versioned, archived.", "Daily wand and floor calibration.", "Tight suit, markers fixed.", "Direct mocap like a stage play.", "Three gates: fill, contacts, acting.", "Biovision Hierarchy: skeleton + motion sections, plain text."];
var GROUPS=["Capture", "Cleanup", "Direction", "Formats", "Pipeline", "QC", "Rigging"];
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
window['JAHDB_GEN_human_motion_capture']={generate:generate};
})();
