(function(){'use strict';
/* JAH The Self-Building Cities Future Technology Database generator — jahdb-futuretech-66-self-building-cities-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT66-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "c. 100 CE: Rome Builds Modular - Foundations",
  "1830s: the Balloon Frame - Foundations",
  "1908: Sears Sells Houses by Mail - Foundations",
  "1947: Levittown - the Factory Suburb - Foundations",
  "1967: Habitat 67 - Modular Architecture - Foundations",
  "1970s: Manufactured Housing - Foundations",
  "1980s: Japan Automates Construction - Foundations",
  "1986: 3D Printing Is Born - Foundations",
  "2004: Contour Crafting - Foundations",
  "2008: D-Shape Prints Stone - Foundations",
  "2014: 10 Houses in a Day - Foundations"
 ],
 "Compounded": [
  "2015: Printing Goes Vertical - Compounded",
  "2016: Dubai's Printed Office - Compounded",
  "2017: the Mobile House Printer - Compounded",
  "2018: the Permitted Printed Home - Compounded",
  "2019: Printing for the Homeless - Compounded",
  "2021: Germany Prints a Home - Compounded",
  "2021: the Printed Bridge - Compounded",
  "2022: 100 Printed Homes - Compounded",
  "2023: Robots Draw the Blueprints - Compounded",
  "2023: the Robot Mason - Compounded",
  "2024: Printing Goes High-Rise - Compounded",
  "2025: the Site Gets a Brain - Compounded"
 ],
 "Advanced": [
  "Robot-Built Neighborhoods - Advanced",
  "Self-Assembling Structures - Advanced",
  "Cities Printed in Place - Advanced",
  "Swarm Construction - Advanced",
  "Printed Infrastructure - Advanced",
  "Self-Repairing Buildings - Advanced",
  "Reconfiguring Cities - Advanced",
  "Printed Disaster Recovery - Advanced",
  "Off-World Construction - Advanced",
  "The Self-Maintaining City - Advanced",
  "The Everyday Self-Building City - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — self-building city record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A self-building city record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-66-self-building-cities-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-66-self-building-cities-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-66-self-building-cities',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
