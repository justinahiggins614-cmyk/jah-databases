(function(){'use strict';
/* JAH The Human Intelligence Database generator — jahdb-human-intelligence-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HUMI-";
var FIELDS=["intelligence-scale abilities"];
var TOPICS={
 "intelligence-scale abilities": [
  "Fluid Reasoning (Gf) \u2014 intelligence-scale abilities",
  "Fluid Reasoning (Gf) (Signature Edition) \u2014 intelligence-scale abilities",
  "Crystallized Knowledge (Gc) \u2014 intelligence-scale abilities",
  "Crystallized Knowledge (Gc) (Signature Edition) \u2014 intelligence-scale abilities",
  "Logical-Mathematical Intelligence \u2014 intelligence-scale abilities",
  "Logical-Mathematical Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Linguistic Intelligence \u2014 intelligence-scale abilities",
  "Linguistic Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Spatial-Visual Intelligence \u2014 intelligence-scale abilities",
  "Spatial-Visual Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Musical Intelligence \u2014 intelligence-scale abilities",
  "Musical Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Bodily-Kinesthetic Intelligence \u2014 intelligence-scale abilities",
  "Bodily-Kinesthetic Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Interpersonal Intelligence \u2014 intelligence-scale abilities",
  "Interpersonal Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Intrapersonal Intelligence \u2014 intelligence-scale abilities",
  "Intrapersonal Intelligence (Signature Edition) \u2014 intelligence-scale abilities",
  "Emotional Intelligence (EQ) \u2014 intelligence-scale abilities",
  "Emotional Intelligence (EQ) (Signature Edition) \u2014 intelligence-scale abilities",
  "Savant Memory and Calculation Abilities \u2014 intelligence-scale abilities",
  "Savant Memory and Calculation Abilities (Signature Edition) \u2014 intelligence-scale abilities",
  "Genius-Level Creativity \u2014 intelligence-scale abilities",
  "Genius-Level Creativity (Signature Edition) \u2014 intelligence-scale abilities"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Human Intelligence — "+safe+"\n"
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
    name:topic+' — human intelligence ability',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A human intelligence ability of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-human-intelligence-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('human-intelligence',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
