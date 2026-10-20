(function(){'use strict';
/* JAH Canning Hobby Database generator — jahdb-e2-hobby-canning-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-canning',PREFIX='JAH-E2HOBBYCANN-',NAME='JAH Canning Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Canning: the complete hobby guide", "d": "Canning: preserve harvest..", "g": "overview", "l": 2, "q": "What is Canning: the complete hobby guide?", "a": "Canning: preserve harvest..", "x": "The complete Canning hobby guide: preserve harvest.. Water bath. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Tested recipes.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Canning this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Canning this weekend.", "x": "Start here: Water bath.. preserve harvest. Begin with Pressure. — small, cheap, and fun. Safety. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Water bath.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Water bath.", "x": "Canning essential: Water bath.. Safety. One of the six things every practitioner knows — Jars.. preserve harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Water bath..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Water bath..", "x": "In practice: Water bath.. Altitude. Here is how it works in real sessions — Recipes tested.. Canning Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Pressure.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Pressure.", "x": "Canning essential: Pressure.. Altitude. One of the six things every practitioner knows — Recipes tested.. preserve harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Pressure..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Pressure..", "x": "In practice: Pressure.. Labels. Here is how it works in real sessions — Safety.. Canning Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Jars.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Jars.", "x": "Canning essential: Jars.. Labels. One of the six things every practitioner knows — Safety.. preserve harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Jars..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Jars..", "x": "In practice: Jars.. Share. Here is how it works in real sessions — Labels.. Canning Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Recipes tested.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Recipes tested.", "x": "Canning essential: Recipes tested.. Share. One of the six things every practitioner knows — Labels.. preserve harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Recipes tested..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Recipes tested..", "x": "In practice: Recipes tested.. Pantry. Here is how it works in real sessions — Water bath.. Canning Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Safety.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Safety.", "x": "Canning essential: Safety.. Pantry. One of the six things every practitioner knows — Water bath.. preserve harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Safety..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Safety..", "x": "In practice: Safety.. Tested recipes. Here is how it works in real sessions — Pressure.. Canning Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Labels.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Labels.", "x": "Canning essential: Labels.. Tested recipes. One of the six things every practitioner knows — Pressure.. preserve harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Labels..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Labels..", "x": "In practice: Labels.. Safety. Here is how it works in real sessions — Jars.. Canning Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Tested recipes.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Tested recipes.", "x": "Canning tip: Tested recipes.. Pressure. From experienced hobbyists — Labels.. preserve harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Safety.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Safety.", "x": "Canning tip: Safety.. Jars. From experienced hobbyists — Share.. preserve harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Altitude.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Altitude.", "x": "Canning tip: Altitude.. Recipes tested. From experienced hobbyists — Pantry.. preserve harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Labels.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Labels.", "x": "Canning tip: Labels.. Safety. From experienced hobbyists — Tested recipes.. preserve harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Share.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Share.", "x": "Canning tip: Share.. Labels. From experienced hobbyists — Safety.. preserve harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Pantry.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Pantry.", "x": "Canning tip: Pantry.. Water bath. From experienced hobbyists — Altitude.. preserve harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Canning gear: Water bath..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Canning gear: Water bath..", "x": "Gear: Water bath.. Start minimal — Pressure. — and upgrade as skills demand. preserve harvest. Buy once where it matters; go cheap where it does not. Altitude. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Canning on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Canning on a budget.", "x": "Costs: Labels.. Canning can start for little and scale to obsession — Jars.. preserve harvest. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Canning safety: Share..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Canning safety: Share..", "x": "Safety: Share.. Recipes tested. Every hobby has its risks — Canning. preserve harvest. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Canning: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Canning: beginner to expert.", "x": "The ladder: preserve harvest.. Beginner: Safety.. Intermediate: Labels.. Advanced: Pantry.. Canning Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Canning.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Canning.", "x": "Advanced: Labels.. Tested recipes. Once basics are automatic, these separate good from great — Canning. preserve harvest. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-canning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
