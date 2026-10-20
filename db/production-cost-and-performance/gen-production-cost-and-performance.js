(function(){'use strict';
/* Public Production Cost and Performance Database generator — jahdb-production-cost-and-performance-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same records.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,fn){return r[(fn()*r.length)|0];}
var PREFIX='JAH-COST-';
var LAST='2026-10-19';
var TITLES=["Crew Costing", "Equipment Costing", "Location Costing", "Post Costing", "AI Compute Costing", "Music Costing", "Contingency", "Cashflow", "Cost Reporting", "Variance Analysis", "Schedule Performance", "Earned Value", "KPI Dashboard", "Forecasting", "Change Control", "Savings Log", "Overtime Control", "Petty Cash", "Fringes and Tax", "Insurance", "Completion Bond", "Financing", "Recoupment", "Profit Participation", "Audit Rights", "Wrap Accounting", "Tax Incentives", "Sustainability Cost", "Master Cost Bible", "Budget Structure"];
var DEFS=["People.", "Gear.", "Places.", "Finish.", "GPUs.", "Score.", "Buffer.", "Timing.", "Actuals.", "Why.", "On time.", "Progress.", "Seen.", "Ahead.", "Gated.", "Kept.", "Watched.", "Small.", "Loaded.", "Covered.", "Guaranteed.", "Funded.", "Paid back.", "Shared.", "Checked.", "Closed.", "Claimed.", "Green.", "One method.", "Categories."];
var GROUPS=["Cost"];
function demoFor(title,defn){return '/* '+title+' \u2014 runnable demo. Save as demo.js and run: node demo.js */\n\'use strict\';\nconsole.log('+JSON.stringify(title)+');\nconsole.log('+JSON.stringify(defn)+');';}
function generate(seed,count){
  var rnd=prng(seed*7919+13),rows=[],n=Math.max(1,Math.min(50,count||5));
  for(var i=0;i<n;i++){
    var ti=(rnd()*TITLES.length)|0, gi=(rnd()*GROUPS.length)|0;
    var title=TITLES[ti], defn=DEFS[ti%DEFS.length], grp=GROUPS[gi];
    var desc=defn.length>170?defn.slice(0,170)+'...':defn;
    var id=PREFIX+String(seed*1000+i+1).padStart(6,'0');
    var demo=demoFor(title,defn);
    rows.push({id:id,t:title,title:title,g:grp,genre:grp,description:desc,definition:defn,
      content:{generated:true,seed:seed,variant:i+1,topic:title,key_points:['Define the standard','Apply per production','Verify at the gate']},
      program_demo:demo,demo:{kind:'program',title:title+' \u2014 demo',program:demo,language:'javascript'},
      source:'signature-original',last_verified:LAST,src:'signature'});
  }
  return rows;
}
window['JAHDB_GEN_production_cost_and_performance']={generate:generate};
})();
