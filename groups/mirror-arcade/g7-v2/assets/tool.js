/* Tools for Signature Arcade */

function scoreForTries(n){
  var t=Number(n);
  if(!isFinite(t)||Math.floor(t)!==t||t<1){return {ok:false,error:'Type a whole number of tries, 1 or more.'};}
  return {ok:true,tries:t,score:Math.max(0,100-10*(t-1))};
}
function secretForSeed(seed){
  var t=Number(seed);
  if(!isFinite(t)||Math.floor(t)!==t){return {ok:false,error:'Type a whole-number seed.'};}
  return {ok:true,seed:t,secret:((t*6)%100+100)%100};
}
if(typeof module!=='undefined'){module.exports={scoreForTries:scoreForTries,secretForSeed:secretForSeed};}
