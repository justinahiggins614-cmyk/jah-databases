(function(){'use strict';
/* JAH Transportation Database generator — deterministic, every record validated.
   Signature records are DESIGN CONCEPTS — never presented as real vehicles
   or routes. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['road','rail','air','maritime','urban-transit','future-transport','amphibious-vehicles','ev-innovation','personal-mobility'];
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
var NEW_FAM_TOPICS={
'future-transport':[["The Sky Lane Commuter", "A personal eVTOL for the daily commute."], ["The Hyperloop Pod Network", "Tubes, pods, and 900 km/h commutes."], ["The Autonomous Ferry Swarm", "Driverless boats for the harbor city."], ["The Maglev Bicycle Lane", "Magnetic assist for the uphill commute."], ["The Straddling Bus Returns", "A bus that drives over traffic."], ["The Personal Rapid Transit Mesh", "Podcars on demand, everywhere."], ["The Solar Sail Cargo Ship", "Windjammers for the container age."], ["The Urban Cable Car Revival", "Gondolas as mass transit."], ["The Night Freight Airship", "Slow cargo, gently, by air."], ["The Sidewalk Delivery Fleet", "Cooler-sized robots on every block."], ["The Vacuum Tube Freight", "Hyperloop for boxes."], ["The Electric Seaplane Commuter", "Harbor to harbor, no runway."], ["The Bike Highway Network", "Grade-separated cycling freeways."], ["The Autonomous Sleeper Coach", "Sleep through the journey."], ["The Future Transport Ledger", "Every concept, honestly costed: the capstone."]],
'amphibious-vehicles':[["The Commuter Duck", "A car that ferries across the river."], ["The Rescue Amphibian", "Flood rescue without boats or trucks — both."], ["The Lake Bus", "A bus that’s also a tour boat."], ["The Fisherman’s Friend", "A pickup that launches its own boat."], ["The Island Hopper", "A taxi that island-hops."], ["The Swamp Buggy Bus", "A bus for the wetlands."], ["The Amphibious Camper", "A camper that moors."], ["The Harbor Patrol Craft", "A patrol boat that chases onto land."], ["The Duck Boat Done Right", "The tour duck, re-engineered for safety."], ["The Research Amphibian", "A lab that drives into the estuary."], ["The Firefighting Amphibian", "A fire truck that drafts from the lake."], ["The Amphibious Food Truck", "A food truck that ferries."], ["The Mail Boat Truck", "Rural delivery, wet or dry."], ["The Amphibious School Bus", "A school bus for the flooded route."], ["The Amphibian’s Code", "Float or drive — never neither: the capstone."]],
'ev-innovation':[["The Battery-Swap Sedan", "A sedan that swaps batteries in 90 seconds."], ["The Solar Roof Wagon", "A wagon that sips the sun."], ["The In-Wheel Motor City Car", "Motors in the wheels, space in the cabin."], ["The Bidirectional Pickup", "A pickup that powers the house."], ["The Solid-State Sports Car", "500 km in a sports car, charging in 10 minutes."], ["The Autonomous Delivery Van", "A van with no cab."], ["The Electric Fire Engine", "A fire engine that’s quiet — until it isn’t."], ["The Swappable-Battery Scooter", "A scooter with vending-machine batteries."], ["The Electric Snow Groomer", "A groomer that doesn’t foul the powder."], ["The Vehicle-to-Grid Fleet", "A fleet that’s a power plant."], ["The Lightweight Commuter", "400 kg, 200 km: the minimal EV."], ["The Electric Classic Conversion", "A 1965 icon, electrified."], ["The Charging Road Pilot", "A highway that charges as you drive."], ["The EV Winter Package", "An EV that loves winter."], ["The Electron’s Promise", "The grid gets cleaner; the car follows: the capstone."]],
'personal-mobility':[["The Standing Scooter Plus", "A scooter you stand tall on."], ["The One-Wheel Commuter", "A single wheel, total freedom."], ["The Enclosed E-Trike", "A trike with a roof."], ["The Walking Exoskeleton Lite", "A gentle push for tired legs."], ["The Cargo E-Bike Max", "A bike that replaces the second car."], ["The Skateboard Commuter Pro", "A board with suspension."], ["The Folding E-Bike Ultra", "A bike that folds to briefcase."], ["The Mobility Scooter, Redesigned", "A scooter with dignity."], ["The Handcycle Sport", "Arm-powered speed."], ["The Snow Commuter Sled", "A sled for the snowy city."], ["The Standing Wheelchair Hybrid", "A chair that stands you up."], ["The Shared Micro-Fleet", "A block’s shared scooters."], ["The Night-Shift Trike", "A trike with lights like a ship."], ["The Last-Mile Wardrobe", "A locker network for the multimodal."], ["The Human Scale", "The city at 15 km/h: the capstone."]]
};
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
  var famT=NEW_FAM_TOPICS[cat]?NEW_FAM_TOPICS[cat][(seed-1)%NEW_FAM_TOPICS[cat].length]:null;
  var famTitle=famT?("Design concept: "+famT[0]+" ("+cat.replace(/-/g," ")+")"):null;
  var famDesc=famT?(famT[0]+" \u2014 "+famT[1]+" A Signature-generated concept in the transportation archive.") : null;
  return {
    id:id,record_id:id,
    title:famTitle||('Design concept: '+cp[0]+' ('+cp[1]+')'),
    category:cat,concept_type:cp[1],
    description:famDesc||(cp[0]+' — '+cp[2]+'. An invented concept for studying how '+cat+' systems are specified. '+NOTICE),
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
