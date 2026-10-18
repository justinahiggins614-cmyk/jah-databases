(function(){'use strict';
/* JAH The Party Planning Database generator — jahdb-party-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRTY-";
var FIELDS=["Party Foundations","Birthdays","Milestones","Themes & Decor","Food & Drink","Hosting & Etiquette"];
var TOPICS={
 "Party Foundations": [
  "The Party Planning Formula - Party Foundations",
  "Party Budgets That Work - Party Foundations",
  "Invitations That Get RSVPs - Party Foundations",
  "The Party Timeline: Day-Of Execution - Party Foundations",
  "Party Venues: Home vs Rented - Party Foundations",
  "Entertainment and Activities - Party Foundations"
 ],
 "Birthdays": [
  "Kids' Birthday Parties by Age - Birthdays",
  "Adult Birthday Parties - Birthdays",
  "Surprise Parties That Actually Surprise - Birthdays",
  "Themed Birthday Parties - Birthdays",
  "Birthday Party Favors and Goodie Bags - Birthdays"
 ],
 "Milestones": [
  "Anniversary Parties - Milestones",
  "Baby Showers - Milestones",
  "Graduation Parties - Milestones",
  "Retirement Parties - Milestones",
  "Housewarming Parties - Milestones"
 ],
 "Themes & Decor": [
  "Choosing a Party Theme - Themes & Decor",
  "DIY Decorations That Look Professional - Themes & Decor",
  "The Photo Backdrop: Memories by Design - Themes & Decor",
  "Lighting That Transforms Parties - Themes & Decor",
  "Table Settings and Centerpieces - Themes & Decor",
  "Outdoor Party Setup - Themes & Decor"
 ],
 "Food & Drink": [
  "Party Food: How Much and What Kind - Food & Drink",
  "The Bar: Stocking and Serving - Food & Drink",
  "Signature Cocktails and Mocktails - Food & Drink",
  "Catering vs DIY Food - Food & Drink",
  "Dessert Tables and Cake Alternatives - Food & Drink",
  "Keeping Food Safe at Parties - Food & Drink"
 ],
 "Hosting & Etiquette": [
  "Being a Great Host - Hosting & Etiquette",
  "Being a Great Guest - Hosting & Etiquette",
  "Handling Party Problems Gracefully - Hosting & Etiquette",
  "Kids at Parties: Including Them Well - Hosting & Etiquette",
  "The Morning After: Cleanup and Thanks - Hosting & Etiquette",
  "Party Traditions Worth Starting - Hosting & Etiquette"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Party Planning Study — "+safe+"\n"
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
    name:topic+' — party planning guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A party planning guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"party-planning-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-party-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('party-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
