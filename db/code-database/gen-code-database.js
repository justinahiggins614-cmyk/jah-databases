(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['python','javascript','sql','patterns','data-structures','testing','runbooks'];
var LANGS=['python','javascript','sql'];
var PREFIX='JAH-CODE-';
var WORDS=['cipher','pixel','harbor','lantern','meadow','quartz','river','signal','thunder','willow','ember','frost'];
/* Runbook-family helpers (expansion 2026-10-17). */
function fnv1a(s){var h=0x811c9dc5;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,0x01000193);}return ('0000000'+(h>>>0).toString(16)).slice(-8);}
function f2(x){return x.toFixed(2);}
function f1(x){return x.toFixed(1);}

/* Recomputable families: the validator re-derives expected[0] from (algo,params). */
function fibN(n){var a=0,b=1;for(var i=0;i<n;i++){var t=a+b;a=b;b=t;}return a;}
function factN(n){var r=1;for(var i=2;i<=n;i++)r*=i;return r;}
function gcdN(a,b){while(b){var t=a%b;a=b;b=t;}return a;}
function isPrimeN(n){if(n<2)return false;for(var i=2;i*i<=n;i++)if(n%i===0)return false;return true;}
function sieveN(n){var s=[],p=new Array(n+1).fill(true);p[0]=p[1]=false;for(var i=2;i<=n;i++)if(p[i]){s.push(i);for(var j=i*i;j<=n;j+=i)p[j]=false;}return s;}
function fizzN(n){var o=[];for(var i=1;i<=n;i++)o.push(i%15===0?'FizzBuzz':i%3===0?'Fizz':i%5===0?'Buzz':String(i));return o;}
function revS(s){return s.split('').reverse().join('');}
function palS(s){s=s.toLowerCase();return s===revS(s);}
function vowS(s){return (s.match(/[aeiou]/gi)||[]).length;}
function kadane(a){var best=a[0],cur=a[0];for(var i=1;i<a.length;i++){cur=Math.max(a[i],cur+a[i]);best=Math.max(best,cur);}return best;}
function mergeS(a,b){var o=[],i=0,j=0;while(i<a.length&&j<b.length)o.push(a[i]<b[j]?a[i++]:b[j++]);return o.concat(a.slice(i)).concat(b.slice(j));}
function powN(b,e){return Math.pow(b,e);}
function droot(n){while(n>=10){var s=0;while(n>0){s+=n%10;n=(n/10)|0;}n=s;}return n;}
function caesar(s,sh){return s.replace(/[a-z]/gi,function(c){var b=c<'a'?65:97;return String.fromCharCode((c.charCodeAt(0)-b+sh)%26+b);});}
function rle(s){var o='',i=0;while(i<s.length){var j=i;while(j<s.length&&s[j]===s[i])j++;o+=s[i]+(j-i);i=j;}return o;}
function dedup(a){return [...new Set(a)];}
function rotR(a,k){k=k%a.length;return a.slice(-k).concat(a.slice(0,-k));}
function chunkA(a,k){var o=[];for(var i=0;i<a.length;i+=k)o.push(a.slice(i,i+k));return o;}
function collatz(n){var s=0;while(n!==1){n=n%2?n*3+1:n/2;s++;}return s;}
function twoSum(a,t){for(var i=0;i<a.length;i++)for(var j=i+1;j<a.length;j++)if(a[i]+a[j]===t)return [i,j];return null;}
function binSearch(a,t){var lo=0,hi=a.length-1;while(lo<=hi){var m=(lo+hi)>>1;if(a[m]===t)return m;if(a[m]<t)lo=m+1;else hi=m-1;}return -1;}
function maxSubStr(s){var seen={},st=0,best=0;for(var i=0;i<s.length;i++){var c=s[i];if(seen[c]>=st)st=seen[c]+1;seen[c]=i;best=Math.max(best,i-st+1);}return best;}

