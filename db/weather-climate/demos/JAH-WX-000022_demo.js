/* JAH interactive demo program — jahdb-demo-1.0
 * Database: weather-climate · Record: JAH-WX-000022 · Pine Grove Observatory
 * Station report: converts units and charts this observation.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var R={"station":"Pine Grove Observatory","lat":31.18,"lon":88.11,"time":"2024-02-04T04:15:00Z","temp_c":-15.52,"humidity":95,"precip_mm":11.69,"condition":"snow"};
function cToF(c){return c*9/5+32;}
function mmToIn(m){return m/25.4;}
function bar(label,val,max,w){var n=Math.max(0,Math.round(val/max*w));console.log(label.padEnd(12," ")+"|"+"#".repeat(n)+" "+val);}
console.log("Station: "+R.station+" ("+R.lat+", "+R.lon+")");
console.log("Time: "+R.time+" · Condition: "+R.condition);
console.log(R.temp_c+"°C = "+cToF(R.temp_c).toFixed(1)+"°F · humidity "+R.humidity+"% · precip "+R.precip_mm+"mm ("+mmToIn(R.precip_mm).toFixed(2)+"in)");
console.log("--- observation chart ---");
bar("temp(C)",R.temp_c,40,30);bar("humidity%",R.humidity,100,30);bar("precip(mm)",R.precip_mm,50,30);
console.log("Try: cToF(20), mmToIn(25.4)");
})();
