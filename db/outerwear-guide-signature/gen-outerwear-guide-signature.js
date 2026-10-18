(function(){'use strict';
/* JAH The Outerwear Guide Database generator — jahdb-outerwear-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OTGDS-";
var FIELDS=["Outerwear Foundations", "The Coats", "Outerwear Mastery"];
var TOPICS={
 "Outerwear Foundations": [
  "The Layering System",
  "The Coat Lengths",
  "The Wool Coat",
  "The Puffer",
  "The Parka",
  "The Trench Coat",
  "The Peacoat",
  "The Overcoat",
  "The Leather Jacket",
  "The Denim Jacket Layer",
  "The Bomber",
  "The Field Jacket Layer"
 ],
 "The Coats": [
  "The Rain Shell",
  "The Windbreaker",
  "The Fleece Mid",
  "The Down Fill",
  "The Synthetic Fill",
  "The Hardshell",
  "The Softshell",
  "The Cape",
  "The Poncho Layer",
  "The Vest Layer",
  "The Anorak",
  "The Duffle Coat",
  "The Shearling",
  "The Quilted Jacket"
 ],
 "Outerwear Mastery": [
  "The Coat Care",
  "The Reproofing",
  "The Outerwear Oath",
  "The Outerwear Legacy",
  "The Cocoon Coat",
  "The Wrap Coat",
  "The Storm Flap",
  "The Packable Down"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# outer — "+safe+"\n"
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
    name:topic+' — outerwear guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A outerwear guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"outer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-outerwear-guide-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('outerwear-guide-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
