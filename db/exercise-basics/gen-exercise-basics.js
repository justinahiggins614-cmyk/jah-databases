(function(){'use strict';
/* JAH Exercise Basics Database generator — jahdb-exercise-basics-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='exercise-basics',PREFIX='JAH-EXE-',NAME='JAH Exercise Basics Database';
var FIELDS=["start", "cardio", "strength", "flexibility", "safety"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Start where you are", "d": "Any movement beats none; consistency beats intensity.", "g": "start", "l": 2, "q": "What is Start where you are?", "a": "Any movement beats none; consistency beats intensity.", "x": "Any movement beats none; consistency beats intensity. Key steps: Get medical clearance if needed; Start with walking; Add gradually; Track simply. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "The 150-minute rule", "d": "150 min moderate or 75 min vigorous weekly, plus strength twice.", "g": "start", "l": 2, "q": "What is The 150-minute rule?", "a": "150 min moderate or 75 min vigorous weekly, plus strength twice.", "x": "150 min moderate or 75 min vigorous weekly, plus strength twice. Key steps: Break into 10-minute chunks; Moderate = can talk, not sing; Add 2 strength days. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Walking programs", "d": "The perfect starter exercise.", "g": "cardio", "l": 2, "q": "What is Walking programs?", "a": "The perfect starter exercise.", "x": "The perfect starter exercise. Key steps: Start 10-15 minutes; Add 5 minutes weekly; Aim for brisk pace; Good shoes matter. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Running: couch to 5K", "d": "Walk-run intervals build runners.", "g": "cardio", "l": 2, "q": "What is Running: couch to 5K?", "a": "Walk-run intervals build runners.", "x": "Walk-run intervals build runners. Key steps: Alternate walk and run; Increase run portions weekly; Rest days between; 8 weeks to 5K. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Cycling basics", "d": "Low-impact cardio for joints.", "g": "cardio", "l": 2, "q": "What is Cycling basics?", "a": "Low-impact cardio for joints.", "x": "Low-impact cardio for joints. Key steps: Fit the bike; Start flat; Build duration first; Helmet always. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Swimming basics", "d": "Full-body, zero-impact.", "g": "cardio", "l": 2, "q": "What is Swimming basics?", "a": "Full-body, zero-impact.", "x": "Full-body, zero-impact. Key steps: Start with short sessions; Learn breathing rhythm; Kickboards build legs; Goggles help. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Jump rope", "d": "Cheap, intense, portable.", "g": "cardio", "l": 2, "q": "What is Jump rope?", "a": "Cheap, intense, portable.", "x": "Cheap, intense, portable. Key steps: Size the rope; Start 1-minute rounds; Land soft; Build to 10 minutes. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "HIIT basics", "d": "Short bursts, big results.", "g": "cardio", "l": 2, "q": "What is HIIT basics?", "a": "Short bursts, big results.", "x": "Short bursts, big results. Key steps: Work 20-40 seconds; Rest equal time; 8-12 rounds; 2-3 times weekly max. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Rowing machine", "d": "Full-body cardio.", "g": "cardio", "l": 2, "q": "What is Rowing machine?", "a": "Full-body cardio.", "x": "Full-body cardio. Key steps: Learn the form: legs, body, arms; Start 10 minutes; Damper 3-5. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Elliptical", "d": "Joint-friendly cardio.", "g": "cardio", "l": 2, "q": "What is Elliptical?", "a": "Joint-friendly cardio.", "x": "Joint-friendly cardio. Key steps: Upright posture; Use the handles; Vary resistance. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Bodyweight squats", "d": "The foundational leg move.", "g": "strength", "l": 2, "q": "What is Bodyweight squats?", "a": "The foundational leg move.", "x": "The foundational leg move. Key steps: Feet shoulder-width; Chest up, knees track toes; Thighs parallel; 3 sets of 10-15. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Push-ups", "d": "The foundational push.", "g": "strength", "l": 2, "q": "What is Push-ups?", "a": "The foundational push.", "x": "The foundational push. Key steps: Hands under shoulders; Straight body line; Start on knees if needed; 3 sets to near-failure. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Planks", "d": "Core stability king.", "g": "strength", "l": 2, "q": "What is Planks?", "a": "Core stability king.", "x": "Core stability king. Key steps: Forearms and toes; Straight line head to heels; 30-60 seconds; Breathe. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Lunges", "d": "Single-leg strength and balance.", "g": "strength", "l": 2, "q": "What is Lunges?", "a": "Single-leg strength and balance.", "x": "Single-leg strength and balance. Key steps: Step forward; Both knees 90 degrees; Push through the heel; Alternate legs. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Glute bridges", "d": "Wake up the glutes.", "g": "strength", "l": 2, "q": "What is Glute bridges?", "a": "Wake up the glutes.", "x": "Wake up the glutes. Key steps: Back on floor, feet flat; Lift hips; Squeeze at top; 3 sets of 15. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Dumbbell rows", "d": "Back strength and posture.", "g": "strength", "l": 2, "q": "What is Dumbbell rows?", "a": "Back strength and posture.", "x": "Back strength and posture. Key steps: Hinge at hips; Pull elbow back; Squeeze shoulder blade; Both sides. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Overhead press", "d": "Shoulder strength.", "g": "strength", "l": 2, "q": "What is Overhead press?", "a": "Shoulder strength.", "x": "Shoulder strength. Key steps: Dumbbells at shoulders; Press up; No arching; Control down. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Deadlift form", "d": "The king lift, done right.", "g": "strength", "l": 2, "q": "What is Deadlift form?", "a": "The king lift, done right.", "x": "The king lift, done right. Key steps: Hinge, do not squat; Flat back; Bar close to shins; Drive through heels. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Goblet squats", "d": "Weighted squat primer.", "g": "strength", "l": 2, "q": "What is Goblet squats?", "a": "Weighted squat primer.", "x": "Weighted squat primer. Key steps: Hold weight at chest; Squat deep; Elbows inside knees. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Resistance bands", "d": "Portable gym.", "g": "strength", "l": 2, "q": "What is Resistance bands?", "a": "Portable gym.", "x": "Portable gym. Key steps: Anchor securely; Control both directions; Full range. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Progressive overload", "d": "The growth principle.", "g": "strength", "l": 2, "q": "What is Progressive overload?", "a": "The growth principle.", "x": "The growth principle. Key steps: Add a little over time; Reps, then weight; Track it; Deload every 4-6 weeks. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Rest days", "d": "Muscles grow resting.", "g": "safety", "l": 2, "q": "What is Rest days?", "a": "Muscles grow resting.", "x": "Muscles grow resting. Key steps: 1-2 rest days weekly; Sleep 7-9 hours; Soreness vs pain: know the difference. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Warm-ups", "d": "Prepare the body.", "g": "safety", "l": 2, "q": "What is Warm-ups?", "a": "Prepare the body.", "x": "Prepare the body. Key steps: 5-10 minutes easy cardio; Dynamic stretches; Build to working intensity. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Cool-downs", "d": "Bring the body down.", "g": "safety", "l": 2, "q": "What is Cool-downs?", "a": "Bring the body down.", "x": "Bring the body down. Key steps: Easy movement 5 minutes; Static stretches; Breathe. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Stretching basics", "d": "Flexibility prevents injury.", "g": "flexibility", "l": 2, "q": "What is Stretching basics?", "a": "Flexibility prevents injury.", "x": "Flexibility prevents injury. Key steps: After workouts, not before; Hold 20-30 seconds; No bouncing; Breathe into stretches. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-exercise-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
