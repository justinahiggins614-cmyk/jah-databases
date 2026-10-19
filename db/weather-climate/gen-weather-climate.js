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
  opts=opts||{};
  if(opts.record_kind==='forecast')return generateForecast(seed,opts,rnd);
  if(opts.record_kind==='accuracy')return generateAccuracy(seed,opts,rnd);
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
/* ============ EXPANSION 2026-10-17 (audit item 57) ============
   Forecast records and forecast-accuracy records. Observations (the existing
   path) are untouched; opt-in via opts.record_kind='forecast'|'accuracy'. */
var FC_HORIZONS=[6,12,24,48,72,120];
var FC_MODELS=['JAH-Forecast-1.0','JAH-Forecast-Ensemble-2.1'];
function fcPrng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function fcTs(rnd,baseY){
  var y=baseY||ri(rnd,2024,2026),mo=ri(rnd,1,12),d=ri(rnd,1,28),h=ri(rnd,0,23);
  function z(n){return (n<10?'0':'')+n;}
  return y+'-'+z(mo)+'-'+z(d)+'T'+z(h)+':00:00Z';
}
function fcStation(rnd,seed){
  var region=pick(rnd,REGIONS);
  return {station_id:'WX-'+region[0]+'-'+String(seed%10000).padStart(4,'0'),
    station_name:pick(rnd,STATION_NAMES)+' '+pick(rnd,SUFFIX),
    lat:r2(-90+rnd()*180), lon:r2(-180+rnd()*360)};
}
function generateForecast(seed,opts,rnd){
  rnd=rnd||fcPrng((opts&&opts.salt)?(seed^opts.salt):(seed^0xfc57));
  var st=fcStation(rnd,seed);
  var horizon=pick(rnd,FC_HORIZONS), model=pick(rnd,FC_MODELS);
  var cond=pick(rnd,CATS);
  var tr=TEMP_RANGE[cond], hr=HUM_RANGE[cond], pr=PRECIP_RANGE[cond];
  var ptemp=r2(tr[0]+rnd()*(tr[1]-tr[0]));
  var phum=ri(rnd,hr[0],hr[1]);
  var pprecip=pr[1]===0?0:r2(pr[0]+rnd()*(pr[1]-pr[0]));
  var issued=fcTs(rnd);
  var title='Forecast \u2014 '+st.station_name+' (+'+horizon+'h)';
  var desc='Weather forecast record: '+model+' issued '+issued+' for '+st.station_name+' ('+st.station_id+'). Valid '+horizon+' hours ahead: '+cond+', '+ptemp+'\u00b0C, humidity '+phum+'%, precipitation '+pprecip+' mm. Forecast skill declines with horizon; verify against observations when the valid time arrives.';
  return {id:'JAH-WX-'+pad(seed),record_kind:'forecast',
    station_id:st.station_id,station_name:st.station_name,lat:st.lat,lon:st.lon,
    issued_at:issued,horizon_hours:horizon,model:model,
    predicted_condition:cond,predicted_temp_c:ptemp,predicted_humidity:phum,
    predicted_precip_mm:pprecip,title:title,description:desc,
    source:'synthetic',creation_mode:'SIGNATURE-GENERATED'};
}
function generateAccuracy(seed,opts,rnd){
  rnd=rnd||fcPrng((opts&&opts.salt)?(seed^opts.salt):(seed^0xacc4^0x5bd1));
  var st=fcStation(rnd,seed);
  var horizon=pick(rnd,FC_HORIZONS), model=pick(rnd,FC_MODELS);
  var pcond=pick(rnd,CATS);
  var tr=TEMP_RANGE[pcond];
  var ptemp=r2(tr[0]+rnd()*(tr[1]-tr[0]));
  var otemp=r2(Math.max(tr[0]-3,Math.min(tr[1]+3,ptemp+(rnd()*8-4))));
  var pprecip=r2(rnd()*20), oprecip=r2(Math.max(0,pprecip+(rnd()*10-5)));
  var hit=rnd()<0.72;
  var ocond=hit?pcond:pick(rnd,CATS);
  var terr=r2(Math.abs(ptemp-otemp));
  var skill=r2(Math.max(0,100-terr*8-(hit?0:25)));
  var issued=fcTs(rnd), verified=fcTs(rnd);
  var title='Forecast accuracy \u2014 '+st.station_name+' (+'+horizon+'h)';
  var desc='Forecast-accuracy record: '+model+' forecast for '+st.station_name+' ('+st.station_id+') issued '+issued+' and verified '+verified+' at +'+horizon+'h. Predicted '+ptemp+'\u00b0C/'+pcond+' vs observed '+otemp+'\u00b0C/'+ocond+': temperature error '+terr+'\u00b0C, condition '+(hit?'hit':'miss')+', skill score '+skill+'/100. Accuracy records close the loop between forecasts and observations.';
  return {id:'JAH-WX-'+pad(seed),record_kind:'forecast-accuracy',
    station_id:st.station_id,station_name:st.station_name,lat:st.lat,lon:st.lon,
    issued_at:issued,verified_at:verified,horizon_hours:horizon,model:model,
    predicted_condition:pcond,predicted_temp_c:ptemp,predicted_precip_mm:pprecip,
    observed_condition:ocond,observed_temp_c:otemp,observed_precip_mm:oprecip,
    temp_error_c:terr,condition_hit:hit,skill_score:skill,
    title:title,description:desc,
    source:'synthetic',creation_mode:'SIGNATURE-GENERATED'};
}
function validateForecast(r,e){
  if(r.record_kind!=='forecast'&&r.record_kind!=='forecast-accuracy')e.push('record_kind');
  if(typeof r.station_id!=='string'||!/^WX-[A-Z]{2}-\d{4}$/.test(r.station_id))e.push('station_id');
  if(typeof r.station_name!=='string'||!r.station_name.length)e.push('station_name');
  if(typeof r.lat!=='number'||r.lat<-90||r.lat>90)e.push('lat');
  if(typeof r.lon!=='number'||r.lon<-180||r.lon>180)e.push('lon');
  if(typeof r.issued_at!=='string'||!/^\d{4}-\d{2}-\d{2}T\d{2}:00:00Z$/.test(r.issued_at))e.push('issued_at');
  if(FC_HORIZONS.indexOf(r.horizon_hours)<0)e.push('horizon_hours');
  if(FC_MODELS.indexOf(r.model)<0)e.push('model');
  if(CATS.indexOf(r.predicted_condition)<0)e.push('predicted_condition');
  if(typeof r.predicted_temp_c!=='number')e.push('predicted_temp_c');
  if(typeof r.predicted_precip_mm!=='number'||r.predicted_precip_mm<0)e.push('predicted_precip_mm');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(r.record_kind==='forecast-accuracy'){
    if(typeof r.verified_at!=='string'||!/^\d{4}-\d{2}-\d{2}T\d{2}:00:00Z$/.test(r.verified_at))e.push('verified_at');
    if(CATS.indexOf(r.observed_condition)<0)e.push('observed_condition');
    if(typeof r.observed_temp_c!=='number')e.push('observed_temp_c');
    if(typeof r.temp_error_c!=='number'||r.temp_error_c<0)e.push('temp_error_c');
    if(typeof r.condition_hit!=='boolean')e.push('condition_hit');
    if(typeof r.skill_score!=='number'||r.skill_score<0||r.skill_score>100)e.push('skill_score');
  }
  return {ok:!e.length,errors:e};
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-WX-\d{6}$/.test(r.id))e.push('id');
  if(r.record_kind==='forecast'||r.record_kind==='forecast-accuracy')return validateForecast(r,e);
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

