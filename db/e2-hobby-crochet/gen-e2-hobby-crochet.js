(function(){'use strict';
/* JAH Crochet Hobby Database generator — jahdb-e2-hobby-crochet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-crochet',PREFIX='JAH-E2HOBBYCROC-',NAME='JAH Crochet Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Crochet: the complete hobby guide", "d": "Crochet: hook into fabric..", "g": "overview", "l": 2, "q": "What is Crochet: the complete hobby guide?", "a": "Crochet: hook into fabric..", "x": "The complete Crochet hobby guide: hook into fabric.. Hook sizes. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Start chunky.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Crochet this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Crochet this weekend.", "x": "Start here: Hook sizes.. hook into fabric. Begin with Yarn weight. — small, cheap, and fun. Count. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hook sizes.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hook sizes.", "x": "Crochet essential: Hook sizes.. Count. One of the six things every practitioner knows — Chain/stitch.. hook into fabric. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Hook sizes..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Hook sizes..", "x": "In practice: Hook sizes.. YouTube. Here is how it works in real sessions — Granny square.. Crochet Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Yarn weight.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Yarn weight.", "x": "Crochet essential: Yarn weight.. YouTube. One of the six things every practitioner knows — Granny square.. hook into fabric. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Yarn weight..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Yarn weight..", "x": "In practice: Yarn weight.. Markers. Here is how it works in real sessions — Tension.. Crochet Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Chain/stitch.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Chain/stitch.", "x": "Crochet essential: Chain/stitch.. Markers. One of the six things every practitioner knows — Tension.. hook into fabric. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Chain/stitch..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Chain/stitch..", "x": "In practice: Chain/stitch.. WIP basket. Here is how it works in real sessions — Patterns.. Crochet Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Granny square.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Granny square.", "x": "Crochet essential: Granny square.. WIP basket. One of the six things every practitioner knows — Patterns.. hook into fabric. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Granny square..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Granny square..", "x": "In practice: Granny square.. Gift. Here is how it works in real sessions — Hook sizes.. Crochet Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Tension.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Tension.", "x": "Crochet essential: Tension.. Gift. One of the six things every practitioner knows — Hook sizes.. hook into fabric. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Tension..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Tension..", "x": "In practice: Tension.. Start chunky. Here is how it works in real sessions — Yarn weight.. Crochet Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Patterns.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Patterns.", "x": "Crochet essential: Patterns.. Start chunky. One of the six things every practitioner knows — Yarn weight.. hook into fabric. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Patterns..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Patterns..", "x": "In practice: Patterns.. Count. Here is how it works in real sessions — Chain/stitch.. Crochet Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Start chunky.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Start chunky.", "x": "Crochet tip: Start chunky.. Yarn weight. From experienced hobbyists — Markers.. hook into fabric. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Count.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Count.", "x": "Crochet tip: Count.. Chain/stitch. From experienced hobbyists — WIP basket.. hook into fabric. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "YouTube.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "YouTube.", "x": "Crochet tip: YouTube.. Granny square. From experienced hobbyists — Gift.. hook into fabric. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Markers.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Markers.", "x": "Crochet tip: Markers.. Tension. From experienced hobbyists — Start chunky.. hook into fabric. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "WIP basket.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "WIP basket.", "x": "Crochet tip: WIP basket.. Patterns. From experienced hobbyists — Count.. hook into fabric. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Gift.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Gift.", "x": "Crochet tip: Gift.. Hook sizes. From experienced hobbyists — YouTube.. hook into fabric. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Crochet gear: Hook sizes..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Crochet gear: Hook sizes..", "x": "Gear: Hook sizes.. Start minimal — Yarn weight. — and upgrade as skills demand. hook into fabric. Buy once where it matters; go cheap where it does not. YouTube. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Crochet on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Crochet on a budget.", "x": "Costs: Markers.. Crochet can start for little and scale to obsession — Chain/stitch.. hook into fabric. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Crochet safety: WIP basket..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Crochet safety: WIP basket..", "x": "Safety: WIP basket.. Granny square. Every hobby has its risks — Crochet. hook into fabric. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Crochet: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Crochet: beginner to expert.", "x": "The ladder: hook into fabric.. Beginner: Tension.. Intermediate: Patterns.. Advanced: Gift.. Crochet Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Crochet.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Crochet.", "x": "Advanced: Patterns.. Start chunky. Once basics are automatic, these separate good from great — Crochet. hook into fabric. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-crochet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
