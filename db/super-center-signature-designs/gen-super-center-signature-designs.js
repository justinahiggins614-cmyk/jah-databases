(function(){'use strict';
/* JAH The Signature Super Center Designs Database generator — jahdb-super-center-signature-designs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCD-";
var FIELDS=["architecture", "structure", "interior", "systems"];
var TOPICS={"architecture": ["The Grand Atrium Entry Blueprint \u2014 architecture", "The Main Retail Floor Plan \u2014 architecture", "The Services Wing Floor Plan \u2014 architecture", "The Community Hall Blueprint \u2014 architecture", "The Food Hall Floor Plan \u2014 architecture", "The Learning Wing Blueprint \u2014 architecture", "The Rooftop Terrace Plan \u2014 architecture", "The Facade and Signage Elevation Plan \u2014 architecture"], "structure": ["The Foundation and Footings Plan \u2014 structure", "The Steel Frame Structural Plan \u2014 structure", "The Roof Structure and Canopy Plan \u2014 structure", "The Seismic and Wind Bracing Plan \u2014 structure", "The Mezzanine and Balcony Plan \u2014 structure", "The Loading Dock Structure Plan \u2014 structure"], "interior": ["The Aisle and Department Layout Plan \u2014 interior", "The Checkout and Service Counter Plan \u2014 interior", "The Lighting Fixture Plan \u2014 interior", "The Flooring and Finishes Schedule \u2014 interior", "The Acoustics Treatment Plan \u2014 interior", "The Wayfinding Signage Interior Plan \u2014 interior", "The Restroom and Family Suite Plan \u2014 interior", "The Food Service Kitchen Plan \u2014 interior"], "systems": ["The HVAC Zoning Plan \u2014 systems", "The Electrical Distribution Plan \u2014 systems", "The Plumbing and Sanitation Plan \u2014 systems", "The Fire Protection and Sprinkler Plan \u2014 systems", "The Life Safety and Egress Plan \u2014 systems", "The Security and Camera Plan \u2014 systems", "The Network and Communications Plan \u2014 systems", "The Solar Array and Energy Plan \u2014 systems", "The Rainwater Harvesting Plan \u2014 systems", "The Elevator and Lift Plan \u2014 systems", "The Waste and Recycling Plan \u2014 systems", "The Building Automation Control Plan \u2014 systems"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH The Signature Super Center Designs Database \u2014 structural study\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 structural study record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A structural blueprint record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"super-center-signature-designs-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-super-center-signature-designs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('super-center-signature-designs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
