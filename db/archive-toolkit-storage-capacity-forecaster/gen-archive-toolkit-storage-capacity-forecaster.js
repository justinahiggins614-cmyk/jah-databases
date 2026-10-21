(function(){'use strict';
var PREFIX="JAH-ATK230-";
var METHODS=[["Growth curve fitting", "Fit linear, exponential, and logistic models to historical usage and pick by backtested error."], ["Per-collection forecasts", "Forecast each collection separately; aggregate forecasts hide the one collection about to explode."], ["Confidence intervals", "Report 50/80/95% bands so planners see the range, not a single seductive number."], ["Seasonality modeling", "Account for weekly and seasonal ingest patterns instead of smoothing them away."], ["Event-adjusted forecasts", "Adjust for known future events (bulk ingests, migrations) entered as calendar inputs."], ["What-if scenarios", "Let planners test 'what if we double ingest' or 'what if we compress at ratio X'."], ["Tiering recommendations", "Recommend which cold data to move to cheaper tiers based on access recency and growth."], ["Compression opportunity analysis", "Estimate reclaimable space from applying modern codecs to old collections."], ["Procurement lead-time alerts", "Alert early enough that procurement and provisioning finish before capacity does."], ["Forecast accuracy tracking", "Backtest every forecast against reality and report the model's track record."], ["Anomaly exclusion", "Exclude one-off bulk loads from trend fitting unless the planner says they represent the future."], ["Multi-site forecasting", "Forecast per site and per replica, not just globally, since capacity is local."], ["Cost projection", "Translate byte forecasts into dollar forecasts per storage class."], ["Retention policy simulation", "Simulate how proposed retention rules change the forecast before adopting them."], ["Dashboard publication", "Publish forecasts where engineers and finance both see them, in plain language."]];
var CATS=["capacity", "forecasting", "planning"];
var DEMO="# Storage Capacity Forecaster demo: least-squares trend + exhaustion date.\nmonths=[120,131,140,152,163,175]  # GB used, last 6 months\nn=len(months); sx=sum(range(n)); sy=sum(months)\nsxx=sum(i*i for i in range(n)); sxy=sum(i*m for i,m in enumerate(months))\nslope=(n*sxy-sx*sy)/(n*sxx-sx*sx); intercept=(sy-slope*sx)/n\ncap=300\nneed=(cap-intercept)/slope\nprint(\"growth %.1f GB/month -> capacity in month %.1f (~%.0f months left)\"%(slope,need,need-(n-1)))\nlo,hi=slope*0.8,slope*1.2\nprint(\"80%% band: %.1f-%.1f months left\"%((cap-intercept)/hi-(n-1),(cap-intercept)/lo-(n-1)))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Storage Capacity Forecaster";
  return {id:id,t:title,title:title,description:"The storage capacity forecaster turns measured growth into procurement and pruning decisions: it models each collection's growth curve, projects when capacity runs out, and recommends actions \u2014 add storage, compress, tier, or retire \u2014 before the crunch. Surprises about disk space are operational failures; forecasting makes them planning inputs. The models stay humble, reporting confidence interval",
    kind:"maintenance tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Public-harvest",last_verified:'2026-10-21',src:"public-harvest",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-storage-capacity-forecaster-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-storage-capacity-forecaster",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();