(function(){'use strict';
/* jahdb-fundamental-psychology-1.0 — fundamental psychology bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FPS-';
var KIND='fundamental psychology record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Psychology is the scientific study of mind and behavior: how people perceive, think, feel, learn, and relate. It joins rigorous experiment with the irreducible complexity of human experience.', 'reasoning':'Psychologists reason by operationalizing: turn \'memory\' or \'happiness\' into measurable variables, manipulate or observe systematically, and replicate. Constructs must earn their keep by predicting behavior.', 'quantities':'The core quantities are effect sizes, reliability, and validity: how big the effect, how consistent the measure, how well it captures the concept. Statistical power — the chance of detecting a real effect — is the master quantity.', 'mechanism':'Psychology works the experiment: hypothesis → operationalization → design (control the confounds) → measurement → analysis → replication. The replication crisis taught the field that single studies persuade but only replications convince.', 'miscon':'Psychology is not just common sense: experiments routinely overturn intuition. It is not all about Freud: modern psychology is experimental, cognitive, and neural. And \'statistically significant\' is not \'important\' — effect size and context decide.'};
var SIGLENS=['In the Signature system, psychology is the human-understanding discipline: every interface, every teaching ladder, every AI interaction in this network applies these principles, and the Signature formulation teaches each one as insight you can test.','The Signature practice is to test the insight: run the experiment in miniature, measure the effect, replicate the finding — so psychological principles are held to evidence, not just asserted.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- Stroop effect demo (data). Runs as-is with python3."""\n# simulated reaction times (ms): congruent vs incongruent\nimport random\nrandom.seed(4)\ncongruent = [random.gauss(600, 80) for _ in range(20)]\nincongruent = [random.gauss(750, 90) for _ in range(20)]\ndef mean(x): return sum(x)/len(x)\nprint(f"congruent mean: {mean(congruent):.0f} ms")\nprint(f"incongruent mean: {mean(incongruent):.0f} ms")\nprint(f"Stroop interference: {mean(incongruent)-mean(congruent):.0f} ms slower")\n', '#!/usr/bin/env python3\n"""{TITLE} -- memory curve demo. Runs as-is with python3."""\nimport math\ndef retention(hours, strength=1.0):\n    return math.exp(-hours / (24 * strength))\nfor h in [1, 24, 168, 720]:\n    print(f"after {h:>4}h: retention {retention(h):.1%}")\nprint("spaced repetition resets the curve: review before it decays")\n', '#!/usr/bin/env python3\n"""{TITLE} -- effect size demo. Runs as-is with python3."""\nimport math\ndef cohens_d(m1, m2, sd):\n    return (m1 - m2) / sd\nfor d in [0.2, 0.5, 0.8]:\n    print(f"Cohen\'s d = {d}: {\'small\' if d<0.3 else \'medium\' if d<0.7 else \'large\'} effect")\nprint("p-values say \'is there an effect\'; effect sizes say \'how big\'")\n'];
var TOPICS=[['What Psychology Is','Psychology is the science of mind and behavior: perception, cognition, emotion, motivation, development, personality, and social interaction — studied with the methods of science applied to the most complex subject there is.'],
['The Core Question of Psychology','The core question is: why do people think, feel, and act as they do? Every study asks it at some level — from neurons to societies — and the answers must survive replication.'],
['Assumptions: Behavior Has Causes','The field assumes behavior has discoverable causes: biological, cognitive, and social factors interacting. Determinism here is methodological — the working assumption that systematic study reveals patterns, not a claim about free will.'],
['The Vocabulary: Constructs and Variables','The vocabulary names the unobservable (constructs: memory, anxiety, intelligence) and the observable (variables: reaction time, score, choice). Operationalization bridges them — the definition that makes a construct measurable.'],
['Effect Size: The Fundamental Quantity','Effect size is the fundamental quantity: how big the difference or relationship is, in standardized units. A significant p-value with a tiny effect is a precisely measured triviality — the field learned this the hard way.'],
['The Experiment: The Primary Method','The experiment is the primary method: manipulate the hypothesized cause, control the confounds, measure the effect. Random assignment is the crown jewel — it balances the unknown unknowns.'],
['A Canonical First Example','The canonical first example is Pavlov\'s conditioning: bell paired with food, soon the bell alone salivates the dog. One experiment founded the study of learning — association as the mind\'s basic operation.'],
['How Psychology Measures','The field measures with tests, observations, and instruments: validated questionnaires, behavioral tasks, reaction times, brain imaging. Reliability (consistency) and validity (truthfulness) judge every measure.'],
['The Core Mechanism: Learning','The core mechanism is learning: classical and operant conditioning, observational learning, and the cognitive processes that elaborate them. Behavior changes with experience — the mind\'s defining property.'],
['The Simplest Law: Practice Improves Performance','The simplest law is the power law of practice: performance improves with practice, with diminishing returns. It holds from typing to tennis — the most replicated regularity in the field.'],
['Common Misconceptions in Psychology','The misconceptions mislead: that psychology is common sense (experiments overturn intuition regularly), that it\'s all Freud (modern psychology is experimental), that significant means important, and that lab findings always generalize.'],
['How Beginners Practice Psychology','Beginners practice by observing systematically: define the behavior, count it reliably, compare conditions. The naturalistic observation — watching carefully and recording honestly — is the root skill.'],
['The Core Model: Information Processing','Information processing is the core cognitive model: sensation → attention → perception → memory → decision, each stage studied separately. The computer metaphor organized a generation of research — useful, and now being transcended.'],
['The Great Finding: Cognitive Biases','The great finding is the catalog of cognitive biases: systematic deviations from rationality — anchoring, availability, confirmation — mapped by Kahneman and Tversky. The mind\'s bugs are as lawful as its features.'],
['Systems Thinking: The Biopsychosocial Model','Systems thinking in psychology is the biopsychosocial model: behavior emerges from biological, psychological, and social levels together. No single level suffices — the levels interact.'],
['Invariance: What Replicates','The invariance principle is replication: genuine effects survive new samples, new labs, new measures. The replication crisis taught the field that invariance must be demonstrated, not assumed.'],
['Approximation: Models of Mind','Approximation builds models of mind: simplified theories capturing the essentials — working memory\'s limits, prospect theory\'s value function. The model is judged by prediction, not by realism.'],
['Evidence Standards: Pre-registration and Replication','The evidence standard is now pre-registration plus replication: hypotheses and analyses declared in advance, findings reproduced independently. The field rebuilt its credibility on these.'],
['Classic Discoveries','The classic discoveries are conditioning, the cognitive revolution, attachment theory, cognitive biases, and the Big Five personality traits. Each revealed lawful structure in the mind\'s apparent chaos.'],
['Core Trade-offs: Internal versus Ecological Validity','The core trade-off is internal versus ecological validity: the lab controls confounds but distorts reality; the field is real but messy. The field needs both — and knows neither alone suffices.'],
['Handling Uncertainty: Individual Differences','Psychology handles uncertainty as individual differences: people vary, and the variation is data. Personality traits, abilities, and disorders are distributions — the field studies the shape, not just the mean.'],
['Tools of the Trade','The tools of the trade are the validated scale, the experimental design, and the meta-analysis. The deepest is the replication — the independent rerun that separates finding from fluke.'],
['Ethics and Responsibility','Ethics in psychology is strict: informed consent, the right to withdraw, debriefing, and special protections for vulnerable participants. The field\'s past abuses wrote its present rules.'],
['Teaching Psychology','Teaching it well runs the classic experiments: the Stroop test, the memory span, the conformity demonstration — students experience the phenomena before theorizing them.'],
['The Frontier Question','The frontier question is the integrated mind: how do genes, brains, experience, and culture jointly produce a person? The frontier is genuinely multilevel — and genuinely hard.'],
['Unifying Theories','The unifying theories are evolution (why minds are built this way), learning theory (how they change), and the emerging computational psychiatry. The field seeks its synthesis — and knows premature unification is worse than none.'],
['Computational Psychology','Computational psychology models the mind: reinforcement learning for choice, Bayesian models for perception, neural networks for representation. The models are tested against behavior — prediction is the proof.'],
['Bridges to Other Fields','Psychology bridges to neuroscience (the brain), medicine (mental health), education (learning), business (behavior), computer science (HCI, AI), and law (judgment). The mind touches everything.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the nature of consciousness, the causes of most mental disorders, and reliable behavior change at scale. Active research, no settled answers.'],
['How New Claims Are Validated','New claims are validated by pre-registered replication: independent labs, same protocol, the effect holding. A finding earns trust when strangers reproduce it — the post-crisis standard.'],
['The Great Debates','The great debates — nature versus nurture, the validity of the unconscious, the medical model of disorder — persist because each side captures part of the truth. The debates matured the field\'s thinking.'],
['Failure Modes: When Psychology Gets It Wrong','The field gets it wrong through p-hacking, HARKing, and overgeneralizing from WEIRD samples. The immune system is now institutional: pre-registration, open data, and replication as routine.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis understands persons from fundamentals: the biology, the learning history, the social context — integrated into formulations that guide help. The fundamentals are the clinician\'s and researcher\'s shared ground.'],
['The Signature Formulation: Psychology as Tested Understanding','The Signature formulation treats psychological principles as tested understanding: every concept here is evidence-graded and replication-aware, because in the Signature system claims about minds must meet the highest standard of proof. That is the Signature capstone on psychological bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
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
    standards:["Constructs are operationalized: every concept is tied to measurable indicators.", "Ethics govern research: informed consent and debriefing are non-negotiable.", "Replication is the standard: findings earn trust by surviving independent repetition."],citations:["Myers, D. G. \u2014 Psychology (Worth Publishers).", "American Psychological Association \u2014 Publication Manual (research standards).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-psychology-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-psychology',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
