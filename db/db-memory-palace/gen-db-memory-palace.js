(function(){'use strict';
/* JAH The Memory Palace Database Database generator — jahdb-db-memory-palace-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEMPAL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Remember: the grocery run",
  "Remember: the morning routine",
  "Remember: the color list",
  "Remember: the animal parade",
  "Remember: the number 1-2-3",
  "Remember: the planet hop",
  "Remember: the fruit basket",
  "Remember: the tool shed",
  "Remember: the seasons",
  "Remember: the first five presidents",
  "Remember: the rainbow"
 ],
 "Compounded": [
  "Remember: the 10-item shopping list",
  "Remember: the periodic table's first 10",
  "Remember: a 12-digit number",
  "Remember: the 8 planets in order",
  "Remember: the Great Lakes",
  "Remember: the cranial nerves trick",
  "Remember: a deck's order (first 8)",
  "Remember: the 7 continents",
  "Remember: the spelling of 'necessary'",
  "Remember: the order of operations",
  "Remember: the 5 oceans",
  "Remember: Henry VIII's wives"
 ],
 "Advanced": [
  "Remember: pi to 15 digits",
  "Remember: the 20 amino acids",
  "Remember: a 52-card deck order",
  "Remember: the US presidents in order (10)",
  "Remember: the NATO phonetic alphabet",
  "Remember: the first 20 elements",
  "Remember: binary to 16 bits",
  "Remember: the 12 cranial nerves",
  "Remember: the resistor color code",
  "Remember: the 9 planets debate (8 + Pluto)",
  "Remember: the metric prefixes"
 ]
};
var DEMOKIND="memory-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Memory Study — "+safe+"\n"
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
    name:topic+' — memory challenge record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A memory challenge record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-memory-palace-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-memory-palace',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
