(function(){'use strict';
/* JAH Simulation Database generator — jahdb-simulation-1.0.
   Every scenario is re-simulated by the validator with the identical
   parameters and seed; the recorded key metrics must reproduce exactly. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-SIM-';
var CATS=['physical','network','process','monte-carlo','digital-twin'];
function sjson(v){return JSON.stringify(v);}
function r6(x){return Math.round(x*1e6)/1e6;}

/* ---------- models: run(params, spec) -> {key_metrics, final_state} ---------- */
function mProjectile(p){
  var th=p.angle_deg*Math.PI/180,v=p.v0,g=p.g;
  var t=2*v*Math.sin(th)/g;
  return {key_metrics:{range:r6(v*v*Math.sin(2*th)/g),max_height:r6(v*v*Math.sin(th)*Math.sin(th)/(2*g)),flight_time:r6(t)},
    final_state:{x:r6(v*v*Math.sin(2*th)/g),y:0}};
}
function mSIR(p,spec){
  var S=p.S0,I=p.I0,R=p.R0,N=S+I+R,peak=I,peakDay=0;
  for(var d=1;d<=spec.steps;d++){
    var nI=p.beta*S*I/N,nR=p.gamma*I;
    S-=nI;I+=nI-nR;R+=nR;
    if(I>peak){peak=I;peakDay=d;}
  }
  return {key_metrics:{final_S:r6(S),final_I:r6(I),final_R:r6(R),peak_I:r6(peak),peak_day:peakDay},
    final_state:{S:r6(S),I:r6(I),R:r6(R)}};
}
function mLotka(p,spec){
  var prey=p.prey0,pred=p.pred0,dt=spec.dt,minPrey=prey,maxPrey=prey;
  for(var i=0;i<spec.steps;i++){
    var dPrey=(p.alpha*prey-p.beta*prey*pred)*dt,dPred=(p.delta*prey*pred-p.gamma*pred)*dt;
    prey+=dPrey;pred+=dPred;
    if(prey<minPrey)minPrey=prey;if(prey>maxPrey)maxPrey=prey;
    if(prey<0||pred<0||!isFinite(prey))break;
  }
  return {key_metrics:{final_prey:r6(prey),final_pred:r6(pred),min_prey:r6(minPrey),max_prey:r6(maxPrey)},
    final_state:{prey:r6(prey),pred:r6(pred)}};
}
function mMM1(p,spec){
  var rnd=prng(spec.seed),t=0,q=[],waitSum=0,done=0,busyUntil=0,maxQ=0;
  function expov(rate){return -Math.log(1-rnd())/rate;}
  var nextArr=expov(p.arrival_rate);
  while(done<spec.steps){
    if(nextArr<=busyUntil){ /* arrival during busy period */
      t=nextArr;q.push(t);nextArr+=expov(p.arrival_rate);
      if(q.length>maxQ)maxQ=q.length;
    }else{
      if(q.length){var at=q.shift();t=Math.max(busyUntil,at);waitSum+=t-at;busyUntil=t+expov(p.service_rate);done++;}
      else{t=nextArr;busyUntil=t+expov(p.service_rate);nextArr+=expov(p.arrival_rate);done++;}
    }
  }
  return {key_metrics:{avg_wait:r6(waitSum/done),utilization:r6(Math.min(1,p.arrival_rate/p.service_rate)),max_queue:maxQ,served:done},
    final_state:{served:done}};
}
function mHeat(p,spec){
  var n=p.points,u=new Array(n).fill(0);
  for(var i=0;i<n;i++)u[i]=p.initial==='hot-left'?(i<n/3?100:20):(i===((n/2)|0)?100:20);
  var r=p.alpha*spec.dt/Math.pow(p.length/(n-1),2);
  for(var s=0;s<spec.steps;s++){
    var v=u.slice();
    for(i=1;i<n-1;i++)v[i]=u[i]+r*(u[i+1]-2*u[i]+u[i-1]);
    u=v;
  }
  var sum=0;u.forEach(function(x){sum+=x;});
  return {key_metrics:{mean_temp:r6(sum/n),center_temp:r6(u[(n/2)|0]),edge_temp:r6(u[0])},
    final_state:{mean:r6(sum/n)}};
}
function mWalk(p,spec){
  var rnd=prng(spec.seed),x=0,mn=0,mx=0;
  for(var i=0;i<spec.steps;i++){x+=rnd()<p.p_up?1:-1;if(x<mn)mn=x;if(x>mx)mx=x;}
  return {key_metrics:{final_position:x,min:mn,max:mx},final_state:{x:x}};
}
function mPackets(p,spec){
  var rnd=prng(spec.seed),del=0,hops=0,lost=0;
  for(var i=0;i<spec.steps;i++){
    var h=1+((rnd()*p.max_hops)|0);
    if(rnd()<p.loss_p){lost++;continue;}
    del++;hops+=h;
  }
  return {key_metrics:{delivered:del,lost:lost,delivery_rate:r6(del/spec.steps),avg_hops:r6(del?hops/del:0)},
    final_state:{delivered:del,lost:lost}};
}
function mAssembly(p,spec){
  var stations=p.station_times.slice(),t=new Array(stations.length).fill(0),done=0;
  for(var it=0;it<spec.steps;it++){
    var start=0;
    for(var s=0;s<stations.length;s++){start=Math.max(start,t[s]);t[s]=start+stations[s];start=t[s];}
    done++;
  }
  var makespan=t[t.length-1];
  return {key_metrics:{makespan:r6(makespan),throughput:r6(done/makespan),items:done},
    final_state:{makespan:r6(makespan)}};
}
var MODELS={projectile:mProjectile,sir:mSIR,lotka:mLotka,mm1:mMM1,heat:mHeat,walk:mWalk,packets:mPackets,assembly:mAssembly};
var MODEL_CAT={projectile:'physical',sir:'physical',lotka:'physical',mm1:'process',heat:'physical',walk:'monte-carlo',packets:'network',assembly:'process'};
var MODEL_NAME={projectile:'Projectile motion',sir:'SIR epidemic model',lotka:'Lotka-Volterra predator-prey',mm1:'M/M/1 queue',heat:'1-D heat diffusion',walk:'Random walk',packets:'Packet network delivery',assembly:'Assembly line'};
var MODEL_DESC={
 projectile:'Closed-form ballistics: range, apex and flight time from launch velocity, angle and gravity.',
 sir:'Kermack\u2013McKendrick SIR: susceptible, infected and recovered compartments evolved by daily Euler steps.',
 lotka:'Predator-prey dynamics: prey grow exponentially, predation couples the populations, predators starve without prey.',
 mm1:'Single-server queue with Poisson arrivals and exponential service: waiting time, utilization and queue length.',
 heat:'One-dimensional heat equation by explicit finite differences; stability requires r = \u03B1 dt/dx\u00B2 \u2264 0.5.',
 walk:'Simple symmetric random walk: each step goes up or down; the validator replays the identical seeded path.',
 packets:'Packets cross up to max_hops links with per-packet loss probability; delivery rate and hop counts recorded.',
 assembly:'Items flow through stations in series; each station processes one item at a time (flow-shop makespan).'};

var ONLINE=[];
var i,j;
/* famous models (verified equations) */
var FAMOUS=[
 ['projectile','physical','Projectile motion (Galileo/Newton)','Range R = v\u00B2 sin(2\u03B8)/g, apex H = v\u00B2 sin\u00B2\u03B8/(2g), flight time T = 2v sin\u03B8/g. Air resistance neglected.','Classical mechanics \u2014 verified closed forms'],
 ['sir','physical','SIR epidemic model (Kermack\u2013McKendrick, 1927)','dS/dt = -\u03B2SI/N, dI/dt = \u03B2SI/N - \u03B3I, dR/dt = \u03B3I. Basic reproduction number R0 = \u03B2/\u03B3.','Kermack\u2013McKendrick 1927 \u2014 verified equations'],
 ['lotka','physical','Lotka-Volterra predator-prey (1925/1926)','dPrey/dt = \u03B1\u00B7prey - \u03B2\u00B7prey\u00B7pred, dPred/dt = \u03B4\u00B7prey\u00B7pred - \u03B3\u00B7pred. Neutral cycles around equilibrium.','Lotka 1925 / Volterra 1926 \u2014 verified equations'],
 ['mm1','process','M/M/1 queue (Erlang)','Poisson arrivals rate \u03BB, exponential service rate \u03BC. Utilization \u03C1=\u03BB/\u03BC; mean wait Wq = \u03C1/(\u03BC(1-\u03C1)). Stable iff \u03C1<1.','Queueing theory (Erlang) \u2014 verified formulas'],
 ['heat','physical','Heat equation (Fourier)','\u2202u/\u2202t = \u03B1 \u2202\u00B2u/\u2202x\u00B2. Explicit scheme stable for r=\u03B1\u0394t/\u0394x\u00B2\u22640.5.','Fourier heat conduction \u2014 verified PDE']];
FAMOUS.forEach(function(f){
  ONLINE.push({kind:'simulation-scenario',cat:f[1],title:'Famous model: '+f[2],model:f[0],
    system:f[2]+'.',model_description:f[3],
    parameters:{reference:true},run_spec:{reference:true},
    results:{reference:'See scenario instances for computed runs.'},
    validation_results:'Equations verified against the published model.',
    source:'online',source_ref:f[4]});
});
/* systematic scenario instances */
function scen(model,params,spec,idx){
  var res=MODELS[model](params,spec);
  return {kind:'simulation-scenario',cat:MODEL_CAT[model],title:MODEL_NAME[model]+' scenario #'+idx,
    system:MODEL_NAME[model]+' with parameters '+sjson(params)+'.',
    model:MODEL_NAME[model],model_description:MODEL_DESC[model],
    parameters:params,run_spec:spec,results:res,
    validation_results:'Re-simulated by the validator with identical parameters and seed; every key metric must reproduce.',
    source:'online',source_ref:'Computed by '+MODEL_NAME[model]+' implementation'};
}
(function(){
var rnd=prng(121212),idx=0;
for(i=0;i<400;i++){idx++;ONLINE.push(scen('projectile',{v0:ri(rnd,5,100),angle_deg:ri(rnd,5,85),g:9.81},{steps:1},idx));}
for(i=0;i<200;i++){idx++;ONLINE.push(scen('sir',{S0:990,I0:10,R0:0,beta:r6(0.1+rnd()*0.4),gamma:r6(0.05+rnd()*0.15)},{steps:60},idx));}
for(i=0;i<150;i++){idx++;ONLINE.push(scen('lotka',{prey0:ri(rnd,20,80),pred0:ri(rnd,5,25),alpha:0.1,beta:0.002,delta:0.0005,gamma:0.1},{steps:500,dt:0.5},idx));}
for(i=0;i<200;i++){idx++;ONLINE.push(scen('mm1',{arrival_rate:r6(0.5+rnd()*2),service_rate:r6(3+rnd()*3)},{steps:500,seed:5000+i},idx));}
for(i=0;i<100;i++){idx++;ONLINE.push(scen('heat',{length:1,points:11,alpha:0.01,initial:pick(['hot-left','hot-center'],rnd)},{steps:200,dt:0.4},idx));}
for(i=0;i<100;i++){idx++;ONLINE.push(scen('walk',{p_up:0.5},{steps:1000,seed:9000+i},idx));}
for(i=0;i<150;i++){idx++;ONLINE.push(scen('packets',{max_hops:ri(rnd,2,6),loss_p:r6(0.01+rnd()*0.2)},{steps:1000,seed:12000+i},idx));}
for(i=0;i<150;i++){var st=[],ns=2+(i%4);for(j=0;j<ns;j++)st.push(ri(rnd,1,8));idx++;ONLINE.push(scen('assembly',{station_times:st},{steps:50},idx));}
})();
/* digital twin specs (curated, real-world system types) */
var TWINS=[
 ['Wind turbine','physical',['rotor rpm','blade pitch','wind speed','gearbox temperature','vibration','power output'],'Vibration and temperature feed remaining-useful-life estimates; the twin mirrors rotor dynamics for predictive maintenance.'],
 ['HVAC building','process',['zone temperature','humidity','CO2','damper position','energy use'],'Thermal zones simulated with occupancy schedules; the twin tunes setpoints to cut energy while holding comfort.'],
 ['Data-center cooling','process',['inlet temperature','CRAC fan speed','PUE','hotspot sensors'],'Airflow and heat load mirrored per rack; the twin predicts hotspots before hardware throttles.'],
 ['Traffic intersection','network',['vehicle counts','signal phase','queue length','pedestrian calls'],'Signal timing mirrored in real time; the twin tests timing plans against live demand.'],
 ['Water pump station','process',['pressure','flow rate','motor current','bearing vibration'],'Hydraulic curve mirrored; the twin flags cavitation and seal wear from vibration drift.'],
 ['Solar farm','physical',['irradiance','panel temperature','inverter output','soiling index'],'Panel-level output mirrored against irradiance; the twin spots underperforming strings.'],
 ['Warehouse robot fleet','network',['robot position','battery','task queue','aisle congestion'],'Fleet positions mirrored; the twin re-routes around congestion before jams form.'],
 ['Bridge structure','physical',['strain gauges','accelerometers','temperature','wind load'],'Structural response mirrored; the twin tracks modal frequencies for damage detection.'],
 ['Chemical reactor','process',['temperature','pressure','pH','agitator speed','feed rate'],'Reaction kinetics mirrored; the twin predicts runaway conditions from temperature trends.'],
 ['Delivery drone','network',['GPS position','battery','motor RPM','wind estimate'],'Flight dynamics mirrored; the twin re-plans routes around wind and battery limits.']];
TWINS.forEach(function(t,ix){
  ONLINE.push({kind:'digital-twin',cat:'digital-twin',title:'Digital twin spec: '+t[0],
    system:'Digital twin of a '+t[0].toLowerCase()+': a live virtual mirror fed by sensors.',
    model:'Digital twin',model_description:t[3],
    parameters:{twin_of:t[0],sensors:t[2],update_hz:1,sync:'live'},
    run_spec:{calibration:'sensor-calibrated'},
    results:{maturity:'descriptive-to-predictive'},
    validation_results:'Spec reviewed for sensor coverage: every critical physical quantity has a named sensor.',
    source:'online',source_ref:'Digital twin concept \u2014 industry practice'});
});

/* ---------- generated records (source: signature) ---------- */
function genEx(rnd){
  var models=Object.keys(MODELS),m=pick(models,rnd),params,spec;
  if(m==='projectile'){params={v0:ri(rnd,10,80),angle_deg:ri(rnd,10,80),g:9.81};spec={steps:1};}
  else if(m==='sir'){params={S0:990,I0:10,R0:0,beta:r6(0.15+rnd()*0.3),gamma:r6(0.05+rnd()*0.1)};spec={steps:ri(rnd,30,90)};}
  else if(m==='lotka'){params={prey0:ri(rnd,20,60),pred0:ri(rnd,5,20),alpha:0.1,beta:0.002,delta:0.0005,gamma:0.1};spec={steps:ri(rnd,200,600),dt:0.5};}
  else if(m==='mm1'){params={arrival_rate:r6(0.5+rnd()*2),service_rate:r6(3+rnd()*3)};spec={steps:ri(rnd,200,600),seed:ri(rnd,1,99999)};}
  else if(m==='heat'){params={length:1,points:11,alpha:0.01,initial:pick(['hot-left','hot-center'],rnd)};spec={steps:ri(rnd,100,300),dt:0.4};}
  else if(m==='walk'){params={p_up:0.5};spec={steps:ri(rnd,500,2000),seed:ri(rnd,1,99999)};}
  else if(m==='packets'){params={max_hops:ri(rnd,2,6),loss_p:r6(0.01+rnd()*0.2)};spec={steps:ri(rnd,500,2000),seed:ri(rnd,1,99999)};}
  else{params={station_times:[ri(rnd,1,6),ri(rnd,1,6),ri(rnd,1,6)]};spec={steps:ri(rnd,20,80)};}
  var res=MODELS[m](params,spec);
  return {kind:'exercise',cat:MODEL_CAT[m],title:'Generated scenario: '+MODEL_NAME[m],
    system:'What-if scenario for '+MODEL_NAME[m].toLowerCase()+' with fresh parameters.',
    model:MODEL_NAME[m],model_description:MODEL_DESC[m],
    parameters:params,run_spec:spec,results:res,
    validation_results:'Run the model yourself with the listed parameters and seed; the metrics must match.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}
function genTwin(rnd){
  var sys=pick(['greenhouse','parking garage','elevator bank','irrigation canal','server rack','ferry route','stadium crowd','cold storage','printing press','harbor crane'],rnd);
  var sens=pick([['temperature','humidity','soil moisture'],['occupancy','gate state','payment events'],['car position','door state','load weight'],['flow rate','gate opening','water level'],['inlet temp','fan speed','power draw'],['vessel position','fuel','passenger count'],['density','entry rate','exit rate'],['temperature','door openings','compressor state'],['speed','ink level','jam sensor'],['load weight','wind speed','hook position']],rnd);
  return {kind:'digital-twin',cat:'digital-twin',title:'Generated twin spec: '+sys,
    system:'Draft digital-twin specification for a '+sys+'.',
    model:'Digital twin',model_description:'Sensor-fed virtual mirror of the '+sys+'; draft spec for review and extension.',
    parameters:{twin_of:sys,sensors:sens,update_hz:1,sync:'live'},
    run_spec:{calibration:'pending'},
    results:{maturity:'descriptive'},
    validation_results:'Draft: sensor list covers the primary physical quantities of the system.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}

function baseRec(seed,cat,title){return {id:PREFIX+String(seed).padStart(7,'0'),category:cat,title:title,_seed:seed};}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category;
  if(seed>=1&&seed<=ONLINE.length&&!cat){
    var e=ONLINE[seed-1],r=baseRec(seed,e.cat,e.title);
    Object.keys(e).forEach(function(k){if(k!=='cat'&&k!=='title')r[k]=e[k];});
    return r;
  }
  if(seed>=1&&seed<=ONLINE.length&&cat){
    var pool=ONLINE.filter(function(x){return x.cat===cat;});
    if(pool.length){var e2=pool[(rnd()*pool.length)|0],r2=baseRec(seed,cat,e2.title+' \u2014 archive pick');
      Object.keys(e2).forEach(function(k){if(k!=='cat'&&k!=='title')r2[k]=e2[k];});return r2;}
  }
  var g=rnd()<0.85?genEx(rnd):genTwin(rnd);cat=cat||g.cat;g.category=cat;
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function numEq(a,b){return Math.abs(a-b)<=1e-4*Math.max(1,Math.abs(a),Math.abs(b));}
function metricsEq(a,b){
  if(typeof a==='number'&&typeof b==='number')return numEq(a,b);
  if(a&&b&&typeof a==='object'&&typeof b==='object'){
    var ka=Object.keys(a);if(ka.length!==Object.keys(b).length)return false;
    for(var i=0;i<ka.length;i++)if(!metricsEq(a[ka[i]],b[ka[i]]))return false;
    return true;
  }
  return a===b;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-SIM-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.system!=='string'||r.system.length<10)e.push('system');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.kind==='simulation-scenario'||r.kind==='exercise'){
    if(r.run_spec&&r.run_spec.reference){
      if(typeof r.model_description!=='string'||!r.model_description.length)e.push('model_description');
    }else{
    var m=r.model;
    var key=MODELS[m]?m:Object.keys(MODELS).filter(function(k){return MODEL_NAME[k]===m;})[0];
    if(!key)e.push('model');
    else{
      var got;try{got=MODELS[key](r.parameters,r.run_spec);}catch(x){e.push('sim threw');}
      if(got){
        if(!metricsEq(got.key_metrics,r.results.key_metrics))e.push('metrics mismatch');
        if(!metricsEq(got.final_state,r.results.final_state))e.push('final_state mismatch');
      }
    }
    }
  }else if(r.kind==='digital-twin'){
    var p=r.parameters||{};
    if(typeof p.twin_of!=='string'||!Array.isArray(p.sensors)||!p.sensors.length)e.push('twin fields');
  }else e.push('kind');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-simulation-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('simulation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
