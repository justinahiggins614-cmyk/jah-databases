(function(){'use strict';
/* JAH The Unusual Museums Database Signature Database generator — jahdb-db-unusual-museums-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UMMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Makes a Museum Unusual?",
  "The Lunchbox Museum",
  "Finding Unusual Museums",
  "The Museum of Bad Art",
  "The Museum Road Trip",
  "The International Banana Museum",
  "The Museum Photography",
  "The Hair Museum",
  "The Museum with Kids",
  "The National Mustard Museum",
  "The Museum Year"
 ],
 "Compounded": [
  "The Salt and Pepper Shaker Museum",
  "The Museum Bucket List",
  "The Spam Museum",
  "The Museum Story",
  "The Neon Museum",
  "The Museum Gift Shop",
  "The Burlingame Museum of Pez",
  "The Museum Decade",
  "The Museum of Everyday Life",
  "The Museum Road Trip II",
  "The Icelandic Phallological Museum",
  "The Museum Solo"
 ],
 "Advanced": [
  "Advanced: The World's Most Unusual",
  "Advanced: The Museum Curator",
  "Advanced: Your Museum Ranking",
  "Advanced: The Museum Legacy",
  "Advanced: The Museum Passport",
  "Advanced: The Museum Book",
  "Advanced: The Museum Finale",
  "Advanced: The Museum Storyteller",
  "Advanced: The Museum Bucket List",
  "Advanced: The Museum Memoir",
  "The Unusual Museums Encyclopedia"
 ]
};
var DEMOKIND="travel-lab-demo";
var SAMPLEDESC="Sample records are complete real museum entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Travel Lab Demo — "+safe+"\n"
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
    name:topic+' — museum record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A museum record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-unusual-museums-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-unusual-museums-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
