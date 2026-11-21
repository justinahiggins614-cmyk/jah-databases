
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function seededShuffle(arr,rnd){var a=arr.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}

/* Seeded password generator: deterministic, for sharing one set with a class.
   The live tool on the service site uses the browser's own random source;
   this generator uses a seeded source instead, so the same seed always
   makes the same set. Outputs are labeled generated. */
var PW_LOWER='abcdefghijklmnopqrstuvwxyz';
var PW_UPPER='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var PW_DIGITS='0123456789';
var PW_MARKS='!#$%&*+-=?@^_~';
function makePasswords(seed, count, length, opts){
  opts=opts||{lower:true,upper:true,digits:true,marks:true};
  var rnd=mulberry32(seed);
  var sets=[];
  if(opts.lower) sets.push(PW_LOWER);
  if(opts.upper) sets.push(PW_UPPER);
  if(opts.digits) sets.push(PW_DIGITS);
  if(opts.marks) sets.push(PW_MARKS);
  var pool=sets.join('');
  var out=[];
  for(var k=0;k<count;k++){
    var chars=[];
    for(var s=0;s<sets.length;s++) chars.push(sets[s][Math.floor(rnd()*sets[s].length)]);
    while(chars.length<length) chars.push(pool[Math.floor(rnd()*pool.length)]);
    chars=seededShuffle(chars,rnd);
    out.push({n:k+1, password:chars.join(''), length:length});
  }
  return {seed:seed, count:out.length, length:length, items:out};
}
function makePassphrases(words, seed, count, nwords){
  var rnd=mulberry32(seed);
  var out=[];
  for(var k=0;k<count;k++){
    var picked=[];
    for(var w=0;w<nwords;w++) picked.push(words[Math.floor(rnd()*words.length)]);
    out.push({n:k+1, passphrase:picked.join('-')});
  }
  return {seed:seed, count:out.length, items:out};
}
if(typeof module!=='undefined'){module.exports={makePasswords:makePasswords,makePassphrases:makePassphrases,mulberry32:mulberry32,seededShuffle:seededShuffle};}
