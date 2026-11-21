
/* PURE TOOL FUNCTIONS — the page's own working tool, tested in Node. */
var PW_LOWER='abcdefghijklmnopqrstuvwxyz';
var PW_UPPER='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var PW_DIGITS='0123456789';
var PW_MARKS='!#$%&*+-=?@^_~';
function secureRandomByte(){
  var a=new Uint32Array(1);
  crypto.getRandomValues(a);
  return a[0]/4294967296;
}
function generatePassword(length, opts, rand){
  rand=rand||secureRandomByte;
  var sets=[];
  if(opts.lower) sets.push(PW_LOWER);
  if(opts.upper) sets.push(PW_UPPER);
  if(opts.digits) sets.push(PW_DIGITS);
  if(opts.marks) sets.push(PW_MARKS);
  if(!sets.length) throw new Error('Pick at least one set of letters.');
  if(length<sets.length) throw new Error('Length must be at least the number of sets picked.');
  var pool=sets.join('');
  var chars=[];
  sets.forEach(function(s){ chars.push(s[Math.floor(rand()*s.length)]); });
  while(chars.length<length){ chars.push(pool[Math.floor(rand()*pool.length)]); }
  for(var i=chars.length-1;i>0;i--){ var j=Math.floor(rand()*(i+1)); var t=chars[i]; chars[i]=chars[j]; chars[j]=t; }
  return chars.join('');
}
function strengthBits(length, poolSize){ return length*(Math.log(poolSize)/Math.log(2)); }
function strengthLabel(bits){
  if(bits<40) return 'weak';
  if(bits<60) return 'fair';
  if(bits<90) return 'strong';
  return 'very strong';
}
function generatePassphrase(words, count, rand){
  rand=rand||secureRandomByte;
  var out=[];
  for(var i=0;i<count;i++){ out.push(words[Math.floor(rand()*words.length)]); }
  return out.join(' ');
}
function makePin(digits, rand){
  rand=rand||secureRandomByte;
  var out='';
  for(var i=0;i<digits;i++){ out+=String(Math.floor(rand()*10)); }
  return out;
}


if(typeof module!=='undefined'){module.exports={secureRandomByte: secureRandomByte, generatePassword: generatePassword, strengthBits: strengthBits, strengthLabel: strengthLabel, generatePassphrase: generatePassphrase, makePin: makePin};}
