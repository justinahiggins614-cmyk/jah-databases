(function(){'use strict';
/* Signature Color Science Database generator — jahdb-color-science-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-COLORS-';
var LAST='2026-10-19';
var TITLES=["Signature Exposure Discipline", "Signature White Balance Intent", "Signature Log Workflow", "Signature Skin Line Law", "Signature Scope Literacy", "Signature False Color Habit", "Signature HDR Intent", "Signature Gamut Plan", "Signature ACES Pipeline", "Signature LUT Versioning", "Signature CDL Travel", "Signature Monitor Calibration", "Signature Delivery Trims", "Signature Noise Budget", "Signature Bit Depth Floor", "Signature Chroma Policy", "Signature LED Testing", "Signature Mixed Source Plan", "Signature Exposure Archive", "Signature Color Teaching", "Signature Color QC Gates", "Signature Color Repair Loop", "Signature Printer Light Heritage", "Signature Color Master Index", "Signature Color Generator"];
var DEFS=["Expose for the grade: protect highlights, feed shadows.", "WB set per scene: mixed sources motivated.", "Shoot log, monitor with LUT, never bake.", "Skin on the line in every grade.", "Waveform and vectorscope on every setup.", "False color check before every take.", "HDR only when the story has highlights to show.", "Working gamut chosen at prep, never mid-shoot.", "Managed color end to end.", "Show LUTs versioned like code.", "CDLs travel with the edit.", "Probes monthly; no uncalibrated eyes.", "Each platform gets its own trim pass.", "Noise acceptable per scene: set at prep.", "10-bit minimum for graded work.", "4:2:2 minimum for keying and grading.", "Every LED tested on skin before the shoot.", "Mixed temps motivated or corrected.", "Exposure decisions logged with the takes.", "Science before style: measure first.", "Scopes pass before picture lock.", "Failed scope checks re-grade the shot.", "Dailies timed with printer-light discipline.", "One index of all transforms and approvals.", "Deterministic exposure plans from scene parameters."];
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
window['JAHDB_GEN_color_science_signature']={generate:generate};
})();
