/* Seeded deterministic generator for Signature Library — same seed, same output. Outputs are generated, never archive records. */

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
var BOOKS=[{"title": "The Silver Lantern", "subjects": "stories, tales", "pages": 214}, {"title": "Tales of the Quiet Valley", "subjects": "stories, tales", "pages": 186}, {"title": "The Brass Compass", "subjects": "travel, maps", "pages": 248}, {"title": "Roads of the Far Coast", "subjects": "travel, maps", "pages": 301}, {"title": "How Rivers Shape Stone", "subjects": "science, nature", "pages": 176}, {"title": "The Garden of Small Stars", "subjects": "science, nature", "pages": 229}, {"title": "A Handbook of Knots", "subjects": "craft, making", "pages": 142}, {"title": "The Weaver's Pattern Book", "subjects": "craft, making", "pages": 198}, {"title": "Songs of the Harvest Moon", "subjects": "stories, poems", "pages": 164}, {"title": "The Mapmaker's Apprentice", "subjects": "travel, stories", "pages": 267}];

function planReadingList(seed){
  seed=String(seed==null||String(seed).trim()===''?'morning-cup':seed);
  var rng=rngFrom(seed);
  var books=pickN(rng,BOOKS,3);
  var total=0; for(var i=0;i<books.length;i++){total+=books[i].pages;}
  return {seed:seed,books:books.map(function(b){return b.title;}),totalPages:total,
    daysAt20PerDay:Math.ceil(total/20),daysAt10PerDay:Math.ceil(total/10),generated:true};
}
if(typeof module!=='undefined'){module.exports={planReadingList:planReadingList,hashSeed:hashSeed,rngFrom:rngFrom,pickN:pickN,BOOKS:BOOKS};}
