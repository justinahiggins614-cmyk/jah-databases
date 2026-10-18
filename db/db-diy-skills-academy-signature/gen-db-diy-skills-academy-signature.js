(function(){'use strict';
/* JAH The DIY Skills Academy generator — jahdb-db-diy-skills-academy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DYSAS-";
var FIELDS=["Home Basics","Repairs","Builds"];
var TOPICS={
 "Home Basics": [
  "The DIY Mindset (Signature Edition) - Home Basics",
  "Your First Toolbox (Signature Edition) - Home Basics",
  "Measuring Like a Pro (Signature Edition) - Home Basics",
  "Drills and Drivers (Signature Edition) - Home Basics",
  "Hammers and Nails (Signature Edition) - Home Basics",
  "Screwdrivers and Screws (Signature Edition) - Home Basics",
  "Levels and Plumb (Signature Edition) - Home Basics",
  "Safety Gear Basics (Signature Edition) - Home Basics",
  "Reading Instructions (Signature Edition) - Home Basics",
  "The Hardware Store Tour (Signature Edition) - Home Basics",
  "Cleaning and Organizing (Signature Edition) - Home Basics",
  "Basic Home Maintenance Schedule (Signature Edition) - Home Basics"
 ],
 "Repairs": [
  "Fixing a Running Toilet (Signature Edition) - Repairs",
  "Unclogging Drains (Signature Edition) - Repairs",
  "Patching Drywall (Signature Edition) - Repairs",
  "Fixing a Leaky Faucet (Signature Edition) - Repairs",
  "Caulking Like a Pro (Signature Edition) - Repairs",
  "Replacing a Light Fixture (Signature Edition) - Repairs",
  "Fixing Squeaky Floors (Signature Edition) - Repairs",
  "Screen Repair (Signature Edition) - Repairs",
  "Door Adjustments (Signature Edition) - Repairs",
  "Touch-Up Painting (Signature Edition) - Repairs",
  "Weatherstripping Doors (Signature Edition) - Repairs",
  "Fixing Cabinet Hinges (Signature Edition) - Repairs"
 ],
 "Builds": [
  "Build a Bookshelf (Signature Edition) - Builds",
  "Build a Workbench (Signature Edition) - Builds",
  "Build Raised Garden Beds (Signature Edition) - Builds",
  "Build a Fire Pit (Signature Edition) - Builds",
  "Install a Ceiling Fan (Signature Edition) - Builds",
  "Lay a Patio (Signature Edition) - Builds",
  "Build Storage Shelves (Signature Edition) - Builds",
  "Paint a Room (Signature Edition) - Builds",
  "Your DIY Journey (Signature Edition) - Builds",
  "Build a Compost Bin (Signature Edition) - Builds"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Diy Skills Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — DIY lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A DIY lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"diy-skills-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-diy-skills-academy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-diy-skills-academy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
