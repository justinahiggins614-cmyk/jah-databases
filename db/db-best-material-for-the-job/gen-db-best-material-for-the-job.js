(function(){'use strict';
/* JAH The Best Material for the Job Database generator — jahdb-db-best-material-for-the-job-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BMFTJ-";
var FIELDS=["Structural Materials","Everyday Materials","Advanced Materials"];
var TOPICS={
 "Structural Materials": [
  "Steel vs Aluminum: Metal Workhorses - Structural Materials",
  "Wood vs Steel: Framing - Structural Materials",
  "Concrete vs Steel: Skyscrapers - Structural Materials",
  "Titanium vs Carbon Fiber: Premium Light - Structural Materials",
  "Brick vs Wood: Walls - Structural Materials",
  "Glass vs Polycarbonate: Transparent - Structural Materials",
  "Copper vs Aluminum: Wiring - Structural Materials",
  "Cast Iron vs Steel: Cookware Metal - Structural Materials",
  "Stone vs Concrete: Ancient vs Modern - Structural Materials",
  "Bamboo vs Timber: Fast Growth - Structural Materials",
  "Rope: Natural vs Synthetic - Structural Materials",
  "Leather vs Synthetic: Upholstery - Structural Materials"
 ],
 "Everyday Materials": [
  "Cotton vs Polyester: Fabric - Everyday Materials",
  "Wool vs Fleece: Warmth - Everyday Materials",
  "Paper vs Plastic: Bags - Everyday Materials",
  "Ceramic vs Plastic: Dishes - Everyday Materials",
  "Down vs Synthetic: Insulation - Everyday Materials",
  "Rubber vs Silicone: Flexible - Everyday Materials",
  "Cardboard vs Plastic: Packaging - Everyday Materials",
  "Beeswax vs Paraffin: Candles - Everyday Materials",
  "Soap: Bar vs Liquid - Everyday Materials",
  "Ink: Ballpoint vs Fountain - Everyday Materials"
 ],
 "Advanced Materials": [
  "Graphene vs Diamond: Carbon Future - Advanced Materials",
  "Aerogel vs Foam: Insulation Future - Advanced Materials",
  "Shape-Memory Alloy vs Spring Steel: Smart Metal - Advanced Materials",
  "Bioplastic vs Petroleum Plastic: Future Plastic - Advanced Materials",
  "Transparent Aluminum vs Glass: Sci-Fi Material - Advanced Materials",
  "Self-Healing Concrete vs Regular: Future Build - Advanced Materials",
  "Metallic Glass vs Steel: Amorphous Metal - Advanced Materials",
  "Superalloy vs Titanium: Hot Metals - Advanced Materials",
  "Quantum Dot vs Phosphor: Display Future - Advanced Materials",
  "Perovskite vs Silicon: Solar Future - Advanced Materials",
  "Spider Silk (Lab) vs Nylon: Fiber Future - Advanced Materials",
  "Wood (Engineered) vs Concrete: Tall Timber - Advanced Materials"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Best Material Study — "+safe+"\n"
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
    name:topic+' — material selection record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A material selection record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"best-material-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-best-material-for-the-job-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-best-material-for-the-job',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
