/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000019 · Banana Bread
 * Step-by-step simulation of "steps" (5 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Heat the oven to 350°F. Grease a 9x5-inch loaf pan.","detail":""},{"n":2,"label":"Whisk together the 1 3/4 cups all-purpose flour, 1/2 teaspoon baking s…","detail":""},{"n":3,"label":"In another bowl, whisk the 1 cup sugar, 2 eggs, 1 1/2 cups mashed ripe…","detail":""},{"n":4,"label":"Pour wet into dry and stir just until combined — a few lumps are fine.…","detail":""},{"n":5,"label":"Bake 60 minutes, until a toothpick in the center comes out clean. Cool…","detail":""}];
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
