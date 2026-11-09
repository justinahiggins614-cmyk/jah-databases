/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000023 · Vanilla Cake
 * Step-by-step simulation of "steps" (5 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Heat the oven to 350°F. Grease and flour two 8-inch round pans.","detail":""},{"n":2,"label":"Whisk the 1 1/2 cups all-purpose flour, 1 cup granulated sugar, 2 teas…","detail":""},{"n":3,"label":"Add the 2 eggs, 3/4 cup milk, 1/2 cup vegetable oil, 1/2 teaspoon vani…","detail":""},{"n":4,"label":"Divide between pans and bake 28 minutes, until a toothpick comes out c…","detail":""},{"n":5,"label":"Cool 10 minutes in pans, then turn out and cool completely before fros…","detail":""}];
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
