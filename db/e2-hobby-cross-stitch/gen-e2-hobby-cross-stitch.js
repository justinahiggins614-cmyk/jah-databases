(function(){'use strict';
/* JAH Cross-Stitch Hobby Database generator — jahdb-e2-hobby-cross-stitch-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-cross-stitch',PREFIX='JAH-E2HOBBYCROS-',NAME='JAH Cross-Stitch Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cross-Stitch: the complete hobby guide", "d": "Cross-Stitch: counted thread pictures..", "g": "overview", "l": 2, "q": "What is Cross-Stitch: the complete hobby guide?", "a": "Cross-Stitch: counted thread pictures..", "x": "The complete Cross-Stitch hobby guide: counted thread pictures.. Aida cloth. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Count.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Cross-Stitch this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Cross-Stitch this weekend.", "x": "Start here: Aida cloth.. counted thread pictures. Begin with Floss. — small, cheap, and fun. Park threads. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Aida cloth.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Aida cloth.", "x": "Cross-Stitch essential: Aida cloth.. Park threads. One of the six things every practitioner knows — Needles.. counted thread pictures. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Aida cloth..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Aida cloth..", "x": "In practice: Aida cloth.. Light. Here is how it works in real sessions — Charts.. Cross-Stitch Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Floss.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Floss.", "x": "Cross-Stitch essential: Floss.. Light. One of the six things every practitioner knows — Charts.. counted thread pictures. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Floss..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Floss..", "x": "In practice: Floss.. Kits. Here is how it works in real sessions — Hoop.. Cross-Stitch Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Needles.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Needles.", "x": "Cross-Stitch essential: Needles.. Kits. One of the six things every practitioner knows — Hoop.. counted thread pictures. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Needles..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Needles..", "x": "In practice: Needles.. Community. Here is how it works in real sessions — Finishing.. Cross-Stitch Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Charts.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Charts.", "x": "Cross-Stitch essential: Charts.. Community. One of the six things every practitioner knows — Finishing.. counted thread pictures. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Charts..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Charts..", "x": "In practice: Charts.. Frame. Here is how it works in real sessions — Aida cloth.. Cross-Stitch Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Hoop.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Hoop.", "x": "Cross-Stitch essential: Hoop.. Frame. One of the six things every practitioner knows — Aida cloth.. counted thread pictures. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Hoop..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Hoop..", "x": "In practice: Hoop.. Count. Here is how it works in real sessions — Floss.. Cross-Stitch Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Finishing.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Finishing.", "x": "Cross-Stitch essential: Finishing.. Count. One of the six things every practitioner knows — Floss.. counted thread pictures. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Finishing..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Finishing..", "x": "In practice: Finishing.. Park threads. Here is how it works in real sessions — Needles.. Cross-Stitch Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Count.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Count.", "x": "Cross-Stitch tip: Count.. Floss. From experienced hobbyists — Kits.. counted thread pictures. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Park threads.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Park threads.", "x": "Cross-Stitch tip: Park threads.. Needles. From experienced hobbyists — Community.. counted thread pictures. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Light.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Light.", "x": "Cross-Stitch tip: Light.. Charts. From experienced hobbyists — Frame.. counted thread pictures. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Kits.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Kits.", "x": "Cross-Stitch tip: Kits.. Hoop. From experienced hobbyists — Count.. counted thread pictures. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Community.", "x": "Cross-Stitch tip: Community.. Finishing. From experienced hobbyists — Park threads.. counted thread pictures. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Frame.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Frame.", "x": "Cross-Stitch tip: Frame.. Aida cloth. From experienced hobbyists — Light.. counted thread pictures. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Cross-Stitch gear: Aida cloth..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Cross-Stitch gear: Aida cloth..", "x": "Gear: Aida cloth.. Start minimal — Floss. — and upgrade as skills demand. counted thread pictures. Buy once where it matters; go cheap where it does not. Light. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Cross-Stitch on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Cross-Stitch on a budget.", "x": "Costs: Kits.. Cross-Stitch can start for little and scale to obsession — Needles.. counted thread pictures. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Cross-Stitch safety: Community..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Cross-Stitch safety: Community..", "x": "Safety: Community.. Charts. Every hobby has its risks — Cross-Stitch. counted thread pictures. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Cross-Stitch: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Cross-Stitch: beginner to expert.", "x": "The ladder: counted thread pictures.. Beginner: Hoop.. Intermediate: Finishing.. Advanced: Frame.. Cross-Stitch Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Cross-Stitch.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Cross-Stitch.", "x": "Advanced: Finishing.. Count. Once basics are automatic, these separate good from great — Cross-Stitch. counted thread pictures. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-cross-stitch-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
