/* Seeded deterministic generator for Signature Social — same seed, same output. Outputs are generated, never archive records. */

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
var POSTERS=[{"author": "Rin"}, {"author": "Mara"}, {"author": "Theo"}, {"author": "June"}, {"author": "Ansel"}, {"author": "Wren"}, {"author": "Kofi"}, {"author": "Lena"}];
var FRAMES=['A quiet morning on the green.','The market was busy today.','A new path through the woods.','Rain on the roof, tea in hand.','The old oak is in leaf again.','A letter arrived from the coast.','Practice went well tonight.','The harvest moon is rising.'];

function startFeed(seed){
  seed=String(seed==null||String(seed).trim()===''?'morning-cup':seed);
  var rng=rngFrom(seed);
  var authors=pickN(rng,POSTERS,3), posts=[];
  for(var i=0;i<authors.length;i++){
    var likes=Math.floor(rng()*30), comments=Math.floor(rng()*8);
    posts.push({author:authors[i].author,text:FRAMES[Math.floor(rng()*FRAMES.length)],
      likes:likes,comments:comments,score:likes+2*comments});
  }
  posts.sort(function(a,b){return b.score-a.score;});
  return {seed:seed,posts:posts,generated:true};
}
if(typeof module!=='undefined'){module.exports={startFeed:startFeed,hashSeed:hashSeed,rngFrom:rngFrom,pickN:pickN,POSTERS:POSTERS};}
