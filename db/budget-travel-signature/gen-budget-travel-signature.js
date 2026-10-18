(function(){'use strict';
/* JAH Budget Travel Database generator — jahdb-budget-travel-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BTRVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Budget Travel?",
  "Setting a Trip Budget",
  "Budget Airlines, Explained",
  "Hostels, Explained",
  "Street Food and Cheap Eats",
  "Traveling in Shoulder Season",
  "Fare Alerts and Price Tracking",
  "The Carry-On-Only Method",
  "Free Walking Tours",
  "Public Transit Over Taxis",
  "Budget Travel Safety Basics"
 ],
 "Compounded": [
  "Error Fares and Mistake Fares",
  "Stopovers and Open-Jaw Tickets",
  "House Sitting for Free Stays",
  "Work Exchange Programs",
  "Repositioning Cruises",
  "Travel Credit Cards for Beginners",
  "Points and Miles Basics",
  "Slow Travel to Spend Less",
  "Cooking Your Own Meals",
  "Overnight Buses and Trains as Hotels",
  "Travel Insurance on a Budget",
  "The Fifty-Dollar-a-Day Framework"
 ],
 "Advanced": [
  "Advanced: Fare Construction Basics",
  "Advanced: Hidden-City Ticketing Risks",
  "Advanced: The Budget Travel Year",
  "Advanced: Geoarbitrage Living",
  "Advanced: Travel Hacking Stacks",
  "Advanced: The One-Bag Budget System",
  "Advanced: Budget Safari and Tours",
  "Advanced: Off-Season Luxury for Less",
  "Advanced: The Budget Travel Ledger",
  "Advanced: Teaching Budget Travel",
  "The Budget Travel Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete budget travel record entries with real measurement math.";
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
    name:topic+' — budget travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A budget travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-budget-travel-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('budget-travel-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
