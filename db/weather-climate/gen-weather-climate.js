/* ✳ JAH Weather Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) weather observation generator: jahdb-weather-climate-1.0.
   Observations are synthetically generated for this catalog. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['clear','cloudy','rain','snow','storm','fog'];
var REGIONS=[['NE','Northeast'],['SE','Southeast'],['MW','Midwest'],['SW','Southwest'],['NW','Northwest'],['AK','Alaska'],['HI','Hawaii'],['AT','Atlantic'],['GL','Great Lakes'],['PL','Plains']];
var STATION_NAMES=['Harbor Point','Cedar Ridge','Lakeview','Summit Pass','Riverbend','Mesa Verde','Pine Grove','Blue Hill','Clearwater','Stonebridge','Willow Creek','Granite Falls','Sand Dune','Fog Hollow','Red Mesa','Brookfield','Timberline','Salt Flat','Meadowlark','Iron Ridge','Coral Bay','Frost Hollow','Sunset Plain','Ash Grove','Quail Run','Birchwood','Driftwood','Canyon Mouth','Larkspur','Alder Bend'];
var SUFFIX=['Weather Station','Observatory','Climate Station','Field Station','Met Station'];

var TEMP_RANGE={snow:[-25,1],rain:[2,25],clear:[-10,38],cloudy:[-8,32],storm:[5,35],fog:[-5,25]};
var HUM_RANGE={snow:[50,100],rain:[60,100],clear:[15,60],cloudy:[40,85],storm:[60,100],fog:[80,100]};
var PRECIP_RANGE={snow:[1,25],rain:[1,40],storm:[5,80],fog:[0,1],clear:[0,0],cloudy:[0,0]};

function r2(x){return Math.round(x*100)/100;}
function isoTs(rnd){
  var y=ri(rnd,2024,2026),mo=ri(rnd,1,12),d=ri(rnd,1,28),h=ri(rnd,0,23),mi=pick(rnd,[0,15,30,45]);
  function z(n){return (n<10?'0':'')+n;}
  return y+'-'+z(mo)+'-'+z(d)+'T'+z(h)+':'+z(mi)+':00Z';
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var region=pick(rnd,REGIONS);
  var name=pick(rnd,STATION_NAMES)+' '+pick(rnd,SUFFIX);
  var tr=TEMP_RANGE[cat],hr=HUM_RANGE[cat],pr=PRECIP_RANGE[cat];
  var temp=r2(tr[0]+rnd()*(tr[1]-tr[0]));
  var hum=ri(rnd,hr[0],hr[1]);
  var precip=pr[1]===0?0:r2(pr[0]+rnd()*(pr[1]-pr[0]));
  var lat=r2(-90+rnd()*180), lon=r2(-180+rnd()*360);
  return {
    id:'JAH-WX-'+pad(seed),
    station_id:'WX-'+region[0]+'-'+String(seed%10000).padStart(4,'0'),
    station_name:name,
    lat:lat,
    lon:lon,
    timestamp:isoTs(rnd),
    temp_c:temp,
    humidity:hum,
    precip_mm:precip,
    condition:cat
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-WX-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.station_id!=='string'||!/^WX-[A-Z]{2}-\d{4}$/.test(r.station_id))e.push('station_id');
  if(typeof r.station_name!=='string'||!r.station_name.length)e.push('station_name');
  if(typeof r.lat!=='number'||r.lat<-90||r.lat>90)e.push('lat');
  if(typeof r.lon!=='number'||r.lon<-180||r.lon>180)e.push('lon');
  if(typeof r.timestamp!=='string'||!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:00Z$/.test(r.timestamp))e.push('timestamp');
  var yr=+r.timestamp.slice(0,4); if(yr<2024||yr>2026)e.push('timestamp-year');
  if(CATS.indexOf(r.condition)<0)e.push('condition');
  if(typeof r.temp_c!=='number')e.push('temp_c');
  else{
    if(r.condition==='snow'&&r.temp_c>=2)e.push('temp_c:snow<2');
    if(r.condition==='rain'&&(r.temp_c<2||r.temp_c>25))e.push('temp_c:rain 2-25');
    if(r.condition==='clear'&&(r.temp_c<-10||r.temp_c>38))e.push('temp_c:clear -10..38');
  }
  if(typeof r.humidity!=='number'||r.humidity<0||r.humidity>100)e.push('humidity');
  if(typeof r.precip_mm!=='number'||r.precip_mm<0)e.push('precip_mm');
  if((r.condition==='clear'||r.condition==='cloudy')&&r.precip_mm!==0)e.push('precip_mm:0 for clear/cloudy');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-weather-climate-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('weather-climate',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
