(function(){'use strict';
/* JAH The Furniture Repair Database generator — jahdb-furniture-repair-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FR-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Furniture Repair: Inspecting Before You Touch Anything — foundations",
  "Furniture Repair: The Essential Tool Kit — foundations",
  "Furniture Repair: Safety Gear and Ladder Rules — foundations",
  "Furniture Repair: Reading the Damage: What Stains Tell You — foundations",
  "Furniture Repair: Cleaning as Maintenance — foundations",
  "Furniture Repair: Sealing Gaps and Cracks — foundations",
  "Furniture Repair: Fasteners: Screws, Nails, and Anchors — foundations",
  "Furniture Repair: When to Repair vs Replace — foundations",
  "Furniture Repair: Working With Contractors — foundations",
  "Furniture Repair: Seasonal Prep Routines — foundations",
  "Furniture Repair: Moisture and Ventilation Control — foundations",
  "Furniture Repair: Documenting for Insurance and Resale — foundations"
 ],
 "compounded": [
  "Furniture Repair: Troubleshooting: It Still Leaks — compounded",
  "Furniture Repair: Troubleshooting: Strange Noises and Smells — compounded",
  "Furniture Repair: Energy Efficiency Upgrades — compounded",
  "Furniture Repair: Dealing With Pests in Structures — compounded",
  "Furniture Repair: Paint, Finish, and Protection — compounded",
  "Furniture Repair: Measuring and Estimating Materials — compounded",
  "Furniture Repair: Renters: What You Can and Cannot Do — compounded",
  "Furniture Repair: Landlords: Maintenance Systems — compounded",
  "Furniture Repair: Emergency Shutoffs Everyone Must Know — compounded",
  "Furniture Repair: Warranties on Work and Materials — compounded",
  "Furniture Repair: Advanced: Diagnosing Intermittent Faults — compounded",
  "Furniture Repair: Advanced: Structural Red Flags — compounded"
 ],
 "advanced": [
  "Furniture Repair: Advanced: Whole-System Upgrades — advanced",
  "Furniture Repair: Advanced: Historic and Old-House Methods — advanced",
  "Furniture Repair: Advanced: Building Your Own Jigs and Helpers — advanced",
  "Furniture Repair: Advanced: Cost Tracking Like a Pro — advanced",
  "Furniture Repair: Advanced: Teaching Household Members — advanced",
  "Furniture Repair: Advanced: Preparing for Extreme Weather — advanced",
  "Furniture Repair: Advanced: Selling a Well-Maintained Home — advanced",
  "Furniture Repair: Advanced: Lifetime Maintenance Calendar — advanced",
  "Furniture Repair: Advanced: When DIY Ends — advanced",
  "Furniture Repair: Advanced: Running a Small Repair Business — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Furniture Repair Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-furniture-repair-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('furniture-repair',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
