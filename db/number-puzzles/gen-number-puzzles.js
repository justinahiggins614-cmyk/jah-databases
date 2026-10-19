(function(){'use strict';
/* Signature Number Puzzles Database generator — jahdb-number-puzzles-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-NUM-P-';
var TOPICS=[["Magic Squares", "Rows, columns, diagonals align."], ["KenKen", "Cage-arithmetic challenges."], ["Kakuro", "Cross-sums number grids."], ["Sudoku Minis", "Small-grid sudoku fun."], ["Calcudoku", "Math-cage sudoku."], ["Number Sequences", "Find the pattern."], ["Cryptarithms", "SEND + MORE = MONEY classics."], ["Alphametics", "Word-sum puzzles."], ["Number Crosswords", "Crossnumber grids."], ["Prime Puzzles", "Prime-hunting challenges."], ["Factor Puzzles", "Multiplication-grid logic."], ["Skyscrapers", "Visibility-clue grids."], ["Futoshiki", "Inequality-sign sudoku."], ["Killer Sudoku", "Cage-sum sudoku."], ["Jigsaw Sudoku", "Irregular-region sudoku."], ["Wordoku", "Letter-based sudoku."], ["Mathdoku", "Arithmetic grid puzzles."], ["Hidato", "Consecutive-number paths."], ["Numbrix", "Snake-path number grids."], ["Binary Puzzles", "Takuzu 0-1 logic."], ["Masyu", "Pearl-loop drawing."], ["Yajilin", "Arrow-clue loop puzzles."], ["Number Mazes", "Count-your-way mazes."], ["Countdown Numbers", "Reach-the-target arithmetic."], ["24 Game", "Make 24 from four numbers."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'number puzzles creation', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('number-puzzles',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}

/* Group-0 expansion: 10 new topics. */
TOPICS.push(
["The Collatz Conjecture (Vol. 2)","Take any number: halve it if even, triple-and-add-one if odd. Every number tested — all the way to 2^68 — reaches 1. Nobody can prove it always does."],
["Perfect Numbers","Numbers equal to the sum of their divisors: 6, 28, 496 — known since Euclid, and every even one comes from a Mersenne prime."],
["Kaprekar’s Constant: 6174","Take any 4-digit number with two different digits, sort its digits up and down, subtract — repeat, and you always land on 6174."],
["The 1089 Trick","Write a 3-digit number, reverse it, subtract, reverse the result, add — the answer is always 1089. A party trick with real algebra behind it."],
["Palindromic Numbers","Numbers that read the same backward and forward — and the delightful “reverse and add” game that may never end."],
["Armstrong Numbers","Numbers equal to the sum of their digits raised to the digit count: 153 = 1³ + 5³ + 3³. Only 88 exist."],
["Benford’s Law","In real-world data, the digit 1 appears as the leading digit 30% of the time — and accountants use this to catch fraud."],
["The Birthday Paradox","In a room of just 23 people, two probably share a birthday. The math surprises everyone — and powers cryptography."],
["Cyclic Numbers: 142857","Multiply 142857 by 1 through 6 and the same digits just rotate. Multiply by 7 and you get 999999. Coincidence? No — it’s 1/7."],
["Fermat’s Little Theorem in Puzzles","A 400-year-old theorem that doubles as a puzzle engine: a^(p−1) ≡ 1 (mod p) for prime p — and endless tricks follow."]
);
})();