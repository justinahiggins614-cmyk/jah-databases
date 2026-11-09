/* JAH interactive demo program — jahdb-demo-1.0
 * Database: laws-compliance · Record: JAH-LAW-0000017 · Securities Act of 1933 — Statute profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-LAW-0000017","title":"Securities Act of 1933 — Statute profile","subject":"Securities Act of 1933","category":"statutes","record_type":"profile","source":"online","source_ref":"https://en.wikipedia.org/wiki/List_of_United_States_federal_legislation,_1901–2001","creation_mode":"ONLINE-CURATED","summary":"Securities Act of 1933 is a statute of United States enacted in 1933, in the area of securities. Requires registration and disclosure for public offerings of securities. It is formally cited as 48 Sta…","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"General information only, not legal advice. Use the citation to look up the current official text; statutes are amended over time."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Securities Act of 1933 — Statute profile ===");
console.log("Record JAH-LAW-0000017 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
