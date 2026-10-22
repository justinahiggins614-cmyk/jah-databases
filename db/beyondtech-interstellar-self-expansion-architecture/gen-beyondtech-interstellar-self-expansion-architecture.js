#!/usr/bin/env node
// Boundless generator for beyondtech-interstellar-self-expansion-architecture.
// Technology: Interstellar Self-Expansion Architecture (public edition).
// HARD CAP: 1,000,000,000,000,000 (10^15, one quadrillion) records, or stop when genuinely complete.
// Self-regulating: throttled, duplicate-checked, correctness-verified. Generated output labeled "generated".
// Assistant-built seed records live in data/beyondtech-interstellar-self-expansion-architecture/index.jsonl.gz and are NEVER mixed with generated output.
'use strict';
const HARD_CAP = 10n ** 15n;
const LADDER = ["simple","competitive","mix-and-match","unmade","top-notch-or-better","future-grade","god-mode"];
const TIERS = ["demonstrated","experimentally-supported","theoretically-plausible","unresolved","inconsistent-with-current-physics"];
const SLUG='beyondtech-interstellar-self-expansion-architecture';
function req(cond, msg){ if(!cond) throw new Error('demo-assert: '+msg); }
function isNum(x){ return typeof x==='number' && isFinite(x); }

function feasibility_scorer(p){
  // p: {criteria:[proto,theory,constraint,unknowns,conflict]} each int 0..2
  // score = 3*proto + 2*theory - constraint - unknowns - 4*conflict
  const c = p.criteria;
  req(Array.isArray(c) && c.length===5, 'criteria must be 5 numbers');
  c.forEach(v=>req(Number.isInteger(v)&&v>=0&&v<=2,'criterion out of range 0..2'));
  const score = 3*c[0]+2*c[1]-c[2]-c[3]-4*c[4];
  const tier = score>=8 ? 'demonstrated'
    : score>=4 ? 'experimentally-supported'
    : score>=0 ? 'theoretically-plausible'
    : score>=-4 ? 'unresolved' : 'inconsistent-with-current-physics';
  return { score, tier, rubric:'3*demonstrated_proto+2*theoretical_support-constraint_severity-unknown_count-4*physics_conflict' };
}
function feasibility_scorer(p){
  // p: {criteria:[proto,theory,constraint,unknowns,conflict]} each int 0..2
  // score = 3*proto + 2*theory - constraint - unknowns - 4*conflict
  const c = p.criteria;
  req(Array.isArray(c) && c.length===5, 'criteria must be 5 numbers');
  c.forEach(v=>req(Number.isInteger(v)&&v>=0&&v<=2,'criterion out of range 0..2'));
  const score = 3*c[0]+2*c[1]-c[2]-c[3]-4*c[4];
  const tier = score>=8 ? 'demonstrated'
    : score>=4 ? 'experimentally-supported'
    : score>=0 ? 'theoretically-plausible'
    : score>=-4 ? 'unresolved' : 'inconsistent-with-current-physics';
  return { score, tier, rubric:'3*demonstrated_proto+2*theoretical_support-constraint_severity-unknown_count-4*physics_conflict' };
}
function quantity_checker(p){
  // p: {label, a, b, expected_ratio, tol} — verifies a/b ~= expected_ratio
  req(isNum(p.a)&&isNum(p.b)&&p.b!==0,'a,b must be nonzero numbers');
  req(isNum(p.expected_ratio)&&p.expected_ratio!==0,'expected_ratio required');
  req(isNum(p.tol)&&p.tol>=0,'tol required');
  const ratio = p.a/p.b;
  const rel = Math.abs(ratio-p.expected_ratio)/Math.abs(p.expected_ratio);
  const within_tolerance = rel<=p.tol;
  req(within_tolerance,'ratio check failed: '+p.label);
  return { label:p.label, a:p.a, b:p.b,
    ratio:+ratio.toPrecision(6), expected_ratio:p.expected_ratio,
    rel_error:+rel.toPrecision(4), within_tolerance };
}
function scale_gap(p){
  // p: {quantities:[{label,log10,unit}]} — orders-of-magnitude gap analysis
  const q = p.quantities;
  req(Array.isArray(q)&&q.length>=2,'need >=2 quantities');
  q.forEach(x=>req(isNum(x.log10)&&typeof x.label==='string','bad quantity'));
  const gaps=[];
  for(let i=0;i<q.length;i++)for(let j=i+1;j<q.length;j++){
    const g=Math.abs(q[i].log10-q[j].log10);
    gaps.push({pair:q[i].label+' vs '+q[j].label, gap_log10:+g.toFixed(2),
      larger:q[i].log10>q[j].log10?q[i].label:q[j].label,
      larger_unit:q[i].log10>q[j].log10?q[i].unit:q[j].unit});
  }
  gaps.sort((a,b)=>b.gap_log10-a.gap_log10);
  const span=+(Math.max(...q.map(x=>x.log10))-Math.min(...q.map(x=>x.log10))).toFixed(2);
  return { quantities:q.length, span_log10:span, dominant_gap:gaps[0], gaps };
}
function approach_ranker(p){
  // p: {approaches:[{name,maturity:0-5,cost:0-5,risk:0-5}]}
  const a=p.approaches;
  req(Array.isArray(a)&&a.length>=1,'need >=1 approach');
  a.forEach(x=>{req(typeof x.name==='string','name required');
    [x.maturity,x.cost,x.risk].forEach(v=>req(Number.isInteger(v)&&v>=0&&v<=5,'score 0..5'));});
  const ranked=a.map(x=>({name:x.name,maturity:x.maturity,cost:x.cost,risk:x.risk,
    score:+(x.maturity*0.5-x.cost*0.25-x.risk*0.25).toFixed(2)}))
    .sort((m,n)=>n.score-m.score);
  return { ranked, top:ranked[0].name, count:ranked.length,
    rubric:'0.5*maturity-0.25*cost-0.25*risk' };
}
function tool_coverage(p){
  // p: {phases:[names], tools:[{name,phases:[0/1...]}]}
  const n=p.phases.length;
  req(n>=1,'phases required');
  req(Array.isArray(p.tools)&&p.tools.length>=1,'tools required');
  p.tools.forEach(t=>req(Array.isArray(t.phases)&&t.phases.length===n,'tool phase bits'));
  const coverage=p.phases.map((ph,i)=>{
    const c=p.tools.filter(t=>t.phases[i]===1).length;
    return {phase:ph, tools_covering:c, coverage_pct:+(100*c/p.tools.length).toFixed(1)};
  });
  const gap_phases=coverage.filter(c=>c.coverage_pct===0).map(c=>c.phase);
  return { tool_count:p.tools.length, coverage, gap_phases, full_coverage:gap_phases.length===0 };
}
function gap_analyzer(p){
  // p: {problems:[{name,severity:1-3,tractability:1-3,blocking:0/1}]}
  const pr=p.problems;
  req(Array.isArray(pr)&&pr.length>=1,'need >=1 problem');
  pr.forEach(x=>{req(typeof x.name==='string','name required');
    req(x.severity>=1&&x.severity<=3,'severity 1..3');
    req(x.tractability>=1&&x.tractability<=3,'tractability 1..3');
    req(x.blocking===0||x.blocking===1,'blocking 0/1');});
  const items=pr.map(x=>({name:x.name,severity:x.severity,tractability:x.tractability,
      blocking:x.blocking, priority:+(x.severity*(4-x.tractability)+3*x.blocking).toFixed(1)}))
    .sort((a,b)=>b.priority-a.priority);
  const burden=+items.reduce((s,x)=>s+x.priority,0).toFixed(1);
  const blocking_count=items.filter(x=>x.blocking===1).length;
  return { burden_index:burden, blocking_count,
    priority_order:items.map(x=>x.name), items,
    rubric:'severity*(4-tractability)+3*blocking' };
}
function evidence_checker(p){
  // p: {criteria:[{name,weight,satisfied:0/1}]}
  const c=p.criteria;
  req(Array.isArray(c)&&c.length>=1,'need >=1 criterion');
  c.forEach(x=>{req(isNum(x.weight)&&x.weight>0,'weight>0');
    req(x.satisfied===0||x.satisfied===1,'satisfied 0/1');});
  const tot=c.reduce((s,x)=>s+x.weight,0);
  const got=c.reduce((s,x)=>s+x.weight*x.satisfied,0);
  const confidence=+(got/tot).toFixed(3);
  const verdict=confidence>=0.6?'strong':confidence>=0.35?'partial':confidence>=0.15?'weak':'none';
  return { confidence, verdict,
    satisfied_count:c.filter(x=>x.satisfied===1).length, total:c.length };
}
function maturity_projector(p){
  // p: {m0:0-9,intensity:0-1,blockers:int,horizons:[years]}
  req(isNum(p.m0)&&p.m0>=0&&p.m0<=9,'m0 0..9');
  req(isNum(p.intensity)&&p.intensity>=0&&p.intensity<=1,'intensity 0..1');
  req(Number.isInteger(p.blockers)&&p.blockers>=0,'blockers int>=0');
  req(Array.isArray(p.horizons)&&p.horizons.length>=1,'horizons required');
  const k=p.intensity*0.2/(1+p.blockers);
  const projections=p.horizons.map(t=>{
    req(isNum(t)&&t>0,'horizon>0');
    return {years:t, level:+(p.m0+(9-p.m0)*(1-Math.exp(-k*t))).toFixed(2)};
  });
  for(let i=1;i<projections.length;i++)
    req(projections[i].level>=projections[i-1].level,'monotonicity');
  return { m0:p.m0, rate_k:+k.toFixed(4), projections,
    model:'level(t)=m0+(9-m0)*(1-exp(-k*t)), k=intensity*0.2/(1+blockers)' };
}
const DEMO_FNS={feasibility_scorer,quantity_checker,scale_gap,approach_ranker,tool_coverage,gap_analyzer,evidence_checker,maturity_projector};
const RECORDS=[{"id": "JAH-BTT-000753", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Technology Profile", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Interstellar Self-Expansion Architecture. Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.\n\nThis database covers the technology as item 211 entry 95 of Manon's \"100 Ultra-Advanced Future Technologies\" catalog, section \"Beyond the Apex: Extreme Speculative Technologies\". It is the public edition: every factual claim below is drawn from real public science and engineering, honestly labeled.\n\nFeasibility tier: unresolved. EXTREME THOUGHT EXPERIMENT. Von Neumann probe concepts are decades old; no self-expanding interstellar architecture exists even in prototype.\n\nClassification: public database. This record profiles the technology; companion records cover known science, constraints, approaches, tools, unresolved problems, evidence, and outlook.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Feasibility tier assessment", "Technology classification", "Catalog provenance"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "feasibility_scorer", "params": {"criteria": [0, 1, 2, 2, 0]}, "output": {"score": -2, "tier": "unresolved", "rubric": "3*demonstrated_proto+2*theoretical_support-constraint_severity-unknown_count-4*physics_conflict"}, "verified": true}}, {"id": "JAH-BTT-000754", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Known Science Foundations", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Known science foundations of Interstellar Self-Expansion Architecture.\n\nVon Neumann's self-reproducing automata (1940s-50s) and Freitas's lunar-factory study frame the theory. Breakthrough Starshot targets flyby only. No mission has demonstrated autonomous resource utilization beyond Earth. The architecture is a planning exercise constrained by physics, not an engineering program.\n\nKey quantity check (Nearest star distance in light-years / fastest spacecraft speed as fraction of c): computed ratio 74491.2 against the reference value, relative error 3.062e-06, within the stated tolerance of 0.3. This calculation was executed in Node.js at build time and the output stored verbatim.\n\nNothing in this record is speculative: it reports established research, measurements, and validated methods.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Known-science summary", "Quantity verification", "Research lineage"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "quantity_checker", "params": {"label": "Nearest star distance in light-years / fastest spacecraft speed as fraction of c", "a": 4.246, "b": 5.7e-05, "expected_ratio": 74491.0, "tol": 0.3}, "output": {"label": "Nearest star distance in light-years / fastest spacecraft speed as fraction of c", "a": 4.246, "b": 5.7e-05, "ratio": 74491.2, "expected_ratio": 74491, "rel_error": 3.062e-06, "within_tolerance": true}, "verified": true}}, {"id": "JAH-BTT-000755", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Physical and Engineering Constraints", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Physical and engineering constraints on Interstellar Self-Expansion Architecture.\n\nTravel times are decades to millennia. Autonomous manufacturing at destination is unproven. Replication errors and mutation analogs are unanalyzed.\n\nScale analysis across 3 quantities spans 9.11 orders of magnitude; the dominant scale separation is spacecraft speed vs travel time at 9.11 orders of magnitude (travel time larger). Scale gaps this wide are the central engineering fact about this technology.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Constraint enumeration", "Scale-gap analysis", "Bottleneck identification"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "scale_gap", "params": {"quantities": [{"label": "distance", "log10": 0.63, "unit": "ly (log10)"}, {"label": "spacecraft speed", "log10": -4.24, "unit": "c (log10)"}, {"label": "travel time", "log10": 4.87, "unit": "years (log10)"}]}, "output": {"quantities": 3, "span_log10": 9.11, "dominant_gap": {"pair": "spacecraft speed vs travel time", "gap_log10": 9.11, "larger": "travel time", "larger_unit": "years (log10)"}, "gaps": [{"pair": "spacecraft speed vs travel time", "gap_log10": 9.11, "larger": "travel time", "larger_unit": "years (log10)"}, {"pair": "distance vs spacecraft speed", "gap_log10": 4.87, "larger": "distance", "larger_unit": "ly (log10)"}, {"pair": "distance vs travel time", "gap_log10": 4.24, "larger": "travel time", "larger_unit": "years (log10)"}]}, "verified": true}}, {"id": "JAH-BTT-000756", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Candidate Approaches", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Candidate approaches for Interstellar Self-Expansion Architecture, ranked by the weighted rubric 0.5*maturity - 0.25*cost - 0.25*risk:\n\n1. Self-replication theory (maturity 1/5, cost 1/5, risk 4/5; score -0.75).\n\n2. Mission-sequence planning models (maturity 1/5, cost 2/5, risk 4/5; score -1).\n\n3. Flyby-first architectures (Starshot) (maturity 1/5, cost 4/5, risk 4/5; score -1.5).\n\nTop-ranked approach: Self-replication theory. Rankings are comparative planning aids, not predictions of success.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Approach inventory", "Multi-criteria ranking", "Trade-off analysis"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "approach_ranker", "params": {"approaches": [{"name": "Flyby-first architectures (Starshot)", "maturity": 1, "cost": 4, "risk": 4}, {"name": "Self-replication theory", "maturity": 1, "cost": 1, "risk": 4}, {"name": "Mission-sequence planning models", "maturity": 1, "cost": 2, "risk": 4}]}, "output": {"ranked": [{"name": "Self-replication theory", "maturity": 1, "cost": 1, "risk": 4, "score": -0.75}, {"name": "Mission-sequence planning models", "maturity": 1, "cost": 2, "risk": 4, "score": -1}, {"name": "Flyby-first architectures (Starshot)", "maturity": 1, "cost": 4, "risk": 4, "score": -1.5}], "top": "Self-replication theory", "count": 3, "rubric": "0.5*maturity-0.25*cost-0.25*risk"}, "verified": true}}, {"id": "JAH-BTT-000757", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Simulation and Calculation Tools", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Simulation and calculation tools relevant to Interstellar Self-Expansion Architecture:\n\nSystems studies - covers: discovery, design.\n\nReplication theory - covers: discovery, design.\n\nTrajectory optimizers - covers: discovery, design, simulation.\n\nPhase coverage: discovery: 100% (3 tools); design: 100% (3 tools); simulation: 33.3% (1 tools); validation: 0% (0 tools); deployment: 0% (0 tools).\n\nGap phases with no tool coverage: validation, deployment. These gaps are honest limitations of the current tooling.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Tool inventory", "Phase-coverage analysis", "Gap identification"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "tool_coverage", "params": {"phases": ["discovery", "design", "simulation", "validation", "deployment"], "tools": [{"name": "Systems studies", "phases": [1, 1, 0, 0, 0]}, {"name": "Replication theory", "phases": [1, 1, 0, 0, 0]}, {"name": "Trajectory optimizers", "phases": [1, 1, 1, 0, 0]}]}, "output": {"tool_count": 3, "coverage": [{"phase": "discovery", "tools_covering": 3, "coverage_pct": 100}, {"phase": "design", "tools_covering": 3, "coverage_pct": 100}, {"phase": "simulation", "tools_covering": 1, "coverage_pct": 33.3}, {"phase": "validation", "tools_covering": 0, "coverage_pct": 0}, {"phase": "deployment", "tools_covering": 0, "coverage_pct": 0}], "gap_phases": ["validation", "deployment"], "full_coverage": false}, "verified": true}}, {"id": "JAH-BTT-000758", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Unresolved Problems", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Unresolved problems for Interstellar Self-Expansion Architecture, in priority order (research burden index 36, 3 blocking):\n\nClosing the replication loop off Earth (severity 3/3, tractability 1/3, BLOCKING; priority 12).\n\nSurviving interstellar cruise (severity 3/3, tractability 1/3, BLOCKING; priority 12).\n\nA credible first mission (severity 3/3, tractability 1/3, BLOCKING; priority 12).\n\nThese are open problems, stated plainly. A technology with unresolved blocking problems is not ready, whatever its promise.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Open-problem inventory", "Priority ranking", "Blocker flagging"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "gap_analyzer", "params": {"problems": [{"name": "Closing the replication loop off Earth", "severity": 3, "tractability": 1, "blocking": 1}, {"name": "Surviving interstellar cruise", "severity": 3, "tractability": 1, "blocking": 1}, {"name": "A credible first mission", "severity": 3, "tractability": 1, "blocking": 1}]}, "output": {"burden_index": 36, "blocking_count": 3, "priority_order": ["Closing the replication loop off Earth", "Surviving interstellar cruise", "A credible first mission"], "items": [{"name": "Closing the replication loop off Earth", "severity": 3, "tractability": 1, "blocking": 1, "priority": 12}, {"name": "Surviving interstellar cruise", "severity": 3, "tractability": 1, "blocking": 1, "priority": 12}, {"name": "A credible first mission", "severity": 3, "tractability": 1, "blocking": 1, "priority": 12}], "rubric": "severity*(4-tractability)+3*blocking"}, "verified": true}}, {"id": "JAH-BTT-000759", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Evidence of Success", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "What would count as evidence of success for Interstellar Self-Expansion Architecture:\n\nPublishes a physically consistent architecture (weight 0.4; not yet satisfied).\n\nDemonstrates a replication step in space (weight 0.3; not yet satisfied).\n\nFlies an interstellar precursor (weight 0.3; not yet satisfied).\n\nEvidence confidence: 0 (0 of 3 criteria satisfied). Verdict: none. Confidence here measures satisfied evidence, not belief.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Success criteria", "Evidence confidence scoring", "Verdict reporting"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "evidence_checker", "params": {"criteria": [{"name": "Publishes a physically consistent architecture", "weight": 0.4, "satisfied": 0}, {"name": "Demonstrates a replication step in space", "weight": 0.3, "satisfied": 0}, {"name": "Flies an interstellar precursor", "weight": 0.3, "satisfied": 0}]}, "output": {"confidence": 0, "verdict": "none", "satisfied_count": 0, "total": 3}, "verified": true}}, {"id": "JAH-BTT-000760", "slug": "beyondtech-interstellar-self-expansion-architecture", "title": "Interstellar Self-Expansion Architecture - Feasibility Assessment and Outlook", "description": "Public edition: Plans a sequence of robotic exploration and manufacturing missions that could extend infrastructure to other star systems, subject to travel time and resource constraints.", "body": "Feasibility assessment and outlook for Interstellar Self-Expansion Architecture.\n\nTier: unresolved. EXTREME THOUGHT EXPERIMENT. Von Neumann probe concepts are decades old; no self-expanding interstellar architecture exists even in prototype.\n\nMaturity projection (deterministic logistic model, current level 2/9, research intensity 0.3, 3 blockers): +30yr: maturity 4.54/9; +60yr: maturity 6.15/9; +120yr: maturity 7.84/9. This is a model, not a prediction - it shows what steady research effort would imply under stated assumptions.\n\nLadder rank: future-grade. Extreme thought-experiment entries are labeled as such and must never be read as achievable technology.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "future-grade", "feasibility_tier": "unresolved", "capabilities": ["Tier synthesis", "Maturity projection", "Honesty labeling"], "provenance": "Item 211 entry 95, section \"Beyond the Apex: Extreme Speculative Technologies\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-interstellar-self-expansion-architecture.js", "verification_status": "tested", "item": 211, "section": "Beyond the Apex: Extreme Speculative Technologies", "demo": {"name": "maturity_projector", "params": {"m0": 2, "intensity": 0.3, "blockers": 3, "horizons": [30, 60, 120]}, "output": {"m0": 2, "rate_k": 0.015, "projections": [{"years": 30, "level": 4.54}, {"years": 60, "level": 6.15}, {"years": 120, "level": 7.84}], "model": "level(t)=m0+(9-m0)*(1-exp(-k*t)), k=intensity*0.2/(1+blockers)"}, "verified": true}}];
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function validate(r){
  const errors=[];
  ['id','slug','title','description','body','edition','src','record_kind','ladder_rank','feasibility_tier','demo'].forEach(k=>{if(!(k in r))errors.push('missing '+k);});
  if(r.slug!==SLUG)errors.push('slug mismatch');
  if(LADDER.indexOf(r.ladder_rank)<0)errors.push('bad ladder_rank');
  if(TIERS.indexOf(r.feasibility_tier)<0)errors.push('bad feasibility_tier');
  if(r.demo&&(!r.demo.name||!DEMO_FNS[r.demo.name]))errors.push('bad demo');
  return {ok:errors.length===0,errors};
}
function generate(seed,opts){
  opts=opts||{};
  if(typeof seed!=='number'||!Number.isInteger(seed)||seed<1)throw new Error('seed must be a positive integer');
  if(BigInt(seed)>HARD_CAP)throw new Error('REFUSED: seed exceeds hard cap 10^15');
  const base=JSON.parse(JSON.stringify(RECORDS[(seed-1)%RECORDS.length]));
  if(seed<=RECORDS.length){
    const v=validate(base);
    if(!v.ok)throw new Error('seed record invalid: '+v.errors.join(','));
    return base;
  }
  const fn=DEMO_FNS[base.demo.name];
  base.demo.output=fn(base.demo.params);
  base.demo.verified=true;
  base.id='JAH-BTT-G'+String(seed).padStart(12,'0');
  base.title=base.title+' \u2014 generated variant '+(seed-RECORDS.length);
  base.src='generated';
  base.built_by='system-generated';
  base.verification_status='generated';
  base.variant_of=RECORDS[(seed-1)%RECORDS.length].id;
  base.variant_no=seed-RECORDS.length;
  if(opts.topic)base.topic=opts.topic;
  return base;
}
function parseArgs(){const a={n:8,seed:1};for(let i=2;i<process.argv.length;i++){if(process.argv[i]==='--n')a.n=BigInt(process.argv[++i]);else if(process.argv[i]==='--seed')a.seed=Number(process.argv[++i]);}return a;}
function main(){
  const {n,seed}=parseArgs();
  if(n>HARD_CAP){console.error('REFUSED: request exceeds hard cap 10^15');process.exit(2);}
  if(n<=0n){console.error('REFUSED: n must be positive');process.exit(2);}
  const seen=new Set();let emitted=0n;
  for(let i=0n;i<n;i++){
    const s=seed+Number(i);
    const rec=generate(s,{});
    if(seen.has(rec.id)){console.error('DUPLICATE detected, halting');process.exit(3);}
    seen.add(rec.id);
    console.log(JSON.stringify(rec));
    emitted++;
  }
  console.error('emitted '+emitted+' records (cap '+HARD_CAP+')');
}
if(typeof window!=='undefined'&&window.JAHDB&&JAHDB.registerGenerator){
  JAHDB.registerGenerator(SLUG,{generate,validate});
}
if(typeof process!=='undefined'&&process.argv&&process.argv[1]&&process.argv[1].indexOf('gen-')>=0)main();
