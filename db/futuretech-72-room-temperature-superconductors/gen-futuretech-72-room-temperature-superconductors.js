(function(){'use strict';
/* JAH The Room-Temperature Superconductors Future Technology Database generator — jahdb-futuretech-72-room-temperature-superconductors-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT72-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1911: Onnes Finds Zero Resistance - Foundations",
  "1933: the Meissner Effect - Foundations",
  "1957: BCS Theory - Foundations",
  "1962: the Josephson Junction - Foundations",
  "1973: 23 Kelvin - the Bar - Foundations",
  "1986: Cuprates - the Ceramic Shock - Foundations",
  "1987: YBCO - Above Liquid Nitrogen - Foundations",
  "1988: 110 Kelvin - Foundations",
  "1993: 138K - the Standing Record - Foundations",
  "2001: MgB2 - the Simple Surprise - Foundations",
  "2008: Iron Pnictides - Foundations"
 ],
 "Compounded": [
  "2015: 203K Under Pressure - Compounded",
  "2019: 250K - So Close - Compounded",
  "2019: Nickelates - Compounded",
  "2020: the Claim and the Retraction - Compounded",
  "2023: LK-99 Summer - Compounded",
  "2023: the Second Retraction - Compounded",
  "2024: Careful Hydrides - Compounded",
  "2025: Ambient Superconductor Hunts - Compounded",
  "Verified Room-Temperature Superconductivity - Compounded",
  "Ambient-Pressure Room-Temp - Compounded",
  "Superconducting Wire - Compounded",
  "The Lossless Grid - Compounded"
 ],
 "Advanced": [
  "Cheap MRI Everywhere - Advanced",
  "Maglev Everywhere - Advanced",
  "Fusion's Cheap Magnets - Advanced",
  "Superconducting Electronics - Advanced",
  "Superconducting Motors - Advanced",
  "Maglev Cars - Advanced",
  "Quantum at Scale - Advanced",
  "Room-Temp Quantum Chips - Advanced",
  "Superconductors at Home - Advanced",
  "The Lossless Civilization - Advanced",
  "Everyday Superconductors - Working Version - Advanced"
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
    name:topic+' — room-temperature superconductor record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A room-temperature superconductor record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-72-room-temperature-superconductors-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-72-room-temperature-superconductors-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-72-room-temperature-superconductors',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
