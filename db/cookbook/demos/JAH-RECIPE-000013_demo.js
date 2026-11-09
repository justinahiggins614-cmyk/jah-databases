/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000013 · Lasagna
 * Step-by-step simulation of "steps" (4 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Bring a large pot of salted water to a boil. Cook the 16 ounces lasagn…","detail":""},{"n":2,"label":"Meanwhile, heat the 2 tablespoons olive oil in a large skillet over me…","detail":""},{"n":3,"label":"Stir in the 1 3/4 cups Alfredo sauce and simmer 8 minutes, loosening w…","detail":""},{"n":4,"label":"Toss the pasta with the sauce, top with 2/3 cup ricotta, and serve imm…","detail":""}];
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
