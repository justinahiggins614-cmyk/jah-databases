
function wordLength(word){
  if(!word||typeof word!=='string') return {error:'Enter a word.'};
  var w=word.trim();
  if(!w) return {error:'Enter a word.'};
  var letters=w.replace(/[^A-Za-z]/g,'');
  if(!letters.length) return {error:'Enter a word with letters in it.'};
  return {word:w, letters:letters.length};
}
function alphaIndex(word){
  if(!word||typeof word!=='string') return {error:'Enter a word.'};
  var w=word.trim().toLowerCase();
  if(!w) return {error:'Enter a word.'};
  var c=w[0];
  if(c<'a'||c>'z') return {error:'The word must start with a letter from A to Z.'};
  return {word:w, letter:c.toUpperCase(), position:c.charCodeAt(0)-96};
}
var WORDS = ["a", "abroad", "academy", "accomplish", "acne", "act", "acute", "adjust", "adolescent", "adverse", "affair", "after", "ago", "aim", "alcohol", "alive", "alone", "alternate", "ambassador", "amy", "ancient", "animation", "annoying", "antique"];
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var w=WORDS[Math.floor(r()*WORDS.length)];
  return 'Fun: Dexter looked up "'+w+'" and found, on the last line, a note saying "see also: the next shelf".';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { wordLength: wordLength, alphaIndex: alphaIndex, makeFun: makeFun };
