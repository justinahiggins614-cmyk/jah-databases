(function(){'use strict';
/* JAH The Micromobility Rules Signature Database generator — jahdb-micromobility-rules-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MRS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Micromobility Rules (Signature): How the System Works — foundations",
  "Micromobility Rules (Signature): Pre-Trip Inspection — foundations",
  "Micromobility Rules (Signature): Warning Signs Decoded — foundations",
  "Micromobility Rules (Signature): Tires: The Critical Contact — foundations",
  "Micromobility Rules (Signature): Brakes: Your Life Depends on Them — foundations",
  "Micromobility Rules (Signature): Lights and Visibility — foundations",
  "Micromobility Rules (Signature): Loading and Weight — foundations",
  "Micromobility Rules (Signature): Weather Driving — foundations",
  "Micromobility Rules (Signature): Night Operations — foundations",
  "Micromobility Rules (Signature): Emergency Procedures — foundations",
  "Micromobility Rules (Signature): Breakdown Kit Essentials — foundations",
  "Micromobility Rules (Signature): Maintenance Schedules — foundations"
 ],
 "compounded": [
  "Micromobility Rules (Signature): Fuel and Energy Smart — compounded",
  "Micromobility Rules (Signature): Rules of the Road Refresher — compounded",
  "Micromobility Rules (Signature): Sharing the Road — compounded",
  "Micromobility Rules (Signature): Micromobility Rules — compounded",
  "Micromobility Rules (Signature): Crossing Borders Prepared — compounded",
  "Micromobility Rules (Signature): Documentation to Carry — compounded",
  "Micromobility Rules (Signature): Insurance for Your Mode — compounded",
  "Micromobility Rules (Signature): Planning Long Trips — compounded",
  "Micromobility Rules (Signature): Passengers and Cargo Safety — compounded",
  "Micromobility Rules (Signature): New Drivers and Training — compounded",
  "Micromobility Rules (Signature): Dealing With Traffic Stops and Citations — compounded",
  "Micromobility Rules (Signature): Winterizing Your Vehicle — compounded"
 ],
 "advanced": [
  "Micromobility Rules (Signature): Advanced: Defensive Mastery — advanced",
  "Micromobility Rules (Signature): Advanced: Adverse Conditions Expert — advanced",
  "Micromobility Rules (Signature): Advanced: Towing and Hauling — advanced",
  "Micromobility Rules (Signature): Advanced: Fleet Management — advanced",
  "Micromobility Rules (Signature): Advanced: Incident Investigation — advanced",
  "Micromobility Rules (Signature): Advanced: Teaching Others — advanced",
  "Micromobility Rules (Signature): Advanced: Regulatory Compliance — advanced",
  "Micromobility Rules (Signature): Advanced: Technology and ADAS — advanced",
  "Micromobility Rules (Signature): Advanced: Emergency Response Driving — advanced",
  "Micromobility Rules (Signature): Advanced: The Lifetime Safe Operator — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Micromobility Rules Signature Database — structural study\n"
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
var gen={version:'jahdb-micromobility-rules-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('micromobility-rules-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
