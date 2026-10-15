(function(){'use strict';
/* Public Engineering Database generator — jahdb-engineering-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ENG-PUB-';
var TOPICS=[["Statics", "Forces in equilibrium; trusses and frames."], ["Dynamics", "Motion of bodies under forces; kinetics and kinematics."], ["Mechanics of Materials", "Stress, strain, and material deformation."], ["Thermodynamics", "Energy, heat engines, and cycles."], ["Fluid Mechanics", "Behavior of liquids and gases in motion and at rest."], ["Electrical Circuits", "Voltage, current, resistance, and circuit analysis."], ["Control Systems", "Feedback, stability, and PID control."], ["Materials Science", "Properties and selection of engineering materials."], ["Manufacturing", "Machining, casting, forming, and additive processes."], ["CAD", "Computer-aided design and technical drawing."], ["Structural Engineering", "Designing buildings and bridges to carry loads."], ["Civil Engineering", "Infrastructure: roads, water, and public works."], ["Mechanical Engineering", "Machines, mechanisms, and mechanical design."], ["Electrical Engineering", "Power, electronics, and signal systems."], ["Chemical Engineering", "Process design, reactors, and separations."], ["Aerospace Engineering", "Flight, rockets, and spacecraft design."], ["Robotics", "Kinematics, sensors, actuators, and control."], ["Systems Engineering", "Managing complex projects from requirements to delivery."], ["Engineering Ethics", "Safety, responsibility, and professional standards."], ["Prototyping", "From sketch to working model quickly."], ["Testing and Validation", "Proving designs work under real conditions."], ["Failure Analysis", "Learning from broken parts and accidents."], ["Technical Drawing", "Reading and creating engineering drawings."], ["Measurement", "Calipers, micrometers, and precision measurement."], ["Project Management", "Scheduling, budgets, and engineering teamwork."]];
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
    type:'engineering knowledge record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('engineering-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();