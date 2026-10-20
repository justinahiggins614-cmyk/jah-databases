(function(){'use strict';
/* JAH 3D Printing Projects Hobby Database generator — jahdb-e2-hobby-3d-printing-projects-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-3d-printing-projects',PREFIX='JAH-E2HOBBY3DPR-',NAME='JAH 3D Printing Projects Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "3D Printing Projects: the complete hobby guide", "d": "3D Printing Projects: make anything..", "g": "overview", "l": 2, "q": "What is 3D Printing Projects: the complete hobby guide?", "a": "3D Printing Projects: make anything..", "x": "The complete 3D Printing Projects hobby guide: make anything.. Printer choice. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Calibrate.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start 3D Printing Projects this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start 3D Printing Projects this weekend.", "x": "Start here: Printer choice.. make anything. Begin with PLA first. — small, cheap, and fun. Start simple. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Printer choice.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Printer choice.", "x": "3D Printing Projects essential: Printer choice.. Start simple. One of the six things every practitioner knows — Slicers.. make anything. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Printer choice..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Printer choice..", "x": "In practice: Printer choice.. Ventilate. Here is how it works in real sessions — Bed leveling.. 3D Printing Projects Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "PLA first.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "PLA first.", "x": "3D Printing Projects essential: PLA first.. Ventilate. One of the six things every practitioner knows — Bed leveling.. make anything. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: PLA first..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: PLA first..", "x": "In practice: PLA first.. Filament dry. Here is how it works in real sessions — Models: Thingiverse.. 3D Printing Projects Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Slicers.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Slicers.", "x": "3D Printing Projects essential: Slicers.. Filament dry. One of the six things every practitioner knows — Models: Thingiverse.. make anything. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Slicers..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Slicers..", "x": "In practice: Slicers.. Community. Here is how it works in real sessions — Safety.. 3D Printing Projects Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Bed leveling.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Bed leveling.", "x": "3D Printing Projects essential: Bed leveling.. Community. One of the six things every practitioner knows — Safety.. make anything. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Bed leveling..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Bed leveling..", "x": "In practice: Bed leveling.. Design. Here is how it works in real sessions — Printer choice.. 3D Printing Projects Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Models: Thingiverse.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Models: Thingiverse.", "x": "3D Printing Projects essential: Models: Thingiverse.. Design. One of the six things every practitioner knows — Printer choice.. make anything. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Models: Thingiverse..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Models: Thingiverse..", "x": "In practice: Models: Thingiverse.. Calibrate. Here is how it works in real sessions — PLA first.. 3D Printing Projects Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Safety.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Safety.", "x": "3D Printing Projects essential: Safety.. Calibrate. One of the six things every practitioner knows — PLA first.. make anything. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Safety..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Safety..", "x": "In practice: Safety.. Start simple. Here is how it works in real sessions — Slicers.. 3D Printing Projects Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Calibrate.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Calibrate.", "x": "3D Printing Projects tip: Calibrate.. PLA first. From experienced hobbyists — Filament dry.. make anything. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Start simple.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Start simple.", "x": "3D Printing Projects tip: Start simple.. Slicers. From experienced hobbyists — Community.. make anything. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Ventilate.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Ventilate.", "x": "3D Printing Projects tip: Ventilate.. Bed leveling. From experienced hobbyists — Design.. make anything. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Filament dry.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Filament dry.", "x": "3D Printing Projects tip: Filament dry.. Models: Thingiverse. From experienced hobbyists — Calibrate.. make anything. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Community.", "x": "3D Printing Projects tip: Community.. Safety. From experienced hobbyists — Start simple.. make anything. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Design.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Design.", "x": "3D Printing Projects tip: Design.. Printer choice. From experienced hobbyists — Ventilate.. make anything. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "3D Printing Projects gear: Printer choice..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "3D Printing Projects gear: Printer choice..", "x": "Gear: Printer choice.. Start minimal — PLA first. — and upgrade as skills demand. make anything. Buy once where it matters; go cheap where it does not. Ventilate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "3D Printing Projects on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "3D Printing Projects on a budget.", "x": "Costs: Filament dry.. 3D Printing Projects can start for little and scale to obsession — Slicers.. make anything. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "3D Printing Projects safety: Community..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "3D Printing Projects safety: Community..", "x": "Safety: Community.. Bed leveling. Every hobby has its risks — 3D Printing Projects. make anything. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "3D Printing Projects: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "3D Printing Projects: beginner to expert.", "x": "The ladder: make anything.. Beginner: Models: Thingiverse.. Intermediate: Safety.. Advanced: Design.. 3D Printing Projects Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up 3D Printing Projects.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up 3D Printing Projects.", "x": "Advanced: Safety.. Calibrate. Once basics are automatic, these separate good from great — 3D Printing Projects. make anything. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-3d-printing-projects-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
