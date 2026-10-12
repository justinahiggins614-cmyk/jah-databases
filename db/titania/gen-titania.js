(function(){'use strict';
/* Titania generator — jahdb-titania-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"fact" = real, verified planetary data. src:"signature" = Signature-authored
   projection, clearly labeled and never presented as established fact. */
var PREFIX='JAH-TIT-';
var SLUG='titania';
var BODY='Titania';
var BTYPE='moon';
var PARENT='Uranus';
var FACTS={"Diameter": "1,578 km", "Distance from Uranus": "436,300 km", "Orbital period": "8.71 days", "Day length": "8.71 days (tidally locked)", "Mean temperature": "-210\u00b0C", "Atmosphere": "Trace CO2", "Gravity": "0.37 m/s\u00b2"};
var FEATURES=[["Largest Uranian moon", "Eighth-largest moon in the solar system."], ["Messina Chasma", "A canyon 1,500 km long and twice as deep as the Grand Canyon."], ["Possible ocean", "May hide liquid water at the rock-ice boundary."]];
var FEATURE_POOLS=null;
var MISSIONS=[["Voyager 2 (1986)", "Mapped the southern hemisphere's canyons."], ["Herschel discovery (1787)", "Found by William Herschel."]];
var KINDS=["overview", "physical-data", "geology", "atmosphere", "exploration", "future"];
var KLBL={overview:'Overview','physical-data':'Physical Data',geology:'Geology & Landforms',atmosphere:'Atmosphere',
 'solar-layer':'Solar Layers', 'solar-activity':'Solar Activity', observation:'Observation & Missions',
 exploration:'Exploration', asteroid:'Asteroids', comet:'Comets', 'meteor-shower':'Meteor Showers',
 meteorite:'Meteorites', 'orbital-mechanics':'Orbital Mechanics', feature:'Features', mission:'Missions', future:'Future & Speculative'};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,arr){return arr[(r()*arr.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function shuffle(r,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(r()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=a[i];a[j]=t;}return a;}
function pad(n){return String(n).padStart(6,'0');}
function factLines(){return Object.keys(FACTS).map(function(k){return k+': '+FACTS[k];}).join(' | ');}
function demoFor(kind, s){
  var D={
   overview:{kind:'light-time',program:'function lightMinutes(distKm){return +(distKm/17987547.5).toFixed(1);}\n// lightMinutes(149600000) -> minutes for sunlight to reach the body',note:'JS: light-travel time to the body.'},
   'physical-data':{kind:'escape-velocity',program:'function escapeVel(g_ms2, rKm){return +Math.sqrt(2*g_ms2*rKm*1000).toFixed(0);}\n// escapeVel(9.81, 6371) -> m/s',note:'JS: escape velocity from surface gravity and radius.'},
   geology:{kind:'crater-scale',program:'function craterEnergy(dKm){return +(Math.pow(dKm,3)*1.2e12).toExponential(2);}\n// craterEnergy(10) -> rough joules for an impactor making a dKm crater',note:'JS: order-of-magnitude impact energy estimator.'},
   atmosphere:{kind:'scale-height',program:'function scaleHeight(tempK, molarMass, g){return +(8.314*tempK/(molarMass/1000*g)/1000).toFixed(2);}\n// scaleHeight(288, 29, 9.81) -> km',note:'JS: atmospheric scale height estimator.'},
   exploration:{kind:'hohmann',program:'function hohmannYears(a1AU, a2AU){var a=(a1AU+a2AU)/2;return +(0.5*Math.pow(a,1.5)).toFixed(2);}\n// hohmannYears(1, 1.52) -> years, Earth to Mars transfer',note:'JS: Hohmann transfer time estimator.'},
   observation:{kind:'hohmann',program:'function hohmannYears(a1AU, a2AU){var a=(a1AU+a2AU)/2;return +(0.5*Math.pow(a,1.5)).toFixed(2);}\n// hohmannYears(1, 1.52) -> years',note:'JS: transfer-time estimator.'},
   'solar-layer':{kind:'fusion-rate',program:'function fusionPower(massKg){return +(massKg*3.6e-4/1.989e30*3.828e26).toExponential(2);}\n// fusionPower(1.989e30) -> watts',note:'JS: luminosity scaling estimator.'},
   'solar-activity':{kind:'flare-scale',program:'function flareClass(wattsM2){var c=["A","B","C","M","X"];var i=Math.min(4,Math.floor(Math.log10(wattsM2)+8));return c[Math.max(0,i)];}\n// flareClass(1e-4) -> GOES class',note:'JS: flare-class estimator.'},
   asteroid:{kind:'delta-v',program:'function deltaV(aAU){return +(Math.sqrt(29.8*29.8*(2-1/aAU))-29.8).toFixed(2);}\n// deltaV(2.77) -> km/s from Earth (rough)',note:'JS: rough rendezvous delta-v estimator.'},
   comet:{kind:'period',program:'function cometPeriod(aAU){return +Math.pow(aAU,1.5).toFixed(1);}\n// cometPeriod(17.8) -> years (Halley)',note:'JS: orbital period from semi-major axis.'},
   'meteor-shower':{kind:'zenith-rate',program:'function expectedCount(zhr, hours, clarity){return Math.round(zhr*hours*clarity);}\n// expectedCount(100, 3, 0.7)',note:'JS: meteor count estimator.'},
   meteorite:{kind:'strewn',program:'function strewnKm(altKm, velKms){return +(altKm*velKms*0.35).toFixed(1);}\n// strewnKm(80, 20) -> km ellipse',note:'JS: strewn-field size estimator.'},
   'orbital-mechanics':{kind:'kepler',program:'function periodYears(aAU){return +Math.pow(aAU,1.5).toFixed(2);}\n// periodYears(2.77) -> years',note:'JS: Kepler third law.'},
   future:{kind:'projection',program:'function arrivalYear(currentTech, targetYear){return targetYear;}\n// Speculative timelines are labeled, never stated as fact.',note:'JS: placeholder — projections are Signature-authored.'}
  };
  return D[kind]||D.overview;
}
function baseRec(seed, kind, s){
  return {id:PREFIX+pad(seed), kind:kind, body:BODY, body_type:BTYPE, parent_body:PARENT,
          demo:demoFor(kind,s), src:'fact', _seed:seed};
}
function bOverview(s,seed){
  var r=baseRec(seed,'overview',s);
  r.title=BODY+' — complete overview';
  r.description='A full overview of '+BODY+' ('+BTYPE+(PARENT?', in the '+PARENT+' system':'')+'). '+factLines()+'.';
  r.known={summary:'Established planetary data, verified against NASA/JPL references.',facts:FACTS};
  return r;
}
function bPhysical(s,seed){
  var r=baseRec(seed,'physical-data',s);
  var keys=Object.keys(FACTS);
  var k=keys[seed%keys.length];
  r.title=BODY+' — '+k;
  r.description='Physical data record for '+BODY+': '+k+' = '+FACTS[k]+'. Full context: '+factLines()+'.';
  r.physical_data=FACTS; r.focus_field=k;
  return r;
}
function bFeature(s,seed,kindKey){
  var pool=(FEATURE_POOLS&&FEATURE_POOLS[kindKey])?FEATURE_POOLS[kindKey]:FEATURES;
  var f=pool[(seed-1)%pool.length];
  var kind=(SLUG==='orbits')?classifyOrbit(f[0]):kindKey;
  var r=baseRec(seed,kind,s);
  r.title=BODY+' — '+f[0];
  r.description=(kind==='solar-layer'?'Solar layer: ':kind==='solar-activity'?'Solar activity: ':'Notable feature of '+BODY+': ')+f[0]+' — '+f[1];
  r.feature={name:f[0],description:f[1]};
  return r;
}
function classifyOrbit(name){
  var n=name.toLowerCase();
  if(/comet|halley|hale-bopp|neowise/.test(n))return 'comet';
  if(/perseid|geminid|leonid|shower/.test(n))return 'meteor-shower';
  if(/meteorite|chelyabinsk|hoba|impactor/.test(n))return 'meteorite';
  if(/kirkwood|trojan|resonance/.test(n))return 'orbital-mechanics';
  return 'asteroid';
}
function bAtmo(s,seed){
  var r=baseRec(seed,'atmosphere',s);
  var atmo=FACTS['Atmosphere']||FACTS['Surface temperature']||'see physical data';
  r.title=BODY+' — atmosphere';
  r.description='Atmosphere of '+BODY+': '+atmo+'. '+(BTYPE==='planet'||BTYPE==='moon'?'Atmospheric science shapes weather, climate, and exploration.':'Stellar atmosphere dynamics drive space weather across the system.');
  r.atmosphere_detail=atmo;
  return r;
}
function bMission(s,seed,kindKey){
  var m=MISSIONS[(seed-1)%MISSIONS.length];
  var r=baseRec(seed,kindKey,s);
  r.title=BODY+' — '+m[0];
  r.description='Exploration record: '+m[0]+' — '+m[1];
  r.mission={name:m[0],description:m[1]};
  return r;
}
function bFuture(s,seed){
  var r=baseRec(seed,'future',s);
  r.src='signature';
  var ideas=['a dedicated orbiter mapping the entire body at sub-meter resolution',
   'a lander or sample-return mission to the most scientifically valuable site',
   'a long-term surface station with in-situ resource utilization',
   'a swarm of small probes surveying the body cooperatively',
   'an international crewed expedition with a permanent research base'];
  var idea=ideas[seed%ideas.length];
  r.title=BODY+' — future concept: '+idea.split(' ').slice(0,4).join(' ')+'...';
  r.description='SPECULATIVE (Signature-authored, not established fact): '+idea+' at '+BODY+'. This is a forward-looking concept for mission planners and dreamers.';
  r.known={note:'No established mission of this exact form has flown.'};
  r.speculative={concept:idea, status:'Signature-authored projection'};
  return r;
}
function generateIndexed(seed){
  var s=prng(seed*2654435761>>>0);
  var k=KINDS[(seed-1)%KINDS.length];
  if(k==='overview'&&seed!==1)k='physical-data';
  if(k==='overview')return bOverview(s,seed);
  if(k==='physical-data')return bPhysical(s,seed);
  if(k==='geology')return bFeature(s,seed,'geology');
  if(k==='solar-layer'||k==='solar-activity')return bFeature(s,seed,k);
  if(k==='asteroid'||k==='comet'||k==='meteor-shower'||k==='meteorite'||k==='orbital-mechanics')return bFeature(s,seed,k);
  if(k==='atmosphere')return bAtmo(s,seed);
  if(k==='exploration')return bMission(s,seed,'exploration');
  if(k==='observation')return bMission(s,seed,'observation');
  if(k==='future')return bFuture(s,seed);
  return bPhysical(s,seed);
}
function generate(seed,opts){
  opts=opts||{};
  var s=prng(seed*40503+7);
  var kind=(opts.kind&&KINDS.indexOf(opts.kind)>=0)?opts.kind:KINDS[(seed-1)%KINDS.length];
  var topic=(opts.topic||'').toString().trim().slice(0,120);
  var r=generateIndexed(seed);
  if(opts.kind&&KINDS.indexOf(opts.kind)>=0){
    var ki=KINDS.indexOf(opts.kind);
    var sk=(opts.kind==='overview')?1:(ki+1+KINDS.length*Math.floor((seed-1)/KINDS.length));
    var keep=r.id;
    r=generateIndexed(sk);
    r.id=keep; r._seed=seed;
  }
  if(topic){r.title=r.title+' — '+topic; r.description=r.description+' Focus: '+topic+'.';}
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var re=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!re.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  if(KINDS.indexOf(r.kind)<0)e.push('kind');
  if(r.src!=='fact'&&r.src!=='signature')e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(x){return x&&x.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-titania-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,kinds:KINDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
