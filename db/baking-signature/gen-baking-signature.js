(function(){'use strict';
/* JAH The Baking Signature Database generator — jahdb-baking-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BAKES-";
var FIELDS=["Breads","Cakes","Cookies","Pies & Tarts","Pastries","Frosting & Decorating","Troubleshooting"];
var TOPICS={
 "Breads": [
  "Bread Baking Fundamentals (Signature Edition) - Breads",
  "Yeast: Types and Handling (Signature Edition) - Breads",
  "Kneading and Gluten Development (Signature Edition) - Breads",
  "Sourdough Starters and Baking (Signature Edition) - Breads",
  "Quick Breads: Banana, Zucchini, and Soda (Signature Edition) - Breads",
  "Rolls, Bagels, and Specialty Breads (Signature Edition) - Breads"
 ],
 "Cakes": [
  "Cake Baking Fundamentals (Signature Edition) - Cakes",
  "Butter Cakes: Vanilla, Chocolate, and Classics (Signature Edition) - Cakes",
  "Sponge and Foam Cakes (Signature Edition) - Cakes",
  "Cheesecakes: Baked and No-Bake (Signature Edition) - Cakes",
  "Cupcakes and Mini Cakes (Signature Edition) - Cakes",
  "Sheet Cakes and Crowd Baking (Signature Edition) - Cakes"
 ],
 "Cookies": [
  "Cookie Fundamentals: The Creaming Method (Signature Edition) - Cookies",
  "Drop Cookies: Chocolate Chip and Beyond (Signature Edition) - Cookies",
  "Cut-Out and Decorated Cookies (Signature Edition) - Cookies",
  "Bar Cookies and Brownies (Signature Edition) - Cookies",
  "Macarons and Meringue Cookies (Signature Edition) - Cookies"
 ],
 "Pies & Tarts": [
  "Pie Crust: Flaky Every Time (Signature Edition) - Pies & Tarts",
  "Fruit Pies and Thickeners (Signature Edition) - Pies & Tarts",
  "Custard Pies: Pumpkin, Pecan, and Chess (Signature Edition) - Pies & Tarts",
  "Tarts: Shells and Fillings (Signature Edition) - Pies & Tarts",
  "Blind Baking and Preventing Soggy Bottoms (Signature Edition) - Pies & Tarts"
 ],
 "Pastries": [
  "Laminated Doughs: Croissants and Puff Pastry (Signature Edition) - Pastries",
  "Danishes, Turnovers, and Hand Pies (Signature Edition) - Pastries",
  "Choux Pastry: Eclairs and Cream Puffs (Signature Edition) - Pastries",
  "Muffins, Scones, and Biscuits (Signature Edition) - Pastries"
 ],
 "Frosting & Decorating": [
  "Buttercream: American, Swiss, and Italian (Signature Edition) - Frosting & Decorating",
  "Ganache, Glazes, and Drips (Signature Edition) - Frosting & Decorating",
  "Cake Assembly and Crumb Coats (Signature Edition) - Frosting & Decorating",
  "Piping Basics and Simple Decorations (Signature Edition) - Frosting & Decorating"
 ],
 "Troubleshooting": [
  "Why Cakes Sink, Dome, or Crack (Signature Edition) - Troubleshooting",
  "Fixing Frosting Failures (Signature Edition) - Troubleshooting",
  "Bread Problems: Dense, Flat, or Pale (Signature Edition) - Troubleshooting",
  "Ingredient Substitutions That Work (Signature Edition) - Troubleshooting"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Baking Study — "+safe+"\n"
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
    name:topic+' — baking guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A baking guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"baking-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-baking-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('baking-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
