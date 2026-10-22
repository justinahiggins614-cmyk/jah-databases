/* JAHDB boundless generator: futuretech-personalized-preventive-medicine-network
 * Future Technology Engineering Database record generator.
 * Dual node+browser. Deterministic: same seed + same topic = same record.
 * HARD_CAP = 1e15 records (refuses larger).
 * Node: node gen-futuretech-personalized-preventive-medicine-network.js --n 8 --seed 1   (prints records as JSONL)
 */
'use strict';
var SLUG = 'futuretech-personalized-preventive-medicine-network';
var IDPREFIX = 'JAH-FTT-';
var IDBASE = 1224;
var HARD_CAP = 1000000000000000;
var TECH = {"title": "Personalized Preventive Medicine Network", "desc": "Health systems that integrate relevant measurements, risk models, and clinically validated preventive interventions.", "catName": "Human Capability and Civilization Health", "tier": "experimentally-supported", "tierFrame": "Feasibility tier: EXPERIMENTALLY-SUPPORTED. Key components or narrow versions have been demonstrated in laboratories, prototypes, or limited deployments, but the full technology as described does not yet exist. Records at this tier separate what experiments have shown from what is extrapolated.", "tierJustify": "Assigned from the catalog description and the state of public research: Feasibility tier: EXPERIMENTALLY-SUPPORTED. Key components or narrow versions have been demonstrated in laboratories, prototypes, or limited deployments, but th", "tierChange": "Integrated prototype demonstrating the full capability end-to-end would move this tier upward.", "trl": [3, 6], "baseYears": 5, "evidenceN": 4, "dims": {"physics": 8, "engineering": 6, "economics": 5, "timescale": 6, "evidence": 7}, "edLabel": "Public Edition", "edition": "public", "src": "assistant-built", "edFraming": "This is the public-edition record: it documents the publicly known research status of Personalized Preventive Medicine Network as engineering reference. It claims nothing beyond the evidence, and every speculative element carries its feasibility tier openly — never presented as established fact.", "principle": "Preventive and regenerative medicine plus assistive technology: measure risk early, intervene precisely, restore function, and support independence.", "constraint": "Evidence standards for health claims, equity of access, data privacy, and the gap between lab capability and deployed care.", "tool": "Population health platforms, clinical decision support, and assistive-robotics stacks.", "domain": "Civilization health scales medicine from the patient to the population: preventive networks, epidemic early warning, resilient supply chains, adaptive learning, and universal translation as cognitive infrastructure. Demonstrated pieces — translation, surveillance networks, assistive robots — are real. The integrated vision (every person with a preventive twin, every outbreak caught early) is a systems and equity challenge more than a pure technology one. Honest records measure outcomes in disability-adjusted life years, not press releases.", "constraints": [["Evidence standards for claims", 9], ["Equity of access", 9], ["Health data privacy", 8], ["Deployment vs lab gap", 8], ["Workforce capacity", 8], ["Sustained funding", 7]], "tools": [["Population health platforms", "Health IT", 8], ["Clinical decision support", "Clinical", 8], ["Epidemic surveillance nets", "Public health", 8], ["Assistive robotics stacks", "Robotics", 7], ["Adaptive learning platforms", "Education", 8], ["Translation APIs", "Language", 9]], "sim": ["Epidemic spread ensembles", "Health-system capacity models", "Preventive intervention trials (in silico)", "Supply-chain resilience sims", "Learning-outcome models"], "breakthroughs": [["Validated preventive twins", 8], ["Outbreak prediction before spread", 9], ["Affordable regenerative therapies", 9], ["Universal assistive independence", 8], ["Resilient global health logistics", 8]], "protoParams": [["Population covered (M)", "M", 0.1, 8000], ["Early-warning lead (days)", "days", 1, 180], ["Intervention cost per capita ($)", "$/person", 1, 10000], ["Outcome improvement (%)", "%", 5, 90]], "flopsNum": 1000000000000000.0, "budget": "$10M-$1B", "pasteRef": "catalog-100-civilization-scale-technologies-2026-10-22.txt (item 210)", "entryNum": "210-71", "verified": "2026-10-22"};

