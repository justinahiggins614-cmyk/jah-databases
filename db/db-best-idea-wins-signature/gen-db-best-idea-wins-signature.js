(function(){'use strict';
/* JAH The Best Idea Wins Signature Database generator — jahdb-db-best-idea-wins-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIWS-";
var FIELDS=["Work Ideas","Life Ideas","Society Ideas"];
var TOPICS={
 "Work Ideas": [
  "Remote vs Office: Work (Signature Edition) - Work Ideas",
  "4-Day Week vs 5-Day: Time (Signature Edition) - Work Ideas",
  "Salary vs Equity: Pay (Signature Edition) - Work Ideas",
  "Generalist vs Specialist: Career (Signature Edition) - Work Ideas",
  "Startup vs Corporate: Path (Signature Edition) - Work Ideas",
  "Freelance vs Employed: Work Style (Signature Edition) - Work Ideas",
  "Deep Work vs Meetings: Time (Signature Edition) - Work Ideas",
  "AI Assistant vs Human: Help (Signature Edition) - Work Ideas"
 ],
 "Life Ideas": [
  "Books vs Movies: Stories (Signature Edition) - Life Ideas",
  "Optimism vs Realism: Outlook (Signature Edition) - Life Ideas",
  "Minimalism vs Abundance: Living (Signature Edition) - Life Ideas",
  "City vs Country: Home (Signature Edition) - Life Ideas",
  "Early Bird vs Night Owl: Rhythm (Signature Edition) - Life Ideas",
  "Cook vs Eat Out: Food (Signature Edition) - Life Ideas",
  "Gym vs Outdoors: Fitness (Signature Edition) - Life Ideas",
  "Digital vs Analog: Notes (Signature Edition) - Life Ideas",
  "Travel vs Home: Experience (Signature Edition) - Life Ideas",
  "Big Wedding vs Small: Celebrate (Signature Edition) - Life Ideas",
  "Own vs Rent: Stuff (Signature Edition) - Life Ideas",
  "News vs No News: Informed (Signature Edition) - Life Ideas",
  "Plan vs Spontaneity: Days (Signature Edition) - Life Ideas"
 ],
 "Society Ideas": [
  "Democracy vs Efficiency: Rule (Signature Edition) - Society Ideas",
  "Privacy vs Convenience: Data (Signature Edition) - Society Ideas",
  "Cars vs Transit: Cities (Signature Edition) - Society Ideas",
  "Nuclear vs Renewables: Power (Signature Edition) - Society Ideas",
  "UBI vs Jobs Guarantee: Welfare (Signature Edition) - Society Ideas",
  "Free College vs Trade School: Education (Signature Edition) - Society Ideas",
  "Open Borders vs Controlled: Migration (Signature Edition) - Society Ideas",
  "Cashless vs Cash: Money (Signature Edition) - Society Ideas",
  "Suburbs vs Density: Housing (Signature Edition) - Society Ideas",
  "Local vs Global: Food (Signature Edition) - Society Ideas",
  "Small School vs Big: Education (Signature Edition) - Society Ideas",
  "Public vs Private: Healthcare (Signature Edition) - Society Ideas",
  "Ban vs Tax: Behavior (Signature Edition) - Society Ideas"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Best Idea Study — "+safe+"\n"
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
    name:topic+' — idea showdown record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A idea showdown record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"best-idea-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-best-idea-wins-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-best-idea-wins-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
