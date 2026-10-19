(function(){'use strict';
/* JAH The Brake System Warning Signs Signature Database generator — jahdb-brake-system-warning-signs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BSWSS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Brake System Warning Signs (Signature): How the System Works — foundations",
  "Brake System Warning Signs (Signature): Pre-Trip Inspection — foundations",
  "Brake System Warning Signs (Signature): Warning Signs Decoded — foundations",
  "Brake System Warning Signs (Signature): Tires: The Critical Contact — foundations",
  "Brake System Warning Signs (Signature): Brakes: Your Life Depends on Them — foundations",
  "Brake System Warning Signs (Signature): Lights and Visibility — foundations",
  "Brake System Warning Signs (Signature): Loading and Weight — foundations",
  "Brake System Warning Signs (Signature): Weather Driving — foundations",
  "Brake System Warning Signs (Signature): Night Operations — foundations",
  "Brake System Warning Signs (Signature): Emergency Procedures — foundations",
  "Brake System Warning Signs (Signature): Breakdown Kit Essentials — foundations",
  "Brake System Warning Signs (Signature): Maintenance Schedules — foundations"
 ],
 "compounded": [
  "Brake System Warning Signs (Signature): Fuel and Energy Smart — compounded",
  "Brake System Warning Signs (Signature): Rules of the Road Refresher — compounded",
  "Brake System Warning Signs (Signature): Sharing the Road — compounded",
  "Brake System Warning Signs (Signature): Micromobility Rules — compounded",
  "Brake System Warning Signs (Signature): Crossing Borders Prepared — compounded",
  "Brake System Warning Signs (Signature): Documentation to Carry — compounded",
  "Brake System Warning Signs (Signature): Insurance for Your Mode — compounded",
  "Brake System Warning Signs (Signature): Planning Long Trips — compounded",
  "Brake System Warning Signs (Signature): Passengers and Cargo Safety — compounded",
  "Brake System Warning Signs (Signature): New Drivers and Training — compounded",
  "Brake System Warning Signs (Signature): Dealing With Traffic Stops and Citations — compounded",
  "Brake System Warning Signs (Signature): Winterizing Your Vehicle — compounded"
 ],
 "advanced": [
  "Brake System Warning Signs (Signature): Advanced: Defensive Mastery — advanced",
  "Brake System Warning Signs (Signature): Advanced: Adverse Conditions Expert — advanced",
  "Brake System Warning Signs (Signature): Advanced: Towing and Hauling — advanced",
  "Brake System Warning Signs (Signature): Advanced: Fleet Management — advanced",
  "Brake System Warning Signs (Signature): Advanced: Incident Investigation — advanced",
  "Brake System Warning Signs (Signature): Advanced: Teaching Others — advanced",
  "Brake System Warning Signs (Signature): Advanced: Regulatory Compliance — advanced",
  "Brake System Warning Signs (Signature): Advanced: Technology and ADAS — advanced",
  "Brake System Warning Signs (Signature): Advanced: Emergency Response Driving — advanced",
  "Brake System Warning Signs (Signature): Advanced: The Lifetime Safe Operator — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Brake System Warning Signs Signature Database — structural study\n"
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
var gen={version:'jahdb-brake-system-warning-signs-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('brake-system-warning-signs-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