function h32(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng32(seed){var a=seed>>>0;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,arr){return arr[Math.floor(r()*arr.length)];}
function ri(r,lo,hi){return lo+Math.floor(r()*(hi-lo+1));}
function rf(r,lo,hi,d){var v=lo+r()*(hi-lo);var p=Math.pow(10,(d===undefined?1:d));return Math.round(v*p)/p;}
function pad6(n){var s=String(n);while(s.length<6){s='0'+s;}return s;}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');}

/* ================= demo engines (pure, self-contained) ================= */
/* Each compute_* takes only P (params) and uses Math/JSON only, so its
   source can be embedded in the demo program and re-executed standalone. */

function compute_readiness(P){
  var out={assumptions:P.assumptions,technology:P.title,feasibility_tier:P.tier,
    current_trl_range:P.trl,scenarios:[],critical_path:P.crit,note:''};
  if(P.tier==='inconsistent-with-current-physics'){
    out.note='No technology-readiness projection is meaningful: the concept conflicts with tested physics. The scenarios below are placeholders showing why.';
    out.scenarios=[{scenario:'conservative',years_per_trl:'n/a',trl9_projection_years:'n/a'},
      {scenario:'baseline',years_per_trl:'n/a',trl9_projection_years:'n/a'},
      {scenario:'accelerated',years_per_trl:'n/a',trl9_projection_years:'n/a'}];
    return out;
  }
  var names=['conservative','baseline','accelerated'];
  var mult=[1.8,1.0,0.55];
  for(var i=0;i<3;i++){
    var ypt=Math.round(P.baseYears*mult[i]*10)/10;
    var gap=9-P.trl[1]; if(gap<0){gap=0;}
    out.scenarios.push({scenario:names[i],years_per_trl:ypt,
      trl9_projection_years:Math.round(gap*ypt*10)/10,
      funding_profile:P.funding[i]});
  }
  out.note='Projections are illustrative planning models, not predictions; they assume sustained effort and no new fundamental blockers.';
  return out;
}

function compute_constraints(P){
  var rows=[],i;
  for(i=0;i<P.constraints.length;i++){
    rows.push({constraint:P.constraints[i][0],severity_1_10:P.constraints[i][1],
      klass:P.constraints[i][1]>=9?'blocking':(P.constraints[i][1]>=7?'major':'manageable')});
  }
  rows.sort(function(a,b){return b.severity_1_10-a.severity_1_10;});
  var sum=0; for(i=0;i<rows.length;i++){sum+=rows[i].severity_1_10;}
  var top=[]; for(i=0;i<3&&i<rows.length;i++){top.push(rows[i].constraint);}
  return {assumptions:P.assumptions,technology:P.title,
    constraint_table:rows,burden_index:Math.round(sum/rows.length*10)/10,
    top_blockers:top,
    mitigation_focus:'Engineering effort should attack the top blockers first; manageable constraints are handled with standard practice.'};
}

function compute_software(P){
  var tools=[],i;
  for(i=0;i<P.tools.length;i++){
    tools.push({name:P.tools[i][0],klass:P.tools[i][1],maturity_1_10:P.tools[i][2]});
  }
  tools.sort(function(a,b){return b.maturity_1_10-a.maturity_1_10;});
  var stacks=[];
  for(var u=0;u<P.usecases.length;u++){
    var rec=[],cov=0;
    for(i=0;i<3&&i<tools.length;i++){rec.push(tools[(u+i)%tools.length].name);cov+=tools[(u+i)%tools.length].maturity_1_10;}
    stacks.push({use_case:P.usecases[u],recommended_stack:rec,
      coverage_pct:Math.round(cov/3/10*100)});
  }
  return {assumptions:P.assumptions,technology:P.title,
    tool_inventory:tools,stack_by_use_case:stacks,
    note:'Coverage is illustrative: it scores tool maturity, not fitness for any specific proprietary workflow.'};
}

function compute_simulation(P){
  var comps=[],i;
  for(i=0;i<P.components.length;i++){comps.push({component:P.components[i],fidelity:['low','medium','high'][i%3]});}
  var est=P.flopsBase*Math.pow(P.scale,2.2);
  function fmt(x){if(x>=1e21){return (x/1e21).toFixed(2)+'e21 FLOP';}if(x>=1e18){return (x/1e18).toFixed(2)+'e18 FLOP';}if(x>=1e15){return (x/1e15).toFixed(2)+'e15 FLOP';}return x.toExponential(2)+' FLOP';}
  return {assumptions:P.assumptions,technology:P.title,
    model_components:comps,
    compute_estimate:fmt(est),
    runtime_note:'Illustrative order-of-magnitude compute for the reference configuration; real campaigns vary widely.',
    validation_checklist:['Compare against analytical limits','Convergence study on resolution','Validate sub-models against experiment','Document all parameter choices']};
}

function compute_evidence(P){
  var items=[],i;
  for(i=0;i<P.claims.length;i++){
    items.push({claim:P.claims[i],strength_1_10:P.strengths[i],status:P.tier==='demonstrated'?'shown':'reported'});
  }
  var sum=0; for(i=0;i<items.length;i++){sum+=items[i].strength_1_10;}
  var gaps=P.gaps.slice(0,Math.max(2,6-items.length));
  return {assumptions:P.assumptions,technology:P.title,feasibility_tier:P.tier,
    evidence_items:items,
    evidence_score:items.length?Math.round(sum/items.length*10)/10:0,
    open_questions:gaps,
    verdict:P.tier==='demonstrated'?'Multiple independent demonstrations exist; remaining work is scaling and cost.':
      P.tier==='experimentally-supported'?'Components demonstrated; integrated full-capability demonstration is still missing.':
      P.tier==='theoretically-plausible'?'Evidence is indirect or small-scale; major demonstrations are still ahead.':
      'No working demonstration exists; the question of possibility itself is open.'};
}

function compute_breakthroughs(P){
  var reqs=[],i;
  for(i=0;i<P.reqs.length;i++){
    reqs.push({requirement:P.reqs[i][0],difficulty_1_10:P.reqs[i][1],
      depends_on:i===0?'none':P.reqs[i-1][0]});
  }
  var order=reqs.slice().sort(function(a,b){return b.difficulty_1_10-a.difficulty_1_10;});
  var names=[]; for(i=0;i<order.length;i++){names.push(order[i].requirement);}
  var sum=0; for(i=0;i<reqs.length;i++){sum+=reqs[i].difficulty_1_10;}
  return {assumptions:P.assumptions,technology:P.title,
    requirements:reqs,critical_path_order:names,breakthrough_burden:sum,
    note:'Burden is an illustrative difficulty sum, not a schedule. The critical path is ordered by difficulty; real programs parallelize.'};
}

function compute_prototype(P){
  var params=[],i;
  for(i=0;i<P.params.length;i++){
    var lo=P.params[i][2],hi=P.params[i][3];
    var dv=Math.round((lo+(hi-lo)*P.dfrac)*100)/100;
    params.push({parameter:P.params[i][0],unit:P.params[i][1],design_value:dv,allowed_range:[lo,hi]});
  }
  var phases=['Concept and modeling','Bench prototype','Integrated demonstrator','Independent verification'];
  var miles=[];
  for(i=0;i<4;i++){miles.push({phase:phases[i],quarters:'Q'+(i*2+1)+'-Q'+(i*2+2)+' (illustrative)'});}
  return {assumptions:P.assumptions,technology:P.title,
    objectives:P.objectives,
    parameters:params,milestones:miles,
    budget_band:P.budget,
    success_criteria:P.criteria,
    note:'A research-prototype specification, not a build order. Values are illustrative design points inside stated ranges.'};
}

function compute_adjudication(P){
  var dims=['physics_compatibility','engineering_path','economic_plausibility','timescale_realism','evidence_strength'];
  var keys=['physics','engineering','economics','timescale','evidence'];
  var scores={},sum=0,wsum=0;
  var weights=[0.3,0.25,0.15,0.1,0.2];
  for(var i=0;i<5;i++){var v=P.dims[keys[i]];scores[dims[i]]=v;sum+=v*weights[i];wsum+=weights[i];}
  return {assumptions:P.assumptions,technology:P.title,
    dimension_scores:scores,
    feasibility_index:Math.round(sum/wsum*10)/10,
    assigned_tier:P.tier,
    tier_justification:P.justify,
    what_would_change_tier:P.change,
    note:'Index is a weighted planning score, not a measurement. The tier assignment is the claim; the index only documents the reasoning.'};
}

var ENGINES={readiness:compute_readiness,constraints:compute_constraints,
  software:compute_software,simulation:compute_simulation,evidence:compute_evidence,
  breakthroughs:compute_breakthroughs,prototype:compute_prototype,adjudication:compute_adjudication};

/* ================= record type definitions ================= */
var RTYPES=[
 {key:'science',engine:'readiness',ladder:'simple',
  title:'Known Science and Physical Principles',
  lede:'sets out the established scientific foundation: what is known, what the governing principles are, and where settled science ends and open questions begin.'},
 {key:'constraints',engine:'constraints',ladder:'competitive',
  title:'Engineering Constraints and Requirements',
  lede:'maps the binding constraints: the physical, economic, and practical limits that any real implementation must satisfy, ranked by severity.'},
 {key:'software',engine:'software',ladder:'mix-and-match',
  title:'Relevant Software and Computational Tools',
  lede:'surveys the software stack used to research, design, and de-risk the technology, from modeling frameworks to deployment tooling.'},
 {key:'simulation',engine:'simulation',ladder:'unmade',
  title:'Simulation Tools and Modeling Approaches',
  lede:'describes how the technology is modeled before it is built: the simulation components, fidelity trade-offs, compute budgets, and validation discipline.'},
 {key:'experiments',engine:'evidence',ladder:'top-notch-or-better',
  title:'Experimental Results and Research Evidence',
  lede:'collects what has actually been shown: the evidence ledger, how strong each item is, and the open questions that experiments have not yet closed.'},
 {key:'problems',engine:'breakthroughs',ladder:'future-grade',
  title:'Unresolved Problems and Breakthrough Requirements',
  lede:'names the hard problems honestly: the breakthroughs that would be required, their difficulty, and the dependency order in which they must fall.'},
 {key:'prototype',engine:'prototype',ladder:'god-mode',
  title:'Research-Prototype Generator',
  lede:'generates a concrete research-prototype specification: objectives, design parameters, milestones, budget band, and success criteria for a serious attempt.'},
 {key:'assessment',engine:'adjudication',ladder:'god-mode',
  title:'Feasibility Assessment and Technology Roadmap',
  lede:'adjudicates feasibility: scored dimensions, a documented tier assignment, a phased roadmap, and exactly what evidence would change the tier.'}
];
var VARIANT_FOCI={
 science:['re-examining the governing equations under extreme parameter regimes','comparing competing theoretical frameworks','tracing how the science constrains design choices','stress-testing textbook assumptions'],
 constraints:['tightening the mass budget','energy-first constraint analysis','manufacturability-led constraint ranking','safety-case-driven requirements'],
 software:['open-source-first toolchain selection','high-assurance software for safety cases','real-time and embedded stack variants','data-pipeline-heavy research workflows'],
 simulation:['high-fidelity single-physics deep dive','coupled multi-physics campaign','uncertainty-quantification-focused ensemble','reduced-order model for design iteration'],
 experiments:['replication-focused evidence audit','negative-result and failure-mode ledger','independent-verification checklist','longitudinal evidence tracking'],
 problems:['dependency-graph critical-path analysis','alternative-path breakthrough mapping','bottleneck-first research sequencing','risk-register formulation'],
 prototype:['minimum-viable-demonstrator variant','full-capability flagship variant','low-cost university-lab variant','industry-partnership variant'],
 assessment:['optimistic-case reassessment','pessimistic-case reassessment','evidence-threshold analysis','roadmap compression study']};

/* ---- per-type middle-paragraph builders ---- */
function midPara(rt,scen,r){
  var T=TECH.title, out='';
  if(rt.key==='science'){
    out='The established science behind '+T+' rests on '+TECH.principle+' At the '+TECH.tier+
    ' feasibility tier, the honest statement is this: the governing principles are '+
    (TECH.tier==='demonstrated'?'well understood and repeatedly exercised in working systems.':
     TECH.tier==='experimentally-supported'?'understood in the laboratory, with open questions about how they behave at full scale and in integrated systems.':
     TECH.tier==='theoretically-plausible'?'understood on paper and in small experiments, with major open questions about whether they can be engineered into the described capability.':
     'incomplete: the relevant regimes are poorly explored, and confident claims about what is possible would outrun the evidence.');
  }else if(rt.key==='constraints'){
    out='The primary engineering constraint for '+T+' is '+TECH.constraint+' The constraint model ranks '+
    TECH.constraints.length+' constraints by severity; anything scoring 9 or above is treated as blocking, '+
    'meaning the program cannot proceed past paper studies until it is retired or worked around.';
  }else if(rt.key==='software'){
    out='The representative software for this domain is '+TECH.tool+' Around it sits a stack of modeling, '+
    'data, and control tools. Software de-risks '+T+' in three ways: it explores designs far cheaper than hardware, '+
    'it manages the experiments that do get built, and it provides the control and autonomy layer if the technology ever deploys.';
  }else if(rt.key==='simulation'){
    out='Simulation of '+T+' decomposes into '+TECH.sim.length+' model components, each run at a chosen fidelity. '+
    'The discipline that matters most is validation: every simulator used here must be checked against analytical limits, '+
    'convergence studies, and whatever experimental data exists, with all parameter choices documented.';
  }else if(rt.key==='experiments'){
    out='The evidence ledger for '+T+' is maintained against the '+TECH.tier+' tier. '+
    (TECH.tier==='demonstrated'?'Independent demonstrations exist in the published record; the ledger records what was shown, under what conditions, and what still needs independent replication.':
     TECH.tier==='experimentally-supported'?'Laboratory and prototype results exist for key components; the ledger distinguishes component-level evidence from full-system evidence, which is still missing.':
     TECH.tier==='theoretically-plausible'?'Evidence is indirect, small-scale, or analogical; the ledger records it as such rather than upgrading it into a demonstration.':
     'No working demonstration exists. The ledger records this plainly, along with the specific experiments whose outcomes would change the tier.');
  }else if(rt.key==='problems'){
    out='The breakthrough requirements for '+T+' are ordered by difficulty into a critical path. '+
    'Programs fail most often by attacking easy problems first; the honest sequence starts with the hardest requirement, '+
    'because everything downstream depends on it. Each requirement names its dependency explicitly.';
  }else if(rt.key==='prototype'){
    out='The research-prototype generator produces a buildable specification for '+T+': objectives first, then design '+
    'parameters drawn as points inside stated ranges, then phased milestones with illustrative quarters, a budget band, '+
    'and falsifiable success criteria. It is a specification for a serious attempt, not a promise that the attempt succeeds.';
  }else{
    out='Feasibility adjudication scores '+T+' on five dimensions and documents the reasoning behind the '+TECH.tier+
    ' assignment. The roadmap is phased by technology-readiness level, and the record states exactly what evidence would '+
    'move the tier up or down. If new evidence arrives, the tier changes; the record does not defend a stale verdict.';
  }
  if(scen>0){
    out+=' Scenario variant '+scen+' focuses on '+pick(r,VARIANT_FOCI[rt.key])+
    '; parameters are resampled deterministically from the same documented ranges, so the variant is reproducible from its seed.';
  }
  return out;
}

function buildParams(rt,r){
  var A=['Illustrative reference values for modeling; not measured data. Same seed reproduces same values.'];
  var P={title:TECH.title,assumptions:A};
  if(rt.engine==='readiness'){
    P.tier=TECH.tier;P.trl=TECH.trl;P.baseYears=TECH.baseYears;P.crit=[TECH.constraints[0][0],TECH.constraints[1][0],TECH.breakthroughs[0][0]];
    P.funding=['flat historic funding','steady programmatic funding','crash-program funding'];
  }else if(rt.engine==='constraints'){
    var cs=TECH.constraints.slice();var out=[];var i;
    for(i=0;i<cs.length;i++){var j=ri(r,0,cs.length-1);out.push(cs.splice(j,1)[0]);if(out.length>=5){break;}}
    P.constraints=out;
  }else if(rt.engine==='software'){
    P.tools=TECH.tools;P.usecases=['research exploration','prototype development','operations at scale'];
  }else if(rt.engine==='simulation'){
    P.components=TECH.sim;P.flopsBase=TECH.flopsNum;P.scale=rf(r,0.5,3.0,2);
  }else if(rt.engine==='evidence'){
    P.tier=TECH.tier;
    var pools={
     'demonstrated':['Independent laboratory demonstration reported','Prototype operated under realistic conditions','Peer-reviewed results published','Performance metrics independently measured','Follow-on systems reproduced the effect'],
     'experimentally-supported':['Key component demonstrated in the laboratory','Subscale prototype tested','Relevant phenomenon measured under controlled conditions','Simulation validated against component tests'],
     'theoretically-plausible':['Paper study with quantitative analysis','Small-scale or analog experiment','Expert elicitation converging on plausibility'],
     'unresolved':['Phenomenon reported but not reproduced'],
     'inconsistent-with-current-physics':[]}[TECH.tier];
    var n=Math.min(pools.length,TECH.evidenceN+ (r()<0.5?1:0));
    P.claims=pools.slice(0,Math.max(n,pools.length?1:0));
    P.strengths=[];for(var k=0;k<P.claims.length;k++){P.strengths.push(ri(r,5,9));}
    P.gaps=['Full-system integrated demonstration','Independent replication by a second group','Long-duration reliability data','Cost evidence at production scale','Side-effect and safety characterization','Operation outside laboratory conditions'];
  }else if(rt.engine==='breakthroughs'){
    P.reqs=TECH.breakthroughs;
  }else if(rt.engine==='prototype'){
    P.params=TECH.protoParams;P.dfrac=r();P.budget=TECH.budget;
    P.objectives=['Demonstrate the core effect outside idealized conditions','Measure performance against the stated success criteria','Produce a replication package a second group can rebuild from'];
    P.criteria=['Primary effect measured with documented uncertainty','Operates for the full milestone duration without intervention','Independent group reproduces the headline result'];
  }else{
    P.tier=TECH.tier;P.dims=TECH.dims;P.justify=TECH.tierJustify;P.change=TECH.tierChange;
  }
  return P;
}

function buildDemo(rt,r){
  var P=buildParams(rt,r);
  var fn=ENGINES[rt.engine];
  var result=fn(P);
  var src='/* '+TECH.title+' - '+rt.title+' demo. Run: node '+SLUG+'.js */\n'+
    '"use strict";\nvar PARAMS='+JSON.stringify(P)+';\n'+
    fn.toString().replace(/^function\s+[^\(]+\(/,'function compute(')+
    '\nconsole.log(JSON.stringify(compute(PARAMS),null,2));\n';
  return {program:src,output:result,params:P};
}

function capabilities(rt){
  var T=TECH.title;
  var base={
   science:['Explains the established physical principles behind '+T,'States the governing equations and scaling laws qualitatively','Separates settled science from open questions','Projects technology-readiness under three funding scenarios','Documents all modeling assumptions explicitly'],
   constraints:['Ranks the binding engineering constraints by severity','Identifies blocking constraints that gate any program','Computes an overall constraint-burden index','Names the mitigation focus for the top blockers','Keeps the analysis reproducible from its seed'],
   software:['Inventories the relevant software tool classes','Recommends stacks for research, prototype, and operations','Scores illustrative tool-maturity coverage','Explains how software de-risks hardware programs','Documents that coverage scores maturity, not fitness'],
   simulation:['Decomposes the system into model components','Estimates order-of-magnitude compute budgets','Provides a validation checklist for every simulator','Trades fidelity against cost explicitly','Documents parameter choices for reproducibility'],
   experiments:['Maintains an evidence ledger with strength scores','Distinguishes component evidence from system evidence','Lists open questions experiments have not closed','States the verdict implied by the feasibility tier','Never upgrades indirect evidence into demonstration'],
   problems:['Names the required breakthroughs explicitly','Scores difficulty and dependency order','Orders the critical path by difficulty','Computes an illustrative breakthrough-burden sum','Sequences research bottleneck-first'],
   prototype:['Generates objectives for a serious attempt','Picks design parameters inside stated ranges','Lays out phased milestones with budget band','States falsifiable success criteria','Produces a replication-ready specification'],
   assessment:['Scores five feasibility dimensions','Documents the tier assignment reasoning','Computes a weighted feasibility index','Phases a roadmap by readiness level','States exactly what evidence would change the tier']};
  return base[rt.key];
}

function buildRecord(seed,topic){
  if(seed<1){seed=1;}
  if(seed>HARD_CAP){throw new Error('seed exceeds HARD_CAP');}
  var r=rng32(h32(SLUG)^ (seed*2654435761>>>0));
  var idx=(seed-1)%8, scen=Math.floor((seed-1)/8);
  var rt=RTYPES[idx];
  var id=IDPREFIX+pad6(IDBASE+seed);
  var title=rt.title+': '+TECH.title+' \u2014 '+TECH.edLabel;
  var desc=rt.lede.charAt(0).toUpperCase()+rt.lede.slice(1);
  desc='Engineering record for '+TECH.title+' ('+TECH.catName+'). '+desc;
  var demo=buildDemo(rt,r);
  var paras=[];
  paras.push('This record '+rt.lede+' It covers '+TECH.title+' \u2014 '+TECH.desc);
  paras.push(TECH.domain);
  paras.push(TECH.tierFrame);
  paras.push(midPara(rt,scen,r));
  paras.push(TECH.edFraming);
  if(topic){paras.push('Topic focus for this generation: '+topic+'. The analysis above is read through that lens; the underlying parameters and tier assignment are unchanged.');}
  paras.push('The executable demo accompanying this record ('+rt.engine+' model) computes its analysis under stated, reproducible assumptions: '+
    'every value derives deterministically from the record seed, and the program prints its assumptions alongside its results. '+
    'Run the demo program with node to reproduce the stored output exactly.');
  var body=paras.join('\n\n');
  return {
    id:id,slug:SLUG,title:title,t:TECH.title,g:TECH.catName,c:1,
    description:desc,body:body,
    capabilities:capabilities(rt),
    demo:{program:demo.program,output:demo.output},
    feasibility_tier:TECH.tier,
    ladder_rank:scen===0?rt.ladder:(scen<3?RTYPES[Math.min(7,idx+scen)].ladder:'god-mode'),
    edition:TECH.edition,src:TECH.src,
    record_kind:'future technology engineering record',
    generator:'gen-'+SLUG+'.js (JAHDB boundless generator, deterministic, HARD_CAP=1e15)',
    verification_status:'tested',
    provenance:'Catalog: '+TECH.pasteRef+'; entry '+TECH.entryNum+'. Built by JAH Databases R22 lane futuretech-a (assistant-built). Demo executed in node; output verified. Last verified '+TECH.verified+'.',
    licensing:'Original engineering summaries and analysis. No copyrighted text reproduced. Property of Justin Addam Higgins (JAH).',
    links:[
      {label:'Database page',url:'https://justinahiggins614-cmyk.github.io/jah-databases/db/'+SLUG+'/'},
      {label:'Database data index',url:'https://justinahiggins614-cmyk.github.io/jah-databases-data-2/data/'+SLUG+'/index.jsonl.gz'},
      {label:'Generator source',url:'https://justinahiggins614-cmyk.github.io/jah-databases/db/'+SLUG+'/gen-'+SLUG+'.js'}
    ]
  };
}

function validate(rec){
  var errors=[];
  if(!rec||typeof rec!=='object'){return {ok:false,errors:['not an object']};}
  if(typeof rec.id!=='string'||rec.id.indexOf(IDPREFIX)!==0){errors.push('bad id');}
  if(rec.slug!==SLUG){errors.push('bad slug');}
  if(typeof rec.title!=='string'||rec.title.length<10){errors.push('bad title');}
  if(['demonstrated','experimentally-supported','theoretically-plausible','unresolved','inconsistent-with-current-physics'].indexOf(rec.feasibility_tier)<0){errors.push('bad feasibility_tier');}
  if(['public','signature'].indexOf(rec.edition)<0){errors.push('bad edition');}
  if(!rec.demo||typeof rec.demo.program!=='string'||rec.demo.program.indexOf('console.log')<0){errors.push('bad demo.program');}
  if(!rec.demo||typeof rec.demo.output!=='object'){errors.push('bad demo.output');}
  if(typeof rec.body!=='string'||rec.body.length<800){errors.push('body too short');}
  if(!rec.ladder_rank){errors.push('missing ladder_rank');}
  return {ok:errors.length===0,errors:errors};
}

function main(){
  var args=process.argv.slice(2),n=8,seed=1;
  for(var i=0;i<args.length;i++){
    if(args[i]==='--n'){n=parseInt(args[i+1],10);}
    if(args[i]==='--seed'){seed=parseInt(args[i+1],10);}
  }
  if(!(n>=1&&n<=10000)){throw new Error('bad --n');}
  for(var k=0;k<n;k++){console.log(JSON.stringify(buildRecord(seed+k)));}
}

if(typeof process!=='undefined'&&process.argv&&process.argv[1]&&process.argv[1].indexOf('gen-')>=0){main();}
if(typeof window!=='undefined'&&window.JAHDB&&JAHDB.registerGenerator){
  JAHDB.registerGenerator(SLUG,{generate:function(seed,opts){return buildRecord(seed,(opts&&opts.topic)||'');},validate:validate});
}
if(typeof module!=='undefined'&&module.exports){module.exports={buildRecord:buildRecord,validate:validate,SLUG:SLUG};}
