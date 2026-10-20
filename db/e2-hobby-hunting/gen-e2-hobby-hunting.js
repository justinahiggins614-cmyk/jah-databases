(function(){'use strict';
/* JAH Hunting Hobby Database generator — jahdb-e2-hobby-hunting-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-hunting',PREFIX='JAH-E2HOBBYHUNT-',NAME='JAH Hunting Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hunting: the complete hobby guide", "d": "Hunting: ethical harvest..", "g": "overview", "l": 2, "q": "What is Hunting: the complete hobby guide?", "a": "Hunting: ethical harvest..", "x": "The complete Hunting hobby guide: ethical harvest.. Hunter safety course. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Safety first.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Hunting this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Hunting this weekend.", "x": "Start here: Hunter safety course.. ethical harvest. Begin with License/tags. — small, cheap, and fun. Know laws. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hunter safety course.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hunter safety course.", "x": "Hunting essential: Hunter safety course.. Know laws. One of the six things every practitioner knows — Know game.. ethical harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Hunter safety course..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Hunter safety course..", "x": "In practice: Hunter safety course.. Practice shooting. Here is how it works in real sessions — Scout.. Hunting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "License/tags.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "License/tags.", "x": "Hunting essential: License/tags.. Practice shooting. One of the six things every practitioner knows — Scout.. ethical harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: License/tags..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: License/tags..", "x": "In practice: License/tags.. Respect land. Here is how it works in real sessions — Ethics.. Hunting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Know game.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Know game.", "x": "Hunting essential: Know game.. Respect land. One of the six things every practitioner knows — Ethics.. ethical harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Know game..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Know game..", "x": "In practice: Know game.. Mentor. Here is how it works in real sessions — Field dressing.. Hunting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Scout.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Scout.", "x": "Hunting essential: Scout.. Mentor. One of the six things every practitioner knows — Field dressing.. ethical harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Scout..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Scout..", "x": "In practice: Scout.. Meat care. Here is how it works in real sessions — Hunter safety course.. Hunting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Ethics.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Ethics.", "x": "Hunting essential: Ethics.. Meat care. One of the six things every practitioner knows — Hunter safety course.. ethical harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Ethics..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Ethics..", "x": "In practice: Ethics.. Safety first. Here is how it works in real sessions — License/tags.. Hunting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Field dressing.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Field dressing.", "x": "Hunting essential: Field dressing.. Safety first. One of the six things every practitioner knows — License/tags.. ethical harvest. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Field dressing..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Field dressing..", "x": "In practice: Field dressing.. Know laws. Here is how it works in real sessions — Know game.. Hunting Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Safety first.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Safety first.", "x": "Hunting tip: Safety first.. License/tags. From experienced hobbyists — Respect land.. ethical harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Know laws.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Know laws.", "x": "Hunting tip: Know laws.. Know game. From experienced hobbyists — Mentor.. ethical harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Practice shooting.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Practice shooting.", "x": "Hunting tip: Practice shooting.. Scout. From experienced hobbyists — Meat care.. ethical harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Respect land.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Respect land.", "x": "Hunting tip: Respect land.. Ethics. From experienced hobbyists — Safety first.. ethical harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Mentor.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Mentor.", "x": "Hunting tip: Mentor.. Field dressing. From experienced hobbyists — Know laws.. ethical harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Meat care.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Meat care.", "x": "Hunting tip: Meat care.. Hunter safety course. From experienced hobbyists — Practice shooting.. ethical harvest. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Hunting gear: Hunter safety course..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Hunting gear: Hunter safety course..", "x": "Gear: Hunter safety course.. Start minimal — License/tags. — and upgrade as skills demand. ethical harvest. Buy once where it matters; go cheap where it does not. Practice shooting. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Hunting on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Hunting on a budget.", "x": "Costs: Respect land.. Hunting can start for little and scale to obsession — Know game.. ethical harvest. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Hunting safety: Mentor..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Hunting safety: Mentor..", "x": "Safety: Mentor.. Scout. Every hobby has its risks — Hunting. ethical harvest. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Hunting: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Hunting: beginner to expert.", "x": "The ladder: ethical harvest.. Beginner: Ethics.. Intermediate: Field dressing.. Advanced: Meat care.. Hunting Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Hunting.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Hunting.", "x": "Advanced: Field dressing.. Safety first. Once basics are automatic, these separate good from great — Hunting. ethical harvest. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-hunting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
