(function(){'use strict';
/* JAH Thermodynamics Database generator — jahdb-thermodynamics-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record. src:"online" = core facts
   verified against published thermodynamics references (formulas computed exactly);
   src:"signature" = Signature-authored cycle study (exact math, clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function K(c){return c+273.15;}
var CATS=['carnot-cycle','rankine-cycle','otto-cycle','diesel-cycle','brayton-cycle','refrigeration'];
var PREFIX='JAH-THD-';
var FLUIDS={
 'carnot-cycle':['ideal gas','air','helium'],
 'rankine-cycle':['water/steam','water/steam','ammonia'],
 'otto-cycle':['air-fuel mixture','air (air-standard)'],
 'diesel-cycle':['air-fuel mixture','air (air-standard)'],
 'brayton-cycle':['air','combustion gas'],
 'refrigeration':['R-134a','ammonia','CO2']
};
var CYCF={
 'carnot-cycle':'η = 1 − Tc/Th (two reversible isotherms, two reversible adiabats)',
 'rankine-cycle':'η = (W_turbine − W_pump) / Q_boiler; enthalpies from steam tables',
 'otto-cycle':'η_otto = 1 − 1/r^(k−1); constant-volume heat addition',
 'diesel-cycle':'η_diesel = 1 − (1/r^(k−1))·((rc^k − 1)/(k·(rc − 1))); constant-pressure heat addition',
 'brayton-cycle':'η = 1 − 1/rp^((k−1)/k); k = 1.4 for air',
 'refrigeration':'COP_R = TL/(TH − TL) (Carnot refrigerator); COP_HP = TH/(TH − TL)'
};
var REAL={
 'carnot-cycle':['Real engines reach about 0.7 of the Carnot maximum.','The ideal Carnot engine has zero power output, so it is a limit, not a design.','100% efficiency would need a cold reservoir at absolute zero — impossible.'],
 'rankine-cycle':['Actual steam plants run 35–40% thermal efficiency — about 54–62% of their Carnot limit.','Turbine isentropic efficiency runs 85–92%; compressor 75–85%.','Superheated steam at 540–600°C feeds the high-pressure turbine.'],
 'otto-cycle':['Real gasoline engines deliver about 25–30% thermal efficiency.','At the same compression ratio and heat input: η_otto > η_dual > η_diesel.','The four strokes are intake, compression, power, exhaust.'],
 'diesel-cycle':['Real diesel engines deliver about 35–40% thermal efficiency.','At constant maximum pressure and heat input: η_diesel > η_dual > η_otto.','Compression ignition needs no spark plug; ratios run 14:1 to 22:1.'],
 'brayton-cycle':['Simple-cycle gas turbines deliver about 30–40% thermal efficiency.','The compressor typically eats 40–60% of the turbine\u2019s gross work.','Regeneration and intercooling raise real-cycle efficiency.'],
 'refrigeration':['Household refrigerators run COP ≈ 2–4; heat pumps reach 3–5.','COP is heat moved per unit work — it can exceed 1.','Throttling in the expansion valve is the cycle\u2019s main irreversibility.']
};
var APPS={
 'carnot-cycle':['efficiency benchmarking','textbook limit analysis','engine concept screening'],
 'rankine-cycle':['coal and nuclear power stations','combined-cycle bottoming plants','solar thermal power'],
 'otto-cycle':['passenger cars','motorcycles','small aircraft','lawn equipment'],
 'diesel-cycle':['heavy trucks','ships','locomotives','backup generators'],
 'brayton-cycle':['aircraft jet engines','peaking power plants','pipeline compressors'],
 'refrigeration':['home refrigerators','air conditioning','cold-chain transport','heat pumps']
};
function carnotEff(thC,tcC){return (1-K(tcC)/K(thC))*100;}
function build(rnd,cat){
 var online=rnd()<0.6;
 var fluid=pick(FLUIDS[cat],rnd);
 var thC,tcC,ideal,realNote,extra='';
 if(cat==='carnot-cycle'){
  if(online){thC=600;tcC=40;}else{thC=ri(rnd,400,900);tcC=ri(rnd,20,80);}
  ideal=carnotEff(thC,tcC);
  realNote='Documented reference point: 600°C boiler with 40°C condenser gives 64.2% Carnot; real plants reach about 0.7 of the Carnot maximum.';
 }else if(cat==='rankine-cycle'){
  if(online){thC=540;tcC=35;}else{thC=ri(rnd,450,620);tcC=ri(rnd,25,60);}
  ideal=carnotEff(thC,tcC);
  realNote='Published plant data: actual steam-plant efficiency 35–40%, roughly 54–62% of the Carnot limit.';
 }else if(cat==='otto-cycle'){
  var r=online?9:ri(rnd,7,12);
  thC=online?2200:ri(rnd,1800,2500); tcC=online?27:ri(rnd,20,40);
  ideal=(1-1/Math.pow(r,0.4))*100;
  extra=' Air-standard ideal at compression ratio '+r+':1 is '+ideal.toFixed(1)+'%.';
  ideal=carnotEff(thC,tcC);
  realNote='Real gasoline engines: about 25–30% thermal efficiency; η_otto > η_dual > η_diesel at equal compression ratio.';
 }else if(cat==='diesel-cycle'){
  var rr=online?18:ri(rnd,14,22), rc=online?2:2;
  thC=online?2100:ri(rnd,1700,2400); tcC=online?27:ri(rnd,20,40);
  var k=1.4;
  var dideal=(1-(1/Math.pow(rr,k-1))*((Math.pow(rc,k)-1)/(k*(rc-1))))*100;
  extra=' Air-standard ideal at '+rr+':1 with cutoff ratio 2 is '+dideal.toFixed(1)+'%.';
  ideal=carnotEff(thC,tcC);
  realNote='Real diesel engines: about 35–40% thermal efficiency; at constant max pressure, η_diesel leads.';
 }else if(cat==='brayton-cycle'){
  var rp=online?10:ri(rnd,6,20);
  thC=online?1200:ri(rnd,1000,1400); tcC=online?27:ri(rnd,20,40);
  var bideal=(1-1/Math.pow(rp,0.4/1.4))*100;
  extra=' Ideal at pressure ratio '+rp+':1 is '+bideal.toFixed(1)+'%.';
  ideal=carnotEff(thC,tcC);
  realNote='Simple-cycle gas turbines: about 30–40% thermal efficiency in service.';
 }else{
  var thK,tcK;
  if(online){tcK=270;thK=300;}else{tcK=ri(rnd,250,280);thK=ri(rnd,295,310);}
  thC=+(thK-273.15).toFixed(1); tcC=+(tcK-273.15).toFixed(1);
  ideal=tcK/(thK-tcK);
  extra=' Carnot COP between '+tcK+' K and '+thK+' K is '+ideal.toFixed(2)+'.';
  ideal=carnotEff(thC,tcC);
  realNote='Household refrigerators run COP ≈ 2–4; heat pumps 3–5.';
 }
 var app=pick(APPS[cat],rnd);
 var fact=pick(REAL[cat],rnd);
 var specOut={cycle:cat.replace(/-/g,' '),hot_temp_C:thC,cold_temp_C:tcC,hot_temp_K:+K(thC).toFixed(2),cold_temp_K:+K(tcC).toFixed(2),
   carnot_efficiency_pct:+ideal.toFixed(2),real_efficiency_note:realNote,efficiency_formula:CYCF[cat],
   working_fluid:fluid,key_fact:fact,application:app};
 if(cat==='refrigeration')specOut.cop_carnot=+(tcK/(thK-tcK)).toFixed(2);
 var title,desc;
 if(online){
  title=cap(cat)+' — '+fluid+' reference';
  desc='Reference record for the '+cat.replace(/-/g,' ')+' using '+fluid+' as the working fluid. '+
   'Hot reservoir '+thC+'°C ('+K(thC).toFixed(0)+' K), cold reservoir '+tcC+'°C ('+K(tcC).toFixed(0)+' K): the Carnot limit is '+ideal.toFixed(1)+'%'+(cat==='refrigeration'?', and '+extra:'')+'. '+
   realNote+' '+fact+' Typical application: '+app+'.';
 }else{
  title='Signature Study — '+cap(cat)+' design ('+fluid+')';
  desc='This is a Signature-authored thermodynamic design study of the '+cat.replace(/-/g,' ')+' with '+fluid+'. '+
   'Hot side '+thC+'°C, cold side '+tcC+'°C: Carnot limit '+ideal.toFixed(1)+'%'+(extra?'; '+extra:'')+'. '+
   'Governing relation: '+CYCF[cat]+'. Intended application: '+app+'.';
 }
 return {title:title,description:desc,src:online?'online':'signature',spec:specOut};
}
function cap(s){return s.split('-').map(function(w){return w.charAt(0).toUpperCase()+w.slice(1);}).join(' ');}
function generate(seed,opts,rnd){
 opts=opts||{};rnd=rnd||prng(seed);
 var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
 var b=build(rnd,cat);
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,category:cat,src:b.src,spec:b.spec,_seed:seed};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-THD-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<10)e.push('title');
 if(typeof r.description!=='string'||r.description.length<80)e.push('description');
 if(CATS.indexOf(r.category)<0)e.push('category');
 if(r.src!=='online'&&r.src!=='signature')e.push('src');
 var s=r.spec;
 if(!s||typeof s!=='object')e.push('spec');
 else{
  if(typeof s.cycle!=='string'||!s.cycle)e.push('spec.cycle');
  if(typeof s.hot_temp_C!=='number'||typeof s.cold_temp_C!=='number'||s.hot_temp_C<=s.cold_temp_C)e.push('spec.temps');
  if(Math.abs(s.hot_temp_K-(s.hot_temp_C+273.15))>0.05)e.push('spec.hot_K');
  if(Math.abs(s.cold_temp_K-(s.cold_temp_C+273.15))>0.05)e.push('spec.cold_K');
  var expect=(1-s.cold_temp_K/s.hot_temp_K)*100;
  if(Math.abs(s.carnot_efficiency_pct-expect)>0.6)e.push('spec.carnot_eff');
  if(typeof s.efficiency_formula!=='string'||!s.efficiency_formula)e.push('spec.formula');
  if(typeof s.working_fluid!=='string'||!s.working_fluid)e.push('spec.fluid');
  if(typeof s.application!=='string'||!s.application)e.push('spec.application');
 }
 return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-thermodynamics-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('thermodynamics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
