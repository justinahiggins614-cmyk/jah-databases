(function(){'use strict';
/* Public Camera Movement Database generator — jahdb-camera-movement-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-CAMMOVE-';
var LAST='2026-10-19';
var TITLES=["Pan", "Tilt", "Dolly In", "Dolly Out", "Tracking Lateral", "Crane Up", "Crane Down", "Arc Shot", "Steadicam Follow", "Gimbal Orbit", "Drone Ascent", "Drone Push", "Handheld Intimacy", "Whip Pan", "Whip Tilt", "Slow Push Dread", "Pull Back Reveal", "Circle of Dread", "Vertigo Dolly-Zoom", "SnorriCam", "Car Mount Chase", "Cable Cam", "Underwater Drift", "Slider Micro", "Motion Control Pass", "FPV Dive", "Pedestal Move", "Compound Move", "Stillness as Move", "Static Lock-Off"];
var DEFS=["Horizontal rotation on a fixed axis.", "Vertical rotation: reveal height.", "Track forward: intimacy approaches.", "Track back: the world widens.", "Side track with the subject.", "Rise above: the god view.", "Descend into the scene.", "Camera orbits the subject.", "Floating follow through space.", "Stabilized 360 around action.", "Rising aerial: the world map.", "Forward flight through space.", "Shoulder-held: presence and nerves.", "Fast pan: energy and transition.", "Fast vertical: the drop.", "Inexorable approach.", "Widening reveals the trap.", "Slow orbit tightening.", "Dolly in, zoom out: the world warps.", "Camera rigged to the actor.", "Rigged to the vehicle.", "Wire-suspended lateral flight.", "Housed camera floating.", "Short track for tabletop.", "Repeatable robotic moves for VFX.", "First-person drone: the plunge.", "Column rise/fall in studio.", "Dolly + pan + tilt in one.", "The cut is the move.", "No movement: the world acts, the camera witnesses."];
var GROUPS=["Move"];
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
window['JAHDB_GEN_camera_movement']={generate:generate};
})();
