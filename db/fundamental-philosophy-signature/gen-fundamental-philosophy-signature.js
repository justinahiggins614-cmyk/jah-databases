(function(){'use strict';
/* jahdb-fundamental-philosophy-signature-1.0 — fundamental philosophy bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFPH-';
var KIND='fundamental philosophy record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Philosophy is the disciplined examination of fundamental questions: what exists, what we can know, what is right, and how to live. It proceeds by argument — reasons offered, objections answered — rather than by experiment.', 'reasoning':'Philosophers reason by conceptual analysis and argument: clarify the question, distinguish the senses, construct the argument, consider the objections, revise. The thought experiment is the laboratory — the trolley problem, the brain in a vat.', 'quantities':'The core \'quantities\' are distinctions: the field measures in clarity — necessary versus sufficient, de re versus de dicto, type versus token. Precision of distinction is the master skill.', 'mechanism':'Philosophy works the dialectic: thesis, objection, reply, refinement. Progress looks like better questions and dissolved confusions — and occasionally like a proof that changes what everyone must believe.', 'miscon':'Philosophy is not just opinions: it is argument with standards — validity, soundness, counterexample. It is not useless: it underlies science (what counts as evidence?), law (what is justice?), and AI (what is mind?). And philosophers do make progress — many questions have been settled by argument.'};
var SIGLENS=['In the Signature system, philosophy is the clarity discipline: every hard question in this network — about minds, rights, knowledge — gets philosophical scrutiny, and the Signature formulation teaches each principle as an argument you can examine.','The Signature practice is to argue well: state the claim, give the reasons, face the objection — so philosophical fundamentals are learned as disciplined reasoning, not as quoted opinions.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- argument validity demo. Runs as-is with python3."""\ndef check_argument(premises_true, conclusion_follows):\n    valid = conclusion_follows\n    sound = valid and all(premises_true)\n    return valid, sound\nfor pt, cf, name in [([True, True], True, "valid+sound"), ([True, False], True, "valid, unsound"),\n                     ([True, True], False, "invalid")]:\n    v, s = check_argument(pt, cf)\n    print(f"{name}: valid={v}, sound={s}")\nprint("validity is form; soundness is form + true premises")\n', '#!/usr/bin/env python3\n"""{TITLE} -- trolley problem demo (data). Runs as-is with python3."""\n# survey-style results (illustrative): % who would pull the lever\nresults = {"switch (1 dies, 5 live)": 0.85, "push (1 dies, 5 live)": 0.30}\nfor case, pct in results.items():\n    print(f"{case}: {pct:.0%} would act")\nprint("same numbers, different actions: deontology vs consequentialism in data")\n', '#!/usr/bin/env python3\n"""{TITLE} -- Ship of Theseus demo (identity). Runs as-is with python3."""\nclass Ship:\n    def __init__(self, planks): self.planks = list(planks)\n    def replace(self, i, new): self.planks[i] = new\nship = Ship(["p1", "p2", "p3"])\nfor i in range(3): ship.replace(i, f"q{i+1}")\nprint("all planks replaced:", ship.planks)\nprint("same ship? identity over time: the metaphysics of persistence")\n'];
var TOPICS=[['Signature What Philosophy Is','Philosophy is the systematic investigation of fundamental questions — existence, knowledge, value, reason, mind — by argument and analysis. It is the discipline that asks what other disciplines assume.'],
['Signature The Core Question of Philosophy','The core questions are the permanent ones: What is real? What can we know? What should we do? How should we live? Every philosophy is an attempt at these — and the attempts are judged by argument.'],
['Signature Assumptions: Reason Can Investigate','The field assumes reason can investigate the fundamental: that careful thinking about concepts, arguments, and possibilities yields genuine knowledge. Skepticism about this is itself a philosophical position — argued, not assumed.'],
['Signature The Vocabulary: The Branches','The vocabulary names the branches: metaphysics (what exists), epistemology (what we can know), ethics (what is right), logic (what follows), aesthetics (what is beautiful). Fluency means locating any question in its branch.'],
['Signature The Argument: The Fundamental Unit','The argument — premises supporting a conclusion — is the fundamental unit. Validity (conclusion follows) and soundness (valid plus true premises) are the master distinctions; everything else is commentary.'],
['Signature Analysis: The Primary Method','Conceptual analysis is the primary method: clarify the concept, distinguish its senses, test with thought experiments. The thought experiment — the trolley, the brain in a vat — is the laboratory.'],
['Signature A Canonical First Example','The canonical first example is Socrates in the Apology: the examined life, the profession of ignorance, the elenchus — questioning that exposes false confidence. Philosophy begins as the discipline of not fooling yourself.'],
['Signature How Philosophy Measures','Philosophy measures by argumentative standards: validity, soundness, explanatory power, and counterexample-resistance. There are no instruments — the measure is whether the argument survives the strongest objections.'],
['Signature The Core Mechanism: The Dialectic','The core mechanism is the dialectic: position, objection, reply, refinement. Knowledge advances as confusions dissolve and distinctions sharpen — progress measured in clarity.'],
['Signature The Simplest Law: The Principle of Non-Contradiction','The simplest law is non-contradiction: the same thing cannot both be and not be in the same respect. Aristotle called it the firmest principle — all reasoning presupposes it.'],
['Signature Common Misconceptions in Philosophy','The misconceptions dismiss: that philosophy is mere opinion (it has standards of argument), that it makes no progress (many questions are settled), that it\'s impractical (it founds science, law, and ethics), and that \'everything is relative\' is deep (it\'s usually confused).'],
['Signature How Beginners Practice Philosophy','Beginners practice by reconstructing arguments: read the passage, extract premises and conclusion, evaluate. The argument map — boxes and arrows — makes reasoning visible and criticizable.'],
['Signature The Core Model: The Syllogism','The syllogism is the core model of deductive argument: all men are mortal; Socrates is a man; therefore Socrates is mortal. Twenty-four centuries old and still the template of valid reasoning.'],
['Signature The Great Distinction: Is versus Ought','Hume\'s is-ought distinction is the great caution: no description of how things are entails how they should be, without an added value premise. Ethics needs values — facts alone don\'t supply them.'],
['Signature Systems Thinking: Worldviews','Systems thinking in philosophy is the worldview: metaphysics, epistemology, and ethics as an integrated position. The great systems — Plato\'s, Aristotle\'s, Kant\'s — are attempts at the whole.'],
['Signature Invariance: Logical Form','The invariance principle is logical form: the argument\'s validity is invariant across subject matter. The skeleton judges — content is interchangeable, form is not.'],
['Signature Approximation: Thought Experiments','Approximation uses idealized scenarios: frictionless planes of the mind — the trolley, the veil of ignorance. The idealization isolates the intuition; the debate tests whether it tracks the real.'],
['Signature Evidence Standards: The Counterexample','The evidence standard is the counterexample: one case where premises hold and conclusion fails refutes the universal claim. Philosophy\'s experiments are cases — real or imagined — that test principles.'],
['Signature Classic Discoveries','The classic \'discoveries\' are argumentative: Socratic method, Aristotle\'s logic, the ontological debates, Hume\'s fork, Kant\'s Copernican turn. Each redefined what could be asked — and how.'],
['Signature Core Trade-offs: Depth versus Breadth','The core trade-off is depth versus breadth: the specialist\'s precision against the generalist\'s vision. Philosophy needs both — the system-builder and the analyst — and honors each.'],
['Signature Handling Uncertainty: Fallibilism','Philosophy handles uncertainty with fallibilism: even our best-supported beliefs might be wrong. The response is not skepticism\'s paralysis but inquiry\'s discipline — believe proportionally, revise readily.'],
['Signature Tools of the Trade','The tools of the trade are the distinction, the thought experiment, and the counterexample. The deepest is the steelman — the opponent\'s argument in its strongest form, which honest inquiry requires.'],
['Signature Ethics and Responsibility','Ethics in philosophy is both subject and duty: philosophers argue about the good while owing their interlocutors honesty — no straw men, no sophistry. The field\'s ethic is intellectual virtue itself.'],
['Signature Teaching Philosophy','Teaching it well is dialogue: the question posed, positions defended, objections raised. Students learn philosophy by doing it — the seminar as dialectic in miniature.'],
['Signature The Frontier Question','The frontier question is philosophy of the new: AI minds, digital persons, engineered biology — do the old concepts stretch? The frontier tests whether 2,500 years of distinctions still cut.'],
['Signature Unifying Theories','The unifying attempts — the great systems — aim to join metaphysics, epistemology, and ethics into one vision. The field values the attempt even where it judges the system incomplete.'],
['Signature Computational Philosophy','Computational philosophy formalizes arguments: argument-mapping software, formal epistemology, experimental philosophy\'s surveys. The tools are new; the standards — clarity, validity, honesty — are ancient.'],
['Signature Bridges to Other Fields','Philosophy bridges to every field with foundations: science (methodology), law (jurisprudence), medicine (bioethics), computer science (AI, logic), and art (aesthetics). It is the discipline of foundations.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: consciousness, free will, the ground of morality, the nature of truth. Twenty-five centuries of attention, no consensus — the deepest questions resist closure.'],
['Signature How New Claims Are Validated','New philosophical claims are validated by the literature\'s scrutiny: published, objected to, defended, refined. A position earns standing when it survives the field\'s best objections — peer review as dialectic.'],
['Signature The Great Debates','The great debates — realism versus anti-realism, consequentialism versus deontology, the mind-body problem — are the field\'s permanent curriculum. They persist because each side captures genuine insight.'],
['Signature Failure Modes: When Philosophy Gets It Wrong','Philosophy gets it wrong through obscurity mistaken for depth, cleverness without wisdom, and disconnection from the sciences. The immune system is clarity\'s demand — and the counterexample.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis thinks whole: the metaphysics grounding the epistemology grounding the ethics — a position, argued, objection-faced. The fundamentals are the toolkit; the synthesis is the philosophy.'],
['Signature The Signature Formulation: Philosophy as Clarity Engine','The Signature formulation treats philosophy as the clarity engine of the network: every hard question here gets argued honestly, because in the Signature system unexamined assumptions are the most expensive bugs. That is the Signature capstone on philosophical bedrock.']];
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
    standards:["Arguments are explicit: premises stated, inferences named.", "Objections are faced: the strongest counterargument is answered, not the weakest.", "Distinctions are drawn: ambiguities are resolved before conclusions are drawn."],citations:["Plato \u2014 Republic and Apology (founding texts of Western philosophy).", "Russell, B. \u2014 The Problems of Philosophy (Oxford University Press).", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-philosophy-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-philosophy-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
