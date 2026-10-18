(function(){'use strict';
/* JAH Family Travel Database generator — jahdb-family-travel-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FTRVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Family Travel?",
  "Traveling with Babies and Toddlers",
  "Traveling with School-Age Kids",
  "Traveling with Teenagers",
  "Family Travel Budgets",
  "Kid-Friendly Accommodation",
  "Flying with Kids",
  "Road Trips with Kids",
  "Family Travel Safety Basics",
  "Packing for the Whole Family",
  "Keeping Routines on the Road"
 ],
 "Compounded": [
  "Multigenerational Trips",
  "Family Cruises",
  "All-Inclusive Resorts for Families",
  "National Parks with Kids",
  "Theme Parks, Planned Well",
  "Educational Travel for Kids",
  "Family Travel During School Breaks",
  "Kids Eat Free and Meal Planning",
  "Handling Meltdowns and Jet Lag in Kids",
  "Family Travel Insurance",
  "Document Prep for Traveling with Kids",
  "The Annual Family Trip Tradition"
 ],
 "Advanced": [
  "Advanced: Worldschooling on the Road",
  "Advanced: The Gap Year as a Family",
  "Advanced: Family Sabbaticals",
  "Advanced: Adventure Travel with Kids",
  "Advanced: The Family Travel Ledger",
  "Advanced: Special Needs Family Travel",
  "Advanced: Blended Family Trip Planning",
  "Advanced: Family Reunion Trips",
  "Advanced: Teaching Kids to Plan Trips",
  "Advanced: The Family Travel Archive",
  "The Family Travel Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete family travel record entries with real measurement math.";
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
    name:topic+' — family travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A family travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-family-travel-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('family-travel-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
