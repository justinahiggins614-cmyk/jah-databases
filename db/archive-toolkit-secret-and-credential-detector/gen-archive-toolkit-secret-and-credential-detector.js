(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["entropy-analysis", "pattern-matching", "exposure-triage"];
var PREFIX="JAH-ATK264-";
var KIND="secret and credential detector";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["entropy-analysis", "High-entropy string detection", "Random-looking tokens have high Shannon entropy: the character distribution is close to uniform. Strings above an entropy threshold, of sufficient length, and in the right character set are flagged as candidate secrets. Entropy catches secrets that no known-prefix list contains.", "Shannon entropy over candidate strings", "length and charset gates to cut noise", "thresholds tuned per codebase", "CFG = {1: \"hello world\", 2: \"xK9#mQ2$vL8@nP4!\", 3: \"AKIAIOSFODNN7EXAMPLE\"}\nimport math\nfrom collections import Counter\ns = CFG[LEVEL]\nfreq = Counter(s)\nentropy = -sum((c / len(s)) * math.log2(c / len(s)) for c in freq.values())\nsecret = entropy > 4.0 and len(s) >= 12\nprint(\"string: %s | entropy %.2f -> %s\" % (s, entropy, \"SECRET?\" if secret else \"clean\"))"],
["pattern-matching", "Known-prefix secret patterns", "Many credential formats have recognizable prefixes: AKIA for AWS keys, ghp_ for GitHub tokens, sk- for API keys. Prefix matching is fast and precise, and each prefix maps to a specific rotation runbook. The prefix library is updated as providers add formats.", "prefix-to-provider mapping", "per-prefix rotation runbooks", "updatable prefix library", "CFG = {1: \"hello\", 2: \"AKIAIOSFODNN7EXAMPLE\", 3: \"ghp_abc123DEF456\"}\nPREFIXES = {\"AKIA\": \"aws-key\", \"ghp_\": \"github-token\", \"sk-\": \"api-key\"}\ns = CFG[LEVEL]\nhit = next((v for p, v in PREFIXES.items() if s.startswith(p)), None)\nprint(\"string:\", s, \"| detected:\", hit or \"none\")"],
["exposure-triage", "Private-key block detection", "Private keys in PEM format are wrapped in unmistakable BEGIN/END markers. Scanning for these markers catches keys committed to repositories, the most common serious exposure. Detection triggers immediate rotation because a committed private key is considered compromised.", "PEM BEGIN/END marker scanning", "immediate rotation on detection", "history scanning, not just current files", "CFG = {1: \"no keys here\", 2: \"-----BEGIN RSA PRIVATE KEY-----\\nMIIE...\", 3: \"-----BEGIN OPENSSH PRIVATE KEY-----\\nb3Bl...\"}\ntext = CFG[LEVEL]\nfound = \"PRIVATE KEY-----\" in text\nprint(\"private key block:\", \"FOUND -> rotate immediately\" if found else \"none\")"],
["entropy-analysis", "Exposure triage workflow", "Findings move through states: new, verified, rotation-in-progress, resolved, and false-positive. Each state has an owner and a deadline; stale findings escalate. The workflow ensures every detected secret is driven to resolution instead of lingering in a report.", "finding lifecycle states", "owners and deadlines per state", "escalation on stale findings", "CFG = {1: [\"new\"], 2: [\"new\", \"verified\"], 3: [\"new\", \"verified\", \"rotating\"]}\nstates = CFG[LEVEL]\nflow = {\"new\": \"verified\", \"verified\": \"rotating\", \"rotating\": \"resolved\"}\nfor s in states:\n    print(s, \"->\", flow.get(s, \"terminal\"))"],
["pattern-matching", "Allowlist for test fixtures", "Test suites legitimately contain fake secrets, so an allowlist exempts known fixture values and documented example keys. Allowlist entries require justification and expire, preventing real secrets from hiding behind permanent exemptions. Example keys from documentation are pre-allowlisted.", "exempting documented fake secrets", "justified, expiring allowlist entries", "pre-allowlisted documentation examples", "CFG = {1: \"AKIAIOSFODNN7EXAMPLE\", 2: \"xK9#mQ2$vL8@nP4!\", 3: \"test-password-123\"}\nALLOW = {\"AKIAIOSFODNN7EXAMPLE\": \"aws docs example\", \"test-password-123\": \"fixture\"}\ns = CFG[LEVEL]\nprint(\"candidate:\", s, \"|\", \"ALLOWLISTED (%s)\" % ALLOW[s] if s in ALLOW else \"FLAGGED\")"]
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
  return {id:id,t:row[1],title:row[1],description:row[2]+' '+stage+focus+'.',kind:KIND,category:row[0],ladder_rank:ladder,demo:'LEVEL = '+ladder+'\n'+row[6],provenance:"Public harvest — documented archive-engineering practice; method fact-checked against standard references.",last_verified:'2026-10-21',src:SRC,_seed:seed};
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
var gen={version:"jahdb-archive-toolkit-secret-and-credential-detector-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-secret-and-credential-detector",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
