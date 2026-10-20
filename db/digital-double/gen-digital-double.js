(function(){'use strict';
/* Signature Digital Double Database generator — jahdb-digital-double-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-DOUBLE-';
var LAST='2026-10-19';
var TITLES=["Digital Double: June Halla", "Digital Double: Mara Voss", "Digital Double: Ilsa Renn", "Digital Double: Rey Castil", "Digital Double: Ash Korvac", "Digital Double: Mara Voss", "Digital Double: Mara Voss", "Digital Double: Mara Voss", "Digital Double: Mara Voss", "Digital Double: Ash Korvac", "Digital Double: June Halla", "Digital Double: Kato Merid", "Digital Double: Nova Lind", "Digital Double: Ash Korvac", "Digital Double: Rey Castil", "Digital Double: Ilsa Renn", "Digital Double: Mara Voss", "Digital Double: Ash Korvac", "Digital Double: Mara Voss", "Digital Double: Ash Korvac", "Digital Double: Dev Okafor", "Digital Double: Rey Castil", "Digital Double: Nova Lind", "Digital Double: Kato Merid", "Digital Double: Ash Korvac", "Digital Double: Mara Voss", "Digital Double: Ash Korvac", "Digital Double: June Halla", "Digital Double: Mara Voss", "Digital Double: Rey Castil"];
var DEFS=["An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain.", "An authorized digital-double specification with scan, rig and approval chain."];
var GROUPS=["Double spec"];
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
window['JAHDB_GEN_digital_double']={generate:generate};
})();
