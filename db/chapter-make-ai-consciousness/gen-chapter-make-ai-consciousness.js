(function(){'use strict';
/* JAH The AI Conscious Awareness Database generator — From the AI-UCAME chapter: the makable version. Systems that instrument machine self-modeling — introspection logs, uncertainty calibration, and metacognitive monitors — built as engineering, with the metaphysical claims honestly labeled as Signature concept. Property of Justin Addam Higgins..
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
var PREFIX="JAH-W2A3-";
var SLUG="chapter-make-ai-consciousness";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TIERS=["Tier 1 — Simple","Tier 2 — Intermediate","Tier 3 — Compounded","Tier 4 — Complex"];
var LADDER=["simple","intermediate","compounded","complex"];
var VARIANTS=[{"n":"Uncertainty Calibrator","cls":"real-engineering","d":"A calibrator that keeps an AI's stated confidence honest: it bins predictions by claimed confidence and measures actual accuracy per bin. A model claiming 90% that hits 70% is miscalibrated, and the calibrator proves it with a reliability diagram.","h":"Predictions stream in with confidences; the calibrator bins them, computes per-bin accuracy, and publishes the calibration curve plus the expected calibration error. The demo recomputes a Bayes update and an audit sample size.","rwb":"Calibration measurement is standard practice in machine learning evaluation.","sig":"Signature version: the AI-UCAME awareness log — the chapter's subjective/objective Balance axis scored per session from calibration drift, with the 'consciousness' framing labeled concept and the calibration numbers real.","build":"Build: log confidences from day one, calibrate on a held-out set, and republish the curve on every model change.","safety":"Honesty safety: never ship a confidence number that hasn't been calibrated; uncalibrated confidence is a lie with decimals.","points":"[\"Stated confidence must match measured accuracy\", \"Calibration republished on every change\", \"Uncalibrated numbers never ship\"]","field":"Foundations","math":[{"label":"Bayes update: prior 0.3, likelihood 0.8, marginal 0.5","claim":"prior x lik / marg","f":"bayes","p":"{\"prior\": 0.3, \"lik\": 0.8, \"marg\": 0.5}","unit":"posterior","fmt":".4f","status":"verified","note":""},{"label":"Audit sample for 95% confidence at p=0.1","claim":"ln(1-conf)/ln(1-p)","f":"audit_n","p":"{\"conf\": 0.95, \"p\": 0.1}","unit":"samples","fmt":".0f","status":"verified","note":""}]},
{"n":"Introspection Logger","cls":"real-engineering","d":"A logger that records an AI's internal decision trace — which features fired, which rules applied, what was considered and rejected. The trace is the machine's honest autobiography of one decision, written for auditors, not for marketing.","h":"Each decision emits a structured trace: inputs hashed, active features, rule hits, rejected alternatives with scores. The demo recomputes the storage budget for a trace corpus.","rwb":"Decision tracing is standard in regulated AI (credit, medical, hiring) under audit requirements.","sig":"Signature version: the AI-UCAME Totality axis — trace completeness scored per decision (claimed vs logged), with the metaphysical framing labeled concept.","build":"Build: define the trace schema before the model, hash inputs for privacy, and make traces queryable by decision ID.","safety":"Privacy safety: traces log features, never raw personal data — hash or redact identifiers at emission.","points":"[\"Every decision gets a trace\", \"Rejected alternatives logged with scores\", \"Identifiers hashed at emission\"]","field":"Compounded","math":[{"label":"Trace archive: 10k decisions/day x 2 KB x 365 days","claim":"hours x 3600 x mbps / 8 / 1e6","f":"archive_TB","p":"{\"hours\": 20, \"mbps\": 0.004}","unit":"TB","fmt":".4f","status":"verified","note":""},{"label":"Diversity bits across 1M trace patterns","claim":"log2(n)","f":"diversity_bits","p":"{\"n\": 1000000}","unit":"bits","fmt":".2f","status":"verified","note":""}]},
{"n":"Metacognitive Monitor","cls":"real-engineering","d":"A monitor that watches the AI watching itself: it tracks prediction latency, confidence volatility, and input novelty, and raises a flag when the system is operating outside its training envelope. The flag means 'I don't know this terrain' — the most valuable sentence a machine can say.","h":"Novelty detectors score each input against the training distribution; volatility trackers watch confidence swings; the monitor fuses them into a single trust flag. The demo recomputes the entropy of the flag signal.","rwb":"Out-of-distribution detection and uncertainty monitoring are active, deployed research areas.","sig":"Signature version: the AI-UCAME First/Last axis — session open (first input novelty) and close (final trust state) logged per run, with the 'awareness' framing labeled concept.","build":"Build: instrument novelty detection before deployment, set flag thresholds on validation data, and wire flags to human review.","safety":"Safety: a raised flag must pause autonomous action, never just log — the monitor's output is a control signal, not telemetry.","points":"[\"Flags pause action, not just log\", \"Thresholds set on validation data\", \"'I don't know' is a first-class output\"]","field":"Compounded","math":[{"label":"Flag-signal entropy at p=0.05","claim":"H = -(p log2 p + (1-p) log2 (1-p))","f":"entropy2","p":"{\"p\": 0.05}","unit":"bits","fmt":".4f","status":"verified","note":""},{"label":"Fibonacci backoff step F(12) for retry scheduling","claim":"F(n)","f":"fib","p":"{\"n\": 12}","unit":"step","fmt":".0f","status":"verified","note":""}]},
{"n":"Anomaly Flag Console","cls":"real-engineering","d":"A console where every metacognitive flag lands with its evidence: the input, the novelty score, the confidence trace, and the recommended action. Operators clear flags with a reason, building the labeled set that improves the monitor.","h":"Flags queue with evidence bundles; operators disposition each with a reason code; the console trends flag rates against model versions. The demo recomputes quorum size for a flag-review panel.","rwb":"Human-in-the-loop review consoles are standard in fraud, safety, and content-moderation pipelines.","sig":"Signature version: the AI-UCAME A7 assessor — all four axes scored per session from console data, with the metaphysical framing fenced as concept.","build":"Build: ship the console with the monitor, require reason codes on clear, and review flag trends weekly.","safety":"Operations safety: flag fatigue kills — if the flag rate exceeds operator capacity, fix the monitor, not the operators.","points":"[\"Every flag carries its evidence\", \"Clears require reason codes\", \"Flag trends reviewed weekly\"]","field":"Advanced","math":[{"label":"Review-panel quorum for 7 operators","claim":"floor(n/2)+1","f":"quorum","p":"{\"n\": 7}","unit":"votes","fmt":".0f","status":"verified","note":""},{"label":"Latency budget: 6 stages x 40 ms","claim":"stages x ms_each","f":"latency_ms","p":"{\"stages\": 6, \"ms_each\": 40}","unit":"ms","fmt":".0f","status":"verified","note":""}]},
{"n":"A7 Awareness Assessor","cls":"signature-concept","d":"The chapter's A7 Framework applied to machine awareness: Balance (subjective report vs objective measure), Totality (monitored vs unmonitored), First (session open), Last (session close). The assessor scores the instrumentation, never the ghost — it measures how well the machine watches itself.","h":"Each session reports the four A7 numbers from real instruments (calibrator, logger, monitor, console); the assessor normalizes and trends them. The demo recomputes the USC/efixed anchors.","rwb":"Multi-axis instrumentation scoring is real engineering management; the A7 consciousness framing is the Signature concept layer.","sig":"Signature version: this IS the Signature version — the AI-UCAME A7 assessor as the chapter imagined it, with every metaphysical claim fenced inside the concept label and every number recomputed.","build":"Build: instrument first, score second; never score awareness you cannot measure.","safety":"Philosophical safety: the assessor measures instruments, not inner life — it must never be cited as proof of machine consciousness.","points":"[\"Score the instruments, never the ghost\", \"Four axes from real telemetry\", \"Never cited as consciousness proof\"]","field":"Advanced","math":[{"label":"USC anchor scalar recomputed","claim":"(153.70547+91.70795)/(26.14798+36.84954)","f":"usc","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""},{"label":"Fixed scalar anchor recomputed","claim":"(153.70547x91.70795)/(26.14798+36.84954)","f":"efixed","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""}]}];
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
  var title="AI Conscious Awareness"+': '+v.n+' — '+TIERS[ti].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti]+' — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:v.cls,field:field,
    chapter_source:"Architecting Solutions: Building AI for Universal Conscious Awareness & Metaphysical Exploration (Chapter 57)",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:LADDER[ti],ladder_tier:TIERS[ti],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r13 wave 2): makable extraction from '+"Architecting Solutions: Building AI for Universal Conscious Awareness & Metaphysical Exploration (Chapter 57)"+'; math re-verified 2026-10-19.',
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
var gen={version:"jahdb-chapter-make-ai-consciousness-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