/* GROUP3 expansion bridge (2026-10-18): node-only; covers new item record shapes
   added by the group-3 expansion worker. Browser behavior unchanged. */
(function(){
if(typeof module==='undefined'||!module.exports) return;
var GROUP3=null;
try{ GROUP3=require('./expansion-group3.json'); }catch(e){ GROUP3=null; }
if(!GROUP3||!GROUP3.byId) return;
if(module.exports.__group3bridged) return;
module.exports.__group3bridged=true;
var _gen=module.exports.generate, _val=module.exports.validate;
var REQUIRED=["condition", "demo", "humidity", "id", "lat", "lon", "precip_mm", "station_id", "station_name", "temp_c", "timestamp"];
function deepCopy(o){ return JSON.parse(JSON.stringify(o)); }
function lookup(seed,opts){
  if(seed!==undefined&&seed!==null&&GROUP3.bySeed&&GROUP3.bySeed[String(seed)]) return GROUP3.bySeed[String(seed)];
  if(opts&&opts.id&&GROUP3.byId[opts.id]) return GROUP3.byId[opts.id];
  return null;
}
function isGroup3(r){
  if(!r||typeof r!=='object') return false;
  if(r.id&&GROUP3.byId[r.id]) return true;
  if(r._seed!==undefined&&r._seed!==null&&GROUP3.bySeed&&GROUP3.bySeed[String(r._seed)]) return true;
  return false;
}
if(typeof _gen==='function'){
  module.exports.generate=function(seed,opts,rnd){
    var hit=lookup(seed,opts);
    if(opts&&opts.group3&&hit) return deepCopy(hit);
    return _gen.call(this,seed,opts,rnd);
  };
}
if(typeof _val==='function'){
  module.exports.validate=function(r){
    if(isGroup3(r)){
      var errs=[];
      for(var i=0;i<REQUIRED.length;i++){ if(!(REQUIRED[i] in r)) errs.push('missing '+REQUIRED[i]); }
      var d=r.demo;
      if(!d||typeof d.program!=='string'||!d.program.length) errs.push('demo.program');
      if(!/^JAH-/.test(r.id||'')) errs.push('id');
      if(r.title!==undefined&&(typeof r.title!=='string'||!r.title.length)) errs.push('title');
      return {ok:errs.length===0,errors:errs};
    }
    return _val.call(this,r);
  };
}
})();
