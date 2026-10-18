(function(){'use strict';
/* JAH The Mushroom Discovery Database Database generator — jahdb-db-mushroom-discovery-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Mushroom Safety First",
  "What Is a Fungus?",
  "The Fly Agaric",
  "The Destroying Angel",
  "Oyster Mushrooms",
  "Chanterelles",
  "Morels",
  "Puffballs",
  "The Mycelium Network",
  "Spore Prints",
  "Mushroom Seasons"
 ],
 "Compounded": [
  "The Shiitake",
  "Lion's Mane",
  "Reishi",
  "Turkey Tail",
  "The Chaga",
  "Mushroom Cultivation Basics",
  "The Foray",
  "Dye Mushrooms",
  "The Stinkhorn",
  "Bioluminescent Mushrooms",
  "Mushroom Photography",
  "The Ink Cap"
 ],
 "Advanced": [
  "Advanced: The Amanita Family",
  "Advanced: Mycoremediation",
  "Advanced: The Truffle Hunt",
  "Advanced: Medicinal Mushroom Evidence",
  "Advanced: The Mycological Society",
  "Advanced: Your Fungi Year",
  "Advanced: The Poison Control File",
  "Advanced: The Lookalike Drill",
  "Advanced: The Cultivation Business",
  "Advanced: The Fungi Festival",
  "The Mushroom Discovery Encyclopedia"
 ]
};
var DEMOKIND="animals-lab-demo";
var SAMPLEDESC="Sample records are complete real fungi entries with safety warnings and real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nature Lab Demo — "+safe+"\n"
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
    name:topic+' — mushroom record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mushroom record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-db-mushroom-discovery-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mushroom-discovery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
