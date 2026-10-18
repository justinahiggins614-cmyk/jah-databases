(function(){'use strict';
/* JAH The Most Influential Ideas Database generator — jahdb-db-most-influential-ideas-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MII-";
var FIELDS=["Political Ideas","Scientific Ideas","Human Ideas"];
var TOPICS={
 "Political Ideas": [
  "Democracy vs Republic: Self-Rule - Political Ideas",
  "Markets vs Planning: Economies - Political Ideas",
  "Rights vs Duties: Citizenship - Political Ideas",
  "Federalism vs Unitary: Power Split - Political Ideas",
  "Rule of Law vs Rule of Man: Justice - Political Ideas",
  "Separation of Powers vs Unity: Government - Political Ideas",
  "Welfare State vs Night Watchman: Government Size - Political Ideas",
  "Nationalism vs Cosmopolitanism: Belonging - Political Ideas",
  "Revolution vs Reform: Change - Political Ideas",
  "Pacifism vs Just War: Conflict - Political Ideas",
  "Free Speech vs Safety: Expression - Political Ideas"
 ],
 "Scientific Ideas": [
  "Evolution vs Creation Narratives: Origins - Scientific Ideas",
  "Relativity vs Quantum: Physics Pillars - Scientific Ideas",
  "Germ Theory vs Miasma: Medicine - Scientific Ideas",
  "Heliocentrism vs Geocentrism: Cosmos - Scientific Ideas",
  "Plate Tectonics vs Fixed Earth: Geology - Scientific Ideas",
  "Big Bang vs Steady State: Universe - Scientific Ideas",
  "Natural Selection vs Lamarck: Evolution Mechanisms - Scientific Ideas",
  "Atomic Theory vs Continuum: Matter - Scientific Ideas",
  "Vaccination vs Hygiene: Public Health - Scientific Ideas",
  "Double Helix vs Central Dogma: Genetics - Scientific Ideas"
 ],
 "Human Ideas": [
  "Golden Rule vs Social Contract: Ethics - Human Ideas",
  "Skepticism vs Faith: Knowing - Human Ideas",
  "Individualism vs Collectivism: Self - Human Ideas",
  "Progress vs Tradition: Time - Human Ideas",
  "Utopia vs Dystopia: Futures - Human Ideas",
  "Meritocracy vs Equality: Fairness - Human Ideas",
  "Stoicism vs Epicureanism: Life - Human Ideas",
  "Narrative vs Data: Truth - Human Ideas",
  "Competition vs Cooperation: Success - Human Ideas",
  "Simplicity vs Complexity: Design - Human Ideas",
  "Hope vs Realism: Outlook - Human Ideas",
  "Love vs Justice: Values - Human Ideas",
  "Forgiveness vs Revenge: Healing - Human Ideas"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Influential Ideas Study — "+safe+"\n"
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
    name:topic+' — idea influence record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A idea influence record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"influential-ideas-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-most-influential-ideas-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-most-influential-ideas',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
