/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000001 · mean
 * Runnable mock of the "mean" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"mean","description":"Arithmetic mean of a list of numbers.","parameters":{"values":{"type":"array","description":"Non-empty array of finite numbers."},"round":{"type":"integer","description":"Decimal places in the result (default 6)."}},"error_codes":[{"code":"E_EMPTY","meaning":"The values array is empty."},{"code":"E_VALUE","meaning":"A value is not finite."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"result\":4}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.math.mean({values:[2,4,6]})");
console.log("--- live mock run ---");
call({"values":[],"round":1});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
