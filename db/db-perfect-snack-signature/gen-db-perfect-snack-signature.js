(function(){'use strict';
/* JAH The Perfect Snack Database Signature Database generator — jahdb-db-perfect-snack-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Snack Formula",
  "5-Minute Snacks",
  "Crunchy and Salty",
  "Sweet but Sensible",
  "High-Protein Snacks",
  "Snacks for Kids",
  "Movie Night Spreads",
  "Healthy Office Snacks",
  "Pre-Workout Fuel",
  "Post-Workout Recovery",
  "Party Snack Boards"
 ],
 "Compounded": [
  "Energy Bites and Bars",
  "Homemade Trail Mix",
  "Dips That Carry the Party",
  "Savory Baking: Crackers and Chips",
  "Sweet Baking: Cookies and Bars",
  "Fermented Snacks",
  "Cheese Course Snacking",
  "Global Snack Tour",
  "Snack Science: Why We Crave",
  "Freezer Snack Stash",
  "Spiced Nuts, Homemade",
  "Yogurt Parfait Bar"
 ],
 "Advanced": [
  "Advanced: The Perfect Snack Drawer",
  "Advanced: Hosting Snack Strategy",
  "Advanced: Snack Nutrition Deep Dive",
  "Advanced: The Zero-Waste Snack Kitchen",
  "The Perfect Snack Master System",
  "Advanced: The 100-Calorie Myth",
  "Advanced: Mindful Snacking Practice",
  "Advanced: Snack Pairing with Tea and Coffee",
  "Advanced: Travel Snack Kit",
  "Advanced: Hosting Bites Calculator",
  "The Perfect Snack Encyclopedia"
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
    name:topic+' — snack record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A snack record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-perfect-snack-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-perfect-snack-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
