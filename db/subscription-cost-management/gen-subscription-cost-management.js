(function(){'use strict';
/* JAH Subscription Cost Management Database generator — jahdb-subscription-cost-management-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SUBSCM-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Subscription Inventory", "Cost-Per-Use Analysis", "Streaming Service Strategy", "Cancelling Without the Runaround", "Free Trial Traps", "Annual vs Monthly Billing", "Negotiating Retention Offers", "Family and Shared Plans", "App Subscription Audit", "Subscription Boxes", "Gym and Membership Math"], "Compounded": ["Software Subscriptions", "News and Content Paywalls", "Gaming Subscriptions", "Kids Subscription Controls", "Business Subscription Creep", "The 60-Day Rule", "Downgrading Tiers", "Pausing Instead of Cancelling", "Tracking Renewal Dates", "Virtual Cards for Subscriptions", "Zombie Subscription Revival", "Bundling Decisions"], "Advanced": ["Price Increase Responses", "Sharing Costs Fairly", "The Subscription Policy", "Quarterly Audit Ritual", "Teaching Subscription Smarts", "Annual Subscription Summit", "Emergency Subscription Freeze", "Subscription Alternatives", "Lifetime Subscription Math", "The Minimal Subscription Stack", "Gifted Subscriptions"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — subscription guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — subscription guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A subscription guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"subscription-cost-management-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-subscription-cost-management-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("subscription-cost-management",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
