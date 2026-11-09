/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-problems · Record: JAH-CODE-000015 · Write a JavaScript function that capitalizes the first lette…
 * Runnable code from this record ("solution_code") — executes with console output captured.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
"use strict";
/* ---- record code (solution_code) ---- */
function capitalize(s) {
  if (!s) return s;
  return s[0].toUpperCase() + s.slice(1);
}

console.log(capitalize("hello"));
/* ---- auto-run: call main/demo/solve if the snippet defines one ---- */
try{
  if(typeof main==="function"){console.log("--- main() output ---");main();}
  else if(typeof demo==="function"){console.log("--- demo() output ---");demo();}
  else if(typeof solve==="function"){console.log("--- solve() output ---");console.log(solve());}
}catch(e){console.log("runtime note: "+e.message);}
})();
