(function(){'use strict';
/* JAH The Palindrome Playground Signature Generator Database — REAL generator — "jahdb-gen-palindrome-playground-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Every run produces a genuine,
   fully-formed new item — never a structural sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function fill(t,slots,s){var out=t;Object.keys(slots).forEach(function(k){out=out.split('{'+k+'}').join(pick(slots[k],s));});return out;}
function pyDemo(title,text){
  var t=String(text).replace(/\\/g,'\\\\').replace(/"""/g,'\\"\\"\\"');
  var h=String(title).replace(/[\r\n]+/g,' ').slice(0,120);
  return '# '+h+'\n# Property of Justin Addam Higgins (JAH).\n'
    + 'ITEM = """'+t+'"""\n'
    + 'print(ITEM)\n'
    + 'assert len(ITEM) > 40, "empty generated item"\n'
    + 'assert "{" not in ITEM, "unfilled slot in generated item"\n'
    + 'print("generated_chars=%d" % len(ITEM))\n'
    + 'print("DEMO OK")\n';
}
var PREFIX="JAH-PALPLAS-";
var SRC="signature";
var RECORD_KIND="palindrome playground record";

var FIELDS=["Word Palindromes","Phrase Palindromes","Palindrome Builder","Name Palindromes"];
var WORDS=["racecar", "level", "rotor", "civic", "kayak", "madam", "refer", "rotator", "deified", "repaper", "reviver", "stats", "solos", "tenet", "radar", "minim", "redder", "noon", "peep", "wow", "anna", "otto", "hannah", "redivider", "detartrated", "malayalam", "aibohphobia", "tattarrattat"];
var PHRASES=["A man, a plan, a canal: Panama", "Was it a car or a cat I saw", "Never odd or even", "Do geese see God", "Madam, in Eden, I'm Adam", "Able was I ere I saw Elba", "Go hang a salami, I'm a lasagna hog", "A Toyota's a Toyota", "Borrow or rob", "Don't nod", "Live on time, emit no evil", "Mr. Owl ate my metal worm", "No lemon, no melon", "Pull up if I pull up", "Rise to vote, sir", "Step on no pets", "Taco cat", "Too bad I hid a boot", "Was it a bat I saw", "Yo, banana boy", "Some men interpret nine memos", "Evil is a name of a foeman, as I live"];
var NAMES=["Anna", "Otto", "Hannah", "Bob", "Ava", "Eve", "Ada", "Asa", "Elle", "Ewe", "Halah", "Renner", "Nayan", "Navan", "Sahas"];
var BUILD_A=["step","live","star","draw","loop","part","straw","diaper","reward","dennis"];
var BUILD_B=["on","it","up","at","in","so"];
function letters(s){return s.toLowerCase().replace(/[^a-z]/g,'');}
function isPal(s){var l=letters(s);return l===l.split('').reverse().join('')&&l.length>2;}
function rev(w){return w.split('').reverse().join('');}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var title,body,proof;
  if(field==="Word Palindromes"){
    var w=pick(WORDS,rnd);
    if(!isPal(w))throw new Error('pool word failed palindrome check: '+w);
    title='Palindrome word: "'+w+'"';
    proof='Letters "'+letters(w)+'" reversed are "'+letters(w).split('').reverse().join('')+'" — identical.';
    body='The word "'+w+'" reads the same forward and backward. '+proof+' It has '+w.length+' letters. Say it aloud forward, then backward: it never changes. Word palindromes like this one are the building blocks of the playground — collect them, then combine them into phrases.';
  }else if(field==="Phrase Palindromes"){
    var p=pick(PHRASES,rnd);
    if(!isPal(p))throw new Error('pool phrase failed palindrome check: '+p);
    title='Palindrome phrase: "'+p+'"';
    proof='Stripped to letters, "'+letters(p)+'" reversed is identical — a true phrase palindrome.';
    body='"'+p+'" is a genuine phrase palindrome. '+proof+' ('+letters(p).length+' letters.) Phrase palindromes ignore spaces, punctuation, and capitalization; only the letter order matters. Try writing it backward yourself to feel the symmetry.';
  }else if(field==="Name Palindromes"){
    var n=pick(NAMES,rnd);
    if(!isPal(n))throw new Error('pool name failed palindrome check: '+n);
    title='Palindrome name: "'+n+'"';
    proof='Letters "'+letters(n)+'" reversed are identical.';
    body='"'+n+'" is a palindrome name. '+proof+' Palindrome names are favorites for characters, pets, and pen names — the same forward and backward, like the person wearing it two ways at once.';
  }else{
    var a=pick(BUILD_A,rnd),b=pick(BUILD_B,rnd);
    var phrase=a+' '+b+' '+rev(b)+' '+rev(a);
    if(!isPal(phrase))throw new Error('builder produced non-palindrome: '+phrase);
    title='Built palindrome: "'+phrase+'"';
    proof='Construction: "'+a+'" + "'+b+'" + reverse("'+b+'")="'+rev(b)+'" + reverse("'+a+'")="'+rev(a)+'". Letters "'+letters(phrase)+'" reversed are identical — guaranteed by the mirror construction.';
    body='Fresh-built palindrome: "'+phrase+'". '+proof+' The Palindrome Builder mirrors any two words around a center: A + B + reverse(B) + reverse(A) always reads the same backward. ('+letters(phrase).length+' letters.) Swap in your own words and the mirror still holds — that is the whole trick, and now it is yours.';
  }
  var desc='NEW PALINDROME (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated palindrome — machine-verified to read the same backward. Seeded archive records are the authoritative entries.',
    demo:{kind:'palindrome-verified',language:'python',program:pyDemo(title,desc),note:'Verified palindrome; demo prints the generated item.'},
    _seed:seed
  };
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.description||r.description.length<40)e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-palindrome-playground-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-palindrome-playground-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
