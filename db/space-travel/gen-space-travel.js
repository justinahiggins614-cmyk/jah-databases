(function(){'use strict';
/* Signature Space Travel Database generator — jahdb-space-travel-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SPACE-TRAV-';
var TOPICS=[["Starship and Reusable Heavy Lift", "Fully reusable rockets aim to slash launch costs; the test program iterates rapidly."], ["Artemis: Return to the Moon", "NASA's program targets a sustainable lunar presence; international partners share the manifest."], ["Lunar Gateway Station", "A small station will orbit the Moon; it serves as a staging point for surface missions."], ["Mars Sample Return", "Fetching Martian rocks is scientifically priceless; the mission's cost keeps growing."], ["Nuclear Thermal Propulsion", "Nuclear rockets could halve Mars transit time; the technology was tested in the 1960s."], ["Ion Drives and Electric Propulsion", "Efficient thrusters already propel probes; scaling them for crews is the challenge."], ["Solar Sails", "Light pressure can push spacecraft; demonstrators have flown successfully."], ["Space Elevators: The Physics", "A tether to orbit needs materials beyond current strength; carbon nanotubes aren't quite there."], ["Rotating Space Stations", "Artificial gravity via spin is well understood; no one has built a large one yet."], ["Orbital Habitats", "Commercial stations plan to replace the ISS; the business case is still forming."], ["Lunar Mining", "Water ice at the poles could fuel rockets; prospecting missions are queued."], ["Asteroid Mining Economics", "Trillion-dollar asteroid valuations ignore market flooding; the first ventures target water."], ["Space Tourism's Trajectory", "Suborbital hops became routine for the wealthy; orbital tourism grows slowly."], ["The Overview Effect", "Astronauts report profound perspective shifts; psychologists study the phenomenon."], ["Radiation: The Mars Problem", "Cosmic rays threaten long missions; shielding solutions add mass."], ["Closed-Loop Life Support", "Recycling air and water is essential; the ISS recovers most of its water."], ["Growing Food in Space", "Lettuce grows on the ISS; staple crops need far more energy."], ["Hibernation for Deep Space", "Torpor could cut mission costs; medical researchers study therapeutic hypothermia."], ["Interstellar Probes", "Breakthrough Starshot proposes laser-pushed chips to Alpha Centauri; the physics is sound, the engineering extreme."], ["Generation Ships", "Multi-century voyages need self-sustaining societies; the sociology is harder than the rockets."], ["Terraforming Mars: Realistic?", "Thickening Mars's atmosphere looks infeasible; local domes are the practical path."], ["The Outer Planets Missions", "Probes to Europa and Enceladus hunt oceans; launch windows are rare."], ["Space Debris Crisis", "Trackable debris threatens orbits; cleanup missions are finally launching."], ["Space Traffic Management", "Thousands of new satellites need coordination; regulation is catching up."], ["The Militarization Question", "Anti-satellite tests create debris; treaties lag the technology."], ["First Contact Protocols", "Astronauts have no official alien-contact playbook; scientists have drafted proposals."], ["The Cost Curve", "Launch costs fell 10x in a decade; the trend enables everything else."], ["Humanity's Multiplanetary Future", "Advocates argue survival demands spreading out; critics say fix Earth first."]];
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
    type:'space travel exploration', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('space-travel',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();