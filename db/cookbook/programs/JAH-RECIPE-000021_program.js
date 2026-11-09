/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000021 · Dinner Rolls
 * Step-by-step simulation of "steps" (5 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Stir the 2 teaspoons active dry yeast and 1 tablespoon sugar into the …","detail":""},{"n":2,"label":"Add the 4 cups bread flour, 1 1/2 teaspoons salt, and 3 tablespoons ol…","detail":""},{"n":3,"label":"Cover and rise in a warm spot about 1 hour, until doubled.","detail":""},{"n":4,"label":"Punch down, shape as desired, and rise 30 minutes more.","detail":""},{"n":5,"label":"Bake at 375°F for 25 minutes until deep golden and hollow-sounding whe…","detail":""}];
function render(i){
  var s=STEPS[i];if(!s){console.log("no step "+i);return;}
  var pct=Math.round(((i+1)/STEPS.length)*100);
  var filled=Math.round(pct/5), bar2="█".repeat(filled)+"░".repeat(20-filled);
  console.log("\n[step "+s.n+"/"+STEPS.length+"] "+bar2+" "+pct+"%");
  console.log("  "+s.label);
  if(s.detail)console.log("  → "+s.detail);
}
console.log("Simulating steps — "+STEPS.length+" steps");
for(var i=0;i<STEPS.length;i++)render(i);
try{globalThis.jahDemoAPI={render:render};}catch(e){}
console.log("\nSimulation complete ✓  Try: jahDemoAPI.render(0) to replay step 1.");
})();
