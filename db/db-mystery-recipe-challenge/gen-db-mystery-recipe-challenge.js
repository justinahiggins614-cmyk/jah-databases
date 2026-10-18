(function(){'use strict';
/* JAH The Mystery Recipe Challenge Database generator — jahdb-db-mystery-recipe-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MRC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Mystery Box Rules",
  "Challenge 1: Chicken, Lemon, Capers",
  "Challenge 2: Eggs, Potatoes, Onion",
  "Challenge 3: Canned Tuna, White Beans",
  "Challenge 4: Ground Beef, Cabbage",
  "Challenge 5: Pasta, Cherry Tomatoes",
  "Reading a Mystery Box",
  "Pantry Staples Allowed",
  "Time Management Under Pressure",
  "Plating the Challenge Dish",
  "Challenge 0: The Pantry Raid"
 ],
 "Compounded": [
  "Challenge 6: Salmon, Miso, Bok Choy",
  "Challenge 7: Pork Tenderloin, Apples",
  "Challenge 8: Shrimp, Coconut Milk",
  "Challenge 9: Lentils, Carrots, Cumin",
  "Challenge 10: Steak, Blue Cheese",
  "Vegetarian Mystery Boxes",
  "Dessert Mystery Boxes",
  "Team Challenge Format",
  "Judging Criteria Decoded",
  "Challenge 11: Tofu, Peanut, Lime",
  "Challenge 12: Sausage, Peppers, Polenta",
  "Challenge 13: Duck, Orange, Fennel"
 ],
 "Advanced": [
  "Advanced: The Iron Box (10 Ingredients)",
  "Advanced: Mystery Box League Play",
  "The Mystery Recipe Challenge Hall of Fame",
  "Advanced: The 30-Minute Lightning Round",
  "Advanced: Mystery Box for Kids",
  "Advanced: The Chopped-Style Tournament",
  "Advanced: Cooking for Dietary Restrictions",
  "Advanced: The Finale — Your Signature Box",
  "Advanced: Mystery Box Travel Edition",
  "Advanced: The Judge's Table",
  "The Mystery Recipe Challenge Encyclopedia"
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
    name:topic+' — recipe challenge record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A recipe challenge record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-mystery-recipe-challenge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mystery-recipe-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
