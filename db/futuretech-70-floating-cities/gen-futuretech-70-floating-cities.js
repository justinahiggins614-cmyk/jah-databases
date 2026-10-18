(function(){'use strict';
/* JAH The Floating Cities Future Technology Database generator — jahdb-futuretech-70-floating-cities-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT70-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Uros - Centuries of Floating Life - Foundations",
  "1960s: Triton City - Fuller Dreams Floating - Foundations",
  "1980s: Oil Rigs - Towns at Sea - Foundations",
  "2003: The World - Islands for Sale - Foundations",
  "2008: the Seasteading Institute - Foundations",
  "2000s: Palm Jumeirah - the Sculpted Sea - Foundations",
  "2010s: Dutch Floating Neighborhoods - Foundations",
  "2021: Schoonschip - the Floating Eco-Village - Foundations",
  "2019: Oceanix City at the UN - Foundations",
  "2020: Floating Solar Scales - Foundations",
  "2021: Busan Says Yes - Foundations"
 ],
 "Compounded": [
  "2021: SeaPods for Sale - Compounded",
  "2022: the Maldives Floats - Compounded",
  "2023: Modular Ocean Platforms - Compounded",
  "2023: Oxagon - the Floating Giga-City - Compounded",
  "2024: Data Centers at Sea - Compounded",
  "2024: Living on the Ocean - Compounded",
  "2025: First Floating Homes Ready - Compounded",
  "2025: Floating Districts Approved - Compounded",
  "The First Floating District - Compounded",
  "Self-Sufficient Floating Utilities - Compounded",
  "Floating Self-Governance - Compounded",
  "Floating Farms - Compounded"
 ],
 "Advanced": [
  "Climate-Refuge Floating Cities - Advanced",
  "Reef-Restoring Ocean Cities - Advanced",
  "The Floating Metropolis - Advanced",
  "Floating Airports - Advanced",
  "Deep-Ocean Habitats - Advanced",
  "Floating Universities - Advanced",
  "The Ocean City Network - Advanced",
  "Floating Industry - Advanced",
  "Marine Permaculture Cities - Advanced",
  "The Ocean Civilization - Advanced",
  "The Everyday Floating City - Working Version - Advanced"
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
    name:topic+' — floating city record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A floating city record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-70-floating-cities-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-70-floating-cities-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-70-floating-cities',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
