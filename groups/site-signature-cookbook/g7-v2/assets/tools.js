
function scaleServings(base, want){
  var b=Number(base), w=Number(want);
  if(!isFinite(b)||!isFinite(w)) return {error:'Enter numbers for the servings.'};
  if(b<=0||w<=0) return {error:'Servings must be more than zero.'};
  if(Math.floor(b)!==b||Math.floor(w)!==w) return {error:'Servings must be whole numbers.'};
  return {base:b, want:w, factor:Math.round((w/b)*100)/100};
}
function totalTime(prep, cook){
  var p=Number(prep), c=Number(cook);
  if(!isFinite(p)||!isFinite(c)) return {error:'Enter numbers for the minutes.'};
  if(p<0||c<0) return {error:'Minutes cannot be negative.'};
  if(Math.floor(p)!==p||Math.floor(c)!==c) return {error:'Minutes must be whole numbers.'};
  return {prep:p, cook:c, total:p+c};
}
var NAMES = ["Guacamole", "Classic Hummus", "Deviled Eggs", "Bruschetta", "Chicken Noodle Soup", "Tomato Soup", "Beef Stew", "Caesar Salad", "Greek Salad", "Roast Chicken", "Chicken Stir-Fry", "Spaghetti Bolognese", "Lasagna", "Baked Salmon", "Meatloaf", "Mashed Potatoes", "Roasted Broccoli", "Rice Pilaf", "Banana Bread", "Garlic Bread", "Dinner Rolls", "Chocolate Chip Cookies", "Vanilla Cake", "Apple Pie"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var n=NAMES[Math.floor(r()*NAMES.length)];
  return 'Fun: Rosie rolled out a crust for "'+n+'" so wide it covered the whole table — and the pie was excellent.';
}
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
if (typeof module !== 'undefined' && module.exports) module.exports = { scaleServings: scaleServings, totalTime: totalTime, makeFun: makeFun };
