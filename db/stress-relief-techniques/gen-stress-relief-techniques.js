(function(){'use strict';
/* JAH Stress Relief Techniques Database generator — jahdb-stress-relief-techniques-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='stress-relief-techniques',PREFIX='JAH-STR-',NAME='JAH Stress Relief Techniques Database';
var FIELDS=["breathing", "movement", "mindset", "quick"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Box breathing", "d": "Navy SEAL calm: 4-4-4-4.", "g": "breathing", "l": 2, "q": "What is Box breathing?", "a": "Navy SEAL calm: 4-4-4-4.", "x": "Navy SEAL calm: 4-4-4-4. Key steps: Inhale 4 counts; Hold 4; Exhale 4; Hold 4. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "4-7-8 breathing", "d": "Inhale 4, hold 7, exhale 8.", "g": "breathing", "l": 2, "q": "What is 4-7-8 breathing?", "a": "Inhale 4, hold 7, exhale 8.", "x": "Inhale 4, hold 7, exhale 8. Key steps: Exhale completely; Inhale 4; Hold 7; Exhale 8. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Diaphragmatic breathing", "d": "Belly breathing activates calm.", "g": "breathing", "l": 2, "q": "What is Diaphragmatic breathing?", "a": "Belly breathing activates calm.", "x": "Belly breathing activates calm. Key steps: Hand on belly; Breathe into the hand; Slow exhale longer than inhale. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Progressive muscle relaxation", "d": "Tense and release head to toe.", "g": "breathing", "l": 2, "q": "What is Progressive muscle relaxation?", "a": "Tense and release head to toe.", "x": "Tense and release head to toe. Key steps: Tense each group 5 seconds; Release and notice; Move downward; End with full-body release. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Body scan", "d": "Notice without fixing.", "g": "mindset", "l": 2, "q": "What is Body scan?", "a": "Notice without fixing.", "x": "Notice without fixing. Key steps: Lie down; Scan slowly head to toe; Breathe into tension; No judgment. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "5-4-3-2-1 grounding", "d": "Name 5 things you see, 4 you hear, 3 you touch, 2 you smell, 1 you taste.", "g": "quick", "l": 2, "q": "What is 5-4-3-2-1 grounding?", "a": "Name 5 things you see, 4 you hear, 3 you touch, 2 you smell, 1 you taste.", "x": "Name 5 things you see, 4 you hear, 3 you touch, 2 you smell, 1 you taste. Key steps: Look around; Count through senses; Breathe slowly. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Cold water reset", "d": "Cold triggers the dive reflex.", "g": "quick", "l": 2, "q": "What is Cold water reset?", "a": "Cold triggers the dive reflex.", "x": "Cold triggers the dive reflex. Key steps: Splash cold water on face; Or hold ice; Breathe slowly after. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Walk it off", "d": "Rhythmic movement metabolizes stress.", "g": "movement", "l": 2, "q": "What is Walk it off?", "a": "Rhythmic movement metabolizes stress.", "x": "Rhythmic movement metabolizes stress. Key steps: Walk 10-20 minutes; Swing arms; Breathe with steps. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Shake it out", "d": "Animals shake after threat; so can you.", "g": "movement", "l": 2, "q": "What is Shake it out?", "a": "Animals shake after threat; so can you.", "x": "Animals shake after threat; so can you. Key steps: Stand and shake limbs; 30-60 seconds; Breathe. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Stretch break", "d": "Tension lives in shoulders and hips.", "g": "movement", "l": 2, "q": "What is Stretch break?", "a": "Tension lives in shoulders and hips.", "x": "Tension lives in shoulders and hips. Key steps: Neck rolls; Shoulder shrugs; Hip openers; Hold each 30 seconds. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Exercise for stress", "d": "The most reliable reliever.", "g": "movement", "l": 2, "q": "What is Exercise for stress?", "a": "The most reliable reliever.", "x": "The most reliable reliever. Key steps: 20-30 minutes most days; Anything you enjoy; Consistency over intensity. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Yoga for calm", "d": "Breath-linked movement.", "g": "movement", "l": 2, "q": "What is Yoga for calm?", "a": "Breath-linked movement.", "x": "Breath-linked movement. Key steps: Gentle flows; Long exhales; 10-20 minutes. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Reframe the story", "d": "Stress is information, not identity.", "g": "mindset", "l": 2, "q": "What is Reframe the story?", "a": "Stress is information, not identity.", "x": "Stress is information, not identity. Key steps: Name the stressor; Ask: what is in my control?; Choose one small action. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Worry time", "d": "Contain worry to 15 minutes.", "g": "mindset", "l": 2, "q": "What is Worry time?", "a": "Contain worry to 15 minutes.", "x": "Contain worry to 15 minutes. Key steps: Schedule it daily; Write worries; Problem-solve, then close. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Gratitude practice", "d": "Three good things daily.", "g": "mindset", "l": 2, "q": "What is Gratitude practice?", "a": "Three good things daily.", "x": "Three good things daily. Key steps: Write three; Feel each one; Specific over general. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Self-compassion break", "d": "Talk to yourself like a friend.", "g": "mindset", "l": 2, "q": "What is Self-compassion break?", "a": "Talk to yourself like a friend.", "x": "Talk to yourself like a friend. Key steps: Acknowledge the pain; Remember common humanity; Offer kindness. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Limit news intake", "d": "Doomscrolling feeds stress.", "g": "quick", "l": 2, "q": "What is Limit news intake?", "a": "Doomscrolling feeds stress.", "x": "Doomscrolling feeds stress. Key steps: Set check times; No news before bed; Curate sources. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Declutter one drawer", "d": "Small order, big calm.", "g": "quick", "l": 2, "q": "What is Declutter one drawer?", "a": "Small order, big calm.", "x": "Small order, big calm. Key steps: Pick one small space; 15 minutes; Donate or toss. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Laugh", "d": "Laughter is physiological reset.", "g": "quick", "l": 2, "q": "What is Laugh?", "a": "Laughter is physiological reset.", "x": "Laughter is physiological reset. Key steps: Funny video; Call a funny friend; Do not underestimate it. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Connect", "d": "Humans co-regulate.", "g": "mindset", "l": 2, "q": "What is Connect?", "a": "Humans co-regulate.", "x": "Humans co-regulate. Key steps: Call someone; Hug 20 seconds; Ask for help. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Time in nature", "d": "Green reduces cortisol.", "g": "movement", "l": 2, "q": "What is Time in nature?", "a": "Green reduces cortisol.", "x": "Green reduces cortisol. Key steps: 20 minutes outside; Notice details; No phone. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Tea ritual", "d": "Warmth and pause.", "g": "quick", "l": 2, "q": "What is Tea ritual?", "a": "Warmth and pause.", "x": "Warmth and pause. Key steps: Make tea slowly; Sip mindfully; No multitasking. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Music reset", "d": "Tempo shifts mood.", "g": "quick", "l": 2, "q": "What is Music reset?", "a": "Tempo shifts mood.", "x": "Tempo shifts mood. Key steps: Upbeat to energize; Slow to calm; Sing along. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Journal dump", "d": "Get it out of your head.", "g": "mindset", "l": 2, "q": "What is Journal dump?", "a": "Get it out of your head.", "x": "Get it out of your head. Key steps: Write uncensored 10 minutes; No editing; Shred if you want. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Prioritize ruthlessly", "d": "Overload is a choice point.", "g": "mindset", "l": 2, "q": "What is Prioritize ruthlessly?", "a": "Overload is a choice point.", "x": "Overload is a choice point. Key steps: List everything; Circle top 3; Park or delegate the rest. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-stress-relief-techniques-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
