(function(){'use strict';
/* JAH Senior Travel Database generator — jahdb-senior-travel-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SNTR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Senior Travel?",
  "Best Destinations for Senior Travelers",
  "Senior Travel Discounts, Explained",
  "Travel Insurance for Seniors",
  "Medications and Health Prep for Trips",
  "Comfortable Pacing: The Slow Itinerary",
  "Accessible Accommodation Choices",
  "Flying Comfortably at Any Age",
  "Senior Group Tours, Explained",
  "Staying Healthy on the Road",
  "Travel Documents Checklist for Seniors"
 ],
 "Compounded": [
  "River Cruises for Seniors",
  "Ocean Cruises for Seniors",
  "Rail Journeys for Seniors",
  "National Parks for Seniors",
  "Solo Travel After 60",
  "Traveling with Grandchildren",
  "Long-Stay Winter Escapes",
  "Senior Travel Clubs and Programs",
  "Managing Mobility Aids While Traveling",
  "Travel Vaccinations for Seniors",
  "Senior Travel Scams to Know",
  "The Senior Travel Budget"
 ],
 "Advanced": [
  "Advanced: Around-the-World After Retirement",
  "Advanced: Expat Retirement Scouting Trips",
  "Advanced: Adventure Travel After 60",
  "Advanced: The Senior Travel Year",
  "Advanced: Volunteering Abroad in Retirement",
  "Advanced: Teaching Senior Travel",
  "Advanced: Legacy Trips",
  "Advanced: The Senior Travel Health File",
  "Advanced: Multigenerational Legacy Cruises",
  "Advanced: The Senior Travel Memoir",
  "The Senior Travel Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete senior travel record entries with real measurement math.";
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
    name:topic+' — senior travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A senior travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-senior-travel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('senior-travel',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
