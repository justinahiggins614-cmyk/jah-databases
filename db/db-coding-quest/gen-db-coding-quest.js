(function(){'use strict';
/* JAH The Coding Quest Database generator — jahdb-db-coding-quest-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CQ-";
var FIELDS=["First Programs","Logic & Data","Projects"];
var TOPICS={
 "First Programs": [
  "Quest 1: Hello, World - First Programs",
  "Variables: Named Boxes - First Programs",
  "Numbers and Math - First Programs",
  "Strings: Text Tools - First Programs",
  "Input: Talking to Users - First Programs",
  "If Statements: Decisions - First Programs",
  "While Loops: Repeat Until - First Programs",
  "For Loops: Repeat For Each - First Programs",
  "Debugging: Reading Errors - First Programs",
  "Comments: Notes to Humans - First Programs",
  "Lists: Ordered Collections - First Programs",
  "Dictionaries: Labeled Lookup - First Programs"
 ],
 "Logic & Data": [
  "Functions: Named Recipes - Logic & Data",
  "Scope: Where Variables Live - Logic & Data",
  "Booleans and Logic - Logic & Data",
  "String Methods Toolbox - Logic & Data",
  "List Comprehensions - Logic & Data",
  "File I/O: Reading and Writing - Logic & Data",
  "Errors and Exceptions - Logic & Data",
  "Modules and Imports - Logic & Data",
  "Recursion: Functions Calling Themselves - Logic & Data",
  "Sorting and Searching - Logic & Data",
  "Big-O: How Code Scales - Logic & Data",
  "Sets: Unique Collections - Logic & Data"
 ],
 "Projects": [
  "Project: Number Guessing Game - Projects",
  "Project: To-Do List App - Projects",
  "Project: Password Generator - Projects",
  "Project: Quiz Game - Projects",
  "Project: File Organizer - Projects",
  "Project: Web Scraper Basics - Projects",
  "Project: Simple API - Projects",
  "Project: Data Dashboard - Projects",
  "Project: Chatbot (Rule-Based) - Projects",
  "Capstone: Ship Your First Project - Projects"
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
var gen={version:'jahdb-db-coding-quest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-coding-quest',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
