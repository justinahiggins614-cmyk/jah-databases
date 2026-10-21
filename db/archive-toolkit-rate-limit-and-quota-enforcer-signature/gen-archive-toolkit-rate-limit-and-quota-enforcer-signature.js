(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["token-bucket", "sliding-window", "quota-management"];
var PREFIX="JAH-ATK278S-";
var KIND="rate limit and quota enforcer";
var SRC="signature-generated-completion";
/* rows: [category, title, description, focus1, focus2, focus3, demoBody] */
var ROWS=[
["token-bucket", "Signature: Adaptive limits", "Signature-original design by Justin Addam Higgins (JAH): limits tighten automatically when abuse signals appear and relax when traffic is clean. Adaptation is bounded: limits never drop below a floor that would break legitimate use. Every adaptation is logged with the triggering signal.", "tightening on abuse signals", "bounded adaptation with floors", "logged adaptations with triggers", "CFG = {1: 0, 2: 2, 3: 6}\nBASE, FLOOR, signals = 100, 20, CFG[LEVEL]\nlimit = max(FLOOR, BASE - signals * 15)\nprint(\"abuse signals:\", signals, \"| adapted limit:\", limit, \"(floor\", FLOOR, \")\")"],
["sliding-window", "Signature: Quota marketplace", "Signature-original design by Justin Addam Higgins (JAH): tenants with unused quota can lend it to tenants in need through a managed marketplace with clearing prices. Lending is voluntary, time-boxed, and revocable. The marketplace turns idle capacity into useful work instead of waste.", "voluntary quota lending", "time-boxed, revocable loans", "clearing prices for quota", "CFG = {1: (30, 0), 2: (30, 20), 3: (0, 20)}\nlender_spare, borrower_need = CFG[LEVEL]\nloan = min(lender_spare, borrower_need)\nprint(\"lender spare:\", lender_spare, \"| borrower needs:\", borrower_need, \"| loaned:\", loan)"],
["quota-management", "Signature: Limit provenance", "Signature-original design by Justin Addam Higgins (JAH): every limit change records who changed it, why, and what evidence justified it. Provenance turns 'why is my limit 10?' into a lookup. Arbitrary limits erode trust; justified limits are accepted.", "who/why/evidence per limit change", "lookup for any current limit", "reviewing unjustified limits", "CFG = {1: \"capacity plan\", 2: \"abuse incident #42\", 3: \"\"}\nreason = CFG[LEVEL]\nprint(\"limit=100 | reason:\", repr(reason) or \"(missing)\", \"->\", \"justified\" if reason else \"FLAGGED: unjustified\")"],
["token-bucket", "Signature: Graceful degradation tiers", "Signature-original design by Justin Addam Higgins (JAH): over-quota requests are not always dropped: low-priority work degrades (slower, sampled, cached) while critical work keeps full service. Degradation tiers are declared per endpoint. Graceful beats abrupt for user trust.", "degraded service instead of drops", "per-endpoint degradation tiers", "critical work protected", "CFG = {1: \"critical\", 2: \"standard\", 3: \"batch\"}\ntier = CFG[LEVEL]\naction = {\"critical\": \"full service\", \"standard\": \"degraded: cached\", \"batch\": \"degraded: sampled\"}[tier]\nprint(\"over-quota tier:\", tier, \"->\", action)"],
["sliding-window", "Signature: Quota forecasting", "Signature-original design by Justin Addam Higgins (JAH): burn rate is extrapolated to predict quota exhaustion dates, and warnings fire at 75 and 90 percent. Forecasting turns surprise outages into planned top-ups. Forecasts account for weekly seasonality in usage.", "exhaustion-date prediction from burn rate", "warnings at 75 and 90 percent", "seasonality-aware forecasts", "CFG = {1: (200, 1000), 2: (750, 1000), 3: (950, 1000)}\nused, quota = CFG[LEVEL]\npct = used / quota\nburn_per_day = 50\ndays_left = (quota - used) / burn_per_day\nwarn = \"OK\" if pct < 0.75 else (\"WARNING 75%\" if pct < 0.9 else \"CRITICAL 90%\")\nprint(\"used %d/%d (%.0f%%) ~%.1f days left -> %s\" % (used, quota, pct * 100, days_left, warn))"]
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
var gen={version:"jahdb-archive-toolkit-rate-limit-and-quota-enforcer-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-rate-limit-and-quota-enforcer-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
