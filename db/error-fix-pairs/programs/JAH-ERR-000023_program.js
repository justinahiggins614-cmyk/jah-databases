/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000023 · Cannot connect to the Docker daemon at unix:///var/run/docke…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000023","error_id":"JAH-ERR-000023","error_text":"Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?","context":"Every docker command fails to reach the daemon.","root_cause":"The Docker daemon is not running (or the user cannot reach its socket).","fix":"Start Docker Desktop / `sudo systemctl start docker`; on Linux, add your user to the `docker` group.","language_or_tool":"docker","severity":"critical","title":"Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docke"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is… ===");
console.log("Record JAH-ERR-000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
