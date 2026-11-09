/* JAH interactive demo program — jahdb-demo-1.0
 * Database: api-docs · Record: JAH-API-000006 · stop_audio
 * Runnable mock of the "stop_audio" endpoint — validates args, returns the documented example response.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var SPEC={"name":"stop_audio","description":"Stops all audio playback on the page.","parameters":{"fade_ms":{"type":"integer","description":"Fade-out duration in ms (default 0)."},"session":{"type":"string","description":"Optional session id to stop."}},"error_codes":[{"code":"E_AUDIO","meaning":"Audio engine unavailable."},{"code":"E_STATE","meaning":"Nothing is playing."}]};
function call(args){
  args=args||{};
  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");
  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});
  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}
  var resp="{\"stopped\":true}";
  console.log("< "+resp);
  return resp;
}
console.log("API: "+SPEC.name+" — "+SPEC.description);
console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));
console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));
console.log("--- documented example ---");
console.log("call: jahdb.media.stop_audio()");
console.log("--- live mock run ---");
call({"fade_ms":1,"session":"demo"});
console.log("Tip: call your own args and watch the mock validate + respond.");
})();
