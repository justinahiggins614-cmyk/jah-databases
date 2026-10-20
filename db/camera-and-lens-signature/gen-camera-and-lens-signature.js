(function(){'use strict';
/* Signature Camera and Lens Database generator — jahdb-camera-and-lens-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-CAMS-';
var LAST='2026-10-19';
var TITLES=["Signature Hyperfocal Discipline", "Signature Bokeh Casting", "Signature Lens Bible", "Signature Vintage Character Glass", "Signature Anamorphic Intent", "Signature Focus Pull Choreography", "Signature Deep Focus Statements", "Signature Shallow Isolation", "Signature Lens Change Ritual", "Signature Zoom Restraint", "Signature Macro Intent", "Signature Telephoto Compression", "Signature Wide Honesty", "Signature Normal Restraint", "Signature Lens Flare Control", "Signature Breathing Check", "Signature T-Stop Truth", "Signature Lens QC", "Signature Lens Archive", "Signature Lens Teaching", "Signature DOF Preview", "Signature Split Diopter Craft", "Signature Lens Repair Loop", "Signature Lens Master Index", "Signature Glass Generator"];
var DEFS=["Focus at H for infinite depth; verify on the monitor, never guess.", "Choose blur character like casting: smooth for romance, nervous for tension.", "One lens list per production; rentals matched to the bible.", "Period stories get period aberrations: documented, not accidental.", "Squeeze only when the story is wider than the frame.", "Pulls rehearsed like dance; marks on the floor, not hope.", "Deep focus when the background is a character.", "Shallow depth when the world must fall away.", "Lens changes logged; the why recorded for the edit.", "Zooms are moves with meaning, never coverage laziness.", "Macro only for the detail that turns the story.", "Compression stacks layers: use for surveillance and fate.", "Wides show the truth of the space; no hiding.", "50mm for scenes that need no comment.", "Flares motivated by sources; flagged in the plan.", "Focus breathing tested per lens; compensated in the grade.", "Expose by T-stop, not f-stop: honesty in low light.", "Every rental tested: chart, flare, breathing.", "Approved glass archived with character notes.", "Focal length is a storytelling decision first.", "DOF previewed on set at shooting aperture.", "Split field when both planes are story.", "Soft or breathing failures trigger re-shoots or re-grades.", "One index of all glass, character and approvals.", "Deterministic lens packages from story parameters."];
var GROUPS=["Signature method"];
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
window['JAHDB_GEN_camera_and_lens_signature']={generate:generate};
})();
