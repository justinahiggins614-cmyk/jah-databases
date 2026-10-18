(function(){'use strict';
/* JAH The Chefs Database generator — jahdb-chefs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHEF-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Chefs Do",
  "Knife Skills: The Foundation",
  "Heat: The Chef's True Medium",
  "Seasoning: Salt, Acid, Fat, Heat",
  "Stocks: The Soul of the Kitchen",
  "The Mother Sauces",
  "Eggs: The Chef's Test",
  "Vegetables: Respect the Produce",
  "Kitchen Safety and Sanitation",
  "The Kitchen Brigade",
  "Mise en Place: Everything in Its Place"
 ],
 "Compounded": [
  "Proteins: Meat Cookery",
  "Fish and Seafood",
  "Pastry and Baking Fundamentals",
  "Menu Design and Engineering",
  "Food Cost Control",
  "Wine, Pairing, and Beverage",
  "Cuisines of the World: Foundations",
  "Plating and Presentation",
  "Banquets and Catering",
  "Butchery and Charcuterie",
  "Fermentation and Preservation",
  "Running the Pass"
 ],
 "Advanced": [
  "The Chef's Career Path",
  "Opening a Restaurant",
  "Michelin Stars and Competitions",
  "Food Writing and Media",
  "Sustainability in the Kitchen",
  "The Future Kitchen",
  "Tasting Menus and Fine Dining",
  "Street Food and Casual Concepts",
  "Culinary Education and Mentorship",
  "The Chef's Palate: Training Taste",
  "Famous Chefs in History"
 ]
};
var DEMOKIND="kitchen math";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Chef kitchen calculator — "+safe+"\n"
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
    name:topic+' — chefs profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A chefs profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-chefs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chefs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
