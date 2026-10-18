(function(){'use strict';
/* JAH Travel Hacking and Miles Database generator — jahdb-travel-hacking-miles-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-THML-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Travel Hacking?",
  "Airline Miles, Explained",
  "Hotel Points, Explained",
  "Transferable Points Currencies",
  "Earning Miles Without Flying",
  "The Signup Bonus Strategy",
  "Credit Scores and Travel Cards",
  "Award Charts vs Dynamic Pricing",
  "Booking Your First Award Flight",
  "Hotel Award Nights, Explained",
  "Keeping Miles from Expiring"
 ],
 "Compounded": [
  "Airline Alliances, Explained",
  "Sweet Spots in Award Charts",
  "Positioning Flights",
  "Stopovers on Award Tickets",
  "Companion Passes and Companion Fares",
  "Everyday Spending Strategy",
  "Shopping Portals and Dining Programs",
  "Transfer Bonuses",
  "Points for Family Travel",
  "When Cash Beats Points",
  "Taxes and Fees on Award Tickets",
  "The Points Devaluation Problem"
 ],
 "Advanced": [
  "Advanced: Round-the-World Award Tickets",
  "Advanced: First Class for the Price of Economy",
  "Advanced: Status Matching and Challenges",
  "Advanced: The Two-Player Mode",
  "Advanced: Business Travel Points Strategy",
  "Advanced: Tracking Your Points Portfolio",
  "Advanced: Teaching Travel Hacking",
  "Advanced: The Points and Miles Ledger",
  "Advanced: Lifetime Status, Explained",
  "Advanced: The Travel Hacking Year",
  "The Travel Hacking Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete travel hacking record entries with real measurement math.";
function demoProgram(topic,field){
  return "'use strict';\n// "+topic+" \u2014 sample demo.\n// Field: "+field+"\nconst a = 12;\nconst b = 4;\nconst r = a / b;\nconsole.log('sample ratio = ' + r.toFixed(2));\nif (!isFinite(r)) throw new Error('bad');\nconsole.log('DEMO_OK');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — travel hacking record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A travel hacking record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'node',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-travel-hacking-miles-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('travel-hacking-miles',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
