(function(){'use strict';
/* JAH The Permanent Lunar Settlements Future Technology Database generator — jahdb-futuretech-91-permanent-lunar-settlements-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT91-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1638: Voyage to the Moon - Foundations",
  "1865: Verne's Moon Shot - Foundations",
  "1903: the Rocket Equation - Foundations",
  "1950s: Von Braun's Moon - Foundations",
  "1959: First Contact - Foundations",
  "1966: Soft Landing - Foundations",
  "1969: Apollo 11 - Foundations",
  "1972: the Last Walk - Foundations",
  "1970s: Paper Moon Bases - Foundations",
  "1994: Clementine - Foundations",
  "2009: Water Confirmed - Foundations"
 ],
 "Compounded": [
  "2013: the Jade Rabbit - Compounded",
  "2017: Artemis - Compounded",
  "2019: the Far Side - Compounded",
  "2020: Moon Rules - Compounded",
  "2022: Artemis I - Compounded",
  "2023: India's South Pole - Compounded",
  "2024: Private Touchdown - Compounded",
  "2024: Starship HLS - Compounded",
  "2025: Artemis II Readied - Compounded",
  "The Moon Base - Compounded",
  "The Lunar Village - Compounded",
  "The Moon Town - Compounded"
 ],
 "Advanced": [
  "Lunar Industry - Advanced",
  "The Moon City - Advanced",
  "Lunar Farming - Advanced",
  "The Lunar Economy - Advanced",
  "The Moon-Born - Advanced",
  "The Lunar Civilization - Advanced",
  "The Earth-Moon System - Advanced",
  "Lunar Tourism - Advanced",
  "The Lunar Republic - Advanced",
  "The Settled Moon - Advanced",
  "Everyday Lunar Life - Working Version - Advanced"
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
    name:topic+' — lunar settlement record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A lunar settlement record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-91-permanent-lunar-settlements-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-91-permanent-lunar-settlements-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-91-permanent-lunar-settlements',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
