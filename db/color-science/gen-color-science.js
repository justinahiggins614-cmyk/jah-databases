(function(){'use strict';
/* Public Color Science Database generator — jahdb-color-science-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-COLOR-';
var LAST='2026-10-19';
var TITLES=["Sunny 16 Rule", "18% Grey", "White Balance Kelvin", "sRGB vs Rec.709", "DCI-P3", "Rec.2020", "ACES Workflow", "Log vs Raw", "Bit Depth", "Chroma Subsampling", "Gamma Curves", "HDR: PQ vs HLG", "Contrast Ratio", "Skin Tone Line", "Luminance vs Luma", "Waveform Monitor", "Vectorscope", "Histogram", "False Color", "Color Temperature Shift", "Metamerism", "LED Color Spikes", "Printer Lights", "Look-Up Tables", "CDL Grades", "Dynamic Range", "Noise Floor", "Color Management", "Delivery Color Policy", "Exposure Triangle"];
var DEFS=["Bright sun: f/16, 1/ISO shutter.", "Meters calibrate to middle grey.", "Color temperature of sources.", "Delivery spaces for web and broadcast.", "Cinema projection gamut.", "UHD broadcast gamut.", "Scene-referred color management.", "Flat capture preserves latitude.", "8 vs 10 vs 12 bit banding.", "4:4:4 vs 4:2:2 vs 4:2:0.", "2.2, 2.4, 2.6 and PQ.", "Two HDR standards.", "White to black luminance.", "Skin lives on the vectorscope line.", "Y vs Y prime: know the difference.", "Luminance plotted per column.", "Hue and saturation plotted.", "Tonal distribution.", "Exposure as colors.", "Warming and cooling for story.", "Colors match under one light only.", "Cheap LEDs have spectral gaps.", "Traditional timing points.", "LUTs transform color deterministically.", "Slope, offset, power: portable grades.", "Stops from black to white.", "Shadow noise vs ISO.", "One managed pipeline end to end.", "Each platform gets its trim.", "Aperture, shutter, ISO: the three-way trade."];
var GROUPS=["Capture", "Color", "Delivery", "Exposure", "HDR", "Pipeline", "Scopes", "Spaces"];
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
window['JAHDB_GEN_color_science']={generate:generate};
})();
