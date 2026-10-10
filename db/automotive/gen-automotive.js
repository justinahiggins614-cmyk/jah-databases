(function(){'use strict';
/* JAH Automotive Database — deterministic boundless generator.
   Conceptual vehicle/system records; validate() recomputes all math. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['engines','electric','maintenance','diagnostics','safety'];
var PREFIX='JAH-AUTO-';
var RTYPES=['datasheet','specifications','calculation','diagnostics','maintenance','safety','technology','application','selection','history','comparison','concept-design','dimensions','tolerance-class','material-process','installation','failure-modes','standards'];
var FORMULAS={
 power_kw:function(i){return i.hp*0.7457;},
 torque_nm:function(i){return i.hp*7121/i.rpm;},
 braking_dist:function(i){return i.v_ms*i.v_ms/(2*9.81*i.mu);},   /* m */
 stopping:function(i){return i.v_ms*1.5+i.v_ms*i.v_ms/(2*9.81*i.mu);},
 fuel_L100:function(i){return i.liters/i.km*100;},
 ev_range:function(i){return i.kwh/i.kwh_100km*100;},
 tire_circ:function(i){return Math.PI*(i.rim_in*25.4+2*i.width_mm*i.aspect/100)/1000;}, /* m */
 gear_speed:function(i){return i.rpm*i.tire_m*60/(i.ratio*1000);}, /* km/h */
 oil_capacity:function(i){return i.disp_L*1.6;},
 coolant_mix:function(i){return i.total_L*0.5;}
};
var ARCH=[
 ['Concept Sedan','engines'],['Concept SUV','engines'],['Concept EV','electric'],
 ['Concept Hybrid','electric'],['Concept Coupe','engines'],['Concept Pickup','engines'],
 ['Diagnostic Case','diagnostics'],['Service Procedure','maintenance'],['Safety System','safety']
];
function num(n,d){return +(+n).toFixed(d==null?2:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var map={engines:['Concept Sedan','Concept SUV','Concept Coupe','Concept Pickup'],electric:['Concept EV','Concept Hybrid'],maintenance:['Service Procedure'],diagnostics:['Diagnostic Case'],safety:['Safety System']};
  var pool=(map[cat]&&map[cat].length)?map[cat]:ARCH.map(function(x){return x[0];});
  var name=pick(pool,rnd);
  var tag='AU-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var spec={},calc=null,diag=null,maint=null,saf=null,desc='';
  function C(formula,inputs,unit){return {formula:formula,inputs:inputs,result:sfig(FORMULAS[formula](inputs)),unit:unit};}
  if(name==='Concept EV'||name==='Concept Hybrid'){
    var kwh=rf(rnd,40,120,0),eff=rf(rnd,14,22,1);
    var range=FORMULAS.ev_range({kwh:kwh,kwh_100km:eff});
    calc=C('ev_range',{kwh:kwh,kwh_100km:eff},'km');
    spec={battery_kWh:kwh,consumption_kWh_100km:eff,range_km:num(range,0),drivetrain:name==='Concept EV'?'dual-motor AWD (concept)':'series-parallel hybrid (concept)',charge_port:'CCS/NACS (concept)'};
    desc='Concept '+name.toLowerCase()+' '+tag+': '+kwh+' kWh pack at '+eff+' kWh/100 km → ~'+num(range,0)+' km range. Generated concept: validate with real drive-cycle simulation and thermal modeling.';
  }else if(name==='Diagnostic Case'){
    var codes=[['P0300','Random/multiple cylinder misfire detected'],['P0171','System too lean (bank 1)'],['P0420','Catalyst system efficiency below threshold (bank 1)'],['P0401','EGR insufficient flow'],['P0128','Coolant thermostat below regulating temperature'],['P0442','EVAP small leak detected'],['P0500','Vehicle speed sensor malfunction'],['P0700','Transmission control system malfunction']];
    var cd=pick(codes,rnd);
    diag={code:cd[0],meaning:cd[1],likely_causes:['worn component in the affected circuit','wiring/connector fault','sensor drift'],first_checks:['scan freeze-frame data','visual inspection','targeted component test']};
    spec={code:cd[0],meaning:cd[1],severity:pick(['low','moderate','high'],rnd)};
    desc='Generated diagnostic case '+tag+': '+cd[0]+' — '+cd[1]+'. Study case: always confirm with freeze-frame data and pinpoint tests; this generated case is for training, not a real vehicle fault.';
    calc={formula:'braking_dist',inputs:{v_ms:27.8,mu:0.7},result:num(FORMULAS.braking_dist({v_ms:27.8,mu:0.7}),1),unit:'m at 100 km/h'};
  }else if(name==='Service Procedure'){
    var item=pick([['Engine oil + filter','5W-30 synthetic'],['Brake pads (axle set)','ceramic'],['Cabin air filter','particulate'],['Spark plugs (set)','iridium'],['Coolant exchange','OAT 50/50'],['Transmission fluid','ATF synthetic']],rnd);
    var interval=ri(rnd,1,6)*10000;
    maint={item:item[0],spec:item[1],interval_km:interval,torque_note:'torque fasteners to spec; road-test after'};
    spec={service:item[0],spec:item[1],interval_km:interval};
    desc='Generated service procedure '+tag+': '+item[0]+' ('+item[1]+') every '+interval.toLocaleString()+' km or per the real owner manual. Generated template: always follow the actual vehicle service manual for torques and procedures.';
    calc={formula:'fuel_L100',inputs:{liters:50,km:650},result:num(FORMULAS.fuel_L100({liters:50,km:650}),2),unit:'L/100km example'};
  }else if(name==='Safety System'){
    var sys=pick([['Automatic emergency braking','radar+camera fusion'],['Lane-keeping assist','camera'],['Blind-spot monitoring','radar'],['Adaptive cruise','radar'],['Rear cross-traffic alert','radar'],['Driver attention monitor','camera']],rnd);
    saf={system:sys[0],sensing:sys[1],note:'driver remains responsible; systems assist, not replace'};
    spec={system:sys[0],sensing:sys[1],status:'concept evaluation'};
    desc='Generated safety-system study '+tag+': '+sys[0]+' using '+sys[1]+'. Generated concept: real validation needs track testing to regulatory protocols (e.g., Euro NCAP scenarios).';
    calc={formula:'stopping',inputs:{v_ms:27.8,mu:0.7},result:num(FORMULAS.stopping({v_ms:27.8,mu:0.7}),1),unit:'m at 100 km/h with reaction'};
  }else{
    var hp=ri(rnd,120,700),rpm=ri(rnd,4000,7500),disp=rf(rnd,1.5,6.5,1);
    var kw=FORMULAS.power_kw({hp:hp}),tq=FORMULAS.torque_nm({hp:hp,rpm:rpm});
    calc=C('torque_nm',{hp:hp,rpm:rpm},'Nm');
    spec={power_hp:hp,power_kW:num(kw,1),torque_Nm:num(tq,0),at_rpm:rpm,displacement_L:disp,engine:'concept ICE',transmission:pick(['6MT','8AT','CVT','DCT'],rnd),drivetrain:pick(['FWD','RWD','AWD'],rnd)};
    desc='Concept '+name.toLowerCase()+' '+tag+': '+disp+' L engine making '+hp+' hp ('+num(kw,1)+' kW), '+num(tq,0)+' Nm at '+rpm+' rpm. Generated concept: emissions, crash, and durability programs gate any real vehicle.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,auto_id:id,title:name+' '+tag+' — Concept Record',category:cat,record_type:'concept-design',
    vehicle_or_system:name+' '+tag,specifications:spec,diagnostics:diag,maintenance:maint,safety:saf,
    calculations:calc,description:desc,source:'signature',
    source_ref:{authority:'JAH Databases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',design_status:'conceptual — generated concept, not a real vehicle; do not use for actual service or diagnosis',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-AUTO-\d{7}$/.test(r.id||''))e.push('id');
  if(r.auto_id!==r.id)e.push('auto_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.vehicle_or_system!=='string'||!r.vehicle_or_system.length)e.push('vehicle_or_system');
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
var gen={version:'jahdb-automotive-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automotive',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
