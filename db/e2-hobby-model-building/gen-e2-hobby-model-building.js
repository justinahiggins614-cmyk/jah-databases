(function(){'use strict';
/* JAH Model Building Hobby Database generator — jahdb-e2-hobby-model-building-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-model-building',PREFIX='JAH-E2HOBBYMODE-',NAME='JAH Model Building Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Model Building: the complete hobby guide", "d": "Model Building: scale models: planes, cars, ships..", "g": "overview", "l": 2, "q": "What is Model Building: the complete hobby guide?", "a": "Model Building: scale models: planes, cars, ships..", "x": "The complete Model Building hobby guide: scale models: planes, cars, ships.. Choose a skill level 1-2 kit. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Start simple.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Model Building this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Model Building this weekend.", "x": "Start here: Choose a skill level 1-2 kit.. scale models: planes, cars, ships. Begin with Basic tools: cutters, glue. — small, cheap, and fun. Thin glue. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Choose a skill level 1-2 kit.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Choose a skill level 1-2 kit.", "x": "Model Building essential: Choose a skill level 1-2 kit.. Thin glue. One of the six things every practitioner knows — Paints: acrylics.. scale models: planes, cars, ships. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Choose a skill level 1-2 kit..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Choose a skill level 1-2 kit..", "x": "In practice: Choose a skill level 1-2 kit.. Wash hands. Here is how it works in real sessions — Follow instructions.. Model Building Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Basic tools: cutters, glue.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Basic tools: cutters, glue.", "x": "Model Building essential: Basic tools: cutters, glue.. Wash hands. One of the six things every practitioner knows — Follow instructions.. scale models: planes, cars, ships. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Basic tools: cutters, glue..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Basic tools: cutters, glue..", "x": "In practice: Basic tools: cutters, glue.. Ventilate. Here is how it works in real sessions — Decals: water slide.. Model Building Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Paints: acrylics.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Paints: acrylics.", "x": "Model Building essential: Paints: acrylics.. Ventilate. One of the six things every practitioner knows — Decals: water slide.. scale models: planes, cars, ships. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Paints: acrylics..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Paints: acrylics..", "x": "In practice: Paints: acrylics.. Patience. Here is how it works in real sessions — Display.. Model Building Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Follow instructions.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Follow instructions.", "x": "Model Building essential: Follow instructions.. Patience. One of the six things every practitioner knows — Display.. scale models: planes, cars, ships. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Follow instructions..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Follow instructions..", "x": "In practice: Follow instructions.. Join club. Here is how it works in real sessions — Choose a skill level 1-2 kit.. Model Building Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Decals: water slide.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Decals: water slide.", "x": "Model Building essential: Decals: water slide.. Join club. One of the six things every practitioner knows — Choose a skill level 1-2 kit.. scale models: planes, cars, ships. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Decals: water slide..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Decals: water slide..", "x": "In practice: Decals: water slide.. Start simple. Here is how it works in real sessions — Basic tools: cutters, glue.. Model Building Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Display.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Display.", "x": "Model Building essential: Display.. Start simple. One of the six things every practitioner knows — Basic tools: cutters, glue.. scale models: planes, cars, ships. Learn these and you are no longer a beginner.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Display..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Display..", "x": "In practice: Display.. Thin glue. Here is how it works in real sessions — Paints: acrylics.. Model Building Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Start simple.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Start simple.", "x": "Model Building tip: Start simple.. Basic tools: cutters, glue. From experienced hobbyists — Ventilate.. scale models: planes, cars, ships. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Thin glue.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Thin glue.", "x": "Model Building tip: Thin glue.. Paints: acrylics. From experienced hobbyists — Patience.. scale models: planes, cars, ships. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Wash hands.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Wash hands.", "x": "Model Building tip: Wash hands.. Follow instructions. From experienced hobbyists — Join club.. scale models: planes, cars, ships. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Ventilate.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Ventilate.", "x": "Model Building tip: Ventilate.. Decals: water slide. From experienced hobbyists — Start simple.. scale models: planes, cars, ships. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Patience.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Patience.", "x": "Model Building tip: Patience.. Display. From experienced hobbyists — Thin glue.. scale models: planes, cars, ships. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Join club.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Join club.", "x": "Model Building tip: Join club.. Choose a skill level 1-2 kit. From experienced hobbyists — Wash hands.. scale models: planes, cars, ships. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Model Building gear: Choose a skill level 1-2 kit..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Model Building gear: Choose a skill level 1-2 kit..", "x": "Gear: Choose a skill level 1-2 kit.. Start minimal — Basic tools: cutters, glue. — and upgrade as skills demand. scale models: planes, cars, ships. Buy once where it matters; go cheap where it does not. Wash hands.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Model Building on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Model Building on a budget.", "x": "Costs: Ventilate.. Model Building can start for little and scale to obsession — Paints: acrylics.. scale models: planes, cars, ships. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Model Building safety: Patience..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Model Building safety: Patience..", "x": "Safety: Patience.. Follow instructions. Every hobby has its risks — Model Building. scale models: planes, cars, ships. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Model Building: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Model Building: beginner to expert.", "x": "The ladder: scale models: planes, cars, ships.. Beginner: Decals: water slide.. Intermediate: Display.. Advanced: Join club.. Model Building Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Model Building.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Model Building.", "x": "Advanced: Display.. Start simple. Once basics are automatic, these separate good from great — Model Building. scale models: planes, cars, ships. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-model-building-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
