/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000022 · Chocolate Chip Cookies
 * Step-by-step simulation of "steps" (5 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Heat the oven to 350°F. Line baking sheets with parchment.","detail":""},{"n":2,"label":"Beat the 3/4 cup butter, softened with the 3/4 cup brown sugar and 1/4…","detail":""},{"n":3,"label":"Beat in the 2 eggs, 1 teaspoon vanilla extract.","detail":""},{"n":4,"label":"Stir in the 1 1/2 cups all-purpose flour, 1 teaspoon baking soda, 1 te…","detail":""},{"n":5,"label":"Scoop rounded tablespoons 2 inches apart. Bake 12 minutes until edges …","detail":""}];
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