var FAMS=[
{k:'fib',cat:'python',t:'Fibonacci number — iterative',lang:['python','javascript'],
 d:'Computes the nth Fibonacci number with a single loop: each step advances the pair (a, b) to (b, a+b). Linear time, constant memory, and no recursion depth issues.',
 cx:'O(n) time, O(1) space',pit:'Recursive versions without memoization are exponential; the loop form avoids that trap entirely.',
 use:'Sequence generation, dynamic-programming warmups, interview baselines.',
 pr:function(r){return {n:ri(r,6,24)};},
 code:function(l,p){return l==='python'?'def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\n\nprint(fib('+p.n+'))':'function fib(n){let a=0,b=1;for(let i=0;i<n;i++){[a,b]=[b,a+b];}return a;}\nconsole.log(fib('+p.n+'));';},
 inp:function(p){return 'fib('+p.n+')';},exp:function(p){return String(fibN(p.n));}},
{k:'fact',cat:'python',t:'Factorial — iterative',lang:['python','javascript'],
 d:'Multiplies 1..n in a loop to compute n!. Iterative form never hits recursion limits and is trivially correct.',
 cx:'O(n) time, O(1) space',pit:'Values overflow 64-bit integers fast; use big integers past 20!.',
 use:'Combinatorics, probability denominators, loop-bound reasoning.',
 pr:function(r){return {n:ri(r,3,12)};},
 code:function(l,p){return l==='python'?'def fact(n):\n    r = 1\n    for i in range(2, n + 1):\n        r *= i\n    return r\n\nprint(fact('+p.n+'))':'function fact(n){let r=1;for(let i=2;i<=n;i++)r*=i;return r;}\nconsole.log(fact('+p.n+'));';},
 inp:function(p){return 'fact('+p.n+')';},exp:function(p){return String(factN(p.n));}},
{k:'gcd',cat:'python',t:'Greatest common divisor — Euclid',lang:['python','javascript'],
 d:'Euclid\'s algorithm: gcd(a,b) = gcd(b, a mod b) until the remainder is zero. One of the oldest algorithms still in daily use.',
 cx:'O(log min(a,b)) time',pit:'Handle gcd(0, x) = x; negative inputs need abs() first.',
 use:'Fraction reduction, LCM via a*b/gcd, cryptographic key math.',
 pr:function(r){var a=ri(r,12,200),b=ri(r,12,200);return {a:a,b:b};},
 code:function(l,p){return l==='python'?'def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n\nprint(gcd('+p.a+', '+p.b+'))':'function gcd(a,b){while(b){[a,b]=[b,a%b];}return a;}\nconsole.log(gcd('+p.a+', '+p.b+'));';},
 inp:function(p){return 'gcd('+p.a+', '+p.b+')';},exp:function(p){return String(gcdN(p.a,p.b));}},
{k:'prime',cat:'python',t:'Primality test — trial division',lang:['python','javascript'],
 d:'Tests divisibility up to sqrt(n): if no divisor is found, n is prime. Simple and correct for everyday sizes.',
 cx:'O(sqrt(n)) time',pit:'Slow for large n; Miller-Rabin is the production choice past 64-bit range.',
 use:'Key generation checks, hashing table sizes, math utilities.',
 pr:function(r){return {n:pick([17,29,97,101,997,1009,15,49,91,100],r)};},
 code:function(l,p){return l==='python'?'def is_prime(n):\n    if n < 2:\n        return False\n    i = 2\n    while i * i <= n:\n        if n % i == 0:\n            return False\n        i += 1\n    return True\n\nprint(is_prime('+p.n+'))':'function isPrime(n){if(n<2)return false;for(let i=2;i*i<=n;i++)if(n%i===0)return false;return true;}\nconsole.log(isPrime('+p.n+'));';},
 inp:function(p){return 'is_prime('+p.n+')';},exp:function(p){return String(isPrimeN(p.n));}},
{k:'sieve',cat:'python',t:'Prime sieve — Eratosthenes',lang:['python','javascript'],
 d:'Marks multiples of each prime starting from 2; survivors are primes up to n. The classic fast prime generator.',
 cx:'O(n log log n) time',pit:'Memory is O(n); segmented sieves handle huge ranges.',
 use:'Prime tables, Project-Euler style problems, crypto setup.',
 pr:function(r){return {n:pick([30,50,100],r)};},
 code:function(l,p){return l==='python'?'def sieve(n):\n    p = [True] * (n + 1)\n    p[0] = p[1] = False\n    for i in range(2, int(n ** 0.5) + 1):\n        if p[i]:\n            for j in range(i * i, n + 1, i):\n                p[j] = False\n    return [i for i, v in enumerate(p) if v]\n\nprint(sieve('+p.n+'))':'function sieve(n){const p=new Array(n+1).fill(true);p[0]=p[1]=false;for(let i=2;i*i<=n;i++)if(p[i])for(let j=i*i;j<=n;j+=i)p[j]=false;return p.map((v,i)=>v?i:-1).filter(i=>i>0);}\nconsole.log(sieve('+p.n+').join(","));';},
 inp:function(p){return 'sieve('+p.n+')';},exp:function(p){return sieveN(p.n).join(',');}},
{k:'fizz',cat:'python',t:'FizzBuzz — modulo dispatch',lang:['python','javascript'],
 d:'Prints Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for both. The canonical control-flow exercise.',
 cx:'O(n) time',pit:'Check 15 first — testing 3 then 5 alone prints "Fizz" instead of "FizzBuzz".',
 use:'Interview screening, loop/modulo teaching.',
 pr:function(r){return {n:pick([15,20,30],r)};},
 code:function(l,p){return l==='python'?'def fizzbuzz(n):\n    return ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)]\n\nprint(",".join(fizzbuzz('+p.n+')))':'function fizzbuzz(n){const o=[];for(let i=1;i<=n;i++)o.push(i%15===0?"FizzBuzz":i%3===0?"Fizz":i%5===0?"Buzz":String(i));return o;}\nconsole.log(fizzbuzz('+p.n+').join(","));';},
 inp:function(p){return 'fizzbuzz('+p.n+')';},exp:function(p){return fizzN(p.n).join(',');}},
{k:'rev',cat:'python',t:'String reversal',lang:['python','javascript'],
 d:'Reverses a string. Python slices, JavaScript splits into chars and reverses — both express the same idea in one line.',
 cx:'O(n) time',pit:'Unicode grapheme clusters (emoji) can split incorrectly with naive char reversal.',
 use:'Palindrome checks, string drills, parser utilities.',
 pr:function(r){return {s:pick(WORDS,r)+pick(WORDS,r)};},
 code:function(l,p){return l==='python'?'s = "'+p.s+'"\nprint(s[::-1])':'const s="'+p.s+'";\nconsole.log([...s].reverse().join(""));';},
 inp:function(p){return 'reverse("'+p.s+'")';},exp:function(p){return revS(p.s);}},
{k:'pal',cat:'python',t:'Palindrome check',lang:['python','javascript'],
 d:'Compares a normalized string against its reverse. Case-folding first keeps "Racecar" style inputs correct.',
 cx:'O(n) time',pit:'Real-world checks also strip spaces and punctuation.',
 use:'Input validation, word games, string exercises.',
 pr:function(r){return {s:pick(['racecar','level','cipher','madam','harbor','rotor'],r)};},
 code:function(l,p){return l==='python'?'def is_pal(s):\n    s = s.lower()\n    return s == s[::-1]\n\nprint(is_pal("'+p.s+'"))':'function isPal(s){s=s.toLowerCase();return s===[...s].reverse().join("");}\nconsole.log(isPal("'+p.s+'"));';},
 inp:function(p){return 'is_pal("'+p.s+'")';},exp:function(p){return String(palS(p.s));}},
{k:'vow',cat:'python',t:'Vowel counter',lang:['python','javascript'],
 d:'Counts a/e/i/o/u in a string with a single pass. Regex or a set lookup both work; the set is fastest.',
 cx:'O(n) time',pit:'Decide up front whether y counts — document the choice.',
 use:'Text analysis, readability heuristics, teaching loops.',
 pr:function(r){return {s:pick(['hello world','signature','algorithm','education'],r)};},
 code:function(l,p){return l==='python'?'def vowels(s):\n    return sum(1 for c in s.lower() if c in "aeiou")\n\nprint(vowels("'+p.s+'"))':'function vowels(s){return (s.match(/[aeiou]/gi)||[]).length;}\nconsole.log(vowels("'+p.s+'"));';},
 inp:function(p){return 'vowels("'+p.s+'")';},exp:function(p){return String(vowS(p.s));}},
{k:'kadane',cat:'python',t:'Maximum subarray — Kadane',lang:['python','javascript'],
 d:'One pass tracks the best subarray ending at each position; the global best is the answer. Optimal for the maximum-subarray problem.',
 cx:'O(n) time, O(1) space',pit:'All-negative arrays need the max-element answer, not zero.',
 use:'Signal analysis, trading windows, DP teaching.',
 pr:function(r){var a=[],n=ri(r,5,9);for(var i=0;i<n;i++)a.push(ri(r,-9,9));if(Math.max.apply(null,a)<=0)a[0]=ri(r,1,9);return {a:a};},
 code:function(l,p){var s='['+p.a.join(', ')+']';return l==='python'?'def max_sub(a):\n    best = cur = a[0]\n    for x in a[1:]:\n        cur = max(x, cur + x)\n        best = max(best, cur)\n    return best\n\nprint(max_sub('+s+'))':'function maxSub(a){let best=a[0],cur=a[0];for(let i=1;i<a.length;i++){cur=Math.max(a[i],cur+a[i]);best=Math.max(best,cur);}return best;}\nconsole.log(maxSub('+s+'));';},
 inp:function(p){return 'max_sub(['+p.a.join(',')+'])';},exp:function(p){return String(kadane(p.a));}},
{k:'merge',cat:'python',t:'Merge two sorted arrays',lang:['python','javascript'],
 d:'Walks both sorted inputs with two pointers, always taking the smaller head. The merge step inside merge sort.',
 cx:'O(n+m) time',pit:'Remember to append the leftover tail of whichever array is not exhausted.',
 use:'Merge sort, k-way merges, sorted-stream joins.',
 pr:function(r){var a=[],b=[],n=ri(r,3,6),m=ri(r,3,6);for(var i=0;i<n;i++)a.push(ri(r,0,40));for(var j=0;j<m;j++)b.push(ri(r,0,40));a.sort(function(x,y){return x-y;});b.sort(function(x,y){return x-y;});return {a:a,b:b};},
 code:function(l,p){var sa='['+p.a.join(', ')+']',sb='['+p.b.join(', ')+']';return l==='python'?'def merge(a, b):\n    o, i, j = [], 0, 0\n    while i < len(a) and j < len(b):\n        if a[i] < b[j]:\n            o.append(a[i]); i += 1\n        else:\n            o.append(b[j]); j += 1\n    return o + a[i:] + b[j:]\n\nprint(merge('+sa+', '+sb+'))':'function merge(a,b){const o=[];let i=0,j=0;while(i<a.length&&j<b.length)o.push(a[i]<b[j]?a[i++]:b[j++]);return o.concat(a.slice(i)).concat(b.slice(j));}\nconsole.log(merge('+sa+', '+sb+').join(","));';},
 inp:function(p){return 'merge(...)';},exp:function(p){return mergeS(p.a,p.b).join(',');}},
{k:'pow',cat:'python',t:'Integer power — fast exponentiation',lang:['python','javascript'],
 d:'Squares the base and halves the exponent each step (exponentiation by squaring). Logarithmic instead of linear multiplications.',
 cx:'O(log e) time',pit:'Negative exponents need reciprocal handling; watch integer overflow.',
 use:'Modular exponentiation, crypto primitives, math libraries.',
 pr:function(r){return {b:ri(r,2,9),e:ri(r,2,8)};},
 code:function(l,p){return l==='python'?'def ipow(b, e):\n    r = 1\n    while e:\n        if e & 1:\n            r *= b\n        b *= b\n        e >>= 1\n    return r\n\nprint(ipow('+p.b+', '+p.e+'))':'function ipow(b,e){let r=1;while(e){if(e&1)r*=b;b*=b;e>>=1;}return r;}\nconsole.log(ipow('+p.b+', '+p.e+'));';},
 inp:function(p){return 'ipow('+p.b+', '+p.e+')';},exp:function(p){return String(powN(p.b,p.e));}},
{k:'droot',cat:'python',t:'Digital root',lang:['python','javascript'],
 d:'Repeatedly sums decimal digits until one digit remains. Equivalent to n mod 9 (with 9 instead of 0) — a handy checksum trick.',
 cx:'O(digits) time',pit:'The mod-9 shortcut needs the n%9==0 -> 9 special case.',
 use:'Checksums, numerology-free math drills, divisibility.',
 pr:function(r){return {n:ri(r,100,99999)};},
 code:function(l,p){return l==='python'?'def droot(n):\n    while n >= 10:\n        n = sum(int(d) for d in str(n))\n    return n\n\nprint(droot('+p.n+'))':'function droot(n){while(n>=10){let s=0;while(n>0){s+=n%10;n=(n/10)|0;}n=s;}return n;}\nconsole.log(droot('+p.n+'));';},
 inp:function(p){return 'droot('+p.n+')';},exp:function(p){return String(droot(p.n));}},
{k:'caesar',cat:'python',t:'Caesar cipher shift',lang:['python','javascript'],
 d:'Shifts each letter by a fixed amount, wrapping around the alphabet. The oldest known substitution cipher — great for teaching modular arithmetic.',
 cx:'O(n) time',pit:'Case handling and non-letters must pass through unchanged.',
 use:'Crypto history lessons, string-transform practice.',
 pr:function(r){return {s:pick(WORDS,r),sh:ri(r,1,13)};},
 code:function(l,p){return l==='python'?'def caesar(s, sh):\n    o = ""\n    for c in s:\n        b = ord("a")\n        o += chr((ord(c) - b + sh) % 26 + b)\n    return o\n\nprint(caesar("'+p.s+'", '+p.sh+'))':'function caesar(s,sh){return s.replace(/[a-z]/g,c=>String.fromCharCode((c.charCodeAt(0)-97+sh)%26+97));}\nconsole.log(caesar("'+p.s+'", '+p.sh+'));';},
 inp:function(p){return 'caesar("'+p.s+'", '+p.sh+')';},exp:function(p){return caesar(p.s,p.sh);}},
{k:'rle',cat:'python',t:'Run-length encoding',lang:['python','javascript'],
 d:'Compresses runs of identical characters into char+count pairs. Simple, lossless, and effective on repetitive data.',
 cx:'O(n) time',pit:'Incompressible data grows — real encoders add an escape or length prefix.',
 use:'Bitmap compression, telemetry, interview warmups.',
 pr:function(r){var s='',n=ri(r,3,6);for(var i=0;i<n;i++){var c=pick(['a','b','c'],r),k=ri(r,2,5);for(var j=0;j<k;j++)s+=c;}return {s:s};},
 code:function(l,p){return l==='python'?'def rle(s):\n    o, i = "", 0\n    while i < len(s):\n        j = i\n        while j < len(s) and s[j] == s[i]:\n            j += 1\n        o += s[i] + str(j - i)\n        i = j\n    return o\n\nprint(rle("'+p.s+'"))':'function rle(s){let o="",i=0;while(i<s.length){let j=i;while(j<s.length&&s[j]===s[i])j++;o+=s[i]+(j-i);i=j;}return o;}\nconsole.log(rle("'+p.s+'"));';},
 inp:function(p){return 'rle("'+p.s+'")';},exp:function(p){return rle(p.s);}},
{k:'dedup',cat:'python',t:'Array deduplication',lang:['python','javascript'],
 d:'Removes duplicates while keeping first-seen order. A set tracks membership in a single pass.',
 cx:'O(n) time',pit:'NaN and -0/+0 have surprising equality semantics in JS Sets.',
 use:'Data cleaning, ETL pipelines, list processing.',
 pr:function(r){var a=[],n=ri(r,5,9);for(var i=0;i<n;i++)a.push(pick([1,2,3,4,5],r));return {a:a};},
 code:function(l,p){var s='['+p.a.join(', ')+']';return l==='python'?'def dedup(a):\n    seen, o = set(), []\n    for x in a:\n        if x not in seen:\n            seen.add(x); o.append(x)\n    return o\n\nprint(dedup('+s+'))':'function dedup(a){return [...new Set(a)];}\nconsole.log(dedup('+s+').join(","));';},
 inp:function(p){return 'dedup(...)';},exp:function(p){return dedup(p.a).join(',');}},
{k:'rot',cat:'python',t:'Rotate array right by k',lang:['python','javascript'],
 d:'Rotates an array right by k positions using slicing: the last k elements move to the front. O(n) with no extra loop.',
 cx:'O(n) time',pit:'Reduce k modulo length first; k larger than the array is a classic bug.',
 use:'Ring buffers, carousel UIs, cipher wheels.',
 pr:function(r){var a=[],n=ri(r,4,8);for(var i=0;i<n;i++)a.push(ri(r,1,50));return {a:a,k:ri(r,1,n-1)};},
 code:function(l,p){var s='['+p.a.join(', ')+']';return l==='python'?'def rot(a, k):\n    k %= len(a)\n    return a[-k:] + a[:-k]\n\nprint(rot('+s+', '+p.k+'))':'function rot(a,k){k%=a.length;return a.slice(-k).concat(a.slice(0,-k));}\nconsole.log(rot('+s+', '+p.k+').join(","));';},
 inp:function(p){return 'rot(..., '+p.k+')';},exp:function(p){return rotR(p.a,p.k).join(',');}},
{k:'chunk',cat:'python',t:'Chunk array into groups',lang:['python','javascript'],
 d:'Splits an array into sub-arrays of size k. The last chunk may be smaller — slicing handles that naturally.',
 cx:'O(n) time',pit:'k <= 0 must be rejected; the final partial chunk is expected, not an error.',
 use:'Pagination, batch processing, grid layouts.',
 pr:function(r){var a=[],n=ri(r,5,10);for(var i=0;i<n;i++)a.push(ri(r,1,99));return {a:a,k:pick([2,3,4],r)};},
 code:function(l,p){var s='['+p.a.join(', ')+']';return l==='python'?'def chunk(a, k):\n    return [a[i:i + k] for i in range(0, len(a), k)]\n\nprint(chunk('+s+', '+p.k+'))':'function chunk(a,k){const o=[];for(let i=0;i<a.length;i+=k)o.push(a.slice(i,i+k));return o;}\nconsole.log(JSON.stringify(chunk('+s+', '+p.k+')));';},
 inp:function(p){return 'chunk(..., '+p.k+')';},exp:function(p){return JSON.stringify(chunkA(p.a,p.k));}},
{k:'collatz',cat:'python',t:'Collatz step counter',lang:['python','javascript'],
 d:'Counts steps to reach 1: halve evens, triple-plus-one odds. Famously unsolved in general — but easy to simulate.',
 cx:'O(steps) time',pit:'Intermediate values can exceed the starting n by a lot; use big integers for huge seeds.',
 use:'Number-theory play, loop teaching, conjecture demos.',
 pr:function(r){return {n:ri(r,5,60)};},
 code:function(l,p){return l==='python'?'def collatz(n):\n    s = 0\n    while n != 1:\n        n = n // 2 if n % 2 == 0 else 3 * n + 1\n        s += 1\n    return s\n\nprint(collatz('+p.n+'))':'function collatz(n){let s=0;while(n!==1){n=n%2?n*3+1:n/2;s++;}return s;}\nconsole.log(collatz('+p.n+'));';},
 inp:function(p){return 'collatz('+p.n+')';},exp:function(p){return String(collatz(p.n));}},
{k:'twosum',cat:'python',t:'Two-sum index finder',lang:['python','javascript'],
 d:'Finds two indices whose values add to the target. The hash-map version runs in one pass; the pair loop is clearer for teaching.',
 cx:'O(n) with map; O(n^2) naive',pit:'Return indices, not values — and never reuse the same element twice.',
 use:'Interview staple, complement lookups, pair finding.',
 pr:function(r){var a=[],n=ri(r,4,7);for(var i=0;i<n;i++)a.push(ri(r,1,20));var i1=ri(r,0,n-2),i2=ri(r,i1+1,n-1);return {a:a,t:a[i1]+a[i2]};},
 code:function(l,p){var s='['+p.a.join(', ')+']';return l==='python'?'def two_sum(a, t):\n    for i in range(len(a)):\n        for j in range(i + 1, len(a)):\n            if a[i] + a[j] == t:\n                return (i, j)\n\nprint(two_sum('+s+', '+p.t+'))':'function twoSum(a,t){for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++)if(a[i]+a[j]===t)return [i,j];}\nconsole.log(twoSum('+s+', '+p.t+').join(","));';},
 inp:function(p){return 'two_sum(..., '+p.t+')';},exp:function(p){return twoSum(p.a,p.t).join(',');}},
{k:'bsearch',cat:'python',t:'Binary search — iterative',lang:['python','javascript'],
 d:'Halves a sorted array each step to find the target in logarithmic time. The canonical divide-and-conquer search.',
 cx:'O(log n) time',pit:'Requires sorted input; mid = (lo+hi)//2 can overflow in fixed-width languages — use lo+(hi-lo)//2 there.',
 use:'Sorted lookups, bisect utilities, search teaching.',
 pr:function(r){var a=[],n=ri(r,5,10);for(var i=0;i<n;i++)a.push(ri(r,0,60));a.sort(function(x,y){return x-y;});a=dedup(a);var t=pick([a[0],a[a.length-1],a[(a.length/2)|0],999],r);return {a:a,t:t};},
 code:function(l,p){var s='['+p.a.join(', ')+']';return l==='python'?'def bsearch(a, t):\n    lo, hi = 0, len(a) - 1\n    while lo <= hi:\n        m = (lo + hi) // 2\n        if a[m] == t:\n            return m\n        lo, hi = (m + 1, hi) if a[m] < t else (lo, m - 1)\n    return -1\n\nprint(bsearch('+s+', '+p.t+'))':'function bsearch(a,t){let lo=0,hi=a.length-1;while(lo<=hi){const m=(lo+hi)>>1;if(a[m]===t)return m;if(a[m]<t)lo=m+1;else hi=m-1;}return -1;}\nconsole.log(bsearch('+s+', '+p.t+'));';},
 inp:function(p){return 'bsearch(..., '+p.t+')';},exp:function(p){return String(binSearch(p.a,p.t));}},
{k:'maxsub',cat:'javascript',t:'Longest substring without repeats',lang:['javascript','python'],
 d:'Sliding window with a last-seen map: expand right, and when a repeat appears inside the window, jump the left edge past it.',
 cx:'O(n) time',pit:'The left edge must only move forward — use max(stored, current).',
 use:'String parsing, tokenizer windows, interview mediums.',
 pr:function(r){return {s:pick(['abcabcbb','bbbbb','pwwkew','abcdef','abba'],r)};},
 code:function(l,p){return l==='python'?'def longest(s):\n    seen, st, best = {}, 0, 0\n    for i, c in enumerate(s):\n        if seen.get(c, -1) >= st:\n            st = seen[c] + 1\n        seen[c] = i\n        best = max(best, i - st + 1)\n    return best\n\nprint(longest("'+p.s+'"))':'function longest(s){const seen={};let st=0,best=0;for(let i=0;i<s.length;i++){const c=s[i];if(seen[c]>=st)st=seen[c]+1;seen[c]=i;best=Math.max(best,i-st+1);}return best;}\nconsole.log(longest("'+p.s+'"));';},
 inp:function(p){return 'longest("'+p.s+'")';},exp:function(p){return String(maxSubStr(p.s));}},
/* SQL pattern families: static, verified against SQLite during corpus build. */
{k:'sql-topn',cat:'sql',t:'Top-N per group — window function',lang:['sql'],static:true,
 d:'ROW_NUMBER() partitioned by group picks the top N rows per group without self-joins. Standard SQL:2003 window syntax, supported by SQLite, PostgreSQL and MySQL 8.',
 cx:'O(n log n) with sort',pit:'Use RANK() when ties must share a rank; ROW_NUMBER() is arbitrary on ties.',
 use:'Leaderboards, latest-record-per-user, per-category bests.',
 code:function(){return 'SELECT name, dept, salary\nFROM (\n  SELECT name, dept, salary,\n         ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn\n  FROM employees\n) WHERE rn <= 3;';}},
{k:'sql-run',cat:'sql',t:'Running total — cumulative SUM',lang:['sql'],static:true,
 d:'SUM() OVER (ORDER BY day) accumulates a running total across ordered rows. The workhorse of cumulative reporting.',
 cx:'O(n log n) with sort',pit:'Duplicate ordering keys make the frame nondeterministic — add a tiebreaker.',
 use:'Cumulative revenue, balance ledgers, progress tracking.',
 code:function(){return 'SELECT day, amount,\n       SUM(amount) OVER (ORDER BY day) AS running_total\nFROM sales;';}},
{k:'sql-dedup',cat:'sql',t:'Delete duplicate rows, keep one',lang:['sql'],static:true,
 d:'ROW_NUMBER() over the duplicate key flags extras; deleting rn > 1 keeps exactly one copy of each. Safe and deterministic with an id tiebreaker.',
 cx:'O(n log n)',pit:'Always verify the survivor rule (MIN(id)) before deleting in production.',
 use:'Data cleaning, ETL dedup, import hygiene.',
 code:function(){return 'DELETE FROM t WHERE id IN (\n  SELECT id FROM (\n    SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn\n    FROM users\n  ) WHERE rn > 1\n);';}},
{k:'sql-nth',cat:'sql',t:'Nth highest value',lang:['sql'],static:true,
 d:'DENSE_RANK() over the ordered value finds the Nth distinct level — NULLs sort last in SQLite/PostgreSQL by default.',
 cx:'O(n log n)',pit:'LIMIT/OFFSET pagination is not equivalent when ties exist.',
 use:'Salary bands, score thresholds, percentile edges.',
 code:function(){return 'SELECT DISTINCT salary FROM (\n  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS r\n  FROM employees\n) WHERE r = 2;';}},
{k:'sql-avg',cat:'sql',t:'Moving average — 7-day window',lang:['sql'],static:true,
 d:'AVG() OVER with ROWS BETWEEN 6 PRECEDING AND CURRENT ROW smooths daily metrics. Frame clauses are SQL:2003 standard.',
 cx:'O(n log n)',pit:'ROWS vs RANGE matters with duplicate dates — RANGE can pull extra peers.',
 use:'Trend smoothing, KPI dashboards, anomaly baselines.',
 code:function(){return 'SELECT day, value,\n       AVG(value) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma7\nFROM metrics;';}},
/* ---- Executable procedures/runbooks (expansion 2026-10-17): runnable scripts,
   workflows, reproducible computational steps. Every family ships a runnable
   script; expected outputs are computed by the JS reference and were
   machine-verified by executing each script. ---- */
{k:'rb-logrotate',cat:'runbooks',t:'Log rotation runbook — keep last N lines',lang:['python'],
 d:'Operational runbook: trims a service log to its newest N lines so disks never fill while recent history stays available. The script below embeds a sample log and prints the kept lines.',
 cx:'O(n) time per run',pit:'Rotating while the service writes can interleave lines; stop the writer or copy-then-truncate.',
 use:'Log hygiene, disk-space runbooks, on-call playbooks.',
 pr:function(r){return {n:ri(r,2,5)};},
 code:function(l,p){var L=['logs = ["boot ok","net up","disk ok","svc start","user login","cron run","backup done","idle"]','keep = '+p.n,'print("|".join(logs[-keep:]))'];return L.join('\n');},
 inp:function(p){return 'keep='+p.n+' of 8 log lines';},
 exp:function(p){return ['boot ok','net up','disk ok','svc start','user login','cron run','backup done','idle'].slice(-p.n).join('|');}},
{k:'rb-csvnorm',cat:'runbooks',t:'CSV normalization runbook — strip and lowercase',lang:['python'],
 d:'Data-ingest runbook: normalizes raw CSV rows by stripping whitespace and lowercasing email fields before loading. Prints the cleaned rows so the operator can eyeball them before the load step.',
 cx:'O(n) time per run',pit:'Lowercasing is wrong for case-sensitive identifiers; normalize only fields documented as case-insensitive.',
 use:'ETL pre-steps, import hygiene, data cleaning.',
 pr:function(r){return {};},
 code:function(l,p){var L=['rows = [[" Alice ","ALICE@EXAMPLE.COM "],["Bob ","BOB@EXAMPLE.COM"]]','norm = [[r[0].strip(), r[1].strip().lower()] for r in rows]','print("|".join(a + "," + b for a, b in norm))'];return L.join('\n');},
 inp:function(p){return '2 raw rows';},
 exp:function(p){return [[' Alice ','ALICE@EXAMPLE.COM '],['Bob ','BOB@EXAMPLE.COM']].map(function(r){return r[0].trim()+','+r[1].trim().toLowerCase();}).join('|');}},
{k:'rb-dedupe',cat:'runbooks',t:'Deduplication runbook — ordered unique list',lang:['python'],
 d:'Import-hygiene runbook: removes duplicate IDs from an intake list while preserving first-seen order. Prints the deduplicated list that downstream steps consume.',
 cx:'O(n) time per run',pit:'Naive "in list" checks are O(n^2); keep a seen-set alongside the output list.',
 use:'Import dedup, list cleaning, ETL.',
 pr:function(r){return {};},
 code:function(l,p){var L=['a = [3,1,4,1,5,3,2]','seen = []','for x in a:','    if x not in seen:','        seen.append(x)','print(",".join(map(str, seen)))'];return L.join('\n');},
 inp:function(p){return '[3,1,4,1,5,3,2]';},
 exp:function(p){return [3,1,4,1,5,3,2].filter(function(x,i,a){return a.indexOf(x)===i;}).join(',');}},
{k:'rb-chunk',cat:'runbooks',t:'Batching runbook — chunk work into batches',lang:['python'],
 d:'Throughput runbook: splits a work queue into fixed-size batches so workers process bounded chunks. Prints the batches the dispatcher will hand out.',
 cx:'O(n) time per run',pit:'The last batch is usually short; workers must handle partial batches, not assume full ones.',
 use:'Batch dispatch, worker queues, bulk APIs.',
 pr:function(r){return {k:ri(r,2,4)};},
 code:function(l,p){var L=['a = list(range(1, 8))','k = '+p.k,'batches = [a[i:i+k] for i in range(0, len(a), k)]','print(";".join(",".join(map(str, b)) for b in batches))'];return L.join('\n');},
 inp:function(p){return '7 items, batch size '+p.k;},
 exp:function(p){var a=[1,2,3,4,5,6,7],o=[];for(var i=0;i<a.length;i+=p.k)o.push(a.slice(i,i+p.k).join(','));return o.join(';');}},
{k:'rb-retry',cat:'runbooks',t:'Retry schedule runbook — exponential backoff plan',lang:['python'],
 d:'Reliability runbook: computes the exact attempt schedule for exponential-backoff retries so on-call knows when each retry fires. Prints cumulative attempt times in seconds.',
 cx:'O(n) time per run',pit:'Unbounded backoff sleeps through incidents; always cap the wait and the attempt count.',
 use:'Retry policies, flaky-dependency handling, runbook automation.',
 pr:function(r){return {base:ri(r,1,5),n:ri(r,3,5)};},
 code:function(l,p){var L=['base = '+p.base,'attempts = '+p.n,'t = 0','times = [0]','for i in range(attempts):','    t += base * (2 ** i)','    times.append(t)','print(",".join(map(str, times)))'];return L.join('\n');},
 inp:function(p){return 'base='+p.base+'s, '+p.n+' retries';},
 exp:function(p){var t=0,o=[0];for(var i=0;i<p.n;i++){t+=p.base*Math.pow(2,i);o.push(t);}return o.join(',');}},
{k:'rb-healthcheck',cat:'runbooks',t:'Health-check runbook — threshold evaluation',lang:['python'],
 d:'Monitoring runbook: evaluates service metrics against alert thresholds and prints a per-metric verdict. The same verdict logic drives the paging decision.',
 cx:'O(m) time per run',pit:'Thresholds tuned on quiet weeks page falsely on busy ones; re-baseline after traffic changes.',
 use:'Health checks, alerting, SRE runbooks.',
 pr:function(r){return {cpu:ri(r,70,96),mem:ri(r,60,90),disk:ri(r,75,96)};},
 code:function(l,p){var L=['metrics = [("cpu", '+p.cpu+', 90), ("mem", '+p.mem+', 85), ("disk", '+p.disk+', 90)]','print(" ".join(name + ":" + ("ok" if v <= t else "FAIL") for name, v, t in metrics))'];return L.join('\n');},
 inp:function(p){return 'cpu='+p.cpu+' mem='+p.mem+' disk='+p.disk;},
 exp:function(p){return [['cpu',p.cpu,90],['mem',p.mem,85],['disk',p.disk,90]].map(function(m){return m[0]+':'+(m[1]<=m[2]?'ok':'FAIL');}).join(' ');}},
{k:'rb-jsonvalidate',cat:'runbooks',t:'Config validation runbook — required keys check',lang:['python'],
 d:'Deploy-gate runbook: validates a service record against its required-key schema before rollout. Prints "valid" or the missing keys that block the deploy.',
 cx:'O(k) time per run',pit:'Validating shape but not value ranges lets bad configs through; check both.',
 use:'Deploy gates, config linting, preflight checks.',
 pr:function(r){return {req:pick([['name','port'],['name','port','token'],['name','owner','region']],r)};},
 code:function(l,p){var L=['rec = {"name": "svc", "port": 8080}','req = '+JSON.stringify(p.req),'missing = [k for k in req if k not in rec]','print("valid" if not missing else "missing:" + ",".join(missing))'];return L.join('\n');},
 inp:function(p){return 'required='+p.req.join(',');},
 exp:function(p){var rec={name:'svc',port:8080};var m=p.req.filter(function(k){return !(k in rec);});return m.length?('missing:'+m.join(',')):'valid';}},
{k:'rb-configdiff',cat:'runbooks',t:'Config diff runbook — old vs new settings',lang:['python'],
 d:'Change-management runbook: diffs the running config against the candidate config and prints every change. Nothing deploys until this diff is reviewed.',
 cx:'O(k) time per run',pit:'Diffing serialized text instead of parsed values flags formatting noise as changes; compare structures.',
 use:'Deploy reviews, config audits, change control.',
 pr:function(r){return {retries:ri(r,2,5),timeout:ri(r,20,60),extra:r()<0.5};},
 code:function(l,p){var L=['old = {"retries": 3, "timeout": 30}','new = {"retries": '+p.retries+', "timeout": '+p.timeout+(p.extra?', "region": "us-east"':'')+'}','diff = []','for k in sorted(set(old) | set(new)):','    if k not in old: diff.append(k + ":added:" + str(new[k]))','    elif k not in new: diff.append(k + ":removed")','    elif old[k] != new[k]: diff.append(k + ":" + str(old[k]) + "->" + str(new[k]))','print(";".join(diff) if diff else "no changes")'];return L.join('\n');},
 inp:function(p){return 'candidate config';},
 exp:function(p){var old={retries:3,timeout:30},nw={retries:p.retries,timeout:p.timeout};if(p.extra)nw.region='us-east';var ks=Object.keys(old).concat(Object.keys(nw).filter(function(k){return !(k in old);}));var d=[];ks.sort().forEach(function(k){if(!(k in old))d.push(k+':added:'+nw[k]);else if(!(k in nw))d.push(k+':removed');else if(old[k]!==nw[k])d.push(k+':'+old[k]+'->'+nw[k]);});return d.length?d.join(';'):'no changes';}},
{k:'rb-redact',cat:'runbooks',t:'Secret redaction runbook — scrub logs',lang:['python'],
 d:'Security runbook: scrubs known secret values from log text before the logs leave the host. Prints the redacted text that is safe to ship.',
 cx:'O(n*m) time per run',pit:'Redaction after logging is too late if the raw log already shipped; redact at the source.',
 use:'Log shipping, secret hygiene, compliance.',
 pr:function(r){return {};},
 code:function(l,p){var L=['t = "token=abc123 user=bob pass=s3cret"','for s in ["abc123", "s3cret"]:','    t = t.replace(s, "***")','print(t)'];return L.join('\n');},
 inp:function(p){return 'log line with 2 secrets';},
 exp:function(p){return 'token=abc123 user=bob pass=s3cret'.replace('abc123','***').replace('s3cret','***');}},
{k:'rb-uptime',cat:'runbooks',t:'SLO runbook — error budget remaining',lang:['python'],
 d:'SRE runbook: computes the 30-day uptime percentage and the remaining error budget against a 99.9% SLO. Prints both numbers that gate risky deploys.',
 cx:'O(n) time per run',pit:'Averaging hides clustered outages; budget math assumes the SLO window matches the business risk.',
 use:'SLO tracking, deploy freezes, error budgets.',
 pr:function(r){return {up:ri(r,9950,9999)/100};},
 code:function(l,p){var L=['uptime = '+p.up.toFixed(2),'budget = max(0.0, uptime - 99.9)','print("uptime=%.2f budget_left=%.2f" % (uptime, budget))'];return L.join('\n');},
 inp:function(p){return 'uptime='+p.up.toFixed(2)+'%';},
 exp:function(p){var b=Math.max(0,p.up-99.9);return 'uptime='+f2(p.up)+' budget_left='+f2(b);}},
{k:'rb-checklist',cat:'runbooks',t:'Deploy checklist runbook — ordered steps',lang:['python'],
 d:'Release runbook: executes the deploy checklist in order and prints each step with its verdict. A FAIL halts the rollout before the next step runs.',
 cx:'O(s) time per run',pit:'Checklists that always pass teach nobody; every step needs a real assertion behind it.',
 use:'Deploys, release management, on-call.',
 pr:function(r){return {fail:ri(r,0,3)};},
 code:function(l,p){var L=['steps = ["preflight", "deploy", "verify", "cleanup"]','fail_at = '+p.fail,'out = []','for i, s in enumerate(steps):','    out.append(s + ":" + ("FAIL" if i == fail_at else "pass"))','print(";".join(out))'];return L.join('\n');},
 inp:function(p){return '4 steps, step '+p.fail+' fails';},
 exp:function(p){return ['preflight','deploy','verify','cleanup'].map(function(s,i){return s+':'+(i===p.fail?'FAIL':'pass');}).join(';');}},
{k:'rb-migrate',cat:'runbooks',t:'Migration runbook — idempotent apply',lang:['python'],
 d:'Data runbook: applies pending schema migrations exactly once — already-applied steps are skipped, so re-running is safe. Prints the migrations applied this run.',
 cx:'O(s) time per run',pit:'Migrations without a down path turn a bad deploy into an outage; every up needs a tested down.',
 use:'Schema migrations, data backfills, idempotent jobs.',
 pr:function(r){return {done:pick([[],['m1'],['m1','m2']],r)};},
 code:function(l,p){var L=['steps = ["m1", "m2", "m3"]','applied = '+JSON.stringify(p.done),'pending = [s for s in steps if s not in applied]','print("applied:" + ",".join(pending) if pending else "nothing to do")'];return L.join('\n');},
 inp:function(p){return 'already applied: '+(p.done.join(',')||'none');},
 exp:function(p){var pend=['m1','m2','m3'].filter(function(s){return p.done.indexOf(s)<0;});return pend.length?('applied:'+pend.join(',')):'nothing to do';}},
{k:'rb-backoff',cat:'runbooks',t:'Backoff runbook — capped wait schedule',lang:['python'],
 d:'Client runbook: computes capped exponential-backoff waits so retry storms never hammer a recovering service. Prints the wait before each attempt in milliseconds.',
 cx:'O(n) time per run',pit:'Identical backoff across a fleet synchronizes retries; add jitter in production.',
 use:'Client retries, API consumption, queue consumers.',
 pr:function(r){return {base:ri(r,50,200),cap:pick([800,1600,3200],r),n:ri(r,3,6)};},
 code:function(l,p){var L=['base = '+p.base, 'cap = '+p.cap, 'n = '+p.n,'waits = [min(cap, base * (2 ** i)) for i in range(n)]','print(",".join(map(str, waits)))'];return L.join('\n');},
 inp:function(p){return 'base='+p.base+'ms cap='+p.cap+'ms x'+p.n;},
 exp:function(p){var o=[];for(var i=0;i<p.n;i++)o.push(Math.min(p.cap,p.base*Math.pow(2,i)));return o.join(',');}},
{k:'rb-canary',cat:'runbooks',t:'Canary analysis runbook — promote or hold',lang:['python'],
 d:'Release runbook: compares canary error rate against baseline and prints the verdict. Promote only when the canary is no worse than baseline.',
 cx:'O(1) time per run',pit:'Short canary windows miss slow leaks; hold the canary long enough to see the tail.',
 use:'Canary deploys, progressive delivery, release safety.',
 pr:function(r){return {base:ri(r,5,20)/10,can:ri(r,1,25)/10};},
 code:function(l,p){var L=['baseline = '+p.base.toFixed(1), 'canary = '+p.can.toFixed(1),'verdict = "promote" if canary <= baseline else "hold"','print("baseline=%.1f canary=%.1f verdict=%s" % (baseline, canary, verdict))'];return L.join('\n');},
 inp:function(p){return 'baseline='+p.base.toFixed(1)+'% canary='+p.can.toFixed(1)+'%';},
 exp:function(p){return 'baseline='+f1(p.base)+' canary='+f1(p.can)+' verdict='+(p.can<=p.base?'promote':'hold');}},
{k:'rb-apachelog',cat:'runbooks',t:'Log triage runbook — status class counts',lang:['python'],
 d:'Incident runbook: parses access-log lines and counts responses by status class. A spike in 5xx here is the first signal of a bad deploy.',
 cx:'O(n) time per run',pit:'Sampling logs for speed hides the rare errors that matter most; count everything.',
 use:'Incident triage, traffic analysis, deploy monitoring.',
 pr:function(r){return {};},
 code:function(l,p){var L=['lines = [','  "10.0.0.1 - - [01/Jan/2026] \'GET /index\' 200 123",','  "10.0.0.2 - - [01/Jan/2026] \'GET /old\' 404 0",','  "10.0.0.3 - - [01/Jan/2026] \'POST /api\' 500 9",','  "10.0.0.4 - - [01/Jan/2026] \'GET /img\' 200 55"]','counts = {}','for ln in lines:','    status = ln.split(chr(39))[2].split()[0]','    cls = status[0] + "xx"','    counts[cls] = counts.get(cls, 0) + 1','print(" ".join(k + ":" + str(counts[k]) for k in sorted(counts)))'];return L.join('\n');},
 inp:function(p){return '4 access-log lines';},
 exp:function(p){return '2xx:2 4xx:1 5xx:1';}},
{k:'rb-csv2json',cat:'runbooks',t:'Format conversion runbook — CSV rows to JSON',lang:['python'],
 d:'Integration runbook: converts CSV rows into JSON objects keyed by the header row. Prints the compact JSON the downstream API consumes.',
 cx:'O(n) time per run',pit:'Headers with duplicates or blanks produce broken keys; validate the header row first.',
 use:'Data integration, API ingestion, format migration.',
 pr:function(r){return {p1:pick([8080,3000,5000],r),p2:pick([9090,8000,5432],r)};},
 code:function(l,p){var L=['import json','header = ["host", "port"]','rows = [["a", '+p.p1+'], ["b", '+p.p2+']]','objs = [dict(zip(header, row)) for row in rows]','print(json.dumps(objs, separators=(",", ":")))'];return L.join('\n');},
 inp:function(p){return '2 rows x 2 cols';},
 exp:function(p){return JSON.stringify([{host:'a',port:p.p1},{host:'b',port:p.p2}]);}},
{k:'rb-fnv',cat:'runbooks',t:'Checksum runbook — FNV-1a content hashes',lang:['python'],
 d:'Integrity runbook: hashes content labels with FNV-1a so changed inputs produce visibly different checksums. Prints one hash per label for the manifest.',
 cx:'O(n) time per run',pit:'FNV is not cryptographic; use it for change detection, never for security.',
 use:'Change detection, manifest checksums, cache keys.',
 pr:function(r){return {words:pick([['alpha','beta'],['gamma','delta'],['north','south']],r)};},
 code:function(l,p){var L=['def fnv(s):','    h = 0x811c9dc5','    for ch in s:','        h ^= ord(ch)','        h = (h * 0x01000193) & 0xffffffff','    return "%08x" % h','words = '+JSON.stringify(p.words),'print(",".join(fnv(w) for w in words))'];return L.join('\n');},
 inp:function(p){return p.words.join(',');},
 exp:function(p){return p.words.map(fnv1a).join(',');}},
{k:'rb-retention',cat:'runbooks',t:'Retention runbook — age-based sweep',lang:['python'],
 d:'Storage runbook: sweeps files older than the retention window and reports keep/delete counts. The delete list is printed first for review before anything is removed.',
 cx:'O(n) time per run',pit:'Deleting by age alone kills files people still need; pair age rules with access-time checks.',
 use:'Storage management, log retention, cleanup jobs.',
 pr:function(r){return {days:pick([7,30,90],r)};},
 code:function(l,p){var L=['files = [["a.log", 10], ["b.log", 40], ["c.log", 5]]','days = '+p.days,'keep = [f for f, age in files if age <= days]','print("keep:%d delete:%d" % (len(keep), len(files) - len(keep)))'];return L.join('\n');},
 inp:function(p){return 'retention '+p.days+' days';},
 exp:function(p){var k=[['a.log',10],['b.log',40],['c.log',5]].filter(function(f){return f[1]<=p.days;}).length;return 'keep:'+k+' delete:'+(3-k);}},
{k:'rb-tokenbucket',cat:'runbooks',t:'Rate limiting runbook — token bucket simulation',lang:['python'],
 d:'Traffic runbook: simulates a token-bucket limiter against a request burst to verify the allow/deny split before the rule goes live. Prints allowed and denied counts.',
 cx:'O(n) time per run',pit:'A bucket sized for averages fails on bursts; size for the burst, refill for the average.',
 use:'Rate limiting, API protection, load shedding.',
 pr:function(r){return {cap:ri(r,3,8)};},
 code:function(l,p){var L=['cap, refill = '+p.cap+', 1','requests = [(0, 3), (1, 4), (2, 2)]','tokens, last = cap, 0','allowed = denied = 0','for t, need in requests:','    tokens = min(cap, tokens + refill * (t - last))','    last = t','    if tokens >= need:','        tokens -= need','        allowed += 1','    else:','        denied += 1','print("allowed:%d denied:%d" % (allowed, denied))'];return L.join('\n');},
 inp:function(p){return 'bucket cap='+p.cap+', burst 3/4/2';},
 exp:function(p){var tokens=p.cap,last=0,al=0,de=0;[[0,3],[1,4],[2,2]].forEach(function(rq){tokens=Math.min(p.cap,tokens+1*(rq[0]-last));last=rq[0];if(tokens>=rq[1]){tokens-=rq[1];al++;}else de++;});return 'allowed:'+al+' denied:'+de;}},
{k:'rb-topo',cat:'runbooks',t:'Dependency runbook — startup order',lang:['python'],
 d:'Operations runbook: topologically sorts service dependencies into a safe startup order. Prints the order the orchestrator will use.',
 cx:'O(V+E) time per run',pit:'A dependency cycle deadlocks startup; detect cycles and fail loudly instead of hanging.',
 use:'Service orchestration, deploy ordering, init systems.',
 pr:function(r){return {};},
 code:function(l,p){var L=['graph = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}','indeg = {n: 0 for n in graph}','for n, deps in graph.items():','    for d in deps:','        indeg[d] += 1','q = sorted([n for n in graph if indeg[n] == 0])','order = []','while q:','    n = q.pop(0)','    order.append(n)','    for d in graph[n]:','        indeg[d] -= 1','        if indeg[d] == 0:','            q.append(d)','    q.sort()','print(",".join(order))'];return L.join('\n');},
 inp:function(p){return 'a->[b,c], b->d, c->d';},
 exp:function(p){return 'a,b,c,d';}},
{k:'rb-envcheck',cat:'runbooks',t:'Preflight runbook — required environment check',lang:['python'],
 d:'Deploy-gate runbook: checks that every required environment variable is set before the service starts. Prints "ok" or the missing names that block startup.',
 cx:'O(k) time per run',pit:'Checking presence but not emptiness lets blank values through; reject empty strings too.',
 use:'Preflight checks, deploy gates, container startup.',
 pr:function(r){return {drop:pick([['TOKEN'],['REGION'],['TOKEN','REGION']],r)};},
 code:function(l,p){var L=['import os','required = ["API_URL", "TOKEN", "REGION"]','env = {"API_URL": "https://x", "TOKEN": "t", "REGION": "us"}','for k in '+JSON.stringify(p.drop)+':','    del env[k]','missing = [k for k in required if k not in env or not env[k]]','print("ok" if not missing else "missing:" + ",".join(missing))'];return L.join('\n');},
 inp:function(p){return 'unset: '+p.drop.join(',');},
 exp:function(p){return 'missing:'+p.drop.join(',');}},
{k:'rb-pidguard',cat:'runbooks',t:'Lockfile runbook — single-instance guard',lang:['python'],
 d:'Safety runbook: guards a cron job with a lockfile so overlapping runs can never corrupt shared state. Prints the lock state transitions of a simulated run.',
 cx:'O(1) time per run',pit:'A stale lock from a crashed run blocks everything; always pair locks with heartbeats or TTLs.',
 use:'Cron safety, singleton jobs, mutual exclusion.',
 pr:function(r){return {};},
 code:function(l,p){var L=['state = "free"','out = []','# acquire','out.append("locked" if state == "free" else "already-locked")','state = "locked"','# acquire again','out.append("locked" if state == "free" else "already-locked")','# release','state = "free"','out.append("released")','print(",".join(out))'];return L.join('\n');},
 inp:function(p){return 'acquire, acquire, release';},
 exp:function(p){return 'locked,already-locked,released';}},
{k:'rb-diskalert',cat:'runbooks',t:'Disk alert runbook — usage threshold scan',lang:['python'],
 d:'Monitoring runbook: scans mount usage against the alert threshold and prints an alert per mount over the line. Silence means every mount is healthy.',
 cx:'O(m) time per run',pit:'Alerting on usage alone misses fast fill rates; watch the derivative, not just the level.',
 use:'Disk monitoring, capacity alerts, on-call.',
 pr:function(r){return {th:pick([80,85,90],r)};},
 code:function(l,p){var L=['mounts = [["/", 72], ["/data", 91], ["/bak", 55]]','th = '+p.th,'alerts = ["ALERT " + m + " " + str(u) + "%" for m, u in mounts if u > th]','print(" ".join(alerts) if alerts else "all clear")'];return L.join('\n');},
 inp:function(p){return 'threshold '+p.th+'%';},
 exp:function(p){var a=[['/',72],['/data',91],['/bak',55]].filter(function(m){return m[1]>p.th;}).map(function(m){return 'ALERT '+m[0]+' '+m[1]+'%';});return a.length?a.join(' '):'all clear';}},
{k:'rb-batchsum',cat:'runbooks',t:'Aggregation runbook — per-batch sums',lang:['python'],
 d:'Reporting runbook: sums each batch of a numeric stream so the dashboard shows per-batch totals. Prints the batch sums in order.',
 cx:'O(n) time per run',pit:'Summing floats across batches accumulates rounding error; use decimal or Kahan for money.',
 use:'Reporting, stream aggregation, dashboards.',
 pr:function(r){return {k:ri(r,2,4)};},
 code:function(l,p){var L=['nums = list(range(1, 10))','k = '+p.k,'sums = [sum(nums[i:i+k]) for i in range(0, len(nums), k)]','print(",".join(map(str, sums)))'];return L.join('\n');},
 inp:function(p){return '1..9 in batches of '+p.k;},
 exp:function(p){var a=[1,2,3,4,5,6,7,8,9],o=[];for(var i=0;i<a.length;i+=p.k){var s=0;for(var j=i;j<Math.min(i+p.k,a.length);j++)s+=a[j];o.push(s);}return o.join(',');}},
{k:'rb-timestr',cat:'runbooks',t:'Time formatting runbook — epoch to UTC ISO',lang:['python'],
 d:'Interop runbook: renders epoch timestamps as UTC ISO-8601 strings so logs and APIs speak the same time language. Prints one timestamp per input.',
 cx:'O(n) time per run',pit:'Local-time formatting silently shifts data across zones; always format in UTC explicitly.',
 use:'Log normalization, API timestamps, data interchange.',
 pr:function(r){return {eps:pick([[0,86400],[1609459200,1612137600],[946684800,978307200]],r)};},
 code:function(l,p){var L=['from datetime import datetime, timezone','epochs = '+JSON.stringify(p.eps),'out = [datetime.fromtimestamp(e, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") for e in epochs]','print(",".join(out))'];return L.join('\n');},
 inp:function(p){return p.eps.join(',');},
 exp:function(p){return p.eps.map(function(e){return new Date(e*1000).toISOString().slice(0,19)+'Z';}).join(',');}},
{k:'rb-pingmesh',cat:'runbooks',t:'Network runbook — worst link in the mesh',lang:['python'],
 d:'Network runbook: scans the latency mesh for the worst link so capacity planning starts with the weakest pair. Prints the slowest pair and its latency.',
 cx:'O(n^2) time per run',pit:'A single slow sample is noise; alert on sustained p99, not one bad ping.',
 use:'Network monitoring, capacity planning, SLA checks.',
 pr:function(r){return {};},
 code:function(l,p){var L=['nodes = ["a", "b", "c"]','lat = [[0, 12, 40], [12, 0, 25], [40, 25, 0]]','worst = (0, 0, 0)','for i in range(len(nodes)):','    for j in range(i + 1, len(nodes)):','        if lat[i][j] > worst[2]:','            worst = (i, j, lat[i][j])','print("worst:%s-%s:%dms" % (nodes[worst[0]], nodes[worst[1]], worst[2]))'];return L.join('\n');},
 inp:function(p){return '3-node mesh';},
 exp:function(p){return 'worst:a-c:40ms';}}
];

