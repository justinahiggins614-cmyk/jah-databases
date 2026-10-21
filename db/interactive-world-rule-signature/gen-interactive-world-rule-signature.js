(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["physics", "spawning", "economy", "ai-behavior", "events"];
var PREFIX='JAH-IWR-S-';
var USE="Used by game designers, simulation engineers, and metaverse builders to keep worlds consistent and fair.";
var FLD=[["rule", "Rule"], ["scope", "Scope"], ["effect", "Effect"]];
var DEMO="# {title} - spawn simulation (python3)\nrate={d1}\ncap={d2}\nticks={d3}\npop=0\nfor t in range(ticks):\n    pop=min(cap, pop+rate)\nprint(\"population after %d ticks: %d (cap %d)\" % (ticks, pop, cap))\nprint(\"STABLE\" if pop <= cap else \"OVERPOPULATED\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["physics", "Gravity Rule", "Applies constant downward acceleration to dynamic bodies, grounding movement and projectiles.", "Gravity Rule", "global physics", "predictable falling and jumping", "3", "40", "30"], ["spawning", "Collision Response Rule", "Resolves interpenetration with impulse or positional correction plus friction and restitution.", "Collision Response Rule", "physics bodies", "stable non-overlapping world", "2", "60", "40"], ["economy", "Spawn Rule", "Controls where, when, and how many entities appear, keeping density within design targets.", "Spawn Rule", "spawn zones", "balanced population", "3", "40", "30"], ["ai-behavior", "Despawn Rule", "Removes distant or long-idle entities to bound memory and keep simulation cost predictable.", "Despawn Rule", "world stream", "bounded entity count", "1", "80", "50"], ["events", "Day-Night Cycle", "Advances a 24-hour clock driving lighting, NPC schedules, and nocturnal gameplay systems.", "Day-Night Cycle", "global time", "living world rhythm", "1", "25", "24"], ["physics", "Economy Pricing Rule", "Sets vendor prices from supply, demand, and rarity so the in-world economy stays stable.", "Economy Pricing Rule", "trading", "no runaway inflation", "2", "50", "36"], ["spawning", "NPC Schedule Rule", "Assigns NPCs daily routines (work, eat, sleep) so towns feel inhabited around the clock.", "NPC Schedule Rule", "NPC AI", "believable crowds", "1", "70", "48"], ["economy", "Quest Trigger Rule", "Fires quests when players meet conditions, gating story progression behind real achievements.", "Quest Trigger Rule", "quests", "paced progression", "2", "30", "20"], ["ai-behavior", "Damage Falloff Rule", "Scales weapon damage with distance so close-range and long-range play stay distinct.", "Damage Falloff Rule", "combat", "fair fights", "4", "45", "25"], ["events", "Line-of-Sight Rule", "Blocks AI perception and ranged attacks through walls, making cover meaningful.", "Line-of-Sight Rule", "perception", "tactical depth", "3", "55", "30"], ["physics", "Resource Respawn Rule", "Regenerates harvestable resources on timers so gathering stays renewable but contested.", "Resource Respawn Rule", "resources", "sustainable gathering", "2", "60", "40"], ["spawning", "Weather System Rule", "Drives rain, fog, and storms that affect visibility, movement, and AI behavior.", "Weather System Rule", "environment", "dynamic atmosphere", "1", "35", "24"], ["economy", "Faction Reputation Rule", "Tracks player standing per faction, unlocking or locking quests, prices, and safe zones.", "Faction Reputation Rule", "factions", "meaningful choices", "1", "90", "60"], ["ai-behavior", "Building Placement Rule", "Validates construction against terrain slope, overlap, and zone permissions.", "Building Placement Rule", "building", "no floating structures", "4", "50", "30"], ["events", "Pathfinding Cost Rule", "Weights navmesh traversal by terrain, danger, and congestion for believable routing.", "Pathfinding Cost Rule", "navigation", "smart movement", "2", "75", "50"], ["physics", "Loot Drop Rule", "Determines drop tables and rarity rolls so rewards feel earned and economies stay intact.", "Loot Drop Rule", "rewards", "exciting progression", "5", "40", "25"], ["spawning", "Cooldown Rule", "Enforces ability cooldowns to prevent spam and preserve tactical pacing.", "Cooldown Rule", "abilities", "balanced combat", "2", "65", "40"], ["economy", "Zone Transition Rule", "Handles loading, player transfer, and state handoff when crossing world boundaries.", "Zone Transition Rule", "streaming", "seamless travel", "1", "45", "30"], ["ai-behavior", "Physics Sleep Rule", "Puts settled bodies to sleep so the physics solver skips work on static scenes.", "Physics Sleep Rule", "performance", "60fps with crowds", "3", "70", "45"], ["events", "Event Cascade Rule", "Propagates world events (alarms, explosions) to nearby systems with falloff and delay.", "Event Cascade Rule", "events", "reactive world", "2", "55", "35"]];
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
var gen={version:'jahdb-interactive-world-rule-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('interactive-world-rule-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
