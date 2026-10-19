(function(){'use strict';
/* JAH The Mineralogy Database generator — jahdb-mineralogy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MIN-";
var FIELDS=["Foundations","Compounded","Advanced", "Crystal Kingdom"];
var TOPICS={
 "Foundations": [
  "What Is Mineralogy: The Science of Earth's Crystalline Materials \u2014 Foundations",
  "The Five Tests: What Counts as a Mineral \u2014 Foundations",
  "Crystal Systems: The Seven Symmetry Systems of Mineralogy \u2014 Foundations",
  "Mineral Habit: The Shapes Crystals Take \u2014 Foundations",
  "The Mohs Hardness Scale: Scratch Testing \u2014 Foundations",
  "Cleavage, Fracture, and Parting: How Minerals Break \u2014 Foundations",
  "Luster and Streak: How Minerals Handle Light \u2014 Foundations",
  "Color in Minerals: Causes and Traps \u2014 Foundations",
  "Specific Gravity: Weighing Minerals in Water \u2014 Foundations",
  "The Dana Classification: Eight Chemical Classes \u2014 Foundations",
  "The Nickel-Strunz Classification: Structure-First Classes \u2014 Foundations",
  "Reading Mineral Formulas: From Symbols to Composition \u2014 Foundations"
 ],
 "Compounded": [
  "Symmetry Elements and the 32 Point Groups \u2014 Compounded",
  "Crystal Lattices: The 14 Bravais Lattices \u2014 Compounded",
  "Silicate Structures: The Six Tetrahedral Families \u2014 Compounded",
  "Rock-Forming Minerals: The Minerals That Build Continents \u2014 Compounded",
  "Ore Minerals: Where Metals Come From \u2014 Compounded",
  "Igneous Crystallization: Bowen's Reaction Series \u2014 Compounded",
  "Sedimentary and Metamorphic Mineral Formation \u2014 Compounded",
  "Hydrothermal Veins and Pegmatites \u2014 Compounded",
  "Optical Mineralogy: The Polarizing Microscope \u2014 Compounded",
  "Refractive Index and Birefringence \u2014 Compounded",
  "Pleochroism and Interference Colors \u2014 Compounded",
  "Gemstones: Properties, Cutting, and Value \u2014 Compounded",
  "Hand-Sample Identification: The Field Workflow \u2014 Compounded"
 ],
 "Advanced": [
  "X-Ray Diffraction: Bragg's Law and the Unit Cell \u2014 Advanced",
  "Crystal Structure Determination \u2014 Advanced",
  "Solid Solution and Polymorphism \u2014 Advanced",
  "Thermodynamics of Mineral Stability \u2014 Advanced",
  "Phase Diagrams: Reading Mineral Stability Fields \u2014 Advanced",
  "Ionic Substitution: Goldschmidt's Rules \u2014 Advanced",
  "Gemstone Treatments and Synthetics Detection \u2014 Advanced",
  "The IMA and the Master List of Minerals \u2014 Advanced",
  "Describing a New Mineral: From Discovery to Approval \u2014 Advanced",
  "Environmental Mineralogy: Acid Drainage and Remediation \u2014 Advanced",
  "Building a Systematic Mineral Collection \u2014 Advanced"
 ]
,
 "Crystal Kingdom": [
  "Quartz: The King of Crystals",
  "Diamonds: The Compressed Legend",
  "Fluorite: The Rainbow Cube",
  "Pyrite: Fool's Gold",
  "Amethyst: The Purple Palace",
  "Calcite: The Double Vision",
  "Malachite: The Green Swirls",
  "Opal: The Fire Within",
  "Garnet: The Deep Red",
  "Topaz: The Golden Standard",
  "Tourmaline: The Electric Rainbow",
  "Beryl: The Emerald Family",
  "Selenite: The Moonlight Blades",
  "Labradorite: The Northern Lights Stone",
  "The Collector's Ethic"
 ]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mineralogy Study — "+safe+"\n"
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
    name:topic+' — mineralogy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mineralogy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mineralogy-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-mineralogy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mineralogy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();




/* ==== ARCHIVE-SHAPE APPENDIX (EXPAND group-4) ====
   generateRecord(seed)/validateRecord(r) cover the real archive record
   shape for mineralogy (deterministic: same seed, same record). */
;(function(){'use strict';
function apRng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var AGROUPS=["Crystal Kingdom"];
var APREFIX="JAH-MIN-";
var APAD=6;
function generateRecord(seed){
  var rnd=apRng(seed);
  var group=AGROUPS[(rnd()*AGROUPS.length)|0];
  var id=APREFIX+String(seed).padStart(APAD,'0');
  var title="Archive Study "+seed+" — "+group;
  var r={
    id:id,
    t:title,
    g:group,
    name:title,
    title:title,
    description:"Archive record: "+title+" — full study in "+group+". ",
    how_it_works:"In practice, "+title+" works as follows. Full study content. ",
    key_points:["Point one for "+title,"Point two for "+title],
    requirements:["Standard requirements."],
    standards:["Standard references"],
    citations:["Standard references (public sources)."],
    src:"signature",
    ladder_rank:2,
    ladder_tier:"foundations",
    demo:{kind:"python",language:"python",program:"# archive demo — "+title+"\nprint(\""+title+"\")\nprint(\"record "+id+" verified\")\n"},
  };
  return r;
}
function validateRecord(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-MIN\\-\\d{6}$").test(r.id||''))e.push('id');
    if(!(typeof r["id"]==='string'&&r["id"].length>0))e.push("id");
    if(!(typeof r["t"]==='string'&&r["t"].length>0))e.push("t");
    if(!(typeof r["g"]==='string'&&r["g"].length>0))e.push("g");
    if(!(typeof r["name"]==='string'&&r["name"].length>0))e.push("name");
    if(!(typeof r["title"]==='string'&&r["title"].length>0))e.push("title");
    if(!(typeof r["description"]==='string'&&r["description"].length>0))e.push("description");
    if(!(typeof r["how_it_works"]==='string'&&r["how_it_works"].length>0))e.push("how_it_works");
    if(!(Array.isArray(r["key_points"])))e.push("key_points");
    if(!(Array.isArray(r["requirements"])))e.push("requirements");
    if(!(Array.isArray(r["standards"])))e.push("standards");
    if(!(Array.isArray(r["citations"])))e.push("citations");
    if(!(typeof r["src"]==='string'&&r["src"].length>0))e.push("src");
    if(!(typeof r["ladder_rank"]==='number'))e.push("ladder_rank");
    if(!(typeof r["ladder_tier"]==='string'&&r["ladder_tier"].length>0))e.push("ladder_tier");
    if(!(r["demo"]&&typeof r["demo"]==='object'&&!Array.isArray(r["demo"])))e.push("demo");
  return {ok:!e.length,errors:e};
}
if(typeof module!=='undefined'&&module.exports){module.exports.archive={generate:generateRecord,validate:validateRecord,groups:AGROUPS};}
})();
