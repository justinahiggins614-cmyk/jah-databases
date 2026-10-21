(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["structure", "branching", "emergence", "pacing", "characters"];
var PREFIX='JAH-PSL-';
var USE="Used by narrative designers and AI storytellers to generate quests, dialogue, and plot arcs that stay coherent.";
var FLD=[["pattern", "Pattern"], ["structure", "Structure"], ["use", "Use"]];
var DEMO="# {title} - ending count estimate (python3)\nbranches={d1}\ndepth={d2}\nmax_end={d3}\nendings=branches**depth\nprint(\"possible endings: %d\" % endings)\nprint(\"MANAGEABLE\" if endings <= max_end else \"PRUNE NEEDED\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["structure", "Beat Graph", "Represents story beats as a directed graph where edges carry preconditions, letting the engine pick valid next beats.", "Beat Graph", "directed graph", "dynamic quest chains", "3", "4", "200"], ["branching", "Branching Dialogue Tree", "Classic choice tree where each player line selects a child node, with merge points to bound explosion.", "Branching Dialogue Tree", "tree with merges", "conversation systems", "2", "5", "100"], ["emergence", "State Machine Quest", "Models quest stages as states with guarded transitions, making quest logic testable and debuggable.", "State Machine Quest", "finite state machine", "mission logic", "3", "3", "60"], ["pacing", "Emergent Faction Simulation", "Simulates faction goals and resources so conflicts and alliances arise without scripted beats.", "Emergent Faction Simulation", "agent simulation", "living politics", "4", "6", "500"], ["characters", "Three-Act Template", "Fits generated plots to setup, confrontation, and resolution proportions for familiar pacing.", "Three-Act Template", "act structure", "main story arcs", "2", "3", "40"], ["structure", "Hero's Journey Arc", "Maps generated events onto departure, initiation, and return stages for mythic resonance.", "Hero's Journey Arc", "monomyth stages", "epic campaigns", "3", "4", "80"], ["branching", "Flashback Frame", "Presents the story as a flashback, letting the generator reveal backstory as collectible memories.", "Flashback Frame", "framing device", "mystery plots", "2", "3", "50"], ["emergence", "Parallel Timelines", "Runs two timelines whose events rhyme, converging at a finale the player assembles.", "Parallel Timelines", "dual timeline", "puzzle narratives", "2", "4", "70"], ["pacing", "Choice Consequence Ledger", "Logs every major choice with delayed consequences, so decisions echo hours later.", "Choice Consequence Ledger", "ledger", "meaningful choices", "3", "5", "120"], ["characters", "Relationship Matrix", "Tracks pairwise affinity between characters, gating dialogue options and betrayals.", "Relationship Matrix", "affinity matrix", "social simulation", "4", "3", "90"], ["structure", "Procedural Backstory", "Generates each NPC's history from life-event tables, giving rumors and motives on demand.", "Procedural Backstory", "life paths", "open-world NPCs", "3", "4", "150"], ["branching", "Dynamic Difficulty Story", "Adjusts story pressure (timers, enemy counts) to the player's demonstrated skill.", "Dynamic Difficulty Story", "difficulty curve", "accessible epics", "2", "3", "45"], ["emergence", "Moral Alignment Tracker", "Scores actions on axes like mercy vs justice, unlocking endings tied to the player's ethics.", "Moral Alignment Tracker", "alignment axes", "branching endings", "3", "2", "30"], ["pacing", "Rumor Propagation", "Spreads procedurally generated rumors through NPC networks with distortion per hop.", "Rumor Propagation", "network diffusion", "living gossip", "4", "5", "200"], ["characters", "Memory System", "Gives NPCs persistent memories of player deeds so the world reacts to history.", "Memory System", "episodic memory", "reactive NPCs", "3", "4", "110"], ["structure", "Goal-Plan Decomposition", "Breaks high-level story goals into character plans with steps, conflicts, and fallbacks.", "Goal-Plan Decomposition", "HTN planning", "agent-driven plots", "3", "3", "75"], ["branching", "Scene Weaving", "Interleaves A and B plots by dramatic tension, cutting between storylines at cliffhangers.", "Scene Weaving", "interleaving", "serialized pacing", "2", "2", "25"], ["emergence", "Dramatic Irony Engine", "Engineers situations where the player knows more than characters, creating tension.", "Dramatic Irony Engine", "knowledge gaps", "thriller beats", "2", "3", "55"], ["pacing", "Pacing Controller", "Monitors tension over time and injects action or breather beats to hold the designed curve.", "Pacing Controller", "tension curve", "engagement", "2", "4", "65"], ["characters", "Ending Resolver", "Selects and composes the finale from accumulated flags, delivering a coherent payoff.", "Ending Resolver", "flag resolution", "satisfying endings", "3", "5", "140"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-procedural-story-logic-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('procedural-story-logic',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
