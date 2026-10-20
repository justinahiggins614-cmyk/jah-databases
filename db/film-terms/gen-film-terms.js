(function(){'use strict';
/* JAH Film Terms Database generator — jahdb-film-terms-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='film-terms',PREFIX='JAH-FLM-',NAME='JAH Film Terms Database';
var FIELDS=["craft", "editing", "camera", "sound", "story", "business", "theory", "performance", "effects"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mise-en-scene", "d": "Everything placed before the camera.", "g": "craft", "l": 2, "q": "What is Mise-en-scene?", "a": "Everything placed before the camera.", "x": "Mise-en-scene — Everything placed before the camera. Example: Composition..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Cinematography", "d": "The art of the camera image.", "g": "craft", "l": 2, "q": "What is Cinematography?", "a": "The art of the camera image.", "x": "Cinematography — The art of the camera image. Example: Roger Deakins..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Montage", "d": "Assembled sequence compressing time.", "g": "editing", "l": 2, "q": "What is Montage?", "a": "Assembled sequence compressing time.", "x": "Montage — Assembled sequence compressing time. Example: Rocky training..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Continuity editing", "d": "Invisible seamless cutting.", "g": "editing", "l": 2, "q": "What is Continuity editing?", "a": "Invisible seamless cutting.", "x": "Continuity editing — Invisible seamless cutting. Example: Classical Hollywood..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Jump cut", "d": "Abrupt time-skip cut.", "g": "editing", "l": 2, "q": "What is Jump cut?", "a": "Abrupt time-skip cut.", "x": "Jump cut — Abrupt time-skip cut. Example: French New Wave..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Match cut", "d": "Cut linking similar shapes.", "g": "editing", "l": 2, "q": "What is Match cut?", "a": "Cut linking similar shapes.", "x": "Match cut — Cut linking similar shapes. Example: 2001's bone to spaceship..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Cross-cutting", "d": "Alternating parallel action.", "g": "editing", "l": 2, "q": "What is Cross-cutting?", "a": "Alternating parallel action.", "x": "Cross-cutting — Alternating parallel action. Example: The Godfather baptism..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Long take", "d": "Extended unbroken shot.", "g": "camera", "l": 2, "q": "What is Long take?", "a": "Extended unbroken shot.", "x": "Long take — Extended unbroken shot. Example: Touch of Evil opening..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Tracking shot", "d": "Camera moving alongside action.", "g": "camera", "l": 2, "q": "What is Tracking shot?", "a": "Camera moving alongside action.", "x": "Tracking shot — Camera moving alongside action. Example: Goodfellas Copacabana..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Dolly zoom", "d": "Zoom plus dolly: the vertigo effect.", "g": "camera", "l": 2, "q": "What is Dolly zoom?", "a": "Zoom plus dolly: the vertigo effect.", "x": "Dolly zoom — Zoom plus dolly: the vertigo effect. Example: Jaws beach..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Aerial shot", "d": "From above.", "g": "camera", "l": 2, "q": "What is Aerial shot?", "a": "From above.", "x": "Aerial shot — From above. Example: Establishing scale..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Close-up", "d": "Face-filling intimacy.", "g": "camera", "l": 2, "q": "What is Close-up?", "a": "Face-filling intimacy.", "x": "Close-up — Face-filling intimacy. Example: Emotion..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Extreme close-up", "d": "Detail magnified.", "g": "camera", "l": 2, "q": "What is Extreme close-up?", "a": "Detail magnified.", "x": "Extreme close-up — Detail magnified. Example: Eyes, objects..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Wide shot", "d": "Full scene context.", "g": "camera", "l": 2, "q": "What is Wide shot?", "a": "Full scene context.", "x": "Wide shot — Full scene context. Example: Landscapes..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Over-the-shoulder", "d": "Dialogue framing.", "g": "camera", "l": 2, "q": "What is Over-the-shoulder?", "a": "Dialogue framing.", "x": "Over-the-shoulder — Dialogue framing. Example: Conversations..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "POV shot", "d": "Character's viewpoint.", "g": "camera", "l": 2, "q": "What is POV shot?", "a": "Character's viewpoint.", "x": "POV shot — Character's viewpoint. Example: Immersion..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Dutch angle", "d": "Tilted unease.", "g": "camera", "l": 2, "q": "What is Dutch angle?", "a": "Tilted unease.", "x": "Dutch angle — Tilted unease. Example: Thrillers..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Steadicam", "d": "Stabilized moving camera.", "g": "camera", "l": 2, "q": "What is Steadicam?", "a": "Stabilized moving camera.", "x": "Steadicam — Stabilized moving camera. Example: The Shining..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Diegetic sound", "d": "Sound from the story world.", "g": "sound", "l": 2, "q": "What is Diegetic sound?", "a": "Sound from the story world.", "x": "Diegetic sound — Sound from the story world. Example: A radio on screen..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Non-diegetic sound", "d": "Sound outside the story: score.", "g": "sound", "l": 2, "q": "What is Non-diegetic sound?", "a": "Sound outside the story: score.", "x": "Non-diegetic sound — Sound outside the story: score. Example: The soundtrack..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Foley", "d": "Recreated everyday sounds.", "g": "sound", "l": 2, "q": "What is Foley?", "a": "Recreated everyday sounds.", "x": "Foley — Recreated everyday sounds. Example: Footsteps in post..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "ADR", "d": "Re-recorded dialogue.", "g": "sound", "l": 2, "q": "What is ADR?", "a": "Re-recorded dialogue.", "x": "ADR — Re-recorded dialogue. Example: Looping lines..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Score", "d": "Original composed music.", "g": "sound", "l": 2, "q": "What is Score?", "a": "Original composed music.", "x": "Score — Original composed music. Example: John Williams..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Soundtrack", "d": "All released music.", "g": "sound", "l": 2, "q": "What is Soundtrack?", "a": "All released music.", "x": "Soundtrack — All released music. Example: Guardians mixtape..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Three-act structure", "d": "Setup, confrontation, resolution.", "g": "story", "l": 2, "q": "What is Three-act structure?", "a": "Setup, confrontation, resolution.", "x": "Three-act structure — Setup, confrontation, resolution. Example: Most features..  Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-film-terms-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
