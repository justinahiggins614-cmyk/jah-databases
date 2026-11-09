/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000007 · calculate
 * Runnable mock of the "calculate" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"calculate","description":"Evaluates a math expression and returns the result.","parameters":{"expression":{"type":"string","description":"The expression to evaluate, e.g. \"2*(3+4)\"."},"precision":{"type":"integer","description":"Decimal places in the result (default 6)."},"angle":{"type":"string","description":"\"deg\" or \"rad\" for trig functions (default \"deg\")."}},"error_codes":[{"code":"E_SYNTAX","meaning":"The expression could not be parsed."},{"code":"E_DIVZERO","meaning":"Division by zero encountered."},{"code":"E_DOMAIN","meaning":"Function argument outside its domain."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"result\":20,\"precision\":6}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.math.calculate({expression:\"sqrt(144)+2^3\"})");
console.log("--- live mock run ---");
call({"expression":"demo","precision":1,"angle":"demo"});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
