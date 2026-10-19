(function(){'use strict';
/* JAH The Home Battery Systems Signature Database generator — jahdb-home-battery-systems-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HBSS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Home Battery Systems (Signature): Inspecting Before You Touch Anything — foundations",
  "Home Battery Systems (Signature): The Essential Tool Kit — foundations",
  "Home Battery Systems (Signature): Safety Gear and Ladder Rules — foundations",
  "Home Battery Systems (Signature): Reading the Damage: What Stains Tell You — foundations",
  "Home Battery Systems (Signature): Cleaning as Maintenance — foundations",
  "Home Battery Systems (Signature): Sealing Gaps and Cracks — foundations",
  "Home Battery Systems (Signature): Fasteners: Screws, Nails, and Anchors — foundations",
  "Home Battery Systems (Signature): When to Repair vs Replace — foundations",
  "Home Battery Systems (Signature): Working With Contractors — foundations",
  "Home Battery Systems (Signature): Seasonal Prep Routines — foundations",
  "Home Battery Systems (Signature): Moisture and Ventilation Control — foundations",
  "Home Battery Systems (Signature): Documenting for Insurance and Resale — foundations"
 ],
 "compounded": [
  "Home Battery Systems (Signature): Troubleshooting: It Still Leaks — compounded",
  "Home Battery Systems (Signature): Troubleshooting: Strange Noises and Smells — compounded",
  "Home Battery Systems (Signature): Energy Efficiency Upgrades — compounded",
  "Home Battery Systems (Signature): Dealing With Pests in Structures — compounded",
  "Home Battery Systems (Signature): Paint, Finish, and Protection — compounded",
  "Home Battery Systems (Signature): Measuring and Estimating Materials — compounded",
  "Home Battery Systems (Signature): Renters: What You Can and Cannot Do — compounded",
  "Home Battery Systems (Signature): Landlords: Maintenance Systems — compounded",
  "Home Battery Systems (Signature): Emergency Shutoffs Everyone Must Know — compounded",
  "Home Battery Systems (Signature): Warranties on Work and Materials — compounded",
  "Home Battery Systems (Signature): Advanced: Diagnosing Intermittent Faults — compounded",
  "Home Battery Systems (Signature): Advanced: Structural Red Flags — compounded"
 ],
 "advanced": [
  "Home Battery Systems (Signature): Advanced: Whole-System Upgrades — advanced",
  "Home Battery Systems (Signature): Advanced: Historic and Old-House Methods — advanced",
  "Home Battery Systems (Signature): Advanced: Building Your Own Jigs and Helpers — advanced",
  "Home Battery Systems (Signature): Advanced: Cost Tracking Like a Pro — advanced",
  "Home Battery Systems (Signature): Advanced: Teaching Household Members — advanced",
  "Home Battery Systems (Signature): Advanced: Preparing for Extreme Weather — advanced",
  "Home Battery Systems (Signature): Advanced: Selling a Well-Maintained Home — advanced",
  "Home Battery Systems (Signature): Advanced: Lifetime Maintenance Calendar — advanced",
  "Home Battery Systems (Signature): Advanced: When DIY Ends — advanced",
  "Home Battery Systems (Signature): Advanced: Running a Small Repair Business — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Home Battery Systems Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
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
var gen={version:'jahdb-home-battery-systems-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-battery-systems-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
