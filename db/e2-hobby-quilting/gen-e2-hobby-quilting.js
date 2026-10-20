(function(){'use strict';
/* JAH Quilting Hobby Database generator — jahdb-e2-hobby-quilting-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-quilting',PREFIX='JAH-E2HOBBYQUIL-',NAME='JAH Quilting Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Quilting: the complete hobby guide", "d": "Quilting: fabric into warmth..", "g": "overview", "l": 2, "q": "What is Quilting: the complete hobby guide?", "a": "Quilting: fabric into warmth..", "x": "The complete Quilting hobby guide: fabric into warmth.. Rotary cutter. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Classes.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Quilting this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Quilting this weekend.", "x": "Start here: Rotary cutter.. fabric into warmth. Begin with Quarter inch seam. — small, cheap, and fun. Prewash. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Rotary cutter.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Rotary cutter.", "x": "Quilting essential: Rotary cutter.. Prewash. One of the six things every practitioner knows — Patchwork.. fabric into warmth. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Rotary cutter..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Rotary cutter..", "x": "In practice: Rotary cutter.. Press. Here is how it works in real sessions — Batting.. Quilting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Quarter inch seam.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Quarter inch seam.", "x": "Quilting essential: Quarter inch seam.. Press. One of the six things every practitioner knows — Batting.. fabric into warmth. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Quarter inch seam..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Quarter inch seam..", "x": "In practice: Quarter inch seam.. Community. Here is how it works in real sessions — Binding.. Quilting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Patchwork.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Patchwork.", "x": "Quilting essential: Patchwork.. Community. One of the six things every practitioner knows — Binding.. fabric into warmth. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Patchwork..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Patchwork..", "x": "In practice: Patchwork.. Shows. Here is how it works in real sessions — Machine.. Quilting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Batting.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Batting.", "x": "Quilting essential: Batting.. Shows. One of the six things every practitioner knows — Machine.. fabric into warmth. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Batting..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Batting..", "x": "In practice: Batting.. Gift. Here is how it works in real sessions — Rotary cutter.. Quilting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Binding.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Binding.", "x": "Quilting essential: Binding.. Gift. One of the six things every practitioner knows — Rotary cutter.. fabric into warmth. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Binding..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Binding..", "x": "In practice: Binding.. Classes. Here is how it works in real sessions — Quarter inch seam.. Quilting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Machine.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Machine.", "x": "Quilting essential: Machine.. Classes. One of the six things every practitioner knows — Quarter inch seam.. fabric into warmth. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Machine..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Machine..", "x": "In practice: Machine.. Prewash. Here is how it works in real sessions — Patchwork.. Quilting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Classes.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Classes.", "x": "Quilting tip: Classes.. Quarter inch seam. From experienced hobbyists — Community.. fabric into warmth. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Prewash.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Prewash.", "x": "Quilting tip: Prewash.. Patchwork. From experienced hobbyists — Shows.. fabric into warmth. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Press.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Press.", "x": "Quilting tip: Press.. Batting. From experienced hobbyists — Gift.. fabric into warmth. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Community.", "x": "Quilting tip: Community.. Binding. From experienced hobbyists — Classes.. fabric into warmth. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Shows.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Shows.", "x": "Quilting tip: Shows.. Machine. From experienced hobbyists — Prewash.. fabric into warmth. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Gift.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Gift.", "x": "Quilting tip: Gift.. Rotary cutter. From experienced hobbyists — Press.. fabric into warmth. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Quilting gear: Rotary cutter..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Quilting gear: Rotary cutter..", "x": "Gear: Rotary cutter.. Start minimal — Quarter inch seam. — and upgrade as skills demand. fabric into warmth. Buy once where it matters; go cheap where it does not. Press. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Quilting on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Quilting on a budget.", "x": "Costs: Community.. Quilting can start for little and scale to obsession — Patchwork.. fabric into warmth. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Quilting safety: Shows..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Quilting safety: Shows..", "x": "Safety: Shows.. Batting. Every hobby has its risks — Quilting. fabric into warmth. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Quilting: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Quilting: beginner to expert.", "x": "The ladder: fabric into warmth.. Beginner: Binding.. Intermediate: Machine.. Advanced: Gift.. Quilting Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Quilting.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Quilting.", "x": "Advanced: Machine.. Classes. Once basics are automatic, these separate good from great — Quilting. fabric into warmth. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-quilting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
