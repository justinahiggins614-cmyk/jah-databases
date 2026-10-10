(function(){'use strict';
/* JAH Energy Systems Database — deterministic boundless generator.
   Conceptual generation/storage concepts; validate() recomputes all math. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['solar','wind','storage','grid','nuclear'];
var PREFIX='JAH-ENGY-';
var RTYPES=['datasheet','performance','calculation','technology','application','selection','installation','maintenance','safety','economics','standards','history','comparison','concept-design','dimensions','tolerance-class','material-process','failure-modes'];
var FORMULAS={
 solar_output:function(i){return i.area_m2*i.irradiance_W_m2*i.efficiency/1000;}, /* kW */
 wind_power:function(i){return 0.5*1.225*i.area_m2*Math.pow(i.v_ms,3)*i.Cp/1e6;},   /* MW */
 storage_mwh:function(i){return i.MW*i.hours;},
 capacity_factor:function(i){return i.actual_MWh/(i.MW*8760)*100;},                /* % */
 hydro_power:function(i){return 1000*9.81*i.Q_m3s*i.H_m*i.eff/1e6;},               /* MW */
 lcoe:function(i){return i.capex_per_kW*1000*i.crf/(8760*i.cf/100)+i.opex_per_MWh;}, /* $/MWh approx */
 nuclear_burnup:function(i){return i.MW*365*i.cf/i.fuel_t;},                        /* MWd/t approx */
 electrolyzer_h2:function(i){return i.MW*1000*i.eff/39.4;}                          /* kg/h approx (HHV) */
};
var TECH=[
 ['Solar PV Array','solar'],['Wind Turbine','wind'],['Battery Storage','storage'],
 ['Pumped Hydro','storage'],['Grid Substation','grid'],['SMR Nuclear','nuclear'],
 ['Solar Thermal','solar'],['Offshore Wind','wind'],['Flow Battery','storage'],
 ['HVDC Link','grid'],['Fusion Concept','nuclear'],['Green Hydrogen','storage']
];
function num(n,d){return +(+n).toFixed(d==null?2:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var tf=TECH.filter(function(x){return x[1]===cat;});
  var t=pick(tf.length?tf:TECH,rnd);
  var tag='EY-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var spec={},calc=null,desc='';
  function C(formula,inputs,unit){return {formula:formula,inputs:inputs,result:sfig(FORMULAS[formula](inputs)),unit:unit};}
  if(t[0]==='Solar PV Array'){
    var area=ri(rnd,100,100000),eff=rf(rnd,18,26,1),irr=ri(rnd,800,1100);
    var kw=FORMULAS.solar_output({area_m2:area,irradiance_W_m2:irr,efficiency:eff});
    calc=C('solar_output',{area_m2:area,irradiance_W_m2:irr,efficiency:eff},'kW');
    spec={area_m2:area,module_efficiency_pct:eff,irradiance_W_m2:irr,peak_kW:num(kw,1),tilt_deg:ri(rnd,10,35)};
    desc='Concept solar array '+tag+': '+area.toLocaleString()+' m² at '+eff+'% module efficiency under '+irr+' W/m² peaks at '+num(kw,1)+' kW. Generated concept: run a full yield model with local TMY data before sizing inverters.';
  }else if(t[0]==='Wind Turbine'){
    var D=ri(rnd,80,220),v=rf(rnd,6,12,1),Cp=rf(rnd,0.35,0.48,2);
    var ar=Math.PI*Math.pow(D/2,2),mw=FORMULAS.wind_power({area_m2:ar,v_ms:v,Cp:Cp});
    calc=C('wind_power',{area_m2:num(ar,1),v_ms:v,Cp:Cp},'MW');
    spec={rotor_dia_m:D,swept_area_m2:num(ar,0),wind_ms:v,Cp:Cp,rated_MW:num(mw,2),hub_height_m:ri(rnd,80,160)};
    desc='Concept wind turbine '+tag+': '+D+' m rotor in '+v+' m/s wind at Cp '+Cp+' → '+num(mw,2)+' MW. Generated concept: verify against the site wind distribution and grid code ride-through rules.';
  }else if(t[0]==='Battery Storage'){
    var MW=ri(rnd,10,500),hrs=rf(rnd,1,8,1);
    calc=C('storage_mwh',{MW:MW,hours:hrs},'MWh');
    spec={power_MW:MW,duration_h:hrs,energy_MWh:num(MW*hrs,1),chemistry:'LFP (concept)',cycles:6000};
    desc='Concept battery plant '+tag+': '+MW+' MW × '+hrs+' h = '+num(MW*hrs,1)+' MWh of LFP storage. Generated concept: confirm augmentation plan and fire-code spacing for the real site.';
  }else if(t[0]==='Pumped Hydro'){
    var Q=rf(rnd,20,300,0),H=ri(rnd,100,800),ef=rf(rnd,0.8,0.9,2);
    var pmw=FORMULAS.hydro_power({Q_m3s:Q,H_m:H,eff:ef});
    calc=C('hydro_power',{Q_m3s:Q,H_m:H,eff:ef},'MW');
    spec={flow_m3_s:Q,head_m:H,efficiency:ef,power_MW:num(pmw,1),upper_reservoir:'conceptual'};
    desc='Concept pumped-hydro '+tag+': '+Q+' m³/s through '+H+' m head at '+ef+' efficiency → '+num(pmw,1)+' MW. Generated concept: geotechnical and water-rights studies gate any real project.';
  }else if(t[0]==='Grid Substation'){
    var kv=pick([69,115,230,345,500],rnd),mva=ri(rnd,50,800);
    spec={voltage_kV:kv,capacity_MVA:mva,bus:'double breaker-double bus (concept)',transformers:ri(rnd,1,4)};
    desc='Concept substation '+tag+': '+kv+' kV, '+mva+' MVA. Generated concept: protection coordination and arc-flash studies required for real design.';
    calc={formula:'storage_mwh',inputs:{MW:mva,hours:1},result:mva,unit:'MVA rating reference'};
  }else if(t[0]==='SMR Nuclear'){
    var mw2=ri(rnd,50,470),cf=rf(rnd,0.85,0.95,2);
    var gwh=FORMULAS.capacity_factor({actual_MWh:mw2*8760*cf,MW:mw2});
    calc=C('capacity_factor',{actual_MWh:num(mw2*8760*cf,0),MW:mw2},'%');
    spec={power_MW:mw2,capacity_factor_pct:num(cf*100,1),annual_GWh:num(mw2*8760*cf/1000,0),coolant:'light water (concept)'};
    desc='Concept SMR '+tag+': '+mw2+' MWe at '+num(cf*100,1)+'% capacity factor → '+num(mw2*8760*cf/1000,0)+' GWh/yr. Generated concept: licensing path and fuel supply gate everything in nuclear.';
  }else if(t[0]==='Solar Thermal'){
    var area2=ri(rnd,50000,500000),ef2=rf(rnd,0.35,0.45,2);
    var kw2=FORMULAS.solar_output({area_m2:area2,irradiance_W_m2:950,efficiency:ef2*100});
    calc=C('solar_output',{area_m2:area2,irradiance_W_m2:950,efficiency:num(ef2*100,1)},'kW');
    spec={mirror_area_m2:area2,thermal_efficiency:num(ef2*100,1),peak_kW:num(kw2,0),storage_h:ri(rnd,4,12)};
    desc='Concept solar-thermal '+tag+': '+area2.toLocaleString()+' m² of mirrors, '+num(ef2*100,1)+'% thermal efficiency, '+num(kw2/1000,1)+' MW peak with '+spec.storage_h+' h storage. Generated concept: water use and soiling drive real siting.';
  }else if(t[0]==='Offshore Wind'){
    var D2=ri(rnd,150,260),v2=rf(rnd,8,13,1);
    var ar2=Math.PI*Math.pow(D2/2,2),mw3=FORMULAS.wind_power({area_m2:ar2,v_ms:v2,Cp:0.45});
    calc=C('wind_power',{area_m2:num(ar2,1),v_ms:v2,Cp:0.45},'MW');
    spec={rotor_dia_m:D2,wind_ms:v2,rated_MW:num(mw3,1),foundation:'monopile (concept)',distance_km:ri(rnd,10,80)};
    desc='Concept offshore turbine '+tag+': '+D2+' m rotor, '+num(mw3,1)+' MW at '+v2+' m/s. Generated concept: foundation and O&M logistics dominate real offshore economics.';
  }else if(t[0]==='Flow Battery'){
    var MW4=ri(rnd,5,100),hrs4=rf(rnd,4,12,1);
    calc=C('storage_mwh',{MW:MW4,hours:hrs4},'MWh');
    spec={power_MW:MW4,duration_h:hrs4,energy_MWh:num(MW4*hrs4,1),chemistry:'vanadium redox (concept)'};
    desc='Concept flow battery '+tag+': '+MW4+' MW / '+num(MW4*hrs4,1)+' MWh vanadium redox. Generated concept: electrolyte leasing can reshape the economics — model it.';
  }else if(t[0]==='HVDC Link'){
    var kv2=pick([320,500,800],rnd),mw5=ri(rnd,500,4000),km=ri(rnd,200,2000);
    spec={voltage_kV:kv2,capacity_MW:mw5,length_km:km,loss_pct:num(km*0.0003*100,2)};
    desc='Concept HVDC link '+tag+': ±'+kv2+' kV, '+mw5+' MW over '+km+' km (~'+num(km*0.0003*100,2)+'% line loss). Generated concept: converter stations set the real cost.';
    calc={formula:'storage_mwh',inputs:{MW:mw5,hours:1},result:mw5,unit:'MW capacity reference'};
  }else if(t[0]==='Fusion Concept'){
    var q=rf(rnd,0.5,10,1);
    spec={Q_gain:q,approach:pick(['tokamak','stellarator','inertial'],rnd),fuel:'D-T (concept)',stage:'conceptual'};
    desc='Concept fusion plant '+tag+': target Q = '+q+' via '+spec.approach+'. Generated concept at paper-study maturity: breakeven physics and tritium breeding gate all timelines.';
    calc={formula:'capacity_factor',inputs:{actual_MWh:q*1000,MW:1000},result:num(q/8760*100,4),unit:'% placeholder'};
  }else{
    var MW6=ri(rnd,10,200),ef6=rf(rnd,0.6,0.75,2);
    var h2=FORMULAS.electrolyzer_h2({MW:MW6,eff:ef6});
    calc=C('electrolyzer_h2',{MW:MW6,eff:ef6},'kg/h');
    spec={electrolyzer_MW:MW6,efficiency_LHV:num(ef6,2),hydrogen_kg_h:num(h2,1),storage:'salt cavern (concept)'};
    desc='Concept green-hydrogen '+tag+': '+MW6+' MW electrolyzer at '+num(ef6*100,0)+'% LHV efficiency → '+num(h2,1)+' kg/h H₂. Generated concept: offtake contracts decide whether it gets built.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,engy_id:id,title:t[0]+' '+tag+' — Concept Study',category:cat,record_type:'concept-design',
    system:t[0]+' '+tag,technology:t[0],specifications:spec,performance:{maturity:'conceptual'},
    calculations:calc,description:desc,source:'signature',
    source_ref:{authority:'JAH Databases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',design_status:'conceptual study — not an operating plant; figures are modeled, not metered',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ENGY-\d{7}$/.test(r.id||''))e.push('id');
  if(r.engy_id!==r.id)e.push('engy_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.system!=='string'||!r.system.length)e.push('system');
  if(!r.specifications||typeof r.specifications!=='object')e.push('specifications');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&(!r.source_ref||!r.source_ref.authority))e.push('source_ref');
  var c=r.calculations;
  if(c){var f=FORMULAS[c.formula];
    if(!f)e.push('calc_formula');
    else{var expect=f(c.inputs),got=+c.result;
      if(!(got>=0)||Math.abs(got-expect)/Math.max(expect,1e-12)>0.03)e.push('calc_recompute');}}
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-energy-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('energy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
