(function(){'use strict';
/* JAH The Skill Tree Generator generator - jahdb-gen-skill-tree-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real generation, not a sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-STG-";
var FIELDS=["Skill Trees"];
var SKILLS=[
 {s:'Sourdough baking',t:['Feed the starter','Mix & autolyse','Stretch & fold','Shape the loaf','Score & bake','Maintain the starter','Cold retard mastery','Capstone: market-ready loaf']},
 {s:'Conversational Spanish',t:['Core 200 words','Present-tense verbs','Ask & answer questions','Past-tense storytelling','Hold a 5-minute conversation','Idioms & slang','Debate an opinion','Capstone: 15-minute fluent chat']},
 {s:'Python programming',t:['Variables & types','Loops & conditionals','Functions','Data structures','File & error handling','OOP basics','Build a CLI tool','Capstone: shipped mini-app']},
 {s:'Watercolor painting',t:['Washes & gradients','Color mixing','Wet-on-wet','Wet-on-dry detail','Composition','Light & shadow','Plein-air session','Capstone: finished landscape']},
 {s:'Home espresso',t:['Dial in the grind','Dose & tamp','Pull the shot','Steam milk','Latte art basics','Troubleshoot sour/bitter','Single-origin exploration','Capstone: cafe-quality flat white']},
 {s:'Public speaking',t:['Beat the freeze','Structure a talk','Open strong','Storytelling','Voice & pace','Handle Q&A','Persuade a room','Capstone: 10-minute keynote']},
 {s:'Bicycle repair',t:['Fix a flat','Adjust brakes','Index gears','True a wheel','Replace a chain','Overhaul bearings','Build a wheel','Capstone: full tune-up solo']},
 {s:'Chess tactics',t:['Piece values','Forks & pins','Skewers & discovered attacks','Mating patterns','Calculate 3 deep','Openings with ideas','Endgame technique','Capstone: beat a 1200-rated player']}
];
function buildTree(skill,rnd){
 var tiers=skill.t,tiersN=4,nodes=[],per=Math.ceil(tiers.length/tiersN);
 for(var i=0;i<tiers.length;i++){var tier=Math.min(tiersN,1+((i/per)|0));
  var xp=50+tier*50+(((rnd()*40)|0));
  var pre=i===0?'':tiers[i-1];
  nodes.push({name:tiers[i],tier:tier,xp:xp,prereq:pre});}
 return nodes;
}
function demoProgram(topic,field,nodes){
  var L=['# '+topic,'# Field: '+field,'', 'nodes=['];
  nodes.forEach(function(n){L.push('nodes.append(('+JSON.stringify(n.name)+', '+n.tier+', '+n.xp+', '+JSON.stringify(n.prereq)+'))');});
  L.push('total=sum(x for _,_,x,_ in nodes)');
  L.push('print("nodes: %d  total XP: %d"%(len(nodes),total))');
  L.push('names={n:t for n,t,_,_ in nodes}');
  L.push('ok=True');
  L.push('for name,tier,xp,pre in nodes:');
  L.push('    if pre and (pre not in names or names[pre]>=tier): ok=False');
  L.push('assert ok, "prerequisite chain broken"');
  L.push('print("prerequisite chain: valid")');
  L.push('print("OK: tree generated clean")');
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var skill=opts.skill||pick(SKILLS,rnd).s;
  var defn=null,i;for(i=0;i<SKILLS.length;i++){if(SKILLS[i].s===skill){defn=SKILLS[i];break;}}
  if(!defn)defn=pick(SKILLS,rnd);
  var nodes=buildTree(defn,rnd);
  var total=0;for(i=0;i<nodes.length;i++)total+=nodes[i].xp;
  var topic='Skill tree: '+defn.s;
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,name:topic+' - '+nodes.length+' nodes',title:topic,
   description:'GENERATED SKILL TREE. '+defn.s+' mapped as '+nodes.length+' unlockable nodes '
    +'across 4 tiers, '+total+' total XP. Each node unlocks only after its prerequisite.',
   field:field,skill:defn.s,nodes:nodes,total_xp:total,
   src:'signature-generated',sample:true,
   disclaimer:'Generated tree - not an archive record.',
   demo:{kind:'skill-tree-demo',language:'python',
    program:demoProgram(topic,field,nodes),note:'Runnable builder of this exact tree.'},
   _seed:seed};
}
function validate(r){var e=[];
 if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
 if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
 if(FIELDS.indexOf(r.field)<0)e.push('field');
 if(!r.nodes||!r.nodes.length)e.push('nodes');
 if(!r.demo||!r.demo.program)e.push('demo');
 return{ok:!e.length,errors:e};}
function driftCheck(record,sample){var dups=(sample||[]).filter(function(r){return r&&r.skill===record.skill;});
 return dups.length?{ok:false,errors:['skill tree already in archive sample']}:{ok:true,errors:[]};}
var gen={version:"jahdb-gen-skill-tree-generator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:["Skill Trees"]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-skill-tree-generator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
