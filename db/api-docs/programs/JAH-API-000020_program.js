/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000020 · rhymes
 * Runnable mock of the "rhymes" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"rhymes","description":"Lists words rhyming with the input.","parameters":{"word":{"type":"string","description":"The word to rhyme."},"limit":{"type":"integer","description":"Max results (default 20)."}},"error_codes":[{"code":"E_NOTFOUND","meaning":"No rhymes found."},{"code":"E_INTERNAL","meaning":"An unexpected internal error occurred."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"rhymes\":[\"hat\",\"bat\",\"mat\"]}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.dict.rhymes({word:\"cat\",limit:3})");
console.log("--- live mock run ---");
call({"word":"demo","limit":1});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
