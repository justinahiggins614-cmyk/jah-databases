(function(){'use strict';
/* Game Release Database generator — jahdb-game-release-1.0.
   Property of Justin Addam Higgins (JAH).
   Type 1 public record: seeded records are real verified facts (src public-harvest).
   The generator mints clearly-labeled SAMPLE records only — never presented as real.
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-GMR-';
var GROUPS=["1970s","1980s","1990s","2000s","2010s","2020s"];
var SAMPLE_NAMES=["Pong","Space Invaders","Pac-Man","Donkey Kong","Tetris","Super Mario Bros.","The Legend of Zelda","Dragon Quest","Final Fantasy","Mega Man 2","Tetris (Game Boy)","Super Mario World","Sonic the Hedgehog","Street Fighter II","Mortal Kombat","Doom","Super Metroid","Final Fantasy VII","Super Mario 64","Pok\u00e9mon Red and Green"];
function generate(seed,opts){
  opts=opts||{};var s=prng(seed);
  var grp=opts.group&&GROUPS.indexOf(opts.group)>=0?opts.group:pick(GROUPS,s);
  var name=pick(SAMPLE_NAMES,s);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,name:name,title:name,
    description:'SAMPLE RECORD (generated — structural sample). A game release sample generated deterministically from seed '+seed+'. Generated samples are clearly labeled and never presented as real records.',
    group:grp,g:grp,t:'sample',
    src:'signature-generated-sample',year:2026,_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-]/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<2)e.push('name');
  if(!r.src)e.push('src');
  return{ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.src==='public-harvest';});
  return dups.length?{ok:false,errors:['name collides with a real archive record']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-game-release-1.0',generate:generate,validate:validate,driftCheck:driftCheck,groups:GROUPS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('game-release',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
