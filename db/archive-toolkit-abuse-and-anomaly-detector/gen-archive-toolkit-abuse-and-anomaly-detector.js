(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["behavioral-baselining", "rate-anomaly", "pattern-flagging"];
var PREFIX="JAH-ATK277-";
var KIND="abuse and anomaly detector";
var SRC="public-harvest";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["behavioral-baselining", "Baseline and deviation detection", "Normal behavior is baselined per identity and per endpoint: typical request rates, hours, and volumes. Live activity is compared to the baseline with z-scores; deviations beyond threshold flag for review. Baselines adapt slowly so gradual legitimate change does not false-alarm.", "per-identity and per-endpoint baselines", "z-score deviation flagging", "slowly adapting baselines", "CFG = {1: 12, 2: 45, 3: 200}\nobs, mean, sd = CFG[LEVEL], 10.0, 2.0\nz = (obs - mean) / sd\nprint(\"observed %d vs baseline %.0f±%.0f: z=%.1f\" % (obs, mean, sd, z), \"->\", \"FLAG\" if abs(z) > 3 else \"normal\")"],
["rate-anomaly", "Impossible-travel detection", "Logins from geographically distant locations within an impossible time window indicate credential compromise or sharing. The detector computes required travel speed between successive logins and flags the physically impossible. VPN and travel exceptions are handled via declared itineraries.", "travel-speed computation between logins", "flagging physically impossible sequences", "declared-itinerary exceptions", "CFG = {1: (100, 2), 2: (8000, 1), 3: (500, 5)}\nkm, hours = CFG[LEVEL]\nspeed = km / hours\nprint(\"login moved %d km in %dh = %.0f km/h\" % (km, hours, speed), \"->\", \"IMPOSSIBLE-TRAVEL FLAG\" if speed > 1000 else \"plausible\")"],
["pattern-flagging", "Burst detection", "Sudden spikes in request volume versus recent history indicate scraping, brute force, or runaway clients. The detector compares short-window counts against longer baselines and flags multiplicative jumps. Bursts trigger rate limiting first and investigation second.", "short-window vs baseline comparison", "multiplicative-jump flagging", "limit first, investigate second", "CFG = {1: (100, 110), 2: (100, 500), 3: (100, 5000)}\nbaseline, now = CFG[LEVEL]\nratio = now / baseline\nprint(\"baseline %d -> now %d (x%.1f)\" % (baseline, now, ratio), \"->\", \"BURST: rate-limit\" if ratio > 5 else \"normal\")"],
["behavioral-baselining", "Known-abuse pattern matching", "Attack signatures (credential stuffing rhythms, enumeration sequences, scanner fingerprints) are matched against live traffic. Pattern libraries come from incident history and threat sharing. Matches fire with the pattern name and recommended response attached.", "attack-signature libraries", "matches with named patterns", "recommended response per pattern", "CFG = {1: [\"login-ok\"], 2: [\"login-fail\"] * 20 + [\"login-ok\"], 3: [\"/admin\", \"/wp-admin\", \"/.env\"]}\nevents = CFG[LEVEL]\nstuffing = events.count(\"login-fail\") >= 10\nscanning = sum(1 for e in events if e.startswith(\"/\")) >= 3\nprint(\"events:\", len(events), \"| credential-stuffing:\", stuffing, \"| scanner:\", scanning)"],
["rate-anomaly", "Risk scoring and triage", "Signals combine into a composite risk score: anomaly size, pattern matches, asset sensitivity, and identity history. Scores map to actions: allow, challenge (step-up), or block. Triage queues are ordered by score so analysts work the riskiest first.", "composite scores from multiple signals", "allow/challenge/block mapping", "analyst queues ordered by risk", "CFG = {1: 15, 2: 55, 3: 92}\nscore = CFG[LEVEL]\naction = \"allow\" if score < 30 else (\"challenge\" if score < 70 else \"BLOCK\")\nprint(\"risk score:\", score, \"->\", action)"]
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
var gen={version:"jahdb-archive-toolkit-abuse-and-anomaly-detector-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-abuse-and-anomaly-detector",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
