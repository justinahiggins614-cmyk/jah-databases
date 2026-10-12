(function(){'use strict';
/* Signature Weird Science Database generator — jahdb-weird-science-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-WEIRD-SCI-';
var TOPICS=[["Tardigrades: The Indestructible Micro-Animal", "Water bears survive the vacuum of space, lethal radiation, and decades without water; scientists study their damage-suppressor proteins for medical applications."], ["The Immortal Jellyfish", "Turritopsis dohrnii can revert to its polyp stage and begin life again; researchers study its transdifferentiation for aging science."], ["Ball Lightning Reports", "Witnesses describe glowing spheres during thunderstorms; physicists have proposed plasma, silicon-vapor, and microwave theories without consensus."], ["The Placebo Effect's Strange Power", "Inert treatments can produce real physiological changes; neuroimaging shows genuine brain activity behind placebo pain relief."], ["Quantum Entanglement at a Distance", "Particles remain correlated across vast distances in ways Einstein called 'spooky'; experiments have confirmed the effect repeatedly."], ["Time Dilation Is Real", "GPS satellites must correct for relativity daily; astronauts age slightly slower than people on Earth."], ["The Mpemba Effect", "Hot water can freeze faster than cold under some conditions; physicists still debate the exact mechanism."], ["Slime Mold Problem-Solving", "Brainless Physarum polycephalum finds shortest paths through mazes; engineers borrow its strategies for network design."], ["Bioluminescent Waves", "Dinoflagellates light up surf with blue flashes when disturbed; the chemistry involves luciferin reactions tuned by evolution."], ["The Hum of the Earth", "Seismometers detect a constant low-frequency planetary hum; researchers attribute it to ocean waves coupling with the seafloor."], ["Spontaneous Human Levitation Claims", "Saints and mystics were reported to float; stage magicians replicate the effect with hidden supports, and no case has survived controlled testing."], ["Fire Rainbows and Sun Dogs", "Ice-crystal optics paint halos and arcs across the sky; atmospheric physicists can reproduce every form in the lab."], ["The Blue Hole Optical Illusions", "Deep ocean sinkholes create startling color contrasts; divers study their unique chemistry and fossil records."], ["Blood Falls of Antarctica", "Iron-rich brine oxidizes into a red waterfall at Taylor Glacier; the source is a subglacial lake sealed for millennia."], ["Singing Sand Dunes", "Some dunes boom like low organ notes when sand avalanches; the frequency depends on grain size and humidity."], ["Catatumbo Lightning", "A Venezuelan river mouth sees lightning up to 300 nights a year; methane and topography create the storm factory."], ["The Sailing Stones of Death Valley", "Rocks glide across Racetrack Playa leaving trails; time-lapse cameras proved thin ice sheets push them on windy nights."], ["Eternal Flames and Natural Gas Seeps", "Fires burn for centuries above gas vents in places like Azerbaijan; geologists map them as surface expressions of deep reservoirs."], ["The Giant's Causeway Geometry", "Hexagonal basalt columns formed as lava cooled and contracted; the same physics appears in dried mud and corn starch."], ["Aurora Sounds", "Some observers report crackling during auroras; Finnish researchers recorded audible claps linked to temperature inversions."], ["The Bloop Revisited", "Once a mystery, the 1997 sound is now attributed to icequakes; it shows how new data can dissolve old puzzles."], ["Infrasound and Ghost Feelings", "Low-frequency sound can induce unease and visual artifacts; researchers link some 'haunted' sensations to standing infrasound waves."], ["The Taos Hum Investigation", "A New Mexico town's reported hum drew acoustic teams; some hearers matched it to local equipment, others never found a source."], ["Synchronous Fireflies", "Thousands of fireflies flash in unison in Southeast Asia; mathematicians model it as coupled oscillators, like applause synchronizing."], ["The Coriolis Misconception", "Bathtub drains don't reliably spin by hemisphere; the real Coriolis effect needs hurricane-scale distances to dominate."], ["Ferrofluids: Liquid That Dances", "Magnetic nanoparticles in oil spike into hedgehogs under magnets; artists and engineers both exploit the effect."], ["Non-Newtonian Oobleck", "Cornstarch and water flows like liquid but shatters like solid under impact; the shear-thickening physics now informs body armor."], ["Sonoluminescence", "Sound waves can make bubbles collapse into flashes of light; the mechanism involves plasma hotter than the sun's surface."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'weird science exploration', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('weird-science',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();