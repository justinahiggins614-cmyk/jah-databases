/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000009 · Greek Salad
 * Step-by-step simulation of "steps" (4 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Wash and dry the 4 cups chopped romaine and place in a large salad bow…","detail":""},{"n":2,"label":"Add the 2/3 cup chopped walnuts, 1/3 cup sliced strawberries, 1 cup sl…","detail":""},{"n":3,"label":"In a small jar, shake together the 1/2 tablespoon olive oil, 3 tablesp…","detail":""},{"n":4,"label":"Pour the dressing over the salad and toss gently until everything is l…","detail":""}];
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
