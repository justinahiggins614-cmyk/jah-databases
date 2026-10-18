(function(){'use strict';
/* JAH The Hobby Clubs Signature Database generator — jahdb-hobby-clubs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HBCG-";
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
  return "# Hobby Clubs Signature — "+safe+"\n"
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
var gen={version:'jahdb-hobby-clubs-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hobby-clubs-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
