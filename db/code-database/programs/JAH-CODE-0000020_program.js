/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-database · Record: JAH-CODE-0000020 · Flatten nested arrays (Javascript)
 * Runnable code from this record ("code") — executes with console output captured.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
"use strict";
/* ---- record code (code) ---- */
function flat(a) {
  return a.reduce((o, x) => o.concat(Array.isArray(x) ? flat(x) : x), []);
}
console.log(flat([1, [2, [3, 4], 5], 6]).join(","));
/* ---- auto-run: call main/demo/solve if the snippet defines one ---- */
try{
  if(typeof main==="function"){console.log("--- main() output ---");main();}
  else if(typeof demo==="function"){console.log("--- demo() output ---");demo();}
  else if(typeof solve==="function"){console.log("--- solve() output ---");console.log(solve());}
}catch(e){console.log("runtime note: "+e.message);}
})();
