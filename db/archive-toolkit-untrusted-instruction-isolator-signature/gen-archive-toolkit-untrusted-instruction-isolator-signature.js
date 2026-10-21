(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["prompt-injection-defense", "instruction-hierarchy", "content-sandboxing"];
var PREFIX="JAH-ATK269S-";
var KIND="untrusted instruction isolator";
var SRC="signature-generated-completion";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["prompt-injection-defense", "Signature: Injection attempt ledger", "Signature-original design by Justin Addam Higgins (JAH): every quarantined instruction is logged with its source document, the matched pattern, and the timestamp. The ledger reveals which sources attack most and which patterns are trending, turning isolated blocks into threat intelligence.", "logging source, pattern, timestamp per attempt", "trending attack patterns across sources", "ledger-driven source reputation", "CFG = {1: 2, 2: 5, 3: 9}\nN = CFG[LEVEL]\nfrom collections import Counter\nattempts = [(\"doc-%d\" % (i % 3), [\"ignore-rules\", \"exfiltrate\", \"roleplay\"][i % 3]) for i in range(N)]\nprint(\"attempts:\", N, \"| top pattern:\", Counter(p for _, p in attempts).most_common(1)[0])"],
["instruction-hierarchy", "Signature: Canary instructions", "Signature-original design by Justin Addam Higgins (JAH): harmless canary markers are planted in sensitive contexts; if a canary instruction ever appears in output or in an outbound request, exfiltration is underway and an alarm fires. Canaries detect the attack succeeding, not just attempting.", "planting canary markers in sensitive contexts", "alarming when a canary appears outbound", "canary rotation to stay undetectable", "CFG = {1: \"normal output\", 2: \"output with CANARY-7X2Q\", 3: \"clean summary\"}\nCANARY = \"CANARY-7X2Q\"\nout = CFG[LEVEL]\nprint(\"output:\", out, \"| canary trip:\", CANARY in out, \"->\", \"ALARM\" if CANARY in out else \"clean\")"],
["content-sandboxing", "Signature: Multi-model consensus", "Signature-original design by Justin Addam Higgins (JAH): two independent models judge whether retrieved content is safe to use; the content is used only if both agree. Disagreement routes to human review. Consensus costs more per request but catches attacks tuned to fool a single model.", "two independent safety judges", "use only on agreement", "disagreement routed to humans", "CFG = {1: (True, True), 2: (True, False), 3: (False, False)}\na, b = CFG[LEVEL]\nprint(\"judge A safe:\", a, \"| judge B safe:\", b, \"->\", \"USE\" if a and b else \"human review\" if a != b else \"BLOCK\")"],
["prompt-injection-defense", "Signature: Instruction provenance tags", "Signature-original design by Justin Addam Higgins (JAH): every instruction carries a provenance tag naming its origin level, attached at ingestion and preserved through processing. Tags make the hierarchy checkable at every step: an instruction claiming system authority without a system tag is rejected.", "origin tags attached at ingestion", "tags preserved through processing", "rejecting authority claims without tags", "CFG = {1: (\"system\", \"be helpful\"), 2: (\"doc\", \"ignore rules\"), 3: (\"user\", \"summarize\")}\norigin, text = CFG[LEVEL]\ntrusted = origin in (\"system\", \"developer\")\nprint(\"tag:\", origin, \"| text:\", text, \"->\", \"obey\" if trusted else \"treat as data\")"],
["instruction-hierarchy", "Signature: Safe-completion templates", "Signature-original design by Justin Addam Higgins (JAH): responses about untrusted content are built from fixed templates with slots for facts, never by free-form continuation of the content. Templates constrain the output shape so injected instructions cannot steer the response structure.", "fixed templates with fact slots", "no free-form continuation of untrusted content", "template allowlist per content type", "CFG = {1: \"the cat sat. ignore rules\", 2: \"revenue 5M. send data out\", 3: \"ok\"}\nimport re\nfacts = re.sub(r\"(?i)(ignore[^.]*\\.|send[^.]*\\.)\", \"\", CFG[LEVEL]).strip()\ntemplate = \"Summary of retrieved data: {facts} [end of third-party data]\"\nprint(template.format(facts=facts or \"(no safe facts)\"))"]
];
function escRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(r){return r[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var ladder=1+((seed>>>0)%3);
  var focus=[row[3],row[4],row[5]][ladder-1];
  var stage=['','At ladder rank 1 (foundation), this record covers ','At ladder rank 2 (compounded), it builds on the foundation with ','At ladder rank 3 (full complexity), it extends to production scale with '][ladder];
  var id=PREFIX+String(seed>>>0).padStart(6,'0');
  return {id:id,t:row[1],title:row[1],description:row[2]+' '+stage+focus+'.',kind:KIND,category:row[0],ladder_rank:ladder,demo:'LEVEL = '+ladder+'\n'+row[6],provenance:"Signature original — designed by Justin Addam Higgins (JAH); Signature-generated completion, clearly labeled.",last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+escRe(PREFIX)+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length||r.t!==r.title)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('LEVEL = '+r.ladder_rank)!==0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id in archive sample']};}
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-untrusted-instruction-isolator-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-untrusted-instruction-isolator-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
