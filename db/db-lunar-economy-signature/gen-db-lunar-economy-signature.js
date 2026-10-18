(function(){'use strict';
/* JAH The Lunar Economy Signature Database generator — jahdb-db-lunar-economy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CLEDS-";
var FIELDS=["Resources","Industries","Trade"];
var TOPICS={
 "Resources": [
  "Lunar Water Mining (Signature Edition) \u2014 Resources",
  "The Signature Method for Lunar Water Mining \u2014 Resources",
  "Regolith Construction (Signature Edition) \u2014 Resources",
  "The Signature Method for Regolith Construction \u2014 Resources",
  "Helium-3 Prospecting (Signature Edition) \u2014 Resources",
  "The Signature Method for Helium-3 Prospecting \u2014 Resources",
  "The Lunar Economist's Method (Signature Edition) \u2014 Resources",
  "The Signature Method for The Lunar Economist's Method \u2014 Resources"
 ],
 "Industries": [
  "Lunar Power Beaming (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Power Beaming \u2014 Industries",
  "Lunar Manufacturing (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Manufacturing \u2014 Industries",
  "Lunar Tourism (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Tourism \u2014 Industries",
  "Lunar Science Services (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Science Services \u2014 Industries",
  "Lunar Agriculture (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Agriculture \u2014 Industries",
  "Lunar Settlement Economics (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Settlement Economics \u2014 Industries",
  "Lunar Data Services (Signature Edition) \u2014 Industries",
  "The Signature Method for Lunar Data Services \u2014 Industries"
 ],
 "Trade": [
  "Cislunar Trade Routes (Signature Edition) \u2014 Trade",
  "The Signature Method for Cislunar Trade Routes \u2014 Trade",
  "Lunar Finance (Signature Edition) \u2014 Trade",
  "The Signature Method for Lunar Finance \u2014 Trade",
  "Lunar Law and Governance (Signature Edition) \u2014 Trade",
  "The Signature Method for Lunar Law and Governance \u2014 Trade",
  "Lunar Labor (Signature Edition) \u2014 Trade",
  "The Signature Method for Lunar Labor \u2014 Trade",
  "Lunar Exports (Signature Edition) \u2014 Trade",
  "The Signature Method for Lunar Exports \u2014 Trade",
  "Lunar Heritage Sites (Signature Edition) \u2014 Trade",
  "The Signature Method for Lunar Heritage Sites \u2014 Trade"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Lunar Economy Study — "+safe+"\n"
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
    name:topic+' — lunar economy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A lunar economy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-lunar-economy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-lunar-economy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
