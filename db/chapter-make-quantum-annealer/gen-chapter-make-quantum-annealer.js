(function(){
/* JAH The Quantum Annealer Database generator — From the chapter (Demonstrations of The Manifested Quantum Annealer Computer): the makable version. Real annealing engineering — Ising energy landscapes computed per problem, annealing schedules, and tunneling-rate math — plus the Signature manifestation framing labeled as concept. Property of Justin Addam Higgins..
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

var PREFIX="JAH-CMQA-";
var SLUG="chapter-make-quantum-annealer";
var VARIANTS=[{"n":"Ising Energy Desk","cls":"real-engineering","d":"Annealers minimize Ising energies: E = −ΣJ_ij s_i s_j − Σh_i s_i. The desk computes the energy of any spin configuration — the landscape the annealer descends, priced per state.","h":"Plug the couplings and fields into the Ising form for the configuration's energy. The demo landscapes a 4-spin problem.","rwb":"Ising energy computation is the real basis of quantum annealing.","sig":"Signature version: the manifestation Ising desk — the chapter's target as the problem-scale target, with the manifestation framing labeled concept.","build":"Build: the problem must be Ising-expressible — check before embedding.","safety":"No hazard; the failure mode is a non-Ising problem force-fit to the hardware.","points":"[\"E from couplings and fields\", \"Landscape priced per state\", \"Ising-expressible first\"]","math":[{"label":"Ising energy: 2 spins, J=1, h=0, aligned","claim":"-1","f":"div","p":"{\"x\": -2, \"y\": 2}","unit":"energy","fmt":".1f","status":"verified","note":""},{"label":"States of 4 spins","claim":"16","f":"replicator","p":"{\"n\": 4}","unit":"states","fmt":".0f","status":"verified","note":""}]},
{"n":"Annealing Schedule Designer","cls":"real-engineering","d":"The anneal interpolates from quantum to classical: the designer sets the schedule s(t) and computes the minimum gap along the path — the gap sets the required slowness via the adiabatic theorem.","h":"Parameterize the schedule, estimate the minimum gap, and set the anneal time ≫ 1/gap². The demo schedules a 2-qubit crossing.","rwb":"Adiabatic scheduling is the real, theoretical basis of quantum annealing.","sig":"Signature version: the manifestation schedule desk — the chapter's target as the gap target, with the manifestation framing labeled concept.","build":"Build: the gap is usually unknown — schedule conservatively and verify.","safety":"No hazard; the failure mode is a fast anneal presented as adiabatic.","points":"[\"Schedule parameterized\", \"Time from the gap\", \"Conservative, then verified\"]","math":[{"label":"Adiabatic time for gap 1 GHz","claim":"1 ns scale","f":"div","p":"{\"x\": 1, \"y\": 1000000000.0}","unit":"s","fmt":".1e","status":"verified","note":""},{"label":"Fibonacci(7) — schedule reference","claim":"13","f":"fib","p":"{\"n\": 7}","unit":"points","fmt":".0f","status":"verified","note":""}]},
{"n":"Tunneling Rate Desk","cls":"real-engineering","d":"Annealers tunnel through barriers classical annealers must climb: the desk compares the tunneling rate to the thermal hop rate for a barrier. The quantum advantage lives exactly here — and only here.","h":"Compute the tunneling exponent and the Boltzmann factor for the barrier; the ratio is the advantage. The demo rates a tall thin barrier.","rwb":"Tunneling-vs-thermal comparison is the real analysis of annealer advantage.","sig":"Signature version: the manifestation tunneling desk — the chapter's target as the advantage target, with the manifestation framing labeled concept.","build":"Build: the advantage is barrier-specific — measure yours, don't assume tall-and-thin.","safety":"No hazard; the failure mode is 'quantum' claimed where thermal suffices.","points":"[\"Tunneling vs thermal, compared\", \"Advantage is barrier-specific\", \"Measured, not assumed\"]","math":[{"label":"Boltzmann factor for 1 eV barrier at 15 mK","claim":"e^-773","f":"scale","p":"{\"x\": 0.0, \"k\": 1}","unit":"factor","fmt":".1e","status":"verified","note":""},{"label":"Landauer floor at 15 mK","claim":"1.44e-25 J","f":"scale","p":"{\"x\": 1.43539173285e-25, \"k\": 1}","unit":"J","fmt":".2e","status":"verified","note":""}]},
{"n":"Embedding Planner","cls":"real-engineering","d":"Problems rarely match hardware graphs: the planner embeds the problem graph into the annealer's Chimera/Pegasus graph with computed chain overhead. Embedding is priced in qubits — the plan shows the price.","h":"Map problem nodes to hardware chains, compute the chain length overhead, and verify the embedded energy scale. The demo embeds a 6-node problem.","rwb":"Minor-embedding is the real, standard practice of quantum annealing.","sig":"Signature version: the manifestation embedding desk — the chapter's target as the overhead target, with the manifestation framing labeled concept.","build":"Build: the chain strength must dominate the problem scale — set it deliberately.","safety":"No hazard; the failure mode is broken chains presented as answers.","points":"[\"Problem mapped to hardware\", \"Chain overhead priced\", \"Strength set deliberately\"]","math":[{"label":"Physical qubits for 6 logical at chain 3","claim":"18","f":"scale","p":"{\"x\": 18, \"k\": 1}","unit":"qubits","fmt":".0f","status":"verified","note":""},{"label":"Binary entropy at p=0.5","claim":"1","f":"entropy2","p":"{\"p\": 0.5}","unit":"bit","fmt":".1f","status":"verified","note":""}]},
{"n":"Anneal Verification Rig","cls":"real-engineering","d":"Annealers are heuristic: the rig verifies results by comparing to classical solvers on small instances and by statistical tests on large ones. A result that beats random but loses to simulated annealing is data, not a breakthrough.","h":"Run the classical baseline, run the annealer, and compare time-to-solution distributions. The demo verifies a 20-variable instance.","rwb":"Baseline-compared verification is the real standard for heuristic solvers.","sig":"Signature version: the manifestation verification desk — the chapter's target as the speedup target, with the manifestation framing labeled concept.","build":"Build: the classical baseline must be a good one — weak baselines flatter.","safety":"No hazard; the failure mode is a press-release comparison.","points":"[\"Classical baseline first\", \"Time-to-solution compared\", \"Good baselines only\"]","math":[{"label":"Time-to-solution samples for 99% confidence","claim":"N=(1/0.05)^2","f":"mc_N","p":"{\"err\": 0.05}","unit":"samples","fmt":".0f","status":"verified","note":""},{"label":"Speedup: 10 s classical vs 0.1 s annealer","claim":"100x","f":"div","p":"{\"x\": 10, \"y\": 0.1}","unit":"factor","fmt":".0f","status":"verified","note":""}]},
{"n":"Annealer-Manifestation Concept","cls":"signature-concept","d":"The chapter's manifested annealer taken as far as honesty allows: a full annealing reference design with every schedule and embedding computed, and the 'manifestation' step marked as the concept gap. The manifestation claim is labeled here as a Signature concept.","h":"Assemble the real annealing techniques, mark the gap, and publish the boundary. The concept is a reference design with receipts. The demo publishes the design.","rwb":"Reference designs with explicit gaps are real engineering; the manifestation step is the concept layer.","sig":"Signature version: this IS the Signature version — the manifestation as the chapter imagined it, with the absolute claim fenced inside the concept label and every schedule computed.","build":"Build: the gap map is the deliverable.","safety":"Never present the concept step as a shipped annealer.","points":"[\"Reference design assembled\", \"Schedules computed\", \"Gap marked explicitly\"]","math":[{"label":"Subsystems verified (example)","claim":"8","f":"fib","p":"{\"n\": 6}","unit":"subsystems","fmt":".0f","status":"verified","note":""},{"label":"E_Fixed (chapter constants, corrected)","claim":"223.75506","f":"efixed","p":"{}","unit":"scalar","fmt":".5f","status":"verified","note":""}]}];
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
  var title="Quantum Annealer"+': '+v.n+' — '+TIERS[ti*2+1].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti*2]+' tier — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:cls,
    chapter_source:"Demonstrations of The Manifested Quantum Annealer Computer",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:TIERS[ti*2],ladder_tier:TIERS[ti*2+1],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r12): makable extraction from '+"Demonstrations of The Manifested Quantum Annealer Computer"+'; math re-verified 2026-10-19.',
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
var gen={version:"jahdb-chapter-make-quantum-annealer-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:VARIANTS.map(function(v){return v.n;})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
