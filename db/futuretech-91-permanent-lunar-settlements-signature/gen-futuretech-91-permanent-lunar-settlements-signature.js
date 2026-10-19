(function(){'use strict';
/* JAH The Permanent Lunar Settlements Future Technology Database — Signature Edition generator — jahdb-futuretech-91-permanent-lunar-settlements-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT91-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Permanent Lunar Settlements — Voyage to the Moon (Signature Edition)", "Permanent Lunar Settlements — Verne's Moon Shot (Signature Edition)", "Permanent Lunar Settlements — the Rocket Equation (Signature Edition)", "Permanent Lunar Settlements — Von Braun's Moon (Signature Edition)", "Permanent Lunar Settlements — First Contact (Signature Edition)", "Permanent Lunar Settlements — Soft Landing (Signature Edition)", "Permanent Lunar Settlements — Apollo 11 (Signature Edition)", "Permanent Lunar Settlements — the Last Walk (Signature Edition)", "Permanent Lunar Settlements — Paper Moon Bases (Signature Edition)", "Permanent Lunar Settlements — Clementine (Signature Edition)", "Permanent Lunar Settlements — Water Confirmed (Signature Edition)"], "Compounded": ["Permanent Lunar Settlements — the Jade Rabbit (Signature Edition)", "Permanent Lunar Settlements — Artemis (Signature Edition)", "Permanent Lunar Settlements — the Far Side (Signature Edition)", "Permanent Lunar Settlements — Moon Rules (Signature Edition)", "Permanent Lunar Settlements — Artemis I (Signature Edition)", "Permanent Lunar Settlements — India's South Pole (Signature Edition)", "Permanent Lunar Settlements — Private Touchdown (Signature Edition)", "Permanent Lunar Settlements — Starship HLS (Signature Edition)", "Permanent Lunar Settlements — Artemis II Readied (Signature Edition)", "Permanent Lunar Settlements — The Moon Base (Signature Edition)", "Permanent Lunar Settlements — The Lunar Village (Signature Edition)", "Permanent Lunar Settlements — The Moon Town (Signature Edition)"], "Advanced": ["Permanent Lunar Settlements — Lunar Industry (Signature Edition)", "Permanent Lunar Settlements — The Moon City (Signature Edition)", "Permanent Lunar Settlements — Lunar Farming (Signature Edition)", "Permanent Lunar Settlements — The Lunar Economy (Signature Edition)", "Permanent Lunar Settlements — The Moon-Born (Signature Edition)", "Permanent Lunar Settlements — The Lunar Civilization (Signature Edition)", "Permanent Lunar Settlements — The Earth-Moon System (Signature Edition)", "Permanent Lunar Settlements — Lunar Tourism in Permanent Settlements (Signature Edition)", "Permanent Lunar Settlements — The Lunar Republic (Signature Edition)", "Permanent Lunar Settlements — The Settled Moon (Signature Edition)", "Permanent Lunar Settlements — Everyday Lunar Life - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Permanent Lunar Settlements study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-91-permanent-lunar-settlements-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-91-permanent-lunar-settlements-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
