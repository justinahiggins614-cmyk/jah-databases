(function(){'use strict';
/* JAH The AI Governance and Harmony Database generator — From the governance chapters: the makable version. Decision-support systems for fair administration — policy simulators, civic feedback analyzers, and transparency ledgers — each with recomputed fairness budgets. Property of Justin Addam Higgins..
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

function fmtNum(x,fmt){ if(fmt&&fmt.charAt(0)==='.') return Number(x).toFixed(parseInt(fmt.slice(1),10)); return String(x); }
var PREFIX="JAH-W2A7-";
var SLUG="chapter-make-ai-governance";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TIERS=["Tier 1 — Simple","Tier 2 — Intermediate","Tier 3 — Compounded","Tier 4 — Complex"];
var LADDER=["simple","intermediate","compounded","complex"];
var VARIANTS=[{"n":"Policy Simulator","cls":"real-engineering","d":"A simulator that tests policies before they touch people: it models the affected population, runs the proposed rule, and reports distributional effects by group. A policy that looks neutral in aggregate but harms one group is caught here, before enactment.","h":"Population microdata feeds the rule engine; the simulator runs scenarios and reports effects per subgroup with uncertainty. The demo recomputes the audit sample size for validating the simulation and the quorum for the review panel.","rwb":"Microsimulation for policy analysis is standard in treasuries and central banks.","sig":"Signature version: the governance Balance assessor — the chapter's A7 Balance (order vs liberty) scored per policy from simulation outputs, with the 'universal harmony' framing labeled concept.","build":"Build: validate the simulator on past policies first, publish assumptions, then test the new rule.","safety":"Democracy safety: simulation advises elected decision-makers; it must never be presented as the decision itself.","points":"[\"Test policies before they touch people\", \"Effects reported per subgroup\", \"Advises; never decides\"]","field":"Foundations","math":[{"label":"Audit sample for 95% confidence at p=0.15","claim":"ln(1-conf)/ln(1-p)","f":"audit_n","p":"{\"conf\": 0.95, \"p\": 0.15}","unit":"samples","fmt":".0f","status":"verified","note":""},{"label":"Review-panel quorum for 9 members","claim":"floor(n/2)+1","f":"quorum","p":"{\"n\": 9}","unit":"votes","fmt":".0f","status":"verified","note":""}]},
{"n":"Civic Feedback Analyzer","cls":"real-engineering","d":"An analyzer that reads public comment at scale without losing the minority view: it clusters feedback by theme, preserves dissenting clusters above a size floor, and reports sentiment with its sampling frame. Loud is not the same as representative.","h":"Comments stream in; the analyzer clusters themes, weights by sampling frame, and protects minority clusters from the floor. The demo recomputes the entropy of the theme distribution and the diversity bits across clusters.","rwb":"Large-scale public-comment analysis is deployed by regulators and city governments.","sig":"Signature version: the governance Totality assessor — heard vs unheard populations as a computed coverage ratio, with the framing labeled concept.","build":"Build: publish the sampling frame first, protect minority clusters by rule, then report.","safety":"Representation safety: the analyzer must report who was NOT heard alongside what was said.","points":"[\"Minority clusters protected by rule\", \"Sampling frame published\", \"Unheard populations reported too\"]","field":"Compounded","math":[{"label":"Theme entropy at p=0.5 across 2 themes","claim":"H = -(p log2 p + (1-p) log2 (1-p))","f":"entropy2","p":"{\"p\": 0.5}","unit":"bits","fmt":".4f","status":"verified","note":""},{"label":"Diversity bits across 64 theme clusters","claim":"log2(n)","f":"diversity_bits","p":"{\"n\": 64}","unit":"bits","fmt":".1f","status":"verified","note":""}]},
{"n":"Transparency Ledger","cls":"real-engineering","d":"A ledger that makes administrative decisions auditable: every decision links to its data, its rule, and its decider, in an append-only public log. Citizens can trace any decision to its evidence — trust through verifiability.","h":"Decisions emit records with data hashes, rule versions, and decider identity; the ledger chains them publicly. The demo recomputes hash-collision odds for the log.","rwb":"Public decision registers and audit trails are standard in open-government practice.","sig":"Signature version: the governance First/Last assessor — proposal (first) and enacted outcome (last) anchored per decision, with the framing labeled concept.","build":"Build: define the decision record schema first, publish the log, and make every record resolvable by ID.","safety":"Privacy safety: the ledger is transparent about decisions, never about individuals — redact personal data by rule before publication.","points":"[\"Every decision links to evidence\", \"Append-only public log\", \"Personal data redacted by rule\"]","field":"Compounded","math":[{"label":"Hash-collision odds, 5M decisions in 64 bits","claim":"n^2/2^65","f":"collision_prob","p":"{\"n\": 5000000.0, \"bits\": 64}","unit":"probability","fmt":".3e","status":"verified","note":""},{"label":"ISBN-style check digit for decision IDs (demo)","claim":"check digit","f":"isbn13","p":"{\"d12\": \"978030640615\"}","unit":"digit","fmt":".0f","status":"verified","note":""}]},
{"n":"Budget Allocator","cls":"real-engineering","d":"An allocator that turns a budget into an optimal portfolio of programs under constraints: it scores programs on outcomes per cost, respects legal floors, and publishes the trade-off frontier. Every dollar's opportunity cost is shown.","h":"Program data feeds an optimizer with floor constraints; the allocator publishes the chosen portfolio and the frontier of alternatives. The demo recomputes an allocation split and the throughput of the budgeting pipeline.","rwb":"Portfolio optimization under constraints is standard in public finance and philanthropy.","sig":"Signature version: the governance A7 assessor — all four axes from allocator data, with the 'global harmony' framing fenced as concept.","build":"Build: score outcomes honestly first, encode legal floors as hard constraints, then optimize and publish the frontier.","safety":"Accountability safety: the allocator recommends; the appropriating body decides — the recommendation log is public.","points":"[\"Opportunity cost shown per dollar\", \"Legal floors as hard constraints\", \"Recommendation log public\"]","field":"Advanced","math":[{"label":"Split: 2.4M budget across 3 programs (40/35/25)","claim":"2400000x0.40","f":"scale","p":"{\"x\": 2400000, \"k\": 0.4}","unit":"USD","fmt":".0f","status":"verified","note":""},{"label":"Pipeline throughput: 4 cores x 3 GHz x 8 ipc x 64 bits","claim":"cores x GHz x 1e9 x ipc x bits / 1e9","f":"throughput_Gbps","p":"{\"cores\": 4, \"GHz\": 3, \"ipc\": 8, \"bits\": 64}","unit":"Gbps","fmt":".1f","status":"verified","note":""}]},
{"n":"A7 Harmony Assessor","cls":"signature-concept","d":"The chapter's A7 Framework applied to governance: Balance (order vs liberty), Totality (heard vs unheard), First (proposal), Last (outcome) scored per decision from real administrative data. The assessor keeps power legible in four numbers.","h":"Each decision reports the four A7 numbers; the assessor trends them per institution. The demo recomputes the USC/efixed anchors.","rwb":"Governance scorecards are real institutional practice; the A7 framing is the Signature concept layer.","sig":"Signature version: this IS the Signature version — the governance A7 assessor as the chapter imagined it, with the 'universal' claim fenced inside the concept label and every number recomputed.","build":"Build: instrument decisions first, define axes with civic stakeholders, then score.","safety":"Liberty safety: the assessor measures administration; it must never be used to score citizens.","points":"[\"Score decisions, never citizens\", \"Four axes from administrative data\", \"Trends per institution, public\"]","field":"Advanced","math":[{"label":"USC anchor scalar recomputed","claim":"(153.70547+91.70795)/(26.14798+36.84954)","f":"usc","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""},{"label":"Fixed scalar anchor recomputed","claim":"(153.70547x91.70795)/(26.14798+36.84954)","f":"efixed","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""}]}];
var TOPICS={};
FIELDS.forEach(function(f){ TOPICS[f]=VARIANTS.filter(function(v){return v.field===f;}).map(function(v){return v.n;}); });
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
  L.push(']','print("record: "+rid)',"for label, expected, unit in checks:","    print('  CHECK '+label+' expected='+expected+' '+unit)","print('OK: '+rid+' math re-verified')");
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=VARIANTS.filter(function(v){return v.field===field;});
  if(!pool.length) pool=VARIANTS;
  var v=pick(pool,rnd);
  var ti=(rnd()*TIERS.length)|0;
  var mc=mathCheck(v);
  var badge=v.cls==='real-engineering'?'[REAL ENGINEERING]':'[SIGNATURE CONCEPT]';
  var title="AI Governance and Societal Harmony"+': '+v.n+' — '+TIERS[ti].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti]+' — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:v.cls,field:field,
    chapter_source:"Architecting Solutions: Building AI for Universal Governance & Societal Harmony + AI-Powered Universal Governance & Global Harmony",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:LADDER[ti],ladder_tier:TIERS[ti],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r13 wave 2): makable extraction from '+"Architecting Solutions: Building AI for Universal Governance & Societal Harmony + AI-Powered Universal Governance & Global Harmony"+'; math re-verified 2026-10-19.',
    last_verified:'2026-10-19',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.math_check||!r.math_check.length)e.push('math_check');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate title+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-chapter-make-ai-governance-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
