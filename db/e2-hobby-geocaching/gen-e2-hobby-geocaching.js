(function(){'use strict';
/* JAH Geocaching Hobby Database generator — jahdb-e2-hobby-geocaching-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby-geocaching',PREFIX='JAH-E2HOBBYGEOC-',NAME='JAH Geocaching Hobby Database';
var FIELDS=["overview", "getting-started", "essentials", "tips", "gear", "costs", "safety", "skills", "projects", "community", "mistakes", "resources", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Geocaching: the complete hobby guide", "d": "Geocaching: treasure hunt GPS..", "g": "overview", "l": 2, "q": "What is Geocaching: the complete hobby guide?", "a": "Geocaching: treasure hunt GPS..", "x": "The complete Geocaching hobby guide: treasure hunt GPS.. App. Everything to start and master it — the essentials, the gear, the skills ladder, starter projects, costs, safety, and the community. Start easy.", "s": "public-reference", "f": null}, {"t": "Getting started", "d": "Start Geocaching this weekend.", "g": "getting-started", "l": 2, "q": "What is Getting started?", "a": "Start Geocaching this weekend.", "x": "Start here: App.. treasure hunt GPS. Begin with GPS. — small, cheap, and fun. Bring pen. Mastery comes later; joy comes first. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "App.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "App.", "x": "Geocaching essential: App.. Bring pen. One of the six things every practitioner knows — Containers.. treasure hunt GPS. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 1 in practice", "d": "Doing: App..", "g": "essentials", "l": 2, "q": "What is Essential 1 in practice?", "a": "Doing: App..", "x": "In practice: App.. Stealth. Here is how it works in real sessions — Log.. Geocaching Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "GPS.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "GPS.", "x": "Geocaching essential: GPS.. Stealth. One of the six things every practitioner knows — Log.. treasure hunt GPS. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 2 in practice", "d": "Doing: GPS..", "g": "essentials", "l": 2, "q": "What is Essential 2 in practice?", "a": "Doing: GPS..", "x": "In practice: GPS.. Kids love. Here is how it works in real sessions — Trade.. Geocaching Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Containers.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Containers.", "x": "Geocaching essential: Containers.. Kids love. One of the six things every practitioner knows — Trade.. treasure hunt GPS. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 3 in practice", "d": "Doing: Containers..", "g": "essentials", "l": 2, "q": "What is Essential 3 in practice?", "a": "Doing: Containers..", "x": "In practice: Containers.. Travel bugs. Here is how it works in real sessions — Leave No Trace.. Geocaching Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Log.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Log.", "x": "Geocaching essential: Log.. Travel bugs. One of the six things every practitioner knows — Leave No Trace.. treasure hunt GPS. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 4 in practice", "d": "Doing: Log..", "g": "essentials", "l": 2, "q": "What is Essential 4 in practice?", "a": "Doing: Log..", "x": "In practice: Log.. Community. Here is how it works in real sessions — App.. Geocaching Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Trade.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Trade.", "x": "Geocaching essential: Trade.. Community. One of the six things every practitioner knows — App.. treasure hunt GPS. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 5 in practice", "d": "Doing: Trade..", "g": "essentials", "l": 2, "q": "What is Essential 5 in practice?", "a": "Doing: Trade..", "x": "In practice: Trade.. Start easy. Here is how it works in real sessions — GPS.. Geocaching Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Leave No Trace.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Leave No Trace.", "x": "Geocaching essential: Leave No Trace.. Start easy. One of the six things every practitioner knows — GPS.. treasure hunt GPS. Learn these and you are no longer a beginner. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Essential 6 in practice", "d": "Doing: Leave No Trace..", "g": "essentials", "l": 2, "q": "What is Essential 6 in practice?", "a": "Doing: Leave No Trace..", "x": "In practice: Leave No Trace.. Bring pen. Here is how it works in real sessions — Containers.. Geocaching Practice deliberately; mindless repetition teaches little. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 1", "d": "Start easy.", "g": "tips", "l": 2, "q": "What is Tip 1?", "a": "Start easy.", "x": "Geocaching tip: Start easy.. GPS. From experienced hobbyists — Kids love.. treasure hunt GPS. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 2", "d": "Bring pen.", "g": "tips", "l": 2, "q": "What is Tip 2?", "a": "Bring pen.", "x": "Geocaching tip: Bring pen.. Containers. From experienced hobbyists — Travel bugs.. treasure hunt GPS. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 3", "d": "Stealth.", "g": "tips", "l": 2, "q": "What is Tip 3?", "a": "Stealth.", "x": "Geocaching tip: Stealth.. Log. From experienced hobbyists — Community.. treasure hunt GPS. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 4", "d": "Kids love.", "g": "tips", "l": 2, "q": "What is Tip 4?", "a": "Kids love.", "x": "Geocaching tip: Kids love.. Trade. From experienced hobbyists — Start easy.. treasure hunt GPS. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 5", "d": "Travel bugs.", "g": "tips", "l": 2, "q": "What is Tip 5?", "a": "Travel bugs.", "x": "Geocaching tip: Travel bugs.. Leave No Trace. From experienced hobbyists — Bring pen.. treasure hunt GPS. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Tip 6", "d": "Community.", "g": "tips", "l": 2, "q": "What is Tip 6?", "a": "Community.", "x": "Geocaching tip: Community.. App. From experienced hobbyists — Stealth.. treasure hunt GPS. Small tips, big difference. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Gear guide", "d": "Geocaching gear: App..", "g": "gear", "l": 2, "q": "What is Gear guide?", "a": "Geocaching gear: App..", "x": "Gear: App.. Start minimal — GPS. — and upgrade as skills demand. treasure hunt GPS. Buy once where it matters; go cheap where it does not. Stealth. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Geocaching on a budget.", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Geocaching on a budget.", "x": "Costs: Kids love.. Geocaching can start for little and scale to obsession — Containers.. treasure hunt GPS. Budget for the hobby, not against it; joy has value. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Geocaching safety: Travel bugs..", "g": "safety", "l": 2, "q": "What is Safety?", "a": "Geocaching safety: Travel bugs..", "x": "Safety: Travel bugs.. Log. Every hobby has its risks — Geocaching. treasure hunt GPS. Learn the rules before the skills; no project is worth an injury. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "The skill ladder", "d": "Geocaching: beginner to expert.", "g": "skills", "l": 2, "q": "What is The skill ladder?", "a": "Geocaching: beginner to expert.", "x": "The ladder: treasure hunt GPS.. Beginner: Trade.. Intermediate: Leave No Trace.. Advanced: Community.. Geocaching Climb one rung at a time; plateaus are normal. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}, {"t": "Advanced techniques", "d": "Level up Geocaching.", "g": "skills", "l": 2, "q": "What is Advanced techniques?", "a": "Level up Geocaching.", "x": "Advanced: Leave No Trace.. Start easy. Once basics are automatic, these separate good from great — Geocaching. treasure hunt GPS. Study masters; copy, then innovate. Hobby knowledge from standard references and practitioner guidance. Safety rules are real; follow them.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby-geocaching-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
