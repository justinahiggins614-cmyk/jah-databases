/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000004 · manifest
 * Runnable mock of the "manifest" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"manifest","description":"Returns the network manifest.","parameters":{"version":{"type":"string","description":"Manifest schema version to request."},"pretty":{"type":"boolean","description":"Pretty-print the JSON output."}},"error_codes":[{"code":"E_INTERNAL","meaning":"Manifest unreadable."},{"code":"E_VERSION","meaning":"Manifest version mismatch."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"databases\":[...],\"version\":\"1.0\"}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.route.manifest()");
console.log("--- live mock run ---");
call({"version":"demo","pretty":true});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
