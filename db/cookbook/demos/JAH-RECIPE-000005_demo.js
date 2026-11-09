/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cookbook · Record: JAH-RECIPE-000005 · Chicken Noodle Soup
 * Step-by-step simulation of "steps" (5 steps).
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var STEPS=[{"n":1,"label":"Heat the 2 tablespoons butter in a large pot over medium heat. Add the…","detail":""},{"n":2,"label":"Pour in the 4 cups beef broth and add the 1 cup diced chicken breast, …","detail":""},{"n":3,"label":"Reduce the heat to low, cover partially, and simmer 40 minutes, until …","detail":""},{"n":4,"label":"Remove any bay leaf. Season with the 1/4 teaspoon salt, 1/2 teaspoon b…","detail":""},{"n":5,"label":"Ladle into warm bowls, top with 2 tablespoons cilantro, and serve hot.","detail":""}];
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
