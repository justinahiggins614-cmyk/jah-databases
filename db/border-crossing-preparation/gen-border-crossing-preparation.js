(function(){'use strict';
/* JAH The Border Crossing Preparation Database generator — jahdb-border-crossing-preparation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BCP-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Border Crossing Preparation: How the System Works — foundations",
  "Border Crossing Preparation: Pre-Trip Inspection — foundations",
  "Border Crossing Preparation: Warning Signs Decoded — foundations",
  "Border Crossing Preparation: Tires: The Critical Contact — foundations",
  "Border Crossing Preparation: Brakes: Your Life Depends on Them — foundations",
  "Border Crossing Preparation: Lights and Visibility — foundations",
  "Border Crossing Preparation: Loading and Weight — foundations",
  "Border Crossing Preparation: Weather Driving — foundations",
  "Border Crossing Preparation: Night Operations — foundations",
  "Border Crossing Preparation: Emergency Procedures — foundations",
  "Border Crossing Preparation: Breakdown Kit Essentials — foundations",
  "Border Crossing Preparation: Maintenance Schedules — foundations"
 ],
 "compounded": [
  "Border Crossing Preparation: Fuel and Energy Smart — compounded",
  "Border Crossing Preparation: Rules of the Road Refresher — compounded",
  "Border Crossing Preparation: Sharing the Road — compounded",
  "Border Crossing Preparation: Micromobility Rules — compounded",
  "Border Crossing Preparation: Crossing Borders Prepared — compounded",
  "Border Crossing Preparation: Documentation to Carry — compounded",
  "Border Crossing Preparation: Insurance for Your Mode — compounded",
  "Border Crossing Preparation: Planning Long Trips — compounded",
  "Border Crossing Preparation: Passengers and Cargo Safety — compounded",
  "Border Crossing Preparation: New Drivers and Training — compounded",
  "Border Crossing Preparation: Dealing With Traffic Stops and Citations — compounded",
  "Border Crossing Preparation: Winterizing Your Vehicle — compounded"
 ],
 "advanced": [
  "Border Crossing Preparation: Advanced: Defensive Mastery — advanced",
  "Border Crossing Preparation: Advanced: Adverse Conditions Expert — advanced",
  "Border Crossing Preparation: Advanced: Towing and Hauling — advanced",
  "Border Crossing Preparation: Advanced: Fleet Management — advanced",
  "Border Crossing Preparation: Advanced: Incident Investigation — advanced",
  "Border Crossing Preparation: Advanced: Teaching Others — advanced",
  "Border Crossing Preparation: Advanced: Regulatory Compliance — advanced",
  "Border Crossing Preparation: Advanced: Technology and ADAS — advanced",
  "Border Crossing Preparation: Advanced: Emergency Response Driving — advanced",
  "Border Crossing Preparation: Advanced: The Lifetime Safe Operator — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Border Crossing Preparation Database — structural study\n"
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
var gen={version:'jahdb-border-crossing-preparation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('border-crossing-preparation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
