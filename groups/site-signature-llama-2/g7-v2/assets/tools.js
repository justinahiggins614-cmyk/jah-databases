
function searchTitles(q, titles){
  if(!q || typeof q !== 'string') return [];
  var needle = q.toLowerCase().trim();
  if(!needle) return [];
  var out = [];
  for(var i=0;i<titles.length && out.length<10;i++){
    var row = titles[i];
    var hay = ((row[0]||'')+' '+(row[1]||'')).toLowerCase();
    if(hay.indexOf(needle) !== -1) out.push(row[1] + ' (' + row[0] + ')');
  }
  return out;
}

function countText(text){
  if(typeof text !== 'string') return {error:'Enter some text to count.'};
  var chars=text.length;
  var words=text.trim()==='' ? 0 : text.trim().split(/\s+/).length;
  return {chars:chars, words:words, tokens:chars, note:'Character-level estimate: one token per character.'};
}
var TITLES = [["JAH-LM2-000001", "What Meta Llama Is All About"], ["JAH-LM2-000002", "What Meta Llama is"], ["JAH-LM2-000003", "Maker and history"], ["JAH-LM2-000004", "Core features"], ["JAH-LM2-000005", "Platforms and editions"], ["JAH-LM2-000006", "Getting started"], ["JAH-LM2-000007", "How it works"], ["JAH-LM2-000008", "Files and formats"], ["JAH-LM2-000009", "Security and privacy"], ["JAH-LM2-000010", "Alternatives"], ["JAH-LM2-000011", "Pro tips"], ["JAH-LM2-000012", "Core Glossary: Meta Llama"], ["JAH-LM2-000013", "Self-Test Quiz: Meta Llama"], ["JAH-LM2-000014", "Side-by-Side Comparison: Meta Llama"], ["JAH-LM2-000015", "Selection Guide: Meta Llama"], ["JAH-LM2-000016", "Safety and Responsible Use: Meta Llama"], ["JAH-LM2-000017", "Maintenance and Troubleshooting: Meta Llama"], ["JAH-LM2-000018", "History and Turning Points: Meta Llama"], ["JAH-LM2-000019", "Teach It to Someone Else: Meta Llama"], ["JAH-LM2-000020", "Master Checklist: Meta Llama"]];
function findGuide(q){ return searchTitles(q, TITLES); }
function makeFun(seed){
  var r=rng0(seed);
  var g=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: Lulu read "'+g[1]+'" aloud to the ranch, and every llama in the pasture nodded at once.';
}
function rng0(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return (function(){ h|=0; h=(h+0x6D2B79F5)|0; var t=Math.imul(h^(h>>>15),1|h); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }); }
if (typeof module !== 'undefined' && module.exports) module.exports = { countText: countText, findGuide: findGuide, searchTitles: searchTitles, makeFun: makeFun };
