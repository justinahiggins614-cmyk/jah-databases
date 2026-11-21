var TEMPLATES = [["JAH-TPL-0000001", "Cozy Bakery Studio", "Soft Pastel"], ["JAH-TPL-0000002", "Cozy Portfolio Garden", "Sunny Bright"], ["JAH-TPL-0000003", "Shiny Blog Garden", "Ocean Fresh"], ["JAH-TPL-0000004", "Lucky Local Nest", "Soft Pastel"], ["JAH-TPL-0000005", "Zesty Online Works", "Ocean Fresh"], ["JAH-TPL-0000006", "Clever Restaurant Corner", "Bold Modern"], ["JAH-TPL-0000007", "Prime Photography House", "Bold Modern"], ["JAH-TPL-0000008", "Merry Music Works", "Royal Gold"], ["JAH-TPL-0000009", "Shiny Fitness Garden", "Earthy Calm"], ["JAH-TPL-0000010", "Rapid Real Garden", "Earthy Calm"], ["JAH-TPL-0000011", "Swift Salon Station", "Ocean Fresh"], ["JAH-TPL-0000012", "Noble Auto Post", "Royal Gold"], ["JAH-TPL-0000013", "Merry Pet Garden", "Bold Modern"], ["JAH-TPL-0000014", "Golden Kids Harbor", "Sunny Bright"], ["JAH-TPL-0000015", "True Education Post", "Earthy Calm"], ["JAH-TPL-0000016", "Rapid Nonprofit Nest", "Cozy Classic"], ["JAH-TPL-0000017", "Warm Church Hub", "Dark Neon"], ["JAH-TPL-0000018", "Happy Events Place", "Bold Modern"], ["JAH-TPL-0000019", "Rapid Travel Post", "Earthy Calm"], ["JAH-TPL-0000020", "Happy Tech Shop", "Royal Gold"], ["JAH-TPL-0000021", "Warm Bakery Garden", "Soft Pastel"], ["JAH-TPL-0000022", "Zesty Portfolio Station", "Bold Modern"], ["JAH-TPL-0000023", "Noble Blog Post", "Earthy Calm"], ["JAH-TPL-0000024", "Vivid Local Studio", "Sunny Bright"]];
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }

function slugifyTitle(title){
  if(title==null) return {error:'Enter a website title, for example Cozy Bakery Studio.'};
  var s=String(title).trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
  if(!s) return {error:'That title has no letters or numbers to make a slug from.'};
  return {title:title, slug:s};
}
function styleCount(style){
  if(style==null) return {error:'Enter a style, for example Soft Pastel.'};
  var s=String(style).trim().toLowerCase();
  if(!s) return {error:'Enter a style, for example Soft Pastel.'};
  var n=0;
  for(var i=0;i<TEMPLATES.length;i++){ if(TEMPLATES[i][2].toLowerCase()===s) n++; }
  if(n===0){
    var known=[]; for(var j=0;j<TEMPLATES.length;j++){ if(known.indexOf(TEMPLATES[j][2])===-1) known.push(TEMPLATES[j][2]); }
    return {error:'Style "'+style+'" is not among the 8 styles. Try: '+known.join(', ')+'.'};
  }
  return {style:style, count:n};
}
var TITLES = ["Cozy Bakery Studio", "Cozy Portfolio Garden", "Shiny Blog Garden", "Lucky Local Nest", "Zesty Online Works", "Clever Restaurant Corner", "Prime Photography House", "Merry Music Works", "Shiny Fitness Garden", "Rapid Real Garden", "Swift Salon Station", "Noble Auto Post", "Merry Pet Garden", "Golden Kids Harbor", "True Education Post", "Rapid Nonprofit Nest", "Warm Church Hub", "Happy Events Place", "Rapid Travel Post", "Happy Tech Shop", "Warm Bakery Garden", "Zesty Portfolio Station", "Noble Blog Post", "Vivid Local Studio"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var t=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: Webby wove "'+t+'" into the web — and the whole Workshop fit inside it.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { slugifyTitle: slugifyTitle, styleCount: styleCount, makeFun: makeFun };
