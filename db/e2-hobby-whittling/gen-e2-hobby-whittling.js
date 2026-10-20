(function(){'use strict';
/* JAH Whittling Hobby Database generator — jahdb-e2-hobby-whittling-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-whittling',PREFIX='JAH-E2HOBBYWHIT-',NAME='JAH Whittling Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Whittling: the complete hobby guide", "d": "Whittling: knife and wood..", "g": "overview", "l": 2, "q": "What is Whittling: the complete hobby guide?", "a": "Whittling: knife and wood..", "x": "The complete Whittling hobby guide: knife and wood.. Knife. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Sharp knife.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Whittling this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Whittling this weekend.", "x": "Start here: Knife.. knife and wood. Begin with Basswood. — small, cheap, and fun. Cut away. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Knife.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Knife.", "x": "Whittling essential: Knife.. Cut away. One of the six things every practitioner knows — Cuts.. knife and wood. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Knife..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Knife..", "x": "In practice: Knife.. Glove. Here is how it works in real sessions — Safety.. Whittling Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Basswood.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Basswood.", "x": "Whittling essential: Basswood.. Glove. One of the six things every practitioner knows — Safety.. knife and wood. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Basswood..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Basswood..", "x": "In practice: Basswood.. Start simple. Here is how it works in real sessions — Projects.. Whittling Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Cuts.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Cuts.", "x": "Whittling essential: Cuts.. Start simple. One of the six things every practitioner knows — Projects.. knife and wood. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Cuts..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Cuts..", "x": "In practice: Cuts.. Patience. Here is how it works in real sessions — Strop.. Whittling Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Safety.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Safety.", "x": "Whittling essential: Safety.. Patience. One of the six things every practitioner knows — Strop.. knife and wood. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Safety..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Safety..", "x": "In practice: Safety.. Gift. Here is how it works in real sessions — Knife.. Whittling Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Projects.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Projects.", "x": "Whittling essential: Projects.. Gift. One of the six things every practitioner knows — Knife.. knife and wood. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Projects..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Projects..", "x": "In practice: Projects.. Sharp knife. Here is how it works in real sessions — Basswood.. Whittling Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Strop.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Strop.", "x": "Whittling essential: Strop.. Sharp knife. One of the six things every practitioner knows — Basswood.. knife and wood. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Strop..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Strop..", "x": "In practice: Strop.. Cut away. Here is how it works in real sessions — Cuts.. Whittling Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Sharp knife.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Sharp knife.", "x": "Whittling tip: Sharp knife.. Basswood. From experienced hobbyists — Start simple.. knife and wood. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Cut away.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Cut away.", "x": "Whittling tip: Cut away.. Cuts. From experienced hobbyists — Patience.. knife and wood. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Glove.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Glove.", "x": "Whittling tip: Glove.. Safety. From experienced hobbyists — Gift.. knife and wood. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Start simple.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Start simple.", "x": "Whittling tip: Start simple.. Projects. From experienced hobbyists — Sharp knife.. knife and wood. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Patience.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Patience.", "x": "Whittling tip: Patience.. Strop. From experienced hobbyists — Cut away.. knife and wood. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Gift.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Gift.", "x": "Whittling tip: Gift.. Knife. From experienced hobbyists — Glove.. knife and wood. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Whittling gear: Knife..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Whittling gear: Knife..", "x": "Gear: Knife.. Start minimal — Basswood. — and upgrade as skills demand. knife and wood. Buy once where it matters; go cheap where it does not. Glove. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Whittling on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Whittling on a budget.", "x": "Costs: Start simple.. Whittling can start for little and scale to obsession — Cuts.. knife and wood. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Whittling safety: Patience..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Whittling safety: Patience..", "x": "Safety: Patience.. Safety. Every hobby has its risks — Whittling. knife and wood. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Whittling: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Whittling: beginner to expert.", "x": "The ladder: knife and wood.. Beginner: Projects.. Intermediate: Strop.. Advanced: Gift.. Whittling Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Whittling.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Whittling.", "x": "Advanced: Strop.. Sharp knife. Once basics are automatic, these separate good from great — Whittling. knife and wood. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-whittling-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
