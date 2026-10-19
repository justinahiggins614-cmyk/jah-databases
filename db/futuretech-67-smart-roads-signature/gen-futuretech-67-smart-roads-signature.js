(function(){'use strict';
/* JAH The Smart Roads Future Technology Database — Signature Edition generator — jahdb-futuretech-67-smart-roads-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT67-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Smart Roads — Roman Roads - the First Network (Signature Edition)", "Smart Roads — the First Traffic Signal (Signature Edition)", "Smart Roads — Lane Markings - the Road Speaks (Signature Edition)", "Smart Roads — the Interstate System (Signature Edition)", "Smart Roads — the Road Feels Traffic (Signature Edition)", "Smart Roads — Ramp Meters (Signature Edition)", "Smart Roads — the Road Talks (Signature Edition)", "Smart Roads — Electronic Tolling (Signature Edition)", "Smart Roads — the Road Watches (Signature Edition)", "Smart Roads — Smart Parking (Signature Edition)", "Smart Roads — Solar Roadways Goes Viral (Signature Edition)"], "Compounded": ["Smart Roads — Wattway - the Solar Road (Signature Edition)", "Smart Roads — Jinan's Solar Highway (Signature Edition)", "Smart Roads — the Road That Charges (Signature Edition)", "Smart Roads — Cars Talk to Roads (Signature Edition)", "Smart Roads — Connected Intersections (Signature Edition)", "Smart Roads — Michigan's Robot Road (Signature Edition)", "Smart Roads — Indiana's Charging Highway (Signature Edition)", "Smart Roads — C-V2X Spreads (Signature Edition)", "Smart Roads — Smart Road Pilots Multiply (Signature Edition)", "Smart Roads — V2X Gets Grammar (Signature Edition)", "Smart Roads — Charging Roads Expand (Signature Edition)", "Smart Roads — Highways That Charge (Signature Edition)"], "Advanced": ["Smart Roads — Self-Healing Pavement (Signature Edition)", "Smart Roads — Roads Talk to Every Car (Signature Edition)", "Smart Roads — Adaptive Lanes (Signature Edition)", "Smart Roads — Solar Roads at Scale (Signature Edition)", "Smart Roads — Self-Clearing Roads (Signature Edition)", "Smart Roads — The Road as Data Platform (Signature Edition)", "Smart Roads — Pedestrian-Aware Roads (Signature Edition)", "Smart Roads — Fair Congestion Pricing (Signature Edition)", "Smart Roads — Rural Smart Roads (Signature Edition)", "Smart Roads — The Sentient Highway (Signature Edition)", "Smart Roads — The Everyday Smart Road - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Smart Roads study \u2014 "+safe+"\n"
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
var gen={version:'jahdb-futuretech-67-smart-roads-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-67-smart-roads-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
