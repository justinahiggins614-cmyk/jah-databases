/* JAH interactive demo program — jahdb-demo-1.0
 * Database: film-video · Record: JAH-FILM-0000023 · Two Shot (2S)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"shots","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Two Shot (2S)","topic":"shot type","shot":{"(object keys)":["shot","abbr","framing","purpose"]},"source_ref":"https://www.adobe.com/vn_en/creativecloud/video/production/cinematography/camera-shots-and-angles.html","description":"The Two Shot (2S) frames two subjects in one frame. Relationship between characters. A standard shot in the cinematographer’s vocabulary. Filed as a complete searchable record in the JAH Data Bases ar…","id":"JAH-FILM-0000023"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Two Shot (2S) ===");
console.log("Record JAH-FILM-0000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
