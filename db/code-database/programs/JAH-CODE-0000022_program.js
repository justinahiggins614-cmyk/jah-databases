/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-database · Record: JAH-CODE-0000022 · Decorator — wrap with logging (Javascript)
 * Runnable code from this record ("code") — executes with console output captured.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
"use strict";
/* ---- record code (code) ---- */
function logged(fn, name) {
  return (...a) => {
    const r = fn(...a);
    console.log(name + ":" + r);
    return r;
  };
}
const add = logged((a, b) => a + b, "add");
add(2, 3);
/* ---- auto-run: call main/demo/solve if the snippet defines one ---- */
try{
  if(typeof main==="function"){console.log("--- main() output ---");main();}
  else if(typeof demo==="function"){console.log("--- demo() output ---");demo();}
  else if(typeof solve==="function"){console.log("--- solve() output ---");console.log(solve());}
}catch(e){console.log("runtime note: "+e.message);}
})();
