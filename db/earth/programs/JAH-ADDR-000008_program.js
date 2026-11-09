/* JAH interactive demo program — jahdb-demo-1.0
 * Database: earth · Record: JAH-ADDR-000008 · JAH-ADDR-000008
 * Charts this record's numeric fields as ASCII bars with summary statistics.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var N={"lat":33.6879358,"lon":-117.7591356,"osm_place_id":317432873};
var ks=Object.keys(N);
var mx=Math.max.apply(null,ks.map(function(k){return Math.abs(N[k]);}).concat([1]));
function bar(k){var v=N[k];var n=Math.round(Math.abs(v)/mx*36);console.log(k.padEnd(18," ").slice(0,18)+" | "+(v<0?"-":"")+"#".repeat(n)+" "+v);}
console.log("=== JAH-ADDR-000008 ===");
ks.forEach(bar);
var vs=ks.map(function(k){return N[k];});
var sum=vs.reduce(function(a,b){return a+b;},0);
console.log("--- stats ---");
console.log("count "+vs.length+" · sum "+(+sum.toFixed(4))+" · mean "+(+(sum/vs.length).toFixed(4))+" · max "+Math.max.apply(null,vs)+" · min "+Math.min.apply(null,vs));
function whatif(f){console.log("scaled ×"+f+":");ks.forEach(function(k){console.log("  "+k+": "+N[k]+" → "+(+(N[k]*f).toFixed(4)));});}
try{globalThis.jahDemoAPI={whatif:whatif};}catch(e){}
console.log("Try: jahDemoAPI.whatif(2)  — scales every value and re-prints.");
})();
