(function(){'use strict';
/* JAH The Global Learning Access Signature Database generator — jahdb-db-global-learning-access-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGLAS-";
var FIELDS=["The Schools","The Connection","The Content"];
var TOPICS={
 "The Schools": [
  "The School for All (Signature Edition) \u2014 The Schools",
  "The Signature Method for The School for All \u2014 The Schools",
  "The Girls' Classroom (Signature Edition) \u2014 The Schools",
  "The Signature Method for The Girls' Classroom \u2014 The Schools",
  "The Teacher Corps (Signature Edition) \u2014 The Schools",
  "The Signature Method for The Teacher Corps \u2014 The Schools",
  "The Mentor Network (Signature Edition) \u2014 The Schools",
  "The Signature Method for The Mentor Network \u2014 The Schools",
  "The Inclusive Classroom (Signature Edition) \u2014 The Schools",
  "The Signature Method for The Inclusive Classroom \u2014 The Schools",
  "The Refugee Classroom (Signature Edition) \u2014 The Schools",
  "The Signature Method for The Refugee Classroom \u2014 The Schools",
  "The Access Advocate's Method (Signature Edition) \u2014 The Schools",
  "The Signature Method for The Access Advocate's Method \u2014 The Schools"
 ],
 "The Connection": [
  "The Connected Learner (Signature Edition) \u2014 The Connection",
  "The Signature Method for The Connected Learner \u2014 The Connection",
  "The Learning Device (Signature Edition) \u2014 The Connection",
  "The Signature Method for The Learning Device \u2014 The Connection",
  "The Radio School (Signature Edition) \u2014 The Connection",
  "The Signature Method for The Radio School \u2014 The Connection",
  "The Learning Finance (Signature Edition) \u2014 The Connection",
  "The Signature Method for The Learning Finance \u2014 The Connection"
 ],
 "The Content": [
  "The Mother-Tongue Library (Signature Edition) \u2014 The Content",
  "The Signature Method for The Mother-Tongue Library \u2014 The Content",
  "The Open Library (Signature Edition) \u2014 The Content",
  "The Signature Method for The Open Library \u2014 The Content",
  "The Lifelong Campus (Signature Edition) \u2014 The Content",
  "The Signature Method for The Lifelong Campus \u2014 The Content",
  "The Learning Measure (Signature Edition) \u2014 The Content",
  "The Signature Method for The Learning Measure \u2014 The Content",
  "The Employer Classroom (Signature Edition) \u2014 The Content",
  "The Signature Method for The Employer Classroom \u2014 The Content",
  "The Sign Language Library (Signature Edition) \u2014 The Content",
  "The Signature Method for The Sign Language Library \u2014 The Content"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Learning Access Study — "+safe+"\n"
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
    name:topic+' — learning access record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A learning access record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-global-learning-access-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-global-learning-access-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
