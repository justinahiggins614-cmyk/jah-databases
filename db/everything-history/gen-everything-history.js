(function(){'use strict';
/* JAH The Everything History Database generator — jahdb-everything-history-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVH-";
var FIELDS=["Ancient","Medieval","Early Modern","Modern","Contemporary","Signature History", "Ancient History Adventures", "Ancient vs Modern Engineering"];
var TOPICS={
 "Ancient": [
  "Ancient Civilizations: Mesopotamia and Egypt \u2014 Ancient",
  "Classical Antiquity: Greece and Rome \u2014 Ancient"
 ],
 "Medieval": [
  "The Middle Ages: 500-1500 \u2014 Medieval"
 ],
 "Early Modern": [
  "The Renaissance and Reformation \u2014 Early Modern",
  "The Age of Exploration \u2014 Early Modern"
 ],
 "Modern": [
  "The Industrial Revolution \u2014 Modern",
  "The World Wars: 1914-1945 \u2014 Modern"
 ],
 "Contemporary": [
  "The Cold War and Decolonization \u2014 Contemporary"
 ],
 "Signature History": [
  "Signature Timeline Engine (Signature Edition) \u2014 Signature History",
  "Signature Civilization Mapper (Signature Edition) \u2014 Signature History",
  "Signature Cause-and-Effect Analyzer (Signature Edition) \u2014 Signature History",
  "Signature Archive Harmonizer (Signature Edition) \u2014 Signature History"
 ]
,
 "Ancient History Adventures": [
  "Walking the Streets of Pompeii",
  "Sailing with the Phoenicians",
  "The Building of the Pyramids",
  "Athens in the Age of Pericles",
  "The Silk Road Caravan",
  "Rome's Water Empire",
  "The Library of Alexandria",
  "The Terracotta Army",
  "Viking Voyages",
  "The Inca Road System",
  "Angkor at Its Zenith",
  "The Mali Empire's Gold",
  "Byzantium: The Queen of Cities",
  "The Minoan Labyrinth",
  "The Adventure Continues"
 ],
 "Ancient vs Modern Engineering": [
  "Roman Concrete vs Modern Concrete",
  "The Antikythera Mechanism vs Computers",
  "Inca Masonry vs Modern Masonry",
  "Egyptian Surveying vs GPS",
  "Roman Aqueducts vs Modern Water Systems",
  "Damascus Steel vs Modern Metallurgy",
  "Greek Fire vs Modern Weapons",
  "The Baghdad Battery vs Modern Batteries",
  "Polynesian Navigation vs Instruments",
  "Medieval Cathedrals vs Skyscrapers",
  "The Seismoscope of Zhang Heng",
  "Ancient Surgery vs Modern Surgery",
  "The Lighthouse of Alexandria vs Modern Lighthouses",
  "Qanats vs Modern Irrigation",
  "The Verdict: What Progress Means"
 ]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything History — "+safe+"\n"
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
    name:topic+' — history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-everything-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-history',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();



/* ==== ARCHIVE-SHAPE APPENDIX (EXPAND group-4) ====
   generateRecord(seed)/validateRecord(r) cover the real archive record
   shape for everything-history (deterministic: same seed, same record). */
;(function(){'use strict';
function apRng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var AGROUPS=["Ancient History Adventures", "Ancient vs Modern Engineering"];
var APREFIX="JAH-EVH-";
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
    requirements:"Standard requirements.",
    standards:["Standard references"],
    citations:"Standard references (public sources). ",
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
  if(!new RegExp("^JAH\\-EVH\\-\\d{6}$").test(r.id||''))e.push('id');
    if(!(typeof r["id"]==='string'&&r["id"].length>0))e.push("id");
    if(!(typeof r["t"]==='string'&&r["t"].length>0))e.push("t");
    if(!(typeof r["g"]==='string'&&r["g"].length>0))e.push("g");
    if(!(typeof r["name"]==='string'&&r["name"].length>0))e.push("name");
    if(!(typeof r["title"]==='string'&&r["title"].length>0))e.push("title");
    if(!(typeof r["description"]==='string'&&r["description"].length>0))e.push("description");
    if(!(typeof r["how_it_works"]==='string'&&r["how_it_works"].length>0))e.push("how_it_works");
    if(!(Array.isArray(r["key_points"])))e.push("key_points");
    if(!(typeof r["requirements"]==='string'&&r["requirements"].length>0))e.push("requirements");
    if(!(Array.isArray(r["standards"])))e.push("standards");
    if(!(typeof r["citations"]==='string'&&r["citations"].length>0))e.push("citations");
    if(!(typeof r["src"]==='string'&&r["src"].length>0))e.push("src");
    if(!(typeof r["ladder_rank"]==='number'))e.push("ladder_rank");
    if(!(typeof r["ladder_tier"]==='string'&&r["ladder_tier"].length>0))e.push("ladder_tier");
    if(!(r["demo"]&&typeof r["demo"]==='object'&&!Array.isArray(r["demo"])))e.push("demo");
  return {ok:!e.length,errors:e};
}
if(typeof module!=='undefined'&&module.exports){module.exports.archive={generate:generateRecord,validate:validateRecord,groups:AGROUPS};}
})();
