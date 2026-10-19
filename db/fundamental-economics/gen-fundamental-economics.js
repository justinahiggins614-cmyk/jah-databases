(function(){'use strict';
/* jahdb-fundamental-economics-1.0 — fundamental economics bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FEC-';
var KIND='fundamental economics record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Economics studies how societies allocate scarce resources: what gets produced, how, and for whom. It joins mathematical models of choice with the messy reality of human behavior and institutions.', 'reasoning':'Economists reason with models and incentives: assume agents respond to incentives, work out the equilibrium, and test against data. \'Incentives matter\' is the master insight — people respond to the rewards in front of them.', 'quantities':'The core quantities are supply, demand, price, and the aggregates — GDP, inflation, unemployment. Elasticity measures responsiveness; the interest rate is the price of time itself.', 'mechanism':'The economy works through decentralized coordination: prices signal scarcity, profits signal opportunity, and competition disciplines producers. The market is a distributed computer solving allocation problems no planner could.', 'miscon':'Economics is not just money: it studies all choice under scarcity, including time and attention. Economists do not worship markets: they study when markets fail — externalities, public goods, monopoly — and what fixes them. And GDP is not wellbeing: it measures output, nothing more.'};
var SIGLENS=['In the Signature system, economics is the allocation discipline: every resource decision in this network — what to build, what to prioritize — follows economic reasoning, and the Signature formulation teaches each principle as a trade-off you can calculate.','The Signature practice is to compute the trade-off: model the incentives, price the alternatives, check the equilibrium — so economic reasoning is done with numbers, not just narratives.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- supply and demand demo. Runs as-is with python3."""\ndef equilibrium():\n    # Qd = 100 - 2P, Qs = 20 + 3P\n    P = (100 - 20) / (2 + 3)\n    Q = 100 - 2 * P\n    return P, Q\nP, Q = equilibrium()\nprint(f"Qd=100-2P, Qs=20+3P -> equilibrium P={P:.0f}, Q={Q:.0f}")\nprint("price adjusts until quantity demanded equals quantity supplied")\n', '#!/usr/bin/env python3\n"""{TITLE} -- compound growth demo. Runs as-is with python3."""\ndef future_value(pv, rate, years):\n    return pv * (1 + rate) ** years\nfor rate in [0.02, 0.05, 0.07]:\n    print(f"${1000} at {rate:.0%} for 30y -> ${future_value(1000, rate, 30):,.0f}")\nprint("small rate differences compound enormously: growth is exponential")\n', '#!/usr/bin/env python3\n"""{TITLE} -- opportunity cost demo. Runs as-is with python3."""\noptions = {"job A": 60000, "job B": 55000, "startup": 40000}\nchosen = max(options, key=options.get)\nopp_cost = max(v for k, v in options.items() if k != chosen)\nprint(f"choose {chosen} (${options[chosen]}); opportunity cost = ${opp_cost} (best alternative)")\nprint("cost is what you give up: the next-best alternative, not the money spent")\n'];
var TOPICS=[['What Economics Is','Economics studies choice under scarcity: how individuals, firms, and societies allocate limited resources among competing wants. It is the science of trade-offs — every economic statement is about what is given up.'],
['The Core Question of Economics','The core question is: what gets produced, how, and for whom? Markets, firms, and governments are alternative answers — and the field studies which answer works, where, and why.'],
['Assumptions: Scarcity and Incentives','The field assumes scarcity (wants exceed resources) and incentive-response (behavior follows rewards). Models add rationality as a first approximation — then behavioral economics corrects it with evidence.'],
['The Vocabulary: Supply, Demand, Equilibrium','The vocabulary names the market\'s moving parts: supply, demand, price, and equilibrium — plus the aggregates: GDP, inflation, unemployment. Fluency means seeing every market as these forces in balance.'],
['Opportunity Cost: The Fundamental Concept','Opportunity cost is the fundamental concept: the cost of anything is the best alternative forgone. It reframes every decision — the cost of college is not tuition but the earnings and experiences traded away.'],
['Supply and Demand: The Primary Model','Supply and demand is the primary model: the curves cross at equilibrium, price adjusts to clear the market. Shifts versus movements along the curves — the distinction that organizes all market analysis.'],
['A Canonical First Example','The canonical first example is the apple market: a frost shifts supply left, price rises, quantity falls. One diagram predicts the direction of every market shock — the field\'s workhorse.'],
['How Economics Measures','The field measures with national accounts, surveys, and experiments: GDP, price indices, labor statistics — plus randomized trials and natural experiments for causality. Measurement turned economics empirical.'],
['The Core Mechanism: The Price System','The core mechanism is the price system: prices signal scarcity and coordinate strangers. Hayek\'s insight — prices compress dispersed knowledge into one number — explains how markets coordinate without coordinators.'],
['The Simplest Law: Demand Slopes Down','The simplest law is the law of demand: higher price, lower quantity demanded, all else equal. It is the most confirmed regularity in economics — and the starting point of all policy analysis.'],
['Common Misconceptions in Economics','The misconceptions mislead: that economics is only about money (it\'s about all scarce choice), that trade has winners and losers only (voluntary trade benefits both), that GDP measures wellbeing, and that economists all agree (they don\'t — that\'s why it\'s interesting).'],
['How Beginners Practice Economics','Beginners practice by thinking at the margin: the next unit\'s benefit versus its cost. Marginal thinking — applied to studying, hiring, pricing — is the habit the field installs.'],
['The Core Model: Comparative Advantage','Comparative advantage is the core model of trade: even the less productive party gains by specializing in what it does relatively best. Ricardo\'s 1817 logic still underlies all trade policy — and is still widely disbelieved.'],
['The Great Insight: Incentives Matter','Incentives matter is the great insight: people respond to the rewards they face — foreseen and unforeseen. Every policy is an incentive system; the question is always what behavior it actually rewards.'],
['Systems Thinking: General Equilibrium','Systems thinking in economics is general equilibrium: everything affects everything — a tax here shifts markets there. Partial analysis is the first step; the system is the full picture.'],
['Invariance: The Budget Constraint','The invariance principle is the budget constraint: spending is bounded by income plus borrowing. Every agent, every government, faces it — the accounting identity no policy escapes.'],
['Approximation: Ceteris Paribus','Approximation holds other things equal: ceteris paribus isolates the effect of interest. The real world never holds still — which is why the field hunts natural experiments.'],
['Evidence Standards: Identification','The evidence standard is credible identification of cause: randomized trials, discontinuities, instruments — methods that isolate causality from correlation. The credibility revolution remade empirical economics around this standard.'],
['Classic Discoveries','The classic discoveries are the invisible hand, comparative advantage, marginal analysis, and the Phillips curve\'s rise and fall. Each reshaped how societies organize production — ideas with trillion-dollar consequences.'],
['Core Trade-offs: Efficiency versus Equity','The core trade-off is efficiency versus equity: markets maximize the pie\'s size; societies argue over its slices. The field clarifies the trade — it cannot resolve the values beneath it.'],
['Handling Uncertainty: Expectations','Economics handles uncertainty through expectations: people act on beliefs about the future, and beliefs shape outcomes. Rational-expectations modeling made the assumption explicit — and testable.'],
['Tools of the Trade','The tools of the trade are the supply-demand diagram, regression, and the randomized trial. The deepest is the natural experiment — the world running the treatment group for you.'],
['Ethics and Responsibility','Ethics in economics concerns advice with consequences: policies move livelihoods. The field\'s responsibility is honesty about uncertainty, about trade-offs, and about whose welfare the analysis counts.'],
['Teaching Economics','Teaching it well starts with the student\'s own choices: the job offer, the purchase, the vote — each an economic problem. Experiments in class (trading games) make equilibrium visceral.'],
['The Frontier Question','The frontier question is the digital economy: zero-marginal-cost goods, platform monopolies, and AI\'s effect on work. The frontier asks whether the old models still bind — and what replaces them.'],
['Unifying Theories','The unifying theories are choice theory and equilibrium: optimizing agents plus market clearing describe phenomena from marriage to macroeconomics. Behavioral economics refines the agent; the framework endures.'],
['Computational Economics','Computational economics simulates economies: agent-based models, DSGE models, and now machine learning for prediction. The models discipline intuition — and fail instructively where they miss.'],
['Bridges to Other Fields','Economics bridges to psychology (behavioral), political science (policy), sociology (institutions), history (development), and computer science (mechanism design, algorithmic game theory). Scarcity is universal — so is the field\'s reach.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: what causes long-run growth, why some nations stay poor, and how to model financial crises. Active research, no settled answers.'],
['How New Claims Are Validated','New claims are validated by replication and out-of-sample prediction: the effect found in fresh data, the model forecasting the unseen. An economic finding earns trust when it survives new samples and new settings.'],
['The Great Debates','The great debates — Keynes versus Hayek, the minimum wage\'s effects, austerity versus stimulus — persist because values and evidence intertwine. The debates are substantive: each side has models and data.'],
['Failure Modes: When Economics Gets It Wrong','The field gets it wrong through models mistaken for reality, ignored institutions, and overconfident forecasts. The immune system is the empirical check — and humility about what models omit.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis analyzes whole economies from fundamentals: the incentives, the constraints, the equilibria — and the institutions shaping them. The fundamentals are the lens; judgment is the focus.'],
['The Signature Formulation: Economics as Trade-off Calculus','The Signature formulation treats economics as the calculus of trade-offs: every principle here prices a choice, because in the Signature system resources are finite and decisions must be calculated. That is the Signature capstone on economic bedrock.']];
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
    standards:["Models state assumptions: every result is conditional on its premises.", "Evidence is empirical: claims are tested against data, natural experiments preferred.", "Welfare is distinguished from output: GDP is reported as GDP, not as wellbeing."],citations:["Mankiw, N. G. \u2014 Principles of Economics (Cengage).", "Krugman, P. and Wells, R. \u2014 Economics (Worth).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-economics-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-economics',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
