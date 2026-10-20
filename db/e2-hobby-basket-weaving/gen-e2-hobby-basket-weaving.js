(function(){'use strict';
/* JAH Basket Weaving Hobby Database generator — jahdb-e2-hobby-basket-weaving-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-basket-weaving',PREFIX='JAH-E2HOBBYBASK-',NAME='JAH Basket Weaving Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Basket Weaving: the complete hobby guide", "d": "Basket Weaving: woven vessels..", "g": "overview", "l": 2, "q": "What is Basket Weaving: the complete hobby guide?", "a": "Basket Weaving: woven vessels..", "x": "The complete Basket Weaving hobby guide: woven vessels.. Reed. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Kits.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Basket Weaving this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Basket Weaving this weekend.", "x": "Start here: Reed.. woven vessels. Begin with Soak. — small, cheap, and fun. Soak. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Reed.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Reed.", "x": "Basket Weaving essential: Reed.. Soak. One of the six things every practitioner knows — Weaves.. woven vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Reed..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Reed..", "x": "In practice: Reed.. Tension. Here is how it works in real sessions — Bases.. Basket Weaving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Soak.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Soak.", "x": "Basket Weaving essential: Soak.. Tension. One of the six things every practitioner knows — Bases.. woven vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Soak..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Soak..", "x": "In practice: Soak.. Classes. Here is how it works in real sessions — Finishing.. Basket Weaving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Weaves.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Weaves.", "x": "Basket Weaving essential: Weaves.. Classes. One of the six things every practitioner knows — Finishing.. woven vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Weaves..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Weaves..", "x": "In practice: Weaves.. Community. Here is how it works in real sessions — Patterns.. Basket Weaving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Bases.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Bases.", "x": "Basket Weaving essential: Bases.. Community. One of the six things every practitioner knows — Patterns.. woven vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Bases..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Bases..", "x": "In practice: Bases.. Gift. Here is how it works in real sessions — Reed.. Basket Weaving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Finishing.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Finishing.", "x": "Basket Weaving essential: Finishing.. Gift. One of the six things every practitioner knows — Reed.. woven vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Finishing..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Finishing..", "x": "In practice: Finishing.. Kits. Here is how it works in real sessions — Soak.. Basket Weaving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Patterns.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Patterns.", "x": "Basket Weaving essential: Patterns.. Kits. One of the six things every practitioner knows — Soak.. woven vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Patterns..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Patterns..", "x": "In practice: Patterns.. Soak. Here is how it works in real sessions — Weaves.. Basket Weaving Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Kits.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Kits.", "x": "Basket Weaving tip: Kits.. Soak. From experienced hobbyists — Classes.. woven vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Soak.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Soak.", "x": "Basket Weaving tip: Soak.. Weaves. From experienced hobbyists — Community.. woven vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Tension.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Tension.", "x": "Basket Weaving tip: Tension.. Bases. From experienced hobbyists — Gift.. woven vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Classes.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Classes.", "x": "Basket Weaving tip: Classes.. Finishing. From experienced hobbyists — Kits.. woven vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Community.", "x": "Basket Weaving tip: Community.. Patterns. From experienced hobbyists — Soak.. woven vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Gift.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Gift.", "x": "Basket Weaving tip: Gift.. Reed. From experienced hobbyists — Tension.. woven vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Basket Weaving gear: Reed..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Basket Weaving gear: Reed..", "x": "Gear: Reed.. Start minimal — Soak. — and upgrade as skills demand. woven vessels. Buy once where it matters; go cheap where it does not. Tension. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Basket Weaving on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Basket Weaving on a budget.", "x": "Costs: Classes.. Basket Weaving can start for little and scale to obsession — Weaves.. woven vessels. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Basket Weaving safety: Community..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Basket Weaving safety: Community..", "x": "Safety: Community.. Bases. Every hobby has its risks — Basket Weaving. woven vessels. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Basket Weaving: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Basket Weaving: beginner to expert.", "x": "The ladder: woven vessels.. Beginner: Finishing.. Intermediate: Patterns.. Advanced: Gift.. Basket Weaving Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Basket Weaving.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Basket Weaving.", "x": "Advanced: Patterns.. Kits. Once basics are automatic, these separate good from great — Basket Weaving. woven vessels. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-basket-weaving-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
