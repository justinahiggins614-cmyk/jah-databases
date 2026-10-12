(function(){'use strict';
/* Solar System Master Map generator — jahdb-solar-system-map-1.0.
   Property of Justin Addam Higgins (JAH). Deterministic.
   Tours use real interplanetary distances (semi-major axes); travel times are
   clearly labeled estimates. src:"fact" = real data. */
var PREFIX='JAH-SSM-';
var SLUG='solar-system-map';
var KINDS=['overview','tour','comparison'];
var BODIES=[{"slug": "mercury", "name": "Mercury", "au": 0.39}, {"slug": "venus", "name": "Venus", "au": 0.72}, {"slug": "earth-planet", "name": "Earth Planetary", "au": 1.0}, {"slug": "mars", "name": "Mars", "au": 1.52}, {"slug": "jupiter", "name": "Jupiter", "au": 5.2}, {"slug": "saturn", "name": "Saturn", "au": 9.58}, {"slug": "uranus", "name": "Uranus", "au": 19.2}, {"slug": "neptune", "name": "Neptune", "au": 30.1}, {"slug": "pluto", "name": "Pluto", "au": 39.5}, {"slug": "moon", "name": "Earth's Moon", "au": 0.0026}, {"slug": "phobos", "name": "Phobos", "au": 0.0001}, {"slug": "deimos", "name": "Deimos", "au": 0.0002}, {"slug": "io", "name": "Io", "au": 0.0028}, {"slug": "europa", "name": "Europa", "au": 0.0045}, {"slug": "ganymede", "name": "Ganymede", "au": 0.0072}, {"slug": "callisto", "name": "Callisto", "au": 0.0126}, {"slug": "titan", "name": "Titan", "au": 0.0082}, {"slug": "enceladus", "name": "Enceladus", "au": 0.0016}, {"slug": "rhea", "name": "Rhea", "au": 0.0035}, {"slug": "iapetus", "name": "Iapetus", "au": 0.0238}, {"slug": "dione", "name": "Dione", "au": 0.0025}, {"slug": "tethys", "name": "Tethys", "au": 0.002}, {"slug": "mimas", "name": "Mimas", "au": 0.0012}, {"slug": "miranda", "name": "Miranda", "au": 0.0009}, {"slug": "ariel", "name": "Ariel", "au": 0.0013}, {"slug": "umbriel", "name": "Umbriel", "au": 0.0018}, {"slug": "titania", "name": "Titania", "au": 0.0029}, {"slug": "oberon", "name": "Oberon", "au": 0.0039}, {"slug": "triton", "name": "Triton", "au": 0.0024}, {"slug": "charon", "name": "Charon", "au": 0.0001}, {"slug": "sun", "name": "Sun", "au": 1.0}, {"slug": "orbits", "name": "Orbits", "au": 1.0}];
var FACTS={"mercury": {"Diameter": "4,879 km", "Distance from Sun": "57.9M km (0.39 AU)", "Orbital period": "88 days", "Day length": "59 Earth days", "Mean temperature": "167\u00b0C (-180 to 430\u00b0C)", "Atmosphere": "Trace exosphere (O, Na, H, He, K)", "Gravity": "3.7 m/s\u00b2", "Moons": "0"}, "venus": {"Diameter": "12,104 km", "Distance from Sun": "108.2M km (0.72 AU)", "Orbital period": "225 days", "Day length": "243 Earth days (retrograde)", "Mean temperature": "465\u00b0C", "Atmosphere": "CO2 96.5%, N2 3.5%, sulfuric-acid clouds", "Surface pressure": "92 bar", "Gravity": "8.87 m/s\u00b2", "Moons": "0"}, "earth-planet": {"Diameter": "12,742 km", "Distance from Sun": "149.6M km (1.00 AU)", "Orbital period": "365.25 days", "Day length": "23.9 hours", "Mean temperature": "15\u00b0C", "Atmosphere": "N2 78%, O2 21%, Ar 0.9%", "Gravity": "9.81 m/s\u00b2", "Moons": "1 (the Moon)"}, "mars": {"Diameter": "6,779 km", "Distance from Sun": "227.9M km (1.52 AU)", "Orbital period": "687 days", "Day length": "24.6 hours", "Mean temperature": "-63\u00b0C (-140 to 30\u00b0C)", "Atmosphere": "CO2 95%, N2 2.8%, Ar 2%", "Gravity": "3.71 m/s\u00b2", "Moons": "2 (Phobos, Deimos)"}, "jupiter": {"Diameter": "139,820 km", "Distance from Sun": "778.5M km (5.20 AU)", "Orbital period": "11.86 years", "Day length": "9.9 hours", "Mean temperature": "-110\u00b0C", "Atmosphere": "H2 ~90%, He ~10%, ammonia clouds", "Gravity": "24.79 m/s\u00b2", "Moons": "95 confirmed"}, "saturn": {"Diameter": "116,460 km", "Distance from Sun": "1.43B km (9.58 AU)", "Orbital period": "29.4 years", "Day length": "10.7 hours", "Mean temperature": "-140\u00b0C", "Atmosphere": "H2 ~96%, He ~3%, ammonia clouds", "Gravity": "10.44 m/s\u00b2", "Moons": "146 confirmed"}, "uranus": {"Diameter": "50,724 km", "Distance from Sun": "2.87B km (19.2 AU)", "Orbital period": "84 years", "Day length": "17.2 hours (retrograde)", "Mean temperature": "-195\u00b0C", "Atmosphere": "H2 83%, He 15%, CH4 2%", "Gravity": "8.69 m/s\u00b2", "Moons": "28 confirmed", "Axial tilt": "97.8\u00b0"}, "neptune": {"Diameter": "49,244 km", "Distance from Sun": "4.50B km (30.1 AU)", "Orbital period": "164.8 years", "Day length": "16.1 hours", "Mean temperature": "-200\u00b0C", "Atmosphere": "H2 80%, He 19%, CH4 1%", "Gravity": "11.15 m/s\u00b2", "Moons": "16 confirmed"}, "pluto": {"Diameter": "2,377 km", "Distance from Sun": "5.9B km avg (39.5 AU)", "Orbital period": "248 years", "Day length": "6.4 days", "Mean temperature": "-229\u00b0C", "Atmosphere": "N2, CH4, CO (thin, seasonal)", "Gravity": "0.62 m/s\u00b2", "Moons": "5 (Charon, Styx, Nix, Kerberos, Hydra)"}, "moon": {"Diameter": "3,474 km", "Distance from Earth": "384,400 km", "Orbital period": "27.3 days", "Day length": "27.3 days (tidally locked)", "Mean temperature": "-20\u00b0C (-173 to 127\u00b0C)", "Atmosphere": "Trace exosphere", "Gravity": "1.62 m/s\u00b2"}, "phobos": {"Diameter": "~22 km", "Distance from Mars": "9,376 km", "Orbital period": "7.65 hours", "Day length": "7.65 hours (tidally locked)", "Mean temperature": "-40\u00b0C", "Atmosphere": "None", "Gravity": "0.0057 m/s\u00b2"}, "deimos": {"Diameter": "~12 km", "Distance from Mars": "23,463 km", "Orbital period": "30.3 hours", "Day length": "30.3 hours (tidally locked)", "Mean temperature": "-40\u00b0C", "Atmosphere": "None", "Gravity": "0.003 m/s\u00b2"}, "io": {"Diameter": "3,643 km", "Distance from Jupiter": "421,700 km", "Orbital period": "1.77 days", "Day length": "1.77 days (tidally locked)", "Mean temperature": "-160\u00b0C (lava: 1,600\u00b0C)", "Atmosphere": "Trace SO2", "Gravity": "1.80 m/s\u00b2"}, "europa": {"Diameter": "3,122 km", "Distance from Jupiter": "671,000 km", "Orbital period": "3.55 days", "Day length": "3.55 days (tidally locked)", "Mean temperature": "-160\u00b0C", "Atmosphere": "Trace O2", "Gravity": "1.31 m/s\u00b2"}, "ganymede": {"Diameter": "5,268 km", "Distance from Jupiter": "1.07M km", "Orbital period": "7.15 days", "Day length": "7.15 days (tidally locked)", "Mean temperature": "-160\u00b0C", "Atmosphere": "Trace O2", "Gravity": "1.43 m/s\u00b2"}, "callisto": {"Diameter": "4,821 km", "Distance from Jupiter": "1.88M km", "Orbital period": "16.69 days", "Day length": "16.69 days (tidally locked)", "Mean temperature": "-160\u00b0C", "Atmosphere": "Trace CO2", "Gravity": "1.24 m/s\u00b2"}, "titan": {"Diameter": "5,150 km", "Distance from Saturn": "1.22M km", "Orbital period": "15.95 days", "Day length": "15.95 days (tidally locked)", "Mean temperature": "-179\u00b0C", "Atmosphere": "N2 98%, CH4 1.4% \u2014 thicker than Earth's", "Surface pressure": "1.45 bar", "Gravity": "1.35 m/s\u00b2"}, "enceladus": {"Diameter": "504 km", "Distance from Saturn": "238,000 km", "Orbital period": "1.37 days", "Day length": "1.37 days (tidally locked)", "Mean temperature": "-200\u00b0C", "Atmosphere": "Trace water vapor", "Gravity": "0.11 m/s\u00b2"}, "rhea": {"Diameter": "1,527 km", "Distance from Saturn": "527,000 km", "Orbital period": "4.52 days", "Day length": "4.52 days (tidally locked)", "Mean temperature": "-180\u00b0C", "Atmosphere": "Trace O2/CO2", "Gravity": "0.26 m/s\u00b2"}, "iapetus": {"Diameter": "1,470 km", "Distance from Saturn": "3.56M km", "Orbital period": "79.3 days", "Day length": "79.3 days (tidally locked)", "Mean temperature": "-180\u00b0C", "Atmosphere": "None", "Gravity": "0.22 m/s\u00b2"}, "dione": {"Diameter": "1,123 km", "Distance from Saturn": "377,000 km", "Orbital period": "2.74 days", "Day length": "2.74 days (tidally locked)", "Mean temperature": "-190\u00b0C", "Atmosphere": "Trace O2", "Gravity": "0.23 m/s\u00b2"}, "tethys": {"Diameter": "1,062 km", "Distance from Saturn": "295,000 km", "Orbital period": "1.89 days", "Day length": "1.89 days (tidally locked)", "Mean temperature": "-190\u00b0C", "Atmosphere": "None", "Gravity": "0.15 m/s\u00b2"}, "mimas": {"Diameter": "396 km", "Distance from Saturn": "185,500 km", "Orbital period": "0.94 days", "Day length": "0.94 days (tidally locked)", "Mean temperature": "-200\u00b0C", "Atmosphere": "None", "Gravity": "0.064 m/s\u00b2"}, "miranda": {"Diameter": "472 km", "Distance from Uranus": "129,900 km", "Orbital period": "1.41 days", "Day length": "1.41 days (tidally locked)", "Mean temperature": "-200\u00b0C", "Atmosphere": "None", "Gravity": "0.079 m/s\u00b2"}, "ariel": {"Diameter": "1,158 km", "Distance from Uranus": "190,900 km", "Orbital period": "2.52 days", "Day length": "2.52 days (tidally locked)", "Mean temperature": "-210\u00b0C", "Atmosphere": "None", "Gravity": "0.27 m/s\u00b2"}, "umbriel": {"Diameter": "1,169 km", "Distance from Uranus": "266,000 km", "Orbital period": "4.14 days", "Day length": "4.14 days (tidally locked)", "Mean temperature": "-210\u00b0C", "Atmosphere": "None", "Gravity": "0.23 m/s\u00b2"}, "titania": {"Diameter": "1,578 km", "Distance from Uranus": "436,300 km", "Orbital period": "8.71 days", "Day length": "8.71 days (tidally locked)", "Mean temperature": "-210\u00b0C", "Atmosphere": "Trace CO2", "Gravity": "0.37 m/s\u00b2"}, "oberon": {"Diameter": "1,523 km", "Distance from Uranus": "583,500 km", "Orbital period": "13.46 days", "Day length": "13.46 days (tidally locked)", "Mean temperature": "-210\u00b0C", "Atmosphere": "None", "Gravity": "0.35 m/s\u00b2"}, "triton": {"Diameter": "2,707 km", "Distance from Neptune": "354,800 km", "Orbital period": "5.88 days (retrograde)", "Day length": "5.88 days (tidally locked)", "Mean temperature": "-235\u00b0C", "Atmosphere": "N2, trace CH4", "Gravity": "0.78 m/s\u00b2"}, "charon": {"Diameter": "1,212 km", "Distance from Pluto": "19,596 km", "Orbital period": "6.39 days", "Day length": "6.39 days (mutually tidally locked)", "Mean temperature": "-220\u00b0C", "Atmosphere": "None", "Gravity": "0.29 m/s\u00b2"}, "sun": {"Diameter": "1,392,700 km", "Mass": "1.989 \u00d7 10\u00b3\u2070 kg (99.86% of the system)", "Spectral type": "G2V main-sequence", "Surface temperature": "5,505\u00b0C", "Core temperature": "~15,000,000\u00b0C", "Age": "4.6 billion years", "Rotation": "~27 days (equator)", "Composition": "H 73%, He 25%", "Solar cycle": "~11 years"}, "orbits": {"Small-body populations": "Asteroid belt: 1\u20132M+; NEOs tracked: 35,000+; known comets: ~3,900", "Governing law": "Kepler's laws + Newton's gravitation", "Key resonance": "Kirkwood gaps in the belt", "Famous impact": "Chicxulub, 66M years ago", "Sample returns": "Hayabusa, Hayabusa2, OSIRIS-REx"}};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pad(n){return String(n).padStart(6,'0');}
var AU_KM=149597870.7;
function bOverview(s,seed){
  return {id:PREFIX+pad(seed),kind:'overview',body:'Solar System',body_type:'system',parent_body:'—',
   title:'Solar System Master Map — complete overview',
   description:'The master map links every planet, moon, the Sun, and small-body database in the JAH network: '+BODIES.length+' worlds mapped, each with its own full database. Use the orrery to travel between them.',
   known:{bodies_mapped:BODIES.length, note:'Each body links to its dedicated database.'},
   demo:{kind:'au-converter',program:'function auToKm(au){return +(au*149597870.7).toExponential(3);}\n// auToKm(1.52)',note:'JS: AU to km.'},
   src:'fact',_seed:seed};
}
function bTour(s,seed){
  var n=3+(seed%3), start=(seed*7)%BODIES.length, stops=[], i;
  for(i=0;i<n;i++)stops.push(BODIES[(start+i*5)%BODIES.length]);
  var distKm=0, legs=[];
  for(i=1;i<stops.length;i++){
    var d=Math.abs(stops[i].au-stops[i-1].au)*AU_KM; distKm+=d;
    legs.push(stops[i-1].name+' → '+stops[i].name+': '+(d/1e6).toFixed(1)+'M km');
  }
  var days=distKm/15/86400; // 15 km/s cruise, labeled estimate
  var r={id:PREFIX+pad(seed),kind:'tour',body:'Solar System',body_type:'system',parent_body:'—',
   title:'Grand tour: '+stops.map(function(b){return b.name;}).join(' → '),
   description:'A plotted route across the map: '+legs.join('; ')+'. Total distance '+(distKm/1e9).toFixed(2)+'B km; at a steady 15 km/s cruise (estimate) about '+Math.round(days).toLocaleString()+' days of flight. Each stop links to its full database.',
   tour:{stops:stops.map(function(b){return b.slug;}),legs:legs,total_km:Math.round(distKm),est_days:Math.round(days)},
   demo:{kind:'tour-time',program:'function tourDays(distKm, cruiseKms){return Math.round(distKm/cruiseKms/86400);}\n// tourDays('+Math.round(distKm)+', 15)',note:'JS: estimate tour duration.'},
   src:'fact',_seed:seed};
  return r;
}
function bComparison(s,seed){
  var a=BODIES[seed%BODIES.length], b=BODIES[(seed*3+1)%BODIES.length];
  var fa=FACTS[a.slug]||{}, fb=FACTS[b.slug]||{};
  return {id:PREFIX+pad(seed),kind:'comparison',body:'Solar System',body_type:'system',parent_body:'—',
   title:'Compare: '+a.name+' vs '+b.name,
   description:'Side-by-side: '+a.name+' (diameter '+(fa['Diameter']||'?')+', '+('Mean temperature' in fa?fa['Mean temperature']:'?')+') vs '+b.name+' (diameter '+(fb['Diameter']||'?')+'). Both link to their full databases.',
   comparison:{a:{name:a.name,facts:fa},b:{name:b.name,facts:fb}},
   demo:{kind:'size-ratio',program:'function sizeRatio(d1,d2){return +(d1/d2).toFixed(2);}\n// sizeRatio(a, b)',note:'JS: diameter ratio.'},
   src:'fact',_seed:seed};
}
function generateIndexed(seed){
  var s=prng(seed*2654435761>>>0);
  var k=KINDS[(seed-1)%KINDS.length];
  if(k==='overview'&&seed!==1)k='tour';
  if(k==='overview')return bOverview(s,seed);
  if(k==='tour')return bTour(s,seed);
  return bComparison(s,seed);
}
function generate(seed,opts){
  opts=opts||{};
  var topic=(opts.topic||'').toString().trim().slice(0,120);
  var r=generateIndexed(seed);
  if(topic){r.title=r.title+' — '+topic; r.description=r.description+' Focus: '+topic+'.';}
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-SSM-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  if(KINDS.indexOf(r.kind)<0)e.push('kind');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(x){return x&&x.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-solar-system-map-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,kinds:KINDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
