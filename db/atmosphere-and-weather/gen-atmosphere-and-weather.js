(function(){'use strict';
/* Public Atmosphere and Weather Database generator — jahdb-atmosphere-and-weather-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-ATMOS-';
var LAST='2026-10-19';
var TITLES=["Heavy Fog", "Light Haze", "Rain: Drizzle", "Rain: Downpour", "Rain: Storm", "Snow: Flurry", "Snow: Blizzard", "Dust Storm", "Sand Drift", "Smoke: Thin", "Smoke: Thick", "Steam", "Mist on Water", "Heat Shimmer", "Wind: Gentle", "Wind: Gale", "Embers", "Ash Fall", "Pollen Drift", "Ocean Spray", "Morning Dew", "Frost Breath", "Cloud Time-Lapse", "Lightning Distant", "Rainbow Moment", "Haboob Wall", "Ice Fog", "Volcanic Ash", "Bioluminescent Mist", "Ground Fog"];
var DEFS=["White-out: figures emerge.", "Beams become visible.", "Fine mist, barely visible.", "Sheets of water, drama.", "Wind-driven, violent.", "Gentle flakes.", "White chaos.", "Brown-out: the world vanishes.", "Desert wind, low sand.", "Battle haze.", "Fire aftermath.", "Urban alleys, manholes.", "Dawn lakes.", "Mirage on hot roads.", "Hair and cloth move.", "Bodies lean.", "Fire aftermath particles.", "Grey snow of disaster.", "Golden motes in shafts.", "Coast drama.", "Sparkle on grass.", "Cold made visible.", "Sky as character.", "Storm on the horizon.", "Hope after storm.", "Dust wall approaching.", "Arctic breath of the air.", "Grey apocalypse.", "Fantasy glow fog.", "Low-lying fog: mystery at ankle height."];
var GROUPS=["Atmosphere", "Weather"];
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
window['JAHDB_GEN_atmosphere_and_weather']={generate:generate};
})();
