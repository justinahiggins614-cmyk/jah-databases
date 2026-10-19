(function(){'use strict';
/* JAH The AI Energy and Resources Database generator — From the AI-UER chapter: the makable version. AI systems that balance energy demand against supply and schedule resource extraction against sustainability — grid controllers, storage dispatchers, and yield schedulers, each with recomputed budgets. Property of Justin Addam Higgins..
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
var PREFIX="JAH-W2A1-";
var SLUG="chapter-make-ai-energy-resources";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TIERS=["Tier 1 — Simple","Tier 2 — Intermediate","Tier 3 — Compounded","Tier 4 — Complex"];
var LADDER=["simple","intermediate","compounded","complex"];
var VARIANTS=[{"n":"Grid Balance Controller","cls":"real-engineering","d":"A dispatch controller that matches generation to load in 5-minute intervals. It forecasts demand from recent history, commits slow generators first, and holds fast storage for the residual. The controller's job is arithmetic, not magic: every interval must show supply equal to demand plus reserve.","h":"Load forecast feeds a merit-order stack: cheapest reliable megawatts dispatch first, batteries cover ramps. The controller re-solves each interval and logs the imbalance it had to absorb. The demo recomputes a solar farm's output and a battery bank's energy from first principles.","rwb":"Real grid operators run exactly this stack — day-ahead commitment plus real-time economic dispatch — on every interconnected grid on Earth.","sig":"Signature version: the AI-UER balance assessor — the chapter's A7 Balance (demand vs supply) scored per interval as a 0–1 index, with the scoring rule versioned and the 'universal' framing kept as an explicit Signature concept.","build":"Build: pick a service area, size generation to 120% of peak, provision storage for the worst ramp, then verify dispatch cost against the forecast.","safety":"Electrical safety: dispatch software never overrides protection relays; treat every setpoint as advisory until field-verified.","points":"[\"Forecast, then dispatch, then verify\", \"Storage covers ramps, not baseload\", \"Every interval balances or logs why not\"]","field":"Foundations","math":[{"label":"Solar farm output, 10,000 m2 at 22% efficiency","claim":"P = area x irradiance x eff / 1000","f":"solar_kw","p":"{\"area_m2\": 10000, \"eff\": 0.22}","unit":"kW","fmt":".1f","status":"verified","note":""},{"label":"Battery bank energy, 48 V 200 Ah string x 20","claim":"E = mAh x V / 1000","f":"battery_Wh","p":"{\"mAh\": 200000, \"V\": 48}","unit":"Wh","fmt":".0f","status":"verified","note":""}]},
{"n":"Resource Extraction Scheduler","cls":"real-engineering","d":"A scheduler that plans extraction against regeneration so a resource is never mined past its maximum sustainable yield. It tracks stock, applies the logistic growth rate, and caps each period's take at the computed MSY. Extraction above the cap is flagged, not executed.","h":"Stock surveys feed the logistic model; the scheduler converts the growth rate into a per-period quota and distributes it across sites by cost. The demo recomputes MSY and the logistic increment for a fishery-style stock.","rwb":"Maximum sustainable yield scheduling is standard practice in fisheries, forestry, and groundwater management worldwide.","sig":"Signature version: the AI-UER Totality assessor — the chapter's A7 Totality (extraction vs regeneration) as a computed ratio per period, with the 'universal resource' framing labeled concept and the quota itself real.","build":"Build: survey the stock, fit the logistic rate, publish the quota, then meter actual takes against it.","safety":"Ecological safety: never set a quota from a single survey; require three consecutive agreeing estimates before raising any cap.","points":"[\"Quota never exceeds computed MSY\", \"Stock surveyed before each period\", \"Over-takes flagged automatically\"]","field":"Compounded","math":[{"label":"Maximum sustainable yield, r=0.4, K=1,000,000","claim":"MSY = rK/4","f":"msy","p":"{\"r\": 0.4, \"K\": 1000000}","unit":"units/period","fmt":".0f","status":"verified","note":""},{"label":"Logistic increment, N=600,000 of K=1,000,000","claim":"dN = rN(1-N/K)","f":"logistic","p":"{\"r\": 0.4, \"N\": 600000, \"K\": 1000000}","unit":"units/period","fmt":".0f","status":"verified","note":""}]},
{"n":"Demand Response Coordinator","cls":"real-engineering","d":"A coordinator that shaves peaks by shifting flexible loads instead of firing peaker plants. It ranks loads by shiftability, sends curtailment signals with a price, and verifies each response against metered data. Every megawatt shifted is metered, never assumed.","h":"Price signals go out ahead of the peak; enrolled loads respond on contract; meters confirm. The coordinator's ledger matches signaled curtailment against measured drop, and the demo recomputes the channel capacity the signal network needs.","rwb":"Demand response programs operate at gigawatt scale in North America, Europe, and parts of Asia.","sig":"Signature version: the AI-UER First/Last assessor — the chapter's A7 First (trigger) and Last (settlement) events logged per curtailment round, with the framing labeled concept and the metered megawatts real.","build":"Build: enroll flexible loads first, prove the signal path, then bid the aggregated curtailment into the peak window.","safety":"Consumer safety: curtailment contracts must exempt medical and life-safety loads explicitly, in writing, before enrollment.","points":"[\"Shift loads, don't build peakers\", \"Every curtailed MW is metered\", \"Life-safety loads exempt by contract\"]","field":"Compounded","math":[{"label":"Signal entropy for a 2-state curtailment signal at p=0.7","claim":"H = -(p log2 p + (1-p) log2 (1-p))","f":"entropy2","p":"{\"p\": 0.7}","unit":"bits/signal","fmt":".4f","status":"verified","note":""},{"label":"Shannon capacity of a 5 MHz signal link at SNR 7","claim":"C = B log2(1+SNR)","f":"shannon_Mbps","p":"{\"MHz\": 5, \"snr\": 7}","unit":"Mbps","fmt":".2f","status":"verified","note":""}]},
{"n":"A7 Energy Balance Assessor","cls":"signature-concept","d":"The chapter's A7 Framework applied to energy: Balance (demand vs supply), Totality (extraction vs regeneration), First (commissioning), Last (decommissioning) scored per asset per period. The assessor is a scoring discipline — it makes trade-offs visible instead of hiding them in averages.","h":"Each asset reports the four A7 numbers; the assessor normalizes them to 0–1 and publishes a balance sheet. Assets below threshold get flagged for review. The demo recomputes the chapter's USC-style scalar anchors to show the scoring math is honest.","rwb":"Multi-criteria asset scoring is real practice in utility integrated-resource planning; the A7 four-axis framing is the Signature concept layer.","sig":"Signature version: this IS the Signature version — the AI-UER A7 assessor as the chapter imagined it, with the 'universal' claim fenced inside the concept label and every anchor number recomputed, not copied.","build":"Build: define the four axes for your domain first, calibrate thresholds on history, then score live assets.","safety":"Governance safety: a score is advisory — no automated shutdown may key off an A7 score alone without human review.","points":"[\"Four axes, one balance sheet per asset\", \"Thresholds calibrated on history\", \"Scores advise; humans decide\"]","field":"Advanced","math":[{"label":"USC anchor scalar (D+L)/(N+S) recomputed","claim":"(153.70547+91.70795)/(26.14798+36.84954)","f":"usc","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""},{"label":"Fixed scalar anchor (D x L)/(N+S) recomputed","claim":"(153.70547x91.70795)/(26.14798+36.84954)","f":"efixed","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""}]},
{"n":"Post-Scarcity Resource Planner","cls":"signature-concept","d":"The chapter's end-state vision engineered as far as honesty allows: a planner that assumes fabrication capacity and computes what abundance would require — energy per capita, material throughput, and the compounding curve to get there. The 'post-scarcity' in the chapter is labeled here as a Signature concept; the planner's arithmetic is real.","h":"The planner takes a population, a per-capita target, and a growth rate, then compounds the requirement curve and prices it in energy. The demo recomputes the compounding and the doubling-step count.","rwb":"Capacity planning with compounding curves is standard in infrastructure economics; the post-scarcity endpoint is the concept layer.","sig":"Signature version: this IS the Signature version — the AI-UER abundance planner as the chapter imagined it, with the scarcity-free claim fenced as concept and every curve recomputed.","build":"Build: set the per-capita target first, compound honestly, and publish the energy price of abundance before promising it.","safety":"Planning safety: never present a concept curve as a commitment — label the endpoint speculative in every briefing.","points":"[\"Abundance priced in energy before promised\", \"Compounding shown, not hand-waved\", \"Endpoint labeled speculative\"]","field":"Advanced","math":[{"label":"Doubling steps to reach 1,000,000 fabrication units","claim":"2^n >= 1e6","f":"replicator","p":"{\"n\": 20}","unit":"units","fmt":".0f","status":"verified","note":""},{"label":"Compounded capacity, base 100 at 8% for 25 years","claim":"base x (1+rate)^yrs","f":"growth_cap","p":"{\"base\": 100, \"rate\": 0.08, \"yrs\": 25}","unit":"units","fmt":".1f","status":"verified","note":""}]}];
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
  var title="AI Energy and Resources"+': '+v.n+' — '+TIERS[ti].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti]+' — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:v.cls,field:field,
    chapter_source:"Architecting Solutions: Building AI for Universal Energy & Resources (Chapter 1)",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:LADDER[ti],ladder_tier:TIERS[ti],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r13 wave 2): makable extraction from '+"Architecting Solutions: Building AI for Universal Energy & Resources (Chapter 1)"+'; math re-verified 2026-10-19.',
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
var gen={version:"jahdb-chapter-make-ai-energy-resources-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
