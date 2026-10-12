(function(){'use strict';
/* JAH Public Video Games Database generator — jahdb-public-video-games-1.0.
   Property of Justin Addam Higgins (JAH).
   Generates complete game records. Two kinds:
   - 'playable-arcade': references one of the 12 hand-built playable games (only via opts.playableSlug, never invented).
   - 'game-design': full original game design documents (Signature-authored, src:'signature').
   The generator NEVER claims a generated record is playable in-browser. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-PVG-';
var PLAYABLE={
  snake:{title:'Snake',genre:'action',controls:'Arrows / WASD / numpad 2468 to steer; on-screen D-pad on phone.'},
  pong:{title:'Pong',genre:'action',controls:'W/S or up/down (numpad 8/2); tap above/below the paddle or use the on-screen buttons on phone.'},
  breakout:{title:'Breakout',genre:'action',controls:'Left/right arrows (A/D, numpad 4/6); drag on the court or use on-screen buttons on phone. SPACE launches.'},
  invaders:{title:'Invaders',genre:'action',controls:'Left/right to move, SPACE to fire; on-screen ◀ ▶ FIRE buttons on phone.'},
  blocks:{title:'Blocks',genre:'puzzle',controls:'Arrows: move/rotate/drop. Numpad 4/6/2/8/5/0. On-screen buttons on phone.'},
  minesweeper:{title:'Minesweeper',genre:'puzzle',controls:'Tap/click to reveal, DIG/FLAG mode button or right-click to flag.'},
  '2048':{title:'2048',genre:'puzzle',controls:'Arrow keys or numpad 2468; swipe or on-screen pad on phone.'},
  flier:{title:'Flier',genre:'action',controls:'SPACE / tap / click to flap; on-screen FLAP button on phone.'},
  sokoban:{title:'Sokoban',genre:'puzzle',controls:'Arrows / WASD / numpad to push; A=undo, B=reset; on-screen pad on phone.'},
  asteroids:{title:'Asteroids',genre:'action',controls:'Left/right rotate, up thrust, SPACE fire; on-screen buttons on phone.'},
  hopper:{title:'Hopper',genre:'action',controls:'Arrows / WASD / numpad 2468 to hop; on-screen D-pad on phone.'},
  simon:{title:'Simon',genre:'puzzle',controls:'Tap the pads, click them, or press numpad 1-4.'}
};
var GENRES=['action','puzzle','strategy','racing','simulation','rpg','fps','rhythm','platformer','adventure'];
var MECHS=[
 ['time-attack','Beat the clock across 12 hand-tuned stages; medals for gold/silver/bronze times.'],
 ['combo-chain','Chain actions without a miss to multiply the score; one mistake resets the chain.'],
 ['territory','Claim zones faster than the rival; holding a majority for 10 seconds wins the round.'],
 ['escort','Guide the convoy through 8 hazard lanes; losing the cargo ends the run.'],
 ['survival','Endless waves with rising speed; every 5 waves unlocks a new hazard type.'],
 ['collection','Gather all 60 tokens across 5 maps; hidden tokens need ability combos to reach.'],
 ['boss-rush','Five bosses, no healing between; learn each pattern in 3 phases.'],
 ['puzzle-ladder','100 handcrafted puzzles in rising difficulty; par move counts included.']
];
var WORLDS=[
 ['Neon Harbor','a rain-slick port city of glowing signs'],
 ['Cinder Wastes','a volcanic desert of glass dunes'],
 ['Verdant Deep','an overgrown jungle of giant flora'],
 ['Frostline','a frozen research outpost'],
 ['Hollow Orbit','a derelict ring station'],
 ['Ember Isles','a chain of volcanic islands']
];
var HOOKS=[
 'one more run is always 90 seconds away',
 'every death teaches the next attempt',
 'the leaderboard is your rival',
 'master one mechanic, then the game remixes it',
 'short sessions, long mastery curve',
 'easy to start, brutal to perfect'
];
function normGenre(g){
  if(!g) return null;
  var t=String(g).toLowerCase().trim().replace(/[^a-z0-9]+/g,'');
  for(var i=0;i<GENRES.length;i++) if(GENRES[i]===t) return GENRES[i];
  return null;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var slug=opts.playableSlug;
  if(slug&&PLAYABLE[slug]){
    var p=PLAYABLE[slug];
    return {id:id,title:p.title,description:'A complete, playable arcade game in the Public Video Games Database — open this record and press play to run it right in the browser. '+p.controls,
      genre:p.genre,year:2026,license:'Openly licensed (MIT) in-browser original',developer:'JAH Databases arcade studio',
      playable:true,play_url:'play.html?game='+slug,controls:p.controls,src:'signature',_seed:seed,game_slug:slug};
  }
  var g=normGenre(opts.genre)||pick(GENRES,rnd);
  var mech=pick(MECHS,rnd), world=pick(WORLDS,rnd), hook=pick(HOOKS,rnd);
  var title=world[0]+': '+mech[0].split('-').map(function(w){return w[0].toUpperCase()+w.slice(1);}).join(' ');
  return {
    id:id,
    title:title,
    description:'A complete original game design document: "'+title+'" ('+g+'). Set in '+world[1]+'. Core loop: '+mech[1]+' The hook: '+hook+'. Includes full mechanics, controls, level structure, and scoring — a build-ready design.',
    genre:g, year:2026, license:'Signature-authored design (not yet built)', developer:'JAH Databases arcade studio',
    playable:false, play_url:null,
    controls:'Designed for keyboard (arrows/WASD/numpad) and touch (on-screen pad, tap, swipe) when built.',
    src:'signature', _seed:seed,
    design:{world:world[0],setting:world[1],mechanic:mech[0],loop:mech[1],hook:hook,
      levels:'12 stages in 3 tiers (learn / remix / master)', scoring:'Base points × combo multiplier; medals at score thresholds'}
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PVG-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<3)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(typeof r.playable!=='boolean')e.push('playable');
  if(r.playable&&typeof r.play_url!=='string')e.push('play_url');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES,playable:PLAYABLE};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-video-games',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
