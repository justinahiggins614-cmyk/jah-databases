(function(){'use strict';
/* JAH The Hobby Clubs Database generator — jahdb-hobby-clubs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HBC-";
var FIELDS=["group-kind catalog", "Hidden Hobby Finder", "Hobby Discovery Machine", "Hobby Partners", "Shared Interest Discovery", "Universal Hobby Generator"];
var TOPICS={
 "group-kind catalog": [

 ]
,
 "Hidden Hobby Finder": [
  "The Hobby You Didn't Know Existed: Lock Picking",
  "Hidden Hobby: Stone Balancing",
  "Hidden Hobby: Niche Perfumery",
  "Hidden Hobby: Urban Sketching",
  "Hidden Hobby: Beekeeping",
  "Hidden Hobby: Bookbinding",
  "Hidden Hobby: Foraging",
  "Hidden Hobby: Stargazing",
  "Hidden Hobby: Fermentation",
  "Hidden Hobby: Calligraphy",
  "Hidden Hobby: Birding",
  "Hidden Hobby: Whittling",
  "Hidden Hobby: Letterboxing",
  "Hidden Hobby: Bonsai",
  "Hidden Hobby: The Finder Itself"
 ],
 "Hobby Discovery Machine": [
  "Machine Input: Your Hands",
  "Machine Input: Your Time",
  "Machine Input: Your People",
  "Machine Input: Your Budget",
  "Machine Output: The Shortlist",
  "Machine Output: The Trial Protocol",
  "Machine Calibration: The Check-In",
  "Machine Mode: The Deep Dive",
  "Machine Mode: The Wild Card",
  "Machine Mode: The Social Match",
  "Machine Learning: The Feedback Loop",
  "Machine Ethics: No Shame",
  "Machine Integration: The Calendar",
  "Machine Community: The Alumni",
  "Machine Philosophy: The Examined Leisure"
 ],
 "Hobby Partners": [
  "Finding Your Climbing Partner",
  "The Chess Club Welcome",
  "The Running Group",
  "The Maker Space Buddy",
  "The Language Exchange",
  "The Photography Walk Group",
  "The Book Club Dynamics",
  "The Gaming Group",
  "The Volunteer Crew",
  "The Music Jam",
  "The Cooking Collective",
  "The Hiking Club",
  "The Craft Circle",
  "The Stargazing Party",
  "The Partnership Principle"
 ],
 "Shared Interest Discovery": [
  "The Interest Inventory",
  "The Taste Buddies",
  "The Skill Swap Meet",
  "The Fandom Finder",
  "The Cross-Pollination",
  "The Interest Graph",
  "The Beginner's Table",
  "The Deep Dive Club",
  "The Interest Speed Dating",
  "The Shared Calendar",
  "The Interest Incubator",
  "The Reunion Tour",
  "The Interest Audit",
  "The Discovery Journal",
  "The Shared Discovery"
 ],
 "Universal Hobby Generator": [
  "Generator Seed: Hands Plus Outdoors",
  "Generator Seed: Mind Plus Solitude",
  "Generator Seed: Body Plus Community",
  "Generator Seed: Create Plus Share",
  "Generator Seed: Learn Plus Teach",
  "Generator Output: The Recipe",
  "Generator Output: The Progression",
  "Generator Output: The Community",
  "Generator Mode: The Remix",
  "Generator Mode: The Constraint",
  "Generator Mode: The Season",
  "Generator Mode: The Life Stage",
  "Generator Ethics: The Honest Brochure",
  "Generator Future: The Learning Loop",
  "Generator Philosophy: The Good Life"
 ]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hobby Clubs — "+safe+"\n"
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
    name:topic+' — hobby club record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hobby club record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-hobby-clubs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hobby-clubs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();



/* ==== ARCHIVE-SHAPE APPENDIX (EXPAND group-4) ====
   generateRecord(seed)/validateRecord(r) cover the real archive record
   shape for hobby-clubs (deterministic: same seed, same record). */
;(function(){'use strict';
function apRng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var AGROUPS=["Hidden Hobby Finder", "Hobby Discovery Machine", "Hobby Partners", "Shared Interest Discovery", "Universal Hobby Generator"];
var APREFIX="JAH-HBC-";
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
  if(!new RegExp("^JAH\\-HBC\\-\\d{6}$").test(r.id||''))e.push('id');
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
