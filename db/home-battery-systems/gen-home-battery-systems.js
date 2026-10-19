(function(){'use strict';
/* JAH The Home Battery Systems Database generator — jahdb-home-battery-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HBS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Home Battery Systems: Inspecting Before You Touch Anything — foundations",
  "Home Battery Systems: The Essential Tool Kit — foundations",
  "Home Battery Systems: Safety Gear and Ladder Rules — foundations",
  "Home Battery Systems: Reading the Damage: What Stains Tell You — foundations",
  "Home Battery Systems: Cleaning as Maintenance — foundations",
  "Home Battery Systems: Sealing Gaps and Cracks — foundations",
  "Home Battery Systems: Fasteners: Screws, Nails, and Anchors — foundations",
  "Home Battery Systems: When to Repair vs Replace — foundations",
  "Home Battery Systems: Working With Contractors — foundations",
  "Home Battery Systems: Seasonal Prep Routines — foundations",
  "Home Battery Systems: Moisture and Ventilation Control — foundations",
  "Home Battery Systems: Documenting for Insurance and Resale — foundations"
 ],
 "compounded": [
  "Home Battery Systems: Troubleshooting: It Still Leaks — compounded",
  "Home Battery Systems: Troubleshooting: Strange Noises and Smells — compounded",
  "Home Battery Systems: Energy Efficiency Upgrades — compounded",
  "Home Battery Systems: Dealing With Pests in Structures — compounded",
  "Home Battery Systems: Paint, Finish, and Protection — compounded",
  "Home Battery Systems: Measuring and Estimating Materials — compounded",
  "Home Battery Systems: Renters: What You Can and Cannot Do — compounded",
  "Home Battery Systems: Landlords: Maintenance Systems — compounded",
  "Home Battery Systems: Emergency Shutoffs Everyone Must Know — compounded",
  "Home Battery Systems: Warranties on Work and Materials — compounded",
  "Home Battery Systems: Advanced: Diagnosing Intermittent Faults — compounded",
  "Home Battery Systems: Advanced: Structural Red Flags — compounded"
 ],
 "advanced": [
  "Home Battery Systems: Advanced: Whole-System Upgrades — advanced",
  "Home Battery Systems: Advanced: Historic and Old-House Methods — advanced",
  "Home Battery Systems: Advanced: Building Your Own Jigs and Helpers — advanced",
  "Home Battery Systems: Advanced: Cost Tracking Like a Pro — advanced",
  "Home Battery Systems: Advanced: Teaching Household Members — advanced",
  "Home Battery Systems: Advanced: Preparing for Extreme Weather — advanced",
  "Home Battery Systems: Advanced: Selling a Well-Maintained Home — advanced",
  "Home Battery Systems: Advanced: Lifetime Maintenance Calendar — advanced",
  "Home Battery Systems: Advanced: When DIY Ends — advanced",
  "Home Battery Systems: Advanced: Running a Small Repair Business — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Home Battery Systems Database — structural study\n"
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
var gen={version:'jahdb-home-battery-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-battery-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
