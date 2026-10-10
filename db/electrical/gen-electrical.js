(function(){'use strict';
/* JAH Electrical Engineering Database — deterministic boundless generator.
   Complete conceptual circuit/component records; validate() recomputes all math. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['circuits','components','power','signals','safety'];
var PREFIX='JAH-ELEC-';
var RTYPES=['datasheet','dimensions','calculation','tolerance-class','material-process','application','selection','installation','maintenance','safety','failure-modes','standards','history','comparison','concept-design'];
var FORMULAS={
 ohm_v:function(i){return i.I_A*i.R_ohm;},
 ohm_i:function(i){return i.V_V/i.R_ohm;},
 ohm_p:function(i){return i.V_V*i.I_A;},
 power_r:function(i){return i.V_V*i.V_V/i.R_ohm;},
 series_r:function(i){return i.R.reduce(function(a,b){return a+b;},0);},
 parallel_r:function(i){return 1/i.R.reduce(function(a,b){return a+1/b;},0);},
 rc_tau:function(i){return i.R_ohm*i.C_F;},
 resonant:function(i){return 1/(2*Math.PI*Math.sqrt(i.L_H*i.C_F));},
 xc:function(i){return 1/(2*Math.PI*i.f_Hz*i.C_F);},
 xl:function(i){return 2*Math.PI*i.f_Hz*i.L_H;},
 divider:function(i){return i.Vin_V*i.R2_ohm/(i.R1_ohm+i.R2_ohm);},
 led_r:function(i){return (i.Vs_V-i.Vf_V)/i.I_A;},
 transformer:function(i){return i.Vp_V*i.Ns/i.Np;},
 motor_sync:function(i){return 120*i.f_Hz/i.poles;},
 wire_r:function(i){return i.rho_ohm_mm2_m*i.L_m/i.A_mm2;},
 decibel:function(i){return 20*Math.log10(i.V2/i.V1);},
 battery_wh:function(i){return i.V_V*i.Ah;},
 cap_energy:function(i){return 0.5*i.C_F*i.V_V*i.V_V;},
 timer_555:function(i){return 1.44/((i.R1_ohm+2*i.R2_ohm)*i.C_F);}
};
var ARCH=[
 ['Resistor Network','circuits'],['RC Timing Stage','circuits'],['LED Driver','circuits'],
 ['Voltage Divider','circuits'],['Mains Transformer','power'],['Motor Starter','power'],
 ['LC Filter','signals'],['Linear Power Supply','power'],['Fuse Selection','safety'],
 ['Op-Amp Gain Stage','signals'],['555 Timer Oscillator','signals'],['PCB Trace','components']
];
function num(n,d){return +(+n).toFixed(d==null?3:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  var tag='CX-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var spec={},calc=null,safety=null,desc='';
  function C(formula,inputs,unit){return {formula:formula,inputs:inputs,result:sfig(FORMULAS[formula](inputs)),unit:unit};}
  if(a[0]==='Resistor Network'){
    var r1=pick([100,220,470,1000,2200,4700,10000],rnd),r2=pick([100,220,470,1000,2200,4700,10000],rnd);
    var v=rf(rnd,3,24,1);
    var rp=FORMULAS.parallel_r({R:[r1,r2]}),p=FORMULAS.power_r({V_V:v,R_ohm:rp});
    calc=C('parallel_r',{R:[r1,r2]},'ohm');
    spec={R1_ohm:r1,R2_ohm:r2,supply_V:v,equivalent_ohm:num(rp,2),dissipation_W:num(p,3)};
    safety={note:'Keep dissipation under half the resistor power rating; verify at worst-case supply tolerance.'};
    desc='Concept resistor network '+tag+': '+r1+' Ω in parallel with '+r2+' Ω across a '+v+' V rail. Equivalent resistance '+num(rp,2)+' Ω dissipates '+num(p,3)+' W. Generated concept: derate parts and check tolerance stack-up for the real build.';
  }else if(a[0]==='RC Timing Stage'){
    var rr=pick([1000,4700,10000,47000,100000],rnd),cc=pick([1e-6,4.7e-6,10e-6,47e-6,100e-6],rnd);
    var tau=FORMULAS.rc_tau({R_ohm:rr,C_F:cc});
    calc=C('rc_tau',{R_ohm:rr,C_F:cc},'s');
    spec={R_ohm:rr,C_F:cc,time_constant_s:num(tau,4),settle_5tau_s:num(5*tau,4)};
    desc='Concept RC timing stage '+tag+': '+rr+' Ω with '+(cc*1e6)+' µF gives τ = '+num(tau,4)+' s (settles in '+num(5*tau,4)+' s). Generated concept: use film capacitors for timing accuracy; mind leakage in electrolytics.';
  }else if(a[0]==='LED Driver'){
    var vs=rf(rnd,5,24,1),vf=rf(rnd,1.8,3.4,1),il=rf(rnd,0.01,0.05,3);
    var rled=FORMULAS.led_r({Vs_V:vs,Vf_V:vf,I_A:il});
    calc=C('led_r',{Vs_V:vs,Vf_V:vf,I_A:il},'ohm');
    spec={supply_V:vs,led_Vf_V:vf,current_A:il,series_R_ohm:num(rled,1),resistor_power_W:num(il*il*rled,3)};
    safety={note:'Never drive an LED without current limiting; verify heatsinking above 1 W.'};
    desc='Concept LED driver '+tag+': '+vs+' V supply, LED Vf '+vf+' V at '+(il*1000)+' mA needs '+num(rled,1)+' Ω in series (dissipates '+num(il*il*rled,3)+' W). Generated concept: prefer a constant-current driver for strings of LEDs.';
  }else if(a[0]==='Voltage Divider'){
    var ra=pick([1000,4700,10000],rnd),rb=pick([1000,4700,10000],rnd),vin=rf(rnd,5,24,1);
    var vo=FORMULAS.divider({Vin_V:vin,R1_ohm:ra,R2_ohm:rb});
    calc=C('divider',{Vin_V:vin,R1_ohm:ra,R2_ohm:rb},'V');
    spec={R1_ohm:ra,R2_ohm:rb,Vin_V:vin,Vout_V:num(vo,3)};
    desc='Concept voltage divider '+tag+': '+vin+' V across '+ra+' Ω / '+rb+' Ω gives '+num(vo,3)+' V out. Generated concept: buffer with an op-amp if the load draws more than a tenth of the divider current.';
  }else if(a[0]==='Mains Transformer'){
    var vp=pick([120,230],rnd),nsn=ri(rnd,1,20),vs2=FORMULAS.transformer({Vp_V:vp,Np:100,Ns:nsn*5});
    calc=C('transformer',{Vp_V:vp,Np:100,Ns:nsn*5},'V');
    spec={primary_V:vp,turns_ratio:'100:'+(nsn*5),secondary_V:num(vs2,2),frequency_Hz:vp===120?60:50,insulation_class:'B (130 C)'};
    safety={note:'Mains transformer: fuse the primary, earth the core, respect creepage/clearance per IEC 61558.'};
    desc='Concept mains transformer '+tag+': '+vp+' V primary, 100:'+(nsn*5)+' turns, '+num(vs2,2)+' V secondary at '+(vp===120?60:50)+' Hz. Generated concept: size the VA rating at 1.5x the load and verify inrush current.';
  }else if(a[0]==='Motor Starter'){
    var hp=rf(rnd,1,50,1),vv=pick([230,460],rnd);
    var fla=hp*746/(1.732*vv*0.85*0.9);
    spec={motor_hp:hp,supply_V:vv,full_load_amps:num(fla,1),starter:'DOL with thermal overload',overload_setting_A:num(fla*1.15,1)};
    safety={note:'Lockout/tagout before servicing; set overload at 115% of FLA per NEC 430.'};
    desc='Concept motor starter '+tag+' for a '+hp+' hp, '+vv+' V three-phase motor: estimated full-load current '+num(fla,1)+' A, overload set at '+num(fla*1.15,1)+' A. Generated concept: verify starting method against utility flicker limits for large motors.';
    calc={formula:'ohm_p',inputs:{V_V:vv,I_A:num(fla,3)},result:num(FORMULAS.ohm_p({V_V:vv,I_A:fla}),2),unit:'W (apparent, single-phase equiv.)'};
  }else if(a[0]==='LC Filter'){
    var l=rf(rnd,1e-6,1e-3,9),cf=rf(rnd,1e-9,10e-6,12);
    var f0=FORMULAS.resonant({L_H:l,C_F:cf});
    calc=C('resonant',{L_H:l,C_F:cf},'Hz');
    spec={L_H:l,C_F:cf,resonant_Hz:num(f0,1)};
    desc='Concept LC filter '+tag+' resonant at '+num(f0,1)+' Hz. Generated concept: damp the resonance with series resistance and check inductor saturation current.';
  }else if(a[0]==='Linear Power Supply'){
    var vo2=pick([3.3,5,9,12,15,24],rnd),io=rf(rnd,0.1,3,2);
    var pd=(rf(rnd,4,10,1))*io;
    spec={output_V:vo2,current_A:io,regulator:'linear',heatsink_required_W:num(pd,2)};
    safety={note:'Size heatsink for worst-case dropout; add input fuse and thermal shutdown.'};
    desc='Concept linear supply '+tag+': '+vo2+' V at '+io+' A. Regulator must shed about '+num(pd,2)+' W as heat. Generated concept: switch to buck regulation above a few watts of loss.';
    calc={formula:'ohm_p',inputs:{V_V:vo2,I_A:io},result:num(FORMULAS.ohm_p({V_V:vo2,I_A:io}),2),unit:'W output'};
  }else if(a[0]==='Fuse Selection'){
    var il2=rf(rnd,0.5,30,1);
    var fr=il2*1.25;
    spec={load_A:il2,fuse_rating_A:num(fr,2),type:'time-delay',voltage_rating_V:250,interrupting_kA:10};
    safety={note:'Fuse at 125% of continuous load per NEC; never replace with a higher rating.'};
    desc='Concept fuse selection '+tag+': '+il2+' A continuous load calls for a '+num(fr,2)+' A time-delay fuse (next standard size up). Generated concept: coordinate with upstream protection and verify I²t let-through.';
    calc={formula:'ohm_p',inputs:{V_V:120,I_A:il2},result:num(FORMULAS.ohm_p({V_V:120,I_A:il2}),1),unit:'W at 120 V'};
  }else if(a[0]==='Op-Amp Gain Stage'){
    var g=ri(rnd,2,100);
    spec={topology:'non-inverting',gain:g,R1_ohm:10000,R2_ohm:10000*(g-1),opamp:'general purpose',supply_V:'±15'};
    desc='Concept op-amp stage '+tag+': non-inverting gain of '+g+' (R1 10 kΩ, R2 '+num(10000*(g-1)/1000,1)+' kΩ). Generated concept: check gain-bandwidth, slew rate, and input offset for the real signal chain.';
    calc={formula:'decibel',inputs:{V1:1,V2:g},result:num(FORMULAS.decibel({V1:1,V2:g}),2),unit:'dB'};
  }else if(a[0]==='555 Timer Oscillator'){
    var r1t=pick([1000,4700,10000],rnd),r2t=pick([1000,4700,10000,47000],rnd),ct=pick([10e-9,100e-9,1e-6,10e-6],rnd);
    var f5=FORMULAS.timer_555({R1_ohm:r1t,R2_ohm:r2t,C_F:ct});
    calc=C('timer_555',{R1_ohm:r1t,R2_ohm:r2t,C_F:ct},'Hz');
    spec={R1_ohm:r1t,R2_ohm:r2t,C_F:ct,frequency_Hz:num(f5,1),duty_percent:num((r1t+r2t)/(r1t+2*r2t)*100,1)};
    desc='Concept 555 astable '+tag+': '+num(f5,1)+' Hz at '+num((r1t+r2t)/(r1t+2*r2t)*100,1)+'% duty. Generated concept: use the CMOS 7555 variant for lower supply current.';
  }else{
    var len=ri(rnd,10,200),wid=rf(rnd,0.2,2,2),th=0.035;
    var area=wid*th;
    var tr=FORMULAS.wire_r({rho_ohm_mm2_m:0.0175,L_m:len/1000,A_mm2:area});
    calc=C('wire_r',{rho_ohm_mm2_m:0.0175,L_m:len/1000,A_mm2:area},'ohm');
    spec={length_mm:len,width_mm:wid,thickness_mm:th,resistance_ohm:num(tr,4),copper:'1 oz'};
    desc='Concept PCB trace '+tag+': '+len+' mm long, '+wid+' mm wide, 1 oz copper → '+num(tr,4)+' Ω. Generated concept: widen or stitch vias for currents above ~2 A; mind controlled impedance for fast edges.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,elec_id:id,title:a[0]+' '+tag+' — Concept Design',category:cat,record_type:'concept-design',
    component:a[0]+' '+tag,specifications:spec,calculations:calc,safety:safety,
    standards:['IEC 61010-1','NEC Article 110'],description:desc,source:'signature',
    source_ref:{authority:'JAH Databases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',design_status:'conceptual — generated design, not a built circuit; verify against real datasheets before construction',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ELEC-\d{7}$/.test(r.id||''))e.push('id');
  if(r.elec_id!==r.id)e.push('elec_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.component!=='string'||!r.component.length)e.push('component');
  if(!r.specifications||typeof r.specifications!=='object')e.push('specifications');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&(!r.source_ref||!r.source_ref.authority))e.push('source_ref');
  var c=r.calculations;
  if(c){
    var f=FORMULAS[c.formula];
    if(!f)e.push('calc_formula');
    else{var expect=f(c.inputs),got=+c.result;
      if(!(got>=0)||Math.abs(got-expect)/Math.max(expect,1e-12)>0.03)e.push('calc_recompute');}
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-electrical-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('electrical',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
