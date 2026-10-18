(function(){'use strict';
/* JAH The Unsolved Materials Science Signature Database generator — jahdb-unsolved-materials-science-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USMTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Room-Temperature Superconductivity (Signature Edition) - Electronic",
  "Bulk Metallic Glass: The Perfect Metal (Signature Edition) - Structural",
  "High-Entropy Alloys: The Compositional Frontier (Signature Edition) - Structural",
  "Battery Materials: Beyond Lithium-Ion (Signature Edition) - Energy",
  "Thermoelectrics: Waste Heat to Power (Signature Edition) - Energy",
  "Photovoltaics: The Efficiency Limit (Signature Edition) - Energy",
  "Corrosion: The Trillion-Dollar Decay (Signature Edition) - Structural",
  "Self-Healing Materials (Signature Edition) - Functional",
  "Strong Glass: The Transparent Steel (Signature Edition) - Structural",
  "Shape-Memory Materials: The Programmable Metal (Signature Edition) - Functional",
  "Catalyst Design: The Rational Catalyst (Signature Edition) - Functional"
 ],
 "Compounded": [
  "The Materials Genome: Computing New Materials (Signature Edition) - Theory",
  "Grain Boundaries: The Weak Links (Signature Edition) - Structural",
  "Fatigue: The Unpredictable Failure (Signature Edition) - Structural",
  "Quasicrystals: The Impossible Materials (Signature Edition) - Structural",
  "Metamaterials: The Designed Impossible (Signature Edition) - Functional",
  "2D Materials: Beyond Graphene (Signature Edition) - Electronic",
  "Topological Materials: The Protected States (Signature Edition) - Electronic",
  "Ferroelectrics: The Memory Materials (Signature Edition) - Electronic",
  "Magnetic Materials: Beyond Rare Earths (Signature Edition) - Functional",
  "Solid Electrolytes: The Battery Bottleneck (Signature Edition) - Energy",
  "Hydrogen Storage Materials (Signature Edition) - Energy",
  "Green Cement: Decarbonizing Concrete (Signature Edition) - Structural"
 ],
 "Advanced": [
  "Materials for Additive Manufacturing (Signature Edition) - Processing",
  "Nuclear Materials: Surviving the Reactor (Signature Edition) - Structural",
  "Biomimetic Materials: Learning from Nature (Signature Edition) - Functional",
  "Materials Informatics: The Data-Driven Discovery (Signature Edition) - Theory",
  "Quantum Materials: The Correlated Frontier (Signature Edition) - Electronic",
  "Interface Science: The Boundary Problem (Signature Edition) - Theory",
  "Materials for Extremes (Signature Edition) - Structural",
  "Circular Materials: The Recycling Problem (Signature Edition) - Processing",
  "A Theory of Materials (Signature Edition) - Theory",
  "The Future of Materials: A Century Ahead (Signature Edition) - Theory",
  "Programmable Matter (Signature Edition) - Theory"
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
var gen={version:'jahdb-unsolved-materials-science-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-materials-science-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
