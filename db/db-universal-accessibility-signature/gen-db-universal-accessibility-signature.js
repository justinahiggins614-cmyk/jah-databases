(function(){'use strict';
/* JAH The Universal Accessibility Signature Database generator — jahdb-db-universal-accessibility-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CUADS-";
var FIELDS=["The Built World","The Digital World","The Services"];
var TOPICS={
 "The Built World": [
  "The Step-Free City (Signature Edition) \u2014 The Built World",
  "The Signature Method for The Step-Free City \u2014 The Built World",
  "The Accessible Transit (Signature Edition) \u2014 The Built World",
  "The Signature Method for The Accessible Transit \u2014 The Built World",
  "The Playable Playground (Signature Edition) \u2014 The Built World",
  "The Signature Method for The Playable Playground \u2014 The Built World",
  "The Visitable Home (Signature Edition) \u2014 The Built World",
  "The Signature Method for The Visitable Home \u2014 The Built World",
  "The Sensory-Friendly Spaces (Signature Edition) \u2014 The Built World",
  "The Signature Method for The Sensory-Friendly Spaces \u2014 The Built World",
  "The Access Designer's Method (Signature Edition) \u2014 The Built World",
  "The Signature Method for The Access Designer's Method \u2014 The Built World"
 ],
 "The Digital World": [
  "The Accessible Web (Signature Edition) \u2014 The Digital World",
  "The Signature Method for The Accessible Web \u2014 The Digital World",
  "The Captioned World (Signature Edition) \u2014 The Digital World",
  "The Signature Method for The Captioned World \u2014 The Digital World",
  "The Cognitively Accessible (Signature Edition) \u2014 The Digital World",
  "The Signature Method for The Cognitively Accessible \u2014 The Digital World",
  "The Co-Design Method (Signature Edition) \u2014 The Digital World",
  "The Signature Method for The Co-Design Method \u2014 The Digital World"
 ],
 "The Services": [
  "The Welcoming Service (Signature Edition) \u2014 The Services",
  "The Signature Method for The Welcoming Service \u2014 The Services",
  "The Accessible Emergency (Signature Edition) \u2014 The Services",
  "The Signature Method for The Accessible Emergency \u2014 The Services",
  "The Accessible Workplace (Signature Edition) \u2014 The Services",
  "The Signature Method for The Accessible Workplace \u2014 The Services",
  "The Inclusive School (Signature Edition) \u2014 The Services",
  "The Signature Method for The Inclusive School \u2014 The Services",
  "The Accessible Healthcare (Signature Edition) \u2014 The Services",
  "The Signature Method for The Accessible Healthcare \u2014 The Services",
  "The Accessible Culture (Signature Edition) \u2014 The Services",
  "The Signature Method for The Accessible Culture \u2014 The Services",
  "The Accessible Ballot (Signature Edition) \u2014 The Services",
  "The Signature Method for The Accessible Ballot \u2014 The Services"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Accessibility Study — "+safe+"\n"
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
    name:topic+' — accessibility design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A accessibility design record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-universal-accessibility-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-universal-accessibility-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
