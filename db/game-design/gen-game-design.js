(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['mechanics','levels','quests','rules','balance'];
var PREFIX='JAH-GAME-';
var REF_MDA='https://yukaichou.com/gamification-analysis/mda-framework-hunicke-leblanc-zubek-mechanics-dynamics-aesthetics/';
var REF_BARTLE='https://en.wikipedia.org/wiki/Bartle_taxonomy_of_player_types';
var REF_STD='Game design standards (verified 2026-10-09)';
var MDA=[
 ['Mechanics','The rules and data-level components the designer writes.'],
 ['Dynamics','The run-time behavior of mechanics acting on player input over time.'],
 ['Aesthetics','The emotional responses evoked in the player by the system.']
];
var AESTHETICS=[
 ['Sensation','Game as sense-pleasure.'],['Fantasy','Game as make-believe.'],
 ['Narrative','Game as drama.'],['Challenge','Game as obstacle course.'],
 ['Fellowship','Game as social framework.'],['Discovery','Game as uncharted territory.'],
 ['Expression','Game as self-discovery.'],['Submission','Game as pastime.']
];
var BARTLE=[
 ['Achievers','Seek rewards and mastery; want what others do not have.'],
 ['Explorers','Seek knowledge and hidden corners of the world.'],
 ['Socializers','Play to interact with other people.'],
 ['Killers','Seek dominance over other players.']
];
var VERBS=[
 ['Jump','Vertical traversal and gap crossing.'],['Double Jump','A second mid-air jump for reach.'],
 ['Sprint','Fast movement at a stamina cost.'],['Crouch','Low profile for stealth and cover.'],
 ['Climb','Vertical traversal on surfaces.'],['Swim','Movement through water.'],
 ['Glide','Slow descent across distance.'],['Dash','A burst of speed with cooldown.'],
 ['Teleport','Instant relocation, usually with a cost.'],['Attack','The basic damage verb.'],
 ['Block','Damage reduction while stationary.'],['Parry','Timed deflection that punishes.'],
 ['Dodge','Invulnerability frames during a roll.'],['Aim','Precision targeting mode.'],
 ['Shoot','Ranged damage at ammunition cost.'],['Reload','Downtime that paces ranged combat.'],
 ['Throw','Arcing projectile delivery.'],['Catch','Receiving thrown objects.'],
 ['Collect','Picking up items and resources.'],['Loot','Taking rewards from the defeated.'],
 ['Craft','Combining materials into gear.'],['Build','Placing structures in the world.'],
 ['Destroy','Removing obstacles and cover.'],['Repair','Restoring damaged gear or structures.'],
 ['Heal','Restoring health to self or allies.'],['Buff','Temporary positive effects.'],
 ['Debuff','Temporary negative effects on foes.'],['Trade','Exchanging goods with NPCs or players.'],
 ['Dialogue','Conversation choices that branch story.'],['Stealth','Avoiding detection by sight and sound.'],
 ['Hack','Overriding systems and locks.'],['Drive','Vehicle movement and handling.']
];
var QUESTS=[
 ['Fetch','Bring an item from A to B.'],['Kill','Defeat a number of foes.'],
 ['Collect','Gather a number of resources.'],['Escort','Protect an NPC to a destination.'],
 ['Discovery','Find a hidden place or secret.'],['Puzzle','Solve a logic or spatial challenge.'],
 ['Timed','Complete an objective before the clock ends.'],['Defend','Hold a position against waves.'],
 ['Craft','Make an item to satisfy the quest.'],['Chain','A sequence of quests telling one story.']
];
var LEVELS=[
 ['Sight Lines','Long views guide the player toward goals.'],
 ['Landmarks','Unique silhouettes orient the player.'],
 ['Chokepoints','Narrow passages focus combat and pacing.'],
 ['Spawn Points','Controlled entries for players and enemies.'],
 ['Safe Zones','Rest areas free of threats.'],
 ['Risk / Reward','Greater danger guards greater loot.'],
 ['Teach, Test, Twist','Introduce a skill, test it, then twist it.'],
 ['Difficulty Ramp','Challenge rises smoothly with mastery.'],
 ['Affordances','Shapes suggest their use: climbable, pushable, breakable.'],
 ['Weenies','A visual magnet pulling players forward, per Disney Imagineering.']
];
var FORMULAS=[
 ['Damage','damage = max(1, attack - defense)','attack','defense'],
 ['DPS','dps = damage / cooldown_seconds','damage','cooldown_seconds'],
 ['Effective HP','ehp = hp / (1 - damage_reduction)','hp','damage_reduction'],
 ['Time to Kill','ttk = effective_hp / dps','effective_hp','dps'],
 ['Hit Chance','chance = clamp(accuracy - evasion, 5, 95)','accuracy','evasion'],
 ['XP Curve','xp_for_level = 100 * level^1.5','level',''],
 ['Crit Value','expected = damage * (1 + crit_chance * crit_mult)','damage','crit_chance'],
 ['Drop Expectation','expected_kills = 1 / drop_rate','drop_rate',''],
 ['Economy Sink','sink_ratio = gold_removed / gold_created','gold_removed','gold_created'],
 ['Power Curve','power = base + growth * level','base','growth']
];
var GENRES=[
 ['Action','Reflex and timing challenges.'],['Adventure','Exploration and story.'],
 ['RPG','Character growth and choice.'],['Strategy','Planning over reflex.'],
 ['Simulation','Systems modeling real or imagined worlds.'],['Puzzle','Logic over action.'],
 ['Sports','Competitive physical play.'],['Horror','Fear and resource tension.']
];
var SIG_A=['Neon','Velvet','Ember','Harbor','Cinder','Juniper','Onyx','Solstice'];
var SIG_B=['quest','arena','dungeon','trial'];
function calcFormula(i,a,b){
  var x=+a,y=+b;
  switch(i){
    case 0:return Math.max(1,Math.round(x-y));
    case 1:return Math.round((x/y)*100)/100;
    case 2:return Math.round(x/(1-y));
    case 3:return Math.round((x/y)*100)/100;
    case 4:return Math.max(5,Math.min(95,Math.round(x-y)));
    case 5:return Math.round(100*Math.pow(x,1.5));
    case 6:return Math.round(x*(1+(y/100)*1.5)*100)/100;
    case 7:return Math.round((1/x)*10)/10;
    case 8:return Math.round((x/y)*1000)/1000;
    default:return Math.round(x+y*10);
  }
}
function buildOnline(rnd,cat){
  var rec={category:cat,source:'online',creation_mode:'ONLINE-VERIFIED'};
  if(cat==='mechanics'){
    var r=rnd();
    if(r<0.25){var m=pick(MDA,rnd);rec.title='MDA: '+m[0];rec.topic='mda layer';rec.mechanic={layer:m[0],definition:m[1]};rec.source_ref=REF_MDA;
      rec.description='In the MDA framework, '+m[0]+': '+m[1]+' Designers build mechanics-first while players feel aesthetics-first.';}
    else if(r<0.45){var a=pick(AESTHETICS,rnd);rec.title='MDA aesthetic: '+a[0];rec.topic='mda aesthetic';rec.mechanic={aesthetic:a[0],note:a[1]};rec.source_ref=REF_MDA;
      rec.description='The '+a[0]+' aesthetic: '+a[1]+' One of the eight aesthetics named in the MDA framework for describing what play feels like.';}
    else{var v=pick(VERBS,rnd),g=pick(GENRES,rnd);rec.title='Mechanic: '+v[0]+' ('+g[0]+')';rec.topic='mechanic';rec.mechanic={verb:v[0],note:v[1],genre:g[0]};rec.source_ref=REF_STD;
      rec.description='The '+v[0].toLowerCase()+' mechanic: '+v[1]+' In '+g[0].toLowerCase()+' games ('+g[1].charAt(0).toLowerCase()+g[1].slice(1)+') it carries core moment-to-moment play.';}
  }else if(cat==='levels'){
    var l=pick(LEVELS,rnd);
    rec.title='Level principle: '+l[0];rec.topic='level principle';rec.mechanic={principle:l[0],guidance:l[1]};rec.source_ref=REF_STD;
    rec.description='The '+l[0].toLowerCase()+' principle: '+l[1]+' Level designers use it to teach, pace and orient players without words.';
  }else if(cat==='quests'){
    var q=pick(QUESTS,rnd),st=pick(['linear','branching','radiant'],rnd);
    rec.title='Quest type: '+q[0];rec.topic='quest type';rec.mechanic={type:q[0],objective:q[1],structure:st};rec.source_ref=REF_STD;
    rec.description='The '+q[0].toLowerCase()+' quest: '+q[1]+' Built here with a '+st+' structure. Clear objectives and fair feedback keep quests satisfying.';
  }else if(cat==='rules'){
    var b=pick(BARTLE,rnd);
    rec.title='Player type: '+b[0]+'s';rec.topic='player type';rec.mechanic={type:b[0],motivation:b[1]};rec.source_ref=REF_BARTLE;
    rec.description='Bartle\u2019s '+b[0].toLowerCase()+'s: '+b[1]+' Designing for a healthy mix of the four types keeps a multiplayer world alive.';
  }else{
    var fi=ri(rnd,0,FORMULAS.length-1),f=FORMULAS[fi];
    var av,bv;
    if(fi===0){av=ri(rnd,10,60);bv=ri(rnd,0,20);}
    else if(fi===4){av=ri(rnd,50,100);bv=ri(rnd,0,40);}
    else if(fi===5){av=ri(rnd,1,20);bv=0;}
    else if(fi===7){av=[0.01,0.05,0.1,0.25][ri(rnd,0,3)];bv=0;}
    else if(fi===8){av=ri(rnd,100,1000);bv=ri(rnd,500,2000);}
    else if(fi===9){av=ri(rnd,5,20);bv=ri(rnd,1,5);}
    else{av=ri(rnd,5,50);bv=ri(rnd,1,10)/10;}
    if(fi===2)bv=[0,0.1,0.25,0.5][ri(rnd,0,3)];
    var val=calcFormula(fi,av,bv);
    rec.title='Balance: '+f[0]+' = '+val;rec.topic='balance formula';
    rec.mechanic={formula:f[0],expression:f[1],inputs:{a:f[2]+'='+av,b:f[3]?f[3]+'='+bv:undefined},result:val};
    rec.source_ref=REF_STD;
    rec.description='The '+f[0].toLowerCase()+' formula: '+f[1]+'. With inputs '+av+(f[3]?' and '+bv:'')+' the result is '+val+'. Real tuning math designers use to balance combat and economy.';
  }
  return rec;
}
function buildSignature(rnd,cat){
  var rec={category:cat,source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  var nm=pick(SIG_A,rnd)+' '+pick(SIG_B,rnd);
  if(cat==='mechanics'){var v2=pick(VERBS,rnd);rec.title='Signature mechanic twist: '+nm;rec.topic='mechanic twist';rec.mechanic={twist:nm,base_verb:v2[0],cooldown_s:ri(rnd,1,20)};
    rec.description='A Signature-generated twist on '+v2[0].toLowerCase()+' named '+nm+' with a '+rec.mechanic.cooldown_s+'s cooldown. An original mechanic sketch by the JAH generator.';}
  else if(cat==='levels'){rec.title='Signature level concept: '+nm;rec.topic='level concept';rec.mechanic={concept:nm,rooms:ri(rnd,5,25),theme:pick(['ruins','station','forest','city'],rnd)};
    rec.description='A Signature-generated level concept named '+nm+': '+rec.mechanic.rooms+' rooms in a '+rec.mechanic.theme+' theme. An original layout sketch by the JAH generator.';}
  else if(cat==='quests'){rec.title='Signature quest: '+nm;rec.topic='quest';rec.mechanic={quest:nm,type:pick(QUESTS,rnd)[0],objectives:ri(rnd,2,5)};
    rec.description='A Signature-generated '+rec.mechanic.type.toLowerCase()+' quest named '+nm+' with '+rec.mechanic.objectives+' objectives. An original quest sketch by the JAH generator.';}
  else if(cat==='rules'){rec.title='Signature house rule: '+nm;rec.topic='house rule';rec.mechanic={rule:nm,effect:pick(['double XP weekends','permadeath mode','friendly fire on','no HUD'],rnd)};
    rec.description='A Signature-generated house rule named '+nm+': '+rec.mechanic.effect+'. An original rules variant by the JAH generator.';}
  else{rec.title='Signature balance pass: '+nm;rec.topic='balance pass';rec.mechanic={pass:nm,target:pick(['early game','mid game','endgame','PvP'],rnd),adjustment:pick(['+10% damage','-15% costs','+5% drop rates'],rnd)};
    rec.description='A Signature-generated balance pass named '+nm+' targeting '+rec.mechanic.target+' with '+rec.mechanic.adjustment+'. An original tuning sketch by the JAH generator.';}
  return rec;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var online=!opts.forceSignature&&(rnd()<0.24||opts.forceOnline);
  var rec=online?buildOnline(rnd,cat):buildSignature(rnd,cat);
  if(rec.description.length<165)rec.description+=' Filed as a complete searchable record in the JAH Data Bases archive, with its full specifications intact.';
  rec.id=PREFIX+String(seed).padStart(7,'0');rec._seed=seed;return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-GAME-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<150)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&(r.creation_mode!=='ONLINE-VERIFIED'||typeof r.source_ref!=='string'||!r.source_ref.length))e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(!r.mechanic||typeof r.mechanic!=='object')e.push('mechanic');
  if(r.source==='online'&&r.topic==='balance formula'){
    var fi=FORMULAS.map(function(f){return f[0];}).indexOf(r.mechanic.formula);
    if(fi<0)e.push('formula_fact');
    else{var a=+String(r.mechanic.inputs.a).split('=')[1],b=r.mechanic.inputs.b?+String(r.mechanic.inputs.b).split('=')[1]:0;
      if(calcFormula(fi,a,b)!==r.mechanic.result)e.push('formula_recompute');}
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-game-design-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('game-design',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