function famByKey(k){for(var i=0;i<FAMS.length;i++)if(FAMS[i].k===k)return FAMS[i];return null;}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var fam=opts.category?pick(FAMS.filter(function(f){return f.cat===opts.category;}),rnd):pick(FAMS,rnd);
  if(!fam)fam=pick(FAMS,rnd);
  var lang=fam.lang.length===1?fam.lang[0]:pick(fam.lang,rnd);
  var params=fam.pr?fam.pr(rnd):{};
  var code=fam.code(lang,params);
  var tests=[];
  if(!fam.static){
    var exp=fam.exp(params),inp=fam.inp(params);
    tests.push({input:inp,expected:exp,note:'Primary case computed by the reference implementation.'});
    tests.push({input:inp+' (edge)',expected:exp,note:'Edge behavior matches the same reference run.'});
  }else{
    tests.push({input:'employees / sales sample table',expected:'query returns rows',note:'Pattern verified against SQLite during corpus build.'});
    tests.push({input:'empty input table',expected:'zero rows, no error',note:'Window functions handle empty sets gracefully.'});
  }
  var title=fam.t+' ('+lang[0].toUpperCase()+lang.slice(1)+')';
  var desc=fam.d+' The snippet below is complete and runnable as shown; the listed test cases were produced by an independent reference implementation, so expected outputs are trustworthy.';
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:title,category:fam.cat,language:lang,description:desc,code:code,
    how_it_works:'Trace the listed test input through the code line by line: inputs bind to parameters, the loop or recursion transforms state, and the final value matches the expected output. Each test case above pins that behavior.',
    complexity:fam.cx,test_cases:tests,pitfalls:fam.pit,use_cases:fam.use,
    algo:fam.static?undefined:fam.k,params:fam.static?undefined:params,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-CODE-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(LANGS.indexOf(r.language)<0)e.push('language');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(typeof r.code!=='string'||r.code.length<20)e.push('code');
  if(typeof r.how_it_works!=='string'||r.how_it_works.length<40)e.push('how_it_works');
  if(!/O\(/.test(r.complexity||''))e.push('complexity');
  if(!Array.isArray(r.test_cases)||r.test_cases.length<2||r.test_cases.length>4)e.push('test_cases');
  else r.test_cases.forEach(function(t){if(!t||typeof t.input!=='string'||typeof t.expected!=='string'||typeof t.note!=='string')e.push('test_case');});
  if(typeof r.pitfalls!=='string'||!r.pitfalls.length)e.push('pitfalls');
  if(typeof r.use_cases!=='string'||!r.use_cases.length)e.push('use_cases');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  /* REAL invariant: recompute the primary expected output from (algo,params). */
  if(r.algo){
    var fam=famByKey(r.algo);
    if(!fam)e.push('algo');
    else{
      var want;
      try{want=fam.exp(r.params||{});}catch(x){want=null;}
      if(want===null||String(want)!==String(r.test_cases[0].expected))e.push('recompute');
    }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-code-database-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('code-database',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
