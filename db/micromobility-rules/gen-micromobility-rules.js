(function(){'use strict';
/* JAH The Micromobility Rules Database generator — jahdb-micromobility-rules-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MR-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Micromobility Rules: How the System Works — foundations",
  "Micromobility Rules: Pre-Trip Inspection — foundations",
  "Micromobility Rules: Warning Signs Decoded — foundations",
  "Micromobility Rules: Tires: The Critical Contact — foundations",
  "Micromobility Rules: Brakes: Your Life Depends on Them — foundations",
  "Micromobility Rules: Lights and Visibility — foundations",
  "Micromobility Rules: Loading and Weight — foundations",
  "Micromobility Rules: Weather Driving — foundations",
  "Micromobility Rules: Night Operations — foundations",
  "Micromobility Rules: Emergency Procedures — foundations",
  "Micromobility Rules: Breakdown Kit Essentials — foundations",
  "Micromobility Rules: Maintenance Schedules — foundations"
 ],
 "compounded": [
  "Micromobility Rules: Fuel and Energy Smart — compounded",
  "Micromobility Rules: Rules of the Road Refresher — compounded",
  "Micromobility Rules: Sharing the Road — compounded",
  "Micromobility Rules: Micromobility Rules — compounded",
  "Micromobility Rules: Crossing Borders Prepared — compounded",
  "Micromobility Rules: Documentation to Carry — compounded",
  "Micromobility Rules: Insurance for Your Mode — compounded",
  "Micromobility Rules: Planning Long Trips — compounded",
  "Micromobility Rules: Passengers and Cargo Safety — compounded",
  "Micromobility Rules: New Drivers and Training — compounded",
  "Micromobility Rules: Dealing With Traffic Stops and Citations — compounded",
  "Micromobility Rules: Winterizing Your Vehicle — compounded"
 ],
 "advanced": [
  "Micromobility Rules: Advanced: Defensive Mastery — advanced",
  "Micromobility Rules: Advanced: Adverse Conditions Expert — advanced",
  "Micromobility Rules: Advanced: Towing and Hauling — advanced",
  "Micromobility Rules: Advanced: Fleet Management — advanced",
  "Micromobility Rules: Advanced: Incident Investigation — advanced",
  "Micromobility Rules: Advanced: Teaching Others — advanced",
  "Micromobility Rules: Advanced: Regulatory Compliance — advanced",
  "Micromobility Rules: Advanced: Technology and ADAS — advanced",
  "Micromobility Rules: Advanced: Emergency Response Driving — advanced",
  "Micromobility Rules: Advanced: The Lifetime Safe Operator — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Micromobility Rules Database — structural study\n"
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
var gen={version:'jahdb-micromobility-rules-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('micromobility-rules',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
