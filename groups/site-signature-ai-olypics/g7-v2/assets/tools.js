
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function medalPoints(gold, silver, bronze){
  var g=Number(gold), s=Number(silver), b=Number(bronze);
  if(!isFinite(g)||!isFinite(s)||!isFinite(b)) return {error:'Enter numbers for gold, silver and bronze.'};
  if(g<0||s<0||b<0||Math.floor(g)!==g||Math.floor(s)!==s||Math.floor(b)!==b) return {error:'Medal counts must be whole numbers, zero or more.'};
  return {points: 3*g+2*s+b, gold:g, silver:s, bronze:b};
}
var EVENTS = ["Wrestling","All-Around","Sprint","Marathon","Weightlifting","Gymnastics","Debate","Puzzle Hunt"];
var TOP = ["Deterministic Engine", "Probabilistic Mind", "Geometric Six-Tool Mind", "Hash Oracle", "Neural Weaver", "Evolutionary Breeder", "Fuzzy Sage", "Swarm Coordinator", "Decision Tree Judge", "Cellular Dreamer"];
function pickBout(seed){
  var r=rng(String(seed==null?'':seed));
  var a=TOP[Math.floor(r()*TOP.length)], b=TOP[Math.floor(r()*TOP.length)];
  if(b===a) b=TOP[(TOP.indexOf(a)+1)%TOP.length];
  return {a:a, b:b, event:EVENTS[Math.floor(r()*EVENTS.length)]};
}
function makeFun(seed){
  var p=pickBout(seed);
  return 'Fun: '+p.a+' challenged '+p.b+' to a game of '+p.event+' — and the laurel wreath went to the crowd.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { medalPoints: medalPoints, pickBout: pickBout, makeFun: makeFun };
