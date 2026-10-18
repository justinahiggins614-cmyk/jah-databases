(function(){'use strict';
/* The The Viewer Choice Adventure Database generator — jahdb-db-viewer-choice-adventure-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-VIEWER-CHOICE-ADVENTURE-PUB-";
var GENVER="jahdb-db-viewer-choice-adventure-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Two-Door Choice",
  "The Character Vote",
  "The Path Poll",
  "The Loot Decision",
  "The Name Choice",
  "The Meal Vote",
  "The Rest or Push",
  "The Trust Vote",
  "The Style Choice",
  "The Pet Decision",
  "The Song Vote",
  "The Omen Read"
 ],
 "Compounded": [
  "The Branching Quest",
  "The Moral Arc",
  "The Heist Plan",
  "The Mystery Vote",
  "The Expedition",
  "The Trial",
  "The Alliance",
  "The Dungeon Delve",
  "The Romance Arc",
  "The Rebellion",
  "The Treasure Map",
  "The Final Battle Plan"
 ],
 "Advanced": [
  "The Season Saga",
  "The Multiverse",
  "The Legacy Campaign",
  "The Crossover Event",
  "The Canon Vote",
  "The Prequel Vote",
  "The Ending Vote",
  "The Sequel Greenlight",
  "Teaching Choice Design",
  "Masterclass: Interactive Narrative"
 ]
};
var BLURBS={
 "The Two-Door Choice": "Left or right? The simplest branching.",
 "The Character Vote": "Who joins the party? The casting choice.",
 "The Path Poll": "Which road? The journey\u2019s fork.",
 "The Loot Decision": "Keep or share? The moral micro-choice.",
 "The Name Choice": "Name the companion: the christening vote.",
 "The Meal Vote": "What does the hero eat? The delicious decision.",
 "The Rest or Push": "Camp or press on? The strategic breather.",
 "The Trust Vote": "Trust the stranger? The dramatic dilemma.",
 "The Style Choice": "Stealth or spectacle? The approach vote.",
 "The Pet Decision": "Adopt the creature? The heart\u2019s choice.",
 "The Song Vote": "The adventure\u2019s anthem: the musical choice.",
 "The Omen Read": "Which sign to follow? The mystical fork.",
 "The Branching Quest": "A full quest with real branches: the saga begins.",
 "The Moral Arc": "Choices with consequences: the weighty adventure.",
 "The Heist Plan": "Vote the approach: the clever caper.",
 "The Mystery Vote": "Accuse the suspect: the detective democracy.",
 "The Expedition": "Plan the journey together: the logistics adventure.",
 "The Trial": "Judge the case: the courtroom choice.",
 "The Alliance": "Who do we side with? The political adventure.",
 "The Dungeon Delve": "Room by room, voted: the classic crawl.",
 "The Romance Arc": "Who wins the heart? The shippers\u2019 saga.",
 "The Rebellion": "Rise up or lay low? The revolutionary choice.",
 "The Treasure Map": "Follow which clue? The hunt, voted.",
 "The Final Battle Plan": "The endgame strategy: the epic vote.",
 "The Season Saga": "A season-long branching epic: the magnum opus.",
 "The Multiverse": "Parallel branches explored: the ambitious saga.",
 "The Legacy Campaign": "Years-long choices: the generational epic.",
 "The Crossover Event": "Many audiences, one story: the united saga.",
 "The Canon Vote": "What becomes official lore? The historic choice.",
 "The Prequel Vote": "Explore the past: the origins saga.",
 "The Ending Vote": "Choose the finale: the ultimate trust.",
 "The Sequel Greenlight": "Continue the story? The democratic renewal.",
 "Teaching Choice Design": "Show others the craft: the narrative mentor.",
 "Masterclass: Interactive Narrative": "The art of branching stories: the design theory."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — viewer choice record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-viewer-choice-adventure',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();