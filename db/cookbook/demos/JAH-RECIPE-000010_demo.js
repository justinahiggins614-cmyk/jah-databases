/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000010 · Roast Chicken
 * Step-by-step simulation of "steps" (4 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Heat the oven to 425°F. Pat the 1 pound whole chicken dry with paper t…","detail":""},{"n":2,"label":"Rub all over with 2 tablespoons olive oil and season generously with 1…","detail":""},{"n":3,"label":"Scatter the 2 1/2 cups carrots around the pan. Roast 45 minutes, until…","detail":""},{"n":4,"label":"Rest 10 minutes before slicing so the juices settle. Serve warm.","detail":""}];
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
