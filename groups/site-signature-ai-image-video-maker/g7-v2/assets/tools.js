
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function gcd(a,b){ a=Math.abs(a); b=Math.abs(b); while(b){ var t=b; b=a%b; a=t; } return a||1; }
function aspectRatio(w, h){
  var x=Number(w), y=Number(h);
  if(!isFinite(x)||!isFinite(y)) return {error:'Enter numbers for width and height.'};
  if(x<=0||y<=0||Math.floor(x)!==x||Math.floor(y)!==y) return {error:'Width and height must be whole numbers, more than zero.'};
  var g=gcd(x,y);
  return {width:x, height:y, ratio:(x/g)+':'+(y/g), pixels:x*y};
}
function hexOk(s){ return typeof s==='string' && /^#[0-9a-fA-F]{6}$/.test(s.trim()); }
function mixColors(a, b){
  if(!hexOk(a)||!hexOk(b)) return {error:'Enter two colours as #rrggbb, for example #00B8D4 and #E91E63.'};
  function ch(s,i){ return parseInt(s.substr(i,2),16); }
  function hx(n){ var s=n.toString(16); return s.length===1?'0'+s:s; }
  var r=Math.round((ch(a,1)+ch(b,1))/2), g=Math.round((ch(a,3)+ch(b,3))/2), bl=Math.round((ch(a,5)+ch(b,5))/2);
  return {a:a, b:b, mixed:'#'+hx(r)+hx(g)+hx(bl)};
}
var GOODS = ["Thunder Vista Sticker", "Golden Comet T-Shirt", "Velvet Talon Number Sticker", "Azure Comet Surfboard", "Storm Meadow Mug", "Nova Beacon Phone Case", "Golden Summit Hat", "Neon Ranger Banner", "Frozen Reef Tote Bag", "Neon Bolt Hoodie", "Nova Warden Mousepad", "Wild Sable Notebook", "Thunder Ranger Flag", "Frozen Pioneer Wall Decal", "Crimson Drift Keychain", "Blazing Canyon Water Bottle", "Azure Talon Backpack", "Crimson Voyager Calendar", "Lunar Comet Puzzle", "Azure Summit Lunchbox", "Velvet Zephyr Beach Towel", "Blazing Ranger Socks", "Echo Horizon Playing Cards", "Nova Zephyr Room Poster", "Tidal Reef Sticker", "Blazing Reef T-Shirt", "Echo Pioneer Number Sticker", "Silent Meadow Surfboard", "Drift Horizon Mug", "Thunder Talon Phone Case", "Crimson Warden Hat", "Drift Beacon Banner", "Solar Ranger Tote Bag", "Iron Yonder Hoodie", "Drift Yonder Mousepad", "Tidal Warden Notebook", "Prime Comet Flag", "Drift Surge Wall Decal", "Cosmic Pioneer Keychain", "Solar Talon Water Bottle", "Ember Beacon Backpack", "Wild Horizon Calendar", "Frozen Reef Puzzle", "Crimson Comet Lunchbox", "Blazing Summit Beach Towel", "Velvet Sable Socks", "Thunder Reef Playing Cards", "Violet Sable Room Poster", "Radiant Canyon Sticker", "Lunar Canyon T-Shirt", "Prime Comet Number Sticker", "Azure Meadow Surfboard", "Lunar Beacon Mug", "Crimson Talon Phone Case", "Silent Ranger Hat", "Violet Meadow Banner", "Nova Beacon Tote Bag", "Azure Meadow Hoodie", "Lunar Ranger Mousepad", "Thunder Zephyr Notebook", "Echo Canyon Flag", "Silent Sable Wall Decal", "Golden Zephyr Keychain", "Ember Talon Water Bottle", "Drift Zephyr Backpack", "Blazing Reef Calendar", "Frozen Falcon Puzzle", "Blazing Pioneer Lunchbox", "Tidal Summit Beach Towel", "Violet Reef Socks", "Echo Canyon Playing Cards", "Velvet Drift Room Poster", "Neon Voyager Sticker", "Neon Zephyr T-Shirt", "Cosmic Summit Number Sticker", "Velvet Beacon Surfboard", "Wild Ranger Mug", "Nova Canyon Phone Case", "Nova Onyx Hat", "Ember Sable Banner", "Azure Warden Tote Bag", "Ember Meadow Hoodie", "Velvet Ranger Mousepad", "Storm Horizon Notebook", "Mystic Talon Flag", "Ember Reef Wall Decal", "Frozen Falcon Keychain", "Neon Pioneer Water Bottle", "Drift Horizon Backpack", "Storm Drift Calendar", "Azure Reef Puzzle", "Wild Vista Lunchbox", "Frozen Comet Beach Towel", "Neon Vista Socks", "Violet Harbor Playing Cards", "Frozen Horizon Room Poster", "Iron Talon Sticker", "Drift Voyager T-Shirt", "Cosmic Yonder Number Sticker", "Ember Yonder Surfboard"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var g=GOODS[Math.floor(r()*GOODS.length)];
  return 'Fun: Pixie painted a "'+g+'" so bright that the studio wall asked for sunglasses — twice.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { aspectRatio: aspectRatio, mixColors: mixColors, makeFun: makeFun };
