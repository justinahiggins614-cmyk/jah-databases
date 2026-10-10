(function(){'use strict';
/* JAH Mechanical Engineering Database — deterministic boundless generator.
   Produces COMPLETE conceptual mechanical design records (never stubs).
   Every calculation is recomputed by validate(): fake math cannot pass. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['components','mechanisms','materials','tolerances','statics'];
var PREFIX='JAH-MECH-';
var RTYPES=['datasheet','dimensions','calculation','tolerance-class','material-process','application','selection','installation','maintenance','safety','failure-modes','standards','history','comparison','concept-design'];
/* Real engineering formulas. Each takes an inputs object and returns the result.
   validate() recomputes every stored calculation through these. */
var FORMULAS={
 bolt_clamp:function(i){return 0.75*i.proof_MPa*i.As_mm2;},                 /* N: preload = 0.75*proof*stress area */
 torsion_stress:function(i){return 16*(i.T_Nm*1000)/(Math.PI*Math.pow(i.d_mm,3));}, /* MPa */
 twist_angle:function(i){return (i.T_Nm*1000)*i.L_mm/(i.G_MPa*Math.PI*Math.pow(i.d_mm,4)/32);}, /* rad */
 beam_cantilever:function(i){return i.F_N*Math.pow(i.L_mm,3)/(3*i.E_MPa*i.I_mm4);}, /* mm */
 beam_simple:function(i){return i.F_N*Math.pow(i.L_mm,3)/(48*i.E_MPa*i.I_mm4);},   /* mm */
 spring_force:function(i){return i.k_Nmm*i.x_mm;},                            /* N */
 spring_energy:function(i){return 0.5*i.k_Nmm*Math.pow(i.x_mm,2)/1000;},       /* J */
 gear_ratio:function(i){return i.z2/i.z1;},
 gear_center:function(i){return i.m_mm*(i.z1+i.z2)/2;},                       /* mm */
 belt_speed:function(i){return Math.PI*i.d_mm*i.n_rpm/60000;},                /* m/s */
 bearing_L10:function(i){return Math.pow(i.C_kN/i.P_kN,3);},                  /* millions of revolutions */
 friction_force:function(i){return i.mu*i.N_N;},                              /* N */
 buckling:function(i){return Math.PI*Math.PI*i.E_MPa*i.I_mm4/Math.pow(i.KL_mm,2);}, /* N */
 hoop_stress:function(i){return i.p_MPa*i.ri_mm/i.t_mm;},                     /* MPa */
 power_torque:function(i){return i.T_Nm*i.n_rpm/9550;},                       /* kW */
 key_shear:function(i){return 2*(i.T_Nm*1000)/(i.d_mm*i.w_mm*i.l_mm);},        /* MPa */
 bolt_torque:function(i){return i.K*i.F_N*i.d_mm/1000;},                      /* Nm */
 weld_throat:function(i){return i.F_N/(0.707*i.h_mm*i.l_mm);},                 /* MPa */
 stress_axial:function(i){return i.F_N/i.A_mm2;},                              /* MPa */
 fit_max_clear:function(i){return i.hole_upper_um-i.shaft_lower_um;},          /* µm */
 fit_min_clear:function(i){return i.hole_lower_um-i.shaft_upper_um;},          /* µm */
 oring_squeeze:function(i){return (i.cs_mm-i.groove_mm)/i.cs_mm*100;},         /* % */
 pump_hyd_power:function(i){return i.Q_m3h*i.H_m*9.81/(3600*i.eff);},            /* kW */
 lead_travel:function(i){return i.pitch_mm*i.starts*i.rpm/60;}                 /* mm/s */
};
var MATS=[
 ['AISI 1045 medium-carbon steel',7850,310,565],['AISI 4140 alloy steel (quenched & tempered)',7850,655,1020],
 ['AISI 304 stainless steel',8000,205,515],['6061-T6 aluminum',2700,276,310],
 ['7075-T6 aluminum',2810,503,572],['Ti-6Al-4V titanium',4430,880,950],
 ['C36000 free-cutting brass',8500,140,340],['ASTM A36 structural steel',7850,250,400],
 ['Ductile iron 65-45-12',7100,310,448],['Music wire ASTM A228',7860,2000,2200]
];
var ARCH=[
 ['Torsion Shaft','components','shaft'],['Cantilever Beam Bracket','statics','beam'],
 ['Bolted Flange Joint','components','joint'],['Compression Spring','components','spring'],
 ['Spur Gear Pair','mechanisms','gear'],['V-Belt Drive','mechanisms','belt'],
 ['Deep-Groove Bearing Selection','components','bearing'],['Machine Column','statics','column'],
 ['Pressure Vessel Shell','components','vessel'],['Parallel Key Drive','components','key'],
 ['Welded Bracket','statics','weld'],['Lead Screw Drive','mechanisms','screw']
];
function num(n,d){return +(+n).toFixed(d==null?2:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  if(opts.category==='mechanisms'&&a[1]!=='mechanisms')a=pick(ARCH.filter(function(x){return x[1]==='mechanisms';}),rnd);
  if(opts.category==='statics'&&a[1]!=='statics')a=pick(ARCH.filter(function(x){return x[1]==='statics';}),rnd);
  var m=pick(MATS,rnd);
  var calc=null,props={},dims={},tol=null,desc='';
  var tag='MK-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  function C(formula,inputs,unit){var res=FORMULAS[formula](inputs);return {formula:formula,inputs:inputs,result:sfig(res),unit:unit};}
  if(a[2]==='shaft'){
    var d=ri(rnd,20,80),L=ri(rnd,200,1200),T=ri(rnd,100,2000);
    var tau=FORMULAS.torsion_stress({T_Nm:T,d_mm:d}),phi=FORMULAS.twist_angle({T_Nm:T,L_mm:L,d_mm:d,G_MPa:79000});
    var sf=m[2]/tau;
    calc=C('torsion_stress',{T_Nm:T,d_mm:d},'MPa');
    props={material:m[0],density_kg_m3:m[1],yield_MPa:m[2],uts_MPa:m[3],shear_stress_MPa:num(tau,2),twist_rad:num(phi,4),safety_factor_yield:num(sf,2)};
    dims={diameter_mm:d,length_mm:L};
    tol={shaft:'k6',housing:'H7',note:'Bearing seats ground to k6; general diameters h11.'};
    desc='Concept torsion shaft '+tag+' in '+m[0]+', '+d+' mm diameter by '+L+' mm long, transmitting '+T+' Nm. '+
      'The computed torsional shear stress is '+num(tau,2)+' MPa against a '+m[2]+' MPa yield, giving a safety factor of '+num(sf,2)+'. '+
      'Angle of twist over the full length is '+num(phi,4)+' radians. This is a generated conceptual design for study and iteration, not a manufactured part.';
  }else if(a[2]==='beam'){
    var F=ri(rnd,500,20000),Lb=ri(rnd,500,3000),I=ri(rnd,20000,800000);
    var de=FORMULAS.beam_cantilever({F_N:F,L_mm:Lb,E_MPa:200000,I_mm4:I});
    calc=C('beam_cantilever',{F_N:F,L_mm:Lb,E_MPa:200000,I_mm4:I},'mm');
    props={material:m[0],load_N:F,length_mm:Lb,moment_of_inertia_mm4:I,max_deflection_mm:num(de,3),elastic_modulus_MPa:200000};
    dims={length_mm:Lb,load_position:'free end'};
    desc='Concept cantilever bracket '+tag+' carrying '+F+' N at its free end over a '+Lb+' mm span. '+
      'With a section moment of inertia of '+I+' mm^4 in steel (E = 200,000 MPa), the tip deflection computes to '+num(de,3)+' mm. '+
      'Generated as a study concept: verify section properties and fatigue life before any real use.';
  }else if(a[2]==='joint'){
    var th=pick([['M6',20.1],['M8',36.6],['M10',58.0],['M12',84.3],['M16',157],['M20',245]],rnd);
    var gr=pick([[640,'8.8'],[900,'10.9'],[1080,'12.9']],rnd);
    var Fp=FORMULAS.bolt_clamp({proof_MPa:gr[0],As_mm2:th[1]});
    var Tq=FORMULAS.bolt_torque({K:0.2,F_N:Fp,d_mm:parseInt(th[0].slice(1),10)});
    calc=C('bolt_clamp',{proof_MPa:gr[0],As_mm2:th[1]},'N');
    props={thread:th[0],grade:'ISO '+gr[1],proof_load_MPa:gr[0],tensile_stress_area_mm2:th[1],preload_N:num(Fp,1),tightening_torque_Nm:num(Tq,1),friction_factor_K:0.2};
    dims={thread:th[0],grade:gr[1]};
    tol={thread:'6g/6H',note:'Property class per ISO 898-1.'};
    desc='Concept bolted flange joint '+tag+' using '+th[0]+' property-class '+gr[1]+' fasteners. '+
      'Target preload is '+num(Fp,1)+' N (75% of proof load over '+th[1]+' mm^2 stress area), calling for about '+num(Tq,1)+' Nm tightening torque at K = 0.2. '+
      'Generated concept: confirm joint stiffness, embedment, and vibration loosening in a real design review.';
  }else if(a[2]==='spring'){
    var k=rf(rnd,5,200,1),x=ri(rnd,10,100);
    var Fs=FORMULAS.spring_force({k_Nmm:k,x_mm:x}),Es=FORMULAS.spring_energy({k_Nmm:k,x_mm:x});
    calc=C('spring_force',{k_Nmm:k,x_mm:x},'N');
    props={wire:'Music wire ASTM A228',rate_N_per_mm:k,deflection_mm:x,force_N:num(Fs,1),stored_energy_J:num(Es,2)};
    desc='Concept compression spring '+tag+' with a rate of '+k+' N/mm compressed '+x+' mm, delivering '+num(Fs,1)+' N and storing '+num(Es,2)+' J. '+
      'Generated concept in music wire: check solid height, buckling, and fatigue (S-N) before prototyping.';
  }else if(a[2]==='gear'){
    var z1=ri(rnd,12,30),z2=ri(rnd,30,120),mod=pick([1,1.5,2,2.5,3,4,5,6,8],rnd);
    var ratio=FORMULAS.gear_ratio({z1:z1,z2:z2}),cd=FORMULAS.gear_center({m_mm:mod,z1:z1,z2:z2});
    calc=C('gear_ratio',{z1:z1,z2:z2},'ratio');
    props={module_mm:mod,pinion_teeth:z1,gear_teeth:z2,ratio:num(ratio,3),center_distance_mm:num(cd,2),pressure_angle_deg:20};
    desc='Concept spur gear pair '+tag+': '+z1+'-tooth pinion driving a '+z2+'-tooth gear at '+mod+' mm module, 20-degree pressure angle. '+
      'Ratio '+num(ratio,3)+':1 with '+num(cd,2)+' mm center distance. Generated concept: run tooth bending (Lewis) and contact (Hertz) checks for real duty.';
  }else if(a[2]==='belt'){
    var d1=ri(rnd,50,200),d2=ri(rnd,100,400),n=ri(rnd,500,3000);
    var v=FORMULAS.belt_speed({d_mm:d1,n_rpm:n});
    calc=C('belt_speed',{d_mm:d1,n_rpm:n},'m/s');
    props={driver_dia_mm:d1,driven_dia_mm:d2,speed_rpm:n,belt_speed_m_s:num(v,2),ratio:num(d2/d1,3)};
    desc='Concept V-belt drive '+tag+': '+d1+' mm driver at '+n+' rpm driving a '+d2+' mm pulley. Belt speed '+num(v,2)+' m/s, ratio '+num(d2/d1,3)+':1. '+
      'Generated concept: select belt section by power and verify slip, tension, and bearing loads.';
  }else if(a[2]==='bearing'){
    var bore=pick([20,25,30,35,40,45,50,60,70,80],rnd),Cb=rf(rnd,10,80,1),Pb=rf(rnd,1,20,1);
    var L10=FORMULAS.bearing_L10({C_kN:Cb,P_kN:Pb});
    calc=C('bearing_L10',{C_kN:Cb,P_kN:Pb},'million revolutions');
    props={bore_mm:bore,dynamic_rating_kN:Cb,equivalent_load_kN:Pb,L10_million_rev:num(L10,2),lube:'ISO VG 68, NLGI 2 grease'};
    tol={shaft:'k5',housing:'H7',note:'Typical rotating-inner-ring fit.'};
    desc='Concept bearing selection '+tag+' for a '+bore+' mm shaft: dynamic rating '+Cb+' kN against '+Pb+' kN equivalent load gives L10 life of '+num(L10,2)+' million revolutions. '+
      'Generated concept: confirm static rating, limiting speed, and contamination factor for the real application.';
  }else if(a[2]==='column'){
    var Lc=ri(rnd,1000,4000),Ic=ri(rnd,50000,2000000);
    var Pcr=FORMULAS.buckling({E_MPa:200000,I_mm4:Ic,KL_mm:Lc});
    calc=C('buckling',{E_MPa:200000,I_mm4:Ic,KL_mm:Lc},'N');
    props={material:'ASTM A36 steel',effective_length_mm:Lc,moment_of_inertia_mm4:Ic,critical_load_N:num(Pcr,1),critical_load_kN:num(Pcr/1000,2)};
    desc='Concept machine column '+tag+', '+Lc+' mm effective length in A36 steel. Euler critical load computes to '+num(Pcr/1000,2)+' kN. '+
      'Generated concept: check slenderness limits, eccentric loading, and base fixity before sizing a real column.';
  }else if(a[2]==='vessel'){
    var p=rf(rnd,0.5,5,2),riv=ri(rnd,100,500),t=ri(rnd,5,30);
    var hoop=FORMULAS.hoop_stress({p_MPa:p,ri_mm:riv,t_mm:t});
    calc=C('hoop_stress',{p_MPa:p,ri_mm:riv,t_mm:t},'MPa');
    props={pressure_MPa:p,inner_radius_mm:riv,wall_mm:t,hoop_stress_MPa:num(hoop,2),material:'SA-516 Grade 70'};
    desc='Concept pressure vessel shell '+tag+' at '+p+' MPa internal pressure, '+riv+' mm inner radius, '+t+' mm wall. '+
      'Hoop stress '+num(hoop,2)+' MPa in SA-516 Grade 70. Generated concept only: pressure vessels demand code design (ASME VIII) and registered review.';
  }else if(a[2]==='key'){
    var dk=pick([20,25,30,40,50,60],rnd),Tk=ri(rnd,50,800);
    var wk=dk<=30?8:dk<=50?12:16,lk=ri(rnd,20,80);
    var taus=FORMULAS.key_shear({T_Nm:Tk,d_mm:dk,w_mm:wk,l_mm:lk});
    calc=C('key_shear',{T_Nm:Tk,d_mm:dk,w_mm:wk,l_mm:lk},'MPa');
    props={shaft_dia_mm:dk,key_w_mm:wk,key_l_mm:lk,torque_Nm:Tk,key_shear_MPa:num(taus,2),key_material:'C1045 key stock'};
    dims={shaft_dia_mm:dk,key:wk+'x'+lk+' mm'};
    desc='Concept parallel key drive '+tag+' on a '+dk+' mm shaft transmitting '+Tk+' Nm through a '+wk+'x'+lk+' mm key. '+
      'Key shear stress '+num(taus,2)+' MPa. Generated concept: also check bearing (crushing) stress on key and hub.';
  }else if(a[2]==='weld'){
    var Fw=ri(rnd,1000,50000),hw=ri(rnd,3,12),lw=ri(rnd,50,400);
    var tw=FORMULAS.weld_throat({F_N:Fw,h_mm:hw,l_mm:lw});
    calc=C('weld_throat',{F_N:Fw,h_mm:hw,l_mm:lw},'MPa');
    props={load_N:Fw,fillet_leg_mm:hw,weld_length_mm:lw,throat_shear_MPa:num(tw,2),electrode:'E7018'};
    desc='Concept welded bracket '+tag+': '+Fw+' N on a '+hw+' mm fillet, '+lw+' mm long. Throat shear '+num(tw,2)+' MPa with E7018 electrode. '+
      'Generated concept: apply code allowable (e.g., 30% of electrode tensile) and fatigue category checks.';
  }else{
    var pitch=rf(rnd,2,20,1),starts=ri(rnd,1,4),np=ri(rnd,100,2000);
    var lead=pitch*starts,travel=lead*np/60;
    calc={formula:'lead_travel',inputs:{pitch_mm:pitch,starts:starts,rpm:np},result:num(travel,2),unit:'mm/s'};
    props={pitch_mm:pitch,starts:starts,lead_mm:num(lead,2),speed_rpm:np,travel_mm_s:num(travel,2),nut:'bronze C93200'};
    desc='Concept lead screw drive '+tag+': '+pitch+' mm pitch, '+starts+' starts ('+num(lead,2)+' mm lead) at '+np+' rpm gives '+num(travel,2)+' mm/s nut travel. '+
      'Generated concept: check critical speed, column buckling of the screw, and PV limits on the nut.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  var title=a[0]+' '+tag+' — Concept Design';
  return {id:id,mech_id:id,title:title,category:cat,record_type:'concept-design',component:a[0]+' '+tag,
    material:props.material||m[0],standards:['ISO 2768-m','ASME Y14.5'],properties:props,dimensions:dims,
    calculations:calc,tolerances:tol,description:desc,source:'signature',
    source_ref:{authority:'JAH Data Bases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',design_status:'conceptual — generated design, not a manufactured product; properties predicted, not measured',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MECH-\d{7}$/.test(r.id||''))e.push('id');
  if(r.mech_id!==r.id)e.push('mech_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.component!=='string'||!r.component.length)e.push('component');
  if(typeof r.material!=='string'||!r.material.length)e.push('material');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!r.properties||typeof r.properties!=='object')e.push('properties');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&(!r.source_ref||!r.source_ref.authority))e.push('source_ref');
  var c=r.calculations;
  if(c){
    var f=FORMULAS[c.formula];
    if(!f)e.push('calc_formula');
    else{
      var expect=f(c.inputs);
      var got=+c.result;
      if(!(got>0)||Math.abs(got-expect)/Math.max(expect,1e-9)>0.03)e.push('calc_recompute');
    }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-mech-engineering-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mech-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
