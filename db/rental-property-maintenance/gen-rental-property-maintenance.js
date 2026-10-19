(function(){'use strict';
/* JAH The Rental Property Maintenance Database generator — jahdb-rental-property-maintenance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RPM-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Rental Property Maintenance: Inspecting Before You Touch Anything — foundations",
  "Rental Property Maintenance: The Essential Tool Kit — foundations",
  "Rental Property Maintenance: Safety Gear and Ladder Rules — foundations",
  "Rental Property Maintenance: Reading the Damage: What Stains Tell You — foundations",
  "Rental Property Maintenance: Cleaning as Maintenance — foundations",
  "Rental Property Maintenance: Sealing Gaps and Cracks — foundations",
  "Rental Property Maintenance: Fasteners: Screws, Nails, and Anchors — foundations",
  "Rental Property Maintenance: When to Repair vs Replace — foundations",
  "Rental Property Maintenance: Working With Contractors — foundations",
  "Rental Property Maintenance: Seasonal Prep Routines — foundations",
  "Rental Property Maintenance: Moisture and Ventilation Control — foundations",
  "Rental Property Maintenance: Documenting for Insurance and Resale — foundations"
 ],
 "compounded": [
  "Rental Property Maintenance: Troubleshooting: It Still Leaks — compounded",
  "Rental Property Maintenance: Troubleshooting: Strange Noises and Smells — compounded",
  "Rental Property Maintenance: Energy Efficiency Upgrades — compounded",
  "Rental Property Maintenance: Dealing With Pests in Structures — compounded",
  "Rental Property Maintenance: Paint, Finish, and Protection — compounded",
  "Rental Property Maintenance: Measuring and Estimating Materials — compounded",
  "Rental Property Maintenance: Renters: What You Can and Cannot Do — compounded",
  "Rental Property Maintenance: Landlords: Maintenance Systems — compounded",
  "Rental Property Maintenance: Emergency Shutoffs Everyone Must Know — compounded",
  "Rental Property Maintenance: Warranties on Work and Materials — compounded",
  "Rental Property Maintenance: Advanced: Diagnosing Intermittent Faults — compounded",
  "Rental Property Maintenance: Advanced: Structural Red Flags — compounded"
 ],
 "advanced": [
  "Rental Property Maintenance: Advanced: Whole-System Upgrades — advanced",
  "Rental Property Maintenance: Advanced: Historic and Old-House Methods — advanced",
  "Rental Property Maintenance: Advanced: Building Your Own Jigs and Helpers — advanced",
  "Rental Property Maintenance: Advanced: Cost Tracking Like a Pro — advanced",
  "Rental Property Maintenance: Advanced: Teaching Household Members — advanced",
  "Rental Property Maintenance: Advanced: Preparing for Extreme Weather — advanced",
  "Rental Property Maintenance: Advanced: Selling a Well-Maintained Home — advanced",
  "Rental Property Maintenance: Advanced: Lifetime Maintenance Calendar — advanced",
  "Rental Property Maintenance: Advanced: When DIY Ends — advanced",
  "Rental Property Maintenance: Advanced: Running a Small Repair Business — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Rental Property Maintenance Database — structural study\n"
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
var gen={version:'jahdb-rental-property-maintenance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rental-property-maintenance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
