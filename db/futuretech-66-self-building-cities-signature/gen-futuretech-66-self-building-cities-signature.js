(function(){'use strict';
/* JAH The Self-Building Cities Future Technology Database — Signature Edition generator — jahdb-futuretech-66-self-building-cities-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT66-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Self Building Cities — Rome Builds Modular (Signature Edition)", "Self Building Cities — the Balloon Frame (Signature Edition)", "Self Building Cities — Sears Sells Houses by Mail (Signature Edition)", "Self Building Cities — Levittown - the Factory Suburb (Signature Edition)", "Self Building Cities — Habitat 67 - Modular Architecture (Signature Edition)", "Self Building Cities — Manufactured Housing (Signature Edition)", "Self Building Cities — Japan Automates Construction (Signature Edition)", "Self Building Cities — 3D Printing Is Born (Signature Edition)", "Self Building Cities — Contour Crafting (Signature Edition)", "Self Building Cities — D-Shape Prints Stone (Signature Edition)", "Self Building Cities — 10 Houses in a Day (Signature Edition)"], "Compounded": ["Self Building Cities — Printing Goes Vertical (Signature Edition)", "Self Building Cities — Dubai's Printed Office (Signature Edition)", "Self Building Cities — the Mobile House Printer (Signature Edition)", "Self Building Cities — the Permitted Printed Home (Signature Edition)", "Self Building Cities — Printing for the Homeless (Signature Edition)", "Self Building Cities — Germany Prints a Home (Signature Edition)", "Self Building Cities — the Printed Bridge (Signature Edition)", "Self Building Cities — 100 Printed Homes (Signature Edition)", "Self Building Cities — Robots Draw the Blueprints (Signature Edition)", "Self Building Cities — the Robot Mason (Signature Edition)", "Self Building Cities — Printing Goes High-Rise (Signature Edition)", "Self Building Cities — the Site Gets a Brain (Signature Edition)"], "Advanced": ["Self Building Cities — Robot-Built Neighborhoods (Signature Edition)", "Self Building Cities — Self-Assembling Structures (Signature Edition)", "Self Building Cities — Cities Printed in Place (Signature Edition)", "Self Building Cities — Swarm Construction (Signature Edition)", "Self Building Cities — Printed Infrastructure (Signature Edition)", "Self Building Cities — Self-Repairing Buildings (Signature Edition)", "Self Building Cities — Reconfiguring Cities (Signature Edition)", "Self Building Cities — Printed Disaster Recovery (Signature Edition)", "Self Building Cities — Off-World Construction (Signature Edition)", "Self Building Cities — The Self-Maintaining City in Self-Building Cities (Signature Edition)", "Self Building Cities — The Everyday Self-Building City - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Self Building Cities study \u2014 "+safe+"\n"
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
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-66-self-building-cities-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-66-self-building-cities-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
