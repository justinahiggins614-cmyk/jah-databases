(function(){'use strict';
/* Signature Director Intelligence Database generator — jahdb-director-intelligence-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-DIRECT-';
var LAST='2026-10-19';
var TITLES=["Tone Calibration", "Visual Strategy", "Performance Direction", "Rehearsal Method", "Blocking Grammar", "Coverage Philosophy", "Take Discipline", "Set Communication", "Department Alignment", "Casting Eye", "Child Direction", "Non-actor Direction", "Stunt Direction", "VFX Direction", "Comedy Direction", "Horror Direction", "Drama Direction", "Action Direction", "Musical Direction", "Improvisation", "Silence Direction", "Montage Direction", "Ending Direction", "Reshoot Judgment", "Edit Collaboration", "Composer Collaboration", "Color Collaboration", "Master Director Bible", "Vision Statement", "Tone Calibration"];
var DEFS=["The film's temperature.", "How it looks.", "Actors.", "Prepare.", "Bodies tell.", "How much.", "How many.", "Clear orders.", "All serve vision.", "Faces with history.", "Young actors.", "Real people.", "Safe and clear.", "Imagined worlds.", "Timing.", "Dread.", "Truth.", "Geography.", "Counts.", "Controlled.", "Held beats.", "Image chains.", "The button.", "When.", "The final rewrite.", "Music.", "Look.", "One method.", "One sentence every department serves.", "The film's temperature."];
var GROUPS=["Direction"];
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
window['JAHDB_GEN_director_intelligence']={generate:generate};
})();
