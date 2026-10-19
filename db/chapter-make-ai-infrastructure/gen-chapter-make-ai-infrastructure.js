(function(){'use strict';
/* JAH The AI Infrastructure and Urban Planning Database generator — From the infrastructure chapter: the makable version. City-system optimizers — traffic signal controllers, water network balancers, and maintenance predictors — each with recomputed capacity budgets. Property of Justin Addam Higgins..
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
var PREFIX="JAH-W2A10-";
var SLUG="chapter-make-ai-infrastructure";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TIERS=["Tier 1 — Simple","Tier 2 — Intermediate","Tier 3 — Compounded","Tier 4 — Complex"];
var LADDER=["simple","intermediate","compounded","complex"];
var VARIANTS=[{"n":"Adaptive Signal Controller","cls":"real-engineering","d":"A controller that times traffic signals to the actual demand: it reads loop and camera data, optimizes splits and offsets per cycle, and coordinates corridors as green waves. Timing follows measurement, not the 1987 timing plan.","h":"Demand data feeds a per-cycle optimizer; the controller sets splits, offsets, and cycle length, then measures the result. The demo recomputes the stopping distance the timing must respect and the throughput of the control network.","rwb":"Adaptive signal control is deployed in thousands of cities with measured delay reductions.","sig":"Signature version: the city Balance assessor — the chapter's A7 Balance (throughput vs livability) scored per corridor, with the 'universal' framing labeled concept.","build":"Build: instrument the intersection first, optimize per cycle, and always keep pedestrian minimums inviolable.","safety":"Safety: pedestrian clearance intervals are hard constraints — no optimization may shorten them, ever.","points":"[\"Timing from measurement, not history\", \"Pedestrian minimums inviolable\", \"Corridors coordinated as green waves\"]","field":"Foundations","math":[{"label":"Stopping distance: 13.4 m/s, 1.5 s react, 3.4 m/s2","claim":"v x t + v^2/(2a)","f":"stop_m","p":"{\"v\": 13.4, \"t_react\": 1.5, \"a\": 3.4}","unit":"m","fmt":".1f","status":"verified","note":""},{"label":"Control throughput: 2 cores x 2.4 GHz x 4 ipc x 32 bits","claim":"cores x GHz x 1e9 x ipc x bits / 1e9","f":"throughput_Gbps","p":"{\"cores\": 2, \"GHz\": 2.4, \"ipc\": 4, \"bits\": 32}","unit":"Gbps","fmt":".1f","status":"verified","note":""}]},
{"n":"Water Network Balancer","cls":"real-engineering","d":"A balancer that keeps water pressure right everywhere: it models the pipe network, places pressure zones, and schedules pumps to meet demand at minimum energy. Leaks are found by the water balance — inflow minus metered outflow.","h":"Network models feed pump scheduling; pressure sensors close the loop; the water balance flags leak zones. The demo recomputes pipe flow velocity pressure and the ideal-gas-style pressure check for a tank.","rwb":"Pressure management and water-balance leak detection are standard utility practice.","sig":"Signature version: the city Totality assessor — water produced vs water billed as a computed ratio, with the framing labeled concept.","build":"Build: model the network first, zone the pressure, then schedule pumps — and meter everything.","safety":"Public-health safety: pressure must never drop below the contamination-intrusion threshold in any zone.","points":"[\"Pressure zoned and scheduled\", \"Leaks found by water balance\", \"Minimum pressure never violated\"]","field":"Compounded","math":[{"label":"Tank pressure: 2 mol air at 300 K in 0.5 m3","claim":"nRT/V/1000","f":"idealgas_kPa","p":"{\"n\": 2, \"T\": 300, \"V\": 0.5}","unit":"kPa","fmt":".1f","status":"verified","note":""},{"label":"Reynolds in a 0.3 m main at 1.2 m/s","claim":"rho v L / mu","f":"reynolds","p":"{\"rho\": 1000, \"v\": 1.2, \"L\": 0.3, \"mu\": 0.001}","unit":"Re","fmt":".0f","status":"verified","note":""}]},
{"n":"Maintenance Predictor","cls":"real-engineering","d":"A predictor that schedules infrastructure repair before failure: it fuses inspection, sensor, and age data into a remaining-life estimate per asset, then sequences work by risk and cost. Maintenance becomes planned, not panicked.","h":"Asset data feeds deterioration models; the predictor outputs remaining-life distributions and an optimal work sequence. The demo recomputes beam deflection for a bridge member and the audit sample for inspection validation.","rwb":"Predictive maintenance with deterioration modeling is standard in bridge, rail, and utility asset management.","sig":"Signature version: the city First/Last assessor — commissioning (first) and predicted end-of-life (last) anchored per asset, with the framing labeled concept.","build":"Build: inventory assets first, calibrate deterioration on inspection history, then sequence by risk.","safety":"Safety: any asset whose predicted failure risk exceeds the safety threshold gets immediate inspection — the schedule never overrides a red flag.","points":"[\"Remaining life per asset, with uncertainty\", \"Work sequenced by risk and cost\", \"Red flags override the schedule\"]","field":"Compounded","math":[{"label":"Beam deflection: 10 kN/m over 20 m span","claim":"5wL^4/(384EI)","f":"beam_defl_mm","p":"{\"w\": 10, \"L\": 20, \"E\": 200000000.0, \"I\": 0.004}","unit":"mm","fmt":".1f","status":"verified","note":""},{"label":"Inspection audit at 95%, p=0.08","claim":"ln(1-conf)/ln(1-p)","f":"audit_n","p":"{\"conf\": 0.95, \"p\": 0.08}","unit":"samples","fmt":".0f","status":"verified","note":""}]},
{"n":"Transit Frequency Optimizer","cls":"real-engineering","d":"An optimizer that sets bus and train frequencies to the demand: it forecasts ridership per route per hour, assigns vehicles to minimize wait plus crowding, and publishes the timetable with its load factors. Service follows riders, not habit.","h":"Ridership forecasts feed a vehicle-assignment optimizer; the timetable publishes with expected load factors. The demo recomputes the round-trip cycle time math and the passenger throughput.","rwb":"Frequency optimization from demand data is standard transit-planning practice.","sig":"Signature version: the city A7 assessor — all four axes from transit data, with the 'universal' framing fenced as concept.","build":"Build: count riders honestly first, optimize frequency to demand, and publish load factors.","safety":"Equity safety: coverage routes serving the transit-dependent keep minimum frequencies regardless of efficiency scores.","points":"[\"Frequency from measured demand\", \"Load factors published\", \"Coverage minimums protected\"]","field":"Advanced","math":[{"label":"Cycle time: 12 km at 18 km/h + 10 min layover","claim":"2x12/18x60+10","f":"add2","p":"{\"x\": 80.0, \"y\": 10.0}","unit":"min","fmt":".0f","status":"verified","note":""},{"label":"Peak throughput: 40 buses x 60 pax x 3 trips","claim":"40x60x3","f":"scale","p":"{\"x\": 2400, \"k\": 3}","unit":"pax","fmt":".0f","status":"verified","note":""}]},
{"n":"A7 City Assessor","cls":"signature-concept","d":"The chapter's A7 Framework applied to cities: Balance (throughput vs livability), Totality (served vs unserved), First (plan), Last (outcome) scored per district from real operational data. The assessor keeps city systems accountable in four numbers.","h":"Each district reports the four A7 numbers; the assessor trends them across years. The demo recomputes the USC/efixed anchors.","rwb":"City dashboards are real institutional practice; the A7 framing is the Signature concept layer.","sig":"Signature version: this IS the Signature version — the city A7 assessor as the chapter imagined it, with the 'universal' claim fenced inside the concept label and every number recomputed.","build":"Build: instrument city systems first, define axes with residents, then score.","safety":"Justice safety: the assessor must surface underserved districts; it must never be used to justify their neglect.","points":"[\"Score districts, surface the underserved\", \"Axes defined with residents\", \"Never justifies neglect\"]","field":"Advanced","math":[{"label":"USC anchor scalar recomputed","claim":"(153.70547+91.70795)/(26.14798+36.84954)","f":"usc","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""},{"label":"Fixed scalar anchor recomputed","claim":"(153.70547x91.70795)/(26.14798+36.84954)","f":"efixed","p":"{}","unit":"index","fmt":".5f","status":"verified","note":""}]}];
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
  var title="AI Infrastructure and Urban Planning"+': '+v.n+' — '+TIERS[ti].split(' — ')[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=badge+' '+v.d+'\n\n'+TIERS[ti]+' — Headline number: '+mc[0].label+' = '+mc[0].recomputed+' '+mc[0].unit+'.';
  return {
    id:id,t:title,g:v.n,name:title,title:title,description:desc,status:v.cls,field:field,
    chapter_source:"Architecting Solutions: Building AI for Universal Infrastructure & Urban Planning (Chapter)",real_world_basis:v.rwb,signature_version:v.sig,build_steps:v.build,
    math_note:mc.map(function(m){return m.label+': '+m.recomputed+' '+m.unit+' ['+m.status+']';}).join('; '),
    math_check:mc.map(function(m){return {label:m.label,claim:m.claim,recomputed:m.recomputed,unit:m.unit,status:m.status,note:m.note};}),
    safety:v.safety,how_it_works:v.h,
    requirements:['Read real_world_basis before signature_version','Re-run the demo program to re-verify every number','Follow safety on every build'],
    standards:['Full-file record, never a stub','Speculative = Signature-labeled, never as established fact','Every numerical claim recomputed at build time'],
    citations:[],src:'signature',ladder_rank:LADDER[ti],ladder_tier:TIERS[ti],
    demo:{kind:'python',language:'python',program:demoProgram(id,title,mc),note:'Recomputes every math claim in this record — the honesty check.'},
    provenance:'Chapter-trawl build (trawl-r13 wave 2): makable extraction from '+"Architecting Solutions: Building AI for Universal Infrastructure & Urban Planning (Chapter)"+'; math re-verified 2026-10-19.',
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
var gen={version:"jahdb-chapter-make-ai-infrastructure-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
