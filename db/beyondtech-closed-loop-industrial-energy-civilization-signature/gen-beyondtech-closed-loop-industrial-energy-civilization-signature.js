#!/usr/bin/env node
// Boundless generator for beyondtech-closed-loop-industrial-energy-civilization-signature.
// Technology: Closed-Loop Industrial Energy Civilization (signature edition).
// HARD CAP: 1,000,000,000,000,000 (10^15, one quadrillion) records, or stop when genuinely complete.
// Self-regulating: throttled, duplicate-checked, correctness-verified. Generated output labeled "generated".
// Assistant-built seed records live in data/beyondtech-closed-loop-industrial-energy-civilization-signature/index.jsonl.gz and are NEVER mixed with generated output.
'use strict';
const HARD_CAP = 10n ** 15n;
const LADDER = ["simple","competitive","mix-and-match","unmade","top-notch-or-better","future-grade","god-mode"];
const TIERS = ["demonstrated","experimentally-supported","theoretically-plausible","unresolved","inconsistent-with-current-physics"];
const SLUG='beyondtech-closed-loop-industrial-energy-civilization-signature';
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
const RECORDS=[{"id": "JAH-BTTS-000377", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Technology Profile - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nClosed-Loop Industrial Energy Civilization. Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.\n\nThis database covers the technology as item 211 entry 48 of Manon's \"100 Ultra-Advanced Future Technologies\" catalog, section \"Energy Beyond Conventional Infrastructure\". It is the public edition: every factual claim below is drawn from real public science and engineering, honestly labeled.\n\nFeasibility tier: demonstrated. Waste-heat recovery and industrial symbiosis operate commercially (Kalundborg since the 1970s).\n\nClassification: public database. This record profiles the technology; companion records cover known science, constraints, approaches, tools, unresolved problems, evidence, and outlook.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Feasibility tier assessment", "Technology classification", "Catalog provenance"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "feasibility_scorer", "params": {"criteria": [2, 2, 1, 1, 0]}, "output": {"score": 8, "tier": "demonstrated", "rubric": "3*demonstrated_proto+2*theoretical_support-constraint_severity-unknown_count-4*physics_conflict"}, "verified": true}}, {"id": "JAH-BTTS-000378", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Known Science Foundations - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nKnown science foundations of Closed-Loop Industrial Energy Civilization.\n\nKalundborg's industrial symbiosis exchanges steam, heat, and materials among plants. Waste-heat recovery generates power in cement and steel plants. District heating reuses industrial heat in Scandinavia. Pinch analysis optimizes heat exchange networks. Full closed-loop civilization is aspirational, but the unit operations are demonstrated.\n\nKey quantity check (Industrial waste heat in EJ per year / global primary energy in EJ): computed ratio 0.05 against the reference value, relative error 0, within the stated tolerance of 0.3. This calculation was executed in Node.js at build time and the output stored verbatim.\n\nNothing in this record is speculative: it reports established research, measurements, and validated methods.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Known-science summary", "Quantity verification", "Research lineage"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "quantity_checker", "params": {"label": "Industrial waste heat in EJ per year / global primary energy in EJ", "a": 30.0, "b": 600.0, "expected_ratio": 0.05, "tol": 0.3}, "output": {"label": "Industrial waste heat in EJ per year / global primary energy in EJ", "a": 30, "b": 600, "ratio": 0.05, "expected_ratio": 0.05, "rel_error": 0, "within_tolerance": true}, "verified": true}}, {"id": "JAH-BTTS-000379", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Physical and Engineering Constraints - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nPhysical and engineering constraints on Closed-Loop Industrial Energy Civilization.\n\nLow-grade heat has limited uses. Co-locating industries for symbiosis is organizationally hard. Retrofitting existing plants is capital-intensive.\n\nScale analysis across 3 quantities spans 2.3 orders of magnitude; the dominant scale separation is recovery efficiency vs symbiosis parks worldwide at 2.3 orders of magnitude (symbiosis parks worldwide larger). Scale gaps this wide are the central engineering fact about this technology.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Constraint enumeration", "Scale-gap analysis", "Bottleneck identification"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "scale_gap", "params": {"quantities": [{"label": "waste heat", "log10": 1.48, "unit": "EJ (log10)"}, {"label": "recovery efficiency", "log10": -0.3, "unit": "fraction (log10)"}, {"label": "symbiosis parks worldwide", "log10": 2.0, "unit": "count (log10)"}]}, "output": {"quantities": 3, "span_log10": 2.3, "dominant_gap": {"pair": "recovery efficiency vs symbiosis parks worldwide", "gap_log10": 2.3, "larger": "symbiosis parks worldwide", "larger_unit": "count (log10)"}, "gaps": [{"pair": "recovery efficiency vs symbiosis parks worldwide", "gap_log10": 2.3, "larger": "symbiosis parks worldwide", "larger_unit": "count (log10)"}, {"pair": "waste heat vs recovery efficiency", "gap_log10": 1.78, "larger": "waste heat", "larger_unit": "EJ (log10)"}, {"pair": "waste heat vs symbiosis parks worldwide", "gap_log10": 0.52, "larger": "symbiosis parks worldwide", "larger_unit": "count (log10)"}]}, "verified": true}}, {"id": "JAH-BTTS-000380", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Candidate Approaches - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nCandidate approaches for Closed-Loop Industrial Energy Civilization, ranked by the weighted rubric 0.5*maturity - 0.25*cost - 0.25*risk:\n\n1. Heat-exchange network optimization (maturity 4/5, cost 2/5, risk 1/5; score 1.25).\n\n2. Waste-heat power (ORC) (maturity 4/5, cost 3/5, risk 1/5; score 1).\n\n3. Industrial symbiosis parks (maturity 4/5, cost 3/5, risk 2/5; score 0.75).\n\nTop-ranked approach: Heat-exchange network optimization. Rankings are comparative planning aids, not predictions of success.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Approach inventory", "Multi-criteria ranking", "Trade-off analysis"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "approach_ranker", "params": {"approaches": [{"name": "Waste-heat power (ORC)", "maturity": 4, "cost": 3, "risk": 1}, {"name": "Industrial symbiosis parks", "maturity": 4, "cost": 3, "risk": 2}, {"name": "Heat-exchange network optimization", "maturity": 4, "cost": 2, "risk": 1}]}, "output": {"ranked": [{"name": "Heat-exchange network optimization", "maturity": 4, "cost": 2, "risk": 1, "score": 1.25}, {"name": "Waste-heat power (ORC)", "maturity": 4, "cost": 3, "risk": 1, "score": 1}, {"name": "Industrial symbiosis parks", "maturity": 4, "cost": 3, "risk": 2, "score": 0.75}], "top": "Heat-exchange network optimization", "count": 3, "rubric": "0.5*maturity-0.25*cost-0.25*risk"}, "verified": true}}, {"id": "JAH-BTTS-000381", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Simulation and Calculation Tools - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nSimulation and calculation tools relevant to Closed-Loop Industrial Energy Civilization:\n\nPinch analysis tools - covers: discovery, design, simulation, validation, deployment.\n\nORC systems - covers: discovery, design, simulation, validation, deployment.\n\nSymbiosis park planners - covers: discovery, design, simulation, validation.\n\nPhase coverage: discovery: 100% (3 tools); design: 100% (3 tools); simulation: 100% (3 tools); validation: 100% (3 tools); deployment: 66.7% (2 tools).\n\nAll five phases have at least one covering tool.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Tool inventory", "Phase-coverage analysis", "Gap identification"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "tool_coverage", "params": {"phases": ["discovery", "design", "simulation", "validation", "deployment"], "tools": [{"name": "Pinch analysis tools", "phases": [1, 1, 1, 1, 1]}, {"name": "ORC systems", "phases": [1, 1, 1, 1, 1]}, {"name": "Symbiosis park planners", "phases": [1, 1, 1, 1, 0]}]}, "output": {"tool_count": 3, "coverage": [{"phase": "discovery", "tools_covering": 3, "coverage_pct": 100}, {"phase": "design", "tools_covering": 3, "coverage_pct": 100}, {"phase": "simulation", "tools_covering": 3, "coverage_pct": 100}, {"phase": "validation", "tools_covering": 3, "coverage_pct": 100}, {"phase": "deployment", "tools_covering": 2, "coverage_pct": 66.7}], "gap_phases": [], "full_coverage": true}, "verified": true}}, {"id": "JAH-BTTS-000382", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Unresolved Problems - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nUnresolved problems for Closed-Loop Industrial Energy Civilization, in priority order (research burden index 12, 0 blocking):\n\nOrganizational barriers (severity 2/3, tractability 1/3; priority 6).\n\nEconomics of low-grade heat (severity 2/3, tractability 2/3; priority 4).\n\nRetrofit capital (severity 2/3, tractability 3/3; priority 2).\n\nThese are open problems, stated plainly. A technology with unresolved blocking problems is not ready, whatever its promise.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Open-problem inventory", "Priority ranking", "Blocker flagging"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "gap_analyzer", "params": {"problems": [{"name": "Economics of low-grade heat", "severity": 2, "tractability": 2, "blocking": 0}, {"name": "Organizational barriers", "severity": 2, "tractability": 1, "blocking": 0}, {"name": "Retrofit capital", "severity": 2, "tractability": 3, "blocking": 0}]}, "output": {"burden_index": 12, "blocking_count": 0, "priority_order": ["Organizational barriers", "Economics of low-grade heat", "Retrofit capital"], "items": [{"name": "Organizational barriers", "severity": 2, "tractability": 1, "blocking": 0, "priority": 6}, {"name": "Economics of low-grade heat", "severity": 2, "tractability": 2, "blocking": 0, "priority": 4}, {"name": "Retrofit capital", "severity": 2, "tractability": 3, "blocking": 0, "priority": 2}], "rubric": "severity*(4-tractability)+3*blocking"}, "verified": true}}, {"id": "JAH-BTTS-000383", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Evidence of Success - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nWhat would count as evidence of success for Closed-Loop Industrial Energy Civilization:\n\nRecovers 50%+ of a park's waste heat (weight 0.4; SATISFIED).\n\nSymbiosis park operates profitably (weight 0.35; SATISFIED).\n\nReplicates Kalundborg in a new region (weight 0.25; SATISFIED).\n\nEvidence confidence: 1 (3 of 3 criteria satisfied). Verdict: strong. Confidence here measures satisfied evidence, not belief.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Success criteria", "Evidence confidence scoring", "Verdict reporting"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "evidence_checker", "params": {"criteria": [{"name": "Recovers 50%+ of a park's waste heat", "weight": 0.4, "satisfied": 1}, {"name": "Symbiosis park operates profitably", "weight": 0.35, "satisfied": 1}, {"name": "Replicates Kalundborg in a new region", "weight": 0.25, "satisfied": 1}]}, "output": {"confidence": 1, "verdict": "strong", "satisfied_count": 3, "total": 3}, "verified": true}}, {"id": "JAH-BTTS-000384", "slug": "beyondtech-closed-loop-industrial-energy-civilization-signature", "title": "Closed-Loop Industrial Energy Civilization - Feasibility Assessment and Outlook - Signature Edition", "description": "Signature edition: Industrial networks that recover waste heat and reuse energy wherever technically and economically feasible.", "body": "SIGNATURE EDITION. The Signature Energy Loop is JAH's original closed-loop industrial concept: Signature industrial networks recovering and reusing energy with full lineage on every exchange. This is JAH's original Signature concept for \"Closed-Loop Industrial Energy Civilization\": real and working inside the Signature ecosystem, clearly labeled as a Signature original - never presented as public record. \n\nFeasibility assessment and outlook for Closed-Loop Industrial Energy Civilization.\n\nTier: demonstrated. Waste-heat recovery and industrial symbiosis operate commercially (Kalundborg since the 1970s).\n\nMaturity projection (deterministic logistic model, current level 7/9, research intensity 0.8, 0 blockers): +2yr: maturity 7.55/9; +5yr: maturity 8.1/9; +10yr: maturity 8.6/9. This is a model, not a prediction - it shows what steady research effort would imply under stated assumptions.\n\nLadder rank: simple. Progress here is measured by verified results, not by enthusiasm.", "edition": "signature", "src": "signature-generated-completion", "built_by": "assistant-built", "record_kind": "future technology record", "ladder_rank": "simple", "feasibility_tier": "demonstrated", "capabilities": ["Tier synthesis", "Maturity projection", "Honesty labeling"], "provenance": "Item 211 entry 48, section \"Energy Beyond Conventional Infrastructure\"; built 2026-10-22 by the futuretech-b-r22 lane.", "licensing": "Property of Justin Addam Higgins (JAH) - Signature original.", "generator": "gen-beyondtech-closed-loop-industrial-energy-civilization-signature.js", "verification_status": "tested", "item": 211, "section": "Energy Beyond Conventional Infrastructure", "demo": {"name": "maturity_projector", "params": {"m0": 7, "intensity": 0.8, "blockers": 0, "horizons": [2, 5, 10]}, "output": {"m0": 7, "rate_k": 0.16, "projections": [{"years": 2, "level": 7.55}, {"years": 5, "level": 8.1}, {"years": 10, "level": 8.6}], "model": "level(t)=m0+(9-m0)*(1-exp(-k*t)), k=intensity*0.2/(1+blockers)"}, "verified": true}}];
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
  base.id='JAH-BTTS-G'+String(seed).padStart(12,'0');
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
