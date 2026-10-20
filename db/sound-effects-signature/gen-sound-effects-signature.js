(function(){'use strict';
/* Signature Sound Effects Database generator — jahdb-sound-effects-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-SFXS-';
var LAST='2026-10-19';
var TITLES=["Signature Recording First", "Signature Layer Discipline", "Signature Sync Tolerance", "Signature Perspective Truth", "Signature Sub-Bass Care", "Signature Transient Priority", "Signature Tail Honesty", "Signature Variation", "Signature Taste", "Signature Silence Design", "Signature Slow-Mo Honesty", "Signature Underwater Muffle", "Signature Dream Unreality", "Signature Horror Rarity", "Signature Comedy Taste", "Signature Library Order", "Signature License Clean", "Signature SFX QC", "Signature SFX Repair", "Signature SFX Teaching", "Signature SFX Archive", "Signature SFX Versioning", "Signature SFX Master Index", "Signature SFX Generator", "Signature Final SFX Pass"];
var DEFS=["Real recordings before synthesis.", "Three layers deep minimum.", "±2 frames.", "Distance in tone and level.", "Felt, not just heard.", "Attacks sell impacts.", "Rooms have tails.", "No machine-gun repeats.", "Restraint.", "Absence as effect.", "Stretched with detail.", "Submerged true.", "Unreal with intent.", "Stingers rare.", "Cartoon with control.", "Findable.", "All cleared.", "Three gates.", "Failed syncs redone.", "Listen first.", "Stored.", "Kept.", "One index.", "Deterministic recipes.", "The last listen."];
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
window['JAHDB_GEN_sound_effects_signature']={generate:generate};
})();
