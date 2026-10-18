(function(){'use strict';
/* JAH The Menswear Guide Database generator — jahdb-menswear-guide-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MNGDS-";
var FIELDS=["Menswear Foundations", "The Wardrobe", "Menswear Mastery"];
var TOPICS={
 "Menswear Foundations": [
  "The Menswear Fit",
  "The Suit Guide",
  "The Dress Shirt",
  "The Chinos",
  "The Polo",
  "The Oxford Shirt",
  "The T-Shirt Tier",
  "The Jeans Rotation",
  "The Blazer Move",
  "The Sweater Layer",
  "The Outerwear Pick",
  "The Shoe Lineup"
 ],
 "The Wardrobe": [
  "The Watch",
  "The Belt Match",
  "The Tie Edit",
  "The Pocket Square Move",
  "The Grooming Basics",
  "The Fragrance Choice",
  "The Casual Friday",
  "The Date Night Man",
  "The Wedding Guest Man",
  "The Gym to Street",
  "The Denim Jacket Man",
  "The Henley Layer",
  "The Cardigan Man",
  "The Bomber Man"
 ],
 "Menswear Mastery": [
  "The Capsule Man",
  "The Tailor Relationship",
  "The Menswear Oath",
  "The Menswear Legacy",
  "The Loafer Move",
  "The Boot Polish",
  "The Winter Layering",
  "The Summer Linen"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# men — "+safe+"\n"
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
    name:topic+' — menswear guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A menswear guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"men-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-menswear-guide-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('menswear-guide-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
