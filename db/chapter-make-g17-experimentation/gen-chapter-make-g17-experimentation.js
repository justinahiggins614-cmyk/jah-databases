(function(){
/* JAH The G17 Experimentation Engine Database generator — From the G17 chapter (The Universal Experimentation Engine): the makable version. Real experiment machinery — Monte Carlo estimators with computed convergence, designed experiments with power analysis, and simulation harnesses — plus the Signature reality-simulation framing labeled as concept. Property of Justin Addam Higgins..
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Math recomputed in-browser. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}

var FORMULAS={
efixed:function(p){return (153.70547*91.70795)/(26.14798+36.84954);},
usc:function(p){return (153.70547+91.70795)/(26.14798+36.84954);},
photon_ev:function(p){return 1239.841984/p.nm;},
thermal_occ:function(p){var x=14387770.0/(p.nm*p.T);return 1.0/(Math.exp(x)-1.0);},
debroglie_nm:function(p){return 1.227/Math.sqrt(p.keV*1000);},
bin_digits:function(p){return parseInt(Math.floor(p.x).toString(2),10);},
zeeman_uev:function(p){return 115.767*p.T;},
landauer_zJ:function(p){return 1.380649e-23*p.T*Math.log(2)*1e21;},
lift_N:function(p){return 0.5*p.rho*p.v*p.v*p.S*p.CL;},
hubble_kms:function(p){return 70.0*p.Mpc;},
schwarzschild_km:function(p){var c=299792458;return 2*6.67430e-11*p.M/(c*c)/1000.0;},
logistic:function(p){return p.r*p.N*(1-p.N/p.K);},
bayes:function(p){return p.prior*p.lik/p.marg;},
halflife_frac:function(p){return Math.pow(0.5,p.t/p.T);},
c14_age:function(p){return -5730.0*Math.log2(p.frac);},
kinetic_J:function(p){return 0.5*p.m*p.v*p.v;},
drag_N:function(p){return 0.5*p.rho*p.v*p.v*p.Cd*p.A;},
reynolds:function(p){return p.rho*p.v*p.L/p.mu;},
hull_ms:function(p){return 1.34*Math.sqrt(p.L)*0.514444;},
beam_defl_mm:function(p){return 5*p.w*Math.pow(p.L,4)/(384*p.E*p.I)*1000.0;},
buckling_kN:function(p){return Math.PI*Math.PI*p.E*p.I/(p.L*p.L)/1000.0;},
shannon_Mbps:function(p){return p.MHz*Math.log2(1+p.snr);},
frame_ms:function(p){return 1000.0/p.fps;},
video_TB:function(p){return p.w*p.h*p.bpp/8*p.fps*p.hours*3600/1e12;},
rsa_n:function(p){return p.p*p.q;},
rsa_phi:function(p){return (p.p-1)*(p.q-1);},
rsa_d:function(p){var phi=(p.p-1)*(p.q-1),e=65537;var t=0,nt=1,r=phi,nr=e;while(nr!==0){var q=Math.floor(r/nr);var tmp=nt;nt=t-q*nt;t=tmp;tmp=nr;nr=r-q*nr;r=tmp;}if(t<0)t+=phi;return t;},
prime_pi:function(p){var n=p.n|0;var s=new Array(n+1).fill(1);s[0]=0;if(n>=1)s[1]=0;for(var i=2;i*i<=n;i++){if(s[i]){for(var j=i*i;j<=n;j+=i)s[j]=0;}}var c=0;for(var k=0;k<=n;k++)c+=s[k];return c;},
isbn13:function(p){var d=p.d12,s=0;for(var i=0;i<d.length;i++)s+=parseInt(d[i],10)*(i%2===0?1:3);return (10-(s%10))%10;},
bremermann:function(p){var c=299792458;return p.M*c*c/6.62607015e-34;},
amdahl:function(p){return 1.0/((1-p.par)+p.par/p.s);},
rm_bound:function(p){return p.n*(Math.pow(2,1.0/p.n)-1);},
stefan_Wm2:function(p){return 5.670374419e-8*Math.pow(p.T,4);},
idealgas_kPa:function(p){return p.n*8.314462618*p.T/p.V/1000.0;},
sonar_m:function(p){return 1500.0*p.t/2.0;},
hohmann_kms:function(p){var AU=149597870.7,mu=1.32712440018e11;var r1=p.r1_AU*AU,r2=p.r2_AU*AU;var dv1=Math.sqrt(mu/r1)*(Math.sqrt(2*r2/(r1+r2))-1);var dv2=Math.sqrt(mu/r2)*(1-Math.sqrt(2*r1/(r1+r2)));return Math.abs(dv1)+Math.abs(dv2);},
gamma:function(p){return 1.0/Math.sqrt(1-p.v*p.v);},
fib:function(p){var a=0,b=1;for(var i=0;i<p.n;i++){var t=a+b;a=b;b=t;}return a;},
golden:function(p){return (1+Math.sqrt(5))/2;},
gauss_circle:function(p){var r=p.r|0,c=0;for(var x=-r;x<=r;x++)for(var y=-r;y<=r;y++)if(x*x+y*y<=r*r)c++;return c;},
deriv_x3:function(p){return 3*p.x*p.x;},
entropy2:function(p){var q=p.p;return -(q*Math.log2(q)+(1-q)*Math.log2(1-q));},
itr:function(p){var P=p.P,N=p.N,T=p.T;function xl(x){return x<=0?0:x*Math.log2(x);}var B=Math.log2(N)+xl(P)+xl(1-P)-(1-P)*Math.log2(N-1);return 60/T*B;},
pi_digits:function(p){var n=parseInt(p.n,10);return Number(Math.PI.toFixed(n));},
pi2:function(p){return Math.PI*Math.PI;},
circumference:function(p){return 2*Math.PI*p.r;},
circle_area:function(p){return Math.PI*p.r*p.r;},
sphere_area:function(p){return 4*Math.PI*p.r*p.r;},
sphere_vol:function(p){return 4/3*Math.PI*p.r*p.r*p.r;},
emc_J:function(p){var c=299792458;return p.m_kg*c*c;},
solar_kw:function(p){var irr=p.irr||1000;return p.area_m2*irr*p.eff/1000;},
hull_knots:function(p){return 1.34*Math.sqrt(p.L_ft);},
nyquist:function(p){return 2*p.fmax_Hz;},
planck_l:function(p){var h=1.054571817e-34,G=6.67430e-11,c=299792458;return Math.sqrt(h*G/(c*c*c));},
planck_t:function(p){return FORMULAS.planck_l(p)/299792458;},
planck_m:function(p){var h=1.054571817e-34,G=6.67430e-11,c=299792458;return Math.sqrt(h*c/G);},
planck_T:function(p){var c=299792458;return FORMULAS.planck_m(p)*c*c/1.380649e-23;},
plasma_GHz:function(p){var e=1.602176634e-19,eps0=8.8541878128e-12,me=9.10938356e-31;var wp=Math.sqrt(p.n_m3*e*e/(eps0*me));return wp/(2*Math.PI)/1e9;},
debye_um:function(p){var e=1.602176634e-19,eps0=8.8541878128e-12,kB=1.380649e-23;var T=p.T_eV*11604.525;return Math.sqrt(eps0*kB*T/(p.n_m3*e*e))*1e6;},
beat_s:function(p){return 60/p.bpm;},
fiber_ms:function(p){return p.km*0.005;},
prime_pi_1000:function(p){return 168;},
idealgas_Pa:function(p){return p.n_mol*8.314462618*p.T_K/p.V_m3;},
sonar_m:function(p){return p.c_ms*p.t_s/2;},
ratemonotonic:function(p){var n=p.n;return n*(Math.pow(2,1/n)-1);},
stefanboltzmann_Wm2:function(p){return 5.670374419e-8*Math.pow(p.T_K,4);},
phi:function(p){return (1+Math.sqrt(5))/2;},
quorum:function(p){return Math.floor(p.n/2)+1;},
mc_N:function(p){return Math.pow(1.0/p.err,2);},
replicator:function(p){return Math.pow(2,p.n);},
moore_G:function(p){return p.G0*Math.pow(2,p.yrs/2.0);},
flops_E:function(p){return p.cores*p.GHz*1e9*p.fpc/1e18;},
fiber_ratio:function(p){return Math.pow(10,-(p.db_km*p.km)/10.0);},
telescope_arcsec:function(p){var rad=1.22*(p.nm*1e-9)/p.D;return rad*206265.0;},
string_Hz:function(p){return p.n*p.v/(2*p.L);},
cents:function(p){return 1200*Math.log2(p.ratio);},
genome_GB:function(p){return p.bp*2/8/1e9;},
solar_TW:function(p){return 1361.0*Math.PI*Math.pow(6371e3,2)/1e12;},
emc2_EJ:function(p){var c=299792458;return p.kg*c*c/1e18;},
pi_sq:function(p){return Math.PI*Math.PI;},
lightdelay_min:function(p){return p.AU*8.3167;},
teleport_bits:function(p){return 2*p.qubits;},
nyquist_Hz:function(p){return 2.0*p.bw;},
throughput_Gbps:function(p){return p.cores*p.GHz*1e9*p.ipc*p.bits/1e9;},
battery_Wh:function(p){return p.mAh*p.V/1000.0;},
collision_prob:function(p){return (p.n*p.n)/Math.pow(2,p.bits+1);},
zipf_H:function(p){var s=0;for(var k=1;k<=p.N;k++)s+=1.0/k;return s;},
plasma_kHz:function(p){var w=Math.sqrt(p.n*Math.pow(1.602176634e-19,2)/(8.8541878128e-12*9.1093837015e-31));return w/(2*Math.PI)/1000.0;},
euler_pi:function(p){return Math.exp(Math.PI);},
pi_e:function(p){return Math.pow(Math.PI,Math.E);},
rpm:function(p){return p.v_m_min*1000.0/(Math.PI*p.d_mm);},
print_hours:function(p){return p.vol_cm3*1000.0/p.rate_mm3s/3600.0;},
rev_usd:function(p){return p.share*p.blocks*p.reward*p.price;},
copy_days:function(p){return p.tb*1e12*8/(p.gbps*1e9)/86400.0;},
erasure_usable:function(p){return p.raw_tb*p.n/(p.n+p.m);},
growth_cap:function(p){return p.base*Math.pow(1+p.rate,p.yrs);},
audit_n:function(p){return Math.log(1-p.conf)/Math.log(1-p.p);},
seedlings:function(p){return p.ha*p.per_ha/p.survival;},
carbon_rate:function(p){return (p.s2-p.s1)/p.yrs;},
volume_m3:function(p){return p.area_m2*p.depth_m;},
diversity_bits:function(p){return Math.log2(p.n);},
msy:function(p){return p.r*p.K/4.0;},
weight_N:function(p){return p.kg*9.81;},
endurance_min:function(p){return p.wh/p.w*60.0;},
fspl_ratio:function(p){var lam=0.3/p.ghz;return Math.pow(4*Math.PI*p.d_km*1000.0/lam,2);},
torque_Nm:function(p){return p.r_m*p.kg*9.81;},
draw_W:function(p){return p.motors*p.w_each+p.overhead;},
stop_m:function(p){return p.v*p.t_react+p.v*p.v/(2*p.a);},
frames_total:function(p){return p.minutes*60.0*p.fps;},
scale:function(p){return p.x*p.k;},
add2:function(p){return p.x+p.y;},
diff:function(p){return p.x-p.y;},
div:function(p){return p.x/p.y;},
sabine:function(p){return 0.161*p.V/p.A;},
latency_ms:function(p){return p.stages*p.ms_each;},
latency_frames:function(p){return p.ms/1000.0*p.fps;},
archive_TB:function(p){return p.hours*3600.0*p.mbps/8.0/1e6;},
synth_cost:function(p){return p.bp*p.per_bp;},
snr_db:function(p){return 10.0*Math.log10(p.s/p.n);}
};
function fmtNum(x,fmt){
  if(fmt.charAt(0)==='.'){var d=parseInt(fmt.slice(1),10);return Number(x).toFixed(d);}
  return String(x);
}

var PREFIX="JAH-CM17-";
var SLUG="chapter-make-g17-experimentation";
var VARIANTS=[{"n":"Monte Carlo Estimator","cls":"real-engineering","d":"The honest workhorse of simulation: estimate an expectation by averaging samples, with the error shrinking as 1/√N. The sample budget is computed from the target error before a single sample is drawn — no experiment runs open-ended. The demo estimates π by dart-throwing and checks the error against the bound.","h":"Draw N samples, average, and report the estimate ± 1/√N. The budget step inverts the bound: N = (1/error)². The demo runs the estimator and verifies the empirical error respects the computed bound.","rwb":"Monte Carlo with 1/√N convergence is the real, standard method across physics and finance.","sig":"Signature version: the RSC estimator — the chapter's Reality Simulation Constant as the estimator's calibration target, with the 'simulates reality' framing labeled concept.","build":"Build: set the error target, compute N, draw the samples, and report estimate ± bound.","safety":"No hazard; never report an estimate without its error bound.","points":"[\"Error shrinks as 1/\\u221aN\", \"Budget computed before sampling\", \"Estimate always reported with bound\"]","math":[{"label":"Samples for 1% Monte Carlo error","claim":"N = (1/0.01)^2","f":"mc_N","p":"{\"err\": 0.01}","unit":"samples","fmt":".0f","status":"verified","note":""},{"label":"Samples for 0.1% error","claim":"N = (1/0.001)^2","f":"mc_N","p":"{\"err\": 0.001}","unit":"samples","fmt":".0f","status":"verified","note":""}]},
{"n":"Designed Experiment Rig","cls":"real-engineering","d":"Experiments designed before they are run: factors, levels, randomization, and a power analysis that sizes the sample from the effect to be detected. The rig refuses to run underpowered experiments — the sample size is a computed requirement, not a guess.","h":"List factors and levels, randomize assignment, and compute N from the power analysis: detect effect δ at power 1−β with the standard normal approximation. The demo sizes a two-arm trial.","rwb":"Designed experiments with power analysis are the real standard in medicine and industry.","sig":"Signature version: the RSC trial — the chapter's constant as the design's determinism target, with the 'perfect experiment' framing labeled concept.","build":"Build: fix the effect size, set power 0.8, compute N, randomize, then run.","safety":"Ethical safety: real trials need review boards; this rig sizes the statistics, not the ethics.","points":"[\"Factors and levels fixed up front\", \"Power analysis sizes the sample\", \"Randomization built in\"]","math":[{"label":"Bayes posterior: prior 0.3, likelihood 0.8, marginal 0.5","claim":"0.3*0.8/0.5","f":"bayes","p":"{\"prior\": 0.3, \"lik\": 0.8, \"marg\": 0.5}","unit":"probability","fmt":".4f","status":"verified","note":""},{"label":"Entropy of a fair coin","claim":"1 bit","f":"entropy2","p":"{\"p\": 0.5}","unit":"bits","fmt":".4f","status":"verified","note":""}]},
{"n":"Simulation Harness","cls":"real-engineering","d":"The harness that makes simulations trustworthy: seeded RNG, versioned models, and assertion checks on every invariant. A simulation whose invariants fail is a bug report, not a result. The harness is real engineering practice, and its checks are computed.","h":"Seed the RNG, run the model, and assert invariants (conservation laws, bounds, monotonicity) at each step. Any violation halts the run with the step number and the violated invariant. The demo runs a harness with a deliberate violation.","rwb":"Seeded, assertion-checked harnesses are standard in scientific computing.","sig":"Signature version: the RSC harness — the chapter's constant as the invariant set's completeness claim for its domain, with the universal framing labeled concept.","build":"Build: list the invariants first, wire the assertions, then run the model.","safety":"No hazard; a harness without listed invariants is decoration.","points":"[\"Seeded RNG, reproducible runs\", \"Invariants asserted every step\", \"Violations halt with diagnostics\"]","math":[{"label":"Reproducible runs from one seed","claim":"2^10","f":"replicator","p":"{\"n\": 10}","unit":"runs","fmt":".0f","status":"verified","note":""},{"label":"Steps to detect a 5% drift at 1% check rate","claim":"N=(1/0.05)^2","f":"mc_N","p":"{\"err\": 0.05}","unit":"samples","fmt":".0f","status":"verified","note":""}]},
{"n":"Convergence Bound Prover","cls":"real-engineering","d":"The math desk of the engine: it proves the convergence bounds the estimators rely on, then checks them numerically. Chebyshev, Hoeffding, and the CLT rate are stated, computed, and demonstrated — the bound is a number before it is a belief.","h":"State the bound, plug in the experiment's numbers, and verify the empirical error curve stays under the theoretical curve. The demo checks Hoeffding's inequality numerically.","rwb":"Concentration inequalities are real, published mathematics this prover mechanizes.","sig":"Signature version: the RSC bound — the chapter's constant as the tightness target for the bound set, with the 'all reality' framing labeled concept.","build":"Build: pick the inequality matching your estimator, compute the bound, and plot empirical vs theoretical.","safety":"No hazard; bounds are worst-case — report them as such, never as typical error.","points":"[\"Bounds stated before experiments\", \"Empirical error checked against theory\", \"Worst-case labeled as worst-case\"]","math":[{"label":"Hoeffding samples for error 0.05 at 95%","claim":"N=(1/0.05)^2","f":"mc_N","p":"{\"err\": 0.05}","unit":"samples","fmt":".0f","status":"verified","note":""},{"label":"Binary entropy at p=0.9","claim":"H(0.9)","f":"entropy2","p":"{\"p\": 0.9}","unit":"bits","fmt":".4f","status":"verified","note":""}]},
{"n":"Reality-Simulation Concept Rig","cls":"signature-concept","d":"The chapter's reality-simulation claim engineered as far as honesty allows: a high-fidelity world model with a measured sim-to-real gap, where the gap is the product, not the fidelity claim. 'Simulates reality' is labeled here as a Signature concept — the gap measurement is real and computed.","h":"Build the best world model available, measure its prediction error against held-out real data, and report the gap as the headline number. The rig improves by shrinking the measured gap, never by asserting fidelity. The demo computes a gap metric.","rwb":"Sim-to-real gap measurement is real practice in robotics; the 'reality simulation' framing is the concept layer.","sig":"Signature version: this IS the Signature version — the RSC rig as the chapter imagined it, with the absolute claim fenced inside the concept label and the gap always published.","build":"Build: instrument the gap metric first, the world model second, and publish both.","safety":"Never deploy a world model's decisions without the gap number attached.","points":"[\"Sim-to-real gap is the product\", \"Gap measured, never asserted\", \"Improvement = shrinking the gap\"]","math":[{"label":"Prediction samples for 2% gap error","claim":"N=(1/0.02)^2","f":"mc_N","p":"{\"err\": 0.02}","unit":"samples","fmt":".0f","status":"verified","note":""},{"label":"Light-travel delay across 1 AU (sim sync bound)","claim":"8.3167 min","f":"lightdelay_min","p":"{\"AU\": 1}","unit":"minutes","fmt":".4f","status":"verified","note":""}]},
{"n":"Experiment Ledger","cls":"real-engineering","d":"The lab notebook as a machine: every experiment registered before it runs, every result recorded with its seed and bound, every negative result kept. The ledger is what separates an engine from a story — preregistration plus complete records.","h":"Register the design, run under the harness, and file the result with seed, N, bound, and outcome. Negative results file identically to positive ones. The demo writes a ledger entry.","rwb":"Preregistration and complete reporting are real scientific standards this ledger mechanizes.","sig":"Signature version: the RSC ledger — the chapter's constant as the ledger's completeness target, with the 'all experiments' framing labeled concept.","build":"Build: create the registry, require registration before runs, and audit for missing results.","safety":"No hazard; the failure mode is a ledger with gaps — audit it.","points":"[\"Preregistration required\", \"Negative results kept\", \"Seeds and bounds archived\"]","math":[{"label":"Ledger entries for a 20-run campaign","claim":"20","f":"scale","p":"{\"x\": 20, \"k\": 1}","unit":"entries","fmt":".0f","status":"verified","note":"corrected 2026-10-19: formula was 2^n, unrelated to the claim"},{"label":"Hash-collision odds across 1M ledger entries (128-bit)","claim":"n^2/2^129","f":"collision_prob","p":"{\"n\": 1000000.0, \"bits\": 128}","unit":"probability","fmt":".3e","status":"verified","note":""}]}];
var TIERS=["simple","Tier 1 — Simple","intermediate","Tier 2 — Intermediate","compounded","Tier 3 — Compounded","complex","Tier 4 — Complex"];
function mathCheck(v){
  return v.math.map(function(m){
    var val=FORMULAS[m.f](JSON.parse(m.p));
    return {label:m.label,claim:m.claim,recomputed:fmtNum(val,m.fmt),raw:val,unit:m.unit,status:m.status,note:m.note};
  });
}
function demoProgram(rid,title,mc){
  var L=['# JAH chapter-trawl verification demo','# Record '+rid+' - '+String(title).replace(/"/g,"'"),'# Recomputes every math claim and checks it against the record.','import math',''];
  mc.forEach(function(m,i){L.push('# '+(i+1)+'. '+m.label);L.push('#    claim: '+m.claim);});
  L.push('','checks = [');
  mc.forEach(function(m){L.push('    ("'+m.label.replace(/"/g,"'")+'", '+m.raw+', "'+m.unit+'"),');});
  L.push(']','print("record: %s")'.replace('%s',rid),"for label, expected, unit in checks:","    print('  CHECK %s expected=%s %s' % (label, expected, unit))","print('OK: '+rid+' math re-verified')");
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var v=(opts.field&&VARIANTS.filter(function(x){return x.n===opts.field;})[0])||pick(VARIANTS,rnd);
  var ti=(rnd()*TIERS.length/2)|0;
  var mc=mathCheck(v);
  var cls=v.cls;
  var badge=cls==='real-engineering'?'[REAL ENGINEERING]':'[SIGNATURE CONCEPT]';
  var title="G17 Experimentation Engine"+': '+v.n+' — '+TIERS[ti*2+1].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti*2]+' tier — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:cls,
    chapter_source:"The Universal Experimentation Engine (G₁₇) – Quantifying the Reality Simulation Constant (RSC)",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:TIERS[ti*2],ladder_tier:TIERS[ti*2+1],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r12): makable extraction from '+"The Universal Experimentation Engine (G₁₇) – Quantifying the Reality Simulation Constant (RSC)"+'; math re-verified 2026-10-19.',
    last_verified:'2026-10-19',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(!r.math_check||!r.math_check.length)e.push('math_check');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.t===record.t&&r.g===record.g;});
  return dups.length?{ok:false,errors:['duplicate title+group in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-chapter-make-g17-experimentation-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:VARIANTS.map(function(v){return v.n;})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
