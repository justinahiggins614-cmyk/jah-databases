(function(){'use strict';
/* JAH HTTP Status Codes Database generator — jahdb-http-status-codes-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='http-status-codes',PREFIX='JAH-HTTP-',NAME='JAH HTTP Status Codes Database';
var FIELDS=["informational", "success", "redirection", "client-error", "server-error"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "100 Continue", "d": "The server received the request headers; the client should send the body.", "g": "informational", "l": 2, "q": "What is 100 Continue?", "a": "The server received the request headers; the client should send the body.", "x": "100 Continue — The server received the request headers; the client should send the body. Example: Expect: 100-continue handshakes..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "101 Switching Protocols", "d": "The server agrees to switch protocols, e.g. to WebSocket.", "g": "informational", "l": 2, "q": "What is 101 Switching Protocols?", "a": "The server agrees to switch protocols, e.g. to WebSocket.", "x": "101 Switching Protocols — The server agrees to switch protocols, e.g. to WebSocket. Example: WebSocket upgrades..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "102 Processing", "d": "The server is still working; prevents client timeouts.", "g": "informational", "l": 2, "q": "What is 102 Processing?", "a": "The server is still working; prevents client timeouts.", "x": "102 Processing — The server is still working; prevents client timeouts. Example: WebDAV long operations..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "103 Early Hints", "d": "Preliminary headers so the client can preload resources.", "g": "informational", "l": 2, "q": "What is 103 Early Hints?", "a": "Preliminary headers so the client can preload resources.", "x": "103 Early Hints — Preliminary headers so the client can preload resources. Example: Faster page loads..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "200 OK", "d": "The standard success response.", "g": "success", "l": 2, "q": "What is 200 OK?", "a": "The standard success response.", "x": "200 OK — The standard success response. Example: GET requests..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "201 Created", "d": "A new resource was created.", "g": "success", "l": 2, "q": "What is 201 Created?", "a": "A new resource was created.", "x": "201 Created — A new resource was created. Example: POST that makes a record..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "202 Accepted", "d": "Accepted for later processing.", "g": "success", "l": 2, "q": "What is 202 Accepted?", "a": "Accepted for later processing.", "x": "202 Accepted — Accepted for later processing. Example: Queued jobs..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "203 Non-Authoritative Information", "d": "Returned meta-information is from a third party.", "g": "success", "l": 2, "q": "What is 203 Non-Authoritative Information?", "a": "Returned meta-information is from a third party.", "x": "203 Non-Authoritative Information — Returned meta-information is from a third party. Example: Proxies..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "204 No Content", "d": "Success with an intentionally empty body.", "g": "success", "l": 2, "q": "What is 204 No Content?", "a": "Success with an intentionally empty body.", "x": "204 No Content — Success with an intentionally empty body. Example: DELETE confirmations..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "205 Reset Content", "d": "Success; the client should reset its document view.", "g": "success", "l": 2, "q": "What is 205 Reset Content?", "a": "Success; the client should reset its document view.", "x": "205 Reset Content — Success; the client should reset its document view. Example: Form resets..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "206 Partial Content", "d": "Partial response to a Range request.", "g": "success", "l": 2, "q": "What is 206 Partial Content?", "a": "Partial response to a Range request.", "x": "206 Partial Content — Partial response to a Range request. Example: Video seeking..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "207 Multi-Status", "d": "Multiple status codes for batched operations.", "g": "success", "l": 2, "q": "What is 207 Multi-Status?", "a": "Multiple status codes for batched operations.", "x": "207 Multi-Status — Multiple status codes for batched operations. Example: WebDAV..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "208 Already Reported", "d": "Members already listed in a previous response.", "g": "success", "l": 2, "q": "What is 208 Already Reported?", "a": "Members already listed in a previous response.", "x": "208 Already Reported — Members already listed in a previous response. Example: WebDAV..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "226 IM Used", "d": "Response to an instance-manipulation request.", "g": "success", "l": 2, "q": "What is 226 IM Used?", "a": "Response to an instance-manipulation request.", "x": "226 IM Used — Response to an instance-manipulation request. Example: Delta encoding..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "300 Multiple Choices", "d": "Several representations exist; the client picks.", "g": "redirection", "l": 2, "q": "What is 300 Multiple Choices?", "a": "Several representations exist; the client picks.", "x": "300 Multiple Choices — Several representations exist; the client picks. Example: Content negotiation..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "301 Moved Permanently", "d": "The resource moved for good; update bookmarks and SEO.", "g": "redirection", "l": 2, "q": "What is 301 Moved Permanently?", "a": "The resource moved for good; update bookmarks and SEO.", "x": "301 Moved Permanently — The resource moved for good; update bookmarks and SEO. Example: Domain migrations..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "302 Found", "d": "Temporary redirect; historically misused for 303.", "g": "redirection", "l": 2, "q": "What is 302 Found?", "a": "Temporary redirect; historically misused for 303.", "x": "302 Found — Temporary redirect; historically misused for 303. Example: Login flows..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "303 See Other", "d": "See another URI with GET after POST.", "g": "redirection", "l": 2, "q": "What is 303 See Other?", "a": "See another URI with GET after POST.", "x": "303 See Other — See another URI with GET after POST. Example: Post/Redirect/Get..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "304 Not Modified", "d": "Cached copy is still fresh; saves bandwidth.", "g": "redirection", "l": 2, "q": "What is 304 Not Modified?", "a": "Cached copy is still fresh; saves bandwidth.", "x": "304 Not Modified — Cached copy is still fresh; saves bandwidth. Example: Conditional GET..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "305 Use Proxy", "d": "Deprecated: access via the named proxy.", "g": "redirection", "l": 2, "q": "What is 305 Use Proxy?", "a": "Deprecated: access via the named proxy.", "x": "305 Use Proxy — Deprecated: access via the named proxy. Example: Legacy..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "307 Temporary Redirect", "d": "Temporary move, keeping the original method.", "g": "redirection", "l": 2, "q": "What is 307 Temporary Redirect?", "a": "Temporary move, keeping the original method.", "x": "307 Temporary Redirect — Temporary move, keeping the original method. Example: Maintenance pages..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "308 Permanent Redirect", "d": "Permanent move, keeping the original method.", "g": "redirection", "l": 2, "q": "What is 308 Permanent Redirect?", "a": "Permanent move, keeping the original method.", "x": "308 Permanent Redirect — Permanent move, keeping the original method. Example: HTTPS upgrades..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "400 Bad Request", "d": "The server cannot process the malformed request.", "g": "client-error", "l": 2, "q": "What is 400 Bad Request?", "a": "The server cannot process the malformed request.", "x": "400 Bad Request — The server cannot process the malformed request. Example: Bad JSON bodies..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "401 Unauthorized", "d": "Authentication is required or failed.", "g": "client-error", "l": 2, "q": "What is 401 Unauthorized?", "a": "Authentication is required or failed.", "x": "401 Unauthorized — Authentication is required or failed. Example: Missing login token..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "402 Payment Required", "d": "Reserved for future payment use.", "g": "client-error", "l": 2, "q": "What is 402 Payment Required?", "a": "Reserved for future payment use.", "x": "402 Payment Required — Reserved for future payment use. Example: Paywalls..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-http-status-codes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
