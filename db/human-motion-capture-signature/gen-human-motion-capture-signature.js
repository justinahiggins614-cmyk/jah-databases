(function(){'use strict';
/* Signature Human Motion Capture Database generator — jahdb-human-motion-capture-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-MOCAPS-';
var LAST='2026-10-19';
var TITLES=["Signature Gap Zero Policy", "Signature Contact Lock", "Signature Retarget Truth", "Signature Additive Direction", "Signature Mocap QC Gates", "Signature Take Versioning", "Signature Crowd Take Bank", "Signature Finger Truth", "Signature Face-Body Sync", "Signature Stunt Honesty", "Signature Prop Contact", "Signature Mirror Discipline", "Signature Warp Limits", "Signature Real-Time Direction", "Signature Suit Protocol", "Signature Calibration Ritual", "Signature Data Naming Law", "Signature Select Archive", "Signature Mocap Teaching", "Signature Filter Restraint", "Signature Loop Seamless", "Signature Multi-Actor Choreo", "Signature Mocap Repair Loop", "Signature Mocap Master Index", "Signature Take Direction"];
var DEFS=["Selects ship with zero gaps: fill, spline, or reshoot.", "Feet plant: contacts detected and locked before any polish.", "Proportions matched, contacts preserved, acting intact.", "Changes layered additively; the base take is sacred.", "Fill, contacts, acting: three gates per select.", "Raw, clean, retargeted: three versions, one select.", "Background cycles banked with seeds for infinite variety.", "Hero hands get finger solves; no mitten acting in close-up.", "HMC synced to body take within one frame.", "Wire frames marked; physics kept honest in cleanup.", "Props parented to hands; interpenetration flagged.", "Mirrored takes labeled; asymmetric acting never mirrored.", "Retiming capped: acting rhythm is not negotiable.", "Director directs the character live, not the dots.", "Markers checked before every take; dead markers replaced.", "Wand and floor calibrated daily; test take validated.", "character_action_take_version: no exceptions.", "Selects archived with raw, clean, retarget and gates.", "Acting first, dots second: performers, not puppets.", "Filter noise only; the performance is never filtered.", "Cycles loop invisibly: pose-matched seams, planted feet.", "Interactions choreographed marker-safe before capture.", "Failed gates regenerate the solve with tightened constraints.", "One index of all takes, selects and approvals.", "Direct mocap like stage: block, shoot the acting, protect the best take."];
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
window['JAHDB_GEN_human_motion_capture_signature']={generate:generate};
})();
