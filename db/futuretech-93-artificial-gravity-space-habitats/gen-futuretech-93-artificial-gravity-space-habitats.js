(function(){'use strict';
/* JAH The Artificial-Gravity Space Habitats Future Technology Database generator — jahdb-futuretech-93-artificial-gravity-space-habitats-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT93-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1903: the Wheel Imagined - Foundations",
  "1928: Noordung's Wheel - Foundations",
  "1950s: Von Braun's Wheel - Foundations",
  "1968: 2001's Wheel - Foundations",
  "1973: Skylab - Foundations",
  "1986: Mir - Foundations",
  "1998: the ISS - Foundations",
  "2000s: Spin Studies - Foundations",
  "2011: Nautilus-X - Foundations",
  "2016: BEAM - Foundations",
  "2019: the Gateway - Foundations"
 ],
 "Compounded": [
  "2021: Orbital Reef - Compounded",
  "2021: Starlab - Compounded",
  "2023: Haven-1 - Compounded",
  "2020: Axiom - Compounded",
  "2024: Gravitics - Compounded",
  "2025: Private Orbit - Compounded",
  "2025: Spin Science - Compounded",
  "The Rotating Station - Compounded",
  "The Gravity Wheel - Compounded",
  "The Stanford Torus - Compounded",
  "The O'Neill Cylinder - Compounded",
  "The Gravity Deck - Compounded"
 ],
 "Advanced": [
  "The Rotating City - Advanced",
  "The Gravity Hospital - Advanced",
  "The Space Suburb - Advanced",
  "The Rotating Nation - Advanced",
  "The Gravity Civilization - Advanced",
  "The Spun World - Advanced",
  "The Comfortable Orbit - Advanced",
  "The Gravity Economy - Advanced",
  "The Orbital Home - Advanced",
  "The 1G Station - Advanced",
  "Everyday Artificial Gravity - Working Version - Advanced"
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
    name:topic+' — artificial-gravity habitat record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A artificial-gravity habitat record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-93-artificial-gravity-space-habitats-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-93-artificial-gravity-space-habitats-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-93-artificial-gravity-space-habitats',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
