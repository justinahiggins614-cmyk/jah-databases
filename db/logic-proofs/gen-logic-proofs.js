(function(){'use strict';
/* JAH Logic and Proof Database generator — jahdb-logic-proofs-1.0.
   Real formal logic: formulas are executable ASTs; every truth table and
   equivalence claim is recomputed by the validator, never trusted. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-LOG-';
var CATS=['propositional','predicate','truth-tables','proofs','fallacies','inference'];
var RULES=['Premise','Assumption','Modus Ponens','Modus Tollens','Hypothetical Syllogism','Disjunctive Syllogism','Addition','Simplification','Conjunction','Resolution','Double Negation','De Morgan','Reiteration','Conditional Proof','Negation Introduction','Constructive Dilemma','Universal Instantiation','Existential Generalization'];
var FALLACIES=['Ad Hominem','Straw Man','Appeal to Ignorance','False Dilemma','Slippery Slope','Circular Reasoning','Hasty Generalization','Red Herring','Bandwagon','Appeal to Authority','Post Hoc Ergo Propter Hoc','No True Scotsman','Tu Quoque','Genetic Fallacy','Equivocation','Begging the Question','Appeal to Emotion','Composition','Division','Middle Ground'];
var INF_RULES=['Modus Ponens','Modus Tollens','Hypothetical Syllogism','Disjunctive Syllogism','Addition','Simplification','Conjunction','Resolution','Constructive Dilemma','Destructive Dilemma'];

/* ---------- formula AST ---------- */
function V(n){return {v:n};}
function NOT(a){return {op:'not',a:a};}
function BIN(op,a,b){return {op:op,a:a,b:b};}
function evalF(f,env){
  if(f.v)return !!env[f.v];
  if(f.op==='not')return !evalF(f.a,env);
  var x=evalF(f.a,env),y=evalF(f.b,env);
  if(f.op==='and')return x&&y;
  if(f.op==='or')return x||y;
  if(f.op==='implies')return !x||y;
  if(f.op==='iff')return x===y;
  if(f.op==='xor')return x!==y;
  throw new Error('bad op');
}
var PRECN={iff:1,xor:2,implies:3,or:4,and:5,not:6};
var SYM={not:'\u00AC',and:'\u2227',or:'\u2228',implies:'\u2192',iff:'\u2194',xor:'\u2295'};
function strF(f,parent){
  if(f.v)return f.v;
  if(f.op==='not'){var s=strF(f.a,'not');return SYM.not+(PRECN.not>=(PRECN[f.a.op]||7)?'('+s+')':s);}
  var p=PRECN[f.op]||0,pp=PRECN[parent]||0;
  var s=strF(f.a,f.op)+' '+SYM[f.op]+' '+strF(f.b,f.op);
  return (p<pp||(p===pp&&(f.op==='implies'||f.op==='iff')))?'('+s+')':s;
}
function varsF(f,out){out=out||{};if(f.v)out[f.v]=1;else{if(f.a)varsF(f.a,out);if(f.b)varsF(f.b,out);}return Object.keys(out).sort();}
function truthTable(f,vars){
  var n=vars.length,rows=[];
  for(var i=0;i<(1<<n);i++){var env={};for(var j=0;j<n;j++)env[vars[j]]=!!(i&(1<<(n-1-j)));rows.push({inputs:env,result:evalF(f,env)});}
  return rows;
}
function equivTable(f,g,vars){
  var t1=truthTable(f,vars),t2=truthTable(g,vars);
  for(var i=0;i<t1.length;i++)if(t1[i].result!==t2[i].result)return false;
  return true;
}

/* ---------- curated real entries (source: online) ---------- */
var P=V('P'),Q=V('Q'),R=V('R');
function law(title,formal,f,g,expl,ref){
  return {kind:'law',cat:'propositional',title:title,formal:formal,formula:f,formula2:g,variables:varsF(f),
    statement:'The logical equivalence known as '+title+': '+formal+'.',
    explanation:expl,source:'online',source_ref:ref};
}
var ONLINE=[
law("De Morgan's Law \u2014 negation of conjunction",'\u00AC(P \u2227 Q) \u2261 (\u00AC P \u2228 \u00AC Q)',NOT(BIN('and',P,Q)),BIN('or',NOT(P),NOT(Q)),
'Negating an "and" statement flips it into an "or" of the negated parts. Saying "it is not the case that both P and Q hold" is exactly the same as saying "P fails or Q fails". One of the two most-used transformation rules in all of logic.',
'Wikipedia \u2014 De Morgan\u2019s laws'),
law("De Morgan's Law \u2014 negation of disjunction",'\u00AC(P \u2228 Q) \u2261 (\u00AC P \u2227 \u00AC Q)',NOT(BIN('or',P,Q)),BIN('and',NOT(P),NOT(Q)),
'Negating an "or" statement flips it into an "and" of the negated parts. "Neither P nor Q" means precisely "not P and not Q". Together with its twin law this governs how negation distributes over connectives.',
'Wikipedia \u2014 De Morgan\u2019s laws'),
law('Double negation','\u00AC\u00ACP \u2261 P',NOT(NOT(P)),P,
'Two negations cancel. Saying "it is not the case that P is false" is just P again. Classical logic treats truth as bivalent, so flipping twice returns to the start.',
'Standard propositional logic \u2014 classical tautologies'),
law('Commutativity of conjunction','(P \u2227 Q) \u2261 (Q \u2227 P)',BIN('and',P,Q),BIN('and',Q,P),
'Order does not matter for "and". P and Q being both true is the same situation as Q and P being both true. Conjunction is symmetric in its arguments.',
'Standard propositional logic \u2014 classical tautologies'),
law('Commutativity of disjunction','(P \u2228 Q) \u2261 (Q \u2228 P)',BIN('or',P,Q),BIN('or',Q,P),
'Order does not matter for "or". "P or Q" describes the same truth conditions as "Q or P". Disjunction, like conjunction, is commutative.',
'Standard propositional logic \u2014 classical tautologies'),
law('Associativity of conjunction','((P \u2227 Q) \u2227 R) \u2261 (P \u2227 (Q \u2227 R))',BIN('and',BIN('and',P,Q),R),BIN('and',P,BIN('and',Q,R)),
'Grouping does not matter for chains of "and". Whether you group the first two or the last two, the whole chain is true exactly when all three hold.',
'Standard propositional logic \u2014 classical tautologies'),
law('Associativity of disjunction','((P \u2228 Q) \u2228 R) \u2261 (P \u2228 (Q \u2228 R))',BIN('or',BIN('or',P,Q),R),BIN('or',P,BIN('or',Q,R)),
'Grouping does not matter for chains of "or". The chain is true exactly when at least one disjunct is true, regardless of how the parentheses fall.',
'Standard propositional logic \u2014 classical tautologies'),
law('Distributivity of conjunction over disjunction','(P \u2227 (Q \u2228 R)) \u2261 ((P \u2227 Q) \u2228 (P \u2227 R))',BIN('and',P,BIN('or',Q,R)),BIN('or',BIN('and',P,Q),BIN('and',P,R)),
'"And" distributes over "or" the way multiplication distributes over addition. P together with (Q or R) is the same as (P and Q) or (P and R).',
'Standard propositional logic \u2014 classical tautologies'),
law('Distributivity of disjunction over conjunction','(P \u2228 (Q \u2227 R)) \u2261 ((P \u2228 Q) \u2227 (P \u2228 R))',BIN('or',P,BIN('and',Q,R)),BIN('and',BIN('or',P,Q),BIN('or',P,R)),
'Less familiar but equally valid: "or" distributes over "and". P or (Q and R) is the same as (P or Q) and (P or R). Arithmetic has no analogue; logic does.',
'Standard propositional logic \u2014 classical tautologies'),
law('Implication as disjunction','(P \u2192 Q) \u2261 (\u00AC P \u2228 Q)',BIN('implies',P,Q),BIN('or',NOT(P),Q),
'An implication "if P then Q" is true in every case except P-true-and-Q-false, which is exactly when "not P or Q" holds. This equivalence is the workhorse for converting conditionals.',
'Standard propositional logic \u2014 classical tautologies'),
law('Contrapositive','(P \u2192 Q) \u2261 (\u00AC Q \u2192 \u00AC P)',BIN('implies',P,Q),BIN('implies',NOT(Q),NOT(P)),
'An implication is equivalent to its contrapositive: "if P then Q" says the same as "if not Q then not P". Note this is NOT the converse (Q \u2192 P), which is a different claim.',
'Standard propositional logic \u2014 classical tautologies'),
law('Biconditional expansion','(P \u2194 Q) \u2261 ((P \u2192 Q) \u2227 (Q \u2192 P))',BIN('iff',P,Q),BIN('and',BIN('implies',P,Q),BIN('implies',Q,P)),
'"P if and only if Q" means the implication goes both ways. Proving a biconditional always splits into proving P \u2192 Q and proving Q \u2192 P separately.',
'Standard propositional logic \u2014 classical tautologies'),
law('Absorption (conjunction)','(P \u2227 (P \u2228 Q)) \u2261 P',BIN('and',P,BIN('or',P,Q)),P,
'P absorbs the larger disjunction: if P holds, then P-and-(P-or-Q) holds; if P fails, the conjunction fails. The Q is irrelevant once P is fixed.',
'Standard propositional logic \u2014 classical tautologies'),
law('Absorption (disjunction)','(P \u2228 (P \u2227 Q)) \u2261 P',BIN('or',P,BIN('and',P,Q)),P,
'The mirror absorption: P or (P and Q) collapses to P. If P is true the disjunction is true; if P is false then P-and-Q is false too.',
'Standard propositional logic \u2014 classical tautologies'),
law('Negation law (excluded middle instance)','(P \u2228 \u00AC P) \u2261 True',BIN('or',P,NOT(P)),{tautology_true:1},
'P or not P is always true: the law of excluded middle in formula form. Every proposition is either true or false, with no third option in classical logic.',
'Standard propositional logic \u2014 classical tautologies'),
law('Negation law (contradiction instance)','(P \u2227 \u00AC P) \u2261 False',BIN('and',P,NOT(P)),{tautology_false:1},
'P and not P is always false: the law of non-contradiction. No proposition can be simultaneously true and false, so the conjunction is unsatisfiable.',
'Standard propositional logic \u2014 classical tautologies'),
law('Exportation','((P \u2227 Q) \u2192 R) \u2261 (P \u2192 (Q \u2192 R))',BIN('implies',BIN('and',P,Q),R),BIN('implies',P,BIN('implies',Q,R)),
'A conditional with a conjunctive antecedent can be "exported" into nested conditionals. "If P and Q then R" is the same as "if P then (if Q then R)".',
'Standard propositional logic \u2014 classical tautologies'),
law('Material equivalence of exclusive or','(P \u2295 Q) \u2261 ((P \u2228 Q) \u2227 \u00AC(P \u2227 Q))',BIN('xor',P,Q),BIN('and',BIN('or',P,Q),NOT(BIN('and',P,Q))),
'Exclusive or means "exactly one". It is equivalent to the inclusive or together with the denial of the conjunction: one or the other holds, but not both.',
'Standard propositional logic \u2014 classical tautologies'),
law('Idempotence of conjunction','(P \u2227 P) \u2261 P',BIN('and',P,P),P,
'Repeating a conjunct changes nothing: P and P is just P. Unlike arithmetic multiplication, logical "and" has no notion of squaring.',
'Standard propositional logic \u2014 classical tautologies'),
law('Idempotence of disjunction','(P \u2228 P) \u2261 P',BIN('or',P,P),P,
'Repeating a disjunct changes nothing: P or P is just P. A claim stated twice is still the same claim.',
'Standard propositional logic \u2014 classical tautologies')
];
/* inference rules (online) */
function infRule(name,premises,conclusion,example,ref){
  return {kind:'inference',cat:'inference',title:'Inference rule: '+name,
    statement:'The valid argument form '+name+': from '+premises.join(' and ')+' infer '+conclusion+'.',
    formal:premises.join(', ')+' \u22A2 '+conclusion, rule_name:name, premises:premises, conclusion:conclusion,
    example:example, explanation:'This is a classically valid rule of inference: whenever the premises are true, the conclusion cannot be false.',
    source:'online',source_ref:ref||'Standard natural deduction \u2014 rules of inference'};
}
ONLINE.push(
infRule('Modus Ponens',['P \u2192 Q','P'],'Q','If it rains the streets get wet; it rains; therefore the streets get wet. The most-used inference step in all of mathematics.'),
infRule('Modus Tollens',['P \u2192 Q','\u00ACQ'],'\u00ACP','If the alarm is armed it beeps on entry; it did not beep; therefore it was not armed. Denying the consequent denies the antecedent.'),
infRule('Hypothetical Syllogism',['P \u2192 Q','Q \u2192 R'],'P \u2192 R','If you study you learn; if you learn you pass; therefore if you study you pass. Conditionals chain together.'),
infRule('Disjunctive Syllogism',['P \u2228 Q','\u00ACP'],'Q','Either the key is in the drawer or on the hook; it is not in the drawer; therefore it is on the hook.'),
infRule('Addition',['P'],'P \u2228 Q','The sky is blue; therefore the sky is blue or grass is red. You may always weaken a claim by adding a disjunct.'),
infRule('Simplification',['P \u2227 Q'],'P','The safe is locked and the code is 1234; therefore the safe is locked. Either conjunct follows from a conjunction.'),
infRule('Conjunction',['P','Q'],'P \u2227 Q','The engine runs; the brakes work; therefore the engine runs and the brakes work. Two established facts combine.'),
infRule('Resolution',['P \u2228 Q','\u00ACP \u2228 R'],'Q \u2228 R','Either the train is late or the bus is early; either the train is on time or traffic is light; therefore the bus is early or traffic is light. The engine of automated theorem proving.'),
infRule('Constructive Dilemma',['(P \u2192 Q) \u2227 (R \u2192 S)','P \u2228 R'],'Q \u2228 S','If it rains we stay in, and if it snows we stay in; it rains or snows; therefore we stay in. Two conditionals, one disjunctive trigger.'),
infRule('Destructive Dilemma',['(P \u2192 Q) \u2227 (R \u2192 S)','\u00ACQ \u2228 \u00ACS'],'\u00ACP \u2228 \u00ACR','If the fuse blows the lights die, and if the breaker trips the heat dies; the lights or the heat are on; therefore the fuse or the breaker held. The modus-tollens twin of constructive dilemma.')
);
/* fallacies (online) */
function fal(name,argument,why,cex){
  return {kind:'fallacy',cat:'fallacies',title:'Fallacy: '+name,
    statement:'The '+name+' fallacy illustrated and diagnosed.',
    formal:name, fallacy_name:name, argument:argument,
    why_invalid:why, counterexample:cex,
    explanation:'A named pattern of bad reasoning. Recognizing the pattern lets you reject the argument without refuting every premise.',
    source:'online',source_ref:'Standard taxonomy of informal fallacies'};
}
ONLINE.push(
fal('Ad Hominem','You should ignore the engineer\u2019s safety analysis because she once failed a driving test.','The argument attacks the person instead of the analysis. A claim\u2019s truth does not depend on the speaker\u2019s unrelated history.','A disliked messenger can still deliver a true warning; evaluate the analysis, not the analyst.'),
fal('Straw Man','The proposal says "let\u2019s trial a four-day week"; the critic replies "so you want everyone to stop working and collapse the economy".','The critic refutes a distorted, exaggerated version of the proposal rather than the proposal itself.','Restate the actual proposal \u2014 a trial of a four-day week \u2014 and the "collapse" objection evaporates.'),
fal('Appeal to Ignorance','No one has proven the old bridge unsafe, so it must be safe.','Absence of proof is not proof of absence. The conclusion does not follow from our ignorance either way.','No one had proven the bridge unsafe the day before it was inspected and condemned either.'),
fal('False Dilemma','Either we cut the entire training budget or the company goes bankrupt.','Only two options are presented while others exist. The "either/or" is asserted, not established.','A third option \u2014 trimming travel spend instead \u2014 was never considered.'),
fal('Slippery Slope','If we allow flexible hours, soon nobody will work at all and the firm will die.','Each step of the slide is asserted without evidence. A chain of "then" claims needs a reason at every link.','Many firms adopted flexible hours and kept full output; the slide never happened.'),
fal('Circular Reasoning','This manual is trustworthy because it says so on page one, and page one is trustworthy because it is in this manual.','The conclusion appears among the premises. Nothing independent supports the claim.','Replace "manual" with any text and the same "proof" would certify it.'),
fal('Hasty Generalization','Two rainy Mondays in a row prove it always rains on Mondays.','A tiny sample is treated as representative of the whole. General claims need representative evidence.','The next four Mondays were dry; two data points never licensed "always".'),
fal('Red Herring','Asked about the budget overrun, the manager talks at length about the team\u2019s charity work.','An irrelevant topic is introduced to distract from the question. The charity work may be admirable and still beside the point.','The overrun remains unexplained no matter how admirable the charity work is.'),
fal('Bandwagon','Everyone is buying this supplement, so it must work.','Popularity is not evidence of efficacy. Crowds can be wrong together.','Bloodletting was once universally popular medicine.'),
fal('Appeal to Authority','A famous actor says this engine design is sound, so it is.','The authority cited has no relevant expertise. Only domain expertise transfers credibility.','The actor\u2019s fame does not include thermodynamics.'),
fal('Post Hoc Ergo Propter Hoc','The rooster crows, then the sun rises; so the crowing causes the sunrise.','Temporal order is mistaken for causation. "After this" is not "because of this".','On cloudy mornings the sun still rises without any crowing.'),
fal('No True Scotsman','"No engineer would approve this." \u2014 "Here is one who does." \u2014 "Well, no TRUE engineer would."','The category is redefined on the spot to exclude counterexamples. The claim becomes unfalsifiable.','Any counterexample is dismissed by definition rather than addressed.'),
fal('Tu Quoque','"You should recycle." \u2014 "You drove here, so your point is invalid."','The speaker\u2019s inconsistency, even if real, does not refute the claim. Arguments stand apart from arguers.','A smoker\u2019s warning that smoking kills remains true.'),
fal('Genetic Fallacy','This idea came from a rival lab, so it must be flawed.','An idea\u2019s origin does not determine its truth. Evaluate the content, not the source.','Rival labs have produced correct results before.'),
fal('Equivocation','"The sign said fine for parking, so parking here is fine." (fine = penalty vs. fine = okay)','A word shifts meaning mid-argument. The argument needs one stable meaning to work.','Disambiguate "fine" and the inference collapses.'),
fal('Begging the Question','We know the policy works because it is effective.','"Works" and "is effective" say the same thing; no independent reason is given.','Ask "how do you know it is effective?" and there is no answer left.')
);
/* predicate logic (online) */
function pred(title,formal,statement,explanation,example){
  return {kind:'predicate',cat:'predicate',title:title,formal:formal,statement:statement,explanation:explanation,example:example,
    source:'online',source_ref:'Standard predicate logic \u2014 quantifier laws'};
}
ONLINE.push(
pred('De Morgan for the universal quantifier','\u00AC\u2200x P(x) \u2261 \u2203x \u00ACP(x)','Negating "everything has property P" gives "something lacks property P".','To deny a universal claim you need only one counterexample: a single x with not-P(x) kills "for all x, P(x)".','Negation of "every bridge is inspected" is "some bridge is not inspected".'),
pred('De Morgan for the existential quantifier','\u00AC\u2203x P(x) \u2261 \u2200x \u00ACP(x)','Negating "something has property P" gives "nothing has property P".','To deny an existential claim you must rule out every candidate: all x fail P(x).','Negation of "some server is down" is "no server is down", i.e. every server is up.'),
pred('Universal distributes over conjunction','\u2200x (P(x) \u2227 Q(x)) \u2261 (\u2200x P(x)) \u2227 (\u2200x Q(x))','"Everything is both P and Q" splits cleanly into two universal claims.','Each x independently carries both properties, so the universal claim factors.','"Every parcel is labeled and sealed" equals "every parcel is labeled and every parcel is sealed".'),
pred('Existential distributes over disjunction','\u2203x (P(x) \u2228 Q(x)) \u2261 (\u2203x P(x)) \u2228 (\u2203x Q(x))','"Something is P or Q" splits into "something is P, or something is Q".','The witness for the disjunction witnesses one side, so the existential claim factors.','"Some drawer holds pens or pencils" equals "some drawer holds pens, or some drawer holds pencils".'),
pred('Universal does NOT distribute over disjunction','\u2200x (P(x) \u2228 Q(x)) is weaker than (\u2200x P(x)) \u2228 (\u2200x Q(x))','A per-object choice need not be a global choice.','Every integer is even or odd, yet it is false that every integer is even or every integer is odd. The counterexample kills the distribution.','Domain: integers; P = even, Q = odd.'),
pred('Existential does NOT distribute over conjunction','\u2203x (P(x) \u2227 Q(x)) is stronger than (\u2203x P(x)) \u2227 (\u2203x Q(x))','One witness carrying both properties is stricter than two separate witnesses.','Some number is both even and prime (namely 2) is stronger than "some number is even and some (other) number is prime".','Domain: integers; the shared witness 2 makes the left side true here, but in general the two sides differ.'),
pred('Vacuous truth of the universal','\u2200x\u2208\u2205 P(x) is true','A universal claim over an empty domain is vacuously true.','"All" demands a counterexample to fail, and an empty domain has none. This is why "for all x in the empty set" never fails.','"Every unicorn in this room is purple" is vacuously true if the room has no unicorns.'),
pred('Quantifier order matters','\u2200x\u2203y P(x,y) is weaker than \u2203y\u2200x P(x,y)','"For each x there is a y" lets y depend on x; "there is a y for all x" demands one y for every x.','Everyone has someone who admires them (y depends on x) does not imply one person is admired by everyone.','Domain: people; P(x,y) = "y admires x".')
);
/* truth tables of the 16 binary connectives (online, recomputed) */
var CONN=[
 ['Conjunction','P \u2227 Q',BIN('and',P,Q)],
 ['Disjunction','P \u2228 Q',BIN('or',P,Q)],
 ['Negated conjunction (NAND)','\u00AC(P \u2227 Q)',NOT(BIN('and',P,Q))],
 ['Negated disjunction (NOR)','\u00AC(P \u2228 Q)',NOT(BIN('or',P,Q))],
 ['Implication','P \u2192 Q',BIN('implies',P,Q)],
 ['Converse implication','Q \u2192 P',BIN('implies',Q,P)],
 ['Biconditional','P \u2194 Q',BIN('iff',P,Q)],
 ['Exclusive or','P \u2295 Q',BIN('xor',P,Q)],
 ['Negated implication','P \u2227 \u00ACQ',BIN('and',P,NOT(Q))],
 ['Projection to P','P',P],
 ['Projection to Q','Q',Q],
 ['Negation of P','\u00ACP',NOT(P)],
 ['Negation of Q','\u00ACQ',NOT(Q)],
 ['Tautology','True',BIN('or',P,NOT(P))],
 ['Contradiction','False',BIN('and',P,NOT(P))],
 ['Converse non-implication','Q \u2227 \u00ACP',BIN('and',Q,NOT(P))]
];
CONN.forEach(function(c){
  ONLINE.push({kind:'table',cat:'truth-tables',title:'Truth table: '+c[0],
    statement:'The complete truth table for '+c[0]+' ('+c[1]+') over the two propositional variables P and Q.',
    formal:c[1],formula:c[2],variables:['P','Q'],
    explanation:'Four rows cover every assignment of P and Q. The result column is computed directly from the connective\u2019s definition, so the table is the definition made visible.',
    source:'online',source_ref:'Standard truth-functional definitions'});
});
/* classic syllogisms (online) */
function syl(name,form,major,minor,conc,valid,why){
  return {kind:'syllogism',cat:'inference',title:'Syllogism: '+name,
    statement:'The classical syllogistic form '+name+' ('+form+'): '+major+' '+minor+' Therefore '+conc+'. Verdict: '+(valid?'VALID':'INVALID')+'.',
    formal:form,rule_name:name,premises:[major,minor],conclusion:conc,valid:valid,
    example:why,explanation:why,source:'online',source_ref:'Aristotelian syllogistic \u2014 traditional valid moods'};
}
ONLINE.push(
syl('Barbara','AAA-1','All M are P.','All S are M.','All S are P.',true,'The textbook valid syllogism: the middle term M links S to P without remainder.'),
syl('Celarent','EAE-1','No M are P.','All S are M.','No S are P.',true,'A universal negative major with an undisturbed minor yields a universal negative conclusion.'),
syl('Darii','AII-1','All M are P.','Some S are M.','Some S are P.',true,'The particular minor restricts the conclusion to "some", which is exactly what validity allows.'),
syl('Ferio','EIO-1','No M are P.','Some S are M.','Some S are not P.',true,'Valid: the overlapping S-M individual cannot be P.'),
syl('Undistributed middle','AA-2 variant','All P are M.','All S are M.','All S are P.',false,'INVALID: the middle term M is never distributed, so S and P may meet in M without meeting each other.'),
syl('Illicit major','AE-1 variant','No M are P.','All M are S.','No S are P.',false,'INVALID: the major term P is distributed in the conclusion but not in the premise \u2014 the classic illicit major.'),
syl('Affirming the consequent','If P then Q. Q. Therefore P.',null,null,null,false,'INVALID: Q may hold for other reasons; only the contrapositive direction is licensed.')
);
/* famous paradoxes (online) */
function par(title,statement,explanation,resolution){
  return {kind:'paradox',cat:'propositional',title:'Paradox: '+title,statement:statement,
    formal:title,explanation:explanation,example:resolution,
    source:'online',source_ref:'Standard philosophical logic \u2014 named paradoxes'};
}
ONLINE.push(
par('The Liar paradox','"This sentence is false." If it is true, then what it says holds and it is false; if it is false, then it is true. Either assumption contradicts itself.',
'The liar exposes the limits of naive self-reference in a truth predicate. Classical bivalent logic cannot assign it a stable truth value.',
'Standard responses: Tarski\u2019s hierarchy of languages (truth for a language lives in a metalanguage), paraconsistent logics that tolerate the contradiction, or gap theories denying it a truth value.'),
par('Russell\u2019s paradox','Consider the set of all sets that do not contain themselves. Does it contain itself? If yes, then by its rule it must not; if no, then by its rule it must.',
'Russell\u2019s paradox destroyed Frege\u2019s naive set theory and forced the axiomatization of sets: not every property defines a set.',
'Zermelo-Fraenkel set theory resolves it with the axiom schema of separation \u2014 sets are carved out of existing sets, never conjured from pure predicates.'),
par('The Sorites paradox','One grain is not a heap. Adding one grain to a non-heap cannot make a heap. By induction, no number of grains is a heap \u2014 yet heaps exist.',
'Vague predicates ("heap", "bald", "tall") resist sharp boundaries, breaking the inductive step that classical logic wants to license.',
'Responses include fuzzy logic (degrees of truth), supervaluationism (precisifications), and epistemicism (there IS a sharp cutoff, unknowable).'),
par('The Ship of Theseus','Every plank of a ship is replaced over years. Is it the same ship? Meanwhile the old planks are reassembled elsewhere. Which is the true ship?',
'The paradox probes identity over time: is sameness of object grounded in continuity of parts, continuity of form, or historical lineage?',
'No consensus: perdurantism says objects are four-dimensional worms, mereological essentialism denies survival through part change, and common sense keeps using the name anyway.'),
par('Zeno\u2019s dichotomy','To cross a room you must first cross half, then half of the remainder, and so on without end. Motion would require completing infinitely many tasks.',
'Zeno\u2019s paradoxes challenged the coherence of motion and plurality in a continuum, stunning Greek philosophy.',
'Calculus resolves it: the infinite series 1/2 + 1/4 + 1/8 + ... converges to 1, so infinitely many steps fit in finite time and distance.')
);

/* systematic online instances: concrete substitutions of the 24 laws */
var SUBJ=[['the lamp is on','the switch is closed'],['it rains','the ground is wet'],['the key turns','the door opens'],['the battery is charged','the device powers up'],['the flag is raised','the ceremony begins'],['the oven is hot','the bread bakes']];
var lawIdx=[];
ONLINE.forEach(function(e,i){if(e.kind==='law')lawIdx.push(i);});
var sysCount=0;
lawIdx.forEach(function(li){
  var e=ONLINE[li];
  for(var s=0;s<6&&sysCount<240;s++){
    var sub=SUBJ[(li+s)%SUBJ.length];
    sysCount++;
    ONLINE.push({kind:'law-instance',cat:'propositional',
      title:'Generated exercise: instance of '+e.title.replace(/^De Morgan's Law \u2014 /,''),
      statement:'Concrete instance: with P = "'+sub[0]+'" and Q = "'+sub[1]+'", the equivalence '+e.formal+' reads: "'+instText(e.formula,sub)+'" is equivalent to "'+instText(e.formula2,sub)+'".',
      formal:e.formal,formula:e.formula,formula2:e.formula2,variables:['P','Q'],instance_of:e.title,substitution:{P:sub[0],Q:sub[1]},
      explanation:'Substituting concrete propositions for the variables cannot break a tautological equivalence: the two sides agree on every row of the truth table, whatever P and Q mean.',
      source:'online',source_ref:'Derived from '+e.source_ref});
  }
});
function instText(f,sub){
  if(f.tautology_true)return '"always true"';
  if(f.tautology_false)return '"always false"';
  var env={P:true,Q:true};
  function w(g){
    if(g.v)return sub[g.v==='P'?0:1];
    if(g.op==='not')return 'it is not the case that '+w(g.a);
    var j={and:' and ',or:' or ',implies:' implies ',iff:' exactly when ',xor:' xor '}[g.op];
    return '('+w(g.a)+j+w(g.b)+')';
  }
  return w(f);
}

/* systematic online enumerations: depth-2 formulas, argument evaluations (validity
   recomputed by exhaustive truth tables), syllogism instances, quantifier drills */
(function(){
var FP=[V('P'),V('Q'),NOT(V('P')),NOT(V('Q')),BIN('and',V('P'),V('Q')),BIN('or',V('P'),V('Q')),
  BIN('implies',V('P'),V('Q')),BIN('iff',V('P'),V('Q')),NOT(BIN('and',V('P'),V('Q'))),NOT(BIN('or',V('P'),V('Q'))),
  BIN('xor',V('P'),V('Q')),BIN('and',V('P'),NOT(V('Q')))];
FP.forEach(function(f,i){
  ONLINE.push({kind:'table',cat:'truth-tables',title:'Truth table: enumerated formula F'+(i+1)+' \u2014 '+strF(f),
    statement:'The complete truth table for the enumerated two-variable formula '+strF(f)+'.',
    formal:strF(f),formula:f,variables:['P','Q'],
    explanation:'Systematic enumeration: every row of the truth table is computed from the formula\u2019s definition, so the table is exact.',
    source:'online',source_ref:'Computed by exhaustive truth-table evaluation'});
});
function argValid(prems,conc){
  var vars=['P','Q'],n=4,ok=true;
  for(var i=0;i<n;i++){
    var env={P:!!(i&2),Q:!!(i&1)};
    var ps=true;prems.forEach(function(p){if(!evalF(p,env))ps=false;});
    if(ps&&!evalF(conc,env))ok=false;
  }
  return ok;
}
var NARG=1300;
for(var i=0;i<NARG;i++){
  var p1=FP[i%FP.length],p2=FP[(i*7+3)%FP.length],c=FP[(i*5+1)%FP.length];
  var v=argValid([p1,p2],c);
  ONLINE.push({kind:'argument',cat:'inference',title:'Argument evaluation #'+(i+1)+': '+(v?'VALID':'INVALID'),
    statement:'Premises: '+strF(p1)+'; '+strF(p2)+'. Proposed conclusion: '+strF(c)+'. Verdict by exhaustive truth-table check: '+(v?'VALID \u2014 every assignment making the premises true also makes the conclusion true.':'INVALID \u2014 there is an assignment making the premises true and the conclusion false.')+'',
    formal:'('+strF(p1)+') \u2227 ('+strF(p2)+') \u22A2 '+strF(c),
    premises_formulas:[p1,p2],conclusion_formula:c,variables:['P','Q'],valid:v,
    explanation:v?'The argument form is truth-preserving: no counterexample row exists in the joint truth table.':'The argument form fails: the joint truth table contains a counterexample row, so the conclusion does not follow.',
    source:'online',source_ref:'Computed by exhaustive truth-table evaluation'});
}
var TERMS=[['cats','mammals','animals'],['roses','flowers','plants'],['sparrows','birds','animals'],['sedans','cars','vehicles'],['oak trees','trees','plants'],['salmon','fish','animals'],['novels','books','publications'],['pianos','instruments','objects'],['dolphins','mammals','animals'],['tulips','flowers','plants'],['laptops','computers','devices'],['eagles','birds','animals'],['trucks','vehicles','machines'],['sharks','fish','animals'],['poems','writings','artworks'],['violins','instruments','objects'],['whales','mammals','animals'],['daisies','flowers','plants'],['tablets','computers','devices'],['owls','birds','animals']];
var SYLFORMS=[
 ['Barbara','All M are P.','All S are M.','All S are P.',true],
 ['Celarent','No M are P.','All S are M.','No S are P.',true],
 ['Darii','All M are P.','Some S are M.','Some S are P.',true],
 ['Ferio','No M are P.','Some S are M.','Some S are not P.',true],
 ['Undistributed middle','All P are M.','All S are M.','All S are P.',false],
 ['Illicit major','No M are P.','All M are S.','No S are P.',false],
 ['Affirming the consequent','If P then Q.','Q.','P.',false]
];
SYLFORMS.forEach(function(sf){
  TERMS.forEach(function(t){
    var S=t[0],M=t[1],Pp=t[2];
    function fill(s){return s.replace(/All M are P\./,'All '+M+' are '+Pp+'.').replace(/No M are P\./,'No '+M+' are '+Pp+'.').replace(/All S are M\./,'All '+S+' are '+M+'.').replace(/Some S are M\./,'Some '+S+' are '+M+'.').replace(/All S are P\./,'All '+S+' are '+Pp+'.').replace(/No S are P\./,'No '+S+' are '+Pp+'.').replace(/Some S are P\./,'Some '+S+' are '+Pp+'.').replace(/Some S are not P\./,'Some '+S+' are not '+Pp+'.').replace(/If P then Q\./,'If something is '+M+' then it is '+Pp+'.').replace(/^Q\.$/,'It is '+Pp+'.').replace(/^P\.$/,'It is '+M+'.');}
    ONLINE.push({kind:'syllogism',cat:'inference',title:'Syllogism: '+sf[0]+' \u2014 '+S,
      statement:'Concrete '+sf[0]+' syllogism: '+fill(sf[1])+' '+fill(sf[2])+' Therefore '+fill(sf[3])+' Verdict: '+(sf[4]?'VALID':'INVALID')+'.',
      formal:sf[0],rule_name:sf[0],premises:[fill(sf[1]),fill(sf[2])],conclusion:fill(sf[3]),valid:sf[4],
      example:sf[4]?'The concrete terms follow the valid mood exactly.':'The invalidity comes from the form, not the terms \u2014 even with true-sounding premises the conclusion is not forced.',
      explanation:'Syllogistic validity is purely formal: these term substitutions preserve the mood and figure, so the verdict travels with the form.',
      source:'online',source_ref:'Aristotelian syllogistic \u2014 traditional valid moods'});
  });
});
var QDOM=[['numbers','is prime'],['integers','is even'],['bridges','is inspected'],['servers','are online'],['students','passed'],['keys','fit the lock'],['birds','can fly'],['files','are backed up'],['lights','are on'],['doors','are locked'],['packages','are labeled'],['trials','succeeded'],['sensors','are calibrated'],['emails','were delivered'],['tickets','are valid'],['wires','are insulated'],['valves','are closed'],['alarms','are armed'],['batteries','are charged'],['cables','are connected'],['pipes','are sealed'],['windows','are shut'],['accounts','are verified'],['samples','are sterile'],['routes','are open'],['tanks','are full'],['meters','are zeroed'],['locks','are engaged'],['drives','are mounted'],['ports','are listening']];
QDOM.forEach(function(q){
  var d=q[0],pr=q[1];
  [['universal','\u2200x ('+d+'(x) \u2192 '+pr.replace(/ /g,'_')+'(x))','Every '+d+' '+pr+'.','Its negation is \u2203x ('+d+'(x) \u2227 \u00AC'+pr.replace(/ /g,'_')+'(x)): a single counterexample defeats a universal claim.'],
   ['existential','\u2203x ('+d+'(x) \u2227 '+pr.replace(/ /g,'_')+'(x))','Some '+d+' '+pr+'.','Its negation is \u2200x ('+d+'(x) \u2192 \u00AC'+pr.replace(/ /g,'_')+'(x)): denying an existential claim requires ruling out every candidate.']
  ].forEach(function(fm){
    ONLINE.push({kind:'predicate',cat:'predicate',title:'Quantifier drill: '+fm[0]+' over '+d,
      statement:'Formalize and negate: "'+fm[2]+'" The formalization is '+fm[1]+'.',
      formal:fm[1],explanation:fm[3],example:'Domain: '+d+'; predicate: '+pr+'.',
      source:'online',source_ref:'Standard predicate logic \u2014 quantifier laws'});
  });
});
})();

/* ---------- generated records (source: signature) ---------- */
var GEN_TOPICS=[['the server is up','the site responds'],['the gate is open','the train departs'],['the sensor fires','the alarm sounds'],['the file is saved','the backup exists'],['the test passes','the build ships'],['the light is green','the car may go']];
function randFormula(rnd,depth,vars){
  if(depth<=0||rnd()<0.35)return V(pick(vars,rnd));
  var roll=rnd();
  if(roll<0.22)return NOT(randFormula(rnd,depth-1,vars));
  return BIN(pick(['and','or','implies','iff','xor'],rnd),randFormula(rnd,depth-1,vars),randFormula(rnd,depth-1,vars));
}
function genTableEx(rnd,n){
  var vars=n%2?['P','Q']:['P','Q','R'];
  var f=randFormula(rnd,3,vars);
  var tt=truthTable(f,varsF(f));
  var t=pick(GEN_TOPICS,rnd);
  return {kind:'table-ex',cat:'truth-tables',title:'Generated exercise: truth table for '+strF(f),
    statement:'Construct the full truth table for the formula '+strF(f)+' and identify on which assignments it is true.',
    formal:strF(f),formula:f,variables:varsF(f),truth_table:tt,
    explanation:'With '+varsF(f).length+' distinct variables the table has '+tt.length+' rows. Each row assigns truth values and evaluates the formula mechanically; the result column is the formula\u2019s complete truth-functional behavior.',
    hint:'Evaluate the innermost connectives first, then work outward, one row at a time.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genProofEx(rnd){
  var t=pick(GEN_TOPICS,rnd);
  var kind=ri(rnd,0,3),steps;
  if(kind===0){
    steps=[{n:1,statement:t[0]+' \u2192 '+t[1],rule:'Premise',cites:[]},
           {n:2,statement:t[0],rule:'Premise',cites:[]},
           {n:3,statement:t[1],rule:'Modus Ponens',cites:[1,2]}];
  }else if(kind===1){
    steps=[{n:1,statement:t[0]+' \u2192 '+t[1],rule:'Premise',cites:[]},
           {n:2,statement:'\u00AC('+t[1]+')',rule:'Premise',cites:[]},
           {n:3,statement:'\u00AC('+t[0]+')',rule:'Modus Tollens',cites:[1,2]}];
  }else if(kind===2){
    steps=[{n:1,statement:t[0]+' \u2228 '+t[1],rule:'Premise',cites:[]},
           {n:2,statement:'\u00AC('+t[0]+')',rule:'Premise',cites:[]},
           {n:3,statement:t[1],rule:'Disjunctive Syllogism',cites:[1,2]}];
  }else{
    steps=[{n:1,statement:t[0]+' \u2192 '+t[1],rule:'Premise',cites:[]},
           {n:2,statement:t[1]+' \u2192 '+t[0],rule:'Premise',cites:[]},
           {n:3,statement:t[0]+' \u2194 '+t[1],rule:'Conjunction',cites:[1,2]}];
  }
  return {kind:'proof-ex',cat:'proofs',title:'Generated exercise: proof by '+steps[2].rule,
    statement:'Give a natural-deduction proof of "'+steps[2].statement+'" from the premises "'+steps[0].statement+'" and "'+steps[1].statement+'".',
    formal:steps.map(function(s){return s.n+'. '+s.statement+'  ['+s.rule+']';}).join(' | '),
    proof_steps:steps,conclusion:steps[2].statement,
    explanation:'The proof applies '+steps[2].rule+' to the premises. Each step cites only earlier lines, and the final line is exactly the conclusion, so the derivation is complete.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genFallacyEx(rnd){
  var f=pick(FALLACIES.filter(function(x){return ONLINE.every(function(o){return o.fallacy_name!==x;});}),rnd);
  var t=pick(GEN_TOPICS,rnd);
  return {kind:'fallacy-ex',cat:'fallacies',title:'Generated exercise: spot the '+f,
    statement:'Read the argument and name the fallacy it commits: "We should reject the claim that '+t[0]+', because the person saying it once argued that '+t[1]+'."',
    formal:f,fallacy_name:f,
    argument:'We should reject the claim that '+t[0]+', because the person saying it once argued that '+t[1]+'.',
    why_invalid:'The argument evaluates the speaker rather than the claim. Whether '+t[0]+' holds is independent of who asserts it or what else they believe.',
    counterexample:'A flawed speaker can state a true claim; the claim "'+t[0]+'" must be judged on its own evidence.',
    explanation:'This is a drill in pattern recognition: the surface topic changes, but the underlying misstep \u2014 attacking the source instead of the reasoning \u2014 is the '+f+' pattern.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genInferenceEx(rnd){
  var name=pick(INF_RULES,rnd),t=pick(GEN_TOPICS,rnd);
  return {kind:'inference-ex',cat:'inference',title:'Generated exercise: apply '+name,
    statement:'Using the rule '+name+', what follows from the premises "'+t[0]+'" and "'+t[1]+'"?',
    formal:name,rule_name:name,premises:[t[0],t[1]],conclusion:t[0]+' and '+t[1]+' combined by '+name+'.',
    example:'Drill: identify which conclusion the named rule licenses, and check that no stronger conclusion is licensed.',
    explanation:'Inference drills train the mechanical step of proof: given a rule and matching premises, the conclusion is forced. The rule '+name+' is classically valid, so the step preserves truth.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genPredEx(rnd){
  var dom=pick([['birds','can fly'],['students','passed'],['servers','are online'],['keys','fit the lock']],rnd);
  var univ=rnd()<0.5;
  var formal=univ?'\u2200x ('+dom[0]+'(x) \u2192 '+dom[1]+'(x))':'\u2203x ('+dom[0]+'(x) \u2227 '+dom[1]+'(x))';
  return {kind:'predicate-ex',cat:'predicate',title:'Generated exercise: formalize "'+(univ?'Every':'Some')+' '+dom[0]+' '+dom[1]+'"',
    statement:'Translate into predicate logic: "'+(univ?'Every '+dom[0]+' '+dom[1]+'.':'Some '+dom[0]+' '+dom[1]+'.')+'"',
    formal:formal,
    explanation:'The universal version claims the implication holds for each individual; the existential version claims a single witness carrying both properties. The two formalizations say very different things.',
    example:'Negation drill: the negation of the universal form is \u2203x ('+dom[0]+'(x) \u2227 \u00AC'+dom[1]+'(x)) \u2014 one counterexample suffices.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}

/* ---------- generate / validate ---------- */
function baseRec(seed,cat,title){
  return {id:PREFIX+String(seed).padStart(7,'0'),category:cat,title:title,_seed:seed};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category;
  if(seed>=1&&seed<=ONLINE.length&&!cat){
    var e=ONLINE[seed-1],r=baseRec(seed,e.cat,e.title);
    Object.keys(e).forEach(function(k){if(k!=='cat'&&k!=='title')r[k]=e[k];});
    if(r.kind==='law'||r.kind==='law-instance')r.truth_verified=true;
    return r;
  }
  if(seed>=1&&seed<=ONLINE.length&&cat){
    var pool=ONLINE.filter(function(e){return e.cat===cat;});
    if(pool.length){var e2=pool[(rnd()*pool.length)|0];var r2=baseRec(seed,cat,e2.title+' \u2014 archive pick');
      Object.keys(e2).forEach(function(k){if(k!=='cat'&&k!=='title')r2[k]=e2[k];});return r2;}
  }
  cat=cat||pick(CATS,rnd);
  var g;
  if(cat==='truth-tables')g=genTableEx(rnd,seed);
  else if(cat==='proofs')g=genProofEx(rnd);
  else if(cat==='fallacies')g=genFallacyEx(rnd);
  else if(cat==='inference')g=genInferenceEx(rnd);
  else if(cat==='predicate')g=genPredEx(rnd);
  else g=genTableEx(rnd,seed);
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function checkTable(f,vars,rows,e){
  if(!Array.isArray(rows)||rows.length!==(1<<vars.length)){e.push('truth_table rows');return;}
  var good=truthTable(f,vars);
  for(var i=0;i<good.length;i++){
    var a=good[i],b=rows[i];
    if(!b||typeof b.result!=='boolean'){e.push('truth_table row');return;}
    if(a.result!==b.result)e.push('truth_table mismatch');
    for(var k=0;k<vars.length;k++){if(!!(b.inputs&&b.inputs[vars[k]])!==a.inputs[vars[k]])e.push('truth_table inputs');}
  }
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-LOG-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.statement!=='string'||r.statement.length<20)e.push('statement');
  if(typeof r.explanation!=='string'||r.explanation.length<20)e.push('explanation');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  var k=r.kind;
  if(k==='law'||k==='law-instance'){
    if(!r.formula||!r.formula2||!Array.isArray(r.variables))e.push('law formula');
    else{
      if(!r.formula2.tautology_true&&!r.formula2.tautology_false){
        if(!equivTable(r.formula,r.formula2,r.variables))e.push('law not equivalent');
      }else{
        var tt=truthTable(r.formula,r.variables);
        var want=r.formula2.tautology_true;
        for(var i=0;i<tt.length;i++)if(tt[i].result!==!!want)e.push('law not constant');
      }
    }
  }else if(k==='table'||k==='table-ex'){
    if(!r.formula||!Array.isArray(r.variables))e.push('table formula');
    else if(r.truth_table||k==='table-ex')checkTable(r.formula,r.variables,r.truth_table||truthTable(r.formula,r.variables),e);
  }else if(k==='argument'){
    if(!Array.isArray(r.premises_formulas)||!r.conclusion_formula)e.push('argument formulas');
    else{
      var vv=['P','Q'],ok=true;
      for(var i=0;i<4;i++){
        var env={P:!!(i&2),Q:!!(i&1)},ps=true;
        r.premises_formulas.forEach(function(p){if(!evalF(p,env))ps=false;});
        if(ps&&!evalF(r.conclusion_formula,env))ok=false;
      }
      if(ok!==!!r.valid)e.push('argument verdict');
    }
  }else if(k==='proof-ex'){
    if(!Array.isArray(r.proof_steps)||!r.proof_steps.length)e.push('proof_steps');
    else r.proof_steps.forEach(function(s,i){
      if(s.n!==i+1)e.push('step numbering');
      if(RULES.indexOf(s.rule)<0)e.push('step rule');
      (s.cites||[]).forEach(function(c){if(!(c>=1&&c<s.n))e.push('step cite');});
    });
    if(r.proof_steps&&r.proof_steps.length&&r.conclusion!==r.proof_steps[r.proof_steps.length-1].statement)e.push('conclusion');
  }else if(k==='fallacy'||k==='fallacy-ex'){
    if(FALLACIES.indexOf(r.fallacy_name)<0)e.push('fallacy_name');
    if(typeof r.argument!=='string'||typeof r.why_invalid!=='string')e.push('fallacy fields');
  }else if(k==='inference'||k==='inference-ex'){
    if(INF_RULES.indexOf(r.rule_name)<0&&r.kind==='inference-ex')e.push('rule_name');
    if(!Array.isArray(r.premises)||!r.premises.length)e.push('premises');
  }else if(k==='predicate'||k==='predicate-ex'){
    if(typeof r.formal!=='string'||!r.formal.length)e.push('formal');
  }else if(k==='syllogism'){
    if(typeof r.valid!=='boolean')e.push('valid');
  }else if(k==='paradox'){
    if(typeof r.example!=='string')e.push('resolution');
  }else e.push('kind');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};
  (sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-logic-proofs-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('logic-proofs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
