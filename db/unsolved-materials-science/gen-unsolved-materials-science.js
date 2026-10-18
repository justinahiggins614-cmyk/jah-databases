(function(){'use strict';
/* JAH The Unsolved Materials Science Database generator — jahdb-unsolved-materials-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USMT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Room-Temperature Superconductivity - Electronic",
  "Bulk Metallic Glass: The Perfect Metal - Structural",
  "High-Entropy Alloys: The Compositional Frontier - Structural",
  "Battery Materials: Beyond Lithium-Ion - Energy",
  "Thermoelectrics: Waste Heat to Power - Energy",
  "Photovoltaics: The Efficiency Limit - Energy",
  "Corrosion: The Trillion-Dollar Decay - Structural",
  "Self-Healing Materials - Functional",
  "Strong Glass: The Transparent Steel - Structural",
  "Shape-Memory Materials: The Programmable Metal - Functional",
  "Catalyst Design: The Rational Catalyst - Functional"
 ],
 "Compounded": [
  "The Materials Genome: Computing New Materials - Theory",
  "Grain Boundaries: The Weak Links - Structural",
  "Fatigue: The Unpredictable Failure - Structural",
  "Quasicrystals: The Impossible Materials - Structural",
  "Metamaterials: The Designed Impossible - Functional",
  "2D Materials: Beyond Graphene - Electronic",
  "Topological Materials: The Protected States - Electronic",
  "Ferroelectrics: The Memory Materials - Electronic",
  "Magnetic Materials: Beyond Rare Earths - Functional",
  "Solid Electrolytes: The Battery Bottleneck - Energy",
  "Hydrogen Storage Materials - Energy",
  "Green Cement: Decarbonizing Concrete - Structural"
 ],
 "Advanced": [
  "Materials for Additive Manufacturing - Processing",
  "Nuclear Materials: Surviving the Reactor - Structural",
  "Biomimetic Materials: Learning from Nature - Functional",
  "Materials Informatics: The Data-Driven Discovery - Theory",
  "Quantum Materials: The Correlated Frontier - Electronic",
  "Interface Science: The Boundary Problem - Theory",
  "Materials for Extremes - Structural",
  "Circular Materials: The Recycling Problem - Processing",
  "A Theory of Materials - Theory",
  "The Future of Materials: A Century Ahead - Theory",
  "Programmable Matter - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Materials Science Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-materials-science-solution-explorer",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-materials-science-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-materials-science',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
