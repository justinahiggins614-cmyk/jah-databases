/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000013 · prime_factors
 * Runnable mock of the "prime_factors" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"prime_factors","description":"Prime factorization of a positive integer.","parameters":{"n":{"type":"integer","description":"Integer from 2 to 10^12."},"unique":{"type":"boolean","description":"Return only unique factors (default false)."}},"error_codes":[{"code":"E_RANGE","meaning":"n outside 2..10^12."},{"code":"E_TYPE","meaning":"n is not an integer."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"factors\":[2,2,3,7]}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.math.prime_factors({n:84})");
console.log("--- live mock run ---");
call({"n":1,"unique":true});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
