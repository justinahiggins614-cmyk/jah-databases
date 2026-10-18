(function(){'use strict';
/* JAH The Coding Quest Signature Database generator — jahdb-db-coding-quest-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CQS-";
var FIELDS=["First Programs","Logic & Data","Projects"];
var TOPICS={
 "First Programs": [
  "Quest 1: Hello, World (Signature Edition) - First Programs",
  "Variables: Named Boxes (Signature Edition) - First Programs",
  "Numbers and Math (Signature Edition) - First Programs",
  "Strings: Text Tools (Signature Edition) - First Programs",
  "Input: Talking to Users (Signature Edition) - First Programs",
  "If Statements: Decisions (Signature Edition) - First Programs",
  "While Loops: Repeat Until (Signature Edition) - First Programs",
  "For Loops: Repeat For Each (Signature Edition) - First Programs",
  "Debugging: Reading Errors (Signature Edition) - First Programs",
  "Comments: Notes to Humans (Signature Edition) - First Programs",
  "Lists: Ordered Collections (Signature Edition) - First Programs",
  "Dictionaries: Labeled Lookup (Signature Edition) - First Programs"
 ],
 "Logic & Data": [
  "Functions: Named Recipes (Signature Edition) - Logic & Data",
  "Scope: Where Variables Live (Signature Edition) - Logic & Data",
  "Booleans and Logic (Signature Edition) - Logic & Data",
  "String Methods Toolbox (Signature Edition) - Logic & Data",
  "List Comprehensions (Signature Edition) - Logic & Data",
  "File I/O: Reading and Writing (Signature Edition) - Logic & Data",
  "Errors and Exceptions (Signature Edition) - Logic & Data",
  "Modules and Imports (Signature Edition) - Logic & Data",
  "Recursion: Functions Calling Themselves (Signature Edition) - Logic & Data",
  "Sorting and Searching (Signature Edition) - Logic & Data",
  "Big-O: How Code Scales (Signature Edition) - Logic & Data",
  "Sets: Unique Collections (Signature Edition) - Logic & Data"
 ],
 "Projects": [
  "Project: Number Guessing Game (Signature Edition) - Projects",
  "Project: To-Do List App (Signature Edition) - Projects",
  "Project: Password Generator (Signature Edition) - Projects",
  "Project: Quiz Game (Signature Edition) - Projects",
  "Project: File Organizer (Signature Edition) - Projects",
  "Project: Web Scraper Basics (Signature Edition) - Projects",
  "Project: Simple API (Signature Edition) - Projects",
  "Project: Data Dashboard (Signature Edition) - Projects",
  "Project: Chatbot (Rule-Based) (Signature Edition) - Projects",
  "Capstone: Ship Your First Project (Signature Edition) - Projects"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Coding Quest Study — "+safe+"\n"
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
    name:topic+' — coding lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A coding lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"coding-quest-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-coding-quest-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-coding-quest-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
