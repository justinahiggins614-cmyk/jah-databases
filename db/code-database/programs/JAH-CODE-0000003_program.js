/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-database · Record: JAH-CODE-0000003 · Deep clone — recursive (Javascript)
 * Runnable code from this record ("code") — executes with console output captured.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
"use strict";
/* ---- record code (code) ---- */
function clone(v) {
  if (Array.isArray(v)) return v.map(clone);
  if (v && typeof v === "object") {
    const o = {};
    for (const k of Object.keys(v)) o[k] = clone(v[k]);
    return o;
  }
  return v;
}
const a = { x: [1, { y: 2 }] };
const b = clone(a);
b.x[1].y = 99;
console.log(a.x[1].y, b.x[1].y);
/* ---- auto-run: call main/demo/solve if the snippet defines one ---- */
try{
  if(typeof main==="function"){console.log("--- main() output ---");main();}
  else if(typeof demo==="function"){console.log("--- demo() output ---");demo();}
  else if(typeof solve==="function"){console.log("--- solve() output ---");console.log(solve());}
}catch(e){console.log("runtime note: "+e.message);}
})();
