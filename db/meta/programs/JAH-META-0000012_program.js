/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000012 · Keystone Social Realm Prime
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000012","title":"Keystone Social Realm Prime","signature_name":"Keystone Social Realm Prime","alludes_to":"Meta AI — conversational assistant","class":1,"category":"platforms","specs":{"(object keys)":["surfaces","model","cost","platforms"]},"description":"Meta AI — conversational assistant is the nominative anchor for this record. The Keystone Social Realm Prime carries the same working details — built into WhatsApp, Messenger, Instagram and Facebook —…","year":2023};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Keystone Social Realm Prime ===");
console.log("Record JAH-META-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
