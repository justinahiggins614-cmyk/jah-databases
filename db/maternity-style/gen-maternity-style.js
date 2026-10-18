(function(){'use strict';
/* JAH The Maternity Style Database generator — jahdb-maternity-style-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MTST-";
var FIELDS=["Maternity Foundations", "Trimester Style", "Maternity Mastery"];
var TOPICS={
 "Maternity Foundations": [
  "The Bump Celebration",
  "The Comfort First",
  "The First Trimester",
  "The Second Trimester",
  "The Third Trimester",
  "The Empire Waist",
  "The Wrap Dress",
  "The Legging Essential",
  "The Maternity Jean",
  "The Bump Band",
  "The Nursing Ready",
  "The Supportive Bra"
 ],
 "Trimester Style": [
  "The Occasion Bump",
  "The Work Bump",
  "The Photoshoot",
  "The Gender Reveal",
  "The Baby Shower Look",
  "The Hospital Bag",
  "The Postpartum",
  "The Nursing Style",
  "The Capsule Bump",
  "The Rental Bump",
  "The Bump Loungewear",
  "The Bump Sleep"
 ],
 "Maternity Mastery": [
  "The Partner Match",
  "The Sibling Match",
  "The Maternity Oath",
  "The Maternity Legacy",
  "The Grandma Style",
  "The Bump on Budget",
  "The Hand-Me-Down Bump",
  "The Bump Flat Lay",
  "The Name Reveal",
  "The Going-Home Outfit"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# matern — "+safe+"\n"
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
    name:topic+' — maternity style record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A maternity style record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"matern-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-maternity-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('maternity-style',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
