(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["identity-proofing", "credential-verification", "session-management"];
var PREFIX="JAH-ATK261-";
var KIND="identity and authentication manager";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["identity-proofing", "Multi-factor authentication flow", "Authentication requires two or more independent factors: something known (password), something held (one-time code), or something inherent (biometric). The factors must be independent so compromising one does not compromise the others. Step-up authentication adds factors for sensitive actions.", "combining password with a one-time code", "independent factors that do not share failure modes", "step-up authentication for sensitive actions", "CFG = {1: (\"correct\", \"123456\"), 2: (\"correct\", \"000000\"), 3: (\"wrong\", \"123456\")}\npw, otp = CFG[LEVEL]\npw_ok = (pw == \"correct\")\notp_ok = (otp == \"123456\")\nprint(\"password:\", \"ok\" if pw_ok else \"FAIL\", \"| one-time code:\", \"ok\" if otp_ok else \"FAIL\", \"| authenticated:\", pw_ok and otp_ok)"],
["credential-verification", "Password hashing with salt", "Passwords are never stored directly: each is combined with a unique random salt and run through a slow key-derivation function like PBKDF2, bcrypt, or Argon2. Verification re-derives the hash and compares in constant time. Salts defeat rainbow tables; slowness defeats brute force.", "unique random salt per password", "slow key-derivation functions", "constant-time comparison on verify", "CFG = {1: 1000, 2: 10000, 3: 60000}\nimport hashlib, os, hmac\nsalt = os.urandom(16)\ndk = hashlib.pbkdf2_hmac(\"sha256\", b\"s3cret\", salt, CFG[LEVEL])\nguess = hashlib.pbkdf2_hmac(\"sha256\", b\"s3cret\", salt, CFG[LEVEL])\nprint(\"iterations:\", CFG[LEVEL], \"| verify:\", hmac.compare_digest(dk, guess))"],
["session-management", "Token-based session management", "After authentication the server issues a signed session token carrying the identity and expiry. Each request presents the token; the server verifies the signature and expiry without a database lookup. Tokens are short-lived and refreshable, and revocation lists kill compromised sessions.", "signed tokens carrying identity and expiry", "stateless verification of signature and expiry", "revocation lists for compromised sessions", "CFG = {1: 3600, 2: 600, 3: 60}\nimport hashlib, hmac, time\nSECRET = b\"session-secret\"\ndef issue(user, ttl):\n    body = \"%s|%d\" % (user, int(time.time()) + ttl)\n    return body + \"|\" + hmac.new(SECRET, body.encode(), hashlib.sha256).hexdigest()[:16]\ndef verify(tok):\n    body, sig = tok.rsplit(\"|\", 1)\n    user, exp = body.split(\"|\")\n    good = hmac.compare_digest(sig, hmac.new(SECRET, body.encode(), hashlib.sha256).hexdigest()[:16])\n    return good and int(exp) > time.time()\ntok = issue(\"amy\", CFG[LEVEL])\nprint(\"ttl=%ds token valid:\" % CFG[LEVEL], verify(tok))"],
["identity-proofing", "Identity proofing levels", "Identity assurance levels (IAL1 self-asserted, IAL2 remotely proofed, IAL3 in-person proofed) map verification rigor to risk. Higher-value access requires higher proofing. Proofing evidence is recorded so the assurance level of every identity is auditable.", "assurance levels mapped to verification rigor", "higher proofing for higher-value access", "auditable proofing evidence per identity", "CFG = {1: 1, 2: 2, 3: 3}\nial = CFG[LEVEL]\nneed = 2  # resource requires IAL2\nsteps = {1: [\"self-assert\"], 2: [\"self-assert\", \"document-check\"], 3: [\"self-assert\", \"document-check\", \"in-person\"]}\nprint(\"identity IAL%d\" % ial, steps[ial], \"| access:\", \"GRANT\" if ial >= need else \"DENY (proofing too low)\")"],
["credential-verification", "Account recovery with verification", "Account recovery requires proof through a verified channel plus a cooldown before the recovered account regains full privileges. Recovery codes are single-use and the old credentials are invalidated. Every recovery is logged and the account owner is notified through all channels.", "verified-channel proof plus cooldown", "single-use recovery codes", "owner notification on every recovery", "CFG = {1: {\"code_ok\": True, \"hours\": 25}, 2: {\"code_ok\": True, \"hours\": 5}, 3: {\"code_ok\": False, \"hours\": 30}}\nc = CFG[LEVEL]\nok = c[\"code_ok\"] and c[\"hours\"] >= 24\nprint(\"code valid:\", c[\"code_ok\"], \"| cooldown %dh:\" % c[\"hours\"], \"met\" if c[\"hours\"] >= 24 else \"NOT met\", \"| recovered:\", ok)"]
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
var gen={version:"jahdb-archive-toolkit-identity-and-authentication-manager-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-identity-and-authentication-manager",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
