/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000014 · pronounce
 * Runnable mock of the "pronounce" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"pronounce","description":"Returns pronunciation guidance for a word.","parameters":{"word":{"type":"string","description":"The headword."},"dialect":{"type":"string","description":"\"us\" or \"uk\" (default \"us\")."}},"error_codes":[{"code":"E_NOTFOUND","meaning":"No entry for this headword."},{"code":"E_INTERNAL","meaning":"An unexpected internal error occurred."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"ipa\":\"/ˈdeɪtə/\",\"syllables\":\"da-ta\"}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.dict.pronounce({word:\"data\"})");
console.log("--- live mock run ---");
call({"word":"demo","dialect":"demo"});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
