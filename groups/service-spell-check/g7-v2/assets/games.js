
/* Word Workshop games core: words from the archive headword sample. */
function letterCounts(s){var c={};for(var i=0;i<s.length;i++){var ch=s[i];c[ch]=(c[ch]||0)+1;}return c;}
function wordsFromLetters(letters, words){
  var have=letterCounts(letters.toLowerCase().replace(/[^a-z]/g,''));
  var out=[];
  for(var i=0;i<words.length;i++){
    var w=words[i]; if(w.length<3||w.length>letters.length) continue;
    var need=letterCounts(w), ok=true;
    for(var ch in need){if((have[ch]||0)<need[ch]){ok=false;break;}}
    if(ok) out.push(w);
  }
  return out.sort(function(a,b){return b.length-a.length||(a<b?-1:1);});
}
function anagramsOf(letters, words){
  var key=letters.toLowerCase().replace(/[^a-z]/g,'').split('').sort().join('');
  var out=[];
  for(var i=0;i<words.length;i++){
    var w=words[i];
    if(w.length!==key.length) continue;
    if(w.split('').sort().join('')===key) out.push(w);
  }
  return out;
}
if(typeof module!=='undefined'){module.exports={wordsFromLetters:wordsFromLetters,anagramsOf:anagramsOf};}
