(function(){'use strict';
/* Public Music and Sound Rights Database generator — jahdb-music-and-sound-rights-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-RIGHTS-';
var LAST='2026-10-19';
var TITLES=["Work for Hire", "Licensing: Sync", "Licensing: Master", "Library Music", "Public Domain", "Creative Commons", "Cue Sheets", "PRO Registration", "Sound Recording Rights", "Sample Clearance", "Foley Ownership", "SFX Library Licenses", "Voice Contracts", "Composer Agreements", "Lyric Rights", "Adaptation Rights", "Territory", "Term", "Media", "Attribution", "Moral Rights", "Orphan Works", "Fair Use Limits", "Parody", "AI-Generated Music Rights", "Signature Originals Policy", "License Calendar", "Infringement Response", "Master Rights Bible", "Ownership Basics"];
var DEFS=["Production owns.", "Music to picture.", "Recording use.", "Pre-cleared.", "Free but verify.", "Check the license.", "Report usage.", "Collect royalties.", "Masters.", "Clear samples.", "Recorded foley.", "Bought sounds.", "Actors.", "Composers.", "Words.", "Arrangements.", "Where.", "How long.", "Which uses.", "Credit.", "Integrity.", "Unknown owners.", "Narrow.", "Comment.", "New frontier.", "JAH owns.", "Renewals tracked.", "If accused.", "One method.", "Who owns what."];
var GROUPS=["Rights"];
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
window['JAHDB_GEN_music_and_sound_rights']={generate:generate};
})();
