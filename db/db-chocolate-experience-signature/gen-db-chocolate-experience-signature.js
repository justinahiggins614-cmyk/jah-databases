(function(){'use strict';
/* JAH The Chocolate Experience Database Signature Database generator — jahdb-db-chocolate-experience-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Cacao: From Pod to Bean",
  "Dark, Milk, and White",
  "Tasting Chocolate Like a Pro",
  "Melting Without Seizing",
  "Ganache: The Mother Sauce",
  "Chocolate Chip Cookies, Perfected",
  "Brownies: Fudgy vs Cakey",
  "Hot Chocolate, Real Style",
  "Chocolate and Fruit Pairings",
  "Chocolate and Salt, Spice, Heat",
  "Storing Chocolate Right"
 ],
 "Compounded": [
  "Tempering Chocolate",
  "Truffles, Hand-Rolled",
  "Chocolate Cake, Ultimate",
  "Mousse: Air and Chocolate",
  "Chocolate Bark",
  "Drinking Chocolate Around the World",
  "Bean-to-Bar at Home",
  "Chocolate and Wine",
  "Vegan Chocolate Desserts",
  "Chocolate Sculpture Basics",
  "Chocolate-Covered Fruit",
  "Drinking Chocolate Mixes"
 ],
 "Advanced": [
  "Single-Origin Tasting Flight",
  "The Science of Snap and Gloss",
  "Chocolate Factory Tour Knowledge",
  "Advanced Truffle Collection Design",
  "Chocolate and Health: The Real Story",
  "The Chocolate Experience Masterclass",
  "Advanced: Chocolate and Cheese",
  "Advanced: Raw Cacao Desserts",
  "Advanced: Chocolate Subscription Tasting",
  "Advanced: The Craft Chocolate Map",
  "The Chocolate Experience Encyclopedia"
 ]
};
var DEMOKIND="food-lab-demo";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Food Lab Demo — "+safe+"\n"
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
    name:topic+' — chocolate record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A chocolate record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-chocolate-experience-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-chocolate-experience-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
