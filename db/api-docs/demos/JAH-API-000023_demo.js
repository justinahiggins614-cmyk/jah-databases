/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000023 · fetch_chunk
 * Runnable mock of the "fetch_chunk" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"fetch_chunk","description":"Fetches one archive chunk by number.","parameters":{"database":{"type":"string","description":"Database slug."},"chunk":{"type":"integer","description":"Chunk number, 1-based."}},"error_codes":[{"code":"E_DB","meaning":"Unknown database slug."},{"code":"E_CHUNK","meaning":"Chunk number out of range."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"records\":[{...}],\"chunk\":3}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.data.fetch_chunk({database:\"unit-tests\",chunk:3})");
console.log("--- live mock run ---");
call({"database":"demo","chunk":1});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
