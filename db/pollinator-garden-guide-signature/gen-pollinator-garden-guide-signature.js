(function(){'use strict';
/* JAH Pollinator Garden Guide Database generator — jahdb-pollinator-garden-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-POLLGGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Why Pollinators Matter (Signature Edition)", "Know Your Pollinators (Signature Edition)", "Native Plants (Signature Edition)", "Bloom Succession (Signature Edition)", "Planting in Drifts (Signature Edition)", "Milkweed for Monarchs (Signature Edition)", "Nesting Habitat (Signature Edition)", "Water Sources (Signature Edition)", "Pesticide Elimination (Signature Edition)", "Leave the Leaves (Signature Edition)", "Reducing Lawn (Signature Edition)"], "Compounded": ["Container Pollinator Gardens (Signature Edition)", "Community Habitat (Signature Edition)", "Teaching Pollinator Gardening (Signature Edition)", "Certification Programs (Signature Edition)", "The Annual Habitat Review (Signature Edition)", "Bee Hotels (Signature Edition)", "Butterfly Puddling (Signature Edition)", "Moth Gardens (Signature Edition)", "Hummingbird Gardens (Signature Edition)", "Beetle Pollinators (Signature Edition)", "Pollinator Lawns (Signature Edition)", "Hedgerows (Signature Edition)"], "Advanced": ["Green Roofs (Signature Edition)", "School Pollinator Gardens (Signature Edition)", "Pesticide-Free Nurseries (Signature Edition)", "Invasive Plants (Signature Edition)", "Climate-Resilient Habitat (Signature Edition)", "Monitoring Pollinators (Signature Edition)", "Photographing Pollinators (Signature Edition)", "Neighborhood Corridors (Signature Edition)", "Policy Advocacy (Signature Edition)", "The Joy of Pollinators (Signature Edition)", "Winter Habitat (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — garden guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — garden guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A garden guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"pollinator-garden-guide-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-pollinator-garden-guide-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("pollinator-garden-guide-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
