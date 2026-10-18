(function(){'use strict';
/* JAH The Build Your First App Signature Database generator — jahdb-db-build-your-first-app-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BYFAS-";
var FIELDS=["App Ideas","Building Blocks","Launch"];
var TOPICS={
 "App Ideas": [
  "What Counts as an App (Signature Edition) - App Ideas",
  "Find a Problem Worth Solving (Signature Edition) - App Ideas",
  "The One-Sentence Pitch (Signature Edition) - App Ideas",
  "Sketch Before You Code (Signature Edition) - App Ideas",
  "User Stories: Features as Promises (Signature Edition) - App Ideas",
  "MVP: The Smallest Real Thing (Signature Edition) - App Ideas",
  "Pick Your Platform (Signature Edition) - App Ideas",
  "Name It Well (Signature Edition) - App Ideas",
  "The Competition Audit (Signature Edition) - App Ideas",
  "Scope: The Feature Budget (Signature Edition) - App Ideas",
  "Wireframes to Layout (Signature Edition) - App Ideas",
  "Copy: Words Are UI (Signature Edition) - App Ideas"
 ],
 "Building Blocks": [
  "HTML: The Skeleton (Signature Edition) - Building Blocks",
  "CSS: The Styling (Signature Edition) - Building Blocks",
  "JavaScript: The Behavior (Signature Edition) - Building Blocks",
  "Forms: Collecting Input (Signature Edition) - Building Blocks",
  "State: Remembering Things (Signature Edition) - Building Blocks",
  "Lists and Data Display (Signature Edition) - Building Blocks",
  "Navigation: Moving Between Screens (Signature Edition) - Building Blocks",
  "Storing Data: Your First Database (Signature Edition) - Building Blocks",
  "APIs: Borrowing Superpowers (Signature Edition) - Building Blocks",
  "Debugging Your App (Signature Edition) - Building Blocks",
  "Making It Look Good (Signature Edition) - Building Blocks",
  "Icons and Images (Signature Edition) - Building Blocks"
 ],
 "Launch": [
  "Testing With Real Users (Signature Edition) - Launch",
  "The Launch Checklist (Signature Edition) - Launch",
  "Sharing Your App (Signature Edition) - Launch",
  "Handling Feedback (Signature Edition) - Launch",
  "Your First 100 Users (Signature Edition) - Launch",
  "Iterate: Version Two (Signature Edition) - Launch",
  "Monetization Basics (Signature Edition) - Launch",
  "Keeping It Running (Signature Edition) - Launch",
  "Celebrate and Share the Story (Signature Edition) - Launch",
  "What You Learned Building (Signature Edition) - Launch"
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
var gen={version:'jahdb-db-build-your-first-app-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-build-your-first-app-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
