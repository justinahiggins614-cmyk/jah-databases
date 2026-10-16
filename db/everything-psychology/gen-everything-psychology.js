(function(){'use strict';
/* JAH The Everything Psychology Database generator — jahdb-everything-psychology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVPS-";
var FIELDS=["Cognitive","Developmental","Social","Personality","Clinical","Behavioral","Biological","Methods","Signature Psychology"];
var TOPICS={
 "Cognitive": [
  "Cognitive Psychology: Memory and Attention \u2014 Cognitive"
 ],
 "Developmental": [
  "Developmental Psychology: Lifespan Stages \u2014 Developmental"
 ],
 "Social": [
  "Social Psychology: Groups, Conformity, Persuasion \u2014 Social"
 ],
 "Personality": [
  "Personality: Traits and Theories \u2014 Personality"
 ],
 "Clinical": [
  "Abnormal Psychology: A Clinical Overview \u2014 Clinical"
 ],
 "Behavioral": [
  "Behavioral Psychology: Conditioning and Learning \u2014 Behavioral"
 ],
 "Biological": [
  "Biological Psychology: Brain and Behavior \u2014 Biological"
 ],
 "Methods": [
  "Research Methods in Psychology \u2014 Methods"
 ],
 "Signature Psychology": [
  "Signature Cognitive Pattern Engine (Signature Edition) \u2014 Signature Psychology",
  "Signature Behavior Mapper (Signature Edition) \u2014 Signature Psychology",
  "Signature Learning Optimizer (Signature Edition) \u2014 Signature Psychology",
  "Signature Mind Metrics (Signature Edition) \u2014 Signature Psychology"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Psychology — "+safe+"\n"
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
    name:topic+' — psychology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A psychology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-psychology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-psychology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
