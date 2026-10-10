(function(){'use strict';
/* JAH Astronomy Database — deterministic boundless generator.
   Conceptual exoplanets/missions/observatories; validate() recomputes math.
   Generated missions are marked conceptual and never masquerade as real. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(a,r){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function rf(r,a,b,d){var v=a+r()*(b-a);return d==null?v:+v.toFixed(d);}
var CATS=['planets','stars','galaxies','missions','observations'];
var PREFIX='JAH-AST-';
var RTYPES=['datasheet','orbital','physical','mission','observation','calculation','technology','history','comparison','concept-design','dimensions','tolerance-class','material-process','application','selection','installation','maintenance','safety','failure-modes','standards'];
var MU_SUN=1.32712440018e11; /* km^3/s^2 */
var FORMULAS={
 orbital_period_d:function(i){return 2*Math.PI*Math.sqrt(Math.pow(i.a_km,3)/i.mu_km3_s2)/86400;},
 escape_kms:function(i){return Math.sqrt(2*i.mu_km3_s2/i.r_km);},
 orbital_v_kms:function(i){return Math.sqrt(i.mu_km3_s2/i.r_km);},
 light_days:function(i){return i.dist_ly*365.25;},
 synodic_d:function(i){return 1/Math.abs(1/i.T1_d-1/i.T2_d);},
 angular_arcsec:function(i){return 2*Math.atan(i.d_km/(2*i.D_km))*206265;},
 parsec_dist:function(i){return 1/i.p_arcsec;},
 hill_radius:function(i){return i.a_km*Math.pow(i.m_ratio/3,1/3);}
};
var ARCH=[['Concept Exoplanet','planets'],['Concept Mission','missions'],['Concept Observatory','observations'],['Concept Star System','stars'],['Concept Deep Survey','galaxies']];
function num(n,d){return +(+n).toFixed(d==null?3:d);}
function sfig(v){return +(+v).toPrecision(6);}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var af=ARCH.filter(function(x){return x[1]===cat;});
  var name=pick(af.length?af:ARCH,rnd)[0];
  var tag='AS-'+ri(rnd,100,999)+'-'+String.fromCharCode(65+ri(rnd,0,25));
  var spec={},orb=null,phys=null,mis=null,calc=null,desc='';
  function C(formula,inputs,unit){return {formula:formula,inputs:inputs,result:sfig(FORMULAS[formula](inputs)),unit:unit};}
  if(name==='Concept Exoplanet'){
    var a_au=rf(rnd,0.05,5,3),a_km=a_au*149597870.7,mstar=rf(rnd,0.3,1.6,2);
    var mu=MU_SUN*mstar;
    var T=FORMULAS.orbital_period_d({a_km:a_km,mu_km3_s2:mu});
    var rp=rf(rnd,0.5,2.5,2),mp=rf(rnd,0.5,8,1);
    calc=C('orbital_period_d',{a_km:num(a_km,1),mu_km3_s2:mu},'days');
    orb={semi_major_axis_au:a_au,semi_major_axis_km:num(a_km,0),period_days:num(T,2),star_mass_solar:mstar,eccentricity:rf(rnd,0,0.3,2)};
    phys={radius_earth:rp,mass_earth:mp,method:'transit + radial velocity (concept)'};
    spec={designation:'JAH-EXO-'+tag,class:rp<1.6?'rocky (concept)':'gas-rich (concept)'};
    desc='Concept exoplanet JAH-EXO-'+tag+': '+rp+' Earth radii, '+mp+' Earth masses, orbiting a '+mstar+' solar-mass star at '+a_au+' AU — period '+num(T,2)+' days. Generated concept for study: not a real detection; real exoplanets live in the archive with measured data.';
  }else if(name==='Concept Mission'){
    var dest=pick(['Mars','Venus','Europa','Titan','Enceladus','Psyche','Ceres','a near-Earth asteroid'],rnd);
    var yr=ri(rnd,2030,2060),dur=rf(rnd,0.5,12,1);
    var dv=rf(rnd,3,12,1);
    mis={destination:dest,launch_year:yr,cruise_years:dur,delta_v_kms:dv,propulsion:pick(['chemical','solar-electric','nuclear-electric (concept)'],rnd),status:'conceptual study'};
    spec={mission:'JAH-MSN-'+tag,cost_class:pick(['Discovery','New Frontiers','Flagship (concept)'],rnd)};
    desc='Concept mission JAH-MSN-'+tag+' to '+dest+': notional launch '+yr+', '+dur+'-year cruise, Δv budget '+dv+' km/s. Generated concept study — not a real funded mission; real missions are archived with verified dates.';
    calc={formula:'light_days',inputs:{dist_ly:0.00001},result:num(FORMULAS.light_days({dist_ly:0.00001}),4),unit:'days placeholder'};
  }else if(name==='Concept Observatory'){
    var ap=rf(rnd,0.5,15,1);
    var ang=FORMULAS.angular_arcsec({d_km:ap*1000,D_km:3.844e5});
    calc=C('angular_arcsec',{d_km:ap*1000,D_km:3.844e5},'arcsec');
    spec={aperture_m:ap,type:pick(['reflector','radio array','interferometer'],rnd),site:pick(['Atacama (concept)','lunar far side (concept)','L2 halo (concept)'],rnd)};
    desc='Concept observatory '+tag+': '+ap+' m aperture resolving ~'+num(ang,3)+' arcsec at lunar distance. Generated concept: site, funding, and technology readiness gate any real facility.';
  }else if(name==='Concept Star System'){
    var nstars=ri(rnd,1,3),dly=rf(rnd,4,500,1);
    var lt=FORMULAS.light_days({dist_ly:dly});
    calc=C('light_days',{dist_ly:dly},'days');
    spec={stars:nstars,distance_ly:dly,light_travel_days:num(lt,0),spectral:pick(['G2V (concept)','K5V (concept)','M3V (concept)','A0V (concept)'],rnd)};
    desc='Concept star system '+tag+': '+nstars+' star(s), '+spec.spectral+', '+dly+' light-years away (light travel '+num(lt,0)+' days). Generated concept for world-building and study.';
  }else{
    var z=rf(rnd,0.1,6,2),dly2=rf(rnd,1000,12000,0);
    calc=C('light_days',{dist_ly:dly2},'days');
    spec={survey:'JAH-DS-'+tag,redshift:z,lookback_ly:dly2,targets:ri(rnd,1000,1000000)};
    desc='Concept deep survey JAH-DS-'+tag+' to redshift '+z+' ('+dly2.toLocaleString()+' light-years lookback), targeting '+spec.targets.toLocaleString()+' galaxies. Generated concept: real surveys (SDSS, DESI, Euclid) are archived with measured results.';
  }
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,ast_id:id,title:name+' '+tag+' — Concept Record',category:cat,record_type:'concept-design',
    object:name+' '+tag,specifications:spec,orbital:orb,physical:phys,mission:mis,
    calculations:calc,description:desc,source:'signature',
    source_ref:{authority:'JAH Databases — Signature generator',url:''},
    creation_mode:'SIGNATURE-GENERATED',design_status:'conceptual — generated concept; not a real detection, mission, or facility',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-AST-\d{7}$/.test(r.id||''))e.push('id');
  if(r.ast_id!==r.id)e.push('ast_id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(RTYPES.indexOf(r.record_type)<0)e.push('record_type');
  if(typeof r.object!=='string'||!r.object.length)e.push('object');
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
var gen={version:'jahdb-space-astro-1.0',generate:generate,validate:validate,FORMULAS:FORMULAS,CATS:CATS,PREFIX:PREFIX,RTYPES:RTYPES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('space-astro',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
