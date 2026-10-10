(function(){'use strict';
/* JAH Geography Atlas Database generator — deterministic, every record validated.
   Signature records describe FICTIONAL illustrative places — never presented
   as real locations. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['physical','political','climate','hydrology','places'];
var PREFIX='JAH-GEO-';
var NOTICE='FICTIONAL ILLUSTRATIVE GEOGRAPHY — invented for map-reading practice, not a real location.';
var REGIONS=['the Meridia Archipelago','the Thessaly Highlands','the Corvantine Basin','the Isles of Aer','the Vandor Steppes','the Lumen Delta','the Kestrel Ranges','the Palomar Fjords'];
var TYPES={
 physical:[['a volcanic island','basalt cliffs'],['a folded mountain range','ridgelines'],['a canyon system','sandstone walls'],['a plateau','mesa tops'],['a rift valley','fault scarps']],
 political:[['a harbor city-state','charter districts'],['a river confederacy','canton assemblies'],['a highland kingdom','clan provinces'],['a delta republic','ward councils'],['a steppe khanate','banner camps']],
 climate:[['a monsoon coast','rain belts'],['a high desert','dune seas'],['a cloud forest','moss zones'],['a tundra plain','permafrost'],['a savanna corridor','grass seas']],
 hydrology:[['a braided river','channels'],['a crater lake','shores'],['a tidal estuary','mudflats'],['an artesian basin','springs'],['a glacial fjord','inlets']],
 places:[['a market town','bazaars'],['a lighthouse point','beacons'],['a university quarter','colleges'],['a fishing village','harbors'],['a rail junction','yards']]
};
var STAT_T=[['elevation','m',function(r){return ri(r,0,4800);}],['area','sq km',function(r){return ri(r,50,90000);}],['mean temperature','°C',function(r){return ri(r,-12,34);}],['annual rainfall','mm',function(r){return ri(r,80,3200);}],['river length','km',function(r){return ri(r,60,2400);}],['coastline','km',function(r){return ri(r,20,1800);}]];
var NP1=['Vel','Cor','Mar','Dun','Pel','Syl','Kes','Bra'],NP2=['mar','dore','thia','wen','lia','gard','mere','ford'];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var region=pick(REGIONS,rnd),tp=pick(TYPES[cat],rnd);
  var name=pick(NP1,rnd)+pick(NP2,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var lat=Math.round((rnd()*170-85)*100)/100,lng=Math.round((rnd()*350-175)*100)/100;
  var hemi=(lat>=0?'Northern':'Southern')+'/'+(lng>=0?'Eastern':'Western');
  var stats=[],used={},i;
  for(i=0;i<2;i++){var st=pick(STAT_T,rnd);if(used[st[0]]){i--;continue;}used[st[0]]=1;
    stats.push({label:st[0],value:st[2](rnd),unit:st[1]});}
  var neigh=[],seen={};
  while(neigh.length<2){var nb=pick(NP1,rnd)+pick(NP2,rnd);if(nb!==name&&!seen[nb]){seen[nb]=1;neigh.push(nb);}}
  return {
    id:id,record_id:id,
    title:'Illustrative place: '+name+' ('+tp[0]+', '+region+')',
    category:cat,place_type:tp[0],region:region,
    description:name+' is '+tp[0]+' in '+region+' for practicing '+cat+' map reading: '+tp[1]+', setting, neighbors. '+NOTICE,
    coordinates:{lat:lat,lng:lng,hemisphere:hemi},
    stats:stats,neighbors:neigh,
    is_real:false,notice:NOTICE,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-GEO-\d{7}$/.test(r.id||''))e.push('id');
  if(r.record_id!==r.id)e.push('record_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.is_real!==false)e.push('is_real');
    if(typeof r.notice!=='string'||r.notice.indexOf('not a real location')<0)e.push('notice');
    if(r.title.indexOf('Illustrative place:')!==0)e.push('title-prefix');
    var c=r.coordinates;
    if(!c||typeof c.lat!=='number'||typeof c.lng!=='number')e.push('coordinates');
    else{
      if(c.lat<-90||c.lat>90)e.push('lat-range');
      if(c.lng<-180||c.lng>180)e.push('lng-range');
      var hemi=(c.lat>=0?'Northern':'Southern')+'/'+(c.lng>=0?'Eastern':'Western');
      if(c.hemisphere!==hemi)e.push('hemisphere-recompute');
    }
    if(typeof r.place_type!=='string'||!r.place_type.length)e.push('place_type');
    if(typeof r.region!=='string'||!r.region.length)e.push('region');
    if(!Array.isArray(r.stats)||r.stats.length<2)e.push('stats');
    else r.stats.forEach(function(s){if(typeof s.label!=='string'||!s.label.length||typeof s.value!=='number'||typeof s.unit!=='string'||!s.unit.length)e.push('stat');});
    if(!Array.isArray(r.neighbors)||!r.neighbors.length)e.push('neighbors');
  }else{
    if(r.is_real!==true)e.push('is_real');
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
    if(typeof r.place!=='string'||!r.place.length)e.push('place');
    if(typeof r.place_type!=='string'||!r.place_type.length)e.push('place_type');
    if(typeof r.region!=='string'||!r.region.length)e.push('region');
    if(!Array.isArray(r.key_facts)||r.key_facts.length<2)e.push('key_facts');
    else r.key_facts.forEach(function(s){if(typeof s.label!=='string'||!s.label.length||typeof s.value!=='string'||!s.value.length)e.push('key_fact');});
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-geography-atlas-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('geography-atlas',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
