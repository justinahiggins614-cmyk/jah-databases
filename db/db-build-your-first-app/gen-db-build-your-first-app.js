(function(){'use strict';
/* JAH The Build Your First App Database generator — jahdb-db-build-your-first-app-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BYFA-";
var FIELDS=["App Ideas","Building Blocks","Launch"];
var TOPICS={
 "App Ideas": [
  "What Counts as an App - App Ideas",
  "Find a Problem Worth Solving - App Ideas",
  "The One-Sentence Pitch - App Ideas",
  "Sketch Before You Code - App Ideas",
  "User Stories: Features as Promises - App Ideas",
  "MVP: The Smallest Real Thing - App Ideas",
  "Pick Your Platform - App Ideas",
  "Name It Well - App Ideas",
  "The Competition Audit - App Ideas",
  "Scope: The Feature Budget - App Ideas",
  "Wireframes to Layout - App Ideas",
  "Copy: Words Are UI - App Ideas"
 ],
 "Building Blocks": [
  "HTML: The Skeleton - Building Blocks",
  "CSS: The Styling - Building Blocks",
  "JavaScript: The Behavior - Building Blocks",
  "Forms: Collecting Input - Building Blocks",
  "State: Remembering Things - Building Blocks",
  "Lists and Data Display - Building Blocks",
  "Navigation: Moving Between Screens - Building Blocks",
  "Storing Data: Your First Database - Building Blocks",
  "APIs: Borrowing Superpowers - Building Blocks",
  "Debugging Your App - Building Blocks",
  "Making It Look Good - Building Blocks",
  "Icons and Images - Building Blocks"
 ],
 "Launch": [
  "Testing With Real Users - Launch",
  "The Launch Checklist - Launch",
  "Sharing Your App - Launch",
  "Handling Feedback - Launch",
  "Your First 100 Users - Launch",
  "Iterate: Version Two - Launch",
  "Monetization Basics - Launch",
  "Keeping It Running - Launch",
  "Celebrate and Share the Story - Launch",
  "What You Learned Building - Launch"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# First App Study — "+safe+"\n"
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
    name:topic+' — app-building lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A app-building lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"first-app-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-build-your-first-app-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-build-your-first-app',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
