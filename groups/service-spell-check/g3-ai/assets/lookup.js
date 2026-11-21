
/* Word lookup for the spelling helper: headword + regular-form rules,
   same rules as the Group 1 checker (see its words-README). */
var BLOCKED={'thier':'their','mispelled':'misspelled','mispell':'misspell','withing':'within','accidently':'accidentally','basicly':'basically','truely':'truly','arguement':'argument','writting':'writing','comming':'coming','geting':'getting','makeing':'making','useing':'using','haveing':'having','liveing':'living','danceing':'dancing','happyness':'happiness','calender':'calendar','grammer':'grammar','prefering':'preferring','refering':'referring'};
var WORDSET=null;
function lookupIsWord(w){
  if(BLOCKED[w]) return false;
  if(!WORDSET) return true;
  if(WORDSET.has(w)) return true;
  var s;
  if(w.endsWith('ies')&&w.length>3&&WORDSET.has(w.slice(0,-3)+'y')) return true;
  if(w.endsWith('ied')&&w.length>3&&WORDSET.has(w.slice(0,-3)+'y')) return true;
  if(w.endsWith('ing')&&w.length>4){s=w.slice(0,-3);if(WORDSET.has(s)||WORDSET.has(s+'e'))return true;if(s.length>1&&s[s.length-1]===s[s.length-2]&&WORDSET.has(s.slice(0,-1)))return true;}
  if(w.endsWith('ed')&&w.length>3){s=w.slice(0,-2);if(WORDSET.has(s)||WORDSET.has(s+'e'))return true;if(s.length>1&&s[s.length-1]===s[s.length-2]&&WORDSET.has(s.slice(0,-1)))return true;}
  if(w.endsWith('es')&&w.length>3&&WORDSET.has(w.slice(0,-2))) return true;
  if(w.endsWith('s')&&w.length>2&&WORDSET.has(w.slice(0,-1))) return true;
  if(w.endsWith('ly')&&w.length>3&&WORDSET.has(w.slice(0,-2))) return true;
  if(w.endsWith('ness')&&w.length>5&&WORDSET.has(w.slice(0,-4))) return true;
  if(w.endsWith('ment')&&w.length>5&&WORDSET.has(w.slice(0,-4))) return true;
  if(w.endsWith('er')&&w.length>3){s=w.slice(0,-2);if(WORDSET.has(s)||WORDSET.has(s+'e'))return true;}
  if(w.endsWith('est')&&w.length>4){s=w.slice(0,-3);if(WORDSET.has(s)||WORDSET.has(s+'e'))return true;}
  return false;
}
if(typeof module!=='undefined'){module.exports={lookupIsWord:lookupIsWord,BLOCKED:BLOCKED,setWords:function(s){WORDSET=s;}};}
