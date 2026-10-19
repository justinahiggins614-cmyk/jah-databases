(function(){'use strict';
/* JAH The Device Blueprint Database generator — jahdb-blueprint-devices-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BDP-";
var FIELDS=["Climate","Computing","Home","Kitchen"];
var TOPICS={
 "Climate": [
  "Air Conditioner - Compact Architectural Blueprint - Climate",
  "Ceiling Fan - Compact Architectural Blueprint - Climate",
  "Air Conditioner - Standard Architectural Blueprint - Climate",
  "Ceiling Fan - Standard Architectural Blueprint - Climate",
  "Air Conditioner - Grand Architectural Blueprint - Climate",
  "Ceiling Fan - Grand Architectural Blueprint - Climate"
 ],
 "Computing": [
  "Desktop Computer - Compact Architectural Blueprint - Computing",
  "Laptop - Compact Architectural Blueprint - Computing",
  "Smartphone - Compact Architectural Blueprint - Computing",
  "Desktop Computer - Standard Architectural Blueprint - Computing",
  "Laptop - Standard Architectural Blueprint - Computing",
  "Smartphone - Standard Architectural Blueprint - Computing",
  "Desktop Computer - Grand Architectural Blueprint - Computing",
  "Laptop - Grand Architectural Blueprint - Computing",
  "Smartphone - Grand Architectural Blueprint - Computing"
 ],
 "Home": [
  "Television - Compact Architectural Blueprint - Home",
  "Vacuum Cleaner - Compact Architectural Blueprint - Home",
  "LED Lamp - Compact Architectural Blueprint - Home",
  "Television - Standard Architectural Blueprint - Home",
  "Vacuum Cleaner - Standard Architectural Blueprint - Home",
  "LED Lamp - Standard Architectural Blueprint - Home",
  "Television - Grand Architectural Blueprint - Home"
 ],
 "Kitchen": [
  "Refrigerator - Compact Architectural Blueprint - Kitchen",
  "Washing Machine - Compact Architectural Blueprint - Kitchen",
  "Microwave Oven - Compact Architectural Blueprint - Kitchen",
  "Toaster Oven - Compact Architectural Blueprint - Kitchen",
  "Refrigerator - Standard Architectural Blueprint - Kitchen",
  "Washing Machine - Standard Architectural Blueprint - Kitchen",
  "Microwave Oven - Standard Architectural Blueprint - Kitchen",
  "Toaster Oven - Standard Architectural Blueprint - Kitchen",
  "Refrigerator - Grand Architectural Blueprint - Kitchen",
  "Washing Machine - Grand Architectural Blueprint - Kitchen",
  "Microwave Oven - Grand Architectural Blueprint - Kitchen",
  "Toaster Oven - Grand Architectural Blueprint - Kitchen"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Devices Blueprint Study — "+safe+"\n"
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
    name:topic+' — device blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A device blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-devices-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-devices',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
