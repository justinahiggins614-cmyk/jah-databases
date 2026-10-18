(function(){'use strict';
/* JAH Luxury Travel Database generator — jahdb-luxury-travel-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LTRV-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Luxury Travel?",
  "Five-Star Hotels, Explained",
  "Business Class, Explained",
  "First Class, Explained",
  "Private Transfers and Chauffeurs",
  "The Luxury Travel Advisor",
  "All-Inclusive Luxury Resorts",
  "Fine Dining While Traveling",
  "Luxury Travel Seasons",
  "Packing for Luxury Travel",
  "Luxury Travel Etiquette Basics"
 ],
 "Compounded": [
  "Private Jets, Explained",
  "Suites and Villas",
  "Private Guides",
  "Spa and Wellness Travel",
  "Yacht Charters, Explained",
  "Luxury Train Journeys",
  "Private Safari Lodges",
  "Luxury Cruise Lines",
  "Art and Culture VIP Access",
  "Luxury Travel Insurance",
  "Honeymoon-Level Service, Everyday",
  "The Long-Stay Luxury Villa"
 ],
 "Advanced": [
  "Advanced: Around-the-World by Private Jet",
  "Advanced: Buyouts and Private Islands",
  "Advanced: The Luxury Travel Portfolio",
  "Advanced: Quiet Luxury vs Loud Luxury",
  "Advanced: Sustainability in Luxury Travel",
  "Advanced: The Personal Travel Team",
  "Advanced: Luxury Family Travel",
  "Advanced: Wellness Retreats, Deep Dive",
  "Advanced: Collecting Hotel Status",
  "Advanced: The Luxury Travel Year",
  "The Luxury Travel Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete luxury travel record entries with real measurement math.";
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
    name:topic+' — luxury travel record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A luxury travel record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-luxury-travel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('luxury-travel',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
