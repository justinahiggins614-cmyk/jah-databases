(function(){'use strict';
/* Public Environmental Detail Database generator — jahdb-environmental-detail-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-ENVIR-';
var LAST='2026-10-19';
var TITLES=["Harbor Dawn", "Vault Interior", "Rooftop Dusk", "Desert Road", "Forest Clearing", "Subway Platform", "Abandoned Mall", "Space Station", "Medieval Alley", "Neon Alley", "Arctic Station", "Tropical Market", "Cathedral Nave", "Server Farm", "Film Studio Backlot", "Hospital Corridor", "School Hallway", "Diner Night", "Gas Station Desert", "Library Stacks", "Police Station", "Newsroom", "Theater Stage", "Boxing Gym", "Greenhouse", "Observatory", "Shipyard", "Village Square", "Airport Terminal", "Night Street"];
var DEFS=["Cranes, gulls, mist on water.", "Shelves, dust shafts, brass.", "City vista, vents, antenna.", "Heat shimmer, one gas station.", "Canopy shafts, ferns.", "Tile, ads, arriving train.", "Dead stores, skylight leaks.", "White modules, one red alarm.", "Cobbles, torch brackets.", "Signs stacked, steam.", "Modules on stilts, snow.", "Stalls, color, crowd.", "Shafts, scale, silence.", "Rack rows, LED blink.", "Facades, sky backing.", "Fluorescent, gurney marks.", "Lockers, posters.", "Neon window, pie case.", "One pump, buzzing sign.", "Tall shelves, dust.", "Desks, boards, buzz.", "Screens, deadline energy.", "Curtain, footlights.", "Ring, bags, sweat.", "Glass, plants, humidity.", "Dome, telescope, night.", "Cranes, hulls, sparks.", "Fountain, cafes.", "Glass, announcements.", "Wet asphalt, lit windows, practicals."];
var GROUPS=["Environment"];
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
window['JAHDB_GEN_environmental_detail']={generate:generate};
})();
