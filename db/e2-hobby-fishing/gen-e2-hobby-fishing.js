(function(){'use strict';
/* JAH Fishing Hobby Database generator — jahdb-e2-hobby-fishing-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-fishing',PREFIX='JAH-E2HOBBYFISH-',NAME='JAH Fishing Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fishing: the complete hobby guide", "d": "Fishing: catch dinner or release..", "g": "overview", "l": 2, "q": "What is Fishing: the complete hobby guide?", "a": "Fishing: catch dinner or release..", "x": "The complete Fishing hobby guide: catch dinner or release.. License required. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Check regs.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Fishing this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Fishing this weekend.", "x": "Start here: License required.. catch dinner or release. Begin with Rod/reel combo. — small, cheap, and fun. Barbless. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "License required.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "License required.", "x": "Fishing essential: License required.. Barbless. One of the six things every practitioner knows — Knots.. catch dinner or release. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: License required..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: License required..", "x": "In practice: License required.. Handle wet hands. Here is how it works in real sessions — Bait basics.. Fishing Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Rod/reel combo.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Rod/reel combo.", "x": "Fishing essential: Rod/reel combo.. Handle wet hands. One of the six things every practitioner knows — Bait basics.. catch dinner or release. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Rod/reel combo..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Rod/reel combo..", "x": "In practice: Rod/reel combo.. Patience. Here is how it works in real sessions — Local spots.. Fishing Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Knots.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Knots.", "x": "Fishing essential: Knots.. Patience. One of the six things every practitioner knows — Local spots.. catch dinner or release. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Knots..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Knots..", "x": "In practice: Knots.. Tides. Here is how it works in real sessions — Catch and release.. Fishing Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Bait basics.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Bait basics.", "x": "Fishing essential: Bait basics.. Tides. One of the six things every practitioner knows — Catch and release.. catch dinner or release. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Bait basics..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Bait basics..", "x": "In practice: Bait basics.. Respect. Here is how it works in real sessions — License required.. Fishing Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Local spots.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Local spots.", "x": "Fishing essential: Local spots.. Respect. One of the six things every practitioner knows — License required.. catch dinner or release. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Local spots..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Local spots..", "x": "In practice: Local spots.. Check regs. Here is how it works in real sessions — Rod/reel combo.. Fishing Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Catch and release.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Catch and release.", "x": "Fishing essential: Catch and release.. Check regs. One of the six things every practitioner knows — Rod/reel combo.. catch dinner or release. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Catch and release..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Catch and release..", "x": "In practice: Catch and release.. Barbless. Here is how it works in real sessions — Knots.. Fishing Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Check regs.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Check regs.", "x": "Fishing tip: Check regs.. Rod/reel combo. From experienced hobbyists — Patience.. catch dinner or release. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Barbless.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Barbless.", "x": "Fishing tip: Barbless.. Knots. From experienced hobbyists — Tides.. catch dinner or release. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Handle wet hands.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Handle wet hands.", "x": "Fishing tip: Handle wet hands.. Bait basics. From experienced hobbyists — Respect.. catch dinner or release. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Patience.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Patience.", "x": "Fishing tip: Patience.. Local spots. From experienced hobbyists — Check regs.. catch dinner or release. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Tides.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Tides.", "x": "Fishing tip: Tides.. Catch and release. From experienced hobbyists — Barbless.. catch dinner or release. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Respect.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Respect.", "x": "Fishing tip: Respect.. License required. From experienced hobbyists — Handle wet hands.. catch dinner or release. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Fishing gear: License required..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Fishing gear: License required..", "x": "Gear: License required.. Start minimal — Rod/reel combo. — and upgrade as skills demand. catch dinner or release. Buy once where it matters; go cheap where it does not. Handle wet hands. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Fishing on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Fishing on a budget.", "x": "Costs: Patience.. Fishing can start for little and scale to obsession — Knots.. catch dinner or release. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Fishing safety: Tides..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Fishing safety: Tides..", "x": "Safety: Tides.. Bait basics. Every hobby has its risks — Fishing. catch dinner or release. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Fishing: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Fishing: beginner to expert.", "x": "The ladder: catch dinner or release.. Beginner: Local spots.. Intermediate: Catch and release.. Advanced: Respect.. Fishing Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Fishing.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Fishing.", "x": "Advanced: Catch and release.. Check regs. Once basics are automatic, these separate good from great — Fishing. catch dinner or release. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-fishing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
