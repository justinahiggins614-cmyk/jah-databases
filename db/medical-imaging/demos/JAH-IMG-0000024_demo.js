/* JAH interactive demo program — jahdb-demo-1.0
 * Database: medical-imaging · Record: JAH-IMG-0000024 · fluoroscopy - typical parameters
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"fluoroscopy - typical parameters","category":"xray","description":"Modality (typical parameters): fluoroscopy - continuous X-ray imaging displayed in real time. Developed in the early 1900s for dynamic studies.","modality":"fluoroscopy","principle":"continuous X-ray imaging displayed in real time","indications":"[array ×2]","contraindications":"[array ×2]","protocol_steps":"[array ×3]","annotation_guidelines":"Label anatomy, mark findings with standard terms, and record acquisition parameters.","performance_notes":"Reference teaching notes; not measured clinical performance.","privacy_note":"Reference record. Contains no real patient data and no protected health information.","source":"online","source_ref":"https://www.acr.org/","creation_mode":"ONLINE-VERIFIED"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== fluoroscopy - typical parameters ===");
console.log("Record JAH-IMG-0000024 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
