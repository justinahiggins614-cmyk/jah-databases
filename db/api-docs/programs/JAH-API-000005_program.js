/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000005 · stats
 * Runnable mock of the "stats" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"stats","description":"Returns storage stats for a database.","parameters":{"database":{"type":"string","description":"Database slug."},"detail":{"type":"boolean","description":"Include per-chunk breakdown (default false)."}},"error_codes":[{"code":"E_DB","meaning":"Unknown database slug."},{"code":"E_INTERNAL","meaning":"An unexpected internal error occurred."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"records\":10000,\"chunks\":100,\"bytes_gz\":2450000}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.data.stats({database:\"embedding-chunks\"})");
console.log("--- live mock run ---");
call({"database":"demo","detail":true});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
