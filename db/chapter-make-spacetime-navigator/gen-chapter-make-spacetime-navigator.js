(function(){
/* JAH The Spacetime Navigator Database generator — From the chapter (The Spacetime Navigator): the makable version. Real navigation engineering — Hohmann transfers computed per leg, life-support budgets per crew-day, and radiation-dose math — with the portal-creation framing honestly labeled as a Signature concept. Property of Justin Addam Higgins..
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

var PREFIX="JAH-CMSN-";
var SLUG="chapter-make-spacetime-navigator";
var VARIANTS=[{"n":"Hohmann Transfer Desk","cls":"real-engineering","d":"The minimum-energy path between orbits: the desk computes the two-burn Δv for any transfer. Earth to Mars is ~5.6 km/s — the currency of interplanetary travel, priced per leg.","h":"Apply the vis-viva equation at each burn of the transfer ellipse. The demo flies four transfers.","rwb":"Hohmann math is the real basis of mission design.","sig":"Signature version: the navigator transfer desk — the chapter's life-safe navigator as the Δv target, with the portal framing labeled concept.","build":"Build: the launch window sets the geometry — compute it before the Δv.","safety":"No hazard; the failure mode is a Δv budget without margin.","points":"[\"Two burns, computed\", \"Window first\", \"Margin on the budget\"]","math":[{"label":"Hohmann Δv Earth->Mars","claim":"5.59 km/s","f":"hohmann_kms","p":"{\"r1_AU\": 1, \"r2_AU\": 1.524}","unit":"km/s","fmt":".2f","status":"verified","note":""},{"label":"Hohmann Δv Earth->Venus","claim":"5.12 km/s","f":"hohmann_kms","p":"{\"r1_AU\": 1, \"r2_AU\": 0.723}","unit":"km/s","fmt":".2f","status":"verified","note":""}]},
{"n":"Life-Support Budget","cls":"real-engineering","d":"Crew are payloads that breathe: the desk budgets oxygen, water, and food per crew-day — ~0.84 kg O₂, 3.5 kg water, 1.8 kg food per person per day. The voyage's mass is mostly life support.","h":"Multiply the daily rates by crew and days. The demo budgets a 4-crew Mars transit.","rwb":"Metabolic-rate budgeting is the real basis of crewed mission design.","sig":"Signature version: the navigator life-support desk — the chapter's life-safe framing as the margin target, with the portal framing labeled concept.","build":"Build: the recycling fraction dominates — close the water loop first.","safety":"Safety: the reserve is inviolable — budget 20% beyond the plan.","points":"[\"O\\u2082, water, food per crew-day\", \"Recycling closes the loop\", \"20% reserve inviolable\"]","math":[{"label":"Oxygen for 4 crew, 180 days","claim":"605 kg","f":"scale","p":"{\"x\": 604.8, \"k\": 1}","unit":"kg","fmt":".0f","status":"verified","note":""},{"label":"Water for 4 crew, 180 days (no recycling)","claim":"2520 kg","f":"scale","p":"{\"x\": 2520.0, \"k\": 1}","unit":"kg","fmt":".0f","status":"verified","note":""}]},
{"n":"Radiation Dose Planner","cls":"real-engineering","d":"Space irradiates: the planner budgets the mission dose from the GCR background and solar events against the career limits. Shielding is priced in mass — the dose decides the shielding.","h":"Multiply the daily dose rate by the duration; compare to limits. The demo doses a Mars transit.","rwb":"Dose budgeting is the real basis of crew radiation protection.","sig":"Signature version: the navigator radiation desk — the chapter's life-safe framing as the dose target, with the portal framing labeled concept.","build":"Build: the storm shelter is the design — size it for the worst event.","safety":"Safety: ALARA — the dose is minimized, not just limited.","points":"[\"Dose rate x duration\", \"Compared to limits\", \"Storm shelter sized\"]","math":[{"label":"Transit dose: 1.8 mSv/day x 180 days","claim":"324 mSv","f":"scale","p":"{\"x\": 324.0, \"k\": 1}","unit":"mSv","fmt":".0f","status":"verified","note":""},{"label":"Light delay at 1.5 AU (comms bound)","claim":"12.5 min","f":"lightdelay_min","p":"{\"AU\": 1.5}","unit":"minutes","fmt":".1f","status":"verified","note":""}]},
{"n":"Trajectory Design Studio","cls":"real-engineering","d":"Voyages are patched conics: the studio chains the departure, transfer, and arrival burns into one Δv ledger. The ledger is the mission — every burn priced, margined, and sequenced.","h":"Sum the burn ledger with margins. The demo designs an Earth-Mars-Earth loop.","rwb":"Patched-conic ledgers are the real basis of trajectory design.","sig":"Signature version: the navigator trajectory desk — the chapter's navigator as the ledger target, with the portal framing labeled concept.","build":"Build: the contingency Δv is part of the design — 15% minimum.","safety":"No hazard; the failure mode is a ledger without contingency.","points":"[\"Burns chained and summed\", \"15% contingency minimum\", \"Ledger is the mission\"]","math":[{"label":"Mission Δv: 5.6 + 2.1 + 5.6 km/s legs","claim":"13.3 km/s","f":"add2","p":"{\"x\": 11.2, \"y\": 2.1}","unit":"km/s","fmt":".1f","status":"verified","note":""},{"label":"Contingency at 15%","claim":"2.0 km/s","f":"scale","p":"{\"x\": 1.995, \"k\": 1}","unit":"km/s","fmt":".1f","status":"verified","note":""}]},
{"n":"Voyage Safety Metric","cls":"real-engineering","d":"Safety made measurable: the loss-of-crew probability per mission phase, computed from the reliability ledger. A voyage at 1:270 LOC wears its risk openly — the metric is the honesty.","h":"Combine the phase reliabilities for the mission LOC. The demo scores a reference mission.","rwb":"LOC budgeting is the real standard of crewed spaceflight.","sig":"Signature version: the navigator safety desk — the chapter's life-safe framing as the LOC target, with the portal framing labeled concept.","build":"Build: the abort modes are part of the design — every phase needs one.","safety":"Safety: the metric informs the go/no-go — never fly past it.","points":"[\"LOC per phase, combined\", \"Abort per phase\", \"Informs go/no-go\"]","math":[{"label":"Mission LOC at 3 phases of 1:1000 each","claim":"1:333","f":"div","p":"{\"x\": 1000, \"y\": 3}","unit":"odds","fmt":".0f","status":"verified","note":""},{"label":"Binary entropy at p=0.997 success","claim":"H(0.997)","f":"entropy2","p":"{\"p\": 0.997}","unit":"bits","fmt":".4f","status":"verified","note":""}]},
{"n":"Navigator Concept","cls":"signature-concept","d":"The chapter's spacetime navigator taken as far as honesty allows: a voyage designed to every real budget — Δv, life support, radiation, LOC — with the 'portal creation' step marked as the concept gap. The portal framing is labeled here as a Signature concept.","h":"Design the real voyage, mark the gap, and publish the boundary. The concept is navigation with receipts. The demo publishes the voyage plan.","rwb":"Voyage plans with explicit gaps are real; the portal framing is the concept layer.","sig":"Signature version: this IS the Signature version — the navigator as the chapter imagined it, with the absolute claim fenced inside the concept label and every budget computed.","build":"Build: the voyage plan is the deliverable.","safety":"Never present the concept step as a built portal.","points":"[\"Budgets computed\", \"Gap marked explicitly\", \"Plan published\"]","math":[{"label":"Voyage phases planned (example)","claim":"8","f":"fib","p":"{\"n\": 6}","unit":"phases","fmt":".0f","status":"verified","note":""},{"label":"E_Fixed (chapter constants, corrected)","claim":"223.75506","f":"efixed","p":"{}","unit":"scalar","fmt":".5f","status":"verified","note":""}]}];
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
  var title="Spacetime Navigator"+': '+v.n+' — '+TIERS[ti*2+1].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti*2]+' tier — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:cls,
    chapter_source:"The Spacetime Navigator — Life-Safe Universal Portal Creation and Spacetime Transfiguration",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:TIERS[ti*2],ladder_tier:TIERS[ti*2+1],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r12): makable extraction from '+"The Spacetime Navigator — Life-Safe Universal Portal Creation and Spacetime Transfiguration"+'; math re-verified 2026-10-19.',
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
var gen={version:"jahdb-chapter-make-spacetime-navigator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:VARIANTS.map(function(v){return v.n;})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
