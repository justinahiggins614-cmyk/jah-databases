(function(){'use strict';
/* JAH The Floating Cities Future Technology Database — Signature Edition generator — jahdb-futuretech-70-floating-cities-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT70-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Floating Cities — The Uros - Centuries of Floating Life (Signature Edition)", "Floating Cities — Triton City - Fuller Dreams Floating (Signature Edition)", "Floating Cities — Oil Rigs - Towns at Sea (Signature Edition)", "Floating Cities — The World - Islands for Sale (Signature Edition)", "Floating Cities — the Seasteading Institute (Signature Edition)", "Floating Cities — Palm Jumeirah - the Sculpted Sea (Signature Edition)", "Floating Cities — Dutch Floating Neighborhoods (Signature Edition)", "Floating Cities — Schoonschip - the Floating Eco-Village (Signature Edition)", "Floating Cities — Oceanix City at the UN (Signature Edition)", "Floating Cities — Floating Solar Scales (Signature Edition)", "Floating Cities — Busan Says Yes (Signature Edition)"], "Compounded": ["Floating Cities — SeaPods for Sale (Signature Edition)", "Floating Cities — the Maldives Floats (Signature Edition)", "Floating Cities — Modular Ocean Platforms (Signature Edition)", "Floating Cities — Oxagon - the Floating Giga-City (Signature Edition)", "Floating Cities — Data Centers at Sea (Signature Edition)", "Floating Cities — Living on the Ocean (Signature Edition)", "Floating Cities — First Floating Homes Ready (Signature Edition)", "Floating Cities — Floating Districts Approved (Signature Edition)", "Floating Cities — The First Floating District (Signature Edition)", "Floating Cities — Self-Sufficient Floating Utilities (Signature Edition)", "Floating Cities — Floating Self-Governance (Signature Edition)", "Floating Cities — Floating Farms (Signature Edition)"], "Advanced": ["Floating Cities — Climate-Refuge Floating Cities (Signature Edition)", "Floating Cities — Reef-Restoring Ocean Cities (Signature Edition)", "Floating Cities — The Floating Metropolis (Signature Edition)", "Floating Cities — Floating Airports (Signature Edition)", "Floating Cities — Deep-Ocean Habitats (Signature Edition)", "Floating Cities — Floating Universities (Signature Edition)", "Floating Cities — The Ocean City Network (Signature Edition)", "Floating Cities — Floating Industry (Signature Edition)", "Floating Cities — Marine Permaculture Cities (Signature Edition)", "Floating Cities — The Ocean Civilization in Floating Cities (Signature Edition)", "Floating Cities — The Everyday Floating City - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Floating Cities study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-70-floating-cities-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-70-floating-cities-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
