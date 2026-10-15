(function(){'use strict';
/* Weather Database generator — jahdb-weather-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-WX-';
var TOPICS=[["Rain", "Falling water drops from clouds."], ["Snow", "Falling ice crystals in cold air."], ["Hail", "Ice balls formed in strong thunderstorms."], ["Thunderstorms", "Storms of lightning, thunder, and heavy rain."], ["Lightning", "The electric flash of storms."], ["Tornadoes", "Violent rotating funnels of wind."], ["Hurricanes", "The great tropical cyclones of the Atlantic."], ["Typhoons", "The Pacific's name for hurricanes."], ["Clouds", "Visible masses of water droplets in the sky."], ["Cumulus Clouds", "The puffy fair-weather clouds."], ["Stratus Clouds", "The gray layered clouds of overcast days."], ["Cirrus Clouds", "The wispy high ice-crystal clouds."], ["Fog", "Cloud at ground level reducing visibility."], ["Wind", "Moving air from high to low pressure."], ["Temperature", "How hot or cold the air is."], ["Humidity", "The moisture in the air."], ["The Barometer", "The instrument measuring air pressure."], ["Weather Forecasting", "How meteorologists predict the weather."], ["Meteorologists", "The scientists of the atmosphere."], ["Weather Radar", "Tracking precipitation with radio waves."], ["Seasons", "The yearly weather cycle."], ["Cold Fronts", "Boundaries where cold air pushes in."], ["Warm Fronts", "Boundaries bringing gradual warming."], ["Dew", "Morning moisture condensing on surfaces."], ["Frost", "Ice crystals forming on cold surfaces."], ["Rainbows", "Sunlight splitting through raindrops."], ["Droughts", "Long periods without rain."], ["Heat Waves", "Extended periods of extreme heat."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'weather record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('weather',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();