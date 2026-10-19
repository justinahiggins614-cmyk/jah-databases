(function(){'use strict';
/* JAH The Roof and Gutter Maintenance Signature Database generator — jahdb-roof-and-gutter-maintenance-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RAGMS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Roof and Gutter Maintenance (Signature): Inspecting Before You Touch Anything — foundations",
  "Roof and Gutter Maintenance (Signature): The Essential Tool Kit — foundations",
  "Roof and Gutter Maintenance (Signature): Safety Gear and Ladder Rules — foundations",
  "Roof and Gutter Maintenance (Signature): Reading the Damage: What Stains Tell You — foundations",
  "Roof and Gutter Maintenance (Signature): Cleaning as Maintenance — foundations",
  "Roof and Gutter Maintenance (Signature): Sealing Gaps and Cracks — foundations",
  "Roof and Gutter Maintenance (Signature): Fasteners: Screws, Nails, and Anchors — foundations",
  "Roof and Gutter Maintenance (Signature): When to Repair vs Replace — foundations",
  "Roof and Gutter Maintenance (Signature): Working With Contractors — foundations",
  "Roof and Gutter Maintenance (Signature): Seasonal Prep Routines — foundations",
  "Roof and Gutter Maintenance (Signature): Moisture and Ventilation Control — foundations",
  "Roof and Gutter Maintenance (Signature): Documenting for Insurance and Resale — foundations"
 ],
 "compounded": [
  "Roof and Gutter Maintenance (Signature): Troubleshooting: It Still Leaks — compounded",
  "Roof and Gutter Maintenance (Signature): Troubleshooting: Strange Noises and Smells — compounded",
  "Roof and Gutter Maintenance (Signature): Energy Efficiency Upgrades — compounded",
  "Roof and Gutter Maintenance (Signature): Dealing With Pests in Structures — compounded",
  "Roof and Gutter Maintenance (Signature): Paint, Finish, and Protection — compounded",
  "Roof and Gutter Maintenance (Signature): Measuring and Estimating Materials — compounded",
  "Roof and Gutter Maintenance (Signature): Renters: What You Can and Cannot Do — compounded",
  "Roof and Gutter Maintenance (Signature): Landlords: Maintenance Systems — compounded",
  "Roof and Gutter Maintenance (Signature): Emergency Shutoffs Everyone Must Know — compounded",
  "Roof and Gutter Maintenance (Signature): Warranties on Work and Materials — compounded",
  "Roof and Gutter Maintenance (Signature): Advanced: Diagnosing Intermittent Faults — compounded",
  "Roof and Gutter Maintenance (Signature): Advanced: Structural Red Flags — compounded"
 ],
 "advanced": [
  "Roof and Gutter Maintenance (Signature): Advanced: Whole-System Upgrades — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Historic and Old-House Methods — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Building Your Own Jigs and Helpers — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Cost Tracking Like a Pro — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Teaching Household Members — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Preparing for Extreme Weather — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Selling a Well-Maintained Home — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Lifetime Maintenance Calendar — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: When DIY Ends — advanced",
  "Roof and Gutter Maintenance (Signature): Advanced: Running a Small Repair Business — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Roof and Gutter Maintenance Signature Database — structural study\n"
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
var gen={version:'jahdb-roof-and-gutter-maintenance-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('roof-and-gutter-maintenance-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
