(function(){'use strict';
/* Signature Brain Teasers Database generator — jahdb-brain-teasers-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-BRAIN-';
var TOPICS=[["Lateral Thinking", "Think sideways to solve."], ["What Is It", "Mystery-object teasers."], ["Sequence Solvers", "Find the next in line."], ["Odd One Out", "Spot the misfit."], ["Word Ladders", "Climb from word to word."], ["Anagram Teasers", "Scrambled-letter challenges."], ["Cryptarithms", "Letters-as-digits puzzles."], ["Weighing Teasers", "Balance-scale brainwork."], ["Crossing Teasers", "Get everyone across."], ["Time Teasers", "Clock-and-calendar tricks."], ["Age Teasers", "How-old-are-they puzzles."], ["Speed Teasers", "Rate-and-distance riddles."], ["Coin Teasers", "Heads-or-tails head-scratchers."], ["Card Teasers", "Deck-based deductions."], ["Chess Teasers", "Knight tours and queens."], ["Match Teasers", "Matchstick mind-benders."], ["Cube Teasers", "Folding and unfolding."], ["Water Teasers", "Pouring puzzles."], ["Light Bulb Teasers", "Switch-and-bulb logic."], ["Prisoner Teasers", "Hat-and-door classics."], ["Truth-Teller Teasers", "Knights, knaves, spies."], ["Island Teasers", "Blue eyes and common knowledge."], ["Bridge Teasers", "Torch-crossing optimization."], ["Elevator Teasers", "The man who takes stairs."], ["Word Equation Teasers", "DITLOID-style puzzles."], ["The Lightning Logic Sprint", "The Lightning Logic Sprint is a tournament event where contestants solve 20 rapid-fire logic puzzles in 10 minutes, with points for speed and accuracy."], ["The Memory Palace Marathon", "The Memory Palace Marathon tests memorization: contestants study a shuffled deck for five minutes, then recall it in order."], ["The Lateral Thinking Gauntlet", "The Lateral Thinking Gauntlet presents classic lateral puzzles where the obvious reading is wrong: 'A man pushes his car up to a hotel and says I'm bankrupt. Why?' (He's playing Monopoly.)"], ["The Mental Math Decathlon", "The Mental Math Decathlon covers ten events: multiplication, square roots, calendar dates, and more, all done without paper."], ["The Chess Puzzle Blitz", "The Chess Puzzle Blitz gives contestants tactical chess positions with three minutes each to find the winning combination."], ["The Riddle Relay", "The Riddle Relay is a team event: each solved riddle unlocks the next, and teams race through chains of twenty."], ["The Spatial Reasoning Cube", "The Spatial Reasoning Cube event shows unfolded cube nets and asks which 3D cube each forms, under time pressure."], ["The Word Ladder Climb", "The Word Ladder Climb challenges contestants to transform one word into another, changing one letter at a time: CAT to DOG in three steps (CAT, COT, COG, DOG)."], ["The Probability Pit", "The Probability Pit poses counterintuitive probability puzzles: the Monty Hall problem, the birthday paradox, and the boy-or-girl paradox."], ["The Cipher Break", "The Cipher Break event hands contestants encoded messages in classic ciphers: Caesar shifts, Vigenere, and Playfair."], ["The Estimation Showdown", "The Estimation Showdown asks Fermi questions: how many piano tuners in Chicago, how many grains of sand on a beach?"], ["The Pattern Matrix", "The Pattern Matrix shows 3x3 grids with one cell missing, in the style of Raven's progressive matrices, testing pure pattern recognition."], ["The Debate Puzzle", "The Debate Puzzle is unusual: contestants get a paradox, like the Ship of Theseus, and must argue both sides convincingly."], ["The Speed Sudoku Showdown", "The Speed Sudoku Showdown is a pure racing event: contestants solve identical expert grids side by side, fastest clean solve wins."], ["The Grand Puzzle Hunt", "The Grand Puzzle Hunt is the tournament finale: teams race through a building solving interconnected puzzles that combine every earlier event's skills."]];
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
    type:'brain teasers creation', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||(r.content_completeness!=='stub'&&r.content.length<50))errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('brain-teasers',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();