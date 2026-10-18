(function(){'use strict';
/* JAH The Baking Database generator — jahdb-baking-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BAKE-";
var FIELDS=["Breads","Cakes","Cookies","Pies & Tarts","Pastries","Frosting & Decorating","Troubleshooting"];
var TOPICS={
 "Breads": [
  "Bread Baking Fundamentals - Breads",
  "Yeast: Types and Handling - Breads",
  "Kneading and Gluten Development - Breads",
  "Sourdough Starters and Baking - Breads",
  "Quick Breads: Banana, Zucchini, and Soda - Breads",
  "Rolls, Bagels, and Specialty Breads - Breads"
 ],
 "Cakes": [
  "Cake Baking Fundamentals - Cakes",
  "Butter Cakes: Vanilla, Chocolate, and Classics - Cakes",
  "Sponge and Foam Cakes - Cakes",
  "Cheesecakes: Baked and No-Bake - Cakes",
  "Cupcakes and Mini Cakes - Cakes",
  "Sheet Cakes and Crowd Baking - Cakes"
 ],
 "Cookies": [
  "Cookie Fundamentals: The Creaming Method - Cookies",
  "Drop Cookies: Chocolate Chip and Beyond - Cookies",
  "Cut-Out and Decorated Cookies - Cookies",
  "Bar Cookies and Brownies - Cookies",
  "Macarons and Meringue Cookies - Cookies"
 ],
 "Pies & Tarts": [
  "Pie Crust: Flaky Every Time - Pies & Tarts",
  "Fruit Pies and Thickeners - Pies & Tarts",
  "Custard Pies: Pumpkin, Pecan, and Chess - Pies & Tarts",
  "Tarts: Shells and Fillings - Pies & Tarts",
  "Blind Baking and Preventing Soggy Bottoms - Pies & Tarts"
 ],
 "Pastries": [
  "Laminated Doughs: Croissants and Puff Pastry - Pastries",
  "Danishes, Turnovers, and Hand Pies - Pastries",
  "Choux Pastry: Eclairs and Cream Puffs - Pastries",
  "Muffins, Scones, and Biscuits - Pastries"
 ],
 "Frosting & Decorating": [
  "Buttercream: American, Swiss, and Italian - Frosting & Decorating",
  "Ganache, Glazes, and Drips - Frosting & Decorating",
  "Cake Assembly and Crumb Coats - Frosting & Decorating",
  "Piping Basics and Simple Decorations - Frosting & Decorating"
 ],
 "Troubleshooting": [
  "Why Cakes Sink, Dome, or Crack - Troubleshooting",
  "Fixing Frosting Failures - Troubleshooting",
  "Bread Problems: Dense, Flat, or Pale - Troubleshooting",
  "Ingredient Substitutions That Work - Troubleshooting"
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
var gen={version:'jahdb-baking-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('baking',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
