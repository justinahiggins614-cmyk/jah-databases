(function(){'use strict';
/* JAH The Mocktail Mixology Database Signature Database generator — jahdb-db-mocktail-mixology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MOCS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Mocktail Philosophy",
  "Essential Bar Tools",
  "Simple Syrups, Elevated",
  "Citrus Mastery",
  "The Virgin Mojito",
  "Virgin Pina Colada",
  "Shirley Temple, Grown Up",
  "Arnold Palmer Variations",
  "Sparkling Refreshers",
  "Iced Teas and Lemonades",
  "Layered Sunset Drinks"
 ],
 "Compounded": [
  "Frozen Mocktails",
  "Bitters and Complexity",
  "Shrubs and Drinking Vinegars",
  "Mock Mules and Bucks",
  "Tiki Without Rum",
  "Coffee Mocktails",
  "Tea-Based Mocktails",
  "Batching for Parties",
  "Garnish Like a Pro",
  "Zero-Proof Spirit Alternatives",
  "Cucumber-Mint Cooler",
  "Watermelon Basil Smash"
 ],
 "Advanced": [
  "Advanced: House Syrup Program",
  "Advanced: Mocktail Tasting Flights",
  "Advanced: The Mocktail Menu",
  "The Mocktail Mixology Master Bar",
  "Advanced: Fermented Sodas",
  "Advanced: Mocktail and Food Pairing",
  "Advanced: The Soda Fountain Revival",
  "Advanced: Zero-Proof Bitters Deep Dive",
  "Advanced: Mocktail Catering",
  "Advanced: Seasonal Mocktail Calendar",
  "The Mocktail Mixology Encyclopedia"
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
    name:topic+' — mocktail record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mocktail record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-mocktail-mixology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mocktail-mixology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
