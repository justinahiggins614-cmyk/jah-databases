(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
/* Self-regulation — his standing order: hard stop at 1 trillion records,
   throttled output, simulated labeling, correctness verification,
   completion detection. */
var SELF_REG={HARD_STOP:1000000000000,MAX_BATCH:50,WINDOW_MS:60000,LABEL:'simulated'};
var _callTimes=[];
function selfRegCheck(seed){
  if(typeof seed==='number'&&seed>SELF_REG.HARD_STOP){throw new Error('generator hard stop: 1,000,000,000,000 record limit reached — generation complete');}
  var now=Date.now();_callTimes=_callTimes.filter(function(t){return now-t<SELF_REG.WINDOW_MS;});
  if(_callTimes.length>=SELF_REG.MAX_BATCH){throw new Error('generator throttled: max '+SELF_REG.MAX_BATCH+' generations per minute');}
  _callTimes.push(now);
}
var CATS=["algorithms", "cryptography", "simulation", "optimization", "sensing"];
var PREFIX='JAH-QCAPS-';
var SEEDS=[{"t": "Signature Quanta App: Thought Compiler", "c": "algorithms", "l": 1, "d": "Manon's original Thought Compiler concept: a quanta app that takes a loosely-worded goal and compiles it into an ordered plan by running many candidate decompositions in superposition-inspired parallel search, then collapsing to the highest-scoring plan. The app shows its work \u2014 every candidate plan is inspectable \u2014 and the scoring function is user-editable, so the 'compiler' optimizes for what the user actually values. Labeled Signature concept: the parallel search is classical simulation of the idea.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept \u2014 simulated classically", "pipeline": ["Goal in plain words", "Candidate plan generation", "Parallel scoring", "Collapse to best", "Show all candidates"]}, "p": "// JAH demo program \u2014 Plan scoring demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction score(plan){ return plan.steps*2+plan.clarity*5-plan.cost; }\nvar plans=[{steps:3,clarity:8,cost:10},{steps:5,clarity:9,cost:6},{steps:2,clarity:5,cost:4}];\nvar best=plans.reduce(function(a,b){return score(a)>score(b)?a:b;});\ncheck(\"best plan has 5 steps\", best.steps, 5);\ncheck(\"score computed\", score(best), 49);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Memory Palace OS", "c": "simulation", "l": 2, "d": "Manon's Memory Palace OS concept: a quanta app that stores everything the user wants to remember in a navigable 3D memory palace \u2014 rooms for projects, shelves for facts \u2014 using spatial memory, the oldest mnemonic trick in the book. Retrieval is a walk, not a search: the app guides the user through the palace to the shelf where the fact lives. Spaced-repetition scheduling decides which rooms need revisiting. Signature concept, classically simulated.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "method": "method of loci + spaced repetition"}, "p": "// JAH demo program \u2014 Spaced-repetition schedule\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction nextReview(box){ return [1,3,7,14,30][Math.min(box,4)]; }\ncheck(\"box 0 \\u2192 1 day\", nextReview(0), 1);\ncheck(\"box 2 \\u2192 7 days\", nextReview(2), 7);\ncheck(\"box 4 \\u2192 30 days\", nextReview(4), 30);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Honest Coin", "c": "cryptography", "l": 3, "d": "Manon's Honest Coin concept: a randomness app that refuses to hide its source \u2014 every random bit it emits is tagged with where it came from (system entropy, user mouse timing, quantum-simulated stream) and a statistical health check runs continuously. If the entropy source degrades, the app says so loudly instead of silently weakening. It is a randomness app designed around distrust, which is the correct posture for cryptography.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "every bit tagged with its source; health checks continuous"}, "p": "// JAH demo program \u2014 Entropy health check (seeded)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction health(bits){ var ones=bits.reduce(function(s,b){return s+b;},0); var p=ones/bits.length;\n  return p>0.4&&p<0.6?'HEALTHY':'DEGRADED'; }\nvar a=7,b=[]; for(var i=0;i<1000;i++){ a=(Math.imul(a,1103515245)+12345)&0x7fffffff; b.push((a>>>16)&1); }\ncheck(\"seeded stream healthy\", health(b), \"HEALTHY\");\ncheck(\"biased stream flagged\", health([1,1,1,1,0]), \"DEGRADED\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Parallel Drafts", "c": "optimization", "l": 4, "d": "Manon's Parallel Drafts concept: a writing app that holds many draft variants of the same document 'in superposition' \u2014 the user edits one and the app propagates compatible edits across variants, collapsing to a final only at export. Variant comparison shows exactly which sentences differ, and the app never auto-deletes a variant. It treats indecision as data to be organized, not a problem to be rushed.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "collapse only at export; never auto-delete variants"}, "p": "// JAH demo program \u2014 Variant diff demo\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction diff(a,b){ var d=0; for(var i=0;i<Math.max(a.length,b.length);i++) if(a[i]!==b[i])d++; return d; }\ncheck(\"identical \\u2192 0 diffs\", diff('hello','hello'), 0);\ncheck(\"five chars differ\", diff('the cat sat','the dog ran'), 5);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Skill Ladder", "c": "simulation", "l": 5, "d": "Manon's Skill Ladder concept: a learning app that maps any skill into the basic-to-complex ladder, tests the user's current rung with five questions, and assigns exactly the next rung's drills \u2014 never two rungs ahead. Progress is a visible climb, and the app detects plateaus by tracking error patterns, switching drill types when grinding stops working. It applies the teaching-ladder standing rule to everything learnable.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "assign exactly the next rung \u2014 never two ahead"}, "p": "// JAH demo program \u2014 Rung assignment\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction rung(score){ if(score>=4) return 'advance one rung'; if(score>=2) return 'stay \u2014 more drills'; return 'drop half a rung \u2014 rebuild'; }\ncheck(\"4/5 correct\", rung(4), \"advance one rung\");\ncheck(\"2/5\", rung(2), \"stay \\u2014 more drills\");\ncheck(\"0/5\", rung(0), \"drop half a rung \\u2014 rebuild\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Fair Splitter", "c": "optimization", "l": 6, "d": "Manon's Fair Splitter concept: an app for dividing anything \u2014 bills, chores, inheritance items \u2014 using envy-free division algorithms (like cake-cutting protocols) so every party values their own share at least as much as anyone else's. Each person ranks items privately, the algorithm proposes the split, and anyone can challenge with a counter-ranking. It replaces arguments with a protocol everyone agreed to beforehand.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "method": "envy-free division protocols"}, "p": "// JAH demo program \u2014 Envy-free check (2 parties, 4 items)\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction envyFree(aVal,bVal){ return aVal>=bVal; }\nvar split={alice:['car','books'],bob:['bike','desk']};\nvar aliceVals={car:60,books:20,bike:10,desk:10}, bobVals={car:30,books:10,bike:40,desk:20};\nfunction shareVal(p,items,vals){ return items.reduce(function(s,i){return s+vals[i];},0); }\ncheck(\"alice values own share 80\", shareVal('a',split.alice,aliceVals), 80);\ncheck(\"alice envies bob? no\", envyFree(80,20), true);\ncheck(\"bob values own share 60\", shareVal('b',split.bob,bobVals), 60);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Deep Work Timer", "c": "algorithms", "l": 7, "d": "Manon's Deep Work Timer concept: a focus app that treats attention as the scarce quantum resource \u2014 it schedules work in 90-minute ultradian blocks, measures interruptions as 'decoherence events', and guards the block by batching notifications. The app's honesty feature: it reports actual focused minutes, not time the app was open. Interruption analytics show which hours of the day hold coherence best.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "block": "90-minute ultradian", "metric": "focused minutes, not app-open minutes"}, "p": "// JAH demo program \u2014 Focus score\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction focusScore(minutes, interruptions){ return Math.max(0, minutes-interruptions*5); }\ncheck(\"90 min, 2 interruptions\", focusScore(90,2), 80);\ncheck(\"90 min, 20 interruptions\", focusScore(90,20), 0);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Universal Translator's Notebook", "c": "simulation", "l": 8, "d": "Manon's Translator's Notebook concept: a language app that keeps every phrase the user learns alongside its literal gloss, cultural note, and three example sentences \u2014 because a translation without context is a fact without a home. It quizzes by recall direction (both ways), tracks which words decay fastest, and schedules them first. Built for his unified Signature language work as much as for natural languages.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "entry": "phrase + literal gloss + cultural note + 3 examples"}, "p": "// JAH demo program \u2014 Recall scheduling\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction priority(word){ return word.fails*3-word.streak; }\nvar w1={fails:4,streak:1}, w2={fails:1,streak:5};\ncheck(\"struggling word prioritized\", priority(w1)>priority(w2), true);\ncheck(\"priority score\", priority(w1), 11);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: What-If Engine", "c": "optimization", "l": 9, "d": "Manon's What-If Engine concept: a decision app that runs the user's options through explicit scenario trees \u2014 best, likely, worst case \u2014 with probabilities the user assigns and must defend. The engine's rule is that every forecast shows its assumptions; changing an assumption re-runs the tree live. It does not predict the future \u2014 it makes the user's thinking auditable.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "every forecast shows its assumptions"}, "p": "// JAH demo program \u2014 Expected value over scenarios\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction ev(scenarios){ return scenarios.reduce(function(s,x){return s+x.p*x.v;},0); }\nvar plan=[{p:0.2,v:100},{p:0.5,v:40},{p:0.3,v:-20}];\ncheck(\"EV of plan\", ev(plan), 34);\ncheck(\"probabilities sum to 1\", plan.reduce(function(s,x){return s+x.p;},0), 1);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Habit Forge", "c": "algorithms", "l": 10, "d": "Manon's Habit Forge concept: a habit app built on implementation intentions ('after X, I will Y') instead of streaks \u2014 because streaks punish one bad day and intentions survive them. Each habit has a minimum viable version (two push-ups, one sentence) for bad days, and the app measures consistency of the minimum, not the maximum. It treats willpower as a battery to budget, not a character trait.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "method": "implementation intentions + minimum viable habit"}, "p": "// JAH demo program \u2014 Consistency score\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction consistency(days){ var kept=days.filter(function(d){return d;}).length; return Math.round(kept/days.length*100); }\ncheck(\"6 of 7 days\", consistency([1,1,1,1,1,1,0]), 86);\ncheck(\"minimums count\", consistency([1,1,1]), 100);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Argument Clinic", "c": "simulation", "l": 11, "d": "Manon's Argument Clinic concept: a reasoning app where the user states a claim and the app steelmans the opposition, lists the claim's load-bearing assumptions, and flags fallacies by name. It never tells the user what to conclude \u2014 it makes weak thinking expensive and strong thinking visible. Every session ends with the user restating the best counterargument in their own words.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "method": "steelman + assumption audit + fallacy flags"}, "p": "// JAH demo program \u2014 Fallacy flagger\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction flag(text){ if(/everyone knows|obviously/i.test(text)) return 'bandwagon / proof by assertion';\n  if(/you would say that/i.test(text)) return 'ad hominem';\n  if(/slippery/i.test(text)) return 'slippery slope \u2014 check the chain';\n  return 'no flag \u2014 argue the merits'; }\ncheck(\"bandwagon\", flag('everyone knows this is true'), \"bandwagon / proof by assertion\");\ncheck(\"clean claim\", flag('the data shows X'), \"no flag \\u2014 argue the merits\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Project Autopsy", "c": "optimization", "l": 12, "d": "Manon's Project Autopsy concept: a post-mortem app that dissects finished or failed projects with a fixed protocol \u2014 timeline reconstruction, decision-point audit, resource accounting, and a 'what would we repeat' list. The app's signature move is the pre-mortem flip: before starting, it asks the team to imagine the project failed and write why. Failures become searchable so the same mistake needs a new disguise to recur.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "protocol": ["Timeline", "Decision audit", "Resource accounting", "Repeat list"]}, "p": "// JAH demo program \u2014 Autopsy protocol\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nvar __steps=[\"Reconstruct the timeline from records\", \"Audit each major decision point\", \"Account for time and money spent\", \"List what to repeat and what to never repeat\"];\n__steps.forEach(function(s,i){console.log(\"step \"+(i+1)+\": \"+s);});\ncheck(\"step count\", __steps.length, 4);\nfunction autopsyOK(sections){ return sections===4?'autopsy complete':'finish the protocol'; }\ncheck(\"four sections\", autopsyOK(4), \"autopsy complete\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Signal Garden", "c": "sensing", "l": 13, "d": "Manon's Signal Garden concept: a personal-analytics app that treats the user's data \u2014 sleep, spending, screen time \u2014 as a garden to tend rather than a dashboard to optimize. Each metric is a plant: watered by good days, wilting on bad ones, with seasons instead of streaks. The app's rule is that no metric is ever shown without its context ('sleep dropped the week of the move'), because numbers without stories lie.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "rule": "no metric without its story"}, "p": "// JAH demo program \u2014 Trend with context\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction trend(vals){ var n=vals.length, sx=0, sy=0, sxx=0, sxy=0;\n  for(var i=0;i<n;i++){ sx+=i; sy+=vals[i]; sxx+=i*i; sxy+=i*vals[i]; }\n  return (n*sxy-sx*sy)/(n*sxx-sx*sx); }\ncheck(\"rising trend positive\", trend([5,6,7,8])>0, true);\ncheck(\"falling trend negative\", trend([8,7,6,5])<0, true);\ncheck(\"slope of steady climb\", Math.round(trend([5,6,7,8])*100)/100, 1);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Oath Keeper", "c": "cryptography", "l": 14, "d": "Manon's Oath Keeper concept: a commitment app for promises that matter \u2014 it records the promise, the deadline, and the witness (a person, not an algorithm), then checks in at the halfway point and the deadline. Broken promises are not punished; they are reviewed: the app asks what changed and whether the promise should be remade or released. It treats integrity as a practice with a paper trail.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "structure": "promise + deadline + human witness"}, "p": "// JAH demo program \u2014 Promise status\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction oath(kept, reviewed){\n  if(kept) return 'kept \u2014 integrity compounded';\n  if(reviewed) return 'released or remade consciously';\n  return 'overdue \u2014 review required'; }\ncheck(\"kept\", oath(true,false), \"kept \\u2014 integrity compounded\");\ncheck(\"broken, reviewed\", oath(false,true), \"released or remade consciously\");\ncheck(\"broken, ignored\", oath(false,false), \"overdue \\u2014 review required\");\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}, {"t": "Signature Quanta App: Legacy Writer", "c": "simulation", "l": 15, "d": "Manon's Legacy Writer concept: a memoir app that interviews the user with one question per day \u2014 drawn from a bank of a thousand life questions \u2014 and assembles the answers into chapters automatically. A year of daily answers becomes a book; the app handles structure, the user supplies only honesty. It includes a 'for my family' export that prints cleanly. The premise: everyone has a book in them if the questions are good enough.", "f": {"origin": "Signature original by Justin Addam Higgins", "type": "Signature concept", "method": "one interview question per day \u2192 auto-assembled chapters"}, "p": "// JAH demo program \u2014 Book progress\n\"use strict\";\nvar __checks=[];\nfunction check(l,g,w){__checks.push([l,g,w]);}\nfunction progress(answered, total){ return Math.round(answered/total*100); }\nfunction words(answers){ return answers*150; }\ncheck(\"180 of 365 days\", progress(180,365), 49);\ncheck(\"~150 words per answer\", words(180), 27000);\nvar __ok=true;\n__checks.forEach(function(c){var ok=String(c[1])===String(c[2]);__ok=ok&&__ok;console.log((ok?\"PASS\":\"FAIL\")+\" | \"+c[0]+\" => \"+c[1]);});\nconsole.log(__ok?\"ALL CHECKS PASSED\":\"SOME CHECKS FAILED\");\nif(!__ok){throw new Error(\"demo self-check failed\");}", "s": ["Save the program as demo.js.", "Run it with: node demo.js", "Confirm every line prints PASS and the run ends with ALL CHECKS PASSED."]}];
var GEN_VARIANTS=["Signature concept sketch", "Signature prototype notes", "Signature field test", "Signature v2 idea", "Signature crossover", "Signature minimal version"];
var GEN_PROV="Signature simulated record - boundless generator output; labeled simulated for weeding per standing order. Verified by generator self-check 2026-10-21.";
var GEN_LIC="Signature original by Justin Addam Higgins.";
var SRC_EDITION="signature";
function generate(seed,opts,rnd){
  selfRegCheck(seed);
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=SEEDS.filter(function(s){return s.c===cat;});
  var sd=pick(pool.length?pool:SEEDS,rnd);
  var variant=pick(GEN_VARIANTS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var ladder=sd.l+ri(rnd,-2,2);if(ladder<1)ladder=1;if(ladder>15)ladder=15;
  var rec={
    id:id,
    title:sd.t+' \u2014 '+variant,
    ladder_rank:ladder,
    category:cat,
    description:'Simulated '+(SRC_EDITION==='signature'?'Signature-style':'public-style')+' variant ('+variant+') of the archive record \u201c'+sd.t+'\u201d. '+sd.d,
    fields:sd.f,
    demo:{language:'javascript',program:sd.p,run_steps:sd.s,expected_output:'ALL CHECKS PASSED'},
    march:'March to a million in progress \u2014 generated record (seed '+seed+'), marching toward the 1,000,000-record target.',
    provenance:GEN_PROV,
    licensing:GEN_LIC,
    source_edition:SRC_EDITION,
    last_verified:'2026-10-21',
    simulated:true
  };
  rec._seed=seed;
  var v=validate(rec);
  if(!v.ok){throw new Error('generator self-check failed: '+v.errors.join(', '));}
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.simulated!==true)e.push('simulated-label');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.length<40)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');

  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  var t=String(rec.title||'').toLowerCase();
  for(var i=0;i<sample.length;i++){
    if(String(sample[i].title||'').toLowerCase()===t){return {ok:false,errors:['duplicate of archive title: '+sample[i].title]};}
  }
  return {ok:true,errors:[]};
}

var QuantaSim=(function(){
'use strict';
/* ================= utilities ================= */
function sHash(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function sRng(seed){var a=sHash(String(seed))||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function fmtN(x,d){if(!isFinite(x))return String(x);var p=Math.pow(10,d==null?4:d);return String(Math.round(x*p)/p);}
/* safe expression evaluator: numbers, + - * / ^ % ( ) sqrt sin cos tan log */
function evalExpr(src){
  var toks=String(src).match(/(\d+\.?\d*|\.\d+|[A-Za-z_]\w*|[+\-*/^%(),])/g)||[];
  var pos=0;
  function peek(){return toks[pos];} function next(){return toks[pos++];}
  function parseE(){var v=parseT();while(peek()==='+'||peek()==='-'){var o=next();var r=parseT();v=o==='+'?v+r:v-r;}return v;}
  function parseT(){var v=parseP();while(peek()==='*'||peek()==='/'||peek()==='%'){var o=next();var r=parseP();v=o==='*'?v*r:(o==='/'?v/r:v%r);}return v;}
  function parseP(){var v=parseU();if(peek()==='^'){next();var r=parseP();v=Math.pow(v,r);}return v;}
  function parseU(){var t=peek();if(t==='-'){next();return -parseU();}if(t==='+'){next();return parseU();}
    if(t==='('){next();var v=parseE();if(next()!==')')throw new Error('missing )');return v;}
    if(/^[A-Za-z_]/.test(t||'')){next();var f=t.toLowerCase();
      if(peek()==='('){next();var a=parseE();if(next()!==')')throw new Error('missing )');
        var F={sqrt:Math.sqrt,sin:Math.sin,cos:Math.cos,tan:Math.tan,log:Math.log,exp:Math.exp,abs:Math.abs};
        if(!F[f])throw new Error('unknown function '+f);return F[f](a);}
      var C={pi:Math.PI,e:Math.E};if(C[f]!=null)return C[f];throw new Error('unknown name '+f);}
    if(/^\d/.test(t||'')){next();return parseFloat(t);}
    throw new Error('unexpected '+(t==null?'end':t));}
  var v=parseE();if(pos<toks.length)throw new Error('trailing input');
  return v;
}
/* complex numbers for the state-vector lab */
function C(re,im){return {re:re,im:im||0};}
function cadd(a,b){return C(a.re+b.re,a.im+b.im);}
function cmul(a,b){return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re);}
function cprob(a){return a.re*a.re+a.im*a.im;}
/* 2-qubit state vector simulator: state[4] over |00>,|01>,|10>,|11> (q0 = leftmost bit) */
function newState(){return [C(1),C(0),C(0),C(0)];}
function apply1(st,q,mat){ /* mat: [[a,b],[c,d]] on qubit q */
  var n=[C(0),C(0),C(0),C(0)];
  for(var i=0;i<4;i++){var bit=(i>>(1-q))&1;
    for(var nb=0;nb<2;nb++){var j=(i&(~(1<<(1-q))))|(nb<<(1-q));
      n[j]=cadd(n[j],cmul(mat[bit][nb],st[i]));}}
  for(var k=0;k<4;k++)st[k]=n[k];return st;}
function applyCNOT(st,c,t){
  var n=[C(0),C(0),C(0),C(0)];
  for(var i=0;i<4;i++){var cb=(i>>(1-c))&1;var j=cb?i^(1<<(1-t)):i;n[j]=cadd(n[j],st[i]);}
  for(var k=0;k<4;k++)st[k]=n[k];return st;}
var SQ1=Math.SQRT1_2;
var GATES={
  H:[[C(SQ1),C(SQ1)],[C(SQ1),C(-SQ1)]],
  X:[[C(0),C(1)],[C(1),C(0)]],
  Z:[[C(1),C(0)],[C(0),C(-1)]],
  S:[[C(1),C(0)],[C(0),C(0,1)]],
  T:[[C(1),C(0)],[C(0),C(SQ1,SQ1)]]
};
function runCircuit(src){
  var st=newState();var steps=[];
  var lines=String(src).split(/[\n;]+/);
  lines.forEach(function(ln){
    var p=ln.trim().split(/\s+/);if(!p[0])return;
    var g=p[0].toUpperCase();
    if(g==='CNOT'&&p.length>=3){applyCNOT(st,+p[1],+p[2]);steps.push('CNOT '+p[1]+' '+p[2]);}
    else if(g==='RX'&&p.length>=3){var th=parseFloat(p[2]);var q=+p[1];
      apply1(st,q,[[C(Math.cos(th/2)),C(0,-Math.sin(th/2))],[C(0,-Math.sin(th/2)),C(Math.cos(th/2))]]);steps.push('RX('+th+') q'+q);}
    else if(GATES[g]&&p.length>=2){apply1(st,+p[1],GATES[g]);steps.push(g+' q'+p[1]);}
    else throw new Error('bad gate line: '+ln);
  });
  var labels=['00','01','10','11'];
  var out=['2-qubit state after '+steps.length+' gate(s): '+steps.join(', ')];
  var tot=0;
  for(var i=0;i<4;i++){var pr=cprob(st[i]);tot+=pr;
    out.push('|'+labels[i]+'>  P='+fmtN(pr)+'  amp='+fmtN(st[i].re)+((st[i].im>=0?'+':'')+fmtN(st[i].im)+'i'));}
  out.push('total probability = '+fmtN(tot)+' (must be 1)');
  return out.join('\n');
}
/* ================= virtual FS ================= */
function makeFS(){
  var F={'/':{d:1}};
  function add(p,content){F[p]={d:0,content:String(content)};}
  add('/readme.txt','QuantaOS '+"signature"+' — simulated quanta desktop.\nEvery app below genuinely runs in this page.');
  add('/notes.txt','- Grover gives quadratic speedup for unstructured search.\n- BB84 key exchange is information-theoretically secure.');
  add('/circuits/bell.txt','H 0\nCNOT 0 1');
  add('/circuits/ghz2.txt','H 0\nCNOT 0 1');
  return {
    ls:function(p){p=p||'/';var out=[];Object.keys(F).forEach(function(k){
      if(k!==p&&k.indexOf(p)===0){var rest=k.slice(p.length).replace(/^\//,'');
        var seg=rest.split('/')[0];if(seg&&out.indexOf(seg)<0)out.push(seg+(F[k].d?'/':''));}});
      return out.length?out.join('  '):'(empty)';},
    cat:function(p){if(!F[p]||F[p].d)throw new Error('no such file: '+p);return F[p].content;},
    write:function(p,c){add(p,c);return 'wrote '+c.length+' chars to '+p;}
  };
}
/* ================= app registry ================= */
var APPS={};
function defApp(id,name,icon,help,run){APPS[id]={id:id,name:name,icon:icon,help:help,run:run};}
defApp('terminal','Quanta Terminal','\u2328',
 'help | apps | echo <t> | calc <expr> | run <app> <args> | qubits | whoami | clear',
 function(input,ctx){
  var p=String(input||'').trim().split(/\s+/);var c=(p[0]||'').toLowerCase();
  if(c===''||c==='help')return 'commands: help, apps, echo <text>, calc <expr>, run <app> <args>, qubits, whoami, clear';
  if(c==='apps')return api.apps().map(function(a){return a.id+' — '+a.name;}).join('\n');
  if(c==='echo')return p.slice(1).join(' ');
  if(c==='calc'){try{return String(fmtN(evalExpr(p.slice(1).join(' '))));}catch(e){return 'calc error: '+e.message;}}
  if(c==='run'){var id=p[1];if(!APPS[id])return 'no such app: '+id;try{return APPS[id].run(p.slice(2).join(' '),ctx);}catch(e){return id+' error: '+e.message;}}
  if(c==='qubits')return 'virtual QPU: 2 simulated qubits, state-vector backend (classical simulation)';
  if(c==='whoami')return 'quanta-operator@quanta-desktop';
  if(c==='clear')return '';
  return 'unknown command: '+c+' (try help)';
 });
defApp('calc','Quanta Calculator','\u03BB',
 'Evaluate math: 2+2*2, sqrt(16), sin(pi/2), 2^10',
 function(input){ if(!String(input).trim())return 'type an expression, e.g. 2+2*2';
  try{return String(input).trim()+' = '+fmtN(evalExpr(input));}catch(e){return 'error: '+e.message;} });
defApp('circuit','Quantum Circuit Lab','\u269B',
 'One gate per line: H q | X q | Z q | S q | T q | RX q theta | CNOT c t   (2 qubits, q = 0 or 1). Real state-vector math.',
 function(input){ if(!String(input).trim())return 'enter gates, e.g.:\nH 0\nCNOT 0 1';
  try{return runCircuit(input);}catch(e){return 'circuit error: '+e.message;} });
defApp('explorer','File Explorer','\uD83D\uDDC0',
 'ls [path] | open <path>',
 function(input,ctx){var p=String(input||'').trim().split(/\s+/);
  if(p[0]==='open'&&p[1]){try{return ctx.fs.cat(p[1]);}catch(e){return e.message;}}
  return ctx.fs.ls(p[0]==='ls'?(p[1]||'/'):(p[0]||'/'));});
defApp('editor','Text Editor','\u270E',
 'open <path> | write <path> <text>',
 function(input,ctx){var s=String(input||'').trim();
  if(s.indexOf('write ')===0){var rest=s.slice(6);var sp=rest.indexOf(' ');
    if(sp<0)return 'usage: write <path> <text>';
    return ctx.fs.write(rest.slice(0,sp),rest.slice(sp+1));}
  if(s.indexOf('open ')===0){try{return ctx.fs.cat(s.slice(5).trim());}catch(e){return e.message;}}
  return 'usage: open <path> | write <path> <text>';});
var _bootT=Date.now();
defApp('monitor','System Monitor','\uD83D\uDCCA',
 'Live virtual-QPU stats (no input needed)',
 function(input,ctx){var r=sRng('mon'+Math.floor(Date.now()/4000));
  return ['virtual QPU status ('+"signature"+')',
   'qubits simulated : 2 (state-vector)',
   'jobs queued      : '+Math.floor(r()*4),
   'coherence util   : '+fmtN(80+r()*19,1)+'%',
   'cryo stage       : '+fmtN(0.012+r()*0.004,3)+' K (simulated)',
   'uptime           : '+Math.floor((Date.now()-_bootT)/1000)+' s'].join('\n');});
defApp('settings','Settings','\u2699',
 'theme dark|light | about',
 function(input){var p=String(input||'').trim().toLowerCase();
  if(p==='about')return 'QuantaOS '+"signature"+' — simulated quanta desktop running entirely in this page.';
  if(p==='theme dark'||p==='theme light')return 'theme set: '+p.split(' ')[1]+' (applies to new windows)';
  return 'usage: theme dark|light | about';});

defApp('grover','Grover Search Sim','\uD83D\uDD0D',
 'Simulate Grover unstructured search. Input: n=<size> target=<index>  (e.g. n=16 target=5)',
 function(input){var m=String(input||'').match(/n\s*=\s*(\d+).*target\s*=\s*(\d+)/);
  if(!m)return 'usage: n=<size> target=<index>  e.g. n=16 target=5';
  var N=+m[1],t=+m[2];if(t<0||t>=N)return 'target must be in [0,'+(N-1)+']';
  var iters=Math.round(Math.PI/4*Math.sqrt(N));
  var theta=Math.asin(1/Math.sqrt(N));
  var p=Math.pow(Math.sin((2*iters+1)*theta),2);
  return ['Grover search over N='+N+' items, target index '+t,
   'optimal iterations : '+iters+'  (~ (pi/4)*sqrt(N))',
   'classical expected : ~'+(N/2)+' queries',
   'success probability: '+fmtN(p,4)+' (after '+iters+' iterations)',
   'speedup: quadratic — real Grover math, classically simulated'].join('\n');});
defApp('bb84','BB84 Key Exchange','\uD83D\uDD11',
 'Simulate BB84 quantum key distribution. Input: bits=<n>  (e.g. bits=16)',
 function(input){var m=String(input||'').match(/bits\s*=\s*(\d+)/);
  var n=m?Math.min(64,Math.max(4,+m[1])):16;
  var r=sRng('bb84'+n);var abits=[],abases=[],bbases=[];
  for(var i=0;i<n;i++){abits.push(r()<0.5?0:1);abases.push(r()<0.5?0:1);bbases.push(r()<0.5?0:1);}
  var key=[];for(var j=0;j<n;j++){if(abases[j]===bbases[j])key.push(abits[j]);}
  return ['BB84 simulation: '+n+' qubits sent (seeded, reproducible)',
   'alice bits : '+abits.join(''),
   'alice bases: '+abases.join(''),
   'bob bases  : '+bbases.join(''),
   'sifted key ('+key.length+' bits): '+key.join(''),
   'matching bases kept; the rest discarded — real BB84 sifting, classically simulated'].join('\n');});
defApp('vqe','VQE Energy Demo','\u2697',
 'Variational quantum eigensolver toy: H2 molecule. Input: steps=<n> (e.g. steps=9)',
 function(input){var m=String(input||'').match(/steps\s*=\s*(\d+)/);
  var S=m?Math.min(25,Math.max(3,+m[1])):9;
  var out=['VQE toy scan: H2 ground-state energy vs ansatz angle theta'];
  var best={e:1e9,th:0};
  for(var i=0;i<S;i++){var th=-Math.PI+i*(2*Math.PI/(S-1));
    var e=-1.0-0.15*Math.cos(th); /* toy Hamiltonian E(theta) */
    if(e<best.e)best={e:e,th:th};
    out.push('theta='+fmtN(th,3)+'  E='+fmtN(e,4)+' Ha');}
  out.push('best: E='+fmtN(best.e,4)+' Ha at theta='+fmtN(best.th,3)+' (variational minimum found)');
  return out.join('\n');});

/* ================= API ================= */
var _fs=makeFS();
var api={
  edition:"signature",
  apps:function(){return Object.keys(APPS).map(function(k){return {id:k,name:APPS[k].name,icon:APPS[k].icon};});},
  help:function(id){return APPS[id]?APPS[id].help:'no such app';},
  run:function(id,input){if(!APPS[id])throw new Error('no such app: '+id);
    return APPS[id].run(input==null?'':input,{fs:_fs,api:api});}
};
/* ================= DOM ================= */
function el(tag,cls,html){var d=document.createElement(tag);if(cls)d.className=cls;if(html!=null)d.innerHTML=html;return d;}
function mount(host){
  host.innerHTML='';
  var desk=el('div','qsim-desktop');host.appendChild(desk);
  var icons=el('div','qsim-icons');desk.appendChild(icons);
  var taskbar=el('div','qsim-taskbar');desk.appendChild(taskbar);
  var zTop=10;
  function openWin(appId){
    var app=APPS[appId];if(!app)return;
    var w=el('div','qsim-win');w.style.zIndex=++zTop;
    w.style.left=(20+ (zTop*37)%220)+'px';w.style.top=(16+(zTop*29)%120)+'px';w.style.width='380px';
    var tb=el('div','tbar','<span>'+app.icon+' '+app.name+'</span><button style="padding:2px 8px">\u2715</button>');
    var body=el('div','tbody');
    var pre=el('pre','',app.help);body.appendChild(pre);
    var row=el('div','row');var inp=document.createElement('input');
    inp.style.flex='1';inp.placeholder='type input, Enter to run';row.appendChild(inp);
    var go=el('button','go','Run');row.appendChild(go);body.appendChild(row);
    w.appendChild(tb);w.appendChild(body);desk.appendChild(w);
    var fs=makeFS();
    function runIt(){var v=inp.value;inp.value='';
      var out=el('div');out.innerHTML='<div class="dim">&gt; '+String(v).replace(/[<>&]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;'}[c];})+'</div>';
      body.insertBefore(out,row);
      try{var r=app.run(v,{fs:fs,api:api});var o=el('pre','',String(r).replace(/[<>&]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;'}[c];}));body.insertBefore(o,row);}
      catch(e){var er=el('div','bad','error: '+e.message);body.insertBefore(er,row);}
      body.scrollTop=body.scrollHeight;}
    go.addEventListener('click',runIt);
    inp.addEventListener('keydown',function(e){if(e.key==='Enter')runIt();});
    tb.querySelector('button').addEventListener('click',function(){w.remove();});
    tb.addEventListener('mousedown',function(e){if(e.target.tagName==='BUTTON')return;
      var sx=e.clientX-w.offsetLeft,sy=e.clientY-w.offsetTop;
      function mv(ev){w.style.left=(ev.clientX-sx)+'px';w.style.top=Math.max(0,ev.clientY-sy)+'px';}
      function up(){document.removeEventListener('mousemove',mv);document.removeEventListener('mouseup',up);}
      document.addEventListener('mousemove',mv);document.addEventListener('mouseup',up);});
    w.addEventListener('mousedown',function(){w.style.zIndex=++zTop;});
    if(appId==='monitor'){var iv=setInterval(function(){if(!w.isConnected){clearInterval(iv);return;}
      try{pre.textContent=app.run('',{fs:fs,api:api});}catch(e){}},4000);}
  }
  api.apps().forEach(function(a){
    var ic=el('div','qsim-icon','<span class="g">'+a.icon+'</span>'+a.name);
    ic.addEventListener('click',function(){openWin(a.id);});
    icons.appendChild(ic);});
  var clock=el('span','dim','QuantaOS '+"signature");
  taskbar.appendChild(clock);
  var time=el('span','dim','');taskbar.appendChild(time);
  setInterval(function(){var d=new Date();time.textContent=d.toLocaleTimeString();},1000);
  return {openWin:openWin};
}
return {api:api,mount:mount,APPS:APPS};
})();

var gen={version:'jahdb-quanta-computer-apps-database-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,selfReg:SELF_REG};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quanta-computer-apps-database-signature',gen);
if(typeof window!=='undefined'&&typeof QuantaSim!=='undefined'){window.QuantaSim=QuantaSim;}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;if(typeof QuantaSim!=='undefined'){module.exports.QuantaSim=QuantaSim;}}
})();
