(function(){'use strict';
/* JAH Materials Database — deterministic boundless generator.
   Conceptual alloy/composite formulations with predicted (not measured)
   properties. validate() recomputes every derived value. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['metals','polymers','ceramics','composites','properties', 'programmable', 'programmable'];
var PREFIX='JAH-MAT-';
var RTYPES=['datasheet','mechanical','thermal','electrical-prop','corrosion','processing','heat-treatment','joining','machining','applications','selection','sustainability','standards','testing','failure-modes','history','comparison','concept-design','dimensions','calculation','tolerance-class','material-process','application','installation','maintenance','safety'];
/* ---- Characterization/failure-analysis record families (expansion 2026-10-17):
   microscopy, fractography, root-cause failure records. Signature-authored
   analytical records — clearly labeled, not measured lab data. ---- */
var CHARTYPES=['microscopy','fractography','failure-analysis'];
CHARTYPES.forEach(function(t){if(RTYPES.indexOf(t)<0)RTYPES.push(t);});
var CHAR_TECH={
 microscopy:[['optical microscopy','reflected-light examination of etched microstructure'],
  ['scanning electron microscopy','high-resolution surface and cross-section imaging'],
  ['transmission electron microscopy','nanoscale dislocation and precipitate imaging'],
  ['grain-size measurement','ASTM E112 intercept method for average grain size'],
  ['inclusion rating','ASTM E45 sulfide/oxide inclusion assessment'],
  ['phase identification','metallographic phase fraction estimation']],
 fractography:[['dimple rupture analysis','microvoid coalescence from overload'],
  ['cleavage facet mapping','transgranular brittle fracture planes'],
  ['fatigue striation counting','one striation per load cycle on the fracture face'],
  ['intergranular fracture study','grain-boundary separation from embrittlement'],
  ['beach-mark tracing','macroscopic crack-growth front positions'],
  ['shear-lip measurement','ductile final-fracture region sizing']],
 'failure-analysis':[['five-whys analysis','iterative why-questioning to the root cause'],
  ['fault-tree analysis','top-down logic-gate decomposition of the failure'],
  ['FMEA review','failure modes with severity, occurrence, detection ranks'],
  ['fishbone diagram','cause-and-effect categories for the failure event'],
  ['timeline reconstruction','ordered event sequence leading to failure'],
  ['corrective-action plan','containment, root-cause fix, and verification steps']]
};
var CHAR_MATS=['316L stainless steel','6061-T6 aluminum','Ti-6Al-4V','AISI 1045 steel','PEEK','alumina ceramic','Cu-Cr-Zr copper','Inconel 718'];
function buildChar(seed,rnd,rt,cat){
  var id=PREFIX+String(seed).padStart(7,'0');
  var mat=pick(CHAR_MATS,rnd), tech=pick(CHAR_TECH[rt],rnd);
  var tag='CH-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var props,desc,name;
  if(rt==='microscopy'){
    var mag=pick([100,200,500,1000,5000,10000],rnd);
    var gs=rf(rnd,5,120,1);
    props={family:'characterization record',technique:tech[0]+' — '+tech[1],magnification:mag+'x',
      etchant:pick(['nital','Keller\u2019s reagent','Marble\u2019s reagent','electrolytic oxalic'],rnd),
      observed_feature:pick(['equiaxed austenite grains','elongated rolled grains','martensite laths','precipitate dispersion','twin boundaries','dendritic structure'],rnd),
      avg_grain_size_um:gs,specimen_prep:'mounted, ground, polished to 0.05 um, etched'};
    name='Microscopy record '+tag+' ('+mat+')';
    desc='Signature-authored microscopy record: '+tech[0]+' of '+mat+' at '+mag+'x shows '+props.observed_feature+' with an average grain size near '+gs+' um. Analytical record — representative parameters, not a measured laboratory result.';
  }else if(rt==='fractography'){
    var fmode=pick(['ductile overload','fatigue','brittle cleavage','stress-corrosion cracking','hydrogen embrittlement','creep rupture'],rnd);
    props={family:'characterization record',technique:tech[0]+' — '+tech[1],fracture_mode:fmode,
      magnification:pick([50,200,1000,5000],rnd)+'x',
      key_feature:pick(['equiaxed dimples','river patterns','striations','intergranular facets','beach marks','wedge cracks'],rnd),
      crack_origin:pick(['surface defect','inclusion','weld toe','keyway corner','corrosion pit','machining mark'],rnd)};
    name='Fractography record '+tag+' ('+mat+')';
    desc='Signature-authored fractography record: the fracture face of '+mat+' failed by '+fmode+', originating at a '+props.crack_origin+'; '+tech[0]+' reveals '+props.key_feature+'. Analytical record — representative parameters, not a measured laboratory result.';
  }else{
    var fmode2=pick(['fatigue crack growth','overload fracture','wear-out','corrosion perforation','thermal fatigue','fretting'],rnd);
    var cause=pick(['inadequate fillet radius raising stress concentration','missed heat-treatment step','abrasive contamination in the lubricant','design load underestimated by 30%','protective coating damaged in assembly','maintenance interval exceeded'],rnd);
    props={family:'failure-analysis record',technique:tech[0]+' — '+tech[1],component:pick(['drive shaft','pressure vessel','bearing race','welded bracket','turbine blade','fastener'],rnd)+' ('+mat+')',
      failure_mode:fmode2,root_cause:cause,
      contributing_factors:pick(['cyclic loading','elevated temperature','corrosive environment','vibration'],rnd)+'; '+pick(['poor surface finish','residual stress','material substitution'],rnd),
      corrective_action:pick(['redesign fillet and re-qualify by test','restore specified heat treatment and audit','upgrade filtration and oil analysis','revise loads and re-run FEA','repair coating procedure and inspect','shorten interval and monitor'],rnd)};
    name='Root-cause failure record '+tag+' ('+mat+')';
    desc='Signature-authored root-cause failure record: '+props.component+' failed by '+fmode2+'. Root cause: '+cause+'. Corrective action: '+props.corrective_action+'. Analytical record — a structured investigation template, not a real incident report.';
  }
  return {id:id,mat_id:id,title:name+' — Signature characterization',category:cat,record_type:rt,
    material:mat,composition:tech[0],properties:props,
    processing:['characterization workflow — specimen prep, examination, interpretation'],
    applications:['quality investigation','design feedback','failure prevention'],
    standards:['ASTM E3','ASTM E407','ASTM E112'],description:desc,source:'signature',
    source_ref:{authority:'JAH Databases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',data_quality:'predicted-not-measured',
    design_status:'analytical characterization record — Signature-authored, not measured',_seed:seed};
}
var FORMULAS={
 specific_strength:function(i){return i.uts_MPa/i.density_kg_m3*1000;},   /* kN·m/kg */
 specific_stiffness:function(i){return i.E_MPa/i.density_kg_m3*1000;},
 weight_plate:function(i){return i.density_kg_m3*i.L_m*i.W_m*i.t_mm/1000/1000;}, /* kg: t mm -> m */
 thermal_stress:function(i){return i.E_MPa*i.alpha_1e6*1e-6*i.dT_K;},      /* MPa */
 rule_of_mixtures:function(i){return i.Ef_MPa*i.Vf+i.Em_MPa*(1-i.Vf);},    /* MPa */
 hv_to_mpa:function(i){return i.HV*9.807;},
 resistivity_r:function(i){return i.rho_ohm_m*i.L_m/i.A_m2;}
};
var BASE=[
 ['Fe','iron base',7870],['Al','aluminum base',2700],['Cu','copper base',8960],
 ['Ti','titanium base',4430],['Ni','nickel base',8900],['Mg','magnesium base',1740]
];
var ALLOYANTS=['Cr','Ni','Mo','Mn','Si','V','W','Co','Nb','C','N','B','Zr','Y'];
var POLY=[['PA66-GF30','polyamide 66, 30% glass',1370,185],['PPS-GF40','polyphenylene sulfide, 40% glass',1440,195],
 ['PEEK-CF30','polyetheretherketone, 30% carbon',1440,210],['POM-C','acetal copolymer',1410,68],
 ['PTFE','polytetrafluoroethylene',2200,25],['UHMWPE','ultra-high-molecular-weight polyethylene',940,40]];
function num(n,d){return +(+n).toFixed(d==null?2:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(opts.record_type&&CHARTYPES.indexOf(opts.record_type)>=0)
    return buildChar(seed,rnd,opts.record_type,opts.category||pick(CATS,rnd));
  var cat=opts.category||pick(CATS,rnd);
  var tag='MX-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var kind=cat==='metals'?0:cat==='polymers'?1:cat==='composites'?1:ri(rnd,0,2),name,props={},calc=null,desc='';
  function C(formula,inputs,unit){return {formula:formula,inputs:inputs,result:sfig(FORMULAS[formula](inputs)),unit:unit};}
  if(kind===0){
    var b=pick(BASE,rnd),a1=pick(ALLOYANTS,rnd),a2=pick(ALLOYANTS,rnd);
    var p1=rf(rnd,0.2,12,2),p2=rf(rnd,0.1,4,2);
    var dens=num(b[2]*(1-p1/100*0.05),0);
    var uts=ri(rnd,300,1800),E=ri(rnd,70000,220000),hv=ri(rnd,120,600);
    var ss=FORMULAS.specific_strength({uts_MPa:uts,density_kg_m3:dens});
    calc=C('specific_strength',{uts_MPa:uts,density_kg_m3:dens},'kN·m/kg');
    name=b[1]+' concept alloy '+tag+' ('+a1+' '+p1+'%, '+a2+' '+p2+'%)';
    props={family:'conceptual alloy',base:b[0],alloyants:a1+' '+p1+' wt%, '+a2+' '+p2+' wt%',
      density_kg_m3:dens,uts_MPa:uts,yield_MPa:num(uts*0.72,0),elastic_modulus_MPa:E,
      hardness_HV:hv,specific_strength:num(ss,1),melting_C:ri(rnd,600,1700)};
    desc='Concept alloy '+tag+' on a '+b[1]+' with '+a1+' '+p1+'% and '+a2+' '+p2+'%. Predicted UTS '+uts+' MPa at '+dens+' kg/m³ gives specific strength '+num(ss,1)+' kN·m/kg. Predicted — not measured; real qualification needs melt trials and ASTM E8 testing.';
  }else if(kind===1){
    var p=pick(POLY,rnd);
    var vf=rf(rnd,0.1,0.5,2),Ef=ri(rnd,200000,400000),Em=ri(rnd,2000,5000);
    var Ec=FORMULAS.rule_of_mixtures({Ef_MPa:Ef,Vf:vf,Em_MPa:Em});
    calc=C('rule_of_mixtures',{Ef_MPa:Ef,Vf:vf,Em_MPa:Em},'MPa');
    name='Concept composite '+tag+' ('+p[0]+' family)';
    props={family:'conceptual composite',matrix:p[0]+' — '+p[1],fiber_volume_fraction:vf,
      fiber_modulus_MPa:Ef,matrix_modulus_MPa:Em,predicted_modulus_MPa:num(Ec,0),
      density_kg_m3:p[2],matrix_strength_MPa:p[3]};
    desc='Concept composite '+tag+' in the '+p[0]+' family at '+num(vf*100,0)+'% fiber volume. Rule of mixtures predicts a modulus of '+num(Ec,0)+' MPa. Predicted — not measured; validate with coupon tests before structural use.';
  }else{
    var el=pick(ALLOYANTS,rnd);
    var dT=ri(rnd,50,400),EE=ri(rnd,70000,220000),al=rf(rnd,5,25,1);
    var ts=FORMULAS.thermal_stress({E_MPa:EE,alpha_1e6:al,dT_K:dT});
    calc=C('thermal_stress',{E_MPa:EE,alpha_1e6:al,dT_K:dT},'MPa');
    name='Concept thermal-barrier formulation '+tag;
    props={family:'conceptual formulation',key_addition:el,elastic_modulus_MPa:EE,cte_1e6_per_K:al,
      delta_T_K:dT,thermal_stress_MPa:num(ts,2),service_temp_C:ri(rnd,200,1200)};
    desc='Concept formulation '+tag+' built around '+el+' addition for a '+dT+' K swing: constrained thermal stress predicts '+num(ts,2)+' MPa. Predicted — not measured; thermal cycling tests required.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,mat_id:id,title:name+' — Concept Formulation',category:cat,record_type:'concept-design',
    material:name,composition:props.alloyants||props.matrix||props.key_addition||'conceptual',
    properties:props,processing:['conceptual route — lab scale first'],applications:['study concept'],
    standards:['ASTM E8','ASTM E384'],calculations:calc,description:desc,source:'signature',
    source_ref:{authority:'JAH Databases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',data_quality:'predicted-not-measured',
    design_status:'conceptual formulation — properties predicted, not measured',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MAT-\d{7}$/.test(r.id||''))e.push('id');
  if(r.mat_id!==r.id)e.push('mat_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.material!=='string'||!r.material.length)e.push('material');
  if(!r.properties||typeof r.properties!=='object')e.push('properties');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.data_quality!=='predicted-not-measured')e.push('data_quality');
  }
  if(r.source==='online'&&(!r.source_ref||!r.source_ref.authority))e.push('source_ref');
  var c=r.calculations;
  if(c){var f=FORMULAS[c.formula];
    if(!f)e.push('calc_formula');
    else{var expect=f(c.inputs),got=+c.result;
      if(!(got>=0)||Math.abs(got-expect)/Math.max(expect,1e-12)>0.03)e.push('calc_recompute');}}
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-materials-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('materials',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
