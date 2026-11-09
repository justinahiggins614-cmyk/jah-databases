/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000011 · generate
 * Runnable mock of the "generate" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"generate","description":"Generates a deterministic record by seed.","parameters":{"database":{"type":"string","description":"Database slug."},"seed":{"type":"integer","description":"Seed."},"category":{"type":"string","description":"Optional category."}},"error_codes":[{"code":"E_DB","meaning":"Unknown database slug."},{"code":"E_GEN","meaning":"No generator registered."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"record\":{...},\"version\":\"jahdb-error-fix-pairs-1.0\"}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.data.generate({database:\"error-fix-pairs\",seed:42})");
console.log("--- live mock run ---");
call({"database":"demo","seed":1,"category":"demo"});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
