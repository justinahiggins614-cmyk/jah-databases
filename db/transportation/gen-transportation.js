(function(){'use strict';
/* JAH Transportation Database generator — deterministic, every record validated.
   Signature records are DESIGN CONCEPTS — never presented as real vehicles
   or routes. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['road','rail','air','maritime','urban-transit'];
var PREFIX='JAH-TRN-';
var NOTICE='DESIGN CONCEPT — an invented concept for study, not a real vehicle or route.';
var CONCEPTS=[
 ['Skybridge cable ferry','air','a cable car crossing a wide river gorge'],
 ['Harbor hop catamaran','maritime','a twin-hull ferry for island commuters'],
 ['Dune rail cruiser','rail','a desert train on a raised guideway'],
 ['Night owl metro loop','urban-transit','an overnight subway ring line'],
 ['Solar mail trike','road','a three-wheel cargo trike with a solar roof'],
 ['River packet steamer','maritime','a shallow-draft cargo boat'],
 ['Stratospheric glider bus','air','a high glider towing passenger pods'],
 ['Greenbelt tramway','urban-transit','a tram through a park corridor'],
 ['Ice road hauler','road','a tracked winter freight rig'],
 ['Maglev shuttle pod','rail','a small magnetic-levitation shuttle']
];
var STOPS=['Northgate','Millford','Cedar Falls','Portside','Hillcrest','Lakeside','Oldtown','Fairview','Brookline','Summit'];
var SPEC_T=[['cruise speed','km/h',function(r){return ri(r,20,300);}],['capacity','passengers',function(r){return ri(r,4,400);}],['range','km',function(r){return ri(r,50,2000);}],['length','m',function(r){return ri(r,6,220);}]];
function fmt(n){return Math.round(n*100)/100;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var cp=pick(CONCEPTS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var nst=ri(rnd,3,5),stops=[],seen={};
  while(stops.length<nst){var s=pick(STOPS,rnd);if(!seen[s]){seen[s]=1;stops.push(s);}}
  var segs=[],total=0,i;
  for(i=0;i<nst-1;i++){var km=fmt(4+rnd()*60);segs.push(km);total=fmt(total+km);}
  var timeH=fmt(total/(40+rnd()*120));
  var specs=[],used={};
  for(i=0;i<3;i++){var sp=pick(SPEC_T,rnd);if(used[sp[0]]){i--;continue;}used[sp[0]]=1;
    specs.push({label:sp[0],value:sp[2](rnd),unit:sp[1]});}
  return {
    id:id,record_id:id,
    title:'Design concept: '+cp[0]+' ('+cp[1]+')',
    category:cat,concept_type:cp[1],
    description:cp[0]+' — '+cp[2]+'. An invented concept for studying how '+cat+' systems are specified. '+NOTICE,
    specs:specs,
    route:{stops:stops,segments_km:segs,total_km:total},
    performance:{distance_km:total,time_h:timeH,avg_speed_kmh:fmt(total/timeH)},
    is_real:false,notice:NOTICE,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-TRN-\d{7}$/.test(r.id||''))e.push('id');
  if(r.record_id!==r.id)e.push('record_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.is_real!==false)e.push('is_real');
    if(typeof r.notice!=='string'||r.notice.indexOf('not a real vehicle or route')<0)e.push('notice');
    if(r.title.indexOf('Design concept:')!==0)e.push('title-prefix');
    if(typeof r.concept_type!=='string'||!r.concept_type.length)e.push('concept_type');
    if(!Array.isArray(r.specs)||r.specs.length<2)e.push('specs');
    else r.specs.forEach(function(s){if(typeof s.label!=='string'||!s.label.length||typeof s.value!=='number'||typeof s.unit!=='string'||!s.unit.length)e.push('spec');});
    var rt=r.route;
    if(!rt||!Array.isArray(rt.stops)||rt.stops.length<3)e.push('route-stops');
    else if(!Array.isArray(rt.segments_km)||rt.segments_km.length!==rt.stops.length-1)e.push('route-segments');
    else{
      var sum=0;rt.segments_km.forEach(function(k){if(typeof k!=='number'||k<=0)e.push('segment');sum+=k;});
      if(typeof rt.total_km!=='number'||Math.abs(sum-rt.total_km)>0.011)e.push('route-total-recompute');
    }
    var pf=r.performance;
    if(!pf||typeof pf.distance_km!=='number'||typeof pf.time_h!=='number'||pf.time_h<=0||typeof pf.avg_speed_kmh!=='number')e.push('performance');
    else if(Math.abs(pf.distance_km/pf.time_h-pf.avg_speed_kmh)>Math.max(0.01,pf.avg_speed_kmh*0.005))e.push('speed-recompute');
  }else{
    if(r.is_real!==true)e.push('is_real');
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
    if(typeof r.subject_name!=='string'||!r.subject_name.length)e.push('subject_name');
    if(!Array.isArray(r.key_specs)||r.key_specs.length<2)e.push('key_specs');
    else r.key_specs.forEach(function(s){if(typeof s.label!=='string'||!s.label.length||typeof s.value!=='string'||!s.value.length)e.push('key_spec');});
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-transportation-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('transportation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
