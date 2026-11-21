/* Seeded deterministic generator for Signature Arcade — same seed, same output. Outputs are generated, never archive records. */

function hashSeed(s){
  var h=2166136261>>>0; s=String(s==null?'':s);
  for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); }
  return h>>>0;
}
function rngFrom(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pickN(rng, arr, n){
  var copy=arr.slice(), out=[];
  while(out.length<n && copy.length){ out.push(copy.splice(Math.floor(rng()*copy.length),1)[0]); }
  return out;
}
var GAMES=[{"name": "Secret Number", "kind": "number guessing", "rules": "Guess the secret number from 1 to 100."}, {"name": "Lantern Maze", "kind": "maze", "rules": "Guide a lantern through 12 rooms to the far gate."}, {"name": "Starfall Catch", "kind": "catching", "rules": "Catch 20 falling stars before 5 slip past."}, {"name": "Word Ladder", "kind": "word play", "rules": "Climb from one word to another, changing one letter at a time."}, {"name": "River Stones", "kind": "puzzle", "rules": "Cross the river by stepping only on stones that add to 50."}, {"name": "Comet Dodge", "kind": "dodging", "rules": "Steer a small ship past 30 comets."}, {"name": "Garden Match", "kind": "matching", "rules": "Pair 8 sets of garden tiles in as few turns as you can."}, {"name": "Beacon Code", "kind": "code breaking", "rules": "Find a 4-symbol code from the beacon's clues."}, {"name": "Harbor Checkers", "kind": "board play", "rules": "A two-player checkers board beside the harbor."}, {"name": "Cloud Hop", "kind": "hopping", "rules": "Hop across 15 clouds without missing a step."}];

function planGameNight(seed){
  seed=String(seed==null||String(seed).trim()===''?'morning-cup':seed);
  var rng=rngFrom(seed);
  var games=pickN(rng,GAMES,3).map(function(g){return g.name;});
  var rounds=3+Math.floor(rng()*4);
  var secret=hashSeed(seed)%100;
  var target=Math.max(0,100-10*(rounds-1));
  return {seed:seed,games:games,rounds:rounds,secret:secret,targetScore:target,generated:true};
}
if(typeof module!=='undefined'){module.exports={planGameNight:planGameNight,hashSeed:hashSeed,rngFrom:rngFrom,pickN:pickN,GAMES:GAMES};}
