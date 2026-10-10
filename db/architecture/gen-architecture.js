(function(){'use strict';
/* JAH Architecture Database — deterministic boundless generator.
   Conceptual building/component designs; validate() recomputes all math. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['residential','commercial','structural','sustainable','interiors'];
var PREFIX='JAH-ARCH-';
var RTYPES=['datasheet','plans','calculation','structural','materials','sustainable','interiors','application','selection','codes','maintenance','safety','history','comparison','concept-design','dimensions','tolerance-class','material-process','installation','failure-modes','standards'];
var FORMULAS={
 floor_area:function(i){return i.L_m*i.W_m;},
 concrete_vol:function(i){return i.area_m2*i.t_m;},
 steel_tonnage:function(i){return i.area_m2*i.kg_m2/1000;},
 live_load:function(i){return i.area_m2*i.kPa;},          /* kN */
 stair_riser:function(i){return i.total_rise_mm/i.risers;},
 occupancy:function(i){return i.area_m2/i.m2_per_person;},
 daylight_factor:function(i){return i.glazing_m2/i.floor_m2*100;},
 rainwater:function(i){return i.roof_m2*i.rain_mm/1000*0.9;}, /* m³/yr */
 beam_reaction:function(i){return i.w_kN_m*i.L_m/2;},
 column_load:function(i){return i.floors*i.area_m2*i.kPa;},
 hvac_tonnage:function(i){return i.area_m2/35;},            /* tons approx */
 paint_liters:function(i){return i.wall_m2/10*2;}
};
var ARCH=[
 ['Courtyard House','residential'],['Mixed-Use Block','commercial'],['Timber Frame Hall','structural'],
 ['Net-Zero Pavilion','sustainable'],['Loft Interior','interiors'],['Rowhouse Terrace','residential'],
 ['Office Tower Concept','commercial'],['Steel Truss Bridge Hall','structural'],
 ['Earth-Sheltered Retreat','sustainable'],['Gallery Interior','interiors']
];
function num(n,d){return +(+n).toFixed(d==null?2:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var af=ARCH.filter(function(x){return x[1]===cat;});
  var t=pick(af.length?af:ARCH,rnd);
  var tag='AR-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var spec={},calc=null,desc='';
  function C(formula,inputs,unit){return {formula:formula,inputs:inputs,result:sfig(FORMULAS[formula](inputs)),unit:unit};}
  var L=rf(rnd,8,60,1),W=rf(rnd,6,40,1),area=FORMULAS.floor_area({L_m:L,W_m:W});
  if(t[0]==='Courtyard House'||t[0]==='Rowhouse Terrace'){
    var beds=ri(rnd,2,5);
    calc=C('floor_area',{L_m:L,W_m:W},'m²');
    spec={footprint_L_m:L,footprint_W_m:W,floor_area_m2:num(area,1),bedrooms:beds,storeys:ri(rnd,1,3),structure:'load-bearing masonry + timber joists (concept)'};
    desc='Concept '+t[0].toLowerCase()+' '+tag+': '+num(area,1)+' m² footprint ('+L+' × '+W+' m), '+beds+' bedrooms. Generated concept: verify egress, daylight, and local energy code for a real scheme.';
  }else if(t[0]==='Mixed-Use Block'||t[0]==='Office Tower Concept'){
    var fl=ri(rnd,2,t[0]==='Office Tower Concept'?40:8);
    var tot=area*fl,occ=FORMULAS.occupancy({area_m2:tot,m2_per_person:10});
    calc=C('occupancy',{area_m2:num(tot,1),m2_per_person:10},'persons');
    spec={footprint_m2:num(area,1),floors:fl,gfa_m2:num(tot,0),occupancy:num(occ,0),structure:'steel frame, composite deck (concept)'};
    desc='Concept '+t[0].toLowerCase()+' '+tag+': '+fl+' floors, '+num(tot,0)+' m² GFA, ~'+num(occ,0)+' occupants. Generated concept: core sizing, elevator traffic, and fire strategy come before any facade study.';
  }else if(t[0]==='Timber Frame Hall'||t[0]==='Steel Truss Bridge Hall'){
    var span=rf(rnd,12,60,1),w=rf(rnd,2,10,1);
    var R=FORMULAS.beam_reaction({w_kN_m:w,L_m:span});
    calc=C('beam_reaction',{w_kN_m:w,L_m:span},'kN');
    spec={span_m:span,uniform_load_kN_m:w,reaction_kN:num(R,1),system:t[0]==='Timber Frame Hall'?'glulam portal frames (concept)':'steel trusses (concept)'};
    desc='Concept '+t[0].toLowerCase()+' '+tag+': '+span+' m span under '+w+' kN/m → '+num(R,1)+' kN end reactions. Generated concept: connection design and lateral stability govern the real frame.';
  }else if(t[0]==='Net-Zero Pavilion'||t[0]==='Earth-Sheltered Retreat'){
    var glz=rf(rnd,10,80,1),df=FORMULAS.daylight_factor({glazing_m2:glz,floor_m2:area});
    calc=C('daylight_factor',{glazing_m2:glz,floor_m2:num(area,1)},'%');
    spec={floor_area_m2:num(area,1),glazing_m2:glz,daylight_factor_pct:num(df,1),strategy:'passive solar + heat pump + PV (concept)',target:'net-zero annual energy'};
    desc='Concept '+t[0].toLowerCase()+' '+tag+': '+num(area,1)+' m² with '+glz+' m² glazing ('+num(df,1)+'% daylight factor), targeting net-zero. Generated concept: model with real climate data; airtightness detailing decides success.';
  }else{
    var wall=rf(rnd,60,400,0),pl=FORMULAS.paint_liters({wall_m2:wall});
    calc=C('paint_liters',{wall_m2:wall},'liters');
    spec={wall_area_m2:wall,paint_L:num(pl,1),finish:'low-VOC (concept)',lighting:'layered ambient/task/accent (concept)'};
    desc='Concept '+t[0].toLowerCase()+' '+tag+': '+wall+' m² of wall needs ~'+num(pl,1)+' L for two coats. Generated concept: sample finishes in the real light before committing.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,arch_id:id,title:t[0]+' '+tag+' — Concept Design',category:cat,record_type:'concept-design',
    subject:t[0]+' '+tag,specifications:spec,structural:{system:spec.structure||spec.system||'conceptual'},
    standards:['IBC','local building code (concept)'],calculations:calc,
    description:desc,source:'signature',
    source_ref:{authority:'JAH Data Bases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',design_status:'conceptual — not a permitted design; a licensed architect/engineer must develop any real project',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ARCH-\d{7}$/.test(r.id||''))e.push('id');
  if(r.arch_id!==r.id)e.push('arch_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.subject!=='string'||!r.subject.length)e.push('subject');
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
var gen={version:'jahdb-architecture-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('architecture',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
