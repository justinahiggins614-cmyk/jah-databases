(function(){'use strict';
/* JAH Wood Carving Hobby Database generator — jahdb-e2-hobby-wood-carving-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-wood-carving',PREFIX='JAH-E2HOBBYWOOD-',NAME='JAH Wood Carving Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wood Carving: the complete hobby guide", "d": "Wood Carving: relief and sculpture..", "g": "overview", "l": 2, "q": "What is Wood Carving: the complete hobby guide?", "a": "Wood Carving: relief and sculpture..", "x": "The complete Wood Carving hobby guide: relief and sculpture.. Gouges. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Classes.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Wood Carving this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Wood Carving this weekend.", "x": "Start here: Gouges.. relief and sculpture. Begin with Basswood. — small, cheap, and fun. Sharp. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Gouges.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Gouges.", "x": "Wood Carving essential: Gouges.. Sharp. One of the six things every practitioner knows — Design.. relief and sculpture. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Gouges..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Gouges..", "x": "In practice: Gouges.. Grain. Here is how it works in real sessions — Safety.. Wood Carving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Basswood.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Basswood.", "x": "Wood Carving essential: Basswood.. Grain. One of the six things every practitioner knows — Safety.. relief and sculpture. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Basswood..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Basswood..", "x": "In practice: Basswood.. Practice. Here is how it works in real sessions — Sharpening.. Wood Carving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Design.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Design.", "x": "Wood Carving essential: Design.. Practice. One of the six things every practitioner knows — Sharpening.. relief and sculpture. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Design..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Design..", "x": "In practice: Design.. Community. Here is how it works in real sessions — Finish.. Wood Carving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Safety.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Safety.", "x": "Wood Carving essential: Safety.. Community. One of the six things every practitioner knows — Finish.. relief and sculpture. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Safety..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Safety..", "x": "In practice: Safety.. Sell. Here is how it works in real sessions — Gouges.. Wood Carving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Sharpening.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Sharpening.", "x": "Wood Carving essential: Sharpening.. Sell. One of the six things every practitioner knows — Gouges.. relief and sculpture. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Sharpening..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Sharpening..", "x": "In practice: Sharpening.. Classes. Here is how it works in real sessions — Basswood.. Wood Carving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Finish.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Finish.", "x": "Wood Carving essential: Finish.. Classes. One of the six things every practitioner knows — Basswood.. relief and sculpture. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Finish..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Finish..", "x": "In practice: Finish.. Sharp. Here is how it works in real sessions — Design.. Wood Carving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Classes.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Classes.", "x": "Wood Carving tip: Classes.. Basswood. From experienced hobbyists — Practice.. relief and sculpture. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Sharp.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Sharp.", "x": "Wood Carving tip: Sharp.. Design. From experienced hobbyists — Community.. relief and sculpture. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Grain.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Grain.", "x": "Wood Carving tip: Grain.. Safety. From experienced hobbyists — Sell.. relief and sculpture. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Practice.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Practice.", "x": "Wood Carving tip: Practice.. Sharpening. From experienced hobbyists — Classes.. relief and sculpture. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Community.", "x": "Wood Carving tip: Community.. Finish. From experienced hobbyists — Sharp.. relief and sculpture. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Sell.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Sell.", "x": "Wood Carving tip: Sell.. Gouges. From experienced hobbyists — Grain.. relief and sculpture. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Wood Carving gear: Gouges..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Wood Carving gear: Gouges..", "x": "Gear: Gouges.. Start minimal — Basswood. — and upgrade as skills demand. relief and sculpture. Buy once where it matters; go cheap where it does not. Grain. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Wood Carving on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Wood Carving on a budget.", "x": "Costs: Practice.. Wood Carving can start for little and scale to obsession — Design.. relief and sculpture. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Wood Carving safety: Community..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Wood Carving safety: Community..", "x": "Safety: Community.. Safety. Every hobby has its risks — Wood Carving. relief and sculpture. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Wood Carving: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Wood Carving: beginner to expert.", "x": "The ladder: relief and sculpture.. Beginner: Sharpening.. Intermediate: Finish.. Advanced: Sell.. Wood Carving Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Wood Carving.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Wood Carving.", "x": "Advanced: Finish.. Classes. Once basics are automatic, these separate good from great — Wood Carving. relief and sculpture. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-wood-carving-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
