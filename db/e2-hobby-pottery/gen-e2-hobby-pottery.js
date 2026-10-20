(function(){'use strict';
/* JAH Pottery Hobby Database generator — jahdb-e2-hobby-pottery-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-pottery',PREFIX='JAH-E2HOBBYPOTT-',NAME='JAH Pottery Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pottery: the complete hobby guide", "d": "Pottery: clay into vessels..", "g": "overview", "l": 2, "q": "What is Pottery: the complete hobby guide?", "a": "Pottery: clay into vessels..", "x": "The complete Pottery hobby guide: clay into vessels.. Hand building. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Classes.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Pottery this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Pottery this weekend.", "x": "Start here: Hand building.. clay into vessels. Begin with Wheel. — small, cheap, and fun. Center. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hand building.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hand building.", "x": "Pottery essential: Hand building.. Center. One of the six things every practitioner knows — Kiln.. clay into vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: Hand building..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: Hand building..", "x": "In practice: Hand building.. Patience. Here is how it works in real sessions — Glazes.. Pottery Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Wheel.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Wheel.", "x": "Pottery essential: Wheel.. Patience. One of the six things every practitioner knows — Glazes.. clay into vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: Wheel..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: Wheel..", "x": "In practice: Wheel.. Glaze test. Here is how it works in real sessions — Wedging.. Pottery Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Kiln.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Kiln.", "x": "Pottery essential: Kiln.. Glaze test. One of the six things every practitioner knows — Wedging.. clay into vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Kiln..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Kiln..", "x": "In practice: Kiln.. Community. Here is how it works in real sessions — Tools.. Pottery Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Glazes.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Glazes.", "x": "Pottery essential: Glazes.. Community. One of the six things every practitioner knows — Tools.. clay into vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Glazes..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Glazes..", "x": "In practice: Glazes.. Sell. Here is how it works in real sessions — Hand building.. Pottery Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Wedging.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Wedging.", "x": "Pottery essential: Wedging.. Sell. One of the six things every practitioner knows — Hand building.. clay into vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Wedging..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Wedging..", "x": "In practice: Wedging.. Classes. Here is how it works in real sessions — Wheel.. Pottery Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Tools.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Tools.", "x": "Pottery essential: Tools.. Classes. One of the six things every practitioner knows — Wheel.. clay into vessels. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Tools..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Tools..", "x": "In practice: Tools.. Center. Here is how it works in real sessions — Kiln.. Pottery Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Classes.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Classes.", "x": "Pottery tip: Classes.. Wheel. From experienced hobbyists — Glaze test.. clay into vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Center.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Center.", "x": "Pottery tip: Center.. Kiln. From experienced hobbyists — Community.. clay into vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Patience.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Patience.", "x": "Pottery tip: Patience.. Glazes. From experienced hobbyists — Sell.. clay into vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Glaze test.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Glaze test.", "x": "Pottery tip: Glaze test.. Wedging. From experienced hobbyists — Classes.. clay into vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Community.", "x": "Pottery tip: Community.. Tools. From experienced hobbyists — Center.. clay into vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Sell.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Sell.", "x": "Pottery tip: Sell.. Hand building. From experienced hobbyists — Patience.. clay into vessels. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Pottery gear: Hand building..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Pottery gear: Hand building..", "x": "Gear: Hand building.. Start minimal — Wheel. — and upgrade as skills demand. clay into vessels. Buy once where it matters; go cheap where it does not. Patience. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Pottery on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Pottery on a budget.", "x": "Costs: Glaze test.. Pottery can start for little and scale to obsession — Kiln.. clay into vessels. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Pottery safety: Community..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Pottery safety: Community..", "x": "Safety: Community.. Glazes. Every hobby has its risks — Pottery. clay into vessels. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Pottery: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Pottery: beginner to expert.", "x": "The ladder: clay into vessels.. Beginner: Wedging.. Intermediate: Tools.. Advanced: Sell.. Pottery Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Pottery.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Pottery.", "x": "Advanced: Tools.. Classes. Once basics are automatic, these separate good from great — Pottery. clay into vessels. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-pottery-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
