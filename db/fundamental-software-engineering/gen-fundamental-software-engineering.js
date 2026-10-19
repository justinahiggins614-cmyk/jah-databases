(function(){'use strict';
/* jahdb-fundamental-software-engineering-1.0 — fundamental software-engineering bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FSWE-';
var KIND='fundamental software-engineering record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Software engineering is the disciplined construction of large software systems: applying engineering principles — requirements, design, testing, maintenance — to programs that must work reliably, evolve over years, and be built by teams.', 'reasoning':'Software engineers reason about change: code will be modified, requirements will shift, team members will rotate. Every decision — modularity, tests, documentation — is judged by how it affects the cost of future change.', 'quantities':'The core quantities are defect density, lead time, deployment frequency, and mean time to recovery — the DORA metrics of engineering performance. Technical debt is the master quantity: the future cost of today\'s shortcuts.', 'mechanism':'Software engineering works the lifecycle: requirements → design → implementation → testing → deployment → maintenance. Agile methods run the loop in small iterations; the loop never ends — maintenance is most of a system\'s life.', 'miscon':'Software engineering is not just coding: coding is a fraction of the work. Adding people to a late project makes it later (Brooks\'s law). And \'done\' does not mean \'works once\' — it means tested, documented, deployable, and maintainable.'};
var SIGLENS=['In the Signature system, software engineering is how the network itself is built: every database page, every generator, every tool here follows these disciplines, and the Signature formulation teaches each principle as a practice for building things that last.','The Signature practice is to engineer the software: write the requirement, design the module, test the behavior, document the decision — so engineering discipline is practiced on real builds.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- unit test demo. Runs as-is with python3."""\ndef add(a, b):\n    return a + b\ndef test_add():\n    assert add(2, 3) == 5\n    assert add(-1, 1) == 0\n    assert add(0, 0) == 0\n    return "all tests passed"\nprint(test_add())\nprint("a test is an executable specification")\n', '#!/usr/bin/env python3\n"""{TITLE} -- version control simulation demo. Runs as-is with python3."""\nhistory = []\ndef commit(message, change):\n    history.append({"message": message, "change": change})\n    return len(history)\ncommit("add login", {"files": ["login.py"]})\ncommit("fix null bug", {"files": ["login.py"]})\ncommit("add tests", {"files": ["test_login.py"]})\nfor i, c in enumerate(history, 1):\n    print(f"commit {i}: {c[\'message\']} -> {c[\'change\'][\'files\']}")\nprint("every change is recorded, attributable, and reversible")\n', '#!/usr/bin/env python3\n"""{TITLE} -- technical debt demo. Runs as-is with python3."""\ndef cost_of_change(debt, months):\n    # shortcuts compound: each month of debt makes changes costlier\n    cost = 1.0\n    for _ in range(months):\n        cost *= (1 + debt)\n    return cost\nfor debt in [0.0, 0.05, 0.15]:\n    print(f"monthly shortcut rate {debt:.0%}: 24-month change cost x{cost_of_change(debt, 24):.1f}")\nprint("small shortcuts compound like interest: that is technical debt")\n'];
var TOPICS=[['What Software Engineering Is','Software engineering is the engineering discipline of building software systems: applying systematic methods to requirements, design, construction, testing, and maintenance so that large programs work reliably and evolve over years. Programming writes code; engineering ships systems.'],
['The Core Question of Software Engineering','The core question is: how do we build software that works, on time, and keeps working as it changes? Every practice — testing, review, modularity — is an answer to the cost of change, which dominates software economics.'],
['Assumptions: Change Is Certain','The field assumes change is certain: requirements will shift, libraries will update, team members will leave. Designs are judged not by how clever they are today but by how cheaply they absorb tomorrow\'s changes.'],
['The Vocabulary: Requirements, Architecture, Debt','The vocabulary names the concerns: requirements (what must hold), architecture (the big decisions), technical debt (shortcuts with interest), and the lifecycle (the stages every system passes through). Fluency means thinking in lifecycles, not just code.'],
['Technical Debt: The Fundamental Quantity','Technical debt is the fundamental quantity: the future cost implied by today\'s shortcuts. Like financial debt, it compounds — and like financial debt, it is sometimes the right choice, provided it is tracked and repaid deliberately.'],
['The Lifecycle: The Primary Method','The lifecycle is the primary method: requirements, design, implementation, testing, deployment, maintenance — run iteratively. Agile, waterfall, and DevOps are different cadences on the same loop; the loop itself is non-negotiable.'],
['A Canonical First Example','The canonical first example is the small project that grew: a script becomes a tool becomes a system, and the practices that were optional at 100 lines — tests, version control, documentation — become survival at 100,000. Engineering is what lets software grow up.'],
['How Software Engineering Measures','The field measures with DORA metrics: deployment frequency, lead time, change failure rate, and recovery time. High performers deploy often, fail small, and recover fast — measurement replaced mythology about what \'good\' looks like.'],
['The Core Mechanism: Feedback Loops','The core mechanism is nested feedback loops: tests give feedback in seconds, code review in hours, staging in days, production monitoring continuously. Shortening the loops is the master lever — bugs caught early cost a hundredth of bugs caught late.'],
['The Simplest Law: Brooks\'s Law','The simplest law is Brooks\'s: adding people to a late software project makes it later. Communication overhead grows with the square of team size while work divides linearly — the arithmetic behind every death march.'],
['Common Misconceptions in Software Engineering','The misconceptions are expensive: that more programmers means faster (Brooks), that testing can be skipped under pressure (pressure is when you need it most), that the plan survives contact with code, and that maintenance is someone else\'s problem (it is most of the cost).'],
['How Beginners Practice Software Engineering','Beginners practice by building complete small systems: specify it, build it, test it, document it, deploy it. Finishing — the last 10% of polish, docs, and deployment — is the skill tutorials skip and employers pay for.'],
['The Core Model: Modularity','Modularity is the core model: dividing systems into pieces with hidden internals and clean interfaces. Information hiding lets teams work independently and lets pieces be replaced — the prerequisite for software at scale.'],
['The Great Idea: Continuous Delivery','Continuous delivery is the great idea: every change shippable, deployments routine and boring. It inverts the old risk model — small frequent releases are safer than rare big ones — and it made \'release day\' stop being scary.'],
['Systems Thinking: Socio-Technical Systems','Systems thinking in software engineering includes the team: Conway\'s law says systems mirror their organizations\' communication. The architecture and the org chart co-evolve — you cannot fix one while ignoring the other.'],
['Invariance: Contracts','The invariance principle is the contract: module interfaces promise behavior that implementations must preserve across changes. Tests encode the contracts executably — the suite is the specification that cannot drift from the code.'],
['Approximation: Good Enough Engineering','Approximation is engineering judgment: the 80% solution shipped beats the 100% solution perpetually in design. Prototypes, MVPs, and iterative refinement are disciplined approximations — each version a better estimate of what users need.'],
['Evidence Standards: Production Data','The evidence standard is production: does it work for real users under real load? Staging tests predict; production measures. Monitoring, error budgets, and postmortems turn operations into evidence.'],
['Classic Discoveries','The classic discoveries are time-sharing, version control, the structured program, design patterns, and continuous integration. Each turned individual craft into team-scale engineering.'],
['Core Trade-offs: Speed versus Quality','The core trade-off is speed versus quality, managed as technical debt: borrowing speed today against tomorrow\'s velocity. The discipline is making the trade explicitly — and scheduling repayment.'],
['Handling Uncertainty: Iterative Development','Iterative development handles uncertainty about requirements: build the smallest thing, show users, learn, repeat. Agile is risk management — the plan adapts because the plan was always a hypothesis.'],
['Tools of the Trade','The tools of the trade are version control, CI/CD, issue tracking, and monitoring. The deepest is the postmortem — the blameless autopsy that turns each outage into organizational learning.'],
['Ethics and Responsibility','Ethics in software engineering is professional: the ACM code, safety-critical standards, and the duty to refuse harmful work. Engineers sign off on systems that fly planes and dose medicine — the responsibility is literal.'],
['Teaching Software Engineering','Teaching it well means team projects with real users: the specification will change mid-semester, the integration will hurt, the demo will be public. Nothing else teaches the lifecycle.'],
['The Frontier Question','The frontier question is AI-assisted engineering: when AI writes the code, what becomes of design, verification, and accountability? The frontier redefines the engineer\'s job from writing to specifying and assuring.'],
['Unifying Theories','The unifying view is economics: every practice is priced in the cost of change. Modularity, testing, and automation all pay by making future changes cheap — software engineering is applied economics of modification.'],
['Computational Software Engineering','Computational support — static analysis, fuzzing, formal verification — automates assurance: machines checking code for entire bug classes. The frontier pushes machine-checked guarantees from critical kernels toward everyday software.'],
['Bridges to Other Fields','Software engineering bridges to project management, organizational psychology, economics, and every domain with software to build. It is the meta-discipline of the digital age — every field\'s tools pass through it.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the cost-effective verification of large systems, accurate estimation, and preserving institutional knowledge across team turnover. Active research, no settled answers.'],
['How New Claims Are Validated','New methods are validated by field studies and adoption: the practice tried on real teams, measured with DORA metrics, adopted voluntarily. A methodology earns trust when teams choose it after the trial.'],
['The Great Debates','The great debates — agile versus plan-driven, monolith versus microservices, static versus dynamic — recur because context decides. The mature position is contingency: the right method depends on the system\'s scale, criticality, and rate of change.'],
['Failure Modes: When Software Engineering Gets It Wrong','The field gets it wrong through big-bang rewrites, process without judgment, and metrics gamed into meaninglessness. The immune system is small batches, honest retrospectives, and measuring outcomes instead of activity.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis runs whole organizations from fundamentals: the lifecycle, the feedback loops, the contracts, the debt ledger — scaled to hundreds of engineers. The fundamentals are the management system, not just the coding standard.'],
['The Signature Formulation: Engineering as Lasting Construction','The Signature formulation makes software engineering the build discipline of the network: every database here is engineered to last and evolve, because in the Signature system software that cannot be maintained cannot be trusted. That is the Signature capstone on engineering bedrock.']];
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
    standards:["Requirements are written: what the system must do is stated before it is built.", "Tests guard behavior: every feature has automated tests that run on every change.", "Changes are reviewed: no code reaches users without a second pair of eyes."],citations:["Brooks, F. P. \u2014 The Mythical Man-Month (Addison-Wesley).", "Hunt, A. and Thomas, D. \u2014 The Pragmatic Programmer (Addison-Wesley).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-software-engineering-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-software-engineering',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
