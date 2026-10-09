/* JAH Test Case Database generator. Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function choice(r,s){return s[(r()*s.length)|0];}
var CATS=['python','javascript','sql','java','go','rust'];
var WORDS=['alpha','bravo','cargo','delta','echo','foxtrot','gamma','hotel','index','joker'];
function rev(s){return s.split('').reverse().join('');}
function isPrime(n){if(n<2)return false;for(var i=2;i*i<=n;i++)if(n%i===0)return false;return true;}
function fib(n){var a=0,b=1;for(var i=0;i<n;i++){var t=a+b;a=b;b=t;}return a;}
function gcd(a,b){while(b){var t=a%b;a=b;b=t;}return Math.abs(a);}
function fac(n){var r=1;for(var i=2;i<=n;i++)r*=i;return r;}
/* each fn: [name, gen(rnd)->{inputs,expected}] */
var F={
python:[
['add',function(r){var a=ri(r,-50,50),b=ri(r,-50,50);return{inputs:{a:a,b:b},expected:a+b};}],
['is_even',function(r){var n=ri(r,0,100);return{inputs:{n:n},expected:n%2===0};}],
['factorial',function(r){var n=ri(r,0,8);return{inputs:{n:n},expected:fac(n)};}],
['reverse_string',function(r){var s=pick(r,WORDS)+pick(r,WORDS);return{inputs:{s:s},expected:rev(s)};}],
['is_palindrome',function(r){var s=r()<0.5?pick(r,WORDS):rev(pick(r,WORDS));return{inputs:{s:s},expected:s===rev(s)};}],
['max_of_three',function(r){var a=ri(r,0,99),b=ri(r,0,99),c=ri(r,0,99);return{inputs:{a:a,b:b,c:c},expected:Math.max(a,b,c)};}],
['fibonacci',function(r){var n=ri(r,0,15);return{inputs:{n:n},expected:fib(n)};}],
['count_vowels',function(r){var s=pick(r,WORDS)+pick(r,WORDS);return{inputs:{s:s},expected:(s.match(/[aeiou]/g)||[]).length};}],
['celsius_to_fahrenheit',function(r){var c=ri(r,-40,100);return{inputs:{celsius:c},expected:Math.round((c*9/5+32)*100)/100};}],
['is_prime',function(r){var n=ri(r,0,100);return{inputs:{n:n},expected:isPrime(n)};}],
['clamp',function(r){var v=ri(r,-10,110);return{inputs:{value:v,lo:0,hi:100},expected:Math.min(100,Math.max(0,v))};}],
['dedupe',function(r){var a=[ri(r,0,5),ri(r,0,5),ri(r,0,5),ri(r,0,5)];var u=[];a.forEach(function(x){if(u.indexOf(x)<0)u.push(x);});return{inputs:{items:a},expected:u};}]
],
javascript:[
['sumArray',function(r){var a=[ri(r,0,20),ri(r,0,20),ri(r,0,20)];return{inputs:{arr:a},expected:a[0]+a[1]+a[2]};}],
['capitalize',function(r){var s=pick(r,WORDS);return{inputs:{s:s},expected:s.charAt(0).toUpperCase()+s.slice(1)};}],
['chunk',function(r){var a=[1,2,3,4,5,6],n=ri(r,1,3);var o=[];for(var i=0;i<a.length;i+=n)o.push(a.slice(i,i+n));return{inputs:{arr:a,size:n},expected:o};}],
['unique',function(r){var a=[ri(r,0,4),ri(r,0,4),ri(r,0,4)];var u=[];a.forEach(function(x){if(u.indexOf(x)<0)u.push(x);});return{inputs:{arr:a},expected:u};}],
['camelToSnake',function(r){var s='my'+pick(r,WORDS).replace(/^./,function(c){return c.toUpperCase();})+'Name';return{inputs:{s:s},expected:s.replace(/[A-Z]/g,function(c){return '_'+c.toLowerCase();})};}],
['repeat',function(r){var s=pick(r,WORDS),n=ri(r,1,4);var o='';for(var i=0;i<n;i++)o+=s;return{inputs:{s:s,n:n},expected:o};}],
['gcd',function(r){var a=ri(r,1,60),b=ri(r,1,60);return{inputs:{a:a,b:b},expected:gcd(a,b)};}],
['isEmail',function(r){var ok=r()<0.6;var s=ok?pick(r,WORDS)+'@example.com':pick(r,WORDS);return{inputs:{s:s},expected:/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s)};}],
['flatten',function(r){var a=[[ri(r,0,9)],[ri(r,0,9),ri(r,0,9)]];var o=[];a.forEach(function(x){o=o.concat(x);});return{inputs:{nested:a},expected:o};}],
['padStart',function(r){var s=pick(r,WORDS),n=ri(r,3,8);var o=s;while(o.length<n)o='0'+o;return{inputs:{s:s,length:n},expected:o};}]
],
sql:[
['total_sales',function(r){var a=ri(r,100,999),b=ri(r,100,999);return{inputs:{q1:a,q2:b},expected:a+b};}],
['avg_price',function(r){var a=ri(r,10,99),n=ri(r,2,5);return{inputs:{sum:a,n:n},expected:Math.round(a/n*100)/100};}],
['name_length',function(r){var s=pick(r,WORDS);return{inputs:{name:s},expected:s.length};}],
['upper_code',function(r){var s=pick(r,WORDS);return{inputs:{code:s},expected:s.toUpperCase()};}],
['discount_price',function(r){var p=ri(r,10,200),d=ri(r,5,30);return{inputs:{price:p,discount_pct:d},expected:Math.round(p*(1-d/100)*100)/100};}],
['row_count',function(r){var n=ri(r,0,50);return{inputs:{table_rows:n},expected:n};}],
['first_letter',function(r){var s=pick(r,WORDS);return{inputs:{name:s},expected:s.charAt(0)};}],
['age_years',function(r){var b=ri(r,1970,2010);return{inputs:{birth_year:b},expected:2026-b};}],
['coalesce_name',function(r){var s=r()<0.5?pick(r,WORDS):null;return{inputs:{name:s},expected:s===null?'unknown':s};}],
['in_stock',function(r){var q=ri(r,0,20);return{inputs:{qty:q},expected:q>0};}]
],
java:[
['add',function(r){var a=ri(r,-50,50),b=ri(r,-50,50);return{inputs:{a:a,b:b},expected:a+b};}],
['max',function(r){var a=ri(r,0,99),b=ri(r,0,99);return{inputs:{a:a,b:b},expected:Math.max(a,b)};}],
['isPositive',function(r){var n=ri(r,-20,20);return{inputs:{n:n},expected:n>0};}],
['square',function(r){var n=ri(r,0,20);return{inputs:{n:n},expected:n*n};}],
['concat',function(r){var a=pick(r,WORDS),b=pick(r,WORDS);return{inputs:{a:a,b:b},expected:a+b};}],
['toUpper',function(r){var s=pick(r,WORDS);return{inputs:{s:s},expected:s.toUpperCase()};}],
['abs',function(r){var n=ri(r,-50,50);return{inputs:{n:n},expected:Math.abs(n)};}],
['min3',function(r){var a=ri(r,0,99),b=ri(r,0,99),c=ri(r,0,99);return{inputs:{a:a,b:b,c:c},expected:Math.min(a,Math.min(b,c))};}],
['isEven',function(r){var n=ri(r,0,100);return{inputs:{n:n},expected:n%2===0};}],
['repeatStr',function(r){var s=pick(r,WORDS),n=ri(r,1,3);var o='';for(var i=0;i<n;i++)o+=s;return{inputs:{s:s,n:n},expected:o};}]
],
go:[
['Add',function(r){var a=ri(r,-50,50),b=ri(r,-50,50);return{inputs:{a:a,b:b},expected:a+b};}],
['Max',function(r){var a=ri(r,0,99),b=ri(r,0,99);return{inputs:{a:a,b:b},expected:Math.max(a,b)};}],
['IsEven',function(r){var n=ri(r,0,100);return{inputs:{n:n},expected:n%2===0};}],
['Reverse',function(r){var s=pick(r,WORDS);return{inputs:{s:s},expected:rev(s)};}],
['Repeat',function(r){var s=pick(r,WORDS),n=ri(r,1,3);var o='';for(var i=0;i<n;i++)o+=s;return{inputs:{s:s,n:n},expected:o};}],
['Sum',function(r){var a=[ri(r,0,20),ri(r,0,20)];return{inputs:{nums:a},expected:a[0]+a[1]};}],
['Contains',function(r){var s=pick(r,WORDS),sub=s.slice(0,2);return{inputs:{s:s,sub:sub},expected:s.indexOf(sub)>=0};}],
['ToUpper',function(r){var s=pick(r,WORDS);return{inputs:{s:s},expected:s.toUpperCase()};}],
['Min',function(r){var a=ri(r,0,99),b=ri(r,0,99);return{inputs:{a:a,b:b},expected:Math.min(a,b)};}],
['Len',function(r){var a=[ri(r,0,9),ri(r,0,9),ri(r,0,9)];return{inputs:{slice:a},expected:a.length};}]
],
rust:[
['add',function(r){var a=ri(r,-50,50),b=ri(r,-50,50);return{inputs:{a:a,b:b},expected:a+b};}],
['is_even',function(r){var n=ri(r,0,100);return{inputs:{n:n},expected:n%2===0};}],
['double',function(r){var n=ri(r,0,50);return{inputs:{n:n},expected:n*2};}],
['reverse',function(r){var s=pick(r,WORDS);return{inputs:{s:s},expected:rev(s)};}],
['len',function(r){var s=pick(r,WORDS)+pick(r,WORDS);return{inputs:{s:s},expected:s.length};}],
['max',function(r){var a=ri(r,0,99),b=ri(r,0,99);return{inputs:{a:a,b:b},expected:Math.max(a,b)};}],
['starts_with',function(r){var s=pick(r,WORDS);return{inputs:{s:s,prefix:s.slice(0,2)},expected:true};}],
['square',function(r){var n=ri(r,0,20);return{inputs:{n:n},expected:n*n};}],
['is_positive',function(r){var n=ri(r,-20,20);return{inputs:{n:n},expected:n>0};}],
['repeat',function(r){var s=pick(r,WORDS),n=ri(r,1,3);var o='';for(var i=0;i<n;i++)o+=s;return{inputs:{s:s,n:n},expected:o};}]
]
};
function shortInputs(inp){
  var ks=Object.keys(inp);
  return ks.map(function(k){var v=inp[k];return JSON.stringify(v).slice(0,24);}).join(', ');
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=opts.category||pick(rnd,CATS);
  var bank=F[cat]||F.python;
  var f=bank[ri(rnd,0,bank.length-1)];
  var spec=f[1](rnd);
  var edge=rnd()<0.25;
  return {
    id:'JAH-TEST-'+String(seed).padStart(6,'0'),
    test_id:'JAH-TEST-'+String(seed).padStart(6,'0'),
    function_name:f[0],
    language:cat,
    inputs:spec.inputs,
    expected_output:spec.expected,
    edge_case:edge,
    passed_ref:true,
    title:f[0]+'('+shortInputs(spec.inputs)+')'
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','test_id','function_name','language','inputs','expected_output','edge_case','passed_ref','title'].forEach(function(k){if(r[k]===undefined||r[k]===null||r[k]==='')e.push('missing '+k);});
  if(r.id&&!/^JAH-TEST-\d{6}$/.test(r.id))e.push('bad id');
  if(r.test_id&&r.test_id!==r.id)e.push('test_id != id');
  if(r.language&&CATS.indexOf(r.language)<0)e.push('bad language');
  if(r.inputs&&(typeof r.inputs!=='object'||Array.isArray(r.inputs)))e.push('inputs not object');
  if(typeof r.edge_case!=='boolean')e.push('edge_case not bool');
  if(r.passed_ref!==true)e.push('passed_ref not true');
  return{ok:!e.length,errors:e};
}
var gen={version:'jahdb-unit-tests-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unit-tests',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
