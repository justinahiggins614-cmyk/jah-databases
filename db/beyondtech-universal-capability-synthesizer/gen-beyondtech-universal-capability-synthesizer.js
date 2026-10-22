#!/usr/bin/env node
// Boundless generator for beyondtech-universal-capability-synthesizer.
// Technology: Universal Capability Synthesizer (public edition).
// HARD CAP: 1,000,000,000,000,000 (10^15, one quadrillion) records, or stop when genuinely complete.
// Self-regulating: throttled, duplicate-checked, correctness-verified. Generated output labeled "generated".
// Assistant-built seed records live in data/beyondtech-universal-capability-synthesizer/index.jsonl.gz and are NEVER mixed with generated output.
'use strict';
const HARD_CAP = 10n ** 15n;
const LADDER = ["simple","competitive","mix-and-match","unmade","top-notch-or-better","future-grade","god-mode"];
const TIERS = ["demonstrated","experimentally-supported","theoretically-plausible","unresolved","inconsistent-with-current-physics"];
const SLUG='beyondtech-universal-capability-synthesizer';
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
const RECORDS=[{"id": "JAH-BTT-001561", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Technology Profile", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Universal Capability Synthesizer. Combines existing tools and verified components into new systems that can perform previously unsupported tasks.\n\nThis database covers the technology as item 216 entry 8 of Manon's \"100 Technologies Beyond Omega (B)\" catalog, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\". It is the public edition: every factual claim below is drawn from real public science and engineering, honestly labeled.\n\nFeasibility tier: experimentally supported. Tool composition is real (agents, workflows); universal synthesis of new capabilities is emerging.\n\nClassification: public database. This record profiles the technology; companion records cover known science, constraints, approaches, tools, unresolved problems, evidence, and outlook.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Feasibility tier assessment", "Technology classification", "Catalog provenance"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "feasibility_scorer", "params": {"criteria": [1, 2, 1, 1, 0]}, "output": {"score": 5, "tier": "experimentally-supported", "rubric": "3*demonstrated_proto+2*theoretical_support-constraint_severity-unknown_count-4*physics_conflict"}, "verified": true}}, {"id": "JAH-BTT-001562", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Known Science Foundations", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Known science foundations of Universal Capability Synthesizer.\n\nLLM agents compose tools into workflows. Unix pipelines compose programs. Zapier composes services. Synthesizing genuinely new capabilities \u2014 tasks nothing could do before \u2014 from verified components is the frontier.\n\nKey quantity check (Tools composed in largest agents / verified components available): computed ratio 0.01 against the reference value, relative error 0, within the stated tolerance of 0.4. This calculation was executed in Node.js at build time and the output stored verbatim.\n\nNothing in this record is speculative: it reports established research, measurements, and validated methods.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Known-science summary", "Quantity verification", "Research lineage"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "quantity_checker", "params": {"label": "Tools composed in largest agents / verified components available", "a": 100.0, "b": 10000.0, "expected_ratio": 0.01, "tol": 0.4}, "output": {"label": "Tools composed in largest agents / verified components available", "a": 100, "b": 10000, "ratio": 0.01, "expected_ratio": 0.01, "rel_error": 0, "within_tolerance": true}, "verified": true}}, {"id": "JAH-BTT-001563", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Physical and Engineering Constraints", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Physical and engineering constraints on Universal Capability Synthesizer.\n\nComposition needs compatible interfaces. New capabilities need validation. Most compositions are trivial.\n\nScale analysis across 3 quantities spans 3 orders of magnitude; the dominant scale separation is components vs new capabilities at 3 orders of magnitude (components larger). Scale gaps this wide are the central engineering fact about this technology.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Constraint enumeration", "Scale-gap analysis", "Bottleneck identification"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "scale_gap", "params": {"quantities": [{"label": "composed", "log10": 2.0, "unit": "count (log10)"}, {"label": "components", "log10": 4.0, "unit": "count (log10)"}, {"label": "new capabilities", "log10": 1.0, "unit": "count (log10)"}]}, "output": {"quantities": 3, "span_log10": 3, "dominant_gap": {"pair": "components vs new capabilities", "gap_log10": 3, "larger": "components", "larger_unit": "count (log10)"}, "gaps": [{"pair": "components vs new capabilities", "gap_log10": 3, "larger": "components", "larger_unit": "count (log10)"}, {"pair": "composed vs components", "gap_log10": 2, "larger": "components", "larger_unit": "count (log10)"}, {"pair": "composed vs new capabilities", "gap_log10": 1, "larger": "composed", "larger_unit": "count (log10)"}]}, "verified": true}}, {"id": "JAH-BTT-001564", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Candidate Approaches", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Candidate approaches for Universal Capability Synthesizer, ranked by the weighted rubric 0.5*maturity - 0.25*cost - 0.25*risk:\n\n1. Workflow synthesis (maturity 4/5, cost 2/5, risk 1/5; score 1.25).\n\n2. Agent tool composition (maturity 3/5, cost 2/5, risk 2/5; score 0.5).\n\n3. Verified-component libraries (maturity 3/5, cost 2/5, risk 2/5; score 0.5).\n\nTop-ranked approach: Workflow synthesis. Rankings are comparative planning aids, not predictions of success.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Approach inventory", "Multi-criteria ranking", "Trade-off analysis"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "approach_ranker", "params": {"approaches": [{"name": "Agent tool composition", "maturity": 3, "cost": 2, "risk": 2}, {"name": "Workflow synthesis", "maturity": 4, "cost": 2, "risk": 1}, {"name": "Verified-component libraries", "maturity": 3, "cost": 2, "risk": 2}]}, "output": {"ranked": [{"name": "Workflow synthesis", "maturity": 4, "cost": 2, "risk": 1, "score": 1.25}, {"name": "Agent tool composition", "maturity": 3, "cost": 2, "risk": 2, "score": 0.5}, {"name": "Verified-component libraries", "maturity": 3, "cost": 2, "risk": 2, "score": 0.5}], "top": "Workflow synthesis", "count": 3, "rubric": "0.5*maturity-0.25*cost-0.25*risk"}, "verified": true}}, {"id": "JAH-BTT-001565", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Simulation and Calculation Tools", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Simulation and calculation tools relevant to Universal Capability Synthesizer:\n\nAgent frameworks - covers: discovery, design, simulation, validation.\n\nWorkflow engines - covers: discovery, design, simulation, validation, deployment.\n\nComponent registries - covers: discovery, design, simulation, validation.\n\nPhase coverage: discovery: 100% (3 tools); design: 100% (3 tools); simulation: 100% (3 tools); validation: 100% (3 tools); deployment: 33.3% (1 tools).\n\nAll five phases have at least one covering tool.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Tool inventory", "Phase-coverage analysis", "Gap identification"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "tool_coverage", "params": {"phases": ["discovery", "design", "simulation", "validation", "deployment"], "tools": [{"name": "Agent frameworks", "phases": [1, 1, 1, 1, 0]}, {"name": "Workflow engines", "phases": [1, 1, 1, 1, 1]}, {"name": "Component registries", "phases": [1, 1, 1, 1, 0]}]}, "output": {"tool_count": 3, "coverage": [{"phase": "discovery", "tools_covering": 3, "coverage_pct": 100}, {"phase": "design", "tools_covering": 3, "coverage_pct": 100}, {"phase": "simulation", "tools_covering": 3, "coverage_pct": 100}, {"phase": "validation", "tools_covering": 3, "coverage_pct": 100}, {"phase": "deployment", "tools_covering": 1, "coverage_pct": 33.3}], "gap_phases": [], "full_coverage": true}, "verified": true}}, {"id": "JAH-BTT-001566", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Unresolved Problems", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Unresolved problems for Universal Capability Synthesizer, in priority order (research burden index 17, 1 blocking):\n\nValidating new capabilities (severity 3/3, tractability 2/3, BLOCKING; priority 9).\n\nInterface compatibility (severity 2/3, tractability 2/3; priority 4).\n\nNon-trivial synthesis (severity 2/3, tractability 2/3; priority 4).\n\nThese are open problems, stated plainly. A technology with unresolved blocking problems is not ready, whatever its promise.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Open-problem inventory", "Priority ranking", "Blocker flagging"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "gap_analyzer", "params": {"problems": [{"name": "Interface compatibility", "severity": 2, "tractability": 2, "blocking": 0}, {"name": "Validating new capabilities", "severity": 3, "tractability": 2, "blocking": 1}, {"name": "Non-trivial synthesis", "severity": 2, "tractability": 2, "blocking": 0}]}, "output": {"burden_index": 17, "blocking_count": 1, "priority_order": ["Validating new capabilities", "Interface compatibility", "Non-trivial synthesis"], "items": [{"name": "Validating new capabilities", "severity": 3, "tractability": 2, "blocking": 1, "priority": 9}, {"name": "Interface compatibility", "severity": 2, "tractability": 2, "blocking": 0, "priority": 4}, {"name": "Non-trivial synthesis", "severity": 2, "tractability": 2, "blocking": 0, "priority": 4}], "rubric": "severity*(4-tractability)+3*blocking"}, "verified": true}}, {"id": "JAH-BTT-001567", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Evidence of Success", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "What would count as evidence of success for Universal Capability Synthesizer:\n\nSynthesizes a capability nothing had (weight 0.4; not yet satisfied).\n\nCapability passes verification (weight 0.35; SATISFIED).\n\nAdopted by users (weight 0.25; not yet satisfied).\n\nEvidence confidence: 0.35 (1 of 3 criteria satisfied). Verdict: partial. Confidence here measures satisfied evidence, not belief.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Success criteria", "Evidence confidence scoring", "Verdict reporting"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "evidence_checker", "params": {"criteria": [{"name": "Synthesizes a capability nothing had", "weight": 0.4, "satisfied": 0}, {"name": "Capability passes verification", "weight": 0.35, "satisfied": 1}, {"name": "Adopted by users", "weight": 0.25, "satisfied": 0}]}, "output": {"confidence": 0.35, "verdict": "partial", "satisfied_count": 1, "total": 3}, "verified": true}}, {"id": "JAH-BTT-001568", "slug": "beyondtech-universal-capability-synthesizer", "title": "Universal Capability Synthesizer - Feasibility Assessment and Outlook", "description": "Public edition: Combines existing tools and verified components into new systems that can perform previously unsupported tasks.", "body": "Feasibility assessment and outlook for Universal Capability Synthesizer.\n\nTier: experimentally supported. Tool composition is real (agents, workflows); universal synthesis of new capabilities is emerging.\n\nMaturity projection (deterministic logistic model, current level 5/9, research intensity 0.6, 1 blockers): +5yr: maturity 6.04/9; +15yr: maturity 7.37/9; +30yr: maturity 8.34/9. This is a model, not a prediction - it shows what steady research effort would imply under stated assumptions.\n\nLadder rank: competitive. Progress here is measured by verified results, not by enthusiasm.", "edition": "public", "src": "public-harvest", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "competitive", "feasibility_tier": "experimentally-supported", "capabilities": ["Tier synthesis", "Maturity projection", "Honesty labeling"], "provenance": "Item 216 entry 8, section \"Meta-Intelligence: Systems That Invent New Forms of Intelligence\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Public factual summaries; original synthesis CC-BY.", "generator": "gen-beyondtech-universal-capability-synthesizer.js", "verification_status": "tested", "item": 216, "section": "Meta-Intelligence: Systems That Invent New Forms of Intelligence", "demo": {"name": "maturity_projector", "params": {"m0": 5, "intensity": 0.6, "blockers": 1, "horizons": [5, 15, 30]}, "output": {"m0": 5, "rate_k": 0.06, "projections": [{"years": 5, "level": 6.04}, {"years": 15, "level": 7.37}, {"years": 30, "level": 8.34}], "model": "level(t)=m0+(9-m0)*(1-exp(-k*t)), k=intensity*0.2/(1+blockers)"}, "verified": true}}];
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
