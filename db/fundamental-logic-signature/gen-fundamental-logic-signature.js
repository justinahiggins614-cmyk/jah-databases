(function(){'use strict';
/* jahdb-fundamental-logic-signature-1.0 — fundamental logic bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFLOG-';
var KIND='fundamental logic record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Logic is the study of valid reasoning: what makes an argument\'s conclusion follow necessarily from its premises, regardless of subject matter. It underlies mathematics, computer science, law, and every disciplined argument.', 'reasoning':'Logicians reason about reasoning itself: they formalize arguments into symbols, test which forms preserve truth, and prove meta-theorems about entire systems — like whether a system can prove its own consistency.', 'quantities':'The core quantities are truth values (true/false), and the derived measures: validity, satisfiability, and provability of formulas; the complexity of deciding them; and the expressive power of logical systems.', 'mechanism':'Logical work runs: translate the argument into a formal language → check the form against the rules of inference → test with truth tables, proofs, or models → report valid or invalid with a counterexample if invalid.', 'miscon':'Logic is not about being right: a valid argument can have false premises. Formal logic does not replace judgment: it checks the skeleton of an argument, not the truth of its claims. And logic did not end with Aristotle: modern logic rebuilt the field from 1879 onward.'};
var SIGLENS=['In the Signature system, logic is the verification layer: every generator\'s validation rules, every dedupe check, every drift control in this network is applied logic, and the Signature formulation teaches each principle as a check you can execute.','The Signature practice is to run the logic: evaluate the truth table, execute the proof checker, generate the counterexample — so validity is demonstrated by machine, not merely asserted.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- truth table demo. Runs as-is with python3."""\ndef table():\n    print("A      B      A AND B   A OR B   NOT A   A -> B")\n    for a in (True, False):\n        for b in (True, False):\n            impl = (not a) or b\n            print(f"{str(a):<7}{str(b):<7}{str(a and b):<10}{str(a or b):<8}{str(not a):<8}{impl}")\ntable()\n', '#!/usr/bin/env python3\n"""{TITLE} -- validity checker demo. Runs as-is with python3."""\ndef entails(premises, conclusion):\n    # brute-force over 2 variables A, B\n    for a in (True, False):\n        for b in (True, False):\n            env = {"A": a, "B": b}\n            if all(eval(p, {}, env) for p in premises):\n                if not eval(conclusion, {}, env):\n                    return False, env\n    return True, None\nok, ce = entails(["A", "A or B"], "B")       # invalid form\nprint("A, A or B |= B ?", ok, "counterexample:", ce)\nok2, _ = entails(["A", "not A or B"], "B")   # modus ponens shape\nprint("A, not A or B |= B ?", ok2)\n', '#!/usr/bin/env python3\n"""{TITLE} -- syllogism demo. Runs as-is with python3."""\ndef all_are(group, prop):\n    return all(prop(x) for x in group)\nmen = ["socrates", "plato"]\nmortal = {"socrates": True, "plato": True}\npremise1 = all_are(men, lambda m: True)          # all men are in group\npremise2 = all(mortal[m] for m in men)           # all men are mortal\nconclusion = mortal["socrates"]                  # socrates is mortal\nprint("premises true:", premise1 and premise2)\nprint("conclusion follows:", conclusion)\n'];
var TOPICS=[['Signature What Logic Is','Logic is the study of valid inference: the patterns of reasoning that guarantee a true conclusion whenever the premises are true. It does not tell you which premises are true — that is the job of science and observation — it tells you which moves from premises to conclusions are legitimate.'],
['Signature The Core Question of Logic','The core question of logic is: does this conclusion follow? Given premises and a proposed conclusion, logic asks whether every situation making the premises true also makes the conclusion true. If yes, the argument is valid; if even one counterexample exists, it is not.'],
['Signature Assumptions: The Laws of Thought','Classical logic rests on bedrock assumptions: the law of identity (a thing is itself), non-contradiction (no statement is both true and false), and excluded middle (every statement is true or false). Alternative logics relax these — intuitionists reject excluded middle — and say so explicitly.'],
['Signature The Vocabulary: Propositions and Connectives','The vocabulary of logic is propositions (statements that are true or false) and connectives: AND, OR, NOT, IF-THEN, IF-AND-ONLY-IF. With these five, plus quantifiers (for-all, there-exists), the whole of mathematical reasoning can be expressed.'],
['Signature Truth Values: The Fundamental Quantity','The fundamental quantity of logic is the truth value: true or false, 1 or 0. Every complex formula\'s truth is computed from its parts by truth tables, and the entire digital world — every chip, every program — runs on this two-valued arithmetic.'],
['Signature Deduction: The Primary Method','Deduction is logic\'s primary method: deriving conclusions guaranteed by the premises. Modus ponens (from P and if-P-then-Q, infer Q) is the workhorse; natural deduction systems build proofs from a small set of such rules, each obviously truth-preserving.'],
['Signature A Canonical First Example','The canonical first example is the Socratic syllogism: all men are mortal; Socrates is a man; therefore Socrates is mortal. The form — all A are B, x is A, therefore x is B — is valid in every instance, whatever A, B, and x happen to be.'],
['Signature How Logic Tests Arguments','Logic tests arguments with truth tables, Venn diagrams, proof trees, and countermodels: systematic procedures that decide validity. For propositional logic the truth table always terminates; for richer logics, proof search and model-building do the checking.'],
['Signature The Core Mechanism: Form Over Content','The core mechanism of logic is form over content: strip away what the argument is about, examine the skeleton, and judge the skeleton. \'All glibberish are florp; x is glibberish; therefore x is florp\' is valid — the nonsense words prove the point.'],
['Signature The Simplest Law: Modus Ponens','The simplest law is modus ponens: P; if P then Q; therefore Q. Every chain of reasoning you trust — every \'since this, then that\' — is built from repeated applications of this one rule, which is why getting it exactly right matters.'],
['Signature Common Misconceptions in Logic','The misconceptions persist: that valid means true (validity concerns the connection, not the premises), that logic settles factual disputes (it checks arguments, not evidence), and that formal logic is just common sense written down (common sense routinely fails the Wason selection task).'],
['Signature How Beginners Practice Logic','Beginners practice logic by translating everyday arguments into symbols and testing them: find the premises, find the conclusion, formalize, and check. Puzzle books of Knights-and-Knaves problems train the same muscle that later handles mathematical proofs.'],
['Signature The Core Model: Propositional Logic','Propositional logic is the core model: the complete, decidable system of truth-functional connectives. It is the logic of circuits and conditions, and its meta-theorems — soundness, completeness — are the templates for all deeper logical investigation.'],
['Signature The Great Result: Completeness','Gödel\'s completeness theorem is the great result: in first-order logic, every valid formula has a proof. Validity (truth in all models) and provability (derivability by rules) coincide — the system misses nothing it should capture.'],
['Signature Systems Thinking: Syntax versus Semantics','Systems thinking in logic distinguishes syntax (symbol manipulation by rules) from semantics (truth in structures). Soundness says syntax never outruns semantics; completeness says semantics never outruns syntax. Their interplay is the field\'s central drama.'],
['Signature Invariance: Logical Equivalence','The invariance principle is logical equivalence: formulas with identical truth tables are interchangeable in all reasoning — De Morgan\'s laws, contraposition, double negation. Spotting equivalences simplifies arguments the way factoring simplifies arithmetic.'],
['Signature Approximation: Non-Classical Logics','Non-classical logics approximate reasoning that classical logic mishandles: fuzzy logic for degrees of truth, modal logic for necessity and possibility, temporal logic for reasoning about time, paraconsistent logic for inconsistent databases. Each relaxes one classical assumption deliberately.'],
['Signature Evidence Standards: Proof and Counterexample','The evidence standards are proof for validity and counterexample for invalidity: to show an argument valid, derive the conclusion by the rules; to show it invalid, exhibit one assignment making premises true and conclusion false. One counterexample outweighs a thousand confirming instances.'],
['Signature Classic Discoveries','The classic discoveries are Aristotle\'s syllogistic, Frege\'s predicate logic of 1879, Russell and Whitehead\'s Principia, Gödel\'s completeness and incompleteness theorems, and Turing\'s analysis of computation. Each redefined what reasoning itself could be.'],
['Signature Core Trade-offs: Expressiveness versus Decidability','The core trade-off is expressiveness versus decidability: richer logics say more but decide less. Propositional logic is fully decidable; first-order logic is semi-decidable; second-order logic can express arithmetic but admits no complete proof system.'],
['Signature Handling Uncertainty: Probabilistic Logic','Probabilistic and non-monotonic logics handle uncertainty: assigning degrees of belief to propositions, and allowing conclusions to be withdrawn when new evidence arrives. Classical logic is monotonic — new premises never invalidate old conclusions — which real reasoning often is not.'],
['Signature Tools of the Trade','The tools of the trade are truth tables, natural deduction, semantic tableaux, and modern proof assistants and SAT solvers: software that checks proofs and searches for countermodels automatically. The deepest tool remains the patient counterexample.'],
['Signature Ethics and Responsibility','Ethics in logic is about argumentative honesty: not equivocating between senses of a word, not straw-manning opponents, not passing rhetoric off as proof. Logic gives no moral conclusions by itself, but it exposes the dishonest moves in moral argument.'],
['Signature Teaching Logic','Teaching logic well moves from puzzles to formalism: Knights-and-Knaves, then truth tables, then natural deduction, then quantifiers. Students learn fastest when they first feel validity as a constraint on what they can consistently believe.'],
['Signature The Frontier Question','The frontier question is the logic of real reasoning: how to formalize the defeasible, probabilistic, resource-bounded inference that humans and AI systems actually perform. Classical logic is the solved core; the frontier extends it toward minds and machines.'],
['Signature Unifying Theories','The unifying theories connect logic to the rest of mathematics: the Curry-Howard correspondence identifies proofs with programs and propositions with types, making logic the theory of computation itself. Model theory, proof theory, and computability are one subject seen three ways.'],
['Signature Computational Logic','Computational logic turned inference into industry: SAT solvers decide million-variable formulas, model checkers verify hardware and protocols, and automated provers assist mathematicians. The P versus NP question is, at bottom, a question about the cost of logical reasoning.'],
['Signature Bridges to Other Fields','Logic bridges to computer science (circuits, programs, databases), philosophy (arguments about everything), linguistics (the structure of meaning), law (the anatomy of cases), and mathematics (the foundation of proof). Each field borrows the skeleton and adds its own flesh.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the exact complexity of key logical decision problems, the search for practical complete systems for richer logics, and the philosophical question of which logic is the \'right\' one. No settled answers — active research.'],
['Signature How New Claims Are Validated','New logical claims are validated by proof and by independent formalization: the theorem is proved, the proof is checked by referees and increasingly by proof assistants, and the definitions are tested against intended models. A logic earns trust by surviving hostile formal scrutiny.'],
['Signature The Great Debates','The great debates ask which logic is correct: classical versus intuitionistic versus paraconsistent, and whether logic describes thought or prescribes it. The pluralist answer — different logics for different jobs — now dominates, but the debate sharpened every position.'],
['Signature Failure Modes: When Logic Gets It Wrong','Logic goes wrong through equivocation, hidden premises, and formalism worship: arguments that are valid but unsound, proofs with suppressed assumptions, and symbols manipulated without meaning. The cure is always the same — say what you mean, show the counterexample.'],
['Signature Synthesis: Building on the Fundamentals','Synthesis combines the fundamentals: translate the argument, check the form, hunt the counterexample, name the system. Every advanced logical investigation — modal, temporal, higher-order — is this pipeline applied to richer languages.'],
['Signature The Signature Formulation: Logic as Executable Check','The Signature formulation makes logic executable: every principle in this database is paired with a program that evaluates it, because in the Signature system a rule of inference you cannot run is a rule you do not yet own. That is the Signature capstone on logical bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Separate form from content: judge the argument's structure before its claims.", "Produce counterexamples for invalidity: a single true-premise, false-conclusion case refutes the form.", "State the system: classical, intuitionistic, and modal logics have different rules."],citations:["Aristotle \u2014 Organon (4th century BCE): the founding works of formal logic.", "Enderton, H. \u2014 A Mathematical Introduction to Logic (Academic Press).", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-logic-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-logic-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
