(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['python','javascript','sql','bash','java','c'];
var PREFIX='JAH-CODE-';
/* each template: [prompt, code(lines array with {v} slot), explanation] */
var T={
python:[
 ['Write a Python function that returns the sum of squares from 1 to n.',
  ['def sum_of_squares(n):','    total = 0','    for i in range(1, n + 1):','        total += i * i','    return total','','print(sum_of_squares({v}))'],
  'Loop from 1 to n, accumulate each square, and return the total. It runs in linear time.'],
 ['Write a Python function that counts vowels in a string.',
  ['def count_vowels(s):','    vowels = "aeiouAEIOU"','    count = 0','    for ch in s:','        if ch in vowels:','            count += 1','    return count','','print(count_vowels("{v}"))'],
  'Scan each character once and count matches against the vowel set. Simple and fast.'],
 ['Write a Python function that reverses the words in a sentence.',
  ['def reverse_words(sentence):','    words = sentence.split()','    words.reverse()','    return " ".join(words)','','print(reverse_words("{v}"))'],
  'Split on spaces, reverse the list in place, then rejoin with single spaces.'],
 ['Write a Python function that finds the maximum value in a list.',
  ['def find_max(items):','    best = items[0]','    for x in items[1:]:','        if x > best:','            best = x','    return best','','print(find_max([{v}]))'],
  'Track the best value seen so far in one pass; it handles negatives correctly.']
],
javascript:[
 ['Write a JavaScript function that filters even numbers from an array.',
  ['function evens(arr) {','  return arr.filter(function(x) {','    return x % 2 === 0;','  });','}','','console.log(evens([{v}]));'],
  'The filter method keeps only elements passing the even test. Clean and idiomatic.'],
 ['Write a JavaScript function that capitalizes the first letter of a string.',
  ['function capitalize(s) {','  if (!s) return s;','  return s[0].toUpperCase() + s.slice(1);','}','','console.log(capitalize("{v}"));'],
  'Uppercase the first character and append the rest unchanged. Guards empty input.'],
 ['Write a JavaScript function that sums an array of numbers.',
  ['function sum(arr) {','  var total = 0;','  for (var i = 0; i < arr.length; i++) {','    total += arr[i];','  }','  return total;','}','','console.log(sum([{v}]));'],
  'A single loop accumulates the total; works for any numeric array.'],
 ['Write a JavaScript function that checks if a number is prime.',
  ['function isPrime(n) {','  if (n < 2) return false;','  for (var i = 2; i * i <= n; i++) {','    if (n % i === 0) return false;','  }','  return true;','}','','console.log(isPrime({v}));'],
  'Trial division up to the square root is enough; early exit keeps it fast.']
],
sql:[
 ['Write a SQL query listing the top {v} customers by total spend.',
  ['SELECT customer_id, SUM(amount) AS total','FROM orders','GROUP BY customer_id','ORDER BY total DESC','LIMIT {v};'],
  'Aggregate spend per customer, sort descending, and take the first rows.'],
 ['Write a SQL query counting orders per month.',
  ['SELECT DATE_TRUNC(\'month\', order_date) AS month, COUNT(*) AS n','-- monthly order counts','FROM orders','GROUP BY 1','ORDER BY 1;'],
  'Truncate dates to month buckets, count rows per bucket, order chronologically.'],
 ['Write a SQL query finding products never ordered.',
  ['SELECT p.product_id, p.name','-- products with no orders','FROM products p','LEFT JOIN order_items o ON o.product_id = p.product_id','WHERE o.product_id IS NULL;'],
  'A left join plus a null check isolates products with no matching order rows.'],
 ['Write a SQL query with the average order value by region.',
  ['SELECT region, AVG(amount) AS avg_value','-- average order value by region','FROM orders','GROUP BY region','HAVING COUNT(*) >= {v};'],
  'Group by region, average the amounts, and require a minimum order count.']
],
bash:[
 ['Write a bash one-liner pipeline counting lines in {v} files.',
  ['#!/bin/bash','count=0','for f in *.{v}; do','  n=$(wc -l < "$f")','  count=$((count + n))','done','echo "Total lines: $count"'],
  'Loop over matching files, count lines with wc, and accumulate the total.'],
 ['Write a bash script that backs up a directory with a timestamp.',
  ['#!/bin/bash','src="$1"','stamp=$(date +%Y%m%d)','tar -czf "backup-$stamp.tgz" "$src"','echo "Saved backup-$stamp.tgz"'],
  'Build a dated archive name, compress the directory, and confirm the file.'],
 ['Write a bash script that prints the {v} largest files in a directory.',
  ['#!/bin/bash','# largest files first','find . -maxdepth 1 -type f -printf "%s %p\\n" \\','  | sort -nr \\','  | head -{v}'],
  'Find files with sizes, sort numerically descending, and show the top rows.'],
 ['Write a bash script that greets each name in a list.',
  ['#!/bin/bash','# greet each name','while IFS= read -r name; do','  echo "Hello, $name!"','done < names.txt'],
  'Read names line by line and print a greeting for each one.']
],
java:[
 ['Write a Java method that reverses a string.',
  ['public static String reverse(String s) {','    StringBuilder sb = new StringBuilder();','    for (int i = s.length() - 1; i >= 0; i--) {','        sb.append(s.charAt(i));','    }','    return sb.toString();','}'],
  'Walk the string backwards appending to a StringBuilder; linear and allocation-friendly.'],
 ['Write a Java method that finds the smallest integer in an array.',
  ['public static int findMin(int[] a) {','    int best = a[0];','    for (int i = 1; i < a.length; i++) {','        if (a[i] < best) best = a[i];','    }','    return best;','}'],
  'One pass keeps the smallest value seen; the loop starts at index 1.'],
 ['Write a Java method that checks whether an array is sorted ascending.',
  ['public static boolean isSorted(int[] a) {','    for (int i = 1; i < a.length; i++) {','        if (a[i] < a[i - 1]) return false;','    }','    return true;','}'],
  'Compare each pair of neighbors; the first inversion proves it unsorted.'],
 ['Write a Java class holding a simple counter.',
  ['public class Counter {','    private int count = 0;','    public void bump() { count++; }','    public int value() { return count; }','    public void reset() { count = 0; }','}'],
  'Encapsulated state with bump, value, and reset operations.']
],
c:[
 ['Write a C function that returns the length of a string.',
  ['#include <stddef.h>','size_t str_len(const char *s) {','    size_t n = 0;','    while (s[n]) n++;','    return n;','}'],
  'Count bytes until the null terminator; no library call needed.'],
 ['Write a C function that sums an integer array.',
  ['int array_sum(const int *a, int n) {','    int total = 0;','    for (int i = 0; i < n; i++)','        total += a[i];','    return total;','}'],
  'A tight loop accumulates the sum; the caller passes the length.'],
 ['Write a C program that prints the first {v} multiples.',
  ['#include <stdio.h>','int main(void) {','    for (int i = 1; i <= {v}; i++)','        printf("%d\\n", i * {v});','    return 0;','}'],
  'Loop and print each multiple with printf; returns zero on success.'],
 ['Write a C function that swaps two integers.',
  ['void swap(int *a, int *b) {','    int t = *a;','    *a = *b;','    *b = t;','}'],
  'Dereference the pointers and exchange values through a temporary.']
]};
var V={python:['10','hello world','4, 2, 9, 1'],javascript:['2, 3, 4, 5','hello','5, 1, 4'],sql:['5','10'],bash:['txt','5'],java:[],c:['7']};
var CODA=['It handles edge cases cleanly.','The approach is easy to test.','This pattern works in most codebases.','Readability was the main goal here.','It runs in linear time.'];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var t=pick(T[cat],rnd);
  var vs=V[cat],v=vs.length?pick(vs,rnd):'';
  var code=t[1].map(function(l){return l.split('{v}').join(v);}).join('\n');
  var prompt=t[0].split('{v}').join(v);
  var expl=t[2]+' '+pick(CODA,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,task_id:id,title:prompt.slice(0,80),prompt:prompt,language:cat,solution_code:code,explanation:expl,tests_passed:ri(rnd,3,12),difficulty:pick(['easy','medium','hard'],rnd),_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-CODE-\d{6}$/.test(r.id||''))e.push('id');
  if(r.task_id!==r.id)e.push('task_id');
  if(r.title!==r.prompt.slice(0,80))e.push('title');
  if(typeof r.prompt!=='string'||!r.prompt.length)e.push('prompt');
  if(CATS.indexOf(r.language)<0)e.push('language');
  if(typeof r.solution_code!=='string'||!r.solution_code.length)e.push('solution_code');
  else{var lines=r.solution_code.split('\n');if(lines.length<5||lines.length>15)e.push('code lines');}
  if(typeof r.explanation!=='string'||!r.explanation.length)e.push('explanation');
  var ws=r.explanation.split(/[.!?]+/).filter(function(x){return x.trim().length;});
  if(ws.length<2||ws.length>3)e.push('explanation sentences');
  if(!(r.tests_passed>=0&&r.tests_passed===(r.tests_passed|0)))e.push('tests_passed');
  if(['easy','medium','hard'].indexOf(r.difficulty)<0)e.push('difficulty');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-code-problems-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('code-problems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
