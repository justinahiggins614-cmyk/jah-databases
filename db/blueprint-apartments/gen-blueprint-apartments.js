(function(){'use strict';
/* JAH The Apartment Blueprint Database generator — jahdb-blueprint-apartments-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BATP-";
var FIELDS=["2BR","3BR+","Specialty","Studio / 1BR"];
var TOPICS={
 "2BR": [
  "Two-Bedroom Apartment - Compact Architectural Blueprint - 2BR",
  "Garden Apartment - Compact Architectural Blueprint - 2BR",
  "Duplex Apartment - Compact Architectural Blueprint - 2BR",
  "Two-Bedroom Apartment - Standard Architectural Blueprint - 2BR",
  "Garden Apartment - Standard Architectural Blueprint - 2BR",
  "Duplex Apartment - Standard Architectural Blueprint - 2BR",
  "Two-Bedroom Apartment - Grand Architectural Blueprint - 2BR",
  "Garden Apartment - Grand Architectural Blueprint - 2BR"
 ],
 "3BR+": [
  "Three-Bedroom Apartment - Compact Architectural Blueprint - 3BR+",
  "Courtyard Apartment Block - Compact Architectural Blueprint - 3BR+",
  "Three-Bedroom Apartment - Standard Architectural Blueprint - 3BR+",
  "Courtyard Apartment Block - Standard Architectural Blueprint - 3BR+",
  "Three-Bedroom Apartment - Grand Architectural Blueprint - 3BR+"
 ],
 "Specialty": [
  "Loft Apartment - Compact Architectural Blueprint - Specialty",
  "Penthouse - Compact Architectural Blueprint - Specialty",
  "Senior Living Unit - Compact Architectural Blueprint - Specialty",
  "Student Housing Unit - Compact Architectural Blueprint - Specialty",
  "Loft Apartment - Standard Architectural Blueprint - Specialty",
  "Penthouse - Standard Architectural Blueprint - Specialty",
  "Senior Living Unit - Standard Architectural Blueprint - Specialty",
  "Student Housing Unit - Standard Architectural Blueprint - Specialty",
  "Loft Apartment - Grand Architectural Blueprint - Specialty",
  "Penthouse - Grand Architectural Blueprint - Specialty",
  "Senior Living Unit - Grand Architectural Blueprint - Specialty",
  "Student Housing Unit - Grand Architectural Blueprint - Specialty"
 ],
 "Studio / 1BR": [
  "Studio Apartment - Compact Architectural Blueprint - Studio / 1BR",
  "One-Bedroom Apartment - Compact Architectural Blueprint - Studio / 1BR",
  "Micro-Apartment - Compact Architectural Blueprint - Studio / 1BR",
  "Studio Apartment - Standard Architectural Blueprint - Studio / 1BR",
  "One-Bedroom Apartment - Standard Architectural Blueprint - Studio / 1BR",
  "Micro-Apartment - Standard Architectural Blueprint - Studio / 1BR",
  "Studio Apartment - Grand Architectural Blueprint - Studio / 1BR",
  "One-Bedroom Apartment - Grand Architectural Blueprint - Studio / 1BR",
  "Micro-Apartment - Grand Architectural Blueprint - Studio / 1BR"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Apartments Blueprint Study — "+safe+"\n"
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
    name:topic+' — apartment blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A apartment blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-blueprint-apartments-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-apartments',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
