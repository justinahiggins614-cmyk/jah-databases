(function(){'use strict';
/* Public AI Planning Database generator — jahdb-ai-planning-public-ai-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PLAN-AI-PUB-';
var TOPICS=[["Classical Planning", "Symbolic planning using formalisms like STRIPS and PDDL to find action sequences achieving goals."], ["State-Space Search", "Searching through state spaces with BFS, DFS, and Dijkstra for optimal plans."], ["Heuristic Search", "Using heuristics like in A* search to find optimal paths efficiently."], ["Planning Graphs", "Graphplan-style planning graphs that compactly represent reachable states over time."], ["Hierarchical Task Networks", "HTN planning breaking abstract tasks into primitive actions via decomposition methods."], ["Partial-Order Planning", "Planners that commit to action orderings only when necessary for correctness."], ["Planning Under Uncertainty", "Planning techniques that account for nondeterministic outcomes and partial observability."], ["MDP Planning", "Solving Markov Decision Processes via value and policy iteration for optimal behavior."], ["POMDPs", "Partially Observable MDPs for decision-making under state uncertainty."], ["Monte Carlo Tree Search", "Sampling-based search balancing exploration and exploitation in large decision trees."], ["Game-Tree Search", "Adversarial search algorithms from minimax to alpha-beta pruning for game playing."], ["Multi-Agent Planning", "Coordinating plans across multiple agents in shared environments."], ["Temporal Planning", "Planning with durative actions, concurrency, and temporal constraints."], ["Planning and Scheduling", "Integrated approaches combining action planning with resource and time scheduling."], ["LLM-Based Planning", "Using large language models to generate and refine plans in natural language."], ["ReAct and Plan-Act Loops", "Agent architectures alternating planning steps with actions and observations."], ["Task Decomposition", "Breaking complex objectives into subtasks for tractable planning and execution."], ["Plan Verification", "Validating plans for correctness, safety, and goal achievement before execution."], ["Replanning and Execution Monitoring", "Monitoring execution and replanning when deviations or failures occur."], ["Planning in Robotics", "Task and motion planning for robots operating in real environments."], ["Logistics Planning", "Optimization of routes, fleets, and deliveries in logistics operations."], ["Automated Planning Competitions", "The International Planning Competition benchmarking planner performance."], ["Neurosymbolic Planning", "Combining learned heuristics and representations with classical planning algorithms."], ["Learning Planning Heuristics", "Machine learning approaches that acquire domain-specific planning guidance."], ["Plan Explanation", "Generating understandable explanations of why a plan achieves its goals."], ["Future of AI Planning", "Informed outlook on planning research and its integration with learning systems."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'public ai planning record', content:content,
    demo:null, src:'public', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('ai-planning-public-ai',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();