(function(){'use strict';
/* JAH Knowledge Level-Up generator — jahdb-db-knowledge-level-up-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KLUS-";
var FIELDS=["Basics","Quests","Mastery"];
var TOPICS={
 "Basics": [
  "Character Creation: Your Learner Stats (Signature Edition) - Basics",
  "XP: Experience Points Explained (Signature Edition) - Basics",
  "Levels: From Novice to Sage (Signature Edition) - Basics",
  "Quest Boards: Choosing Missions (Signature Edition) - Basics",
  "Streaks: The Chain (Signature Edition) - Basics",
  "Boss Fights: Hard Challenges (Signature Edition) - Basics",
  "Power-Ups: Learning Techniques (Signature Edition) - Basics",
  "Guilds: Learning Together (Signature Edition) - Basics",
  "Inventory: Your Knowledge Pack (Signature Edition) - Basics",
  "Save Points: Review Rituals (Signature Edition) - Basics",
  "Tutorial Complete: First Week (Signature Edition) - Basics",
  "The Map: Domains of Knowledge (Signature Edition) - Basics"
 ],
 "Quests": [
  "Science Quest: The Lab (Signature Edition) - Quests",
  "Math Quest: Number Dungeon (Signature Edition) - Quests",
  "History Quest: Time Travel (Signature Edition) - Quests",
  "Language Quest: New Tongue (Signature Edition) - Quests",
  "Art Quest: The Studio (Signature Edition) - Quests",
  "Music Quest: The Stage (Signature Edition) - Quests",
  "Code Quest: The Terminal (Signature Edition) - Quests",
  "Body Quest: The Arena (Signature Edition) - Quests",
  "Nature Quest: The Wild (Signature Edition) - Quests",
  "Money Quest: The Vault (Signature Edition) - Quests",
  "Social Quest: The Tavern (Signature Edition) - Quests",
  "Cooking Quest: The Kitchen (Signature Edition) - Quests"
 ],
 "Mastery": [
  "The Final Exam: Proving Mastery (Signature Edition) - Mastery",
  "Teaching: The Sage Ability (Signature Edition) - Mastery",
  "Cross-Training: Domain Fusion (Signature Edition) - Mastery",
  "The Mentor Quest (Signature Edition) - Mastery",
  "Speedrunning: Accelerated Learning (Signature Edition) - Mastery",
  "The Archive: Documenting Everything (Signature Edition) - Mastery",
  "Prestige Mode: Starting Over Better (Signature Edition) - Mastery",
  "The Hall of Fame (Signature Edition) - Mastery",
  "New Game Plus: The Lifelong Player (Signature Edition) - Mastery",
  "The Tournament: Competing (Signature Edition) - Mastery"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Knowledge Levelup Study — "+safe+"\n"
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
    name:topic+' — knowledge lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A knowledge lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"knowledge-levelup-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-knowledge-level-up-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-knowledge-level-up-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
