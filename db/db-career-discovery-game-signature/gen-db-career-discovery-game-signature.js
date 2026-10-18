(function(){'use strict';
/* JAH The Career Discovery Game generator — jahdb-db-career-discovery-game-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CDGS-";
var FIELDS=["Interests","Exploration","Planning"];
var TOPICS={
 "Interests": [
  "Game Start: What Is Work For? (Signature Edition) - Interests",
  "Interest Inventory (Signature Edition) - Interests",
  "Skills Audit (Signature Edition) - Interests",
  "Values Check (Signature Edition) - Interests",
  "Strengths Finder (Signature Edition) - Interests",
  "Curiosity Trails (Signature Edition) - Interests",
  "The Ikigai Map (Signature Edition) - Interests",
  "Childhood Clues (Signature Edition) - Interests",
  "Energy Audit (Signature Edition) - Interests",
  "Role Models (Signature Edition) - Interests",
  "Anti-Goals (Signature Edition) - Interests",
  "The Player Profile (Signature Edition) - Interests"
 ],
 "Exploration": [
  "Career Safari: Shadowing (Signature Edition) - Exploration",
  "Informational Interviews (Signature Edition) - Exploration",
  "Try Before You Buy: Projects (Signature Edition) - Exploration",
  "Internships and Apprenticeships (Signature Edition) - Exploration",
  "The 100-Careers List (Signature Edition) - Exploration",
  "Industry Deep Dives (Signature Edition) - Exploration",
  "Salary Reality Check (Signature Edition) - Exploration",
  "Work-Life Patterns (Signature Edition) - Exploration",
  "Education Paths Compared (Signature Edition) - Exploration",
  "The Future-Proof Test (Signature Edition) - Exploration",
  "Side Doors: Unconventional Entry (Signature Edition) - Exploration",
  "Your Shortlist (Signature Edition) - Exploration"
 ],
 "Planning": [
  "Skill Gap Analysis (Signature Edition) - Planning",
  "The 90-Day Learning Sprint (Signature Edition) - Planning",
  "Building Proof: Portfolio (Signature Edition) - Planning",
  "Resume That Works (Signature Edition) - Planning",
  "Networking Without Awkwardness (Signature Edition) - Planning",
  "Interview Preparation (Signature Edition) - Planning",
  "Negotiating Offers (Signature Edition) - Planning",
  "The First 90 Days (Signature Edition) - Planning",
  "Career Lattices, Not Ladders (Signature Edition) - Planning",
  "Your Career Game Plan (Signature Edition) - Planning"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Career Discovery Study — "+safe+"\n"
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
    name:topic+' — career lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A career lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"career-discovery-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-career-discovery-game-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-career-discovery-game-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
