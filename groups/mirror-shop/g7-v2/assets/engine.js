/* Seeded deterministic generator for Signature Shop — same seed, same output. Outputs are generated, never archive records. */

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
var GOODS=[{"name": "Signature Lantern", "amount": 12, "desc": "a hand-held light"}, {"name": "Signature Mug", "amount": 8, "desc": "a cup for hot drinks"}, {"name": "Signature Blanket", "amount": 25, "desc": "a warm woven cover"}, {"name": "Signature Kettle", "amount": 30, "desc": "a pot for boiling water"}, {"name": "Signature Scarf", "amount": 15, "desc": "a warm neck wrap"}, {"name": "Signature Notebook", "amount": 6, "desc": "a book of blank pages"}, {"name": "Signature Candle", "amount": 9, "desc": "a wax light"}, {"name": "Signature Backpack", "amount": 40, "desc": "a bag with straps"}, {"name": "Signature Water Bottle", "amount": 14, "desc": "a bottle for water"}, {"name": "Signature Clock", "amount": 22, "desc": "a clock for the wall"}];

function planBasket(seed){
  seed=String(seed==null||String(seed).trim()===''?'morning-cup':seed);
  var rng=rngFrom(seed);
  var goods=pickN(rng,GOODS,3), lines=[], total=0;
  for(var i=0;i<goods.length;i++){
    var qty=1+Math.floor(rng()*4), line=goods[i].amount*qty; total+=line;
    lines.push({name:goods[i].name,amount:goods[i].amount,qty:qty,line:line});
  }
  return {seed:seed,lines:lines,cartTotal:total,generated:true};
}
if(typeof module!=='undefined'){module.exports={planBasket:planBasket,hashSeed:hashSeed,rngFrom:rngFrom,pickN:pickN,GOODS:GOODS};}
