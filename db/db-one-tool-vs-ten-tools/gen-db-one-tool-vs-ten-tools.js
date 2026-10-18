(function(){'use strict';
/* JAH The One Tool vs. Ten Tools Database generator — jahdb-db-one-tool-vs-ten-tools-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OTVTT-";
var FIELDS=["Everyday Versatility","Workshop Versatility","Digital Versatility"];
var TOPICS={
 "Everyday Versatility": [
  "Swiss Army Knife vs Toolbox: Carry - Everyday Versatility",
  "Smartphone vs Gadgets: Convergence - Everyday Versatility",
  "Duct Tape vs Tape Collection: Fix - Everyday Versatility",
  "WD-40 vs Lubricant Shelf: Squeak - Everyday Versatility",
  "Chef's Knife vs Knife Set: Kitchen - Everyday Versatility",
  "Cast Iron vs Pan Collection: Cook - Everyday Versatility",
  "Multitool vs Kitchen Gadgets: Drawers - Everyday Versatility",
  "Leatherman vs Tool Roll: EDC - Everyday Versatility",
  "Paracord vs Rope Collection: Cord - Everyday Versatility",
  "Bandana vs Kit: Cloth - Everyday Versatility",
  "Credit Card vs Wallet Full: Pay - Everyday Versatility",
  "Cooler vs Mini-Fridge: Portable Cold - Everyday Versatility"
 ],
 "Workshop Versatility": [
  "Oscillating Tool vs Specialists: Workshop - Workshop Versatility",
  "Drill/Driver vs Dedicated: Holes - Workshop Versatility",
  "Angle Grinder vs Specialists: Cut - Workshop Versatility",
  "Shop Vac vs Specialists: Clean - Workshop Versatility",
  "Workbench vs Special Benches: Bench - Workshop Versatility",
  "Clamp Collection vs One: Hold - Workshop Versatility",
  "Saw: Circular vs Table+Miter - Workshop Versatility",
  "Sander: Random Orbit vs Set - Workshop Versatility",
  "Router vs Shaper: Profiles - Workshop Versatility",
  "Welder: MIG vs Full Shop - Workshop Versatility"
 ],
 "Digital Versatility": [
  "Laptop vs Desktop+Tablet: Compute - Digital Versatility",
  "Phone vs Camera+GPS+Music: Pocket - Digital Versatility",
  "All-in-One vs Components: Audio - Digital Versatility",
  "E-reader vs Tablet: Read - Digital Versatility",
  "Smart Speaker vs Stereo: Listen - Digital Versatility",
  "Console vs PC: Play - Digital Versatility",
  "Notebook App vs Paper System: Notes - Digital Versatility",
  "Multitool App vs Suite: Software - Digital Versatility",
  "Swiss Card vs Knife: Flat - Digital Versatility",
  "One Pan vs Kitchen: Cook - Digital Versatility",
  "Master Key vs Ring: Access - Digital Versatility",
  "Universal Remote vs Many: Control - Digital Versatility"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# One Vs Ten Study — "+safe+"\n"
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
    name:topic+' — tool versatility record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tool versatility record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"one-vs-ten-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-one-tool-vs-ten-tools-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-one-tool-vs-ten-tools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
