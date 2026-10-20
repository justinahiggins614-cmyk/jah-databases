(function(){'use strict';
/* Signature Crowd Behavior Database generator — jahdb-crowd-behavior-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-CROWD-';
var LAST='2026-10-19';
var TITLES=["Panic Egress", "Protest Surge", "Station Rush", "Festival Drift", "Queue Discipline", "Riot Climb", "Evacuation Order", "Sidewalk Commute", "Beach Scatter", "Museum Drift", "Stadium Wave", "Crosswalk Pulse", "Nightclub Pack", "Airport Flow", "Refugee Column", "Parade Route", "Black Friday Surge", "Park Stroll", "Construction Crew", "School Release", "Wedding Mixer", "Funeral Procession", "Marathon Pack", "Market Haggle", "Subway Car", "Elevator Silence", "Flash Mob", "Zombie Horde", "Victory Crowd", "Market Flow"];
var DEFS=["Exits attract; herding amplifies.", "Chanting mass with banner anchors.", "Pulsed by train arrivals.", "Low urgency, attraction points.", "Single file with service points.", "Aggression waves, projectile arcs.", "Directed flow, marshals at nodes.", "Lane discipline, overtaking.", "No paths; attraction to water.", "Slow, exhibit-anchored, quiet.", "Coordinated standing wave.", "Signal-gated bursts.", "Dense, beat-synced micro-motion.", "Signage-directed, luggage-slowed.", "Single direction, burdened, slow.", "Lined route, float anchors.", "Door-rush, high urgency.", "Diffuse, leisurely, dog walkers.", "Task-anchored clusters.", "Burst then scatter.", "Clustered conversation islands.", "Slow column, black mass.", "Paced groups, thinning.", "Stall-anchored dyads.", "Packed, still, phone-lit.", "Packed, eyes forward.", "Stillness to sync eruption.", "Shambling convergence.", "Jumping unison, confetti.", "Bidirectional streams with eddy zones at stalls."];
var GROUPS=["Crowd"];
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
window['JAHDB_GEN_crowd_behavior']={generate:generate};
})();
