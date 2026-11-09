/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000009 · ERROR: column reference "id" is ambiguous
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000009","error_id":"JAH-ERR-000009","error_text":"ERROR: column reference \"id\" is ambiguous\nLINE 851: SELECT id FROM users JOIN orders ON users.id = orders.user_id;","context":"A join query cannot tell which `id` is meant.","root_cause":"Both joined tables have an `id` column and the select list does not qualify it.","fix":"Qualify every column: `SELECT users.id ...` (or alias the tables and use the aliases).","language_or_tool":"sql","severity":"low","title":"ERROR: column reference \"id\" is ambiguous"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== ERROR: column reference \"id\" is ambiguous ===");
console.log("Record JAH-ERR-000009 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
